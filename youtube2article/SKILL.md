---
name: youtube2article
description: Convert YouTube videos into comprehensive, readable markdown articles with screenshots. Supports single videos and full channels. USE WHEN user provides a YouTube video URL, channel URL, or asks to convert/transcribe/extract a video.
---

# YouTube to Article Skill

Convert YouTube videos into comprehensive, richly illustrated markdown documents. Extracts the full transcript, formats it for readability, and captures key screenshots from the video.

## Quick Commands

| Say | Does |
|-----|------|
| "Convert this video: [URL]" | Single video → markdown article |
| "Process this channel: [URL]" | All videos in channel → numbered articles |
| "youtube2article [URL]" | Auto-detect: single video or channel |

## Requirements

- `yt-dlp` must be installed (for transcripts and video URLs)
- `ffmpeg` must be installed (for screenshot capture)
- `python3` must be available (for transcript cleaning)

---

## Mode 1: Single Video

### Process

#### Step 1: Ask for destination

Ask the user:
> **Where should this article be saved?** (e.g., `notes/`, `articles/`, or a specific folder path)

If the user has already specified a path, use it directly.

#### Step 2: Extract metadata

```bash
yt-dlp --print "%(title)s|||%(duration)s|||%(upload_date)s|||%(channel)s" --no-download --no-playlist "VIDEO_URL"
```

#### Step 3: Download transcript

```bash
yt-dlp --write-auto-sub --sub-lang en --sub-format vtt --skip-download --no-playlist -o "/tmp/yt2a/transcript" "VIDEO_URL"
```

#### Step 4: Clean transcript

Use Python to strip VTT headers, tags, timestamps, and deduplicate lines:

```python
import re

with open(vtt_path, 'r') as f:
    content = f.read()

content = re.sub(r'WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
content = re.sub(r'<[^>]+>', '', content)
content = re.sub(r' align:\w+ position:\d+%', '', content)
lines = content.strip().split('\n')
result = []
prev_text = ''
for line in lines:
    line = line.strip()
    if not line or re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', line):
        continue
    if line != prev_text and line != '[Music]':
        result.append(line)
        prev_text = line
text = ' '.join(result)
```

#### Step 5: Capture screenshots

Get the direct video URL and capture frames at key moments:

```bash
VURL=$(yt-dlp -f "best[height<=720]" --get-url --no-playlist "VIDEO_URL" | head -1)
```

Capture strategy:
- For videos **< 5 minutes**: every 30 seconds
- For videos **5-15 minutes**: every 45 seconds
- For videos **15-30 minutes**: every 60 seconds
- For videos **> 30 minutes**: every 90 seconds

Save to `images/` subfolder alongside the article. Use naming: `[safe_title]_XXXX.jpg` where XXXX is the second count.

```bash
ffmpeg -ss TIMESTAMP -i "$VURL" -frames:v 1 -q:v 2 "OUTPUT_PATH" -y
```

#### Step 6: Format the article

Write a markdown file with this structure:

```markdown
---
type: study
title: "[Video Title]"
date: [Upload date YYYY-MM-DD]
source: youtube
status: complete
channel: [Channel Name]
video_url: [Full URL]
tags:
  - [relevant tags]
  - full-transcript
---

# [Video Title]

**Channel:** [Channel Name]
**Video:** [YouTube Link](URL)
**Duration:** MM:SS

---

[Full transcript text, formatted as:]
- Proper paragraphs (break every ~150-200 words at sentence boundaries)
- Section headers (##) at natural topic breaks
- Screenshots inserted at corresponding timestamps: ![](images/filename.jpg)
- **Bold** key terms on first mention
- Code blocks for technical content
- > Blockquotes for notable statements

---

## Connections

[Wiki-links to related vault content — scan for matches]
- [[relevant area or project]]
- [[related notes]]
```

#### Step 7: Suggest connections

After writing, scan the vault for related content using grep and suggest wiki-links to add to the Connections section. Always suggest links — the user can edit later.

---

## Mode 2: Full Channel

### Trigger

When the URL contains `/@` or `/c/` or `/channel/` or ends with `/videos`.

### Process

#### Step 1: Confirm with the user

List all videos in the channel with titles and dates:

```bash
yt-dlp --print "%(upload_date)s|||%(id)s|||%(title)s" --no-download "CHANNEL_URL" | sort
```

Present as a numbered table and ask:
> **This channel has N videos. Process all of them? Or select specific numbers?**

#### Step 2: Ask for destination folder

> **Where should these articles be saved?** A subfolder will be created with the channel name.

#### Step 3: Create folder structure

```
[destination]/[Channel Name]/
├── images/
└── [numbered articles]
```

#### Step 4: Process each video

For each video, sorted oldest first (numbered 01, 02, ...):

1. Download transcript
2. Clean transcript
3. Capture screenshots
4. Write markdown article named: `NN - [Title].md`

Use parallel background jobs for screenshot capture where possible (batch by groups of 5).

**Important:** Get fresh video URLs for each batch — yt-dlp URLs expire after a few minutes.

#### Step 5: Create index note

After all videos are processed, create a `README.md` index:

```markdown
---
type: study
title: "[Channel Name] — Video Series Index"
date: [today]
source: youtube
channel: [Channel Name]
---

# [Channel Name]

[Brief channel description if available]

## Videos

| # | Title | Date | Duration |
|---|-------|------|----------|
| 01 | [[01 - Title]] | YYYY-MM-DD | MM:SS |
| 02 | [[02 - Title]] | YYYY-MM-DD | MM:SS |
...

## Connections
[Wiki-links to related vault content]
```

---

## Error Handling

- If no English subtitles are available, try: `--sub-lang en --write-auto-sub` (auto-generated)
- If transcript download fails, note it in the article and still capture screenshots
- If screenshot capture fails for a video (URL expiry), retry with a fresh URL
- If a video in a channel batch fails, continue with the rest and report failures at the end

## Notes

- Always create an `images/` subfolder — never dump images alongside markdown files
- Use `--no-playlist` for single videos to avoid accidentally downloading playlists
- For channels with 20+ videos, process in batches of 5 to manage URL expiry
- The full transcript is NEVER summarized — every sentence is preserved
- Format for maximum readability: paragraphs, headers, images, bold terms
- The `type: study` frontmatter and the Connections wiki-link section assume an Obsidian-style vault, so adopters who write plain Markdown can remove both
