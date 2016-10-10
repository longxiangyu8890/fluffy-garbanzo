
public class anwser13 {

	public anwser13() {
		// TODO Auto-generated constructor stub
	}

	public static void testChangeRealAgr(int a[])
	{
		int[] dst = new int[a.length];
		copyArray(a, dst);
		
		a[0] = 2;
		/*
		for (int i = 0; i < a.length; i++) {
			System.out.println(a[i]);
		}
		*/
		
		if(a[0] != dst[0]){
			System.out.println("java can change real agr");
		}else{
			System.out.println("can not change real agr");
		}
	}
	
	public static void copyArray(int src[], int dst[])
	{
		for (int i = 0; i < dst.length; i++) {
			dst[i] = src[i];
		}
	}
	
	public static int[][] generateMatrix(int line_num, int colunm_num){
		int[][] a = new int[line_num][colunm_num];
		for (int i = 0; i < line_num; i++) {
			for (int j = 0; j < colunm_num; j++) {
				a[i][j] = i+1;
				System.out.print(a[i][j]);
				System.out.print(" ");
			}
			System.out.println("");
		}
		return a;
	}

	public static int[][] convertMatrix(int[][] matrix){
		int[][] newMatrix = new int[matrix[0].length][matrix.length];
		
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[0].length; j++) {
				newMatrix[j][i] = matrix[i][j];
			}
		}
		return newMatrix;
	}
/*	
	public static void convertMatrixOld(int[][] matrix){	
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[0].length; j++) {
				matrix[j][i] = matrix[i][j];
			}
		}

	}
*/
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int line_num = 3;
		int column_num = 4;
		int[][] matrix = generateMatrix(line_num, column_num);
		
		int[][] newMatrix; //= new int[column_num][line_num];
		newMatrix = convertMatrix(matrix);
		for (int i = 0; i < newMatrix.length; i++) {
			for (int j = 0; j < newMatrix[0].length; j++) {
				System.out.print(newMatrix[i][j]);
				System.out.print(" ");
			}
			System.out.println("");
		}


		//System.out.println(matrix.length);// 二维数组的行数
		//System.out.println(matrix[0].length);// 二维数组的列数
	}

}
