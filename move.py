import os
import sys
import shutil

def move(mime, src, dest):
	os.system('clear')
	if not os.path.exists(src):
		print('Source directory does not exist !')
		print()
		return
	if not os.path.exists(dest):
		print('Creating destination directory...')
		print()
		os.makedirs(dest)
	for root, dirs, files in os.walk(src):
		for file in files:
			if root != dest:
				if file.endswith(mime):
					path = os.path.join(root,file)
					print('Moving ' + path + '...')
					shutil.move(path, dest)
	print()
	print('ALL DONE!')
	print()

if __name__ == '__main__':
	move(*sys.argv[1:])