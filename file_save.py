
def save_urls(urls, filepath):
  final_string = ""
  for u in urls:
    final_string = final_string + u.strip() + "\n"
  #print(final_string)
  #open, write, close file
  file = open(filepath,"w")
  #print(file)
  file.write(final_string.strip()) 
  file.close()

