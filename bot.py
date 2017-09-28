import telebot
import config
import parser
import phrases
import emotion_api

# connection to bot by token (got from BotFather)
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, phrases.start_message)


# catch photos
@bot.message_handler(content_types=['photo'])
def get_emotions(message):

    file = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    img = 'https://api.telegram.org/file/bot{}/{}'.format(config.token, file.file_path)

    response = emotion_api.get_emotion(img)
    data = parser.response_parser(response)

    if data == 'error: no faces':
        bot.send_message(message.chat.id, phrases.photo_without_faces_message)
    if data == 'error: more than one person':
        bot.send_message(message.chat.id, phrases.more_than_one_person_message)

    if type(data) == dict:
        answer = ''
        for key in data:
            answer += '{} - {}%\n'.format(phrases.translate[key], data[key])
        bot.send_message(message.chat.id, answer)


@bot.message_handler()
def none_photo(message):
    bot.send_message(message.chat.id, phrases.none_photo_message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
