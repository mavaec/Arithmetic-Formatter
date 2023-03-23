
def arithmetic_arranger(list, giveResult = False) :
	firstOperand = ''
	secondOperand = ''
	lineOperands = ''
	resOperation = ''
	errNumber = 0
	opResult = 0

	operator = ''


	for operation in list :
		posOperatorAdd = operation.find('+')
		posOperatorSub = operation.find('-')


		if posOperatorAdd > 0 :
			operator = 'Addition'
			op1 = operation[:posOperatorAdd]


		elif posOperatorSub > 0 :
			operator = 'Substraction'
			op1 = operation[:posOperatorSub]

		else :
			print('Error: Operator must be \'+\' or \'-\'.')
			errNumber += 1
			if errNumber >= 5 :
				print('Error: Too many problems.')
				return 0
			continue


		op1 = op1.strip() 
		op1len = len(op1)
		try :
			valOp1 = int(op1)
		except:
			print('Error: Numbers must only contain digits.')
			errNumber += 1
			if errNumber >= 5 :
				print('Error: Too many problems.')
				return 0
			continue

		if op1len > 4 :
			print('Error: Numbers cannot be more than four digits.')
			errNumber += 1
			if errNumber >= 5 :
				print('Error: Too many problems.')
				return 0
			continue


		if operator == 'Addition' :
			op2 = operation[posOperatorAdd+1:]
		else :
			op2 = operation[posOperatorSub+1:]

		op2 = op2.strip() 
		op2len = len(op2)
		try :
			valOp2 = int(op2)
		except:
			print('Error: Numbers must only contain digits.')
			errNumber += 1
			if errNumber >= 5 :
				print('Error: Too many problems.')
				return 0
			continue

		if op2len > 4 :
			print('Error: Numbers cannot be more than four digits.')
			errNumber += 1
			if errNumber >= 5 :
				print('Error: Too many problems.')
				return 0
			continue

		if giveResult == True :
			if operator == 'Addition' :
				opResult = valOp1 + valOp2
			else :
				opResult = valOp1 - valOp2

		if op1len >= op2len :
			alignment = op1len + 2
		else :
			alignment = op2len + 2

		op1 = op1.rjust(alignment)
		op2 = op2.rjust(alignment)

		if operator == 'Addition' :
			op2 = op2[:0] + '+' + op2[1:]
		else : 
			op2 = op2[:0] + '-' + op2[1:]

		firstOperand = firstOperand + op1 + '    '
		secondOperand = secondOperand + op2 + '    '
		lineOperands = lineOperands + ''.ljust(alignment,'-') + '    '
		resOperation = resOperation + str(opResult).rjust(alignment) + '    '





	print(firstOperand)
	print(secondOperand)
	print(lineOperands)
	if giveResult == True :
		print(resOperation)
	return 0