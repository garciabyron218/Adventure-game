import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
from Character import player


def main(player):
    chapter1_completed = Chapter1.run(player)
    if not chapter1_completed:
        print("\nChapter 1 was not completed.")
        return

    print("\n--- Chapter 2 ---")
    chapter2_completed = Chapter2.run(player)
    if not chapter2_completed:
        print("\nChapter 2 was not completed.")
        return

    print("\n--- Chapter 3 ---")
    chapter3_completed = Chapter3.run(player)
    if not chapter3_completed:
        print("\nChapter 3 was not completed.")
        return

    print("\n--- Chapter 4 ---")
    chapter4_completed = Chapter4.run(player)
    if not chapter4_completed:
        print("\nChapter 4 was not completed.")
        return

    print("\n--- Chapter 5 ---")
    chapter5_completed = Chapter5.run(player)
    if chapter5_completed:
        print("\nCongratulations! You have completed the game.")
    else:
        print("\nChapter 5 was not completed.")


if __name__ == "__main__":
    main(player)
