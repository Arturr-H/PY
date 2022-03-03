import PIL;
from PIL import Image;

## The desired configuratons
## of the image output.
desired = {
	"density": 50,
	"ascii": ["#", "$", "@", "*", "+", "=", "-", ":", ",", "."],
};

asciiCharactersLength = len(desired["ascii"]);

## Replace this your the image's path
image = Image.open("/Users/artur/Desktop/img.png");
image = image.convert("RGB");

## Width and height for
## looping through pixels.
width, height = image.size;

## Load all rgb values from image
imagePixels = image.load();

## Brightness of all pixels which will
## be converted into ascii characters.
def getBrightness(rgb):
	r, g, b = rgb[0:3];

	## Average light level
	return int((r + b + g) / 3);

def getAsciiChar(brightness):

	## Get the index of what ascii
	## character that "matches" the brightness.
	charIndex = int(( brightness / 255 ) * asciiCharactersLength)

	return desired["ascii"][min(charIndex, asciiCharactersLength-1)];


## Output image as an array
imageArray = [];

## Loop through all pixels
for h in range(int( height / desired["density"] )):

	imageArray.append([]);

	for w in range(int( width / desired["density"] )):

		x, y = (w * desired["density"], h * desired["density"])
		
		## Current pixel's rgb values
		currentPixel = image.getpixel((x, y));

		## Brightness of the pixel from 0 - 255
		brightness = getBrightness(currentPixel);

		imageArray[h].append(
			getAsciiChar(brightness)
		);


def prettyPrint(map):

	outputW = int(width / desired["density"]);
	outputH = int(height / desired["density"]);

	for h in range(outputH):
		for w in range(outputH):
			print(imageArray[h][w], end=" ");

		print("");


prettyPrint(imageArray);




