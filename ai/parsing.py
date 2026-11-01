"""Turn raw model text into clean data. Small models are messy, so this is forgiving."""
import re

_BULLET = re.compile(r"^\s*(?:[-*\u2022]+|\d+[.)])\s*")
_INTRO = re.compile(r"(?i)^(here are|here is|here's|sure|certainly).*(title|option|idea)")


def clean(text):
    return text.replace("**", "").replace("__", "").strip()


def parse_lines(text, limit=10, max_len=100):
    """One item per line (titles). Drops numbering, quotes and intro sentences."""
    out, seen = [], set()
    for raw in clean(text).splitlines():
        line = _BULLET.sub("", raw).strip().strip("\"'\u201c\u201d`").strip()
        if not line or line.endswith(":") or len(line) > max_len or _INTRO.match(line):
            continue
        if line.lower() in seen:
            continue
        seen.add(line.lower())
        out.append(line)
        if len(out) == limit:
            break
    return out


def split_blocks(text, words="idea|concept|short"):
    """Split 'Idea 1: ... Idea 2: ...' output into one string per item."""
    text = clean(text)
    pattern = re.compile(rf"(?im)^[ \t#>*_-]*(?:{words})\s*#?\s*\d+\b")
    starts = [m.start() for m in pattern.finditer(text)]
    if not starts:
        return [text] if text else []
    return [text[a:b].strip() for a, b in zip(starts, starts[1:] + [len(text)])]


def parse_hashtags_keywords(text, max_tags=15, max_keywords=15, max_chars=480):
    """Return (hashtags, keywords) as two separate lists."""
    t = clean(text)
    h = re.search(r"(?is)hashtags?\s*:(.*?)(?=keywords?\s*:|$)", t)
    k = re.search(r"(?is)keywords?\s*:(.*)$", t)
    tags, seen = [], set()
    for tag in re.findall(r"#\w+", h.group(1) if h else t):
        if tag.lower() not in seen:
            seen.add(tag.lower())
            tags.append(tag)
    keywords, total, kseen = [], 0, set()
    for item in re.split(r"[,\n]", k.group(1) if k else ""):
        item = _BULLET.sub("", item).strip().strip("\"'")
        if not item or item.startswith("#") or item.lower() in kseen:
            continue
        if total + len(item) + 2 > max_chars:
            break
        kseen.add(item.lower())
        keywords.append(item)
        total += len(item) + 2
    return tags[:max_tags], keywords[:max_keywords]
