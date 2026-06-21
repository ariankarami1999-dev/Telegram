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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-661670">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3481e208e1.mp4?token=bCgFYUCdfz13Lvqu0aRNoGAedg0RZ5XyUmw8SabLJzBz18KH5oeAoVABH2FnTf9Ze1XgIGBjiGmXGBK61J1NVNdtFoEDEgakzSJF9I3_fgllBPwavQ6ejJWGfM_Hr6b7HPJYT9pzcBkCmAZ94JCssjurGu6Tuz1MYj0sn_3P4LIWdlXQPVZHeQq6sLQDMRp_qE8v5HsonJBrsZNz4p52e-kZLVoRVOQK7lOMjghUwGNuoeqUkEkJ7f5Cygk0446KI_JugygnuKXHYPHM5HE3Gd2TVyB4IGcrrKFrDH4tcaK3LHvvG0dxbv4gLQciRg--Ysz3Wuzm-qYacsSFNZBoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3481e208e1.mp4?token=bCgFYUCdfz13Lvqu0aRNoGAedg0RZ5XyUmw8SabLJzBz18KH5oeAoVABH2FnTf9Ze1XgIGBjiGmXGBK61J1NVNdtFoEDEgakzSJF9I3_fgllBPwavQ6ejJWGfM_Hr6b7HPJYT9pzcBkCmAZ94JCssjurGu6Tuz1MYj0sn_3P4LIWdlXQPVZHeQq6sLQDMRp_qE8v5HsonJBrsZNz4p52e-kZLVoRVOQK7lOMjghUwGNuoeqUkEkJ7f5Cygk0446KI_JugygnuKXHYPHM5HE3Gd2TVyB4IGcrrKFrDH4tcaK3LHvvG0dxbv4gLQciRg--Ysz3Wuzm-qYacsSFNZBoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اعلام نام کامادا به عنوان زننده گل اول هزارمین بازی تاریخ جام جهانی توسط گوینده استادیوم مونتری مکزیک
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/661670" target="_blank">📅 10:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661669">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccapNgsXsaDdwkShJa3U1gmpQPq08fr-D9iUgmkjtjuO35vuPOo92S215gOiisc8BrCtutQH0Jb96d2i3ahRbKlwxsfaf2R5bfduV3zyvFDC4HBWy3GqnJFzxFdHNcb0AyPYpeZxGrMNSnylZ3JAj-_ED2kVA3oEr9rD5YWiSD3s1CjfPAyTNHQUM3lCz-98C-uXBTrz2__CyqlKE90Lf71kPZI3tF9SXeeceQe75iW6ACFcEV5IYIGeILYnsTqco78f8WvJvUosgOV6kFN1RRaUbcXrDV9ymhdpZ95a0abN_40X9Vkq_W5Xpy6p034lC-WBjHbwbpO4a1Id665A0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پشت صحنه خونه مادربزرگه، سال ۶۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/661669" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661668">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23064b2d30.mp4?token=YDhMfYLokCatlbeFharwlNnhD7ttp9SCs57lof83eM0PVD32ALkjNQl9vdmL4sovc5gTr3cBFlbs4_Cfh-uFwKNxZiWkbh1EB8pxTwCKvFW3zgvoVn-VHE1eyBJrxahdzi1PgcuWGaiWo6HYZfeU0rozToKgY7MujvoiQuFJp_A6CT7GG3lA23_6rbd3FyPkFA2kICVwDnwj5CuR4kn9qLy9zbDHW2ba3hRA_bePP1QJ_z-HVPYhOsz1zn6zuxjuVu1plFmdpY4Z1Qz8txe8l0xH3omQuCHu0zd8KZCcW70AHMECFmAqAOPnB_xyCwcVcgjZA_w7NHK6JkD8hFI7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23064b2d30.mp4?token=YDhMfYLokCatlbeFharwlNnhD7ttp9SCs57lof83eM0PVD32ALkjNQl9vdmL4sovc5gTr3cBFlbs4_Cfh-uFwKNxZiWkbh1EB8pxTwCKvFW3zgvoVn-VHE1eyBJrxahdzi1PgcuWGaiWo6HYZfeU0rozToKgY7MujvoiQuFJp_A6CT7GG3lA23_6rbd3FyPkFA2kICVwDnwj5CuR4kn9qLy9zbDHW2ba3hRA_bePP1QJ_z-HVPYhOsz1zn6zuxjuVu1plFmdpY4Z1Qz8txe8l0xH3omQuCHu0zd8KZCcW70AHMECFmAqAOPnB_xyCwcVcgjZA_w7NHK6JkD8hFI7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار کامیون حامل سوخت در شرق مکزیک
🔹
انفجار و آتش‌سوزی یک کامیون حامل سوخت در شرق مکزیک پس از نقص فنی در سیستم ترمز، موجب ایجاد هرج‌ومرج در منطقه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/661668" target="_blank">📅 10:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661667">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پزشکیان: عدم تناسب میان منابع و مصارف اصلی‌ترین مشکل امروز کشور است
رئیس‌جمهور:
🔹
ناترازی منابع و مصارف، عامل اصلی نارضایتی و بی‌اعتمادی اقتصادی است.
🔹
تداوم تورم ۵۰ تا ۶۰ درصدی در سال‌های آینده غیرقابل قبول است و از مدیران پولی و بانکی می‌خواهم برای مهار تورم و خروج از این بن‌بست راهکارهای عملی ارائه کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/661667" target="_blank">📅 10:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661666">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c780d691.mp4?token=SDywpAJtHP2PJrBTc6J0d32DPRwcze7XSZ5SW7dDWbmLninRTo7AQUGFj5YoyKzXJHYxOG8AEt0InQiA-xlusEM0iG6UFl1sk_7IrgvMkoSvHIaQIFzyPGl1mLvcC5vzEfocR5ktjTy8Lzf0ti_mbZcpwSHMavDiOzulGtRZLW50w4L5rLBuimInr8wAXnjqAMOGznoMtc9wf4aGZGmvR1tVxQZxy6busvyfDvroe5d-Bop7grR18Km6Jo_prTNguxcyx4HXrg-7F6UImPqWj934oGKCxjidB1hnpvdgpcwCIhW2o-z7BtMq2sjkjnq-4oaAGlloVbxBfFqQSyZ8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c780d691.mp4?token=SDywpAJtHP2PJrBTc6J0d32DPRwcze7XSZ5SW7dDWbmLninRTo7AQUGFj5YoyKzXJHYxOG8AEt0InQiA-xlusEM0iG6UFl1sk_7IrgvMkoSvHIaQIFzyPGl1mLvcC5vzEfocR5ktjTy8Lzf0ti_mbZcpwSHMavDiOzulGtRZLW50w4L5rLBuimInr8wAXnjqAMOGznoMtc9wf4aGZGmvR1tVxQZxy6busvyfDvroe5d-Bop7grR18Km6Jo_prTNguxcyx4HXrg-7F6UImPqWj934oGKCxjidB1hnpvdgpcwCIhW2o-z7BtMq2sjkjnq-4oaAGlloVbxBfFqQSyZ8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مومنی: وزیر کشور پاکستان حامل پیام‌ بود
وزیر کشور در پایان سفر وزیر کشور پاکستان به تهران:
🔹
از روز یکشنبه، مذاکرات برای اجرایی شدن بندهای تفاهم‌نامه و تحقق شروط آن از سرگرفته خواهد شد.
وزیر کشور پاکستان:
🔹
موضوعات در مسیر خوب و درستی قرار گرفته‌اند.
🔹
ایران یک رهبر خیلی خوب و واقع‌بین دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/661666" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661665">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/661665" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661664">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0163e2ea9.mp4?token=GiKZvfESzxX6pwFmezVcJDfdUcFz12ihSQy-HOp4xbVjZivtrGvruOwzJihwEhmb1X0Ig1PcMLS-x_w483UpAmizuOcTo6sTOqgKeR9gamVjlgZYONER8x9UtOKdPM3cjr8NUfUc1XwiaKaUPOkOp4GczKPCZFI7zw5WIPX5QYUaqTAevBHgAu4Ah8slcx5Vb4ywTZBqnjULMGNwVX6n-XenuVWSRAGfEo-P86VGmsGo1DtEaZzXZkmN4vVYwrXAIQknrtr_Zh-ePTLR-py6-ZBKdaVJyqOPcUShNaNX9x96WPPdiR0lnHfo_nTg9w8usdU50rwAt-16tlykTSNUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0163e2ea9.mp4?token=GiKZvfESzxX6pwFmezVcJDfdUcFz12ihSQy-HOp4xbVjZivtrGvruOwzJihwEhmb1X0Ig1PcMLS-x_w483UpAmizuOcTo6sTOqgKeR9gamVjlgZYONER8x9UtOKdPM3cjr8NUfUc1XwiaKaUPOkOp4GczKPCZFI7zw5WIPX5QYUaqTAevBHgAu4Ah8slcx5Vb4ywTZBqnjULMGNwVX6n-XenuVWSRAGfEo-P86VGmsGo1DtEaZzXZkmN4vVYwrXAIQknrtr_Zh-ePTLR-py6-ZBKdaVJyqOPcUShNaNX9x96WPPdiR0lnHfo_nTg9w8usdU50rwAt-16tlykTSNUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نام‌ اثر: تاثیر اطرافیان بر شما #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/661664" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa_UgU4RpncSau22gdzI2UND6MSX8EMK-TUhSs9gjaJymqG0wG_9BLlc5oAsOhuziHe0naBDfyqfyD-bvRGDwhuGlBU0Q6oH-f9d2hjbkfSVuK3zNhCUxzRn4Y9L_A39NidfXATJzSD4haaW2elSilqmhEwRHw_M7E_RFXJOGtJMcRKgKY5n9La-Nz5mrYSZ4qn_sKSfJHylr4H0IsOr9m7tKbAgzhZvTR_bhc1ZPpc3Rd0n4ysP1vwbKZhIQ86oW0WX4GzEkw27KoASLZnXgtutSvoW83wWW47JdFzbusS_ToBqEihyjqiu0GEBzHntvw2_sXoP3T5lx_m-gnb7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنده بلژیکی نوبل فیزیک درگذشت
🔹
فرانسوا انگلرت، دانشمند بلژیکی و متخصص فیزیک ذرات که در سال ۲۰۱۳ به خاطر کارش بر روی بوزون هیگز برنده جایزه نوبل شد، در سن ۹۳ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/661663" target="_blank">📅 10:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae8430d65.mp4?token=cOLOzX_09bXl4ADDUmFB9V_85NDDgeLn7DrdHoLM4Yw3YuwP0jj0lZynyZuZ8hDyvZu4fKvMDUgCqxLglSsunp6j7qPVbXH50hZWBETCLf9INSr0ZNy8kFw0KolpImpAz3SisDu41q361274B7Sm8Bzr6iKfwuydo0hVhE_M-jsD4o47fOvYIqumuI7ONe55qjmp9gjIiTy51E-viBPYeJ6eme-yDRN0_gbosWHfh1Jt_Gm7xRucMbwi165OuQOw5rxjFTHQkeAULdoVILbxdbV7mAdqmYpsHydzV7lZhrPhq3HFCGJn6CJhRBmTCRIVZW_vqipT_LA8Nh1baFnabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae8430d65.mp4?token=cOLOzX_09bXl4ADDUmFB9V_85NDDgeLn7DrdHoLM4Yw3YuwP0jj0lZynyZuZ8hDyvZu4fKvMDUgCqxLglSsunp6j7qPVbXH50hZWBETCLf9INSr0ZNy8kFw0KolpImpAz3SisDu41q361274B7Sm8Bzr6iKfwuydo0hVhE_M-jsD4o47fOvYIqumuI7ONe55qjmp9gjIiTy51E-viBPYeJ6eme-yDRN0_gbosWHfh1Jt_Gm7xRucMbwi165OuQOw5rxjFTHQkeAULdoVILbxdbV7mAdqmYpsHydzV7lZhrPhq3HFCGJn6CJhRBmTCRIVZW_vqipT_LA8Nh1baFnabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدردانی لبنانی‌ها از ایران؛ از وفاداری شما متشکریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/661662" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: دلیل اصلی گرانی برنج، افزایش نرخ ارز از ۲۸ به ۱۵۰ هزار تومان است؛ بخشی با کالابرگ جبران شد و با رفع موانع ترخیص، قیمت‌ها تعدیل می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/661661" target="_blank">📅 10:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سی‌ان‌ان: اولویت هیأت ایرانی در مذاکرات امروز، پایان حملات به لبنان است.
🔹
وزیر اقتصاد: نرخ سود باید اصلاح شود.
🔹
انفجارهای کنترل‌شده در دزفول از ساعت ۱۰ الی ۱۴ امروز/ مردم نگران نباشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/akhbarefori/661660" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3625e5.mp4?token=BeFhiQaMEjp926CigvR3YcwDbBFix2Zvn9jumSo61ZXz6_Ma5K8QN0GRBpQkyvow20s9fpyNHWs0T-lHBwe50BReZzydkqS1_AJJsBEq0ARHOg4K4kRHnLbzGCIMcZRuEnWuGNi6nFwC7fqreZJWJ6nB20mwHFH_Am2Z0ActajrlCKLH0Huz6JchyYRngQCkPa-antFBLBVdKu7Q9KzVfJWM0EHG2Lbnwa7TXw5vtmqvOUjrADXaYZ8kUT6nWGA3NSFs6yllv6j7TdFtMdIKQAd3HpZaC_9dCyIJNhj9SQUfWslFICbrU2tp7Mf5Ig63wb6jt85PvGXMYlQLUEJaQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3625e5.mp4?token=BeFhiQaMEjp926CigvR3YcwDbBFix2Zvn9jumSo61ZXz6_Ma5K8QN0GRBpQkyvow20s9fpyNHWs0T-lHBwe50BReZzydkqS1_AJJsBEq0ARHOg4K4kRHnLbzGCIMcZRuEnWuGNi6nFwC7fqreZJWJ6nB20mwHFH_Am2Z0ActajrlCKLH0Huz6JchyYRngQCkPa-antFBLBVdKu7Q9KzVfJWM0EHG2Lbnwa7TXw5vtmqvOUjrADXaYZ8kUT6nWGA3NSFs6yllv6j7TdFtMdIKQAd3HpZaC_9dCyIJNhj9SQUfWslFICbrU2tp7Mf5Ig63wb6jt85PvGXMYlQLUEJaQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر اسبق رژیم‌صهیونیستی :نتانیاهو ترامپ را فریب داد تا برجام را پاره کند که بتواند آمریکا را به باتلاق جنگ بکشاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661659" target="_blank">📅 10:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqeNLVqO-OKv4BM2nDyNxIey2rxH3rTgn4B6w5VwiauS_VzD5h3zkfYlsA_kjYGPerhFJCc9mg_Fw-p7C0NcQIsOPK7Czfs4t_FUCyR_ykvZyJHkqJixffw1J_GlM6dJ8sSUpxOQUOvD2pVn4q5sImN0x1TIVs1qXTdiHZ3RVcv9Ka5s5BvDVfq7B_un2S3WiTk6XfOjd1WO_BjuNPMmzJDSnBPa0_WKUNttGIgZ_jDZFf34-qsfH55QtsdhWzUzD7GDRKRwPLIM_GcFjdPVCd_uObwvGKdHsYbn2i1dXxTS_8n3q1fA80TsJH0b5RFWLqoVaWDWLf1J7s-PZP6leA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHAQ2FSc63sURFL5a-2lbJCtXkC8JPWdCYa-F1x2n3pCHJCuZIvA0zTk9RI41wlAfvNjYLsdlvLjpjUXiNyk-DZXNCP_gym4d3ohdYgV_yuXcuYTZeHFG8qD7Z4sYwf30g_X26oYq6t_FFZO7os7pGNoZ604Dqf0M5Bj1JskdGm3yuxxKI66JylYNk-HdgZkj2i9_rDZCLNwpbHRVKn7CKb3QC8x9bHYHYHdnK1Z2g9qCZD2IFhr_eAEaRB7mFAl7YYgXH91yrHI6-bqoywrqnb4kVeEhw5m1AaNH0n86SkR84TVqdLQ04ShvNRg8q9Oh7wozA6xjnLf_nYCMOcSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661657" target="_blank">📅 10:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661656" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnXLQUIK7lC65PDeLLFAYH2_4DFXnwzLB1NojHEuH5rhtjFWpkCGj7no6pOa8xm_B9mgBVR5YrefnfDo5AGjfGsMIFEpkWO8vPR2BTuU_39Esznc8KOV2TvNZ8DKDnCerej8hN13zoHrF-QBz5-eXuU1QnuCaMz0y0udB8sxUsmc9Hu0a2S4CytkFuYX9FOfzWq-aG2VqHw37zVDk5hH3ubtpVGAR3vDmCmz7Jt0AcHnuA8rcrMgK4qlBVoVP_gwCq7syVFhnTRwN4n6VczF1C21wxh0OTut1_ZzUaqnc__4IenN5iyKhtgLf9w_HuLzemzvBzG6rA8gPXQ1rJ7CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلیس رومشکان یک دستگاه پراید را که با حرکات مخاطره‌آمیز در حال تردد بود، متوقف کرد و مشخص شد راننده آن پسربچه‌ای ۹ ساله است که بدون اطلاع خانواده خودرو را برداشته بود
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661655" target="_blank">📅 09:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ستاد اربعین: هزینۀ بیمه زائران اربعین امسال ۲۰۰ هزار تومان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/661654" target="_blank">📅 09:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مدیرکل بنادر و دریانوردی هرمزگان: نخستین شناور حامل کالای اساسی در اسکله شماره ۱۰ بندر شهید رجایی پهلو گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661653" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwtZEFUlQlWo4jP46pteDB5i27CXTsdyZVeHZikRQpcMrrD-28GesGDSh3dN5VWZlJryBR4EcELdCkMMubucKd-grBaNdNZdKacgedT5RCy9t6nj_PbGF_9nCfzV6ScG5YPgPZBejLBd6NfGAStrCLFBeapsSh5pvkh3pLLN7XOiSWIEpMNsKRu_oOhwvUJQDs9uF3lGwUhLDftBJsxL4rlLbgFOc89fkY8Uze9K1aUwBiShr3I-oG3E-l2kCL9zg-xGIcZiaSzcY4RFepqfD2HZbgDYjAB7qHS0AoGKN13LRA13NLIwXZWgZ-NXSW8LZwlhQw7iW5DIM4x3Rfv_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661652" target="_blank">📅 09:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM0tWenNebm9ejYdpPHUfARV6P5CzpVZgt_eJ5ExLPBF8Y863-VuR5qjQajfe60b2szhICD9P96ys_Fj-Knoxl9DkfT3PprgfS6_ZLGqGASUU0n_YfekP4v7wNU6i0FnebRiP-vEXZTKS6sU8HD9gVeN_kkWDpm2tPYwxeaBQoba1wGAv4xFG2jR8W6DCwM6s9qRUQQFImfkrabnvZAydE1ycUZzBCUaS57mhqAIpD9XETHK181K4Lfr3hcn77XFDfFmVm1KdUnUTpaiHGvTwxcE2whzcJA3hb9p5D_ih835wpcj_NP2Yr82jOvvL8tKiV7MisgtMxAZzF25PZEZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/661651" target="_blank">📅 09:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2c9cdf88.mp4?token=ROhlpTwHfr-RE32ONwg4Fd5ZNpAOowBFzDxLCynBN1fepmImyKFk2k7G-aua_ME3BuiAP9ceF3WLa4aym5VbAWF7V5936bVCjplJPNwo4eyDRGOGiK-X5n6dvKBqdIq2OEsSua2c4uzG3f9gxZd_39vq08PAPLoiQpDlgSeJUSOv3jmNL1Dh9Oj4pJRhHg_UhMVTuqNza5ufFTU4I82rcTwLHTxl1Gffr1x62oAwlgwAM_0ZE9ry6vx92mj6z41jX1HIRqimdTK4DzNz_XdciZkGF02dkcVCX5u01hoWl3ceoEo8dTa9E6AyJGnOQVNOKd5DUKkpCyX3uBkOS0Iyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2c9cdf88.mp4?token=ROhlpTwHfr-RE32ONwg4Fd5ZNpAOowBFzDxLCynBN1fepmImyKFk2k7G-aua_ME3BuiAP9ceF3WLa4aym5VbAWF7V5936bVCjplJPNwo4eyDRGOGiK-X5n6dvKBqdIq2OEsSua2c4uzG3f9gxZd_39vq08PAPLoiQpDlgSeJUSOv3jmNL1Dh9Oj4pJRhHg_UhMVTuqNza5ufFTU4I82rcTwLHTxl1Gffr1x62oAwlgwAM_0ZE9ry6vx92mj6z41jX1HIRqimdTK4DzNz_XdciZkGF02dkcVCX5u01hoWl3ceoEo8dTa9E6AyJGnOQVNOKd5DUKkpCyX3uBkOS0Iyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره: خب فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661650" target="_blank">📅 09:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661649">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc_nnV-mPYn4gP84iHgzGkUqf66t20Pz2hardzwOQQQPW24aPktEcYfOs3s8ivmVhx6UPA6N0KkDHMYLFfShxS0wCMMMuEN374xOqKrAM320SUbW508ENIjO7gNiTBOK5J1_yrg1kwHvsaT7CiIxIlibJ8FjMHLRNhSn6JaV17ByklIGCt52Jsd1Od7KQmqVQ7mi9Uiol0HgYre_h8KJX2UimonmQ5A6xwLXwKXKwXYAT45TKpmMRydqE2Tq4N-ZSEGocFpBPlRuHqvd8P2KEuHHCG4ev-0jcd0_HhjdsBFkcOIFeJCQShii3f1KyCqCx23hBOlWf7IT3i1yiSia-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس اطلاعات آمریکا اسناد محرمانه منشأ کرونا را منتشر کرد | چه کسی ۱۵ میلیون نفر را کُشت؟
🔹
تولسی گابارد، رئیس اطلاعات ملی آمریکا، مجموعه‌ای از اسناد محرمانه‌ درباره منشأ همه‌گیری کووید-۱۹ را منتشر کرده و مدعی شده است که این اسناد ارتباط‌هایی میان تحقیقات تأمین مالی‌شده توسط آمریکا، مؤسسه ویروس‌شناسی ووهان در چین و برخی مقام‌های بهداشتی سابق ایالات متحده را نشان می‌دهند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3224472</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661649" target="_blank">📅 09:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPwEXeRxl8s-3oFh8vNFX5onuqPh4l607x_lfPqhA37eP4Wk3jXMHw9wq0uwIDFYe9Ygtvz1pWmqL2Wg0Rx5ofj4UNNkZk3QJpFrpUgS6A3blpHkyk_aJYXAJ3YNXZFmBEsKEt57Vo_ldN3XEQHG5N8RwClA3DRGH3JXY7UeyQGvxbYZDUbOivtFh2ifkPM_nSDGQegCUHdalD8n7ph_dZKiC7EM_pxDanqg2cnRkKLlvIh3aoSS3704IMuLnbkWX7R6N3ECTqM9YAt0eg7NfyVWT5ttnsIJet8poAhLJZ_O9ipVmjN7lq_IByz_kNT4wOMhNef69lGtgYeL8aE5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slBe289NCU3HB44FqKpOH6Mhu-AmT6yVBYf4hAmTOhBfOVYsqipky8tRbCfqldBMfIaQkxB9MqrWjzXzZCMCOWAgyqNz1zNN7GbMXaLTRqmqCJGeSxSujH5dMyBGIa1IJAKV1vW9Vh5_chmsUhIYVOojqhcQIevLqoieRaLoud6UqXBQKDZ7D3WsNn9K5lESdB1TvcARqDVs9VlKLp6EVIdomVQNhXe_9PT9hbuXtvxXSlLkJ878I3IVkPxoOvtzhPCo5-UV1RIj0zZcfUArMaZSJIfcCl2LcFHQrbCDIqU4bIjAuTvahRMR0ZC4x9kkLj2GpQklffgVfPiCjj3_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRDPm1RHSKaLZcxHdQKFnHxJ_KN1Yq9-J7wWn4mf3-WDajO0eHd-hrg-XoNCkzsF_Y8MPYJSM43Hio6Utwshn67o9B3vLVnl3PlPUgZIz77zv8KGrbfYQkkzl1MpoDKGtTFBAbH4ol3pYSRl09MHn93h06NIRFrjqbzUJtQFydTKrHvGgPooTX7OlMLgddkBvBb7ujpvFJVfgXWVOK7rfY5jmq66-COBrd-SPoCLEbzsZrUU2wAjzgRU0RuwvrDGhGuxA4XRqQZq5mnAlLZOxDLDdOB0ZZPIwsOoc0uGasV2KswShaLzIi1pHEOjOP7vYNbmfW76G9T6bY9OJY4LUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3466d6772d.mp4?token=W4izeSVp5Lgh-juhZE-npNSVaP6Q-UfNCueQDjdmN9CYDfCBx53s0Pvu9frmyIi73bWFOm60LX8VTgh59PfRV8zkb2a2eEkStq46BDyrqNHFvMKlUNId1Cclu_9Zv_u-IvhQuuG50MoV7wfZgFkS4HVgmo_G0J-l-C9SBohNbbixyUytgC2pzXmYFi2vJDrbtmX8AwIyMHMzJBK2_X5OJlKDIMsvyDcow5IvVcpdHwMK6LCCISXSc_HRUBvaDqIOdU9U6xwUPIj4t7xGu4gao-5Yp1OXkyd95_k4zcYk2R8dTn3qUpb7FTisAUWsZs3WJxb_iphIYr5efwNV_HtyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3466d6772d.mp4?token=W4izeSVp5Lgh-juhZE-npNSVaP6Q-UfNCueQDjdmN9CYDfCBx53s0Pvu9frmyIi73bWFOm60LX8VTgh59PfRV8zkb2a2eEkStq46BDyrqNHFvMKlUNId1Cclu_9Zv_u-IvhQuuG50MoV7wfZgFkS4HVgmo_G0J-l-C9SBohNbbixyUytgC2pzXmYFi2vJDrbtmX8AwIyMHMzJBK2_X5OJlKDIMsvyDcow5IvVcpdHwMK6LCCISXSc_HRUBvaDqIOdU9U6xwUPIj4t7xGu4gao-5Yp1OXkyd95_k4zcYk2R8dTn3qUpb7FTisAUWsZs3WJxb_iphIYr5efwNV_HtyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توپ رسمی جام جهانی به ایستگاه فضایی بین‌المللی رفت
‌
🔹
مهندسان ورزشی مرکز جرم و تعادل توپ‌ها را با دقت اندازه‌گیری و بهینه‌سازی می‌کنند تا حرکت آنها قابل پیش‌بینی باشد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/661645" target="_blank">📅 09:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تحلیل سیاستمدار فرانسوی از جایگاه جهانی آمریکا و روابط منطقه‌ای ایران
سیاستمدار فرانسوی:
🔹
به زودی ما شاهد غروب «امپراتوری آمریکا» خواهیم بود؛ کدام تغییر رژیم؟! در ایران ما صرفاً از «اسلام‌گرایی نظامی» به «نظامی‌گری اسلامی» گذشتیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/661644" target="_blank">📅 09:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ونس وارد سوئیس شد
🔹
جی دی ونس، معاون رئیس‌جمهور آمریکا، برای شرکت در مذاکرات با ایران وارد سوئیس شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/661643" target="_blank">📅 09:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تنگه هرمز هنوز به صلح نرسیده است؛ با وجود اعلام صلح، بیش از ۵۰۰ کشتی همچنان در دو سوی تنگه هرمز در انتظارند و بازگشت به شرایط عادی زمان‌بر خواهد بود/
اقتصادنیوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661642" target="_blank">📅 09:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رسانه‌های انگلیس از استعفای قریب الوقوع نخست وزیر این کشور خبر دادند
🔹
عضو هیئت رئیسه کمیسیون صنایع: افزایش قیمت خودرو غیرقانونی است
🔹
تجربه موج بعدی گرما در کشور از اوایل هفته آینده آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661641" target="_blank">📅 09:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
لیبرمن خواستار سرنگونی نتانیاهو شد
وزیر پیشین جنگ رژیم صهیونیستی:
🔹
آتش‌بس با حزب‌الله ما را می‌کشد، هیچ راهی جز نابودی حزب‌الله وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/661640" target="_blank">📅 09:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXpvBwwX0KUyKEoSqHpSflsV1Izpx6QpCJxbZRPW7vgdLBoRxS5YH0zKdUtcD7f3T_wh0KUJ2brzbZgWzICLDJq8kSB3Tzq9s5wzq4uv5NDpofK-sLNDcbNZilXAL0Iow-32_Sy8est8uRYWk9LxQNB3vlp0GQOX1owI5n2h_MoE4yiL7x9n84Z7oNW7QrSlPuioW0Z87Ctzhc45H-6LDNZ9PPDx4NfohNDohifEVxWBvRIQcsSqGY2k6Fwx4nuiqYSOF3YUs9iSQ6gVowJ5fVYZ6rbYl3mYikRtZ8M3THT9JXa9IwUICjlHhWRCXlwqfRQk2sZ30MUqyx_NfENqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی امشب مقابل بلژیک با تصویری از بیرانوند و کورتوا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/661639" target="_blank">📅 09:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9bc3ebe5.mp4?token=YO4O-mQoHPXS76LNJ2QUXviqGXO7h-BDwRY3SJYQiQabfb8O9phhGOT3F02eSdVSPLAWnTpcvHPAqkwha2Zr9iHp426zmAlXBOFP7p4Uf2Uq0Q6u2950yEjrDBvW7nynJbDfVUK28F1ZJhlrLdyGCAZLlAt2RQvnUeiaE05xLwmfzyU-ZLxhR-0oaXtdXw5M5uVTwsBIgXOBrWhhVV_t__rWchFREzAKvQSA24TFzB106VTIa4wZ0sXqezIgPxLxbPGTHpaGbEurx7VdldvuCFJzyZm9EnMGV7zKO90ncZybJWENXVHHLTP3byMTdbZoECuqhJMszPSWNLrey2iPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9bc3ebe5.mp4?token=YO4O-mQoHPXS76LNJ2QUXviqGXO7h-BDwRY3SJYQiQabfb8O9phhGOT3F02eSdVSPLAWnTpcvHPAqkwha2Zr9iHp426zmAlXBOFP7p4Uf2Uq0Q6u2950yEjrDBvW7nynJbDfVUK28F1ZJhlrLdyGCAZLlAt2RQvnUeiaE05xLwmfzyU-ZLxhR-0oaXtdXw5M5uVTwsBIgXOBrWhhVV_t__rWchFREzAKvQSA24TFzB106VTIa4wZ0sXqezIgPxLxbPGTHpaGbEurx7VdldvuCFJzyZm9EnMGV7zKO90ncZybJWENXVHHLTP3byMTdbZoECuqhJMszPSWNLrey2iPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتاض هندی ۱۲ سال است که ننشسته!
🔹
«دولت گیری جی مهاراج» مرد هندی نذر کرده تا پایان عمرش هرگز ننشیند و معتقد است این کار او را به دیدار الهه هندو «ماه‌دیفی» می‌رساند. او حدود ۱۲ سال است حتی برای خواب نیز به‌صورت ایستاده و با تکیه‌گاه استراحت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/661638" target="_blank">📅 09:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661636">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiyIPMv5g1EivlpeJLNHcLz2gLJGOXb3oWShqPyfHEs7gJkf7cKozkOum55NkdYyXpP5eh-zw2qEYPzxgccekWFk-kYYLM39l9W3VC3PTZRxISUuZEe-8gueZDynaQfmMVw3K2KwXik9deDnWbD8-3Wx0Z3TBu8fR9y57kNKAjAcRa4J42YJYl4kIG7WwlXOx81Rtyfo3B0rqt2BQY6H8VjTlbtaDzazlvItLVxfFZScnZubFRgmV2AHh-USly59DVR0pp_hQ7jGyBeXdXiQo4PguU-vWmeK8nulMTw8x84sVbtvLEu9F5e8hp8wz_fx-waAard4uMaP0RbAH8RAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c9d4dbee.mp4?token=m2DaJhO_jwMy2X-bGZCvOU9rLHI7xbgNcUuUsKxRzfvvWpQJaJdjAml-mOUyzuQKPzyLkYu2XClYHC9HgA87LqdUL4A-yetFWR_Al9E7yhyEupIQNkd37ASe7IXQBlhYZACAJGqVNOmFWnDExAZhyJTulyuKd8T47brn3uwuQQSAjM09dHiDaEr-xSJvSDE47S4D8NGBdc8pG8-mwD77rMQDtf3457O0nmJumsbY9U2hq_wnJphX92q0TUpUN2Oivft0DssZr2PDdaQxzHb7RMWJL7bWuYKuSYRLTHgqLmhAwOa6t5AFAfAksca39nAnsf2Vf8tRHyiaIv81AS104Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c9d4dbee.mp4?token=m2DaJhO_jwMy2X-bGZCvOU9rLHI7xbgNcUuUsKxRzfvvWpQJaJdjAml-mOUyzuQKPzyLkYu2XClYHC9HgA87LqdUL4A-yetFWR_Al9E7yhyEupIQNkd37ASe7IXQBlhYZACAJGqVNOmFWnDExAZhyJTulyuKd8T47brn3uwuQQSAjM09dHiDaEr-xSJvSDE47S4D8NGBdc8pG8-mwD77rMQDtf3457O0nmJumsbY9U2hq_wnJphX92q0TUpUN2Oivft0DssZr2PDdaQxzHb7RMWJL7bWuYKuSYRLTHgqLmhAwOa6t5AFAfAksca39nAnsf2Vf8tRHyiaIv81AS104Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارمای اسپانیا به ژاپن رسید؛ توپی که میلی‌متری گل نشد!
🔹
شوت ژاپنی‌ها مقابل تونس با واکنش تماشایی دروازه‌بان از روی خط برگشت؛ صحنه‌ای که بسیاری را به یاد گل جنجالی ژاپن برابر اسپانیا در جام ۲۰۲۲ انداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/661636" target="_blank">📅 08:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661635">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8owHnYxKYi34J2NvrRqVe73i2XWuJdQG3i3L2l0hOJmD91CXfP3vmVtrgkpZDV8eQaJVsdUmk2CgV4cgXvOr-lmyxyi8HW8Icbp2aMF9TefBUGvUs8PhUbTJyw6C3NoiyKVaARdRDcVE1rIU9u_GDEWvrsLG2r4Z1i7u0wL0-iXHbZO5BEk9s8-5kBUob_Kz26GiDMx-uUFaLfpnye12QV9cX3PopdAeiyB-DeRNl5QVgSYFLYEYx2orXz-_t04ByO8w6E2MmJBD5jfsXWRWwDlJXRuTdRTW3jeGBrPEd9FcAaMg3CRo0Bs0tVywzcZzsz5RtEKdqIFm2S3uSFmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت رونالدینیو به فوتبال در ۴۶ سالگی!
🔹
رونالدینیو، اسطوره ۴۶ ساله برزیل و برنده توپ طلای ۲۰۰۵، با باشگاه راونا در سری C ایتالیا قرارداد بست و احتمال دارد بیش از یک دهه پس از آخرین بازی حرفه‌ای‌اش، دوباره به میادین فوتبال بازگردد
#ورزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/661635" target="_blank">📅 08:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661634">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اجبار دختران به برداشتن چادر در آزمون سمپاد
🔹
اخبار رسیده حاکی است در برخی حوزه‌های آزمون سمپاد و نمونه‌دولتی تهران، از دانش‌آموزان دختر خواسته شده برای جلوگیری از تقلب، چادر خود را بردارند؛ اقدامی که به‌دلیل نداشتن پوشش مناسب زیر چادر برای برخی دانش‌آموزان، موجب استرس و اضطراب شده و در برخی حوزه‌ها نیز با حضور یا تردد بازرس مرد همراه بوده است./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/661634" target="_blank">📅 08:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661633">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
قلعه‌نویی: برای بازی با بلژیک کمتر از ۱۶ ساعت به ما وقت دادند و مجبور شدیم تمرین نصف و نیمه‌ای انجام دهیم؛ این کار را سخت کرد
🔹
نسبت به بازی گذشته تغییراتی خواهیم داشت
🔹
اجازه دادند که برای بازی بعد، دو روز زودتر به سیاتل برویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/661633" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661632">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001b5e2780.mp4?token=ZPNq56Tyl6IRvih48faj_Gcwzro3FX__oEqObrj_Kahnjb3LYwbC6bEsXYqOSgEktjJAP-ad-dnPBQ0FAY2-k4459GxIEbh7VL0-MvhEKLoNsnVmzKFyq_89GoLm_iTgA7_36gTeLKzF1pTa4BM7xNjNPSbkSWtfMCV78YQQjnZJymrVZ0WDKK1UTTtV8OBWNM8OzvH_V2gG6sdJdhNMSO-t4W0TOFPIW1mx2fQ0TCDyFxQPMvo38s4IVfAVCokm5mhAuYsvninzkx40P2dfQjGE6gaJSbN69_d7cAfU7VCJDmzUrlbHjYTbYC4enpZPktgANz0L2ay32jfAZE3Zfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001b5e2780.mp4?token=ZPNq56Tyl6IRvih48faj_Gcwzro3FX__oEqObrj_Kahnjb3LYwbC6bEsXYqOSgEktjJAP-ad-dnPBQ0FAY2-k4459GxIEbh7VL0-MvhEKLoNsnVmzKFyq_89GoLm_iTgA7_36gTeLKzF1pTa4BM7xNjNPSbkSWtfMCV78YQQjnZJymrVZ0WDKK1UTTtV8OBWNM8OzvH_V2gG6sdJdhNMSO-t4W0TOFPIW1mx2fQ0TCDyFxQPMvo38s4IVfAVCokm5mhAuYsvninzkx40P2dfQjGE6gaJSbN69_d7cAfU7VCJDmzUrlbHjYTbYC4enpZPktgANz0L2ay32jfAZE3Zfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ایستگاه فضایی بین‌المللی در حال پرواز بر فراز استرالیا و اقیانوس آرام در شب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/661632" target="_blank">📅 08:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661631">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تیم ملی کاراته بانوان ایران قهرمان آسیا شد
🔹
تیم ایران در کومیته تیمی بانوان قهرمانی آسیا با برتری مقابل تیم های چین تایپه، ازبکستان و ویتنام در دیدار پایانی هم مقابل ژاپن صاحب برتری شد و به نشان طلا رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661631" target="_blank">📅 08:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWgTmXpCQ6olMOn3tu5gbYiEizmd2eB6NzGQeGVP7-lcWdnBzOOV4R10xQw3mxZaA2PNDc3xAYngymSW0m5PEgKmYMRlwgOP7lA4uBz7GON2e2W4m0MRp8A70hYx0C9G9hRTHmqpWE8KcEoZwftHm64bRFAXXQBabR7hkbkmmpbgnSzSUauPnU9hqPzXywZF03vxfD0wyf9g0RJbVgqLkM_uCxIfl-l_8wGJS8aRsuhM6SDzD0DaCf_egA1LBC418XoIu43eA_LPmOt8o9rhuzcOzP2yTmLNThp3z9_ZiizflIOr7w2Yd-jwYAh4nwzKBrgYgKiPL90_PJCLJrKK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8SO-IMUFDffHB9h9yT9jDP0IGcM_mXGRmexfx83ZvXF-T4szMp69BTWurjaMoaXlfY7-37CD6DhOPL13RGPsekIfyptTfwebT3c5PqXy0PG4LUDhoNuQvQu8_byvplF65SbTbKf3v2Ln6w1xlKRO8EEdQMofnMQ3n-tf_q4apMpTjBhCGCtuTlsEZkT5Z47HsS00LeVTfUOwIPBqMLbMP_VNjj6zwlBBBUYLNBqT7TuJqyKRGFwA1WQbmKF5n4WWfY2gTvIaox4P4drij3Ui57dtZtboZe80XMQBZuRx3ZeScqE8WsmThAiWmdrSVQw0Vf-WvbRlvnS7a4Hd2ufHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1uaW7RdtTlAOJ6aWkWbUlC2pYZREnQG4PS9o_ITh_8RdlbG_s9E7vgUsK98cqqA670BZCkxbZDncHOtgMX7eK9Q0_cHJiSRIleZZDB0DwTQY6j2gitkAdGm8M2I9U2RW7gcD3M1R9GMIS5AYxQ8vD85UONkown61TaqbmHNTH-3rMLc9ceMAlXV_9oj5ibYbpf99umJ2D7K6uZkpHM_XyI1s3ffp4FNFc3-mADzeoVtiEGV1zQD-t9sa2RJrdCoDMGGyoYoFwF9UbaYD2-q__z9wTtb8ci_bkeuXH-WB2m0Xtv5v0CcRNTnslpmzlb5TgQcwyCIjt9EmzEN9VjDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm_G_Bo7UWkO7Mj2YVAfku4x4tgdTzMsdt04305Df8m7jKo3_jArCARjkMzwitgtsRgz0vpocWgDdX6M50yiauKri7ZJrtpzN65O7NajQ9TDjjXgxa3OpKWZ5msnhF7ZgecwcQmhKvQ-pIP-0TNdsDR_Vqk7o-NrBKz9QxNzp-ZQ2ZGusFVf7FxR9mdrab9GfsQ50A4bifk6Bg6rJDDcpiqrXu0r5rBmel2WlrNMNGJbblDvgi1SE26cJKSYzCaiygz-z6VDIwxScvQUdaMyN16KJ0Qu6ijIIs9-iv9qxKhKZDZ9pso10Bfmu4LXgrjPPs-iEju-I2oAifwD0ZAyrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب جادویی قلاب‌بافی و گلسازی در تاپستری‌های خلاقانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661627" target="_blank">📅 08:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سی‌بی‌اس: موضوع لبنان در نشست اضطراری مذاکرات بررسی می‌‌شود  شبکۀ سی‌بی‌اس نیوز آمریکا به نقل از یک منبع دیپلماتیک مدعی شد:
🔹
هیئت‌های ایرانی و آمریکایی قصد دارند در یک نشست فوق‌العاده و اضطراری، مسئلۀ حزب‌الله و اسرائیل را بررسی کنند.
🔹
به گفتۀ این منبع…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661626" target="_blank">📅 08:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=Pl4qy0KEic5WDRPO07911TXUbSGaCYOpFdDj8-tu0uRlHwHnWQ0aFX999UG-RtseVbWPWLhJ4mb6La4Z-ulvpQ24y5zPBtExXuNG5glNYUZ2RkAxsnw1PfNqKRROdOrb1jkqG0aNTkt_GhmONCbwhAR169IX_boE4MzNx519c90Cfh6nN_fK9n3w-ci7ceN_Us5GdICeq0BOL7mytriSVrSNhbCChuw-0Ek5CBhKSb_TJ3bkmyF7TX1Ac8BvDHVCZR28GRU1c32crVQYpLoV5sKWNw_bI4BULuDKaBZ1RYOc3Owdl8OCsnhocBk7_1g6k8hNyF7rBHnYWLuoO-zBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=Pl4qy0KEic5WDRPO07911TXUbSGaCYOpFdDj8-tu0uRlHwHnWQ0aFX999UG-RtseVbWPWLhJ4mb6La4Z-ulvpQ24y5zPBtExXuNG5glNYUZ2RkAxsnw1PfNqKRROdOrb1jkqG0aNTkt_GhmONCbwhAR169IX_boE4MzNx519c90Cfh6nN_fK9n3w-ci7ceN_Us5GdICeq0BOL7mytriSVrSNhbCChuw-0Ek5CBhKSb_TJ3bkmyF7TX1Ac8BvDHVCZR28GRU1c32crVQYpLoV5sKWNw_bI4BULuDKaBZ1RYOc3Owdl8OCsnhocBk7_1g6k8hNyF7rBHnYWLuoO-zBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ‌های رباتیک هم آمدند
🔹
در هزارمین دیدار تاریخ جام‌جهانی، سگ‌های رباتیک هم برای تأمین امنیت ورزشگاه‌ها حاضر بودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661625" target="_blank">📅 08:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE327KLogDMCHS7nVzOGmP_YIQibjpbNUrNfDaB1eJfZIxPzLsAnD91e9J1aC2V0VYZb5_E_TNpJdB2_QgKgeSvSRdYS5lV5JTcO28yDenjCMcasairzDHTEn1E926F4PFJb_cHUkNUu1sx9ixSissY7wULE9tjoLNmfLmAtzFwehQ8ALsvvWMok6LmkGYoPLEzlHt0dtxPIwEat2joGBfQYLdmz2hxdSKmM16SqR0JDdP7ExDPlHFki9W03d4tfkU5CmhRURFCxgudCrFDnaUZw2Y5mpOyzBfugRYlen2tgCHidKofgGaKZSbf71l06gOdcirvNS6YbRq37J5FWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: آمریکا و قطر در حال بررسی آزادسازی ۶ میلیارد دلار از دارایی‌های مسدودشده ایران هستند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661624" target="_blank">📅 08:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240e6fb06a.mp4?token=XRkvdnYIW2u9Yy5C5YA7tjDiGlqbL5yhTVQEKeAyZyzR9j6U_vfbGiy2T6hPjtDtpBuyIomk1W1Y47bVtvOIG-mDDXBEOgSOGb9wWvaZxJ-gic8Q3rACuJfemsif75fmDkZGYN2A3eQ9ZFXhaSrJw5Ee0_KhbT59-IeCRUwzTKVLDS8KRvyz8LPlWuD-LnZYbxpNJCCZirGy4rZfqFK0vwKKafE_CqnfNnPpXFDYNCai7SCC2gN_j1ypO1Qg_Tgz7_j7xriH53zjVWgA8gsAPv6Wxreg89DRqSLSLkEjfDVNUOyuNrtm7NZ25QeH3pfTc0JO3ILhVKTxsPbsb9HUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240e6fb06a.mp4?token=XRkvdnYIW2u9Yy5C5YA7tjDiGlqbL5yhTVQEKeAyZyzR9j6U_vfbGiy2T6hPjtDtpBuyIomk1W1Y47bVtvOIG-mDDXBEOgSOGb9wWvaZxJ-gic8Q3rACuJfemsif75fmDkZGYN2A3eQ9ZFXhaSrJw5Ee0_KhbT59-IeCRUwzTKVLDS8KRvyz8LPlWuD-LnZYbxpNJCCZirGy4rZfqFK0vwKKafE_CqnfNnPpXFDYNCai7SCC2gN_j1ypO1Qg_Tgz7_j7xriH53zjVWgA8gsAPv6Wxreg89DRqSLSLkEjfDVNUOyuNrtm7NZ25QeH3pfTc0JO3ILhVKTxsPbsb9HUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اصلاحی قوز کمر #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/661623" target="_blank">📅 08:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxseqds5Z3EDYUBRcqzI9sRij8bqWrAFbo_k1F5ZUEW3ac_pbUDl9OziTwkK_nf_oCWwkLndvPvRY8HLgWZQbdf1Z_xnIA6fqAbojHGw4rA1-B7LXcFi0cIsYRxjzJgQm5jY3S7Y2WUjFQWMPuOtvETqC48Cj_ocTLoQvLKSXLlJj1cbGKCcvnZLM5QBEa8CygrJ_WWxNx3Vl6PuGKwDg7TWoxNtEZ6YrAPvugCiVQc5nPV62S6H1F-_o12qfZMuPZ13zFmz8340uQce3-noIHi0qghzH465512nYuanBdlMr68z1aBHC1zg-cUOYuRVUY_yotoEBTv_6O2v3g3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخت افسانه‌ای رابین هود پس از ۱۲۰۰ سال از پا افتاد
🔹
درخت افسانه‌ای «میجر اوک» در جنگل شروود بریتانیا، که حدود ۱۲۰۰ سال قدمت داشت و با داستان‌های رابین هود گره خورده بود، امسال برگ نداد و کارشناسان احتمال می‌دهند برای همیشه از بین رفته باشد.
🔹
این درخت از نمادهای طبیعی بریتانیا و جاذبه‌ای گردشگری در جنگل شروود بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661622" target="_blank">📅 08:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed993766c3.mp4?token=fcLePJGcRdCtvbKUGZkTQX33zgO26hnIZTMsCtOebbMJxjHHxyfB9MY5jysotjzRCH1Qn-fxwlBPb_r3W3Yfy7wME5BtorWWUkZwx4mE9ujfl6iEeu6OxczWOzcCTp3oA7LOsZ1_HTW_ZPvOuc-MCTlDRKTYhkDm7VHjnvTF0ltIDQnfSng3LTsa2_VfolQy9OWtIbf6xk9wsI2r35CMqKLCxHoNUqmm_6hu1tUUM4OuRycsrqknoiviovipi_bqItqipdj9RVNLygSZPpXkSQ0MesW1QchuxH7if54xgfDKbds-ujwnQLS-F89WrKnpXrJa4lsd68X774CUjqUxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed993766c3.mp4?token=fcLePJGcRdCtvbKUGZkTQX33zgO26hnIZTMsCtOebbMJxjHHxyfB9MY5jysotjzRCH1Qn-fxwlBPb_r3W3Yfy7wME5BtorWWUkZwx4mE9ujfl6iEeu6OxczWOzcCTp3oA7LOsZ1_HTW_ZPvOuc-MCTlDRKTYhkDm7VHjnvTF0ltIDQnfSng3LTsa2_VfolQy9OWtIbf6xk9wsI2r35CMqKLCxHoNUqmm_6hu1tUUM4OuRycsrqknoiviovipi_bqItqipdj9RVNLygSZPpXkSQ0MesW1QchuxH7if54xgfDKbds-ujwnQLS-F89WrKnpXrJa4lsd68X774CUjqUxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آلمان به ساحل عاج توسط اونداو ۴+۹۰
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661621" target="_blank">📅 08:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661620">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661620" target="_blank">📅 07:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661619">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مدرسه میناب میزبان زائران راهیان نور می‌شود
🔹
با تصویب شورای سیاست‌گذاری راهیان نور، مدرسه شجره طیبه میناب به‌عنوان یادمان دفاع مقدس ثبت و به فهرست مقاصد کاروان‌های راهیان نور کشور افزوده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/661619" target="_blank">📅 07:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661618">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSE8djkByouudEc45OFcl36zO5vWIvLsqCU2SPdNFmm-LqW9H2426lvLFYjL9KK89F0HM2Z8PtkikxpRSjS5BEz8HsOKJDGJ1ziKB5ToHFnC3Lc9Iqy_SC7FUnPoANkxZ3Ld-WM1Nze4cRW3qvUOLLjEPjFd_9BSrM8xUUtrKvyXY7PNGuZUVRHmwNZgbHYzz7zHIsFBWCMELLUccglBJ1mksIvzk3eP3wanQ15rjXChxmtI3pL_c-5hBS8n4U88E_DRLcpoyKnNXqb1J6Waan6T7nXJEwBO5bXyzrkdOKI30VgLCc2Yrh7mpEQGcL-hi4O7fdRb9e1tE-5lsWU0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمود نعمتی با شکست قاطع ۴-۰ برابر حریف عربستانی در فینال وزن ۸۴+ کیلوگرم، به مدال طلای کاراته قهرمانی آسیا دست یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/661618" target="_blank">📅 07:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661617">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1328989a02.mp4?token=GoxPWf7dfwsun6go5HG7Yd_jpgy2EcR1MiYNRnX4JKuRfpQpxtmmPaXfvfhpVD9bntqGnWwgs5CuXZwsD81fI0rhxINdAKvh3dGVZLORJLFBZEysu456ICJQlKKY0p0Ojj-eF1-DJMbWWFC3yTiB00gHNpOHTHO3JDjT4yCL5rpjlrkAgdHwLh9bZPdabGC_tUZ5mOGhGVu91rdl71UHO91BJ4ws3D7UO86xnjAzLY2tmLbUJL70OtzQU9tiW4eHK48n4AGsmp8y4wrs-c7-1iTdRU4f_A9PhmGXvdIwKppcqcG0M2J-5PbazGokrwO-REVJpbI3avynDPyVUa-CCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1328989a02.mp4?token=GoxPWf7dfwsun6go5HG7Yd_jpgy2EcR1MiYNRnX4JKuRfpQpxtmmPaXfvfhpVD9bntqGnWwgs5CuXZwsD81fI0rhxINdAKvh3dGVZLORJLFBZEysu456ICJQlKKY0p0Ojj-eF1-DJMbWWFC3yTiB00gHNpOHTHO3JDjT4yCL5rpjlrkAgdHwLh9bZPdabGC_tUZ5mOGhGVu91rdl71UHO91BJ4ws3D7UO86xnjAzLY2tmLbUJL70OtzQU9tiW4eHK48n4AGsmp8y4wrs-c7-1iTdRU4f_A9PhmGXvdIwKppcqcG0M2J-5PbazGokrwO-REVJpbI3avynDPyVUa-CCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آلمان به ساحل عاج
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661617" target="_blank">📅 07:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5nykFsPfr5epz09Cz2yResIMxf9V_I6LFNzc26J66tlvQ7M79bxt8mT3HMsWzYpgFzvUqsYBpZliS6DYl_vgkOfejDrh3MPFsEWkIS3fIWOgXCxyytKfJjAueQ_VqfCUOwHgowLU8-Abp2ShMd1CFo7obvRRRc-yyQ2vzax5yy_6-R8MV5JqjzQWRY9vHeuaUf1kuXKhqSVuktTi3-2gT2UuTZpmed64hV6Wd3IvMOkrKyD1IT-eq5ch0gvzW7PGRfwljROBXpcGPuAT-CZ31YaAWd18IKvxEtI172F5LCdo6AbfCZWzDFphwEVxtvqwtMQMW-hJ8cHjUhK7vfrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVXZiBgr2HJX5NCUQdGK_PDn5uoHqZyOgxv-qj2a_i9duMMmrDAkpclFWr-ARv6ml8W6DhorkN02_XkM3mBiDd2eLulM5thF_dwy5gqfiqX7G2aCPltI7y-ujKEoLXdSvo0yfUpWSU_eYMqbJMoMHk8dYgrgs9E8jKWasdU9N3agMHwOxTiHTmW4M-MEFWAq6KccNBTqORMzyO9faMweiOZXq5y_fXvOFaumVJZqCRKhyiATlkSD66I6zCp9qfOfy4kiBn3mFMuOllUG29TReTJCKzlrxc0DSvu2Zog33R5ltt1OHvHwujgbQSOt5G7O3shWI9Sdm2ld4fCc7FjW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odl_9XFtH2dgaC9W411ZIIFVKmXJVdx-aWfjuyAROc2ZeAxvNUZlsX3U-DpO71B1oShMr0ooEtNTTDz4Vi37vm0LzVS-TpKU8_hO63xdMm8NcS7IqkCN-_iGXqd3mh768AI1IKF6Hbx865GPwpzdkRXI-3fccIULBbsww3WN2v9UWW3E7lQKEWru7t9ujsHZ7aKYRnR4rIzqDGO_Z804z3dXParlhUVrMhOmPS7fBsuCoVSYO2oM64LhvoiP_g975ibXzHhqqib6PtHsvTXPdGT6qJBoTYytT6cjF7DCGBOS5u-_S19r968_Ta0cleAhKegGLG0oI9Xl2khvh9WEKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هیئت مذاکره‌کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661614" target="_blank">📅 07:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e200fbe4.mp4?token=UeP6QvPDxLZ6X1K_EtzwpC-M0AJ1XxpLkIFkUSkwWpFKWW3-FxkmUZhwcW1d2covBY-xTqcv_isf8XN7zQEJSJ6JatHlSssFCnZrLi5_V07RNIyXd3sK2RW6J5dF3odQGpe7hWkZz78D1jvVv6YsnICcxLUUHHV41B09-3to6x8VceNf6-yr5cHUJe5rO-6GoY4jrMuxqAe3PCWOZtSQ12ShCMcvWPmN48kihTLbhEnHAGk3qoRPTi20FDmQq9Kb-G73EzWty_CllFc7ZW3uqkuvYAZtQIhRNAuByrWl9SbnQOipTNae15Itsr4Rb0V7PvsGk5ouGZGxpQohtQDC-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e200fbe4.mp4?token=UeP6QvPDxLZ6X1K_EtzwpC-M0AJ1XxpLkIFkUSkwWpFKWW3-FxkmUZhwcW1d2covBY-xTqcv_isf8XN7zQEJSJ6JatHlSssFCnZrLi5_V07RNIyXd3sK2RW6J5dF3odQGpe7hWkZz78D1jvVv6YsnICcxLUUHHV41B09-3to6x8VceNf6-yr5cHUJe5rO-6GoY4jrMuxqAe3PCWOZtSQ12ShCMcvWPmN48kihTLbhEnHAGk3qoRPTi20FDmQq9Kb-G73EzWty_CllFc7ZW3uqkuvYAZtQIhRNAuByrWl9SbnQOipTNae15Itsr4Rb0V7PvsGk5ouGZGxpQohtQDC-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیدز بریتانیا؛ تظاهرات در حمایت از غزه و اسرای فلسطینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/661612" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پرواز فرودگاه‌های بوشهر و عسلویه دوباره برقرار می‌شود
🔹
دریای مازندران تا سه‌شنبه تعطیل شد
🔹
سرمربی بلژیک: برای شکست دادن ایران باید با صد درصد توان‌مان بازی کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/661611" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656df50885.mp4?token=Il39EEktfb-hGIklr_rEgE4UJ0rRehR2jqUcJ7wNC2Db3hAFd4TrXkxy6s_u2AVIegUI9XXu-BSmhWEFJO3NDhIrV-LOiOiBdzuLYYmrKdU77LOlB3AatUPvmukvYai3C7scVMkBFkYZie0zbwcwhidadkRsHiD8cqYBzm8ZCr5H7HDc60QwOa32IHpNXAtrMJG7aPHneNg4TV2sOJbujcIYDeeiQFa3Z4fnhv-pP8BwvggZjMNQTelK3NQaGvgSuYtF0YlWGvO-fpLjZywawhhQWAaoDbCfsIHj36GlsCjpXcq8zCLgsn6sTNazlwy6K56fssZfA31Rrz86VYaAuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656df50885.mp4?token=Il39EEktfb-hGIklr_rEgE4UJ0rRehR2jqUcJ7wNC2Db3hAFd4TrXkxy6s_u2AVIegUI9XXu-BSmhWEFJO3NDhIrV-LOiOiBdzuLYYmrKdU77LOlB3AatUPvmukvYai3C7scVMkBFkYZie0zbwcwhidadkRsHiD8cqYBzm8ZCr5H7HDc60QwOa32IHpNXAtrMJG7aPHneNg4TV2sOJbujcIYDeeiQFa3Z4fnhv-pP8BwvggZjMNQTelK3NQaGvgSuYtF0YlWGvO-fpLjZywawhhQWAaoDbCfsIHj36GlsCjpXcq8zCLgsn6sTNazlwy6K56fssZfA31Rrz86VYaAuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای جنگیدن تا آخرین ثانیه آمده‌ایم
🔹
ویدیوی صفحۀ رسمی تیم ملی فوتبال، در آستانۀ بازی با بلژیک را ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661610" target="_blank">📅 07:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c527a10d52.mp4?token=HiYhOFfqNIfRPbrK9icNXfBU-jt_hbPuwOvt61niyQ9aSsVXoq4wCAZb7rLxU2-fDQvj3Gacf2T8LrfWei1Rn0ACiFxLuhfCVxUKz0FCIcBibbTLMsUMowaGxHbPZbo8a2s970Dwxyu6zEHrgp2SZEw3AmRKzSCxKnrZZWM_8-bbGtFl2mZy7EA_KUm-LaS_lHrQwx0wNGb0JQ8fHIKeLMMNAXRhsxBPY4jbDGTzBCI2s7K3B08YHDyoZonWEVZK8SXLnCDL2t7-Vg66ROfyaMo3zZyuKg_KAhCgm5NF2rkSlBvJZiaWl2usIwcLFTGyzVJTqmtAl7bFWOSf45VUEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c527a10d52.mp4?token=HiYhOFfqNIfRPbrK9icNXfBU-jt_hbPuwOvt61niyQ9aSsVXoq4wCAZb7rLxU2-fDQvj3Gacf2T8LrfWei1Rn0ACiFxLuhfCVxUKz0FCIcBibbTLMsUMowaGxHbPZbo8a2s970Dwxyu6zEHrgp2SZEw3AmRKzSCxKnrZZWM_8-bbGtFl2mZy7EA_KUm-LaS_lHrQwx0wNGb0JQ8fHIKeLMMNAXRhsxBPY4jbDGTzBCI2s7K3B08YHDyoZonWEVZK8SXLnCDL2t7-Vg66ROfyaMo3zZyuKg_KAhCgm5NF2rkSlBvJZiaWl2usIwcLFTGyzVJTqmtAl7bFWOSf45VUEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661609" target="_blank">📅 07:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سی‌بی‌اس: موضوع لبنان در نشست اضطراری مذاکرات بررسی می‌‌شود
شبکۀ سی‌بی‌اس نیوز آمریکا به نقل از یک منبع دیپلماتیک مدعی شد:
🔹
هیئت‌های ایرانی و آمریکایی قصد دارند در یک نشست فوق‌العاده و اضطراری، مسئلۀ حزب‌الله و اسرائیل را بررسی کنند.
🔹
به گفتۀ این منبع دیپلماتیک، اولین نشست دو هیئت به این موضوع اختصاص خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/661608" target="_blank">📅 07:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjOdvzWB-WPLyweEuPqK5MUAaw3E0r0-flU4Q3BJ9vc887PpWJ0BEh61SL90E1TbSJ5kOBVYlcs0xEuuEohOBeDuytbPMvn0hpLP9j2ZWLktMdiRZkIW2SFUoC9Pfb-_Um5mlxSeXDknK3pB-uLJiJ68_C1wzF4L8bzuS1lPVup82Tc3HxNf75W8l1OSnVBaPbwwqpqCIXqxVeCVrfWE8SfoJqZtXLomjocH5WvMF_kjJi2di__Aw001JwnGcJDsXoU39EFyutWjrZara1XUKxiF0wxkakyAQ6wsNXYBwIAy6UfrJjhZMQUEW2y_6DqlJhzeQW6VJOWiZquS8dfUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۳۱ خرداد ماه
۶ محرم ۱۴۴۷
۲۱ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/661607" target="_blank">📅 07:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4gtYktGezqLUWweU71rfyRCZHMzECgNaej0e5pxY6R-_qsFbNZfNDiNYiKE2uwpIlXZzZRSB5ZitDnsbHJ7OoLc8DQCBvZGtDm2z2xOJEQKVcvzu-1ns7qoImizr8RNnWTGfW1qN4PykrOQodlDJav4Vu4I0-yvu4vw2mwn-TWhtNvkjXpoEp8OKFLk8_CM8xojXKOGMCIoa4awn1PsD3ZOi1yDNNrwldcJpOC3JnAAfdVLdGA_iib_LWHVYY9i2DqLrxXoSKSLtzlbK7ZUCJ-q5yxHV_WfLZBl0xtZli7Nl6tDyALXhh3l9Y050eNsKDUv1I-dP-d1Y0gLHTn0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
۷ روز ویزیت تلفنی رایگان
توسط متخصصان
اورولوژی و نورولوژی
، هدیه ایزی‌لایف به مناسبت هفته جهانی بی‌اختیاری ادرار است.
🗓
۲۵ تا ۳۱ خردادماه
🔖
کد تخفیف: easylife100
❗️
اگر مبتلا به این عارضه هستید یا وظیفه مراقبت از اشخاص دارای بی‌اختیاری ادرار را بر عهده دارید، برای مشاهده لیست پزشکان و رزرو نوبت رایگان وارد
لینک زیر
شوید.
👇
👇
👇
👇
📎
https://B2n.ir/ue2237</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/661606" target="_blank">📅 01:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@Modaberane_Barsa
📩
یا عدد ۴۱ را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/661605" target="_blank">📅 00:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeHfSyjAFamUSeAE_Fxq8qpZqXYUd0X-l0z1ohJIE0BdlzsG950jc-LUhgXU2X52oNTfgE2iPc_xxIi6J5-K4nHBJ4zIpoyK0bRhqdBE7zokHiXu3pM6ELqPeckhCAY75qmN3ofDKyPT30LODKbQ7BvPPVtxZDsCkdZROvUtZKmJ04BoSweSpVeNsq_IQC4h1LF1KiPHwGqQDfQ49_rau8pdykBDdL6mX3xWBXokSwsxTbdixMUmI9y6yMrj6_94SJ4xaCPxLNaF3K3VSF9b1EZwfgzR4xlObwlu-WRVlhbQGJ9Xb1F5gFAUJPO5kWuzNLibNKu9lleZAsnv75PxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در بدو ورود به زوریخ: کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/661604" target="_blank">📅 00:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بی‌بی‌سی‌: استارمر، نخست وزیر بریتانیا دوشنبه استعفا می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/661603" target="_blank">📅 00:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ff94695b.mp4?token=Fm-2vywR7oL7xyvVpMu3HnzuKr3Ag4wefEea_dnzBPeowQ0Y-LFU1kAP--XlLVphgrWlXc2ynBHM9gwrIJyt_jArvk8sTEtLEfFt3l1a-GYNkGfZZwc2cqHg6rQojruCexEFDOpcQQnXvggsfhQ89-KdLNKQMQ6bpVD3t7fDCbg0rQ6Z9aT8OMWr1sqlWhWxdXMIfSuaSXCO6Rw5zw7bOx8zzInidSZZEZp1bKMbB3CIB5S60vkcKraWcu1qJCnRbtxyF2hhglGaxlme7akoXBADE6gj9EBUvvWG3sN8Glkxdo3qMx7i1u3Pr-bXjYUue4j25DuUqqf9qJsVeHhWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ff94695b.mp4?token=Fm-2vywR7oL7xyvVpMu3HnzuKr3Ag4wefEea_dnzBPeowQ0Y-LFU1kAP--XlLVphgrWlXc2ynBHM9gwrIJyt_jArvk8sTEtLEfFt3l1a-GYNkGfZZwc2cqHg6rQojruCexEFDOpcQQnXvggsfhQ89-KdLNKQMQ6bpVD3t7fDCbg0rQ6Z9aT8OMWr1sqlWhWxdXMIfSuaSXCO6Rw5zw7bOx8zzInidSZZEZp1bKMbB3CIB5S60vkcKraWcu1qJCnRbtxyF2hhglGaxlme7akoXBADE6gj9EBUvvWG3sN8Glkxdo3qMx7i1u3Pr-bXjYUue4j25DuUqqf9qJsVeHhWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان تیم ملی فوتبال به هتل محل اقامت خود در لس‌آنجلس رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/661602" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/661601" target="_blank">📅 00:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c337d72de.mp4?token=BFrz1zJQQ1jTM62e9XOnWw__9d0_4GX2_glUjvjyeItRowbWUxYT2-VOTfqYg-H_G1Ve5uJsV36MMDR_LpHEcNSHktN3LocH-Fzd59BLGll8QBkf5vpzNPy6AA1e1GQL7cvT83NRUfc_iliEyN8lWA2O35uLMVzm6pMmMNHhhA_0uB3qDL7qLPn_LHKsTsJqRm2yzkxnEH8k8ksLmDL04NqMyODR6cJU-uy2BaZlK6pMjB0H5neZiuBVH5_Be88klM-4ufpvZgbP61UedQPNnfhmU_n-96jtyb9Ce8mn2l08_hu0itNhoY4KGLTFRrtWcO7EHYde7mfHtecySWu9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c337d72de.mp4?token=BFrz1zJQQ1jTM62e9XOnWw__9d0_4GX2_glUjvjyeItRowbWUxYT2-VOTfqYg-H_G1Ve5uJsV36MMDR_LpHEcNSHktN3LocH-Fzd59BLGll8QBkf5vpzNPy6AA1e1GQL7cvT83NRUfc_iliEyN8lWA2O35uLMVzm6pMmMNHhhA_0uB3qDL7qLPn_LHKsTsJqRm2yzkxnEH8k8ksLmDL04NqMyODR6cJU-uy2BaZlK6pMjB0H5neZiuBVH5_Be88klM-4ufpvZgbP61UedQPNnfhmU_n-96jtyb9Ce8mn2l08_hu0itNhoY4KGLTFRrtWcO7EHYde7mfHtecySWu9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/661600" target="_blank">📅 00:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bc4db8d9.mp4?token=RmX-5FfPPEvTnoLDkhN0IFQNQXUPAnWkNkJbDmJacnpUkxVrXAhcx0M7wbmddrak-IfUUS-6QefkLR0fKTrL6SqrTcXg8pCDxBoSpoMXY2tXinvQ8Ztwy_qHEfggHJ_11-Gj7_ptqOHisaS1e8Y5Un9T9EZV1ytOP3828g2Nvn7iwGHI2qMWMCdhXcpnL0QwU48J1AQpZfc6_zWAbBYedlep869PQzPJXtuwup5VpkKXf5VnWCdza5f41CfC_ng31M75tyu37ZrAfYib7Hc_SgfOzPJwQX5nHsc1ubhm0CRYIfG6ZF5IMuya1Ej1IdPVkBV-ZoRfuF1A6kE0h6NnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bc4db8d9.mp4?token=RmX-5FfPPEvTnoLDkhN0IFQNQXUPAnWkNkJbDmJacnpUkxVrXAhcx0M7wbmddrak-IfUUS-6QefkLR0fKTrL6SqrTcXg8pCDxBoSpoMXY2tXinvQ8Ztwy_qHEfggHJ_11-Gj7_ptqOHisaS1e8Y5Un9T9EZV1ytOP3828g2Nvn7iwGHI2qMWMCdhXcpnL0QwU48J1AQpZfc6_zWAbBYedlep869PQzPJXtuwup5VpkKXf5VnWCdza5f41CfC_ng31M75tyu37ZrAfYib7Hc_SgfOzPJwQX5nHsc1ubhm0CRYIfG6ZF5IMuya1Ej1IdPVkBV-ZoRfuF1A6kE0h6NnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهردار نیویورک آیپک را «هیولا» توصیف کرد؛ «آن‌ها میلیون‌ها دلار پول‌های پنهان را صرف حفظ قدرت خود می‌کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/661599" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان و هسته‌ای پیشرفت حاصل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/661598" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0bba0bd1.mp4?token=ieadhPNuRn6_JFJyDGDmcAvdXJ95ldjUpQeTjLQgk9omB1bHc3QE3FyXvRPcO5bBLMhtmin5BcEJGp6_p7lKs_MaugX3hB1jqIGy40glxvxDH2eQEPkdl-cz6aTf0Pcr7LflR2IX6QOjjjajd_AMNImpoyCBdVAYl8Qo_EJJ71Dia3X1WzNDxPQjye5aE9Mkf6A8I5xzla5ZDFGEHTgv8DP3qtjlFrJ2vxuPCON8xv8pKuEYp5BYaF4CJyCceY0SoDZaZn6UZAEU_H84oNew_5LY9ZFpFIYdPR3P1nD3zXvw5GlsuxE0ZHyRP6SGWuP03qR5VG27qGRqGqPUmmJ9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0bba0bd1.mp4?token=ieadhPNuRn6_JFJyDGDmcAvdXJ95ldjUpQeTjLQgk9omB1bHc3QE3FyXvRPcO5bBLMhtmin5BcEJGp6_p7lKs_MaugX3hB1jqIGy40glxvxDH2eQEPkdl-cz6aTf0Pcr7LflR2IX6QOjjjajd_AMNImpoyCBdVAYl8Qo_EJJ71Dia3X1WzNDxPQjye5aE9Mkf6A8I5xzla5ZDFGEHTgv8DP3qtjlFrJ2vxuPCON8xv8pKuEYp5BYaF4CJyCceY0SoDZaZn6UZAEU_H84oNew_5LY9ZFpFIYdPR3P1nD3zXvw5GlsuxE0ZHyRP6SGWuP03qR5VG27qGRqGqPUmmJ9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیئت مذاکره‌کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/661597" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM5kjLfMKCPC_mgRY89_EOvYZ4nli1M67HIlE9EzKFJI5rUarrJG69mbFLb8qnWj5NJl6HCSQNXkpJP0tR_FTeh8jj1FwLKxY08atV-mS6_SCTu5x-5ymuDwnif1N1vX_arqClP2UEHht0qg9Fx_M8V03JhCvDFsqVIJDagokpE5vVng7oN7YOMmnX7770lvPOY3PVKvcBu4Jmo1hut8RpBIp1EB_05P3ikVT-DXB5pN4aKk8ZD80q5QBt-bk7Hr9mFOFkdQeYfgod4jKIKBbKx0wwsvpE3TYhzK8XkzJF6sSidDO0vMLWXfg7hjiyp42Uw3vD7-016pbWsbPBSczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/661596" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661594">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73197ae8c4.mp4?token=FAehR-0S4lFvN2Uhf4mf3FIqDu0txNdTvIbsOGQhOOhcmPb3pfH9nKYlLYWpqRC6wP4O4oOqbSpd4AOj_-jS1zqiEj7f-S3DUVEoIC8gsMkXECYUBPUKY4N4VmQ6BDFNonS-bxAGtMINAeu2Rx2RhXC3oG6CBrTwWUPp33ZOzhCUmctrME-_YDZlarcYt-Ftlfqfi8_n_jDV3Ctti9VM4EYwP-lswbgrXmM2pKZAUH4Li182yh3U3LgxSQc7PivlkAvw4Gt-VkbJ3jfEBd6pGBwoC2Bryv6eq1_ic4PWM7L7vFz7B86KiYiGhcOWAIsTzORyYSdiioCwUfxJsPxtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73197ae8c4.mp4?token=FAehR-0S4lFvN2Uhf4mf3FIqDu0txNdTvIbsOGQhOOhcmPb3pfH9nKYlLYWpqRC6wP4O4oOqbSpd4AOj_-jS1zqiEj7f-S3DUVEoIC8gsMkXECYUBPUKY4N4VmQ6BDFNonS-bxAGtMINAeu2Rx2RhXC3oG6CBrTwWUPp33ZOzhCUmctrME-_YDZlarcYt-Ftlfqfi8_n_jDV3Ctti9VM4EYwP-lswbgrXmM2pKZAUH4Li182yh3U3LgxSQc7PivlkAvw4Gt-VkbJ3jfEBd6pGBwoC2Bryv6eq1_ic4PWM7L7vFz7B86KiYiGhcOWAIsTzORyYSdiioCwUfxJsPxtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول ساحل عاج به آلمان توسط کسیه
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/661594" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بدرقه ملی‌پوشان در مسیر سفر به لس آنجلس برای بازی مقابل بلژیک #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/661593" target="_blank">📅 00:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjGmqV_CjtRErOH3jNReD1G42gQ7IjEO9gQPrZ8W931RY9lWPG46uw4FHsOaDdWq6nPxWL1Iz_hVWio_NSekVzRvPPHmtz1cbgCxkuyiR0E-YPoBQ37G-ag1ODHqVx0p9ZZOnFOSrXXA4EKBNbw7WyxtMqmKpYHmmHzic9Vdy5LCKzHSiBEH8BPghWbUy1bGuB1k34foJtamEdP6ssXVa4pZ8MpfXstH_RdkR9udimCFtlDTr6NQRITUqgcaXI8dqEd1gsFvUkLecn4tME26Ezv5aSU8CYzWBqNPPLqhtyyFcf3rSjg7xu69rcw9TarPjD1bFCILFMDbaRR7bFkcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه از سر رفع تکلیف؛ بلکه کاملا اصولی و روی خط استراتژیِ از قبل تعریف شده!
هم‌زمان با شروع بیست و سومین دوره‌ی جام‌جهانی فوتبال، فیلیمو برای دومین بار لوگوی خود را بر اساس کی‌ویژوال‌های مرتبط با جام، به‌صورت داینامیک تغییر داد.
اوایل دی ماه ۱۴۰۴ بود که در بیانیه‌ی رسمی فیلیمو اعلام شد، هویت بصری برند جدید، به‌خصوص لوگوی فیلیمو به‌صورت داینامیک خواهد بود و برخلاف بسیاری از فعالیت‌های مارکتینگی برندهای ایرانی که اکثرا از سر رفع تکلیف وارد فعالیت در این نوع حوزه‌ها می‌شوند، فیلیمو گام جدی دیگری برای پیشگام‌شدن در این حوزه‌ از فعالیت‌ها درمیان برندهای ایرانی برداشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/661592" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFDsLEs2dn-cDy1vojsT3fZSFaos9LlaTzUc9MIv3vOo3qJgdBm2m6lyu-sLpWnfjHgkmo4wYPTFglZTaQi4_RjzL2nI7ijav1gWtwLke8Oo88fTZSYmTjM-ygeTNoa8WXKoNJifuqha6gFYVtYrC16tRnq6sXJ9MSIq-PfaDtOBDb9fT3515udVJ1imzHqfQ2UQiUJmv4gJXHV0gfTb9u1OeiNsTzsWv-vfFdNlr3KV3IQp5ibFwPt6X9E2xKEyIku7OLWl-L8IAU1fYhwS60EmvtFtGYHNCGmo-fCFWgULhgukJFMUlVRqpo8bcL1wTSjvSunZeDGWhmGX94o0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC9WipnDGmETtneEnCqymdXzQmiAdhwVSmRVviCD57EemGJooL2b0TTYOWnYSAkA572LD9KsuF3glPIG-l7M8M7HzoMMmtDHewDpY_XKyd1xh5iWbIlir4k7OAw4GJvhDYi4--_N6cInZQHzNa3IBleir0pPm2o39PrqESbDIy3ED6WbfYB4oOaBPBd0V5oI0e6Keu-r_xsXsAlghRdVu7xanDzpR0SBy5YjhiruTAzxAFkZ-mr-sSNFUZc8_4LREFHuz-grt5WZDYiVez2W7823uTcRFgg8wn0ikram9oITsJhSJ7DS_PDMwJ2tvS35fa1DD-J7a7IK2V7yYoBLpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر دیدنی از زائر کوچک رواق کشوردوست در کنار تصویر نوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/661590" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e650d65.mp4?token=u0ZlIH76pEIyVTrypsGbnq8hHy1Hn6Prj9rlZ4ZBO8AIBuZP_wNwahyQCh1VeFTvZc0aBJC6qzToIAhPZcFowuEqz1a2gtnPPBxsNPUEEykh76Ja85VBPH4UKANZMAvlNGVAlESQYB8LEQCxkZgGeDqMKzwNFIfaKHQ2VtX3iTB1oK7Bh07qV2p7kHjVR2Cg38FdTxKPaSw8RYLnBSHu6EFAtaqTl6E7gs9v3D_ItuO6ZH-MqruRB5_p0f-N6_y7gUSPopgPH0HI256-R8M04ZzWB7adzoTyfaR6yJ7QFfR3qfMuttkI-lzMfy8vYUI7CK1H3qx4Z4rxRWECdv8h9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e650d65.mp4?token=u0ZlIH76pEIyVTrypsGbnq8hHy1Hn6Prj9rlZ4ZBO8AIBuZP_wNwahyQCh1VeFTvZc0aBJC6qzToIAhPZcFowuEqz1a2gtnPPBxsNPUEEykh76Ja85VBPH4UKANZMAvlNGVAlESQYB8LEQCxkZgGeDqMKzwNFIfaKHQ2VtX3iTB1oK7Bh07qV2p7kHjVR2Cg38FdTxKPaSw8RYLnBSHu6EFAtaqTl6E7gs9v3D_ItuO6ZH-MqruRB5_p0f-N6_y7gUSPopgPH0HI256-R8M04ZzWB7adzoTyfaR6yJ7QFfR3qfMuttkI-lzMfy8vYUI7CK1H3qx4Z4rxRWECdv8h9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: حمله موشکی هدفمند و متمرکز در جنگ ۱۲ روزه دشمن را وادار به درخواست آتش‌بس کرد/ آتش‌بس های دروغین هیچ ارزشی ندارد و مقاومت، آزادی عمل دشمن را نمی‌پذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/661589" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3943689543.mp4?token=NlVFrLI_8aXYQ9LEpCMgEvjkAlBBfZDS8EMor_sDlWP4K2Ww2xPJO1ZYq3RHveKqWbFrk_6xx6KjUXI4GnrBJ_Dj9BpuNvcFduez0YorvsCN5XvjrWcsvsJzQwLKPUVIRZsApOnNKZ1ECpJzY2zLB7QOpITIs6FyLTjT02UZTMDWBpiVzvqvV9yYM-owKNsoZpc7ToFfKhHy4yDUFFwNTHc2KKR7vJYrS-PKN3ldVMMK06kNzihV5ls99SA4vFdKOmFX61We49EN75-KG-uXYv0OfSs8E3knQ7m0FkS5Xg_cBEkaRnEvLp4ffsFK1YsR8Oewz04g24t7ew8bo_Xrug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3943689543.mp4?token=NlVFrLI_8aXYQ9LEpCMgEvjkAlBBfZDS8EMor_sDlWP4K2Ww2xPJO1ZYq3RHveKqWbFrk_6xx6KjUXI4GnrBJ_Dj9BpuNvcFduez0YorvsCN5XvjrWcsvsJzQwLKPUVIRZsApOnNKZ1ECpJzY2zLB7QOpITIs6FyLTjT02UZTMDWBpiVzvqvV9yYM-owKNsoZpc7ToFfKhHy4yDUFFwNTHc2KKR7vJYrS-PKN3ldVMMK06kNzihV5ls99SA4vFdKOmFX61We49EN75-KG-uXYv0OfSs8E3knQ7m0FkS5Xg_cBEkaRnEvLp4ffsFK1YsR8Oewz04g24t7ew8bo_Xrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی رژیم‌صهیونسیتی متوقف شده است/ دشمن قصد دارد دستاوردهای حاج‌قاسم و حسن‌نصرالله را در لبنان بگیرد و کسی به او شلیکی نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/661588" target="_blank">📅 23:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بدرقه ملی‌پوشان در مسیر سفر به لس آنجلس برای بازی مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/661587" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تعطیلی اقامتگاه مجلل محل برگزاری مذاکرات ایران و آمریکا
سی‌بی‌اس:
🔹
اقامتگاه بورگن‌استوک در سوئیس، مکانی‌ که مذاکرات  ایران و آمریکا روز یکشنبه برگزار می‌شود، تا سه‌شنبه به روی عموم بسته خواهد ماند.
🔹
این اقامتگاه مجلل مشرف به دریاچه لوسرن و کوه‌های آلپ سوئیس از ۱۷ ژوئن (چهارشنبه ۲۷ خرداد) تعطیل بوده است و قرار است از ظهر چهارشنبه فعالیت عادی خود را از سر بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/661586" target="_blank">📅 23:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/661585" target="_blank">📅 23:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927b09cb39.mp4?token=qS0neilvE4ReZBTGyfvN6Kxie4LANlV2fPEzGsynGvaAaYC2ot1cRbL9JewMhaXSfxNs7r3D8i0N2wcM3QXFUH1V4pj2J03Ef3bJYQW_PrV4rKpA4OouZWwdLYh0FvC_BeqUiZN83fr9edSqQZpZH-4-LRgW_Dqn4wgVMia7wluVawkGfF4vx8xNjN7AHl3X_w6F_l5WblvEq2ReAlHFygmJduptGMb4yRxeaNG_KDvwBIRmMY2W6ZeidJ5uicctQUCKezIllOxqjUV-gYVgCA3jZ0-4XH6TqcGmbHCBqIQqDtZ3BVHq51Ij1w9E7Q43FsY_y-Bp3RLNE4D5Ysj0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927b09cb39.mp4?token=qS0neilvE4ReZBTGyfvN6Kxie4LANlV2fPEzGsynGvaAaYC2ot1cRbL9JewMhaXSfxNs7r3D8i0N2wcM3QXFUH1V4pj2J03Ef3bJYQW_PrV4rKpA4OouZWwdLYh0FvC_BeqUiZN83fr9edSqQZpZH-4-LRgW_Dqn4wgVMia7wluVawkGfF4vx8xNjN7AHl3X_w6F_l5WblvEq2ReAlHFygmJduptGMb4yRxeaNG_KDvwBIRmMY2W6ZeidJ5uicctQUCKezIllOxqjUV-gYVgCA3jZ0-4XH6TqcGmbHCBqIQqDtZ3BVHq51Ij1w9E7Q43FsY_y-Bp3RLNE4D5Ysj0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: رژیم‌صهیونسیتی پس از آغاز تفاهم میان ایران و امریکا، بیش از ۳۰۰ بمباران در لبنان انجام داده است/آمار اولیه ۲۰۰ شهید و زخمی در این دو روز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/661584" target="_blank">📅 23:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: تا امروز که نزدیک چهار ماه از جنگ می‌گذرد، هنوز یک کیلوگرم هم از نهاده‌های دامی و ذخایر استفاده نکرده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661583" target="_blank">📅 23:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40a0a59d3.mp4?token=cWEsPThsZwySigyv3AY6mlY-pMeYzHa93QpXAOrYYEc1ptFHOUJetzTi27gYCexCAbQ7DPt5D4RshbGXSaMo5vqBN1BgGaLaTDD1kItAK51TWAK0Ez-uv5ZsnWbQjwT-UXvdjz95nmEFvfrhA-LMkACxRxKwc9N4h2Cn503C8pEVEHtKJJIvmqdoTcm1PsBDXutnKRfVU65-SA__-3x6l-OF40v7XLKkZkj-YEvCrkDJnYe4ntYgUGnHxg4RF7NnHPW2ZEeaBZooe2ruVoDH1dYX4OzUmIlEj4RWGS5jufke5CDMAJqpjY70DInPfEGrrUj0fKDkRxM9XGrH-I3o5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40a0a59d3.mp4?token=cWEsPThsZwySigyv3AY6mlY-pMeYzHa93QpXAOrYYEc1ptFHOUJetzTi27gYCexCAbQ7DPt5D4RshbGXSaMo5vqBN1BgGaLaTDD1kItAK51TWAK0Ez-uv5ZsnWbQjwT-UXvdjz95nmEFvfrhA-LMkACxRxKwc9N4h2Cn503C8pEVEHtKJJIvmqdoTcm1PsBDXutnKRfVU65-SA__-3x6l-OF40v7XLKkZkj-YEvCrkDJnYe4ntYgUGnHxg4RF7NnHPW2ZEeaBZooe2ruVoDH1dYX4OzUmIlEj4RWGS5jufke5CDMAJqpjY70DInPfEGrrUj0fKDkRxM9XGrH-I3o5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات تند سناتور آمریکایی علیه ترامپ و جنگ با ایران
سناتور جان آساف درباره جنگ ایران:
🔹
این یک فاجعه برای سیاست خارجی آمریکا، برای اقتصاد آمریکا، برای امنیت ملی آمریکا و برای ریاست‌جمهوری ترامپ است.
🔹
منظورم این است که، مردم عزیز، یادتان باشد که در روز اول این جنگ، دونالد ترامپ به ما اطمینان داد که اوضاع از برنامه جلوتر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661582" target="_blank">📅 23:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قلعه‌نویی: در جام جهانی جا برای اشتباه نیست
🔹
می‌خواهیم کاری کنیم که ستاره‌های قبلی نکردند
🔹
بازیکنان ما مصمم هستند که به دور بعد صعود کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/661581" target="_blank">📅 23:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
چرا کالاهای اساسی گران شد؟
وزیر کشاورزی:
🔹
یکی از علت‌های گرانی، اصلاح ارز ترجیحی است.
🔹
موضوع دیگر شرایط جنگی است که در جهان باعث افزایش قیمت حمل‌ونقل و بسته‌بندی شده.
🔹
افزایش ۶۰ درصدی حقوق کارگران نیز علت دیگر افزایش قیمت کالاهاست.
🔹
قیمت حمل‌ونقل رانندگان داخلی نیز ۹۰ درصد افزایش یافته است.
🔹
مالیات بر ارزش افزودهٔ کالاهای اساسی از امسال ۱۱ درصد شده است.
🔹
حقوق گمرکی کالاهای اساسی هم قبلا یک درصد بود اما امسال ۵ درصد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661580" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
🔹
جی. دی. ونس، معاون رئیس جمهور آمریکا، گفت که مطمئن است واشنگتن می‌تواند آتش‌بس را حفظ کند
🔹
او تأکید کرد آنچه دونالد ترامپ، رئیس جمهور آمریکا، برخلاف برخی از احزاب در دولت اسرائیل، گفت این است که واشنگتن به مذاکرات فرصتی خواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661579" target="_blank">📅 23:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50b28ca66.mp4?token=ieQwGCY2H-L1DzcWwg6AfqLhIEIg-GsDUXWslGSvGUy4nXS9IGw9cdXi5xG-Y5NtWaEx0bF8MyOPZ9z5CKzj5bmA4Rr_agLVm-TjPQqcnYD4wZDHe2n9m9UhceM12oO7yMysxhWWdk5pc7XC2FC11mED6ZbVaDHmeVyhVLfSFcYd3H5F8ihnWQUAp7KOVtb0qscm0m8OvQgh_BQ2M49UlZY6moukseSklTHbqQgkuIa_DOSUohEnJfTk7bNnMU7Lybvfsw2RZCrnj6zGXb-UdfXCZBL8k0ZS9cQaiYRBgyArPar6P7t16x4gIrHP6OXROIvgKSVox1GiMMb2z-BoBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50b28ca66.mp4?token=ieQwGCY2H-L1DzcWwg6AfqLhIEIg-GsDUXWslGSvGUy4nXS9IGw9cdXi5xG-Y5NtWaEx0bF8MyOPZ9z5CKzj5bmA4Rr_agLVm-TjPQqcnYD4wZDHe2n9m9UhceM12oO7yMysxhWWdk5pc7XC2FC11mED6ZbVaDHmeVyhVLfSFcYd3H5F8ihnWQUAp7KOVtb0qscm0m8OvQgh_BQ2M49UlZY6moukseSklTHbqQgkuIa_DOSUohEnJfTk7bNnMU7Lybvfsw2RZCrnj6zGXb-UdfXCZBL8k0ZS9cQaiYRBgyArPar6P7t16x4gIrHP6OXROIvgKSVox1GiMMb2z-BoBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی از داخل خودرو به جمعیت در شیکاگوی آمریکا
🔹
پلیس شیکاگو اعلام کرد که دستکم ۱۲ نفر در یکی از خیابان‌های شیکاگو، پرجمعیت‌ترین شهر ایالت ایلینوی  در آمریکا پس از توقف یک خودروی شاسی بلند و تیراندازی ۲ نفر داخل آن زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/661578" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حزب‌الله ادعای صهیونیست‌ها را تکذیب کرد
‌
الجزیره:
🔹
روابط عمومی حزب‌الله اعلام کرد ادعای اسرائیل مبنی بر محاصره مجاهدان مقاومت در بلندی‌های علی الطاهر صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/661577" target="_blank">📅 23:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071d4a05d0.mp4?token=slgbOOqSFglVJzvKL5uKdjt-rDYk0FMrDpAnaLOp8ax-sd-jWYBCwV5JlXYusAvRKvaaDzbEgnKBJzuvIKwRaXZe83Rz4BwZDf23KyR35q3b8QB2eYOfSC24f49GWGQ2_fCFg3vG-6nlLVvp09VTX4YjcqFKkmZWziw6mfqkoVb4xrq8Weqcf1aQ5QKfM92FJTwMIvw8YHP2utJKQosj1otUa1-5RttXR5hAA_38nL63d9ChkY3b4Zqc9z2eGPbr4-S9MxJ1jbYJoa-vR1k7Q1VfgYYXX8BjkfVABurp315AZBzuHmkuKOWCYyhmKs67nbiXlFWQgpuNgwA6TbAvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071d4a05d0.mp4?token=slgbOOqSFglVJzvKL5uKdjt-rDYk0FMrDpAnaLOp8ax-sd-jWYBCwV5JlXYusAvRKvaaDzbEgnKBJzuvIKwRaXZe83Rz4BwZDf23KyR35q3b8QB2eYOfSC24f49GWGQ2_fCFg3vG-6nlLVvp09VTX4YjcqFKkmZWziw6mfqkoVb4xrq8Weqcf1aQ5QKfM92FJTwMIvw8YHP2utJKQosj1otUa1-5RttXR5hAA_38nL63d9ChkY3b4Zqc9z2eGPbr4-S9MxJ1jbYJoa-vR1k7Q1VfgYYXX8BjkfVABurp315AZBzuHmkuKOWCYyhmKs67nbiXlFWQgpuNgwA6TbAvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق ایران و آمریکا به معنای پایان تلاش برای تغییر رژیم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/661576" target="_blank">📅 23:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le9ZJsYs-bUCLOyAY4caiaLL_7kui_8Pcx3vQj_Oml0XrReG_7oJuSHUqeSjzo3fOSHgfg_U2sb62XyHQ6Zd84OjjCgJ5PBB5XBcFe8ppxs1n18jwtWlVNQTFLc78jgT14SUZsqFr9RAfvHf3yZx4weZVwKft53wIlFCIkQFx8Vhysx2gW1YAh1lirCyRmgbwYsMWAEWbfYpMSUCBK6g82ybYxGWQNMjdjCOh07TjAEtRBeIV-C6sN4ZSa95VCWfam3Qya7qvrQHOFLwg0x0_vHiV7Bo0CuzvGrQF9Kwf31mI4wtaRJx2viPYDNxEveMVfRETpR6D1AfRzizbgmdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر توافق نشود، آمریکا در تنگه هرمز عوارض خواهد گرفت
دونالد ترامپ:
🔹
در طول دوره آتش‌بس به مدت ۶۰ روز، هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از انقضای دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه در صورت عدم تکمیل توافق، توسط ایالات متحده آمریکا و برای ایالات متحده، به دلیل خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه داده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/661575" target="_blank">📅 23:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a195dc3a1f.mp4?token=d0cIllN93GpHTlUXaOSM_1FDdq_s8gf91kTDEnhFq2ZBd08Pzw702zGrYpp_D6Zs9e12DQtcrVGu8cbHROQcwiYwYBHmgbW_KxBEMsvnitnfNK0e-hSc7iqH-mR2MA4YheSNonxMrglN3PoAlBcmBEwLUgRtYwo7LUI1aO3_HqBHZlXK6vm8YlMHvOU_T-sYCZoaTgO_xU37OyahDIQCjBrFTcqtDjhlduYBM9Xk2TdU_wN8syjyOIs5If9AmSEocBi_68HfPr1Uyc3vP9gai41fhRQ3UQ5-jk-UYSMpHBrwnifp-f_LIcwUOsOFGx_36vOoWjoURa60eXBUimt0MHE0xeybY8skVx1PbpF1bxb43nIhE8ivYV9tVgCG7q4Ylrb9bFMNuvNO_RgFuRnFieU2nUaqk_ckZWzW0XS2l8emDJ0XJgHtEKl7_KplF60HQ5_5Y3AO9mBzSBGVsoOppR-wjSttebeWztr-8hTS9DmiZ1KrSBvGYXhJzscZvlYGMgHyyMvcvkVxAw7-6BSAqAldzwn3H8gAtwDunC8fcWc8KR-z5c97IGbatzdESLU_D70h470Yn6izdYhNfMlXOYL3zQljhMD-DzNFtkNVaJx5sVUySq9Y6l1anJain--VxnQLVuO_6sfnFAvc6U2FnzujSLu_gJrxmxWbziulD44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a195dc3a1f.mp4?token=d0cIllN93GpHTlUXaOSM_1FDdq_s8gf91kTDEnhFq2ZBd08Pzw702zGrYpp_D6Zs9e12DQtcrVGu8cbHROQcwiYwYBHmgbW_KxBEMsvnitnfNK0e-hSc7iqH-mR2MA4YheSNonxMrglN3PoAlBcmBEwLUgRtYwo7LUI1aO3_HqBHZlXK6vm8YlMHvOU_T-sYCZoaTgO_xU37OyahDIQCjBrFTcqtDjhlduYBM9Xk2TdU_wN8syjyOIs5If9AmSEocBi_68HfPr1Uyc3vP9gai41fhRQ3UQ5-jk-UYSMpHBrwnifp-f_LIcwUOsOFGx_36vOoWjoURa60eXBUimt0MHE0xeybY8skVx1PbpF1bxb43nIhE8ivYV9tVgCG7q4Ylrb9bFMNuvNO_RgFuRnFieU2nUaqk_ckZWzW0XS2l8emDJ0XJgHtEKl7_KplF60HQ5_5Y3AO9mBzSBGVsoOppR-wjSttebeWztr-8hTS9DmiZ1KrSBvGYXhJzscZvlYGMgHyyMvcvkVxAw7-6BSAqAldzwn3H8gAtwDunC8fcWc8KR-z5c97IGbatzdESLU_D70h470Yn6izdYhNfMlXOYL3zQljhMD-DzNFtkNVaJx5sVUySq9Y6l1anJain--VxnQLVuO_6sfnFAvc6U2FnzujSLu_gJrxmxWbziulD44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از بستن تنگه هرمز؛ چرا اسرائیل عملیات خود در لبنان را تعلیق کرد؟
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
معادله جدیدی در منطقه شکل گرفته است، ایران در جنگ و میدان، نظم جدیدی را به منطقه تحمیل کرده؛ نظمی که نشان می‌دهد جنگ باید در همه جبهه‌ها متوقف شود، به‌ویژه در لبنان.
🔹
با این حال، هنوز برای قضاوت نهایی زود است و باید منتظر ماند تا پس از مذاکرات مشخص شود چه اتفاقی خواهد افتاد. آنچه روشن است این است که موقعیت ایران نسبت به گذشته تغییر کرده و نمی‌توان نقش و اعتبار تهران را در معادلات جدید منطقه نادیده گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/661574" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b1efe9c5.mp4?token=IO8NlyycY6GJVK9l8PhZ1OgarEskf1MWN_dKMosJbkcIv_UnWxsrNG5pG40-9wYzVQLBpLnVyIMFlBZgY4kNCxcAT1n1cxobO5PWD5_8fPf51577xySiAcsmzxtiYfsvd-DCxkLvZhX-l9O20AxnG0NHUXkrKX3bG6lAlU6Rn5D3y0bE-i0uwMdKIJ-4wQql6AFzjgHg3JdmV3aNP77lm_tqWhXw3JxoM27P0m49WGveRb4oCkHBnb83xlYJqr7vegai1i2931XJIvIvkzWZy6gIi2JXMgOPIuVRZ2_pmHm25Ra8OPRNSMZMyJLFaxbTBymokd4tCHUpy9FtsdiqLkoba9D_WMZk85j69ZvoRjrNvA7-XnmoOQwDhqCv_HSBGuRRctKrFGMpezYojP5JkdkadlK8JnaY0l31zMZx9qSMXYIrCtDXSuXoGpAq8a63ec6S2ieQdgOX8cZgjP3tuhaegpfX2I8wrEO4T_n6pW6UqR_x4rv4VSr23zOq6eiZsk2sWQMbCyyUOUFV7KHZA7VT4JalNrCpH5KYez5U7mzt-IT-hcOVU2h5GMWs28G_bThiZtBDGhAmcw3RGOZ8bVpmlPAkDooujLKNekqF-1U2mKwK_uUl3-u7xXoQFr7J3JbFwYy1KtEit9I9Vuv1YOBgyJhZTbDSLqNGvmWBMKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b1efe9c5.mp4?token=IO8NlyycY6GJVK9l8PhZ1OgarEskf1MWN_dKMosJbkcIv_UnWxsrNG5pG40-9wYzVQLBpLnVyIMFlBZgY4kNCxcAT1n1cxobO5PWD5_8fPf51577xySiAcsmzxtiYfsvd-DCxkLvZhX-l9O20AxnG0NHUXkrKX3bG6lAlU6Rn5D3y0bE-i0uwMdKIJ-4wQql6AFzjgHg3JdmV3aNP77lm_tqWhXw3JxoM27P0m49WGveRb4oCkHBnb83xlYJqr7vegai1i2931XJIvIvkzWZy6gIi2JXMgOPIuVRZ2_pmHm25Ra8OPRNSMZMyJLFaxbTBymokd4tCHUpy9FtsdiqLkoba9D_WMZk85j69ZvoRjrNvA7-XnmoOQwDhqCv_HSBGuRRctKrFGMpezYojP5JkdkadlK8JnaY0l31zMZx9qSMXYIrCtDXSuXoGpAq8a63ec6S2ieQdgOX8cZgjP3tuhaegpfX2I8wrEO4T_n6pW6UqR_x4rv4VSr23zOq6eiZsk2sWQMbCyyUOUFV7KHZA7VT4JalNrCpH5KYez5U7mzt-IT-hcOVU2h5GMWs28G_bThiZtBDGhAmcw3RGOZ8bVpmlPAkDooujLKNekqF-1U2mKwK_uUl3-u7xXoQFr7J3JbFwYy1KtEit9I9Vuv1YOBgyJhZTbDSLqNGvmWBMKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز از ساحل بندر سیریک
🔹
روایت خبرنگار خبرفوری از قلب تحولات جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/661573" target="_blank">📅 22:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
تنگه هرمز مجددا بسته شد
👇
khabarfoori.com/fa/tiny/news-3224511
🔹
ویتکاف و کوشنر در سوئیس، عراقچی و قالیباف در راه؟ مذاکرات از سر گرفته می شود
👇
khabarfoori.com/fa/tiny/news-3224325
🔹
بهترین پاسخ ایران به حمله بزرگ اسرائیل به لبنان/ این اقدام تهران ترامپ را به وحشت می اندازد
👇
khabarfoori.com/fa/tiny/news-3224502
🔹
لحظه قتل پسر 14 ساله ارومیه ای توسط یک مرد جلوی چشم مردم
👇
khabarfoori.com/fa/tiny/news-3224484
🔹
پزشکیان تهدید به قتل شد
👇
khabarfoori.com/fa/tiny/news-3224302
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/661572" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e34471e1.mp4?token=RgYwoYuW1cN4mckwL8qThhlR0TZgPAGbr24TSjcD215184QGxkivQXUphgVsF-2DfjjBEYj4cPaNPYuhvV8iJ7YPlq31ud0E8M6DhL1q1BgN_CoV_xP9NqAgFdidVijI1FzMipm6b2_kHIVE6EqBCTcjKltLQIxKVLSD_m_Eys-uidPVZbZtaiJtvTzqbWqLXQzHxnE6jLEB-mwqi20j0soIIDMO_oj01PEZsSPnRNQ8rLoE2Tn-bqNkyG8ornBUV5j7uf4Zj2f3URN7D99IT7Ipj84xkzcTDKlXFHY1GuRoo66OFjhFDmzAUtkdqdrtL6yahf1wG_CFzhpttZg96g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e34471e1.mp4?token=RgYwoYuW1cN4mckwL8qThhlR0TZgPAGbr24TSjcD215184QGxkivQXUphgVsF-2DfjjBEYj4cPaNPYuhvV8iJ7YPlq31ud0E8M6DhL1q1BgN_CoV_xP9NqAgFdidVijI1FzMipm6b2_kHIVE6EqBCTcjKltLQIxKVLSD_m_Eys-uidPVZbZtaiJtvTzqbWqLXQzHxnE6jLEB-mwqi20j0soIIDMO_oj01PEZsSPnRNQ8rLoE2Tn-bqNkyG8ornBUV5j7uf4Zj2f3URN7D99IT7Ipj84xkzcTDKlXFHY1GuRoo66OFjhFDmzAUtkdqdrtL6yahf1wG_CFzhpttZg96g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشاورزی: افزایش مبلغ کالابرگ همچنان درحال بررسی است و اگر به نتیجه برسیم دولت اعلام می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/661571" target="_blank">📅 22:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYbz70nUZrxK5sOaPTOYSUjlWqMRLguXSu8gPatuH7E_oqhm64lUmOqBkbsdRZTZBp680rtOQatqLBEZdY4E-XKtak250t9wCM_aUqwOTwGsPdTfjUWvEK6i2NH2_0ywcCdS4fwSuWfWv5iJb-lqEDiwvKIBRIhbkHHp1lVv8EwvBrW04We-UAQ9zhIMNSknSDdmLcKtB_alKWKeA7zd5aeIAeW8j7b11lQx7whP_Klx0xozlMG9-xHT9Hum0r2r67_8Ce41vSjbxYGKswDdKhOA_gMFmliaRw9cq8rVeFaEKL_ZW_ZuXo2iVLTYlK5a_RbnV05r9ATsA4nyHLEoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هنرِ هجرت؛ چرا نباید اسیرِ مرزهایِ جغرافیایی شد؟
🔹
امام علی(ع) می‌فرماید: بهترین مکان، شهری است که بستر آرامش و پیشرفت تو را فراهم کند. اگرچه حب وطن ارزشمند است، اما نباید به بهای عقب‌ماندگی و ذلت باشد. تعصبِ کور منطقی نیست؛ اگر وطن جایی برای رشد ندارد،…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/661570" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1qKtx7EwzkD644soe1VsEINsurXF9qNJXj9whdZqcq-JcrCHMMVitDkbhWbxGOL8IlZoX-Wlc1wblQimUuRDWk_8_Wnax340pOOxyO4x2jIrVFIxt1BbVY0tJcrwktEIAcVPT47GBfpWusdi-hTW2ahNYwibOWPFGDdMn0JgiERif78xHSSRtRnIWh_SXWBKfcZJO29TPU0_ZK1CZwK7uwzqYvxjUaidp58fg7fsN6pSJE1OWcH_cbtVLenKMKfqvqMlZa9eGoxfJ-0WdEJY77bOKeuNKHAqmjEjaAyyWOLJbN2DnwoHstcd9NCHEyhlut5RXppz2VlNH85tJdePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوکو غایب بزرگ مقابل ایران
🔹
به نقل از DAZN، جرمی دوکو به دلیل عفونت دستگاه تنفسی بازی مقابل ایران را از دست خواهد داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/661569" target="_blank">📅 22:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXmDItinVLk7Uhucd7tyLS3zgvMPyJWH4q7sjFxEQSLPKU-gClJWk3V6CHExZKS5qjjy3HZrie2SIMzRwmt1havvE-nHnY4EpWlpCxOcP6JEcR2Buzl7Rg7hLhIHd2y61umQaKQdV8hTEKZAtfOPeQxrp3LtyXJEIYx1Rb7P44ou2Pw1750GBGfGnI8UYyXxoFJBUn7t71NQPv_2RrgEn09I7o6iaG-w8TYmmK4nXb6E7euZ5z3kx6EqdAGo83iLd5OMOYIRushuyp1bo_X8saR4XBqlJ9ATlQbL48KmARJxTF6E6yc8ls9KfommZgUvAfUaklsOSw9dvtt8orNILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مروری بر وضعیت فعلی و نحوه شکل‌گیری جدول مسابقات مرحله حذفی جام جهانی فوتبال فیفا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/661568" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2tOTNe9MwxK0-_8PiRjq7V_AWqvavrshNvOlOINB5P9rs07Fr1NoTzdTmEibbnGZHqRcHNSbVsCJycgLltJ0yQZB3WYRfvOhS2iMDV82CZD1L6a6Nl6bFjatuppNvrkhYIxXOjfa5cvIuVrWHzEyDJcPiNewB75y55urjVorkH5_gAP-iFpBa3j60G3L2oNhTnUCjiRGvFOgB0vAacnEWgmnFqIKIOHfrrFNffzyt_plSCVAO-NZNntaRts8fR4v5mILeP8YMx_eFmgUH3MPMErxJXjKbVsGIXM6m_jrNmcjTDK1WJf-TnZ0SH0l0pM6FXuToCWTJ4VojTMSBbobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8nFFt7pl2jrvGiIQoa1zT3tpOGESWLHJG-ojNHOZxM8H-Txo3mR22hBxAYoO-BPiLsNgroVq0y083Of5MaIWBo5jGEyOLaJXuj6VuYOe0khn_sSIccvyTcYyRvQr1bYR75IydqzENbKuQtifTNO6-c8Cj1plo6DvUqWFYVOlVs_-1nbXROHfdN3KD7aS0hXdV8FChM6vahdBtdtjCocvwunfi0l8LcoWgJaG4SA2WGxBUB16yeaBZRm8xDOBh5dNS2fKPNP2M_-gqLLc1wkjnLHRxFTe2p6YhT3mA3cVgcNgG5qHows4a2c19bLQqfem_IkZA61HXb1iHqqrf08zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZvWOxehC-tXIt5r-zDwCwV1cYp3ees37-CDkZW-7ei0VjUjaw7B7GCDmTWBf3LOGW2-MuB2UYOjyoCqX9ZPj9HQ_yli6iAUklNosYEzw93hwF3E3nAU0dT6HcSMwhZ8bC_7z6QFnI7s1Z_dYC70aQOZyG7FTrn6C4AKFZ7OyXe6kB3WAnCMc5NKvB149TSaq5ybkHqpFnRCNRCSfGi-eGO7OJHignM6r9gInrTrDzuKHT7BmtIcayeN7xoFsHGktP7SUZmufvPFeR4S01Q4PITD6LruM9C8suLqkOPyocLDvDysxAIN3ALMQhGg56fxhu4b1kZwvU_esrxk6QD-zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چندین حادثه آتش‌سوزی با منشأ اختلالات صنعتی در شهرک بت عین رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/661565" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غوغای دسته عزاداری نوجوانان در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/661564" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم هلند به سوئد توسط کریسنسیو سومرویل در دقیقه ۸۹
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/661563" target="_blank">📅 22:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdoizAPKzkjZUmptGiUgWJuBMptVcszvNdNrNHl6DU8GNm7ieeyz-A1Qzs7MyfVGCAehScCAhffSxwAosnr9MexCso7PpSShPxcxHrnDNZNG-he0FEneg5b9SFXlRd7yG9h7qhaLEISnBKq8sG8HvPa5irr0z0BaNe646S10PDTjwrTshSjo6xVR5baEHUXYvcojj-lZLuttJooSVJWMR8SmJ2IWC9L5ePyoDk1PLRtHUC49rhOr3joPl7IvYnBhFd3Qguk2MAIKxT-OUmoF5rT-VE2ZhzzTR-G3cDXkumVOYHWRDid7S8AJIVUIFhYwPLINJ_ckR9J5j0gzImHJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب شب ششم محرم حضرت قاسم بن الحسن (ع)
🥀
این بار طوفانی به سوی دشت عازم بود
سهم حسن از کربلا غوغای قاسم بود
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/661557" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpFOWlt1W7PKPBAN1-2VrklM3qa3GzICJ6vDdsIrbsf1g0VpzxA0VybBVqPMAtqjgBBXwRghl5e5T8P09g6f01mjHrgsAuvuC3U2D4_5kir_PbNiarSGc-oI9DamkWRLTXPQKoBxVDEe1cdaRFDF-6GyaO0ie9IMx3cWQ0Hp47NmCZ3UstyuedS01wklG7eemmvxpzOog-UzdR23qis9g6VosL1XrDzGVvTKvJMY8P1HDBzm1Bv5V7GzMhOsbiNXIWOm1kBv0g83J9tWreM9GcZtBdlG7FXORqAfS2cWjDadBr4il25Aag1q-mWb2f-dPhcI-Sz0LC0yN2hCQXCKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNXfnfbJvQIgR3CqQZ5diiBSGZr05JY-jwoOhmZrMufFCAGGPbelkJ9UBO83Y4tFsRzg09UwUk7y2bg3cT6eAk2ThFltIQEeB1XWYhKrpEqlBXAUch_dudHudQCzZ66hsjD6jxEAjhP-5hzKDcX6XT8oewnyFNcviBu-7TsWR_NDDgNnp2j6Jxq_VK4nfFtj98S-No-yFGzjNGnpvm3Ivo5WbHzSX_vSQyHIosu3MBu5iwxo-_5T8MCYVV-N_WQjtsyVSCpGdM-Cs898Sb5f-UfUP7LZvnf-SRDvAmq0X9HzBX8eKW1RAi2ilLV4oLAJbBA2VKWgXdWpzqux2TIf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ms8zg81FoHIYM1DI1I_3MAG6TBRpV6gzUsXfSuO9hC5ZRh6GpT3-Ry3n_ilJRlZxF4qVVZJipuObFE9RkVOewBoFMXbQAQKFVcrvOJa_vyNgK92sFxMOn-a-BsCo-S51cZDXcHZf-oRZcShC_XA1Qg-ZXqMjcXE9Dqz2Wwc4EZFqaF4P-ZEsGNQQ2dynleO0z_BcwCpCBBt7HLzi8GXnf8sdux8443KF7v0WnScM0iVMumxePPyGHGAkxokbw-2QkDXcefY6Iy5WTRaf8Y3DnizN8GEzF379GmR_bK1yv4PjHeNsoHi4PsesNfNdx-KgDixhjjPwyGoP3TXI9_yyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLttIcjaLLuU-tCKQ32_1ueVeU2rTjL-QiMJuJiGLTE-Yn8lsNBq3SIepvh9JvT1gBo2Le96s21W2mu4adCkvJVOyXYkgK9E5_9yRJFY8F18tRAmsCqZYw43l6k7n2BSXeMXDg_0kUgwzlYhgOeTDpodqn2xgh57MqXJecFqD5M5EuCPI-QS_jidV2guxJRkfBTVGPFQOp1NjH-NXPSZlXhNFGqH1eENCyeWg8Wn-okhAjze5haGaRJ62xVSZciHZaUl9FUTHHPGCCfNh-H40XgasBaDuFdBaHd_d2afYTEFPy3faeFFy36laf_dbtvZyvKqJmo36Hc4Dkw7SvukTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDt2QrXZHC0zOl4QeaZkwoEzh3TslpSDgdHnznZohg2iyDrf-ZWQ0wsWAiN1aTixtDVU6CG31ofzbrof2S5C13Pr8K-Z-SM9QIhon267Zs9JINdxc622Zv1zjEPLtVaIZgyhoSXgxafj8oRJYY38DpXaI-9YsF7YfS2kLMy4HDcllg0vzUt6f3NS0KjEtQ9LObCCMvbW58Fp2EaXenZ0iXn_Tbqrhv1dxklqKLLbl5wXezgaucc8BsNLmGYtwZWdSgj6H_g2iw2Mxx9uW85nvjq4zbrkqxW7aXSn7W_h_QBsLG-RZZAkW_rb3rXwVJZ1whLmkRCMRoe9A71KSAzLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUNk5XCy0Uhu6IMbjOi1U6P2AABgW57AgumgwfV7kQmYbiS56tlb9xNJpmEkbcIrC4OK2NBaFfIZVoAw2zgspMyWyVV8dOeBgiaFhSkn9_qH2gPRhJdaY5CEacpPsqBTlkNdbqRirHY2c5LOgg2TYRmi2FH0UAJSZI4iQIFqx4GdGxbfUmQ3MdxsXfnVtya_sNbJUp1e_fbY4rCWGg9vPksK3_-Wxg88tcnb03qnZaegnvOyJWSLNaDDIwP86LeII_O6t8vu8MYnS2UMltMaSY6iea-3gU98644IZIsmBBYMleqQMIdnL3Lc6AKq6q3aQ7rhmxFELDy2wOL0UV8NnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترفندهای کمیابی که طعم غذاتو معرکه میکنه
🍽
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/661551" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم هلند به سوئد توسط خاکپو
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/661550" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
المیادین: هیئت آمریکایی در سوئیس حضور داشت
‌
ادعای المیادین:
🔹
هیئت آمریکایی در سوئیس حضور داشت اما اعلام نکرد.
🔹
جرد کوشنر دو روز است که در زوریخ است و منتظر تصمیم ایران است.
🔹
هیأت آمریکایی پیش از اعلام رفتن ایرانی‌ها برای مذاکره وارد سوئیس شد.
🔹
حضور کوشنر در سوئیس اعلام نشد تا گفته نشود آمریکایی‌ها قبل از تصمیم ایرانی‌ها وارد شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/661549" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روی پاس زیبای ایساک؛ گل اول سوئد به هلند توسط الانگا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/661548" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRpdou9NA7oG8e1pclY3kB1RfFVIsP_0d3wlSkTca0E4oEkZMgkoKvQNlwdZfGL3CdifRcrXWktquRZtyp24PT1OkABJYxcPsXtLczZh8oRBUO7gKaxZth31pym19LejOUQIxylsVAwjHH3jOdAr2qow0SmBsxihltPwZ5yQjG7pdr9vA2tQX7RekaeVOr17sADtzKG8dv4tc7tHeK8ExQTykJnkvRF6XUNuqSQvaREK6T2nz59tcGGG3NSK-E8vSrxs0CMB93E9g_q8jd-zs2f6woH0ZPZvtsvE1j5-IJp84GTklZNtIIG_CXp2XvtaLD60H-GKZ0zh3W-L2mDnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661547" target="_blank">📅 22:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGCzOBNeAUSNIBf581A-4eMFH3Ia_PjHk56zlyB8E5GebGqdXit7wdIMLYA5w-GL5bTCoLY6MsjC_QcWE_ZAlEucRShgiHi3UCbItnniy4k_OoJ4h2WydIryjYIJ9Y9sdq_YLOlZZmZn5odDV6agDx5nkOQHKN85F1G4EYx49a_ALABqcBwoGGDHKPslj7QmSu1aHsMWVvkRqxt1BbQUC4N8WbHLA18svcZtqy1BMzxsR5PE0wid3Aj6VspFqDJOcJ1DxpAwvESgkFK6uUx5jFc9SI3mPwCuXmQKXFICTzEwl4ZVVUHiDeC9Ht_2W-P-Py4Lg_jwSpRFFrgDn09wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرکل برنامه‌های سیاسی صداوسیما: از راه گناه به مقصد نمی‌رسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/661544" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
