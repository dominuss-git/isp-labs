import {
  SORT_EMAIL, SORT_NAME, USER_DEL, USER_GET,
} from '../types';

const InitialState = {
  users: null,
};

export const userReducer = (state = InitialState, action) => {
  switch (action.type) {
    case USER_GET:
      return { ...state, users: action.payload };

    case USER_DEL:
      return { ...state, users: null };

    case SORT_NAME:
      return {
        ...state,
        users: [...state.users].sort((a, b) => (a.name > b.name ? 1 : -1)),
      };

    case SORT_EMAIL:
      return {
        ...state,
        users: [...state.users].sort((a, b) => (a.email > b.email ? 1 : -1)),
      };

    default:
      return state;
  }
};
