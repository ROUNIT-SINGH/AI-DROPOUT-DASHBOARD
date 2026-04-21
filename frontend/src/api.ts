const API_URL = 'http://localhost:8000';

export interface Student {
    student_id: string;
    name: string;
    age: number;
    attendance_rate: number;
    gpa: number;
    financial_aid: boolean;
    failed_courses: number;
    extracurricular_activities: boolean;
    dropout_risk_score?: number;
    risk_category?: string;
}

export interface StudentCreate {
    student_id: string;
    name: string;
    age: number;
    attendance_rate: number;
    gpa: number;
    financial_aid: boolean;
    failed_courses: number;
    extracurricular_activities: boolean;
}

export interface ChatRequest {
    student_id: string;
    message: string;
}

export const createStudent = async (student: StudentCreate): Promise<Student> => {
    const response = await fetch(`${API_URL}/students/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(student)
    });
    if (!response.ok) throw new Error('Failed to create student');
    return response.json();
};

export const getStudent = async (studentId: string): Promise<Student> => {
    const response = await fetch(`${API_URL}/students/${studentId}`);
    if (!response.ok) throw new Error('Failed to get student');
    return response.json();
};

export const chatWithCounselor = async (chatReq: ChatRequest): Promise<{reply: string}> => {
    const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(chatReq)
    });
    if (!response.ok) throw new Error('Failed to send message');
    return response.json();
};
