$(function(){	
	$('#addUserToList').on('click', addUser);
	$('#submit_group').on('click', createGroup);
});

var users = [];
function createGroup() {
	var group_name = $('#GroupName_id').val();
	var usersToAdd = JSON.stringify(users);
	if (group_name =="")
	{
		alert("Please enter group name");
		return;
	}
	
	$.ajax({
		url:'/newGroup',
		type:'GET',
		dataType:'json',
			data:{GroupName_id:group_name, Users:usersToAdd},
			success:function(data, status, xhr) {
				if (data.status == 'exists')
				{
					alert('Exist!');
					return;
				}
				else
				{
					if (data == null)
						return;
					var dom = document.getElementById('allGroups');
					var gid = data[1];
					var names = data[0];
					$( "#allGroups" ).empty();
					for (i = 0; i < data.length; ++i)
						dom.insertAdjacentHTML('beforeend','<p><a href="listPage?gid=' + names[i][0] + '">' + names[i][1] + '<br/> </a></p>');
					$("#GroupName_id" ).val("");
					if (gid != null)
						window.location.replace("listPage?gid="+gid);
					return;
				}
			},
			error:function(xhr, status, error) {
				alert(xhr);
				console.error(xhr, status, error);
			}			
		});							
	}
	
function addUser(){
	var exist = 0;
	var user_name = $('#combobox').val();
	var i;
	for (i=0; i<users.length; i++)
		if (user_name == users[i])
		{
			alert("User already exist");
			exist = 1;
		}
	if (exist == 0)
	{
		//$('#users_list').val($('#users_list').val()+addUser+'\n');
		users.push(user_name);
		var dom = document.getElementById('users_list');
		i = users.length-1;
		dom.insertAdjacentHTML('beforeend','<td>'+ users[i] + '</td>'
			+'<td><button onclick=deleteFromList('+i+')>delete</button></td></p>');
	}
}

function deleteFromList(index) {
	users.splice(index,1);
	var dom = document.getElementById('users_list');
	$("#users_list").empty();
	dom.insertAdjacentHTML('beforeend','<col width="300px" /><col width="30px" /><tr></tr>');
	for (i = 0; i < users.length; ++i)
	{
		dom.insertAdjacentHTML('beforeend','<td>'+ users[i] + '</td>'
			+'<td><button onclick=deleteFromList('+i+')>delete</button></td></p>');
	}
}