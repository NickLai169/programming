class Book:
	language = 'English'
	worn_down = False
	varieties = {}

	def __init__(self, genre, title, author, publication_year):
		self.genre = genre
		self.title = title
		self.author = author
		self.publication_year = publication_year
		return

	def calculate_age(self):
		#Calculates the age of the book by subtracting its publication year from the current year.
		return 2019 - self.publication_year

	def outdated(self, old_age):
		#Determines if the book is outdated. Takes in an old_age and sets worn_down to True.
		return self.calculate_age() > old_age


	def add_genre(self):
		'''If the book's genre isn't in the varieties, then you'll need to add the genre to varieties
		as well as the original book's information. Otherwise, just make sure the book isn't
		inside varieties before you add it!'''
		if self.genre in self.varieties:
			self.varieties[self.genre].append([self.title, self.author])
		else:
			self.varieties[self.genre] = [[self.title, self.author]]

def tester_boooks():
	Eggs = Book('comedy', 'Eggs', 'Nick Lai', 2018)

	print(Eggs.varieties)

	Eggs.add_genre()

	print(Eggs.varieties)

	Lagg = Book('comedy', 'Book of lagg', 'Kevin Lin', 2016)

	print(Eggs.varieties)

	Lagg.add_genre()

	print(Eggs.varieties)

	Rage = Book('rage', 'A day in Daniel Ais life', 'Eli Chang', 2019)

	print(Eggs.varieties)

	Rage.add_genre()

	print(Eggs.varieties)

	print(Book.varieties)

	return

class Textbook(Book):
	publisher = 'Houghton Mifflin Harcourt'

	def random_function(self):
		return 'Do something'

class UCBMFET:
	members = 173532
	topic = 'memes'
	posts = {}

	def __init__(self, name):
		self.name = name
		self.activity = 0
		self.posts = 0
		self.member = True
		UCBMFET.members += 1
		return

	def tag_ur_friend_in_meme(self, friend):
		#Hint: use the isinstance function
		if isinstance(friend, UCBMFET):
			self.activity += 1
			return '@' + friend.name + ' us in CS10!'
		else:
			return 'You cannot tag someone in a meme if they are not a memeber of UCBMFET.'

	def post_in_UCBMFET(self, title_of_post):
		if title_of_post in list(UCBMFET.posts.keys()):
			return 'You have been banned for reposting a meme.'
		else:
			self.activity += 1
			self.posts += 1
			UCBMFET.posts[title_of_post] = 0
			return  'Your total activity on UCMBFET is ' + str(self.activity) + ' , and your total posts to UCBMFET is now ' + str(self.posts)

	def like_a_post_in_UCBMFET(self, title_of_post):
		self.activity += 1
		UCBMFET.posts[title_of_post] += 1
		return 'Your total activity on UCBMFET is ' + str(self.activity) + ' and the total number of likes on the post ' + title_of_post + ' is ' + str(UCBMFET.posts[title_of_post])

Nick = UCBMFET('Nick Lai')
Eli = UCBMFET('Eli Chang')
Daniel = UCBMFET('Daniel Ai')
Book = Book('Comedy', 'Farts are for gay people', 'Eugene Tang', 2019)

def tester_UCB_memes():
	print(Nick.posts)
	print(Nick.tag_ur_friend_in_meme(Eli))
	print(Nick.activity)
	print(UCBMFET.members)
	print(Nick.post_in_UCBMFET('Why do we lick trees?'))
	print(UCBMFET.posts['Why do we lick trees?'])
	print(Daniel.post_in_UCBMFET('Why do we lick trees?'))
	print(Nick.like_a_post_in_UCBMFET('Why do we lick trees?'))

tester_UCB_memes()
