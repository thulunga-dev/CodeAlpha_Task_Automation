from tkinter import Tk
from tkinter.filedialog import askdirectory


class FileDialog:

    def select_folder(self, title):

        root = Tk()
        root.withdraw()

        folder = askdirectory(title=title)

        root.destroy()

        return folder