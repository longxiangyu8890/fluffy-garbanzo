
public class answer12 {

	public answer12() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = new int[10];
		for(int i=0; i < 10; i++)
		{
			a[i] = 9 -i;
		}
		for(int i=0; i < 10; i++)
		{
			a[i] = a[a[i]];
		}
		for(int i=0; i < 10; i++)
		{
			System.out.println(a[i]);
		}
	}

}
