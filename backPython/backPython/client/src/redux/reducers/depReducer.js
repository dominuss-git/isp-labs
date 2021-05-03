import { DEPARTAMENTS_DEL, DEPARTAMENTS_GET } from '../types';

const InitialState = {
  deps: null,
};

export const depReducer = (state = InitialState, action) => {
  switch (action.type) {
    case DEPARTAMENTS_GET:
      return { ...state, deps: action.payload };

    case DEPARTAMENTS_DEL:
      return { ...state, deps: null };

    default:
      return state;
  }
};
