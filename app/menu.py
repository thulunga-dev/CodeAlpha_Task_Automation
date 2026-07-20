class Menu:
    """Handles the application menu."""

    def display(self):
        """Display the main menu."""
        print("\n" + "=" * 40)
        print("      PYTHON TASK AUTOMATION")
        print("=" * 40)
        print("1. Move JPG Files")
        print("2. Extract Email Addresses")
        print("3. Scrape Webpage Title")
        print("4. Exit")
        print("=" * 40)

    def get_choice(self):
        """Get a valid menu choice from the user."""

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))

                if 1 <= choice <= 4:
                    return choice

                print("❌ Please enter a number between 1 and 4.")

            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")

            except KeyboardInterrupt:
                print("\n\n⚠ Program interrupted by user.")
                return 4

            except Exception as error:
                print(f"Unexpected Error: {error}")