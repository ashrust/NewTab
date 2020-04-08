import random

def get_image(filepath):
  #open urls File
  file = open(filepath,"r")
  #pick image at random
  lines = file.readlines()
  #print (lines)
  #return html
  final_img_url = random.choice(lines)
  # "IMGURL", "IMGREDDITLINK", "IMGTXT"
  splits = final_img_url.split('\t')

  return splits