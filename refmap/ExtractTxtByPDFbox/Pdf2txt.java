import java.io.IOException;

public class Pdf2txt {
 
    public static void main(String[] args) throws IOException {
 
       PDFManager pdfManager = new PDFManager();
       pdfManager.setFilePath("/tmp/test.pdf");
       System.out.println(pdfManager.ToText());       
    
    }    
}
