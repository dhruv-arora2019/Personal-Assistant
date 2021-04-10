import os
import time
import wolframalpha
from virtual import *
def ask():
    speak('I can answer to computational and geographical questions')
    question=takeCommand()
    app_id="29R7PV-X9K3U8X5ET"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)
    print(answer)
