import cocos
import pyglet
from cocos.actions import *

class KeyDisplay(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(KeyDisplay,self).__init__()
        self.text = cocos.text.Label("",x=100,y=100)
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = "Keys: "+ ",".join(key_names)
        self.text.element.text= text

    def on_key_press(self,key,modifiers):
        self.keys_pressed.add(key)
        self.update_text()
    
    def on_key_release(self,key,modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

# After defining the HelloWorld class,
# we need to initialize and create a window. 
# To do this, we initialize the Director(主管):
cocos.director.director.init(resizable=True)
#cocos.director.director.run(main_scene)
cocos.director.director.run(cocos.scene.Scene(KeyDisplay()))