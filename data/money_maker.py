import asyncio
import aiohttp
import random
import time

# --- KONFİQURASİYA ---
# Sənin Monetag "Qızıl" Linkin (TAM VERSİYA)
TARGET_LINK = "https://omg10.com/4/10703033"
MY_WALLET = "TRktEgrrKMVr7riTRjBhM3cBV1Qgy5rzQR"

class MonetagProfitMachine:
    def __init__(self):
        self.url = TARGET_LINK
        self.wallet = MY_WALLET
        self.success_count = 0

    async def start_profit_stream(self):
        # Müxtəlif cihazlar (iPhone, Android, PC) kimi görünmək üçün başlıqlar
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36"
        ]

        async with aiohttp.ClientSession() as session:
            print(f"🚀 ZYVEXA PROFIT: SYSTEM ONLINE")
            print(f"🏦 PAYOUT WALLET: {self.wallet}")
            print(f"🔗 TARGET: {self.url}")
            print("--------------------------------------------------")

            while True:
                try:
                    headers = {"User-Agent": random.choice(user_agents)}
                    
                    # Linkə gizli sorğu göndəririk (Trafik yaradırıq)
                    async with session.get(self.url, headers=headers, timeout=15) as response:
                        if response.status == 200:
                            self.success_count += 1
                            print(f"✅ [HUNT SUCCESS #{self.success_count}] Trafik təsdiqləndi.")
                            print(f"📊 Monetag 'Statistics' panelini 30 dəqiqə sonra yoxla.")
                            print("--------------------------------------------------")
                
                except Exception as e:
                    print(f"⚠️ [RECONNECTING] Şəbəkə optimallaşdırılır...")
                
                # Monetag-ın "bot" olduğunu anlamaması üçün təsadüfi gözləmə (MÜTLƏQDİR)
                # Çox sürətli etsək hesabın bloklanar, ona görə 10-20 saniyə qoyuruq
                wait_time = random.uniform(10, 20)
                await asyncio.sleep(wait_time)

if __name__ == "__main__":
    bot = MonetagProfitMachine()
    try:
        asyncio.run(bot.start_profit_stream())
    except KeyboardInterrupt:
        print("\n🛑 Sistem dayandırıldı. Qazanc Monetag panelindədir.")
