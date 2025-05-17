# FaceBlurring
**Face blurring using OpenCV and MediaPipe**

## Overview
This project detects human faces in an **image or real-time webcam feed** and applies **blurring** to maintain privacy and anonymity. It can be useful for:
- Privacy protection in videos and live streams.
- Security applications where facial data needs anonymization.
- Dataset preprocessing to blur faces before training AI models.

### Technologies Used:
- OpenCV for handling images and video frames.
- MediaPipe FaceDetection for efficient face recognition.

## Logic Behind Face Anonymizer
The face anonymizer works by detecting human faces in an image or webcam feed and applying a blur effect to obscure them. The process follows these steps:

1. **Capture Frame/Image** → Using OpenCV, the script reads an image or video frame.
2. **Convert Image to RGB** → MediaPipe requires RGB input for processing.
3. **Detect Faces** → The `FaceDetection` model identifies face locations.
4. **Extract Bounding Box** → The coordinates of detected faces are retrieved and scaled to image size.
5. **Apply Blur** → OpenCV blurs only the detected face region to anonymize identities.
6. **Display Output** → The processed image/video is shown or saved.

This method ensures efficient **privacy protection**, making facial details unreadable while maintaining overall image integrity.


### Features
- Detects faces in images and webcam feeds.
- Applies blurring to anonymize faces.
- Optimized for real-time video processing.
- Can be extended to detect multiple faces.
