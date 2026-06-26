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
<img src="https://cdn4.telesco.pe/file/uTaIMdr-YgfQFrpbEsWQClbZ-9T7MzWhbMPkrZ21uNNbmEsn5zwmaCM_Ezgv24m6qICRXvAhAa7nxXR1f3ypexwniP4w3h33b7q7FgpsVbKBpPlyJp_J8EWpNWmbodwKsEECjj68v8jEg7NuSxTPZXu1FF4_7UnGmwpsRX3YY0s1UP8yQkTWq_jvX4FndsgB_nyTKu5hxqjQlY-OQSNNJx2BvrwQx6_NqzvlorHJUl1VztGjNNMjJWbf5dV1DkuiN4VCfZC9m8etrI9bl1ygNdil9iAgbNJoZSfQnvF8oxwBvqs_LkFEtTau8a1ytZJSlxzyvuCw0407_w7BVGlxKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هاليوم هاليوم نعزي فاطمة.. جانب أخر من شعيرة "ركضة طويريج" في منطقة بين الحرمين بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 367 · <a href="https://t.me/naya_foriraq/79931" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من شعيرة "ركضة طويريج" الحسينية في حرم الإمام الحسين عليه السلام بكربلاء المقدسة، الرمز لنصرة الحق وعدم الحياد عند مواجهة الباطل ويزيد العصر.</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/naya_foriraq/79930" target="_blank">📅 13:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايةُ الحشد الشعبي تتصدّر حشودَ المعزّين خلال مراسم ركضة طويريج، في مشهدٍ مهيبٍ احتضنته كربلاء المقدسة .</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/naya_foriraq/79929" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/naya_foriraq/79928" target="_blank">📅 13:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/naya_foriraq/79927" target="_blank">📅 13:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
حشود من الاف المعزين تشارك في إحياء شعائر سید الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/naya_foriraq/79925" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق شعيرة ركضة طويريج من كربلاء المقدسة بمشاركة جموع المعزين.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/naya_foriraq/79924" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/naya_foriraq/79923" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM3VAFkJ0PCkQfoh6nh-S05mMKB3ZuhyJpO0iwS_Pj0d6v3ayMLtSj0L7jWqrprImu4kSrJcIPs-XvUI7I3TgmnZuY_SnSiisuYApfhqf3Qzk2kXkuSTr5MpAL6ZepDBaI0LZDHtMuOGyxB_kKjUpBxqWfTU3_7NnaeQxB-hQ3lar6UKWFsapT5w_FpxrbvAwiJyuSY5IZ_30BL-11P6UuzNAyOXKSoQ4RYOpxZ21d97glTVXnetCtg3_StKu54QjKr7qdayNwP078FhEzdX_SWLv_lWaiz-GDYUFW0WOaa-_oZ9PLeiQ7H1zArBk8tkAX9_i25TuaSidce5-apbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/79922" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79921" target="_blank">📅 12:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEe-wqUY7fN4NflqM7CIreZdh43ju413muvemM4oR5CkD5bNbsIOwG86Cl5ohUPC4jH7FCBGjbrzCL4hketlmqMFdQQSG2uMccDOwSVj9dJPCq6jvQt92znU-C-CUEzULtMlx9nczrifkKFj9rhFvOZ6qwma-gsoz4eFhxdA5e4R7vawnRSuL2BCHJqUvSSdWDZaa6QCXm5kDhDoAQBUd3o8cPIQfEQ3Kqf0H9cukdHk62SHQF19YSGLIX523wc7wvYyPh8kVzQ5yWk0zeJzKXfH1xtX0HxAq-pl_LAqb391hWoOBbZlcl0Mt1fsqp7l8ZnXdMCx0OD5H5zR2TQ-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم ، كن انت المراسل وانضم الى فريقنا
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/naya_foriraq/79920" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0-mDi-UN3NIhOwMpw1OLcYhNEQOwOGujvac_HH0uPFptFMdDazKQzqu-tTch4MLPzs8VWfNU7javYXFy47bD7ddCElYdYOwZvF5r0E4iA9kLVo1Pu79_a9Q6RGCstzArMqbuInMQHZS2Mtb2mlBXSwkZeV86TbmDawgM7p1ke3JPVQ9-hmCZuQy3yMP3HQRAOJjmtoXUhLrvIeEZfJVr0AhUmTS7H5ZSnulRJY88_a7x5lYyrn6Jj-WaOS-B78rKXtkFk86V-1Bn1r5SWD6hs3gFaRt_ZWAWypz79S-lSKLTRfpQN3AvcGuFmL7qs8Wm7RRwCutRkoJs4_VH93krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQJTEOrvQydf3th1DmyaksAtwDbmNL21hL7Vj7YTtr9Mchu73P6e3gqkSqRuoVt17nXNzoWnCqRe4cZHS4rmryELaGS2FFVH8jTGGIrn_nW9QqpKRNYdTa-JjwYpDc9eG_TT99L6z08jC3zZfDhjanBY2jRZH7h6pCNncwcPFC5XmG3h4FknZBR9ScYtGl2oBM90WZOBmTH278avCmTZy1NJuxSKtmlYZ5HJT7WWVxhWU-ONzvdHl6IwvHdDcJhSNsYWq0Tq0QY6x_AovnVczXTlx_TKIg6b8B8f72y5IvQ4fKL_RrNJbCp-EiqRD02nOapVZLZ-DD80fIWaC8RjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeNBT9A27YmCSETZt30k-_sA8hnU70-19YEOdYCIjB4g3hltrOKTiCcXGP1JzOxBWrPsXq7lGl76tInTaoP_eqjqTl3IZpzC8aurIL481IGrAH8kNzbjnhvRIT8vP4GbJwS7_E88fVyFTr2gEi5LtYiTZVrk8eX8BSytP3wZHWv7kQGCtLCMjt9OU0EckSI1ICcrP_W6qvLdNtHjMFxz7a0_qMKguiMIRiEAocbVpRUpS_NzZeIejsAhLmfvp7m_-7AXC-yENHJs2XX9rVnasCsW8kz5YrBRkDz4_TU61DQlsnKGxatOYq-L8RlMKMwp2pkIIyWPMlCCWEKY0olRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zq36gUR1ELdDV2ptKab9id6JgiqOroTMPehqBlIT7BhQfF3A_T6DX4PQ5jImKakkS3V2FL9PRZ_m6AlL67xdR8QYsqMNxm6hLVyEMtMyaTdyhYMI7BrXjooOV6YQbEdpq77Zpro0EeAosMvCIQ7-bmyI9OQSZAkpooTWi7VtLId325HMzKa1DLpC_j68rq8lCVFufL8qg685xVtBZlQ2832nyqlVNz4UJXMAk4ChfEqZYr5N3rQcALDeyaNkCCfOpA7Bwb2QcqC4-_OKp7HrrIrx_Hler9vx_zHIZIbp7rrAo-81oWACmRs_zIwY8qWQwcXFI1xhkZ5r_yWcGFinbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد إيمانية من داخل العتبتين المقدستين، تزامنا مع اقتراب انطلاق شعيرة ركضة طويريج.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/79916" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=ifx03FVjSTnjoy-MQ5NrSu7AVzK8ZCHglapfuLT3Rq04D41Gkgpf5pq2TESmCkHZbtSJ5SA287FcikjDKivjLi7JQKde7BmxJmAZPS36uQws1Jgm0oHPsx1nKl1XmUHlHYEqsXTZ3P1WOECiZXAYt6NtdZpZJAe4yBIiMGEArIGkSgmnvHHpdZEbkfANqr9rfth7E_e_qmIdMfjAJt1fgKWOqAWhzOrTqLDN_tt6LcyDoieh7lJtJA9q__P2euq6IE-5su7MIa8Omboe4lLtBnV7P7J6NBUEWYvE3DOousTWmBizsy8WxGDUIC7EOfCwCxerPIdMzMQ_M9QzwpG9koghEg2loDojv7wQdpxvdrDMY9I1qRWT5GnhNjbWY397fZSTHnHe_5y3B4ibSO7TkTVtEMUbbxTAMfQJ3vYEsfXiNrIqe5uWj9ikxav8AsVfE0JyhSV-7LwT2vIixhR5BDNzcGKELr51Pqk4FK7mMuwRNy77qqg-L4XMvJo0BZnd-qODlDYm3HyT71HQ-eKuWv2mN28pQP6iI-swgeqsZn2-FpKqdfotPan8PScPTEuULOFuPKSmxmoxeRC-LjeE4CK4MsS59L5IkrAaacvIo9mq0kPt80F6-ugNAzeIjWy19CU8LikBZZJoJnk_ciQBdR1OKZcBOKZUvYu2cIPf9z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=ifx03FVjSTnjoy-MQ5NrSu7AVzK8ZCHglapfuLT3Rq04D41Gkgpf5pq2TESmCkHZbtSJ5SA287FcikjDKivjLi7JQKde7BmxJmAZPS36uQws1Jgm0oHPsx1nKl1XmUHlHYEqsXTZ3P1WOECiZXAYt6NtdZpZJAe4yBIiMGEArIGkSgmnvHHpdZEbkfANqr9rfth7E_e_qmIdMfjAJt1fgKWOqAWhzOrTqLDN_tt6LcyDoieh7lJtJA9q__P2euq6IE-5su7MIa8Omboe4lLtBnV7P7J6NBUEWYvE3DOousTWmBizsy8WxGDUIC7EOfCwCxerPIdMzMQ_M9QzwpG9koghEg2loDojv7wQdpxvdrDMY9I1qRWT5GnhNjbWY397fZSTHnHe_5y3B4ibSO7TkTVtEMUbbxTAMfQJ3vYEsfXiNrIqe5uWj9ikxav8AsVfE0JyhSV-7LwT2vIixhR5BDNzcGKELr51Pqk4FK7mMuwRNy77qqg-L4XMvJo0BZnd-qODlDYm3HyT71HQ-eKuWv2mN28pQP6iI-swgeqsZn2-FpKqdfotPan8PScPTEuULOFuPKSmxmoxeRC-LjeE4CK4MsS59L5IkrAaacvIo9mq0kPt80F6-ugNAzeIjWy19CU8LikBZZJoJnk_ciQBdR1OKZcBOKZUvYu2cIPf9z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/79915" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/79914" target="_blank">📅 11:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk3xP6sfAScrCOCZRmk-IHHe6urRVdvK1-SOLDYqNL8Fzw3HgHeO-ZCq3lktU1ZNyD398hUOnw-Nt-qk5LgnavNpOPxbNA0HYUjPCGzhrz-vpufYUwD8wEv9G7fp4-6p9vOBujA8JnXaazVJHFAEFikpD25_nQ7zbPmJTJ-0ehjVPV58zz3rh_B-3qgpOfR2kWaDphu4oT6UzizXmbmnbQswYFoJq1kXwqfXBi6raMYIVFus7l1t7lDhR1WqGgTdSOg2XYUgJlh7p_sDwp-UCDEcsgkrz3bwCox_VFf3k0_-or5gd_waR2WFnoGjFe698GfNTZ-tOS-7pRLms0JAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية بشأن البيان التدخلي لروبيو ومجلس التعاون الخليجي
تعتبر وزارة الخارجية لجمهورية إيران الإسلامية المواقف الواردة في البيان المشترك لوزير الخارجية الأمريكي ووزراء خارجية مجلس التعاون الخليجي - بتاريخ 25 يونيو 2026 - تدخلاً غير مسؤول واستفزازياً، وتحذر من استمرار السلوكيات العدائية والتدخلية في المنطقة.
إن الادعاء بـ «الالتزام الدائم لأمريكا بأمن دول مجلس التعاون الخليجي» ليس سوى كلام فارغ وتحريف للواقع. لقد أصبح واضحاً للجميع الآن أكثر من أي وقت مضى أن الوجود العسكري الأمريكي في دول المنطقة هو عبء على شعوب المنطقة وعامل لعدم الأمن والتفرقة في المنطقة.
إن استخدام أمريكا للقواعد والمرافق العسكرية الموجودة في دول المنطقة لارتكاب جريمة عدوان ضد جمهورية إيران الإسلامية خلال الفترة من 9 اسفند 1405 إلى 19 فروردين 1406 أظهر بوضوح أن أمريكا لا تعير أي قيمة لأمن دول المنطقة وللعلاقات فيما بينها.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/79913" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم: - تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.  - عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.  - سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/naya_foriraq/79912" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم
:
- تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.
- عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.
- سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين في الميدان تساعد في إيجاد التوازن المناسب لكسر "اسرائيل" وطردها من أرضنا.
- لا خيار أمام "اسرائيل" إلّا الانسحاب الكامل من كلّ شبر وأرض لبنانية وإيقاف العدوان الذي فشل في تحقيق الأهداف التوسعية.
- أيّ التزام ضدّ سيادة لبنان لن يمرّ.
- سقف السيادة يمكن تحقيقه بأن نبقى في إطار اتفاق 27/11/2024، على قاعدة جنوب نهر الليطاني حصرًا.
- المقاومة مستمرة بوجودها، وحضورها، وقرارها.
- المقاومة هي عماد استقلال لبنان وتحريره.
- لا تستطيع السلطة أن تعادي أكثر من نصف الشعب اللبناني.
- على السلطة السياسية أن تعيد النظر في مسارها، وأن تعمل على جمع الكلمة، ووحدة الصف والموقف في مواجهة العدو الإسرائيلي، وأن تتوقف عن تنفيذ إملاءاته.
- نحن جاهزون ونمدّ اليد، فانتهزوا الفرصة، فالمقاومة قوية.
- هناك ضرورة لشحذ الهمم، وسدّ الفجوة الاجتماعية، وإعادة الإعمار.
- لضرورة الاستفادة من مسار التفاهم بين ايران وأميركا كداعم أساسي للسيادة اللبنانية أرسلها الله كهبة.
- لقد ثبت أن إيران طريق الخلاص.
- كفّوا أيدي الدول العربية والأجنبية التي تضغط عليكم للفتنة ولمصالح "اسرائيل"</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/naya_foriraq/79911" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=INKZ47Bh3JuSSifDva62QgeJrjtZYLkgFvYqTqxictNi4X4REJGMdteYh9tlyJW-iTvdzTyIzYKeIU49o3JKk7fZJC2E1Lvaqfmuijzjb6wlmu0kYIv2ZUKQeY3Id9E4W5YZF6duT53MKOSva3EwZY-eWP6WkmmOq-gF759KRDsfcwzjCSQjyprRdBtAKARKaL2p-ZhLw0hjwX6JvQNsk_vt3RF-eMqsuzyAke68WttA87K57VFmoLj9Dg04huEOZQGVlnHlMcFE1AychIsbnErvyiG7ULI4L8uTaAcflQrfs1a-J5eRnRWY9ZCjhpzVu4QDWxWvska3p6haVj8ymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=INKZ47Bh3JuSSifDva62QgeJrjtZYLkgFvYqTqxictNi4X4REJGMdteYh9tlyJW-iTvdzTyIzYKeIU49o3JKk7fZJC2E1Lvaqfmuijzjb6wlmu0kYIv2ZUKQeY3Id9E4W5YZF6duT53MKOSva3EwZY-eWP6WkmmOq-gF759KRDsfcwzjCSQjyprRdBtAKARKaL2p-ZhLw0hjwX6JvQNsk_vt3RF-eMqsuzyAke68WttA87K57VFmoLj9Dg04huEOZQGVlnHlMcFE1AychIsbnErvyiG7ULI4L8uTaAcflQrfs1a-J5eRnRWY9ZCjhpzVu4QDWxWvska3p6haVj8ymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ازدواجية المعايير في ابهى صورة لها:
في الوقت الذي تُنبش فيه قبور الدروز والعلويين في سوريا تسارع جهات سورية تابعة للجولاني إلى ترميم قبور اليهود خشيةً من رد فعل نتنياهو.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/79910" target="_blank">📅 10:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء:
نعتبر تحركات ووجود الطائرات العسكرية التابعة للكيان الصهيوني الإرهابي في سماء بعض الدول المجاورة باتجاه إيران عملاً خطيراً وتهديداً للجمهورية الإسلامية الإيرانية.
نعلن أنه إذا عجزت الولايات المتحدة عن احتواء الكيان الصهيوني والسيطرة عليه، فإن الجمهورية الإسلامية الإيرانية لن تتسامح مع أي تهديد يطالها، وتعتبر من حقها الرد على هذه الأعمال الخطيرة.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/79909" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
مرقد السيد حسن نصر الله قرب مطار بيروت يعج بالمعزين في يوم استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/79908" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwi2RNAmTBdik5ebi0qgla4tubMuSCZffKNiAqCf9qQbqKYoL-GWv7sFKvI5EITrpWoXofBpolqlX5JbE-F3bMl1y9vxMnc5EGM6lGdL0eQ4pOxprUnoiB_dI7CshwKHZhAHCRv3csGgtERtsjVHrXVWIU3mvWpBiXTy1Cejhkns0T7xNTiKKpa40i7QBuxW8TBFzZI7cBEk2c3_RKM5XcGD5JDSN1CVVZkfcnT8_jmP9gUma3CIjQvURzTVhQxAsU__41BZ2YKMiihiY_jhzvQJigl8h95R2Fi806xxUI5JBwoVjBDp_p5ob9fhTGXJwLJ0x3Vrq6u4XI40P2JBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RggLVAT_WkWuwYQ3GnjGSOy0Yx4L2u8sZBQAvXhRpbEujY9yagjbLdnAZb_rRsm3kfxQe1VL44-qzYaT50Up47ySOnoQ7ozJMt4PBWnxubgKafD62sRRcE3zCm9v0R-1kMFS9UvgmqJ8b7dwRik6cznCQkT0EosuXdTaTgubbiMC-cC15lIFifeZS07wtyPIECrtppsjL7onY0apVtq0tjFI2tpIWSKsEUujle2rugyJAgJk92tz566eBo7pUv2LLjgoyZTw7InVZoAkJlo2bXJ7J4fTOmx8gKWTBRwmVxN3dnQ7EmlxSEgETaqbHOSH0SQUn-hZukrecH2aAW9KRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ma8WVfMa8JNWch4UjTiE8PScXcer3vlAujSC1y7FYg85oXuYEhTG39JAl_mtYC5fCBmn0yJkGGqVWYQcAEfsWsRGRLFfyPlDjuvWwvmWOQT6EKW3qnBBvFN19o3JuVPlPPtSE1TzrL3Ov0PSVaxyEkoRSHyVOt-RxgSG8mfPwi5jTo7zamHiYAK_DnQ_127F0fmG01SgDszWNc5ey-6K-7lsCQ9Lv2hkMra6r2DykNbLSXeE-Bne2U5tgb1JQe8REV2DUD2efDQaR3wTZswuQvurJSOoHRgCpcNI_J7NWwUjbt8wI-NezwNRhDyd1aSVKw1nK8BkxnywEVa_1dq5KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جموع المعزين في الصحن الحسيني الشريف بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/79905" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duCAFmN-thaZkCMYjsJU2Jgbbm8o0-06mcCpM3ULd3ebg_4Tl8zuUrYqYC3lgkhbLOs3pGOfpICazbW6cyGtZkph6hUMoht_-NLmV4Sl2dvjJEKAOadwarD-8FqiZHYdfLUpRcByLsGsZUjaQ2Ud4PKWAFtTT4qHcd-tPUhZNYB-a2kpUrJZiJ0KnDVUK9izNRfU5ETQGbAHBJk1hRsn69hPSbQIPRPyVNdTXbpjfMyV_y0Lf2BGw9hn9r33SPwxE__VaI3M9JssUvC_KdlxVk3OvhZ-Uog69jRca9O8ZT6qmkSnjxAmqEbRBD-qKusGiAE23P7J9WedRwhUmI4EYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
أربع هزات أرضية تضرب الحدود العراقية الإيرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/naya_foriraq/79904" target="_blank">📅 09:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=HrQ6zSd9_VWLSbJyOeQRbJbIYWrpSZNo2S9QguM4T0FFhmv17fduulizGA1tnmNFShWyGcGkI-7d_m_wSm6B3Xqlw8lXgMbQarkZ1WqKlVjKtInNfKPTMgsyZhWBNtVCD0txdpPCk2VZDyBCgJSA-qtthdnhsICq4_oGpyFgzaQh5ZOOszwDr4yMxnzD1tbFyQDpnJ4kSkjwOwt7E3csxUxdQbMJw99v323ligefy-knDIBun-k0NAZN2C_iIfXgr_ftuCJgPDXw0xu6ixPu1elb17k3xLC0uAoUFloGQsaiMIqYZrq8D1MEhfh4GD6OaZaGl2bfRQ91bF6zy5-29CkbaXHFb-1RLc1OphC8nuUKZKDn8t2VWGeCPL3RqlXrK2OUc1TUxSrgje-5lcf6a_1VQVpPyAAQCjBPpOOkaKiC9XUqIunOXtTa_M1K6ZNqYJqJ_M7Z24whoPD-XND12ZvTGnwG42mcWanUpQsK3YpOReRKiVFpuVSwKWpBvpTuA89ESddC4f8KMCmgpdpjYhwhDXjLYZzasG2yOGgZhe2nJIDQFhO3XHr99Uz_WSmCYXbFCa7xPwoFBzBXKXwhWYO9YDxXOqHsDIxvNW-NzNN4-U2ab3JotmxYXXiGEGrtjKKuhb9ISiFunpVlPHZNGuCGHcty4m1qWNhDlxnhyvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=HrQ6zSd9_VWLSbJyOeQRbJbIYWrpSZNo2S9QguM4T0FFhmv17fduulizGA1tnmNFShWyGcGkI-7d_m_wSm6B3Xqlw8lXgMbQarkZ1WqKlVjKtInNfKPTMgsyZhWBNtVCD0txdpPCk2VZDyBCgJSA-qtthdnhsICq4_oGpyFgzaQh5ZOOszwDr4yMxnzD1tbFyQDpnJ4kSkjwOwt7E3csxUxdQbMJw99v323ligefy-knDIBun-k0NAZN2C_iIfXgr_ftuCJgPDXw0xu6ixPu1elb17k3xLC0uAoUFloGQsaiMIqYZrq8D1MEhfh4GD6OaZaGl2bfRQ91bF6zy5-29CkbaXHFb-1RLc1OphC8nuUKZKDn8t2VWGeCPL3RqlXrK2OUc1TUxSrgje-5lcf6a_1VQVpPyAAQCjBPpOOkaKiC9XUqIunOXtTa_M1K6ZNqYJqJ_M7Z24whoPD-XND12ZvTGnwG42mcWanUpQsK3YpOReRKiVFpuVSwKWpBvpTuA89ESddC4f8KMCmgpdpjYhwhDXjLYZzasG2yOGgZhe2nJIDQFhO3XHr99Uz_WSmCYXbFCa7xPwoFBzBXKXwhWYO9YDxXOqHsDIxvNW-NzNN4-U2ab3JotmxYXXiGEGrtjKKuhb9ISiFunpVlPHZNGuCGHcty4m1qWNhDlxnhyvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً  إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/79903" target="_blank">📅 09:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3pM-euAlILZjlcnZyPr3xD9aQWvhrCaCkKipKdQb7uK6VYsa55vo6gyMRtiqa8t-QHyrOyArMVkPrF9_tA1EZOAGcZW7OtR9-ZDRsyJFeoi1D_yVFbI3JYrm_xLSpJDBI63jJSD-RWg-LzPhfDsdsozyCNogEdRu8fW9MQypLCuYlA0UrRWmeBlQP6XKD3qrNQBPsGb39uzNA9fNnZC8eF4zoESAPdCh9ssmZI5J170ln9VZQozvPAMic-6sYLtJCMzPkpn4olagR55aYGKKfHa-bbohgVXraivemB_iAs0KMjiOa9p4YRTAnM3Q9tj8tchYIUzdVGPA5tZYvjj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدة نييورك من احد المواكب الحسينية يستذكر الإمام الحسين بن علي</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/79902" target="_blank">📅 08:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLYO4DQcxODKHj4CgDZ_Ty7k-tp9nAJHmxwDfz6CnqMAUMqGutVOs9Gil0S5v8batib_Fj_qkEulUE_M16Q0ZvgSJCnzBt14F7vVMFFrqmdn0PR6K_cNMCldrC_WLlAojthy6oMqpqZKpZFrBdoPa2xxOa-66Zgr2nU9gfHzmLOYRTtaa1Unj9hWbaf3wvVgWh0yPr8sre67n_q0VXHJauqe1dlGuPUxHfmDZxLOS_SuupqPOJ8MXGsNjuaq6UgZlJkXA9VB34sB4lRWXHbryyrsZaitdxOYeJmgFTA8LeJinjP5KN9vQBsvR2EwlgNtBoc5IsYdCBNVG5lWdua4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM8i3aFAoJXu8nP8BYOyLOFGHTHiZ3Tr7Y5DWPIv5j2mIvdXLJuFKfKElwl0PuYFWzJkbPJuZltEMYKSdmzHZmhNgsAMMPiFC0d_sA0uFo3ddKAC72ZBs5kjIJOormL9gv0ewSEjHsx5GpQskuAZHSJr0L-9240F-4rwltRiQdPnkmRKwAvzLYfZ7J0VBLuiALanzIe6Wx7l3AHaQdS0AXGl6DwR4WDEyuRvJG9DAE-GIqR9nE65B4Cp1aeLRDk1PEuZxdgdsPm70As8KilZgS5TXoY81gu2b_QEuLSYvXpJkAF7TYSVO9mzFaPq6Rjb2lXt3q-g0AFP5XYpXAe8AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
🌟
رغم إعلان وقف إطلاق النار وأثناء إحياء العاشر من محرم الحرام.. غارات صهيونية مكثفة تستهدف النبطية الفوقا.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/79900" target="_blank">📅 08:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgL81fizKe4YED0HH-x3BArg1yN2Mkz-L1rKaqU9qu5Qo1bV8yZrKQpEoKqzjDkBSKA6b_-P5C8zs_puch7ef_tIY16yNUm1_TK21ecMyk1q-c9y3dF-r0JsAMY_nm4AHDsNVz9s9FKhX5yYLpdLscDUMG20SxB7ix8TrHNtFFF0lQwZ5NrG3fROG9CMghlmcj3wvBhP7f3wHJGmi8OczGAZXDWT7XsrK5frdZyKCphQ-O7bBJlxnoDMoliS8Iu6wb9s2Q2yDWfNFQO2L5JH9KcyrfmSrTUER2elp3DjqPcgORbv30H2zfWEZxTh7I4i9l20wEUnGP3bRXeqAYWbnha8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgL81fizKe4YED0HH-x3BArg1yN2Mkz-L1rKaqU9qu5Qo1bV8yZrKQpEoKqzjDkBSKA6b_-P5C8zs_puch7ef_tIY16yNUm1_TK21ecMyk1q-c9y3dF-r0JsAMY_nm4AHDsNVz9s9FKhX5yYLpdLscDUMG20SxB7ix8TrHNtFFF0lQwZ5NrG3fROG9CMghlmcj3wvBhP7f3wHJGmi8OczGAZXDWT7XsrK5frdZyKCphQ-O7bBJlxnoDMoliS8Iu6wb9s2Q2yDWfNFQO2L5JH9KcyrfmSrTUER2elp3DjqPcgORbv30H2zfWEZxTh7I4i9l20wEUnGP3bRXeqAYWbnha8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً
إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/naya_foriraq/79899" target="_blank">📅 08:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=UcukNfatmA6RFTE5TCkHbFeNE_peouJv8ldo2FHUvLixOBtXiqPukZCJYmU7_ecAVVb7vhnUCXDMx5kVYgtD7XSTHneyUglw204bUpFVuRhw36X1i-ACEUSd5laX-2c7_-Pt5lOphQOxhI0O6x7GhCMXsyzeyIB_SzXgL-UXILqUsP0H85UIEDsbS8LEb06u3YKmsQ7eEGhG3b7ZalBPKCP_kr8LW58U8NITpsPpZklqz5WUOhhzYmgCOlzjJUVz-4xGk62d6Gg1KUY6-h8jSpTYd9KOzxBMAYLEQNKIGWOrZlDUyobas6RhogVOm8uRQxKAFUS_CJh_6mWC3QXooq5hxRQL2lm4CSJpjHIbsKko8t7Q36fPVwgHklPwUFumaTTGgizj0e_EwR8YzxAZz04YqwAYN3FyyKAn5hLWaI8x8p_Xdrj-3Kwmh5NJx4xo6AljrS8o4hBXJBB8QYrkUA8NwpXYWel51cItKpVrTJKPKX-z3dzWq1n1I8o5919O_Uvyk-4JxIiXOngZcGKkFeXaDsGtrccC5yYY5kycnplrT0Z9EwmszAF3sANsfAcJcGp76HF5zjIwTs_09AGyhMvtR_urBkDRvFcPxetRo3h4CgQyV8jKsuqVy1E9g5q3gSe5IL4UmeTw3oO4K-IyC_gmV7M8FzoY-J0YRGEl8ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=UcukNfatmA6RFTE5TCkHbFeNE_peouJv8ldo2FHUvLixOBtXiqPukZCJYmU7_ecAVVb7vhnUCXDMx5kVYgtD7XSTHneyUglw204bUpFVuRhw36X1i-ACEUSd5laX-2c7_-Pt5lOphQOxhI0O6x7GhCMXsyzeyIB_SzXgL-UXILqUsP0H85UIEDsbS8LEb06u3YKmsQ7eEGhG3b7ZalBPKCP_kr8LW58U8NITpsPpZklqz5WUOhhzYmgCOlzjJUVz-4xGk62d6Gg1KUY6-h8jSpTYd9KOzxBMAYLEQNKIGWOrZlDUyobas6RhogVOm8uRQxKAFUS_CJh_6mWC3QXooq5hxRQL2lm4CSJpjHIbsKko8t7Q36fPVwgHklPwUFumaTTGgizj0e_EwR8YzxAZz04YqwAYN3FyyKAn5hLWaI8x8p_Xdrj-3Kwmh5NJx4xo6AljrS8o4hBXJBB8QYrkUA8NwpXYWel51cItKpVrTJKPKX-z3dzWq1n1I8o5919O_Uvyk-4JxIiXOngZcGKkFeXaDsGtrccC5yYY5kycnplrT0Z9EwmszAF3sANsfAcJcGp76HF5zjIwTs_09AGyhMvtR_urBkDRvFcPxetRo3h4CgQyV8jKsuqVy1E9g5q3gSe5IL4UmeTw3oO4K-IyC_gmV7M8FzoY-J0YRGEl8ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من إحياء العاشر من محرم الحرام استذكاراً لفاجعة الطف واستشهاد الإمام الحسين عليه السلام في محافظة البصرة جنوب العراق.</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/79898" target="_blank">📅 07:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=Plx-_yQyCdGMkeoxKjCR-1tcVuccail8wAcvxq3CoDe_p6SqO43atiDD9CgpGPhR1hB2CVDK1rnD2IydwIuAmVsKOVAP51RQZ0b5NRbOo_uvE66Xc__NcLyglBG5HXkc1usX7kA-BYrXmUe4kyxJxNOsxKUHwjs5UhA484BAIspOQjuCINj33MCee_nQJ4c0EqPrHLI-O_BPn7pNkGJcqbWw34tz-cIwmHY3GvjNF0fwRoGAoVEdImjjXwRqp_d4wsL5XyGKYHyhK7v--bua5S2GG5yy7FWNrCyZzi9sHZaicL8sxpBmk0wx6kvzMW4h06qlWS5TCkMW58aKP42aUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=Plx-_yQyCdGMkeoxKjCR-1tcVuccail8wAcvxq3CoDe_p6SqO43atiDD9CgpGPhR1hB2CVDK1rnD2IydwIuAmVsKOVAP51RQZ0b5NRbOo_uvE66Xc__NcLyglBG5HXkc1usX7kA-BYrXmUe4kyxJxNOsxKUHwjs5UhA484BAIspOQjuCINj33MCee_nQJ4c0EqPrHLI-O_BPn7pNkGJcqbWw34tz-cIwmHY3GvjNF0fwRoGAoVEdImjjXwRqp_d4wsL5XyGKYHyhK7v--bua5S2GG5yy7FWNrCyZzi9sHZaicL8sxpBmk0wx6kvzMW4h06qlWS5TCkMW58aKP42aUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/79897" target="_blank">📅 07:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=rh7qYnf3NIyNV2oS6EaGqULirvc2DRFUaGDZN0uyWThlHDhLGMyqJaerrCbGdRHgOn69TKjq0CLZBU82o1wEsN49cO9HeAKrb-MhBtkrMHRUsRMGDiZPrb_Ue2wE9lrkCh10QMiwDv-hwJnpS7ELy6a24_mH3El5gEaijWgLYkjIJu42dXNlI3fGtncEqGNZAbTxWZncBi2Xv2tqhtYFkH0awZYh8ICtOaXIVRgkg7GBRupJWW-XOaruJsf-9mOOJ6SNgcMtXCAMWMYxw_ZuDuho7KZnySU99QQCn_ULNjJwmq_jtFxJsnHkdk5ZCpF-JQphRQUxmZbluDezAAlbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=rh7qYnf3NIyNV2oS6EaGqULirvc2DRFUaGDZN0uyWThlHDhLGMyqJaerrCbGdRHgOn69TKjq0CLZBU82o1wEsN49cO9HeAKrb-MhBtkrMHRUsRMGDiZPrb_Ue2wE9lrkCh10QMiwDv-hwJnpS7ELy6a24_mH3El5gEaijWgLYkjIJu42dXNlI3fGtncEqGNZAbTxWZncBi2Xv2tqhtYFkH0awZYh8ICtOaXIVRgkg7GBRupJWW-XOaruJsf-9mOOJ6SNgcMtXCAMWMYxw_ZuDuho7KZnySU99QQCn_ULNjJwmq_jtFxJsnHkdk5ZCpF-JQphRQUxmZbluDezAAlbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الزوار إلى مقام الامام زين العابدين عليه السلام لإحياء يوم العاشر من محرم في سهل نينوى شمال العراق.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/79896" target="_blank">📅 06:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-text">تمزقت راية الحسين في طفّ كربلاء ولكنها لم تنكس، وتمزقت أشلاؤه ولم يركع،
وذبح اولاده واخوانه واصحابه ولم يهن
انها عزة الايمان في اعظم تجلياتها
السلام عليك يا سيدي ويا مولاي يا ابا عبدالله الحسين.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79895" target="_blank">📅 04:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
كعبة الأحرار كربلاء المقدسة حيث ينطلق معنى الحق ومذهب المقاومة ومنها تُستلهم قيم التضحية والكرامة والإباء لتبقى منارةً للأحرار في كل زمان ومكان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79894" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79893" target="_blank">📅 00:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79892" target="_blank">📅 00:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
خيارنا بالعراق هو خيار حسيني،،  المواجهة مع أعداء العراق والإسلام وشعار هيهات منا الذلة مثلته ثلة عراقية شريفة رفضت الذلة والخنوع والخضوع امام مغريات يزيد هذا العصر
السلام على فصائل المقاومة العراقية الشريفة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79891" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9-UJyXzVY5HeHsTlROalP89boAjKIdUTxy9_Kvzd0yTJQ1shiMsof6JwUn93wE1hC76sJ7C5AREUvVoAC4DpA9_Hpb1nBKoXacjwJ_0A_1ZaTJPwxuc-ea7CjYmaouy-tpI1UABUNm3ZoEH7SBtJS1qJwPx6Mnqq9ZWAJYYZf4w0D9oqNgT-MChUT5aCydtO6GG9y0gm-_r_aVony1MgCiWKnIHJIdBHp_p1ioYVk4lrXhqXOvKEbxp4j0D1-R5IHP3Di2zB7-G4mY9doXBzgX_h0JqHDRG3egVU7deIYzkTpn3KLLniwTY4f404R94PfKh5wO1o3EX5jNyM4tFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة إدارة الممر المائي للخليج الفارسي:
🔹
تقع المسؤولية الكاملة عن أي تبعات ناجمة عن الإبحار عبر المسارات غير المصرح بها على عاتق مالك السفينة ومشغّلها وقائدها.
🔹
إن أي حركة ملاحة خارج المسارات المحددة من قبل هيئة إدارة الخليج الفارسي (PGSA) لا تشملها ضمانات العبور الآمن، كما أنها لا تتمتع بأي تغطية تأمينية أو التزامات قانونية مرتبطة بذلك.
🔹
وتبقى جميع النتائج والتبعات المترتبة على استخدام المسارات غير المصرح بها مسؤولية مباشرة لمالك السفينة ومشغّلها وقائدها.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79890" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR7Icv65bF0nYoNE-2azeFhgEFTq4HRu_scjxTSFx2Piu40GH3dwZ1QkB2IWqSkoAOKV7WoL1R0UnWnvvWnsidTVdwt0ou81uYKVnOrsPLAtcDOWyTyeBbc7dpFUAYfU38P2CVQp2Iyf6MKGke8TKBJRDKJHZLJQFrVcZbLU3l49o595zMSoUJz4shQ5Ei3FRGZ24R92YIpSKhw8tJ5iQK2ghENRYdvJt6LnW5YJop9gxgqzToJ3qHHwTjST1aFwBgpyxaZ5nlPIxfdy8IOYgoxxkBmX4czyEg1A3h0KGXLcR8dNwSMtvrYm2jki5ufRfQ1LRvglthNJabnIyT3Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79889" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79888" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReAWYI448nJfvGRf_zcZObCBtvAc4exsDdfVXJb_Gek2YUNxQiQ5xK7EWcNTyQRP9GN_nw8awmxx05HPxZaMmwCUUup_uQrP7JMMKHbLcnaJh-_0W4lBazFzcO4Wm3BatiRamC8c__X84Tv4GG91BbKw8Xs-bCoxs47VVGXMMaUVIwGgDtff8KOJDidvmvho4FHJda4KYQouBEZrQxnd0w14kjboHziv7wOothE_bwI8ZtZ8UOyU8Xv7KRUAIe6vV8VljTpLa2HxP4dO3OsWkEBztgHAzl91vq3ohzeE8IDitM6QGvFYIpCHkq_MlA-GgEUGTx2Ta2o8j3-PJ-oq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
مسؤولين أمريكيين: الحرس الثوري الإيراني هاجم اليوم بمضيق هرمز سفينة شحن ترفع علم سنغافورة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79887" target="_blank">📅 22:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79886" target="_blank">📅 21:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79885" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79884" target="_blank">📅 21:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇹
🇮🇷
‏
رئيسة الوزراء الإيطالية ميلوني:
لم نشارك مطلقًا في حرب إيران ؛قدمنا دعمًا تقنيًّا ولوجستيًّا فقط.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79883" target="_blank">📅 20:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
🇮🇷
وزير الطاقة الأمريكي:
رفع العقوبات عن نفط إيران يتيح لها بيعه في أسواق أخرى وتقاضي الثمن بالدولار.
أموال إيران التي سيرفع عنها التجميد ستخضع لرقابة صارمة بشأن كيفية إنفاقها.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79882" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-06-2026
تجمعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79881" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
هبوط اضطراري لطائرة هليكوبتر الرئيس هرتسوغ في قاعدة بلمحيم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79880" target="_blank">📅 20:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭐️
‏
بيان خليجي أميركي:
إدانة هجمات الفصائل المدعومة من إيران في العراق ضد دول الخليج.
السلام بالمنطقة يتطلب التصدي لتهديدات إيران بما فيها صواريخها ومسيراتها ودعمها لوكلائها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79879" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79878" target="_blank">📅 20:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
مصدر مقرب من الفريق الإيراني المفاوض:
انسحاب الكيان الإسرائيلي من الأراضي اللبنانية المحتلة يُعد أحد شروط الاتفاق النهائي، كما يعتبره الفريق الإيراني "خطاً أحمر" مهماً.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79877" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=cg7MspjH3PuAmUOL2pkWx3Tcfk_wrmGynlfN8yD3fUK5zY0O2XVuG8RttJaYvzKDXYfXu6wBHZ9lSfKfCotEVlpkj3eH1g-TcaC--dJgwx40dMd373Arf38Y4JWJLLbJAnR3IUA_8ccn1NbLusohTnxkVEGHhWekUJpeK9jxG4-fC7snP014HNCNe6BVNPwcXM3Rrk6jWyASfMP4h5JALpb5_qOyRxZS053poJ2XyYiCJww6bk5tAZzEDEl-CCzoxW5jF9YIs6cYOUFXtUK75JSTfm9Mu0RAk8EfrjCOckYt_LkIYoEZ7v3xjgCvDQV8brGtqGRzCzZRj7-KGiI_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=cg7MspjH3PuAmUOL2pkWx3Tcfk_wrmGynlfN8yD3fUK5zY0O2XVuG8RttJaYvzKDXYfXu6wBHZ9lSfKfCotEVlpkj3eH1g-TcaC--dJgwx40dMd373Arf38Y4JWJLLbJAnR3IUA_8ccn1NbLusohTnxkVEGHhWekUJpeK9jxG4-fC7snP014HNCNe6BVNPwcXM3Rrk6jWyASfMP4h5JALpb5_qOyRxZS053poJ2XyYiCJww6bk5tAZzEDEl-CCzoxW5jF9YIs6cYOUFXtUK75JSTfm9Mu0RAk8EfrjCOckYt_LkIYoEZ7v3xjgCvDQV8brGtqGRzCzZRj7-KGiI_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مواكب المقاومة العراقية البطلة تجوب شوارع ميسان.. إنهم رجال الفارس الكربلائي أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79876" target="_blank">📅 19:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
🌟
قوات الأمن السعودية تختطف مواطن عراقي من محافظة البصرة أثناء أداء "مناسك العمرة" وتقتاده إلى مكان مجهول عقب نشره صورة "لقبور أئمة البقيع المهدمة" على إحدى برامج التواصل الإجتماعي!!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79875" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAtsP6ilQZbSDzX6paEWwWh1chu5eqUcR59Fu03vWKX4lZg5yKb8g0UNJyNiN0zkn4lxTCuSYGzZQcC1Mha3vvsj45uMRX85SP6RL8zLfpqO66IZkiRq9EAfpiKv7-ESmW01OGkvZU5vk93u0rkrDlYOKk0cix_r3XwyOhk01Ivvwqn7Z6uWLbX307GIvE-Xuhg5vjAJH1YeF2xEv0tRPg4xFz_9iXtxs32UR3d6qBLB7HncN3JnNoUZ3p_v8y5xsoOeFPdCScEJZNDb7g4wpMJ8AA2k5DL7_GbpyP4yRw4hUXUERjtXbtPP0o3vKnkXDOo9gU1tqS1F7jF-FB2o5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأمين العام للمقاومة الإسلامية حركة النجباء "الشيخ أكرم الكعبي":
سيف يزيد المعاصر سينكسر أمام القبضات الحسينية، وراية الحق ستبقى ترفرف فوق قمم الانتصار.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79874" target="_blank">📅 19:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79873" target="_blank">📅 19:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭐️
المعارضة الكردية الإيرانية الإرهابية، ماتسمى"وحدات كردستان الشرقية" تزعم تعرض مقراتها بالقرب من الحدود العراقية الإيرانية إلى هجمات بطائرات مسيرة صباح اليوم.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79872" target="_blank">📅 19:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=l5rEXFeZdF25Yd_tO8kYbMP0VQ4jFg9-sJib3dO42fuR62DOZNu5X59yR-zJi2VBZKJ8qw5PKKpFPC2vz4q_YZOhcX326JxmPGPKx1XoPr6jTJkP_50A9eJXIIXFvrwiBMw703jcbdOiBu0_AHzt1Gmr-Mfxmcyh0F-nIU6GS8zCimX0SiqSsc_pY8Ij79N3Abb0WKFYlHp4MIlGYuQWn0bxJAwtc3SNUmPQvwkITguX7f75041vY8cvxAInfFO9jNY-oXu00ElmnRdCQClFj2cI11GJGUjkinOq5M9kOc-YiFmdeCXCslQRGPHVNWwk25AwpByPWAhgbo0aNauQNFnDn3V0SFqtZcb9T2xk65iWJM1EmtD0mAVEB2gvMf_2lS3JtGlka9ps6VDEPMKUq2mwMrN8zfKRszqwlbKwFadq6CTnrcH8iHNehZJrNfJWuRcphTCE1DPd-yM4-WvshDt41P-eV0s25Z3xK7rJRC88kY11O1kilGbrbMU9CsjGGPbBzr3hhPL2fL6I1_RNOd5RHElyZYdfy5ioFkFbaJyp9bpBt6njOxC1J0-2H5rhAK1YQ9tZ3ZrXE2Ic5t_B1dLlW1dm-e2hHmjqyHr4A0crp2oESo-188hcAMp2i20j7q_1EVtFUx4UkqbESJEDyP0tkYr60Gwz4TPM_bqsNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=l5rEXFeZdF25Yd_tO8kYbMP0VQ4jFg9-sJib3dO42fuR62DOZNu5X59yR-zJi2VBZKJ8qw5PKKpFPC2vz4q_YZOhcX326JxmPGPKx1XoPr6jTJkP_50A9eJXIIXFvrwiBMw703jcbdOiBu0_AHzt1Gmr-Mfxmcyh0F-nIU6GS8zCimX0SiqSsc_pY8Ij79N3Abb0WKFYlHp4MIlGYuQWn0bxJAwtc3SNUmPQvwkITguX7f75041vY8cvxAInfFO9jNY-oXu00ElmnRdCQClFj2cI11GJGUjkinOq5M9kOc-YiFmdeCXCslQRGPHVNWwk25AwpByPWAhgbo0aNauQNFnDn3V0SFqtZcb9T2xk65iWJM1EmtD0mAVEB2gvMf_2lS3JtGlka9ps6VDEPMKUq2mwMrN8zfKRszqwlbKwFadq6CTnrcH8iHNehZJrNfJWuRcphTCE1DPd-yM4-WvshDt41P-eV0s25Z3xK7rJRC88kY11O1kilGbrbMU9CsjGGPbBzr3hhPL2fL6I1_RNOd5RHElyZYdfy5ioFkFbaJyp9bpBt6njOxC1J0-2H5rhAK1YQ9tZ3ZrXE2Ic5t_B1dLlW1dm-e2hHmjqyHr4A0crp2oESo-188hcAMp2i20j7q_1EVtFUx4UkqbESJEDyP0tkYr60Gwz4TPM_bqsNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
لن ننسحب من لبنان ‏وأمرنا الجيش بالقيام بكل ما يلزم لحماية سكان الشمال.
نحن في ذروة حرب إقليمية متواصلة لا تقل عن حرب الاستقلال.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79871" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭐️
حادث وقع على بعد 7.5 ميل بحري جنوب شرق داهيت، عمان. أصيبت سفينة شحن على جانبها الأيمن بمقذوف مجهول، مما تسبب في أضرار لجسر القيادة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79870" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
​
ضغوطات لحركة طالبان ضد أكبر مدرسة دينية شيعية وقناة التمدن الفضائية في العاصمة الأفغانية كابل..
وفقاً للتقارير الواردة من العاصمة الأفغانية، تواجه "حوزة خاتم النبيين (ص) العلمية" و"شبكة التمدن التلفزيونية" ضغوطاً ومساعي من قبل حركة طالبان للسيطرة عليهما أو تعليق أنشطتهما، واللتين تُعدّان من أبرز الميراثين العلمي والثقافي  آية الله الشيخ محمد آصف محسني (رحمه الله).
​نبذة عن المؤسسات المستهدفة
​مدرسة خاتم النبيين (ص) العلمية: يُعرف هذا المركز بأنه أكبر مدرسة للعلوم الدينية الشيعية وأكثرها تجهيزاً في أفغانستان. ولم يقتصر دورها على تعليم طلاب العلوم الدينية فحسب، بل لعبت دوراً محورياً في التقريب بين المذاهب الإسلامية والحفاظ على الانسجام والتماسك الاجتماعي في البلاد.
​شبكة التمدن التلفزيونية: تأسست هذه الوسيلة الإعلامية المرئية بهدف نشر معارف أهل البيت (عليهم السلام)، وترويج الأخلاق الإسلامية، ورفع الوعي الديني والثقافي. وقد نشطت لسنوات طويلة كواحدة من وسائل الإعلام الرصينة والمستقلة في أفغانستان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79869" target="_blank">📅 18:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحين تابعين لعصابات الجولاني الإرهابية، ترفض عودة الأكراد إلى مدينة رأس العين ضمن محافظة الحسكة السورية وتتوعد من يعود إلى المدينة بالقتل.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79868" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79867" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79866" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
تسعى إيران إلى كسب مليارات من الدولارات عن طريق فرض رسوم على السفن لخدمات الأمن والسلامة والبيئة في مضيق هرمز بعد الحرب.
تقول طهران إن الخطة يمكن أن تدر ما يصل إلى 40 مليار دولار أمريكي سنويًا، وتريد من الدول الخليجية المجاورة أن تشارك في الإيرادات.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79865" target="_blank">📅 18:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQo20yPgUw0NvLg2u6AseV14lHMwcv-HnzOs123KXveFQYPrdX4GZcWZeF2B8xT4E3Za_FB3I4SoKEJ1LqOS7u6jmDgxopENsy0P8Chy2_PMeV9jERl28x3dbIlHM5CrjwAkhmAK7V5i_FUlFsN6fDVqp7SMwyxUvk2bJrdLEEQ_M5i1lGBLxKebw9MQKbn3iccZw8so3rVpaoFR6Cg3dWLtZcJUlL2xfKyhDRRJicx2baQCNRsUUQOuJzXuUNJrC52gS19VOVaeLp8rP5tu7T3_hoHDVUkwHwI_39DI4GRnxcJZfq-YDT5mBVgreRHy6bb91hYz8JQhw-cLezjGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUkkImm8Jkfk375WL7REgRV0pEH9cAfY4d8oxy9vXfnhcPxsQlAFtIHPbdKCo-9i9EyhXZ3w9SlTeXxgXDVfYofGi6TrRhdprDg3uWrvCwoEwMHvIKzwpZCV_-IIRURCj6ewJBMFxmmceOr0CyG0NoRrZYjCpeYqOYPxqwvFAtFjIlN_D7gC5KcvDvLJtENgnxCdqjkIUsgWErAlSW2OpGmoR9iEC8SQ_l5kJHqkfJZH6xMCHTNJxG-YjRkCM3lAycQ4mVthEsNPcQfoZpRzD5gUvkbO7770m6WEYje6s-nAmmXRne4p427SlcVWCmATNH_-t-X_F76Yo-_bREj-1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء "عبدالقادر الكربلائي":
إننا بعون الله لن نحيد عن درب المقاومة، ولن ننساق وراء تخرصات الأعداء وأوهامهم، فسلاحنا سيبقى مرفوعاً بوجههم وراياتنا خفاقة ما دام فينا عرق ينبض وسنبقى مقاومين حسينيين لن نتراجع أو نساوم إن شاء الله.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79863" target="_blank">📅 18:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79862" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79861" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79860" target="_blank">📅 17:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
نرصد بكل اهتمام مجريات الوضع في أرض الصومال وما يقوم به العدو الإسرائيلي بهدف السيطرة على خليج عدن وباب المندب والتحكم في البحر الأحمر، نحث الدول المطلة على البحر الأحمر لموقف مشترك إزاء نشاط العدو الإسرائيلي، ولن نقف مكتوفي الأيدي أمام أي تمركز في الصومال وسنبادر في أي وقت لاستهداف أي نشاط للعدو الإسرائيلي في أرض الصومال.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79859" target="_blank">📅 17:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقتل ضابط بجهاز المخابرات العراقي برتبة مقدم في العاصمة بغداد بعد اندلاع اشتباكات مسلحة في منطقة المعالف</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79858" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
✊
العراق يعلن تسجيل تحفظه على بعض فقرات “إعلان باكو” الصادر عن الدورة العشرين لمؤتمر اتحاد مجالس الدول الأعضاء في منظمة التعاون الإسلامي المنعقد في العاصمة الأذربيجانية باكو
العراق يؤكد تمسكه بمواقفه الثابتة والداعمة للقضية الفلسطينية وحقوق الشعب الفلسطيني المشروعة، معرباً عن تحفظه على الإشارة إلى “حل الدولتين” بصيغته الواردة في الإعلان، انسجاماً مع التشريعات والقرارات الصادرة عن مجلس النواب العراقي الداعمة لإقامة الدولة الفلسطينية وعاصمتها القدس الشريف، وضمان حق العودة والتعويض للشعب الفلسطيني.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79857" target="_blank">📅 16:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
السلطة القضائية الايرانية:
أن الادعاء بـ"حظر ترديد الشعارات المناهضة للنظام الأمريكي وحرق علم الحكومة الأمريكية الإرهابية في التجمعات" ادعاءٌ باطلٌ لا أساس له من الصحة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79856" target="_blank">📅 16:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇷🇺
‏وزارة الخارجية الروسية تستدعي سفير رومانيا وتعلن القنصل العام لرومانيا في سانت بطرسبرغ شخصًا غير مرغوب فيه وتعلن اغلاق المكتب القنصلي الروماني هناك ردًا على إلغاء بوخارست موافقتها على القنصلية العامة الروسية في كونستانتا وإعلان مديرها شخصًا غير مرغوب فيه.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79855" target="_blank">📅 16:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDuIm4lBl14uBYCiM0bg4NtUQRyJsJctjff4qRvhpWJv238_WRv7sEH5hapQPyC91BHhE57gIH5WiosWsfcshjrgFA3s_lF43qJD_mUdh8m9bNLxBjl6QPXhwuqiZuokOBSBWL3cxHmHmUYww6pyfGK8aOeFOK1aIBV6pP-hONQAy0P3SgGX1Jh_v_zmyW9IGer0Udd3LXGzBT2rhY_W-OzmhmbkIL2VdWS4pz-7KPXCwmb9_3gKuhuAoq-c72c3HS3mj9eSgW74uPfkDXn0KmNLkhSDaX6JXW5_UtQywwxDQQAB5sHBGIwZNpwx5Ke-VPqmgT61nlPk2pvOBZw9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
‏
تزعم أمريكا زوراً أن أصولنا المجمدة ستشتري منتجاتها الزراعية. أمرٌ مثيرٌ للاهتمام. المحصول الوحيد الذي نحصده هو ما زرعتموه أنتم: عقودٌ من انعدام الثقة. إنه عضوي، وفير، ومحلي الصنع. لكن يبدو أن الولايات المتحدة لا تصدّر سوى فول الصويا المعدل وراثياً، والوعود الكاذبة، والتصريحات الجوفاء.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79854" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCz_ig3AVy9NN48qbV6MnMru7XUWdycU_wrLtaAv2t3bZkhgwlq9LO-N7vbitHa9Tm5EAlWAnLE1Id9vgdNtKKYT_8Rz1fDj5UnArB4Wls_Q27xKFc-WRc2BNUV4sZll8bIs6NEW9UGfSee3sV5P21XmYoWeE-NDw-y2Kj6z9HRDDP-BE7TvfxRWpNsg4pK0ZiGbYOVjsnNPiRjrGr-DuMmBnmk43MaC-_-xxY6Lv2Td_7iuVZPOabTHgflPJ8VA9lL9nfUO7_w7fp49MBlDgvunx5O09-lPqKPTh3mo3DvTBkPBixK-fFzC-P_8GlLn1vRpI8P5wmYjjNdCdxywZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yjloqo8DoydSwP1vEtX8IZELKpp7Ml42VjlIYbfNaZJWNQZgP9l7oHh6Uj7rh6oVBxLznMuU6JkOaYzTO56PJWo45yocw8eVztShmaTq67hugLDv6ICITTDOrSgFTOKNbc4DthxdSgU1z4WzBpkOf1pA2eaAW5QcGYhaUKTdRjARSPXfvgNxYgyJm0hnSBdju4UbgKRoPyu0oFXvONXR_nJ59q8zoBSKA24gpgodA320141KKkPhrpnQNhCtdkxTeBGYA8w_q3uSS_60iKLHxs6nWkK1dl_Bzz0uprYl0MVCDkNjv7pqr0wAQpmlg4r6_oxQ4mAUGgm-ukkl8XsDVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
❤️
القيادات الايرانية تشارك في احياء يوم عاشوراء.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79852" target="_blank">📅 15:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏ زلزال بقوة 5.5 درجة يضرب تشيلي</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79851" target="_blank">📅 15:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏روبيو: دول الناتو لم تسمح لنا باستخدام قواعدنا العسكرية رغم أن إيران تشكّل تهديداً أكبر لهم</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79850" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روبيو: إذا استخدمت إيران الأموال لتمويل وكلاء لها، فإن الاتفاق لن ينجح.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79849" target="_blank">📅 15:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روبيو: نحن قريبون من التوصل إلى اتفاق مبدئي بين إسرائيل ولبنان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79848" target="_blank">📅 15:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏روبيو: سنشارك دول الخليج على خطوات تطبيق مذكرة التفاهم مع إيران  تحديدا فقرة دفع الـ300 مليار دولار
😄</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79847" target="_blank">📅 15:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
‏روبيو: لن يكون هناك سلام واستقرار في المنطقة مع وكلاء إيران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79846" target="_blank">📅 15:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">السلطات المصرية تغلق مسجد الامام الحسين (عليه السلام) في القاهرة لمدة 3 ايام بحجة "اجراء صيانة"!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79845" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
‏
بيان صادر عن البحرية التابعة للحرس الثوري الإيراني:
لا يُسمح بالمرور في مضيق هرمز إلا عبر المسارات التي أعلنها مراسل إيران دراغون المتمركز في المياه الشمالية لمضيق هرمز. وقد أعلنت البحرية التابعة للحرس الثوري الإيراني حظر مرور السفن خارج هذه المسارات، واصفةً إياه بالخطير للغاية، وطلبت من جميع السفن الالتزام التام بالمسارات المعلنة. ويُشترط التنسيق مع البحرية التابعة للحرس الثوري الإيراني لعبور مضيق هرمز عبر القناة 16، وسيتم اتخاذ الإجراءات اللازمة بحق المخالفين. والرسالة العامة لهذا البيان هي أن الملاحة في مضيق هرمز لن تكون آمنة إلا في ظل الأوامر الإيرانية</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79844" target="_blank">📅 14:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو: لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79843" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو:
لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79842" target="_blank">📅 14:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
قائد قوة القدس في حرس الثورة الإسلامية اللواء اسماعيل قاأني للصهاينة:
عليكم مغادرة لبنان بأكمله؛ لأن هذه الأرض ساحة مقاومة ونضال، وليست ملعبًا للمحتلين. إن لم تتراجعوا اليوم بإرادتكم الحرة، فستُجبرون غدًا على الفرار مُذلّين مهزومين. لا تنسوا عام 2000 والإرادة التاريخية للشهيد السيد الحسن نصر الله في بنت جبيل؛ ذلك الوعد لا يزال قائمًا، ولا شك أن المشهد نفسه سيتكرر.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79841" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس: كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79840" target="_blank">📅 14:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس:
كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79839" target="_blank">📅 14:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
مقتل ثلاث اشخاص واصابة اخرين كحصيلة اولية في اشتباكات مسلحة بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79838" target="_blank">📅 14:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
تتويج العراق في لقب بطولة العالم للمواي تاي في ماليزيا بعد فوز اللاعب العراقي مصطفى التكريتي على نظيره الروسي في النهائي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79837" target="_blank">📅 13:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
إن ما أُثير بشأن تلويح العراق بانهاء عضويته بمنظمة أوبك لا يعكس الموقف الرسمي للحكومة العراقية، إذ لم يطرح رئيس مجلس الوزراء أو الحكومة العراقية مسألة الانسحاب، بل أكد العراق باستمرار أهمية إعادة تقييم السقوف الإنتاجية بما يتوافق مع الطاقات الإنتاجية المستدامة للدول الأعضاء وفقا للاتفاق الذي أقرته كافة الدول المعنية والتفاهمات الخاصة بوضع العراق الأمني والاقتصادي.
وفي هذا السياق، استجابت دول منظمة أوبك والدول المؤتلفة معها لهذا التوجه من خلال إطلاق عملية إعادة تقييم الطاقة الإنتاجية القصوى المستدامة للدول الأعضاء، والتي تُنفَّذ حالياً بالتنسيق مع شركة استشارية دولية مستقلة، وبمشاركة فاعلة من العراق، وفقاً للجدول الزمني المعتمد.
كما باشرت دول منظمة أوبك والدول المؤتلفة معها بالفعل بإعادة الكميات المخفضة تدريجياً، ومن المقرر استكمال عودة جميع التخفيضات الطوعية خلال الأشهر القليلة المقبلة، بما يسهم في تعزيز السقف الإنتاجي للعراق. وعليه، فإن أي مطالب تتعلق بالسقوف الإنتاجية أو مستويات الطاقة الإنتاجية تُعالج من خلال الآليات الفنية والتوافقية المعتمدة ضمن إطار دول منظمة أوبك والدول المؤتلفة معها.
كما نود الإشارة هنا إلى وجود تفهم عالي المستوى من الدول الأعضاء في المنظمة لوضع العراق الخاص وما عانته الصناعة النفطية العراقية خلال اكثر من أربعين عام مضى من الحروب والحصار والتحديات وآخرها ما حصل من تدمير للعديد من جزئيات بنيته التحتية النفطية والساندة من خلال الهجمات الارهابية التخريبية وان هذا سيؤخذ بنظر الاهتمام ليكون الانتاج النفطي العراقي بالمستوى العادل الذي يمكنه من استعادة موقعه كثاني اكبر منتج ضمن دول المنظمة ويحقق النتائج المرجوة من مشاريع التطوير والتأهيل لكافة مفاصل الصناعة النفطية التي تشكل العصب الرئيسي للعائدات المالية العراقية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79836" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gck91H-n_rlJhlwe51nfVoYoakXAhzfhA1hVmzRww5fi0jgZmXlrRcD93L3-6bHsLJ52mMOnyDbzCWKLiEF9ALo8zjusea-7sxT08Bx7fjgtnDZgAiv_DHDh7bCwgHUMhusml-HMokCZkUPaIP--i0rkqkjY9Vl8H8BEkcjRMWI0_5ULUzM5qSPk-2CsDx3Onr8Y-CTOHj47RjrB2JXny9b3vqmvOpHT8Yv1oAVtL-0vwyHi_AQiO2x-7PaXotOYgsXQ29MFlETXl3JtGx1-s0CV2qcrSNH2IBqcQZev3fL0L8sLLYT0HpqDaJVjHGuFPa46Cz7rZKme3j17fbUOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
قوات حرس الحدود العراقية تحبط محاولة تهريب 34 كغم من المخدرات بواسطة بالون هوائي على الحدود العراقية الاردنية السورية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79835" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
🔵
فرنسا تتدعي انها اعترضت ناقلة نفط خامسة تابعة لأسطول الظل الروسي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79834" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79832" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79831" target="_blank">📅 12:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
📰
رويترز عن مسؤول كبير بقطاع النفط: العراق يمر بأزمة مالية حادة ناجمة عن الانخفاض الكبير في صادرات النفط بسبب حرب إيران ويجب النظر في زيادة حصته في أوبك بمنتهى الجدية
🔻
العراق ناقش داخلياً احتمال خروجه من منظمة أوبك، لكنه يعتزم البقاء في المجموعة والضغط من أجل الحصول على حصة إنتاج أكبر.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79830" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJXasLcaYpkXffnwDqMtmxgTWW8Ignm7a7cSKj0tsAJWRr2l6V9boZpFdR4k03ouHV7hYoWRHTLTQsNEjPrWKOUmmwAJh8Vz1-i3xvaREDna9F1GQxctld_P816EmLApgpuMZLeoOAD6_HzWlggYfLGsp0KJ6Rr_OZ1G2fUs_67EL5KoPVYMFARNU9NdZXTmYWQMpSlI4oQpQim3Xks2xBlK36guymyttjG66i_0XPOv_ult8jpG7LfPTrSL6CDE-BesOdmtlk6cgW3wHCyo5B8nxY7gdoUd507Zpvs_DyNvfqZ4ZT4XiyjLcLB1tNXzMTjgsiJxV1aRdWiTtjOr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أفلس العراق رسميا ؟!
مجلس الوزراء العراقي يقرر إيقاف التعاقدات للمشروعات الجديدة الاستثمارية وما يخص العقود السابقة يبلغ الشركات " اصبروا ان الله مع الصابرين " يبدو انها آثار عواقب الحرب بين امريكا وايران على المنطقة ..</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79829" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=OPtzjcjN6RLWllB7J6RdJYwtpiSqvf5kijTPp_41tGiiqmpp4ZSqgq6Z2CQY1py1_8Nx04P13sha_4WzB6UuUVYwHHUvR1AjVnQETrrOQV0KQCHE3nkP6en6b1LF2zz6y3kgkvURgP65zZJONu1OEOcolAcgtDa2gHNDqmnMbMWszpG-ARM3EYAZRAjSBIdApnmVyQ4Mc4Bmrnz4jsT2qkVT8wKwW8YIZ3V2vU9aKz0-5l7pueOABcCh0YJzOsBKqYXHrKbTQfKRWWAaTZKfXKKC56arVJo6NGUUjc8JgA8F294D61JWTPHWZ8vXpOsDDkMuuGbkjdA7sIBfepX24A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=OPtzjcjN6RLWllB7J6RdJYwtpiSqvf5kijTPp_41tGiiqmpp4ZSqgq6Z2CQY1py1_8Nx04P13sha_4WzB6UuUVYwHHUvR1AjVnQETrrOQV0KQCHE3nkP6en6b1LF2zz6y3kgkvURgP65zZJONu1OEOcolAcgtDa2gHNDqmnMbMWszpG-ARM3EYAZRAjSBIdApnmVyQ4Mc4Bmrnz4jsT2qkVT8wKwW8YIZ3V2vU9aKz0-5l7pueOABcCh0YJzOsBKqYXHrKbTQfKRWWAaTZKfXKKC56arVJo6NGUUjc8JgA8F294D61JWTPHWZ8vXpOsDDkMuuGbkjdA7sIBfepX24A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تاكر كارلسون: كان ترامب مقتنعًا بأن قتل آية الله سيؤدي بطريقة ما إلى انهيار إيران. لكنه وقع في فخ الحرب مع إيران بعد وفاة آية الله علي خامنئي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79828" target="_blank">📅 09:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=jW__83Gs1xpqde0tvN7RSd8ifrv8zyVpvBkhYLbmFDzoM7X3Jegz5wyZifA93yNoHbh01RFKfoTp2HqzNkTgeBDpsikeA0j8CvhF46kQfjJJNOQFNj5wD5Vun89PHwhzU_2HApGlF_nzsVjnA2dJ4x5yJdH-FW8gNSC1a0iZH5T6-z-pG5Wa8CtOetAtptpRs3MQRz8MpALGXRgFpKMnaXMP2XRL19MRd-tt9DHnkJO9g8GI1MdSnIuibsArjNTkVaTd0AzKhcKkDYD4YQF0xb9NnK4Jolc2sDphWjUuV4ZXhmCAhDTLHgYA0miFtNsjkF-yAE7bk-sinhmRjK_DLZXo2pOlyqKNnp9zh7ci8sAjmmM8MFIIoBlHybHYQMo-gcvFTrRu2F9VBAF5K1aa6gwNVGJnd2ew1gQyxXeqYaukiG1Rk9mTFF0dTuS7xJrJefCs7WDqeEpmG7XdaI8DCHsp9mfa-r0Hss5qWqdPln9vAdwOGfs0N26Y4xZa24CDp1iubkpggDBlY-9duaZNzkOIJdlr6nPy5t_T2p9znLVw192fhPmo68TmyMbi6bXUzz7Dd-gfN-z-r-2XS9BrJQsG63iV06eTSIGVEoeOOcNy_KwLw1rOke1hJtYntYulOgqxvWXZo6JwYoco4bx1oujEk8H71c5wVSXyuF9EwY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=jW__83Gs1xpqde0tvN7RSd8ifrv8zyVpvBkhYLbmFDzoM7X3Jegz5wyZifA93yNoHbh01RFKfoTp2HqzNkTgeBDpsikeA0j8CvhF46kQfjJJNOQFNj5wD5Vun89PHwhzU_2HApGlF_nzsVjnA2dJ4x5yJdH-FW8gNSC1a0iZH5T6-z-pG5Wa8CtOetAtptpRs3MQRz8MpALGXRgFpKMnaXMP2XRL19MRd-tt9DHnkJO9g8GI1MdSnIuibsArjNTkVaTd0AzKhcKkDYD4YQF0xb9NnK4Jolc2sDphWjUuV4ZXhmCAhDTLHgYA0miFtNsjkF-yAE7bk-sinhmRjK_DLZXo2pOlyqKNnp9zh7ci8sAjmmM8MFIIoBlHybHYQMo-gcvFTrRu2F9VBAF5K1aa6gwNVGJnd2ew1gQyxXeqYaukiG1Rk9mTFF0dTuS7xJrJefCs7WDqeEpmG7XdaI8DCHsp9mfa-r0Hss5qWqdPln9vAdwOGfs0N26Y4xZa24CDp1iubkpggDBlY-9duaZNzkOIJdlr6nPy5t_T2p9znLVw192fhPmo68TmyMbi6bXUzz7Dd-gfN-z-r-2XS9BrJQsG63iV06eTSIGVEoeOOcNy_KwLw1rOke1hJtYntYulOgqxvWXZo6JwYoco4bx1oujEk8H71c5wVSXyuF9EwY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79827" target="_blank">📅 09:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039cf77145.mp4?token=XRnqUMky9Ic21JVEq5MOpuHSwDgrOsetrYpWNX9dLAbn1uuXvvmz7nlsqD2S_7u68YRi7N5EZacbRdnMq-XkpgZTsgAMsyWlNwLULtzuOz-VPwhWhbgifcYaWLeZSqAdG_XgP73Uck_oikTODbt1Ek94TvYGe7kAAxEBs__bcc7QLaY_gSM2_7NCMvYbphT4Lw_UoEGX_FR7svtnd3egjH9se2fRovlSJX_wavNZn3r8MVwLZpyualjRN2PJqtGU320GeYFXn5DZI3GAJDhih6KPbqJy4Feewfqkfm3RXbuKb3T0JWtD14vrlUgVkC81MahbYYwBe_D0bHFK2sujWxFiBKmiuacAE6TLGGRxThOtR-I4J7-a9-On0If6J0eQ531HxRWK6vyfUuJo7Tv9HfMCgbYn-S4aMxLsho7-4MevXZYfhSC6xZ0qwfueGvyI-n6JGHRFVYbZ4Vc97iVEWvzg1kHl5V1sks-cYwRpn40CJ2agWDD-L5aRess_1LXuEcItUXFprZg-qS0EV0_GkqUGRI36dyd4wbWtQJTNzydIvj76Nf7HvxSG6Wszi4lY856FxdJxovZJsTAUb-g7uvH4YXIPZY1qL0dufqaUg8hHSOXDw_wRr6drV1j0WTHk-x63ZN4Ywky2oBZuDaWBaKG95SLcQWzAFKJ3OJGBQ-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039cf77145.mp4?token=XRnqUMky9Ic21JVEq5MOpuHSwDgrOsetrYpWNX9dLAbn1uuXvvmz7nlsqD2S_7u68YRi7N5EZacbRdnMq-XkpgZTsgAMsyWlNwLULtzuOz-VPwhWhbgifcYaWLeZSqAdG_XgP73Uck_oikTODbt1Ek94TvYGe7kAAxEBs__bcc7QLaY_gSM2_7NCMvYbphT4Lw_UoEGX_FR7svtnd3egjH9se2fRovlSJX_wavNZn3r8MVwLZpyualjRN2PJqtGU320GeYFXn5DZI3GAJDhih6KPbqJy4Feewfqkfm3RXbuKb3T0JWtD14vrlUgVkC81MahbYYwBe_D0bHFK2sujWxFiBKmiuacAE6TLGGRxThOtR-I4J7-a9-On0If6J0eQ531HxRWK6vyfUuJo7Tv9HfMCgbYn-S4aMxLsho7-4MevXZYfhSC6xZ0qwfueGvyI-n6JGHRFVYbZ4Vc97iVEWvzg1kHl5V1sks-cYwRpn40CJ2agWDD-L5aRess_1LXuEcItUXFprZg-qS0EV0_GkqUGRI36dyd4wbWtQJTNzydIvj76Nf7HvxSG6Wszi4lY856FxdJxovZJsTAUb-g7uvH4YXIPZY1qL0dufqaUg8hHSOXDw_wRr6drV1j0WTHk-x63ZN4Ywky2oBZuDaWBaKG95SLcQWzAFKJ3OJGBQ-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79826" target="_blank">📅 09:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 تضرب خراسان شمال شرق إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79825" target="_blank">📅 09:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwy5LElst9cUKxDkhg_2g2hit-P3PjXgDG_qP82Q0ftEq3gs08ON-PuU0OuL1mEYFSlHEJQnTcYIE83M-E-eo56s7341qph7naH5NmUhqb3whEfUXhAVPy0Tm8EIPdzwW119_lFNcqDFVMQTMvajs5uNGrXIgXHKkFHwhlLD8dwnM_l2xkaabEOkTVcHK3SqFB8nSb7zmEYYoUdsCE-v52G6rz_jPb9_icUiMi5EuoElux375dOCdOUe-IF2OpF_obVRXamulReRTnv8X2Q8kicgqoJCOh5uUuULyWybE-v5NOjIxqOADnQqOXuU4lanyzuQBdxC_LWtJ73cqPVKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الزلزالان الكبيران اللذان ضربا فنزويلا مؤخراً كانا هائلين، وقد خلّفا عدداً هائلاً من الضحايا. الولايات المتحدة الأمريكية على أهبة الاستعداد لتقديم المساعدة!
‏لقد أصدرتُ تعليماتي لجميع أجهزة حكومتنا بالاستعداد للتحرك بسرعة. سنكون حاضرين لدعم أصدقائنا الجدد والرائعين. التقارير الأولية ليست مبشرة!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79824" target="_blank">📅 08:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n70C5HLbq8Qes5Bwo0yhd8BTsIVD5rgA_19KBFdPwKYFc69FTw_rH0vYZPiNyMdbsq2ejDCJzNY6tc_VFj2CP_3PM3HtsqVMRRerJxCdLrA0RqMdrSidYneFsTblAcWwluYjBMSvOfTwOGvDM9ITt3QmjK2JYPUynL7RUCRSga8iRN_3oM-itfsfZ53f2lMFHW2a8XGwiaJ7LcZvX6QAkTROamV-9ryIsZnpZo6ZuVoKZxJrQVnX6kh3-UWkSGBPNdqlgvCnrsycLYM5zQeI-usMrNgAWZLQk9smn1mwjInAZ8s_2fLHFtS7YQX9mU_RFEwQZT0Qbhqhy49JGgfBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي للصحافة العالمية :
سيتم تخصيص 500 ألف برميل يومياً من النفط العراقي لتجديد الاحتياطي النفطي الاستراتيجي الأمريكي ؛ سيدرس العراق "تعليق" عضويته في منظمة أوبك إذا مُنع من الإنتاج بما يتناسب مع قدراته
‏سيتم "خنق" الفساد
‏سيتم نزع سلاح الميليشيات بحلول 30 سبتمبر مع مغادرة آخر القوات الأمريكية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/79823" target="_blank">📅 01:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران. ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/79822" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
