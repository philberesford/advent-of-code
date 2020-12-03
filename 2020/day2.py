import pandas as pd

def main():
    dataFrame = pd.read_csv("day2.data", header=None, delimiter=r"[-\s]+", engine="python")
    part1(dataFrame)
    part2(dataFrame)
    
def part1(df):  
    transformed = df.apply(characterCounter, axis=1)
    minColoumn = transformed[0]
    maxColumn = transformed[1]
    matchingCharacterCountColumn = transformed[4]
    filter = (minColoumn <= matchingCharacterCountColumn) & (matchingCharacterCountColumn <= maxColumn) # The number of matching characters must be within the min/max range
    printRowCount(df, filter)
    
def part2(df):  
    transformed = df.apply(positionCounter, axis=1)
    filter = (transformed[5] == 1)  # There must only be one character in the specified positions
    printRowCount(df, filter)

def printRowCount(df, filter):
    filtered = df[filter]
    rowCount = filtered.shape[0]
    print(rowCount) # Done

def characterCounter(df):
    """Adds a column to the dataframe indicating the number of characters in the password that conform to the policy"""
    min = str(df[0])
    max = str(df[1])
    char =  str(df[2]).replace(":", "")
    password = str(df[3])
    df[4] = password.count(char)    # Add on the number of characters found in the password field
    return df

def positionCounter(df):
    """Adds a column to the row in the dataframe indicating the number of characters that are in the position specified in the policy"""
    pos1 = int(str(df[0]))
    pos2 = int(str(df[1]))
    char =  str(df[2]).replace(":", "")
    password = str(df[3])
    positionalCharCount = 0
    if password[pos1-1] == char:
        positionalCharCount += 1
    if password[pos2-1] == char:
        positionalCharCount += 1
    df[5] = positionalCharCount

    return df

main()
