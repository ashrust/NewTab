import requests, json, schedule, time, os
import file_save, render_img, pull_images

from flask import Flask, send_from_directory, request, redirect
#from flask_sslify import SSLify
from threading import Thread
app = Flask(__name__, static_folder='static')
#sslify = SSLify(app)
#app = Flask('')

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

def main():
  print ("main is running")
  pull_images.pullTopImages()
  keep_alive()
  app.run(host='0.0.0.0', port='3000')

def keep_alive():  
    t = Thread(target=newtab)
    t.start()

if __name__ == "__main__":
  main()

schedule.every().day.at("12:00").do(pull_images.pullTopImages)
while True:
    schedule.run_pending()
    time.sleep(1)