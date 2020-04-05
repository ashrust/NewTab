import requests
import file_save

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"

def pullTopImages():
  #pull top images from reddit

  #collect json
  url = 'https://imgur.com/r/earthporn/top/day.json'
  resp = requests.get(url=url)
  data = resp.json()

  #loop over images
  final_img_urls = []
  for img in data["data"]:
    #print (img)
    #check if wide and tall enough - 
    if width <= img['width'] and height <= img['height']:
      #save the image url
      #http://i.imgur.com/'.$image->hash.'.jpg
      imgur_url = 'http://i.imgur.com/'+img['hash']+'.jpg'
      imgur_url = imgur_url + '\t' + trimTitle(img['title'])
      final_img_urls.append(imgur_url)
      
    #print (img['hash'], img['width'], img['height'])
  #save urls to a file
  file_save.save_urls(final_img_urls, img_urls_path)
  print ("Image collection complete")

def trimTitle(title):
  #split title by spaces
  words = title.split(" ")
  #clean string
  rebuilt = []
  for w in words:
    if ("[" in w) or ("]" in w) or ("{" in w) or ("}" in w):
      #stop when we find a bracket
      break
    else:
      rebuilt.append(w)
  #join the string again
  new_title = " ".join(rebuilt)
  return new_title
  