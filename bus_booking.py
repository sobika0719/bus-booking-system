#bus booking system
#add bus name, bus id ,place, ticket rate ,capacity
#display bus
#destination
#booking

class bus_info:
    def __init__(self):
        self.name=input("Bus Name: ")
        self.bus_id=input("Bus ID: ")
        self.place=input("Place: ")
        self.destination=input("Destination: ")
        self.ticket_rate=int(input("Ticket Rate: "))
        self.capacity=int(input("Capacity: "))

    def getname(self):
        return self.name
    def getbus_id(self):
        return self.bus_id
    def getplace(self):
        return self.place
    def getdestination(self):
        return self.destination
    def getticket_rate(self):
        return self.ticket_rate
    def getcapacity(self):
        return self.capacity

    def setbus_id(self,b):
        self.bus_id=b
    def setplace(self,p):
        self.place=p
    def setdestination(self,d):
        self.destination=d
    def setticket_rate(self,r):
        self.ticket_rate=r
    def setcapacity(self,c):
        self.capacity=c

class booking:
    def __init__(self):
        self.booking_list=[]

    def addbooking(self):
        e=bus_info()
        self.booking_list.append(e)
        print(self.booking_list)

    def display(self):
        for i in self.booking_list:
            print("Bus Name: ",i.getname(),"Bus ID: ",i.getbus_id(),"Place: ",i.getplace(),"Destination: ",i.getdestination(),
                  "Ticket Rate: ",i.getticket_rate(),"Capacity: ",i.getcapacity())

    def search(self):
        name=input("Bus Name: ")
        for i in self.booking_list:
            if name==i.getname():
                 print("Bus Name: ",i.getname(),"Bus ID: ",i.getbus_id(),"Place: ",i.getplace(),"Destination: ",i.getdestination(),
                       "Ticket Rate: ",i.getticket_rate(),"Capacity: ",i.getcapacity())

    def book(self):
        get_id=input("Enter Bus ID: ")
        tickets=int(input("Enter no.of tickets: "))
        for i in self.booking_list:
            if get_id==i.getbus_id():
                if i.getcapacity()>=tickets:
                    i.setcapacity(i.getcapacity()-tickets)
                    print("Booking successful")
                    print("Remaining capacity: ",i.getcapacity())
                elif i.getcapacity()==0:
                    print("Bus is Housefull")
                else:
                    print("Not enough seats available")
                return
        print("Bus ID not found")

b=booking()

a=1
while a!=0:
    a=int(input("Enter 1 to add Bus ,2 for display ,3 for search ,4 for booking,and 0 for exit: "))
    if a==1:
         b.addbooking()
    elif a==2:
        b.display()
    elif a==3:
        b.search()
    elif a==4:
        b.book()
