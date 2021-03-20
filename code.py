#input is stored in a text file named "input_x.txt"  , where x=1,2,3
ip_file=open('C:\\Users\\naga chaitanya\\Desktop\\HIGHPEAK_CODING\\input.txt')
f_data=ip_file.readlines()

#ouput is stored in a text file named "output.txt"
op_file = open("C:\\Users\\naga chaitanya\\Desktop\\HIGHPEAK_CODING\\output.txt", "w")

#absolute path is specified for calling files

#----------------------------------------------------------------------------
#data processing from file to required format
data_tup=[]
for item in f_data:
    data_tup.append(item.split(": "))
for i in range(len(data_tup)):
    data_tup[i][1]=int(data_tup[i][1][:])


a_names,a_values=[],[]
for item in data_tup:
    a_names.append(item[0])
    a_values.append(item[1])

a=a_values[:]
a.sort()
#---------------------------------------------------------------------------------
no_of_employees=6

print('Number of employees: {}\n'.format(no_of_employees))
print('Here the goodies that are selected for distribution are:')

op_file.write('Number of employees: {}\n'.format(no_of_employees))
op_file.write('Here the goodies that are selected for distribution are:\n')

#---------------------main logic-------------------------------------
mini=99999999999
min_index=0
for i in range(0,len(a)-no_of_employees):
    if a[i+no_of_employees-1]-a[i]<mini:
        min_index=i
        mini=a[i+no_of_employees-1]-a[i]
res=a[min_index:min_index+no_of_employees]

#-----------------printing output and writing output into file--------------------------
for val in res:
    i=a_values.index(val)
    s="{}: {}".format(a_names[i],a_values[i])
    print(s)
    op_file.write(s)
    op_file.write("\n")
print("\n")
print('And the difference between the chosen goodie with highest price and the lowest price is {}'.format(res[-1]-res[0]))

op_file.write('\nAnd the difference between the chosen goodie with highest price and the lowest price is {}'.format(res[-1]-res[0]))
op_file.close()