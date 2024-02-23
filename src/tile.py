import numpy as np
import pygame

GAME_BOY_WIDTH = 20
GAME_BOY_HEIGHT = 18
GBA_WIDTH = 30
GBA_HEIGHT = 20
GAME_BOY_VRAM_SIZE = 32


def read_bin(file_path):
    tile_map = []
    # Open the binary file
    with open(file_path, "rb") as file:
        # Read 16 bytes of data for the tile
        tile_data = file.read()
        print(len(tile_data))
        # Iterate the tile data
        for i in range(0, len(tile_data), 2):
            # get first byte pair
            tile_id = tile_data[i] | ((tile_data[i + 1] & 0x03) << 8)
            # get first 4 bits from second byte pair
            palette = (tile_data[i + 1] & 0xF0) >> 4
            # get bool from last thrid bit
            x_flip = bool(tile_data[i + 1] & 0x04)
            # get bool from last fourth bit
            y_flip = bool(tile_data[i + 1] & 0x08)
            # append tile
            tile_map.append((tile_id, palette, x_flip, y_flip))
    return tile_map


def n_fits_size(n, width, height):
    return n % width == 0 and n // width <= height


def guess_width(tiles):
    n = len(tiles)

    if n_fits_size(n, GAME_BOY_WIDTH, GAME_BOY_HEIGHT):
        return GAME_BOY_WIDTH
    if n_fits_size(n, GAME_BOY_WIDTH, GAME_BOY_HEIGHT):
        return n // GAME_BOY_HEIGHT
    if n_fits_size(n, GBA_WIDTH, GBA_HEIGHT):
        return GBA_WIDTH
    if n_fits_size(n, GAME_BOY_VRAM_SIZE, GAME_BOY_VRAM_SIZE):
        return GAME_BOY_VRAM_SIZE
    if n_fits_size(n, GAME_BOY_HEIGHT - 6, GAME_BOY_WIDTH):
        return n // (GAME_BOY_HEIGHT - 6)
    if n_fits_size(n, 64, 64):
        return 64
    r = int(n**0.5)
    if r > 0:
        return r
    return 16


class Tileset:
    def __init__(self, file, size=(8, 8)):
        self.size = size
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self._load()

    def _load(self):
        self.tiles = []
        x0 = y0 = 0
        w, h = self.rect.size
        dx, dy = self.size

        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)


class Tilemap:
    def __init__(self, file, tileset, size=None, rect=None):
        self.tile_map = read_bin(file)
        self.tileset = tileset
        self.map = None

        if size:
            self.size = size
        else:
            width = guess_width(self.tile_map)
            height = len(self.tile_map) // width
            self.size = (height, width)

        h, w = self.size
        self.image = pygame.Surface((8 * w, 8 * h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

        self._set_map()

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                tile = pygame.transform.flip(tile, self.x_flip[i, j], self.y_flip[i, j])
                self.image.blit(tile, (j * 8, i * 8))

    def _set_map(self):
        h, w = self.size
        # 4 channels - tile_id, palette, x-flip, y-flip
        tile_map = np.array(self.tile_map).reshape(h, w, 4)
        self.map = tile_map[:, :, 0]
        self.x_flip = tile_map[:, :, 2]
        self.y_flip = tile_map[:, :, 3]
