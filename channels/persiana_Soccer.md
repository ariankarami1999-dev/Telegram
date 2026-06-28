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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 335K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 19:15:55</div>
<hr>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qw4qp4dxEDFqU8Q5JOrcr1CiJOqzRIqTXSDljYLzf_bm_cppHyNSCa5VhaqLJehNL_Fnj4LZAgmCVWOH91EQ9C2kAsye0MFLco3nZcbZvs6IhjejmHjXsPcKYriGJpNqp1DdIhsYsP86tBUt3NE1fJnQQ7qrbAjtw1PzkYiIZufswSqawf4maKWKrbjom_qAcNKOgS6xLLls7apOUvuxfvrT41B79OawQlj8p7cFrxnPRBAOSTFXNkkbyn-YOElxvb7kwB4Y3xvSBP1n5ddJQwNtRGSXjoB5g6cuLP4fm3jPpxAfPFgY0ZyCON9tbRNGPPD1n-m0cwI7GF1-fbSApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بالنزبت هیجان بازیهای جام رو چندین برابر کن.
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوسهای روزانه مخصوص کاربران فعال لنزبت
🍀
🔣
0️⃣
3️⃣
کش بک هفتگی
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet8.online</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/24547" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZk8c5Jhrre3xCGyOMIksqCLExIjxfj9Fo8poYUGDB4OWM75Peuc9_NGeNTrlU_ORtSl8zdM_4uln_m6N3wzmrp7bsmd1tLIYy5Jc2dHWpYn7g7Aho4AJdON_vZr4STNw-7efOi73VXb7iWEHBJeRdVKlLWo25DIa6OHUm9QlWyBlGGBtboXgEqJNMQ0wIOP3gaSJ2W_YIVkRuYYqk_WH1Sf9jBErBvaDviwY4ln7qKaZoWi72DgOkohBDcv6hh19MvFBKZh0cmMNEIURHTIAyV8bL3WQA0My20kyC8Qn511E8B6XfEzilxw4hD6G0EbY1_W5xgXgllkXIV8PdLukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ema4j1ooSJbESNM_v-R3SOvnQTapSpt_3BCQNrBNNSor8UkIBtiRJolT41GBgnsON0TqodGFkOayvuSsAyf4A15hbtKlmlWQ0pjQI5rLW2CmqBfK9SJhpD9L8I_VADLR6QSXeUF-0vL_ce29HgTC2eNUJyldulQfRyyhoGpL_TXyS7D6dAdbiyJenS2CfqXs_crIwraQMFUmk8cPPz364L6ZtZTkMWlNH3H4EG8jO4KfQB59zubBALDdfnBGuqRyrv1Wpjs0OthIBwE3akpKLkXD5_n-7WhGZMBrzF7ng7tAwJrKp5owvumkp4J-11zap3eZnFMhdvb6M8fpRvWZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSzGB67SdAGaRXEGZLiwF_ft94N_0_4RLYVzQSsm1PmsSncAnecT5BqcI3TZbiv6nOq-UMIhti29vfykaQCYg3XzQFsZx-35-J6DkggLpdaLG7lTHDE4JuIXmOp1BsCLbwMHup8EOFbNzUKlCOumwZDTf6auHjJHWZRmPMaOLQeMqPat585A8RjToyyWeNB1nbBWq7BtGXRQ7FQam62Vqf4cqPx1D1Hhv7-iDTfek4Aos2x19BHwxa6kh9P7rfpS2ye2b_4pHtelypt1bC4Jzcs1G-7da8_Xlky85ppJft5N2E-h3uKAt-bKVoMQYJODk3LPWqAGkNd60VU2qwZ5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnOZ_m9JN_sIUuQI3fRuFgbifAaB-XF1laoAqvmT4DYfumxPW07DrTjpPPMUZTFYEQ96IsRd371DWkMUSmMQRA2FRtFKlKaz1jUY_E6Bk_SzUDZV43O65sX0o7s_43RHSYr4bAbFOAJ-TaA84Tqx7FLBuuukLayY0Qf25FevVzfRUmv8aOrMZ03UMfEcXoqIcim_z2vzupy3BbehCd2wWcPGUeeQBP5GmyaCQqEokEHVyYREAPpOG8bSEb1Efvt5gfmyMIGrxnz3E_wfirsp9wB0EjkvY8CUEWA-C53ufUmOEMDsf7ubwe9FlyTF_T0kUODrM-qOTK6aSGQRxUCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-kg2ncUVlUXg4K3XO-TmXPQPDBTMsz0Clae2KzqC0wCLWNUHotoz5shQmak2LsKIP09MIiSIR4ifYvT9TryXkJrJpqgqm1BZsamAdUFsbOWBUhqNrONsVRu9wqsR4nKDhLVZPIuwvYH5XtviYNLOW1S6qzQN3kqdiG-Q-I2xsX5JcqoruT45usGWB6fDMKGRUVvq_CrIYlFlTDfTRNeD36XGUQcDqhOwAZh64-ZTlLLtjv93D9cqjr91Rwo2Un3PHCpLr9Gryo__IBf3kcrNJ6tJk7_EH34ueqxSWvGlIz6_Gw42yD-59f_Ne-_EXUL7Em2DmP7E482sBH6_oZBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikL4Qk2tPCmLjTAhmx8rndSanhUkqXZ7hR3T0g0i2IOzGsGUmLWt6gKBvolHnBr2IXWYI-hYuDehZo4N0N0F8Ci0Uqj1bxqwEdauTAXh-q-ceEIJPwdrJdzfJDwaI594oPVUEXNmh_0GsfYHv3KQVHabUEm32upeTSilGWN2WCs9VprVAB0pZxm1ArOy5zG8tGfmd5yjLZPpuA9jiuGXa4yCv-J_Bweju4EMUyphtzdEH35CTChOAc0m-QiYwMdBi1_cEoLm38EPKl1SpLeDzwVs03h-gzG50QbmL4zH850YGTrODjstp9SJFm4qcqwy_rx933zELBCBOzIFNgimlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiJg4U_QPMfONezQ3RUv8UZpCSPinOVicvgNYvU0XgwlyrTU9OL1yEEPlvjHhn6I9tqHSQlv-GImk6Mn1F5CCXnplCSTV50fkp_Vl9clNdSyrG_DCcR6PJiorUAkC9suisyAPjqW8HYqMUtW52MQHb1hTxSz5YJUGFp0CRy-zx_-bxtSGuTkV4BJq7L32p2v6lZHVvHbZkt92m0uXmPehrkmFOGQmCnFrVyDESHgPogfd9XrKFr4NsR8mEMasWy_NM2g97FQwyxeocd6ygDLoDQ0dXkX0itxIU8M4GO_DO2kEq9pKR83CiwVL2vNwdOPwdVy9Hpj5sZxUisI-jkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn07myubOlcHeRcSxL4WaTSG-JulvXyRXLlSD8aRXyGuQaA6KdrARfJrepKuptyuQUXcW0WidWG-0OpgklwIUUvlgZOFbTPkjoJPMlPnzgmmmdeAA4sCgRya9DAPF0VPH02gwXWAccQNYADoEuwbNNk984KNC4qJ4lwP0-ftF7Gpi8OMt1AdOiqACHFbqrQGbTrJth2EXY0E5elnjypwraHjFmBjBSvI3Oir65FCe9Is83fKvsHpmJPRd7O5-sKkAGg-HUQ9NeXHRAOtJvq9X_V_Oze_hP0QytYHQQwVhFiGJ4nWMlTc_eJYK23uaUcZFIu5e8mWTP_VsoI5paWhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COHdbmYdKtB5tSRyNzAKSzCHBDpMYz8bJziwrsvNFrky3GSNsJLxpyiNv-1bWuVmG_gYHffGduYlLRcYzAS69fhca8ReqprpSJv0L4FCgkmNDSxnULKWULZBSSs6gX8AnGisytqcnkbZMdeJNE1F5Ctm1foFlnR-26aOVNSbRWqngbZnFaFUALRqx4r8tuWIub6L0yNl4zNtshsM00ZHnCbCkf5c2hGnBqfRydWGIv0bbXJVLNQdkBtx90dzU8NNdcg_G9sCcfN_xRyqNwYNSXZFwH1ic3o_Yeo7kMupu7UHrQgIC3BGOulRkhvHy9Yhtx0Ni2ux7-nAnPYP02AChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCKVYQmNdKc_HEqnWUnzta2rmLuVAT5digCngF52po758pvbd76s0Oa3Z2kq8VN49EVS-T88gmKuYjnweI2cZStWw_n4D3AOXNR631K6EYQxWS_NzwMS9XdlyRQZUFj23uE8ijVFhhJmiSnhv5o_2JvhKWPb1Ut-0fB05wpvpneg_-4_9Elxq0RikxC5cjqHYAY_W-0XUlruILxQBql0cYFHFABdSosQ6EzbhmIuf542Di-cHiseLbGsMDEMpjTd0k76VyxNNZNFtlh3izq7lkh2iTOtkAeBjWLX98WPsgw94iZ7Fd7sd9eaRR0OdHuv958JkKLADN7OgPapmpFVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_W8yB-nC-ncJ9Ayc0lAgAPo8He8yAM87Ja7vh56nM0CYm84WJ2XuSQOag8rWMxeUtn_Re8tGvxhGguQ8pmCBYdbcdvkAgRzGIpPDWxlhQnzYbSmQ_HkM9oHhxnMxnf96c0GEOiRJDMEk1jcBugjjQ2fqJOPoz0bzZayrcOPylULMrRsVFizsxKLv-M79NeRzzMX7nE0GNfTX3yTqd4WWJ6ve5RieiAU8gpIkvvFsz9QWZeJtOBQfpLhPdzRTsgItcfJZaqj3wOww4e7KFCyRqPuP1LsbqVNCL-BzBjssc829Ektd-XCC8t2mN5pJdHy2MFnOorpBeFwAq32we8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK9XigW6u7bmYUaRSRtZkf4AYCPHHry4yXA8l0Biio8jQg9LvqEoVVvs6aWOXs_rbGATYuyt7ow4P2kkoiTToLoBVb5H9G8vHymstArzw_XxGo0SWx7dPB4hYCtZhlEZc_iGmz5KSwcCBmzT3bTYmJPouboNzrkjNO8yVyi9IyZ9TpEEx0PH6BiuBYIuDm6WWNAuBsrpoJZhY0V14G4JR6kbhTdXyxPRB4cuSUP8syPYQ_I6zqqfGytb05D4zOxNiRc7Jq9WH_mWjk3CxyTEdqo4YTddkQ1X6T6K72MVX3FxY9mGpClS7bge4hNN0rToe0I0dfok8JR7GE_rGRee-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqbPGNa2CEVHb7hAeiJ5Tg7-05Z0kvP3y8Jiqm63UZYDK92mHNP1QCwU1qVdzHC8XnwP4lWRQ9vUK6gPmih2d0yanZQKcoC2QUHbNi_ff9ilImnH_qQbEV7i8vcNbwax3X2WXl9E3HCr2e25Wr9Df-wqdW2OcGL29qatqOPzV2yVox6ISlWA2bMSJjqdPW9S1wK3Lxx0Cf6UDIEPRRn8DC4qo6bi7prRfIkoz4fIIW5s7YYEdgjcQ6KTAxrtBWU3Yu-8LYR4PI78UJBJ3T9H07Z-pA7Rcey8Xlb76GSE2TCloS6Y-kH5y49PCI1IeZvleDOsEFOLZVqICe6u4QwfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldc3yl7Niq0mdCEA_YflqYVd6LhqVbuHna0ZihIo2w2Fv_HTl0LrgQ2_uB0xlwM5JOi_3nNpP9z-KNwAwwzBurorObO2LFahyrwJHoUcxBfzQEST76Hyj81oPsdWYAjsrjJdtpHJiFw1aLDNKLdMBbI9xKRXDFGitTQXsWeaTGx9efM02gZ0FGUmQ5EjdVI3FkoYOTvdZmywLJqZKJxPXamBysDN36TbNYqJysfK91cD-OW37accuIAZkJ5DhVPxazcfyYU9O6q66eKjjGGu18qeDy2TX-hNYPogY6VTr8FTrTu8Cblbkz_cv33WsEX4G8UoLI0P3t9UjcHbTmAg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agm7aCLOs4hyv_Unh2Harf2pQJ5zxdkBAvPO6O17xN6xuyp0ujhyGrb1DkDptV78s-1l-t5RFii0LUivhfidP2LjBnUDK0O9gaSfPgvRH2TlTsSLIURN1CwV9zuNpmMt_U_PujdCD1LNqYvZqL-gPk91-LppNI2ToqH9GKEY-1R8abt-0A3wlQJgzfOYs1VR38Cx8AsG9Q_qsEB0gZLHME8NMhKvcZ6kq18zkcXhLGpU3gapIRaO-udGmNXSnby7u6WxHjMQDvpvrShMHX2WE5ZhTRVl3BZpB9XcSYnQlmUPmGHNuxlbj1ox4_dCxewYDy_wzIN0kQqyXhdCIGSCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKcfWuNwHLAHqVZ47YcUI4Vxmpx_zQg6RyIhT6_p8K2rmoxUwwiX3zexleU60UZ4jD7ZJknNJTHYp39KvLT9Evqfbq6rTBkTDI2hJhUKvl7t5vyUOtdss54aESIWQ2Xa9r6QpgGOgWiW3IGQjw5Vedw80hcKTyMdjY-ZP84VlAhYx1VdcozhF8KEVmKl_v-DWoxo-78kuHa5_J6V_SBFM0lg-cx-DCmpYcFkG1y4Ih-76ptvpo3MVP2GvvDClW8cImprCkCuLbKqfeBfwgdLJxv19Duo4tK4TvaKIzAPZyiR8g9Yzp7QsYkhJ-OXbxCCkIgzzSNi23QNrYR1tHodsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftHmcY3TNGVsiB93d1AvhIKspGbUwKn9Rbpb61x-TyKjqVG-qU_tdjRVcj71zmfqy94wBYg5El-rVLpU5j_TwhB33Yc805pFQlhmgRJMmlW3WgRSotqfYYptYtjmKTFnSQLgEG5HhAjHC4a22uLSlD3O5sLoW-VqOPxJm_DmWNBuwmii43jPSN4bCyHpXvLcUWR03jszawFe2y9qyuQcqHB3zGlfi7NqxxUMFOUTsifNaO8w_SGnEjSCwLoB_MxNFSWrIBPC3TW20icGZVsBftLMZhHsNcDFOsW7n7ChPZe6DL6UxDv4CfV4PIyCzfI09fSCObuasrxdmh08SCo2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me7nHM-5qbDJ4DVPMGr1XlpSNBCNKzboSPDrdGt2StaORxJC3AP5ha_5lhOBgOEhfs7dII1OmI-T_ksJvd8bEQ2W7kamVtHvNvakbeIJuFJBWWs38K8fKK31aAW7EJdZ309vT7IOApRR9_LN_B0uyF_SmqAQTX2fIVzGv8geFBcK1GUt__N8RTD-_c7i5vEhnJkWyTQ19bMT73_m2QiZfflNc0ArqxT5LiVNEa9x1-iMc4jVyL0r0ChFnqdvrh2LjkrkY5R4fF7VVrck35G1ZaPOJBiYmWBEc3TUJCFeara4cW7NqNMEV0px9h4xpTpRiXu6q44_DaA5Q1oJ3JJlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=KFQy88vW3Ddo_ojx5xTF5mL66_ECn4r5sxSxmGiOfKujx0SJDBKcpVUBE1YYb-m39eque5kzDttfGRWInjhvBb4aJtuV-SxTA42XJmjDnRoPNqcjg2oE_WDZvAQfpw0H7KSDSljb9SFKSL2kii9NOdCRoDyg9R-ZCa8JmKWmkpqK_aHnUXB1ZmH7MvmmLcpNVCaQE5WZW6JwM5vj5E8WgKPVRGuU8PdNPCl06-NaDsuo_snOqpzC7XF3z0Scg-cUesPQIN6WPK6uOyxqXTaTh0YgQYoLjuIk7lbrNUOwfju2Aj2TwcJ7I3TeT1-DFVvXrx01f67ZjlOKJ3zUDQYyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=KFQy88vW3Ddo_ojx5xTF5mL66_ECn4r5sxSxmGiOfKujx0SJDBKcpVUBE1YYb-m39eque5kzDttfGRWInjhvBb4aJtuV-SxTA42XJmjDnRoPNqcjg2oE_WDZvAQfpw0H7KSDSljb9SFKSL2kii9NOdCRoDyg9R-ZCa8JmKWmkpqK_aHnUXB1ZmH7MvmmLcpNVCaQE5WZW6JwM5vj5E8WgKPVRGuU8PdNPCl06-NaDsuo_snOqpzC7XF3z0Scg-cUesPQIN6WPK6uOyxqXTaTh0YgQYoLjuIk7lbrNUOwfju2Aj2TwcJ7I3TeT1-DFVvXrx01f67ZjlOKJ3zUDQYyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHGoJWEIow2G0madMmfxq_rQ2I82r840i27UBLOMs2IbOtXqaa58DciUyNu9eebbYe6QoHt-sJXkEkweQ03lojvz31N7Tq45yTU6HPacx_dKTLPFOJjuIYOWDYb74wI_A8F0TITd_sZq6nUuQM3KM6orhBzy2jugriYw5uXdV0Sl_57hnKK1CWnO4oNvJ6PbaNC8EFfwpQX7FrL47uWyekSOKdS2WLsBf1PhJtXM4_3kBi7YEp7CMHbzhPY6B0pE_5jiTZmHAHzwfqsf_h3Vvr3wlgoW6ZEfl1G0HHGuxU72wxATUT43pHO31MonLt6Kqu5BgvcuXbQuSIHHxG0tEe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHGoJWEIow2G0madMmfxq_rQ2I82r840i27UBLOMs2IbOtXqaa58DciUyNu9eebbYe6QoHt-sJXkEkweQ03lojvz31N7Tq45yTU6HPacx_dKTLPFOJjuIYOWDYb74wI_A8F0TITd_sZq6nUuQM3KM6orhBzy2jugriYw5uXdV0Sl_57hnKK1CWnO4oNvJ6PbaNC8EFfwpQX7FrL47uWyekSOKdS2WLsBf1PhJtXM4_3kBi7YEp7CMHbzhPY6B0pE_5jiTZmHAHzwfqsf_h3Vvr3wlgoW6ZEfl1G0HHGuxU72wxATUT43pHO31MonLt6Kqu5BgvcuXbQuSIHHxG0tEe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXOzK0Fke1hrGE-SU9Ts-S8Nr9P2kHSyDaXSEDVLQBOmEKZVw27ToYZkrQJBGaeA_sfh59Whl4Z3ks4ykxg2LBRzU7RpQQt_GGeLQC8ZNxxKMeuz69VUKwWm6wACXvH3xkYu0FZQdSeiPxnR_OFvMvlBDU46cL67l6kWJMEJF4OyNsdTpy20eWEl3RnGHTXPzs6AKNBzd0qJK3_F5GoXBUMDEzX7d4lpX-RM5gYsW8jQIBSgTZuMFB-6dUghcEfqmPtQvAdE-J2E0hnmYi6TE-U_OzDuk_Tm89D6aGWQKrdVv2uB-DdPuPygYOWq-Md5zcp9BmzCjuP1c9faruGTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-89TO-3YK9KfmMrszLkQGRHFfQhLGE1_2715m7eSBuWko1QidAkxuMsUSIgMNqvqEzT5GDrCtU_FqPIBwuSZxAOPEozrskNEqtrh9u8D0x-RHvws9l2IgwGg-Dhhg1YbDG7eScUFrOEkVpvx-64xz3Tl-pOKJtTx3zWRazivPbBYbP86Vxcf7n9iq2B_SKl06MmClo9ecDDhRp83NRdXsNVTkN8Wbqg9zjqfNynlp_iYD2oAU3GjmyU4kS29QC9srCRJM7NWg_lLIFvyJM6KfuGN9eBZ81iAwx1Oozmzh2n2Wn6iphypKC0vmwvKVYDFpEKkPefel02WgR2u8umWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfTsHEZ4fwMt4vXTtMvEZ6R2_1qlgg34oSGVjcoBI7b45lmSJPxomkZ-3-bb4CUIiTNUu2JeezsG4d_LKrKOdWYiVPPC6VwHtUp0LBXZdfB5pxq2jvpjrAiGMdWatt6q0F8JdAXquRextyY07vPO7JJKc-CHUbhs7eU38k1IpSqORtq285w9xm8W1p8RoLI4vy_xLeIz8cuGZiz5RvwAe9cdQbdrheyhZrEBVjxtHl0V4seRNC2i81YH4yy75ok3tqQkOtCXbYnwY3MNQ4hnX8crcU-Gt0n3nzOwZu4Qc_c9oh2Ya9YUnR7dUwFoosSQUydUg-vcFhXxs93UkXdIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSVx5bw6ZOkuv0FR-vkn45bTT6RypaEWw0OzIDFVr_i_c5KDGQosW8diB0f4DG0LGgUW-7zrR9ypSXovWeZFFyIjdKeT-oD8mFLkZDDqLKnxAagVdrYem0q0iFY5sMeF3NDrTBv5CrAqE5PPO_DpOTNVVvnIxVQvvEfBpkR6ftDK7uMhnFSvtWpGPxcsIKcJoChBHNyZ8TgKeIv4NnOATlW2I1iQcLCZ25ZnTMyEWFr323CU4rOFx3gzlKLrZvVFUBRAAR5BU0LmmzM-r19UR97YKdY2Nn83MPVh-leRV2wiSZENSqP3WnqG3ImILE8iUOXNvQSHOrMe852TbccqkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=CtIC7MKbsEITPpwqr2jSzeBmy9Ir1isxA4B_lihhqqdPMe4dPY2_K2XykKNhQchdd_xdoFEjXGLdD7urCR5Go_rjlWQLYe-BOC6mEH18IIT01YgcjKY9tZgz5qwIDnf1V2WR7E-YLB5n0-SlBj1lTEN4n4YMs68DHhLnUb230o2T0t10PZcNCHZw4m_1rZGAjuHsqlJ20VTnCYp6hRA6p5jgxCfdBJLdiN6UM1UU139AC1kEcOrhgUdcmuk1RkU23gPtqkaPSuI9WFs1x-9z5xh7W4vW9mL24N9jJRrpVwPbsAs4IqZ-3GyFTZ0hKBNUvl5WJZ0g40wOMR6N_Gvbb4BUAL2SZ2jwW4yHUGqSkC87PG4vKxMZhESAkkGkDgShkzlCLiIgVQncub5O9CTyiRebBq1Iwk14mkzdz0JGs8EpOaO6r5tJct0p555D6Y4NTeH216wMihZrSj4TZ6omjMv-Fms-bxQZjMtE2BF7rUHMmaKIJ3EpOCNGruvgQ6MIWwuMz5dEmWVhdx17e_qRVk7G6tYwDvgyRt6oky0BYQPCp4KaEy_KugDpJd1SL50Q6OPJcJGVRiYC0u9KnHy1EDR85tSs7oiwc0vt5BGZ1x0cHIFaShGKMH4mveKkhEgfi0RD4gdzwMMJI_TKSTXk-CZsPgglgvhl2dey9hDAUnk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=CtIC7MKbsEITPpwqr2jSzeBmy9Ir1isxA4B_lihhqqdPMe4dPY2_K2XykKNhQchdd_xdoFEjXGLdD7urCR5Go_rjlWQLYe-BOC6mEH18IIT01YgcjKY9tZgz5qwIDnf1V2WR7E-YLB5n0-SlBj1lTEN4n4YMs68DHhLnUb230o2T0t10PZcNCHZw4m_1rZGAjuHsqlJ20VTnCYp6hRA6p5jgxCfdBJLdiN6UM1UU139AC1kEcOrhgUdcmuk1RkU23gPtqkaPSuI9WFs1x-9z5xh7W4vW9mL24N9jJRrpVwPbsAs4IqZ-3GyFTZ0hKBNUvl5WJZ0g40wOMR6N_Gvbb4BUAL2SZ2jwW4yHUGqSkC87PG4vKxMZhESAkkGkDgShkzlCLiIgVQncub5O9CTyiRebBq1Iwk14mkzdz0JGs8EpOaO6r5tJct0p555D6Y4NTeH216wMihZrSj4TZ6omjMv-Fms-bxQZjMtE2BF7rUHMmaKIJ3EpOCNGruvgQ6MIWwuMz5dEmWVhdx17e_qRVk7G6tYwDvgyRt6oky0BYQPCp4KaEy_KugDpJd1SL50Q6OPJcJGVRiYC0u9KnHy1EDR85tSs7oiwc0vt5BGZ1x0cHIFaShGKMH4mveKkhEgfi0RD4gdzwMMJI_TKSTXk-CZsPgglgvhl2dey9hDAUnk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB4QnEYREw1qLeqYMXReT-2KhhLFO5eiVIAayIBNoEQNC9alRcPddhCqAcwp5q3VnEYFGKSlyFor4aEMiQQUoKoO-V7q-MWOdvXfSO1-2Y-t_lPxGJ5jnEWSr9mJSKCkjrT9aD9wAV7z62eGNtKzsBc9SasmEmRONFQaHnJ-7RJQlKfnt57SKpM5dNSLxOgv_0HiyNGq9KPExOMRqED8EcfHihaaGnZU468q_TLe3OCVcQ2YLvrHnAE06TwewchMVptuKVXpM77TFlv-wVScJ4lggnwnoXc7hYCh_K0W_Cz9586wBfMlJN5y96KapFyXDVgQ3imIQpNaqUmP-BbF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=uiv0x1ZT5qu6xoCsP7_37K5wvfz01Di85DorMxBaF3OmMREDQEB-ga3WRcW5SrOVEHoYHroOJ6ARTGjGEYsTv5iEncDtBi24pXU766vbadJnoiAlzWMay1zwCkAK0e8ASo0OEbMVIyjAfu3tfybAVygaWeCuv_84PgVJbvRohR5x8B_LWrZKJyC4tYHOVzNBtH7Y8JZVjcGB_UYG9yQSSyXNQFii7YY8RFiuH3il4f7a8sos9igCMeRXpcnLo1fFXelUCjC5CoBki26LnWBmBfqCojU03WubXsjuqVz0N-NJpJ_b2IK2vLZWPayCWOW6TXkWzgDQhwe79jdzEnZKPL1KewOdt72ujO0MsfJ3kIBnhpyvlrxURpS80ZJdV1B9UwIWye4ABOAhwK3PdB9wuo8fDC3YEZXxd9PUertOye-Faj8p427UdQgLd1IyVLbUzPU0uLaKmi2eRnPP9wM7Dm57ThUjeLTjoE5uFjA83qWGiSgaRYxbl8eKPSNErmnfW87X67aaZNeE-97HaLKxkK1TGuoDRKfBkJKMx_9hxgJt8wvxYBNF6jkdqeVw4G3ZXDTKPTguBR8WJ4wfdlQRCSvevgJwLTbx2KTdRNO22-hmegEQT9gXFIMf-mRPaOLJJrfzuxsAHdshGvbVu7HTnYCeR3hBf2OV4lUHfStb_uY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=uiv0x1ZT5qu6xoCsP7_37K5wvfz01Di85DorMxBaF3OmMREDQEB-ga3WRcW5SrOVEHoYHroOJ6ARTGjGEYsTv5iEncDtBi24pXU766vbadJnoiAlzWMay1zwCkAK0e8ASo0OEbMVIyjAfu3tfybAVygaWeCuv_84PgVJbvRohR5x8B_LWrZKJyC4tYHOVzNBtH7Y8JZVjcGB_UYG9yQSSyXNQFii7YY8RFiuH3il4f7a8sos9igCMeRXpcnLo1fFXelUCjC5CoBki26LnWBmBfqCojU03WubXsjuqVz0N-NJpJ_b2IK2vLZWPayCWOW6TXkWzgDQhwe79jdzEnZKPL1KewOdt72ujO0MsfJ3kIBnhpyvlrxURpS80ZJdV1B9UwIWye4ABOAhwK3PdB9wuo8fDC3YEZXxd9PUertOye-Faj8p427UdQgLd1IyVLbUzPU0uLaKmi2eRnPP9wM7Dm57ThUjeLTjoE5uFjA83qWGiSgaRYxbl8eKPSNErmnfW87X67aaZNeE-97HaLKxkK1TGuoDRKfBkJKMx_9hxgJt8wvxYBNF6jkdqeVw4G3ZXDTKPTguBR8WJ4wfdlQRCSvevgJwLTbx2KTdRNO22-hmegEQT9gXFIMf-mRPaOLJJrfzuxsAHdshGvbVu7HTnYCeR3hBf2OV4lUHfStb_uY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVIpIcF-YsBtKwnLbcy58f8-i3Kbv0NUo2ExQcdBfNhG0DZqru-us3wkx4vBbvhGBsfVrnE98LMYc_RAz-dKg3TzuBOUdiUqbwGm3yx-Xzy5gZWDYeNnKkidvVOndI3ItCgPDfNEqJeUk8JkEIet3aj0RikapFkzsxRe7EDqHXCSQ4PcozzsZkfVGP0_kwOGqGKFO7KHLObifH2bWvrMY_PBw4Q887BdhCTco4aceidbzEo8J16WeOOnoCPJZAmUH2ML1X7S6jdHMbr_m6bjzO60RqJsG_d-i7f3X9uL4PXo2tenXO5LAe17Wvfm6h6MqElqDNQsXQ9vABExb9daVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJ1KqrdF4wENHZfamlI8AfmgU1DY8pPjD9qveHl3EJALIwSktt0vJUfksA7TAyC50Q2h60HrXNc8wt2FYEX46HScYzhh8eoof3bIJwTOH2EVer0EJKwT4cchdsCG65fj0cc0nHrw2Mxx-2mil7oiVEeKs-CYptu8ooggUrGq0Fy-8ozwCLqcLcM7cJ57MLKhZYhyBwr822uwxXvzqQ5WoB_B8O1rKSPEKB-MFbCPqOktcD1ozm9XVda9h6-mmMx1ijjEptg6eFKaE2yrjDrsYpp-wsu64zfZ2lZ2PYGCoBqQ8a_ttuexxWoOHVft_BvPZu-40XubPec9la0HJfEprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0B4lT6no41uLWzBCi8TOy7GJ4-pZI9AltmYr-xSH1WkxBXsnJzKx6r8D1Xuw77ni09uIQp-Fq_Ngu_bzJcqT4NylltnmkV7HvWqamzrTVHD99eL5qPN7D87cAvJOVJneWoph_5-0gGPFzb0BSY0exs6R756GLpwxdDO-pNpAwvb_n8CFhbkfHrGzuIE2oqFNDLTMMFMu_5CU1qGgpj8Uvbo3y6WbKbKB-KjpuVbEDuckKiIEDyHzPW8vPQTc2Na9nG3fT1Md3JAUVXEvjmPoGDdIfrU-mjw6aSdzuAx95q5QhtsUxb4oiuvgmaR7Cm6Hjumu0-9A_q4uFEs3A95aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy-9rTwy74E2DHTa0yCQsuTaq7ot-neV4KkE6bSgSrI5u_jGFPgeOkm44rSowrcaXZQcBAjmB8vhz5qtM7sBXyC8p5xMdfUYhwbWJC6GahTamkzjAWQUmZBqCPBT3u_wao644uzeHnaMBiBSXxwryL0zdcZhgW_tIvG_BUEuSbveIJDICp8PvYvSlnAH8A_onqkTjauWJRH8O_dK39RTBkouU73M5QglKCxKDpgXAlE-X8KBtxE6F1MKkzkzSlbJdw3DceJT-cWZ04eZjkrchmWgS2S6fayor8ztJTnk8tvYBgb2fO4XyIENJ22JTvL-faSFZ-H3y3QbfqlcLsqcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZBW5aBG3jD1ZdNdXJvcJPlAAMmdAuSmIdot0lWZYkYhWzTnYmLoIdr7SYuCHrndTIGGAJAZaI2ClYPRW6HHWgBLxbGkMntdcEynhbH-wtT1re68C1D9-yKLAvzy8M_r5OI0BRWNjchHk9i1ADlUP6yUh4V8Dhrh9VNkSCaTfkXfUUXILnuc3qFdIOP7ocpa2v00l-gl48Qv2QHSc8CiJrdZxvK5Ln51fOYknw6Zq2WyROFU5EB1sVgtIrwK-l47dTkXgZhtnCG06_XFgyttBpNB9Gu7jYGI7Z0AGBBMTP_kvrppVPnAFEubKjBWgDvs8XbaobxE1vq0NnrrfxmK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvDlkGJtl6-YnQURwbMZd6qCUKfypJCNdpyfOmt_Lk6jVAD6KgL3wglT4ljlNsfo7ImI19ZxYRyfpn_PNhzh9dxJnUk4k2JZxNkf6kfCfDDQw9M3i3hwfTdhaCqgvC2STmPMQHVYL20txpYpE2fPnkKuU7cIR0NbePRBQPr-pCtp0XXiTt3k8KadNyHKTGqdpoUvLkEVjQyx67DsGe8Rey4Ry9GkCnvQChveD7xr_8gp7YYoigU-nN-_4-tS-6uAchaEV7HXu4dhaPDIjdDt_SGQuyyWgH8Hnzgp3SFxXGVyxEDlWLQyCSLXGdXXJK88AXR5PEbV2aONm9Bq7E8vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDCxCkmo7fHOSVlmXEoVvnWLMqiA6_JPCtAcs6-nRnNkzOqCUfjeZs2_GXufZ0lFVu00JuOBW0nabqvhlApymLBW-eCEvAZVvvfMZQu9Omq6-D7nNnZU76RIo7eBUKq9wkqpuJstmSwKCaVUEq8FvDopXh4tUhMSzAxXnrXTy79SZUx4CfSESze7XnC9jfaCytn-F50UjbsxbHbbWY2IJi8HTVSr-Gvkdjl19EdrONPpvnB_gY4aQorvM4qB0NDpneBnwI_vxwJCbofl5IfM53GnpHvQs6GO80PbATmUh8BQAlMnTDhgT7XzYw1DoRa_yiEt1R-7Yn1cH5LGmCsX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV7zXK0iY4TydqEu5k0Am6mTzLXs3UOs8kzzGFi7BRftkJBboDupjdFr3C2CBsSMzJxim7cGurmmySNB2r7RG9dpXpbWSmXxAlAorlogOENvDTqV0K8D144OgA69tJAIZRzJwVrp5-zG_6LkXON5oeDe0_I0EN20-p7JEIlgS6LKI3AB24-Tedt6bvaodrOyiN591s1qKIUKXnfRjjHBavkqM4ZmmKBFK0Tkcrrhe9Dj_JTIWs-dif9zOHo_IcGfTXfnPUg2ovOyyPJkn_eAKCLSmIrOgLl1edVrTZarEg9f0p0QAFoTrh0oMwCRnoWWJ827v9iF4RhnJ794drDkkKic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV7zXK0iY4TydqEu5k0Am6mTzLXs3UOs8kzzGFi7BRftkJBboDupjdFr3C2CBsSMzJxim7cGurmmySNB2r7RG9dpXpbWSmXxAlAorlogOENvDTqV0K8D144OgA69tJAIZRzJwVrp5-zG_6LkXON5oeDe0_I0EN20-p7JEIlgS6LKI3AB24-Tedt6bvaodrOyiN591s1qKIUKXnfRjjHBavkqM4ZmmKBFK0Tkcrrhe9Dj_JTIWs-dif9zOHo_IcGfTXfnPUg2ovOyyPJkn_eAKCLSmIrOgLl1edVrTZarEg9f0p0QAFoTrh0oMwCRnoWWJ827v9iF4RhnJ794drDkkKic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVbKB5IRWwA4enaRtsbU-NSFLGzmmNERCt3THgOtGO-0Zsmo_jwT3L8rEUCVJ_rHcYZP1gCKirraS_1i-6e86RqMfzusTsBIJGQsvkG_ug5BiFQEtcVmRfhfCXVi-6l2x57IDKdOlOpJVKmFgyd_a6N_nXREk4jWD_PSWIsnWwiMLJOeE4JJRm5cMLxo1SvZ74yPzfTwoaprGjOasOBLw5cuhKON4Xy0pQE8UX15cIKIYpbucm3Do_157VIzOs-q1nsvejdFcT7ODbIfhfp0kYw8Z_3GPczCklU12Pg8YkNkkG78BxUXpOAcvpQjJgIqZUn-eXHd3ZpnHaOQShiZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLThSbE2X_BVUk71qFjSivVFtMJTHvSgskdRV24iAjcTw18-3bro2XlE1cD1nUcGhjVl99tig7o3Y2JKW6miuWIAoVecKlYK-6Hqv9Z9rHZbfrqOFevhH6H42m7mrWcPNixs_239oFi5dw74R9Qfbx4vcAaqoTrhPcn02NyFFRpBFmINIuMtQzQV86Y_Yb_eYv-i3uUnDvHIy5PT92BhV4tGDqCX8gwXIZz0I-GWX04xoqMY4pyzFpBONHrxn9L8cCj3MoPwJ56L1FNBfKi3WAwOryhmgVMeHKDqvjagLtuHmL_h21PqsdWb2Ej7-y080ipS-3KgYxECheI3Jf8j-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtJiVNem37YLhktCzWLIbJEiR7JJPZE5ZLhqT0Uj1lyUmJgMzZhTKv3jMp3XxPNZ3MGPdNJHaTYUNgYIhGH-MPjC5iQqym3-yaZnVzxtI7HhX1-ZzFqvkJzF7aMfIP8WdNAlfCZtgxqci62c9nbxqrTh4wJYcGlQHywzEOFM6eIuft3Ndh2AgSZSpShZowX7p776637cT4asvOShwNWU9Dx33diDCb8zWmsStHss73qZRhW-QDTNAnsrDyUep6h83EoiaaP8hIQndC-CwSV4HF3XFUZ4mvIYCfiKNSEnWfrjFSqpdSuyn6aMH3_cGhXsDE86eDrD2WpDJqa-p6hXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=tKHRfNp-j81J0oIqW4QW3Og8VDK8bVuYLc9XeeQoSxcE_YGZb_-5MIlssD-QqzqNvyHRIGWLAFyVS0eZMaH11yQy_kBYAklRBet4VdcJpOMR1t3iWkMhlek46pxmqbI6zMn8uDoekZWzWq386kZDwA30JpDjeXRTVrzeMomuK8NQQi0JhD0ytiQMXUBDHIqccfNCy7sOYCZ_8w01-5Dj9dULCIRNM0-PHZPUCv55qdBmOwjPyCBZf-o1pA2Bw-xqLVK3o5BTO_UoBVAG2hClcIsW0fIPi-sJEgYo3YAeSzFby_HihJL0SPmebJ9SGYNvP-0BwQDNKXPaBjmHz8FiJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=tKHRfNp-j81J0oIqW4QW3Og8VDK8bVuYLc9XeeQoSxcE_YGZb_-5MIlssD-QqzqNvyHRIGWLAFyVS0eZMaH11yQy_kBYAklRBet4VdcJpOMR1t3iWkMhlek46pxmqbI6zMn8uDoekZWzWq386kZDwA30JpDjeXRTVrzeMomuK8NQQi0JhD0ytiQMXUBDHIqccfNCy7sOYCZ_8w01-5Dj9dULCIRNM0-PHZPUCv55qdBmOwjPyCBZf-o1pA2Bw-xqLVK3o5BTO_UoBVAG2hClcIsW0fIPi-sJEgYo3YAeSzFby_HihJL0SPmebJ9SGYNvP-0BwQDNKXPaBjmHz8FiJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrChcAb-lWq3tNeSQsBQyKo3UaeNnL7mYK_7XSnCwKgcVvZeecrlQYBOV_ktoknMkFGt7TTwK9ciCxL-qssH94q2jyt3h0FTTzJXgEtJd7P4TpWqh0DjCYukGYBRXT7gtI2PA5w_mtdTkXggCEb5ndzVYFvOeF-natK4pEW6-sv6q7EHABxP7tue613bgL2duJExrSQvW-VxkQYZeFNJ-KW50ZaTIXcuIRyyRh60KPpisEBERsId29ZGrQgF9jvMVCMWTz8N6Dr0ZaJ63dGduto9IsHOnySpQhRiwAvSMYEAs5Nr4EUD-ZUBfRC7Z8kM_DJUu_1-JTo-T2kkIJu6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxW35w7My5sFgkVz8WlwBcdzGme99H1cFF9iKr8JY5n6S7x3QkzA-DGmYYa4jU_JZ6ihO5Z-zo2rG4mnoJE3QBNgyX4OIkAUmV_vzlyYEnTSiTb0mhSxcwTkrmaHHGQEN1v5Edbz5ZtQWbzyd79zeQjGf4NpB78vuU1DJzB4LK9ZcLagKZLT1d7wHslcjLfMK0ghWdDCn4KUewt5jlzvhmfmtXY1_iUPLPVKLrHG9zS_6FlTb_5qI3PctC92NpAUt3FoSNOfXl5QtO6KnzLC8OTuu_roQrk88IgnnQXF4FMJBIqtraeamCYb9yAQ4UzMBdPL07F_p7L6GN34PkLgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGJ_3Q5HyM2bvPy3I0KxHasCfRse9pgc5MzR4QasJLzlC5nwD-hzC6wxVrMweHcR3I_8KhoAAghp5Uhqqn7-BqX4caFaCj231egNGouyHm9xnRVIQ2F6ql_o5NI1LjXybHvlsJVlgJ3Y9fcaR7frs0XkGbHGgFVEo39Y0VWtfT1HtnIQbBFZUlzqR9V81ohRJ1xNznTyXkgtue1Tl8kk2Gp0ElDoJFiFh-jG9pNH4fvIVPhjzlZB0GxH8x7wxMhS1UhIsZqn40Fppv_fvw-VHq-PtMQ7wty1Pz620ctp7KLdtRdQoHqizgGn-U-xdB9H4ewJ-v5DQG1wlcZENRyziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt4sPDjkmWvTXGYasFTipDzdqLVXX-Gjp-WIkVPemy-FajFexOKOerxuelFieps0v3ff5oZdOZ5rB8t74tMEWfyHz00_wH-JCCL9qOwbTW8hdUcvIo-tT9CaWHNgdJFuDRr9kXXz5zTRG1y0HY4MsljHMdtVDL2v7Texz8KjEa4F3JzRfrSgxSzKJdbAUDD6hT--ITOUq5m7fdYNA_EUWvD_qxyUuc57q8EF-vRSO4LqNata7UOWpjc-taNIro0WwsCwacEVCIaFAmG6WiP7Fd2BkiDLirzDRNakLj7DuYtXcsHGz90v0MNGYqs9D31mGYzA_GcRy2H1MeeJAFYAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsQOSa2reUldnBBItv9RLN_l-uJFW3XeQzKW915aGBvVVK3r5DS2XrQDjNvMOqy-0lNUyITDvZ_35ik1mqQZpoJyvZNja19XEitYfpqKkRbVytgHeEWWClMWJwkvJnf-kyW1ALshzz8uvs8SrFxTghi-WjhfM5sfozVcsqueTZ_LvPQU784alLhUIsM_yXyGdeGtVQKIqFyyKHKpTyp_gfd6eVEjF6yElj-zJfDMZTJFL5BMSbn-ra8IlxKFPEUgoXb1C_jRpDgEZw2uPq0KWhPrcV7p6TC31NnSnzV_kPMfNRO2zL4gAR2xAvyzEpURJ0EDB1f_wr-Mm9gZTCz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcjgbdWLOAkhHHe22J7ghAyZ9ewzGQ8HWk3pWu_FnEjGSH-W0begY-fDg5_ZOS1NUNlWWe-awQb-lpUr31qEEERcOUl94py8POxb82T9ruRoNtqWuRgfvO3PfqK7yjTpXbWCA2jzb7AGmK3lRkYgVlIOilNOOSjJk3_ds3ReaH8oaGUqe2Eg1pfCsrJdvlu8aKkLJnNFozzRFL0wM1VVe6ePcIX-yPj1FNojxSGxj8aYVP9gbsaJyqAy820J1TWRduBtrTSDWknM43wo3GkKink84JrXykOusgxHa_bykJpS40I7iBPch4WkRpGLZw-hQUXszLXrjZW0qdVm-hthGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmgO3nSxEpi6l_nOemmhZ5xM0EXY1CwD1AgAyW9qqDrywIeXeOztwiyEki1U0Sbv_8-5y7KBuYmG3Bfii5PBRiu0-3viL_w1uJB3LoeftLy5UU_Y-H49nm9jr8J0zi2AcyE9kmcPfOTAGq6LHwGE6JXm5D9OrkwUq-uDR_xFPeY_0lyZQBe1n8EYv_3MML0mL71K5LSXMgEulISL3y2wM2CoLmwrorG_F6RpHV5IUUrUx-yG5NpX9zUu-KYCyI-hdGMPt_8Cb5ft86qnvC0iAl2T_65fv7WPtk393jpBRBDUO7VVPUO5bwOMk4SduwAo-h5tecJtvWmiiWjH0fJjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9iPRLlYzi-QETEhfDzP0h9J-M9OZtTU60-JAXFtVTQGf3CRWVNOIgJC9tFrkTbdU8gm3TK6mUtmrrKlzLS1qD99rbkQhelznwU-vFdAq1vSZOCypQY6YuSnADa9dzFpGv-uKPCd0gKf5i1plaEfwOV9h-9PgPDRmS0ngcUsRQQq2YOa6R-OyNu6lfMFSIo8d3-nWu_fO0vRIVTb-HHpKpu_Po80uuNYA9smq-rzlpcgD5Plpk0kCQAXX2IKRZHk64WecICfnPmYM5K_Eog0DomftA5KBS2q2xK3Dfn83Jh7-CMsz1aFh56792CWLiQEH5FqEhzeg66hOOMtIOa83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nda2nFxB6v1Q9ZEhAKd6SYrgT9oV62db4RRvpaNfYCF1SBvOiFtkLmEzA7jbWmUNbTc47SaDGl0sVKrXV4cQVlErsSSXvl26RVIVG5qHDnmAWGDJRx-zpGTeoJOGZZj8ptUA-Ee41GGdrL7UYUZFfrxj-THxFoDEgeH8zOIn0sNnK264aYMfECCRbNn_mO4WWeOSrvPS0I3vi91tF6QoSqU-bcwhPAUV-4KYnAl5aTfcWIqw8I3GMJzyXNR8tiaV5A3oOw-00kbKrJD3BF5ZSaIJEz0MxbN7I4YBsTl_laCNGDyNpsvgy8icA999dVgX6D23LJZcCgvfwZwSY5WU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nda2nFxB6v1Q9ZEhAKd6SYrgT9oV62db4RRvpaNfYCF1SBvOiFtkLmEzA7jbWmUNbTc47SaDGl0sVKrXV4cQVlErsSSXvl26RVIVG5qHDnmAWGDJRx-zpGTeoJOGZZj8ptUA-Ee41GGdrL7UYUZFfrxj-THxFoDEgeH8zOIn0sNnK264aYMfECCRbNn_mO4WWeOSrvPS0I3vi91tF6QoSqU-bcwhPAUV-4KYnAl5aTfcWIqw8I3GMJzyXNR8tiaV5A3oOw-00kbKrJD3BF5ZSaIJEz0MxbN7I4YBsTl_laCNGDyNpsvgy8icA999dVgX6D23LJZcCgvfwZwSY5WU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H34dB17LZRMtgJJsPxb4cSoSoAXHXMqGS5_jYbtvD3G7B1SF9rWk2u13P5EEPkLIEd1Ad1uBV4gkWvtbXvIpYnV9wJNCTMGLqRsuO0T8AnBLCG-vfbm-NvoIWXyVeo6r2V2bbBZH0hxQKTyVbFPTNUKvMyfed7mo7vk62o_8mdRmmtljSXKrnb6SbScshAvOzJfzM4dtUgAgWTDNdtQ-i__lZZSIwnqxTlkftiQel1OssLrB3ic-kWKbczsOdDNzq1xKuRgD-rs-zkZlh4fo_VoOWOPCbpnfEj3zUf44xwmwVSdZq-nTE32x4-L-V0phhL93MwCWjGrW1dBA8UFQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkIiz6Dap-Y67IOkmsNeNUwVvJ6S_HCr9_zFu2G6coKCBOSpu_0Ne--cG0hZPuUA0zTIMPSadO6gYQ-xd_lowBagk8ff-lALNTfIhMi_tVVl6d-Oh0xEFUVmVFit-Bfol1U4NNBRYm6WK7XvQXA1K9jBdODKS9dVPOo8L1No9xJEP24LXLNhDEiD8wt7yzbgQZKjli_4742fzqGjCb2q7CAwQvxBoUVEhE_XRXzJXlCzRp9YUj-tqcA22KL0JScDqPDdqEjvfY9khqvb4mcC5WJY8qSCJp58rN-5-h7MIvZn8wL6Khmoc0dJkt2vqwv3pMtcl59JtOgJAL_MUnkvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaBcSCC_OKpiCQ7S_FQmZaRayto8nB1NU3_jL2cbliKfZAtgVEblf1IoMYna1xF9w0jX2h6VcKw6_ChJOLFQDuXhmV7zpiE1qGAICw7Zu59YfUOoKYLOtjRAAYxwkhITY83moP51GFavGk4IO-EkX-Ffd0KK0D0zY3FTz0ugFIctA77aOejgYxRlnak8MR88wAniayzUVpAbEKqrCMTkv5gCAVbXbIpQXCXi-t2ihiHNw7gevs2HyTyN7cshFVL88hnhYT53B5i8f4P7HNPZYyNYA0r_0XN56WMpUyrB3GBIT0o0pwFsjb0uQjtp2lk8yPm9p0jKuTKXybb6ZO_JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIFKKzszAym6V65VTlw1mVk0qPP5yKKClEYjOhtU5jYMfC5Dy9939HKzqIDQcGrRgSWx0iJymLjObQ10CCgoahG804xcwCfwOsFy40zf7KncSekPwuOi4Y-75sqKCuyLM6o1496e64duVwqqpgxMzbP32K7N9rK79sqhj0pz2Vh-UIapYa9h4rJfeP8bojzvf-QwwzEaicXIbk4zg0ztHPaXVmntfHCobH8PTgw6h_gfTpdj1TZlP9z5jk1CWuVvAf1Htz-qp1ixA9irTayTNx_AfE-BnQAZMzFoZIOSQUkWLL0Q_WBQW4M2qT4NvVl9hJm3pYKAnVWdZCnULvVUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=gOhUeCbjYWjAyIsUVbL7f2AXPAMP339X-k5635Hh7AW_hIwIQDFHNvTV7VcnRA6Flsr0TWSVtKHTJBLepMSC2Exa-OnGNq68jDHu9j0meVFNg02xnzMPHDsZ0v64Afv_olM8pJLuNW7R6ul9_NkkNnSSTeFaFKQLnjimKGR9S2a2PD-cZT5pBJ7LMI2J1HIDPo7vV-y5TSknDWlL2VZiNLAMNUbmh4FQSIv3RUjy5vV5fjKZM1ywJfciV9mBN7F0HiXpuQKmufNkVmE4v6SALrUxoOCv0NMHGaPP7RwgmMMZfmvPyDdThXUDjjN27PLdzVKV1ceSKf1qW5j1x049lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=gOhUeCbjYWjAyIsUVbL7f2AXPAMP339X-k5635Hh7AW_hIwIQDFHNvTV7VcnRA6Flsr0TWSVtKHTJBLepMSC2Exa-OnGNq68jDHu9j0meVFNg02xnzMPHDsZ0v64Afv_olM8pJLuNW7R6ul9_NkkNnSSTeFaFKQLnjimKGR9S2a2PD-cZT5pBJ7LMI2J1HIDPo7vV-y5TSknDWlL2VZiNLAMNUbmh4FQSIv3RUjy5vV5fjKZM1ywJfciV9mBN7F0HiXpuQKmufNkVmE4v6SALrUxoOCv0NMHGaPP7RwgmMMZfmvPyDdThXUDjjN27PLdzVKV1ceSKf1qW5j1x049lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXeG1Ad8Vq_9DnCdCv1SmXTULm47SSKBFAieKCDb9_M-mCTdmTvffh_opgxYGJAeKDfZV-bk3dt6lg1n0usW7iOFvvLjdB2rshaXFuSgHtmvsMvCrkl2wITcjfRhtGc_IIg3jDxI-GpwqiiuF7lkHux0e0igJAMheG-ZcK-13_OoaGM72UMVopaUxJ19_wiWD_AHkU8XxPs20ACbHFBaK9Ma3HpEWDcmf-ZdLrxWegqYqByYPWgFCEb2nukyq9CJfcVjvz8xGMzeU6lWXotPtGWUX9u3_2ipMBK2TF9RDwqbLFyFxGzy6lNp16UcdZgWwgI-7MfwvabzWCwV0ueg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIgUwFjNYvQjNPY8Ehqt39HtgVsz4hQsEeBHk956q4xGfVbkSmbczX2TLP3DWxFB6v92IaDBIyh0QB6nAO3Knhpp-3plyXie97D9cGYYF4jpBMhDA4WQFBnVh9pCmPI-rxegjifzcCAHtIlTJfnk4faYJBHNX_ZoJjHKcOnsaJneD0a3Afhp4-ndpQf4l1_ZahAa2MNUb6ycXvwxBDoJOisCIEMeLDooq_62rJFJoeVLHMMLb5f2k6Bu0DHUWu4v_S0txVy6vwwGwznWRT3B_XgYaej5KzFT-MZAXtoFtvOtqQD73gtNAtCuM8zP0MFuvqBn1uGl3z93LVPz6oD3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XwSENMLQ0CnkJ8M6QHR7t_jpAFYQZWSv9b_KxEBFtCU3frvBx7dqwbmXfemgmxfHF0uwbnQNl3A-Yhqjn5an_a2EP14yce-NqCQ04h463cGBkZO9ESTWP3GvGV7yPdMz25nVzhHhNKBI-npZrqyyroNkxySIntl0xk32s1DMonLA-BQgH3qxdH3Lv5Oh3mwAbDnfF8b3CSkJiWAlUK6cH7YLVRU7b5lRrv37Cq9tbtet2ebvzv8gkmf0sn16J2Bt-MHiQ4P2CkE-QWgNFOTK-QjNimIugsWw63CNPJ3AyNx7ZqcX5lONKNkytvxqXlpCU7m6agDzlHicyWpgcDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJvh4kbUTklOnmaJ4OJNzMp1he3LT1iDpGXfM8ieTQx3Vx1zvoim2CZU5jj4ECk1BziWk_C5-ItXQW_FJokALlzfnVXPbG5N8-R88Q242iILybF71Ditb7oh7cBxj8bbb7G2GjpT6fiDqtP-aIwMAYZK5IDlwNTh9udDypMzHiky67ibTrwOOSaLTfKs8veNABBTpujG6UWyTBHMTixRnVQd9wIXFQACm6esYftIiwAb0R8swTdxOXWuX2zqr-WNsPuXuybqr_p0aFbUompOHm0NtWIJWc-nSW8FQ6-2Yr-ThygZv2-T3uCmeJw72ykhB-yqko29b9aMaBiiQPEY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6-P3bniim6QpP_V3DkJgyPS6YwY89tAlb7Yjko1gyrdifqw3E0K65kJpUbTWhxadynPLiFpsTlsWgApzgm4LEoo_VLO4x0qEIFCtUYbg71zHPRg5pncLhb8Rolw4iASfZBhKy2MPNIOazycplLVeAhzMSBtBMLaI1ci2TQuP3aHQ5a9WniMtqVsuDjPW5AkcyqoSh9Sk2Gp0Lu431thIT1ganrLzz-4wTC6zo-SJAlbrNBON7jeHfpHkmT_c-eCcNMxWr7Z7eFG4BVbFSrqlgeDmzj0YQwAFG7CmSCchcesnhdElnfi_2FiCKauiZJxizvUWj3n7CVexC122cS0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Haa1X6nrSTAACxAuTmFv3prI8MBb-P0NM7uHP5cbVeMfG3SiVnuSlMKsXdSLgwjT6IetVU_JA_wPtEHmCxUYgE3k1CMmHda0GJ2ZsvD9vxz85DIRZt9UccHiRzQIW5laHwD6O9N8Ipn1SxLpxX5wHwbVnHDr9X_ii6t_6c_VPHKrKZ4smS4F0xPj6SYo18kqqzbCAg_HOJXi_8bAlzDQR-nM32vtS_3eHT2LIFR5KSNA2HulVMyhvNL9BCesLJYhl4bKkmDb1L7c5Jtt8tGl6hWsHJDSOq_mMGw19MZHEzveNy-17RAC-AZf-sAuOj0c8Ctl_X_4zqaMP7hlZf7FcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG8kfvLGbDpV0BXWvjhGjD8QIGuikyHLX5VhqrLKBZiOe3GexmEHcDzuicZynJab1kON8-DXvhLPi7vaT1fOyWLAwjVEFxcNLn8skUL7evzLtPxASchAibkNiLGxTNe_TtJbP0ofaj2COTxtwWHI43enD3CZ_i4V2UYdxNLcXIhyBKMi0sVGoXwBoeTT_-YDaSJ2Ccc5Qv7Udw7zuEdwTPVx55Ama9dHGyBYtrtYTFRsaSRI9On92mLRtqr9XOPkiDdCw3UtdYBgjMnb2eZFDUB8kB0gc7EmRTyJ8dYLpi-6tJGSlXw8WuxqnteWKwlpJvi5iG0jR3-SW-2PctRmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibWIlAgDoQ82pyMiGBWmkXisEYmFyYw09CLigcbWOGRxmuiQ9yqzkeGJaN0YCecaGhU4HSb4jXkURe4f5Uiwm-1eVhIG6D5LDu_Kki31h0kTCPyufwNAxLmtwN-2lKxL37vCQL0nLpJwHWa5eMWY7N2OEOVUeEkRBfSfcl9FIQQ3OHIBw-bqjIgTpiQvcOOIWOZrTpx863os3WCzpz434uyJ915UhyTLywNmsWeoMayATl6TlW_mH6MUU1MTHc2ocP3_j7AliYBa5MoT12JbFKNTXG3kCsBheVVNNSCx_0HhAd6wROTNfG0fsBjw-4w4Ekby7vu5ON46idghLcc2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=GWomWpo23WqYieQJoS9i0HUKgKFXUMIhch5QEvUt1DoAVFbH0m1weYZ71HAyAQumZW4O8UkbMStrpLVxD7B0lN603l34KYxwyBn6BCXCGwCf2nhL-Pf-qdIexVTQKNdco1N66gxf-QfibMUiU8aoiLSglx2EVqoacDy1Du6MTDUxc2GdILevnnz8o6ZqZtG56axRvlTmOTA4IzZLrE1vCS3Jn7atzxtaHougA7Zn0sD1hTYnxJyRYpuxoq1e104Oz3AWIfolLVNWFjGdoDbFRVLt2BATrOeeaigKmWPYw_IVJ5lu7ovRRMf6mhOqdBQP-Y8i5_YzasOz82Ooldev0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=GWomWpo23WqYieQJoS9i0HUKgKFXUMIhch5QEvUt1DoAVFbH0m1weYZ71HAyAQumZW4O8UkbMStrpLVxD7B0lN603l34KYxwyBn6BCXCGwCf2nhL-Pf-qdIexVTQKNdco1N66gxf-QfibMUiU8aoiLSglx2EVqoacDy1Du6MTDUxc2GdILevnnz8o6ZqZtG56axRvlTmOTA4IzZLrE1vCS3Jn7atzxtaHougA7Zn0sD1hTYnxJyRYpuxoq1e104Oz3AWIfolLVNWFjGdoDbFRVLt2BATrOeeaigKmWPYw_IVJ5lu7ovRRMf6mhOqdBQP-Y8i5_YzasOz82Ooldev0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=XPurhBYqnTOA6NroVvMznMRGKRSzLSNFcV8FNY61lXqqdOTkeHQfbqLOn3IvnFm7xUGWAu4GKK2e5O1k8J9VqrrGKiq_fHI2DRHRrhrijDbvjKSb5WySsmSm10ZoRsRg1CAY8ujvtJluttkRYE3050zvoJkebV1mWY8czE2lTKhg0CQZ5jY6yHdFnqXzAGwITq2L-IFmxcp9qVdnRwbY3D77C3FgXpOcX6IP7pp_3iQf8A0F7OYzBMSkeSgVVqym2FPqnnKpgJPyNsVgvuDBov3fnKYuVxc0091iR81-M3iMdgYDsD7ppdbJjjqBFPmnMv_pLbF0MuiVy1pLzxvNswR9hIMfWL52gRd9mg0VuX-GRK0LVQNw5oADKWJagBKFV93Vr51j7ndPdvBM7JrBb8s5tIy5p7EWf73NZVE2dk8Y_ML3aQsgRgPbj0zMffi5JDYL54KzILaCZMBGK4q8ys5QnzAutjlcQ53wo6PpaN35bHqRz6nWaUjOeTDB95wRz2p86QM04yQmttPfJPoBhoUGcuIGHceD5cVcoLprvKKkj2LqW5Y_Cw1qbTn1Par7FIOnVUHFyHay4GGeo2EZBClhQw4CO8Qi4XaBEuGWkVJc4dk8oUqfQuW5XKfAZSpbCAZGTJ2-e_I3bdIzFdiLrjDUtYabLS3cnk6y3NAC1ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=XPurhBYqnTOA6NroVvMznMRGKRSzLSNFcV8FNY61lXqqdOTkeHQfbqLOn3IvnFm7xUGWAu4GKK2e5O1k8J9VqrrGKiq_fHI2DRHRrhrijDbvjKSb5WySsmSm10ZoRsRg1CAY8ujvtJluttkRYE3050zvoJkebV1mWY8czE2lTKhg0CQZ5jY6yHdFnqXzAGwITq2L-IFmxcp9qVdnRwbY3D77C3FgXpOcX6IP7pp_3iQf8A0F7OYzBMSkeSgVVqym2FPqnnKpgJPyNsVgvuDBov3fnKYuVxc0091iR81-M3iMdgYDsD7ppdbJjjqBFPmnMv_pLbF0MuiVy1pLzxvNswR9hIMfWL52gRd9mg0VuX-GRK0LVQNw5oADKWJagBKFV93Vr51j7ndPdvBM7JrBb8s5tIy5p7EWf73NZVE2dk8Y_ML3aQsgRgPbj0zMffi5JDYL54KzILaCZMBGK4q8ys5QnzAutjlcQ53wo6PpaN35bHqRz6nWaUjOeTDB95wRz2p86QM04yQmttPfJPoBhoUGcuIGHceD5cVcoLprvKKkj2LqW5Y_Cw1qbTn1Par7FIOnVUHFyHay4GGeo2EZBClhQw4CO8Qi4XaBEuGWkVJc4dk8oUqfQuW5XKfAZSpbCAZGTJ2-e_I3bdIzFdiLrjDUtYabLS3cnk6y3NAC1ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=nmXQOhYZLcSjvs_wDA89-ypv0WHIMjJsLRhchm2UxqAzc-LGF-rfpdwQY4ziKAmesbWtLPMNbedzUF0zlBw_yzHcHAdM8mLcKdydkgYenK7XHqheO9fgf_tOSDyoqGfnfZKDMUlTgWjvX_vY-mgQc98A_U6J_U0IEfgJc_y8hITD9DSaazet9MUctKAUweZoTqeBxhdBptYjUGdznnWH30shR4g6lXJFDKwWuu8aBecFYu-zlCvx2aDDVjp_bdYL_VCDHySHCEndpD701ZSxgrX3llJ61yKfqZoiNODM0LQQ2AoQa2w2kEEhMMqrqXhgMKxU1fiL00trZ8HcpQzZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=nmXQOhYZLcSjvs_wDA89-ypv0WHIMjJsLRhchm2UxqAzc-LGF-rfpdwQY4ziKAmesbWtLPMNbedzUF0zlBw_yzHcHAdM8mLcKdydkgYenK7XHqheO9fgf_tOSDyoqGfnfZKDMUlTgWjvX_vY-mgQc98A_U6J_U0IEfgJc_y8hITD9DSaazet9MUctKAUweZoTqeBxhdBptYjUGdznnWH30shR4g6lXJFDKwWuu8aBecFYu-zlCvx2aDDVjp_bdYL_VCDHySHCEndpD701ZSxgrX3llJ61yKfqZoiNODM0LQQ2AoQa2w2kEEhMMqrqXhgMKxU1fiL00trZ8HcpQzZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7gcZZQYfBH1uH8NfWRwHPLtntvAhbTyUg2QiMuh5XjAqlZzbEn-TZCoQm5le82RCfLH5cgOb8dYxc2szZH-9Xce6ZWC9Dexk80WsgMBazocF5hZZmD6i8qWhbUXXlxFzfvkWOJcDHOC1w_Be3B1BRvrJs6FFzJcCPXfc7rDgDWkjLpB-dr1ARlUHQBcZfYfr78l_vNEvJSFAPsBxfLls5b8Vrs-pgcHBrMi5MKTbkFw3Qv4rxLF5VaSuPhdYRogCEYTnzBewxgWse7uUPLaGr01f3Y1FTyEtaUxDmOtr1CkNvcT0A4FXWYczuWxMC5RDtgnmsxx_Ia4OeV7HkgcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW6g_aEwwKkjfs6UFUsQPS9ElWm1Qw-hmlU9yMbDhIMWYtRbev_nnFInSeOaEDEGqBWIE61cMleIpzVzZqQq6jmQKhdRFtcMMjHPGLe-eiXNYP-C9VpdnGoWc9McPWJzwIx6h4Mkoy1fQmhhuwOdE3vMN57db4h-7t2M8w28ROW4JM5ABBOW_7nL1YPSO3hZbPe2VPwl_q17toZupgEUEc8Mll4X-JRVGgfa7BqkVSIbDP07jWZ2lmk8bOlwBiovJaa8IcWk-77gHAfzoaUDorExAYbIdd8C_Spc6z2mx7kcesbDPARMO18pQgbiasdPC7O1GK7XskR-ZB9HjfVy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=lznMdviZv9o8_xT_VLTav6BpDnDQ6QdZVd1Bz5iv1pubiRey9sGlPhNANW-5C2r-BgX4Sqntnk9BKO1S_ku1C_49Kx4GnvrRvYrwdeRcbuJxZS0Q2TJx0gKPB8SQQlNSS3qEpYmUN4qXTMq_Q2td8QgVQ2u2AO0SLfJ2uGfW5pLN2SzkxbcpRb7rwHs11yfE4S5iTR36NKjNGTCLMlAydifmpw5aYaEkPKdYQWNlioFDuFJGLmxrXFJ4qmyb_aMeEF4W7vJn9NifeN2IHyHME6VuC1h0Hluuhke4t6w6ysec4bQ4nYNYCTREJ9W9JpxJANLLRLeP8v4YJ8D5RHELZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=lznMdviZv9o8_xT_VLTav6BpDnDQ6QdZVd1Bz5iv1pubiRey9sGlPhNANW-5C2r-BgX4Sqntnk9BKO1S_ku1C_49Kx4GnvrRvYrwdeRcbuJxZS0Q2TJx0gKPB8SQQlNSS3qEpYmUN4qXTMq_Q2td8QgVQ2u2AO0SLfJ2uGfW5pLN2SzkxbcpRb7rwHs11yfE4S5iTR36NKjNGTCLMlAydifmpw5aYaEkPKdYQWNlioFDuFJGLmxrXFJ4qmyb_aMeEF4W7vJn9NifeN2IHyHME6VuC1h0Hluuhke4t6w6ysec4bQ4nYNYCTREJ9W9JpxJANLLRLeP8v4YJ8D5RHELZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icTLAeOUXfIpvs2pePYAIrXKwFkTcGL6LK5quq1N0lRe4UK8Y2e_tABXXE9eHijyc0hqHbRuEfRa1tx5cYDuifN-ubyIliKDuk3xqGziALFr2AP8LugT32bPWZmzbdWaLa-69pLzVIPqShjda1UIORBp9YndQ_MpBCjVh0VNDTzpVqa6SL1VO9FoIaWW6bvgKytij8_qv45a7m53G5ZOjozf-BBo4OKoeEHpvOM0nUSek5y5RvsXBfgIvAWJQbgJrZvBL38aazq4yUDaWkWYxhtwzulcW6hEOf8fEc6skjw-wPvl_cde9L0zCEIFeEkyefnqisN1NpdhIHwslfsH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlhuMx251g2mdbHIxOgY23qxotGhXuanqO8vwvt3kvq_9M20F18mo-Tr7CZrn9TBXQVfftm_dHssJ4uaFEHqKM0jfwWVvgfqp2QRyt7h6mgtUnggrWOXfI-ECmPM4WPxgyIVbIYRoQj_5hSOrEDuAFdPABQAxSkIerMc45_2XfUJ9EUcQl9RDLgFMJlzjZrVFW_M6-23ihZa_qSQZhSzn7IH8YondLTyKZKwJuZZ9oa4V_qIdqYh3P7XalNl6xBd1FGPpKQet4nuFdVBRenzg0Mx2xHKVXhJkKdVxK1WpAdbRmimR_DPZd7QT5oCMqCfAzJUwbWURTvKKmKclQ1QWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiscRqgt0gn1KMdZUIRXtuC8st2mm3Ev3R7om5IdY-8pTNhzgUdARy_ynDFUvm497Raov6S6HF2d6Z2IHhhL-hmwAL-CPbdDeL761RP_WjZZy2_OBsHGtEGUFdZzyft-fxw_Ng2qXU5JUBLsgrQj5W4-Y-vOvIDL3J_3hNsbFeynp6YlHoHN7GJoBd2hXKMW_BzdjpXl6496cM-eAnrmRPAQxLngPgR5pCfBhsGgJhsAshGCf3Hy0lgg-_Nty39QgobTxp8jh4lX7ZFF3v57ogvIOtk5WM874ML8K4ITO5O64wQ_3MSnJEWtIImeylIeSUYOdy46VENivMAaF5vC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls7TQ9bhpt3-468BvuCtAYWjuG1kAnLFmx4BT74bPIUGe7e4musNFKl39kQjmmcPwxhmBBDwgug0zb76iWt20_krNeBdcRDgEOdreymTW5lx_0x7SFG4ps5oBDbnNvg7tDT2jV_Bi2m9iupsDR0Yi3hH75Ae1nKEeyCw_uMM5sLgSuRNNJoYlkFmd6fOekphDbKKRHgCxkImDjhC9F56Pu2MbYDrS91NBmC1-KtcZocQVgS-JUfvXwWcyoVcDNkz1wSWdSEJG6scHvUlCz6L8dE8bB2239J9lLQS9GKYpAcre9zYO7NxaNT_aEEbncrq5Exym2fqZWQJ9GvmmYeB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8zCU1qaA5o39OKNr01bjBr5OJrx8l3rnqDtXpe6EAHSPAFajHapVinSO5A1LiyMG_DGGqPLvYFf-qvR98pECSQxC2dwLig-cL18pMe0QzY90oVm8_AayeRalJQrG2u7DBI3fNo_OZuSiuHjIOWPxi_Foo29AZM_wnriahe9bt5iRqXUOdwdiGXHa34SZ_c1BZWekS7vu_0vKmZwe7LYsEDnFfccQriKI-Bvh6k2uM8b9gyxwrxzyAm8uUrruNPRsRp-s30ELDdQmI1USO5Z0mxaxJHvI9tWPajr7Ixp2J2TLjHREUkXsG9zEQnIctjdxIltjpr5NkzA1J1N7SECnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyF2Qo7s1ey49aIE_6eRMIddvL_Pu-iEWxwSBCBNTsJKhp5EhKpsZ496Fk5dkCsjYVpJEgiRxooMjW1aUHcxZkXfOU0lAno4oZbvvOj77wFjBc_zr4Eb5EG9LdVy9ReeAnRsEAipL8nlKMYtPQQuLN6UNZ0dCWrkec-POlgEKQ5p13kFydfWLXIFFQ4LCi2MsnUCdS-ZnBaYw1L2xvjy7w1drlZOcLzVwPwq7E8o7fyHV4RMCBhcfZirWOc774M3jq2WVqFYAjqOFmGvXC5u2KVLKXnB02UcdZVPyJSq6IOWMGEtgTNFQAM3JQUwP4QlBhjmeKFvRrSe4rI1ZrYXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeVVJKZdLDFQdUnDIugEfVSRiVzlGhLMV4T2OO99vNopAXhrSiCJ0pf_8WFUaOz6SVvEgdBkZK9OlOO1L7xaaJhk0JzwvSB_58M60w9BHgNnwKJZkVOXRWUNn51CMxP39SfntQy1kfwfbzw3wy12zXBr7lXXNdw-4d2lWU7ML5ku-uR4SojvrxspLVp-Q0jFEeN0KoFyLevcDPA90iwHP1_RIKJyfEc9L1w1ZJ9HIK-s69wQ3YIXRdJylx8B4JrrBIbt6ndHl2QYAqMNpHNR258gDGXBNwobRlmyrHhezUpIOaHlbuwCeigV58UOY6cWy3NSnjr06j9c8H803gFWeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiDJ_tJby8S6B6GsDZ_u6Pxbw2mJLyprxtCDBavAevEz3jSvVdSBag7tpw9saPTnK__l67gRZZlauekcmWDOAmEJ-h1vZIU577hzHMqpz3OXCLNvlRvjuO7qZXkt9N2kxIemy6u2gp9uSe3PfMqAGMeBESdRDaI6YjMq_8TYeDZfvgCnk2St9h-xp-B259hhzPSZctAGPeBpoItGYhmJVdU5Yecs8yXwN0tNWdcRpu4dFiqvdtwP51WdJayCuWJkdc9IWKHql8GKOgBR8qPsPuFQsg2mMbW3kj1t1IzsNzoZw8Z-72hBFi3v8O3rshFjQPEv9CLXfKXwe4WLTOx8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn_KDuuk60INS3vjKcNa4DK_i2ZeGrnub_n2Rd_S6oS2YWcQUDylEI3HOciZDey5VUYusWuCDc_NPKyMsJIv4gtR6J9I7c5onIZu04AZTdIUxQwfcbL1P_S6L6oiI0qKD-97VrAYRX7VrgtrflGiINn4HJhj4YDAbwO8n7qudbuODGKFPPm_AMgMeIQWK12RBUPeVap4OmAfePNQsjS-U5iW5_kj0lShZuvUCY5LMUGKeo4CVtU4d9ItZf2yef0sBBW51yVLIRU-T67KUpN1kKPYKLTPRSZWV-auMXrUuaWTupdLq3ROM2lJiE_43UMH21zqYtMEfDQN7pCkknL1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=YgXsdxms8oISjqHF-qwv6HgAuKvLrS7R7GxiKGa_fWqNG4uGGqu1rBryMlnwifvH7jZafobBSNiHcjYshARCEydMMKWE5Zbvup5c-NlsCy_5NJWGWkFmT_SN0Xz5Lea7bnkQArhBmLy0_cXWakZiroxPB8hZk-InvBni9tVht8bAPvwU2-EhurBQnpXDBdfDpJWWFp7AS95azQ2ij_ZkMDFaF6xlabZsYjoQGC9uK5O92DONW4khmSVa_ed2ZwdEp8IkrI3cH131qOr_5ErBTLhN-ZS4nEKu-dPkEEQEHr2Dx2Nq-Zxpwwov3ysErAXtj92bqkvPVIl1HTHGcL1n1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=YgXsdxms8oISjqHF-qwv6HgAuKvLrS7R7GxiKGa_fWqNG4uGGqu1rBryMlnwifvH7jZafobBSNiHcjYshARCEydMMKWE5Zbvup5c-NlsCy_5NJWGWkFmT_SN0Xz5Lea7bnkQArhBmLy0_cXWakZiroxPB8hZk-InvBni9tVht8bAPvwU2-EhurBQnpXDBdfDpJWWFp7AS95azQ2ij_ZkMDFaF6xlabZsYjoQGC9uK5O92DONW4khmSVa_ed2ZwdEp8IkrI3cH131qOr_5ErBTLhN-ZS4nEKu-dPkEEQEHr2Dx2Nq-Zxpwwov3ysErAXtj92bqkvPVIl1HTHGcL1n1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=MGdnLOMPZPCoQOGCvWmuwlWls2oi9h2ng3xVEBd0nANXUOOlD8nkODd6v0B_u0L2sy7OhnfaQ9zfZmk7XOjxEFy5AXhYDAc18zz50zmppOaZFUuQqroC91OX-3GllmOpMz4KUuOu24CP2B4u5Kz8ZD0tn9DWed8g_S7pL4PsDfowl4-OEgRFPpk_MbboUPdBtVQvWA-RbIlr-MLq9cDH0yzLYCzOfoVuR2UENO3dwmjsF1auDXaGIbYjUwnHdHpQ5rPQvvrzEIJhltFdsPSlxKSDV1w2JybH4wZ4YrG8l6Jp8xDuNmi7X9WG_6zza22XFJxqrw12TGmXnWTm7hkPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=MGdnLOMPZPCoQOGCvWmuwlWls2oi9h2ng3xVEBd0nANXUOOlD8nkODd6v0B_u0L2sy7OhnfaQ9zfZmk7XOjxEFy5AXhYDAc18zz50zmppOaZFUuQqroC91OX-3GllmOpMz4KUuOu24CP2B4u5Kz8ZD0tn9DWed8g_S7pL4PsDfowl4-OEgRFPpk_MbboUPdBtVQvWA-RbIlr-MLq9cDH0yzLYCzOfoVuR2UENO3dwmjsF1auDXaGIbYjUwnHdHpQ5rPQvvrzEIJhltFdsPSlxKSDV1w2JybH4wZ4YrG8l6Jp8xDuNmi7X9WG_6zza22XFJxqrw12TGmXnWTm7hkPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiKgl9vMWHyEHSYgNqhoy5Ku04J8Yo4gnjy8gkfCB1Gr1-vwDlY9I83XrAUYT6TfDDPZ5TxE6GQedHn596eSARjiN0IPAzCJATzDB1aXC2AqqjU3RF8teY0OXOUroHEKbxNfp68iNkGfPTPPpYvUYQZkBkR_ZxDWcaj6gdYslz7Q6o0Kal8fFVbVxHt9-k_Z8Qzi_2wj3cNSdf--urrOKnBqynhjCn0WB9QDg8xtEzqO8CUU7a0Wdnlx1_crj6es6mIIyqIkj7h2NH1k8Rn4qmDqGI28B_rKUfHiYddGjD6R8EdgAWpmoLyTmHhy7MrB9a_ZXr1y1TjNd3zFr_bbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUL2O9Kf7tbv382mdoOlLqL3LAXKbDly1JuTv7Q63bXmnHNb57Sp-Tg4m3yJ0XhNsnGTfB8-ih2phjXRb8rYS_VjyA1QkWmxlEv3Sehibk6ZAkZmC4YXMOSZi3lQlBWsKWUIqaDtlGdEyqsQTnQfj5o6XveTKm1NjRre25DrVFXtZpOsd49k9TBWBaEXemLRly4OHqVWSl04oPvY8K0wDww0-89amraD2Om7RrHG6ouWuM-X-94VxZqeyGtPQI-ewiPC6XWPwAfJ6EmscNhhXESfFDPQXjEgpyDCEmk6wPmHFHbPMmOGrUR5vSMJm9ZK3seOwglaN5a-exxFr1HDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=TPhjWpm6xJ-Onc6qz45pNZYX40Gs24ppebMAItIEyJn2-vBfxO5wLAMmwrC2lLJYuHbaK3Ks2ZpqEWn8ErmzL_fr6Krc3Lo_4mWMdA4PK31Yq0BiCTbH9zd00O6JP1TrdMN8LhiIdodQ3hW_9nZJN7M_9cgi6JnmH1sbD7IaKeqz8fXUhoVqGEG7Y8r8vuwccKOCKhsqgpO0OV2Z9qvjWuPRAvFy14PEQyOior7PpCHmEvio1Y8XucpwSdAtQs0d4ptu3249e2G8tW2Lk-tvWxsvNSQTmWOCb5B9ai8MOQ0DzAIS7NHS2hIJqtIJkRGfA2Qb6Wed6UhM_H4CnwhddA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=TPhjWpm6xJ-Onc6qz45pNZYX40Gs24ppebMAItIEyJn2-vBfxO5wLAMmwrC2lLJYuHbaK3Ks2ZpqEWn8ErmzL_fr6Krc3Lo_4mWMdA4PK31Yq0BiCTbH9zd00O6JP1TrdMN8LhiIdodQ3hW_9nZJN7M_9cgi6JnmH1sbD7IaKeqz8fXUhoVqGEG7Y8r8vuwccKOCKhsqgpO0OV2Z9qvjWuPRAvFy14PEQyOior7PpCHmEvio1Y8XucpwSdAtQs0d4ptu3249e2G8tW2Lk-tvWxsvNSQTmWOCb5B9ai8MOQ0DzAIS7NHS2hIJqtIJkRGfA2Qb6Wed6UhM_H4CnwhddA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=T-j1tmXGTTy6uZ6oAdjYC49AedBB_iAiFlpm3lskISIkHOBQf35JmTdHYLDHtwCqsusimHxjyrwF1mEuYAVmDgUwsO88uEnnsjXFflzIAsatRupv_Hw6Jx15UxJ3p4onDANIykHem_NjMGijwvBvmH8vk2uVb6lb8wfVmLTqiHWun42swIXwQSVfJmSwIwc5g6I5N3RYVTY-cRtDOddjCzSRdannVwyFYYuZoA4YLJrLM1xqhL--mK1PGRRzYtab3caQ0IZNiqLzIX-xKbYJ3lIEzZzQ1ZYOB_Kx5wbobrI-r7cSUBwFM8yvuPyrZJipqpwfHWNJAFjFubT8wYkt4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=T-j1tmXGTTy6uZ6oAdjYC49AedBB_iAiFlpm3lskISIkHOBQf35JmTdHYLDHtwCqsusimHxjyrwF1mEuYAVmDgUwsO88uEnnsjXFflzIAsatRupv_Hw6Jx15UxJ3p4onDANIykHem_NjMGijwvBvmH8vk2uVb6lb8wfVmLTqiHWun42swIXwQSVfJmSwIwc5g6I5N3RYVTY-cRtDOddjCzSRdannVwyFYYuZoA4YLJrLM1xqhL--mK1PGRRzYtab3caQ0IZNiqLzIX-xKbYJ3lIEzZzQ1ZYOB_Kx5wbobrI-r7cSUBwFM8yvuPyrZJipqpwfHWNJAFjFubT8wYkt4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
