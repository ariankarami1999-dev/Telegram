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
<img src="https://cdn4.telesco.pe/file/qUbg_NQRHjPEsrj-I_y_DA3bPo_qpmWkhU6JpUDt4EbqnoegZT3p3LwMFBxg7UX80rcHLDEC1ifps5UTo3LbLizTg97BZkbvs9PGFz4VJu6HGErsi5JLyZzzVh4S33yXLeGcxkNBI67wXkq5t6-3woGaNKMEYAONocA6C0VQUcLqe82oa5fsJwkEmHHn0sr_YkcyMcL4UDSZCgQZt5AKuPT2w-TcqYva3DPO-FQJ_8FuXkrybH5szuU3Io_iiUjNTbLQ11Q9kUGbcXLMA2e_lU3qq79gWsNL8tV-KCqu01fDWRZiWzKgmNbA9ClB5wgjDZs8lCy-27dD8M_-wIfXnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-465381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9_4viJ-7NuuOUsVhOo4a4Y4Uy0F-QQOdEf2Hg0pVp35cU3oYNgp0ax4z6RAz_mXxijQ1DyLzfPD_UuTFBWjgUeev_Pf24iFBrNWNencG5xQpCvNUV3qEchwLM90VZOY6W5BInK5pTEz75OSwU37QuhRUccgV57CNdd4V9oaLomUyLZHxXQqV-fh7JvfdZW4D661zvKLTBlj54alOquM1wQVtm7-W_Coe0T9fPWIfdQmGHRh0TK7p_wqm74f2Ajxww72CVfvECZgOo8Ol6-hUHr3dFa3IS8rUooxJrXgrlaOxF64DbkA_5wnSlkYC1WITlK0VhnTMpx0fxXGdUU-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
امیر قهرمان عرب
🔹
رهبر انقلاب: بی‌تردید در طول کل تاریخ شامات تاکنون، پس از انبیاء و اوصیاء ایشان، رَجُلی به عظمت سیدحسن نصرالله در آن خطّه کهن سر بلند نکرده بود. @Farsna</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/farsna/465381" target="_blank">📅 23:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxN8JuUTirW_hxtnggQlO3GIlxp0ikulclpR3szYRhZq_m3fP6WTn-G2MavQ35rngI491EN90EMHGc36oZdenaa7FGEHmzWyeNt3AoVJwO2NnBuy2NuSZcJedcTXLuih3q2mT-_VCZBbTqScTjHGhA9lc3KzaaEGSgrGNc2isiOuwo3EBKCt9rpD12QVqJA_qAoZXhVpvnp4JY9NWPlql3aJznMV9EnYTa3Jj1bxrqypniGM1Lpt9eRvI19ud1kor_B6YRtXjdqEURTVkbtXdbXjrVNHehi49SJDtkvQALD7a_jnv5KCSGeUK2y5Lp2Dxt_kFtWX2Q7B_qEyF0zutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌تیم قلعه‌نویی حریف روسیه نشد
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/465380" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/465379" target="_blank">📅 23:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هشداری برای تخلیۀ شهروندان اروپایی از ایران صادر نشده است
🔹
برخی کانال‌های تلگرامی در حال انتشار خبری مبنی بر این هستند که فرانسه، آلمان، ایتالیا، سوئد، نروژ، دانمارک و فنلاند هشدارهای سفر خودشان به ایران را تمدید کرده و از شهروندانشان خواسته‌اند هرچه سریع‌تر این کشور را ترک کنند.
🔹
بااین‌حال، این کشورها هشدار جدیدی صادر نکرده‌اند و به نظر می‌رسد که این خبر قدیمی و مربوط به چند ماه پیش است.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/465378" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGtKHM4tIjcabotlZ2S6r_UMtDUw-w-SilT8jYQHL6-L7ftNO6XCoKEQTMgbMyms09H0N9NQjeM0_27tso4wP4y_MbncyRP7AwilLK5aPC0R3VGMHJDEI0GAAh0OSmg7gvynDszRyUA3F6ljImSQxHypF_3UDPoXD1A_K4smAQmrj7A5kXfWw132NHrL5UuVs0PuQGmf4r0q9f9iR1vH78VaYogscpaGC-rX71cNo0rABEjMm_Huu8Ts01hJ1Ck_LjG-EMKfwhcdkM4kYE_-NpvhnE6th01oAGhCmQ8C1Qslw3O7RQPHxGRXto7gQreWChp8xt1i2IcC39iTnBtTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📝
چرا سپاه به مردم آمریکا نامه نوشت؟
🔴
محسن مهدیان
✏️
نامه سپاه به مردم آمریکا را دقیق ببینید. نهادنظامی ما با این نامه وارد عرصه دیپلماسی عمومی شده است. اما چرا؟ چرا این نامه را باید سپاه بنویسد؟ چرا وزارت خارجه نه؟
چون ایده نامه قطعه تکمیل‌کننده یک پازل متفاوت جنگی است.
✏️
جمهوری اسلامی در این جنگ به شکل بی سابقه ای یک جنگ ترکیبی تمام عیار را علیه دشمن به کار بست. میدان نظامی، دیپلماسی، پشتوانه اجتماعی در داخل و جنگ ادراکی در دنیا.
خروجی این جنگ باید چه شود؟ بازدارندگی.
✏️
ایران برای رسیدن به این هدف برای اولین بار جنگی که ترامپ راه انداخت را سر سفره مردم آمریکا برد تا هزینه این جنگ را حساس کنند.
اما این برای بازدارندگی کافیست؟ نه
گام بعدی اینست که بفهمند علت کوچک شدن سفره شان چیست. اگر بفهمند چه میشود؟ تحمیل هزینه به فهم علت هزینه تبدیل می‌شود و در نهایت این فهم به اراده سیاسی منتهی می شود. بازدارندگی دقیقا در این نقطه است.
اینجاست که نامه سپاه معنا پیدا می‌کند.
💡
برای خواندن جزئیات
اینجا
را کلیک کنید.
@Fars_plus</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/465377" target="_blank">📅 23:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb04cf477d.mp4?token=Wrup-2C1-kNuLxure-NC7GQOXqMN3K6M7hkRRpD-8VS9M1bH8M4d30wwJjEq5OPhnuNQMu53p4x4ZPXRMdI-kIi5-BvWHfO4r84SE34tNXXDyHGhw5TioX1And0k_aDzVwQxSx-4tfwvc0SdTokotFrifrQHF70YpGp1qFl0j3u9NoPYn5xeZyA-LW_5qgqpgsrLvGJS2OxXAXRN7swYJm1fOvVBjBWnDaxrJTGHQm7yYXeJWOfGddT-yODa2p9VdXz1e1ngLSNcKannGvHvmLMj70bbIEGUPYdlosxog8-Ibfzo-rXY5ey5M2FGwL2hcHOiZdVinLwvGz0GTRIilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb04cf477d.mp4?token=Wrup-2C1-kNuLxure-NC7GQOXqMN3K6M7hkRRpD-8VS9M1bH8M4d30wwJjEq5OPhnuNQMu53p4x4ZPXRMdI-kIi5-BvWHfO4r84SE34tNXXDyHGhw5TioX1And0k_aDzVwQxSx-4tfwvc0SdTokotFrifrQHF70YpGp1qFl0j3u9NoPYn5xeZyA-LW_5qgqpgsrLvGJS2OxXAXRN7swYJm1fOvVBjBWnDaxrJTGHQm7yYXeJWOfGddT-yODa2p9VdXz1e1ngLSNcKannGvHvmLMj70bbIEGUPYdlosxog8-Ibfzo-rXY5ey5M2FGwL2hcHOiZdVinLwvGz0GTRIilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانۀ بین‌المللی درخواست مصاحبه با رئیس‌جمهور را داشتند و ما ۳ تا را انتخاب کردیم.
🔹
فاکس‌نیوز سخنگوی جریان راست‌گرای آمریکاست و مخاطبان آن از نگاه ترامپ…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/465376" target="_blank">📅 22:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شرور مسلح ایرانشهر به پایان خط رسید
🔹
فرماندهی انتظامی سیستان‌وبلوچستان:  یکی از اشرار و سارقان مسلح تحت تعقیب در درگیری مسلحانه با مأموران پلیس ایرانشهر به هلاکت رسید.
🔹
این شرور مسلح که سابقه چندین فقره قتل، سرقت به عنف، زورگیری مسلحانه را داشت، با فعالیت در فضای مجازی نیز اقدام به قدرت‌نمایی و ایجاد رعب و وحشت می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/465375" target="_blank">📅 22:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAjnks3c3AHSJhPWy30BHnSkGoLFE6ki2pb2VMUqojS7_jDUEH4fkuVf1K7PAHYlq0TjB7rAsCDSsLpNjd_MOExdYRUshuRisTBBt0Grsgwcuy4vnbJnkCrKt0qCFEzHR1DbBVvtV-ilNwXC1abAtTf3cp8hFRkzyeklOLjBXjVw95A5mYJHFi2l4Zt5gBpopTICTXJcjeHq5IJ8Ua0A8fSBHdCaTB44L63mWQg8gHUaHSyFzISxOqSLPQbhou0wMjVFDzV62sW2U_Eh0OkaAmBgSGBjqvY3H2bYt2Ux166eLZq4IfSJU_R9xC0aC3mhqYVLmAKxBo0U_82_K0chKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو با دعوت رئیس امارات به این کشور سفر کرده بود
🔸
دفتر نخست‌وزیری رژیم صهیونیستی در بیانیه‌ای گفت که نتانیاهو به دعوت رئیس امارات، به این کشور رفته بود.
🔹
در این بیانیه آمده، این دیدار بر تقویت روابط دوجانبه و چالش‌های منطقه‌ای متمرکز بود. رئیس شورای…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/465374" target="_blank">📅 22:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=ucI82pO3O9nTefP-ieaSkqVNyEI1bMcJ3NOnMMuQIFR2jImTf7afeDhOtRe8BI4GfLJ9ERyxujcBaM_o1tbOjm82K22CQr9PZFXvhE0LwBn3IvvfZmpz-bZk6OFHJdJJnSduhyOzBZjbTbTGIaupNV2V-s0YbywCowEKIijhYZQCCyzmnh8mXGwg-f8t17-cy4pybx-AKTe59Udg5ojsWy0zJWjJ1UELDv59v1SdP_PIXQpDtl4Bru6aPwEn2QIp0jU0vfIB44fnJpYfI8D7szEnQ0pwFbL4OC5e3NFH6CdQT0dOYnx7t7clD4RH8_rRLIsrzG_E5HodhuSB7jOnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=ucI82pO3O9nTefP-ieaSkqVNyEI1bMcJ3NOnMMuQIFR2jImTf7afeDhOtRe8BI4GfLJ9ERyxujcBaM_o1tbOjm82K22CQr9PZFXvhE0LwBn3IvvfZmpz-bZk6OFHJdJJnSduhyOzBZjbTbTGIaupNV2V-s0YbywCowEKIijhYZQCCyzmnh8mXGwg-f8t17-cy4pybx-AKTe59Udg5ojsWy0zJWjJ1UELDv59v1SdP_PIXQpDtl4Bru6aPwEn2QIp0jU0vfIB44fnJpYfI8D7szEnQ0pwFbL4OC5e3NFH6CdQT0dOYnx7t7clD4RH8_rRLIsrzG_E5HodhuSB7jOnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/465373" target="_blank">📅 22:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIReJkbeU9zCSRxv8Xvd5UXQ3KLYxCuRsVpbsB7LACKtCfHVBfT0pSmaJUlENInCtNI_gT1XXfJly7yvmBD0GPdw3P7hWsqEfD0kF4srfYPH5BMoD5-v1u2O__PD3f0sv9LvmZv8X9_DMFNQElA5Z0kZoMOe-zE4nXoKVmTLa0ecpsYm4bJKuh0lKUmMCbjVDGTBiBAroxELNPz0duDEgI1U2hboFdIeB9RDJ3j80VvlPF3PA-6NLxkI68uBG683Th1HOFEynExkIJUqS5Q6uypcvgD1d_xJMi89qbzBOcHcfP3C4cz6gh3ZtsUaae0V8iXF6WIdbG5ne5WWyQM4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌اصلاح‌طلبان از تسلیم‌طلبی صحبت می‌کنند یا توافق؟
🔹
مرز میان «مذاکره» و «تسلیم» را باید در یک نقطه جست‌وجو کرد؛ نسبت میان امتیازهای داده‌شده و امتیازهای گرفته‌شده. مذاکره، فرایندی متقابل است؛ هر طرف بخشی از خواسته‌های خود را روی میز می‌گذارد و در برابر آن،…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/465372" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در ملارد
🔹
سپاه حضرت سیدالشهدای استان تهران اعلام کرد صدای انفجارهای امشب در شهرستان ملارد، مربوط به عملیات فنی و کنترل‌شدهٔ انهدام مهمات عمل‌نکردهٔ باقی‌مانده از جنگ آمریکایی-صهیونی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/465371" target="_blank">📅 22:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkXqVmEn5_LviFweuYOHfXOJ-1exQBbYLrY7SLgrfnexHKKC_tpEs_rhislflvCV5GKq7Rz7DDU09RoJbXc716r0Zo4QpD5qs2jqdGAO3Y8i1_Ylu0wL-cehtpZUZQFgjkAob1Tl9Ssw44TE98xMswwvuOtE7nUasxGxG5VJsij0tDk19NfPjid4EFHTG_FcRx9L27DSZBBI1eGYN46UT8c6S7e46AJpR1n9196pFdBTFd04nis6QHObLrNd-flnivdjgQqCcVbacjix7FWNE4mSo6eDtq_1T0vaa17Hxl-M4H0WwDl1wCjegT-EdSd7MfTsZuDrCSbEKhFa8jnGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اخبار امیدآفرین امروز را یک‌جا بخوانید
@Farsan</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/465370" target="_blank">📅 22:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftGBSg82TZdc4wd0Xu6X-GsQE_SXSDXvDmMytdNmwTo9hsLpZSOJKlxWQ0htXY2y6WvgcT-7Jk6bQu2sfZtFUvULstifXrIOxFQWBLmcVDFfuLNrN7f-SHWu9oEcsdyLEVuwL2zXZ-U8vWKghMeO0UOT5rV2GDyaw2PgAXfOwM4L7eVs96ise9XBzJddCTNQ5lNEp_1_mp99LBo38TfQrWT91zR1cwXQ_nkx1cNwBgCQTN0TDgc0QO-pFpJTEVCS3yCLz9AKBeCzUqjPREQLelbRYP28kGzd6-H6zae52EKvyUwJMQ-QGacP6nUVxZEgXCMznGdEum9tek5bCXXPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiwAoY2DRr-qFUaag8JLkuvexjKxqvVSebDoQovVMBA-czsY0jF6ohIQ-qim1CLVe47bPp5UvVSfdkumjIHw8TaWYDZyhEnIMQaB8iNjWtcv7-_0Vp80WNdXjPlfvQ_nA4Si-4gsOsnnmlRM3e3GWthCmDQhkepLX9DAHDyph4s_cYIpbQrVFMOGBq7N5SYbl_MeT45vhFzYXdf23ZVfRJy2hdvAHuXMXNjM_lpJgejHhdV9IMeHnyqeETiUzeXjQ0Nx8z4bislB8gY2SXccH8k7_cMC072QKvLQeAxQEe_JSfr2cKYCvPHnd2rOK9nfY8Pp1mqJcAmVbnV0b8Mm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r28Ke_dWRHuOUqMVB2WP4ymOd5RDdqg29FV3G88neDaXM1YI3htth7kw31xNnyKEyRgaCLeSVlDse2i7jACbN6Oa8qlrQj2GBQMykdlM94UvkCpS1jE6atzsqkyQs-sBMxIyqZFkHls43dnjpQHFnc-JRga90vdYrXZ2RzEHsGG_F_ZxnV4B0shbbZMyYO1haPLtsWKuRuH7MRXjr_gNCT-nli4oBUYFlB9q4MDrW055KuTt9q2LCFZf65zDWkJs8Fx5Sil0WAyb2-nyESNn3nGgLLJwfgWCTCFBVlUV1NDx7NxEgwSxLRl6HeEgtFZ9v4OAlEY7VlUzhSXJ0Qhrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmi0NyMYjQ117uI4WY1tKq0RgKfwXnYeRp_1aGHkPVBnZIsHdUiI5AcOrIvinXWg67xn-YjVX0b1havJXFrG_Ofj_iVTX77GlU-I0C90SF1ut8VoHaHavWx1wmck47L4y7FjvjMk3_DwLsfL591z7GFXiM2hrMAPmfP-Rzgiwd2UJsec9ibdcS-FgFwHZAJcrSNAeq9xOIPCq5B3nGwe8_ZZU_Tq5U882tqyn98iKr0yNZ6_EAPm3EDBMDxXgGIzzSQaRDzyrlIsPua8pSeqf2BB1aRfZu3q15S1Ncm92tlfUqSrZ0wKv0O9SoWqI0wJCzaMYAwKaRioJ6poQFQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwKAcHSZkMtNaMFeI4m0eNdsYtRd2kXB7soiuNvehpa7_82xRM44EHY781tEaWOL2aa3d6LhD_ZpsmFe9FuZ-2rD8PV4pJG6bF5J804fUJyXIZ1dKEL2TlJ5okiRGISscTvurNYJAoepDfveWEoRqH_56gpnjw4BCa6Ozc8qtwRp8ZkG88nWzubc1Kn0RWSdGtddtJ7YKSKDGvyC1_TQTzPQXf4Txtws0wCwYTyWzGrJwjw4GQ-XrdOkEsHze1-vjrJe38dxtHRmi4GC883WY9UAOw5pftum6AHq1TKi-LHJJ7D71X0xCNpim5_LDNTyAFusnjQ7ULRQoa8xHgiNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpSFwzJMVBp9JTe13Dn7LGv1LFrCy_QBiLkITEa2jPNbd-5vd0T0HGMNEGBQEY1eepLY6WOPu0RaYDHDQ8flaC_kjBsAyPQPmM0M-43JZS6DsR8lsBatwwmNRLTho4kM0G7tUyqoBt1GMD7pnC1RPGIb6mupV417CkHl8z8TRt4bPTF-7ZE_G_gnHQL5qPtplWeBxkXkuxATMNZH5NjW6CiEDExoDT2xIE3mZvIjAF17q6uvYOFGNJmJy2eG10Po8v8XXFLq7Ahk_Q9kJTSVNWHLeu8v2QmWghVRDtQ51DVKSuoHN7V5oejWDidbZEW2R58-ROpWyMnkDzhPi7fk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfQaNL47UJW0mNUnRi3vhOYpPVCbtc1d_oLttczd8fgxEWzo5n5jo9HsU-OWp6wSBHH7Tn1YAyIgRsuqOgZWz7kjYHs6NWP_Pe3qSCsMy2ArNG9F1nnmPCRui8QExb2q3y9vwoWq8wq7SWPJYMOmMKns8w4n_AqjzmR1pSH7BLDkV2sAm6WzfelzB39BuQ4jHniIPeW51r8m24AtsPZn5YfiwoK8MX0ZqjtUbCMO3iY6vcfYstNvky9P3L5e4k7toZZLIAjFnrKp89_9yRgqYkMsixrQshOWQl4lSBTEymx75SM19i-rq3KN4dLshSfvOtIg2AieuGdK-LJsWiu5aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
نشست خبری کنترل پروژه فیبرنوری
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/465363" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
از ساکنان
منطقۀ ۱۲ تهران
، میدان قیام تهران هستیم. حدود یک ماه است
کابل تلفن خانه ما به سرقت رفته
. با تلفن گویای مخابرات درخواست تعمیر کردیم،
مخابرات اعلام کرد کابل ندارد و باید خودمان آن را تهیه کنیم
. هزینه حدود ۲۰ متر کابل نزدیک به ۵ میلیون تومان شده است. سؤال ما این است که مخابرات در حالی که آبونمان، هزینه تلفن و اینترنت را از مشترکان دریافت می‌کند، چرا باید تأمین کابل و تعمیر خط را بر عهده خود مردم بگذارد؟
🔹
ما
رانندگان تاکسی‌های اینترنتی
اسنپ و تپسی نسبت
به پایین بودن کرایه‌ها
در مقابل افزایش شدید هزینه قطعات یدکی، تعمیرات، سوخت و سایر مخارج
اعتراض داریم
. بسیاری از رانندگان از بیمه و حداقل حقوق و مزایای کارگری نیز برخوردار نیستند. خواهشاً مربوطه رسیدگی کنند.
🔸
از شهرستان خاتم استان یزد پیام می‌دهم. خودروی من دوگانه‌سوز است اما در طول ماه فقط ۳۰ لیتر بنزین ۱۵۰۰ تومانی و ۲۵ لیتر بنزین ۳۰۰۰ تومانی سهمیه دارم.
در مسیر مهریز تا خاتم نیز با وجود دو جایگاه CNG، هیچ‌کدام فعال نیستند
. با این شرایط، تکلیف مالکان خودروهای دوگانه‌سوز چیست؟
🔹
بنده ساکن
نی‌ریز فارس
و سرپرست خانواده‌ای هفت‌نفره با پنج فرزند هستم و نزدیک به چهار سال است برای
دریافت زمین در طرح حمایت از خانواده و جوانی جمعیت
ثبت‌نام کرده‌ام. در حال حاضر در منزلی یک‌خوابه، قدیمی و نامناسب زندگی می‌کنیم که مشکلات بهداشتی و خطر جانوران گزنده دارد. با وجود مراجعه‌های مکرر به فرمانداری و ارسال چندین نامه برای قرار گرفتن خانواده ما در اولویت، تاکنون
هیچ اقدامی برای واگذاری زمین انجام نشده
است.
🔸
با توجه به شروع مهرماه و زودتر شدن ساعت آغاز به کار ادارات و مراکز آموزشی، از شرکت بهره‌برداری
مترو تهران
و حومه خواهش کنید زمان
شروع فعالیت مترو کرج را نیز مجدداً به روال سابق برگرداند
. در حال حاضر ساعت آغاز به کار مترو کرج از ۵ صبح به ۵:۲۰ تغییر کرده و این موضوع برای بسیاری از کارکنان و دانش‌آموزانی که باید صبح زود تردد کنند، مشکل ایجاد کرده است.
🔹
بنده از شهروندان
زابل در سیستان‌وبلوچستان
هستم. وضعیت شهر از نظر قطعی و نوسانات برق، کیفیت نان، معابر، فاضلاب و زیرساخت‌های شهری بسیار نامناسب است. حفاری‌های مربوط به لوله‌گذاری گاز نیز در بسیاری از نقاط ترمیم نشده و چاله‌ها و نشست معابر باعث آسیب به خودروهای مردم شده است. با کمترین بارندگی، خیابان‌ها دچار آب‌گرفتگی می‌شوند و طوفان و ریزگردها نیز زندگی مردم را دشوار کرده است. لطفا
مسئولان استانی و کشوری وضعیت زابل را جدی‌تر بررسی کنند
و برای بهبود شرایط زندگی مردم این شهر اقدام فوری انجام دهند.
🔸
معاونت آموزش وزارت بهداشت پاسخ دهد؛ در
فراخوان جذب ۲۲ هیئت علمی
، برخی
دانشگاه‌ها داوطلبانی
را که هنوز تعهد قانونی خدمت خود را آغاز نکرده‌اند،
از فراخوان حذف می‌کنند
؛ درحالی‌که در متن فراخوان صراحتاً فقط افرادی که از انجام تعهدات قانونی خودداری کرده‌اند، مجاز به شرکت نیستند. بسیاری از داوطلبان هنوز امکان شروع تعهد خدمت برایشان فراهم نشده است. اگر این افراد امکان ثبت‌نام ندارند، چرا سامانه از ابتدا اجازۀ ثبت‌نام و پرداخت هزینه را به آنان داده و حتی درباره شروع تعهد خدمت از داوطلب سؤال کرده است؟
🔹
ما از
پلتفرم «میلی» طلا
خریداری کرده‌ایم، اما اکنون به‌دلیل مشکلات به‌وجودآمده، بسیاری از خریداران قصد فروش دارند و قیمت اعلامی پلتفرم برای معاملات فروش به گفته کاربران، پایین‌تر از قیمت متعارف بازار است. با توجه به نگرانی و ریسک بالای کاربران، انتظار داریم مسئولان و
نهادهای ناظر نحوۀ قیمت‌گذاری و معاملات این پلتفرم را بررسی
و از تضییع حقوق خریداران جلوگیری
کنند
.
🔸
ساکن
مسکن ویژه تهران
هستم.
واحد مسکونی ما در جریان موشک‌باران به‌شدت آسیب دید
و خسارت هر واحد بیش از ۸۰۰ میلیون تومان بود، اما
شهرداری فقط ۵۰ میلیون تومان پرداخت کرده
است. با وجود مراجعه به شهرداری مرکزی و بازرسی شهرداری، نتیجه‌ای نگرفته‌ایم. من بازنشسته‌ام و دو فرزند دانشجو و دانش‌آموز دارم؛ با این مبلغ چگونه باید خسارت خانه را جبران کنم؟
🔹
پس از افتتاح
اتوبان شهید شوشتری
،
ترافیک حوالی میدان مطهری به‌شدت افزایش یافته
و عبور و مرور برای شهروندان بسیار دشوار شده است. به نظر می‌رسد تبدیل میدان به چهارراه می‌تواند به بهبود وضعیت ترافیکی کمک کند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/465362" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9C-an_YElliyxmlW2DwojOqoWLqtyq_7GWCD_l5fUtEVqPepca2RjPbMEeyUTjAsbc-YUkfGaBqA_jfkBte7Qzgwhh7llPWnEb5WmvZoMfVDVFJRUop8ARu56YWMk7jfpwnbEzeQOlTgbsqmZaUaaheoe5x70Hab1nRVf15Lwqvurr7A4seiuVMEufFtKE2XvtfPic7ucb9QilrExfcKV6Oupwxxy4XfiTmlT5PG8Ac3_Hl2rbqt6SuUg-degNloZvc3wR03WUrRAn0WceZ6msHzAR04tbSaNv_zLUvXl2WF_W9r35h_MnUqjuj-8oUPw-GgzxMtty_war_3o90Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندۀ قرارگاه نجف سپاه: پیشمرگان کُرد مسلمان حافظ امنیت غرب کشور هستند
🔹
سردار کریمی: تداوم امنیت پایدار در استان‌های غربی، مرهون تفکری است که سازمان پیشمرگان مسلمان کُرد بر پایه آن شکل گرفت.
🔹
ما وظیفه داریم با خدمت‌رسانی صادقانه به مردم این مناطق و زنده نگه‌داشتن یاد شهدای والامقام پیشمرگ، راه آنان را با قدرت ادامه دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/465361" target="_blank">📅 22:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872812b7f.mp4?token=Dw-1Y7BVgcHyGNBW94RhdTzcgXy2YqNh6lNmaiGfis30NImvBsXiI_3sJEVQhKUkX40wOEFqOdf55p0IiYRc44Xe4RY4JEWdTAhKF1N2pVg3pcOPkmYV9QAmlByvGAXwtIMqG_X2sBdnL6dYDwqcKmuPtoMkzVx1J9v6UcV_NQH1E2YBN89ZdehoOvah-osd_fc_R4jYAz7nZF-ROEX1JULj8eq3sF2ypUYISp0j8AAOcoT6iGijE2K8QT9U1eVncrlNrYMmrhfRupq6pcPo_yibf4pGEpBVamsW_aZ0rK7P_Wq_EjZ2O0ZvqesLFz1-t9B4fY_QyGsfTkW380MkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872812b7f.mp4?token=Dw-1Y7BVgcHyGNBW94RhdTzcgXy2YqNh6lNmaiGfis30NImvBsXiI_3sJEVQhKUkX40wOEFqOdf55p0IiYRc44Xe4RY4JEWdTAhKF1N2pVg3pcOPkmYV9QAmlByvGAXwtIMqG_X2sBdnL6dYDwqcKmuPtoMkzVx1J9v6UcV_NQH1E2YBN89ZdehoOvah-osd_fc_R4jYAz7nZF-ROEX1JULj8eq3sF2ypUYISp0j8AAOcoT6iGijE2K8QT9U1eVncrlNrYMmrhfRupq6pcPo_yibf4pGEpBVamsW_aZ0rK7P_Wq_EjZ2O0ZvqesLFz1-t9B4fY_QyGsfTkW380MkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۱۳ میدان‌داری مردم ایران هم فرا رسید
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/465360" target="_blank">📅 21:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkQ9vAtX1CA74-Y8USK0d58mau6S1vbOJUNtR4hIA8mfMmlz1KP_TQ9m35QP7yp5MG0sNGrBsG1W53tw9KuN_m9tFSfdohIGidpFVgIRrQ23sMtYjlL1NT0DqTmDyyoGkI0Y8leZgRuUXnUAPcQnkm2__axHz0X6BYEOaQJzK6wc4poioKn1tgc8eQdEXzADagQvLvjRxNhLar05fvkqCKEgn2XJkJpqdG7pTQqRhVmeFw2H1TjpGuLnEA4m-JJAMrSiRMFtpEbH3YeiOi378wrQcS9tbWA_mmpKvxWkadXv7B2xNk8YkegBiQ5Udg5s2n8VPEx5Ig9FiG-l58e4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌تیم قلعه‌نویی حریف روسیه نشد
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465359" target="_blank">📅 21:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/465358" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhYYrpJQh_esvW48x1GI-C-sPHuhPnEpRm8Ows47VJDncq1ylVJVDkiI8NylfcHhCm2u8uuxLnJogGq0vfp-37nOGhCBjMBEKWJElK0kXd1-K657JGzIRlXk6Z-h71M4iA6lQbs6o67aVdhH4F_Br7D37vD9fsQicQKeb2u5ZDD7J9dlyslJccHf1ZMYUk1RICOdje3j3VenIdv8U64bU-eJMiOCRN3fOYQlwttf_E5Kja-KmTakXmNLAl8SGBrb0BU2o8TRNfokd1Ho-a0SC0M84NZy80cJFPxbj7d0R-uTP4GceBRgmhxFMsAzLkCfcruOAViKUGX_Obm2ewl8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
۲ واکنش خوب دیگر از نیازمند که دروازۀ ایران را نجات داد  @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/465357" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465355">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af299db612.mp4?token=AT0joubvvU89nJKYGPV4xI4aJ_ce53zYTTZ1PR1yB65uvY-k9Yr-AuiPywe2DGo-NelELpgU7684W0k8fYZ841P47RXFqy-rkepvxNgqB4TDyWIKNhzl6NCsixgl-LMBwSxzfK0ZEeAVEKgQfaGhbEUl053czvFpCnTtOAnWe0gC9iZLfp2DnIMijH3GdEys8ilchG4nHl4ugT-BoD6bO9nuwPXIQjbvvM2bkLMBCM5B3cqYpdWEFBURbX1jy3hxVo-J3hsx10CefWlkydb3hG9LS2HpwHd1xrYDylv9YyQtIjqqZegILmUW2EAKI7bWOw_QWY9yOB3PMpWhBtUL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af299db612.mp4?token=AT0joubvvU89nJKYGPV4xI4aJ_ce53zYTTZ1PR1yB65uvY-k9Yr-AuiPywe2DGo-NelELpgU7684W0k8fYZ841P47RXFqy-rkepvxNgqB4TDyWIKNhzl6NCsixgl-LMBwSxzfK0ZEeAVEKgQfaGhbEUl053czvFpCnTtOAnWe0gC9iZLfp2DnIMijH3GdEys8ilchG4nHl4ugT-BoD6bO9nuwPXIQjbvvM2bkLMBCM5B3cqYpdWEFBURbX1jy3hxVo-J3hsx10CefWlkydb3hG9LS2HpwHd1xrYDylv9YyQtIjqqZegILmUW2EAKI7bWOw_QWY9yOB3PMpWhBtUL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش تماشایی نیازمند مانع سومین گل روسیه شد  @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/465355" target="_blank">📅 21:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465354">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bd57de5c.mp4?token=AGkYTGdr7r2iNKYLGNyETmE1uupplGm1Fz49IS1lRJcGkspSUOxMMyaH2yzPfY_8YMQ6lgfIh1YgjWvrDp5mIXWYZ1mSApUi01FZ3fAJUIxd0Aui1cPkXwnjMy8UA0fIgkuzIMTgHS4eDSFWMqt9IqNzV-CslaZz70fpoPJi7OVd_-6vsSJxcBCQaRrWehWmDg3whf3KupRjlf4dX1TxhbluV5MIVWJr7yjZz72165424AuH9e6_J92A4-9I0eKZRxwt_DDnaMQqXvjyaxSZdjHue8_1mFAd0KmkVWk6L2NJ-Z1zu8PsC0TUuJq5YbqGqabcBAoULZftw2OmwpwZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bd57de5c.mp4?token=AGkYTGdr7r2iNKYLGNyETmE1uupplGm1Fz49IS1lRJcGkspSUOxMMyaH2yzPfY_8YMQ6lgfIh1YgjWvrDp5mIXWYZ1mSApUi01FZ3fAJUIxd0Aui1cPkXwnjMy8UA0fIgkuzIMTgHS4eDSFWMqt9IqNzV-CslaZz70fpoPJi7OVd_-6vsSJxcBCQaRrWehWmDg3whf3KupRjlf4dX1TxhbluV5MIVWJr7yjZz72165424AuH9e6_J92A4-9I0eKZRxwt_DDnaMQqXvjyaxSZdjHue8_1mFAd0KmkVWk6L2NJ-Z1zu8PsC0TUuJq5YbqGqabcBAoULZftw2OmwpwZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنۀ مشکوک به پنالتی روی دنیس درگاهی که داور اعتقادی به خطا نداشت  @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/465354" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745688ee9b.mp4?token=qGpoM0ypPCz4HggjUkB3l4VrYZKPAZnMBPLyZiyZUJP_iLNYFOBZcn4OQO1tUEJbvnnAJzXd5soojCXfJKedAO8QzuBsvDJBpsNULAD636YovBIcpoCdl8ChfcUC45HQZo4NHpRaQh_KoL7a8BD5uC51Jgk1oft3N8wZvh-u73_5aa0pcBM3HsJYJuyCBKJKHmxdN4YenG4IHPGJbTUitiEhicoQwqeKmvgkLYzs5yzmicchIv38y5eHQ5zv5HbvkrKjPjXBnsuw83QG1P1soQHhEn-uy1F5lLATQjLjU_PMN1tAEbs8U-BB3B1jLV28OffJ_lAJwQ6kCO2Q_kRa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745688ee9b.mp4?token=qGpoM0ypPCz4HggjUkB3l4VrYZKPAZnMBPLyZiyZUJP_iLNYFOBZcn4OQO1tUEJbvnnAJzXd5soojCXfJKedAO8QzuBsvDJBpsNULAD636YovBIcpoCdl8ChfcUC45HQZo4NHpRaQh_KoL7a8BD5uC51Jgk1oft3N8wZvh-u73_5aa0pcBM3HsJYJuyCBKJKHmxdN4YenG4IHPGJbTUitiEhicoQwqeKmvgkLYzs5yzmicchIv38y5eHQ5zv5HbvkrKjPjXBnsuw83QG1P1soQHhEn-uy1F5lLATQjLjU_PMN1tAEbs8U-BB3B1jLV28OffJ_lAJwQ6kCO2Q_kRa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ رهبر شهید به توهم تاریخی ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/465353" target="_blank">📅 21:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9d2ed720.mp4?token=hP8CJFXeQetsfctT5XSg-Cw56YNPCEj4bzY7uhmVHxqj7nMlY_17b4G2XDgsJyoRTKbyNwbwc4YeqLksC4w91v26wqahmNU5V0rWwBmfvvtkz7EvMLonWlSSFo4KpLwOsDXd6Dlx9_dBmew8TNo1Ig7ktbJ8Uc3Z2q7gAX9OlLiNh5ZZ65b65SgiBErMHNRSHFP8SNH115fyKbDBHIeH2NS5mHyfF56pT4oYvShPx19I6vd8JXS4zKxN_o_-qFIOqiHaz2EHitllhXyJyTr43mOyHTaBzZsMWefYUSCQJ5HSvY_IY0EqoseM1QInP0sRNDbV-HSLgZa9IJkf5S2DXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9d2ed720.mp4?token=hP8CJFXeQetsfctT5XSg-Cw56YNPCEj4bzY7uhmVHxqj7nMlY_17b4G2XDgsJyoRTKbyNwbwc4YeqLksC4w91v26wqahmNU5V0rWwBmfvvtkz7EvMLonWlSSFo4KpLwOsDXd6Dlx9_dBmew8TNo1Ig7ktbJ8Uc3Z2q7gAX9OlLiNh5ZZ65b65SgiBErMHNRSHFP8SNH115fyKbDBHIeH2NS5mHyfF56pT4oYvShPx19I6vd8JXS4zKxN_o_-qFIOqiHaz2EHitllhXyJyTr43mOyHTaBzZsMWefYUSCQJ5HSvY_IY0EqoseM1QInP0sRNDbV-HSLgZa9IJkf5S2DXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهرۀ درهم امیر قلعه‌نویی در جریان دیدار ایران-روسیه  @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/465352" target="_blank">📅 21:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeKpf-x4MC2rnv8_-5KvnYPTIVfFjMf-FrQ3uCCG7LNfLyOEGv2aPQRiR-R3r7BkMYOPpf2eAdMJD1sTlaOyTyO9sPRUlgPcwqzJOpgrGqKW-X_7te343nTQekGTnt5eyMlK4B9Bw0jAPh0PSJYKyU_ik4Mi2jt5O0dHQBhPBDDEduFSJcIUjHhHq50Y1Hv_VuT-zXqYA_zHcvfCHd6re7LCr5RZxjbTMCjotG3JrYxg72bJQiNJPA_3TSqz6bdxUojzbbXMTMJQLGJ3i_3slSe8F62Sx5yD-0YSyN6cen33QCgk43b3vQHlsQaHxrSfmo-0Kp3RO5gmKfn-cKxAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPyTWHyYIFwjCovBETlXksOGgM4NN8YRMFbZpiKTlS-myLcrPpXNb16cEMrhanBgeSyqZVFWjskit8z0tFTBh93eIAM7QU28J2wjAY15OVxBVQWGBa35HLbR2K6d9x5soapVGLizhHnjH6mufQMTw1ZSh6Jriyk8BHWrXT1Ps79inJMC93s2cLB2L1fpJbtwP8GbBZfMJaLcoGWCBzkhrO9kUbXBEN1Pze7YIpbrrydk2rm7J1ro2gOITBWrxwejEwcpob7NvOMLmSVpq0CJckFTkRIDYZ2ROcBVuXU0mImk5_KZYXEuJPkB3kgJJZgzjAU7oT4_nNGFywHm3kR2zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران با ۸ طلا در ردۀ هشتم بازی‌های آسیایی
🔹
در پایان روز نهم بازی‌های آسیایی ناگویا، کاروان ایران با ۸ طلا، ۱۵ نقره و ۹ برنز و مجموع ۳۲ مدال در ردۀ هشتم قرار دارد.
🔸
رقابت‌های کشتی از ۸ مهر آغاز می‌شود و با مدال‌آوری کشتی‌گیران جایگاه ایران بهبود خواهد یافت.…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/465350" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdOYFLXpo3xLH35JZ3VyDUtlnh360R__Qtv8J7SKTmXVioCjZLusL5-fqYiKU5Bm09JEyddOZDsPHaVqGWxQAmV3j8kAJgQhbwrFZeryUZyWIKDc6_RvJjB-kxMeM0RctYivuTsd-dF7lAabcU7zl7lbSGvTtyFl024YojTV9WwftnoWWRBsbC27W9qxrARxPGP6qLhwFBIKXppVGfURDT98brPFGAgl_HQFeA7wrAH9-7hBEIo2liq8AEGPty5X0R4Dojd9DY3gwUqTRYOyTvM6doQcz7_4qEVInpUtxVCf4gGcvf3s5C4F9iOpPB9UiR82_iqTntDXs6_4raRjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۱۰ فرد و نهاد را تحریم کرد
🔹
خزانه‌داری آمریکا ۱۰ فرد و نهاد جدید را به فهرست تحریم‌های آمریکا علیه ایران افزود.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/465349" target="_blank">📅 21:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bcd44b72.mp4?token=UJQnFtmqAzTQt31Q9KmiyQewt7wBF9XPEEVwWRy1KGLm6NSsk6n7GVloyhl8P7tYy6Sm7gGGzS1leGdc0memweTV0hdoOZWGECNCykCXXY8zjx-I4pnqpkw7Za5puAwFjpp-gPXkp1AQs-s6JUjDcAdFx9fIBjBYyBOAh06u38YBqKfVpQ60hmz77JYmyuKBA1S9yLLeKBGHmeFXULbxAnHzFPzYzOWl8HbFsZZttqbUmwAdyDlxb5UpTRwAsWPfa2E-kVu1_FSEc8Im-iYqKpxvgHf9sbXJ9Fc6UmiEzrfle5et19JKM_q7dll2Ja0OXErReZZwJUwuK-DFF4Jm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bcd44b72.mp4?token=UJQnFtmqAzTQt31Q9KmiyQewt7wBF9XPEEVwWRy1KGLm6NSsk6n7GVloyhl8P7tYy6Sm7gGGzS1leGdc0memweTV0hdoOZWGECNCykCXXY8zjx-I4pnqpkw7Za5puAwFjpp-gPXkp1AQs-s6JUjDcAdFx9fIBjBYyBOAh06u38YBqKfVpQ60hmz77JYmyuKBA1S9yLLeKBGHmeFXULbxAnHzFPzYzOWl8HbFsZZttqbUmwAdyDlxb5UpTRwAsWPfa2E-kVu1_FSEc8Im-iYqKpxvgHf9sbXJ9Fc6UmiEzrfle5et19JKM_q7dll2Ja0OXErReZZwJUwuK-DFF4Jm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم روسیه به ایران توسط گلووین در دقیقۀ ۳۶
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/465348" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9MXUuiPNFO-GeNyLHYbcaoFcIYSx8p_yJHsrt_MWyh4pf3SLkKRkEKxOnQ1zzTvfbjHL-6-txDA37r_fu6k0yWbiTQRUEXbOOItbfB-MZO1dIcyBsUkvbitQSEfY-qYZTKmVcYI2BK6ZecLAwBrReQw1d1ttdIYqfvzmKplWY5UUAryUHaqdg8C_SvC0ab5k0162ZtJmGhpAq7VDrtxEhjqNYy_hgUnCqdEaewaMPGRPVCHwpRBO7mEjZmxD7aKM2QX8_bEAKCWYk-Wre3HIEg7c7H47JiJ2ySlM_KA1PlGJyFVfFcjIC2_8FSn-C4_hEj27MTPX7SBeW-BvtfR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفت‌کش در تنگۀ هرمز منفجر شد
🔹
همزمان که ترامپ می‌گوید که «قیمت نفت به‌زودی کاهش پیدا می‌کند»، یک یدک‌کش در مسیر جنوبی تنگۀ هرمز برای انتقال نفت‌کش منفجرشده هرمز درحال حرکت است.
🔹
بامداد امروز داده‌های امنیت دریانوردی نیز از انفجار یک نفت‌کش در تنگۀ هرمز خبر داده بودند.
🔹
این نفت‌کش به‌دلیل تخلف و عبور بدون اجازۀ ایران از تنگۀ هرمز هدف قرار گرفت.
🔹
هم‌اکنون قیمت نفت در محدودۀ ۱۰۴ دلار نوسان می‌کند و گریگوری بروی، تحلیل‌گر ژئوپلیتیک انرژی، معتقد است که بازار نفت با حرف درمان نمی‌شود و تداوم وضع فعلی می‌توان قیمت نفت را تا ۱۳۰ دلار بالا ببرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465347" target="_blank">📅 20:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465343">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd358d0da.mp4?token=lCG4DkHF68WGMhzsq50TpFkvXuXe-3e_Kd8b5ci11RV-2O_nseJmkeEGzWvbBb6-S5uDq9rhc2fuQ0Dqd9qTo_FDOFxUAF6-GQZj-eklBcg0A7ua4Z4-GhLRjTWPKAf2P4zXxpl_kBUpGK7SEYgoLGRYZkuTwMRJhLbiHiuvU9z12BhyWeSBk8SJyxzcbxfYYA1uLvL-BaCpF73o9Gv3-IZG-4PUa4udx-5Eau-N63bfKLakoEhm-iSbulKzQpr6RQISNU7nVeEo6ZeHb_eTixOnUfU7Mrz53ApvnY2iWYt5304P7X_jNedSXb-5ogPqyCtxyPXp1DWwUOPU2hRGIzgOKlkBOjuA9Dtw-Qc2SMj9keNQCXrjfBzyo02FumTXqRiTGt6ROgrmkvm3kK4lym79UOomYPxAMEpmU6gbHlgM5y6NkesLyPEWmVvDjA4N6KBU_l5VSiVdqibbG2lqfCHvdUb1q7a703gJDIdxi79X-Kh-lH5x0b0CEnX4v6N-LzVJ4vZZK_6HM2scD_UK12lET38TzgE2h1frSTxDWNctiBsCVQWwAyFndxMMzXTHWv-6CGATMqOUULex1MWu9yB93Ip7r42OOFrqySwbyIUR4QvAE-XNSxS7B-yWCLhLlwbPZXuRyRDowIiOqjDqVHz0XS4TffGrssAVR3LIA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd358d0da.mp4?token=lCG4DkHF68WGMhzsq50TpFkvXuXe-3e_Kd8b5ci11RV-2O_nseJmkeEGzWvbBb6-S5uDq9rhc2fuQ0Dqd9qTo_FDOFxUAF6-GQZj-eklBcg0A7ua4Z4-GhLRjTWPKAf2P4zXxpl_kBUpGK7SEYgoLGRYZkuTwMRJhLbiHiuvU9z12BhyWeSBk8SJyxzcbxfYYA1uLvL-BaCpF73o9Gv3-IZG-4PUa4udx-5Eau-N63bfKLakoEhm-iSbulKzQpr6RQISNU7nVeEo6ZeHb_eTixOnUfU7Mrz53ApvnY2iWYt5304P7X_jNedSXb-5ogPqyCtxyPXp1DWwUOPU2hRGIzgOKlkBOjuA9Dtw-Qc2SMj9keNQCXrjfBzyo02FumTXqRiTGt6ROgrmkvm3kK4lym79UOomYPxAMEpmU6gbHlgM5y6NkesLyPEWmVvDjA4N6KBU_l5VSiVdqibbG2lqfCHvdUb1q7a703gJDIdxi79X-Kh-lH5x0b0CEnX4v6N-LzVJ4vZZK_6HM2scD_UK12lET38TzgE2h1frSTxDWNctiBsCVQWwAyFndxMMzXTHWv-6CGATMqOUULex1MWu9yB93Ip7r42OOFrqySwbyIUR4QvAE-XNSxS7B-yWCLhLlwbPZXuRyRDowIiOqjDqVHz0XS4TffGrssAVR3LIA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی و انتقام، شعار رزمایش جان‌فدا در مهران استان ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/465343" target="_blank">📅 20:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465342">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSZ56kJ2MaatbqRHTnPfh7txOL3P9u83bnx_l8ylTJzfDg5W7IQwfYoo8osYlaRhUwgghmmRGqINgx855ahmIHrIvQ6UJpo-_9WZ4ShdLKoobW4y7elagG_mmYAvZaItqHs8P3h8lLigsWWdTBdb4GHiiRL05QfI_xOg89GjyJpcwCEJ5uoWSchmUod4t1MEFvxIdhYO5Fk0dGj4ZWlonAZZwtBiqjERD-_8tinRQF04hUCUx2ir2jvKVvh5PBT2hLOc04tTPbQsGQuE_cE7s9QMivbl1ae_C8rKH6mdf3HJSdPG0EjYN00St1t7-9JKfZ1etP0n7AoBuRxlwMJpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما شروطمان را گفته‌ایم اما ترامپ قادر به تصمیم‌گیری نیست
🔹
ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.
🔹
شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/465342" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465341">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f59ca0cf8.mp4?token=JRFw75VIPHGOtRnW_mFKxL8OlKq37Fp73je6pT_DX5VtsnTWCdiqXtCU-NjdEjIveUE2Dly3LmqqVppbalyO7JTXxJplQsyk2LJin9ElrpqzdpGNo9jphNRMa-sh0SUMVXE5jfLR55DxH2dgMk-OE6ko0TjjPOs32gRXSXuwJBn7vqcwhx2ld5IhCTo4EY5ruFijQJ6PSpaeY98fEOXYF5xhiksDyMnuPwbCfapCVTy-xns3Zbrr_FMNLqv3-H8t_N-yWdUsV0cSSOo7k7VPCmDiwWHWS1yRuKPt4-xkEHBi3ETtVjXnctW36L0tU34I_G_zZJV_Nxe8-7tTti7G5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f59ca0cf8.mp4?token=JRFw75VIPHGOtRnW_mFKxL8OlKq37Fp73je6pT_DX5VtsnTWCdiqXtCU-NjdEjIveUE2Dly3LmqqVppbalyO7JTXxJplQsyk2LJin9ElrpqzdpGNo9jphNRMa-sh0SUMVXE5jfLR55DxH2dgMk-OE6ko0TjjPOs32gRXSXuwJBn7vqcwhx2ld5IhCTo4EY5ruFijQJ6PSpaeY98fEOXYF5xhiksDyMnuPwbCfapCVTy-xns3Zbrr_FMNLqv3-H8t_N-yWdUsV0cSSOo7k7VPCmDiwWHWS1yRuKPt4-xkEHBi3ETtVjXnctW36L0tU34I_G_zZJV_Nxe8-7tTti7G5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: شرمند‌ۀ معلمان هستیم
🔹
به‌طور جدی پیگیر دغدغه‌های معیشتی معلمان هستیم و تلاش می‌کنیم رفاهیات آن‌ها را هم پایدار کنیم و هم افزایش بدهیم.
🔹
دولت در ۲ سال گذشته ۱۸ همت برای نیازهای رفاهی معلمان تخصیص داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465341" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465340">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سارقان مسلح ایرانشهر در محاصرهٔ نیروهای پلیس
🔹
یک منبع مطلع به خبرنگار فارس در زاهدان گفت: از ساعتی پیش چند سارق مسلح در محاصرهٔ نیروهای پلیس در ایرانشهر سیستان‌وبلوچستان گرفتار شده‌اند و صدای تیرانداز‌ی‌های شنیده‌شده در شهر مربوط به این عملیات دستگیری پلیس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/465340" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465339">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYd_QTE1MQUtk2tT-8imV7ckWVQ6ftmok5ynwHHzSZ0l05s2cxsosvw501GkWYSokezpAQj-ocxRpWJELOw_OmldDAjAMon7ELm97WVc0BDY3EBwpqhGb6wZGjK6XFYyLTMPJh6vd2qn1wq4DAofO4obqPaWgS0OsfEPddXFz4Gcq_eZUjk_Dac1EAcl-SIqdkCv-CFF_26JC1JEwdF0y6glSUoX2VSbvHOiLIkhOR8K98R5Ky9EnTzRKVIrext_q5Zpca0f6UD3a17SXkeH5E4b5mJWAoJLYCGDSsGgDzDdpBhDsDP-lMiv8PJQN6urkm6MFpjGssHycSvTCr5QYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکره با روسیه؛ آخرین تلاش واشنگتن برای کنترل بحران انرژی
🔹
در حالی که قیمت سوخت در آمریکا سر‌به‌فلک کشیده، واشنگتن و مسکو دور جدیدی از مذاکرات را با محوریت همکاری در حوزه انرژی آغاز کرده‌اند.
🔹
کاخ‌سفید اعلام کرد که کریل دمیتریف، نماینده ویژه رئیس‌جمهور روسیه، روز دوشنبه در واشنگتن حضور داشت و با مقامات آمریکایی درباره پایان دادن به جنگ اوکراین و توافق‌های احتمالی با آمریکا در زمینه انرژی گفت‌وگو کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/465339" target="_blank">📅 20:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465338">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHMMHKCDenqzzdCmyGVlMur4nGeKKuNOitM6D-NKAE73s_W7DsuKUXKbRkA_d9eZhR2Dm5tVSgFjG-Q24mZbo-6cz1G5tg4BrRXNXdYxRddaWUkV0924Gd0_WrWCuFdu_AXom_9niiA-5SHnL4ui7_E4ze6xmOWVfgPVXLXUtf6fiMZJ_89ZuXLt8GMvEeXyXHNuC9cenGhY-xVJJOkZ0SRBXFqHsggF3eIgvtU3GaucYuzHWjwiQMKf1HAzzj6xaQe6zXJwPQ_LHxc_O3o40L8oeB6eVe9sGPhqpzVlMxfh7J_5OIolceJDcHeNjr4SVftZfND6gUxZ0EUVziLn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما شروطمان را گفته‌ایم اما ترامپ قادر به تصمیم‌گیری نیست
🔹
ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.
🔹
شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصرۀ هوایی روی آورده است.
🔹
بیگانگان زیادی در طول تاریخ آمدند و رفتند، اما ایران و کشورهای منطقه همچنان باقی مانده‌اند.
🔹
ایران برای کمک به برقراری صلح در منطقه قفقاز آماده است اما آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/465338" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465337">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefd4b1436.mp4?token=Yy4xWpe0Na3HKPmAtTm6lBk6ck9zyTXY6FxVtTtajk37E5_F31W5vg5r7sMvuwBnRYdBj3010qkCX4ibHRPPCSn_HOie4BSb6v3Tw8T-8g32dcW4yEx8CxunZV6OyvF73LCmYeilYBmqaRE2Rk-0FaNpyvuaQdvHgz-S3T4tOGJOVBaZ8R5vxmIxt9JdBB1KK7eLTNoWq7X_h67hcwM7Hd_iLRwaXiUgzxKcd4avmNRzOVZ3vOngPsr-xHLwobLhcDJRZhuO9J3jiqW9m2L3xcdRQa57vBfw6CwKKd9h0nXoQWHdzTtZ5---cKHmTJeAm9YlZRZaXYbpODr_YDuLYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefd4b1436.mp4?token=Yy4xWpe0Na3HKPmAtTm6lBk6ck9zyTXY6FxVtTtajk37E5_F31W5vg5r7sMvuwBnRYdBj3010qkCX4ibHRPPCSn_HOie4BSb6v3Tw8T-8g32dcW4yEx8CxunZV6OyvF73LCmYeilYBmqaRE2Rk-0FaNpyvuaQdvHgz-S3T4tOGJOVBaZ8R5vxmIxt9JdBB1KK7eLTNoWq7X_h67hcwM7Hd_iLRwaXiUgzxKcd4avmNRzOVZ3vOngPsr-xHLwobLhcDJRZhuO9J3jiqW9m2L3xcdRQa57vBfw6CwKKd9h0nXoQWHdzTtZ5---cKHmTJeAm9YlZRZaXYbpODr_YDuLYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول روسیه به ایران توسط گلووین در دقیقه ۲۱
⚽️
روسیه ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/465337" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465336">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
منابع محلی از شلیک پهپاد به یک کشتی متخلف در مسیر جنوبی تنگۀ هرمز خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/465336" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465335">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5w3yS-Ms3-Iz56owxL4XcCwwSXzX3PcmpKQStlum1J5DiDCQF1ID8aJbnKurGZRWAWOxWWs7u-ALgfxW-Cw-D3_gWrf83GFJP_x2SSQx1I6nsIiGIRojzl53AEgxUuGcJTaHS_2BNb6HTceQqavoUtanRb6OaR62fLzPuaCgGFW5U446vyJ27TbfHHJJBiybLNMNq7Zn0OgccWfq_WNy4nGEI69vCQU71pcMd6Yv47OItTzi7aBeMr_6zdvOpF40dEwoPEdfKmH3SDl34oFu1Rx-JPA3HuA63fq9ZpO-veg2bNV8z4dyrEZ96cN3px7X8kZEZT_BcT_lT1aR7lhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات عربستان به مدارس و جاده‌های یمن
🔹
عربستان امروز در چندین حملۀ هوایی، مناطقی در استان‌های صعده، تعز و الحدیده از جمله یک مدرسۀ روستایی و چند جاده ارتباطی را هدف قرار داد؛ به گفتۀ منابع عربی علاوه بر چند کشته و  مجروح، یک دختربچه نیز در این حملات به شهادت رسیده است.
🔸
در روزهای اخیر، حملات هوایی عربستان به مناطق مختلف یمن ادامه داشته است. یک منبع نظامی یمنی، این حملات روزانه را «غیرهدفمند» توصیف کرد و گفت که این حملات اهداف غیرنظامی را نیز هدف قرار می‌دهد؛ این منبع هشدار داد که حملات سعودی بدون پاسخ باقی نخواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/465335" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465334">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6d292dc3.mp4?token=JHHC9ZCoVnYdRelkFwM176CokjyfY95fn9llzP88UTvYO16Cx295g3UfFQRx5oG7YXvm2vskVIyf6q1D1JaSMXcPxtVhO6KVtUOteX4u5i8hxgd1-VWXqv1I3WWMWVe5hfvSgUueWQpJjpv6tSWJ968kZFZ9L1EeeenqxijUNaAwBMb07A2kBp1YMVeteFzPFvxQlvIqHtJuxZ1GNZvUTBVT9zNNSYDwIgotiu_JgGNGZB2tEIvAQxEPMvanUmGCK6AjMeg5VfcQMSr7vwGfuspRsMEvHosReOn3P9eYxNMQ_hYsO8vSgN1uqrAHM6Ud4-IIis9Qyzw1zjKrcV_tcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6d292dc3.mp4?token=JHHC9ZCoVnYdRelkFwM176CokjyfY95fn9llzP88UTvYO16Cx295g3UfFQRx5oG7YXvm2vskVIyf6q1D1JaSMXcPxtVhO6KVtUOteX4u5i8hxgd1-VWXqv1I3WWMWVe5hfvSgUueWQpJjpv6tSWJ968kZFZ9L1EeeenqxijUNaAwBMb07A2kBp1YMVeteFzPFvxQlvIqHtJuxZ1GNZvUTBVT9zNNSYDwIgotiu_JgGNGZB2tEIvAQxEPMvanUmGCK6AjMeg5VfcQMSr7vwGfuspRsMEvHosReOn3P9eYxNMQ_hYsO8vSgN1uqrAHM6Ud4-IIis9Qyzw1zjKrcV_tcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
۳-۵-۲ سیستم جدید تیم ملی
⚽️
همانطور که قلعه‌نویی وعده داده بود سیستم بازی تیم ملی در بازی مقابل روسیه تغییر کرده و ایران پس‌از مدت‌ها با سیستم ۳-۵-۲ به زمین بازی رفته است.
⚽️
میانگین سنی ترکیب اصلی تیم ملی در این مسابقه ۳۰.۷۸ سال است؛ آریا یوسفی ۲۴ ساله…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/465334" target="_blank">📅 20:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465333">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030de33e81.mp4?token=YsJ9wq0s3kMAnJoEhdw7uE-FObBtEf21S3bt0ADpFfzsFUtvVFwG-2pzBlOVBLSNspLM0sHGhSmf3amFmCqjg9SYmMO-kS9kBU26W-2lXG5kk3tkBZR75vvHs4i1Pv6DAJ-wpu0HRI5JYFORl65UEasflcbUxhxGpbMVaNfkCMqyf3lj-6yJ53tc3j4hzK9ePln05-iZid6CBlMWFZNKt2eb5Yq_4-op8E2zVIwsDtFTQVT4cHCtszWuxmAeQVua6CjJkRx1-LDAemHxd8c2UyxzYjUPZSMS7gkuBfrF_vnADDP1HUGdKOGKmQjc81q0aVbCx-jmaq3jXtfpci4C3Sgvf0kgb2K9Y-BNYUkh_CtzowS5XWopvebBiGxXiSAHoagIq74KNF-2Ykg0QeMxsA9r3RE55TjMr-Kd95tQBtoHIHscErQCNLUQPaRNNuLCKy84h7m6eB3z3fIUcUNsI1PHIi91qu5kECcHUBJb8mcNWi6tTV6K_i8NnL1L0bMUiPSat8hCKJiaZkV_XuSjqut4ruSpwc5opdFPw040bH470oBOlIxHLA1HJKRPsHaDgLUXsdJiAXleKzzXj9EYn6SUzjqW4hPmDAvNhowt9euDPvzhGEzaJkbEj3M28BUrz-7JZ9vQ710nZ2Zys8PO6kbvrJdPOd5xuNpT9wm_kkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030de33e81.mp4?token=YsJ9wq0s3kMAnJoEhdw7uE-FObBtEf21S3bt0ADpFfzsFUtvVFwG-2pzBlOVBLSNspLM0sHGhSmf3amFmCqjg9SYmMO-kS9kBU26W-2lXG5kk3tkBZR75vvHs4i1Pv6DAJ-wpu0HRI5JYFORl65UEasflcbUxhxGpbMVaNfkCMqyf3lj-6yJ53tc3j4hzK9ePln05-iZid6CBlMWFZNKt2eb5Yq_4-op8E2zVIwsDtFTQVT4cHCtszWuxmAeQVua6CjJkRx1-LDAemHxd8c2UyxzYjUPZSMS7gkuBfrF_vnADDP1HUGdKOGKmQjc81q0aVbCx-jmaq3jXtfpci4C3Sgvf0kgb2K9Y-BNYUkh_CtzowS5XWopvebBiGxXiSAHoagIq74KNF-2Ykg0QeMxsA9r3RE55TjMr-Kd95tQBtoHIHscErQCNLUQPaRNNuLCKy84h7m6eB3z3fIUcUNsI1PHIi91qu5kECcHUBJb8mcNWi6tTV6K_i8NnL1L0bMUiPSat8hCKJiaZkV_XuSjqut4ruSpwc5opdFPw040bH470oBOlIxHLA1HJKRPsHaDgLUXsdJiAXleKzzXj9EYn6SUzjqW4hPmDAvNhowt9euDPvzhGEzaJkbEj3M28BUrz-7JZ9vQ710nZ2Zys8PO6kbvrJdPOd5xuNpT9wm_kkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگ مدرسه‌ برای یک قهرمانِ کوچک به صدا درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/465333" target="_blank">📅 20:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465332">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aag4uWyt1168nEjqWyInZQWL9srxxceMUQ13HKp5MeYD9cqiwR153p8rk0vGzjAsc-BA3Dk6rEIt-zceZi5sRpVpe3sF7e1JhWWMvfGAFglR5wi-rJD554ljbj87BVIQysohbolp5kwhnaV3BzzhNxbnL87bC-HHLgujbbmejgnr65T5q2iXIEotlvNpLCUgcBLovYF-sWyPl1ULyojQbE9xYd_i3bqVQAmvPVysyUVwNhD5v2pkYHA8P_T7ZoQ58P2tTDi9CTkIt8K9Z9qDosSzVzwIckV5N0sOsVZvmO8UPXlTK8-OO5xiZdjVSB4S2lrPUQga0SG5va8tvg5D5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: با سبک جدید به مصاف روسیه می‌رویم
⚽️
می‌خواهیم از بازیکنان مختلف در فیفا‌دی‌هایی که تا جام ملت‌ها فرصت داریم استفاده کنیم تا مشخص شود آیا به عیار تیم ما می‌خورند یا خیر.
⚽️
متأسفانه در بازی قبل به‌خاطر شرایطی که نمی‌خواهم بازش کنم، فرصت حتی یک…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/465332" target="_blank">📅 19:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465331">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab59fdf9e7.mp4?token=ULDG-XxabsZK6QzbxfwnC_h_pPcgKcCOdqXo1wwn8xKxveNJDnZsZ4jjC0_V1GKxjKGx-tLnvKOBA6sLuAoH7SJoRqilLpblCEZqCLJJCq81MGMuIAqoIv-0iKixgmYSTjs8JbkLRbyj1JNV-5iXa-0hPs9YQWY7_7_nywsYyNlbKEXg6FN684GYs5qLcYLv1tlCCNJb5o6iz6pzn9cmY3vEVo83sAGKxeGrcw-3MXpMqurbki5cCQcRkkIZBFF8bRvxWwLRqKx6HLHavUXo_jLLrmHJQb5-XxCaeEloOlSoGPJzb8f2BWGvDquMe91a--zV5SdqGV-t0CoCVhZ1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab59fdf9e7.mp4?token=ULDG-XxabsZK6QzbxfwnC_h_pPcgKcCOdqXo1wwn8xKxveNJDnZsZ4jjC0_V1GKxjKGx-tLnvKOBA6sLuAoH7SJoRqilLpblCEZqCLJJCq81MGMuIAqoIv-0iKixgmYSTjs8JbkLRbyj1JNV-5iXa-0hPs9YQWY7_7_nywsYyNlbKEXg6FN684GYs5qLcYLv1tlCCNJb5o6iz6pzn9cmY3vEVo83sAGKxeGrcw-3MXpMqurbki5cCQcRkkIZBFF8bRvxWwLRqKx6HLHavUXo_jLLrmHJQb5-XxCaeEloOlSoGPJzb8f2BWGvDquMe91a--zV5SdqGV-t0CoCVhZ1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویانمایی ویژهٔ
RAHBAR.IR
به مناسبت هفتهٔ دفاع مقدس؛ روایتی از حضور آیت‌الله سیدمجتبی خامنه‌ای در خط مقدم نبرد در دوران دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/465331" target="_blank">📅 19:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zzb1F2-M4IjOhGuFzLYwKAYOY13ryvLBBui9ix2Pk6QPaY4oKhM_nY6B8T_SsMeNLcVOlmiFBOh3NSVhXkiEUZDRH9CJh4OHgjsNhrwKBglGHJzPkdd3JuyLSMT5JiBDzXpQeidFq5SU3Ht7VPGkpPsdVj12fZamefUYJluJ5t5tEs7mGrDxXpt3pBA_ewIuan_q4Vah73dKeDe6KVuET-3FkXJw2OpDkFxpEWo2Jbonm9kPqQkrmpgpZNF69mMAsVkMGlK_aNKQqIokpze5neOUC7B7XFMOBNt42TmZFvanD-Q0YQ5oO9s77eXPuJ_qC6IW2H2o6X1zbgoMON9V2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFqudJLuo7xLreqiLmxXMhUDyDvwI7tQ27BDhZno3NWjSgCteXSWJgmEcyAn43tX9xUw439_78Sh9q9ki5hRDDJ7P417ukFqP9dID6JfIcKK2DN0Y7hDQspmoamy-wNFG2vRDn686_stJhfirtkkOr77gFOtnlBAEo4Xts6WefYWBq-4Jf84HgoyhxMWeO5U7ijxPMgvyGa_QsyaVMpOBWD_RBsvUrJikAYbXXi5feCCptOUpzC8UAzF8GrIBRz_MK59A0eUqzibUfNsIjNPsxvcr8cz0pYW1o9PulrNnxASGQASPmKg2U9JrTfp1WZOtEN4jNZQeMDNTjdg9wSW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2L5qf31prdVisU4aY-AvQRWwG-jYIhSB8K9jDri4r8gxoicEeyLV4PKyddpHkHz8rg2gkeuvM9ahcXoRkJouSteM-tsSgredVnccUTc4llAX5WKY4ISEntmbbQpVfxNDnJKPjG8hYxHWuWvo7YeFmyV5GfiE30k4tB7ebgg5WMFYL6b9NIZvqNVOUuvAJfBf7RDsKJUYuyUZGo9Vr_bWn09mExWYen1rJE2XAnPi5eZhvdnaxaceZIJDhM4iI7J48blakG451fEg7W9TMsKJfTk1Vcj9m-Zq7AGfZaZRuicsyF9E-f3VAjqN-xLAK4NvIXdMbfBKEdYaznHn0LbyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: مرزها مانعی برای توسعۀ روابط ایران و جمهوری‌آذربایجان نخواهند بود
🔹
رئیس‌جمهور در دیدار با معاون نخست‌وزیر آذربایجان: توسعۀ مسیرهای زمینی، هوایی و ریلی زمینه‌ساز تحکیم روابط تهران و باکو است.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/465328" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_XtzG1LWttbjqOlN7JsS94qXEzO1yIDHDTHyPts7YNM8quBytu9D12ATeKjVfjBpbHwOGURmgjIeknrNcDW0AG_TXEMl9Wa4f5tfMi3qWul0WgbNfFGd6H25kT36Ievy5ClS2tnM_34WO0xe0kpzw4oF0LHVIducFyYremJm0ReCaq2gLzdg-YBvnZbC1hy30V5VYPcRpGA2ohR0qMxA8OAMywrBpG22U7W-tX5ateoxtMMk5pctuUPEoGhzFTr3CsKdaL3ivkjME3LpPavy8EEjj-yFwId7PXmJPNH6SPpn-1A_kugySFs1k4yNhbc1cYpGVOin1JG_1bCkxp_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویری از حضور رهبر شهید انقلاب در منزل خانوادهٔ شهید یزدانی در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/465327" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760db79b09.mp4?token=Uy9RU124mrEX5Mv62jbVjhQ_e6Ccp-xrhQJucgOFNK3qSEyKn1KbuFB3DOxBnbQgShVcn6AcC-H7aFNOiuZv23zPwAhX2TKpHa3qRoNZ7FICJf7ut6nrCh6gOHdlAkOD32a-4ir643s4rm1iRlLBGX_MFCr-bkybH6k-8qmcfqTaEfgEmVZ3slPYUjgYtcxrzKqgn0UIQ4qRyKWARZhInTcYv1JJS9-qa8KZvyrmN8qkRSTKt_fG7IojlRvrWCE1cW2yMht0OK4AvxNRmUECZNf_sml-4dSuEaGAUsejFacwjMv6jsZpXMvqS0p2816eIaMVlwpIJ2E9-rTNTTYlx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760db79b09.mp4?token=Uy9RU124mrEX5Mv62jbVjhQ_e6Ccp-xrhQJucgOFNK3qSEyKn1KbuFB3DOxBnbQgShVcn6AcC-H7aFNOiuZv23zPwAhX2TKpHa3qRoNZ7FICJf7ut6nrCh6gOHdlAkOD32a-4ir643s4rm1iRlLBGX_MFCr-bkybH6k-8qmcfqTaEfgEmVZ3slPYUjgYtcxrzKqgn0UIQ4qRyKWARZhInTcYv1JJS9-qa8KZvyrmN8qkRSTKt_fG7IojlRvrWCE1cW2yMht0OK4AvxNRmUECZNf_sml-4dSuEaGAUsejFacwjMv6jsZpXMvqS0p2816eIaMVlwpIJ2E9-rTNTTYlx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش جان‌فدایان مرزنشین مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/465326" target="_blank">📅 19:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465325">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2AO2SVe_Wwo4i1IoLea0DTvnKCg8swfrf5MrNXhTiPVjWrkc-QrXXroxGgF2j0okXLPQ2A_5QvnkLRUL9F0sZE-Qbc9Lp3qRSJuX_sW5vjlVb0oPLvoCtWCB-EiZ9xyOONrP7DPHhO1mFcs1Yw0und8W240Ge6LJee-9u84frdp0x7UogFcCMCyO4Tb1EP1I_Xscx7Y-BZDB9UQsQ5BV_x_Jt4w2PSsq-QrOeoQwmGD2gCEne1mDysRjNdBrKAIGggH0xWrkjirs-BL-U8xE427Emm4KwIGsLiaVUn5yMwVcUB0vxpRxriicLTrFTKlZJ8t3uoaEGhKYnP4oAAVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ثبت رکورد تاریخی در تاپیکو
✅
رتبه هشتم بازار سرمایه با ارزش بازار ۵۱۵ همت
🔸
تاپیکو با دستیابی به ارزش بازار ۵۱۵ هزار میلیارد تومان در معاملات ۷ مهر ۱۴۰۵، برای نخستین بار به
رتبه هشتم
در میان شرکت‌های بازار سرمایه ایران صعود کرد.
🔸
به گزارش مدیریت برند، روابط عمومی و مسئولیت اجتماعی تاپیکو، شرکت سرمایه‌گذاری نفت و گاز و پتروشیمی تأمین (تاپیکو)در بازه یک‌ساله منتهی به ۷ مهر ۱۴۰۵، با احتساب رشد قیمت سهم و سود نقدی، بازده کل 251 درصدی را برای سهامداران رقم زد؛ عملکردی بالاتر از شاخص کل بورس،  هموزن، شاخص گروه شیمیایی و نیز بالاتر از عملکرد هلدینگ‌های مشابه بورسی که از رشد چشمگیر ارزش سرمایه سهامداران تاپیکو  حکایت دارد.
🔸
این ارتقا، نقطه عطفی در جایگاه بورسی تاپیکو است و این هلدینگ را در جمع هشت شرکت بزرگ بازار سرمایه از نظر ارزش بازار قرار می‌دهد.
🔸
کارشناسان معتقدند بهبود ارزش بازار و ثبت این جایگاه، ظرفیت‌های سرمایه‌گذاری و توان ارزش‌آفرینی سبد دارایی‌های تاپیکو را بیش از پیش در کانون توجه قرار داده؛ ظرفیتی که توسعه و بهره‌برداری مؤثر از آن می‌تواند پشتوانه خلق ارزش پایدار برای سهامداران باشد.
@tappico1381</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/465325" target="_blank">📅 19:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwQQrCBUDQe50EE6ogp-Ug15ADNaj3eRs-2li67-TqTksEVfTO-JTmktw4ctdiin33dHdPmJd3YkyLzCwVi9Qyncet5h9ydP_UB85B1TcGh8UXgOKVBpjVW26zsFih75J8HN5sokzcbrkHpzzOZFckVVw7U3OM6_SSbIN05mRq3-4Vqgg8jZHeuO1zCYJCUVlcXPsXcCStx7z21kYtsM007JwFKaE9ctRw5vQAWrLiaCe0ZKu0UqKEvR2ux8_EVl_oM1P6HeSMG-Ttu0NF5io3uhxIRPs2wMJhfxQo8CK17chsFUnezyaXC_zkWj3PSjSytM9tt9cq6XvEPkhaevBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
سفر وزیر تعاون، کار و رفاه اجتماعی و مدیرعامل بانک رفاه کارگران به استان خوزستان
🔹️
دکتر میدری وزیر تعاون، کار و رفاه اجتماعی در راس هیئتی از مدیران این وزارتخانه برای بررسی مسائل جامعه کار و تولید، بازدید از چند واحد صنعتی و تولیدی و گفت‌وگوی مستقیم با کارگران به استان خوزستان سفر کرد.
🔹️
دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه که وزیر تعاون، کار و رفاه اجتماعی را همراهی می‌کند، طی سخنانی هدف از این سفر را بازدید از برخی کارخانه‌ها و واحدهای تولیدی و ارزیابی شرایط فعالیت بنگاه‌های اقتصادی و مسائل مرتبط با حوزه تولید و اشتغال عنوان کرد.
🔹️
بررسی شرایط رفاهی و اجتماعی استان و پیگیری مسائل مرتبط با حوزه‌های مأموریتی وزارت تعاون، کار و رفاه اجتماعی از دیگر محورهای این سفر است.
🔹️
دکتر اسماعیل للـه‌گانی تصریح کرد: حضور در جمع کارگران و فعالان اقتصادی و بررسی مسائل و دغدغه‌های آنان و امضای چند تفاهم‌نامه با هدف بهبود زیرساخت‌های شهری و آموزشی، حمایت از جامعه کارگری و توسعه مسئولیت اجتماعی بنگاه‌های تولیدی، از دیگر موضوعات مورد توجه در این سفر هستند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/465324" target="_blank">📅 19:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/465323" target="_blank">📅 19:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایتالیا هم از عراق عقب‌نشینی کرد
🔹
درحالی‌که آمریکا در حال خروج ارتش خود از عراق است، ایتالیا روز سه‌شنبه اعلام کرد که روند خروج آخرین نیروهای خود را از عراق تکمیل کرده است.
🔹
نظامیان ایتالیایی در عملیات به اصطلاح «عزم راسخ» به رهبری آمریکا علیه داعش و همچنین…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/465322" target="_blank">📅 19:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdU4Zvg22j3G_d15HYd8j6zGVzYOxsM0TumHE_iQ30D7STZvryz9DoX3s_KGjPRHVQNffwx2P2bxSVA_6Bav84LunWZ75wTHUCOCEYHNz98xvntQJ9Z-HeAHWqrpCyjVQM3bUwiapkzhfYaz406LH4cCjCmGKl1MXdvhcEBYiqoljsCRTk-yEkcI2L-8CJgqJvxFyfwQ0q0IXmSuS3AamOMsEmIuGRn-GGVIBWAsPI1-YIcMj1eWaKRR7LkKwZEzIZ7srOyIecjlqV6jGUBB4FFzjHbMDjrRHLiAnQd7wENCUrPXzAe7atDChfnAWyhvRPemr6HDhqnAWSxT3M3S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRz17409QJ0nfUfec_PDLJY4S2F_ozDdykZeoJmTeBvDl20WUrNLOdDPYUfjaMj8TNeswH5PDI78S5ml70o7ryjn5f1PGTQwJC6NJV980zoeTQgy6tVXZdojYGMFMNYpFneYdaKeoLPNC7EDADcjQSLDPGSFX-vrEj8hrLOUd7Ynt2jpwUMlUbxXf8TTV29osM5G6PRNSfbFdiFPYCrwoPIm8iZvy0P8O1F8DTy8KWX2H12kjT6N6r-SSgx-qG4X_4TRFeroR0Yt3Ubk6-Q3eQYfPClOZsJTbk5JbYEYhANjgpowU9LH4jd9GRtz9afUXxSCd0tfR0bhGPq3VnBtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DshOdu4KoWaP4Lr44cidy7rVXSQNJoZ2KqLyHHs6mZeRiQu0zRT6w2CXFnWp4dXaa2ki2CNHSyuSfv7QisOAkhQS16LGxYYW5JZiWnRma9sORb9EXdQpptoyrf0wu2UJy5HU7zcxmMVSU3MX-cnkvTrk55qXNDJ3CxbDkSiMeMhuBkDUgdItim3blwRWlZxBT-zGLj-3lcHrVrLQOptIgG-X-ggjtm8X3grYiozRpBCqlAgsE8iE6sHNCY2MUHdHXYJHYET1Emm-RozjxsL5w6G2axabCeb7Y0sOZCkAmmnU1_d_m-my10RxIbb-pAvzrN8hQFkT3cZQR7FMHeEnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFlSkzdjjY79Z_YH0dWUhN5674g-LKPAo0gX5pl4TArUQR_eGShc46IMOxk-ndFC3_F1TEZYxEWzkRO1rtYMZ0yLdIYF0kZYhulejyiHlHryW8oBCZG_z5-BB-iDTyqTN_LtBHpHRyrA7yf24Y1840Pnudtqq9CRLkeq8i_XcXfCNiCb3s-v-lD4rkfH387Yy6olHYN_geKaUHFABREM5Hi3mSRT3bpz3bOA9k_GxT8spyC5vdz95n_uODONPXZIPfkDweQvl7VTyliuL9vtFUw9zczZBdWn7zIPuTsPFVwY6bzhpTvkm5L1AXPwSRraiunTW633QAlu8G0L7KVJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUY-4ZC-S8jGavw4Qxo-eEQBs5axxTA_umlKb3scHmKlWELcLP49ZbLpbzH1ueX9eYdj8Rn4JSGmi1mjBftf-qUSsGk-RBOpPZuyzlvw1gYcX7iidBIGZ7iykcZGMGRI6A-j072F_NNxuQ-7LkyoWTuPTwEWdmO6As8qh6HiAw6N9xyg3CUil4DiWfL0xDCcLjxkZYf_Vhj2eI8pTzMD4xY_76iRRcsS5sGFz8x4V3boMAiY26OSum3owTUJ5QyMoE5fxOUReUf-ZjCq8slmScVLgE_fPJ9-4Ruj1BRC-Jh6aTQO-89DNkXS3u-RutQptYhksC_hnNh3Y3x_21mF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3pKgRPc6lbBaqoGzN63YZdtJZznL0n1AQYoGIRnLFWl6rAx9Ex_pApEfbmoPN254eVGZpYbEvaMjpwatp00kZnr9-L4nFJm27XHb0IdwahAJOtnYBVEyRl5TyYi9p9i5AKspyoRkZN01Wcemtt1YXlllyruxmKixCsI4qr1s2aLjroWayDR-kji5uNRV5s4yZhF6uD8VRxw8vxeENXsEVdDBhC_j4F_Lp5q01VZfKPOmB98ns7RavRrBoeR6yGalVfPiAUOCd57A13VYaZfHuRTItTh6mipcHfrhHxofGGl6XrEe-1OjLRGowO9FZTm5gMbILMmd-YzwzKGG9l5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itq8A4DfJOznogZY8wk5J31njZ7cAMLmrb45jmoP0tssfJmjff_2EHdTgfL_XBQNg8nMI45Ygp2zRVseuN7E3MnZqHOr32IcaWQhdOZKGIB-n2EephqjZxtbJ4_kwr_pc53uMM-owNyxvrHRc9nmmKklzds33PPK6EbF4qWXfQxeLOArnqOU_o_dHEsmvWSwzsp4GjW8S7Zt2CUkPzu41Rft8mcAAL9tW2XR1NUq50Qxn9hjrAyVtBJrw__YHeBmP1szdtyROYi9Tq0c29ydMZpARu-q_olinuOtiNfjElXHV_IZM32V5XP2P76UY6ITUyE3SoEBgT6eBtdYx2H4ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری سخنگوی سپاه با رسانه‌های داخلی و خارجی
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/465315" target="_blank">📅 19:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dad3f075d.mp4?token=LnH25Z6OcvBaFQBOQMXnZUSM1D8pXYjYeBv_-YWfWAc0FyP9PJagynoyzxybOPBNlvOBHY-eP7ZCKOQXKwfhg4RUZXwVAwlu6uNmVFf54YNCNS-u2vO0CwW9wxf5G6HERtXe8gFiCw9IprLIvP0DOeVeSe74sWpxU5jEtRtl9ep_E7lezX6pGeNOY6Sz41zSSpq3fmSyC1v_ztfX4TDNuiFmryk1mPN5Hi_VdhUhr1M8jab24VHbDS_5tIXPCO7ozBtHa4TF8i-MQo2RrpxH1AtkJv99GLA62r-yTreqzd6Y8xVY5gYdRQ0BQJx3TOaOu6u50pMF7ZtUy6HqZwdc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dad3f075d.mp4?token=LnH25Z6OcvBaFQBOQMXnZUSM1D8pXYjYeBv_-YWfWAc0FyP9PJagynoyzxybOPBNlvOBHY-eP7ZCKOQXKwfhg4RUZXwVAwlu6uNmVFf54YNCNS-u2vO0CwW9wxf5G6HERtXe8gFiCw9IprLIvP0DOeVeSe74sWpxU5jEtRtl9ep_E7lezX6pGeNOY6Sz41zSSpq3fmSyC1v_ztfX4TDNuiFmryk1mPN5Hi_VdhUhr1M8jab24VHbDS_5tIXPCO7ozBtHa4TF8i-MQo2RrpxH1AtkJv99GLA62r-yTreqzd6Y8xVY5gYdRQ0BQJx3TOaOu6u50pMF7ZtUy6HqZwdc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ادارهٔ نظام‌های پرداخت بانک مرکزی: از ابتدای دی‌ماه، پذیرش چک رمزدار در سامانهٔ چکاوک نیز متوقف می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/465314" target="_blank">📅 18:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بانک مرکزی سراغ ۱۱ رئیس شعبهٔ متخلف رفت
🔹
بانک مرکزی: در ادامهٔ بازرسی‌ها و  رصد تراکنش‌های مشکوک به پولشویی که منجر به اخلال در بازارهای پول ارز و فلزات گران‌بها می‌شوند ۱۱ بانک متخلف نیز جریمهٔ نقدی شدند.
🔹
با هدف ایجاد بستر لازم برای فعالیت‌های اقتصادی…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/465313" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3bcb2e5e.mp4?token=baFPevZv0b2Bdxd_5UWXo2qgRq4pPsACTGr_ORHD6FMV2zPIfrNhHAAp0AMUGPG3uIAOibH587F0d4Sz6rq3i1wNEma-OTUeX8BlQZpOK8W3a79b_KkJGmeQchMJzVCcJy4AApuQPKBr54PvERQ5vCRfukJi3qew9W9JIv5PDI6ksEgSvJb4UhtSWk4XEgAW7S-__Y1bGs-N414hf60TRGuaZNtSPv8DR0FXC0P-XMkrNY7SMgCjVp0PKKYf0gCtN9N9pZaSJOfd7v5HhFpOVIGPSkkf1HIReEhD0hSlBkWXnplnU7hxcdWDYsgWoHsw-gFfG5QZKclHLxIrAGybvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3bcb2e5e.mp4?token=baFPevZv0b2Bdxd_5UWXo2qgRq4pPsACTGr_ORHD6FMV2zPIfrNhHAAp0AMUGPG3uIAOibH587F0d4Sz6rq3i1wNEma-OTUeX8BlQZpOK8W3a79b_KkJGmeQchMJzVCcJy4AApuQPKBr54PvERQ5vCRfukJi3qew9W9JIv5PDI6ksEgSvJb4UhtSWk4XEgAW7S-__Y1bGs-N414hf60TRGuaZNtSPv8DR0FXC0P-XMkrNY7SMgCjVp0PKKYf0gCtN9N9pZaSJOfd7v5HhFpOVIGPSkkf1HIReEhD0hSlBkWXnplnU7hxcdWDYsgWoHsw-gFfG5QZKclHLxIrAGybvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کینۀ انقلاب از دل سیاست آمریکا خارج نمی‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/465312" target="_blank">📅 18:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyulXv0fn2RTEUf6OrZN6KUxK3IDUH2kPEEYYAGOg0cd0qENTVn6epsAMpY8-CfOgWEfAOnuQtf-uMacSiW7eGNTk9FGmQEZMcJtgWEPkmwYvI62V7Y6l7kwAl5YVMuF8yzmQl-nl7H1tggKWiJLaWEDyaR2bodm5PmA8fkmhIs96zVgQVszZPg1kRXliSYx9vRHEBvBvBT-TStnyee644iHcug1nvKmbNT2y5LbFYYvY-pw9EVC1HkmaGx5N1j7l4aMBiogqftCpE1xf8mw3wy7isPoYarzcJkJtNzZnDH85BMbkxK3LTLNPRqnUzDU_zMpcxk80ZgI6V__YFi1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: پروندۀ حضور نظامی آمریکا تا دو روز دیگر بسته می‌شود
🔹
سخنگوی نخست‌وزیر عراق: نیروهای آمریکایی و ائتلاف بین‌المللی قرار است تا ۳۰ سپتامبر (دو روز دیگر) روند خروج خود از عراق را تکمیل کنند؛ بغداد همزمان بر کنترل کامل اوضاع امنیتی و پایان حضور نظامی خارجی…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/465311" target="_blank">📅 18:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTKAUuqAbEcwwwOBXM1WB-CweTCFmjdVHVbpm6cUOcmSgAIQkO1KdabExqmokHk9QUMRPCIL7vQ-GerQlSs2wcIMNvprfbUEa7ihDPIOCu22qggMIM1QlITT9pzqMhQP561yEu2fi_XbRkGpQpHTS4nzpmg7TQTUPWBc20Db1apNrk4MQm8cuH8H_c7Hh06OkV6yQPxeVbbeNjQaD1rjMj8dOiJypgJZ3y9kxruEG66WVDUp-EieOhJirdWUXdkFNMn0O5UpU9UviFfsBlmhytpWf9fTzwQUir862a5rJwUiqb8s0de9mMdMix9N2fNib4vXpdb-rhB6ERvwrE-xcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالیفرنیا ترمز ارزهای دیجیتال ترندی را کشید
🔹
انگجت: کالیفرنیا با امضای قانون جدید، مقام‌های دولتی را از ساخت و عرضه میم‌کوین منع کرده است؛ ارزهای دیجیتالی که معمولاً بر پایه شوخی‌ها، چهره‌های مشهور یا موضوعات داغ اینترنتی ساخته می‌شوند.
🔹
میم‌کوین‌ها نوعی ارز دیجیتال هستند که برخلاف پروژه‌هایی مانند بیت‌کوین، معمولاً با یک شوخی، تصویر، شخصیت یا موج اینترنتی شکل می‌گیرند.
🔹
محبوبیت آن‌ها می‌تواند به‌سرعت بالا یا پایین برود و همین ویژگی باعث شده استفاده از نام و تصویر افراد مشهور در این بازار به موضوعی بحث‌برانگیز تبدیل شود.
🔹
قانون جدید کالیفرنیا که به امضای گاوین نیوسام، فرماندار این ایالت، رسیده، صدور میم‌کوین توسط مقام‌های دولتی را ممنوع می‌کند.
🔹
علاوه بر این، شرکت‌ها نیز نمی‌توانند بدون توجه به ارتباطشان با دولت، میم‌کوینی را با استفاده از نام، تصویر یا چهره یک مقام دولتی عرضه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/465310" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU90eplKiRmxGMqXSr6OxFkWD0YT4VDJ1nghgxYc5wdMS4_DA159Baxvy6EVLmx3YJFHdP67rUeNr5G5umtWn5TpsZy7dp03fluJnLjEN2Us4p1S4R8RHjyjpktk-2wssMdxiQAfsXKDFZf6UsetlN-xdEm2oMIkG2hXw5C1l38rZnEwo_XBM7juzRKMBjIByNiHBYjKXF8182SD6RQiqf4kcIDw4skg-dD_BR1IM8MRp-J_Rs7ddj5tlYqhDvcEFYqhGOgr7wqVpCAfSgqGTrwxaYJ5yd8XX4Bmso44FKxLg2SbudWDEbQ4X6RH7VrqykMuq27vFh7ZEKmcs6yAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: اگر بفهمیم حملۀ دشمن نزدیک است، حتماً عملیات پیش‌دستانه انجام می‌دهیم
🔹
امیر سرتیپ اکرمی‌نیا: شهید سپهبد سید عبدالرحیم موسوی با جدیت این راهبرد را دنبال کردند که راهبرد نظامی ما یا دکترین دفاعی ما به سمت آفند پیش برود؛ از پدافند به آفند. ما در این جنگ عملاً این راهبرد یا دکترین را عملیاتی کردیم، آنجایی که مواضع ضد انقلاب و تجزیه‌طلبان را در اقلیم کردستان عراق مورد هدف قرار دادیم.
🔹
این در واقع نوعی جنگ پیش‌دستانه محسوب می‌شود؛ قبل از اینکه دشمن دست به تعرضی بزند، مورد هدف قرار گرفته است. و شما ملاحظه فرمودید تا امروز ضد انقلاب نتوانسته است که عملیاتی را علیه مرزها و مرزهای زمینی ما انجام بدهد.
🔹
در آینده هم به همین شکل است. در واقع اگر به این نتیجه برسیم که دشمن حمله قریب‌الوقوعی خواهد داشت، ما حتماً جنگ پیش‌دستانه یا عملیات پیش‌دستانه انجام خواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/465309" target="_blank">📅 18:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNmnWEFoZfF-KL-4SafzwdtwcRT_QrYz9ObAKP_CAtcR-amTbBmhQlMbj03szZHD1MQwHwQavgS5Sofor3nuvNOBoX7V_Kzxt5qN33PrcZZCCVGhRy15Zvn6RO1-jxc6R45xbdJb71nVTIrA0U6xOcNI5nQun704W8DI1XBzhjRlo2IrPPFmo6ujpvjfvvgphojmQTdulwBPcPF1Jpj-lw6ClYf1ksU2WnnDu5El6v4RxPKtjYRVRE-ntBUPfzTvCE0k5ZQr5eW5brgB_e_8Q0hz7WhPEffJz1eZZMDZObpTAUZS7oNiVGIrSWzUNDL5K8efOCnC_D53HvorKmQRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیارد فوت‌مکعب گاز به ایران رسید
🔹
فاز ۱۱ پارس جنوبی با اتصال چاه دوازدهم، اکنون به ظرفیت تولید یک میلیارد فوت‌مکعب گاز در روز رسیده است.
🔹
پیش از این، معاون برنامه‌ریزی وزیر نفت، از بازگشت حدود ۵۰ درصد ظرفیت آسیب‌دیدهٔ پارس جنوبی به مدار تولید خبر داده بود.
🔹
پارس جنوبی حدود ۷۰ درصد گاز کشور را تأمین می‌کند و از مهم‌ترین ارکان تأمین پایدار انرژی کشور، به‌ویژه در فصل سرد سال، به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/465308" target="_blank">📅 17:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdumRRhwxayflojaTFMNpKbTe-u1rylvbqaxj0Oyg0_pwDHN_HJzh5cw0gTkKca72czQGUNOwGaDsgCaOcrLHQwlrSxTOVn5IZxd4bWWKAiNTGjlzj6Qkklpj9Smt784BvOlImhXWUYqyZua0-A-R5ALMf0kcZMbcej1zgtv_X2Mu-WlJoEoDkQ_bs-EEKoVOWZ7sXyI01c7zVQkGCY06k9z98BFtX8ez2Rwqj5dJ2g0Xjz6-kqkWxz93d8lqkkZhcvIVv0GpdgLbr0jmHk302bP5ovZifd7iqL4tNGBfup7CiP0hfciD9R4xJIIPQF8Eql3O_rYkqlVi_dfIy8nyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد هسته‌ای روسیه روی میز ایران
🔹
رئیس شرکت روس‌اتم، گفته است که روس‌اتم درحال بررسی چندین سایت جدید برای ساخت نیروگاه‌های هسته‌ای با ظرفیت بالا و پایین در ایران است.
🔹
از ۳ سال پیش عملیات ساخت واحد ۲ و ۳ نیروگاه اتمی در بوشهر وارد مرحلۀ اجرایی شده است.
🔹
ایران در «برنامۀ هفتم توسعه» ساخت ۳ هزار مگاوات نیروگاه اتمی را هدف کرده و قصد دارد ظرفیت تولید برق اتمی خود را ۳ برابر کند. رقمی که ناترازی برق ایران در صنعت را صفر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465307" target="_blank">📅 17:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ماجرای انفجارهای پیاپی در مرز ایران و آذربایجان چه بود؟
🔹
فرماندار خداآفرین: صدای انفجارهای پیاپی در نوار مرزی، ناشی از عملیات مین‌روبی نیروهای جمهوری آذربایجان در خاک این کشور بوده است.
🔹
این عملیات در نزدیکی مرز انجام شده و به‌همین‌دلیل صدای انفجارها در برخی مناطق مسکونی خداآفرین شنیده شده است.
🔹
هیچ خطری متوجه اراضی ایران و مرزنشینان نیست و وضعیت مرزها عادی و تحت رصد نیروهای امنیتی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465306" target="_blank">📅 17:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd93667ac.mp4?token=eHi_fQAEjj8lu4tMFN3BLNNA6mNbFqChTI9d1g8L2yRL7eUkzxspX1e5_NTLhZFgvMfHwC7zNXZM3wVVQ2Jo766BAzUwBAsXTaN094p0SUeQ0kOa_6VKqK-l3ofIkBN4eIZWKlOclwBK0kxcngOfZPD1ITdgAGBI3Slsr4Czp13tKy7oHqS8z6CFlqyiEGnCR4vtogXdoPbJgpEtmYkAK28P62KctowixF9GVPTN1fL3-2X41C3Py-kmuHyjVQz8NnwRZLutofvr2r9UeOBg4X530WoEBRRCKYlPw_pEiD0DzwaNhFKlxZyhnhRUHbxoy_NZtsgKZQ6aJJgIReupgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd93667ac.mp4?token=eHi_fQAEjj8lu4tMFN3BLNNA6mNbFqChTI9d1g8L2yRL7eUkzxspX1e5_NTLhZFgvMfHwC7zNXZM3wVVQ2Jo766BAzUwBAsXTaN094p0SUeQ0kOa_6VKqK-l3ofIkBN4eIZWKlOclwBK0kxcngOfZPD1ITdgAGBI3Slsr4Czp13tKy7oHqS8z6CFlqyiEGnCR4vtogXdoPbJgpEtmYkAK28P62KctowixF9GVPTN1fL3-2X41C3Py-kmuHyjVQz8NnwRZLutofvr2r9UeOBg4X530WoEBRRCKYlPw_pEiD0DzwaNhFKlxZyhnhRUHbxoy_NZtsgKZQ6aJJgIReupgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسکو سقوط بمب‌افکن روسی را تأیید کرد
🔹
وزارت دفاع روسیه با انتشار بیانیه‌ای اعلام کرد: در ۲۹ سپتامبر، یک فروند هواپیمای تو-۹۵ در جریان یک پرواز آموزشی در منطقه آمور سقوط کرد.
🔸
این هواپیما در منطقه‌ای خالی از سکنه سقوط کرد. بر اساس داده‌های اولیه، ۶ نفر از خدمه جان باختند و یک نفر مجروح و به یک مرکز درمانی منتقل شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465305" target="_blank">📅 17:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📽
از زمین خاکی تا تیم ملی
روایتی از استعدادهای فوتبالی کشور که از محلات کم‌برخوردار انتخاب شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465304" target="_blank">📅 17:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d60pqWksPQM-CKqAECosAIWX7BaJzZ6VDse9THmrLab51wvMO2Zf1azXoQGr_-fihqIpI2vf2vzLkKEvJjdHSM6UaKiXrm9Uh46B1T-JSl8YQ9C1jBbx_ohKSdvOdZQeA2cLO8X5mh9QbP-6oBBwYmunRhbX9Bfl6TuyfNbU2zaxNFu5DFuPIwOqN8e7RZMprl8LDN2TO7xNL5QQ4Qx5WZt0RAJbuOfawUoYM9VlgUPnoGizLzMI9mePn3cFLVq8sHmDWrXfWRvDiJjRvSj2pDb5RPyEokg1kRKSGu4IKKGiwfCWPxzOwI7RCLnqxIywxYfXpu_OFI4RRzlCOt7kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZ7fhR_FpD7gqMQmnwzvIZY2JfSuHPtfjrhHSSVefzWU-5-M9QycYHUQO3OMrpJNdOeeIj2mNZKmkZV_rjmh5F7lHfqOV9SV2hj-XVk1Xfi19TuiBk3yq8yID75Hrno1YX72zIYK1m6WI4us2buLc-CJgnKxYqlTL9D0K-oc8Do86T62JA1jWGYj6tYErcIb4ea9CPWz97kzFn7yVRsXIXLu3-1wJlU9mZsagIkKL6UAcBrlU_XYdyFYFCEC0OXBWO5nRwEE-na4tZG5SsBxA2kbfr-Djy2hB7W2155UCmE8Td5fVsZ6ROp55BNOqiuOmvEvK_mMwW_nNT8O_1NODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osX8Kn2br1D8J9EtbMCPez4LZ-X-6HSp6bc03G1FztajJeBCI59bb397-OXK7WsGevqN7CA0urJ-La--dLTO_Lp0PVsmNB-qK8W6d16xA5OAfnx03xqmpH4gDTp20p4noToy--zF7BOn45HNEW049tSvmtzFSO5_wyD-x4-03dyFk1o5C51c8_VpgcVAZh3AyGhMIIG0neq7I1c-xBuZmkkQS-Z6U1biILNHNofQ1mmH0jaVQF3cxTaSnTRP4r9PjtdmZKNDlJs2ll_B-fHUV5-Wo_n4Yfm_9a-IWSxu5_NKt42WDfrcRFssfqDeFykgzKmE22Mr7GFgA0CzKxlq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez6Bcs2l9CYuCRtQJV-dtdj5vac-8_2q12Hs2GWpSZ5Jw1bmL7Swz7ZHp5lAcuKVU5OzNToo7aJH1A_Coj6QLv1KOhI6MeJBCrwJ0VFa0jMbxYhaqVrn3QwbQifnrFkAOPCncrbaKnEJgMROVRHgvVFYsVhMxc9kODzX-fch_S8K2pp6pAjnLUZTi_1wO9a8sD2MfcF3EEIRGTqdzO_psmWs9EvVs5hkO7NTsPKmsy7uFuA315TFdOf6-33aI-T3FSKXbF52ioPHCOpldNzsJsvWq3G0V_8wc2GGn93atSoLA5Xzm9zgdQ5DADt7IV8uC1E7dAZeEPEbpuxVT1HrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKzZlxeuRsoeLLvT5BqHhTOIKyJ8MXXk7zMBOpAEFWFtISrpOxRmcD0iIF6C6Jb2Oth7la9AXJYmDnwsz7okQm9_qs7oqvNOR-xkstIpgLp52Hjf5tcALgi33kS8dqL7ReAult4xi1ZfJjHy4asjxSIi9c4zXlWIEpmd95MHMSz1wCN7Cgp89kYGCS5EQdSjoudjmMSEiKLyiNIRADqlQP53eXLqDD8wOtkM11XIZK3xRI4x5zYMRwjh7HJFqdy43aF_nPRmdA9QFw2VqYW78-tiZCOaCkWimC8qY8QZ89QLBLnZnwnCITpSWkuelfBhFoXozUsuQK537F3BC6oG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMIS84i9slxh3lcnTighWI9ue0horLGcKJI3v7rVKyaGdKfHmBhT-uQV0BbLpZu766AfCkG7Zap_Etos5dbFdAJMZd3DyOf-jAVVfudROuzSG1J0Z9AlKzFN-cgEpkJDG7bHwTpszi5QrQkDoY-XlBciSxAlhfoT5Z7P2z14p9_RSr9NUn5scAMfkEHwknbv51vS3KMk_yCGxFng0qOa7V2rkWKX6vg1Kb5aZOii4gk30QoCNEVl6V9JbVP8Z3zPsRzhV7d8smCUGTyZ8XnykWejjjdvw2zV2OhqJROrhs5MC3y9fJAw4pJRzyEk1kH0cOm7FF0UZPGop3t1e-3yWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec_IJwJtynwQai3JV_V-nyFHOSomssiZO7GJ8icxIhXTAdccuXQTPTuTXtVTMR7zrRb1zWApg8vqiReXk00C43s5yHyZxWR-ghFo_eaMeIqz7X90R_RSx0jM4Tgh0kCvjkQ7ZRDw6feBOwFs2O1eJkC38_ozsGzcr3V-yNEfAYuNUhdcGIKZK70Fh3esM5BdEXsRelsUFSvZ4y5dQa3c-CAq2z4CBNQtXzjZb5nB0M-4Gq_giJT2xcdytjM3m_dZHNIWKgoInKs4mIF_Ep0UWS4P-qh58xu9WMMqKYRhlOPML6y1XBbm0r1_-iPXa3T-mVwn9SKFYrOCmrHVN9ODkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZeXJmuVunAtccln2iGtHX1GhpdSNGqIh3uAVD0oDWAbO-tNcqEPYkuDlkoESHgihnhwDoDF2eKwS_yTZClL8zGD5Aj6fFSyW198Q9GK5hEkRprmUtggqNgreUv4m6iQpgT78-XfvhVVcclNsr8p9esTXD9N2EG4wUqMHiH2uuCg5S6bWNw0BSqicTfqLViqE0ozZ69xsmAFuEQF5RVDw6biYzLXMCfWnQI_M0wv83vHCDGJbg8RxQ_tMXJ1kF9kBDooAUP-k9sET0KO_DZWMOWLB9yQvNyHm4r2OJ3t1WPKN4Fc1oIw_Vii6R5AwOZPKscb4bQeGb2oLY0GUptHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W35KC0astzGQN38MNOBC-n5zuzP8KlCQZK1m_m3u_PNU1V1hxpLG-2kNpzQ2af-P_MmM6EB7bN0eDtf94Tn8l4sDzZ2CgljN6CSea_1k-1XYt643e-8n9ZO2efo8FVsl2tC8zoZGUz72e7NSvzvyK8-dkHMKfTHpqwDGliQyY5m96jAfwczQc6BMP5iUjmsBjoc8PGQrih61tuPOSGnTe7ZbW5yUJKSywjkz0CBISLMYuosyoKp_B12zdNzzHHq8kVeYbiDbuFLELM0Ixan66Ec_eQghEdEZsBXAbXyzw7LF5_RPdLzN3YnEOgu5yawV86N5asFwdv2FeyOv5l_0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJoFpHhRWjKFGaKO87kVYxPVdVWoaL-9ewQ2KpviC69V-vTalN6w4rtynfv9montZHugDjsVHFAYyP64anPVwugmcbXL_oGxY8fR7XrBVsJNEaLZogRJOWeImKMLNhrPOq8N7han8oTlwNE-4AomP6e2veaaw82oUMuPDv3MSHEaImXDwG6ZPi_LPmOuv4lu1ivkmR10xI13nIcLYGJPi6mfwL8FJpw8AH2BJfoD-e9rMaRDkIQZrjptKx2aHtc0bYCgsyuPifSAdVkY6TUMV735vLSD9YSnQ_9STo31XobJbw6UqjKIKU9WF356WcrRPvskI0UnspusdPBTVFpKfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در راستای پاسداشت مقام والای شهدای ارامنه
آیین رونمایی از نمایشگاه "شهدای ارامنه
"
🔸️
با مشارکت
بنیاد شهید و امور ایثارگران استان تهران
و با حضور
خانواده‌های معظم شهدای ارامنه و اصحاب رسانه،
نمایشگاه
جانم فدای ایران «شهدای ارامنه»
روز دوشنبه ۶ مهرماه ۱۴۰۵ در ایستگاه
حضرت مریم مقدس سلام الله علیها
رونمایی و اکران شد.
@metro_farhangi
|
ایتا
|
بله
|
اینستاگرام
|
زیلینک
|</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465294" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/465293" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEbRi9Dd23klSqsXwZ9ic0QWN5U1Ln4zQEur61-MOSVooJaCNVyJPRc-aT7xs_IJaCosHHQBg47cVIuIRwM_d98vcVggE9Idm30lg8CNpwITf9iHberhuw7dI9eOSZx0YxAiZb5MZV917r7PwF7ERXHc80JXBV8V36BeTyWcOVbIqs085yQuJM0Z_hDXzjMAJYCboAfJMBp_Zod4AADOu3R8m1SUK-GnXyyHL-Hxw30BIXkGeUN_HV2S-hhClS_SkWGyrvZX1YekvxBUCF1oTHcb7s7Z0bcs8cAGh9y6VglXGykOecuyztYDSQOC_b7sSJkcrsCVVOfuj0MuWXMiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465292" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8YAtsucavSU5aBJOuYC7UEzv4wkzMCpT08UA-CgPHRIBJL6EqDDv-5MthkCI2HO163jKs99FsFuuha8x8lBNLphNcu3zLrQ9De6dMNEeKbYILBBGSjATvqHNpcWLLaKWxRjADWtv4IqR44mFtAM4y8qk97UXahU68Eck6yoqC2lg70DS4_8SHiTMvwBWnAwEBdKWiHn7BowGZvEgMojqSSFqTd4YwlkxinhyzTVpn1t30h7U_tnX_gfaP4YstvsapLESHwlrxMS4B7DccWQhdYvYOitYdFRlLJWUClZsYtslobi-EzxhILBDn68S9NSjvbUMiRH9KNvZyZEW-i9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط توهین‌آمیز آمریکا برای ازسرگیری پروازهای نجف
🔹
وزارت خزانه‌داری آمریکا با صدور مجوز موقت، شروط عجیبی برای ازسرگیری پروازهای نجف اشرف اعلام کرد.
🔹
طبق این مجوز، تنها شرکت‌های هواپیمایی عراق می‌توانند اقدام به جابه‌جایی مسافران کنند و شرکت‌های ایرانی همچنان…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465291" target="_blank">📅 16:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maWJ_rLG-F9Itpn6NICrZiqLmMUIe50Y_SauVruE5rrppKYwLaJYafs8ckMjOAEJj49UE0IWhZdgB8uRHDENhrnixgL2jy-J_KMYKAK2DEQeIQvPnYRcWHjKbr3I43QXlMKv5aCcZ5VtMtLIjj4SlY0EoJ0l3bTOlXF5DGVXxxSEp-phcEd1FoxOQ5720vvfnxDnKJnfgfihvYl7Wi7JDHwUHDabukyZM9iEQnZ-PXUlRCZXKwiuh-_o6PfMPB23WbAyvzWOGEKhHYmOlF8t0AcQLrcZr9rFszB_G1CxMkWyw16nXrTF6w101mlEEKp8VaKRN-kcccgkZxIQvdai6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۴ درجه‌ای دمای تهران از فردا
🔹
هواشناسی تهران: امروز دمای هوا در استان کمی افزایش می‌یابد؛ اما از فردا تا پس‌فردا، به‌طور میانگین کاهش ۲ تا ۴ درجه‌ای دما در استان مورد انتظار است.
🔹
در بخش‌های شمالی استان، به‌ویژه ارتفاعات، رشد ابر، بارش پراکنده و وزش باد شدید موقتی مورد انتظار است.
🔹
از هفتهٔ دوم مهر تا دست‌کم پایان آذر، انتظار افزایش گذر امواج بارشی از استان نسبت به میانگین بلندمدت وجود دارد و به تبع آن افزایش رطوبت و بارش نیز پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/465290" target="_blank">📅 16:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAOt3gFd9DLli2akEt00CFFtQzo4cEmituGTKWuHqdqj4PdXIEUYuQp6I9bhQEFCDLY37DFyP_9tKMix9mbnWDlcb87SKUmtzHvwwMp5JlbOr9Wd_GEYxqBwCH66golNMpBsH2G0TLnVw24dhF8UkP3KBoVhgJsC0fRNebp-vR1DEcKwfitUMefEweVWo_954R7-6uS7JI50XM5VPFRM0Ozxa1Bjzl9yEr_e3PMV8tpL-MgIRjiaoUfrnHBCtFGO86FhsICyoKJmmFhILNJwIuS9NF194GuGwq3mHaAXuqUDLgAWKVxtKl_tbyjk3lJjRc4VdTLbK82WawMMIi8I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twyzaM9Q5seS55eNAbiwLmoXnONK-2oCFxvhfoPRhEW6_uvI2zoHS_notUDo4QQMmNlBFIzsMAOnw_NTHuCcr_SC7EfXJGqFdKWUENgwSrP9X-G2jenOf83IQSr0lZE_Nl4jLitmy7nDfMZpMPhUGJPbpb1_DNmIis5-_iIVtfIgtLIB5N7gFVS2IJqUGgkRVYN47YaYK0nWN4tbL6HS3AH4gH7q2ShpPLzFDK7OisEMT5jWa3sOrIS9mpl1Xn7XTBrg5g5RFY362kdQOCesxvu9tx7Fo6K7FaZwNaiiH9ZRluNGszeWvlu_obyxZAyFqH9R89Zp48K6waaLaYl5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhCN1WbSAV-jFiPAfgJi-hLbMOPYbhyXqE64fSsWSW0jaz8AqZUfsz-GKi8ivpgwYkKyhoF2iads2gPizMc2ffnUkX-6_-kybsaAS9eN6-nolrq-WnZrtgmxosfuc7HzcRFpJ_siO45Xl6JtTHGgKtbMlKumf-b_iGnkRZH0sNGUgj2XfvCyJW42wV0Cu5vRksRSUdXZnp6y9DZk-1xzBdA_biA55CqNCXs797_4PTaigdO63-5XPyYioOneLwgUUwxk6UEqU_Z-12FN7IsockRVpxefiJuM7MbJZRljj1nZltqqp1DF9uzAT27-IEN_fr4sgjTR_n7NGUt9H2Ux5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3d1_bySFiEVUuGIOIFagqtZlO6eNgNQ7BC3WOZbEnbPfaa6hQOvbLIvQELWQ5h0X-B_DSt4K-sYUCmdnBI-m8IXPZeBgxzfPt4dz4TopcK1-rFIYph78Bh4WDRKE9eTfYGwdLN-a3YwjjPEXlKatjkZzmX2GOURwQqReFbymMjyw_m8EoAp57IqeJmni21_qqXyJu-pakLOfVy8ZBLlOZLGvbGgqcP9c0B8fvgYnUtTUD3jSpfDsO5rY0YrW1DFHtIR1tiJk-o5e1qwF1ODUJpZz3o8UGpvWPVFGsug2cARIG52cTDyqADCW6TYC1VegOOWPCM-yOf-Rqi9aW9gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eImyUYZ_TFFQvGY5h7kGkiTvyZ4NFrMGX7kaVv-eZFhHJL4o68mhpUAvxenDGk2Oox6NVNs2J_u4PWMByapYvHAG3wPJfXTnxeduX1QiDbHUUfRptEn8C--N_pFInJNjgcs0ekD0FrN-zLg1TlQhgBplGtuDJac9hHjyR-dIJS11soJJrdrsyEYT-rgWizGSOhvASW_CNxNxeFSCLM3arVQr5tM03ywGV2Gy6LQvFcb82FM64R0ILjvWRUhVG_CJBHz4VCcvr6AD63BgH7cAT9FIB4M7Y-j-Mnk3Y5qAj2XhOf6WVAh8T_SlSwzv43OocfMaLUtTz3yzcJWiKonLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzPwHHTL0A9-8QnpL2_jTWDriAeAC64JMW8o2cCiMWiebYVxBnv5JPGswXkGDHDao6GXs76hNQ1LmX7WOjYczmeQCWjvauhGlc19fAINz3IBCnc2-T5qNCOnKj6bN7fNuRzLilTdhakxjUlwH4ddwTVu11zx4uSopDE6gCz2lGrIMsvadu2FMU589EwKRrAAJmXHnz4h27LRUyEWRxe_UJiSrBcaPZBn3HexZUuTzZSf6kCsx2sWqth12R1KTy282XaooiqsGCXCO8OLRv8-AaVOzXeiePIfawHwQOUHtPIG_d0jejUbmyYmDKch0odyZGNlEKQz7NSqHkypZllouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4QHwXYV7MaM8l7T5isKyL6x2UjbIb1viyXIsl3evWgm46DOjZcgHucUYJbjngGgISZldaXnzXbGr0qNdKTdAvkKNUs7wliFvGtIfeKq725CslNmf2SJoDMUSgMnt7GfFWFUghIZeiCvejxQjFRK3GgetxpWhv5bui4NKNokyEpe9wPadyUM6cTo2XQO3Y8PwVN1i35AHpZwHPwTUIsiWm1FgeAuICntqLm1bNP7fN-5KsNccQBFeKy9o6YZgIpMjYHLc71nV4u5JNAXKrmJvEHtMtKTZl_O2IPwMYQfpzNkas_dc8HvLLQ6elWqitBK7dQZq9hqX0sU_27fJpTcsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردانی که به دل آتش می‌زنند
🔹
هفتم مهر ماه روز جهانی ایمنی و آتش نشانی است.
عکس:
غلامرضا شمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/465283" target="_blank">📅 16:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOfxtUDTsrTBDcd3BaEVRs4jDK6pDOkdplpEJ8Bcs26lOn5pyCg68SQirxGKZQ1HLITpUGOw9Ku0ala3tU6AjcRI_HINYfqlsGbPMsf8Hw4WuFIEiCHtYK_RG9hLYkSzhdb_hqjhsPZuTxxDRgJ52XTg7z1QTta82X1xQt-1Dw0en_8j87Ft7d1yvHl9DNwRJdh9etgI90NaugTA_5WDBAxD_1Yhp9UFIysOrW86jfWFFLJW-CILYZ9HXOzNs11Gff82RAQUc5ZNytNo2QPjqRU25oFj52oY8IDEiwY2ZESk20_F8KeUg_eeyF5dPOL0IFTxE9QZlmXFWzRQvJAkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اصلاح‌طلبان به نقاط قوت ایران
🔹
ایران در شرایط کنونی از مؤلفه‌های مختلف قدرت برخوردار است که در کنار یکدیگر، این کشور را به بازیگری مؤثر در عرصه منطقه‌ای و بین‌المللی تبدیل کرده‌اند؛ مؤلفه‌هایی که مجموعه آنها می‌تواند جایگاه ایران را در معادلات جهانی…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/465282" target="_blank">📅 16:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5065b7d248.mp4?token=n9Fb124YPzoY03Es7Ipxr0vJ2mMWVs-7B5be5CT3z9Eyn_TN9o3xoENoi_v1ku26egsPggHPkBsNrCzBhwmKPBcWQ_ljWzWdk-h0FTtqumAZd9EU31adE3M67H2f8hyrfOi_bKYbxzcT0zAK80O0mKYarqmHvF27xtMy3lm7HZI4Q4K6R0eb6QfaXrX7_-ef_xCzSJDtpbNDCE1EycwKGuowa6VvLJ48Sa26UOFPtVGOGrgpliN05ArDuvw6MRhscXL39vu36Nwxfx9w8OhDSvvLarRkm_JCUBypLa3_Cfdjw-QyLBrUaGzvhG6wR5Bjd3hQ7pwEa2U1-ztbbb0S2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5065b7d248.mp4?token=n9Fb124YPzoY03Es7Ipxr0vJ2mMWVs-7B5be5CT3z9Eyn_TN9o3xoENoi_v1ku26egsPggHPkBsNrCzBhwmKPBcWQ_ljWzWdk-h0FTtqumAZd9EU31adE3M67H2f8hyrfOi_bKYbxzcT0zAK80O0mKYarqmHvF27xtMy3lm7HZI4Q4K6R0eb6QfaXrX7_-ef_xCzSJDtpbNDCE1EycwKGuowa6VvLJ48Sa26UOFPtVGOGrgpliN05ArDuvw6MRhscXL39vu36Nwxfx9w8OhDSvvLarRkm_JCUBypLa3_Cfdjw-QyLBrUaGzvhG6wR5Bjd3hQ7pwEa2U1-ztbbb0S2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طلای دهم شیرین‌ترین طلا شد
🔹
علی داوودی نمایندهٔ ایران در دستهٔ ۱۱۰+ کیلوگرم وزنه‌برداری مردان، با مهار وزنهٔ ۲۰۶ کیلوگرمی در یک ضرب و ۲۶۰ کیلوگرمی در ۲ ضرب با ۴۶۶ کیلوگرم به‌مدال طلا دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465280" target="_blank">📅 15:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTen2bEL9zOpYVrg2a5NOP9cJlY4FTSn9SznwNYNTK_HBDUJw4c9sl0820MtlbjBi3Jv4YYjYax8pH1qg-wiyVXhKR8ZSfjtWqDooP5QBUK-2mHQRVhCr4ab2Be-svst2iLEx2pT29G7FnT8EXIYQxavpzxVQp6R4AkwHhVK9sLJ1Z3TRTnkRPi9lVyiC7lPa2YpZhvxzn8adexetszh3LfA79ZsQerQSEvjNr-gatkIJBR01zlthqCx-8sINqkjGK8Ntrm0F6KCiNExR48XKlIlu0K3rGafdKREj-pd1RMuJYnkxkKupskVpRbeIcvQndshEX3juZAtO404vlVqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی انگلیس هم اعلام کرد که دیروز در تنگهٔ هرمز یک کشتی با اصابت پرتابهٔ نامشخص دچار آتش‌سوزی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465278" target="_blank">📅 15:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB2IK1bIpp0OQM_dHnL8wUcKIEdJJfG4AjO9kzVYuE4T_bCdCbfSJ1ft_ux7DD6ltgmKq_2l-s0szQ5Ele9ISSt8-UowgswOEy4mP8C1ZIjuHz6X0ZByK_dAmMrDmeoQCl2raeRdK1EjDCUy4vPr5Ns4rJMFhpYSSt5Aa1hrzxkiudomI9uYRfJ0Ex9Wbaxv0GQvWRHkGYUxAsgpl4qSxlUThC_XBrHFe3gEo83ts2ka1efPdQv4p0NxXlGNGjLcnYXKifendZDOlglIbBTg4ClNeuTvr-xw0wWJCvhbA6CufnxJELCeQ8xO60nG9i_SJa__8HINsX7BaYY1WnkgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید بنزین سوپر مشخص شد
🔹
در معاملات امروز بورس انرژی، هر لیتر بنزین ویژه(سوپر) وارداتی با قیمت ۱۱۱ هزار تومان کشف قیمت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/465277" target="_blank">📅 15:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678142e59c.mp4?token=KT6L0j37CcHNqCY-r-EGE50SP0OMwH8zomM6utNYFqZxpsmKXXYxDgmC-h4R5oHBx3L122LqS_kN-cP-anGd6ADieKaM-EFb-WMeX8UyjloIfXKdAWYvbtejZUW7HFyV-gD9TlyNXYb9KmcWg9V4RMswrc6EH82Vlwc31DI8k2-luFtXxqyrtSWLlAZ7TBY5gvWXbacPt0AFAhltMN7Mhl3eKef_rppwWG2d8IdDFK9KaYoYuP-E3zajsEvOb3SfA-C2teMNAI7TaeM48RnmCZlpuIb479oJw7gO7RG8YOEBeLmuSfoPyon-TiuKKYXMV5GA6Z5bKHaZBGn2NdwFLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678142e59c.mp4?token=KT6L0j37CcHNqCY-r-EGE50SP0OMwH8zomM6utNYFqZxpsmKXXYxDgmC-h4R5oHBx3L122LqS_kN-cP-anGd6ADieKaM-EFb-WMeX8UyjloIfXKdAWYvbtejZUW7HFyV-gD9TlyNXYb9KmcWg9V4RMswrc6EH82Vlwc31DI8k2-luFtXxqyrtSWLlAZ7TBY5gvWXbacPt0AFAhltMN7Mhl3eKef_rppwWG2d8IdDFK9KaYoYuP-E3zajsEvOb3SfA-C2teMNAI7TaeM48RnmCZlpuIb479oJw7gO7RG8YOEBeLmuSfoPyon-TiuKKYXMV5GA6Z5bKHaZBGn2NdwFLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترس سربازان آمریکایی‌ از تلویزیون ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/465276" target="_blank">📅 15:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853b0a4d36.mp4?token=Fza9apmj6i4ivCRDKAtWNesn6AKm07p8ArW5_lHGIR4OHIQQWoKfjOoR8UTnpgvEUNpSE8QAScyUl4Op6o-MDzaMqELTazAKfEzGmtRGvEJyjL1nIsPtIxUHNYSUS90bqm2ywvQkzbDuEYnMKI55jaZNxKJbx6Xu7UOHRFuXelwpItIwHYqFameaZZRiaVRYpWTA0J9ewOPPOQAhiNYDnXjjLknzUIFQIYuuXnlvVioleaDb6ZWqo62f3zpmgWDM0p1-8_g8TXlgxTLXS90meq_-Gfir3z_G5eEZQabooEqv9WDkjqElA3IaXw0-hkXbVLLsFdu1m6Nzk033gzVRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853b0a4d36.mp4?token=Fza9apmj6i4ivCRDKAtWNesn6AKm07p8ArW5_lHGIR4OHIQQWoKfjOoR8UTnpgvEUNpSE8QAScyUl4Op6o-MDzaMqELTazAKfEzGmtRGvEJyjL1nIsPtIxUHNYSUS90bqm2ywvQkzbDuEYnMKI55jaZNxKJbx6Xu7UOHRFuXelwpItIwHYqFameaZZRiaVRYpWTA0J9ewOPPOQAhiNYDnXjjLknzUIFQIYuuXnlvVioleaDb6ZWqo62f3zpmgWDM0p1-8_g8TXlgxTLXS90meq_-Gfir3z_G5eEZQabooEqv9WDkjqElA3IaXw0-hkXbVLLsFdu1m6Nzk033gzVRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین استقبال از ورزشکاران اعزامی به بازی‌های ناگویا در زنجان برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/465275" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465274">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facc0d5c41.mp4?token=j7t6m835y4vBg-GfQwEhTeHUMnKPPLmVd-5L8SLw9ZDVrW1cOTj1LD0HRVQnbLIBbpMMU36MfiMzPbqZZFCYt7Nmfq6MdoOvA9wpzZha9-bhVBxAWPd_IJeDlWL68etSkbiKrwCsd6ZcSI2oO-M2YkN530lUatOaqMpnw5EiObKsvpO210nq1fUmT33SjrG3CNPOGPC9083XHPoqlYdHX-V6ASDI09nqdbGBK3xGS-UnvUhabcTv9j8thwhPW3kE_Z_XtmaxNz0a0ZdN1veoPJU1nmcoNYdOx-VlWA40yOBHIP0BX0qXc5v67n7_WINlVgPW04J6ShGnJu2_BECFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facc0d5c41.mp4?token=j7t6m835y4vBg-GfQwEhTeHUMnKPPLmVd-5L8SLw9ZDVrW1cOTj1LD0HRVQnbLIBbpMMU36MfiMzPbqZZFCYt7Nmfq6MdoOvA9wpzZha9-bhVBxAWPd_IJeDlWL68etSkbiKrwCsd6ZcSI2oO-M2YkN530lUatOaqMpnw5EiObKsvpO210nq1fUmT33SjrG3CNPOGPC9083XHPoqlYdHX-V6ASDI09nqdbGBK3xGS-UnvUhabcTv9j8thwhPW3kE_Z_XtmaxNz0a0ZdN1veoPJU1nmcoNYdOx-VlWA40yOBHIP0BX0qXc5v67n7_WINlVgPW04J6ShGnJu2_BECFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رادیوداروی ایرانی برای تشخیص انواع سرطان‌ها تولید شد
🔹
این رادیودارو که با دقت ۹۵ درصدی، سلول سرطانی را تشخیص می‌دهد، تا پایان سال به مراکز پزشکی هسته‌ای توزیع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465274" target="_blank">📅 15:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c03dde89d.mp4?token=svdHWgDVlnl7xS_hHLluxL99ZKSZ-ISKaWEtRcR0iPTJrWpsuXuL0C4fHPdU0i8Ml4deXmKCTzys0Y6MuvQxXLH52948AP0kK3rKcXcwbQpt5okLeS5DdmUIohKD47xyqqZi5XrLAJKlaDfoomjROW25_0YgO3xiu7bPDZP5yj8ZjmBmRwJtYVv0zcapYngDKjeGMghDUqUi_AUrX5_m1oB8hgKKx7QStbO4lyF5--VKNNVUJZcwx1NGP2uacvRqDn9S_UHHEtvCbtWxdgrWEvSTU62eK5A0ndyr5IJA9pJstetFmJ6IH5BBhpvMnqnbIR7elQ13nioLL0AOlagJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c03dde89d.mp4?token=svdHWgDVlnl7xS_hHLluxL99ZKSZ-ISKaWEtRcR0iPTJrWpsuXuL0C4fHPdU0i8Ml4deXmKCTzys0Y6MuvQxXLH52948AP0kK3rKcXcwbQpt5okLeS5DdmUIohKD47xyqqZi5XrLAJKlaDfoomjROW25_0YgO3xiu7bPDZP5yj8ZjmBmRwJtYVv0zcapYngDKjeGMghDUqUi_AUrX5_m1oB8hgKKx7QStbO4lyF5--VKNNVUJZcwx1NGP2uacvRqDn9S_UHHEtvCbtWxdgrWEvSTU62eK5A0ndyr5IJA9pJstetFmJ6IH5BBhpvMnqnbIR7elQ13nioLL0AOlagJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هیچ تغییری در مواضع ما رخ نداده است
🔹
درحال‌حاضر موضوع ما فقط تنگهٔ هرمز است؛ بازشدن آن هم منوط به شرایطی است که به طرف مقابل اعلام کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465272" target="_blank">📅 15:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
تصاویر واقعی از عملیات‌های عجیب‌وغریب آتش‌نشانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/465271" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5oqXuT8IAmh8gDQwAeXYhRuw-Vuj_YhTrBGh6HYLltdBablR6G7pxlUzoWwV5CY9tP1pviV4Z81-fBRM6_WtTzRy9biASiX6TAb60oWfNm0iIJMHh3Xv6sUCVzFqMBAyvaTHxCS7IWmcJvuvOCa4pCPcLVQh0tz-BvkNgmGzN-Xkgshfzoo-WI7900jZ6bWZBJH6a3BS_LGf0tofa88vw0zBqnuQKTkyuhbsyu2Tzjnj99N2IiVhDORLALQ4dx8KLdYwQlBxMtQBlotcTjtI2ldA0J59tINjGZpDM327Ypem_GMUo5NjmmqT29IagoSyaDXXjZu0Zv0kGMP4rw9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط توهین‌آمیز آمریکا برای ازسرگیری پروازهای نجف
🔹
وزارت خزانه‌داری آمریکا با صدور مجوز موقت، شروط عجیبی برای ازسرگیری پروازهای نجف اشرف اعلام کرد.
🔹
طبق این مجوز، تنها شرکت‌های هواپیمایی عراق می‌توانند اقدام به جابه‌جایی مسافران کنند و شرکت‌های ایرانی همچنان حق ورود به آسمان عراق را نخواهند داشت.
🔹
بر اساس اطلاعیه وزارت خزانه‌داری آمریکا، این مجوز تا ۲۸ اکتبر ۲۰۲۶ اعتبار دارد و آمریکا حق لغو یا اصلاح آن را در هر زمان برای خود محفوظ دانسته است.
🔹
وزارت خزانه‌داری آمریکا انتقال مقادیر عمده پول نقد، محموله‌های مربوط به دستگاه‌های اطلاعاتی، نظامی و انتظامی ایران و همچنین انتقال افراد تحت تحریم را ممنوع کرده است. یعنی طبق این مجوز، مقامات و شخصیت‌های ایرانی که تحت تحریم آمریکا قرار دارند حق سفر هوایی برای زیارت عتبات را نخواهند داشت.
🔹
همچنین عراق باید مانع ورود یا عبور پروازهای ایرانی از حریم هوایی خود، خارج از موارد مجاز، شود، در غیر این صورت، مجوز صادر شده لغو یا اصلاح می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/465270" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a988378ca.mp4?token=lby_bDGxdAOpUsh4_K2RxXYEuaqQlTOSTchPSlbMoNxGbaX2s_R9cyU6lMdSVlcbcvNQM5iOspUzgg3nqq2rsPx06zDrsQJFWej1d4838m_ckSXIdf43IjmH9JpdgKN95-ZV2pIbreDyE6MkbyC3Q7MkoMYXUwBKsqwwfRk8ANvLXKaKLOyr2gOu7YzVd8Gbn4TYuufFIe9bYI4r98cNiL9mhUftP48RXtjBvurZGJbG8JMpeHvWK_oDo1RTbyx8Lmm4JSImheDli-SNBykJpgY_AjyyX0QudGTKp-fTMmPmk-O1dyM4Q0TXM9t2X7qwkIwSSgpSFV3ai9t5pTUK2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a988378ca.mp4?token=lby_bDGxdAOpUsh4_K2RxXYEuaqQlTOSTchPSlbMoNxGbaX2s_R9cyU6lMdSVlcbcvNQM5iOspUzgg3nqq2rsPx06zDrsQJFWej1d4838m_ckSXIdf43IjmH9JpdgKN95-ZV2pIbreDyE6MkbyC3Q7MkoMYXUwBKsqwwfRk8ANvLXKaKLOyr2gOu7YzVd8Gbn4TYuufFIe9bYI4r98cNiL9mhUftP48RXtjBvurZGJbG8JMpeHvWK_oDo1RTbyx8Lmm4JSImheDli-SNBykJpgY_AjyyX0QudGTKp-fTMmPmk-O1dyM4Q0TXM9t2X7qwkIwSSgpSFV3ai9t5pTUK2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هیچ تغییری در مواضع ما رخ نداده است
🔹
درحال‌حاضر موضوع ما فقط تنگهٔ هرمز است؛ بازشدن آن هم منوط به شرایطی است که به طرف مقابل اعلام کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/465269" target="_blank">📅 14:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a31b4653.mp4?token=e7L6cDsp9KS3ln0GBmicRPryys5yfjL_uwZBepi591AlCU8n6s_Cs1N5MMjBUYQsOSwBPGBIEne288pjeyCro5zBBaNISsPukc-I2YOk2SOb-m7YE51nJqFjJfFZ9XVvr6jEXEcIBN-UumAT4z2kFm2gpZMifBsz6BBVJJ9Wdi_1TXlVl1C5SbZk8q3_VrobdAaAxOIY38xkNAsvUf8YwwVjNCFv5j5rP0GoDY38DZLNiElaAO23SpMn72oHc2ElJy1vNCK2zlL8yqv9qeVp4VtKj_Ljd-YM5EJs-D1hoXc_1UItsAMiDLreO8tCTRMjzEBI16E2qNxizONiqYgsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a31b4653.mp4?token=e7L6cDsp9KS3ln0GBmicRPryys5yfjL_uwZBepi591AlCU8n6s_Cs1N5MMjBUYQsOSwBPGBIEne288pjeyCro5zBBaNISsPukc-I2YOk2SOb-m7YE51nJqFjJfFZ9XVvr6jEXEcIBN-UumAT4z2kFm2gpZMifBsz6BBVJJ9Wdi_1TXlVl1C5SbZk8q3_VrobdAaAxOIY38xkNAsvUf8YwwVjNCFv5j5rP0GoDY38DZLNiElaAO23SpMn72oHc2ElJy1vNCK2zlL8yqv9qeVp4VtKj_Ljd-YM5EJs-D1hoXc_1UItsAMiDLreO8tCTRMjzEBI16E2qNxizONiqYgsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلاس درسی که در محل جنایت آمریکا برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/465268" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707df41be6.mp4?token=eJEmpJxbiQMW82nbW82PvqmEoS25c20WUJkHD02UBaxD4WFolPlhIXNycIBZ1f7WCTtEyCmniMfXBlqqqR0pCNfJEIKSMbE3VtN5Te3IGy8_xdCfCZf4D714885BOB_WpVxnfgcYznmjy_sfQJnMBlqL3V7V2X9OVANeCNBpuIYcUIXstOrdC-7eqR0FAK20PYxjA-b_GcPO5d5pmeRPojBQb0Zq5rqlNB-ZL7-Hp1DoBRLyf5m9TRETCkB16KBIVoQmwc8lp-jB94UcBjoCdWspT_sw4G-SxfJ6Tew0lsN0CDf40PNsbwUHwttqbXhBUIqAhhs5L0s5E6pNcKw2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707df41be6.mp4?token=eJEmpJxbiQMW82nbW82PvqmEoS25c20WUJkHD02UBaxD4WFolPlhIXNycIBZ1f7WCTtEyCmniMfXBlqqqR0pCNfJEIKSMbE3VtN5Te3IGy8_xdCfCZf4D714885BOB_WpVxnfgcYznmjy_sfQJnMBlqL3V7V2X9OVANeCNBpuIYcUIXstOrdC-7eqR0FAK20PYxjA-b_GcPO5d5pmeRPojBQb0Zq5rqlNB-ZL7-Hp1DoBRLyf5m9TRETCkB16KBIVoQmwc8lp-jB94UcBjoCdWspT_sw4G-SxfJ6Tew0lsN0CDf40PNsbwUHwttqbXhBUIqAhhs5L0s5E6pNcKw2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نامهٔ سپاه به مردم آمریکا منتشر شد
🔹
سپاه پاسداران در نامه‌ای به مردم آمریکا نوشت: حساب خودتان را از اشغالگران فلسطین که خواه-ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
🔹
در این نامه…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/465267" target="_blank">📅 14:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90885e52ae.mp4?token=o5BHGfDdF7piCn_1zeOz6INy-3V2su9MHqx0asJNzRInje4_2mzNBrvbWsScSiXR2nsXGmuNmIMs1BFKTKNxLWBkFT7S-7raZbqcreCKOnBDjQmjs0YDj2xEUbpb5mfsG_Na6nNhLLE5fn3OMTgk9Bye-aXPCNPA9ioDAAsNSKYWJQUbcTo8cKMe9OQ7wYVyDRWMuci2TvOfX-1xKoX5vctWKYqwNPQMXNrCB50BqA-4jIAvovMEUVSYurAD9wBni2dSA-yOyJp0YKbgQ71Ndj0h0wRzBufbF_uuYRu402ulKHY3sUzJSFifh5el3bvwturqU4y316C5S2tRW09c1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90885e52ae.mp4?token=o5BHGfDdF7piCn_1zeOz6INy-3V2su9MHqx0asJNzRInje4_2mzNBrvbWsScSiXR2nsXGmuNmIMs1BFKTKNxLWBkFT7S-7raZbqcreCKOnBDjQmjs0YDj2xEUbpb5mfsG_Na6nNhLLE5fn3OMTgk9Bye-aXPCNPA9ioDAAsNSKYWJQUbcTo8cKMe9OQ7wYVyDRWMuci2TvOfX-1xKoX5vctWKYqwNPQMXNrCB50BqA-4jIAvovMEUVSYurAD9wBni2dSA-yOyJp0YKbgQ71Ndj0h0wRzBufbF_uuYRu402ulKHY3sUzJSFifh5el3bvwturqU4y316C5S2tRW09c1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: زود است که دریای عرب هم خود را از حضور دشمن خالی کند
🔹
آن روزها (روزهای سلطه‌گری استعمارگران بر ایران) ۲ دریای جنوب ایران، جولان‌گاه نیروهای دشمن بود؛ ولی این روزها آنان به‌خاطر ضربات دردآوری که از رزمندگان دلاور و محافظان تنگهٔ هرمز خورده‌اند،…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/465266" target="_blank">📅 14:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twaA3m44zwILkpvZrHCVMYu6d71XzqdcxXRmRM_kcPm0dD27vo2O_eTh_VRgufvCjRP9h7llLvneUqq4xc7coX7Svz4zCm52iPHJq8AKzLSJCZkvV04oquCKYAMQlQIixKqCSZ_6j32RQN-oUMdUyigkO4fRL5znF0BRuOSd3bSAQS6nNRlzBwBlum6zmqKQObascvq1iKggJA54QyLgffDAz9Q183e6HTKCwHp4AtVNPDU1UGUXqfnhkbBdB7vlEcKofOWComN8xP54K2qJiyjOsDQx8lYZnUS7eetMORZwTn6nKPIgdZMSagwwk4_TiMWQ7o0G8BQ13m3o8qfBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDHBrzb70hahhpKlEaglChA-uvhvWv8HPFiZwkrJfuBMlvotFdFhPCF6ZsQeiPhcWBLHrHq4LFCMPE1ZW8Bofg9UyqBrhA7Ao7UjGHsnIIAuE4DNyq8GM3JMGL5Emqscu47qo6LUktYB3p4jhrkLXwC2MHARdp5qOfwADwnkUFOg4uU7QIDsB7LARXnUg20gcQGmTem940yXdjfvFvHQPFlboTO1lSuFB6DUuVyS5R7XWIP_vimPF5SJsLKKsNaJA43cT2qavAUl91g_xE517-EkvcCuk9WC1Svk0-nIE_KMHsQ69rYxbhZzff9UxyGZ5M4pX17PX1VKjqNgCTyaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpgHsVhoACl6teQy4iFQtOi3F6ZHJEYbRsQerHPZ8IYmvWVKZEFTruxDFgzvjxWXcebfrRIqnaEdWX94ee4Iy5r1X12RJ48VqaV9Fc3QHnJE0DVYDnXIpo5Oln4jGIs7uibW-GOcDkSHqOYJJfwO61IMGOEWfQlGqX3N3Fj8IUjit3NTPrrlWWQSGeT_LPIVeKdAUzE3a8ucbRlyQh3uJepFengi6tzmopccV_4rQl5WWt3T-2zqvJD5nRGj8sVFu9mcxlspVwHH-VL2TqHCSTTMA5_OdwN5b3Lvx8E4fS9Yk5gfauWVvm06j7E2YpHhy17Kg1bMxJTw_TPPLTSj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1YWnP1_OG2eI8Q0AxaZDdgwEcgTRpFUiOT7YGc0FvzwtDv4OG3RCoM_4mFF6FJH9oawnR83oHAyWO_uj3Id3HBNfVihwCWVKHCh_8T_X1JUgULGMMLR19LNIr0isljsV-4GEdKvuj5MG-iwtnHp1HwL4uphUpkOneHmvvWREuEGSyBYn3tCai35OXx0E8LaLdzgo_VXyGLKs8LkJscWKSxspQja3VK2Gu06mA7nPJudPik4EvWaYjx_mrnaj1pqLDI80izY-JrUoJaxWRqXbf4cq5C8AFiLU3slGHYYSFR7QiozPBu5CquYYFBSJPrlmqpDa11E1ohL_VzGWW7BjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaD5C55RUiwS31XVXJNb9lsHku7a2WZhuox-0A34qW9WBH5bd7HfabLpO_OYAJwW5SsSphFdNRSrHpsk9CUSOU09urZnEhMId2JiIAw2U-BEdvUpH2uGw5-woK9_IKCMM6eTid--m0XC69vtPx9daRirzlMsOfB9__T3jufZdbzzg1MkIYvsUnGdLTPyiPlWW-Ar3hpvtiQlCafLU2p7hG6p0nwQHcgDPUSqyYBiVM57Qi9_9O1SiVF4PIDyOd9DIXOZvZdc_SWSPe3TljTuLX9c6a_qxORIn-r3W0cTw91gBd3XO31BWC8YoLpJeS3qEB0O3OxN-96cUHQrF4TfNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست رئیس‌جمهور با شهرداران کلان‌شهرها و مراکز استان‌ها
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/465261" target="_blank">📅 14:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuNlYdkNgk27jaVtzxWZ9lgg4caoFkcOUcUzYQbcx7WPEuVqPE3ZCIfMXyzr8OZo2Az0mkZT2VrYEiOUwYy8AHgSnRZoMQe-v0nvJ6KGmorcXwEgJvjjCn-5CU5BHcHB68WIjB2C2lFSTNsq6HWxQlJq3f07OGlbz6hirVloRBT1hm5bgl85G1OI5kiXfELg0kMdi17rNbP5xHNShU8ffc6CYjdkQCgO3rSYvk4ZlwIYMcLBVaMtzhyUgfUyLOn_NlPWfknRnGaKu-bvTX027elVblRVFAq87cGc7u58aVGldqtJsZ-rmoi6C-cpI8kHJZlpaKBmMpfhnW65sOLwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚢
استقبال صادرکننده‌های کالا و خدمات از بسته اعتباری سکو/ اعطای تسهیلات برمبنای عملکرد صادراتی در بانک صادرات ایران
💵
بانک صادرات ایران در قالب بسته اعتباری «سکو» به فعالان اقتصادی برمبنای عملکرد صادراتی‌شان تسهیلات پرداخت می‌کند؛ در چارچوب این محصول جدید، بدون نیاز به شرط معدل حساب، امکان دریافت اعتبار در هر ماه فراهم شده است.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بسته_اعتباری_سکو
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465260" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M60RGcFc-WUYLh73QuJz3BD86bf0U8nyKukEJ0tYZu2SaOx-gWbMubD1GV1yTpN_2LJ1nen-wq6mSVf1wAbhBbMhUDoY06gynz1dh6vVQuWfVZWU7jXGwyFSNiExZVKhH7_tuC12q9PCag8XcfcljRp1PtL3Zq4c_UkL24-BmzM9h8sI0rdPadUBpMKNzcLyXuDS6LfoYeH2Emw2OWk0HzNPZ-zoRIv8hZTJ-i5F3u3jmwY2rhILsqc6BBx4ITbaV1swYoQHj8NBf1uLYnUuyob7JQDNk98W2V0HiQVrwRSW3FsJMhTaBf6nAleLvy6zqfNn2iKhtOE-S1oiUCciow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8IMpKID8qBGocwLRf59YWFC8EQLoKA7_CuNPEI0lfMOIfmhA7BGyVt30Cu1IAuuhc3jeu37SeOwJYx3AXX_XlWwvUTQIY4pnxCJ-HfFMnI-uCg0laH6lMAefYJqb_4IV0PKM_CmVjOd5k8doTi_BCxQUWmzOGAtJyzu0I1VC1ExlPLfXMHg9KSqzv2GTtORelyisqcLM33GzDCItt-kmPWd2xg-U66FFASAfuip6WUURuKbfkkaNVBTdpGYPAg5MXATjHNXWdTQLtIKwO1Vko1o96-pAB9TtbHiI2Dos7zHY0dY8TXSN8HNH0fDKM7ZaKlEnPCFPAT0dagLTtCw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
#فروش_مشارکت_در_تولید
محصول شرکت پارس خودرو ویژه متقاضیان طرح‌ عادی، حمایت از خانواده و جوانی جمعیت و جایگزینی خودروهای فرسوده
🚗
خودروی قابل عرضه: پارس‌نوآ با گیربکس دستی
📆
آغاز ثبت‌‌نام: از ساعت ۱۴ روز چهارشنبه ۸ مهرماه
🔹
بر اين اساس متقاضيان محترم می‌توانند با مراجعه به صفحه فروش اینترنتی محصولات گروه سایپا به نشانی اینترنتی
https://saipa.iranecar.com،
نسبت به خرید خودرو تا زمان تکمیل ظرفیت اقدام کنند.
❗️
جهت تسهيل در فرآيند خرید، قبل از شروع زمان ثبت‌نام، در سامانه فروش اينترنتی مذکور نسبت به ثبت و يا به‌روزرسانی اطلاعات شخصی و دريافت كد كاربری و رمز عبور اقدام کنید.
▫️
شرایط کامل بخشنامه را مطالعه کنید
👇🏻</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/465258" target="_blank">📅 14:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/465257" target="_blank">📅 14:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n39kIXgLLbN2H-497bbT341TM_kbd9DxRQisZ2VumSvfEapLNuQQtX2RKeW06HzNiYqrKyNkkMOGCEh534c4kvpPuI23xvBFyVb1jsxuLgnejzmhD6JK1dfP9X-sHBw0Kg4QBgB93rsoxoOr3iddByjEYQJ8K2RZQ7FdUof8h9cGuIvqVzfbqhHoyIFqi3UOjRhDwL4LM7GVOJqODw6HND988hqpbtTTtIK9wb_zHuMoK4CpI4Jd46gM8m0R-SA6u6qHJy3UNeD9ikuPmE4yEMdB6xLdZ2vIs2GwZfUYlQYj8A61gfduvSH20fNAo1-IQDhtd47Eb6HzK1pLtDUS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار کشتی در تنگه هرمز
🔹
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/465256" target="_blank">📅 14:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
آژیر هشدار در نجران عربستان به‌صدا در آمد
🔹
سازمان دفاع مدنی عربستان از اعلام وضعیت هشدار در شهر نجران واقع در جنوب این کشور خبر داد.
🔹
منابع عربی هم از شلیک موشک‌هایی از سمت یمن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/465255" target="_blank">📅 14:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItK5BxWatGFcjbpQ8HpAnnpKkJCx3-Fv9dgCoIHNEucV-oi7CaEsbCJNwTWjrhWKRCLMwygrNqJuaVqN32D7db2QMF9eHkY9rxvuWTMCg4fD-T0udwm7bHs7HeEtljHpHOxZyaKNmv67t0DuKt_25QnLSlbc-XV5vYeHreSZVqSn6aZCiW0YLoLXV2-eZhUnj9sKln3c0n6gJYamfAmj7cpuwSxl2JDn2EdOuS7d9JSxfHAiA_8ln0lygf512Zlxqu4jb7uiLRDo1uiYXnRpybIw87by47KRzV2URWcZfMEo-_L_H17hZ1ObAKUCOp7YSjkGqKKSOtLNeRobiVF0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwF0k95DSi2ENYOJ9uCC4HNH2Pvy4T_-PQIkgvMC3rhT1-sJr5aLzhNRv10ufo_PBdFK-93z9fXIuA2srAvVciRvPqZt9Stxr2Sj6xeQ0fbbGabPPshskcWLj06qM4LuTO5UInpgYHuxO0jFPJUdEVpLo6rgLuJAvFHj9KxSTbao7cMiGZFTLmxTq9x-7_ur1ra7DiW8DsclTUFqabBFF3S7lC63fXuID7lU3x1Hy-bqQLU0Q4lX6xNGsZvK2S_mYGdQmMWxedsAuQCsm-6CbsSEfUbCKX3tKO-jh7_h-gXFq9KWh2HKuRE2FMCViD3WvFgO0cl-rmqABXsDTqKe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQH0jhmfUprVobn7pZ8J0sTg8RnURxejdekZAicDk_fNtwpfz3_IpmYgfN_RP6LsU-aeTN0kX5rJQao3pDvB5CzliJT7id4-4nS5fPpenkzz4nOuTbpWwm0TNnbZZASa3R69BTaz3JtznMo8ZJYh_yVur94rgi0QLrtgx3ju3CzBBoWW5A0EmuRlIRmCdAVQYEYj33faI7wLm2unW75aQ5ECw9KFJREh6dkaYQVqGy2xwiEqLibjSbJ1u0WY7LMYlFI1S-2pbU2q3ycYK6M9DJl2Llno0KB2Ke-e1O9UemUS-pG5UbggaC5ZtOZm81q_SGaF3by9-PJpVsMpvJ5CaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVgQSz6IogpsgQG9IWpM0fwJAx_RntIjrcyN9DB_eEl3Ns79PlIBwLi5Il4JFHvvAz9I4sF2ZbHmZaEi2oDzoJZlS1BeeMDZ7uFSkcu0Ho_UqsW2OBivEI9dDwJqzXjYcBlU6vUF5A_foWXvnJ1hYZyLaXqBZl5A4KA8QmxkJE-XTW7j4X3cMuHxWsRX47YVPxVxwotjnP5slSHq9FFFzT8_Gb8EYYcGLbf5cVWlE4_muFe2I6uyW1Tlw9yFBf9rhsN1Hr3jouGUyXvi0IIQKruDiMtUTXGo6PpBwqAh-FeVir-a8EerrGldTrP2R-tvj-nOiSv3LZnOJBwE3S8jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFiwcX9rYC5R4qEAUtZWH83n8RXN3vvSQl-zwIPQv1WH1MHlHYevfWaYEDQrHd1RLdYCdwuGhofrT9FqUgGP5_0cgTHQLMeYjiJW6dWnVg7CcZyGeg_YTQD4huHH6S4oM1-sewhNqbs66yHXwgCpVZBviRaETsULBUgxL-sdg04vjgvEqST8iITtm5NTRjdd4BgpTHgLNaVCoUcuaYhNuiRs2Nf8yqjdZwqpeLIQcewILp620NWIr5dWC4JRN2gQAUAxcCwWYJRG5CNezPtCknyBORVYXn4W2hAiwczueslcdUa41BRsIxg34t4tVS0DPTa03aoA5A9yuiOmC7rebw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست کمیتهٔ راهبردی انجمن مهندسی گاز ایران با حضور رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/465250" target="_blank">📅 14:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytoqXM_EConMWdyytAE_QtBAFVpxF56KwgaX76DrHfBtaip2ruvh2FhaRZfgch9k3kNZCrlsloqjwc2-GJwqcRBowp0o3aDvutKUPSUww_RemmsZibugifHaX_bGiyoAjsUuCxz2tK2G-sp-SandEgD2NAVGgzwM4IGCs6Yu-HeL8UxmnAzrGiVAG3vgwpoR5-1nQdWL61ngHWwNXVMQlbFdwDgpYafKNS-s6RtwvkfCUpMFp1_RSmhgeUbuRvj0KJUxsAFN7Dn-FGkMnOmfHCMiNpjw49hWnZI4_aJf8FEpzRp7iriV-8zkGI6RxpHjmSRrGygv4xW0k2tdlHCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت پیکان از ماشاریپوف رد شد
🔹
کمیتهٔ انضباطی فدراسیون فوتبال شکایت باشگاه پیکان تهران از استقلال دربارهٔ استفاده از جلال‌الدین ماشاریپوف را رد کرد.
🔹
براساس استعلام سازمان لیگ، قرارداد و کارت بازی این بازیکن پیش‌از آغاز محرومیت نقل‌وانتقالاتی آبی‌پوشان صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/465249" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2038aea258.mp4?token=g7Hx1EcsPc_E6a63i0gDZQ3J_swYpWYDYqZNRVRo3B2P0TBXcNvIBia24lgaiS4ex2HPb9fWUh2GxivBvLTlHhJY0Q_OrPYgNY1DjV3k9BtLPkDHcxZ_gsN3s9KmvsgPB6o7xBPv6PZ0HmoNIgTGepf8U8eMN4rPbVjlweqcIY8EpkenSHg2DN9LBPTy6ouYWXaK1ZUZtogY1_p3ohG5Wfk6BfTQU7Jnkyo9n8UNVXjzmr6WtgYyvyq7oAJsj0OefHRo5_jKTq8zDLuVgIGzM2CEOdfMRUgcvPjbL0-bXHWu-ypo2sXcYlm5oIJM0O7Ic34eZCHe72abe4X8iOQsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2038aea258.mp4?token=g7Hx1EcsPc_E6a63i0gDZQ3J_swYpWYDYqZNRVRo3B2P0TBXcNvIBia24lgaiS4ex2HPb9fWUh2GxivBvLTlHhJY0Q_OrPYgNY1DjV3k9BtLPkDHcxZ_gsN3s9KmvsgPB6o7xBPv6PZ0HmoNIgTGepf8U8eMN4rPbVjlweqcIY8EpkenSHg2DN9LBPTy6ouYWXaK1ZUZtogY1_p3ohG5Wfk6BfTQU7Jnkyo9n8UNVXjzmr6WtgYyvyq7oAJsj0OefHRo5_jKTq8zDLuVgIGzM2CEOdfMRUgcvPjbL0-bXHWu-ypo2sXcYlm5oIJM0O7Ic34eZCHe72abe4X8iOQsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام میرهاشم حسینی از جایگاه ویژه حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/465248" target="_blank">📅 13:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">An_Open_Letter_to_the_Honorable_People_of_the_United_States_of_America.pdf</div>
  <div class="tg-doc-extra">367.7 KB</div>
</div>
<a href="https://t.me/farsna/465246" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامهٔ سپاه به مردم آمریکا منتشر شد
🔹
سپاه پاسداران در نامه‌ای به مردم آمریکا نوشت: حساب خودتان را از اشغالگران فلسطین که خواه-ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
🔹
در این نامه…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/465246" target="_blank">📅 13:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXY4g3qpqVf-ddtG7wkF66WWw5l6pE0mpXhwKPWKfyZwxZK-fmLIgw2EGEnbKgKMZ5udh7C5NgX48jyraFwpSc2y6-sjg42SBHSAFfmo1OFlrgJD5oJoawKHmDZeGk-u0HNN59sKWGI2-z8qpKNGWO9eTN-LVS9-E_MI17jbcz6VT87L2RllPIFDPlJ9TScdofrgTSCdVwsE-IBaqu1EfHzRzYikVHwS0ZPzzkn9snpLLSV5dT3RnArioR45BAKqrX2b72bPZfMeLoDVJjQdD6BOQkEgwtLbQIajbY0k7pxmAxr6JmedqOughl8QFvC7uyf6CkW0gG7JkFWhj5M2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی سپاه: دشمنان حتما سناریوهای دیگری هم دارند
🔹
ما از آن سناریوها بی‌اطلاع نیستیم و خودمان را آماده کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465245" target="_blank">📅 13:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sukuj3JNgCxEBXUwh8pW8L18-IwTdJKvVxMzwzV_Yqj3tdlWpPb-PlE63bYqu4xpXVhHBMxfyUJpean9xPO-XC-hWX4Ad0aT_wCSTGxagPV6rbaNJR6UD4RBDPlr01ZrC_AYf1isKwf9xZ6AUeCwCkD-d4KPRCtjgf6aqoxhy6WjiSg0iJnWhCFyyUzPcAKzwneRousSy3YLps8MHturEVzXHibJ4sgEcOczGB2eqxN1d6T2XMj_lBmYZOQ75EZX6m563xy8lQel6q7H6tWhGoAF1_rvU2Ugs7hWGWZzglyK8dOKR1sYQ7RUz4URuhMm22LsW5MAGyld8_9NmKGV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت توقیف بوئینگ ایرانی در استانبول مشخص شد
🔹
باحکم دادگاه ترکیه، یک فروند بوئینگ ۷۳۷ شرکت کاسپین به‌دلیل بدهی ۳ میلیون یورویی بابت خدمات فرودگاه استانبول توقیف شد و مسافران مجبور به ترک هواپیما شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/465244" target="_blank">📅 13:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5MDoKZISEYdxuM-d8_weBILOsJkR606lTGxDcQKnxxRWruiQlowpaRtDYye6RIxvl1V6cWNUt0u0n-KKGcnayzQb5CKmNsDNFpSVDGI6uHPKkmzDJelTV_iC68guJlENNMo_Ga2-9eA4OFg8Tkw5C9qhqdHDwsh-HGOceqIBVFbPip3Wf_5QdNa2R2pKbFULg6q22JlxmukFL3u-BiygGfKDA8McDuBgvp-_38NhlEdjQO6FJdcxyU_-2R1ei8dQmNCxu_af-Vl_N0a3lfzYFMoekOzk0hqmSvs8yuVt0kWzxJ5ozMsv73KkuhBD2QaxG66U95IHm8P0KxymFddyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۶۲ کیلو تریاک در اصفهان
🔹
جانشین فرمانده انتظامی اصفهان: درپی بازرسی از ۲ خودروی توقیف‌شده، ۱۶۲ کیلوگرم تریاک کشف و ۲ نفر دستگیر شدند.
عکس: مجتبی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/465243" target="_blank">📅 13:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5447a0d6.mp4?token=gY_8GJzQ4ysTUIe0lqU08i9nXiWeovhnZApjN-H9IXS07gtQ41K-_-40lNAiIaVTv8jQsRV7I-d8ntG7AqW3xphztTjxfTbKrX_8h14zPrUT_J6XbyAglqHdAYq2fFHA89brGQvz84BGaI7Ip0OILlszrzxXBK_7R3K-_LVfHOTNXIy4rvdXsyVILPh-P8qJmXzGI2MYrqNoo1IFiY3NBg-O45Mb4bPmYz7OgjClo-1Adn11HaQKmahkD5bQrI0KBQmSan6YzODZXg1mVhFo4xEH6aV-T-xm5RsgRcUncE7E39k6oiquMrtodZxSY03Or2w6N_qdnF_VDHOvMxd2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5447a0d6.mp4?token=gY_8GJzQ4ysTUIe0lqU08i9nXiWeovhnZApjN-H9IXS07gtQ41K-_-40lNAiIaVTv8jQsRV7I-d8ntG7AqW3xphztTjxfTbKrX_8h14zPrUT_J6XbyAglqHdAYq2fFHA89brGQvz84BGaI7Ip0OILlszrzxXBK_7R3K-_LVfHOTNXIy4rvdXsyVILPh-P8qJmXzGI2MYrqNoo1IFiY3NBg-O45Mb4bPmYz7OgjClo-1Adn11HaQKmahkD5bQrI0KBQmSan6YzODZXg1mVhFo4xEH6aV-T-xm5RsgRcUncE7E39k6oiquMrtodZxSY03Or2w6N_qdnF_VDHOvMxd2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان آتشین موشک استارشیپ در اقیانوس
🔹
استارشیپ، موشک شرکت اسپیس‌ایکس، در چهاردهمین پرواز آزمایشی خود برای نخستین‌بار از مرز مدار زمین عبور کرد و ۲۶ ماهواره «استارلینک وی۳» را در ارتفاع حدود ۲۶۹ کیلومتری زمین مستقر کرد.
🔹
این مأموریت با وجود خاموش‌شدن غیرمنتظرهٔ یکی از موتورهای استارشیپ در میانه پرواز، ادامه یافت و فضاپیما پس از انجام مانور ورود مجدد به جو، در اقیانوس آرام فرود آمد اما بلافاصله پس از برخورد با آب، در یک انفجار بزرگ آتشین منهدم شد.
🔹
اسپیس‌ایکس در مراحل بعدی قصد دارد فرود و بازگشت موشک را روی زمین در تگزاس آزمایش کند.
🔹
این موفقیت گام مهمی برای برنامه‌های اسپیس‌ایکس در زمینه ارسال انسان به ماه و در نهایت مریخ محسوب می‌شود؛ هرچند انفجار هنگام فرود نشان داد این سامانه هنوز تا پروازهای کاملا عملیاتی و استفاده مجدد فاصله دارد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/465242" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77a777410.mp4?token=LiBMEORkFOFKl-HC8vpArYTzctEhTAWhpdkzKYJi1rKQQm8t3DYh69RjYGwPvEqu7XHQ4CHmDFs6F_EAkAByTTBJqMavwANaMhs7USfT6PsARo4tMsvg95h9RMI76SlxKaLPDLWVdSuWMRni8ZET24Bo9x-N8SdeAgEiBCm50LRiUOVcDmaqm1gbFjIb5goSIbJjPeQgneQ8BqIJQt0i2JxwUNJxSCVs4vHOtSWAYhpDPDtiny2g8J8MZusUX_Ehn0pg2MT7w86iR-_b3cyW3SkLg6zUp5JMDFCppui5zzT0YAMFucM2oeAkZV3XAO64s3z4ahxv2fjbVPORiyf-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77a777410.mp4?token=LiBMEORkFOFKl-HC8vpArYTzctEhTAWhpdkzKYJi1rKQQm8t3DYh69RjYGwPvEqu7XHQ4CHmDFs6F_EAkAByTTBJqMavwANaMhs7USfT6PsARo4tMsvg95h9RMI76SlxKaLPDLWVdSuWMRni8ZET24Bo9x-N8SdeAgEiBCm50LRiUOVcDmaqm1gbFjIb5goSIbJjPeQgneQ8BqIJQt0i2JxwUNJxSCVs4vHOtSWAYhpDPDtiny2g8J8MZusUX_Ehn0pg2MT7w86iR-_b3cyW3SkLg6zUp5JMDFCppui5zzT0YAMFucM2oeAkZV3XAO64s3z4ahxv2fjbVPORiyf-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبریز به میدان ۳۱۳ هزار جان‌فدای ایران تبدیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/465241" target="_blank">📅 13:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBKFCUZqRaDeN-oZkIJd7HrCVBgpO_oqFNm2L_VB9WU2wm0e1rDTjQIGoWf9d7VO21LQ-QLB5EEEjQx1q95kvXt6swp9cfMdZRWDnxH9A7gz3jV-NTDpVjCcbC8l1gFgoGv45dtbnnIvut1IOk5Zxh3vBcGLVXIjxe41bLlJSVpYrUVbRJdt1gdVFirisgItxDXOIaViEsy_afrjgLiDko1papyWRBKGx0gqkvriaUHSpnNa_LUIxHdJZljJAz6YxslW_e1w6xCUTg-6Nx4z1KJeAAxArT_B9dOfzwKBO4Wx4E6q7t4xhd9o0MAe9_wmhJrWjhZEC9Dh6XH_h99utA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب مجازی پای صادرات میوه رفت
🔹
دولت برای جلوگیری از خروج آب از کشور، برای صادرات محصولات آب‌بر عوارض تعیین کرده بود؛ اما وزارت جهاد کشاورزی در نامه‌ای اعلام کرده برخی از این محصولات مصرف آب زیادی ندارند و خواستار لغو عوارض صادراتی آن‌ها شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/465240" target="_blank">📅 13:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03c135011.mp4?token=eBu6uI12mmr-111PsMLZPXIUR04VDCHNYIGQt-V7EiCNxKa7NuJnI1t_uhr1xG1_XLy0LdwM9p7sfk5aECvTBFAzbYAP8GsjY4N5WRAz1VaX56dkaoMTEg8xONZeUtkuK1bTE0NhvBNenCb-4-EI2sfhvhgx31LnElD9UT6H9vejQHeHbavhrMusQeRgE5jQUehq20MfVeNQ4uImh-0AQYV-Z7EpHzQovD3gaNWCE6IwOMdfIVkhaaREm_kw-5k0f3-iJN_hr0KMj5ksqNq293NHUn9udqCPEMSlehCabWHhzLY-5iAXNvfgu9uILo6FAnI5unlzcr5WCezZQ6ZuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03c135011.mp4?token=eBu6uI12mmr-111PsMLZPXIUR04VDCHNYIGQt-V7EiCNxKa7NuJnI1t_uhr1xG1_XLy0LdwM9p7sfk5aECvTBFAzbYAP8GsjY4N5WRAz1VaX56dkaoMTEg8xONZeUtkuK1bTE0NhvBNenCb-4-EI2sfhvhgx31LnElD9UT6H9vejQHeHbavhrMusQeRgE5jQUehq20MfVeNQ4uImh-0AQYV-Z7EpHzQovD3gaNWCE6IwOMdfIVkhaaREm_kw-5k0f3-iJN_hr0KMj5ksqNq293NHUn9udqCPEMSlehCabWHhzLY-5iAXNvfgu9uILo6FAnI5unlzcr5WCezZQ6ZuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
🏐
کامبک ایران امید اندونزی به صعود را ناامید کرد
تیم ملی والیبال ایران، ۳ بر ۲ اندونزی را شکست داد.
صعود ایران قطعی بود اما اندونزی برای گرفتن جای تایلند در رتبۀ دوم گروه و صعود، به امتیاز این رقابت نیاز داشت.
🇮🇷
۲۲ | ۲۱ | ۲۵ | ۲۵| ۱۷
🇮🇩
۲۵ | ۲۵ | ۲۱ | ۱۹ | ۱۵
@Sportfars</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/465239" target="_blank">📅 12:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49dcec5a0b.mp4?token=cY3clFTLb7_Bc-dyxxRdi4jfiQpVl0rb2yz3ynEcdQxr5E7ICMjb3YNKKcVn9R4CjYaXQpq-iG0ki6xtDPJA7fOn-H05QJPWaJr7Cvoy8GGYrCKluuje2YJFhGkooOoXqJOVyZsVV6UuJED1JL1SnwDABavi7LZEBs884gGgP7CReIkhXx9e1qdCxBJ2aVsoyrL7v6SIJJ2_tXOId3oIUb_-fXeLB8nD8wT0V-HtA2-axku3KH07IbShjfXhk8UMsJmvs7egwCJnbV6tIbKVXftu4FxcwiFv1EhA9OoGeQafA0LBV-lANflzBEErJxOTT9lBV4h3uniRRZuWAVuTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49dcec5a0b.mp4?token=cY3clFTLb7_Bc-dyxxRdi4jfiQpVl0rb2yz3ynEcdQxr5E7ICMjb3YNKKcVn9R4CjYaXQpq-iG0ki6xtDPJA7fOn-H05QJPWaJr7Cvoy8GGYrCKluuje2YJFhGkooOoXqJOVyZsVV6UuJED1JL1SnwDABavi7LZEBs884gGgP7CReIkhXx9e1qdCxBJ2aVsoyrL7v6SIJJ2_tXOId3oIUb_-fXeLB8nD8wT0V-HtA2-axku3KH07IbShjfXhk8UMsJmvs7egwCJnbV6tIbKVXftu4FxcwiFv1EhA9OoGeQafA0LBV-lANflzBEErJxOTT9lBV4h3uniRRZuWAVuTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین دارایی ما توی این سال‌ها چی بوده؟!
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/465238" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXf4g9TC0mptilJhO_alNOqXwUcX7py2CfYZsQgwFADmbGuClT-hi0Kcfoie0DAiAoZzXvush_PJnibh4mUorYVCHZvuy_M_A5rlIvEhIIKAwcN9XswsmLtND-KCGzQ6q3dVt4EwBO07tjrrIJ26nsXS964CZ1Cy-J7WK4okZ9nsHBtm_q_kfFX0ReRFnjtOGNngwmqbCWOGOCwQZjKX45vtCGekhTFzo-1i4_BBmaEZa3uS5echAY8NoFSFz4LluFwZrpRCppHxYFL-Al53VUPCmbKQ5KsH3BBovePHZioEjJIXDJ4uCNRjO7DOV6okY3P_rttwUqdkcRQNS8S8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به مرز ۷.۶ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۶ هزار واحدی به ۷ میلیون و ۵۹۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/465237" target="_blank">📅 12:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788b51378.mp4?token=GSnHVupzY6ln7EO6TXvAAuNN2ioK1LdAnSBj08xP-UmAKjgK1qrV2Jba95rD5bK6zv3Hoaaw_5KHYuDEKSlZYXY1QCFXkKCHlekoISBwRhR68nRf53W38Xms_0ire3IIlhuR9ZpVVdVf81TeBVbNQFnLfEj86ogSINkHLrs7XCsIH6fkYPNQ0NE2t8qjGV5oEk6G09x36f2p0KoRe_PsD0TqL1NLkiNSm_xhScAMDuuvTgMGzjzXncX0VI5f6NOUGi7b3Mdi3v-JknYceoI6IfZdFUCuHVcTwnJQTMl0qjRkgvcoYn0S1TXdbOiJIiJh7L9AYpZ4YXvZOdiGno3cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788b51378.mp4?token=GSnHVupzY6ln7EO6TXvAAuNN2ioK1LdAnSBj08xP-UmAKjgK1qrV2Jba95rD5bK6zv3Hoaaw_5KHYuDEKSlZYXY1QCFXkKCHlekoISBwRhR68nRf53W38Xms_0ire3IIlhuR9ZpVVdVf81TeBVbNQFnLfEj86ogSINkHLrs7XCsIH6fkYPNQ0NE2t8qjGV5oEk6G09x36f2p0KoRe_PsD0TqL1NLkiNSm_xhScAMDuuvTgMGzjzXncX0VI5f6NOUGi7b3Mdi3v-JknYceoI6IfZdFUCuHVcTwnJQTMl0qjRkgvcoYn0S1TXdbOiJIiJh7L9AYpZ4YXvZOdiGno3cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ساخت شهرهای موشکی به‌روایت مشاور فرمانده هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/465236" target="_blank">📅 12:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=CMh11Fd-a9wxIHnisr9WKoojBbB1YCOgRmRxJwXUnIy60qeIOBX6lyCDW_S_JA6ILhp_9nynP2S8xRlbcvJadvsKhRYvhl6q1dhW6tp0V2CA-KGiPskMhk9TX1UpP7Ls6j5gaAinVff1fEEg7XS-hc08G3xkcQLMrqa7GJPXV12cohAh4CNIw2R-mcfA2JP51ElIpQ7Ef3be0VeOvOJgI7BuRYCz7_XttJXe4rY69_ESy1DYT8OYwMF-0HgYQ7Ifi4kjL3kKk1bITUHdgwkmBY9yUU2bdZIhitjF_dRpof-idU-FnS2vVt932L5Qx_7c7LP9gM6TlEg9Fg3U5JJKHkPcQbuDuFOEsNDYnZ7LD0eAX68_AYzLYEqnp0O5V39b5uNdzX9m-7c4HQIEUFwUcRuTkEx1DQoEpi-LM99eKlsY6vZqNiVV-1T4UYmgvzUKxonMpozJsfpRlbYPpOGS3hP4jHc9ryWYD_Cp0-kErHNL4ZAkeOhIIODAz9VlN6-5NK3F3WS3rPU6DXqC_mPZuxXAh8NlqawNNvYbg7kfq_wKYCIOR1eriCJpaO2R9peyOgeVDTwSdSZG4IAEMp2D2XXzbrR0C9rUpYN3a6pTOEl_0F8xFewse4mbKIg2DLVq7ijq-ALwR4HnUMEcITmj34JhAF-WFYB2H8vj-ptLmNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=CMh11Fd-a9wxIHnisr9WKoojBbB1YCOgRmRxJwXUnIy60qeIOBX6lyCDW_S_JA6ILhp_9nynP2S8xRlbcvJadvsKhRYvhl6q1dhW6tp0V2CA-KGiPskMhk9TX1UpP7Ls6j5gaAinVff1fEEg7XS-hc08G3xkcQLMrqa7GJPXV12cohAh4CNIw2R-mcfA2JP51ElIpQ7Ef3be0VeOvOJgI7BuRYCz7_XttJXe4rY69_ESy1DYT8OYwMF-0HgYQ7Ifi4kjL3kKk1bITUHdgwkmBY9yUU2bdZIhitjF_dRpof-idU-FnS2vVt932L5Qx_7c7LP9gM6TlEg9Fg3U5JJKHkPcQbuDuFOEsNDYnZ7LD0eAX68_AYzLYEqnp0O5V39b5uNdzX9m-7c4HQIEUFwUcRuTkEx1DQoEpi-LM99eKlsY6vZqNiVV-1T4UYmgvzUKxonMpozJsfpRlbYPpOGS3hP4jHc9ryWYD_Cp0-kErHNL4ZAkeOhIIODAz9VlN6-5NK3F3WS3rPU6DXqC_mPZuxXAh8NlqawNNvYbg7kfq_wKYCIOR1eriCJpaO2R9peyOgeVDTwSdSZG4IAEMp2D2XXzbrR0C9rUpYN3a6pTOEl_0F8xFewse4mbKIg2DLVq7ijq-ALwR4HnUMEcITmj34JhAF-WFYB2H8vj-ptLmNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موتورسواری روی پل عابر!
🔹
تصاویر منتشرشده در فضای مجازی، حرکت عجیب یک موتورسوار در مشهد و استفاده از پل عابر پیاده با موتورسیکلت را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465235" target="_blank">📅 12:07 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
