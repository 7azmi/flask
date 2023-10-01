from flask import Flask, request, jsonify
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

app = Flask(__name__)

# Your Telegram Bot API Token
TELEGRAM_API_TOKEN = "6088899662:AAGP8lQ9GixY3UVjmMwK4idtZBnCY030lSE"

# Initialize the Telegram Bot
bot = telegram.Bot(token=TELEGRAM_API_TOKEN)


@app.route('/')
def index():
    return jsonify({"Working :)})


@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if update.message:
        user_id = update.message.chat.id
        message_text = update.message.text

        # Process the incoming message and send a response
        response_text = f"You said: {message_text}"
        bot.send_message(chat_id=user_id, text=response_text)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
