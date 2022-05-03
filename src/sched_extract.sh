#!/bin/bash

# "THE BEER-WARE LICENSE" (Revision 42):
#
# As long as you retain this notice you can do whatever you want with this stuff.
# If we meet some day, and you think this stuff is worth it, you can buy me a
# beer in return.   
#
# -- grtcdr

CLASS="$1"
FILE="schedule.pdf"

# -- Find the page that contains $CLASS
PAGE="$(pdfgrep -m 1 -n "$CLASS" "$FILE" | cut -f1 -d ":" | head -n1)"

# -- Extract the page and overwrite the original $FILE
pdftk "$FILE" cat $PAGE output - | sponge "$FILE"
