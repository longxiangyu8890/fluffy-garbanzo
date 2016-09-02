package chapter1;

public class testgcd {
	public static int gcd(int p, int q){
		if (q == 0)
			return p;
		int r = p % q;
		return gcd(q, r);
	}
	public static boolean isprime(int N){
		if (N < 2)
			return false;
		for(int i = 2; i*i < N; i++){
			if(N % i == 0)
				return false;
		}
		return true;
	}
	
	public static double H(int N){
		double sum = 0.0;
		for(int i=1; i<=N; i++){
			sum += 1.0/i;// 留意1.0，如果是1/i就有问题了
		}
		return sum;
	}
	
	public static double abs(double x){
		if (x < 0)
			return -x;
		else
			return x;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
/*
 * test greatest common devider begin 
 * 
*/	
		System.out.println("hello test gcd");
		int great = gcd(10, 3);
		System.out.println(great);
/*
 * test greatest common devider end
 * 
*/

/*
 * test array begin
 * 
*/	
		int[] a = {8,32,6654,2432,74,8686,243,65437,84903};
		int[][]a1 = new int[3][3];
		int[][]b1 = new int[3][3];
		for(int i=0;i<3; i++){
			for(int j=0;j<3; j++){
				a1[i][j] = 2;
				b1[i][j] = 3;
			}
		}
 		/*get_max_inarray*/
		if( false ){
			int max = a[0];
			for(int i=1; i<a.length; i++){
				if(a[i] > max){
					max = a[i];
				}
			}
			System.out.println(max);
		}
		/*get_average*/
		if(false){
			int sum = 0;
			int len = a.length;
			for(int i=0; i < len; i++){
				sum += a[i];
			}
			int avr = sum / len;
			System.out.println(avr);
		}
		/*copy array*/
		if(false){
			int len = a.length;
			int[] b = new int[len];// 动态分配，不必考虑数组的大小要明确
			for(int i=0; i<len; i++){
				b[i] = a[i];
			}
			for(int i=0; i<len; i++){
				System.out.println(b[i]);
			}			
			
		}
		/*reverse array*/
		if(false){
			int len = a.length;
			for(int i=0; i<len/2; i++){
				int tmp = a[i];
				a[i] = a[len-1-i];
				a[len-1-i] = tmp;
			}
			for(int i=0; i<len; i++){
				System.out.println(a[i]);
			}			
			
		}
		/*matrix product 矩阵乘积*/
		if(false){
			int N = 3;
			int[][] c = new int[N][N];
			for(int i=0; i<N; i++){
				for(int j=0; j<N; j++){
					//计算c[i][j]的值
					for(int k=0; k<N; k++){
						c[i][j] += a1[i][k]*b1[k][j];
					}
					System.out.println(c[i][j]);
				}	
			}	
		}
/*
 * test array end
 * 
*/	
	
/*
 * 
 * 
*/	
		System.out.println( isprime(1) );
		
		System.out.println( H(9) );
		
		System.out.println( abs(-9.0/7) );
	
	}

}
