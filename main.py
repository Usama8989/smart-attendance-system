from face_recognition_module import load_known_faces, recognize_face
from fingerprint_module import authenticate_fingerprint
from db_handler import init_db, mark_attendance

def main():
    init_db()
    print("Loading known faces...")
    known_faces, known_names = load_known_faces()

    print("Recognizing face...")
    name = recognize_face(known_faces, known_names)
    if name:
        print(f"Face recognized: {name}")
        if authenticate_fingerprint(user_id=name):
            mark_attendance(name)
            print(f"Attendance marked for {name}")
        else:
            print("Fingerprint authentication failed.")
    else:
        print("Face not recognized.")

if __name__ == "__main__":
    main()
