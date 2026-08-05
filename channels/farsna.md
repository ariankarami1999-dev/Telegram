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
<img src="https://cdn4.telesco.pe/file/UyDAITSr9Qv56ZURddr-BjvPogKcKhZXeJZcgkpd97TAKpDTjkHb4zz-YJGsbRGM8c2TqKAL5kLjwBJ8Xk2Pz2Kv-i-ag8RfpqDaTkR8b5mFpsSJArVEHxn-4Kpla7QNvT2KMB9hJZ3mwUD9mUh05saMOp10BI7Zl2UU8r3rl2ndXwRKhcqv06urceEwj1eOTDDutzZhx2CVWbNNcCm0E1k_NO20DPpfdKPW1dtKTt9rRo9K2awphsN1Lm-ex8vymxmhRA0TrzQp4ggMA_37DMU5-Sfge2NkaMKU1KQquz21r4w2G7jJC8YPIpMxInwj8-bvHTzMWAjRaJCM-eIOEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-454588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
زخمی‌شدن نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی از زخمی‌شدن چند نظامی صهیونیست در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان صهیونیست با بالگرد به بیمارستان‌ها انتقال یافتند.
@Farsna</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/454588" target="_blank">📅 13:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با رئیس دفتر سیاسی جنبش حماس: ایران از هر تدبیر، ابتکار و تصمیمی که رهبران فلسطینی در روند مذاکرات اتخاذ کنند، حمایت خواهد کرد.
🔹
به‌رغم تجاوزات اخیر رژیم صهیونیستی و آمریکا علیه خاک ایران و شرایط منطقه، مسئلۀ فلسطین همچنان جایگاه محوری خود را در سیاست خارجی ایران حفظ کرده و از نگاه مسئولان، سیاستگذاران و رهبر ایران دور نمانده و همچنان مسئلۀ نخست جهان اسلام به‌شمار می‌رود.
🔹
خلیل الحیه: ایران توانسته معادلات جدیدی در منطقه ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/454587" target="_blank">📅 13:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خادمان اربعین غمگین از اتمام فصل عاشقی
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/454586" target="_blank">📅 13:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa44218d82.mp4?token=HR5Ix6fEozuW2eeZ8e_9d1z4A7laIdHZEonRNnwyol3ZBULZ9YA53x3dUrE-5yF_KG5xO9eEg9gdClOUlw1b4N_q1jBGZoQytBa2hTAVkFojfSnN8CvbrmRXmqI0o0ysAzp-5HOfiitbZjjagNuQtCu_uOoAgYcrK-nTWiSSlV8HlbcWgqSKxZKigkBiVqGSqlcCas_DmyMJp5hZx3-1mJT7_MkmYnPPlEZ-NEb4RqiF1jrqTbEb2uiCRfZ6G8EjYFWDA0h_3gPljlBUOkVHzHdZ53w4nRGOHmSfQG6y7GzIIG0JHGnEjtAUsEzRxaJGzRH87Nc9NJWLPDDYkHQ24UDcJn0-9yUMz-AZ-jjPCNrnf2QjkzQCHvlMZ4zdXNLnSKXavWbBgetm5fWWYTCZeLzch2uDkragfhS30gyLaf_sE_Tv-s9Az3epaR6XSYewW_el3VeHwzGQ88p0SD0rW36OB_jys2VIMLTsGCM24c_0-_EfwN61hAqV2tzWC2_Ym3hTm3wBttekn-ih2yquoQQH_VtGv4QG_TbfE5nlVTiQUIHYd_a50bswz4yuFBLdBeAYNqdosmuD54SiglMw7EUB8f_yNs0YryROGTRIBYZUpQlLuN4gxOStyYAvhBYfL0rmBzAT0HyJd1k3z0WK87qmiPIb79hRqUSgudi7VVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa44218d82.mp4?token=HR5Ix6fEozuW2eeZ8e_9d1z4A7laIdHZEonRNnwyol3ZBULZ9YA53x3dUrE-5yF_KG5xO9eEg9gdClOUlw1b4N_q1jBGZoQytBa2hTAVkFojfSnN8CvbrmRXmqI0o0ysAzp-5HOfiitbZjjagNuQtCu_uOoAgYcrK-nTWiSSlV8HlbcWgqSKxZKigkBiVqGSqlcCas_DmyMJp5hZx3-1mJT7_MkmYnPPlEZ-NEb4RqiF1jrqTbEb2uiCRfZ6G8EjYFWDA0h_3gPljlBUOkVHzHdZ53w4nRGOHmSfQG6y7GzIIG0JHGnEjtAUsEzRxaJGzRH87Nc9NJWLPDDYkHQ24UDcJn0-9yUMz-AZ-jjPCNrnf2QjkzQCHvlMZ4zdXNLnSKXavWbBgetm5fWWYTCZeLzch2uDkragfhS30gyLaf_sE_Tv-s9Az3epaR6XSYewW_el3VeHwzGQ88p0SD0rW36OB_jys2VIMLTsGCM24c_0-_EfwN61hAqV2tzWC2_Ym3hTm3wBttekn-ih2yquoQQH_VtGv4QG_TbfE5nlVTiQUIHYd_a50bswz4yuFBLdBeAYNqdosmuD54SiglMw7EUB8f_yNs0YryROGTRIBYZUpQlLuN4gxOStyYAvhBYfL0rmBzAT0HyJd1k3z0WK87qmiPIb79hRqUSgudi7VVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری عامل تولید کلیپ جعلی اعتراض نوجوانان کشتی‌گیر به اعدام
🔹
این فرد با سوء استفاده از ویدیوی گرفته شده از تمرینات کشتی نوجوانان، بدون اینکه هیچ‌کدام از آنها اطلاعی داشته باشند، به‌عنوان اعتراض به اعدام تروریست‌های آشوب‌های اصفهان منتشر کرده بود.
🔸
پیش‌تر قوه قضائیه برای برخورد با هرگونه انتشار محتوا در خصوص سیاه‌نمایی و هم‌سویی با رسانه‌های دشمن در خصوص اعدام جنایتکاران اغتشاشات هشدار داده داده بود
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/454585" target="_blank">📅 12:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guiTlD9gHWGCgBYmmTqhz1mKksRnCPlzfIzYjl8Mf54oK-9C_vzlIcGloVe2Rnt8-JZG7-kUma2AUll_ez2LqmCghI8CIwUB28QW3pvV-CuTiAZTKsoYcudf9Q5ovDeaE6_NXTcwAts21s4N-4yHGfluzNiX5llXZ9iXS6SfM527IGq345xZpNwfKfTnKDe8baAYZQeltnwZb81z6tkfOJcJL9maKlaRU-y6NqNIj__EqUhZ0rUd08JBjgyham2VtLpNMU28WpSDvXASGcNn40CIHoWx_Gu13pxbIYpuybfChVAyuE7_vguRZU3gZAOh6VWAOBP9yg-FiGIyuhIiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با عبور از ۵ میلیون و ۴۰۰ هزار واحد به قلهٔ تاریخی جدیدی رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/454584" target="_blank">📅 12:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شارژ مرحلهٔ جدید کالابرگ از پنجشنبه آغاز می‌شود
🔹
مرحلهٔ جدید طرح کالابرگ الکترونیکی از پنجشنبه با شارژ اعتبار مشمولانی که رقم آخر کد ملی آن‌ها ۰، ۱ یا ۲ است، آغاز می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/454583" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjwdP6YESZGCQbAIb4zIGEbkemlRtON605SnrGJB1uWTiXkBpxR30n7BJzsdjQfV_LOQRrsjV1LWlpx7ZoX0qcDwN0EYBn6dm3LQAJPhKrVTKpbGIJRKhK58uwwqicBfdraJ4zBZxkY_Mi0Q7wDAdVc7fV2iVckIv7dCh2HZo2hVFXcThH8X356-vM_4R9u_BBIGSSfrfMtxCpZzjWW1xSVJV3z6CYDryF1c1Wpn7MP3vKjiY25tBkPGpum6ryheBlxbZaIvybaGkQdaQ-Q12Q6efmYss9vk7cYpbJlP95Y6iPdG1JeC2Gj5yIS_on_JWhamAaSTMoWaJFt_GCClWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان همکاری استقلال و رضاییان
🔹
❌
باشگاه استقلال در بیانیه‌ای نوشت:
🗣
با توجه به مفاد قرارداد یک‌ساله رامین رضاییان و عدم پذیرش شرایط پیشنهادی باشگاه از سوی این بازیکن برای ادامه همکاری، همچنین با پایان یافتن مهلت تفاهم‌نامه فی‌مابین، باشگاه استقلال تصمیم به قطع همکاری با وی گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/454582" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837e4354bf.mp4?token=gjXKQ9IGwRwKRdQf3WmIA6gTCYE-J1y9GWOmi40-voBJh7Uvhxi86Tag3yKWpxeMm4z00hrvq53L3EptQNZK4BFSbrsWaUI_pHksc0GChNdlYi8zT7KU-phQdjxffJPjSZqKPwhdnmCGb64j36iMnThehV4lT_jq753XxEz5QRqmy8IrUVUOCIMN6SFAVMlyjH81WYxp8zIO7e9aYoj-4FcdxFwYXcBzjZtLX458Np-g0dZsJn9ehKgKI0aU7Q7AAKqTU82lc540oAfH4gnfx0wXZCzJC5ZZ51KjAMRuMixkC3u25gpeNc1ZUXIAVL3IYqgfY2gc06FK14tZkK1Wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837e4354bf.mp4?token=gjXKQ9IGwRwKRdQf3WmIA6gTCYE-J1y9GWOmi40-voBJh7Uvhxi86Tag3yKWpxeMm4z00hrvq53L3EptQNZK4BFSbrsWaUI_pHksc0GChNdlYi8zT7KU-phQdjxffJPjSZqKPwhdnmCGb64j36iMnThehV4lT_jq753XxEz5QRqmy8IrUVUOCIMN6SFAVMlyjH81WYxp8zIO7e9aYoj-4FcdxFwYXcBzjZtLX458Np-g0dZsJn9ehKgKI0aU7Q7AAKqTU82lc540oAfH4gnfx0wXZCzJC5ZZ51KjAMRuMixkC3u25gpeNc1ZUXIAVL3IYqgfY2gc06FK14tZkK1Wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار روس حاضر در مراسم اربعین: چیزی بیشتر به‌چشم می‌خورد زنده‌شدن فرهنگ خون‌خواهی شیعه و پرچم‌های قرمز انتقام است که مردم می‌گویند برای فرزند حسین(ع) و مرجع عالی‌قدرشان به‌دست گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/454581" target="_blank">📅 12:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تمدید فرصت ثبت درخواست معافیت سربازی برای مشمولان دارای ۳ فرزند و بیشتر
🔹
سازمان وظیفهٔ عمومی اعلام کرد مهلت استفاده از معافیت خدمت سربازی برای مشمولان دارای ۳ و ۴ فرزند تا پایان سال ۱۴۰۷ تمدید شده است.
شرط سنی استفاده از این معافیت چیست؟
🔸
مشمولان دارای ۳ فرزند: حداقل ۴۰ سال سن.
🔹
مشمولان دارای ۴ فرزند و بیشتر: بدون محدودیت سنی.
🔹
مشمولان واجد شرایط می‌توانند با مراجعه به دفاتر پلیس +۱۰ در سراسر کشور، درخواست خود را ثبت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/454580" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqpUs_eEmFg8DNgU_hb8vMGoHx0-FPFNZhUgMfBB2m2kcz_FtnIw806USwOpYcgYUVDnMGP1G0Mca_NYahWSaczR2sywWh2p0grPrbXsxXaJNT0D0fsn0frFEiji_N7pChmejgUk2xA2Hdt04_mZqni2y3nXGruHUVtDE4QoB2A58_jNQJlIjLMYWrl6DuaKi8Z3SH8cxzEFopqR5utHsYBV7IRsmHziix9bQgn5XscjOBakWDsERnwe1Uk-NHOoDhdCVEMn5Oz-5Wvd7jAuNzLfBWkTy-w8XtxqfzOYEn9qzmLSjZHmbCjGfYgyqtvUlhlZQW5wIX5VIQdR1Q1lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
محمد صلاح بازیکن سابق لیورپول به ترابزون اسپور ترکیه پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/454579" target="_blank">📅 11:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حساب‌ شرکت ملی نفت ایران بسته شد
🔹
کسب اطلاع فارس نشان می‌هد بانک دولتی صنعت‌ومعدن حساب‌های شرکت ملی نفت را به‌خاطر بدهی بست.
🔸
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود.
🔹
اقدام این بانک در شرایطی انجام می‌شود که طبق قانون بودجه بدهی‌های شرکت ملی نفت تا پایان سال ۱۴۰۵ امهال شده و این شرکت تا آخر اسفند برای بازپرداخت بدهی‌ها مهلت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/454578" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqiRmHgWpzeCOnIvt0yEImYCuGgFu67Ar8XTj-GF2zPPKr1Vxcz-8OOlqxycpeQ3N2iHC-UrWJekkjpLCxTmhXBo8owuZxFyc5jY9_mkqz8600uERxzyLx02I0ZGgxOglSPjBqwcyFh4V22qo5iyz7rMw776WL4XyGw9in7Iu3Y6M41wH4WQmJUnpkXE_OxwWXMjpRlOz9X_N0Ia1EmhMZ6iWAkLkgu-TJeO-kydxIy--h6zgLy1Nne8fl3muh_rHIeq3O7hy2edN8iUhlwCZG7whYVIBGIVu7HnVw3abksaQkZ8yg1rj7zbAcTXJS-cRaGP8Ihh7S5fXWiI0m7dgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت پلیس اهل سنت بلوچ در ایرانشهر
🔹
نورالله ناروئی یکی از کارکنان بلوچ و اهل سنت پلیس که در جریان حمله و تیراندازی چند روز پیش به خودروی پلیس در ایرانشهر مجروح شده بود بر اثر شدت جراحات وارده به شهادت رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/454577" target="_blank">📅 11:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c52fabc58.mp4?token=jzv6Aw_fGFKkc5QFyhHLK2fY2nJ0rNjI8rtss1CQcCOQE4G7DVjIow4wMQgpdovCQz9bJ0g_L9Uw3rUuQ_Yj03QsP7eoWqv-4I6qVRqsVNpORbdIbqSyT-cg59gcqIf8FLcc3hsHU5FTL9nhrWLIDQSegTjFc88Xhq1u4ILydBRKhKEYLovd7e6Ejqvxexlb97HOpYe6mCaqfE3cMvCxxh8IbVyA6D2arfy_0UMuPEfyNA2oFdoWqWZCGljSG3LQV79OThHcvXgwO1_GautYGzV4LYkDN6pUngBmZB4Q4nwyZcD92J3onU1dH0m8lJCe5WKEG102A8ArMMZM-vIK5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c52fabc58.mp4?token=jzv6Aw_fGFKkc5QFyhHLK2fY2nJ0rNjI8rtss1CQcCOQE4G7DVjIow4wMQgpdovCQz9bJ0g_L9Uw3rUuQ_Yj03QsP7eoWqv-4I6qVRqsVNpORbdIbqSyT-cg59gcqIf8FLcc3hsHU5FTL9nhrWLIDQSegTjFc88Xhq1u4ILydBRKhKEYLovd7e6Ejqvxexlb97HOpYe6mCaqfE3cMvCxxh8IbVyA6D2arfy_0UMuPEfyNA2oFdoWqWZCGljSG3LQV79OThHcvXgwO1_GautYGzV4LYkDN6pUngBmZB4Q4nwyZcD92J3onU1dH0m8lJCe5WKEG102A8ArMMZM-vIK5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی گسترده روسیه به کی‌یف
🔹
رسانه‌های اوکراینی بامداد چهارشنبه از وقوع چندین انفجار قدرتمند در پایتخت این کشور در پی اصابت حداقل ۳۰ موشک بالستیک روسی خبر دادند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454576" target="_blank">📅 11:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23960fdf53.mp4?token=eTTeutDLFTTO5YapPyAul0fHneRVlsW7V3CBI12adcG-tOBfA3PP0pkzOZtmuI--O0F20CvThzGdnqWjiL9WyPDAVVjZ7xXlg1B9Nyh9E3PnWWcM_P4ohvhq0kUDB_ZOCSg-dHhO0AhhUyMX9ZVh4YjTtmyxhh0gbV06KVn5eW_dfsS3G8d1FVVbzIpHa65D7TMNLyFhptjtCOYS50ec_mYrm7zwuO-yVBSU5L7gNGXk4YyQKcOqVKC-Eeyly2T7g1F7ad8-FYeerXc1nas61vFVTk4ecYJI1m07yzr1ux6q3PnKfQT4lGQK7W_dIlBNeUPbXu8jTR3w1kVLP-gVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23960fdf53.mp4?token=eTTeutDLFTTO5YapPyAul0fHneRVlsW7V3CBI12adcG-tOBfA3PP0pkzOZtmuI--O0F20CvThzGdnqWjiL9WyPDAVVjZ7xXlg1B9Nyh9E3PnWWcM_P4ohvhq0kUDB_ZOCSg-dHhO0AhhUyMX9ZVh4YjTtmyxhh0gbV06KVn5eW_dfsS3G8d1FVVbzIpHa65D7TMNLyFhptjtCOYS50ec_mYrm7zwuO-yVBSU5L7gNGXk4YyQKcOqVKC-Eeyly2T7g1F7ad8-FYeerXc1nas61vFVTk4ecYJI1m07yzr1ux6q3PnKfQT4lGQK7W_dIlBNeUPbXu8jTR3w1kVLP-gVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار اروپایی: آنچه در کربلا می‌بینیم، میلیون‌ها نفرند که خواهان انتقام هستند. انتقام برای رهبر عالی‌مقامشان و کودکان میناب با کشتن ترامپ.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/454575" target="_blank">📅 10:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU65Qcbf7Sdj2BzfeulP-Y_FlmazXTR1qYhd2wUyQhdEaiTqpLxKRYRMWZEshk7kY9jczkHl_Yv523ry4cJMyNTmDcYGk1-j3buT0mVxprtSNsRxa5pXDMwoDhqdKOt1nGv9BdUAIVmKJRrwO9er1hAsvKd_a985QI45sqvyrBtMrjd_i3hrbR0rbE4oxbyuM6idRSfydGNv7aIar_pRWmRwknY27Fky7oB5kJyHPhfl4gThwFzUwZ748bPtVgqtZvYnScJPfciQJzd0QPf1OEWyDAFEidpbgsgAQv7QDHUWokAnMJp7BATeG1QAuPB1dLsNoj3MyEba0r3eqAah-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/454574" target="_blank">📅 10:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
روابط‌عمومی سپاه سیدالشهدا استان تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان پاکدشت تا ۱۶ امروز صورت می‌گیرد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/454573" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b905e7a3f7.mp4?token=DviwatXppPsMsY30wpLCHPY6xl-7js6fY1Z8pcKAd8FK8vcmHHNc7gMYjjkVXhMNDb6_LKEGkD0k2wAWLYtYuAveu8TWJprFbm3taNsxUVkQTp810iht6QYepChkS4qd6kuNXFfhMP51t_3N83G6QdMCh0z96YbahdnkhIx091odW6ktHKbgdFevBeLT32F-GtMEDK2VdaUJYmON-RTOMI7jRXD60DT9RlVXdanmFbh28ylwYzRnmzADe16vhRFyXoLGJNozrFMrkNARYwcdO6dYESMgvy9q7__CYoPXe6-iWXsPM2UNqcD_xnD7Ay4hWQFVVx6kobLGlxclCxWmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b905e7a3f7.mp4?token=DviwatXppPsMsY30wpLCHPY6xl-7js6fY1Z8pcKAd8FK8vcmHHNc7gMYjjkVXhMNDb6_LKEGkD0k2wAWLYtYuAveu8TWJprFbm3taNsxUVkQTp810iht6QYepChkS4qd6kuNXFfhMP51t_3N83G6QdMCh0z96YbahdnkhIx091odW6ktHKbgdFevBeLT32F-GtMEDK2VdaUJYmON-RTOMI7jRXD60DT9RlVXdanmFbh28ylwYzRnmzADe16vhRFyXoLGJNozrFMrkNARYwcdO6dYESMgvy9q7__CYoPXe6-iWXsPM2UNqcD_xnD7Ay4hWQFVVx6kobLGlxclCxWmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صهیونیست: باید اقتصاد ایران را به زانو دربیاریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/454572" target="_blank">📅 10:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfEN-zvHKVTrW-F9xR0Vcf4-bbJut1OGz921yGh4tzEdQtsFlAUVyv60NosUvGOhpeu_lCTYRMyMKCvYZWP7eN6noRw8IG4D43hqGRNxBfaMwfrEtNXiJCUhe1LD0Wt9V_qddYi8zGYt7c9bDftwyygT4R1oJ5hkK1pXpo7hSf-A-Yf-vZ00da8Hh8YAHcHcEUNqoDPYK4mS1FEvEsiO5KEeBjcrn7sj6HLn8Fg5iJPQqrcBoRIsd4dNqR1s4RBwPCxR4WUdHJMHORjFN4_hhSPKXf3HHbs2Q_2AvkpXd16EZ9zsRDVaP7rbJD1Fx2kb2EcPz1gHXh3lMGVpmlgYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این عملیات با استفاده از تعدادی موشک بالستیک انجام شد و با لطف خداوند، اصابت دقیقی صورت گرفت.
🔹
با انجام این عملیات، مجموع کشتی‌هایی که نیروهای ما از آغاز محاصرهٔ دریایی هدف قرار داده‌اند، به ۸ نفتکش سعودی رسید و مجموع کشتی‌هایی که از تردد آن‌ها جلوگیری شده به ۲۹ نفتکش سعودی می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/454571" target="_blank">📅 10:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ec883c5b.mp4?token=u1RZOJcH9Ry2X0AU1mObV8LtlE5pHxQp7jefrPgUoibzQNM62RtBF7ll-OLA533qki_ue0jmwvvzc8JZo7QpjZnkYeEfEI-bc3eUw0-lsFoBR_RybtxqiVeG-ocJYHEkCLTCQnxWAHlJofSs0kFGFLK7JXndbaCBwEXrRTpVjgWbSoKPGlWXjB_ETgtOGN0lYwHQOqlRFiXxYKMdHVLcmdIc0UnhBJYc2pqwAxl53XuxoOxH2zuAOXYKOVYgwoeUKKTEs347p7i39rIbQof6oIKK9IKWjch__jZq99LOLHUddwoRXfAu7Ua3J3hF820hsbXe1-emPZBl_2Vdp6c08Yuzzfe3QOIGTrNghitDvwOg_Ey69i-mnUQklqtvZLEkROYTXMzUNJsBhZZpbZvuEIVGZmXbsoI3O_TxDCg8IJK6T22cDk5BqTAi3_Wxzh6Hy6xTsj9bHLXQwIwbTH89yVGLxbF2zc76QQL_y-EjsxVw-OTCPmx7yhAilD6XHDV4txKaUxVEYdItYUexB5ZEM1iFg4mH16zycVR25A1Q7UqGa4kGhLgn6hQo4fuHHDihKu_Q-ON3r8ozGzXWqZRmkuGpTRpaw43__Maw6_Ct-ksJ_WZYAnno1ssnlmNJK0wIfmIm2AfVyXbrk-4tUO-aNPc_Q6DEqyZRDClmY1bE9jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ec883c5b.mp4?token=u1RZOJcH9Ry2X0AU1mObV8LtlE5pHxQp7jefrPgUoibzQNM62RtBF7ll-OLA533qki_ue0jmwvvzc8JZo7QpjZnkYeEfEI-bc3eUw0-lsFoBR_RybtxqiVeG-ocJYHEkCLTCQnxWAHlJofSs0kFGFLK7JXndbaCBwEXrRTpVjgWbSoKPGlWXjB_ETgtOGN0lYwHQOqlRFiXxYKMdHVLcmdIc0UnhBJYc2pqwAxl53XuxoOxH2zuAOXYKOVYgwoeUKKTEs347p7i39rIbQof6oIKK9IKWjch__jZq99LOLHUddwoRXfAu7Ua3J3hF820hsbXe1-emPZBl_2Vdp6c08Yuzzfe3QOIGTrNghitDvwOg_Ey69i-mnUQklqtvZLEkROYTXMzUNJsBhZZpbZvuEIVGZmXbsoI3O_TxDCg8IJK6T22cDk5BqTAi3_Wxzh6Hy6xTsj9bHLXQwIwbTH89yVGLxbF2zc76QQL_y-EjsxVw-OTCPmx7yhAilD6XHDV4txKaUxVEYdItYUexB5ZEM1iFg4mH16zycVR25A1Q7UqGa4kGhLgn6hQo4fuHHDihKu_Q-ON3r8ozGzXWqZRmkuGpTRpaw43__Maw6_Ct-ksJ_WZYAnno1ssnlmNJK0wIfmIm2AfVyXbrk-4tUO-aNPc_Q6DEqyZRDClmY1bE9jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یوتیوبر معروف در انگلیس: افراد زیادی از سراسر جهان خودشان را به کربلا رسانده‌اند و یک چیز می‌خواهند؛ انتقام خون رهبر عالی‌قدرشان [امام] سیدعلی خامنه‌ای.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/454570" target="_blank">📅 10:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047db8a693.mp4?token=gM2A3qYi2sdpWB_Wecb_PUL9hbRVw5nlna7rxZqIEUn35cuxd6JOHXWooD28OGfErSTEbX36DK1rW-cGxuhEeln8Aw2YNU3tGCRFZexDM2rpmmwLpc1IFuEVYVpC7y3F29MhwisC1rDHdTOdL7lTALAaCL9WQ9VUAJNDjoUYme1iWM5b8n5D8T6c9lSjXziY1RIF5aM2Ctqa1DbzvL-IzBIAtUSdrMXVRrNyb6y4_n5OMdJi4tpGa5RX9K2Cu6nMSt3yiqvGA0NgfHTKF5vS2qywaSElMgZCCcQq1Wsr6aMqz5m6iShsFfbOnCqsn2280pCbHpNRFDt9q2LiH_-EYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047db8a693.mp4?token=gM2A3qYi2sdpWB_Wecb_PUL9hbRVw5nlna7rxZqIEUn35cuxd6JOHXWooD28OGfErSTEbX36DK1rW-cGxuhEeln8Aw2YNU3tGCRFZexDM2rpmmwLpc1IFuEVYVpC7y3F29MhwisC1rDHdTOdL7lTALAaCL9WQ9VUAJNDjoUYme1iWM5b8n5D8T6c9lSjXziY1RIF5aM2Ctqa1DbzvL-IzBIAtUSdrMXVRrNyb6y4_n5OMdJi4tpGa5RX9K2Cu6nMSt3yiqvGA0NgfHTKF5vS2qywaSElMgZCCcQq1Wsr6aMqz5m6iShsFfbOnCqsn2280pCbHpNRFDt9q2LiH_-EYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی‌های ترامپ
🔹
کوثری، عضو کمیسیون امنیت ملی مجلس: ترامپ ۱۰۶ بار گفته ما ایران را شکست دادیم، ۹۵ بار گفته ما ایران را نابود کردیم، ۸۸ بار گفته توافق با ایران قریب‌الوقوع است.
🔹
او همچنین ۷۵ بار گفته تنگۀ هرمز باز است؛ اگر باز است چرا دوباره جنگ ۱۷…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/454569" target="_blank">📅 10:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=lFR7hTLgWDivoGCjfPuuPDsHhtlCOeLHOERHviCk5Br81AfMU1bYF-HX8v-qDn2oQ1lqUgBPqcDvXCTOYC0js-6xytHUO160Hnidb0OVM2OPCrVHOCLSrjFlEfiX4mPUxLEWdHEfRt1utUl58G6AWy_n1W9870Yb6XqgW9h5KDxJJ0hYcsKxrIXEHNhGddncTmmfszh4DxMOXLZEvRxPovEIuJ-fVtWxXAXaoGYQ7h-H_0o9Eul8wlOIYySNEfc16mxYesbP_dutE0SABKYzSD7zd-hSpyqBS_6GxmXPO6iCawOl1EWUU6UVaasSj-SQb7awxoCXwVQHyfNKCbWoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=lFR7hTLgWDivoGCjfPuuPDsHhtlCOeLHOERHviCk5Br81AfMU1bYF-HX8v-qDn2oQ1lqUgBPqcDvXCTOYC0js-6xytHUO160Hnidb0OVM2OPCrVHOCLSrjFlEfiX4mPUxLEWdHEfRt1utUl58G6AWy_n1W9870Yb6XqgW9h5KDxJJ0hYcsKxrIXEHNhGddncTmmfszh4DxMOXLZEvRxPovEIuJ-fVtWxXAXaoGYQ7h-H_0o9Eul8wlOIYySNEfc16mxYesbP_dutE0SABKYzSD7zd-hSpyqBS_6GxmXPO6iCawOl1EWUU6UVaasSj-SQb7awxoCXwVQHyfNKCbWoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی‌های ترامپ
🔹
کوثری، عضو کمیسیون امنیت ملی مجلس: ترامپ ۱۰۶ بار گفته ما ایران را شکست دادیم، ۹۵ بار گفته ما ایران را نابود کردیم، ۸۸ بار گفته توافق با ایران قریب‌الوقوع است.
🔹
او همچنین ۷۵ بار گفته تنگۀ هرمز باز است؛ اگر باز است چرا دوباره جنگ ۱۷ روزۀ هرمز را راه انداختند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/454568" target="_blank">📅 10:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBZmfvaPd1IyZO8MzJROxkx5wx9p-11zzZH3UoTkGoxH--bSi2xYHqkO2z1c_6CIyZ2ejKKDDPTkUFroCxNjrgPMrMRCS9e4IF0WG5lk4UTq7-Caw6ZF7UCrgMceNqIq8MxvbRfVeB1LKMv-jUfJF-WTwRNRiJ5iz9S8clEq8KZQvpZqw88idshdsh8EHqOEcTJZp9HyGPG2dp0yZPjefXbY-w6qLpGTEhJmRgEilyI7YxC7gSogb5VcVGv2o0XfIbQ-eToC1BUhvqpHQ_IDsn0XQyaxd1hdOpuG25SAbD8c-cb33USpne356gSyx6xYPU5LT-ewV24O9w2Sy7sxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده جدید مرزبانی کردستان معرفی شد
🔹
سردار احمدرضا حاتمی به‌عنوان فرمانده جدید مرزبانی استان کردستان معرفی شد. او پیش از این فرمانده مرزبانی استان گلستان بود.
🔹
استان کردستان به‌دلیل برخورداری از مرز مشترک با اقلیم کردستان عراق، از استان‌های راهبردی کشور در حوزه مرزبانی به‌شمار می‌رود و ارتقای امنیت پایدار، صیانت از مرزها و تسهیل ترددهای قانونی از مهم‌ترین مأموریت‌های مرزبانی در این منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454567" target="_blank">📅 09:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دادگاه شرکت تات‌موتور تاک با ۲۹۷۹ شاکی برگزار شد
🔹
دادگاه رسیدگی به پروندۀ شرکت خودرویی تات‌موتور تاک، با ۲۹۷۹ نفر شاکی و ۹ متهم حقیقی و حقوقی و ارزش مال برده شده هزار و ۴۹۸ میلیارد و ۵۵۶ میلیون تومان برگزار شد.
🔹
نمایندۀ دادستان شهرستان تاکستان: فعالیت شرکت از سال ۱۳۹۹ در قالب پیش‌فروش و پیش‌ثبت‌نام خودرو با وعدۀ تحویل خودرو با قیمتی پایین‌تر از نرخ کارخانه آغاز شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/454566" target="_blank">📅 09:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسیدگی به پروندۀ کلاهبرداری یک شرکت مهاجرتی با ۳۰۰ شاکی
🔹
دادستان تهران: در فرآیند رسیدگی به یک پروندۀ کلاهبرداری با موضوع مهاجرت ضمن پلمب شرکت متخلف، حدود ۲ همت از اموال آن در مرحلۀ تحقیقات قضایی توقیف شد.
🔹
میزان وجوه کلاهبرداری، حدود ۴ همت است. تعداد شکات پرونده تاکنون ۳۰۰ نفر و در حال افزایش است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454565" target="_blank">📅 09:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GObSlaSxTjsv1fE197UEVRsT5hHOJSJy_NdtoGyQx7fGi1xBDXVmtcaM7plPnlJqNzKOEXWosfDx4Qu9j5lRAsyhNTIkHu6IVCqeAtv6NtI_kR-GcQZzuWb2Hvs9vP0KAuguy8gKldzwaUfBxqJixLEzB96CPG0etMQjoFJtKryO9o3GkWiDJzR3xXxaDa-Umt45r1nB6t3PY59vwbowctSGH4uRzOp1hmiwZebJixWYjWS21BRhlrNzCXK0iLF4wiHA69ycJt1M9RTdVZDfwxN58cFL1KlatkCiDNVhOBGBDD4ApYIVwiL306rLY4XzPmnLxbHKBBEfPycNwIX8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین‌بار اتوبوس عراقی زائران را به ایران آورد
🔹
مدیر گمرک مرز خسروی: امروز برای نخستین‌بار یک اتوبوس عراقی زائران اربعین را مبدأ کربلا و نجف بدون نیاز به جابه‌جایی از طریق مرز بین‌المللی خسروی به ایران آورد.
🔹
در ایام اربعین همچنین تشریفات خروج موقت ۱۱۰ دستگاه اتوبوس ایرانی از طریق گمرک مرز خسروی انجام شد و زائران با این ناوگان به عتبات عالیات اعزام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454564" target="_blank">📅 09:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شهادت پلیس اهل سنت بلوچ در ایرانشهر
🔹
نورالله ناروئی یکی از کارکنان بلوچ و اهل سنت پلیس که در جریان حمله و تیراندازی چند روز پیش به خودروی پلیس در ایرانشهر مجروح شده بود بر اثر شدت جراحات وارده به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454563" target="_blank">📅 09:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1ae1ed3.mp4?token=Cj951YI8wShWfXv_KL9Lgq6aL8jqsupuaCCIsBxqBHTlcvDmdWFkoHCP3ahu3y1YTFhQ14IvdWW6WyIXH68oBWPRLf789yTj6xn_06_QqDZt7k_rU8BxcTlMHksApuPlUXyDIknFfFowYI5b_Dqreng3ByumGmBkgqzTQqyB3fCGpPXSwv6biq-C2H-LUGoPBc9RO3j18hiJP34l5rL5aWmJ-W2v-fTqACdzjtfqIfCwsSpAjv08f34H_BtyLGXjXhiKrqW2QzSgo0WXtENhhyw9oQyug8uhI22ss17n0qbt7RR0KGSSIL5PHfvo8GPaC-09gwYyhn0UiwwRuiWCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1ae1ed3.mp4?token=Cj951YI8wShWfXv_KL9Lgq6aL8jqsupuaCCIsBxqBHTlcvDmdWFkoHCP3ahu3y1YTFhQ14IvdWW6WyIXH68oBWPRLf789yTj6xn_06_QqDZt7k_rU8BxcTlMHksApuPlUXyDIknFfFowYI5b_Dqreng3ByumGmBkgqzTQqyB3fCGpPXSwv6biq-C2H-LUGoPBc9RO3j18hiJP34l5rL5aWmJ-W2v-fTqACdzjtfqIfCwsSpAjv08f34H_BtyLGXjXhiKrqW2QzSgo0WXtENhhyw9oQyug8uhI22ss17n0qbt7RR0KGSSIL5PHfvo8GPaC-09gwYyhn0UiwwRuiWCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امروز تا جمعه در مازندران و ارتفاعات البرز مرکزی بارندگی داریم
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454562" target="_blank">📅 08:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار کنترل‌شده در اطراف یزد
🔹
سپاه الغدیر استان یزد از احتمال شنیده شدن صدای انفجار کنترل شده طی ساعات ۹ تا ۱۳ امروز در اطراف و محدودۀ خارج از شهر یزد خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454561" target="_blank">📅 07:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D30po8C-mGyaDuwp9QiiVE--G1_UecFwNIi6yDfCwHr9ZA9-jWrz70BdRAgRpdKKAdQuNlqoZVWgltY8ScV_iDbbFVD5k-KzuFCBrQuA4uTg0Q8FkzzgSqzwULgkWEWVIyWS4IwLg58S4SqBZB865gNOlGS2WXKi9jFy7bJ2erUoukeQN5HqJJYT5i4BZVA3ClmqjSgwWbvI4UyJe6aGDH4_f7Ep0Q_D2wzmhr3YmgXZIpxT_BTPLrSTt429awWqCNyhwdVsvrJ4DQaD0gMw5jxmwLXqHe-ISxNX7fwAi8JTyrJZNA-KJdgz5nRLFCD9S1HTaMpHm6zqQD24TsOC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای پایتخت قابل‌قبول است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۹ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454560" target="_blank">📅 07:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBBU2XgAEk8THQFhSxfwgATiy6DIepmZCGdxAE1DQN80Q82z33TsCdHC9ggjriNXEVKKAgbW-kZEAWCjVKpg2yIgDyz3Yufrhd_XWfVgpopD6pic6zB_tAGKPmv9z-aLW7oNQMJc5a9FiX-iqb4cArgAhKMYvWWbHqya236hZPXrkW1zWfSkwNHAoPemIzI4ISyt259r4vAEjFiovdbNt9o1ElW2Iq8FDtMLONxSujP3bjO4FJx2Du09jzgmU1WwZSDFXimhSoq4LOZugkp__yIsV0EMBctKTeJXF6I685ECtW1zUgrw02H3euRcbFCB7G-_GUHExLyNfLPD_bCcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: ترامپ وعدۀ تسلیم ایران داد، تحقیر نصیبش شد
🔹
روزنامۀ فایننشال‌تایمز در گزارشی تحلیلی نوشت ترامپ که جنگ با ایران را با شعار «تسلیم بی‌قید و شرط» آغاز کرد، اکنون خود در موقعیت تحقیر استراتژیک گرفتار شده است.
🔹
رئیس‌جمهور آمریکا و دستیارانش در پنج ماه گذشته بیش از ده‌ها بار گفته‌اند که آمریکا «نزدیک» به توافق با ایران است. اما اگر از دل مذاکرات ایران و عمان توافقی بیرون بیاید، این توافق بسیار پایین‌تر از اهدافی خواهد بود که رئیس‌جمهور آمریکا هنگام آغاز این جنگ ترسیم کرده بود.
🔹
طبق گزارش فایننشال‌تایمز، از زمان حمله به ایران در ماه فوریه، خواسته‌های فوری ترامپ از فهرستی بلندبالا از امتیازات شامل برنامه هسته‌ای تهران، تولید موشک‌های بالستیک و حمایت از گروههای مقاومت منطقه به یک مورد کوچک رسیده است: اینکه ایران اجازه دهد تنگۀ هرمز به وضعیت پیش از جنگ بازگردد.
🔹
چیزی که به گفتۀ منتقدان، به‌خودی‌خود چیزی شبیه به یک تحقیر استراتژیک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454559" target="_blank">📅 07:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9658f031bf.mp4?token=IJb5D2OW5LpNPFHniyFRrou1-ySreY_nJUYpip7SW7CS5Kz0gN4RLAm8zKbxXsIwYMLSTqgpsPDQ_VjE1n5KZwC93m7DwryxuNFzdyH4edqqqk3rlYppzE0MOHnEnegtdutXHIkvo76kVCLWzp5PonaZinqjV4Vxm1tWnFvhZg12NHOgVx8v7uBHm-FchQ5BIcEwBsjaR7LpdRgD2Xm2q97ZSgGrq3oFYRJbYycDrw20GUMU97auT2HYORGX0qteZoSDzfMY0w9rHXXjtcVUOVn__7mTPivKpYjTTelU9OcBu3l3oLRyaIFB7IrLBicEK5yDwD8DNln4_FJ64sUOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9658f031bf.mp4?token=IJb5D2OW5LpNPFHniyFRrou1-ySreY_nJUYpip7SW7CS5Kz0gN4RLAm8zKbxXsIwYMLSTqgpsPDQ_VjE1n5KZwC93m7DwryxuNFzdyH4edqqqk3rlYppzE0MOHnEnegtdutXHIkvo76kVCLWzp5PonaZinqjV4Vxm1tWnFvhZg12NHOgVx8v7uBHm-FchQ5BIcEwBsjaR7LpdRgD2Xm2q97ZSgGrq3oFYRJbYycDrw20GUMU97auT2HYORGX0qteZoSDzfMY0w9rHXXjtcVUOVn__7mTPivKpYjTTelU9OcBu3l3oLRyaIFB7IrLBicEK5yDwD8DNln4_FJ64sUOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با همین کارتان فرزندتان را بی‌نماز می‌کنید!
🎙
آیت‌الله حائری شیرازی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454558" target="_blank">📅 06:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تهران از جمعه خنک‌تر می‌شود
🔹
بر اساس اعلام هواشناسی، امروز افزایش نسبی دما در استان تهران مورد انتظار است، اما روز جمعه کاهش نسبی دما رخ خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454557" target="_blank">📅 05:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برخاستن ستون‌های عظیم دود از بندر جبل‌علی دبی
🔹
رسانه‌های اماراتی با اشاره به شنیده‌شدن صدای حداقل ۷ انفجار در مدت ۲۰ دقیقه، ادعا کردند این حادثه شاید به‌دلیل مشکلات فنی باشد.  @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/454555" target="_blank">📅 03:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH-rczei-QTkv9aNdqcjoD_Z2b-b9NYE5RzgH8U9aKnf-P5OHlZXTdCUFTJSiRwTriAOpYzlG4tS1iKaIbjqjY55z0_sqrMh2JGPpOMK0iufW8vWNzcfFWvyIGiN8b7L7TMaw_ZmH3N8B0Ttf0jzWBEsCfQGDfRmxMN5tHXQZXY5EOXsjXIze3wwBb7mZ8fPEn3P_lQCGtDrPi4tB5DhDOMaGo5q_xaNPqfq81sivyW_TD33ZwlMEW0tQj6hLMImsr1kU0F09ZZr6Te8c11KANq_g8rea1wGiUxxZTSrO68JC9VLWeOD24L0RnJ0fg2MnKXBknhN-Ay7DtamCGVK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/454554" target="_blank">📅 03:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufHTBbB8XFt-D8MtghigEhObeP61UXln-gJoLJ-M-FcrY-FxeLqOSCNza_d5_Xt6P7g5Hg1Aulsq7Dbk9SbShR7PTrBr2G0FPz8WNdIfL5I1F7vHTCzUZ9zYOThvL7Nt7YKLHnYF0fF1q18t4DGHf1YDfwvrPEmxwGvgRk26XB43G9lFN2wNu7v8jTD2lguDouaafTOYMETueri_DA6blYj7rQ04XyQYtqB0qIQKpKz78rOVfCdtbbBE5pSHXG_2_d38C31Y2vE895qzweZik8DWdg4uR42v6-AgGO6RCpqo9GPAW8IjZYJk3Qk-m0pFC30fhdUwbAT-3Y1m0DE8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1nUR0YKvrn4SmR0zwUUlJL0uAEZrzTRBVPy9HzKaXDVCJuv_5-jH71cAhwYeJCJ2i4btiqQXFkL7KcDn24mp-TMxxz8ALjvGHgl59264mFEzHJEiBbY1Nc6F3ZtWHMBR81iMizKlndJtjA1Mh21t3_xDpzNq5NVi7UDU1drQdtSsB_4RgI5ju7Ylqux4bmCW2drRzt8BDSvS8XcGnJgdkMYJf-uwRTETykx2pIyDsphdmTfay6fM0BmLEpkXtWilQ231JQU8V1H7_poqGb96tyxf3FmZWvdaHPwLyiu95bi15bb7hZKQRET7MmAjN9FpjTwenceF6IQtPMVJUu0Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/454552" target="_blank">📅 03:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/454551" target="_blank">📅 02:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBW43EqictE70kuSRdfMWAetImAmEcPv_NnIlytGgS9wyXQzY8HUvKjjbSpFrs-6VjD7BEOFFIQBK2NNFoHZ1EzlAVXCc8nJktSnfXXWg6ZqI72L9LRksQS1PQHZ0D4vcn8p8QjRVPaKDptw8rI0M2xuDMcrh3XOaSpYvF9LkaIDeXEDrBKN8nQegpHFVlsYzcWThgpnin-xKrGQuJFzYCGOxgieKtvwnouPFjiIB8s85k8QrjRbp0go89FaSjVFo2KFcw5gP3HssUsTxoor0QvtxcapiYM-yCeTOHyGhwE_QBgOso1f5RUDoJFKByiGeRJG1EuJBsViUNsqasAEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار بی‌سابقۀ کشتی‌های سعودی از باب‌المندب
🔹
در حالی که عربستان سعودی از تشکیل ائتلافی از ۱۴ کشور برای حفاظت از باب‌المندب خبر داده، جدیدترین داده‌ها نشان می‌دهد که تردد کشتی‌های مرتبط با این کشور در این آبراه به پایین‌ترین سطح ثبت‌شده رسیده است.
🔹
بر اساس تحلیل شرکت بین‌المللی اطلاعات دریایی ویندوارد، میانگین روزانۀ تردد کشتی‌ها در تنگۀ باب‌المندب از حدود ۳۰ فروند به ۱۸ فروند کاهش یافته که نشان‌دهندۀ کاهش ۲۲ درصدی است. این کاهش در بخش نفتکش‌ها با افت ۳۹ درصدی همراه بوده است.
🔹
همچنین دست‌کم هشت نفتکش مرتبط با عربستان مسیر خود را تغییر داده و به مبدأ بازگشته‌اند.
🔹
در همین حال، شش نفتکش با پرچم عربستان به سمت دماغۀ امید‌نیک در آفریقای جنوبی منحرف شده‌اند تا از تنگه باب‌المندب عبور نکنند.
🔹
یک نفتکش عربستانی که از منطقۀ تایوان به مقصد بندر ینبع عربستان در حرکت بود، به دلیل تغییر مسیر از دماغۀ امیدنیک، زمان سفرش از ۲۴ روز به ۵۶ روز افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/454550" target="_blank">📅 02:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa13bb083.mp4?token=iyBOTDAr8pYFnyo4dGSJ1gLKDvrjDUpCcDtERwuyvrs7NSEHkIc_xtU1Kn2Lhgi9crY9745mdi90BzeIhSl7BWL7_IEIVo-buyh7ouQhAcGmQw8nRkmTlv0ocBOLsGgEL8WeI5rMAokfYRpBYNs87WcVCowTMzkalMqWGBRWyCzr_G8Ol8Yx5Or_6epmLiu0PQ3v783rXIX3LVm5x6AnJCp6puLFwqQGPuQJn1xBT2pAVXentbF7yqdCz2E7Ja1BxL_8sOeTGmLBGKLLNatMzVPfAibl58QKnBdHco5b5UdH38-FMOVWGv5u6DLaw0iQyHHSCxrX8jW1uyUf6EaTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa13bb083.mp4?token=iyBOTDAr8pYFnyo4dGSJ1gLKDvrjDUpCcDtERwuyvrs7NSEHkIc_xtU1Kn2Lhgi9crY9745mdi90BzeIhSl7BWL7_IEIVo-buyh7ouQhAcGmQw8nRkmTlv0ocBOLsGgEL8WeI5rMAokfYRpBYNs87WcVCowTMzkalMqWGBRWyCzr_G8Ol8Yx5Or_6epmLiu0PQ3v783rXIX3LVm5x6AnJCp6puLFwqQGPuQJn1xBT2pAVXentbF7yqdCz2E7Ja1BxL_8sOeTGmLBGKLLNatMzVPfAibl58QKnBdHco5b5UdH38-FMOVWGv5u6DLaw0iQyHHSCxrX8jW1uyUf6EaTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی گسترده روسیه به کی‌یف
🔹
رسانه‌های اوکراینی بامداد چهارشنبه از وقوع چندین انفجار قدرتمند در پایتخت این کشور در پی اصابت حداقل ۳۰ موشک بالستیک روسی خبر دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/454547" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCUaaHtvzwH9-nPolKC81cEHxRlZNIfcL3nAmlF3wZcOQxP-VPddTSsnKNm4Mf_cw7HJ9Vg71tl2AI29fasboT9X6RnLnx90_vdlwF3GS6cQaXpdaC5B8IwjeLYfG0tklwFryDcp51MHLS72_Y51vL8usF1a1KpxMd2ycteoWIcAAVlyFFfyqzhXTJuw7j6h2Tmv0xh6tLWJlGX1lx6Qyph7BppQ4mr38kQCKqO7x-6S7B_UZ0feJ4vSVXqo8OLVoYhQoSi8NszUG3TjhyJQnMADJZe1LgxrCaq3NkOWcQch7Dar5jlXG4EnWkvY2WDugm7Z9zsQ2D6V-QYMFDT6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روی ماه اتفاقی غیرمنتظره رخ می‌دهد
🔹
یک مرحله از موشک فالکون ۹ اسپیس‌ایکس پس از ماه‌ها سرگردانی در فضا، امروز به سطح ماه برخورد می‌کند.
🔹
این قطعۀ چند تنی که زمانی بخشی از یک مأموریت فضایی بود، حالا به یک آزمایش طبیعی تبدیل شده است.
🔹
در نگاه اول، سقوط یک قطعۀ بزرگ فلزی روی ماه ممکن است فقط یک برخورد تصادفی با یک جرم آسمانی به‌نظر برسد، اما این اتفاق برای پژوهشگران یک فرصت علمی کم‌سابقه است.
🔹
قرار است این موشک با سرعتی حدود ۸۷۰۰ کیلومتر بر ساعت به سطح ماه برخورد کند؛ سرعتی که انرژی عظیمی ایجاد خواهد کرد و احتمالاً دهانه‌ای تازه روی سطح ماه به وجود می‌آورد.
🔹
این برخورد در نزدیکی دهانۀ «آینشتین» در بخش دورتر از مرکز دید زمین رخ خواهد داد؛ منطقه‌ای که به دلیل شرایط خاص زمین‌شناسی خود، مورد توجه دانشمندان قرار دارد.
🔹
دانشمندان امیدوارند داده‌های این رویداد بتواند به طراحی بهتر مأموریت‌های آینده کمک کند؛ مأموریت‌هایی که قرار است انسان و تجهیزات بیشتری را به ماه بازگردانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/454546" target="_blank">📅 01:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8dlmA2u_MlMzw1IX4qicQVvbBsCrMYeTp9V8DLACKgaXpTW5Q8z3PvEvIVz97d9rz0WHjR-DdFPljQdRIN45oV1ean0s7FqJFpfCaIuzr9IK9cOHoY5OySyPuE5uCrTLuPpDeWtVqEgwZU1FKD5UapKs0Sxi7kFSg14bxAl9MIG2MsYKbwt5_zuytxvFuG5Nt375xCjsRdTs343xjle200j-ROfFbhe1mNr3Koz3sdAvq52Mydf4DIYT7bUr2LhQp3RCg9aC2ST95TvKnNx5AvcJPfCbQ9buSpWdqtOp37laGpZyL1ZkTlD8_aZB65tbS2BPg8X6FbBF4z1G_n1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRQYAL6CzoZL4dFzWiSSVsimoE7dsGKpq5_SY5-I36ZLd3Of4Z-Sd65BoHv8wEgx8oTzK0omaZRZ3oSEUtYhoSZ-OV66xV_qD87ehtRgwEGbF1oAWhr95EwbzVV2f1hl42lwcEhh0WV4G9w1zz9ip5JrO0FzQOfGwNOR3UZ-DNJEDS4dBS8wNkuOQffjLM5w0VCgpEN1SvWwJXHpNawqtfSjXqt8Tz23EuIyt2aPbC5PbagYeG2A6PzloKI642KGTXs2nBSND8mBLeEc2aMk6ZFKUtWr7oQHeyOPuR0Cn_lmFQD3_evu5bHZQ6zGvqTSZQFtnUvvoMmD4vXcxl4nDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD4HApvYpZ0NCvE72SlZPdrShMtXVDiDJTXk5BE9OYW6zkubtxz-9iuL2TU387gKDioj3ixxBKvTVmGvuQiB0WVN6v3dWHGGC21JxEKWoSiDeGd0RuM5_-v-PoaCJFEZj1skM8nsZ8GteoN7mVml_vdKxNPJi1eoFguoY2u2z_s2duMwrXpI6yJ4cmnANv-A-rxq2xYSug4Mqa57uGIUnF0PAxpAhrrXvZotGTxpPXqX4jEIPJZTnB0hVz-KJtI0HU9cI5yDGTbzne3zUM3ZhkoTkDudOx6wWoWJvCktecuQ4bQTI3J8XjcPILDjbPqbSbD1oJ_A3xkGIiqPgzjpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRi-4nTKODzwGtbwoLaGZaNGmMo5JFGJvDIhP_rynwL1JJWKD08vLx1cZ83PBVNhs_q5OEvX7ULQAqTe_6-LCQyhobV04YsJ1mSyUcxWot2C33iF05q58lzO90pg0MHcLqZpjlvU_5h32WjRoF_VVhBD8tDTywzgttGHJCQstGom8Dh4D2TlqJty5ZP3Aza5hB5JP0wTNOGelc5zAhpUMekHm_7BDdJ72l7NDOKOtQOS9g-es4_StMBTtR-YVu3XoVed83dlbXuV4xxwneZCdV3VpjKjba1kOoL_l8LxDUpRTLY0jEZXoGMP_Z04tPz_D-3zenM1xSeKwbqWP67QOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454542" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeVbUSMly_6Dt_FJUA_mFdr1y4SxbJMSRNzjSQ_-vSDIzPIWhrULBnbxDxc37N4GvDdhJTZXOZ5X512pZF6KCPI7t_Y1qHQJ5O-IsZLaeC5WI2aM2ZnMhOI7QHOPuCHW1xDkQc-MZ8zmlQftdndfcwLFBeth-EdOGRe6VqiPb7BdtNXc3AadyGhbF3AIH2RPqwDwfCsZX30JbympMrmZmHTEgHkjqczozyX7ztZCe1_PSZox4oNkKslvV_MNLekIcEupkmpghfLr51SEFbg3kHrlTxjBPOV9zn_cGIJk1L5DA1U9bGUxvFVjk_pfYoMdYzO7zBBlYxLBINEdzXUTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L741TBQYxyXRzxBbKoPCFdFrXhW8yTCVCIPm51_xEEEo62TFV34qb4ccSyqFOqalZEtMIlcxFuVzdg1NPvnvFOsYpxo1zFv_W-mBUAWU7dALdUP-GyGQF3R8UZ5yBAqRxdOYzZHrXY1lEOQrcCjTrwe-DSAjRKyw3OxwMpzlbPdzSEInS5qpWLmLQSVezJTH7G7hpRteNobbC1JxwNsKVxBXvvULuiDosfDulGbMNG1KQ4uwzlztSzHyNzWahbwnB1FDZ5hzFsDCh-Ub06B58EwlA7BDkWKa5RC-F4kIdsgx6yFMIA6da9G7wnqG54sEqqRvrmX7Jlu-pidjB2z6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8q2uFf3XnV1BkLA9W0ILd_O_DNakbUi5bxgb1-TsXcBYv35GZoAvDCG7RjX-omPiYrG9M3Nna6t4Uv2JjcP-y6JdHXVQZFXCgeI9KaQe8ITgobzRHRlnZ66r7q2gJ9F8CQ5GrUb_Eogz3Z9SWw3FtyoHGHt0e_5NPxgAuQxkFHFNGODBjEbGOCB9kEMqEdXaKBZAhFATt2h1OmG8VfgENzYRY_kFhKDvjaqpO3xb0n66TQs4uc0-zIsk5ysHFK-JI4Pr8ggFjtlVEMH7f3ZJdgXiwT63yS6jPxVfb29zUk_JXypmgynnE_lnHNTrqYsSvaqq910udhk6GZI-YqEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uK6ywvDxf_FyrycxfyG2NqApGf4-D4kDoIx4nBQ7Uvs5AYad7r2teAxdHl9radakCeLiZzKyhA4N86T3oUg7JUY2eBgAAqsK-v-lhf_GnCKVBWOKeIoknUzEcTJ8oEm_4tX7nAsg2ayaSPc5jhpZsmuP8eUsGBdVswwKQXQQRXmdFZRTFJhIxpH9kdb58oKS5SxRQ8RLQzKq8W4rzf3SLOiJwF6rR7oN-ZMZypl0B55Mcpof3I61jTcgfwYsyR7FOS8ffXH1egvU0gh4_ou6slbxywsxK7QhtyLW7L0_ZLm8aOKo7zg2fhZnqDS7tToPkV5K-rXWHqKmsvwiQt8zqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knTAEUCrLCS14fDwZGryXufGrxPUWeNs474ccgu5k4b5GKjpqA5yzTGUqJlIJzyL_hDR9wzWhazttQE2MNu7ZQ9kBob03kqSDAKeqWAsUj4PCw6f8xFU3zsRXF2vIBQmhMmb90fAOk7N9QyqVrBZ83C2Itl6TOPPFAT8b2W1LaZ9iuXEGqYh_rp3g7D3XjMKo4L4X7lMQK87K8f9svDDGxwMpO8FM23sHaHd4I2t7RedFi_ePd1ch2WUJ08df3zjqe5k43Ed7gorfsVEJnGrlIP9BT19WiLs2Qhf1iQauUxVS6xVEFh8CIucC3lEvFtJ9-DUdB87mIsFgIcwzRNnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcEfHMiuiR-JFBnUZju2q2a5bb1iuVgO0bI3SZOoocENKxqD0N9s2FdVWd7xX6X9Wa7v3BA8L9WSViL9omGvA9PwnkTb67jKvKU-I-eyVPnuG8lOvwW1EO1wAbcqKelVLdXPa4feo-MA1PYSQVmlB4A2Hs1gJBCCHklM9muenDI1XD3iyc9_4vZgToa5EJermAvcTa7ujQruaTct_lFMDC-_ElXODT2Ywo_Q-8HRDI_OTWwx5orc_v5oSya3HuI6RJBrSxin_fCawJJva7fCAIITd0w2AddR-jnz0u9-UtjcTtEqALONXM641t9QKaOlBIuoVIqL6D8kA0jD85LbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5O59xvH89jOf7DEo59W2BmyQ4PbiOajI2SSWWQT0BaJ0o2ex_iTDLMFxzUNr2vLNJ0OaaadFaGjERdKMEKEMK_OYf4vG-5ED2HbeA4xEvROvyUDbW3aUp5pS49s8UHuj_-l08NLJBE_BXkNKgi99ji-9GxUm1JrNW9_ZOad2x_aUlWCReTRvcUZrdT00V1H4Y4SHnU7yN4rPr7GTfYnPcC5AbNuHOTM5UPEFX46zXlT2ZPH_mHISk_0y5lqyLf6lPTKxbbNUYP9ttP6F5v43UyI-9le3NYEEgnKcl9ZiKu04XG9ZBD2zPybfY_M8QwsJl3etPpi9-HqvpFvRppMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ed_R-2cdiWzwppxTXH3lgHLWfwmHDWQP9KeWOE9sOZfbrsavezlTWiFd8e9ojDav9jP1MXO_E8x8Bh0Scf-KmJCiZO4DObbVaCs8Rcxs89XD_I5Ar0Ph0EMz_4hmZ44nDrvOz-GX5d9GTnRagYkbaNiwSbVvMgUJXFo1gAwuGmVqIJNhzZMAFh7OS4EjgnTPPWl_W7hbruKoro2nZAKP0uotJfSZ_nNYh20dV7X77uhjd1gPTODEbtiL4N188wl1cG0TbvNBkjk9CyIr60jskXQvOPc7J42avOt9VmtwerCSZdoR0VqprcnfZNqRTLKNj5X7s-QT_fJzhDNw5UyjMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454534" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منابع خبری از وقوع چندین انفجار شدید در کی‌یف، پایتخت اوکراین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454533" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2b13B4yDV473u_1flr3vvoTnRsHkYySkbg4cxEpxFKLv3taHrL65x_k1aoRBQz_79N2OgX000qgBov3MaNKwrtdfCtfDAh6mhyt2oGRMSf-YYFJ9fX5NUEgCkWCocsv1zUE4_yOrIzIWPPeq_eu3kIhlCH3kp5WmRvD0Wp_-KZpr9b8sIYbChXMBQ5l2uQoTqAhyiS5P1n3Kg_iDuyuUeq9mhHZTDcMjppEVXDNjM-K66IVTao32zN3EKzgTvaUQKYh-asEsANAtXi6fp05tDhPPsupeYkCC5G3IvVbb27AO110mfHTU0Rz9d9tXyWecTproP_mHLCEIg1IVGPvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: جنگ ایران، ۸۰ درصد موشک‌های تاد را مصرف کرد
🔹
منابع آمریکایی اعتراف کردند که حملات ایران به پایگاه‌های آمریکا در منطقه، باعث خالی‌شدن ۸۰ درصد ذخایر رهگیر سامانه‌های پدافندی «تاد» و همچنین نیمی از موشک‌های «پاتریوت» شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454532" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ادعای تحریک‌آمیز سنتکام دربارۀ مسیر جنوبی در تنگۀ هرمز
🔹
باوجود هشدارهای جمهوری اسلامی ایران دربارۀ هرگونه تلاش آمریکا برای بازکردن گذرگاه جدید در تنگۀ هرمز، سازمان تروریستی سنتکام ادعای تحریک‌آمیزی دربارۀ مسیری در جنوب این آبراه مطرح کرد.
🔹
سنتکام مدعی شد که مسیر جنوبی تنگۀ هرمز برای همۀ کشتی‌های تجاری که به‌دنبال عبور از این آبراه بین‌المللی هستند، آزاد و باز است.
🔹
همچنین این سازمان تروریستی ادعا کرد که طی سه ماه گذشته، نیروهای آمریکایی به بیش از یک هزار کشتی کمک کرده‌اند تا علی‌رغم حملات ایران، با موفقیت از این تنگه عبور کنند.
🔸
این درحالی است که تهران بارها به شناورهای تجاری در آب‌های جنوبی ایران هشدار داده که تنها مسیر عبور از تنگۀ هرمز، گذرگاه تعیین‌شده توسط ایران است و عبور از هر مسیر دیگری باعث وارد آمدن آسیب‌های جدی به این کشتی‌ها می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454531" target="_blank">📅 00:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7UEZkXXiJJvSIywE77TLdGKsDlIHYFNi4Wl4bWXdcSUq-uU6ove5eXirBkpXaT85j1piGvAZ7jkqgh2oZiOwrd3f2Zw6vJGGwG9KuMyoBb_L-z7oAs0h8mkZ8XJ9WwoEzWldfIhn-VZd1TckJTQ33ObhpRX8ykMNliCabLppFq2KFMQZPZsLC2f4oDWap6FGW2SnAKY9ZC-wUuQS8yqiXUupviOpFeigPqnxBEo1odr8PydZM2eibzU4EztgLMW-h9rVTBscagOiG5HT_n1XlDH1cJeobvq8aUKU5jMUepN5BE1rSXi7jFajBatlvoSxPEBl9GyxBFRWpVLro5JiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ یمن به فرودگاه نجران در عربستان
🔹
سخنگوی نیروهای مسلح یمن: یک هدف حساس متعلق به دشمن سعودی در فرودگاه نجران با استفاده از پهپاد مورد اصابت قرار گرفت.
🔹
این عملیات در پاسخ به نقض حریم هوایی استان‌های صعده و حجه انجام شد.
🔹
به عربستان اطمینان می‌دهیم که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/454530" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f271b99a48.mp4?token=EyyH-dHFdyvMNSxBJxMkN0BBujRXcdWqp05GOKfnaLCPUVQTydkBsimr5VLMijLOcu2xhOF55GRjgXVj4OmhiN33twzRLG7mTaPNHkulm1U7QXk9FiJrfmUIYfCD-1WWnzdTtGi6dtLzSPAIO-jF7lQchzWV-XBAFDtKIXrSPj3kNyhorn3eXIICml-xCIwAgpKOLaNVl2S1bg9Cuhg3ue-M-TBbCA-I1mxQW5ExIpdMBA34Yo7lK7GSBycgeQrvFBm2zKMqdSBw4HmJkVWVqqEgjq00aJEtsWPxl02THEiWoeNou8i7fu8ExVVAHM40O-eE_Wqk__7RpYsSeTb0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f271b99a48.mp4?token=EyyH-dHFdyvMNSxBJxMkN0BBujRXcdWqp05GOKfnaLCPUVQTydkBsimr5VLMijLOcu2xhOF55GRjgXVj4OmhiN33twzRLG7mTaPNHkulm1U7QXk9FiJrfmUIYfCD-1WWnzdTtGi6dtLzSPAIO-jF7lQchzWV-XBAFDtKIXrSPj3kNyhorn3eXIICml-xCIwAgpKOLaNVl2S1bg9Cuhg3ue-M-TBbCA-I1mxQW5ExIpdMBA34Yo7lK7GSBycgeQrvFBm2zKMqdSBw4HmJkVWVqqEgjq00aJEtsWPxl02THEiWoeNou8i7fu8ExVVAHM40O-eE_Wqk__7RpYsSeTb0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران از مرز شلمچه در شام اربعین حسینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454529" target="_blank">📅 00:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSok_QUg6mLySRZECUP4hvfohaf8gOSFDqSxbR-tDX0hf_aDHqNpCobS6SCkHOjiH9JF5jIvlFuANFhw92ioneC32avbhpiqsivrRY5RG1hAGllr7A9PlkRNq0n6IGFzMHTzH1piPD-R65LBFN7rWGb8hAkFZMavD6CWoGlp5XnxS6eavII_UAQAFzmBNACL6tbB-FLgqmwySBs11t2IbECw-8v3VBYG-CCfbDCkK8s4oRKHT9RPC9ezdSP4Qro7UIG3Sc26Wf_Hqb0yoFFAi7DBnzSK0OrQsiojX-bffJzm888AjfwTftrlt-72MH-3mMQvWrrGjwaChei3PrwyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a7ccecab3.mp4?token=Xby5TcTzBdti365Di-Tqm5JUgnv-i4lSzZjUQceNvgSGAznaAMZTdlI13h1kmabLiZ3tBlw2CcCi70k1WOUssWJzpl-2t8aA3KLr9ljiARB4WWZgXAbjerNCPn2UMaD0LTUY-222STzj797At2qN5xw37aFZBUSt-QJ4kllFm8DRZzJhqeHulUaUEl53nAatf3fxJGY4zXm7gR0mX6OfctfXN__YSmFNeOh-PZsp7yY9ppC2-HXoGMJOKGtKPPR8fncIBveaTsvM1rvTrtVAa3NgoCnozqNagwZzc1EjmhZb5QZZEw-aoWf6MU70UhBnvck06BgixLJRYg2nTUVqKEFQDJhJIBWKTH6rU80xt2NWZORIbLemxClq0QE20YyNG7QHnXU6kAdrW1ASqCGVVb6SVb7dh8HVINvg1_8SCcfKSpUOHTCtTKyThscPKnBbTKq1eXRXfVym2PjY5ApU1U3ZApepUzMmX9XMy6EX-kZmBrTmrFBH_TdpzuyAvNEXpYW-VrrTDWF8QF05ehCiDambsLrxJG97Jr0Zx8pGfnhyTpmDGbgLEw5WnEbKU8zTXGhayxr5atphvj_QzFEZ8k_w3qcaELh2d4cijCtij0YGOz4UQC8c6-LNgK32_MMSsvRT7l7bisf1_XqPbqp0vT-LotNI69dZISER2o0dXdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a7ccecab3.mp4?token=Xby5TcTzBdti365Di-Tqm5JUgnv-i4lSzZjUQceNvgSGAznaAMZTdlI13h1kmabLiZ3tBlw2CcCi70k1WOUssWJzpl-2t8aA3KLr9ljiARB4WWZgXAbjerNCPn2UMaD0LTUY-222STzj797At2qN5xw37aFZBUSt-QJ4kllFm8DRZzJhqeHulUaUEl53nAatf3fxJGY4zXm7gR0mX6OfctfXN__YSmFNeOh-PZsp7yY9ppC2-HXoGMJOKGtKPPR8fncIBveaTsvM1rvTrtVAa3NgoCnozqNagwZzc1EjmhZb5QZZEw-aoWf6MU70UhBnvck06BgixLJRYg2nTUVqKEFQDJhJIBWKTH6rU80xt2NWZORIbLemxClq0QE20YyNG7QHnXU6kAdrW1ASqCGVVb6SVb7dh8HVINvg1_8SCcfKSpUOHTCtTKyThscPKnBbTKq1eXRXfVym2PjY5ApU1U3ZApepUzMmX9XMy6EX-kZmBrTmrFBH_TdpzuyAvNEXpYW-VrrTDWF8QF05ehCiDambsLrxJG97Jr0Zx8pGfnhyTpmDGbgLEw5WnEbKU8zTXGhayxr5atphvj_QzFEZ8k_w3qcaELh2d4cijCtij0YGOz4UQC8c6-LNgK32_MMSsvRT7l7bisf1_XqPbqp0vT-LotNI69dZISER2o0dXdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین در کربلا امسال رنگ انتقام داشت
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/454524" target="_blank">📅 00:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad9637a9d.mp4?token=I66257Jq2MW2dbJOOtifI0HZ-32y9mo4BmmEuiDIpqjz1BFNSQqZJ-Gt-rJAobX0psw0SsoTl7_HGoAkJtytnoqhKfi2hq2fQMaBATz54ahpd44dtOfZhUMwPaz-6A9A1yyZ-vw8V77zpur9Q7s4k-TMPA2FxGcIVHjiQmAEHM29DP7YSsNP9qI-55hLoGI11vWyPaKxF915AV-vY6lNTmoUxqSzji0DFqSeXcTLAFecnsP6SHZzB3dRHeyebTxwPtQZ4tV7CdPRsIfDgWZbE2CyglzOLlSD8A33xn703WUlODZuOLxoWofLT1h9Hq1wCCnXZzzuTuJr-ywfUfhFVl6_hEAITsZmID1lVkUEMG_OLBVd66AhKVd8B36RmIJZ6zDW3aR9h8FY9ApxrKRA7j0ZuGTcivbFiisj-TskdHaUdvNiO6Q3tZbRYIUxHwzB9i65zcwf1bXNfzlK-bWrl4RvaQbHps_FcsHf73mVmJJLAhtobe84c9w03ChyQBnsX05dGMHaqYYQ_bF5LjzcvIoIOfzOVoyjPyhBnGr_DO6cCaKF5mIkEJm3P7gLDIKp0WD_routNav6pnIPLxTpcldQqVe15sro5faliqvTV7frp_nrdCYXXrV15MdAwKPgJP7NwWBj1EhdNjl0w-NntyYsZD9O6ecZU5wa77tmLs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad9637a9d.mp4?token=I66257Jq2MW2dbJOOtifI0HZ-32y9mo4BmmEuiDIpqjz1BFNSQqZJ-Gt-rJAobX0psw0SsoTl7_HGoAkJtytnoqhKfi2hq2fQMaBATz54ahpd44dtOfZhUMwPaz-6A9A1yyZ-vw8V77zpur9Q7s4k-TMPA2FxGcIVHjiQmAEHM29DP7YSsNP9qI-55hLoGI11vWyPaKxF915AV-vY6lNTmoUxqSzji0DFqSeXcTLAFecnsP6SHZzB3dRHeyebTxwPtQZ4tV7CdPRsIfDgWZbE2CyglzOLlSD8A33xn703WUlODZuOLxoWofLT1h9Hq1wCCnXZzzuTuJr-ywfUfhFVl6_hEAITsZmID1lVkUEMG_OLBVd66AhKVd8B36RmIJZ6zDW3aR9h8FY9ApxrKRA7j0ZuGTcivbFiisj-TskdHaUdvNiO6Q3tZbRYIUxHwzB9i65zcwf1bXNfzlK-bWrl4RvaQbHps_FcsHf73mVmJJLAhtobe84c9w03ChyQBnsX05dGMHaqYYQ_bF5LjzcvIoIOfzOVoyjPyhBnGr_DO6cCaKF5mIkEJm3P7gLDIKp0WD_routNav6pnIPLxTpcldQqVe15sro5faliqvTV7frp_nrdCYXXrV15MdAwKPgJP7NwWBj1EhdNjl0w-NntyYsZD9O6ecZU5wa77tmLs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام رمضانی از نحوهٔ شهادت حضرت علی‌اصغر
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454523" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmmrw-QUsC9i-SmJzWybEKWrjY75YFwSL2HESQV672Bbs9IiRGee5BqzOknkvcFeTg0oIijKIMCIXhtSDiTSeMO-3P1raJgXwie9X_P5ktATU_qXSiFt0Lp-SkGMbha4gpYy3MYKtmgNZKEUWmvHmwsEAKfksn9FkzX5CD3FMe-Vq4tRrR7QGNZrewDdPIWXiz47L45IHAKcxs0rQy9o7DBujwP3Qy2gejiflSbbAFB1ObqbHx67pOIK-10aMN-4j_QriAHBu4Ccmo--afIEN-c7mh6ULce4x1QpKJD3swLieKqwn3Yl_6O2JclOMDclfdiZkxT271tph4dJrzQc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9VmiFz7o_cw7XFgFw5BnDWa9zO2hpU77IwJowkhzJfb4A3RTi2rWo7yYzTBX1dFqA9KNbHcic9v7vbTYpYfZPF1MyvjaIcT6e1ZrdSvnOAabbuejZHTTF78t8TyYIl7DutVN53to9LHrdTPLqHj_E3g5u23uf9dk-2eoEp9atHmLUSrqBwLb23DroT4Kl3vKKZZAaOhP2gTyRITTWohofaZ8ZOqIkxPC7Uav_7sz7oLyj5lHTbitgeWxRAfjaZVaJV2TRmEw1-sTCPFNXZj4dhf8udXZJFccWW5OV96tZ_R3jF9oerivqb4Axmf-_nw6f9IlVjSF5aDauAupHmixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_zK9ha5jeSKfwjfUEKCdar2KifaEsS1-GhowuHWtx8uBJkATcaAHpqZOsHitUQB9hfjckmVQomCiOmlDuZQ3P7xyJLZ3wX77Zca9_gc7QPJXggmFW0tGjDdNxPE5ZKTpTmSRoNJJsvzAxoRklWUIPqQMiRpX7cWedxEYio9B25mxvKb8kBcVxqKKqQkOhEZsY969Se_dpm-q6AV3UEWVTYU2SQyx2fzt62ougBbO6ajuqFOX9RCwf6DMawWAmB8dQwcTp2MQnBAcmvyqW5zbfwqRX787eUTJUuQhkbvph2dNXyqA47i5t39WcSrkESfM7wagx-6qtwOGYNN0Zeb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeC-lCg4Os8i9_JGwo7MUpN7dSbHVUZkIPA5qx4MYKrZV2YM1Pw0wLQXfRXTTMdoNcKbd7-zEc0W1piIXlKe90I11toceDmFnp7zhNTn6oZmNN87M_JmjmYKl_xoRBVeA_U91_SYv5LwkjMSa6jJC5ULyF0zgrJmATtBcZUpM9ixecJJwZrtL493D7GI3l40a1eDHadrlhZ42HRZ0na4huVlU5M19z039N-42csJswIz75Cc27gfu-dtJVLF8He-BiIxDdlXtTi2wjLsWeIyxr7esA-Ahg2iLVC2BFnzelheRb1C0ihWIgl2BOcwpbFwSMcguw6rlh4BdxvSK97OWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXebj5EfcBknW-R0QIluaGKDDd-IxXLqyEnJYvkDuPcnwPa2Jyi7-C8rlC1LGFI2ArUD4Ksy8OQREyvP6ZLawFH8dyweS54mnLwTSrWn7wB0Nsp4ZxFAzLkp5ZPqgX24kVRtmLP3xvb8AfRZPVYkZPVlVCLMiOUmQ3oX_gOfGtZ3hKSfz5LNbJD5MpqGTTBGhbTjxlZwnHzzurvyxf9yUhrwUCgI2Gj_U11v9ed85uMyzcPtxr1NHsyJj5iMlLx9h8dlUPMDEN4YnnQbzvoi3vmL9bNyMTtnQ8RUP1bbdXuq4gUEDh0U1hpwOMVnn5QJdjmpUIRgfISVjlgIYKMySQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیاده‌روی دلدادگان اربعین در بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/454518" target="_blank">📅 23:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7022408df2.mp4?token=bYzAyKy6X1lwiNVELjyaSzg36thHLcnq-IRtqXFol4ilfepBGFirAc7rni3KmfXtG5WOCr-e29Yq_tklSoymOAE2FKL9secOKBRqyx3wkaVXKszoLBNY-naL68M6K_eRQsqyZ-BDuayICFWgw6HsDIZR54Z5BAirZ5s4xRovzjOhEaUL_QaMuxPzj2n6s9Bcx4Wch7PPa-FiEWoH1KKFxLQs574tNGQTX8p3a7gpMsH4M3_1tGMhSszV8mGSdZ0MgOTeRZijxfvJ3WCmzJCDJjRsmRYcP5J5smmuxu-M3uy0Fxpp670Bzah_Mx1RSScWBm5SCR2aonH2jomWkVo0vYkc6g6yW5AFlxmUDmBC0czcs_j8-u4h0AP0CZqKny9ZzucaBkB-7uHWlMxrhOUwXwtbT49sDkhEsZ5ZL-VzqtBiizDo7pcBistwR1I6enuk25AUP0fFZpRu1uqHVbItC6lSlLqItCUMkV78H-mn4riGtUzgAr1I2VfzwwbijAdA2u-YfKqEE7s_nbgqq_TdiW-fVYB1A5DKroFKOMMEPubSnWmrtjfVA-_y7XNaAqmOgME-X9xmAzJJZHAo3RxHZpb-DTxZ20OadyYdHv25d61yoWIkJx_-I3bBk4hk3nmjARo8ow9O0stpeewQJIEeRcoWwPzVvnGOnng0kfIHmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7022408df2.mp4?token=bYzAyKy6X1lwiNVELjyaSzg36thHLcnq-IRtqXFol4ilfepBGFirAc7rni3KmfXtG5WOCr-e29Yq_tklSoymOAE2FKL9secOKBRqyx3wkaVXKszoLBNY-naL68M6K_eRQsqyZ-BDuayICFWgw6HsDIZR54Z5BAirZ5s4xRovzjOhEaUL_QaMuxPzj2n6s9Bcx4Wch7PPa-FiEWoH1KKFxLQs574tNGQTX8p3a7gpMsH4M3_1tGMhSszV8mGSdZ0MgOTeRZijxfvJ3WCmzJCDJjRsmRYcP5J5smmuxu-M3uy0Fxpp670Bzah_Mx1RSScWBm5SCR2aonH2jomWkVo0vYkc6g6yW5AFlxmUDmBC0czcs_j8-u4h0AP0CZqKny9ZzucaBkB-7uHWlMxrhOUwXwtbT49sDkhEsZ5ZL-VzqtBiizDo7pcBistwR1I6enuk25AUP0fFZpRu1uqHVbItC6lSlLqItCUMkV78H-mn4riGtUzgAr1I2VfzwwbijAdA2u-YfKqEE7s_nbgqq_TdiW-fVYB1A5DKroFKOMMEPubSnWmrtjfVA-_y7XNaAqmOgME-X9xmAzJJZHAo3RxHZpb-DTxZ20OadyYdHv25d61yoWIkJx_-I3bBk4hk3nmjARo8ow9O0stpeewQJIEeRcoWwPzVvnGOnng0kfIHmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی سعید حدادیان به‌یاد رهبر شهید در محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/454517" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAxm2a0yz4O2OHTFQpt-WERt8vL_jU1rY5vXFDRYJS6qVX5nvTz7O7UTYGlrNYtYEQ7WL4XAHvRb6JZLdYcTKh8rVxp_HbOPfGy6WJcV7LX2QPx0s5S7ZdOw_39sa6YCyRq_Q5DhWBipoPbv82cGyqMkX5TygH-YaJWEDR3SPu5bT-nC9cQDT8ixkPz6YkPYiqAgZs37NbonMdu7Hj2MMQR7tEqaCRJCUlNHCP6H9DHb6h5a08Sdh4KyIoLKkZyuaxBk-R_SP3o3kO6QQzXSUL_dANUCeZDAKhIjqIjbrIk-VggxB6_rQSEF94bnV4RoEDs6md54dJK5Jpa63tIHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viglPJ17CPpQz3krSfBSwpi1oTuFB779kw0ZHYAllI3BvgtY8pedX-BSGoh0umlNu0OwYYkSUB3K8asX59EkEEmwruQrH-bDFzLN-vlF6Fxu1gIIptFkNw12P3M3lf5IL3D1wekbbKxSvmmulPk9Z3qpReGrHps3sihFWVF_1k6YcIgF_IZYZ0EQnpOX_sdvCiHqIlO5d5T246Fn6ito3BgJ3cW1JxuC8YBM3oOli1X62PbMDSUWJpAbub17ggtdUWYQ0S2YRt28Q0kFnBMp8o0wyZl-se6tRvW9GKNkeA37eOwlr_nYDlY-kA7IbfsHOfsiuZOG9AMZ0azRwvzotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOv2Ebr_IAET5BRr2QVbudet13OHpSB8ThxBhcwNpEZ82GQqL4pqyuAEjpR6j5prN9yN4Bn0Gm58_LEdT7IqKK9njwvZE2MUy2k1n85DUvCQx29ua7450oox6LhI_wJHDX4cdJoXY8KmLZ48XPyg73TztOn5PlDvnf8PJ3A1QllA_kIxFcIuo4syRpSll5wHpCLKoCqwr2LS17y8MHhmfvwIwMfzX50tuGytFG2-sj0QGkWgvwGodjuzXMGscEklmgFrc-WjW1YcTW3_vherW-c0MEzmCZsZevHuRx6vPI_v9ZT4fc7TFs1LWk4VnKrgEOhHSvUhKL05Wn4AlXONHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSIYkUjvZzngbCdxSIcwkd_nhiyl98mf7YQz9ebuMxAkHfDuDC0uFxOGt8k5vFPGvciXJNhsUzRKX-scQtlZXRChmbFNMR0EdNybNhcQQgKHcj00jcLYIamUipwBU9_EioSSSaihI5xqHeVhFhpQu5FG_RUm0gE54A3Lau6W0OgIL5bv5yv3uanxpum06k7EOnC24lpFKka2Bqj038c4TiOnyRJ-SRqZzZaVZ4-Kz4Fd29S-CaeYNO29qjoqeWYS9DYgf0iNoP2gQSTk3UZwvbWaSjuCvCUWEyxMR7wgPd5yZT1HXcUXVW_Jgb_KEc4PKyY9LLBv2xdxfT2CMhKx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvpwpKn-wqW5wO6GBK2BoMJaIVDuwhf29cq4KsOzoAKvwZG3YMwY17HwyaRNrESjZiVDF6oMYotsFubI2WpljHf636gnleAz0_EA2utId-5AXJIklnbdSW09ddSFoeXeP_l3GWQ9cZk9oRRz2lsXtH_D8jrY3BNV5tIvLK7EvwYtSzoLtC4d0DOB9js87Mx8AJ3Igmw1yOIU3I4XnLs53I-6Ee4usAtHQ_EHIzknPVUzPrfB-anufxCn0-UtvL-3NF_dq2YKqunFB11dCq-qwMBkv7liad7O07vlkjf_a9NFNoNe3qTHq_gtPieb5fjInbzzOL2TjQaTipQD5rC5Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff4717665.mp4?token=exYIbjrpRBrqZdVtgIweKeSajJg82VwVFNhqonurTGpSOdhfhGuzwGrJVqa5JdC5haO9U_5mj-crE_F1hIOAqlqXLnYmIaNf9RkySjwYEe2XD6agotzVe0lNGrwPUjts3vANlizg0fHrCLLuHxAk_K0YZ_rDW_2OfwUOf-B4azLPLq7zYtLqOLX6eucOBw86KXv_pygFjAL9fuvrF1MqX9-wFzJ-p3_9ajrdQyvsY7lCKj_vFeaePgRDl02axOpoAnFeo0Lgr_IMkfqLQ6CTFrRHM2qZoUTODglUPHUY3yseCNsck2pJwbRRk76uquecB55e74lPLz4mXo3NN8mbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff4717665.mp4?token=exYIbjrpRBrqZdVtgIweKeSajJg82VwVFNhqonurTGpSOdhfhGuzwGrJVqa5JdC5haO9U_5mj-crE_F1hIOAqlqXLnYmIaNf9RkySjwYEe2XD6agotzVe0lNGrwPUjts3vANlizg0fHrCLLuHxAk_K0YZ_rDW_2OfwUOf-B4azLPLq7zYtLqOLX6eucOBw86KXv_pygFjAL9fuvrF1MqX9-wFzJ-p3_9ajrdQyvsY7lCKj_vFeaePgRDl02axOpoAnFeo0Lgr_IMkfqLQ6CTFrRHM2qZoUTODglUPHUY3yseCNsck2pJwbRRk76uquecB55e74lPLz4mXo3NN8mbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انبوه پرچم‌های خون‌خواهی در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/454511" target="_blank">📅 22:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34667a08e3.mp4?token=bSlM7GRXwh4WGxywSHvGi3RDg2F_kHWwpFPhARzPGgqYKMvs4Ncv4mf3SmZH_YG8yIiNV-6rB9mPI0cb9YQ5JLJA0IFfP2nDr4tofb6QqB6Y01TxMys9L_pNbbbvx4Y6B3okOlzQ5ZVl3Yh7ZRx5pwQ6qwn_SZXJx3T9yYZ_l_66YKHGflbiSIEvhzsBVHi4276G7rRUYhPA-FF77A5imyebibCza0yXamrNI0XMAwnpYjJ5vIFxC87_o1B1J2BJD_GnOF_Cehw6ox1jFJLsFR4TB7BbaUAH0vKzBm9s3yzMzOiS0S0RaQFaApdwka2QIV0jdNuQe2w7LvYcpHUfNBnsIz_VSgfWnusqkBSXoPKK46e4clWFltDuozFkRoir97zGVPY6N_ZgrMf-4lfxsV1DrdtSXZmpcgkHcTmR7J8rKGlY5yPWVySePwMXYdryL8T3qeVQh2Gzw_1mle_BckftqsQLeeGxgs04uW0f4lNa8mm2-bmHpgmfoi08Z552KvmOOCB7ODNOabNOF4K4YUnh8NUzjTj4EK3GqDpiGHT5MoF6PKraCVPxzgeKnxa69MRlFM71-uGuQqX_2Hhw4nNP2Z24zcroHroEi1c9fOT65bZmYGxFQZ_yJ4wlQVyV4WKDy6EIyX6tmRtAnAmdnALaRKw-Fw4jJoI2F3nHhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34667a08e3.mp4?token=bSlM7GRXwh4WGxywSHvGi3RDg2F_kHWwpFPhARzPGgqYKMvs4Ncv4mf3SmZH_YG8yIiNV-6rB9mPI0cb9YQ5JLJA0IFfP2nDr4tofb6QqB6Y01TxMys9L_pNbbbvx4Y6B3okOlzQ5ZVl3Yh7ZRx5pwQ6qwn_SZXJx3T9yYZ_l_66YKHGflbiSIEvhzsBVHi4276G7rRUYhPA-FF77A5imyebibCza0yXamrNI0XMAwnpYjJ5vIFxC87_o1B1J2BJD_GnOF_Cehw6ox1jFJLsFR4TB7BbaUAH0vKzBm9s3yzMzOiS0S0RaQFaApdwka2QIV0jdNuQe2w7LvYcpHUfNBnsIz_VSgfWnusqkBSXoPKK46e4clWFltDuozFkRoir97zGVPY6N_ZgrMf-4lfxsV1DrdtSXZmpcgkHcTmR7J8rKGlY5yPWVySePwMXYdryL8T3qeVQh2Gzw_1mle_BckftqsQLeeGxgs04uW0f4lNa8mm2-bmHpgmfoi08Z552KvmOOCB7ODNOabNOF4K4YUnh8NUzjTj4EK3GqDpiGHT5MoF6PKraCVPxzgeKnxa69MRlFM71-uGuQqX_2Hhw4nNP2Z24zcroHroEi1c9fOT65bZmYGxFQZ_yJ4wlQVyV4WKDy6EIyX6tmRtAnAmdnALaRKw-Fw4jJoI2F3nHhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها از آخرین دیدار با آقای شهید می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454510" target="_blank">📅 21:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پرس تی‌وی: باوجود مانع‌تراشی آمریکا مذاکرات ایران و عمان در مورد کریدور تنگهٔ هرمز وارد مرحلهٔ جدیدی شده
🔹
شبکهٔ پرس تی‌وی به‌نقل از یک منبع آگاه گزارش کرد: مذاکرات ایران با عمان دربارهٔ ترتیبات آتی تنگهٔ هرمز از همان اولین روزهای بعداز آتش‌بس در ۱۹ فروردین…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454509" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454504">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYIPAzi98Z5OfeILbfH1U2PBgiX6uxsGldfiwlhjqhy9pTudHK6EB_YXfRZ_SI7cUxpHRB7LwyiElgfB6Y_Sb2B0J3rAUI9OmCs316AoI_kGSVC4kxyPc3kPrnXTIx1tSPlUPw3amWnfivsRNzbmYnaNAE2KjJrPHGIMJq1F4X0BfuvQPch11yCQNMAZNBItPKek2QKdP5WsxIRVPfN01XkDYv_-ykptupvhMvhPU36azvxnYxQNmFpV-bTxaksXBeK6G__0nJzUx-GFwfkXXkN3MOwRW2hY61yTRC2TUbitZc9ybZ77D_3IBp3S8ktexinPrBl-p5jOEkyqeaFY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfgQVwocRnlHb9DpLVKuM0FvKxaRI_NEjlyZVwB2HOf45Z339Ml35p5YoJnrksmrMOs-2tosJZTiiJMmqYRSfEIMIYzkuqA8-ZAT2KepFbdDc4-j5fZW0dheBvAcqJaWHAMVT-2PmMr57-z2zopfvKpEIfz-OJS0V92o8s9hUj7cVmPYq433vDTJnxObdfRqejFX6BZ4E6OIoxFazX4nxdYzdikluAHb24oDaY7LAWN1L6K-8NRn21WO2hTNtm4VR87gDF426-4jpbMaHbMScJaKELh_7PuXY64KPGRFDipD72vaa1JIVTwXp4tY3ug-aPkh7Pcw2I_I1I7vOQf5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJrYfTFR7Q6ABG5w6ce8Ugr8nIAhgkiJ8iQnt3fnLCYfFadhRafXIJC7zX8BgiYnk8Kuu3tN7J7Smf06wlCI0TnWvUmyZcrXnKf57uUcE3863ZsUdJIaD0K7Hr54TFzv_tQ6gsDHz2A5kboEQ4LfKhOyGYOuZacGqfj8Vjqbf0jzH_qc9UduC21fwPtHV6Ss_E6aH7WyLHhHsNrzcCLKzCi3jDmO1MxP7KiqaX4rCCrgJ8ZRqFThy0-rJHAidmKTBaPyhPMXEdjsaPq2jg8oWmL3fcPv-1zo-_1QTplHtjUlniabxMCTHGcDkEaG1Oad896LMETFCcFDdktS3D5nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfK5nlikpAqUjpj6G2J2oH56cWgUlMbHY5WTOLEsgtk6q8EU27hfX0UmPypV3j_5BdwQmt5vz5wDn5LA7_mjxuJoogLPJHuJiGOuikMGVhdFWMPjGI6nMdRFOBIneEZFr4PPQ9E5N7X4wlbS6MfXNhsuSrVNZbpEM-0TlY-YG0GyIqwtcw-Mbl3k9mJ-6gO9wHJDZ_UN6OX_mPHqhFuD90nDfSu5TFaQtC5UieBpUA0SyntcwEKGBuvvXxVd6xVdEw3Uiya3GvYUG-nNUcaHn1hgvvIia4Av7o0yXJ3JvDwErd4excfrDMMFdZO8DVdFpjVke7vZqHQQzswCAMeICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fozinNvJcV97kZnNW7yOo5HDd3E8309ani8NtgcD3NB5mY0FUNrpOGRkFYRIrUE01YVU4UVlO7_KokSAA2GaGe1Jjw8kHcyA1-iyhZnn9OkIdEYamj6vW8m2f9q1pcH4MK-ctyRAJoqOuXA1PSGfo8suYx-Av7KGOikLtn_FcS4WeWCtJcEwxeyfGqJHDoi3T1Cl3Df4u686CIE-fO1fn8Sk5ISzcXVv-ioP1VD0LtWjhoFmVMfOd9EQyh6Dcq2esspIie-_ygzOQkYLXKprII6USlDyJ_EDWH1MwdFXHt19fbw1-BNQt9pMdXq8kKYXpX-6zhzls2SLgauzBxHzxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قیام خون‌خواهی مردم یزد در اربعین
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454504" target="_blank">📅 21:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454503">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
مستند کوتاه «یک لیوان آب»؛ روایتی از خانوادهٔ شهید محمدرضا خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454503" target="_blank">📅 21:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپاه هرمزگان: از فردا احتمال شنیده‌شدن صدای انفجار کنترل‌شده در اطراف بندرعباس وجود دارد
🔹
سپاه هرمزگاه اعلام کرد: از فردا به‌مدت ۳ روز در ساعات ۸ صبح تا ۱۲ عملیات انهدام مهمات عمل‌نکرده در محدودهٔ ایسین و سرخون انجام خواهد شد؛ شهروندان نگران نباشند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454502" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d23c2c06.mp4?token=o04y56TQIPIy47kGmLkHBEoKvWjQzSoyy6ql3TEaPwvQ69Cl2XJTMijP-3WXqNlPu626-E684y-1AAd21SP3O9OjkryDScfjFkyhq6EE__FjeyXcl0ChrEngrVrJ82htho67uRLTvrZVk8LdNykNWWnNJZsjbV0EScisRi-qp2YX1yHqKerhLwHuk9mjwiHuI7PPxiQYT6rnuO64G12l9OMpPJu2dSPHyklctQhmjXFSWWfru4tv0jq15RbY5qO6ysnJtC2xGWMwl78vL_JwAIHG07mL3IZbbvrfIXD1xvkPt36nAGcfrF2_6vHNtR_wtAuGgBDqLSrbAup0A8NEmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d23c2c06.mp4?token=o04y56TQIPIy47kGmLkHBEoKvWjQzSoyy6ql3TEaPwvQ69Cl2XJTMijP-3WXqNlPu626-E684y-1AAd21SP3O9OjkryDScfjFkyhq6EE__FjeyXcl0ChrEngrVrJ82htho67uRLTvrZVk8LdNykNWWnNJZsjbV0EScisRi-qp2YX1yHqKerhLwHuk9mjwiHuI7PPxiQYT6rnuO64G12l9OMpPJu2dSPHyklctQhmjXFSWWfru4tv0jq15RbY5qO6ysnJtC2xGWMwl78vL_JwAIHG07mL3IZbbvrfIXD1xvkPt36nAGcfrF2_6vHNtR_wtAuGgBDqLSrbAup0A8NEmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فرماندار ری: آتش‌سوزی در شهرک صنعتی شمس‌آباد اطفا شده و آتش‌نشانان در حال لکه‌گیری هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/454501" target="_blank">📅 20:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454500">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787dd9fb3a.mp4?token=CbgxBi1qszR1CXknqfEqILNw7f_f1zDfZdfMKLdpP7lmwHdfI8Vx1fLkWlNZZuugGs_gp20hx-QTs7HeUlB0pZSTAgsF1Mlc4HrLiMsOJIJaFf662OpCquihlEHZJGvd2wbzUfzMHvJEK8H_uw4Glx98H3V3rm5CDfZ5Lcg5uoB1lS-J_WEWYLN9_eLne36whmrLfyMC-Fa7Rge_fG2tFlLvko5McQxtF4X6TR-0BGB7O-PhPpDR8bTcjqgyCKr5FQ3feHr9wUGhOW-GG4a-AYkiK6JNcgFC-mQgeR7oKWZeOjB-dZOXfZJ5-GqvGEwXrQMg01G9HL_7CQBuhUq9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787dd9fb3a.mp4?token=CbgxBi1qszR1CXknqfEqILNw7f_f1zDfZdfMKLdpP7lmwHdfI8Vx1fLkWlNZZuugGs_gp20hx-QTs7HeUlB0pZSTAgsF1Mlc4HrLiMsOJIJaFf662OpCquihlEHZJGvd2wbzUfzMHvJEK8H_uw4Glx98H3V3rm5CDfZ5Lcg5uoB1lS-J_WEWYLN9_eLne36whmrLfyMC-Fa7Rge_fG2tFlLvko5McQxtF4X6TR-0BGB7O-PhPpDR8bTcjqgyCKr5FQ3feHr9wUGhOW-GG4a-AYkiK6JNcgFC-mQgeR7oKWZeOjB-dZOXfZJ5-GqvGEwXrQMg01G9HL_7CQBuhUq9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخی که پیام اربعین امسال شد
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454500" target="_blank">📅 20:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای رویترز درباره غرق شدن یک کشتی هندی
🔹
خبرگزاری رویترز مدعی شده یک کشتی هندی پس از اصابت یک پرتابه در نزدیکی آب‌های یمن غرق شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454499" target="_blank">📅 20:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938227f39d.mp4?token=jRAcAzcz-NUrd-p2z9bDIaqElmceaJoen1GUhWv5gazx0V0YLsK5VDUljSKS3UImcMuzqqXK7eNH319TxU3oQrDa0XaEjfWPzOk2qK1WKdSPXzYEqoJJs2rJrnpQ5TWt-aNRu9U-2i5nOUm-t4DLQFoVl5axbmm_DrzTgp_gfbuluDsfjUjoEaj69qWoBmQLVRaimJY6hENywf2Y5l176RF7oaqZJNcOVwPkgFM4h8KKKJ3_EnLzWKGmHHSQCmM805aOpUY3wGXzpfZ6mgij-BU3QVV7emyLu244P99vdrQVKQjOvw5T1V-LN1V6XqEGj7epy8UTV7nx7HHMQZfJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938227f39d.mp4?token=jRAcAzcz-NUrd-p2z9bDIaqElmceaJoen1GUhWv5gazx0V0YLsK5VDUljSKS3UImcMuzqqXK7eNH319TxU3oQrDa0XaEjfWPzOk2qK1WKdSPXzYEqoJJs2rJrnpQ5TWt-aNRu9U-2i5nOUm-t4DLQFoVl5axbmm_DrzTgp_gfbuluDsfjUjoEaj69qWoBmQLVRaimJY6hENywf2Y5l176RF7oaqZJNcOVwPkgFM4h8KKKJ3_EnLzWKGmHHSQCmM805aOpUY3wGXzpfZ6mgij-BU3QVV7emyLu244P99vdrQVKQjOvw5T1V-LN1V6XqEGj7epy8UTV7nx7HHMQZfJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر ترامپ زیر پای مردم عراق و زائران اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454498" target="_blank">📅 20:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bssAK-781jEhrcovajlYcrEUnoW48PvFZ1hO7_bzjEgiAaGOyS1hK5HZcdkSAPGBMlWb2T1lPLbEq2GSS4-BdDPqiALv92nRVydQ5tGNh7xOiuespNojZNwrSoRxuwdfrLZfDcOGPBTJrtlDYR4fRxQ2eF-fvBXAtmBlzTl2NnsXz3J3PvkV3NoczajjJtKGAwC8jHi2MQfXKqIp6gUtCBSE5ax8IfkoF9DyfkkDgTqBPlMBIvzqK3_5V74lp_UBow4aEy9vWI9wd2veUpyEciH_jeWxZI7FnGfFvsYpWFyj6I23zrn3zR7eNcj8fYuAFhHyX9deEowaJrIEgnkwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی: باوجود مانع‌تراشی آمریکا مذاکرات ایران و عمان در مورد کریدور تنگهٔ هرمز وارد مرحلهٔ جدیدی شده
🔹
شبکهٔ پرس تی‌وی به‌نقل از یک منبع آگاه گزارش کرد: مذاکرات ایران با عمان دربارهٔ ترتیبات آتی تنگهٔ هرمز از همان اولین روزهای بعداز آتش‌بس در ۱۹ فروردین…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454496" target="_blank">📅 20:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b453dbc80f.mp4?token=lHNgTUiuJUsOhAfIaQ4_DDen5RJYb5CbjH149Su1cfC8tpe9m4oLMVnNUPChLkM9jwUaL5phWVMgr2pobFeY7dJuDy2mCVvew45UJvfMSVISyZWEJppmTHXlhi_5xEujEvmOlqzdJtwetBVPGqn255XKCtRnU8H5HCWRi3aAZSy0mo2hXStB2vhnhQRp134-QOVrIf-Mu2Mx6bQcvN1ilUOgidnleAyxAos7d9JDRz0bKMyFtF0GYngBXvAP5FeaBnXBdPE_e_C94oSozNj9W5FHVPMBcOOOCp5fmtc0BdmUGqnOlk6wYPIttg7H5DhhC7PGlReR2nP0Xgsdw-LoSKZuNN4FxRTEOk8Lc8Tj-M7Msh167yQAvNyHESp6J1MisGNtLEADlVaATefhm-4BxcCR46RLBHdvUXNxnxz7BsSMIBSKcmUabaYNFwNAYL8Ig85A54qI5naOz85Ehv_YfiBiaEjgdYMnJJ7S3MnUhnqy_segmHrrQTcaxqWuCDCazwWmxPBMJJqCj1FqbubXHBS40DpwdBUios92iC5HgJv-enlqtcGHFK6hzj2nnhrQdYmuuUO1rzB5Qi1adIeOHc1qtdmBv3UpKaqPNqG-YODBQw2mhvGipliyhlbFbiTsM4U5XEdUOF-JJlDig5t_FtwnAG4ddF0wbL5e2V-KdHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b453dbc80f.mp4?token=lHNgTUiuJUsOhAfIaQ4_DDen5RJYb5CbjH149Su1cfC8tpe9m4oLMVnNUPChLkM9jwUaL5phWVMgr2pobFeY7dJuDy2mCVvew45UJvfMSVISyZWEJppmTHXlhi_5xEujEvmOlqzdJtwetBVPGqn255XKCtRnU8H5HCWRi3aAZSy0mo2hXStB2vhnhQRp134-QOVrIf-Mu2Mx6bQcvN1ilUOgidnleAyxAos7d9JDRz0bKMyFtF0GYngBXvAP5FeaBnXBdPE_e_C94oSozNj9W5FHVPMBcOOOCp5fmtc0BdmUGqnOlk6wYPIttg7H5DhhC7PGlReR2nP0Xgsdw-LoSKZuNN4FxRTEOk8Lc8Tj-M7Msh167yQAvNyHESp6J1MisGNtLEADlVaATefhm-4BxcCR46RLBHdvUXNxnxz7BsSMIBSKcmUabaYNFwNAYL8Ig85A54qI5naOz85Ehv_YfiBiaEjgdYMnJJ7S3MnUhnqy_segmHrrQTcaxqWuCDCazwWmxPBMJJqCj1FqbubXHBS40DpwdBUios92iC5HgJv-enlqtcGHFK6hzj2nnhrQdYmuuUO1rzB5Qi1adIeOHc1qtdmBv3UpKaqPNqG-YODBQw2mhvGipliyhlbFbiTsM4U5XEdUOF-JJlDig5t_FtwnAG4ddF0wbL5e2V-KdHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پیاده‌روی اربعین امسال بیشتر از همه نایب‌الزیارهٔ چه کسی بودید؟
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454495" target="_blank">📅 20:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651dbae8f5.mp4?token=CrvsoN9RLP0W-Nyrdj8XVa9zXLQ-vRmkJTJmTJYyUddAFOZQm41Hojp1hVydGlBGC-NnUQDjmNkgOqM_eDnRn_pPnhaDW6G_sjFhnhSxCk6aNf_XiG9tu_6vjSmI54rYZFeW2Tmq-GSl8RsoohrVIPbmGBSY3bktBBjjqQfOpPnmAJzukCrWrBbQw4xyAUomv-oVH9Xy4fJ0ssmQ9aWLdNbj9vF7UgECMq5WZWg_RgkKlm7VQ-c6Y1glsCg3uh68UFh6YJxGf-Jp9XR6DskDDNf5dLlpyEUK1HhYvNsc0BWQLkmfQmS2AJxpfQsDcOu3-59Tq9uuWJQ2sJ2mxiRi_CKR3ZrLY6HJ-bz5Ell2R_3ztaw2QrZZwd_Qk6dX78xr8pfsjyppy2mA8dUBGIUFZu8iye-2lmeElkonC3htd_E2_z3CK5sYgS5HL-Pfazov-2eVbKOrrYxLjJIkasUX_K-NTql-YguYSMBGhv7oe6Y2oYOYmktbUj1TwxHiRoIn9Bvl6npx6Uqhbm8lN5ndHRbKNn9rsBuU-vUMzveGO57Ad-WfLtduMuTluEpu72jC6eejpQn4iz-bBYXIKm1DWc_6ufESRi3ZrjSJeGuATW_gFNxEfBMAJSIAXZ1STNtp6biIMYwkgtFIG5szJKzHhXTY60KaeWypyO131LZ4QJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651dbae8f5.mp4?token=CrvsoN9RLP0W-Nyrdj8XVa9zXLQ-vRmkJTJmTJYyUddAFOZQm41Hojp1hVydGlBGC-NnUQDjmNkgOqM_eDnRn_pPnhaDW6G_sjFhnhSxCk6aNf_XiG9tu_6vjSmI54rYZFeW2Tmq-GSl8RsoohrVIPbmGBSY3bktBBjjqQfOpPnmAJzukCrWrBbQw4xyAUomv-oVH9Xy4fJ0ssmQ9aWLdNbj9vF7UgECMq5WZWg_RgkKlm7VQ-c6Y1glsCg3uh68UFh6YJxGf-Jp9XR6DskDDNf5dLlpyEUK1HhYvNsc0BWQLkmfQmS2AJxpfQsDcOu3-59Tq9uuWJQ2sJ2mxiRi_CKR3ZrLY6HJ-bz5Ell2R_3ztaw2QrZZwd_Qk6dX78xr8pfsjyppy2mA8dUBGIUFZu8iye-2lmeElkonC3htd_E2_z3CK5sYgS5HL-Pfazov-2eVbKOrrYxLjJIkasUX_K-NTql-YguYSMBGhv7oe6Y2oYOYmktbUj1TwxHiRoIn9Bvl6npx6Uqhbm8lN5ndHRbKNn9rsBuU-vUMzveGO57Ad-WfLtduMuTluEpu72jC6eejpQn4iz-bBYXIKm1DWc_6ufESRi3ZrjSJeGuATW_gFNxEfBMAJSIAXZ1STNtp6biIMYwkgtFIG5szJKzHhXTY60KaeWypyO131LZ4QJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر از خادم خاص امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454494" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a692ea0b08.mp4?token=UNoEVD7mhEcPHeiBMehqkl-Jo_uj-u_ys2v5s_Zt12SDZlMS0Lzux_G5EShU29k4GtJ9tNrWFewkYEHw052rHLupQw7o09F0B72bJd0um72WwSz-So23yztn8u8uIOS0HrrB2iTgnKlys5312iZetr-3Z40t4QF-Z_wy6TogPs_taWL12Ymv7huPVM_0nFGDRRtQrefeLREJNztpPqZWxPdXFonKzdfuMgn-S7hz2X2DLbAuuBy9Xs8ICgMqeIXuLir2uKLMyOfYeNqSm6ycjSM6q3Ojk4Qql04ItEiLF6M-r5y_uNbdUNc84I_fYLJOqcJApsrBAZvE5dEeXK6wug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a692ea0b08.mp4?token=UNoEVD7mhEcPHeiBMehqkl-Jo_uj-u_ys2v5s_Zt12SDZlMS0Lzux_G5EShU29k4GtJ9tNrWFewkYEHw052rHLupQw7o09F0B72bJd0um72WwSz-So23yztn8u8uIOS0HrrB2iTgnKlys5312iZetr-3Z40t4QF-Z_wy6TogPs_taWL12Ymv7huPVM_0nFGDRRtQrefeLREJNztpPqZWxPdXFonKzdfuMgn-S7hz2X2DLbAuuBy9Xs8ICgMqeIXuLir2uKLMyOfYeNqSm6ycjSM6q3Ojk4Qql04ItEiLF6M-r5y_uNbdUNc84I_fYLJOqcJApsrBAZvE5dEeXK6wug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمد انصاری، بازیکن اسبق پرسپولیس: اربعین امسال را به‌نیابت از رهبر شهید و شهدای جنگ ۱۲ روزه قدم برداشتیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454493" target="_blank">📅 19:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvvnxXOVDDzAtoSkHjWz-Mcu2U9gwIuyJYRJBPl0LRv8r76Bk1ZxRLuM4lYblFqSrv2p2kPWaqMOpTbtsWq3hgg5XI5xbceU_RH7as9_7Wf0sDbl6wp9oCkGJ0SyQv-2PzVfOlh2SVGUwiCtrp17g_IuNvPC5FCq07d7ZIGN_-yBrmTc0RFRb8UlmqOsKRQ0TcelGR2IfEkWCz34rqVhljo2EAFAazLvM5A9zrAUdA79Bu4oduIDK_kmnsQCLrx7WightiBtP1QDj4i-Je71niwDayDn1n6kWpb6JTsxS8CDVD_bxmGrBgtl-f_qKjgvZ6iKhPpFSyYlTfuI9Kx0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی: باوجود مانع‌تراشی آمریکا مذاکرات ایران و عمان در مورد کریدور تنگهٔ هرمز وارد مرحلهٔ جدیدی شده
🔹
شبکهٔ پرس تی‌وی به‌نقل از یک منبع آگاه گزارش کرد: مذاکرات ایران با عمان دربارهٔ ترتیبات آتی تنگهٔ هرمز از همان اولین روزهای بعداز آتش‌بس در ۱۹ فروردین شروع شد و در پی تفاهم خاتمهٔ جنگ در ۲۸ خرداد، وارد مرحلهٔ جدی‌تری شد.
🔹
ایران تعهد خود طبق بند ۵ یادداشت تفاهم را در مشورت با عمان و گفت‌وگو با سایر کشورهای منطقه با جدیت دنبال کرد و انتظار می‌رفت که در بازهٔ زمانی ۳۰ روزه پیش‌بینی شده در بند ۵، به نتیجه برسد. اما متأسفانه مداخلات آمریکا و کارشکنی‌های برخی کشورهای منطقه این روند را دچار اختلال کرد.
🔹
اکنون بیش از ۲ هفته است که مذاکرات با طرف عمانی وارد فاز تازه‌ای شده و اگر کارشکنی آمریکا و برخی دیگر متوقف شود، تفاهم دوجانبهٔ ایران-عمان در دسترس است.
🔹
هدف این مذاکرات، توافق بر سر یک کریدور جدید است که تأمین‌کنندهٔ حقوق و ملاحظات حاکمیتی ایران به‌عنوان دولت ساحلی متضرر از سوءاستفاده‌های آمریکای متجاوز و همدستانش از این آبراه باشد. این کریدور میانی می‌تواند تردد ایمن از تنگه را فراهم کند و با عملیاتی‌شدن این کریدور، هر دو مسیر شمالی و جنوبی متوقف خواهد شد.
🔹
این مذاکرات، میان ۲ دولت ساحلی است و ربطی به دیگران از جمله آمریکا ندارد؛ اما ترامپ با مداخلات مکرر در صدد القای اثرگذاری بر این روند است.
🔹
او در صدد دستاوردسازی است که به افکار عمومی داخل آمریکا بگوید که از طریق تهدید و اولتیماتوم موفق به اثرگذاری بر این روند شده است. با وجود این، اثرگذاری آمریکا در این روند همواره منفی بوده و روند مذاکرات را کند کرده است. چرا که ایران براساس زمان‌بندی یا خواست ترامپ، منافع و اولویت‌هایش را شکل نمیدهد.
🔹
ترامپ نقض عهد کرده و ایران طرح خود را برای تحقق ترتیبات در تنگه، مستقل از تهدیدات آمریکا به‌پیش برده و خواهد برد.
🔹
لازم‌به‌ذکر است که کریدور رسمی موجود در تنگه از سال ۱۹۶۸ در آب‌های سرزمینی عمان بوده و ایران هم نسبت به آن حساسیتی به خرج نداده بود. اما تحولات ۵ ماه گذشته و سوءاستفاده آمریکا و هم‌پیمانان منطقه‌ای آن از این آبراه برای حمله به ایران، هیچ جایی برای ادامهٔ رویکرد نجیبانه ایران باقی نگذاشت و ایران مصمم است که ترتیبات جدید تردد در تنگه به‌نحوی تنظیم و مدیریت شود که حقوق حاکمیتی ایران و منافع و امنیت ملی آن به‌طور کامل تأمین گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454492" target="_blank">📅 19:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6nYt6visOFs6NZNh3ZbZgIOIBN3L8UdrmD9tb4Nmg_BqrsYXMRafVo8q69J-gXMpZmufIo_zjzOIaTH9n5WOukgwg-ocDGO2VNz6Y-1hbSOxvp1BbL28oEcLp61_R6WLeYHSrimmNXqd3Q1fgptKDRLO8wcXNdIRIq_mQ8PrkDh4NLZpueLY4R6W1rm9iJKc1QqxbCJ3NyOqkaPwxVnKlAAgfHIHtHZc2df0nkIGNfxVAmgY3zsHuwBaXAtkZyHwVVqtq5jiL2ZjvsXSkhfZ_H6cEGmJzUa86sHHBOs9LfaJBm6kEZTahijsPUiWx9gqQ6gDRCD62QUo4tvps00hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWk2dvSzlrhmZvzibMaK0nd0Xmz-okPuRvZcIh9Zhah_4FPACPd1NBfInC3nHpy_OlHqTQf3KDJENwDjgQEdG88qYMwimAKLG1BJX2mgJhfk5tBoWzdq97MjumNieD-pBPAJIK8R2mBncDXhuLUBA2TQREK2vIoTxDepk9hyyKv-8qy82WoJqQ4b3E9cnI9QbeLJ0dJSw21sTDUZlkAFa6AJu6qSvz-ZL5CTw2zBFTQJJnbK6b-Vhtad8UNKlirVl9Vy33KANw0aPsJuMTZfu6xjzym74B64wOb3X6p9Y52xCi1sePX74_N7sR7508qRCXQZs_x9qTeODv4pCQ-KdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKx7fBICol4m4N4Mcss0coLWNZuOv4m0e8APfpAe9d0QOgGysA99ZTbTzeSO0rRlN98ri4sZRfBKXySStGcpUcgrx2wzZlWWPOUuWU5b3HAZ4y8RyC21wBtd5U062Y5puQiPkWd4ueMbk0Ec1foc9_Qvgp1U9gHbPf80_KElWd0G_73EM96rwGakqIaHdxZePEqeRvp0gP-Cbr1oDzyr4yYlwQUg8mHjkO8cD2jMdlW1TTYFR3mNFzN46_EETaksSv1Y6GIgtZMXCH6RW7KsFEtEceyR7zd-jvLz8WrdM-CiqE1Q-u19a2emSROqpYQ_8wlrPMrUowIR8q4fmjfrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaV6T3bVbvNtIq9qfYpT75dScYGzZ5ah24TBI_MOKgctObLK86mpVRobAjD8EwCXKzcitILBCSF0mWys9UG8ceif1S6EFLvLeuGKzapHnZpsSMSzXSssQiO_ASObaX3tfEO3wULefMgEE99RmBza3mFbJOYkaVn-WksZJznHv7OxCj7GDfWEBPFYtxAeo4aUe0TorDY-yhadf-4plp1GdZuesMYRiOXMoTqKSg60nP3GT62cIoD_cSCfxmVlo7OS_9vm1SL8Ool2OhhBSuWFgw4hek6n4Lp6nT5AvDMJK1ddbnkpyClfxdqyt6mwc6EAMtJKe3PB4sWu3ePv3fLPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/np-dambwQS4dcYH0EzHliZJNL1dIQSu0lmnZLqtK53pFFx23MYeHeMSljqpUgxA2PO2R-LkNI8krhS3pcqDWhtx88-AALs4gnqW6oe0b0fke3XNvXFMJo6DmnTbrmIMTBB8HZ69t4p9kdzF5VwpPDEwCdPDnF7prEScyikD-lLlSoQ729reS-JK3YKd4w8Hj1z9akwwTpM1CUiCdxX8cfbFz3IlwTDEjfFx0-q8k7TitaSV2WBZ7soyvEO-uQ_SCZ1RqLnNDjMq-iZJeN8xxrX03qcp0chJIMhKgcMFwTOuEpqdMr_8HwtQrhLLYtPRo2ofW2hi_7rAfQnscgDzLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kG9cmtfL3FFYKvXqkVOq7hmHuKz8Bz0caJtMpk0vwB9zs9GsomMuH25NGXGRT4pOm_tfaVy9Vf6NnLoQZHZZfPD3tL0d8khYyTkfJ5ELUHu671ytQHMxRFa8w4TbErMuI3v2TIZwQjfwI4AVlrwCvvpWEZX7x7rzgv7dgYbkBXP_6YAAGKNSa-Dn1VJjV41LGpkxGxcHyUKUvNr0kr37xHKfpgU9Am1YpL04S3YhM6bueEsKZrrG0_Vj9kW2ix5KrRU2wWEFdQrRL8_arm12FmOOpn9HlVYj20bMg3EOP4IxKcpbOSsz-oDCjQHaDGXrR-TRwUPR5Cd1803lKH9wEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم امروز از کهریزک هم پیاده به‌سوی حرم حضرت عبدالعظیم(ع) آمدند
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454486" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8f4de393.mp4?token=ia_bxSxoxoztMsW0nEavyBMRsTLnZUeDX_k7iOvFOyOKjTgu_K3yiDF54zenzBz51zDQ7y4zFs3XDxJhula4l6vCga4NmkIEdWyrpqvfy5mrKnRxjaMoqcGpXVVWtBUA_VLFJ5e3RS5gwprHXxZoJyCm3GAFcnyugjD2HsEpzK6XrzOeaTqMrRoRtSGGnq7fDDvNEDrrznGSkH73UfZqfNOutu6ExX6kRQXA1m0A3syc_A0k3AcGbosjiJ-GTvwTv9fjMWpm6EO9DZLezz3vpipWzMLXy810mDKmvJDWhoTqlVwHm7fsTI3_uGIvsupsRcO14MC8JTQcnzg_EVG04pM1gtLybO_ydZg7qPLVJ7zOzOymZzxSBpNtQ6vSnWMNsyjeDmFPWe2Kw-f1f1SfNFkV4q-4Zqk-Sa3PiM9TRRWuLbONiUjeXmUsURsc_fz5Qrg-6YvyTdinlicGENPKTFPPrFk32JzDWhhaV2SXE2MUYxMz8RHFWwHdYfQWWbKVyP84FxqOWtNeY9m150viZhXgrmr1nSbFaqUNE8Kuen8zcjhwHsgRn5NF9geDh8kl-t8l_tC4zW3CJfU9nlHxQVagiz32vIo2Cd_jdrqf3Z4qWnTTEvfy0y0Cx_0euXqzQ-o2i6_4-JMeAWxwYutvXgoQL0pY1nbQjIu4PJZg_hs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8f4de393.mp4?token=ia_bxSxoxoztMsW0nEavyBMRsTLnZUeDX_k7iOvFOyOKjTgu_K3yiDF54zenzBz51zDQ7y4zFs3XDxJhula4l6vCga4NmkIEdWyrpqvfy5mrKnRxjaMoqcGpXVVWtBUA_VLFJ5e3RS5gwprHXxZoJyCm3GAFcnyugjD2HsEpzK6XrzOeaTqMrRoRtSGGnq7fDDvNEDrrznGSkH73UfZqfNOutu6ExX6kRQXA1m0A3syc_A0k3AcGbosjiJ-GTvwTv9fjMWpm6EO9DZLezz3vpipWzMLXy810mDKmvJDWhoTqlVwHm7fsTI3_uGIvsupsRcO14MC8JTQcnzg_EVG04pM1gtLybO_ydZg7qPLVJ7zOzOymZzxSBpNtQ6vSnWMNsyjeDmFPWe2Kw-f1f1SfNFkV4q-4Zqk-Sa3PiM9TRRWuLbONiUjeXmUsURsc_fz5Qrg-6YvyTdinlicGENPKTFPPrFk32JzDWhhaV2SXE2MUYxMz8RHFWwHdYfQWWbKVyP84FxqOWtNeY9m150viZhXgrmr1nSbFaqUNE8Kuen8zcjhwHsgRn5NF9geDh8kl-t8l_tC4zW3CJfU9nlHxQVagiz32vIo2Cd_jdrqf3Z4qWnTTEvfy0y0Cx_0euXqzQ-o2i6_4-JMeAWxwYutvXgoQL0pY1nbQjIu4PJZg_hs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحید شمسایی: اربعین، نقطه پیوند دل‌هاست. از ایران، عراق، بحرین و یمن همه زیر پرچم سیدالشهدا(ع) کنار هم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454485" target="_blank">📅 19:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9alB6fQeOFnZvHbiP8YfEjqq_8jY1qjcppRET2fBb2lNb1PRGt4xRdXUxit6esGQECCI7XnqTLFfFne7EolRS3ZfFwSA4AFHM7on2sgJAR8XtKtT9iB9pBndefYSIiGek6S4l6I50yWzqM3bF37grh5Idt5J8vzM6gQSvpgMuXQtJwtMuucKoXs_nPo4fM0oIptmz9-zF_tSgx3iiAptM07Xn20QX4VjxySobtbTJdqFy0OXyr33roy3iQPq5xK-zIdq62hdukiLomZGbOTwkXjoSfGgn9hvTGs_59UzwXMOLSj5YT_Qg90nimuEbbvPnxmD1CsfnLyk5BDnAh9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtHJ_IrYa1QLEafq9PbSmQLhWo5HGezlkIUYMCus-3oUH_Sn4Hm3Sjn2PIxAuxEWV_UvY2jOpJbmzLoIBggjzzwByrb0iWTChk3VIIApni-85rT_HJfUuV6peHTcT1JRdU4WRWxHkA8AamiE4nXEfGwAcIx3-KDzcLHk1XnyuFUMz7yDIkMkxyMD3MSwjXVcY4HFsigNIVPQdRfMv5dsWnjH1P1dYd7WH0rR9jpyRHMIzxHMjgyMwj3iFHfAG6IrztSGUcT7dS1-xDeMkebeLQR952yKVhO8ZO47i2PleCp2uZhHc3WuKWipLHdHhk9HiORyNk8xLc1MrR1WcZqntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taFSKbacPHcKAuFDS8s5VxU-E8NM7EH1-aYLjwpdF3HPg-DiZPj1Lmfd2iZ466OJvum2SnGSo-QZmzEoeE3Ha3slQ_yZ2-GdgGvthhFlcTmscF2kwDsxo8FCbRKvnB9kRR2s6LlQblczwqA5Sls7Eyuc5ev4xMOrU5EcAT5N_LUjU2qysCIYQR2ZTUw-2y9jj2wf8E-Im8C3hF1JKRJERLQQiHqDmvgohqpIMY6FjdyiZKiZRwpCjsHCturIEpEO4A257KVuuSQkpTCY2gjygfiI0gVTpCEQrxmzUvx5jsoSbm8NUMP7kxi5f1DT3rbbO8jgSisImWaYIQz3n_6oUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ruw1fsqWLKDauNHDwn64obTIPaJy7WyxQdIpb3rjoU95_FbaDv4ARNuCorVJaRmXsXhDOw-20fmhqLQTcUVxpaAPtSTDEfTJwTKDCFql23Wmjv3h8G0ZwBzeTr-wDT8enlvrGj_X6Jdpe32roQGuMIrw_I5n6KO3kTjVcDXXWDPT26K4nK1aKDoii6xU5SNzCmMuuP8gh0MgwAo3khS7Ky61ey68qtVEuMDQUPwcs0n22-XMzin4oyxV1V4LFz45nrbppo-9hgzcLFrHrXnR-g4gW-n0V6K_4UMS3EUS5qPVUd3qjIQDsTKCOWWJT4A2KA7mOn3_J-uJRDigQDUA9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم جاماندگان اربعین در گرگان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454481" target="_blank">📅 19:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6367a5b7.mp4?token=XXNCJ9NSJIt4sah9HD_Xag2lE0tsu6riShggJPWEsgPGfoMnPZkf6W4D6gRqPJ-AAo-fSdRbNc-dSnERGkW4HTDhxOoMG4XCsgyxr0OFn7MKWQT7smfjdQf_ByX0bd532zgedxAUozIZC_iionyPUWikNCH1jNWSHaMfOR1wSxmbh7rlXmWb4SLhNUahPSfzMtpu3xFc_IxAkB7jki9r2hOPOb2ZaHVmm2Cppks3LFvRd0zzEfJW9SQlvwX3ZoRHpPBWhQGtkN8yj21I1bc1aY-l_elHEtul-Jxw925nce85WAbodEZCbN907nq4xWRRIAc8Dd8JYlvd3arLpoyx9nMjYwXubFTLLu8-sy97WjWwUa9BrKo_4mTcAJ1q9-irf47sDeqydYODaxDS6-bFVT_Dmq05BBuPMZBDLEBhwDdUhE1SzIZOqG5eYCHADNvakMxUNElpAZgYZMmuFDZYSYOuuiNLflnK1eRQUZshXGHbJ5G2URkxuAssMoPKqjzO3YAtnABFiEbT6xCHv0UFLn031S9zFpnU6YnkUtk9pXapP8vXxreNa5mz8IhgkwDO9f0oLdHWReuBjR1MFq9U2W1QnvexQwDVv3BId-qe9t7pUWzYLp8MUvr-QtcBtoTnz32NkXkcfWG6QEgWoCwa5fx5sn41YHZE6hS6zd7wV1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6367a5b7.mp4?token=XXNCJ9NSJIt4sah9HD_Xag2lE0tsu6riShggJPWEsgPGfoMnPZkf6W4D6gRqPJ-AAo-fSdRbNc-dSnERGkW4HTDhxOoMG4XCsgyxr0OFn7MKWQT7smfjdQf_ByX0bd532zgedxAUozIZC_iionyPUWikNCH1jNWSHaMfOR1wSxmbh7rlXmWb4SLhNUahPSfzMtpu3xFc_IxAkB7jki9r2hOPOb2ZaHVmm2Cppks3LFvRd0zzEfJW9SQlvwX3ZoRHpPBWhQGtkN8yj21I1bc1aY-l_elHEtul-Jxw925nce85WAbodEZCbN907nq4xWRRIAc8Dd8JYlvd3arLpoyx9nMjYwXubFTLLu8-sy97WjWwUa9BrKo_4mTcAJ1q9-irf47sDeqydYODaxDS6-bFVT_Dmq05BBuPMZBDLEBhwDdUhE1SzIZOqG5eYCHADNvakMxUNElpAZgYZMmuFDZYSYOuuiNLflnK1eRQUZshXGHbJ5G2URkxuAssMoPKqjzO3YAtnABFiEbT6xCHv0UFLn031S9zFpnU6YnkUtk9pXapP8vXxreNa5mz8IhgkwDO9f0oLdHWReuBjR1MFq9U2W1QnvexQwDVv3BId-qe9t7pUWzYLp8MUvr-QtcBtoTnz32NkXkcfWG6QEgWoCwa5fx5sn41YHZE6hS6zd7wV1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روح‌الله رستمی، قهرمان وزنه‌برداری پاراالمپیک: داغ رهبر شهید از سخت‌ترین لحظات امسال بود
🔹
به‌نیت ایشان در مسیر اربعین قدم گذاشتم و امیدوارم در همهٔ لحظات زندگی، پیرو راه و آرمان‌های ایشان باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454480" target="_blank">📅 18:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌  اورژانس تهران: حادثه شهرک صنعتی شمس‌آباد ۱۸ مصدوم داشته است
🔹
سخنگوی اورژانس استان تهران: حادثۀ شهرک صنعتی شمس‌آباد ۱۸ مصدوم داشته که  ۴ مصدوم به مراکز درمانی منتقل شده‌ و اقدامات درمانی برای ۱۴ فرد دیگر در محل حادثه درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454479" target="_blank">📅 18:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454478">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3db77b531.mp4?token=bGqyfxUV8E4SgyiVauVm9AvBr4ovm517Zu3iSeYoy877ft1c0hZDgZjvJoiDSaEhud3COPpntRKB0mQ5dboP5RLqJlRd0vxRWv6r74AUUKDWz7NE45D3EptrXkx1xbIAi2bc3UcNzUmDI6jGtTxZDU1NU5rMwKPd8nxjDGq3wxbigtYGmXdQchPEjoLJp94lzj7RGDeiXkerTEtFBj5fjw31lMOdQh9D7TjrlcMZixVzC1ynhiPVNx3HcuDXa-XoCMZ4SoTHmYFxK8W_Trjhnf32j91PlVDFu9wFeDq83YVTUURNY8e2z9blN4e0SpnT57diqOX2Fc6gIY19JW9UXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3db77b531.mp4?token=bGqyfxUV8E4SgyiVauVm9AvBr4ovm517Zu3iSeYoy877ft1c0hZDgZjvJoiDSaEhud3COPpntRKB0mQ5dboP5RLqJlRd0vxRWv6r74AUUKDWz7NE45D3EptrXkx1xbIAi2bc3UcNzUmDI6jGtTxZDU1NU5rMwKPd8nxjDGq3wxbigtYGmXdQchPEjoLJp94lzj7RGDeiXkerTEtFBj5fjw31lMOdQh9D7TjrlcMZixVzC1ynhiPVNx3HcuDXa-XoCMZ4SoTHmYFxK8W_Trjhnf32j91PlVDFu9wFeDq83YVTUURNY8e2z9blN4e0SpnT57diqOX2Fc6gIY19JW9UXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حال‌وهوای متفاوت سفر اربعین توسط رضا قیطاسی، قهرمان مسابقهٔ مردان آهنین
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454478" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454477">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/454477" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454476">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f0073b30.mp4?token=jl2flf7bBkAOw4ewuupyTBWUgCtq9rNhRhoxukEPcp3mizZM7ka3NhZA-ccfKKVjIe6zfaJlY1vaAqBFx6mjQDUjK8Bl8P67oRwXjggAX7TuVJ13fir9gmkr7jMwktDrLg64vGYW9_JBG1Nj0ZxmKnDCZXVzIHvfmY0hMET5s5jgv5XTgxLf8H76QRG6cqFJeQi7HnXuo0RTc-2vkUv5xtq6OBa_n5Fht5Edr1xPqa9XkHblbPrj7hWNp0t3a8yksZKZ-41EQDRanp7-Wpvo2PhBhzu2rRpGS6KpQnz8zDZf-KEaVoj6cR6M-zvnGMbaeHOKsIIzOf7dWK_SpS-Y7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f0073b30.mp4?token=jl2flf7bBkAOw4ewuupyTBWUgCtq9rNhRhoxukEPcp3mizZM7ka3NhZA-ccfKKVjIe6zfaJlY1vaAqBFx6mjQDUjK8Bl8P67oRwXjggAX7TuVJ13fir9gmkr7jMwktDrLg64vGYW9_JBG1Nj0ZxmKnDCZXVzIHvfmY0hMET5s5jgv5XTgxLf8H76QRG6cqFJeQi7HnXuo0RTc-2vkUv5xtq6OBa_n5Fht5Edr1xPqa9XkHblbPrj7hWNp0t3a8yksZKZ-41EQDRanp7-Wpvo2PhBhzu2rRpGS6KpQnz8zDZf-KEaVoj6cR6M-zvnGMbaeHOKsIIzOf7dWK_SpS-Y7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ «یا لثارات» در سراسر کشور بر دست جاماندگان اربعینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454476" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sETl71RMM-5wWuHDspf6If-apuyVeeAx19WDkNStoDNNm8LjxMtQjh6OgUreYoTCwnIjzngVE3Aewtr8Pmt3guCTaHOG7SuCLEqn8zuNUe6xROpLS4Az-AM-7R2BRdZ237j6h6IkFL3K16R6OuUwS4o6sdo3kDjhLblSbNMhLw81G-nAvn8QkIORIlw8WID9703hRpueAR4ZfB_pv3Y-3kyGWimBeIvuTrLhZCW4Mo2_U-SmddpC96u_-PaI8zBCXQAcMK-KzxiG40huwDJ1pDTMJsWrV8aZv7UrWEKnY1vE1XBE9RGGwEfYY4UxFN0iHNfBp9qPp9k6dNzPb6HvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0E6OBL7o8G4vqfNzrfAY1iUs8v0_HLDkwtv_jQTnd4G9Tzzvf2bukIq0LBW35cmiWYGQHXVMTPCYCl4QdJddaiErmTyhmBq6JHxoq9COFVL3hIZo48lGVa8VOnchcehdO380LiJyDQQ42J2TG77xGNzL5y0_eRMSoHLQxIamvmcAk0BhVLFg2jfjZsVQBa6deK2Xhh4utObuLBpMBXbNVrkP9hLlKOP1d75saxxVQ9y-BIwqt3rnbfJzCalW8rjxERkRkyPsMb-llDQiKqbYfhsefwg0z7nLT_E3-5a0OujGDrgmam_j3fEGawhEbwx9uSapw9QzxO51YK8Oif_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRkvSDHKE96C7_IqSWiyVYdxW-z3L2IEKFzGXn9r7Z5iGirNHcenIzi8zYwaO-4xQhOZ-Z-6iG1EBTgYkzFj-tWOHWr0PifGzfeVFTVMRi0fThNbrPuHvJwRrmEOJeojW9FET9eOLl4nYYorfycsP9BvSuQ74PvH88pSB4CMbvrqURwm4gVAJKoUkdgUucxiKjlVt_77285Bkt-3XV51sKBbARK_PZXVrwfxTvnGYi9OsLk_ZHJ8IQSe9UVpm848BGRn7NWKxX92cdAuDFuOTO95ZsqJYtDcCcXjTAppA8pK1SWjFKi1PpAzLA6TQQtlY08kavD7x4ywaSJdqMX-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMEN1SuES8u7c2kNkDy-3nv5HTfyHJJK8hJNxUF09g0_2LsUkskVvXuA5sN8_gpddwe8pFtmq0mL_fNCLYOsNcUeWcSJKL0vzx8UTSz2TFxeej_7wsGpaFweCjETqh3OWNvIOgINUjf23Pkm3V7mM4xXGIagTBp4d1yDNoHc8bG_VDevyB-mc0f1wdZwszWaLhmOMF5PQMF0gMf2PLyli-UtQYZM22jiCTYxdx8W_bbKKKBdrSXVRz9OuDPBUan4ytE5X400bLCR-h12jBCcP4KmU2EKy6M-FczkQdQISUkb9k533wa6hM_tPZXHcee_Z2BFqqUDmxCseor5Qu07HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1w-iflcxBtud1PTpRXp9LQmNDFp_zGMgEnOxF7oekp29WHWugtqmGmTKL5hQmkBQ7k-b6qQOJ8QhjD8Hxjs_pB2KgI2sYPV7Ss1lPCKhMbBvgBWBYCSWS47w1gO1I2YZs2SIUdUKNWImCW8m7Z2Deljd17YRIOvooBAxF_IZxyeSu7XdGa3GGzkc60xzQhPhK5f9dFSokXIRgDRGTGEqnFCIEN9zR5zXaTVwgvCpKohuvhKSG76qVR4Fw_JmnZ0hSkf8WL_x24t2zdbAgoKA8t80TWUbe6EUYWW4xoFALRDRj0odXIjWwT5wqjA9e9WziUhQAtWem8Fznn1kqZqEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم جاماندگان اربعین حسینی در زنجان
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454471" target="_blank">📅 17:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f59293cf.mp4?token=AqfaqAgQpoZV-NW1_facPgv86QXsONBSopObUAUwbs-cUgSUwKLf6vcwLjLYBJpo8hEwoeIhHaQ-gfak5G_SaaEQZT_0NYZeVBIAAcRsr-9Syi70tW6RpNRCBfd7Phfbvm17F-cAadI_Rt280amA2iD1y2GP6rfV6T_XKO2RTZjaZ-WTdQcsEKBK9NNwbRI_3sN9qXtb1lwnYj_xo-AjNAplXCDFShxtBCvs0akI1Ko4CTXSiwqwNjNpjnBCPY9_ATkH5-qX0RLWCNURIuMauVlTWIM2OW1GtKrKE-t8_OV9ngKi6fg4g7kGScnGNFPGCJqb3f-Ln_CZC8aIsaZcTgUaogH_O88Qm7ZpQ9x7sE_oz3IF0IerVKDtnEtBVw7Zwr3Y8fzvQQhPf3WBNu72A-ZJQr1wavz7HcVoTMtD9_5ZXfbHov3DTfUajrFbIbqU9TFFt_fFoqzLCDRer6B00E2bOgJpFR_nrWX0hI_KbTjayUNlOpcEAA-I9SDAvuP3V9We8DBwvgV5q1Y-dWz9IR8Br5UZarYBzIfXhrMEtQ4ZUZTvaaIF-24ZXmpgh-L8jlV49JXLPpdi7nF2f0SSvF841xUGxdZJF1KeXkSeBiSx3C4Gt4YR8zAOOGr_GnHSoJxh7YC7Q8uAPRihJqqPWnZfcfRdN4LKx6ZTPD74c3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f59293cf.mp4?token=AqfaqAgQpoZV-NW1_facPgv86QXsONBSopObUAUwbs-cUgSUwKLf6vcwLjLYBJpo8hEwoeIhHaQ-gfak5G_SaaEQZT_0NYZeVBIAAcRsr-9Syi70tW6RpNRCBfd7Phfbvm17F-cAadI_Rt280amA2iD1y2GP6rfV6T_XKO2RTZjaZ-WTdQcsEKBK9NNwbRI_3sN9qXtb1lwnYj_xo-AjNAplXCDFShxtBCvs0akI1Ko4CTXSiwqwNjNpjnBCPY9_ATkH5-qX0RLWCNURIuMauVlTWIM2OW1GtKrKE-t8_OV9ngKi6fg4g7kGScnGNFPGCJqb3f-Ln_CZC8aIsaZcTgUaogH_O88Qm7ZpQ9x7sE_oz3IF0IerVKDtnEtBVw7Zwr3Y8fzvQQhPf3WBNu72A-ZJQr1wavz7HcVoTMtD9_5ZXfbHov3DTfUajrFbIbqU9TFFt_fFoqzLCDRer6B00E2bOgJpFR_nrWX0hI_KbTjayUNlOpcEAA-I9SDAvuP3V9We8DBwvgV5q1Y-dWz9IR8Br5UZarYBzIfXhrMEtQ4ZUZTvaaIF-24ZXmpgh-L8jlV49JXLPpdi7nF2f0SSvF841xUGxdZJF1KeXkSeBiSx3C4Gt4YR8zAOOGr_GnHSoJxh7YC7Q8uAPRihJqqPWnZfcfRdN4LKx6ZTPD74c3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌های خون‌خواهی امام شهید در راهپیمایی جاماندگان اربعین در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454470" target="_blank">📅 16:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nyw_cYzZ85y7uzlp7TxnaUBrXU8htqRkYpbLXe8TD2JiosCvfHJuIfDcyVeyXk1hzfKeQcIsXsEitLCrfv9In92OOWZ90chHxDlCIR7xHRbPU7rgfP5TUCDrl6Xan2Kf6VFSjNS5tQCL__zHcRXAZK-Try-uyNuLKgeUmJV7toh2fzJDv4ooaMAU44k0SPEtY3CZnGfy0F1ecyJB76ZaJwp60lLLV5RGE7uBUpG4SGj5fPmX5nqN-1avIB2itASx8bZX9P4jCy2053l9Ee_nAMv1N62J9TvU8cAql0cSCvQWN0m_Dcs-X3HuA7hPqMNxMriSzvFx3o9ZCQGkgVsH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار تشرف ایرانی‌ها به زیارت اربعین، ۳ میلیون و ۳۴۰ هزار نفر
🔹
رئیس ستاد مرکزی اربعین: تاکنون بیش از سه میلیون و ۳۴۰ هزار نفر از مرزهای اربعینی کشور راهی عتبات عالیات شده‌اند.
🔹
نزدیک به دو میلیون و ۵۰۰ هزار نفر از زائران پس از زیارت، به کشور بازگشته‌اند و تردد در تمامی مرزهای اربعینی بدون مشکل در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454469" target="_blank">📅 16:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
دلدادگی مردم خلخال به سیدالشهدا در روز اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454468" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDHYGMcyy2hQ90kNkcV2nIo4s-obvrm7pW_6HUf1x5EiPYi1_becI0DImG7Ct654GzFJex3N_zD5dDcRM5SGU90AaT-oY20stH9_ztjV0DRPGbn_Vaw8U84Hd-Yt0jmigPzCantPhIjqSos2tnzy_Bj0HtYAwtev2O0PzLaN7oMhgmmYOKX_7I0MhJjrpAGjUx09g6d21RdMuxK1fV97JzQQaSbXw6mbRsXZULad7j1MuaaA1qo6gX3L3IVPKEr-JeA8145xrj2Ikytb1tLluW18sHPKBooO2ttekAo2b-J8zbsDEsNNf0m5vITlh-X6etcJiAZfhAVE6eEXdV7h3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوریه: با حذف از فهرست‌ سیاه آمریکا بی‌خیال نفت روسیه می‌شویم
🔹
طبق گزارش رویترز، دمشق در مذاکرات به واشنگتن گفته که به دلیل حضور در فهرست سیاه تروریستی آمریکا، مجبور به خرید نفت روسیه است.
🔹
طبق گزارش این رسانه، دمشق موافقت کرده که به عنوان بخشی از مذاکرات خود با آمریکا درباره لغو تحریم‌های سوریه، واردات نفت از روسیه را کاهش دهد.
🔹
رویترز نوشت: «چنین کاهشی نشانه تغییر عمده‌ای در سیاست انرژی سوریه خواهد بود که با وجود چرخش سیاسی به سمت غرب، به شدت به نفت روسیه وابسته شده است و این سوال را مطرح می‌کند که سوریه چگونه این خلاء ایجاد شده را پر خواهد کرد.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454467" target="_blank">📅 15:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3xA9rRhoZlda_l3BorMn63h4_yhUfC2B2ZcAS6bRVF88fIZj9mNn5q5uD_PxQhwi_MejXy2klAYGWDFTl54_-4zPPz26BypToSBHRAfl_6f3of6LB8hA4-FhwFTJz3U2pGUVgzzwPC8mCp-wevf9-ga8Rw79FeA0LMcgMdpIfSLJD709neLzv8ngULuyeRQs38p4sIB_QFZXHltlij7gcRbCrvB3rBwJ75OXCnd5MZn8Y342RBhLGdEOiwU3SYIaedGkPaekZvucokdPBOXToAKvrZeeMMPgOshAtQeOPWQAhmrujlfO93Et3Cc9U3z0rdI4w0O7bZ7HG_medcWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMj_TI6SqjSZvZrSAcgxApj6WQmpc8xJcQQpoaM7N8C5YVMnFgjdLYMpUlL7pCWOrjYRdkNs6FuCIV-E0LPO_Vb-vCHAjmCJAv7zY8B6NBBeK19MWoEkYEMUiNvGUrnR5-9GiGkhCgBxzWBz0aepBh3PXLbqeAiFx-rhGWXlZIbvovz2uwHTHXYNaeNqHUihz3pEEumjk1RYE0I85N0NMpiDMFggFG4lNkfkVFu8MDlPGw74UeOsT43Q5nxn2jW9HYvGxKTsfvn5I1tGihsr44Ykp9JiGYo_VuqvewmvmDRSRvl5FcF5cvGPDPRHdEaHOsg1obEQ6Me-wfPCk0UxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okqeXPXxnctUbwZSpMd6SUT5nYvwJFLfNWBix1D_F0JTGp0FzOHIUgx39uq_gXW5POOEBoZW29mfdLQvKs6GQ8ngrjZFuBhWJUqazBoJkF8VJK2RUmA7zNHEKZmtqX_Cy1wOrE2KGEjvGqozBQuKiFU_tKK1sFxkSDnN-cFrzwZVZGQLHC7eCDD6rDklLecV1xC767y_tBmbT8TMY2kEW9J0NIO7PgexZW6LD2T5VdZ6ptOIPllt68uTzOSikvdu1Mh30psUscU0KUj3jJPAD-Inu_nqxPF9e4kFgdBRPdgSqFuIvOU34yJKATB_5anDKBny5zYSlbVTmrYG7m2qmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmjauhA2dG0skfoQkyptSGZa-qoBZDk_HLDnjMJSULW7iqVlemKMHYbvqqOpoC5IBzvKolT8nocVd7iX3UjxLLQbsC-LDu0jUB_Ov1aDbuSFwqgR1xwpqtJSwEoV8ObAKGWayEEaLsyMryYUJkGn38q_sVDb-3oimQK9FlrsrCmiR4aWqg68h73oVvUWO-Kp4uqHfmhH7_-slyFbIGGqdcCtlvBVmlZsgMIpQ2Nv_Al2lsHCUAvdJkzT-5F1lKZqEIiKHCw1_eyMf9ijv4mXrp2y0Xmi1VI2lUF2o8xutGOZb_SzfeHLpRhLkw8-hX5XVDroPypgZS1rVuEuIEfy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd1eeJTXRAw482dCI_BrVCAVskYTYk-H4urgph-l4l9bkmyyjZtZAIx16cLyWrMj-__zGH8ORsyCdhAKKmue28nCeTcr78mDWW87fqXxOAFhIlusgUqLgj5n4ksyD7KmxGD24B_jTB0xeR84ooXh1tOWQI6vIL2SbjaFz9Ie5RJixQbeCW3c-qHuhsIS2dUjJFVARFhwKu6dblAOIQeIiaeRr9mp7EWsEogk3KCtE_GKvzEVIUHlXYGMTalEdB4CtP5JudZLCpBcNcFwmDzEpOKbd9DPDK0s18o2y1_7ZVYoWabkQ1dqzu4PTNiMWpbXlGccNfUc0prnuzDKnQHiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQ4sO_b018BR63QEvZkxggjdMfsaKD8GmpX4_6xdjf6ve9fQI2p4b2Hw5xhBpqhMsGVthQnsAI62xgGusymEZmoRXlE1QS9Nqa-lgk90DkwtjoY3mT5YOR9LpwFZ_DeOEQe5jbzFOVclH38hcPEXkfisYWN9cXhcnJkh6D2iQhS2A-r3colvQnXHhyo8IodypijIERsFbn1_cpTmy5PTFMMhqj3cQTuTbvwsvC6dYA85d21Q8ZXyvo46Sf7msFUNDmw6DuSlbuDEnyli51TM48joHqeOZae7S3lP4jDBhKZ_FG1Ghng_DVdhl7-CwHXJJPi5ERj6c_S5vk1_GZZ-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLzbomdAdm7SQuwfxjw6MtTaiLLGoiwmtekdAZLAdBbDR0zUllNC7oHKa_HJiiaIIj8VjIM3DQDwkP-gWiu1AZcbYsKCzkxLVE9HCZENco1Ouq8mTM4yJueOJixyxZ8vVDVWK4j05JOuuUFQfqITMRHoecfndZsJzx46rTkZe9LPVkM8fHvrsI4gfnTfXfxuH-CYUcfpjwRyqMu89uJze_4y2StT-eENWTwgDtJ5FH_gzfI9F7irj8azc4jTSMD-x4AaM2XP538dNSeFwDhATG7MHUAECwSjIofzgs8Y41bnwd0aedEZiQTBYVAG43XbhNGX-pVZtocmkF0Px2dG7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیاده‌روی جاماندگان اربعین در تهران
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454460" target="_blank">📅 15:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03ecdc740.mp4?token=RsneujaUn_ftc68pEjvMOzMKhUe2Gh918r1JgKEskN6jW_CTiu9nxrmWpr1E1GYWolIoTwwnAn4cn95cNhvoAXt1xGPwJPMcp_eNbQn3JREjnCE_XTlKfm8N8ACrArd4AwtvKsCvSY83sqwGP3bKpQiOKi-0nTPlMsk1Te0-XvT6bKWQiOkg9oLRFSw0U62gXWx4dE0FvMSmbqDDYo6spQ9m1IRlNrajAewor-8Wy-cRLaI9ytjSBZBsFiKfdLFIAuEmTECSGe9qkJ2_5txKuJVqgSeWlv9VmaelCo47B_IgUZQKb6PY2PQsiY7V8-KG0Df7murW5V92PQ_JV-qDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03ecdc740.mp4?token=RsneujaUn_ftc68pEjvMOzMKhUe2Gh918r1JgKEskN6jW_CTiu9nxrmWpr1E1GYWolIoTwwnAn4cn95cNhvoAXt1xGPwJPMcp_eNbQn3JREjnCE_XTlKfm8N8ACrArd4AwtvKsCvSY83sqwGP3bKpQiOKi-0nTPlMsk1Te0-XvT6bKWQiOkg9oLRFSw0U62gXWx4dE0FvMSmbqDDYo6spQ9m1IRlNrajAewor-8Wy-cRLaI9ytjSBZBsFiKfdLFIAuEmTECSGe9qkJ2_5txKuJVqgSeWlv9VmaelCo47B_IgUZQKb6PY2PQsiY7V8-KG0Df7murW5V92PQ_JV-qDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ردپای عاشقان حسینی در جاده سی‌سخت به کریک استان کهگیلویه‌وبویراحمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454459" target="_blank">📅 15:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5b074e19.mp4?token=gN6RzpNMguT_cBH_0n_oePiLrOOEUGdTPQsCYB-8hxRBNGCNVuAupbWlT37wz4dVU4ydAZYHf-z5T2H7zEUkkJT4OvnzwIIQUbR7Y2FHVm36XOG-YJgyvMZZ006R9GBm_jd-ELyQ7HRSzt_CDupyMgeWFAnqxjaXQ_7bqoKw6UnN8CehcDOBWi0G7gIEqY4_OearixtAEcyOI2htXmLUkHWartAWAQfjUQq0ZeCANP559ZG2O8xwM8wqhPz6LgnQ6pNl775MKHih8_CXXgQ81aIKPLOIr0Vlz_lPlf4s83uAeL7knmNUcZiJ3fCru0BpZ3TLRsIBwrKWN3MXKoyFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5b074e19.mp4?token=gN6RzpNMguT_cBH_0n_oePiLrOOEUGdTPQsCYB-8hxRBNGCNVuAupbWlT37wz4dVU4ydAZYHf-z5T2H7zEUkkJT4OvnzwIIQUbR7Y2FHVm36XOG-YJgyvMZZ006R9GBm_jd-ELyQ7HRSzt_CDupyMgeWFAnqxjaXQ_7bqoKw6UnN8CehcDOBWi0G7gIEqY4_OearixtAEcyOI2htXmLUkHWartAWAQfjUQq0ZeCANP559ZG2O8xwM8wqhPz6LgnQ6pNl775MKHih8_CXXgQ81aIKPLOIr0Vlz_lPlf4s83uAeL7knmNUcZiJ3fCru0BpZ3TLRsIBwrKWN3MXKoyFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا سلبریتی‌ها جانیان را ستایش می‌کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454458" target="_blank">📅 15:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWutIkTQj6OXu5UUvdwl8dXIp6uWzDuUR65ZFxx6BXa7hYbjyGpH0QIppddKEnbnJejuKwS_3F_C_qXaFADIsTEN6d3fk9WtYEPlC8QjYIDKKQw5fj2K5ADrtwsThDuemrSFKYGzhN0ZpJvhtpDnByrttvpdcg6VwxsbkTRfePaY_buOZW94P3VOcrh6dopfAddqULTWtE80vQMOiWvDjfg2YnY7NlYrAWXlH0n7seiCiTbGW06yi0SWkaXEjaY_AC7-mi5y4KTtevIAzoS5I63qmzgu1RRYfzevyHgoD4j3iYlcJl3pIAqA96xN-iAP7qcmVZh4Ff2W1apELoFBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDYel62hbUr2VCpS09K8U1TocDDEKGC9fYLv4gqWq4-RELgp-089AbU-II-0rI1ijlwWKJldBcPME2JMC9nSlED-90TmcOdz1yWnk5fdTnw3b_81jvTbH5-iiwrCKz7x1qd6b8w7O3qGIqLp5WC12rMGf_C6vYOP4jqSuqWD8QFmaqb14iI0x2oqquAZIN1565D07ubFDsH78iPZdfEwOBfn8EuQ5aqaNiyFp1wnMOxr12EDymDsWFfvEkJaGy3-pq47106KLIfzSov-n-65nEkXj8_qjkcY9rGWRaNQSpURhzG0dtqWTP5sI7cUYpxI18-tiJzB3jxPGdlPB6iyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9bQZsGn0LmdkS6bCk4UpNhyy8VtUjw2_GAPHCwQW__toGJf0ve7V2ReOvp-llktqAs2SJX5wIlyoxw61QFVdLqk161E5yH8i0Ghihzy5gq2DfeK1-1wxezfssCut3ZdOe8o_JqlL4Q_q1TnLkaeDYUYIwHfTyaL66nTbhnYbOXJQuqCnVObbFtrb13nHVovVdjwXk34677HW7dRBcnlbpNLBaP5mTwJIvfqvz3LUCm-fy326eDOV_v1jYAnJUSAPCAYoEXyumj79W3fAd3am9A0k7DRJV7M0mN5GnCMFHHogmqCu38kWk8zyhKQtuqpNNpIw8f8Dr6dOKbWtE6Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNbGFKDRpMMcVzE0GMK90Q4Isia71E_ScBbsLK12Q09Sc9W7uPFwbMxb0UIhBvAvt0csLsfUhH6wLIi4LaRH8L3Ro0Ual0AX-c86KD1iauHtNOne8bcMT8qNK8vWUWICjU0ZhTmWjDEOjn-JIThHzB1HSI5tixwpC-GIXUJ1FZ-noHC4lgk8J7NYAOZgl52cdeWaslTwdfvSquNwtWw8BiGmd1Gbq2ihpJSKRwNMOCQCleZapleP2UA_ehY2xDU_HybHcxWDK0XlPCeFUHllAc-Yn40yTtNe38Zu4shFT8I8ohCkNOTA7iIE_uZIVCCdOrIyz--W_IP0kVCcDZO6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aO1nrdW8mlKtVbqCimKUQC_Jld34A14jsLCpZ0SqHhOvNSC8IP1Tl6jPRf0Y1K1PJJG0cG7c1Az8BJJstyPdr8jC7vlrwTo-ZnWAR-a3w9GRsJGCB8C8Vv9VIr3E0pSAWPV7nxea6FM5NAwnJxwwfp_7H2xB9_dRQHP2_lwxs_XIvu2WxJvL7Emg4tuiK2xvvU2qMxDDCNKRqpQ-1Xp4Qkh_Dystj1mYxVcZDxfUILTsg6cusqA2JQqdcGhYqskxIF1nxEntar8hMNYHtZUA42-K8rzIfH1Wk8BqOWico_mlc7aIfhJXLFOxo0zHW-nrH3QySyTNshYuhK54i66gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9jhJFZi2piVgJsFpqPS_mOKaEyswvx3hijBuFE9XiMxOHJEvoNKQQfXMFZt_PCGlgv640e4exeNvX6ep4oCErtV91fDsCX9ZO6g5hwkxBeEVMTNERTtU5q7EcRxDmcDZt3KT1ce_xQjCkM412losdT9D0s600U-cleCSlhIKuV6_dZqu9UR5G2aIMGwXHjVA9ggnGCXkBHTDxCcmuIaP1VxqyyXyaE1lZma49cq_maeZy42vYnmxCRoK7NdmrC_HjYPI8JYGeqI08nii5ARizz8rnhd4UUJA23DEjY-LPYT-fyE5_fTiiRPZTav6UPzuDrODzI3udRIC3NVTyf_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zx48FyQaEEy__jqYCKLGwW5wiTI4P88keGJbG73XFCIpznl-TSjjDiRjXwD_uA2PbAO96dFonb623L_lPFb5apr5FzJ7LFmggJEJs-EtMsh_iLt8_qCexemxKy4piDX014h6KWqakXAO3hw3vvrlu3XbPgZQG3Wy2hVlSxMSqxZ9BeYPB1A0LOaKssTJvngDl-rGwkhu4EIG0T1QTJYMomjLvzeMo9-_vMq9ndHZWfPa_HKn2OrGGBVczqBwIiGZgEGcGWhyo4LUB9G9LmlouiTk-X5_j-22-JLrkGVePUXGqJ4aizwQuhaeXElhRkPwhtTPcRjzPKhcLP6IjI3x6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UG92b2I5WQrnPwQyPDVVlt0G-RGUJohpQDb2rEEsxzsUvT8X7pS01OJJOGS_K5sM0OnzDHNr8vV_JcG3ippJXDuxVTGlO0e2jic677tbenXqFO5ycbCkqm2v1CLuekjvR9fwkasPX2G_Kd14srDu6zKAPQXXHFFVBncSN6ROgZXsCfrXTErytajd9Q0mPu3kUd1ODXvz7_1TBG08j2BfDWpdRthZq1dYM7GXSJO6vjFI7EocYruYN0_Njf-gGbV1kS0CTeP9rQkixxqbyhFj-mt1GCH79gNBoPSBGgd_bEvPJrn7pYC1fWilSI3UZ8y-lBh16mQ35-A4XIeWsWkg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ab0lp6eQkF3TwkLvavXkg7EIcQXTKr38bp_kjqXDaFeHGJYPKOedo7H8C1LgSn3BovIlnRq0MWxyFQhZ_9cXtoJStyDnKTo7iEum2Mn03u53utxuma96XkjplgBS9q-YPPyq0svReKKzOX8zYpaP_QEPpb4lHXarXufIfMxXlF3MU7G2J92pOWFp18hNM5rwy8B6ycHdMreMamISo8IY64OD3InhmxGFQT6sIMlyv8irhn_QjM6Ai6VZgVfldxBhzUVPTs2oFabP0bp5bT85oSPD5nVPfu66rZgqHjKmE68lFcr_DY4yjQCU3qWjqH8qydJZ06syu2JFXbnDWmPXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-AyjEcsqMgpt2SqIVa5OB7mTdY9UDSDUEZvtne3Xq-oFWLIr_biBSJSyCuvZZf4QdEhYWN3dP2HQNG8flOCFp2Xs5O7_r0kg2O0_YaHq8eu13JgDXOP0jSJ8YAG0OVPQRE8tfA4s1gd7xjlKXoI26Mud-u5yn5zNfEpZAbskVKz0S39AwC7JASf0z2YodA45LvgVzOwUQe0EdZIDEJluA3RCik0mOdJcxmNvhSiISUJOwkyWOWVnU5eStc0BKWAYaxNYMkYqKy7QmW_YkTWK75i2Ie2n_gsaJWe2YLbcJ2fE5K5e2a5GVmIAItUTNU-EtjDg86MouRUutvjEQc3SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرچم خونخواهی یالثارات الحسین در دست عزاداران اربعین حسینی در کربلا
فضای اربعین امسال در کربلا و نجف پس از شهادت رهبر شهید انقلاب رنگ و بوی انتقام و خونخواهی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454448" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR2nlTvDSkH3pnzR9sF-oexaSagtN0k23_bgatJ2UywFCvVURBx-RbUWWYQoPmsbYm1MMEh6JwvQlBgmTD_gR_0DEXBCnv9Czpyoo0VDRKcT-O2oTLa3IINMtqIhFS_A_9fNjepBMlwVe6lHhv4MhdEgsmt_FlU2rhA3f3FUQTtzR1WlrJAQChpiCutJKLcCyWFf2JpvyKtpfXvX8U5NPVMWmMfgHBKGmG8k1oWUFFPHmbB2vpDm3TivsiMO-heF8-KRqtwzodzQljFzeiTjV2GzLXJwThGILL7p21c9WmdDQMzex8Jhy5bByleAuxh4DKIL70XayE3hO2VgScSjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
جهش بیش از ۳۳ برابری سود خالص بانک رفاه کارگران در بهار ۱۴۰۵
🔹️
بانک رفاه کارگران بر پایه جدیدترین اطلاعات و صورت‌های مالی منتشرشده در سامانه کدال، در بهار سال جاری با ثبت رشد خیره‌کننده ۳۳۷۱ درصدی سود خالص، عملکردی درخشان از خود به نمایش گذاشت.
🔹️
بر اساس صورت‌های مالی مذکور، سود خالص این بانک در سه ماهه نخست سال جاری به رقمی بالغ بر ۲۲ هزار میلیارد ریال رسیده است که در مقایسه با دوره مشابه سال گذشته (حدود ۶۵۱ میلیارد ریال)، جهشی ۳۳ برابری را نشان می‌دهد.
🔹️
براساس گزارش کدال، درآمدهای تسهیلات اعطایی بانک نیز در این دوره با رشد ۵۳ درصدی به بیش از ۱۷۵ هزار میلیارد ریال رسیده است که نشان‌دهنده ارتقای توان تخصیص منابع و حمایت از بخش‌های تولیدی و اقتصادی کشور است.
🔹️
این جهش عملیاتی در حوزه اعطای تسهیلات، بیش از هر چیز بیانگر تمرکز راهبردی بانک رفاه کارگران بر ایفای نقش اثربخش در اقتصاد کلان کشور است. هدایت منابع مالی به سمت پروژه‌های پیشران و واحدهای تولیدی، علاوه بر تزریق نقدینگی به رگ‌های صنعت، گامی عملی در جهت تثبیت و ایجاد فرصت‌های شغلی جدید محسوب می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454447" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/454446" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آتش‌سوزی یک مخزن گاز در شهرک صنعتی شمس‌آباد شهر ری
🔹
عضو هیأت مدیره شهرک صنعتی شمس‌آباد: دقایقی پیش یک مخزن گاز مایع در یکی از کارخانجات شهرک صنعتی شمس‌آباد دچار آتش‌سوزی شد.
🔹
نیروهای آتش‌نشانی و امدادی هم اکنون در محل حضور دارند و درحال اطفای حریق هستند.…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/454445" target="_blank">📅 15:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM1h6UG79CnTOjvqA2BM7Jmr65QQn8m2spN2dUwY6K879F0JcmzIKny39ouE-8NgsIOzOWqtBA9nWQ-iSna2W3SYS4NczhWByEawa4EJhan8j1N4xmRutd6RAK5I2989cTQsjN9K8CZfwYIQ9f78go-l-zo0sIZ--ggjNfkyGpeSPqnz-m5JalB7-llCFGuowN410Vyy6aJua6mKOmjGCks0z4ZLakOJcchqVCgVH1tnPRWr8ozvlQZtlhwxaPiXTQ74e93J8w7wyD3Qmlwcr__VH0_zDsJ6-r3qv1TjDETXRtMRKv5AQf-O2nYvU16-MGxfAjXKuDLm-1YzS0rN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
انقلاب ما از اساس حسینی بود و با شعار و مرام حسین ساخته شد و بالید
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/454444" target="_blank">📅 15:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr-dwwEIvHhG0HGZPC1Yt_YaQCFnv5EiHuB86IaLtWCZoJz7MPW1cIt9JGqctBnoOXfkjXPhLFswFdwEOzAWq2xxM07w6Euk9FcGZEnk7tBbBrqZ1gxmBkxZ9fRAxoJBJfOc9QGDfC-2dxBWmxCWhMvmCm34crEFiSSX9PkpfeEsihmT0cNAJKn_fSNHpDhT0RmRE0U0FkqrZtTJHb7636CojMRd5o-Tj6q3BoYPZatnG5pT3PgHOqM6g2NLI3s9T14CSXXAUWhiqT47_unwllwwHXlXyVhaqYWH2oIOLw7ZLu_4pQDvfv4yGMIGvrKXe-zEcWzKHaOpBcpdOgdU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی دولت: کارت امید مادر در بستر کالابرگ الکترونیک فعال است
🔸
۲ میلیون تومان به ازای هر نوزاد به حساب مادران واریز شد. @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/454443" target="_blank">📅 15:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQBJWC4Kavtg-S-GwEyW0DBxoWkNRy3UHJkg_lOaSn_bDPI4EIOMXSwA7Pj7-0brazxXuNKdSt9Mh0iNdPdQzivefIu8BoPaZew3_rRYVu3zRryRm25F9EpwtefYPd2ffxI8GPvndEupl5azg2cDysPxUA7YxFtTHoxPRCykMeeF-q-ffXjzG1Aj7hcvNQgJEaZWvpTwBRdQI050dP__HRuAjFG-pkrDd6rHISH6ZlFKUdaRFu78iQodpVqqkTZcZV4fp4n6d7O5qzgtftE8xUDik1srcMvjYFY6ALbddOe1ABtZhJNnZ42pDarhIa7TqUZtX8-EAMxJZqUjtYQ4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-DTP7Evtq1ZoeFBtmVKTrE2ELyn_Wv5BEJDsguynr3xr_d8MJJap8Q3Ereli9W26Db9zqfgrbX7qtG0vNlpZNWB2L7RrJGOYB6bC7keDaBsoMSwD8Kn-gXliu0rM9Y0b3wU-KYg92hSY-NHI-h-q-LeXdqbI2uq0H-iCDcEG8gf6fGu94N8A22zJULFXprX0GiZLjK70UPCJCpBvA-QLCu-oT907OEoe-F6bKtd65vx4Ti0iq513aqZeR9A55duOPZGZPSF0-sgsGvPUBfQIG8cNjfCiIe76p0mHjoaFvCOIKMLDalVsTO-2lMcNhWueFj5Ss5UM9r2NT1qdPI1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgRrQSzxRTznVuJTD93NAEIoDlfHpvOvAhwvSrNzVhxMcMurZ4rsPEGc0XdCxQpkUnQuI_tCA2qgop_kiF2i5u2pzWBz4G1BEPFSVMCWniFTdy7tBqVyRHnTAjaxUDM1LHyEXtKPiFDrLPc6dSCVLf6DfrkB703oqu50myzafAccdBkqt_42OdTrDreJ9a9mT5IjNspklh4aEYRgjyAFDTI75thAzvxtoW3G_bmY1dEBBVe96e-W6qpJ7b-O-R3rA7pwjtnRCsD5jx25t8KIEqgX6xJMuoWD8XWJquqJh4m-wwdLBPm29Wfqr8YOKWPswBiH4qQ9yJUl97KSWDidKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFRZJz_C5h5ssMIuZ85C9SD9xdfpLlGPAVyol4gJWoG1hjGUTEA9XqC-8cLfrWl_3V2hyt2V6Fc9UkmEKgAjN56qmCa1aWS3pGVoAWVQu16HU0kUMJlEkqT14T0btviqvoxoBBumifsYf3xuPk48wxg-UE5VLSjxDO3yBe4NTCaOcsw0Coi3FmR9meoLFBHTZleCcGkBYZzfzF1Wk9FtniwEV6FeQuKeVe1JmWwqIUptlwp0szivggp9qP5zo7V2QyPjqNHomvRBE9cdc7JBYilExIqeZQ8lMIKKaVl_ADEo66V7jj59GT1-HY0aslvmQpOfwuZj9AyPMZovHYOvPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شعار عاشورایی رهبر شهید انقلاب که در اربعین امسال جهانی شد
◾️
مثلی لا یبایع مثل یزید: حسین هرگز با یزید زمان سازش نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454438" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de82b7b8b.mp4?token=eShnH6zGKv7wE6W6fJnFmHwnRVVCWUOAX6NGef4iybn0X4na2p10QAEbCszRu6JGWsrn9Ae9jU9V99NmuKpniRihVXBHjjBHOFGxP4DL4utL3vi2evooLFdulNYFNUrZmt0ruRYYxlYGnaZAQxIFphnp4NnfBeNp10Gw2O96Fa2ZVCWQOd3Sqi3xjA0v371nMwfPkn7MLHcKNVhrvb2kLjImN32_XCmO1Tq-sBmZlGrL7qViaUb4Xe-hOlhz__hmGy5GeveEX1vsMvAElUq_xfhkRHynsSIqp9hTJ7fVk9OHSCCVffKVkAIOJtcAQzQ5mORJMe9dU4MwyKnPnfjI6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de82b7b8b.mp4?token=eShnH6zGKv7wE6W6fJnFmHwnRVVCWUOAX6NGef4iybn0X4na2p10QAEbCszRu6JGWsrn9Ae9jU9V99NmuKpniRihVXBHjjBHOFGxP4DL4utL3vi2evooLFdulNYFNUrZmt0ruRYYxlYGnaZAQxIFphnp4NnfBeNp10Gw2O96Fa2ZVCWQOd3Sqi3xjA0v371nMwfPkn7MLHcKNVhrvb2kLjImN32_XCmO1Tq-sBmZlGrL7qViaUb4Xe-hOlhz__hmGy5GeveEX1vsMvAElUq_xfhkRHynsSIqp9hTJ7fVk9OHSCCVffKVkAIOJtcAQzQ5mORJMe9dU4MwyKnPnfjI6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف دل مردم با مردی که نبودش در هر قدم احساس می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454437" target="_blank">📅 14:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42466891a6.mp4?token=cuIn1bZyJC1dOiKnbYaly0Dticwrr4lCLoX32mXR75D5hvD7CrwZPlRBpeYqz6dgfAuwB2FlTrVffueS2-IcdQA6Ejc0IsABkVHLQSgSEUtExBxCCXkDf-v4kRdqcSkNkXYm-emhw7iXDqscEuKJkcEIa0fm5CBZRQg3mz8j_BchjkWRqTbxF2Wgz4GqhY5g7bCDOLLkgsgogiotnzUDdans9q0PjrISxLycSN9ZiOs3_bJqg6AxAcLNxSGT5Z2uw0GI-02U2SlaSVsTDjcDdlCXV3r1MH5HRrc-_z8eXn2bP144t8CF_GrZdfhv_deciSbL5tizkMM4Kps3lIce9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42466891a6.mp4?token=cuIn1bZyJC1dOiKnbYaly0Dticwrr4lCLoX32mXR75D5hvD7CrwZPlRBpeYqz6dgfAuwB2FlTrVffueS2-IcdQA6Ejc0IsABkVHLQSgSEUtExBxCCXkDf-v4kRdqcSkNkXYm-emhw7iXDqscEuKJkcEIa0fm5CBZRQg3mz8j_BchjkWRqTbxF2Wgz4GqhY5g7bCDOLLkgsgogiotnzUDdans9q0PjrISxLycSN9ZiOs3_bJqg6AxAcLNxSGT5Z2uw0GI-02U2SlaSVsTDjcDdlCXV3r1MH5HRrc-_z8eXn2bP144t8CF_GrZdfhv_deciSbL5tizkMM4Kps3lIce9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: بیش‌از هزار اتوبوس برای بازگشت زائران پیش‌بینی شده‌است
🔹
یک سوم زائران هنوز بازنگشته‌اند که درخواست می‌شود از همه مرزها برای ورود به‌کشور استفاده کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454436" target="_blank">📅 14:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtejN4e32MVTveCZTqWnKh5SxVffgYssnar64EnBYd_YMShb2lPn4W2sbhc7QIizQeKrTFBm-oWyInsfT_aJDCx5cgV0ooFOXVn9Y9FCB5SwoSyS6oFZmaOefy9WnMiq-C661wJaUZ1vbUpYLe5W7I7sYi0LNFpBdhhU5wvEc2I8W3QTOzyUsQ4fTRmCndxqUTkeGYopNU7UgoF2RM4OhUiovIk8QwkGEcmr81RaBL_aM8f9HB_2hqb9safLtX-NGBsql66Wld_ovBV5b56K3FGFlQhDPk8JXwj_my9NRv94NjNhad6rnf3wIF6NR-PwfijunRt1dfiVCClG4Hd8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScTmIqXsg2NFVABawBYmhIkFf1zOJj5S_F2n3JogYHipoF0n9UUWXYuKRNnFIOk2Aa5qdYHwoFhBbR3xi1Q2HCpaGnkUTAAdTKibNa2KxcGtWku3bQwNc6X2mze_L-pAS70v3_l7CF7r_SH-Y5N3zkzBWqtqJn3mILR2iKMdpfwteEKigbRPbqWDWFDOf58yhlZc0elE2CvO2T90wR4TxKVCOX4DxAK9UhvmqPL_7YRGz1n3uV2G6jQnTeAE6VFm1vPP5Fsli8F2detX87UiYe8rowZtvvmEjPlbBwDu4ArFTa8M5qK_ZsicEcDylVyFo9_NIHQObrs4N6EmRTCOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEybzQ9sxaCHQIVZr5Xwvcko0BMaEfV8-1V6NBZBMdQHlrMfN3jnXx1AVTFvhnD3q4mNUnjsm9C2bXA9-6NIrT6J4g3j1vOwkJ5WeKPSmr0Wj1J2VKo4NDRrpN0N_9QmY9D_d6GhtfGDMtBeyeZrXgI4EgMVlQ63dPN0b_4T7AIMoCLh-NQQBoTZamJ3P4UPxBuxamdCPNLieqnUJvbeSqlXkFPnH_bPCsyDcsOGBPpfcpVcc8Fm7QhlYkVu-Gv-I_RT94-PLNuQQeRCGbo2w32eMsJRXiYyX1fvV-c-U_VEFwOrWBXDy2eijU693vYGKHMCkCGiw0YCm2sJxHuBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sfdh1AtpV0uPlNBppsSLcKW9wakxY1k2prXynX2X4ohPcSRK8rRhnG78NntZ3SpOEubjyH1mGa9TCriMuLVFyWY-l3AAjU4nAPYYUB_bSs1bYzPsI5T__T9FWVyliJLBp4sz59k4GMjxHZtE-NhVmyv6b7tWzXUK2XW0LAMl3hCLTK9xf-qcX56TREkUlvetS0jr6tIlYMzpZrBmkHcym4QaNdYx7JuRyJVBsmVrtiMV7Q3JiEUVT7m7o2GxMXo1TgCq57zB5S5kpg7fR_XTtFMcg7rRD5eTRqxkGFjufVmMI1osmM84pl5XBXAOrSxneUySTSEKOiD2QYqor-MFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0wwqEJsSReqGGZk_OIP6bWg60MS5ueZ58555MBULHW_6_Mcs4I9FQIbNI6klzhaEHWrpD3_4q3VEiDhlid0HxwPL3mXrbLaiEaAaAPz-HvUBCQ4V_9old_IGaOHLzyUsI6jP5w_7cEaMedCyFJNyAYt34fT0fuWeJMwhJAH1KUj4TswE0L_cAazp1Xzsjlf7ucIvbCbkxEt_gCUGy1xBNKRaM_qorhOtcWQG-Z32gGQ52xPBFPEWMqM7kKWfFYgoCx9noJMZh6gmCj9gXSPnhvBZ5Qr_m-PhNX2shVY2w_TXw6KuUS24K_C_0pYgo8Ry_xk1yarnDEVzrZvE7Mnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwWS03gVI6Kdsw8UPvRhV7xcHJcDdpSzayvosZdv3RE3wIb6rdkXB-reBLUPVkjB9ApDJQp8sDeUVRWdghlj96LoNlHH22G_ecCCm7F3oDUlLbn0rrmdi0C5GY_X2xJpv2IweDds6JTmzoFHTkcqv-IjqfygWX23avKdDR_jIybd2tV-NInpanAHWkNsL0ZdztuszRtNBbTA3meishgPGhJfGFKMzHM87bAvx9EapqWLd_MnlP6FcuhW7z17iqI6Qbwfm0EtkN9ge5Fpaas5sKyHbm_u2zwPNOSohlR3h0eOboyyb0TS7ZZsffCg6DlP-3-tPsKsUBFT6o-n79iTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZsAPiUrf-q17yCH__0hI9XN0j5058ORIaHZGxVYnOaNTu8X4IBLoVrN4G8_8x4h329sn0m-jNl8xweqN6A2Y-dnIEjp9P9TQXFvdAoEzSQCABJUp6pME59YsneLvU5uAnQhCWyIjvfCe9i72ygyZ1ESPRgCUUjQSNZP5POGo3M1KJcMPlYJuXmjlGtGiKQfCAz7l6m1On_imhYfcFzzt2kgbMnM6BmmsL-f8p_8dmfyQw_GCbMg0aeEibmJNPaaS_NyIKWCFrvY6RK296Zuv0hNdE4zoYUJFgPP62F16pWCqrAEfgttnvQBpUGvlJYbcmVoqwwGY6SmGVtC4jedEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلوه عشق حسینی در اردبیل
عکس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454429" target="_blank">📅 14:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75caaf208d.mp4?token=aS6VKLcdGicttYZeEHsXpaOWkOg0M91QZMVCRkBWAyWnjX0WmNhUCvvoIbyOyFDSe27qWZDmxHOHmc5yXaRrao6dLcsrg8JtXp7upGNOrGtK08xRgKr3TZYgUGeSl_I2j-39eWgZiechF0XDRFcS-O5niv8mcYOfZ4HF41tjqFOYz7DJNtYeuxjfNbqquvyIYoWgdhLLDkQTOI3QTmV7DnHo3_iQ4hoUtF7wmJYFLEd5Mm5QNAr3vqpsDCl7s7LeNI8t3CehDMm83kCVDpstSkiPrAMYWu_SSDLLGq6w_5dkIr9OwiAI4rFHVvU5XmM0eatiWvJplEC7G54TwzTMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75caaf208d.mp4?token=aS6VKLcdGicttYZeEHsXpaOWkOg0M91QZMVCRkBWAyWnjX0WmNhUCvvoIbyOyFDSe27qWZDmxHOHmc5yXaRrao6dLcsrg8JtXp7upGNOrGtK08xRgKr3TZYgUGeSl_I2j-39eWgZiechF0XDRFcS-O5niv8mcYOfZ4HF41tjqFOYz7DJNtYeuxjfNbqquvyIYoWgdhLLDkQTOI3QTmV7DnHo3_iQ4hoUtF7wmJYFLEd5Mm5QNAr3vqpsDCl7s7LeNI8t3CehDMm83kCVDpstSkiPrAMYWu_SSDLLGq6w_5dkIr9OwiAI4rFHVvU5XmM0eatiWvJplEC7G54TwzTMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از راهپیمایی جاماندگان اربعین در کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454428" target="_blank">📅 14:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg6t4fAcHRqjuQZJ3l8pn4jakfAxd2uidZ70bgA_zixpJ4FdghcGETjKMWixsGGiFfEtMxuHcZzFzUwoG82_rcQFF4UBB2Jt2na5dw1bhun4KDtPptvQJaI9jQ3ocqGdb-RfGhx0KiQ78obYIZoD4PeWBF9CWXy_9g-UYRb6ktPwauvckDcqpnfAIJ59WUmV3aXY6het1lwBBtnH_HMYDW45oV0vsV1HnKDr7AGK_8g7Ztn4ZY-zklVhKL91jN4RrPtik2i_UBJzA7dhNcdS1pZqBDJdi6neLkwGPVyA5XrLJ9XsaXcbksNNJL0Em_cNlZaIDpXfXfpmMnGZ8WEQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از حضور سردار شهید علیرضا تنگسیری در پیاده‌روی اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454427" target="_blank">📅 14:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_21otVZJ2L5lLtVrvcFWQCLI5CygbU2ghZEFKHrRhSXt3S2tT-o37z8_MBOR6phi8lP2JivRqB5qOU89I2jDSAvlMy89yQvPaTCBwv0-LKCx9hILkQiu5PIfCjYNJxc3CPRH7cVbw7pUC1MxwZTskG6M73msMS3hPNVcLTYNW5EjPvnhdrVkxwVvgP6ggiV-HC4E3EiPtjINoj5PBNUL49EWQX6eb-aAoTZodCM4n2wqvki25HOjE8KuLkVj7H7tGANhdGfVh_BIEmn6P-nPbM7U2qJ-37Zyo2LLXWIf-6cHyIbUwTxB4s8czAZApd5a8-kWu2kYPCODIVp19b9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله ۴.۱ ریشتری در کهنوج کرمان
زمین‎لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۲۶ کیلومتری زمین، کهنوج در استان کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454426" target="_blank">📅 14:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3978967eea.mp4?token=KOWReFxLM5F86pKZ5gMaQMKkR-1YlorYss3b8oiIT-2BD_8bJCupvA9VeG5y3AJrk8MliGj575EAOlY59Awc3afkYcmGUqN1J_JJABIvA7ZeLPCG5HC2OYLkl0kjb9nxiFAXHC9xBIsFUQN2cD_JwYk6kyEXiTASqbbeXUd63GjHJN5iAId_aJwM7Pfh7fimJvDhPhohvJSz4zZLCZBvfPOVtGbjSDPY_iiBMp4yX0Ivy9XSHW0wUcuSTYi9_LAQuYyG5XeSFI7dTRFneMFoSu2gFGRq3uXQC1lo5f2-RnfuhcOcKLTCeWlqmx2N8PZbPHvJClRkFtbTXSd7gJAUHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3978967eea.mp4?token=KOWReFxLM5F86pKZ5gMaQMKkR-1YlorYss3b8oiIT-2BD_8bJCupvA9VeG5y3AJrk8MliGj575EAOlY59Awc3afkYcmGUqN1J_JJABIvA7ZeLPCG5HC2OYLkl0kjb9nxiFAXHC9xBIsFUQN2cD_JwYk6kyEXiTASqbbeXUd63GjHJN5iAId_aJwM7Pfh7fimJvDhPhohvJSz4zZLCZBvfPOVtGbjSDPY_iiBMp4yX0Ivy9XSHW0wUcuSTYi9_LAQuYyG5XeSFI7dTRFneMFoSu2gFGRq3uXQC1lo5f2-RnfuhcOcKLTCeWlqmx2N8PZbPHvJClRkFtbTXSd7gJAUHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت جاماندگان اربعین به شهرری رسید  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454425" target="_blank">📅 14:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آتش‌سوزی یک مخزن گاز در شهرک صنعتی شمس‌آباد شهر ری
🔹
عضو هیأت مدیره شهرک صنعتی شمس‌آباد: دقایقی پیش یک مخزن گاز مایع در یکی از کارخانجات شهرک صنعتی شمس‌آباد دچار آتش‌سوزی شد.
🔹
نیروهای آتش‌نشانی و امدادی هم اکنون در محل حضور دارند و درحال اطفای حریق هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454424" target="_blank">📅 14:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454423">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: وضعیت قلعه‌نویی در هفته آینده مشخص می‌شود
🔹
از همه باشگاه‌ها تقاضا می‌کنم اجازه بدهند در این فرصت کم نفرات‌شان به تیم ملی جوانان اضافه شوند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454423" target="_blank">📅 13:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711a29dd4.mp4?token=KTYGlnE3yv2U9Ku8A1yclbleOlGLTYWHboOgFpO7Rt22K7IRoI5rFcUVLyhTov6ToFtVnGKS2KO2u4eL_JiY7KroCnsPfCFo3voImI2b0yFjg1bJ1BcfrrBRIBZ2qgiGTTVfmB9nyfUK6Qta60PtwjKKYMURX9hpIM7MT8Z1q-FH3e7wmAc8yTR9WQiyZcz8K9oCcabNopDh-U96IQXTzVRQ5cV_XRlXFZ0pO3jqeSbuNKLaNfwKW1VzvY2THeFin5ZKXHSCOV5nsHtn7bb8_pp9p7A3QacXuhyi_33lwCS-4ZHJpWRl4sxZ9GLDIKSlmegi40hE4ZrmnXBuI-U63DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711a29dd4.mp4?token=KTYGlnE3yv2U9Ku8A1yclbleOlGLTYWHboOgFpO7Rt22K7IRoI5rFcUVLyhTov6ToFtVnGKS2KO2u4eL_JiY7KroCnsPfCFo3voImI2b0yFjg1bJ1BcfrrBRIBZ2qgiGTTVfmB9nyfUK6Qta60PtwjKKYMURX9hpIM7MT8Z1q-FH3e7wmAc8yTR9WQiyZcz8K9oCcabNopDh-U96IQXTzVRQ5cV_XRlXFZ0pO3jqeSbuNKLaNfwKW1VzvY2THeFin5ZKXHSCOV5nsHtn7bb8_pp9p7A3QacXuhyi_33lwCS-4ZHJpWRl4sxZ9GLDIKSlmegi40hE4ZrmnXBuI-U63DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی جاماندگان اربعین در خمین
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454421" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حملۀ یمن به فرودگاه نجران در عربستان
🔹
سخنگوی نیروهای مسلح یمن: یک هدف حساس متعلق به دشمن سعودی در فرودگاه نجران با استفاده از پهپاد مورد اصابت قرار گرفت.
🔹
این عملیات در پاسخ به نقض حریم هوایی استان‌های صعده و حجه انجام شد.
🔹
به عربستان اطمینان می‌دهیم که هرگونه نقض حریم هوایی ما بدون پاسخ و مجازات نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454420" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
رویترز : یک کشتی باری در نزدیکی تنگۀ هرمز هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454419" target="_blank">📅 13:36 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
