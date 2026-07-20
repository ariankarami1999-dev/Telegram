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
<img src="https://cdn4.telesco.pe/file/hHN-KtnS6JNJw2NUUrZ-gGJkC4e1i0Lmz9pRJ2gFWdOLek1_ZHF0fb2dBgzcs0tbm0pynx0KA8eua1W_7LmRQFSN1NIHwWzCqkdaCh2f16ryn-3BoNfbuS9gxK6B74zY9-yPDjTh4YWARBm0VqE8bkGiJvLjO3mPmz0a4Cg63Ys8gA-FdZP5KHi01Uk2q08J4kR4gOSKa7OTB4TZ9Eq3ZyQUNK-3OZpsOs9BfZDtx1Wk-70hU9pQoYVRvuoZdTcWYmoW7z9_HAJulV49y0HiRzzSjv36EDf84S2fQP8NG_xF0u3pUraZwG4k96RpLGjz3lC9ReFI2HhbmioUCc_WXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12176828e.mp4?token=JrNK8FRbCma14dNE7bvzL1DTZLgMwJI6SJpz1EWS7Kdn8MnlnbzkfQGCx4DQ_UNxMqFJRhdxpOdRER5Y4rH-t8qzA23FwzdNST5t2Q75T1iaMeqbj1o1hT4Q7Gzg__PCuPLDZTdDfp-SHbD8WTorRrVMfhwrL3binkSKGsnA2-V9VLjvleNCteBgyGhw-K14Tf4C1kxA1GV9tEFYfirr7ghN87gh-T3YnZJ9UE2FvCeQj9Rk-4Ev6BAq4AriN9ibf5OzHIn6ckr5M_pzkbBiL-2tITY7dv2CAUabcmj5GNeakppIo2q1l5gkSF62ufuRruRMtg-WaQY6_6MBsnUiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12176828e.mp4?token=JrNK8FRbCma14dNE7bvzL1DTZLgMwJI6SJpz1EWS7Kdn8MnlnbzkfQGCx4DQ_UNxMqFJRhdxpOdRER5Y4rH-t8qzA23FwzdNST5t2Q75T1iaMeqbj1o1hT4Q7Gzg__PCuPLDZTdDfp-SHbD8WTorRrVMfhwrL3binkSKGsnA2-V9VLjvleNCteBgyGhw-K14Tf4C1kxA1GV9tEFYfirr7ghN87gh-T3YnZJ9UE2FvCeQj9Rk-4Ev6BAq4AriN9ibf5OzHIn6ckr5M_pzkbBiL-2tITY7dv2CAUabcmj5GNeakppIo2q1l5gkSF62ufuRruRMtg-WaQY6_6MBsnUiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة العدوان الأمريكي الغاشم على ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/84535" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/84534" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/84533" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a66581210.mp4?token=OT1VBFbumrYqj30mcFdfvlRu69Hwyk1YhOHhqs8MqsaMJySsS6mJtA0xbGwCXAXX1VmmA3DgWIylybjQuvQB6xQZVj0DuYkUoerCWrjK3DkNISajkLvUbyRTiMKP90tOOIK8qyOeHnplZzd2iXD4FjIGypUc5_wU9T1CM1-waQSGE9eOyWetb1LspuN6rMW24BdsHiNteSfupZiZqj_Qmv17qh4Clf7ey51j_kdHRhK6YQhPc3Aw3b4ESgeu9pRbVMuu5Kjab9KsEcVomxR92SMC67dMq9qCE60UWAZ6Ys4y9DCBBVowsj8yhdvxuNuqflAkkDoxhRoB9_D3-h8MfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a66581210.mp4?token=OT1VBFbumrYqj30mcFdfvlRu69Hwyk1YhOHhqs8MqsaMJySsS6mJtA0xbGwCXAXX1VmmA3DgWIylybjQuvQB6xQZVj0DuYkUoerCWrjK3DkNISajkLvUbyRTiMKP90tOOIK8qyOeHnplZzd2iXD4FjIGypUc5_wU9T1CM1-waQSGE9eOyWetb1LspuN6rMW24BdsHiNteSfupZiZqj_Qmv17qh4Clf7ey51j_kdHRhK6YQhPc3Aw3b4ESgeu9pRbVMuu5Kjab9KsEcVomxR92SMC67dMq9qCE60UWAZ6Ys4y9DCBBVowsj8yhdvxuNuqflAkkDoxhRoB9_D3-h8MfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان على كنارك وقشم وسيريك وتشابهار</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/84532" target="_blank">📅 00:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86bb21e994.mp4?token=GbOI2IjA9tRvL3x6fTkIZgtqoj0Z3YBfKJU_GBAhiDoKj7MLE9F3Ayz7u9NR_r9sr7lTCKBAwxr_ZB-xBU3JbX3b6kAd4HHSE7cIitipDcjlzy-oo46TkdPU8-iIfshxvWFLJAfkqN-eqEKeC9zX8nBCYLGgDCpSTF3wrgLEFP9GpHpJ2pppXHEIcuKh1GeYsN1JrgipQ97K0y3TAY03DuJZs-hE0M_1550fapXa6yYOVImag30bua3vZ9mV-dKKdasL7OCCU3NZy35NUSEMCfMez5KnuOiRt4qO9nplm3qvW86lBypZ7wrXielsMo_qjT8VBIvJMgZRrt31edlbEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86bb21e994.mp4?token=GbOI2IjA9tRvL3x6fTkIZgtqoj0Z3YBfKJU_GBAhiDoKj7MLE9F3Ayz7u9NR_r9sr7lTCKBAwxr_ZB-xBU3JbX3b6kAd4HHSE7cIitipDcjlzy-oo46TkdPU8-iIfshxvWFLJAfkqN-eqEKeC9zX8nBCYLGgDCpSTF3wrgLEFP9GpHpJ2pppXHEIcuKh1GeYsN1JrgipQ97K0y3TAY03DuJZs-hE0M_1550fapXa6yYOVImag30bua3vZ9mV-dKKdasL7OCCU3NZy35NUSEMCfMez5KnuOiRt4qO9nplm3qvW86lBypZ7wrXielsMo_qjT8VBIvJMgZRrt31edlbEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/84531" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سماع دوي انفجار في ميناء لنكة جنوبي إيران</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/naya_foriraq/84530" target="_blank">📅 00:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/84529" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات في مدينة شيراز الإيرانية</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/84528" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الولايات المتحدة ستفرض رسوماً جمركية بنسبة 50% على البضائع الكندية</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/84527" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">إنفجارات في محافظة أصفهان الإيرانية</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/84526" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
العميل وإبن الشاه الهارب "رضا بهلوي" يقول إن التدخل الأجنبي في إيران "ضروري":
يمكن لهذا التدخل أن يساعد بالفعل في إنقاذ المزيد من الأرواح التي [قد تُفقد] لولا ذلك.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/84525" target="_blank">📅 00:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8b4dd13a.mp4?token=t61vb-UCkS1FFD6GSiyyvt8c76ZlsAl-SpWdAzYSA_jugD8sIGsh3l6iyshhx6dhzLkhsjaSbp6OO67hFLpuaLKiUAZyRVQDZBqnbPbrfakHcTimwomePF892NXp2ZYnCXuS66qNOxvCSDa9ZM4_jg9lV7lsbs3CwJjZA1VfOqFGL8hLpBuuyn5wo_uwMgK_jllyQxDYx_WFyKJ8UtrOZOgGrZfjIzUzwubr6YvPN_c1-kxmixF5-oMhbfGI-YkjG2Uy6DrV7FKnibFD1258ANBKiHqRZHiyYWGqadTLNNmqId28hM0sZ449D0Vedv81y8hqzt-3ur2W-7-ZL3WW9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8b4dd13a.mp4?token=t61vb-UCkS1FFD6GSiyyvt8c76ZlsAl-SpWdAzYSA_jugD8sIGsh3l6iyshhx6dhzLkhsjaSbp6OO67hFLpuaLKiUAZyRVQDZBqnbPbrfakHcTimwomePF892NXp2ZYnCXuS66qNOxvCSDa9ZM4_jg9lV7lsbs3CwJjZA1VfOqFGL8hLpBuuyn5wo_uwMgK_jllyQxDYx_WFyKJ8UtrOZOgGrZfjIzUzwubr6YvPN_c1-kxmixF5-oMhbfGI-YkjG2Uy6DrV7FKnibFD1258ANBKiHqRZHiyYWGqadTLNNmqId28hM0sZ449D0Vedv81y8hqzt-3ur2W-7-ZL3WW9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لقطات حصرية و اولية من قاعدة موفق السلطي في الأردن اثناء تساقط الصواريخ الإيرانية عليها بفشل واضح لمنظومة الباتروبت.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/84524" target="_blank">📅 00:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjLiwsf40HXk5onCZ9p1kjGTSxb_5yhXyzjGltsR_G1ElBk5XayzioadRS8sEiknOAv9jbB_7WN2a5oDVp00JuchpJNfk7i4pkOW7nVXwNvrDGeI7GOOqeJTUb4QCbB6pRPPjUlWP3fmEkq9Oyt54JkIXN410KOIuJo17bsi_rZWE5tZwRad7cGs-YoWjUp2Xx4uJ1JATrT8-8DV6xqCxRkvQzjSKPcYux1fkdug2I6muwgmfqp6Tg2pKneYqaAXF3a-zGTNC2CMPmTKyOhg37ezZY2jy0-eXGiA2ugSYJGVBZi_Bt7iIsg7j-qPWKq0_OGY0MNYvsV3rXz-Y2rcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار الانفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/84523" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-G_iy9HlbOv6XFUtqnzBs1WiT0R0USeaVGsc5tYPP3S4Oe5ScSu_RdCvI4G_X3R2v9PByQvEEV4ViAq4xedCqv_0lRvCWj0S5HSdn2Cr_LJenTHobnWhTP3JRGs971sJfB6WDALO8s0hHUfd8lzuzMFsZR94jLSsVbe1q6X4mfw2FxamAo5WBEep_OWCL7n_S0CHaovC1Ruh43FAt7jMSEjCiZt7mQNwa0W-gPLNPMh1cUAA1ZJKwl4QN2ngGj9XtziLDnbD2SQncWxXT-WpeHdU-1ueZgNKBnkF-q9LHg5D_1GtodWleA2LXjHfT8jRDRRJDBDIRb3BUWTEePTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس سعر ٩٠ دولار للبرميل الواحد ، مع توقعات بارتفاع أسعار النفط بعد إغلاق مضيق باب المندب من قبل أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/84522" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84521" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معارك بحرية في بندر عباس</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84520" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84519" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
الإطار التنسيقي يعرب عن دعمه لنتائج زيارة رئيس الوزراء إلى واشنطن ومساندته للحكومة في تنفيذ الاتفاقات والتفاهمات التي جرى التوصل إليها</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84518" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5zqGssS7Bu_h1AKI5KAA64z6atSfmFd6tiooN3X5OzwVASfQnRiixKUlwg6aMZSmsnKPxNNeRaUqfOM82LlDywKcYpNYWP0STv4GO0qRwR0xgr-DvlrkDqkgECPHpTXPXU6TBIAg-g0iOfF7sRv4s0lbmu3TgTbdRGc2oCOybuF0oy5aVYWLtV9t5Kj8TY8xmU2vZryG0DV1S6CK11vvTvchuuVmRxhZ7bT-AktivIe_Ouv2-QBlOtKzoAVVc-uSC4-qclqgrlkt4urnBoLhpFj9g-0RfgIFHl_CqfY9H4dh7TjS1RBQpfFwmdsxBQ50ZNtoFxQaoQCQV5eo2q4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
لأول مرة منذ القزو العراقي القاشم
مواطنون كويتيون يطالبون الحكومة بايقاف شاشات الإعلانات في شوارع الكويت بسبب استهلاك الطاقة الكهربائية، يذكر ان الكويت تعاني من نقص حاد بالطاقة نتيجة القصف الإيراني القاشم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84517" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/birGcqjUoomcUG4CyHl7rofVNmuzHwhPxaFIGKHtPUOYjkfxlgbALimfiNoEeWPUFIs_EsIA6KeY0tnTSO9w_P4eyrm-qs4Atf7WvbF-epu0aPShOK8sBqLssqxlalvFExVcSAEGFBEaOBh_PgtlCGcKCPckn7kiMDh_8h1stKebPxLEr2toMA4OBhln4o6WAIDFWYmDZvcJKq6TXlPadlQolWJfekZ1SdpodDIAqpzrYxjoSC5mUtcUmbCVCXnX0YlskJt4_hkCiWSIHxjoxoWBVQuCuiPtTEWbuxclkLPaxUtJIrb9phhjy286YGdgOK9Yu0hjTY-y-Q7cfQ3g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مواطن كويتي يتحدث عن القصف الإيراني : ايران تقصفنا على مدار ٢٤ ساعة ليل ونهار</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84516" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUUdYazug7TTy2sE9sdDV5w2bZcdrwbYmT-hEWyPA3iMsG_EhjwXaOrM26ZEnZgNldv1fTLHlv1_aWVSz1GFul6y1En37lbCW__F4UrmzZtoU4iiFhWcx2VS_uKDXf9miJYdoodVx2JJ81-CNSlRQcRHveVPhthxWwIoNUS_MO8e9hj_cjzKt-9nhwZ4Wakef8emOmu6cv94TA_FHGcwii6H91Bnk9qDhVsL5srg4mJ2R0-GkvWJBc4xSZ1xXZVTFHzxJenkMt9NIkFxw0GiZUPxl-G0CVr0Q_fmVlUgx38c-QgHzmPsSWs0gZI0-bUy_j2tDQ-JpzcesaZmsx1Kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اضطر الموقع الرسمي للمنتخب الإسباني لاستخدام الذكاء الصناعي AI ومسح صورة تواجد ترامب اثناء الاحتفال بكاس العالم ..</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84515" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84514" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي تستخدمها لمهاجمة السفن التجارية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84513" target="_blank">📅 23:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84512" target="_blank">📅 23:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
السعودية
: ندين بشدة ما تطرقت له الحوثي بشأن حظر الملاحة البحرية على المملكة.
اضرب ارامكو
😆</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84511" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84510" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
قال مسؤولون أمريكيون إن ما يقرب من 100 جندي أمريكي أصيبوا في هجمات إيرانية على قواعد متعددة في الشرق الأوسط هذا الشهر.
‏تعرض بعضهم لإصابات دماغية رضية، لكن 96% منهم عادوا بالفعل إلى العمل.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84509" target="_blank">📅 23:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
🇮🇷
اكسيوس :
مسؤول أمريكي يؤكد إمكانية إجراء محادثات لوقف إطلاق النار مع إيران ..</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84508" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cdb4e63c4.mp4?token=Y_676zQDzSlEpjaZfjdS2zMg1rcSNErhVPkwHYJz4lmw14ABlU5SUtlTTyMpchT4T6VuWyrAxrxkQJiPMEsBK3iK0epYKp--0qkwk_84eXFaJpzqfLo5ODz4eQHwBunBDQYZsXv5BVxQMCCopW45pmb_3gKaaztVJIJSf6rtm28ovAv9jXdKByQ5Jv_hhKLzxwgTGOD-tXDzYcaepWt4gIY-xM2ARvdBHRDWpjOCUwVTJM9iVTaOgit8QrqB_CrTqtjSUz8vtRT9JSb9TxDjGk66PB_g0YNmGACuZCAmrh4_Bw1TtSkxyvM0I-3ljIcVLvV4aFLZBI9VCDCc7pwOYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cdb4e63c4.mp4?token=Y_676zQDzSlEpjaZfjdS2zMg1rcSNErhVPkwHYJz4lmw14ABlU5SUtlTTyMpchT4T6VuWyrAxrxkQJiPMEsBK3iK0epYKp--0qkwk_84eXFaJpzqfLo5ODz4eQHwBunBDQYZsXv5BVxQMCCopW45pmb_3gKaaztVJIJSf6rtm28ovAv9jXdKByQ5Jv_hhKLzxwgTGOD-tXDzYcaepWt4gIY-xM2ARvdBHRDWpjOCUwVTJM9iVTaOgit8QrqB_CrTqtjSUz8vtRT9JSb9TxDjGk66PB_g0YNmGACuZCAmrh4_Bw1TtSkxyvM0I-3ljIcVLvV4aFLZBI9VCDCc7pwOYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
مواطن كويتي يتحدث عن تعرض طائرة عسكرية كويتية إلى هجوم إيراني كادت ان تسقط !!!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84507" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpYIZMkgK2na27BN2t4KcOp3KQWTYRb71hTuWk8-TMsRqMHjOxQeXVWp88gQ7KtGiN8AFXlufqw0JnYeaferSZvpzhdlyptdVmCMrN6MGgxYQI1taOqL3_k-TdFp9T_4H9BwBuOEfEAkycQAGF9Lq0UULFtcq7e1EBL_n5dJAo8cIdpK8H_0ZViD6rciSw9f4Rq9mrP8VB3iLT4pmNDGoVpDeiiWnlNvPdAGPnoejqwaF4FPtUMZ_5-D-ZA0NDL98BeKqYbQ_1LJGl5O25GTeEaGrJAyYKlDhJoY_bfKD9baFrXjdFlC-mJN2jZR_oHqrYznO4wmUVcxNzAKmoWpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
كتائب حزب الله في العراق تبارك لانصار الله قيامهم بالحصار على السعودية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84506" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjPPK5g0wabe_7ZMywxcR37QVtE5SOhJiiSJK6zPIKGcS0-KLHPxNPzOMDTL_QWIv7jg8viOSDTdxgecHCZOzR6GBh7qhvlXLhl8DScgSA7KN0CIXlFqRBVZzg05Mz6gaMg5N2frS7vA-HbDRXj2HFYNarZv7pZyiNEXH8N03vqiTXYbU5uhXQEwcE4dY77HfphDX4k-vhDzFVTf-CSe-ciQAKsqi9DBcO5lX_SlD1JZynwmyGtDQOrvzuaUdLdOb8ADE1CWNp6gPX9xpvNsXUQgC8XCF6CngYzoz9ywd0tVSnzj5kXk1x4YfEbuCQPaiFjAazaRt0vYRQq9weNyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
مواطن كويتي يتحدث عن تعرض طائرة عسكرية كويتية إلى هجوم إيراني كادت ان تسقط !!!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84505" target="_blank">📅 22:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4708281409.mp4?token=st51fxrKBf-HEvcu5XA-u5IlxiPhnK6OmWR6rYqFs7HhvcJlJOELaooNmasRETBehMVXHqQbf75ZFUFZjmKvufXFXOg9moSWNMABL_NUk1BpgoSVlxXkOU6ly4oFsN8r96BTNfTOxjQKUDEs8mElKUm7-qxd4TQqmcKT53xVwWfR-QBVuQ6mt8_3S79cLOLsny5fs1TQ7DGR8gPvtKfGwHmG7uP1J5wJz3YMwcyMEX-breGo4YKn-Iehxgs44BxEfEp9ZQy1vUf19Xb7MtvRuZvXQ7Nd30mWRDN8QXGUt1ww8enAEV2mgU2fNj812LBo1TxzRSihpyHv364bBlWKHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4708281409.mp4?token=st51fxrKBf-HEvcu5XA-u5IlxiPhnK6OmWR6rYqFs7HhvcJlJOELaooNmasRETBehMVXHqQbf75ZFUFZjmKvufXFXOg9moSWNMABL_NUk1BpgoSVlxXkOU6ly4oFsN8r96BTNfTOxjQKUDEs8mElKUm7-qxd4TQqmcKT53xVwWfR-QBVuQ6mt8_3S79cLOLsny5fs1TQ7DGR8gPvtKfGwHmG7uP1J5wJz3YMwcyMEX-breGo4YKn-Iehxgs44BxEfEp9ZQy1vUf19Xb7MtvRuZvXQ7Nd30mWRDN8QXGUt1ww8enAEV2mgU2fNj812LBo1TxzRSihpyHv364bBlWKHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
🔻
قاعدة برج ٢٢ تحت غضب رحمة صواريخ الحرس الثوري</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84504" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF4rgnFmgWSlskCHMHOh39eJaAYsc6E6JsWYr_K38fkZoMWGbquyG5MsXFozrFwQDqigoCrqRTXCodtwUL3Jj9Oadjw0ky3BamGHS4UibTC2WaF2I5TWOC3w_d0BKTBa9V5VWzTFK4o0NwvcXWX_oWoRpPWp4FkzvWjA9gQNLUJwZdhIhDae3t2oi_4YlsxqSujL0RNh099iUXh1ljqBsqOjSX5TJhCr1V4Ez4xKHpx8ss5CeY26xMobkp1Xpp2ssvSqiqpmHs13DXS_PhC8QGVeQ8wR8vy8SRz9mNhS1tA1YSYw1seAzzZSCJ4p23dVq7BGndia0gzQmJmuk1__Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asFDLsRckbMTESLeD3JYM2qkTSzFg2zULjJ3FPrkgrdHM5AMcVW0Bqj9Re77JLlqpE6PNKbrGS2oUc5eQblXqSPXR2a684tOsJCfyZVfj0T1g__qqYMH51dm7rsl_gtKCwNAez7jJgY7wr4h1is4maHNpQd96_ABkgoLvm3hF1bRRHdR2pFFZjhdyusIvZAfxt-BB2M_50FakM88KnXIzlUF2coIC4cUPZ0t6NW4WOwJrB6tnIG5GMPpKJquSsOBFIrZ1Ue5gTXX8tGqPtb9K_MkcrIBVorv1SbIhC1_vvoFUzF6f5s1S85CKtDyKnf1NRqi6MLQqpxfo3oAdiM7YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اثناء انطلاق الصواريخ الايرانية نحو اهدافها</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84502" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYERH8RhLXv-fq4DDS-4NH3nhGojDA59s3olpAl36xVjsMv8NgHrGxOBbsNKQ8S5aCJ3hyynTOkEktCgTProHO-Vz6CMAjqV5LtQacL9kjEyQT0urMqRESmTYWvNdJzH_cmIPn0go65TT3WHIAKwHJSk_4iJe3AKy5B9ksLXmPwghefih6xIH-sFZIJpHWPOLDHyJcwRMR4vqq6Vp1M5bBq80BsegGqOwgro663f9xAGvblD8fWy-HY9FAr8SFVZEP9JIRjdCFMJKuWEVt7S3gk9BPNr5mWjDsgtayEF26j-Mm8fr-DS3bnvEdwQZAqSWYRYWNKStMhOp-0YuIWoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تم اعتراض وتدمير صاروخ كروز أمريكي معادٍ في سماء جنوب محافظة كرمان.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84501" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استهداف قاعدة الحرير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84500" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">أعلنت الخطوط الجوية الفرنسية تعليق رحلاتها إلى دبي والرياض مع استمرار الحرب في الخليج.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84499" target="_blank">📅 22:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تايلر جيمس فيهان من هاواي القتيل الثالث الذي قُتل بصاروخ ايراني بقاعدة موفق السلطي بالاردن.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84498" target="_blank">📅 22:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d6a551d.mp4?token=i9MGxi0YIwEJJThbJ2OdDFrf2RbCtEA44ObSMs30VVA512GiRMkcoCRwLZHK0xOxba0DFihm-ieNJ6oa4WjFJ7nk-r-7o514DCbkAucT3EY2qZ0AGmjwY6btn_bnHNIJ_VzdzHgvnbeMEMv1tfKAS305tMvDoWmYQC8ehMj9TzFyKoJcS2avB-DqeYEi44tsZHVqXkQQiZGT6jzlHiYAPYmt3hWXaMlB8Uc_YmKmJGiTrszDL2BL1vq8z_YjsvK4D05FXb0PQpSpRF6Tdvwv0NDdrPioZ8k1lHYTGcFfJ8V-XEGbbmlO31ESiwFBIn-g0ToCdUdwhfZa-3irl39xeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d6a551d.mp4?token=i9MGxi0YIwEJJThbJ2OdDFrf2RbCtEA44ObSMs30VVA512GiRMkcoCRwLZHK0xOxba0DFihm-ieNJ6oa4WjFJ7nk-r-7o514DCbkAucT3EY2qZ0AGmjwY6btn_bnHNIJ_VzdzHgvnbeMEMv1tfKAS305tMvDoWmYQC8ehMj9TzFyKoJcS2avB-DqeYEi44tsZHVqXkQQiZGT6jzlHiYAPYmt3hWXaMlB8Uc_YmKmJGiTrszDL2BL1vq8z_YjsvK4D05FXb0PQpSpRF6Tdvwv0NDdrPioZ8k1lHYTGcFfJ8V-XEGbbmlO31ESiwFBIn-g0ToCdUdwhfZa-3irl39xeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
مشاهد جميلة مصورة بعدسة عراقية من انطلاق صواريخ الايرانية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84497" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c5ba4b30.mp4?token=JBqEsoC0OgsS4tAjzclHVs3h3rkFUoWtW6IjP5qYauEpuWNEroM667e8b0iXod5oAEVAqGD9o-IfO3vKHvpXBBPv40B0aYuGm7BFeQBDM6sq8x4aLgkAaORR61iemsgdsfb-pCgi7-WW-B_DZFlM1OCbr603gURV2njGl0XsYaeklOGEKlox4LjJimShTuvB3fbDOVwiZEZ2P3deIbWj2VBF2tA7aSVpD3mJ_dnsBFmVKKxAIQic6kXauukA7frPLH5lGk7NamGX0IsAXJUJP5MV2wgmLvbO9bYWRepNWoHL8SPW2OLHOctqRW8N7G559zs6lmF_tyDE09Ugq0EzHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c5ba4b30.mp4?token=JBqEsoC0OgsS4tAjzclHVs3h3rkFUoWtW6IjP5qYauEpuWNEroM667e8b0iXod5oAEVAqGD9o-IfO3vKHvpXBBPv40B0aYuGm7BFeQBDM6sq8x4aLgkAaORR61iemsgdsfb-pCgi7-WW-B_DZFlM1OCbr603gURV2njGl0XsYaeklOGEKlox4LjJimShTuvB3fbDOVwiZEZ2P3deIbWj2VBF2tA7aSVpD3mJ_dnsBFmVKKxAIQic6kXauukA7frPLH5lGk7NamGX0IsAXJUJP5MV2wgmLvbO9bYWRepNWoHL8SPW2OLHOctqRW8N7G559zs6lmF_tyDE09Ugq0EzHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84496" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84495" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtqwk2VxvEDyJfO-aRMf9QTdUdzZQnwjCtJ0h6R8vUDg6JMhJKJfefPO6TEV3RsRDBbjZ0YdF3py2mASaWwhUzQ_NZVJlu3PzD5vaVh5G1TVxq2QVN9ChBZFk29M1qEBb9uZY52831_PvOjS59MgLRPhL2SgIItRdBptbGnKyhZzLf8krPS4aJZJaMU3Ru8hM7S7U-ASvYIntf19nrrJz-QXcAfCRJxDJEMgKyb3HskUErftQIeYcwy9PfOK6EqRCBCzlvmJGLcYlO0QO4aphh7hD4EC7T64Pn5hEtUBYqww5WDJH6CvQHoEsr1nRnPEvu4-KlLPnpA3xrlAaPXRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأردن تتدعي : اعتراض وإسقاط 3 صواريخ قادمة من إيران استهدفت أراضي الأردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84494" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab6ef0aca.mp4?token=nWdny3_k9h61Q3apEWicLLgSSA0rRBYPpZKYQRlE8cy6EtLUgw2CCm3UTsZf04YmKTgxPsUN1C4H79FA6Fs5F6uph4PMec7aCFsB0-MmBwCQ4LNjl6DrxJOz_Tv7Mos2uLr0909KpIZFwuo2z7IaAW5RSWILc9OYKNcfNl0S_aK662AqMMufFPYF8S8EDVRYD7NGoIjo7m4iE3N6V8JhkfRnjsMmw63QfJLup2G6Eb2KTMRl5OPnQ6e4wNsZ_0tEyXX5ufAnkmsOAUptLAtph7VdC01sSadybfPsugPY6TEUI9MtleywSP3DnXhpO84Ssp0mZXSGCknpiRcFMxfMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab6ef0aca.mp4?token=nWdny3_k9h61Q3apEWicLLgSSA0rRBYPpZKYQRlE8cy6EtLUgw2CCm3UTsZf04YmKTgxPsUN1C4H79FA6Fs5F6uph4PMec7aCFsB0-MmBwCQ4LNjl6DrxJOz_Tv7Mos2uLr0909KpIZFwuo2z7IaAW5RSWILc9OYKNcfNl0S_aK662AqMMufFPYF8S8EDVRYD7NGoIjo7m4iE3N6V8JhkfRnjsMmw63QfJLup2G6Eb2KTMRl5OPnQ6e4wNsZ_0tEyXX5ufAnkmsOAUptLAtph7VdC01sSadybfPsugPY6TEUI9MtleywSP3DnXhpO84Ssp0mZXSGCknpiRcFMxfMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق العديد من الصواريخ الاعتراضية من قواعد الاحتلال الاميركي في الاردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84492" target="_blank">📅 21:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqCHJ2XaeHoVQV-TiVPYF1r7s1dsTVV0QHyqzHCG9DOz2g88mB-npdFXpMlcCxEkRqEkkyg2Ab21F38rv8GTtcx7WrbKQTNMu2nk3fnJyfmovkLwg-L5rMHnUUBuv1IAHa_rp4WSPBJt4vzcU8aXn95gRKNcmhmJ2PF1vrvn0kVjWVsLSTdLHWKKm2OLbW7tfV-qxhY5fKRRHmK8QPDuXKcpE7Z9YI0_Tz9dcib7A50VUnV-Aa1K1jc1ejnULULZjLqSKPTJcSrI7dvqfoTHxPCm7Y_GuUoqO-jAIuBg7k79sAtIESCR6Ujpr6U_ORjVa2BnaV83pmpa35oD_S7gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
نایا 10K شد
از اینکه عضوی از خانواده نایا هستید، سپاسگزاریم.
@Naya_Press</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84491" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8929456f8.mp4?token=KMsczyGyb2Kq4fwx0EmZ0XTn7KnytDIUvaREOY00KA_JPyZdW4bQO714J1LZuUJNtp9VE6UrlsD8GCp-vjbkQJQT99F15DEMFX0kcJ7dmz9XGSc8cDM95JnSaJhfidNYKMtLQ1A2WhgmPOwOnyOsn2fDaTE-dke_9WXAqkCY3pBNUDsozZVapib7sP4-QqViWouvKsSZDa-9WZtsBjtOFCzT5VEq7-X8Yim_PhIPncJ8ChMkZN1qzM3jA0cIyaHs-O1qOhquP3afgBQwcodHlD4jMvB7VTMVIBTcV4YeJqSUmgJilITwPr5naPlTElCFDDTCKJ6jOGRS5GSlmtS2kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8929456f8.mp4?token=KMsczyGyb2Kq4fwx0EmZ0XTn7KnytDIUvaREOY00KA_JPyZdW4bQO714J1LZuUJNtp9VE6UrlsD8GCp-vjbkQJQT99F15DEMFX0kcJ7dmz9XGSc8cDM95JnSaJhfidNYKMtLQ1A2WhgmPOwOnyOsn2fDaTE-dke_9WXAqkCY3pBNUDsozZVapib7sP4-QqViWouvKsSZDa-9WZtsBjtOFCzT5VEq7-X8Yim_PhIPncJ8ChMkZN1qzM3jA0cIyaHs-O1qOhquP3afgBQwcodHlD4jMvB7VTMVIBTcV4YeJqSUmgJilITwPr5naPlTElCFDDTCKJ6jOGRS5GSlmtS2kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في عموم الأردن بلا توقف نتيجة القصف الإيراني</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84490" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84489" target="_blank">📅 21:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0bbf054c.mp4?token=WA4_VfCC62ARb7Nc8ICvCUnEIdmIaYcPo52CwBqcL1JNSKpOOmJQ_emf4qnJ5p7OG9Z-KUw_4eEDEWgduURglD17-iRB7THYHhACnSxsSMuY7kin2j_Ga5Jr6fu3MCCJOdUnXKjZn7N2Qe6GG7WfRMB3DtrKYJ6LV4oCV6-VyWbkP5fciMOCu3PMx--HEdC92Mp0Oadyuc7O5MI8RadXBmaavdbNap2_B0LW3rXq7hGgaIKhn1-HMJj8nAExCV7iLubwuPSNVbtjmEiGr4FqIgBr6Ki-fzet0TCFk9lESzayab8PqZxUbhFmIamQsvXvGIu056GrSCxlkH0sSu_VEy9vKgR278LkH0PKG34geN4dCcE3959YiVV9qlf5EzdJFFuyf_9QS66g5LrysddXQH_t_cQc7hUgSfq9zG50YQE5oAK4bHRrrQKQshMEpbfUeQeGc2WADhVwF6Tpk7lh1TMAFd7SUjnufaW6FM0ZBn-5Vnv88ASJbrD66dXHzpMkbC0KEDUIzgnSaomvGoynEYctcpBi2maTuQKcjk0DzzQBNtqpDDEEOQ9Ibl5hB95UMtB206zTTE3yUM52DgBDGMPBDOH_MO2oSKhNyHolMHZgv1Gx-dqx9s6qop8rp86lmIEi7Wrwc4PFWstdUnqgJEUJ7NrDsMrkw5X0WHzpfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0bbf054c.mp4?token=WA4_VfCC62ARb7Nc8ICvCUnEIdmIaYcPo52CwBqcL1JNSKpOOmJQ_emf4qnJ5p7OG9Z-KUw_4eEDEWgduURglD17-iRB7THYHhACnSxsSMuY7kin2j_Ga5Jr6fu3MCCJOdUnXKjZn7N2Qe6GG7WfRMB3DtrKYJ6LV4oCV6-VyWbkP5fciMOCu3PMx--HEdC92Mp0Oadyuc7O5MI8RadXBmaavdbNap2_B0LW3rXq7hGgaIKhn1-HMJj8nAExCV7iLubwuPSNVbtjmEiGr4FqIgBr6Ki-fzet0TCFk9lESzayab8PqZxUbhFmIamQsvXvGIu056GrSCxlkH0sSu_VEy9vKgR278LkH0PKG34geN4dCcE3959YiVV9qlf5EzdJFFuyf_9QS66g5LrysddXQH_t_cQc7hUgSfq9zG50YQE5oAK4bHRrrQKQshMEpbfUeQeGc2WADhVwF6Tpk7lh1TMAFd7SUjnufaW6FM0ZBn-5Vnv88ASJbrD66dXHzpMkbC0KEDUIzgnSaomvGoynEYctcpBi2maTuQKcjk0DzzQBNtqpDDEEOQ9Ibl5hB95UMtB206zTTE3yUM52DgBDGMPBDOH_MO2oSKhNyHolMHZgv1Gx-dqx9s6qop8rp86lmIEi7Wrwc4PFWstdUnqgJEUJ7NrDsMrkw5X0WHzpfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في عموم الأردن بلا توقف نتيجة القصف الإيراني</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84488" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
🇺🇸
طيران بريطاني من طراز تايفون يحاول التصدي للهجوم الإيراني على الأردن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84487" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=B2aOBhxb8jeuWc5AdMXowJ8RF5w9Rg89Bj81k-c9jUX5QieBuPwY0EcUJec6GUvjkx4iEtxls0gn1YHXJEObKd9ov_U7Nn4boT3gdyVpmbxK9Q6V_QMlvCYHk28cPeVHOubk7xcI7GxMe0_3IZsnOUmTwnZgPmhZVdzHADEo4wJzAzEEDZ856lmkFlCFTBkxBJBigDYPVeJsRhTGDPMBXWlXOzP3c7XvCVSdsR2egDrneWIxRiO7cV3Hj-YCFvcz6kEBAnza4Ftl5r9wxxM76ENrc3TwvZc5FUeG25hshkvOlk_WqE3OhMe9pLIUewSE2rugTSxAmSysbWf_yTd7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=B2aOBhxb8jeuWc5AdMXowJ8RF5w9Rg89Bj81k-c9jUX5QieBuPwY0EcUJec6GUvjkx4iEtxls0gn1YHXJEObKd9ov_U7Nn4boT3gdyVpmbxK9Q6V_QMlvCYHk28cPeVHOubk7xcI7GxMe0_3IZsnOUmTwnZgPmhZVdzHADEo4wJzAzEEDZ856lmkFlCFTBkxBJBigDYPVeJsRhTGDPMBXWlXOzP3c7XvCVSdsR2egDrneWIxRiO7cV3Hj-YCFvcz6kEBAnza4Ftl5r9wxxM76ENrc3TwvZc5FUeG25hshkvOlk_WqE3OhMe9pLIUewSE2rugTSxAmSysbWf_yTd7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تتوالى بالانطلاق من قواعد الاحتلال في الاردن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84486" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10e9679e1.mp4?token=rw0HgJ9dtq5IoXASTtz2lmuVlhAcZHYWdYuurBR57SFexPCY25IOtD_sOU705l080e89FNR8dROjFjchYJO9Qi29WujWudZ5kZlbypZZoRTdzWt3-j4Dig0tuLMs24cC2aYePZ_atkrs_Cx3OFQlNl647hmY1x2thakrLwYoClJdO30ionhudbjtNViabMFVHMnwvuX5sPM1B6kVwEh_XNCzKTV1uQ4ZKlldEa4apFYyMqHuc4EoT1Sb1yxSBa9F-sQkRcAlX5ocF0_DdyqBSx6VNZq_LlBeymVQNT_wbaxB2Df7bF43uQVuwgyEyA09BQqjiTGB9FXG0drz5zjDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10e9679e1.mp4?token=rw0HgJ9dtq5IoXASTtz2lmuVlhAcZHYWdYuurBR57SFexPCY25IOtD_sOU705l080e89FNR8dROjFjchYJO9Qi29WujWudZ5kZlbypZZoRTdzWt3-j4Dig0tuLMs24cC2aYePZ_atkrs_Cx3OFQlNl647hmY1x2thakrLwYoClJdO30ionhudbjtNViabMFVHMnwvuX5sPM1B6kVwEh_XNCzKTV1uQ4ZKlldEa4apFYyMqHuc4EoT1Sb1yxSBa9F-sQkRcAlX5ocF0_DdyqBSx6VNZq_LlBeymVQNT_wbaxB2Df7bF43uQVuwgyEyA09BQqjiTGB9FXG0drz5zjDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تتوالى بالانطلاق من قواعد الاحتلال في الاردن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84485" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">إعلام أمريكي : مسؤول أمريكي يقول إن زيادة القوات والطائرات في الشرق الأوسط مقيدة بأضرار المعارك، محذراً: "ليس لدينا ما يكفي لمواصلة العمليات بأمان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84484" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e42363f.mp4?token=IEz9DPbpy5conwdfOt-MVRLXAsxeGa4PVigEDweaPQjwuY8FkYeUfSfsydsLW0v-uEJt1_PQ86Nl6EQw1oYNmW4TB8lsd3CoWjZbrPQxkew-Y8hFaVnyz8zoZbj4hRyRlZOmJ3qX0hWneQ1RUGKdni5NJCRKAJ7F0xQ6RR11e-8PxlCf9sJ4gwXdScRrMkpVYqX5tICpGYRu_AmnR7nxgQE0quMigP87s4T1E9X-db7dEGMhD85BAB_NUbFBqnbgfBNYHwVFFhp3w4kXMexC3_u6SUZzFWxbXsfXkBhLG58r_43fXWi1-7lnJ4kdj1faOcw6HM0om-4KzaQ5A5zVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e42363f.mp4?token=IEz9DPbpy5conwdfOt-MVRLXAsxeGa4PVigEDweaPQjwuY8FkYeUfSfsydsLW0v-uEJt1_PQ86Nl6EQw1oYNmW4TB8lsd3CoWjZbrPQxkew-Y8hFaVnyz8zoZbj4hRyRlZOmJ3qX0hWneQ1RUGKdni5NJCRKAJ7F0xQ6RR11e-8PxlCf9sJ4gwXdScRrMkpVYqX5tICpGYRu_AmnR7nxgQE0quMigP87s4T1E9X-db7dEGMhD85BAB_NUbFBqnbgfBNYHwVFFhp3w4kXMexC3_u6SUZzFWxbXsfXkBhLG58r_43fXWi1-7lnJ4kdj1faOcw6HM0om-4KzaQ5A5zVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الرعب تدوي في عموم الأردن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84482" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC0Z2-zcyNkzKSzdo5UBNiYhVbdLpP927Vj-Gfj8ZhICuNdFH_GmlhGLKX0_3LZTZVPPHTUt4w5W6uJELaRDJCXe0SJA12cqph62NZmwb-bK9CRYM1taMVgUKTuQB0Irb2yNsApmCwkiJzFP_QaRNVed15RWw3oUr-Pd8dwbJDarB1592pHlo4OJGZWpmxZ2RCMFdx6UfCe_3735LdJjgVHaysB6Ck0wGdWi1Jz-DlxldvS8TBr7BD4FIW0nNsn4PjvfzB6xSTgzjUM56LrU5IfcTHYg579EisIrDhpc-fPwC6B6eqQrUfJty-b-gY_Gwl6dghs-mNZvt5Audd4Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثناء انطلاق الصواريخ الايرانية نحو اهدافها</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84481" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84479" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8882bd7598.mp4?token=in22o7GVf32I2CzwoDhRXmghAIGSOfTDyVFaNpmmhPW-fWPmBeHSPHpSyD2ZK9vVnQ7mK0UJKFg5B5mn3Wl04lKQgQs3z1XaD51OiqTdJOOtiJ9eCABNcTTU8YHvJqhtqJjpNU8CdLLthbzlJeQbfZQKKy_9uqxu9cUvfZlgiSpEF6fhumxa7WSKIaN03vie0cCbI2ECxWVj1eOGHTiF6Gp3H3MYKybVYUx39qMzOG0WPhM623jJOfNv8eivp1UwT-oJb5dKkLm1IeI-_ZVWRd-3lvGu8pAK8A3jXYD1ZH85IV4GflCszWshV1OH2xtulqI2kaK2MQmq3EfYHO1wbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8882bd7598.mp4?token=in22o7GVf32I2CzwoDhRXmghAIGSOfTDyVFaNpmmhPW-fWPmBeHSPHpSyD2ZK9vVnQ7mK0UJKFg5B5mn3Wl04lKQgQs3z1XaD51OiqTdJOOtiJ9eCABNcTTU8YHvJqhtqJjpNU8CdLLthbzlJeQbfZQKKy_9uqxu9cUvfZlgiSpEF6fhumxa7WSKIaN03vie0cCbI2ECxWVj1eOGHTiF6Gp3H3MYKybVYUx39qMzOG0WPhM623jJOfNv8eivp1UwT-oJb5dKkLm1IeI-_ZVWRd-3lvGu8pAK8A3jXYD1ZH85IV4GflCszWshV1OH2xtulqI2kaK2MQmq3EfYHO1wbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الانذار تدوي في جميع انحاء الاردن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84478" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbb776333.mp4?token=sBl-YMj4LUIbyqzddGAamOhhIxGpyjNp9DbfXYJzI_Kj_cRwL5b0vHFGzAehwr_-yttqm74QfDNJ6AE279CMikNqhLVsBQNcc4O3iSAfeMNrEQiX9W6njZOmgQR6c1O4fg_ks7jKV5TxZjFgO3hVUqrouPAdGmSdiXsEP9wbb5ZVrRlvbORkrEkUjTMsMg8lDgcaLEWv3IWTvRBL2gueq7a3eSX7_p7dxCLsIvEf5uszsslMaOpD23d8BcXb_wRE98Td5ppnnKp5S8C5U-wE_wnto1Xf6bU-itsphcGx1kIpVHRoF_2ZPR7tEpdKsh4K0-I1PnRJbTS5NGOEddheuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbb776333.mp4?token=sBl-YMj4LUIbyqzddGAamOhhIxGpyjNp9DbfXYJzI_Kj_cRwL5b0vHFGzAehwr_-yttqm74QfDNJ6AE279CMikNqhLVsBQNcc4O3iSAfeMNrEQiX9W6njZOmgQR6c1O4fg_ks7jKV5TxZjFgO3hVUqrouPAdGmSdiXsEP9wbb5ZVrRlvbORkrEkUjTMsMg8lDgcaLEWv3IWTvRBL2gueq7a3eSX7_p7dxCLsIvEf5uszsslMaOpD23d8BcXb_wRE98Td5ppnnKp5S8C5U-wE_wnto1Xf6bU-itsphcGx1kIpVHRoF_2ZPR7tEpdKsh4K0-I1PnRJbTS5NGOEddheuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تنطلق من قواعد الاحتلال الاميركي في الاردن في محاولة منها للتصدي للصواريخ الايرانية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84477" target="_blank">📅 21:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=nj942LwyIgzwmtcAUktWE3ti72C6QTNXXIANZb8UmWBM1dacre_wj3LFDfEqAZ4hI5xFLwTmaZ8gd_K-MbvNQmtM6Ac6GXY-LttOTY3DUS_SMUo74yt4FkDPoEW3U4Ohhn4TUS8K37su7srPwtl5KzI0qYuqtqKWpBzqbqDcOgsp-Z-8a16Exsgtfb1fQsezubpl9zW1-uWPAQrGPVE0yDLkeqvdtCg3Drpohu9-hmTno2UzS6ToWdD7plBdEouOKFKgPz7qpGuRTYyETFYo6B4Xd0icBvlytjLzoQJFvrcsUFsyRtw4wUfBujbkEJ9L94QgSaS-2dicTQaNmrM0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=nj942LwyIgzwmtcAUktWE3ti72C6QTNXXIANZb8UmWBM1dacre_wj3LFDfEqAZ4hI5xFLwTmaZ8gd_K-MbvNQmtM6Ac6GXY-LttOTY3DUS_SMUo74yt4FkDPoEW3U4Ohhn4TUS8K37su7srPwtl5KzI0qYuqtqKWpBzqbqDcOgsp-Z-8a16Exsgtfb1fQsezubpl9zW1-uWPAQrGPVE0yDLkeqvdtCg3Drpohu9-hmTno2UzS6ToWdD7plBdEouOKFKgPz7qpGuRTYyETFYo6B4Xd0icBvlytjLzoQJFvrcsUFsyRtw4wUfBujbkEJ9L94QgSaS-2dicTQaNmrM0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في الاردن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84476" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84475" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شاهد ١٣٦ بالميدان .. الان باتجاه قواعد غرب اسيا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84474" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=Lswqwt57sLuJAU3AA5JwUzkraU72lXtnz-wWQj7jaoipHxIF1_IgbP4AYabGz1waKSDDNo5vqLQyDffsQVdjkk0k3uiRfHHZC3s_94CwnrL2lCWLhqS7tCY3CQfSxrljP9sOa17IzjCTEF8kUzgSqvSk34Uhfr102beb79TbpRcIZ3coUwvEVccW2nt-vI0i7ob7uzoCnfNgR5f71tqy54ZAurlCFzA2ybVOoXojDi7qPqZ-KNR7TQ_6dQaAt4rfj-sMigZW9WGz5SyLe1RbA8zJY6bUG50Fuj-0mV9cv-UVQRkOTs7Rz4ByczB4qjJ8qcL1CWOfkA4QrPsB-l-XbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=Lswqwt57sLuJAU3AA5JwUzkraU72lXtnz-wWQj7jaoipHxIF1_IgbP4AYabGz1waKSDDNo5vqLQyDffsQVdjkk0k3uiRfHHZC3s_94CwnrL2lCWLhqS7tCY3CQfSxrljP9sOa17IzjCTEF8kUzgSqvSk34Uhfr102beb79TbpRcIZ3coUwvEVccW2nt-vI0i7ob7uzoCnfNgR5f71tqy54ZAurlCFzA2ybVOoXojDi7qPqZ-KNR7TQ_6dQaAt4rfj-sMigZW9WGz5SyLe1RbA8zJY6bUG50Fuj-0mV9cv-UVQRkOTs7Rz4ByczB4qjJ8qcL1CWOfkA4QrPsB-l-XbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهد ١٣٦ بالميدان .. الان باتجاه قواعد غرب اسيا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84473" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84472" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe61c52d0c.mp4?token=Ysm4TKBcRMzw-ZnOFEamNTU6FVqpwkkUinl4gcV-GJORzu3fj56B5ejuy_akqV79DWV1nhefAtZba_Viro5PI-x1wjBuQf-k5yHNDbt1Pc7iqPglvvUofwmR5enE-Sxsx3vVtDz7-jgNZKcpQ0b7kXqnY41y3h3ouRhp_Vsz3UjMM88LlSEqYUPUS91E19FVz-sQEimYFoCDGQytdKF0JhBHul8vkMA3kpVamYvmYTE-9FdKrwnjVN_zWGNUG9PGWwv1dGKzgIz4dy8j0u9tXRFX5xJao7Ywd8JihgqXQKx5dpmZGXnvEzQl8QbHWTJEsTqws2RmwCcvkNH9iDPc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe61c52d0c.mp4?token=Ysm4TKBcRMzw-ZnOFEamNTU6FVqpwkkUinl4gcV-GJORzu3fj56B5ejuy_akqV79DWV1nhefAtZba_Viro5PI-x1wjBuQf-k5yHNDbt1Pc7iqPglvvUofwmR5enE-Sxsx3vVtDz7-jgNZKcpQ0b7kXqnY41y3h3ouRhp_Vsz3UjMM88LlSEqYUPUS91E19FVz-sQEimYFoCDGQytdKF0JhBHul8vkMA3kpVamYvmYTE-9FdKrwnjVN_zWGNUG9PGWwv1dGKzgIz4dy8j0u9tXRFX5xJao7Ywd8JihgqXQKx5dpmZGXnvEzQl8QbHWTJEsTqws2RmwCcvkNH9iDPc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اطلاق المسيرات نحو قواعد العدو الاميركي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84471" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بسبب مزاعم عن نقص حاد في عناصر الجيش الكويتي بعد مغادرة عدد منهم البلاد بحجة قضاء عطلة الصيف خارج الكويت، فتح باب التطوع للانضمام إلى الجيش الكويتي حيث لجأت السلطات إلى من تم سحب جناسيهم واعادة تجنيدهم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84470" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9oNS-hPLRn_R4BWYJpmLSG8GE5Ds12CEL04mYXQI-xThJPJhTEBAjlkCwnaipzrHzwPW5ZM_1Ft49FUQvlvr5U9S2sDKVaw3WbRGfZ6hZSeY5E7wfwv_jJcgLrO7NAX5naN1AMTKSmA4Gu-wYK-pmHlcMsMKOzaN3cLSWPjz2nuKtomDuuPajliauoWo6rnXnGYfR8IAj4ora4b0-32zv1MiBiM2NPrDl0WTOYDbs4st1mijv5N0pMP-RgekMlqg2WfnKVbS1fXbWy4GLok3KaSUzag-5FEv0u7jbqDvUD5da_vHfcIJFekFeBSJvqqmkcRfdy5ie89Yd34vnTCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسبب مزاعم عن نقص حاد في عناصر الجيش الكويتي بعد مغادرة عدد منهم البلاد بحجة قضاء عطلة الصيف خارج الكويت، فتح باب التطوع للانضمام إلى الجيش الكويتي حيث لجأت السلطات إلى من تم سحب جناسيهم واعادة تجنيدهم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84469" target="_blank">📅 21:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2G742n7xUqbMAVa5KuQBKWuB796Q73OCvZCyQxi8jdgHYg7-v9zbGDUTolf7AcN-atk_bW7PMhfWmJLwddZo4LE1XHyfLDpNNptU8lAPzV4QNOreWmcXBi2-Cy0TRFfJ_BzDg4t6eC1SsRl287KbgiQRX3k76cJjHmQ1jfQmJbVLnJEUDp0gf1mdaVCT0ic3qE-bNjfI53IGaHoYCiOlENM9NxyGCcV5vUx2BKmAsPzdMNMbMySyJ-VBo-j8yTgTpsKr0MRbr6trdeelVP8QPV1iBt8q__Hiz8ZypEWHcQgfrQ8U7uwT4kuze9voFcgH4aDoNc_JUjLiY3wYCDoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏هيئة البحرية: بلاغ عن واقعة على بعد 17 ميلا بحريا شرق دبا في الإمارت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84468" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84467" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
خلل تقني يضرب تطبيق فيسبوك.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84466" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تايلر جيمس فيهان من هاواي القتيل الثالث الذي قُتل بصاروخ ايراني بقاعدة موفق السلطي بالاردن.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/84465" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/84464" target="_blank">📅 20:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0TCY_pb6TBHEgWEnPxFIShCgVEHYStKx9_-aWwDxzUCUqW9GCHa4FVh_IURb5X8a7m-n6_yZvMBybcwpkqxGZib2HA5yfxynJIcBNJB1jkCnjrah55x3_Wix3lTtYNW_zp7oSmjv0ufki_CqP37h8-sfXpxTOE5YDR9kE6qSCiiKjGs0WVUa5a4gvbJtmHH51cKQAjQyFOqXRkWwJ5jKWPJ4BWnws0421t-V6QS0j-emZwppTBCcqxESq9ra9S1BMRbXHtPbMqQn_v7oEuBu3zy9GK1Vnq3H8gyQVCD05xpJKdJTOLirGpk3cFAM_V6mxzN9Ipkl9sPhO-u2JoDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
‏من المرجح أن تكون السفينة "شين وي يانغ" التي ترفع علم سنغافورة أول اختبار حقيقي لحصار أنصار الله البحري على السعودية، حيث أنها متجهة إلى ينبع.
‏يبدو أنها عطلت جهاز الإرسال والاستقبال الخاص بنظام التعرف الآلي (AIS)، ولم تظهر تحديثات الموقع منذ ما يقرب من ساعة.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/84463" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/84462" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAX7Pwk9wvIkCzGz6dM79rcuWcoqwcWpSRJ6FLyy4pDovrC3mrxHpvJoIC-nplyBACoB87n9Z2NwEB_KGqTjOvTzPa-x7Wk17BD8iW5gH2KKkRw9YJ7qWqxGDbd5K_B48APhX4Pg0n9a63bTou1M4RT5mEvdYvLmzxgmrGneEssNTKa4cp34VFrjWItTNZgMLMkQeTmjFDIh5L7FoKYu1Tihrm5VZQkjqZnk2fmUZ3KeG-HGXkNOx3tPoJfFzV_llV1H0jls2ymFKVcNgGZIhMidvOjCVo3wJTzrVbPEt-TaCLLe9YzGtruJOPgm-1g9hn5SirXoE2DvaHT_lmmUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامب:
لن يُعتقل بنيامين نتنياهو، بأي شكل من الأشكال، أثناء وجوده في الولايات المتحدة الأمريكية. إنه يُحارب الجمهورية الإسلامية الإيرانية، التي قتلت مؤخرًا 52 ألف متظاهر بريء، وأمضت السنوات الـ47 الماضية في قتل الجنود الأمريكيين وغيرهم. الوحيدون الذين يجب اعتقالهم هم من قادوا إيران إلى هذه الدوامة غير المسبوقة من الموت والدمار، وهو أمر كان ينبغي على الرؤساء السابقين معالجته منذ سنوات! الرئيس دونالد جيه. ترامب»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/84461" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
الأمم المتحدة:
تهديدات انصار الله باستهداف الملاحة البحرية قد تؤدي لتصعيد إقليمي أكبر.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84460" target="_blank">📅 20:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/84459" target="_blank">📅 20:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP1RyQvC15ICrs0IoI6sZnFFzr-6rCoA6Ypf8UAIDhddJUS_UhCb-PF-DY4PtQXx8nHnU3OUg3p9nx7L5BsWMYK-CqSA-HZNIUTwL9Zod89snQYId9rYAnBvtt88kB3sLQlBjxgWQ8Ei0Fu1Dv1IryHONtAJUaV2dS2s2pxMYGSOxsQgI3DbjItFjD326I6vaUbIqHmjgGf_TEqzLGCPDTaX4kMpMddUypbjRloHf9u4QGSNf6ZsMR1kmUGgzf584g5ag3vqxY7U8DRwyIxNVrtvXmOyWI1_j4EnMI3pV8Ryt51PxIefldA_NIndNpD58eWUBlxDvh0gXF6rQ5Ky_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كون العوز يفشل
ترامب كلما قتلت ايران جندي امريكا سوف يزداد دفعها الثمن .</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/84458" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
مصدر أمني لنايا
تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/84456" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IatWxGBkmFGKjcQ3fX0jvGtBh4e2aDG5R-uZQtD7zTO5EQQVw10852SUMvJkFdKriMrLMArvthf9nDe8p8nJsqjB_psfkeSoIMskLkRK6iJBChluYUdHRH37QSiy4S6teNUiw_iDrNr8SpEjgSUD5uy0p8TOUchsvXvggkXrPA5SM4KDj8U1G37fFud6CQ0IbhNODJIOe4OS3kenbVgc0-ZpEylC3iEdr675QYe0avCIyJMDIV9hPCJLon9HQ584wrKHunik1Mdifk2QmjMNwmJI7Gawbkm327BIFUYG4MQenO7Uo0puaDxH7JkDR1C7k8mhIB7onopr6WAKEKKspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
هيئة البحرية:
بلاغ عن واقعة على بعد 17 ميلا بحريا شرق دبا في الإمارت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/84455" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veGh7O8jN7_eUiqiGrLVg1BWi35FTaOl53wNQIHuj1NlXpsaYpDSUdBqS41Y2gN8IDJDEFIxt3frGCr9zVY3uhAyYK4kGf9ihklBvX5SevNgi-i7qzMegqjPJF8Y-tDwhzzMh0kqFFNg2HIL1b9hdgM70uuAjHpCWJAyLMEjTkMAJz1qwg7BWhHvdp33y5yb_imJsLBZRaOzhytFJtodoUZe-FWi7l8Jmys0uNhEGoghVPKBywDXKIck6pwAPBkuUiMNVVnA6_ZzUxSZ0X4A-QCmZvogsbJ1imhSzpJbXIfxPHjPPpR2KG78sWa6o3HrjAXtwX4_gtJqDpgwx1D0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84454" target="_blank">📅 19:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ فتاح ١١٠ البالستية يتبختر في سماء خليج فارس</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84453" target="_blank">📅 19:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1bbZxmrS1WZRduLt8TQVdazzqnUBWSP7rL3vuj8ITtvk9OSQIKxoWoBmZN0eLgPdEfOiY7vXMDZxuaSLG4_L-foNJCDlRvQYM6uK_cKXC9siA0oQDeiSxWoUyNVpwNgDL13bnO9-EaIs19lePZ5FnSu5OjZ1t71HC3gb2VA5vqZ6WvUzS1tzWsMHO7GAL0VrmNZxb6Iah3ICAICSZOk8ryPMWVP7HsBr5BPoXigSkEDOC6keRnjKEl_4EsWbYC9sFjTE7MycO4jc-J3wRnCWfgYljLBe8Z5ratDXAbwNzOHnxbtxJGcZVfneC55n8c-mO49lQ2ZPCGcpUod0X1T4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية إيرانية اتجاه القواعد الأميركية في غرب اسيا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84452" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">واحد معطب السرفة و واحد معطب الهمر
#شاركها</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84451" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a526d078.mp4?token=g9RmrZSZzMN5km6LhAExW8ojAmhiAxoKEUW3DEcPHSq0Y8LiLSE-COAIGHwFjCJ5EwmvHawvMX67EBS877A_oujLGkmbfv3cUaj3UlSIJ9JqDwXKHvv6ogK6AcjxIkE9LISTU1ZqCoh1puD6F4rmzmJqRR2Qmjd3qRKK7lRafe_E-gc8wqGIic50zvbt-z4rtBrsVfpeUMK0lu3vu1bGR6bkOW8JLAe3O2HVYnANtnD4HYCNp7SOQX62iNqdJwnClqChMqFbwNHWMKYkiSkBvLbV-LTDSDvb5G-NZTmlp3HCY41GtcHuCwyvArciPsXqfuLOhdhHcu_RvezPjmkbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a526d078.mp4?token=g9RmrZSZzMN5km6LhAExW8ojAmhiAxoKEUW3DEcPHSq0Y8LiLSE-COAIGHwFjCJ5EwmvHawvMX67EBS877A_oujLGkmbfv3cUaj3UlSIJ9JqDwXKHvv6ogK6AcjxIkE9LISTU1ZqCoh1puD6F4rmzmJqRR2Qmjd3qRKK7lRafe_E-gc8wqGIic50zvbt-z4rtBrsVfpeUMK0lu3vu1bGR6bkOW8JLAe3O2HVYnANtnD4HYCNp7SOQX62iNqdJwnClqChMqFbwNHWMKYkiSkBvLbV-LTDSDvb5G-NZTmlp3HCY41GtcHuCwyvArciPsXqfuLOhdhHcu_RvezPjmkbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية إيرانية اتجاه القواعد الأميركية في غرب اسيا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84450" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رشقة صاروخية من ايران باتجاه البحرين الان</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84449" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتيجة الهجمات الإيرانية ؛ شركة شيفرون الأمريكية تعلن إيقاف إنتاج النفط في منصة بترونيوس.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84448" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84447" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84446" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/84446" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3d0d6c4d.mp4?token=sg4aQLmqWlPzoXr43DqVfJWB4eq9wO_aGB-Alf-lXorYaoOUwuncUCGV-GvADQaBkS8Rj_Fdk-WXBmaPJ5CFt96kBoh1A5UIZyLbW2HyL4MRfc6PTLC9y_gwS-UEF1n2VlzPTDLihiwefmO9j2NZVOQzEKqaGLScbuabDxHmrf4cb2MtjeBSmzMnndqI0lDGh0WHQHvAfYa6cdLWXGCjidgt4F4ZrsUG3G6UdFEiVoJNhkNQUDOvNBMuE4JdO1p3DZ7ytsGF7HZubeIx_SF8UaoIEaOn9JCkzVv51Pvjdk31u9ge_zAvJNSxYyBzwDRo6HgXcd9Wk9OdnUgLTBZPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3d0d6c4d.mp4?token=sg4aQLmqWlPzoXr43DqVfJWB4eq9wO_aGB-Alf-lXorYaoOUwuncUCGV-GvADQaBkS8Rj_Fdk-WXBmaPJ5CFt96kBoh1A5UIZyLbW2HyL4MRfc6PTLC9y_gwS-UEF1n2VlzPTDLihiwefmO9j2NZVOQzEKqaGLScbuabDxHmrf4cb2MtjeBSmzMnndqI0lDGh0WHQHvAfYa6cdLWXGCjidgt4F4ZrsUG3G6UdFEiVoJNhkNQUDOvNBMuE4JdO1p3DZ7ytsGF7HZubeIx_SF8UaoIEaOn9JCkzVv51Pvjdk31u9ge_zAvJNSxYyBzwDRo6HgXcd9Wk9OdnUgLTBZPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
أنصار الله في اليمن تتصل الآن بالسفن المتجهة إلى السعودية عبر راديو VHF، وتطلب منها العودة في إطار سعيها لفرض الحصار المعلن، وتحذر من إمكانية اتخاذ إجراء عسكري في حال تجاهل أوامرها.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84445" target="_blank">📅 18:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🔵
أفاد وزير الخارجية الفرنسي بارو أن اثنين من مسؤولي السفارة تعرضا لترهيب خطير من قبل أجهزة الأمن الإيرانية يوم الأحد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84444" target="_blank">📅 18:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0y7K4K0S_2hxFmUDHNQFYhzpPv8kAhEt9HqIky38sFJTTCdCXmamQ39Vn7tn7-CZkvMhobl6fjnIZ-BVS7Ka8iSWVaJCxPA-2owBx-2YEEZejoOxcKdPgEo7w1bWcn4NZak6vkddFGNSxmxZOWBp5H5zRkpgRjyqn7elEeAwJz4jKU9b_haEr6eJjHHxO5h_p_GHQsRzPmMTGoRx8QFM9FqxRcpOYgm2S3fKSfVUv_adh5bz9Qbc-gT177Na0CZ0R1PeWCyYY42QnMu6jccFzBi6d-Ea-VsUKzW-XMfCUKb4h2L6-DDMwLMTep3obWvHlxNe3eN-beojh4AtAnrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇭
استمرار الانفجارات في قاعدة اسطول الخامس بالبحرين</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84443" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2AA6ergXaNZGbyB4x1W4nEYeP8PRVvdbJLrAYMtTr3k5ceAEJzPQnZg6ueL5Fa9ATB_slEoGNe_t6Fcja6kUffY9BHqR1hOLaPGlBcaqc3z7Njj8bIOuhgt9KnXTpwaRv5uMBM7NarHk3pfe8xLgJAnvpibxDNpBGF6jvAHn_UTxkPD2qe65b5pwfxT7aBdvcCBY0uuQCbNQWqp5PAabdq9q8Q8Mu3Urx202vr1N8qGaHHbTLuoK31jBByLjTX2Sz6c5NwGhrDJEp2HIJK06Z2nvD7DwZwz7F6_CeU-2Z4qSibCxRGNCnUov1OEOj4P67rKauXqAGHbJ5ryLr4gYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
🔻
This could happen when you choice wrong president that he work for Israel not for America
Tyler James Feehan another solider in US army who die in Jorden due to IRGC missiles before 2 days</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84442" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252853cc5a.mp4?token=PmZ1RRxhrtOXkRl00HAuQ7Up_8DQmndZ54cT0jekzTWn6sC1OeqBxqvc_J1GZ9h5HhgfTSst5gAQs0mkviy_NBAirC_rN3RE3muU1NatMNFw-Bz5uMX0JYw3p43B8opABCxzEILrqzla3o89etVKLZxAfjo_P1yhASgkHbxd-eIYUpNr9uG3x-rlB5lLSojLnkIjBS1fHotzcrCx5_QuPc7rDKF86K7b-nHyQ75av-Y84MRQjTfi92JCCC64NPcy-1I-vlE55moew5S_xD9Oj9ihc7j6TAXYP_rfHpq0RsMz3lkCiT5BqPmjUGenSEAqt-kyo6mdASrlycJb7VcE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252853cc5a.mp4?token=PmZ1RRxhrtOXkRl00HAuQ7Up_8DQmndZ54cT0jekzTWn6sC1OeqBxqvc_J1GZ9h5HhgfTSst5gAQs0mkviy_NBAirC_rN3RE3muU1NatMNFw-Bz5uMX0JYw3p43B8opABCxzEILrqzla3o89etVKLZxAfjo_P1yhASgkHbxd-eIYUpNr9uG3x-rlB5lLSojLnkIjBS1fHotzcrCx5_QuPc7rDKF86K7b-nHyQ75av-Y84MRQjTfi92JCCC64NPcy-1I-vlE55moew5S_xD9Oj9ihc7j6TAXYP_rfHpq0RsMz3lkCiT5BqPmjUGenSEAqt-kyo6mdASrlycJb7VcE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد بالأقمار الصناعية تُظهر تدمير أربع حضائر بشكل كامل جراء استهدافها بطائرة مسيّرة من طراز شاهد 136 في قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84441" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5aec97ad.mp4?token=HJ_KVnftmdB2xnJl4CXs1cyAfu3wOeYX8iImJQA0zXVsQN3XG7nO6gjqR7ZU8LzN5kgwpRJLVaRbhVDTbzNrx9e3kDSLt6kYnSgT41qFrOk8dsBm9RqPPgz_uYneCrR2Vaq9j9BEFP-cqL0qiyZ7PytmRnnoIe_FuohW4q9tN4s1hEGrF_u4YhNBB0DlbzRg68vKiQim9sbMaoGEkrLDLE944IxHuKMPkCIpYqq-9-fv-qiT2tYWFz1F7AjAVjoRo9us8KYMJfcgNugPs-aCxW7VwaicduzdMoSuguO0mEDXh_rHDmEbxm-10aF-v7WB9LkVGHIMmQ2boRnDzFy4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5aec97ad.mp4?token=HJ_KVnftmdB2xnJl4CXs1cyAfu3wOeYX8iImJQA0zXVsQN3XG7nO6gjqR7ZU8LzN5kgwpRJLVaRbhVDTbzNrx9e3kDSLt6kYnSgT41qFrOk8dsBm9RqPPgz_uYneCrR2Vaq9j9BEFP-cqL0qiyZ7PytmRnnoIe_FuohW4q9tN4s1hEGrF_u4YhNBB0DlbzRg68vKiQim9sbMaoGEkrLDLE944IxHuKMPkCIpYqq-9-fv-qiT2tYWFz1F7AjAVjoRo9us8KYMJfcgNugPs-aCxW7VwaicduzdMoSuguO0mEDXh_rHDmEbxm-10aF-v7WB9LkVGHIMmQ2boRnDzFy4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
الانفجارات مستمرة في قاعدة الاسطول الخامس الاميركي بدولة البحرين.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84440" target="_blank">📅 18:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7ed8l_z4Y6YdFXvrS6aDZuiouxrxmhdI1cG7llz8ZIaUOBv7xsxqm4V-kBuICmqIttPBHjrIkHfifpo98OV7iGrrVSadb3ykn1Uxw4i00K_Ru6Gzjgdskxfq90cmQ1-MGAkEwv03aUlfDoRYgGz4OzumVF77lnR-bxPGBs4t6OlNwxZpGMJvSEgpP_FMDgCjp42ibrorf3OSF-TKzu7-LdMLkbKT92M2SJquWAPlhsvMGhmhnEgSZHGacRxfixoCmROLEt0kOBZ5G83cFCx6INBoCIO17VDyQfMj52OBRgC-cticuKzoB6qN4992Bb7BvpZX73KTOm0y9plblRkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq4ynD_4Cr3xnuo0pRDwugTIVFmuCSKEj26LuL5UC3cmmRa6FmmQq-py9uHitWnpQF1haXSmxC1I6yaC7oZk-PX0xc6JhdpUCH-kxgM8EbH-vxd9eqbLtnsTSiGnG1tIeRNzHwW4M3Ttai5FfibKifpP9UbgA_8KiEdN3TMQP8LAeqOyO7x-Mbw5TyokDSSa2uAqiQO_2bjOtx-kyUGuVI9VTw6HjM00BvMW1AoLURB7wmJSqOdGCP1Ct9YVUkBYynrGG7RW15YE04D-Uw3_4QmgBAnyRsjaWzUqf37uY9UUZtj0so88DJ1AozcUaZLBGOZrwhK-qK6VJW3TEP1fBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇭
استمرار اطلاق الدفاعات الجوية تجاه الصواريخ الايرانية في البحرين</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84438" target="_blank">📅 18:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d83612b8.mp4?token=WOC5_OHtkG1NMXjQjyVRRhZ6XPIfmo_weKcMaMuLK6irqR5BeBBgmV_O2OghMEe06pIBlay2hLafATfDJWeK4ivfleMSX3g10idl8t1BYTjZBFF7pnxpYip_SbAltObBw2Kr8Qf7VNh09af_anY-fqdOt5CaN5Zh5bEiNu0i8Ni0CyjnW7gZbSwUTcsbL4C8bZucq7b9wq3FAavrfYbHPw30Nr-F3dRXVn2sjWNyZkFl8ivZSpFSuBmvzVf81TGMChVNFp228b76nE-gj3o4i1O3KMciG9-XGE4x2cvRBwqJOWUkXTtlGOwI7QEpif8SBKUXp1UexP5LSOVI5GsSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d83612b8.mp4?token=WOC5_OHtkG1NMXjQjyVRRhZ6XPIfmo_weKcMaMuLK6irqR5BeBBgmV_O2OghMEe06pIBlay2hLafATfDJWeK4ivfleMSX3g10idl8t1BYTjZBFF7pnxpYip_SbAltObBw2Kr8Qf7VNh09af_anY-fqdOt5CaN5Zh5bEiNu0i8Ni0CyjnW7gZbSwUTcsbL4C8bZucq7b9wq3FAavrfYbHPw30Nr-F3dRXVn2sjWNyZkFl8ivZSpFSuBmvzVf81TGMChVNFp228b76nE-gj3o4i1O3KMciG9-XGE4x2cvRBwqJOWUkXTtlGOwI7QEpif8SBKUXp1UexP5LSOVI5GsSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
معارك جوية بين صواريخ الايرانية وصواريخ الدفاعات الجوية الاميركية في البحرين</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84436" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT_7i6iZEtKKncdJHzTx4KHZAdg9AP5POnYw1hkhqF9Vx_5IB5eqk2sIKmu70FgDj1tvjUeOaYnFrzpGC5rE8boGANtHPlCeESagGNC9ISmSLLU0XkxiEYDeuH4RV5OzFqESXpkVnWEpNaIsdx1T-5zw1XATxsMjdg7QT8xB91y1rBTtn4ShjQ9-m30NZ0552Op3a0vRJknZEffr33NiYEl9X16Vaj4CY1z5sHS9L0zI75uSv4LwD7lI9cMdID_ZN8SuNG0UjrYalq2QD2KkIke7MD9CCInd50wBHZI1Efa6XLZ1kDHujXmhkASt_6RR7n9DQFYaggxWe3edX9ekOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل منظومة الباتريوت الامريكية في مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84435" target="_blank">📅 18:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📰
‏
أكسيوس:
انسحاب الجيش الإسرائيلي من "المناطق التجريبية" في جنوب لبنان سيبدأ غدا الثلاثاء.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84434" target="_blank">📅 18:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84433" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84432" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84431" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS9jT1pn0Ikrz3NCnY6flALx7SH6oeySRjlXsknkd-Cd_vEkdDVVAO-usj7OuaCLPEix3K_m0PSqBpGqxUV9ijyuvj6XjNYWSOQ95nYsXcEKUndZw-ImK12qpKBNIX50Ib2iAotCV1E7EFb_bIhhEkBing1YCt2j07UGDZCRTS8dD9F6CXciv46iC7xBqfbutzvzkIWbdBDZ9qhU0y4Tb_3AT784ymhr3zVNptL2Rk2IqkCu5W-ZbVomDlr3aYFcyGEaG3Z_3GsE3Cm8pCJ-1LHA1mzDSlNcoYGWgIpk4tODHkLtZhvheNx90CIf8ZnBYFlGEAZNNwJDaQQUpvJN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpRr1vRo3VXMgkzhhRzODYy774gTRwp-N5MjATi70sO2h7iMy4wfUGMWyRufX_htbF5CKGSak-cQeDvX6kOaYzE2zFN1eivy1wA1DjyT4KGfN5DIZSpo0E_NbDZAIaFpUVbK7eCaoOUfTBWeP33Aa1y2mYBWI09CUerfgjSgWTncKElA86bzVsuoF-pYRCvxrShJQDMRnsZRGCoFAX6krlLsXS4urwNA5Ls_sDbgRIE7UlB_JZRSBTbyvs68ep4_4uiygG7GS1_-objg4v4aYllHaDXZl5iWWFg5JPomxxovl5fbW-9UNdzBOFiyZkXfLyvY5qcQjCNujR9VeEK_qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان امريكي على مدينة شيراز الايرانية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84429" target="_blank">📅 17:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استهداف سفينة شحن يونانية قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84428" target="_blank">📅 17:24 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
