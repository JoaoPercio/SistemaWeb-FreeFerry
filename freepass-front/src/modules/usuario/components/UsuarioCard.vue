<template>
  <biblioteca-row>
    <biblioteca-col
      :sm="4"
      :md="2">
      <biblioteca-icon
        class="mt-2"
        size="xl"
        icon="person" />
    </biblioteca-col>
    <biblioteca-col
      :sm="20"
      :md="22">
      <biblioteca-header v-truncate size="sm">
        <biblioteca-usuario-link :id="usuario.Id">{{ usuario.Nome_Completo }}</biblioteca-usuario-link>
      </biblioteca-header>
      <biblioteca-p
        v-truncate="2"
        color="regular">
        {{ usuario.Email }}
      </biblioteca-p>
      <biblioteca-p
        v-truncate="2"
        color="regular">
        data de registro: {{ usuario.Data_Cadastro }}
      </biblioteca-p>
    </biblioteca-col>
  </biblioteca-row>
</template>

<script>
import BibliotecaUsuarioLink from '@/modules/usuario/components/UsuarioLink.vue';

export default {
  name: 'UsuarioCard',
  components: {
    BibliotecaUsuarioLink,
  },
  props: {
    usuario: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
    };
  },
  computed: {
  },
};
</script>
