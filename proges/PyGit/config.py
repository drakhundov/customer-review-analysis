import os
import platform

GIT = 'https://github.com/akhundzade-abdul/{0}.git'

platform = platform.system()

if platform == 'Linux':
	MAIN = os.path.join(
			os.environ['HOME'],
			'Documents',
			'code'
		)

elif platform == 'Windows':
	MAIN = f'C:\\Users\\{os.getlogin()}\\GoogleDrive\\Code'
