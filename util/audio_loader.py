import simpleaudio as sa

def load_audio(audio_path=None):
	try:
		audio = sa.WaveObject.from_wave_file(audio_path)
	except Exception as e:
		print('error loading audio sample', e)

	return audio