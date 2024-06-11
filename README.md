# Slack Avatar Face Recognition for Enterprise Migration

## Overview

This solution provides a method for accurately detecting human faces in Slack avatar images. 
It serves as a double-check mechanism to ensure user avatars meet specific standards
before migrating to an enterprise environment. The script uses the `face_recognition` library,
which is built on top of `dlib` and provides highly accurate face detection.

## Prerequisites

Before you begin, ensure you have Python installed on your system. 
This solution requires Python 3.8 or higher. 
You will also need to install the `face_recognition`, `dlib`, `open-cv2` 
libraries along with its dependencies.

## Installation

To install libraries, run the following command:

```bash
pip install -r requirements.txt
```
i.e.
Depending on your operating system, installation might require additional steps. 
Refer to the official `face_recognition` [installation guide](https://github.com/ageitgey/face_recognition#installation) for detailed instructions.

## Usage

To validate the avatars, place all PNG images in a designated directory. 
Then, execute the face detection script as follows:

```bash
python validate_avatars.py --avatar-dir /path/to/avatar/directory
```

## Script Example: `validate_avatars.py`

```python
import face_recognition
import os
import argparse

def is_human_face(face_image_path):
    image = face_recognition.load_image_file(face_image_path)
    face_locations = face_recognition.face_locations(image)
    return len(face_locations) > 0

def validate_avatars(directory_path):
    results = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(directory_path, filename)
            is_face_present = is_human_face(image_path)
            results.append((filename, is_face_presence))
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Slack avatars for human face presence.")
    parser.add_argument('--avatar-dir', required=True, help='Path to the directory with avatar images')
    args = parser.parse_args()

    validated_results = validate_avatars(args.avatar_dir)
    for filename, has_face in validated_results:
        print(f"{filename}: {'Human face detected' if has_face else 'No human face detected'}")
```

## Results

After running the script, it will output the results in the console, indicating whether a human face was detected in each avatar image. The results can be logged or exported as needed for further analysis or auditing purposes.

## Notes

- The default face detection model used is HOG (Histogram of Oriented Gradients), which balances accuracy and performance.
- For more accuracy, especially under complex imaging conditions, the CNN-based model can be used by modifying the face detection call with `model='cnn'`. Be aware that this requires significantly more computational power and might be slower.
- Always ensure that you comply with data protection laws and obtain necessary permissions before processing personal images.