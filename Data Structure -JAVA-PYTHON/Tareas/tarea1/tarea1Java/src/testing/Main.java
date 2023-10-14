package testing;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	
    String calculo;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println( "\t \t Bienvenido a la calculadora binaria");
        System.out.println("\t Recuerda escribir tu calculo en binario separado por espacios!");
        System.out.println("\t \t  \t Ejemplo: 1010 + 0101");
        Scanner scan = new Scanner(System.in);
        String calculo = scan.nextLine();

  
        System.out.println( calcular(calculo));
 
    }

    public static String[] cortarCadenaPorEspacios(String cadena) {
        return cadena.split("\\ ");
    }

    
    public static int binarioADecimal(String cadena){
        
        String binario = cadena;
        int n = 1;
        int decimal = 0;

     
        for (int i = binario.length() - 1; i >= 0; i--) {
            
            if (binario.charAt(i) == '1')
                decimal += n;
            n = n * 2;
        }
 
        return decimal;
    }

    public static boolean esNumero(String cadena) {
        
        try {
            Integer.parseInt(cadena);
            return true;
        } catch (NumberFormatException nfe) {
            return false;
        }
    }


    public static float calcular(String calculos) {

      
        String[] subCadena = cortarCadenaPorEspacios(calculos);
        List<String> operadores = new ArrayList<>();
        List<Integer> operandos = new ArrayList<>();
 

        int cant = subCadena.length;
        
        for(int i = 0; i < cant; i++){
            
            
          if(esNumero(subCadena[i])){

            operandos.add( binarioADecimal(subCadena[i]));
          
           }else{
            
            operadores.add(subCadena[i]);
      
            
            }
      
        } 

  
        int j = 0;
        int res=operandos.get(0);;
        for(int i= 1; i<operandos.size(); i++){


                switch(operadores.get(j)){  
  
                case "+": 
                    res+=operandos.get(i);               
                        break;
                case "-":
                    res-=operandos.get(i);
                    break;  

                case "*":  
                   res *= operandos.get(i) ;
                    break;  
                case "/": 
                   res = (res /operandos.get(i)) ;
                    break; 
 
                default:System.out.println("Entrada no valida");  
    }                          j++;
    

    }
   return res;
}
	
	
	

}
