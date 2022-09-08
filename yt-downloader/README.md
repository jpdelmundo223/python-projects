# YouTube Downloader

A Python class library, which was derived from another famous library called [pytube](https://pytube.io/en/latest/), that is used for downloading youtube contents and/or media.

## Basic usage

```bash
python3 cli.py https://www.youtube.com/watch?v=2lAe1cqCOXo --format video
```

## Features

- Command-line interface

## Required arguments

- `url`
- `--format` or `-f`: Specifies which format the file should be downloaded (supported formats are mp4 for video, and mp3 for audio).

## Optional arguments

- `--outfile` or `-o`: Where downloaded files are going to be placed.
- `--playlist` or `-p`:
