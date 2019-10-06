"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:

    if type(text) != str:

        return {} 

    frequencies = {} 

    text = text.lower() 

    illigal_signs = '1234567890^%~|[]<>{}@#&*-+=()_₽$€¥"£¢:;/?!`÷×§¶°¬¡¿™®©'

    for i in text:

        if i in illigal_signs:

            text = text.replace(i,'')

    text = text.split() 

    for i in text:

        frequencies[i] = 0

    for i in frequencies:

        for k in text:

            if i == k:

               frequencies[i] = frequencies.get(i, 0) + 1              

    return frequencies

frequencies = calculate (text) 
    

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    if type(frequencies)!= dict and type(stop_words) != tuple:

        return {} 

    d_clean = {} 

    for k, v in frequencies.items():

        if k not in stop_words and type(k) == str:

            d_clean[k] = v 

    return d_clean  

filter_stop_words (frequencies, stop_words)

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    "if type(frequencies) != dict or type(top_n) != int:

        return () 

    answer = () 

    if len(frequencies) < top_n:

        print ('В словаре только', l, 'записей') 

    freqsorted = sorted(frequencies.items(), key=lambda item: item[1], reverse = True)

    d_cleansort = {} 

    for k, v in freqsorted:

        d_cleansort[k] = v   

    m = 0

    for k, v in d_cleansort.items():

        if m != top_n:

            answer += (k, ) 

        else:

            break

        m += 1

    return answer 

get_top_n (frequencies, top_n) 
python -m unittest discover -p "*_test.py" -s .
