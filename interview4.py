NVIDIA GRID GAME STREAMING: http://shield.nvidia.com/grid-game-streaming/
NVIDIA PROFESSIONAL APP STREAMING: https://trial.gimli.nvidiagrid.net/accounts/register/?source=USA

1->2->3->4->5
1->2->4->5

3 = 3.next
3.next = 3.next.next

[a1, a2, a3, b1, b2, b3]

a2 = 1
b2 = 5

Size = 2n
[a1, a2, a3, a4, .... an, b1, b2, b3, b4, ... bn]
[a1, b1, a2, b2, a3, b3................an, bn]

[a1, a2, a3, a4, b1, b2, b3, b4]

def rearrange(alist):
  inc = 0
  while inc <= len(alist)/2:
    if i % 2 == 1:
     temp = alist[inc]
     alist[inc] = alist[len(alist)-inc]
     alist[len(alist)-inc] = temp
    inc = inc+1
    
   return alist
