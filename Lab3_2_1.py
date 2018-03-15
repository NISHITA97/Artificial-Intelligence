import sys
from collections import defaultdict
import Queue as Q
class Graph:
    def __init__(self,len1):
        self.data=[];
        self.V=len1;
        for row in range(0,len1):
            cr=[];
            for col in range(0,len1):
                cr.append(0);
            self.data.append(cr);
        print self.data;

    def adding(self,row, col):
        self.data[row][col]=1;
        self.data[col][row]=1;


    def dipp(self, dist):
        print "Vertex tDistance from Source"
        for node in range(self.V):
            print node,"t",dist[node]
 
   
    def mkdt(self, dist, sptSet):
 
        mk = sys.maxint
 
        for v in range(self.V):
            if dist[v] < mk and sptSet[v] == False:
                mk = dist[v]
                mk_index = v
 
        return mk_index
 
    def djks(self, src):
 
        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
            u = self.mkdt(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.data[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.data[u][v]:
                        dist[v] = dist[u] + self.data[u][v]
        self.hu=dist; 


    def bfs(self,src,dest,dict):
        self.djks(dest);
        q = Q.PriorityQueue()
        print "bfs";
        q.put((self.hu[src],src));
        while not q.empty():
            ele1=q.get();
            cs=ele1[1];
            print ele1 , dict[cs];
            if(self.hu[cs]==0):
                break;
            for vers in range(0,self.V):
                if(self.data[cs][vers]==1 ):
                    q.put((self.hu[vers],vers));

    def HillClimbing(self,src,dest,dict):
        self.djks(dest);
        q = Q.PriorityQueue()
        print "HillClimbing";
        q.put((self.hu[src],src));
        while not q.empty():
            ele1=q.get();
            cs=ele1[1];
            print ele1 , dict[cs];
            if(self.hu[cs]==0):
                break;
            q2 = Q.PriorityQueue()
            for vers in range(0,self.V):
                if(self.data[cs][vers]==1 ):
                    q2.put((self.hu[vers],vers));
            minele=q2.get();
            q.put(minele);

        
        
ifile = open(sys.argv[1],'r');
ofile=open(sys.argv[2],'w');
read=ifile.readlines();
line1=read[0];
vtx=[];
t=[];
rows=len(read);
source=read[1][0];
dict={};
dest=read[rows-2][0];
for i in range(0,26):
    dict[chr(ord('a')+i)]=i;

dict2={};
for i in range(0,26):
    dict2[i]=chr(ord('a')+i);
print dict;
for ch in line1:
    if(ch!=',' and ch!='\n'):
        vtx.append(ch);

len1 = len(vtx);
g=Graph(len1);
for i in range(len(read[0])-1):
    if(i%2==0):
        vtx.append(read[0][i]);
for i in range(2,rows-2):
    src=read[i][0];
    des=read[i][2];
    g.adding(dict[src],dict[des]);

g.HillClimbing(dict[source],dict[dest],dict2);
