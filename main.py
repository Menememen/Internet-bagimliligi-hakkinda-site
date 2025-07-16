from flask import Flask
import random
import string

app = Flask(__name__)

# Bilgi listesi
facts_list = [
    "İnternet Bağımlılığı bir hastalıktır.",
    "İnternet Bağımlılığını yenmek için çok fazla tabletle, telefonla, bilgisayarla vakit geçirmemeliyiz.",
    "Dışarıda zaman geçirmek internet bağımlılığına karşı yardımcı olabilir.",
    "Günlük teknoloji kullanımını sınırlamak faydalıdır.",
    "Aile ile birlikte zaman geçirmek, ekran süresini azaltabilir."
]

# Ana sayfa
@app.route("/")
def anasayfa():
    return '''
        <h1>İnternet Bağımlılığı Hakkında Bilgiler</h1>
        <p>Bu sayfada internet bağımlılığı ile ilgili gerçekleri bulabilirsiniz.</p>
        <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a><br>
        <a href="/sifre_olustur">Rastgele Şifre Oluştur!</a>
    '''

# Rastgele bilgi sayfası
@app.route("/rastgele_gercek")
def rastgele_gercek():
    secilen_gercek = random.choice(facts_list)
    return f'''
        <h1>Rastgele Gerçek:</h1>
        <p>{secilen_gercek}</p>
        <a href="/">Ana sayfaya dön</a>
    '''

# Şifre oluşturucu sayfası
@app.route("/sifre_olustur")
def sifre_olustur():
    karakterler = string.ascii_letters + string.digits + string.punctuation
    rastgele_sifre = ''.join(random.choice(karakterler) for _ in range(12))
    return f'''
        <h1>Rastgele Şifre:</h1>
        <p style="font-size: 24px; color: green;">{rastgele_sifre}</p>
        <a href="/sifre_olustur">Yeni bir şifre oluştur!</a><br>
        <a href="/">Ana sayfaya dön</a>
    '''

# Uygulamayı çalıştır
if __name__ == "__main__":
    app.run(debug=True)
