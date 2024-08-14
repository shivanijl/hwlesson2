import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

#BLUE = 0, 128, 255
GRAVITY = 2000.0  # pixels per second per second

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


ball = Ball(50, 100)
ball1 = Ball(30 , 150)
ball2 = Ball(70 , 50)


def draw():
    screen.clear()
    ball.draw()

def update(dt):
    # Apply constant acceleration formulae
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt

    ball2.vy += GRAVITY * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt

    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius:  # we've bounced!
        ball.y = HEIGHT - ball.radius  # fix the position
        ball.vy = -ball.vy * 0.9  # inelastic collision

    if ball1.y > HEIGHT - ball1.radius:  # we've bounced!
        ball1.y = HEIGHT - ball1.radius  # fix the position
        ball1.vy = -ball1.vy * 0.9  # inelastic collision

    if ball2.y > HEIGHT - ball2.radius:  # we've bounced!
        ball2.y = HEIGHT - ball2.radius  # fix the position
        ball2.vy = -ball2.vy * 0.9  # inelastic collision



    # X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx

    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx


def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()