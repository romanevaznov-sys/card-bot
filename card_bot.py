import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

# Веб-сервер для удержания порта Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# Твой основной код бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "9289461046:AAMxMqsf85NZH9Qa1bywppDo-WBTMZ8")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    text = (
        "<b>⚠️ ПОМНИ ДРУЗЬЯ: ВСЕ И В ЭТОЙ СФЕРЕ СКАМ, ТОЛЬКО SAMPERLIFE ПЛАТИТ! ТО ЕСТЬ Я.</b>\n\n"
        "<b>*Близко к самым честным гарантам. В Telegram ссылок **НЕ ВЕДУ** — здесь сплошной скам!*</b>\n"
        "<b>"Все переписки, сделки и выплаты веду строго через:"</b>\n\n"
        "👉 <b>WhatsApp</b>\n"
        "👉 <b>Discord</b>\n\n"
        "<b>🎁 *АКЦИЯ ДРУЗЬЯ:* Пригласи друга и получи **100 рублей** за каждого успешного типа!</b>"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать в WhatsApp", url="https://wa.me/8944682980")],
        [InlineKeyboardButton(text="💬 Написать в Discord", url="https://discord.com/users/skup55")],
        [InlineKeyboardButton(text="▶️ YouTube", url="https://www.youtube.com/@SamperLife/featured")],
        [InlineKeyboardButton(text="🎵 TikTok", url="https://www.tiktok.com/@skuptapuskinskihcart")]
    ])

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        print(f"Вебхук пропущен: {e}")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
