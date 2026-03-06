import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

mensajes = [
    """En memoria de {nombre}, informamos con profundo dolor su fallecimiento. 🕊️💔
Solicitamos respetuosamente a Facebook que este perfil sea convertido en una cuenta conmemorativa oficial, para preservar su legado y permitir que familiares y amigos continúen honrando su memoria.
Su recuerdo vivirá eternamente en nuestros corazones. 🥀🙏""",

    """Con gran tristeza anunciamos la partida de {nombre}. 💔🕊️
Pedimos formalmente que esta cuenta sea transformada en conmemorativa, para que permanezca como un espacio de respeto, amor y recuerdo.
Gracias a todos por acompañarnos en este difícil momento. 🤍""",

    """Hoy despedimos a {nombre}, quien dejó una huella imborrable en nuestras vidas. 🖤🕊️
Solicitamos que su perfil sea memorializado para conservar sus fotografías, publicaciones y recuerdos como parte de su legado digital.
Que descanse en paz. 🙏🥀""",

    """En honor a {nombre}, pedimos que esta cuenta sea convertida en memorial para que amigos y familiares puedan seguir compartiendo mensajes de cariño y homenaje.
Su luz seguirá brillando en cada recuerdo. 🕯️🤍"""
]

async def conmemorar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        nombre = " ".join(context.args)
    else:
        nombre = "Nombre Completo"

    mensaje = random.choice(mensajes).format(nombre=nombre)
    await update.message.reply_text(mensaje)

app = ApplicationBuilder().token("8540373327:AAFbUoSlhW3GPFpNzKC2Xq2RNd8TxzbRJHo").build()

app.add_handler(CommandHandler("conmemorar", conmemorar))

print("Bot activo...")
app.run_polling()
