/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primaryBlack: '#090909',
        secondaryBlack: '#151515',
        premiumGold: '#D4AF37',
        lightGold: '#F2D27A',
        offWhite: '#F5F3ED',
        darkGrey: '#252525',
        mutedGrey: '#A6A6A6',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}