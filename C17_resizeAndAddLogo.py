"""
At a high level, here’s what the program
should do:
• Load the logo image.
• Loop over all .png and.jpg files in the working directory.
• Check whether the image is wider or taller than 300 pixels.
• If so, reduce the width or height (whichever is larger) to 300 pixels and
scale down the other dimension proportionally.
• Paste the logo image into the corner.
• Save the altered images to another folder.

"""

# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
os.chdir('.\\files')
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % filename)
        im = im.resize((width, height))

        # Add the logo.
        print('Adding logo to %s' % filename)
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # Save changes
        im.save(os.path.join('withLogo', filename))

