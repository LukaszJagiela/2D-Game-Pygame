import pygame, os, random
pygame.init()
# Kolory/Rozmiary/Ikony
DARKRED = pygame.color.THECOLORS['darkred']
LIGHTRED = pygame.color.THECOLORS['palevioletred']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
BLACK = pygame.color.THECOLORS['black']
WHITE = pygame.color.THECOLORS['white']
RED = pygame.color.THECOLORS['red']
GRAY = pygame.color.THECOLORS['gray']
LIGHTGREEN = pygame.color.THECOLORS['lightgreen']
WIDTH = 1470
HEIGHT = 700
ICON = pygame.image.load('png\logo.png')
FPS = 60


# grafika postać
STAND = pygame.image.load('png\stand.png')
WALK_R1 = pygame.image.load('png\walk_R1.png')
WALK_R2 = pygame.image.load('png\walk_R2.png')
WALK_L1 = pygame.image.load('png\walk_L1.png')
WALK_L2 = pygame.image.load('png\walk_L2.png')
UP_1 = pygame.image.load('png\gora1.png')
UP_2 = pygame.image.load('png\gora2.png')
FIGHT_L3 = pygame.image.load('png\walkal3.png')
FIGHT_R3 = pygame.image.load('png\walkar3.png')
UP = [UP_1, UP_2]
WALK_R = [WALK_R1, WALK_R2]
WALK_L = [WALK_L1, WALK_L2]
PRINCESS = pygame.image.load('png\princess.png')



#grafika otoczenie
LADDER = pygame.image.load('png\ladder.png')
GRASS = pygame.image.load('png\grass.png')
GRASS1 = pygame.image.load('png\grass1.png')
DOOR = pygame.image.load('png\castledoors.png')
CHEST_CLOSED = pygame.image.load('png\chestclosed.png')
CHEST_OPEN = pygame.image.load('png\chestopen.png')
BACKGROUND = pygame.image.load('png\ckground.png')

# grafika wrogów
DRAGON_R1 = pygame.image.load('png\dragon_r1.png')
DRAGON_R2 = pygame.image.load('png\dragon_r2.png')
DRAGON_L1 = pygame.image.load('png\dragon_l1.png')
DRAGON_L2 = pygame.image.load('png\dragon_l2.png')
DRAGON_L = [DRAGON_L1, DRAGON_L2]
DRAGON_R = [DRAGON_R1, DRAGON_R2]
DRAGON_DEAD_L = pygame.image.load('png\dragon_dead_L.png')
DRAGON_DEAD_R = pygame.image.load('png\dragon_dead_R.png')
SKELETON_L1 = pygame.image.load('png\skeleton_L1.png')
SKELETON_L2 = pygame.image.load('png\skeleton_L2.png')
SKELETON_R1 = pygame.image.load('png\skeleton_R1.png')
SKELETON_R2 =pygame.image.load('png\skeleton_R2.png')
SKELETON_L = [SKELETON_L1, SKELETON_L2]
SKELETON_R = [SKELETON_R1, SKELETON_R2]
RDRAGON_R1 = pygame.image.load('png\Rdragon_R1.png')
RDRAGON_R2 = pygame.image.load('png\Rdragon_R2.png')
RDRAGON_L1 = pygame.image.load('png\Rdragon_L1.png')
RDRAGON_L2 = pygame.image.load('png\Rdragon_L2.png')
RDRAGON_L = [RDRAGON_L1, RDRAGON_L2]
RDRAGON_R = [RDRAGON_R1, RDRAGON_R2]
KILL_ENEMY = pygame.image.load('png\kill_enemy.png')

# grafika itemów
SHURIKEN = pygame.image.load('png\weapon.png')
SHURIKEN_R1 = pygame.image.load('png\weapon_r1.png')
SHURIKEN_R2 = pygame.image.load('png\weapon_r2.png')
SHURIKEN_R = [SHURIKEN_R1, SHURIKEN_R2]
SHURIKEN_L1 = pygame.image.load('png\weapon_l1.png')
SHURIKEN_L2 = pygame.image.load('png\weapon_l2.png')
SHURIKEN_L = [SHURIKEN_R1, SHURIKEN_R2]
KEY = pygame.image.load('png\key.png')
HEARTH = pygame.image.load('png\hearth.png')
SPIKE = pygame.image.load('png\spike.png')
DIAMOND = pygame.image.load('png\diamond.png')
DIAMOND_RED = pygame.image.load('png\diamond_red.png')
DIAMOND_ENEMY = pygame.image.load('png\diamond_enemy.png')
hitbox = pygame.image.load('png\kwadrat.png')
hitbox_sprite = pygame.sprite.Sprite()
hitbox_sprite.image = hitbox
hitbox_sprite.rect = hitbox_sprite.image.get_rect()
FIREBALL = pygame.image.load('png\cireball_1.png')

#dźwięki
music = pygame.mixer.music.load('sound\music.mp3')
throw_shuriken = pygame.mixer.Sound('sound\shuriken.wav')
jump = pygame.mixer.Sound('sound\jump.ogg')
hit_enemy = pygame.mixer.Sound('sound\hit_enemy.wav')
item_pick = pygame.mixer.Sound('sound\item_pick.wav')
door_lv_open = pygame.mixer.Sound('sound\door_lv_open.wav')
spikes = pygame.mixer.Sound('sound\spikes.wav')
take_diamond = pygame.mixer.Sound('sound\diamond.wav')
take_key = pygame.mixer.Sound('sound\key.ogg')
game_over = pygame.mixer.Sound('sound\game_over.ogg')
victory = pygame.mixer.Sound('sound\wictory.wav')

