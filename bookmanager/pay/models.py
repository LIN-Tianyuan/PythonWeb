from django.db import models
"""
1.ORM
Table - Class
Fields -> Properties

2. The model class needs to inherit from models.Model.
3. The model class will automatically add (generate a primary key) for us.
4. Attribute name = Attribute type (option)
    Attribute names: don't use Python, mysql keywords. Do not use continuous underlining.
    Attribute type: similar to mysql type
    Options: charfield must set max_length
             null      Whether or not it is empty
             unique    
             default
             verbose_name Mainly backend displays
    
    
"""
"""
Book table: id,name,pub_date,readcount,commentcount,is_delete
"""
# Create your models here.
