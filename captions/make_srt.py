#!/usr/bin/env python3
"""
Generate simple evenly-spaced SRT lines from a text list.
Usage: python make_srt.py sample_lyrics.txt > edgesignals.srt
"""
import sys
import textwrap

lines = [l.strip() for l in open(sys.argv[1], 'r').read().splitlines() if l.strip()]

# default: 60s total; adjust as needed
TOTAL = 60.0
n = len(lines)
chunk = TOTAL / max(n, 1)

def ts(t):
    h = int(t // 3600)
    t -= h * 3600
    m = int(t // 60)
    t -= m * 60
    s = int(t)
    ms = int((t - s) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

start = 0.0
for i, txt in enumerate(lines, 1):
    end = min(TOTAL, start + chunk - 0.25)
    print(i)
    print(f"{ts(start)} --> {ts(end)}")
    print(textwrap.fill(txt, 42))
    print()
    start += chunk

