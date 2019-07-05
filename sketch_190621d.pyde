def setup():
    frameRate(80)
    rectMode(CENTER)
    size(600,550)
    background(255,255,0)
    global kolory
    kolory=((123,104,238),(128,0,128),(255,0,255))
    fill(*kolory[0])
    strokeWeight(4)
    stroke(*kolory[2])
    global x
    global y
    x = 30
    y = 30
    
def draw():
    global x
    x=x+1
    global y
    y=y+1
    rect(x,y, height/6, width/6)
    if x > 600:
        exit()
    global kolory
    if x > 100:
        fill(*kolory[1])
        stroke(*kolory[0])    
    if x > 200:
        fill(*kolory[2])
        stroke(*kolory[1])
    if x > 300:
        fill(*kolory[0])
        stroke(*kolory[2])
    if x > 400:
        fill(*kolory[1])
        stroke(*kolory[0])
    if x > 500:
        fill(*kolory[2])
        stroke(*kolory[1])
