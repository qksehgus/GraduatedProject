<%@ page language="java" contentType="text/html; charset=EUC-KR"
	pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<link rel="stylesheet" href="css/base.css">
</head>
<body>
	<form action="test2.jsp" method="post">
		<table>



		</table>
		<table class="templateTable2" bordercolor="#505050" cellspacing="0"
			cellpadding="5" width="90%" align="center" border="1">
			<tbody>
				<tr>
					<th class="loc_th_item">탑바
					<td class="loc_td_radio_item"><input type="radio"
						name="check_info" value="top_bar">top_bar
					</th>
				</tr>
				<tr>
					<th class="loc_th_item">탑LMF</th>
					<td class="loc_td_radio_item"><input type="radio"
						name="check_info" value="top_left">top_left <input
						type="radio" name="check_info" value="top_center">top_center
						<input type="radio" name="check_info" value="top_right">top_right</td>
				</tr>
				<tr>
					<th class="loc_th_item">third</th>
					<td class="loc_td_radio_item"><input type="radio"
						name="check_info" value="upper_third">upper_third <input
						type="radio" name="check_info" value="middle_third">middle_third
						<input type="radio" name="check_info" value="lower_third">lower_third</td>
				</tr>
				<tr>
					<th class="loc_th_item">bottomLMF</th>
					<td class="loc_td_radio_item"><input type="radio"
						name="check_info" value="bottom_left">bottom_left <input
						type="radio" name="check_info" value="bottom_center">bottom_center
						<input type="radio" name="check_info" value="bottom_right">bottom_right</td>
				<tr class="loc_th_item">
					<th>바텀 바</th>
					<td class="loc_td_radio_item"><input type="radio"
						name="check_info" value="bottom_bar">bottom_bar</td>
				</tr>
			</tbody>
		</table>
		<input type="submit" value="전송">
	</form>
</body>
</html>