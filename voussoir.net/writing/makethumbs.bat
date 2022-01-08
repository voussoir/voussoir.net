rem A width of 905 makes the image occupy the entire horizontal width of the
rem article, at least with the current font settings.
md thumbs
resize *.jpg 905 0 --only-shrink --destination thumbs --inplace --quality 50
resize *.png 905 0 --only-shrink --destination thumbs --inplace --quality 50
optipng thumbs\*.png
