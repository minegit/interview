package designpattern.decorator;

public class Milk extends BeverageDecorator {


  public Milk(Beverage beve, int qty) {
    this.beverage = beve;
    this.qty = qty;
  }
  public Milk(Beverage beve) {
    this.beverage = beve;
    this.qty = 1;
  }

  @Override
  public String getBeverageName() {
    return this.beverage.getBeverageName() + " WITH "+this.qty+" MILK";
  }

  @Override
  public Integer getBeveragePrice() {
    return this.beverage.getBeveragePrice() + 5* this.qty;
  }
}
