# bridge_bidding
A program that tells you how to bid in an opening round of bridge

For anyone who might be unfamiliar, bridge is a game played with two sets of partners. 
After the entire deck is dealt (13 cards per person), the game begins with a round of bidding. 

Bidding serves two main purposes: one, to communicate something to your partner about what you have in your hand.
Two, it will determine what the 'trump' suit is (which you want to play to your advantage) and how points will be 
accumulated at the end of the round. 
  
This program is designed to tell the first person, i.e. the opening bidder, how to bid. It will ask the user for two
types of quantities: one, the length of each suit (literally, how many cards in the suit they have). Two, the strength of 
that suit, which is determiend by high card points (HCP). These are calculated as follows:

  ace: 4 points
  king: 3 points
  queen: 2 points
  jack: 1 point

To use this program, first you will need to be able to run python on your computer. This program requires user input, so I reccomend using an environment that has a reasonable user interface (I used PyCharm). Next, you will need your deck of cards. Deal yourself a hand of 13 cards. The program will ask how many cards you have in each particular suit, starting with clubs, along with how many points you have in each suit (calculated using the point system listed above). Input the length of each suit, and then how many points are in that suit. Once you get to spades, the program will know how many cards you have left. All you will need to do is input the number of points you have in spades. 

Please be sure to only input whole, positive numbers (the program will reject anything that is not a positive integer). 

Once you have input the card counts and points into the program, it will tell you how you should bid as opening bidder. This program can be used for practice (learning to bid properly is difficult!), or during a casual game of bridge, when your partner and opposing team do not mind a little technological support. 



