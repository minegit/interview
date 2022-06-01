package lld.nPlayerCardGame;

import java.util.ArrayList;
import java.util.List;

public class Player {
  int id;
  int score;
  List<Card> cards;

  public Player(int id) {
    super();
    this.id = id;
    this.score = 0;
    this.cards = new ArrayList<Card>();
  }

  public List<Card> getCards() {
    return cards;
  }

  public void setCards(List<Card> cards) {
    this.cards = cards;
  }

  public int getId() {
    return id;
  }

  public void setId(int id) {
    this.id = id;
  }

  public int getScore() {
    return score;
  }

  public void setScore(int score) {
    this.score = score;
  }
  
  public void incrementScore(int n) {
    this.score+=n;
  }

  @Override
  public String toString() {
    return "Player [id=" + id + ", score=" + score + ", cards=" + cards + "]";
  }
  
  
}
