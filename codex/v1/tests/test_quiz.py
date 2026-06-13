import pytest

from app import QUESTIONS, create_app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SECRET_KEY": "testing-key"})
    return app.test_client()


def test_quiz_has_at_least_30_movie_type_questions():
    assert len(QUESTIONS) >= 30

    for question in QUESTIONS:
        assert question["prompt"]
        assert len(question["options"]) == 4
        assert question["answer"] in question["options"]
        assert question["category"]


def test_start_initializes_session_and_redirects_to_first_question(client):
    response = client.post("/start")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/quiz/1")

    with client.session_transaction() as session_data:
        assert session_data["current_index"] == 0
        assert session_data["score"] == 0
        assert session_data["answers"] == []
        assert session_data["last_feedback"] is None


def test_question_page_shows_one_question_and_progress(client):
    client.post("/start")

    response = client.get("/quiz/1")

    assert response.status_code == 200
    assert b"Question 1 of" in response.data
    assert QUESTIONS[0]["prompt"].encode() in response.data
    assert QUESTIONS[1]["prompt"].encode() not in response.data


def test_answer_moves_to_next_page_and_keeps_previous_context(client):
    client.post("/start")
    first_question = QUESTIONS[0]

    response = client.post("/quiz/1", data={"answer": first_question["answer"]})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/quiz/2")

    with client.session_transaction() as session_data:
        assert session_data["current_index"] == 1
        assert session_data["score"] == 1
        assert session_data["answers"] == [
            {
                "question": first_question["prompt"],
                "selected": first_question["answer"],
                "correct_answer": first_question["answer"],
                "is_correct": True,
            }
        ]
        assert session_data["last_feedback"]["is_correct"] is True

    next_page = client.get("/quiz/2")

    assert next_page.status_code == 200
    assert b"Last answer" in next_page.data
    assert b"Correct" in next_page.data
    assert first_question["answer"].encode() in next_page.data


def test_cannot_skip_ahead_without_answering_prior_questions(client):
    client.post("/start")

    response = client.get("/quiz/3")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/quiz/1")


def test_invalid_answer_stays_on_same_question_with_error(client):
    client.post("/start")

    response = client.post("/quiz/1", data={"answer": "Definitely not an option"})

    assert response.status_code == 400
    assert b"Choose one of the listed answers" in response.data

    with client.session_transaction() as session_data:
        assert session_data["current_index"] == 0
        assert session_data["score"] == 0
        assert session_data["answers"] == []


def test_finishing_all_questions_shows_final_score_and_answer_history(client):
    client.post("/start")

    for index, question in enumerate(QUESTIONS, start=1):
        response = client.post(f"/quiz/{index}", data={"answer": question["answer"]})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/result")

    result_page = client.get("/result")

    assert result_page.status_code == 200
    assert f"{len(QUESTIONS)} / {len(QUESTIONS)}".encode() in result_page.data
    assert QUESTIONS[-1]["prompt"].encode() in result_page.data


def test_result_redirects_to_start_when_quiz_has_not_started(client):
    response = client.get("/result")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
