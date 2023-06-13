// App.js
import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [count, setCount] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!text.trim() || !count.trim()) {
      setError('Please provide both text and count.');
      return;
    }

    if (!Number.isInteger(+count) || +count <= 0) {
      setError('Count must be a positive integer.');
      return;
    }

    setError('');
    setOutput(text.repeat(+count));
  };

  return (
    <div className="App">
      <h1>React App</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="text">Text:</label>
          <input
            type="text"
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="count">Count:</label>
          <input
            type="number"
            id="count"
            value={count}
            onChange={(e) => setCount(e.target.value)}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {error && <p className="error">{error}</p>}
      {output && <p>{output}</p>}
    </div>
  );
}

export default App;
