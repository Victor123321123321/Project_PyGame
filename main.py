import pygame
import os
import sys
import time
import sqlite3

# делаем классы для земли и стен
class Ground1(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_1_ground.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Ground1.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Roof1(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_1_roof.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Roof1.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_right1(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_1_ground_проба.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_right1.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_left1(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_1_left_wall.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_left1.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Ground2(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_2_ground.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Ground2.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Roof2(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_2_roof.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Roof2.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_right2(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_2_right_wall_проба.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_right2.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_left2(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_2_left_wall.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_left2.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Ground3(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_3_ground.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Ground3.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Roof3(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_3_roof.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Roof3.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_right3(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_3_right_wall.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_right3.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576


class Walls_left3(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join('Карта', "level_3_left_wall_ПРОБА.png"))
    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Walls_left3.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 576

# переключатель для функций
def switch_scene(scene):
    global current_scene
    current_scene = scene

# функция прыжка для главного героя
def jump(gr, rf):
    global player_y, jump_counter, make_jump
    if jump_counter >= -20:
        if pygame.sprite.collide_mask(hero_run_r, gr) and jump_counter < 19 and not pygame.sprite.collide_mask(
                hero_run_r, rf):
            jump_counter = 20
            make_jump = False
            return
        hero_run_r.y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 20
        make_jump = False

# фуннкция для бега главного героя
def moving(wl, wr):
    global go_left, go_rigth, player_x, speed
    if not pygame.sprite.collide_mask(hero_run_r, wl):
        if go_left:
            hero_run_r.x -= hero_run_r.speed_x
    if not pygame.sprite.collide_mask(hero_run_r, wr):
        if go_rigth:
            hero_run_r.x += hero_run_r.speed_x

# загрузка изображения
def load_image(name, colorkey=None):
    if name == "Idle-Sheet.png" or name == "Idle-Sheet_Left.png":
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Character', 'Idle', name)
    elif name == "Run-Sheet_Left_player.png" or name == "Run-Sheet_player.png":
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Character', 'Run', name)
    elif name == "level_1_background.png" or name == "level_2_background.png" or name == "level_3_background.png":
        fullname = os.path.join('Карта', name)
    elif name == 'Attack-01-Sheet.png' or name == 'Attack-02-Sheet.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Character', 'Attack-01', name)
    elif name == 'Run-Sheet-White.png' or name == 'Run-Sheet-White_right.png' or name == 'Run-Sheet-Black.png' or\
            name == 'Run-Sheet-Black_right.png' or name == 'Run-Sheet.png' or name == 'Run-Sheet_right.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Mob', 'Boar', 'Run', name)
    elif name == 'Hit-Sheet-White_right.png' or name == 'Hit-Sheet-White.png' or name == 'Hit-Sheet-Black_right.png' or\
            name == 'Hit-Sheet-Black.png' or name == 'Hit-Sheet_right_boar.png' or name == 'Hit-Sheet_boar.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Mob', 'Boar', 'Hit-Vanish', name)
    elif name == 'Dead-Sheet_left.png' or name == 'Dead-Sheet.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Character', 'Dead', name)
    elif name == 'Attack-Sheet.png' or name == 'Attack-Sheet_right.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Mob', 'Small Bee', 'Attack', name)
    elif name == 'Fly-Sheet.png' or name == 'Fly-Sheet_right.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Mob', 'Small Bee', 'Fly', name)
    elif name == 'Hit-Sheet.png' or name == 'Hit-Sheet_right.png':
        fullname = os.path.join('Legacy-Fantasy - High Forest 2.3', 'Mob', 'Small Bee', 'Hit', name)
    else:
        fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

# анимация персонажа и логика передвижений и атак
class AnimatedMob(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, mob_x, mob_y, speed_x, speed_y, run_flag_right, alive, count_run,
                 count_death, attack, make_jump, name, left_border, right_border):
        super().__init__(hero_run_right)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = mob_x
        self.y = mob_y
        self.run_flag_right = run_flag_right
        self.alive = alive
        self.count_run = count_run
        self.count_death = count_death
        self.attack = attack
        self.make_jump = make_jump
        self.name = name
        self.left_border = left_border
        self.right_border = right_border
    # выделяем кадры
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
    # обновляем кадры
    def update(self, go_left, go_rigth, make_jump, player_x, player_y):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
    #функция передвижения для кобанов и пчёл
    def run(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.name == 'boar' or self.name == 'boar_type_2' or self.name == 'boar_type_3' and self.alive:
            if self.x <= self.left_border or self.x >= self.right_border and self.alive:
                self.speed_x = self.speed_x * -1
                if self.run_flag_right:
                    self.run_flag_right = False
                else:
                    self.run_flag_right = True
        elif self.name == 'bee' or self.name == 'bee_type_2' or self.name == 'bee_type_3':
            if (self.name == 'bee_type_2' or self.name == 'bee_type_3') and\
                    ((self.x < 182 and self.y > 325) or (self.x < 376 and self.y > 355) or
                     (self.x < 440 and self.y > 365) or (self.x < 550 and self.y > 425)):
                self.run_flag_right = True
                self.speed_x = 1
            else:
                if self.x <= self.left_border and self.alive:
                    self.speed_x = 1
                if (self.speed_x > 0 and 50 >= self.x - hero_run_r.x >= 40):
                    self.speed_x = -1
                    if self.run_flag_right:
                        self.run_flag_right = False
                    else:
                        self.run_flag_right = True
                elif self.speed_x < 0 and 50 <= hero_run_r.x - self.x >= 40:
                    self.speed_x = 1
                    if self.run_flag_right:
                        self.run_flag_right = False
                    else:
                        self.run_flag_right = True
                elif self.x >= self.right_border and self.alive:
                    self.speed_x = -1
                if (self.x <= self.left_border or self.x >= self.right_border) and self.alive:
                    if self.run_flag_right:
                        self.run_flag_right = False
                    else:
                        self.run_flag_right = True
                if not not pygame.sprite.collide_mask(bee_fly_l, walls_left3):
                    self.speed_x = 1
                    if self.run_flag_right:
                        self.run_flag_right = False
                    else:
                        self.run_flag_right = True
    # раюота с логикой анимаций мобов
    def working_with_animation(self):
        if self.name == 'boar' or self.name == 'boar_type_2' or self.name == 'boar_type_3':
            if self.alive:
                if not self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'boar':
                            boar_run_left.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'boar_type_2':
                            boar_run_left2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'boar_type_3':
                            boar_run_left3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'boar':
                        boar_run_left.draw(virtual_surface)
                    elif self.name == 'boar_type_2':
                        boar_run_left2.draw(virtual_surface)
                    elif self.name == 'boar_type_3':
                        boar_run_left3.draw(virtual_surface)
                elif self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'boar':
                            boar_run_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'boar_type_2':
                            boar_run_right2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'boar_type_3':
                            boar_run_right3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'boar':
                        boar_run_right.draw(virtual_surface)
                    elif self.name == 'boar_type_2':
                        boar_run_right2.draw(virtual_surface)
                    elif self.name == 'boar_type_3':
                        boar_run_right3.draw(virtual_surface)
                self.run()
            elif not self.alive and self.count_death != 1:
                if self.speed_x > 0:
                    if self.count_run >= 20 and boar_death_r.cur_frame <= 3:
                        if self.name == 'boar':
                            boar_death_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.count_run >= 20 and boar_death_r2.cur_frame <= 3:
                        if self.name == 'boar_type_2':
                            boar_death_right2.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.count_run >= 20 and boar_death_r3.cur_frame <= 3:
                        if self.name == 'boar_type_3':
                            boar_death_right3.update(go_left, go_rigth, make_jump, player_x, player_y)
                        self.count_run = 0
                elif self.speed_x < 0:
                    if self.count_run >= 20 and boar_death_l.cur_frame <= 3:
                        if self.name == 'boar':
                            boar_death_left.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.count_run >= 20 and boar_death_l2.cur_frame <= 3:
                        if self.name == 'boar_type_2':
                            boar_death_left2.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.count_run >= 20 and boar_death_l3.cur_frame <= 3:
                        if self.name == 'boar_type_3':
                            boar_death_left3.update(go_left, go_rigth, make_jump, player_x, player_y)
                        self.count_run = 0
                if self.name == 'boar':
                    if boar_death_r.cur_frame == 3 or boar_death_l.cur_frame == 3:
                        self.count_death = 1
                elif self.name == 'boar_type_2':
                    if boar_death_r2.cur_frame == 3 or boar_death_l2.cur_frame == 3:
                        self.count_death = 1
                elif self.name == 'boar_type_3':
                    if boar_death_r3.cur_frame == 3 or boar_death_l3.cur_frame == 3:
                        self.count_death = 1
                if self.name == 'boar' or self.name == 'boar_type_2' or self.name == 'boar_type_3':
                    if self.speed_x > 0:
                        if self.name == 'boar':
                            boar_death_right.draw(virtual_surface)
                        elif self.name == 'boar_type_2':
                            boar_death_right2.draw(virtual_surface)
                        elif self.name == 'boar_type_3':
                            boar_death_right3.draw(virtual_surface)
                    else:
                        if self.name == 'boar':
                            boar_death_left.draw(virtual_surface)
                        elif self.name == 'boar_type_2':
                            boar_death_left2.draw(virtual_surface)
                        elif self.name == 'boar_type_3':
                            boar_death_left3.draw(virtual_surface)
        elif self.name == 'bee' or self.name == 'bee_type_2' or self.name == 'bee_type_3':
            if self.alive and not self.attack:
                if not self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'bee':
                            bee_fly_left.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_fly_left2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_fly_left3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'bee':
                        bee_fly_left.draw(virtual_surface)
                    elif self.name == 'bee_type_2':
                        bee_fly_left2.draw(virtual_surface)
                    elif self.name == 'bee_type_3':
                        bee_fly_left3.draw(virtual_surface)
                elif self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'bee':
                            bee_fly_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_fly_right2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_fly_right3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'bee':
                        bee_fly_right.draw(virtual_surface)
                    elif self.name == 'bee_type_2':
                        bee_fly_right2.draw(virtual_surface)
                    elif self.name == 'bee_type_3':
                        bee_fly_right3.draw(virtual_surface)
            if self.alive:
                self.run()
            if self.attack and self.alive:
                if not self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'bee':
                            bee_attack_left.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_attack_left2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_attack_left3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'bee':
                        bee_attack_right.remove(bee_attack_r3)
                        bee_attack_right.remove(bee_attack_r2)
                        bee_attack_left.remove(bee_attack_r3)
                        bee_attack_left.remove(bee_attack_r2)
                        bee_attack_left.empty()
                        bee_attack_left.add(bee_attack_l)
                        bee_attack_left.draw(virtual_surface)
                    elif self.name == 'bee_type_2':
                        bee_attack_left2.draw(virtual_surface)
                    elif self.name == 'bee_type_3':
                        bee_attack_left3.draw(virtual_surface)
                elif self.run_flag_right:
                    if self.count_run >= 5:
                        self.count_run = 0
                        if self.name == 'bee':
                            bee_attack_right.remove(bee_attack_r3)
                            bee_attack_right.remove(bee_attack_r2)
                            bee_attack_left.remove(bee_attack_r3)
                            bee_attack_left.remove(bee_attack_r2)
                            bee_attack_left.empty()
                            bee_attack_left.add(bee_attack_r)
                            bee_attack_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_attack_right2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_attack_right3.update(go_left, go_rigth, make_jump, player_x, player_y)
                    if self.name == 'bee':
                        bee_attack_right.draw(virtual_surface)
                    elif self.name == 'bee_type_2':
                        bee_attack_right2.draw(virtual_surface)
                    elif self.name == 'bee_type_3':
                        bee_attack_right3.draw(virtual_surface)
                self.speed_y = 2
            elif not self.alive and self.count_death != 1:
                if self.speed_x > 0:
                    if self.count_run >= 20 and bee_death_r.cur_frame <= 3:
                        if self.name == 'bee':
                            bee_death_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_death_right2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_death_right3.update(go_left, go_rigth, make_jump, player_x, player_y)
                elif self.speed_x < 0:
                    if self.count_run >= 20 and bee_death_l.cur_frame <= 3:
                        if self.name == 'bee':
                            bee_death_left.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_2':
                            bee_death_left2.update(go_left, go_rigth, make_jump, player_x, player_y)
                        elif self.name == 'bee_type_3':
                            bee_death_left3.update(go_left, go_rigth, make_jump, player_x, player_y)
                if self.name == 'bee':
                    if bee_death_r.cur_frame == 3 or bee_death_l.cur_frame == 3:
                        self.count_death = 1
                    else:
                        if self.speed_x > 0:
                            bee_death_right.draw(virtual_surface)
                        else:
                            bee_death_left.draw(virtual_surface)
                elif self.name == 'bee_type_2':
                    bee_death_left2.empty()
                    bee_death_right2.empty()
                    bee_death_right2.add(bee_death_r2)
                    bee_death_left2.add(bee_death_l2)
                    if bee_death_r2.cur_frame == 3 or bee_death_l2.cur_frame == 3:
                        self.count_death = 1
                    else:
                        if self.speed_x > 0:
                            bee_death_right2.draw(virtual_surface)
                        else:
                            bee_death_left2.draw(virtual_surface)
                elif self.name == 'bee_type_3':
                    if bee_death_r3.cur_frame == 3 or bee_death_l3.cur_frame == 3:
                        self.count_death = 1
                    else:
                        if self.speed_x > 0:
                            bee_death_right3.draw(virtual_surface)
                        else:
                            bee_death_left3.draw(virtual_surface)
    #передвигаем все спрайты мобов к одной точке
    def moving_all_sprites(self):
        if self.name == 'bee':
            if bee_fly_r.alive:
                bee_fly_r.rect.x = self.x
                bee_fly_r.rect.y = self.y
                bee_fly_l.rect.x = self.x
                bee_fly_l.rect.y = self.y
                bee_attack_r.rect.x = self.x
                bee_attack_r.rect.y = self.y
                bee_attack_l.rect.x = self.x
                bee_attack_l.rect.y = self.y
            bee_death_r.rect.x = self.x
            bee_death_l.rect.x = self.x
            bee_death_r.rect.y = self.y
            bee_death_l.rect.y = self.y
        elif self.name == 'bee_type_2':
            if bee_fly_r2.alive:
                bee_fly_r2.rect.x = self.x
                bee_fly_r2.rect.y = self.y
                bee_fly_l2.rect.x = self.x
                bee_fly_l2.rect.y = self.y
                bee_attack_r2.rect.x = self.x
                bee_attack_r2.rect.y = self.y
                bee_attack_l2.rect.x = self.x
                bee_attack_l2.rect.y = self.y
            bee_death_r2.rect.x = self.x
            bee_death_l2.rect.x = self.x
            bee_death_r2.rect.y = self.y
            bee_death_l2.rect.y = self.y
        elif self.name == 'bee_type_3':
            if bee_fly_r3.alive:
                bee_fly_r3.rect.x = self.x
                bee_fly_r3.rect.y = self.y
                bee_fly_l3.rect.x = self.x
                bee_fly_l3.rect.y = self.y
                bee_attack_r3.rect.x = self.x
                bee_attack_r3.rect.y = self.y
                bee_attack_l3.rect.x = self.x
                bee_attack_l3.rect.y = self.y
            bee_death_r3.rect.x = self.x
            bee_death_l3.rect.x = self.x
            bee_death_r3.rect.y = self.y
            bee_death_l3.rect.y = self.y
        elif self.name == 'boar':
            if boar_run_r.alive:
                boar_run_r.rect.x = self.x
                boar_run_r.rect.y = self.y
                boar_run_l.rect.x = self.x
                boar_run_l.rect.y = self.y
            boar_death_r.rect.x = self.x
            boar_death_l.rect.x = self.x
            boar_death_r.rect.y = self.y
            boar_death_l.rect.y = self.y
        elif self.name == 'boar_type_2':
            if boar_run_r2.alive:
                boar_run_r2.rect.x = self.x
                boar_run_r2.rect.y = self.y
                boar_run_l2.rect.x = self.x
                boar_run_l2.rect.y = self.y
            boar_death_r2.rect.x = self.x
            boar_death_l2.rect.x = self.x
            boar_death_r2.rect.y = self.y
            boar_death_l2.rect.y = self.y
        elif self.name == 'boar_type_3':
            if boar_run_r3.alive:
                boar_run_r3.rect.x = self.x
                boar_run_r3.rect.y = self.y
                boar_run_l3.rect.x = self.x
                boar_run_l3.rect.y = self.y
            boar_death_r3.rect.x = self.x
            boar_death_l3.rect.x = self.x
            boar_death_r3.rect.y = self.y
            boar_death_l3.rect.y = self.y
        elif self.name == 'hero':
            hero_standing_r.rect.x = self.x
            hero_standing_r.rect.y = self.y
            hero_standing_l.rect.x = self.x + 15
            hero_standing_l.rect.y = self.y
            self.rect.x = self.x
            self.rect.y = self.y
            hero_run_l.rect.x = self.x
            hero_run_l.rect.y = self.y
            hero_attack_r.rect.x = self.x
            hero_attack_r.rect.y = self.y
            hero_attack_l.rect.x = self.x
            hero_attack_l.rect.y = self.y
            hero_death_r.rect.x = self.x
            hero_death_r.rect.y = self.y + 15
            hero_death_l.rect.x = self.x
            hero_death_l.rect.y = self.y + 15
            hero_attack_r.rect.x = self.x
            hero_attack_l.rect.x = self.x
# задаём основные настройки экрана
WIDTH = 1040
HEIGHT = 576
FPS = 60
player_width = 35
player_height = 48
player_x = 75
player_y = HEIGHT - 130
level = 1
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
info = pygame.display.Info()
FULLSCREEN_SIZE = (info.current_w, info.current_h)
is_fullscreen = False
go_rigth = False
go_left = False
make_jump = False
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size
# загружаем картинки заднего фона
back_1 = load_image('level_1_background.png')
back_2 = load_image('level_2_background.png')
back_3 = load_image('level_3_background.png')
clock = pygame.time.Clock()
virtual_surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('adventures')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
jump_counter = 20
speed = 3
current_scene = None
# создаём все спрайты мобов и игрока
hero_run_right = pygame.sprite.Group()
hero_run_r = AnimatedMob(load_image("Run-Sheet_player.png"), 8, 1, 80, 80, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                         False, False, 'hero', 0, 0)
hero_run_right.add(hero_run_r)
hero_run_left = pygame.sprite.Group()
hero_run_l = AnimatedMob(load_image("Run-Sheet_Left_player.png"), 8, 1, 80, 80, 5, HEIGHT - 130, 3, 3, True, False, 0,
                         0, False, False, 'hero', 0, 0)
hero_run_left.add(hero_run_l)
hero_run_right.remove(hero_run_l)
hero_standing_right = pygame.sprite.Group()
hero_standing_r = AnimatedMob(load_image("Idle-Sheet.png"), 4, 1, 64, 80, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                              False, False, 'hero', 0, 0)
hero_standing_right.add(hero_standing_r)
hero_run_right.remove(hero_standing_r)
hero_standing_left = pygame.sprite.Group()
hero_standing_l = AnimatedMob(load_image("Idle-Sheet_Left.png"), 4, 1, 64, 80, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                              False, False, 'hero', 0, 0)
hero_standing_left.add(hero_standing_l)
hero_run_right.remove(hero_standing_l)
hero_attack_right = pygame.sprite.Group()
hero_attack_r = AnimatedMob(load_image("Attack-01-Sheet.png"), 8, 1, 96, 80, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                            False, False, 'hero', 0, 0)
hero_attack_right.add(hero_attack_r)
hero_run_right.remove(hero_attack_r)
hero_attack_left = pygame.sprite.Group()
hero_attack_l = AnimatedMob(load_image("Attack-02-Sheet.png"), 8, 1, 96, 80, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                            False, False, 'hero', 0, 0)
hero_attack_left.add(hero_attack_l)
hero_run_right.remove(hero_attack_l)
hero_death_right = pygame.sprite.Group()
hero_death_r = AnimatedMob(load_image("Dead-Sheet.png"), 8, 1, 80, 64, 5, HEIGHT - 130, 3, 3, True, False, 0, 0, False,
                           False, 'hero', 0, 0)
hero_death_right.add(hero_death_r)
hero_run_right.remove(hero_death_r)
hero_death_left = pygame.sprite.Group()
hero_death_l = AnimatedMob(load_image("Dead-Sheet_left.png"), 8, 1, 80, 64, 5, HEIGHT - 130, 3, 3, True, False, 0, 0,
                           False, False, 'hero', 0, 0)
hero_death_left.add(hero_death_l)
hero_run_right.remove(hero_death_l)
boar_run_left = pygame.sprite.Group()
boar_run_l = AnimatedMob(load_image("Run-Sheet-White.png"), 6, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0, False, True,
                         0, 0, False, False, 'boar', 100, 950)
boar_run_left.add(boar_run_l)
hero_run_right.remove(boar_run_l)
boar_run_right = pygame.sprite.Group()
boar_run_r = AnimatedMob(load_image("Run-Sheet-White_right.png"), 6, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0, False,
                         True, 0, 0, False, False, 'boar', 100, 950)
boar_run_right.add(boar_run_r)
hero_run_right.remove(boar_run_r)
boar_death_right = pygame.sprite.Group()
boar_death_r = AnimatedMob(load_image("Hit-Sheet-White_right.png"), 4, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0,
                           False, False, 0, 0, False, False, 'boar', 100, 950)
boar_death_right.add(boar_death_r)
hero_run_right.remove(boar_death_r)
boar_death_left = pygame.sprite.Group()
boar_death_l = AnimatedMob(load_image("Hit-Sheet-White.png"), 4, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0, False,
                           False, 0, 0, False, False, 'boar', 100, 950)
boar_death_left.add(boar_death_l)
hero_run_right.remove(boar_death_l)
boar_run_left2 = pygame.sprite.Group()
boar_run_l2 = AnimatedMob(load_image("Run-Sheet-Black.png"), 6, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0, False,
                          True, 0, 0, False, False, 'boar_type_2', 50, 655)
boar_run_left2.add(boar_run_l2)
hero_run_right.remove(boar_run_l2)
boar_run_right2 = pygame.sprite.Group()
boar_run_r2 = AnimatedMob(load_image("Run-Sheet-Black_right.png"), 6, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0,
                          False, True, 0, 0, False, False, 'boar_type_2', 50, 655)
boar_run_right2.add(boar_run_r2)
hero_run_right.remove(boar_run_r2)
boar_death_right2 = pygame.sprite.Group()
boar_death_r2 = AnimatedMob(load_image("Hit-Sheet-Black_right.png"), 4, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0,
                            False, False, 0, 0, False, False, 'boar_type_2', 50, 655)
boar_death_right2.add(boar_death_r2)
hero_run_right.remove(boar_death_r2)
boar_death_left2 = pygame.sprite.Group()
boar_death_l2 = AnimatedMob(load_image("Hit-Sheet-Black.png"), 4, 1, 48, 32, WIDTH - 100, HEIGHT - 240, -2, 0, False,
                            False, 0, 0, False, False, 'boar_type_2', 50, 655)
boar_death_left2.add(boar_death_l2)
hero_run_right.remove(boar_death_l2)
boar_run_left3 = pygame.sprite.Group()
boar_run_l3 = AnimatedMob(load_image("Run-Sheet.png"), 6, 1, 48, 32, WIDTH - 10, HEIGHT - 245, -2, 0, False, True, 0, 0,
                          False, False, 'boar_type_3', 540, WIDTH - 50)
boar_run_left3.add(boar_run_l3)
hero_run_right.remove(boar_run_l3)
boar_run_right3 = pygame.sprite.Group()
boar_run_r3 = AnimatedMob(load_image("Run-Sheet_right.png"), 6, 1, 48, 32, WIDTH - 10, HEIGHT - 245, -2, 0, False, True,
                          0, 0, False, False, 'boar_type_3', 540, WIDTH - 50)
boar_run_right3.add(boar_run_r3)
hero_run_right.remove(boar_run_r3)
boar_death_right3 = pygame.sprite.Group()
boar_death_r3 = AnimatedMob(load_image("Hit-Sheet_right_boar.png"), 4, 1, 48, 32, WIDTH - 10, HEIGHT - 245, -2, 0,
                            False, False, 0, 0, False, False, 'boar_type_3', 540, WIDTH - 50)
boar_death_right3.add(boar_death_r3)
hero_run_right.remove(boar_death_r3)
boar_death_left3 = pygame.sprite.Group()
boar_death_l3 = AnimatedMob(load_image("Hit-Sheet_boar.png"), 4, 1, 48, 32, WIDTH - 10, HEIGHT - 245, -2, 0, False,
                            False, 0, 0, False, False, 'boar_type_3', 540, WIDTH - 50)
boar_death_left3.add(boar_death_l3)
hero_run_right.remove(boar_death_l3)
bee_fly_right = pygame.sprite.Group()
bee_fly_r = AnimatedMob(load_image("Fly-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                        0, 0, False, False, 'bee', 100, 950)
bee_fly_right.add(bee_fly_r)
hero_run_right.remove(bee_fly_r)
bee_fly_left = pygame.sprite.Group()
bee_fly_l = AnimatedMob(load_image("Fly-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0, 0,
                        False, False, 'bee', 100, 950)
bee_fly_left.add(bee_fly_l)
hero_run_right.remove(bee_fly_l)
bee_attack_right = pygame.sprite.Group()
bee_attack_r = AnimatedMob(load_image("Attack-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                           False, 0, 0, False, False, 'bee', 100, 950)
bee_attack_right.add(bee_attack_r)
hero_run_right.remove(bee_attack_r)
bee_attack_left = pygame.sprite.Group()
bee_attack_l = AnimatedMob(load_image("Attack-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                           0, 0, False, False, 'bee', 100, 950)
bee_attack_left.add(bee_attack_l)
hero_run_right.remove(bee_attack_l)
bee_death_right = pygame.sprite.Group()
bee_death_r = AnimatedMob(load_image("Hit-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                          False, 0, 0, False, False, 'bee', 100, 950)
bee_death_right.add(bee_death_r)
hero_run_right.remove(bee_death_r)
bee_death_left = pygame.sprite.Group()
bee_death_l = AnimatedMob(load_image("Hit-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0,
                          0, False, False, 'bee', 100, 950)
bee_death_left.add(bee_death_l)
hero_run_right.remove(bee_death_l)
bee_fly_right2 = pygame.sprite.Group()
bee_fly_r2 = AnimatedMob(load_image("Fly-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                         0, 0, False, False, 'bee_type_2', 60, 950)
bee_fly_right2.add(bee_fly_r2)
hero_run_right.remove(bee_fly_r2)
bee_fly_left2 = pygame.sprite.Group()
bee_fly_l2 = AnimatedMob(load_image("Fly-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0, 0,
                         False, False, 'bee_type_2', 60, 950)
bee_fly_left2.add(bee_fly_l2)
hero_run_right.remove(bee_fly_l2)
bee_attack_right2 = pygame.sprite.Group()
bee_attack_r2 = AnimatedMob(load_image("Attack-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                            False, 0, 0, False, False, 'bee_type_2', 60, 950)
bee_attack_right2.add(bee_attack_r2)
hero_run_right.remove(bee_attack_r2)
bee_attack_left2 = pygame.sprite.Group()
bee_attack_l2 = AnimatedMob(load_image("Attack-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                            0, 0, False, False, 'bee_type_2', 60, 950)
bee_attack_left2.add(bee_attack_l2)
hero_run_right.remove(bee_attack_l2)
bee_death_right2 = pygame.sprite.Group()
bee_death_r2 = AnimatedMob(load_image("Hit-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                           False, 0, 0, False, False, 'bee_type_2', 60, 950)
bee_death_right2.add(bee_death_r2)
hero_run_right.remove(bee_death_r2)
bee_death_left2 = pygame.sprite.Group()
bee_death_l2 = AnimatedMob(load_image("Hit-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0,
                           0, False, False, 'bee_type_2', 60, 950)
bee_death_left2.add(bee_death_l2)
hero_run_right.remove(bee_death_l2)
bee_fly_right3 = pygame.sprite.Group()
bee_fly_r3 = AnimatedMob(load_image("Fly-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                         0, 0, False, False, 'bee_type_3', 60, 950)
bee_fly_right3.add(bee_fly_r3)
hero_run_right.remove(bee_fly_r3)
bee_fly_left3 = pygame.sprite.Group()
bee_fly_l3 = AnimatedMob(load_image("Fly-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0, 0,
                         False, False, 'bee_type_3', 60, 950)
bee_fly_left3.add(bee_fly_l3)
hero_run_right.remove(bee_fly_l3)
bee_attack_right3 = pygame.sprite.Group()
bee_attack_r3 = AnimatedMob(load_image("Attack-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                            False, 0, 0, False, False, 'bee_type_3', 60, 950)
bee_attack_right.add(bee_attack_r3)
hero_run_right.remove(bee_attack_r3)
bee_attack_left3 = pygame.sprite.Group()
bee_attack_l3 = AnimatedMob(load_image("Attack-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False,
                            0, 0, False, False, 'bee_type_3', 60, 950)
bee_attack_left.add(bee_attack_l3)
hero_run_right.remove(bee_attack_l3)
bee_death_right3 = pygame.sprite.Group()
bee_death_r3 = AnimatedMob(load_image("Hit-Sheet_right.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True,
                           False, 0, 0, False, False, 'bee_type_3', 60, 950)
bee_death_right3.add(bee_death_r3)
hero_run_right.remove(bee_death_r3)
bee_death_left3 = pygame.sprite.Group()
bee_death_l3 = AnimatedMob(load_image("Hit-Sheet.png"), 4, 1, 64, 64, WIDTH - 100, HEIGHT - 360, -1, 0, True, False, 0,
                           0, False, False, 'bee_type_3', 60, 950)
bee_death_left3.add(bee_death_l3)
hero_run_right.remove(bee_death_l3)
# загружаем картинки для игры
image_win = load_image("YoгWin.png")
image_level_1 = load_image("Level1.png")
image_level_2 = load_image("Level2.png")
image_level_3 = load_image("Level3.png")
image_button_not_active = load_image("Play_01.png")
image_button_active = load_image("Play_02.png")
tablet = load_image("tablet.png")
# ставим разные счётчики
count_run = 0
count_sound_run = 0
count_sound_fall = 0
direction = 'east'
# загружаем музыку
run_sound = pygame.mixer.Sound('audio_run2.wav')
fall_sound = pygame.mixer.Sound('fall.wav')
button_sound = pygame.mixer.Sound('the sound of pressing the button.wav')
the_sound_of_a_sword = pygame.mixer.Sound('the sound of a sword.wav')
the_sound_of_a_sword = pygame.mixer.Sound('the sound of a sword.wav')
the_sound_of_death = pygame.mixer.Sound('the sound of death.wav')
the_sound_of_victory = pygame.mixer.Sound('the sound of victory.wav')
flag_exit = True
flag_sound = True

# функция рисования текста
def draw_text(screen, text='', text_x='', text_y=''):
    font = pygame.font.Font(None, 30)
    text = font.render(text, True, (0, 0, 0))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    if current_scene == start_window:
        con = sqlite3.connect("records_bd.db")
        cur = con.cursor()
        result = cur.execute("""SELECT 1000000 - time FROM records ORDER BY time LIMIT 3""").fetchall()
        con.commit()
        con.close()
        font = pygame.font.Font(None, 22)
        text = font.render('1. ' + str(round(1000000 - result[0][0], 3)), True, (0, 0, 0))
        text_x = 130
        text_y = 30
        screen.blit(text, (text_x, text_y))
        text = font.render('2. ' + str(round(1000000 - result[1][0], 3)), True, (0, 0, 0))
        text_x = 130
        text_y = 50
        screen.blit(text, (text_x, text_y))
        text = font.render('3. ' + str(round(1000000 - result[2][0], 3)), True, (0, 0, 0))
        text_x = 130
        text_y = 70
        screen.blit(text, (text_x, text_y))

# функция для стартового окна
def start_window():
    global current_size, is_fullscreen, last_size, screen, WIDTH, HEIGHT, flag_sound, flag_exit, aa, button_far_start,\
        level
    if flag_sound:
        # настраиваем громкость и количество повторений музыки
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    running = True
    # загружаем картинки дял стартового окна
    image_start_game = load_image('background_for_start_window.png')
    image_sound_on = load_image('SoundON.png')
    image_sound_off = load_image('SoundOFF.png')
    image_records = load_image('Cubok.png')
    while running: # главный цикл стартового окна
        clock.tick(FPS)
        screen.blit(image_start_game, (0, 0))
        screen.blit(image_records, (47, 22))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # работаем с кнопкой входа в игру
        if WIDTH // 2 + 44 >= pygame.mouse.get_pos()[0] >= WIDTH // 2 - 70 and \
                HEIGHT // 2 + 20 >= pygame.mouse.get_pos()[1] >= HEIGHT // 2 - 20:
            screen.blit(image_button_active, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
        else:
            screen.blit(image_button_not_active, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
        if flag_sound:
            screen.blit(image_sound_on, (860, 15))
        else:
            screen.blit(image_sound_off, (860, 15))
        for event in pygame.event.get(): # обработка событий
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                flag_exit = False
            if event.type == pygame.MOUSEBUTTONDOWN and WIDTH // 2 + 44 >= pygame.mouse.get_pos()[0] >= WIDTH // 2 - 70\
                    and WIDTH // 2 + 20 >= pygame.mouse.get_pos()[1] >= HEIGHT // 2 - 20:
                pygame.mixer.Sound.play(button_sound)
                running = False
                level = 1
                aa = time.perf_counter()
                switch_scene(game1)
            elif click[0] and 830 <= mouse[0] <= 1040 and 0 <= mouse[1] <= 128:
                if flag_sound:
                    pygame.mixer.music.pause()
                    flag_sound = False
                else:
                    pygame.mixer.music.unpause()
                    flag_sound = True
                pygame.mixer.Sound.play(button_sound)
        draw_text(screen) # рисуем текст
        pygame.display.flip()
# настраиваем уровень, мобов и игрока
timer_sound_run = 0
run_sound_flag = False
for_the_timer_run = 0
timer_sound_fall = 0
fall_sound_flag = False
for_the_timer_fall = 0
ground_sprites1 = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
walls_left_sprites1 = pygame.sprite.Group()
walls_right_sprites1 = pygame.sprite.Group()
roof_sprites1 = pygame.sprite.Group()
roof1 = Roof1()
ground1 = Ground1()
walls_left1 = Walls_left1()
walls_right1 = Walls_right1()
ground_sprites1.add(ground1)
walls_left_sprites1.add(walls_left1)
walls_right_sprites1.add(walls_right1)
roof_sprites1.add(roof1)
ground_sprites2 = pygame.sprite.Group()
walls_left_sprites2 = pygame.sprite.Group()
walls_right_sprites2 = pygame.sprite.Group()
roof_sprites2 = pygame.sprite.Group()
roof2 = Roof2()
ground2 = Ground2()
walls_left2 = Walls_left2()
walls_right2 = Walls_right2()
ground_sprites2.add(ground2)
walls_left_sprites2.add(walls_left2)
walls_right_sprites2.add(walls_right2)
roof_sprites2.add(roof2)
ground_sprites3 = pygame.sprite.Group()
walls_left_sprites3 = pygame.sprite.Group()
walls_right_sprites3 = pygame.sprite.Group()
roof_sprites3 = pygame.sprite.Group()
roof3 = Roof3()
ground3 = Ground3()
walls_left3 = Walls_left3()
walls_right3 = Walls_right3()
ground_sprites3.add(ground3)
walls_left_sprites3.add(walls_left3)
walls_right_sprites3.add(walls_right3)
roof_sprites3.add(roof3)
make_attack = False
level = 0
aa = time.perf_counter()
flag_for_level_image = True
running = True
pygame.mixer.music.load("background sound.mp3")


def game1(): # функция первого уровня
    global run_sound, direction, count_run, FULLSCREEN_SIZE, current_size, is_fullscreen, last_size, screen, make_jump,\
        go_rigth, go_left, player_x, player_y, count_sound_run, count_sound_fall, timer_sound_run, for_the_timer_run, \
        timer_sound_fall, fall_sound_flag, for_the_timer_fall, roof1, ground1, walls_right1, walls_left1, level, \
        make_attack, flag_for_level_image, count_death_hero, running
    # настройка уроня
    running = True
    a = clock.tick()
    timer_sound_run += a - for_the_timer_run
    for_the_timer_run = a
    timer_sound_fall += a - for_the_timer_fall
    direction = 'east'
    count_run = 0
    make_jump = False
    go_rigth = False
    go_left = False
    hero_run_r.x = 5
    hero_run_r.y = HEIGHT - 130
    level = 1
    hero_run_r.count_run = 0
    count_sound_run = 0
    count_sound_fall = 0
    timer_sound_run = 0
    run_sound_flag = False
    for_the_timer_run = 0
    timer_sound_fall = 0
    fall_sound_flag = False
    for_the_timer_fall = 0
    make_attack = False
    boar_run_r2.x = WIDTH - 600
    boar_run_r2.y = HEIGHT - 97
    boar_run_r2.speed_x = -2
    boar_run_r2.run_flag_right = False
    boar_run_r2.count_run = 0
    boar_run_r2.count_death = 0
    boar_run_r2.alive = True
    hero_run_r.alive = True
    the_moment_of_entering_the_window = time.perf_counter()
    while running: # главный игровой цикл уровня
        clock.tick(FPS)
        if time.perf_counter() - the_moment_of_entering_the_window >= 3:
            flag_for_level_image = False
        if boar_run_r2.count_run >= 5 and boar_run_r2.alive:
            boar_run_r2.run()
        boar_run_r2.count_run += 1
        count_run += 1
        if make_attack and count_run >= 5 and hero_run_r.alive: # атака игрока
            count_run = 0
            if hero_attack_r.cur_frame == 3 and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_a_sword)
            if hero_attack_r.cur_frame >= 7:
                hero_attack_r.cur_frame = 0
                make_attack = False
            if pygame.mouse.get_pos()[0] > hero_run_r.x:
                direction = 'east'
                hero_attack_right.draw(virtual_surface)
                hero_attack_right.update(go_left, go_rigth, make_jump, player_x, player_y)
            else:
                direction = 'west'
                hero_attack_r.cur_frame += 1
                hero_attack_left.draw(virtual_surface)
                hero_attack_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        if (go_left or go_rigth) and not not pygame.sprite.collide_mask(hero_standing_r, ground1): # хождение игрока
            if (run_sound_flag and timer_sound_run >= 33000) or not run_sound_flag:
                run_sound_flag = True
                timer_sound_run = 0
                if flag_sound:
                    pygame.mixer.Sound.play(run_sound)
        else:
            pygame.mixer.Sound.stop(run_sound)
            run_sound_flag = False
        if not pygame.sprite.collide_mask(hero_standing_r, ground1): # проигрывание звука полёта игрока
            if (fall_sound_flag and timer_sound_fall >= 252000) or not fall_sound_flag:
                if flag_sound:
                    pygame.mixer.Sound.play(fall_sound)
                timer_sound_fall = 0
                fall_sound_flag = True
        else:
            fall_sound_flag = False
            pygame.mixer.Sound.stop(fall_sound)
        # анимация игрока
        if go_rigth and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_run_right.draw(virtual_surface)
            hero_run_right.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif go_left and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_run_left.draw(virtual_surface)
            hero_run_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and\
                direction == 'east' and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_right.draw(virtual_surface)
            hero_standing_right.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and\
                direction == 'west' and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_left.draw(virtual_surface)
            hero_standing_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        if not pygame.sprite.collide_mask(hero_standing_r, ground1) and not make_jump:
            hero_run_r.y += 3
        if hero_run_r.x > WIDTH - 100: # переход на новый уровень
            if not boar_run_r2.alive:
                hero_run_r.count_death = 0
                running = False
                level = 2
                switch_scene(game2)
                break
            else:
                hero_run_r.x = WIDTH - 120
        for event in pygame.event.get(): # обработка событий
            if event.type == pygame.QUIT or not flag_exit:
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not not pygame.sprite.collide_mask(
                    hero_standing_r, ground1):
                make_jump = True
                a = pygame.time.get_ticks()
                pygame.time.Clock = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                go_left = True
                direction = 'west'
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                go_left = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                go_rigth = True
                direction = 'east'
            elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                go_rigth = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not go_rigth and not go_left:
                if not make_attack and flag_sound:
                    pygame.mixer.Sound.play(the_sound_of_a_sword)
                make_attack = True
        if make_jump: # прыжок игрока
            jump(ground1, roof1)
        if go_left or go_rigth and hero_run_r.alive: # передвижение игрока
            moving(walls_left1, walls_right1)
        walls_left_sprites1.draw(virtual_surface)
        walls_right_sprites1.draw(virtual_surface)
        ground_sprites1.draw(virtual_surface)
        roof_sprites1.draw(virtual_surface)
        if pygame.mouse.get_pos()[0] > hero_run_r.x:
            hero_attack_right.draw(virtual_surface)
        else:
            hero_attack_left.draw(virtual_surface)
        virtual_surface.blit(back_1, (0, 0, WIDTH, HEIGHT))
        # перемещение всех спрайтов игрока в 1 точку
        hero_standing_r.rect.x = hero_run_r.x
        hero_standing_r.rect.y = hero_run_r.y
        hero_standing_l.rect.x = hero_run_r.x + 25
        hero_standing_l.rect.y = hero_run_r.y
        hero_run_r.rect.x = hero_run_r.x
        hero_run_r.rect.y = hero_run_r.y
        hero_run_l.rect.x = hero_run_r.x
        hero_run_l.rect.y = hero_run_r.y
        hero_attack_r.rect.x = hero_run_r.x
        hero_attack_r.rect.y = hero_run_r.y
        hero_attack_l.rect.x = hero_run_r.x
        hero_attack_l.rect.y = hero_run_r.y
        hero_death_r.rect.x = hero_run_r.x
        hero_death_r.rect.y = hero_run_r.y + 17
        hero_death_l.rect.x = hero_run_r.x
        hero_death_l.rect.y = hero_run_r.y + 17
        # работа с мобами
        if boar_run_r2.alive:
            boar_run_r2.moving_all_sprites()
        if boar_run_r2.count_death != 1:
            boar_run_r2.working_with_animation()
        if go_rigth and hero_run_r.alive:
            hero_run_right.draw(virtual_surface)
        elif go_left and hero_run_r.alive:
            hero_run_left.draw(virtual_surface)
        elif make_attack and hero_run_r.alive:
            if pygame.mouse.get_pos()[0] > hero_run_r.x:
                hero_attack_right.draw(virtual_surface)
                if 0 <= boar_run_r2.x - hero_run_r.x <= 50:
                    boar_run_r2.alive = False
            else:
                hero_attack_left.draw(virtual_surface)
                if 0 <= hero_run_r.x - boar_run_r2.x <= 50:
                    boar_run_r2.alive = False
        # анимация стояния игрока
        elif not make_attack and not go_left and not go_rigth and direction == 'east' and hero_run_r.alive:
            hero_standing_right.draw(virtual_surface)
        elif not make_attack and not go_left and not go_rigth and direction == 'west' and hero_run_r.alive:
            hero_standing_left.draw(virtual_surface)
        if not not pygame.sprite.collide_mask(hero_standing_r, boar_run_r2) and boar_run_r2.alive:
            if hero_run_r.alive and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_death)
            hero_run_r.alive = False
            make_jump = False
        # логика смерти игрока
        if not hero_run_r.alive and hero_run_r.count_death != 1:
            if direction == 'east':
                if count_run >= 5:
                    count_run = 0
                    hero_death_right.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_right.draw(virtual_surface)
            else:
                if count_run >= 5:
                    count_run = 0
                    hero_death_left.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_left.draw(virtual_surface)
            if hero_death_r.cur_frame >= 7 or hero_death_l.cur_frame >= 7:
                hero_run_r.count_death = 1
        player_sprites.draw(virtual_surface)
        player_sprites.update(go_left, go_rigth, make_jump, player_x, player_y)
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        hero_run_r.moving_all_sprites()
        # начало игры заново
        if not hero_run_r.alive and hero_run_r.count_death == 1:
            direction = 'east'
            count_run = 0
            make_jump = False
            go_rigth = False
            running = False
            go_left = False
            hero_run_r.x = 5
            hero_run_r.y = HEIGHT - 130
            level = 1
            count_run = 0
            count_sound_run = 0
            count_sound_fall = 0
            timer_sound_run = 0
            run_sound_flag = False
            for_the_timer_run = 0
            timer_sound_fall = 0
            fall_sound_flag = False
            for_the_timer_fall = 0
            make_attack = False
            boar_run_r.alive = True
            boar_run_r2.x = WIDTH - 100
            boar_run_r2.y = HEIGHT - 240
            boar_run_r2.count_death = 0
            hero_run_r.alive = True
            hero_death_l.cur_frame = 0
            hero_death_r.cur_frame = 0
            boar_death_l2.cur_frame = 0
            boar_death_r2.cur_frame = 0
            hero_run_r.count_death = 0
            switch_scene(game1)
        if flag_for_level_image:
            screen.blit(image_level_1, (255, 250))
        pygame.display.flip()


def game2(): # функция для второго уровня
    global run_sound, direction, count_run, FULLSCREEN_SIZE, current_size, is_fullscreen, last_size, screen, make_jump,\
        go_rigth, go_left, player_x, player_y, count_sound_run, count_sound_fall, timer_sound_run, for_the_timer_run, \
        timer_sound_fall, fall_sound_flag, for_the_timer_fall, roof2, ground2, walls_right2, walls_left2, level, \
        run_sound_flag, make_attack, boar_death_r, boar_death_l, boar_run_right, boar_run_left, hero_Right,\
        player_height, player_widt, flag_for_level_image, current_sceneent
    # настройка уровня
    go_left = False
    go_rigth = False
    make_jump = False
    flag_for_level_image = True
    a = clock.tick()
    timer_sound_run += a - for_the_timer_run
    for_the_timer_run = a
    timer_sound_fall += a - for_the_timer_fall
    for_the_timer_fall = a
    hero_run_r.y = HEIGHT - 270
    hero_run_r.x = 5
    boar_run_r.x = WIDTH - 100
    boar_run_r.y = HEIGHT - 240
    boar_run_r.speed_x = -2
    boar_run_r.run_flag_right = False
    boar_run_r.count_run = 0
    boar_run_r.count_death = 0
    boar_run_r.alive = True
    hero_run_r.count_death = 0
    hero_run_r.alive = True
    bee_fly_r.x = WIDTH - 100
    bee_fly_r.y = HEIGHT - 360
    bee_fly_r.speed_x = -1
    bee_fly_r.speed_y = 0
    bee_fly_r.run_flag_right = False
    bee_fly_r.count_run = 0
    bee_fly_r.count_death = 0
    bee_fly_r.alive = True
    bee_fly_r.attack = False
    running = True
    the_moment_of_entering_the_window = time.perf_counter()
    while running: # главный игровой цикл уровня
        clock.tick(FPS)
        if time.perf_counter() - the_moment_of_entering_the_window >= 3:
            flag_for_level_image = False
        count_run += 1
        if boar_run_r.count_run >= 5 and boar_run_r.alive:
            boar_run_r.run()
        bee_fly_r.count_run += 1
        boar_run_r.count_run += 1
        if bee_fly_r.count_run >= 5 and bee_fly_r.alive:
            bee_fly_r.run()
        if hero_run_r.alive: # анимация игрока
            if make_attack and count_run >= 5:
                count_run = 0
                if hero_attack_r.cur_frame == 3 and flag_sound:
                    pygame.mixer.Sound.play(the_sound_of_a_sword)
                if hero_attack_r.cur_frame >= 7:
                    hero_attack_r.cur_frame = 0
                    make_attack = False
                if pygame.mouse.get_pos()[0] > hero_run_r.x:
                    direction = 'east'
                    hero_attack_right.draw(virtual_surface)
                    hero_attack_right.update(go_left, go_rigth, make_jump, player_x, player_y)
                else:
                    direction = 'west'
                    hero_attack_r.cur_frame += 1
                    hero_attack_left.draw(virtual_surface)
                    hero_attack_left.update(go_left, go_rigth, make_jump, player_x, player_y)
            if (go_left or go_rigth) and not not pygame.sprite.collide_mask(hero_run_r, ground2):
                if (run_sound_flag and timer_sound_run >= 33000) or not run_sound_flag:
                    run_sound_flag = True
                    timer_sound_run = 0
                    if flag_sound:
                        pygame.mixer.Sound.play(run_sound)
            else:
                pygame.mixer.Sound.stop(run_sound)
                run_sound_flag = False
            if not pygame.sprite.collide_mask(hero_run_r, ground2): # проигрывание звука полёта игрока
                if (fall_sound_flag and timer_sound_fall >= 252000) or not fall_sound_flag:
                    if flag_sound:
                        pygame.mixer.Sound.play(fall_sound)
                    timer_sound_fall = 0
                    fall_sound_flag = True
            else:
                fall_sound_flag = False
                pygame.mixer.Sound.stop(fall_sound)
            # анимация игрока
            if go_rigth and count_run >= 5:
                count_run = 0
                hero_run_right.draw(virtual_surface)
                hero_run_right.update(go_left, go_rigth, make_jump, player_x, player_y)
            elif go_left and count_run >= 5:
                count_run = 0
                hero_run_left.draw(virtual_surface)
                hero_run_left.update(go_left, go_rigth, make_jump, player_x, player_y)
            elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and \
                    direction == 'east' and count_run >= 5:
                count_run = 0
                hero_standing_right.draw(virtual_surface)
                hero_standing_right.update(go_left, go_rigth, make_jump, player_x, player_y)
            elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and \
                    direction == 'west' and count_run >= 5:
                count_run = 0
                hero_standing_left.draw(virtual_surface)
                hero_standing_left.update(go_left, go_rigth, make_jump, player_x, player_y)
            elif not go_left and not go_rigth and not make_jump and count_run >= 5 and direction == 'east' and\
                    count_run >= 5:
                count_run = 0
                hero_standing_right.draw(virtual_surface)
                hero_standing_right.update(go_left, go_rigth, make_jump, player_x, player_y)
            elif not go_left and not go_rigth and not make_jump and count_run >= 5 and direction == 'west' and\
                    count_run >= 5:
                count_run = 0
                hero_standing_left.draw(virtual_surface)
                hero_standing_left.update(go_left, go_rigth, make_jump, player_x, player_y)
            if not pygame.sprite.collide_mask(hero_run_r, ground2) and not make_jump:
                hero_run_r.y += 3
        for event in pygame.event.get(): # обработка событий
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if hero_run_r.alive:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not not pygame.sprite.collide_mask(
                        hero_run_r, ground2):
                    make_jump = True
                    pygame.time.Clock = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    go_left = True
                    direction = 'west'
                elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                    go_left = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    go_rigth = True
                    direction = 'east'
                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    go_rigth = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not go_rigth and not go_left:
                    if not make_attack and flag_sound:
                        pygame.mixer.Sound.play(the_sound_of_a_sword)
                    make_attack = True
        if hero_run_r.x > WIDTH - 100: # переход на следующий уровень
            if not bee_fly_r.alive and not boar_run_r.alive:
                hero_run_r.x = 5
                hero_run_r.y = HEIGHT - 270
                switch_scene(game3)
                running = False
                level = 3
            else:
                hero_run_r.x = WIDTH - 100
                hero_run_r.y = HEIGHT - 270
        elif hero_run_r.x < 0:
            hero_run_r.x = 5
            hero_run_r.y = HEIGHT - 270
            go_left = False
        if make_jump: # прыжок игрока
            jump(ground2, roof2)
        if (go_left or go_rigth) and hero_run_r.alive: # бег игрока
            moving(walls_left2, walls_right2)
        walls_left_sprites2.draw(virtual_surface)
        walls_right_sprites2.draw(virtual_surface)
        ground_sprites2.draw(virtual_surface)
        roof_sprites2.draw(virtual_surface)
        virtual_surface.blit(back_2, (0, 0, WIDTH, HEIGHT))
        hero_run_r.moving_all_sprites()
        # работа с мобами
        if boar_run_r.alive:
            boar_run_r.moving_all_sprites()
        if bee_fly_r.alive:
            bee_fly_r.moving_all_sprites()
        if hero_run_r.alive:
            if go_rigth:
                hero_run_right.draw(virtual_surface)
            elif go_left:
                hero_run_left.draw(virtual_surface)
            elif make_attack:
                if pygame.mouse.get_pos()[0] > hero_run_r.x:
                    hero_attack_right.draw(virtual_surface)
                    if 0 <= boar_run_r.x - hero_run_r.x <= 50:
                        boar_run_r.alive = False
                    if 0 <= bee_fly_r.x - hero_run_r.x <= 50:
                        bee_fly_r.alive = False
                        bee_fly_r.attack = False
                else:
                    if 0 <= hero_run_r.x - boar_run_r.x <= 50:
                        boar_run_r.alive = False
                    if 0 <= hero_run_r.x - bee_fly_r.x <= 50:
                        bee_fly_r.alive = False
                        bee_fly_r.attack = False
                    hero_attack_left.draw(virtual_surface)
            elif not make_attack and not go_left and not go_rigth and direction == 'east':
                hero_standing_right.draw(virtual_surface)
            elif not make_attack and not go_left and not go_rigth and direction == 'west':
                hero_standing_left.draw(virtual_surface)
        if boar_run_r.count_death != 1:
            boar_run_r.working_with_animation()
        if bee_fly_r.count_death != 1:
            bee_fly_r.working_with_animation()
        if not not pygame.sprite.collide_mask(hero_run_r, bee_fly_r) and bee_fly_r.alive:
            if hero_run_r.alive and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_death)
            hero_run_r.alive = False
            bee_fly_r.speed_y = 0
            make_jump = False
        elif not not pygame.sprite.collide_mask(hero_run_r, boar_run_r) and boar_run_r.alive:
            if hero_run_r.alive and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_death)
            hero_run_r.alive = False
            make_jump = False
        if -50 <= bee_fly_r.x - hero_run_r.x <= 50 and bee_fly_r.y <= hero_run_r.y:
            bee_fly_r.attack = True
            bee_fly_r.speed_y = 2
        else:
            bee_fly_r.attack = False
            bee_fly_r.speed_y = 0
        if not hero_run_r.alive and hero_run_r.count_death != 1: # логика смерти игрока
            if direction == 'east':
                if count_run >= 5:
                    count_run = 0
                    hero_death_right.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_right.draw(virtual_surface)
            else:
                if count_run >= 5:
                    count_run = 0
                    hero_death_left.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_left.draw(virtual_surface)
            if hero_death_r.cur_frame >= 7 or hero_death_l.cur_frame >= 7:
                hero_run_r.count_death = 1
        if not hero_run_r.alive and hero_run_r.count_death == 1: # начало уроня заново
            direction = 'east'
            count_run = 0
            make_jump = False
            go_rigth = False
            running = False
            go_left = False
            player_width = 35
            player_height = 48
            hero_run_r.x = 5
            hero_run_r.y = HEIGHT - 130
            level = 1
            count_run = 0
            count_sound_run = 0
            count_sound_fall = 0
            timer_sound_run = 0
            run_sound_flag = False
            for_the_timer_run = 0
            timer_sound_fall = 0
            fall_sound_flag = False
            for_the_timer_fall = 0
            make_attack = False
            boar_run_r.alive = True
            boar_run_r.x = WIDTH - 100
            boar_run_r.y = HEIGHT - 240
            hero_run_r.alive = True
            hero_run_r.count_death = 0
            boar_run_r.count_death = 0
            bee_fly_r.speed_y = 0
            bee_fly_r.run_flag_right = False
            bee_fly_r.count_run = 0
            bee_fly_r.count_death = 0
            bee_fly_r.alive = True
            bee_fly_r.attack = False
            bee_fly_r.x = WIDTH - 100
            bee_fly_r.y = HEIGHT - 360
            bee_fly_r.speed_x = -1
            hero_death_l.cur_frame = 0
            hero_death_r.cur_frame = 0
            bee_death_l.cur_frame = 0
            bee_death_r.cur_frame = 0
            boar_death_l.cur_frame = 0
            boar_death_r.cur_frame = 0
            boar_death_l2.cur_frame = 0
            boar_death_r2.cur_frame = 0
            switch_scene(game1)
        player_sprites.update(go_left, go_rigth, make_jump, player_x, player_y)
        player_sprites.draw(virtual_surface)
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        if flag_for_level_image:
            screen.blit(image_level_2, (255, 250))
        pygame.display.flip()


def game3(): # функция третьего уровня
    global run_sound, direction, count_run, FULLSCREEN_SIZE, current_size, is_fullscreen, last_size, screen, make_jump,\
        go_rigth, go_left, player_x, player_y, count_sound_run, count_sound_fall, timer_sound_run, for_the_timer_run, \
        timer_sound_fall, fall_sound_flag, for_the_timer_fall, roof3, ground3, walls_right3, walls_left3, make_attack,\
        aa, image_win, level, run_sound_flag
    # настройка уровня
    running = True
    go_left = False
    go_rigth = False
    make_jump = False
    flag_for_level_image = True
    a = clock.tick()
    timer_sound_run += a - for_the_timer_run
    for_the_timer_run = a
    timer_sound_fall += a - for_the_timer_fall
    for_the_timer_fall = a
    hero_run_r.y = HEIGHT - 270
    hero_run_r.x = 5
    hero_run_r.alive = True
    boar_run_r3.x = WIDTH - 50
    boar_run_r3.y = HEIGHT - 111
    boar_run_r3.speed_x = -2
    boar_run_r3.run_flag_right = False
    boar_run_r3.count_run = 0
    boar_run_r3.count_death = 0
    boar_run_r3.alive = True
    hero_run_r.count_run = 0
    bee_fly_r2.x = 200
    bee_fly_r2.y = 200
    bee_fly_r2.speed_x = -1
    bee_fly_r2.speed_y = 0
    bee_fly_r2.run_flag_right = False
    bee_fly_r2.count_run = 0
    bee_fly_r2.count_death = 0
    bee_fly_r2.alive = True
    bee_fly_r2.attack = False
    bee_fly_r3.x = 500
    bee_fly_r3.y = 100
    bee_fly_r3.speed_x = -1
    bee_fly_r3.speed_y = 0
    bee_fly_r3.run_flag_right = False
    bee_fly_r3.count_run = 0
    bee_fly_r3.count_death = 0
    bee_fly_r3.alive = True
    bee_fly_r3.attack = False
    the_moment_of_entering_the_window = time.perf_counter()
    while running: # главный игровой цикль уровня
        if time.perf_counter() - the_moment_of_entering_the_window >= 3:
            flag_for_level_image = False
        virtual_surface.blit(back_3, (0, 0, WIDTH, HEIGHT))
        bee_attack_right3.add(bee_attack_r3)
        bee_attack_left3.add(bee_attack_l3)
        clock.tick(FPS)
        count_run += 1
        hero_run_r.count_run += 1
        if boar_run_r3.count_run >= 5:
            boar_run_r3.run()
        bee_fly_r2.count_run += 1
        bee_fly_r3.count_run += 1
        boar_run_r3.count_run += 1
        if make_attack and count_run >= 5: # логика атаки игрока
            count_run = 0
            if hero_attack_r.cur_frame == 3 and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_a_sword)
            if hero_attack_r.cur_frame >= 7:
                hero_attack_r.cur_frame = 0
                make_attack = False
            if pygame.mouse.get_pos()[0] > hero_run_r.x:
                direction = 'east'
                hero_attack_right.draw(virtual_surface)
                hero_attack_right.update(go_left, go_rigth, make_jump, player_x, player_y)
            else:
                direction = 'west'
                hero_attack_r.cur_frame += 1
                hero_attack_left.draw(virtual_surface)
                hero_attack_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        if (not not pygame.sprite.collide_mask(hero_standing_r, boar_run_r3) and boar_run_r3.alive) or\
                (not not pygame.sprite.collide_mask(hero_run_r, bee_fly_r2) and bee_fly_r2.alive) or\
                (not not pygame.sprite.collide_mask(hero_run_r, bee_fly_r3) and bee_fly_r3.alive): # поведение мобов
            if hero_run_r.alive and flag_sound:
                pygame.mixer.Sound.play(the_sound_of_death)
            hero_run_r.alive = False
            make_jump = False
            bee_fly_r.speed_y = 0
            bee_fly_r2.speed_y = 0
            bee_fly_r3.speed_y = 0
        if (go_left or go_rigth) and not not pygame.sprite.collide_mask(hero_run_r, ground3): # звук хождения игрока
            if (run_sound_flag and timer_sound_run >= 33000) or not run_sound_flag:
                run_sound_flag = True
                timer_sound_run = 0
                if flag_sound:
                    pygame.mixer.Sound.play(run_sound)
        else:
            pygame.mixer.Sound.stop(run_sound)
            run_sound_flag = False
        if not pygame.sprite.collide_mask(hero_run_r, ground3):
            if (fall_sound_flag and timer_sound_fall >= 252000) or not fall_sound_flag: # звук полёта игрока
                if flag_sound:
                    pygame.mixer.Sound.play(fall_sound)
                timer_sound_fall = 0
                fall_sound_flag = True
        else:
            fall_sound_flag = False
            pygame.mixer.Sound.stop(fall_sound)
        # анимация игрока
        if go_rigth and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_run_right.draw(virtual_surface)
            hero_run_right.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif go_left and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_run_left.draw(virtual_surface)
            hero_run_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and \
                direction == 'east' and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_right.draw(virtual_surface)
            hero_standing_right.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not make_attack and not go_left and not go_rigth and not make_jump and count_run >= 5 and \
                direction == 'west' and count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_left.draw(virtual_surface)
            hero_standing_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not go_left and not go_rigth and not make_jump and count_run >= 5 and direction == 'east' and\
                count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_right.draw(virtual_surface)
            hero_standing_right.update(go_left, go_rigth, make_jump, player_x, player_y)
        elif not go_left and not go_rigth and not make_jump and count_run >= 5 and direction == 'west' and\
                count_run >= 5 and hero_run_r.alive:
            count_run = 0
            hero_standing_left.draw(virtual_surface)
            hero_standing_left.update(go_left, go_rigth, make_jump, player_x, player_y)
        if not pygame.sprite.collide_mask(hero_run_r, ground3) and not make_jump:
            hero_run_r.y += 3
        for event in pygame.event.get(): # обработка событий
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif hero_run_r.x < 0:
                hero_run_r.x = 0
                hero_run_r.y = HEIGHT - 270
                go_left = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not not pygame.sprite.collide_mask(
                    hero_run_r, ground3):
                make_jump = True
                a = pygame.time.get_ticks()
                pygame.time.Clock = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                go_left = True
                direction = 'west'
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                go_left = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                go_rigth = True
                direction = 'east'
            elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                go_rigth = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not go_rigth and not go_left:
                if not make_attack and flag_sound:
                    pygame.mixer.Sound.play(the_sound_of_a_sword)
                make_attack = True
        if hero_run_r.x > WIDTH - 100: # переход на финальное окно
            if not boar_run_r3.alive and not bee_fly_r2.alive and not bee_fly_r3.alive:
                if flag_sound:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.Sound.play(the_sound_of_victory)
                switch_scene(start_window)
                pygame.mixer.Sound.stop(fall_sound)
                pygame.mixer.Sound.stop(run_sound)
                running = False
                screen.blit(image_win, (232, 250))
                pygame.display.flip()
                clock.tick(0.5)
                screen.blit(image_win, (10000, 10000))
                # запись с базу данных результатов игры
                con = sqlite3.connect("records_bd.db")
                cur = con.cursor()
                cur.execute(
                    """INSERT INTO records(time) VALUES(?)""", (str(time.perf_counter() - aa), )).fetchall()
                con.commit()
                con.close()
                switch_scene(final_window)
        if make_jump and hero_run_r.alive: # прыжок игрока
            jump(ground3, roof3)
        if (go_left or go_rigth) and (hero_run_r.alive) and hero_run_r.x >= 0 and\
                (hero_run_r.x < WIDTH - 80 or (not boar_run_r3.alive and not bee_fly_r3.alive and not
                boar_run_r2.alive)): # хождение игрока
            moving(walls_left3, walls_right3)
        walls_left_sprites3.draw(virtual_surface)
        walls_right_sprites3.draw(virtual_surface)
        ground_sprites3.draw(virtual_surface)
        roof_sprites3.draw(virtual_surface)
        # перемещение все спрайтов игрока в 1 точку
        hero_standing_r.rect.x = hero_run_r.x
        hero_standing_r.rect.y = hero_run_r.y
        hero_standing_l.rect.x = hero_run_r.x + 25
        hero_standing_l.rect.y = hero_run_r.y
        hero_run_r.rect.x = hero_run_r.x
        hero_run_r.rect.y = hero_run_r.y
        hero_run_l.rect.x = hero_run_r.x
        hero_run_l.rect.y = hero_run_r.y
        hero_attack_r.rect.x = hero_run_r.x
        hero_attack_r.rect.y = hero_run_r.y
        hero_attack_l.rect.x = hero_run_r.x
        hero_attack_l.rect.y = hero_run_r.y
        hero_death_r.rect.x = hero_run_r.x
        hero_death_r.rect.y = hero_run_r.y + 15
        hero_death_l.rect.x = hero_run_r.x
        hero_death_l.rect.y = hero_run_r.y + 15
        # логика мобов
        if bee_fly_r2.alive:
            bee_fly_r2.moving_all_sprites()
        if bee_fly_r3.alive:
            bee_fly_r3.moving_all_sprites()
        if bee_fly_r2.count_death != 1:
            bee_fly_r2.working_with_animation()
        if bee_fly_r3.count_death != 1:
            bee_fly_r3.working_with_animation()
        if boar_run_r3.alive:
            boar_run_r3.moving_all_sprites()
        if boar_run_r3.count_death != 1:
            boar_run_r3.working_with_animation()
        if go_rigth and hero_run_r.alive:
            hero_run_right.draw(virtual_surface)
        elif go_left and hero_run_r.alive:
            hero_run_left.draw(virtual_surface)
        elif make_attack and hero_run_r.alive: # атака игрока
            if pygame.mouse.get_pos()[0] > hero_run_r.x:
                hero_attack_right.draw(virtual_surface)
                if 0 <= boar_run_r3.x - hero_run_r.x <= 50:
                    boar_run_r3.alive = False
                if 0 <= bee_fly_r2.x - hero_run_r.x <= 50 and hero_run_r.y - bee_fly_r2.y <= 50:
                    bee_fly_r2.alive = False
                    bee_fly_r2.attack = False
                if 0 <= bee_fly_r3.x - hero_run_r.x <= 50 and hero_run_r.y - bee_fly_r3.y <= 50:
                    bee_fly_r3.alive = False
                    bee_fly_r3.attack = False
            else:
                hero_attack_left.draw(virtual_surface)
                if 0 <= hero_run_r.x - boar_run_r3.x <= 50:
                    boar_run_r3.alive = False
                if 0 <= hero_run_r.x - bee_fly_r2.x <= 50 and hero_run_r.y - bee_fly_r2.y <= 50:
                    bee_fly_r2.alive = False
                if 0 <= hero_run_r.x - bee_fly_r3.x <= 50 and hero_run_r.y - bee_fly_r3.y <= 50:
                    bee_fly_r3.alive = False
                    bee_fly_r3.attack = False
        # анимация стояния игрока
        elif not make_attack and not go_left and not go_rigth and direction == 'east' and hero_run_r.alive:
            hero_standing_right.draw(virtual_surface)
        elif not make_attack and not go_left and not go_rigth and direction == 'west' and hero_run_r.alive:
            hero_standing_left.draw(virtual_surface)
        elif not go_left and not go_rigth and direction == 'east' and hero_run_r.alive:
            hero_standing_right.draw(virtual_surface)
        elif not go_left and not go_rigth and direction == 'west' and hero_run_r.alive:
            hero_standing_left.draw(virtual_surface)
        player_sprites.draw(virtual_surface)
        player_sprites.update(go_left, go_rigth, make_jump, player_x, player_y)
        # реакция пчёл на игрока
        if -50 <= bee_fly_r2.x - hero_run_r.x <= 50 and bee_fly_r2.y <= hero_run_r.y:
            bee_fly_r2.attack = True
            bee_fly_r2.speed_y = 2
        else:
            bee_fly_r2.attack = False
            bee_fly_r2.speed_y = 0
        if -50 <= bee_fly_r3.x - hero_run_r.x <= 50 and bee_fly_r3.y <= hero_run_r.y:
            bee_fly_r3.attack = True
            bee_fly_r3.speed_y = 2
        else:
            bee_fly_r3.attack = False
            bee_fly_r3.speed_y = 0
        if not hero_run_r.alive and hero_run_r.count_death != 1: # логика смерти игрока
            if direction == 'east':
                if count_run >= 5:
                    count_run = 0
                    hero_death_right.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_right.draw(virtual_surface)
            else:
                if count_run >= 5:
                    count_run = 0
                    hero_death_left.update(go_left, go_rigth, make_jump, hero_run_r.x, hero_run_r.y)
                hero_death_left.draw(virtual_surface)
            if hero_death_r.cur_frame >= 7 or hero_death_l.cur_frame >= 7:
                hero_run_r.count_death = 1
        if not hero_run_r.alive and hero_run_r.count_death == 1: # начало игры заново
            direction = 'east'
            count_run = 0
            make_jump = False
            go_rigth = False
            running = False
            go_left = False
            hero_run_r.x = 5
            hero_run_r.y = HEIGHT - 130
            level = 1
            count_run = 0
            count_sound_run = 0
            count_sound_fall = 0
            timer_sound_run = 0
            run_sound_flag = False
            for_the_timer_run = 0
            timer_sound_fall = 0
            fall_sound_flag = False
            for_the_timer_fall = 0
            make_attack = False
            boar_run_r.alive = True
            boar_run_r3.x = WIDTH - 100
            boar_run_r3.y = HEIGHT - 240
            boar_run_r3.count_death = 0
            hero_run_r.alive = True
            hero_death_l.cur_frame = 0
            hero_death_r.cur_frame = 0
            bee_death_l.cur_frame = 0
            bee_death_r.cur_frame = 0
            bee_death_l2.cur_frame = 0
            bee_death_r2.cur_frame = 0
            bee_death_l3.cur_frame = 0
            bee_death_r3.cur_frame = 0
            boar_death_l.cur_frame = 0
            boar_death_r.cur_frame = 0
            boar_death_l2.cur_frame = 0
            boar_death_r2.cur_frame = 0
            boar_death_l3.cur_frame = 0
            boar_death_r3.cur_frame = 0
            hero_run_r.count_death = 0
            switch_scene(game1)
            bee_fly_r2.speed_y = 0
            bee_fly_r2.run_flag_right = False
            bee_fly_r2.count_run = 0
            bee_fly_r2.count_death = 0
            bee_fly_r2.alive = True
            bee_fly_r2.attack = False
            bee_fly_r2.x = WIDTH - 100
            bee_fly_r2.y = HEIGHT - 360
            bee_fly_r2.speed_x = -1
            bee_fly_r3.speed_y = 0
            bee_fly_r3.run_flag_right = False
            bee_fly_r3.count_run = 0
            bee_fly_r3.count_death = 0
            bee_fly_r3.alive = True
            bee_fly_r3.attack = False
            bee_fly_r3.x = WIDTH - 100
            bee_fly_r3.y = HEIGHT - 360
            bee_fly_r3.speed_x = -1
        player_sprites.update(go_left, go_rigth, make_jump, player_x, player_y)
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        if flag_for_level_image:
            screen.blit(image_level_3, (255, 250))
        pygame.display.flip()


def final_window(): # функция для финального окна
    global current_size, is_fullscreen, last_size, level, go_left, go_rigth, aa
    running = True
    go_left, go_rigth = False, False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
        virtual_surface.fill('black')
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        screen.blit(tablet, (106, 88))
        # вывод результатов
        draw_text(screen, 'Ваше время: ' + str(time.perf_counter() - aa) + 'секунд', 100, 100)
        pygame.display.flip()
        clock.tick(0.5)
        switch_scene(start_window)
        running = False
# переключение между функциями
switch_scene(start_window)
while current_scene is not None:
    current_scene()
pygame.quit()