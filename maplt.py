#maplt.py Launches a map in browser using address from command line and clip board

import webbrowser,sys,pyperclip 

if len(sys.argv)>1:
    #Get address from command line
    address=''.join(sys.argv[1:])
else:
    #Get address from clipbord
    address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+ address)
