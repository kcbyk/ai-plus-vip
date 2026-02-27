[app]
title = AI Plus VIP
package.name = aiplusvip
package.domain = org.senol
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,opencv-python,numpy,requests
orientation = landscape
fullscreen = 1
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
services = aimbot:aimbot_logic.py
