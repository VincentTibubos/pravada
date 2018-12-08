new Vue({
  el: '#login',
  delimiters: ['[[', ']]'],
  data: function(){
    return {
    username: '',
    password: '',
    block:true,
    user_msg: null,
    pass_msg: null,
    user_state: null,
    pass_state: null
    }
  },
  methods:{
    login: function(){
      var formdata=new FormData();
      var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value;
      formdata.append('csrfmiddlewaretoken',csrf);
      formdata.append('username',this.username);
      formdata.append('password',this.password);
      axios.defaults.xsrfHeaderName='X-CSRFToken';
      axios.defaults.xsrfCookieName='XCSRF-TOKEN';
      axios({
        method:'POST',
        url: '/login/',
        data:formdata,
        headers:{
          'X-CSRFToken': csrf
        }
      })
      .then(( res)=>{
        this.pass_msg=res.data.p_error;
        this.user_msg=res.data.u_error;
        var error=res.data.error;
        this.user_state=this.user_msg==''?true:false
        this.pass_state=this.pass_msg==''?true:false
        if(!this.pass_msg&&!this.user_msg){
          if(error!=''){
            this.pass_state=this.user_state=false;
            this.pass_msg=error;
          }
          else{
            window.location='/profile/';
          }
        }
        console.log(data);
      })
      .catch(function( error){
      });
    }
  }
})
