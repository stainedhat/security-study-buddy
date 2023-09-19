//import Question from "./Question.tsx";
import QuestionList from "./components/QuestionList.tsx";
import {Questions} from "./api_client.tsx";
import {Question} from "./interfaces/question_interfaces.tsx";
import {useEffect, useState} from "react";

function App() {
    const [questions, setQuestions] = useState<Question[]>([])
    const [isError, setIsError] = useState<boolean>(false);

    useEffect(() => {
            Questions.getQuestions().then(
                (data) => {
                    setQuestions(data);
                }
            ).catch(
                () => {
                    setIsError(true);
                }
            )
            return () => {
            }
        }, []
    )
    return (
        <>
            {isError ? console.log("Error") : (
                <div><QuestionList items={questions}/></div>
            )
            }
        </>
    )
}

export default App
