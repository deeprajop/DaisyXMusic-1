# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 ᴛʜɪs ɪs ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶, ɪ ʜᴀᴠᴇ ʟᴏᴛs ᴛᴏ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ɪɴʙᴜɪʟᴛ! ᴛʜɪs ɪs ᴛʜᴇ ᴍᴏsᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ʙᴏᴛ ᴛʜᴀᴛ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ\n\n✔️ sᴇɴᴅ /help ғᴏʀ ᴍᴏʀᴇ ᴍᴏʀᴇ ɪɴғᴏ"
      HELP_MSG = [
        ".",
f"""
**ʜᴇʏ 👋 ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶**

>> ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀs ᴡᴇʟʟ ᴀs ᴄʜᴀɴɴᴇʟ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs

>> ᴀssɪsᴛᴀɴᴛ ɴᴀᴍᴇ: @Zer0ByteAssistant2
""",

f"""
**ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 sᴇᴛᴛɪɴɢ ᴜᴘ!**
 >> **ғᴏʀ ɢʀᴏᴜᴘs**
𝟷. ᴍᴀᴋᴇ ʙᴏᴛ ᴀᴅᴍɪɴ (ɢʀᴏᴜᴘ ᴀɴᴅ ɪɴ ᴄʜᴀɴɴᴇʟ ɪғ ᴜsᴇ ᴄᴘʟᴀʏ)
𝟸. sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
𝟹. ᴛʀʏ /play [sᴏɴɢ ɴᴀᴍᴇ] ғᴏʀ ᴛʜᴇ ғɪʀsᴛ ᴛɪᴍᴇ ʙʏ ᴀɴ ᴀᴅᴍɪɴ
𝟺. ɪғ ᴜsᴇʀʙᴏᴛ ᴊᴏɪɴᴇᴅ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ, ɪғ ɴᴏᴛ ᴀᴅᴅ @Zer0ByteAssistant2 ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ʀᴇᴛʀʏ!

 >>ғᴏʀ ᴄʜᴀɴɴᴇʟ
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 
𝟸. sᴇɴᴅ /userbotjoinchannel ɪɴ ʟɪɴᴋᴇᴅ ɢʀᴏᴜᴘ
𝟹. ɴᴏᴡ sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ʟɪɴᴋᴇᴅ ɢʀᴏᴜᴘ

**ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ᴄᴏᴍᴍᴀɴᴅs ʟᴏᴀᴅᴇᴅ**

 >>**sᴏɴɢs ʟᴏᴀᴅᴇᴅ**

• /play: ᴘʟᴀʏ sᴏɴɢ ᴜsɪɴɢ ʏᴏᴜᴛᴜʙᴇ ᴍᴜsɪᴄ
• /play [ʏᴛ ᴜʀʟ] : ᴘʟᴀʏ ᴛʜᴇ ɢɪᴠᴇɴ ʏᴛ ᴜʀʟ
• /play [ʀᴇᴘʟʏ ʏᴏ ᴀᴜᴅɪᴏ]: ᴘʟᴀʏ ʀᴇᴘʟɪᴇᴅ ᴀᴜᴅɪᴏ
• /dplay: ᴘʟᴀʏ sᴏɴɢ ᴠɪᴀ ᴅᴇᴇᴢᴇʀ
• /splay: ᴘʟᴀʏ sᴏɴɢ ᴠɪᴀ ᴊɪᴏ sᴀᴀᴠɴ
- /ytplay: ᴅɪʀᴇᴄᴛʟʏ ᴘʟᴀʏ sᴏɴɢ ᴠɪᴀ ʏᴏᴜᴛᴜʙᴇ ᴍᴜsɪᴄ

 >>**ᴘʟᴀʏʙᴀᴄᴋ ʟᴏᴀᴅᴇᴅ**

• /player: ᴏᴘᴇɴ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ ᴏғ ᴘʟᴀʏᴇʀ
• /skip: sᴋɪᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ
• /pause: ᴘᴀᴜsᴇ ᴛʀᴀᴄᴋ
• /resume: ʀᴇsᴜᴍᴇs ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴛʀᴀᴄᴋ
• /end:sᴛᴏᴘs ᴍᴇᴅɪᴀ ᴘʟᴀʏʙᴀᴄᴋ
• /current: sʜᴏᴡs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ
• /playlist: sʜᴏᴡs ᴘʟᴀʏʟɪsᴛ

⚠️ᴘʟᴀʏᴇʀ ᴄᴍᴅ ᴀɴᴅ ᴀʟʟ ᴏᴛʜᴇʀ ᴄᴍᴅs ᴇxᴄᴇᴘᴛ /play, /current and /playlist  ᴀʀᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
""",
        
f"""
 >>**ᴄʜᴀɴɴᴇʟ ᴍᴜsɪᴄ ᴄᴏᴍᴍᴀɴᴅs ʟᴏᴀᴅᴇᴅ**

⦾ ғᴏʀ ʟɪɴᴋᴇᴅ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ᴏɴʟʏ:

- /cplay [sᴏɴɢ ɴᴀᴍᴇ] - ᴘʟᴀʏ sᴏɴɢ ʏᴏᴜ ʀᴇǫᴜᴇsᴛᴇᴅ
- /cdplay [sᴏɴɢ ɴᴀᴍᴇ] - ᴘʟᴀʏ sᴏɴɢ ʏᴏᴜ ʀᴇǫᴜᴇsᴛᴇᴅ ᴠɪᴀ ᴅᴇᴇᴢᴇʀ
- /csplay [sᴏɴɢ ɴᴀᴍᴇ] - ᴘʟᴀʏ sᴏɴɢ ʏᴏᴜ ʀᴇǫᴜᴇsᴛᴇᴅ ᴠɪᴀ ᴊɪᴏ sᴀᴀᴠɴ
- /cplayist - sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏɪɴɢ ʟɪsᴛ
- /ccurrent - sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏɪɴɢ
- /cplayer - ᴏᴘᴇɴ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴇᴛᴛɪɴɢs ᴘᴀɴᴇʟ
- /cpause - ᴘᴀᴜsᴇ sᴏɴɢ ᴘʟᴀʏ
- /cresume - ʀᴇsᴜᴍᴇ sᴏɴɢ ᴘʟᴀʏ
- /cskip - ᴘʟᴀʏ ɴᴇxᴛ sᴏɴɢ
- /cend - sᴛᴏᴘ ᴍᴜsɪᴄ ᴘʟᴀʏ
- /userbotjoinchannel - ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ

⚠️ᴄʜᴀɴɴᴇʟ ɪs ᴀʟsᴏ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ɪɴsᴛᴇᴀᴅ ᴏғ ᴄ ( /ᴄᴘʟᴀʏ = /ᴄʜᴀɴɴᴇʟᴘʟᴀʏ )

⦾ ɪᴅ ʏᴏᴜ ᴅᴏɴᴛ ʟɪᴋᴇ ᴛᴏ ᴘʟᴀʏ ɪɴ ʟɪɴᴋᴇᴅ ɢʀᴏᴜᴘ ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ʜᴀs ᴀ sᴏʟᴜᴛɪᴏɴ:

𝟷. ɢᴇᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪᴅ.
𝟸. ᴄʀᴇᴀᴛᴇ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴛɪᴛᴛʟᴇ: ᴄʜᴀɴɴᴇʟ ᴍᴜsɪᴄ: ʏᴏᴜʀ_ᴄʜᴀɴɴᴇʟ_ɪᴅ
𝟹. ᴀᴅᴅ ʙᴏᴛ ᴀs ᴄʜᴀɴɴᴇʟ ᴀᴅᴍɪɴ ᴡɪᴛʜ ғᴜʟʟ ᴘᴇʀᴍs
𝟺. ᴀᴅᴅ @Zer0ByteAssistant2 ᴛᴏ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀs ᴀɴ ᴀᴅᴍɪɴ.
𝟻. sɪᴍᴘʟʏ sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
""",

f"""
 >>**ᴍᴏʀᴇ ᴛᴏᴏʟs ʟᴏᴀᴅᴇᴅ**

- /reload: ᴜᴘᴅᴀᴛᴇs ᴀᴅᴍɪɴ ɪɴғᴏ ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴛʀʏ ᴏɴʟʏ ɪғ ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇsɴᴛ ʀᴇᴄᴏɢɴɪsᴇ ʏᴏᴜ ᴀs ᴀɴ ᴀᴅᴍɪɴ!
- /userbotjoin: ɪɴᴠɪᴛᴇs ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴠᴏɪᴄᴇ's ᴄʜᴀᴛ

 >>**ᴄᴏᴍᴍᴀɴᴅs ʟᴏᴀᴅᴇᴅ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs!**

 - /userbotleaveall - ʀᴇᴍᴏᴠᴇᴀ ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ᴀssɪsᴛᴀɴᴛ ғʀᴏᴍ ᴀʟʟ ᴄʜᴀᴛs! ғᴜᴋ ɪᴛ.
 - /gcast  - ɢʟᴏʙᴀʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴢᴇʀ𝟶ʙʏᴛᴇ 𝟸.𝟶 ɴᴇᴡ ᴜᴘᴅᴀᴛᴇs.
 - /pmpermit [on/off] - ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴛʜᴇsᴇ ɢᴏ ᴀɴᴅ ʟɪsᴛᴇɴ ᴍᴜsɪᴄ .
⚠️ɴᴏᴛᴇ:- sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴀɴʏ ɢʀᴏᴜᴘs ʙᴇ ᴀᴡᴀʀᴇ ᴏғ ᴛʜᴇᴍ!
"""
      ]
