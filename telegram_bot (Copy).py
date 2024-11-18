import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.error import BadRequest

# Задайте ваш токен
TOKEN = '...'
# Задайте ID вашей группы
GROUP_ID = ...

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    # Создаем таблицу для хранения сообщений
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

# Сохранение ID сообщения в базу данных
def save_message_id(message_id):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message_id) VALUES (?)', (message_id,))
    conn.commit()
    conn.close()

# Получение всех ID сообщений из базы данных
def get_message_ids():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT message_id FROM messages')
    message_ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return message_ids

# Очистка всех записей из базы данных после удаления сообщений
def clear_message_ids():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM messages')
    conn.commit()
    conn.close()

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Бот запущен и готов к работе!')

async def cleanup(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    if chat_id != GROUP_ID:
        await update.message.reply_text('Эта команда доступна только в указанной группе.')
        return
        
    # Сначала удаляем команду /cleanup
    try:
        await update.message.delete()
    except Exception as e:
        await update.message.reply_text(f'Ошибка при удалении команды /cleanup: {e}')

    message_ids = get_message_ids()
    
    # Удаление сообщений по ID из базы данных
    for message_id in message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception as e:
            print(f'Ошибка при удалении сообщения: {e}')
            
        # Независимо от успеха или неудачи, удаляем запись из базы данных
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM messages WHERE message_id = ?', (message_id,))
        conn.commit()
        conn.close()

    # Очистить базу данных после удаления
    # await update.message.reply_text(f'Очистка бд: {e}')
    # clear_message_ids()

async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    if chat_id != GROUP_ID:
        return

    # Сохраняем ID сообщений для последующей проверки
    if not update.message.text.endswith('#info'):
        save_message_id(update.message.message_id)

def main() -> None:
    init_db()  # Инициализируем базу данных
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('cleanup', cleanup))
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()


