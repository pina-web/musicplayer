#!/usr/bin/env python3
"""
전시회음악 폴더의 mp3를 깃허브용 영문 이름으로 정리합니다.
  전시회음악/피아노곡-요피 (7).mp3  →  music/piano-07.mp3

사용법: 이 파일을 '전시회음악' 폴더가 있는 위치에 두고
        터미널에서  python3 rename-music.py
"""
import os, re, shutil, sys

SRC_CANDIDATES = ["전시회음악", "."]
DST = "music"

def find_files():
    for d in SRC_CANDIDATES:
        if not os.path.isdir(d):
            continue
        hits = []
        for f in os.listdir(d):
            m = re.search(r"\((\d+)\)\s*\.mp3$", f, re.I)
            if m:
                hits.append((int(m.group(1)), os.path.join(d, f)))
        if hits:
            return sorted(hits)
    return []

files = find_files()
if not files:
    print("mp3를 찾지 못했습니다. '전시회음악' 폴더가 있는 위치에서 실행하세요.")
    sys.exit(1)

os.makedirs(DST, exist_ok=True)
for n, path in files:
    dst = os.path.join(DST, f"piano-{n:02d}.mp3")
    shutil.copy2(path, dst)
    print(f"  {os.path.basename(path)}  →  {dst}")

print(f"\n완료: {len(files)}곡을 '{DST}' 폴더에 정리했습니다.")
print("이제 index.html, music 폴더, .nojekyll 을 깃허브에 올리세요.")
