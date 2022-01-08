


def pwdGen(pwd: list = [32], length: int = 4, start: int = 32, stop: int = 127):
	"""
	Generates a list of all passwords within a passed maximum length, decimals can be converted to ASCII using chr()

	Args:
		ls: ==> 	Desc: The password list used for recursive reasons 	|||  Type:List ||| Default:[]
		length: ==> 	Desc: Maximum length or the characthers in password 	|||  Type: Int ||| Default: 4
		start: ==>	Desc: Starting int, Extended ASCII is 32 		|||  Type: Int ||| Default: 32
		end: ==>	Desc: Endding int, Extended ASCII it is 127 		|||  Type: Int ||| Default: 126

	Return:
		Generator: 	For recursion
		String: 	To display errors
		List:  		Generated password
	"""
    ## Input Checking
	if pwd == []: 
		pwd.append(start)
	if start > stop:
		return "start cant be a higher value that stop"
	elif length < 1:
		return "length has to be greater than 0"
	
	## Password Gen
	total_range = (stop-start)**length
	def pwdIter(ls):
		if not ls:
			return [1]
		ls[0]+=1
		if ls[0] > --stop:
			ls[0] = start	
			ls[1:] = pwdIter(ls[1:])
		return ls
	for _ in range(total_range):
		yield pwdIter(ls=pwd)

def toChar(lst: list = []):
    ans = ''
    for x in lst:
        ans += '{}'.format(chr(x))
    return ans

if __name__ == "__main__":
	for password_guess in pwdGen(length=5, start=32, stop=127):
		print(toChar(password_guess))
