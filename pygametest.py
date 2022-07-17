# import pygame module in this program
import pygame
import pygame.freetype
import textwrap
from globals import *

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
# create the display surface object
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = None
clock = pygame.time.Clock()


# set the pygame window name
pygame.display.set_caption('Texticular')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
#font = pygame.font.Font('C:\Windows\Fonts\segoeui.ttf', 16)
font = pygame.font.SysFont('Sans', 24)
ft_font = pygame.freetype.SysFont('Sans', 24)



fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)

# create a text surface object,
# on which text is drawn on it.
text_to_render = (
"As you look around the hotel room you see an old TV with rabbit ears that looks like "
"it came straight out of the 1950's. Against the wall there is a beat up night stand "
"with a little drawer built in to it and an old phone on top. Next to it is a lumpy old "
"bed that looks like it's seen better days, with a dark brown stain on the sheets and "
"a funny smell coming from it. There is an obnoxious orange couch in the corner next to "
"a small window smudged with sticky purple hand prints. The stuffing is coming out of "
"the cushions which are also spotted with purple, and the floor is covered with empyt cans "
"of Fast Eddie's Colon Cleanse."
)

def display_text(text_to_render):
    output = textwrap.wrap(text_to_render,100)
    start_x = 20
    start_y = 20
    for line in output:
        """
        text = font.render(line, True,(100, 200, 255))
        screen.blit(text, (start_x, start_y))
        """


        text_str = line
        text_rect = ft_font.get_rect(text_str)
        text_rect.center = screen.get_rect().center
        ft_font.render_to(screen, (start_x, start_y), text_str, (100, 200, 255))

        start_y += 30

def get_input():
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(20, 950, 800, 35)


    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    pygame.draw.rect(screen, color, input_rect)
    text_surface = font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()


# infinite loop
while True:

    # completely fill the surface object
    # with white color
    screen.fill(BLACK)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        display_text(text_to_render)
        get_input()
        pygame.display.update()
    clock.tick(30)