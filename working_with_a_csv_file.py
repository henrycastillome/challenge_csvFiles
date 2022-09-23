import csv

filename="Summer22_FootballTransfers.csv"

fields=[]
rows=[]


with open (filename,'r') as csvfile:
    csvReader=csv.DictReader(csvfile)
    fields=next(csvReader) #extracting the names of the columns
    print('Field names are:' + ', '.join(field for field in fields))

    data=[row for row in csvReader] # to pass multiple time the csv file


    for row in data:
        if row["position"]=='Goalkeeper':
             print("these are the GKs traded this summer-------->", row["name"],"--", row["country_new_club"])
        
        

    for row in data:
        if row["country_new_club"]=="Spain" and row ["age"]<=str(25):
            print("These are the player traded to Spain under 25 years old --->", row["name"],"--",row["age"])

    
    
           
            

    

   

    
    
    
    
    
    
    
       

