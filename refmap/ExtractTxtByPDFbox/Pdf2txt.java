import java.io.IOException;
import java.io.File;

public class Pdf2txt {
 
    public static void main(String[] args) throws IOException {
 
       PDFManager pdfManager = new PDFManager();
       if (args.length > 0){
           File f = new File(args[0]);
           if(f.exists() && !f.isDirectory()) {
               pdfManager.setFilePath(args[0]);
               System.out.println(pdfManager.ToText());
           } else
               System.out.println("NOT a valid file");
       } else
           System.out.println("Give me a PDF file");

    }
}
