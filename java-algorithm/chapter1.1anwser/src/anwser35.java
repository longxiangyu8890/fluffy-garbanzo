import java.util.ArrayList;


public class anwser35 {

	public anwser35() {
		// TODO Auto-generated constructor stub
	}
	/*
	 * 模拟骰子过程
	 * para:N 试验次数
	 * */
	public static double[] simulation(int N) {
		int NUM = 6;
		double[] record = new double[2*NUM +1];// record[12]，这就要13个数
		
		for (int i = 0; i < N; i++) {
			int result1 = StdRandom.uniform(0, 6) + 1;//[1, 7) 整数下就是 1 2 3 4 5 6 内随机产生
			int result2 = StdRandom.uniform(0, 6) + 1;
			int sum = result1 + result2;
			//System.out.println(sum);
			record[sum] += 1.0;// 当出现这个点，就+1
		}
		
		for (int i = 0; i < record.length; i++) {
			System.out.println("record[" + i + "]: " + record[i]);
			record[i] = record[i]/N;
			System.out.println(i + "出现的频率" + record[i]);
		}
		
		return record;
	}

	public static double[] get_problity() {
		int SIDES = 6;
		double[] dist = new double[2*SIDES+1];// arr[12]--13
		//出现i+j 场景的次数
		for (int i = 1; i <= SIDES; i++){
			for (int j = 1; j <= SIDES; j++)
				dist[i+j] += 1.0;	
		}
		// 占总场景的比例
		for (int k = 2; k <= 2*SIDES; k++)
			dist[k] /= 36.0;
		for (int i = 2; i < dist.length; i++) {
			System.out.println(i + " 出现的概率" + dist[i]);
		}
		
		return dist;
	}
	
	public static boolean match(double[] a, double[] b){		
		if(a.length != b.length){
			System.out.println("not same");
			return false;
		}
	
		double[] distance = new double[b.length];
		/*
		for (int i = 0; i < b.length; i++) {
			distance[i] = a[i] - b[i];
			System.out.println(i + "差距:" + distance[i]);
		}
		*/
		for (int i = 0; i < b.length; i++) {
			if(Math.abs(a[i] - b[i]) >= 0.001){
				return false;
			}
		}
		return true;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double[] problicty = get_problity();
		
		for(int num = 10;num < 10000000; num = num+num/10){
			double[] practice = simulation(num);
			
			if(match(problicty, practice)){
				System.out.println(num + "次，才能匹配");
				break;
			}
			
			System.out.println("go");
		}



		
	}

}
