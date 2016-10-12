import java.util.Arrays;
import java.util.Scanner;


public class anwser22 {

	public anwser22() {
		// TODO Auto-generated constructor stub
	}
	
	
	/*
	 * 非递归实现二分查找
	 * 在a数组中找到key所在的index*/
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
		return -1;// 没找到
	}
	
	/*
	 * 递归实现二分查找
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
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] whitelist = In.readInts(args[0]);
		while(!StdIn.isEmpty()){
			int key = StdIn.readInt();
			if(rank_recursion(whitelist, 0, whitelist.length-1, key) < 0){
				System.out.print("not found ");
				System.out.print(key);
				System.out.println("");	
			}

		}
		
		/*
		int[] a = {3,2,5,6,7,8,1,5,9,0,3,6,6};
		Arrays.sort(a);
		Scanner in = new Scanner(System.in);//读取标准输入
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

	}

}
