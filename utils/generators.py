import random

from utils.templates import (
    COMMON_TITLE_TEMPLATES, DESCRIPTION_TEMPLATES, GAMES,
    GENERAL_HASHTAGS, THUMBNAIL_TIPS,
)

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
    hooks = GAMES[game]["description_hooks"][:]
    random.shuffle(hooks)
    results = []
    for hook in hooks[:count]:
        tags = " ".join(generate_hashtags(game, topic, video_format, 8))
        results.append(DESCRIPTION_TEMPLATES[video_format].format(
            hook=hook.format(topic=topic, game=game), game=game, hashtags=tags))
    return results


def generate_thumbnail_ideas(game, topic, count=4):
    topic = topic.strip()
    if not topic:
        return []
    data = GAMES[game]
    ideas = data["thumbnail_ideas"][:]
    random.shuffle(ideas)
    texts = data["thumbnail_text"][:]
    random.shuffle(texts)
    out = []
    for i, idea in enumerate(ideas[:count]):
        out.append({"idea": idea.format(topic=topic, game=game),
                    "text": texts[i % len(texts)]})
    return out


def random_tip():
    return random.choice(THUMBNAIL_TIPS)
