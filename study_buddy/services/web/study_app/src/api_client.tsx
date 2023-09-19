import axios, {AxiosResponse} from "axios";
import {NewQuestion, Question} from "./interfaces/question_interfaces.tsx";


const API_URL = "http://127.0.0.1:8000"

const instance = axios.create(
    {
        baseURL: API_URL,
        timeout: 15000,
    }
)

const responseBody = (response: AxiosResponse) => response.data;

const requests = {
    get: (url: string) => instance.get(url).then(responseBody),
    post: (url: string, body: {}) => instance.post(url, body).then(responseBody),
    put: (url: string, body: {}) => instance.put(url, body).then(responseBody),
    delete: (url: string) => instance.delete(url).then(responseBody),
}

export const Questions = {
    getQuestions: (): Promise<Question[]> => requests.get("/questions/"),
    getQuestion: (question_id: number): Promise<Question> => requests.get(`/questions/${question_id}`),
    createQuestion: (question: NewQuestion): Promise<Question> => requests.post("/questions", question),
    deleteQuestion: (question_id: number): Promise<void> => requests.delete(`/questions/${question_id}`)
};
