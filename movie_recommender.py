import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# Fetch data and format it
data = fetch_movielens(min_rating=4.0)

# Print training and testing data
print(repr(data['train']))
print(repr(data['test']))

# Create model
model1 = LightFM(loss='warp')
model2 = LightFM(loss='logistic')
model3 = LightFM(loss='bpr')
model4 = LightFM(loss='warp-kos')
# Train model
model1.fit(data['train'], epochs=30, num_threads=2)
model2.fit(data['train'], epochs=30, num_threads=2)
model3.fit(data['train'], epochs=30, num_threads=2)
model4.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

	# Number of users and movies in training data
	n_users, n_items = data['train'].shape

	# Generate recommendations for each user we input
	for user_id in user_ids:

		# Movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		# Movies our model predicts they will like
		scores = model.predict(user_id, np.arange(n_items))
		# Rank them in order of most liked to least liked
		top_items = data['item_labels'][np.argsort(-scores)]

		# Print out the results
		print("User %s" % user_id)
		print("    Known Positives:")

		for p in known_positives[:3]:
			print("        %s" % p)

		print("    Recommended:")

		for i in top_items[:3]:
			print("        %s" % i)

print("Warp")
sample_recommendation(model1, data, [3, 25, 450])
print("Logistic")
sample_recommendation(model2, data, [3, 25, 450])
print("BPR")
sample_recommendation(model3, data, [3, 25, 450])
print("Warp-Kos")
sample_recommendation(model4, data, [3, 25, 450])
