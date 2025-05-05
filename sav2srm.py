#!/usr/bin/python

import sys, getopt

def usage():
    print('Usage: sav2srm.py -i <input.sav> -o <output.srm>')
    print('Converts raw GB SAV files back to SRM format')

def main(argv):
    inputfile = None
    outputfile = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg

    if not inputfile or not outputfile:
        usage()
        sys.exit(2)

    with open(inputfile, "rb") as infile, open(outputfile, "wb") as outfile:
        data = infile.read()

        # Remove the 0xFF padding bytes at the beginning (if any)
        padding_length = 0
        while len(data) > 0 and data[0] == 0xFF:
            padding_length += 1
            data = data[1:]  # Remove the leading 0xFF bytes

        # Write padding at the start of the .srm file.
        outfile.write(b'\xFF' * padding_length)
        outfile.write(data)

        print(f"Converted {len(data)} bytes from {inputfile} to {outputfile}, added {padding_length} bytes of padding.")

if __name__ == "__main__":
    main(sys.argv[1:])
