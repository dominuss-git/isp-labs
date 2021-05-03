import React from 'react';
import { NavLink } from 'react-router-dom';

export const User = ({ user, numbering }) => {
  const workerId = `/workers/${user.id}`;
  let date = new Date(user.date);
  date = `${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}`;

  return (
    <tr className="link__bg">
      <th scope="row">{numbering + 1}</th>
      <td>{user.name}</td>
      <td>{user.email}</td>
      <td>
        {user.dep.length >= 2 && (
        <div className="dropdown">
          <a className="btn btn-dark dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
            Departments
          </a>
          <ul className="dropdown-menu" aria-labelledby="dropdownMenuLink">
            {user.dep.map((pos, i) => (
              <li key={i}>
                <NavLink to={`/departments/${pos.id}`} className="dropdown-item link link__bg">
                  {pos.name}
                  {' '}
                  :
                  {' '}
                  {pos.position}
                </NavLink>
              </li>
            ))}
          </ul>
        </div>
        ) }
        {user.dep.length === 1
        && (
        <NavLink to={`/departments/${user.dep[0].id}`} className="dropdown-item link link__bg">
          {user.dep[0].name}
          {' '}
          :
          {' '}
          {user.dep[0].position}
        </NavLink>
        )}
      </td>
      <td>
        {date}
      </td>
      <td>
        <NavLink
          to={workerId}
          type="button"
          className="btn btn-dark"
        >
          Check
        </NavLink>
      </td>
    </tr>
  );
};
