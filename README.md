ical2json
=========

This is a super simple webservice that consumes iCal data (.ics file) that is publicly available at an HTTP URL and returns JSON data.


Usage
-----

Simply construct an URL like this:

    http://ical2json.pb.io/hostname.com/path/to/file.ics

E.g., let's say we want to get the iCal data available at http://ws.audioscrobbler.com/1.0/artist/Shout+Out+Louds/events.ics in JSON format, the URL would look like this:

    http://ical2json.pb.io/ws.audioscrobbler.com/1.0/artist/Shout+Out+Louds/events.ics

The response would look something like this:

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


JSON-P Callback
---------------

If you want to consume the JSON data with JavaScript on a website you probably need to utilize JSON-P. Therefore simply append <code>?callback=*yourCallBackFunction*</code> to the URL, and we'll wrap the response in <code>yourCallBackFunction(…);</code>.


Local installation
------------------

If you wanted to install this on your own server (I encourage you to do so) you would need the following prerequisites:

* [Python](http://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [icalendar](http://pypi.python.org/pypi/icalendar)




Status
------

I wrote this thing in less than an hour. For me it does what I want it to do. But I have not tested a whole lot of different URLs. And it probably does not cover everything that is part of the iCal spec. So if you find something that does not work feel free to fork and send a pull request. 
