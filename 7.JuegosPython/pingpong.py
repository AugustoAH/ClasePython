import turtle
import random

# ─── Configuración de la ventana ────────────────────────────────────────────
ventana = turtle.Screen()
ventana.title("Ping Pong - Jugador vs Máquina")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# ─── Paleta del jugador (izquierda) ─────────────────────────────────────────
jugador = turtle.Turtle()
jugador.speed(0)
jugador.shape("square")
jugador.color("cyan")
jugador.shapesize(stretch_wid=5, stretch_len=1)
jugador.penup()
jugador.goto(-350, 0)

# ─── Paleta de la máquina (derecha) ─────────────────────────────────────────
maquina = turtle.Turtle()
maquina.speed(0)
maquina.shape("square")
maquina.color("red")
maquina.shapesize(stretch_wid=5, stretch_len=1)
maquina.penup()
maquina.goto(350, 0)

# ─── Pelota ─────────────────────────────────────────────────────────────────
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)

VELOCIDAD_INICIAL = 2
pelota.dx = VELOCIDAD_INICIAL * random.choice([-1, 1])
pelota.dy = VELOCIDAD_INICIAL * random.choice([-1, 1])

# ─── Marcador ───────────────────────────────────────────────────────────────
puntaje_jugador = 0
puntaje_maquina = 0

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write(f"Jugador: {puntaje_jugador}   Máquina: {puntaje_maquina}",
               align="center", font=("Courier", 20, "bold"))

# ─── Línea central ──────────────────────────────────────────────────────────
linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.penup()
linea.goto(0, 280)
linea.pendown()
linea.setheading(270)
for _ in range(14):
    linea.forward(20)
    linea.penup()
    linea.forward(20)
    linea.pendown()
linea.hideturtle()

# ─── Mensaje de ayuda ────────────────────────────────────────────────────────
ayuda = turtle.Turtle()
ayuda.speed(0)
ayuda.color("gray")
ayuda.penup()
ayuda.hideturtle()
ayuda.goto(0, -270)
ayuda.write("W / S  o  ↑ / ↓  para mover tu paleta",
            align="center", font=("Courier", 12, "normal"))

# ─── Movimiento del jugador ──────────────────────────────────────────────────
VELOCIDAD_PALETA = 20

def jugador_arriba():
    y = jugador.ycor()
    if y < 250:
        jugador.sety(y + VELOCIDAD_PALETA)

def jugador_abajo():
    y = jugador.ycor()
    if y > -250:
        jugador.sety(y - VELOCIDAD_PALETA)

ventana.listen()
ventana.onkeypress(jugador_arriba, "w")
ventana.onkeypress(jugador_abajo, "s")
ventana.onkeypress(jugador_arriba, "Up")
ventana.onkeypress(jugador_abajo, "Down")

# ─── Actualizar marcador ─────────────────────────────────────────────────────
def actualizar_marcador():
    marcador.clear()
    marcador.write(f"Jugador: {puntaje_jugador}   Máquina: {puntaje_maquina}",
                   align="center", font=("Courier", 20, "bold"))

# ─── Reiniciar pelota ────────────────────────────────────────────────────────
def reiniciar_pelota():
    pelota.goto(0, 0)
    pelota.dx = VELOCIDAD_INICIAL * random.choice([-1, 1])
    pelota.dy = VELOCIDAD_INICIAL * random.choice([-1, 1])

# ─── Bucle principal del juego ───────────────────────────────────────────────
VELOCIDAD_IA = 20       # qué tan bien sigue la pelota la máquina (1-10)
MAX_VELOCIDAD = 20   # velocidad máxima de la pelota

while True:
    ventana.update()

    # Mover pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebotar en paredes superior e inferior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Pelota sale por la derecha → punto para el jugador
    if pelota.xcor() > 390:
        puntaje_jugador += 1
        actualizar_marcador()
        reiniciar_pelota()

    # Pelota sale por la izquierda → punto para la máquina
    if pelota.xcor() < -390:
        puntaje_maquina += 1
        actualizar_marcador()
        reiniciar_pelota()

    # Colisión con paleta del jugador
    if (-340 < pelota.xcor() < -330 and
            jugador.ycor() - 50 < pelota.ycor() < jugador.ycor() + 50):
        pelota.setx(-330)
        pelota.dx = abs(pelota.dx) * 1.05   # acelera un poco
        if abs(pelota.dx) > MAX_VELOCIDAD:
            pelota.dx = MAX_VELOCIDAD

    # Colisión con paleta de la máquina
    if (330 < pelota.xcor() < 340 and
            maquina.ycor() - 50 < pelota.ycor() < maquina.ycor() + 50):
        pelota.setx(330)
        pelota.dx = -abs(pelota.dx) * 1.05  # acelera un poco
        if abs(pelota.dx) > MAX_VELOCIDAD:
            pelota.dx = -MAX_VELOCIDAD

    # IA de la máquina: sigue la pelota con velocidad limitada
    if maquina.ycor() < pelota.ycor() - 5:
        maquina.sety(maquina.ycor() + VELOCIDAD_IA)
    elif maquina.ycor() > pelota.ycor() + 5:
        maquina.sety(maquina.ycor() - VELOCIDAD_IA)

    # Limitar paletas dentro de la pantalla
    if maquina.ycor() > 250:
        maquina.sety(250)
    if maquina.ycor() < -250:
        maquina.sety(-250)
