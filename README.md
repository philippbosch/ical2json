ical2json
=========

This is a super simple webservice that consumes iCal data (.ics file) that is publicly available at an HTTP URL and returns JSON data.


Installation
------------

```
$ git clone https://github.com/philippbosch/ical2json.git
Cloning into 'ical2json'...
remote: Reusing existing pack: 54, done.
remote: Total 54 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (54/54), done.
Checking connectivity... done.

$ cd ical2json
$ virtualenv venv
New python executable in venv/bin/python2.7
Also creating executable in venv/bin/python
Installing Setuptools..............................................................................................................................................................................................................................done.
Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.

$ source venv/bin/activate
$ pip install -r requirements.txt
Downloading/unpacking ...
...
Successfully installed Flask Jinja2 Werkzeug gunicorn icalendar pytz distribute
Cleaning up...

$ python app.py
 * Running on http://0.0.0.0:5000/
```




Installation on Heroku
----------------------

First, install locally (see above). Then:

```
$ heroku create
Creating polar-beyond-7859... done, stack is cedar
http://polar-beyond-7859.herokuapp.com/ | git@heroku.com:polar-beyond-7859.git
Git remote heroku added

$ git push heroku master
Initializing repository, done.
Counting objects: 59, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (52/52), done.
Writing objects: 100% (59/59), 7.95 KiB | 0 bytes/s, done.
Total 59 (delta 21), reused 0 (delta 0)

-----> Python app detected
-----> No runtime.txt provided; assuming python-2.7.6.
-----> Preparing Python runtime (python-2.7.6)
-----> Installing Setuptools (2.1)
-----> Installing Pip (1.5.4)
-----> Installing dependencies using Pip (1.5.4)
...
       Successfully installed Flask Jinja2 Werkzeug gunicorn icalendar pytz distribute
       Cleaning up...
-----> Discovering process types
       Procfile declares types -> web

-----> Compressing... done, 30.6MB
-----> Launching... done, v3
       http://polar-beyond-7859.herokuapp.com/ deployed to Heroku

To git@heroku.com:polar-beyond-7859.git
 * [new branch]      master -> master
```

Done.


Usage
-----

Simply construct an URL like this:

    http://0.0.0.0:5000/http://hostname.com/path/to/file.ics

E.g., let's say we want to get the iCal data available at http://ws.audioscrobbler.com/1.0/artist/Shout+Out+Louds/events.ics in JSON format, the URL would look like this:

    http://0.0.0.0:5000/http://ws.audioscrobbler.com/1.0/artist/Shout+Out+Louds/events.ics

The response would look something like this:

```json
{
  "VCALENDAR": {
    "VEVENT": [
      {
        "DTSTAMP": "20110328T203000",
        "UID": "LFMEVENT-1748422",
        "URL": "http://www.last.fm/event/1748422+Shout+Out+Louds+at+La+Machine+du+Moulin+Rouge+on+28+March+2011",
        "SUMMARY": "Shout Out Louds at La Machine du Moulin Rouge",
        "LOCATION": "La Machine du Moulin Rouge, Paris, France",
        "DTEND": "20110328T235900",
        "DTSTART": "20110328T203000",
        "GEO": "2.332258;48.884008",
        "DESCRIPTION": "Shout Out Louds\n\nhttp://www.last.fm/event/1748422+Shout+Out+Louds+at+La+Machine+du+Moulin+Rouge+on+28+March+2011"
      },
      {
        "DTSTAMP": "20110329T203000",
        "UID": "LFMEVENT-1755031",
        "URL": "http://www.last.fm/event/1755031+Shout+Out+Louds+at+La+Nef+on+29+March+2011",
        "SUMMARY": "Shout Out Louds + Hello Bye Bye at La Nef",
        "LOCATION": "La Nef, Angoul\u00eame, France",
        "DTEND": "20110329T235900",
        "DTSTART": "20110329T203000",
        "GEO": "0.130579;45.640423",
        "DESCRIPTION": "Shout Out Louds, Hello Bye Bye\n\nhttp://www.last.fm/event/1755031+Shout+Out+Louds+at+La+Nef+on+29+March+2011"
      }
      # …
    ],
    "VERSION": "2.0",
    "X-WR-CALNAME": "Last.fm Events",
    "PRODID": "-//Last.fm Limited Event Feeds//NONSGML//EN",
    "X-WR-CALDESC": "Event listing - supplied by http://www.Last.fm"
  }
}
```

JSON-P Callback
---------------

If you want to consume the JSON data with JavaScript on a website you may need to utilize JSON-P. Therefore simply append <code>?callback=*yourCallBackFunction*</code> to the URL, and we'll wrap the response in <code>yourCallBackFunction(…);</code>.



Status
------

I wrote this thing in less than an hour. For me it does what I want it to do. But I have not tested a whole lot of different URLs. And it probably does not cover everything that is part of the iCal spec. So if you find something that does not work feel free to fork and send a pull request.
