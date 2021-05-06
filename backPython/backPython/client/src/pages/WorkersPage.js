import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Loader } from '../components/Loader';
import { User } from '../components/User';
import { useHttp } from '../hooks/http.hook';
import { getDepsAction } from '../redux/actions/dep.actions';
import { getUsers, sortByEmail, sortByName } from '../redux/actions/user.actions';

export const WorkersPage = () => {
  const token = useSelector((state) => state.login.token)
  const { request, loading } = useHttp();
  const users = useSelector((state) => state.usr.users);
  const deps = useSelector((state) => state.dep.deps);
  const dispatch = useDispatch();

  const getUser = async () => {
    const data = await request('/user', 'GET', null, { Authorization : 'Bearer ' + token });
    if (data.status === 200) {
      dispatch(getUsers(data.body));
    }
  };

  const getDeps = async () => {
    const data = await request('/department', 'GET', null, { Authorization : 'Bearer ' + token });
    if (data.status === 200) {
      dispatch(getDepsAction(data.body));
    }
  };

  useEffect(() => {
    if (!deps && !loading) {
      getDeps();
    }
  }, [deps, getDeps]);

  useEffect(() => {
    if (!users && !loading) {
      getUser();
    }
  }, [users, getUser]);

  if (!users || !deps) {
    return <Loader />;
  }

  for (const user of users) {
    user.dep = [];
    for (const dep of deps) {
      for (const worker of dep.users) {
        if (worker.id === user.id) {
          user.dep.push({
            name: dep.name,
            id: dep.id,
            position: Number(dep.bossId) === Number(user.id) ? 'boss' : 'clerk',
          });
          break;
        }
      }
    }
  }

  return (
    <div className="d-flex flex-row check">
      <table className="table me-5">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Department</th>
            <th scope="col">Date</th>
            <th scope="col">Account</th>
          </tr>
        </thead>
        <tbody>
          {!!users && users.map((user, i) => (
            <User user={user} key={i} numbering={i} />
          ))}
        </tbody>
      </table>
      <div className="dropdown">
        <button className="btn btn-dark dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
          Sorting by :
        </button>
        <ul className="dropdown-menu middle" aria-labelledby="dropdownMenuButton1">
          <li className="middle">
            <button
              className="dropdown-item link__bg"
              onClick={() => dispatch(sortByName())}
            >
              Name
            </button>
          </li>
          <li className="middle">
            <button
              className="dropdown-item link__bg"
              onClick={() => dispatch(sortByEmail())}
            >
              Email
            </button>
          </li>
        </ul>
      </div>
    </div>
  );
};
