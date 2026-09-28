import asyncio, os
import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp=Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("EventHub bot. Use /events to see upcoming events.")

@dp.message(Command("events"))
async def events(message: Message):
    base=os.getenv("WEB_URL","http://web:8000")
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base}/api/events/") as response:
            data=await response.json()
    if not data["events"]:
        return await message.answer("No upcoming events.")
    result="\n\n".join(f"Event: {e['title']}\n{e['starts_at']}\nFree places: {e['free_places']}" for e in data["events"])
    await message.answer(result)

async def main():
    token=os.environ["BOT_TOKEN"]
    await dp.start_polling(Bot(token=token))

if __name__=="__main__":
    asyncio.run(main())
