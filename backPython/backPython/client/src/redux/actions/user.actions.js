import {
  SORT_EMAIL, SORT_NAME, USER_DEL, USER_GET,
} from '../types';

export function getUsers(data) {
  return {
    type: USER_GET,
    payload: data,
  };
}

export function delUser() {
  return {
    type: USER_DEL,
  };
}

export function sortByName() {
  return {
    type: SORT_NAME,
  };
}

export function sortByEmail() {
  return {
    type: SORT_EMAIL,
  };
}
