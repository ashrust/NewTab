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
  opacity: 0.3;
  background-color: #777;
  white-space: nowrap; 
  max-width: 500px; 
  overflow: hidden;
  text-overflow: ellipsis; 
  padding-bottom: 3px;
  padding-top: 3px;
}

.bottomright a{
  #display:block;
  padding-right: 15px;
  padding-left: 15px;
  padding-bottom: 10px;
  padding-top: 15px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: 150%;
}

/* link */
a:link, a:visited, a:hover, a:active {
  color: #FFF;
  text-decoration: none;
}

div.bottomright:hover{
  opacity: 1;
}

.topleft {
  position: absolute;
  top: 8px;
  left: 8px;
  font: 16px arial,sans-serif ;
}

input[type=text]{
  font-size:16px;
  color: #000;
  opacity: 0.3;
}

input[type=text]:focus {
  background-color: lightblue;
  opacity: 0.6;
}
#ddgDiv{
  float:left; 
  padding-left: 10px;
}
</style>
</head>
<body onbeforeunload="">
<div class='bgimg-1'>
<div class="bottomright"><a href="https://www.reddit.com/IMGREDDITLINK" target="_blank"> IMGTXT </a></div>
<div class="topleft">
  <div id="ddgDiv">
  <form id="ddgSearch" method="get" action="https://duckduckgo.com/" style="padding:0; margin:0;">
    <input id="ddgSearchBar" type="text" name="q" size="25" value="" autofocus="autofocus" placeholder="DuckDuckGo Search..." spellcheck="false">
    <input type="hidden" name="ia" value="web">
  </form>
  </div>
  <div style="float:left; padding-left: 10px;">
  <form id="googleSearch" method="get" action="https://www.google.com/search" style="padding:0; margin:0;">
    <input id="googleSearchBar" type="text" name="q" size="25" value=""  placeholder="Google Search..." spellcheck="false">
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
  #add reddit img url - IMGREDDITLINK
  replace_vars = ["IMGURL", "IMGREDDITLINK", "IMGTXT"]
  temp = raw_html
  for x in range( len(replace_vars) ):#need to use int for splits traversal
    temp = temp.replace(replace_vars[x], splits[x].strip())
  return temp