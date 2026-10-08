#!/usr/bin/env python3
"""Compare a draft against Sal's samples. Stdlib only, offline.

Hard fail: any em dash, en dash, or spaced hyphen used as a dash.
Drift: flags metrics more than --threshold standard deviations from the samples.

  python3 voicecheck.py --samples a.md b.md --draft draft.md
"""
import argparse, re, statistics, sys

DASH = re.compile(r"—|–| - ")
CONTRACTION = re.compile(r"\b\w+'(s|t|re|ve|ll|d|m)\b", re.I)

def metrics(text):
    text = text.replace("’", "'")
    words = re.findall(r"[A-Za-z0-9']+", text)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if re.search(r"\w", s)]
    lens = [len(re.findall(r"[A-Za-z0-9']+", s)) for s in sents] or [0]
    n = max(len(words), 1)
    return {
        "avg_sentence_words": statistics.mean(lens),
        "sentence_variation": statistics.pstdev(lens) / (statistics.mean(lens) or 1),
        "contractions_per_100": 100 * len(CONTRACTION.findall(text)) / n,
        "avg_word_length": sum(len(w) for w in words) / n,
        "i_per_100": 100 * sum(w.lower() in ("i", "i'm", "i've", "i'd", "i'll", "me", "my") for w in words) / n,
        "questions_per_100": 100 * text.count("?") / n,
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--samples", nargs="+", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--threshold", type=float, default=1.5)
    a = ap.parse_args()
    draft = open(a.draft, encoding="utf-8").read()
    dashes = DASH.findall(draft)
    print(f"DASHES: {len(dashes)} {'FAIL' if dashes else 'ok'}")
    base = [metrics(open(p, encoding="utf-8").read()) for p in a.samples]
    d = metrics(draft)
    drift = 0
    for k, v in d.items():
        vals = [b[k] for b in base]
        mu = statistics.mean(vals)
        sd = statistics.pstdev(vals) if len(vals) > 1 else 0
        sd = max(sd, abs(mu) * 0.25, 0.5)  # floor so 1-2 samples still give a sane band
        z = (v - mu) / sd
        flag = "DRIFT" if abs(z) > a.threshold else "ok"
        drift += flag == "DRIFT"
        print(f"{k:22} draft {v:6.2f}  samples {mu:6.2f}  z {z:+5.2f}  {flag}")
    print("RESULT:", "FAIL" if dashes else ("REVIEW" if drift else "PASS"))
    sys.exit(1 if dashes else 0)

if __name__ == "__main__":
    main()
