
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[5]:

pd.Series(np.random.randn(5))


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[7]:

d


# In[8]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[9]:

pd.Series(d)


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s


# In[12]:

s(0)


# In[14]:

s(0)


# In[15]:

s(0)


# In[16]:

s[0]


# In[17]:

s[:3]


# In[18]:

s[:]


# In[20]:

s[s > s.median()] # identif elements with value greater than the median


# In[21]:

s[s > s.median()] # identif elements with value greater than the median


# In[22]:

s[[4, 3, 1]]


# In[23]:

s[[4, 3, 1]] # list elements in different order


# In[24]:

np.exp(s) # convert elements to exponential 


# In[25]:

s['a']


# In[27]:

s['a','c']


# In[28]:

s['e'] = 12 # put valeu in 'c'


# In[29]:

s


# In[30]:

s['f']


# In[31]:

'f' in s


# In[34]:

if 'f' in s:
    print (s['f'])
else:
    print (s['e'])
    


# In[35]:

s.get('f')


# In[36]:

s.get('e')


# In[37]:

s.get('f')  # will only bring it back if it's available


# In[38]:

s.get('f', 'NaN'')  # will only bring it back if its available otherwise it returns NaN


# In[39]:

s.get('f', np.NaN)  # will only bring it back if its available otherwise it returns NaN


# In[40]:

s


# In[41]:

s+s


# In[42]:

s *3


# In[43]:

np.exp(s)


# In[44]:

s[1:]


# In[46]:

s[1:]


# # s[:-1]

# In[47]:

s[:-1]


# In[48]:

s[1:] + s[:-1]


# In[49]:

s[1:] + s[:-1]  # outups NaN as certain elements of vector are missing


# In[50]:

s[1:] + s[:-1]  # returns NaN as certain elements of vector are missing, i.e. both arrays do not align when added


# In[51]:

s = pd.Series(np.random.randn(5), name='something')  # assign a name to object


# In[52]:

s


# 

# In[53]:

something


# In[54]:

s['f'] = 0  # add new element with a value to the series


# In[55]:

s


# In[56]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[57]:

d


# In[58]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}  #  Set up two pandas series with two sets of data 


# In[59]:

d


# In[60]:

df = pd.dataframe(d)  # Create a dataframe using series in d


# In[61]:

df = pd.DataFrame(d)  # Create a dataframe using series in d


# In[62]:

df


# In[63]:

pd.DataFrame(d, index=['a', 'b', 'c'])


# In[64]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[65]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']) # Set up data frame with column two and new column three with no data


# In[66]:

df.index


# In[68]:

df.columns



# In[69]:

d = {'one' : [1., 2., 3., 4.],
    'two' : [4., 3., 2., 1.]}


# In[70]:

d


# In[71]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[72]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[73]:

data


# In[74]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])  # Sets up an arrany and defines the type of data it will accept


# In[75]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")] # inserts data into two rows


# In[76]:

data


# In[77]:

pd.DataFrame(data)


# In[78]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])  # Sets up an arrany and defines the type of data it will accept


# In[79]:

pd.DataFrame(data)


# In[80]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")] # inserts data into two rows


# In[81]:

pd.DataFrame(data)


# In[82]:

data[:] = [(10000,2.,'Hello'), (2,3.,"World")] # inserts data into two rows


# In[83]:

pd.DataFrame(data)


# In[84]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")] # inserts data into two rows


# In[85]:

pd.DataFrame(data)


# In[86]:

pd.DataFrame(data, index=['first', 'second'])


# In[87]:

pd.DataFrame(data)


# In[88]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[89]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

pd.DataFrame(data2)


# In[90]:

pd.DataFrame(data2)


# In[91]:

pd.DataFrame(data2, index=['first', 'second'])


# In[92]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[93]:

df


# In[94]:

df['one']


# In[95]:

df['three'] = df['one'] * df['two'] # create column three and execute a calculation


# In[96]:

df


# In[97]:

df['a','b']


# In[98]:

df['a']


# In[99]:

df('a')


# In[100]:

df['flag'] = df['one']>2


# In[101]:

df


# In[102]:

df['flag']


# In[103]:

df['a']


# In[104]:

df[,'a']


# In[105]:

three = df.pop('three')


# In[107]:

df


# In[108]:

fd.loc['a']


# In[109]:

df.loc['a']


# In[110]:

three


# In[111]:

df


# In[112]:

df['three'] = df['one'] * df['two']


# In[113]:

df


# In[114]:

df['foo'] = 'bar'


# In[115]:

df


# In[116]:

df['one_trunc'] = df['one'][:2]


# In[117]:

df


# In[118]:

df.insert(1, 'bar', df['one'])


# In[119]:

df


# In[120]:

df['bar_two] = df['one']']


# In[121]:

df['bar_two] = df['one']


# In[ ]:



