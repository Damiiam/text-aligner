def split_text_into_lines(text, number):
    results, line = [], []
    words = text.split(' ')

    for w in words:
        line.append(w)
        words_count = len(''.join(line)) + len(line)

        # Si la cantidad de letras es mayor al numero 
        # solicitado se crea una nueva linea
        if words_count > number:
            last_word = line.pop(-1)
            results.append(line)
            line = []
            line.append(last_word)
    
    results.append(line)
    return results

def fill_text_lines(text_lines, number, symbol = ' '):
    result = []

    for l in text_lines:
        words = str.join(' ', l)
        
        words_copy = list(map(lambda x: f'{x}{symbol}', l))
        words_copy[-1] = words_copy[-1][:-1] # Remueve el simbolo de la ultima palabra
        space_to_add = number - len(words)
        # print(f'add {space_to_add} space to: {words}')

        # Se le agregan espacios a todas las palabras menos la ultima
        words_slice = words_copy[:-1] 
        while space_to_add > 0 and len(words_slice):
            words_slice = words_slice[0:space_to_add]
            for i in range(len(words_slice)):
                words_copy[i] = f'{words_copy[i]}{symbol}'
                space_to_add -= 1
        
        result.append(words_copy)
    
    return result

def text_aligner(text, number_of_char, symbol = ' '):
    text_lines = split_text_into_lines(text, number_of_char)
    # print(text_lines)

    fill_lines = fill_text_lines(text_lines, number_of_char, symbol)
    # print(fill_lines)

    lines = [str.join('', l) for l in fill_lines]
    # print(lines)

    for line in lines: print(line)


if __name__ == '__main__':
    
    text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
    number_of_char = 5
    symbol = ' ' # Simbolo para agregar entre cada palabra

    text_aligner(text, number_of_char, symbol)
