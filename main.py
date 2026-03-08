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
        print("\n" + "!"*40)
        print("1. الكود اتبعت دلوقتي على تليجرام.")
        print("2. روح اعمل ملف جديد اسمه code.txt")
        print("3. اكتب فيه الكود اللي جالك حالا ودوس حفظ.")
        print("!"*40 + "\n")
        
        # هيفضل مستنيك 5 دقائق ترفع الملف
        for i in range(60):
            if os.path.exists("code.txt"):
                with open("code.txt", "r") as f:
                    my_code = f.read().strip()
                if len(my_code) > 2:
                    await client.sign_in(phone, sent_code.phone_code_hash, my_code)
                    print(f"\nSESSION_STRING_SUCCESS:\n{await client.export_session_string()}\n")
                    return
            await asyncio.sleep(5)
            if i % 6 == 0: print("مستني ملف code.txt...")
            
    except Exception as e:
        print(f"حصلت مشكلة: {e}")

if __name__ == "__main__":
    asyncio.run(main())
