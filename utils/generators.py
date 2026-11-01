import random

from utils import storage
from utils.templates import (
    COMMON_TITLE_TEMPLATES, DESCRIPTION_TEMPLATES, GAMES,
    GENERAL_HASHTAGS, THUMBNAIL_TIPS,
)
from utils.thumbnail_data import COMPOSITIONS, LIGHTING, VISUALS

MAX_TITLE_LENGTH = 100


def generate_titles(game, topic, video_format, count=8):
    topic = topic.strip()
    if not topic:
        return []
    templates = list(COMMON_TITLE_TEMPLATES[video_format])
    templates += GAMES[game]["title_templates"][video_format]
    random.shuffle(templates)
    titles = []
    for t in templates:
        title = t.format(topic=topic, game=game)
        if len(title) <= MAX_TITLE_LENGTH and title not in titles:
            titles.append(title)
        if len(titles) == count:
            break
    return titles


def generate_hashtags(game, topic, video_format, count=15):
    topic = topic.strip()
    tags = []
    slug = "".join(ch for ch in topic.lower() if ch.isalnum())
    if slug:
        tags += [f"#{slug}", f"#{game.lower().replace(' ', '')}{slug}"]
    game_tags = GAMES[game]["hashtags"][:]
    random.shuffle(game_tags)
    tags += game_tags[:8]
    tags += GENERAL_HASHTAGS[video_format]
    seen, result = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t)
            result.append(t)
    return result[:count]


def generate_descriptions(game, topic, video_format, count=2):
    topic = topic.strip()
    if not topic:
        return []
    channel = storage.load_settings()["channel"].strip()
    hooks = GAMES[game]["description_hooks"][:]
    random.shuffle(hooks)
    results = []
    for hook in hooks[:count]:
        tags = " ".join(generate_hashtags(game, topic, video_format, 8))
        text = DESCRIPTION_TEMPLATES[video_format].format(
            hook=hook.format(topic=topic, game=game), game=game, hashtags=tags)
        if channel:
            text = text.replace("Subscribe for more", f"Subscribe to {channel} for more")
        results.append(text)
    return results


def generate_thumbnail_ideas(game, topic, count=4):
    topic = topic.strip()
    if not topic:
        return []
    data = GAMES[game]
    vis = VISUALS[game]
    comps = random.sample(COMPOSITIONS, count)
    lights = random.sample(LIGHTING, count)
    subjects = random.sample(vis["subjects"], min(count, len(vis["subjects"])))
    backs = random.sample(vis["backgrounds"], min(count, len(vis["backgrounds"])))
    ideas = random.sample(data["thumbnail_ideas"], min(count, len(data["thumbnail_ideas"])))
    texts = random.sample(data["thumbnail_text"], len(data["thumbnail_text"]))
    out = []
    for i in range(count):
        out.append({
            "idea": ideas[i % len(ideas)].format(topic=topic, game=game),
            "composition": f"{comps[i][0]}: {comps[i][1]}",
            "subject": subjects[i % len(subjects)].format(topic=topic),
            "background": backs[i % len(backs)],
            "lighting": f"{lights[i][0]}: {lights[i][1]}",
            "palette": vis["palette"],
            "text": texts[i % len(texts)],
        })
    return out


def random_tip():
    return random.choice(THUMBNAIL_TIPS)
