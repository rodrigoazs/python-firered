# Palette-loading utility function, by Kevin.
# Public domain.  Have fun.

import re


NORMAL_FADE = 0
FAST_FADE = 1
HARDWARE_FADE = 2


def load_palette(src):
    """Loads a palette file and returns a list suitable for Surface.setpalette()

    Loads a palette file, which is anything that looks like this:

    0 0 0
    0 0  4
    0 64 8
    ...

    GIMP and Fractint palette files both match this description.
    Lines that don't match are silently ignored.
    Only recognizes decimal values, not 0xFF or #AA66FF.
    """

    with open(src) as f:
        pal = []
        rgb_re = re.compile("^(?:\s+)?(\d+)\s+(\d+)\s+(\d+)")
        for l in f.readlines():
            m = rgb_re.search(l)
            if m:
                pal.append(tuple(map(int, m.groups())))
    return pal


class PaletteFadeControl:
    def __init__(self):
        self.multipurpose1 = 0
        self.delayCounter = 0
        self.y = 0
        self.targetY = 0
        self.blendColor = 0
        self.active = False
        self.multipurpose2 = 0
        self.yDec = 0
        self.bufferTransferDisabled = 0
        self.mode = 0
        self.shouldResetBlendRegisters = 0
        self.hardwareFadeFinishing = 0
        self.softwareFadeFinishingCounter = 0
        self.softwareFadeFinishing = 0
        self.objPaletteToggle = 0
        self.deltaY = 0


def update_blend_registers(gPaletteFade):
    # SetGpuReg(REG_OFFSET_BLDCNT, gPaletteFade_blendCnt)
    # SetGpuReg(REG_OFFSET_BLDY, gPaletteFade.y)
    if gPaletteFade.hardwareFadeFinishing:
        gPaletteFade.hardwareFadeFinishing = False
        gPaletteFade.mode = 0
        gPaletteFade_blendCnt = 0
        gPaletteFade.y = 0
        gPaletteFade.active = False


def update_palette_fade():
    dummy = 0
    
    if s_pltt_buffer_transfer_pending:
        return PALETTE_FADE_STATUS_LOADING
    
    if g_palette_fade.mode == NORMAL_FADE:
        result = update_normal_palette_fade()
    elif g_palette_fade.mode == FAST_FADE:
        result = update_fast_palette_fade()
    else:
        result = update_hardware_palette_fade()
    
    s_pltt_buffer_transfer_pending = g_palette_fade.multipurpose1 | dummy
    return result


def begin_normal_palette_fade(gPaletteFade, selectedPalettes, delay, startY, targetY, blendColor):
    color = blendColor

    if gPaletteFade.active:
        return False
    else:
        gPaletteFade.deltaY = 2
        if delay < 0:
            gPaletteFade.deltaY += abs(delay)
            delay = 0
        gPaletteFade_selectedPalettes = selectedPalettes
        gPaletteFade.delayCounter = delay
        gPaletteFade_delay = delay
        gPaletteFade.y = startY
        gPaletteFade.targetY = targetY
        gPaletteFade.blendColor = color
        gPaletteFade.active = True
        gPaletteFade.mode = NORMAL_FADE
        gPaletteFade.yDec = False if startY < targetY else True
        UpdatePaletteFade()
        temp = gPaletteFade.bufferTransferDisabled
        gPaletteFade.bufferTransferDisabled = False
        #CpuCopy32(gPlttBufferFaded, PLTT, PLTT_SIZE)
        sPlttBufferTransferPending = False
        if gPaletteFade.mode == HARDWARE_FADE and gPaletteFade.active:
            update_blend_registers(gPaletteFade)
        gPaletteFade.bufferTransferDisabled = temp
        return True


