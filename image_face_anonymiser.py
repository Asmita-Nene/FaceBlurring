import cv2
import mediapipe as mp

image_path = r'sample.jpg'

img = cv2.imread(image_path)
H, W, C = img.shape

with mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_det:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_det.process(img_rgb)

    if out.detections is not None:
        for det in out.detections:
            bbox = det.location_data.relative_bounding_box
            xmin = bbox.xmin
            ymin = bbox.ymin
            w = bbox.width
            h = bbox.height

            xmin = max(0, int(bbox.xmin * W))
            ymin = max(0, int(bbox.ymin * H))
            w = min(W - xmin, int(bbox.width * W))
            h = min(H - ymin, int(bbox.height * H))


            img[ymin:ymin+h, xmin:xmin+w, :] = cv2.blur(img[ymin:ymin+h, xmin:xmin+w, :], (30, 30))


cv2.imshow('frame', img)
cv2.waitKey(0)