#     The intro is grouped into the following scenes
#     - Copyright screen
#     - GF Logo
#     Scene 1. Brief close up shot of grass
#     Scene 2. A panning wide shot followed by a close-up of Gengar/Nidorino
#     Scene 3. A fight between Gengar/Nidorino

#     After this it progresses to the title screen

from src.main import g_main


def set_up_copyright_screen():
    if g_main.state == 0:
        # begin_normal_palette_fade(PALETTES_ALL, 0, 16, 0, rgb_white_alpha())
        print("HEHE")
    elif g_main.state == 140:
        # begin_normal_palette_fade(PALETTES_ALL, 0, 0, 16, rgb_black())
        print("HAHA")
    # update_palette_fade()
    g_main.state += 1
    return True