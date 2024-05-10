# coding: latin-1
import tkinter as tk
from tkinter import messagebox
import sqlite3

class Gemiler:
    def __init__(self, seri_no, ad, agirlik, yapim_yili, kapasite , gemi_turu,petrol,kont_sayisi):
        self.seri_no = seri_no
        self.ad = ad
        self.agirlik = agirlik
        self.yapim_yili = yapim_yili
        self.kapasite = kapasite
        self.gemi_turu = gemi_turu
        self.petrol = petrol
        self.kont_sayisi = kont_sayisi

class Seferler:
    def __init__(self, gemi_id, kaptan1_id, kaptan2_id, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani,liman_ulkesi,varis_ulkesi,pasaport,demirleme_ucreti,kaptan_ad,kaptan_ad2,k1_ulke,k2_ulke,m_ad,m_ulke):
        self.gemi_id = gemi_id
        self.kaptan1_id = kaptan1_id
        self.kaptan2_id = kaptan2_id
        self.murettebat = murettebat
        self.yola_cikis_tarihi = yola_cikis_tarihi
        self.donus_tarihi = donus_tarihi
        self.yola_cikis_limani = yola_cikis_limani
        self.liman_ulkesi = liman_ulkesi
        self.varis_ulkesi = varis_ulkesi
        self.pasaport = pasaport
        self.demirleme_ucreti = demirleme_ucreti
        self.kaptan_ad = kaptan_ad
        self.kaptan_ad2 = kaptan_ad2
        self.k1_ulke = k1_ulke
        self.k2_ulke = k2_ulke
        self.m_ad = m_ad
        self.m_ulke = m_ulke

def gemi_ekle(seri_no, ad, agirlik, yapim_yili, kapasite, gemi_turu, petrol, kont_sayisi):
    connection = sqlite3.connect('gemiler_seferler.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Gemiler (seri_no, ad, agirlik, yapim_yili, kapasite, gemi_turu, petrol, kont_sayisi) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (seri_no, ad, agirlik, yapim_yili, kapasite, gemi_turu, petrol, kont_sayisi))
    connection.commit()
    connection.close()



def sefer_ekle(gemi_id, kaptan1_id, kaptan2_id, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, liman_ulkesi, varis_ulkesi, pasaport, demirleme_ucreti, kaptan_ad, kaptan_ad2, k1_ulke, k2_ulke, m_ad, m_ulke):
    connection = sqlite3.connect('gemiler_seferler.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Seferler (gemi_id, kaptan1_id, kaptan2_id, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, liman_ulkesi, varis_ulkesi, pasaport, demirleme_ucreti, kaptan_ad, kaptan_ad2, k1_ulke, k2_ulke, m_ad, m_ulke) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (gemi_id, kaptan1_id, kaptan2_id, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, liman_ulkesi, varis_ulkesi, pasaport, demirleme_ucreti, kaptan_ad, kaptan_ad2, k1_ulke, k2_ulke, m_ad, m_ulke))
    connection.commit()
    connection.close()


def show_message_box(message):
    messagebox.showinfo("Bilgi", message)

def on_gemi_ekle_click():
    seri_no = seri_no_entry.get()
    ad = ad_entry.get()
    agirlik = float(agirlik_entry.get())
    yapim_yili = int(yapim_yili_entry.get())
    kapasite = float(kapasite_entry.get())
    gemi_turu = gemi_turu_entry.get()  # gemi_turu bilgisini al
    petrol = petrol_entry.get()
    kont_sayisi = kont_sayisi_entry.get()
    gemi_ekle(seri_no, ad, agirlik, yapim_yili, kapasite, gemi_turu,petrol,kont_sayisi)  # gemi_turu bilgisini gemi_ekle fonksiyonuna aktar
    show_message_box("Yeni gemi eklendi!")

def on_sefer_ekle_click():
    gemi_id = int(gemi_id_entry.get())
    kaptan1_id = int(kaptan1_id_entry.get())
    kaptan2_id = int(kaptan2_id_entry.get())

    murettebat_text = murettebat_entry.get()
    if murettebat_text.strip() == '':
        show_message_box("M�rettebat ID bo� b�rak�lamaz.")
        return
    murettebat = int(murettebat_text)

    yola_cikis_tarihi = yola_cikis_tarihi_entry.get()
    donus_tarihi = donus_tarihi_entry.get()
    yola_cikis_limani = yola_cikis_limani_entry.get()
    liman_ulkesi = liman_ulkesi_entry.get()  # liman_ulkesi bilgisini al
    varis_ulkesi = varis_ulkesi_entry.get()  # varis_ulkesi bilgisini al
    pasaport = pasaport_entry.get()  # pasaport bilgisini al
    demirleme_ucreti = demirleme_ucreti_entry.get()
    kaptan_ad = kaptan_ad_entry.get()
    kaptan_ad2 = kaptan_ad2_entry.get()
    k1_ulke = k1_ulke_entry.get()
    k2_ulke = k2_ulke_entry.get()
    m_ad = m_ad_entry.get()
    m_ulke = m_ulke_entry.get()

    sefer_ekle(gemi_id, kaptan1_id, kaptan2_id, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, liman_ulkesi, varis_ulkesi, pasaport, demirleme_ucreti,kaptan_ad,kaptan_ad2,k1_ulke,k2_ulke,m_ad,m_ulke)  # liman_ulkesi, varis_ulkesi, pasaport ve demirleme_ucreti bilgilerini sefer_ekle fonksiyonuna aktar
    show_message_box("Yeni sefer eklendi!")


# Ana uygulama penceresi olu�tur
root = tk.Tk()
root.title("Gezgin Gemi �irketi Y�netim Sistemi")

# Gemiler i�in form elemanlar�n� olu�tur
seri_no_label = tk.Label(root, text="Seri No:")
seri_no_label.grid(row=0, column=0)
seri_no_entry = tk.Entry(root)
seri_no_entry.grid(row=0, column=1)

ad_label = tk.Label(root, text="Ad:")
ad_label.grid(row=1, column=0)
ad_entry = tk.Entry(root)
ad_entry.grid(row=1, column=1)

agirlik_label = tk.Label(root, text="A��rl�k:")
agirlik_label.grid(row=2, column=0)
agirlik_entry = tk.Entry(root)
agirlik_entry.grid(row=2, column=1)

yapim_yili_label = tk.Label(root, text="Yap�m Y�l�:")
yapim_yili_label.grid(row=3, column=0)
yapim_yili_entry = tk.Entry(root)
yapim_yili_entry.grid(row=3, column=1)

kapasite_label = tk.Label(root, text="Kapasite:")
kapasite_label.grid(row=4, column=0)
kapasite_entry = tk.Entry(root)
kapasite_entry.grid(row=4, column=1)

gemi_turu_label = tk.Label(root, text="Gemi T�r�:")
gemi_turu_label.grid(row=5, column=0)
gemi_turu_entry = tk.Entry(root)
gemi_turu_entry.grid(row=5, column=1)

petrol_label = tk.Label(root, text="Petrol :")
petrol_label.grid(row=6, column=0)
petrol_entry = tk.Entry(root)
petrol_entry.grid(row=6, column=1)

kont_sayisi_label = tk.Label(root, text="Konteyner Sayisi: ")
kont_sayisi_label.grid(row=7, column=0)
kont_sayisi_entry = tk.Entry(root)
kont_sayisi_entry.grid(row=7, column=1)



gemi_ekle_button = tk.Button(root, text="Gemi Ekle", command=on_gemi_ekle_click)
gemi_ekle_button.grid(row=8, column=0, columnspan=2)

# Seferler i�in form elemanlar�n� olu�tur
gemi_id_label = tk.Label(root, text="Gemi ID:")
gemi_id_label.grid(row=9, column=0)
gemi_id_entry = tk.Entry(root)
gemi_id_entry.grid(row=9, column=1)

kaptan1_id_label = tk.Label(root, text="Kaptan 1 ID:")
kaptan1_id_label.grid(row=10, column=0)
kaptan1_id_entry = tk.Entry(root)
kaptan1_id_entry.grid(row=10, column=1)

kaptan2_id_label = tk.Label(root, text="Kaptan 2 ID:")
kaptan2_id_label.grid(row=11, column=0)
kaptan2_id_entry = tk.Entry(root)
kaptan2_id_entry.grid(row=11, column=1)

murettebat_label = tk.Label(root, text="M�rettebat ID:")
murettebat_label.grid(row=12, column=0)
murettebat_entry = tk.Entry(root)
murettebat_entry.grid(row=12, column=1)  # M�rettebat giri� kutusunu (Entry) grid'e yerle�tirme


yola_cikis_tarihi_label = tk.Label(root, text="Yola ��k�� Tarihi:")
yola_cikis_tarihi_label.grid(row=13, column=0)
yola_cikis_tarihi_entry = tk.Entry(root)
yola_cikis_tarihi_entry.grid(row=13, column=1)

donus_tarihi_label = tk.Label(root, text="D�n�� Tarihi:")
donus_tarihi_label.grid(row=14, column=0)
donus_tarihi_entry = tk.Entry(root)
donus_tarihi_entry.grid(row=14, column=1)

yola_cikis_limani_label = tk.Label(root, text="Yola ��k�� Liman�:")
yola_cikis_limani_label.grid(row=15, column=0)
yola_cikis_limani_entry = tk.Entry(root)
yola_cikis_limani_entry.grid(row=15, column=1)


liman_ulkesi_label = tk.Label(root, text="Yola ��k�� Liman �lkesi:")  # Etiket olu�turuluyor
liman_ulkesi_label.grid(row=16, column=0)  # Etiket konumland�r�l�yor
liman_ulkesi_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
liman_ulkesi_entry.grid(row=16, column=1)  # Giri� kutusu konumland�r�l�yor


varis_ulkesi_label = tk.Label(root, text="Var�� Liman �lkesi:")  # Etiket olu�turuluyor
varis_ulkesi_label.grid(row=17, column=0)  # Etiket konumland�r�l�yor
varis_ulkesi_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
varis_ulkesi_entry.grid(row=17, column=1)  # Giri� kutusu konumland�r�l�yor

pasaport_label = tk.Label(root, text="Pasaport Gerekli mi? :")  # Etiket olu�turuluyor
pasaport_label.grid(row=18, column=0)  # Etiket konumland�r�l�yor
pasaport_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
pasaport_entry.grid(row=18, column=1)  # Giri� kutusu konumland�r�l�yor


demirleme_ucreti_label = tk.Label(root, text="Demirleme �creti:")  # Etiket olu�turuluyor
demirleme_ucreti_label.grid(row=19, column=0)  # Etiket konumland�r�l�yor
demirleme_ucreti_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
demirleme_ucreti_entry.grid(row=19, column=1)  # Giri� kutusu konumland�r�l�yor


kaptan_ad_label = tk.Label(root, text="Kaptan1 Ad�:")  # Etiket olu�turuluyor
kaptan_ad_label.grid(row=20, column=0)  # Etiket konumland�r�l�yor
kaptan_ad_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
kaptan_ad_entry.grid(row=20, column=1)


kaptan_ad2_label = tk.Label(root, text="Kaptan2 Ad�:")  # Etiket olu�turuluyor
kaptan_ad2_label.grid(row=21, column=0)  # Etiket konumland�r�l�yor
kaptan_ad2_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
kaptan_ad2_entry.grid(row=21, column=1)

k1_ulke_label = tk.Label(root, text="K1 �lke:")  # Etiket olu�turuluyor
k1_ulke_label.grid(row=22, column=0)  # Etiket konumland�r�l�yor
k1_ulke_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
k1_ulke_entry.grid(row=22, column=1)  # Giri� kutusu konumland�r�l�yor


k2_ulke_label = tk.Label(root, text="K1 �lke:")  # Etiket olu�turuluyor
k2_ulke_label.grid(row=23, column=0)  # Etiket konumland�r�l�yor
k2_ulke_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
k2_ulke_entry.grid(row=23, column=1)  # Giri� kutusu konumland�r�l�yor


m_ad_label = tk.Label(root, text="M�rettebat Ad�:")  # Etiket olu�turuluyor
m_ad_label.grid(row=24, column=0)  # Etiket konumland�r�l�yor
m_ad_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
m_ad_entry.grid(row=24, column=1)  # Giri� kutusu konumland�r�l�yor

m_ulke_label = tk.Label(root, text="M�rettebat �lkesi:")  # Etiket olu�turuluyor
m_ulke_label.grid(row=25, column=0)  # Etiket konumland�r�l�yor
m_ulke_entry = tk.Entry(root)  # Giri� kutusu olu�turuluyor
m_ulke_entry.grid(row=25, column=1)  # Giri� kutusu konumland�r�l�yor




sefer_ekle_button = tk.Button(root, text="Sefer Ekle", command=on_sefer_ekle_click)
sefer_ekle_button.grid(row=26, column=0, columnspan=2)

# Uygulamay� �al��t�r
root.mainloop()

