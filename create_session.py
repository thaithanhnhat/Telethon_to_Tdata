from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = "YOUR API-ID"
api_hash = "YOUR API-HASH"
phone ="Your Phone Number"
client = TelegramClient(StringSession(), api_id, api_hash)

async def export_session_to_file(file_path):
    await client.start()
    
    session_string = client.session.save()
    
    with open(file_path, 'w') as file:
        file.write(session_string)
    
    print("Done")


directory_path = os.path.join("AllAccTele", phone)
if phone[0]=="1":
    directory_path = os.path.join("AccTele+1", phone)


os.makedirs(directory_path, exist_ok=True)

file_path = os.path.join(directory_path, f"{phone}.session")

with client:
    client.loop.run_until_complete(export_session_to_file(file_path))

