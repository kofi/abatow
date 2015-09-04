from django.db import models
# https://docs.djangoproject.com/en/1.8/topics/db/aggregation/
from django.db.models import Sum
import datetime
import uuid

REGIONAL = 'REG'
CONSTITUENCY = 'CON'
REGION_TYPE_CHOICES = (
    (REGIONAL, 'Regional'),
    (CONSTITUENCY, 'Constituency'),
)

# Create your models here.
class Country(models.Model):
    """docstring for Country"""
    # def __init__(self, arg):
    #     super(Country, self).__init__()
    #    self.arg = arg
    def __str__(self):
        return self.name
    class Meta:
        """docstring for Meta"""
        verbose_name_plural = "countries"
    # def save(self):
    #     """docstring for save"""
    #     self.nameslug = slugify(name)
    #     super(Country, self).save(*args, **kwargs)
                    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=250)
    nameslug = models.SlugField(max_length=64,null=True)
    total_registered = models.BigIntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepopulated_fields = {"nameslug": ("name",)}        

class Congress(models.Model):
    """docstring for Congress"""
    # def __init__(self, arg):
    #     super(Congress, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return self.name
    
    class Meta:
        """docstring for Meta"""
        verbose_name_plural = "congress"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=True)
    year = models.DateField(default=datetime.datetime.today)
    election_date = models.DateField()
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Region(models.Model):
    """docstring for Region"""
    # def __init__(self, arg):
    #     super(Region, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return self.name
    # def save(self):
    #     """docstring for save"""
    #     self.nameslug = slugify(name)
    #     super(Region, self).save(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=250)
    nameslug = models.SlugField(max_length=64,null=True)
    total_registered = models.BigIntegerField(null=True,default=0)
    regiontype_text = models.CharField(max_length=3,
                                        choices=REGION_TYPE_CHOICES,default=CONSTITUENCY)
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepopulated_fields = {"nameslug": ("name",)}
        

class Election(models.Model):
    """docstring for election"""
    # def __init__(self, arg):
    #     super(Election, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return self.name
    def _get_total_votes(self):
        """docstring for _get_total_votes"""
        return self.result_set.all().aggregate(total_votes=Sum('votes'))
    NATIONAL = 'NAT'
    REGIONAL = 'REG'
    CONSTITUENCY = 'CON'
    ELECTION_TYPE_CHOICES = (
        (NATIONAL, 'National'),
        (REGIONAL, 'Regional'),
        (CONSTITUENCY, 'Constituency'),
    )
    congress = models.ForeignKey(Congress)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    electiontype_text = models.CharField(max_length=3,
                                        choices=ELECTION_TYPE_CHOICES,default=CONSTITUENCY)
    region = models.ForeignKey(Region)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.SlugField(max_length=128,null=True)
    prepopulated_fields = {"name": ("congress.name","region.name","electiontype_text",)}
    
    total_votes = property(_get_total_votes)
    
class Party(models.Model):
    """docstring for Party"""
    # def __init__(self, arg):
    #     super(Party, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return self.name
    class Meta:
        """docstring for Meta"""
        verbose_name_plural = "parties"        
    # def save(self):
    #     """docstring for save"""
    #     self.nameslug = slugify(name)
    #     super(Party, self).save(*args, **kwargs)
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=250)
    nameslug = models.SlugField(max_length=64)
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepopulated_fields = {"nameslug": ("name",)}

class Candidate(models.Model):
    """docstring for Candidate"""
    # def __init__(self, arg):
    #     super(Candidate, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return self.fullname
    # def save(self):
    #     """docstring for save"""
    #     self.nameslug = slugify(fullname)
    #     super(Candidate, self).save(*args, **kwargs)      
    def _get_full_name(self):
        """returns the full name """
        if self.middlename is None or len(self.middlename) == 0:
            return '%s %s' % (self.firstname,self.lastname)
        return '%s %s. %s' % (self.firstname,self.middlename[0], self.lastname)
    def _get_full_name_by_lastname(self):
        """docstring for _get_full_name_by_lastname"""
        if self.middlename is None or len(self.middlename) == 0:
            return '%s, %s' % (self.lastname,self.firstname)
        return '%s, %s %s.' % (self.lastname,self.firstname, self.middlename(0))
    
    fullname = property(_get_full_name)
    fullname_by_lastname = property(_get_full_name_by_lastname) 
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(blank=False, max_length=100)
    middlename = models.CharField(blank=True, max_length=100,null=True)
    lastname = models.CharField(blank=False, max_length=100)
    nameslug = models.SlugField(max_length=64)
    party = models.ForeignKey(Party)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepopulated_fields={"nameslug" : ("firstname","middle_initial","lastname",)}

class Result(models.Model):
    """docstring for Results"""
    # def __init__(self, arg):
    #     super(Results, self).__init__()
    #     self.arg = arg
    def __str__(self):
        return '%s | %s' % (self.candidate.fullname, self.election.region.name)
    def save(self, *args, **kwargs):
        """docstring for save"""
        if (self.is_published is True) and (self.date_published is None):
            self.date_published = datetime.datetime.now()
        if (self.is_published is False) and (self.date_published is not None):
            self.date_published = None
        super(Result, self).save(*args, **kwargs)
    
    def _get_region(self):
        return self.election.region.name
    def _get_congress(self):
        return self.election.congress.name
    def _get_electiontype(self):
        return self.election.electiontype_text    
    def _get_party(self):
        return self.candidate.party.name
    def _get_vote_fraction(self):
        myvotes = self.votes 
        allvotes= self.election.total_votes['total_votes']
        print(myvotes)
        print(allvotes)
        return float(myvotes/allvotes)*100
    def vote_percentage(self):
        return u'%.2f%%' % (self.vote_fraction)
        
    election = models.ForeignKey(Election)
    candidate = models.ForeignKey(Candidate)
    votes = models.BigIntegerField(blank=False, null=False, default=0)
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    result_region = property(_get_region)
    result_congress = property(_get_congress)
    result_electiontype = property(_get_electiontype)
    result_party = property(_get_party)
    vote_fraction = property(_get_vote_fraction)
    
    
        