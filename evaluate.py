import os
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# Load model
model = load_model("model/rice_resnet50.h5")

print("Model berhasil dimuat")


# Dataset validasi
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)


val_data = datagen.flow_from_directory(
    "dataset_small",
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)


# Prediksi
prediction = model.predict(val_data)

y_pred = np.argmax(prediction, axis=1)

y_true = val_data.classes


class_names = list(val_data.class_indices.keys())


# Accuracy
accuracy = accuracy_score(
    y_true,
    y_pred
)

print("\nAccuracy:")
print(round(accuracy*100,2), "%")


# Classification report
print("\nClassification Report:")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names
    )
)


# Confusion matrix
cm = confusion_matrix(
    y_true,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)


# Simpan gambar confusion matrix
os.makedirs("hasil", exist_ok=True)

plt.figure(figsize=(8,6))

plt.imshow(cm)

plt.title("Confusion Matrix Rice Classification")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.xticks(
    range(len(class_names)),
    class_names,
    rotation=45
)

plt.yticks(
    range(len(class_names)),
    class_names
)

plt.colorbar()

plt.tight_layout()

plt.savefig(
    "hasil/confusion_matrix.png"
)

plt.close()


print("\nConfusion matrix tersimpan di folder hasil")