
public class rolltheDice {

	public rolltheDice() {
		// TODO Auto-generated constructor stub
	}
    public static double[] simulation(double[] a,int N,int SIDES)
    {
    	for(int i=0;i<N;i++)
    	{
    		int n=1+StdRandom.uniform(SIDES);
    		int m=1+StdRandom.uniform(SIDES);
    		a[n+m]=a[n+m]+1.0;
    	}
    	for (int k = 2; k <= 2*SIDES; k++)
		{
		a[k]= a[k]/N;
		}
    	return a;
    }
    public static void match(double[] dist,double[] dist2,int SIDES,int N)
    {
    	boolean Ismatch=true;
		for(int n=N;Ismatch;n=n+n/10)
		{
		   dist2 =simulation(dist2,n,SIDES);
		   int cnt=0;
		   for (int k = 2; k <= 2*SIDES; k++)
		   {			  		   
				if(Math.abs(dist[k]-dist2[k])>0.0001)
		         { Ismatch=true;  continue;}
		        else {
			             cnt++;
		             }
		        if(cnt==11)
		         {
			         Ismatch=false;
		         }
		   }
		   StdOut.println("n="+n +"  cnt="+cnt);
		   Print(dist2,SIDES);           
		}		
    }
    public static void Print(double [] a,int SIDES)
    {
    	for (int k = 2; k <= 2*SIDES; k++)
		{		
		StdOut.print("k="+k+" "+a[k]+" ");
		if((k-1)%6==0)
			StdOut.println(" ");
		}
		StdOut.println(" ");
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int SIDES = 6;
		int N=1000000;
		double[] dist = new double[2*SIDES+1];
		double[] dist2 = new double[2*SIDES+1];
		//准确概率分布
		for (int i = 1; i <= SIDES; i++)
		for (int j = 1; j <= SIDES; j++)
		dist[i+j] += 1.0;		
		for (int k = 2; k <= 2*SIDES; k++)
		{	dist[k]/=36;	
		}
		StdOut.println("dist:");
		Print(dist,SIDES);
		match(dist,dist2,SIDES,N);
	}
}