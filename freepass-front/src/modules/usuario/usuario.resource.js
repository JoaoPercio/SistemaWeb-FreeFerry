import { get, put, post, remove } from '@/helpers/http';

const BASE_PATH = 'usuarios';
const BASE_PATH2 = 'documentos';
const BASE_PATH3 = 'usuarios2';

export function fetchUsuarios() {
  return get(`${BASE_PATH}`);
}
export function fetchUsuarios2() {
  return get(`${BASE_PATH3}`);
}
export function getUsuario(id) {
  return get(`/${BASE_PATH}/${id}`);
}

export function getDocumento(id) {
  return get(`/${BASE_PATH2}/${id}`);
}

export function updateUsuario(usuario) {
  return put(`/${BASE_PATH}/${usuario.Id}`, usuario);
}

export function createUsuario(usuario) {
  return post(`${BASE_PATH}`, usuario);
}

export function removeUsuario(usuario) {
  return remove(`/${BASE_PATH}/${usuario.Id}`);
}
