import csv
import sys

sizes = []

# load file
with open('battery.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    csvreader.next() # skip header row
    for row in csvreader:
        if len(row) >= 4:
            sizes.append({ "size": row[0], "length": float(row[1]), "width": float(row[2]), "height": float(row[3])})

# get the size we want to find
if len(sys.argv) < 2:
    print 'Not enough arguments'

query = " ".join(sys.argv[1:]).upper()

try:
    found = next(size for size in sizes if size['size'] == query)
except StopIteration:
    print 'Failed to find battery group size named %s. Known sizes are: %s' % (query, ", ".join([i['size'] for i in sizes]))
    sys.exit(1)

print 'Alternative sizes for group %s (%.2f x %.2f x %.2f):' % ( found['size'], found['length'], found['width'], found['height'])

# found a size, filter the collection by tray
tray_fits = [size for size in sizes if size['length'] <= found['length'] and size['width'] <= found['width'] and size['size'] <> query]

for fitment in tray_fits:
    delta_h = fitment['height'] - found['height']
    print "group %s: %.2f x %.2f (change in height: %.2f inches)" % (fitment['size'], fitment['length'], fitment['width'], delta_h)
