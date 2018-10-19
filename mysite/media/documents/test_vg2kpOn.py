import espn_api_v3 as espn


scores = espn.get_scores(espn.NCAA_FB)
for game in scores:
	print(scores[game][0], scores[game][1])
	print(scores[game][2], scores[game][3])
	print(scores[game][4], "\n")

	# for item in scores[game]:
		# print(item)

