import os
import logging
import face_recognition


class FaceRecognizer():
    """Face recognition module for package theft detection system"""

    def __init__(self):
        self._load_known_face()

    def _load_known_face(self):
        """Known faces..."""
        faces_db = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'face')
        faces = [os.path.join(faces_db, f) for f in os.listdir(faces_db) if f.endswith('.jpeg')]
        recognfized_faces = [face_recognition.load_image_file(i) for i in faces]
        self.known_faces = []
        for image in recognfized_faces:
            encoding = face_recognition.face_encodings(image)
            if len(encoding) > 0:
                logging.debug('Recognized people')
                self.known_faces.append(encoding[0])

    def _known_face_detected(self, frame):
        """Are you a stranger"""
        searched_faces = face_recognition.face_encodings(frame)
        if len(searched_faces) > 0:
            unknown = face_recognition.face_encodings(frame)[0]
            results = face_recognition.compare_faces(self.known_faces, unknown)
            if True in results:
                logging.info('I know you')
                return True
            logging.info('You are weird...')
            return False
