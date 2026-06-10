<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/oJ8uaN2jOSHKH0dm51QfikTvaGTcx9JKLUui1bicbBcQ95PjtsD8EKk2BYEE2bdI1IhrDEY1OC1AtiPoayhrzkfxDatIgIrfM_6AvLq5wXkArwqB6TXGbffFODyABVWJ6ZdARQcK_lLMSe1YFfO4d98pM62Ig6STcM8igJ8S1p8MzOR2uFGq_FMkt4ScbKPFnjRlySGFUR2CUZDs4CuqHf0Hi9Ifl7eSjMh3U7HkxRyFVzXCkSVQ9QCw1Nst8ZgDOyImZPafEf-FAaQ5pCjjsDa2xjcDl7PX6Eseq8s_ptPegEkZStdfkWmbU7Xjg4g1k7AHG4rWGV6VcqKrtUzx9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تفعيل الدفاعات الجوية بالتزامن مع دوي انفجارات في مناطق شرق بندر عباس</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/78229" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
مسؤول أمني إسرائيلي:
اسرائيل لم تشارك في الضربات على إيران حتى الآن.</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/78228" target="_blank">📅 01:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدر مطلع: كل مايشاع حول استهداف منشأت الطاقة في عسلوية غير صحيحة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78227" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78226" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78225" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله أكبر  القوات المسلحة الإيرانية تستهدف القوات المعادية بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78224" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار في جزيرة هنكام بجنوب إيران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78223" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوي انفجار في كنگان بمحافظة بوشهر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78222" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بيان بعد قليل لمقر خاتم الانبياء المركزي</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78221" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عدوان جديد على بندر عباس في هذه الاثناء</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78220" target="_blank">📅 01:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">أنباء عن دوي انفجارين في بندرعباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78219" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مسؤولين أمريكيين: نتوقع ردا إيرانيا قد يستهدف القواعد الأمريكية كما حدث ليلة الثلاثاء</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78218" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd0efe8be.mp4?token=jRdkefQYu1kCXEEzh_nKN92GRrZSFge2WKv6gIjzSLzoTHUTkId9Zs4TqOqgmRHRriLVlh13KWR_Hipd4wVOMj6wF8dbUDXfaaDZo7NFwUa_ZxbyT8z23UDldWoNw1NMsnnYnsuYMeYx5SqzuQkmsoqwVG2QE8p630YVbVQzvXTdjaKwxTA4boDUUSsLKC8_pzh1Q0acC4pK7wG8v_wQbO-5g1t__pYeOyF9HSPSTJKTduKxssSAn34GHAJx1dusyUyeIm6sSTGwovvkR5JORa1vLG_HE4mr7-C1OVI-FvNhlbZ2r4cF3vVXerLWze143FNIUWFO3dW1AWRs3fo7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd0efe8be.mp4?token=jRdkefQYu1kCXEEzh_nKN92GRrZSFge2WKv6gIjzSLzoTHUTkId9Zs4TqOqgmRHRriLVlh13KWR_Hipd4wVOMj6wF8dbUDXfaaDZo7NFwUa_ZxbyT8z23UDldWoNw1NMsnnYnsuYMeYx5SqzuQkmsoqwVG2QE8p630YVbVQzvXTdjaKwxTA4boDUUSsLKC8_pzh1Q0acC4pK7wG8v_wQbO-5g1t__pYeOyF9HSPSTJKTduKxssSAn34GHAJx1dusyUyeIm6sSTGwovvkR5JORa1vLG_HE4mr7-C1OVI-FvNhlbZ2r4cF3vVXerLWze143FNIUWFO3dW1AWRs3fo7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الطيران الإيراني في سماء طهران العاصمة</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78217" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوي انفجار في محيط مدينة ميناب</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78216" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسؤولين أمريكيين: نتوقع ردا إيرانيا قد يستهدف القواعد الأمريكية كما حدث ليلة الثلاثاء</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78215" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68be3e7840.mp4?token=Vl82DkvU-J8WdUPjMH2ZHIpLbrJi650uS9hbAMiWPRUklYmae6JZhKKsxqLs8-p-_cF0sJzmHvZh0L_M0PPePMq8RXBewAgZDeDnUHsu6p423uFrxkiQ6GYYDZ5W6iEQwL3IQnqiIGJvVXDZTqUT2v4AY12VRbgjZd-QKkM4PpPzpdoBEJuXYpMkhNDA1xr3BSmx4QBX-AvfAiafH5uKVAepzyiSEk7B8XmcRfnR9dw5B9atVhrewyCOiAedMztSGhNRsdVR13vGjr9d-YosHRUedlNVkVAxzStwH08UHorXTy-E3qvvN-xpMkeWI7cNd-K82BjweifuheZ99d_FyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68be3e7840.mp4?token=Vl82DkvU-J8WdUPjMH2ZHIpLbrJi650uS9hbAMiWPRUklYmae6JZhKKsxqLs8-p-_cF0sJzmHvZh0L_M0PPePMq8RXBewAgZDeDnUHsu6p423uFrxkiQ6GYYDZ5W6iEQwL3IQnqiIGJvVXDZTqUT2v4AY12VRbgjZd-QKkM4PpPzpdoBEJuXYpMkhNDA1xr3BSmx4QBX-AvfAiafH5uKVAepzyiSEk7B8XmcRfnR9dw5B9atVhrewyCOiAedMztSGhNRsdVR13vGjr9d-YosHRUedlNVkVAxzStwH08UHorXTy-E3qvvN-xpMkeWI7cNd-K82BjweifuheZ99d_FyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امريكا تتبنى رسميا العدوان على المحافظات الايرانية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78214" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
سنتكوم: ‏بدأت قوات القيادة المركزية الأمريكية اليوم، في تمام الساعة 5:15 مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية إضافية ضد أهداف متعددة في إيران، وذلك بتوجيه من القائد الأعلى للقوات المسلحة. وتأتي هذه الضربات ردًا على العدوان الإيراني المستمر…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78213" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تفعيل الدفاعات الجوية في قشم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78212" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
سنتكوم:
‏بدأت قوات القيادة المركزية الأمريكية اليوم، في تمام الساعة 5:15 مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية إضافية ضد أهداف متعددة في إيران، وذلك بتوجيه من القائد الأعلى للقوات المسلحة. وتأتي هذه الضربات ردًا على العدوان الإيراني المستمر وغير المبرر.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78211" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">أنباء عن دوي انفجارين في بندرعباس</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78210" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لاتوجد انفجارات في قشم وكيش حتى اللحظة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/78209" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوي انفجار في محيط مدينة ميناب</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/78208" target="_blank">📅 01:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عدوان على ميناء سيريك بجنوب ايران</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/78207" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/78206" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في سماء العاصمة الايرانية طهران.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/78205" target="_blank">📅 00:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">إعلام العدو: الجيش الإسرائيلي يرفع حالة التأهب استعدادا لإمكانية استئناف القتال مع إيران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/78204" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjmBwycQaP4x_cf_Ik0Izrztc0MqRqtLFiALxmw5B2wjQArltdGKgmuJB3_jyeZyRqeHx-KOGJQdx3e7o9g4m2VUQY8diusuJEEGa-ItHDphR-0ap1iL0cy1Zh4Tp9vmh2rsvYfO1A3cEB3ZyilIDVTjDprDhBTl-GvSnreIgdN3LqLPZH04aFdXn8HsNh2E6oZ1-OeVb3EkFzW8cBvcW8F9fs8dIlbLXsJsNzOc4gYwZ2oX8UCBygh0QLwDbPTQp01MBgizSpAaVF7STeWRh5wo3REWb19Xb-paL1kMsab9UWV3qbM5LwDXnssriy8HGcP2UF6jnDlCGFgbkxPRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشيخ محسن الأراكي عن النزع
حرام شرعاً ولا شك أن تجريد قوى المقاومة عن سلاحها اضعاف للمقاومة ونصرة للطغاة والكفرة الحربيين وعلى رأسهم الطغيان الامريكي الصهيوني.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/78203" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">التلفزيون الإيراني: الطيران في اجواء محافظة لرستان غربي البلاد تابع للقوات الجوية الإيرانية</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78202" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">التلفزيون الإيراني: الطيران في اجواء محافظة لرستان غربي البلاد تابع للقوات الجوية الإيرانية</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/78201" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية تتصدى لاهداف معادية في سماء محافظة فارس الايرانية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78200" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNQSvTPChKwqCVAmYL4AshKMPZJIL9UMg2w_3LJWV4FgPfh00kg-bM2pZ66XKgFMVIdhIb4-P2Ucm5Qym8dLorwf9Ao_hQHL9mB31U529XdvjfmNtWbqV4EXwcKcWA3ZdePcSmezJoS9vahrkeiqktpIKPDtDg0msRJuSQuTVJ5JmHGSex6bRPlgWJVI2Pisg9w5qvaRVvN2EzdVBDv5adRoBed2Sllf6AUr1KMBBrwdye0dIzvIQeoX-laEPKu7WF_7FWMWfCPGVxPjw9ErWwSBDJEEEk9MBhIrQiocLQQ_ziLSesAfl1DruFeUUAVXNPxprDxaTkfkXgQIhoFnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بين إغلاق وتعطيل الرحالات مطار أربيل الدولي شمالي العراق</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78199" target="_blank">📅 00:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية تتصدى لاهداف معادية في سماء محافظة فارس الايرانية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/78198" target="_blank">📅 00:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
🇮🇷
وزير الحرب الأمريكي بشأن إيران: القيادة المركزية ستكون مشغولة الليلة.   الولايات المتحدة ستقصف منشآت رئيسية في إيران.  ‏الضربات التي ستحدث الليلة ستكون قوية وواضحة.  ‏الضربات الليلة ستعزز المصالح العسكرية الأمريكية وتدعم الموقف الدبلوماسي.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/78197" target="_blank">📅 00:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=hTTCKG0tXcp5QzRpn6_NPGTsiz6gHftn17XdODjyztwVjHC134EGJECHDnuogIGEVlwBfXgPFiCqoCUAa1ytAC7kvfkJsMOopvXsBwFS2Sz7KpcGRdtJPjIp_FceBEAmUaZm_jxCoYGH6TtQv303CiuUTw0ZQb_MdXEXSsE-sDFSqHU3eFprWIfLmt0NfFV5g-Qm9MgGAQNjhar9Y_VhKjWYioieSrqWQn7w5OnSEnYK3GI3cV4qYqGxTWX0K5tvTIN7oHDzwlKFaMfIlKDHi9Ya1DJO5hYlG0BvETIbfxbj786eIVJdJSwud9yOsKIX4Pi_rpdYZ5LY23XMKJmPOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=hTTCKG0tXcp5QzRpn6_NPGTsiz6gHftn17XdODjyztwVjHC134EGJECHDnuogIGEVlwBfXgPFiCqoCUAa1ytAC7kvfkJsMOopvXsBwFS2Sz7KpcGRdtJPjIp_FceBEAmUaZm_jxCoYGH6TtQv303CiuUTw0ZQb_MdXEXSsE-sDFSqHU3eFprWIfLmt0NfFV5g-Qm9MgGAQNjhar9Y_VhKjWYioieSrqWQn7w5OnSEnYK3GI3cV4qYqGxTWX0K5tvTIN7oHDzwlKFaMfIlKDHi9Ya1DJO5hYlG0BvETIbfxbj786eIVJdJSwud9yOsKIX4Pi_rpdYZ5LY23XMKJmPOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
السفارة الأمريكية في بغداد: نظراً للتطورات الإقليمية الأخيرة، نُنصح المواطنين الأمريكيين في العراق بالحفاظ على أعلى درجات اليقظة والانتباه ومتابعة مصادر الأخبار المحلية باستمرار. وقد تحدث اضطرابات في السفر أو إغلاقات للمجال الجوي بشكل مفاجئ ودون إشعار مسبق.ويُنصح…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78196" target="_blank">📅 00:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
السفارة الأمريكية في بغداد:
نظراً للتطورات الإقليمية الأخيرة، نُنصح المواطنين الأمريكيين في العراق بالحفاظ على أعلى درجات اليقظة والانتباه ومتابعة مصادر الأخبار المحلية باستمرار. وقد تحدث اضطرابات في السفر أو إغلاقات للمجال الجوي بشكل مفاجئ ودون إشعار مسبق.ويُنصح المواطنون الأمريكيون بما يلي:‏"لا تسافروا إلى العراق لأي سبب كان. وإذا كنتم موجودين فيه، غادروه الآن."</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78195" target="_blank">📅 00:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مصدر ‏إيراني مطلع: سنضرب أهدافاً أمريكية جديدة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78194" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae33e394c4.mp4?token=ZJ3hCwaxQ1Ogm_MYdhPqybbJIaTnydZMmaofiWIrLf7epbDH-jv98BgQO2ooRbsmO6VJCM9XZoE5ftMtNtEvJ1Rf-3dVxFBfoC_U7jwCiWJBXFrd2UgaNK6DTmNoi8kE2kZp6kZQNo0DKEeaKvxVri7gNaUlgbeNr5NNtMOmofOtb01nikJpfxrD0vtme9Z0JdSvv2y_ULNILvC0x-BBGji8sVzXTGSLdKWUq5YyDICc9n92Xzx8rt6Kkg_SDmXkIp1vd44TJ_mWNMEt1IcCmz-4UUnDfRyK_Bav7T3bWGXDhrs3AfTWtsBtJZ4tkX7q9aG_W-sehMCrs9J2fSKDjaqMeXM4peAm7CcrrehkQ-4FhAE1i64PCKNxP8oCpB0eGF7Wu3iyKzuLtk-mp69giqhwCGrSKRk1ZwQJy_ROXl4D7BkJ9bgmkggOOEzy_EaEPWfUornbUUIoma5EDZqdqCT77d4TIvdLmrKsxNBeXVG2G1ehiV5BfNMjrlqUyxGQkUeO4HeXSiA31NEqMVAhceLcYYE7s0OocH2IoceMoqn5mpVdaejkVEeqcNtroSY-YxWxncEk9i0DCzQzDcOVPglNuuyyiPECb9y-BU20Oy_91EF3HcWNHRNcdo2om504xKNrqXuwW4jNTSZo31lrRW4rnSFlvCIxHcp0Rjlug9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae33e394c4.mp4?token=ZJ3hCwaxQ1Ogm_MYdhPqybbJIaTnydZMmaofiWIrLf7epbDH-jv98BgQO2ooRbsmO6VJCM9XZoE5ftMtNtEvJ1Rf-3dVxFBfoC_U7jwCiWJBXFrd2UgaNK6DTmNoi8kE2kZp6kZQNo0DKEeaKvxVri7gNaUlgbeNr5NNtMOmofOtb01nikJpfxrD0vtme9Z0JdSvv2y_ULNILvC0x-BBGji8sVzXTGSLdKWUq5YyDICc9n92Xzx8rt6Kkg_SDmXkIp1vd44TJ_mWNMEt1IcCmz-4UUnDfRyK_Bav7T3bWGXDhrs3AfTWtsBtJZ4tkX7q9aG_W-sehMCrs9J2fSKDjaqMeXM4peAm7CcrrehkQ-4FhAE1i64PCKNxP8oCpB0eGF7Wu3iyKzuLtk-mp69giqhwCGrSKRk1ZwQJy_ROXl4D7BkJ9bgmkggOOEzy_EaEPWfUornbUUIoma5EDZqdqCT77d4TIvdLmrKsxNBeXVG2G1ehiV5BfNMjrlqUyxGQkUeO4HeXSiA31NEqMVAhceLcYYE7s0OocH2IoceMoqn5mpVdaejkVEeqcNtroSY-YxWxncEk9i0DCzQzDcOVPglNuuyyiPECb9y-BU20Oy_91EF3HcWNHRNcdo2om504xKNrqXuwW4jNTSZo31lrRW4rnSFlvCIxHcp0Rjlug9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هما إجو للموت ماجبناهم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78193" target="_blank">📅 00:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c05df1e0.mp4?token=epRCS89Xf8c7NfVqhLiMs511pKCEPdj_YjXtnlM5Q5HlRGyGA9IjX5b46vDGIYNpqE48SlB6jR4Yf-8piB48U594oK7nVFkcQfg3aLwTqe4kZ0dcBf4sA85ge8x9EDmirB-GsvMjx0CayQNj0e4s5obnmCpI8uCVnziP3eHlq_gICpII--I0RLl2__vI0twXMcLuAYCslhNKirpYTpKYCG3jyj52gG5OGjdq0FK2SmMfHbuNfOTD9qrkvG-QfnfuTfx0LNlhd2Y_r9BJBRnx145IsWSjUxbw21sucj85O19QoEHGZ39vSA1qXnA7z-AMP3q4jmneBySujMTleFrJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c05df1e0.mp4?token=epRCS89Xf8c7NfVqhLiMs511pKCEPdj_YjXtnlM5Q5HlRGyGA9IjX5b46vDGIYNpqE48SlB6jR4Yf-8piB48U594oK7nVFkcQfg3aLwTqe4kZ0dcBf4sA85ge8x9EDmirB-GsvMjx0CayQNj0e4s5obnmCpI8uCVnziP3eHlq_gICpII--I0RLl2__vI0twXMcLuAYCslhNKirpYTpKYCG3jyj52gG5OGjdq0FK2SmMfHbuNfOTD9qrkvG-QfnfuTfx0LNlhd2Y_r9BJBRnx145IsWSjUxbw21sucj85O19QoEHGZ39vSA1qXnA7z-AMP3q4jmneBySujMTleFrJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
وزير الحرب الأمريكي بشأن إيران:
القيادة المركزية ستكون مشغولة الليلة.
الولايات المتحدة ستقصف منشآت رئيسية في إيران.
‏الضربات التي ستحدث الليلة ستكون قوية وواضحة.
‏الضربات الليلة ستعزز المصالح العسكرية الأمريكية وتدعم الموقف الدبلوماسي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78192" target="_blank">📅 00:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
مصدر استخباراتي إيراني:
إيران تراقب عن كثب جميع تحركات الجيش الأمريكي في المنطقة، براً وجواً.  كما سبق التحذير، فإن أي تحرك عسكري ضد إيران من أي دولة - سواء على أراضيها أو في مجالها الجوي - سيُعتبر هدفاً مشروعاً للجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78191" target="_blank">📅 00:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
قال مسؤول أمريكي كبير إن طائرة الهليكوبتر الهجومية AH-64 Apache التي تحطمت يوم الثلاثاء كانت تحمي مجموعة من السفن في مضيق هرمز من الطائرات بدون طيار والصواريخ الإيرانية.
هرب الطياران من الطائرة المحترقة بعد أن سقطت في الماء، وخرجا قبل غرقها بثوانٍ معدودة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78190" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭐️
أكسيوس: قد تنهار المفاوضات خلال الساعتين إلى الثلاث القادمة!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78189" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
المندوب الإيراني بمجلس الأمن:
لا يمكن التوصل إلى اتفاق مستدام مع أمريكا بالتهديد أو الترهيب أو استخدام القوة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78188" target="_blank">📅 23:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ed92d82b.mp4?token=aEpMYCU-rPKPnCmF3AjDwlla7atT8lEQOUSkHpzjCQAPAPm-X-CpoQRY8_IFdRSN_M_m3GOd4OfuoKKH6435me6yNvSQcQHjnnFa7o4aGbfYVCwVVKrBa-wFQTjVzrSboVTDWur7Js8TnFu632yyfjBWePHVtoQJsKjxi2tRNFYr-8-Zh_Cu23Eo-glBY65eTJvjZwo5O4mtJIxFhkpjcd3wG9ky_1exEg3EKoIH6D4Mx-xf9INapvHTWogH8_AhrUMMjCvQiewD3CEjPbpzZu1WZpZmVu39L4ORhOYJbgw8I7aOu5TlaQjp6us1tqJQDGxcr1EJAugb4JAzKuIKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ed92d82b.mp4?token=aEpMYCU-rPKPnCmF3AjDwlla7atT8lEQOUSkHpzjCQAPAPm-X-CpoQRY8_IFdRSN_M_m3GOd4OfuoKKH6435me6yNvSQcQHjnnFa7o4aGbfYVCwVVKrBa-wFQTjVzrSboVTDWur7Js8TnFu632yyfjBWePHVtoQJsKjxi2tRNFYr-8-Zh_Cu23Eo-glBY65eTJvjZwo5O4mtJIxFhkpjcd3wG9ky_1exEg3EKoIH6D4Mx-xf9INapvHTWogH8_AhrUMMjCvQiewD3CEjPbpzZu1WZpZmVu39L4ORhOYJbgw8I7aOu5TlaQjp6us1tqJQDGxcr1EJAugb4JAzKuIKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إندلاع معارك عنيفة بين عناصر قسد وعصابات الجولاني الإرهابية في مدينة عين العرب بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78187" target="_blank">📅 23:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
مجلس محافظة الديوانية يعطل الدوام الرسمي يوم غداً الخميس باستثناء الامتحانات الوزارية بمناسبة فاجعة سبايكر.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78186" target="_blank">📅 23:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كركوك توجه بتعطيل الدوام الرسمي يوم غد وفاءً لشهداء سبايكر وتضحيات القوات الامنية البطلة.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78185" target="_blank">📅 23:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
نائب محافظ قم المقدسة:
الشائعات المتداولة حول نشاط الدفاعات الجوية في قم المقدسة خلال الساعات الماضية غير صحيحة. لم تُسجّل أيّ حوادث أمنية في قم المقدسة حتى الآن، ويسود الأمن والهدوء في المحافظة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78184" target="_blank">📅 23:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة ميسان تعلن تعطيل الدوام الرسمي يوم غداً الخميس وذلك إحياءً للذكرى السنوية لمجزرة سبايكر الأليمة وتخليداً لدماء الشهداء الأبرار.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78183" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
اكسيوس: إيران ترفض الاجتماع الثلاثي مع الولايات المتحدة وقطر.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78182" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث غير عادي مرة أخرى على خط المواجهة، طُلب من سكان زرعيت الدخول إلى الملاجئ والبقاء بالقرب منها حتى إشعار آخر: "يجب تجنب التجمعات والتنقل في المنطقة، والالتزام بتعليمات قوات الأمن".</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78181" target="_blank">📅 22:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345cbd8002.mp4?token=T4ItsLIB5ur7753a1im98-E6x3ZX8GPGDxx9QVeT-QeWzmBtKM87UOEpltvW-G-VLSoN7Vg6cALOObgt_jSnC87EN935FPpzH0x9WWc6KKgpfNa61PRzpPXwL8ChgLNMhGi6ziprmTXCnwuiwLBqIyULIirDh6Y2iLaRgtV2JQqXXdx1NZ8Gir6RoIgWf2kSeIXbkqJQ-FQdeHRm1r7S4Df0Hy5oVgpR1zppopXBcSkHDNEGMCCqR8bYWK6wLK598RrLSAJwFwMjHctjnUzjE0x2Xk1LG_c25XIhMbQotu6Jvv3TUVmGdz7Z5qxJ5R8Ln1nxforKoqH8xEgj0JQ5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345cbd8002.mp4?token=T4ItsLIB5ur7753a1im98-E6x3ZX8GPGDxx9QVeT-QeWzmBtKM87UOEpltvW-G-VLSoN7Vg6cALOObgt_jSnC87EN935FPpzH0x9WWc6KKgpfNa61PRzpPXwL8ChgLNMhGi6ziprmTXCnwuiwLBqIyULIirDh6Y2iLaRgtV2JQqXXdx1NZ8Gir6RoIgWf2kSeIXbkqJQ-FQdeHRm1r7S4Df0Hy5oVgpR1zppopXBcSkHDNEGMCCqR8bYWK6wLK598RrLSAJwFwMjHctjnUzjE0x2Xk1LG_c25XIhMbQotu6Jvv3TUVmGdz7Z5qxJ5R8Ln1nxforKoqH8xEgj0JQ5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
دعماً لمحور المقاومة..
حشود غفيرة في الضاحية الجنوبية لبيروت ترفع أعلام حزب الله واليمن والجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78180" target="_blank">📅 22:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث غير عادي مرة أخرى على خط المواجهة، طُلب من سكان زرعيت الدخول إلى الملاجئ والبقاء بالقرب منها حتى إشعار آخر: "يجب تجنب التجمعات والتنقل في المنطقة، والالتزام بتعليمات قوات الأمن".</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78179" target="_blank">📅 22:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
اكسيوس:
إيران ترفض الاجتماع الثلاثي مع الولايات المتحدة وقطر.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/78178" target="_blank">📅 22:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHQ1oePEswV_RH7QysiSMeejFiiJn4rXyAnq3uhOQSVoZrWLb9sEz4XCl4LMeeFGD-SmUJSymCgZ0G3emro78HvMUgAPuxYpgp72dNBqhEOSffqnrIQBJI0WqAq_DYaUWPW4zzwfxJAZ3BWQKLXXA0TBBYWhmLT9VcFLh1lpC4Vn9L6_yJfA0ZCwH8kq5t7sN3GZa3wNTz850l1CneniFsJ3gmHY4EYgxZOqI7q9nvVBDzAV8UejPxDoS-JYfrih7PbrUFASRTudF3DBnl4BjFRTmikzQVmYC613hkgENUJ4HpHC1BJfojxspyhx73G29dG4lmGLInu25Ymo6-DhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الإيراني"إبراهيم عزيزي":
لسنا خائفين من قتال الخاسرين.
عدد الخسائر الأمريكية أعلى بكثير مما يؤكده ترامب، وسيرتفع.
هذه المرة، لن تقتصر الحرب على المنطقة.
سنرى ما سيحدث!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/78177" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIarbuMSJKOGOBYDsR33iVVlCY-XCY2uEBThasKlWHYbHtP_DPNAB7D0b3GUAWuUVx7b9wrpdDs1wL_GDcKwT06mXA9vkeZRq43Sw2Upjpu46_EMY0TIUuxeH4vWeznELzFVmcFwFXXB3IKP6lRc7RdtHbZxCS1MPYz3AWFU9RI_U1CJYBOTww8Topdire5fqhcr4yl1BEupFxqwMG3LKJz8HFF2AL_cwBPW_jA9FjipWzTN_jZQzXoHIaz-5ItMrL2qSEyw6RZSmuXFoSG27T-RxdrZBrQ6cPKSqADV5qHEunGH43Lrm1ru7w4e-8KWpZ2fMp1ReUMH_qtWcAZ0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2PQ7hxo2KBzrzFLajE9ZuxG1sE57NmyycrIKyOxkbtkuecv9IR4eqVkuPT_UztuwHiDd41qbR_h8zyKv7kCDsmKAjSjq3G4ehU5rJgfheXy1vbkfmKOw8fllTB_egDs-gOjyL8ANBAhEalY_xKTKYWvhoILO46BAtcjo5wbP-3FrCiFaklevYWX4u_B42KM6avcWD5-s_D-G4Wg7K6MGJMzpW9BLf9ppLtNjh2kNAuSKA6ZzWel5gqdZmco8xI8-I9K2uSoi1ZDPY0DtZQoOJPOrpO_NDvVO9ujEPn6PsNF2iziEpWLOyxIYzfwXz4R6jpaKzCKzQ6alr2COGn9hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a362799fc.mp4?token=n-Ko8SIGpKPJBxRQxt-nVpaWtDzz2gNb3tIBqaWfNvcBDouRE4kzOlxoOHJHoE0WoZEGDLwW7BV1EXAA56FbhzkkSXzEgILU2J5SZwR8PTlel36qyUsjEb1jSZGGNUFJDX5oTq8KAwVAVLvNyrXZQ8T2jR__k6_aNHqxF6CA7BpLlgoSGxRpP2xZxqRPOokn7lVJif4_H6rY7cuzH6j-lQ2t3AjqVgxXSW4i8KWCOr98pFLOAPc5YBDiLoHbL9QojjQsPAKb8ttNdnAECeHdQqUM7h7T-Zmwg_izOjv2_JsjXh3oIK2dULNGA4hJOUqDg1_p-A6uc_iYwlFGEqUV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a362799fc.mp4?token=n-Ko8SIGpKPJBxRQxt-nVpaWtDzz2gNb3tIBqaWfNvcBDouRE4kzOlxoOHJHoE0WoZEGDLwW7BV1EXAA56FbhzkkSXzEgILU2J5SZwR8PTlel36qyUsjEb1jSZGGNUFJDX5oTq8KAwVAVLvNyrXZQ8T2jR__k6_aNHqxF6CA7BpLlgoSGxRpP2xZxqRPOokn7lVJif4_H6rY7cuzH6j-lQ2t3AjqVgxXSW4i8KWCOr98pFLOAPc5YBDiLoHbL9QojjQsPAKb8ttNdnAECeHdQqUM7h7T-Zmwg_izOjv2_JsjXh3oIK2dULNGA4hJOUqDg1_p-A6uc_iYwlFGEqUV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بغداد تحتفل بمناسبة اليوم الوطني الروسي عبر وضع العلم العراقي والروسي كجزء من التضامن والعلاقات الشعبية بين البلدين على شاشة مول الحارثية … يذكر ان العاصمة بغداد شهدت اليوم حفل آخر كبير برعاية السفارة الروسية لدى العراق على فندق الرشيد حضرته عدد من النخب السياسية والثقافية والإعلامية وعدد من أعضاء مجلس النواب بمناسبة اليوم الوطني الروسي .</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78174" target="_blank">📅 21:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط موقع بلاط المستحدث جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78173" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlPjE--OWswc_N9sv2e4XUqjHHiT6gvqa7KkOKx7-IgwjIYVjlw9ShQEQvVb0FMsRvei8rx_gv1MmBm6GXJxT-xd2oA6HW1wdEa4791AvlyBzqtNTwsBE44XJyIDMAPlDHOYJdOotj6vplmHAwaSqdzZEn56WU94VDIPLZTwnX7G6pED8qgveD0mvXITiShU5rLkLL7z7EIdtzdePK0QvBXdaBTZcpBiCYeYhegiRMugwn2QWEPH8eiI-4_45CURx-48oEN6vkwXybk89_2hUxKXQRvYuaf_DBCz0Ok2wQaTDcfk88v-Srd-zGf_XQPB0eXPvMZ9mCqfqWtmpFMxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في الشهر الماضي، وجهتُ جيشنا الأمريكي العظيم لتنفيذ مهمة سرية لدعم ناقلات النفط والسفن التجارية الأخرى عبر مضيق هرمز. واليوم، يسعدني أن أعلن أن هذا الجهد قد أسفر عن مرور أكثر من 100 مليون برميل من النفط عبر المضيق، ودخولها السوق المفتوحة. وقد عبرت أكثر من 200 سفينة تجارية المضيق بأمان. ويعود هذا النجاح الباهر إلى سيطرة الولايات المتحدة الأمريكية على مضيق هرمز - وليس إيران. لقد هُزم جيشهم، وخسر اقتصادهم. لقد انتهى الأمر بالنسبة لإيران! شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78172" target="_blank">📅 21:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني كاتس: "الحملة ضد إيران لم تنته بعد - الجيش الإسرائيلي مستعد لمهاجمة إيران بقوة كبيرة".  نحن نرفض من البداية محاولة إيران ربط الساحات.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78171" target="_blank">📅 21:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني كاتس:
"الحملة ضد إيران لم تنته بعد - الجيش الإسرائيلي مستعد لمهاجمة إيران بقوة كبيرة".
نحن نرفض من البداية محاولة إيران ربط الساحات.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78170" target="_blank">📅 21:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl87q_KM6tsGju7SDu2PdKkoRLs0C0s8b-wR7K6kJFCufr_rOiakGccYFoGdNE839b4T3UZRkKD5dLcuaF3MrRuIqIoBYJgaY7OArAP0467l8cNEUXvyyOrVGqMOtARmgmrzaU1O5zcx4VMWbpm3i27WzyW7BgLL3r6m4xQYfrNVbZrlkTCdadTm6SRldvCBumG4tTrsCBNZ551oDK3EiQ5-mVR0zfeeylWrURHu_GZDEBpsJz-DO24MVCh40ethRSNJasCEmDECr1yGtfsq_zEhW3xkp1zVxqJ-87L_wvH-2zGc-HPnti2hwKWyqQLwwBL9GwKNQtl02wcPpz91Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
رصد نايا..
‏تحلق الآن قاذفة قنابل استراتيجية من طراز B-52H ستراتوفورتريس تابعة لسلاح الجو الأمريكي فوق المملكة العربية السعودية باتجاه الخليج الفارسي مع تشغيل جهاز الإرسال والاستقبال الخاص بها.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78169" target="_blank">📅 21:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي:
البيت الأبيض أوضح للإيرانيين أن الوقت ينفد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78168" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
أطلقت تايوان لأول مرة قاذفات صواريخ HIMARS التي قدمتها الولايات المتحدة في مضيق تايوان، مستخدمة 32 صاروخًا اختباريًا في تدريبات بالقرب من منطقة هبوط صينية محتملة.
على الرغم من أن الصواريخ المستخدمة كانت ذات مدى قصير، إلا أن ترسانة HIMARS التابعة لتايوان تشمل صواريخ قادرة على الوصول إلى البر الرئيسي الصيني.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78167" target="_blank">📅 20:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtI-xSnpPpcwYYjTAxoCkmKKw0F7ucWICai-bQ4qbNnMWDYUEftNypAC2CyvLDmwa6bpzPFnWKK8eI7Ksz_f_317sNcTaRQjRTCw9x_hxhom_7UpcjR7twNIFll1pw4_9PQnCZdT9n4jdni3B0n4Xw1tqApRLa0Iv3Bn5QVLDZ3MJfnFLZ-ml26aeCZ0jzQn8UkNt_NvAxC20Jcv0a8la222OGZBNLhpHwE-EBGXwP5HuLG2Ukpo_7aFmbZgYV7nKgYDzk83zcpet5kyBcfT9aUTlecwfAcI0YcWpdHdfvDDf28BEbPonesmdQvAKd-gcq4G9CFZuUJ4vjdl4-64WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تهانينا لصديقي، رئيس الوزراء ناريندرا مودي، على أن يصبح رئيس الوزراء الأطول خدمة في الهند - وهو عظيم! إنه رجل قوي وصحي وحكيم، وسيكون أمامه سنوات عديدة من العظمة والنجاح!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78166" target="_blank">📅 20:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة بغداد تعطل الدوام الرسمي يوم غد الخميس في ديوانها ودوائرها استذكاراً لأرواح شهداء مجزرة سبايكر.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78165" target="_blank">📅 20:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ترامب:
من دوني لم تكن إسرائيل موجودة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78164" target="_blank">📅 20:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">المراسل:  هل أنت قلق بشأن أحدث رقم للتضخم الذي صدر هذا الصباح؟  ترامب:  لا، أنا أحب ذلك. الأرقام كانت رائعة. أتعلم ما الذي أحبه حقًا؟ أنا أحب التضخم. أتعلم لماذا؟ لأنه بمجرد أن تنتهي هذه الحرب — تعلم، يمكنني أن أقول ذلك الآن، شيء لم تكن تعرفه.   لقد كنا نستخرج…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78163" target="_blank">📅 20:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
في ختام تقييم الوضع، تظل سياسة الدفاع التابعة لقيادة الجبهة الداخلية دون تغيير وستظل سارية حتى يوم الأحد، 14 يونيو 2026، الساعة 20:00.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78162" target="_blank">📅 20:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78161">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴‍☠️
النتن ياهو للبنان:
نحن نتوق إلى السلام معكم. العقبة الوحيدة أمام هذه الرؤية الجميلة هي حزب الله. أنتم تستحقون أكثر. أطفالكم يستحقون أكثر".إسرائيل تريد السلام معكم. استلموا مستقبلكم، وانضموا إلى إسرائيل. بمجرد تفكيك حزب الله، ستكون الفرص لا حصر لها".</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78161" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سي إن إن:
أخبر بيل جيتس الكونغرس أن جيفري إبستين حاول الضغط عليه باستخدام معرفته بشؤونه الخارجة عن الزواج بعد انتهاء علاقتهما.
“علمت أن إبستين قد أصبح على علم بمعلومات حساسة عن حياتي الشخصية، بما في ذلك حقيقة أنني كنت غير مخلص في زواجي.”</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78160" target="_blank">📅 20:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245f0d1885.mp4?token=Arcmiim7VeveXcTytFPF3LQ_NcEvjJu_1nH279sZNgGV5nk_TeyXXDouUYqlH0I0vcPTR1vVbZyQGcSpr4nwXKRwEeiBBU58FpDDV0XTKNQixcjRaDn3xgr5j18TJNyyIU7h8nhmf_a0AOoaHym4l5Lmx7i3dbvLeFycV4_1F-4q6wGKBbQHFL3Nol_Y-zrMn0ywQNhK36yXuD2iyvNjOKUSfOuCYZuSf_YOIyP-tENZphbGx-lU-3F-P7tJv9x6hp9nCSobtmvKaS1bGI4Lah6S9qYxKBoaSIf5HpaPxAfMmcUsraaDdkunlbNFzftI3Bq6rm587PA2eitgC2J-Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245f0d1885.mp4?token=Arcmiim7VeveXcTytFPF3LQ_NcEvjJu_1nH279sZNgGV5nk_TeyXXDouUYqlH0I0vcPTR1vVbZyQGcSpr4nwXKRwEeiBBU58FpDDV0XTKNQixcjRaDn3xgr5j18TJNyyIU7h8nhmf_a0AOoaHym4l5Lmx7i3dbvLeFycV4_1F-4q6wGKBbQHFL3Nol_Y-zrMn0ywQNhK36yXuD2iyvNjOKUSfOuCYZuSf_YOIyP-tENZphbGx-lU-3F-P7tJv9x6hp9nCSobtmvKaS1bGI4Lah6S9qYxKBoaSIf5HpaPxAfMmcUsraaDdkunlbNFzftI3Bq6rm587PA2eitgC2J-Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
توثيق يظهر دمار كبير في السفينة الهندية التي استهدفتها القوات الأمريكية قبل يومين.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78159" target="_blank">📅 20:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az3HlGM3xgbTYufGbIHiQJEk8WDqf8FMCGzAz0KUQvzyhFnicaxOzm0sCdKtbxv5_LxzCYGlVMad9o6nX82Vy46Nj9rLJT854SVaKh8lpqA16CZaVdoU2Qx11VArU1IZ2HoHBBlHfeelHVcSUQos154olUQqnOxMYIKhxSIDBZS5gVkLR-z0aptzp5qmLDXdqk1Hf_F2F98OVncarpNgUJYEEeYfYvRlzRJ57QE0lzEE2_RPCU3062sx0gb6j_4Rg6WlCT8PM1VBjzbrA-xCBXlMX2TogzGsedjM_ElVMSldQ7XNDugaqGs2p0rkhzFx9qIl7_FCQo-3GToGgrAOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزشكيان:
تُعدّ البنية التحتية الحيوية شريان الحياة للشعب. والتهديد باستهدافها، بدءًا من شبكات النقل وصولًا إلى قطاعي الكهرباء والمياه، ليس استعراضًا للقوة، بل دليل على اليأس أمام إرادة الشعب.
ستصمد إيران في وجه أي ضغط أو تهديد، مستندةً إلى خبرة وكفاءة أهلها، ووحدتها الوطنية، وتضامنها.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78158" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEKW2i8xdRiCN7vH2V1XHm2HOvSthGTBeWmpZvvw0P-LyVFo6a3wYaBaK6LEse3QuRyel_DI5LbrTGrUU6d6wCYuDJ8f5BtUCvAaxGLoCfchGCx--KLYza8q5mqu6U-aQxFZpk70vFYx4EvaT_LmMbDzcmoPuMBAlyWWmUNhMBsqjYWTUqOw11l0EnGjo58IPQ5qJxSdT275lK6QzpqNqrsPb_JC1nKiwkFkFVV2ohPdLPE2E0P0KO0k80KRz1XjbQ6FeA1yxJoR1zkDjwxtUecb7ioeYdCicyznHJWg9x38AOSfLpqgnCWT0jagQFnTwUQ_ukSoAXecTao9MvfH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3GgIu1l43cTUa0ja0TVp3BCmjx9HmnZ8nbI4fdb0j-bPew_masaHYbNs7DQWZBO73p0jJNCwWeFO_FbaL_Mnrspklv4KD-GHkwAKrtuN0L_vV0QZS54V9j4tju37Oekih3pyTtqyeN-KYsZJYisexRg8jJYztb8mf9-IGo9PM4KKUdcBTjUV5EDECli7X8KHOciOrZFaS-e1ZChta4tOs9WLpY5mTPJ_4alaOc_TTSJDan7tBxVmogqVJkCO_kw4rESIUycqIEnUA8ntaK6sd-HjnjPo1EKYY5MOoOzd8Vy_gNR1ewNDH5b3jA58iVMCPFbntUywIlPgA7CBwVyvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
دوي انفجار مجهول وارتفاع اعمدة الدخان في منطقة اروندكنار جنوبي إيران بالقرب من مدينة الفاو العراقية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78156" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec6fd73ce3.mp4?token=rnkBy9XJVO7oe5dqjp1KxSmnxs0G-t3UuXEnJsT8panrJ2CSFWfyj-PhCjbwivWZa0QwYVqRaACkGLYtytTbQHccXENQG5HST2RhE-JsyMDbFRU7eZANe45COW1XjguRMdUAovlxeakwE31-yif0aC7yMtICmN51McUvpEUvVNImV9jXFwgI-DIeLXgoDzY6i1p8Mf4OErKHT479jz2C5ESKJiVwlisfuHD5pQSxgzl5gIzmi1rs8dy2E-UUNOpvWQjx21oomZpeNYfd-t5_XZQh_wgqYWVN2YV-64IzbCHt2biuBgysgNcXEAUqqg_3HRM1eOH6W9ZXWvkehxYZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec6fd73ce3.mp4?token=rnkBy9XJVO7oe5dqjp1KxSmnxs0G-t3UuXEnJsT8panrJ2CSFWfyj-PhCjbwivWZa0QwYVqRaACkGLYtytTbQHccXENQG5HST2RhE-JsyMDbFRU7eZANe45COW1XjguRMdUAovlxeakwE31-yif0aC7yMtICmN51McUvpEUvVNImV9jXFwgI-DIeLXgoDzY6i1p8Mf4OErKHT479jz2C5ESKJiVwlisfuHD5pQSxgzl5gIzmi1rs8dy2E-UUNOpvWQjx21oomZpeNYfd-t5_XZQh_wgqYWVN2YV-64IzbCHt2biuBgysgNcXEAUqqg_3HRM1eOH6W9ZXWvkehxYZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الدخان الذي شوهد في العاصمة الإيرانية طهران ناتج عن اندلع حريق في مستودع قرب ميدان القيام، ولايوجد حدث أمني.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78155" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي ينشر مشاهد يزعم أنها لأستهداف سفينة في بحر عمان صباح اليوم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78154" target="_blank">📅 19:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39c7bbe50.mp4?token=jWlSD6Q9U8lZZkyMwgLQza_MHfSuGSsTRFZYNH-p2Qi2HZ-o7KWcEBFi5wUNKxS8ZLJsDKUMDFWsUQkto1iuF6aispzW30LpO7-bHCKTFTNcOHKBhMEceBpybGQ7ookjHZcWYoC155KYilWyeAQ9R1hR27fAeRqUbIYGXTJK6JXKIbPFKifw__LsftT8VoFceAChuLoR0WaU5raq2-zH_zF6LjLk0qjVvbxuCj_L0g7r70-tcz0GDYyE_psxzR8G-wwACo2nmdISIdvaL5-e05jsKJnAzqqF3lizM2QZ2ki7kq2bjdowvHpdWT1uzOjmmhgRuDc6L2eKZrVRuctXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39c7bbe50.mp4?token=jWlSD6Q9U8lZZkyMwgLQza_MHfSuGSsTRFZYNH-p2Qi2HZ-o7KWcEBFi5wUNKxS8ZLJsDKUMDFWsUQkto1iuF6aispzW30LpO7-bHCKTFTNcOHKBhMEceBpybGQ7ookjHZcWYoC155KYilWyeAQ9R1hR27fAeRqUbIYGXTJK6JXKIbPFKifw__LsftT8VoFceAChuLoR0WaU5raq2-zH_zF6LjLk0qjVvbxuCj_L0g7r70-tcz0GDYyE_psxzR8G-wwACo2nmdISIdvaL5-e05jsKJnAzqqF3lizM2QZ2ki7kq2bjdowvHpdWT1uzOjmmhgRuDc6L2eKZrVRuctXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي: في تمام الساعة 11:14 مساءً من يوم 9 يونيو، عطّلت القوات الأمريكية ناقلة نفط في خليج عُمان لليوم الثاني على التوالي، بعد أن انتهكت سفينة أخرى الحصار المفروض عليها بمحاولتها نقل النفط من إيران. عطّلت القيادة المركزية الأمريكية (سنتكوم) ناقلة…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78153" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇳
الخارجية الهندية: إنقاذ 21 هنديا من أفراد الطاقم البالغ عددهم 24 بينما لا يزال 3 في عداد المفقودين.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78152" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8314eb870.mp4?token=Kg5qHOLR2jGkU46ncFsCD4CKzzY-Elw9dJ-M19kwKEtvKPbIqAOXEC0s-nvhf8xQLV_GhSZkoHpOAGWxqNUepE9ACfjLIuQ-i-E4dnKlsdIfWgPp65zAomPPLPZP9qjNvVe98ISbW_A_zBec0T_ZmDeRhHqYDWtT6cImvAF1tN6Zt6vKgcevVFjEGqoMPY8SZSlbVNaUrqyVtFMdAfE1Tb7k8BbAsXDo7bpmclEhHwAeuDTNUXzJ3q6j-8koWJSRpsgkmkpp-dOthjG_8ev_8FTMBPcrHilZKd29gBiv5xRp4vinOdboeDyhAvtAuyrC9O_PsrTLFUyCrdZEIe0oPSNUe2OstDcEwkS321m7Z-C6MI-lEam0aMGUCaUXnR6r5do4NRIwkyXWRdisykjQAvR1M099trutczrqnd0WhwRiHp_O1pP1kjndZGfVjdV-ozjWjpH1xI_AAdEGUKNXt2zJNsUa88qJAz1yJFWt2Ip08jqfi5clpeQmf44m1h9E5RJPrZ7RZDpR84DGpx3jVo0t5onfJrTzmlTvQZnT1KRvQ02jWROZIL9pcMRsmCt886j8Y4YXBrAHbd5ejkyGKVVo5QaKTQhzF5ZAcdCCZP4KLjyh-51RwFl7FOdJ1OYlHZZu_v1_EE61Uh7-f3vBztBfCrh2zDc_XMy1WLA3crc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8314eb870.mp4?token=Kg5qHOLR2jGkU46ncFsCD4CKzzY-Elw9dJ-M19kwKEtvKPbIqAOXEC0s-nvhf8xQLV_GhSZkoHpOAGWxqNUepE9ACfjLIuQ-i-E4dnKlsdIfWgPp65zAomPPLPZP9qjNvVe98ISbW_A_zBec0T_ZmDeRhHqYDWtT6cImvAF1tN6Zt6vKgcevVFjEGqoMPY8SZSlbVNaUrqyVtFMdAfE1Tb7k8BbAsXDo7bpmclEhHwAeuDTNUXzJ3q6j-8koWJSRpsgkmkpp-dOthjG_8ev_8FTMBPcrHilZKd29gBiv5xRp4vinOdboeDyhAvtAuyrC9O_PsrTLFUyCrdZEIe0oPSNUe2OstDcEwkS321m7Z-C6MI-lEam0aMGUCaUXnR6r5do4NRIwkyXWRdisykjQAvR1M099trutczrqnd0WhwRiHp_O1pP1kjndZGfVjdV-ozjWjpH1xI_AAdEGUKNXt2zJNsUa88qJAz1yJFWt2Ip08jqfi5clpeQmf44m1h9E5RJPrZ7RZDpR84DGpx3jVo0t5onfJrTzmlTvQZnT1KRvQ02jWROZIL9pcMRsmCt886j8Y4YXBrAHbd5ejkyGKVVo5QaKTQhzF5ZAcdCCZP4KLjyh-51RwFl7FOdJ1OYlHZZu_v1_EE61Uh7-f3vBztBfCrh2zDc_XMy1WLA3crc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل:  هل تعتقد أن هناك فرصة لنشوب صراع بين إسرائيل وتركيا؟ ترامب:  أنا معجب بأردوغان كثيرًا. إنه شخص قوي... لا أعتقد أن ذلك سيحدث مع تركيا، ليس طالما أنا الرئيس، لأن أردوغان يحترمني وأنا أحترمه.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78151" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68899348d5.mp4?token=PptRdo_pgxFdjA_iVik1HT_Wmn5JtdX2Ca7rnKCSQFXFx5EWhbbgW3lrbk1gN-6kDXDbPy58qseoBzcGHeMWOKE8hwpyNp93ALl3o7l0wzjuJiCKYS3R129EsmQxdr7BQqkEhCwBV2i58CfIrVfSIFxtemoDVYudgnUKS6s68WyVIsSGyORpe7zEEXJPHZfwzXwc_NSkATwTUlBlsQPi3c9TzSMSCvw4tgoOa7iUZcWqBKUML0KPxBFioBXrnL6hoklO3oHpt8jHgz2Zxn2hcTjfed-KA7QtIpqXrcim-qdGcEKg7QQJwoU2NHiL0NuF8rtPn5M4gHrUxz_9-O_K1RK0URphM0oVSG2sne2FVUPEYrt8keitUSFD_w6lD-SRK-9KeJ8b_bDEHKE0qzZLFgmci2ysUeNAwNZYg43GcM1jlgvz2M3zBBKTuNxo0VHVLMcgivO7wVRFA7Frx83bVQKh0M2QgARVeJJUgFzNB2hlIZ38t9P6C7CuIDfHT_t_iGKplqVsy3Mt4T-63A-DoW9H07bmlQoQjafxr8HyLhNyEZ39d-BCytq1jPVrsCaG4xcRNW8MRuiB9EJTxUQqkaPb2Y-OXLFi8wERi8QGj-Tnu1qhZrSq9rkruYdPvkePQvFcXvSOtPQpsmaFb8mMFfg9LheYbfnYZ-9s_AAUpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68899348d5.mp4?token=PptRdo_pgxFdjA_iVik1HT_Wmn5JtdX2Ca7rnKCSQFXFx5EWhbbgW3lrbk1gN-6kDXDbPy58qseoBzcGHeMWOKE8hwpyNp93ALl3o7l0wzjuJiCKYS3R129EsmQxdr7BQqkEhCwBV2i58CfIrVfSIFxtemoDVYudgnUKS6s68WyVIsSGyORpe7zEEXJPHZfwzXwc_NSkATwTUlBlsQPi3c9TzSMSCvw4tgoOa7iUZcWqBKUML0KPxBFioBXrnL6hoklO3oHpt8jHgz2Zxn2hcTjfed-KA7QtIpqXrcim-qdGcEKg7QQJwoU2NHiL0NuF8rtPn5M4gHrUxz_9-O_K1RK0URphM0oVSG2sne2FVUPEYrt8keitUSFD_w6lD-SRK-9KeJ8b_bDEHKE0qzZLFgmci2ysUeNAwNZYg43GcM1jlgvz2M3zBBKTuNxo0VHVLMcgivO7wVRFA7Frx83bVQKh0M2QgARVeJJUgFzNB2hlIZ38t9P6C7CuIDfHT_t_iGKplqVsy3Mt4T-63A-DoW9H07bmlQoQjafxr8HyLhNyEZ39d-BCytq1jPVrsCaG4xcRNW8MRuiB9EJTxUQqkaPb2Y-OXLFi8wERi8QGj-Tnu1qhZrSq9rkruYdPvkePQvFcXvSOtPQpsmaFb8mMFfg9LheYbfnYZ-9s_AAUpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو يهاجم أردوغان: الطاغية المعادي للسامية أردوغان الذي يرتكب إبادة جماعية ضد الأكراد، ويدعم منظمة الإرهاب حماس، ويقمع شعبه ويضع خصومه السياسيين في السجن هو آخر من يمكنه أن يعظ دولة إسرائيل. دولة إسرائيل وجيش الدفاع الإسرائيلي، الجيش الأخلاقي الأكثر في…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78150" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-TKSoOgY9DEuEmIhCWEZjo1F_r1PvO6ljMSQDTLpQTfcFuotqDPguPZmvRBAcSsVxnF0D4GR9QaOANDgoxR7_1Yls34S04UxqOl5-VNbuTVJC8dXixDNe_eRm1hv1NbLR1ZuQZ28kMcTdTRdi9-bLccHg7izyBe2SMUj6GR1c5BNkMC9U_L9h9ccUo-GpSujh1WUc4GoN8YTnmZQj1QiBcjBHPVsuPS-Q8QToeUWh7dQr5R2yrfvG_c7T9q7g0zSKkYiF9ism0isuvuNge4MWjmYxSPZVSXcyh__TBT6C2wazXwoe3L0fjG2ctPCCC7KYMOUOI3uEvk3BxEFCjyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
بعد دقائق من تهديد ترامب لإيران..
النفط يرتفع ويتجازو 93 دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78149" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7529d340.mp4?token=rpfHkjPrMyicB8V_A4FpBZgNCuN8c-sAv4tiur_GSidri_Zp547zcmoCav1F_vRNHujgoZBXqKUK11_3wIopnyE-WOD2ITUJTBWApW81McbrT-7JA3dPULbSxnjU6xFdeaiyI7v6YwmiF1fm7RAyhQcjP9hSFQSRPcQCsF5tNwBZ2TVjPh9Fgipr77dFNmkM4oiA5vr1Z7k9Ofx0gznPakdQj0AjQg1ATlgKJGRMc9ggFop8zVmAkuEEsc4uDz2AWh88s6W3WUYCCXZ66jRqRynyVY5z4UiOcqZb4SPdfS5EZtigst0hQea8WPOYbW_8s4Mx6yuhN_J0euKnEKxM5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7529d340.mp4?token=rpfHkjPrMyicB8V_A4FpBZgNCuN8c-sAv4tiur_GSidri_Zp547zcmoCav1F_vRNHujgoZBXqKUK11_3wIopnyE-WOD2ITUJTBWApW81McbrT-7JA3dPULbSxnjU6xFdeaiyI7v6YwmiF1fm7RAyhQcjP9hSFQSRPcQCsF5tNwBZ2TVjPh9Fgipr77dFNmkM4oiA5vr1Z7k9Ofx0gznPakdQj0AjQg1ATlgKJGRMc9ggFop8zVmAkuEEsc4uDz2AWh88s6W3WUYCCXZ66jRqRynyVY5z4UiOcqZb4SPdfS5EZtigst0hQea8WPOYbW_8s4Mx6yuhN_J0euKnEKxM5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لن أفصح عما إذا كنا سنستهدف الجسور ومحطات الكهرباء.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78148" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامب: سنوجه ضربة قوية لإيران اليوم مجددًا.  ضربنا إيران بقوة أمس وسنواصل الضغوط اليوم.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78147" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e3b8f531.mp4?token=Rp7F6Km-hnd1pCpy7flIX_P78Rl1PlhTFCfIoUIPLBdHlUd-PYt7hJra36iVCL4YFaCPLD4W9bfsCcXvLBkmD4UrD_R6fWBJTO8vK3ruqkug4BPBvUeZh6lnaLfC3QfoE2aMkzG2YbjpdtAcESB6NlNsXFBw4Pji817MjGGb5LA4AHKTPXt5lEChKsEtgrL6RJ_yu6wyWaljFeTfry6Gq4yHc84hNx_3j40LFSY3bs72-Pj7MG8YvkQly2bAwjH23kxn5_X695OeSRfrVFwOjV02ae4i_3X-aW12vXsjExoIOQZEVtDNexhYyWrxEInJnwWaXKNxWrtXKbMptlAmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e3b8f531.mp4?token=Rp7F6Km-hnd1pCpy7flIX_P78Rl1PlhTFCfIoUIPLBdHlUd-PYt7hJra36iVCL4YFaCPLD4W9bfsCcXvLBkmD4UrD_R6fWBJTO8vK3ruqkug4BPBvUeZh6lnaLfC3QfoE2aMkzG2YbjpdtAcESB6NlNsXFBw4Pji817MjGGb5LA4AHKTPXt5lEChKsEtgrL6RJ_yu6wyWaljFeTfry6Gq4yHc84hNx_3j40LFSY3bs72-Pj7MG8YvkQly2bAwjH23kxn5_X695OeSRfrVFwOjV02ae4i_3X-aW12vXsjExoIOQZEVtDNexhYyWrxEInJnwWaXKNxWrtXKbMptlAmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بشأن إيران: سنهاجمهم وسنهاجمهم بشدة جدًا. سنستأنف القصف. لدينا الحق في القيام بذلك. لقد أسقطوا طائرتنا الهليكوبتر.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78146" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامب بشأن إيران: سنهاجمهم وسنهاجمهم بشدة جدًا. سنستأنف القصف. لدينا الحق في القيام بذلك. لقد أسقطوا طائرتنا الهليكوبتر.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78145" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a40be040.mp4?token=YqZ0Fcn3VXZWOSIMbMNIacpK7YeOnK3MK1HdYtjuS-WWll14YpKXnfWgfEOb-6hjR5cu0vfUzs6r0cEo10ySwHJLJR0dgDI2EMjX-bf-1ZKSHHkyUM6MU8iwIJ6rKfBM9I0wUxmWepP2RQ9M1w8Z76bE9xpbscBXMcqEAZW3Ho6Ry_VZWfI__EPoP1NRZjg99THz-9ZBtjLhneTFMOFeYpnrqVI8WUIt4kwTbinVgOEfh3Cw0NbRDBQ_SdbMp2T0Q7QBfhh2FJITPPut7EyYFmMTQ7ukz6n6wApsYGLDbFgAKfPGoudgHqs7WwKMm-3e6QibXmZXwxYLio123Ht8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a40be040.mp4?token=YqZ0Fcn3VXZWOSIMbMNIacpK7YeOnK3MK1HdYtjuS-WWll14YpKXnfWgfEOb-6hjR5cu0vfUzs6r0cEo10ySwHJLJR0dgDI2EMjX-bf-1ZKSHHkyUM6MU8iwIJ6rKfBM9I0wUxmWepP2RQ9M1w8Z76bE9xpbscBXMcqEAZW3Ho6Ry_VZWfI__EPoP1NRZjg99THz-9ZBtjLhneTFMOFeYpnrqVI8WUIt4kwTbinVgOEfh3Cw0NbRDBQ_SdbMp2T0Q7QBfhh2FJITPPut7EyYFmMTQ7ukz6n6wApsYGLDbFgAKfPGoudgHqs7WwKMm-3e6QibXmZXwxYLio123Ht8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترمب عن إيران: إما أن نجد حلا معها أو سنقضي عليها.  يجب على ايران توقيع الاتفاق.  لقد كنت أعمل مع إيران لعدة أشهر، ويجب عليهم توقيع الاتفاق. إنه اتفاق جيد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78144" target="_blank">📅 19:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96c3ceb08.mp4?token=aC6x6EN5jjlDVOjpj7eFOHbJEMs21dRczjWdvoErA7h90wvN30WbYgGyKqA4ElBnxJT67Zj8ilEB3a0yFt_2shXrTxK3tGzg6k-XOEaJcqL9ZWVFSd6KFDNDSUs41vdmi2PtQdwz5iQhuXPp3Lubl2i2dahB1SrJvQnMrLieTtJ49H3eH3ksL58LJWDlhp5QSY23cxmW1L3bO6yO_b3ValL3W95uQQ7e53aLM-KjiecvDu_Gx9nLkDs2G3b8p2YIsoGPmli_nTDHlynHiHvrFkXu1D-LYtMx0Rw0LwjrMv0SGEqqjb6QVkh_VPUXS5PkDHJoD649yGM4qvHGaFFFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96c3ceb08.mp4?token=aC6x6EN5jjlDVOjpj7eFOHbJEMs21dRczjWdvoErA7h90wvN30WbYgGyKqA4ElBnxJT67Zj8ilEB3a0yFt_2shXrTxK3tGzg6k-XOEaJcqL9ZWVFSd6KFDNDSUs41vdmi2PtQdwz5iQhuXPp3Lubl2i2dahB1SrJvQnMrLieTtJ49H3eH3ksL58LJWDlhp5QSY23cxmW1L3bO6yO_b3ValL3W95uQQ7e53aLM-KjiecvDu_Gx9nLkDs2G3b8p2YIsoGPmli_nTDHlynHiHvrFkXu1D-LYtMx0Rw0LwjrMv0SGEqqjb6QVkh_VPUXS5PkDHJoD649yGM4qvHGaFFFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: شومر (زعيم الديمقراطيين في مجلس الشيوخ) يصاب بالجنون بسبب هذا، أو ذاك، أو إبستين، إبستين، إبستين!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78143" target="_blank">📅 19:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
ترامب: قمنا بقطع تدفق الفينتانيل عبر حدودنا بنسبة تقارب 60٪. وبالنسبة للقادمين عن طريق البحر، فإن النسبة 97٪.   ونحن نبحث عن الـ3٪ لأننا نعتقد أنهم من بين أشجع الناس.  أكره أن أخبر المكسيك بهذا، لكننا نركز الآن على الداخلين عن طريق البر.  كان يأتي الكثير…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78142" target="_blank">📅 19:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9849efe213.mp4?token=pWs_rjbZjtsVKzANkjWlFLxoD1rj97nNAnQXDETP701Hxhc7iSkdRj8t77GIoESN8Pn4CuK_SYRnYAp4vJ2i-imHH20rEhmx-oFMIXNs6gtKqRAO9BHGKYt3E80cD_H9wjcWZQ1yNG7FsautaWFFfKhEue1LFk73vlWXU3Z-ntYWdsYNhaT0do9hx3VyWBWSkoyjphgANGJnNX9YhlupnMpSMzFFaB3dVBlk8DlNA6jZd6qeWIxzqju3cH52_uDLaryvpCTURH6ZAB1hER3UAleLOX7n0-3zo3Rw7ubmWyBoZt7Mw0ZVXcwPbJSggMQ3bb-4fqT0igH0L2FymQf06UTi_7gpowI8RFGPAkbFnnw_FYifx4uMgGtULzTReXmoovmoLeIWoheR_U6jzs88FdXDTjNQPzk-s2EboSmQejPFZvwXYfTXL7hAW7osfE8e6mosFx_dlbnBQonwr_aTkXkJk7QqhMe9_Arg38RAisVj443RyhgEFTIxu_HZQ4lnGsQa8A2nDcArYOAknw70qdp5hvWs6MkD34tUnEd7mzftOsjkVt-bbNqVYUS-Q6DoAingnU5EE7yeRROG-C3z6b67qxXHY0jnrbuiRbej-9PpooZ1fdO0qmrhXkhJIQhYX2M39coh46cBSewyd6FoNmcL9eMz1BaTAvV0byrJmqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9849efe213.mp4?token=pWs_rjbZjtsVKzANkjWlFLxoD1rj97nNAnQXDETP701Hxhc7iSkdRj8t77GIoESN8Pn4CuK_SYRnYAp4vJ2i-imHH20rEhmx-oFMIXNs6gtKqRAO9BHGKYt3E80cD_H9wjcWZQ1yNG7FsautaWFFfKhEue1LFk73vlWXU3Z-ntYWdsYNhaT0do9hx3VyWBWSkoyjphgANGJnNX9YhlupnMpSMzFFaB3dVBlk8DlNA6jZd6qeWIxzqju3cH52_uDLaryvpCTURH6ZAB1hER3UAleLOX7n0-3zo3Rw7ubmWyBoZt7Mw0ZVXcwPbJSggMQ3bb-4fqT0igH0L2FymQf06UTi_7gpowI8RFGPAkbFnnw_FYifx4uMgGtULzTReXmoovmoLeIWoheR_U6jzs88FdXDTjNQPzk-s2EboSmQejPFZvwXYfTXL7hAW7osfE8e6mosFx_dlbnBQonwr_aTkXkJk7QqhMe9_Arg38RAisVj443RyhgEFTIxu_HZQ4lnGsQa8A2nDcArYOAknw70qdp5hvWs6MkD34tUnEd7mzftOsjkVt-bbNqVYUS-Q6DoAingnU5EE7yeRROG-C3z6b67qxXHY0jnrbuiRbej-9PpooZ1fdO0qmrhXkhJIQhYX2M39coh46cBSewyd6FoNmcL9eMz1BaTAvV0byrJmqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
قمنا بقطع تدفق الفينتانيل عبر حدودنا بنسبة تقارب 60٪. وبالنسبة للقادمين عن طريق البحر، فإن النسبة 97٪.
ونحن نبحث عن الـ3٪ لأننا نعتقد أنهم من بين أشجع الناس.
أكره أن أخبر المكسيك بهذا، لكننا نركز الآن على الداخلين عن طريق البر.
كان يأتي الكثير عبر البحر، وهي نسبة أكبر بكثير مما قد يعرفه أي شخص.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78141" target="_blank">📅 19:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
‏وزير الحرب الأميركي: نحذر كوبا من الحصول على أسلحة تهدد أميركا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78140" target="_blank">📅 19:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0ed57685.mp4?token=SWP8DK5g3f-luDnkkC67qcqUnGHs29ywWgZ_qWEh1702lr9xnqXUU0wp_Kw1KkWmeiKFc54zLg7x8BTs9GXANhG0ToQkHxZz6nugehqUpqzdynCO372l9v8Jq3e3DpyLWTvELpRV6hcDmdSSleuUh_vOCoAJ6_XfRV2W8jCa9cKcl-4POSq-h1L7Z0pRxnMAFxtZnlLoGg42-AMBmVV3dC5r5GR8Sx6Gk6RH1aY2cTwFBQFNB1_lFwvW4r7XhO2_0lMfHc4JBgN_Rl0Crbj7iZGbFhz54LjWfbpnWYqZ-lXqpt5qpRcHT-3Wvzjwt_0ODmIJkKERiLKtUa-nTcNGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0ed57685.mp4?token=SWP8DK5g3f-luDnkkC67qcqUnGHs29ywWgZ_qWEh1702lr9xnqXUU0wp_Kw1KkWmeiKFc54zLg7x8BTs9GXANhG0ToQkHxZz6nugehqUpqzdynCO372l9v8Jq3e3DpyLWTvELpRV6hcDmdSSleuUh_vOCoAJ6_XfRV2W8jCa9cKcl-4POSq-h1L7Z0pRxnMAFxtZnlLoGg42-AMBmVV3dC5r5GR8Sx6Gk6RH1aY2cTwFBQFNB1_lFwvW4r7XhO2_0lMfHc4JBgN_Rl0Crbj7iZGbFhz54LjWfbpnWYqZ-lXqpt5qpRcHT-3Wvzjwt_0ODmIJkKERiLKtUa-nTcNGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🏴‍☠️
بنك أهداف الجيش "الأكثر أخلاقية وإنسانية"..
مشاهد جديدة تظهر وحشية وإجرام العدو الصهيوأمريكي بأستهداف مناطق سكنية في العاصمة الإيرانية طهران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78139" target="_blank">📅 19:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78138">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
‏
وزير الحرب الأميركي:
نحذر كوبا من الحصول على أسلحة تهدد أميركا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78138" target="_blank">📅 18:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هيئة عمليات التجارة البحرية البريطانية: حريق اندلع في غرفة محركات ناقلة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78137" target="_blank">📅 18:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">محافظة المثنى تقرر تعطيل الدوام الرسمي ليوم غدٍ الخميس وذلك إحياءً لذكرى فاجعة مجزرة سبايكر واستذكاراً لتضحيات الشهداء الذين ارتقوا في هذه الجريمة الإرهابية البشعة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78136" target="_blank">📅 18:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ما يسمى بـ"‏وكالة الطاقة الذرية": على إيران الكشف عن مخزونها من اليورانيوم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78135" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2t_CcFFYucbhiExSOnU-QuD76ThpCfAwwMekxw3yFeNlpc5a45AUoIu-nBsAmnWJl3EyDwuQ3YlZVhfLfTiuaoTZ_A-KCisMEjjhCVsduwL4Fy_Y6T_NLioyOovNCSMa2qFjN8rt_1zw3xYkG8aMCGMQzBBiiFZdkKDsEQkzsuMhWc8uVN_6cfN2UDCbcs4fBbDnoMg0T9qmakMeJnR8q7vTbYA_MUJgr_A7XdYXfSuGUH0PWnouQGpU3HOYIAc0M5uPssvthXXPWeqz9WsS3_Qz4t1Eb6EZNaClk1HLJQn5nIIoK9ZDAqOIF-lzHcAbTOcNS631K_PBRPt2hNN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاولات للتصدي في شمال الكيان بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78134" target="_blank">📅 18:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTaAX_JqqJk85XX36rPV_jGV6t75edpwsYdBrzyLlDwEDWiRV0yEmGUSePGV9JFFgHNHDJDfk-j5d4pQ3Q0BDlUrfFY_KsfwIuhHw0UMECduNnUq_JJMOrHEPa5lP22uJK8MOsJoR5KsQqDYKD0vefQNhjO2TWlgEf_4QIq5oxWcDYijvoISmJ1i5VJfde2-R4OWtKygMhUku3DZ1gTOj3bMZrIE4x3lTGNhaJNkIL4_l1XO9M4xtWoZWO7zcE-3feNY_bfCSreoYCWq2Q-N5r5S2mFBNePrGwiWswCXNejezRm-e8_Yq3yhmeFhLaH3k2lSYwq5c_M3zMmsODo7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج ابو الاء الولائي يوجه رسالة للاعلاميين الاحرار</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78133" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ما يسمى بـ"‏وكالة الطاقة الذرية":
على إيران الكشف عن مخزونها من اليورانيوم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78132" target="_blank">📅 18:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
صفارات الإنذار دوت في شلومي نتيجة إطلاق طائرة بدون طيار اتجاه القوات في جنوب لبنان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78131" target="_blank">📅 17:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامب يعلن عن خطاب طارئ اليوم الساعة 5:30 مساءً بتوقيت الساحل الشرقي الأمريكي</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78130" target="_blank">📅 17:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اعفاء رئيس هيئة التقاعد الوطنية في العراق ماهر حسين رشيد من منصبه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78129" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب: هجمات أمريكية إضافية على إيران - خيار واقعي.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78128" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مسؤول رفيع في البيت الأبيض بعد منشور ترامب: المفاوضات مع إيران لا تزال جارية بشكل غير رسمي رغم تهديد ترامب</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78127" target="_blank">📅 16:03 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
