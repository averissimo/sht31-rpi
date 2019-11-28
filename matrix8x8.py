import time

from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8

#
# Draw some shapes using the Python Imaging Library.
#
# Numbers and some letters
def draw(val, type = ''):
    def digit(d, x0 = 0, y0 = 0):
        options = {0: zero, 1: one, 2: two, 3: three,
                   4: four, 5: five, 6: six, 7: seven,
                   8: eight, 9: nine}
        options[d](x0, y0)

    def zero(x0,y0):
        draw.line((0+x0,0+y0,0+x0,4+y0), fill=255)
        draw.line((1+x0,0+y0,1+x0,4+y0), fill=255)

    def one(x0, y0):
        ## One
        draw.line((1+x0,0+y0,1+x0,4+y0), fill=255)

    def two(x0, y0):
        ## Two
        draw.line((0+x0,0+y0,1+x0,0+y0), fill=255)
        draw.line((1+x0,0+y0,1+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,0+x0,2+y0), fill=255)
        draw.line((0+x0,2+y0,0+x0,4+y0), fill=255)
        draw.line((0+x0,4+y0,1+x0,4+y0), fill=255)

    def three(x0, y0):
        ## Three
        draw.line((0+x0,0+y0,1+x0,0+y0), fill=255)
        draw.line((1+x0,0+y0,1+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,0+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,1+x0,4+y0), fill=255)
        draw.line((1+x0,4+y0,0+x0,4+y0), fill=255)

    def four(x0, y0):
        draw.line((0+x0,0+y0,0+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,1+x0,4+y0), fill=255)

    def five(x0, y0):
        draw.line((0+x0,0+y0,1+x0,0+y0), fill=255)
        draw.line((0+x0,0+y0,0+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,0+x0,2+y0), fill=255)
        draw.line((1+x0,2+y0,1+x0,4+y0), fill=255)
        draw.line((0+x0,4+y0,1+x0,4+y0), fill=255)

    def six(x0, y0):
        draw.line((0+x0,0+y0,0+x0,4+y0), fill=255)
        draw.line((1+x0,2+y0,1+x0,4+y0), fill=255)

    def seven(x0, y0):
        draw.line((0+x0,0+y0,1+x0,0+y0), fill=255)
        draw.line((1+x0,1+y0,1+x0,4+y0), fill=255)

    def eight(x0, y0):
        draw.line((0+x0,0+y0,1+x0,0+y0), fill=255)
        draw.line((0+x0,1+y0,1+x0,1+y0), fill=255)
        draw.line((0+x0,3+y0,1+x0,3+y0), fill=255)
        draw.line((0+x0,4+y0,1+x0,4+y0), fill=255)

    def nine(x0, y0):
        draw.line((1+x0,0+y0,1+x0,4+y0), fill=255)
        draw.line((0+x0,0+y0,0+x0,2+y0), fill=255)

    def negative(x0 = 0, y0 = 0):
        draw.line((0+x0,2+y0,1+x0,2+y0), fill=255)

    def error_letter(x0 = 0, y0 = 0):
        draw.line((0+x0,0+y0,2+x0,0+y0), fill=255)
        draw.line((0+x0,2+y0,1+x0,2+y0), fill=255)
        draw.line((0+x0,4+y0,1+x0,4+y0), fill=255)
        draw.line((0+x0,0+y0,0+x0,4+y0), fill=255)
        #
        draw.line((3+x0,2+y0,3+x0,4+y0), fill=255)
        draw.line((4+x0,2+y0,4+x0,2+y0), fill=255)
        #
        draw.line((6+x0,2+y0,6+x0,4+y0), fill=255)
        draw.line((7+x0,2+y0,7+x0,2+y0), fill=255)

    def h_letter(x0 = 0, y0 = 0):
        draw.line((0+x0,0+y0,0+x0,2+y0), fill=255)
        draw.line((0+x0,1+y0,2+x0,1+y0), fill=255)
        draw.line((2+x0,0+y0,2+x0,2+y0), fill=255)

    def t_letter(x0 = 0, y0 = 0):
        draw.line((0+x0,0+y0,2+x0,0+y0), fill=255)
        draw.line((1+x0,0+y0,1+x0,2+y0), fill=255)

    def getNum(val):
        isneg = 0
        if val < 0:
            isneg = 1
            val = abs(val)

        valstr = str(int(round(val)))

        if len(valstr) == 1:
            valstr = '0' + valstr

        if len(valstr) == 3 and isneg == 1:
            error_letter(0, 3)
        elif(len(valstr) == 3):
            digit(int(valstr[0]), 0, 3)
            digit(int(valstr[1]), 3, 3)
            digit(int(valstr[2]), 6, 3)
        elif(isneg == 1):
            negative(0,3)
            digit(int(valstr[0]), 3, 3)
            digit(int(valstr[1]), 6, 3)
        else:
            digit(int(valstr[0]), 3, 3)
            digit(int(valstr[1]), 6, 3)

    # Create display instance on default I2C address (0x70) and bus number.
    display = Matrix8x8.Matrix8x8()

    # Initialize the display. Must be called once before using the display.
    display.begin()

    # Clear the display buffer.
    display.clear()

    # First create an 8x8 1 bit color image.
    image = Image.new('1', (8, 8))

    # Then create a draw instance.
    draw = ImageDraw.Draw(image)
    if type == 'temp':
        t_letter()
        getNum(val)
    elif type == 'humd':
        h_letter()
        getNum(val)
    elif type == 'error':
        error_letter()

    # Draw the image on the display buffer.
    display.set_image(image)

    # Draw the buffer to the display hardware.
    display.write_display()
