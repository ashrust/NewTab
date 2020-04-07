import requests
import file_save

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"

brackets_list = ['[',']','{','}','(',')']

def pullTopImages():
  #pull top images from reddit

  #collect json
  url = 'https://imgur.com/r/earthporn/top/month.json'
  resp = requests.get(url=url)
  data = resp.json()

  #loop over images
  final_img_urls = []
  for img in data["data"]:
    #print (img)
    #check if wide and tall enough and landscape
    if width <= img['width'] and height <= img['height'] and img['width'] > img['height']:
      #save the image url
      #print (img['hash'], img['title'])
      imgur_url = 'https://i.imgur.com/'+img['hash']+'.jpg'
      imgur_url = imgur_url + '\t'+ img['reddit'] + '\t' + trimTitle(img['title'])
      final_img_urls.append(imgur_url)
      
    #print (img['hash'], img['width'], img['height'])
  #save urls/titles to a file
  file_save.save_urls(final_img_urls, img_urls_path)
  print ("Image collection complete")

def trimTitle(title):
  #split title by spaces
  words = title.split(" ")
  #clean string
  rebuilt = []
  for w in words:
    if any(b in w for b in brackets_list): 
      #stop when we find a bracket, if we have a title
      if len(rebuilt) > 0: 
        break
    else:
      rebuilt.append(w)
    #print (rebuilt)
  #join the string again
  new_title = " ".join(rebuilt)
  return new_title
  