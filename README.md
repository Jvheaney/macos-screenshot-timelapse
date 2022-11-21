# MacOS Screenshot Timelapse
These are two scripts, one to take screenshots on MacOS on an interval and another to stitch together those screenshots into a timelapse video.

You run `timelapse.py`, which takes screenshots on an interval, with `python timelapse.py {interval}`.

Interval is an int and is optional, the default is 10s.

You run `render_timelapse.py`, which stitches those screenshots together into an MP4 video, with `python render_timelapse.py {output_name} {fps}`.

output_name is a string and is optional, the default is "timelapse.mp4".

fps is an int and is optional, the default is 30.

It uses OpenCV (and by extension NumPy).

You can install it with `pip install opencv-python`.
