import java.util.Arrays;
import java.util.Scanner;


public class anwser22and29 {

	public anwser22and29() {
		// TODO Auto-generated constructor stub
	}
	
	
	/*
	 * 闈為�褰掑疄鐜颁簩鍒嗘煡鎵�
	 * 鍦╝鏁扮粍涓壘鍒発ey鎵�湪鐨刬ndex*/
	public static int rank_no_recur(int a[], int key){
		int low = 0;
		int high = a.length - 1;
		while(low <= high){
			int mid = low + (high - low)/2;
			if(key < a[mid]) 
				high = mid - 1;
			else if(key > a[mid]) 
				low = mid + 1;
			else 
				return mid;
		}
		return -1;// 娌℃壘鍒�
	}
	
	/*
	 * 閫掑綊瀹炵幇浜屽垎鏌ユ壘
	 * */
	public static int rank_recursion(int[] a, int low, int high, int key){
		if(low > high)
			return -1;
		else{
			int mid = low + (high - low)/2;
			if(key < a[mid]) 
				return rank_recursion(a, low, mid-1, key);
			else if(key > a[mid])
				return rank_recursion(a, mid+1, high, key);
			else 
				return mid;		
		}
	}
	
	/**/
	public static int get_Less_Num(int[] a, int key){
		int index = rank_no_recur(a, key);
		if(index == -1){
			System.out.println("not found key");
			return -1;
		}

		int num_less = 0;
		int i;
		for (i = index; i > 0; i--) {
			if(a[i] != a[i-1])
				break;
		}
		num_less = i;
		return num_less;
	}
	
	public static int get_Key_RepeatNum(int[] a, int key){
		int index = rank_no_recur(a, key);
		if(index == -1){
			System.out.println("not found key");
			return -1;
		}
			
		//int num_key_repeatnum = 0;
		int i;
		for (i = index; i > 0; i--) {
			if(a[i] != a[i-1])
				break;
		}
		//num_key_repeatnum = index - i;
		//return num_key_repeatnum;
		return index - i;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		int[] whitelist = In.readInts(args[0]);
		while(!StdIn.isEmpty()){
			int key = StdIn.readInt();
			if(rank_recursion(whitelist, 0, whitelist.length-1, key) < 0){
				System.out.print("not found ");
				System.out.print(key);
				System.out.println("");	
			}

		}
		*/
		
		/*
		int[] a = {3,2,5,6,7,8,1,5,9,0,3,6,6};
		Arrays.sort(a);
		Scanner in = new Scanner(System.in);//璇诲彇鏍囧噯杈撳叆
		while (true) {
			int key = in.nextInt();
			System.out.println(rank_no_recur(a, key));
			if(key == 999){
				System.out.println("exit");
				break;				
			}

		}
		in.close();
		*/

		/*test anwser 29*/
		int[] a = {1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8};
		int key = StdIn.readInt();
		System.out.print("less key 's num:");
		System.out.println(get_Less_Num(a, key));
		System.out.print("equal key 's num:");
		System.out.println(get_Key_RepeatNum(a, key));
		
		
		
	}

}
