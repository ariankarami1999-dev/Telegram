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
<img src="https://cdn4.telesco.pe/file/UByV2a-t6w3YeXu1ZRlVUdIWFFjva2Thc-sFF3MjeiyhdqTe-CMg0k2OnAA0d0f7w7JF6L_f_447-LfZ7MwCkM7aL049ON4OKCnw_VtvvaaeipqCTW8HLJ6a7YFphPiNwD63wg7KOLwXrsargPEqsJ0rhkGRDM215YvYDacShNSqHnTOYl6ljTtLnhr0H4e7GAsHY7ZuBEO6O6tigv0ScqiZ3rXnoHeQqEtdCCY6rfj-tzT3a2hq5l9gMASwJpNzq8wIbPnrUU704gw3vGyPdhMgil5IHfQwEdwOVUw_4nuPJ88agp7s46tDf-ZZxvWDyOTIH0hy2WhtCYlLRsydPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 22:31:10</div>
<hr>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 243 · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 551 · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUR1_tqSGIPxuaXBbRYH7TPHI6GRXeZRnViXd-MGtjgfbXV47EBwFr-5SDaCaMUCDzvog8XJnKyqa2KMalkV10U4MsE4xdnyk26g50pj7nTuDSGr6mkEx51FyqGmin_MwNRtyDefZiolvxDqep36X8fnedEdy22hSRuEwEM8gCzl3aSGi2IOk5c8IZXVaIzdhEVbZPBPwf6At-t_-fB7VMt-l5jTzeih4s4SPsMQ5pEVxwhRghNVUORdlHmo5XSi5Xl6UAA4FgCQrGJEbaKQRNNGJZJAla7ytudggpMgNdt_4oyYcgsSS6MpzaW5_BdaP-6V-kqQGwruaGjIIe_iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Me5vOkXEeaE3nVliITQc9g3J0HKetMUnb3sSJMGHWQoOs5jfoxt4jtM7bLLOkNEYkfem0P2nVAkPEbBRhuDVNVumvLM6Y96ObuU5Opsu--VojIK8Mhuvs0RiZjNqt10uNCCwvehbhJFFDCjj9wYsdvhBQvCI_byNAI1bdUM-0uCgoiIH62hrXV2bBRfwfrSccPf012VBw1C1DBpJPPMM6E6HeFqd-O_ms-1y8cTzHqiRDFv8RSmufQnEZOeOeNsede4hcTZs2HVqESH5tnExf43HgwyByxaiDNedvqx55nZFozE9tKUDT4LPaYG2gvSbW_Mje-LxOX9hfhimdFmOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Me5vOkXEeaE3nVliITQc9g3J0HKetMUnb3sSJMGHWQoOs5jfoxt4jtM7bLLOkNEYkfem0P2nVAkPEbBRhuDVNVumvLM6Y96ObuU5Opsu--VojIK8Mhuvs0RiZjNqt10uNCCwvehbhJFFDCjj9wYsdvhBQvCI_byNAI1bdUM-0uCgoiIH62hrXV2bBRfwfrSccPf012VBw1C1DBpJPPMM6E6HeFqd-O_ms-1y8cTzHqiRDFv8RSmufQnEZOeOeNsede4hcTZs2HVqESH5tnExf43HgwyByxaiDNedvqx55nZFozE9tKUDT4LPaYG2gvSbW_Mje-LxOX9hfhimdFmOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=AJ_-x5MGK1metZpvx0QphpIzOwI4RGmqaujdKlJfFA9T-po2Iw5et_dsfO9uFT8-Sj-9ib7uDCmhXZL5lI8y-Cxw9Fdwr2qMzTEooSCqxgp4syYqdzYmBRja1Y8xt3uePqQUGxIcrIwgYh81yfq1jtFIoUAzx-vy2WT4O1S6926_tm1DWftTuF5AuFUGf3-bPmhReL8e7vVC-8aaX2bSqrL0q-voeVttuJoMWFGXuKPC_xNmfEQReRwb88Ai8CNa_QQC2ql1UGB6hCqZmhagKQU4bC4XkrXBLXKVf-HFKeUMBOcBk2n_B3qhLMzUtiGYFwL-hKpXzJRR_xUjmPTncQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=AJ_-x5MGK1metZpvx0QphpIzOwI4RGmqaujdKlJfFA9T-po2Iw5et_dsfO9uFT8-Sj-9ib7uDCmhXZL5lI8y-Cxw9Fdwr2qMzTEooSCqxgp4syYqdzYmBRja1Y8xt3uePqQUGxIcrIwgYh81yfq1jtFIoUAzx-vy2WT4O1S6926_tm1DWftTuF5AuFUGf3-bPmhReL8e7vVC-8aaX2bSqrL0q-voeVttuJoMWFGXuKPC_xNmfEQReRwb88Ai8CNa_QQC2ql1UGB6hCqZmhagKQU4bC4XkrXBLXKVf-HFKeUMBOcBk2n_B3qhLMzUtiGYFwL-hKpXzJRR_xUjmPTncQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBRf5UdtjyaEZ1T2J9t_QTDt7r6qBrrEdgbCk0falRL8pfUVuTxqF28bgqMTahP_27bOU0n1TQloU-mUJEF_czhrWJe5mkQQ9ym0fkB2BrbQny9PF7bZb51naBnhAmUs0FtJY7sOE28k9gorZecZlYZ5Kaue_6CdZBRW1syyiwA2wSpchpvzL5mmo60J8MJBUlrEOwJ7YPYNU1PtoJZ4z9KASFuA5vYG6CE0QL1LC4fkB18PUAYGEzYqavMhPZCSfTBOaBYTOPHWQv1yB5RhCIkAU6EkMAqxxS0Vbtu3JQAUOHtcFFtjNEO8XW_QG2OEupi4Y7cEPnoTC2zjFsRdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKEC3EirWSVN0tqvCPY9f3mHrEljrzcFCTn4Wey_IFeML78ovQiIczAjlEiLh65EemxtfggQZe9EFZFrS2lg7E7520u7d8_mR2M0K3slL58tHP8O0LwFYJL2taiDt4GEBCPitCX-w_thtfrFzvSsXbjp8bq830XskYGmBgCQekO7NoPOS1BBJcPHf3LZNV0vDalo-e9nz1hJ3OB8Ki2SA7c8wsfUJpVFkM70uLUJSU58CY0--P2g7jOwvjzB6oSrnwUaEH6TAEOlSxPaSgHOmzMcIOI5NT3PZE32HmjqYv_y_segp3YWTch_1PsoAi70NKkc4AtVmMwejcTb0rabEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=IWT_4nojjS1MLMVskRDgXPfTW3mblr6c7qK6rDq5ZsJQNlx05RQiump8-Qftq_JDtndA0Qn_n9V0rH40oQhLXx2ieKrJ1iHRQ-e8AmP4NJlFYMD2bVGI404mYiIhzLIyReinzvIaACZIX09ajFc3ETRwRkUnYXWvtaKJDTAzRulwBF24XGAiCm4V93hAHQuFGvOlgffhpuvcu4T865z6no-XrxPRFMz-zMpI51rAEo5SNSa6dVw6Dd9WdPv4RhvMioKSDrftKMs3C0aKw8_PFEM9dn2fC7a80AhtBuB7WM7fUZwxLGjn17eLv0GzKEcgoKR2HiNXwbO1sfkQ2FJ87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=IWT_4nojjS1MLMVskRDgXPfTW3mblr6c7qK6rDq5ZsJQNlx05RQiump8-Qftq_JDtndA0Qn_n9V0rH40oQhLXx2ieKrJ1iHRQ-e8AmP4NJlFYMD2bVGI404mYiIhzLIyReinzvIaACZIX09ajFc3ETRwRkUnYXWvtaKJDTAzRulwBF24XGAiCm4V93hAHQuFGvOlgffhpuvcu4T865z6no-XrxPRFMz-zMpI51rAEo5SNSa6dVw6Dd9WdPv4RhvMioKSDrftKMs3C0aKw8_PFEM9dn2fC7a80AhtBuB7WM7fUZwxLGjn17eLv0GzKEcgoKR2HiNXwbO1sfkQ2FJ87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=dHamEvH6cZ5UyWDHOKsidyyK-EoyBFQLpGjqVDzR2QCDYT9Tg4q7JcRp_Q5NA4jH-DTn4cSnF6hSzr-fEP1P6VhXB9_lGRwTURch24RxSDTFarKI4MC2j9mTxIWogvGrb87-II9R7reK9Aw52cYQxx_g9VGutaO24baqp9Qgd4jCt5ISXBuk_GigiOtqCKHne-IByCxn9Hq5W6n3zy4t23y5lwsFfrvur9pSKDr3HRGb2DV1yDjermXl860QoGpOPfmH__0Oa1B_dynTKG8Wxg5M9-8SV3HSesUI45RErn4hjOUXFglJHXCiiy-ZIYK2k3Q11o6yPYtTNwxKx3W4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=dHamEvH6cZ5UyWDHOKsidyyK-EoyBFQLpGjqVDzR2QCDYT9Tg4q7JcRp_Q5NA4jH-DTn4cSnF6hSzr-fEP1P6VhXB9_lGRwTURch24RxSDTFarKI4MC2j9mTxIWogvGrb87-II9R7reK9Aw52cYQxx_g9VGutaO24baqp9Qgd4jCt5ISXBuk_GigiOtqCKHne-IByCxn9Hq5W6n3zy4t23y5lwsFfrvur9pSKDr3HRGb2DV1yDjermXl860QoGpOPfmH__0Oa1B_dynTKG8Wxg5M9-8SV3HSesUI45RErn4hjOUXFglJHXCiiy-ZIYK2k3Q11o6yPYtTNwxKx3W4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
سیو تماشایی
پیام
نیازمند
…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=QeDggdxCWqCTeoxdOClQjytCNf3xPBfjqGSYFiZ-LGgEBiZ1nR4XOkMJE2dxXOn2-jH67Gylv4GopZtFZifZF0XT38R14JjxADwvOAOT14mPa5m58dWA0XQkQKvqzfYcposd4X0awDHhACqIxHCBKBMzFBGk_ESCrz30tae_aA-193lkEWdu84UJdA5v7ed8YPt3qVdCgYdW88KJZJzyLHsRXtFu9kxiZ1dPaNdQWJ0hnafLCK4-WsuJ2sOzbEqzmx6TZcNZqAwcbbZq7NFT8Tl6_uZrcCBOHck-JgpKt3fsjjZDHRMTqU1ARQ7uPlcwNYFNAqiVX__35EL8VZpMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=QeDggdxCWqCTeoxdOClQjytCNf3xPBfjqGSYFiZ-LGgEBiZ1nR4XOkMJE2dxXOn2-jH67Gylv4GopZtFZifZF0XT38R14JjxADwvOAOT14mPa5m58dWA0XQkQKvqzfYcposd4X0awDHhACqIxHCBKBMzFBGk_ESCrz30tae_aA-193lkEWdu84UJdA5v7ed8YPt3qVdCgYdW88KJZJzyLHsRXtFu9kxiZ1dPaNdQWJ0hnafLCK4-WsuJ2sOzbEqzmx6TZcNZqAwcbbZq7NFT8Tl6_uZrcCBOHck-JgpKt3fsjjZDHRMTqU1ARQ7uPlcwNYFNAqiVX__35EL8VZpMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
نیمه دوم نکشیم عقب پیروزی پرگلی قبل دربی خواهیم داشت‌.......
✔️
✔️
اقای تارتار یاد بگیر اینجور شجاعانه بازی کردن رو تو بازیا بزرگ نشون بدی
✔️
✔️
همینجوری جلو استقلال بازی کنیم بدون ترس پر گل میبریمشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=Vv1iiTJ1aJ4n9URmChqG_xfXNUbQBERxbdk_hrDj9w3KKp9LmHXGeJiLqkSiY1iIW0rpBVtPYQ9QP9wHyGRPt4KbShkOLmXwel6jeUDN3T0rCJ2qImNvgcLXxq1Q0C1l5pHWgtZwjXf9yozEuomncpNWlrmV05dmzv73XpKeMmngh06yhORuWTElAWw5GMv-_go3bCBoZ3nfS0DFa-pkkKFIJqaQvS9ZaRwdIhfpwa-FAuorlIg-_ILDd0QzfsVwoBlk_AEvGGv20gvI5fPTFr3LWUFXqvhhdvsj9vKyoa3Y66455N4fIkiM2ikYppvng3pbg_kXqDlBoxrYG2L9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=Vv1iiTJ1aJ4n9URmChqG_xfXNUbQBERxbdk_hrDj9w3KKp9LmHXGeJiLqkSiY1iIW0rpBVtPYQ9QP9wHyGRPt4KbShkOLmXwel6jeUDN3T0rCJ2qImNvgcLXxq1Q0C1l5pHWgtZwjXf9yozEuomncpNWlrmV05dmzv73XpKeMmngh06yhORuWTElAWw5GMv-_go3bCBoZ3nfS0DFa-pkkKFIJqaQvS9ZaRwdIhfpwa-FAuorlIg-_ILDd0QzfsVwoBlk_AEvGGv20gvI5fPTFr3LWUFXqvhhdvsj9vKyoa3Y66455N4fIkiM2ikYppvng3pbg_kXqDlBoxrYG2L9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=ULeOB7stLdbsHzQ3OZAZht-Xpi2Z94YSYOuH8H_8uhZ8BpPMjJZGEd_90LGsAu9iQZ5wbBZnzx0lyesFm7HGs49T1WhEdFQYoJVTQ_m9BTHJelsW1VsLmFmAZZJx8_lijAteTW0KHP74L-YJooWowLUjQhgXrMLu_FTpALZKeZUbMjPTsmneGzkvRcWVRxZW5VcS0kQGNst1jmtORs5VdCxVw-BkQK7JmE4XsYDQafTrc1S--XNdbdpbpadSrUs8ILua6VFDwZhhWJgl-962c-EpVtwm5h5Od7aE8_32JBYphmxcox__Q0H-1ZERwud_NP8dnShUmXkK8CYZB5thvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=ULeOB7stLdbsHzQ3OZAZht-Xpi2Z94YSYOuH8H_8uhZ8BpPMjJZGEd_90LGsAu9iQZ5wbBZnzx0lyesFm7HGs49T1WhEdFQYoJVTQ_m9BTHJelsW1VsLmFmAZZJx8_lijAteTW0KHP74L-YJooWowLUjQhgXrMLu_FTpALZKeZUbMjPTsmneGzkvRcWVRxZW5VcS0kQGNst1jmtORs5VdCxVw-BkQK7JmE4XsYDQafTrc1S--XNdbdpbpadSrUs8ILua6VFDwZhhWJgl-962c-EpVtwm5h5Od7aE8_32JBYphmxcox__Q0H-1ZERwud_NP8dnShUmXkK8CYZB5thvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/139180" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/139179" target="_blank">📅 20:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/139178" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD0IRMST54Pkvsh8QhBkQIhlXKhH9Xk8LOrkjMqoH2iJNDD1cC7Ec5TSO56P4emh5pt2RAHYrHK7o2eU3OcEdgSHW_xGEFbZr9HKddzS-n4n1MU8a_PXfcwohGraUo-6VTGuXXRgpfu0xeiWMFb7ttV9Yvgts-PCCSCDR2SBITxMzwACtgkaL6sFRoEmVjwJdUVnkbG85_dj8NhSCmtnOeUQrz-eRMxwrfmfGr-Ql7Tvvzm1bHSfqz4rkWrRH8EgJFWtcBJ250efgO0_dhBIMNJByPjAhQz1u_sfLWVOYuMk9oM9_uYiFDJZbiIfUOhWsh1JqVE1qY985Mx0EnVGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/139177" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5wWcz_QTYYJGLthejX3P_bdpfYUqmQtJT1Ud3c0aQbG0ryCgd6_TaFhSSK_isJ0uclhjqhq1Y-TgUbLa21GlUySDo6qwtjeaGfry_ofDnEgxqYQY8pSxPquuKcfONXtDTyrvIofQBnotrUvQK6Zsvglv6IPiB-hca3on5Cpg9TehSEt0bcPnLnDfC_kWa1IRQZP4a3J1Z9wvQLoCYGSFLPPa3it99-nkPdkNC8NtEVtC4rreoi6bilBZUftF_K43JZUPSVrTlX11wW-z12YIlkvzcdHBYFfhvGGm_pdvjpzhisMxZik0GmHYkRV6UCs8Hd0C4p_XdQ_U0XSaW-3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یووه در تورین دنبال دومین برد فصل؛ پارما هم برای جبران شکست هفته اول آمده!
برتری کیفیت و امتیاز میزبانی با یوونتوس است، اما غیبت ییلدیز می‌تواند کار را کمی سخت کند.
نبردی که بوی برد یووه می‌دهد؛ اما پارما می‌تواند برای مدعی دردسرساز شود
[
یوونتوس
⚽️
🆚
⚽️
پارما
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/139176" target="_blank">📅 20:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
پایان بازی در نیمه نخست
⚪️
پرسپولیس دو - ملوان صفر
⚽️
گل‌ها: محمد پاپی(گل‌به‌خودی)، بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/139175" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
خداییش دو تا زدیم سه تا نزدیم .عجب تیمی ..چه استارت هایی چه ضد حمله هایی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139174" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/139173" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=BBv6iWBo3aw5Ef_B2oq2nGoyfyE1vgUKinOF0YSoHGo5SeoiBsLYXApFuUz2h9BwoHU9kGiH4fWXFXn0gBm3rMcEPDvfISw-q_etUk2PPHYWqIrh_3IM992K0Degq_jxdJ9lMkZnaYFtxewgalUUzYx7S_Nvxyyc1X8amHHlHIhbpT8lha5VZjGWE4Esm8PJniVJPyD_LLqvkjlo_b_dKcyG4xRYz-jbCw7PB4YjIgFzXxXz-NiSPd6b_vp3kD8A6kaY93B862gmBOSr1w37S_TqZ4iz_dHDgBgU-Weo5sOLsUEm4dosciaMpDzvN8GrtVDguTWOF5Xa4wdYwxeTIF9srBTqQIAfYGuh9rb9WqnZ4fpkZmdZEPRyriHthjLQIanfsYOV7CCwX6yJYsnbYHYe0xawzn6SHAGKq4r5LjXEIBfxYQztSsOgqiiHioHvIe2Wxroh1H4UDBj2yJtqWL1XbGLQ5ECNsUYfVtoW33MX_UW3MsuGjIuPHHZ549DEouaRTboRCbta999AdVFb6EUp1VjMUmjjdHkGqb1Kx1s5fVVdoqX2WmgD1IjUJk9VV2QYIduyo7-m2YTY5hum7bo_WoGact8ujwDVZo4QWs_fEHGwIeI9GdZsgHwwaA3YGP5kPAYGN3YGFeytXuvpkUneotrRe0wlaEM6vqpuq_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=BBv6iWBo3aw5Ef_B2oq2nGoyfyE1vgUKinOF0YSoHGo5SeoiBsLYXApFuUz2h9BwoHU9kGiH4fWXFXn0gBm3rMcEPDvfISw-q_etUk2PPHYWqIrh_3IM992K0Degq_jxdJ9lMkZnaYFtxewgalUUzYx7S_Nvxyyc1X8amHHlHIhbpT8lha5VZjGWE4Esm8PJniVJPyD_LLqvkjlo_b_dKcyG4xRYz-jbCw7PB4YjIgFzXxXz-NiSPd6b_vp3kD8A6kaY93B862gmBOSr1w37S_TqZ4iz_dHDgBgU-Weo5sOLsUEm4dosciaMpDzvN8GrtVDguTWOF5Xa4wdYwxeTIF9srBTqQIAfYGuh9rb9WqnZ4fpkZmdZEPRyriHthjLQIanfsYOV7CCwX6yJYsnbYHYe0xawzn6SHAGKq4r5LjXEIBfxYQztSsOgqiiHioHvIe2Wxroh1H4UDBj2yJtqWL1XbGLQ5ECNsUYfVtoW33MX_UW3MsuGjIuPHHZ549DEouaRTboRCbta999AdVFb6EUp1VjMUmjjdHkGqb1Kx1s5fVVdoqX2WmgD1IjUJk9VV2QYIduyo7-m2YTY5hum7bo_WoGact8ujwDVZo4QWs_fEHGwIeI9GdZsgHwwaA3YGP5kPAYGN3YGFeytXuvpkUneotrRe0wlaEM6vqpuq_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
گل دوم پرسپولیس به ملوان ..استارت انفجاری و برق آسا از بیفوما
✔️
توسط بیفوما 33
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/139172" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/139171" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/139170" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNhojw7Q7Ih8B60zbscYANBYLkHon8KKaJUVXMtJDDHQejQ6EZUUUFcSBCgnzn4YYrL8B1h61H7g9WyaJJxwvsE7Rc1wOH20dL98WFDsGAeCMjCpq0h9U3lt5OwDbEfOUyXQLdu3eY1CVUt0i_jhmzi_HPYXS0y67HJHyb25jW8_8PcG62aBTERRmUWaE4M4tJ9GUzlzaIeoCH60FDlkj-9UHc-DiPr4mJkGVM_dz7KPY6K3XAbbcVWKmuyBxAscXXL5izfi6Okhh3eOOksSK2ajUm3Vg8bB9cWT1c4OmxqUh0OLFCv1aj5SSfyKuFVeKL6o_riSpYpNDf3vNBYHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJr5N-cQS7ptZKQgFifWjXZIPGwW7_iy8UBzfwzUPrI9KvDTs0B7bndXLrar76dN8Jou-ypSVeVAZ3ObU46q7tucubEMnsLuSjCXYlYEUW6G2LtITHdnWuD-fAA6c7r1JdaHq6kYRtq5KXhDGcXvee-8-5VEKUQdxSTGYI67LUHycMqD4VRRXUYvg2FtiMmdMerZeVDoC5J_LnBjO53hw7A3hPPCR4xNhfJ4O6cu9tvlBf7WBJosf35l83xz4CFm1BBdQIt0CCt8MH6wSS04qnrkrTOndUSuFGEF_b6VYBCBMlZWFmt7IxTQnvCiLjZ4QGnQQw1Ar-xRTghenwgYaP6J4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJr5N-cQS7ptZKQgFifWjXZIPGwW7_iy8UBzfwzUPrI9KvDTs0B7bndXLrar76dN8Jou-ypSVeVAZ3ObU46q7tucubEMnsLuSjCXYlYEUW6G2LtITHdnWuD-fAA6c7r1JdaHq6kYRtq5KXhDGcXvee-8-5VEKUQdxSTGYI67LUHycMqD4VRRXUYvg2FtiMmdMerZeVDoC5J_LnBjO53hw7A3hPPCR4xNhfJ4O6cu9tvlBf7WBJosf35l83xz4CFm1BBdQIt0CCt8MH6wSS04qnrkrTOndUSuFGEF_b6VYBCBMlZWFmt7IxTQnvCiLjZ4QGnQQw1Ar-xRTghenwgYaP6J4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=EIEBrOCdV9TAsU8ShxWNEEbPNyIBJgNpUhG8QAlAFm4wy8a8ALMG7xggjGkT5blM0iqloz8iNBBje2e7qQtAHTSNEqb5JNFjqqsAfv_vXE1DoMb0QJqLVYZ5Apo7eRpy89j9AkIkxORV60Qel6zQYjIGeX0WJPkEIS0_Qtjx4hrBY7qpcLnT7tyMWRfiD_lK2fz46wXfOBaOTPYS3Q_q7UUo1lAV_5fX5EDF4z0Pw9gPb9aEoN71K9E2F_KgtmjrJBtsdaCPlZB4ZHRTw_NDq1g5OGTXxyQJAuf6pU8Vw8yOioSALyx9tvEXx_hjNPzOY-fBGdp8N3dYDbGhJt6K6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=EIEBrOCdV9TAsU8ShxWNEEbPNyIBJgNpUhG8QAlAFm4wy8a8ALMG7xggjGkT5blM0iqloz8iNBBje2e7qQtAHTSNEqb5JNFjqqsAfv_vXE1DoMb0QJqLVYZ5Apo7eRpy89j9AkIkxORV60Qel6zQYjIGeX0WJPkEIS0_Qtjx4hrBY7qpcLnT7tyMWRfiD_lK2fz46wXfOBaOTPYS3Q_q7UUo1lAV_5fX5EDF4z0Pw9gPb9aEoN71K9E2F_KgtmjrJBtsdaCPlZB4ZHRTw_NDq1g5OGTXxyQJAuf6pU8Vw8yOioSALyx9tvEXx_hjNPzOY-fBGdp8N3dYDbGhJt6K6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=YX5utmyG4bl6LXAPgFrri2VnItof-DX1VWWWapvGdArMx6HED4LN_KjFbeVKOOhV_Ai0sCE9HuhNQL8X4l3vpMNKwOEPC2n7WXLO_eqsTQD0dtal6stbctJft78OMhYfK4Q-7R6koD18P-pQmouJvcB76q8yjUkkWJb7cZ8AaSzsSh3psXgxkRHrrTmHXcU_KnPtbUWHDm9466RVzMiQhs3X-l3_4jFj77RtB4LShGb0OeFjrlrEK0nFAfIJvcL8VFKiJr7XneRBxx-YlJ-FQx7QsWtiPe06YKXCf8mLpxNxHt4kTKfr9unqDfBtd8N2h8JbLfR-4hp_9cRwsKwZ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=YX5utmyG4bl6LXAPgFrri2VnItof-DX1VWWWapvGdArMx6HED4LN_KjFbeVKOOhV_Ai0sCE9HuhNQL8X4l3vpMNKwOEPC2n7WXLO_eqsTQD0dtal6stbctJft78OMhYfK4Q-7R6koD18P-pQmouJvcB76q8yjUkkWJb7cZ8AaSzsSh3psXgxkRHrrTmHXcU_KnPtbUWHDm9466RVzMiQhs3X-l3_4jFj77RtB4LShGb0OeFjrlrEK0nFAfIJvcL8VFKiJr7XneRBxx-YlJ-FQx7QsWtiPe06YKXCf8mLpxNxHt4kTKfr9unqDfBtd8N2h8JbLfR-4hp_9cRwsKwZ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=kPZ6oyRwB47JeTrEYFzaBsQloLm9LNKN7hoI3plYRq6vGKlMyIdgGbxiElS2AjFV9ddvv8RbKUyZCqBqoxnGknMKP3Zps-YdoT93FmbyL12ycEBmDhOYvH9XkCgWTh2sdFWigy_Mj8zzc87iP-hf94r4XfeFPD927FtlJQ7mKMQ-0Dbmnq87ipwGyPSFmg1ZQ-3N1sfM2TGaDBlfzsp8GE--k3m8331axcOxS4oxOQNOG6iJiinW8MH78ALOf7kEljjUbmDCwwcJrYG1NDnxiii0MVnEsvmiO1PTnDtXYtg5sDfDYKD6D1lx_vdZLyiH3ISc7zel4x-sNDl38vpwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=kPZ6oyRwB47JeTrEYFzaBsQloLm9LNKN7hoI3plYRq6vGKlMyIdgGbxiElS2AjFV9ddvv8RbKUyZCqBqoxnGknMKP3Zps-YdoT93FmbyL12ycEBmDhOYvH9XkCgWTh2sdFWigy_Mj8zzc87iP-hf94r4XfeFPD927FtlJQ7mKMQ-0Dbmnq87ipwGyPSFmg1ZQ-3N1sfM2TGaDBlfzsp8GE--k3m8331axcOxS4oxOQNOG6iJiinW8MH78ALOf7kEljjUbmDCwwcJrYG1NDnxiii0MVnEsvmiO1PTnDtXYtg5sDfDYKD6D1lx_vdZLyiH3ISc7zel4x-sNDl38vpwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=EtvRbuG1mDxv1qwtk5jGvixzScfIy3ziMHQHTGFEN6peQjhyN24_LrqkgdFn4buvBri8GKl6Kerv787fzfI1ESx6uq8YZSs3KKr6A-VSjLNPxz3P-m7Z5WuKcL0TNXZl2hWdfhfE7ozRaN8Y8SNw0GMCWfhW99hcJ2z-03gZrqATqZeKAhD9wGaA0HbQcRwGN4qG3pYdWrSo2zlwAk0vbUf8SVpzQYFA6VljaJ53PhGO2MZt5cy_NaHTHNXlGnnZnFRKnbliC8W2WcM64fQueooljLcbDuSz3ZsV8STrmytdmTxG36jYE-TFKnoTSwf9QF1iobKgOuyawq4xqwMrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=EtvRbuG1mDxv1qwtk5jGvixzScfIy3ziMHQHTGFEN6peQjhyN24_LrqkgdFn4buvBri8GKl6Kerv787fzfI1ESx6uq8YZSs3KKr6A-VSjLNPxz3P-m7Z5WuKcL0TNXZl2hWdfhfE7ozRaN8Y8SNw0GMCWfhW99hcJ2z-03gZrqATqZeKAhD9wGaA0HbQcRwGN4qG3pYdWrSo2zlwAk0vbUf8SVpzQYFA6VljaJ53PhGO2MZt5cy_NaHTHNXlGnnZnFRKnbliC8W2WcM64fQueooljLcbDuSz3ZsV8STrmytdmTxG36jYE-TFKnoTSwf9QF1iobKgOuyawq4xqwMrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
🎙
روشنک مسئول مسابقات لیگ برتر:
✔️
✔️
شاید جام حذفی را امسال نتوانیم برگزار کنیم، هدفمان این نیست ولی شما ببنید چقدر امسال برنامه‌ها فشرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=ZX4ahh1OPsW9G88e2XpAxmlhZK8JoicvmzlOTDdskUkpWUm14qngnaOoOc-Zg4Rcxkg9fYEP8K7QpwdLA9Dyy8birdrOTQX9o3pWYph1-3kFjyliRm8gPLr-RgYDVCdfIhMuvBX-W65tYbfngdp7FYJqxWIQnpT2CsVVf30c0_wbbtKqDBYR96KXtBCCJ4SOBUfaijDX8r7-YzlyhK19wl0x87Hpf7gBa6krsnl5EvXrqX0kKA2iFjJ__vEwcT4198nYN3BiHNY21o4-Or-SBSklND_Rx7HaiwZS4Ksiqou6f326wBf8Tb0VnJ1x6StjmvRTl7Jnk07bQscqtSRmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=ZX4ahh1OPsW9G88e2XpAxmlhZK8JoicvmzlOTDdskUkpWUm14qngnaOoOc-Zg4Rcxkg9fYEP8K7QpwdLA9Dyy8birdrOTQX9o3pWYph1-3kFjyliRm8gPLr-RgYDVCdfIhMuvBX-W65tYbfngdp7FYJqxWIQnpT2CsVVf30c0_wbbtKqDBYR96KXtBCCJ4SOBUfaijDX8r7-YzlyhK19wl0x87Hpf7gBa6krsnl5EvXrqX0kKA2iFjJ__vEwcT4198nYN3BiHNY21o4-Or-SBSklND_Rx7HaiwZS4Ksiqou6f326wBf8Tb0VnJ1x6StjmvRTl7Jnk07bQscqtSRmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139159" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkhImQSR1WY0Moa35Yra_FrT9k1ycTnxQ-5pjuyDK6U1SYKF8SjZl3X3vzoyTsZSz_bVOs-3RyZ7ZOTL8rnaBZDIQMIhPyDFfrGD__rCeOIS0YIH204RjX9uvtXxPKDd5Xz7sVU-_WFcaAdDSoE_K9CgH-YdRZKyQEWaHB-xXQ8DD7lGSVEBSvQHaFYBKu2mmTlMIizb08m-bJR6ZF9ct_PML0rcb94zY3b2lk4iCAqgWIkAewFMPNyhBGrUdFVqAM-UL6M-0_VkU4KcgVqYnJsMTI5D6wjAHuPL43wYjh2kPzsYdvJiCQoM61SHF8AI7EVXiWVmdVpPVsBOidOihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جریمه 50 میلیون تومانی باشگاه پرسپولیس بدلیل توهین علیه مقام رسمی مسابقه توسط تماشاگران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139158" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=RZrHT7TYrAFUsoSPAx0qrijDAOKs3ULjI0pR-FpkNqedFfasSX_w-zoibwscQTZ3I6FCGoNPj2xakID0a15jJlrJF8XZek_UeNLW8caeBceMdRHqbTA1iqWn2C0KADC0ni4fthCG0HzpGkcZH88dsLN_kmEHOST5F2xIe54Ct0rarBwFhGNfyVb6QBXrh9t7wfSAT0SIWzQ_vLa5aEARGF6944P7JCyhSjl7fyTJcJ_J99nVYAd-QSfrfCH-s5d5kQ-RGSBDil6EejqWIy8mo-mMLVFQbFpuud4-niH7VjNLZAALaGVAOZtVWY4LrFf3tDpADyqvmFn1wp649ywfow4bslRWmTC7ZqkzaLVkCpW6LCyE7STUSYqTOTJm6tveq1h_0Q1MqpDPaQYssWWa0MDjARRXBAvUraoQMVCllb79km-ibZTfqTwAwhfcnh7x4VnObSi476xZ6Jo7PGu2p_CEvkzLBzMYfyRz2GeHMDrKz4iKqLBg3QYQ9wN3ovVbd9t31PMbFebIZgtuPlkAT_LZGKhtQotlKxa8r0iwPGosMNR10o88EbFi9ojwm8LkQ4D3GzOtQcIv9vrGxLtJ9x92xGuCf3TCCB6K6xC4Il6WbPoi2dZyROCX0p-RHhIfNKJgIPhLMCKHcVUD4c0ft6bm5ql7KMt2VFtCxZM72SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=RZrHT7TYrAFUsoSPAx0qrijDAOKs3ULjI0pR-FpkNqedFfasSX_w-zoibwscQTZ3I6FCGoNPj2xakID0a15jJlrJF8XZek_UeNLW8caeBceMdRHqbTA1iqWn2C0KADC0ni4fthCG0HzpGkcZH88dsLN_kmEHOST5F2xIe54Ct0rarBwFhGNfyVb6QBXrh9t7wfSAT0SIWzQ_vLa5aEARGF6944P7JCyhSjl7fyTJcJ_J99nVYAd-QSfrfCH-s5d5kQ-RGSBDil6EejqWIy8mo-mMLVFQbFpuud4-niH7VjNLZAALaGVAOZtVWY4LrFf3tDpADyqvmFn1wp649ywfow4bslRWmTC7ZqkzaLVkCpW6LCyE7STUSYqTOTJm6tveq1h_0Q1MqpDPaQYssWWa0MDjARRXBAvUraoQMVCllb79km-ibZTfqTwAwhfcnh7x4VnObSi476xZ6Jo7PGu2p_CEvkzLBzMYfyRz2GeHMDrKz4iKqLBg3QYQ9wN3ovVbd9t31PMbFebIZgtuPlkAT_LZGKhtQotlKxa8r0iwPGosMNR10o88EbFi9ojwm8LkQ4D3GzOtQcIv9vrGxLtJ9x92xGuCf3TCCB6K6xC4Il6WbPoi2dZyROCX0p-RHhIfNKJgIPhLMCKHcVUD4c0ft6bm5ql7KMt2VFtCxZM72SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139157" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kr_Nk5fPEDCFTknQdgVIHU8NOzj7gxsgIyiW7Gga2tWbNxFVdDsxG3Ir7Gvxl_OnLFqHRmHXFcOmJk2iVrbJh3AsDDLgLysQilha4kIl02GpDdB12Q-7Kv0zVTVfobNLhRs7wst7vNef9VOG3jM_tDDfnEO24cAB2sW3D_TQrL2RPIxM8DYAa-_9lzVlJ0L6N8xcyIbYZhMLHKMBFMPW5tWFCGs1M9-BLtiwGRbJedMhNYDqL5GOl97mxCwSyGw2fPHmv4aZBi0I2Z7Gw_kUwhH8vCXR1WI8Mh6iAg_jKS-Ic55KQwcmPX-1JJqKdF-ewRuGf8vCQfSGjw71vG_ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJC7ju6MmHPgDast6Dy6zG6TNzBfLWCM6VM-b1IQQfjGWkUDbRIOQKCQp9L2W29mmIJBKVQEABS7C4lDHrVMrQpKgcRdL1za8wLoyTa7KUiDNVdWv6RpJdSmtlU46mLC-eqIxhRe_gChITBpY2fl62xzmV1S2kPoadoNvnKFfg53oWcJF_adFQVwc53rZdKUTddc6LqASWN-yubuvmGAX9IGQ9YAgBvmAA-3CkLc9XStP6X3evut0854YsZxCmBtctlTb85ZkJVqaLT-S3SSRMixTQi2iCFhGotpKu9dNNRwzR4LH3wykmijTgSmVfG6TmSFenxJQj_uAiqCsW9sbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhM6DMbC3i3rg2Y2tvEaII_PSAX8jvLRiZNvNrxWwEAAZ_ZHIN3KCSFOsCv2gKTzrq96CZXOA6Acu87i95y4fYCtapcCwzk8HrZooZVOuYfRD2lQeXMYCFjJUMhKROCWQ6kClgYZnmm4ld3h4eu5rWj_9_ManLP5kmFR4n7mg9q3fFNkYinwB26fB0hOqIupoj6Uzpa6Yso0GKjI6r3LnOqTLUWbhr0bMmDq1LfX0soA7nDq707NH3i5IHiDGC3FspRX1vywFeiQqw6HYSXH27eg14IEE_J0etJfas0_INdlAB9V5ZDsJd7jiTjXsKUDNlp_MylQBzBAZtW5yb_cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kizTqJCZ9LxXrEfh1sJJ2C9AtJ1-qwc68EMX4O9V-b3qDUnThn4eZwHQvLGSwCFCYnY1odMsnvUpGGI6iLVy-rFELAsk7wrWEPabUG4CMDT8uSPbce_CBZ4s0c5Wlvh-qBJqiM96Tpfs1Baw-mecw4gtA8Nwp7he2ilUTdgUJyu_DqmDkwz2qrJ5-p5j6axke1uFSbU32oZTzaqSxU6d6dxV_oJ8Q0dW1OTtozDnaUwhOjsDbySy5jzTK6dYu42qhCRYR3DO0-H1v8xRC9NykxJFJWvomwLejAtnUBCP5-gqwooOgWZbDzQhpT5cLKdLeSgyE0yo-0Odz5fhQfJ_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWARraiU1tHSL3TB4YybKCBDD7XQskPX_rNFCD0QN91060UbuO5sPzJjf4JX5Fve-YG7slBU1hJ8Z2FjYjnStEO8zijpvxQV1nGD4yHJnB7PIpc6SkL2VqQ-IAmYqIc-aK_tcPffYyeSfAwWhFgqjkBPYuJaMieLFCZWxB7TrPS-0cGKStoxLvD3UZCWyr_xXQFQVUHlnGo9a9i1L3YhDJDKKglAnoW6rrFKQNGqiv_-eQ_CTV-lIcAuODP3gxdac_xhA-RHc5lpDUdWmO--BDsK5a_uqTW6PFfpUWL9OeLn35okmYdkvMnoBNu2x-GaiAbrIUaKSo4nqW8qCEkNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI2IgU5wWzBU5iCpofAPHzOL0yEt1amOqE2jc3hf5oq_z8gxvo5JbCqLT-XVnd1haOCIR6I7h1C8mV4c3qePOZPLHgnhwOSs2Q7J8HSeMURMep1Ma7BIHuuNCH7myqouJOQ_uhChxBwMA04mtgAMNOTE_WaVbTKvi0RoBPoZ5qzXf3wp89VuIvCLooxSLqK0dxpkjP8E2Nk3EZC6paM48E5u85ntC3TSxghAg4U_dAKzer5w7nqa6VtNnagJJB60_vSyrBSKTuQ6StODcLNeSD2jH-QGcOw0_d0V5KsMK6REZW1phd4Mmy4yG-C4JpJObec0-aeVBLu8_dZeY-VZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUGzlZ6NmLHX-tq_LniKFXoQ9IE1JqzOOsvMhRMby82VgjyEO9TvXotmcRK0YmrWVuPsbKB8FJW1wSW_lLeTRwRhe0NQG9XxUQ46SL3_syZPwhi7YNtqX-6-djhrCkrLpb66K2L2mCLwCuow8HU1C4CMPHK_6ATz_nGq3EQRlX4AtOmRQoFwdX_9wq022xDKTI-XdHIA_LoKG-i5XMxEyYZiIWmGen8KZUgO-bS_A-ThY0HlCxZQCZEiPvXSFTqGSCM8PTA8YLZlP_nWEhSWf0OgCDe_FmMLXxlXbacbectrvXPDpf2z945BnyVClBBY0ldkQEA8bE3PaS_1yrCeEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
⛔️
حواشی نا تمام هوادار متمول؛گادفادر متوهم ول کن نیست
‼️
🔽
رشته استوری هارا بخوانید…رامین پوکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139150" target="_blank">📅 15:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8tNH1Wbyr5nA2C0b9sUcC37jn5rXzCkHguArlcdOWkgB8SPkRaAH1UOJEXKi82tYY5mtE05Gwl4waEaYpB3O40OfEClcpW1-a_lan6Er9oghmzyC2ILjN5i-zomieATDSHyuLHNymDSqQhyZCy-57QuWV3TFZM1-FvYYybgmYYsAdf40I8D4GLfskfMNtZMLW69Bg5lykl4ucnFsLb1_idMPoVTWWtJVPHp-Vwdg1G4aZnkzuws_-YG-qxIe_wecP4gsL1KprxBVJ3cxJsznid3biVUzCnLIOBGy9kySBGo_13NMtYNRPjBdiftPXGl4Ow8wrYffYQtmk1fc4_yMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پایتخت آماده یک شب داغ!
🔥
پرسپولیس دنبال شکار ملوان؛ قویِ انزلی برای غافلگیری به‌میدان میاد!
امشب نوبت کدوم تیمه که حرف آخر رو بزنه؟
[
پرسپولیس
⚽
🆚
⚽
ملوان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJkmMg07xqm-DfotVNW7w_Q098-fUd6_zvTYLFpuoIKlsIFn6tQscNpOZjAN7AUc5IqMMrMA5NIs1XDiIwWC9g7w131mZZNOsnS11lr56TWPWseEdnenX9dUVy3zWRMqhlxQykhSNcrDtokSwqi0VrXc7EIB5ho8wBIWlO-noxQPso2Yon2o_gTjSWpZzvVXPBzfIfoNGhJOZ3MmbMVZN-S1TWG8Fw2XytXuBOmMFutMZbUnZrZS4KcXt3yfqaeib4fH7oVvLJaL1MxxXg80h-2OrbLeWRyoLtfqZxcpvR1ZHNnfoK9QFs3IeKrmVZ-bmIlfKqNRv9B23F6BzjKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
رضاییان در توجیه رفتنش به استقلال میگفت هواداران استقلال جنتلمن و با فرهنگ هستند اما دیروز هرچی فحش توهین بود بارش کردند وسط بازی هم کلی بطری سنگ و ... سمتش پرتاپ شد !
🔻
🔻
بله آقای رضاییان اینا همون هواداران جنتلمن و بزرگ استقلال هستند که به مادربزرگ مرحوم جلالی هم رحم نکردن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139148" target="_blank">📅 13:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139147" target="_blank">📅 13:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
دنیل گرا مصدومیتش برطرف شده اما تارتار بهش اجازه شرکت در تمرینات رو نمی‌ده و باشگاه هم گرا رو نمی‌خواد ولی تا پایان قراردادش در پرسپولیس میمونه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139146" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khpEw8nkQfnYB182UDTX0goZOc03xa1A9Vr3dyukNnrrKfRSjU21bQA5TtPgFfrOO1oeVCcH7hU0_fSQfF-rw8ezXSB3us4xtci_d1xdN5RdG77dYoLe4GVotjBp2E7ktN0WID-iGuWg2TocBpfjItiH3LzHGlHVGZSQgh5MlzLhO2HzVyIIRV4jeN-lM7_rdcKk0XegfuY-yx1nq08gvx5Lr4hLSoTQKGjJhI70SPsBdihvlJWyj7sFyMq3Vnrz1zTC5trmSYTMk6f271ewlPFf-dOmhDiRGpEopgcZaGMzoRZi-fB4ZQbqWQyxlasxVl4We2XWf6QcaVQ71H5-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اتفاق عجیب در لیگ عربستان؛ از هوش رفتن ۵۰ تماشاگر!
🔻
در دیدار الهلال و الخلیج بیش از ۵۰ تماشاگر به دلیل گرما و رطوبت شدید هوا بیهوش شدند.‌ بسیاری از هواداران نیز پیش از پایان نیمه اول ورزشگاه را ترک کردند. الهلال این دیدار را با نتیجه ۵-۱ به سود خود به پایان رساند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139145" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
گفته میشه مدیران باشگاه گل گهر برای شکایت از باشگاه سپاهان بخاطر بازی دادن به کسری طاهری از تیم حقوقی پرسپولیس قبل از شروع مسابقه مشورت گرفتن!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139144" target="_blank">📅 11:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139143" target="_blank">📅 09:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139142" target="_blank">📅 09:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139141" target="_blank">📅 08:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
صبحی که ی بازی سخت و حساسی  داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139140" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_b3DFBnQ3lRPnAhZmwf9vjVdbOL2hvrrlgqit0R56F43nfjBsxKPNR931qwjuNsGagAtZCB8zZudKlDUZXiIuzdbkN9JnY2Cm0m4jxaJPrFYaWNKLxgEuN7p3euKIoaGOIm-CyN3fGz5Mh-79KRntA8SWJFzRb4bPrCEya2bUdUrE9TwdRTT9Jk-HnkmLr1D7PObMA4tuha80CBOEfGha7qKCXm-pAK2NUKRc86dHeLzIF7FLUklR6cWuMdWtKJ04TXlhzKycXNeP9KNDHtP6jjVsazdB8zYKamyqIYxsJt1EeqSwl2oQV1XALr9tmm9c2tt_lAGsEgdBs0cvR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=OBYwNCP1uPIaIpQsntZxOR6AF6CaKbO5UEdkqL-6EulMiQaRj6TDLFbFS3yOkwDsl3jwYhHuyS3k-r2qV1yLa-xGJvLWgjKaOXFAwi6-9vI7gIeWeXO9w0mt_1qIFSothh2BUZbv3lO9eu2tMOuaY6xe0dYVVCQfRS3p0bbWYt8C3hlmYXfm5smdolhX2cw-AZQTMbq7BzFvHneGi0LG5ZKlnjJy-bOGqIzeewxuOfBnWxhDnGhFfN6fbtLqHvCxc8vsWrZEnJ0sqWVifR-Dy0rNMSK5_xoXU44UvDd2Z_Y8YSrawnrwKw_JGvJEMqhWtT9sheUeNUNg5yT9c241haEpl5mOMmFmU6kHhlHEH2RReRgjuoMAKOKDe85V_a_D06rsmlTcRJ-4wTqifq-9tnGmrl5T_z9AcrWgkmYm6471sN9x04LjzgzJdB3sLWO0CJsGLHPQCnvM2pNU_t9KwjmxEl1UUgWMmLE8J9nTjh3EzpUnvVgygLn8v4aln1xtc7J9MW-99cRU9bDkKZIpmw20L5_0zg1Org0XJCa2znokTBUzm0_68-ax0renW37V9bj5A18cJHpKZdHl5_Fw-eF6CqnDPiZfft3pnhD1mCYsSA7K6rFT9pmSAy4E_UscskqXKQ64M39v6_DeXzEuPNU4OnOACq-16uUKQ3XLTn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=OBYwNCP1uPIaIpQsntZxOR6AF6CaKbO5UEdkqL-6EulMiQaRj6TDLFbFS3yOkwDsl3jwYhHuyS3k-r2qV1yLa-xGJvLWgjKaOXFAwi6-9vI7gIeWeXO9w0mt_1qIFSothh2BUZbv3lO9eu2tMOuaY6xe0dYVVCQfRS3p0bbWYt8C3hlmYXfm5smdolhX2cw-AZQTMbq7BzFvHneGi0LG5ZKlnjJy-bOGqIzeewxuOfBnWxhDnGhFfN6fbtLqHvCxc8vsWrZEnJ0sqWVifR-Dy0rNMSK5_xoXU44UvDd2Z_Y8YSrawnrwKw_JGvJEMqhWtT9sheUeNUNg5yT9c241haEpl5mOMmFmU6kHhlHEH2RReRgjuoMAKOKDe85V_a_D06rsmlTcRJ-4wTqifq-9tnGmrl5T_z9AcrWgkmYm6471sN9x04LjzgzJdB3sLWO0CJsGLHPQCnvM2pNU_t9KwjmxEl1UUgWMmLE8J9nTjh3EzpUnvVgygLn8v4aln1xtc7J9MW-99cRU9bDkKZIpmw20L5_0zg1Org0XJCa2znokTBUzm0_68-ax0renW37V9bj5A18cJHpKZdHl5_Fw-eF6CqnDPiZfft3pnhD1mCYsSA7K6rFT9pmSAy4E_UscskqXKQ64M39v6_DeXzEuPNU4OnOACq-16uUKQ3XLTn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139135" target="_blank">📅 00:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139134" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=QcS4VyWQtEFf2Hdv9qcjAf4Joa4Qobt0xUi12avlSoqFzorsFPLgn9cS1dC9xpTdMJD4jad8G2P6qUHgmtlQDuBaXyaGWg_VkbDKZDktKVdWXG-HkZsAAuew-4FK-AUmR8acDu4uXsuTRYoFZK30GlMp3c-Rnj6VyFiHmZr0KK--xPQ5eoUvuEALhU6MSLoKN9VCZmDm9ak2khY8LS4PFHIHWSUni3Eqmcyt6EdobioI4y0mSzrcbSAueydRgl1RxRXP65IsbCu8CbUtgN093aSSJ5rY6OaGGK7YfULWhKcE2tpPHKMozQfzArw9aJgHuH1amyNBuHpeTSyTsfvYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=QcS4VyWQtEFf2Hdv9qcjAf4Joa4Qobt0xUi12avlSoqFzorsFPLgn9cS1dC9xpTdMJD4jad8G2P6qUHgmtlQDuBaXyaGWg_VkbDKZDktKVdWXG-HkZsAAuew-4FK-AUmR8acDu4uXsuTRYoFZK30GlMp3c-Rnj6VyFiHmZr0KK--xPQ5eoUvuEALhU6MSLoKN9VCZmDm9ak2khY8LS4PFHIHWSUni3Eqmcyt6EdobioI4y0mSzrcbSAueydRgl1RxRXP65IsbCu8CbUtgN093aSSJ5rY6OaGGK7YfULWhKcE2tpPHKMozQfzArw9aJgHuH1amyNBuHpeTSyTsfvYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران
یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139133" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=JbRmGAuZBdLpcthffGJfLZmpwqSajWm2Us_Z-0dHZmo2CRVJ9AijE5j1Q8anaazz-L4CBOvzwynk6OOGjbitxnDWcX_twtXXQEjjFgadG64XVuUnnHEKVFRgkHOjJU2SyaVoRBIyVjH--g5UrGEBvQHbyhBVut8bAmQ4eWt-tMLBpn3pCIP4Mtdeqk5dfxyP8lNW0seIklNC6TmSretn2wPpJcmOk5_DHRSPalyuHRgZXoAevmE9twToxZaWDU8eW5T5fsQD261PLc5Q906sqZsJ-FzznXEFrORzbqoXXpfrNLQ9qtGWJ2i3NhyzRnJKgmWT6PYmOgSrhQ7NhlMSxm-40AxkNsJ67-u4YL7k5JzG1wRMo7l8JTdUrnyTz35GgYNmlDpFT-lJCSXOlinxjaz3vs3S_eDtCQsZPupwhTgYiZQ1CyDLFbi0RdxSolwYPCUgoLIJlHeBWJcPnGwPh6vikg73-J9xTSeVwmsS1xjxiEmeAqAqZhFTSPMePrLFLhOdn5jIL1QQ_asVI22JRbRgF4A25vNvht6BvqMZCBzT3rz1N7iE-WQ0eU0rNpvxYWN2sdJGZeDAOBn3V-vDgrjG_uuO1L-dqCaIs0iR_rzGvnTUW-34YTdg4T3u7O9fW7uZSKkeTQPDWT_YTPO4aLxyQNKMXR1fxOYsyMy1o6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=JbRmGAuZBdLpcthffGJfLZmpwqSajWm2Us_Z-0dHZmo2CRVJ9AijE5j1Q8anaazz-L4CBOvzwynk6OOGjbitxnDWcX_twtXXQEjjFgadG64XVuUnnHEKVFRgkHOjJU2SyaVoRBIyVjH--g5UrGEBvQHbyhBVut8bAmQ4eWt-tMLBpn3pCIP4Mtdeqk5dfxyP8lNW0seIklNC6TmSretn2wPpJcmOk5_DHRSPalyuHRgZXoAevmE9twToxZaWDU8eW5T5fsQD261PLc5Q906sqZsJ-FzznXEFrORzbqoXXpfrNLQ9qtGWJ2i3NhyzRnJKgmWT6PYmOgSrhQ7NhlMSxm-40AxkNsJ67-u4YL7k5JzG1wRMo7l8JTdUrnyTz35GgYNmlDpFT-lJCSXOlinxjaz3vs3S_eDtCQsZPupwhTgYiZQ1CyDLFbi0RdxSolwYPCUgoLIJlHeBWJcPnGwPh6vikg73-J9xTSeVwmsS1xjxiEmeAqAqZhFTSPMePrLFLhOdn5jIL1QQ_asVI22JRbRgF4A25vNvht6BvqMZCBzT3rz1N7iE-WQ0eU0rNpvxYWN2sdJGZeDAOBn3V-vDgrjG_uuO1L-dqCaIs0iR_rzGvnTUW-34YTdg4T3u7O9fW7uZSKkeTQPDWT_YTPO4aLxyQNKMXR1fxOYsyMy1o6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
بخش دوم صحبت های تند خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139132" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎙
درگیری شدید خداداد با خبرنگاران یزدی
!
پ.ن باز شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139131" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139130" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139129" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
گل‌گهر از سپاهان به خاطر کسری شکایت کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139128" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139127" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adbKHYrLGo8yAbq7e9q_gAvcI7Ml_nlPAUv0bZ1YJ3DPPv19YDdbRNzYCLi_P3Y8rNwO6oFnn2dvt4QOQDTmvC-cX-K0069KG3_WJB3LSGn5mScAMerzqjYFpcMDcXcEfWniafuD0-xayGJ0ZbQDAHso1O0B-oqZ4Q7ilr3d-cd-Iru4gnTWgf6k6G0ZJB8a1JwSfio2MGsSEFv6p-RY3QmdK2Zejk8i_CxBvZqq2dTDdgn3sBe7vNOKTB8JPqO2taZNJInPVIszqPqlMIUP3RN2e_8BO2FQpwDefjedEVrpbgEbkRV_cNOn7qRpTEuooSaPFAYp9uV7vO2QAP7s5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139126" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_5Z2IxgXAC13yPlru7R8OfjQ5B2iP9_-M2K0S9X73RessYNWp8qy32L9BRKeTfQcYZ3MzBNO-ZA5g4srNVztqCndGHtVvdTBOvzWHS2Evuo0TxOwumXARThqUfNsmPjaxzNSqZhSl5UvQngmscshHv9wL_x8o-qIy_hos9fCpYRcAcOnwxg9Ndu3ayvUEKan-EnLbAJRq6nKJ7G6k0W-lZiAIlYNsj_RxPhbEwN8wEJmvyIRv-JUt2XnjgQ3hggoDgXmNAN-o3XoKzZwRqdR5jGiFNqmRjoN8NDO15sy_qcGE2JGQTf1qz97NgIseT8od2_Ez0nqmv3IWHdccy8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرکت یوسف جامه اسپانسر جدید پرسپولیس شد و قراره ۵۵۰ میلیارد تومان در سه مرحله به حساب باشگاه واریز کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139125" target="_blank">📅 23:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
سپاهان هم با دو گل کسری طاهری .گل گهر و دو هیچ برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139123" target="_blank">📅 23:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
آغاسی اخراج شد ولی قبلش آفساید بود و شانس آورد که دربی و از دست نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139122" target="_blank">📅 23:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139120" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
بند 500 هزار دلاری در انتقال بازیکن پرسپولیس به نساجی
❌
❌
در بندی از تفاهم نامه انتقال قرضی براجعه از پرسپولیس به نساجی عنوان شده است در صورتی که باشگاه مازندرانی خواستار دائمی کردن قرارداد براجعه باشد، می تواند با پرداخت 500 هزار دلار به پرسپولیس، قرارداد…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139119" target="_blank">📅 22:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌬
پایان بازی
نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139118" target="_blank">📅 22:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139117" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oB3btvK2W0fNOz6o9x20xKe-7y_KZ0lnXORXjUTICXj2SAr9WwVFscGLi17zKNrQhP1otY88Z_gSUf1ykkkO3RxCBPmJs89fKfGDu53QtORNy7NF0qZ4dwzm7Subh9ouoTMckUra03kuX6C-o33i0ErpAFlDeeoBCPOmFJYoxok_TQpiMEuZYvG-5dN9CQSuKoJhi-OgZMKBjsliHk3KEI_1_eUkGA0gnvmzGrsa9cAVEgYMnMlqihxb_3sw8m4-ll5FyOx70hFQTlMf988hWun-fdpJqRWoTTaaEXaPU3P9cPxBMlRayaPtWhP-MTKuM6u0sSENu-KOYIp4XCFyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFs67-iaoN_Hq7krPLPkCIMlr7Pd3fBZCq30jDLDvgnt_algz7VmwoIlLv0QJtrcRQb_V28XDE3tJ5V4duYVtAoSzel3piE8ngvWWXPvUb0dC_0tbTlnFYT1ARaSNahiz7S4xzEO8sOOSB5zvbPv0Wt6IekQ6NBYuZGYzGPakwfqv5OjPcdNuQLVU8wsM-fh9saLDUKzXYb8LzwA8zl3qG4YfjAxDjgs-Htgd_E88j7NXfS9HXLXcl9k8ZmnqndUVzs-dEFqSzZFeOi8rXBxU51biZSP-SmMkkhmsBAXO3B6X6zIC5Sl7VTADHkSDqJLS-bWY36q-Kvu4uhCYABbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sLXY5Bfw6XxI-b8CNmUIyljk53X2CWSAhVpgYrLSF5BVKEuQZEcU-yg5FZKDpYPDIDL-b0edaWAd6iNP3pMetRKxm-72gjE9dkumtT_de8Q7fAYoMMjLBwlJT7gMMPGiPS5lQ6hypzMNhhgj0QcH3_Hna9uWgO-M_eDf34SMs5Ox9DLQFoiljKrZL6wqbUxtu4bIrYqgLIzfu1Hha59iZfsfWqV6l5PRjcGpTopw3fEwYZ4IYj4m37_kCYErPbMMiEwQ-TNwsRjVdAb_9kZwQpuqG7MT9ZU710y6GwdHWWlM4pgNVAFH-VVK6xllaOGIReOKtdHhCuASt7uk_dMeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgYtHqaQBqlOxH40p15sLebf--Hp9ryOAWqXIjDclBei0cdqyiOs6MzsPRrZz1zvRhgbGkQoNops5hw0Vnd43L0EYpLSqEplrk3sd8AYTbZmju-ISYKwe7vqbVIdJqOqydTKRNRlSJ909I5-hTHzXHer1obc7l0Z2pAAiq7ixwaVjPR2VABlTDLlWPfmbS2Q6HhOfC1Un5Q1ABZLaOPTAl80InHBypp8xPy1A5gwYG6Qwn_Qi_UiboDep_lDW_LLL81PcyRBQadY4TcqPjFf8w_X6_76J_q51-hL87vBnpHXGWFZ54vlicvDBm72Bt35X81XD--ak0WzkdTReqbtEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽
🤩
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به همراه ناصر محمدخانی، بهروز سلطانی و مرتضی فنونی‌زاد رفتن سر تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139113" target="_blank">📅 22:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139112" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139111" target="_blank">📅 21:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHpILZt3SSSxd-4X9sQO7lZfrBDH9XiRbxaPPvO2DvftWqKiVNdbN8GEylSBkv6X155HOMAypWL-ZF9i0OFLWqmc0gBt95SSSmZBH-3WnU22DY4d5HMhUIUIgA1YgA-QB35FShVa8nMmwzYYwJXYkGcGD_nMsb86fgfc3d0H5J1sEJuoox9yEKziRP3byhByCgWsjpXh9f2AxTQL5v7uRUrUO7nDc6ksRg1iHsUE7WwX0lAAtNt4_ImJVYUijHqgNhJY3P9C4wLWL6pYWAzeoOR7S6EhyDvwqTWehqZib2nm2XOfKOYZ7ARwpT7FzrVx9NjHpPH_r5WyIONix7xxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139110" target="_blank">📅 21:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139109" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcON1S63JsPprxT3fCSUUQ3uFosBjZ72U-wZiJ0Hdx6WCcKxpLO6kfP-wXYnye_UT5I3fmPgai5K_7HiHnNgqBf2U_bYUb1_yykXlQD05fl42WqFuunl-9xzFbg1k-hNpdiRwXbzGSAVjZ3RSDTUPlIfhNOnvhIbMJfAhqilfch6dIzbZNlnL6luGdzF6oqYhe4tz4aw1gZXOiNWU8pJyFWgXDY7CyEsm0rK2iMFCqCPrM5qqGvm-Issq1b_wjppQgD4E9RZfItAOKBJogWQRsQ2ZVc1K0Nxujhrcb19YbK1M4wwjIPUiNPLH5IaqpAEBrhmr07kJZayZZIN20lIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139108" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=s44m-njfvJ_q6bjE_E4S2LWYpLZekONTn6Oq7mnSG3M_U5MAyXhxxIcdoYnNzg6YJln1VYm1qDLICNOVXu8jg4x9bf4Y47jGiHVkID4ImNjBm0TM7HNddSBqPrYKnNaveW_3YDM0-so-zuTUnG-qZbFRg15W_5d3m3CUwi_A7xxr-AkwrFDq-Huk08AVbvYmi3Il8AdPIRDB0Ch6A_6VetEkejW-TR5mUOBpztRAFAltz6nG5-2pvQrXaihmEx5WljQadjvnOPKRFgpxRtLgPfZ8Ea5Y9KjnmuujEDtGVXuLKkcQgD8OXFlGuV0vaVzKSrvXM_JbQrJO9brKlJ1eXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=s44m-njfvJ_q6bjE_E4S2LWYpLZekONTn6Oq7mnSG3M_U5MAyXhxxIcdoYnNzg6YJln1VYm1qDLICNOVXu8jg4x9bf4Y47jGiHVkID4ImNjBm0TM7HNddSBqPrYKnNaveW_3YDM0-so-zuTUnG-qZbFRg15W_5d3m3CUwi_A7xxr-AkwrFDq-Huk08AVbvYmi3Il8AdPIRDB0Ch6A_6VetEkejW-TR5mUOBpztRAFAltz6nG5-2pvQrXaihmEx5WljQadjvnOPKRFgpxRtLgPfZ8Ea5Y9KjnmuujEDtGVXuLKkcQgD8OXFlGuV0vaVzKSrvXM_JbQrJO9brKlJ1eXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139107" target="_blank">📅 21:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139106" target="_blank">📅 21:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKeSEHjUWH_zbM-rc7428OSuhma4f2_cBGnccH_viSAPmfMRQheVdisKuTCpUgAB-s21D3RBqPJ49EzzC2Rhib8vNyZApSxBhqdmI5Er_viRv4mQwG32yWV8Rouhc42Z1T3HFj1MmU7h4Fx5R-vUmc0on8W9oig4QmF9ooxsDJ6Q15rZCaze9VOpNnTyWQ2mczI2gv0F1Yp9XZO0X6Jz8v9Ml5Floz8Fbhsqvf0mdStTzX7oBQMxHgJkSqitJD_-KDTN54rd6_3xk3l8p-Tei6jXUDKY2bQzrhjSm-Ijg_f4HsbcJC1O663m0zOO2kj0bIxSLEac3WWpBCPflZjj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139105" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139097" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
