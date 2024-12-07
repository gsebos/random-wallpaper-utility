# Random Unsplash wallpaper on demand for Linux

A quick script to set a random unsplash picture as wallpaper for each of your monitors in linux. It uses feh for X11 and wpaperd (default) or swaybg (with option) for wayland so these programmes need to be installed on the system for this to work (see installation).


# Installation
1. Get an api key from [https://unsplash.com/documentation](https://unsplash.com/documentation)
2. Save the key in a file named `api_key.txt` **in the same folder as the scripts, i.e. inside the python-scripts folder if you have cloned the repo** 
3. Install `swaybg` (used with option) or `wpaperd` (used by default) using your package manager
4. Install `feh` and `xrandr` with your package manager (even if using wayland)
5. Install the python module `requests` using `pip` [in a venv](https://docs.python.org/3/library/venv.html):
Installing in a venv (run commands one by one in a terminal)
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install requests
```
# Other Requirements
- You need a folder structure like `~/Pictures/Wallpapers` as the script will create folders (formatted like `uws_mon[0-9]`) there to save the wallpaper images.
- If using wpaperd, check that your config file is read from `~/.config/wpaperd/` the script will create and save a config file there called `wallpaper_unsplash.toml`

# Usage
Run the script with the venv python path (using defaults):
```
path/to/script/folder/venv/bin/python randomunsplash.py
```

## Options
--collection (string: default is "1053828")
An unsplash collection ID

--waylandsetter (string: default is "wpaperd")
valid options are "swaybg" or "wpaperd"

## Example
Set wallpaper using swaybg from unsplash collection "4819574" in wayland
```
path/to/script/folder/venv/bin/python randomunsplash.py --collection "4819574" --waylandsetter "swaybg"
```

Set wallpaper using wpaperd (in wayland or uses feh in X11) and default collection (1053828)
```
path/to/script/folder/venv/bin/python randomunsplash.py 
```
