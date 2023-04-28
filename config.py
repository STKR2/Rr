"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5249489492:AAFEuC8rLTz-ticTrf_7OLE0QYzoUNCOewY")
SESSION_STRING = getenv("SESSION_STRING", "BACIVfMAs0JxAI8WxNI7p4H03zmjZjqdgLmOmB_zxc9ge6Vpd0sO3DfL9a3azboec3kErwDtpJXwrQqtgl97uDfCgH9C5rJkgP2ZiajdLZcPErHCcf2ED1gESl-lgVrOhziWyTShmuroyK99EK1ztR6kOt3mBZXMaJs6HWpH5dphGkJNTDFrcXc4_U5uPUO1gpQB5ssdwZILdbo78SJ88LnNcL7oiIVlb_cmSuRzoKgOhk9Q6EkVjDDKifRSR83v75jsNFB2V4u-PVgK--gN5qsh2mf_ax2zCsQGR9Tq33Rg1IiPwqYlceSNUK_Db-rAnb4ounqJMS0FA3N3CcnpXD6pVUT8lAAAAAF13-NdAA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VVRVV3")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", " ")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
