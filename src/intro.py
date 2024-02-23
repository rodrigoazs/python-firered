#     The intro is grouped into the following scenes
#     - Copyright screen
#     - GF Logo
#     Scene 1. Brief close up shot of grass
#     Scene 2. A panning wide shot followed by a close-up of Gengar/Nidorino
#     Scene 3. A fight between Gengar/Nidorino

#     After this it progresses to the title screen

GFXTAG_STAR = 0
GFXTAG_SPARKLES_SMALL = 1
GFXTAG_SPARKLES_BIG = 2
GFXTAG_GF_LOGO = 3
GFXTAG_PRESENTS = 4
GFXTAG_SCENE3_NIDORINO = 5
GFXTAG_SCENE2_GENGAR = 6
GFXTAG_SCENE2_NIDORINO = 7
GFXTAG_SCENE3_GRASS = 8
GFXTAG_SCENE3_GENGAR = 9
GFXTAG_SCENE3_SWIPE = 10
GFXTAG_SCENE3_RECOIL_DUST = 11

PALTAG_STAR = 0
PALTAG_SPARKLES = 1
PALTAG_UNUSED_2 = 2
PALTAG_GF = 3
PALTAG_UNUSED_4 = 4
PALTAG_UNUSED_5 = 5
PALTAG_GENGAR = 6
PALTAG_NIDORINO = 7
PALTAG_SCENE3_GRASS = 8
PALTAG_UNUSED_9 = 9
PALTAG_SCENE3_SWIPE = 10
PALTAG_SCENE3_RECOIL_DUST = 11

BG_GF_TEXT_LOGO = 2
BG_GF_BACKGROUND = 3

BG_SCENE1_GRASS = 0
BG_SCENE1_BACKGROUND = 1
BG_SCENE1_UNUSED1 = 2
BG_SCENE1_UNUSED2 = 3

PALSLOT_SCENE1_GRASS = 1
PALSLOT_SCENE1_BG = 2

# Background IDs for Scene 2
BG_SCENE2_PLANTS = 0
BG_SCENE2_NIDORINO = 1
BG_SCENE2_GENGAR = 2
BG_SCENE2_BACKGROUND = 3  # Bg for wide shot on upper half, close up on lower half

# Background IDs for Scene 3
BG_SCENE3_GENGAR = 0
BG_SCENE3_BACKGROUND = 1
BG_SCENE3_UNUSED1 = 2
BG_SCENE3_UNUSED2 = 3

ANIM_NIDORINO_NORMAL = 0
ANIM_NIDORINO_CRY = 1
ANIM_NIDORINO_CROUCH = 2
ANIM_NIDORINO_HOP = 3
ANIM_NIDORINO_ATTACK = 4

ANIM_SPARKLE_LOOP = 0
ANIM_SPARKLE_ONCE = 1

ANIM_SWIPE_TOP = 0
ANIM_SWIPE_BOTTOM = 1

AFFINEANIM_NORMAL = 0
AFFINEANIM_ZOOM = 1

# Window ids for sWindowTemplates (only one)
WIN_GF_TEXT_LOGO = 0
WIN_COUNT = 1

NUM_GENGAR_BACK_SPRITES = 4

COLOSSEUM_GAME_CODE = 0x65366347  # "Gc6e" in ASCII


class IntroSequenceData:
    def __init__(self):
        self.callback = None
        self.state = 0
        self.task_id = 0
        self.gengar_attack_landed = False
        self.data = [0] * 5  # [0] and [1] are set but never read, the rest are unused
        self.timer = 0
        self.game_freak_logo_art_sprite = None
        self.scene3_nidorino_sprite = None
        self.scene2_gengar_sprite = None
        self.scene2_nidorino_sprite = None
        self.scene3_grass_sprite = None
        self.scene3_gengar_sprites = [None] * NUM_GENGAR_BACK_SPRITES
        self.unused0 = [0] * 4
        self.game_freak_logo_gfx = [0] * 0x400
        self.game_freak_text_gfx = [0] * 0x400
        self.unused1 = [0] * 0x2080
