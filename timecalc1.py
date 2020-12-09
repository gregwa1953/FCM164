import numpy as np

# read file with one duration per line
with open("hours-11-20-20.txt", "r") as f:
    x = f.read()

print(x)

# Convert string to list of '00:02:12.31'
# I had to drop last item (empty string)
tmp = x.split("\n")[:-1]

print("Variable tmp at this point...")
print(tmp)

# get list of ['00', 02, '12.31']
tmp = [i.split(":") for i in tmp.copy()]

print(f"tmp={tmp}")

np_tims = []
for ls in range(len(tmp) - 1):
    # for ls in range(len(tmp)):
    # create numpy array with floats
    np_tmp = np.array(tmp[ls], dtype=np.float)
    print(f"np_tmp={np_tmp}")
    np_tims.append(np_tmp)

# sum via columns and divide
# hours/24 minutes/60 milliseconds/1000
# X will be a float array [days, hours, seconds]
# Something like `array([ 0.        , 15.68333333,  7.4189    ])`

print(np_tims)

# X = np.array(np_tims).sum(axis=0) / np.array([24, 60, 1000])
X = np.array(np_tims).sum(axis=0)  # / np.array([1, 60, 1000])
print(X)
hrs = X[0]
mins = X[1]
print(hrs, mins)
totalsecs = (hrs * 3600) + (mins * 60)
print(f"TotalSecs: {totalsecs}")
min, sec = divmod(totalsecs, 60)
hours, minutes = divmod(min, 60)
print(f"{hours} hours and {minutes} minutes")
billingratehours = 25
billingrateminutes = 25 / 60
billtotal = (hours * billingratehours) + (minutes * billingrateminutes)
print(f"Bill= ${billtotal:.2f}")
