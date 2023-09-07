#!/usr/bin/python3
if __name__ == "__main__":
    """Print all the hidden directories."""
    import hidden_4

    for x in dir(hidden_4):
        if x[:2] != "__":
            print(x)
