from importlib import util


class PackageError(Exception):
    def __init__(self, mess) -> None:
        super().__init__(f"PackageError: {mess}")


def test_package() -> dict:
    packages = ["pandas", "requests", "matplotlib", "numpy"]
    res = [util.find_spec(pack) for pack in packages]
    if None in res:
        raise PackageError("Some package are missing. You need to import or"
                           " install pandas requests matpolib and numpy")
    return {
        "pandas": packages[0],
        "requests": packages[1],
        "matplotlib": packages[2]
    }


def main() -> None:
    try:
        res = test_package()
        import pandas as pd
        import requests
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
        res1 = {
            "pandas": "Data manipulation ready",
            "requests": "Data manipulation ready",
            "matplotlib": "Data manipulation ready"
        }
        versions = {
            "pandas": pd.__version__,
            "requests": requests.__version__,
            "matplotlib": matplotlib.__version__
        }
        print("LOADING STATUS: Loading programs...\n")
        print("Checking dependencies:")
        for key in res1:
            print(f"[{'OK' if res[key] is not None else 'KO'}] {res[key]} "
                  f"({versions[key]}) - {res1[key]}")
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        data = np.random.normal(size=1000)
        print("Generating visualization...")
        df = pd.DataFrame({"values": data})
        plt.hist(df["values"])
        plt.savefig("analysis.png")
        print("\nAnalysis complete!")
        print("Results saved to: analysis.png")
    except PackageError as e:
        print(e)
    except Exception as e:
        print(f"Type Error: {e.__class__.__name__}")
        print(f"Message Error {e}")


if __name__ == "__main__":
    main()
