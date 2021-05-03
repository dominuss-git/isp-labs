import React from 'react';

export const Alert = ({ text }) => (
  <div className="alert alert-danger text-center" role="alert">
    {text}
  </div>
);
