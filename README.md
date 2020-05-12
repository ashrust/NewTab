# NewTab for Safari - Beautiful Images, Simple Search

## Overview

[NewTab](https://newtab.click) is simple new tab page with beautiful background images, simple search and no ads or trackers. 

I was frustrated that no extension for this existed on Safari, so I built it. You can also use it on Google Chrome, Brave and Microsoft Edge. Every night, the app collects links to the top images from [Reddit](https://www.reddit.com/) via [Imgur](http://imgur.com/). The default search engine is [DuckDuckGo](http://duckduckgo.com/) but you can hit tab to switch to Google. 

Made by [Ash Rust](https://twitter.com/@ashrust).

## How to Use

First clone the [repo on GitHub](https://github.com/ashrust/NewTab).

### Running your own server

In the **NewTab** folder run: 
* **pip install -r requirements.txt**
* **python main.py**

This will start the web server. Point any domain, with SSL, at the web server and you're live! If you'd prefer to try it out without SSL, comment out line 8 in **main.py**.

You can also try a slightly older version on [Repl.it](https://repl.it/@ashrust/NewTabOpenSource).

### Browser Installation
**Safari:**
* Go to Safari's Preferences
* Under the _General_ tab, set your homepage to: **YOUR DOMAIN NAME** e.g. https://newtab.click
* Then set _New tabs open with_ to **Homepage**
* Lastly set _New windows open with_ to **Homepage** 

**Chrome:**

To create your own extension, edit line 1 of **script.js** in the **chrome-extension** folder to be your domain. You can then load the unpacked extension from Chrome, under _Window_, then _Extensions_. 
If you would like others to be able to easily install your extension, [submit the extension to the Chrome Webstore](https://developer.chrome.com/webstore/publish).

**Edge:**

Information on how to port a Chrome extension to Edge is [here](https://docs.microsoft.com/en-us/microsoft-edge/extensions-chromium/developer-guide/port-chrome-extension).

## Support & Contributing

This software is provided free and [open source](https://github.com/ashrust/NewTab/blob/master/LICENSE), it comes with absolutely no warranty or customer support whatsoever. 

If you find a bug or would like to contribute code to the project, contact [Ash Rust](https://twitter.com/@ashrust).

## Credits

This software is released under the [MIT license](http://bit.ly/mit-license). You *may not* redistribute this software without proper attribution.

* Monitoring provided by [UptimeRobot](https://uptimerobot.com/)
* Globe icon is from the [Vistoon](https://findicons.com/icon/60415/globe) icon pack under Creative Commons
* Code for query suggestions was adapted from tutorials on [W3Schools](https://www.w3schools.com/js/default.asp)
* Default image by [Ricardo Gomez Angel](https://unsplash.com/photos/TkSi_p-5HR0).