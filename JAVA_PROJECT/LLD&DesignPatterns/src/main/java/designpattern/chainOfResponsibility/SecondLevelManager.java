package designpattern.chainOfResponsibility;

public class SecondLevelManager extends Managers {
  public SecondLevelManager(int approvalLimit, String name) {
    this.name = name;
    this.approvalLimit = approvalLimit;
  }
  
  @Override
  protected void processSalary(int salary) {
    System.out.println("Salary: "+salary +" Processed by : "+ this.getClass().getSimpleName());
  }

}
