

public class anwser32 {	
	
	public anwser32() {
		// TODO Auto-generated constructor stub
	}
	/*将(l r)分成N段
	 * */
    public static double[] segmentation(int N,double l,double r,double[] a)
    {    	
    	if(N==0)    return	a;
    	double delta = (r-l)/N;
    	a[0]=l;// 是l，不是1
    	for(int i=1;i<a.length;i++)
    	{
    		a[i]=a[i-1]+delta;
    	}
    	return a;
    }    
    
    /*
     * 1.计算落入各区段的个数
     * 2.画直方图
     *     a.画直方图之前，要先设置xscale yscale
     * */
    public static void makehistogram(double[] a,double[] b,double l,double r)
    {
    	int[] c=new int[a.length-1];
    	for(int i=0;i<b.length;i++){
    		for(int j=0;j<a.length-1;j++)
    		{
    			if(b[i]>=a[j]&&b[i]<a[j+1])
    			{
    				c[j]++;
    				continue;
    			}
    		} 		
    	}

    	int N=c.length;
    	StdDraw.setXscale(0,(r-l)*1.2 );
		StdDraw.setYscale(0, b.length/N*1.5);
    	for(int i=0;i<N;i++)
    	{    		
    		double x = l+(r-l)/N*i;
    		double y = c[i]/2.0;
    		double rw = (r-l)/(2*N);
    		double rh = c[i]/2.0;
    		StdDraw.filledRectangle(x, y, rw, rh);
    		StdOut.print(c[i]+" ");
       	}   	
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
        int N=10;//段数
        double l=2;
        double r=20;
		double [] a=new double[N+1];//分N段，就有N+1个点
		double [] b=new double[N*N*N];//随机产生的数组，作为输入数字
		a=segmentation(N,l,r,a);
		for(int i=0;i<b.length;i++)
		{
			b[i]=StdRandom.uniform(l, r);
		}
		makehistogram(a,b,l,r);
		
		/*
		StdDraw.setXscale(-20, 20);
		StdDraw.setYscale(-20, 20);
		StdDraw.filledCircle(5, 5, 10);
		*/
	}
   }