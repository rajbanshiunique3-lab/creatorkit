"""
Template data for CreatorKit.

Placeholders you will see inside the text:
    {topic}  -> what the video is about (e.g. "Hardcore Survival")
    {game}   -> the game name (e.g. "Minecraft")
"""

GAME_NAMES = ["Minecraft", "GTA V", "Roblox"]
VIDEO_FORMATS = ["YouTube Shorts", "Long Video"]


# ---------------------------------------------------------------
# Titles that work for every game
# ---------------------------------------------------------------
COMMON_TITLE_TEMPLATES = {
    "YouTube Shorts": [
        "{topic} in {game} 😱",
        "This {game} {topic} trick is INSANE",
        "I tried {topic} in {game} (it worked!)",
        "{topic} gone wrong in {game} 💀",
        "Nobody knows this {topic} secret in {game}",
        "{game}: {topic} in 60 seconds",
        "POV: you try {topic} in {game}",
        "Wait for the end... {topic} in {game}",
    ],
    "Long Video": [
        "I Spent 24 Hours on {topic} in {game}",
        "{topic} in {game}: The Complete Guide",
        "I Tried {topic} in {game} So You Don't Have To",
        "The Truth About {topic} in {game}",
        "{topic} in {game} Was Harder Than I Expected",
        "How to Master {topic} in {game} (Beginner to Pro)",
        "{game} {topic}: Everything You Need to Know",
        "I Challenged My Friends to {topic} in {game}",
    ],
}


# ---------------------------------------------------------------
# Game-specific data
# ---------------------------------------------------------------
GAMES = {
    "Minecraft": {
        "icon": "⛏️",
        "topic_ideas": [
            "Hardcore Survival", "Speedrun", "Redstone Build", "Mega Base",
            "Mob Farm", "Ender Dragon Fight", "100 Days Challenge",
        ],
        "title_templates": {
            "YouTube Shorts": [
                "Minecraft but {topic} 😳",
                "The BEST {topic} build in Minecraft",
                "Minecraft {topic} hack you need to know",
            ],
            "Long Video": [
                "I Survived 100 Days of {topic} in Minecraft Hardcore",
                "Minecraft But {topic} Is Impossible",
                "I Built the Ultimate {topic} in Minecraft Survival",
            ],
        },
        "hashtags": [
            "#minecraft", "#minecraftmemes", "#minecraftbuilds", "#minecrafthardcore",
            "#minecraftsurvival", "#minecraftpe", "#minecraftjava", "#minecraftshorts",
            "#minecraftcommunity", "#minecraftgameplay", "#minecraftredstone", "#mcyt",
        ],
        "thumbnail_ideas": [
            "Split screen: your tiny player on the left, a giant glowing {topic} on the right, with a red arrow between them.",
            "Close-up of your skin looking shocked, a creeper peeking over your shoulder, bright yellow text on a dark cave background.",
            "Before and After: a dirt hut next to an epic {topic} build, with a bold 'BEFORE / AFTER' label.",
            "A massive Ender Dragon behind your character with purple lightning and the text 'IMPOSSIBLE?'.",
        ],
        "thumbnail_text": ["IMPOSSIBLE?", "100 DAYS", "I SURVIVED", "TOO EASY", "NEVER AGAIN"],
        "description_hooks": [
            "Today in Minecraft we take on {topic}, and things get wild.",
            "In this Minecraft video, I try {topic} and show you exactly how it works.",
        ],
    },
    "GTA V": {
        "icon": "🚗",
        "topic_ideas": [
            "Police Chase", "Super Car Race", "Heist", "Stunt Jump",
            "Funny Moments", "Roleplay", "Secret Location",
        ],
        "title_templates": {
            "YouTube Shorts": [
                "GTA V {topic} that looks FAKE 🤯",
                "GTA 5 {topic} you can't miss",
                "The most insane {topic} in GTA V",
            ],
            "Long Video": [
                "GTA V: I Tried the Most Dangerous {topic}",
                "Surviving a 5-Star {topic} in GTA V",
                "GTA 5 {topic} Gone Completely Wrong",
            ],
        },
        "hashtags": [
            "#gta5", "#gtav", "#gtaonline", "#gta5funny", "#gta5shorts",
            "#gtavroleplay", "#gta5mods", "#gta5stunts", "#grandtheftauto",
            "#gtaclips", "#gta5gameplay", "#rockstargames",
        ],
        "thumbnail_ideas": [
            "Your character jumping off a helicopter with a giant explosion behind, red and orange glow, bold white text.",
            "Police cars filling the background with a 5-star wanted level in the corner and your shocked face in front.",
            "A supercar mid-drift with neon blue light trails and the text '{topic}' in a thick outline.",
            "Two characters facing each other, VS in the middle, city skyline at sunset.",
        ],
        "thumbnail_text": ["5 STARS", "GONE WRONG", "WATCH THIS", "INSANE", "NO WAY"],
        "description_hooks": [
            "In this GTA V video, I try {topic} and it gets out of control fast.",
            "GTA V {topic}: watch what happens when everything goes wrong.",
        ],
    },
    "Roblox": {
        "icon": "🧱",
        "topic_ideas": [
            "Obby", "Tycoon", "Horror Game", "Brookhaven Roleplay",
            "Blox Fruits", "Adopt Me", "Tower Defense",
        ],
        "title_templates": {
            "YouTube Shorts": [
                "Roblox {topic} but I'm the BEST 😎",
                "I beat this Roblox {topic} in 1 minute",
                "Roblox {topic} secret you didn't know",
            ],
            "Long Video": [
                "I Played Roblox {topic} for 24 Hours Straight",
                "Roblox {topic}: From Noob to Pro",
                "I Went Undercover in Roblox {topic}",
            ],
        },
        "hashtags": [
            "#roblox", "#robloxgames", "#robloxshorts", "#robloxedit",
            "#robloxobby", "#robloxtycoon", "#robloxfunny", "#robloxgameplay",
            "#robloxroleplay", "#bloxfruits", "#adoptme", "#robloxcommunity",
        ],
        "thumbnail_ideas": [
            "Your Roblox avatar with a huge shocked face next to a glowing {topic} item, bright colors, thick white outline text.",
            "Noob vs Pro split screen with a red VS in the center and a crown over the pro.",
            "A giant boss behind your avatar, the text 'I BEAT IT?!' in yellow, with a red circle highlighting the prize.",
            "Rainbow background with your avatar holding a mystery box and a big question mark.",
        ],
        "thumbnail_text": ["NOOB TO PRO", "I WON?!", "SECRET", "24 HOURS", "SO EASY"],
        "description_hooks": [
            "In this Roblox video, I play {topic} and try to win everything.",
            "Roblox {topic}: I show you tips and tricks to get ahead fast.",
        ],
    },
}


# ---------------------------------------------------------------
# General (non-game) data by format
# ---------------------------------------------------------------
GENERAL_HASHTAGS = {
    "YouTube Shorts": [
        "#shorts", "#youtubeshorts", "#gaming", "#gamer", "#viral", "#fyp",
    ],
    "Long Video": [
        "#gaming", "#gameplay", "#letsplay", "#gamer", "#youtubegamer", "#walkthrough",
    ],
}

DESCRIPTION_TEMPLATES = {
    "YouTube Shorts": (
        "{hook}\n\n"
        "👍 Like if you enjoyed it\n"
        "🔔 Subscribe for more {game} content\n\n"
        "{hashtags}"
    ),
    "Long Video": (
        "{hook}\n\n"
        "In this video:\n"
        "• The setup and goal\n"
        "• Tips and mistakes to avoid\n"
        "• The big finish\n\n"
        "👍 Like the video if you enjoyed it\n"
        "🔔 Subscribe for more {game} videos\n"
        "💬 Tell me in the comments what I should try next\n\n"
        "{hashtags}"
    ),
}

THUMBNAIL_TIPS = [
    "Use 3 words or fewer of big, bold text.",
    "Show a clear emotion on a face or character.",
    "Use high contrast: bright colors on a dark background.",
    "Add one clear focal point, not many small things.",
    "Keep text away from the bottom-right corner, where the timestamp sits.",
]