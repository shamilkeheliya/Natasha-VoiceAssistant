import wolframalpha
import editables
import speak


def calculate(query):
    client = wolframalpha.Client(editables.wolframalphaAPIkey)
    indx = query.lower().split().index('calculate')
    query = query.split()[indx + 1:]
    res = client.query(''.join(query))
    answer = next(res.results).text
    speak.speak(f'The Answer is : {answer}')


def explain(query):
    client = wolframalpha.Client(editables.wolframalphaAPIkey)
    res = client.query(query)

    try:
        speak.speak(next(res.results).text)
    except StopIteration:
        speak.speak('No Result')
