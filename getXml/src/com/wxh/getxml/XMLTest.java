package com.wxh.getxml;
/*
 * author:wxh1949.cn
 * date:2016-04-02
 * QQ:836405440
 * 欢迎大家互相交流学习
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
	//以数据流的方式获取到xml内容
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
	//将数据流转换成字符串，便于按照自己的需要处理
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
			InputStream is=downloadXML("http://php.weather.sina.com.cn/xml.php?city=三亚&password=DJOYnieT8234jlsK&day=0");
			outfile=convertStreamToString(is);
		    String[] cc=outfile.split("/n");
		    //showweather.setText(outfile+"城市："+cc[4]+"天气："+cc[5]+"天气："+cc[6]+"最高温度："+cc[13]);
		    System.out.println(outfile);
		  }

}
