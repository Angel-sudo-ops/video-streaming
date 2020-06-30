# video-streaming
IP camera streming on the web using python, flask and opencv.

In this project the RTSP streaming of an IP camera is taken, the python program reads each frame and then using flask those frames are sent to a server. Besides, some controls are added to the HTML file rendered so they can be used to move the camera and go to specific presets. All that is using waitress as the production WSGI server.

The way the commands are sent to the camera is sending GET requests to the camera using the python module requests.

Then the camera and the controls are all rendered on an HTML. The purpose of doing this is to be able to stream and control the camera in any browser, without the restrictions of the camera's web interface, that only works on IE. The camera used in this project is from the D-Link family.

Once the camera is running it can be added to any other HTML file as an iframe or as a popup window.
