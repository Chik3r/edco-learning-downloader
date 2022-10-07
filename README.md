# Edco Learning Downloader
A tool to download a book from Edco Learning as images. The images can then be converted to a `.pdf` file.

`download_chapter.py` requires various things (all of them can be found by opening the Network menu in Dev Tools and then loading a book):
 - `token`: The token used to get the images. Found in the url to the images
 - `cookies`: The cookies that are sent to the `GetPages` endpoint.
 - `bookId`: The id of the book, can be found in the book URL when you open it.
 - The output images will be stored in a folder next to the script. The folder will have the book id as its name.
 - The naming scheme of the images is `{chapterId}-{pageId}-{imageNumber}.jpg`
 
 `convert_to_pdf.py` converts the images in a folder next to it to a `.pdf` file.
  - `bookId`: The id of the book. (The folder name)
  - The output pdf will be inside the folder.
