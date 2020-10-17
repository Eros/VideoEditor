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
    parser.add_argument('framesstart', type=str, help='Set where to start converting frames')
    parser.add_argument('framesend', type=str, help='Set where to end converting frames')
    parser.add_argument('framesall', type=bool, help='Convert entire video to images')
    args = parser.parse_args()

    if not is_video(args.file):
        print('Video is not of type mp4, avi, mov, wmv, flv')
        exit(1)
    else:
        if args.extract is not None and args.file is not None:
            command = 'ffmpeg -i ' + args.file + '-ab 160k -ac 2 -ar 44100 -vn ' + args.newname + '.wav'
            print('[+] Extracting audio')
            subprocess.call(command)
        elif args.start is not None and args.end is not None and args.file is not None:
            command = 'ffmpeg -ss ' + args.start + ' -i ' + args.file + ' -t ' + args.end + ' -c copy ' + args.newname + '.mp4'
            print('[+] Cutting video between ' + args.start + ' ' + args.end)
            subprocess.call(command)
        elif args.framesstart is not None and args.framesend is not None and args.file is not None:
            command = 'ffmpeg -i ' + args.file + ' -vf select=`between(t,' + args.framesstart + ',' + args.framesend + ')` -vsync 0 ' + args.newname + '%d.png '
            print('[+] Converting frames starting at ' + args.framesstart + ' ending at ' + args.framesend)
            subprocess.call(command)
        elif args.framesall is True and args.file is not None:
            command = 'ffmpeg -i ' + args.file + ' -vf fps=1 ' + args.newname + '%d.png'
            print('[+] Converting all frames to images...')
            subprocess.call(command)
        else:
            print('[!] Something went wrong, check the command!')


def is_video(filepath):
    suffix = pathlib.Path(filepath).suffix
    if suffix == 'mp4' or suffix == 'avi' or suffix == 'mov' or suffix == 'wmv' or suffix == 'flv':
        return True


if __name__ == '__main__':
    main()
