package designpattern.decorator;

public abstract class BeverageDecorator implements Beverage {
  
  public Beverage beverage;
  public int qty;
  public String getBeverageName() {
    return beverage.getBeverageName();
  }

  public Integer getBeveragePrice() {
    return beverage.getBeveragePrice();
  }

}
