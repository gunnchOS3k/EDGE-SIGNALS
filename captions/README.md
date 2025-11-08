# Captions Post-Processing

Optional workflow for adding SRT subtitles to the final video.

## Quick Start

1. Edit `sample_lyrics.txt` with your section markers or lyrics (one per line)
2. Generate SRT file:
   ```bash
   python make_srt.py sample_lyrics.txt > edgesignals.srt
   ```
3. Mux captions into video:
   ```bash
   ffmpeg -i EDGE_SIGNALS_EdmundGunnJr.mp4 -i edgesignals.srt -c copy -c:s mov_text EDGE_SIGNALS_EdmundGunnJr_captions.mp4
   ```

## Notes

- The script evenly distributes captions across 60 seconds by default
- Adjust `TOTAL` in `make_srt.py` if your video is a different length
- The SRT format is compatible with most video players and platforms
- Post-processing is allowed per event FAQ

