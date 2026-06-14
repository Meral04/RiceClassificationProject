import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Load model
model = load_model("model/rice_resnet50.h5")

print("Model berhasil dimuat")


# Nama kelas
classes = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]


# Gambar uji
img_path = "test.jpg"


# Load gambar
img = image.load_img(
    img_path,
    target_size=(224,224)
)


# Convert gambar
img_array = image.img_to_array(img)


# Tambah dimensi
img_array = np.expand_dims(
    img_array,
    axis=0
)


# Normalisasi
img_array = img_array / 255.0


# Prediksi
prediction = model.predict(img_array)


# Ambil kelas tertinggi
index = np.argmax(prediction)

confidence = np.max(prediction) * 100


print("======================")
print("HASIL PREDIKSI")
print("======================")

print(
    "Jenis Beras :",
    classes[index]
)

print(
    "Confidence :",
    round(confidence,2),
    "%"
)