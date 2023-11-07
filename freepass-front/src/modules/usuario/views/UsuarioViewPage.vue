<template>
  <biblioteca-single-content-layout container-size="lg">
    <template v-if="usuario" #content>
      <div v-if="mostrarMensagem" class="success-message">
        Usuário aprovado com sucesso!
      </div>
      <div v-if="mostrarMensagem2" class="danger-message">
        Usuário negado com sucesso!
      </div>
      <biblioteca-row class="d-flex align-items-center">
        <biblioteca-col>
          <biblioteca-header>
            Informações do Usuário
          </biblioteca-header>
        </biblioteca-col>
      </biblioteca-row>
      <biblioteca-row>
        <biblioteca-col>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong> Nome completo: </strong> {{ usuario.Nome_Completo }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>E-mail: </strong>{{ usuario.Email }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>cpf: </strong>{{ usuario.Cpf }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>telefone: </strong>{{ usuario.Telefone }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>Categoria: </strong>{{ exibirCategoria }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>Motociclista: </strong>{{ exibirMotociclista }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--large">
            <strong>Endereço: </strong>
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>cep: </strong>{{ usuario.endereco.Cep }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>Estado: </strong>{{ usuario.endereco.Estado }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>cidade: </strong>{{ usuario.endereco.Cidade }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>bairro: </strong>{{ usuario.endereco.Bairro }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>logradouro: </strong>{{ usuario.endereco.Logradouro }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--medium">
            <strong>complemento: </strong>{{ usuario.endereco.Complemento }}
          </biblioteca-p>
          <biblioteca-p class="biblioteca-u-text--large">
            <strong>Documentos: </strong>
          </biblioteca-p>
          <div v-if="documentos.length">
            <div
              v-for="documento in documentos"
              :key="documento.id">
              <biblioteca-p class="biblioteca-u-text--medium"><a :href="documento.Url"> Nome documento: {{ documento.Nome }}  link: {{ documento.Url }} </a></biblioteca-p>
            </div>
          </div>
          <div v-if="imagemAmpliada" class="imagem-ampliada-container">
            <img
              :src="imagemAmpliada.url"
              class="imagem-ampliada"
              alt="Imagem Ampliada" />
            <button class="fechar-imagem-ampliada" @click="fecharImagemAmpliada">X</button>
          </div>
        </biblioteca-col>
      </biblioteca-row>
      <div class="button-container">
        <button id="btn" type="button" class="btn btn-success" @click="saveUsuario()"> Aprovar </button>
        <button type="button" class="btn btn-danger" @click="onDeleteUsuario()"> Negar </button>
      </div>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import { USUARIO_ERRORS } from '@/modules/usuario/usuario.constants';
// eslint-disable-next-line import/no-cycle
import { goToUsuarioNotFound } from '@/modules/usuario/usuario.routes';
import { toastError } from '@/services/toastService';
import { saveUsuario, getUsuario, removeUsuario, getDocumento } from '@/modules/usuario/usuario.service';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'BibliotecaUsuarioViewPage',
  components: {
    BibliotecaSingleContentLayout,
  },
  data() {
    return {
      mostrarMensagem: false,
      mostrarMensagem2: false,
      imagemAmpliada: null,
      usuario: null,
      documentos: [],
    };
  },
  computed: {
    id() {
      return this.$route.params?.id;
    },
    exibirCategoria() {
      return this.usuario.Passe_Categoria ? 'estudante' : 'trabalhador';
    },
    exibirMotociclista() {
      return this.usuario.Motociclista ? 'sim' : 'não';
    },
  },
  mounted() {
    this.fetch();
    this.fetch2();
  },
  methods: {
    fetch() {
      getUsuario(this.id)
        .then(data => {
          this.usuario = data.data;
        })
        .catch(err => {
          this.usuario = null;
          if (err) {
            goToUsuarioNotFound(this.$router);
          } else if ((err.response.data.errors === USUARIO_ERRORS[err.response.status] && err.response.status === 404)) {
            goToUsuarioNotFound(this.$router);
          } else {
            toastError('Erro ao buscar o usuário');
          }
        });
    },
    fetch2() {
      getDocumento(this.id)
        .then(({ data }) => {
          this.documentos = data.data;
          console.log(this.documentos.length);
        })
        .catch(() => {
          this.documentos = [];
        });
    },
    saveUsuario() {
      saveUsuario(this.usuario)
        .then(() => {
          this.mostrarMensagem = true;
          setTimeout(() => {
            this.mostrarMensagem = false;
            this.$router.go(-1);
          }, 1000);
        })
        .catch(() => toastError('Erro ao aprovar o usuário'));
    },
    onDeleteUsuario() {
      removeUsuario(this.usuario)
        .then(() => {
          this.mostrarMensagem2 = true;
          setTimeout(() => {
            this.mostrarMensagem2 = false;
            this.$router.go(-1);
          }, 1000);
        })
        .catch(() => toastError('Não foi possível reprovar o usuário'));
    },
    ampliarImagem(documento) {
      this.imagemAmpliada = documento;
    },
    fecharImagemAmpliada() {
      this.imagemAmpliada = null;
    },
  },
};
</script>
<style>
.success-message {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
  padding: 10px;
  margin-top: 10px;
}
.danger-message{
  background-color: #e98c9c;
  color: #7e0707;
  border: 1px solid #e98c9c;
  padding: 10px;
  margin-top: 10px;
}
.biblioteca-u-text--medium{
  border-bottom: 1px solid rgb(131, 131, 131);
  font-size: 24px !important;
  margin-bottom: 10%;
}
.biblioteca-u-text--large{
  font-size: 30px !important;
}
.image-container {
  display: flex; /* Torna os elementos filhos em flex containers */
}

.image-item {
  margin-right: 10px; /* Adicione algum espaço entre as imagens */
}
#btn {
  margin-right: 50px!important;
}
.aa{
  width: 200px;
  height: 200px;
  transition: transform 0.3s ease-in-out;
  max-width: 100%; /* Define a largura máxima como 100% da coluna */
  height: auto; /* Mantém a proporção da imagem */

}
.button-container{
  margin-top: 8% !important;
}
.imagem-ampliada-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.imagem-ampliada {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(1.5); /* Ajuste a escala conforme necessário */
  z-index: 9999;
  width: auto;
  height: auto;
}
.fechar-imagem-ampliada {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  font-size: 16px;
  color: white;
  cursor: pointer;
  outline: none;
}

.fechar-imagem-ampliada:hover {
  background-color: rgba(255, 255, 255, 0.2);
}
</style>
