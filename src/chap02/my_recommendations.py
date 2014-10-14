from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(prefs, person1, person2):
	# Get the list of shared items
	si={}
	for item in prefs[person1]:
		for item2 in prefs[person2]:
			if item==item2:
				si[item]=1

	if len(si)==0: return 0

	sum_of_squares=sqrt(sum([pow(prefs[person1][item]-prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]]))

	return 1/(sum_of_squares+1)

def sim_pearson(prefs, person1, person2):
	si={}
	for item in prefs[person1]:
		for item in prefs[person2]:
			si[item]	= 1

	n = len(si)

	if n==0:
		return 0;

	# sum up all the preferences
	sum_si_1	= sum([prefs[person1][item] for item in si])
	sum_si_2	= sum([prefs[person2][item] for item in si])

	# sum up the squares
	sum_si_square_1	= sum([pow(prefs[person1][item],2) for item in si])
	sum_si_square_2	= sum([pow(prefs[person2][item],2) for item in si])

	# sum up the products
	sum_products	= sum([prefs[person1][item]*prefs[person2][item] for item in si])

	# calculate Pearson score
	num		= sum_products-(sum_si_1*sum_si_2/n)
	denom	= sqrt((sum_si_square_1-pow(sum_si_1,2)/n)*(sum_si_square_2-pow(sum_si_2,2)/n))
	if denom==0:
		return 0

	r	= num/denom

	return r

def topMatches(prefs, person, similarity=sim_pearson):
	scores	= [(similarity(prefs, person, other), other) for other in prefs if other!=person]

	scores.sort()
	scores.reverse()
	return scores

def getRecommendations(prefs, person, similarity=sim_pearson):
	for other in prefs:
		if other==person:
			continue;

		sim	= similarity(prefs, person, other)
		
