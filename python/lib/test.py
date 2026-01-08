import time
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V2

def main():
    # 1. Instanciation et init
    epd = epd2in13_V2.EPD()    # pas d'arguments
    epd.init()
    epd.Clear()                # efface l'écran

    # 2. Création de l'image PIL (mode 1‑bit, fond blanc)
    width, height = epd.width, epd.height
    image = Image.new('1', (width, height), 255)
    draw  = ImageDraw.Draw(image)

    # 3. Texte centré
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
    text = "Bonjour  !" 
    w, h = draw.textsize(text, font=font)
    x = (width  - w) // 2
    y = (height - h) // 2
    draw.text((x, y), text, font=font, fill=0)

    # 4. Envoi à l'écran
    epd.display(epd.getbuffer(image))
    time.sleep(1)

    # 5. Mise en veille
    epd.sleep()

if __name__ == '__main__':
    main()
