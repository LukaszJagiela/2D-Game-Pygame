import pygame, os
import game_module as gm


os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()
pygame.mixer.music.play(-1)

## ustawienia ekranu i gry
screen = pygame.display.set_mode((gm.WIDTH, gm.HEIGHT))
pygame.display.set_caption('NightKnight')
pygame.display.set_icon(gm.ICON)
clock = pygame.time.Clock()
vec_doors = []
vec_chests = []
vec_platforms = []

def text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, gm.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#klasa  przeciwnika
class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_image, image_list_right,
                 image_list_left, movement_x=0, movement_y=0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.image_list_right = image_list_right
        self.image_list_left = image_list_left
        self.direction_of_movement = 'right'
        self.lifes = 2
        self._count = 0


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _move(self, image_list):
        if self._count < 2:
            self.image = image_list[0]
        elif self._count < 4:
            self.image = image_list[1]
        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1



#Klasa przeciwnika
class HorizontalEnemy(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 3


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY

        if self.movement_x == 252:
            self.movement_x = -252

# zmiana kierunku lotu po przekroczeniu movement_x
        if self.lifes > 0:
            if self.movement_x >= 0:
                if self.rect.x < 1470:
                    self.movement_x += 1
                    self.rect.x += 5
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'right'
            elif self.movement_x < 0:
                if self.rect.x >= 0:
                    self.movement_x += 1
                    self.rect.x -= 5
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'left'

class VerticalEnemy(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 3


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY

        if self.movement_y == 100:
            self.movement_y = -100

        if self.lifes > 0:
            if self.movement_y >= 0:
                if self.rect.y < 1470:
                    self.movement_y += 1
                    self.rect.y += 5
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'right'
            elif self.movement_y < 0:
                if self.rect.y >= 0:
                    self.movement_y += 1
                    self.rect.y -= 5
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'left'
class VerticalEnemy1(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 3


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY

        if self.movement_y == 50:
            self.movement_y = -50

        if self.lifes > 0:
            if self.movement_y >= 0:
                if self.rect.y < 1470:
                    self.movement_y += 1
                    self.rect.y += 5
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'right'
            elif self.movement_y < 0:
                if self.rect.y >= 0:
                    self.movement_y += 1
                    self.rect.y -= 5
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'left'
class VerticalEnemy2(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 3


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY

        if self.movement_y == 40:
            self.movement_y = -40

        if self.lifes > 0:
            if self.movement_y >= 0:
                if self.rect.y < 1470:
                    self.movement_y += 1
                    self.rect.y += 5
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'right'
            elif self.movement_y < 0:
                if self.rect.y >= 0:
                    self.movement_y += 1
                    self.rect.y -= 5
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'left'
class Skeleton(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 3


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY



        if self.movement_x == 60:
            self.movement_x = -60

        if self.lifes > 0:
            if self.movement_x >= 0:
                if self.rect.x < 800:
                    self.movement_x += 1
                    self.rect.x += 5
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'right'
            elif self.movement_x < 0:
                if self.rect.x >= 0:
                    self.movement_x += 1
                    self.rect.x -= 5
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'left'
class Boss(Enemy):
    def __init__(self, start_image, image_list_right, image_list_left, height, width,
                 movement_x = 0, movement_y =0):
        super().__init__(start_image,image_list_right,image_list_left, movement_x, movement_y)
        self.rect.y = height
        self.rect.x = width
        self.lifes = 9


    def update(self):
        if self.lifes <= 0:
            self.kill()
            self.image = gm.KILL_ENEMY

        if self.movement_x == 90:
            self.movement_x = -90

        if self.lifes > 0:
            if self.movement_x >= 0:
                    self.movement_x += 1
                    self.rect.x -= 10
                    self.rect.y += 6
                    self._move(self.image_list_left)
                    self.direction_of_movement = 'right'
            elif self.movement_x < 0:
                    self.movement_x += 1
                    self.rect.y -= 6
                    self.rect.x += 10
                    self._move(self.image_list_right)
                    self.direction_of_movement = 'left'



# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = {}
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.lifes = 3
        self.princess = 0
        self.level = None
        self.direction_of_movement = 'right'
        self.score = 0
        self.hitbox = gm.hitbox_sprite
        self.hitbox_rect = self.hitbox.rect


    def turn_right(self):
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 8

    def turn_left(self):
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -8

    def jump(self):
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2
        if colliding_platforms:
            self.movement_y = -12

    def up(self):
            self.movement_y = -6

    def down(self):
        self.movement_y = 6

#strzelanie shurikenem
    def shoot(self):
        if self.items.get('shuriken', False) and len(self.level.set_of_bullets) < 1:
            if self.direction_of_movement == 'right':
                bullet = Bullet(
                    gm.SHURIKEN, self.direction_of_movement,
                    self.rect.centerx, self.rect.centery + 15)
                self.level.set_of_bullets.add(bullet)
            else:
                bullet = Bullet(
                    gm.SHURIKEN, self.direction_of_movement,
                    self.rect.centerx, self.rect.centery + 15)
                self.level.set_of_bullets.add(bullet)

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def update(self):
        self.hitbox_rect.left = self.rect.left + 10
        self.hitbox_rect.right = self.rect.right - 15
        self.hitbox_rect.top = self.rect.top + 18
        #print(self.rect.x, self.rect.y)
        self._gravitation()

        # -----------------ruch w poziomie ----------------
        self.rect.x += self.movement_x

        # sparwdzanie kolizji

        #kolizja z przeciwnikiem
        colliding_enemies = pygame.sprite.spritecollide(
            self.hitbox, self.level.set_of_enemies, False)
        for enemy in colliding_enemies:
            if self.direction_of_movement == 'right':
                if enemy.lifes:
                    if enemy.movement_x > 0:
                        player.rect.bottom = gm.HEIGHT - 70
                        player.rect.x = 100
                        self.lifes -= 1
                        self.image = gm.WALK_R1
                    else:
                        player.rect.bottom = gm.HEIGHT - 70
                        player.rect.x = 100
                        self.lifes = -1
                        self.image = gm.WALK_R1
            else:
                if enemy.lifes:
                    if enemy.movement_x > 0:
                        player.rect.bottom = gm.HEIGHT - 70
                        player.rect.x = 100
                        self.lifes -= 1
                        self.image = gm.WALK_L1
                    else:
                        player.rect.bottom = gm.HEIGHT - 70
                        player.rect.x = 100
                        self.lifes = -1
                        self.image = gm.WALK_L1

        if self.rect.top > gm.HEIGHT:
            self.lifes -= 1
            player.rect.bottom = gm.HEIGHT - 70
            player.rect.x = 100


        # kolizja z drzwiami
        colliding_doors = pygame.sprite.spritecollide(
            self.hitbox, self.level.set_of_doors, False)
        for door in colliding_doors:
            if door.name == "down":
                    if self.movement_x < 0:
                        self.rect.left = door.rect.right
                        self.rect.x = vec_doors[1][0] - 70
                        self.rect.y = vec_doors[1][1]
            elif door.name == "up":
                self.rect.x = vec_doors[0][0] + 40
                self.rect.y = vec_doors[0][1]

        # kolizja z platformą
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        # animacje
        if self.movement_x > 0:
            self._move(gm.WALK_R)
        if self.movement_x < 0:
            self._move(gm.WALK_L)

        #kolizja z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self.hitbox, self.level.set_of_items, False)
        for item in colliding_items:
            if item.name == 'chest':
                item.name = 'chest_open'
                item.image = gm.CHEST_OPEN
                item.rect.y = gm.HEIGHT - 600
                shuriken = Item(gm.SHURIKEN, 'shuriken', gm.WIDTH - 220, gm.HEIGHT - 600)
                self.level.set_of_items.add(shuriken)
            if item.name == 'shuriken':
                gm.item_pick.play(+2)
                self.items[item.name] = 1
                item.kill()
            if item.name == 'key':
                gm.take_key.play()
                item.kill()
                if isinstance(self.level, Level_1):
                    self.level.set_of_items.add(Item(gm.DOOR, 'door_lv', gm.WIDTH - 400, gm.HEIGHT - 100))
                elif isinstance(self.level, Level_2):
                    self.level.set_of_items.add(Item(gm.DOOR, 'door_lv2', 140, gm.HEIGHT - 600))
                elif isinstance(self.level, Level_3):
                    self.level.set_of_items.add(Item(gm.DOOR, 'door_lv3', 50, 100))
                elif isinstance(self.level, Level_4):
                    self.level.set_of_items.add(Item(gm.DOOR, 'door_lv4', 200, 40))
                gm.door_lv_open.play()
            if item.name == 'hearth':
                gm.item_pick.play()
                item.kill()
                self.lifes += 1
            if item.name == 'diamond1' or item.name == 'diamond2':
                gm.take_diamond.play()
                item.kill()
                self.score += 50
            if item.name == 'diamond_red1' or item.name == 'diamond_red2':
                gm.take_diamond.play()
                item.kill()
                self.score += 100
            if item.name == 'spike' or item.name == 'spike1':
                gm.spikes.play()
                if self.direction_of_movement == 'right':
                    self.rect.right = self.rect.left
                    self.lifes -= 1
                    player.rect.bottom = gm.HEIGHT - 70
                    player.rect.x = 100
                if self.direction_of_movement == 'left':
                    self.rect.left = self.rect.right
                    player.rect.bottom = gm.HEIGHT - 70
                    player.rect.x = 100
                    self.lifes -= 1
            if item.name == 'door_lv':
                del self.level
                self.level = Level_2(self)
                self.level.draw(screen)
                player.rect.bottom = gm.HEIGHT - 70
                player.rect.x = 100
                self.image = gm.STAND
                self.rect.x += 150
                self.stop()
            if item.name == 'door_lv2':
                del self.level
                self.level = Level_3(self)
                self.level.draw(screen)
                player.rect.bottom = gm.HEIGHT - 70
                player.rect.x = 100
                self.image = gm.STAND
                self.rect.x += 150
                self.stop()
            if item.name == 'door_lv3':
                del self.level
                self.level = Level_4(self)
                self.level.draw(screen)
                player.rect.bottom = gm.HEIGHT - 70
                player.rect.x = 70
                self.image = gm.STAND
                self.rect.x += 150
                self.stop()
            if item.name == 'door_lv4':
                del self.level
                self.level = Finish(self)
                self.level.draw(screen)
                player.rect.bottom = gm.HEIGHT - 70
                player.rect.x = 100
                self.image = gm.STAND
                self.rect.x += 150
                self.stop()
            if item.name == 'princess':
                player.princess += 1



        # -----------------ruch w pionie ----------------
        self.rect.y += self.movement_y

        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.direction_of_movement == 'left' and self.movement_x == 0:
                    self.image = gm.WALK_L1
                if self.direction_of_movement == 'right' and self.movement_x == 0:
                    self.image = gm.WALK_R1
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0


        self.rect.y += 3
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 3


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(gm.hitbox, gm.hitbox_sprite.rect)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_c:
                gm.jump.play()
                self.jump()
            if event.key == pygame.K_a:
                self.turn_left()
            if event.key == pygame.K_s:
                self.down()
            if event.key == pygame.K_x:
                gm.throw_shuriken.play()
                self.shoot()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
                self.image = gm.WALK_R1
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
                self.image = gm.WALK_L1
            if event.key == pygame.K_w:
                self.stop()
            if event.key == pygame.K_s:
                self.stop()





    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1

    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 2
        else:
            self.movement_y += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                colliding_ladders = pygame.sprite.spritecollide(
                    self.hitbox, self.level.set_of_ladders, False)
                if colliding_ladders:
                    self.up()
                    self._move(gm.UP)
            if event.key == pygame.K_s:
                colliding_ladders = pygame.sprite.spritecollide(
                    self.hitbox, self.level.set_of_ladders, False)
                if colliding_ladders:
                        self.down()
                        self._move(gm.UP)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.stop()
            if event.key == pygame.K_s:
                self.stop()

# ogólna klasa przedmiotu
class Item(pygame.sprite.Sprite):
    def __init__(self, image, name, rect_center_x, rect_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name
        self.rect.center = [rect_center_x, rect_center_y]

# klasa reprezentująca pocisk
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, direction, rect_center_x, rect_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [rect_center_x, rect_center_y]
        self.direction_of_movement = direction
        self._count = 0

    def update(self):
        if self.direction_of_movement == 'right':
            self.rect.x += 15
            self._move(gm.SHURIKEN_R)
        else:
            self.rect.x -= 15
            self._move(gm.SHURIKEN_L)

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1

#klasa platformy
class Platform(pygame.sprite.Sprite):
    def __init__(self, file_image, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.image.blit(file_image, (0,-11))
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#klasa drabiny
class Ladder(pygame.sprite.Sprite):
    def __init__(self, file_image, rect_x, rect_y):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)


#klasa drzwi
class Door(pygame.sprite.Sprite):
    def __init__(self, file_image, rect_x, rect_y, name):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.name = name

    def draw(self, surface):
        surface.blit(self.image, self.rect)



#ogólna klasa planszy
class Level:
    def __init__(self, player):
        self.set_of_items = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()
        self.set_of_platforms = set()
        self.set_of_ladders = set()
        self.set_of_doors = set()
        self.set_of_chests = set()
        self.set_of_enemies = set()
        self.player = player


    def update(self):
        self.set_of_bullets.update()
        self.set_of_items.update()
        self._delete_bullet()
        for p in self.set_of_platforms:
            p.update()
        for l in self.set_of_ladders:
            l.update()
        for d in self.set_of_doors:
            d.update()
        for c in self.set_of_chests:
            c.update()
        for enemy in self.set_of_enemies:
            enemy.update()

        for enemy in self.set_of_enemies:
            colliding_bullets = pygame.sprite.spritecollide(enemy, self.set_of_bullets, False)
            for bullet in colliding_bullets:
                if enemy.lifes > 0:
                    gm.hit_enemy.play()
                    enemy.lifes -= 3
                    bullet.kill()
                if enemy.lifes <= 0:
                    diamond1 = Item(gm.DIAMOND_ENEMY, 'diamond1', enemy.rect.x, enemy.rect.y + 40)
                    self.set_of_items.add(diamond1)
                    enemy.rect.x = - 100






    def draw(self, surface):
        self.set_of_items.draw(surface)
        self.set_of_bullets.draw(surface)
        for enemy in self.set_of_enemies:
            enemy.draw(surface)
        for p in self.set_of_platforms:
            p.draw(surface)
        for l in self.set_of_ladders:
            l.draw(surface)
        for d in self.set_of_doors:
            d.draw(surface)
        for c in self.set_of_chests:
            c.draw(surface)




    def _delete_bullet(self):
        for b in self.set_of_bullets:
            # sprwadzamy kolizje z platformami i usuwamy pocisk
            if pygame.sprite.spritecollideany(b, self.set_of_platforms):
                b.kill()
            # sprwadzamy czy pocisk wyleciał poza planszę i usuwamy pocisk
            if b.rect.left > gm.WIDTH or b.rect.right < 0:
                b.kill()

# klasa planszy nr 1
class Level_1(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self.create_platforms()
        self.create_ladders()
        self.create_doors()
        self.create_items()
        self.create_enemies()

    def create_enemies(self):
        enemy1 = HorizontalEnemy(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 395, 0)
        self.set_of_enemies.add(enemy1)
        enemy2 = Skeleton(gm.SKELETON_R1, gm.SKELETON_R, gm.SKELETON_L, 85, 200)
        self.set_of_enemies.add(enemy2)

    def create_items(self):
        chest = Item(gm.CHEST_CLOSED, 'chest', gm.WIDTH - 200, gm.HEIGHT-567)
        self.set_of_items.add(chest)
        key = Item(gm.KEY, 'key', gm.WIDTH - 310, gm.HEIGHT - 590)
        self.set_of_items.add(key)
        spike = Item(gm.SPIKE, 'spike', 300, gm.HEIGHT - 48)
        self.set_of_items.add(spike)
        spike1 = Item(gm.SPIKE, 'spike1', 450, gm.HEIGHT - 558)
        self.set_of_items.add(spike1)
        diamond1 = Item(gm.DIAMOND,'diamond1', 500, gm.HEIGHT - 240)
        self.set_of_items.add(diamond1)
        diamond2 = Item(gm.DIAMOND, 'diamond2', 1420, gm.HEIGHT - 410)
        self.set_of_items.add(diamond2)
        diamond_red1 = Item(gm.DIAMOND_RED, 'diamond_red1', 900, gm.HEIGHT - 570)
        self.set_of_items.add(diamond_red1)
        diamond_red2 = Item(gm.DIAMOND_RED, 'diamond_red2', 1200, gm.HEIGHT - 60)
        self.set_of_items.add(diamond_red2)




    def create_platforms(self):
        ws_platform_static = [[400, 20, 0, gm.HEIGHT - 40], [350, 20, 480, gm.HEIGHT - 40], [gm.WIDTH / 2, 20, gm.WIDTH / 2 + 250, gm.HEIGHT - 40], [gm.WIDTH, 20, 0, gm.HEIGHT - 720],
                              [200, 20, 0, gm.HEIGHT - 210], [280, 20, 280, gm.HEIGHT - 210], [200, 20, 660, gm.HEIGHT - 210], [445, 20, 915, gm.HEIGHT - 210], [60, 20, 1430, gm.HEIGHT - 210],
                                [250, 20, 0, gm.HEIGHT - 380], [180, 20, 330, gm.HEIGHT - 380], [50, 20, 580, gm.HEIGHT - 380], [265, 20, 710, gm.HEIGHT - 380], [220, 20, 1065, gm.HEIGHT - 380], [120, 20, 1355, gm.HEIGHT - 380],
                               [115, 20, 0, gm.HEIGHT - 550], [500, 20, 205, gm.HEIGHT - 550], [250, 20, 775, gm.HEIGHT - 550], [115, 20, 1105, gm.HEIGHT - 550], [250, 20, gm.WIDTH / 2 + 485, gm.HEIGHT - 550]]


        for ws in ws_platform_static:
            platform_object = Platform(gm.GRASS, *ws)
            vec_platforms.append(ws)
            self.set_of_platforms.add(platform_object)

        vertical_platform = [[40, 700, -40, gm.HEIGHT - 700], [40, 700, gm.WIDTH, gm.HEIGHT - 700], [20, 150, gm.WIDTH / 2 + 460, 0]]

        for ver in vertical_platform:
            platform_object1 = Platform(gm.GRASS1, *ver)
            self.set_of_platforms.add(platform_object1)

    def create_ladders(self):
        ws_ladder_static = [[590, gm.HEIGHT - 210], [gm.WIDTH - 95, gm.HEIGHT - 210], [1000, gm.HEIGHT - 380], [140, gm.HEIGHT - 550]]

        for wss in ws_ladder_static:
            ladder_object = Ladder(gm.LADDER, *wss)
            self.set_of_ladders.add(ladder_object)

    def create_doors(self):
        ws_door_static = [[5, gm.HEIGHT - 334, 'down' ], [gm.WIDTH - 70, gm.HEIGHT - 673, 'up']]

        for wss in ws_door_static:
            door_object = Door(gm.DOOR, *wss)
            vec_doors.append(wss)
            self.set_of_doors.add(door_object)

# klasa planszy nr 2
class Level_2(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self.create_platforms()
        self.create_ladders()
        self.create_doors()
        self.create_items()
        self.create_enemies()

    def create_enemies(self):
        enemy1 = HorizontalEnemy(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 245, 0)
        self.set_of_enemies.add(enemy1)
        enemy2 = HorizontalEnemy(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 40, 0)
        self.set_of_enemies.add(enemy2)

    def create_items(self):
        hearth = Item(gm.HEARTH, 'hearth', 1200, gm.HEIGHT - 400)
        self.set_of_items.add(hearth)
        key = Item(gm.KEY, 'key', gm.WIDTH - 300, gm.HEIGHT - 120)
        self.set_of_items.add(key)
        diamond1 = Item(gm.DIAMOND, 'diamond1', 1350, gm.HEIGHT - 160)
        self.set_of_items.add(diamond1)
        diamond2 = Item(gm.DIAMOND, 'diamond2', 330, 120)
        self.set_of_items.add(diamond2)
        spike = Item(gm.SPIKE, 'spike', 660, gm.HEIGHT - 325)
        self.set_of_items.add(spike)






    def create_platforms(self):
        ws_platform_static = [[gm.WIDTH / 4, 40, 0, gm.HEIGHT - 40], [100, 20, 500, gm.HEIGHT - 100], [100, 20, 800, gm.HEIGHT - 100], [100, 20, 1100, gm.HEIGHT - 100],
                              [100, 20, 1290, gm.HEIGHT - 140], [200, 40, 60, 490], [100, 20, 350, gm.HEIGHT - 270], [200, 20, 550, gm.HEIGHT - 320], [100, 20, 850, gm.HEIGHT - 370],
                              [100, 20, 1150, gm.HEIGHT - 370], [300, 40, 580, gm.HEIGHT - 545], [100, 20, 280, gm.HEIGHT - 545], [100, 20, 100, gm.HEIGHT - 545]]

        for ws in ws_platform_static:
            platform_object = Platform(gm.GRASS, *ws)
            vec_platforms.append(ws)
            self.set_of_platforms.add(platform_object)

        vertical_platform = [[40, 700, -40, gm.HEIGHT - 700], [40, 700, gm.WIDTH, gm.HEIGHT - 700]]

        for ver in vertical_platform:
            platform_object1 = Platform(gm.GRASS1, *ver)
            self.set_of_platforms.add(platform_object1)

    def create_ladders(self):
        ws_ladder_static = [[10,480], [900, gm.HEIGHT - 545]]

        for wss in ws_ladder_static:
            ladder_object = Ladder(gm.LADDER, *wss)
            self.set_of_ladders.add(ladder_object)

    def create_doors(self):
        ws_door_static = []

        for wss in ws_door_static:
            door_object = Door(gm.DOOR, *wss)
            vec_doors.append(wss)
            self.set_of_doors.add(door_object)

# klasa planszy nr 3
class Level_3(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self.create_platforms()
        self.create_ladders()
        self.create_doors()
        self.create_items()
        self.create_enemies()

    def create_enemies(self):
        enemy1 = VerticalEnemy(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 0, 720)
        self.set_of_enemies.add(enemy1)
        enemy2 = Skeleton(gm.SKELETON_R1, gm.SKELETON_R, gm.SKELETON_L, 425, 0)
        self.set_of_enemies.add(enemy2)
        enemy3 = Skeleton(gm.SKELETON_R1, gm.SKELETON_R, gm.SKELETON_L, 89, 0)
        self.set_of_enemies.add(enemy3)

    def create_items(self):
        diamond_red1 = Item(gm.DIAMOND_RED, 'diamond_red1', 150, 450)
        self.set_of_items.add(diamond_red1)
        diamond1 = Item(gm.DIAMOND, 'diamond1', 150, 120)
        self.set_of_items.add(diamond1)
        key = Item(gm.KEY, 'key', 1200, 610)
        self.set_of_items.add(key)
        spike1 = Item(gm.SPIKE, 'spike', 1200, 485)
        self.set_of_items.add(spike1)
        spike2 = Item(gm.SPIKE, 'spike', 1300, 145)
        self.set_of_items.add(spike2)
        hearth = Item(gm.HEARTH, 'hearth', 1300, gm.HEIGHT - 400)
        self.set_of_items.add(hearth)


    def create_platforms(self):
        ws_platform_static = [[gm.WIDTH / 4, 40, 0, gm.HEIGHT - 40], [gm.WIDTH / 4.7, 20, 0, gm.HEIGHT - 210], [gm.WIDTH / 4.7, 20, 60, gm.HEIGHT - 380],
                              [gm.WIDTH / 4.7, 20, 0, gm.HEIGHT - 550], [gm.WIDTH / 4, 40, 1100, gm.HEIGHT - 40], [gm.WIDTH / 4.7, 20, 1100, gm.HEIGHT - 210],
                              [gm.WIDTH / 4.7, 20, 1160, gm.HEIGHT - 380], [gm.WIDTH / 4.7, 20, 1100, gm.HEIGHT - 550],[70, 20, 500, gm.HEIGHT - 465],
                              [70, 20, 600, gm.HEIGHT - 400], [70, 20, 850, gm.HEIGHT - 400], [70, 20, 950, gm.HEIGHT - 465]]

        for ws in ws_platform_static:
            platform_object = Platform(gm.GRASS, *ws)
            vec_platforms.append(ws)
            self.set_of_platforms.add(platform_object)

        vertical_platform = [[40, 700, -40, gm.HEIGHT - 700], [40, 700, gm.WIDTH, gm.HEIGHT - 700]]

        for ver in vertical_platform:
            platform_object1 = Platform(gm.GRASS1, *ver)
            self.set_of_platforms.add(platform_object1)

    def create_ladders(self):
        ws_ladder_static = [[320, gm.HEIGHT - 220],[10, gm.HEIGHT - 390],[320,gm.HEIGHT - 560],
                            [1420, gm.HEIGHT - 220],[1110, gm.HEIGHT - 390],[1420,gm.HEIGHT - 560]]

        for wss in ws_ladder_static:
            ladder_object = Ladder(gm.LADDER, *wss)
            self.set_of_ladders.add(ladder_object)

    def create_doors(self):
        ws_door_static = []

        for wss in ws_door_static:
            door_object = Door(gm.DOOR, *wss)
            vec_doors.append(wss)
            self.set_of_doors.add(door_object)

# klasa planszy nr 4
class Level_4(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self.create_platforms()
        self.create_ladders()
        self.create_doors()
        self.create_items()
        self.create_enemies()

    def create_enemies(self):
        enemy1 = VerticalEnemy1(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 340, 770)
        self.set_of_enemies.add(enemy1)
        enemy2 = VerticalEnemy2(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 340, 970)
        self.set_of_enemies.add(enemy2)
        enemy3 = VerticalEnemy1(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 340, 370)
        self.set_of_enemies.add(enemy3)
        enemy4 = VerticalEnemy2(gm.DRAGON_R1, gm.DRAGON_R, gm.DRAGON_L, 340, 570)
        self.set_of_enemies.add(enemy4)
        enemy5 = Skeleton(gm.SKELETON_R1, gm.SKELETON_R, gm.SKELETON_L, 37, 70)
        self.set_of_enemies.add(enemy5)

    def create_items(self):
        hearth = Item(gm.HEARTH, 'hearth', 1400, gm.HEIGHT - 230)
        self.set_of_items.add(hearth)
        key = Item(gm.KEY, 'key', 1450, 300)
        self.set_of_items.add(key)
        diamond1 = Item(gm.DIAMOND, 'diamond1', 925, gm.HEIGHT - 230)
        self.set_of_items.add(diamond1)
        diamond2 = Item(gm.DIAMOND, 'diamond2', 525, gm.HEIGHT - 230)
        self.set_of_items.add(diamond2)
        diamond_red1 = Item(gm.DIAMOND_RED, 'diamond_red1', 390, gm.HEIGHT - 55)
        self.set_of_items.add(diamond_red1)
        spike = Item(gm.SPIKE, 'spike', 300, gm.HEIGHT - 47)
        self.set_of_items.add(spike)


    def create_platforms(self):
        ws_platform_static = [[400, 20, 0, gm.HEIGHT - 40], [gm.WIDTH / 4.7, 20, 1100, gm.HEIGHT - 550], [gm.WIDTH / 4.7, 20, 1100, gm.HEIGHT - 200],
                              [50, 20, 900, gm.HEIGHT - 200], [50, 20, 700, gm.HEIGHT - 200], [50, 20, 500, gm.HEIGHT - 200], [50, 20, 300, gm.HEIGHT - 200],
                              [150, 20, 0, gm.HEIGHT - 200], [400, 20, 70, 100], [100, 20, 800, 150], [100, 20, 550, 150]]

        for ws in ws_platform_static:
            platform_object = Platform(gm.GRASS, *ws)
            vec_platforms.append(ws)
            self.set_of_platforms.add(platform_object)

        vertical_platform = [[40, 700, -40, gm.HEIGHT - 700], [40, 700, gm.WIDTH, gm.HEIGHT - 700]]

        for ver in vertical_platform:
            platform_object1 = Platform(gm.GRASS1, *ver)
            self.set_of_platforms.add(platform_object1)

    def create_ladders(self):
        ws_ladder_static = [[170, gm.HEIGHT - 220], [0, gm.HEIGHT - 380], [0, gm.HEIGHT - 498], [0, gm.HEIGHT - 616]]

        for wss in ws_ladder_static:
            ladder_object = Ladder(gm.LADDER, *wss)
            self.set_of_ladders.add(ladder_object)

    def create_doors(self):
        ws_door_static = []

        for wss in ws_door_static:
            door_object = Door(gm.DOOR, *wss)
            vec_doors.append(wss)
            self.set_of_doors.add(door_object)

# klasa planszy nr 5
class Finish(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self.create_platforms()
        self.create_enemies()
        self.create_ladders()
        self.create_items()

    def create_enemies(self):
        enemy1 = Boss(gm.RDRAGON_R1, gm.RDRAGON_R, gm.RDRAGON_L, 0, 1200)
        self.set_of_enemies.add(enemy1)

    def create_platforms(self):
        ws_platform_static = [[gm.WIDTH, 40, 0, gm.HEIGHT - 40], [300, 20, 500, gm.HEIGHT - 100], [300, 20, 800, gm.HEIGHT - 250],
                              [300, 20, 1100, gm.HEIGHT - 400], [150, 20, 1400, gm.HEIGHT - 550]]

        for ws in ws_platform_static:
            platform_object = Platform(gm.GRASS, *ws)
            vec_platforms.append(ws)
            self.set_of_platforms.add(platform_object)

        vertical_platform = [[40, 700, -40, gm.HEIGHT - 700], [40, 700, gm.WIDTH, gm.HEIGHT - 700]]

        for ver in vertical_platform:
            platform_object1 = Platform(gm.GRASS1, *ver)
            self.set_of_platforms.add(platform_object1)

    def create_ladders(self):
        ws_ladder_static = [[750, gm.HEIGHT - 270], [1050, gm.HEIGHT - 420], [1350, gm.HEIGHT - 570]]

        for wss in ws_ladder_static:
            ladder_object = Ladder(gm.LADDER, *wss)
            self.set_of_ladders.add(ladder_object)

    def create_items(self):
        princess = Item(gm.PRINCESS, 'princess', 1455, gm.HEIGHT - 580)
        self.set_of_items.add(princess)

#klasa przycisku
class Button:
    def __init__(self, text, width, height, text_colour,
                 background_colour, centerx, cenetry,
                 font_type=None, size=74):
        self.text = str(text)
        self.text_colour = text_colour
        self.font_type = font_type
        self.size = size
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.font = pygame.font.SysFont(self.font_type, self.size)
        self.image = self.font.render(self.text, 1, self.text_colour,
                                      self.background_colour)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [centerx, cenetry]
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surfece):
        surfece.fill(self.background_colour, self.rect)
        surfece.blit(self.image, self.rect_image)




# konkretyzacja obiektów
player = Player(gm.STAND)
current_level = Level_1(player)
player.level = current_level
#player.rect.center = screen.get_rect().center

player.rect.center = (80, gm.HEIGHT - 40)
button_1 = Button("START", 400, 150, gm.BLACK, gm.GRAY,
                gm.WIDTH//2, gm.HEIGHT//2.5, size = 74, font_type='Arial')
button_2 = Button("EXIT", 400, 150, gm.BLACK, gm.GRAY,
                gm.WIDTH//2, gm.HEIGHT//1.5, size = 74, font_type='Arial')
button_nightknight = Button("NIGHT KNIGHT", 1200, 100, gm.WHITE, gm.BLACK,
                gm.WIDTH//2, gm.HEIGHT/5.5, size = 85, font_type='Arial')
button_finish = Button("YOU DIED", 1200, 100, gm.RED, gm.BLACK,
                gm.WIDTH//2, gm.HEIGHT/5.5, size = 85, font_type='Arial')
button_win = Button("Congratulations you win!!!", 1200, 100, gm.WHITE, gm.BLACK,
                gm.WIDTH//2, gm.HEIGHT/5.5, size = 85, font_type='Arial')


# głowna pętla gry
window_open = True
active_game = False
while window_open:
    screen.blit(gm.BACKGROUND, (0, 0))
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_1.rect.collidepoint(pygame.mouse.get_pos()):
                active_game = True
                pygame.mouse.set_visible(False)
                pygame.time.delay(500)
            if button_2.rect.collidepoint(pygame.mouse.get_pos()):
                window_open = False

        if active_game:
            player.get_event(event)

    if active_game:
        #warunki zatrzymania gry
        if player.lifes <= 0:
            pygame.mixer.music.stop()
            gm.game_over.play()
            active_game = False
        if player.princess > 1:
            pygame.mixer.music.stop()
            gm.victory.play()
            gm.victory.set_volume(0.3)
            active_game = False

        # rysowanie i aktualizacja obiektów
        player.update()
        current_level = player.level
        current_level.update()
        current_level.draw(screen)
        player.draw(screen)
        text(screen, "Score: "+str(player.score), 32, gm.WIDTH/2, 10)
        text(screen, "Lifes: " + str(player.lifes), 32, gm.WIDTH / 3, 10)

    #menu gry
    #menu głowne
    elif (active_game == False) and (player.lifes > 0) and (player.princess == 0):
        button_1.draw(screen)
        button_2.draw(screen)
        button_nightknight.draw(screen)
        text(screen, "C - Jump ", 32, 300, 300)
        text(screen, "X - Shoot ", 32, 300, 350)

    #menu po śmierci
    elif (active_game == False) and (player.lifes <= 0):
        pygame.mouse.set_visible(True)
        button_finish.draw(screen)
        text(screen, "Score: " + str(player.score), 100, gm.WIDTH / 2, 230)
        button_2.draw(screen)

    #menu po "zebraniu księżniczki"
    elif (active_game == False) and (player.lifes > 0) and (player.princess > 0):
        pygame.mouse.set_visible(True)
        button_win.draw(screen)
        text(screen, "Score: " + str(player.score), 100, gm.WIDTH / 2, 230)
        button_2.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(gm.FPS)

pygame.quit()