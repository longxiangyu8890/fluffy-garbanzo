

public class anwser16 {

	public anwser16() {
		// TODO Auto-generated constructor stub
	}

	public static String exR1(int n){
		if(n <= 0)
			return "";
		return exR1(n-3) + n + exR1(n-2) + n;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = exR1(6);
		System.out.println(str);//"311361142246"
	}

}
