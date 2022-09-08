from ytdownloader import YTDownloader, _initialize_folders
import argparse

def args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("url", type=str, help="YouTube URL")
    parser.add_argument( "-f","--format", metavar="", help="Format from which the file should be downloaded", choices=["video", "audio"], required=True)
    parser.add_argument( "-o","--outfile", metavar="", help="Specify where to save downloaded files", default=None, required=False)
    parser.add_argument( "-p","--playlist", help="Download audio/video from a playlist", action="store_true", required=False)
    return parser.parse_args()

def main():
    _initialize_folders()
    if not args().playlist:
        downloader = YTDownloader(args().url, args().outfile)
        if args().format == "video":
            downloader.to_video()
        elif args().format == "audio":
            downloader.to_audio()
    else:
        YTDownloader.from_playlist(args().url, format=args().format)

if __name__ == "__main__":
    main()