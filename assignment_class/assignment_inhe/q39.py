# 39. Navigation System

# Methods:

# navigate()

# Implement:

# GoogleMaps
# AppleMaps

import webbrowser
import urllib.parse


class Navigation:

    def navigate(self):
        pass


class GoogleMaps(Navigation):

    def navigate(self):
        print("You are Using Google Maps")
        location = input("Enter which location to see")
        destination = urllib.parse.quote(location)
        url = f"https://www.google.com/maps/search/{destination}"

        webbrowser.open(url)


g = GoogleMaps()
g.navigate()