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
        sent_code = await client.send_code(phone)
        print("\n" + "="*40)
        print("تم إرسال الكود بنجاح!")
        print("الآن: اذهب للصفحة الرئيسية واصنع ملف اسمه code.txt")
        print("واكتب بداخله الكود الذي وصلك حالاً.")
        print("="*40 + "\n")
        
        # السيرفر سيفحص وجود الملف كل 5 ثواني لمدة 5 دقائق
        for i in range(60): 
            # هذه الخطوة تجبر جيتهاب على إعادة قراءة المجلد
            if os.path.exists("code.txt"):
                with open("code.txt", "r") as f:
                    code = f.read().strip()
                
                if len(code) > 2: # للتأكد أن الملف ليس فارغاً
                    await client.sign_in(phone, sent_code.phone_code_hash, code)
                    string = await client.export_session_string()
                    print(f"\nSESSION_STRING_SUCCESS:\n{string}\n")
                    return
            
            await asyncio.sleep(5)
            if i % 6 == 0:
                print(f"لا زلت أنتظر ملف code.txt... (مرت {i*5} ثانية)")
                
        print("انتهى الوقت ولم نجد الملف.")
    except Exception as e:
        print(f"خطأ: {e}")

if __name__ == "__main__":
    asyncio.run(main())
