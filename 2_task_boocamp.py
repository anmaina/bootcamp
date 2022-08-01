
from moviepy.editor import VideoFileClip
import os

def tiktok_to_gif(video_url: str)-> str:
    '''converts video into .gif format and returns direcroty path to the converted video
    param video_url: url path or directory path to the target video that needs convertation'''

    videoClip = VideoFileClip(video_url)
    new_s = "new_videoclip.gif"
    videoClip.write_gif(new_s, fps=15)
    path = os.path.dirname(__file__)
    return os.path.join(path, new_s)

if __name__ == '__main__':
    filename = "D:\\Projects\\fizz_buzz\\1.mp4"
    filepath=os.path.basename(filename)
    print(tiktok_to_gif(filename))
