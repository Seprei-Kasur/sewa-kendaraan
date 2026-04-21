from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        try:
            # Ambil data dari form
            jenis = request.form['jenis']
            jumlah = int(request.form['jumlah'])
            tarif = float(request.form['tarif'])
            lama = int(request.form['lama'])
            biaya_operasional = float(request.form['biaya_operasional'])
            biaya_tetap = float(request.form['biaya_tetap'])

            # Validasi input
            if jumlah <= 0 or tarif <= 0 or lama <= 0 or biaya_operasional < 0 or biaya_tetap < 0:
                raise ValueError("Nilai harus positif")

            # Perhitungan
            pendapatan_kotor = jumlah * tarif * lama
            total_biaya_variabel = jumlah * biaya_operasional * lama
            total_biaya = total_biaya_variabel + biaya_tetap
            laba_bersih = pendapatan_kotor - total_biaya

            hasil = {
                'jenis': jenis,
                'pendapatan_kotor': pendapatan_kotor,
                'total_biaya': total_biaya,
                'laba_bersih': laba_bersih,
                'status': 'Untung' if laba_bersih > 0 else 'Rugi' if laba_bersih < 0 else 'Impas'
            }
        except (ValueError, TypeError):
            hasil = {'error': 'Masukkan angka yang valid dan positif!'}

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)