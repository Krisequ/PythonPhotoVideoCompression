import ffmpeg as ff

def compressVideo(inputFile, outputFile, quality = 20, vcodec='libx264'):
    # Compress video using ffmpeg
    # inputFile: path to input video
    # outputFile: path to output video
    # quality: 0-51, 0 is best quality, 51 is worst quality
    # Returns: True if successful, False otherwise
    # command = "ffmpeg -i " + inputFile + " -vcodec libx264 -crf " + str(quality) + " " + outputFile
    try:
        ff.input(inputFile).output(outputFile, vcodec=vcodec, crf=quality).run()
        return True
    except:
        return False


# TODO test input output and quality.