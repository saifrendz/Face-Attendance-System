import cv2
import face_recognition_models
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/',
    'storageBucket': 'your-project-id.appspot.com'
})


# ## Importing students images
foldePath = 'Images'
pathList = os.listdir(foldePath)
imgList = []
studentIds = []
print(pathList)
for path in pathList:
    imgList.append(cv2.imread(os.path.join(foldePath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{foldePath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFIle.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("FIle Saved")
