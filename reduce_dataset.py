import os
import shutil
import random


source_folder = "dataset_equalized"
target_folder = "dataset_small"

jumlah_gambar = 2000


os.makedirs(target_folder, exist_ok=True)


classes = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]


for class_name in classes:

    source_class = os.path.join(
        source_folder,
        class_name
    )

    target_class = os.path.join(
        target_folder,
        class_name
    )

    os.makedirs(
        target_class,
        exist_ok=True
    )


    images = os.listdir(source_class)

    random.shuffle(images)


    selected_images = images[:jumlah_gambar]


    print(
        class_name,
        ":",
        len(selected_images),
        "gambar"
    )


    for img in selected_images:

        shutil.copy(
            os.path.join(source_class, img),
            os.path.join(target_class, img)
        )


print("\nDataset kecil berhasil dibuat")