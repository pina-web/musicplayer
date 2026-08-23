# 요피의 전시음악플레이리스트

요피(박미화)가 요피(박미화)가 직접 연주한 피아노곡을 전시장에서 하루 종일 이어서 재생하는 웹 플레이어입니다.

## 플레이리스트

| 목록 | 곡 수 | 내용 |
|---|---|---|
| 🎼 요피의 전시음악플레이리스트 | 33 | 실제 피아노 연주 녹음 (66분) |
| 🎧 생성 음악 전체 | 200 | 브라우저가 실시간 연주 (14시간) |
| 🎹 피아노 · 🌿 잔잔한 · 🎻 클래식 · 🎤 가요풍 · ✨ 애니 OST · 🍋 경쾌한 · ☕ 카페 재즈 | 44·32·30·30·26·24·14 | 생성 음악을 느낌별로 |
| 💿 불러온 음원 | — | 파일·폴더로 추가한 곡 |
| 🔀 전부 섞기 | 233 | 전부 섞어서 |

생성 음악은 음원 파일이 아니라 웹오디오로 그 자리에서 연주되는 소리입니다.
저장 용량을 차지하지 않고 저작권자도 없습니다.

## 올릴 파일 구조

```
저장소/
├── index.html
├── .nojekyll
└── music/
    ├── piano-01.mp3
    ├── piano-02.mp3
    └── … piano-33.mp3
```

`music` 폴더가 없으면 `전시회음악/피아노곡-요피 (n).mp3` 경로도 자동으로 찾습니다.
다만 **영문 이름을 권장합니다.** 한글 파일명은 macOS에서 자모가 분리된 형태로
저장돼 깃허브에서 404가 나는 일이 있습니다.

정리는 `rename-music.py`를 한 번 실행하면 됩니다.

```
python3 rename-music.py
```

## 깃허브에 올리기

### 0. 먼저 파일 이름 정리

`rename-music.py`를 `전시회음악` 폴더가 있는 위치에 두고 한 번 실행합니다.

```
python3 rename-music.py
```

`music/piano-01.mp3` ~ `piano-33.mp3`가 만들어집니다. 원본은 그대로 남습니다.
**깃허브에는 `music` 폴더만 올리세요.** 원본 한글 폴더까지 올리면 용량이 두 배가 됩니다.

### 1. 저장소 만들기

github.com → 우측 상단 `+` → **New repository**

- Repository name: `random-play` (원하는 이름)
- **Public** 선택 — GitHub Pages 무료 사용 조건입니다
- Add a README file은 체크하지 않습니다 (직접 올릴 예정)
- **Create repository**

### 2. 파일 올리기 — 웹으로 (가장 쉬움)

1. 저장소 첫 화면의 **uploading an existing file** 링크를 누릅니다.
   (이미 파일이 있다면 `Add file` → `Upload files`)
2. `index.html`, `README.md`, `rename-music.py`, `.nojekyll`을 끌어다 놓습니다.
3. 아래 **Commit changes**를 누릅니다.
4. 다시 `Add file` → `Upload files`로 들어가서
   이번엔 **`music` 폴더 자체를 통째로** 끌어다 놓습니다.
   폴더를 끌면 경로가 유지되어 `music/piano-01.mp3` 형태로 올라갑니다.
5. 33개 목록이 다 뜬 것을 확인하고 **Commit changes**.

> 음원이 합쳐서 90MB라 업로드에 몇 분 걸립니다. 중간에 멈추면
> 15개 정도씩 두 번에 나눠 올려도 됩니다. 이어서 올려도 문제없습니다.
> 웹 업로드는 파일당 25MB까지 가능한데 가장 큰 곡이 4MB라 여유롭습니다.

### 2-대안. GitHub Desktop으로

파일이 많아 웹이 불편하면 GitHub Desktop이 편합니다.

1. desktop.github.com 에서 설치 후 로그인
2. `File` → `Clone repository`로 방금 만든 저장소를 내 컴퓨터에 받습니다
3. 받아진 폴더에 `index.html`, `.nojekyll`, `music` 폴더를 복사해 넣습니다
4. GitHub Desktop에 변경 파일이 뜨면 아래 요약란에 `add player` 입력 → **Commit to main**
5. 우측 상단 **Push origin**

### 2-대안. 명령줄로

```bash
cd 파일이_있는_폴더
git init
git add index.html .nojekyll README.md rename-music.py music
git commit -m "add player"
git branch -M main
git remote add origin https://github.com/<계정>/<저장소>.git
git push -u origin main
```

### 3. GitHub Pages 켜기

저장소 → **Settings** → 왼쪽 **Pages**

- Source: **Deploy from a branch**
- Branch: **main** / **/ (root)** → **Save**

1~2분 뒤 `https://<계정>.github.io/<저장소>/` 로 열립니다.

### 4. 확인

주소창에 음원 주소를 직접 넣어 봅니다.

```
https://<계정>.github.io/<저장소>/music/piano-01.mp3
```

재생기가 뜨면 성공입니다. 404가 나면 `music` 폴더가 저장소 최상단에
있는지, 파일 이름이 `piano-01.mp3` 형식인지 확인하세요.

## 전시장에서 쓰기

- 페이지를 열고 **재생 버튼을 한 번 눌러야** 시작됩니다. 브라우저 정책이라 우회할 수 없습니다.
- 위쪽 `⌄` 버튼을 누르면 전시 모드(전체화면)로 바뀌고 화면이 꺼지지 않습니다.
  이 기능은 HTTPS에서만 동작하므로 깃허브 페이지에서 제대로 작동합니다.
- 설정(`•••`)에서 크로스페이드와 곡 사이 여백을 조절합니다.
  솔로 피아노는 **여백 4~6초** 쪽이 자연스럽습니다.
- 랜덤은 전체를 한 바퀴 돈 뒤 다시 섞습니다. 같은 곡이 연달아 나오지 않습니다.

## 참고

- 33곡 약 66분입니다. 8시간 전시라면 7~8바퀴 돕니다.
  녹음을 추가하면 `music` 폴더에 `piano-34.mp3` 형식으로 넣고
  `index.html`의 `EX_LIST`에 `[34, 곡길이초]`를 추가하면 됩니다.
  번거로우면 설정의 **음악 폴더 통째로 불러오기**로 그때그때 불러와도 됩니다.
- 깃허브 페이지는 트래픽이 월 100GB로 넉넉하지만, 음원이 90MB라
  방문자가 아주 많아지면 Cloudflare Pages 쪽이 여유롭습니다.
