import random

raw_html = """
<html>
<head>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>New Tab</title>
<link rel='shortcut icon' href='favicon.ico' type='image/x-icon'>
<style>
html { 
  background: url(IMGURL) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.bottomright {
  position: absolute;
  bottom: 8px;
  right: 8px;
  font-family: arial,sans-serif;
  color: #FFF;
  font-size: 16px; 
  opacity: 0.5;
  background-color: #777;
  padding-right: 10px;
  padding-left: 10px;
  padding-top: 5px;
  padding-bottom: 5px;
}
.topleft {
  position: absolute;
  top: 8px;
  left: 8px;
  font: 16px arial,sans-serif ;
  color: #222;
}

input[type=text]{
  font-size:16px;
  color: #555;
  opacity: 0.3;
}

input[type=text]:focus {
  background-color: lightblue;
  opacity: 0.6;
}

</style>
</head>
<body onbeforeunload="">
<div class='bgimg-1'>
<div class="bottomright"> IMGTXT </div>
<div class="topleft">
  <div style="float:left; padding-right: 10px;">
  <form id="ddgSearch" method="get" action="https://duckduckgo.com/" style="padding:0; margin:0;">
    <input id="ddgSearchBar" type="text" name="q" size="25" value="" autofocus="autofocus" placeholder="DuckDuckGo Search...">
    <input type="hidden" name="ia" value="web">
  </form>
  </div>
  <div style="float:left;">
  <form id="googleSearch" method="get" action="https://www.google.com/search" style="padding:0; margin:0;">
    <input id="googleSearchBar" type="text" name="q" size="25" value=""  placeholder="Google Search...">
  </form>
  </div>
</div>
</div>
</body>
"""

def render_html(filepath):
  #open urls File
  file = open(filepath,"r")
  #pick image at random
  lines = file.readlines()
  #print (lines)
  #return html
  final_img_url = random.choice(lines)
  splits = final_img_url.split('\t')
  temp = raw_html.replace("IMGURL", splits[0].strip())
  return temp.replace("IMGTXT", splits[1].strip())