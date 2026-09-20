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
<img src="https://cdn4.telesco.pe/file/C8mdvrnepZewpqBIVOgnhrZ_eJI9jRG4D03fKEnqKY-EZeXUzVBWOe4s9alUCZ6r9ps46iim00Ep6h4-NGqzGobqt1AnARsZZ2KP6tti0z0YMXcu2xY8PC4ylW35YyzzVQGLF6MFnSYKYrrz4EvC14IT45-IWi8HW5grbl77g4rMsrLPprUU54g6BbA7n78OLrfacsUHh1cJbr1_WrfLQohkEhBkji3YyWvkosDVwIoxnkwdJdTVZGE9hp7Cl-l2HbpQB573BLBRpzP45Alp1KJsVxAkwJ39QKLW_z5VqZ2lDBLtBOe4DrLmxe5XnhIE8Z3NhfL_DRGMtHqgI8PMxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 479K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 04:00:47</div>
<hr>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTOGziEmvSlLH8xZqQMZMPYayq7C4rBbZz9oYIzhlhiQ6RlsyXp-NwZnrsmY-R-S7TVktnqZCucY0vQMMpUQyLI-ck6vITq1xofvoNSz1P9zmMZFOU0_z2toqb44SH5KUsF1l7acovB9R9KmyI-YUW_eDorHNnArf-tpD9HlvvlTeZ3oy8W4JmxbvG6PXB19ajdSZjcrKn8oEwxz_VFLOMGJFjExhOCT8d_5jzTzkYJDtBJqOJFJAwB9HnjCUIqpgUH_uSf-cQucnBFLDIq4zRbO7ShGj2pYdqIIdX9_HwoHV190pr3M4kY1cUBZGGqjjAFjP7SteKwCYb8L5uWL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3cOl_PxZpvQqewNuue5PEE5E4uASzpR_0h2hWoJzZDlGnjAmijxO72kKmaDWptdLxb2fvwXEYnSpjHe7Ig9SYfksfcsxFcp60B6pzg6ZswmO8b--sRehg5Maae-H_qNy6PI4zkC1wtyUT6I-7l9Z0T6L4T8gZKg0AfQ07cKTQyy9dhIzvR7qML4rEr2iJRRv3fDi4UwDb0qWl29-gb2QGhg8ilxf3_Fj8FJheGsSOHg126epCrtcabK2JJGJOJYxDEi6pBf2PqF4IG4Vp90DiMFlr-835dWl00a8Owp6cXu98xofFHpvphT3TjMNCHu7eywZV29PrZWeI8SnXSBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgEpdJM7bSNreHJCFphhtRuqZr_0ZhLsfRtdiz15L9De2ukIrlI_MRjXtWCRFKY7oCq3NWT7EU-A3Ece7XkE0V_y_FoyqCy1nWh6T0II1uaBWif1t32lrr4IQk2OdvpD91cn85NQtSHhZXxw7DWGWPvczRB1exEy5H_BSevQmkMkpBAJKNx8c47lQI1Hp4G-lJyi9OrJuVrk7ccuCLVNBhSK-HJ0o0IUsMJI3vrFEkzAiAP3ejcpDNW_UWrx13pPMrlWfTTRX1xOKoJHrUT6qjr8luIRblebTE6Bo_MfwnG5jwzlkUh-YbIivA1BE-fzHkSTK8TKLH8s8AkwFxpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksGXoT52PhqkZ1k-W-BD2SlFrn_dRlVYoGgNGqsz_rUemD8s7LJm23YvdfhGUIU9tsGHA9Sb5NoQ4yOhXi8flcDVftscqgTXmlvqrySkL9SGtq5O8bqnQtrBN9lc7F2XDixh5CM1LliTFeMmh_QbAZkhYpsQZkcPVJn3anSlPBkXgAY9rEliY0XzAu-yQLfEh3fzq1yp9APW55UcnxlLssts6u9satx0K7MKUa-5oic3ox0q3ytM66vv-8ehyPQJPmsznotvxiATVGcW5AD3K80VhicPhCYAZ60ddMQXI6Hw3oBMwif-8y4GKthMXUZ0sVwyGWpjPlXQ4YM6FS0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au7Bq1uNATrlVXA-2ga1gTA0rY6hxaTTdWlJvtFtmhAQZhXV_kOMH--zZEh0iVxzhQ_KZUNoheXY61aXWW-GSf0bde284Q4g9T-NNRchx3p2PsH0HS6hpLjxTZhCoZOyp3Rmzloa3Ys-8TcwyT_O7q4ZaWmXfAK1-Lyn0vw8y3uTRQtteC3O6akiHdKrUWUlL3kxokQvGAteqfdbmLgOS2dsA7K5H1WM6SVOXqKuBOA6WDTqVtlfU-meGJophZvBuJv1sdNkGHGvh_pUVrJOmaeX0XLYDmGhuWfd49DIdPyHMRh4UMFY1sy04Hly35n8KQWBUg22BtvNGOnx5sDSxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRkSx1CVLmXw70ZlpuKzmNe5WG0XnrPIhi-lEJ27PUIDE2UF7wo4WB6NKzRiYSxroY92zGLuFM7D5fDH1kTO0Z6TyKDuV6xEmLdmmEVjxRhSrFByNU9R5UVh5gmn8jOpGalBB2LYzN7Sal4ig4FHXG841ljeORI-WyCpLIFK8S_aN0XXHq1UBd7baGUw4hgRf1Uo1Y-OzVlRaZfiV1utrB2tqu7xaJ1WlN08q86NAfPHdI_9b_u7aYO_Ke9J_ezY-kr0pdUvOf1W3idPE-GIau-diSZAy92GG3iGQ2aU5-jNow3MEHsj7fQkVqIO7XhQahIEzHQ6-O96yGFqXQHdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptdB7Ocu3PeLPu9ffY399pd0qYvQLxotW1VA0RoHR8oQAGWtcgYL9PQ57yLcPJnTviohMs7e_PAvYu1s7GmKpMyDHEl-bxm-oEMMW2JJQ1Akx7qOLbAg8nlgm9HN2GsxdUgglrKxCOYcCTF2vWwXhPYkDAS33AUom1_J6AZdmJ4hGV4nGJYDRYb9DuEuqWgk5HRvvL7GqxBDAyeOC5FsaI0GDO9ZcWq1Jzjg6anqOY2OrHrmTFX_JDXt8stTh5RWJoTwqIjoyhwOcq9pro8e_bMcp9RRAI4B2hn0fxDkR5lTsJwg8-id6oerFqvs7uHZM_IaGuQGZ3ZU9YNmEGO1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎁
🤩
🤩
🤩
کش‌بک هفتگی در یک‌بت
⚡️
یک هفته بازی کن، کش‌بک بگیر و هفته بعد دوباره برگرد.
💱
هر هفته بخشی از پیش‌بینی‌های ناموفق خود را به‌صورت کش‌بک دریافت کنید و دوباره شانس خود را امتحان کنید.
💥
درصد کش‌بک هفتگی:
🆓
برای دریافت کش‌بک، کافی است درخواست خود را از طریق پشتیبانی 24 ساعته یک‌بت ثبت کنید.
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
P28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/30097" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfi3LKkchfvraePiRhYKjfbdGExPU2VBSNg5pa7TgIIoZZb5alLDK3vIuqJEaYtJ6_N1-ibuRqBDceVH62vV-IMNfiVLKN_bFJV1AQkJR5k1GMFc4cQD6nv6udVBBI0T4Ytfh-yFImqbizr5RFNHmUHh3TDVnC6zEFupkHi7Tk_Z7W2OLcjEQ7dF2dq4uqGKFOQucH4WfLcOwo3rtCvSAvdcBrpPjmEWtXNNnXXvD6U0yo6L9M-aRglg-dDD0I0A2uAQcxpkVl5Qv3x65LiVBdCeUIYMp4pkD8nf-yjpTuzceETZXkMXQYdntPTGdaIvnRaleLvmrYY8saD8I8mopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O25t1wiznl-5R7CW-u9C9dnoHit-Zx0hP8MJRyG8E3-GVy2Xdr1Y3aVociS7bAdSHbWFuJ3eCbH1QX2D9Mv4HaU8kRGBwNZ2yZHoYtz2QoQtXjEAKxdqkJoAgpUc4-SM9Aeo7opZPwyn5039yOfkC0Yq0BAqJ6M3sow4LAPV76vcm4M3dClVK8D8Rz7ceKwqhgc5E2oJnlOrQJf8cH2uT4-BJ5xM31QIKp89cgbvC5uDq_LJUxudQ36E3aO7aYZTf4xLYCRCGHFaVPEAMBDDeSIiKyUB0HMdFCW7Ml6dfVWoVaq8Q_uAdrapav0giaojDewRXeWyiJyHCFZXRpLLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg9NeU_g6wgAeXEqczzrEb4h3wziwqyrbAgB3KjPmatvMjnsH3LbHRR9q_lLX-UEANjj5FHdQoCzCCMB--paGMFr8p9fiF6APCIPNyrzdWtLNORqlnS5Ts7FmVCw7rp5ir4-XZMtxEla8uSE98KcKiwtB_Z8ktGfTriQISXMi8y0ql6y3H01xNbv8IXHnH_I7TreEruAITpbQh6kkSAM3lAscVypExYkoaxryqwQNzOtmjNHbgR2hTQSmzPZM8_l7LrEFEzFJuT5CYCrKz3wQbyrSmO9CbHDgwndFyRUOKXxCd0hg9tXly667fuZjZWEHWqbmZB5zKj6fcJQWbJ1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIGbvZgNUlpYWbaDoBMh-o6-nOvcvLT71H-SowmskkjBAfHY6Bg1Hefok8WCxWhKpXlqD10V-qVOqkv-y2uLZhwlHEZoIIh_CWdV9T0vpqBoNyuN4So7XqSZzbEp-hWjsgpDqKc0734O3nr97t1a67toExoPkeefi2DvpU78TLd4zj6m3bAOY-JpUABmSScRFnJUbGFlwVBTeN0clUiiXrkO4-BfK2gLsQ95REtLD1qP4CnOtgU4TX3bGPtfcEwHiw9E2ly99cQHgsY7kw2BcBhhAbUrhys8XO8E79jEYdsS15w7nEMr9GDcCAeW3mdhQJPTqN17KDIBYfPRe7bAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onylzP1WjChArR373TBFiqEYy6hspV04RiNes6oZ6nxCKn_xP-HSeNoNNcebYO0RfeREfNzh0ua5PyeznfD6IrzvRnHG1hhIgg_mds-20_TutUVPJTAzxj0R-KP5G2ESU1h-26mnAWKhSFQVvRl1pMUIUfckkFhYrkMK27EVzYxI6P_xNo-kpBEKEwQ2tcLV6F4Vcr0en6efNuDjv_QrWbxbv7P_fQK_Ry5qFwoKJRK6kNvJYFrzRRsVlMnz_nHF3-fcvEdYP9xVJqA8B5Rsg4u_Us1mCIrfMMIdK-3Vs54C4YWF14RON0VaP_c9GKV7oOkGQVftbF0PYuaky3mc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5sD5U3htL94PyfLpPLHIIohvih1yzawmlJNq80nlvV9huSE-n5i07FivoRhe-dTAKp8wVi9HqPYKyb4z9FH8NKYTIRmKamS-K769tpJsbeLrmLMnA9Tb6_EnMJvNwBzKeKtUTV1SdKYmHdxvj1DvdI9YyhsChFMooA3sJAHUMmacMSdSE03QC4emoKXMrPvxp191oVedfdQXY9PyrSSQ7eASECOD5wgF-YisGCm-MoaoATzOmPX79GSHD18XMpkwqTsN80badAARLbdl3bHM6P1P7FyHCOYZsLPEETKS638y4rBtrOVaGa2ITh3UEKN0Is2UX-aKrFmGiIHbi_GOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSAoxkyu1wn4NuJxuxb4R7LsUlwu2CYkUe9NByVFwM8Lmsar4uiHC7NSwTlbyL5demtBEmS3A22xryvjPDjTIoaYUbgYvtWcX6GgK94Y-psvaJcLsAYlo_wvY9LM8YnpTcelUQcAPQqynRKQ551_WB8dmJTE4Fp5R9oF828L5Xrv546qo_SfYpirwad_sSUPkUYa6EJ9NIA_ajdpJUN8WUPAYysbIZAnRt5nvyURpW2R4bF3M_1v8qs3voVsMUk2mlwvj290723yR8BkPhPD1NhgkdF2pOVkhCWIgegrqVG-6is7x3-nEWthu4NQVa_h3FXj6TjZM2D-KzGlwUsJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZsPzhWgw0n6PX1vt5XcxMgFP7k6CZgc0_pLn3iqlT31s9UOmTVDXDExdCqDdmTx5L-D1LdaKtOy2rY7KpmZ1V_S7_juUSMwKJ1T1K_kOhDEPY_1oS0fRuUq5Bdz7sjl47F3J6GNQ9zb90HSjQHZgXBKy_Zq39IRsuUrp6G3fQCYQybjIMg5AYzYtSJYt3PiX08ufbpqiu9p9fhrP14z12-N6aPngCCJZpushqZbF8kt5ys--VDraR6mOp9XQhGREfn8cJi8WC97g_pHHRIifriqKhWpifY5nmys7X9yrU0mNgTCrGsT7tq1Jk5EFY765o-BSbSRGI_wtwRju9qbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-DgOHpgXDHJNM8L0qjggzR9ELOsER1IVBQsCl7_t5yNDaBynl05sznj5ZlV_k4NUCeljPELcmFrHYR77E4UWdCESeRfhAMWLAf7UllWrC90_jv5My_9t6hp9-jg71HbVMtn936nFljdKxIgZr7W0xcjt_ua4TRd0WNbbLkEg4LKlTeXwdggmHWDMW3ethq7BBHa0XllbweugjqYA3Hj7vkEWDpDx2R0JnAoa44YOQvENcgS9ipJQK-NZXBbg7eCKxgipCYTbF6esrqOH6IN0LEs-5kLNrR8f4wVxCE9T1aN4zc7iyUNROEiXlNSsjDHOxWaNzpnEjYyGj7vXsydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mthtyuuvogo9OwwN2JuT7Qtd_6IT5hNd23xtRaOSWIlZsEvFiboZc5861soGyV2X64_a3Y6eUaYLM8df9ysysao1TAsCbi_Cx9DsmbNziGVPfVYnde64YslTJ6iOSGFF__0piArA2Rsc1pmsMps05ABI0zHK51HdG3R1dRJE02U-4935KdmpxSQ38tF5tkffsMCHCUCsOg0-kDrcmVRWRW_1mMbTjZ_98sjWBTDFbSIAoP8QIRMbPvMBInbrGbMUKo6ISuOkAJyGXeUpwxvhR-rlIuqkT9RG65C9yHdZcJC6YqZUyIcld6VxFQm7IhAZLnji2JbSpL9f1MuRt53KSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXxwO-wa0k846V53zN4mHs5zFO0vZwnuWmxcvdMBgldEwJERcjhhqynKBW2J0IxI_BIKgdqaTQFbbhpvRLn5-YWtMtd9MnnQMVj03qtcW3o1MOqw_T_LP6IU5lh0gwbEoEAQwY9VLIMtE-D4gGEAOAZUntK6t1cvpLEovkmQO7L29GvAxu29viKa2h0sEpeV43rv7ts-APeKbFwcSubUxrFMO5q553vz-x0J9CEIbbrKM9lgqEjJ2qz-ByKE9_tDQcid-LhNYCOpVfXMdj_Smh671FlrjKbJMlh2P2CkrEo0-Qew3vZfFMQjzBmTm_ogLQqHao0ag5ObEDtHd5nCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvGY0yuOgZ0rQKNiMk5a4eiamxIuMdePRqUBnS3YQHjoGF6t4vo_iYdLvKgPEcRKEDVFPikme7sP8fLYfZdSlJ1GWWwuUJWc4O15hkqax8pyZJJ_yFPyiip85ptKNdWOkXr_f6axFcFTtpOlHn4cX8Q_aHrIwPrunQ0O8BU1qoXTqNdfUvkz67mVp6p_avto7KsEcPB89D6iWj4p1vOjv17VzVIoXPfVdHSzEOc5K1gbgO-SRsLYCJr0vshnCGOOiMxNNo_GJuS-_iSMKo6oBKzi0HFU6X2SysONogQ02qplCWZNZDI6jacQONZwAnp4NvVmBwVTra7T6BM56cK2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aer_wvcXldQxNzfAJPAfc-ADQdHew7uAZDeF9QLA_oMMdIz-R-TKtNxW5nJjyacp6tv9Msw9mOwanjNYNw6sCsWbWhon8vD-qbjpuIQ6-w8L1IY9W_-CcvdlIvgDGma3sLu2WSfQysmHcOJ_m_61tmlwOIu1MA33nyLVbjxj48Mot_JDq3XDdkpqx070PcwMZYmquB2xVguH9fcQPUnIFtusSDVpuEzjcrJ1d8TyzwMXsqvB2iBW0d8xv8Lt1u-zvymz8F8FqoBfKbbV41_D1o165ho9DfcqbqKZZn69YjglwCQgiNls4EexOByw40v_B27GSqWXXnm8JdmE-8r8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZmNg83CmHb3Ky4cbasjRik0_cOSK7UPloLP7OQ68JGLSAycmYwI8T5_l72AQzXV-qrkgrp05gs8P3Ie4UP4dzZS0m9Wrl6gr2QSApMQtGq2nPurFPY3CVZ0swzaJys0LtfXlv7H-JTC9SCbfEiYv6cLlXNXnMczK3XKc-Nc8pPUggVI-GZHM5xctV8dGzb3ecdtuUFs7oto2GJRhgfWiXkORVvRbgt0KkeQZ6AHYvKEwJ12QU0Mh8CEIWD3lFk-fRp0OvLpZKC3E0hYbbJQajeO-e9GbzDV53EfgWyt_amBBHXPOTgihhBZ-gGFRiuv-lJuzemgObUATnheigC7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIaEgYmglcYwyHzt4M56AYTdwlihUGnZeoP4i2kAVe6PCZZnwpc3uUL2DLTIxclckZ1KYdlF1ETa-PPf0hmlRpN7swaaA35iC_yNR5ZMZxYAkMwbA7mHqk56dnaxDagTjIN5tMbqWZM65crB5DYkc1bEsrleXMiZu79BjypFl3mlgzOqHB_t9Ysd4M6iHGzd0mlncMxTrzb6LuZg-CuYzJQ8TBmBHSPP0bw2lF2KvH9e4SpAIS7cqGKTXM1qrleICyggDWvxQlEWf6gOwPXiFvde4eCyUFGR9ferylkRptnDQKKWRm0LVMusYW4N_dYVrRvR91luJhYiiWGwX0ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGugPRA5IQ9Z16qzKBce9N7np_gUEH2R19KJpUnK7apmwzIX6ejTbha95oQ40ZX6j_6F1mW1hAHEAhLidZL1eAOeGC6AJbBOW8vIyLdgo0uH32GQp0ozjz001xgtgQUKxZyHHPA5vdxUkOuemgAVDywYtQ3L6bu6he4mHSTkkVifk2JJdjjJKJFNIy26vgAyD3KKUIfQJ2CUYNQ9mJWle7eY5menbLO46vW0XD9ThByeIgueqJcy0VaDhguap-c4lud_-ochTs85-inNih1z6Mh9Bo9VAB-CXzzJYIudZ6exnxB5vf8jIvrR1-wBEh-1Rwey2ql2YCTDEx0Dz52VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSrAjgxEc3YuDvQukqrK9MIpH3oUEFj5wPwPkJaNwz-u-LUaS4ac_F9sJGDi5yyhFpBWo_gDiD5G8OADyUHbbtUhAI8gYstp-XkJVA8uCNpRpg5TTJQnnUdqtYhJobponHesiek8CYRHVRZ1wGWNOBqWRe3B2f48n7Bmnb9m0lANYg_hrnw4FpvNh62xmAsPGMlUDPreXVrgKb0FJob1ws3dZTKKKU_sp_kpE3odbiQHeGnCs86CT4pm-_LG0MdHl5MU6ESLCkHJ4ml-B5vceFQ9X4VLRaBDwLY27VTWFtAyFzBWC2mITJk5n8dMhKkBckunMEo2xF6zyGM-n1fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5BSgqvybJGjsAQuXUIORRAgv3TVFUd8tAlQBbMM-mjR1QWRzvD3yW5cSEvVKo72JsS0K8Nk2T-L6ozc5v_ttIhfrhfAe-y7xuwvv8m-zAma7GEOUH4BybuZ8Ybf1KrIBy-pc_OhsjUAxWbAOMPvRX5UOvmTXAYKxoDRxW-JWr_uy_80naf-taBfpcflKYgZAr1dVU_wxgoOu7enT_uOaenllq_17jtl3f61iyE18BhnnO_T74EJB8PBlHczVQ_Hnwyf0_RrvmzUwek_CoEysdLbM2mdH86K3xUK7RbeldaYKOl2h1UvtcqeK-cbOzzBzqfGT79iS0mBLbnp17u0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCaWz05mtsQeGSQX64CGuOqS8wHN8TdoTsuWzYWwuQmFQvTEF1tOC30_7tR0kKIFD2UMnQrgxYWwcZNyu-QOyYn9vi7qA6rqy0CP2vHZAGlsGkqO0ovCvV3ygD1pMUQrRZaTmvxdG6j8vN9IepaHrrpBeIUPb0TTGBRe4x4LrXJLMGJvIj-yazwU9znC3cn3-LKv2Mqad1qB7V491wBlQhRcwAIMJvBK-XHw5tSKSYmFHdc5ia2TJgSe65uOlWK8exQxsPS2ssKWlR7QieP6aq6Ej4GeOfczYtFdmpDMid8jOQeVlnu7r105CTBqHM_HaEKqDeI9Q3e5WtSJ2_9YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDJWK9emWXq66yAxjVv2c2GevtCBvRn-X4jHo0fFXVAAVMlt8A9Rl9PW6GSawH2ICy2fSbClYk5xZSpdVDM9Nr5-mwP9vuJaUe6soc1UocZzBmjZL1t3h7FtUzPkU69lI2ujDM3P9wgKU9VvltsGOXr4TMG-LhWm5TB7kB5VNrT_Aufhmg-fMbKiKzOFXcqJrl86LB3K4lg2OokZAstXe45Zf2N8VmzODTUrcdsczuzXe5a1g9f8AOqHSORvzViYC4F1685Gt_DxQ45jWLDmx7z9ii40UyVzzkTYmuzjrZnv6yw3wBxcyJSH0YAn88l4lAfsEPunZvAEFnkhMwCYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJKf5DItL38qdgIBMc5doNb-DyZdKUIHfqQ35BZ5IompZOuzYV7D9ECA17A1Xocc0_nDujmqrIpDZ2ApKTpghQVVqgzCa1bEbCi9IG258uW4omaeEJI4P46bEhfZrHeoSFhNio6LBU-2KlZozB8lqbU_OaodyJ9iBcB8mSedCNTHDZiEGDdXkgIDQukO6Tue1pi7ESbneki2NaG49swvN2qPKZSEVpAxXj4SkJ06d6-3alY7jZAQzAm0JHa9Lq1uOaV8oLoFmyb4AZwyKqg9hS_sIJKo4LCZ4vb8IU9CbE1ivDWV2yX3PR-5t9K2S6z1aAf6xcfNfme08CPeZC0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnUlpJ0VUAls4vOa4Mzb8fMve2hI6Jd4M96IcmyyH4tGTq0avJW5XLg7FUhRYyYDB25ztN6EfGRNdHEsBIAJd7yeCrPAYiLRAvLqGMBBqUZPB8DX7BLKL5AvB7mJwBxRvF7JECgXeSP_ADXYPYwwwSP-brOVvY4xZQBELwV_TisDRoFVyFgLHnY3UpMOhFH0vHSsuLVwE8Xe1TsHzumo2gPUydtKjgDy2Od7LMtCSaamHsK_nQHinulenLsqRzaJbUE2vNCkXTGZXhpT01pB-z5AbckIqZhlN8sLiESnHzdPUsbTMqgOp2yL-S7p2S5wdFRjw8PUwRy5Dvt7SU6fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpRT8Dp6GEGF5RuR0wVVsbzCJ9yyK59HrgRm7RNJ5G3BhTbrpTRtXSFbI9_cAjAvkht-EPC37JfxDqjUYuLq-9DXXXgMmdTsKXc3qOX-Ps8FjlU1USEsV_8aJJAGEWhzL9uqG_jpXjfLBshlBA1HWvjPCjkDxzV0QSyDpOFsQwVNdnSPfTO3QNNTKBkjhpImvnEbcU-AwZOTOpEB-4pflp4qxQpE85P4iezLTe8H8lq90VSvSYnl0dCrKin6vPxqwgLOr1kxgfx6P7RfbUum8CwBpdSFYHskVOQ6n6Z7dCYUyDPzuNbM1Om_0A0_WeBBXABz_3ASXSABTxTQXDg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtbGFZvbb_9znM8Xa8Sb4lnZCrALLI4psh0AuWk77_EYGyKcdCfJwzvWyL3cN_u4UAOxW4jcmgUYvolSvBzIclnOX6b3fpFWc2UOCxou6-UJnTNaT9AwISlFoVVKlEmg3QrX6sHwkcgwvKE-729TXR0tkbVmFl0OKnt-rDCHXXPG1snVDVRBMFigV8-I_dkqSqFbSQaIvq52x2VG__f70f88ntQyRhEH7dwyc2JIpYzTBmlnTdkLvT886gWxrrtVCoSKRNqJQEiEgMcTDZcw7Zref-InEGINMja9VMpM3GhgxMBxzk8Ruf3OzC7JZoXSGtUguzdpbDkfSNkMCxP0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMOAnUzdVduC697Pjo868Zntg0st8J1-r1_qEdPcfu_ZMeOHkIwkf-aFg0sUz_oV5s6rYmi0H_KaOCKQ1KdUZTrYw6GXEuzPjWcmvQPOva3nvZk76o_ZMG6J1GzXQTdX5-1yzX112uUSL_76ND-RUM8Lqu1RZEY22rsL_RRhc8WJ1aYXzlIT1HTcOFmwz4_XnNcKBaaEWYlBNf0E6f2DPTLAg6xQaZr-7CG1ZUOdUoPP2RSwsUfPAFDkYbjoRs2Q0d1PW3HIrM97PW4t-C9fg9Kea1d4UgBhft7NJpurbuGqImb5NMZJTkPQmuXL2a0iCSzeZtDxnM9cYL_p-i98rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig4DHNG-ttUbcyHrsZQ8-rTYCJ2IL7J8AS0bCOfyYeujEp6Y-sqXv2H5jmZbKdQBOUM6RAnaoGcXg9wfKiQJ4foesVOj5kx9rJjdGCBFWdEPB45v-l9H3-zHburTaIlw-Tlu6qNlFgvLJ0DHtI5SvkvoOm-7iC9B_s0CmOFV06igDPtm1ELnusQBNuITe7i84lXZfJAruL9HErskXI9dvsq576_1f9EkuP6m97r6z9XJO5njRBF9WKlpexb-fRlg6M-kYNhbQsdcZ-zepGrdnspjoarg9aMI-viAfaMHerVrMgWnF2LS-ORuQGE-90aKR0oGdQr8LhQ_1fdLLXiUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwJIgCW_1JGNvlYOU4mffP-Y1nZKVjg_4gJbA3yjV91pEMMfucIRk50pH92as5dvxXLTP5_SZG2PvEmAwv7HBK45cdbS18FQTpqbfGySPmXbB6YncbIYmYV444s5QHG4ZmS7GKw6ARvcjBEw5pA32D_8cMKOQkNBvoVvitkFr89ddWxuP2x1upl7v4kOQEDqj_CY-0LjT-DLo2N3aZ5FL0smRICVZvJbi8EW4LQuhaVHZG7P73lzRZLgRgeC0T9fFNBWs1a6RqJglDx2CYU7IJLaSqvh0SD7fCVJZxpG_ry-KB5FBFlpsGDeu-X6nnWW4qKZbscfZ10o7L5UVSdObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOIfCNl9gRHm8Uog2DXJpG4olmDAjikFuVbNOEf6hpCfQPldUZkSrZQCRhD5xyK_VZ8e7KUgMHVMqUO3u8Nq-O_r4yvllCCsNstri2LPoI1DCudRbD9AFZGF32J2EPyAQWWh4lNZs60yln1vV2nGmwiX8corLUZBIgeD8ftQo_XDNlatAcgdR9iGtn1rNUF-pEDzQsyYuMbGyy-0eqZ9UwazjaP0fBjDfQDvyG-Q_JiNM6Dp2bqqr1L_M0HUNKBGT_ozu-mlTOMKqZc_NUY7gWIWK7QHPTYF2zpJA9djZrsyv0FzK7YVFg94JCa4EFSHU26SwdkehpTdhB4dZ6iSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxcqUNZwEM5ZN_AHoZTZMD6AoW-ctJE0CDzafLzSX2aUHSFH0Ubc6GtCGZYv0ruezYefl-ufhkVBcDE7bvgaB4DebZOXu3yt1jtbss8x1j_QoX-u0qMHjaWm5enlhSy1NqMu05ux3Ff60RDxWv6k4bdsG5PIMK-6N8DyMWjKvKjX6mQ1x8edk7OGNmBmyw_zeWA1gzlbkFYJCpRgBRhoBWd-KIsAr-F-XAbx7ht6W36qU43oMOWLFQrK27b7TGC0E2irJEtT6qSG674axWzQyniPPXqpcYoDzg-lt96G-_pyV_Pdt7Gf6BsQk-uTTLCpx_3K6wd2-9ue7Xx7nSUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C907D7I9pc6lrtQVwRWz9fla8xVDNG99Ww9uZt4qZiJnwYJm16a3T_EmiTjXDvQVXcLmmAYYK9zYbg815j4MfB7GioRUbb9kSaCBPpaCkR4gASI0Y_wQOVyku_UdkYcR1v4P7paVITiA9RawzmM2DYQr7YK7wOPibA_7lUVKbJ8Gzhnb7AWJJ0C-ipm0TEdQjkelm7M4IXAhyjGqFdoDiaBejOmCaBqSNNhgzWU1dlHeYDOxGbZ9YKmHAE9Gk3YhAmGuq-AzBrzIO1cLUSZNbYPep2DOO91a4nx4vEZVIswszdhTmGpiIokzMTwurdPHNsZ34n8O8tJ_iQkGpLXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKS77uwWB9J97UPMoe3x49gxP41GlQZnGWSJSUQ4aO07Xh53-xVVAoABvFyloYkBMULO834NKO9pa_clSNCbpO4WOIXQ74U_RHdMHwL5ajnitFgeMOGOWNkyAfJb2n8DEqu5jh_eBKYPXrq-wOgnqAngK5B8DNDz-h3YZFUVoqwiY9k-W3EF4qfA3-5z6bIhWit2C7sDwiQ0FjYHvm1GZwCQ8oYscvB7acn1LptYU8GbcaNWN1OzwPn0CWErQv3jKLpTM9V5NQUIyUtiu_w8bMeIIQT3sG7R4FLUQaSParB5v3LCe4AOyLSeJ5J25-T175VmNlPWrE8tGceJnIQ6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxUWbHA-B6Id5-eN2mQYk-KmpTdYfdsj7QYosevC3redE5dPcxz8xCNcojzHAo5AwErNp7IHcFaKdP7BXxIMwhKKB2eL8cOYa3wf8rnsxYvpJko5I3MyXsL_quFWat6WyEveRYDUBMa7vxSp92wCneFdZS3WXzAAsO5pdE4NRO68ps-8awDjDYMdsyHfehUCBIstQEBlJBP75hsBJnZdJXHBp5plZtIf4IeC3DL3Iy6BG5ibyKJIQFhUgMcNXZyr0ZOqQ4tAX8q1QJ0Js_wRPs_mKeWtKxHTg3vU2yLDD6V4jgRLFol2XpgV8tIjACyg_1rod2_DYLx8BNBlBE2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk20zxfh5_6B5ZOaiOr72pcx8S3c_4kg-9sQoykWqeDCNqLrKQcvPH7z9Tp7KhIsE_aOxjbSeSc6E4ESarIyWNH3HpvoOO5mZkavZvuJ9KKkWS_xp024UKPfaZlnbsor6n8xJdIcdRqQuH_B9lf9JCFVoQIwWI2RuI7Ks4GORGeW_Wh-A_wbZp8MuFbgm3ksR7oKujhNYyu4-3cCBcHXll4wyM5pz9Jh5CiWetCJOr3g4rz7wPCs1pMW1_yn42jDGfO0fpWryLjII3wkM8aTG3l_Hwl4z8j1z9KAx_YT-qaYKZ_ZL6IxncztvrpgI5PiEYfSFIRHlDtlZNHrsJurgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OozZJWVTyHO2YbdGHSAsxsnxf37EluBouMXbvonWL7YC9rm_O2kalvvZP-SRBUHEhH16uEE4zQwZXw7hdUa5IcWbGeAHqUiijfJCncJO6I5BzGhOZqyS3AMOhYfNMrqgFpUJgNGjcub8cd3T8mZxV133xlPyvdiIegFPakJJZ0emaPXh-GIke2GNaj6Wpv56BmRtdk68SkLz-zdHU5_TTOG3lIHsVcqEX7hNaft_uDSZt1RcoGkCd4WFonyelsFJJqjyTvpTz15ksHAMQ_8kk8DjDG4W0Nuveij_hHkO51M01p74jA7T6_SkpdyqcPoK_TXXViwxkPEKdAisDJe5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=Jnoj8YMUsv0ud2KGRTrtIfIBWdjjEWyXgEucwc-Bqus9edQQZxFcl9EXSTTHkeetpixCnwy9ar3pI2PCwROB1NGbCueQjDT0pB4ukTZPe-ZU6Cp6mf0noM_ymatM6CV9D-ew1TF_RSy9V4BKB0egSiDop59xnPt9T0R6O6mF5jXzQTULCO8ztZxHZTtT-Oeq6OB2GKJ4zLDXPBqeR8ucOCun2nnxJFY0E7HpOwOC3nbNEfwEZT1Sa9vaKSCH00Fn7dq9wiJ-pUDGRqaI9Sf2hLCGP5kyY-TtNgTzQv7img5ZKJwSdWTh6KAYcRwShfx_bmJwwyxwY_mjh7jd3dx1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=Jnoj8YMUsv0ud2KGRTrtIfIBWdjjEWyXgEucwc-Bqus9edQQZxFcl9EXSTTHkeetpixCnwy9ar3pI2PCwROB1NGbCueQjDT0pB4ukTZPe-ZU6Cp6mf0noM_ymatM6CV9D-ew1TF_RSy9V4BKB0egSiDop59xnPt9T0R6O6mF5jXzQTULCO8ztZxHZTtT-Oeq6OB2GKJ4zLDXPBqeR8ucOCun2nnxJFY0E7HpOwOC3nbNEfwEZT1Sa9vaKSCH00Fn7dq9wiJ-pUDGRqaI9Sf2hLCGP5kyY-TtNgTzQv7img5ZKJwSdWTh6KAYcRwShfx_bmJwwyxwY_mjh7jd3dx1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI4H9mX3KYUktM4XxgxR3aJVLKxatbMilwWlijKE85PPGoL6x9cxAwHTpxaItORQfdM6KG3mxWQPp4xaEIXvRNP06kuYLmATUMWFkfLb1Av21rjvp_KiGCCq_J4HWWUWpCvnIrdxW1UZ_1zRtDh6n0K7T3zleEKe8VMpiuM6LIalgjMWbVL6S6NqeuFjUZVeerSanaNzuyhqTxrFovh3w_Iz75g-iY0KtpKE4gPORQ3bEhM0D2CiYN9WI6VZlJ7W5UBz7v1LI_cIxsU8zIr3M9bw_j1RSVlJgKIKEVtCn1o7uLP_Fj_9kvXzRUhO58HrWQneoKA8GSIWhzG4JFIfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlgwwVSknJefbxru4lAWI5GxVBr-NPlHfjsGDcX5chIg3_gqL5Nqmn2rulDSKEmSjF93y9kpeAmjU2VcaL8__Cg7tQsrHbRm69sZ6BWq4epAT3O7_j0erMcBkMw0alGoJQCC700rdu2yo_xdgAOavAs3IDOmbUs7__9LgJGO1LpmY8NKC86ESWJ-L-Z6B5R9TE2liBFoWs15OJn1TeSXvWDzI_w32-D2wQ52KrYeT6hVWCb7y7XSRPDtLGWjl31s85jMjwMdWzVI4od2hkuR_madZMXMntD9CLJ6KjjhJpTeyrSLNZrqp84FhGoThgqT8M7wNktu7Nz25xTODWoClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssO30ULhKi7HGevhHcIZ761pYpv0v5uerju3Kort-7VS1fP3k6JY7f0moIdPPjjNLTsOuymmhVg29eq6IZ2oycfZKDY0-Hb0WSaA9Eba-mVKjq22cEY232R-l9SO2kov8F6-pZTW8jhRKe88taCfnOn_wT3T2Pnkfd9U23xqPmzkH8h0cJjPf601ShEAcTKmrMtchWS--q-ysj6ZGVkZ3dvohbkBRE66jvrjGEy55Rv3t82e7WAgiNQJt8hz6go2Mg4qupze4qjSHxWSZYVk8iJlBpltNEUp5nzKCTeXbCiiE-FBBy_Bec0JIgBlwR4Hv6-RqCIwJ0WjCU7ZJXrVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAlaALMLpWntuJ_zJffNLouUMksU-S7fJDdzXIviv3kjBWNLGz0SQJALMUund1yNSFb2_EQXU0bljn-z2VhE4OvpwIxHNIHJE5_KoIgvbZRRFSp7QdXXimA6z1XyVLniF8JhLqV0SEsJhyoi9n3nRb52bLbf9L-V5PN7_97ONhEiMCxtDsoiIyWJcZU6H2XElvPqXpXy3gDiAU5yegSQjCdipnsu_xlGh2_r-SHruACgqvOiXMxtZCIqYX2fJgDzdCg_0-XB-tvQ4R5GCyVgX77T-A4EgLEi-PsZUcppkYWIOuTbWb85em0Ibbi2p9V13lsgNp_2h0FT2YcJpxUuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joc4HbUX4dC7Rtsqbc1QaDKQ5b5Zk3qemOaBE2nDlVz9K9pEurVUp-94Fv1je-mSSXNcUUsqneDEzkW0G0OK23oysoU59N3Z3izI_4bwhnlO4uhD1IftdooKc229kap4wrtFdao0BRmpQvPLbHdTnZnZ1sigbBzlQQLKkUnxRuSzXZZqjEqo04E1oUUoT0NelgjLlNOPNiRmt5dtDv_ptowLMP_58E2_I5WgJIRU9WiJQEKvEsoexMgSBoo4t4LIC7Icg72XV2P_dI-CuHAsIFFgtUIYe9CU9jc7utdAAGwrcULTKRe9N4130a_H5wj_gjP-x4rT6JqpfGg8OLpCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIX4MF9cOxZ_iHRv3ZZgztHudlRXQioMHp3AzT4M4jfRUgxdndoBUPYgwtaHPYSO2fEMzz_Msa9NT02tNL02Fnm5ciOQGVMqJC998fO1t3ny20kYdyBLozmS2XDkd71qlAZtYGPEfZ7w5EpVyUVRhaZHXjWN6k_AQ0Anx45IqpK6gi7r9dpvWuBjpkKY-__72s15WalrwX3WMwDgLuD_w9WVTEigYOPuuxnBoyo1a1XbdA_Y6pYkqk0lAfRHdW-YP-Ow15muG-y53Z-ZT56rSiwESOYNc-4ZQ6gHR6yGphpiMdOMNXEUcCcqjuxwiCsdNK5OvYqLBeXu8ARctzwiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=JCjTA29iBWzviuQU_9iWS1bs4EjoNGaR7CIAzc0aOSZAU2OI6n-xgB3RizIZnKU_7w9bdu7akbOfZ2tltNDHSS8ah09j_Tjqm-oFNy1BqsRhVWOvt2HCuRwaVbCnBgU7DFQXvo2A_NfKh7G8OhD9VwKuzHkHp9d1jiXpJMnbs_OOwzy2q6MF-5D2k8P_z2yV48ge2H8BApkeufD0qWQ1h3wq6KFy-fJLEKauaDlWFRdFe74nPoYWCME0f2pUsvQTy1rWRAddHeXvQXbbtN5byvNLOHgzNQCcf24g-cdSar-fSfWQ5P3BN70J2ZkQRgdwSoppqqtISm7lKEQwLQipgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=JCjTA29iBWzviuQU_9iWS1bs4EjoNGaR7CIAzc0aOSZAU2OI6n-xgB3RizIZnKU_7w9bdu7akbOfZ2tltNDHSS8ah09j_Tjqm-oFNy1BqsRhVWOvt2HCuRwaVbCnBgU7DFQXvo2A_NfKh7G8OhD9VwKuzHkHp9d1jiXpJMnbs_OOwzy2q6MF-5D2k8P_z2yV48ge2H8BApkeufD0qWQ1h3wq6KFy-fJLEKauaDlWFRdFe74nPoYWCME0f2pUsvQTy1rWRAddHeXvQXbbtN5byvNLOHgzNQCcf24g-cdSar-fSfWQ5P3BN70J2ZkQRgdwSoppqqtISm7lKEQwLQipgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIhv2dx0Fw3NnbWqO-9bnW80jnel5UaHzLQztHKppzKzNFgZcWkQ1XLpLMHm3sOiP2aLS-Ons-bMUfzh__02eVCiYq0keDQ2csFCXeuCyix3ZTG_lRsPJd0g9Moley2VgezsVzv_mPB8wjzHUk-sA68rjgyh1kZtyJXBnTJDbf6MUbHBSstVr0vr4-PhXKN9E_HibExP-TMw0jI3M07a0s3812nOhmP6uTGGgws_QiFmElPV_Na6o8BV3z5-REuElrVSIn4e9dOkpzx8O2nqQQg-zhBsUvROv-yTAx9K8DHo6YYGnkoJRgv_DSZg289pBOVmF51gTJ5Ba4ccYZ6agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwgYD3HdLxrwn5dE04TIYsQSndIZZKVpyzEZI_ZhoDCJwyuvTAA0U7vNojxcxR_H9FowBDHUe_o02jUFr0RUTxW6DfqN2-EOrAfSMxanqP1vYaNJ_AtPOIfekcN6EPeaBDQsmqAgJ4m-HLG6NGJLCVO3nXxru1PN2Mk34anKTIB7uAW0AoRYC4k91kSZka8uiEM1JkssmnCpQvSEPbYdElMXNVpmJyZ95iLJWzNeCdf9rJHl3PdB4GTpNnYGD23PJNWJEFPfvQ0SfwWjurbQQ56-nSvL_SPK68TsfxW89wj2ky8zvKfmuAp6MgzCn6L6LJBNEPjRlWjddd_BqDdq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjlVuBBMMW1HgTiugD0sDRvq-m9ZPkHV8Khk7-jOgVWN2DIH4OO75hnih2A01WmxdlFA3vow91TXdIWjvOcNHZZaNzJvY8Q-WZRBc0TX6_Wb64FWPeO8mlgHhEE1DtVQRdPUTrUQmg57hLdG__fOw1SiwjIgUnKXSlHV3M6rVnAcDG7uiA1E2qKDMHZLL_A90MXHc2TUsl1r7Ub3ENSulbAKOMkn0wSkGTj6efPyDjeFU9hhpMm7-LEMVq46jLNjkmULSqmaEXN4v-q7qs0BEWSOllziWZCFnYGXG4u1m5SSQY8q8LTiezxXDcutpCj-CjSHl1XlhjI7wDfGpI1XJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=Mwvxpehlg3h3KnZUYEN6097ZXzDBO1csDy-OVG4rQeN2m8HCiW9SP0rgk3c5rehDHIHXuJgtaEdzUzSG45pg_GMSC0OEQ7mVbpps-N1XdtfOj0I9KuAhzVxva7ZkFPQPjC8Uzd6FaLIHoj6zUFB4HZhjtwQ2QHqxKEnPKd32uTDSqJ6QgWqtZLvHypgGPefh5UFD5PZrn1eaWu-uS4k7d8y1m_DlSXKJpctKuJeoPxHSgZUNJfZLsUMSEd0GpymgFc4qztw3JqyZZO0QVlPsHaR1ZWbRfYfu0hrN_1fsPnPoT1wuBK1RKEdopIv-a7QKjbhTCcZ0GTRcMup6Nh9n14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=Mwvxpehlg3h3KnZUYEN6097ZXzDBO1csDy-OVG4rQeN2m8HCiW9SP0rgk3c5rehDHIHXuJgtaEdzUzSG45pg_GMSC0OEQ7mVbpps-N1XdtfOj0I9KuAhzVxva7ZkFPQPjC8Uzd6FaLIHoj6zUFB4HZhjtwQ2QHqxKEnPKd32uTDSqJ6QgWqtZLvHypgGPefh5UFD5PZrn1eaWu-uS4k7d8y1m_DlSXKJpctKuJeoPxHSgZUNJfZLsUMSEd0GpymgFc4qztw3JqyZZO0QVlPsHaR1ZWbRfYfu0hrN_1fsPnPoT1wuBK1RKEdopIv-a7QKjbhTCcZ0GTRcMup6Nh9n14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKp2OLen_XUZZ3N7jULNJC7B1gzLKxbNPjm6o7M_zWoRSgquCMFYcZ6AZnwk5qstrSM1-LgRcfEFpEG_mVCMa7PdhYAE-uuMxmnZLaQFRvqITQMyi14f_sNruQDtWeVVu__AKULt3VZFsxwiE766hgoVJHeF10MgkHprGpH8bNb4gDenSmk8SVoj7dkpqhpHhUHVzx5uy1mCut4wRr2Q1AC2g1W3ROklGisBvQ9F3e_nEWuRo8yvQOOgoBJP6MwpB2XAOOpCSrkRQJJ-gh9VV4wiBV14r98xLsIJY3D0FrxFYDXK_pYyqI6I3PtpLuEEdo8zibSTYhAB0o2LkIZPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7MPn0wJWP4Onu7UNOyzCcUZdfkBStedbZYptlqVyo_Var2NyWyGhU-rJHs3LJ4tgnlL7k5cgrspHosn-vGRrSMU2zlS2Inb_rC8Bt5NLtx5hbaTfGQDTeX1pQ8lkxytxyTBpyd4X656uXhipltoYy6cHCZlcDSQjBLClSN4Jkb5m1O4-iKnwuQMZcGZ5TBRpzet8iMTROqL9rqAnoiXuwd2fRXnd1J7w7p4aTgLoZThyRSlYKDOKQ9daDnGRoVsa1VrtignucHMZl1FeGwdWdAMYrYPDXMgyKaIjhHp6f5apvSnjUYHhgzkWK-drPJ7-y9xKa5GFu4PGcScaa6mOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzJuVeGlbMXBRMOffaxcnwr9kmERMkOU860bbzeSTBJ_GGw72-__YqzKJ65bs1ulumG9onsJZrc4OdMrXNfbg1WwpHwVWVXHQ4XV3xeatj8WSfopgQoly3DvWpl3_OOpxGSWSLLlbZLiGeY2OkFoHkblZVMvIHs3gkjmuME3rZrTSU5Hu38LSjddQ_msCckEoS9DGQ1MmBZrsuEKXgxz5nS-vQxRolEJep4lYa1wx1N5Qvf5x0bqPs-oXOVOCirdJNA7xE3f8LOY4n_N0Cmv1MBIyBCsruawYU1bWMwP_CDRXmlynWrkqvDc1uuxpZ8kWiLye_0mkSkKm2o4_aGB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP0GbVaqoSXR-eQ-SOUlIlFywQMa1yIiTZSTBa22jmYTi3zA0bjbFQ0wThFHDyQGOGEcJUCmqZKc0nduuSNPH2SAUfC36dw4PBVIRxKDY5QwavOJPkpDkO41yHwUMu4zycVBU4MfUyKlnnlllhu5QNY2AxRp-YMqCaA2M8sK4L_9S3SLMorr5XhL_UDIFAwamPTRzK8iHF5nwJXREyLuEgFf0HImM8aXt5uePpJronQxC7qk-2okfF_h0lQatmbLcD9pBZ8q1cc1iz9_syqpJJJ9gKWIgluKLfCYq0gWtERKIRSnn-P2aPebUxwiuoRRU_Vk6pguezIBOI8q6ge0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj-zVxGBB7sWHFS542WBNDVmPGqCwJYo6ixlYf0fFTciouxQNQH17-hELUNQComzTg5xpgect8T1gK1MDBeLIEblNAQ8Pzm9u32TeW0Ky7HaRXxakxDsjfsNEX3sDEkpqr-rvw5oAgyO2JZcN5-Tqz8ob-kyhVuOHHEi7DlDkycGFl6gVZBifoktc_FD9zlld_6KGseWV3XPFU31gCFQugzcYG6GqRuYK51TCeww2vwlh7rG9oynp8ADfu6WYRbB93Dcgf5yr1l7uhLxtlZulQPKS7ktVuEfPqsdy4eK6Tx7R_JJU5diVzCvMYEE_UHWjacfnaZM4HCUUp6qfILPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=AuCYabayeCGVUCMgWJwKnJxpKuZap5qurrgRo-XdhOC1M_9-wqz8moKBHhUErlYcfxnTD8VABtFSKpPe2SAUh6ZVmXA19_okklxQtQipPH0RwT1h7T7aeWVnOVsjhh2c23D6o_vRvOVHPlmqr8epELozgrXOmy5_C1_G2ynF1UIEytjZLrGL__RXKeiYrNz0uRXoCfV2TJF6Ok0txv7SuXJsXzv_H-GP-IvcSBURu9_nimCCjPtWIuSeBfVUfovINU77JBLhLoR4CCBW5OswvbHyI-uOCLjtn8UAbc25DZ_CwXzMnKf8MnU_1v3oiW94vow7gqK3NpEqJFybQk6QXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=AuCYabayeCGVUCMgWJwKnJxpKuZap5qurrgRo-XdhOC1M_9-wqz8moKBHhUErlYcfxnTD8VABtFSKpPe2SAUh6ZVmXA19_okklxQtQipPH0RwT1h7T7aeWVnOVsjhh2c23D6o_vRvOVHPlmqr8epELozgrXOmy5_C1_G2ynF1UIEytjZLrGL__RXKeiYrNz0uRXoCfV2TJF6Ok0txv7SuXJsXzv_H-GP-IvcSBURu9_nimCCjPtWIuSeBfVUfovINU77JBLhLoR4CCBW5OswvbHyI-uOCLjtn8UAbc25DZ_CwXzMnKf8MnU_1v3oiW94vow7gqK3NpEqJFybQk6QXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=hpijGp0D3LpHXmq87CNTOa6-rTDepBANNUgMwlcWH5B8No9cgJTs7MAOjRi4TqpmW_dp0H0oLI-_4kG9SXJxX0mBUdJ3PeshC_1mogy-JWnM53lAi5TsGb0fAwGbfeTnieAnPy_n2v-RXT0TKqMHwjp_OwaHWA7ctRRH0-QjTQbJhRHHB_cY592Ua5E_iZ9qu4_MF0i2ny3aopVrm8UuStV4cBNLDJjGPta98ksqGmfbGdMc-Gz6WQxfSm7QuWoK_8pkzV5xZkeC6aQW-vQp7HWDpog0Y3B33LWyttzVaoOxFk9QZH7geESKq7kEDuoE5nczVJsQYh4C5MChrw2tkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=hpijGp0D3LpHXmq87CNTOa6-rTDepBANNUgMwlcWH5B8No9cgJTs7MAOjRi4TqpmW_dp0H0oLI-_4kG9SXJxX0mBUdJ3PeshC_1mogy-JWnM53lAi5TsGb0fAwGbfeTnieAnPy_n2v-RXT0TKqMHwjp_OwaHWA7ctRRH0-QjTQbJhRHHB_cY592Ua5E_iZ9qu4_MF0i2ny3aopVrm8UuStV4cBNLDJjGPta98ksqGmfbGdMc-Gz6WQxfSm7QuWoK_8pkzV5xZkeC6aQW-vQp7HWDpog0Y3B33LWyttzVaoOxFk9QZH7geESKq7kEDuoE5nczVJsQYh4C5MChrw2tkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrN33RGsv4uEB4b2RuNHRYMsscbW27WgFGpdWrrBgzrGnZQh2KZObroRUqGSJsIQTN96fR-TxGssXP2mmBW7xNNmgFv385-9_WvopYp04nmGP3pua2h81dasEsxRGzTgc9oapdJ4KTWjE8S2z4vsUr2jD0k3O3-hnTM6mZpLXqh0xhEYdJPs6gVjFpFsxqKeXanvXzx_BbFc143qU3poHnOkKmel0d4UfiIHh_vzHRo4kHGFBx3PEwacIlGvp-uc-hFIiekXFyk2l42wLhSUCNA8KamXEQUib_Drw6qK3KSaU_rmYp3eIWo_elzhyPaUYGXHLuQ5O3IPTo2o-ck_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJaWGD8K90170V92kJ8tPSSCtolvwLskmMtRT9AbwZIe3cScv3X3K1Ple0fZuqtFNVGtb3v1txiJBhyDaadZhrNtfzhB2NLRuFZW0-Rv5y0Qe4c3rX4_MZ9NgBX1_G7KKCFGLn0zflVkNWZVouXmRlowWRHAYdN9ARct6yXDhYSkI4kHfOVGXz5TWjHWCPQiMtiqzb4_u8zarzsH9IaDxYGMnqfjVBvEpxPoSIoc_73EoIN5747c3JBv-hrgGEU7vF8FMPJJjBs6LGWLR4HeYKev2A1Ovp9P6_U4kVD74qzUHa-qTP-L6ycBINHkbi76AIFaF0PKZyPrBxL7M-iVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTeLaGFmALAO4M06QbsRaPALFGM-4smYBf0neWU0w0vBUFHbyXTV0Xjmx7S5Ce-0Zq0kBwQz5azDjGM0kzN8IxYHGLj3SsmFl2h-SC1kSsidr2J3YniVXZGZA8jTMueqE3zX2GKWXvlY0NiAy2vgYtQngjSI0n72--VKVXIuA1f1gzHZAR6edZEx0JBLpGR33ky3a4TO1u0_87exfncFsByGcm_exwAlIl1mtqpFWIs9bK0v4SIEv60VKJIX5NHz4y7lTnVqvIdDqrbHsf7ep9CuJlo6jvtKVYYgnx9tmN_IyuijDIgTXzfKSkzU_m_aZJb4hmuM3DHrCQL0XSOOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBTFOQK138Gh93NwoFkSRNIHDxhyyfpMr_KN8hykKzkmxg7DX8m9z4AKIPNURKIPYiSAyz-Te5plFroDUCI94pEfP3CAKeAJdGWVMtNfKRcm5D6A8Z9EB_YR2Z_vTnnfj8MUFg7X3WP5bq-wR_WtdOsz71VXMSszyBKOIOgsWHKhbutWJBsVpUQyxQnLryB9YOXXzFMe52bPRDnYHu8QtVbHn7jX-30mLI4K5n7H0zq7eXY69Vyq_c5AWMtgVDXItzWNUgwtPg1tn7XbxhuOsYyF8s_VSukIPkbii5alw9hVVMghUxwiuliKa4uGpbgEsn-_S5f2BKAWebNeOHUs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sykRct2aK_1-JhCL2D9oqdSWl3U7kWlT7SKvtMiL96xx2OhcIUbE98aEBStyy47AJSQ43xIhA1yC87uwRoSgw0br0sTeezHYEZoUHI5NmEXka9LBVnJd26rGbr-79t_45vL3al_Gfn8wSHzQkb8Pyya13sg3XAXi0xvgadsXHiIKgoiB0HkuWEcKh5OYd2eB6nvdqzfl79M13BjM1h5oQ3o_04TXVrEuIT9GpnPl3-wgyvDTHKDV6R9Zr1K8RhSKJR--MAPhacGFT022y8EQgSRBp5z_xSFlfVixpyhplj3_1peU6m-AJ3Tk1n_YBQfErRm09_OCYhu8iSHi3uf2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpFx0CO6lZbaH7WigbRg1-IXvDZZrTFyxFrgx3GvMxApNpg9hsARY5TnWismz_pYdx6H3PC5-_yD46KxT36Hj5WF711xWhUoYMUVqLmYqM6B2ZRuQP81bEWfKLD6Jwohwb6H2TJq-6-su-v_c3VgQ5xmThG_mwtp0pOOAVSadX-p6KRs01XXcm5fSbCawLzOIzaw7rKVsXFrYUx7oHHodXZPOofJywAxI1Lh4dDU0WarZS3nZ8ILKl7VQq1-0d71AhkhzIFTtuwJqQgib9_h2zZ09L9QvShF5KpLc2kGUGt3RxcsZKo6Hmj_fVzP_hQQ8ADgqD6gN2VEUCfcR0VDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5-lqBSJHxo2riudmcYSiOE4XmmHvJqt15i2J7eNbLNfbM51OyivsXWUAvCg-je6ZSslZgGv0iAXSqxL8WbbPRmYbBRqvgctl36esFytVxSpNJphWpXe9NUYb8_oNyic7C1Mt03ShiM4_oGzlmMqqj__rKY6KjOt0q9PAZixI-2A18ztMD0A-uLqM1km37wxJ7KJXorYtYza42U3VW5yVRlNC7QtR8LhQkCNsiI3-CW9CLo0GpoNkA5WKO1V6S3Ky2-R84s701TK57PF64SFkBrFjYlQBFNCy-uPsImClx6mV_tBhZiHOhCcoS226FHd4gj5YvbTdBxnyQYZ3CUDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xay_n6ifTa4i0JDv0-6yoU0LX1NiFNGMvTRrM_9xOPuamuqC8Nl6xZJfvE691myKXFvu_HMDaXIPlOJBpGHd57dvFhtufwDgxca4nUKM0_nGLcOZvD8FGIg2HSa95MIyh95nXr_eRwhPGEzvYQxGrixqED8MfkzQ_nYX7dLNQjPhygjqOvRjcXJpz7Z0lUqHOSvMfc16Bw_VgQZy6S9QepZXYzw6P1cZ-exWmqESFeJ74numrnWyk8WGsHbLRSyapBt7la9BlKxXUBGJ1wigGfKAdMh_-WDSZ0IErDVdXR0p5SRcSE5y11qQsVn5qjZ9xAMm_fasZ_Et4Zpr6Wy3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayKXaIwNIjrhYgYGhRJVSr1AqmCQ8RmypJh880QdeDPq2-f0PTVIfA3xhkFPXRTNRPen2lp7xMjWzr_PnzdiBJ5PXgjsrArpnPsC57svk_cBV8ygFMs-oAy2lKWXMyYQJcO8SWrm6DHwyw4s5gwv-fbuCTBZjQz6I3TUWBmyLMC3u2s8doTnX_wiRConBsY2mUow8mOZDA4VkVYfj4DQO-Vtw51tiyzow2GRBzht3_ItJmq1jmNog2xB8mVzVLTgxF6SRTWlubRu8d93ombbOM-JetWYFWacExQmOTsTWoaFgGgyoeQKe7idYkxsw3-fQK4USdYUu2dp0kHj74T-lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RYph5k2sZd0h9QQM6OvNlrHFK4k06vRcqbKFgFzG0VDIZz0U2HyGM8pDi2trk9KrjRT6bKs8HcM_Z3GTNNxJujCyW-m_obTh5X62wuZS2HYbA0KI_1jzWCXD5MobOKaFXn5PVj-hiNdS9cI6roQEJihYww9Qz0wVSzKKYvtVzpEtlqLmJNM1dUOSh_A_dr0b8OGMhxn567jsGGCy5jAPxEVNBMaCHrO2G8GybYNAaQoIA-opPpWPDiBj70VyhgUux0ZYpMDKkuPxGAu55OrlbUFnk_75SKxsE4ZF6sszX9uGKYw9Bf4BoHf6hm81ZNXsBoHnF6UzuHEMQ8VLq-1h3i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RYph5k2sZd0h9QQM6OvNlrHFK4k06vRcqbKFgFzG0VDIZz0U2HyGM8pDi2trk9KrjRT6bKs8HcM_Z3GTNNxJujCyW-m_obTh5X62wuZS2HYbA0KI_1jzWCXD5MobOKaFXn5PVj-hiNdS9cI6roQEJihYww9Qz0wVSzKKYvtVzpEtlqLmJNM1dUOSh_A_dr0b8OGMhxn567jsGGCy5jAPxEVNBMaCHrO2G8GybYNAaQoIA-opPpWPDiBj70VyhgUux0ZYpMDKkuPxGAu55OrlbUFnk_75SKxsE4ZF6sszX9uGKYw9Bf4BoHf6hm81ZNXsBoHnF6UzuHEMQ8VLq-1h3i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnXtSBI-OsZESySm4AV5K_EH-UktaPUpQa2vSZAkRkb0B53776xnf9IM_rguKpkv0-TegL0HqvivLIDbikLS0oZ-p5MaGzkP_0wnDcNg9yNGAS5qF0q-OnXkIyKjr1MZaUB3TTka1fajzPsPa5Tqy1T462M8dJ13G-_rRghWurjRxgsQGp1H6NTFWHdJcFU9FgQsw5qvHOei65qkCOG_F0HLe-QOdqPJYH27UkQ89l_ut5pdLICyUhcndP7JuCGptlYE4wa6wvkfK3FXlbnLYU8Zz0RznqQ_a8MOhswr97MEqytuv1HZ9suSu1LqRCSYpae2lorX5YVYpDi1g-A9aEdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnXtSBI-OsZESySm4AV5K_EH-UktaPUpQa2vSZAkRkb0B53776xnf9IM_rguKpkv0-TegL0HqvivLIDbikLS0oZ-p5MaGzkP_0wnDcNg9yNGAS5qF0q-OnXkIyKjr1MZaUB3TTka1fajzPsPa5Tqy1T462M8dJ13G-_rRghWurjRxgsQGp1H6NTFWHdJcFU9FgQsw5qvHOei65qkCOG_F0HLe-QOdqPJYH27UkQ89l_ut5pdLICyUhcndP7JuCGptlYE4wa6wvkfK3FXlbnLYU8Zz0RznqQ_a8MOhswr97MEqytuv1HZ9suSu1LqRCSYpae2lorX5YVYpDi1g-A9aEdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1KxCOtgzjZu5v6Dlve7S-C-jHAOoQpUnnJsbWIeZNoBhyxliEWTlB0usRmaRFXXTKzhzfWkssBdu_DdVG5Px5nl6boGou-rnhZ-evqsHqgnYrzdUBk_YLDi_HZjos6WRUXvhdVj6HWs0lxo2oZxxyd-FdF_g-fNDi-52hTVTJTP-iAwGpLih_zhLfXAAB_xhrG3prVCnqlaoVfQV4WpHOuiaLiW9jWbpQzbqzyr0hG3e938NipVMXeFzp_FFyxsSEGqNieGQmVEn_t1d1C82_DDzi2zmPFxMrLpbklzZrL4fQS6kjUMR8vsRn2t9uhsfEeQMLyCnn6Q-y_Uwzx0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtRBhOsF1qEIzRsWXxP5G360E5hOwMtWaCDYOz-hxlXT4plCphoGrEy3x5uzGdhewmXN4wADYU1QbKqvOE3TkCR7Y97A4MU3Oz4y7noa92dTtYroiK5r9CHp6T4SpNM9JECGk6kFWTrf1ZIgFDeeRMER6jq69oJxveJRFDdHW3GRXR_oaf7WYHaSCNeKue6TzF71Y1h14T9PPui4tfwEWUFsTr7rN50kGDhgCuCE5GI5vQjJSps-bkIXEjnaILREnCxtD1UsBRzX2TpQarOs9z9pbK6EiOJGHQ4ZnpRQS5_YpW2jzBNmk1FSOQITT3QLjGv13QYDxI8DxBm1Ztkx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZRLrp2Q0NxY6IAwfo-t-fJRDfh_Cc9r9HTnIh5A_oZRxU4i05upS5SG23x_DHGVvz79UnRm0UjFqJHAoPg2ZYhPzIspqOTFOdN1tkKO-UOOBFR-LTi6L-jrAYce8QauzEqjIzUujmpsk6JbSEUICkzPLhebNBHAbdkb1K-5qocZRF4O_Zl8cCXxZojzEPAdabSism3mJSFYQL_y9onViZ2jiBmdzPGnyQk97u7l9fxhu_M1bbX_0PQ7oNEuYwAU7oOnqa6SJ79-pulnD_d6XO79DcDeK5uybPo3USbEqCdlvmnqvL1lj9tx9CTUy1EKgMHxulLtoFoNNY5P96flnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Uk_4LjcBLXcuvN9IXuSzVg-pfsyCUsQHd5sV5vfCpAzjxo55FiDRz5aadBDhuyb8D1OacUVN9osSWjmAO_Ia56LDLkkJXlafZYcXDkSI_YO-BEQsu6xfF0OihUIzIJeNS_3e3Wa1wHmm6Y-Dtke9divQeSPjMInAPCM7tDrt-JGh2tMU1Z32fBs17pIRPAHN_dfArhQwKgQmVoKMfJdvXes7B_rbsaElFFLzEXwD-8BZJpWyPa4xKhoEvLmlSr_Y-k7YMCVGnvbRtyseFr0ZJ68iUALioVYVWFlTVt-4BU2HBdVtUsWgp1pmQPYD40vWbL_vOkF5qN04jZGYI9gu1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Uk_4LjcBLXcuvN9IXuSzVg-pfsyCUsQHd5sV5vfCpAzjxo55FiDRz5aadBDhuyb8D1OacUVN9osSWjmAO_Ia56LDLkkJXlafZYcXDkSI_YO-BEQsu6xfF0OihUIzIJeNS_3e3Wa1wHmm6Y-Dtke9divQeSPjMInAPCM7tDrt-JGh2tMU1Z32fBs17pIRPAHN_dfArhQwKgQmVoKMfJdvXes7B_rbsaElFFLzEXwD-8BZJpWyPa4xKhoEvLmlSr_Y-k7YMCVGnvbRtyseFr0ZJ68iUALioVYVWFlTVt-4BU2HBdVtUsWgp1pmQPYD40vWbL_vOkF5qN04jZGYI9gu1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIvi5oYpaepKbw_jBg3OepQOaLlagmUcslYcQQlABDtpkPaR9b_Erx_m3VI75EtmNOZV8ninPdNG1av5VCLDmA6tbgm0I5Ed7ibflT3nyh5ZJa647-0Odu9uvxgj_MvGAko-aMU3dAMQi_5aOoxRqtPXRWeqcwcIaJVvhF3ZeMXCqNXP9S8NJn1-tpKb4Wre4VGYDty1pGD0o6BNtJU_rK69_KM34Fw7ohOquX0Yye_APEL8PPuZ2facQaXehNTdFZZwodk6X5S-UawKlQIqwyBkuardt7nlL0PlRon2ML8knVrFp9oVmOk_vrFJYj16ivbQxUZnP7tVPQ5GzOdUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=DOAMk_1hHoEHx3FnweCEuZdM3QMfjTsxPwcz_OTrDy7RigF8K8G_kdNCZ1ChukgbauhiULrfojC5xMgbwhIEM53lsI0_K2yzQde6_2gxW9aUM7BevCi55etBaXj1m9jPXwoD-MXIJM_SJjf8cmj2DbbVP2s3B4ylrnMGM2Cm01zw13QpWHfj-H93mA4rHegiHKCfqj-ZsbiumATkDg2kQBJURYhlP3569J4j-ZWYwreDEUCqpce4vp_PAI3x-QbMuKoEmC_ZiB5AHzanI2DtOODSeFOBuRzkxIYHGo-OzXavDJLOgJf_K2u7OF5Mxobcjgn2fTxzorgMa95w8mgbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=DOAMk_1hHoEHx3FnweCEuZdM3QMfjTsxPwcz_OTrDy7RigF8K8G_kdNCZ1ChukgbauhiULrfojC5xMgbwhIEM53lsI0_K2yzQde6_2gxW9aUM7BevCi55etBaXj1m9jPXwoD-MXIJM_SJjf8cmj2DbbVP2s3B4ylrnMGM2Cm01zw13QpWHfj-H93mA4rHegiHKCfqj-ZsbiumATkDg2kQBJURYhlP3569J4j-ZWYwreDEUCqpce4vp_PAI3x-QbMuKoEmC_ZiB5AHzanI2DtOODSeFOBuRzkxIYHGo-OzXavDJLOgJf_K2u7OF5Mxobcjgn2fTxzorgMa95w8mgbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Scf5CEB12GevycXCF1NWErv5hDxjJ3aIsW48KrfL0mehyXooQ-V3OqUTNNMgrA4xVCI3k3GXQsC9tvj-mQ16w5z18esR7u6wUCRNQ4w-1vIjmPWjoq4p-2JwUIsaoXJs7feSxsuv5t4gbYoQMtg9-KjqKWljJi0JCaZrIYIdAOM1sHdt8bzPDz3oz08rrWmso_OEy7xf1CzBzsVAXTf0gS-9UJlUzDX_fdOdDQmix8m-v5kzfvCcsjNjSHw4sqRNa0WWzgNjYyNvXbHzZA7gmQtgrIcQhHAyqpZ_ymLyxzOSBPE7T_sxuLpAOICtyEdy6ctJGN5qM8cBO8kS6y9cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7F0ewGr0a0yqPOXPI-w6K7jIRwjHztXMINlimJGH4TPHDCYjZ3s18L0Jk6yMCw8QT-xNxdkrl57zdhoCbBxzEODb4nqxGfV1DJVQf4MA-2_2-cLrHrDZVVZ0rGuogdwBtLzwqZiyX-cTwMsqi8QUY-rkO_AgdVj38DXb-rCm1F_a8kixIoGLV6UYpNCpNWhEi4HG2X54UzD9oHaTxv-m-OmQTdY_cAkeW6EyVRHAqlN3PLujBX1-rH_GJzRWzT_1GBYuSuePgszetaBMz0o5ejdriO6UVLiWF3ZrcJTgkEVKGV-lx6KjO53RwlJDE5y6oQbgCaIPQt_9Gx5P5CNtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHtluDXma-Ks9OYFtcf0OZnWb8dUv3X8BO8Fbe1xYqSKfj4yMcH6HWQd79sNjNbPRNrl3KFC_ROoCHE2yr7fYSA-uxWqOaW15PGTprkDs2g_qOpyU6HwZ0GB1yvCp-dX-mqu4Ig6mS2DVvOL5BJGWC4A3a8wT59Ed75zvKrrsST7rLhf0t2uY96kz5u2Ufnt4v4vkxUYxaAX2f9U0stjQl5Fp2xLEpFmTs8n-meWancoOwT3wlBlS7tP7M6M7MBR_z8Ho2VeNJwHtoPPgNJCk6m9MkvVVWQMcjkP_298edsIteowQaeD9fBX2aNZ3KjHwm9anfZgHm7CP2tDU3VJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcyFoBDttOmnCSsUZrSYUz0hDdBDKn-tPPVZ0u35M63WQN4O1ujnxV79MTuJhDW43a0A3wrPvTg6TRmTlyjeRxN5XUxsutZPNczAj3V1oc4y8IQRFyCj5T826SXKpocXDiWKtIMNNXGZ5-zZEOA11FWkKgIoPInTsm_oCXOLeMyqSKzbDpOvobhtNNhyOHzcFyfmo4KHr0yat3vzP7CgIJq41K223wPbnkrNh8mdUkmtU4sXh66xP2DJ_cp9ktneh1XmpYvQlXGWYVgU-Pm7lvaYa1BI_-lhArpoO3vPo5vCo-LwyoE-c2yQEdio5Y3EJnD1ElklQ9yTKx-r4GAvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OES10oZLi27SjFaW4KfikWQ-8K69lSsX0GXFJQYe5pWHV6Ks5hoxJSrqVScy0G-IKk9LzV4IapoB8QHpRUWL9BG0xkj0wyKVVJc1GOpWD4-ginXqp9GC-BCbk1TPxwP2-CR4XkXrJC82HCJEmDnkBTGdniVPXkDjP6UtUH7wH796pJ0Nr596JnKAyznindnS1LCrXT4qDnB-p-MaLtIiic8Btv0kErPQhRC8icwmN5ZD3bnsNseAtIVjPNinqC-EzQNRip7wTBeJatxI9C9Ax-TkZVluz4vBasUHLFRRdu_SxoKsp_PTOmJsBiC8EYvKvAnlESSmoUTuRLvgJIw7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXGI17eqtFQdQIUBxI6Qt6yu8X_IMqE3oDHskKqQBz5ibrk61yt6q-u-Wxd2jJ_KaleKHzWdJ3197WYQyb8uM8OhuN__tq9p8jqUxUaKXvDEuhWiWGBAceZt9F3aRVyUVnhtzzZalgAJ_tkhXLfQoRu-XUc-nCVrLVsa8oyFFAVDtTUA3kJLdpmsAgqQM3VtPLQXuUyXfv7O3EFdXxNn4W6y-kOUNBimbFoFIOxJh8t7A_g0OtNJCzMkhOhzk8plWVi0g3T-Dg8Ymhy2fn4WeiiZRE-GHqReIChoec31D0lA4NSpWj524TW_hSgam0i9VwozoG5Z9Kye9NHH4HMXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=UM82NsMCHdgiuwZwg4yeIOdhu-wvj3GAZMTHKfyYOLVUhbAptIR5Z66qbT2vSQppCmCbyEEwknCIrJyWx7F7BRUzxYt8N2OjBBXbRBt42uigJ2Y_5emeuGoZYDIHxJe4dFlBbSy1Oytc1ZQdaTnash2GRTQjl8_KEYJjWirrGv8tadZx_T0BsC2Ccrhu1vAQgOwI3pslqYHMPvCbu3Kv6VKv3u5ZF9kGdudtsBRQvqBbcavH6zHLAG_Ykr2WbeqvwrAuD2TEGSVgBCgKyoq9EZ72GJhao4GdWO_lLnD-5ndEqnwp33bB6SapfrgJeZ-JZn9gQb2TVVsBHEFMj86Zcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=UM82NsMCHdgiuwZwg4yeIOdhu-wvj3GAZMTHKfyYOLVUhbAptIR5Z66qbT2vSQppCmCbyEEwknCIrJyWx7F7BRUzxYt8N2OjBBXbRBt42uigJ2Y_5emeuGoZYDIHxJe4dFlBbSy1Oytc1ZQdaTnash2GRTQjl8_KEYJjWirrGv8tadZx_T0BsC2Ccrhu1vAQgOwI3pslqYHMPvCbu3Kv6VKv3u5ZF9kGdudtsBRQvqBbcavH6zHLAG_Ykr2WbeqvwrAuD2TEGSVgBCgKyoq9EZ72GJhao4GdWO_lLnD-5ndEqnwp33bB6SapfrgJeZ-JZn9gQb2TVVsBHEFMj86Zcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aInxpUYe8ljkuG-sM77K3Gph3qeFM_gJFCBjlFQ38gNGNYT8MQD0Z7YBp3Kxkus_xTutdUg50Sq1kV0Xm3kd31bMXMSWqsoc1_Go0BAZgLEKXVQEINIPBu1Ts-46yTxf5c_7xTTo2JQv-mMJSbIPtZsSD0SpnvYhcrdsxrcy4U82wKEDLCyvLXieHWqsfwakTu9_6ByMvbGiNCDELB53yR4WJhfC1hATq2WSck19pUo9dr9euQrR0N4mPPst-8DznwaFe4ktwvNQspRiEN31cuD5gVkrxov7ZgrWptz-wL_7GsYJrBHGyUe6Lq8VSeP1drjw8aYvRpJXgho6yaTu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5fSZRBedhJoc1oVYdB2NBxc_Wi2DJMYKNQqOj4QVezTXLEz-f1m8GBTBa97sb4WhWQ51wI2asHbPg0eFnDh_-o1lOy0y2Nr7hsCN70iM1TrRvtG0FK6NVC-AvDhvcCx_K2QiYXRmK9tsPYUUR6khd7FKvvp6Gx_pvHcrSMElEfD1ujr-BNRHv_1WZJtzUE9Tpbcu4tuO_Y3hKJEck4198eEYaOr8mQLJPZUSGgOyDFTU0U6I6t3KLxCeLo919iO7vtzMCOf73fGhD8R65Av49kJnGLjzjbMpU6ogplQsNiQuAkOJGnFPRDJlODCUF7JFeQEpv3P9j_kJtEFDYM3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWtq70jBn9E1vcZ2XU9c-qUeQDM_STRuNiKvRvTc1pfIWqAqsoiU6UOg3NbgKP1Q2GOwp9oBhCl5keIY0bWesZGYP0zIW5J4XFUu82lCpetLS6HaRJ_IOkR8IXKQjImFlOF46C4YSNq_5PMcSv-HHCBOnDkIPkjRdmBuY7waHV7DMP9wCFwdnAhCCh5HfYlboHzrrce_ybB85fKt5U1lHFIJ-OqO3UMYtvQ8UtrYWetfLpoBHPDF97SM13pNOlEPXBVYT_BCmmE1OknoU8xDDKVwaLOXFBvXfa2VcBHYxzIBcA5rikAWj01NEBR7h4afSC3ZTaecNoE2LhDkyh3RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=DaV6hUO53gIVTgwQ--2BEp_-F5-h1g2nylPIJ594UoCfkV6kp9iN_jaSVuzj6NoPOpHKdtFMgbRf907ktxu1gtpzBiOIOpJCDfYmKSVgcdXC73y8bdyL8-kM_1NLcbf3WeC09LBVOBZbTLhRCdfbQyDB5Dii9XJawVuasao0g75xXozeM7YgOHZDRyghwRIZPPgmXPILyrE35dwv7rrfMxPYsK5LdhRX4LqrLO9VZX2TI3qw0CGNOKRzUxNcv4EqN9VEFPrmfNXxn-sSAhaNdy0n4LEKt81vydSon3rhOsR9X8P7RSYOBi_A8fg9OEJFBXMQd24HcSBQ_M4gE3Z2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=DaV6hUO53gIVTgwQ--2BEp_-F5-h1g2nylPIJ594UoCfkV6kp9iN_jaSVuzj6NoPOpHKdtFMgbRf907ktxu1gtpzBiOIOpJCDfYmKSVgcdXC73y8bdyL8-kM_1NLcbf3WeC09LBVOBZbTLhRCdfbQyDB5Dii9XJawVuasao0g75xXozeM7YgOHZDRyghwRIZPPgmXPILyrE35dwv7rrfMxPYsK5LdhRX4LqrLO9VZX2TI3qw0CGNOKRzUxNcv4EqN9VEFPrmfNXxn-sSAhaNdy0n4LEKt81vydSon3rhOsR9X8P7RSYOBi_A8fg9OEJFBXMQd24HcSBQ_M4gE3Z2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etEtyYsTBfuloDmKZ9ocOI-MM-yDVVW_BY7LJq-mJ8DXQqwFbb-5779-1wOPKAOUGFNgw_usEvq18-_OowhGnMPPVvqRYzymaHSgIMrxJadTYWWaFsPIJ8xlhHEgovyIZIobCMJoioXNJIuN5-MhMehhJroOxeyr7_VM5gKAgyzisfmElYDshpn9LKC09yg2aWGh_OA_g-tutG0jL9Jh_1glDpCHQFiWXr2pK3naeMNntDNzP9Wj-EO2IHRrCyJOt3Zi8MoKwtFdrsk7gd4kI1SnwYpzuj7wC8eXgxy-IYpQr5WrekhQy-VlFx-6ATKjiPyJuCO7AQEi_eNUf7ceEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He5w-0gr7A7chJ7_gs5rNl7UBvKDGRHSmm0vg_8CLEmVL1DOONX7F9knI_80C-T5ADRMwn_Mjl6s4s8h3I69Td836CyYsuR0nmlvnriu0xQvV7yWdjjuNtO3jQc4RtxQPKMJfMz2nIQHWGDSqgRgHT78F26sFVZvajycN1BeMEXopV0XmgQf3NPoE9ZxmSUkaTovYfvSMcMV1_-ZXkT4JHSRgfFgkUH5-_8x1F2hTP3tuVKA9nK4Q79Cdt5xR26EEu2irByAsCPTOT4BeuMRM2RI30Bmi6F7mVT6NmvC6zY2f4IigHIimaUG401bkCMJcqs4a1RRu3lA3Pl9InpPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCpexV81dPjkcTMqilqRxTp5r69QER7apgSmy_H3zIRkUm7t2rxwiYoO-IyUlIx6BbxTjmtOYHBGGvp8ZR-yFAOQdixclE1GxZIT_JHscveXRvE8dbnP6hPzbozmR6ia4kfocwTgVSLWV1lyobjr6OtZy5FbUteb3JtbqMwz8lSa4j0G_skJcEul4L5XlKMkX-Fuw3gyKVIJEJnIrs4i8ssVeh1qV_kodx1YrXAOI2hlruUg8vfk56Y5j-aF2kcnAxkh5uMkiaGipsBq24uZsNPE6jbPS3t_xO2jNxDoMiCHt2acEiIPrmmpfwg8jmChTOjSt5zGlDZi0sU-1WlJXeg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCpexV81dPjkcTMqilqRxTp5r69QER7apgSmy_H3zIRkUm7t2rxwiYoO-IyUlIx6BbxTjmtOYHBGGvp8ZR-yFAOQdixclE1GxZIT_JHscveXRvE8dbnP6hPzbozmR6ia4kfocwTgVSLWV1lyobjr6OtZy5FbUteb3JtbqMwz8lSa4j0G_skJcEul4L5XlKMkX-Fuw3gyKVIJEJnIrs4i8ssVeh1qV_kodx1YrXAOI2hlruUg8vfk56Y5j-aF2kcnAxkh5uMkiaGipsBq24uZsNPE6jbPS3t_xO2jNxDoMiCHt2acEiIPrmmpfwg8jmChTOjSt5zGlDZi0sU-1WlJXeg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
