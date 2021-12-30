board4 = [
    [0, 2, 1, 0],
    [0, 0, 0, 2],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

boardX = [
    [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 1],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 2, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 2, 0, 2, 0, 0, 0, 1]
]

board12 = [
    [2, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 0],
    [0, 0, 2, 2, 0, 0, 1, 0, 0, 1, 2, 0],
    [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0, 2, 0, 1, 1, 0, 0],
    [1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 2, 0, 0, 1, 2, 0, 0],
    [0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 1, 0],
    [2, 0, 1, 1, 2, 1, 2, 1, 0, 0, 2, 0],
    [2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 1, 2],
    [0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 2, 0, 0, 1, 1, 0, 0, 0]
]


def lazy(value):
    if value == 1:
        return 2
    elif value == 2:
        return 1
    else:
        return None

# identify "local pairs".
def checkpairs(table):
    for i, row in enumerate(table):
        for ii, cell in enumerate(row):
            if cell == 0:
                try:
                    check = row[ii + 1:ii + 3]
                    if 0 not in check and len(check) == 2: #dodgy fix logic. bad.
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {i + 1}:{ii + 1} (right)")
                            return table
                    check = row[ii - 2:ii]
                    if 0 not in check and len(check) == 2:
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {i + 1}:{ii + 1} (left)")
                            return table
                except IndexError:
                    continue

    table = list([list(a) for a in zip(*table)])
    for i, row in enumerate(table):
        for ii, cell in enumerate(row):
            if cell == 0:
                try:
                    check = row[ii + 1:ii + 3]
                    if 0 not in check and len(check) == 2: #dodgy fix logic. bad.
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {ii + 1}:{i + 1} (down)")
                            return list([list(a) for a in zip(*table)])
                    check = row[ii - 2:ii]
                    if 0 not in check and len(check) == 2:
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {ii + 1}:{i + 1} (up)")
                            return list([list(a) for a in zip(*table)])
                except IndexError:
                    continue
    
# check for triplicates (ie 2, 0, 2 and 1, 0, 1)
def checktrip(table):
    for i, row in enumerate(table):
        for ii, cell in enumerate(row):
            if cell == 0:
                try:
                    check = [row[ii + 1], row[ii - 1]]
                    if 0 not in check:
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {i + 1}:{ii + 1}")
                            return table
                except IndexError:
                    continue
    
    table = list([list(a) for a in zip(*table)])
    for i, row in enumerate(table):
        for ii, cell in enumerate(row):
            if cell == 0:
                try:
                    check = [row[ii + 1], row[ii - 1]]
                    if 0 not in check: 
                        if check.count(check[0]) == len(check):
                            table[i][ii] = lazy(check[0])
                            print(f"added {lazy(check[0])} at {ii + 1}:{i + 1}")
                            return list([list(a) for a in zip(*table)])
                except IndexError:
                    continue

# check for "impossibilities"
def testforcollisions(table): # something fucky here.
    for i, row in enumerate(table):
        if row.count(0) == 2:
            for x in range(1, 2):
                temp = row
                for ii, cell in enumerate(temp):
                    if cell == 0:
                        temp[ii] = x
                        break
                for ii, cell in enumerate(temp):
                    if cell == 0:
                        temp[ii] = lazy(x)
                for k, comp in enumerate(table):
                    if i != k:
                        if temp == comp:
                            temp = row
                            for ii, cell in enumerate(temp):
                                if cell == 0:
                                    temp[ii] = lazy(x)
                                    break
                            for ii, cell in enumerate(temp):
                                if cell == 0:
                                    temp[ii] = x
                            table[i] = temp
                            print(f"added pair on row {i}")
                            return table

# check row and column totals
def checkmax(table):
    for i, row in enumerate(table):
        # print(f"{row.count(2)} twos and {row.count(0)} zeros.")
        # print(int(len(row) / 2))
        if row.count(0) > 0:
            if row.count(1) == int(len(row) / 2):
                table[i] = [2 if x == 0 else x for x in table[i]]
                print(f"added 2s to row {i + 1}")
                return table
            if row.count(2) == int(len(row) / 2):
                table[i] = [1 if x == 0 else x for x in table[i]]
                print(f"added 1s to row {i + 1}")
                return table

    table = list([list(a) for a in zip(*table)])
    for i, column in enumerate(table):
        if column.count(0) > 0:
            if column.count(1) == int(len(column) / 2):
                table[i] = [2 if x == 0 else x for x in table[i]]
                print(f"added 2s to col {i + 1}")
                return list([list(a) for a in zip(*table)])
            if column.count(2) == int(len(column) / 2):
                table[i] = [1 if x == 0 else x for x in table[i]]
                print(f"added 1s to col {i + 1}")
                return list([list(a) for a in zip(*table)])
    return None

def runtestloop(table):
    [print(r) for r in table]
    print("")
    i = 0
    while any(0 in rows for rows in table):
        infloop = i
        temp = checkpairs(table)
        if temp:
            table = temp
            i += 1
        temp = checkmax(table)
        if temp:
            table = temp
            i += 1
        temp = checktrip(table)
        if temp:
            table = temp
            i += 1
        # temp = testforcollisions(table)
        # if temp:
        #     table = temp
        #     i += 1
        if infloop == i:
            print(f"Test complete. Halted after {i} steps")
            print("")
            [print(r) for r in table]
            break
    if any(0 in rows for rows in table):
        return
    else:
        print(f"Test completed after {i} steps")
        print("")
        [print(r) for r in table]


if __name__ == "__main__":
    runtestloop(board12)
    # [print(r) for r in board12]
    # print("")
    # board12 = testforcollisions(board12)
    # [print(r) for r in board12]
