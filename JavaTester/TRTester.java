//import java.io.*;
//import java.util.*;
//
//public class TRTester{
//
//    public void main(String[] args) {
//        String intro = "Hello my jame is nohn";
//        int num = 56;
//        int inter = intro.read();
//        System.out.println(inter);
//        System.out.println((char) inter);
//    }
//}
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args)
    {

        try {

            String str = "GeeksForGeeks";

            // Create a Reader instance
            Reader reader
                    = new StringReader(str);

            // Get the character
            // to be read from the stream
            int ch;

            // Read the first 5 characters
            // to this reader using read() method
            // This will put the str in the stream
            // till it is read by the reader
            for (int i = 0; i < 5; i++) {
                ch = reader.read();
                System.out.println("\nInteger value "
                        + "of character read: "
                        + ch);
                System.out.println("Actual "
                        + "character read: "
                        + (char)ch);
            }

            reader.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}