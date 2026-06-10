# create sales data cleaner  and analyze
try:
   with open ("FoodSalesData.txt","r") as file:
        data=file.readlines()
       # print(data)
        total_len=len(data) 
       # print(total_len)
        
# all columns in food sales data...
        columns=data[0].strip().split(",")
        print(columns)

#  all food sales data... 
        rows=data[1:total_len]
        for line in rows:
         row = line.strip().split(",")
         print(row)

# Missing value in data
        for line in rows:
           row = line.strip().split(",")
            
           for i in range(len(row)):
             if row[i] == "":
               print("Missing value found in row :", row, "at column:", columns[i])
       
# only pizza sales detail...
        for line in rows:
           row=line.strip().split(",")
        
           for pizza in range(len(row)):
             if row[pizza]=="Pizza":
              print("Only pizza detail are:" , row)
    

    
except FileNotFoundError:
   print("File does not exist.....")

