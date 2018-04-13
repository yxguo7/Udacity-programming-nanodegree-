import media

import fresh_tomatoes

toy_story = media.Movie(
	"Toy story", 
	"A story of a boy and his toys that come to life", 
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc" 
	)

fight_club = media.Movie(
	"Fight club", 
	"A depressed man (Edward Norton) suffering from insomnia meets\
	a strange soap salesman named Tyler Durden (Brad Pitt) and soon\
	finds himself living in his squalid house after his perfect apartment \
	is destroyed.", 
	"https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg", 
	"https://www.youtube.com/watch?v=_XgQA9Ab0Gw"
	)

the_wedding_banquet = media.Movie(
	"The Wedding Banquet", 
	"The story of a family", 
	"https://upload.wikimedia.org/wikipedia/zh/8/87/Xiyan-1993_02.jpg", 
	"https://www.youtube.com/watch?v=nlBQrLjzefQ"
	)


movies = [toy_story, fight_club, the_wedding_banquet]

fresh_tomatoes.open_movies_page(movies)
