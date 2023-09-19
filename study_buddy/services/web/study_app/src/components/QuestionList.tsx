import {Question} from "../interfaces/question_interfaces.tsx";

interface ListGroupProps {
    items: Question[];
}

function QuestionList({items}: ListGroupProps) {

    return (
        <>
            <h1>Questions</h1>
            <ul className="list-group">
                {
                    items.map((question: Question) => (
                            <li className="list-group-item" key={question.question_id}>{question.question}</li>
                        )
                    )
                }
            </ul>
        </>
    );
}

export default QuestionList;