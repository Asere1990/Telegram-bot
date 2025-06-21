import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7898142673:AAHSHjtleMrgdi_ZOduDu-RHc3V4x6B5KqAA'
CHAT_ID = '@jineteras'
IMAGE_URL = 'https://i.postimg.cc/MGQf6tKG/IMG-8234.jpg'

bot = telebot.TeleBot(TOKEN)

def botonera_para_canal():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url="https://t.me/share/url?url=https://t.me/jineteras"),
        InlineKeyboardButton("¿𝐂𝐨́𝐦𝐨 𝐝𝐞𝐬𝐛𝐥𝐨𝐪𝐮𝐞𝐚𝐫?", url="https://t.me/jinetera_bot?start=como_desbloquear")
    )
    return markup

def botonera_para_privado():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url="https://t.me/share/url?url=https://t.me/jineteras"),
        InlineKeyboardButton("¿𝐂𝐨́𝐦𝐨 𝐝𝐞𝐬𝐛𝐥𝐨𝐪𝐮𝐞𝐚𝐫?", callback_data="mostrar_popup")
    )
    return markup

bot.send_photo(
    chat_id=CHAT_ID,
    photo=IMAGE_URL,
    caption="🇨🇺𝐂𝐀𝐍𝐀𝐋 𝐏𝐑𝐈𝐕𝐀𝐃𝐎 𝐏𝐀𝐑𝐀 𝐀𝐃𝐔𝐋𝐓𝐎𝐒🔞",
    reply_markup=botonera_para_canal()
)

@bot.message_handler(commands=['start'])
def start_handler(message):
    if 'como_desbloquear' in message.text:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=IMAGE_URL,
            caption="🇨🇺𝐂𝐀𝐍𝐀𝐋 𝐏𝐑𝐈𝐕𝐀𝐃𝐎 𝐏𝐀𝐑𝐀 𝐀𝐃𝐔𝐋𝐓𝐎𝐒🔞",
            reply_markup=botonera_para_privado()
        )

@bot.callback_query_handler(func=lambda call: call.data == "mostrar_popup")
def mostrar_popup(call):
    bot.answer_callback_query(
        callback_query_id=call.id,
        text="Presione DESBLOQUEAR y seleccione 3 GRANDES GRUPOS.",
        show_alert=True
    )

bot.polling()
