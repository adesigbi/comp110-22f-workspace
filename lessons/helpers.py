"""Demonstrae defining a modle imported elsewhere."""

THE_ANSWER_TO_LIFE: int = 42

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as module")
print("helpers.py was evaluated")


if __name__ == "__main__":
    main()
else:
    print(f"helpers.py was improted: {__name__} ")