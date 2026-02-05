from flask import Flask, render_template, request, send_file
from google_play_scraper import reviews, Sort
import pandas as pd
import re
import io
import base64
import matplotlib
matplotlib.use('Agg') # Wajib biar gak crash di server
import matplotlib.pyplot as plt
from wordcloud import WordCloud

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data_hasil = []
    pesan_error = ""
    wordcloud_img = None # Wadah buat gambar awan kata

    if request.method == 'POST':
        url_target = request.form.get('url_input')
        jumlah_target = int(request.form.get('jumlah_input', 100))
        
        try:
            match = re.search(r'id=([a-zA-Z0-9._]+)', url_target)
            
            if match:
                app_id = match.group(1)
                
                # 1. Ambil Data
                hasil_reviews, _ = reviews(
                    app_id,
                    lang='id', 
                    country='id', 
                    sort=Sort.NEWEST, 
                    count=jumlah_target 
                )
                
                all_text = "" # String raksasa buat nampung semua komentar
                
                for ulasan in hasil_reviews:
                    komentar = ulasan['content']
                    all_text += komentar + " " # Gabungin teks
                    
                    data_hasil.append({
                        'Waktu': ulasan['at'].strftime('%Y-%m-%d'),
                        'User': ulasan['userName'],
                        'Rating': ulasan['score'],
                        'Komentar': komentar
                    })
                
                # 2. GENERATE WORD CLOUD (Fitur Baru)
                if len(all_text) > 0:
                    # Bikin awan kata
                    wc = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(all_text)
                    
                    # Simpan ke memori (bukan file disk) biar cepat
                    img = io.BytesIO()
                    wc.to_image().save(img, format='PNG')
                    img.seek(0)
                    
                    # Ubah jadi kode base64 biar bisa tampil di HTML
                    wordcloud_img = base64.b64encode(img.getvalue()).decode('utf-8')

            else:
                pesan_error = "Link gak valid! Pastikan link Google Play Store."
            
        except Exception as e:
            print(f"Error: {e}")
            pesan_error = "Gagal mengambil data. Cek koneksi atau link aplikasi."

    return render_template('index.html', data=data_hasil, error=pesan_error, wordcloud=wordcloud_img)

@app.route('/download')
def download_csv():
    # Disarankan simpan data ke CSV setiap request sukses (opsional logic-nya)
    # Disini kita asumsi data terakhir
    return "Fitur download butuh simpan file dulu (logic dataframe to csv)."

if __name__ == '__main__':
    app.run(debug=True)
