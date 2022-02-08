<template>
  <div class="add">
   
    <h1>{{ pagetitle }}</h1>
    <form v-on:submit.prevent="addNewNote" action="" >
        <input  v-model="note_title" type="text" name="title-form"  placeholder="type the title here">
        <br>
        <textarea v-model ="note_description" name="text-form" id="text-form-id"  placeholder="type the description"></textarea>
        <br>
        <button id="submit-button">Submit this note!</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'AddNote',
  data() {
    return {
        pagetitle:"Añade una nota nueva: ",
        note_title: "",
        note_description: "",
        num: 100,
        notes_front:[]

        
    }
  },   
  mounted() {
        this.loadData()
  },

  
  methods:{
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes')
      this.notes_front= await response.json()
    },
    addNewNote(){
        if (this.note_title != "" && this.note_description != ""){
            this.num +=1 
            
            let newNote = {"id": "note-" + this.num, "title": this.note_title, "text": this.note_description}
            
            //this.notes_front.push(newNote)


            const settings={
                method:'POST',
                body:JSON.stringify(newNote),
                headers:{
                    'Content-Type': 'application/json'
                }

            }
            fetch('http://localhost:5000/api/notes', settings) // <-- comprobar ruta

            console.log("post a la BD hacia el endpoint - 5000/api/notes POST - ")
            console.log("obj mandado al back " + JSON.stringify(newNote))
        }
              
        else{
            alert("Error! Fill in all the fields, please")
        }

        this.note_title = ""
        this.note_description= ""
        

        }
    }
}
</script>

<style >
h1 {
  font-style: italic;
  
}

</style>
