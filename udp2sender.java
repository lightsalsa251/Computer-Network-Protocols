import java.io.*;
import java.net.*;
class udp2sender
{
public static void main(String a[])throws Exception
{	
while(true)
{
DatagramSocket ds=new DatagramSocket();
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
System.out.println("enter the msg:");
String msg=br.readLine();
byte bl[]=msg.getBytes();
InetAddress add=InetAddress.getLocalHost();
DatagramPacket dp=new DatagramPacket(bl,bl.length,add,1234);
ds.send(dp);
if(msg.equals("exit"))
System.exit(0);
byte b[]=new byte[255];
DatagramPacket dp1=new DatagramPacket(bl,bl.length);
ds.receive(dp1);
String msg1=new String(dp1.getData());
System.out.println("received msg:" +msg1);
}
}
}









