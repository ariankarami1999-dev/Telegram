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
<img src="https://cdn4.telesco.pe/file/AncggfiCU95rumxzJa7ML3cTDnN1NjH_nk7JcelTkrhZjO7enmJUsOKAqv_vNfmJtVRP-VzzBYfXKO__qSmzR7Nd02wBlpzM8Wflc95ZDWtdEwQ5ZcPC7gg-uN7MJQQH_q3cLY2c4NWAHgMwTQqWJURgCyGlDrWw4Q-aMAHQdCLNTmyTKPrWg50eEzQMWnN4WI_iVbT_nV3ZxedVv3hHBdf3nBXcn9sFTCtdMAPPikzAp2tenASRdpbhztlL9d3w5Rn5ZrK4KIiorvnv1II4EI0n4Rp4Z3N3CLlcK8iO-IWpBl5Epue2MQ58CebKjzRBlqVT9MvYVEbTMgoV7FoZGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 03:22:13</div>
<hr>

<div class="tg-post" id="msg-85976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f9b4b140.mp4?token=jlgvG_ql_KPgjeafdic8xBCFyU8AOaPW3pzyQ_B4ErydzOb8GVU_dJuVAWyfPS15d4K4TTExw1XYxoN7sZxOoj_Q9M-FcIKIWOyOVIMSbDszP0Kipmt2yU6mR-Qxu-kr_RkN_R-2qRd3ktdjx7ei7fmhBqInul0EVV6hX--z6dZuwl70rjUc43G1RICwrO81CziA3SsgxosHwHNP4hJYaVT7nS5tT8G5EtB0et1Fw3PW5uNqCC3Y8RL5ATp7YFvYfm6SRE6z0DD6hfsSnzMm1G1MZDbAGfmXWR_1Qrwdzt2WZUTmVGUCXYH1Wqr4W-uKFD6HBxVtfdZ-V3jZD3LO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f9b4b140.mp4?token=jlgvG_ql_KPgjeafdic8xBCFyU8AOaPW3pzyQ_B4ErydzOb8GVU_dJuVAWyfPS15d4K4TTExw1XYxoN7sZxOoj_Q9M-FcIKIWOyOVIMSbDszP0Kipmt2yU6mR-Qxu-kr_RkN_R-2qRd3ktdjx7ei7fmhBqInul0EVV6hX--z6dZuwl70rjUc43G1RICwrO81CziA3SsgxosHwHNP4hJYaVT7nS5tT8G5EtB0et1Fw3PW5uNqCC3Y8RL5ATp7YFvYfm6SRE6z0DD6hfsSnzMm1G1MZDbAGfmXWR_1Qrwdzt2WZUTmVGUCXYH1Wqr4W-uKFD6HBxVtfdZ-V3jZD3LO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي الانفجارات نتيجة انفجار كدس عتاد قرب مقر عسكري جنوبي العراق</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/naya_foriraq/85976" target="_blank">📅 03:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85975">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3af92751.mp4?token=GBW9yIjNTQpXIs3DRWp91JDdKwMAQ5GlrDjjDzZ21hRPsY8j1yytkyogDeGEDseI0Xnv18QLvNufGAMAnAzmsbErnlVFXFMmF-dlpoA7lVhzYS9gDRNtk0a0MVz8wsiod1WDYTR-25H4KnF5Jj14lgSbwtF9M_YWVa508SnAYe8zku2yVzHBdcM75E7uiutNUl9WRGEr8HJrewOaQR0skpO817mceOi5ZlAUV28iO_MQBRdeqpDp6qVZCK5lKMYTMDLjGaN_8gW3ueCqLQeaLZw8Yajr2MOqIcGE6BthNImJjcW6vhdSQWUo6YRrIjjRWf_K6PbPrSzY_BR6x82tQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3af92751.mp4?token=GBW9yIjNTQpXIs3DRWp91JDdKwMAQ5GlrDjjDzZ21hRPsY8j1yytkyogDeGEDseI0Xnv18QLvNufGAMAnAzmsbErnlVFXFMmF-dlpoA7lVhzYS9gDRNtk0a0MVz8wsiod1WDYTR-25H4KnF5Jj14lgSbwtF9M_YWVa508SnAYe8zku2yVzHBdcM75E7uiutNUl9WRGEr8HJrewOaQR0skpO817mceOi5ZlAUV28iO_MQBRdeqpDp6qVZCK5lKMYTMDLjGaN_8gW3ueCqLQeaLZw8Yajr2MOqIcGE6BthNImJjcW6vhdSQWUo6YRrIjjRWf_K6PbPrSzY_BR6x82tQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/85975" target="_blank">📅 02:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85974">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/85974" target="_blank">📅 02:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85973">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/naya_foriraq/85973" target="_blank">📅 02:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
‏
إدارة الطيران الفيدرالية الأمريكية:
تعليق رحلات الخطوط الجوية في جميع أنحاء الولايات المتحدة بسبب عطل في أنظمة تكنولوجيا المعلومات.</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/85972" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsUR-c24-pziFuJWCSrJAiFHMCci2TWIY1ltnfmlo0gNXvPFQNSB7VwsuOcn5M0tx-f_Xi4d7zj-6u8q-uvHW_VnEBXFHsKXcH3d45RtsDjVFw1tGgQ_2D2eVA6AfiLeHVzt1M6f4TqN0v7UmnHvtYTQzwgdy5bTqpgZ-bi4gz_pE25bazstFV18fQ55WF9rdBDK0qGEVbojvQyC2JRJ3_pxD4KRJKgZ8DbXv4hlRLMrrv4JMDAH_yxV5RA_nUgFt92pGXtIfmCKuJspSZNSJ6bzDbk6lnF6pVWQEvYJTWVDXV4_oW3sleRomb8ByfbUdPmafPi6CO1GD7-0BfhYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1ArSOlEM8n9HXhjg5nlEOCbo1K9wRTuiZtGJ8hn7D8De_ysXLnP1YDhyAsn1GrOdb_U15vKe-65FV92vPsw0arvVd1ca2o3XoPoZpbQ6fu2nvQtsXoZZdCw_D9HkDvpwxj4uW434vCBTn4XsJgCBhG4fjlJQHwFjjjL3J7XMnX7qJpDoh1FR_z6LnMANaVyO8Y0ISyQ9i8QYFgK4Jf9piOesUqrboYexpvL4rhtlYdymg3rNn0UF2xV_4B9WqaV2bkP8v76NcL4kuoSH7vWTrezGRusHvmkMFFKvqHidHZsbl3R-fNrsWx2-GAGO3xVmjN0PShdP3OEEJmhFqOjCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات الجوية الأميركية طيران الإرضاع الجوي و طائرات النقل الثقيل تحاول قدر الإمكان تجنب المرور بالعراق وتسلك مسارات السعودية الأردن خوفا من استهدافها في سماء العراق التي شهدت البارحة سقوط مسيرتين أمريكية</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/85970" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDAuPOVTgkBHfC-HkHPVpPy5IT7Yu9t-nfanZm5QlZT8upBkZsiwaCeChL1b4KnAQkaD8Ic7wBuB2KBeueRSyKPQlI52EU-2utGCJcx35vhd6bns6mkDPycCrghE_2fztvhWo4lNs6OlbZbc56UH6JtsRM30Y3haYTxLohVdmpmnUEgbkAxrVCrXOZsvRGVseJF5W0BLhym3R2g_DjCjNHFzHeEybtSSNN8C3ofrUEiXCTiPnKlXE-cEe-NvQx9w86J9p3AlxsxIl9d99uoJA4tinrLuUEytEjI4tnaZS_Pva860L891fU8a-k-vzYrHw2eYeGS7EV5Lc0oNLfbR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات الجوية الأميركية طيران الإرضاع الجوي و طائرات النقل الثقيل تحاول قدر الإمكان تجنب المرور بالعراق وتسلك مسارات السعودية الأردن خوفا من استهدافها في سماء العراق التي شهدت البارحة سقوط مسيرتين أمريكية</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/85969" target="_blank">📅 02:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجار عنيف في أربيل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/85968" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار عنيف في أربيل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/85967" target="_blank">📅 02:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طيران حربي في سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/85966" target="_blank">📅 02:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فقط للتنويه   وقف إطلاق النار كان من جانب امريكا وليس من جانب ايران ؛ بمعنى ايران لا تكسر الهدنة ؛ امريكا هي لوحدها قررت وقف إطلاق النار بعد ١٣ جولة ، و بسبب العوز الصاروخي والوضع الماساوي للقواعد في الكويت والبحرين والأردن وغلق باب المندب من قبل أنصار الله…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85965" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طيران حربي في سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85964" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
في تمام الساعة 5:45 مساءً بتوقيت شرق الولايات المتحدة اليوم، أطلقت قوات الحرس الثوري الإسلامي عدة صواريخ باليستية من إيران في محاولة لشن هجوم مفاجئ على القوات الأمريكية المتمركزة في الشرق الأوسط. وقد تم اعتراض جميع الصواريخ الإيرانية بنجاح. ولا تزال القوات الأمريكية في حالة تأهب قصوى.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85962" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd2f9593.mp4?token=ZMmhB5bNBzLMIAG-mN_TMrlP5o5rVrbYEzHlMX0IL66UuymbkxyZpoOCfxbamTo6kAvff0WGGqRmZm56_otKf0v6Hhb9YTmDOKK5uOOf7Q1OhEirtPH7VNtRQvkbv2KSPbJr0lWZ0S_cy9N98uBUWF_JzmUTuz6hX9bvJHzpPo8ucD08dobFJ_hS9OPBrRprcQbxB28uF6fZjYPN0WyZ7WaRzkvy_OyaCG0iW0ZumU5YMvCoS5D04xEaZ9uZEj1F_dlWc09zknxa_4YUT9_VcGhFMuDHaT3LvvLHmJiQMs-2HAoCzYnZfVtsYTsGj4nibJQ-kYom8tdlCHpTfPZbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd2f9593.mp4?token=ZMmhB5bNBzLMIAG-mN_TMrlP5o5rVrbYEzHlMX0IL66UuymbkxyZpoOCfxbamTo6kAvff0WGGqRmZm56_otKf0v6Hhb9YTmDOKK5uOOf7Q1OhEirtPH7VNtRQvkbv2KSPbJr0lWZ0S_cy9N98uBUWF_JzmUTuz6hX9bvJHzpPo8ucD08dobFJ_hS9OPBrRprcQbxB28uF6fZjYPN0WyZ7WaRzkvy_OyaCG0iW0ZumU5YMvCoS5D04xEaZ9uZEj1F_dlWc09zknxa_4YUT9_VcGhFMuDHaT3LvvLHmJiQMs-2HAoCzYnZfVtsYTsGj4nibJQ-kYom8tdlCHpTfPZbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة من سماء عَمان عقب إطلاق الصواريخ الإيرانية ومحاولات منظومة الباتريوت التصدي والاعتراض.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85961" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdWNh3YV0KIC37vVYjiLr_85bGQGrxHd8lRwqrcAhtmGmRLb9iKv3IGY9-gbH_SMwOd67rtxt5cs_n3RxX_dPbHIMum5NAfeSCNoPQI4KskVJeabDnF3cA_JLR6KhKPHn8RDGnBgvpge1bbdPRc9a_ITwtLehgGnm3Rky7ndf1zC2SVkQjzYZntDu7JtIf2w0KqJ2Ap9UKiI-sBYe-HY7GEVfIt79gPxvYDOI3EUygHElSbVPwtrOSQ-66QkBtlKJSYyPmai_8Jw56dig4566_cOiFBXRHB85-J1VqtbL6S3sdJYP-fZJs1Iug0hhsAuzuYoI8rt1nP2XzdP9vGqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شركة إيلون ماسك تطلق خدمة ستارلنك في العراق ..</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/85960" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">أعلام العدو: اصابة مباشرة في قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85959" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">أعلام العدو: اصابة مباشرة في قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85958" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4wkRHnjgagCloTaza642auISd17KXMG5G8C6hHGl_ocZp0yhBpJGlU0V7gV4vh9WharkEXN7OYyypkx5AkSvInigz421YVtLUMo1TpzDknQnovVwmsFsVYnL4xcfP2e2YAdwJNTJAcFPXZ04-4evQw5gJVeudJ5vZLQZqJfv4OMTZiKPLJxf4hXg1pxPHUwEAAble3qiLYsxt4hNTwAQsqdru0aeG0fKzvx9lXcP4hMIdx1FpQXz0SHkZDHJHUyA7JDEXCt1jM57KJxVK9fJtZbxbT3mzstTPpVxugJTsUZ7zsGIq9ytpf1iMdnkB2aKruEA1XLHZ3JfakQU-tOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85957" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079a967bc2.mp4?token=RPrxvlns0Vc37M34OgmfMjmmRPEubxD8TF640CdtmJblx99uQiWc7G2TwYQ9hlI4n9aee0iXQj9ZGGGilThwOjCJPrrAKnsyE0d1Q8LR-Mk2aXDFoubKdA2796HNKfcVnVvnUsAJD9jur_LaoEBlk6HaZrrRUByk4gumnirRGOCK4nmREpfRLQ1fxUaVzzMiA5g9i4IXtiScVlcsfnnouxLG-xZUr783qjmQlGACKytMxtI-YB5nshynt7SMf-OImEpiMvsz8TmBWztw8OEN78Fq4vWygyNCT270mp3ld0POH_ENb3nEh3UeLcacr_A84TNI3_IHBmbeK4iqQ0qyeKChpW9D7EaPWuN_9xmZNv2gx6T6FSpU0YA3bO4kfNtFXxAYGwYbH-RGDuFEr4PCjtQr32bmgT3NKXezRCyOT6wkjIK3_az1mMvWDcCDCpRdqUsILe3zpBeZl21MZlXE3sTAYHZAiLweL3Ehk7BRYub6riHAH3EfvBK8Im5wJdoASOCvFYleuOe57nxJawfJpz1KhynY4_ODML9c83jxaitahom_4S9C1cxUWK0JD0-mK0mwc3fuXs1UfDsIuqdWShfrpr16aq00II1kgmcy7aF4TnU12xqO8i9cykuTab-kd1bZmLOh_LJDpg-oF4SyU_Sou-C42ul9bQ5g2NnGTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079a967bc2.mp4?token=RPrxvlns0Vc37M34OgmfMjmmRPEubxD8TF640CdtmJblx99uQiWc7G2TwYQ9hlI4n9aee0iXQj9ZGGGilThwOjCJPrrAKnsyE0d1Q8LR-Mk2aXDFoubKdA2796HNKfcVnVvnUsAJD9jur_LaoEBlk6HaZrrRUByk4gumnirRGOCK4nmREpfRLQ1fxUaVzzMiA5g9i4IXtiScVlcsfnnouxLG-xZUr783qjmQlGACKytMxtI-YB5nshynt7SMf-OImEpiMvsz8TmBWztw8OEN78Fq4vWygyNCT270mp3ld0POH_ENb3nEh3UeLcacr_A84TNI3_IHBmbeK4iqQ0qyeKChpW9D7EaPWuN_9xmZNv2gx6T6FSpU0YA3bO4kfNtFXxAYGwYbH-RGDuFEr4PCjtQr32bmgT3NKXezRCyOT6wkjIK3_az1mMvWDcCDCpRdqUsILe3zpBeZl21MZlXE3sTAYHZAiLweL3Ehk7BRYub6riHAH3EfvBK8Im5wJdoASOCvFYleuOe57nxJawfJpz1KhynY4_ODML9c83jxaitahom_4S9C1cxUWK0JD0-mK0mwc3fuXs1UfDsIuqdWShfrpr16aq00II1kgmcy7aF4TnU12xqO8i9cykuTab-kd1bZmLOh_LJDpg-oF4SyU_Sou-C42ul9bQ5g2NnGTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تشعل سماء عَمان وقاعدة موفق السلطي الأمريكية تحت غضب نيران الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85954" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/85953" target="_blank">📅 01:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فقط للتنويه
وقف إطلاق النار كان من جانب امريكا وليس من جانب ايران ؛ بمعنى ايران لا تكسر الهدنة ؛ امريكا هي لوحدها قررت وقف إطلاق النار بعد ١٣ جولة ، و بسبب العوز الصاروخي والوضع الماساوي للقواعد في الكويت والبحرين والأردن وغلق باب المندب من قبل أنصار الله في اليمن وارتفاع اسعار الوقود
سنرّكع العدو</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85952" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ecc7e77f.mp4?token=ZTPsrWiZVeFPlwM1Ok4ERTxnMm3m5QqxL7i83iiPDLqt5mtdpjnx6iuG3Yvr9ZugfFRnUU80nfeAE8tD_Liq1WDDrArztEhK7R1sWiDvFtmuwpgTvN_XynRPcbpz-GYYxIezDFT9irhBiPfzJxrVt1CxSrBj3KXgTPkjKAhvkY_mz7dpNYXu6sluhvfHO9iwbffYffu0Jg2_7E9iI-Rmb_soJ9BSwOdKPkN_bDrf4A6hmBtTHPkblEHQDswa0mxkJsfUhgyDoi-IK-ic7XNM11eC1DVOZi5a5ODOr8_QUEOna1N9P3Ulyp8DSoK2hnyvQ7OrzAC0wPyrIunq2l1Hyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ecc7e77f.mp4?token=ZTPsrWiZVeFPlwM1Ok4ERTxnMm3m5QqxL7i83iiPDLqt5mtdpjnx6iuG3Yvr9ZugfFRnUU80nfeAE8tD_Liq1WDDrArztEhK7R1sWiDvFtmuwpgTvN_XynRPcbpz-GYYxIezDFT9irhBiPfzJxrVt1CxSrBj3KXgTPkjKAhvkY_mz7dpNYXu6sluhvfHO9iwbffYffu0Jg2_7E9iI-Rmb_soJ9BSwOdKPkN_bDrf4A6hmBtTHPkblEHQDswa0mxkJsfUhgyDoi-IK-ic7XNM11eC1DVOZi5a5ODOr8_QUEOna1N9P3Ulyp8DSoK2hnyvQ7OrzAC0wPyrIunq2l1Hyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في أجواء قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85950" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/624386482d.mp4?token=MGDEB7o8OSe0Q_aa1xUEcte5IqQc7JVCKao_5GVCtzTPQHGgmWTn9hg-jNqBVivIIdKUYcq_XknLG954m-dPrFgx44Oos0wDT8kCehjxHXw6yJLo989HV1h6X3BcjJMYOuOQwAULLpNXBEh5_fzJnMP0gqw5led9RKzOWgxFxK1NQ2Seh4ZEqxOyh1E7kQBbug6aBEasxCEWUkaGkfbuPcMZMiCuIDO2-gt0Rmi0XSh_oifPZyew2qOGbs2ALTlCK-YN3cyCo4INm8B-j0HZrb68PwbeMvXG1IevNwIk3CesQpcL6gfvc5nQm5NFh6n6fO3tjMd1t3zDWMyHkwuxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/624386482d.mp4?token=MGDEB7o8OSe0Q_aa1xUEcte5IqQc7JVCKao_5GVCtzTPQHGgmWTn9hg-jNqBVivIIdKUYcq_XknLG954m-dPrFgx44Oos0wDT8kCehjxHXw6yJLo989HV1h6X3BcjJMYOuOQwAULLpNXBEh5_fzJnMP0gqw5led9RKzOWgxFxK1NQ2Seh4ZEqxOyh1E7kQBbug6aBEasxCEWUkaGkfbuPcMZMiCuIDO2-gt0Rmi0XSh_oifPZyew2qOGbs2ALTlCK-YN3cyCo4INm8B-j0HZrb68PwbeMvXG1IevNwIk3CesQpcL6gfvc5nQm5NFh6n6fO3tjMd1t3zDWMyHkwuxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85949" target="_blank">📅 01:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/85948" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/85947" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4be504ac0.mp4?token=owCfO-HVH8T6da4Mx28GJ7f8AVqb4kOJO3RCmLwSJq06Q04sCgm963Hu9aVQP4C5dSVx2dfQmtP7J10kSworpmAg-KAcXYMs78wQwxxj4sO9VITOrvwrhjCZxwuSIrg6o-YV56TfljvqPkruNES71YF9vZHZ52Ru-s2zPKEYmhKZ6ga2GzcZVRw-CCmBRVTJ6lfvBc_PLAGNX1-igEGH24grP8Hb7AO2I2X9-tgrwfpBhFXNpsaPJ4YQ3xcU3u_ccNfkP1EPytPvmuTN1Ial8BRuS1WMlh9fmvYnGhLFsCAuZOZplPcG4ahcvSOpLHTP9vTUu34ZpX83wh2sImUJBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4be504ac0.mp4?token=owCfO-HVH8T6da4Mx28GJ7f8AVqb4kOJO3RCmLwSJq06Q04sCgm963Hu9aVQP4C5dSVx2dfQmtP7J10kSworpmAg-KAcXYMs78wQwxxj4sO9VITOrvwrhjCZxwuSIrg6o-YV56TfljvqPkruNES71YF9vZHZ52Ru-s2zPKEYmhKZ6ga2GzcZVRw-CCmBRVTJ6lfvBc_PLAGNX1-igEGH24grP8Hb7AO2I2X9-tgrwfpBhFXNpsaPJ4YQ3xcU3u_ccNfkP1EPytPvmuTN1Ial8BRuS1WMlh9fmvYnGhLFsCAuZOZplPcG4ahcvSOpLHTP9vTUu34ZpX83wh2sImUJBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/85946" target="_blank">📅 01:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed59912d11.mp4?token=Po9RDDefv5nw5HUV58wguyZ7RkssdXDxl2alLRhxFjmbi5rpGaZeO70i6QVJl9Ib5xjYJckp-nKTTlX0SV4RMI57fXxED6_9OKmSp07yXs4jiq4rSbDi53-dXkch90GbcldeyMfPzxgg4bIOk6ol5UYYQFKk5B9Q3AkAQU3W7JCoeMDHzWec001BHbRNkfbTPwrUndJ9FMxTerbMQB6_oWD4kf9iDQFwepAHLU0ve8fCY235Iue-1l5-0M-SyIvzRpu34AGsZ3vu5I0Zi9Ta4TBBGZUopSpf5JWYxtbmlkmNY3jkJUvOeI60Xq3ObwidQTiL-Azqxj9eF1fQ1U6C9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed59912d11.mp4?token=Po9RDDefv5nw5HUV58wguyZ7RkssdXDxl2alLRhxFjmbi5rpGaZeO70i6QVJl9Ib5xjYJckp-nKTTlX0SV4RMI57fXxED6_9OKmSp07yXs4jiq4rSbDi53-dXkch90GbcldeyMfPzxgg4bIOk6ol5UYYQFKk5B9Q3AkAQU3W7JCoeMDHzWec001BHbRNkfbTPwrUndJ9FMxTerbMQB6_oWD4kf9iDQFwepAHLU0ve8fCY235Iue-1l5-0M-SyIvzRpu34AGsZ3vu5I0Zi9Ta4TBBGZUopSpf5JWYxtbmlkmNY3jkJUvOeI60Xq3ObwidQTiL-Azqxj9eF1fQ1U6C9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/85945" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d615425b.mp4?token=wCaKJyFmiyn2CJ_eCg-9IPKspE8LOF1uSSW06K5SSyAcN0epCkRe-yKQxyLxQINCBxk1vi1sU0rUFB30mGPKe2r9GxOJjaSI59OhEwp-y-4F_mVTNxHbWCpHDX_UAM-ywh6vXq_tFKtd5yxW2S1KtHgDt6W9Zs3WqcrDwM0Gw3ZX0wjeq3rudI70RvTarnMdiFdzOaoWWbz1YitC7O4fzvd_bCOpez3lXcidW2uKIvH1iUjOb_r27agBcHty5mMSVOO-s3anrPpZQsksGmaAmAPc0m61rxqDhvTMWTqRljJtxV-A5Nb8XowKZQhVtkTUte38eSrpHN0PZGDtNFsnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d615425b.mp4?token=wCaKJyFmiyn2CJ_eCg-9IPKspE8LOF1uSSW06K5SSyAcN0epCkRe-yKQxyLxQINCBxk1vi1sU0rUFB30mGPKe2r9GxOJjaSI59OhEwp-y-4F_mVTNxHbWCpHDX_UAM-ywh6vXq_tFKtd5yxW2S1KtHgDt6W9Zs3WqcrDwM0Gw3ZX0wjeq3rudI70RvTarnMdiFdzOaoWWbz1YitC7O4fzvd_bCOpez3lXcidW2uKIvH1iUjOb_r27agBcHty5mMSVOO-s3anrPpZQsksGmaAmAPc0m61rxqDhvTMWTqRljJtxV-A5Nb8XowKZQhVtkTUte38eSrpHN0PZGDtNFsnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة وسط تفعيل منظومة الباتريوت بسماء الأردن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/85944" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123326eeb8.mp4?token=RGPOUnep_jIqpTJlCR_eeii9m92sFe81U61Gzz-WyMrMJMPmz-1D_VsDsawhrUqkhmYrLCICyalqZ0bfMX21o-aaOEEu-Z5KiCtYkJYIt9sh4yv_2HUDDZeKYDP7UGSQgEriVZvsgIbssSmv3Ga8HvbuDBaMH6vSuHYSqJBVbxhKhO5Z3gxtWnjxmN23FiZVovIb1P9mUkSmVeuVI1FTgFDJPAD9Znad7iuf7B_7m3ftLwRwsnXnLpFUksHO970rZGqg4ad4bnDldYskCZJJr2K8H42ZkLd6LEAIpQHnLYuEtAnhZ2Tr9XneOCLGzHsjQ3ezW4I6nnsAJM0yo1ma7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123326eeb8.mp4?token=RGPOUnep_jIqpTJlCR_eeii9m92sFe81U61Gzz-WyMrMJMPmz-1D_VsDsawhrUqkhmYrLCICyalqZ0bfMX21o-aaOEEu-Z5KiCtYkJYIt9sh4yv_2HUDDZeKYDP7UGSQgEriVZvsgIbssSmv3Ga8HvbuDBaMH6vSuHYSqJBVbxhKhO5Z3gxtWnjxmN23FiZVovIb1P9mUkSmVeuVI1FTgFDJPAD9Znad7iuf7B_7m3ftLwRwsnXnLpFUksHO970rZGqg4ad4bnDldYskCZJJr2K8H42ZkLd6LEAIpQHnLYuEtAnhZ2Tr9XneOCLGzHsjQ3ezW4I6nnsAJM0yo1ma7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات الدفاع الجوي الأمريكي بصد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/85943" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d59bfa47d.mp4?token=t_-MjLAuRQc9o0oNmD8p4bdrQyJ8jWB7tIFj8zTBtUrwwRlMn44ednY_Fv69HSG0lgJcNjbXJd1B7rVSptNkhQx0haTqEvT5kuW6qwuGM9guvQrApJZTQkXCPXI_quWkAtc6F1oDmnVuHFOHE-LaAQyZ-h9CHW6azBUJr-0Dmw13KvxTwXCi7IebEdju4QXorvVRIuGKUfbB6DtaUQdAa9XjTtDYIlOcDna7A87zaRXZBckNg9yOMQKUAg_hd1pBc4HRDTFJJzmG7r9v8X4Z6zQ_1P_pEepdlzURg08SiVWv7lnzAn_J8-hSrhCOcUZng-PZeEdJWnvy7y4iMUD0CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d59bfa47d.mp4?token=t_-MjLAuRQc9o0oNmD8p4bdrQyJ8jWB7tIFj8zTBtUrwwRlMn44ednY_Fv69HSG0lgJcNjbXJd1B7rVSptNkhQx0haTqEvT5kuW6qwuGM9guvQrApJZTQkXCPXI_quWkAtc6F1oDmnVuHFOHE-LaAQyZ-h9CHW6azBUJr-0Dmw13KvxTwXCi7IebEdju4QXorvVRIuGKUfbB6DtaUQdAa9XjTtDYIlOcDna7A87zaRXZBckNg9yOMQKUAg_hd1pBc4HRDTFJJzmG7r9v8X4Z6zQ_1P_pEepdlzURg08SiVWv7lnzAn_J8-hSrhCOcUZng-PZeEdJWnvy7y4iMUD0CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات الدفاع الجوي الأمريكي بصد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/85942" target="_blank">📅 01:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85939">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7au9_HWHEjakldjvbnRxsWzv2CaIhH9SoRjeGzhKd8vlUrzfICCq_Wv3fAT0jIdJXQSb9eX3EYNrZZfaN1q7e0LrLC6pquTflWJSB2CHJRSuKfVZFrpJ_L1rBE9TsJ2mijucGAIf65zQ6ymcyaZ7U01_PhCoFJ_AdEWw5jBchD2ogMCIP3L1gaNYME6FXnqWlVzY6g6PDJL_MG-D9Rq6hS5vFvfG-vjXbGDp5ZvsfO9WsgUqilNtO0mzekPjkHJTNZtekpmE4Jm2Va8VYIWCOKSygG9dTiYZryENYHAtIPZP2reXwDjY5265xV1YuWMw6mFa1WkwASGvEZF_lBF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRCfjBFKgVyGM9FrTXt0Hu10k951zQjjNKpitm2cSYSz6vGw5lwS6kIZqWQRU9a40welUyc5K4fCaW4NfQzLolyJ-qenM8P0ukc4wnV_Eo9JC5OugY9hIpUbhO-ISEI47S1vRnXO-Ur4bqVhMRKSGeLca39YNQhfqMOVZx5qZOxellZKYQYMTArGUS7CAz20ZaetKD7kHbPF-OHZ0AfdVbAj3ud0a6QNRmCo4pmObsXdrcKu9KMQRHURyBUlneNcFBStTku0g-7QeZenyC8RIwbKB1HMdPxmVPxutzEG_72Xk2M-51HO0_qYONcpqcHLv_XWMTf9UhNVOO60NEOR1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=PJD6-GY-wsE0RBfTy1z07XqmXvid0603IpdD4bwzCvMNxr-bhfM9w7QoF1a7d9PBMa93WTYER-5USrUenh3HzuAGaScaYGcPGaT3ziPhlD8knjdotxf-b1-w8rF_b42zrhB6LLORxMDbx44p_OCmQ5FDQtgYhaYN0zVD4U8J9gKuhFaz9qbLCBTxTdeGdUToV7v6Jvqiv5nLZbh9SumvzlyUAji54ipzQprMlm4tUnxFt3cVGmP6svh6FDUEJ0Uthe4q27tPH0MdUAP6Ld7Cx8Sat1akrc9zDDLCnB_NEJSwUDLtCRw0Xr1bSn_9jlA7N4OFLrjBd3-6ZhNvf4IygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=PJD6-GY-wsE0RBfTy1z07XqmXvid0603IpdD4bwzCvMNxr-bhfM9w7QoF1a7d9PBMa93WTYER-5USrUenh3HzuAGaScaYGcPGaT3ziPhlD8knjdotxf-b1-w8rF_b42zrhB6LLORxMDbx44p_OCmQ5FDQtgYhaYN0zVD4U8J9gKuhFaz9qbLCBTxTdeGdUToV7v6Jvqiv5nLZbh9SumvzlyUAji54ipzQprMlm4tUnxFt3cVGmP6svh6FDUEJ0Uthe4q27tPH0MdUAP6Ld7Cx8Sat1akrc9zDDLCnB_NEJSwUDLtCRw0Xr1bSn_9jlA7N4OFLrjBd3-6ZhNvf4IygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء الأردن</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/85939" target="_blank">📅 01:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85938">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=jpvPIopzRr91kvQoj9ky46XJ8_ITfWN33s68BlA2YSW8KGZPJUEwiueY9Ywj0gbOFZmnbZdbHA0p1NCiY-OaOZDSOSWfIdHdaBOldEK97687wELz6MsmDOt_zIRwTsMcYQbtqIVSYK59eEFKDDd8BBSiQk00gUGQgWI1adtE066ci6uiqlbgvf8ZAEC1kjobSWbg-VFineJefn-f_UbGKW7K53fyJQxSxpLSndqnRlOweIYerK-_AnX_Py5yEUwpqnB905IBXgXEKsYymBTVegr2vtG_orveAsAS5VeCJBBoJ5VN35mCdPFB4zUGsmSiFEKfB6hRsNRXrlHha_Bx5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=jpvPIopzRr91kvQoj9ky46XJ8_ITfWN33s68BlA2YSW8KGZPJUEwiueY9Ywj0gbOFZmnbZdbHA0p1NCiY-OaOZDSOSWfIdHdaBOldEK97687wELz6MsmDOt_zIRwTsMcYQbtqIVSYK59eEFKDDd8BBSiQk00gUGQgWI1adtE066ci6uiqlbgvf8ZAEC1kjobSWbg-VFineJefn-f_UbGKW7K53fyJQxSxpLSndqnRlOweIYerK-_AnX_Py5yEUwpqnB905IBXgXEKsYymBTVegr2vtG_orveAsAS5VeCJBBoJ5VN35mCdPFB4zUGsmSiFEKfB6hRsNRXrlHha_Bx5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الأردن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85938" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85937">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تفعيل منظومة الباتريوت في سماء الأردن</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85937" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebfe400c9.mp4?token=USu4HXXGLQ8pfJ9qaxiuS476qYhePpcQ1N9-VW4QdU8JSQDnTPiQQTmBY2UDUKLvAS2sLJpG1ia3ELYTeTPwBG0ayOqxd8XL4AAUz1grFZAIY6ayLpcCWqitc8jryZNQ_spWwPDff3uSGthzosoBncL5yUgxgB6HGWmWrfsovvHEJqunLWQAih79hxdKYlKJCgY_ebAy6aSAUxf73KrTvVWmoqxPfhqnZkiMFZEcGyaMkgUiKO7h6Yef-SEgYaHA5dZof09pDMXhc7mAeoZj7fCK94iGzXJVK87lcSB8DLIZFDEJwi2QlgNUG7s9Ob3cd5HJzh3prsL25zhlxMM_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebfe400c9.mp4?token=USu4HXXGLQ8pfJ9qaxiuS476qYhePpcQ1N9-VW4QdU8JSQDnTPiQQTmBY2UDUKLvAS2sLJpG1ia3ELYTeTPwBG0ayOqxd8XL4AAUz1grFZAIY6ayLpcCWqitc8jryZNQ_spWwPDff3uSGthzosoBncL5yUgxgB6HGWmWrfsovvHEJqunLWQAih79hxdKYlKJCgY_ebAy6aSAUxf73KrTvVWmoqxPfhqnZkiMFZEcGyaMkgUiKO7h6Yef-SEgYaHA5dZof09pDMXhc7mAeoZj7fCK94iGzXJVK87lcSB8DLIZFDEJwi2QlgNUG7s9Ob3cd5HJzh3prsL25zhlxMM_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من إطلاق صواريخ في سماء إيران الإسلامية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85936" target="_blank">📅 01:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd4HLHL4OHzNgovJEZN1SukCo_RhVo50OpngvqCcnwRKQuh-77k2Q68CY_comTK0TbN0b-Ye8A4mRrhzbUHyxcnjjO0Mf7yJuUpIPzvF4mopyZlGPbQ-RqcOp-WKbEXed1V4j0V4dNAfep4MOuJB1CLAhrCKG3GbKIVGtu0mkbc9HQmokNzrxq0mRXlYeZSrqTyxKK0chUon6Hi5wfONFh7aqt_PwODNkdbT3m3yYMBSDytFmRqF89OrAFyu9-5T5jaYdwOHWEsibpks-BIk1gs2ILgfccg-5wBM8LYdZ5vbq32B3GI8QCB60RFLYIbKcvetFu2aD9plfgeWw1puLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85935" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الصواريخ الايرانية تكشف الزوجة الثانية...  سيدة أردنية تكشف خيانة زوجها أثناء قصف قاعدة موفق السلطي بعدما فضحت تنبيهات هاتف ثان كان يخفيه في الخزانة ويستخدمه للتواصل مع زوجته الثانية.  والعباس القصة حقيقية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85934" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85933" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بوليتيكو: ترفض الدول الأوروبية المتحالفة دعم دورية بحرية تقودها الولايات المتحدة في مضيق هرمز، حتى يتم التأكد من أن الهدنة مع إيران ستستمر.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85932" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YllfjPNk_ETTw2N0RIAoszXIDDyrORowbebp6d30vkTBwsXp4fG7lqGnJnih1iHVjJGb6-3oza-eBa_77EBg9ikjyQ8EuCRSi2hrMo6U3ngS9lDIq5w1I_aODEgjrN5f5jXzYvi8-INAfw-Xj1T-OLuoaUTYkpJ3o2Va0bLYgbD08HeOFCTY-dI7bgI7_xcpTAXST1WrRUOPSj98uZYZC64JMZtD7c-59jOdyxn7vzZ1P6IfTJ5Tw-c8RVOCGKixEUzLIPVIrbTrwX9y1-L6OVe6P_Qf8cs558xtO4U5lVGRlhKSlKOW-6k2nNAv098w0F1kfr3ozeBRJ-aMQ0Vnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7LWcPAIEBon6f2un2w4oClyAtFj03OF0Us1rvc1YJhVs0swHFF1V--sVbzXXwBKtFssZRQpN47xVBOSgF1VjLJUoyFL7WlswBWISoaKnS1GN37SgL6B33heigN6XuJNbQJH-DTun7HEXEaBP1S8YtO1vviSQBe5LE1nAVehmZmuzdhTtKwNiuTHL6un1N0cuPtYaXTn_hcsyhX15nd9ZO4HQLYrY9OKWC4iWmXVyzZAmDqSHMIxGBvsKvL6X2rhu2XmXx6YFv2c_zkO5sqWNBlBcdFyBguSLCGpW_E8OKCaAiC_jPjKtObQYsLh5XgeLSvwgiSjdqbk12eirCOiNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد حصرية لنايا... مراسلتنا الميدانية من المملكة العربية السعودية توثق تصاعد أعمدة الدخان من محافظة البقيق، عقب استهدافها بصواريخ أنصار الله في اليمن.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85930" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85928">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHRmaOTUif9yZezAy0mfEx38Suxz1KSsshvH0fT6kU1CuTY4OvdOorlZ_vX9bthJKMOmdiIJ_AIt_7mAVxFq8LmIiZDfVRZXhgP5hHABabE8MR1wa51--uzxekyictxee29mEKquFz3Jz3wzqoHX4Zk7PK4aQSd3Y45qC_fFCZ3zyJIW0HwDrtHoEWV1JXsxGEo5aHckrHkvoWUIxGpPlzOBB9CgwQUrkD8BR0EQNE1m3sBZEjj6UPoqVDDLX3WCHKje8jcylHCRyVDsOFue0GxYVdYKe2Me7Rf6DrWzNqXW3aOSQwFZgYZsqQDQhzClSfKfrmY9KKZMmbF-Ec0b_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhSIB9UsvaNytjkidcLh6efqdj5WddTUqmhg6Sh1pjIeawTcYLxJZuy7xMgXoTNUhqJd6XmsuEch52v_YoFk5RzhQmcX1uachvRjbe95OQWH1VRuIcBbJN8cGZlvT4vXB_xXOM0Z2IZAe7efUIcwONOzbUAlnfBP8TcID7iot1pnxZCxyGXSPf353jEpLHe3pzgzm0gqR6q_ifb0gFbUP22MRC3_2ssxdzvU-HqGR_wfUmZVEBD6hZecbAEqdCPMPV7uG4f10y6M5GChoAPxVVtGeaztcivi6XoYj1CGTavFpJeKa5e38sje-OhVVdTyJsVNXvQoEbgs1cSj8H0q3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
حدث مجهول في منشآت لتسييل وتصدير الغاز بمنطقة رأس لفان الصناعية شمالي دولة قطر يوم أمس أدى إلى توقفها عن العمل بشكل تام.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/85928" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85927">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04839e658d.mp4?token=TtVaBbpOl4cOsu8aqk420nlrMCMcQPYmqZiX44E1He33ieAzKlvUQy3jXFLCvTaxFSwh8PbiTySb5lvO9whrfOM6aj4AEQoiKgO04tmZhJ2f803JIwwAZkAK-ilVxWBQnsyYD0dXyTl8-VPkEJU6WJ6xFk1-w8_3wXj7t8e1qbCqLWkPhrZm53fOz6F2_QRCn3KyKw-aCvkyIuqJSG9rIGNDiue24Fc1RWcYqdc_Uh9TXAurIc_XXVhek0Fh0JcGwyBWNQFWUOlOHm-xLU-Tj9Uf9SUBx1cmN3fEzsr87B3fXqE_K6zJEGh00c0tSG6XCm0Hd_dJb6f25tojA5N7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04839e658d.mp4?token=TtVaBbpOl4cOsu8aqk420nlrMCMcQPYmqZiX44E1He33ieAzKlvUQy3jXFLCvTaxFSwh8PbiTySb5lvO9whrfOM6aj4AEQoiKgO04tmZhJ2f803JIwwAZkAK-ilVxWBQnsyYD0dXyTl8-VPkEJU6WJ6xFk1-w8_3wXj7t8e1qbCqLWkPhrZm53fOz6F2_QRCn3KyKw-aCvkyIuqJSG9rIGNDiue24Fc1RWcYqdc_Uh9TXAurIc_XXVhek0Fh0JcGwyBWNQFWUOlOHm-xLU-Tj9Uf9SUBx1cmN3fEzsr87B3fXqE_K6zJEGh00c0tSG6XCm0Hd_dJb6f25tojA5N7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
🇮🇷
وزير الطاقة الإسرائيلي، إيلي كوهين:
أعتقد أن العامل الوحيد الذي دفع الرئيس ترامب إلى توقيع الاتفاق مع إيران هو مسألة أسعار النفط، وتأثيرها على سوق الأسهم، وتأثيرها على الاقتصاد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85927" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85926">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الصواريخ الايرانية تكشف الزوجة الثانية...
سيدة أردنية تكشف خيانة زوجها أثناء قصف قاعدة موفق السلطي بعدما فضحت تنبيهات هاتف ثان كان يخفيه في الخزانة ويستخدمه للتواصل مع زوجته الثانية.
والعباس القصة حقيقية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85926" target="_blank">📅 23:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ستة انفجارات سمعت بوضوح قرب مؤسسات نفطية و غازية دون تفعيل صافرات الإنذار بالمنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85925" target="_blank">📅 23:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل قضاء كوية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85924" target="_blank">📅 23:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ستة انفجارات سمعت بوضوح قرب مؤسسات نفطية و غازية دون تفعيل صافرات الإنذار بالمنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85923" target="_blank">📅 23:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ستة انفجارات سمعت بوضوح قرب مؤسسات نفطية و غازية دون تفعيل صافرات الإنذار بالمنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/85921" target="_blank">📅 23:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCOvfEBh8EGVNo1xYr7Qc1nby5uDkwuxxhBGZwEjVTf2l0xE-OlQwaR-ps40q1hg8B1TtahQodyDfi1_VchPQ5FVWtkvOuaIegwFeClGWBkvWdNA_3tElKFIMcUTSiaoT827fK4PQtae_Vy7sTslzX7kzmWrKMEeCsPx9i0iESTMZxamBFBtjm0AGwqoM2jNa1yOHah9EuyOV5P7uasBc-q5QYrCtWyocYfMUAu5QWWObdiwrLvtYWTEWyRjAoVIXt1cuMqx_u_Xl9BT3NwjobsYALvEr95NEUGSQnKJfMOXyrkemztwdq9iEilzBZtNVbD9DEIminRIfFVzTa79aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري استهداف سفينة في البحر الاحمر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85920" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85919">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85919" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85918">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85918" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85917">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حدث بحري
استهداف سفينة في البحر الاحمر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85917" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85916">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">السعودية تعترف</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85916" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85915" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85914">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85914" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85913">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91015376f1.mp4?token=QzqxxVD9YMsl0LkNFp5vMZ9VnnxAai3k6-UDZpQbTCbZ_Ha8obMySo6Uj8ADlJ8ajACybVbac8JZh7EKMWMhAyHrAHxqfJ_FZXsUYQ6Yxgn7DeLGSTI8hRLR0okjgiq7DeMrY9p0GDW4H_x2mkkTcfm3fFdx4S53ZzwgjLuNpZQ9ZhMxpXy7J_5CFnzO2ay_MM5pqb_VUzHUpr85-GQDK-4tDC3JwjI2xaRRCTnXzJFzKMWJyPuDrX5q_Ue92Bvb3WvCT6Kfr8L_dOi79Mbtl0P8P4xhd_Qo3tC9b6A0ZqALutttbqgOd89xKI8Tw8ILS8bSAKv_NFIuVM3Aey-eqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91015376f1.mp4?token=QzqxxVD9YMsl0LkNFp5vMZ9VnnxAai3k6-UDZpQbTCbZ_Ha8obMySo6Uj8ADlJ8ajACybVbac8JZh7EKMWMhAyHrAHxqfJ_FZXsUYQ6Yxgn7DeLGSTI8hRLR0okjgiq7DeMrY9p0GDW4H_x2mkkTcfm3fFdx4S53ZzwgjLuNpZQ9ZhMxpXy7J_5CFnzO2ay_MM5pqb_VUzHUpr85-GQDK-4tDC3JwjI2xaRRCTnXzJFzKMWJyPuDrX5q_Ue92Bvb3WvCT6Kfr8L_dOi79Mbtl0P8P4xhd_Qo3tC9b6A0ZqALutttbqgOd89xKI8Tw8ILS8bSAKv_NFIuVM3Aey-eqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
النيران تشتعل من قاعدة الاحتلال الاميركي بمحافظة اربيل شمالي العراق عقب استهدافها بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85913" target="_blank">📅 22:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85912">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة على اثر اطلاق صاروخ.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85912" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85911">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة على اثر اطلاق صاروخ.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85911" target="_blank">📅 22:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85910">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0ebc773e.mp4?token=JUTcSMnnli0IKSRYcMUW1Kg5TNKFHSqKwb020CCU0BxmY7mqnDtLy5hrvzw_-4KyXGYcsaIrCzSkNUkVUdCD0AtSKS04TB9w-G6m9imrW195jn8vTwMs53FyRP0zqaIplY-UhXeoO6UP0C1ODduktKLWGnucISdSfxYCE-xq0lWvMcbYUGc5NEm7Pi8rd5baz_EbLCwwugH3ffUZZIKf26YiDnFdMqXEJCPCMfDzJecjxhhcPaWHpj7DQVc9qjxVBngQwt8nwDDCdIQWkxMxH29y1H6sJfbUevsX00EXZN0-F1nxHk9rlLu-K2Dhdb7Ebeze0u2I4RVzALM5Gkuy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0ebc773e.mp4?token=JUTcSMnnli0IKSRYcMUW1Kg5TNKFHSqKwb020CCU0BxmY7mqnDtLy5hrvzw_-4KyXGYcsaIrCzSkNUkVUdCD0AtSKS04TB9w-G6m9imrW195jn8vTwMs53FyRP0zqaIplY-UhXeoO6UP0C1ODduktKLWGnucISdSfxYCE-xq0lWvMcbYUGc5NEm7Pi8rd5baz_EbLCwwugH3ffUZZIKf26YiDnFdMqXEJCPCMfDzJecjxhhcPaWHpj7DQVc9qjxVBngQwt8nwDDCdIQWkxMxH29y1H6sJfbUevsX00EXZN0-F1nxHk9rlLu-K2Dhdb7Ebeze0u2I4RVzALM5Gkuy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان قرب قاعدة الحرير في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85910" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85909">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان قرب قاعدة الحرير في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85909" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85908">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85908" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85907">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyy4WsZ7tIrwMDOGdeLd5qzM3m05ADxGhDq6ZrS6sTTA1o__i0BQP98WybyHLTpg1MbbPt290C82ZYgUsF8SZC-n6XUb5VSCE8Vkjaf9KjfoK5w7If9zc0ZzwMx76FpzxQdLSQpGWyaxneSAKtk2klVYitjtmSC4oDx6zcSQq_dzk-imw0x-InXFhDXs41maH76T02E0WMoQw1sMG1Gl92BDutDNLvHR5-JR0qEzZyy6J3p34l7V6-JQBkfPKSRzs1_LYm3rA_SUBu1CETfUTueyDjo0GS4GqGEZhqKs-hG5OeQS-Xka13sUdKBIUUY8gtXKXtFmroPg-jeixpHF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
وزير الخارجية الأوكراني متخوفا
😆
: اتصلت بنظيري الإيراني لإجراء محادثة صريحة وشددت على أن هدفنا هو تجنب أي تصعيد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85907" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a504ea0426.mp4?token=kepUtw_r8ekAtu6tEce3TWqkd4bBZtduGx1Kw0Qfb7fvBmYWwa4qEkI1bG3lrkNacM9N39VXfLOgC8c2Cy9_vLSrR-hE8bhBb5uszzqDIiBc94ZkUEziiBuL-MOfvrXSjccKPLCVtXM9_2SLug1mdngkGBRpoPxQnCfTSDfUi1nANhCzZPtxuMPwB4qWHk-QFQ7yVDGsyTMT89IU1M8qKYheTu_gIwvCCfqwMzP59SkVLQ-t1WcGZI6crSv7sbgZ21_RJ1ngIgKKmRaLG69-5HGT2VTIpJEExw_uOcWHDK3aizosZrj87KO0kCdun0dRDBnQL92UZ1AALYYytUae3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a504ea0426.mp4?token=kepUtw_r8ekAtu6tEce3TWqkd4bBZtduGx1Kw0Qfb7fvBmYWwa4qEkI1bG3lrkNacM9N39VXfLOgC8c2Cy9_vLSrR-hE8bhBb5uszzqDIiBc94ZkUEziiBuL-MOfvrXSjccKPLCVtXM9_2SLug1mdngkGBRpoPxQnCfTSDfUi1nANhCzZPtxuMPwB4qWHk-QFQ7yVDGsyTMT89IU1M8qKYheTu_gIwvCCfqwMzP59SkVLQ-t1WcGZI6crSv7sbgZ21_RJ1ngIgKKmRaLG69-5HGT2VTIpJEExw_uOcWHDK3aizosZrj87KO0kCdun0dRDBnQL92UZ1AALYYytUae3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب يخوض معركة شرسة مع النعاس خلال مراسم العزاء لغراهام.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85906" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85905">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇱
العثور على جثة مجندة صهيونية في جنوب الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85905" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85902">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMykCnt9MUergqgfWgjmrLXFr6_NOqqx-2Jj48RJ-fpKvgoy8BzGr6JNm1Dc_xOpFGkkrqJfj-sLNiIMeXG55nysZMAI6Rj1PeVn6PN6Mux0SPjlkGECgqNADj0p2W4NGR3VZ5GMSMo1FCg7BVLHREL6PD_Jgj8-gGv6GlKEuFpUDRyEp7LW-q2CI1Ly-vO_NnCQ0dqopQLxvV6ycix8n6oiYSBZrnGAzCmGw9WF-MdLgorWAO_ZWiuOCprRsKCLBn1cjSyZiYMaF7Z-WuTmP_05zjrixX8NY41OMYnGmTRCHD74-5DtcKFLVf_MeAZ5jEPQfLbPom-gfgFmglL4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27343411e7.mp4?token=osF3Sf81K8p-xaS0N9pMwNM7qeiDGKCUaZAXwsLWy1FqxhzSmhbl06-5u52icLcog8qi8TAhVZNmhycwVtNWYk4TtJ1sM93XSz6gSu1qJ6hLm5O-7BwWyKf6gRDE-jJsuf9NswzKjJjTqgZAJJ4r6KX-9k9QUPzDRHgwaOOJEAxpctrBGtdM_y3-tPSUdkL0fY_htyFxCrw8cDqUxJh8Sn2Gh5Dt6q4Zq9ILdP6A6DtR3SrCqDr0VZ6Czp2bUYb_Gf8pX0Wjn8ZZJ6pgjimFHFYjCo2dp3N7o28dT1o0GVGIhTaCN5vKDo2DjBCmQKK_U-5xOqGcimuiLypAwnY_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27343411e7.mp4?token=osF3Sf81K8p-xaS0N9pMwNM7qeiDGKCUaZAXwsLWy1FqxhzSmhbl06-5u52icLcog8qi8TAhVZNmhycwVtNWYk4TtJ1sM93XSz6gSu1qJ6hLm5O-7BwWyKf6gRDE-jJsuf9NswzKjJjTqgZAJJ4r6KX-9k9QUPzDRHgwaOOJEAxpctrBGtdM_y3-tPSUdkL0fY_htyFxCrw8cDqUxJh8Sn2Gh5Dt6q4Zq9ILdP6A6DtR3SrCqDr0VZ6Czp2bUYb_Gf8pX0Wjn8ZZJ6pgjimFHFYjCo2dp3N7o28dT1o0GVGIhTaCN5vKDo2DjBCmQKK_U-5xOqGcimuiLypAwnY_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من الاقمار الاصناعية تظهر تدمير في محطة تحلية المياه المالحة وتوليد الطاقة بمدينة ينبع السعودية بعد القصف من قبل انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85902" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85901">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyvVMaiQumvjwp0AJcG4g52eHtc8xKc-BEG8GeAk9AI4yvdLyNTZ0iYB9pyY6LwORwuIk0TLIe1-BVICetCZJna3kwI6UeItjPNpRTpwcilfKDspUia_flyXitNd2YSRWhRhdDNrhpXjYHGyi6LithixgQbF-UeBJOzqxTQO9fImeVCnO2z2JKt3BFKQugtdv_1tyav2koWPsB4Ic01c11QaKmw7X8jQyD6s38VybrrEMBxAnkKykeiOa31FrsBjkC6JI8-Li7_NfoX14lsCJ_sJpvdyiP0krjt6yRc5LlerQ9MNjS98o_F_hIzt4ZtHz72ddKlqrbBKLKfQPDEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85901" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85900">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو:
اطلاق صاروخ اعتراضي من كريات شمونة حول هدف جوي مشبوه انطلق من جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85900" target="_blank">📅 21:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85899">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmliGkCMICWwlknxpiXvV7ydvv9ymE38rsphd4AYQqJxvC-7gZOz6mh19YDlI13HqiOjSZcFmnjdX1OvNTe-P8MiNC7PeXjbRHguyXiRMXkpYuhw4GOtmyHugTdN1Vnt7UKKxOPv6A0iU_yRMZlHCdjyZKTfJheyLKv-a2C00yP6VNrcx5xDEqs33QUX6ps5yrvttojkjS66Qv22NgDcR7YJCJdGHhcCFL41yK0JEFiZTNcPes_ZXipBQnUTDLJY_Glhh-i7GBQCrzfor5BLEEhxcsCfI46FBeAUpEG4ZpNSGO1SaFBZxKlOur8TkcD3F_PfVjCZPJWI_nLNVyFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85899" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85898">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cepD3fXpV8zir-1DGgsw3F9RcmcYGGGZLJXLV5U0Wxd8QFcVfsgyb7Vszt7jxYuCAiCfbVskaxxML04cG9F9t7bam7S0OhGlBP-RpO5Fb9B-Z7vrNODwNa8QDeC41A-bp1i31Zq2N-SAgnHRhx85RbbzjSv0zp1-AtlbC5QaqO2jVaFCVRovEmTPTxFQ9AWypVWYulLUPQeXC2ayYm3YVEp336d9sCwHeWUvcquCcRHCKedI5ly-WKICQZs87VMn8aUzMIbe1E2nF6M2tDUOFBN963m93at70MxeP5d3JY4FtYwF21KxpfyByOepnNuZ5x8gVs43_mhYucbcalQAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85898" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85897">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85897" target="_blank">📅 20:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
عراقجي:  أن العمل الانتهازي الذي انطلق من أوكرانيا لن يمر دون رد.  هاجم زيلينسكي سفينة تجارية إيرانية وقتل بحارًا. هذا العمل يُعد انتهاكًا صريحًا لميثاق الأمم المتحدة، ونُفذ بتحريض من إسرائيل لجرّ أوروبا إلى حرب معها.  خلال اتصالات هاتفية مع كايا كالاس،…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85896" target="_blank">📅 20:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5AS893n-WHiQ3s98OWsYBuVNn4rR3qUi-YaJKmR5pkwWYE5Vb3ZbOJTvX3qyShIo8CMXOEr4Taf-HFWHpD-MZQcF3YZyR_RfRzyNWR7YdH6Nwtq8teIB7E1Uf4OXBWaJO0rNYT0g7rpL_Ck0SHKZqGwib0tl3AkPRJZ-O-zYiCAkhAthWaYrzIzNBbjsQKAu97lcUgwh2aXc7Nqvjq6sI_CTRGja_nDUOGTLPmzb1r1YdHJIHuoMS049vBe19Uio4eH8xfxHBn0T7aL789AFSjFXbKlML44MbU7n-kXQ46fByZAz9PduCs298JX8NEsoc3wUWv-P1ouelkNa-uLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
(أمريكا، لا تثقي به)
شعارات على شاشات عرض متجولة نصبت امام البيت الابيض اثناء لقاء نتنياهو وترامب.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85895" target="_blank">📅 20:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇸🇦
مجلس الوزراء السعودي:
ندين اعتداء الميليشيات التابعة لإيران باليمن والعراق على منشآت نفطية وسفن بالبحر الأحمر.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85894" target="_blank">📅 20:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85893">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
وكالة أمن حكومة إقليم كردستان العراق:
خلال الأربع والعشرين ساعة الماضية، تعرضت خمس طائرات مسيرة لهجمات في كويا ومحيطها، وطائرة مسيرة أخرى لهجوم في شربازهر.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85893" target="_blank">📅 18:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGBcYMB7kdY-SV302MgAV36TaRfmHqm6lekEB70U8z1YcpoCOGdKs5WhwM8dqoaOi5D19fsmjQPo9PZ_wRTq2v_dThQEVN85Lytf-7xTr8l5ZmzVKGrOpnYza4ITzqvBJy2zoAJVANNzxO99mZyBm8CUzo6pq18moXUNx483gecGr6z92KoGEZfNICCV6ToCY74bS6DRXoczXI-ioYUl2Ayca6HL-jTAo7zM3PkMQjaw8etuXGm0yNQlvn00guiWNqHqE1Re94Sz_hu9pU-7EAallUA-FKPgSS7Cnduo7Xokh8OM_696csFbKx_rm-1f_r-zk2QwSGDvXh2YuW-XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس اسماعيل قاأني:
من المتوقع أن تتعلم الحكومة السعودية من سلوك أمريكا غير الحكيم والمكلف وأن تنهي الحصار المفروض على دولة مسلمة يبلغ عدد سكانها أكثر من 38 مليون نسمة.
إن توقعات المسلمين في جميع أنحاء العالم من المملكة العربية السعودية، التي تعتبر نفسها حامية الحرمين الشريفين، هي أنه بدلاً من مواصلة الحرب والضغط على أمة مسلمة مضطهدة، ينبغي عليها استخدام قوتها ومواردها لدعم الشعب الفلسطيني ومواجهة جرائم الكيان الصهيوني.
إن محاولة إنقاذ غزة المضطهدة مسألة شرف، وليس استمرار الحصار على الشعب اليمني المضطهد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/85892" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
🇺🇸
اذاعة جيش العدو: ترامب يقول قبل ساعات من لقائه بنتنياهو: "لا أحتاج إلى أن يقدم لي نتنياهو معلومات استخباراتية عن إيران، إنه سيقدمها لأنه يريد أن يبقى مشاركا في الحرب."</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85891" target="_blank">📅 18:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85890" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85889" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة الوقود متواصلة في محافظة أربيل باقليم كردستان شمالي العراق وسط استمرار طوابير المركبات أمام محطات التعبئة في ظل شكاوى المواطنين من صعوبة الحصول على الوقود وامتداد فترات الانتظار دون بوادر واضحة لانفراج الأزمة حتى الآن.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85888" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85887" target="_blank">📅 16:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
بسم الله الرحمن الرحيم
أعلن رئيس الولايات المتحدة، في أعقاب أعمال عدوانية وجهود متواصلة لزعزعة استقرار المنطقة، ما يلي:
‏سيتم دفع التعويضات من الأصول الإيرانية التي تم تجميدها عن الأضرار التي لحقت بالسفن التي تضررت خلال الحرب المفروضة على إيران، بسبب انعدام الأمن الذي خلقه الجيش الأمريكي، وانتهاكات الطرق غير القانونية وغير الآمنة في الجزء الجنوبي من مضيق هرمز.
‏وبينما نحذر الرئيس الأمريكي المجرم من عواقب هذا العمل غير القانوني، فإننا نعلن لجميع الشركات والدول التي ترحب باقتراح ترامب وتستخدم الأصول الإيرانية المجمدة تحت هذا الذريعة أنه من الآن فصاعدًا، لن تسمح القوات المسلحة للجمهورية الإسلامية الإيرانية لأي من سفنها بالمرور عبر مضيق هرمز.
‏ولا نصر إلا من الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85886" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/85885" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga-j2AEXXP00_v8SyAXQOQoaKs0y8fNzSk9GrnJ8lA-DxqtYViwb-wV7H6VVnO4INmAqcDO_OKKGjozTcREnM6X4Ht0u6ZdML_IaRyyM9hZQlAHBAhmNN_f99A9iZLjH-Lf1OjW8h2wHK8s1g8JQp0f4ayjenESBfPbre8kcNpkzE5LPiQdRwMQbNzEN0UNQJBi_YutMtadz3KOl6cbCqKl---KMJUTdX70ePDZQWCoSuRu_8s75qm66u2sseNspA_zfhokD98JLgXok_SkpekmLl0AidmddTcrY8MkeNJWfWUapB2a2ItLGQYUKGeljievv0lABuXUNtg-JkyLASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
کانال خبری ما در روبیکا و بله راه اندازی شد.
🔹
لینک کانال روبیکا:
rubika.ir/Naya_Fa
🔹
لینک کانال بله:
ble.ir/Naya_Fa
کانال سروش و ایتا به زودی ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85884" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrgkSBaapXRfG85lYa3i7YWWOJdE_EA6SDlmmyM91lrBmbHbrM8b1l9Fa6Iu4QFkGc2HgXiVM0LUfcMd4gleNyS9IEhcr5qm1t9cVpYSWZNEwCBJs-qsCqW3DtAFU6Zw2h-WHA4vCdC3-YRylzogyMGUg0J58BVmh_LqvNeq_esZkU23jTxjhAFxap8mB92SxYqbwrh6KnKvb-dtUBJuS7w8DhOquKjiMzRNlxp8VUdNGqC1Luze3bTMzig-Jn0fotUMxaMuNUxhOqTjgFaMNBvHL0qBvaLOCu9Rmqh1OFiYj2aqZ0AG5T2e72QSN_oDIaeuLBnKkoLmUYn4ZZ2yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85883" target="_blank">📅 16:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الأردن تعرضنا لهجوم بسبعين صاروخ و ٢٥ مسيرة خلال ١٦ يوم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85882" target="_blank">📅 16:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".  ‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث  ‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟  ‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85881" target="_blank">📅 16:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".
‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث
‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟
‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85880" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇰🇼
بسبب انقطاع التيار الكهربائي..
إغلاق بعض أجزاء مصفاة "الأزور" النفطية في الكويت والتي تبلغ طاقتها الإنتاجية 615,000 برميل يوميًا
الكويت تعورت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85879" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇯🇵
انفجار يهز المركز التجاري في اليابان وتسجيل عدة وفيات وفقدان اخرين على خلفية الزلزال الذي ضرب البلاد وانهيار المباني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85878" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية: إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل. ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85877" target="_blank">📅 15:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل.
ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما يشاء ويستهدف من أراد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85876" target="_blank">📅 15:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85873">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBvmc-Cz1bXKAQlwki-MOBdIGMpJNcorcgrddorFaTbuVUepgZM7CYplfpB_8zMSdtxAzbP18fvB4MFYc4vbaRomO9pBy3-_e1V4G3tqmr7KFzgiABbC31rWGotBSqG2QxjyGKzw1Z0-WFs0cNRVWwWbap6QBnRqFt_WE0_aLaAqD6oQZYCKD7tkbDNawnElycxQ0S4uCg9Z_cnZth5bsRR2dSI3wpuSnqk_CIY4Usq9VJX5l9jvvNHQJEwP8QiXNXJBUF5hTDpUX_fmDJlry_MrZr8XHlcSKztWhtDYFhLkPmG1j_DwPYkTcLMyLr0PMaj0o51fbqeZ-xWfwTcRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAtXbjTbTRSv9xtCtA9YUftP7NwqAlHYoWEU33zCUaoEhHbVJ01CjmXJEKN5FcxIOwuiuoeoD4eEL70LlQiVXg-Yukwl4nSrnWbZEu20LtWdm4OOhJUyHB0-qriQw0tOg0CaihYmCxOuddsOFS3EuQg9PQ3d_BpRO2cphXozGp0FBD8jLNys9oAqrShoA_b6LYn8nhF4MwFoGStrMJ4QLTUk75gTXGatM2tCG-tLAusN88LeK_oPU9178oTcfvQWyxR5caq3g6MJGCpieyHq1udjtNTag6WVsFZ9uq6IRQPsngiFqMD0XB-RRfiip-2w56Zkm7hvSJVMng-1u0Y0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5GSyDwjYnQ2gSlvCD4Piz1oylUHlWtLfTFh87ZoIAxOPHqLjXLGoMdZyP7RdCDShce1B6ZTopL4nLgxln7-wf-RjB1ARQmtm9A89ij4UdFip-okeOuQ3jJ17iO1oGSLa-8mS8O76Nt-ehDtBsmN8h_TQpno-T38Abi-TLKpUcPK6IAqYIQiXiraDgsYvvGMb6lj5MJN3hajOh9DdiTRBsZqJoCslfkFHBaVTDF9NVCSNQDmp5ODnJbHf4gCkLVydkKQXbKX_48AI0sLkYZqEMuFBeIRzQ_FRQtVLUhY3EIvkxO-Z0w5bYc6rbGzL2ldWBBy8vr7PceRW_mtubDdPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85873" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85872">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd6LQiIxrxwaDXbx0RErreSHA6a235IrbZKTdMh2TJfcG0qFxP8WWdzwXF1_rL1Lke7HBYEfwlHmNEAeYpW7z6KkDDLJZFqA4bAh-7mWUtB4EhvET45BmrH84F6ARs3GxUyeFX-Dt0ZbC5WUEY7sIHe5dnqWDtELIJoiZizjJQ4MfcV4OaSkHL0Ex-zU7MBcc3JC-TFPEYzrkHaJ3nHcUXU0J5igI9L2O4_9roeiJ4M302gLd_MNh3eWS3W-FrPlosRMLgGi8_VKUUBep8AfGMSFN341UsAmmV8_dHxsCDHt9xzg45N8UGuSYdPH7ShsDhiAaHfUPCwDV8xf0lw8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85872" target="_blank">📅 14:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85871">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شركة أرامكو السعودية تغلق مصفاة جازان للنفط التي تبلغ طاقتها الإنتاجية 400 ألف برميل يومياً عقب هجوم انصار الله قبل ايام.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85871" target="_blank">📅 14:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇱
وزير الشتات الإسرائيلي:
مشكلة إسرائيل الأساسية الآن هي سوريا خصوصا مع التمويل التركي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85870" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85869">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇩🇿
🇦🇪
الرئيس الجزائري يهاجم الامارات:
هناك دويلة كل ما تضع قدمها تسيل الدم ولدينا أدلة ولا نريد زيادة الطين بلة في العالم العربي لما يشهده من انشقاقات ولو غير ذلك لقطعنا العلاقات معها منذ زمن بعيد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85869" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85868">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزير الحرب الصهيوني المجرم كاتس متفاخرا: اليوم، لم يعد هناك حي "الشجاعية" في غزة، ولم يعد هناك مخيم "جباليا". كل تلك الأماكن لم تعد موجودة. لقد قال رئيس القيادة الجنوبية لي: "لا أرى أي منازل، بل أرى شاطئ البحر." لقد دمرنا غزة. في غزة، نحن ندمر ليس فقط ما هو…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85868" target="_blank">📅 13:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85867">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزير الحرب الصهيوني كاتس: تم تكليف "الشاباك" لحماية نتنياهو والقيادة السياسية والعسكرية الإسرائيلية من التهديد الايراني الخطير.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85867" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85866">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني يهاجم اردوغان: نحن لسنا الإمبراطورية المسيحية المتهاوية. القدس ليست القسطنطينية، التي غزوتموها عندما أسسستم الإمبراطورية العثمانية. لا تحاولوا استفزازنا. نصيحتي لأردوغان هي ألا يحاول استفزازنا، وألا يضع نفسه في الموقف الذي وضعته فيه إيران.…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85866" target="_blank">📅 13:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85865">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هل سترد اسرائيل على الطائرة المسيرة التي أُطلقت في وقت سابق من اليوم من العراق؟!
🇮🇱
وزير الحرب الصهيوني كاتس: نحن نعرف كيف ندير الأمور - نحن مستعدون.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85865" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
صرف رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85864" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85863" target="_blank">📅 13:15 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
