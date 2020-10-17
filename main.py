import pathlib


def is_video(filepath):
    suffix = pathlib.Path(filepath).suffix
    if suffix == 'mp4' or suffix == 'avi' or 'mov' or suffix == 'wmv' or suffix == 'flv':
        return True
