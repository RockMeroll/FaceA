import face_recognition
from FaceA.apps.face_web.models import *
import os


def do_check_func(class_, unknown_faces):
    known_face_encodings = []
    absence = []
    face_locations = []
    face_encodings = []
    attend = []
    students = Student.objects.filter(myclass=class_)
    for i in students:
        path = os.path.join("known_faces", str(class_), str(i)+'.jpg')
        face_image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_face_encodings.append(face_encoding)
        absence.append(str(i))

    unknown_faces_image = face_recognition.load_image_file(unknown_faces)
    # unknown_faces_encoding = face_recognition.face_encodings(unknown_faces_image)[0]
    face_locations = face_recognition.face_locations(unknown_faces_image)
    face_encodings = face_recognition.face_encodings(unknown_faces_image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = absence[first_match_index]
            absence.remove(name)

        attend.append(name)

    return absence


def do_record(class_, absence):
    pass
