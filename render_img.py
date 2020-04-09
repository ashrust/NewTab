import random

default_image = ["static/default.jpg", 
                  "https://unsplash.com/photos/TkSi_p-5HR0",
                  "Engelberg, Switzerland by Ricardo Gomez Angel"]

def get_image(filepath):
  #open urls File
  file = open(filepath,"r")
  #pick image at random
  lines = file.readlines()
  #print (lines)
  if len(lines) > 0:
    final_img_url = random.choice(lines)
    # return list "IMGURL", "IMGREDDITLINK", "IMGTXT"
    splits = final_img_url.split('\t')
    return splits
  else:
    #if no new images available, return default img
    return default_image