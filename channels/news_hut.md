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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 01:43:18</div>
<hr>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OteJF0hYRGEzUIQ9egwX3RlFqS2WK8-hIEknzis_US2kKPDCpMNNGP31P9WgUwAKhdT5oFSlr-Jk_pbP5kHnuPuuYlAtAUDxHJABLeR0nkEem9E3Sf9S5Tn6ImyqnHMJSgoyekC7SVMuV_XCyho9M2vaMjwAmk15ynYVpDUbbsX_yLZ__qRRo2mI3XyJmPjY9xEjtstM1JAO3nkuDLflgafviO2znihGK_KfUU9y7yDlmJpGrCk6zQp-lpYw5eaH95Y8U3ghLZ-LoDjmDoLDNwad43MPE70Mun1QLp7M6K76toYv7CjDF3epUzv0GV0LHIVcBFDU9on2BNXXqLbU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeEbQi8T2PC_sQqd4hKtH5vzOSgidP3JASufOrlidF1eEZaY4o-yRsCLKsjT_3fsH-K5zptddt4LtVRZ-ioni_Y9E6UbclXyeuRixzMGabj5ChOKHV5V5qSkdn0mX4IzM34HopQfn2DffcN59hq_qWfbvHSs4ExMnLPsIbYkDB2xUeBWhE4SuJUDLWvuoIXfaK7bpN1TYEtJ616qILHX7IStR-60MRKgkqH0wkfyobryJ0wKaeGm8K8fk40BzqS-ypFN8nSHfGw4wBiinMsnt70YY-MhmmaOhguLJFvOs7KgtfgDp5_HeiGHf_G0NkheESvTscOdaiPUnpa41kv0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7lhaT-Ic-nzi2RP-gJ6aoXDmytJ48npqmADdjt_pvuZlI8GynlaWq6dyaWY-_xvo4RMN9JfbPQoPMz5JwlivucEEubEBlXAYXwg2KOySckxSlw7Pn2vdl0puQoqOIM9E7mOKZ_GupbKhCPNE8zeVeL9xeRXpsnw2njNO3SAMAzs1kd2h-7Oy0wwwh8pTZHH6sR9bvrZgBPthyLAxM1Z_WaAFuSF_fj4OvLgeeCG2GU8BF3gM4B2Le2gl125KkXy2nghuWQJOKQIKvXeHPUEtJJ4o1a1r586EFLAMY2UNP3uBZWm0firfaUUaTrBPIUilhXZokXyNV9dLizrUNmPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtRrzde2SrO2dqZsHizSjk3GBSKURoeUa21vmRd0uZjQTw0yMiGvvt0_c3QZDzom1U9fPwmSWDRJR-tYNvMrWMzgHe1M8PSl1XooFxi8nKFGSafe5f10km3s7khoTn7gYmAZn22vKOQYviuCPiyL8Kv5FdBm85ltq5DEvnvowiklYiLNOMhDHSFKZcQ7Dm7q_7A1lRVJ_zSYtWFnw8X34A0bjnSB4w04tM7ZWPpWuo7zyBxJLEcwVZ84qsx1hRxHp7PN7huFETRARlF5ggokILyDJ80sjAgo33f7JWEDWQyzH5V69i9gVcouVFM7bd9ichyDAXgBWpAJsGfLTmYIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=cPNIp5dwlFnGAoSyfrJMmpheG8vjl8SDqE84rVC1fYByk-mB-HLS0A03iI_9gp4KOEhfrnB2E9ePo_DUD_ChhwL-Rh8QamkUQKUTlAbTuEOK_NNH1IFh35jW64UuKljEeeZos1nWmBNLRdDJE-vjgjMRRdCq9xjbTriEqhheYoBcLF4hL9VMBYO6EaE5SfxO_jzSjS3lVXW8_vseDNjcLUrhMLndOWEBuMJFknyP16pLb8rEfIqEmvG1roaJl7N_U5u6CUeBAXGtfrqMBrHqMoJj1_utPl4NdnKPkGBzNnBiHMeSLWyuOZHNf6EMggcLqReT_KXjCvyDv2HKJSenSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=cPNIp5dwlFnGAoSyfrJMmpheG8vjl8SDqE84rVC1fYByk-mB-HLS0A03iI_9gp4KOEhfrnB2E9ePo_DUD_ChhwL-Rh8QamkUQKUTlAbTuEOK_NNH1IFh35jW64UuKljEeeZos1nWmBNLRdDJE-vjgjMRRdCq9xjbTriEqhheYoBcLF4hL9VMBYO6EaE5SfxO_jzSjS3lVXW8_vseDNjcLUrhMLndOWEBuMJFknyP16pLb8rEfIqEmvG1roaJl7N_U5u6CUeBAXGtfrqMBrHqMoJj1_utPl4NdnKPkGBzNnBiHMeSLWyuOZHNf6EMggcLqReT_KXjCvyDv2HKJSenSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=uKvMkdav3EK6Ncctx_FQos-BKA_jj2fv1zsmYQT6p65otQU96nq-7ufcS1-gYmbqeAjjMbY80yUKY1xe2dXkpfHSe6IdEsZigN27v2Y0_XEpgyo611QPoenZaYNLTXc_LK5moWC7s6gkaEOeUxpk3J5kpejuey2XLLfIQ7F3nXfamIV9KsRezA3LCBGW5APw1_f1sE_dv7JhLq3fEH9IIWENmWC10CZDC1ZzApu4HFT0NCFpCHjEWyRqDi6SsD0nktvuMrG2zq8QBNSRgX3NZzifmz95mHAG7zHspOWoyfF3-5Y6VpMSLTWYRDe3-Ilsy03_wfhUYbVRoJLcV2zRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=uKvMkdav3EK6Ncctx_FQos-BKA_jj2fv1zsmYQT6p65otQU96nq-7ufcS1-gYmbqeAjjMbY80yUKY1xe2dXkpfHSe6IdEsZigN27v2Y0_XEpgyo611QPoenZaYNLTXc_LK5moWC7s6gkaEOeUxpk3J5kpejuey2XLLfIQ7F3nXfamIV9KsRezA3LCBGW5APw1_f1sE_dv7JhLq3fEH9IIWENmWC10CZDC1ZzApu4HFT0NCFpCHjEWyRqDi6SsD0nktvuMrG2zq8QBNSRgX3NZzifmz95mHAG7zHspOWoyfF3-5Y6VpMSLTWYRDe3-Ilsy03_wfhUYbVRoJLcV2zRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=uD9UJaUZlIiePAZJ8kfAvgJcq5WdgWx8v09zzDo1-iWdBQVYXZlN_BOsxjhO7s2CO4_D1-QuPWOtNULxppRKa0k92bKOwGhHIhM9Xdm2ptVjMIy4WqMiM_WYhv8SorTnrSiBV0PViOCUr94T_DENXJEkLjv5gByFSMg4QDMOzhQifL2DOe--lpo9RTjKRfqGZ3aEkbGxwSGiiQTB5WVhzNQSCjBP7gd-ZaxClabisTeqkkYLGmo8OTfU_u5-dLOKKx4z9ucByzxHq3XALrGuoC6DKXh7CX8hi3rjAD8vV-rCamKXvkaE9qFLmMaNmVhkZLtv9x_-3MudzjV_YmuStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=uD9UJaUZlIiePAZJ8kfAvgJcq5WdgWx8v09zzDo1-iWdBQVYXZlN_BOsxjhO7s2CO4_D1-QuPWOtNULxppRKa0k92bKOwGhHIhM9Xdm2ptVjMIy4WqMiM_WYhv8SorTnrSiBV0PViOCUr94T_DENXJEkLjv5gByFSMg4QDMOzhQifL2DOe--lpo9RTjKRfqGZ3aEkbGxwSGiiQTB5WVhzNQSCjBP7gd-ZaxClabisTeqkkYLGmo8OTfU_u5-dLOKKx4z9ucByzxHq3XALrGuoC6DKXh7CX8hi3rjAD8vV-rCamKXvkaE9qFLmMaNmVhkZLtv9x_-3MudzjV_YmuStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=JNAJ7lNiFjt3MwnD1rPGNvQ9z_Ey9V-xU4sPduzwgNA3STx4uGEIUpu2tLdMYabq5No-5FbPa4GA0XK3kN7-G9dPI5xMasmJAtPEylILtQ6xQ8FP1CyJpElzuXmWrzxlK1IZwxO9_ltJ328nDymhMYcfghzdtkRmFsgOKvliEo8wp77RDZF2sHA0THE4GPC_T4-B3ZYzh-yAPKpanu1_oNcpOcLb0rWq8Ub4Szrvd9aXvuqeMOQHvUy-gCTedgntTCJqfCy4fRbjWY1TGTZZm7Z_dPOImu9YUAyfrCfKvCPkdJQQ_ZQldNVO0Up_jRwMudjnthVu2KthHicpHxEJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=JNAJ7lNiFjt3MwnD1rPGNvQ9z_Ey9V-xU4sPduzwgNA3STx4uGEIUpu2tLdMYabq5No-5FbPa4GA0XK3kN7-G9dPI5xMasmJAtPEylILtQ6xQ8FP1CyJpElzuXmWrzxlK1IZwxO9_ltJ328nDymhMYcfghzdtkRmFsgOKvliEo8wp77RDZF2sHA0THE4GPC_T4-B3ZYzh-yAPKpanu1_oNcpOcLb0rWq8Ub4Szrvd9aXvuqeMOQHvUy-gCTedgntTCJqfCy4fRbjWY1TGTZZm7Z_dPOImu9YUAyfrCfKvCPkdJQQ_ZQldNVO0Up_jRwMudjnthVu2KthHicpHxEJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnkeF5HkrcEdO6tLtaBCkoxEVT1Bkx6Sw72G6JFmLlvv9FAmKGmY92FyhRgUg0T8AgZvgo4ZpTHhlvZMFqzL6K2zzh7dQubEcak8CBUUtHfDd3SYYnZqqyU1stl7q-qLAnVjbR_u3JZLxrsvFr_ybXr2Fjy8musGvvuZG5NIjwyQz1Cv-fNdg2lLIyusjycShlU3SxboMMTv6F8thhBqjIXctUtdzGbwz3O4UykxbqQYQ8Zq8XFdLlRu6towwsFAzsaOvTTuJJn36yex0Nt2pcvey-RSbkk0pRr4PrNoR6DZBWAywBA5MD4MabFArEoKHKfjU8gFXEAAPPb7_S6P2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIo7kE_QXBbvjlPlCHKQhMOxIEkOSIugLKMXAKtEe2WzyNSCV9_2eQtVEkrFdA8Hzp_LHpoZsr97lduNNyg6cZuPfwlE7i8me4e7_VzPHM208-yzhfnPNTAGLylebYEuotjH7Fi8pNt3dMtkPBnycwX47YjRtCzbGDBBCSYmreLAti-WzlYNS0-nRVr6D97Hel8KmLp4brtDPjMyzz6-HAYr21WzFh_xNhk-J8BSRpZ8r_tjHLH9BIXzriE3-Li6QVqUTSczu8Jt2GZ5z87KuMpAYv9OYRG2bdQz0yigtrqoXFPkh9jCumS2h9l7PINgOlNrE8L_CLojcSaJpH_2lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS_hBEBftXImDStsip3-K9dgBo5JXAxGpNn3IoJdLFbI0FvlykibWcw-M9sktb_o-0FXrmB9r2rexIog6CDxI2iFz0PVDWjzC-F4RDgGmFbMHm-vBTXcp468nkiV9tWjynCyJmbFyyJI89tV2yzwGCGIV0J6ocnZvBRtKFZbZdNllKk0moN92f7ASpvxLIDql6TXm3PkUsvNOXJys6E-FcJY0QmVLo2vMk8u3qFfJzhHmhwIQN8u3TcZIOu7Y5RE-5CtyaKabMRvJnokXNdMoNFAVqCaR2a20HmxSrXX7fbG7t_KkjmeWND7S8dD8g7N0cmJUIXE3xQJZyom1RiQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saX148JE4ez0b0e5hfgfpNMEQ-m0KiPEVrpjotKxt3KNEN21-qiVE_oK6DlaWnmz-TO8QImAAB3dQZAC9pl0fjnaBqo28HPouW3lZrZb5DepRyi3Jmq18f1-C_O4vjkNvo1Icqzk63TMj2juBo7BF_-9HStQ_5ZnpL7HrWIn1SaOLEHJ2oP7dsuZtT_zsgEHwB3zSd89axxRn678gnDlLwct3BZsWSPwhYnwyoz63xmpBvjLfgjH3CjVh72vTutJzUGHK20YfEGidnNzrsdso78NGS9y33aJ_qgiIdtow4NDSXiMvnazId8cMhAtzhx9gsMjGJM9IrmEOc1rlSyX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy1PXa8NJboGGVKdWRLj9ezdoCkuORj167f9eTUPAfw9enoTYYx0Nn9g5UjT6RNzHARPan8GEtmy2ChN9QsAbmj-T4k9Ij6SgwxCPPjpscAoKXhc0jhyPIJeR5VukNGwCASGqv_U2T-5iV3dfwkJ36BRpRRVraQGcFJQDZaWuEL3tXvgvVFWh-AkrhWbUEU7MqGRtwUrYiQZyQfl9c0cu-5FH4p46DVStX-2L2ryjUgBXmShxj04HSHQhKFFkH4Ur8lAxEeFFE8BsfvcHQS5mnAS_b0q1-scpIYpVvcwTVkG6gtKmpLutQwH9Z_OtFjCbzGSvMjBILJcdvL6fOluIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=poB7nOzZxeWb-uH8T8TiCvw3Coyo9eaycbxDNXRLw0bdZSPqFRz6gfhQ5UAbo5_ZCHrWWOeABB0J7SHTVzz3JPvDE44q97MtvN6Z8GQsFkbxxMl_IkgtalQixUr-qxByAunRBSRDeZfQ_8m1-dTdWh_8xI_HUVEGTrJaPcTQpdy7oEGX2G3R3pCwMb_-A7JJtrSgGPieh_oGkeKWYLvFtJzuqItQU0GRyrIyZJkZSuV1nBB6CWTPUBzHKTePVwULcEYCb4RgkCvnhg59UYRon_Vc7G6aYgKqrppwEsfVgTdFkZqnV7Pi7Mwf5Xdc3kz49hw8p16hADjkTR4tNxHCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=poB7nOzZxeWb-uH8T8TiCvw3Coyo9eaycbxDNXRLw0bdZSPqFRz6gfhQ5UAbo5_ZCHrWWOeABB0J7SHTVzz3JPvDE44q97MtvN6Z8GQsFkbxxMl_IkgtalQixUr-qxByAunRBSRDeZfQ_8m1-dTdWh_8xI_HUVEGTrJaPcTQpdy7oEGX2G3R3pCwMb_-A7JJtrSgGPieh_oGkeKWYLvFtJzuqItQU0GRyrIyZJkZSuV1nBB6CWTPUBzHKTePVwULcEYCb4RgkCvnhg59UYRon_Vc7G6aYgKqrppwEsfVgTdFkZqnV7Pi7Mwf5Xdc3kz49hw8p16hADjkTR4tNxHCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvpLQ0kuHFjZwee1o1BnYI3lbqsruIxzUm7rzeGXsGelq1RSDNqqRcTTfhPCnR8xu1SepqNkOYUpIM0NcyiPmTG0Yb6nv896-ItIh0ZYdS9rDrDcdnyO9XVQ3AmJaj-nBR_7GlmlY0iS7aI6G2S9BDM7tfamP91HJR43iFaOV8ZmaaprTLYlyCkwTHH1CxepnhypCEPKUENTlEO0Gz3ox4gdEbXmE-1T0NCW1KnfSM_lvvhItmuxeAl1dD0dw2iz370-0-itSUe-LzRgHz4hM1KvYKz3OOeUVvjXiJH6lNpO6QhqimJF9WWfIoISEhdH1YxQFbE3dWpaMisDypIzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDKqqGpc-DNKfy_r5CNv9NPmlrH-TfwvBU_xEIqRcV6dGN9bLVns_bDTu6VleK-p_haCXRw0x0ULRKW1EO9X79iW7ZYh-G8r9r5JOTMLzieG1jCQjPdOCk6FG9RjgnWk0REaGPnCH-iDa-3QSxqWdhdKn9eMk4xZKTY6wFI0lpE11ogODnip4LfmpSo1unVPNUX5FXpntUGubn8dcpQI52TsJvNyoyRQT-NRioShbRKxMihNMIHk6jffK86nPpV-8aYPFxmsLk-IeFJBilQIHbNnAk0tP-gYkL8FVAD1V1uu8NLxcIubvueCbNJOYppTyllSTGohCUk0Cl-PCKJwuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=VpUsm5cRvP9hqe8Qi7AndFeqMhWmgI7bbfrjokbO3F2ObDFoht9smAkBgfkMp66baCZK3XRmvRfPZRRh9x0qBOo8uMa5wifwriQtX_C8h0H8EcTLNp7qPr__Eiw2j6-u-4sL7prNBPlDwlKQg9D_GiglngtDe9FqGjWrqDZzGhmMiaQPFj8afsJ7rgrYzgouBJ7x8R5RM1AxIyvaQgBo8FmrnQ6RwCm3vGJ3_kzLYiFWcky-7WDB6btZhvsmcs90xvxTSC8Fk7FFMwZIXnHziYMcC9epqqjzPRy19r8TPGKEYFgfsilyIaxZtxtaEoauuPigKw8b3ffF3TVC3qm5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=VpUsm5cRvP9hqe8Qi7AndFeqMhWmgI7bbfrjokbO3F2ObDFoht9smAkBgfkMp66baCZK3XRmvRfPZRRh9x0qBOo8uMa5wifwriQtX_C8h0H8EcTLNp7qPr__Eiw2j6-u-4sL7prNBPlDwlKQg9D_GiglngtDe9FqGjWrqDZzGhmMiaQPFj8afsJ7rgrYzgouBJ7x8R5RM1AxIyvaQgBo8FmrnQ6RwCm3vGJ3_kzLYiFWcky-7WDB6btZhvsmcs90xvxTSC8Fk7FFMwZIXnHziYMcC9epqqjzPRy19r8TPGKEYFgfsilyIaxZtxtaEoauuPigKw8b3ffF3TVC3qm5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=AvTkO79HfGqLielWAtkzkwvaULpiD7SmV2yQMeuOeP4TVC1h7sas4QH39Z380asbO0178QGY_tUZRwIP889JOCExv3uU4t3g-1QRS1AIGH5qBbjR1iTk9_M9b3yYwiqlMbn6KHR6WnQBAiVa0VJNSKoijS2EUnVnCmwXg3LsPMmV7WZYCnze9aKFbyRxPvGcr6d46FgNvbG38STrtWzz3toXzXwA_RkCcZYHxzjd2qjm-HY63XBvjyBExYT2-1ai3Z8fFFqA6vLtNin0HSAyFoJgizk1ivUTt9F68xfhHvWHgBXhTY-R2g3OuN3PvmKM9pemsms8fHOl6TQIyzP3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=AvTkO79HfGqLielWAtkzkwvaULpiD7SmV2yQMeuOeP4TVC1h7sas4QH39Z380asbO0178QGY_tUZRwIP889JOCExv3uU4t3g-1QRS1AIGH5qBbjR1iTk9_M9b3yYwiqlMbn6KHR6WnQBAiVa0VJNSKoijS2EUnVnCmwXg3LsPMmV7WZYCnze9aKFbyRxPvGcr6d46FgNvbG38STrtWzz3toXzXwA_RkCcZYHxzjd2qjm-HY63XBvjyBExYT2-1ai3Z8fFFqA6vLtNin0HSAyFoJgizk1ivUTt9F68xfhHvWHgBXhTY-R2g3OuN3PvmKM9pemsms8fHOl6TQIyzP3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=rbhG2b0_Igc5uStiMAautwyzcxZpJ7Fc0vXpCve8BVRDpVKtGyypzy_PzVoCz5TVctSvxgbz5fw_-BEvaWZ8uJs021vsE6ZN17zahzDI74TzSfXJDAywFmmXjYlFthqtC46r6VRQ4jZbUp2urmHS3KzEoI1Kja9yhzjoX1HpjuW3Fa0xvKxM0aZGfRXpAa4TYM6GIRA589RylJqhmILpt5N9fgsEYJEVh_ki45w2MlkAQfSQZEjRpnxLw3wgSIDpn-UF_7PR6Bz0JzxMygBAOJeatYBVUPMhIxUwMyQcMrSxKahpia_EPwMxlUOT9JQiBDymOBLxMnxRpjRMsYEQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=rbhG2b0_Igc5uStiMAautwyzcxZpJ7Fc0vXpCve8BVRDpVKtGyypzy_PzVoCz5TVctSvxgbz5fw_-BEvaWZ8uJs021vsE6ZN17zahzDI74TzSfXJDAywFmmXjYlFthqtC46r6VRQ4jZbUp2urmHS3KzEoI1Kja9yhzjoX1HpjuW3Fa0xvKxM0aZGfRXpAa4TYM6GIRA589RylJqhmILpt5N9fgsEYJEVh_ki45w2MlkAQfSQZEjRpnxLw3wgSIDpn-UF_7PR6Bz0JzxMygBAOJeatYBVUPMhIxUwMyQcMrSxKahpia_EPwMxlUOT9JQiBDymOBLxMnxRpjRMsYEQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=YZh6B9PZxUKval9jiJL5yVKP4ejrig6OXuWsJpzxtptPW-4jf2uP8OVIRmrmp2pOaJBO29x_xH44Rp9QQtMyA3jJ133JqUIbIPFxfFY0dL4QGVnNX83VvZjrtqiwVfsjNeERd1FUJ8mfc9ZnOirIfJK3noexi39o79-QGElfchEREOlCVrEa9wtHJaXUMsS8w1DxWt_dRo6Q3KjQXmlk6Baov5YncsyEeg9Lrs-itIHisoMYfsgtodzDBkS1SiM8TJyU6h3G4OxofxJ3i72dKL_F25RrO83iQq6gVPmO9zMJE1VpUo0ouXqduMthSX5XWXfYDNsWV2JKjMN65kfQIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=YZh6B9PZxUKval9jiJL5yVKP4ejrig6OXuWsJpzxtptPW-4jf2uP8OVIRmrmp2pOaJBO29x_xH44Rp9QQtMyA3jJ133JqUIbIPFxfFY0dL4QGVnNX83VvZjrtqiwVfsjNeERd1FUJ8mfc9ZnOirIfJK3noexi39o79-QGElfchEREOlCVrEa9wtHJaXUMsS8w1DxWt_dRo6Q3KjQXmlk6Baov5YncsyEeg9Lrs-itIHisoMYfsgtodzDBkS1SiM8TJyU6h3G4OxofxJ3i72dKL_F25RrO83iQq6gVPmO9zMJE1VpUo0ouXqduMthSX5XWXfYDNsWV2JKjMN65kfQIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=Iyj23B7tDqWgcJRjKWvsm4w6-2mZKJElAyuT4EqGQwx3rp4E9lMaDF_MN38bxrdu1siZaT6kG9HK5EwHg3TUqsxa0rpBL3Y2Z5KX8cL3JY9Q6ajaIZgoAa44mzqe443e-hvfto8EEsOYL1DmmdZWBKl6ootGHrPROJJXuO-nLIl3lGU_WJ2vu-ggvAy71ob0buxFe5mWuI5cOJKGFJUfTEvuO5TbpILDKd5gpvOOEl-XeDpw0Ez0GnBaCncSbukE3oLfG5HUy1S-v-81KVckDnASEo3kvLpE7TZe1W49cyK3li0L1XlZVzx8oPR92vEiJjQnF3mSJWQTPphoBCHI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=Iyj23B7tDqWgcJRjKWvsm4w6-2mZKJElAyuT4EqGQwx3rp4E9lMaDF_MN38bxrdu1siZaT6kG9HK5EwHg3TUqsxa0rpBL3Y2Z5KX8cL3JY9Q6ajaIZgoAa44mzqe443e-hvfto8EEsOYL1DmmdZWBKl6ootGHrPROJJXuO-nLIl3lGU_WJ2vu-ggvAy71ob0buxFe5mWuI5cOJKGFJUfTEvuO5TbpILDKd5gpvOOEl-XeDpw0Ez0GnBaCncSbukE3oLfG5HUy1S-v-81KVckDnASEo3kvLpE7TZe1W49cyK3li0L1XlZVzx8oPR92vEiJjQnF3mSJWQTPphoBCHI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC_OcKX9-pd_VRJgAeK0_5PsolOcQy06fkpwO28RoRF7yHL2kTZGBztPAYdzZW6wrI4bpR-XBYkXYRuA6lxs4UdP8gPLr-QU_fLh9RollLiOJdiS7wSJ-SJuWBlI-wwIq5SudhS9M2moRV9UDhoG9h8oB9cDVHu_TZuD4x56d8Ptu7ydPTVmm-kHSVkymzwS4BwL1TLaQ5_xSpA1P9wcQRdKmiG9M4gie9mWoqCc6l8Q0CZC_5QXewZmCw1fre4LbU10mPyP6LybEtqa1Z3E_AQ2vFKuHsxhILx7B05nQ0cmwLQwPpk3fP8l5WoCw2Hl5GRtdbK8m6OWMLKdm1sCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAB-sO0wEqIVdObIRYbe86LdPGMme599Rl0fuxkJmWOkoReQYyB-_on4XjorPD59zhPIt_oV5BzUNp3kHK6jpKQxjHp0g0CkP-_5YqiQwuW5Ut0RKXD5vdoniHRgTcnVJclAX_RwM6LltsflsTXPdGqDxUGHC-EspIYAANk3Tjya705h0knDZOoRlP0zMwyoOfFy2Q6thvq76P5CP-QHFR-3Hx8zTls26MI93yiu_iX9CK5Y-BW2Ln2jxu04fEDRciKksh1XHcQLWx5ZgP1nQwsTELj-q-mzQOBe3rST8h9zUB6ILq24tVssjtj4-Sdc0C4lwEF6xuSy-b1a7w12ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oA-gnycW8tCY13gc_ljzItkOaEWM2XvAyk6gzfaPF3D6pnLUdvZoc_OPNcLWAQUAtp8VWL0KQm3_sO6qOICUpnlkaZi8swDmxrdtDR-Piw3DocRHORd6Wl7riVqui6s4Oj463sdyenlzlSZqmX5e-24FI8k6cvME90WuLUAvasTJDNysok-XyVlSsgSlcP8ZvhQ_-4BrDFwp9IUJawvk-8wdqpmGIOKmwi73rrgjjDqGl2bjKtAu032mIV8nYYvpLtafHEE6kNdzkcjKLBYEEWArMloBL8Pb7lEIOKVfTk-q6bWFgvFcP4gFbrh2WC2M4-1b519Eb5t-iltqtxOrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=J9emYTWYypzA4KBY0RGTVwAdCGXpSW4zQIqAYJXM3p_E0Phzu9-knhLcXGWkxOuaFgmEsJEAsBitvs1eYlsVmAyUUEptl1rQ1vzkP-b0NhqIbYkR1Ol7UMvFSSUYZ8erdLPsd2w5qds2-NsMz97Q2LHUutsMM7t9Z4px2ZXdt-iuBGey4hHSqZcPhvgKk35Qy0k1MUjzEQgT2-L7j9vk2OXIOvxK7XlN5osYz5Qd0YgTGiFMipB9yDHeuIg64Cej1DCXMaOhZiLwEORMdrMwfJWlpbFl8dRVgDzTX873x3JevITtaw_KIaBIiaX9GHU-vTrho8b22kHnNBY6U50IeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=J9emYTWYypzA4KBY0RGTVwAdCGXpSW4zQIqAYJXM3p_E0Phzu9-knhLcXGWkxOuaFgmEsJEAsBitvs1eYlsVmAyUUEptl1rQ1vzkP-b0NhqIbYkR1Ol7UMvFSSUYZ8erdLPsd2w5qds2-NsMz97Q2LHUutsMM7t9Z4px2ZXdt-iuBGey4hHSqZcPhvgKk35Qy0k1MUjzEQgT2-L7j9vk2OXIOvxK7XlN5osYz5Qd0YgTGiFMipB9yDHeuIg64Cej1DCXMaOhZiLwEORMdrMwfJWlpbFl8dRVgDzTX873x3JevITtaw_KIaBIiaX9GHU-vTrho8b22kHnNBY6U50IeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNy3xTff7kp7SP3XiF92C6jUJC4-pZxUhOAQQMP1_H9DnZ5Dc4K73m5MSPPY7Iesp8N8Vchj3g8kZkqsPInsB928HYJMZEviQVdZ526OCrW6fHfOB1vw-kL8N9qHsB4VpBu0t6gOTWfBhXB0nmkQAJYqxePaaqttpD3EyvqTIbhVH8tCWTE_swG_eCn311g54JAkWOeauw-bGIM6E2hCBkzH2ETrc3BgV08Yp2yYbBIK3Yg7bxhhTp9SQvHabsUZ0hN5X7o1tRULopfy2CkbJOaufwxN4zcCTewU92Bmo08zsJo8wPJEMDxH8K_STJkcYCVHU3HJCzXXtwn9aXjoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=Thrpu-Ge1maQOWXtT_9nHMQJTgcl5CsDUusq8tpOn4cHeqxCK6UWMRiO-MMyJaGa39EFOPCbhXlcqeRQZOdCUb7nsSxYuhb5PwZsbQDZACc8bfExr2k8N9zM3ENELoHPO1BwIEYexj_2MlaWmsUH2g9I5AeFbwtaNB6yzFqbSXkYMAcOV5HOKXEr_F2pfKm2jRxJmnVEE_qQ994JtxaI1TbaelL3jRltoVIvKWYp6rc2d10EuV8yafhOAy6kaSX7Xt1IuW7Y7Ll-F-Ra2O1U80QDH_1mvHZQKEJm0yCbriaMvbACMlFoHvPeKjOWuBjQA8hs3FrbFkN-m5RccQRXow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=Thrpu-Ge1maQOWXtT_9nHMQJTgcl5CsDUusq8tpOn4cHeqxCK6UWMRiO-MMyJaGa39EFOPCbhXlcqeRQZOdCUb7nsSxYuhb5PwZsbQDZACc8bfExr2k8N9zM3ENELoHPO1BwIEYexj_2MlaWmsUH2g9I5AeFbwtaNB6yzFqbSXkYMAcOV5HOKXEr_F2pfKm2jRxJmnVEE_qQ994JtxaI1TbaelL3jRltoVIvKWYp6rc2d10EuV8yafhOAy6kaSX7Xt1IuW7Y7Ll-F-Ra2O1U80QDH_1mvHZQKEJm0yCbriaMvbACMlFoHvPeKjOWuBjQA8hs3FrbFkN-m5RccQRXow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=nOKzco93mYK5uIiuTn3ZgljLFZgUotXnO-vUAylWZnWvHelabbYn6g_uTsLbJe0IelHdgg1DI1uFVb_iGvs7_WwWKqG8Amhkn7P6gjdpmDRwnUh0VslkyUrXp_I9RDpkoM-awUE00C7j8taQHBnXJ-eScL2mQDiDy8csW4WEfV-zRTVuv_LpDZhn777z1wuF8CzwnjlX9539a2h3_tot0XAWPPFWOzbusF2BYY9PKHaUU2Lq4n93B6UWnqiGwGbWgNGDY3qtwcxfxb01VTrU_c3uLk43M7WZWEStikHdlo0HaoXX3ETv7RkomfixU6rcIqtxGN07BOE3yqUvTaePcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=nOKzco93mYK5uIiuTn3ZgljLFZgUotXnO-vUAylWZnWvHelabbYn6g_uTsLbJe0IelHdgg1DI1uFVb_iGvs7_WwWKqG8Amhkn7P6gjdpmDRwnUh0VslkyUrXp_I9RDpkoM-awUE00C7j8taQHBnXJ-eScL2mQDiDy8csW4WEfV-zRTVuv_LpDZhn777z1wuF8CzwnjlX9539a2h3_tot0XAWPPFWOzbusF2BYY9PKHaUU2Lq4n93B6UWnqiGwGbWgNGDY3qtwcxfxb01VTrU_c3uLk43M7WZWEStikHdlo0HaoXX3ETv7RkomfixU6rcIqtxGN07BOE3yqUvTaePcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=hSiSdHEeMqThTo0s--7gYQ7jS844yNk-u1s9yfR8mXyddU9kaT_wwn9X_twny-2EW6nM9FgH52xqcvR8JIpSP78gQTgRTIqzCbRFYKApjWZ2KqjQLZmfilgE8w0KFe4bBEtrTrlzGX6nkU3-6oupGELNY_rhg1wMZp0FSwyMG8wBzYSfImPDoyPDBTNrU_CMl-UPikv_GZgziouSSf6lFZhDMxTwFK7bWgpMVgaUbgL7SM1jQltxBDmQJ9gN637CqkQojccHsQgwWuXz2qdD2rJVOwZ0kYfh9VwamEOEB1sR1XyYxIgBGeSNNwDGRqJTwbjKLJsJylKAfBVLqMWT0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=hSiSdHEeMqThTo0s--7gYQ7jS844yNk-u1s9yfR8mXyddU9kaT_wwn9X_twny-2EW6nM9FgH52xqcvR8JIpSP78gQTgRTIqzCbRFYKApjWZ2KqjQLZmfilgE8w0KFe4bBEtrTrlzGX6nkU3-6oupGELNY_rhg1wMZp0FSwyMG8wBzYSfImPDoyPDBTNrU_CMl-UPikv_GZgziouSSf6lFZhDMxTwFK7bWgpMVgaUbgL7SM1jQltxBDmQJ9gN637CqkQojccHsQgwWuXz2qdD2rJVOwZ0kYfh9VwamEOEB1sR1XyYxIgBGeSNNwDGRqJTwbjKLJsJylKAfBVLqMWT0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=fyIepRsqtNS3mzzuqZO1hySTLSsiMNx4GEdse4myalbVkaestrf4L0r_01yC0TXN2hsi3KP1LZuGGa6drIJ2shmQuWfKg5KS-2y6TAIjTHF73dZlTwBxtn7nH1_V_CbCWK675RfXwxmt3uJQ7eNlFexoYfkEHkAlfeRLZALqfKObv5iKVDhRrWCKQggjANKtG14RPjDCbVZws6xu8fQuBFMw9_i9USQ8xdLCQF550Xcqvd_0q3qOmXlA8nVHKds3d6qMeI6x8Mf5mJ5A2ejkfcxvsO2AzX72XSsIogMTwLx-YNzwklM85lnz2fzv36lXcY7TbPPEQ83meWIFbDzZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=fyIepRsqtNS3mzzuqZO1hySTLSsiMNx4GEdse4myalbVkaestrf4L0r_01yC0TXN2hsi3KP1LZuGGa6drIJ2shmQuWfKg5KS-2y6TAIjTHF73dZlTwBxtn7nH1_V_CbCWK675RfXwxmt3uJQ7eNlFexoYfkEHkAlfeRLZALqfKObv5iKVDhRrWCKQggjANKtG14RPjDCbVZws6xu8fQuBFMw9_i9USQ8xdLCQF550Xcqvd_0q3qOmXlA8nVHKds3d6qMeI6x8Mf5mJ5A2ejkfcxvsO2AzX72XSsIogMTwLx-YNzwklM85lnz2fzv36lXcY7TbPPEQ83meWIFbDzZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=LI_sESkMnemVpXV-IvknzRxD33FKvDijbGpCYkQT9lkf2zETeFi4m6pLRS7S7saYHCTKS4tF5ennIaToXaQSyb7queUcgMJYW5ko8YxHWpa-w8srrkv-Af4ZksWBq6Vqf6yvmq9d8SfHOCZoXYss2AYbZt1wQ1iq1V0ttchJGhp5kRT4c8qYZL9vKwMt1nxdYjxsa11MXRXYc6p-HukvcFm9SzpoF2QEr9SOfqRCIcdhRy-fuLB5u_yNW6VPZjoKeXs21qYeLWZ1eUzskej-vbgS-aa6MRfJRkVAt0P_EiwUN8pTtv5iOfi--NF0fEapIi3AWLEp48xmGIprSUvNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=LI_sESkMnemVpXV-IvknzRxD33FKvDijbGpCYkQT9lkf2zETeFi4m6pLRS7S7saYHCTKS4tF5ennIaToXaQSyb7queUcgMJYW5ko8YxHWpa-w8srrkv-Af4ZksWBq6Vqf6yvmq9d8SfHOCZoXYss2AYbZt1wQ1iq1V0ttchJGhp5kRT4c8qYZL9vKwMt1nxdYjxsa11MXRXYc6p-HukvcFm9SzpoF2QEr9SOfqRCIcdhRy-fuLB5u_yNW6VPZjoKeXs21qYeLWZ1eUzskej-vbgS-aa6MRfJRkVAt0P_EiwUN8pTtv5iOfi--NF0fEapIi3AWLEp48xmGIprSUvNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY2veqvpKPZJZ2mUhmcs3I9_fTW5rdUBGljVTQh8rCq5eOTWSbfscmEX5g6w9qEb7tMQP-jq4loY_7_VEQGLVsCy_kvv8-QRaRYK0Rg5efAV8R4gaIHmNr4eD0UrI_NGuLGj1KSzXpcmgVreYEv-ySWqpH4kzIj2II97Fj0Z_9a1i87LprepjYMOx5Av82oUFEW19xTuN-nszUM4zVtpXgQj7Ct6ADprYKqbsqBsq9wrVkG3OMJw4a9Uz44NwZIlGrFZdHPE9EzNxB0sgEmhin-Mabrzaj31ef8LLYd23tuYpA7IhA3hdnWd929JZBG5JYfb0riF8CGYIs-ijtUrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7yGYrxLRIhSwbE9RWMldHkmukEQ-Yi9UmH7SLfY_MtYbLQRhCKoj8f923FUbLqw_5B4Cur9Vq8djWFiKdq_6xZJLj2FTIWK7H-6Sc2KiOri5WoWgd7Pu-CVXPFzrQSmtx0upHbK2_-Djfx6q1ydPKI44kkF9yUwj2cCbukFEbWiPYFeGcZCrCrkWLAv6-UGXy9lYI7xozydDqRH20a0_P0oUVTn9dht_y8FVpUTOZWH2A6rr4pKWun7BoiE22j-g8CFNodfTkvsqEIochgZmLdnHtzowrwcAN6BHrcamLe8keGVrmEdV_7P4lxTjrfOjzyG634o-6AyLqZ7jOiim4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7yGYrxLRIhSwbE9RWMldHkmukEQ-Yi9UmH7SLfY_MtYbLQRhCKoj8f923FUbLqw_5B4Cur9Vq8djWFiKdq_6xZJLj2FTIWK7H-6Sc2KiOri5WoWgd7Pu-CVXPFzrQSmtx0upHbK2_-Djfx6q1ydPKI44kkF9yUwj2cCbukFEbWiPYFeGcZCrCrkWLAv6-UGXy9lYI7xozydDqRH20a0_P0oUVTn9dht_y8FVpUTOZWH2A6rr4pKWun7BoiE22j-g8CFNodfTkvsqEIochgZmLdnHtzowrwcAN6BHrcamLe8keGVrmEdV_7P4lxTjrfOjzyG634o-6AyLqZ7jOiim4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=GoKo3-fVZziAKu41pYr9RcKSOGl7t2ZJzDEtRqRineeuLbWWuN9mZgwFFB3OJ1SZp6UymNKCusrvJqClDWA79PQ4pVbS8Y23DZ1036no66Qf6ynlP99WmC8WT8CDlHrqg--2wlAdP_BlKJHblyMp2hslRp-UjW2e9rb0oDRJBOjINxwXm5KOC2BRtOlJ4MeWhcOPm18dh2Fu71UojAEGSrKzUvastC9itcm9dYc2-PKtUCDPpWGtL4WIDMOe5xeBmteFIHsoX_VEjA6ogmM7Q4_dKjO0oUEOguE-CdQqo-jHei-gIvSLC0kgbMHP9BMHPM2p6WTGksotMG1nPeUV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=GoKo3-fVZziAKu41pYr9RcKSOGl7t2ZJzDEtRqRineeuLbWWuN9mZgwFFB3OJ1SZp6UymNKCusrvJqClDWA79PQ4pVbS8Y23DZ1036no66Qf6ynlP99WmC8WT8CDlHrqg--2wlAdP_BlKJHblyMp2hslRp-UjW2e9rb0oDRJBOjINxwXm5KOC2BRtOlJ4MeWhcOPm18dh2Fu71UojAEGSrKzUvastC9itcm9dYc2-PKtUCDPpWGtL4WIDMOe5xeBmteFIHsoX_VEjA6ogmM7Q4_dKjO0oUEOguE-CdQqo-jHei-gIvSLC0kgbMHP9BMHPM2p6WTGksotMG1nPeUV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=ZzbQ7PLaIZ9-kIRx3EZKIfurtuGLDzr1sHZoAB_Y6lQEFgNkJFB1iD8whu1OkfO4CQRvRWm8k05tDP3dyms-tZZz_W3YEAqbuiGNiSXXH6Dqh6QR2yc2pQ1QgfFgQyFAwe5_-b0rgIMtN271ODACri_XG36d0jPHwbebtvEKzyKMSgIQ9Vf50gMoUAOry856aeo6Ik1FEQkSikJh5c3N4abzfZeyQrJbOG6cu6ezMzZ1j2i1VOxOyjiZdJL6YHWH1Ng2HKEsuUrcqj80W7TP1osISnn_QaJA7HmLXhphTVxd7mY8DXrBXx04yG2HjpfP3x6CwFXvlaCo9FZcV8dgua_UDjM8dAxm1sHKDIkzfZnSxKB0GTh4bPR7mAuVsIK2wcD0fCS2QYl_OncFz4g_GaHQDeQgwZy_mS08y1ApRwRhYNHEef-1CjC9kesM2ZzK4BG2RkzJlmXCukyVpDtgdJmcKlb9VCmq_LD-cPt2k5j07KOA18e9sLspA20j_X6xyUjAX2foQZ5R_V5-jhcdc1dgIEaEzd8VnzXv9AKxNvmvVLmHSKTqHCp7xNG3AAfomnXj_lsoocRXvhII6l_8UQy30rSDnS5s010fxcZkLRxbDzdtMdS6iUTKwWs83tH5GkrbieZ-7cdhoKPoh2ZOucJcdj255a5bEx_6Y4VBfRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=ZzbQ7PLaIZ9-kIRx3EZKIfurtuGLDzr1sHZoAB_Y6lQEFgNkJFB1iD8whu1OkfO4CQRvRWm8k05tDP3dyms-tZZz_W3YEAqbuiGNiSXXH6Dqh6QR2yc2pQ1QgfFgQyFAwe5_-b0rgIMtN271ODACri_XG36d0jPHwbebtvEKzyKMSgIQ9Vf50gMoUAOry856aeo6Ik1FEQkSikJh5c3N4abzfZeyQrJbOG6cu6ezMzZ1j2i1VOxOyjiZdJL6YHWH1Ng2HKEsuUrcqj80W7TP1osISnn_QaJA7HmLXhphTVxd7mY8DXrBXx04yG2HjpfP3x6CwFXvlaCo9FZcV8dgua_UDjM8dAxm1sHKDIkzfZnSxKB0GTh4bPR7mAuVsIK2wcD0fCS2QYl_OncFz4g_GaHQDeQgwZy_mS08y1ApRwRhYNHEef-1CjC9kesM2ZzK4BG2RkzJlmXCukyVpDtgdJmcKlb9VCmq_LD-cPt2k5j07KOA18e9sLspA20j_X6xyUjAX2foQZ5R_V5-jhcdc1dgIEaEzd8VnzXv9AKxNvmvVLmHSKTqHCp7xNG3AAfomnXj_lsoocRXvhII6l_8UQy30rSDnS5s010fxcZkLRxbDzdtMdS6iUTKwWs83tH5GkrbieZ-7cdhoKPoh2ZOucJcdj255a5bEx_6Y4VBfRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=cPsb2o60B97hKRy69_iVifllViZjhZryOr2cukVfs36MRnpUQJvxlNRCKB2m7EQWFubTD1CGbCQU8ltkO1mn_W1tvQ-OdRn00vAgwaTLSxSdwEVxbhvJGcIU3ooDU9_6_aphEEuEhQuLg3gSafzwrst0DPkOnSlEz_i50dD8G9nrIdaCBr8GXccNI1oRo9Bs_GC64VjIXuCO1qNA0qma6N-s6KsZTokUJ6EqEQ53gUW1byFKdiHHCpikxAoQT09XGaQ9ksSbRd3E_WVsB6oDC87qUrRjzU-SzMXfADkhMllxkMnAMzQu9NV4EHIXJXYnqs2Hyfs6W8rzDdIUwXDYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=cPsb2o60B97hKRy69_iVifllViZjhZryOr2cukVfs36MRnpUQJvxlNRCKB2m7EQWFubTD1CGbCQU8ltkO1mn_W1tvQ-OdRn00vAgwaTLSxSdwEVxbhvJGcIU3ooDU9_6_aphEEuEhQuLg3gSafzwrst0DPkOnSlEz_i50dD8G9nrIdaCBr8GXccNI1oRo9Bs_GC64VjIXuCO1qNA0qma6N-s6KsZTokUJ6EqEQ53gUW1byFKdiHHCpikxAoQT09XGaQ9ksSbRd3E_WVsB6oDC87qUrRjzU-SzMXfADkhMllxkMnAMzQu9NV4EHIXJXYnqs2Hyfs6W8rzDdIUwXDYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=KH_M8IjrcUUexcrtZfE6sEDF2KS9uU7no9dg2w4n94GNLttZWn1znKQtkLMFDjvB-k__oy973ouHzpmuuAJczdV-waXaFIQ5cK8hM4CHn_zzKCCe2VCpVSJ9jFTyOub6M5q7jfMSraDk37FHtqS0K1IPSowtCzEAi57CaRnmXM-_kEuwGpjg7nSx_lFgw7jyD72a25IKmOMlvOdkeazJIBPDx9aBOj0Sr9-gjlr7ojayp1EDQhtURttmp2YFVKsUZx7RaAxtQuok67LsbhOROG8qaV8Qd25yX-bo3Ij2rggO49W-tfetXiEkI62IuqvYmqKmQQLw4yHFujC0xjqpGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=KH_M8IjrcUUexcrtZfE6sEDF2KS9uU7no9dg2w4n94GNLttZWn1znKQtkLMFDjvB-k__oy973ouHzpmuuAJczdV-waXaFIQ5cK8hM4CHn_zzKCCe2VCpVSJ9jFTyOub6M5q7jfMSraDk37FHtqS0K1IPSowtCzEAi57CaRnmXM-_kEuwGpjg7nSx_lFgw7jyD72a25IKmOMlvOdkeazJIBPDx9aBOj0Sr9-gjlr7ojayp1EDQhtURttmp2YFVKsUZx7RaAxtQuok67LsbhOROG8qaV8Qd25yX-bo3Ij2rggO49W-tfetXiEkI62IuqvYmqKmQQLw4yHFujC0xjqpGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=sUnoU_picLxxY4FjeiRkU-ltGZKbJYTyiKL1GLOnBMhVUtwfN_sVcvStyJz0Zc-3N-W7ZLLOtGX8USIKgIn5D7J55ZEwU26PtAYJTImULt3F-AnygxlsTiDQZVZylOpbcPRq-Qt0lVOFBsbmFmVQgIvMOgMsxb7wGnErDQRPviJdJc8B7vZjLEh5KL3YC-bFxX0YpiWhVN0WkvJC_Sqej1-AaGDEkpF8JGbQYHEp_Qc1do6le0velPEjnDReNFnU89Qum6XWrP_ZDNs4PQm0lyzn0WxpAVGz9cG9GextzFCCbMjvolInMUEgZq5jD4CPrK257HF7xszXF6dqLZOYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=sUnoU_picLxxY4FjeiRkU-ltGZKbJYTyiKL1GLOnBMhVUtwfN_sVcvStyJz0Zc-3N-W7ZLLOtGX8USIKgIn5D7J55ZEwU26PtAYJTImULt3F-AnygxlsTiDQZVZylOpbcPRq-Qt0lVOFBsbmFmVQgIvMOgMsxb7wGnErDQRPviJdJc8B7vZjLEh5KL3YC-bFxX0YpiWhVN0WkvJC_Sqej1-AaGDEkpF8JGbQYHEp_Qc1do6le0velPEjnDReNFnU89Qum6XWrP_ZDNs4PQm0lyzn0WxpAVGz9cG9GextzFCCbMjvolInMUEgZq5jD4CPrK257HF7xszXF6dqLZOYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o29FlhS-S8WqohIe5xUZriOnV0PyKUz6SnDGILHqgxd0OWzePfOSJvxTsAAOYxy8qhDd07IRG91wYMVkqqkuQuT771U1LlWyzl5J-nWF8i_F6EMkB8sZoCvpNXs3wsCFVC6IygqbZW_slFnS6ehAe3B1wc-uDp8GuvcJi2rpuUPDM9beCprF0JFpJ26fTZLNGtaON47F8a6TFF42pM4LUmS4o2GOdN2hNIvmYWtKaNC42F74qMC-eA3MLH5j36Xg8CMkX_HmuTN8qkVxy2gdOcDwXv3AtQFIPBgM1DkVEjciv-TapsUiV7PjLuPW368PIgvTjwRAO98TObxB2HKDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dc_1oBEV3tn6GmcN0ViM9Mv10ZvRJb_rC5d6RK4g3qGG4ZeDN0NNbtYjOSsW5xEc9loIRonfWyhxjit4biP-vuO91jlg4N5sDN9t97IdMiHvekfL1OWO0yuPAO8X2bnU08hMBf54IFEDJjVm4RITfaHys7kB2rbCLd8H7vVff27n-eU-977Iva6OmUnzC-VWokSYheq6kP4TG60RcDduMCOFPhQGdS64CxBt6tMMNctDU9s4V7V_kOJ3cEpia2JycT0wk8oLJDuRczQoXUd_lkZ6vhyV37QbIerOHtfwtGCaHtik2h2VbsdrpoLN69KrF3Yw4RvxWVD-HrlJRQvbvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTBAikOB3n6o--5Al6lNhusJW4Tvos2XvzHljCoSoBPd8AV5oxsjQNC7Kz_i0hhgyOL9up1IGskrI_BRcxQ90nG-Nv5tipFjL-LpeiAwGTX-lCP1I-0EQVoFkn_nRq42nUtG3JoI_nz0HZ70kTf7Ffc512kjnvBHzcVz3fuNl49ltOyzzaCW2VP8vBrsCgN0o-WOtCe9dWKRlS_oA67dgng0hBzq22U5aSlDVmjsyCOuKb6GdjzrqdWe78sLGITWf9ByUVwFIaUfQHFp_2-D5UagoEJvp2zC-GB9nsMtSQ5ZlsoVfBMpb4hVGAcp2ds06vOQR86maz88b3tVfVz_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oE_8GLC5pJHqprk931BeyqIXuUZbqs4DfQtW5EC1iC2TKq9U_zlIYxmYb4uChqGc3z7q5e6DryFug9kRL8jqX6P4Y2VovaneWslRC904XFNpQGaeNVwVYeXchae1fDkolmlFgXLvgkzaYWCUGndjhw06pCbyTprS53gYPVcDHmUTGHLkPs65ll060JnwCYRIfcODCzRH33NsA4MaiYw_fDi5AdFnvNbyyWOWDisSLpOSfLo6ZZyeDXrw_2PXXqDdUHpeiXCpwHlN1PugsefGHuYygFNZq9Id8vLnuZa-spmwv_DlEMHLAoWGpxkvPO7oeom9p-sdoeYFPf-S00-3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhYs5Y9Gi1YfiFTV8AesUBnML0PLJ8C_Oo8ZXyCGb0ohOHcTsGiHTBWw4R4C-B_9R_YJXbtuNh0fXXF3yR1Im8maMIkZgoaPG2i4XcZsba4upuF66CeBCOek7u_OlU0jpFcxq5_rzTytXbsRQ5doJDFK0uryrkKQRs_w01JVdhhW5i2nMfEe54X5JFy-a_IrHUccfPK4UoAeLAaz1GM8spm6bTrxq-J_H6NrVHi6M1IgOdnxWBEJO6sjjKX061jNy_CuNaI6_DBkLbzUn49s1_u4KasB0E3pYuSY3Anpj3KR_IaavynINapXaGjGYLC52y1Zq5O8qrD_nx7E7G_tIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfKprmbTT6EuImVQ56ajwIoUDftJjlO3p8DhVEfiyoSwvMP2tE3I1YqwBFBuIs2JOXktO7kQmuX-PLmmJQjY27LUrhs4BrfQ91uje1u-f6wYTKyic_APoeD2eVZAhYBVllUvathPQiPScJN9LTcEQ-_7O6z4xu0_dXasj8zleScbdiMxrIlkImSR_NC-lJFZiS1Q4KrBqRMFtbcDRVvqyiUvOdt2rloph2uxHIgnr0Wp-9SLp8JLK-UG2ENud2NV37KQkmPAboN7N2GyCHOYwxbnoCDzdW2JwmP5yJl9ibeLot63PkSeTJHrmpRjL7j1UK0abnEVLCDH_eAEm1AdDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Xzobvgl_CWs5NXu4plIdxmLiZfhpM2nD6U8p9UpTU8E6oaFk27SFeaXRb7UqvbiIP3n7j_cbqg8d4CboptJ8dvcweVz4Ze79I0RN_C8H6wP8huysF0RszRNa87cvlqq3s6KxKBOPGLitCdimnBUfUZ-ZCuH7vYn9xkctim63fJbwvNTcE4Ta03ZNWjoIifbgHLkqedNqitO6B6ynnnTv2BUv4n2gGqN4cUqYMi8aKoLjAbUmeBlyGnZT1IeHfBm0e1EnEIQcm5cs88Ul4oYEJC4wC6KMgTfDJD7Ppus-Q1TC6T9cijqs01OfOsdMwWJdcxXre3bpu9ay75L1271MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Xzobvgl_CWs5NXu4plIdxmLiZfhpM2nD6U8p9UpTU8E6oaFk27SFeaXRb7UqvbiIP3n7j_cbqg8d4CboptJ8dvcweVz4Ze79I0RN_C8H6wP8huysF0RszRNa87cvlqq3s6KxKBOPGLitCdimnBUfUZ-ZCuH7vYn9xkctim63fJbwvNTcE4Ta03ZNWjoIifbgHLkqedNqitO6B6ynnnTv2BUv4n2gGqN4cUqYMi8aKoLjAbUmeBlyGnZT1IeHfBm0e1EnEIQcm5cs88Ul4oYEJC4wC6KMgTfDJD7Ppus-Q1TC6T9cijqs01OfOsdMwWJdcxXre3bpu9ay75L1271MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=p71CL-slSD4GX_e9DK6kbFj1HNgFz8-lfhyWyAqPOVEST6uKjst4pUx17NRdAMlhnjqEvGm_b3MkA8Bhvcow0q36z50f6tidllG8pBkVv76Yx4ZAxYXESJBBp1oY3CUuoKvWD4LLnDBHzh9x7RE2Y3ztaL2CGAZrzdUeIa06iVHfw-g6ERwrfi0qdevlQM9Hh_5zIWt6h4HEw9AYxzMHMWl43HE58kE9o0Y0TixTouOG4_yayUFhCRv7qbwBFGJpBjrcY7u_vmJAKTt2TUCaeThwf6wQEBo5OlUK9E6LYbJ51B4KicyOSjTPY7p6VSV1WMKeUJveaSFnY_yi3rqD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=p71CL-slSD4GX_e9DK6kbFj1HNgFz8-lfhyWyAqPOVEST6uKjst4pUx17NRdAMlhnjqEvGm_b3MkA8Bhvcow0q36z50f6tidllG8pBkVv76Yx4ZAxYXESJBBp1oY3CUuoKvWD4LLnDBHzh9x7RE2Y3ztaL2CGAZrzdUeIa06iVHfw-g6ERwrfi0qdevlQM9Hh_5zIWt6h4HEw9AYxzMHMWl43HE58kE9o0Y0TixTouOG4_yayUFhCRv7qbwBFGJpBjrcY7u_vmJAKTt2TUCaeThwf6wQEBo5OlUK9E6LYbJ51B4KicyOSjTPY7p6VSV1WMKeUJveaSFnY_yi3rqD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-8k-uidaU1R5Fcp8pAso7SmCr2z63kYU8xuK8Vtod-gqCk5mw9ILQZRbMvvs9uOV6D5nuERflBSxLe221bcgd9IL0L0iIAXe8RRHKmjBrMH5psXS06UTQUsk0p4u25k3e0Gnu8bXsf7aPF-dj87TMyaxkIC7ct3P1bIbQrMYs1jdXiCh_tYlQ4jNw55IsKy89-Iwyjt0DWuulvXb02ewUi4m3SIx5_Aldz_DEovxo12_v8yUjSHV8JdXNdogkYvXgfv9Hnsfcoh8OLa0f42cJM_evA1zatP--3SfLmQMTE0PnK9qYRn0CFJr_6f-UPARJxkFFoAhJvwH0-tV4B1dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9wjqnHY1eWkcoiEwMf0R9DoaPa_zBH9Njn2Q7nrRfRdS9Cw6BmBv6P9yEMhFArzKLBQBLMW6_w1zqqk-sPdCXFeOYvJOsBx9ztsYercZ9ce9TOZBePZmzAWt1l9ouErdgTFvn0Mt49JORroAtK_j3s3JbO8WBdQO870z38Y8ncWOl31Qiu_Q9qCtILxVX66u7byISV8PsUDsz_phIoCQiIPl3eCuY5zgdlWpZvCo3TGYiUJhfjQZFHUFOqcNahYagHCr8VviFgeh38e7Is7eUWjr7KAfUQchXcSr9pmP8F7EEqSrefwJhkA3oMGk3xnPFaMa_9QlN7wSVbsxpYplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=R5cpdZ4Y7WqiokBaKTDfDTs7_ZtKzqawSSgiAHPI1me4raWAZ68abm4BWoEVWBUNZyG6NgCoYpHDbOzNl8CTkW5Ro_faqFE6og18kdC3KJj2uoND6yZoQooCQb5G1aRkH9LVH0T9DpJ_Iqt4hnOTzuSTOhd2SCmUiu-t2kJIYPaX_yzo5sXdrelXAIGy1ZKKColQlhmzYfW2vJWOLcB7-RfzeUYMsnRx4FuMpmTOeGkK18k5bcfh-P0381FeEssYwwkDNEpLuDYhjSJA1mTxUJ5FMrrXR-XM6-E0QgyLRKmRxtLxfysZwxjHDBrjsJOsBe4xSVM0ILfC13q5Vd5w7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=R5cpdZ4Y7WqiokBaKTDfDTs7_ZtKzqawSSgiAHPI1me4raWAZ68abm4BWoEVWBUNZyG6NgCoYpHDbOzNl8CTkW5Ro_faqFE6og18kdC3KJj2uoND6yZoQooCQb5G1aRkH9LVH0T9DpJ_Iqt4hnOTzuSTOhd2SCmUiu-t2kJIYPaX_yzo5sXdrelXAIGy1ZKKColQlhmzYfW2vJWOLcB7-RfzeUYMsnRx4FuMpmTOeGkK18k5bcfh-P0381FeEssYwwkDNEpLuDYhjSJA1mTxUJ5FMrrXR-XM6-E0QgyLRKmRxtLxfysZwxjHDBrjsJOsBe4xSVM0ILfC13q5Vd5w7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=niLFOpTl4HVjweipW8vlOLHPwPLDdPryJDBxEzd97ftR3BNzDsorSIURl-IiOAcW-VyHDTBKmIq-vogls9e-LB6swotxpVIfsa5z7jNLYXWyIGUuocWMYTYmlHniphlp5HvRAA51CzOALmTKuxvRGtIH-jPHkU9rrj-Wryeg4Rj7Qo_gV-IXAplduFGcTg638_oTbaO1L0tcq2QcPNdQCjxKJV9NghGrieTMgClYSOxQoyTqTBfMbJKbG8ivE_qbB0oQX-B0ceaPU6Ng4y5-vf8IwWsLEpPFBuJws2irRHFezMImHwofwUG2o2-iCMGlsstn4N5rDduZMVqMUOVB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=niLFOpTl4HVjweipW8vlOLHPwPLDdPryJDBxEzd97ftR3BNzDsorSIURl-IiOAcW-VyHDTBKmIq-vogls9e-LB6swotxpVIfsa5z7jNLYXWyIGUuocWMYTYmlHniphlp5HvRAA51CzOALmTKuxvRGtIH-jPHkU9rrj-Wryeg4Rj7Qo_gV-IXAplduFGcTg638_oTbaO1L0tcq2QcPNdQCjxKJV9NghGrieTMgClYSOxQoyTqTBfMbJKbG8ivE_qbB0oQX-B0ceaPU6Ng4y5-vf8IwWsLEpPFBuJws2irRHFezMImHwofwUG2o2-iCMGlsstn4N5rDduZMVqMUOVB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=cW2OpO8FEgMyUpxGb69-Wy7bCDbBsjeHaH3xqVaiEQFdzh1MabLCUOgpEBPhBw5ZE60nhhyVNya27cDX_n_nPfxwRy1Mbbs7odux9ykFQer8l5rXH6cC7TkO17ksCgqaWx_rf3xZVH1hf1I9W_4T9a2dSWhF8TjE2C8brbxCMFbgPyTRD9gltqXCJSRHO2Y5PAz1fIskUAbmuo4newdGHoqRGy429YYWI9D0akMBiCfT2XPypvB7MET-SI-15n8x3g-98IvL5QoTeuGy0uZk6xFG5uyQKmvv-AGnmfP2snovtNGozWSlGoCfHVN4T7ExoUS4Y1Xa0MrjJyutTHOIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=cW2OpO8FEgMyUpxGb69-Wy7bCDbBsjeHaH3xqVaiEQFdzh1MabLCUOgpEBPhBw5ZE60nhhyVNya27cDX_n_nPfxwRy1Mbbs7odux9ykFQer8l5rXH6cC7TkO17ksCgqaWx_rf3xZVH1hf1I9W_4T9a2dSWhF8TjE2C8brbxCMFbgPyTRD9gltqXCJSRHO2Y5PAz1fIskUAbmuo4newdGHoqRGy429YYWI9D0akMBiCfT2XPypvB7MET-SI-15n8x3g-98IvL5QoTeuGy0uZk6xFG5uyQKmvv-AGnmfP2snovtNGozWSlGoCfHVN4T7ExoUS4Y1Xa0MrjJyutTHOIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=A9zy3F4xaKfICcW4QysS6M1vp7mHX-ddqKhj4JAyMxhyYGjsHcTckbrzpHkjrcu8GVaVgLv-sVJ0dZzhzp9C0KfzrYZ0dN0fFxH5bhWSKQH4Gm07L4aarAhG7AtH6l52eWXvjNGiDYeUEJF-uN_24T6K8zyZlAI_WK7EnkljU-tEsEIm553I1qhQ-hrZ4FOEd8sBWSil7QO96643Pn46bh3NU9APoxffSy1eBjhPo3nIEhBIEkkMlP52Fwse8qxn31Ys10ourmSR_UApnioRQdgh3MLVWcgz2MdNt4ZdmR8uF2ibVy22IM5Ds45ZWYUHlRnQwKM6YLIiHQtM9UxD77aW1mcbE7II1-qTDq7hTnTw2qzQi4bairXzN_ZnN7DCLfQ-0gML7T1bQwOA-RFJYkYdyevFJFHWDtNRdMMNDniTWbUzylPok8tECcT1tJ1Lcqu605WSu0-LCl35siF4TAPtMk4IOeXb-WqBr-DD5rKQVoD8J5sGeb64mbvk4Ay8yWLycPU120suAj0iRY9dN8UYccp5bxDV2GhwMDwH7WzKc8Ymj_92khI-fSURp6GOc6TQmEgtlKB2xK9YITftIqBwwvIGs5yFNRf7acgZq4YAfrTNe17_loaROzn68ZdPoFBjlWemp0b60eUtXx0iRegwhtyyP9HiBtpemC7gqYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=A9zy3F4xaKfICcW4QysS6M1vp7mHX-ddqKhj4JAyMxhyYGjsHcTckbrzpHkjrcu8GVaVgLv-sVJ0dZzhzp9C0KfzrYZ0dN0fFxH5bhWSKQH4Gm07L4aarAhG7AtH6l52eWXvjNGiDYeUEJF-uN_24T6K8zyZlAI_WK7EnkljU-tEsEIm553I1qhQ-hrZ4FOEd8sBWSil7QO96643Pn46bh3NU9APoxffSy1eBjhPo3nIEhBIEkkMlP52Fwse8qxn31Ys10ourmSR_UApnioRQdgh3MLVWcgz2MdNt4ZdmR8uF2ibVy22IM5Ds45ZWYUHlRnQwKM6YLIiHQtM9UxD77aW1mcbE7II1-qTDq7hTnTw2qzQi4bairXzN_ZnN7DCLfQ-0gML7T1bQwOA-RFJYkYdyevFJFHWDtNRdMMNDniTWbUzylPok8tECcT1tJ1Lcqu605WSu0-LCl35siF4TAPtMk4IOeXb-WqBr-DD5rKQVoD8J5sGeb64mbvk4Ay8yWLycPU120suAj0iRY9dN8UYccp5bxDV2GhwMDwH7WzKc8Ymj_92khI-fSURp6GOc6TQmEgtlKB2xK9YITftIqBwwvIGs5yFNRf7acgZq4YAfrTNe17_loaROzn68ZdPoFBjlWemp0b60eUtXx0iRegwhtyyP9HiBtpemC7gqYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=LiWnmLTchF7tza-aSjXefkiadO7Z_3Yo7H-XbUtWOMIvdlR2V8B9uYYtot14bDg5nBlF4ICG61NfhUlBFL6G798rl0mh3q-qw0cU5AFPMGPYR1Q_oioXahO6g7K9vC1RhPVwZ2091fMfUvXseejwtL71BcGC3otc_JDql92dv36loxLnJXFt9Vjrv-BZMFk19FmaiIu35TW-yv22QcY6FB2xW-1wYzClmzSOnTc_0DSDYSGMiCSi8nzb78HLmeLm1MGYmCbOlhwSdiFkvTu2XxmXOgFymssDeSRZMGIGnlrhgEWUMtKq6pd6lPbHJb3DIFE3jVdSPuvGbRxkCh1akl1ON38SLU4rtUYiE3iqyAr8GCSUwx2OEo9unAiNbR4pjm_AQDQKTOZyKG7wy-cvczcKtE4Mbgm-FDvqAMLrd4ZWabVB42lW2ODf8oYvQg_trvIYfQazhS6A3JeIQcs3QKs45ZIzJ78JsAEUZ7Qk1tAL200mfUAEnl2-YmNeVE3VbXiDZPALHWw8RtTKKhB1M54cc-2i4SCfY2tAvJpMAM14RGlfk8O9Eyjyyv-8ajwq6J31NB2t416XueiM7acnEgRwT4YiP-bGhkodkVbeujrtJKsqaEjWkV6aBXedm2RXKSDVIsbSY37txCHuf-S4LFcHiyzQAksn1aAE1NbClvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=LiWnmLTchF7tza-aSjXefkiadO7Z_3Yo7H-XbUtWOMIvdlR2V8B9uYYtot14bDg5nBlF4ICG61NfhUlBFL6G798rl0mh3q-qw0cU5AFPMGPYR1Q_oioXahO6g7K9vC1RhPVwZ2091fMfUvXseejwtL71BcGC3otc_JDql92dv36loxLnJXFt9Vjrv-BZMFk19FmaiIu35TW-yv22QcY6FB2xW-1wYzClmzSOnTc_0DSDYSGMiCSi8nzb78HLmeLm1MGYmCbOlhwSdiFkvTu2XxmXOgFymssDeSRZMGIGnlrhgEWUMtKq6pd6lPbHJb3DIFE3jVdSPuvGbRxkCh1akl1ON38SLU4rtUYiE3iqyAr8GCSUwx2OEo9unAiNbR4pjm_AQDQKTOZyKG7wy-cvczcKtE4Mbgm-FDvqAMLrd4ZWabVB42lW2ODf8oYvQg_trvIYfQazhS6A3JeIQcs3QKs45ZIzJ78JsAEUZ7Qk1tAL200mfUAEnl2-YmNeVE3VbXiDZPALHWw8RtTKKhB1M54cc-2i4SCfY2tAvJpMAM14RGlfk8O9Eyjyyv-8ajwq6J31NB2t416XueiM7acnEgRwT4YiP-bGhkodkVbeujrtJKsqaEjWkV6aBXedm2RXKSDVIsbSY37txCHuf-S4LFcHiyzQAksn1aAE1NbClvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=GKc8cjl18tmqFJFse0BGxr-u6eFlW6THoA5b7gDgBn5nCZspFvtYcRD3aj_LbI2I-2hZXvwaOQgteMiKg7kiP76CMJbpaEgpL9TNNgUtYnq2Uhteo8ivq8mLDroRtcImfuABDRCLSVQ29rTHNh-G0BQox8mldeinHs9zaV5A8gT7rAl5gMbnQFj6W0Vvh5CYNHRkaf_L_vcSce8VmFRiVqOWaReePtokllszNRaYRA14UkqI2PqyNZuoptMqwYuJX4V6SmqrC3ENQxpLDejhSbVz63PVPo8i0XLc4teFRiQp7rynYq6W955vJzzMzkFrP7G6jjivsMdRTLhU1hsz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=GKc8cjl18tmqFJFse0BGxr-u6eFlW6THoA5b7gDgBn5nCZspFvtYcRD3aj_LbI2I-2hZXvwaOQgteMiKg7kiP76CMJbpaEgpL9TNNgUtYnq2Uhteo8ivq8mLDroRtcImfuABDRCLSVQ29rTHNh-G0BQox8mldeinHs9zaV5A8gT7rAl5gMbnQFj6W0Vvh5CYNHRkaf_L_vcSce8VmFRiVqOWaReePtokllszNRaYRA14UkqI2PqyNZuoptMqwYuJX4V6SmqrC3ENQxpLDejhSbVz63PVPo8i0XLc4teFRiQp7rynYq6W955vJzzMzkFrP7G6jjivsMdRTLhU1hsz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X830p3xfGzUYRcHxe-IyNPlKGQl4KVANSFGsbKHj26kn24nufo2NIh8F2WbiWjwr9POsCbPeO5WslnuiP-3y-5KUBEdRpmjV90-EpdvOwD_9X_SUMB-uN5b6d8_hOr78DjvzWAZB3uFYS-Cp3YtRKEM0PO9rv6ZDk52QBW43yOHYMuy1pXP2xqgL_Q29vyPhJDCuDthaVNfUqPvNBRdeCsudu0X1A57R6cq4OCP2byzMv_GwtrErDg0Lcp1PG7NAvKvnJFdls9thH8OckHLSAnntwmT6SKGIt-MmgZsVL-fTEa3k31r8WDLyMKBTEoayJH8UdJ9xobPZlSQAkboGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOLavSiAFgiW0ba2yxKwPMgp-lhVzH7SnWa0uKg_5eV2_N9x7Od6qwuZ0jp-LTLM6yM7iTSG4zzmikwpuMWJe6TFl_J3OJM9nW5YKcAYOR3x3U0y0CuSTNu2SxcsXu4yXGaw5J3bpe4ypOQt5mk1VYzEEjvSmj6uTw0W37cdJn8MFg2zHn7XcSD3rvl6F0cCuSTkJI4qPIIRcSRg6HxF3bPahQ1LZYC6lHpWm2itu86aWvVCmQm6Jh-bVzZGfUXUXLJDZ19geuNKhox7H_s1ZLpbAIh-1qlTkwYGOlUvK0UjZwXKgykb1E1nfS4oN3jJV5_J8HKhPgV6RyeyTTh1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=f5iS6IK0TaEnhohKbA1kC5XZ7ONoW8Rzvmgpcq1tth0OYBAEyYG0mBgeww5uMzUL2BdldO6Ipl_2Gy9Q7KGFOQEcjKECe99AIwShX5hOwj1sqeuP3Q_PamSK1m2nZlIridMk1770R9otjy3D92gt5lk8kQ95yw4R8zMy-xTAsBY5lSn9lFCHDdwn0sWWI8516FH66jhdpziI3ZjOvEdOd1_OMCH_XCaeuyT22xt-wAI6_sjqd0HtNYO5PZ7l3nEVDCeMkQqg53aHaG4L_BgIbtN5A60RXuQkjzA0WKnk_yu5aBix0Ig0aYvR_pH7tHUWiMnsFNzmYBPxVqwEHNloJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=f5iS6IK0TaEnhohKbA1kC5XZ7ONoW8Rzvmgpcq1tth0OYBAEyYG0mBgeww5uMzUL2BdldO6Ipl_2Gy9Q7KGFOQEcjKECe99AIwShX5hOwj1sqeuP3Q_PamSK1m2nZlIridMk1770R9otjy3D92gt5lk8kQ95yw4R8zMy-xTAsBY5lSn9lFCHDdwn0sWWI8516FH66jhdpziI3ZjOvEdOd1_OMCH_XCaeuyT22xt-wAI6_sjqd0HtNYO5PZ7l3nEVDCeMkQqg53aHaG4L_BgIbtN5A60RXuQkjzA0WKnk_yu5aBix0Ig0aYvR_pH7tHUWiMnsFNzmYBPxVqwEHNloJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANKr05debcBp2FUaCCfOrgYFBb7UoCPAgwGTXI2NmVooYggj42Tzfll0FvfDhaSx7JezU_8Q6vzyevQTwGUXIzqPUlxGDA98KTbmd9UgATftG1QyaEVPCO5sZzPzJ884csLnZ2rZLsQjBf9v1X6_R9kzvG-GWSDNuLZ1YLJ3dtf_PZFlSwsdnUcWiAev6tZW4J7fwgTX2KMAv9ym0Zj30j-FGGhNTPtJGbugSbXH2iaJBBO2wbKe41zqVvK9xlrHete9loge-CHWx8qiCqx7BQS1vIMk5NqGfxdAIFGcZsC3tKZ2m12eKok_lywx_IS1vBQ9w8m18JLOMtOA6KReyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmt9aFrrv2TXx4gGq90UiIHJpVghgSv95QYymLvVmfKbbbBrmrc5tqEB97AeEVd6xUnIrS3BDDzDNexgYWsh3Y5K-56cQmaSSL8bj3avrTRuzPQdjKHH9s6q-s3M3J2ltPE7i1FiaZe8UuKlGTnYoWOHdlhv-Cr3znzn0OSm6___lFJ4a8DvtO2RLBJWNzXnukZ-k5qblWsE5uMd7d3G1khIFgvrCEbfdMJavzyBIrX7HqS4PrgKq-mB8t13Gm48bBGaNfo7RMU6k0dSZetIlTib1WcLxm3rNSLg8Zln2qbX82k8W3ADs-yMRfS4xF3N9M7uEHXFN9A0zt7mm7rV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2DG3e5_VCR1orUyxAegesNaPvlOd5Gi3fBeIhjNn4hKH6fjgrRYpTTqedKWnzSF-YQBq33C2Hb0f3xWp1cfiLf-jk_PoZPF7HWwaV3F6nFKGPmNRzyoQV4MZd-DhIgMRI_OzNtkmNee8diWJdPwVosJFIUV0oveovLwJMHcvW4xZefvYsCISO0c5oTw9DMTq0n9vj7MiLfr8cUbT8LxhjjS6rga71K5Wo6kaaUOd8i_bmmXMCpDnSL45KXlOc9EYg596O_eRx28QBcBDy1S_d7qAl5I6ZC_R5A4M1sI2TSj3vQgCGvqtP1VKZSGCkfoH778j_UPM-U7uBtq96Rr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQM6GJ-UrVHEWUmOlFnGMcMTFJ8o7thOEwH9SfiCxMfxSwgtmFHq_zwb99lI9UUSZ_DKqKnHjuDVfLbtQd5j9dVL0a4lmjWkXKpdR8ihW5PB6CclcWhaELwVFONRdMzYMcx2y-oElTl7Zbc21Y4hs3Z-vUZ7c1tjgz7kYZOQWUai1_jlInuAD1LnFt9laomyScSKo7ZKWW2SSJBo9zBGy5X4ObVbMyzk-tGj0n0WlDT1iKAJMc-1nG9IYsMhjnTuMn_DagxUluYee7TNb5w1EjBcYn6vbVOVgnRAzSFvg33SDMyETo_usDKHtgJ02JbHn_f835RyYy8Bb_-OsGBRmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enfKOI18s_FxvhRJrukwP7lnVYRo7HoNNoiDzlCDGloJW7abCvkd0W93gxFBaMF22J6beHalpTlComempIQUChNox5tBZBKaAvcUSCqe2iVJrSYguJAkDzQ85RBG3aois-TsD2Y5Fp65BTAxbRWeBoEsd0i301os4NOHqZjG85Pvd4b5yfVWKbTx3KkN8Umr0G333z5EDhkjKISSkZU6NljWi8OfVmUrdOlQFqEbCXf1mxKEzah3rV8La7Y63pQ3bO-Cv5Cpx6FeSG5btuVFnlK_fXV0Zsjh1Op3STWrAZ68n7_G-64FofclZjoVTuqrd6hAfdihTDTAgHpC5jaHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsG40o_geFtAp2H0bJVHQNvej0s9QYFnoHw1oapz9idj9SSfxLzAGOxs7Brc6ryKIO9buWcZ6ifbIjUR7J8NzWgSPcL8n3Jvfe-mfn8xftXqMSvpuc7N4-Vspq4UHOVQkgN6S5fI0jU014KLGD3HjBpQfdNGDvfrOY0RvmxonuBDdCVzypFM7qT9MeRuyztFZe_ukSmoNsEI0Ecdl0qCk6mkxRGPx7GF841p3vSbBPLx6M3F9gmLCCaPpJl9fnd0gIZNVnPTJf8Ik95GJs-M7oAKn0nUyaLvT_rFv62PPg-14z-NmBpizEyU8ltUFcI8ChKoqc-qHZmw5gQ260_hUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3fEP5vKOZaKzXkIPXPJz-VwKmbPg2N5cIz8lZLuzV1ftQcOC0vAiYIOIEMpw5ed2X9FoKK2enLV9ziNhea-iFn4PZ0OEoyqzc4WsbEP5Y8KFm4elLqEJIO4y7-GaCnk1_zLNf5dNhqqzlDP7goOmHqHQG9BRpwh5cBr6ke0ukMax6CRnerw2mUE-x57t7ewSC5YK4aMZ6lIuvordC32i-hPuLJ-98CdwhZu-kSlRwGhcQo0e_3S_UVkp1zpZXsiZZ25tb0K98EeCNg22HNEblqa5B17wbvHElOR-1ucjL7A5Er_1LPeEsvfDQpueYKRapmyEMwTSG0AOwK7TPD1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcKiYnRoCnS8vmdCZmy_C_jvRf7X9G0ZizO5KS5wkaO-6pf_heBQ-cq7VVhqUWWZ7xbXgKh_PEHzWlVpf66L3vxBB68p2sOkOChJ3nBk_yXRQdBFsEyWZnlCnCK1A22ZG5G5zqywd4y8280dInmSamda4FW__wbDtGJcxcHBc-nQp2FGAub_MGhdwdqkwVTyms9LZ1x9LIO2CkmTnTF-FDpyp3ZHsApR85HX4OGDer2XJt0KzdBnyYTUMy5rulppsF3bs1nKJmISdHuj4KR8ZqdPFjhijznjuKi2fdLDafiorgw9ogSUY6EEP90FUc9oXYtElGDe20ti-mlRXgCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6fO3gyJWWi0ekCNNBt5jGNnIJMqffKsoWuLD8fdElYzBqxlqBPaS1rXakQnYfM8vhxjOd2aamuWxemZTU3mB-JYpaXZuOwEjUy_990gm_-p9nfp6sdKO2D40ekvBe0qpLNG7c-PAWbqqi3nRHkdHl9SFZcAP0z7iDNUGA1eOsA9UHFRfbIaHQLXhJLKXVhKJHTAzGTCs97YJiac6FsHTGSGZnsBNmQMxXGWaVykxB-0O73e2j7z6WlSE--UUta32a3bSGBI4GYz71NAYoMDON1i6uOcp8Yx6vLD9otnIwmFzKjZew_BUYr_oCMTgGsOH1643zu1CXBNw5sd8iPxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMPioRQNg9fVazrF6qmzq3Zw8ExnK5gXFzWM2RLEri9_64jTIY0erXhHgxEOqRYcoSy73vp0vdRu0zzZiqABa-97RjFzcTWF5kdZu-Kb2-ox9MuYmWTlybResSuxw3IbVFm5tKIHbgRKkb3YGY2R9HigZ5OXhjebvxfKz0-38YCmm20bD4nU0f5OD0O_IXdJECwabiftwChNI-1QV89SLchJJs0dzlzXlLdUelSPu5qeNaISyOQ8pYDYoOJtgmweMzZqCblSn8rQ7_88XuyOCldQvz9NN1b5JuTAsJMYsGWGsP6syGsdAc-hwc-5Vp0oA6TIbKcq-eeQMqZgXWvTkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI8XXn5owOOlHhAn2gS0zlu82PdV4e-0JdxNx3VAHJz5MWAyzcCvtNQibsjumdIxR2jW0yzT-5U8YjwcJjexp5ivoGphQmdQkk125D8BU7irxStmwlOCpUgH5WO0kjC7ArKvxYDl7c_-2M8ADC2ZdzZZTrqFF-WepbDSea8mtvuImlgjzwet-rcWXfhPO50JlV7oIaqMmPzB2enqfCgUtYAn1-nz2X6B1eUWfAuutaGNT7g87wESW1NwziZF2MOMavsxW-zmsVFg_0YI2eTdIpo-JyFkaPa1PnQUoZ7rOIUTDlxEs7T6NZOBe6hfCo9jqc12WBAJZ_ja_KVp4cpQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=hMTDt4nZ0GggxECQixF1gw64Wp8cxqO4fDiryd-PlkHQUl4PrMFO-yVtA3vICSdtLIwID8gq32iCFlu30XAlS93Ax_q2hTDsTHhog9wAP2mmQ_Du99a_XnQp4Ivcmw2E5-XjWZoKpvoon4Jz5ZucapakPKdVjjcBYVava4Jere4DTI9yhcheqx6fOzrTYD_rXNVui35Jrneh0qJW5V-ia093E6r72kNBUO-zf9hAAQW5eJNP1yWNSOB6jdBz1lZjRke3rqAEjVU59u5kn2qE45YF7_XGqBx6Ju_EyXC7iarHY0D5KJ5teeVVxIriynkOaiiF9yCPvf_Y6SUCldS3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=hMTDt4nZ0GggxECQixF1gw64Wp8cxqO4fDiryd-PlkHQUl4PrMFO-yVtA3vICSdtLIwID8gq32iCFlu30XAlS93Ax_q2hTDsTHhog9wAP2mmQ_Du99a_XnQp4Ivcmw2E5-XjWZoKpvoon4Jz5ZucapakPKdVjjcBYVava4Jere4DTI9yhcheqx6fOzrTYD_rXNVui35Jrneh0qJW5V-ia093E6r72kNBUO-zf9hAAQW5eJNP1yWNSOB6jdBz1lZjRke3rqAEjVU59u5kn2qE45YF7_XGqBx6Ju_EyXC7iarHY0D5KJ5teeVVxIriynkOaiiF9yCPvf_Y6SUCldS3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Ki4c-UBpyPJ7wpJTN2HHQvL_R2gF8o3JcoEZRHwlLmCz9i33Hdp5yZcezvj5csaeJvtZSa_u3tCKBNiccWv_3P84AOG8urG702Q_rdlGZyv7yejvMlj2O05dQ1pob0UtW1QK-yF_ECSM_tBkg7arXN3foUXPBY6JHMd8jN3VLPOvM9SmLi2CJjVGwgD6gKWPJjyxIZDfOY0Sb3zaP9GLU5AqTw-VJgDH2o7kgcq0tpbzH_NSC1bQ9rlt4riZMv7jOVNawLK0jVAVI0E4wq-1hhsp17clA3o6XbMHgpBMX4hzYK3MWzxe_tqFI6UJR5rwQH8YSKKs0p5tVIhUil9w1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Ki4c-UBpyPJ7wpJTN2HHQvL_R2gF8o3JcoEZRHwlLmCz9i33Hdp5yZcezvj5csaeJvtZSa_u3tCKBNiccWv_3P84AOG8urG702Q_rdlGZyv7yejvMlj2O05dQ1pob0UtW1QK-yF_ECSM_tBkg7arXN3foUXPBY6JHMd8jN3VLPOvM9SmLi2CJjVGwgD6gKWPJjyxIZDfOY0Sb3zaP9GLU5AqTw-VJgDH2o7kgcq0tpbzH_NSC1bQ9rlt4riZMv7jOVNawLK0jVAVI0E4wq-1hhsp17clA3o6XbMHgpBMX4hzYK3MWzxe_tqFI6UJR5rwQH8YSKKs0p5tVIhUil9w1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=rVPVFJ6sYlsdgQe39wCbjwFQBqzNrWQEECWmi3r_ROzTH0HjsNfjg9yFW89Jh2r8b-6JgMMJKfZAjN50Sb_wY2hvoJ2Ju0oV7l2A0Ajh6NO8JleXidN8HM-_6M1B-R0RPVAQS_cqLks97WAQoCJ6wu2D2pm9aENdOJNBbsV055IL1oB9I0trEvrWtf-OnAOFHFARs5Pl8-W5l56VXk0xf4oaEDblTtB1O50ncz0u1KefaIR9qQ6pKSbYD7DX9_8C3T11zZyQMuejTvQZL2eRQru9iye69eVuBARHVIn0YVI-lXA48NnavP_BViFRE2LqTaL2xjw1lf_BJ2bNXt-p8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=rVPVFJ6sYlsdgQe39wCbjwFQBqzNrWQEECWmi3r_ROzTH0HjsNfjg9yFW89Jh2r8b-6JgMMJKfZAjN50Sb_wY2hvoJ2Ju0oV7l2A0Ajh6NO8JleXidN8HM-_6M1B-R0RPVAQS_cqLks97WAQoCJ6wu2D2pm9aENdOJNBbsV055IL1oB9I0trEvrWtf-OnAOFHFARs5Pl8-W5l56VXk0xf4oaEDblTtB1O50ncz0u1KefaIR9qQ6pKSbYD7DX9_8C3T11zZyQMuejTvQZL2eRQru9iye69eVuBARHVIn0YVI-lXA48NnavP_BViFRE2LqTaL2xjw1lf_BJ2bNXt-p8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=KKpV0eA9-qmytuUBSP7aCzupxKNessUeIupEU2t7OU5qVGkuWLcAWWDB3u0Qtki7MhL08nkboLE89C_9QwtUBSZPHiMyPw6d82bNvIWtEdisfpv01GDh0_G1vEWkL1A6s5v-e5_8yud6XGgrhYDu5-Nb97YJfIot_imP41MsoiD4mBKgjVjvGgZNbR-oF3nbgwGNvZo0nWhDpAl5WRQ4qR5b-j7ZJq4yLQujHBpR00UcRwbaYZZvOdHbUNF4gCcdXFoAL_aBFPwTTSTcIBet8n8pF1Dm1oKKmbIQvLEWFki3cVjceGNEIcF8_yLmbskwcp_lo-uSk1VFSL9wuqSvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=KKpV0eA9-qmytuUBSP7aCzupxKNessUeIupEU2t7OU5qVGkuWLcAWWDB3u0Qtki7MhL08nkboLE89C_9QwtUBSZPHiMyPw6d82bNvIWtEdisfpv01GDh0_G1vEWkL1A6s5v-e5_8yud6XGgrhYDu5-Nb97YJfIot_imP41MsoiD4mBKgjVjvGgZNbR-oF3nbgwGNvZo0nWhDpAl5WRQ4qR5b-j7ZJq4yLQujHBpR00UcRwbaYZZvOdHbUNF4gCcdXFoAL_aBFPwTTSTcIBet8n8pF1Dm1oKKmbIQvLEWFki3cVjceGNEIcF8_yLmbskwcp_lo-uSk1VFSL9wuqSvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hlOLgxe7PGDrP7gki_BfPwF7ven9xRQJcf1ZHa2G-GadnyLyk119Lc_sUvweSIOosqv4RUJcK-Is9L1cIP78fu_2NqalxJYU00urRISHCVyhuGdvplE2XkvecS9deomU4R5TWeJDLlqQ2HlbHJzbinnrH-OobRzRLB_PprdvRZa__OuiPYm6ayhZGCp8esQKPYSXSmbBs0AVWelPWvnE46l3dJkp31lKyRuaPvXqYYUjtvMV4pakSlypltxZmdY6n94xQz2B_qQ4y7lFt6IAzFrHLXSGbzxkJTWLO3dg-sNq9u-hGXqxaxiLkwy5DAaKy_QJCzrElC8LKNifeZfi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOVUG6TwsVYEsF6lMf4yrwZl8AJ7T5UwNDNfPMc3hWocOofwNc_31MowBI_EIr-Jr_ImBOO2YQwwt0DVbbEQnKvqCQ-H636KyxCqzMc1CMyXYkdrVKc9Ynqn6xK5ppOBFussdx-dL3MR6MxK_uomgiHGiaBMPniEq6-n82buzt-fPGFPp4AdWwEdaN0-mgxfaJfNr7Ah--cbEy8Ldhu1S2chu0LxSIv3RH1_MtN3assjqMIp5iu2Qlmsnpk2xQ7S_q-SqAFY0vSi_CNErNJv-C8Ys2QvS8F8OnKBbyTQgZsaDwb2pAURi0E412DEFKWXuNFUbS0c4G7ncThLACLLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4NIQWeswfq5_MOSMSjTQ95Xf448onVu_yD9o-29puZAKCKxdu3cnGQs3ckfEEh_D4z89ak97QyLV6jb3J83O5qemYlTGG1USlEaKHxWUcJrF17wXhb54B8XCqzPNchJZAJRL8NzN0TJsuCkLRQjz4MaGWW3ePTSgLBI8X4yuT-A2Pq9VBVHUK1f7ftD1RBWMn5UGqqslgAmO9XvRExzOkmk5zaHiRIXXlVZofA2nLMakaa5bx4NtZTDeehD15XqJ2vKDpPFd-LwXbKv1bO47yjfR0iBwIWhb_weXhf7OQ5DQx4sZCGT-oV0uhqvb8vyb-nPTR9EZaVK-X3TOLoE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=QZRRocPER42J-1vw74p6XEOiP5h2dXyMP2ppYNsNGgrGpYSsx9GXp8YGpjquvPKoGqt3NAI7GZ0hK3BhMv0mTUSxFdCNk9PwqlKYWcfiUA4kqEazN5Ds6kGNRwqa2-J5iapmx2_UCbcHdw-JcNrdHfVXi5PJfMP6d6vrJlg1W_vRmWXN83nWlbwxEsbr2ocwcCTTa1rXsLJw2n0ZiZz787u8mZwyacR-g-OZqABYnIzX9SqQU4Bh2iWAHrskbkp7qC--Uy9zm6iPTyVZCjNKdCEy06qrHABPrq5asu14RmqtZhXo1gvI0wqWGFK4EGCvce6K_W2vj19n1e3_USGtYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=QZRRocPER42J-1vw74p6XEOiP5h2dXyMP2ppYNsNGgrGpYSsx9GXp8YGpjquvPKoGqt3NAI7GZ0hK3BhMv0mTUSxFdCNk9PwqlKYWcfiUA4kqEazN5Ds6kGNRwqa2-J5iapmx2_UCbcHdw-JcNrdHfVXi5PJfMP6d6vrJlg1W_vRmWXN83nWlbwxEsbr2ocwcCTTa1rXsLJw2n0ZiZz787u8mZwyacR-g-OZqABYnIzX9SqQU4Bh2iWAHrskbkp7qC--Uy9zm6iPTyVZCjNKdCEy06qrHABPrq5asu14RmqtZhXo1gvI0wqWGFK4EGCvce6K_W2vj19n1e3_USGtYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhYLVS8ElxdxRa0gjmvgNrpHF5VtXTwdekV59gxDJidzY57iVhgBWAtwr2A7j6fauGqEfhoKkFFtpwSVMRfDlg1C8-XSsMd_CbLDn5gU04fAU0Z-lIZro1B5QubBkR9bY47n6AABl-MRkxjMjf7_vT14jPAouEc785ISJuS1M8LSfLqnm-u9QJhRaotyf1tlgKff5SNSoYB26s-GvfwkdjfbG--qjv3Y0ZthIC5wVpXnqN1o8CPsvBieczVcZXa-NfSJtumw1oW4eGDqQ0Hr_S3q_U-0ExHTQlXDTUOEKHhwKjSW8Bxdo6tIOM4mcqZGcEnUB-q5WbIBWhJZmYPnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=AM7eJZZlpzxz8oqejNI28LTfLUvMsjIS9fRiDv8YYnGsJ4ND1Mh7FNv0En13gszs84cCjZ1IfqH521Hrq2AbuklHLq9ewylnhzC54Z9lQhnpH9xMspI36ClBWrpxGloN_dmeUZKsTy3nDUOe9A8tJN5GZbLToXBCDFh5cZcyZjKlYm2IQDeDJ5PokdQ2KKY9FDHtb-B8pF2G2c_1wan0jDa8WgeCSlTcXoGdLCexMj6NBt_c4XHDSkQOW9O9GqxHKmUN6iBoruiWH6DVMC1mZMLxuK2rBI7_kUkCrJ5jLX_sFSJ8BO9FFR7j4u-T3YcVUheaH97_dmJJxvuf21CMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=AM7eJZZlpzxz8oqejNI28LTfLUvMsjIS9fRiDv8YYnGsJ4ND1Mh7FNv0En13gszs84cCjZ1IfqH521Hrq2AbuklHLq9ewylnhzC54Z9lQhnpH9xMspI36ClBWrpxGloN_dmeUZKsTy3nDUOe9A8tJN5GZbLToXBCDFh5cZcyZjKlYm2IQDeDJ5PokdQ2KKY9FDHtb-B8pF2G2c_1wan0jDa8WgeCSlTcXoGdLCexMj6NBt_c4XHDSkQOW9O9GqxHKmUN6iBoruiWH6DVMC1mZMLxuK2rBI7_kUkCrJ5jLX_sFSJ8BO9FFR7j4u-T3YcVUheaH97_dmJJxvuf21CMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=j6cFarRBsjrtB2qA6TSMKQ1eSKKokeYTzbewtoFIK0XCC6e8B1PoV5xjMDmPZ5MMTISkOcMi8rLDR72ovVp7VC0opsXUTBZti8ppH9Zci6PmLEK0uu-x38s-VSMnb_eSzI_4PIAlr6YjIjYrBJi0rrRZzTNUescnOU3mlHSC_bFfLprcjeGHHm2N9vw9cDwbW9S0ZC8qGNXTbAPncW4Q2BEEztkUmoV32DjO6cHsRgXKxrWGmRJPwryyUhtrexN304ILWuZKs_I9Yw-9bacs5MsCnc71rB1gfkVvlIxuxJ9R07w63i9GflD9ymU1O8q2KucXRgnFGkeb1OQLxBTHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=j6cFarRBsjrtB2qA6TSMKQ1eSKKokeYTzbewtoFIK0XCC6e8B1PoV5xjMDmPZ5MMTISkOcMi8rLDR72ovVp7VC0opsXUTBZti8ppH9Zci6PmLEK0uu-x38s-VSMnb_eSzI_4PIAlr6YjIjYrBJi0rrRZzTNUescnOU3mlHSC_bFfLprcjeGHHm2N9vw9cDwbW9S0ZC8qGNXTbAPncW4Q2BEEztkUmoV32DjO6cHsRgXKxrWGmRJPwryyUhtrexN304ILWuZKs_I9Yw-9bacs5MsCnc71rB1gfkVvlIxuxJ9R07w63i9GflD9ymU1O8q2KucXRgnFGkeb1OQLxBTHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=id-RyP-L3Ehfnf2dvKS2ihHvVIH46vXugHs_TGxdI1cjf16tPh1EtC7ICnDd7I5pk4S9NQgr1DidqefWy59UPtII2NGErZXbIxwWx1bu-cH5OX_V1toPbRuclm9txZyH6xzMoqBF54NGKYv4qrX1svkUD0unCUoT9hoFsJF4HX3bkq48eV2hjU8Cd0p51JfXHFbHKCGIO-P9GnDGewszAh855ro4j-PSjlotiA_Gruu2p8zOqBeHMcmWeO4KI4forik6x6caIB7Ow20zsTTkQ-1VGySQLz4A8C0mWJo92yzd4vToMFMW7vmdQ5DcjZcLRZEcC5AsRgS4E2n9T8SPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=id-RyP-L3Ehfnf2dvKS2ihHvVIH46vXugHs_TGxdI1cjf16tPh1EtC7ICnDd7I5pk4S9NQgr1DidqefWy59UPtII2NGErZXbIxwWx1bu-cH5OX_V1toPbRuclm9txZyH6xzMoqBF54NGKYv4qrX1svkUD0unCUoT9hoFsJF4HX3bkq48eV2hjU8Cd0p51JfXHFbHKCGIO-P9GnDGewszAh855ro4j-PSjlotiA_Gruu2p8zOqBeHMcmWeO4KI4forik6x6caIB7Ow20zsTTkQ-1VGySQLz4A8C0mWJo92yzd4vToMFMW7vmdQ5DcjZcLRZEcC5AsRgS4E2n9T8SPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
