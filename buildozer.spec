[app]
title = blocnotedav
package.name = monapplication
package.domain = org.pydroid
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json,mp3,wav
version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
