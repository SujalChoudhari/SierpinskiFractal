from PIL import Image, ImageDraw
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2)

WIDTH, HEIGHT = 1000, 1000

# Create 3 points to make an equilateral triangle, based on the width and height and have some padding
POINTS = [
    Point(WIDTH/2, 0 + 20),
    Point(WIDTH - 20, HEIGHT - 20),
    Point(0 + 20, HEIGHT - 20)
]


# Plot points 
def plot_points(drawable,iteration):
    randomPoint = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    for i in range(iteration):
        # plot the random point
        drawable.point((randomPoint.x, randomPoint.y), fill=(0,0,0))

        randomPoint = POINTS[random.randint(0, 2)].midpoint(randomPoint)

if __name__ == '__main__':

    # Create a new imageṇ
    im = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
    drawable = ImageDraw.Draw(im)

    plot_points(drawable, 1000000)

    # Save the image
    im.save('output.png')
    im.show()
