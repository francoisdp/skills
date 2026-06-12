# youtube2article

A skill that turns a YouTube video or a whole channel into a readable Markdown article, with the full transcript cleaned into proper prose and key frames captured as screenshots placed at the moments they illustrate. It works on a single video or on every video in a channel and never summarises the transcript, so the article keeps every sentence the speaker said while reading as an article rather than as a wall of timestamped captions.

## What it does

Give the skill a video URL and it extracts the metadata, downloads the transcript, cleans the caption artifacts into flowing paragraphs with section headings, captures screenshots at a spacing chosen from the video length, then writes a single Markdown file with the images placed inline. Give it a channel URL and it lists the videos, asks which to process, then produces one numbered article per video together with an index that links them. The transcript is preserved in full at every step, since the goal is a faithful readable record rather than a précis.

## Installation

The skill is a folder containing a single `SKILL.md`, which most tools discover automatically once the folder sits in the right place. The folder must be named `youtube2article` so it matches the skill name declared in the frontmatter.

For **Claude Code**, copy the folder into your skills directory. For a user-level install that applies across all your projects, place it at `~/.claude/skills/youtube2article/`. For a project-level install that applies inside one project, place it at `.claude/skills/youtube2article/` within that project. Claude Code discovers the skill from its frontmatter, so there is nothing further to configure.

For **Claude Desktop and claude.ai**, skills are added through the application settings rather than the filesystem, so look under settings for an entry named "Skills" or "Capabilities" and add the skill there.

For **Copilot CLI**, skills are auto-discovered from installed plugins, so the same `SKILL.md` works through the `skill` tool once the plugin that carries it is installed.

For **Gemini CLI**, skills activate through the `activate_skill` mechanism, with the frontmatter loaded at session start.

For **any other tool**, the skill is plain Markdown, so you can paste its steps into a system prompt or into an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

This skill drives three command-line tools, so install them before first use. It needs `yt-dlp` for transcripts and video URLs, `ffmpeg` for screenshot capture and `python3` for the transcript cleaning step. On macOS these install through Homebrew with `brew install yt-dlp ffmpeg python` and on most Linux systems through the package manager or `pip` for `yt-dlp`.

## Usage

Trigger the skill by giving it a URL with one of the phrases it recognises. Say "Convert this video: <URL>" for a single video, "Process this channel: <URL>" for a channel, or "youtube2article <URL>" to let it detect which one you gave it. A channel URL is one that contains `/@`, `/c/` or `/channel/`, or that ends in `/videos`.

For a single video the skill asks where to save the article, extracts the metadata, downloads and cleans the transcript, captures the screenshots into an `images/` subfolder, then writes the Markdown file with the frames placed at their timestamps. For a channel it lists the videos and asks which to process, creates a folder named after the channel, writes one numbered article per video oldest first, then builds an index that links them all. If a video has no English subtitles it falls back to the auto-generated track. If a step fails for one video in a channel batch it records the failure and carries on with the rest.

## Rationale

The skill exists because the useful content of a video is locked inside audio and moving images, which you cannot search, quote, link or skim. A transcript alone is not enough, since raw captions arrive as deduplicated fragments with timestamps and music markers rather than as readable sentences, so the cleaning step strips the WEBVTT headers, the inline tags, the position markers and the repeated lines, then joins what remains into prose. Reading is then helped by structure, so the skill breaks the text into paragraphs at sentence boundaries roughly every 150 to 200 words, adds section headings at natural topic breaks, bolds key terms on first mention, then places screenshots at the moments they illustrate, because a wall of unbroken text from a thirty-minute talk is as hard to use as the video itself.

The screenshot spacing scales with length rather than staying fixed, so a short video gets a frame every 30 seconds while a long one gets a frame every 90 seconds, which keeps the article illustrated without burying the text under near-identical images. The transcript is never summarised, because the value of the output is that it is the complete record, faithful to what was said, which a summary would quietly discard. The channel mode adds an index and numbers the articles oldest first, so a series reads in the order it was published and a reader can move between episodes through the links. The fresh-URL handling and the batching of five exist for a practical reason, which is that the direct video URLs from yt-dlp expire after a few minutes, so a long channel run must refetch URLs in small groups rather than collect them all at the start.

## Extension guide

The skill is plain Markdown, so customising it means editing `SKILL.md`.

The generated article carries an Obsidian-oriented shape that you may want to change. The frontmatter sets `type: study` and `status: complete`, which are note conventions rather than anything the skill needs, so edit the frontmatter block in Step 6 to match your own conventions or remove the fields you do not use. The article also ends with a Connections section of wiki-links and a step that scans a vault for related notes, which only does useful work inside an Obsidian-style vault, so a plain-Markdown user can delete the Connections section and the "Suggest connections" step without affecting the transcript or the screenshots.

To change how the text is broken up, edit the formatting instructions in Step 6, where the paragraph length, the heading policy and the bold-term rule are stated. To change the screenshot density, edit the capture-strategy table that maps video length to frame spacing, raising or lowering the seconds between frames. To change the file naming or the folder structure, edit the naming rules in Step 5 for single videos and in the channel folder-structure block for series. To support a language other than English, change the `--sub-lang en` flag in the transcript steps to the language code you need.

## Repository layout

```
youtube2article/
├── SKILL.md     the full skill: requirements, single-video mode, channel mode, error handling
├── README.md    this file
└── LICENSE      MIT licence
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
