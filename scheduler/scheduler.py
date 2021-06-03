class Scheduler:
    def __init__(self, trello_provider, storage, excel_maker, bot):
        self.trello_provider = trello_provider
        self.storage = storage
        self.excel_maker = excel_maker
        self.bot = bot
    
    def run_jobs(self):
        tasks_dict = self.trello_provider.get_tasks()
        self.storage.save_tasks()
        self.trello_provider.uncheck_tasks()
        self.tasks_excel = self.excel_maker.convert_in_excel(tasks_dict)
        self.bot.send_message(self.tasks_excel)
