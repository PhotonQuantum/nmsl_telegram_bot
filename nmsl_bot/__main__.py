import hashlib
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from .nmsl import text_to_emoji

API_TOKEN = os.environ["API_TOKEN"]
PROXY = os.environ.get("PROXY", None)

bot = Bot(token=API_TOKEN, proxy=PROXY)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = text_to_emoji(inline_query.query) or "NMSL"
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        title="NMSL",
        description=text,
        input_message_content=input_content,
    )
    await bot.answer_inline_query(inline_query.id, results=[item])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
