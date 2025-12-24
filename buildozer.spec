[app]

# (str) Title of your application
title = Galaxy

# (str) Package name
package.name = galaxyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.galaxy

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,ttf,mp3

# (list) List of requirements
# This is crucial! List all Python packages your app imports.
# Example: requirements = python3, kivy, kivymd
requirements = python3, kivy

# (str) Application versioning (method 1)
version = 0.1

# (str) Presplash background color (for Android)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
presplash.bgcolor = #000000
# (str) Orientation (one of landscape, portrait, all or sensor)
orientation = portrait
icon.adaptive_foreground.file_name=%(source.dir)s/Foreground.png
icon.adaptive_background.filename=%(source.dir)s/Background.jpg
# (int) Android SDK target version
android.targetsdk = 33
p4a.branch=master
android.accept_sdk_license = True
android.build_tools_version= 34.0.0


# (int) Minimum API your APK / AAB will support.
android.maxapi=33
android.api=33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# (int) Android NDK API to use. This is the minimum API your app will support,
# it should usually match android.minapi.
android.ndk_api = 21

# (int) Android NDK version to use
android.ndk = 25c

# (list) Permissions (for Android)
# Example: android.permissions = INTERNET, WAKE_LOCK
# Add any permissions your app needs here (e.g., CAMERA, READ_EXTERNAL_STORAGE)
#android.permissions = INTERNET

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# The default options for the other sections like [android], [ios], [desktop],
# etc. are usually fine for a basic Colab build.
# You can uncomment and modify them if you have advanced needs.

[buildozer]
# (str) Path to build artifact storage, absolute or relative to spec file.
build_dir = ./.buildozer
