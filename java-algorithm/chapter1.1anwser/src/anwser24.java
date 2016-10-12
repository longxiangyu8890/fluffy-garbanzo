
public class anwser24 {

	public anwser24() {
		// TODO Auto-generated constructor stub
	}
	
	/*定理：gcd(a, b) = g(b, a%b) 不妨设a > b,直到 a%b为0，运算停止
	 * 不用担心p < q,例如 5,10,经过 5 % 10 = 5，这样又变成 10,5
	 * */
	public static int gcd(int p, int q){
		System.out.print("gcd recursion p: ");
		System.out.print(p);
		System.out.print("  q:");
		System.out.println(q);
		if (q == 0){
			System.out.println("gcd result:");
			return p;
		}	
		int r = p % q;
		return gcd(q, r);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("input p and q, to get gcd");
		int p = StdIn.readInt();
		int q = StdIn.readInt();

		System.out.println(gcd(p, q));
	}

}
