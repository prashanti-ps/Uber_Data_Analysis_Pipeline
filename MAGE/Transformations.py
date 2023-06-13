#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
from datetime import datetime


# In[161]:


df=pd.read_csv("../Downloads/uber_data.csv")


# In[162]:


df.head()


# In[163]:


df.info()


# In[164]:


df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.strftime('%Y-%m-%d %H:%M' )
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime']).dt.strftime('%Y-%m-%d %H:%M' )


# In[165]:


df.info()


# ## Date Dimension

# In[166]:


date_dim = pd.DataFrame()
date_dim['Date'] = pd.date_range(start='1/1/2016', end='01/01/2017')


# In[167]:


date_dim.info()


# In[168]:


date_dim['Date_value'] = date_dim['Date'].astype(str)
date_dim['Date_id'] = date_dim['Date_value'].apply(lambda x: x.replace('-', '')).astype(int)
date_dim['DayOfMonth'] = date_dim['Date'].dt.day
date_dim['DayOfWeek'] = date_dim['Date'].dt.dayofweek
date_dim['Day'] = date_dim['Date'].dt.day_name(locale = 'English')
date_dim['Month'] = date_dim['Date'].dt.month
date_dim['Year'] = date_dim['Date'].dt.year


# In[169]:


date_dim = date_dim.drop('Date', axis=1)


# In[170]:


date_dim.head()


# ## Time Dimension

# In[171]:


res = []
for i in range(0,24):
    for j in range(0, 60):
        dic = {}
        dic['24_hour'] = i
        dic['Minute_in_hour'] = j
        res.append(dic)


# In[172]:


dim_time = pd.DataFrame(res)
dim_time.head()


# In[173]:


dim_time.index+= 1 


# In[174]:


dim_time.reset_index(inplace = True)


# In[175]:


dim_time.rename(columns={'index': 'Time_id'}, inplace=True)
dim_time['Time_Value'] = dim_time['24_hour'].astype(str).str.zfill(2) + ':' + dim_time['Minute_in_hour'].astype(str).str.zfill(2)
dim_time['Time_Value'] = pd.to_datetime(dim_time['Time_Value']).dt.strftime('%H:%M')
dim_time.head()


# ## Rate Dimension

# In[176]:


dic = {'Rate_id': [1,2,3,4,5,6], 'Code_Name': ['Standard Rate','JFK', 'Newark', 'Nassau or Westchester', 'Negotiated Fare', 'Group ride']  }
dim_rate = pd.DataFrame.from_dict(dic)


# In[177]:


dim_rate.head()


# ## Vendor Dimension

# In[178]:


dic = {'Vendor_id': [1,2], 'Code_Name': ['Creative Mobile Technologies','VeriFone Inc.']}
dim_vendor = pd.DataFrame.from_dict(dic)


# In[179]:


dim_vendor


# ## Payment Dimension

# In[180]:


dic = {'Payment_id': [1,2,3,4,5,6], 'Code_Name': ['Credit card','Cash', 'No CHarge', 'Dispute', 'Unknown', 'Voided Trip']  }
dim_payment = pd.DataFrame.from_dict(dic)


# In[181]:


dim_payment


# ## Fact Table

# In[193]:


fact_table=df.merge(dim_payment, left_on='payment_type', right_on='Payment_id',how='inner')\
             .merge(dim_vendor, left_on='VendorID', right_on='Vendor_id',how='inner')\
             .merge(dim_rate, left_on='RatecodeID', right_on='Rate_id',how='inner')\
             .merge(date_dim, left_on=pd.to_datetime(df['tpep_pickup_datetime']).dt.strftime('%Y-%m-%d'), right_on='Date_value',how='inner')\
             .merge(date_dim, left_on=pd.to_datetime(df['tpep_dropoff_datetime']).dt.strftime('%Y-%m-%d'), right_on='Date_value',how='inner')\
             .merge(dim_time, left_on=pd.to_datetime(df['tpep_pickup_datetime']).dt.strftime('%H:%M'), right_on='Time_Value',how='inner')\
             .merge(dim_time, left_on=pd.to_datetime(df['tpep_dropoff_datetime']).dt.strftime('%H:%M'), right_on='Time_Value',how='inner')


# In[194]:


fact_table


# In[192]:


fact_table.columns


# In[195]:


fact_table=fact_table[['Vendor_id','Date_id_x','Time_id_x','Date_id_y','Time_id_y','Rate_id',
                      'Payment_id','passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'store_and_fwd_flag',
                      'dropoff_longitude', 'dropoff_latitude', 'fare_amount', 'extra', 'mta_tax', 'tip_amount','tolls_amount', 'improvement_surcharge',
                      'total_amount']]


# In[196]:


fact_table.head()


# In[197]:


fact_table.rename(columns={'Date_id_x': 'Pickup_Date_id','Date_id_y':'Drop_Date_id',
                          'Time_id_x':'Pickup_Time_id','Time_id_y':'Drop_Time_id'}, inplace=True)


# In[199]:


fact_table.head()


# In[ ]:




