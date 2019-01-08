import cocos

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
        self.add(label)
        
# After defining the HelloWorld class,
# we need to initialize and create a window. 
# To do this, we initialize the Director(主管):
cocos.director.director.init()
# 实例化
hello_layer = HelloWorld()
main_scene = cocos.scene.Scene(hello_layer)

cocos.director.director.run(main_scene)