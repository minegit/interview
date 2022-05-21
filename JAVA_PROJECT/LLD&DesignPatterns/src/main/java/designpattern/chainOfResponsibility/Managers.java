package designpattern.chainOfResponsibility;

public abstract class Managers {
  String name;
  int approvalLimit;
  protected Managers manager;

  public void setManager(Managers manager) {
    this.manager = manager;
  }

  public void approveSalary(int salary) {
    if (salary <= approvalLimit) {
      processSalary(salary);
    } else if (this.manager != null) {
      this.manager.approveSalary(salary);
    } else {
      System.out.println("Cannot make offer to Candidate");
    }
  }

  protected abstract void processSalary(int salary);
}
