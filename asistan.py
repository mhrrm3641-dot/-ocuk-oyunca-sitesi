import yfinance as yf
import json

hisseler = ["THYAO.IS", "ASELS.IS", "USDTRY=X", "BTC-USD"]
sonuclar = {}

print("--- SİBER ÜS GÜNCELLEME ---")

for sembol in hisseler:
    try:
        ticker = yf.Ticker(sembol)
        fiyat = ticker.history(period="1d")['Close'].iloc[-1]
        sonuclar[sembol] = round(fiyat, 2)
        print(f"{sembol}: {round(fiyat, 2)} TL")
    except:
        print(f"{sembol} hatali!")

with open('veri.json', 'w') as f:
    json.dump(sonuclar, f)

print("\n'veri.json' güncellendi!")

