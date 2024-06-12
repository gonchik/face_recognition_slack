import dlib
import os
import argparse


def is_human_face_dlib(image_path):
    # Load a pre-trained face detection model
    detector = dlib.get_frontal_face_detector()
    # Load the image
    image = dlib.load_rgb_image(image_path)
    # Perform face detection
    detected_faces = detector(image, 1)
    # Check if any faces are detected
    return len(detected_faces) > 0


# Example usage
def validate_avatars(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(directory_path, filename)
            if is_human_face_dlib(image_path):
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
