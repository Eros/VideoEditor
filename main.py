import argparse
import pathlib
import subprocess


def main():
    parser = argparse.ArgumentParser(description='Do some simple video edits through the command line')
    parser.add_argument('start', type=int, help='Set the start time')
    parser.add_argument('end', type=int, help='Set the duration of a cut')
    parser.add_argument('extract', type=bool, help='Extract audio into a separate file')
    parser.add_argument('file', type=str, help='Specify the video file')
    parser.add_argument('newname', type=str, help='New name for edited file')
    args = parser.parse_args()

    if not is_video(args.file):
        print('Video is not of type mp4, avi, mov, wmv, flv')
        exit(1)
    else:
        if args.extract is not None and args.file is not None:
            command = 'ffmpeg -i ' + args.file + '-ab 160k -ac 2 -ar 44100 -vn ' + args.newname + '.wav'
            subprocess.call(command)
        elif args.start is not None and args.end is not None and args.file is not None:
            command = 'ffmpeg -ss ' + args.start + ' -i ' + args.file + ' -t ' + args.end + ' -c copy ' + args.newname + '.mp4'
            subprocess.call(command)
        

def is_video(filepath):
    suffix = pathlib.Path(filepath).suffix
    if suffix == 'mp4' or suffix == 'avi' or suffix == 'mov' or suffix == 'wmv' or suffix == 'flv':
        return True
