import math

def normal(std_dev, mean, x):
	return 1.0/(std_dev*math.sqrt(2.0*math.pi))*math.pow(math.e, -0.5*pow(x-mean, 2.0)/pow(std_dev, 2.0))

def plot_points(points, blank=" ", filled="x", size="medium"):
	xmin, xmax = min(point[0] for point in points), max(point[0] for point in points)
	ymin, ymax = min(point[1] for point in points), max(point[1] for point in points)
	grid = [[blank for x in range(xmax-xmin+1)] for y in range(ymax-ymin+1)]

	for point in points:
		grid[point[1]][point[0]] = filled

	grid.reverse()
	
	for row in grid: #make y go down
		print "".join(row) 
		

def plot_eq(eq, start, end, step=1):
	points = []
	for x in range(start, end+1, step):
		points.append([x, eq(x)])
	
	print points	
	plot_points(points)

def parabola(x):
	return int(math.pow(x, 2))

plot_eq(parabola, 0, 5)


