#!/bin/bash

# "THE BEER-WARE LICENSE" (Revision 42):
#
# As long as you retain this notice you can do whatever you want with this stuff.
# If we meet some day, and you think this stuff is worth it, you can buy me a
# beer in return.   
#
# -- grtcdr

FILE="schedule.pdf"
CLASS="$1"
OUT="schedule.pdf"

## Find the page that contains $CLASS
PAGE="$(pdfgrep -n "$CLASS" "$FILE" | cut -f1 -d ":" | head -n1 | tr '\n' ' ')"

## Extract pages to new file in original directory
pdftk "$FILE" cat $PAGE output - | sponge "$FILE"
