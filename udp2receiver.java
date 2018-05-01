import java.io.*;
import java.net.*;
import java.lang.*;
class udp2receiver
{
public static void main(String a[])throws IOException
{
DatagramSocket ds=new DatagramSocket(1234);
byte b[]=new byte[255];
while(true)
{
DatagramPacket dp=new DatagramPacket(b,b.length);
ds.receive(dp);
String msg=new String(dp.getData());
System.out.println("Msg Received:"+msg);


//InetAddress add=InetAddress.getByName("10.51.1.121");
InetAddress add=InetAddress.getLocalHost();

int port=dp.getPort();
System.out.println("Enter a line of text to send:");

BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
String msg1=br.readLine();
byte b1[]=msg1.getBytes();

DatagramPacket dp1=new DatagramPacket(b1,b1.length,add,port);
ds.send(dp1);
if(msg1.equals("exit"))
System.exit(0);
}
}
}