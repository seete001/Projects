import csv

with open('test.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    total = 0
    processed_date = []
    next(reader)
    for row in reader:
        name = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total += price * quantity
        #print(f"{name} : {total}")
        processed_date.append([name, quantity, total]) 

    with open('processed_data.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Quantity', 'Total'])
        writer.writerows(processed_date)
    print("Processed data has been written to processed_data.csv")
    