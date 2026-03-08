import os
import asyncio
from pyrogram import Client

async def main():
    api_id = os.environ.get("TELEGRAM_API_ID")
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    phone = os.environ.get("TELEGRAM_PHONE_NUMBER")
    input_code = os.environ.get("INPUT_CODE")
    
    client = Client(":memory:", api_id=int(api_id), api_hash=api_hash)
    await client.connect()
    
    if not input_code:
        # المرة الأولى: نطلب الكود
        await client.send_code(phone)
        print("\n" + "="*40)
        print("تم إرسال الكود بنجاح!")
        print("خد الكود وروح شغله تاني واكتبه في خانة الـ Inputs")
        print("="*40 + "\n")
    else:
        # المرة الثانية: نسجل الدخول بالكود اللي إنت كتبته
        try:
            sent_code = await client.send_code(phone)
            await client.sign_in(phone, sent_code.phone_code_hash, input_code)
            print(f"\nSESSION_STRING_SUCCESS:\n{await client.export_session_string()}\n")
        except Exception as e:
            print(f"خطأ: {e}")

if __name__ == "__main__":
    asyncio.run(main())
