from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/f483b492adb7796fd7224.jpg")
    await message.reply_text(
        f"""**Hey, I'm AMELIA MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [RUPAYAN🤠](https://t.me/Rupayan_Iz_Here)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📠 Source Code 📠", url="https://t.me/Empire_Support21")
                  ],[
                    InlineKeyboardButton(
                        "📢 SUPPORT GROUP 📢", url="https://t.me/Empire_Support21"
                    ),
                    InlineKeyboardButton(
                        "🔰 COMMAND 🔰", url="https://t.me/Empire_Network"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❤ ADD ME TO YOUR GROUP ❤", url="http://t.me/AmeliaMusic_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#EMPIRE_WARRIORS_ON_FIRE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 COMMANDS 🔰", url="https://t.me/Empire_Network")
                ]
            ]
        )
   )


