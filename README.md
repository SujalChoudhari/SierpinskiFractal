# SierpinskiFractal

This is a simple program that draws a Sierpinski Fractal using Pillow and Python.

Run the program with `python3 main.py` and it will generate a fracta.

## Working
* First 3 points are generated to be an isosceles triangle. (Any triangle will work)
* A random point is generated inside the triangle.
* The midpoint of the random point and the previous point is calculated.
* The midpoint is drawn.
* The midpoint is set as the new random point.
* The process is repeated until the desired number of points are drawn.

## Output
![Sierpinski Fractal](https://github.com/SujalChoudhari/SierpinskiFractal/blob/main/output.png?raw=true)