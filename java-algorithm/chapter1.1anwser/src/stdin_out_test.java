import java.util.Scanner;


public class stdin_out_test {

	public stdin_out_test() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		while(true){
			int num = in.nextInt();
			if(num == 0){
				System.out.println("this is 0, break");
				break;
			}else{
				System.out.println(num);
			}
		}
		in.close();
	}

}
