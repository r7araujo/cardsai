from cardsai.models import Flashcard

def test_create_Flashcard():
    card = Flashcard(
        front="der Apfel",
        back="a maçã",
        source_language="de",
        target_language="pt-BR",
    )
    assert card.front == "der Apfel"
    assert card.back == "a maçã"
    assert card.tags == []
    