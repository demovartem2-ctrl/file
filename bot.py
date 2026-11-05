import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))
RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    
    if message.photo:
        # Если отправили как обычное фото (сжатое)
        file_id = message.photo[-1].file_id
        await message.reply_text(f"ID фотографии:\n`{file_id}`", parse_mode="Markdown")
        
    elif message.document:
        # Если отправили как файл/документ (как на твоем скриншоте)
        file_id = message.document.file_id
        file_name = message.document.file_name
        await message.reply_text(f"ID документа ({file_name}):\n`{file_id}`", parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Теперь бот реагирует И на фото, И на документы
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.ALL, get_file_id))

    if RENDER_EXTERNAL_URL:
        webhook_url = f"{RENDER_EXTERNAL_URL}/webhook"
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path="webhook",
            webhook_url=webhook_url
        )
    else:
        app.run_polling()

if __name__ == "__main__":
    main()
