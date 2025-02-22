# ADB Remote Phone

Inspired by the similar projects [adb-remote-control](https://github.com/oberien/adb-remote-control) and [adbcontrol](http://marian.schedenig.name/2014/07/03/remote-control-your-android-phone-through-adb/). Both of these use screenshots to feed screen information, but it is possible to record the screen and stream it in realtime instead, which is much more efficient.

## Dependencies
Requires [adb](https://developer.android.com/studio/releases/platform-tools) and [ffmpeg](https://ffmpeg.org/)

### Python

Python requirements can be installed from with the command `pip install -r requirements.txt` or equivalent. Alternatively, the program uses the OpenCV library for screen rendering and the module `screeninfo` to get the display resolution.