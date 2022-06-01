package lld.nPlayerCardGame;

import lld.nPlayerCardGame.Constants.Suits;

public class Card implements Comparable<Card> {
  public Suits suit;
  public int faceValue;

  public Card(Suits suit, int faceValue) {
    super();
    this.suit = suit;
    this.faceValue = faceValue;
  }

  @Override
  public int compareTo(Card o) {
    if (this.faceValue == o.faceValue)
      return 0;
    if (this.faceValue > o.faceValue) {
      return -1;
    } else {
      return 1;
    }
  }

  @Override
  public String toString() {
    return "Card [suit=" + suit + ", faceValue=" + faceValue + "]";
  }

  
}

