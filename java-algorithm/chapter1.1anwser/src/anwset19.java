
public class anwset19 {

	public anwset19() {
		// TODO Auto-generated constructor stub
	}
	/*运算量指数级增长*/
	public static long F_recursion(int N){
		if(N == 0) return 0;
		if(N == 1) return 1;
		return F_recursion(N-1) + F_recursion(N-2);
	}
	
	public static long F_no_recursion(int N){
		long[] arr = new long[N+1];
		arr[0] = 0;
		arr[1] = 1;
		if(N == 0 || N == 1)
			return arr[N];
		
		// 从arr[2]开始计算，一直计算到arr[N]
		for (int i = 2; i <= N; i++) {
			arr[i] = arr[i-1] + arr[i-2];
		}
		return arr[N];
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int N = 80;
		
		long starttime1 = System.currentTimeMillis();
		System.out.println(F_no_recursion(N));// 非递归方式，极快
		long endtime1 = System.currentTimeMillis();
		System.out.println(endtime1-starttime1);
		
		long starttime = System.currentTimeMillis();
		System.out.println(F_recursion(N));// 递归方式
		long endtime = System.currentTimeMillis();
		System.out.println(endtime-starttime);
		

		
		/*
		for (int i = 0; i < 100; i++) {
			System.out.println(F(i));
		}
		*/
	}

}
