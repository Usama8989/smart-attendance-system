import face_recognition
import cv2
import os

def load_known_faces(directory='images'):
    known_faces = []
    known_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(os.path.splitext(filename)[0])
    return known_faces, known_names

def recognize_face(known_faces, known_names):
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            if True in matches:
                matched_idx = matches.index(True)
                name = known_names[matched_idx]
                video.release()
                cv2.destroyAllWindows()
                return name
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
    return None
