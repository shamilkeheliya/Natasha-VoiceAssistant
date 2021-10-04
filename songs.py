import os
import editables
import random


def play_song():
    music = os.listdir(editables.songs)
    no = random.randint(0, editables.songs_count - 1)
    os.startfile(os.path.join(editables.songs, music[no]))


def play_english_song():
    music = os.listdir(editables.english_songs)
    no = random.randint(0, editables.english_songs_count - 1)
    os.startfile(os.path.join(editables.english_songs, music[no]))


def play_sinhala_song():
    music = os.listdir(editables.sinhala_songs)
    no = random.randint(0, editables.sinhala_songs_count - 1)
    os.startfile(os.path.join(editables.sinhala_songs, music[no]))