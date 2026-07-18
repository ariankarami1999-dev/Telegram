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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 164K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 00:22:32</div>
<hr>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=qIeCrmXBistWXpqKBNf82WYlQBXAeU4-JB0eVo3ehD-HAopvwH3TKe7fNYxWnzSdMAKEIR-81S5-PsZTAEA-aTTKCTtCJtvEI_Rlq0lC5enG8O0bBK5xPBr1qq-2seHF-4DH1aIxMORqm1RFussrkZ4Pz22Eh8cKJb4BIgx8PeU4HdpyDt2qKWPXORp2SMzQ49sfBpK-UidQT2ow0NIVknPmleV_8FJHSEO3a8d7j1KCpRecMLWcJmOlUG5ZiYC3k11nm7TmMZZMXJRwlEgdAG42IXeVwMTM6SGPMqZr0_Lr0M7nzEZHfsY_XXwwhl3dbs7RuCIBiv1SqYGSY6-CAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=qIeCrmXBistWXpqKBNf82WYlQBXAeU4-JB0eVo3ehD-HAopvwH3TKe7fNYxWnzSdMAKEIR-81S5-PsZTAEA-aTTKCTtCJtvEI_Rlq0lC5enG8O0bBK5xPBr1qq-2seHF-4DH1aIxMORqm1RFussrkZ4Pz22Eh8cKJb4BIgx8PeU4HdpyDt2qKWPXORp2SMzQ49sfBpK-UidQT2ow0NIVknPmleV_8FJHSEO3a8d7j1KCpRecMLWcJmOlUG5ZiYC3k11nm7TmMZZMXJRwlEgdAG42IXeVwMTM6SGPMqZr0_Lr0M7nzEZHfsY_XXwwhl3dbs7RuCIBiv1SqYGSY6-CAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=ZvzkM0eixmdCBewdcORA581MCNyFAJMi0xybiMQYR_pnDfPfHVlCH9vs7BxQ99uHqs-C-FQJh_ULRwDClMrBWlCNYxZP8Ir9PDIsy7qwcBequxgnHDPsmB8QO6lrNkcQKrKWugjAuAhuq9BWYcstXwhldqWYlLK0wxQt5JozUDpfWrkN7TdCi3T5B8YXKUdqkzzb7DJEnADP0lMW-d2hV6hgakB1mFqEeo3dwYN1sNADchgBBwKfEcHuCWMBDf50oXyd7GduMbbtqWS-r4AjING5710Yz0Dhxqj5AJ88FfTxPPcO61tlze5OBAJw3wdNbzgLAkBowrJesI036KhLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=ZvzkM0eixmdCBewdcORA581MCNyFAJMi0xybiMQYR_pnDfPfHVlCH9vs7BxQ99uHqs-C-FQJh_ULRwDClMrBWlCNYxZP8Ir9PDIsy7qwcBequxgnHDPsmB8QO6lrNkcQKrKWugjAuAhuq9BWYcstXwhldqWYlLK0wxQt5JozUDpfWrkN7TdCi3T5B8YXKUdqkzzb7DJEnADP0lMW-d2hV6hgakB1mFqEeo3dwYN1sNADchgBBwKfEcHuCWMBDf50oXyd7GduMbbtqWS-r4AjING5710Yz0Dhxqj5AJ88FfTxPPcO61tlze5OBAJw3wdNbzgLAkBowrJesI036KhLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=TlFSwEaU4H3FB95q_67kAPzZP2bCmStMMwi5n1bJAfnXoMpFpTFdm1Uqydx0AaQTxXZe7pn04Oe-a7hR0ID6Y7RBqvdPBAWZ1AWBvVBDLwRVtrWSIcq7wV_liGwnl1H0nZLYykuX-P0b5LovErTFngYPf2aYAxOA4hpsP9S9_v2E0RP-llCSK_VCpMq7Q9qH-NGbgSWkLzs_H5PkeZYOUIeixpk-0gVbxJKpllVzanjcHST6SXmXD53anxXISjGMqHXhIb_yliMneHdU_LF3iqbMeWM6Vm6IpJhpD6TlHbalINeguDwH8MvhG_4ypunnut9oYNgysSitq74vHZqnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=TlFSwEaU4H3FB95q_67kAPzZP2bCmStMMwi5n1bJAfnXoMpFpTFdm1Uqydx0AaQTxXZe7pn04Oe-a7hR0ID6Y7RBqvdPBAWZ1AWBvVBDLwRVtrWSIcq7wV_liGwnl1H0nZLYykuX-P0b5LovErTFngYPf2aYAxOA4hpsP9S9_v2E0RP-llCSK_VCpMq7Q9qH-NGbgSWkLzs_H5PkeZYOUIeixpk-0gVbxJKpllVzanjcHST6SXmXD53anxXISjGMqHXhIb_yliMneHdU_LF3iqbMeWM6Vm6IpJhpD6TlHbalINeguDwH8MvhG_4ypunnut9oYNgysSitq74vHZqnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=e6eX_BfoCob3SQFb7OAniORPWFvj_U9VOMa445bXgYjOrjm89gHeEu95dkgHG0XCmynfWbOyaiaFTSnTlA3hf7RYN651fsRUpTFy9rFVJ7a20uhMX5xiJTzV-M70YhIQhHqifiNrjOUNbJhXWopjgyIoS8_qySarapGDHROy8IN5jGNj17VSsQRSJjJO3AKza4pReYmuZNWzqPpgNcjtuvZxnrCoKIUnPGHn07oV-mR96xi8XvLQHdEK4iQNheUPg3XG8PFOqK0q17I8-CHmh4h0Q1OYxqalVxyHPG6QGQO0Wkdd0eBlEw4bzY1NafIeS63So44xIHRRPCa_sWl7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=e6eX_BfoCob3SQFb7OAniORPWFvj_U9VOMa445bXgYjOrjm89gHeEu95dkgHG0XCmynfWbOyaiaFTSnTlA3hf7RYN651fsRUpTFy9rFVJ7a20uhMX5xiJTzV-M70YhIQhHqifiNrjOUNbJhXWopjgyIoS8_qySarapGDHROy8IN5jGNj17VSsQRSJjJO3AKza4pReYmuZNWzqPpgNcjtuvZxnrCoKIUnPGHn07oV-mR96xi8XvLQHdEK4iQNheUPg3XG8PFOqK0q17I8-CHmh4h0Q1OYxqalVxyHPG6QGQO0Wkdd0eBlEw4bzY1NafIeS63So44xIHRRPCa_sWl7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=ag9GWAGUBSNtUqeBcV_lNZgyP65z8YobmjCBDJ-urjtWEPWwz1IGTvzfef-DhlW5VYvMZGBbp7k31xSHeBj8oFwNXfhmmF-ObQxUY9MlLb3KZsq5-X-tGYmFELlN9jX8oEFghh-y9qbAAJUvX7Gb5SOdHzvxCkGH1Z6M_ta8U5Hf1cPWXpuChENDp6lZDaB-tEBHDis_fWsp2Ypk2Rc3LqmAHfM9b-jYNO56ybn3lEgzkDcNURyO93D8D8yZ6BP9so6MSUDAob1vG9C_FVGrRBEEU1zfRpywGRANfNBqDFBbB4pnD1l0vbbEb1VllSWaYkkZKw9afpm-hbX5rTHYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=ag9GWAGUBSNtUqeBcV_lNZgyP65z8YobmjCBDJ-urjtWEPWwz1IGTvzfef-DhlW5VYvMZGBbp7k31xSHeBj8oFwNXfhmmF-ObQxUY9MlLb3KZsq5-X-tGYmFELlN9jX8oEFghh-y9qbAAJUvX7Gb5SOdHzvxCkGH1Z6M_ta8U5Hf1cPWXpuChENDp6lZDaB-tEBHDis_fWsp2Ypk2Rc3LqmAHfM9b-jYNO56ybn3lEgzkDcNURyO93D8D8yZ6BP9so6MSUDAob1vG9C_FVGrRBEEU1zfRpywGRANfNBqDFBbB4pnD1l0vbbEb1VllSWaYkkZKw9afpm-hbX5rTHYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csv6U6uOM6e_v6AHQs4BHv_LU_iHHpXZyhFNx8mmfjeyXMZInnO7LL3CnYIlWPWBMUdOOz-90uc8NXIobaI3Ib9VM2-mOmqs9TGy1vdLNYcPoo9IDzk9hacJDzEXB-77y2RIPxJlHEOYcxfk157aSVU67HtaL2RKZclhrOMtl7Jwuz1l4KLWyuB0aXTwxf4RD1dSa27oycg2BFyY-iSrF6Myg3bB78SamlJD9nID2yIx-w9VqrglInWqNFQQDbo9BH-Bxbi1PoallMhyqn1dqkh_VTUQb9rla6v2vfuZ-ts92-8Ac0772DS2aAK6VldIkt4z4KBqllWC4wPIIIaRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=NSe1eJ5yZycOPEwgG42-yWUh-Jqehr2qosxyVU6GAcctt_KCatuLmvdcB-NxhQjEngJemI3VGwx7JWsFQLZ61vJEi8rUCsRy61Z9T6iPCqEYRLON4bmcDQkBdfIBQ2oLannrDiZR-EOyFlmEQsQy0PGzKHWM_pSveMYvW0fB1-Hf895MWya-vHi2xkQicWt9jF7Wx49bNtKINbpH6Ml3mwj1i5ZJtWK20Q2PuiROjX-zqNjAIYl-IGylDeQu3x0gaLj8PBFdto95wZCnwT0JBEbrpUuxNtfI5IrFGPmqrQTWflbxdh18FNX60G7j_f-l4nF7W0s8zEo28Yx9Imy9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=NSe1eJ5yZycOPEwgG42-yWUh-Jqehr2qosxyVU6GAcctt_KCatuLmvdcB-NxhQjEngJemI3VGwx7JWsFQLZ61vJEi8rUCsRy61Z9T6iPCqEYRLON4bmcDQkBdfIBQ2oLannrDiZR-EOyFlmEQsQy0PGzKHWM_pSveMYvW0fB1-Hf895MWya-vHi2xkQicWt9jF7Wx49bNtKINbpH6Ml3mwj1i5ZJtWK20Q2PuiROjX-zqNjAIYl-IGylDeQu3x0gaLj8PBFdto95wZCnwT0JBEbrpUuxNtfI5IrFGPmqrQTWflbxdh18FNX60G7j_f-l4nF7W0s8zEo28Yx9Imy9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=o-Q7rdXRCIJZqzEMpX6hBuoUCufZjkrWl1EnChG4oixw_a4_CTydx26qDgl3tjO5SJb7QKJe4x9ZB_wbap55SX_wdaWOY90GeOi0wOFl4TVZanJyPi9CHeTqY3K5Z2cu-rWbcwg5fKfb_WUR44HOVb-FUvmqRKppkGMfroddLZRdewhrqsY2JU1Ou0bVZs8yotIs0PJ4lHz1bJ4IiinwMiDYBB9a6U1JaHG_c5KFhXanK5hJ9Z-Hzoixt2QJqvbaILk_SyJNTDh2VhH9xtHzgYvXxxyoZ9NKL5TdA8StOgN3uguUtFzaiJifG-zGiz92OkssAzX4rSLYw5yFw1YbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=o-Q7rdXRCIJZqzEMpX6hBuoUCufZjkrWl1EnChG4oixw_a4_CTydx26qDgl3tjO5SJb7QKJe4x9ZB_wbap55SX_wdaWOY90GeOi0wOFl4TVZanJyPi9CHeTqY3K5Z2cu-rWbcwg5fKfb_WUR44HOVb-FUvmqRKppkGMfroddLZRdewhrqsY2JU1Ou0bVZs8yotIs0PJ4lHz1bJ4IiinwMiDYBB9a6U1JaHG_c5KFhXanK5hJ9Z-Hzoixt2QJqvbaILk_SyJNTDh2VhH9xtHzgYvXxxyoZ9NKL5TdA8StOgN3uguUtFzaiJifG-zGiz92OkssAzX4rSLYw5yFw1YbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNUiiFm4rC_wXgErGNvWYDGMQAcCgnTWoKN6NQnZDZM-yXe29_draQLBtxNrhzhigeQ3xjSJhs1ynABZSJH-gDZxVi54cCee3vN3bMs52LlDNnzAeqLkdvtRA-ILe458A5hBKEAReFEQfBIXjLGIo9feFr1LuTV7dG9k9XSgHOxh-acjWr02zOZb84Ay0rFrDreGSm-0aO1k6sweW1tZzwU7b2XqEC8uIsrVeQ2-WyMd4osrT7ATtC0jqNlMryTXcKqtw2zsC5Y7RsolzKiOLa0c-Di8UdudQKd2iDMv3pYFEiuKDDLdFakUqH2858sWcq92hSoBFcyArY79YWQy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDV184eVIkPI6SNjnD2NFpflAbZyPfC7ALcq027gbTNocz6hf_CIE77haylsB7DSyAOZQ-33-TkyD1Utffg3yxQrj9tEmooadiVbEGUNiuvnzyLSa_WQbkC2KAWUDoZFvBjDx6Xk_KlbkYBmNsxtrDfPX2fqVobf6RFWBVi5Us8ffCPfGeo1MAHpgPgsIzeSNcGwpc0nPBF6g0VXIVsIgkoIG-Ud5ZcV3KBSRYSdhRg9MK47Zmn1Nq27yvnjyXwtpJxNZyW3QW3i1lsIITAztOr2SY43ESlUvOF-p70Shk5ZR4-D2N96vZWTmr_NG7X9odR_k67OlVup5x4CmHuZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdXZvt0YFoAcUTb6JfTryZTY7_iTx85LyqBTOqlb51jGRfuZ3QdPoj2p5UD_wMA3sHc3z6mPHlYUB8SlAgTtBU_3FGo0vI_MsZT9Ru7kCHc_ODVFI86mhmJYWqoh7zpUrE2CWHRXRWKCf_WRBmli4it-hTnnUL3NZlTiwQ_34g8fWVaaYOnXmbOuIXnw92NWY3a7LzkoaXFKjAq1GwIJEzefdY42A6izZP2q7cnWFcGnM2ptCBaZ2EmHSchLv2DTKbpZr2I0g9x-Vt4sStnFL4vN-mZvygRn44ZhUvY40EgBdyhHfrcSF4UT8loPDvEicWJCZbPI1q0eUy7KxAVEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH_kZg4aJqLDV1ZOal--A7rXcC1vPUTM9T5VS8i5sR3db7ZkveBCfT1dSBJbMuXR_abNAQVqRWjJILGe-yCnSHTT0oQKgNzgmjEUqWMOYUoTsm2gZZq9Bb4RCrK15XBtWJZT8375SZJVgUFGjQOEcCPMvAuWwN79sKY2LtLI2cNhaHM4yD3T51OySH8yUpXD5sgWIcymlVp9GcuJTj21UDe5QnwNE6INNQVzZSB30Zn9AUzjaCA7RqCID0WBREVKbWqO4Je9UhD5MOJv4rXP4dyswpW7-nV66m2sE6G8-lKX4mFOX-jG2RZgBIpkAJ7y8gfqzeTb8U80pTH703w_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5fxder5xo3R_LS5qV2gv2j9VoaXnmogtYgBOmgNpgl8lvcbzbvyw_4-wk0xuDsC_Pa8_SlAnKYjcLhycrO22nG2lKla2uOALLs3tz1ZP6LeUBrZdqWp2K1ws9AY5auIqGwdScr7ia-sNDfhpeLLqbd662reDgBZ5FDB-X9v-NeRS0OZmTQkf6Rn8MeYP3yVswsDfCyURhCdau1vBL_AMBZvW5VqMo_PLcCo56w147SimLVR6VCPZlNx29_NBV-1sgDih9-y382fJ_6eyByXSIYHlgQADVGJiIxqzF1Hfp0QVKlgZ79D8vlh2hxfLZr2OoDiu2qfT0KFgHdVJqRmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=sj-03Qve0l6kUtf7mkzAFgvM3F6bv4ChxOl12poRjeQzbXtr-fwxZAgh8rSkAvQ30xbMqRftMV6a2Yu02LUM16T4075WBXXmwRrwG16L7zus8sGn9jUTuqvgS5O7qKD-bCWW0oQwlNRZltVIGqkIFlZgTSeClXCJRHhjlsciG5lHzY6i6gBGOMZy6Aum2PTVCf-wYH14VOXofSRgl_PGWLcdA4NXE7QcO0kxHj8v1VBNZobCwQbfdt0WFDcicoqS33g9TVCqxwPCk_jv6FvW8yMVNPxLzn6TBpKLD_HFXtgyKDopZ7pQEG6DJdLTIwL1XvA72wvhqg3viz6gSMIkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=sj-03Qve0l6kUtf7mkzAFgvM3F6bv4ChxOl12poRjeQzbXtr-fwxZAgh8rSkAvQ30xbMqRftMV6a2Yu02LUM16T4075WBXXmwRrwG16L7zus8sGn9jUTuqvgS5O7qKD-bCWW0oQwlNRZltVIGqkIFlZgTSeClXCJRHhjlsciG5lHzY6i6gBGOMZy6Aum2PTVCf-wYH14VOXofSRgl_PGWLcdA4NXE7QcO0kxHj8v1VBNZobCwQbfdt0WFDcicoqS33g9TVCqxwPCk_jv6FvW8yMVNPxLzn6TBpKLD_HFXtgyKDopZ7pQEG6DJdLTIwL1XvA72wvhqg3viz6gSMIkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVqfeGJ0pB-Ao3k3Kx29HhmEFHuARhiLansIKBGEyOS0Nop-Gm4P8QDCqB51rgpSGh1oF4B406Zlg0D7687_MurKw_Bh5La19Z2QyaXnCnBoSGiNo1N4fofrLS7VX_AQJtuHfrpev_6KzoGJk-_jjWReGR-yCHjLqvhh1065_ehMH6ZNLeKFSisnbQICZuc-1rzr_Gk9Gbb7PL1g62pbPcp01hFm78lEKPgOEk-dF7Bq4nWiOD3xcA9MdR0j60zo316NX37gLTJrHvLhbrmBgBsNbr0cZysGnXCjD7LZig5ndB311wUQYlYYCKTP5u9x4m0OekbH3fY02JIvOQWPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=f_NhjjZRUZ_FhqpeBVAJFW_ElNiif1nz0td8v_vdDPvYolrJYiE7eJp2k1O1kLOLA9QyPWME-CUlW2SPJBC3hVWPNMg1TZIv6SN3qSXOZlz5Aw8mzMA7vBkIBP6D8GpmM6ay-LB_1DhhM_T6jklOkQlhSQjC6hXLXrnZswL38Fl4JHLVeC9NBMZFVqutogtW9u9k69XBb3RNSnMBI2oTWH2_Ix2UYFHgjO6_5QmWgMnH9r1otLlBNIphC-zbH-vi0GgujY6wIGXiTolstCX8NqhaD6ycgwSZoutYe_wFnjnu3-6RlO9ZEzE6jU9lOrqaW3DfuZ3vBpPREwt11PRUDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=f_NhjjZRUZ_FhqpeBVAJFW_ElNiif1nz0td8v_vdDPvYolrJYiE7eJp2k1O1kLOLA9QyPWME-CUlW2SPJBC3hVWPNMg1TZIv6SN3qSXOZlz5Aw8mzMA7vBkIBP6D8GpmM6ay-LB_1DhhM_T6jklOkQlhSQjC6hXLXrnZswL38Fl4JHLVeC9NBMZFVqutogtW9u9k69XBb3RNSnMBI2oTWH2_Ix2UYFHgjO6_5QmWgMnH9r1otLlBNIphC-zbH-vi0GgujY6wIGXiTolstCX8NqhaD6ycgwSZoutYe_wFnjnu3-6RlO9ZEzE6jU9lOrqaW3DfuZ3vBpPREwt11PRUDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BVlUA8Eam1yHTSz_ICmqDPmEgeNDAuVTbcqU3xLvmMo-rAMwg15KwNGxj0j9zVAkn-D6vh5NRH0Lu84vf7pDNsQwiwcY52lTuihzV5rOfM9Izol8L1rGOSsbmQqtpuH-q9X5eo2Kim62cwNFW08Yf1-tFKSPTKEtwdCvrLB1-CoQXvx4ZEVuSZUDql7WdXiNoHTfoZLxBAXXpuNdYQPHV2ASdP7eBuRsvJLLEAzdlIZILw6BKsq-UalyEoqXd52jTFCcQHrN8QoOsaKvgNhoOgb5FuMTjHrjBZXaOcRttLUy4eAKvcbuu7RCbeW8g8CFHp2xjMm4sfpCx7tl4gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMeNRZMKmdsZb_ExCKl6Z2pgucjKdIrzC23aVd7Lg16ipJiIaZaxsHWfJpHoMiI5r1HTj71c4fddEKV46XKX4_5G8TGRHw0MKS1rbp-B9SmSyk2kvcilc8pZLJMAILJNFmfLC7Dg-p02ZWev8YZtvghFI9YTE2KE0o23DxQ-CiclCaHWpYuGyUvi3ZTMQYtMPM3lSBBkTPTGZgKm2olFKYxy22ZDjVbw0FxDkG8kZu0CNvZBPUQnQXZYVhPp-cEMsrwaDKm4qdl5PWpNX5_nViHd9PO2wDcOFEXH9cPqwNaPNiNnX-W7xEPJIpPcVRBSgsLXQD6Xb5jraEcBDr0mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMHBPDRetBGc4-g66Ip5nLgAO82xOgrweNwGQip6_vCpdS-eahlMIKHm04QwWdsYGNfFhmMf17s5VdhOlC3M-6ErNkV2tZIkik76-28NdVD3IOa5H-f9wOkrniqWeOCtcMsk7QqyN1TRA0c--yzkipYSiq-qPTxkQSndydOgrtHWD6yiej3Kcfe_Qub6YAwHUangHhAaQODfU_Bwwo0QjrKgNRjtVctYVTBRkqBzXCqQyclay_0OEa18M-aYT04Iut2hhC4TgeSaRVjDtKuiVM2oYtiG6Q0DE7a8CaUHUGPP0HNb33SlhFHQ4pFoKy3IGQXSOQty9kz1oL8k5yFyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAHwWZcGQk9bTEPIAfKPO3pOndfQQwHEouwbOs6WPYwahNTkINmELN1cbqQaE7BT8UbCMaAS3wMzWBhNo8rZQjVR3BVuzRNCPNKEuRb7hB0OHc4-lI5_g3NSpLcHRjQqhXnjIuyQpRGwzpQK4z7RTeoOYr0hM91kIHzhLrVH6ugo05QGxZ2mjgDH5Ahw4D1NAPiJS_mOnvHIiNFoliLQmPRBCdX5NIYG50M7LHzlFRGJSdrbV23MK27soloafsPzsgtaPQcL9NMl3nSMC7Gs6lwAova0R-1gvYuxAqyiz0Axqj2GQyWgkp8KTZgxTzO_NaiHZ2ALJCDIRZMp38aBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el8YWblstOLTJChyvfOcg93SjeaCVsL_hZRF93qlInHSjDF0fptgLupC8aPPGy--pvq4yMMNt3TVLZajI_6yt_-wk-NSATPV6TWcYhXswi46Nme-BZADsVxVaJ5XdJmABjXGfI50wRV9gKeYt7j-u2Jb_4utMKk83udfpY1dQdtGJtlvwHNqnPSA2gWHSnWKtjErk3QV5W8ZMiINvrZOj5rv_6AUE6t-7frPqi4hNne08EXa3qIqSu9klgShUCuTGPWNpvurBVXik2LBuRJ3xzUXjbGOOyEmGh2LFyOeILZNsUw640yF2G5gX2vyEz5cXqKxTru8ZTpFDCLKl6zcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4uTcxfBc32O5E4ovfMEV48s-U0QFHiUX6aMXqb2qzTZa_mEeOhYCz_5_XIybc8hwMwHTjH2-1H0ajk6tOXt3Tec2iNxxKxpehJy5L_CZWRNNSHohzfLp8UEVFk3CdZZOOiQ9gOCfoNtRvwbuMant9GigFICOf31d73Y0dAM2yNv6-Ws2VGa5lZGhaCzNXFxXapAAHoAPuc9fQyMi6xZYGEL3IITyyZONuxrV793sFNzD0i9VKDHU8skrau22kuYM8QGFcwiMsyKauyEtiaL1Rk5fd86mekrjAu5TVQH4U_CZYUgCQIiyyTM5D4TCut0Jm-yHgGMZNEPgvUdMUEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olTG6cWd80pr_BAw503nfKuLZypZOeMP8j4VDVJPk6y9qB9LrQIs0VVJvkyYeMG8N6NXtdyv_1rjOpvu-d9dq-2PLv3jq1ioR0O-ZQm8aspVDSog3C0r4jZJv-dsvRU-8sTrkd4i2acphWeh-tlNYHDnnQlxGvh58FFySBW_zNocM0j5P5gR89M3rd4JXoSX5M91xu6RGKgEiJrDwYpYHGBLrI0jHV41QtaTR2ZKw3CJwiQ1NkuZ_9VMrV36I3obK0s_KWH9DBOI4fKNMMLLu3bshxcqeF-LRtxrzCi0eIW6vWGCIlirFOHiRDLAzTfScTn6l7W_4QuVxaBEQKEa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfd_Q6YNJP1grjpJv5GKYLKv2JcpWdEfV1g-3V7WNoatHRXzM8PF6IsVM3OYuTbgzNHVbD-eKE3FcTDZCAN-DLM1_bN0g7HCeLPraSarEtyRdiVLlCVptpqAtzV4dBamRp9T4LG2XmS7bJN6erHaxbWt2EeoZcczktfqUrqibUGoJysfYqS6tB299qXg8UpcOL53MOf71XeH_E1Qy1IZNZOrSlnJN_CW65AMCqxvq2MeBeKpWPm46CuBzSdj-uXYOCVbjs9z997NmcmPoCD1KUDhw-7rEAoiPU1ky35lCxnN_24AMn6nHj8SySwgnHeDQ8DZEkKPKgn48-dUPWewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld_XHD-1Tx6e-hHC2j1Wn4orUZ2s2nX3uzqOkzLTu7gac-AZC1wbuhCbpMiNYgeWG2f_gKP5v9bqsx_iHg9Vb6i16L9iNEjQnr68-lAB6IlxbaNekjNdD7Zwe_kchic7zdUqKHf5k-p-JS5EBI0O25MVD9jTQneQQcEz31gZ2i8Rtm9DvKeaJsJaMe5iwWzF0_xaoN-wAD-lCMmlQ0_7O0cQ6LiTf8kUcjCsV86qZodepeXLLHy6HMJV_JPmxQ1qEmTpdWpLNBXstkto7Puyo9GbwlQsPHsLKfkF44e6vhgqugjyTdyNZaDsbsOKhqhXCeHAHr4slDXtH2YJhXeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM-LWNTjnmcyuKiYgL5dsoS4G-ezxUb2ZLdLJk-UR5GEP2PWjbVRMnEKk5zuvCfulzlh-3xWBhi6eRS495rLoJEUUQb8kHDOEG9fXF4l59RkpNvvI8q95Ya-tmpo8ZU2wR8RvAztmFYmglnTDZpgrpg4uy0wRI4eDSsPL1rx6w5Lw3s6wFidrT5I3iUOM0Hjmaf3X3iqI9A-tXbegRRpF5KCoASuwgZqOr4BldazmQaLDSQDPP8AU-O4pWClKgTIkjMxU_Pkg2PJlPNeRw7TLerShNKE5ziFP99Nv2IyKZjrpl_OBQYp-re-eQ1HuNZoS9gOs699yISU9uC7EWXxsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=IPlbJfHHmf1MuneRkLw_sDFl5Ag0yPZAM27JG_sBjRlg2JS7Q7aNo3Xr_-OxBHmdnuTOhTWlR7zHZXhRy6aBOpZiU8Vtvk7Hh8qmKTHZqQFon-Eyzz3xx1v39LLnzYqo4dnegZi0XS96H5a-p3k8XtbyTmOwBbk-oiFIV4rexi8MazhR11OZt_DFeefYHU8CKmAvtkaYueobx4V4oTB4rC0VhUiYAcynHpdSg0Zhr_OvfF3EqAq2Jl-1G8HPjbSG54cEGYTuY-MymNGe37h3RkLTXDpNeFLvXtS24xWcM1byiYrGHxaKcT3nDiaP9yk8PfbApdew2K8nygQtmjgl-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=IPlbJfHHmf1MuneRkLw_sDFl5Ag0yPZAM27JG_sBjRlg2JS7Q7aNo3Xr_-OxBHmdnuTOhTWlR7zHZXhRy6aBOpZiU8Vtvk7Hh8qmKTHZqQFon-Eyzz3xx1v39LLnzYqo4dnegZi0XS96H5a-p3k8XtbyTmOwBbk-oiFIV4rexi8MazhR11OZt_DFeefYHU8CKmAvtkaYueobx4V4oTB4rC0VhUiYAcynHpdSg0Zhr_OvfF3EqAq2Jl-1G8HPjbSG54cEGYTuY-MymNGe37h3RkLTXDpNeFLvXtS24xWcM1byiYrGHxaKcT3nDiaP9yk8PfbApdew2K8nygQtmjgl-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUYtBvOfJ6oGNNVAh6ky6lH_RiRM_H6ziwcNYvlL7pPaAShJgc--Ea033F2tgfHgyiU2DJiXFEI5MMTTFYz_tDu1305_Ykj27zXggYfC4gogCVDePovfz0WwDb_ObbJKYuq1n_MmQCO8_KHvvyZDUGlaq94o92S0JXbIyhejFtWkGtKPu_O788-LI6DcLDub5V24Cl1re45ELUhdqohs8rA5sFcWExIphWnGJu4kCURNtBKF6n5-aoawWzw4oBq8daHniOYZfZ3zSUQ7ANFyNNaOjvd_6foTulu23t21P5TFpr0o35HNp3YqD80BvQuV6QLMbbsxMKjJjqvw262M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvM5F7yTQx0rMywL-ogRkfOPKHer24s0Ks6_0cwRMEkKObWQ8QEFKFerunVK6T_cus_KmI_EE3keZvrlE7n1r1rCHXqGnhnJOD3qaG805dlydwzLf0N9_R7cCnlIwM8lAgc8k6ULkFy89CVqhXXxHwqIopDP1NXmJwluj6CpslyRPVGJjq3hs_B5dibnSx3pcFvS5Sr1IeE1FJxq0HTjDvXOx_LqjQKijz11c-tAcGpfUAPoJVZQIVw32wWUS4LpOmGgiXk8KyvRk3LMX_cdIesyrDb3Xs6oX8POsWl9KsOtKjWh_Dj8Cx2UD7ES2cgFOgeIYqQYuOpg5lkHS_Rdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv59XJj8kM4ktrREvKoEOvbluG51eWYI6LZXGgsu1TenBOnGy2eGflCecM66PeAuiz-L-tAxFlko16lUnN1rwWFdNLlpggXs9X6We0M_CjE9r8EBRsfl6HdkuUDYuhjroH8AFA2biJMGNSlNKahn_wX1Qoujru-nDZczN-061lB0_eEwKnF2bWLua-7a896Vpqa6i57yqx8933OJzWisINBE5I2dku8I6olHCo2dkGt3_uU5L5XZJbIe-LxVLBl0lHCmqvSa56j4XD4uobEbdzCOhj8fbFQSblxXQxbxGF47lC5Sof0A_1ztrckb27ogkNckCMOOAJZmt6SpAPvLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXMXEEVbf-OM1pbIxoFchx43DhbRVWuclZ5K6h4eKamuZDNA5e_GLyrS8rJxpLzKexK5F3r2PtscYchCZGlV1cQ8TIGyFfuZwBjjV_BurstCT-26Cb0F9C2ZLnD9sxXKKDl2fJMdYlZ66zBAuI831xTAdJUtXnUAHHwJUxoCeMe4py_6fDomlka0lgzlcHpITHpDO37tvkftlCETZxVFr2xyW77j9bASnUx3j8aJUEMmmLT0l52lDmetOUjQd9JPiFaypZ_TJDLNt32VByclL1GLIU3eU-WxSrt3hv-28pXSsHEqWXuRc1hJmYlGoXTgJdyJRX8JvT3-yP4ivywDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEvHEKBpx-2CgI8kXD3xsAzDahQs8B49xevwbUkYkkSH9CM8nrIDsizj5MmrdhGRVzXB3g47GJvyJl8cTTOsVr-IWEl1VrBV58f8WmoJHtdL56xmMP1uTjjQRdnWzXO1o9z-6hfRnKjqPizKqDq5onKoUIW8gcAMfmYhe1eF-AE5coXPlCwKGg4nokDs14IClggM3UQfxQQxnaqY5J-Cxvtu0tPN_eF51fqGYOoRhy-1-EJnoG6Fbw0vY0Up1Ko_mWAPuFIdJFur4q7PEoG22LMmXknxOOZamQ_8WlXtMaHeeRG1P8ucOF1Fbi7QEyVtGHk9V7FkiT6hl0uoUuf-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=kTJccQZ4RnXLWzHtK92mpuCqIKmK6Dk25HX4ePBU2hBgaZyMVZcfiJa8Cpt3U3MQ1bQn0LMf4XJE8FwuVewhEo1EfgQPJiVUjG0pbk9Y3fMmQeBBM_ow2AQeqSFWB6azDeSG4SygwRpGaNID0be0j2eYRemp3dT8QLf80LQDmD8v6Gni9FoXPMXaeihG8P5-V3CZwMfq5jzTKtq4Xcj8pWGwMRKCrHNmFfvaYaQovZEG-mzghzTR-yrZKtTzz8x4aS4_urO0I4gFe0B0mNWSugGClj1KEvmbT6NFt93kdmPTpBc7LYbeN7opYwmUqenTB0WM6MasAZuCVT_CEZCXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=kTJccQZ4RnXLWzHtK92mpuCqIKmK6Dk25HX4ePBU2hBgaZyMVZcfiJa8Cpt3U3MQ1bQn0LMf4XJE8FwuVewhEo1EfgQPJiVUjG0pbk9Y3fMmQeBBM_ow2AQeqSFWB6azDeSG4SygwRpGaNID0be0j2eYRemp3dT8QLf80LQDmD8v6Gni9FoXPMXaeihG8P5-V3CZwMfq5jzTKtq4Xcj8pWGwMRKCrHNmFfvaYaQovZEG-mzghzTR-yrZKtTzz8x4aS4_urO0I4gFe0B0mNWSugGClj1KEvmbT6NFt93kdmPTpBc7LYbeN7opYwmUqenTB0WM6MasAZuCVT_CEZCXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALSkiEEU5C9d9yoyQTEGDgY8KyE5pfsslmhfGGVnmzQvVNPRDX3vCHX6bUHaQ9N81HKdUolwfdc2cE6NXXF-twq6r4LvPFNtzrZRUTEeEMVEqhlhQ_yJqVWGnkMyCJ20_mGIX9qp3tsYbPlSNeurcvpdVl1bcFxt8Ra5ZMbYX_BdJ-ALLcN1Ks9s4JVMQIcn8UbGfds7bbHo4NBToU5fe9j_0WQSOiQgXsCFHiBmcycRj6T4sFGSW6ZNM7JRmKEorpC1HC4YSClctcwp0RiJvlYgE7L44804tFXJK1i1KWJ48qQrjaaLXM5Fu19C1qSVUSHwz9KAufqVrhnZsO76Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8ejywkd_NW3jISGet1bOF70Sf7qPmdBiWTKFJ2FUP4_d1TgfXJXd1lsZ1L3o1rnUG01rP0UtodmpFiO5LCvvV9rlZTqUw7HdD6c_pFB3JM9w3Qpu6szmajVBQSusjMXZSuxHsBw1XbW0RLLSGKqrDnZkC3KqAXPBQ5dfIEP73zOcRmQDmdWUydYCc3-gRb3CTbdjr03AoQAPdiNpAbJWorrXt8LSb5yGwt-1PDsf64W6kLW-Ie0nqzbk4cNca6Eftn9EqweTIE9GuDO3flw0Q2-9MTMZk74x0OwovC_r8whFtSU7072yRDb_20bA18lkksyfMVrcT74Od59NJ8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WY0aQNfHNQTI8Z1ulTHrRJlmj5RtVCTnemBpdZP4t0na0N878r0hDr-X2ff6LX1NyEk9qjEElePwJYEOWJdLt6aYn9sIbHLNn4M1lOzsiPxOFVm4ikoo0QTYlBjGpf6gVT5pnKh1M2z4Gj4qO1jZ5mhJVl6hg-wlxBASHRUXsBghpbtbPI7OO66IVAWkTsst9EZ-JZ4r1S3ui2DLYrI59x7z1I5A_hbVtLiJ7LbROdW-RwgwEIlVqjal1kSpYxhLQNRLmL2wIsxNLdjEwQSQ3_4yR9qBHUXyg4PRUAWyogPA0Fr-JnHhvxgCCME55-wq5QLG2hf-qEOd1tneiN0Alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmHMolloKOpUyFLJCdcM-L4qi6FTp_AY6K36D9_ucBP4P7LPF3rx0F594NHowEdH8aIW_XSqDlS0-fk2jFKLyBetZd89wIgFvDKEa9PQmEeAIv1CuAFpstJelMOWSBjgSnaQWiwnQgd5soOvg0IddypBf9lXcheDzwd0aIXRa-Cv5T6KdaKGrVrOFaHe9kewziWHG84TzPuIQcWqUpGfjiM3dZYl4ddNjwvOfjWWXgamE16UOqj4akes5m3D73o2TgoyljoRROT5VXUWhUzbuejCR-B76DdBcf4oM0JrzBOScZpOKq2YbpU-xNI9l5fE8F5YNcX8_VvIlCAI2_whhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=cJDsU515JYuzrykO1nKW9l5ohMhaK_K3iFjoydtJq_Fh_eWtz7YfkqZAAFoUbl-gzXffi_XzmPT_UfWHBdBoEdTtLB9cUUAYwETq-R2sPOqBPQBPaNpvMS4-z7aQgtya3f_NwtTVwvj2OJNiRsqtKcR69hzCieAAIwqW4zY1iuLnG3aqWjsfO21jUCV5sWFS6h2LzLAEOTLGE6IZ9YStW0y_Fns42F--TBIs1AMWpIpz0AmZFB6iw0mgS0nQF4hF8jugnfz2Btu6k_HXLyCqoL2EZFbyhbzRu-IaXRaoRkmGOKyxg5Py2Q6QVwicYJyUNNBFIv4TCBbAf2ImfLVhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=cJDsU515JYuzrykO1nKW9l5ohMhaK_K3iFjoydtJq_Fh_eWtz7YfkqZAAFoUbl-gzXffi_XzmPT_UfWHBdBoEdTtLB9cUUAYwETq-R2sPOqBPQBPaNpvMS4-z7aQgtya3f_NwtTVwvj2OJNiRsqtKcR69hzCieAAIwqW4zY1iuLnG3aqWjsfO21jUCV5sWFS6h2LzLAEOTLGE6IZ9YStW0y_Fns42F--TBIs1AMWpIpz0AmZFB6iw0mgS0nQF4hF8jugnfz2Btu6k_HXLyCqoL2EZFbyhbzRu-IaXRaoRkmGOKyxg5Py2Q6QVwicYJyUNNBFIv4TCBbAf2ImfLVhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy762Imlbe7PEJjmPdaUn8T1KsXNmkxZasAZaW81Ih385WNUqx-j6kNiFCQ3VEtYSw6NFmLFNw-d0VVpphGYOWF6uSCGOTgmoLwGBhzC6MF9JUgvtNn78J6wVLkEj6aY9U97yPad3m09_AqnxcnYKIJqlqa0Xb-mWvuGCFcWvy50U2MAfbflp4vujzMk9J5c9kUshjxhIJfuNhzG-yKfeMnPT4KjYtFuOpPHg87oFdPx6B0k92wMSM2zBnIdRCqdLWgS1k5931LxxNZ0o-zlPZJKyF1S1A037o0GB1PvjGShRd5xifWfwDHQmhukzc0xRl-t3JSv3iqOQ1ni2ptfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=bAMmrV6zNLkMdws5LdqH8O73XQMN0Aec6v3oktFxI73wihO3GgmCAEg7rWvQIbH7a-87xBNMjRgu0b3zCziFC7AhGm1KPWkoM4ETV6JIHbaF5ffRPeiDx0Bxpc3KS0isawU1TqZ13X0pxJYN_FXbrdxEQcAgSXwm6x3wmFEo21r9BdQdHmLwUqsg5MMbc6EltUv63GPOsJTgolZt-mt-OVUDg9WO-xXvGQLbb7udqQenKuczG4nvpBgHBk4Hj_J0_W4ihYeWcgHLAkY5s2tFhX3k7zIGnj4b6MX_s30KJZWr-P18mE3B4-wlS91Bxusj_DWb85iFoLxB0xBRuOhSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=bAMmrV6zNLkMdws5LdqH8O73XQMN0Aec6v3oktFxI73wihO3GgmCAEg7rWvQIbH7a-87xBNMjRgu0b3zCziFC7AhGm1KPWkoM4ETV6JIHbaF5ffRPeiDx0Bxpc3KS0isawU1TqZ13X0pxJYN_FXbrdxEQcAgSXwm6x3wmFEo21r9BdQdHmLwUqsg5MMbc6EltUv63GPOsJTgolZt-mt-OVUDg9WO-xXvGQLbb7udqQenKuczG4nvpBgHBk4Hj_J0_W4ihYeWcgHLAkY5s2tFhX3k7zIGnj4b6MX_s30KJZWr-P18mE3B4-wlS91Bxusj_DWb85iFoLxB0xBRuOhSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=WaiS74u5VBC9aWSGS9KresafrSW0AYX7K7UocADhagexBvaM9hlmestfJP97TUqos7lMmWlrFZHTX5CvXBIm0BqC-pMa_XLAuPMvhIdec85KmTtQ1vW3gbaHefKn4NeiGRBOJQbjcpB53qZ_9cwgnlk7ahK8x0lIU0H39Ul_VlQWyHFEgyR-UitbAflXIVivp0mHrvmOWyKaJAZMKjb61vfa7kNbhGXyvwU57TsP3pJl0PTZlKkA5FSJx7yKJ7aWaWFMrcui37YL8u0FY8UT9cgqaa5tDC_iMwhSBZND8mRfbEH8YT44eOFltWuFealmEGMIKtjp2-iC58eR0WaPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=WaiS74u5VBC9aWSGS9KresafrSW0AYX7K7UocADhagexBvaM9hlmestfJP97TUqos7lMmWlrFZHTX5CvXBIm0BqC-pMa_XLAuPMvhIdec85KmTtQ1vW3gbaHefKn4NeiGRBOJQbjcpB53qZ_9cwgnlk7ahK8x0lIU0H39Ul_VlQWyHFEgyR-UitbAflXIVivp0mHrvmOWyKaJAZMKjb61vfa7kNbhGXyvwU57TsP3pJl0PTZlKkA5FSJx7yKJ7aWaWFMrcui37YL8u0FY8UT9cgqaa5tDC_iMwhSBZND8mRfbEH8YT44eOFltWuFealmEGMIKtjp2-iC58eR0WaPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=pQoz_6XmTDsL7Cl3j4U9qoBxkSGVjKGFlgOD4L8OVj_NqotVC_vlWoaWRzzt7OZb53cCxLl9hhbo46fG2uWEp1G-YJizs33h3vxwngfIt4MiACxpMV7GdsGwFMuzbThmK3ZuWM1pvJXiscRjxY7Ilhcnl_umK3woQmxttxZP7EWJOLA73K-qWh5-WFEAitSZIp_WhPLqo1Md4SotD5jaZVIuFKfPD2foiBe1XWo5ri3T-CB1Tx6IgcqwiUz3PTYTxFwuJraWsvarZ1_624IBvLp5VFY-lfrE8pAXqmiLyvaK8Fod_NTTb__QSri3DKfmwGPaHzD4yQEpaHyGm1H8HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=pQoz_6XmTDsL7Cl3j4U9qoBxkSGVjKGFlgOD4L8OVj_NqotVC_vlWoaWRzzt7OZb53cCxLl9hhbo46fG2uWEp1G-YJizs33h3vxwngfIt4MiACxpMV7GdsGwFMuzbThmK3ZuWM1pvJXiscRjxY7Ilhcnl_umK3woQmxttxZP7EWJOLA73K-qWh5-WFEAitSZIp_WhPLqo1Md4SotD5jaZVIuFKfPD2foiBe1XWo5ri3T-CB1Tx6IgcqwiUz3PTYTxFwuJraWsvarZ1_624IBvLp5VFY-lfrE8pAXqmiLyvaK8Fod_NTTb__QSri3DKfmwGPaHzD4yQEpaHyGm1H8HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=Bnq4I0cDCVyhoyr7_uM-bDxdBcXPMDCmpPuXpEXvxXDid2jVb9hB-lKTK1egfOOtWpkHCTbvibCZBmLJ_9ppF2uQGQE768Z7l4Aa5yRlMd0Hkt5_Y3GTtlsKK6k9itpMbGs5XVfZ34rUySxP86wefQwvy4CjXTJs5CJHgMH3vAXWQ7Ef9zAPpDdkhpXeeje57ojMY2qPMf--4LcrI44D_O6und9btZzwORDb7Dd0mGLvACiKxqteD5jyQakZT-H6dvOgw55PKCY7SPjHPorbeBDMJAiO0az12JBcVB-Tb5yTeAyLIt1tqBZwBe2qMbMPNzk20fhNtojoZoMhtvbwJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=Bnq4I0cDCVyhoyr7_uM-bDxdBcXPMDCmpPuXpEXvxXDid2jVb9hB-lKTK1egfOOtWpkHCTbvibCZBmLJ_9ppF2uQGQE768Z7l4Aa5yRlMd0Hkt5_Y3GTtlsKK6k9itpMbGs5XVfZ34rUySxP86wefQwvy4CjXTJs5CJHgMH3vAXWQ7Ef9zAPpDdkhpXeeje57ojMY2qPMf--4LcrI44D_O6und9btZzwORDb7Dd0mGLvACiKxqteD5jyQakZT-H6dvOgw55PKCY7SPjHPorbeBDMJAiO0az12JBcVB-Tb5yTeAyLIt1tqBZwBe2qMbMPNzk20fhNtojoZoMhtvbwJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=ljugpT6cHmlXyFXvq9PyAsW20cIpjd4ytInXmYov9MpcZ_VGwYtS88V1MvKxGU0F2Z-ouTt4JkGPgDCZbncHvgHRs4akjKcOyQm8TK8Ws6zn9cI8CK08d-iTSgB4NZgk4n4_79i8sLaBeYzUxWhCJcLfBZsHC8D3Jim5ANg1kZ5d1ueDNhN78oRJ1-69ixs_bN3iZCauKFewYDGq77OBb4y6GJ6BLL2CiXblZSZw-wutpaDt4qrDEXOmNRjVbuvOM00jkZZEFWJxp2TRRUSqO2IeIYxeMBrqb1S4nVbDakVXipiQFVi_By_vGKZ5awsPXl-y0mwqzKevtB9oiBBVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=ljugpT6cHmlXyFXvq9PyAsW20cIpjd4ytInXmYov9MpcZ_VGwYtS88V1MvKxGU0F2Z-ouTt4JkGPgDCZbncHvgHRs4akjKcOyQm8TK8Ws6zn9cI8CK08d-iTSgB4NZgk4n4_79i8sLaBeYzUxWhCJcLfBZsHC8D3Jim5ANg1kZ5d1ueDNhN78oRJ1-69ixs_bN3iZCauKFewYDGq77OBb4y6GJ6BLL2CiXblZSZw-wutpaDt4qrDEXOmNRjVbuvOM00jkZZEFWJxp2TRRUSqO2IeIYxeMBrqb1S4nVbDakVXipiQFVi_By_vGKZ5awsPXl-y0mwqzKevtB9oiBBVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=cgFFGXqlWIyf0R4JZj4jP5Q2iI0NUH2XAMRHIkQgOrCJEpWfCVH1j4TlTj4R7QKuaPpBysvP2znRGitWMlM_lgR2KZ392amu3Z4Ae_uDhw5iCG9g9bjJbYlX6rACEDMBHm6LNLLouLQIFwGywDhAFwPA4uwd3PldT9bqnmfWdB_Ru3gUoTEH499P_otY83Hzt-1vQ0X-k45KJRtr3nUulIn0xf_2zZ5n9zy27A_CxuheSZU5G8eXYMW16KFQF1vveIewVeGae_sqnpCLSmIo6QP5BFXAvbwY7A98x2MwxjSzLobaK1e00Rj5KokVePl_dHGbq1eQV3hnSHSAuQwJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=cgFFGXqlWIyf0R4JZj4jP5Q2iI0NUH2XAMRHIkQgOrCJEpWfCVH1j4TlTj4R7QKuaPpBysvP2znRGitWMlM_lgR2KZ392amu3Z4Ae_uDhw5iCG9g9bjJbYlX6rACEDMBHm6LNLLouLQIFwGywDhAFwPA4uwd3PldT9bqnmfWdB_Ru3gUoTEH499P_otY83Hzt-1vQ0X-k45KJRtr3nUulIn0xf_2zZ5n9zy27A_CxuheSZU5G8eXYMW16KFQF1vveIewVeGae_sqnpCLSmIo6QP5BFXAvbwY7A98x2MwxjSzLobaK1e00Rj5KokVePl_dHGbq1eQV3hnSHSAuQwJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=AzWcrk3x_P9En5Ftd0rxunHZ2c0ZaWthtg1docaIGEbtvI45UUeSB1OZDWguDOnxFOQBURnfs6EzpbLT38GCi9qN7eOI_9qBpRWL275gdiPT-WyD0DMAZvC_W3NwYMI13rJ4H6pAAfPzcj7uLhB9hs3WpR8ZIoExAvczDBGJrnpnPQzLRUO5hdLpKNVHPcPlfCZDoSXlWokJvpIrP1n2xX3nyVPIMkZdUyakkYx3XxcH0WXulApQNuqKhO847uQRtpFUR-ed5cgQtbulAuB0H-5WB6lGM7vNDlS2aEmEh_yilCNhfKtOx_7aWgZE__zn7LcSMisuWpKFiX9ECsjwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=AzWcrk3x_P9En5Ftd0rxunHZ2c0ZaWthtg1docaIGEbtvI45UUeSB1OZDWguDOnxFOQBURnfs6EzpbLT38GCi9qN7eOI_9qBpRWL275gdiPT-WyD0DMAZvC_W3NwYMI13rJ4H6pAAfPzcj7uLhB9hs3WpR8ZIoExAvczDBGJrnpnPQzLRUO5hdLpKNVHPcPlfCZDoSXlWokJvpIrP1n2xX3nyVPIMkZdUyakkYx3XxcH0WXulApQNuqKhO847uQRtpFUR-ed5cgQtbulAuB0H-5WB6lGM7vNDlS2aEmEh_yilCNhfKtOx_7aWgZE__zn7LcSMisuWpKFiX9ECsjwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrhJ0I97sfuKgpSBADJNyZlFHGFJRRQGCITuh1c1aASRdljme-A8PlsS4DlnPqsqZwpZBW_JqU7w_eZ37kpjqmFjHJWpTHIVaFiNMMwdt5fl413Zy45zsm3E5ll7GOWqltU2Kk9AZsfwOlo86J-0VPPdkixhQn1GMDpR2WQml2bXJn9eU6Czg0t_LEwEBvhusPOuFJtYWfNGky4kc43eCjlK2q3o3X_hGbpcZvprbs68e1-wk_u7jFJcSwWi2it4xkQMd79a6pe4WFM5f0yTc8leVGUirnl3LKndSZKbHGbNRNNN6Ihicx3A67SOZrpIeMAeaXBeDZRgN-dT2jh62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
