#!/usr/bin/python3
import pyform
import config

import sys
import time

import music

# import matplotlib.pyplot as plt
# waves

import cache
import stats

import computer

class Gover(pyform.Form):
	def start(self):
		# TODO: Run Favourite Music Of User
		music.new(cache.get()[-1]['path'])

		self.title = pyform.widgets.Label(
			self.form,
			music.info['title']
		).place(20, 0)

		self.artist = pyform.widgets.Label(
			self.form,
			music.info['artist']
		).place(20, 50)

		self.album = pyform.widgets.Label(
			self.form,
			music.info['album']
		).place(20, 100)

	def end(self):
		music.player.kill()

		computer.restore_terminal_settings()

		sys.exit()


pyform.add(Gover, 'main', 'settings.json')
pyform.run('main')

pyform.mainloop()
