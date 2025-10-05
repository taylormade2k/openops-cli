import argparse
from .core.logic import run

def main():
    parser = argparse.ArgumentParser(description="OpenOps Module CLI")
    parser.add_argument("--input", help="Path to input data file")
    parser.add_argument("--output", help="Optional output path")
    args = parser.parse_args()

    run(args.input, args.output)

if __name__ == "__main__":
    main()
