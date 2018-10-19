import graphics as gr

window = gr.GraphWin("gleb and Kuzz project", 400, 400)

def draw_eye():
    eye1 = gr.Circle(gr.Point(150, 180), 20)
    eye1.setFill('yellow')
    eye_center2 = gr.Oval(gr.Point(130, 190), gr.Point(170, 170))
    eye1_center = gr.Circle(gr.Point(150, 180), 8)
    eye1_center.setFill('black')
    eye_center2.setFill('red')
    eye1.draw(window)
    eye_center2.draw(window)
    eye1_center.draw(window)

def draw_XBOCT():
    konchik = gr.Rectangle(gr.Point(0,350), gr.Point(100,400))
    xvost = gr.Rectangle(gr.Point(200,370), gr.Point(400,400))
    konchik.setFill('green')
    xvost.setFill('green')
    xvostic = gr.Polygon(gr.Point(0,380), gr.Point(0,300), gr.Point(50,300))
    xvostic.setFill('green')
    xvostic.draw(window)
    konchik.draw(window)
    xvost.draw(window)
def draw_face():
    x=300
    y=210
    face = gr.Rectangle(gr.Point(100, 150), gr.Point(300,250))
    face.setFill('green')
    nos = gr.Circle(gr.Point(270,190), 3)
    nos.setFill('black')
    yazik = gr.Line(gr.Point(x,y), gr.Point(x+1,y))
    yazik.setOutline('red')
    face.draw(window)
    nos.draw(window)
def draw_textt():
    window.setBackground('pink')
    message = gr.Text(gr.Point(window.getWidth()/2, 30),  'Я прогал всю ночь и я устал')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(window)
def draw_telo():
    telo = gr.Rectangle(gr.Point(100, 250), gr.Point(200,400))
    telo.setFill('green')
    telo.draw(window)
def draw_pytonchik():
    draw_face()
    draw_eye()
    draw_XBOCT()
    draw_telo()
    draw_textt()


draw_pytonchik()

window.getMouse()

window.close()