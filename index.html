<html>
<head>
<title>Phraser</title>
</head>
<body>
<?php
global $n;
global $pl;
function display(){
	//CONNECT TO MYSQL
	mysql_connect("localhost", "root", "") or die(mysql_error());
	mysql_select_db("phraser") or die(mysql_error());
	//GET DATA FROM TABLE
	$noun = mysql_query("SELECT word from word where type = 'noun' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$plural = mysql_query("select word from word where type = 'Plural' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$adjective = mysql_query("select word from word where type = 'adjective' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$verb = mysql_query("select word from word where word not like '%ed' and word not like '%ing' and type = 'verb_transitive' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$verbing = mysql_query("select word from word where word like '%ing' and type = 'verb_transitive' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$verbs = mysql_query("select word from word where word like '%e' and type = 'verb_transitive' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	$verbed = mysql_query("select word from word where word like '%ed' and type = 'verb_transitive' and char_length(word) < 7 order by rand() limit 1;") or die(mysql_error());
	$noun2 = mysql_query("SELECT word from word where type = 'noun' and char_length(word) < 7 order by rand() limit 1;") or die (mysql_error());
	
	
	$sentenceid = mysql_query("select id from sentence order by rand() limit 1;") or die(mysql_error());
	$senid = mysql_fetch_array($sentenceid);
	$senid = $senid['id'];
	
	$sentence = mysql_query("Select sentence from sentence where id = '$senid'") or die(mysql_error());
	$sen = mysql_fetch_array($sentence);
	$sen = $sen['sentence'];
	
	global $n;
	global $pl;
	
	$n = mysql_fetch_array($noun);
	$n2 = mysql_fetch_array($noun2);
	$pl = mysql_fetch_array($plural);
	$adj = mysql_fetch_array($adjective);
	$vb = mysql_fetch_array($verb);
	$ving = mysql_fetch_array($verbing);
	$vs = mysql_fetch_array($verbs);
	$vd = mysql_fetch_array($verbed);
	$n = $n['word'];
	$n2 = $n2['word'];
	$pl = $pl['word'];
	$adj = $adj['word'];
	$vb = $vb['word'];
	$ving = $ving['word'];
	$vs = $vs['word'];
	$vd = $vd['word'];
	
	$sen = str_replace("#noun2",$n2,$sen);
	$sen = str_replace("#noun",$n,$sen);
	$sen = str_replace("#plural",$pl,$sen);
	$sen = str_replace("#adjective",$adj,$sen);
	$sen = str_replace("#verbb",$vb,$sen);
	$sen = str_replace("#verbing",$ving,$sen);
	$sen = str_replace("#verbs",$vs."S",$sen);
	$sen = str_replace("#verbed",$vd, $sen);
	echo $sen;

if(isset($_POST['b1']))
{
echo " <br>You rated: 1";
	$rating = 1;
}
else if(isset($_POST['b2']))
{
echo " <br>You rated: 2";
	$rating = 2;
}
else if(isset($_POST['b3']))
{
echo " <br>You rated: 3";
	$rating = 3;
}
else if(isset($_POST['b4']))
{
echo " <br>You rated: 4";
	$rating = 4;
}
else if(isset($_POST['b5']))
{
echo " <br>You rated: 5";
	$rating = 5;
}
else if(isset($_POST['b6']))
{
echo " <br>You rated: 6";
	$rating = 6;
}
else if(isset($_POST['b7']))
{
echo " <br>You rated: 7";
	$rating = 7;
}
else if(isset($_POST['b8']))
{
echo " <br>You rated: 8";
	$rating = 8;
}
else if(isset($_POST['b9']))
{
echo " <br>You rated: 9";
	$rating = 9;
}
else if(isset($_POST['b10']))
{
echo " <br>You rated: 10";
	$rating = 10;
}
}
display();
function call($rating){
	$dbhost = 'localhost:8080';
	$dbuser = 'root';
	$dbpass = '';
	$database = 'phraser';
	$conn = mysql_connect("localhost", "root", "","phraser");
	mysql_select_db("phraser");
	if(! $conn )
	{
		die('Could not connect: ' . mysql_error());
	}
		global $n;
		global $pl;
		$n = $n['word'];
		$pl = $pl['word'];
		
		echo "<br>$n";
		echo "<br>nig";
		echo "<br>$pl";
	
		$sql = "update word set total_rating = total_rating + $rating where word = '$n'";
		$sql1 = "update word set times_rated = times_rated + 1 where word = '$n'";
		$retval = mysql_query( $sql, $conn );
		$retval1 = mysql_query( $sql1, $conn);
		if(! $retval )
		{
			die('Could not enter data: ' . mysql_error());
		}	
		if(! $retval1 )
		{
			die('Could not enter data: ' . mysql_error());
		}	
		echo "<br> Entered Noun successfully\n";
		
		$sql2 = "update word set total_rating = total_rating + $rating where word = '$pl'";
		$sql3 = "update word set times_rated = times_rated + 1 where word = '$pl'";
		$retval = mysql_query( $sql2, $conn );
		$retval1 = mysql_query( $sql3, $conn);
		if(! $retval )
		{
			die('Could not enter data: ' . mysql_error());
		}	
		if(! $retval1 )
		{
			die('Could not enter data: ' . mysql_error());
		}	
		echo "<br> Entered Plural successfully\n";
		mysql_close($conn);
}	
?>

<form method="post" action="<?php $_PHP_SELF ?>">
<table width="400" border="0" cellspacing="1" cellpadding="2">
<tr>
<td width="100"> </td>
<td> </td>
</tr>
<tr>
<td width="100"> </td>
<td>
<input name="b1" type="submit" value="1">
</td>
<td>
<input name="b2" type="submit" value="2">
</td>
<td>
<input name="b3" type="submit" value="3">
</td>
<td>
<input name="b4" type="submit" value="4">
</td>
<td>
<input name="b5" type="submit" value="5">
</td>
<td>
<input name="b6" type="submit" value="6">
</td>
<td>
<input name="b7" type="submit" value="7">
</td>
<td>
<input name="b8" type="submit" value="8">
</td>
<td>
<input name="b9" type="submit" value="9">
</td>
<td>
<input name="b10" type="submit" value="10">
</td>
</tr>
</table>
</form>
</body>
</html>
