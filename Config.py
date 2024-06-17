import os

# Window Settings
WINDOW_WIDTH, WINDOW_HEIGHT = 960, 540

# Asset Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITESHEET_PATH = os.path.join(BASE_DIR, 'Assets', 'SpriteSheets', 'sheets')
BACKGROUND_IMAGE = os.path.join(SPRITESHEET_PATH, 'Background', 'Background.png')
BEE_IMAGE = os.path.join(SPRITESHEET_PATH, 'Mob', 'Small Bee', 'Fly', 'Fly-Sheet.png')
IDLE_SPRITE = os.path.join(SPRITESHEET_PATH, 'Character', 'Idle', 'Idle-Sheet.png')
ATTACK_SPRITE = os.path.join(SPRITESHEET_PATH, 'Character', 'Attack-01', 'Attack-01-Sheet.png')
RUN_SPRITE = os.path.join(SPRITESHEET_PATH, 'Character', 'Run', 'Run-Sheet.png')

SPEED_BEE = 2

ANIMSPEED_BEE = 0.2

ANIMSPEED_HERO_DEFAULT = 0.25
ANIMSPEED_HERO_IDLE = 0.1
SPEED_HERO = 4
