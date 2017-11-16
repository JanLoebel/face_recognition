import os
from time import sleep, time
from tempfile import TemporaryDirectory
import requests
from picamera import PiCamera

#-----SETTINGS------
# Url to the FaceRec-Server
face_rec_url = 'http://127.0.0.1:8080/'
image_resolution = (640, 480)
black_n_white = True
#-------------------

# Setup camera
camera = PiCamera()

# Set resolution
camera.resolution = image_resolution

# Set the camera to black and white
if black_n_white:
    camera.color_effects = (128, 128)

# Start preview (optional)
camera.start_preview()

# Sleep some seconds to get the white balance and focus right on begin
sleep(5)

# Take a photo and send it to the service
with TemporaryDirectory() as tmp_dir:
    while True:
        milli_sec = int(round(time() * 1000))
        current_picture_path = tmp_dir + '/facerec_' + str(milli_sec) + '.jpg'
        camera.capture(current_picture_path)

        # Upload image
        files = {'file': open(current_picture_path, 'rb')}
        result = requests.post(face_rec_url, files=files)

        # Checking return status
        if result.status_code == 200:
            result_dict = result.json()
            faces_count = result_dict['count']

            # If there are faces found, check which ones
            if faces_count > 0:
                print("Found " + str(faces_count) + " faces from the image.")
                known_faces = result_dict['faces']

                # Are there any known faces?
                if known_faces:
                    print("Known-Faces are: " + ', '.join(known_faces))
                else:
                    print("Only unknown faces could be found.")
            else:
                print("No face found.")
        else:
            print("Error while calling the FaceRec-Service: ",
                  result.status_code, result.content)

        # Delete image directly to not handle to much data on the disk
        os.remove(current_picture_path)

# Stop preview
camera.stop_preview()
