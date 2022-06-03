#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install autoscraper')


# In[3]:


from autoscraper import AutoScraper


# In[8]:


Flipkart_url="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_c3d2cdb0-60bb-4e27-bd9a-50c46d017f41_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=cq6hg5vleo0000001654287836931"
wanted=["realme Narzo 30 5G (Racing Blue, 128 GB)","₹16,999","5% off"]


# In[9]:


scraper=AutoScraper()
result=scraper.build(Flipkart_url,wanted)
print(result)


# In[ ]:





# In[ ]:




