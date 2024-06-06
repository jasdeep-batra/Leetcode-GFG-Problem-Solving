class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        #can we use set

        for j in range(len(hand)):
            if hand[j]==-1:
                continue
            nextt = hand[j]+1
            for i in range(1,groupSize):
                if nextt not in hand:
                    
                    return False
                else:
                    ind = hand.index(nextt)
                    hand[ind] = -1
                nextt = nextt+1
            hand[j] = -1                
        return True
                



        

        