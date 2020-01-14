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
from pprint import pprint
from pandas import ExcelWriter
from pandas import ExcelFile

# SEM-1
df = pd.read_excel('1.xlsx')
set1 = df[['MAP_NUMBER','RESULT','BR_CODE']]

# SEM-2
df = pd.read_excel('2.xlsx')
set2 = df[['MAP_NUMBER','RESULT','BR_CODE']]


bm1_pass = check(set1, set2, 3, 'PASS', 1)
bm1_fail = check(set1, set2, 3, 'FAIL', 1)

ce1_pass = check(set1, set2, 7, 'PASS', 1)
ce1_fail = check(set1, set2, 7, 'FAIL', 1)

ec1_pass = check(set1, set2, 11, 'PASS', 1)
ec1_fail = check(set1, set2, 11, 'FAIL', 1)

it1_pass = check(set1, set2, 16, 'PASS', 1)
it1_fail = check(set1, set2, 16, 'FAIL', 1)

ic1_pass = check(set1, set2, 17, 'PASS', 1)
ic1_fail = check(set1, set2, 17, 'FAIL', 1)

mt1_pass = check(set1, set2, 21, 'PASS', 1)
mt1_fail = check(set1, set2, 21, 'FAIL', 1)

print('Regular : YEAR - 1')
print('====================')
def print_data(s, p, f):
	print(s+'\t'+'Pass:',len(p))
	print('\tFAIL:',len(f))
	print('====================')

print_data('BM',bm1_pass,bm1_fail)
print_data('CE',ce1_pass,ce1_fail)
print_data('EC',ec1_pass,ec1_fail)
print_data('IT',it1_pass,it1_fail)
print_data('IC',ic1_pass,ic1_fail)
print_data('MT',mt1_pass,mt1_fail)

def check_prev(b2, b1):
	b = [i for i in (set(b1) & set(b2))]
	return b

# SEM-3
df = pd.read_excel('3.xlsx')
set3 = df[['MAP_NUMBER','RESULT','BR_CODE']]

# SEM-4
df = pd.read_excel('4.xlsx')
set4 = df[['MAP_NUMBER','RESULT','BR_CODE']]

bm2_pass_reg, bm2_pass_d2d = check(set3, set4, 3, 'PASS', 2)
bm2_fail_reg, bm2_fail_d2d = check(set3, set4, 3, 'FAIL', 2)

ce2_pass_reg, ce2_pass_d2d = check(set3, set4, 7, 'PASS', 2)
ce2_fail_reg, ce2_fail_d2d = check(set3, set4, 7, 'FAIL', 2)

ec2_pass_reg, ec2_pass_d2d = check(set3, set4, 11, 'PASS', 2)
ec2_fail_reg, ec2_fail_d2d = check(set3, set4, 11, 'FAIL', 2)

it2_pass_reg, it2_pass_d2d = check(set3, set4, 16, 'PASS', 2)
it2_fail_reg, it2_fail_d2d = check(set3, set4, 16, 'FAIL', 2)

ic2_pass_reg, ic2_pass_d2d = check(set3, set4, 17, 'PASS', 2)
ic2_fail_reg, ic2_fail_d2d = check(set3, set4, 17, 'FAIL', 2)

mt2_pass_reg, mt2_pass_d2d = check(set3, set4, 21, 'PASS', 2)
mt2_fail_reg, mt2_fail_d2d = check(set3, set4, 21, 'FAIL', 2)

# removing prev student
bm2_pass_reg = check_prev(bm2_pass_reg, bm1_pass)
ce2_pass_reg = check_prev(ce2_pass_reg, ce1_pass)
ec2_pass_reg = check_prev(ec2_pass_reg, ec1_pass)
it2_pass_reg = check_prev(it2_pass_reg, it1_pass)
ic2_pass_reg = check_prev(ic2_pass_reg, ic1_pass)
mt2_pass_reg = check_prev(mt2_pass_reg, mt1_pass)

print('\nRegular : YEAR - 2')
print('====================')

print_data('BM',bm2_pass_reg,bm2_fail_reg)
print_data('CE',ce2_pass_reg,ce2_fail_reg)
print_data('EC',ec2_pass_reg,ec2_fail_reg)
print_data('IT',it2_pass_reg,it2_fail_reg)
print_data('IC',ic2_pass_reg,ic2_fail_reg)
print_data('MT',mt2_pass_reg,mt2_fail_reg)

print('\nD2D : YEAR - 2')
print('====================')

print_data('BM',bm2_pass_d2d,bm2_fail_d2d)
print_data('CE',ce2_pass_d2d,ce2_fail_d2d)
print_data('EC',ec2_pass_d2d,ec2_fail_d2d)
print_data('IT',it2_pass_d2d,it2_fail_d2d)
print_data('IC',ic2_pass_d2d,ic2_fail_d2d)
print_data('MT',mt2_pass_d2d,mt2_fail_d2d)

# SEM-5
df = pd.read_excel('5.xlsx')
set5 = df[['MAP_NUMBER','RESULT','BR_CODE']]

# SEM-6
df = pd.read_excel('6.xlsx')
set6 = df[['MAP_NUMBER','RESULT','BR_CODE']]

bm3_pass_reg, bm3_pass_d2d = check(set5, set6, 3, 'PASS', 2)
bm3_fail_reg, bm3_fail_d2d = check(set5, set6, 3, 'FAIL', 2)

ce3_pass_reg, ce3_pass_d2d = check(set5, set6, 7, 'PASS', 2)
ce3_fail_reg, ce3_fail_d2d = check(set5, set6, 7, 'FAIL', 2)

ec3_pass_reg, ec3_pass_d2d = check(set5, set6, 11, 'PASS', 2)
ec3_fail_reg, ec3_fail_d2d = check(set5, set6, 11, 'FAIL', 2)

it3_pass_reg, it3_pass_d2d = check(set5, set6, 16, 'PASS', 2)
it3_fail_reg, it3_fail_d2d = check(set5, set6, 16, 'FAIL', 2)

ic3_pass_reg, ic3_pass_d2d = check(set5, set6, 17, 'PASS', 2)
ic3_fail_reg, ic3_fail_d2d = check(set5, set6, 17, 'FAIL', 2)

mt3_pass_reg, mt3_pass_d2d = check(set5, set6, 21, 'PASS', 2)
mt3_fail_reg, mt3_fail_d2d = check(set5, set6, 21, 'FAIL', 2)

# removing prev student
bm3_pass_reg = check_prev(bm3_pass_reg, bm2_pass_reg)
ce3_pass_reg = check_prev(ce3_pass_reg, ce2_pass_reg)
ec3_pass_reg = check_prev(ec3_pass_reg, ec2_pass_reg)
it3_pass_reg = check_prev(it3_pass_reg, it2_pass_reg)
ic3_pass_reg = check_prev(ic3_pass_reg, ic2_pass_reg)
mt3_pass_reg = check_prev(mt3_pass_reg, mt2_pass_reg)

bm3_pass_d2d = check_prev(bm3_pass_d2d, bm2_pass_d2d)
ce3_pass_d2d = check_prev(ce3_pass_d2d, ce2_pass_d2d)
ec3_pass_d2d = check_prev(ec3_pass_d2d, ec2_pass_d2d)
it3_pass_d2d = check_prev(it3_pass_d2d, it2_pass_d2d)
ic3_pass_d2d = check_prev(ic3_pass_d2d, ic2_pass_d2d)
mt3_pass_d2d = check_prev(mt3_pass_d2d, mt2_pass_d2d)

print('\nRegular : YEAR - 3')
print('====================')

print_data('BM',bm3_pass_reg,bm3_fail_reg)
print_data('CE',ce3_pass_reg,ce3_fail_reg)
print_data('EC',ec3_pass_reg,ec3_fail_reg)
print_data('IT',it3_pass_reg,it3_fail_reg)
print_data('IC',ic3_pass_reg,ic3_fail_reg)
print_data('MT',mt3_pass_reg,mt3_fail_reg)

print('\nD2D : YEAR - 3')
print('====================')

print_data('BM',bm3_pass_d2d,bm3_fail_d2d)
print_data('CE',ce3_pass_d2d,ce3_fail_d2d)
print_data('EC',ec3_pass_d2d,ec3_fail_d2d)
print_data('IT',it3_pass_d2d,it3_fail_d2d)
print_data('IC',ic3_pass_d2d,ic3_fail_d2d)
print_data('MT',mt3_pass_d2d,mt3_fail_d2d)

# SEM-7
df = pd.read_excel('7.xlsx')
set7 = df[['MAP_NUMBER','RESULT','BR_CODE']]

# SEM-8
df = pd.read_excel('8.xlsx')
set8 = df[['MAP_NUMBER','RESULT','BR_CODE']]

bm4_pass_reg, bm4_pass_d2d = check(set7, set8, 3, 'PASS', 2)
bm4_fail_reg, bm4_fail_d2d = check(set7, set8, 3, 'FAIL', 2)

ce4_pass_reg, ce4_pass_d2d = check(set7, set8, 7, 'PASS', 2)
ce4_fail_reg, ce4_fail_d2d = check(set7, set8, 7, 'FAIL', 2)

ec4_pass_reg, ec4_pass_d2d = check(set7, set8, 11, 'PASS', 2)
ec4_fail_reg, ec4_fail_d2d = check(set7, set8, 11, 'FAIL', 2)

it4_pass_reg, it4_pass_d2d = check(set7, set8, 16, 'PASS', 2)
it4_fail_reg, it4_fail_d2d = check(set7, set8, 16, 'FAIL', 2)

ic4_pass_reg, ic4_pass_d2d = check(set7, set8, 17, 'PASS', 2)
ic4_fail_reg, ic4_fail_d2d = check(set7, set8, 17, 'FAIL', 2)

mt4_pass_reg, mt4_pass_d2d = check(set7, set8, 21, 'PASS', 2)
mt4_fail_reg, mt4_fail_d2d = check(set7, set8, 21, 'FAIL', 2)

# removing prev student
bm4_pass_reg = check_prev(bm4_pass_reg, bm3_pass_reg)
ce4_pass_reg = check_prev(ce4_pass_reg, ce3_pass_reg)
ec4_pass_reg = check_prev(ec4_pass_reg, ec3_pass_reg)
it4_pass_reg = check_prev(it4_pass_reg, it3_pass_reg)
ic4_pass_reg = check_prev(ic4_pass_reg, ic3_pass_reg)
mt4_pass_reg = check_prev(mt4_pass_reg, mt3_pass_reg)

bm4_pass_d2d = check_prev(bm4_pass_d2d, bm3_pass_d2d)
ce4_pass_d2d = check_prev(ce4_pass_d2d, ce3_pass_d2d)
ec4_pass_d2d = check_prev(ec4_pass_d2d, ec3_pass_d2d)
it4_pass_d2d = check_prev(it4_pass_d2d, it3_pass_d2d)
ic4_pass_d2d = check_prev(ic4_pass_d2d, ic3_pass_d2d)
mt4_pass_d2d = check_prev(mt4_pass_d2d, mt3_pass_d2d)

print('\nRegular : YEAR - 4')
print('====================')

print_data('BM',bm4_pass_reg,bm4_fail_reg)
print_data('CE',ce4_pass_reg,ce4_fail_reg)
print_data('EC',ec4_pass_reg,ec4_fail_reg)
print_data('IT',it4_pass_reg,it4_fail_reg)
print_data('IC',ic4_pass_reg,ic4_fail_reg)
print_data('MT',mt4_pass_reg,mt4_fail_reg)

print('\nD2D : YEAR - 4')
print('====================')

print_data('BM',bm4_pass_d2d,bm4_fail_d2d)
print_data('CE',ce4_pass_d2d,ce4_fail_d2d)
print_data('EC',ec4_pass_d2d,ec4_fail_d2d)
print_data('IT',it4_pass_d2d,it4_fail_d2d)
print_data('IC',ic4_pass_d2d,ic4_fail_d2d)
print_data('MT',mt4_pass_d2d,mt4_fail_d2d)