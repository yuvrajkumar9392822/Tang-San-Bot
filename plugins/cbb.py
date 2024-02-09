#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>✨ Creator : <a href='tg://user?id={OWNER_ID}'>Tang San</a>\n✨ Country : <code>India</code>\n✨ YouTube : <a href='https://youtube.com/@mehdreaming'>Meh Dreaming</a>\n✨ Instagram : <a href='https://www.instagram.com/mehdreaming'>@mehdreaming</a>\n✨ Channel : @hindidonghua\n✨ Support Group : @hindidonghuasupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
