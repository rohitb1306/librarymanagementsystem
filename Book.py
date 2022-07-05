class books1():
    num=1001
    def __init__(self,name,type,writer,year):
        self.name=name
        self.type=type
        self.writer=writer
        self.year_of_printing=year
        self.book_number=books1.num
        books1.num+=1
class date:

    @classmethod
    def dat_minus_date(cls,date,date1):
        lit=date.split("-")
        lit1=date1.split("-")
        lit=[int(i) for i in lit]
        lit1=[int(i) for i in lit1]
        if lit[2]-lit1[2]>=0 and lit[2]-lit1[2]<=1:
            if lit[0]-lit1[0]>=0:
                return lit[0]-lit1[0]
            elif lit[0]-lit1[0]<0:
                if lit[1]-lit1[1]==1:
                    if lit1[1]==1 or lit1[1]==3 or lit1[1]==5 or lit1[1]==7 or lit1[1]==9 or lit1[1]==11:
                        lit[0]+=31

                    elif lit1[1]==2:
                        if lit[2]%400==0:
                            lit[0]+=29
                        elif lit[2]%4==0 and lit[2]%100!=0:
                            lit[0]+=29
                        else:
                            lit[0]+=28
                    else:
                        lit[0]+=30
                    return lit[0]-lit1[0]
                elif lit[1]-lit1[1]<0:
                    lit[1]+=12
                    if lit[1]-lit1[1]==1:
                        if lit1[1]==1 or lit1[1]==3 or lit1[1]==5 or lit1[1]==7 or lit1[1]==9 or lit1[1]==11:
                            lit[0]+=31
    
                        elif lit1[1]==2:
                            if lit[2]%400==0:
                                lit[0]+=29
                            elif lit[2]%4==0 and lit[2]%100!=0:
                                lit[0]+=29
                            else:
                                lit[0]+=28
                        else:
                            lit[0]+=30
                        return lit[0]-lit1[0]
                    else:
                        if lit[1]-lit1[1]>=2 and lit[1]-lit1[1]<=5:
                            return -1
                        if lit[1]-lit1[1]>=6 and lit[1]-lit1[1]<=12:
                            return -2
                else:
                    if lit[1]-lit1[1]>=2 and lit[1]-lit1[1]<=5:
                        return -1
                    if lit[1]-lit1[1]>=6 and lit[1]-lit1[1]<=12:
                        return -2
        elif lit[2]-lit1[2]<0:
            return -3
        else:
            return -4