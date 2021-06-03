import config
from provider.trelloProvider import TrelloProvider
from storage.trelloTasksStorage import TrelloTasksStorage
from excelMaker.excelMaker import ExcelMaker
from trelloBot.trelloBot import TrelloBot
from scheduler.scheduler import Scheduler


trello_provider = TrelloProvider(config.TRELLO_CONFIG['board_id'],
                                 config.TRELLO_CONFIG['login'],
                                 config.TRELLO_CONFIG['password'])
storage = TrelloTasksStorage()
excel_maker = ExcelMaker()
bot = TrelloBot()
scheduler = Scheduler(trello_provider, storage, excel_maker, bot)
scheduler.run_jobs()
