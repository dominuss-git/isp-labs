import React from 'react';
import { Worker } from './Worker';

export const DepartmentInfo = ({ data }) => {
  let bossEmail = '';

  for (const user of data.users) {
    if (data.bossId === String(user.id)) {
      bossEmail = user.email;
      break;
    }
  }

  return (
    <div className="container-fluid">
      <div className="row">
        <label htmlFor="staticEmail" className="col-sm-3 col-form-label fw-bold">Boss email</label>
        <div className="col-sm-4">
          <div type="text" readOnly className="form-control-plaintext" id="staticEmail">{bossEmail}</div>
        </div>
      </div>
      <div className="mb-2 row">
        <label htmlFor="type" className="col-sm-3 col-form-label fw-bold">Type</label>
        <div className="col-sm-4">
          <div type="text" readOnly className="form-control-plaintext" id="type">{data.type}</div>
        </div>
      </div>
      <div className="mb-2 row">
        <label htmlFor="name" className="col-sm-3 col-form-label fw-bold">Name</label>
        <div className="col-sm-4">
          <div type="text" readOnly className="form-control-plaintext" id="name">{data.name}</div>
        </div>
      </div>
      <div className="mb-2 row">
        <label htmlFor="name" className="col-sm-3 col-form-label fw-bold">Last Update</label>
        <div className="col-sm-4">
          <div type="text" readOnly className="form-control-plaintext" id="name">{data.update}</div>
        </div>
      </div>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Position</th>
            <th scope="col">Department</th>
            <th scope="col">Dismiss</th>
          </tr>
        </thead>
        <tbody>

          {!!data.users && data.users.map((user, i) => (
            <Worker key={i} numbering={i} user={user} bossId={data.bossId} name={data.name} length={data.users.length} id={data.id} />
          ))}

        </tbody>
      </table>
    </div>
  );
};
