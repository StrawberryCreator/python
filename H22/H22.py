import pgzrun as pgz
import random as r

WIDTH = 500
HEIGHT = 500
TITLE = "aim trainer"
msg = "click wich target you want"
size = 0
score = 0
display = False
time = 0
hits = 0
misses = 0

targetS = Actor ("target_s.png")
targetS.pos = center = 125, 250

targetM = Actor ("target_m.png")
targetM.pos = center = 225, 250

targetL = Actor ("target_l.png")
targetL.pos = center = 375, 250

def hideTargets ():
    targetS.pos = 1000, 1000
    targetM.pos = 1000, 1000
    targetL.pos = 1000, 1000

def update ():
    global time
    if display:
        time += 1/60

def draw ():
    global msg
    global score
    global time
    global hits
    global misses
    screen.fill ("black")
    targetS.draw ()
    targetM.draw ()
    targetL.draw ()
    if display:
        hitPrec = hits + misses
        hitPrec = hits / hitPrec * 100
        hps = hits / time
        msg = "time: "
        msg += str(round(time, 1))
        msg += " | score: "
        msg += str(score)
        msg += " | hits/s: "
        msg += str(round(hps, 1))
        msg += " | accuracy: %"
        msg += str(round(hitPrec))
    screen.draw.text (msg, center = (250, 10))

def on_mouse_down (pos):
    global msg
    global size
    global score
    global display
    global hits
    global misses
    sounds.pew.play ()
    if size == 0:
        if targetS.collidepoint (pos):
            size = 1
            hideTargets ()
            targetS.pos = r.randint (25, 475), r.randint (25, 475)
            msg = "click the targets"
        elif targetM.collidepoint (pos):
            size = 2
            hideTargets ()
            targetM.pos = r.randint (50, 450), r.randint (40, 450)
            msg = "click the targets"
        elif targetL.collidepoint (pos):
            size = 3
            hideTargets ()
            targetL.pos = r.randint (75, 425), r.randint (75, 425)
            msg = "click the targets"
    else:
        display = True
        if targetS.collidepoint (pos) or targetM.collidepoint (pos) or targetL.collidepoint (pos):
            score += 1
            sounds.hit.play ()
            hits += 1
            if size == 1:
                targetS.pos = r.randint (25, 475), r.randint (25, 475)
            elif size == 2:
                targetM.pos = r.randint (50, 450), r.randint (40, 450)
            else:
                targetL.pos = r.randint (75, 425), r.randint (75, 425)
        else:
            misses += 1

pgz.go ()