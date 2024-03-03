def text_aligner(txt: str, n: int, symbol: str = ' ') -> list[str]:
    cls: list[str] = lambda t: [c for c in t.split(' ') if c] # Quita espacios duplicados entre palabras
    
    lines = cls(txt)
    txt = str.join(' ', lines)
    n = max(max(map(len, lines)), n) # n no sera mas chico que la longitud de la palabra mas larga
    
    i: int = 0; txt_len: int = len(txt) - 1; res: list = []
    
    if not txt_len: res.append(txt)

    while txt_len and i < txt_len:
        chunk: str = txt[i:i + n]
        do_extract: bool = (i + n + 1) < txt_len and not any(map(str.isspace, txt[i + n - 1:][:2]))
        to_extract: int = len(chunk.split(' ')[-1])
        
        line: list[str] = cls(chunk[:-to_extract] if do_extract else chunk)
        if len(line) - 1:
            for s in range(n - len(str.join('', line))):
                line[s % (len(line) - 1)] = f'{line[s % (len(line) - 1)]}{symbol}'
        
        res.append(str.join('', line))

        i += (n - to_extract) if do_extract else n
    
    return  res


if __name__ == '__main__':
    
    txt = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
    # text = 'La      historia       de la ópera tiene una duración         relativamente corta  '
    chars = 25
    symbol = '.' # Simbolo para agregar entre cada palabra

    list(map(print, text_aligner(txt, chars, symbol)))