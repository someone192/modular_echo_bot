from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU


user_router = Router()

@user_router.message(CommandStart())
async def process_start_commands(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

@user_router.message(Command(commands='help'))
async def process_help_commands(message: Message):
    await message.answer(text=LEXICON_RU['/help'])