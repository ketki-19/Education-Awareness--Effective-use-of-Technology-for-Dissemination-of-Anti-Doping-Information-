import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      nav_home: "Home",
      nav_substances: "Substance Database",
      nav_study: "Study Materials",
      nav_quizzes: "Awareness Quizzes",
      nav_login: "Login",
      nav_register: "Register as Athlete",
      hero_title: "Education & Awareness – Effective Use of Technology for Dissemination of Anti-Doping Information",
      hero_subtitle: "Empowering elite athletes, coaches, and sports academies with WADA-compliant digital technology, verified prohibited substance databases, and professional clean sport education.",
      explore_btn: "Explore Clean Sport",
      chatbot_title: "CleanSport AI Advisor",
      chatbot_placeholder: "Ask about WADA rules, substances, or TUE..."
    }
  },
  hi: {
    translation: {
      nav_home: "होम",
      nav_substances: "पदार्थ डेटाबेस",
      nav_study: "अध्ययन सामग्री",
      nav_quizzes: "जागरूकता क्विज़",
      nav_login: "लॉगिन",
      nav_register: "एथलीट के रूप में पंजीकरण करें",
      hero_title: "शिक्षा और जागरूकता - डोपिंग रोधी सूचना प्रसार के लिए प्रौद्योगिकी का प्रभावी उपयोग",
      hero_subtitle: "वाडा-अनुरूप डिजिटल तकनीक, सत्यापित प्रतिबंधित पदार्थ डेटाबेस और पेशेवर स्वच्छ खेल शिक्षा के साथ एथलीटों और प्रशिक्षकों का सशक्तिकरण।",
      explore_btn: "क्लीन स्पोर्ट देखें",
      chatbot_title: "क्लीनस्पोर्ट एआई सलाहकार",
      chatbot_placeholder: "वाडा नियमों, पदार्थों या TUE के बारे में पूछें..."
    }
  }
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'en',
  fallbackLng: 'en',
  interpolation: { escapeValue: false }
});

export default i18n;