# tkinter-page-storage
A method to store 'pages' for python tkinter. Allows for back and forward naviagtion through pages, whilst still storing each pages held data and for ease on RAM by not storing every page needed before starting the application.

# How it works
- All pages must be a subclass of the PageBase class.
- All subclasses \_\_name\_\_ is taken in the Window manager and then stored with access to a class
- When a page is selected to be shown (provided it is a subclass of PageBase), it is then created and store in the pages list (attr of Window).
- If to many pages are stored, the oldest pages are deleted.
- Traversing through old pages works by holding an index of the current page, then decreasing and increasing that along woth raising the desired page.
- The amount of pages stored can be altered by changing the old_page_limit parameter of the Window class on instantiation.
