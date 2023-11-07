<template>
  <nav class="navbar navbar-expand navbar-light bg-primary border-0 shadow-sm p--md">
    <biblioteca-container size="xxxxl">
      <slot v-if="showBrand" name="brand">
        <a class="navbar-brand" href="/">
          <img
            alt="Freepass"
            height="36"
            src="@/assets/images/logo.png">
        </a>
      </slot>
      <div>
        <ul
          v-if="$slots.right"
          class="navbar-nav ms-auto">
          <slot name="right" />
        </ul>
      </div>
    </biblioteca-container>
  </nav>
</template>
<script>

export default {
  name: 'BibliotecaNavbar',
  props: {
    showBrand: {
      type: Boolean,
      default: true,
    },
  },
};
</script>
<style>
nav{
  background-color: rgb(4, 46, 163) !important;
}
</style>
