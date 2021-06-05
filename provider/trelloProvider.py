from trello import TrelloClient

BOARD_ID = "Ql9mg3Lg"

class TrelloProvider:
    def __init__(self, config):
        self._board_id = config['board_id']
        self._client = TrelloClient(
            api_key=config['api_key'],
            api_secret=config['api_secret'],
            token=config['token'],
            token_secret=config['token_secret']
        )

    def get_tasks(self):
        board = self._client.get_board(self._board_id)
        for card in board.get_cards():
            print(card.name)

    @staticmethod
    def uncheck_tasks():
        pass
