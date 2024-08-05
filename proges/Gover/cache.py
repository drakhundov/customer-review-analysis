import csv
import config

import stats


__cache = None


def __init__():
	global __cache

	with open(config.CACHE_FILE) as cache_file:
		reader = csv.DictReader(
					cache_file,
					delimiter=config.DELIMITER
				 )

		__cache = list(reader)


def __save_new_music(music):
	with open(config.CACHE_FILE, 'a+') as cache_file:
		writer = csv.DictWriter(
					cache_file,
					fieldnames=config.FIELDNAMES,
					delimiter=config.DELIMITER
				 )

		writer.writerow(music)


def get():
	global __cache

	return __cache.copy()


def add(**music):
	global __cache

	stats.save(music)

	if music.get('check_copy') and music['title'] in [music['title'] for music in __cache]:
		return

	__cache.append(
		{
			'title': music['title'],
			'artist': music['artist'],
			'album': music['album'],
			'path': music['path']
		}
	)

	__save_new_music(__cache[-1])


__init__()
