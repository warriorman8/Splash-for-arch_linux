import os

desktop_icon= open("splash-flow.desktop","w")

desktop_icon.write(r'''
[Desktop Entry]

# The type as listed above
Type=Application

Version=1.0

# The name of the application
Name=splash-flow

# A comment which can/will be used as a tooltip
Comment=Openfoam CFD GUI wrapper.

''')
current_directory = os.getcwd()

desktop_icon.write(r'''Path=''')
desktop_icon.write(current_directory)
desktop_icon.write(r'''/Source/

# The executable of the application, possibly with arguments.
Exec=pypy3 splash.py

# Describes whether this application needs to be run in a terminal or not
Terminal=true

# Describes the categories in which this entry should be shown
Categories=Science; education

# The name of the icon that will be used to display this entry
''')
desktop_icon.write(r'''Icon=''')
desktop_icon.write(current_directory)
desktop_icon.write(r'''/Resources/Logos/simulitica_icon_logo.png

''')