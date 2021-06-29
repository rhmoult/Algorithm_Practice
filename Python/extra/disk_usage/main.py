import os


def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)   # Account for direct usage
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    print ('{0:<7}'.format(total), path)
    return total


def main():
    used = disk_usage('c:/Users/Public')
    print('Used: ', used)

if __name__ == '__main__':
    main()
