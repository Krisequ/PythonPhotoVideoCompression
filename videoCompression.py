import ffmpeg as ff
import os


def compress_video(input_file: str, output_file: str, quality: int = 20, codec:str='libx264'):
    # Compress video using ffmpeg
    # input_file: path to input video
    # output_file: path to output video
    # quality: 0-51, 0 is the best quality, 51 is the worst quality
    # codec: libx264, libx265, libvpx, libvpx-vp9, libaom-av1
    # Returns: True if successful, False otherwise

    print('Alt command')
    print('ffmpeg', '-i', input_file, '-c:v', codec, '-crf', str(quality), output_file)
    print('\n')

    if not os.path.exists(input_file):
        print("File %s not found" % input_file)
        return False

    if os.path.exists(output_file):
        print("Output file %s already exists" % output_file)
        return False

    try:
        (
         ff.input(input_file)
           .output(output_file, vcodec=codec, crf=quality)
           .run()
        )
        return True
    except:
        print("Compress video dropped exception for " + input_file)
        return False


# TODO test input output and quality.
def get_bitrate_and_resolution(file):
    try:
        probe = ff.probe(file)
        codec = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        bitrate = int(codec['bit_rate'])
        width = int(codec['width'])
        height = int(codec['height'])
        return bitrate, width, height
    except:
        print("get_bitrate_and_resolution dropped exception for " + file)
        return 0, 0, 0

def check_bitrate_and_resolution():
    pass

compress_video(".\\YDXJ0737.MP4",
               os.path.curdir+"\\outputs\\testOutput.mp4",
               20,
               "h264")

ff.probe(".\\YDXJ0737.MP4")


