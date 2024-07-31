rem A width of 905 makes the image occupy the entire horizontal width of the
rem article, at least with the current font settings.
md thumbs
resize *.jpg --width 1440 --only-shrink --output .\thumbs\{filename} --quality 80
resize *.png --width 1440 --only-shrink --output .\thumbs\{filename} --quality 80
optipng thumbs\*.png
