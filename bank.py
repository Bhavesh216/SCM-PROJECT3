acc_nums = {"cha233": 0, "bha215": 0, "bha216": 0, "bha221" :0}
acc_pins = {"cha233": "0000", "bha215": "0000", "bha216": "0000"}


def printing_stuff():
    print("To create a new account --> 1")
    print("To deposit money --> 2")
    print("To withdraw money --> 3")
    print("To transfer money --> 4")
    print("To check balance --> 5")
    print("To exit --> 6")
    print()


def new_acc_details():
    name = input("Enter account holder name : ")
    # age = int(input("Enter your age : "))
    aadhar_no = input("Enter your aadhar no. : ")
    acc_num = name[:3] + aadhar_no[-3:]
    acc_nums[acc_num] = 0
    set_pin = input("Enter New Pin: ")
    acc_pins[acc_num] = set_pin
    print("Account No. :", acc_num)
    print()


def checking_pin():
    flag = True
    while flag:
        pin = input("Enter Pin: ")
        if pin == acc_pins[key]:
            flag = False
        else:
            print("Incorrect Pin")
            print()


def transferring():
    if a not in acc_nums.keys() or b not in acc_nums.keys():
        print("Not a valid Account No. ")
        print()

    else:
        flag = True
        while flag:
            pin = input("Enter Pin: ")
            if pin == acc_pins[a]:
                amount = int(input("Enter the amount to transfer : "))
                if amount < acc_nums[a]:
                    acc_nums[a] = acc_nums[a] - amount
                    acc_nums[b] = acc_nums[b] + amount
                    print(f"Successfully transferred {amount} from {a} to {b}")
                    print(f"Remaining balance : {acc_nums[a]}")
                    print()
                    flag = False
                else:
                    print("Insufficient funds! Current Balance :", acc_nums[a])
                    print()
                    break
            else:
                print("Incorrect Pin")
                print()


def deposit(amount):
    acc_nums[key] = acc_nums[key] + amount
    print("Current Balance :", acc_nums[key])
    print()


def withdraw(amount):
    if amount > acc_nums[key]:
        print("Insufficient funds! Current Balance :", acc_nums[key])
        print()
    else:
        acc_nums[key] = acc_nums[key] - amount
        print("Current Balance :", acc_nums[key])
        print()


def check_bal():
    print("Current Balance :", acc_nums[key])
    print()

#          ..............main................


running = True

while running:
    printing_stuff()

    n = int(input("Select any option : "))
    print()

#         .........creating a new acc............

    if n == 1:
        new_acc_details()

    #    ..................depositing money................

    elif n == 2:
        ch = input("Enter account number : ")

        for key in acc_nums.keys():
            if key == ch:
                checking_pin()
                amount = int(input("enter the amount to deposit : "))
                deposit(amount)

            elif key != ch:
                pass

    #      ..................withdrawing money................

    elif n == 3:
        ch = input("Enter account number : ")

        for key in acc_nums.keys():
            if key == ch:
                checking_pin()

                amount = int(input("enter the amount to withdraw : "))
                withdraw(amount)

            elif key != ch:
                pass

#          .................transferring money...............

    elif n == 4:
        a = input("Enter your account number : ")
        b = input("Enter receiver's account number : ")

        for key in acc_nums.keys():
            transferring()
            break


#         .................. checking balance..............

    elif n == 5:
        ch = input("Enter account number : ")

        for key in acc_nums.keys():
            if key == ch:
                checking_pin()
                check_bal()

    elif n == 6:
        running = False
