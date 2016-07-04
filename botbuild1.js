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


//////////////////////////////////Bot Object////////////////////////////////////////////////
var base = {}; // grandparent for all instances
var LearningBot_instance = Object.create(base); // parent to all LearningBots

LearningBot_instance.__init__ = function(dep, truthesmem, truthesbelief)
{
	this.initbelief = 1;
	this.belief = this.initbelief; // current level of disbelief
	if (typeof dep === 'undefined') { this.dep = 1.5; } else {this.dep = dep;} // how fast belief depreciates
	if (typeof truthesmem === 'undefined') { this.truthesmem = []; } else {this.truthesmem = truthesmem;} //  a list of 4 element lists of 2 element lists, first element is the input (4 possibilities), second is its value
	if (typeof truthesbelief === 'undefined') {this.truthesbelief = {}} else {this.truthesbelief = shallowCopy(truthesbelief);} // a dictionary of weighted belief in each input
	this.truthesbelief_tot = shallowCopy( this.truthesbelief );
}

function shallowCopy( original ) // function shallowcopy used in initializer (LearningBot_instance.__init__)
{
	var clone = Object.create( Object.getPrototypeOf( original ));
	var i , keys = Object.getOwnPropertyNames( original ); 
	for ( i = 0; i < keys.length ; i++) 
	{
		Object.defineProperty( clone , keys[ i ], Object.getOwnPropertyDescriptor( original, keys[i]));
	}
	return clone;
}

var LearningBot = function(dep,truthesmem,truthesbelief) // creator function for LearningBot_instance
{
	var instance = Object.create ( LearningBot_instance);
	instance.__init__(dep,truthesmem,truthesbelief);
	return instance;
}

LearningBot_instance.teachTruthes = function (info, influence) // info is a list of 4 elements of len2 lists, influence is a value <=1
{
	if (typeof influence === 'undefined') {var influence = 1;}
	this.truthesmem.push(info);
	this.thinkTruthes(info,influence);
}
function evenate ( d ) // sets total of dictionary values to 1
{
	var total = 0;
        var dic = shallowCopy(d);
	for (var i in dic){total+=dic[i];}
	for (var i in dic){ try{dic[i] /= total} catch(e){dic[i]=0} }
	return dic;
}
LearningBot_instance.thinkTruthes = function (info, influence) // data processing
{
	var beliefdict = {};
	for (var i = 0; i < info.length -1; i++)
	{
		if (info[info.length-1][1] === info[i][1])
		{
			if (info[i][0] in beliefdict)  {beliefdict[info[i][0]]++}
			else {beliefdict[info[i][0]]=1;}
		}
	}
	for (var i = 0; i < info.length -1; i++)
	{
		if (!(info[i][0] in beliefdict)){beliefdict[info[i][0]] = 0;}
	}
	beliefdict = evenate(beliefdict);
	for (var i in beliefdict)
	{
		if ( i in this.truthesbelief_tot ) { this.truthesbelief_tot[i]+=((beliefdict[i]/this.belief)*influence);}
		else {this.truthesbelief_tot[i]=((beliefdict[i]/this.belief)*influence);} 
	}
	this.truthesbelief = evenate(this.truthesbelief_tot);
	this.belief /= this.dep;
}
/////////////////////////////////End Bot Object////////////////////////////////////////////

/////////////////////////////////Test//////////////////////////////////////////////////////

var botA = LearningBot(1.2);
var a = 'a';
info = [[[1,1],[2,0],[3,1],[10,1]],[[4,1],[2,0],[3,1],[10,1]],[[3,1],[2,1],[4,0],[10,0]],[[1,0],[2,1],[3,1],[10,0]],[[1,1],[2,0],[3,1],[10,0]],[[5,0],[2,1],[3,1],[10,0]],[[1,0],[2,1],[3,1],[10,0]]];
for (var i in info)
{
	botA.teachTruthes(info[i]);
}
console.log(botA.truthesbelief);
