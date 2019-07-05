def setup():
    size(400, 400)
    textSize(100)
    textAlign(CENTER)
    fill(100)
    background(70,70,255)
def draw():
    
    if mousePressed:
        text("M", width/2-75, height/2)
        text("K", width/2+75, height/2)
   
     #najeżdżanie    
    if (mouseX >= 90 and mouseX <= 163 and mouseY >= 113 and mouseY <= 200):
        fill(255, 255, 0)
        text("M", width/2-75, height/2)
        fill(250)
        
    if (mouseX >= 237 and mouseX <= 311 and mouseY >= 113 and mouseY <= 200):
        fill(255, 255, 0)
        text("K", width/2+75, height/2)
        fill(250)
        
        
 
    if keyPressed:
        if key == "m" or key == "M":
            text("M", width/2-75, height/2)
            fill(255, 0, 55)
                
        if key == "k" or key == "K":
            text("K", width/2+75, height/2)
            fill(255, 0, 55)


        if keyCode == 39:
            text("M", width/2+75, height/2)
            fill(255, 0, 0)

        
        if keyCode == 37: 
            text("K", width/2+75, height/2)
            fill(255, 0, 0)
    


        
    s = createShape()
    s.beginShape()
    s.fill(255,0,55)
    s.noStroke()
    s.vertex(2, (height/4)*3+20)
    s.vertex(width/2-10, (height/4)*3+50)
    s.vertex(width/5, (height/5)*4+20)
    s.vertex(width, (height/5)*3)
    s.endShape(CLOSE)
    shape(s,25,25)
