import face_recognition
import os
import argparse


def is_human_face(face_image_path):
    image = face_recognition.load_image_file(face_image_path)
    face_locations = face_recognition.face_locations(image)
    return len(face_locations) > 0


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
    parser.add_argument('--avatar-dir', required=True, help='Path to the directory with avatar images')
    args = parser.parse_args()
    if args.avatar_dir:
        avatars_path = args.avatar_dir
    else:
        # Replace with the path where your avatars are located
        avatars_path = 'avatars'
    validate_avatars(avatars_path)
