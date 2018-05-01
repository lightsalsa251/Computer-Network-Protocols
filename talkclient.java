import java.io.*;
import java.net.*;
public class talkclient
{
public static void main(String args[])
{
PrintWriter out=null;
String line1;
BufferedReader networkln=null;
try
{
Socket theSocket=new Socket("LocalHost",9999);
networkln=new BufferedReader(new InputStreamReader(theSocket.getInputStream()));
BufferedReader userln=new BufferedReader(new InputStreamReader(System.in));
out=new PrintWriter(theSocket.getOutputStream());
System.out.println("TALK CLIENT");
System.out.println("--------------------");
while(true)
{
System.out.println("send message to server: ");
String theLine=userln.readLine();
if(theLine.equals("end"))
break;
out.println(theLine);
out.flush();
System.out.println("message sent successfully");
System.out.println(" ");
System.out.println("message received from talkserver: "+networkln.readLine());
}  }
catch(IOException e)
{
System.err.println(e);
}   try
{
if(networkln!=null)
networkln.close();
if(out!=null)
out.close();
}	catch(Exception e)
{
System.err.println(e);
}  }  }
