from moviepy.editor import VideoFileClip

## Get the video clip that has the sound!
## I have tested mp4 and mts video files to work.

sound_clip = VideoFileClip("video.mp4")

## Now get the edited video.

edited_clip = VideoFileClip("edited.mp4")

## Combine the edited clip with the sound from the unedited clip.

final_clip = edited_clip.set_audio(sound_clip.audio)

## Save the file.

final_clip.write_videofile("final.mp4")
