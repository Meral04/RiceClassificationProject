# Rice Classification Project

## Deskripsi

Rice Classification Project merupakan sebuah proyek klasifikasi jenis beras menggunakan metode Deep Learning dengan arsitektur ResNet50.

Proyek ini bertujuan untuk mengenali jenis beras berdasarkan gambar. Model yang dibuat mampu melakukan klasifikasi terhadap 5 jenis beras, yaitu Arborio, Basmati, Ipsala, Jasmine, dan Karacadag.

Pada proyek ini digunakan metode Transfer Learning dengan model ResNet50 yang telah dilatih sebelumnya menggunakan ImageNet. Model kemudian disesuaikan untuk mengenali karakteristik dari gambar beras.

## Dataset

Dataset yang digunakan adalah Rice Image Dataset yang terdiri dari beberapa jenis beras dengan jumlah gambar yang cukup banyak.

Jenis beras yang digunakan dalam proses klasifikasi:

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

Dataset dapat diperoleh melalui program `download_dataset.py`.

## Tahapan Proses

Proses pembuatan model dilakukan melalui beberapa tahap:

1. Download Dataset

Dataset diambil menggunakan library KaggleHub melalui file `download_dataset.py`.

2. Preprocessing

Tahap preprocessing dilakukan untuk mempersiapkan gambar sebelum masuk ke proses training. Pada tahap ini dilakukan resize gambar dan peningkatan kualitas gambar menggunakan histogram equalization.

3. Pengurangan Dataset

Karena jumlah gambar pada dataset cukup besar, dilakukan pengurangan jumlah data agar proses training dapat berjalan lebih efisien menggunakan `reduce_dataset.py`.

4. Training Model

Model dilatih menggunakan arsitektur ResNet50 dengan metode Transfer Learning. Beberapa layer awal ResNet50 dibekukan sehingga proses training hanya berfokus pada bagian klasifikasi.

Training dilakukan selama 10 epoch dengan optimizer Adam dan menggunakan categorical crossentropy sebagai fungsi loss.

5. Evaluasi Model

Model diuji menggunakan data validasi untuk mengetahui performa klasifikasi. Hasil evaluasi berupa nilai akurasi, grafik training, grafik loss, dan confusion matrix.

6. Prediksi

Model yang sudah selesai dilatih dapat digunakan untuk melakukan prediksi terhadap gambar baru.

#Struktur Folder

RiceClassificationProject

├── download_dataset.py
├── preprocessing.py
├── reduce_dataset.py
├── train.py
├── evaluate.py
├── predict.py
├── grafik.py
├── requirements.txt

├── hasil
│ ├── accuracy_graph.png
│ ├── loss_graph.png
│ └── confusion_matrix.png

└── model
└── rice_resnet50.h5

## Instalasi

Sebelum menjalankan program, install library yang dibutuhkan dengan perintah:


pip install -r requirements.txt


## Cara Menjalankan Program

1. Download dataset:
python download_dataset.py

2. Melakukan preprocessing:
python preprocessing.py

3. Mengurangi jumlah dataset (Dataset dikurangi karena jumlah gambar awal yang cukup besar sehingga proses training membutuhkan waktu dan sumber daya komputasi yang tinggi. Pengurangan dilakukan secara seimbang pada setiap kelas agar proses pelatihan lebih efisien dengan tetap mempertahankan variasi data dan kemampuan model dalam mengenali setiap jenis beras):
python reduce_dataset.py

4. Melakukan training model:
python train.py

5. Melakukan evaluasi model:
python evaluate.py

6. Melakukan prediksi gambar:
python predict.py

## Model

Model hasil training menggunakan arsitektur ResNet50 disimpan dalam format HDF5 dengan nama:
rice_resnet50.h5


Karena ukuran file model cukup besar sehingga tidak dapat diunggah langsung ke repository GitHub, file model disimpan pada Google Drive.
Model dapat diakses melalui link berikut:

Link Model:
https://drive.google.com/drive/folders/1TVjtKm2vEwjPGMMqJMAVDV_pcfnNvJv5?usp=sharing 

Model tersebut dapat digunakan untuk melakukan prediksi gambar tanpa perlu melakukan training ulang.

#Hasil Model

Model berhasil melakukan klasifikasi terhadap 5 jenis beras.

Hasil training selama 10 epoch mendapatkan:

- Training Accuracy: 80.45%
- Validation Accuracy: 89.60%

Contoh hasil prediksi:

Jenis Beras: Basmati

Confidence: 96.21%

Hasil grafik training dan evaluasi dapat dilihat pada folder `hasil`.

## Teknologi yang Digunakan

- Python
- TensorFlow
- Keras
- ResNet50
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

#Author
Moh. Rifki Almahdi_232410102023
