from app import QUESTIONS, app


def test_quiz_has_at_least_thirty_questions():
    assert len(QUESTIONS) >= 30


def test_full_quiz_flow_keeps_context_and_scores_answers():
    app.config.update(TESTING=True, SECRET_KEY="test-secret")

    with app.test_client() as client:
        response = client.post("/quiz/start")
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/quiz/1")

        for number, question in enumerate(QUESTIONS, start=1):
            response = client.post(
                f"/quiz/{number}",
                data={"answer": question["answer"]},
                follow_redirects=True,
            )
            assert response.status_code == 200
            if number < len(QUESTIONS):
                assert b"Last scene: Nice read." in response.data

        assert b"30" in response.data
        assert b"100%" in response.data
        assert b"Genre Auteur" in response.data


def test_cannot_skip_unanswered_questions():
    app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with app.test_client() as client:
        client.post("/quiz/start")
        response = client.get("/quiz/12")
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/quiz/1")


def test_invalid_answer_is_rejected():
    app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with app.test_client() as client:
        client.post("/quiz/start")
        response = client.post("/quiz/1", data={"answer": "Not a genre"})
        assert response.status_code == 400
        assert b"Choose one answer" in response.data
