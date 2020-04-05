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
.bottomleft {
  position: absolute;
  bottom: 8px;
  left: 8px;
  opacity: 0.4;
  font: 16px arial,sans-serif ;
  color: #333;
}
#ddg {
  float:left; padding-right: 10px;
}
#goog{
  float:left;
}
.entered {
  position: absolute;
  top: 30%;
  left: 50%;
  display: none;
}

.largetext {
  font-size: 24px;
}

input[type=text]:focus {
  background-color: lightblue;
}
</style>
<script>
var inputBoxes = document.getElementsByClassName('input');
for (var i = 0; i < inputBoxes.length; i++) {
  inputBoxes[x].onkeyup = function() {
    parent_div = inputBoxes[x].parentElement.parentElement;
    parent_div.classList.add("entered");
    parent_div.removeAttribute("id");
    inputBoxes[x].classList.add("largetext");
  }
}

</script>
</head>
<body>
<div class='bgimg-1'>
<div class="bottomright"> IMGTXT </div>
<div class="bottomleft">
  <div id="ddg">
  <form id="ddgSearch" method="get" action="https://www.duckduckgo.com/search" style="padding:0; margin:0;">
    <input id="ddgSearchBar" class="input" type="text" name="q" size="25" value="" autofocus="autofocus" style="font-size:16px;" placeholder="DuckDuckGo Search">
  </form>
  </div>
  <div id="goog" class="input" >
  <form id="googleSearch"  method="get" action="https://www.google.com/search" style="padding:0; margin:0;">
    <input id="googleSearchBar" class="input" type="text" name="q" size="25" value="" style="font-size:16px;" placeholder="Google Search">
  </form>
  </div>
</div>
</div>
</body>
"""
# js css trials http://jsfiddle.net/wuqg49xt/

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