from image_loader import load_image
from detector import detect_faces
from visualization import show_faces

while True:

    print("\n")
    print("=" * 40)
    print("FACE DETECTION")
    print("=" * 40)

    print("1. Detect Face")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        image_path = input("Enter Image Name: ")

        image = load_image(image_path)

        if image is not None:

            faces = detect_faces(image)

            print("Faces Detected:", len(faces))

            show_faces(image, faces)

    elif choice == "2":

        print("Thank You...")
        break

    else:

        print("Invalid Choice")