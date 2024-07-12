import React, { createContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('authToken');
    setIsAuthenticated(!!token);
  }, []);

  const login = (token) => {
    localStorage.setItem('authToken', token);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
