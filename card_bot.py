import asyncio
import logging
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bots are running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

logging.basicConfig(level=logging.INFO)

# --- Конфигурация ботов ---
BOT_TOKEN_1 = "9289461046:AAGWsNqsf05MZh9Qa1IbywbppDo-mMBTN90"
bot1 = Bot(token=BOT_TOKEN_1)
dp1 = Dispatcher()

SECOND_BOT_TOKEN = "9026300591:AAFXAm82-LhYIcuM_m5CzD6WC9mTyCB3ZSI"
bot2 = Bot(token=SECOND_BOT_TOKEN)
dp2 = Dispatcher()

# --- Общий текст для обоих ботов ---
BOT_TEXT = (
    "⚠️ ПОМНИ ДРУЖИЩЕ: ВСЕ В ЭТОЙ СФЕРЕ СКАМ, ТОЛЬКО SAMPERLIFE ПЛАТИТ! ТО ЕСТЬ Я.\n\n"
    "Являюсь единственным честным скупом номер 1. В Telegram сделки НЕ ВЕДУ — здесь сплошной скам!\n"
    "Все переписки, сделки и выплаты веду строго через:\n"
    "• WhatsApp\n"
    "• Discord\n\n"
    "🎁 АКЦИЯ ДО 1 ЯНВАРЯ: Пригласи друга и получи 100 рублей за каждого!"
)

KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💬 Написать в WhatsApp", url="https://wa.me/8944682980")],
    [InlineKeyboardButton(text="🎮 Написать в Discord", url="https://discord.com/users/skupt55")],
    [InlineKeyboardButton(text="▶️ YouTube (КЛИКНИ И УДОСТОВЕРЬСЯ САМ)", url="https://www.youtube.com/@SamperLife/featured")],
    [InlineKeyboardButton(text="🎵 TikTok (КЛИКНИ И УДОСТОВЕРЬСЯ САМ)", url="https://www.tiktok.com/@skuptapuskinskihcart")]
])

@dp1.message(CommandStart())
async def start_cmd_bot1(message: types.Message):
    await message.answer(BOT_TEXT, reply_markup=KEYBOARD)

@dp2.message(CommandStart())
async def start_cmd_bot2(message: types.Message):
    await message.answer(BOT_TEXT, reply_markup=KEYBOARD)

async def main():
    try:
        await bot1.delete_webhook(drop_pending_updates=True)
        await bot2.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        print(f"Ошибка сброса вебхука: {e}")

    await asyncio.gather(
        dp1.start_polling(bot1),
        dp2.start_polling(bot2)
    )

if __name__ == "__main__":
    asyncio.run(main())
