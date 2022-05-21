package designpattern.chainOfResponsibility;

public class ThirdLevelManager extends Managers {
  public ThirdLevelManager(int approvalLimit, String name) {
    this.name = name;
    this.approvalLimit = approvalLimit;
  }
  
  @Override
  protected void processSalary(int salary) {
    System.out.println("Salary: "+salary +" Processed by : "+ this.name);
  }

}
