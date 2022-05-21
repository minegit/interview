package designpattern.chainOfResponsibility;

public class ChainOfManager {
  public Managers buildChain() {
    Managers m1 = new FirstLevelManager(100, "first");
    Managers m2 = new SecondLevelManager(200, "first");
    Managers m3 = new ThirdLevelManager(300, "first");
    m1.setManager(m2);
    m2.setManager(m3);
    return m1;
  }
}
