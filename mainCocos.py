import cocos
from cocos.actions import *

# Subclass(子类) a Layer and define the logic of you program here:
class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld,self).__init__()
        
        label = cocos.text.Label(
            "Hello world" ,
            font_size=32 ,
            anchor_x='center' ,
            anchor_y='center'
        )
        label.position = 320, 240
        self.add(label, z=1)

        sprite = cocos.sprite.Sprite("timg.jpeg")
        sprite.position = 0,0
        # This means that our sprite will be 3 times bigger. 
        # The default scale attribute is 1:
        # scale 缩放
        sprite.scale = 1
        # but on top of the label by setting the z-value to 1, 
        # since the default z-value is 0:
        self.add(sprite, z=0)
        
        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))


# After defining the HelloWorld class,
# we need to initialize and create a window. 
# To do this, we initialize the Director(主管):
cocos.director.director.init()
# 实例化
hello_layer = HelloWorld()

#hello_layer.do(RotateBy(360,duration=10))
main_scene = cocos.scene.Scene(hello_layer)

cocos.director.director.run(main_scene)