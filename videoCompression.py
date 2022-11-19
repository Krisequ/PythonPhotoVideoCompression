import ffmpeg as ff
import os


def compress_video(input_file: str, output_file: str, quality: int = 20, codec:str='libx264'):
    # Compress video using ffmpeg
    # input_file: path to input video
    # output_file: path to output video
    # quality: 0-51, 0 is the best quality, 51 is the worst quality
    # codec: libx264, libx265, libvpx, libvpx-vp9, libaom-av1
    # Returns: True if successful, False otherwise

    if(not os.path.exists(input_file)):
        print("File %s not found" %input_file)
        return False

    try:
        ff.input(input_file).output(output_file, vcodec=codec, crf=quality).run()
        return True
    except:
        return False


# TODO test input output and quality.
def check_bitrate_and_resolution():
    pass

compressVideo("C:\\Users\\Krisq\\Desktop\\Testy kompresji pythonem\\2022.09.08 Nurkowanie\\YDXJ0737.MP4",
              ".\\testOutput.mp4", 20)