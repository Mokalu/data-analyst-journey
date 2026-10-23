Day 1 Self check 

QUESTIONS
What does = do in price= 500?- = stores a value under a name
Why does "5" + 5 fail, but "5" + "5" work? - Because the first are str and int respectively. they can't be calculated together. The second are both recognized as text(str). so, that can work. the answer for the second will be 55 instead of 10 because python repeats texts.
What does "20" * 3 give ? It gives 202020. because python interpretes the "20" as text. the answer means it's multiplied by 3. This answer is not mathematically correct, which can cause discrepancies to business results.
Which line of an error message do you read first? The last line, because, you're able to detect the actual problem and the cause of the error at the last line.

DAY 2 Notes (Lists and Dictionaries)
List is one variable that holds several items in order inside []
Dictionary is one variable that holds key and value pairs inside{}
Each item has a position number(index) starting from zero. products (0) gets the first item while product (-1) gets the last item
.append adds an item to the list
len() counts the number of items, so the last index is always len() -1.
you find a value by it's key(label), not it's position (index)
IndexError : you asked a list for a position that doesn't exist
KeyError : You asked a dictionary for a key(label) that isn't in it
A CSV ROW is like a dictionary while a column is like a list

DAY 3 Notes (IF AND LOOP STATEMENTS)
A loop repeats an action for every item
An if/else makes a decision
Combines, they let code check every item against a rule
indentation tells item which lines belong to which block
= stores a value, while == asks a question. "Are these two things equal? The answer is always true or false.

DAY 4 Notes (Functions)
Def creates a function: It is basically a set of steps saved under a name
Defining (def apply_discount(...)) writes the function.
Calling (apply_discount(5000,10)) runs it
A function that is defined but never called, does nothing.
A parameter is a placeholder for an input, like price or discount_percent. Each call fills it with real value.
Print shows a value on the screen. Nothing comes back.
return hands the value back so you can store it (result + apply_discount (5000, 10)) and use it later.

My formula
apply_discount returns price - price * discount_percent / 100.

DAY 5 NOTES: Inspecting data
A data frame is a table of rows and columns, loaded with pd.read_csv()
.head() shows the first five rows.
.shape gives (rows,columns).
.columns lists names.
.dtypes shows types.
.describe() gives statistics.
.value_counts() counts how often each value appears.
df["Column"] selects a column. A wrong name gives a KeyError. Always copy names from df.columns.
My data: video game sales, 1034 rows and 9 columns. Most common genre: Simulation (23)

DAY 6: Cleaning
NaN means a missing value. isnull().sum() counts them per column.
Fixes: drop rows (few affected), fill with the average (numeric, random gaps), fill with "Unknown" (text).
Publisher had 209 missing. I filled with the "Unknown" because it is text and dropping would lose valid sales figures.
.str.strip() removes stray spaces. drop_duplicates() removes repeated rows (mine had 0)
to_csv("sales_clean.csv",index=False) saves the cleaned file.

DAY 7 & 8 Notes:
groupby splits the table into groups ND CALCULATES ONE NUMBER PER GROUP.
sort_values(ascending=False) puts the biggest first.
Filtering with df[df["Global"] > 5] keeps only matching rows.
A new column is made by assigning to a name: df["NA_share"] = 38.829145546247396
My findings: top genre Action, top region Europe, 23 games sold over 5