#!/usr/bin/python3
import platform
import subprocess

import sys

from setuptools import setup, find_packages

platform = platform.system()


if platform == 'Linux':
	subprocess.run(
		[
			'sudo apt update &',
			'sudo apt upgrade -y &',
			'sudo apt-get install mpg123 &',
			'sudo apt-get install vorbis-tools'
		]
	)


if '--python' in sys.argv:
	setup(
		name='gover',
		version='1.0',
		description='Music Player',
		author='Abdul Akhundzade',
		license='MIT',
		packages=find_packages(),
		include_package_data=True
	)
