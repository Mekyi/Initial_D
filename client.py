import pygame
from socket import *
from pygame.locals import *

HOST = '10.0.0.184'  # 10.0.0.184
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# Define some colors
FONT_COLOR = (255,   0,   0)
WHITE = (255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, FONT_COLOR)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/Gas gas gas.mp3')
    pygame.mixer.music.play(-1)

def forward():
	print ('forward')
	tcpCliSock.send('forward'.encode())

def backward():
	print ('backward')
	tcpCliSock.send('backward'.encode())

def left():
	print ('left')
	tcpCliSock.send('left'.encode())

def right():
	print ('right')
	tcpCliSock.send('right'.encode())

def stop():
	print ('stop')
	tcpCliSock.send('stop'.encode())

def home():
	print ('home')
	tcpCliSock.send('home'.encode())

def quit():
	top.quit()
	tcpCliSock.send('quit')
	tcpCliSock.close()

def keyboardInput():
    if event.type == KEYDOWN:
        if event.key in (K_UP, K_w):
            forward()
        elif event.key in (K_DOWN, K_s):
            backward()
        elif event.key in (K_LEFT, K_a):
            left()
        elif event.key in (K_RIGHT, K_d):
            right()
    elif event.type == KEYUP:
        if event.key in (K_LEFT, K_a) or event.key in (K_RIGHT, K_d):
            home()
        elif event.key in (K_UP, K_w) or event.key in (K_DOWN, K_s):
            stop()

# Sprites
def nuoliyy(x,y):
    screen.blit(yynuoli, (x,y))

def nuoliay(x,y):
    screen.blit(aynuoli, (x,y))

def nuolivy(x,y):
    screen.blit(vynuoli, (x,y))

def nuolioy(x,y):
    screen.blit(oynuoli, (x,y))

def nuoliyp(x,y):
    screen.blit(ypnuoli, (x,y))

def nuoliap(x,y):
    screen.blit(apnuoli, (x,y))

def nuolivp(x,y):
    screen.blit(vpnuoli, (x,y))

def nuoliop(x,y):
    screen.blit(opnuoli, (x,y))

def tausta(x,y):
    screen.blit(tausta, (x,y))

pygame.init()

playMusic()

# Screen size
size = [900, 507]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Project: Initial D")

#Loop until the user clicks the close button.
done = False

# Initialize images
yynuoli = pygame.image.load('images/nuoli_y_y.png')
aynuoli = pygame.image.load('images/nuoli_a_y.png')
vynuoli = pygame.image.load('images/nuoli_v_y.png')
oynuoli = pygame.image.load('images/nuoli_o_y.png')
ypnuoli = pygame.image.load('images/nuoli_y_p.png')
apnuoli = pygame.image.load('images/nuoli_a_p.png')
vpnuoli = pygame.image.load('images/nuoli_v_p.png')
opnuoli = pygame.image.load('images/nuoli_o_p.png')
tausta = pygame.image.load('images/Initial_D.png')
BackGround = Background('images/Initial_D.png', [0,0])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Initialize server connection
tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done == False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

        # Keyboard input
        #keyboardInput()

    # DRAWING STEP
    # First, clear the screen to white.  Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill([255,255,255])
    screen.blit(BackGround.image, BackGround.rect)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick

        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.

        #axes = joystick.get_numaxes()
        #textPrint.print(screen, "Number of axes: {}".format(axes))
        #textPrint.indent()
        #for i in range(axes):
        #    axis = joystick.get_axis(i)
        #    textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        #textPrint.unindent()

        #buttons = joystick.get_numbuttons()
        #textPrint.print(screen, "Number of buttons: {}".format(buttons))
        #textPrint.indent()

        #for i in range(buttons):
        #    button = joystick.get_button(i)
        #    textPrint.print(screen, "Button {:>2} value: {}".format(i,button))
        #textPrint.unindent()

        # Hat switch.  All or nothing for direction, not like joysticks.
        # Value comes back in an array.

        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()
        textPrint.print(screen, "")
        textPrint.print(screen, "Now playing: Runnin in the 90s")

        #Draw direction sprites
        nuoliyp(200,300)
        nuoliap(200,400)
        nuolivp(150,350)
        nuoliop(250,350)

        for i in range(hats):
            hat = str(joystick.get_hat(i))
            textPrint.print(screen, "Hat {} value: {}".format(i, hat))
            if (hat == '(0, 1)'):
                nuoliyy(200,300)
                forward()
            elif (hat == '(0, -1)'):
                nuoliay(200,400)
                backward()
            elif (hat == '(0, 0)'):
                stop()
            elif (hat == '(-1, 0)'):
                nuolivy(150,350)
                left()
            elif (hat == '(1, 0)'):
                nuolioy(250,350)
                right()
        textPrint.unindent()
        textPrint.unindent()
        textPrint.unindent()

        textPrint.print(screen, "")
        textPrint.print(screen, "Now playing: Gas Gas Gas")

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit()
