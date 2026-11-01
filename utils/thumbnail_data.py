"""Visual building blocks for thumbnail suggestions."""

COMPOSITIONS = [
    ("Rule of thirds", "Put the main subject on the left third and the key object on the right third. Leave clean space for 2-3 words of text."),
    ("Split screen", "Divide the frame in two (before/after or noob/pro) with a bold divider or a VS badge."),
    ("Close-up face", "Fill about half the frame with your face or character showing one clear emotion; the object sits behind you."),
    ("Diagonal action", "Run the action along a diagonal from bottom-left to top-right to create energy and movement."),
    ("Centered hero", "One huge subject dead center with a glow behind it and short text above."),
]

LIGHTING = [
    ("Rim light", "Bright purple or blue edge light around the subject so it pops from the background."),
    ("Neon glow", "Neon glow behind the subject with a dark vignette in the corners."),
    ("High contrast", "Deep shadows with one bright, saturated highlight on the subject."),
    ("Dramatic backlight", "Strong light behind the subject, like a sunrise or explosion, giving a silhouette feel."),
    ("Warm vs cool", "Warm orange light on one side and cool blue on the other for depth."),
]

VISUALS = {
    "Minecraft": {
        "subjects": [
            "Your skin with a shocked face holding a glowing diamond sword",
            "A giant creeper face looming over your tiny character",
            "Your skin standing on top of a massive {topic} build",
            "Steve and a huge Ender Dragon staring each other down",
        ],
        "backgrounds": [
            "Dark cave with glowing lava streams",
            "Blocky mountain sunrise with square clouds",
            "The End dimension with floating purple islands",
            "Nether fortress with red fog",
        ],
        "palette": "Purple, lava orange and diamond cyan",
    },
    "GTA V": {
        "subjects": [
            "Your character mid-jump from a helicopter, arms wide",
            "A supercar drifting toward the camera with smoke trails",
            "Your character facing a wall of police cars, {topic} in the corner",
            "Two rival characters back to back with a VS in the middle",
        ],
        "backgrounds": [
            "Los Santos skyline at sunset",
            "Neon-lit city street at night with rain reflections",
            "Highway with an explosion in the distance",
            "Beach and pier with a golden sky",
        ],
        "palette": "Hot pink, sunset orange and electric blue",
    },
    "Roblox": {
        "subjects": [
            "Your avatar with a huge open mouth next to a glowing {topic} item",
            "A noob and a pro avatar side by side with a crown on the pro",
            "Your avatar holding a mystery box with a big question mark",
            "A giant boss towering behind your tiny avatar",
        ],
        "backgrounds": [
            "Bright rainbow gradient with floating blocks",
            "Colorful obby course stretching into the sky",
            "Spooky dark map with a red fog glow",
            "Sunny baseplate with sparkles",
        ],
        "palette": "Bright red, sunny yellow and sky blue",
    },
}
