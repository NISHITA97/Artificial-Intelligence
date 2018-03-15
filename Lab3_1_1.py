import sys
from collections import defaultdict
import Queue as Q
input1 = sys.argv[1]
output1 = sys.argv[2]

filein = open(input1,'r')
fileout = open(output1,'w')

class state:
    def __init__(self,vp,c1,c2,c3,c4):
        self.position=vp;
        self.rm=[vp,c1,c2,c3,c4];
        self.hu=self.hust();

    def comp(self,temp):
        ans=cmp(self.rm,temp.rm)==0;
        #print ans;
        return ans;

    def printstate(self):
        print str(self.rm),"heu=" , self.hu;

    def isDest(self):
        r1 = self.rm[1]==0;
        r2 = self.rm[2]==0;
        r3 = self.rm[3]==0;
        r4 = self.rm[4]==0;
        return r1 and r2 and r3 and r4;

    def hust(self):
        r1 = self.rm[1]==1;
        r2 = self.rm[2]==1;
        r3 = self.rm[3]==1;
        r4 = self.rm[4]==1;
        cnt=0;
        if(r1):
            cnt+=1;
        if(r2):
            cnt+=1;
        if(r3):
            cnt+=1;
        if(r4):
            cnt+=1;
        if(cnt==4):
            return 7;
        elif(cnt==0):
            return 0;
        elif(cnt==1):
            if(self.rm[self.position]==1):
                return 1;
            if(r1==False):
                dirt=1;
            elif(r2==False):
                dirt=2;
            elif(r3==False):
                dirt=3;
            else:
                dirt=4;

            if((r1 and self.position==4) or (self.position==1 and r4) or(self.position==3 and r2) or (self.vpos==2 and r3)):
                return 3;
            return 2;
        elif(cnt==2):
            #daigonal
            if((r1 and r4) or (r2 and r3)):
                if(self.rm[self.vpos]==1):
                    return 4;
                else:
                    return 5;

            elif(self.rm[self.vpos]==1):
                return 3;
            return 4;
        else:
            #cnt=3
            if((r1 and self.vpos==1) or (r2 and self.vpos==2) or(r3 and self.vpos==3) or(r4 and self.vpos==4)):
                return 6;
            elif((r1 and self.vpos==4) or(r2 and self.vpos==3) or (r3 and self.vpos==2) or (r4 and self.vpos==1)):
                return 6;
            return 5;
        
class Graph:
    def __init__(self,src):
        self.config=[]
        cnt=0;
        for pos in range(1,5):
            for r1 in range(0,2):
                for r2 in range(0,2):
                    for r3 in range(0,2):
                        for r4 in range(0,2):
                            self.config.append(state(pos,r1,r2,r3,r4));
                            
                            cnt+=1;
        #print self.config;
        self.src=src;
        self.count=cnt;
    def rt(self,source):
        if((source.vpos==1) or (source.vpos==3)):
            dest=state(int(source.vpos)+1,int(source.rm[1]),int(source.rm[2]),int(source.rm[3]),int(source.rms[4]));
            for idx in range(0,self.count):
                if(dest.comp(self.config[idx])==True):
                    return idx;
        return -1;

    def lft(self,source):
        if((source.position==2) or (source.position==4)):
            dest=state(int(source.position)-1,int(source.rms[1]),int(source.rms[2]),int(source.rms[3]),int(source.rms[4]));
            for idx in range(0,self.count):
                if(dest.comp(self.config[idx])==True):
                    return idx;
        return -1;

    def upper(self,source):
        if((source.position==3) or (source.position==4)):
            dest=state(int(source.position)-2,source.rms[1],int(source.rms[2]),int(source.rms[3]),int(source.rms[4]));
            for idx in range(0,self.count):
                if(dest.comp(self.config[idx])==True):
                    return idx;
        return -1;

    def down(self,source):
        if((source.position==1) or (source.position==2)):
            dest=state(int(source.position)+2,int(source.rms[1]),int(source.rms[2]),int(source.rms[3]),int(source.rms[4]));
            for idx in range(0,self.count):
                if(dest.comp(self.config[idx])==True):
                    return idx;
                    break;
        return -1;

    def suck(self,source):
        pos=int(source.position);
        if(source.rms[pos]==0):
            return -1;
        dest=state(source.position,int(source.rms[1]),int(source.rms[2]),int(source.rms[3]),int(source.rms[4]));
        dest.rms[pos]=0;
        for idx in range(0,self.count):
            if(dest.comp(self.config[idx])==True):
                return idx;
                
       

    def search(self,state):
        for idx in range(0,self.count):
            if(state.comp(self.config[idx])==True):
                return idx;

    def printGraph(self):
        for K in self.config:
            K.printstate();


    def bfs(self):
        q = Q.PriorityQueue()
        print "bfs";
        q.put((self.src.hu,self.src,'N'));
        #q.put((1,"j"))
        #q.put((5,"kk"))
        while not q.empty():
            ele1=q.get();
            #print ele1;
            state=ele1[1];
            print state.printstate(),ele1[2];
            if(state.hu==0):
                break;
            suck=self.suck(state);
            if(suck!=-1):
                suck=self.config[suck];
                q.put((suck.hu,suck,'S'));

            up=self.upper(state);
            if(up!=-1):
                up=self.config[up];
                q.put((up.hu,up,'U'));
            suck=self.down(state);
            if(suck!=-1):
                suck=self.config[suck];
                q.put((suck.hu,suck,'D'));

            up=self.rt(state);
            if(up!=-1):
                up=self.config[up];
                q.put((up.hu,up,'R'));

            up=self.lft(state);
            if(up!=-1):
                up=self.config[up];
                q.put((up.hu,up,'L'));

    def HillClimbing(self):
        q = Q.PriorityQueue()
        print "HillClimbing";
        q.put((self.src.hu,self.src,'N'));
        while not q.empty():
            ele1=q.get();
            #print ele1;
            state=ele1[1];
            q2=Q.PriorityQueue();
            print state.printstate(), ele1[2];
            if(state.hu==0):
                break;
            suck=self.suck(state);
            if(suck!=-1):
                suck=self.config[suck];
                q2.put((suck.hu,suck,'S'));

            up=self.upper(state);
            if(up!=-1):
                up=self.config[up];
                q2.put((up.hu,up,'U'));
            suck=self.down(state);
            if(suck!=-1):
                suck=self.config[suck];
                q2.put((suck.hu,suck,'D'));

            up=self.rt(state);
            if(up!=-1):
                up=self.config[up];
                q2.put((up.hu,up,'R'));


lines=filein.readlines();
pos=int(lines[0][0]);
rm1=int(lines[1][0]);
rm2=int(lines[1][2]);
rm3=int(lines[1][4]);
rm4=int(lines[1][6]);
algo=lines[2][:3];
output="";
source = state(pos,rm1,rm2,rm3,rm4);
g = Graph(source);
#g.printGraph();
g.bfs();
        
