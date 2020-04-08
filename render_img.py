import random

raw_html = """
<html>
  <head>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>New Tab</title>
    <link rel='shortcut icon' href='favicon.ico' type='image/x-icon'>
    <link rel="stylesheet" href="static/styles.css">
    <style>
    html {
      background: url(IMGURL) no-repeat center center fixed;
      -webkit-background-size: cover;
      -moz-background-size: cover;
      -o-background-size: cover;
      background-size: cover;
    }
    </style>
  </head>

  <body>
    <div class='bgimg-1'>
      <div class="bottomright"><a href="https://www.reddit.comIMGREDDITLINK" target="_blank"> IMGTXT </a></div>
      <div class="topleft">
        <div id="ddgDiv">
          <form id="ddgSearch" method="get" action="https://duckduckgo.com/" style="padding:0; margin:0;" autocomplete="off">
            <div class="ddgautocomplete">
            <input id="ddgSearchBar" type="text" name="q" size="25" value="" autofocus="autofocus" placeholder="DuckDuckGo Search..." spellcheck="false" autocomplete="off" tabindex="1">
            </div>
          </form>
        </div>
        <div id="googDiv">
          <form id="googleSearch" method="get" action="https://www.google.com/search" style="padding:0; margin:0;" autocomplete="off">
            <div class="googautocomplete">
              <input id="googleSearchBar" type="text" name="q" size="25" value="" placeholder="Google Search..." spellcheck="false" autocomplete="off" tabindex="2">
            </div>
          </form>
        </div>
      </div>
    </div>
    <script src="static/xhr.js"></script>
  </body>
</html>
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