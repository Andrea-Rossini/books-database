import pandas as pd

db = pd.read_csv("books.csv", on_bad_lines='skip')

f = open("build_db.txt", 'w')

for i in range (0, db.index[-1]):
    f.write ('INSERT INTO books VALUES ("'+str(db.iloc[i][0]).replace("\"", "'")+'","'+str(db.iloc[i][1]).replace("\"", "'")+'","'+str(db.iloc[i][2]).replace("\"", "'")+'","'+str(db.iloc[i][3]).replace("\"", "'")+'","'+str(db.iloc[i][4]).replace("\"", "'")+'","'+str(db.iloc[i][5]).replace("\"", "'")+'","'+str(db.iloc[i][6]).replace("\"", "'")+'","'+str(db.iloc[i][7]).replace("\"", "'")+'","'+str(db.iloc[i][8]).replace("\"", "'")+'","'+str(db.iloc[i][9]).replace("\"", "'")+'","'+str(db.iloc[i][10]).replace("\"", "'")+'","'+str(db.iloc[i][11]).replace("\"", "'")+'");\n')



