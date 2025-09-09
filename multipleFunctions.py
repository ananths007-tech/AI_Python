class mulFunctions():
    @staticmethod
    def eligibility_marriage():
        try:
            v_age = int(input("Enter your Age: "))
            v_gender = input("Enter your Gender: ").capitalize()
            
            if v_gender == 'Male':
                if v_age < 21:
                    print("NOT ELIGIBLE")
                else:
                    print("ELIGIBLE")
            elif v_gender == 'Female':
                if v_age < 18:
                    print("NOT ELIGIBLE")
                else:
                    print("ELIGIBLE")
            else:
                print("Please enter 'Male' or 'Female'")
        except ValueError:
            print("Please enter a valid age (number)")
                    
    @staticmethod
    def Odd_Even():
        v_num= int(input("Enter the number :"))
        if((v_num%2)==1):
            print("Its a Odd number")
            message = 'Odd Number'
        else:
            print("Its an even number")
            message = 'Even number'
        return message
            
    @staticmethod
    def BMI():
        v_bmi = int(input('Enter the BMI index:'))
        if((v_bmi <9)):
            print('Under weight')
            message = 'Under weight'
        elif((v_bmi < 24)):
            print('Optimum range')
            message = 'Optimum range'
        elif ((v_bmi < 29)):
            print('Over weight')
            message = 'Over weight'
        else:
            print('Very over weight')
            message = 'Very over weight'
        return message
    @staticmethod
    def list_AI():
        lst_AI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in lst_AI:
            print(i)
        return lst_AI  # Add this line