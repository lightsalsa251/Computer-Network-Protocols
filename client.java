import java.net.*;
import java.io.*;                        // for IOException
 
public class client
{
  public static void main(String args[ ] ) throws SocketException, IOException
  {
    DatagramSocket dsock = new DatagramSocket(8000);            
    DatagramPacket dpack;
 
    while(true)   
    {
      byte arr1[] = new byte[100];
      dpack = new DatagramPacket(arr1, arr1.length);
      dsock.receive(dpack);                                                           
      byte arr2[] = dpack.getData();             
      String str = new String(arr2);    
      System.out.println(str);                      
    }   					
  }          
}
