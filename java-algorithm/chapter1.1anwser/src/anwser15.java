
public class anwser15 {

	public anwser15() {
		// TODO Auto-generated constructor stub
	}

	public static int[] fun_for_anwser15(int[] arr, int M){
		int[] record = new int[M];
		
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < arr.length; j++) {
				if(i == arr[j]){
					record[i]++;
				}			
			}
		}
		
		return record;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = new int[]{1, 4, 6, 7, 8, 2, 6, 9, 4, 6, 5, 10, 40, 39 };
		int M = 20;
		int[] record = fun_for_anwser15(a, M);
		/*
		for (int i = 0; i < record.length; i++) {
			System.out.println(record[i]);
		}
		*/
		int val = 1;
		for (int i = 0; i < record.length; i++) {
			if(record[i] < 0 || record[i] > M-1){
				val = 0;
			}
		}
		
		int sum = 0;
		if(val == 1){
			for (int i = 0; i < record.length; i++) {
				sum += record[i];
			}
		}
		System.out.println(sum);
	}

}
