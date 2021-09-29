"""
    turtle_square.py
    Demostració de l'ús de Turtle dibuixant un quadrat
"""

import turtle               # avisem a Python que volem fer servir el mòdul turtle
tortuga = turtle.Pen()      # creem la tortuga
tortuga.color('blue')       # canviem el color de la tortuga a blau
tortuga.forward(100)        # la fem avançar 100 passes (pixels)
tortuga.left(90)            # la fem girar 90 graus a l'esquerra
tortuga.color('red')
tortuga.forward(100)
tortuga.left(90)
tortuga.color('blue')
tortuga.forward(100)
tortuga.left(90)
tortuga.color('red')
tortuga.forward(100)
tortuga.left(135)
tortuga.color('green')
tortuga.forward(145)
input()                     # es manté la finestra amb el dibuix fins enter