from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv
from inventory import stok_arama

load_dotenv()
app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/webhook")
async def whatsapp_gelen(request: Request):
    veri = await request.json()
    mesaj = veri.get("Body", "")

    prompt = f"""
    Bir müşteri şöyle sordu: '{mesaj}'
    Bu mesajdan ürün_türü, malzeme, maksimum_fiyat bilgilerini çıkart.
    Sonucu JSON olarak şu şekilde döndür:
    {{
        "urun_turu": "...",
        "malzeme": "...",
        "maksimum_fiyat": ...
    }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    cikti = response['choices'][0]['message']['content']
    sorgu = eval(cikti)

    sonuc = stok_arama(sorgu)

    if not sonuc:
        return {"message": "Üzgünüz, şu anda stoklarımızda bu özelliklere uygun ürün bulunmamaktadır."}

    yanit = "Stoklarımızda şu ürünleri bulduk:\n"
    for urun in sonuc:
        yanit += f"- {urun['isim']} – {urun['fiyat']}₺\n"

    return {"message": yanit}
