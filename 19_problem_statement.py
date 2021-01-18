text_output = ''

while True:
    text = input('Say something: ')
    if text == '\end':
        break
    else:
        if text.startswith('how' or 'when' or 'who' or 'where' or 'whom'):
            text_output = text_output + text.capitalize() + '? '
        else:
            text_output = text_output + text.capitalize() + '. '

print(text_output)


#==================== How it was solved by programmer =========================


def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
    
results = []
while True:
    user_input = input('Say something: ')
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))