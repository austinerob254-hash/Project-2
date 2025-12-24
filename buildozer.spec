[app]

# Application title
title = Galaxy

# Package name
package.name = galaxyapp

# Package domain
package.domain = org.galaxy

# Source code directory
source.dir = .

# File extensions to include
source.include_exts = py,png,jpg,kv,ttf,mp3

# Python requirements
requirements = python3,kivy

# App version
version = 0.1

# Orientation
orientation = portrait

# Presplash background color
presplash.bgcolor = #000000

# Adaptive icons
icon.adaptive_foreground.filename = %(source.dir)s/Foreground.png
icon.adaptive_background.filename = %(source.dir)s/Background.jpg


# -------------------------
# ANDROID CONFIGURATION
# -------------------------

# Android API levels
android.api = 33
android.minapi = 21

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Accept SDK licenses automatically
android.accept_sdk_license = True

# SDK & NDK paths (MATCHES build.yml)
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# NDK configuration
android.ndk = 25c
android.ndk_api = 21

# Build tools (MUST match installed version)
android.build_tools_version = 33.0.2

# Log level (2 = debug)
log_level = 2


# -------------------------
# BUILDOZER INTERNAL
# -------------------------

[buildozer]
build_dir = ./.buildozer
