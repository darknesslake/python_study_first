import telebot
from telebot import types
import private.telegram_token as tg_token

# Замените 'YOUR_BOT_TOKEN' на ваш токен, полученный от BotFather
bot = tg_token.bot

# Приветствие для новых участников
@bot.message_handler(content_types=['new_chat_members'])
def greet_new_member(message):
    for new_member in message.new_chat_members:
        bot.reply_to(message, f"Привет, {new_member.first_name}! Добро пожаловать в нашу группу!")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который приветствует новых участников. \n"
                          "Если вы только что присоединились к группе, я уже вас поприветствовал. \n"
                          "Если вам нужна помощь, обратитесь к администраторам группы.")



# Запуск бота
bot.polling(none_stop=True)