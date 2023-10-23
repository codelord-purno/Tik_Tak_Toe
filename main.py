import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
import random
kivy.require("2.0.1")

class tiktak(App):
    def build(self):
        Window.clearcolor = "magenta"

        self.flag = False
        self.txt = ""
        self.check = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.button = []
        self.dict = {0:(0,0), 1: (1,0), 2:(2,0), 3:(0,1), 4:(1,1), 5:(2,1), 6:(0,2),7:(1,2),8:(2,2)}
        self.idx = 0
        self.lst = []

        self.box = BoxLayout(orientation="horizontal")


        """Button Names are reversed due to neglect don't change"""
        btn_single = Button(text = "Multi Player", color = "black", background_color = "magenta",font_size = 60, on_press = self.single)
        btn_multi = Button(text = "Single Player", color = "black",background_color = "magenta",font_size = 60, on_press = self.multi)

        self.box.add_widget(btn_multi)
        self.box.add_widget(btn_single)

        return self.box

    def single(self,instance):
        self.box.clear_widgets()
        for i in range(3):
            layer = BoxLayout(orientation = "vertical")
            for j in range(3):
                inner = BoxLayout(orientation = "horizontal", padding = 3)
                inner_btn = Button(text = str(self.idx),color = "black", on_press = self.press_S, background_color = "black", font_size = 80)
                self.button.append(inner_btn)
                inner.add_widget(inner_btn)
                layer.add_widget(inner)
                self.idx += 1

            self.box.add_widget(layer)

        return self.box


    def multi(self, instance):
        self.box.clear_widgets()
        for i in range(3):
            layer = BoxLayout(orientation = "vertical")
            for j in range(3):
                inner = BoxLayout(orientation = "horizontal",padding = 2)
                inner_btn = Button(text = str(self.idx),color = "black", on_press = self.press_M, on_release = self.release, background_color = "black", font_size = 80)
                self.button.append(inner_btn)
                inner.add_widget(inner_btn)
                layer.add_widget(inner)
                self.idx += 1

            self.box.add_widget(layer)

        return self.box


    def press_S(self, instance):
        a, b = self.dict[int(instance.text)]
        self.lst.append(int(instance.text))
        if self.flag == False:
            instance.text = "X"
            instance.color = "magenta"
            self.flag = True
        else:
            instance.text = "O"
            instance.color = "magenta"
            self.flag = False

        self.check[a][b] = instance.text

        self.traverse()


    def press_M(self, instance):
        a, b = self.dict[int(instance.text)]
        self.lst.append(int(instance.text))
        instance.text = "X"
        instance.color = "magenta"
        self.check[a][b] = instance.text

        self.traverse()


    def release(self, instance):
        rd = random.choice([i for i in range(0, 9) if i not in self.lst])
        row, col = self.dict[rd]
        cng = self.button[rd]
        cng.text = "O"
        self.check[row][col] = cng.text
        cng.color = "magenta"

        self.traverse()


    def traverse(self):
        for i in range(3):
            if self.check[i][0] == self.check[i][1] == self.check[i][2] != None:
                self.temp = self.check[i][0]
                self.end_game()

            if self.check[0][i] == self.check[1][i] == self.check[2][i] != None:
                self.temp = self.check[0][i]
                self.end_game()

        if self.check[0][0] == self.check[1][1] == self.check[2][2] != None:
            self.temp = self.check[0][0]
            self.end_game()

        if self.check[0][2] == self.check[1][1] == self.check[2][0] != None:
            self.temp = self.check[0][2]
            self.end_game()


    def end_game(self):
        # Remove all widgets from the box
        self.box.clear_widgets()
        self.game_over_screen = BoxLayout()
        lb = self.temp + " Won!"
        self.game_over_screen.add_widget(Label(text=lb, color="black", font_size=80))
        # Add the game over screen to the box
        self.box.add_widget(self.game_over_screen)


tiktak().run()
