def on_on_overlap(sprite, otherSprite):
    info.change_score_by(10)
    pizza.set_position(randint(0, 160), randint(0, 120))
    info.start_countdown(15)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

pizza: Sprite = None
scene.set_background_color(0)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d e f . . 
            . . b d 5 5 b 1 f f 5 e e c . . 
            b b d b 5 5 5 d f b e e e e b . 
            b d d c d 5 5 b 5 e e e e e a b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(img("""
        . . . . . . b b b b . . . . . . 
            . . . . . . b 4 4 4 b . . . . . 
            . . . . . . b b 4 4 4 b . . . . 
            . . . . . b 4 b b b 4 4 b . . . 
            . . . . b d 5 5 5 4 b 4 4 b . . 
            . . . . b 3 3 3 5 5 4 e 4 4 b . 
            . . . b d 3 3 3 5 7 5 4 e 4 4 e 
            . . . b 5 3 3 3 5 5 5 5 e e e e 
            . . b d 7 5 5 5 3 3 3 5 5 e e e 
            . . b 5 5 5 5 5 3 3 3 5 5 d e e 
            . b 3 3 3 5 7 5 3 3 3 5 d d e 4 
            . b 3 3 3 5 5 5 5 5 5 d d e 4 . 
            b d 3 3 d 5 5 5 d d d 4 4 . . . 
            b 5 5 5 5 d d 4 4 4 4 . . . . . 
            4 d d d 4 4 4 . . . . . . . . . 
            4 4 4 4 . . . . . . . . . . . .
    """),
    SpriteKind.food)