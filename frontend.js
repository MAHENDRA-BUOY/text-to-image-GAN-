import React, { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [resultImage, setResultImage] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(file);
    }
  };

  const handleSubmit = async () => {
    if (!image) {
      alert('Please upload an image first.');
      return;
    }

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await fetch('http://localhost:5000/segment', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResultImage(data.result_image);
    } catch (error) {
      console.error('Error processing image:', error);
    }
  };

  return (
    <div className="App">
      <h1>Segment Anything Model</h1>
      <input type="file" onChange={handleImageUpload} accept="image/*" />
      <button onClick={handleSubmit}>Segment Image</button>

      {image && <img src={URL.createObjectURL(image)} alt="Uploaded" className="preview" />}
      {resultImage && <img src={resultImage} alt="Segmented Result" className="result" />}
    </div>
  );
}

export default App;
