import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../hooks/auth.hook';

export const NavBar = () => {
  const auth = useAuth();
  const logoutHandler = (event) => {
    event.preventDefault();
    auth.logout();
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">Own company</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <NavLink className="nav-link" to="/dashboard">Dashboard</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/departments">Departments</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/workers">Workers</NavLink>
            </li>
            <li className="nav-item">
              <a className="nav-link end-0" onClick={logoutHandler}>Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
