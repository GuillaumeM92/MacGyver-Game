# initializing all the squares for the 16x16 grid
squares = list(range(256))

# splitting the squares into 16 rows of 16 squares each
row_00 = squares[0:16]
row_01 = squares[16:32]
row_02 = squares[32:48]
row_03 = squares[48:64]
row_04 = squares[64:80]
row_05 = squares[80:96]
row_06 = squares[96:112]
row_07 = squares[112:128]
row_08 = squares[128:144]
row_09 = squares[144:160]
row_10 = squares[160:176]
row_11 = squares[176:192]
row_12 = squares[192:208]
row_13 = squares[208:224]
row_14 = squares[224:240]
row_15 = squares[240:256]

# building the grid
grid = [row_00, row_01, row_02, row_03, row_04, row_05, row_06, row_07, row_08,
        row_09, row_10, row_11, row_12, row_13, row_14, row_15]
