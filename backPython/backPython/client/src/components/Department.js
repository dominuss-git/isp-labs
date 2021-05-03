import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import { useHttp } from '../hooks/http.hook';
import { useMessage } from '../hooks/message.hook';
import { delDepsAction } from '../redux/actions/dep.actions';

export const Department = ({ data }) => {
  const message = useMessage();
  const history = useHistory();

  let date = new Date(data.date);
  // console.log(data)
  date = `${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}`;

  let boss = null;
  const dispatch = useDispatch();
  const id = useSelector((state) => state.login.id);
  const dep = `/departments/${data.id}`;
  const { request } = useHttp();

  data.users.map((val, i) => {
    if (val.id === Number(data.bossId)) {
      boss = val;
    }
  });

  const deleteHandler = async () => {
    const isDeleted = await request(`/department/${data.id}`, 'DELETE', { userId: String(id) });
    if (isDeleted.status === 400) {
      message(isDeleted.body.message);
      history.push('/departments');
    } else if (isDeleted.status === 200) {
      message(isDeleted.body.message);
      history.push('/departments');
      dispatch(delDepsAction());
    }
  };

  return (
    <NavLink to={dep} className="link">
      <li className="list-group-item d-flex justify-content-between align-items-start link__bg">
        <div className="ms-2 me-auto">
          <div className="fw-bold">{data.name}</div>
          <div className="fw-bold">
            Type : 
            {' '}
            {data.type}
          </div>
          <div className="fw-bold">
            Boss :
            {' '}
            {boss.email}
          </div>
          <div className="fw-bold">
            Last Update :
            {' '}
            {data.update}
          </div>
        </div>
        <div className="fw-bold d-flex flex-column">
          {date}
&#8195;
          <div className="col-auto d-flex justify-content-end">
            <button
              type="submit"
              className="btn btn-dark mb-3"
              onClick={deleteHandler}
            >
              Delete
            </button>
          </div>
        </div>
        <span className="badge bg-dark rounded-pill">{data.users.length}</span>
      </li>
    </NavLink>
  );
};
