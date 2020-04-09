import requests
import file_save

collect_images_url = 'https://imgur.com/r/earthporn/top/month.json'

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"

brackets_list = ['[',']','{','}','(',')']

def pullTopImages():
  #pull top images from reddit

  #collect json
  resp = requests.get(url=collect_images_url)
  data = resp.json()

  #loop over images
  final_img_urls = []
  for img in data["data"]:
    #print (img)
    #check if wide and tall enough and landscape
    #print (img['hash'], img['width'], img['height'])
    if width <= img['width'] and height <= img['height'] and img['width'] > img['height']:
      #save the image 
      imgur_url = 'https://i.imgur.com/'+img['hash']+'.jpg'
      imgur_url = imgur_url + '\t'+ "https://www.reddit.com"+ img['reddit'] + '\t' + trimTitle(img['title'])
      final_img_urls.append(imgur_url)
<<<<<<< HEAD
      
=======
>>>>>>> origin/master
  #save urls/titles to a file
  #TODO - add images to previous if <5 for today. Read current file
  #collect urls, loop over new imgs list and if img isn't in current, add to current
  if len(final_img_urls) > 0:
    file_save.save_urls(final_img_urls, img_urls_path)
    print ("Image collection complete")
  else:
    #leave current file as is
    print ("Image collection unsuccessful. No new images to add. Keeping old file.")


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
  