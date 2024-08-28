from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
import asyncio

api_id = "YOUR API-ID"
api_hash = "YOUR API-HASH"
phone ="Your Phone Number"
async def main():
    if phone[0]=="1":
        with open(rf"AccTele+1\{phone}\{phone}" + '.session', 'r') as file:
            session_string = file.read().strip()
    else:
        with open(rf"AllAccTele\{phone}\{phone}" + '.session', 'r') as file:
            session_string = file.read().strip()
    if not session_string:
        raise ValueError('Khong tim thay session')

   
    client = TelegramClient(StringSession(session_string), api_id, api_hash)

 
    tdesk = await client.ToTDesktop(flag=UseCurrentSession)
    if phone[0]=="1":
          tdesk.SaveTData(rf"AccTele+1\{phone}\tdata")
    else:
         tdesk.SaveTData(rf"AllAccTele\{phone}\tdata")

asyncio.run(main())
