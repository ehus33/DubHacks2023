'''
Inspiration from the OG Mark Rober @ CrunchLabs
This is based on his porch pirate technology

Key differences:
1. My tech does not actually piss off the robber.
2. 
'''

import pathlib

import os

import cv2

from rtsparty import Stream

import time as t

print('Starting input stream:\n')

# Gets the stream from the camera...
stream = Stream(os.environ['RTSP_URL'], )

def get_data():
    ''' Directory of the data within our operating system '''
    ''' We will store image data within this to train OpenCV '''

    # Throws back the data from the data directory...
    # TODO: ADD IMAGES to the data directory to train the model.
    return os.path.dirname(os.path.realpath(__file__)), 'data'  

def make_dir():
    '''Simulates the mkdir command in the terminal... except you're doing it for yourself'''
    ''' LOLOLOLOL Let's gedem...'''
    
    # Here we create the directories together iff they don't exist...

    pathlib.Path(os.path.join(get_data(), 'package')).mkdir(parents = True, exist_ok = True)
    pathlib.Path(os.path.join(get_data(), 'no_package')).mkdir(parents = True, exist_ok = True)

def get_my_files():
    '''Start the Ohio Raid to grab the files from the Gucci Store...'''

    passphrase = 'NO_PACKAGE'

    # Case  1: No package found...

    if bool(os.environ.get('PACKAGE_PRESENT')):
        passphrase = 'PACKAGE'
    # Generate a new filepath with a new filename using the passphrase...
    data_directory = os.path.join(get_data(), 'data', passphrase)
    filename = passphrase + '__' + str(int(t.time()))

    # The unique OS path is a string-join of the data directory and the filename
    # to create a unique identifier...
    return os.path.join(data_directory, filename)

def save_my_files():
    ''' Creates a new file from the image...'''

    '''Stilll image of the camera screen'''
    stop_frame = stream.get_frame()

    filename = get_my_files()

    ''' Test '''
    if stream.is_frame_empty(stop_frame):
        # Nothing Nothing is here!!!!!!!!
        # You failed as cameraman.
        return False
    # If you work, then write something please!!!!
    cv2.imwrite(filename, stop_frame)
    # Return the filename
    return filename

if __name__ == '__main__':
    make_dir()
    try:
        while True:
            save_it = save_my_files()
            if save_it:
                # Show physical output of the saved output
                print(save_it)
                # Take a break...
                t.sleep(5)
            else:
                print("Error 520... retrying operation in 5 seconds...")
    except KeyboardInterrupt:
        # I'm too cool for this... Let's stop it...
        print('Stopping operations now...')