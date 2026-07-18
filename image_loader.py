import cv2

def load_image(path):

    image = cv2.imread(path)

    if image is None:
        print("Image not found.")
        return None

    return image