class TrelloProvider:
    def __init__(self, board_id, login, password):
        self.board_id = board_id
        self.login = login
        self.password = password

    @staticmethod
    def get_tasks():
        return {
            'actions':
                {
                    'eat': {
                        'plan': ['Mon', 'Tue', 'Wed'],
                        'fact': ['Mon', 'Wed']
                    },
                    'drink': {
                        'plan': ['Mon', 'Wed'],
                        'fact': ['Mon', 'Wed']
                    }
                },
            'start_date': '31.05.2021',
            'end_date': '06.06.2021'
        }

    @staticmethod
    def uncheck_tasks():
        pass
