import schedule
import time
import logging
from datetime import date
from const import DATE_FORMAT


class Scheduler:
    def __init__(self, trello_provider, storage, excel_maker, bot, config):
        self.trello_provider = trello_provider
        self.storage = storage
        self.excel_maker = excel_maker
        self.bot = bot
        self.config = config
        self._logger = logging.getLogger('Scheduler')
        self._logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self._logger.addHandler(ch)

    def _send_report(self):
        self._logger.info('Collecting data from is starting...')
        tasks_dict = self.trello_provider.get_tasks()
        self._logger.debug('Collecting data from has finished')

        self._logger.debug('Saving data into mongo is starting...')
        self.storage.save_tasks(tasks_dict)
        self._logger.debug('Saving data into mongo has finished...')

        self._logger.debug('Unchecking trello is starting...')
        self.trello_provider.uncheck_tasks()
        self._logger.debug('Unchecking trello has finished')

        self._logger.debug('Fetching data from mongo is starting...')
        tasks_db = self.storage.get_tasks()
        self._logger.debug('Fetching data from mongo has finished')

        filename = 'result_' + date.today().strftime(DATE_FORMAT) + '.xlsx'

        self._logger.debug('Filling excel is starting...')
        self.excel_maker.convert_in_excel(tasks_db, filename)
        self._logger.debug('Filling excel has finished')

        self._logger.debug('Sending report is starting...')
        self.bot.send_file(filename)
        self._logger.debug('Sending report has finished')

    def run_jobs(self):
        schedule.every().sunday.at(self.config.SCHEDULER_TIME_REPORT).do(self._send_report)
        while True:
            schedule.run_pending()
            time.sleep(1)
