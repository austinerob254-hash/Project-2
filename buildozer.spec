[app]

title = Galaxy
package.name = galaxyapp
package.domain = org.galaxy

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,mp3

version = 0.1
orientation = portrait

requirements = python3,kivy

presplash.bgcolor = #000000

icon.adaptive_foreground.filename = %(source.dir)s/Foreground.png
icon.adaptive_background.filename = %(source.dir)s/Background.jpg

# -------------------------
# ANDROID CONFIGURATION
# -------------------------

android.api = 33
android.minapi = 21

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

# IMPORTANT: Do NOT hardcode SDK/NDK paths for GitHub
# Let Buildozer manage them
android.ndk = 25c
android.ndk_api = 21
android.build_tools_version = 33.0.2

log_level = 2

# -------------------------
# BUILDOZER INTERNAL
# -------------------------

[buildozer]
build_dir = .buildozer
