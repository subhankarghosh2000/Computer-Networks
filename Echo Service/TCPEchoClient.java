//package jun15;
import java.net.*;
import java.io.*;
public class TCPEchoClient
{
	public static void main(String args[])throws IOException
	{
		if((args.length < 2)||(args.length > 3)){
			//if right no. of arguments are not provided
			System.out.println(args.length);
			throw new IllegalArgumentException("Parameter(s):<server><word>[<port>]"); // notification to the user regarding arguments
		}

		String server=args[0];		
		//Store the arguments

		byte[] byteBuffer=args[1].getBytes();
		//in different
		int servPort=(args.length==3)?Integer.parseInt(args[2]):7;

		//variables
		Socket socket=new Socket(server,servPort);
		//Create the client side socket
		
		System.out.println("Connected to server...sending echo string");
		
		InputStream in=socket.getInputStream();
		//Create the input stream

		OutputStream out=socket.getOutputStream();
		//and output stream

		out.write(byteBuffer);
		//Send the msg to server

		int totalBytesRcvd=0;

		//Declare variables for storing the data
		int bytesRcvd;

		//to be received
		while(totalBytesRcvd < byteBuffer.length)
		//As long as receiving of data is not complete
		{
			if((bytesRcvd=in.read(byteBuffer,totalBytesRcvd,byteBuffer.length- totalBytesRcvd))==-1) //read the data received in a single iteration
				throw new SocketException("Connection closed prematurely");
				//if the connection does not close prematurely(while reading you specify what to read, wherefrom to read, and how much to read in a single iteration)
				totalBytesRcvd+=bytesRcvd;
		}
		System.out.println("Received :" + new String(byteBuffer));
		//finally you display what have you received
		socket.close();
		//close the connection from client side
	}
}