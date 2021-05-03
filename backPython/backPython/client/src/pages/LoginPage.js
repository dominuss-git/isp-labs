import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { Loader } from '../components/Loader';
import { useAuth } from '../hooks/auth.hook';
import { useHttp } from '../hooks/http.hook';
import { useMessage } from '../hooks/message.hook';
import { hideLoader, showLoader } from '../redux/actions/app.actions';

export const LoginPage = () => {
  const dispatch = useDispatch();
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

  const onLogin = async () => {
    dispatch(showLoader());
    const data = await request('/login', 'POST', { ...form });
    if (data.status === 400) {
      message(data.body.message);
    } else if (data.status === 200) {
      console.log(data.body)
      login(data.body.token, data.body.userId);
    }
    dispatch(hideLoader());
  };

  return (
    <form className="mt-5 pt-5 w-30">
      <span className="form-label pb-5 bolder fs-2" id="basic-addon1">Authentification</span>
      <div className="input-group mb-3 mt-5">
        <span className="input-group-text" id="basic-addon1">email</span>
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
      </div>
      <div
        className="btn-group d-flex justify-start w-75"
        role="group"
        aria-label="Basic outlined example"
      >
        <button
          type="button"
          className="btn btn-primary"
          onClick={onLogin}
        >
          Sign in
        </button>
        <NavLink
          className="btn btn-dark"
          to="/registr"
        >
          Sign up
        </NavLink>
      </div>
    </form>
  );
};
