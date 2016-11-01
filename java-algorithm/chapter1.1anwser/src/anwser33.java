
public class anwser33 {

	public anwser33() {
		// TODO Auto-generated constructor stub
	}

	public static double dot(double[] a, double[] b){
		double dot_result = 0;
		if(a.length != b.length){
			System.out.println("dot, length is not same");
			return dot_result;
		}
		for (int i = 0; i < a.length; i++) {
			dot_result += a[i] * b[i];
		}
		return dot_result;
	}
	
	public static double[][] mult(double[][] a, double[][] b){
		double[][] result = new double[a.length][b[0].length];
		if(a[0].length != b.length){
			System.out.println("矩阵a的列数与矩阵b的行数不等，无法相乘");
			return result;
		}
		
		for (int i = 0; i < result.length; i++) {
			for (int j = 0; j < result[i].length; j++) {
				result[i][j] = dot(a[i], b[j]);
			}
		}
		return result;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double[] a = {1, 2, 3, 4, 5};
		double[] a1 = {1, 2, 3, 4, 5, 6};
		double[] b = {2, 3, 4, 5, 6}; 
		/*test dot*/
		double result = 0;
		result = dot(a1, b);
		System.out.println("dot result: " + result);

		result = dot(a, b);
		System.out.println("dot result: " + result);
		
		/*test mult*/
		double[][] matrix_a = {
				{1.0, 2.0, 3.0},
				{2.0, 3.0, 4.0},
				{3.0, 4.0, 5.0}
		};
		double[][] matrix_b = {
				{1.0, 2.0, 3.0},
				{2.0, 3.0, 4.0},
				{3.0, 4.0, 5.0}
		};
		double[][] c = mult(matrix_a, matrix_b);
		Mult_print(c);
		
		/*test transporse*/
		double[][] matrix_c = {
				{8.0, 2.0, 3.0},
				{9.0, 3.0, 4.0},
				{3.0, 5.0, 5.0}
		};
		double[][] result_transpose = transpose(matrix_c);
		Mult_print(result_transpose);
		
		/*test 矩阵和向量之积*/
		double[] e = {30.0, 5.0, 2.0};
		double[] re = mult(matrix_c, e);
		arr_print(re);
	}

	private static void Mult_print(double[][] c) {
		// TODO Auto-generated method stub
		for (int i = 0; i < c.length; i++) {
			for (int j = 0; j < c[0].length; j++) {
				System.out.print(c[i][j] + "  ");
			}
			System.out.println(" ");
		}
	}
	
	private static void arr_print(double[] a) {
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i] + "  ");
		}
	}
	
	static double[][] transpose(double[][] a){
		int M = a.length;
		int N = a[0].length;
		double[][] result = new double[N][M];
		
		//行转成列
		for (int j = 0; j < M; j++) {
			for (int i = 0; i < N; i++) {
				result[i][j] = a[j][i];
			}
		}
		
		return result;
		
	}
	
	/*矩阵和向量之积*/
	static double[] mult(double[][] a, double[] x){
		double[] result = new double[a.length]; 
		if(a[0].length != x.length){
			System.out.println("矩阵的列数应当与向量的行数相同，此处不同");
			return result;
		}
		
		for (int i = 0; i < result.length; i++) {
			result[i] = dot(a[i], x);
		}
		
		return result;
	}
}
