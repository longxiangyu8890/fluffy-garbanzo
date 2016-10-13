
public class anwer28 {

	public anwer28() {
		// TODO Auto-generated constructor stub
	}

	public static int[] remove_repeat(int[] a){
		int repeat_cnt = 0;
		int[] b = new int[a.length];
		b[0] = a[0];
		int j = 1;
		for (int i = 0; i < a.length -1; i++) {
			if(a[i+1] == a[i]){
				repeat_cnt++;
			}else{
				b[i+1-repeat_cnt] = a[i+1];
				b[j++] = a[i+1];
			}
		}
		int[] c = new int[a.length - repeat_cnt];
		for (int i = 0; i < c.length; i++) {
			c[i] = b[i];
		}
		return c;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8};
		int[] clear = remove_repeat(a);
		for (int i = 0; i < clear.length; i++) {
			System.out.print(clear[i]);
			System.out.print(" ");
		}
		System.out.println(" ");
		
	}

}
