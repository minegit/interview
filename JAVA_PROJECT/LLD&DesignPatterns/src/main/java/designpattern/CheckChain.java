package designpattern;

import designpattern.chainOfResponsibility.ChainOfManager;
import designpattern.chainOfResponsibility.Managers;

public class CheckChain {
  public static void main(String[] args) {
    ChainOfManager cm = new ChainOfManager();
    Managers m = cm.buildChain();
    m.approveSalary(101);
    m.approveSalary(201);
    m.approveSalary(1);
    m.approveSalary(401);
  }
}
