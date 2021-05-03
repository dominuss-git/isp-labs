import { DEPARTAMENTS_GET, DEPARTAMENTS_DEL } from '../types';

export function getDepsAction(deps) {
  return {
    type: DEPARTAMENTS_GET,
    payload: deps,
  };
}

export function delDepsAction() {
  return {
    type: DEPARTAMENTS_DEL,
  };
}
