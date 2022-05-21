package designpattern.decorator;

public class Sugar extends BeverageDecorator {

  public Sugar(Beverage beve, int qty) {
    this.beverage = beve;
    this.qty = qty;
  }

  public Sugar(Beverage beve) {
    this.beverage = beve;
    this.qty = 1;
  }

  @Override
  public String getBeverageName() {
    return this.beverage.getBeverageName() + " WITH "+this.qty+" SUGAR";
  }

  @Override
  public Integer getBeveragePrice() {
    return this.beverage.getBeveragePrice() + 3*this.qty;
  }
}
