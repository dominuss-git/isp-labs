import React, { useCallback, useEffect, useState } from 'react';
import { useSelector } from 'react-redux'
import { useHistory } from 'react-router';
import { Loader } from '../components/Loader';
import { useHttp } from '../hooks/http.hook';

export const UserPage = () => {
  const token = useSelector((state) => state.login.token);
  const history = useHistory();
  const id = (history.location.pathname.split('/'))[2];
  const { request, loading } = useHttp();
  const [user, setUser] = useState(undefined);
  const [date, setDate] = useState()

  const getUser = async () => {
    console.log("hi")
    const data = await request(`/user/${id}/data`, 'GET',null, { Authorization : 'Bearer ' + token });
    console.log(data)
    if (data.status === 200) {
      setUser(data.body);
      const date_f = new Date(data.body.date);
      setDate(`${date_f.getDate()}.${date_f.getMonth() + 1}.${date_f.getFullYear()}`);
    }
  };

  useEffect(useCallback(() => {
    if (!user && !loading) {
      getUser();
    }
  }), [user, getUser, setUser, loading]);

  if (!user || loading) {
    return <Loader />;
  }

  return (
    <form className="mt-5 pt-5 w-30">
      <span className="form-label pb-5 bolder fs-2" id="basic-addon1">Information</span>
      <div className="input-group mb-3 mt-5">
        <span className="input-group-text" id="basic-addon1">Email</span>
        <input
          type="email"
          className="form-control"
          placeholder={`${user.email}`}
          name="email"
          aria-label="Email"
          aria-describedby="basic-addon1"
          disabled
        />
        <span className="input-group-text" id="basic-addon1">Date</span>
        <input
          type="text"
          className="form-control"
          placeholder={`${date}`}
          name="date"
          aria-label="Date"
          aria-describedby="basic-addon1"
          disabled
        />
      </div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Skils</span>
        <input
          type="text"
          className="form-control"
          placeholder={`${user.skils}`}
          name="skils"
          aria-label="Skils"
          aria-describedby="basic-addon1"
          disabled
        />
      </div>
      <div className="input-group mb-3">
        <span
          className="input-group-text"
          id="basic-addon1"
        >
          Name
        </span
        >
        <input
          type="text"
          className="form-control"
          placeholder={`${user.name}`}
          name="name"
          aria-label="Name"
          aria-describedby="basic-addon1"
          disabled
        />
        <span className="input-group-text" id="basic-addon1">Surname</span>
        <input
          type="text"
          className="form-control"
          placeholder={`${user.surname}`}
          name="surname"
          aria-label="Surname"
          aria-describedby="basic-addon1"
          disabled
        />
      </div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Street</span>
        <input
          type="text"
          className="form-control big"
          placeholder={`${user.street}`}
          name="street"
          aria-label="Street"
          aria-describedby="basic-addon1"
          disabled
        />
        <span
          className="input-group-text"
          id="basic-addon1"
        >
          Home
        </span>
        <input
          type="number"
          className="form-control small"
          placeholder={`${user.home}`}
          name="home"
          aria-label="Home"
          aria-describedby="basic-addon1"
          disabled
        />
        <span
          className="input-group-text"
          id="basic-addon1"
        >
          Flat
        </span>
        <input
          type="number"
          className="form-control small"
          placeholder={`${user.flat}`}
          name="flat"
          aria-label="Flat"
          aria-describedby="basic-addon1"
          disabled
        />
      </div>
    </form>
  );
};
