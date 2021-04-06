import wolframalpha
from virtual import *

app_id ='29R7PV-X9K3U8X5ET'

client = wolframalpha.Client(app_id)

res = client.query(statement)

answer = next(res.results).text

print(answer)