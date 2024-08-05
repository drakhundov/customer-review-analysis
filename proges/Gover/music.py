import subprocess
import eyed3

import os

import cache

player = None
info = None


def __get__info(path, save_cache=False):
	path = os.path.join(os.getcwd(), path)

	for music in cache.get():
		if music['path'] == path:
			return music

	music = eyed3.load(path)

	info = {
		'title': music.tag.title,
		'artist': music.tag.artist,
		'album': music.tag.album,
		'path': path
	}

	if save_cache:
		cache.add(
			**info, 
			check_copy=False
		)

	return info


def new(path):
	global player
	global info

	if not os.path.exists(path):
		return

	info = __get__info(
		path, 
		save_cache=True
	)

	extension = os.path.splitext(path)[1]

	if extension == '.mp3':
		music_player = 'mpg123'

	elif extension == '.ogg':
		music_player = 'ogg123'

	player = subprocess.Popen(
		[
		  music_player,
		  path
		]
	)
