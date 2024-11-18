# TelegramBot_Cleaner
This bot helps keep group chats clean by removing unnecessary messages.

### Описание.

**Этот бот помогает поддерживать чистоту в групповых чатах, удаляя ненужные сообщения.**

**Сценарий использования:**  
Вы создали группу с друзьями, чтобы делиться важной информацией и ссылками, но иногда обсуждения начинают отвлекать и теряют смысловую ценность. В итоге вам приходится вручную удалять десятки сообщений, чтобы сохранить порядок. Этот бот автоматизирует процесс: он отслеживает сообщения в чате и сохраняет в базу данных все сообщения без тега `#info`. По команде бот очищает группу, удаляя все сообщения без этого тега.

**ВАЖНО:**  
Бот **НЕ отправляет ваши данные куда-либо**. Вы можете сами проверить это, изучив исходный код.

---

**Как запустить бота:**  
Есть два варианта:  
1. **Через Docker:** (рекомендуется)  
   В будущем будет добавлена готовая конфигурация для запуска.  
2. **Без Docker (только для Linux):**  
   - Изолируйте папку с кодом бота.  
   - Настройте его автономную работу в системе с помощью Linux-демона.  
   Команды для создания и запуска демона находятся в файле инструкции.  
   (Этот способ немного сложнее, поэтому лучше использовать Docker.)

---

### Edited text in English:

**This bot helps keep group chats clean by removing unnecessary messages.**

**Usage scenario:**  
You’ve created a group with friends to share important information and links, but sometimes discussions derail and lose their informational value. You end up manually deleting dozens of messages to keep things tidy. This bot automates the process: it monitors chat messages and stores all messages without the `#info` tag in a database. With a single command, the bot cleans up the group by deleting all messages without this tag.

**IMPORTANT:**  
The bot **does NOT send your data anywhere**. You can verify this by reviewing the source code.

---

**How to run the bot:**  
There are two options:  
1. **Using Docker:** (recommended)  
   A ready-to-use configuration will be added later.  
2. **Without Docker (Linux only):**  
   - Isolate the directory containing the bot’s code.  
   - Configure it to run autonomously on your system using a Linux daemon.  
   Commands to set up and run the daemon are provided in the instruction file.  
   (This method is slightly more complex, so Docker is preferred.)  
