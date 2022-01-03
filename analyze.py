def count_syllables(words):
    '''Esta função fará a contagem de sílabas em todo o texto.'''
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count

def count_syllables_in_word(word):
    '''Já esta função determinará quantas sílabas haverá em cada palavra, além de tirar os "erros" de que quando separamos as palavras, algumas vem com pontuações no final dela. Também definirá excessões de regras silábicas no inglês, como o "e" mudo no final ou o "y" contando como vogal no final de uma palavra.'''
    count = 0
    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word


    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:    
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count = count + 1 

    return count 

def count_sentences(text):
    '''Esta função fará a contagem de frases em todo o texto de acordo com algumas pontuações.'''
    count = 0

    terminals = '.;!?'
    for char in text:
        if char in terminals:
            count = count + 1 

    return count

def output_results(score):
    '''A função correspondente esta determinando o nível de dificuldade da leitura de acordo com o calculo feito na "compute_readibility".'''
    if score >= 90:
        print('Reading level of 5th Grade')
    elif score >= 80:
        print('Reading level of 6th Grade')
    elif score >= 70:
        print('Reading level of 7th Grade')
    elif score >= 60:
        print('Reading level of 8-9th Grade')
    elif score >= 50:
        print('Reading level of 10-12th Grade')
    elif score >= 30:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')

def compute_readibility(text):
    '''Esta é a função que pegamos todos os dados que precisamos para conta e fazemos ela.'''
    total_words = 0
    total_senteces  = 0
    total_syllables = 0

    words = text.split()
    total_words = len(words)
    total_senteces = count_sentences(text)
    total_syllables = count_syllables(words)
    score = (206.835-1.015 * (total_words / total_senteces) - 84.6 * (total_syllables / total_words))

    output_results(score)