def lines_with_at_least_nchars(text: str, n: int) -> list[str]:
    index: int = 0; text_length: int = len(text) - 1; result: list = []
    
    if not text_length: result.append(text)

    while text_length and index < text_length:
        amount: int = index + n
        line: str = text[index:amount]
        extract_last_remanent_word: bool = (amount + 1) < text_length and (' ' not in text[amount - 1:][:2])
        amount_to_extract: int = len(line.split(' ')[-1])
        
        result.append(line[:-amount_to_extract] if extract_last_remanent_word else line)
        index += (n - amount_to_extract) if extract_last_remanent_word else n
    
    return  result

def adjust_line_to_nchars(line: list[str], n: int, symbol: str = ' ') -> str:
    space_to_add: int = n - len(str.join('', line))
    line_length: int = len(line) - 1

    if line_length:
        for space_index in range(space_to_add):
            index = space_index % line_length
            line[index] = f'{line[index]}{symbol}'
    
    return str.join('', line)


if __name__ == '__main__':
    
    text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
    # text = 'La      historia       de la ópera tiene una duración         relativamente corta  '
    chars_per_line = 20
    symbol = ' ' # Simbolo para agregar entre cada palabra

    # Elimina espacios duplicados entre palabras
    cls_extra_spaces: list[str] = lambda text: list(filter(len, text.split(' ')))
    
    lines = cls_extra_spaces(text)
    # El minimo valor al que se puede ajustar es la longitud de la palabra maxima
    chars_per_line = max(max(map(len, lines)), chars_per_line)

    lines: list[str] = lines_with_at_least_nchars(str.join(' ', lines), chars_per_line)
    lines: list[str] = list(map(lambda l: adjust_line_to_nchars(cls_extra_spaces(l), chars_per_line, symbol), lines))

    list(map(print, lines))