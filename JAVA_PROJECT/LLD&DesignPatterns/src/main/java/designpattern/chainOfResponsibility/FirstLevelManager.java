package designpattern.chainOfResponsibility;

public class FirstLevelManager extends Managers {
  public FirstLevelManager(int approvalLimit, String name) {
    this.name = name;
    this.approvalLimit = approvalLimit;
  }
  
  @Override
  protected void processSalary(int salary) {
    System.out.println("Salary: "+salary +" Processed by : "+ this.getClass().getSimpleName());
  }

}
