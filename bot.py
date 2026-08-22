import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")  # আপনার টোকেনটি Render-এর Environment Variable থেকে নেবে
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! আপনার বট সফলভাবে চালু হয়েছে।")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
