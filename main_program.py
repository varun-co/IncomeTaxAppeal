import os
import make_benchtxt_file
def main():
    bench = make_benchtxt_file.get_benches()
    if type(bench) != type(list):
        print('unable to get benches please try later')
        exit()


if __name__ == '__main__':
    main()
