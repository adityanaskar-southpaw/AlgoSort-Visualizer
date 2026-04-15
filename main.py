from performance import run_analysis
from visualizer import run_visual

def main():
    while True:
        print("\n===== SORTING VISUALIZER PROJECT =====")
        print("1. Run Performance Analysis (Graphs)")
        print("2. Run Sorting Visualization (Animation)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nRunning Performance Analysis...\n")
            run_analysis()

        elif choice == "2":
            print("\nStarting Visualization...\n")
            run_visual()

        elif choice == "3":
            print("\nExiting... Done 👍")
            break

        else:
            print("\nInvalid choice, try again!")

if __name__ == "__main__":
    main()