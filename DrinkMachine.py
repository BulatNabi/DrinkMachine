import arcade
import time

WIDTH = 700
HEIGHT = 1280

class Coin(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('чисто фотки/монетка-removebg-preview.png', scale=0.15)
        self.center_x = center_x
        self.center_y = center_y
        self.change_y = 0
        self.bouncing = False

    def update(self):
        if self.bouncing:
            self.center_y += self.change_y
            self.change_y -= 0.6  # гравитация
            if self.center_y < 745:  # пол
                self.center_y = 745
                self.change_y *= -0.45  # отскок с потерей энергии
                if abs(self.change_y) < 1:
                    self.change_y = 0
                    self.bouncing = False



class Red(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.balance = 0
        self.show_money_options = False
        self.change = 0
        self.coin = None
        self.show_congrat = False
        self.show_need = False
        self.show_coffee = False

        self.show_put_coffee = False
        self.show_agree = False

        self.show_latte = False
        self.green_tea = False
        self.tea = False
        self.espresso = False
        self.hot_chocolate = False
        self.glintveyn = False

        self.transparency = False
        self.timeeeer = 0
        self.timeout = False

        self.progress_time = 10  # 10 секунд для заполнения прогресс-бара
        self.current_time = 0
        self.progress_percent = 0

        self.speed_x = 5
        self.speed_y = 0.3
        self.transparency_bank = False
        self.time_banknotes = False
        self.timeout_banknotes = False




        arcade.set_background_color(arcade.color.AMAZON)

        self.sprite1 = arcade.Sprite('чисто фотки/латте.png', 0.2, center_x=95, center_y=1050)
        self.sprite2 = arcade.Sprite('чисто фотки/гор шоколад.png', 0.2, center_x=245, center_y=1050)
        self.sprite3 = arcade.Sprite('чисто фотки/зеленый чай.png', 0.2, center_x=395, center_y=1050)
        self.sprite4 = arcade.Sprite('чисто фотки/чай.png', 0.2, center_x=95, center_y=900)
        self.sprite5 = arcade.Sprite('чисто фотки/глинтвейн.png', 0.2, center_x=245, center_y=900)
        self.sprite6 = arcade.Sprite('чисто фотки/эспрессо.png', 0.2, center_x=395, center_y=900)

        self.icon1 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=95, center_y=1050)
        self.icon2 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=245, center_y=1050)
        self.icon3 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=395, center_y=1050)
        self.icon4 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=95, center_y=900)
        self.icon5 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=245, center_y=900)
        self.icon6 = arcade.Sprite('чисто фотки/Иконки-vmake-no-bg-preview (carve.photos).png', 0.3, center_x=395, center_y=900)

        self.iconmoney1 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=45, center_y=640)
        self.iconmoney2 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=120, center_y=640)
        self.iconmoney3 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=195, center_y=640)
        self.iconmoney4 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=270, center_y=640)
        self.iconmoney5 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=345, center_y=640)
        self.iconmoney6 = arcade.Sprite('чисто фотки/Для денег-vmake-no-bg-preview (carve.photos).png', 0.2, center_x=420, center_y=640)

        self.display = arcade.Sprite('чисто фотки/лала.png', 0.15, 250, 1200)
        self.wind = arcade.Sprite('чисто фотки/Стёкла-no-bg-preview (carve.photos).png', 0.28, 380, 760.5)

        self.set_transparency(self.wind, 70)

        self.smoke_sprites = []

        self.smoke1 = arcade.Sprite('чисто фотки/1часть.png', 1, 600, 100)
        self.smoke2 = arcade.Sprite('чисто фотки/1часть.png', 1, 600, 100)
        self.smoke3 = arcade.Sprite('чисто фотки/2часть.png', 1, 600, 100)
        self.smoke4 = arcade.Sprite('чисто фотки/3часть.png', 1, 600, 100)
        self.smoke5 = arcade.Sprite('чисто фотки/2часть.png', 1, 600, 100)
        self.smoke6 = arcade.Sprite('чисто фотки/3часть.png', 1, 600, 100)
        self.smoke7 = arcade.Sprite('чисто фотки/4часть.png', 1, 600, 100)
        self.smoke8 = arcade.Sprite('чисто фотки/5часть.png', 1, 600, 100)
        self.smoke9 = arcade.Sprite('чисто фотки/4часть.png', 1, 600, 100)
        self.smoke10 = arcade.Sprite('чисто фотки/5часть.png', 1, 600, 100)
        self.smoke11 = arcade.Sprite('чисто фотки/6часть.png', 1, 600, 100)
        self.smoke12 = arcade.Sprite('чисто фотки/7часть.png', 1, 600, 100)
        self.smoke13 = arcade.Sprite('чисто фотки/7часть.png', 1, 600, 100)
        self.smoke14 = arcade.Sprite('чисто фотки/8часть.png', 1, 600, 100)
        self.smoke15 = arcade.Sprite('чисто фотки/9часть.png', 1, 600, 100)
        self.smoke16 = arcade.Sprite('чисто фотки/10часть.png', 1, 600, 100)
        self.smoke17 = arcade.Sprite('чисто фотки/10часть.png', 1, 600, 100)

        self.smoke_sprites.append(self.smoke1)
        self.smoke_sprites.append(self.smoke2)
        self.smoke_sprites.append(self.smoke3)
        self.smoke_sprites.append(self.smoke4)
        self.smoke_sprites.append(self.smoke5)
        self.smoke_sprites.append(self.smoke6)
        self.smoke_sprites.append(self.smoke7)
        self.smoke_sprites.append(self.smoke8)
        self.smoke_sprites.append(self.smoke9)
        self.smoke_sprites.append(self.smoke10)
        self.smoke_sprites.append(self.smoke11)
        self.smoke_sprites.append(self.smoke12)
        self.smoke_sprites.append(self.smoke13)
        self.smoke_sprites.append(self.smoke14)
        self.smoke_sprites.append(self.smoke15)
        self.smoke_sprites.append(self.smoke16)
        self.smoke_sprites.append(self.smoke17)


        self.smoke_index = 0
        self.smoke_activate_delay = 0.6  # Задержка между активациями спрайтов smoke
        self.current_smoke_activate_time = 0

        self.coffee = arcade.Sprite('чисто фотки/нормал.png', 0.34, 585, 705)

        self.sound_lib = arcade.Sound('чисто фотки/Сдача.wav')
        self.sound_coin_input = arcade.Sound('чисто фотки/Монета в автомат.wav')
        self.sound_but = arcade.Sound('чисто фотки/Звук нажатия кнопки для запуска включения кофемашины.mp3')
        self.sound_coffee = arcade.Sound('чисто фотки/звук кофе.wav')

        self.coinanim = arcade.Sprite('чисто фотки/монетка в автомат уходит.png', 0.40, 32, 737)
        self.coinanim.alpha = 255  # начальная непрозрачность
        self.banknotes = arcade.Sprite('чисто фотки/авыавыаы.png', 0.78, 165, 710)
        self.banknotes.alpha = 255

    def set_transparency(self, sprite, alpha):
        """Устанавливает полупрозрачность спрайта"""
        sprite.alpha = alpha

    def on_draw(self):

        arcade.start_render()
        arcade.draw_rectangle_filled(450, 640, 900, 1280, (195, 176, 145))

        # arcade.draw_rectangle_outline(30, 737, 30, 80, (160,0,0), 2)
        arcade.draw_rectangle_filled(30, 737, 30, 80, (20, 30, 45))

        arcade.draw_rectangle_outline(165, 746, 200, 100, (0,0,0),  2)
        arcade.draw_rectangle_filled(165, 746, 200, 100, (125, 127, 125))

        #RECTANGLE
        # arcade.draw_rectangle_outline(165, 736, 180, 30, (160, 0, 0), 2)
        arcade.draw_rectangle_filled(165, 736, 180, 30, (20, 30, 45))

        arcade.draw_rectangle_outline(380, 760, 180, 130, (0,0,0), 2)
        arcade.draw_rectangle_filled(380, 760, 180, 130, (125, 127, 125))

        arcade.draw_rectangle_outline(380, 760.5, 130, 80, (0, 0, 0), 2)
        arcade.draw_rectangle_filled(380, 760.5, 130, 80, (20, 30, 45))

        # arcade.draw_rectangle_outline(240, 550, 400, 80, (160,0,0), 2)
        arcade.draw_rectangle_filled(240, 550, 400, 80, (255, 229, 180))

        arcade.draw_rectangle_outline(580, 750, 170, 400, (0, 0, 0), 2)

        arcade.draw_rectangle_outline(580, 1100, 170, 170, (0,0,0), 2)

        #PROGRESSBAR
        arcade.draw_rectangle_outline(580, 1050, 150, 30, (0,0,0), 2)

        fill_width = self.progress_percent / 100 * 140  # Ширина заполнения
        arcade.draw_rectangle_filled(580 - (140 - fill_width) / 2, 1050, fill_width, 20, arcade.color.LIGHT_BLUE)

        # Отрисовка процентов
        arcade.draw_text(f"{self.progress_percent:.0f}%", 580, 1050, arcade.color.BLACK, 25, anchor_x="center",
                         anchor_y="center")

        if self.transparency:
            self.coinanim.draw()

        if self.transparency_bank:
            self.banknotes.draw()

        self.icon1.draw()
        self.icon2.draw()
        self.icon3.draw()
        self.icon4.draw()
        self.icon5.draw()
        self.icon6.draw()

        if self.show_money_options:
            self.iconmoney1.draw()
            self.iconmoney2.draw()
            self.iconmoney3.draw()
            self.iconmoney4.draw()
            self.iconmoney5.draw()
            self.iconmoney6.draw()

            arcade.draw_text("2", 40, 630, (0, 0, 0), 25, 50)
            arcade.draw_text("5", 115, 630, (0, 0, 0), 25, 50)
            arcade.draw_text("10", 180, 630, (0, 0, 0), 25, 50)
            arcade.draw_text("50", 255, 630, (0, 0, 0), 25, 50)
            arcade.draw_text("100", 320, 630, (0, 0, 0), 25, 50)
            arcade.draw_text("500", 400, 630, (0, 0, 0), 25, 50)

        self.sprite1.draw()
        self.sprite2.draw()
        self.sprite3.draw()
        self.sprite4.draw()
        self.sprite5.draw()
        self.sprite6.draw()

        self.display.draw()
        self.wind.draw()

        if self.coin:
            self.coin.draw()


        if self.show_congrat:
            self.show_need = False
            # arcade.draw_text(f"Напиток куплен!!", 500, 1160, (0,0,0), 12, 30)
            arcade.draw_text(f"Ваша сдача: {self.change}", 500, 1130, (0, 0, 0), 12, 30)

        if self.show_need:
            arcade.draw_text(f"Недостаточно средств", 500, 1160, (0,0,0), 12, 30)

        arcade.draw_text("Выберите напиток", 70, 1220, arcade.color.WHITE, 25, 100)
        arcade.draw_text(f"Balance: {self.balance}", 70, 1170, arcade.color.WHITE, 25, 100)

        arcade.draw_text("Пополнить баланс", 105, 540, (0, 0, 0), 25, 50)

        arcade.draw_text("Латте-100р", 62, 1110, (0, 0, 0), 13, 30)
        arcade.draw_text("Горячий шоколад-110р", 174, 1110, (0, 0, 0), 12, 30)
        arcade.draw_text("Зеленый чай-70р", 345, 1110, (0, 0, 0), 13, 30)
        arcade.draw_text("Чай-65р", 65, 960, (0, 0, 0), 13, 30)
        arcade.draw_text("Глинтвейн-120р", 190, 960, (0, 0, 0), 13, 30)
        arcade.draw_text("Эспрессо-100р", 341, 960, (0, 0, 0), 13, 30)

        arcade.draw_text("Сдача", 342, 805, (0, 0, 0), 20, 30, font_name="Kenney Rocket Square")

        if self.show_coffee:
            self.coffee.draw()

        for i in range(self.smoke_index + 1):
            self.smoke_sprites[i].draw()

        if self.show_put_coffee:
            arcade.draw_text(f"Осторожно, горячо", 500, 1160, (0, 0, 0), 12, 30)
            arcade.draw_text(f"Заберите напиток", 500, 1130, (0, 0, 0), 12, 30)

        if self.show_latte:
            arcade.draw_text(f"Латте готовится", 500, 1160, (0,0,0), 12, 30)
        if self.hot_chocolate:
            arcade.draw_text(f"Горячий шоколад готовится", 500, 1160, (0, 0, 0), 10, 30)
        if self.green_tea:
            arcade.draw_text(f"Зеленый чай готовится", 500, 1160, (0, 0, 0), 12, 30)
        if self.tea:
            arcade.draw_text(f"Чай готовится", 500, 1160, (0, 0, 0), 12, 30)
        if self.glintveyn:
            arcade.draw_text(f"Глинтвейн готовится", 500, 1160, (0, 0, 0), 12, 30)
        if self.espresso:
            arcade.draw_text(f"Эспрессо готовится", 500, 1160, (0, 0, 0), 12, 30)



    def on_mouse_press(self, x, y, button, modifiers):
        if 40 <= x <= 440 and 510 <= y <= 590:
            self.sound_but.play(0.2, 0)
            self.show_money_options = not self.show_money_options
        elif self.show_money_options:
            if self.iconmoney1.collides_with_point((x, y)):
                self.add_money(2)
                self.sound_coin_input.play(0.1, 0)
                # self.transparency = True
                self.timeout = True
            elif self.iconmoney2.collides_with_point((x, y)):
                self.add_money(5)
                self.sound_coin_input.play(0.1, 0)
                # self.transparency = True
                self.timeout = True
            elif self.iconmoney3.collides_with_point((x, y)):
                self.add_money(10)
                self.sound_coin_input.play(0.1, 0)
                # self.transparency = True
                self.timeout = True
            elif self.iconmoney4.collides_with_point((x, y)):
                self.add_money(50)
                self.timeout_banknotes = True
                # self.transparency_bank = True
            elif self.iconmoney5.collides_with_point((x, y)):
                self.add_money(100)
                self.timeout_banknotes = True
                # self.transparency_bank = True
            elif self.iconmoney6.collides_with_point((x, y)):
                self.add_money(500)
                self.timeout_banknotes = True
                # self.transparency_bank = True

        if self.show_agree:
            if self.coffee.collides_with_point((x, y)):
                self.show_coffee = False
                self.show_put_coffee = False
                self.coin = False
            self.show_agree = False

        if self.icon1.collides_with_point((x, y)):
            self.purchase(100)
            self.sound_but.play(0.2, 0)
            self.show_latte = True
        elif self.icon2.collides_with_point((x, y)):
            self.purchase(110)
            self.sound_but.play(0.2, 0)
            self.hot_chocolate = True
        elif self.icon3.collides_with_point((x, y)):
            self.purchase(70)
            self.sound_but.play(0.2, 0)
            self.green_tea = True
        elif self.icon4.collides_with_point((x, y)):
            self.purchase(65)
            self.sound_but.play(0.2, 0)
            self.tea = True
        elif self.icon5.collides_with_point((x, y)):
            self.purchase(120)
            self.sound_but.play(0.2, 0)
            self.glintveyn = True
        elif self.icon6.collides_with_point((x, y)):
            self.purchase(100)
            self.sound_but.play(0.2, 0)
            self.espresso = True

    def add_money(self, amount):
        self.balance += amount

    def purchase(self, cost):
        if self.balance >= cost:
            self.balance -= cost
            self.change = self.balance
            self.balance = 0

            if self.change > 0:
                self.coin = Coin(center_x=380, center_y=780)  # Начальная позиция монетки
                self.coin.change_y = -5  # Начальная скорость падения монетки
                self.coin.bouncing = True
                self.sound_lib.play(0.1)

            self.show_congrat = True
            self.show_coffee = True

            # Сброс прогресс-бара при покупке
            self.current_time = 0
            self.progress_percent = 0

            # Установка первого спрайта smoke активным
            self.smoke_index = 0
            self.current_smoke_activate_time = 0

            self.sound_coffee.play(0.2, 0)

            print("Напиток куплен!")
        else:
            self.show_need = not self.show_need
            print("Недостаточно средств!")

    def on_update(self, delta_time):
        if self.transparency:
            self.coinanim.alpha = max(0, self.coinanim.alpha - 6)

        if self.transparency_bank:
            self.banknotes.alpha = max(0, self.banknotes.alpha - 6)
            self.banknotes.center_y += self.speed_y

        if self.timeout:
            self.timeeeer += delta_time
            self.transparency = True
            if self.timeeeer > 1:
                self.timeeeer = 0
                self.transparency = False
                self.timeout = False
                self.coinanim.alpha = 255

        if self.timeout_banknotes:
            self.time_banknotes += delta_time
            self.transparency_bank = True
            if self.time_banknotes > 1:
                self.time_banknotes = 0
                self.transparency_bank = False
                self.timeout_banknotes = False
                self.banknotes.alpha = 255
                self.banknotes.center_y = 710
                self.banknotes.center_x = 165

        if self.show_congrat:
            self.current_time += delta_time
            self.progress_percent = min(100, self.current_time / self.progress_time * 100)
            if self.progress_percent >= 100:
                self.show_congrat = False
                self.show_put_coffee = True
                self.show_agree = True


                self.show_latte = False
                self.hot_chocolate = False
                self.green_tea = False
                self.tea = False
                self.espresso = False
                self.glintveyn = False


            # Отображение спрайтов smoke поочередно с задержкой
            self.current_smoke_activate_time += delta_time
            if self.current_smoke_activate_time >= self.smoke_activate_delay:
                self.current_smoke_activate_time = 0
                self.smoke_index += 1

                if self.smoke_index < len(self.smoke_sprites):
                    if self.smoke_index == 16:
                        self.smoke_sprites[self.smoke_index].alpha = 0
                        self.smoke_sprites[self.smoke_index-1].alpha = 0
                    else:
                        self.smoke_sprites[self.smoke_index].scale = 0.45
                        self.smoke_sprites[self.smoke_index].center_x = 580
                        self.smoke_sprites[self.smoke_index].center_y = 915
                        self.smoke_sprites[self.smoke_index].alpha = 255
                        self.smoke_sprites[self.smoke_index-1].alpha = 0
                else:
                    self.smoke_sprites[0].alpha = 0
                    self.smoke_sprites[1].alpha = 0
                    self.smoke_sprites[2].alpha = 0
                    self.smoke_sprites[3].alpha = 0
                    self.smoke_sprites[4].alpha = 0
                    self.smoke_sprites[5].alpha = 0
                    self.smoke_sprites[6].alpha = 0
                    self.smoke_sprites[7].alpha = 0
                    self.smoke_sprites[8].alpha = 0
                    self.smoke_sprites[9].alpha = 0
                    self.smoke_sprites[10].alpha = 0
                    self.smoke_sprites[11].alpha = 0
                    self.smoke_sprites[12].alpha = 0
                    self.smoke_sprites[16].alpha = 0


        if self.coin:
            self.coin.update()

def main():
    game = arcade.Window(WIDTH, HEIGHT, "Автомат")
    red = Red()
    game.show_view(red)
    arcade.run()

main()
