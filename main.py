from app.menu import Menu
from app.file_manager import FileManager


class TaskAutomation:

    def __init__(self):
        self.menu = Menu()
        self.file_manager = FileManager(
            "images/source",
            "images/destination"
        )

    def run(self):

        while True:
            self.menu.display()
            choice = self.menu.get_choice()

            if choice == 1:
                print("\n📁 Image Mover Selected")
                self.file_manager.move_images()

            elif choice == 2:
                print("\n📧 Email Extractor Selected")

            elif choice == 3:
                print("\n🌐 Webpage Scraper Selected")

            elif choice == 4:
                print("\n👋 Exiting Program...")
                break


if __name__ == "__main__":
    app = TaskAutomation()
    app.run()