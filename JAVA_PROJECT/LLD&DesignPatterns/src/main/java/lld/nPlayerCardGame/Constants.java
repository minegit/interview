package lld.nPlayerCardGame;

import java.util.Random;

public class Constants {
  public enum Suits {
    HEART, DIAMOND, SPADE, CLUB
  }

  public static Suits getRandomSuits() {
    Random random = new Random();
    Suits[] values = Suits.values();
    int size = values.length;
    return values[random.nextInt(size)];
  }
}
