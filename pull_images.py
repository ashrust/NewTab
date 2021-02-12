import requests
import file_save
import os

collect_images_url = 'https://api.imgur.com/3/gallery/r/earthporn/top/week/'
client_id = os.getenv("CLIENT_ID")

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"
banned_imgs_path = "static/banned_images.txt"
min_images = 5

brackets_list = ['[',']','{','}','(',')']

#pull top images from reddit
def pullTopImages():
  #collect new image info as json
  payload = {}
  files = {}
  headers = {
    'Authorization': 'Client-ID {}'.format(client_id)
  }
  response = requests.request("GET", collect_images_url, headers=headers, data = payload, files = files)

  #print(response.text.encode('utf8'))
  resp = requests.get(url=collect_images_url)
  data = resp.json()

  #get urls to save
  image_urls = getFinalImages(data)

  #save urls/titles to a file
  if len(image_urls) > 0:
    file_save.save_urls(image_urls, img_urls_path)
    print ("Image collection complete")
  else:
    #leave current file as is
    print ("Image collection unsuccessful. No new images to add. Keeping existing file.")


def getFinalImages(data):
  #collect existing image info
  existing_images = getExistingImages()
  #print("existing_images", existing_images)
  #collect banned image_urls
  banned_images = getBannedImages()

  #loop over top images in json response
  final_img_urls = []
  for img in data["data"]:
    #print (img['hash'], img['width'], img['height'])
    #check if wide and tall enough and landscape
    if width <= img['width'] and height <= img['height'] and img['width'] > img['height']:
      #create img url 
      imgur_url = img['link']
      #check if image banned, if so ignore
      if imgur_url in banned_images: 
        print ("Ignoring banned image: ", imgur_url)
        continue
      #check if image already present
      #if so, don't replace current text and link
      if imgur_url not in existing_images:
        imgur_url = imgur_url + '\t'+ imgur_url + '\t' + trimTitle(img['title'])
      else:
        imgur_url = imgur_url + '\t'+ existing_images[imgur_url][0] + '\t' + existing_images[imgur_url][1]
      #save the image for storage
      final_img_urls.append(imgur_url)

  print("new image collection results", final_img_urls)

  #check if final_img_urls long enough
  #if not, add non duplicate current images to final list
  if len(final_img_urls) < min_images:
    print("finalimg urls too short, adding existing images")
    for url,data in existing_images.items():
      #nested loop but we know the final image list is shorter than the min
      present = False
      for line in final_img_urls:
        #if the url is present, stop loop
        if url in line:
          present = True
          break
      if not present:
        output = url + '\t'+ existing_images[url][0] + '\t' + existing_images[url][1]
        final_img_urls.append(output)

  return final_img_urls

#read current images file into dict
def getExistingImages():
  #open urls File
  file = open(img_urls_path,"r")
  lines = file.readlines()
  existing_images = {}
  for line in lines:
    #ignore blank lines
    if len(line.strip()) < 1: continue
    #split line
    image = line.split('\t')
    #print("image", image)
    existing_images[image[0]] = [image[1], image[2]]
  return existing_images

def getBannedImages():
  banned_images = {}
  #open urls File
  file = open(banned_imgs_path,"r")
  lines = file.readlines()
  for line in lines:
    #ignore blank lines
    line = line.strip()
    if len(line) < 1: continue
    #store banned url
    banned_images[line] = 1
  return banned_images

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