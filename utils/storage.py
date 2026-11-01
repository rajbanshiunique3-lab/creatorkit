import json
import uuid
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "projects.json"


def load_projects():
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _write(projects):
    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(projects, indent=2, ensure_ascii=False), encoding="utf-8")


def add_project(kind, game, video_format, topic, content):
    projects = load_projects()
    projects.insert(0, {
        "id": uuid.uuid4().hex[:8],
        "kind": kind,
        "game": game,
        "format": video_format,
        "topic": topic,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    _write(projects)


def delete_project(project_id):
    _write([p for p in load_projects() if p["id"] != project_id])


def count_projects():
    return len(load_projects())
