from django.db import models

# Create your models here.
"""
1.Defining Model Classes
2.Model Migration
    First Generate migration files (No tables will be generated in the database, only a correspondence between the data table and the model will be created.)
        python3 manage.py makemigrations
        python3 manage.py migrate
    Re-migration (will generate tables in the database)
3.Manipulating the database

Where to define the model
Who the model inherits from
ORM Correspondence
 -> Table - Classes
 -> Fields - Properties
"""


class BookInfo(models.Model):
    """
    1.Primary Key Currently auto-generated
    """
    name = models.CharField(max_length=10, unique=True, verbose_name='Name')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # django automatically added an attribute for us, This attribute makes it possible to look up character information through books
    # peopleinfo_set

    class Meta:
        # Change table name
        db_table = 'bookinfo'
        # Modify the configuration of the display information of the backend admin.
        verbose_name = 'admin'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # ordered dictionary
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='Name')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='Gender')
    description = models.CharField(max_length=200, null=True, verbose_name='Description')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='Book')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='LogicDelete')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = 'People info'

    def __str__(self):
        return self.name
