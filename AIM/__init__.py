#Zsombor Papp
class num:
	def len(self):
		return(len(self.val))
	def __init__(self, string, decimalPoint):
		self.val=[]
		for i in range(len(string)):
			self.val.append(int(string[i]))
		self.dP=int(decimalPoint)
	def add(self, otherNum):
		if((len(self.val)-self.dP)<(len(otherNum.val)-otherNum.dP)):
			for i in range(len(otherNum.val)-otherNum.dP-len(self.val)+self.dP):
				self.val.append(0)
		if(self.dP<otherNum.dP):
			for i in range(otherNum.dP-self.dP):
				self.val.insert(0,0)
			self.dP=otherNum.dP
		c=0
		dPDif=self.dP-otherNum.dP
		for i in range (min(len(self.val),len(otherNum.val))-1,dPDif-1,-1):
			self.val[i]+=otherNum.val[i-dPDif]+c
			c=self.val[i]//10
			self.val[i]%=10
		if c!=0:
			self.val.insert(0,c)
			self.dP+=1
		self.removeZerosBack();
	def multiplyNum(self, otherNum):
		c=[0]
		for i in range(len(self.val)+len(otherNum.val)):
			c.append(0)
		for i in range(len(self.val)):
			for j in range(len(otherNum.val)):
				c[i+j]+=self.val[i]*otherNum.val[j]
		d=0
		for i in range(len(c)-1,-1,-1):
			c[i]+=d
			d=c[i]//10
			c[i]%=10
		while d!=0:
			c.insert(0,d%10)
			d//=10
		self.val=c
		self.dP+=otherNum.dP-1
		self.removeZerosBack();
	def multiplyInt(self,integer):
		c=0
		for i in range (len(self.val)-1,-1,-1):
			self.val[i]=(self.val[i]*integer)+c
			c=self.val[i]//10
			self.val[i]%=10
		while c!=0:
			self.val.insert(0,c%10)
			c//=10
			self.dP+=1
		self.removeZerosBack();
	def isBigger(self,otherNum):
		if(self.dP>otherNum.dP):
			return True
		elif(self.dP<otherNum.dP):
			return False
		else:
			i=0;
			maxN=min(len(self.val),len(otherNum.val))
			while (self.val[i]==otherNum.val[i]) and (maxN-1>i):
				i+=1
			if(i==maxN-1):
				return len(self.val)>len(otherNum.val)
			else:
				return self.val[i]>otherNum.val[i]
	def subtract(self,otherNum):
		if((len(self.val)-self.dP)<(len(otherNum.val)-otherNum.dP)):
			for i in range(len(otherNum.val)-otherNum.dP-len(self.val)+self.dP):
				self.val.append(0)
		if(self.dP<otherNum.dP):
			for i in range(otherNum.dP-self.dP):
				self.val.insert(0,0)
			self.dP=otherNum.dP
		c=0
		dPDif=self.dP-otherNum.dP
		lDif=len(self.val)-len(otherNum.val)
		for i in range (min(len(self.val),len(otherNum.val))-1,dPDif-1,-1):
			self.val[i]-=otherNum.val[i-dPDif]-c
			c=self.val[i]//10
			self.val[i]%=10
		self.removeZerosFront();
		self.removeZerosBack();
	def removeZerosFront(self):
		while (self.val[0]==0) and (len(self.val)>1):
			self.val.pop(0)
			self.dP-=1
		if self.val[0]==0:
			self.dP=1
	def removeZerosBack(self):
		while(self.val[len(self.val)-1]==0) and (len(self.val)>1):
			self.val.pop(len(self.val)-1)
		if self.val[len(self.val)-1]==0:
			self.dP=1
	def divide(self,otherNum,maxAcc):
		c=otherNum.getVal()
		d=otherNum.getDP()
		a=[]
		ot=num("0","0")
		dpr=self.dP-otherNum.dP
		self.dp=otherNum.getDP()
		if(not(otherNum.isBigger(self))):
			dpr+=1
		else:
			self.dP+1;
		while self.val[0]!=0 and len(a)<maxAcc:
			i=9
			ot.modVal(c)
			ot.modDP(d)
			print(c)
			print(ot.val)
			ot=multiplyByInt(ot,i)
			while ot.isBigger(self):
				print(c)
				ot.modVal(c)
				ot.modDP(d)
				i-=1;
				ot.multiplyInt(i)
			a.append(i)
			self.subtract(ot)
			self.dP+=1
		self.val=a
		self.dP=dpr
	def modVal(self,val):
		self.val=val
	def modDP(self,dP):
		self.dP=dP
	def getVal(self):
		return self.val
	def getDP(self):
		return self.dP
	def toString(self):
		s=""
		for i in range(len(self.val)):
			s+=str(self.val[i])
		s=s[:self.dP] + "." + s[self.dP:]
		return s
def multiplyByInt(a,integer):
	c=0
	integer=int(integer)
	ret=num("0",0)
	for i in range(a.len()-1):
		ret.val.append(0)
	ret.dP=a.dP
	for i in range (len(a.val)-1,-1,-1):
		ret.val[i]=(a.val[i]*integer)+c
		c=int(ret.val[i]//10)
		ret.val[i]%=10
	while c!=0:
		ret.val.insert(0,int(c%10))
		c//=10
		ret.dP+=1
	return ret
def stringToNum(str):
	dP=str.find(".")
	str=str.replace(".","")
	return num(str, dP)
def add(num1, num2):
	ret=num("0",0)
	for i in range(len(num1.val)-1):
		ret.val.append(0)
	ret.dP=int(num1.dP)
	while(num1.dP<num2.dP):
		ret.val.insert(0,0)
		ret.dP+=1
		num1.val.insert(0,0)
		num1.dP+=1
	while(num2.dP<num1.dP):
		num2.dP+=1
		num2.val.insert(0,0)
	while(len(num1.val)<len(num2.val)):
		num1.val.append(0)
		ret.val.append(0)
	while(len(num2.val)<len(num1.val)):
		num2.val.append(0)
	c=0
	leng=min(len(num1.val),len(num2.val))
	for i in range (leng-1,-1,-1):
		ret.val[i]=num1.val[i]+num2.val[i]+c
		c=ret.val[i]//10
		ret.val[i]%=10
	if c!=0:
		ret.val.insert(0,c)
		ret.dP+=1
	ret.removeZerosBack()
	num1.removeZerosBack()
	num2.removeZerosBack()
	num1.removeZerosFront()
	num2.removeZerosFront()
	return ret
def multiplyByNum(num1, num2):
	c=[0]
	ret=num("1",0)
	ret.dP=num1.dP+num2.dP-1
	for i in range(len(num1.val)+len(num2.val)):
		c.append(0)
	for i in range(len(num1.val)):
		for j in range(len(num2.val)):
			c[i+j]+=num1.val[i]*num2.val[j]
	d=0
	for i in range(len(c)-1,-1,-1):
		c[i]+=d
		d=c[i]//10
		c[i]%=10
		c[i]=int(c[i])
	while d!=0:
		c.insert(0,int(d%10))
		ret.dP+=1
		d//=10
	ret.val=c
	ret.removeZerosBack()
	return ret