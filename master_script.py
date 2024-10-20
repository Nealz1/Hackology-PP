import concurrent.futures
import threading
# Import the functions from the refactored scripts
from PP_RFR import run_random_forest
from PP_Prophet import run_prophet
from PP_GBR import run_gradient_boosting
from PP_DecisonTree import run_decision_tree

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(run_prophet),
            executor.submit(run_gradient_boosting),
            executor.submit(run_decision_tree),
            #executor.submit(run_random_forest)
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
