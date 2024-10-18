
"""
Similar to ipython
python3 manage.py shell

"""



############################## Add data ##############################
from book.models import BookInfo
# Method 1
# It will return the newly generated object to us.
book = BookInfo(
    name='python',
    pub_date='2024-01-01',
)
# The save method needs to be called manually
book.save()

# Method 2
# Direct access to storage
# objects: management classes for models
# Find it for all additions, deletions, and changes to the model.
BookInfo.objects.create(
    name='java',
    pub_date='2024-01-02'
)

############################## Modify(Update) data ##############################
from book.models import BookInfo
# Method 1
# 1. Query the data first
# select * from bookInfo where id=1
book = BookInfo.objects.get(id=1)

# 2. Modify the properties of the instance directly
book.readcount = 20

# 3. Call the save method
book.save()

# Method 2: Direct update
# filter
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200
)

############################## Delete data ##############################
# Method 1
# 1. First query out the data
book = BookInfo.objects.get(id=5)
# 2. Call the delete method
book.delete()

# Method 2
BookInfo.objects.filter(id=6).delete()

############################## Basic Inquiry ##############################
# get
# all
# count

# select * from bookInfo where id = 1
# Return an object
book = BookInfo.objects.get(id=1)
# Querying data with a non-existent id throws an exception.
# book = BookInfo.objects.get(id=100)

try:
    book = BookInfo.objects.get(id=100)
except BookInfo.DoesNotExist:
    pass

# Returns all results that are lists
BookInfo.objects.all()
# count
BookInfo.objects.all()

############################## filter get exclude ##############################
"""
select * from bookInfo where conditional statement
Equivalent to a where query
filter: Filter n results
get: Return 1 result
exclude: Excluding the remaining results that match the condition is equivalent to not

Syntactic form: as filter (field name __ operator = value)

"""
# Search for book number 1
BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(id=1)
# Search for books with titles containing '湖'
BookInfo.objects.filter(name__contains='湖')
# Search for books with titles ending in '部'
BookInfo.objects.filter(name__endswith='部')
# Search for books with empty titles
BookInfo.objects.filter(name__isnull=True)
# Query books numbered 1 or 3 or 5
BookInfo.objects.filter(id__in=[1, 3, 5])
# Query books with number greater than 3
# gt greater than
# gte greater and equal
# lt less than
BookInfo.objects.filter(id__gte=3)
# Query books with book ids other than 3
BookInfo.objects.exclude(id=3)
# Search for books published in 1980
BookInfo.objects.filter(pub_date__year='1980')
# Search for books published after January 1, 1990
BookInfo.objects.filter(pub_date__gt='1990-1-1')


############################## F ##############################
# How to compare two attributes?
"""
F Syntactic forms of F-objects

filter (field name __ operator = F('value'))
Query books with reads greater than or equal to reviews
"""
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# Query books with more than 2x the number of reviews read.
BookInfo.objects.filter(readcount__gte=F('commentcount') * 2)

############################## Q ##############################
# Query books with an id greater than 2 and a read count greater than 20.
# Method 1
# filter().filter()
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)

# Method 2
# filter(Condition, condition)
BookInfo.objects.filter(id__gt=2, readcount__gt=20)

"""
Q(field name __ operator = value)

Or   Q()|Q()
And  Q()&Q()
not  ~Q()
"""
# Query books with an id greater than 2 or a read count greater than 20.
from django.db.models import Q
BookInfo.objects.filter(Q(id__gt=2) | Q(readcount__gt=20))

# Query books with book ids other than 3
BookInfo.objects.filter(~Q(id=3))

############################## Aggregate function ##############################
"""
Sum,Max,Min,Avg,Count
The aggregate function requires the use of aggregate
The syntax is of the form: aggregate(Xxx('field'))
"""
# Total number of readings of current data
from django.db.models import Sum,Avg,Max,Min,Count
BookInfo.objects.aggregate(Sum('readcount'))

############################## Sort ##############################
# Default ascending order
BookInfo.objects.all().order_by('readcount')
# Descending order
BookInfo.objects.all().order_by('-readcount')

############################## Related queries ##############################
"""
The relationship between books and characters is: one to many
The books don't have any fields for characters
People have fields about books    book Foreign key

Grammatical forms:
 - Query character information by book (known master table data, correlation query slave table data)
 - Main table model(instance object).associated model class name lowercase_set
 
 - Query book information by character (known data from slave table, associated query master table data)
 - From the table model (instance object) . Foreign keys
"""
# Query information for all characters whose book is 1
# Searching for Characters through Books
# 1.Search for books
book = BookInfo.objects.get(id=1)
# 2.Relate Character Information to Books
book.peopleinfo_set.all()

from book.models import PeopleInfo
# Search for books with character 1
# Based on the books, look up the characters
# 1.Search People
person = PeopleInfo.objects.get(id=1)
# 2.Search for books based on character associations
# person.book: instance object
person.book
person.book.name

############################## Filtering of Linked Queries ##############################
"""
The relationship between books and characters is: one to many
The books don't have any fields for characters（Don't think about the field that's hidden）
People have fields about books    book Foreign key
"""
"""
Book query with “郭靖” as the character.
Search for books with character descriptions that include the word “eight”.
Grammatical forms:
    What we need is book information, and the known conditions are character information
    What we need is the master table information and the known condition is the slave table information
    filter(Associative model class name lowercase __ field __ operator = value)
"""
# Book query with “郭靖” as the character.
# Books are needed.The condition is that the characters
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')
# Search for books with character descriptions that include the word “八".
BookInfo.objects.filter(peopleinfo__description__contains='八')

"""
Search for all characters with the title “The Eight Dragons”.
Search for all characters with book reads greater than 30

Grammatical forms:
    What we need is character information, and the known condition is book information
    We need data from a table, and the known condition is the main table information
"""
# Search for all characters with the title “The Eight Dragons”.
PeopleInfo.objects.filter(book__name='天龙八部')
# Search for all characters with book reads greater than 30
PeopleInfo.objects.filter(book__readcount__gt=30)

############################## Query set ##############################
[book.id for book in BookInfo.objects.all()]
# optimisation
books = BookInfo.objects.all()


############################## Pagination ##############################
from django.core.paginator import Paginator
books = BookInfo.objects.all()
# object_list: Result sets/lists
# per_page: Number of records per page
p = Paginator(books, 2)

# Number of records per page
books_page = p.page(1)
