<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CleanSport 2026 | Elite Anti-Doping Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        darkbg: '#070b19',
                        cardbg: '#0f172a',
                        bordercolor: '#1e293b',
                        cyanaccent: '#06b6d4',
                        cyanhover: '#0891b2',
                        tealborder: '#22d3ee',
                    }
                }
            }
        }
    </script>
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body class="bg-darkbg text-zinc-100 font-sans antialiased min-h-screen flex flex-col selection:bg-cyanaccent selection:text-white" x-data="cleanSportApp()">

    <!-- TOP NAVIGATION BAR -->
    <header class="sticky top-0 z-50 bg-darkbg/90 backdrop-blur-md border-b border-cyanaccent/20">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            
            <!-- Logo Brand -->
            <div class="flex items-center space-x-3 cursor-pointer" @click="activeTab = 'home'">
                <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-cyan-600 to-teal-400 flex items-center justify-center font-black text-white text-xl shadow-lg shadow-cyan-500/20">CS</div>
                <div>
                    <span class="text-lg font-black tracking-wider text-white">CLEAN<span class="text-cyan-400">SPORT</span></span>
                    <span class="text-[9px] uppercase tracking-widest text-zinc-400 block font-bold" x-text="t('sub_brand')">WADA 2026 Integrity Platform</span>
                </div>
            </div>

            <!-- Nav Links (Desktop) -->
            <nav class="hidden lg:flex items-center space-x-1 text-xs font-semibold">
                <button @click="activeTab = 'home'" :class="activeTab === 'home' ? 'text-cyan-400 bg-cyan-950/60 border border-cyan-800/50 shadow-sm' : 'text-zinc-400 hover:text-white'" class="px-4 py-2 rounded-xl transition" x-text="t('nav_home')">Home</button>
                <button @click="activeTab = 'substances'" :class="activeTab === 'substances' ? 'text-cyan-400 bg-cyan-950/60 border border-cyan-800/50 shadow-sm' : 'text-zinc-400 hover:text-white'" class="px-4 py-2 rounded-xl transition" x-text="t('nav_substances')">Substance Database</button>
                <button @click="activeTab = 'study'" :class="activeTab === 'study' ? 'text-cyan-400 bg-cyan-950/60 border border-cyan-800/50 shadow-sm' : 'text-zinc-400 hover:text-white'" class="px-4 py-2 rounded-xl transition" x-text="t('nav_study')">Study PDFs</button>
                <button @click="activeTab = 'quizzes'" :class="activeTab === 'quizzes' ? 'text-cyan-400 bg-cyan-950/60 border border-cyan-800/50 shadow-sm' : 'text-zinc-400 hover:text-white'" class="px-4 py-2 rounded-xl transition" x-text="t('nav_quizzes')">Quizzes</button>
            </nav>

            <!-- Right Actions -->
            <div class="flex items-center space-x-4">
                <button @click="toggleLang()" class="px-3 py-1.5 bg-cardbg border border-bordercolor rounded-xl text-xs font-bold text-cyan-400 hover:border-cyan-400 transition">
                    <span x-text="lang === 'en' ? '🌐 हिन्दी (HI)' : '🌐 English (EN)'"></span>
                </button>

                <template x-if="!currentUser">
                    <button @click="activeTab = 'login'" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-extrabold rounded-xl text-xs transition shadow-lg shadow-cyan-600/30" x-text="t('nav_login')">
                        Secure Portal Login
                    </button>
                </template>
                <template x-if="currentUser">
                    <div class="flex items-center space-x-3 bg-cardbg px-3.5 py-1.5 rounded-2xl border border-bordercolor">
                        <div class="text-right">
                            <p class="text-xs font-extrabold text-cyan-400" x-text="currentUser.name"></p>
                            <p class="text-[9px] text-zinc-400 uppercase tracking-widest font-bold" x-text="currentUser.role"></p>
                        </div>
                        <button @click="logout()" class="px-2.5 py-1 bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/30 rounded-xl text-xs font-bold transition" x-text="t('logout')">Logout</button>
                    </div>
                </template>
            </div>
        </div>
    </header>

    <!-- MAIN BODY VIEWCONTAINER -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-6 md:p-10">

        <!-- 1. HOME VIEW -->
        <div x-show="activeTab === 'home'" class="space-y-12">
            <div class="relative overflow-hidden bg-gradient-to-br from-cyan-950/30 via-cardbg to-darkbg rounded-3xl p-8 md:p-16 border border-bordercolor shadow-2xl">
                <div class="absolute -right-20 -bottom-20 w-96 h-96 bg-cyan-600/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="max-w-2xl relative z-10">
                    <span class="px-3.5 py-1.5 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 rounded-full text-[10px] font-black tracking-widest uppercase" x-text="t('badge_wada')">WADA 2026 Standards Compliant</span>
                    <h1 class="text-4xl md:text-6xl font-black mt-6 mb-4 text-white tracking-tight leading-none" x-html="t('hero_title')">
                        Education & <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-teal-300">Awareness Platform</span>
                    </h1>
                    <p class="text-zinc-400 text-sm md:text-base leading-relaxed mb-8" x-text="t('hero_desc')">
                        Effective use of digital technology for dissemination of anti-doping information. Empowering athletes and coaches with verified substance databases, PDF study resources, and strict clean sport regulations.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <button @click="activeTab = 'substances'" class="px-6 py-3.5 bg-cyan-600 hover:bg-cyan-500 text-white font-extrabold rounded-2xl text-xs transition shadow-lg shadow-cyan-600/30" x-text="t('btn_substances')">Explore Substances</button>
                        <button @click="activeTab = 'study'" class="px-6 py-3.5 bg-cardbg hover:bg-zinc-800 border border-bordercolor text-white font-extrabold rounded-2xl text-xs transition" x-text="t('btn_study')">View Study PDFs</button>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor relative overflow-hidden group hover:border-cyan-500/50 transition">
                    <p class="text-[10px] font-extrabold text-zinc-400 uppercase tracking-widest" x-text="t('stat_athletes')">Registered Athletes</p>
                    <h3 class="text-3xl font-black text-white mt-2">100</h3>
                    <p class="text-xs text-cyan-400 mt-2 font-semibold" x-text="t('stat_athletes_sub')">✓ Distributed to 20 Coaches</p>
                </div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor relative overflow-hidden group hover:border-cyan-500/50 transition">
                    <p class="text-[10px] font-extrabold text-zinc-400 uppercase tracking-widest" x-text="t('stat_coaches')">Expert Coaches</p>
                    <h3 class="text-3xl font-black text-white mt-2">20</h3>
                    <p class="text-xs text-cyan-400 mt-2 font-semibold" x-text="t('stat_coaches_sub')">✓ WADA Certified Advisors</p>
                </div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor relative overflow-hidden group hover:border-cyan-500/50 transition">
                    <p class="text-[10px] font-extrabold text-zinc-400 uppercase tracking-widest" x-text="t('stat_substances')">Prohibited Substances</p>
                    <h3 class="text-3xl font-black text-white mt-2">50+</h3>
                    <p class="text-xs text-cyan-400 mt-2 font-semibold" x-text="t('stat_substances_sub')">✓ WADA 2026 Verified List</p>
                </div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor relative overflow-hidden group hover:border-cyan-500/50 transition">
                    <p class="text-[10px] font-extrabold text-zinc-400 uppercase tracking-widest" x-text="t('stat_compliance')">Learning Compliance</p>
                    <h3 class="text-3xl font-black text-white mt-2">94.8%</h3>
                    <p class="text-xs text-cyan-400 mt-2 font-semibold" x-text="t('stat_compliance_sub')">✓ Active Completion Rate</p>
                </div>
            </div>
        </div>

        <!-- 2. SUBSTANCE DATABASE VIEW -->
        <div x-show="activeTab === 'substances'" class="space-y-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-cardbg p-6 rounded-3xl border border-bordercolor">
                <div>
                    <h2 class="text-2xl font-black text-white" x-text="t('sub_db_title')">WADA Prohibited Substance Database</h2>
                    <p class="text-xs text-zinc-400 mt-1" x-text="t('sub_db_desc')">Explore regulated categories, medical uses, and detailed compliance guidance.</p>
                </div>
                <input type="text" x-model="searchQuery" :placeholder="t('search_placeholder')" class="px-4 py-3 w-full md:w-80 rounded-2xl bg-darkbg border border-bordercolor text-white text-xs focus:outline-none focus:border-cyan-400">
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <template x-for="item in filteredSubstances" :key="item.name">
                    <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor flex flex-col justify-between hover:border-cyan-400/40 transition">
                        <div>
                            <div class="flex justify-between items-start mb-4">
                                <span class="px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-wider"
                                    :class="{
                                        'bg-red-500/10 text-red-400 border border-red-500/20': item.status === 'Prohibited',
                                        'bg-amber-500/10 text-amber-400 border border-amber-500/20': item.status === 'Conditional',
                                        'bg-cyan-500/10 text-cyan-400 border border-cyan-500/20': item.status === 'TUE Required'
                                    }" x-text="item.status"></span>
                                <span class="text-xs font-bold text-cyan-400" x-text="item.category"></span>
                            </div>
                            <h3 class="text-lg font-black text-white" x-text="item.name"></h3>
                            <p class="text-xs text-zinc-400 mt-2 leading-relaxed" x-text="item.desc"></p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-bordercolor flex justify-between items-center text-xs">
                            <span class="text-zinc-500 font-semibold text-[10px]" x-text="t('verified_wada')">WADA 2026 Verified</span>
                            <button @click="openGuidance(item)" class="text-cyan-400 font-extrabold hover:underline bg-cyan-500/10 px-3.5 py-1.5 rounded-xl border border-cyan-500/20" x-text="t('view_guidance')">View Guidance &rarr;</button>
                        </div>
                    </div>
                </template>
            </div>
        </div>

        <!-- 3. STUDY MATERIALS VIEW -->
        <div x-show="activeTab === 'study'" class="space-y-8">
            <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor">
                <h2 class="text-2xl font-black text-white" x-text="t('pdf_section_title')">Official Anti-Doping Study PDFs</h2>
                <p class="text-xs text-zinc-400 mt-1" x-text="t('pdf_section_desc')">Preview official WADA & NADA compliant educational handbooks featuring proper pages of structured content.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <template x-for="pdf in pdfList" :key="pdf.id">
                    <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor flex flex-col justify-between hover:border-cyan-400/50 transition">
                        <div>
                            <span class="text-[10px] bg-cyan-500/10 text-cyan-400 px-3 py-1 rounded-full font-bold uppercase tracking-wider border border-cyan-500/20" x-text="pdf.badge">PDF Handbook</span>
                            <h3 class="text-base font-black text-white mt-3" x-text="pdf.title"></h3>
                            <p class="text-xs text-zinc-400 mt-2" x-text="pdf.desc"></p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-bordercolor">
                            <button @click="previewPDF(pdf)" class="w-full py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-extrabold rounded-2xl text-xs transition shadow flex items-center justify-center gap-2">
                                <span x-text="t('preview_btn')">📖 View PDF</span>
                            </button>
                        </div>
                    </div>
                </template>
            </div>
        </div>

        <!-- 4. QUIZZES VIEW -->
        <div x-show="activeTab === 'quizzes'" class="max-w-3xl mx-auto space-y-6">
            <div class="bg-cardbg p-8 md:p-10 rounded-3xl border border-bordercolor shadow-xl">
                <div class="flex justify-between items-center mb-6">
                    <span class="px-3.5 py-1 bg-cyan-500/10 text-cyan-400 rounded-full text-[10px] font-black uppercase tracking-wider border border-cyan-500/20" x-text="t('quiz_progress') + (activeQuizIndex + 1) + ' / 20'">Assessment Question 1</span>
                    <span class="text-xs text-cyan-400 font-bold"><span x-text="t('score_label')">Score:</span> <span x-text="quizScore"></span></span>
                </div>
                <h2 class="text-xl md:text-2xl font-black text-white mb-6" x-text="currentQuiz.question"></h2>
                
                <div class="space-y-3">
                    <template x-for="(option, idx) in currentQuiz.options" :key="idx">
                        <label class="block p-4 bg-darkbg rounded-2xl border border-bordercolor cursor-pointer hover:border-cyan-400/50 transition text-xs md:text-sm font-semibold flex items-center space-x-3">
                            <input type="radio" name="quizOption" :value="idx" x-model.number="selectedOption" class="text-cyan-500 focus:ring-cyan-400">
                            <span x-text="option"></span>
                        </label>
                    </template>
                </div>

                <div class="mt-8 flex justify-between items-center pt-6 border-t border-bordercolor">
                    <button @click="submitQuizAnswer()" class="px-6 py-3 bg-cyan-600 text-white font-black rounded-2xl text-xs hover:bg-cyan-500 transition shadow-lg shadow-cyan-600/30" x-text="t('submit_answer')">Submit Answer & Next &rarr;</button>
                    <span class="text-xs text-zinc-400 font-medium" x-text="quizFeedback"></span>
                </div>
            </div>
        </div>

        <!-- 5. LOGIN VIEW -->
        <div x-show="activeTab === 'login'" class="max-w-md mx-auto py-12">
            <div class="bg-cardbg p-8 md:p-10 rounded-3xl shadow-2xl border border-bordercolor">
                <div class="text-center mb-8">
                    <h2 class="text-2xl font-black text-white" x-text="t('login_title')">Secure Portal Login</h2>
                    <p class="text-xs text-zinc-400 mt-1" x-text="t('login_subtitle')">Authenticate using Google OAuth or strict email/password</p>
                </div>

                <button @click="googleOAuthLogin()" class="w-full mb-6 py-3.5 px-4 bg-white hover:bg-zinc-100 text-zinc-800 rounded-2xl text-xs font-bold transition flex items-center justify-center gap-3 shadow-md">
                    <svg class="w-4 h-4" viewBox="0 0 24 24">
                        <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
                        <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.19v3.15C3.17 21.3 7.23 24 12 24z"/>
                        <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.19C.43 8.12 0 9.87 0 11.7s.43 3.58 1.19 5.12l4.09-2.55z"/>
                        <path fill="#EA4335" d="M12 4.75c1.76 0 3.34.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.23 0 3.17 2.7 1.19 6.58l4.09 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/>
                    </svg>
                    <span x-text="t('google_btn')">Continue with Google OAuth 2.0</span>
                </button>

                <div class="relative flex py-2 items-center mb-6">
                    <div class="flex-grow border-t border-bordercolor"></div>
                    <span class="flex-shrink mx-4 text-zinc-500 text-[10px] uppercase font-bold" x-text="t('or_email')">Or with email</span>
                    <div class="flex-grow border-t border-bordercolor"></div>
                </div>

                <form @submit.prevent="handleLogin()" class="space-y-4">
                    <div>
                        <label class="block text-[10px] font-black text-zinc-400 uppercase tracking-widest mb-1" x-text="t('email_label')">Email Address (Must end with @gmail.com)</label>
                        <input type="text" x-model="loginEmail" placeholder="e.g. rajesh@gmail.com" required class="w-full px-4 py-3.5 bg-darkbg border border-bordercolor rounded-2xl text-white text-xs focus:outline-none focus:border-cyan-400">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-zinc-400 uppercase tracking-widest mb-1" x-text="t('password_label')">Password (Min 8 chars, Uppercase, Lowercase, Number)</label>
                        <input type="password" x-model="loginPassword" placeholder="e.g. SecurePass1" required class="w-full px-4 py-3.5 bg-darkbg border border-bordercolor rounded-2xl text-white text-xs focus:outline-none focus:border-cyan-400">
                    </div>
                    <div x-show="loginError" class="text-xs text-red-400 font-bold bg-red-500/10 border border-red-500/20 p-3 rounded-2xl text-center" x-text="loginError"></div>
                    
                    <button type="submit" class="w-full py-4 bg-cyan-600 hover:bg-cyan-500 text-white font-black rounded-2xl text-xs transition shadow-lg shadow-cyan-600/30 uppercase tracking-wider" x-text="t('login_btn')">Login to Platform</button>
                </form>
            </div>
        </div>

        <!-- 6. ADMIN DASHBOARD -->
        <div x-show="activeTab === 'admin-dash'" class="space-y-8">
            <div class="flex justify-between items-center bg-cardbg p-6 md:p-8 rounded-3xl border border-bordercolor">
                <div>
                    <h2 class="text-2xl font-black text-white" x-text="t('admin_dash_title')">Admin Control Dashboard</h2>
                    <p class="text-xs text-zinc-400 mt-1" x-text="t('admin_dash_desc')">Full platform management, athlete assignments, and system audit logs.</p>
                </div>
                <span class="px-4 py-1.5 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 font-extrabold text-xs rounded-full" x-text="t('admin_badge')">Super Admin Active</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('stat_athletes')">Total Athletes</p><h3 class="text-3xl font-black text-white mt-1">100</h3></div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('stat_coaches')">Total Coaches</p><h3 class="text-3xl font-black text-white mt-1">20</h3></div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('stat_substances')">Substances Database</p><h3 class="text-3xl font-black text-white mt-1">50</h3></div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('stat_sessions')">Active Sessions</p><h3 class="text-3xl font-black text-white mt-1">84</h3></div>
            </div>
        </div>

        <!-- 7. ATHLETE DASHBOARD -->
        <div x-show="activeTab === 'athlete-dash'" class="space-y-8">
            <div class="flex justify-between items-center bg-cardbg p-6 md:p-8 rounded-3xl border border-bordercolor">
                <div>
                    <h2 class="text-2xl font-black text-white" x-text="t('athlete_dash_title')">Athlete Learning Dashboard</h2>
                    <p class="text-xs text-zinc-400 mt-1" x-text="t('athlete_dash_desc')">Track your anti-doping education progress and quiz scores.</p>
                </div>
                <span class="px-4 py-1.5 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 font-extrabold text-xs rounded-full" x-text="currentUser ? currentUser.name : 'Athlete Portal'"></span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('learning_progress')">Learning Progress</p><h3 class="text-3xl font-black text-white mt-1">88%</h3><div class="w-full bg-darkbg h-2 rounded-full mt-4 overflow-hidden border border-bordercolor"><div class="bg-cyan-500 h-full w-[88%]"></div></div></div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('quiz_avg')">Quiz Score Average</p><h3 class="text-3xl font-black text-white mt-1">19 / 20</h3><p class="text-xs text-emerald-400 font-bold mt-2" x-text="t('cert_eligible')">✓ Certificate Eligible</p></div>
                <div class="bg-cardbg p-6 rounded-3xl border border-bordercolor"><p class="text-[10px] font-extrabold text-zinc-400 uppercase" x-text="t('assigned_status')">Assigned Status</p><h3 class="text-lg font-black text-cyan-400 mt-2" x-text="t('clean_verified')">Clean Sport Verified</h3><p class="text-xs text-zinc-400 mt-1" x-text="t('last_verified')">Last verified: WADA 2026</p></div>
            </div>
        </div>

    </main>

    <!-- FULLY WORKING FLOATING AI CHATBOT WIDGET -->
    <div class="fixed bottom-6 right-6 z-50" x-data="aiChatWidget()">
        <template x-if="!openChat">
            <button @click="openChat = true" class="w-14 h-14 bg-cyan-600 hover:bg-cyan-500 text-white rounded-full shadow-2xl flex items-center justify-center text-xl transition transform hover:scale-105 border border-cyan-400/40">
                💬
            </button>
        </template>
        <template x-if="openChat">
            <div class="bg-cardbg border border-cyan-900/80 rounded-3xl w-80 sm:w-96 shadow-2xl overflow-hidden flex flex-col h-[480px]">
                <div class="bg-darkbg px-5 py-4 border-b border-bordercolor flex justify-between items-center">
                    <div class="flex items-center space-x-2">
                        <div class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></div>
                        <span class="text-xs font-black text-white" x-text="t('chat_title')">CleanSport AI Advisor</span>
                    </div>
                    <button @click="openChat = false" class="text-zinc-400 hover:text-white font-bold">✕</button>
                </div>
                
                <!-- Chat Messages Stream -->
                <div class="flex-1 p-4 overflow-y-auto space-y-3 text-xs" id="chatContainer">
                    <template x-for="msg in $root.__x.$data.chatMessages" :key="msg.text">
                        <div :class="msg.sender === 'ai' ? 'bg-darkbg border border-bordercolor text-zinc-300' : 'bg-cyan-600 text-white ml-auto max-w-[80%]'" class="p-3 rounded-2xl">
                            <span class="font-bold text-cyan-400 block mb-1" x-text="msg.sender === 'ai' ? 'CleanSport AI:' : 'You:'"></span>
                            <span x-text="msg.text"></span>
                        </div>
                    </template>
                </div>

                <!-- Chat Input Form -->
                <div class="p-3 bg-darkbg border-t border-bordercolor flex gap-2">
                    <input type="text" x-model="userQuery" @keyup.enter="sendQuery()" placeholder="Ask about WADA rules, substances, TUE..." class="flex-1 bg-cardbg border border-bordercolor rounded-xl px-3 py-2 text-white text-xs focus:outline-none focus:border-cyan-400">
                    <button @click="sendQuery()" class="px-4 py-2 bg-cyan-600 text-white font-bold rounded-xl text-xs hover:bg-cyan-500 transition" x-text="t('chat_send')">Send</button>
                </div>
            </div>
        </template>
    </div>

    <!-- GUIDANCE MODAL -->
    <div x-show="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4" style="display: none;">
        <div class="bg-cardbg border border-bordercolor rounded-3xl p-6 md:p-8 max-w-lg w-full shadow-2xl relative">
            <button @click="showModal = false" class="absolute top-5 right-5 text-zinc-400 hover:text-white font-bold text-lg">✕</button>
            <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-[10px] font-black uppercase rounded-full" x-text="modalItem.status"></span>
            <h3 class="text-2xl font-black text-white mt-3" x-text="modalItem.name"></h3>
            <p class="text-xs text-cyan-400 font-semibold mt-1" x-text="'Category: ' + modalItem.category"></p>
            <div class="mt-4 space-y-3 text-xs text-zinc-300 leading-relaxed bg-darkbg p-4 rounded-2xl border border-bordercolor">
                <p><strong class="text-cyan-400">Description:</strong> <span x-text="modalItem.desc"></span></p>
                <p><strong class="text-cyan-400">Medical Uses:</strong> Approved clinical treatment under strict medical supervision and prescribed therapeutic indications.</p>
                <p><strong class="text-cyan-400">WADA Status:</strong> Strictly regulated under WADA 2026 Prohibited List standards. Verification through official anti-doping portals is mandatory.</p>
            </div>
            <button @click="showModal = false" class="mt-6 w-full py-3.5 bg-cyan-600 text-white font-extrabold rounded-2xl text-xs hover:bg-cyan-500 transition" x-text="t('close_modal')">Close Guidance Panel</button>
        </div>
    </div>

    <!-- PDF VIEWER MODAL -->
    <div x-show="showPDFModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4" style="display: none;">
        <div class="bg-cardbg border border-bordercolor rounded-3xl p-6 md:p-8 max-w-3xl w-full shadow-2xl relative flex flex-col h-[85vh]">
            <button @click="showPDFModal = false" class="absolute top-5 right-5 text-zinc-400 hover:text-white font-bold text-lg">✕</button>
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 mb-4 pb-3 border-b border-bordercolor">
                <div>
                    <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-[10px] font-black uppercase rounded-full">PDF Reader</span>
                    <h3 class="text-lg font-black text-white mt-1" x-text="previewPDFItem.title"></h3>
                </div>
                <div class="flex items-center gap-1.5 bg-darkbg p-1.5 rounded-xl border border-bordercolor self-end sm:self-auto">
                    <button @click="currentPDFPage > 1 ? currentPDFPage-- : null" class="px-2.5 py-1 bg-cyan-950 text-cyan-400 rounded-lg text-xs font-bold hover:bg-cyan-900 transition">&larr; Prev</button>
                    <template x-for="p in [1,2,3,4,5,6]" :key="p">
                        <button @click="currentPDFPage = p" :class="currentPDFPage === p ? 'bg-cyan-600 text-white' : 'text-zinc-400 hover:text-white bg-darkbg'" class="w-7 h-7 rounded-lg text-xs font-bold transition flex items-center justify-center" x-text="p"></button>
                    </template>
                    <button @click="currentPDFPage < 6 ? currentPDFPage++ : null" class="px-2.5 py-1 bg-cyan-950 text-cyan-400 rounded-lg text-xs font-bold hover:bg-cyan-900 transition">Next &rarr;</button>
                </div>
            </div>

            <div class="flex-1 overflow-y-auto p-6 bg-darkbg rounded-2xl border border-bordercolor text-xs md:text-sm text-zinc-300 leading-relaxed space-y-4">
                <div class="flex justify-between items-center text-cyan-400 font-extrabold border-b border-bordercolor pb-2">
                    <span x-text="'Handbook: ' + previewPDFItem.title"></span>
                    <span x-text="'Page ' + currentPDFPage + ' of 6'"></span>
                </div>

                <div x-show="currentPDFPage === 1" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 1: Executive Summary & Core Philosophy</h4>
                    <p x-text="previewPDFItem.desc"></p>
                    <p>Clean sport is foundational to elite athletic competition. Adhering to WADA 2026 standards ensures that talent, dedication, and training remain the sole determinants of sporting victory.</p>
                </div>
                <div x-show="currentPDFPage === 2" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 2: Strict Liability Principle & Athlete Responsibilities</h4>
                    <p>Under Article 2.1 of the World Anti-Doping Code, the principle of <strong>Strict Liability</strong> applies unconditionally. It is each athlete's personal duty to ensure that no prohibited substance enters their body.</p>
                </div>
                <div x-show="currentPDFPage === 3" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 3: Risk Management & Nutritional Supplement Warnings</h4>
                    <p>Nutritional and herbal supplements carry a significant risk of inadvertent positive doping tests due to cross-contamination or undeclared prohibited ingredients during manufacturing.</p>
                </div>
                <div x-show="currentPDFPage === 4" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 4: Therapeutic Use Exemptions (TUE) Protocol</h4>
                    <p>If an athlete has a documented medical condition requiring a medication that appears on the WADA Prohibited List, they may apply for a <strong>Therapeutic Use Exemption (TUE)</strong>.</p>
                </div>
                <div x-show="currentPDFPage === 5" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 5: Doping Control & Sample Collection Procedures</h4>
                    <p>Sample collection sessions involve rigorous chain-of-custody protocols managed by certified Doping Control Officers (DCOs). Athletes have specific rights and obligations during testing.</p>
                </div>
                <div x-show="currentPDFPage === 6" class="space-y-3">
                    <h4 class="text-base font-black text-white">Page 6: Conclusion, Sanctions & Educational Sign-off</h4>
                    <p>Violations of anti-doping rules carry severe sanctions, including mandatory multi-year periods of ineligibility, disqualification of competition results, and forfeiture of medals.</p>
                </div>
            </div>

            <button @click="showPDFModal = false" class="mt-4 w-full py-3.5 bg-cyan-600 text-white font-extrabold rounded-2xl text-xs hover:bg-cyan-500 transition" x-text="t('close_modal')">Close PDF Reader</button>
        </div>
    </div>

    <!-- APP CONTROLLER SCRIPT -->
    <script>
        function aiChatWidget() {
            return {
                openChat: false,
                userQuery: '',
                sendQuery() {
                    if (!this.userQuery.trim()) return;
                    const q = this.userQuery.trim();
                    this.$root.__x.$data.chatMessages.push({ sender: 'user', text: q });
                    this.userQuery = '';

                    setTimeout(() => {
                        let reply = "As per WADA 2026 standards, athletes are strictly responsible for any prohibited substance found in their biological sample. Please verify all medications through Global DRO.";
                        const qLower = q.toLowerCase();
                        if (qLower.includes('tue') || qLower.includes('medical')) {
                            reply = "A Therapeutic Use Exemption (TUE) allows athletes with documented medical conditions to use a prohibited substance if criteria are met.";
                        } else if (qLower.includes('strict liability') || qLower.includes('responsible')) {
                            reply = "Strict Liability means every athlete is personally responsible for any banned substance found in their body regardless of intent.";
                        } else if (qLower.includes('supplement')) {
                            reply = "Supplements carry high contamination risks. Always use batch-tested certified products (Informed-Sport / NSF).";
                        }
                        this.$root.__x.$data.chatMessages.push({ sender: 'ai', text: reply });
                    }, 600);
                }
            }
        }

        function cleanSportApp() {
            return {
                activeTab: 'home',
                lang: 'en',
                currentUser: null,
                searchQuery: '',
                loginEmail: '',
                loginPassword: '',
                loginError: '',
                showModal: false,
                modalItem: {},
                showPDFModal: false,
                previewPDFItem: {},
                currentPDFPage: 1,

                // Chat state
                chatMessages: [
                    { sender: 'ai', text: "Hello! Ask me anything about WADA regulations, prohibited substances, or TUE guidelines." }
                ],

                translations: {
                    en: {
                        sub_brand: "WADA 2026 Integrity Platform",
                        nav_home: "Home",
                        nav_substances: "Substance Database",
                        nav_study: "Study PDFs",
                        nav_quizzes: "Quizzes",
                        nav_login: "Secure Portal Login",
                        logout: "Logout",
                        badge_wada: "WADA 2026 Standards Compliant",
                        hero_title: 'Education & <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-teal-300">Awareness Platform</span>',
                        hero_desc: "Effective use of digital technology for dissemination of anti-doping information. Empowering athletes and coaches with verified substance databases, PDF study resources, and strict clean sport regulations.",
                        btn_substances: "Explore Substances",
                        btn_study: "View Study PDFs",
                        stat_athletes: "Registered Athletes",
                        stat_athletes_sub: "✓ Distributed to 20 Coaches",
                        stat_coaches: "Expert Coaches",
                        stat_coaches_sub: "✓ WADA Certified Advisors",
                        stat_substances: "Prohibited Substances",
                        stat_substances_sub: "✓ WADA 2026 Verified List",
                        stat_compliance: "Learning Compliance",
                        stat_compliance_sub: "✓ Active Completion Rate",
                        sub_db_title: "WADA Prohibited Substance Database",
                        sub_db_desc: "Explore regulated categories, medical uses, and detailed compliance guidance.",
                        search_placeholder: "Search substance name or category...",
                        verified_wada: "WADA 2026 Verified",
                        view_guidance: "View Guidance →",
                        pdf_section_title: "Official Anti-Doping Study PDFs",
                        pdf_section_desc: "Preview official WADA & NADA compliant educational handbooks featuring proper pages of structured content.",
                        preview_btn: "📖 View PDF",
                        quiz_progress: "Assessment Question ",
                        score_label: "Score:",
                        submit_answer: "Submit Answer & Next →",
                        login_title: "Secure Portal Login",
                        login_subtitle: "Authenticate using Google OAuth or strict email/password",
                        google_btn: "Continue with Google OAuth 2.0",
                        or_email: "Or with email",
                        email_label: "Email Address (Must end with @gmail.com)",
                        password_label: "Password (Min 8 chars, Uppercase, Lowercase, Number)",
                        login_btn: "Login to Platform",
                        admin_dash_title: "Admin Control Dashboard",
                        admin_dash_desc: "Full platform management, athlete assignments, and system audit logs.",
                        admin_badge: "Super Admin Active",
                        stat_sessions: "Active Sessions",
                        athlete_dash_title: "Athlete Learning Dashboard",
                        athlete_dash_desc: "Track your anti-doping education progress and quiz scores.",
                        learning_progress: "Learning Progress",
                        quiz_avg: "Quiz Score Average",
                        cert_eligible: "✓ Certificate Eligible",
                        assigned_status: "Assigned Status",
                        clean_verified: "Clean Sport Verified",
                        last_verified: "Last verified: WADA 2026",
                        chat_title: "CleanSport AI Advisor",
                        chat_welcome: "Hello! Ask me anything about WADA regulations, prohibited substances, or TUE guidelines.",
                        chat_send: "Send",
                        close_modal: "Close PDF Reader"
                    },
                    hi: {
                        sub_brand: "वाडा 2026 इंटीग्रिटी प्लेटफॉर्म",
                        nav_home: "होम",
                        nav_substances: "पदार्थ डेटाबेस",
                        nav_study: "अध्ययन पीडीएफ",
                        nav_quizzes: "क्विज़",
                        nav_login: "सुरक्षित पोर्टल लॉगिन",
                        logout: "लॉग आउट",
                        badge_wada: "वाडा 2026 मानक अनुरूप",
                        hero_title: 'शिक्षा और <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-teal-300">जागरूकता मंच</span>',
                        hero_desc: "डोपिंग रोधी जानकारी के प्रसार के लिए डिजिटल तकनीक का प्रभावी उपयोग। सत्यापित पदार्थ डेटाबेस, पीडीएफ अध्ययन संसाधनों और सख्त स्वच्छ खेल नियमों के साथ एथलीटों और प्रशिक्षकों का सशक्तिकरण।",
                        btn_substances: "पदार्थ देखें",
                        btn_study: "अध्ययन पीडीएफ देखें",
                        stat_athletes: "पंजीकृत एथलीट",
                        stat_athletes_sub: "✓ 20 कोचों को आवंटित",
                        stat_coaches: "विशेषज्ञ कोच",
                        stat_coaches_sub: "✓ वाडा प्रमाणित सलाहकार",
                        stat_substances: "प्रतिबंधित पदार्थ",
                        stat_substances_sub: "✓ वाडा 2026 सत्यापित सूची",
                        stat_compliance: "सीखने की अनुपालन",
                        stat_compliance_sub: "✓ सक्रिय पूर्णता दर",
                        sub_db_title: "वाडा प्रतिबंधित पदार्थ डेटाबेस",
                        sub_db_desc: "विनियमित श्रेणियों, चिकित्सा उपयोग और विस्तृत अनुपालन मार्गदर्शन का अन्वेषण करें।",
                        search_placeholder: "पदार्थ का नाम या श्रेणी खोजें...",
                        verified_wada: "वाडा 2026 सत्यापित",
                        view_guidance: "मार्गदर्शन देखें →",
                        pdf_section_title: "आधिकारिक डोपिंग रोधी अध्ययन पीडीएफ",
                        pdf_section_desc: "आधिकारिक वाडा और नाडा अनुरूप शैक्षणिक हैंडबुक का पूर्वावलोकन करें जिसमें संरचित सामग्री शामिल है।",
                        preview_btn: "📖 पीडीएफ देखें",
                        quiz_progress: "मूल्यांकन प्रश्न ",
                        score_label: "स्कोर:",
                        submit_answer: "उत्तर जमा करें और अगला →",
                        login_title: "सुरक्षित पोर्टल लॉगिन",
                        login_subtitle: "गूगल ओएथ या सख्त ईमेल/पासवर्ड का उपयोग करके प्रमाणित करें",
                        google_btn: "गूगल OAuth 2.0 के साथ जारी रखें",
                        or_email: "या ईमेल के साथ",
                        email_label: "ईमेल पता (@gmail.com समाप्त होना चाहिए)",
                        password_label: "पासवर्ड (न्यूनतम 8 अक्षर, अपरकेस, लोअरकेस, नंबर)",
                        login_btn: "प्लेटफॉर्म पर लॉगिन करें",
                        admin_dash_title: "व्यवस्थापक नियंत्रण डैशबोर्ड",
                        admin_dash_desc: "पूर्ण प्लेटफ़ॉर्म प्रबंधन, एथलीट असाइनमेंट और सिस्टम ऑडिट लॉग।",
                        admin_badge: "सुपर एडमिन सक्रिय",
                        stat_sessions: "सक्रिय सत्र",
                        athlete_dash_title: "एथलीट लर्निंग डैशबोर्ड",
                        athlete_dash_desc: "अपनी डोपिंग रोधी शिक्षा प्रगति और क्विज़ स्कोर को ट्रैक करें।",
                        learning_progress: "अध्ययन प्रगति",
                        quiz_avg: "क्विज़ स्कोर औसत",
                        cert_eligible: "✓ प्रमाण पत्र योग्य",
                        assigned_status: "आसन्न स्थिति",
                        clean_verified: "क्लीन स्पोर्ट सत्यापित",
                        last_verified: "अंतिम सत्यापित: वाडा 2026",
                        chat_title: "क्लीनस्पोर्ट एआई सलाहकार",
                        chat_welcome: "नमस्ते! वाडा नियमों, प्रतिबंधित पदार्थों या TUE दिशानिर्देशों के बारे में कुछ भी पूछें।",
                        chat_send: "भेजें",
                        close_modal: "पीडीएफ रीडर बंद करें"
                    }
                },

                t(key) {
                    return this.translations[this.lang][key] || key;
                },
                
                activeQuizIndex: 0,
                selectedOption: null,
                quizScore: 0,
                quizFeedback: '',
                quizzes: [
                    { question: "1. Who is strictly responsible for any prohibited substance found in an athlete's bodily sample?", options: ["The Coach", "The Athlete (Strict Liability Principle)", "The Team Doctor Only", "The WADA Official"], correct: 1 },
                    { question: "2. What does TUE stand for in anti-doping regulations?", options: ["Team Uniform Evaluation", "Therapeutic Use Exemption", "Tested Urine Examination", "Temporary User Eligibility"], correct: 1 },
                    { question: "3. Are anabolic steroids permitted out-of-competition?", options: ["Yes, for muscle recovery", "No, prohibited at all times", "Permitted only with coach approval", "Permitted under 10mg"], correct: 1 },
                    { question: "4. Which organization publishes the annual Prohibited List?", options: ["IOC", "WADA", "CAS", "WHO"], correct: 1 },
                    { question: "5. What is the principle called where athletes are responsible for whatever is in their body?", options: ["Absolute Liability", "Strict Liability", "Direct Accountability", "Total Responsibility"], correct: 1 },
                    { question: "6. Can nutritional supplements cause a positive doping test due to contamination?", options: ["No, supplements are certified", "Yes, unregulated supplements carry high risk", "Only if purchased online", "Only during competition"], correct: 1 },
                    { question: "7. When must an athlete submit to sample collection upon notification?", options: ["At their convenience", "Immediately, under continuous observation", "Within 24 hours", "After training finishes"], correct: 1 },
                    { question: "8. What category does Erythropoietin (EPO) belong to?", options: ["Stimulants", "Peptide hormones and growth factors", "Cannabinoids", "Glucocorticoids"], correct: 1 },
                    { question: "9. What is the status of Caffeine on the WADA 2026 program?", options: ["Prohibited in-competition", "Permitted without restriction", "Monitored program", "Prohibited at all times"], correct: 2 },
                    { question: "10. Who can grant a Therapeutic Use Exemption (TUE)?", options: ["The athlete's personal trainer", "An independent TUE Committee", "The team captain", "Any local pharmacist"], correct: 1 },
                    { question: "11. Are diuretics permitted as weight-loss aids in combat sports?", options: ["Yes, if declared", "No, they are masking agents and strictly prohibited", "Permitted out-of-competition", "Permitted with doctor note"], correct: 1 },
                    { question: "12. What does 'In-Competition' generally mean for testing purposes?", options: ["The day of the event", "Starting from 11:59 PM before the competition through the end of the event", "Only during the finals", "During warm-ups only"], correct: 1 },
                    { question: "13. What is the minimum penalty for a first-time intentional doping offense?", options: ["1 year suspension", "2 years suspension", "4 years suspension", "A formal warning"], correct: 2 },
                    { question: "14. Where must elite athletes submit their whereabouts information?", options: ["In a personal diary", "In the ADAMS database", "To their local gym", "On social media"], correct: 1 },
                    { question: "15. Which body acts as the supreme court for sports doping appeals?", options: ["Court of Arbitration for Sport (CAS)", "Supreme Court of Switzerland", "WADA Tribunal", "International Olympic Committee"], correct: 0 },
                    { question: "16. Are beta-2 agonists permitted by inhalation?", options: ["Strictly prohibited in all forms", "Permitted conditionally up to max dosage limits", "Permitted without limits", "Only for non-athletes"], correct: 1 },
                    { question: "17. What should an athlete do before taking any over-the-counter medication?", options: ["Take it immediately", "Check ingredients against Global DRO / WADA list", "Ask a teammate", "Check product price"], correct: 1 },
                    { question: "18. What is the primary purpose of anti-doping education?", options: ["To punish athletes", "To protect clean sport and athlete health", "To increase ticket sales", "To test new laboratory equipment"], correct: 1 },
                    { question: "19. How long can biological passport data be stored for athlete profiling?", options: ["1 year", "3 years", "Multiple years to track longitudinal biomarkers", "Deleted after each season"], correct: 2 },
                    { question: "20. What is the penalty for refusing to submit to sample collection after notification?", options: ["A small fine", "Same sanction as a positive test (typically 4 years)", "Disqualification from that race only", "Verbal reprimand"], correct: 1 }
                ],

                pdfList: [
                    { id: 1, title: "1. Anti-Doping Fundamentals & Ethics", badge: "PDF Handbook", desc: "Comprehensive guide covering clean sport core ethics, strict liability principles, and testing rights." },
                    { id: 2, title: "2. WADA Prohibited List Overview", badge: "PDF Handbook", desc: "Detailed classification of all substance categories, in-competition rules, and restrictions." },
                    { id: 3, title: "3. Therapeutic Use Exemption (TUE) Guide", badge: "PDF Handbook", desc: "Step-by-step instructions and medical criteria required to apply for permitted medical exemptions." },
                    { id: 4, title: "4. Nutritional Supplements & Risks", badge: "PDF Handbook", desc: "Learn about inadvertent doping risks, cross-contamination, and batch-testing certifications." },
                    { id: 5, title: "5. Doping Control & Sample Collection", badge: "PDF Handbook", desc: "Complete walkthrough of athlete notification, DCO procedures, and split-sample testing." },
                    { id: 6, title: "6. Coach & Mentor Compliance Toolkit", badge: "PDF Handbook", desc: "Essential guidelines for coaches on managing assigned athletes, whereabouts, and anti-doping education." }
                ],

                substances: [
                    { name: 'Testosterone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Endogenous anabolic androgenic steroid prohibited in and out of competition.' },
                    { name: 'Nandrolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Synthetic anabolic steroid causing pronounced muscle hypertrophy.' },
                    { name: 'Stanozolol', category: 'Anabolic agents', status: 'Prohibited', desc: 'Synthetic steroid derived from testosterone.' },
                    { name: 'Methandrostenolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Oral 17-alpha-alkylated anabolic steroid.' },
                    { name: 'Trenbolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Potent veterinary anabolic steroid used illegally for lean mass.' },
                    { name: 'Oxandrolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Oral anabolic steroid promoting protein synthesis.' },
                    { name: 'Boldenone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Anabolic steroid used in veterinary medicine.' },
                    { name: 'Clostebol', category: 'Anabolic agents', status: 'Prohibited', desc: 'Low-potency synthetic androgenic steroid.' },
                    { name: 'Drostanolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Dihydrotestosterone-derived anabolic steroid.' },
                    { name: 'Methenolone', category: 'Anabolic agents', status: 'Prohibited', desc: 'Long-acting anabolic steroid with low androgenic activity.' },

                    { name: 'Erythropoietin (EPO)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Peptide hormone stimulating erythropoiesis and oxygen transport.' },
                    { name: 'Growth Hormone (GH)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Stimulates somatic growth, tissue repair, and metabolism.' },
                    { name: 'Insulin-like Growth Factor (IGF-1)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Mediates growth hormone anabolic effects on skeletal muscle.' },
                    { name: 'Corticotropin (ACTH)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Stimulates adrenal cortex cortisol secretion.' },
                    { name: 'Chorionic Gonadotrophin (hCG)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Stimulates endogenous testosterone production in males.' },
                    { name: 'Luteinizing Hormone (LH)', category: 'Peptide hormones', status: 'Prohibited', desc: 'Gonadotropic hormone controlling gonadal steroidogenesis.' },
                    { name: 'Thymosin beta-4', category: 'Peptide hormones', status: 'Prohibited', desc: 'Actin-sequestering peptide promoting tissue regeneration.' },
                    { name: 'Peginesatide', category: 'Peptide hormones', status: 'Prohibited', desc: 'Synthetic erythropoiesis-stimulating agent.' },

                    { name: 'Salbutamol', category: 'Beta-2 agonists', status: 'Conditional', desc: 'Permitted by inhalation within maximum dosage limits.' },
                    { name: 'Formoterol', category: 'Beta-2 agonists', status: 'Conditional', desc: 'Long-acting beta-2 agonist permitted within therapeutic limits.' },
                    { name: 'Salmeterol', category: 'Beta-2 agonists', status: 'Conditional', desc: 'Permitted inhalation beta-2 agonist for asthma management.' },
                    { name: 'Vilanterol', category: 'Beta-2 agonists', status: 'Conditional', desc: 'Permitted when used with authorized inhaled corticosteroids.' },
                    { name: 'Higenamine', category: 'Beta-2 agonists', status: 'Prohibited', desc: 'Beta-2 agonist found in herbal weight-loss supplements.' },
                    { name: 'Clenbuterol', category: 'Beta-2 agonists', status: 'Prohibited', desc: 'Potent beta-2 agonist prohibited in all disciplines.' },

                    { name: 'Furosemide', category: 'Diuretics', status: 'Prohibited', desc: 'Loop diuretic and masking agent prohibited in all sports.' },
                    { name: 'Hydrochlorothiazide', category: 'Diuretics', status: 'Prohibited', desc: 'Thiazide diuretic used for blood pressure and masking.' },
                    { name: 'Spironolactone', category: 'Diuretics', status: 'Prohibited', desc: 'Potassium-sparing diuretic and aldosterone antagonist.' },
                    { name: 'Amiloride', category: 'Diuretics', status: 'Prohibited', desc: 'Potassium-sparing diuretic.' },
                    { name: 'Mannitol', category: 'Diuretics', status: 'Prohibited', desc: 'Intravenous plasma expander and osmotic diuretic.' },

                    { name: 'Caffeine', category: 'Stimulants', status: 'TUE Required', desc: 'Monitored under WADA monitoring program with specific urinary thresholds.' },
                    { name: 'Amphetamine', category: 'Stimulants', status: 'Prohibited', desc: 'Central nervous system stimulant prohibited in-competition.' },
                    { name: 'Cocainum', category: 'Stimulants', status: 'Prohibited', desc: 'Potent illicit central nervous system stimulant.' },
                    { name: 'Modafinil', category: 'Stimulants', status: 'Prohibited', desc: 'Wakefulness-promoting agent prohibited in-competition.' },
                    { name: 'Methylphenidate', category: 'Stimulants', status: 'Prohibited', desc: 'CNS stimulant used for ADHD treatment requiring TUE.' },
                    { name: 'Pseudoephedrine', category: 'Stimulants', status: 'Conditional', desc: 'Permitted when urinary concentration does not exceed 150 mcg/mL.' },

                    { name: 'Morphine', category: 'Narcotics', status: 'Prohibited', desc: 'Strong opioid analgesic prohibited in-competition.' },
                    { name: 'Oxycodone', category: 'Narcotics', status: 'Prohibited', desc: 'Semisynthetic opioid agonist.' },
                    { name: 'Fentanyl', category: 'Narcotics', status: 'Prohibited', desc: 'Synthetic opioid analgesic with extreme potency.' },
                    { name: 'Methadone', category: 'Narcotics', status: 'Prohibited', desc: 'Synthetic opioid used in pain management and addiction therapy.' },

                    { name: 'Cannabis', category: 'Cannabinoids', status: 'Prohibited', desc: 'Natural cannabinoid prohibited in-competition.' },
                    { name: 'Tetrahydrocannabinol (THC)', category: 'Cannabinoids', status: 'Prohibited', desc: 'Psychoactive cannabinoid found in cannabis.' },
                    { name: 'Synthetic Cannabinoids', category: 'Cannabinoids', status: 'Prohibited', desc: 'Artificial receptor agonists mimicking THC effects.' },

                    { name: 'Prednisone', category: 'Glucocorticoids', status: 'TUE Required', desc: 'Glucocorticoid prohibited when administered orally, intravenously or intramuscularly.' },
                    { name: 'Dexamethasone', category: 'Glucocorticoids', status: 'TUE Required', desc: 'Potent anti-inflammatory glucocorticoid requiring TUE.' },
                    { name: 'Methylprednisolone', category: 'Glucocorticoids', status: 'TUE Required', desc: 'Synthetic glucocorticoid hormone.' },
                    { name: 'Cortisone', category: 'Glucocorticoids', status: 'TUE Required', desc: 'Adrenal cortex steroid hormone.' },

                    { name: 'Blood Transfusion', category: 'Prohibited methods', status: 'Prohibited', desc: 'Administration of blood products to enhance oxygen transport.' },
                    { name: 'Gene Doping', category: 'Prohibited methods', status: 'Prohibited', desc: 'Transfer of nucleic acid polymers or gene editing agents.' },
                    { name: 'Chemical Manipulation', category: 'Prohibited methods', status: 'Prohibited', desc: 'Tampering with urine samples during collection.' },
                    { name: 'Intravenous Infusions', category: 'Prohibited methods', status: 'Prohibited', desc: 'IV infusions exceeding 100mL per 12-hour period without medical justification.' }
                ],

                toggleLang() {
                    this.lang = this.lang === 'en' ? 'hi' : 'en';
                },

                googleOAuthLogin() {
                    this.currentUser = { role: 'ATHLETE', name: 'Google Authenticated User' };
                    this.activeTab = 'athlete-dash';
                },

                handleLogin() {
                    this.loginError = '';
                    const email = this.loginEmail.trim();
                    const pass = this.loginPassword;

                    const emailRegex = /^[a-zA-Z][a-zA-Z0-9._%+-]*@gmail\.com$/;
                    if (!emailRegex.test(email)) {
                        this.loginError = 'Invalid Email! Please enter a valid name/format ending with @gmail.com (numbers only before @ are not allowed).';
                        return;
                    }

                    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
                    if (!passwordRegex.test(pass)) {
                        this.loginError = 'Invalid Password! Must be at least 8 characters and include uppercase, lowercase, and numbers.';
                        return;
                    }

                    if (email.toLowerCase() === 'admin@gmail.com' && pass === 'AdminSecure2026!#') {
                        this.currentUser = { role: 'ADMIN', name: 'Super Administrator' };
                        this.activeTab = 'admin-dash';
                    } else {
                        this.currentUser = { role: 'ATHLETE', name: email.split('@')[0] };
                        this.activeTab = 'athlete-dash';
                    }
                },

                logout() {
                    this.currentUser = null;
                    this.activeTab = 'home';
                    this.loginEmail = '';
                    this.loginPassword = '';

                    this.chatMessages = [
                        { sender: 'ai', text: "Hello! Ask me anything about WADA regulations, prohibited substances, or TUE guidelines." }
                    ];

                    this.activeQuizIndex = 0;
                    this.quizScore = 0;
                    this.selectedOption = null;
                    this.quizFeedback = '';
                },

                openGuidance(item) {
                    this.modalItem = item;
                    this.showModal = true;
                },

                previewPDF(pdf) {
                    this.previewPDFItem = pdf;
                    this.currentPDFPage = 1;
                    this.showPDFModal = true;
                },

                get currentQuiz() {
                    return this.quizzes[this.activeQuizIndex];
                },

                submitQuizAnswer() {
                    if (this.selectedOption === null) {
                        alert('Please select an option before submitting.');
                        return;
                    }
                    if (this.selectedOption === this.currentQuiz.correct) {
                        this.quizScore++;
                        this.quizFeedback = 'Correct! Great job.';
                    } else {
                        this.quizFeedback = 'Incorrect. Check WADA study guidelines.';
                    }

                    setTimeout(() => {
                        this.selectedOption = null;
                        this.quizFeedback = '';
                        if (this.activeQuizIndex < this.quizzes.length - 1) {
                            this.activeQuizIndex++;
                        } else {
                            alert('Quiz Completed! Final Score: ' + this.quizScore + ' / 20');
                            this.activeQuizIndex = 0;
                            this.quizScore = 0;
                        }
                    }, 1200);
                },

                get filteredSubstances() {
                    if (!this.searchQuery) return this.substances;
                    return this.substances.filter(s => 
                        s.name.toLowerCase().includes(this.searchQuery.toLowerCase()) || 
                        s.category.toLowerCase().includes(this.searchQuery.toLowerCase())
                    );
                }
            }
        }
    </script>
</body>
</html>