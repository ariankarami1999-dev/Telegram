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
<img src="https://cdn4.telesco.pe/file/ILFfzXvlLing9qpJA7wweanoimpDbZivp2PtaP2P0Nry5n_hsRXOEYJ-mbdNiBKSAhn6POjno9GZwE64HlDLhDY2q6MZ2T05G8ZKFitH2Xp9hSZsefFuH7lbAJJixiLgtvT-AGZGGfC0sE-clfpAZbVrGlYfT9wrZ4B-VffFKi8_zoQ2bwXnfmpNUpdxN3L8w6hTUefXGWy058WxVM8z1c_ITnoT5lJwsgzhg1hp8bqXoJ7oxKeIV4zRoenun1OMsLymAGY02Th10yQH2Hd8zT1Ga5WwO2xpQhZdZ4dvoCkT5BDU-bH0GXXcUig3mrvoNZuD51qdOoQGmD4ja-rWaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 499 · <a href="https://t.me/naya_foriraq/79270" target="_blank">📅 13:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79269">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/naya_foriraq/79269" target="_blank">📅 13:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGRebmd8DWOSZquAFfh40wvM3djnJhh4qKJH5R_rSzCXMpMij6rd1caedD8-MT1rjWddLEVfUu9sjnKSrq-Oug00O7QKSzunnQSVrsK7SLzHhJ9jA6qez5r_BR1aKf7kcxeoB0Yr7VSA6hrz6Opn6nF5Ac0XujKVaZOZQvqh0rvHjCK-9Psq3bLOftdsxGCemQ1tqttHt3OycOI5oToFr_bn-yrz3X1dsVIOYZmW7-UNhQ-0Vz0GlvhfpxUa4DuUO6G0WP4BSYd0ual1ffq_1epO32dnk5JppnOcZuDEXCvwVO-zNpFIbmW1Afn4IlK2Y1X-Zb1kve1u8EGyrhxJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو يوجه انتقادات لاذعة للرئيس الامريكي دونالد ترامب متهمةً اياه بـ"خداع الإسرائيليين" و"الإضرار بالمصالح الأمريكية والغربية" و"التسبب في إذلال أمريكا" مؤكدة انه كان بإمكانه أن يكون أعظم رئيس على الإطلاق" لكنه "فشل" بدلاً من ذلك.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/naya_foriraq/79268" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
وزارة النقل العراقية:
العراق يتسلم إشعاراً من الاتحاد الدولي للنقل يؤكد تحقيقه تقدماً كبيراً في تطبيق نظام التير
النظام تم تشغيله بشكل كامل وافتتحت 7 مسارات دولية جديدة عبر الأراضي العراقية خلال ثمانية أشهر وشهدت تنفيذ أكثر من (1000) عملية نقل دولي
الإشعار يؤكد أيضاً استمرار اعتماد نظام التير لحركة البضائع العابرة براً عبر الأراضي العراقية</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/naya_foriraq/79267" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🇮🇷
رئيس وزراء باكستان:
الرئيس الإيراني سيزور باكستان</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/79266" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79265">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmGbJymaXjmzhIVvPv9-9Xh51so6n-1pYL0cTBFsfw9R0SYDPaElEjbCkCR8j19OQJmYvLxR-Al4eoZEWr5C7uIf5sSsW1ruTdq3Aa9g14Jtpu7CL5CUgPOTIG2Jsfe_pI8BZgWQIGv4ibBSlGEnPUIKOJnfmkR37yYUnfa3ZXLiPeV6pXS8DTUuI5tUS5JP_Quvtegp1SbPsPjjihm3maVdhUPgKWlhk0rh4PnvIQK21CZuOYD-8Yu62Be3PHfZ-7noV_RZQsEvZl1d4WjGOOrOf9ZDq8dnorFP0Un779vflFFX364wPFzE4SE8pvpSYUJgUj4k3eAF1txLYaFtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الغارة الصهيونية على تولين جنوبي لبنان حيث تسببت بشهيدان وعدة جرحى</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/naya_foriraq/79265" target="_blank">📅 13:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79264">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزير الخارجية الباكستاني:
السبب وراء عدم بدء مفاوضات سويسرا  مرتبط بانشغال مسؤولين إيرانيين بطقوس شهر محرم.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/79264" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد من الدمار جراء الاستهداف الصهيوني في عين بورضاي بقضاء بعلبك شمال شرقي لبنان</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/79263" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9MbGxXE1sXtF9UBTxwjsZU6Q4t0_1KVBkF75zBPnldhhWNmRtGa4jq5GMJsTzlcZiCod7PhGfqTA7pHuUB0ey9d-OqXwOUhFZrkqh13puNDAVmwyAX_aTyPqbkdT-ac-vLG5l8n81W9kD6jrfimDHXJch7DOSwAi_FaUwnDRn_Uk8BvW4o-CBol9LLi_GqaQU4xFPXomZohtEwJ812qyHwPO-kYwIhjlxyQECxmhpFG3danCKlpV7JnKwdixQkQKtbM57oVSul4LcW2rfsa7kmAOR5hGbDRUv9uq2ZEQE5lkPalY6CYJ9l1xXwK0DLe58je2TbnMnGLz-k0nhRHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فايننشال تايمز:
تم تأجيل المحادثات بين إيران والولايات المتحدة في سويسرا بعد أن رفضت طهران إرسال وفد، مشيرة إلى الضربات الجوية الإسرائيلية المستمرة في جنوب لبنان.
وقال ثلاثة أشخاص مطلعين على الأمر إن إيران قررت عدم المشاركة في المحادثات النووية المخطط لها بسبب الهجمات الإسرائيلية المستمرة، مما أدى إلى إلغاء الاجتماع.</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/79262" target="_blank">📅 12:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة غارات صهيونية تستهدف بلدة حبوش جنوب لبنان</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/naya_foriraq/79261" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">إعلام أمريكي: طلبت إيران ضمانات بأن الأعمال العدائية في لبنان ستنتهي، وفقًا للاتفاق القائم، قبل استئناف المحادثات مع الولايات المتحدة في سويسرا.</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/79260" target="_blank">📅 12:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmA2TKg-CafHgTWEQM8qt0FUfnnDnvTo3XrbxgMK-IXSvuIR-8x0cFtBVXgUkeyDNcJK57O97qwBn5OO_yKc4lvpUcnMJXT5I7SUc2Cro_ckF1WeYk4zTyCoe2-ArN7qiDDcizLY7_woZGBTdVsrLZpvG1J_IXqLCaaO_M3M8M4fmGT27_IXJGFteEtvTXp_b4d9F_j2wyQ8VFW7Ol3TKDo1uTjQembUI0_-wj7puxrD1-3OAzdJDbpolvw_GQeufxQ5E6dkOCtobWPwbNMSNaFKQFFQtUR-Y4x5qOUYNe_mEJSuWVdEFN6yepjRmDSr74fDuexR9145nPIg5MU1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/79259" target="_blank">📅 12:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.  لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز  نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان.…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/79258" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.
لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز
نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان. يجب أن يبقى في سوريا، وألا يتدخل معنا، وألا يجعلنا نتدخل معه.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/79257" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/79256" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8z7A3TTA4qQd3kEWhbVhmPG49_Y8WWfStlibibj5C3kjU4CaSbt9xV3wUWYWEGadV_tCqqzi_Fv_FwiEZRQcyK5ZaLm7SfeiCp0NX1Bd6XBWVhPR3cj4w5aRtKuKaQkFpXvDc1pofx4IcpoQJP45tIBQ92KVXoxpimS-EXf7_GNc0SxbLepFK5Hmad7Jk6CoGd0U20Sbw_H4F9iWD389M4kJH3P5AZwb1UWWNHwQyiOYJXu-cIDP3qwzT04BBz3LCieFEr9C4D-z4hZnLNtcQR7QbPVI_cEl0hLFuzgOfW8EtLD0oRB2rHL_t4tDWnA4n-2OG9CnfIqRcLtxgkmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ اعتراضية شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/79255" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/79254" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79253">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1zbjSXSFkBGDc1rS9Vkdf5boBvdhQK4MAjIyN6_8lwunlSIU4JhplPlY8cu7BRlAGIicG1E0uQxtVVIS5N7ReUbgeINiY22aM7sNbNosIUpNFFumvsXe6O_o7bb5KEPt2YC-kMDwwdlVJNQgNCdxepw3Zn617j7fn_Cm1hAjIxgQMLiKGpdREG_A3uNyJ7k5y3ijfbP75XmHnAfh_2q244hR8dbb8vp8BhjxHou-nCn-GctD6RXkKzO0XPXo4erjf2TjdrJgC1FHyEyS_JyHXPyuBEhldq-DlCuJszgQO8LMLZNwvokUiVFAUVNGmds6ziwcy3e-3TroCZ12zIBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:
مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!
‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح للعالم أجمع أن دماء أبنائنا وأمن مواطنينا لن تذهب سدى. يجب أن تحترق لبنان بأكملها. واجبنا الأسمى هو حماية مواطني إسرائيل وجنود جيش الدفاع الإسرائيلي، وهذا الواجب يتقدم على أي اعتبار آخر.
‏قلت لرئيس الوزراء، حتى في اجتماعاتنا: مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية دمعة.
‏كفى من هذا التكتيك. في الشرق الأوسط، لا يُحقق النصر بالردود المدروسة والاحتواء، بل يتطلب الأمر حسماً جذرياً. يجب القضاء على الإرهاب.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/79253" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6V3Y80QN9tN5MNNwL_UPve4vqlFXWSYPXdJ6kEm-QMDYvhvFHE88nHey3PoyJUimemaTLBM-EZ735LjvtEYpr8vfrsbj-eu5JXArc6ACruapTeTAYRsoN2KpWGKVR9WfE62esIxK2YJhR10K-1qhphLtVqAHht1zyVaR9tsMlDuJwx3coBWOjc_a8vPlb0jm_rAdZE2TL101FM92h0meEzTNLJ8mpadcCQHw6MuejWSA_8jYB795l4JLyzdDUY-Bm-qSCCKWmIvT80Qr42xY952aFEjlKS62kRbBfgokAm4sZkLM4wiFQFVhj55PbkIpwIcH_KO6BYsy7PzvWTh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بعد فشلهم باحتلال علي الطاهر ؛ رئيس حزب إسرائيل بيتنا يحرض ضد الضاحية الجنوبية لبيروت:
إذا بقيت الضاحية شامخةً بعد الحادثة المأساوية التي سقط فيها أربعة مقاتلين ودُمّرت عائلات، فهذا يُعدّ فشلاً ذريعاً لرئيس الوزراء ووزير الدفاع. جنود الجيش الإسرائيلي ليسوا أهدافاً سهلة في ميدان الرماية. لكلّ أذى يُصيب جنودنا ثمن باهظ لا ينساه الطرف الآخر.</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/79252" target="_blank">📅 10:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/79251" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=D5D59QkVzBdYLEeogNff0Yap8ns8wHoxSGK6q02nQVd_s-D1Di0sEbY-rIcKNjdfit_Z8XLbfxVVIrrvR8aBaCmOiX1ayr6kkX1KNacCmEjHo8_9iaf1NH1seip3Zo6GiC5QFjo8YPfOQlrydE0YrUqgsePxjTjbt6l00k5gNDWhhHXu474bGXkWl-rEjorrWd6xTxZ53zIOLTGEW7ycMA10kpN6oWgJyQcJYleyhb00NjgcwVPer_mqslcsiwqn4hIKjcwNXaSd5hPHRWu_AVB85CktT4dlfDrzvBjOt2gRqbCsQCwePNblXUPIiAkhLl_9xQ5nM-PCseCogriV2A2vb9rRq3gHEHlixJVenm79GJAY2bVbJIGFH3cT8zYmPS945sK_eAHK2Dff550DWQPjQ6HXQkbtyHGKJPtCjS8kaQnAnoWsSxLLr6w0qy4N5_qVYyNWvH1IChuc0Q6wlIGWWYUdbQOY-w415PDUdGflBMXIT3ovNBzRTkyc8Nx80Q0V0m6L60QRviPhd8uMqcjdBR8bawABwwZI2w-swNefXVGepacX0QD-h_6O9fa3RzMFepFiUEgxrLkEHX5H9flwV0D58CIn4eEiUwM4q46l6NcVX2K_IfunY-r8uZbQlHvvBVjgJYCVndmnn52r8ivyzvEBjPaiSIeRlGjEWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=D5D59QkVzBdYLEeogNff0Yap8ns8wHoxSGK6q02nQVd_s-D1Di0sEbY-rIcKNjdfit_Z8XLbfxVVIrrvR8aBaCmOiX1ayr6kkX1KNacCmEjHo8_9iaf1NH1seip3Zo6GiC5QFjo8YPfOQlrydE0YrUqgsePxjTjbt6l00k5gNDWhhHXu474bGXkWl-rEjorrWd6xTxZ53zIOLTGEW7ycMA10kpN6oWgJyQcJYleyhb00NjgcwVPer_mqslcsiwqn4hIKjcwNXaSd5hPHRWu_AVB85CktT4dlfDrzvBjOt2gRqbCsQCwePNblXUPIiAkhLl_9xQ5nM-PCseCogriV2A2vb9rRq3gHEHlixJVenm79GJAY2bVbJIGFH3cT8zYmPS945sK_eAHK2Dff550DWQPjQ6HXQkbtyHGKJPtCjS8kaQnAnoWsSxLLr6w0qy4N5_qVYyNWvH1IChuc0Q6wlIGWWYUdbQOY-w415PDUdGflBMXIT3ovNBzRTkyc8Nx80Q0V0m6L60QRviPhd8uMqcjdBR8bawABwwZI2w-swNefXVGepacX0QD-h_6O9fa3RzMFepFiUEgxrLkEHX5H9flwV0D58CIn4eEiUwM4q46l6NcVX2K_IfunY-r8uZbQlHvvBVjgJYCVndmnn52r8ivyzvEBjPaiSIeRlGjEWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/79250" target="_blank">📅 10:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79249">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXFqWGNBTp2VJ2tsUFWuAf0LmeZ68P_x5xcqIJkh7yt4IhqnFAxN9GbfX-u4iydwV52QXOjxiV0bKIeAP4RudhQfyjNr8aLbhJbCvErmNPecz-FtOnDB8Iu17Wt6fNg-vnKDVTmP3b9BG6GW1slaJi-44hlnXzuQNv1Sf9n13DuYEAuAdnwDulv0DgAinChf4pbQ2AMa0lD8am80Bs6SNple5XWlm5bKJ66981tCkGWFz6VdkCpU3QwundMqRXLI1ebe17emN6hfsVGxbxoLUTZbcW5Ij3B58eIDdKCEKsN429iJPPYwtCa_gUuhtb0D2FWUfnzmvMnlJpcqUf2i-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة  جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/79249" target="_blank">📅 10:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
نقلاً عن وكالة ‏رويترز : الحرس الثوري شكل خلايا سرية بالعراق لمهاجمة دول الخليج الفارسي
‏رويترز: خلايا الحرس الثوري بالعراق شنت ما لا يقل عن 7 هجمات بالمسيّرات ضد دول المنطقة
خلايا الحرس الثوري العراقية نفذت هجمات في أبريل الماضي ضد ضد الكويت والسعودية والإمارات وأنطلقت من مدينتي البصرة والسماوة</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/79248" target="_blank">📅 10:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة
جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد للدروع</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/79247" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=Us4xk8F5jqc_FuYeduJaxKiecQuLLUSf1Qsm0-7sQ7Rj8Y2d1f4VtMsB9W01EGNvVzEy2YE5xJjAss29bZ8_0UzmUHjqJCSkilx3S3Yoo53iz54ZwbPOcH8T-VAmTZqoUjnJZHSTOweeKcrFOdGQThKksJdUiCy4f4QadSJIIS6x_gaMlBoQ1GqsTf7fu0kFy35QrRIKckFdlLHfiWdzLhbahamp7vIYxilAcizA75GE_dGlbZIqVrQp1b5WZkmdkNAkTvv3HvtJGyfZ6jrV3cfFZjF1raGNTMY6NGIRXS1_Flzwbes7ita0nnCoVuoLVuGTSWcJjiwApN5Fb_BmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=Us4xk8F5jqc_FuYeduJaxKiecQuLLUSf1Qsm0-7sQ7Rj8Y2d1f4VtMsB9W01EGNvVzEy2YE5xJjAss29bZ8_0UzmUHjqJCSkilx3S3Yoo53iz54ZwbPOcH8T-VAmTZqoUjnJZHSTOweeKcrFOdGQThKksJdUiCy4f4QadSJIIS6x_gaMlBoQ1GqsTf7fu0kFy35QrRIKckFdlLHfiWdzLhbahamp7vIYxilAcizA75GE_dGlbZIqVrQp1b5WZkmdkNAkTvv3HvtJGyfZ6jrV3cfFZjF1raGNTMY6NGIRXS1_Flzwbes7ita0nnCoVuoLVuGTSWcJjiwApN5Fb_BmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79246" target="_blank">📅 09:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsOK8fe41MBT9EpXh-YAN3BRLvWllm0z29gvEwapeVL2YCg0VrAQTzxKKm62TQAtSxI8Jd6aNLKIveIunIqu72Ego5RfCproHtkhEGArSr4R7D0jxrfG2OU0fE3OR_zmBLCou0jld0LFXKJm2phLMGx7MlWEY2NHM-TzBrA1rEMyTBA7kzbdUEYATocVceTO_pgmXQ2SsvHawdH0Pk4_nDpq7a-QV4GkxhXnssNaaWJVVjBAEN01MnCh-GNuI0gNolgv23Mw-2ulzY1ukEx-WjMQvyYrTqMFULqOTpJqr4cH4oaiq_ZKQsjx_cwGPTctH_5rjvgnH7LgoolfcL0OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTyT50ZnyX-lfPzEpM7OGm7EcGaj6TCJvdpoCmVRQaFtmnbxySoDuUT2gKGKzEJZjvYP8T_pG6ADAfHmsB8z8DfBcOPB3WGFNelccwyYdftEHbRY37FBaxxh8ie8z2uhE3Rz9XpSttLSjwNAMFtNQ9WklQJZM3Eu7SwM9baIX0zuB6ufqLSsUXh3LYQV6sjZR62c0YbPZIV5yXZa9PCP5YPd0_0OnA72awetLoCh1BSBnwe2rwoy9icyskMdx6BVPSoe8jifGWIvDcdgbTcqdv2DOpmDpr_YUsC0P7NfVU5GqylKba7FQIQcd4w370rTmvA8grMCFN77a3583L4AmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
غارات للطيران الحربي الصهيوني تطال عدة مناطق وبلدات في جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79244" target="_blank">📅 06:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB8647k4JQ8H7HpM46gI9y_FTYpb-SRCIz7DPTGrzxTRlBYhHsTMImrvPbu33XF_Eq2L2G7RiAMeWy99GlaNcLdG6yCquQ0G1DmiB9RVLik2Yv5fG_4kiJ-S3fGohsqS6Dxofh9F2FmMCWGctqaxTPShOgUE5inMKdn-f1MaWdYGU7AoeQ4teAgcSb6SlXaqHkDeEZpi4KmH5Vdq2cdkmo6fzWlTIBE8ThtJvay7hqQmLZS8tsd1d9riPTJiszOjmuLLHScTuJGwZeZd6FZIT9sz_yGtXKr-3itlo2zyrVEIY6RP8daF_zuR3O5ezjdULVlPmzcxvTMjeb6w4GQhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79243" target="_blank">📅 05:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
- الحقول النفطية جاهزة لاستئناف عمليات الاستخراج
- العودة إلى الوضع الطبيعي ستتم بشكل متزايد حتى بلوغ معدلات الإنتاج السابقة
(سومو) تواصلت مع جميع الزبائن لترشيح الناقلات المؤجرة والمملوكة من قبلهم لتحميل الكميات التعاقدية  من النفط الخام العراقي عبر الموانىء الجنوبية
- ستكون عودة الصادرات بشكل تدريجي استناداً إلى انسيابية مرورها عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79242" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب
:كنت أرغب في منح نفسي وسام الشرف من الكونغرس، لكن قيل لي إن ذلك غير ممكن
😫</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79241" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
استنفار أمني واسع في نيويورك لاحتواء الموقف وطمأنة السياح القادمين من مختلف دول العالم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79240" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGPIa6FJFpaflg5Yg-zo7H-04Zi6fAQG0itVwxnnoC9SuER-fkTK7u4OttP_kLC2Zp1Nkyi0z4w3BQNe2AEaPKHOSxSXlektmWqBehmLJEqQW8eiYAOcRVU-XUZTodvfPGYQQSatiTAUuFBGRUELgGYe9eE5JdEeHdrNGzGS_eG79WkspUP-XhLhDAWWl4OdWSLZFeN_zh04ylSad3bUTfvPG7Kk-tT_G9sJcd0_QPEVdJpYyfpDtLoHMS3znN94VA_y0q0emYZ0Qad2N0PE5O3C2pNJLK4oVhH2WW-VUJHjkphD9d32uZY_QgL_AkhO21f728DecQj1CMm3n7Scow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مشاهد أخرى لفرّ وهروب المدنيين في الشوارع إثر اشتباكات مسلحة عنيفة أثارت حالة من الهلع والخوف بين السكان والزوار</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79239" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الذعر بين السياح القادمين إلى الولايات المتحدة لمتابعة مباريات كأس العالم، عقب اندلاع اشتباكات عنيفة أسفرت عن وقوع عدد من الإصابات والوفيات.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79238" target="_blank">📅 00:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79237" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79236" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
قصف صاروخي مجهول يستهدف مواقع لعصابات الجولاني في بلدة الهول بمحافظة الحسكة السورية الملاصقة للعراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79234" target="_blank">📅 23:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇫🇷
إعلام الفرنسي:
تشكيلة منتخب فرنسا أمام العراق {فجر الثلاثاء} ستشهد بحد أقصى تغييرين أو ثلاثة في اللاعبين من أجل حسم التأهل للدور المقبل.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79233" target="_blank">📅 22:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سوالف الگهوة
لقاء بعد قليل بين العامري والمالكي لحسم منصب وزير الداخلية … وباقي المقاعد …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79232" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: الكثير من علامات الاستفهام بشأن الاتفاق..  ولا أعتقد أن الحرب انتهت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79231" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6ZVRUkaUWklN4sxsk00fYRK5hIFW6JuRFq1-bI4xJpAS4MkwvOrRxcpQM1k5PtcVByRLofZwaIiw6sA-JxzVbIXqeZWJViZJh2BqlEwQHFgqQbinyIi77nHUAYt7dUadWv1k6rwz0SRHUnULLdtYDK9wy005KeUrD9jx_NecZKkRGiSGkQq2sLnKR8TOwmEo6wX8kMDFDLfExOHDTs4wvv5Fqi4x7o1nknxBIniAnX0mdNc8uTUulBD2B6wmMxfu34iKSkfNtNqu0vKzd-dG-AHksjBBnHwN42oRSvarsZfZujLoPs0ZuDmWW8w-oXH_-YfZ6j6b3-VF70YIT-A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تلتزم الولايات المتحدة بالسلام، ونشجع الجميع في منطقة الشرق الأوسط على الحفاظ على التزامهم بالسماح لمفاوضاتنا بالتطور بشكل جيد. الأسواق سعيدة بما يحدث مع انخفاض أسعار النفط بشكل كبير، وارتفاع الأسهم بشكل كبير. نتوقع وقفًا كاملاً لإطلاق النار على جميع الجبهات، بما في ذلك لبنان وحزب الله وإسرائيل. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79230" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79229" target="_blank">📅 21:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/79228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رسالة قائد الثورة الإسلاميّة الموجّهة إلى الشعب الإيراني بشأن مذكّرة التفاهم بين رئيسي جمهورية إيران الإسلامية وأمريكا
بسم الله الرحمن الرحيم
أيّها الشعب الإيراني الغيور والوفي،
💬
كما علمتم، فقد جرى توقيع مذكّرة تفاهم بين رئيسي إيران وأمريكا. وفي مسار الوصول إلى هذه المرحلة، بذل المسؤولون المعنيون جهوداً حثيثة دافعُها الحرص وحسن النية، وإن كان الرئيس الأمريكي هو من لجأ إلى شتى أنواع أوراق الضغط، انطلاقاً من حالة العجز لإنجاز هذا الأمر.
💬
كان لي رأيٌ آخرُ بطبيعة الحال، غير أنني أصدرتُ الإذن بذلك من منطلق الالتزام الذي قطعه رئيس الجمهورية الموقّر بوصفه رئيساً للمجلس الأعلى للأمن القومي، نيابةً عن نفسه وسائر الأعضاء، بصون حقوق الشعب الإيراني وجبهة المقاومة، وإعلانه الصريح تحمُّل المسؤولية، حسبما صرّح جنابه، بأنهم لن يرضخوا للطرف الأمريكي إذا ما أراد فرض إملاءات توسُّعية أو المطالبة بالمزيد. ومن هذه اللحظة، سنكون نحن - أي أنتم، أيها الشعب الشامخ، وهذا الخادم الصغير - بانتظار تحقق الشروط المذكورة، بيد أنه من البديهي أن المفاوضات المباشرة التي ستنعقد في المستقبل، لن تعني بحالٍ من الأحوال الإذعان لرأي العدوّ. كلّنا أمل في أن تحفّ دعوات مولانا (عجّل الله تعالى فرجه الشريف) شعب إيران الأبيّ بشتى صنوف النصر والفتوحات.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79228" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
المركزية الأمريكية: رفعت القوات الأمريكية اليوم الحصار المفروض على جميع الملاحة البحرية الداخلة إلى الموانئ والمناطق الساحلية الإيرانية والخارجة منه
🇺🇸
الخزانة الأمريكية: ‏عقوبات أميركية على 3 أفراد و5 كيانات مرتبطة بحزب الله من عدة جنسيات "سوريا عمان العراق لبنان" وأحد الشخصيات سليمان فرنجية ومحمود قماطي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79227" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
‏الخارجية الإيرانية: تخفيف المواد المخصبة مطروح الآن كخيار لكي نغلق الطريق أمام الخيارات الأخرى نقل المواد النووية المخصبة إلى خارج البلاد خيار غير مقبول لنا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79226" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📰
رويترز: البيت الأبيض قدم نص مذكرة التفاهم بين الولايات المتحدة وإيران للكونغرس</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79225" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصادر إعلامية: معلومات عن وصول أعضاء من الوفد الاميركي الى مقر المفاوضات في منتجع بورغنشتوك بسويسرا</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79224" target="_blank">📅 19:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جي دي ‏فانس:  سمحت اتفاقية أوباما النووية بالتخصيب، أما اتفاقيتنا فلن تسمح بذلك. منحتهم اتفاقية أوباما مليار دولار من المال الأمريكي، بينما لا تمنحهم هذه الاتفاقية أي دولار من المال الأمريكي.  ‏لنفترض جدلاً - لنفترض بعد عامين أنهم فعلوا ما نحتاج إلى رؤيته…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79223" target="_blank">📅 19:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
محكمة جنايات الكرخ تصدر حكماً بالحبس لمدة سنة بحق مشعان الجبوري بناءً على شكوى تقدم بها محمد الحلبوسي بتهمة التهديد بالقتل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79222" target="_blank">📅 19:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
جي دي فانس: نشعر بثقة تامة بأننا نستطيع رفع تلك العقوبات مؤقتاً دون اللجوء إلى الكونغرس وطلب موافقته.  لم تكن العقوبات هي العائق الرئيسي أمام النفط الإيراني. لم نعتبر ذلك تنازلاً كبيراً للإيرانيين.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79221" target="_blank">📅 19:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تفعيل الدفاعات الجوية في سماء المطلة شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79220" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79219">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس ملوحاً عن برنامج إيران الصاروخي: لإيران حق في الدفاع عن النفس وحقها في امتلاك صواريخ باليستية، قائلاً: "إسرائيل لا تتخلى عن حقها في الدفاع عن النفس إذا أطلق حزب الله صواريخ أو طائرات مسيرة على إسرائيل. والإيرانيون لا يتخلون عن حقهم في الدفاع عن…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79219" target="_blank">📅 19:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeDfitnWp9GuEryhlA7d3oTfciHQl6rxjeAdIITNuTn6AEF5aB5LVJ4qBJP6-ueMeEwKc-UHo2LOTagHhUCUexysANqNUQ44ffNSjdOnJ1j_qEB5S4sH4mONLcRAvv8Ad1kTQ1KrVoAyskQcvoV40_iflATfnZN3Wml5p2cDPyvTjTJXNTCi-M7Wwtrv3WNgWXbF305kaTlHs0K_srGfSUMKQZhubQpvkBxNJtMupYll-qVLR5l-Y0h0xgheyXRXbli252Ho-mUxWu-AqJxc4zR9medCy-BZiIRepWc9UQXy6k-KHBzG9bOVciPsYtJelRFS_TwrinFVLN8fIJhAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBL4QfPdS_maKZ8P1mgHfacnRezzoYVKdolI3nMpWnNSLt_ImRdSi3lnwHZ1-uTKrxt5LnLwPWZHV7O0sbDaf0tS9kXfLp4p2CgG-1fYzJZwl-ignAocnV5vKchIlLlEe2Be6KCyRyJV4cwUF7OpQ35qs_blufo1HhK0k7WZadE1SeBngLBZU0PDEGeS2Er3ETREKnETogS2uYdyi4gPm96R0AQlQ0kgPXAvHpTIT6bou9nirBfoj7dGG0Au419_NZ-tyP-IRHqF1X0aqDLUktVzvmEDfmpVR3I_i-puhd5k1-_TTJShMAx8b5RGhF01YOwmcRZrPc2V5A5Oo0jl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGHc84lPTDvFAZ9gagavuuIJJz9pNm6-A7ox_WbdoVXJiPBOHiZ57Bzd2kDLiibiMIVuDUZyMTGH0VzsRmbPU4fmQQZr20gGERCO7lssjUbxnjD494Lsg1cEGOML4jFZfEL3Phoz8tQKHHvqRhk5-3_ShlOFRTGa3V4Fyz-JneOqG5i3nUWxsUoTRtBmlbm5fOoCHhi5I1uGW9GGv4sqv37n1assUNDQbndEc6xpA0JS5RfJuSbMqqE7_C_M4HjL0rqYYJaXoXDVLGo_cECZCarDhW_q8nNl7fdwDNKcDECAdSWXSx7s3kGFn1szQAG2CzvvF1EDPHzR0f28-nVuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3i5MKEcQC28ZtTBlXkBntCk2DP8iGRQBvrDFjR4kDn3JpR3ILLQqH7yCP2-ObGTJ8a8EZGpLH-CKARpzIIZRsPelrnue6Jsjrxz27y3tMuAIEqAkPiF1ytsdBem6G8dQQsRIsIrjLF-ShXk2VAwMRAJDBAdswil140RoaTS-lc1LedBkpZYq1CI1vzfCdfSvcvy5PbAbfMmlle5rLMKhEHnekZpZpjBf4fZesUijptT1s9SBZ_ccxq4rBrtpVqriEYhbDweSX-35GwFdncEdeIFHe7bo07KpmU82BX9ql83gQTCkp6P4rdqZ3vMES4YsEI7padcxPX3igObvZpkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFrnigkQFDV4V7RePI_qFvzgHkwQ_KpQ3byXuYsswfxPpvL2SStTVlUtGz8jOvE0RLD2qOn_q-Ll2qo4yUZW3Dqvu28mvHarPKP-K0i5sr4J8jCCzfl2j8SJIr72JsHDmX1Ars2LVMVyAyHZVtGdjA-rgEzZ5qfXwIXdSOtffIZgwdsPkAXqwxSIZdnyK55LRYQT8Fvo4yo1Bw3vscoCcd5ojH3-mQva8ERWj2w5g1P27vXohCdks_OcvCWfi4Yauqk0rGQ2Pt1tPNk7ktmlBrHxWv6V1ukiXjWfwMI1P4r8r76oCLbtlE4rfZlXbPqvoabMv7tzwwL5zVifMIIozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
صيادله العراق يعلنون الاضراب و اغلاق جميع الصيدليات في العراق احتجاجا على قرارات وزاره الصحة العراقية و الظلم و التهميش الذي يتعرض له صيادله العراق و الطلبه الخريجين حسب تعبيرهم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79214" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
جي دي ‏فانس: بدأت فترة الستين يوماً اليوم، بتوقيت إيران ؛ ‏بدأ الاتفاق أمس، وسنبدأ اليوم احتساب فترة الستين يومًا  ‏نتوقع كجزء من الاتفاق النهائي ألا تمتلك إيران صواريخ تهدد العالم بأسره ؛ ‏تم تدمير برنامج الأسلحة النووية الإيراني، لقد انتهى أمره</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79213" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.   وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79212" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.
وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79211" target="_blank">📅 18:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇧🇭
الدفاع المدني في البحرين: حريق كبير في منطقة الصالحية ، والجهات المختصة تباشر بالتحقيقات.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79210" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🦠
الكونغو الديمقراطية: 202 حالة وفاة مؤكدة بفيروس إيبولا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79209" target="_blank">📅 18:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4IJ4aG_r8ql2Evb-m9HSiNu1lCnw_uK9LBFU43fkumZjhfEuPOGyBiY_d_CftKnlUXSFTFcWnt2H8TjrsNhYIK_BslQ7pd5HqyrGYAp85XX4gJAetblI4Ypv_jES1_rGwf3waDFhrwCbzApYUKC0sc_Z8U54pI6dPvTstY7QE4omv6w-MmYkYeFCe_IhCzhqI1QlHpCtRl9sz-TkMfyuQ10B5JFPe2Z2r7S4vVcwEwsHM3_MuJPpWY7zQZa680_Hg-eOWg3OdQy7dU1On4dALfmv-jnPK4wtEpveUkoAzpdMAMGLJEwCC8YpFmwEeAjH_3-QZLU3292bb8tECjFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
احتراق دبابة صهيونية وعدد من آليات جيش الاحتلال إثر استهدافهم برشقة صاروخية من قبل حزب الله في الجنوب اللبناني وإعلام العدو يتحدث عن إصابات عدة في المكان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79208" target="_blank">📅 18:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول التصدّي لمحاولات العدوّ الوصول إلى مرتفع علي الطاهر:‏
يحاول جيش العدوّ الإسرائيليّ، منذ 4 أيّام، التقدّم باتّجاه بلدة كفرتبنيت ومنطقة علي الطاهر عبر أكثر من مسار مدعومًا بقصف مدفعيّ عنيف يستهدف المنطقة وإطباق جوّيّ استخباريّ تنفّذه طائرات العدوّ الاستطلاعيّة. وقد تصدّى مجاهدو المقاومة الإسلاميّة لجميع هذه المحاولات عبر استهداف تحرّكات وتحشّدات العدوّ بالصواريخ والمسيّرات والمحلّقات الانقضاضيّة، ممّا كبّد العدوّ خسائر كبيرة بين ضبّاطه وجنوده وفي آليّاته، اضطرّ خلالها إلى التراجع وزجّ الطائرات المروحيّة تحت غطاء دخانيّ ومدفعيّ في الليل لسحب خسائره.
يوم أمس الأربعاء 17-06-2026، الساعة 8:00، وبعد رصد قوّة مشاة من جيش العدوّ الإسرائيليّ تتسلّل للتموضع في الأطراف الشماليّة الشرقيّة لبلدة كفرتبنيت، وبنداء يا أبا عبد الله، استهدفها مجاهدو المقاومة الإسلاميّة بسرب من المسيّرات ومحلّقات أبابيل الانقضاضيّة وأوقعوا أفرادها بين قتيل وجريح، ثمّ استكمل المجاهدون هجومهم بصليات صاروخية وقذائف مدفعية باتّجاه منطقة الهدف.
وعند الساعة 1:50 من فجر اليوم الخميس 18 - 06 – 2026، وأثناء محاولة العدوّ التحشيد مجدّدًا عند منطقة المعبر، استهدف المجاهدون دبّابة ميركافا بالأسلحة المناسبة وحقّقوا إصابة مؤكّدة ما أجبر القوّة المتحشّدة على الانسحاب من المنطقة.
تؤكّد المقاومة الإسلاميّة أنّ قوّات العدوّ لا تزال تتواجد عند الأطراف الجنوبيّة لبلدة كفرتبنيت لجهة أرنون، وأن منطقة كفرتبنيت - علي الطاهر ستبقى عصيّة على توغّل العدوّ، وسيسطّر المجاهدون فيها ملاحم كربلائيّة دفاعًا عن بلدهم وشعبهم.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79207" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇱
🇮🇱
إعلام صهيوني نقلاً عن ‏ترامب: من المحتمل جدًا أن أدعم نتنياهو في الانتخابات المقبلة لدينا علاقة جيدة لكن على نتنياهو أن يكون أكثر عقلانية.. وأنا مستعد للالتقاء معه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79206" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79205" target="_blank">📅 17:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvKqj7K2ATDCUOaJ5MCYK6tfB-BbR-7D9Ocw5cRyluZUHYjKe3b4zK6IYBIPVASmnWCc4SG_07CSAz9K7lIiifdZbjNDOp4Toe7Uer4QlWhkHdqOGdZYStDdBLg-BxXUlmSPrvWY1-6lPx61ofabeV2vTFzTK_p1KEvTq4J23pshAyY9p9UWZDiKgGPs3NBYSnglhJjaRKc0IO2qOqe12HX_C3yKcaUVmM5VyZz4cFL9fdVgdqcZj5y69sKfm93hSK1CXicz4AbOj1ZG0UAmAlWdot_VrTvjP-QKVXew0Wte3eJcEaBgi0ZkvP6IalhpHYYZlCY_tHVsupvveJgiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب من غمرة أحلامه يغرد: "النفط يتدفق، وإيران لن تمتلك سلاحًا نوويًا أبدًا (سيكون العالم آمنًا!)، وأسواق الأسهم مزدهرة، والوظائف في مستويات قياسية، والأسعار في انخفاض (القدرة على الشراء!). بلدنا قوي وآمن ويحظى بالاحترام أكثر من أي وقت مضى. على الرحب والسعة!"</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مدير عام وزارة الأمن الصهيونية: الحوثيون والميليشيات العراقية يملكون القدرة على التسلل بريا إلى إسرائيل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79203" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية: الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79202" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية:
الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79201" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzZDPrA6rwY1JxJqzeNam24UliwyGtW45mjqHzkrLKn-m0el6C1EPlgb_LgIaIwh6zzcuTzNEWz4rMKRPSyIvldBpGkswbVG0EPEzXFvTcQwjgiKNsYTX2M28lwaxJGenh0Knu8-CXq9wIY0-xDuLZ5O_py8UKvAUDs7yF7SkvRFc1Aw1cOlezjl6z5B92f6qrAOXW7dnHrTnfHEGtWoofVIwrRMhhCYw5nU4fYfMtDkgYBHtEAlLLPVQQ1SV1YVWiE_fGu6JfgIkmwnU8uR3oCva-rIdbu5Vqz8g8GC02DUu_Wh8knJS8_eIM681em4e3zND-Ud8lTo3ObmxAMhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة
يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.
التاريخ: يوم الجمعة 2026/6/19
الوقت: الساعة الخامسة مساءً
المكان: بغداد الصالحية - أمام السفارة الايرانية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79199">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
يعتقد مسؤولون إسرائيليون أن الرئيس ترامب قد يؤجل شحنات الأسلحة أو يفرض حظراً على توريد الأسلحة إلى إسرائيل في المستقبل إذا لم يسحب نتنياهو قواته من لبنان.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79199" target="_blank">📅 17:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
التلفزيون الباكستاني يعلن الغاء زيارة رئيس الوزراء شهباز شريف المقررة إلى سويسرا دون تحديد الاسباب ويقول ان المفاوضات التقنية الأمريكية الإيرانية ستبدأ بشكل منفصل ووكيل وزارة الخارجية سيمثل باكستان في اجتماع سويسرا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79198" target="_blank">📅 17:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد.. نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79197" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79196" target="_blank">📅 17:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف:
زيلينسكي إرهابي وروسيا ستشن ضربات منتظمة على أهداف في أوكرانيا حيوية وفعالة لقواتها العسكرية رداً على هجمات كييف.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79195" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف
الجيش الإسرائيلي
.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79194" target="_blank">📅 17:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">متداول:
تكليف (نزار ناصر) بمنصب محافظ البنك المركزي العراقي.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79193" target="_blank">📅 17:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ظهور كائن نهري نادر غير معروف في محافظة ديالى ومواطن يتسائل هل هو حلال او حرام اكله تمهيدا لتحويله الى منسف.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79192" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMw66rrx3k6KgwTuH-ryPdHzAZQbGqOOubMHmit06uluWeFMNcnwT3OJuvKG8VMt7hKADoSLfvMU9mg8x33-Ot_YNBs0bACMEzm4MhLKPn1hVUTsDGHZjDgUh2L1Nv6APHqwOGRMbQFxd-yr3inVomso2t1S3Dets84mdzLgO2dufC_XMyRBGzLUGBeisZXtm6DOa3jx0a73vjfytFnlSkLEB1VjOfODffCSGLG76PLC0Dey64SE6NU-NV3qbGu9mp6BQiGd2_pTWtEcSs86VE0_T5jyufKSbWWWC4oSGZEEAepVXJuylbZSPeBby-687ILrwb9qkWlDoqOurNlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يعيد نشر تقرير بعنوان "البابا ليو يشيد باتفاق السلام بين الولايات المتحدة وإيران".</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79191" target="_blank">📅 16:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد..
نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79190" target="_blank">📅 16:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇬🇧
‏بريطانيا تقرر تزويد أوكرانيا بـ150 ألف طائرة مسيرة بحلول نهاية العام ضمن حزمة تمويل بقيمة 752 مليون جنيه إسترليني.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79189" target="_blank">📅 16:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
القائد العام للقوات المسلحة يكلف باسم البدري برئاسة جهاز الأمن الوطني العراقي.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79188" target="_blank">📅 16:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جندي في جيش الاحتلال التركي ينشر مشاهد يُظهر الطريق العسكري الجديد الذي تم تشييده بعمق 9 كيلومترات في قرية باساغا بمحافظة دهوك ضمن اقليم كردستان العراق
يمتلك جيش الاحتلال التركي 139 قاعدة عسكرية في إقليم كردستان رُبطت جميع هذه القواعد والمقرات بشبكة من الطرق العسكرية وقد قُطعت عشرات الآلاف من الأشجار ونُسفت جبال وتلال الاقليم لبناء هذه الطرق.
اين مسعود وميليشياته التي تضيق على شباب وجمهور الحشد الشعبي والسائحين ممن يرفع العلم العراقي من هذا الاحتلال؟</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79187" target="_blank">📅 16:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
المتحدثة باسم الحكومة فاطمة مهاجراني:
هذا الانتصار اليوم هو ثمرة جهود القوات المسلحة وكافة أركان المجتمع والحكومة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79186" target="_blank">📅 15:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
الأنواء الجوية العراقية تبشر الشعب العراقي:
موجة حرّ خمسينية تضرب البلاد بداية الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79185" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcqSYB3Pa_f5qePSftBJwfOikirhhOEX2Lu4XaRpHdRFpAH1buUOCJdeC7-Opge-UkvL1T1eheGz1sdb5mFmnx6HD_SbVNFO15Huj4ny4Ga6J8Yrg3gPKRW8_P8fS0eGUddiT4R1ZligzCxpktdaNaBn_i7lAbM_TIG2RixLI3UFo5BOBTBnc7CLatpmx7J8eIo9o75LCNhfszGxre1ORZkegXM_-m0TYBmDLjEh7z_i6lUkqGPX3BoENT6HqD_9iyO7TKOFHCxJRSFVujGtIP_j0KV3rFklWFYVarQOKjh2T29z4M4j8HMqgs1diPzWdQxVH586Y7R_Zvq4L9vvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
توثيق أخر يظهر كثافة استخدام القنابل المسيلة للدموع وإطلاق الرصاص الحي من قبل عصابات آل خليفة نحو المعزين بذكرى أيام إستشهاد الإمام الحسين (عليه السلام) في منطقة أبوصيبع البحرينية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79183" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام العدو:
اتفاق جيد لإيران وسيء "لإسرائيل"، سيبقى اليورانيوم المخصب في إيران، وينهي الحرب في لبنان، ويضمن إعادة إعمار إيران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79182" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
سي إن إن عن مصدر إسرائيلي:
نتنياهو يرى أن الاتفاق النهائي لن يحدث وأن طهران لن توافق على تقييد برنامجها النووي، نتنياهو يسعى للتأثير على الاتفاق مع إيران عبر إعلاميين يمينيين وأعضاء بالكونغرس.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79181" target="_blank">📅 15:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjL2V44BVtBoMcPuaNRJnq951AI1HMTd-mdHcfGQ961yycg6xZmcDHCVb7ZxbZaCE49QUdqd3zWlKXUYd3lHucI7goBxclC53TF2f6Dz828mjZ0TsU337gXVRhRDH6eU8VnWvVVsaugRFaB4mam99TcgbbIc48O-lyNS1FF1Gt-n3tJ9a2KJ8vYA_XC7j12CZbICa_pxEPHQp22lPHwRsT6-ZFbzBV3dDK86bknuYUlrFNEwcsTRMZtjaYyNf1ePVKMHFi5sBtrhWxm_KOZf4lCgJ-Oih9w2oT-7jmPjhWXguo_mnaLCaj7oPlTpYGacIz0xCAx1RITg45wXq2n91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPUTiCX0mu6qN-qAGEF-pr52P5kVR3_TpBtdM2FUzJ81vY_ejozrr_n7i0fPTyWHFHW4ceSfUaumgm9Bbtlm_w1PKXtEW3lw69-MXvwYPTA9PCXhh0UQRVGmWnKlqUOtMSkau-cNd7nyBWCLlHDmWFFGV4XzFABcugLRGS3R8sDJmeIeuZ4Y06bbD3E34ej0O5J6X7jDbBcY5gp4wwvcxHB0GsH7SQs2cdOwzu14SQLGFQueDNRuF6hYDHVlGSlapG8PUPMRmvk4CKycLnufl454THrx3U2q2aQkmcSL5T0omszhW5ZIeDDKfdeBPbPtBpZqmbu8K4JtgRkCYGPK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8YJeI0cFiizC3qaBJcdJSRa9WN5BjNZbequKWbq-Uq23TKBbSoWnUQlKsAtkBTh7Nprdf8kf9DaBhdLIGTYZSi5YTvLzIe3dyfJIvmwi0iYGKumGeUyOm4h5lqYNa3-kfUgZHfLvduyYxEp9ORd1h76G6VS9_Yy_jqeYpSyFEZCwp4GDP0MG1s4S7XH04TYp51E2M_B5MWwu7oQkabINJQoBI-6B4xSEFwlVvqNmwPI9r0ovgrMfGf4Il35YCP_Ot3xz1MgxogV6QsNLkpyGV9eH2GxL8GGR25EAQ0MXtjBTLf5LCMgtR7nNKj2Uf4rHeQy_kuTYLuN8dqeP_BDqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان ينشر بنود الاتفاقية مع الولايات المتحدة رسميا.
- تُعلن الجمهورية الإسلامية والولايات المتحدة وحلفاؤهما في الحرب الحالية الإنهاء الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان، ويتعهدون من الآن فصاعدًا بعدم بدء أي حرب أو أي عملية عسكرية ضد بعضهم البعض
- تتعهد الجمهورية الإسلامية والولايات المتحدة باحترام سيادة كل منهما والسلامة الإقليمية والامتناع عن التدخل في الشؤون الداخلية لكل منهما
- تلتزم الجمهورية الإسلامية والولايات المتحدة بالتفاوض والتوصل إلى الاتفاق النهائي، في مدة أقصاها 60 يومًا قابلة للتمديد بالتراضي.
- فور توقيع مذكرة التفاهم هذه، ستبدأ الولايات المتحدة في إزالة حصارها البحري ضد الجمهورية الإسلامية كما تتعهد الولايات المتحدة الأمريكية بسحب قواتها من محيط جمهورية إيران الإسلامية في غضون 30 يومًا بعد الاتفاق النهائي
- عند توقيع مذكرة التفاهم هذه ستبذل الجمهورية الإسلامية قصارى جهدها لاتخاذ الترتيبات اللازمة لضمان المرور الآمن للسفن التجارية مجانًا لمدة 60 يومًا فقط
- تتعهد الولايات المتحدة مع الشركاء الإقليميين، بوضع خطة نهائية متفق عليها بشكل متبادل بقيمة لا تقل عن 300 مليار دولار أمريكي، لإعادة إعمار وتنمية اقتصاد الجمهورية الإسلامية
- تتعهد الولايات المتحدة بإنهاء جميع أنواع العقوبات المفروضة على الجمهورية الإسلامية، بما في ذلك قرارات مجلس الأمن وقرارات الوكالة الدولية للطاقة الذرية وجميع العقوبات الأحادية الجانب، الأولية والثانوية، وفقًا لجدول زمني متفق عليه كجزء من الاتفاق النهائي
- تؤكد جمهورية إيران الإسلامية مجددًا أنها لن تحصل على أسلحة نووية أو تطورها. وقد اتفقت الجمهورية الإسلامية والولايات المتحدة على حل مسألة التخلص من المواد المخصبة المخزنة وفقًا لآلية يتم الاتفاق عليها بين الطرفين كما اتفق الطرفان على مناقشة مسألة التخصيب، وغيرها من المسائل المتفق عليها والمتعلقة باحتياجات الجمهورية الإسلامية النووية، وذلك في إطار عمل مُرضٍ يتم الاتفاق عليه في الاتفاق النهائي.
- في انتظار الاتفاق النهائي، تتفق الجمهورية الإسلامية والولايات المتحدة على الحفاظ على الوضع الراهن الحالي لبرنامجها النووي، ولن تفرض الولايات المتحدة أي عقوبات جديدة، ولن تنشر قوات إضافية في المنطقة.
- تتعهد الولايات المتحدة بأنه فور توقيع مذكرة التفاهم هذه، وحتى انتهاء العقوبات، ستقوم وزارة الخزانة بإصدار تصاريح لتصدير النفط الخام الإيراني، والمنتجات البترولية ومشتقاتها، وجميع الخدمات المرتبطة بها، بما في ذلك المعاملات المصرفية والتأمين والنقل والشحن
- تتعهد الولايات المتحدة بإتاحة الأموال والأصول المجمدة أو المقيدة للجمهورية الإسلامية للاستخدام بالكامل عند تنفيذ مذكرة التفاهم هذه وتتعهد الولايات المتحدة الأمريكية بإصدار جميع التراخيص والتصاريح اللازمة وفقًا لذلك
- تتفق جمهورية إيران الإسلامية والولايات المتحدة الأمريكية على إنشاء آلية تنفيذية لمراقبة التنفيذ الناجح لهذه المذكرة والامتثال المستقبلي للاتفاقية النهائية لعام 2001
- بعد توقيع مذكرة التفاهم هذه، ورهناً ببدء تنفيذ الفقرات ١ و٤ و٥ و١٠ و١١ من مذكرة التفاهم هذه واستمرار تنفيذ هذه التدابير، ستبدأ جمهورية إيران الإسلامية والولايات المتحدة الأمريكية مفاوضات بشأن الاتفاق النهائي حصراً بشأن الفقرات الأخرى.
14- سيتم اعتماد الاتفاق النهائي بقرار ملزم من مجلس الأمن التابع للأمم المتحدة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79178" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
بيانات ملاحية:
ناقلة فرنسية للغاز الطبيعي المسال تعبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79177" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في أطراف بلدة مجدل زون جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79176" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
بناء على الحاجة العملياتية تنتشر قواتنا في المنطقة الأمنية بعمق 10 كلم داخل الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79175" target="_blank">📅 13:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79174" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79173" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=RRHmA-PRnswT-gGtWwLR6MsDuuQSofXdrnYP-8LDfpDBi93D0FX7-IleAvEkKXdXn01ZglBFbCHYXJFDgA2kcP7VOu-J2stQlKXyJk4XPvw3wcnd-YWVOvEws-V3pt4WsygTPNtlkItL2L_wXq_VHDzdKkCIKV1LyOYKfrEx0MdA3PHkRMmYUtdqrVmrpoi_Xrr7eUmhs2uZVay930csupMozdO-hlOZf2cR6Vlvgv36KKLNTiW5mxEb5_IxJjz_q3A8sQfVuvGVBP2UI-bdMnOu2ASWwYybd6mzXbtGiCBTeqho1M4z6m06-jK7XJEpP-4HL5bOwkn6s4XtK8CYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=RRHmA-PRnswT-gGtWwLR6MsDuuQSofXdrnYP-8LDfpDBi93D0FX7-IleAvEkKXdXn01ZglBFbCHYXJFDgA2kcP7VOu-J2stQlKXyJk4XPvw3wcnd-YWVOvEws-V3pt4WsygTPNtlkItL2L_wXq_VHDzdKkCIKV1LyOYKfrEx0MdA3PHkRMmYUtdqrVmrpoi_Xrr7eUmhs2uZVay930csupMozdO-hlOZf2cR6Vlvgv36KKLNTiW5mxEb5_IxJjz_q3A8sQfVuvGVBP2UI-bdMnOu2ASWwYybd6mzXbtGiCBTeqho1M4z6m06-jK7XJEpP-4HL5bOwkn6s4XtK8CYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79172" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKUK5zkyFW9EWXtFB3-007gD7TCcRXY06otvM-5xawuZllfGmObTdiKmbqdUfK2cea26yvjbm4AjRJJdAp7sFfdUll4FwXajl4FWxq0dpJW-0_VG4bxAQGf4fic_S2161s2GdoVoJWZtDbobsgAlXQtT8AYRsb54One6REHhHLsEl0qVRCMR0UM83aRyTdu_GBXvMLIjtCWlXgsJt68t1LZ9FnlQtKIJsodvjb0EUPOmkLrVAWZoy97PA5Clw4oEIr1Y3xaJAmkqcQckPvaUStnGmtHSEMCGK1hpYpOHWOgO-lC4x_hvgnjmwxsdni970SxLMGCz5Ssf9UUipc7e8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
"هؤلاء الحمقى الذين يظنون أنني لم أكن حازماً بما فيه الكفاية مع إيران، في حين أن سوق الأسهم قد سجل للتو مستوى قياسياً، وأسعار النفط "تنهار"، إما أنهم حسودون، أو أناس سيئون، أو أغبياء. لنجعل أمريكا عظيمة مرة أخرى!!!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79171" target="_blank">📅 12:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=e1XOcJMMpdZkYp7v_9soFW6f_wB65S5gNNX_KkI7NCYI8expPeW7GiloKNxblIPS2K0CVqs5Kg8r4DRAeHZL3xhuLWNIkjfoOIYQhUlLWdA7Jpq9cH0Njn6otSU30YNeHyBmWtN8_RzrQMkAbe3_s62Y7kMFMCugPrF83cgEk5xj2xjjH0Z0u1SZr9srStSaS5DXGst25G1vqMj8cfwv0lEZQsmENEtOnoo6XfPjuW1KMl-5oZNFQZ-YpMUCS_SQ_f2IpDfT2tOcyc4QPAj1-7gVkHa7caRCSuh2shcBC-QNvkzjH4-oBUm-ZuBG4TAS7err8Qk0gqpSTT7bO9HZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=e1XOcJMMpdZkYp7v_9soFW6f_wB65S5gNNX_KkI7NCYI8expPeW7GiloKNxblIPS2K0CVqs5Kg8r4DRAeHZL3xhuLWNIkjfoOIYQhUlLWdA7Jpq9cH0Njn6otSU30YNeHyBmWtN8_RzrQMkAbe3_s62Y7kMFMCugPrF83cgEk5xj2xjjH0Z0u1SZr9srStSaS5DXGst25G1vqMj8cfwv0lEZQsmENEtOnoo6XfPjuW1KMl-5oZNFQZ-YpMUCS_SQ_f2IpDfT2tOcyc4QPAj1-7gVkHa7caRCSuh2shcBC-QNvkzjH4-oBUm-ZuBG4TAS7err8Qk0gqpSTT7bO9HZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79170" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
حان الوقت للجلوس مع الفرق الأمريكية والإيرانية لاتخاذ خطوات ملموسة.
سنشارك في المفاوضات التي ستعقد في سويسرا بين واشنطن وطهران.
هناك خيارات عديدة بشأن التعامل مع المخزون الإيراني من اليورانيوم.‏
الاتصال مع إيران في أدنى مستوى له.
إذا لم يفتح مضيق هرمز حتى نهاية يونيو فسيكون الاقتصاد العالمي في منطقة حمراء.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79169" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79168" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79167" target="_blank">📅 09:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=rRs8Zw7F_uvefaPkpPbzXfIJZkFB6bRsCuYhRa7TYgV_QzcO4X43765VuHoLw2GDLzKLgSNN4lJRTObzVir9e9nnJ8172jfGzOW2EKzRycTTBzBbk_p_du-O1LoS-BD5Jpv0jRnSPph8GtLabibtbMdOTeMFJeSmiJHQrzZE90QNxRXw4QD6jcSO0GcrKoT_-FI8_0UJlXaUkzU6rPkopWtWMsgmqbkaCg8M19fhfyDaKW_3IL57FrL9-Iy5oi0Qy2SNVhA32BkIv_Y-I5qCCQDtTZBpBKnPTybBCdSdufWaIUGxB7yineZ-zOjIXgMJpFtYsJzlg8KTZplKintbmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=rRs8Zw7F_uvefaPkpPbzXfIJZkFB6bRsCuYhRa7TYgV_QzcO4X43765VuHoLw2GDLzKLgSNN4lJRTObzVir9e9nnJ8172jfGzOW2EKzRycTTBzBbk_p_du-O1LoS-BD5Jpv0jRnSPph8GtLabibtbMdOTeMFJeSmiJHQrzZE90QNxRXw4QD6jcSO0GcrKoT_-FI8_0UJlXaUkzU6rPkopWtWMsgmqbkaCg8M19fhfyDaKW_3IL57FrL9-Iy5oi0Qy2SNVhA32BkIv_Y-I5qCCQDtTZBpBKnPTybBCdSdufWaIUGxB7yineZ-zOjIXgMJpFtYsJzlg8KTZplKintbmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79166" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79165" target="_blank">📅 09:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
لا يزال استهتار البعثات الدبلوماسية الأجنبية في العراق مستمر
اصابات خطرة لمجاهدي جهاز الامن الوطني العراقي بعد تعرضهم لحادث سير من قبل رتل تابع للسفارة الأمريكية على طريق مطار بغداد ؛ ثلاثة جرحى كحصيلة اولية من الضباط …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79164" target="_blank">📅 08:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79163" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKenhiF7U6EacyxqdOTjzq0X5dGU8QoLQOdRZpkcftIqfuyNBSt5Cg1WBdx_kBFEv4CjEtlXpT5e9Q6N3o1ssVkk6y9MwtYe18G7MrItB76YzTmrTLL20IBN-9B93vI_VxGSvjgCSXT1KATXmS7XoGGBQJ7gKmxj0JwSHRFBa09avCae4qw5q4deMvLhiCK5YS4_vDMQMnwVwoSGii8cLywrHdmJXvH28L5axXxmG-3oKD3BXYFSkliEY5IfYD3r9LuFU4wnBFlUywMeF7W0SDwioevDlg9jPfWi7AyQG6U2qfnHsGB3rg6cDVgJgZPmTQ8BRXO-ij_FDa1Nw5YGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=Z6CP0rSkOaVUwJxz_H8EVgWXif832WVjWKiZ7YdYlFOdjT1e8If-Sh_eMHNa-4ST0PR51o0owKGqNpKbG3lMP8P6Y3a2RNUPRybFOHjtuKEZieCXW04hyRJVBXCl3DrKfN7AIVXxs_YQ91DEQxFakdzIKJySwviLrNKDt93lr-I25uzi6LtaYxKPW4PsEF0Vkv_SY01WtGz-ckZn5rUEHk6VTZZrf8sYZESunvIriayUMrfoFxMw3W9QKA8SUDhAuDQpyXnOaOWUd_5yozyEgdqtM_GHz0I0exd-hJRG3s5x807kSTxVDePo266Y6m-W4p88E4a1_uAU-tni2Bd7rX1CZDg0td5QhQrNUlygia0KiF6QzuwsGDwC8Sg2tjI8HSu9Rbz3c3sVo-fKNPkOoGoNdQaANSP2tIAuRJSf-l6osIc4_ub6AIs67wbbeMUVsCrjMxl0x36C4xXv9GxoV8kWy0tGCuTQOvOIOHEST_PwwXlRtjx5VK2b1s5sTTi3fGjUdkut_Bi0gvaoCKCix3a-SQ40xbgBv9zqc9lRG18iAuRcy0SxscvMUEQ2LbOYXkkea-OBDReDTQW-4OizVV4XT78KmHZ576YWBfILuzffa8puTBZukhqka0Uh2Ivp2WKMVli1vfz-2uTa2jJBFFnDj6EUKKJTrn-W09pzPaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=Z6CP0rSkOaVUwJxz_H8EVgWXif832WVjWKiZ7YdYlFOdjT1e8If-Sh_eMHNa-4ST0PR51o0owKGqNpKbG3lMP8P6Y3a2RNUPRybFOHjtuKEZieCXW04hyRJVBXCl3DrKfN7AIVXxs_YQ91DEQxFakdzIKJySwviLrNKDt93lr-I25uzi6LtaYxKPW4PsEF0Vkv_SY01WtGz-ckZn5rUEHk6VTZZrf8sYZESunvIriayUMrfoFxMw3W9QKA8SUDhAuDQpyXnOaOWUd_5yozyEgdqtM_GHz0I0exd-hJRG3s5x807kSTxVDePo266Y6m-W4p88E4a1_uAU-tni2Bd7rX1CZDg0td5QhQrNUlygia0KiF6QzuwsGDwC8Sg2tjI8HSu9Rbz3c3sVo-fKNPkOoGoNdQaANSP2tIAuRJSf-l6osIc4_ub6AIs67wbbeMUVsCrjMxl0x36C4xXv9GxoV8kWy0tGCuTQOvOIOHEST_PwwXlRtjx5VK2b1s5sTTi3fGjUdkut_Bi0gvaoCKCix3a-SQ40xbgBv9zqc9lRG18iAuRcy0SxscvMUEQ2LbOYXkkea-OBDReDTQW-4OizVV4XT78KmHZ576YWBfILuzffa8puTBZukhqka0Uh2Ivp2WKMVli1vfz-2uTa2jJBFFnDj6EUKKJTrn-W09pzPaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لحظة توقيع اتفاقية التفاهم بين الرئيسين الايراني والاميركي.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/79161" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
