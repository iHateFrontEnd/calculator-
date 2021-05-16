print('For addition type 1, for division type 3, for multiplication type 4, for subtraction type 1')

allInp = int(input(' is the number:- '))

#fucntion for addition
def addtion():
	mainValAdd = int(input('What the number for addition:- '))

	print('+')

	babyValAdd = int(input('What the number:- '))

	print(babyValAdd + mainValAdd)

#function for subtraction 
def subtraction():
	mainValSub = int(input('what is the number for subtraction:- '))

	print('-')

	babyValSub = int(input('what is the number:- '))

	print(mainValSub - babyValSub)

#fucntion for division 
def division():
	mainValDiv = int(input('What is the number for division:- '))

	print('÷')

	babyValDiv = int(input('What is the number:- '))

	print(mainValDiv / babyValDiv)

#function for multiplication 
def multiplication():
	mainValMul = int(input('What is the number for multiplication:- '))

	print('X')

	babyValMul = int(input('What is the number:- '))

	print(mainValMul * babyValMul)
	
#these if else statement take the input and trasfer to their own function
if allInp == 1:
	addtion()
elif allInp == 2:
	subtraction()
elif allInp == 3:
	division()
elif allInp == 4:
	multiplication()

### symbols as numbers #####
### for Addition = 1 #######
### for Division = 3 #######
### for Multiplication = 4 #
### for Subtraction = 2 ####