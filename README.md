# Ghostly Writing Effect
This takes a movie, removes the background, and applies a "ghostly writing" effect. The background colors are very contrived in my code - to make it work for your background you may have to change them around. Also, the ghostly writing takes a color in the movie and adds a slight white tinge to it. For my example I used orange play dough to "write" with.

My program takes the file named "video.mp4", and applies effects, and saves a file "edited.mp4". To run it requires Python 3 with pygame, numpy, and cv2 (opencv). These can normally be installed with the following commands:
```
pip install pygame
pip install numpy
pip install opencv-python
```

My program removes the sound from the video when applying the effects, but there is an easy fix with the moviepy module. I have included this fix under "fixaudio.py". It is important to not run this from the IDLE, but instead use the terminal or command line (with `python fixaudio.py`). Often moviepy can be installed with the command:
```
pip install moviepy
```

My example videos on GitHub have smaller resolution than normal videos in order to fit the 25 MB limit.
