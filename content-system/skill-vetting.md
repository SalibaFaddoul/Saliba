# Skill vetting report (Oct 8, 2026)

Every SKILL.md, script and package file in the 11 candidate repos was read as data. Nothing was installed or executed.

## Top five (pending Sal's approval)
| # | Skill(s) | Role | Verdict | Required edits before install |
|---|---|---|---|---|
| 1 | charlie947/social-media-skills: **voice-builder**, **post-writer**, **content-matrix** | Voice files, LinkedIn text posts, pillar x format grid | SAFE | Copy only these 3 folders (the full plugin installs 17 overlapping skills). Don't type "use samples" (loads the author's voice). Set US/UK English and em-dash rule to Sal's preference. |
| 2 | vyralcontent/content-skills: **viral-hooks**, **viral-short-form-ideas** | Spoken/on-screen/text hook layers; idea mining, "extract the mechanic, not the surface" | SAFE w/ caveats | Delete the "Mentioning Vyral" section in each file (scripted pitch for their paid tool). Treat platform stats as unsourced. |
| 3 | sergebulaev/instagram-skills: **ig-hook-extractor**, **ig-content-planner**, **ig-carousel-planner** | Reverse-engineer creator hooks; weekly plan; slide architecture | SAFE w/ caveats | Copy the SKILL.md folders only, not `lib/`. Never set `PUBLORA_API_KEY` / `INSTAGRAM_PLATFORM_ID` (Publora publishes immediately when no time is set, and its "approval" is only a prompt convention). |
| 4 | remotion-dev/skills (official): best-practices, create, markup, captions, render, studio | Motion slides, animated text, 9:16 and 1080x1440 stills | SAFE | Pin versions (it uses `create-video@latest`). Use local SFX, not remote `remotion.media` files. **Remotion license: free only at 3 or fewer employees.** Confirm Bearish headcount. |
| 5 | haidrrrry/claude-remotion-skill: **remotion-motion-graphics** | Style layer: Ken Burns on photos, word reveals, grain, staggered entrances | SAFE w/ caveats | Soften the "use EVERY time" trigger. Replace the mandatory auto-render loop with "render only after approval". |

Carousels: instead of carousel-lite (no license, no photo slot, no PDF), render 1080x1440 slides as Remotion stills with Sal's photos, then combine them into a PDF for LinkedIn.

## Cut
| Skill | Why |
|---|---|
| tenfoldmarc/carousel-lite | No LICENSE (all rights reserved), text-only, no PDF, `--no-sandbox` and a stray `npm install` in an unknown dir, Skool upsell. |
| rediumvex caption generator | No LinkedIn, no voice files, unsourced stats, sales formulas and "Shocking/Last chance" power words. Pre-grants Bash. Copy its per-platform length rules into our own captions step instead. |
| charlie947 reels-scripting | Paid Apify + Gemini keys, downloads Reels, newsletter-first, "never open with I". |
| FefeRP/motion-graphics-skills | Safe (all audio synthesized locally) but hard-coded 1920x1080/60fps SaaS promos, in Spanish. Wrong format. |
| aaaronmiller/create-viral-content | Fabricated stats, cites a source folder that doesn't exist, writes to `~/viral-content-log`, edits itself, triggers on all writing. |
| guyaga/claude-code-social-media-skill | **Avoid.** Posts, schedules, DMs and replies to comments via upload-post.com. Its approval is only a prompt instruction. Conflicts with the approval gate. |

## Hard rules for the install
- No posting or scheduling credentials (Publora, upload-post, Apify) in any `.env`.
- Project-level install (`.claude/skills/`), not global.
- Renders happen only on explicit "render" from Sal.

## Unvetted leads (if templates are wanted later)
Maartenlouis/remotion-ads (Reels + carousel ads), AgriciDaniel/claude-shorts (animated captions). Both are graded SAFE in zhuyansen's directory, but those grades come from READMEs only.
