import java.io.File;

public class Renomear{

  public static void main (String[] args){
    //File[] arquivos = (new File("imagens_redimensionadas_normalizadas/Orelha_elefante")).listFiles();
    File[] arquivos = (new File("dataset/Orelha_elefante")).listFiles();
    renomearArquivosOrdenados(arquivos);
  }
  private static void renomearArquivosOrdenados(File[] arquivos) {
    for (int index = 0; index < arquivos.length; index++){
      File novoArquivo = arquivos[index];
      novoArquivo.renameTo(new File("dataset/Orelha_elefante/"+(index+1)+"_orelha_de_elefante.jpg"));
    }
  }
}