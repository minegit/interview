package designpattern.decorator;

public class Expresso implements Beverage {

  public String getBeverageName() {
    return "Expresso";
  }

  public Integer getBeveragePrice() {
    return 10;
  }

}
