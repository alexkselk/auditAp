
$('.custom-file-input').on('change',function(){
  let fileName = $(this).val().split('\\').pop();/*убирает из имени путь до файла*/
  $(this).next('.custom-file-label').addClass("selected").html(fileName);
})













/*function upload(event){
alert(id_title)
$.ajax(
{
type:"POST",
url:"upload_file",
data:{file: id_title}
});

$.ajax(
{
type: "POST",
url: "~/xlAudit.py",
data: { docParam: id_title, amountParam: amount}
})
}*/
