# Skill vetting report (Oct 8, 2026, round 2)

All 29 candidate repos (11 from the brief, 18 found online) were read as data. Nothing was installed or executed.
Goals for round 2: no AI-sounding writing, copy Sal's voice exactly, viral content that works. US English. No em dashes anywhere.

## Final top five (pending Sal's approval)
| # | Job | Skill(s) | Verdict | Edits before install |
|---|---|---|---|---|
| 1 | **Copy Sal's voice** | TravinDSO/myvoice-skill (`my-voice`) + `stylometry.py` from serafinsanchez/voicedna | SAFE | MYVOICE.md: "English: US", hard ban on em and en dashes that the voice file can never override, channel rows (video script, photo-text, LinkedIn carousel, LinkedIn text). Learning from edits only after Sal says "final". Use stylometry.py alone (stdlib, offline). Skip its setup script, embeddings and the LUAR model (downloads and runs third-party code). |
| 2 | **Kill AI slop** | petergyang/no-ai-slop | SAFE | Hard dash ban with a final scan. US spelling. Add blader/humanizer's triads, hedging, sycophancy and AI-vocab list (credited). New "spoken script" section: write for the ear, ~150 wpm, first line is the claim, no "here's the thing", no kicker endings. Voice line: no guru framing, no sales language. |
| 3 | **Short-form viral engine** (Reels, TikTok, Shorts) | Jakeschincariol/instagram-agent-skill: `ig-reel`, `ig-viral`, `ig-human` + vyralcontent `viral-short-form-ideas` | SAFE / SAFE w/ caveats | Jake: copy only those 3 folders. Stdlib Python, no network, no posting. Its hook scorer is honest (only kills weak hooks) and it never invents numbers. `ig-viral` ranks creators' videos against their own median, which is exactly the "steal the skeleton" method. Skip its optional yt-dlp step. Vyral: delete the paid-tool pitch in the file. |
| 4 | **LinkedIn** (carousel PDF + text post) | Jakeschincariol/linkedin-agent-skill: `li-post`, `li-carousel`, `li-human` | SAFE | Copy only those 3. Each says "never publish". Change log path from `~/.claude/linkedin/` to the project. Set post length to 900-1300 chars. Carousel is 1080x1350 HTML to PDF, approved copy first. |
| 5 | **Motion slides** | Remotion official skills + haidrrrry `remotion-motion-graphics` style layer | SAFE / SAFE w/ caveats | Pin versions. Remove haidrrrry's mandatory auto-render loop and "use EVERY time" trigger. Local SFX only. **Remotion license: free only at 3 or fewer employees.** |

Optional sixth: blader/humanizer (24k stars) as a detect-only audit before Sal approves a draft.

## Pipeline
idea (ig-viral, viral-short-form-ideas) -> script (ig-reel / li-post / li-carousel) -> voice pass (my-voice) -> slop pass (no-ai-slop + ig-human/li-human scripts) -> stylometry check (em dash = hard fail) -> **Sal approves** -> film / Remotion -> Storias -> Sal posts by hand.

## Replaced from round 1
| Was | Replaced by | Why |
|---|---|---|
| charlie947 voice-builder, post-writer, content-matrix | my-voice; li-post | my-voice learns from Sal's edits and handles spoken transcripts; li-post is LinkedIn-native with a never-publish rule. |
| vyralcontent viral-hooks | Jake ig-reel | Spoken + on-screen hook pairs, timed beat sheet with loop check, no invented stats. |
| sergebulaev hook extractor / planner / carousel planner | Jake ig-viral, li-carousel | Same jobs, no posting code in the repo at all. |

## Cut (round 2)
| Skill | Why |
|---|---|
| hardikpandya/stop-slop | Absolute rules flatten voice (no adverbs, no "What/Why/How" openers kills spoken hooks). Uses an em dash in its own examples. |
| conorbronsdon/avoid-ai-writing | Broadest coverage but overkill, runs node scripts, and its LinkedIn profile allows em dashes. |
| Byk3y/no-slop | Thin, allows em dashes. |
| jooray/humanizer | 70KB bloated fork of blader. |
| zachthieme capturing-voice, lout33, claude-voice-editor | Wrong fit; voice-editor adds em dashes and invents experiences. |
| jzOcb/writing-style-skill | **Avoid.** Auto-rewrites its own rules with no review, logs text to home dir. |
| rediumvex/viral-hooks-skill | Generic templates, made-up stats, clickbait. |
| coreyhaines31/marketingskills | Good reference only (carousel frameworks); scheduling via Buffer/Typefully, agency upsells. |
| assafkip/linkedin-brand | Unsourced reach stats as rules, third-party MCP, Gumroad funnel. |
| AgriciDaniel/claude-youtube | Long-form focus, invented retention forecasts, API keys. |

## Cut (round 1)
carousel-lite (no license), rediumvex captions (sales words), charlie947 reels-scripting (paid APIs), FefeRP (16:9 only), aaaronmiller (fabricated stats), guyaga (**avoid**: posts, schedules, DMs).

## Hard rules for the install
- Project-level only (`.claude/skills/`). No global installs.
- No posting or scheduling credentials (Publora, upload-post, Buffer, Apify) in any `.env`.
- Nothing posts. Every skill outputs drafts; Sal posts by hand.
- Renders only on Sal's explicit "render".

## Round 3: final check before install (Oct 8)
Searched skill directories and leaderboards again. Challengers vetted head to head:
- aboudjem/humanizer-skill (55 patterns, 0-100 score): keeps petergyang. Its "soul injection" invents details, its score is self-graded, and it fixes em dashes with hyphens.
- trailofbits humanizer: does not exist in trailofbits/skills.
- angelarose210/ghostwriter: keeps my-voice. Referenced scripts and templates are missing; generic sliders flatten voice.
Nothing beat the top five.

## Installed (project-level, `.claude/skills/`)
| Skill | Source (license) | Edits made |
|---|---|---|
| my-voice | TravinDSO/myvoice-skill (MIT) | Dash ban can never be overridden; US English; draft-only; [spoken] samples; runs voicecheck.py |
| my-voice/scripts/voicecheck.py | written for Sal (voicedna's stylometry.py has no license, so not copied) | Dash hard fail + drift vs samples |
| no-ai-slop | petergyang/no-ai-slop (MIT) | Hard dash ban; blader patterns (credited); spoken-script, format, voice and approval sections |
| ig-reel, ig-viral, ig-human | Jakeschincariol/instagram-agent-skill (MIT) | Data paths moved into project; reads MYVOICE.md; Sal's rules block; US spelling |
| li-post, li-carousel, li-human | Jakeschincariol/linkedin-agent-skill (MIT) | Same as above |
| viral-short-form-ideas | vyralcontent/content-skills (MIT) | Paid-tool pitch and banner removed |
| remotion-best-practices, -create, -markup, -captions, -render, -studio | remotion-dev/skills | create-video pinned to 4.0.534 |
| remotion-motion-graphics | haidrrrry/claude-remotion-skill (MIT) | "EVERY time" trigger softened; full render only on "render" |

Tested: humanize.py, detect.py, hookscore.py, voicecheck.py run offline. Note: humanize.py turns an em dash into ", " which can leave "paid., nobody". Use `--report` and fix by hand (rule is in each skill).
