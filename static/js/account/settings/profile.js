new Vue({
  el: '#profile',
  delimiters: ['[[', ']]'],
  data: function(){
    return {
      file:null,
      firstName:'',
      lastName:'',
      email:'',
      bio:'',
      imageSrc:'',
    }
  },
  computed: {
    firstNameState () {
      if(this.firstName=='')
        return null;
      return this.firstName.length > 4 ? true : false
    },
    lastNameState () {
      if(this.lastName=='')
        return null;
      return this.lastName.length > 4 ? true : false
    },
    emailState () {
      if(this.email=='')
        return null;
      return this.email.length > 4 ? true : false
    },
    bioState () {
      if(this.bio=='')
        return null;
      return this.bio.length > 19 ? true : false
    },
  },
  methods:{
    previewImage(event){
      var input = event.target;
      if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = (e) => {
              this.imageSrc = e.target.result;
          }
          reader.readAsDataURL(input.files[0]);
      }
    },
  },
  mounted:function(){
    axios({
      method:'GET',
      url: '/getuserdata'
    })
    .then( (res)=>{
      this.firstName=res.data.first_name;
      this.lastName=res.data.last_name;
      this.email=res.data.email;
    })
    .catch(function( error){
    });
  }
})
