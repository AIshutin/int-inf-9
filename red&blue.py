file = open('output.bmp', mode='wb')
def header(file):
    file.write((ord("B").to_bytes(1, byteorder='little')))
    file.write((ord("M").to_bytes(1, byteorder='little')))
    file.write((54).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little') + 
               (3).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little'))
    
    file.write( (0).to_bytes(4, byteorder='little') )
    file.write( (54).to_bytes(4, byteorder='little') ) #offset
    file.write( (40).to_bytes(4, byteorder='little') ) 
    file.write((0).to_bytes(1, byteorder='little') + 
               (1).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little')) #width
    file.write((0).to_bytes(1, byteorder='little') + 
               (1).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little')) #height
    file.write((1).to_bytes(1, byteorder='little') + (0).to_bytes(1, byteorder='little')) #color plane
    file.write((24).to_bytes(1, byteorder='little') + (0).to_bytes(1, byteorder='little')) #RGB
    file.write( (0).to_bytes(4, byteorder='little') ) #No compresion
    file.write( (0).to_bytes(1, byteorder='little') + (0).to_bytes(1, byteorder='little') + (3).to_bytes(1, byteorder='little') + (0).to_bytes(1, byteorder='little')) #size of stored pixel data
    file.write((195).to_bytes(1, byteorder='little') + 
               (14).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little')) #width
    file.write((195).to_bytes(1, byteorder='little') + 
               (14).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little') + 
               (0).to_bytes(1, byteorder='little')) #height
    file.write( (0).to_bytes(4, byteorder='little') ) #colors
    file.write( (0).to_bytes(4, byteorder='little') ) #colors
header(file)
color =  (13).to_bytes(1, byteorder='little') + (13).to_bytes(1, byteorder='little') + (156).to_bytes(1, byteorder='little')
def g(i, j):
    return max(0, min(255, 255 - i + j))
    
for i in range(256):
    for j in range(256):
        file.write(g(i, j).to_bytes(1, byteorder='little') + (0).to_bytes(1, byteorder='little') + g(255 - i, 255 - j).to_bytes(1, byteorder='little'))
file.close()