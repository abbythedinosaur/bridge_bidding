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

Once you input those variables, the program will determine whether the hand is balanced or unbalanced, move to the appropriate
if/elif structure, and produce a suggested bid. 

