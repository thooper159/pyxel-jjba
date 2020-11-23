import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="JoJo's Bizarre Program")
        
        pyxel.load("assets/combined.pyxres")

        self.player_x = 0
        self.player_y = 0
        
        
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.update_player()
        
    def update_player(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.player_y = (self.player_y - 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = (self.player_y + 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = (self.player_x - 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = (self.player_x + 1) % pyxel.height                    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 12, 23)

App()