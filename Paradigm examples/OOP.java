public class Car {

    private int doors;
    private int wheels;
    private String model;
    private String engine;
    private String colour; 
    
      public void setModel(String model){
        String validModel = model.toLowerCase();
        if (validModel.equals("roadster") || validModel.equals("model s")){
            this.model = model;
        } else {
            this.model = "Unknown";
        }
    }

    public String getModel(){
           return this.model;
    }
}

public class Main {

    public static void main(String[] args) {
           Car tesla = new Car(); //creates a new class object
           System.out.println("Model is " + tesla.getModel());
           tesla.setModel("Roadster");
           System.out.println("Model is " + tesla.getModel());
           tesla.setModel("Model S");
           System.out.println("Model is " + tesla.getModel());
    }
}