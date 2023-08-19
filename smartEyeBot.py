from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,ContextTypes
import Cons as keys
import test as t

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')



async def handle_message(update: Update, context):
    text = update.message.text.lower()
    response = bot = t.TelegramBot(t.token, t.chat_id).handle_command(text)
    await update.message.reply_text(response)

def error(update: Update, context):
    print(f"Update {update} caused error {context.error}")


app = ApplicationBuilder().token(keys.API_KEY).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(None, handle_message))
app.add_error_handler(error)

app.run_polling()
