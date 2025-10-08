# Chacha20 Encryption Example

## Tujuan aplikasi

ChachaSlide adalah kumpulan skrip Python sederhana untuk mengenkripsi dan mendekripsi file JSON menggunakan algoritma ChaCha20. Aplikasi ini berguna untuk menyimpan atau mentransfer data JSON secara terenkripsi lalu mengembalikannya ke bentuk JSON yang valid.

## Cara menjalankan

Persyaratan:

- Python 3.x
- PyCryptodome (install dengan pip jika belum terpasang):

```bash
pip install pycryptodome
```

Langkah menjalankan:

1. Siapkan `example.json` (sudah ada pada repo sebagai contoh input).
2. Jalankan `encrypt.py` untuk membuat `results/encrypted.json` dan menampilkan kunci (base16) serta payload base64:

```bash
python encrypt.py
```

3. Setelah itu jalankan `decrypt.py` untuk mendekripsi `results/encrypted.json` dan menulis hasil ke `results/decrypted.json`. Script akan mencetak JSON ke stdout juga.

```bash
python decrypt.py
```

Catatan: `encrypt.py` akan menghasilkan kunci acak setiap kali dijalankan. Pastikan `results/encrypted.json` dan kunci yang digunakan cocok saat mendekripsi.

## Struktur file / folder

Root repository:

- `encrypt.py` — skrip untuk mengenkripsi isi `example.json` menjadi `results/encrypted.json` (menggunakan ChaCha20).
- `decrypt.py` — skrip untuk membaca `results/encrypted.json`, mendekripsi dengan ChaCha20, dan menulis `results/decrypted.json` (selalu menghasilkan keluaran JSON yang valid bila memungkinkan).
- `example.json` — contoh input JSON yang dienkripsi oleh `encrypt.py`.
- `results/` — folder keluaran yang berisi:
  - `encrypted.json` — file hasil enkripsi (base64-encoded nonce & ciphertext, base64 key)
  - `decrypted.json` — file hasil dekripsi (JSON yang diformat)
- `README.md` — dokumentasi ini.

## Contoh input-output

Contoh `example.json` (ringkasan):

```json
{
  "data": [
    {
      "title": "Otonari Ni Ginga",
      "slug": "otonari-ni-ginga",
      "type": "comic",
      "exclusivity": "paid",
      "synopsis": "...",
      "author": "Amagakure Gido",
      "artist": "Amagakure Gido",
      "status": "Ongoing",
      "publication": "2019",
      "coverArt": "https://..."
    }
  ]
}
```

Setelah menjalankan `encrypt.py`, `results/encrypted.json` berisi objek JSON seperti ini (isi base64 disingkat):

```json
{
  "nonce": "<base64-nonce>",
  "ciphertext": "<base64-ciphertext>",
  "public_key": "<base64-key>"
}
```

Menjalankan `decrypt.py` pada `results/encrypted.json` akan menghasilkan `results/decrypted.json` yang berisi kembali struktur JSON asli (contoh terpotong):

```json
{
  "data": [
    {
      "title": "Otonari Ni Ginga",
      "slug": "otonari-ni-ginga",
      "type": "comic",
      "exclusivity": "paid",
      "synopsis": "After the death of his father...",
      "author": "Amagakure Gido",
      "artist": "Amagakure Gido",
      "status": "Ongoing",
      "publication": "2019",
      "coverArt": "https://..."
    }
  ]
}
```

## Troubleshooting singkat

- Jika `decrypt.py` mencetak "Incorrect decryption", periksa bahwa `results/encrypted.json` memiliki semua kunci (`nonce`, `ciphertext`, `public_key`) dan bahwa file tidak rusak.
- Jika Python memberi error modul hilang, pasang dependensi `pycryptodome` seperti dijelaskan di atas.

## Lisensi

Gunakan sesuka Anda — tidak ada lisensi resmi yang disertakan.
