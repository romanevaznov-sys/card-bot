import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN", "9289461046:AAGWsNqsf05MZh9Qa1IbywbppDo-mMBTN90")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: Message):
    text = (
        "<b>⚠️ ПОМНИ ДРУЖИЩЕ: ВСЕ В ЭТОЙ СФЕРЕ СКАМ, ТОЛЬКО SAMPERLIFE ПЛАТИТ! ТО ЕСТЬ Я.</b>\n\n"
        "Являюсь единственным честным гарантом. В Telegram сделки **НЕ ВЕДУ** — здесь сплошной скам!\n"
        "Все переписки, сделки и выплаты веду строго через:\n"
        "• <b>WhatsApp</b>\n"
        "• <b>Discord</b>\n\n"
        "🎁 **АКЦИЯ ДРУЖИЩЕ:** Пригласи друга и получи **100 рублей** за каждого успешного типа!"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать в WhatsApp", url="https://wa.me/89940602988")],
        [InlineKeyboardButton(text="🎮 Написать в Discord", url="https://discord.com/users/skup55")],
        [InlineKeyboardButton(text="📺 YouTube", url="https://www.youtube.com/@SamperLife/featured")],
        [InlineKeyboardButton(text="🎵 TikTok", url="https://www.tiktok.com/@skupkapuskinskihcart")]
    ])
    
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        print(f"Вебхук пропущен: {e}")
        
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())