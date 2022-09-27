"""Examples of importing Pyhton."""

from lessons import helpers


def main () -> None:
    """Entrypoint of program"""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER_TO_LIFE}")


if __name__ == "__main__":
    main()