# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

all_prices1 = [0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 1.39, 2.08, 2.08, 2.77,
              2.77, 2.77, 2.77, 2.77, 3.46, 3.46, 4.16, 4.16, 4.16, 4.16, 4.85, 4.85, 4.85, 4.85,
 4.85, 4.85, 4.85, 4.85, 4.85, 4.85, 4.85, 5.54, 5.54, 5.54, 5.54, 6.24, 6.24, 6.24, 6.24, 6.24, 6.93,
              6.93, 40.88, 43.66, 55.44, 55.44, 56.13, 57.52, 71.37, 103.25, 868.97, 957.67, 1394.57, 4545.12]



    # Convert all prices from strings to numbers





print(all_prices1)
print(sorted(all_prices1))
print(all_prices1.sort())

# Make sure products are sorted by price correctly:
assert all_prices1 == sorted(all_prices1) , "Sort by price doesn't work!"