Design:
1) class parking:
     __init__(self):
       ticketnumber = 0
       intimemap = {}
     
     is_full(self):
       return ticketnumber == 1000
       
     get_ticketnumber(self):
       if is_full():
          raise "Sorry, we are out of space"
          
       intime = time()
       ticketnumber = ticketnumber + 1
       intimemap[ticketnumber] = intime
       
       return ticketnumber
       
     leaving_garage(self, n):
       outtime = time()
       
       intime = intimemap[n]
       charge = (outtime-intime) * 2
       return charge      
       
     
    CusA = parking()
    CusA.get_ticket()
 
    ...
    Customer Shopping
    ...
    Customer.leaving_garage()
    
    parking lot data structure: 
    using Python dictionary - > key - ticketnumber, using tuple for value (intime, outtime, space #, parking category)
    parking category means: handicapped, regular, restricted or reserved
    

Tests:
1001 entrances -isfull
Leaving the parking lot without come in
people keep coming inwithout leaving
1st floor isfull scenario, 2nd floor is full scenario
regular cust parked in handicaped space
Only 4 floors avaialble and cust wants to park on 5th floor
Morning time and afternoon time in and out 
summer and winters times on time changes
maximun parking time is 12 hrs and if custumers wants to leave after 13 hrs
30 min parking - hourly parking
59 min 50 sec parking
come in the parking lot and leaves immediatly and come back again and uses the same ticket# (doing this multiple times)
