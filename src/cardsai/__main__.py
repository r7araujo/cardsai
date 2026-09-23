from cardsai.models import Flashcard

def main():
      print("CardsAI — create a flashcard")

      front = input("Word or phrase: ").strip()
      back = input("Meaning: ").strip()
      source_language = input("Idioma da frente, ex.: de: ").strip()
      target_language = input("Idioma do significado, ex.: pt-BR: ").strip()

      card = Flashcard(
          front=front,
          back=back,
          source_language=source_language,
          target_language=target_language,
      )

      print("\nCartão criado:")
      print(f"{card.front} → {card.back}")
      print(f"{card.source_language} → {card.target_language}")


if __name__ == "__main__":
    main()