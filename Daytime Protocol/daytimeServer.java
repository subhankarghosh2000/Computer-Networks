import java.net.*;
import java.io.*;
import java.util.*;

public class daytimeServer
{
	public static final int daytimePort=1813;
	public static void main(String args[])
	{
		ServerSocket theServer;
		Socket theConnection;
		PrintStream P;
		try
		{
			theServer = new ServerSocket(daytimePort);
			theConnection = theServer.accept();
			try
			{
				while(true)
				{
					P = new PrintStream(theConnection.getOutputStream());
					P.println(new Date());
					theConnection.close();
				}
			}

			catch(IOException e)
			{
				theServer.close();
				System.err.println(e);
			}
		}
		catch(IOException e)
		{
			System.err.println(e);
		}
	}
}