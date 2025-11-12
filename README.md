# EDGE SIGNALS — 6G Dreams in Neon

**A kinetic, anime-inspired sprint through Brooklyn's signal-lit nights—where 6G dreams, gesture controllers, and city rhythm sync on the beat. EDGE SIGNALS turns latency into choreography, with scene cuts tied to downbeats and color palettes shifting by musical section.**

---

## What We Used

- **OpenArt Music Video** (core) — Generated all visuals using style and story prompts
- **Suno** (optional) — Original instrumental track generation
- **ffmpeg** (optional) — Lightweight post-processing for caption muxing

## How It Was Made

1. Generated visuals via **OpenArt → Music Video** using the prompts in `/prompts`
2. Imported final MP4 to optional post step: captions (`captions/make_srt.py`) then ffmpeg mux
3. Exported as H.264, 1080p, ≤200 MB, named `EDGE_SIGNALS_EdmundGunnJr.mp4`

## Judging Checklist Mapping

### Creativity & Originality
- 2D/3D hybrid anime aesthetic with 6G/edge-tech motifs
- Custom color ramps per musical section (cyan → magenta shifts)
- Beat-synced visual choreography

### Technical Execution
- Scene cuts aligned to downbeats
- Consistent style cues across all shots
- Optional crisp captions with proper timing

### Story & Emotion
- City-to-cosmos narrative arc: ambition → momentum → arrival
- Visual progression from street-level to skyline to cosmic perspective

### Effective Use of OpenArt
- One-tap Music Video workflow
- Specific style + story prompts for precise control
- Temporal consistency maintained across generated shots

### Attributions & Rights
- **Visuals**: Generated with OpenArt Music Video
- **Music**: See `submission/credits_manifest.json` for track source and license details
- All content created for OpenArt × NYU Hackathon submission

## About the Creator

**Edmund Gunn, Jr.** — 6G/URLLC researcher, edge AI engineer, and education outreach advocate. Working at the intersection of ultra-reliable low-latency communications and creative technology. Passionate about making cutting-edge research accessible through visual storytelling.

## Quick Links

- **GitHub**: [gunnchOS3k](https://github.com/gunnchOS3k)
- **LinkedIn**: [edmund-gunn-jr](https://www.linkedin.com/in/edmund-gunn-jr/)
- **Final Video**: [Watch on Google Drive](https://drive.google.com/file/d/1UcFXjcLAlAa0xSllIT6cuR89_b9JbrSb/view?usp=drive_link)
- **Landing Page**: [View Project Site](https://gunnchOS3k.github.io/EDGE-SIGNALS/site/) (or open `site/index.html` locally)
- **Social Posts**: TikTok/IG/YouTube links in `submission/` folder

---

**Hashtags**: #OpenArtMVA #OMVANYU #GenARTNYU

