import os
import asyncio
from pyrogram import Client

async def main():
    api_id = os.environ.get("TELEGRAM_API_ID")
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    phone = os.environ.get("TELEGRAM_PHONE_NUMBER")
    
    client = Client(":memory:", api_id=int(api_id), api_hash=api_hash)
    await client.connect()
    
    try:
        # طلب الرمز فقط
        await client.send_code(phone)
        print("\n" + "="*40)
        print("تم إرسال الرمز بنجاح!")
        print("انتظر الرمز على تليجرام، ثم أعطني إياه.")
        print("="*40 + "\n")
    except Exception as e:
        print(f"خطأ: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
