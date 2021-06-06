from trello import TrelloClient
import config
from const import DATE_FORMAT, DAYS
from datetime import date, timedelta

today = date.today()

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
                  'start_date': (date.today() - timedelta(days=6)).strftime(DATE_FORMAT),
                  'end_date': date.today().strftime(DATE_FORMAT)}
        pull_of_cards = board.get_cards()

        for card in pull_of_cards:
            for el in card.checklists[0].items:
                action = result['actions'].get(el['name'])
                if action is None:
                    action = {'plan': [], 'fact': []}
                    result['actions'][el['name']] = action

                action['plan'].append(DAYS[card.name])
                if el['state'] == 'complete':
                    action['fact'].append(DAYS[card.name])

        return result

    def uncheck_tasks(self):
        board = self._client.get_board(self._board_id)
        for card in board.get_cards():
            for el in card.checklists[0].items:
                if el['state'] == 'complete':
                    card.checklists[0].set_checklist_item(el['name'], False)
