# video-streaming
IP camera streming on the web using python, flask and opencv.

In this project the RTSP streaming of an IP camera is taken, the python program reads each frame and then using flask those frames are sent to a server. Besides, some controls are added to the HTML file rendered so they can be used to move the camera and go to specific presets. All that is using waitress as the production WSGI server.

The way the commands are sent to the camera is sending GET requests to the camera using the python module requests.

Then the camera and the controls are all rendered on an HTML. The purpose of doing this is to be able to stream and control the camera in any browser, without the restrictions of the camera's web interface, that only works on IE. The camera used in this project is from the D-Link family, but this project can be adeqauted to any camera, given that said camera has a streaming in the form of rtsp://"ip"/

# Usage
  1. Start the VideoStream.py and go to "http://0.0.0.0:5003"
  2. See the result in the browser

Once the program VideoStream.py is running the camera stream can be accesed on the route "http://0.0.0.0:5003" and then be added to any other HTML file as an iframe or as a popup window, for example. That can be seen in the popupExample.html file.

# To-Do

The idea of using threads was explored but as teh results are the beginning were not that good, it was decided to move on, but it is worth to try again from a different perspective to see if the proble of the lagging and delay is solved.
