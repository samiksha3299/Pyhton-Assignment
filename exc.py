def main():
    try:
        hours=int(input("How many hours did you work?"))
        pay_rate=float(input("enter your pay rate"))
        gross_pay=hours*pay_rate
        print("gross pay:$",format(gross_pay,'2f'),sep='')

    except:
        print("ERROR:Hours worked & hourly ray rate must be valid number")
        
    
    
    
main()
