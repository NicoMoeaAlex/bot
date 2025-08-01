from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración del Bot (reemplaza con tu token real)
TOKEN = "8457834938:AAFRj2tRX4DMeQjW4V2XAER1lbATsVe4zqo"  # ⚠️ Obtén uno de @BotFather en Telegram

# Función para manejar /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Soy un bot automatizado. Gracias por estar aquí. 😊")

# Función principal
def main() -> None:
    # Crear la aplicación del bot
    application = Application.builder().token(TOKEN).build()

    # Registrar comandos
    application.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    print("✅ Bot en funcionamiento... Presiona Ctrl + C para detenerlo.")
    application.run_polling()  # Bloquea hasta que se detenga el bot

if __name__ == "__main__":
    main()  # No se usa asyncio.run() para evitar conflictos