import webbrowser
url = 'http://docs.python.org/'

webbrowser.open(url, new=0, autoraise=True)

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)