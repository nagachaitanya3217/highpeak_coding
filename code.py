{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of employees: 6\n",
      "\n",
      "Here the goodies that are selected for distribution are:\n",
      "BiCycle: 5000\n",
      "Barkbusters: 10000\n",
      "Gear cycle: 22000\n",
      "Riding accessories: 30000\n",
      "Gopro: 35000\n",
      "Helmet: 54000\n",
      "\n",
      "\n",
      "And the difference between the chosen goodie with highest price and the lowest price is 49000\n"
     ]
    }
   ],
   "source": [
    "#input is stored in a text file named \"input_x.txt\"  , where x=1,2,3\n",
    "ip_file=open('C:\\\\Users\\\\naga chaitanya\\\\Desktop\\\\HIGHPEAK_CODING\\\\input.txt')\n",
    "f_data=ip_file.readlines()\n",
    "\n",
    "#ouput is stored in a text file named \"output.txt\"\n",
    "op_file = open(\"C:\\\\Users\\\\naga chaitanya\\\\Desktop\\\\HIGHPEAK_CODING\\\\output.txt\", \"w\")\n",
    "\n",
    "#absolute path is specified for calling files\n",
    "\n",
    "#----------------------------------------------------------------------------\n",
    "#data processing from file to required format\n",
    "data_tup=[]\n",
    "for item in f_data:\n",
    "    data_tup.append(item.split(\": \"))\n",
    "for i in range(len(data_tup)):\n",
    "    data_tup[i][1]=int(data_tup[i][1][:])\n",
    "\n",
    "\n",
    "a_names,a_values=[],[]\n",
    "for item in data_tup:\n",
    "    a_names.append(item[0])\n",
    "    a_values.append(item[1])\n",
    "\n",
    "a=a_values[:]\n",
    "a.sort()\n",
    "#---------------------------------------------------------------------------------\n",
    "no_of_employees=6\n",
    "\n",
    "print('Number of employees: {}\\n'.format(no_of_employees))\n",
    "print('Here the goodies that are selected for distribution are:')\n",
    "\n",
    "op_file.write('Number of employees: {}\\n'.format(no_of_employees))\n",
    "op_file.write('Here the goodies that are selected for distribution are:\\n')\n",
    "\n",
    "#---------------------main logic-------------------------------------\n",
    "mini=99999999999\n",
    "min_index=0\n",
    "for i in range(0,len(a)-no_of_employees):\n",
    "    if a[i+no_of_employees-1]-a[i]<mini:\n",
    "        min_index=i\n",
    "        mini=a[i+no_of_employees-1]-a[i]\n",
    "res=a[min_index:min_index+no_of_employees]\n",
    "\n",
    "#-----------------printing output and writing output into file--------------------------\n",
    "for val in res:\n",
    "    i=a_values.index(val)\n",
    "    s=\"{}: {}\".format(a_names[i],a_values[i])\n",
    "    print(s)\n",
    "    op_file.write(s)\n",
    "    op_file.write(\"\\n\")\n",
    "print(\"\\n\")\n",
    "print('And the difference between the chosen goodie with highest price and the lowest price is {}'.format(res[-1]-res[0]))\n",
    "\n",
    "op_file.write('\\nAnd the difference between the chosen goodie with highest price and the lowest price is {}'.format(res[-1]-res[0]))\n",
    "op_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
