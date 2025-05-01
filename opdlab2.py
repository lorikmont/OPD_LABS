import requests
import logging
from aiogram import Bot, Dispatcher, executor, types

def get_giphy_image():
    url = f"https://api.giphy.com/v1/gifs/random"
    params = {
        "api_key": 'Gdmx42u3B57MNXRGfpDO43TkCkA0gNwS',
        "tag": 'motivation',
        "rating": "g"
    }
    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["images"]["original"]["url"]
    return None


API_TOKEN = '7779519184:AAF7edvc430Z_ljj5qOaalTFoXW0HnRZN_0'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Доброго времени суток! Я EsDeathDog, ваш личный мотиватор! Скажите мне если вам нужна мотивация.")


@dp.message_handler(lambda message: "мотивац" in message.text.lower())
async def button1_handler(message: types.Message):
    await message.answer_animation(get_giphy_image())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

