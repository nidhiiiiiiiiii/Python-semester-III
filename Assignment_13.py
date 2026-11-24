import threading
import time


def compute_squares(numbers: list[int]) -> None:
    """Task 1: Compute and display squares of numbers with a simulated delay."""
    for n in numbers:
        time.sleep(0.4)
        print(f"[Squares Thread] {n}^2 = {n * n}")


def print_countdown(start: int) -> None:
    """Task 2: Print a countdown from a starting integer."""
    for count in range(start, 0, -1):
        time.sleep(0.5)
        print(f"[Countdown Thread] T-minus {count}...")
    print("[Countdown Thread] Liftoff!")


def process_items(items: list[str]) -> None:
    """Task 3: Simulate processing a batch of items concurrently."""
    for item in items:
        time.sleep(0.3)
        print(f"[Processor Thread] Processed '{item.upper()}'")


def main() -> None:
    start_time = time.perf_counter()

    # Create threads for different tasks
    squares_thread = threading.Thread(
        target=compute_squares,
        args=([1, 2, 3, 4, 5],),
        name="SquaresWorker",
    )
    countdown_thread = threading.Thread(
        target=print_countdown,
        args=(4,),
        name="CountdownWorker",
    )
    processor_thread = threading.Thread(
        target=process_items,
        args=(["alpha", "beta", "gamma", "delta", "epsilon"],),
        name="ProcessorWorker",
    )

    threads = [squares_thread, countdown_thread, processor_thread]

    # Start all threads concurrently
    for t in threads:
        t.start()

    # Wait for all threads to finish before continuing
    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start_time
    print(f"\nAll concurrent tasks completed in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    main()