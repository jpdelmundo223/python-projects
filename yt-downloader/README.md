# YouTube Downloader

A Python class library, which was derived from another famous library called [pytube](https://pytube.io/en/latest/), that is used for downloading youtube contents and/or media.

## Basic usage

### Downloading a video

```bash
python3 cli.py https://www.youtube.com/watch?v=2lAe1cqCOXo --format video
```

### Downloading a audio

```bash
python3 cli.py https://www.youtube.com/watch?v=2lAe1cqCOXo --format audio
```

### Downloading from a youtube playlist

```bash
python3 cli.py https://www.youtube.com/playlist?list=PL5NuQCLaTOJvGZbQatyQBynAC0qt3sckV --playlist --format audio
```

- **Note:** Playlist should be available public for this to work properly, otherwise, it will return an emptry list `[]`

## Features

- Command-line interface

## Required arguments

- `url`: YouTube url.
- `--format` or `-f`: Specifies which format the file should be downloaded (supported formats are mp4 for video, and mp3 for audio).

## Optional arguments

- `--outfile` or `-o`: Where downloaded files are going to be placed.
- `--playlist` or `-p`: Specify whether to download from a youtube playlist.
