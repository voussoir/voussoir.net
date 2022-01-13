rem A width of 905 makes the image occupy the entire horizontal width of the
rem article, at least with the current font settings.
md thumbs
resize *.jpg --width 905 --only-shrink --output .\thumbs\{filename} --quality 50
resize *.png --width 905 --only-shrink --output .\thumbs\{filename} --quality 50
optipng thumbs\*.png
