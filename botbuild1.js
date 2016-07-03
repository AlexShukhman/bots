// Bot Build 1

/*
A simple learning bot that has the capacity to guess which source is correct by its level of trust in each source

This bot uses geometric conservatism bias and will weigh the initial data more than later data
    Bot's level of conservatism bias is positively correlated (>dep value --> >bias)
        Conservatism bias is set initially in initialization as dep
	        eg: Bot = LearningBot(dep = x)

	This bot exibits illusion of validity starting at initilization (it believes everything it hears)

	This bot allows for different administrative strength
	    (one can ovverride conservatism biases by changing influence strength when running teachtruthes method)
*/

// (c) Alex Shukhman: July 3, 2016

var LearningBot = {
	
}
