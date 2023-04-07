class trainticket:
    def traininfo(self,tname,tprice,tavailtkt,tstation):
        self.tname=tname
        self.tprice=tprice
        self.tavailtkt=tavailtkt
        self.tstation=tstation
class bank(trainticket):
    def gst(self):
        self.gst=5
class passenger(bank):
    def getinfo(self):
        tname=input("enter your train name:")
        num=int(input("enter your number of tickets:"))
        if(tname==tname and tavailtkt>num):
            print("ticket details")
            print("train name:",self.tname)
            print("ticket price:",self.tprice)
            print("gst percentage:",self.gst)
            print("total no of tkts:",num)
            amount=self.tprice*num
            gstamount=self.gst*num
            totalamount= amount+gstamount
        else:
            print("invalid statement try again:")
p=passenger()
p.traininfo("pandian",855,22,"maduarai")
p.gst()
p.getinfo()            
		
			