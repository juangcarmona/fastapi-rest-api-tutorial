from mediatr import Mediator
from qna_api.questions.models import QuestionCreate, QuestionResponse
from qna_api.domain.question import QuestionEntity
from qna_api.questions.repository import QuestionRepository

class CreateQuestionCommand:
    def __init__(self, question: QuestionCreate, user_id: int):
        self.question = question
        self.user_id = user_id

@Mediator.handler
class CreateQuestionCommandHandler:
    def __init__(self):
        self.question_repository = QuestionRepository.instance()

    def handle(self, request: CreateQuestionCommand) -> QuestionResponse:
        db_question = QuestionEntity(
            title=request.question.title,
            description=request.question.description,
            user_id=request.user_id
        )
        self.question_repository.create(db_question)
        return QuestionResponse.model_validate(db_question, from_attributes=True)
