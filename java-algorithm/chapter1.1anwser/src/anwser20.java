
public class anwser20 {

	public anwser20() {
		// TODO Auto-generated constructor stub
	}
	
	/*ln(n!) µ›πÈ µœ÷*/
	public static double fun(int n){
		if(n == 1)
			return 0.0;
		return Math.log(n) + fun(n-1);
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(fun(3));
	}

}
