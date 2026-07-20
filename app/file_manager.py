import os
import shutil


class FileManager:

    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.moved_files = 0

    def create_destination(self):
        """Create destination folder if it doesn't exist."""
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

    def move_images(self):
        """Move all JPG files from source to destination."""

        try:
            self.create_destination()

            files = os.listdir(self.source_folder)

            for file in files:

                if file.lower().endswith(".jpg"):

                    source_path = os.path.join(self.source_folder, file)
                    destination_path = os.path.join(self.destination_folder, file)

                    shutil.move(source_path, destination_path)

                    self.moved_files += 1
                    print(f"📁 Moved: {file}")

            print(f"\n✅ {self.moved_files} image(s) moved successfully.")

        except FileNotFoundError:
            print("❌ Source folder not found.")

        except PermissionError:
            print("❌ Permission denied.")

        except Exception as error:
            print(f"❌ Unexpected Error: {error}")