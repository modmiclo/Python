def division_euclidienne(a,b):

	pgcd=b
	if a==0 or b==0:
		print("pas possible")	
		return

	if a>b:
		q=a//b
		r=a%b
		if r==0:
			pgcd=b
		else:
			a=b
			b=r
	print(q,r)
	return(q,r)
	
#division_euclidienne(21,5)

def degre(P):
	if len(P)<1:
		print(0)
		return 0
	else :
		print(len(P)-1)
		return len(P)-1
#degre([4,0,5,8,4])
	
def somme(P,Q) :
        x = []
        if degre(P)>degre(Q) :
                for i in range(len(Q)) :
                        x.append(P[i]+Q[i])
                for i in range(len(Q), len(P)):
                        x.append(P[i])
        else :
                for i in range(len(P)) :
                        x.append(P[i]+Q[i])
                for i in range(len(P), len(Q)):
                        x.append(Q[i])
        return x

#print(somme([4, 0, 5, 3], [3, 5, 4, 2,1]))

def produit(P,Q):
	R=[]
	for i in range(len(P)):
		for j in range(len(Q)):
			R.append(P[i]*Q[j])
		
	print(R) 
	return R

produit([2,1], [1,0,3])


