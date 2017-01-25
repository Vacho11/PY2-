import os 
import glob 
import subprocess 
from multiprocessing import pool  

Source_directory = 'Source'
result = 'Result'

Images = glob.glob(os.path.join(Source_directory, "*.jpg"))

def redacting_image(filename):
	if (os.path.exists(Result)):
		print("The file already exists")
	else:
		os.mkdir(Result)
	subprocess.run(['convert', filename, '-resize', '200',])

for f in Images:
	subprocess.run(['cp', f, Result])

Finished_images = glob.glob(os.path.join(Result, "*.jpg"))

pool = Pool(4)
pool.map(redacting_image, Finished_images)
pool.close()
pool.join()