
def arithmetic_arranger(list) :
	list_len = len(list)

	firstOperand = ''
	secondOperand = ''
	lineOperands = ''

	for operation in list :
		posOperatorAdd = operation.find('+')
		posOperatorSub = operation.find('-')


		if posOperatorAdd > 0 :
			#print("Addition")
			op1 = operation[:posOperatorAdd]
			op1 = op1.strip() 
			op1len = len(op1)
			op2 = operation[posOperatorAdd+1:]
			op2 = op2.strip() 
			op2len = len(op2)

			if op1len >= op2len :
				alignment = op1len + 2
			else :
				alignment = op2len + 2
		
			#op1 = '{:>{alignment}}'.format(op1, alignment=alignment)
			op1 = op1.rjust(alignment)
			op2 = op2.rjust(alignment)
			op2 = op2[:0] + '+' + op2[1:]
			#op2 = '{:>{alignment}}'.format(op2, alignment=alignment)
			
			firstOperand = firstOperand + op1 + '    '
			secondOperand = secondOperand + op2 + '    '
			lineOperands = lineOperands + ''.ljust(alignment,'-') + '    '


		elif posOperatorSub > 0 :
			#print("Substraction")
			op1 = operation[:posOperatorSub]
			op1 = op1.strip() 
			op1len = len(op1)
			op2 = operation[posOperatorSub+1:]
			op2 = op2.strip() 
			op2len = len(op2)

			if op1len >= op2len :
				alignment = op1len + 2
			else :
				alignment = op2len + 2
		
			#op1 = '{:>{alignment}}'.format(op1, alignment=alignment)
			op1 = op1.rjust(alignment)
			op2 = op2.rjust(alignment)
			op2 = op2[:0] + '-' + op2[1:]
			#op2 = '{:>{alignment}}'.format(op2, alignment=alignment)
			
			firstOperand = firstOperand + op1 + '    '
			secondOperand = secondOperand + op2 + '    '
			lineOperands = lineOperands + ''.ljust(alignment,'-') + '    '





		else :
			print("Error: wrong operation")


		#op = operation.strip()
		#pos = op.find(' ')
		#firstOperand = firstOperand + op[:pos] + ' '
		#print(posOperation)
	print(firstOperand)
	print(secondOperand)
	print(lineOperands)
	return 0