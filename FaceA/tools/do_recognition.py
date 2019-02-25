import face_recognition
from FaceA.apps.face_web.models import *

def face_recog(class_):
    known_face_encodings = []
    known_face_names = []
    face_locations = []
    face_encodings = []
    face_names = []
    students = Student.objects.filter(student_class=class_)


