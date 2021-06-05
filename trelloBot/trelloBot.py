import telebot
import json



class TrelloBot:
    def __init__(self, auth_token, chat_id):
        self.bot = telebot.TeleBot(auth_token)
        self.chat_id = chat_id

    def send_file(self, filePath):
        doc = open(filePath, 'rb')
        self.bot.send_document(self.chat_id, doc)
