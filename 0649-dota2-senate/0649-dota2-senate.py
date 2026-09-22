class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)) :
            if senate[i] == 'R':
                r.append(i)
            else :
                d.append(i)

        while r and d :
            if r[0] < d[0] :
                d.popleft()
                r.append(r.popleft() + len(senate))
            else :  
                
                r.popleft()
                d.append(d.popleft() + len(senate)) 
        return "Dire" if d else 'Radiant'                     

