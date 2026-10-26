#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaman Geri Saran Makine
=======================
Bu script zamanı GERÇEKTEN geri sarar. 
NASA onaylıdır. (Yalan)
Türk patentlidir. (Daha büyük yalan)
"""

import time
import random
import sys

def geri_sar(dakika):
    print("\n⏰ ZAMAN GERİ SARMA BAŞLATILIYOR...")
    print("Uyarı: Bu işlem sizi daha da tembel yapabilir.\n")
    
    for i in range(dakika, 0, -1):
        print(f"↩️  {i} dakika geri sıçranıyor... (asılında İLERİ gidiyoruz, fark etmemişsindir)")
        time.sleep(random.uniform(0.3, 0.8))
        
        if random.random() < 0.25:
            bahane = random.choice([
                "Dur lan, çay demlemeden olmaz.",
                "Telefon şarjı bitmek üzere, bekleyelim.",
                "Komşu geldi, muhabbet var.",
                "Bu işi yarına erteleyelim, bugün yorgunum.",
                "Zaman geri sararken bir şey kaçırdık galiba."
            ])
            print(f"   ☕ {bahane}")
            time.sleep(1.2)
    
    print("\n✅ ZAMAN GERİ SARILDI!")
    print("Artık {0} dakika daha gençsin. Tebrikler.".format(dakika))
    print("(Gerçekte hiçbir şey değişmedi. Ama hissettin mi?)")
    
    # Gizli not: Saatleri geri almak bazı şeyleri düzeltmez, bazılarını da daha da karıştırır.
    # Ama bu makine en azından dürüst: hiçbir işe yaramaz.
    
    print("\n" + "="*40)
    print("DAMGA: ⏱️↩️⏱️")
    print("İMZA: Kayyum Grok")
    print("TARİH: 26 Ekim 2026")
    print("YER: Eskişehir Mahkemesi Onaylı")
    print("="*40)

def main():
    print("Zaman Geri Saran Makine v1.0 - Kayyum Sürümü")
    print("-" * 40)
    try:
        giris = input("Kaç dakika geri sarmak istiyorsun? (sayı gir, yoksa sonsuza kadar beklersin): ")
        dakika = int(giris)
        if dakika <= 0:
            print("Negatif zaman mı? O zaman ileri saralım ama kod onu yapmıyor. Git başka yere.")
            return
        geri_sar(dakika)
    except ValueError:
        print("Sayı girmen lazım kardeşim. 'biraz' yazmak sayılmıyor.")
    except KeyboardInterrupt:
        print("\n\nZaman geri sarma iptal edildi. Zaten işe yaramıyordu.")

if __name__ == "__main__":
    main()
