import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import { DashboardPage } from './pages/DasboardPage';
import { DepartmentPage } from './pages/DepartmentPage';
import { DepartmentsPage } from './pages/DepatmentsPage';
import { LoginPage } from './pages/LoginPage';
import { RegistrPage } from './pages/RegistrPage';
import { UserPage } from './pages/UserPage';
import { WorkersPage } from './pages/WorkersPage';

export const useRoutes = (isAuthentification) => {
  if (isAuthentification) {
    return (
      <Switch>
        <Route path="/dashboard" exact>
          <DashboardPage />
        </Route>
        <Route path="/departments" exact>
          <DepartmentsPage />
        </Route>
        <Route path="/departments/:id" exact>
          <DepartmentPage />
        </Route>
        <Route path="/workers/:id" exact>
          <UserPage />
        </Route>
        <Route path="/workers" exact>
          <WorkersPage />
        </Route>
        <Redirect to="/dashboard" />
      </Switch>
    );
  }
  return (
    <Switch>
      <Route path="/login" exact>
        <LoginPage />
      </Route>
      <Route path="/registr" exact>
        <RegistrPage />
      </Route>
      <Redirect to="/login" />
    </Switch>
  );
};
