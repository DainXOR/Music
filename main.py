import os
from tkinter.font import names

import eyed3

import utils
from preprocessing import MusicProcessor
from utils import is_duplicate, is_copy, has_ext

# Paths
mainPath = "./files"

# zipPath = f"{mainPath}/zips"

allPath = f"{mainPath}/all"
testPath = f"{mainPath}/test"

usedPath = testPath

t = MusicProcessor()
t.load_music(usedPath)
t.sanitize(predicate = utils.has_ext, mutator = utils.remove_ext)
t.search_duplicates()
t.delete_duplicate(names = True)
t.process_duplicates()

results: dict[str, list] = t.result().duplicates().not_exact_duplicates().get()

print()
for key, val in results.items():
    print(key)
    print(val)
    print()

