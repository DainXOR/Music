import os

import utils
import eyed3

class MusicProcessor:

    def __init__(self):
        self._path: str = "./"
        self._music: list[str] = []
        self._remove_duplicate_files = False
        self._remove_duplicate_names = False

        self._possible_duplicates: list[str] = []
        self._duplicates: list[str] = []
        self._not_exact_duplicates: list[str] = []

        self._return_result = False
        self._return_duplicates = False
        self._return_not_exact_duplicates = False

    def load_music(self, from_dir: str):
        self._path = from_dir
        self._music = os.listdir(self._path)

        print(len(self._music), self._music)

        return self

    def set_music(self, music: list):
        self._music = music

        print(len(self._music), self._music)

        return self

    def sanitize(self, *, predicate, mutator):
        newNames: list[str] = []

        for name in self._music:
            if predicate(name):
                name = mutator(name)

            newNames.append(name)

        self._music = newNames

        print(len(self._music), self._music)

        return

    def search_duplicates(self, *, predicate = utils.is_duplicate, mutator = lambda n: n):
        self._possible_duplicates = []

        for name in self._music:
            if predicate(name):
                name = mutator(name)
                self._possible_duplicates.append(name)

        print("Possible duplicates: ", len(self._possible_duplicates))
        print(self._possible_duplicates)
        return self

    def delete_duplicate(self, *, files: bool = False, names: bool = False):
        self._remove_duplicate_files = files
        self._remove_duplicate_names = names

        return self

    def process_duplicates(self):
        self._duplicates = []

        for name in self._possible_duplicates:
          try:
            audio_file = eyed3.load(f"{self._path}/{name}.mp3")
            original_file = eyed3.load(f"{self._path}/{utils.remove_2(name)}.mp3")

            if audio_file.info == original_file.info:
              self._duplicates.append(f"{name}")
            else:
              self._not_exact_duplicates.append(f"{name}")

          except:
            print(f"Error with {utils.remove_2(name)}")

        print(len(self._possible_duplicates) - len(self._duplicates))

        print(self._possible_duplicates)
        print(self._duplicates)

        if self._remove_duplicate_files or self._remove_duplicate_names:
            for song in self._duplicates:
                if self._remove_duplicate_files:
                    os.remove(f"{self._path}/{song}")

                if self._remove_duplicate_names:
                    self._music.remove(song)

        return self

    def result(self):
        self._return_result = True

        return self

    def duplicates(self):
        self._return_duplicates = True

        return self

    def not_exact_duplicates(self):
        self._return_not_exact_duplicates = True

        return self

    def get(self) -> dict[str, list]:
        result = {}

        if self._return_result:
            result["result"] = self._music

        if self._return_duplicates:
            result["duplicates"] = self._duplicates

        if self._return_not_exact_duplicates:
            result["not_exact_duplicates"] = self._not_exact_duplicates

        return result