'''
Created on 2015-1-25

@author: duke
'''

# Import the modules
from PIL import Image, ImageDraw, ImageFont

def draw_text(file_name, fill_color_circle, fill_color_text, font_name, text=""):
    try:
        #open image
        image = Image.open(file_name)
        x, y = image.size
        draw = ImageDraw.Draw(image)
        #set font
        font = ImageFont.truetype(font_name, 20)
        #Size of Bounding Box for ellipse
        eX, eY = 80, 80 
        ebox =  (x- eX/2, 0, x, eY/2)
        draw = ImageDraw.Draw(image)
        draw.ellipse(ebox, fill_color_circle)
        draw.text((x- 0.32 * eX, 10), text, fill_color_text, font=font)
        del draw
        image.save("test_result.jpg")
    
    except:
        print "Unable to load image"
        
if __name__ == "__main__":
    
    file_name = "test.jpg"
    text = str(5)
    fill_color_circle = (211,26,30)
    fill_color_text = (255, 255, 255)
    font_name = "Arial.ttf"
    
    draw_text(file_name, fill_color_circle, fill_color_text, font_name, text)