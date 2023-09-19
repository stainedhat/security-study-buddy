interface QuestionAPIResponse {
    questions: Question[];
}

interface Question {
    question_id: number;
    question: string;
    category: string;
}

interface NewQuestion {
    question_id: number;
    question: string;
    answer: string;
    category: string;
}

interface Answer {
    question: string;
    answer: string;
}

export type {Question, Answer, QuestionAPIResponse, NewQuestion};