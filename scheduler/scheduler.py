import schedule
import time


class Scheduler:
    def __init__(self, trello_provider, storage, excel_maker, bot, config):
        self.trello_provider = trello_provider
        self.storage = storage
        self.excel_maker = excel_maker
        self.bot = bot
        self.config = config
    
    def _send_report(self):
        tasks_dict = self.trello_provider.get_tasks()
        self.storage.save_tasks(tasks_dict)
        self.trello_provider.uncheck_tasks()
        tasks_db = self.storage.get_tasks()
        tasks_excel = self.excel_maker.convert_in_excel(tasks_db)
        self.bot.send_message(tasks_excel)

    def run_jobs(self):
        schedule.every().friday.at(self.config.SCHEDULER_TIME_REPORT).do(self._send_report)
        while True:
            schedule.run_pending()
            time.sleep(1)