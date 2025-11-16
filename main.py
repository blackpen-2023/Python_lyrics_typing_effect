import time
import threading
import simpleaudio as sa

class lyrics_typing:
    def __init__(self, BPM_IN=120, LYRICS_PATH='lyrics.txt', MUSIC_PATH='test.wav'):
        self.BPM = BPM_IN
        self.beat_sec = 60 / self.BPM
        self.char_per_beat = 3
        self.delay = self.beat_sec / self.char_per_beat  
        self.lyrics_file = LYRICS_PATH
        self.music_file = MUSIC_PATH

    def read_file(self):
        with open(self.lyrics_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    
    def typing(self, lyrics):
        print(lyrics)
        print('-' * 10)

        for line in lyrics:
            for ch in line:
                print(ch, end='', flush=True)
                time.sleep(self.delay)

    def play_sound(self):
        wave_obj = sa.WaveObject.from_wave_file(self.music_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()


model = lyrics_typing(93, 'lyrics.txt', 'test.wav')

lyrics = model.read_file()
model.play_sound()
typing_thread = threading.Thread(target=model.typing, args=(lyrics,))
typing_thread.start()
model.play_sound()

typing_thread.join()
