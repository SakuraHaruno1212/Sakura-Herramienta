import requests
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO)

TOKEN = "8540373327:AAFbUoSlhW3GPFpNzKC2Xq2RNd8TxzbRJHo"

def reportar_usuario(chat_id, usuario_a_reportar):
    url = f"https://api.telegram.org/bot{TOKEN}/reportChat"
    data = {
        "chat_id": usuario_a_reportar,
        "reason": "SPAM"
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return "Usuario reportado"
    else:
        return f"Error reportando usuario: {response.text}"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido al bot de reporte de usuarios")

def reportar(update, context):
    if len(context.args) > 0:
        usuario_a_reportar = context.args[0]
        resultado = reportar_usuario(update.effective_chat.id, usuario_a_reportar)
        context.bot.send_message(chat_id=update.effective_chat.id, text=resultado)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Debes proporcionar el ID del usuario a reportar")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reportar", reportar))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
