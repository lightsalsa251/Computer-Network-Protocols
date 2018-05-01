
import java.io.*;
import java.net.*;
public class talkserver
{
public static void main(String args[])throws Exception
{
ServerSocket ecsvr=null;
String line1,line2;
DataInputStream dis=null;
PrintStream pts=null;
Socket clsckt=null;
BufferedReader in1=null;
ecsvr=new ServerSocket(9999);
System.out.println("TALK SERVER");
System.out.println("----------------------");
clsckt=ecsvr.accept();
dis=new DataInputStream(clsckt.getInputStream());
pts=new PrintStream(clsckt.getOutputStream());
System.out.println("Node successfully connected..");
while(true)
{
line1=dis.readLine();
System.out.println("Message Received");
System.out.println("The Message ="+line1);
in1=new BufferedReader(new InputStreamReader(System.in));
line2=in1.readLine();
if(line2.equals("end"))
{
break;
}
pts.println(line2);
pts.flush();
System.out.println("Message sent successfully");
}
dis.close();
pts.close();
}
}



