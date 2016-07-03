#from PIL import Image
import pytesseract
from PIL import Image
image_file = 'dailypledges-5.png'
im = Image.open(image_file)
#text = pytesseract.image_to_string(im)
#text = image_file_to_string(image_file)
#text = image_file_to_string(image_file, graceful_errors=True)
#print "=====output=======\n"
#print text
text = pytesseract.image_to_string(im)
print text
