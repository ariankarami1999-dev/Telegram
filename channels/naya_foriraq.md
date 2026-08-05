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
<img src="https://cdn4.telesco.pe/file/bpdICK3Vn72c9XrO51ro5gZI_SDxzBcsvfIsb_aZsNM1pJkXoZa_Zuma_NzyfF_dfaGlQuLSQOJUY3EHR_RSECY43tjUM53j0Z5Tt6Y3A65AvIbLPgGuYenmJCj7HKW03B3rK_CqVLeCZcgu-JjDjxFE9JvZ8LgYrEdsjPwYzTsWVDWZvOlvste4zMe76-iDXGwB3G2S8BPKLVlhINi9O6e-9xdWzUqtwEVoOJOQXnZioYjilJfR4EovTphuIalVAs-lEjkwu-M98weAi_y_XodsRhGnbePNI7kCmKjIFzb98ZH85vT92rZbolRW-ait7B8SeHjr5PeWYR3Latix4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 23:32:41</div>
<hr>

<div class="tg-post" id="msg-87058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية: نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/87058" target="_blank">📅 23:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية:
نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/87057" target="_blank">📅 23:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRVI7WtAB3GVrhtL0VHkWJQu4e2jS2abjYoBcOsu9mu7MgHtl8w8HZGz8ex5jSez-nMzagtZEGQm9RXtr5BjBzrCJyejiNbRdzZYb6X_8rhW1qUWO9L5r9XsIohJJ-pMVAI1yR3g7l9ADiK_u0f8U9eiRC_kQOEPcTfMzZEgSo7Xg7oobcDWRuPVkYiHNFUCT7xojrOY-i8tj5UrHNKCSQqL8AhVMBJ9i5W1-K3LFam1qXWrWp_wZEQI0aqDGCDDqQx22l9Tca84RG-5TWPucXk07Fs9i_Y8DaTphAdN1FMonwID0WqDypS9zlp7PJESQwB_AeKtbrgd9Y7BIXuxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع: تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.  يأتي هذا الاستهداف…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87056" target="_blank">📅 22:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع:
تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.
يأتي هذا الاستهداف في إطار فرض قرار حظر الملاحة البحرية على العدو السعودي وفق معادلة "الحصار بالحصار".
تؤكد القوات المسلحة اليمنية أنها ترصد بدقة كل تحركات السفن السعودية النفطية ولن تسمح بمرور أي سفينة سواء من جنوب البحر الأحمر أو من شماله حتى تتم تلبية مطالب شعبنا المحقة ويرفع الحصار عنه.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87055" target="_blank">📅 21:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87053">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCxcR06TEeWPnB-5XBNGtRFthwDktQRQ7wkT3S_54f5_BqCuSOnsJT52zLpM-6AUxyzwhOKlR2Lez_GZ0LBUS_8PadkiVGUK48Tz0k-ofCIvTEZjOSNgnrxpI48DUG7UXOVtXU3HjWmwSqwgxjAy60NI7ZIVA4uKQ0fMofBnc26bJ3ViYNpeHKy3LWAjn-Okh5U7g_g2gv9eEcZxTTYjY7rL10KYwdZCQbJmwQLdM6m3PbEPNd54Cj7e52NMOtst-xS30GaQ0KmQ2aO3Zw8mVfbkGTjNnS14P4LejhKD8ypxOxJz8Lx7As2Rve8KiDzdBv-VJ8r4Gxuj5DyjtvmhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87053" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87052">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87052" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87051">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين: البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87051" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87050">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين:
البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87050" target="_blank">📅 19:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87049">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzjeh3dml2QRWiCqdOx_OD8Uf7_x1BWLX04-5bnHD2bm4Xom7xS18mnFH3u_esbzo6hoxWkvXBF19_oeQOgJiE5Y_VKtG7x-yWDisryVeNLffMINjaSYkgO4Y5kG0ltIVfy4tHWtUyuKqYbCS269jDHPSns9IPgP4Mo4jX7wAbZc1ushQ0a1IdirKPR-UVM2_bg9uUUM37Svua6-Yt-FPY8FuPlds8e8BpeSN26SBTXbwV4NdJ6c_2SD3NACuU01A4j_uEcII9Vrticjp-rpYuT2kIYfVEWeNXphXUeJX4sTm0RheMZh8NKOMH-8hVfFx--JG589YGvA4XPFDiGOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
بعض أهالي سهل نينوى بمحافظة نينوى شمالي العراق تلقوا هذه الرسالة وهي تتعلق بالابتعاد عن الاحداثية التي تتضمن موقع الفوج نفسه الذي تعرّض سابقًا للاعتداء من قبل العدو السعودي ما أدى إلى استشهاد 10 من منتسبيه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87049" target="_blank">📅 19:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87048">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhSgy4RBwisWCpQumnFNIHXUUKoUVIP1vr2nucAxHSOBiVoDOz9JadlDXS_muDA4krp9keGXgOuspg7UwMbsFgfH0Yq8PUcYEKj3CqwshYXbIqYR5_vtCkOuLi0zsjerYuiiOdTADRsY21gqEOQ4lYh4d9eSHRetjWGGwE8ucztJkE8VKz5rO7EH9e0NkCCZitaR1u3K_LeIR6ZBXL1lGCa_owL_w2YiTH4m8EpcXd98QNpvTL_TrwFwfqFk02HFtNxx2OQ5JXKb0B_LMUQn5L4YnIqy7Zc8X6YEUNTvDydsIZYDgS6COmOw27Y9z32TmHqBEyKTfwzYAQ_kh12bBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
الاعلام العبري
اطلاق صاروخ اعتراضي في اشدود نتيجة تجربة للدفاعات الجوية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87048" target="_blank">📅 18:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87047">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
تم الاتفاق مع عُمان على الخصائص الجغرافية للمسار الملاحي في هرمز.
وهذا لا يعني ان المضيق آمناً لعبور السفن، لأن العوامل التي تجعل مضيق هرمز غير آمن من قبل الولايات المتحدة، ولا سيما الحصار البحري وغيره من الأعمال العدوانية والتهديدية ضد إيران ومصالحها، لا تزال قائمة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87047" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87046">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعلام العدو: قتيلين كحصيلة اولية في الحدث الامني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87046" target="_blank">📅 18:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87045">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
الاتحاد العراقي لكرة القدم:
تجديد عقد غراهام أرنولد لـ7 أشهر لقيادة المنتخب العراقي في بطولتي الخليج وأمم آسيا.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87045" target="_blank">📅 18:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87044">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
نتن ياهو:
ترامب صديق جيد جدًا لنا، ونحن نقدر الجهود المبذولة لمواجهة طموحات إيران ولكن وجود إسرائيل لا يمكن مناقشته.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87044" target="_blank">📅 18:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87043">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
تنفي هيئة الحشد الشعبي ما تم تداوله عبر بعض منصات التواصل الاجتماعي بشأن وقوع اشتباكٍ مسلح بين قوات الحشد الشعبي وأي قوة أخرى في مدينة سامراء المقدسة، وتؤكد أن هذه الادعاءات عارية عن الصحة، ولا تستند إلى أي وقائع ميدانية.
وتدعو الهيئة إلى توخي الدقة في نقل المعلومات، واعتماد المصادر الرسمية، وعدم الانجرار وراء الشائعات والأخبار غير الموثقة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87043" target="_blank">📅 18:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87042">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الخزانة الامريكية ترفع العقوبات عن شركة فلاي بغداد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87042" target="_blank">📅 18:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87041">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87041" target="_blank">📅 17:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87040">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📰
وكالة رويترز:
صادرات النفط الخام السعودي من ينبع انخفضت إلى أقل من 3 ملايين برميل يومياً بعد هجمات الحوثيين، بانخفاض قدره 0.8 مليون برميل يومياً. وكان إجمالي صادرات النفط الخام السعودي يبلغ حوالي 4.5 مليون برميل يومياً لشهر يوليو/تموز قبل هجمات 26 يوليو/تموز.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87040" target="_blank">📅 17:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeUSwTtSqNtlb2SHXEQY7hCIF2q5gZd9OYMDvVeod-VwFsWFC5GgnBIhrBN8y3ovqamrmXkMVwJFN3wUJa0ga2iwg0mv7gZullC0_-nNaQ1s1pRFaBQ6EgYaRRVcdxutct-J54JnSAS_IvdW5RRPXBnSzgpdtLdFMzFxwJOxIfhpXCC1vvi80NZNX6hoGkkqgc5-hvPFPUP3bIX4pS3PIoP9udZLe7JwjXwk3TMOVMDLP9AuWSYnZsiV2l71NcF6jeq77gyIpvqaL5nCFI_PArm2fXC8PIjmfJfLXrEoX1LFDPG3TdOWPNDyIwYejSIF4H8xO3AhXZ3pE6JCycTl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: خبر رائع للحزب الجمهوري. السيد، الخاسر الشيوعي الذي يكره اليهود وإسرائيل، هو الفائز المتوقع في سباقه مع الاشتراكية. وكالعادة، كانت استطلاعات الرأي خاطئة تمامًا في هذه الحالة. لم يكن متوقعًا أن تحقق أداءً جيدًا كما فعلت. الآن، ستزداد سياسات الديمقراطيين المجنونة سوءًا!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87039" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87038" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي
🇦🇪
السلطات الاماراتية تقول ان ما حدث فجر اليوم في دبي هو حريق داخل ورشة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87037" target="_blank">📅 16:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جيش الاحتلال: البدء بتنفيذ غارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87036" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87035" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شركة يورو وينجز للطيران تعلق رحلاتها الى مطار اربيل الدولي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87034" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0b8FTmszqKdeeCuns-itL_-MXVRiJZJ8N24HxPAE0mTHT4WD9kQHWBgR-5DqfILuWG6Zq26l5DkQ1JTTaFTnAMOfcYNRp6809Hhily5YYPXZmsNzBNjayekL5EUwILgc8_d3t0JDH-qSPK8rlf8Dv-7afOyM6QBk_qFf7paSGOLtzh7wZMbRW3M3ackw8zspU4-RO_IxtioYgZIWzp6mKu4eC0w2RaeMOh5We8cbpQAbtksfl3_yjEsnh2vKCK-ghEXI9VgMhYYqQQHCevDej3F_J1PR5MX3Gkg5F6UDNtNJ8NN2yGzHdFXrcgraKI8RFTQk46jRccT03w6d9HHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87033" target="_blank">📅 16:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxeMvMZE2lROscW2cK5Q3RdSn5Z1tLIwGNf25yepPRNa8f3n143_Oulp9-8vmC55HFPxBTziOqZCJ3V-fozKJPmB7EA14Awb0DTcb4eWratgvicDsg_Rm8DPx7jEnIkOWtoVmQwHkNeSzQDQN8ONGwNKVHCIH4MsRn0Q8c-E45IyXS41T1pQYh3EdeZRuPlh4ttoDrCfGaCrS0eGqYjpRg0adk5_D-3aLXwC-hCWJD5O86PvqroM1BpxDXYEC-r9KJ_QRoA-X1TwjkDkQiaPYUHt0otzWdYLqJJnuRLqFToOPEq_afRXGsxAtlXkoiyBTL_Avvp7JyVNolfxOV2iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87032" target="_blank">📅 15:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87031" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=l5H-MuROq6N-wpN_A5tY1MpWVsdq2xrbd5C8P4bYnnXFPRqdnzhRkSszE5c67dvsS5CqJagXdNaxpjBGRH_Kkcoc7e3VQvzp_NlBA8yEP400Y0xFtrAdMI3be8ELNOG-FF2GM-9EF0jQx5nk9nfIZjUugVeZmBDRi-rUGABkHaI2kdD3H00DNT2n7xa1d6xJRZhYD70_5-_lzuIbBS4cNP0ZS5FAVbLSfB9e8oHU6mtSZCd-_QnQnuviYn8podUwXr6qF6WFyI1p_ka73xPG7bP6RGsPCQYK0ILBzoptnqAkCC6nWU2Oa7tqw7H1uLVqCXw_xLOWp03nfJrAAFumGrfgYHMvClxjHlHFycB7HONiQ04xD2oIOFzLB2leKvxRE4Mp2ZgdHs9-O7h0RMKoCUm_QQM1f0DwGXPmzl0cXnPTy4IEpwENLMegq1-vd7hh5cnS9V5AysVLZpY-YG2LEerAoOlkRlVlRLPIAm4td0uWHlJb5k9igFUYF_bgKQLnEQvePX1O91BlWScoH_W7ISJ_KPpc_upYAG3gny53_EQzgSFreiAqF_gWwvwEsFreysq5sq8cDcmuLX1-l1mMatm5udgEPZnpLCXbtrMAYeRgKYCvYhw1J1tNjjxrNuTRk2Vrf3dBco-sxEmdCLv4VklFDOGBYyrx3IMUJ_MTMzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=l5H-MuROq6N-wpN_A5tY1MpWVsdq2xrbd5C8P4bYnnXFPRqdnzhRkSszE5c67dvsS5CqJagXdNaxpjBGRH_Kkcoc7e3VQvzp_NlBA8yEP400Y0xFtrAdMI3be8ELNOG-FF2GM-9EF0jQx5nk9nfIZjUugVeZmBDRi-rUGABkHaI2kdD3H00DNT2n7xa1d6xJRZhYD70_5-_lzuIbBS4cNP0ZS5FAVbLSfB9e8oHU6mtSZCd-_QnQnuviYn8podUwXr6qF6WFyI1p_ka73xPG7bP6RGsPCQYK0ILBzoptnqAkCC6nWU2Oa7tqw7H1uLVqCXw_xLOWp03nfJrAAFumGrfgYHMvClxjHlHFycB7HONiQ04xD2oIOFzLB2leKvxRE4Mp2ZgdHs9-O7h0RMKoCUm_QQM1f0DwGXPmzl0cXnPTy4IEpwENLMegq1-vd7hh5cnS9V5AysVLZpY-YG2LEerAoOlkRlVlRLPIAm4td0uWHlJb5k9igFUYF_bgKQLnEQvePX1O91BlWScoH_W7ISJ_KPpc_upYAG3gny53_EQzgSFreiAqF_gWwvwEsFreysq5sq8cDcmuLX1-l1mMatm5udgEPZnpLCXbtrMAYeRgKYCvYhw1J1tNjjxrNuTRk2Vrf3dBco-sxEmdCLv4VklFDOGBYyrx3IMUJ_MTMzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في اجواء محافظة المثنى جنوبي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87030" target="_blank">📅 15:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Diq60D1m_m4QqLpbCWH8hlpMJx3RLVqgLdvlxVAwmUzdvm6iAGes4h4LKGrQCvvHnY7Gn1b7Z1UefU_pvjp8JXxJPVCeGhaTpH-WyFedQCwFRnx46QRy-dh_4Kx-p6IpDjHC33LaHEYvdUI7CnffnYOnvHbuwTuxrSncdmQtT-LwkC72o5Xusl-jBCQzT0kAEpb0V9oVP6hdmeePTesApemGmkf6FnM9lm1rWTiVRNYbjdrV5WN-idDVjb3qxb3boKplYmujnT-oILL0CmMCsuLJJYcjZbhlT0KlS11OFqXSDQ2mvIhSmB_vYQV1FFHPc8N1QdYNz90hZIQQroQIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
تيمّنًا بالسيد مجتبى الخامنئي..
مواطن عراقي يختار اسم "مجتبى علي" لمولوده الجديد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87029" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">غرق سفينة امام السواحل اليمنية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87028" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldBM0Mq7erprj_UDspt_CsNNu8LAr_WYN4uuIQFmqUZT-JCoJwxsuD6_i9q_BHWg0kdfijt0X8VYJCkXpOnUp_8irgIm88ZZtOI7ceq4pYp-QVF2JlKVK_5vHUofgk0AfxNKThK9g2J_fTnBGF8M8cj7kfGWalchfxDlmIkti-P3VZM5Qbpbtsjb6M5hPHYbQ7_ilZ3XKkIYNnXoBME5Nc37FB0eesDLQKyOZPJqifJLtqMt-uKB39NVr31_q_Zi_iQS_VgR-e8A1gmQ1FySg4kxoD-s_U3jzYCr3OZPtg4pbYPCq52l4jl0ZXKBb6-AcArc4HtKjhHESEd2N6nBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87027" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87026" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87025" target="_blank">📅 15:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVNbMaEtADqY-BX4qWc1Flp6Bg9Z1dT008qacmYz5wMUnWAHDItOJ30UTtXHi_apNtYVBMNGnWIMsNNLGNObp39T1hBEBJFFQ8zATqgF1LcLRL6Mi31m2nnkdy7qy7HzAMa6-l7ODLesX3bvDCXGI-RAjlZbF4IbQI0w88R_sZ0pY8heZ4Y08w2Xrifs3pwAss48zlgKashQ8KcyxU9noKBCfYsmM96u8syxZoMWze5CWz7rQuefwlUhMQZ5bO-7LwqC04_ZRRRxXKioUYmAMx30aANSen5IwCo5jKmrD4NxEP_Y-oJsAXA6eWgDF_GR47BdzrzMAlFoxtny68hqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw7pp8RQR3rmfWC79kW8R0IRtTtHZtF683saztHOLy2HMsV2niuPyIc8n8WC7GehIJVHSYavBvT9cRBiEZtvlKXfZ936sTUO5gnBOhQ3PGl0p3Ac0syaCKT4FSX0sm0tqDRr4afta2udEHl8hiTd9dnQep6_rjHMf0WzwgkstAz69RbpB6UMmYLdxzCYVRqzdV2INTJK5KvwrwJ1VeodmaXn4iugdvSXMuyV9umFN-a72vs29CBhU-P9FDo2I8tjFnaqvwO-TOfd_X91z1w5XiaL7dVN4Ggwlf1ihIhUIGug7d6jMGSQjuCCr78S85xUuEIQoConYy67_T_TnkBFXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
شبكة الإعلام العراقي تفتح تحقيق مع الموظفة "مينا أمير جواد" على خلفية نشرها مقطع فيديو يسيء لزوار الأربعينية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87023" target="_blank">📅 15:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
🇺🇸
ترامب للامريكيين الغاضبين من ارتفاع اسعار الوقود:
وضعنا الاقتصادي ليس سيء.. سينخفض سعر البنزين إلى حوالي 2.50 دولارًا للجالون في حال التوصل إلى اتفاق مع جمهورية ايران الاسلامية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87022" target="_blank">📅 15:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حرائق وأعمدة دخان واسعة تملأ سماء المدينة الصناعية في جبل علي الإماراتية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87021" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزير الخارجية العراقي ونظيره المصري يبحثان أهمية مشروع مد أنبوب النفط إلى العقبة
احلب يا طويل العمر
راحت النفطات</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87020" target="_blank">📅 14:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrkAbnIDPCE_QNx9xFllPsxdeI063ZMZee94ke-AKYjDvNgZa8U4oDC9cPTnLL-vYOsvlz-dBrS0FhE5XhSxALQ7RalSvoY5f1jP1DpqPAGYY1nDzJrRRxixNyyhbPD9LPaL8Hi7_wxhKZPSpMcFWyUUHnQVp3zs6V2XbL7ui70CBrwCcf7zAbsN6yS-XsLsjdoMJBPrjTmRutDUDkhbW6oGgNPJ4nbH0NvNYPtzoqfGuhQLRuPgQQe4PTYkN-jBDNhyqQ7DJl_JO6RrVUb0qLORgMDoGSb3eTrZQkS1jwge7G6-rvsvjMl90xqMNJf4iW7_OH2_ICjTMycgCynLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
اصابة فلاديمير تكاتشوك رئيس الشركة الروسية المصنعة للطائرات المسيرة FPV بجروح خطيرة وادخاله العناية المركزة بعد محاولة اغتيال بالقرب من يكاترينبورغ حيث ‏انفجرت عبوة ناسفة مزروعة أسفل سيارته المرسيدس مما أدى إلى تدمير السيارة ومقتل سائقه.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87019" target="_blank">📅 14:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوي انفجارات في محافظة اللاذقية السورية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87018" target="_blank">📅 14:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعلام العدو: من المحتمل وجود قتلى بين الجنود.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87017" target="_blank">📅 14:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87016" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=RXEV156wqZxrNptGCB29VdVSTeGaJAQABZQRrsjh3zsxSldFh0BNLw3wQ4CuoVY6L-PcvWPU9ku_fDTu131HK4YcGdbHQWo5NPa-2yAmMhTt7knWKtfi-61S9Z0qFbf7QySEuSD4i48Cu8iiNee1-MxCAukwYR72gwj09FgEL2aA0wdp9vlcJvgIfh0n403nHlEP2_bg8NTyl4uz8_7vXhPb0YEQNYliXH56-AINghS8_aNwavkD8PFCcrbjyvAljpgM0iKF9RbeWAdHnTNdwU7IXt2S8bY3dp4CZn33dzpsUcJnplp-32CFP_yfsRxO8770sHB-a-5mQLbLbnLmfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=RXEV156wqZxrNptGCB29VdVSTeGaJAQABZQRrsjh3zsxSldFh0BNLw3wQ4CuoVY6L-PcvWPU9ku_fDTu131HK4YcGdbHQWo5NPa-2yAmMhTt7knWKtfi-61S9Z0qFbf7QySEuSD4i48Cu8iiNee1-MxCAukwYR72gwj09FgEL2aA0wdp9vlcJvgIfh0n403nHlEP2_bg8NTyl4uz8_7vXhPb0YEQNYliXH56-AINghS8_aNwavkD8PFCcrbjyvAljpgM0iKF9RbeWAdHnTNdwU7IXt2S8bY3dp4CZn33dzpsUcJnplp-32CFP_yfsRxO8770sHB-a-5mQLbLbnLmfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87015" target="_blank">📅 13:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">إقليم كردستان يقرر احتساب كل سنة من خدمة عناصر ميليشيات البيشمركة بسنتين ويشمل هذا القرار جميع سنوات الخدمة الممتدة من عام 1960 حتى عام 2003</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87014" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXy6HtUoHuQHYhc4LtJoGzhbWbokQ-xZyj_Kdp6a5hX3tLb2Z42HxXe_NzpDCFfxhEzkqC7vYDfKfCKjjZX8jsoU5di0CxdNRyw8M60RSTi2UPkE69VFbbEIWPnEFSp6D7f089HinxTmcPxXAXs4AKZMLAxt6elWSEBLsODcx-_OhMKVpKSYbdrfNc_NcoWRl3bDn2MWX-GJNBTUcx_hWa0iXMPhWtV4ht9OyPbM3p5HDzOt_6UchA66VmM1wa6ygxvqpqfbw8pExce6hu2k6h9K9hUvQFZRGi7Qrt85lqgHOeVSzK37PgWYewt51fg2Z1QtIUNnT3_Q7i-lnfHLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDkXtcWRRi_PypvACLMXd-1aO6hICfdTOiiyagYcLGhhB62YiQOW-RLjkU98rCeNUCz_FCG9rerTUTDq6hRvZMvoGqve2hxon2f1QqlGjXuAPcXMfGZ6c8O0hRpTsxWuh0NOTASa0CbdrASjvW7wxvnITG2a3HkIcvei6Im8cTpKstV3T-1woT9AEWL2R1eBmmQTBiMe22kEjUeotJ1vEA1Cob82KEv1w85l5XQ2eUQKRCj50G5osNK5q4W3-rjm93NR3E9d-yyPl4p1YDfybLmr_-wS-DkOo8PJyuGn6e219IfwdKIMPRtvAQZX25Ycg97f5OMIA6eJd9vZU23CpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
ألمانيا: اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87012" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3nBLhSxQjM__GkwB56JTl7XOlWffl_rScMGOXnxvRbuxDh9bnpG76Ya3jsnhr2qR7kEfOxSGHqYWopn6fQ2auBNyV70IYdzm-DanQTefL_XNMo0JluDeEkEJTh8O6LzkDipnNTZKB9PEcC-42a8U-raNoWOKohZyNbqTHUc1qmCgE7XpSrRMJEQxrCPe9VX3d99qoNyCc8EtGBsopCFbsWTH-b8W6y1GVywUXaDSg6CGoLGcNh_vdNXtbgE8rMge9CR2ENVgRrqjRAbUK4Wq5AyKf0bJziJbmlhalvI1nxqX-2VAGljCDcDKAltea1dXYxaE9NAuntMinQcszQkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنتحار المعارض الكردي الايراني (مصطفى قاسمي حسنون)د في ناحية بحركة ضمن محافظة أربيل أمام مبنى الأمم المتحدة اعتراضاً على عدم قبولة كمهاجر سياسي وعدم توطينة في دولة أخرى كلاجئ سياسي</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87008" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlqW5fsifF6vJ3rWxkLX6ViDj3ZI7VpLSHImj9heQIggGpM05fYNc5OYK5xxxgtXpV28XNt-xtFJqeB9HkSglSvyIiY_D5Hxz1n4n8N2unXdZyLc4G0tWPvm6HFsoFm9EvxKnoyN7nCMGZMGL2NoXjyK2hIqppo7iZuFqpKsMKGEcj59cdgiXS6swPK7e7YXN1uEX9mksThySULnhTqw5Hze-c7YXzsnQOLqOUVLrBmEWWkIp11Q-xf8IZiYfbgSZSfUxb9wgyEaQU7YH5N9Hd4uX9js8O9hRA5yKMj0BJ--ceLgw17WMP1SlKE1wqtV2FHcvh6BX_gKsd3R2tL_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">More time , more 48 hours softie
😆</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87007" target="_blank">📅 12:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aslcOJ2fXNuNjZeKkaa5ReJLtLkc7l6r3iNyGcAq5KhbwFnusTjox6Za0TYfpO91lFlMDbi91cLpNJdlOuq_JugsFxqdc9aOeHRiv43w-gqUgnBffjudgquCWv6bonUERL32bFdB2z3G3eLnPEuFjo4Ed0PZRGiRQuhsCc0S68FnSI7oyNNk4eVFhNOPnCi9_7Ek9WI1mAMTVnEc17rmWmRiDu_azTRxG748xhEFt-0-LUBHUtY7AG55wSlaEM7Svv4DLBjcFYej7SjnmipBbRIbRXRBYdOuW7e4GnizKbWzfZ35S79w6_fx6uv_hyljSuaucnELBzfdtxfV6J-UaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران  بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87006" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇩🇪
ألمانيا:
اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87004" target="_blank">📅 11:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi_G2VMBArn87d_sETWFQxuAt8mr3hy2ItM3DmFTToKGlXRAY34kI7qLMqk1JZKSWMaT4ga6izwqoVformMkOZ-CLvbJEnmQYVf_ZRrFaURdV9Fx6L1w7_L94CRQLUdwotAzhPCr1mh6ZJ1wLBW0BsL519QRHLvzn2G-puR4WoGy6n2B_mAJ5frgTDB_ZWPCUChvPpWJX8BlGycftEJoEkjyNVg1wobjdR2m1FAug4CfAOgSHDt336TabvxiAXLHMK3EuGVtyZhUdrZyBk8mNwaqeXnVo0jSuAwwkV87HGtNb2DM1cn6v-pNNcsIMmab-WN7rDBAlIhl-g1OVKk9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران
بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87003" target="_blank">📅 11:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:  في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87002" target="_blank">📅 11:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: مضيق هرمز قد يفتح اليوم أو غدا الخميس</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87001" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzDJoCPB9S25xPQeSY-TMt9_QL1mJnBdYxvUHc2LNHxkrU8kNF0Po0_D2ivi9BoJ5QdloYo3xJwsu23aNe-QOwJ96E6YusHMFA6JGe9Bm90MwtAUSNxM6oUEqBNr9OoB-JgW4OaV3IhJ2GPBsK5fw1dsNpmqFJxM0LKHyQ0Qy4tYOPJzPZOSku-GdY958Kxq6caImPV0yWAj8WfhIKEt2O21VexesmiiYblzAAD5fZGfgMX3f8Qk6fFjwtEdsyez57VXdzRq8lBbLXx2eLYt7MvY47EIXagp2Az3JFg5Lnh8xLlVxncbaJQrCjEt4T2TL1BYM4R1-4y66dnq6glttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
استمرار اندلاع الحريق في سفينة تجارية تعرضت لهجوم بسبب مخالفتها لقوانين حرس الثورة الإسلامي واشتعلت النيران فيها أثناء عبورها الممر المائي قبالة سواحل شبه جزيرة مسندم العُمانية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87000" target="_blank">📅 10:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/86999" target="_blank">📅 10:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86998">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:  في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86998" target="_blank">📅 10:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86997">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:
في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ السعوديةِ شماليَّ البحرِ الأحمرِ أمامَ منطقةِ "ينبعَ" وذلكَ بعددٍ منْ الصواريخِ الباليستيةِ وكانَتِ الإصابةُ دقيقةً بفضلِ اللهِ.
وبهذا الاستهدافِ يكونُ إجماليُّ السفنِ التي استهدفتْها قواتُنا ثمانيَ سفنٍ نفطيةٍ سعوديةٍ منذُ بدءِ الحظرِ البحريِّ في 22 منْ يوليوَ الماضي.
فيما بلغَ إجماليُّ السفنِ التي تمَّ منعُها وإجبارُها على التراجعِ والعودةِ في البحرينِ الأحمرِ والعربيِّ 29 سفينةً نفطيةً سعوديةً.
ومعَ نجاحِ القواتِ المسلحةِ اليمنيةِ بفضلِ اللهِ في إحكامِ الحصارِ البحريِّ على العدوِّ السعوديِّ منْ بابِ المندبِ جنوبيَّ البحرِ الأحمرِ اتجهَ العدوُّ السعوديُّ لتحويلِ مسارِ سفنِهِ النفطيةِ باتجاهِ شمالِ البحرِ الأحمرِ ولهذا فإنَّ القواتِ المسلحةَ اليمنيةَ تؤكدُ على أنَّ عملياتِها ستستمرُّ وتتصاعدُ في استهدافِ السفنِ النفطيةِ السعوديةِ شماليَّ البحرِ الأحمرِ لإغلاقِ المنافذِ كافةً عليهِ ومنعِهِ منْ العبورِ لتثبيتِ معادلةِ الحصارِ بالحصارِ مهما كانَتِ النتائجُ والتداعياتُ متوكلينَ في ذلكَ على اللهِ ومعتمدينَ عليهِ.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86997" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇪🇸
وزارة ‏الداخلية الإسبانية: وفاة ما لايقل عن 67 مهاجرا خلال عبورهم جيب سبتة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86996" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0yhoy4prXRPbum3bRXIrW_3JGuVdd2y4FZgRjvVL2BKyON7xWnmaexMOVT7HPR1ugh0vo0LHRG6X3ENLdMf1UJJBe32TtpZKy6-8kgLvk2GWTEJKjcpjWi1iS04lzt07TfVC8SxzB8S4IgQS9qa88Va5RQ8TYOro4iu0u_itjaN2t8GQ42cjQznoBVQaki5QfSVQy6MoCh1z3Kjm4kMdTxWhmuNxM9Q2ZH428Cl2q0Rz5iggERlGO4I0yfea-1xbujqGvxipmIxSOWnz9Fti_yPaTi417yZjKZJJfXfYqBoX2f0t4N7yo8RDNicOwE34H3HJ7kEVh7QrzHXGKscLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
😃
خسارة كبيرة للوبي الصهيوني في مقاطعة ميشغان بامريكا
‏أنفقت لجنة الشؤون العامة الأمريكية الإسرائيلية (أيباك) أكثر من 36 مليون دولار لصالح منافسته، هايلي ستيفنز.
فيما يتوقع لعبد السيد في الانتخابات التمهيدية للحزب الديمقراطي في ولاية ميشيغان.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86995" target="_blank">📅 09:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏بيانات كبلر: 8 سفن فقط عبر مضيق هرمز يوم أمس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86994" target="_blank">📅 07:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed420e5d2.mp4?token=tDuNIu3JEJmqmpIb-0-6JQfg5yNBrOWS8FjIK-Dm7ad1Ith2-X9PI4N_qdleMFteJQKDJlLZI4l_Wc5CeDNz9_fY1wHPxzwTqWTaOG7pVC7t_5EEFEPnAuhXcRZ3TG_JxcUdAWM7bsAiSRw5ao5ZHnwitgnlMBcdxzPH6K94Rjkhjxp1AasuxDaCJzdSEj9dQIuhYFVoGxNRZ943Yu4SfGWSYT78D1KWgdw4mmrxKdRq58-Oet83YOh2u1uS0-1AD0cvC-xTi_clMNkVZpotx06jrMurYKwFUwhzypMGGl677kI12ZAZuBtBUINn2djsLV3PuDnHq4oE6jIY4QV1ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed420e5d2.mp4?token=tDuNIu3JEJmqmpIb-0-6JQfg5yNBrOWS8FjIK-Dm7ad1Ith2-X9PI4N_qdleMFteJQKDJlLZI4l_Wc5CeDNz9_fY1wHPxzwTqWTaOG7pVC7t_5EEFEPnAuhXcRZ3TG_JxcUdAWM7bsAiSRw5ao5ZHnwitgnlMBcdxzPH6K94Rjkhjxp1AasuxDaCJzdSEj9dQIuhYFVoGxNRZ943Yu4SfGWSYT78D1KWgdw4mmrxKdRq58-Oet83YOh2u1uS0-1AD0cvC-xTi_clMNkVZpotx06jrMurYKwFUwhzypMGGl677kI12ZAZuBtBUINn2djsLV3PuDnHq4oE6jIY4QV1ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نحن نخوض نقاشات جيدة جدًا. قد لا يرغبون في الاعتراف بذلك، ولكنكم تعلمون أن الأمر مقلق بعض الشيء.  أخبروا الناس أننا نخوض نقاشات رائعة، ثم يخرج شخص من إيران ويقول إننا لم نجتمع. هذا كذب. إنهم يريدون إبرام صفقة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86992" target="_blank">📅 07:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a30c867.mp4?token=KAcWV4sbbLiWGZdwc4wary_OWTO_8sxZmfUde1WCa45qq2Kw1PIQvgOS-zaNqvorsSN4XCwpV04dnxWC51HBtEg7oRAFo_y2A8tfL11eoEmmT9UJn2Arvy2r1VAFyd2k2BZkVXP0Zugt82QTqCuyzWXPTv6x5DcxB2ARPIh1XMXyxZ21Uz8xUA903wzVrMgWWm1MJdel_C7XQRpXB_PDJGcKgxsxI7IYkrVgtuPuPip_S7CjnB6YTXBvU6JmWSwBlIOQ9dUoaEiYEK6QMYV9wexDhBLEJL60RIk_VXvgvUmJiRyaTEd_OrymW00AJ9AgF6MTRgFnl70zfoDBZuWzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a30c867.mp4?token=KAcWV4sbbLiWGZdwc4wary_OWTO_8sxZmfUde1WCa45qq2Kw1PIQvgOS-zaNqvorsSN4XCwpV04dnxWC51HBtEg7oRAFo_y2A8tfL11eoEmmT9UJn2Arvy2r1VAFyd2k2BZkVXP0Zugt82QTqCuyzWXPTv6x5DcxB2ARPIh1XMXyxZ21Uz8xUA903wzVrMgWWm1MJdel_C7XQRpXB_PDJGcKgxsxI7IYkrVgtuPuPip_S7CjnB6YTXBvU6JmWSwBlIOQ9dUoaEiYEK6QMYV9wexDhBLEJL60RIk_VXvgvUmJiRyaTEd_OrymW00AJ9AgF6MTRgFnl70zfoDBZuWzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سيكون الوضع سيئا للغاية على إيران إذا لم نتوصل لاتفاق   لدينا متسع من الوقت للتوصل إلى اتفاق مع إيران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86991" target="_blank">📅 07:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏المراسل: إذا تراجعت إيران مرة أخرى، فهل ينتهي الأمر؟  ‏ترامب: حسناً، إذا تراجعوا مرة أخرى، فسوف يتعرضون لضربة قوية للغاية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86990" target="_blank">📅 06:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33ea57fb3.mp4?token=LPDKbTmsscIoEWbkMT37NkKbQf1aS9Z7DT3sKlbFO2Ux37sM5dn0T_Sl0K96DJJjKUt2c3HUSZ9p_wWv-Uy6QgCNWEVcrsqz6uKsDGnhNyvdEyWxgSRTJOUEApNyPBz500Orphdpkxch4Xm4c5Gp-WyL5ZR5U2nNvons_sNAO_UIZkUp0WK_4iCZNLIj1Rpii7xvj1M1g2HXCpz38mDT2ZoLJfW34msEA-7OMoRKIiGgU1hSYKRK0PGNMMKlLGPKGLYhdiDzpCaYFUcblNMdjGN_4k8eQ0vw9_SHlLKe3yKvOMTqKeVRWqpp9wdTP2CCZa1fc3RNnUuh-suXb5txag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33ea57fb3.mp4?token=LPDKbTmsscIoEWbkMT37NkKbQf1aS9Z7DT3sKlbFO2Ux37sM5dn0T_Sl0K96DJJjKUt2c3HUSZ9p_wWv-Uy6QgCNWEVcrsqz6uKsDGnhNyvdEyWxgSRTJOUEApNyPBz500Orphdpkxch4Xm4c5Gp-WyL5ZR5U2nNvons_sNAO_UIZkUp0WK_4iCZNLIj1Rpii7xvj1M1g2HXCpz38mDT2ZoLJfW34msEA-7OMoRKIiGgU1hSYKRK0PGNMMKlLGPKGLYhdiDzpCaYFUcblNMdjGN_4k8eQ0vw9_SHlLKe3yKvOMTqKeVRWqpp9wdTP2CCZa1fc3RNnUuh-suXb5txag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نجري مناقشات جيدة جدا مع إيران  مضيق هرمز "سيُفتح قريباً جداً" أو ستتعرض إيران لضربة "قوية للغاية"</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86989" target="_blank">📅 06:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6627805129.mp4?token=tGDbym7PHvv96pzEYFfo46uP6S8fFWu5Dc8L1Wp-Gfc0-7Y7WOiDoE3CAh8as90K7HUJwKsPmUHq7rrFOXUDItKTPLf9IoEPFwmmnkxxOpxP617HvLdjKfFLuh6twdqfIaSW6rzNKwTD-DHorHnRVTMk56hPRbV6rNSU5mRNPHMunvjKtC5qSpKsUNih68OX-oYTdYp1H2im7PDEzLI4swie6CTOH1XidATYmwfjQRMBo8_LRSczliYh3u-5KTyjQK1iYKyBtWF-a9UtRLfBZIWhUN4oh9Q6b5lRlBL9Y719GN1goa1RJmNIlxI3u1LiKvXKRUB5U1FkOFqDi4S1Hlv4IvgyWT2sIuJX7Bc_2diggGLFgnRMG2kXZZfWlOiAT_080tbnL-wbz0oqx_On1UMSDNLbtxexUGbDARNMWSeF3tcGaFFD3OGpu1nJkLHp50oNtkEmtaSO2K4nhcNy3qW0d4_qg-PDAHXVxZxh7uQePqGQNcT7A47-jeCNke_daKjQOSLB0r5p0rmcE_pomELIf_vFuQSzJC4b0l3iZ-1KD3y_wG21WNPoqtPtnNQqH0lV65rkuaZ-o7oZvuBgjiNnFzxfa_vkjc5m1Ja8zssn362xVLjECtU-aijPc911WAt10XfMntNHelk40m8-I9IV-KR7Yw44S3bp29H1pJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6627805129.mp4?token=tGDbym7PHvv96pzEYFfo46uP6S8fFWu5Dc8L1Wp-Gfc0-7Y7WOiDoE3CAh8as90K7HUJwKsPmUHq7rrFOXUDItKTPLf9IoEPFwmmnkxxOpxP617HvLdjKfFLuh6twdqfIaSW6rzNKwTD-DHorHnRVTMk56hPRbV6rNSU5mRNPHMunvjKtC5qSpKsUNih68OX-oYTdYp1H2im7PDEzLI4swie6CTOH1XidATYmwfjQRMBo8_LRSczliYh3u-5KTyjQK1iYKyBtWF-a9UtRLfBZIWhUN4oh9Q6b5lRlBL9Y719GN1goa1RJmNIlxI3u1LiKvXKRUB5U1FkOFqDi4S1Hlv4IvgyWT2sIuJX7Bc_2diggGLFgnRMG2kXZZfWlOiAT_080tbnL-wbz0oqx_On1UMSDNLbtxexUGbDARNMWSeF3tcGaFFD3OGpu1nJkLHp50oNtkEmtaSO2K4nhcNy3qW0d4_qg-PDAHXVxZxh7uQePqGQNcT7A47-jeCNke_daKjQOSLB0r5p0rmcE_pomELIf_vFuQSzJC4b0l3iZ-1KD3y_wG21WNPoqtPtnNQqH0lV65rkuaZ-o7oZvuBgjiNnFzxfa_vkjc5m1Ja8zssn362xVLjECtU-aijPc911WAt10XfMntNHelk40m8-I9IV-KR7Yw44S3bp29H1pJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نجري مناقشات جيدة جدا مع إيران
مضيق هرمز "سيُفتح قريباً جداً" أو ستتعرض إيران لضربة "قوية للغاية"</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86988" target="_blank">📅 06:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">استهداف سفينة في الخليج الفارسي بالقرب من مضيق هرمز والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86987" target="_blank">📅 05:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي جديد على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86986" target="_blank">📅 05:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86984">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pY-OszSTRFQA2DMnN8RZzdd4ZEUh_bVbfWFRVOZae7rfnFPZDPjp1SxoqUpaxZbfnuJVLhOTsLHEGcOurLSW-rcfsv764VwwPjpu-KlnvBSUgOxsaLUVpdkjPyWutTJN3LYYtU_eHEVXoXvGnS8pSbCHAQsi-2xz32WD-lmktZhMURxPvrguxwncTsbhlsS7xrpfBJYA7F7SPcRGsFdlzJ2SrWnACx8aA9QKc8cafwH_iBSrKKL_EaYWwKCJC9WG50mUBgYt-3z8Ap4mFsm3jBfL9XVkd9ZrUy3JRAkzwO0k2xQJ2138ri6y9NlLUF59FV0OeCnaHZPRJrGyqEEJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-6Y4peixttXpMlTdNbap7YZgo-9z9ubhMlD7rbdTm8YZOtL4mJQzLq0NsGjHjjbOFG0KfS_6CuVNSgVIzfMpzy7tWAu6DzoekeWteDOnQLikkum0NPXfDGeSl2a7xMflxWRmDoFcZRQw7XYXduBkYLxIPsoSp9xnsP2x2kuNyKgZmFLx-2AsBwZuKce8Syf_RaEhdQqlMeiJgBfNQG4GeuyZzKhauOM2_FBgYH8by9KRiuXQVN7Xr7lLL5jQ4IcH1l_99t08ZhN6xxtJikEkiJjc-vLYY2pLKtA6KYtadp22AX1AkJ4BdmneEk8qIXd8h68MfdKLGENExj4LQNgTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرائق وأعمدة دخان واسعة تملأ سماء المدينة الصناعية في جبل علي الإماراتية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86984" target="_blank">📅 05:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86983">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال:
مسؤولو الطيران الفيدرالي يراجعون حادثة تتعلق بسلامة الحركة الجوية وقعت الثلاثاء وشملت مروحية كانت تقل الرئيس ترامب.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86983" target="_blank">📅 04:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86982">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjWu9T9KP64utjtxzKNmpDVMipGo8g5O4aRHUjp-8QeBAER88junYVN6_U1gPsafBnHSS3O7jpETLOxkH4PhZtTDB8YFLa38k2ySSJP50Gkd3kXgVYzJ3nAQEpnaobWCuPbZ1rNQ6VoFSMWNAkFe6y_KUgzZgoo0xxWE65E8AWM9McOmP-H4tcxLtNKra7ZbTkSksRsUXzvpdmZqmWbtGPLoDjlT4A49LRXPS12_Ct7B5yTnOgIUHEiolF9m2XsCtDuJAEBTKtLRiDMCL1drUoWujdkNfTa8xfIYf3mOciTvU2u3YhwI1B9jecpeTcl6LO0bVJbmg1DEhraJYcZi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران مسير فوق اجواء قطر والبحرين بعد الانفجارات المجهولة في دبي</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86982" target="_blank">📅 03:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86981">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتفاع شاخص درخواست "کله پاچه" در خیابان فردوسی تهران.
فقط آمریکا نیست که از طریق میزان مصرف پیتزا، نشانه‌هایی از جنگ را تشخیص می‌دهد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86981" target="_blank">📅 03:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86980">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXGxm-LN-R95u6_tE_Z2LJctPviPJ0XjrYuqnhrey0DlFQ0rp6geTP5g1frI3iFFsBwMQyPysAJMz2_F8j-_LdlnHetMmcjl9xJKALRm4VpG0J_3A96dWFLoIS-RSBHBWhaaCB9VChQIs-OPPjIm7U-QfdG49LDG-LV2zSFisVDQs82QSW8jV5VfI_D-uf8EoMg74Z3jTgTj1T37nj53Ra6a7uyyptYXhHcpTjXtH9heXLPP-2Nf5TKX7tOeL7rWjfurHwkpotoWSQcYE0NHbMgw6dIluMVSY7ZY49TshQ40ZRyTpwxkT47UeZHYxbV16RowJoy-sMHtLMBQKdQYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
Whatever happened in Dubai, and who was behind the attack, one thing is clear
the outcome suggests that no U.S. air defense systems nor NATO air defense systems were able to intercept the attack. It also appears that the United States is facing a significant shortage of AD missiles, as Reuters reported today.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86980" target="_blank">📅 03:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86979">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60051ef060.mp4?token=rGvvi1rb-wu7DWtWNw89u1AwEv5up-JRSDQgTUgLo7hl6uGEgTE3cnIq1pGxARzh8ujXIn9_pjS_IXhA_zYnQDOfNh6zHADuuL4DNfBxuTiXP6DAl3WDuAmO5WI2Wemy__QattvuFZ6Q6gWPafaKvIfzsKbug5E5JlOzJMqljI3Wjql92X9vdQuxs6eoT2qKcc0l-quE_Pc4EGJpJJ9t31LP1ojYbfPg9uLBi9aOuibbK5zfChDGapq2P9VUoiwMopGXQSGvyNi09Y1GpqiQlYyERnLfJ0XCdsF-FpZ-KGfyChgJo3reFFcC7dWvccl1TmQgkcXxNGnccfGnUNzbcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60051ef060.mp4?token=rGvvi1rb-wu7DWtWNw89u1AwEv5up-JRSDQgTUgLo7hl6uGEgTE3cnIq1pGxARzh8ujXIn9_pjS_IXhA_zYnQDOfNh6zHADuuL4DNfBxuTiXP6DAl3WDuAmO5WI2Wemy__QattvuFZ6Q6gWPafaKvIfzsKbug5E5JlOzJMqljI3Wjql92X9vdQuxs6eoT2qKcc0l-quE_Pc4EGJpJJ9t31LP1ojYbfPg9uLBi9aOuibbK5zfChDGapq2P9VUoiwMopGXQSGvyNi09Y1GpqiQlYyERnLfJ0XCdsF-FpZ-KGfyChgJo3reFFcC7dWvccl1TmQgkcXxNGnccfGnUNzbcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86979" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4142b08e04.mp4?token=v5bsqvkAJiqdvB-hb6eHmOLhBwGO5HM2yyWu5yB-VpIndjKliEMm7Cwy6n1EXSUo_fwlw_Gnx7HDqrvzf2ODJS-gPJ415g-P6sRNDfTVt8gO6upZcS8pZgcc4trYvqUyjjLTQGvDx0M1SlIBVEn49F59JVrcEmN8lRWydZSPTU38-pZyWh7okA8g7R_CMERSRR3tLdiCsOSepBNb0yWQBNeHx_QsMAmlkUyLXADUf8zzZx5uUDh-6Eqv3kIblrb2nowCPcJkaAMM0HayneKMNTpvAl-gZYEe_UHSLc5hksbz4YIf8P8yY9fxorOaw6SvrrW4E0Qd7eoz54vViM_zPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4142b08e04.mp4?token=v5bsqvkAJiqdvB-hb6eHmOLhBwGO5HM2yyWu5yB-VpIndjKliEMm7Cwy6n1EXSUo_fwlw_Gnx7HDqrvzf2ODJS-gPJ415g-P6sRNDfTVt8gO6upZcS8pZgcc4trYvqUyjjLTQGvDx0M1SlIBVEn49F59JVrcEmN8lRWydZSPTU38-pZyWh7okA8g7R_CMERSRR3tLdiCsOSepBNb0yWQBNeHx_QsMAmlkUyLXADUf8zzZx5uUDh-6Eqv3kIblrb2nowCPcJkaAMM0HayneKMNTpvAl-gZYEe_UHSLc5hksbz4YIf8P8yY9fxorOaw6SvrrW4E0Qd7eoz54vViM_zPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تصاعد أعمدة الدخان في المدينة الصناعية بجبل علي الإماراتية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86978" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86977">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعيدا عن حرائق كييف ودبي
اندلاع حريق قرب مقتربات المستشفى الإيطالي بمنطقة الجادرية بالعاصمة بغداد .</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86977" target="_blank">📅 03:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الصمت يعم الإعلام الإماراتي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86976" target="_blank">📅 03:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwLcduYK9HPfsuNDBAxH8Sz3u5onf7TlcFQcaDJymbUpfQWrZWhqeFaZJQk7yEdVFAj0o1whrKdFusQSUKhw6tuP32XS_5GkVHAzdRW2lU9GWAahzjlgb_oSsD_mJPX2Gr-AhzJ_rq611FtrIicWX9sQG2v79lO2KHUgBf5v18bGv0-rSieBvLx1msFfUV-zvlO6mgHsF4Irj9TMgdZwtQdwR8qdheH36_yRf50d926DRYwfgo5eWPctBpVVHB-bB2BF7GAGLM4lFIFWNGQxgraI_qsF2euh7KwCO2fV-H3Dc-tnbjcQ9zWamv3uiNS1afXt6JOuecuR_QHoNIi_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناسا ترصد ارتفاع درجة الحرارة على ما يبدو حريق او مصدر اشتعال من محطة غازية عائمة قبالة جبل علي !</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86975" target="_blank">📅 03:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86974" target="_blank">📅 03:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyTaF6AQdpMpkpfyO8LQf-4iKFMmsyY9ToMhGhiJwFNUgJHvw2Im3pLtMq3xBqwxzgQXkDPDPO0oAf_-vY6t0Ug068sEH06RhOQAQhMWusGPj7LpSMrfPY_ha5H_GZ4OmZJBpbrhwxHXaC7j4UFWp5NWXo8UXshmCj4Zd90OWGNW-gTWSveOabrs4kXeY1smxM7xC12ytVYf6BCwmpAW98nep4U3MHsPrQ22KXZs0d0N6_4hf6EfUf4RWcH47o6Oe7a-vuVjVYF12-htWbwUX2YddQNPqLFCV5bP_fjSlY4sqnYGX92EYHIINdBSVR7xSg3e7rVh3uJphlXrWed4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمار شامل في المدينة الصناعية بجبل علي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86972" target="_blank">📅 03:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86971" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp6lrpRCIHMGktHxmXCaK8D3HbBa4-YkyKm1gTBXibus5n-Wb5OPEQPPOYCa5hrv1NhFhc4QpHZRACGGY90Unjnw4aZeclFHWZTZw3Z8MVoPAeRebAba92g7xLjZbBful_HtPQABonf6djptbWxe3Aqex7ualyRWpmdpWeVRW3h80LTEfgeZQd_dvZXcOaWwupJqxmfB9VOtZNXfCbkAqDSKYCtJwkKKfc0v9Gy-hPD-i7dsKDmAMRfo5bY8iOF_nrWwV_0RjvTIwzCuhrjBqq4tcusOUCuU7W79CmQXlBwlAuqs6i6lmgPhB9q2LCI0VEgl3havnxaXLvcwqn84cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة في الخليج الفارسي بالقرب من مضيق هرمز والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86970" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86969" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc5IMG0AW8FHc7s6BU1dbrGic1APcfIL8ZItjtSI8iT5Hvncbuyu2sq6tQeikyWpAF5zMuLa6KD5XYxUHrPTihUCJLKOWsUnnxoCHR4itKMaDNhaIqZ_BFUMh71lu5GWrvBSne05IRxok4maD2VKK5djozDdCN0Ypx7e7FbaQHxLtotEQLqB9ddG66YA8zdk-tdxWdXSbEhbkgnsGAslCVW1H8o8vg2k1cQh7N6uoBczZdnZrvlnBBMYoNr4sUOFxb_kpWcKB1oVVLeHBFRaRE0iviYGQL2YeVVgLDShvEIA8m9uKpy3hEdj53OptSWpSY6WXNSz75aj7yiRF0iYFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمار شامل في منطقة المارينا بالمدينة الصناعية في دبي نتيجة هجوم مجهول</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86968" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86967" target="_blank">📅 03:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ef471bfb.mp4?token=bSyFmX7TOImTSc5RlfOpMCjoVvMbLkFqCXXbmIH8wLqqWFa2AXpjr3ebZloVoef9Y76ctvmLV8EUY1F06HcXkRO4lj9kZWbY4YygK2jqQ9oaCEYszp98K3OrX6ZPGK84N3Je_JcJ8yZE7bBor9b1YbzBmn1akjoHTQ2JjBRHUdokPq1y22sAcADT4dvrHh-w7Cqsr_ONlKeLej3nRBUCcTbs4L-jhuB5pqOpyGqtuCaiuoy_ecoxvSMyP1V0ba1x1AEHuLrzLXk7u8MjFI7FnVaoiQDp0Snw2vBz6riVsWjmLjmviw2Pm5DCS61MyzenvcHThGPP7-GSIELkEu4-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ef471bfb.mp4?token=bSyFmX7TOImTSc5RlfOpMCjoVvMbLkFqCXXbmIH8wLqqWFa2AXpjr3ebZloVoef9Y76ctvmLV8EUY1F06HcXkRO4lj9kZWbY4YygK2jqQ9oaCEYszp98K3OrX6ZPGK84N3Je_JcJ8yZE7bBor9b1YbzBmn1akjoHTQ2JjBRHUdokPq1y22sAcADT4dvrHh-w7Cqsr_ONlKeLej3nRBUCcTbs4L-jhuB5pqOpyGqtuCaiuoy_ecoxvSMyP1V0ba1x1AEHuLrzLXk7u8MjFI7FnVaoiQDp0Snw2vBz6riVsWjmLjmviw2Pm5DCS61MyzenvcHThGPP7-GSIELkEu4-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86966" target="_blank">📅 03:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBzyf0XGHYQoesL0QK0Q-Ln92reEkE67DX-7htCfNNq5pDZxTypPc_PQz9BL8pj6_WM_PFK1SXoHh0ZMFBtSmq4DoZYQ4JnEg46zxYgZvvU-tBSXyy1IiqXpRhRNqobNHPkpT10afZsKm4JLK5VpV_NlaDZQfML-vUG1vq2vkUAEQqk4pT64i5nIoEAOFvnrh0a-IJVXo9Svr6mD79kxNddikBQTMRqfsOUWLAJh6gVlJm5kx5oUIctsOkJKJj8OfeZRVve0zLtIOW31jeT_i5zRH7841b1PSH9uueZiadhSwE50Jyq8g-LtCh1iVnN_lM6rEwAOyDEx80fohsQMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي اصوات انفجارات مجددا في دبي المنطقة الصناعية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86965" target="_blank">📅 03:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86964" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hconG9D_c-3jtcM9VgjF-t1NZPe9GcJrKyh6OuHJiCSLd_2XeJUArCkv59tvNTKZfhi3S5iTl8Z5c42UGFkpq2yheBb16Rt_Vr_FrUJdJ9pLMo2Eg9ZQ_p-pCNrj3tpV4wDhmf02kIXRO71z6WiMzi58RDrGtGYBbaSfRbrhMebUid63FwNkHNeezYtGFs2OP2J_zEuURYxu20O1eQvDeR0yCKh6xSMTQLr77aLuTVY43FSGOIQkHCnyHQvnMZRSWKGb7wQj4FJmZst_iE1BS_mBtUPWmGj4mEHxXi26CUc99thl1vcn3iCU8l7jS-cWqi0dF7PYHE_LvrjzmBFCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86963" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86962" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86961" target="_blank">📅 03:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474c99c5b5.mp4?token=sWeinrm08H9TKPjzJBphu27DcxCChr_utfAfwoa81BneLsYMMzZBU5pr-ALMtLnJBbnDV6wXYWZ76M2_BEz1wzCaptMpGRY_nQluD9WAUZFySONkj8SDziqVdP7D753qnITyzz6GjVOwEjFhR_uJ9PlirKTG7Lpo3NVPK-1Xfc6kTe2o4-TbVVuRc-CfKZcj64qpSHjV4EQCVoeJotpJRbc9mPXwtBVp3F0NpYUGlnkD9BYHO-uLI8kPHJpK_GGYpu9PO9lwVsyJ9ZdisIiK6N4wIslN3bsECk6Mf1x5bcTbII_Hizz1qK22MTVFNPCEo6vaNo7n20sZlKTnqYwc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474c99c5b5.mp4?token=sWeinrm08H9TKPjzJBphu27DcxCChr_utfAfwoa81BneLsYMMzZBU5pr-ALMtLnJBbnDV6wXYWZ76M2_BEz1wzCaptMpGRY_nQluD9WAUZFySONkj8SDziqVdP7D753qnITyzz6GjVOwEjFhR_uJ9PlirKTG7Lpo3NVPK-1Xfc6kTe2o4-TbVVuRc-CfKZcj64qpSHjV4EQCVoeJotpJRbc9mPXwtBVp3F0NpYUGlnkD9BYHO-uLI8kPHJpK_GGYpu9PO9lwVsyJ9ZdisIiK6N4wIslN3bsECk6Mf1x5bcTbII_Hizz1qK22MTVFNPCEo6vaNo7n20sZlKTnqYwc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86960" target="_blank">📅 02:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWCg56KZExW3efdmtc64Df5tpuNVdGtJQ-b-yDEZBXuvl8u-Ecl19m4rAH53EdFrmiwOfGdRFEfMEO6Dic9mqp_UbnYkzg_9RXbLQLaTMllBrmBaLThjn0BUYlRduhH86js1H98eS_QtzMcq-z6mwrXNJt5zCo0_s6-9nLsE76Ga37N8jFg0hKv3tF3iFdhN4oS9ZGrRYgnU5NJcnIBICM51yHfnXMJ-S6B1PHeV0vlcZ86rnpaEbbOFWPWW3VFIv6J7AhFvhxzUPpzW0KIC2Iv-h7RCwUeK4yLh_7-1BVMkQSRfEzDefBkO52L4L7yQYykHAuizQ2Vth4zTP4pyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
لفترة طويلة جدًا، حاول نشطاء المناخ المتطرفون احتجاز بلدنا العظيم رهينة من خلال توسيع نطاق قانون الأنواع المهددة بالانقراض بشكل كبير وغير معقول. لقد كان هذا تجاوزًا تنظيميًا كاملًا وشاملًا من قبل بيروقراطيين غير منتخبين! لقد عاملوا الأمريكيين بظلم شديد من خلال خنق إنتاج موارد مهمة مثل النفط والغاز الطبيعي والأخشاب، ومنع بناء منازل العائلات والبنية التحتية الحيوية. حتى جيشنا لم يتمكن من التدريب على أرض اعتبرت "محظورة" لحماية قارض صغير! الآن أعادت إدارتي قانون الأنواع المهددة بالانقراض إلى ما كان مقصودًا له، تمامًا كما أوضح القاضي العظيم أنتونين سكاليا في قضايا سابقة. بينما تحمي الولايات المتحدة الأمريكية بلدنا الجميل بمسؤولية، فإنها ستبني مرة أخرى. شكرًا لكم على اهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86959" target="_blank">📅 02:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86958" target="_blank">📅 02:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2qcasrccAc-hdkQMQ4nuJPctszzHLBBIPAUqbseyEryz5MPUn-rsG_THuFRPqS3TSx5AqIW4OpoiGe0_7f_FNMMIS7tca2PgQU3oLQO5BXaQMioHc2J4lOUf8xYuJ-cevWedXnYpRXLoGZytdnt6FsehPDMmdn7FacdziSWWajlJWIfPv3Fg3QmtAb8BSTF72JENUdiQZJp8rD6HigXP__-6DqZ6Ei7TPV6UIZ9RtORcPA_qVQNyLeBA9lYKRWe51Kou-L9MKw6dU395C2b1w9LAmD3gKs2bRJkQhSpWmuXUM-LqBeGxhQFSCowVlhJrUiBT0PGs617jAUBK2Mmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86957" target="_blank">📅 02:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86956" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عدوان على صنعاء</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86955" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عدوان على صنعاء</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86954" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الغاء رحلة اسطنبول - بغداد لاسباب غير معروفة بعد ان شهدت تأخير دام 6 ساعات</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86953" target="_blank">📅 02:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
‏
اعلام العدو عن مسؤول صهيوني كبير:
ترامب يريد التوصل إلى اتفاق بأي ثمن، مشيراً إلى أن "المسافة بين السلام والحرب مع ترامب هي المسافة بين الأحرف على لوحة المفاتيح</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86952" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5lphcqZBqon-MIqjdXXekwRB4TW_tRlVhwoRQvwe9JJeTUn7cx2Tzb37WxEI6LM_ZK_c3LSEI9rLN7t3IflMr20q3RoAsHZ4lafvLMaV9MrdY2tipVK3nhbKb5MEsf13tnsWVWIskcbWTYYAP2L5ZHrIoAkjCujDq0lMshDwCUGt6itKkFRKr3e58blvWMmPyu5PQ4iOShssD7wwVfzQfeeYs7QFjJYJDa0F2r81n7eiI9FcekLlspRdFv5xYPDBFU4ZO2pdGlyeEN0_0Xhp30wb7PoDtQE8rHDSAq-ekS0saL-6YK-OvR8Jcu8DGgN-vbr6W381jyXoqXV_SULDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط لعبة "ديلاب هوا" بعدد من العوائل في مدينة ألعاب جلولاء بمحافظة ديالى شرقي العراق وانباء عن عدة أصابات بشرية بالغة</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86951" target="_blank">📅 01:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PiGdCS3LAvLtrCmA8vkATaMBlhY-IooAGQbONgttXemxYRvczwicJQwa2EgBWktD0fPWVOEQPRxe0TszPiV9kA9M041baidMEC-f1pi7HU3MI560Np5xwYorp3bB9fAYmmSp5ToSpWRSevC7hHPmad_EhATO-zFOisxgUZh8zePmyfISrQzXXs4MNxLbmHDLOxD1wPTBEGPbNQk9GsfKp5jwLOBNyo0OcQeeHPF3yxuJzjA0s-_w_rK45d7PDVaN-fckp8RCgNcuQ5U-l5GpTu8sg6kyLvBQkuo_KdnBqiSINpPe_Ih4cHQskhXMHdCA98h-WuQepeiM99FUFzO--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsnyvxHQvpLiH9XDEGGn3NYAP-ftmMwNV42q8TL8bi-bg0iU5Ms7D5W4qW3IpMwfaOg194aVa-HgU2CfIRmHCZEG-NOttzyuSOIT1ki6ng8T_lX7IJ1JpiGV5r1Ybff80YQ0iD2d8RqDnRa25_AQQqjobXnXh6oFtZypCL77LIVnT68zx_jDhQk5ra27j9giOYuuebLfL7XGyj3Ftff8yNWiSPBi0nhmaUIiU65oYRgZlNwJUwB-6SQM6DMOxXgLWEnkE43IVKbJPBpHJwGN3bRNBC7OEUV9gNiYRwagYZzscuwssUEjm08cNyjfW4QGQre9p1Sak-kiQ_hT_TgNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzAzhI0PR3DvE1OLagN1oyUOg0HGSfFi7sngerR2gyzfY6PqLjTsuQh6M3ePp0-PpMDbC7cj8ccLYOkSqlYxuWLIesUxmaiSJmTxWY3HYT2A9yA2dded9zAgx_I4-fTBFLjTm4xwwyi5kQaVBsAnXeyQL5xRKNPEjB1oIL5GOR9UDm30OD92pItQWkgn4fsu4y9CswmXB431v4DhZGBzMeMi1N18P6NI47aT6GWmaj6kkEn89QUmNletNnnlIJCWLLhwQfteU9GLOiDqKDAQeY14vQQyJIOmIzhNeR01Y51KrY0X5Rb_3Z6BfF39rCiVQvh2sxiD1X2xqPInQAE_7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدة انفجارات في كييف بعد هجوم باليستي روسي</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86948" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d88d2557f.mp4?token=OgjiNhG3UneaSMnh5LNcqIIgUbMmomKJyKI4aG3mMG09DQpr42edsoBY3lGIicVlIo_atzopgvQ6oM8xBcU4r2oPRLxgD7HaDCT4GzL81Z5QWibwnVtMT-5bUhl3HNG4mk7XfYwlrbGLESDbT9i2-1Uqxq6vhZoYmpDlJDZtEVzhABeyzFfm11qNato4_Dw1nSxR_Lh95rvVwinHm6iRqP_WU49-R4gPib61PzGpgukM6sNv1sP2XwXolp_j-o9wAaJiccnDALaiO4zmN8pkUPF3HmrrdxVU2YE8buwRGb5p-JYX7L3Dng83MgU1cjbuVsWKteQJ0nZ2YFHs7z5PZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d88d2557f.mp4?token=OgjiNhG3UneaSMnh5LNcqIIgUbMmomKJyKI4aG3mMG09DQpr42edsoBY3lGIicVlIo_atzopgvQ6oM8xBcU4r2oPRLxgD7HaDCT4GzL81Z5QWibwnVtMT-5bUhl3HNG4mk7XfYwlrbGLESDbT9i2-1Uqxq6vhZoYmpDlJDZtEVzhABeyzFfm11qNato4_Dw1nSxR_Lh95rvVwinHm6iRqP_WU49-R4gPib61PzGpgukM6sNv1sP2XwXolp_j-o9wAaJiccnDALaiO4zmN8pkUPF3HmrrdxVU2YE8buwRGb5p-JYX7L3Dng83MgU1cjbuVsWKteQJ0nZ2YFHs7z5PZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لصافرات الانذار تدوي في كييف</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86947" target="_blank">📅 01:19 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
