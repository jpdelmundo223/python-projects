from pytube import YouTube, Playlist
from pytube.exceptions import PytubeError
import os
import configparser
import time

def _read_from_config() -> configparser.ConfigParser:
    """Reads from configuration file.
    """
    filename = 'config.cfg'
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
        return config
    else:
        raise FileNotFoundError(filename)

def _initialize_folders() -> None:
    """Creates the folder(s) to be used for storing downloaded files.

    :param:
        None
    :return:
        None
    """
    if not os.path.exists('downloads'):
        os.mkdir('downloads')
        print("downloads folder created ...")
    else:
        pass
    if not os.path.exists('downloads/audio'):
        os.makedirs('downloads/audio', exist_ok=True)
        print("audio folder created ...")
    else:
        pass
    if not os.path.exists('downloads/video'):
        os.makedirs('downloads/video', exist_ok=True)
        print("video folder created ...")
    else:
        pass

class YTDownloader(YouTube):
    def __init__(self, url, outfile=None):
        self.outfile = outfile
        super().__init__(url=url)
        
    @staticmethod
    def download(stream: YouTube.streams, outfile: str):
        """Fetch data from a youtube stream, then downloads it.

        :param Youtube.streams stream:
            YouTube media streams.
        :param str outfile:
            Download(s) destination path.
        :return: 
            None
        """
        start_time = time.time()
        print("Downloading {}, with resolution set to highest: {} ...".format(stream.title, stream.resolution))
        stream.download(outfile, filename=stream.default_filename)
        elapsed_time = time.time() - start_time
        print("Download finished ...")
        print("Time elapsed: {}s ...".format(round(elapsed_time, 2)))

    def to_video(self):
        """Downloads youtube media streams to video/mp4 format, 
        with it's resolution set to highest.

        :param YTDownload self:
            self class object
        :return: 
            None
        """
        stream = self.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
        try:
            if self.outfile is None:
                YTDownloader.download(stream, "downloads/video")
            else:
                YTDownloader.download(stream, self.outfile)
        except PytubeError as e:
            print(e)

    def to_audio(self):
        """Downloads youtube media streams to audio/mp3 format.

        :param YTDownload self:
            self class object
        :return: 
            None
        """
        stream = self.streams.filter(file_extension="mp4", only_audio=True).first()
        try:
            if self.outfile is None:
                YTDownloader.download(stream, "downloads/audio")
                try:
                    os.rename(os.path.join("downloads/audio", stream.default_filename), os.path.join("downloads/audio", stream.default_filename.replace('.mp4', '.mp3')))
                except OSError as e:
                    print(e)
            else:
                YTDownloader.download(stream, self.outfile)
                try:
                    os.rename(os.path.join(self.outfile, stream.default_filename), os.path.join(self.outfile, stream.default_filename.replace('.mp4', '.mp3')))
                except OSError as e:
                    print(e)
        except PytubeError as e:
            print(e)

    @classmethod
    def from_playlist(cls, url: str, format: str):
        """Downloads youtube media streams from a playlist, choose whether to download
        video/mp4 format or audio/mp3 format.

        :param str url:
            Youtube Playlist URL.
        :param str format:
            Format from which the file should be downloaded.
        :return:
            None
        """
        try:
            playlist = Playlist(url)
            for url in playlist.video_urls:
                if format == "audio":
                    cls(url).to_audio()
                elif format == "video":
                    cls(url).to_video()
                else:
                    print("Invalid format ...")
        except:
            print("Invalid playlist url.")