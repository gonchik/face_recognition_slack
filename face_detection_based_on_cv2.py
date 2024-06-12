import cv2
import os
import argparse


def is_human_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces) > 0


def validate_avatars(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(directory_path, filename)
            if is_human_face(image_path):
                # print(f"A human face has been detected in {filename}")
                pass
            else:
                email = filename[:-4]
                if email.__contains__('@'):
                    print(f"No human face detected in {email}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Slack avatars for human face presence.")
    parser.add_argument('--avatar-dir', required=True, help='Path to the directory with avatar images',
                        default='avatars')
    args = parser.parse_args()
    avatars_path = args.avatar_dir
    validate_avatars(avatars_path)
