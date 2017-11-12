import BMP_Reader as pict
if __name__ == "__main__":
    import sys
    print(sys.argv)
    fin = open(sys.argv[1])
    q = pict.readFromFile(fin)
    fin.close()
    print(q)
    
    