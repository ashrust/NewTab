import requests, praw
import file_save
import os

collect_images_urls = ['day', 'week', 'month']
subreddit = "EarthPorn"

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

width = 3840
height = 2160
img_urls_path = "static/image_urls.txt"
banned_imgs_path = "static/banned_images.txt"
min_images = 5

brackets_list = ['[',']','{','}','(',')']

#pull top images from reddit
def pullTopImages():
  #collect new image info as json

  image_urls = []
  for time_period in collect_images_urls:
    reddit = praw.Reddit(
      client_id=client_id,
      client_secret=client_secret,
      user_agent="NewTab by u/ashrust"
    ) 

    #get urls to save
    image_urls = image_urls + getFinalImages(reddit, time_period)
    #print("time, images count", time_period, len(image_urls))

    #save urls/titles to a file, stop when we have enough
    if len(image_urls) >= min_images:
      file_save.save_urls(image_urls, img_urls_path)
      print ("Image collection complete, reached top by:", time_period, len(image_urls))
      break
  
  #still not enough after trying all urls.
  if len(image_urls) < min_images:
    #leave current file as is
    print ("Image collection unsuccessful. No new images to add. Keeping existing file.")


def getFinalImages(reddit, time_period):
  #collect existing image info
  existing_images = getExistingImages()
  #print("existing_images", existing_images)
  #collect banned image_urls
  banned_images = getBannedImages()

  #loop over top images in json response
  final_img_urls = []
  for img in reddit.subreddit(subreddit).top(time_period):
    #print("img: ", vars(img))
    try:
      img.preview
    except AttributeError:
        pass
    else:
      curr_img_width = img.preview['images'][0]['source']['width']
      curr_img_height = img.preview['images'][0]['source']['height']
      #print ("curr height, width", curr_img_height, curr_img_width)
      #check if wide and tall enough and landscape
      if width <= curr_img_width and height <= curr_img_height and curr_img_width > curr_img_height:
        #create img url 
        imgur_url = img.url
        #check if image banned, if so ignore
        if imgur_url in banned_images: 
          print ("Ignoring banned image: ", imgur_url)
          continue
        #if image already present, Keep current text and link
        if imgur_url not in existing_images:
          imgur_url = imgur_url + '\t'+ "http://reddit.com"+ img.permalink + '\t' + trimTitle(img.title)
        else:
          imgur_url = imgur_url + '\t'+ existing_images[imgur_url][0] + '\t' + existing_images[imgur_url][1]
        #save the image for storage, if not already present in final
        if imgur_url not in final_img_urls:
          final_img_urls.append(imgur_url)

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