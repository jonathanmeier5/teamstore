
def team(request):
	"""Return team name """
	team = request.session['team']
	return {'team': team}