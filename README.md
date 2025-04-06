// AI App Generator - Starter Template

// === Frontend (React + Tailwind + Monaco) ===

import React, { useState } from 'react'; import Editor from '@monaco-editor/react'; import { Button } from '@/components/ui/button';

export default function Home() { const [userInput, setUserInput] = useState(''); const [generatedCode, setGeneratedCode] = useState('// Generated code will appear here');

const handleGenerate = async () => { const res = await fetch('/api/generate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ prompt: userInput }) }); const data = await res.json(); setGeneratedCode(data.code); };

return ( <div className="p-6 max-w-screen-xl mx-auto"> <h1 className="text-3xl font-bold mb-4">AI App Generator</h1> <textarea className="w-full border rounded p-3 mb-4" placeholder="Describe your app..." rows={4} value={userInput} onChange={(e) => setUserInput(e.target.value)} /> <Button onClick={handleGenerate}>Generate App</Button> <div className="mt-6"> <Editor
height="400px"
defaultLanguage="javascript"
value={generatedCode}
theme="vs-dark"
/> </div> </div> ); }

