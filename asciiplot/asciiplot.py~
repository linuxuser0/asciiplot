import math

def plot_points(points, xmin=-10, xmax=10, ymin=-10, ymax=10, xscale=5, yscale=5, width=150, height=40, blank=" ", filled="x", pointlist=False, axis=True):
	scale = [width/(xmax-xmin), height/(ymax-ymin)]	
	xming, yming = scale[0]*xmax, scale[1]*ymax
	grid = [[blank for x in range(width+1)] for y in range(height+1)]
	
	if ymin < 0 and  ymax > 0:
		for x in range(0, len(grid[0])):
			if x % xscale == 0:
				grid[int(round(-ymin*scale[1]))][x] = "+"
			else:
				grid[int(round(-ymin*scale[1]))][x] = "-"
			
			

	if xmin < 0 and xmax > 0:
		for y in range(0, len(grid)):
			if y % yscale == 0:
				grid[y][int(round(-xmin*scale[0]))] = "+"
			else:
				grid[y][int(round(-xmin*scale[0]))] = "|"
		
	print "\n"
	for point in points:
		if pointlist:
			print point[0], point[1]
		newx, newy = point[0] - xmin, point[1] - ymin # shift over 
		xgrid, ygrid = int(round(newx*scale[0])), int(round(newy*scale[1])) # and scale!			
		if 0 <= xgrid and xgrid <= width and 0 <= ygrid and ygrid <= height:
			grid[ygrid][xgrid] = filled

	grid.reverse()
	for row in grid:
		print "".join(row) 


def plot_eq(eq, xmin=-10, xmax=10, ymin=-10, ymax=10, step=0.01, xscale=5, yscale=5, width=150, height=40, blank=" ", filled="x", pointlist=False, axis=True):
	points = []		
	x = xmin
	while x <= xmax:
		points.append([float(x), float(eq(x))])
		x += step

	plot_points(points, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, xscale=xscale, yscale=yscale, width=width, height=height, blank=blank, filled=filled, pointlist=pointlist, axis=axis)


