import json, requests

#suggestion urls
goog_url = "http://suggestqueries.google.com/complete/search?client=safari&q="
ddg_url ="https://duckduckgo.com/ac/?kl=wt-wt&q="

def get_suggestions(engine, query):
  print ("eng, q", engine, query)
  response = get_results(engine, query)
  results = json.loads(response)
  final = []

  if engine == 'google':
    for r in results[1]:
      final.append(r[0].strip())
  else:
    for r in results:
      final.append(r['phrase'])

  return final
  
#hit google server for suggestions and return response
def get_results(engine, query):
  print ("url parts",goog_url, query)
  send_url = ""
  if engine == "google": send_url = goog_url+query
  else: send_url = ddg_url+query
  print ("url final",send_url)
  resp = requests.get(url=send_url)
  #print ("response text", resp.text)
  return resp.text


