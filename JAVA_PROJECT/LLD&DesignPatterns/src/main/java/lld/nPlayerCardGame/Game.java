package lld.nPlayerCardGame;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
/**
 * https://mortoray.com/2017/12/14/interview-question-a-two-player-card-game/
 * @author manishverma
 *
 */
public class Game {
  int numberOfPlayers;
  int numberOfCards;
  int playableCard;
  List<Player> players;
  List<Card> cards;
  Map<Integer, Integer> scoreCard = new HashMap<Integer, Integer>();

  public Game(int numberOfPlayers, int numberOfCards) {
    super();
    this.numberOfPlayers = numberOfPlayers;
    this.numberOfCards = numberOfCards;
    this.players = new ArrayList<Player>();
    this.cards = new ArrayList<Card>();

    Random random = new Random();
    for (int i = 0; i < this.numberOfPlayers; i++) {
      this.players.add(new Player(i));
    }
    int extraCard = this.numberOfCards % this.numberOfPlayers;
    this.playableCard = this.numberOfCards - extraCard;
    for (int i = 1; i <= this.playableCard; i++) {
      this.cards.add(new Card(Constants.getRandomSuits(), random.nextInt(13) + 1));
    }
  }

  public void dealtCard() {
    Collections.shuffle(cards);
    int i = 0;
    for (Card card : this.cards) {
      int playerIdx = i % numberOfPlayers;
      players.get(playerIdx).cards.add(card);
      i += 1;
    }
    for (Player player : this.players) {
      Collections.sort(player.getCards());
    }
  }

  public void play() {
    int cardsToPlay = (int)this.playableCard/numberOfPlayers;
    int round = 0;
    while (true) {
      if(cardsToPlay == 0) {
        break;
      }
      
      ArrayList<Player> winningPlayers = new ArrayList<Player>();
      round+=1;
      System.out.println("ROUND : "+ round);
      winningPlayers = findRoundWinner(this.players);
      cardsToPlay -=1;
      int cardsPlayed = 1;
      while(winningPlayers.size()>1) {
        if(cardsToPlay == 0) {
          break;
        }
        round+=1;
        System.out.println("SUB-ROUND : "+ round);
        winningPlayers = findRoundWinner(winningPlayers);
        cardsToPlay-=1;
        cardsPlayed+=1;
      }
      winningPlayers.get(0).incrementScore(cardsPlayed);
    }
  }
  

  private ArrayList<Player> declareWinner() {
    ArrayList<Player> winners = new ArrayList<Player>();
    int maxScore = -1;
    for(Player player:this.players) {
      if(player.getScore() > maxScore) {
        maxScore = player.getScore();
        winners = new ArrayList<Player>();
        winners.add(player);
      }else if (player.getScore()==maxScore) {
        winners.add(player);
      }
    }
    return winners;
  }

  private ArrayList<Player> findRoundWinner(List<Player> players) {
    ArrayList<Player> winningPlayers = new ArrayList<Player>();
    int maxValue = -1;
    for (Player player : players) {
      System.out.println("Player : "+player.id+" with score : "+player.score+" throws : "+ player.cards.get(0));
      if (player.cards.get(0).faceValue > maxValue) {
        maxValue = player.cards.get(0).faceValue;
        winningPlayers = new ArrayList<Player>();
        winningPlayers.add(player);
      }else if(player.cards.get(0).faceValue == maxValue) {
        winningPlayers.add(player);
      }
      player.cards.remove(0);
    }
    return winningPlayers;
  }

  public static void main(String[] args) {
    Game game = new Game(4, 104);
    game.dealtCard();
    game.play();
    ArrayList<Player> winners= game.declareWinner();
    System.out.println(winners);
    System.out.println(game.players); // Debugging purpose
  }

}
