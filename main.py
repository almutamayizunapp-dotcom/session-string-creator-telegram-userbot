import os
import asyncio
from pyrogram import Client

async def main():
    api_id = os.environ.get("TELEGRAM_API_ID")
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    phone = os.environ.get("TELEGRAM_PHONE_NUMBER")
    code = os.environ.get("TELEGRAM_CODE")
    
    client = Client(":memory:", api_id=int(api_id), api_hash=api_hash)
    await client.connect()
    
    try:
        # إرسال طلب الكود مرة أخرى لربطه بالجلسة الحالية
        sent_code = await client.send_code(phone)
        # تسجيل الدخول بالرمز اللي إنت بعته
        await client.sign_in(phone, sent_code.phone_code_hash, code)
        
        string = await client.export_session_string()
        print("\n" + "!"*30)
        print("SUCCESS! YOUR SESSION STRING IS BELOW:")
        print(string)
        print("!"*30 + "\n")
        
    except Exception as e:
        print(f"حدث خطأ: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
