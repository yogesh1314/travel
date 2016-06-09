from django.db import models

REVIEW_CHOICES = (('5', 'Very Good'), ('4', 'Good'),('3', 'Average'),('2', 'Poor'), ('1','Very Poor'))

REACH_CHOICES = (('AIR', 'By Air'), ('BUS', 'By Bus'), ('TRAIN', 'By Train'))

class HomeImages(models.Model):
	image = models.ImageField(upload_to="home/")
	def __str__(self):
		return str(self.image)

class Destination(models.Model):	
	title = models.CharField(unique = True, max_length=30)
	overview = models.CharField(max_length=1000)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	indian = models.BooleanField(default = True)
	hotcount = models.IntegerField(default = 0)
	def __str__(self):
		return "%s" %(self.title)

def destphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return str('destination/'+instance.destination.title+'/images/'+name+'.'+ext)

class DestinationImages(models.Model):
    destination = models.ForeignKey(Destination)
    image = models.ImageField(upload_to=destphotoname)
    def __str__(self):
    	return "%s, %s" % (self.destination.title, self.image)

def things_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/things/'+name+'.'+ext

class Things(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 1000)
	photo = models.ImageField(upload_to = things_photo_name)
	def __str__(self):
		return "%s %s" %(self.destination.title, self.title)

def wtrphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/waystoreach/'+name+'.'+ext

class WaysToReach(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(max_length = 10, choices = REACH_CHOICES, default = REACH_CHOICES[0][0])
	description = models.CharField(max_length = 1000)
	photo = models.ImageField(upload_to = wtrphotoname)
	def __str__(self):
		return "%s %s" %(self.destination, self.title)

def attrphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/attractions/'+name+'.'+ext

class Attractions(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(unique = True, max_length = 50)
	description = models.CharField(max_length = 1000)
	photo = models.ImageField(upload_to = attrphotoname)
	def __str__(self):
		return "%s %s" %(self.destination, self.title)

def musteatphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/musteat/'+name+'.'+ext

class MustEat(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(unique = True, max_length = 50)
	address = models.CharField(max_length = 1000)
	price_for_two = models.CharField(max_length = 30)
	photo = models.ImageField(upload_to = musteatphotoname)
	def __str__(self):
		return "%s %s" %(self.destination, self.title)

def mustbuyphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/mustbuy/'+name+'.'+ext

class MustBuy(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(max_length = 50, unique = True)
	photo = models.ImageField(upload_to = mustbuyphotoname)
	def __str__(self):
		return "%s %s" %(self.destination, self.title)

def shoppingplacesphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return 'destination/'+instance.destination.title+'/shoppingplaces/'+name+'.'+ext

class ShoppingPlaces(models.Model):
	destination = models.ForeignKey(Destination)
	title = models.CharField(unique = True, max_length = 50)
	description = models.CharField(max_length = 1000)
	photo = models.ImageField(upload_to = shoppingplacesphotoname)
	def __str__(self):
		return "%s %s" %(self.destination, self.title)

class WhenToVisit(models.Model):
	destination = models.ForeignKey(Destination)
	jan = models.BooleanField()
	feb = models.BooleanField()
	mar = models.BooleanField()
	apr = models.BooleanField()
	may = models.BooleanField()
	jun = models.BooleanField()
	jul = models.BooleanField()
	aug = models.BooleanField()
	sep = models.BooleanField()
	oct = models.BooleanField()
	nov = models.BooleanField()
	dec = models.BooleanField()
	def __str__(self):
		return "%s %s" %(self.destination, self.id)

class Restaurants(models.Model):
	#From Zomato API.
	pass

# Description of Itineary should be in HTML text and 
# render as html only.
class Itinerary(models.Model):
	destination = models.ForeignKey(Destination)
	description = models.CharField(max_length = 1500)
	def __str__(self):
		return "%s %s" %(self.destination.title, self.description)

#mail to admin as an alert
class Review(models.Model):
	title = models.CharField(max_length = 30)
	description = models.CharField(max_length = 5000)
	creator_name = models.CharField(max_length = 70)
	creator_contact_no = models.IntegerField(default = 91,blank=True, null=True)
	creator_email = models.EmailField()
	creator_rating = models.CharField(max_length = 30, choices=REVIEW_CHOICES, default = REVIEW_CHOICES[0][0])
	created_on = models.DateTimeField(auto_now_add=True)
	is_visible = models.BooleanField(default=False)
	def __str__(self):
		return str(self.title)

def reviewphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	x = instance.review.title.strip()
	return 'review/'+x+'/images/'+name+'.'+ext

class ReviewImages(models.Model):
	review = models.ForeignKey(Review)
	image = models.ImageField(upload_to = reviewphotoname)
	def __str__(self):
		return "%s %s" %(self.review.title, self.id)