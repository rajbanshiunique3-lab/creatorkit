"""Prompt builders. Each returns (system_prompt, user_prompt)."""

SYSTEM = (
    "You are an expert YouTube gaming strategist. Follow the requested format exactly. "
    "Never add introductions, explanations or closing remarks. Never invent facts, "
    "statistics or features of the game. Keep everything honest and not misleading."
)

TITLE_STYLES = {
    "Catchy": "punchy, emotional and easy to say out loud",
    "Professional": "clear, polished and informative, with no clickbait",
    "Curiosity": "open loops that make people want the answer, without lying",
    "Funny": "playful and humorous, meme-friendly but never offensive",
    "SEO-focused": "start with the main keyword and use natural phrases people search for on YouTube",
}


def titles(game, fmt, style, topic, count=10):
    return SYSTEM, (
        f"Write exactly {count} YouTube titles for a {game} {fmt} about: {topic}\n"
        f"Style: {TITLE_STYLES[style]}.\n"
        "Rules:\n- Each title is under 70 characters\n"
        "- One title per line, no numbering, no quotes, no extra text\n"
        "- Every title must honestly match the topic"
    )


def description(game, fmt, topic, details, keywords, chapters, cta, channel):
    shorts = fmt == "YouTube Shorts"
    parts = [
        f"Write a YouTube description for a {game} {fmt} about: {topic}",
        f"What happens in the video: {details}" if details else "",
        f"Naturally include these keywords: {keywords}" if keywords else "",
        "Structure:",
        "1. A natural 2-3 sentence introduction that hooks the viewer.",
        "2. A short summary of what happens in the video.",
    ]
    n = 3
    if chapters and not shorts:
        parts.append(f"{n}. A 'Chapters:' list of 5-7 lines like '00:00 Intro'. Use placeholder "
                     "timestamps in increasing order.")
        n += 1
    if cta:
        who = f" for {channel}" if channel else ""
        parts.append(f"{n}. A short call to action asking viewers to like, comment and subscribe{who}.")
        n += 1
    parts.append(f"{n}. A final line with 3-5 relevant hashtags.")
    parts.append("Plain text only. No markdown, no headings with #." +
                 (" Keep it under 100 words." if shorts else " Keep it under 250 words."))
    return SYSTEM, "\n".join(p for p in parts if p)


def hashtags(game, fmt, topic):
    return SYSTEM, (
        f"Create hashtags and search keywords for a {game} {fmt} about: {topic}\n"
        "Output exactly these two lines and nothing else:\n"
        "HASHTAGS: #tag1 #tag2 ... (10 to 15 hashtags, no spaces inside a hashtag)\n"
        "KEYWORDS: phrase one, phrase two, ... (10 to 15 search phrases people type into YouTube)\n"
        "Rules: only use tags that truly match this video and game. Do not use other games, "
        "other creators' names or unrelated viral tags. Hashtags and keywords must be different things."
    )


def video_ideas(game, fmt, theme, audience, count=5):
    return SYSTEM, (
        f"Create {count} original video ideas for a {game} YouTube channel.\n"
        f"Video type: {fmt}. Audience: {audience}.\n"
        + (f"Theme or starting point: {theme}\n" if theme else "")
        + "Use exactly this format for every idea:\n"
        "Idea 1: <short name>\nConcept: <2 sentences>\nHook: <the opening line of the video>\n"
        "Titles:\n- <title>\n- <title>\n- <title>\n"
        "Ideas must be realistic to film in the game."
    )


def thumbnails(game, fmt, topic, count=4):
    return SYSTEM, (
        f"Create {count} thumbnail concepts for a {game} {fmt} about: {topic}\n"
        "Use exactly this format for every concept:\n"
        "Concept 1: <short name>\nText: <maximum 3 words>\nComposition: <where things sit in the frame>\n"
        "Colors: <main colors>\nVisual elements: <characters, objects, effects>\n"
        "These are written concepts for a designer, not images."
    )


def shorts(game, theme, count=5):
    return SYSTEM, (
        f"Create {count} YouTube Shorts concepts for a {game} channel.\n"
        + (f"Theme: {theme}\n" if theme else "")
        + "Use exactly this format for every Short:\n"
        "Short 1: <short name>\nHook: <what happens in the first 3 seconds>\n"
        "Script: <4-6 short spoken lines, under 45 seconds in total>\n"
        "On-screen text: <max 6 words>\nTitle: <title under 60 characters>"
    )
