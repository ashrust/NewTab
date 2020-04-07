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
        font-family: arial, sans-serif;
        color: #FFF;
        font-size: 16px;
        opacity: 0.3;
        background-color: #777;
        border-radius: 5px;
        white-space: nowrap;
        max-width: 500px;
        overflow: hidden;
        text-overflow: ellipsis;
        padding-bottom: 3px;
        padding-top: 3px;
      }

      .bottomright a {
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
      a:link,
      a:visited,
      a:hover,
      a:active {
        color: #FFF;
        text-decoration: none;
      }

      div.bottomright:hover {
        opacity: 0.9;
        background-color: #555;
      }

      .topleft {
        position: absolute;
        top: 8px;
        left: 8px;
        font: 16px arial, sans-serif;
      }

      input[type=text] {
        font-size: 16px;
        color: #000;
        opacity: 0.3;
      }

      input[type=text]:focus {
        background-color: lightblue;
        opacity: 0.6;
      }

      #ddgDiv {
        float: left;
        padding-left: 10px;
      }

      #googDiv {
        float: left;
        padding-left: 10px;
      }

      .autocomplete-items {
        /*position: absolute;
        border: 1px solid #d4d4d4;
        padding: 1px;*/
        border-bottom: none;
        border-top: none;
        z-index: 99;
        /*position the autocomplete items to be the same width as the container:*/
        top: 100%;
        left: 0;
        right: 0;
        margin-left: 2px;
        margin-right: 2px;
        margin-top: 2px;
      }

      .autocomplete-items div {
        padding: 6px;
        cursor: pointer;
        background-color: #fff;
        border-bottom: 1px solid #d4d4d4;
        opacity: 0.65;
      }

      /*when hovering an item:*/
      .autocomplete-items div:hover {
        background-color: #e9e9e9;
      }

      /*when navigating through the items using the arrow keys:*/
      .autocomplete-active {
        background-color: DodgerBlue !important;
        color: #ffffff;
      }

    </style>
  </head>

  <body>
    <div class='bgimg-1'>
      <div class="bottomright"><a href="https://www.reddit.comIMGREDDITLINK" target="_blank"> IMGTXT </a></div>
      <div class="topleft">
        <div id="ddgDiv">
          <form id="ddgSearch" method="get" action="https://duckduckgo.com/" style="padding:0; margin:0;">
            <div class="ddgautocomplete">
            <input id="ddgSearchBar" type="text" name="q" size="25" value="" autofocus="autofocus" placeholder="DuckDuckGo Search..." spellcheck="false">
            </div>
          </form>
        </div>
        <div id="googDiv">
          <form id="googleSearch" method="get" action="https://www.google.com/search" style="padding:0; margin:0;">
            <div class="googautocomplete">
              <input id="googleSearchBar" type="text" name="q" size="25" value="" placeholder="Google Search..." spellcheck="false">
            </div>
          </form>
        </div>
      </div>
    </div>
    <script>
      function showGoogHint(inp) {

  var currentFocus;

  function collect_results(e) {
    var a, b, i, val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) {
      return false;
    }
    //currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    /*append the DIV element as a child of the autocomplete container:*/
    if (this.value.length == 0) {
      closeAllLists();
      return;
    }
    this.parentNode.appendChild(a);
    //collect query results
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        //convert response
        var suggs = JSON.parse(this.responseText);
        //console.log(suggs)
        /*for each item in the array...*/
        for (i = 0; i < suggs.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (suggs[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + suggs[i].substr(0, val.length) + "</strong>";
            b.innerHTML += suggs[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + suggs[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
            b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
            });
            a.appendChild(b);
          }
        }
      }
    };
    xhttp.open("GET", "/acgoog?q=" + this.value, true);
    xhttp.send();
    console.log(currentFocus)
  }

  function key_down(e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      //e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      } else {
        console.log("current focus is -1")
        document.getElementById("googleSearch").submit();
      }
    }
  }

  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }

  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
    console.log(currentFocus)
    currentFocus = -1
  }
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", collect_results);
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", key_down);
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function(e) {
    closeAllLists(e.target);
  });
}

showGoogHint(document.getElementById("googleSearchBar"));

function showDDGHint(inp) {

  var currentFocus;

  function collect_results(e) {
    var a, b, i, val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) {
      return false;
    }
    //currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    /*append the DIV element as a child of the autocomplete container:*/
    if (this.value.length == 0) {
      closeAllLists();
      return;
    }
    this.parentNode.appendChild(a);
    //collect query results
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        //convert response
        var suggs = JSON.parse(this.responseText);
        //console.log(suggs)
        /*for each item in the array...*/
        for (i = 0; i < suggs.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (suggs[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + suggs[i].substr(0, val.length) + "</strong>";
            b.innerHTML += suggs[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + suggs[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
            b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
            });
            a.appendChild(b);
          }
        }
      }
    };
    xhttp.open("GET", "/acddg?q=" + this.value, true);
    xhttp.send();
    console.log(currentFocus)
  }

  function key_down(e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      //e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      } else {
        console.log("current focus is -1")
        document.getElementById("ddgSearch").submit();
      }
    }
  }

  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }

  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
    console.log(currentFocus)
    currentFocus = -1
  }
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", collect_results);
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", key_down);
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function(e) {
    closeAllLists(e.target);
  });
}

showDDGHint(document.getElementById("ddgSearchBar"));


    </script>
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