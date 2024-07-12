import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import { AuthContext } from '../context/AuthContext';

const Signup = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');
  const [message, setMessage] = useState('');
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/signup/', { username, email, password1, password2 });
      login(response.data.token); // assuming token is returned
      setMessage(response.data.message);
      navigate('/');
    } catch (error) {
      setMessage(error.response.data.errors);
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
        <input type="password" value={password1} onChange={(e) => setPassword1(e.target.value)} placeholder="Password" required />
        <input type="password" value={password2} onChange={(e) => setPassword2(e.target.value)} placeholder="Confirm Password" required />
        <button type="submit">Signup</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Signup;
