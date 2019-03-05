import face_recognition
from FaceA.apps.face_web.models import *
import os


def do_check_func(subject, unknown_faces):
    known_face_encodings = []
    face_names = []
    face_locations = []
    face_encodings = []
    attend = []
    absence = []
    students = Student.objects.filter(myclass=subject.myclass)
    for i in students:
        path = os.path.join("known_faces", str(subject.myclass), str(i)+'.jpg')
        face_image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_face_encodings.append(face_encoding)
        face_names.append(str(i))
        absence.append(i)

    unknown_faces_image = face_recognition.load_image_file(unknown_faces)
    # unknown_faces_encoding = face_recognition.face_encodings(unknown_faces_image)[0]
    face_locations = face_recognition.face_locations(unknown_faces_image)
    face_encodings = face_recognition.face_encodings(unknown_faces_image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)

            absence.remove(students[first_match_index])

            name = face_names[first_match_index]
            attend.append(name)
    do_record(subject, absence)
    return absence


def do_record(subject, absence):
    for i in absence:
        r = Result.objects.create(student=i, subject=subject)
        r.save()
