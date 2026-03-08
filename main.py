import os
import asyncio
from pyrogram import Client

async def main():
    # سحب البيانات بالأسامي اللي إنت سميتها في صورتك بالظبط
    api_id = os.environ.get("TELEGRAM_API_ID")
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    phone = os.environ.get("TELEGRAM_PHONE_NUMBER")
    
    if not api_id or not api_hash or not phone:
        print("خطأ: تأكد من إضافة الـ Secrets بأساميها المظبوطة!")
        return

    # تشغيل العميل في الذاكرة
    client = Client(":memory:", api_id=int(api_id), api_hash=api_hash)
    await client.connect()
    
    try:
        # إرسال الكود لموبايلك الـ Samsung A35
        sent_code = await client.send_code(phone)
        print("\n" + "="*40)
        print("تم إرسال الكود لتليجرام بنجاح!")
        print("اكتب الكود في ملف جديد اسمه code.txt وارفعه فوراً")
        print("="*40 + "\n")
        
        # السيرفر هيستنى 3 دقائق ترفع ملف code.txt
        for i in range(18):
            if os.path.exists("code.txt"):
                with open("code.txt", "r") as f:
                    code = f.read().strip()
                # تسجيل الدخول النهائي
                await client.sign_in(phone, sent_code.phone_code_hash, code)
                print(f"\nSESSION_STRING_SUCCESS:\n{await client.export_session_string()}\n")
                return
            await asyncio.sleep(10)
        print("انتهى الوقت (3 دقائق) ولم نجد ملف code.txt")
    except Exception as e:
        print(f"حصل خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    asyncio.run(main())
