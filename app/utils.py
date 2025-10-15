
from app.config import CHAT_HISTORY_FILE

def save_chat_history(user_query, answer):
    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"User: {user_query}\nBot: {answer}\n\n")

