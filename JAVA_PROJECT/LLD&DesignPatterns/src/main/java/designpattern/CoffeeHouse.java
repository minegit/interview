package designpattern;

import designpattern.decorator.Beverage;
import designpattern.decorator.Milk;
import designpattern.decorator.Sugar;
import designpattern.decorator.Tea;

public class CoffeeHouse {
  public static void main(String[] args) {
    Beverage tea = new Tea();
    System.out.println("NAME :" + tea.getBeverageName()+" PRICE: "+tea.getBeveragePrice().toString());
    Beverage addMilk = new Milk(tea, 4);
    System.out.println("NAME :" + addMilk.getBeverageName()+" PRICE: "+addMilk.getBeveragePrice().toString());
    Beverage addSugar = new Sugar(addMilk, 3);
    System.out.println("NAME :" + addSugar.getBeverageName()+" PRICE: "+addSugar.getBeveragePrice().toString());
    
    
  }
}
