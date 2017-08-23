#! /usr/bin/python3

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

title_font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans-Bold.ttf",35)
playtime_font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSerif-BoldItalic.ttf",25)
desc_font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans.ttf",30)
flavor_font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSerif-Italic.ttf",20)
card_size = (750,1050)
white = (255,255,255)
black = (0,0,0)

def mkCard( card_title, card_playtime, card_desc, card_flavour ):
    img=Image.new("RGBA", card_size, white)
    draw = ImageDraw.Draw(img)
    draw.text((10, 0), card_title, black, font=title_font)
    draw.text((10, int( card_size[1] / 2 ) ), card_playtime, black, font=playtime_font)
    draw.text((30, int( card_size[1] * 2 / 3 )), card_desc, black, font=desc_font)
    draw.text((50, int( card_size[1] * 9 / 10 )), card_flavour, black, font=flavor_font)
    img.save( card_title + ".jpg" )
    #img.show()

def wrap_desc_txt( desc_txt ):
    txt_idx = 0
    mod_txt = list(desc_txt)
    while txt_idx < len( mod_txt ) - 45:
        for i in range( 45 ):
            if mod_txt[txt_idx + 45 - i] == ' ':
                mod_txt[txt_idx + 45 - i ] = '\n'
                txt_idx += 45 - i
                break
    return "".join(mod_txt)
    
def parse_line( txt ):
    title = txt.split( "  " )[0].title()
    playtime = txt.split( "=>" )[0][len(title):].strip().replace('"', '' )
    desc = txt.split( "=>" )[1].split( "==" )[0].strip()
    if "==" not in txt:
        flavor = ""
    else:
        flavor = txt.split( "==" )[1].strip().replace('"', '' )
    desc = wrap_desc_txt( desc )
    return title, playtime, desc, flavor

f = open( "card_ideas" )
cards = f.readlines()
for orig_txt in cards:
    #orig_txt = "catlady neighbour                \"Permenant\": Play anytime in Lead Generation Phase => Increase the dice roll required to sell by one - \"You will get used to her\""
    title, playtime, desc, flavor = parse_line( orig_txt )
    print( title )
    print( playtime )
    print( desc )
    print( flavor )
    mkCard( title, playtime, desc, flavor )
