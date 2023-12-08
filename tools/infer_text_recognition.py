# from modules.text_recognition import TextRecognition
# from PIL import Image
# import cv2
# from tensorflow import keras
# import numpy as np
# 
# IMG_PATH = r"samples/front.png"
# OUTPUT_PATH = r"tools/front.png"
# 
# if __name__ == "__main__":
    
    # img = cv2.imread(IMG_PATH)
# 
    # resized_img = cv2.resize(img, (96, 96))
# 
    # low_res = resized_img.astype('float32') / 255.0
    # low_res = np.expand_dims(low_res, axis=0)
# 

    # model = keras.models.load_model("tools/generator.h5")
    # inputs = keras.Input((None, None, 3))
    # output = model(inputs)
    # model = keras.models.Model(inputs, output)
# 

    # sr = model.predict(low_res)[0]
# 
    # sr = ((sr + 1) / 2.0) * 255.0
    # sr = sr.astype(np.uint8)
    # cv2.imwrite(OUTPUT_PATH, sr)
    # recognizer = TextRecognition(device="cpu")
    # image = sr
    # image = image[:, :, ::-1]
    # text, confidence = recognizer(Image.fromarray(image))
    # title = "Text: " + str(text) + " - Confidence: " + str(confidence)
    # print(title)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
# 
# from modules.text_detection import TextDetection
# from modules.text_recognition import TextRecognition
# from PIL import Image
# from time import sleep
# import cv2
# 
# IMG_PATH = r"samples/front.png"
# 
# if __name__ == "__main__":
    # detector = TextDetection(device="cpu")
    # recognizer = TextRecognition(device="cpu")
# 
    # image = cv2.imread(IMG_PATH)
    # image = image[:, :, ::-1]
    # clone_image = image.copy()
# 
    # bounding_box_count = 0  # Đếm số lượng bounding box
# 
    # for i, line in enumerate(detector(image, False)):
        # line_text = ""
        # for bbox, image_part in line:
            # clone_image = cv2.polylines(clone_image, [bbox], isClosed=True, color=(255, 0, 0), thickness=1)
            # image_part = image_part[:, :, ::-1]
            # bounding_box_count += 1
            # cv2.imshow("result", clone_image)
            # text, confidence = recognizer(Image.fromarray(image_part))
            # line_text += text + " "
# 
        # print(f"Text in bounding box {bounding_box_count}: {line_text}")
# 
    # print(f"Số lượng bounding box được nhận diện: {bounding_box_count}")
# 
    # cv2.waitKey(0)
# 
# 
# from modules.text_detection import TextDetection
# from modules.text_recognition import TextRecognition
# from PIL import Image
# from time import sleep
# import cv2
# import os

# IMG_PATH = r"samples/regex.jpg"

# def extract_bounding_box_images(image, bounding_boxes):
    # box_images = []
    # for bbox, _ in bounding_boxes:

        # x, y, w, h = cv2.boundingRect(bbox)
        # box_image = image[y:y+h, x:x+w]
        # box_images.append(box_image)
    # return box_images

# if __name__ == "__main__":
    # detector = TextDetection(device="cpu")
    # recognizer = TextRecognition(device="cpu")

    # image = cv2.imread(IMG_PATH)
    # image = image[:, :, ::-1]
    # clone_image = image.copy()

    # bounding_box_count = 0  # Đếm số lượng bounding box

    # output_folder = "samples"
    # os.makedirs(output_folder, exist_ok=True)

    # for i, line in enumerate(detector(image, False)):
        # line_text = ""
        # for bbox, image_part in line:
            # clone_image = cv2.polylines(clone_image, [bbox], isClosed=True, color=(255, 0, 0), thickness=2)
            # bounding_box_count += 1

            # box_image = image_part[:, :, ::-1]  # Convert BGR to RGB
            # cv2.imshow(f"Bounding Box {bounding_box_count}", box_image)
            # image_filename = os.path.join(output_folder, f"bounding_box_{bounding_box_count}.png")
            # cv2.imwrite(image_filename, cv2.cvtColor(box_image, cv2.COLOR_RGB2BGR))

            # text, confidence = recognizer(Image.fromarray(box_image))
            # line_text += text + " "

        # print(f"Text in bounding box {bounding_box_count}: {line_text}")

    # print(f"Số lượng bounding box được nhận diện: {bounding_box_count}")

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

from modules.text_recognition import TextRecognition
from PIL import Image 
import cv2

IMG_PATH = r"samples/image2.jpg"

if __name__ == "__main__":
    recognizer = TextRecognition(device="cpu")
    image = cv2.imread(IMG_PATH)
    image = image[:, :, ::-1]
    text, confidence = recognizer(Image.fromarray(image))
    title = "Text: " + str(text) + " - Confidence: " + str(confidence)
    print(title)
    cv2.imshow("image", image)
    cv2.waitKey(0)