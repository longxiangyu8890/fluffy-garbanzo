
public class anwser24 {

	public anwser24() {
		// TODO Auto-generated constructor stub
	}
	
	/*����gcd(a, b) = g(b, a%b) ������a > b,ֱ�� a%bΪ0������ֹͣ
	 * ���õ���p < q,���� 5,10,���� 5 % 10 = 5�������ֱ�� 10,5
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
