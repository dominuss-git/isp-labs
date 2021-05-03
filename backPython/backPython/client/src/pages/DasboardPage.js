import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Department } from '../components/Department';
import { Loader } from '../components/Loader';
import { User } from '../components/User';
import { useHttp } from '../hooks/http.hook';
import { getDepsAction } from '../redux/actions/dep.actions';
import { getUsers } from '../redux/actions/user.actions';

export const DashboardPage = () => {
  const { request, loading } = useHttp();
  const users = useSelector((state) => state.usr.users);
  const deps = useSelector((state) => state.dep.deps);
  const dispatch = useDispatch();

  const getUser = async () => {
    const data = await request('/user/', 'GET');
    if (data.status === 200) {
      dispatch(getUsers(data.body));
    }
  };

  const getDeps = async () => {
    const data = await request('/department', 'GET');
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
  deps.sort((a, b) => (a.users.length < b.users.length ? 1 : -1));
  users.sort((a, b) => (a.id < b.id ? 1 : -1));

  return (
    <div className="d-flex flex-row check">
      <ol className="list-group list-group-numbered me-5">
        <p className="text-start fw-bold">Top 5 biggest departments</p>
        {!!deps && deps.map((val, i) => {
          if (i > 4) {
            return;
          }
          return (
            <Department data={val} numbering={i} key={i} />
          );
        })}
      </ol>
      <div className="d-flex flex-column check__item">
        <p className="text-start fw-bold">New employees</p>
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
            {!!users && users.map((user, i) => {
              if (i > 4) {
                return;
              }
              return (
                <User user={user} key={i} numbering={i} />
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
