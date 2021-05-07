import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';
import { useHttp } from '../hooks/http.hook';
import { useMessage } from '../hooks/message.hook';
import { delDepsAction, getDepsAction } from '../redux/actions/dep.actions';
import { Loader } from './Loader';

export const Worker = ({
  user, numbering, bossId, name, length, id,
}) => {
  const { request, loading } = useHttp();
  const history = useHistory();
  const dispatch = useDispatch();
  const message = useMessage();
  const token = useSelector((state) => state.login.token)

  const dismissHandler = async () => {
    if (user.id === Number(bossId)) {
      if (length === 1) {
        const data = await request(`/department/${id}`, 'DELETE', { userId: bossId }, { Authorization : 'Bearer ' + token });

        if (data.status === 200) {
          message(data.body.message);
          dispatch(delDepsAction());
          history.push('/departments');
          return;
        }
        
        if(data.status === 400) {
          message(data.body.message) 

        }
      }
      message("You can't dissmiss department boss");
    } else {
      const data = await request(`/department/${id}/workers/${user.id}`, 'DELETE', null, { Authorization : 'Bearer ' + token });

      if (data.status === 200) {
        message(data.body.message);
        dispatch(getDepsAction());
      }
    }
  };

  if (loading) {
    return <Loader />;
  }

  return (
    <tr className="link__bg">
      <th scope="row">{numbering + 1}</th>
      <td>{user.name}</td>
      <td>{user.email}</td>
      <td>{bossId === Number(user.id) ? 'boss' : 'clerk'}</td>
      <td>{name}</td>
      <td>
        <button
          type="button"
          className="btn btn-dark"
          onClick={dismissHandler}
        >
          Yes
        </button>
      </td>
    </tr>
  );
};
