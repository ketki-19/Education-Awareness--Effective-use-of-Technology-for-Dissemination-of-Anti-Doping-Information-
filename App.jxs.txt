import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import AIChatbotWidget from './components/AIChatbotWidget';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import AdminDashboard from './pages/AdminDashboard';
import CoachDashboard from './pages/CoachDashboard';
import AthleteDashboard from './pages/AthleteDashboard';
import SubstanceDatabase from './pages/SubstanceDatabase';
import SubstanceDetail from './pages/SubstanceDetail';
import StudyMaterials from './pages/StudyMaterials';
import Quizzes from './pages/Quizzes';
import './translations/i18n';

const ProtectedRoute = ({ children, allowedRoles }) => {
  const { user, loading } = useAuth();
  if (loading) return <div className="min-h-screen bg-primaryBlack text-premiumGold flex items-center justify-center">Loading CleanSport Platform...</div>;
  if (!user) return <Navigate to="/login" replace />;
  if (allowedRoles && !allowedRoles.includes(user.role)) return <Navigate to="/" replace />;
  return children;
};

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen bg-primaryBlack text-offWhite font-sans flex flex-col selection:bg-premiumGold selection:text-primaryBlack">
          <Navbar />
          <div className="flex-grow">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              
              <Route path="/substances" element={<ProtectedRoute><SubstanceDatabase /></ProtectedRoute>} />
              <Route path="/substances/:id" element={<ProtectedRoute><SubstanceDetail /></ProtectedRoute>} />
              <Route path="/study-materials" element={<ProtectedRoute><StudyMaterials /></ProtectedRoute>} />
              <Route path="/quizzes" element={<ProtectedRoute><Quizzes /></ProtectedRoute>} />

              <Route path="/admin-dashboard" element={<ProtectedRoute allowedRoles={['ADMIN']}><AdminDashboard /></ProtectedRoute>} />
              <Route path="/coach-dashboard" element={<ProtectedRoute allowedRoles={['COACH']}><CoachDashboard /></ProtectedRoute>} />
              <Route path="/athlete-dashboard" element={<ProtectedRoute allowedRoles={['ATHLETE']}><AthleteDashboard /></ProtectedRoute>} />
            </Routes>
          </div>
          <AIChatbotWidget />
          <Footer />
        </div>
      </Router>
    </AuthProvider>
  );
}