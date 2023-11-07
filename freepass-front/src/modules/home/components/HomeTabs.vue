<template>
  <el-tabs v-model="tabActive" @tab-click="fetch">
    <el-tab-pane label="Usuários aguardando aprovação de passes" name="usuarios2">
      <div v-if="usuarioList2.length">
        <div
          v-for="usuario in usuarioList2"
          :key="usuario.id"
          class="mb--xl">
          <biblioteca-usuario-card :usuario="usuario" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem Usuários )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="usuários aguardando aprovação de cadastro" name="usuarios">
      <div v-if="usuarioList.length">
        <div
          v-for="usuario in usuarioList"
          :key="usuario.id"
          class="mb--xl">
          <biblioteca-usuario-card :usuario="usuario" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem usuários )</biblioteca-p>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import { fetchUsuarios, fetchUsuarios2 } from '@/modules/usuario/usuario.service';

import BibliotecaUsuarioCard from '@/modules/usuario/components/UsuarioCard.vue';

export default {
  name: 'BibliotecaHomeTabs',
  components: {
    BibliotecaUsuarioCard,
  },
  data() {
    return {
      tabActive: 'usuarios2',
      usuarioList: [],
      usuarioList2: [],
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      if (this.tabActive === 'usuarios2') {
        this.fetchUsuarios2();
      } else if (this.tabActive === 'usuarios') {
        this.fetchUsuarios();
      }
    },
    fetchUsuarios() {
      fetchUsuarios()
        .then(({ data }) => {
          this.usuarioList = data.data;
        })
        .catch(() => {
          this.usuarioList = [];
        });
    },
    fetchUsuarios2() {
      fetchUsuarios2()
        .then(({ data }) => {
          this.usuarioList2 = data.data;
        })
        .catch(() => {
          this.usuarioList2 = [];
        });
    },
  },
};
</script>
