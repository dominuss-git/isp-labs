import React from 'react';
import { useSelector } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import { Alert } from './components/Alert';
import { NavBar } from './components/NavBar';
import { useRoutes } from './routes';

function App() {
  const token = useSelector((state) => state.login.token);
  const isAuthenticated = !!token;
  const routes = useRoutes(isAuthenticated);
  const text = useSelector((state) => state.app.alert);

  return (
    <Router>
      {isAuthenticated && <NavBar /> }
      {text && <Alert text={text} /> }
      <div className="w-100 d-flex justify-content-center align-items-center px-4 py-4 my-4 text-center vertical-center">
        {routes}
      </div>
    </Router>
  );
}

export default App;
