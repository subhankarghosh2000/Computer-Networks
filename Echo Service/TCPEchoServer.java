//package jun15;
import java.net.*;
import java.io.*;
public class TCPEchoServer
{
	private static final int BUFSIZE=80;
	public static void main(String args[])throws IOException
	{
		if(args.length!=1)
			//If right no. of arguments are not provided
			throw new IllegalArgumentException("Parameter(s):<Port>");
			// notification to the user regarding arguments

		int servPort=Integer.parseInt(args[0]);
		//Store the argument

		ServerSocket servSock=new ServerSocket(servPort);
		//Create the server side socket

		int recvMsgSize;
		//Declare variables for storing the data to be received

		byte[] byteBuffer=new byte[BUFSIZE];

		for(;;)
		//Server should run endlessly
		{
			Socket clntSock=servSock.accept();
			//Create the child server
			InputStream in=clntSock.getInputStream();
			//the input stream
			OutputStream out=clntSock.getOutputStream();
			//and the output stream

			while((recvMsgSize=in.read(byteBuffer))!=-1)
				//Receive and read the msg from client
				out.write(byteBuffer,0,recvMsgSize);

			//Echo it back to client
			clntSock.close();

		//Terminate the child server when echoing is complete
		}
	}
}