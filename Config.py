import os

# Window Settings
WINDOW_WIDTH, WINDOW_HEIGHT = 960, 540

# Asset Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITESHEET_PATH = os.path.join(BASE_DIR, 'Assets', 'SpriteSheets', 'sheets')
BACKGROUND_IMAGE = os.path.join(SPRITESHEET_PATH, 'Background', 'Background.png')
BEE_IMAGE = os.path.join(SPRITESHEET_PATH, 'Mob', 'Small Bee', 'Fly', 'Fly-Sheet.png')

SPEED_BEE = 2

ANIMSPEED_BEE = 0.2
