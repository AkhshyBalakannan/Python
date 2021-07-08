import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("physics", help="physics marks")  # This POSITION ARGS
    # This POSITION ARGS
    parser.add_argument("chemistry", help="chemistry marks")
    parser.add_argument("maths", help="maths marks")  # This POSITION ARGS

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    print("Result:", (
        int(args.physics) + int(args.chemistry) + int(args.maths)
    ) / 3)

    # python main.py 60 70 90

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="physics marks")  # Optional Args
    parser.add_argument("--chemistry", help="chemistry marks")  # Optional Args
    parser.add_argument("--maths", help="maths marks")  # Optional Args

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    print("Result:", (
        int(args.physics) + int(args.chemistry) + int(args.maths)
    ) / 3)

    # python main.py --physics 60 --chemistry 70 --maths 90
