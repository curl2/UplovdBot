import requests as req
import telebot
import os

bot = telebot.TeleBot('1314192743:AAG6cPgEweSDZevEO1EUaGCE4f2Rah_6mkk')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, перешли или загрузи файл и я залью его на uplovd.com")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Перешли или загрузи файл, и я залью его на uplovd.com!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
@bot.message_handler(content_types=['document'])
def get_file_tg(message):
    file_name = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    with open("file/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.from_user.id, "Скачал!")
    files = {'file': open('file/'+src, 'rb')}
    r = req.post("https://api.uplovd.com/upload", files=files)
    os.system("rm file/"+src)
    bot.send_message(message.from_user.id, r)
bot.polling(none_stop=True, interval=0)
