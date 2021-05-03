import { LOGIN, LOGOUT } from '../types';

const InitialState = {
  id: null,
  token: null,
  isAdmin: false,
};

export const loginReducer = (state = InitialState, action) => {
  switch (action.type) {
    case LOGIN:
      return { ...state, id: action.payload.id, token: action.payload.token };

    case LOGOUT:
      return { ...state, id: null, token: null };

    default:
      return state;
  }
};
