def is_duplicate(name) -> bool:
  return name.endswith('(2)')

def is_copy(name) -> bool:
  return name.endswith(' - copia')

def has_ext(filename) -> bool:
    return '.' in filename

def remove_ext(filename) -> str:
  return ".".join(filename.split('.')[:-1])

def remove_2(name) -> str:
  name = name[:-3]

  while name[-1] == ' ':
    name = name[:-1]

  return name