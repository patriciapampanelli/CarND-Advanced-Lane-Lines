def plot_images(images, color_map = None, columns = 5, scale = 1):
	#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow	
	#https://matplotlib.org/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap 	
	import matplotlib.pyplot as plt
	
	plt.figure(figsize=(scale*20,scale*10))
	for i, image in enumerate(images):
		plt.subplot(len(images) / columns + 1, columns, i + 1)
		plt.imshow(image, color_map)
	
	