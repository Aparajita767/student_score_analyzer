import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from './components/Header';

export default function App() {
  return (
    <>
      <Header />
      <main className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
        <h2 className="text-4xl font-bold mb-4">Welcome to Student Score Analyzer</h2>
        <p className="text-lg text-gray-700 text-center max-w-xl">
          Upload student test scores and get insights fast!
        </p>
      </main>
    </>
  );
}

