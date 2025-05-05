#!/usr/bin/python

import sys
import getopt
import traceback

def usage():
    print('Usage: sav-to-srm.py -i <input.sav> -o <output.srm>')
    print('Converts raw GBA SAV files back to SRM format (no padding added)')

def log_error(msg):
    with open("sav-to-srm-error.log.txt", "a") as log:
        log.write(msg + "\n")

def main(argv):
    inputfile = None
    outputfile = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
        for opt, arg in opts:
            if opt == '-h':
                usage()
                sys.exit()
            elif opt in ("-i", "--input"):
                inputfile = arg
            elif opt in ("-o", "--output"):
                outputfile = arg

        if not inputfile or not outputfile:
            raise ValueError("Input or output file not specified.")

        with open(inputfile, "rb") as infile:
            data = infile.read()

        with open(outputfile, "wb") as outfile:
            outfile.write(data)

        print(f"Copied {len(data)} bytes from {inputfile} to {outputfile} with 0 bytes of padding.")

    except Exception as e:
        error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
        log_error(error_msg)
        print("An error occurred. Details were saved to sav-to-srm-error.log.txt")

if __name__ == "__main__":
    main(sys.argv[1:])
