import csv
import oracles_headers
cols = oracles_headers.oracles_columns

def output_headers(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print("columns = {")
            for entry in row:
                print(f"    '{entry}',")
            print("}")
            break

def getCell(row, col):
    return row[cols[col]]

if __name__ == "__main__":
    #output_headers('../raw/2014_OraclesElixir.csv')
    
    with open('../event/EU_LCS_Spring_2014_Playoffs.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{getCell(row, 'Player')}: {getCell(row, 'Champion')}")