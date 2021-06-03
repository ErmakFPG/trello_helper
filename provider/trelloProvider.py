class TrelloProvider:
    def __init__(self, board_id, login, password):
        self.board_id = board_id
        self.login = login
        self.password = password
    
    @staticmethod
    def get_tasks():
        return {}
    
    @staticmethod
    def uncheck_tasks():
        pass