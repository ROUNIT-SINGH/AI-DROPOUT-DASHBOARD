import React, { useState } from 'react';
import './App.css';
import { createStudent, chatWithCounselor } from './api';
import type { Student, StudentCreate } from './api';

const LANGUAGES = [
  { code: 'auto', label: '🌐 Auto Detect' },
  { code: 'English', label: '🇬🇧 English' },
  { code: 'Hindi', label: '🇮🇳 Hindi (हिंदी)' },
  { code: 'Hinglish', label: '🇮🇳 Hinglish' },
  { code: 'Spanish', label: '🇪🇸 Spanish' },
  { code: 'French', label: '🇫🇷 French' },
  { code: 'Arabic', label: '🇸🇦 Arabic' },
  { code: 'Bengali', label: '🇧🇩 Bengali (বাংলা)' },
  { code: 'Tamil', label: '🇮🇳 Tamil (தமிழ்)' },
  { code: 'Telugu', label: '🇮🇳 Telugu (తెలుగు)' },
  { code: 'Marathi', label: '🇮🇳 Marathi (मराठी)' },
  { code: 'Gujarati', label: '🇮🇳 Gujarati (ગુજરાતી)' },
  { code: 'Punjabi', label: '🇮🇳 Punjabi (ਪੰਜਾਬੀ)' },
  { code: 'Urdu', label: '🇵🇰 Urdu (اردو)' },
  { code: 'German', label: '🇩🇪 German' },
  { code: 'Portuguese', label: '🇧🇷 Portuguese' },
  { code: 'Chinese', label: '🇨🇳 Chinese (中文)' },
  { code: 'Japanese', label: '🇯🇵 Japanese (日本語)' },
];

function App() {
  const [student, setStudent] = useState<Student | null>(null);
  const [loading, setLoading] = useState(false);
  const [chatMessage, setChatMessage] = useState('');
  const [chatHistory, setChatHistory] = useState<{ sender: 'user' | 'bot', text: string }[]>([]);
  const [chatLoading, setChatLoading] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('auto');

  // Form State
  const [formData, setFormData] = useState<StudentCreate>({
    student_id: `STU-${Math.floor(Math.random() * 10000)}`,
    name: '',
    age: 20,
    attendance_rate: 0.85,
    gpa: 3.0,
    financial_aid: true,
    failed_courses: 0,
    extracurricular_activities: false
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value, type } = e.target;
    let finalValue: any = value;

    if (type === 'number') {
      finalValue = parseFloat(value);
    } else if (type === 'checkbox') {
      finalValue = (e.target as HTMLInputElement).checked;
    } else if (value === 'true' || value === 'false') {
      finalValue = value === 'true';
    }

    setFormData(prev => ({ ...prev, [name]: finalValue }));
  };

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const result = await createStudent(formData);
      setStudent(result);
      setChatHistory([{ 
        sender: 'bot', 
        text: `Hi! I'm your AI Counselor powered by Gemini. I've reviewed ${result.name}'s profile — risk category is ${result.risk_category}. How can I help you support this student? You can chat in any language!` 
      }]);
    } catch (error) {
      console.error("Analysis failed", error);
      alert("Failed to analyze student. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!chatMessage.trim() || !student) return;

    const userMsg = chatMessage;
    setChatHistory(prev => [...prev, { sender: 'user', text: userMsg }]);
    setChatMessage('');
    setChatLoading(true);

    try {
      const res = await chatWithCounselor({
        student_id: student.student_id,
        message: userMsg,
        language: selectedLanguage
      });
      setChatHistory(prev => [...prev, { sender: 'bot', text: res.reply }]);
    } catch (error) {
      console.error("Chat failed", error);
      setChatHistory(prev => [...prev, { sender: 'bot', text: "Sorry, I couldn't process that. Please check if the backend is running." }]);
    } finally {
      setChatLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h1>AI Dropout Dashboard</h1>
        <p>Early Warning System &amp; AI Counselor · Powered by Gemini</p>
      </div>

      <div className="main-content">
        {/* Left Column: Student Form & Results */}
        <div className="card">
          <h2>Student Profile Analysis</h2>
          <form onSubmit={handleAnalyze} className="form-group">
            <div className="form-row">
              <div className="form-group">
                <label>Name</label>
                <input type="text" name="name" value={formData.name} onChange={handleInputChange} required placeholder="John Doe" />
              </div>
              <div className="form-group">
                <label>Student ID</label>
                <input type="text" name="student_id" value={formData.student_id} onChange={handleInputChange} required />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>GPA (0.0 - 4.0)</label>
                <input type="number" step="0.1" max="4.0" min="0" name="gpa" value={formData.gpa} onChange={handleInputChange} required />
              </div>
              <div className="form-group">
                <label>Attendance Rate (0.0 - 1.0)</label>
                <input type="number" step="0.01" max="1.0" min="0" name="attendance_rate" value={formData.attendance_rate} onChange={handleInputChange} required />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Failed Courses</label>
                <input type="number" min="0" name="failed_courses" value={formData.failed_courses} onChange={handleInputChange} required />
              </div>
              <div className="form-group">
                <label>Age</label>
                <input type="number" min="15" name="age" value={formData.age} onChange={handleInputChange} required />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Financial Aid</label>
                <select name="financial_aid" value={formData.financial_aid.toString()} onChange={handleInputChange}>
                  <option value="true">Yes</option>
                  <option value="false">No</option>
                </select>
              </div>
              <div className="form-group">
                <label>Extracurriculars</label>
                <select name="extracurricular_activities" value={formData.extracurricular_activities.toString()} onChange={handleInputChange}>
                  <option value="true">Yes</option>
                  <option value="false">No</option>
                </select>
              </div>
            </div>

            <button type="submit" className={`btn-primary ${loading ? 'loading' : ''}`} disabled={loading}>
              {loading ? 'Analyzing...' : 'Analyze Risk Score'}
            </button>
          </form>

          {student && student.dropout_risk_score !== undefined && (
            <div className="result-display">
              <h3>Dropout Risk Prediction</h3>
              <div className={`risk-score risk-${student.risk_category}`}>
                {(student.dropout_risk_score * 100).toFixed(1)}%
              </div>
              <p>Risk Category: <strong>{student.risk_category}</strong></p>
            </div>
          )}
        </div>

        {/* Right Column: AI Counselor Chat */}
        <div className="card chat-container">
          <div className="chat-header-row">
            <h2>🤖 AI Counselor</h2>
            <div className="language-selector-wrapper">
              <label htmlFor="language-select">🌐 Language</label>
              <select
                id="language-select"
                value={selectedLanguage}
                onChange={e => setSelectedLanguage(e.target.value)}
                className="language-select"
              >
                {LANGUAGES.map(lang => (
                  <option key={lang.code} value={lang.code}>{lang.label}</option>
                ))}
              </select>
            </div>
          </div>

          {!student ? (
            <div style={{ textAlign: 'center', opacity: 0.5, marginTop: '2rem' }}>
              <p>Analyze a student to start a counseling session.</p>
              <p style={{ fontSize: '0.85rem', marginTop: '0.5rem' }}>Supports 18+ languages including Hindi, Tamil, Spanish, and more.</p>
            </div>
          ) : (
            <>
              <div className="chat-messages">
                {chatHistory.map((msg, idx) => (
                  <div key={idx} className={`message ${msg.sender}`}>
                    {msg.text}
                  </div>
                ))}
                {chatLoading && (
                  <div className="message bot typing-indicator" style={{ opacity: 0.7 }}>
                    <span></span><span></span><span></span>
                  </div>
                )}
              </div>
              <form className="chat-input-area" onSubmit={handleSendMessage}>
                <input
                  type="text"
                  value={chatMessage}
                  onChange={e => setChatMessage(e.target.value)}
                  placeholder={`Ask in any language${selectedLanguage !== 'auto' ? ` (${selectedLanguage})` : ''}...`}
                  disabled={chatLoading}
                />
                <button type="submit" disabled={chatLoading}>Send</button>
              </form>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
