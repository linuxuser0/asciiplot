import math

def normal(std_dev, mean, x):
	return 1.0/(std_dev*math.sqrt(2.0*math.pi))*math.pow(math.e, -0.5*pow(x-mean, 2.0)/pow(std_dev, 2.0))

def plot_points(points, blank=" ", filled="x", width=30, height=50):
	xmin, xmax = min(point[0] for point in points), max(point[0] for point in points)
	ymin, ymax = min(point[1] for point in points), max(point[1] for point in points)
	scale = [width/(xmax-xmin), height/(ymax-ymin)]	
	xming, yming = scale[0]*xmax, scale[1]*ymax
	grid = [[blank for x in range(width+1)] for y in range(height+1)]

	#PS
	# -5, -5 - xmin, -ymin	

	for point in points:
		dx, dy = point[0] + xmin, point[1] + ymin 
		xgrid, ygrid = int(round(dx*scale[0])), int(round(dy*scale[1]))			
		grid[ygrid][xgrid] = filled
	grid.reverse()

	for row in grid:
		print "".join(row) 


def plot_eq(eq, start, end, step=1.0):
	points = []
	x = start
	while x <= end:
		points.append([float(x), float(eq(x))])
		x += step
	
	plot_points(points)

def parabola(x):
	return math.pow(x, 2)

plot_eq(parabola, -5, 5, 0.2)


