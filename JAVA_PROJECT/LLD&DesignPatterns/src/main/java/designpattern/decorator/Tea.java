package designpattern.decorator;

public class Tea implements Beverage{

  public String getBeverageName() {
    return "Tea";
  }

  public Integer getBeveragePrice() {
    return 20;
  }

}
