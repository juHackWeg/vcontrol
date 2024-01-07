#!/usr/bin/python3

def add(fig1: int, fig2: int) -> int:
    return fig1 + fig2


def sub(fig1: int, fig2: int) -> int:
    return fig1 - fig2


if __name__ == '__main__':
    print(f"Addition (5+5)      {add(5,5)}")
    print(f"Subtraction (5+5)   {sub(5,5)}")
