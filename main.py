import os
import asyncio
from pyrogram import Client

async def main():
    # سحب بياناتك من الخزنة اللي إنت عملتها
    api_id = int(os.environ.get("API_ID"))
    api_hash = os.environ.get("API_HASH")
    phone = os.environ.get("PHONE")
    
    client = Client(":memory:", api_id=api_id, api_hash=api_hash)
    await client.connect()
    
    # إرسال الكود لموبايلك الـ Samsung A35
    sent_code = await client.send_code(phone)
    print("\n" + "="*40)
    print("تم إرسال الكود لتليجرام بنجاح!")
    print("اكتب الكود في ملف جديد اسمه code.txt وارفعه فوراً")
    print("="*40 + "\n")
    
    # السيرفر هيستنى 3 دقائق ترفع ملف فيه الكود
    for i in range(18):
        if os.path.exists("code.txt"):
            with open("code.txt", "r") as f:
                code = f.read().strip()
            # تسجيل الدخول النهائي
            await client.sign_in(phone, sent_code.phone_code_hash, code)
            string = await client.export_session_string()
            print("\n" + "!"*20)
            print("مبروك! ده الـ SESSION_STRING بتاعك:")
            print(string)
            print("!"*20 + "\n")
            return
        await asyncio.sleep(10)
    print("انتهى الوقت (3 دقائق) ومرفعتش ملف code.txt")

if __name__ == "__main__":
    asyncio.run(main())
