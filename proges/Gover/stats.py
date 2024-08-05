import yaml
import config


def get():
	with open(config.ARTISTS_STATS, 'r') as artists_file:
		return yaml.load(
			artists_file,
			Loader=yaml.FullLoader
		)

def save(music):
	if old_artists:= get():
		artists = old_artists

	else:
		artists = {}

	if music['artist'] in artists.keys():
		artists[music['artist']] += 1

	else:
		artists[music['artist']] = 1

	with open(config.ARTISTS_STATS, 'w') as artists_file:
		yaml.dump(artists, artists_file)
