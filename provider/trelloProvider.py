from trello import TrelloClient
import config

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
        result = {'actions': {},
                  'time_start': None,
                  'time_end': None}
        actions_set = []
        pull_of_cards = board.get_cards()

        for card in pull_of_cards:
            for el in card.fetch_checklists()[0].items:
                actions_set.append(el['name'])
        actions_set = set(actions_set)

        for action in actions_set:
            result['actions'][action] = {'plan': [], 'fact': []}

        for card in pull_of_cards:
            for el in card.fetch_checklists()[0].items:
                result['actions'][el['name']]['plan'].append(card.name)
                if el['state'] == 'complete':
                    result['actions'][el['name']]['fact'].append(card.name)

        return result

    def uncheck_tasks(self):
        board = self._client.get_board(self._board_id)
        for card in board.get_cards():
            for el in card.fetch_checklists()[0].items:
                card.checklists[0].set_checklist_item(el['name'], False)


trello_provider = TrelloProvider(config.TRELLO_CONFIG)
trello_provider.get_tasks()
trello_provider.uncheck_tasks()
