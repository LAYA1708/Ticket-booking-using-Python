def places():
    print("\tTrain Booking System")
    print("__________________________________")
    print("List of Journey places:")
    print("1.chennnai-pune")
    print("2.chennnai-delhi")
    print("3.chennnai-Banglore")
    print("4.chennnai-Vijayawada")
    print("5.chennnai-Mumbai")
    choice=input("Select Your Journey Place:")
    if choice=='1':
        place="1.chennnai-pune"
    elif choice=='2':
        place="2.chennnai-delhi"
    elif choice=='3':
        place="3.chennnai-Banglore"
    elif choice=='4':
        place="4.chennnai-Vijayawada"
    elif choice=='5':
        place="5.chennnai-Mumbai"
    else:
        print("Invalid choice")
    return place
objplaces=places()
print(f" you Selected:{objplaces}")
print("-------------------------------------")
def trains():
    print("List of available trains:")
    print("1.ABC Express")
    print("2.Bharath Express")
    print("3.Chennai Express")
    choice=input("Select Your Train:")
    if choice=='1':
        train="1.ABC Express"
    elif choice=='2':
        train="2.Bharath Express"
    elif choice=='3':
        train="3.chennnai Express"
    else:
        print("Invalid choice")
    return train
objtrains=trains()
print(f"You Selected:{objtrains}")
print("-------------------------------------")
def seats():
    print("List of seats:")
    print("1.AC seats")
    print("2.Non-AC seats")
    choice=input("Select Your Seat:")
    if choice=='1':
        seat="1.AC Seat"
        total_acseats=50
        booked_acseats=1
        avail_acseats=total_acseats-booked_acseats
        if avail_acseats>0:
            print(f"Available AC seats:{avail_acseats}")
        else:
            print("No AC Seats Available.")
    elif choice=='2':
        seat="2.Non-AC seats"
        total_non_acseats=50
        booked_non_acseats=1
        avail_non_acseats=total_non_acseats-booked_non_acseats
        if avail_non_acseats>0:
            print(f"Available Non-AC seats:{avail_non_acseats}")
        else:
            print("No Non-AC Seats Available.")
    else:
        print("Invalid choice")
    return seat
objseats=seats()
print(f"You Selected:{objseats}")
print("-------------------------------------")
def dates():
    print("List of available dates:")
    print("23-10-2024")
    print("25-10-2024")
    print("28-10-2024")
    choice=input("Select Your date:")
    if choice=='1':
        date="23-10-2024"
    elif choice=='2':
        date="25-10-2024"
    elif choice=='3':
        date="28-10-2024"
    else:
        print("Invalid choice")
    return date
objdates=dates()
print(f"You Selected Date:{objdates}")
print("-------------------------------------")
def times():
    print("List of Available Times:")
    print("12AM-3PM")
    print("6PM-10PM")
    print("10AM-3PM")
    choice=input("select Your Time:")
    if choice=='1':
        time="12AM-3PM"
    elif choice=='2':
        time="6PM-10PM"
    elif choice=='3':
        time="10AM-3PM"
    else:
        print("No more timings available...")
    return time
objtimes=times()
print(f"You selected Time:{objtimes}")
print("---------")
Name=str(input("Enter Your Name:"))
Age=int(input("Enter Your Age:"))
print("--------")
def gender():
    print("Gender:")
    print("Male")
    print("Female")
    choice=input("select your gender:")
    if choice=='1':
        gen="Male"
    elif choice=='2':
        gen="Female"
    return gen
obj1=gender()
print(f"You Selected:{obj1}")
print("-------")
Phone=int(input("Enter Your Phone no:"))
DOB=input("Enter Your DOB(YYYY-MM-DD):")
Address=str(input("Enter Your Address:"))
print(".............Your Ticket Booked Successfully................")
def p_tic():
    tic_tem=f"""            ____________________________________
                           TICKET
                _________________________________
                 Name:{Name}
                 Age:{Age}
                 Gender:{obj1}
                 Phone:{Phone}
                 DOB:{DOB}
                 Address:{Address}
                 place:{objplaces}
                 train:{objtrains}
                 seat:{objseats}
                 date:{objdates}
                 Time:{objtimes}
                _________________________________
                Thank You!!..Enjoy the Journey...
                _________________________________"""
    print(tic_tem)
p_tic()
