import schedule, time, hashlib
import render_img, pull_images, autocomplete

from flask import Flask, send_from_directory, request, jsonify, render_template
from flask_sslify import SSLify
from threading import Thread
app = Flask(__name__, static_folder='static')
sslify = SSLify(app)

img_urls_path = "static/image_urls.txt"

#render favicon
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/x-icon')

#google search suggestions
@app.route('/acgoog', methods=['GET'])
def autocomplete_google():
  return jsonify( autocomplete.get_suggestions('google',request.args.get('q')) )

#duckduckgo search suggestions
@app.route('/acddg', methods=['GET'])
def autocomplete_ddg():
  return jsonify( autocomplete.get_suggestions('ddg',request.args.get('q')) )

#new tab page
@app.route('/')
def newtab():
  image = render_img.get_image(img_urls_path)
  return render_template("final.html", imgurl = image[0], imgreddit = image[1], imgtext = image[2])
  
#info page
@app.route('/info')
def infopage():
  image = render_img.get_image(img_urls_path)
  return render_template("info.html", imgurl = image[0], imgreddit = image[1], imgtext = image[2])

#manually run image collection
hash_str = hashlib.sha256(time.ctime().encode('utf-8')).hexdigest()
run_images_url = '/runimages-'+hash_str
print("run images url: ",run_images_url)
@app.route(run_images_url)
def runimages():
  pull_images.pullTopImages()
  return "Image collection is running"
  #return app.send_static_file('./image_urls.txt')

#scheduling for image collection
def img_scheduler():
  print("Scheduling daily image job...")
  schedule.every().day.at("13:00").do(pull_images.pullTopImages)
  while True:
      #print("While loop for scheduler")
      schedule.run_pending()
      local_time = time.ctime()
      print("Scheduler: Local time:", local_time,)
      print("Current jobs:",schedule.jobs)
      time.sleep(50)

#keep image collection job on schedule
def keep_alive():  
    t = Thread(target=img_scheduler)
    t.start()

#start the web server and scheduling job
def main():
  print ("Starting scheduler and web host...")
  pull_images.pullTopImages()
  keep_alive()
  app.run(host='0.0.0.0', port='3000')

if __name__ == "__main__":
  main()
