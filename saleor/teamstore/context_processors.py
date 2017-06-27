
def team(request):
	"""Return team name """
	if 'team' in request.session:
		team = request.session['team']
	else:
		team = 'none'
	return {'team': team}