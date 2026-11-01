import json
import uuid
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

DEFAULT_SETTINGS = {
    "creator": "",
    "channel": "",
    "default_game": "Minecraft",
    "default_format": "YouTube Shorts",
    "hashtag_count": 12,
}


def _read(name, default):
    try:
        return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _write(name, data):
    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / name).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# ---------- Projects ----------
def load_projects():
    return _read("projects.json", [])


def add_project(kind, game, video_format, topic, content):
    items = load_projects()
    items.insert(0, {"id": uuid.uuid4().hex[:8], "kind": kind, "game": game,
                     "format": video_format, "topic": topic, "content": content,
                     "created": _now()})
    _write("projects.json", items)


def delete_project(pid):
    _write("projects.json", [p for p in load_projects() if p["id"] != pid])


def clear_projects():
    _write("projects.json", [])


def count_projects():
    return len(load_projects())


# ---------- Videos (performance tracking) ----------
def load_videos():
    return _read("videos.json", [])


def add_video(title, game, video_format, published, views, likes, comments):
    items = load_videos()
    items.insert(0, {"id": uuid.uuid4().hex[:8], "title": title, "game": game,
                     "format": video_format, "published": published, "views": views,
                     "likes": likes, "comments": comments, "created": _now()})
    _write("videos.json", items)


def update_video(vid, views, likes, comments):
    items = load_videos()
    for v in items:
        if v["id"] == vid:
            v.update(views=views, likes=likes, comments=comments)
    _write("videos.json", items)


def delete_video(vid):
    _write("videos.json", [v for v in load_videos() if v["id"] != vid])


def clear_videos():
    _write("videos.json", [])


# ---------- Settings ----------
def load_settings():
    return {**DEFAULT_SETTINGS, **_read("settings.json", {})}


def save_settings(settings):
    _write("settings.json", settings)
