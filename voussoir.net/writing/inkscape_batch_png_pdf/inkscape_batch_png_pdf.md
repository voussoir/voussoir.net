Batch png to pdf with Inkscape & PDFtk
====================================================

Today, I had 57 png images of QR codes, and needed to create a single pdf document where each page contained a single QR code with the file's name shown centered above the QR. From start to finish, without planning ahead, it took me 23 minutes, a pace which would have required me to do 1 image every 24 seconds if I were to do them by hand. Plus, any subsequent tweaks can be done in a flash.

I used [Inkscape](https://inkscape.org/) and [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/).

1. **Create one svg manually**

    1. Open Inkscape and adjust the document page size to your liking.
    2. Add the image to the page. I chose to embed the image rather than linking, but in retrospect, linking would have been the correct choice.
    3. Add the text box to the page. With the text selected, press CTRL+SHIFT+T to open the Text and Font menu, choose Center alignment, and click apply.
    4. Arrange the image and label to your liking.
    5. Save the document.

2. **Generate svgs for all other images**

    1. Open the template svg in a text editor and copy everything.
    2. Create a Python file, and start by:

        ```Python
        TEMPLATE = '''
        paste the svg file here
        '''.strip()
        ```
    3. If you chose to embed the image, it will be stored as base64. In that case, delete the actual base64 text, but leave the `data:image/png;base64,` prefix. After the comma, add `{image_base64}`.

        `xlink:href="data:image/png;base64,{image_base64}"`

        If you chose to link the image, you'll find the file path. Replace it with `{image_path}`.

        `xlink:href="{image_path}"`

    4. Find the element that contains the label text, and replace the text with `{label_text}`.

    5. The rest of the Python script was as follows:

        ```Python
        import base64
        import glob

        filenames = glob.glob('*.png')
        for filename in filenames:
            label_text = f'...' # do some transformations on the filename
            data = open(filename, 'rb').read()
            image_base64 = base64.b64encode(data).decode('ascii')
            svg = TEMPLATE.format(image_base64=image_base64, label_text=label_text)
            open(filename.replace('.png', '.svg'), 'w').write(svg)
        ```

        Using linking instead of embedding, this would have been more like:

        ```Python
        for filename in filenames:
            label_text = f'...' # do some transformations on the filename
            svg = TEMPLATE.format(image_path=filename, label_text=label_text)
            open(filename.replace('.png', '.svg'), 'w').write(svg)
        ```

3. **Convert svgs to pdf**

    On Windows, a for-loop in the command line looks like this:

    `for %x in (*.png) do inkscape --without-gui --export-pdf=%~nx.pdf %~nx.svg`

4. **Combine all pages into single pdf**

    `pdftk *.pdf cat output "all.pdf"`

If I need to make any updates to the template, I can

1. Open any of the svgs and make the changes.
2. Copy it back into the Python file and redo the `{templating}`.
3. Run the python script, inkscape export loop, and pdftk merger.
