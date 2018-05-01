import java.net.*;     
import java.util.Date;
public class udp
{
  public static void main(String args[]) throws Exception   
  {
    DatagramSocket dsock = new DatagramSocket();     
    //InetAddress address = InetAddress.getLocalHost( ); 
    InetAddress ip = InetAddress.getByName("192.168.43.50");    
    System.out.println("Server is ready");
	
    while(true)                          
    {    
     Thread.sleep(1000);                                           
     Date currentDate = new Date( );
     String s1 = currentDate.toString( );
     byte arr[] = s1.getBytes( );
     DatagramPacket dpack = new DatagramPacket(arr, arr.length, ip, 2000);
     dsock.send(dpack);                                             
    }
  }
}