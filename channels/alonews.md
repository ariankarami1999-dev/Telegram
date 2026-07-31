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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqjru22yyIUT9TJQWgTZ3yiPYv7qVP7FnQyvzgqLN2nJzbdioa7hOA8gbc0jTUAKuqw_O2qSMO55rs7k2YNg7cwIu6SAJ5epEeafC-tCWmvSAHEZA4fHO9GlsNuPum2iyZW8eJMa2_Xw2jXod3X0Zupkt9gco3uruRX19W-NqlSDhgNklUeKn8Am9y7qEGMsgYl1gIYBWYZNB_wpPPHv14ywOYKY-3Mm2xuAfCNmK0U4Tny1HNsKOY8F6HArl_sOUAub3exzgHUCTKjgaoSXGMRAsSOKB1rY0pVO2oGRywGC6pog13PNdyWAx862NWYOFScMsnTlYjLaOzqYpdYnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfMYfmc2AK1JeAy1iTOYChq_QfN-kYcsBq2oOQiVRNHv78GevD8aUp-fLtky8wo2paVLUM-tKJKAX_bDIYTb7BFL3ufLi7ZeatU1sW1Dzvj5muhsobxAqHBJIbpR8YuDufkgurkuyWHOv9BPxESWdlRfOabqDs50YartrqfIteVJMuNhgdoI4Rk0Fzu4V4vV8n0iv4QcyrHbvLPGW4lLj0N7ljQI7eGWE37hQS2M6_4fYEVrA7lJLufFx8ZCelJNYmJykKsHNMnwE3Bw6DHW9I3wqXgrWhUkQ7mF9cqf062dxRvGzM8vQW5UWTuagkokHxyvuGVaDQ34PIozjQEqlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بر اساس تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/138968" target="_blank">📅 20:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
المانیتور: امریکا نیرو‌های باقی‌ماندهٔ خود را پیش از ضرب‌الاجل ۳۰ سپتامبر از عراق خارج می‌کند؛ سامانه‌های پدافند هوایی پاتریوت را نیز از اربیل جمع‌آوری کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/138967" target="_blank">📅 20:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=b5RS1lDc_iTabzfnWFaDzVFD6f_CGTFhiQ7UEnL9j2jj6yFNflZNcYLzfvN4Zvp3diZ9IbcDXeKN18ROTbjZ3JovzZg5oLoJ8Pg2pYUNJd1iPLi18e9JK2RYfKYG8HmcUVXJaOOJ_bOgWLe8__0CoaTCrMaKKYVkXSqHOoGizJVC_JO07O7Jyo1rrV_AN2Pngc59nYWUceFblkLX4tW1iBxGby1Jrk1cOIkCte9NPlRbnq2PbenK5rJzT_2eqlyH_iUgxrFs1GlqeJxWHFCXRBNYyvHvE7hjuDgD-EyaZlnPD7nbJNaxJJMTG7tNcWt88uw2MCGXIJs8RRHrcXUlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=b5RS1lDc_iTabzfnWFaDzVFD6f_CGTFhiQ7UEnL9j2jj6yFNflZNcYLzfvN4Zvp3diZ9IbcDXeKN18ROTbjZ3JovzZg5oLoJ8Pg2pYUNJd1iPLi18e9JK2RYfKYG8HmcUVXJaOOJ_bOgWLe8__0CoaTCrMaKKYVkXSqHOoGizJVC_JO07O7Jyo1rrV_AN2Pngc59nYWUceFblkLX4tW1iBxGby1Jrk1cOIkCte9NPlRbnq2PbenK5rJzT_2eqlyH_iUgxrFs1GlqeJxWHFCXRBNYyvHvE7hjuDgD-EyaZlnPD7nbJNaxJJMTG7tNcWt88uw2MCGXIJs8RRHrcXUlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
🔴
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/138966" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ درباره اوکراین و پاتریوت‌ها:
ما قدرتمندترین سلاح‌های جهان را داریم و باید در مورد افشای اسرار این سلاح‌ها محتاط باشیم. شما نمی‌توانید آن‌ها را کپی کنید.
🔴
این شبیه انویدیا است؛ آن‌ها یک تراشه دارند و می‌گویند که نمی‌توانید آن را کپی کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/138965" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6359aac8e1.mp4?token=Qu3_rtKo4ItzMUuljCqseXd9iCSYIndJNkmM4GM0oEWJ4fN53fX9ZW5c5Qi2dLOLMHoxsqXHfSPbbL2ag_titecBB1ERhFSIGPTYsqiOvhv2zP4sPeWCQod-gLFeVv2x0KPLxMGVXO01H9grZ_IvqmYNW0ukmVFcsrTPngNAjRcyhgA0uVBR18Y5yKjrJHR3Y9SkwRhONG-LWWt-RzW5cE2dI8axI5_MPTKfCy11PngussN8FgN1I0l4c4MKuWlyu2X6Xb4kdL_knzWQwfqIt5qXQQnHPEpsNcC7qkHxmTQCnlFJAznCwyJ9vPnYOYpM_toAqRfRM814bIXDsFx9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6359aac8e1.mp4?token=Qu3_rtKo4ItzMUuljCqseXd9iCSYIndJNkmM4GM0oEWJ4fN53fX9ZW5c5Qi2dLOLMHoxsqXHfSPbbL2ag_titecBB1ERhFSIGPTYsqiOvhv2zP4sPeWCQod-gLFeVv2x0KPLxMGVXO01H9grZ_IvqmYNW0ukmVFcsrTPngNAjRcyhgA0uVBR18Y5yKjrJHR3Y9SkwRhONG-LWWt-RzW5cE2dI8axI5_MPTKfCy11PngussN8FgN1I0l4c4MKuWlyu2X6Xb4kdL_knzWQwfqIt5qXQQnHPEpsNcC7qkHxmTQCnlFJAznCwyJ9vPnYOYpM_toAqRfRM814bIXDsFx9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
موشک تامهاوک باورنکردنی‌ترین است—می‌توانید از یک در عبور کنید، آن را از پنجره خانه عبور دهید. هیچ‌کس چیزی شبیه به آن ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138964" target="_blank">📅 20:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91678c091b.mp4?token=Uu2mhf3a4cmnnw3J0dd7vmPaMcgEcQprgl88NMLakHNZ_b0WWFXc4LO4XLxMhACg_8NeBrWJ8UeELHqtcI0pl6Vbp_bivQS-cgYfpEzxkTj8z_HDDH3MNN3dMo46RGJ7wZGlH_xVoa8WTZC6GIebclp1hL8JzApYpico_nMvzzzZOcV2Xe5YKCQZJVbnXTA4J1wFIZLK1o5VgIM94FHT0aMLt3os6JAhC-MqV_3UWwNDsWTEZ4PxwqgC6-is3mrn3UyJhI7BOyq020o9d7VCA_DgWYB4kmgfZL7I-Xl55TFLH_1KA6C8p9bx9xIVP7CQwwvyZlWBlDyMMXNTqXFdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91678c091b.mp4?token=Uu2mhf3a4cmnnw3J0dd7vmPaMcgEcQprgl88NMLakHNZ_b0WWFXc4LO4XLxMhACg_8NeBrWJ8UeELHqtcI0pl6Vbp_bivQS-cgYfpEzxkTj8z_HDDH3MNN3dMo46RGJ7wZGlH_xVoa8WTZC6GIebclp1hL8JzApYpico_nMvzzzZOcV2Xe5YKCQZJVbnXTA4J1wFIZLK1o5VgIM94FHT0aMLt3os6JAhC-MqV_3UWwNDsWTEZ4PxwqgC6-is3mrn3UyJhI7BOyq020o9d7VCA_DgWYB4kmgfZL7I-Xl55TFLH_1KA6C8p9bx9xIVP7CQwwvyZlWBlDyMMXNTqXFdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: «نیروی دریایی ایران کف اقیانوس است، نیروی هوایی‌اش رفته، رادارش رفته، رهبرانشون رفته‌اند؛ خلاصه همه‌چیز رفته!»
🔴
«
۱۵۹ کشتی داشتند؛ کل نیروی دریایی‌شان همین ۱۵۹ تا بود. الان همه‌شان کف دریا خوابیده‌اند. اگر این اسمش عملیات بزرگ نیست، پس چیست؟»
🔴
نوبت هواپیماها شد:
«۲۰۰ هواپیما داشتند؛ همه‌شان رفته‌اند، دانه‌به‌دانه. حتی یک هواپیما هم برایشان نمانده.»
🔴
پدافند هوایی؟
«خیلی خوب بود... فقط یک مشکل داشت؛ کار نکرد! حالا هم دیگر اثری از آن نیست.»
🔴
رادار؟ «
رفته
.»
🔴
رهبرانشون؟ «
رفته‌اند
.»
🔴
و بعد جمع‌بندی نهایی:
«همه‌چیز رفته.»
🔴
همه‌چیز... رفته. همه‌اش... رفته. رفته که رفته!
🔴
آخر هم با یک بالا انداختن شانه گفت:
«البته، باز هم به جنگیدن ادامه می‌دهند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138963" target="_blank">📅 20:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba80df0a.mp4?token=PllqMpRV6Sx1U21L-rRIpLUMQVTQAGeC9462saHdrSCYnwxYjU8gxVAmghnAfZKG8wHKr_iNaxZ4hN1VXv0mT0pzsCAKsQMlZc2mni5l8Dx596Rsy-t4Xqtaq3j_DBJS57t9PJQ3Olp54dOdCfZIJ87-NepniWI759f3rk5e3GK8nq3gHr_UKbpcqkZoiHqcF6wGnXMaWOdXB9SSI2kiODK567CdnqHfVVAoXtpAyI24e9jVW4y0mz5l_wW_ili3YCfpRqS2YRhYX9S67VT97eoAj-wf0-vnXKS9Ku59J4Wa3ImFzvAEWfX6007zIvCCJaz0ErrI_-xpNl_SKz9Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba80df0a.mp4?token=PllqMpRV6Sx1U21L-rRIpLUMQVTQAGeC9462saHdrSCYnwxYjU8gxVAmghnAfZKG8wHKr_iNaxZ4hN1VXv0mT0pzsCAKsQMlZc2mni5l8Dx596Rsy-t4Xqtaq3j_DBJS57t9PJQ3Olp54dOdCfZIJ87-NepniWI759f3rk5e3GK8nq3gHr_UKbpcqkZoiHqcF6wGnXMaWOdXB9SSI2kiODK567CdnqHfVVAoXtpAyI24e9jVW4y0mz5l_wW_ili3YCfpRqS2YRhYX9S67VT97eoAj-wf0-vnXKS9Ku59J4Wa3ImFzvAEWfX6007zIvCCJaz0ErrI_-xpNl_SKz9Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل و لای گیر کردند.
🔴
یک ژنرال تصمیم گرفت به جای استفاده از بزرگراه که در آنجا به خوبی پیش می‌رفتند، از میان گل و لای عبور کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138962" target="_blank">📅 20:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3931af541f.mp4?token=QIShCC7iR9ob9EE2m8V-bYoyv4-qXOkf0v3o9pCtcWLxVlL4Dm8fAyaGlbhqoNj2ZQmuYYaM_49DtviAHCgDGUjMfOjOg5_ACsVnNntCxRl5hxttrx_cA_942z2XAFXZ8K3fXJynL09Qk_B6c3kGBBk7bUdualEHMbovW3vUw342H09kAwSaNpPwLJ5SHqSF05ta9FE9W4Sh66C5ZzmdGHbbKATRJBhueeuvHxCU4kqX8aCJH8Kwco6UfD6A95EbwCgAEqgctXmUw9TU8zosfsR5MeqPWyCqRD2sVRgD6waG5R0KwvREgIToUjgJ4SOQ5blbBOHlRnUMc4IEsA1nlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3931af541f.mp4?token=QIShCC7iR9ob9EE2m8V-bYoyv4-qXOkf0v3o9pCtcWLxVlL4Dm8fAyaGlbhqoNj2ZQmuYYaM_49DtviAHCgDGUjMfOjOg5_ACsVnNntCxRl5hxttrx_cA_942z2XAFXZ8K3fXJynL09Qk_B6c3kGBBk7bUdualEHMbovW3vUw342H09kAwSaNpPwLJ5SHqSF05ta9FE9W4Sh66C5ZzmdGHbbKATRJBhueeuvHxCU4kqX8aCJH8Kwco6UfD6A95EbwCgAEqgctXmUw9TU8zosfsR5MeqPWyCqRD2sVRgD6waG5R0KwvREgIToUjgJ4SOQ5blbBOHlRnUMc4IEsA1nlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما درگیری بین هند و پاکستان را پایان دادیم. یازده هواپیما سرنگون شدند.
🔴
من گفتم: "اگر قصد جنگ کردن دارید، ما برای هر کدام از آن‌ها، تعرفه‌هایی معادل 250 درصد تعیین خواهیم کرد." آن‌ها فریاد زدند، جیغ کشیدند و هر دو طرف بسیار عصبانی بودند.
🔴
یک روز بعد، آن‌ها تماس گرفتند و گفتند: "ما جنگ نخواهیم کرد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138961" target="_blank">📅 20:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها هفت ساعت درباره موضوع هسته‌ای صحبت می‌کنند. من می‌گویم: "چرا هفت ساعت؟ این کار را می‌شود در پنج تا ده دقیقه انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138960" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138959" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گزارشگر : آیا با اطمینان می‌شه گفت که ایران پشت این حملات سایبری بوده؟
🔴
ترامپ : به نظر من مقصر اصلی ایالت مینه‌سوتاست می‌دونید کار کیه؟ مینه‌سوتا
🔴
چون اون‌ها کاملاً بی‌کفایت هستن. من اصلاً فکر نمی‌کنم این یه حمله سایبری از طرف ایران بوده باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138958" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ درباره روسیه و اوکراین:
هیچ‌کس نمی‌خواهد امتیازی بدهد، اما هم پوتین و هم زلنسکی باید برای رسیدن به توافق امتیاز بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138957" target="_blank">📅 20:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ درباره ایران: «بیشتر مردم تا حالا تسلیم شده بودند. اما آنها این کار را نکرده‌اند، پس به خاطر این موضوع به آنها اعتبار می‌دهم.
🔴
آنها سرسخت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138956" target="_blank">📅 20:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0770d9504e.mp4?token=Kj46UwUmlIVbJf-pvd9eDy8TYq7UXfkM1rO_HkNBLKFsgpxpqvrbK3ScJPSpQGsgiHG5k6muFyw8T05lFUOObluUEvWaVcYaMkaXIOWhrUAKpW2EAImvpohfFuzNv_-W3WCxOY5jS6N39diL22OUXBfSU2-YNNbI0bzmlFgHIcoTHzoU6ZpiMBk7qzyXp9BFhtGaP8-qdtj-GSM1f6vZ5B5OXCK3rDFk6zDspQL-Ix-TqPtAtt8pGm4nl_5iIEr2yzisvfGiGLGeRptuye1Yirwurc0Ldn8Tdr08ygyA67Sj-2OXXvzp5rxQ2kQ8qvz8s_VjYEk6lhyJQNadQyI44w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0770d9504e.mp4?token=Kj46UwUmlIVbJf-pvd9eDy8TYq7UXfkM1rO_HkNBLKFsgpxpqvrbK3ScJPSpQGsgiHG5k6muFyw8T05lFUOObluUEvWaVcYaMkaXIOWhrUAKpW2EAImvpohfFuzNv_-W3WCxOY5jS6N39diL22OUXBfSU2-YNNbI0bzmlFgHIcoTHzoU6ZpiMBk7qzyXp9BFhtGaP8-qdtj-GSM1f6vZ5B5OXCK3rDFk6zDspQL-Ix-TqPtAtt8pGm4nl_5iIEr2yzisvfGiGLGeRptuye1Yirwurc0Ldn8Tdr08ygyA67Sj-2OXXvzp5rxQ2kQ8qvz8s_VjYEk6lhyJQNadQyI44w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد ایران، گزارشی وجود دارد که می‌گوید شما پیشنهادی از ارتش برای اقدام بزرگ دریافت کرده‌اید.
🔴
ادعای ترامپ: ما قبلاً اقدام بزرگ انجام داده‌ایم. چه اقدام بزرگی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138955" target="_blank">📅 20:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ در جلسه کابینه خود باره ایران : ما می‌توانیم با ایران به توافق برسیم، اما به دلیل دروغ‌گویی آن‌ها، اعتمادم به آن‌ها در حال از دست رفتن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138954" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ab421b66.mp4?token=EXDV6kN3XeB0_iOc3faRDDpT9pAwesZa__YmCmpztVBJcQm-5GPhOZmzKCNziBp8x_XfB5FC3tImOTK7dz285Ezi-OjOOdZ6TnLc4E_ur_40DPDCG-tPPPBVUVCXQaTwuy9ygF5qZqzkqAL0FJ7ljik-kOkgF3g47OriBorxuI4KRExzl-wHTyITIDd0RoiDu1hzRoGFZfBRdc222-iDpKLWJb4I2Z0g__BUc-IYjLQY160YINIk6UpPdCdYtBp4J-HWKyahxbMozvqhawCcVcdLjrD_kA0LKtCLdg9_0eV1Ri6o0v2t-gU89zTkZnO0sxc5uc_0TIh9v1_t_E0wWoiJMmJUHPi8i_Is8Vtzvicdpp04UIPVY_eNGxN8S8qrBoEf8ks59Z4L3VTXDBqtQpVHr2KiL0DbrTqYnJkEObedRCH4UN8i4hBubvlYXGw4MEuJv7s75zoX0RSPNmK8npFhuoALHwoc-YzXJyN3rH4YUrXboo8KzfYE-18B0IaFI6GiMYSvMflREOsFNZqeA7T0RjLtoFWC_11ML9stTVbKbohS81MEVSLXt5Xv_9uxrmqm8vpfK4w96UROey554s8-4Y7lPLpOQ0KIaADnd2eXo14TNCorggFci0CkC1ynIM2GnIbdxTEZD8B16n6Et4QoJ6M8-zbpzr5bocyf7IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ab421b66.mp4?token=EXDV6kN3XeB0_iOc3faRDDpT9pAwesZa__YmCmpztVBJcQm-5GPhOZmzKCNziBp8x_XfB5FC3tImOTK7dz285Ezi-OjOOdZ6TnLc4E_ur_40DPDCG-tPPPBVUVCXQaTwuy9ygF5qZqzkqAL0FJ7ljik-kOkgF3g47OriBorxuI4KRExzl-wHTyITIDd0RoiDu1hzRoGFZfBRdc222-iDpKLWJb4I2Z0g__BUc-IYjLQY160YINIk6UpPdCdYtBp4J-HWKyahxbMozvqhawCcVcdLjrD_kA0LKtCLdg9_0eV1Ri6o0v2t-gU89zTkZnO0sxc5uc_0TIh9v1_t_E0wWoiJMmJUHPi8i_Is8Vtzvicdpp04UIPVY_eNGxN8S8qrBoEf8ks59Z4L3VTXDBqtQpVHr2KiL0DbrTqYnJkEObedRCH4UN8i4hBubvlYXGw4MEuJv7s75zoX0RSPNmK8npFhuoALHwoc-YzXJyN3rH4YUrXboo8KzfYE-18B0IaFI6GiMYSvMflREOsFNZqeA7T0RjLtoFWC_11ML9stTVbKbohS81MEVSLXt5Xv_9uxrmqm8vpfK4w96UROey554s8-4Y7lPLpOQ0KIaADnd2eXo14TNCorggFci0CkC1ynIM2GnIbdxTEZD8B16n6Et4QoJ6M8-zbpzr5bocyf7IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه کسی از دولت با ایران صحبت می‌کند؟
🔴
پرزیدنت ترامپ: آن‌ها همیشه می‌خواهند صحبت کنند... استیو، جرد، جی‌دی و مارکو درگیر هستند.
🔴
گزارشگر: ایران می‌گوید مذاکراتی در حال انجام نیست
🔴
ترامپ: ممکن است مدت طولانی درباره هسته‌ای صحبت کنیم و سپس آن‌ها بیرون بروند و بگویند: «ما هرگز درباره هسته‌ای صحبت نکردیم...» آن‌ها فقط کاری می‌کنند که عصبانی شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/138953" target="_blank">📅 20:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a12328c23.mp4?token=hxA5jl2nDaWCeEnueK9Il2rgZAPlUEXhHkrfbhfVnkoW2OuhRkaP8CjZWYJ6ATQ6tf_wbHytSuTQSVFppBdkfZTHFP7OnfoAnurASpuwQGG0OzYmRTmyoTPN-uOV0JjVZclLJz2Te6pgu7ys90HTpGOWWFI1m0iKDm8La7M9TljrDrKlNkD6GGKpPc0QhXdA4nsaB-B51jgZ8KxtbrSdaSbyO3TPlJZtFW1hIxs9q3CHXguobPBWSphru3NofaWBeraS3-wxsswaGcTLdUeDmcXO3N2amJYxSS3-b7_icU2_uXlhQB38EXsYoFUPbPZn6PJbCznh4R-EbItHK_WjaAJ5eNpeeeEDhSQ52ErRNv93W1h1XE8yJjpOKaXT4Dm9SxkfpQPS0u0ft2DxWpNSuPKOJ_dhoG6pKAfCUn6H1xumEyiqnvCVUWDkp9U0rLOp6h29TVJzF8PqptMV56DqU0oFWQ48V87YHH41hwTNkf5DeIvWEhRvGMq3868rSzGk2PyE63YVrKf6Mlz4Klaea-dIO4AkBi7uihqV5FkOLFOzv5PJgtrI7JS1AiittF4voLGbp02EtK2DGMWdGaYRCs8A4vV8BGSQCfWE5OJrhkpDux3PbnLk0ByIOU6j6jFaU0mzCbQ7c2qkGOF_8CFWLifHSbEYA9S-YmGr_HBzP8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a12328c23.mp4?token=hxA5jl2nDaWCeEnueK9Il2rgZAPlUEXhHkrfbhfVnkoW2OuhRkaP8CjZWYJ6ATQ6tf_wbHytSuTQSVFppBdkfZTHFP7OnfoAnurASpuwQGG0OzYmRTmyoTPN-uOV0JjVZclLJz2Te6pgu7ys90HTpGOWWFI1m0iKDm8La7M9TljrDrKlNkD6GGKpPc0QhXdA4nsaB-B51jgZ8KxtbrSdaSbyO3TPlJZtFW1hIxs9q3CHXguobPBWSphru3NofaWBeraS3-wxsswaGcTLdUeDmcXO3N2amJYxSS3-b7_icU2_uXlhQB38EXsYoFUPbPZn6PJbCznh4R-EbItHK_WjaAJ5eNpeeeEDhSQ52ErRNv93W1h1XE8yJjpOKaXT4Dm9SxkfpQPS0u0ft2DxWpNSuPKOJ_dhoG6pKAfCUn6H1xumEyiqnvCVUWDkp9U0rLOp6h29TVJzF8PqptMV56DqU0oFWQ48V87YHH41hwTNkf5DeIvWEhRvGMq3868rSzGk2PyE63YVrKf6Mlz4Klaea-dIO4AkBi7uihqV5FkOLFOzv5PJgtrI7JS1AiittF4voLGbp02EtK2DGMWdGaYRCs8A4vV8BGSQCfWE5OJrhkpDux3PbnLk0ByIOU6j6jFaU0mzCbQ7c2qkGOF_8CFWLifHSbEYA9S-YmGr_HBzP8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران
:
ما فقط می‌خواهیم پیروز شویم. ما خیلی خوب عمل می‌کنیم.
🔴
ما سعی می‌کنیم مهربان باشیم، تا جایی که می‌توانید در چنین شرایطی مهربان باشید.آنها در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/138952" target="_blank">📅 20:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62eddc2fc0.mp4?token=CEVcWdtaB1ddxtFjImVwx6GFp9gmfAE8EmLRqcQw0jhuY_Rf5TOIyKhRcxwZI1MU4y6aN5cAplJsxLDfdOohrIqDEDST07OlBuFmnQHbk9EllwIQ1L2HauIvqlgGrootI9laef6ZIEH8RurDIhf6mvPvsiS6uYYR8QNjIBUWXGNRsxgTv6RTwoncvPAW2vwfB7FLG55198GjxHfH404UD5s3wG9rHtWPNYWVVCjJbWkmdoWpNqouzxVww69rBj0qlrx_u9yc__43UsJ8KJA1-Rdr5OIYYqMLrZKRztfvrdBvAwtp_-irkswlGR3KcCa3gQtP3Qos0VDgAnU2wTXUNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62eddc2fc0.mp4?token=CEVcWdtaB1ddxtFjImVwx6GFp9gmfAE8EmLRqcQw0jhuY_Rf5TOIyKhRcxwZI1MU4y6aN5cAplJsxLDfdOohrIqDEDST07OlBuFmnQHbk9EllwIQ1L2HauIvqlgGrootI9laef6ZIEH8RurDIhf6mvPvsiS6uYYR8QNjIBUWXGNRsxgTv6RTwoncvPAW2vwfB7FLG55198GjxHfH404UD5s3wG9rHtWPNYWVVCjJbWkmdoWpNqouzxVww69rBj0qlrx_u9yc__43UsJ8KJA1-Rdr5OIYYqMLrZKRztfvrdBvAwtp_-irkswlGR3KcCa3gQtP3Qos0VDgAnU2wTXUNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
:
با توجه به اینکه حماس طبق این برنامه سلاح‌های خود را تحویل می‌دهد، چه کسی را مسئول دریافت سلاح‌های آن‌ها می‌دانید؟
🔴
ترامپ
:
هیئت صلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/138951" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783659570a.mp4?token=Ke3YZxkEr-sgBacLg3DEntUzsUGqXbrmf7THgEVLannASyKw4_ZdDD4iv9Tx1w4KVbdEUjP4xT7mF5iRGOMUeJhmEQr_sBgRS6FtlMncCauvaCLi7jHoi4pXQqMIh89IzNkOfKms8ybfiLRfTiD0uP1jtRaA1nK6apkoZ0IkdjA3WKR10s8wRGhp3SqMOpsSLjRE1zT5OFTTX6Ln3-hYqubHz7-BMkgrJ2IraoWRcWVrQmhUVlr6rGevEv1ZS29zsKJ-Nc-NZU0xIBGAYi4aA1OWl6zBoj8C15okEqQjXGIZyonUxatCvLRWYUWXkjNxK5adqqpTsNLIuEcRfYIzrZW8aA2wQcy6ukLKo-pD1GHP9V_DXrRcdWssGA1TSZZ_LaYGTDQ9vn1eVru_TMcwp3nv-VeBLGAzgzVyxtQaS9820qKOb_2GducyLB12Y_-rQSQ-1IdFz5IOKQj98DFk4Nfjy534aIBzVFqIkJI4EghFy7H9_8Q-kGynKS5fy4yfkKe2hBpOoMBYNNKlwHA7VIK1B4bmDFe6sgnnFay_pqeYPyjE7eebFHbS1yJIRQGdw0O1acpDdISRlpBxS8QuxPOKwyTMV0mGjTKXKQPyMzWycN-KBLal5J6d-itJCR2UuwqDB6M5sZc1aOZd57QozrdljV8BkD3jfBW-yFef-0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783659570a.mp4?token=Ke3YZxkEr-sgBacLg3DEntUzsUGqXbrmf7THgEVLannASyKw4_ZdDD4iv9Tx1w4KVbdEUjP4xT7mF5iRGOMUeJhmEQr_sBgRS6FtlMncCauvaCLi7jHoi4pXQqMIh89IzNkOfKms8ybfiLRfTiD0uP1jtRaA1nK6apkoZ0IkdjA3WKR10s8wRGhp3SqMOpsSLjRE1zT5OFTTX6Ln3-hYqubHz7-BMkgrJ2IraoWRcWVrQmhUVlr6rGevEv1ZS29zsKJ-Nc-NZU0xIBGAYi4aA1OWl6zBoj8C15okEqQjXGIZyonUxatCvLRWYUWXkjNxK5adqqpTsNLIuEcRfYIzrZW8aA2wQcy6ukLKo-pD1GHP9V_DXrRcdWssGA1TSZZ_LaYGTDQ9vn1eVru_TMcwp3nv-VeBLGAzgzVyxtQaS9820qKOb_2GducyLB12Y_-rQSQ-1IdFz5IOKQj98DFk4Nfjy534aIBzVFqIkJI4EghFy7H9_8Q-kGynKS5fy4yfkKe2hBpOoMBYNNKlwHA7VIK1B4bmDFe6sgnnFay_pqeYPyjE7eebFHbS1yJIRQGdw0O1acpDdISRlpBxS8QuxPOKwyTMV0mGjTKXKQPyMzWycN-KBLal5J6d-itJCR2UuwqDB6M5sZc1aOZd57QozrdljV8BkD3jfBW-yFef-0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اوکراین و سامانه پاتریوت‌ها: باید بسیار محتاط باشیم در اجازه دادن به کسی برای ساخت سلاح‌های پیشرفته ما
🔴
ما به این موضوع موافقت نکرده‌ایم. در حال صحبت درباره آن هستیم. دادن آن نوع فناوری کار دشواری است.
🔴
آن کسانی که به آن‌ها فناوری می‌دهید نیز می‌توانند علیه شما برگردند. این امکان‌پذیر است.
🔴
باید بسیار محتاط باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138950" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=AcdC1ti66psmAy5gmFhES2mDIHrRig_Y-HN5Ql5sRIda5Sxp7C2T-whxMlgvJnGvxk-7y0v4j29tMQzI6l7_ogCFOYr52mpqBY5hgPW41S_vNrYFe8yqsPuaOGbi9KKCjrUXHQcvNK63mhuWCYUNc3_PZb-CycDGbJAZ72H0JCmpNXqLlbJBKNtzCa-zGxKaHVZLw1R-c9WFCljIg37zNwCzo0OAOv_ew0pP35R7cA7oHhl82_1KPkspEdiGBmapYULVvua0-EQmLUal3-VVlwZVo-Bd_SHB5f2RaABMplOvXrbL7qpOJ2_CTo6NiylBwdGce32RaChwWCJBbXxPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=AcdC1ti66psmAy5gmFhES2mDIHrRig_Y-HN5Ql5sRIda5Sxp7C2T-whxMlgvJnGvxk-7y0v4j29tMQzI6l7_ogCFOYr52mpqBY5hgPW41S_vNrYFe8yqsPuaOGbi9KKCjrUXHQcvNK63mhuWCYUNc3_PZb-CycDGbJAZ72H0JCmpNXqLlbJBKNtzCa-zGxKaHVZLw1R-c9WFCljIg37zNwCzo0OAOv_ew0pP35R7cA7oHhl82_1KPkspEdiGBmapYULVvua0-EQmLUal3-VVlwZVo-Bd_SHB5f2RaABMplOvXrbL7qpOJ2_CTo6NiylBwdGce32RaChwWCJBbXxPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138949" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7681e354db.mp4?token=cqZxSVpFMCHE1lupoCgeUA8KXtdPDnDj_JSn51Xz7q9qsqEdXvUoEZ6_h5Gubv1PV_axq5beP0WBTRQQTjgQlGLf8gtT3O4oC7S5cZt9Z_UiXxbAjxSFcv88MzK2MQybq8a_Y9Be2-2r-5GdmRmDgCh4Eew0Blqstxhar80uApmhaZOi-WqRmMnu72dFE8Jeh2MyYEVos9wx30nd6GcZ3wvVnWUrumRnAImKehet_rShw2OsDHGHqHrNDV0XCcqD0qDI06OcedWwwJ6ls2gAocOE9HZGpCikiMuB9-azME5-OP8LtRDCRku8Tk18D43yLsvLzxn-aqOQsuUPNCcV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7681e354db.mp4?token=cqZxSVpFMCHE1lupoCgeUA8KXtdPDnDj_JSn51Xz7q9qsqEdXvUoEZ6_h5Gubv1PV_axq5beP0WBTRQQTjgQlGLf8gtT3O4oC7S5cZt9Z_UiXxbAjxSFcv88MzK2MQybq8a_Y9Be2-2r-5GdmRmDgCh4Eew0Blqstxhar80uApmhaZOi-WqRmMnu72dFE8Jeh2MyYEVos9wx30nd6GcZ3wvVnWUrumRnAImKehet_rShw2OsDHGHqHrNDV0XCcqD0qDI06OcedWwwJ6ls2gAocOE9HZGpCikiMuB9-azME5-OP8LtRDCRku8Tk18D43yLsvLzxn-aqOQsuUPNCcV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ در مورد ایران: ایران سلاح‌های ضد هوایی بسیار خوبی داشت، اما این سلاح‌ها کارایی نداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138948" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a4937b8c.mp4?token=neQP62BPrrLNBAhnTTE8Slb7llMqESR0IqfFDWT5NmmeAuPtFUJzm5EXSEuEmccfnF1zbuGW_mvfMqE0BlSFtdDp4prM6YAPbs-H7B3mGw-N_aIqHy0UU20Rz6xiWWB_5mLQJN5HY92wK3R4_0MRp6aovOLQBnsQWdS_8rqh28vg37k8vBcBMx5dZ2jfJLQQgGlQQaTbYA1V1Sg8qCuznoedGOUwDIfeXVYll6LcfrIrQeUF6lHmgE73E5ylNPYedYabuqJCKvKT71X4rXuECVFf_zY9npUh30i5XkvkXxMoZ7oNyAy7GsU7Ua8QnntBlvJjvsX3V3aUxFgYyKIehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a4937b8c.mp4?token=neQP62BPrrLNBAhnTTE8Slb7llMqESR0IqfFDWT5NmmeAuPtFUJzm5EXSEuEmccfnF1zbuGW_mvfMqE0BlSFtdDp4prM6YAPbs-H7B3mGw-N_aIqHy0UU20Rz6xiWWB_5mLQJN5HY92wK3R4_0MRp6aovOLQBnsQWdS_8rqh28vg37k8vBcBMx5dZ2jfJLQQgGlQQaTbYA1V1Sg8qCuznoedGOUwDIfeXVYll6LcfrIrQeUF6lHmgE73E5ylNPYedYabuqJCKvKT71X4rXuECVFf_zY9npUh30i5XkvkXxMoZ7oNyAy7GsU7Ua8QnntBlvJjvsX3V3aUxFgYyKIehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: دولت بایدن و دولت اوباما، دولت را به ابزاری تبدیل کردند و زندگی‌ها را نابود کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138947" target="_blank">📅 19:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گزارشگر : درباره ایران، گزارش‌هایی منتشر شده که می‌گه ارتش به شما پیشنهاد داده اقدامات گسترده‌تری انجام بدید.
🔴
ترامپ : ما که همین حالاش هم اقدامات خیلی گسترده‌ای انجام دادیم. اصلاً منظورتون از «گسترده‌تر» چیه‌؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138946" target="_blank">📅 19:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ درباره توافق غزه : اسرائیل از این توافق خیلی خوشحاله
🔴
توی رسیدن بهش هم خیلی بهمون کمک کرد و واقعاً خوب عمل کرد.
🔴
هیچ‌کس فکر نمی‌کرد همچین چیزی ممکن باشه؛ اینکه حماس خلع سلاح بشه.
🔴
این نشون می‌ده که ما در قبال ایران چقدر موفق بودیم. اگه برگردیم به چهار یا پنج ماه پیش، همچین توافقی اصلاً امکان‌پذیر نبود.
🔴
این یه قدم خیلی بزرگ برای خاورمیانه‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138945" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روبیو: ما در خاورمیانه به موفقیت‌های دیپلماتیک دست یافته‌ایم
🔴
توافق بین لبنان و اسرائیل بی‌سابقه است.
🔴
توافق حماس برای خلع سلاح یک دستاورد است
🔴
هنوز کارهای زیادی در رابطه با لبنان و اسرائیل برای حفظ و ایجاد این صلح باید انجام شود، اما این یک هدف قابل دستیابی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138944" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیرجنگ آمریکا: تعهد ما تزلزل‌ناپذیر است که ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138943" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc88001f8.mp4?token=cmgTkAESxVSjpBWOsDe-k1ewCO6DTaHLz2HiN6VuUmuGz6158VEZIiQR-hm9saZdiypcoKetkRgmwbx4FQCSpa_syoKohBtGlW594_JpexsiqtVMwvprJF9eJk92WZq0PM_NOjvXKa4J0ImI4Uv4zpgBtMX__v8kflaGYsZpxd8JPn3flf5fSCdRyxv9RBwgg_KXUR5BVbzeuannNgB2s1CbSxAeqZK_Y2ZHLFgZQl10FzN6XN9Cgccg6nJ-dHc05c9kPckFUffpjLNChpQwBpgAtbh_sluYGw3Km9SCvC8z5qofrFFzfoD2LtHXu6MDP2u-ms_W7ugsP5FNQcbY_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc88001f8.mp4?token=cmgTkAESxVSjpBWOsDe-k1ewCO6DTaHLz2HiN6VuUmuGz6158VEZIiQR-hm9saZdiypcoKetkRgmwbx4FQCSpa_syoKohBtGlW594_JpexsiqtVMwvprJF9eJk92WZq0PM_NOjvXKa4J0ImI4Uv4zpgBtMX__v8kflaGYsZpxd8JPn3flf5fSCdRyxv9RBwgg_KXUR5BVbzeuannNgB2s1CbSxAeqZK_Y2ZHLFgZQl10FzN6XN9Cgccg6nJ-dHc05c9kPckFUffpjLNChpQwBpgAtbh_sluYGw3Km9SCvC8z5qofrFFzfoD2LtHXu6MDP2u-ms_W7ugsP5FNQcbY_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: درباره ایران، گزارشی منتشر شده که می‌گوید ارتش به شما پیشنهاد داده عملیات را در ابعاد بسیار گسترده‌تری انجام دهید.
🔴
ترامپ: ما همین حالا هم اقدام بزرگی انجام داده‌ایم. دیگر «بزرگ‌تر» یعنی چه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138942" target="_blank">📅 19:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca9802ae.mp4?token=ILJVX-h0cjPWQINg52CC2s7G9ft4JWxHfr_L6Uo_Fxf5R8NMkwgQ4o17-sTSMjYcyHv_sNmr1L7bIcPdeTKfXEKXD6e0Me2Bo_8WJXP4cmNC6937aM1L4tk9kORD5i-YCfmTPe7Z_JaHQHk5vrTdk4Ne9ab3SArJYfMp4LUyAjXHEQE3VpOIDb-UHNAaF2fAad-0CrOzUgAbC-A3YxmJvIcNFVSkdVrlq6s0dnW1rkxRkIVPq4prnzgGHp6oqdOMZgG3L5wyaTZ6VMOCTnczqiMVXuxxi8q61BPdSfUFOrgvaU-BIR9eFmaDwNHLXcYXqB4dF9qN5J8GrndSri9Y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca9802ae.mp4?token=ILJVX-h0cjPWQINg52CC2s7G9ft4JWxHfr_L6Uo_Fxf5R8NMkwgQ4o17-sTSMjYcyHv_sNmr1L7bIcPdeTKfXEKXD6e0Me2Bo_8WJXP4cmNC6937aM1L4tk9kORD5i-YCfmTPe7Z_JaHQHk5vrTdk4Ne9ab3SArJYfMp4LUyAjXHEQE3VpOIDb-UHNAaF2fAad-0CrOzUgAbC-A3YxmJvIcNFVSkdVrlq6s0dnW1rkxRkIVPq4prnzgGHp6oqdOMZgG3L5wyaTZ6VMOCTnczqiMVXuxxi8q61BPdSfUFOrgvaU-BIR9eFmaDwNHLXcYXqB4dF9qN5J8GrndSri9Y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما به آنها ضربه بسیار سنگینی وارد خواهیم کرد. در یک مقطعی، آنها خواهند گفت: "دیگر نمی‌توانیم این وضعیت را تحمل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138941" target="_blank">📅 19:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTSlxQDJg7tCIgh3LKEhRkVGb4sI7JkbHUZSUwXS0qMHg2_SCGHXDiFIix6vbf4JtWhvYSBz-1U1SCtjdRQecR8ZeQOuEmIbnG4ulsZRSzxcIq6CEVIVim3eTSslC2NL1uyGo48lRAYPy65ParjswbVDydkwP6W85if9wOxlbvBP7NUOhdKxtif4FWQLrz24yLM8MKRoQrUcSdSbYhVXzPa1iSJkkvSDkWB2gHistAKnzzogITPqi4-gRCL6JN1kPYnw9EqM1-hPI3dix0TQyztGeEp5XDhawkQ0tvclz3YSvOPfky7QZEyuK6zMQyTB8Vt9kqPdDN-lYX_HeSmT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام
🔴
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
🔴
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138940" target="_blank">📅 19:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5ffc0577.mp4?token=FBKk9HVDEbigvNnpvh7ghd-fVemDuxqu9NeQ7cCskL5Sx_sWuEYqQ_chZbPg4SYx00rho2_C6a9rP4HdGNj7p9fx4IegaI2OvLdbIKZPGM-t5-COOUQhr6rnxihEznw_UTq7RxePVEDpJDAEx_CeEoaGMd42_IaQTuYwoBUxxr35LEg_ornr2HPdTLkLdMUo8FnnxqRCiLNqWFsAKVJHYm1BaLaZcrKXuPZLQA1tMh5oARdF9A3S9_eAvYhHc991Inr9ZU4uD96-cAD3MNKkk9f2He_JtdmCZFvG6-0vAauzDN02koNrKAbXUphW59NuQlYWN1GJr1UtNIrP1F1tHALClV9xaUviNsGDL7sMUTaPBHWtIZ1MawSfpOpYCtjKZeLp3NecOr0EPJOvpz2FnaWuVirz8dSbHlHsNr7OXpTaZMuKLY1JSYYJX29vw0BzuQeh_z4w0zKXayXutiZTVBhQbQzeytYnlJujeN750Xy-AAQwn8mHqvAC9tbJA6OtOG12uGzSaxTAViCLIfwFeqBMoQUiMNeXLZ-8EGqmOWLjKnBc5cBrqwk8sFS4b2i1yfl1YHtBOO_1P4ux-xqxZ_Pyxp3PRsUPTXlOonCjfiuVmpNo6XRv7Ro8CTKW8cI1jLa7vBn5jvHLlx3GQ-i36upNK9wPO6rxzJ8TYkozU_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5ffc0577.mp4?token=FBKk9HVDEbigvNnpvh7ghd-fVemDuxqu9NeQ7cCskL5Sx_sWuEYqQ_chZbPg4SYx00rho2_C6a9rP4HdGNj7p9fx4IegaI2OvLdbIKZPGM-t5-COOUQhr6rnxihEznw_UTq7RxePVEDpJDAEx_CeEoaGMd42_IaQTuYwoBUxxr35LEg_ornr2HPdTLkLdMUo8FnnxqRCiLNqWFsAKVJHYm1BaLaZcrKXuPZLQA1tMh5oARdF9A3S9_eAvYhHc991Inr9ZU4uD96-cAD3MNKkk9f2He_JtdmCZFvG6-0vAauzDN02koNrKAbXUphW59NuQlYWN1GJr1UtNIrP1F1tHALClV9xaUviNsGDL7sMUTaPBHWtIZ1MawSfpOpYCtjKZeLp3NecOr0EPJOvpz2FnaWuVirz8dSbHlHsNr7OXpTaZMuKLY1JSYYJX29vw0BzuQeh_z4w0zKXayXutiZTVBhQbQzeytYnlJujeN750Xy-AAQwn8mHqvAC9tbJA6OtOG12uGzSaxTAViCLIfwFeqBMoQUiMNeXLZ-8EGqmOWLjKnBc5cBrqwk8sFS4b2i1yfl1YHtBOO_1P4ux-xqxZ_Pyxp3PRsUPTXlOonCjfiuVmpNo6XRv7Ro8CTKW8cI1jLa7vBn5jvHLlx3GQ-i36upNK9wPO6rxzJ8TYkozU_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا در جلسه کابینه دولت: ما در مارس 2025 شروع کردیم. در دسامبر 2025، بزرگ‌ترین بانک در ایران فرو ریخت.
🔴
بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد. آن‌ها اکنون قادر به پرداخت حقوق سربازان خود نیستند.
و به سفارش شما، ما در سرتاسر جهان به دنبال دارایی های آنها هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138939" target="_blank">📅 19:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uiuj51xxTSINhzZEh3R4qTkjV5yXEHFN8sfeSQcLysVWpR_21SiMvE8JAqoNKnBQ9k46VTGHB8dmIYXQVC9LiH_MoVpK8HwY8iLfSU3NTU_lfGzWv4pJdg9fbVtrn4tO5U1SKWSazMnbZyrZp_-ADu_cqyxeBteUq6PZA_kSDC73lOx3jKzd66WqTavz5-FSVhPqPnbA9cX6A0ftNRpt0ATeyLSrA_XkDXItTAqwsZmFraJf8Tsg4peRqODAbBCM__G6CQg2R5BCk5kauEnrdgkIP8mC9WUNupUsNEqmvgZfmxUJHTguTUP2VCSO8jBxTG5HOQLlrZMPxYGrIbYXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده آمریکا: ایالات متحده در کنار مردم اسپانیا و تمام اروپایی‌ها، در برابر این نقض فاحش حاکمیت و حقوق بشر آن‌ها می‌ایستد.
🔴
این حادثه غیرقابل قبول، نتیجه مستقیم تلاش‌های عمدی دولت اسپانیا برای امکان‌پذیر کردن و تسهیل مهاجرت غیرقانونی انبوه به اروپا است.
🔴
ما در حال بررسی اقداماتی برای دفاع از آمریکایی‌ها در داخل و خارج از کشور در برابر این تهدید هستیم و آماده‌ایم تا به سایر متحدان اروپایی که گزینه‌های مشابهی را در نظر می‌گیرند، کمک کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138938" target="_blank">📅 19:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رویترز: روسیه برای کاهش کمبود سوخت ناشی از حملات اوکراین به پالایشگاه‌های بزرگ این کشور، ۳۰ هزار تن بنزین از مراکش وارد کرده
🔴
مسکو همچنین برای تأمین سوخت به هند، بلاروس و قزاقستان روی آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138937" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا در جلسه کابینه دولت درباره استیو ویتکوف:
🔴
ما بهترین مذاکره‌کنندگان جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138936" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=Zvda12r8ltMrY1Wv6FGnv8jdLDQVVWEkCs1zywfUGaOJJ9RbTp8w6THsA3mjwjNXBOW3K9o8ln3iy9RK-8qAbd47b6xmXkS7XcA7DU6esD1JDvHwVXm2UlCjAupvEdjpBWXXmUTju-P_7sU9WtcU5w9CLZ-AFzku9-N1BPUpk6xvUXE2AiUJH7oCmtaphE5AZCYmdYclk9q198X0BqBc6VNGhvRjc6PHQLazASBSPVw89t7thbc7HqaupvMHkl8lgk70XxEY874zDgCOHBkUO-yVZJGvZ8DKCG-nOxx95-r4_d6K41tSq8wSMRT2x7ZNUQKF32VVRgidGh3j6m5oXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=Zvda12r8ltMrY1Wv6FGnv8jdLDQVVWEkCs1zywfUGaOJJ9RbTp8w6THsA3mjwjNXBOW3K9o8ln3iy9RK-8qAbd47b6xmXkS7XcA7DU6esD1JDvHwVXm2UlCjAupvEdjpBWXXmUTju-P_7sU9WtcU5w9CLZ-AFzku9-N1BPUpk6xvUXE2AiUJH7oCmtaphE5AZCYmdYclk9q198X0BqBc6VNGhvRjc6PHQLazASBSPVw89t7thbc7HqaupvMHkl8lgk70XxEY874zDgCOHBkUO-yVZJGvZ8DKCG-nOxx95-r4_d6K41tSq8wSMRT2x7ZNUQKF32VVRgidGh3j6m5oXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا در جلسه کابینه دولت: شما متعجب هستید که حوثی‌ها در این درگیری درگیر نیستند، با وجود اینکه آن‌ها نیابتی از ایران هستند؟
🔴
زیرا آن‌ها وزن قدرت آمریکا را به مدت ۴۵ روز احساس کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138935" target="_blank">📅 19:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: «هیچ اطلاعاتی وجود ندارد که نشان دهد دیوان کیفری بین‌المللی به دنبال من است.
🔴
البته ممکن است چنین اتفاقی بیفتد؛ فقط خواستم این را بدانید.
🔴
مارکو روبیو در تلاش نیست از من دفاع کند. او در تلاش است از بنیامین نتانیاهو و افراد مختلف دیگری دفاع کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138934" target="_blank">📅 19:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd841332e.mp4?token=XlR2upzkQnJy6Lz8KO7-DGneI1guskO5flbxrruRfSXRv22SQCNLLX-KLWqNI9VKshuY6RHPNww2wlSu3nE1bpSli1I8UBRHLEGrwIHA1xhUH68VMbOOfrYH3OJq_AeLI9Y3iyiQijh9ayJjRhLfzSqFheCl3_IMu370yENTPfngX7mSojBLWpR1rGNwgvZeh9aqvIQo416PzFCJziMeOsybLRAQ-dGarlao5UVIC8Dayf_eaX2dKPidX6VJsm4q1NgKLZa1woTq2dvrigPJR90NZlT8z5p6oOT7pbNluI6nU4hHCB-fH0z5cr8DqckS2XyChOug-O_RP-DAi8379g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd841332e.mp4?token=XlR2upzkQnJy6Lz8KO7-DGneI1guskO5flbxrruRfSXRv22SQCNLLX-KLWqNI9VKshuY6RHPNww2wlSu3nE1bpSli1I8UBRHLEGrwIHA1xhUH68VMbOOfrYH3OJq_AeLI9Y3iyiQijh9ayJjRhLfzSqFheCl3_IMu370yENTPfngX7mSojBLWpR1rGNwgvZeh9aqvIQo416PzFCJziMeOsybLRAQ-dGarlao5UVIC8Dayf_eaX2dKPidX6VJsm4q1NgKLZa1woTq2dvrigPJR90NZlT8z5p6oOT7pbNluI6nU4hHCB-fH0z5cr8DqckS2XyChOug-O_RP-DAi8379g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:ما پنج ماه است که درگیر این موضوع هستیم؛ اگر به ویتنام نگاه کنید، آن‌ها ۲۰ سال درگیر آن جنگ بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138933" target="_blank">📅 19:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: این عصر طلایی آمریکاست و جنگی در جریان داریم؛ حدس می‌زنم بشود آن را جنگ نامید، من آن را یک عملیات نظامی می‌نامم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138932" target="_blank">📅 19:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: ایران دیگر نیروی دریایی در اختیار ندارد و توانمندی‌هایش  در زمینه پرتاب پهپادها از بین رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138931" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: آنها چند موشک دارند، اما تعدادشان خیلی کمتر از ۴-۵ ماه پیش است. قابلیت‌های تولیدشان تقریباً به‌طور کامل از بین رفته است. ما بقیه قابلیت‌هایشان را نابود خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138930" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: ایران در تعاملات بسیار فریبکارانه عمل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138929" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ : ایران الان وضعیت خیلی بدی داره؛ واقعاً خیلی، خیلی بد. روزهای خیلی سختی رو پشت سر می‌ذاره
🔴
کار کردن باهاشون هم خیلی سخت بوده؛ پر از بی‌اعتمادی و بی‌صداقتی
🔴
ولی در نهایت فرقی نمی‌کنه، چون الان تو وضعیت خیلی، خیلی بدی قرار دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138928" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b517d36837.mp4?token=Mlp2ODjnxc3mid84NYgD3AUDuv7vgC5qnVPxPlmg2_QbUAKpqtpL3cK7oxnDZyhi4WGFgIve-QgupB-LiSc9qPma0jvm6QJ3DdJMqKB5fuGedycxJOIifRbGzXyN-AzjKlKbhKr1rbcrW1N_P7v_G8CYhPuJF2x-GSP_IcmSzlljCCV-WfEU0fQM3_3l1W0laAGS8G_dAhWI-oAk4JFogmMuYTi9n_Vwyq-HiQfip9iKxlEY7j2Bmh8uDXL-h9h1T-kdCmGDpDCdS2kJPar5jXbdmctrjE6IzsZR-GvK5ty8DHLNHZPAQayS0z3X9LEjyzpugNURAMYMis3_l9dfq6Et1yH09dPeGWUbMVkrBVV1RpFX8GBPCXNmHrptBHjtW7lGNXkkFRxhjwtVCPmu8M3R8BKOp6ivrnYGBXdvyJYlh6ilVrK_Wm8enuHX3GMGtOzmYZxsqz3VH_Jvgq5i-he23WvFMSj6GjK1jrRAnNCiPrkjv48oPUVV-3hUhAify3GYAhe4V2elKeX7Zr1J1rF-VMdujRtMcH-6bH-FsAFX7XbNCHhIFEhWCCIju2o28QvKyjYinNnQ4j-1y8biIBfzkH0_mHHBgPoiAudP_BcmGQVubmI1AIPgpqXOTIhsur6f__kI5IfQamJWBdwKw3o7sFu1iGjAnIqYN-YMzt4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b517d36837.mp4?token=Mlp2ODjnxc3mid84NYgD3AUDuv7vgC5qnVPxPlmg2_QbUAKpqtpL3cK7oxnDZyhi4WGFgIve-QgupB-LiSc9qPma0jvm6QJ3DdJMqKB5fuGedycxJOIifRbGzXyN-AzjKlKbhKr1rbcrW1N_P7v_G8CYhPuJF2x-GSP_IcmSzlljCCV-WfEU0fQM3_3l1W0laAGS8G_dAhWI-oAk4JFogmMuYTi9n_Vwyq-HiQfip9iKxlEY7j2Bmh8uDXL-h9h1T-kdCmGDpDCdS2kJPar5jXbdmctrjE6IzsZR-GvK5ty8DHLNHZPAQayS0z3X9LEjyzpugNURAMYMis3_l9dfq6Et1yH09dPeGWUbMVkrBVV1RpFX8GBPCXNmHrptBHjtW7lGNXkkFRxhjwtVCPmu8M3R8BKOp6ivrnYGBXdvyJYlh6ilVrK_Wm8enuHX3GMGtOzmYZxsqz3VH_Jvgq5i-he23WvFMSj6GjK1jrRAnNCiPrkjv48oPUVV-3hUhAify3GYAhe4V2elKeX7Zr1J1rF-VMdujRtMcH-6bH-FsAFX7XbNCHhIFEhWCCIju2o28QvKyjYinNnQ4j-1y8biIBfzkH0_mHHBgPoiAudP_BcmGQVubmI1AIPgpqXOTIhsur6f__kI5IfQamJWBdwKw3o7sFu1iGjAnIqYN-YMzt4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اسپانیا:  وقتی اتفاقاتی که در اسپانیا افتاد را دیدم، گفتم: «پسرجون، این موضوعی برای بحث در انتخابات میانی خواهد بود.» اسپانیا نمی‌داند چه کاری انجام دهد و این اتفاق امروز دوباره در حال رخ دادن است. آن‌ها در حال حمله به کشور هستند. این قانون ضعیف، مدیریت بد و قانون بسیار لیبرال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138927" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43705abef4.mp4?token=jUjyqHJWYrU6nG6pHXI4czFKlGEgrj0vkBAP_zO6hIY05nDyTBCv7oqjU6FJOKXYlc5ri9xnozTA_0qRbZRzK2Hwa79A8LXUchrsSegfapsbx619jFmytylzgvub4QGW5zLrD9BEYum40GthgXgrouv9nyeSZYMgfLHaVPolnbbbbTwY6Y5qoBkXELSpwTShtrSZCMG7DbyCMmLSBjvGYeAJBUtoA5239PETceEhLuJWNJIU7JYBN6JW4W3UZQZFYC5LujTmDDmX5wKyhoQ3F46nvBoizMv-arM3ysATXQU24DBG02XWvIGvx8C6Rls-arCrEg7z0hHGwDqUHccLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43705abef4.mp4?token=jUjyqHJWYrU6nG6pHXI4czFKlGEgrj0vkBAP_zO6hIY05nDyTBCv7oqjU6FJOKXYlc5ri9xnozTA_0qRbZRzK2Hwa79A8LXUchrsSegfapsbx619jFmytylzgvub4QGW5zLrD9BEYum40GthgXgrouv9nyeSZYMgfLHaVPolnbbbbTwY6Y5qoBkXELSpwTShtrSZCMG7DbyCMmLSBjvGYeAJBUtoA5239PETceEhLuJWNJIU7JYBN6JW4W3UZQZFYC5LujTmDDmX5wKyhoQ3F46nvBoizMv-arM3ysATXQU24DBG02XWvIGvx8C6Rls-arCrEg7z0hHGwDqUHccLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره اسپانیا: دیروز اسپانیا را دیدم. فاجعه‌ای که رخ داد را تماشا کردم.
🔴
به نظر می‌رسد حمله به یک کشور توسط صدها هزار نفر.
🔴
همان اتفاق برای ما هم خواهد افتاد اگر جمهوری‌خواهان انتخاب نشوند، مگر بدتر—بزرگتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138926" target="_blank">📅 19:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ : قیمت داروها ۳۰۰، ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصد پایین اومده
🔴
هیچ‌کس تا حالا همچین چیزی ندیده و نشنیده
🔴
قیمت داروهاتون اون‌قدر پایین اومده که حتی فکرش رو هم نمی‌شد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138925" target="_blank">📅 19:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ درباره کابینه‌اش : این یکی از بااستعدادترین تیم‌هاییه که تا حالا تو دولت آمریکا خدمت کرده
🔴
واقعاً یه گروه از آدم‌های بااستعدادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138924" target="_blank">📅 19:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006aea3c94.mp4?token=bD3cGzgGrhRcQhsumzwDfIeVQl9RIOKfUyUQ0bHey54BUH6xa1DqE7uPNzOs5_Ba1ScGQZcWuKRmot-mYcYFxcYgjLwaHYRLwFSyzqtJmYg6C7B8Xr3l7xtPVf1Ji4euNvLBx-Fg-rKFp9cc-Y_YytCi9Z1Tg5Znbc-hn921ux7iKKqq-vz2vyASS1XRKNBDkPgY-hSVF0GZ4bhpX5nGzH6BSPRtUsqXNUe9zFHzt4ZQ1WHS6swVw33zu3Cjc1jQXQ2UfGobp4UR2J2Wn9dP-uucAfn8qY1aUeN7m2UUM-aGmZu150puzsnIs5moKbKCF-XZyL0kG4N9yS_hmn3pZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006aea3c94.mp4?token=bD3cGzgGrhRcQhsumzwDfIeVQl9RIOKfUyUQ0bHey54BUH6xa1DqE7uPNzOs5_Ba1ScGQZcWuKRmot-mYcYFxcYgjLwaHYRLwFSyzqtJmYg6C7B8Xr3l7xtPVf1Ji4euNvLBx-Fg-rKFp9cc-Y_YytCi9Z1Tg5Znbc-hn921ux7iKKqq-vz2vyASS1XRKNBDkPgY-hSVF0GZ4bhpX5nGzH6BSPRtUsqXNUe9zFHzt4ZQ1WHS6swVw33zu3Cjc1jQXQ2UfGobp4UR2J2Wn9dP-uucAfn8qY1aUeN7m2UUM-aGmZu150puzsnIs5moKbKCF-XZyL0kG4N9yS_hmn3pZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آن‌ها دوست دارند بگویند: «اوه، کارِ ایران است؛ ایران باید خیلی خوش‌شانس باشد.»ایران مشکلات بسیار بزرگ‌تری از آن دارد که بخواهد نگران مینه‌سوتا باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138923" target="_blank">📅 19:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc10781ead.mp4?token=XWbQhun6VSjSJJaUwwA7SORVSx8rg6W3-WtsPfvlFqS5pQCp0QKbVaptIAmT5h4q_mUTEIvnkQ0pVN3TkE9Kq_bSzEiAUDOkEdhWzPQvwaQcuhf9c8oeGjVO5ttCNNQjFDrfRo34woYrGGq_0FxIAkmhTWavuKy_zpZQdeHiVi1ywzSNUh9oSslwB_f16CB60KmmWUEgL_bMKRTtTxAOH5U5NNGgzpw1gJUbbpWFf6PBxUaI_lY4Z-p8EBmGKZnhsEJFZKQSQZMtF1JLKyKsJTaO1i12rkQQlpLXvkGY8Ky1ZQ7_ZDWrFtKpzArNk1MdbxIK_H24NwQX-a2d-sapKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc10781ead.mp4?token=XWbQhun6VSjSJJaUwwA7SORVSx8rg6W3-WtsPfvlFqS5pQCp0QKbVaptIAmT5h4q_mUTEIvnkQ0pVN3TkE9Kq_bSzEiAUDOkEdhWzPQvwaQcuhf9c8oeGjVO5ttCNNQjFDrfRo34woYrGGq_0FxIAkmhTWavuKy_zpZQdeHiVi1ywzSNUh9oSslwB_f16CB60KmmWUEgL_bMKRTtTxAOH5U5NNGgzpw1gJUbbpWFf6PBxUaI_lY4Z-p8EBmGKZnhsEJFZKQSQZMtF1JLKyKsJTaO1i12rkQQlpLXvkGY8Ky1ZQ7_ZDWrFtKpzArNk1MdbxIK_H24NwQX-a2d-sapKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آنها ایران را مقصر دانستند. من اینطور فکر نمی‌کنم.
🔴
من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138922" target="_blank">📅 19:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk_oYzHDH9ws5ZupwZ3Ar5SMQ0lt6wGYrzDZiCH1LOHT4rrEUTigJSryAmDaFjcnSVsV0o1nKLmw2FZTlDOGp3ZJQdTgb7Tk1Otqg5surucLW6E9MPwASLGJ9eEG0wRYEwDdNyGPtzVAPYGkdYTu2Z9rz1yEv-NWehSe8MxkBsSIEhMDDrOqaxGd20E7d7F2-gtQRF8V_pI5GelzgB3gvXTyaJr9BgQluVJkCRfXx3nwsQbnF1T_Wb5AzTbX_CBRrLZQ97Fb9paK2Bwh8pjE0t42WPexYEOyd_uyKZ90_rLLLVT5vCbUZ_pvO2AEmEDNd98QBoYKlsBjPW_zAnSdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در غنا: ما به یک کشتی قطری اجازه عبور دادیم، آمریکا آن را برگرداند چون از مسیر ایرانی استفاده کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138921" target="_blank">📅 19:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGC1d4qEd2q9UEtR_qxuoLPjGNGugEqvL8_qviU26UMyFjAp3B62Nplet9Uig7LTnkAB_g0whR7OkKlRPhLYMMuJV8rEwYYn_db1Rzr4NFxZMKgZCsAOsV4a2NXvv2rQYpqvWRoIsXH_oJWxStmCi4mURAWCQgRvgS1rx0GDUKkUHDPwX_BIvXQxPhH3epVXVOQ9iU_VfSbxVvWGFxOlyeUIGrsqYodFFpRGsRcNWYzKIjYphvUxwAP9_joajqtMkAvxdJztoYvTiZC20d4lkFwXSLRl9y4_NSds2_Ai6aZYOZqlGuvdoJzTupn0077jD6u7Hyj3yX9FwXzZDBkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنت‌کام: چتربازان ارتش ایالات متحده در حال شلیک گلوله ۱۵۵ میلی‌متری از هویتزر M777 در جریان یک رزمایش توپخانه صحرایی در خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138920" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام پهپاد انتحاری روسی توسط موشک پدافند اهدایی سوئد به اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138919" target="_blank">📅 18:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVtuodePqyzmPuebm4OaEy2CVTcHdM9sV-xTTSYvvp5wCJlve4WNisuAZsubsqbktOnlStvfjLA4WKCfQJ3FHThvTyettThicW3s9eT_0w_1XetWcon5RcP4ZYGMTSgRtB8YsBeEtygW9lhKJtm_qC5ASY-sAlj78crRsqlv19J-uO9bhEfxFPcHRZXN4zscHOQ-hOzRDAKBTPEr9W2jyAVEgzK0O8QI1v3Hi3-_2nWvwgXiKFrpHIWCYhknrT87IitkSZMGEym4EXoENrvxr13wn-RG0LaUAGFPYCtBsJTy3JX6uVcUzORfM0SmMtn-T2zxOWnfs_53y6uGeTo6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقامت شبانه مردم کیف پایتخت اوکراین در ایستگاه های مترو، به دنبال حملات سنگین روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138918" target="_blank">📅 18:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلاش دارد پیش از انتخابات پارلمانی اسرائیل در اکتبر، به توافق عادی‌سازی روابط با عربستان سعودی دست یابد.
🔴
روزنامه هاآرتص به نقل از منابع آگاه گزارش داد نتانیاهو به چند تن از دستیارانش گفته است که پیش از انتخابات به «یک دستاورد بزرگ دیگر» نیاز دارد و منظور او توافق با ریاض است. نتانیاهو امیدوار است موفقیت حزب لیکود در انتخابات، زمینه‌ساز ادامه نخست‌وزیری او شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138917" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138916" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138915" target="_blank">📅 18:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه: واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138914" target="_blank">📅 18:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138913" target="_blank">📅 18:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138912" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : ما رابطه‌ای قوی‌ای با ژاپن داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138911" target="_blank">📅 18:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در راه کمپ دیوید است تا با وزرای خود در مورد ایران دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138910" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت دفاع روسیه امروز جمعه از تصرف دو روستای دیگر در خاک اوکراین خبر داد و اعلام کرد که نیروهای مسکو به پیشروی‌های خود در شرق و شمال شرق این کشور ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138909" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه:
واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138908" target="_blank">📅 18:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سامانه کشتیرانی مارین ترافیک: در ۲۴ ساعت گذشته همه ۵ تردد  ثبت‌شده از تنگه هرمز از مسیر ایرانی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138907" target="_blank">📅 18:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر خزانه آمریکا: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138906" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک مقام آمریکایی: ترامپ حاضر است به مذاکرات فرصتی بدهد
‏
🔴
نیویورک پست (از رسانه های حامی ترامپ) به نقل از یک مقام آمریکایی نوشت: ترامپ حاضر است به مذاکرات فرصتی بدهد اما خواستار موافقت ایران با آتش بس است.
‏
🔴
ترامپ خواهان توافق است، اما اگر حملات ایران ادامه یابد، بهایی برای پرداخت وجود خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138905" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlHY_MIqa_q4m1LvxBM84_6O4T51lvrH0T7fJalNJ7cdDi99M9RjIxWzuQoLjy3vjUHbreNaPIb6EnWQ45YceXS14VLaMkugogwEb9vpwWK41uDZr-bcvP0ktAUQrlhQ7r-AauwxP9K3CmFqMqSOQhnikR58SgvMKShVHspDWkzochYG5SRdA2e9td57tBBd9bcoG2SiJxLa7EjCEd3q6UL3pGnoUHv91K2Dr_QzVi0ywy0KVChCOkVuDzmlIcQl3ZxpPp8WIqC-erLpTdwdXIrRwL7E8RdtG5tp8hbaFF-PS4IQpQGhy7m64UVUYh58OJ1ZX4F3QKZeZy9gBq5BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کاخ سفید: جلسه امروز کابینه دولت ترامپ به صورت زنده پخش خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138904" target="_blank">📅 17:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تماس تلفنی وزرای خارجه ایران و انگلیس
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138903" target="_blank">📅 17:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgPu2Z25DsAPqWBROG-x8BxUI-Btcy-zom6GfWtXcgMb0OX0Q8RsEXq6epoXaBLoC8HlM_GwG7Z5wxJ0IxugNwTTGfSGulzQ_oG3MO0sZWtgwQuOR8LyS3gn5j3zTFn8lmIZXsZi_R5QGv6gYQJNSsAAFaiCfHoiMoV4MTVhyuBk9AiZZDyicq4TKF8w8rPHWhPwsAXwiQfG9RdsKo0FNzWy_lIW91ZfExRa3ixnr0n05Gd6lHladLa3lKD3CbkPr1RjK08N8inFqFXCoGKNLfgT4PbST4EdtK50X2m7nhAeYhrRMJE677JLmoDVS1vuDbUZd8-_GOqScDbThw6yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر بحرین: تا قبل از ورود اسلام، ایرانی‌ها در تاریکی به سر میبردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138902" target="_blank">📅 17:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل:
پیش‌نویس توافقی که توسط شورای صلح منتشر شده، برای اسرائیل غیرقابل قبول است.
🔴
عملیات‌های ترور در غزه باید ادامه یابند، همچنین تشویق به مهاجرت ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138901" target="_blank">📅 17:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دلیگانی، نماینده مجلس: به‌راحتی می‌توانیم شبکه برق آمریکا را از کار بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/138900" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال 12 اسرائیل: تا زمانی که حماس خلع سلاح نشود، هیچگونه عقب‌ نشینی نیروهای ارتش از خط زرد انجام نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138899" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138898" target="_blank">📅 17:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: اتفاقی راجع به ایران قرار است بیوفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138897" target="_blank">📅 16:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5lHI1d4DEP0SuBDWMcHWtQ930oU67IvkoZ5nz58ukRNafsmCbyBbRMEJyM0Cm0IMAYpnr7_KYDU9E_y3WCaksEhPMPNbtXP_tw1f7PdcrJV0QpAnd8OftXEsLwtIIrQ_AExefRELItJvlj7u7T5PaorGoil1dmasYVzUshXj6bnpCnXfZlP0cVwQGS1IywlDMVeIFvBL2qlDi8Fs9BMl6Wtxg1-lMPohTrymU_F_AiI4iaQxK7F7j4rk7kdhSWPeBBFhS-wmmrRLSPh-z33EjdwoETyusB7-n8MCk4N2BP4YzYgpbQB_eb7R8orHZwjs7_64ilk31hmv1QL6aLXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8bD7v3aDIO2nLDFddYsF17niTDUDn6WCr5RYDV3ps_PFJtMhtlv-DSUJgr83M-FnX_Tddw2jRCH4YVVa_hvOzXbjS6s_Im8Fqy7SPkjuW41-dIzGeW1fhdrZDQjHyMw3KmXSGGXyiA3TQ8IolSCvQQRy1YeaH1MuX618ri1AY3XBoVGKKs0lddCij0Iy8er0CC_HuOZQoEW66g7-uRyJmVTEo36Dwb17wB6-3uNVY2cQCUF-L2-BynwZyJ8LLbE-tSk9mZNw-I2ZcQV_YyCR-zV0gllTkCGGEA8dIitO0PxR_kLubgPE7Sv9mLxgcUV8SSvyHJWE4GDDcrwjyKbBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مقایسه جیره غذایی ارتش سوریه در دوران اسد و امروز
🔴
سمت راست جیره فعلی، سمت چپ جیره قبلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138895" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138894">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: جنگ با ایران داره خوب پیش می‌ره
🔴
آمریکا داره حسابی به ایران ضربه می‌زنه و ما فقط داریم پشت سر هم پیروز می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138894" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجران مراکشی که از طریق دریا وارد منطقه سوتای اسپانیا میشن :
🔴
یه نفر دوچرخشم آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138893" target="_blank">📅 16:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOm_rb24WpauS_QcwUxtUuXPGsMalwL2Pb_UYlVltvmiiABwvH8TyEvgeVA-hp56yYhQYY4mQzqPGoOuXWmIX99QwxjTtNqM1TzAed5VCwgtIx_cjV2ABBfZ41h6J2dB3Tkv6iJ_4WhaYUyZYehRRps34AneGJR9zfJUmts79LBBGnsivOMMFVihU89h04ZEzVhVTqp3D3wnbUJsjZCMhjauQBdW6iQ_C3P2hVygCqsuqvkEny4R1cYemFIN-XpJQds_B0_mUQQR6I76NP4Qe5dkWslFCsC3g0W70EcDckjx8WM0POplc8JwJW68HmpbwGz_OX6QbERP2qnuZ2TKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لوومر، فعال سیاسی و مشاور نزدیک جریان محافظه‌کار آمریکا
از کارخونه تولید پهپادهای
SkyFall
تو اوکراین بازدید کرد
و روی دو پهپاد رهگیر
P1-SUN
امضا زد؛ و یکی از اونا‌ها به عنوان «
تقدیم به ایران»
علامت‌گذاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138892" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
ترامپ در مورد اتفاقی که در اسپانیا افتاده:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138891" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5CF8DIHUJnVU622eHRzp-ujIUtgE_LU1KQYLSmlU6BDb42b4X9WhMeAHHoL56WaWEApKPAjb0inpUEoY3Qh0VJ1xkXRK-FULYmHCxqew9NwhjOFiAQJc6WVcOrg6Qkk6FnbUYP4G-P9n91_LcsnvXyPkITSJoVdiC87yocTAGaNBZO-b7_Ob7MNV-_LMq0CfydLU0DehIaxyhbQgiIRviL0Abm0iL3uq8slegGgF1N1D_Gt35vMV0YODEoW9yGEQ1RLz1kVVJGVElJHzHzpGulUjMHSjr97wOF6e-3gwrRg5W6FwcXUumOyFfII--S7yN7lzoRg6UdCHj4hdz-FXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال و پاسخ هوش مصنوعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138890" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/re6I59c_C0eBZRqAWXdyfY3NAvm_T8gLO-f8A4QT5t5ptjczvkNdJUQLWmD80cn_NAQH86zyqjjrSiQxA7Mf5bQymGvRoNo0nUK0CCePjv5kamBsCUt25N55PnBFxLBotOMhNx9ql4nWMHF6R6UHOSNXQ4r1KJAdOiUsKy5ri-I1nQYwLPAiUNHBwAdYLRfs-FsWg50KNOdq2pHQWiy5ke2V2vc8uvwRivf4t3PZKUSdcKOXwy_comizTxzYK8ml4jxvfxb8K1jkZZwvJtjyorn_FjQRry0uY7xFMuC45PyNIhomnSqO2V1hXugT8pgyXaeeuHzq3rzf0uOYK-953g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی از ترامپ خواست تا از ایلان ماسک بخواهد که اجازه دهد از سیستم استارلینک برای هدایت حملات پهپادهای اوکراینی به پایگاه‌های پرتاب موشک‌های بالیستیک در داخل روسیه استفاده شود.
🔴
ترامپ به این درخواست پاسخ قطعی نداد و سرنوشت این پیشنهاد نامشخص باقی ماند.
🔴
اوکراین استدلال می‌کند که این اقدام به جبران کمبود سیستم‌های دفاع هوایی پاتریوت کمک خواهد کرد.
🔴
در حال حاضر، شرکت SpaceX استفاده از استارلینک را در داخل روسیه محدود کرده است و فقط اجازه می‌دهد اوکراین از آن در خاک خود، از جمله مناطق اشغالی مانند کریمه، استفاده کند.
روسیه پیشتر ایلان ماسک را تهدید کرده بود اگر بیش از حد به اقدامات خصمانه خود ادامه دهد، ماهواره های شرکتش را در فضا هدف قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138889" target="_blank">📅 16:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJ5AODmCKeBb6-2EWRLMXTKVXpOyXC1Cf-yhmjXXXhUkS7V9xtWvo4OBNSVuSjp5z79KYiVPfRVyqpnCvVBsoxR7IDSe48VmJYw3tlwhAXxV1P5wglmGS-C2cgD72e1wyZl6uozkvRAyRcs25TH9IRmbMrT6l6hHCvWe1uy_MfVOki0Hk9FfmCMecvIelkvmyp6tXRgubTytPhymxmAQDQgLyFbAAH2OayGxNV_GRFMlfbMPumoyBzn5AESIOMFF4Ct_d0VFOQhbsWgKUSEwZUDsuT9X5Y7JF7OVHS5_I5Db6wDc9xFAuMMzsR46uBY2Pg-EmrjvvaU_tfQTs3kBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدل علی خامنه‌ای در عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138887" target="_blank">📅 16:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138886">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما نوادگان یهودیان اصیل سرزمین مقدس هستیم، و ما بخش اولی از میراث یهودیت و مسیحیت هستیم که آن را گرامی می‌داریم و که به جهان تمدنی مبتنی بر آزادی و ایمان بخشیده است.
🔴
بار دیگر، ما باید ایستاده و از آن دفاع کنیم. این میراث در معرض حملات ناشی از افزایش موج‌های یهودستیزی و مخالفت با مسیحیت انجیلی قرار دارد.
🔴
این اتفاق تصادفی نیست که این دو [یهودیت و مسیحیت] به طور همزمان مورد حمله قرار می‌گیرند، زیرا ما یکی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138886" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138885">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراقب باشید در این روزهای حساس گول پروژه های رژیم رو نخورید.
🔴
از سرتنگ راستی بگیر تا رپرهایی که الان شروع کردن به دعواهای مختلف و اختلاف های قومیتی.
🔴
با آنفالوکردن مهره های رژیم بزرگترین خدمت رو کردین.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138885" target="_blank">📅 16:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:
اگر ترامپ از ما بخواهد، به حمله علیه ایران خواهیم پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138884" target="_blank">📅 16:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138883">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euSQ5wo6nj4hRrWH_doaY9q6AbHPdG-o8B8RmW79EWRGT5eluyQxn44NzGdpDM_go8BoBnxiAohVVwF7xZEXXGOuenv4GbAPEvm7tZPoIaTecVu5y5isCKzI8CA46osj9rNr90GQLZwrJL_UyAw4NX8ddgpZ5LjtoQNJ5tUR10wIiAPf2ZpZA7Hs88o2EOS_y4Cf0S0wnrPDim7FRYwV921SYn9CcQ696YGMHsJalxPjnIpfPezxVgm57CZmwx8PSOZjWRTLkRI-encX-TtdcIrPTizrmJRKe3L45KzO4Qpn3-mtril__FPC-8uy6QqwS-4r-TotFJbRPFAXaUxVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: عربستان قصد داره یه عملیات بزرگ دریایی یا زمینی علیه حوثی‌ها انجام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138883" target="_blank">📅 16:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138882">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغی جالب در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138882" target="_blank">📅 15:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138881">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byXuivMr0W76Fdecra-oJb_giUipgUf2wqn3BgTkGaeSSk7KFalYX54zS1Ma4o9WnbiK3d8JMr24rkRgdmXAUvt4XTpyZanLyER3RVQ9IUEOSYHT_9cnsO9H9BaQWH6K4GJ69VmXEmuq3edbnOLd-PKohE26xtX05wXeL21a5wbYfjWBbfQ1ctICR94jj9vXQhY2xZdOlnhuNrIFKvyVvC6DicdTV1UPowxiXUNszu3AKfHBPxLWp_lBsGZ8L2MVKmbZNkP3P5N9WnxdNi-M7sstadRHQ77AhNwtBx7YYHLXBzx5qXkiLR3ndGyOMOuBXT6sUOvUeYDo9W5wPq7wtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر آمریکایی، از مسیر ایران استفاده کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138881" target="_blank">📅 15:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138880">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138880" target="_blank">📅 15:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh26dInvcZlDJQfsdwakMLNxPXRxqyp4ZpWlxvNSiiWShI6iOE7S98FfiLyvf-bQKUp79jEfRrXVmrDnRkI70JopAoR0liI6vkA9Gu6Xn3tXvXanSTunNCo20y024BXdPYxGReW-dZunppuj6MfvYUP679LHuOQoqhck0Q2K9lDl3MrAmWWcEcdyqD3WOJTVkTAx7_dGuG8zThkA9rWOsBVWauCMQGHvtduylWCPkntuTpKgrbOht5Crk8fYn-596w9YZKe1NhuppdtP6bopI0DV9HlnZQpDk_cyC5d_UKKKzJzPzhD7jY7-g0o9DYKsInPfCjZKgynOWsVpFzh8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش باراک راوید به خبر طرح آمریکا برای اعمال محاصره زمینی ایران
🔴
آیا اصلاً کسی زحمت کشید قبل از اینکه همه سایت‌های خبری اسرائیل این خبر را بزنند که اسرائیل و آمریکا "در حال بررسی" اعمال محاصره زمینی علیه ایران هستند، یک نگاهی به نقشه بیندازد یا فقط یک لحظه از مغزش استفاده کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138879" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRbLCZhMmFVjFGI0-FDmag9p8KRop4yHkO_hHlZsW49vjAtfnHR6jRyPkVLdamjIpNew8srVH7_iG0cT_IBCPDYcF32zx4G3xPdyexBJYYG_AAOkzAnXOdpgDRVNhAX_K9S-ZxaIEhyqwfhktdWFJ-SHFMur8ESjWHEb8OTaua-dP5w1Wmrrf3ldTGHc5pLLeMSDFRpWM2PqxHKzhYix1g4ED6uXSKDS51acxflrZcyjijvayG3nijNNaSbfjt4oB-PU1n9VAmAWP-T9xJorAdlhEXo3fjKjYelAXb8_4sF1Cr0_6Q5b8VaY2nywARVS0L7GzLvvbDFQXEDEFmF_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با یه
مهاجم مراکشی
که اومده اسپانیا مصاحبه کردن؛ میگه تو مراکش منو اذیت میکردن فرار کردم اومدم اسپانیا
خبرنگار :
چجوری؟
مهاجم :
من تو مراکش با یه نقشه همکارم رو کشتم اما بعدش پلیس و مردم اذیتم کردن و میخواستن من رو بگیرن برای همین اومدم اسپانیا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138878" target="_blank">📅 15:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان:
نیاز داریم مدیران و مسئولان کشور را در
زیر زمین و در دل کوه
از ترور ایمن نگه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138877" target="_blank">📅 15:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی وایرال شده از دو پرچمی:
هشتگ نه به اعدام میزنین؟ خودتون و خاندانتون و سس خرسی رو باهم اعدام میکنیم!
هر ۴۰ هزار نفرتون فدای یه تار موی تازه عروسِ شهید علیخانی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138876" target="_blank">📅 15:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVJzQgdZjcVRghj8qMo5CNehDPwYGbTJx5LxXwgrNZDqxVI8q_jYlrrZVgry5zSjQvD5eNAQ0hB5mZJ8P7g93ebjDFK8V9ZO1pPHCfEaJh-zQ_5yqXyB2u2GCCQ6xDgI_weqLQPkC83kDjfZGoVkWLZDAb6oUmDPz5srhfGk4SYSPSBm1p3R_le7gakuY3eMMSeR9adeINfKsp10ppN62ay-QW6W7VVCSV-x2z9vg1meUv-Ge4YjgLhAbx5hxoqctTDOiTxGASH1zbKjA04rfzjIIp1TS0X7J-AYDhISXI85J-7u55OeMZU95PkyCC2vcGUC8ZdjPr-jxlJVs8wIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: اکثرا خانواده هایی که بی حجاب هستن با مشکلات اقتصادی و خانوادگی رو به رو میشن ، خانواده های مومن و با حجاب مشکلات خانوادگی ندارن و فقیر نمیشن و اکثرا ثروتمند هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138875" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB69L55I71kRngaja4RrgMqwcWIdjG96jhMNjWy05IWCB4WZFPD9GFB-80MKinJekHEvea85fqOItmxTLZ_E6XG8CLn8gVP2bX91G73mz1Oz0-6MQnKsfAG4SO0gZzOhNEhqiLoZerG--Rv1H33WX26_Rqu4IK28stbXPNPr0fiVcj2kkWylmxN-sypUaibiU1foD9eRTfW2x7z2SYCpsOk4QzdcXRUMxEYoOTGe1V6LOZv-omtxwXlAJr5hJVh53YhN5ikXx4s2TN618QWFNa-L-3vqjD5NVT7EHEeLVfc4KrOy-xTlp4gMbtCbN2BxvBDIKfuMCEoilgv3NY0ikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوید کلهرودی، نخبه علوم سیاسی دانشگاه تهران: با جمهوری اسلامی هیچ چشم انداز مثبتی برای ایران‌ نمیبینم و این نظام روز به روز ایران رو بدبخت‌تر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138874" target="_blank">📅 15:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
استانداری هرمزگان: دود در شرق بندرعباس ناشی از آتش‌سوزی انبار ضایعات و درختان نخل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138873" target="_blank">📅 14:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تا الان در پی هجوم مهاجمان مراکشی به اسپانیا، ۱۸ نفر از مردم این کشور کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138872" target="_blank">📅 14:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDNeaepKZs7gn71rrYjkAwOnnm9tDeqgWLPqshN3DvhfHN87-iAuEe8KYINbKe4roKXl4oNW1gy0CP-kFgWH3j2qJCiJVpO6vpN6fBo9EGScL9grmLdEIHx0x5y-3pTOHpAh9TAepL9Je_9bgsjsFCXBedb2rmkJTPImNfxe0-tRdgAk20d1sPpdpa3X9P1zg34CpUU0GHhWTAb5pObPYj-WOqISMLAHkRL1eb6hKW0HzM7e3dWTVYOv_Yj4_1VDntd71D568A9jbTu1QKpo_3-TO40qaFHI1GCwJvMV1HWhGg5fEfPGqycjDfVVHSCLkD2prgHwoXCGdUo7SqMO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترکیه احتمال داد کودتای صهیونی آمریکایی(اعتراض مردمی) شکل بگیره و اینترنت مردمشو قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138871" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ قرار است امروز در میان تشدید تنش‌ها، جلسه‌ای با کابینه خود در کمپ دیوید برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138870" target="_blank">📅 14:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-Bqra_3zhlmibnQk5CK70mxvIMqciA_NPFhom8z2bfth404l7dr_00XcJkr42ixRaPBPUghFdkU9IGHziC0x1WvzohC6kx6PI5lES8MotoWaUdmhaBsIEHM3mKTAfeJ46y5ll-MumZ6ofQPDl5K8EWKnqgQLW9w7-Ga-xjMJKQ4bUz2EYtzKRqMX_w3R3_JOmAsrIJ874bnpHOubZV8oHmsyxeuMdIwh_RDbBqonhFiJUS40krAlN9ry3o3P7cuS8BR8EO2qreG-fgZeqhk63z2FbpIPf_eCcdxfhU4aRlq6Fsw3eRRgxMq44o-nhTRTofVMEqeFEdH53EBKmFWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نیروی هوایی اسرائیل به غرب شهر غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138869" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138868">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کویت : از صبح امروز چند پهپاد
وارد حریم هوایی کویت شدن که نیروهای مسلح اون‌ها رو شناسایی و منهدم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138868" target="_blank">📅 14:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138867">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFciBaetyG2RWwknIHMdu8JmO85BV3qtnDI2AmgsHZpTsKiu0Wg2KsBQEe8FZY6DGk15B6FrHmKyn-ipjiOzlcQ7PnvV_PPrxlVPJQOO_KwhOg1GMxtmu9aqlINI_PqW-WDNFOWd8J2ee5QP_zwQf2F4V2iIr198SiSq0RggLqroxvUKh1y4uHiOjU9811TYNK7Af7-q11chE2UlQ6JJJdBA33PnuNIyVO8PPwRNuKRC3YxLLipFlfk9jF4g5Yt7Sf852IY0yZoDJZexzRffQ53pUVlqXmTD_6_ghYvv3CRTP3QyiYWeuefQJcw2g-lj2uox0I18_Mdtfhlr1f5crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در یک مصاحبه، از یک مهاجم مراکشی می پرسند که در کشور شما جنگ نیست، پس چرا دارید به اسپانیا فرار می کنید؟
🔴
‏او می گوید چون در مراکش مردم مرا اذیت می کنند. من همکارمو کشتم و پلیس و مردم دنبال من هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138867" target="_blank">📅 14:04 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
