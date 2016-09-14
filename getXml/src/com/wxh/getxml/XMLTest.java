package com.wxh.getxml;
/*
 * author:wxh1949.cn
 * date:2016-04-02
 * QQ:836405440
 * ��ӭ��һ��ཻ��ѧϰ
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class XMLTest {
	//���������ķ�ʽ��ȡ��xml����
	public static InputStream downloadXML(final String urlStr)
	  {
	    InputStream inStream = null;
	             URL url = null;
	          try {
	            url = new URL(urlStr);
	          } catch (MalformedURLException e) {
	            // TODO Auto-generated catch block
	            e.printStackTrace();
	          }  
	             HttpURLConnection conn = null;
	          try {
	            conn = (HttpURLConnection) url.openConnection();
	          } catch (IOException e) {
	            // TODO Auto-generated catch block
	            e.printStackTrace();
	          }  
	             conn.setConnectTimeout(5 * 1000);  
	            try {
	            conn.setRequestMethod("GET");
	            conn.connect();
	          } catch (Exception e) {
	            // TODO Auto-generated catch block
	          }  	 
	             try {
	               inStream= conn.getInputStream();
	          } catch (IOException e) {
	            // TODO Auto-generated catch block
	            e.printStackTrace();
	          }  
	  return inStream;  
	  }
	//��������ת�����ַ��������ڰ����Լ�����Ҫ����
	  public static String convertStreamToString(InputStream is) throws UnsupportedEncodingException {   
	       BufferedReader reader = new BufferedReader(new InputStreamReader(is,"utf-8"));   	 
	        StringBuilder sb = new StringBuilder();   
	        String line = null;   
	        try {   
	          while ((line = reader.readLine()) != null) {   
	            sb.append(line + "/n");   
	          }   
	        } catch (IOException e) {   
	          e.printStackTrace();   
	        } finally {   
	          try {   
	            is.close();   
	          } catch (IOException e) {   
	            e.printStackTrace();}   
	        }   
	        return sb.toString();   
	      }   
	  public static void main(String[] args) throws UnsupportedEncodingException {
		    String outfile="";
			InputStream is=downloadXML("http://php.weather.sina.com.cn/xml.php?city=����&password=DJOYnieT8234jlsK&day=0");
			outfile=convertStreamToString(is);
		    String[] cc=outfile.split("/n");
		    //showweather.setText(outfile+"���У�"+cc[4]+"������"+cc[5]+"������"+cc[6]+"����¶ȣ�"+cc[13]);
		    System.out.println(outfile);
		  }

}
