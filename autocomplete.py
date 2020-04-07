import json, requests

goog_url = "http://suggestqueries.google.com/complete/search?client=safari&q="

def google_suggestions(query):
  results = get_google_results(query)
  results = json.loads(results)
  final = []
  #print("results", results[1][1][0])
  for r in results[1]:
    final.append(r[0].strip())
  print ("ac final", final)
  return final


def get_google_results(query):
  #print ("url parts",goog_url, query)
  send_url = goog_url+query
  #print ("url final",send_url)
  resp = requests.get(url=send_url)
  #print ("response text", resp.text)
  return resp.text

