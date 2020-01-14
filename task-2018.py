def check(set1, set2, code, result, year):
	if(year==1):
		temp1 = []
		temp2 = []
		temp = []
		for i in set1.index:
			if(set1['BR_CODE'][i] == code and set1['RESULT'][i] == result):
				temp1.append(set1['MAP_NUMBER'][i])
		for i in set2.index:
			if(set2['BR_CODE'][i] == code and set2['RESULT'][i] == result):
				temp2.append(set2['MAP_NUMBER'][i])
		if(result=='PASS'):
			temp = [i for i in (set(temp1) & set(temp2))]
		else:
			temp = [i for i in (set(temp1) | set(temp2))]
		return temp

	else:
		temp = ''
		reg_temp1 = []
		reg_temp2 = []
		d2d_temp1 = []
		d2d_temp2 = []
		reg = []
		d2d = []
		for i in set1.index:
			if(set1['BR_CODE'][i] == code and set1['RESULT'][i] == result):
				temp = str(set1['MAP_NUMBER'][i])
				if(temp[5]=='0'):
					reg_temp1.append(set1['MAP_NUMBER'][i])
				else:
					d2d_temp1.append(set1['MAP_NUMBER'][i])
		for i in set2.index:
			if(set2['BR_CODE'][i] == code and set2['RESULT'][i] == result):
				temp = str(set2['MAP_NUMBER'][i])
				if(temp[5]=='0'):
					reg_temp2.append(set2['MAP_NUMBER'][i])
				else:
					d2d_temp2.append(set2['MAP_NUMBER'][i])

		if(result=='PASS'):
			reg = [i for i in (set(reg_temp1) & set(reg_temp2))]
			d2d = [i for i in (set(d2d_temp1) & set(d2d_temp2))]
		else:
			reg = [i for i in (set(reg_temp1) | set(reg_temp2))]
			d2d = [i for i in (set(d2d_temp1) | set(d2d_temp2))]
		return reg, d2d

import pandas as pd


# SEM-1
df = pd.read_excel('1.xlsx')
set1 = df[['MAP_NUMBER','RESULT','BR_CODE']]

# SEM-2
df = pd.read_excel('2.xlsx')
set2 = df[['MAP_NUMBER','RESULT','BR_CODE']]


bm_pass = check(set1, set2, 3, 'PASS', 1)
bm_fail = check(set1, set2, 3, 'FAIL', 1)

ce_pass = check(set1, set2, 7, 'PASS', 1)
ce_fail = check(set1, set2, 7, 'FAIL', 1)

ec_pass = check(set1, set2, 11, 'PASS', 1)
ec_fail = check(set1, set2, 11, 'FAIL', 1)

it_pass = check(set1, set2, 16, 'PASS', 1)
it_fail = check(set1, set2, 16, 'FAIL', 1)

ic_pass = check(set1, set2, 17, 'PASS', 1)
ic_fail = check(set1, set2, 17, 'FAIL', 1)

mt_pass = check(set1, set2, 21, 'PASS', 1)
mt_fail = check(set1, set2, 21, 'FAIL', 1)

print('Regular : YEAR - 1')
print('====================')
def print_data(s, p, f):
	print(s+'\t'+'Pass:',len(p))
	print('\tFAIL:',len(f))
	print('====================')

print_data('BM',bm_pass,bm_fail)
print_data('CE',ce_pass,ce_fail)
print_data('EC',ec_pass,ec_fail)
print_data('IT',it_pass,it_fail)
print_data('IC',ic_pass,ic_fail)
print_data('MT',mt_pass,mt_fail)
