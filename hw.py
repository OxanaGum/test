print("Hello, World!")
x = input("Как Вас зовут? ")
dictionary = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'cz',
    'ш': 'sh',
    'щ': 'scz',
    'ъ': '',
    'ы': 'y',
    'ь': 'b',
    'э': 'e',
    'ю': 'u',
    'я': 'ja',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'C',
    'Ч': 'CZ',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ъ': '',
    'Ы': 'y',
    'Ь': 'b',
    'Э': 'E',
    'Ю': 'U',
    'Я': 'YA'}
for i in x:
	if i in dictionary.keys():
		x = x.replace(i, dictionary[i])
	if i in dictionary.values():
		slovar = dict(zip(dictionary.values(), dictionary.keys()))
		if i in slovar.keys():
	                x = x.replace(i, slovar[i])
print(slovar)
print("Hello,", x)



#transliteration is not welcomed
