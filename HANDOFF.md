# HANDOFF: Sal's viral content system (Storias)

Last updated: Oct 8, 2026. Branch: `claude/storias-viral-content-system-lx5nf0`.
A new Claude session (local or cloud) should read this file, then `CLAUDE.md`, then `content-system/decisions.md`.

## The goal
Build a repeatable content system that grows Sal's personal channels (IG, TikTok, YouTube Shorts, LinkedIn) at 3 to 5 pieces a day per platform. Pure free value. Business goal is Storias sales (first 50 paying users, then 100), but posts never sell. Method: copy top creators' skeleton (format, hook structure, pacing) with Sal's own story. Nothing is ever posted or scheduled by Claude.

## What's done
1. **Open items decided** (`content-system/decisions.md`):
   - On camera plus photo-with-text posts. Always Sal, never an avatar.
   - Hero claim confirmed true: "I launched to an audience of zero. One week later: 10 paying customers."
   - Founder-first audience (build in public).
   - US English. No em dashes or en dashes, ever.
2. **Skills researched in 3 rounds** (`content-system/skill-vetting.md`): 32 repos read in full, nothing executed. Top five picked, challengers compared head to head.
3. **Skills installed** in `.claude/skills/`, each edited for Sal's rules (dash ban, US English, draft only, no invented facts, no guru or sales hooks):
   - Voice: `my-voice` (+ `my-voice/scripts/voicecheck.py`, written for Sal: dash hard fail + drift vs his samples)
   - Anti AI writing: `no-ai-slop`
   - Short-form: `ig-reel`, `ig-viral`, `ig-human`, `viral-short-form-ideas`
   - LinkedIn: `li-post`, `li-carousel`, `li-human`
   - Motion: `remotion-*` official set + `remotion-motion-graphics` (render only on "render")
4. **Project rules** in `CLAUDE.md`.

## Where we are right now
- **Step 3 of the plan: voice setup.** 35 interview questions were sent to Sal: `content-system/voice/questions.md`. He is answering in his own voice. Put his answers in `content-system/voice/answers.md` verbatim.
- **TikTok transcripts: blocked in the cloud session** (network policy denied www.tiktok.com). A local session does not have that block. Do this locally (see below).

## Next steps, in order
1. **Get Sal's TikTok scripts** (account "Saliba Faddoul Jr", handle not confirmed; best guess `@salibafaddouljr`, ask Sal). Locally:
   ```bash
   python3 -m venv .venv && . .venv/bin/activate && pip install yt-dlp faster-whisper
   yt-dlp --flat-playlist -J "https://www.tiktok.com/@HANDLE" > content-system/voice/tiktok/list.json
   yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*,eng.*" --write-info-json \
     -o "content-system/voice/tiktok/raw/%(upload_date)s_%(id)s.%(ext)s" "https://www.tiktok.com/@HANDLE"
   ```
   If a video has no captions, download audio only (`-x --audio-format mp3`) and transcribe locally with faster-whisper (`small.en`). Never upload his audio to a third-party service. Write one `YYYY-MM-DD_<id>.md` per video (URL, date, views, likes, comments, shares, caption, clean transcript), an `index.md` table, and `content-system/voice/tiktok-analysis.md` (topics, beliefs, verbatim first lines, pacing, signature phrases, endings, best videos vs his median views). Keep `raw/` and audio out of git.
2. **Build `MYVOICE.md`** at the repo root with the `my-voice` skill from: TikTok transcripts (label [spoken]) + interview answers. Must include: "English variety: US", a core rule banning em dashes, en dashes and spaced hyphens as dashes, and channel rows for video script, photo-text post, LinkedIn carousel, LinkedIn text post. Show it to Sal before saving.
3. **Open question for Sal:** how many employees Bearish has. Remotion is free only at 3 or fewer; above that it needs a company license.
4. **Draft a 7-day content plan** (brief step 4): per day, per platform pieces, each with hook, skeleton source, platform adaptation, CTA word, AI-label note. LinkedIn = 2 native pieces a day (carousel + 900 to 1300 char text post), not recut video.
5. **Wait for Sal's approval** before producing anything. Sal posts by hand.

## Drafting pipeline (once MYVOICE.md exists)
idea (`ig-viral`, `viral-short-form-ideas`) -> script (`ig-reel` / `li-post` / `li-carousel`) -> `my-voice` -> `no-ai-slop` -> `ig-human` or `li-human` with `--report` (fix by hand; its auto em-dash swap can leave "paid., nobody") -> `voicecheck.py` (any dash = fail) -> **Sal approves** -> film or Remotion -> Storias -> Sal posts.

## Context from the original brief
- Storias: AI video "director". One recording becomes a finished short and a long-form video. Competitors: Opus Clip, Submagic, Captions. 1 credit = 1 second of finished video. Starter $9.99/mo ($8.99 yearly). Targets real estate agents (open.storiasai.com, /for/real-estate). Owned by Bearish.
- Never: personal wealth, selling in the post, any sale or acquisition of Bearish OS. Not a guru, not soft.
- Google Drive "Founder Saliba v2.0" folder is mostly empty shells. Real file: "Content Ideas, October 6, 2026" (hero script, hook bank, 3 borrowed patterns: comment-word CTA, numbered series, named-authority hook; from 11 studied creators).
- Platform notes (Oct 2026, from articles, verify against Sal's analytics): IG ranks on watch time, sends and likes per reach, 5 hashtag cap, Trial Reels for testing. TikTok: first seconds and completion matter; label realistic AI content. Shorts: original content ranks higher, series feature exists, don't delete and repost. LinkedIn: document carousels lead, first 60 to 90 minutes decide reach, external links cost reach.
