
#Kütüphanelerin Yüklenmesi işlemi 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Giriş değişkenlerini tanımlama (sıcaklık, nem, rüzgar hızı)
# başlagıç- nerde sonlanacacğı - sayilar arasında artış miktari
sicaklik = ctrl.Antecedent(np.arange(0, 51, 1), 'sicaklik')
nem = ctrl.Antecedent(np.arange(0, 101, 1), 'nem')
ruzgar_hizi = ctrl.Antecedent(np.arange(0, 21, 1), 'ruzgar_hizi')

# Çıkış değişkenini tanımlama (hava durumu)
hava_durumu = ctrl.Consequent(np.arange(0, 101, 1), 'hava_durumu')

# Üyelik fonksiyonları tanımlama
# Sıcaklık: düşük, orta, yüksek
sicaklik['dusuk'] = fuzz.trapmf(sicaklik.universe, [0, 0, 10, 20])
sicaklik['orta'] = fuzz.trapmf(sicaklik.universe, [10, 20, 25, 35])
sicaklik['yuksek'] = fuzz.trapmf(sicaklik.universe, [30, 40, 50, 50])

# Nem: düşük, orta, yüksek
nem['dusuk'] = fuzz.trapmf(nem.universe, [0, 0, 30, 50])
nem['orta'] = fuzz.trapmf(nem.universe, [40, 55, 70, 80])
nem['yuksek'] = fuzz.trapmf(nem.universe, [70, 80, 100, 100])

# Rüzgar hızı: düşük, orta, yüksek
ruzgar_hizi['dusuk'] = fuzz.trapmf(ruzgar_hizi.universe, [0, 0, 4, 8])
ruzgar_hizi['orta'] = fuzz.trapmf(ruzgar_hizi.universe, [6, 8, 12, 14])
ruzgar_hizi['yuksek'] = fuzz.trapmf(ruzgar_hizi.universe, [12, 14, 20, 20])


# Hava durumu: güneşli, bulutlu, yağmurlu, fırtınalı
hava_durumu['gunesli'] = fuzz.trapmf(hava_durumu.universe, [0, 0, 20, 40])
hava_durumu['bulutlu'] = fuzz.trapmf(hava_durumu.universe, [30, 40, 50, 60])
hava_durumu['yagmurlu'] = fuzz.trapmf(hava_durumu.universe, [50, 60, 70, 85])
hava_durumu['firtinali'] = fuzz.trapmf(hava_durumu.universe, [70, 85, 100, 100])

# Kuralların tanımlanması işlemi 
#sicaklik dusuk için değerler
kural1 = ctrl.Rule(sicaklik['dusuk'] & nem['dusuk'] & ruzgar_hizi['dusuk'], hava_durumu['gunesli'])
kural2 = ctrl.Rule(sicaklik['dusuk'] & nem['dusuk'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural3 = ctrl.Rule(sicaklik['dusuk'] & nem['dusuk'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural4 = ctrl.Rule(sicaklik['dusuk'] & nem['orta'] & ruzgar_hizi['dusuk'], hava_durumu['bulutlu'])
kural5 = ctrl.Rule(sicaklik['dusuk'] & nem['orta'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural6 = ctrl.Rule(sicaklik['dusuk'] & nem['orta'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural7 = ctrl.Rule(sicaklik['dusuk'] & nem['yuksek'] & ruzgar_hizi['dusuk'], hava_durumu['yagmurlu'])
kural8 = ctrl.Rule(sicaklik['dusuk'] & nem['yuksek'] & ruzgar_hizi['orta'], hava_durumu['yagmurlu'])
kural9 = ctrl.Rule(sicaklik['dusuk'] & nem['yuksek'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

#sicaklık orta için değerler
kural10 = ctrl.Rule(sicaklik['orta'] & nem['dusuk'] & ruzgar_hizi['dusuk'], hava_durumu['gunesli'])
kural11 = ctrl.Rule(sicaklik['orta'] & nem['dusuk'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural12 = ctrl.Rule(sicaklik['orta'] & nem['dusuk'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural13 = ctrl.Rule(sicaklik['orta'] & nem['orta'] & ruzgar_hizi['dusuk'], hava_durumu['bulutlu'])
kural14 = ctrl.Rule(sicaklik['orta'] & nem['orta'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural15 = ctrl.Rule(sicaklik['orta'] & nem['orta'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural16 = ctrl.Rule(sicaklik['orta'] & nem['yuksek'] & ruzgar_hizi['dusuk'], hava_durumu['yagmurlu'])
kural17 = ctrl.Rule(sicaklik['orta'] & nem['yuksek'] & ruzgar_hizi['orta'], hava_durumu['yagmurlu'])
kural18 = ctrl.Rule(sicaklik['orta'] & nem['yuksek'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

#sicaklik yuksek için değerler
kural19 = ctrl.Rule(sicaklik['yuksek'] & nem['dusuk'] & ruzgar_hizi['dusuk'], hava_durumu['gunesli'])
kural20 = ctrl.Rule(sicaklik['yuksek'] & nem['dusuk'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural21 = ctrl.Rule(sicaklik['yuksek'] & nem['dusuk'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural22 = ctrl.Rule(sicaklik['yuksek'] & nem['orta'] & ruzgar_hizi['dusuk'], hava_durumu['gunesli'])
kural23 = ctrl.Rule(sicaklik['yuksek'] & nem['orta'] & ruzgar_hizi['orta'], hava_durumu['bulutlu'])
kural24 = ctrl.Rule(sicaklik['yuksek'] & nem['orta'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])

kural25 = ctrl.Rule(sicaklik['yuksek'] & nem['yuksek'] & ruzgar_hizi['dusuk'], hava_durumu['yagmurlu'])
kural26 = ctrl.Rule(sicaklik['yuksek'] & nem['yuksek'] & ruzgar_hizi['orta'], hava_durumu['yagmurlu'])
kural27 = ctrl.Rule(sicaklik['yuksek'] & nem['yuksek'] & ruzgar_hizi['yuksek'], hava_durumu['firtinali'])


# Kontrolllerin sisteme eklenmesi işlemi 
hava_durumu_kontrol = ctrl.ControlSystem([
    kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9, kural10,
    kural11, kural12, kural13, kural14, kural15, kural16, kural17, kural18, kural19, kural20,
    kural21, kural22, kural23, kural24, kural25, kural26, kural27
])

hava_durumu_simulasyonu = ctrl.ControlSystemSimulation(hava_durumu_kontrol)



sicaklikdeger = int(input("Sıcaklığı giriniz (°C 0-50 arasinda): "))
nemdeger = int(input("Nemi giriniz (% 0-100 arasinda ): "))
ruzgarhiz = int(input("Rüzgar hızını giriniz (Km/H 0-20 arasinda): "))



# Kontrollerin sağlanması 
if sicaklikdeger < 0 or sicaklikdeger > 50:
    print(f"Hata: Sıcaklık değeri 0 ile 50 arasında olmalıdır. Girilen değer: {sicaklikdeger}")
elif nemdeger < 0 or nemdeger > 100:
    print(f"Hata: Nem değeri 0 ile 100 arasında olmalıdır. Girilen değer: {nemdeger}")
elif ruzgarhiz < 0 or ruzgarhiz > 20:
    print(f"Hata: Rüzgar hızı değeri 0 ile 20 arasında olmalıdır. Girilen değer: {ruzgarhiz}")
else:
    # Değerleri ekleme işlemi
    hava_durumu_simulasyonu.input['sicaklik'] = sicaklikdeger
    hava_durumu_simulasyonu.input['nem'] = nemdeger
    hava_durumu_simulasyonu.input['ruzgar_hizi'] = ruzgarhiz




# Sistemi çalıştırma
hava_durumu_simulasyonu.compute()

# Hava Durumu Değerlerini yazdırma işlemi 
print(f"Sıcaklık: {sicaklikdeger} °C")
print(f"Nem: % {nemdeger}")
print(f"Rüzgar Hızı: {ruzgarhiz} Km/S")
# Hava Durumu Tahminini yazdırma işlemi 
print(f"Hava Durumu Değeri : {hava_durumu_simulasyonu.output['hava_durumu']:.2f} (0-100 aralığında)")

# Duruma göre hava tahmin kategorisi belirleme
if hava_durumu_simulasyonu.output['hava_durumu'] <= 40:
    print("Tahmini Hava Durumu: Güneşli")
elif hava_durumu_simulasyonu.output['hava_durumu'] <= 60:
    print("Tahmini Hava Durumu: Bulutlu")
elif hava_durumu_simulasyonu.output['hava_durumu'] <= 85:
    print("Tahmini Hava Durumu: Yağmurlu")
else:
    print("Tahmini Hava Durumu: Fırtınalı")
