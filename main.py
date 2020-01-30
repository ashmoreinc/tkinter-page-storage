import tkinter as tk


class Window(tk.Tk):
    """Main window class, controls pages and navigation"""
    def __init__(self, old_page_limit=3, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Pages Test")

        # Container to hold all future pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Store page names known to be Pages
        self.page_names = {}
        for page in PageBase.__subclasses__():
            self.page_names[page.__name__] = page

        # Page management Attrs
        self.pages = []
        self.old_page_limit = old_page_limit
        self.current_page_index = 0

        # Show first page on initialisation
        self.show_page(Page1.__name__)

    def show_page(self, page_name):
        """Create and raise a new page to top"""
        # Account for page name not existing
        if page_name not in self.page_names:
            return False

        # Create the new page
        new_page = self.page_names[page_name](self.container, self)
        new_page.grid(row=0, column=0, sticky="nsew")

        # Run initialisation functions
        new_page.initialise()
        new_page.page_update()

        # Raise page
        new_page.tkraise()

        # Add page to pages list
        self.pages.append(new_page)

        # Check if the list exceeds the limit
        if len(self.pages) > self.old_page_limit:
            del[self.pages[0]]  # Remove the first element

        # Now set the page index
        self.current_page_index = len(self.pages) - 1

        return True

    def previous_page(self):
        """Show the previous page"""

        # Account for being the first page.
        if self.current_page_index == 0:
            return False

        # Change the page index
        self.current_page_index -= 1

        # Raise the page
        page = self.pages[self.current_page_index]
        page.tkraise()

        return True

    def next_page(self):
        """Show the next page"""

        # Account for their being no more pages ahead
        if self.current_page_index + 1 >= len(self.pages):
            return False

        # Increase the page index
        self.current_page_index += 1

        # Raise the page
        page = self.pages[self.current_page_index]
        page.tkraise()

        return True


class PageBase(tk.Frame):
    """Basis for the page classes"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Create the back and forward button
        section = tk.Frame(self)
        section.pack(side="top", fill="x", expand=True)

        # Back button
        tk.Button(section, text="back", command=controller.previous_page).pack(side="left", fill="y")

        # Next button
        tk.Button(section, text="next", command=controller.next_page).pack(side="right", fill="y")

    def initialise(self):
        """To be overridden with tasks that must be completed on class initialisation by the controller class Window"""
        pass

    def page_update(self):
        """To be overridden with tasks that must be completed when this page is switched too"""
        pass


# Test Pages
class Page1(PageBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        tk.Label(self, text="I am page 1").pack(side="top", fill="x", pady=10, padx=10)

        # p1 btn
        tk.Button(self, text="Page 1", command=lambda: controller.show_page(Page1.__name__)).pack(side="top", fill="x")
        # p2 btn
        tk.Button(self, text="Page 2", command=lambda: controller.show_page(Page2.__name__)).pack(side="top", fill="x")
        # p3 btn
        tk.Button(self, text="Page 3", command=lambda: controller.show_page(Page3.__name__)).pack(side="top", fill="x")


class Page2(PageBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        tk.Label(self, text="I am page 2").pack(side="top", fill="x", pady=10, padx=10)

        # p1 btn
        tk.Button(self, text="Page 1", command=lambda: controller.show_page(Page1.__name__)).pack(side="top", fill="x")
        # p2 btn
        tk.Button(self, text="Page 2", command=lambda: controller.show_page(Page2.__name__)).pack(side="top", fill="x")
        # p3 btn
        tk.Button(self, text="Page 3", command=lambda: controller.show_page(Page3.__name__)).pack(side="top", fill="x")


class Page3(PageBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        tk.Label(self, text="I am page 3").pack(side="top", fill="x", pady=10, padx=10)

        # p1 btn
        tk.Button(self, text="Page 1", command=lambda: controller.show_page(Page1.__name__)).pack(side="top", fill="x")
        # p2 btn
        tk.Button(self, text="Page 2", command=lambda: controller.show_page(Page2.__name__)).pack(side="top", fill="x")
        # p3 btn
        tk.Button(self, text="Page 3", command=lambda: controller.show_page(Page3.__name__)).pack(side="top", fill="x")


if __name__ == "__main__":
    print("Tkinter page storage test.")
    win = Window(old_page_limit=10)
    win.mainloop()