import cv2
import pygame
import numpy as np
pygame.init()

video_name = 'edited.mp4'


vidcap = cv2.VideoCapture('video.mp4')
background_colors=[(197,174,133),
                   (180,157,115),
                   (150,126,88),
                   (139,117,80)]
background_variations=[0.14,0.18,0.18,0.1]

low_colors=np.array([[100, 100, 100], [94, 129, 148], [72, 103, 123], [72, 105, 125]])
high_colors=np.array([[255, 255, 225], [255, 255, 255], [255,255,255], [255,255,255]])

magic_colors=[(184,31,0)]

count=0
success, frame=vidcap.read()
height,width,layers=frame.shape
video=cv2.VideoWriter(video_name,-1,30,(width,height))

black=np.zeros(frame.shape)

background_img=cv2.imread("graveyard.jpg",1)
background_img=background_img

def replace_color(frame,background_colors,background_variations,replace_color):
    frame=pygame.surfarray.make_surface(frame)
    pixel_array=pygame.PixelArray(frame)
    for i in range(len(background_colors)):
        pixel_array.replace(background_colors[i],replace_color,background_variations[i])
    del pixel_array

    return pygame.surfarray.array3d(frame)

def replace_color_slow(frame,low_background_colors,high_background_colors,replace_color):
    for i in range(len(low_background_colors)):
        mask=cv2.inRange(frame,low_background_colors[i],high_background_colors[i])
        frame=cv2.bitwise_and(frame,frame,mask=~mask)
        mask=(frame==(0,0,0))
        frame[mask]=replace_color[mask]
    return frame

def replace_color_with_image(frame,background_color,background_image):
    mask=(frame==background_color)
    frame[mask]=background_image[mask]
    return frame

## The following is to make a "magic" finger look with the red fingertip.

magic_touch=np.full(frame.shape,0.0)
add_to_touch=np.full(frame.shape,255)

lower_red=np.array([0,0,200])
upper_red=np.array([75,125,255])
def replace_red(frame):
    global magic_touch,add_to_touch
    mask=cv2.inRange(frame,lower_red,upper_red)
    for i in range(3):
        mask=cv2.bitwise_or(np.roll(mask,i,axis=1), mask)
        mask=cv2.bitwise_or(np.roll(mask,-i,axis=1),mask)
        mask=cv2.bitwise_or(np.roll(mask,i,axis=0),mask)
        mask=cv2.bitwise_or(np.roll(mask,-i,axis=0),mask)
    frame=cv2.bitwise_and(frame,frame,mask=~mask)
    mask2=(frame==(0,0,0))
    magic_touch[mask2]=magic_touch[mask2]+128
    frame+=magic_touch.astype('uint8')
    return frame

while vidcap.isOpened():
    success,frame = vidcap.read()
    if(type(frame)==type(None)):
        break
    
    magic_touch=magic_touch/1.005

    frame=replace_color(frame,background_colors,background_variations,(0,0,0))
    frame=replace_color_with_image(frame,(0,0,0),background_img)
    frame=replace_red(frame)
    video.write(frame)
    count+=1
    print("{}: {}".format(count,success))
    
cv2.destroyAllWindows()
vidcap.release()
video.release()
