import telebot


class TrelloBot:
    def __init__(self, auth_token, chat_id):
        self.bot = telebot.TeleBot(auth_token)
        self.chat_id = chat_id

    def send_message(self, message):
        self.bot.send_message(self.chat_id, message)
