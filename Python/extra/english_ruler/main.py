def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)    # Stop when length drops to 0
        draw_line(center_length)            # Recursively draw top ticks
        draw_interval(center_length - 1)    # Recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')            # Draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)     # Draw interior ticks for inch
        draw_line(major_length, str(j))     # Draw inch j line and label


def main():
    draw_ruler(5, 3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
