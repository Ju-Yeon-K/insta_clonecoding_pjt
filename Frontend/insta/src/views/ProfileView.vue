<template>
  <div>
    <div class="container text-start">
      <div class="row">
        <div class="col-12" >          
          
          <h3 v-if="is_me">{{profile.user}} 님의 프로필</h3> <!-- {% if request.user.id == profile.user_id %}   -->
          <h3 v-else>내 프로필</h3>
        </div>
      </div>
    </div>

<!-- <div class="container text-center">
      <div class="row">
        <div class="col-2" >
          {% if profile.image_file %}
            <img src="{{ profile.image_file.url }}" class="card-img-top imgbox mt-2">
          {% else %}
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232" class="card-img-top imgbox mt-2">
          
            {% endif %}
        </div>
        <div class="col-4">
        </div>
        <div class="col-2 mt-4">
          {{profile.user.post_set.count}} <br>
          게시물
        </div>
        <div class="col-2 mt-4">
          {{profile.user.followers.count}} <br>
          팔로워
        </div>
        <div class="col-2 mt-4">
          {{profile.user.followings.count}} <br>
          팔로잉
        </div>
      </div>
    </div>
    
    <div class="row m-2">

    {% if profile.nickname %} {{profile.nickname}} {% else %}등록된 닉네임이 없어욤 ㅜㅜ
    {% endif %}
  </div>
  <div class="row mx-2">
      {% if profile.introduction %} {{profile.introduction}}{% else %}등록된 자기 소개글이 없어욤 ㅜㅜ 
    {% endif %}
  </div>
  <div class="row">
    <div class="col-2 mt-2">
      {% if request.user != profile.user %}
      <form action="{% url 'accounts:follow' profile.user.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in profile.user.followers.all %}
          <button type="submit" class="btn btn-secondary">언팔로우</button>
        {% else %}
          <button type="submit" class="btn btn-secondary">팔로우</button>
        {% endif %}
  
        </form>
      {% endif %}
    
    </div>
  </div>
    {% if request.user.id == profile.user_id %}
    <br><br>
    <a href="{% url 'accounts:logout' %}">
      <button type="submit" class="btn btn-secondary">Log out</button>
    </a>
    <a href="{% url 'accounts:profile_update' %}">
      <button type="submit" class="btn btn-warning">Profile Edit</button>
    </a>
    <a href="{% url 'accounts:password' %}">
      <button type="submit" class="btn btn-primary">Change Password</button>
    </a>
    <a href="{% url 'accounts:delete' %}">
      <button type="submit" class="btn btn-danger">Delete Account</button>
    </a>
    {% endif %}
    <hr>
  </div> -->
  </div>
</template>

<script>
export default {
    name:'ProfileView',
    data() {
    return {
      user_pk:this.$route.params.userpk,
      is_me:false
    }
  },

}
</script>

<style>

</style>