import json, schedule, time, os
import file_save, render_img, pull_images

from flask import Flask, send_from_directory
#from flask_sslify import SSLify
from threading import Thread
app = Flask(__name__, static_folder='static')
#app = Flask('')
#sslify = SSLify(app)

img_urls_path = "static/image_urls.txt"

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/x-icon')

@app.route('/')
def newtab():
  return render_img.render_html(img_urls_path)

@app.route('/runimages')
def root():
  pull_images.pullTopImages()
  return "Image collection is running"
  #return app.send_static_file('./image_urls.txt')

def img_scheduler():
  print("Scheduling daily image job...")
  schedule.every().day.at("10:00").do(pull_images.pullTopImages)
  while True:
      #print("While loop for scheduler")
      schedule.run_pending()
      local_time = time.ctime()
      print("Scheduler: Local time:", local_time,)
      print("Current jobs:",schedule.jobs)
      time.sleep(50)

def keep_alive():  
    t = Thread(target=img_scheduler)
    t.start()

def main():
  print ("Starting scheduler and web host...")
  pull_images.pullTopImages()
  keep_alive()
  app.run(host='0.0.0.0', port='3000')

if __name__ == "__main__":
  main()
