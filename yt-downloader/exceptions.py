from pytube.exceptions import PytubeError

class VideoNotFound(PytubeError):
    """Video not found error."""