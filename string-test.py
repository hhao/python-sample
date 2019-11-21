#!/usr/bin/env python
# coding: utf-8

# In[105]:


content = 'this is a test string.'


# In[106]:


assert content == ' '.join(('this','is','a','test','string.'))


# In[107]:


assert len(content) == 22


# In[108]:


assert max(content) == 't'


# In[109]:


assert content.capitalize() ==  'This is a test string.'


# In[110]:


assert content.title() == 'This Is A Test String.'


# In[111]:


assert content.find('test string', 5) == 10


# In[112]:


assert content.startswith('this is')


# In[113]:


tab_content = 'this\tis\ta\ttest\tstring.'


# In[114]:


assert tab_content.expandtabs() == 'this    is      a       test    string.'


# In[115]:


assert tab_content.islower()


# In[119]:


locals()


# In[ ]:




