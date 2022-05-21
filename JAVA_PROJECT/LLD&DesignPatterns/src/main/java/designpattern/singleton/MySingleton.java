package designpattern.singleton;

import java.io.Serializable;

public class MySingleton implements Serializable, Cloneable {
  private volatile static MySingleton mySingletonObj;
  private volatile  String name;

  public String getName() {
    return name;
  }

  private MySingleton() {
    if (mySingletonObj != null) {
      throw new IllegalStateException("Object already created..");
    }
  }

  public static MySingleton getInstance() {
    if (mySingletonObj == null) {
      synchronized (MySingleton.class) {
        if (mySingletonObj == null) {
          mySingletonObj = new MySingleton();
          mySingletonObj.name = "SOME NAME";
        }
      }
    }
    return mySingletonObj;
  }

  protected Object clone() throws CloneNotSupportedException {
    throw new CloneNotSupportedException();
  }

  protected Object readResolve() {
    return mySingletonObj;
  }
}
