from app.menu import Menu
from app.file_manager import FileManager


class TaskAutomation:

    def __init__(self):
        self.menu = Menu()
        self.file_manager = FileManager()

    def run(self):

        while True:
            self.menu.display()
            choice = self.menu.get_choice()

            if choice == 1:
                print("\n📁 Image Mover Selected")
                self.file_manager.move_images()

            elif choice == 2:
                print("\n📧 Email Extractor Selected")
                # Email Extractor will be implemented here

            elif choice == 3:
                print("\n🌐 Webpage Scraper Selected")
                # Web Scraper will be implemented here

            elif choice == 4:
                print("\n👋 Exiting Program...")
                print("Thank you for using Python Task Automation!")
                break


if __name__ == "__main__":
    app = TaskAutomation()
    app.run()