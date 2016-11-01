
public class anwser36 {

	public anwser36() {
		// TODO Auto-generated constructor stub
	}

	public static void shuffle(int[] a){
		int N = a.length;
		
		/*a[i] 与 a[r] 交换，r位于[i,N-1]*/
		for (int i = 0; i < N; i++) {
			int r = i + StdRandom.uniform(N-i);
			int tmp = a[i];
			a[i] = a[r];
			a[r] = tmp;
		}
		
		System.out.println("after:");
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]+"  ");
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = new int[100];
		System.out.println("before:");
		for (int i = 0; i < a.length; i++) {
			a[i] = StdRandom.uniform(1000);
			System.out.print( a[i] + "  ");
		}
		System.out.println(" ");
		
		shuffle(a);

	}

}
