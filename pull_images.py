import requests
import file_save

collect_images_url = 'https://imgur.com/r/earthporn/top/day.json'

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"
min_images = 5

brackets_list = ['[',']','{','}','(',')']

#pull top images from reddit
def pullTopImages():
  #collect new image info as json
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

  #loop over top images in json response
  final_img_urls = []
  for img in data["data"]:
    #print (img['hash'], img['width'], img['height'])
    #check if wide and tall enough and landscape
    if width <= img['width'] and height <= img['height'] and img['width'] > img['height']:
      #create img url 
      imgur_url = 'https://i.imgur.com/'+img['hash']+'.jpg'
      #check if image already present
      #if so, don't replace current text and link
      if imgur_url not in existing_images:
        imgur_url = imgur_url + '\t'+ "https://www.reddit.com"+ img['reddit'] + '\t' + trimTitle(img['title'])
      else:
        imgur_url = imgur_url + '\t'+ existing_images[imgur_url][0] + '\t' + existing_images[imgur_url][1]
      #save the image for storage
      final_img_urls.append(imgur_url)

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
  line = file.readline()
  existing_images = {}
  while line:
    #ignore blank lines
    if len(line.strip()) < 1: continue
    #split line
    image = line.split('\t')
    #print("image", image)
    existing_images[image[0]] = [image[1], image[2]]
    line = file.readline()

  return existing_images

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