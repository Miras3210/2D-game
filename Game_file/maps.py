import pygame

MAPS = {
    "Village": {
        "map": "Assets/Village.tmx",

        "doors": [
            {
                "rect": pygame.Rect(500, 300, 64, 64),
                "target": "Dungeon_Ground_Floor",
                "spawn": (100, 100)
            }
        ]
    },

    "Dungeon_Ground_Floor": {
        "map": "Assets/revised_ground_floor_map.tmx",

        "doors": [
            {
                "rect": pygame.Rect(50, 50, 64, 64),
                "target": "Dungeon_Floor_1",
                "spawn": (120, 120)
            },

            {
                "rect": pygame.Rect(300, 500, 64, 64),
                "target": "Village",
                "spawn": (600, 400)
            }
        ]
    },

    "Dungeon_Floor_1": {
        "map": "Assets/dungeon_floor_1.tmx",
        "type": "traps",

        "doors": [
            {
                "rect": pygame.Rect(700, 100, 64, 64),
                "target": "Dungeon_Floor_2",
                "spawn": (80, 80)
            }
        ]
    },

    "Dungeon_Floor_2": {
        "map": "Assets/dungeon_floor_2.tmx",
        "type": "traps",

        "doors": [
            {
                "rect": pygame.Rect(700, 100, 64, 64),
                "target": "Dungeon_Floor_3",
                "spawn": (80, 80)
            }
        ]
    },

    "Dungeon_Floor_3": {
        "map": "Assets/dungeon_floor_3.tmx",
        "type": "monsters",

        "doors": [
            {
                "rect": pygame.Rect(700, 100, 64, 64),
                "target": "Dungeon_Floor_4",
                "spawn": (80, 80)
            }
        ]
    },

    "Dungeon_Floor_4": {
        "map": "Assets/dungeon_floor_4.tmx",
        "type": "boss",

        "doors": [
            {
                "rect": pygame.Rect(700, 100, 64, 64),
                "target": "Dungeon_Floor_5",
                "spawn": (80, 80)
            }
        ]
    },

    "Dungeon_Floor_5": {
        "map": "Assets/dungeon_floor_5.tmx",
        "type": "crop_of_vitality",

        "doors": [
            {
                "rect": pygame.Rect(400, 400, 64, 64),
                "target": "Village",
                "spawn": (200, 200)
            }
        ]
    }
}