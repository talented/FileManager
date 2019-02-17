<template>
  <!-- <div class="modal">
	<div class="modal-window">
	  <p>Êtes-vous certain de vouloir supprimer l'utilisateur <strong>{{ user.name }}</strong> ?</p>
	  <div class="actions">
		 <button class="cancel" @click="onCancel">Annuler</button>
		 <button class="confirm" @click="onConfirm">Confirmer</button>
	  </div>
	</div>
 </div> -->
  <div>
   <b-btn v-b-modal.modal1>Launch demo modal</b-btn>

   <!-- Modal Component -->
   <b-modal id="modal1" title="Bootstrap-Vue">
     <p class="my-4">Hello from modal!</p>
   </b-modal>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css">
</style>
