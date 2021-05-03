import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { Loader } from '../components/Loader';
import { useAuth } from '../hooks/auth.hook';
import { useHttp } from '../hooks/http.hook';
import { useMessage } from '../hooks/message.hook';

export const RegistrPage = () => {
  const message = useMessage();
  const { request } = useHttp();
  const loading = useSelector((state) => state.app.loading);
  const { login } = useAuth();

  const [form, setForm] = useState({
    email: '',
    password: '',
  });

  if (loading) {
    return <Loader />;
  }

  const changeHandler = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const onRegistr = async () => {
    const data = await request('/registr', 'POST', { ...form });
    if (data.status === 400) {
      message(data.body.message);
    } else if (data.status === 200) {
      login(data.body.token, data.body.userId);
    }
  };

  return (
    <form className="mt-5 pt-5 w-30">
      <span className="form-label pb-5 bolder fs-2" id="basic-addon1">Registration</span>
      <div className="input-group mb-3 mt-5">
        <span className="input-group-text" id="basic-addon1">Email</span>
        <input
          type="email"
          className="form-control"
          placeholder="Email"
          name="email"
          aria-label="Email"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
      </div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Skils</span>
        <input
          type="text"
          className="form-control"
          placeholder="Skils"
          name="skils"
          aria-label="Skils"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
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
          placeholder="Name"
          name="name"
          aria-label="Name"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
        <span className="input-group-text" id="basic-addon1">Surname</span>
        <input
          type="text"
          className="form-control"
          placeholder="Surname"
          name="surname"
          aria-label="Surname"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
      </div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Street</span>
        <input
          type="text"
          className="form-control big"
          placeholder="Street"
          name="street"
          aria-label="Street"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
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
          placeholder="Home"
          name="home"
          aria-label="Home"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
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
          placeholder="Flat"
          name="flat"
          aria-label="Flat"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
      </div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Password</span>
        <input
          type="password"
          className="form-control"
          placeholder="Password"
          name="password"
          aria-label="Password"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
        <span className="input-group-text" id="basic-addon1">Confirm</span>
        <input
          type="password"
          className="form-control"
          placeholder="Password"
          name="confirnPassword"
          aria-label="Password"
          aria-describedby="basic-addon1"
          onChange={changeHandler}
        />
      </div>
      <div
        className="btn-group d-flex justify-start w-75"
        role="group"
        aria-label="Basic outlined example"
      >
        <button
          type="button"
          className="btn btn-primary"
          onClick={onRegistr}
        >
          Sign up
        </button>
        <NavLink
          className="btn btn-dark"
          to="/login"
        >
          Sign in
        </NavLink>
      </div>
    </form>
  );
};
