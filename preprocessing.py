import cv2
import os

input_folder = "dataset"
output_folder = "dataset_equalized"

os.makedirs(output_folder, exist_ok=True)

for class_name in os.listdir(input_folder):

    class_path = os.path.join(input_folder, class_name)

    if os.path.isdir(class_path):

        output_class = os.path.join(output_folder, class_name)
        os.makedirs(output_class, exist_ok=True)

        for image_name in os.listdir(class_path):

            img_path = os.path.join(class_path, image_name)

            img = cv2.imread(img_path)

            if img is not None:

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                equalized = cv2.equalizeHist(gray)

                equalized = cv2.cvtColor(
                    equalized,
                    cv2.COLOR_GRAY2BGR
                )

                save_path = os.path.join(
                    output_class,
                    image_name
                )

                cv2.imwrite(save_path, equalized)

print("Preprocessing selesai.")