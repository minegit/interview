package designpattern;

import designpattern.singleton.MySingleton;

public class CheckSingleton {
  public static void main(String[] args) {

    MySingleton mys = MySingleton.getInstance();

    MySingleton mys1 = MySingleton.getInstance();
    System.out.println(mys);
    System.out.println(mys1);
  }
}
