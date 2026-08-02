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
<img src="https://cdn5.telesco.pe/file/t9V3qwRjqkK3Gm4E0f9xr6BO-LmX9NjH0IqfYWSeWlsIiSvL_YOIVhZ1R-3F8MBPhgvlotiG2ZurOOXQ-OoTbaBIX-tMSKqbYpGvVPOGbS57znO2LKARPlNPdroTfHYV5ts-gfEf7-XqzdGCRqBAM20tscYAu12dUkHjTSDDR9Aj-VNj7oL9I4pZdF8cPOpaGKa3e9e3rldKuTi3VGlWrNu53nhPT5H4cJiiTWpxYaMDY3ewNCMpD5rYCtExd_sNS-dPgS2Vqjt2uJkyFca9KmZlu5J3YxIcARAHVqpaJUlnIltmy8pqnrHNqxDi9H7xA0MxNKnD5DttpJ23a847yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 502K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 17:53:49</div>
<hr>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYdJqaiYXZyYi__F1XAM22YO67kdAKSV0F4hU1wqssDH9Vk7cwuQtWU69sDsUO99X4mp1aBkMjbJ0TmfrLcjVQ_3nCg3b3B5ZX-F9loeZl414NEvwOvVoEgrVOHJXZHtZXuDRrnkCUdkQJw5ToO-54vRfcZ2E1-DzaXQxkofDCjD3ZHTLHihzAr0JR4aKCjox3HAa0-tsXKieWvxWvDTLxoBr3UgU517HxgEARNp71_7cBEyQhEP53rBWZLemQliLNqaKorG3IGvyb7hy0TI-imKL1u_MBE3OWtENz2HpCDlnIjnBWVw7ARVjv9OGyAY3QyOIV9GgSD4XL1W98u-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 340 · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWyRHGdSdije0HpZGADMkjPvQBjUAqjCQTuhjrTvgFA5h9wsQdvRzOupAYblL4RoSYFRUZBM_goRY31Z84Oq6fYpmzCChxLd8SZydJWdoM5xZUJbcYKi2MqrzRSgGDOYbsWL_76wWEtBaDoF_ckUF0hGU1JXexYFagQxZPWRGhVYQza3vfkEC8sgfz-nBOz4HdPWK5EPPN1_LKF6QokNu0MyGvwR14IHBdMNc7G1DNZj4_fu19NojruX7h_IUv5xq2a7AFgYY-GGAO4ChbhIRarEnc0uMeONnSHjyKPy3MvrTsM8krDFsFPIrjwzNjmlggiN7B9xoUjdmtt2Q4rgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0HCDRgZIIq2HuulZtVyzYvfMi5IeDp_yshZ3Hq5trumVl9DKS2-yiKlleQpPuVcEvcjvhooiEBtifLvo18H1OUNfgkxTfvuLaDB790ZjOsF19TBniimJexe3vrIyknaoFMRsqPpTWceZkWwMeFA9LrNsKiRBO_Sx06-su-YHH4fcVQsX1j2X8ydqWYF9VLVYzrJve4N3ma1G7rBMnl_wyXdhK7rHR38ADbQIZVuB6GqEcJbZnwN3hvT4ILRRSfXpFkB3ruOYlyrXvWXkp27xqsmLLHOAggQqnka4ba3M4x0ZFDqHm1GoEhZ5N4-DLyJk0LYfOBNzdKgLhQI6dpNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBjxBAM1LmO6x9esji0nAoK41Y-y7bqr8CqniZJlzNJQ1NH2wZQ2ynJpVOWfjjhjUEIxp-DVi5Q4_fjeMaPyGuzeIvinf2JDWSadi4dVoc8tTA5NEd1Rg6twC-z4uD1bY0RbqQywaZANpi5PwQAqfhPjxdPW_CHa-Jtf6Q_kPeDTqhKctCYkNOSHJugrkmvkXtt7Z_9P_zzyu5r9GMQERNHV7lkgEXqPSv14H_ROYu_kvV1Kr7mwRCnkgQUgEf1NBBThbTbuKn3vIuCZbm-mnp3yUhlloZ-6kvKA4Ns6hTwH_5PylIu3tYoOpDhepyF11_zg4rESUHMicZlcuUTGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMjJ_qNfR6zo-B4GdnkAhHIIqK3JiGKAmQJH0AtVdW0y-ezq7K_o3o9rdbmafAJFiYp2m2Vu1oX6sKu5xlicb_5lTFuzoNTr9TaL3OxutBt_MfCzq0xOphfkFSYsN_5KXsbjTgqF5gk1dsSc39NB9OfjcIV-DmlO9F3jn52uMYTrOj_GfvzXiCLp7VhZQHdgCfOAZSyRyyPq5KHdTvPnBdD_QprZDyC6k0P4Co864YdMtFybtuu9ISRTJZJm9jZJd4qpcIU2eQH1QvdkJpi5YRwlEm0HUw1I5GqVs2Mr1LX7bkYp32Tq_ac_t2l7YUMJOS85a50B-H2S7JJYNUECWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn6Od9pp-UP1ZWfMdYNRmiEo2G87UABrsayd59oNFuSiX3xHOKJMpUy0FbHEha7ZGI3I42mZIX32KRXZQs7ohDUkiJuWEm_-53bBfIjnDo4KdCNbsFHNiUW8eIORpTiE2Ak23hKor-OGVwP3yQeOrBJnURiqBup0_4mTlclaE0Ij02v9DC7VOpypK0Mj9qfGRiMVo32MWL86FD2_wZoB9-2kV7TLmk8LRa3_30j9Hs6oVT19aC3BLDka7rcc7kIc_DfYfAb7jktbOfaqWk0pcRiG7ujEy5x45rn6j4e9k6Zig0KF1WYI4jS2jiWLXjfXcWTvV7u7JBtd-SlISOMKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAbkOKEeVzbJs-rSYYFtOjGp1A88eyJrnipNsriCzb4bJau4ETL4oQNkcim9BjL_amaZBLGj8_a1TMVzJt9TIOoiDNmShR24-j8X5nqz-OhxNPrC4Jj8nSZY5-niIYQFimw2BLwVAah6Ftzkr_p9Z3tRDFqWco3FbTaX3iHBquIJupV0E0GIhT_UzEiiaVlqIwbUfKJpiTQvpqdAKorwvoNaxSQD3rOR4KDSCv0xl4rMCz1xGtD-sOPZUtyNeDPMzEy-A7PEvCq2--MvpnHRTRVYKLk5DHMyPzaOqcEBlHAM02zp3KJV85PilXh8OCMnq2NTS_2YHb7qvv6EJJQlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEOVHNaZv2Jxpa4FGlutaaQ1RN5oZTeTOac107O3ExlLld8x7-VadbIqSuuLrzTF40_8ltaCjUQ9p_nbge5HvDBAYjNhgxSh7_yre8yTREqJ9qkLg_V9tbEyDjiBKI379_1ohdzErultbb1__og8ixJVCWW26nMZSiA_qgnPIWRnHT98LLzMlO0MakrcdqQUsph1RpQ-pYUkd411SUr7E3UFDuRSU5WvPKLJczswAboac73jrhnvgnPhszQasabTwy5DQ4H8rWAe4667xZwOHPDrWqSVIS2Nl7EiL-P5_9NmebeLm61HBwqHmI9cGSC3bUtpcAZ0IHZZhRRcq4f7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWpYUj6mrKFYAaIskFT2Bmr0zTJfJoyxk1QMRn0bRYspK79gEyC4Ui8Cg351pDGVRjKYTzClNOLzjNERUte11TgdMqYd_Q0uYFucdHjH-_DbLifbRYE2ePvIL6xnzAgpotLEgMGOw3eunQlFxJ2uvKovdTmUzf0JO_coqPROYc0ssS9QouZAQVEzhf9sjBd-8gN2d3D-xFHEPIKczIc6P921UFhwlT6TPnPuGpXwOvk_yD-0sa9ujO74puX7mnyAcVBf2vj0THcsgLS7lMv0ozFd20iZZuFk-dzpdgfhrmdPDxn_3zTdQJwbClCAsQulgxx3M7qlL7W8BPRWgpL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpMD_1FG6n3vd4aatAz4wQbDPL61KikOWUNgLMz6OcqbIcouug5_F_8InnD8NRM2mNRiRQasEm45dJkAVBb5q_occWGpw9aj0mg27J0Mw1L4Tcj201mKBn3psSMElUx97Z9EHyNHH1EtHzzlVU8NuGDF7XgLPXGcul3X6VuEyb9X6-ho8kI5E5sSVGgpadFTzJeQcHJBBLIsOxyh-ZGV3UwjAD1Az_qJr-x37Gfyh461L5O3t5d4KiuKN2AYRsJ8QPt0kS0ze7jvacwD8XXNuqKji1PRIIYdXTro13kG96hxLgt1P3AiZtAEdWu6saQaOEwzXaPERnqAp7zi5ylLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q59OSAtfrpCUVoTduRY2AMt69f2btWXtgTsWicBIRsiRBvbyE2kZLBtuHnBjJ4R3TMySAgRXHPEOICG4V9aGxevlSb7Sse0FUy6McXh5NH97S9DYfwJlvXKXb_-oKIo014lLqRawODUwk-LB3NA23CGjwobErFgpvQ6ku61OURlFLSgfVNUTNdNTm3_dpN1oHfgWTlI2LMhU0jZDnqgdby7pxCxwqW-j7EzZp7jtrIMb331sIj8rDYdsThpVR6Iw6QbqcvDVTAtgQUqY7gQe6ML3FmyhlOHz_r07Qt1gQ57WszTuDRcTBCkODRxIj60EGRIKM9fOU-ZO2QBz5drzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4mqedJitNRF6rkZPo1zftI--9rDYWGAMGlm3EsVq6-1hFepkx7C46JgcqGr7bqlIziJk2NTM3rt3U1zxBXMrsfSh_zkVkcwLbdoEklnNQcKiApsok3XZ2N7BvAknU-S4HNp3ZkGvLtSg-dE4yFzsGCXB5A6BD7Edl5znpR1AtIRd7Dk98KXtve3jARVDSoyIz_102Ny3IsHvSgeDLKSlRSUT_wUXGEO-ZLYmXfUe_LiK6f160s0p7e46HnqGt1Y_s3A5ia3P4wL1OSQYmhfDJGWbY4EHGlGdymRAu4RXR8bKqPVyJLs5_dkI3QOsY2-NkpudajEDKUCFEUlrxSobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/durdPnVviKaUU0CdLGLfsDgHrDwRHmsTFOSvd0UThuIKi_yqPLQqts_I44xuxeqsj_66UvSrSsEpK12z6XywWFaHdHgAgvbAsciEu-MErAnU_Y3p9cV41iRMKC6LziTpRqNZKmKfc0sc6qfek8hZEtTICh12-5GKDOSiaj84jf2f4ugMp0PTBnubYNQYF1qdy68hR6ecyDHQjQzKZj12PpR8AVmNxiF8mcla_z1YUO0X-89_a4s6JseCC5pjW9biYxHOL_QnO7Lw3f1mQjWMmc6BgZaG3ZPRMsR28yrJkEdazsYG74K279njmzscXh1L807M_H85V_gzq3Ie7HSjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JknzRKYM4_5KGm2KXs9a-a2LV_dApPxOCOrkSdKK8mw9DzaynicoxDSTO-EaeD_EJYUx5moPOdy5Zx87RZ9SYXcQbovq1sA9g14siNPaoTJl_trB2xMw3PyJr5Lns77eTXst5BqVauaVl4sWeuVYn5Va8Fs6c-Urd5iSM7uF1RppQ4rnV-gU7GIP-gQoiWZ2j_fDxNkfliM8DkYsrLw0tpdWv0HdKFwoR1TzuwbV_TZdIr1Pnk_eRllfIFMnLeZ3h5OfBu4Hw_y2cxDYu7mJPwxVKlR6hWgrxPD2i5uA0cuwgHfzzjCbkh61XWIny1V7z_k6qqebUiqwryxcgAEOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH4fCfzuLFS1Dxaok1vh5ogWnRSjxamZUbuNaLdIT0bvgr9OTV6hwl8z9tJK8aPgpILePZNGbfiSE-dvMnWIIdQptnnFD40jk7NQbEpJ0Vmyn7JfZESFs8JsGhABX7IxOx3w6K7NeB9PO_mnsiCn03zwFW1YZ6O7cUV4cNf9F3c9HdWEX5HGc76MGZPU4GZaj1lIeBW0cYBcvzQgEn8gskWYkZIM3B2AftbLe1wx-mqbkU018gyB1p2L1TDjfPVHRREvp809ZrIWF4J4nxgMeRprgy2RTxiQAyIz-PpNszp2M7qQSkUJIGpx_2FeuMdeBaOlAEbZ1Wl3N7r9aQ1CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYzDJktUan2Nrwzp4tB9NQ8mT05rUxh1ZdExUzWIhRijwyp7Zp6etjZjmPbT0rtPrUQcLxQYA_DP1AQBEbrbngtfCjUfWRcBj8iNdYqNPmXlmWec5XuQXa0TSXfESfNA8deC4FIQpWKHx7t1YaIq0XJcxt0YACbkweF9Y4kMrVgm2kVB-3zqItkDPGWag4umywRn5my65UyXATlZrAqgG9Zc6RBX8RUvk_cH93qFBlmidsCJb9f_3Fc3-Mb4x5YJkG7s1csTZajPcP2WaOT5g3FNSu2xbF-4hKs1a8Suum-s65qHxmBZYBEqa9ErToWK0i0ZiF7jwMmN4yL-IALgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQL8tpikhzUyf3yu1vuyPD_6M85a5LZ-hmoUkVbw1dy-D_DD95WwpYPtotTkXh6lwOdL8cDtRJIVnIDtWjIZQSBsq7rA6xrOJgtCB3u_VljwLqwbQTeAE9MS76VDhSTvYVMplmjooaRuWvhXvp8YQXrtG9bjP5CPIlXjZF9SvGje1WMQVqWMbUkJzFnbhjrOxoe8nSBHeMPFG2BjZ_1cnFYoSlS8wCr4gXxau9Lo08ELtWNYgrrwzxd3E9VhptVOKiXJpBTFbcHVtd40p5_3oecO-r9P5Y5WkFf2gwtoOprGT37NG4zyUgajkGcpOCIjib4W2oS0AA-sG1kfM7cxRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twqWlLkXVmKF1HQFMYrOnd2M8-fpmV9WSGyrIMl6hGwsBLTrn6zG70Djl1EQrcNolES4wCcRvXg2eGr657y1dtBtL3nxVtTOr0tsD5Es95fg2BvsMDrnImOIkHNARe6vD2uLjtk6nvQij2YXZuzawRhLXXf3u07Dc4vsbozYmDT_o1tmmlYpIe3SZRCC51MA1frdZhX7BhBGOgxe8fa6ECoBSzc28x7cPwhUrM6koOO-Y0wedvytFict-PAFR-LjWItuCJtWz-1awPJB8U2jOAtj9vcf843JWQi982sSWLNMrYaNrGw1z-voNym3zt6Y19A8mY0N6zz8mV15s9CfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kox515Y72BUGgFGGtEmFNSzZbDrjvWxSK5rX-YSopoZD5N7Fh5amIHuZ2BjRJVyP-1d_yFQVx6Eh9QNed4JXq7T_ax_kUNB3nz7OjhpxXyhsLkBXSOvXIKGrkR6fS2Gs52MCh0G9UC_KO4soAmzkDGW50VSMPr9uB8T03MQBYHlUgRjIlkMhq8rN5ulvDPQTPmwEoH7ralFi23CdWORQ8nU9aSw-tU7JAYj4oPEYFjJXs8NJ3zOFs0sthtkUfOxb_iS1JghscVbGoeMRLswbcEErsZJfv0l5QHAqRkjcH7P1NPWOUuaSP1xTkm_I5DWAzDeblw4QBKzu-PgENQF_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRVqbnNpHD82jytaMXYvPdEMMyjlnOVqez-NFRFrtKB8REuqGqT8D6_xeAfJfnqaXx3egKW-iVpUBE08_Jb0MvhG6AtPbZ96Z5DKSBA4ohfWfzbsGCBgQ9UeL5b2_Xsg15m9dxWheU-na4FyGCa4lW6gj5CqF_hQLOmlt09KZW6OU7BXB1A73SD8DakWUUOCHnolDco79YxN_Znj2ThJMz0tJRBkEvFhpjWybHzukctKwcP0FlswGoQZRDC0VgHPaxZskxVWyOYFO5qxQkXlBt5vF5-lrgHEAjrx6Jv7tsNpCMzCMCrOiH2mjMJGcwShdcNvPGAG3l7RQ73Qh_dPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRE_f7iurJeg7UcLCDWdQl7HyCsig1KRk13BAUCRiiuXU7mJpdnR-dmJej0olDVOYd3e1WtcUkt3K0DR_vV77uma7jBKwxF9fYp8bINTyPaf-3w2Q7DAOItV0LRuJXeBrJ3qa3qoaGzZTbkQAiGU1LJUHlnYqbn_6BU7NoXaQPSzMLgKB8o9pz_LpWou605CaQEtKRhwaFLtyE4kEY9ggevURgkCWXu1LK6GtrK99RsDEah54TIzLK-1D1C8aQNrJ6tJYZDrSS5bk2ZcW7TKAG79ZqfZMeEPXToWf0Fc7ZI21CqKa-jLS1qXl6KBLGRwzPHBI1IMqDIlRsJ10iMJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEnPaJgz3m16Vbtf754c1LGe-_CKH2KRjk4YV6Yh5NeSBqt30gkRPkVC2ugjVE1EyfVqNumHcYXRs5-cuqNIDAgw0vK8wl01VcxXNBRked29UAh-7g821rTliAGZlXWD-Pmg3pfAE7gxdcq7LvxNoM1i8_DlfNJAzmftmv7ZgetaGZSG0aM1-6Y7suXwkuVbcf_c9ooI26gMy33jD6Rxy3GfFzDD1RDfT95_FCMaB_eoGDIXD79dfJ1cm6C5YhOqDAMMP_prxIYEDnMpxLPa0PGi11MJKn_mKX-O-nYchJQg8jctIUENMkPBAqNPim-IgZdLduqU0xyhJfNW0UAmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLdDLned7CzrS_MMladjmqit0-LdwOVRcp0KaHAFWW8qRDsCG0D4Uq6DjNFGmekvc1OtKiMIx7EpQFW0r35JmUkRQPYELwztUec6OBhtYh5rcMDrjHgVy4nNEM2Md-8taupAe7kLeE3bbzC_KbHVDpYUZqE31QeMsliqOPvU1_uNmR-Gr4YJGc-AkPJDO0UUY-gRUKcK6WWYWcLPhqe_r4HjHYdjk7Z8lCxSSzNucj3vYyvith0EmrvWo8O8S-nlXT9tyO6jnMLnBUM3z7tupRNfD77kl59HaPLx2DrRr5I7q3KPOV0GzFJx3Py799fmoiRgMEUS1OPgqDZGHMVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl1uYlRzxyT4LaYjkNF-c-hYYGHo9f3n4JhvqGFg1KOsvwfg2mYvs0yv26GE0LcxtPIqvO_5wRxXDG6YQxh32rf61vgbBNDI9I8gW3Z5mrrl3Lw-U-Tp0M3LomiQGg4BOqYnhiSWmsDlCYDDz0y1Aeh76Gje9h0wb0UgGGax2w8qvLJ-HnEX_6bbUv-huz-SmoHSuBP8AT4xztaeATtu2VqiKJjWfCCpVzL5452sufIVJve3zC3yi7DUELxqtiKesNjwtCaccyIlsH7Fq8GnU14QlNhiGkKYDMMRzZxGB_SOBqtk3ZEhXizzTAjwHlC8Q8oayL-qrc67UVw4BKE9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkDk1TpHpEH_xI-sRKyRRbYSdVAPGvp5uZhuaUjCA0Ni01uV68MJFhU96aInrStqNoKPKOhhFq0eQK7i2l9sK-yhHg0aUMNSyUs-slpmY4HeTUJrXvyDG1fBcg5tPXmrI6oeZmO2OQZB7haBDMKmDGtkPNXSP_mnusiyfxLVdB_zMc0ZMwAeGRj_j_bawtAAnkXc1u60CDQ25WKO2KsIGimlXNFBRNoPAzQDX6cF4BdC9a7jeJzqk6vvfzVh1fkWy7a5l98Kj9NlTx7nseurKkXooGPjghwKdNZqfKEUWPJwYtAKm3M5GnTDL8CRSq2AuojX481gmm3LNeb0WHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyqUmBSmvVwX5sjigdv9BlUD5H7UCCCWQsu8JTvlp1gEsdkVncjQXxQ-BZODN8nA6jfoqriQVvdsga9WrX2cZYgG8DBgB6csYGMqZf6Mp9u1EqNedcFl8QMB3WEmbbDD0j_U5MpBVGr92XmQv3vpOJo_1E2L2LnjalZm92KYqzZVuT7MqUmTeWmWuc6jq4l_kGH1iSE1UoljDsjbLEAAkXCarJEULpEJuQqfC6Md_z3YljC5xEn3n3FK9NmAFEBkaJssPAucaVR-PmY2tGhsK-dLv_I_jKOPRENcHp6Nm52zZss3VkDmucpByxRHo8sNuuLvj-eqLxSdI3oHzCIuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj0LeoSJny9bqz4CsuPcVcBns7dTWwmb2Z_mvJXmxYhfEMzMvo39kMzqtAxPIAwMlJK4kT2WACJPfWHqy_876uI-VbRYQBPP2BMPyUFzGCufBR2jQkQgEMl17r4kuH2pa5z8QYwXVTqtJD2p_MKm8yyE4QOFQVqC7jnw_hXT79ZuURvJhgJp2DE9T7Wl7bra1j99mjMhIqa_YnoSntG_Ih2jCu1Etr1Ee2C20OkbxPH3LVGs1hoPllDzRK_jc_8fjwpo6WwH6-nT32qYD1CoXoU092lzpofnvoEkO8rDxWzjOfRXONqVUfHtuB9x_z4tPp1pqqADs_w9PuV5LPG1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGqFf38VhYa8aQrwFm_Iz0nzXz1JI6HcOBEHJWerzhlYBJJc9lpoydPm8jyXfHcKULTS9zuacWvbXffAXZRAtHrMGorejDtz82pBjwXuYyZ8CjiLnmfD4tTeSeaN1GaQc_jWgAKYNRPXZ-RvJmOCVl33qgHrsTc-Sq9VoF5OKxCDB0nlq4R2O1zMRU5Kpp1QQSzu5qIuffAwwzgNwbRRxU_Ik5_8SLm4cR23l9pFCuvS4St-OXd4NtuatD2JSMW6R_1tsXoXmmPg5EdcHLy3KmqoGW0n-wfFdBsJyCUF24SekLDydWadn0OzM2tnzzesfJjMRfrqGIYP0_5rRXmVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyTqJISoGJ6EDBTurlcAuJVwoiXUau7liRj9oACg9zUL1aRqaVZTkz_zxPVxnB_OMsfHh7bcvgXCsj3ykvwxtVlGkf44CgYT-1ZS-pOFsWpex7t471gmEin355NXOsfB1w4M3rxvxBPhmtUSOUGGhWK6ht2jWZT7ft7w5q7uT5ZN13wxnnP8WpxMfr5V-81InJim8nZPwhDtFESvh5tZVq4y8PWbIxHorGHRziWNBXcXJ8RZhv5oOZ7dhxnjQwVHZnPjN6swynx97hfqU5oSue-7b4KZU8kSmukbZn1YvXzyEPAl7moZsxJ9fyyqzhXO1qBF_qvenYwkK50gch68kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqvd-1hIdjWBMi7m8xC7MUSmmx8Had1ak__y-BdDgFV9NhWY838HdXJjWhuf-gnNjqO0UZnLUIgQOPt__Fl3EP7cLuhRpOzXpBSSwbYCllANsif0s6xlYNmQ_Ed-PsoOXol8UCvkKznH1QTzl3ooIUkJyYh1DYWmv4-7Ni9NKrt8KGr_vdKHxdm7Ah5VUrw7qHKao_zJpnc38IB-q0uXbr7BD34_tqiTTOKghCgdgyJNGE2btajkZUUWFhwGDkO78dlmznoSVEE0dhgwT8Bmdlao8wIU-xiy1Zex30K4moeznzeCiTwIOq5KlvXEScSIEB2VLl9BGtk_ZF8pzyABHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8Ozw3dBW1Lkxa0nnhKoIC7CYmwyyhZZ9bQcIQfqaOdsjPm9ZkQBsRrRDGvsgz0JyWI1UcNSL9ahic1dQkxDUQ6hzj7WVgjYu9ME7Pju2OtKJcUji4uggEdZbnvw5loDPQJqmek4Wa5UZ3RYcN5bFgFD9l7UX1IJPGfnK0Zz2xRLsd5VyGVYvjtPQ7v1JBZmFdqETcwoeZ37Spfo-gURP0Ki08x_XmMF50HzzQE8QGbeDAZvRCYUr2vsJN5WLJ0gUsPEysDHD3q_uVAjCZ722skFsVPL3UrAQvoizJaNXYjMNJ5LUqJIkVjtblKWLfTlzicbVtILGvhn0PnHaIS87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9pls2J2Z6ZEdImmQ4oBmmHMuTnPxqZDBjZB1xO89EwfsgP-OrFQhSj8rY3EzX4tDF6y1tHJyuFc1_gEpX12zQOc8SceaOO1z0T-RDJcxwinSLeKJTh9Byz5nHqcurpl2toHFjpJ1bi3HxBDqnVtDsyhKyeHxj312KK94dEFpKVjFWs4kQPEpxlZldNOZlu0RxqoUFmETM0fvvxBt4N8Rn2ZqIP25jG_JXBeEo3-ZP92Br46uQt6aDGk8jMxAf4OOGG8YzMMS3ZZhPM6UXuuV1AzDJt2jJeRA6amTdMts8wbLmesLXAfKDUR5Mr-IKDWiflRG-MY6ZVcjRfaE_27Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZbAEOox2smKLRiIl0Jk-fKW5FzikFoHLl0RscHIkpFZtI2Ars1-ZQTaWv9AWjOINXKQb2e_We2wAtDQwuKqr15tGDq5rkWwHp13FVvIQSNhf7jtQZamj9KcA_G_mq_mF305qFGXI1iiDC0RyIZm7byo8Zp7l9Ng26EbPUmHrx9mFGZBaSMHGdeBVAy6o8E2gs6-hi6POzsWuIDXYMqJyzGZ8_h2ij82xcSEFbt9VFqC04ecHgBz2tUKfKEfDWCfN0YfkZE3bRRpxiNGZBEflbtkvBRNvGbiJ8iGArq3p2f6wfZTX0lfKjLvSNhYuLX9AsenGbLDTOyw1jF5I34QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZbEMy2GExXqZVJ1cO48RFBoR_KqdkYVkd3dqh8dDBBdWp-6M-mqnSLTs6lJy_gikQCB2pFrhCxFKiJM4vpq9VXTQAQMzO56jq9LuXkA8Tlev7INHep5Ko3qnvWwWW15ewqfDQol3cJfJk1EjI-wKd1HXOUfLwNgKkfZsGbOgMd3Nolm7SAcm45n9E3r_nL34v6dd5PV76-BrzHBLZkiklOQADqwzHT9v-krCcKfwfxXMo2269SLNkUzK5iapc08d5AnS071kpCLeK_siZ75Iamd8SDNLiv4Sbl6q6wezP7wfrh4ATYaXN8CmygZn2OCv0v50ATXWR6z3sZ2WVJlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E14sGUQyas46H8toaKevIMnPnG9gQ2r1nuzFkFOiJrVgKdIiG74la9EnQXi_XTBfOkRaMF1t-YH-7dTjXJu9z9JgqFwx6y-_hhrvakBfP9hCt3mfseoP61RTVxBjoVrKaccutJY96OBcUySoKh_L6-9DybhGAagAWf5Da3GD3H5oyUEIxCN1LIaU2D3piBddqdHsfLMoAIIdEBZpjQa4tBN72jwbgi0g-OPQVJkfzL1GCtjdFqQCQYBG3FhhZpZEDT0RgfpLVviqa02oFh8Ei4Me_6LEOddiR7HFHlmFg0WYLF2J_kpA4WISAbPuWWlXozfAQlWQ9m5VZJ57rTrb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjLGUwTJJnM9RBhqs6FH3PYcl3Lq2NUnc1u4BA0ofeOpv7BKYW9VYZAMyI22sDWxeQ7z70Hl5AdgsU6YNdd8n_2hdwdUHd3Z5t8aCGrtC2Z8lav9UBWRKQwZiK7mTg7coQGNwpICscn9JlBI4J0pMzNbfMaOfjhHdFq2TvG5yf7JGpP3NeGF51oQ7FQl2sycwfUWJD_vpxY9kcOS1mQc39TRQpeoIFouzolAtz6KwTKUHM3h07HLQSTt_EkjAJ8leOPuOGRYZNFzm4BTfZUJJjT5yXOESxHOAs8lNyL-kVnvS8F_dX-FBm-LHOSOzE7ViAKK1gy8G5gv0_QBJLcuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjx6RxSrlxUzJ-hLqrr6-8B-L6PhSF-9vy-yVkctm9Vbamm1G9Q36Ho839zj67ZyOOZx5fXo_41q1n3kZp55TaX5dJXk6So6BS3l1UG3a_G-YS4GMVQycbySgCRwH2ghFxOhzqcoVXne_ALlwGZzy_hWj2yKYHicctJAjex9z18hjl_MF36ixAeFzybeo9dKwn7YAlM_4c7yODlirQIgZSCC20Z40AisFQstVszyFucdis4WdGWFbPtjP3h-l3--9zNW99kyvqnUo2CpwVI9zIpeGOyr7y4A1g2bGCCPgy4vaVIW4vNBKRUaTYmkQ0CERMIh_aIDPNfn30FWjqC67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqSBNs-pDKS4RF5cEq5v-ntqRMCBaFOvTZRm0aICIi1hpgm_f47CS2zNWXZn5sncKHV-YPclKjeAgvRQ9gllUhXkvsJm4uY-J9vXiw6uHaGuRlMSOz_6laFxp2vNTNPC6TQYg3ixQCSvuztzZ0G_zXgcza--5aTCv75JTpWfEBSDMtqM_yXO-eluj-zbNCReeAeUC42L1azeMzfijdCyI787HedqXem3-x54xfp6sTnzJfVwpttcATUresyuyBjjFlEHgEPDAUOccHO6E54ozOJpF_XXuOXSFgCOW657J3JRVf83uHhQn1XGXpzohqzQS-gfYmVW600mmLRUgmalOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PAsxkSv_NBFWVFRD88WVoQQxpZTk9t8BgzeR1VYaqcORgNOzO2fpbISKhp02-ZDgU813RVsR_MVquTPSBCk2GWF7y0M4RQj7gHFxV4gA9jJhgYgNbX3m--FwTlL3E0qQEM4Bszo-MgmYEDACOcGbfmBNKsEppT0XZQGMTWSk-Un-BBlxjJDrdM_Cp8tLPQEyJEiyUtZ-FyPcp7HUKMmtkbQ7UsQaTBsYGkolvQpkPcir3kcU0QactfY2BxfhoMkzWdB0galG3sDpRxwNoC3R1l2_xei3UUPSiciwZ3lTsSAd26A7n8Qmt24UVUjr18pxJFhBaslc5zRbgZOgdJ7Z6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8hRvbnrxQ6JicqOV-REYPrUXFHeTGCbT6aOGmaFD5abVYlSqRZreCk981cRB6GRBcg3EXrhGgMJzoBhiJAbaU-uIO7sMM-tFQNlVOKM9gDb1u5HZC3sKd3C2IrEwwxK_EWSluI2vf0JytYTJfkh02SQpKelu_mFiXcs8lDg3QQ9EKTsNrVkKlb-uz7Otvu1e18Arj-SEYfzB1c3TulZPtk1XaaB_Ha7qESiipxTnnRx6PeCSX3t0PebIrjIv_yDOzP68IeP_C1vyUvypl9xqaIk9kiq_kSoh7krSHKt5rADd3mBbksFCVYLiW5zpsK5gfMD68Cdbh5P3CAJAC8Wkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMNmMUBfXI37qhRRtBXxNe3_0u5lk0KJOjvLJ84BxqwULgX3jYF--MuGv-LmBnCYPto1zedJV-npbAM2yxKbb-VtFhCpGU_7c6DmspQ8U66kGiftdSlILpzml-BqE3GUfS1XTpWogsPC6a8kcV8DXa2jg40Exi61REv5W3C6TlanEDy7XMGTTua4zggOZqhk3j8Dwe1GAEMMK7Z0DEwNd_V-aUhD-evUMYDvlaaL9eMQ2zWtbtSTEcByttjxC7Fk5MhmtED775VPYXyiNtRagjzKKFIBCDAOym_AXHxM4kklb2jG66mLTAlU2UixdUNUKM0XE2_saz23nmp6JPJTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-xjXLVWr-_1ofOYJn6PBvO2nASHzyGIIa19iaaM2AjYzxRFMQ3p7KVbzIAXMohQFJfhKfSECO2h6FFXqP3WPgFVwhc7ADlH3s_knwT0qjxUiMlKoXtMa62UdDslgEqinC3XkRRZhC5_i74P5suxe2KikLu66Hp6gAJuOkhubbObUfSwbErGlctt0ElUBFGCNTEg2hMCsRPwqIWwgVHDlIhYosL5Gmar3MdWHyw-RP6_HWIaBz4mGfJ7_vrd9QdjIqwNjh9tj65BGQhdM_Prja18v53Uk6Inyy_3Q32K46iqhd-XwdD8yx61kjstD8219g9sYWG6P7r85pFnkqpM9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaXnKbdocshkc-On-fxFtgWsEX0lgOCgcDWVukQjoUhwoy80Kf8xq9jzO7uJNNp4Q2CtftxRP4ZnTZXA6hOZaEi5Q1aFnonxOPLGUBhSoSDbwIqI4T8vAwXqzi0KrnqVoY33cPQICiJEEcuJ1Wf-cIC0OTswrIJSPul2nvjJfEC5BqcrjGySmoYKCD-0SgXBscMJojNZOKoNfFjWWqUgZqnDNM1RAz9C8UZ3WdntT11GJoYuA0_9CFlDziyiBiuLknYOKqQmNpzANgulAiqD7W0TOdxOVOt-MaGv5roo4_S6vDYshbUjELFvvUF7bAEMD17qtytw2q7Fkbt_bm1jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRzZowdkKBn1EreMTpzXQqE30HO8l4T-9pzuvKrhLpcTmLhE5Ez-qAq_LNOXWXh71xknz74j1Z5JpOImmY-cRfWdLh2K40E7yYMXS3tzcJ-MalJii9M1Ml7cGIFc1peoyk3GdrsKTnzMfTB6FeijP6-y_BjRSaZ3QYVZWWrHEGjA9r3beZs9458puyGt0L48HB5Wy4ZB_kLvOeTEj-Z2VL1Wma9oVOE4jPT4-piHdeILGd1KtiWyQ2rN0y6_8cCmcP7utjOP04SN3Ci31aJF3a_hQlfc2_-nrsFyqchJdGdJlrIsYwSl8Ob3BBm_aH5Z865zJ59Fzcn5Lww01K_wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6GXAD4quKo_51JA0e3wjG9n3xiWAkrplQv5iT9RfpNAYswlNw4rJUojPm4JF2jJqKBa2_spquf7_IZbF9bf4fianKU9dRim8aMzV5PjqHUkFTnS1Y71Gm17a7xODrdxZ9syaU0hbcfdTWmv-EBNlYt1ohl_uc2_SyPGTwPSOse5lHvfQY-vriwMvaCFH9VJ1ZE8x-g7LxGncbY85Sb45EvDBkJDMg8uoSZONsygLsoxjKWi1hJ3WNMRUtXkn3qYghdlfed_yTnxoBuSmSU7rykgpVuPqABICvS5LMZTUNGYEPHIP_E6w32M2wxYljKHiPRy0uJEN0C7astnLqKOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=vBW5kWdM9DwOR4fDIKdG2y4nGjsV1dhVkfj1rGk6xwF5jmbDA_wTExXN-pSWJ7RwCWZKTFRvmamR63qZxiLq_4eihrFzHzLX3WOlmsg0eyC6CnxGz3a3oxQ8k4_uUEXM5O-KCZaAOWce7rc2W_HsCkr5dKJ5KJzZ1gUyWL_PY-ABh2d-59c0RoPkbJ2SWdb3FtRGODmOqhErmS5YLalyFqF37t7dAUXJ1v4rCJyXKtrewwRtDW3U-fQJjZjfyF4D3piWqLvVb1qkSaLhUwvgOrsgSk3Gz5u8LQqjTOEbAA2Ll8k-WoFgXPs72ndeI7tjQE_hsmGpKxtKZ51Tkano8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=vBW5kWdM9DwOR4fDIKdG2y4nGjsV1dhVkfj1rGk6xwF5jmbDA_wTExXN-pSWJ7RwCWZKTFRvmamR63qZxiLq_4eihrFzHzLX3WOlmsg0eyC6CnxGz3a3oxQ8k4_uUEXM5O-KCZaAOWce7rc2W_HsCkr5dKJ5KJzZ1gUyWL_PY-ABh2d-59c0RoPkbJ2SWdb3FtRGODmOqhErmS5YLalyFqF37t7dAUXJ1v4rCJyXKtrewwRtDW3U-fQJjZjfyF4D3piWqLvVb1qkSaLhUwvgOrsgSk3Gz5u8LQqjTOEbAA2Ll8k-WoFgXPs72ndeI7tjQE_hsmGpKxtKZ51Tkano8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7exbmvyrb1qhzFryIVR15TnMjvWBzJFwIwxjFJ9zRNlAJcMT5IOJbegQ5MDG9jrFvJXjurRDifV5twcTZuklxXnrwSnh3tNpKjDf9J8tDTUQxod0tLgZVeuOm3LFnvao0sqLp8so5lDYSr2ZVMGVaQWQUlnRc81nfL091gC_5_4ravVqJ6-9Ec-nJxJ2sVwyxqZ1qDhopmYlS5AMMg5o13uJzn3CcVDn2OYbKtcaPNnJWcWT8hXKfQvkQYQJ8K8pSooH6B8w7yPldv_M4he8CC9GslYHDUXv8XgYtMqwkZDJv7h1KfrAKgCSYspW692jiyA9pYkmfCo2oVOwowTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4GrqDx529r2Ct-w5NGjpl6KaEo44jyDKgkLPLeNYM9IYtOUba-hVCEcTTCV7jdxMZ5dxHhFg-uzWZFd4RqZ5RCYlidXIIMkthp2FwP4xPBvkNGwwun4EBwyBHKxNpzgLNdXhzYAS5PnNSXIL6rdNNCQuQzIiit3XkheNWLAl-tZiOmBBsGRcI57Q7fZy7IOz5oEmS-QPjc2jcOdbN0zd6yQ3jqHeHQ5MIHphkpVwoTJ9XdUTcauLv0xtpEZSbMVsYBnF-CyGNawxdr2fYVR53mzuZj7T3KhxcCTl2-18ER45tP4gSiuZs7Lz0JlB_kjxAqhaUW_gej4RCOSdFepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGZiIH2WEB6n8rPvLh_064MiVyNDm8L7GyqonwhgnOtf3iATy3Y5k-T1mLgu0sh2FC-ln4lue5oGWXDnNcXahJ2VDfTlDhXEqvPVfBA0Rc5tHhTr8MVrXXIDZMFl_GbcEfZR2b1QFy3vmIVzUyJTSnABiTk2lwMyILefj1bN-KKDRXC6cJJpu98dnEDus7QxoCYO9kt6IDN7vL8oWa3bUicN2AphYym8ylCwbMZPmpDlo1UWmc5j88ZGIae6PuAktqvr2uNQb72MD4OsRQ6ACeJM4iWyUSyy5-MTKTNp64jpz2D__BWQ9OOikSfNp8AbMLr605BaB2RYUlK9qoDv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnaZecuy1ETUkbZqPKy_3eJqeZzlrhOnox0D2cSz1AmHCZOf156F2lyi3fD63E1gHVZGwlEr9XXUTQCBxlx_a5UNr-XxEhNNovxRTBUzwVj2Ey6R5NihTQbj2fiQsrtUk1Mo4hgrrPO7BxTCcIGvIqc98Vz-jCbTh-IS0FloEA2o-QDBsnzmr7dJTHbdLpw6Z5DOpVZqczyUhRj0BWW1iwO27bK_c2Zpx1cmv9OE9N3keSkIesbPFVeuBcruZsLnIDMahDm6-SnkdOujyLxxKTm7Ryj5XLuJ1dHG5lmeNPjNRtKKIoKcG3wxRCYQ_ChT74A4tkBR7eLNBZfxXtlJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3OSkCfk2t2h9NBtjmwjCYM_YUE1KEdH2WX3GB5E0PMbpkJjPDY_ntHsPTdBCbL0kondH1gKVZkeYQBc8pkC_A5wPsCKhjrlkDngDdA7jHo0KhKadfSWzpremONv7IcJ8d7Nf4I5dR91NxLZb-wl1ndFcQlLK58pG3AnyrO65R3Ki7a1yWcmqtpQi-kL0vyYngJgB1dXWlO6IKeg-a5z8QEA6eROBBXBPGQrwlezd8NceBQPTlxLxZUTNGfAHr182LrVZyZhTur9s59Y3vb-RqAr8-Dp5x_ozxCG1NQ8boWDBbtZmETh-JyyZLQ1P0CFENZE4LlreiJkLfRLuAiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJLZiX8KxUpLcNdY_Xk7B4oSI_9EKq9Fm5XfBdhmu1kBhAv6K8AjjjfTuvW1QyCxVrtVCh2sL4Xxw5ya1xAw4Er4xRSGUsuQv8hFlsJqTNrf0_rqoPajhOe0IItWdqYo4194nd4diZYu9a-V13sznmBsrSCLuEwrAmXUZbUagCzLuNBhHx3AgV3Nr4848Q0JTW3FnfAWZtCMVW7YsVBPHDZFNpwQtpHNRRn_B-RJ_yzf1Bscj7lUfS1ClciVxXbPQIUHq6XADS9tar5DeKH7LubteK1IGWqEh-tfI06B1xGcVKquHU_LTCavoAUMUvKsvCvGmb0RuDJNN6U4TbFkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4rxGNMemZ07X158t21ksX4rNTQ190SYt5exabeD9lib9Sl4_XmQJE7sMmVWVivCxYsJZ2HdVGZzknwm8Wn7Zy68sMChZG48LQXzXcFdKV5horYS3xKDIbhxZ062QiwGJmmWCGA2nzjVJwg6DZ6apGAKDE-3tmAYAP5X9S60APcv1d7ghspdiMXu9iN7Q_87dHJidsUfNxFEo3Wzbf-fKPJ0hL562Ap0EULJDoKQQVU0IqTeFvdBGemYlwiZMVLIDaodU5VnADkTumXDGyIO5CBxz9a_gEscPjJGbRrBGefgm4YumcmSIcnAAgTT6LEos2ia5UyOGzSsxVL58K8vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdd4d1NihlfVZ72USbOQMZPO8-lAp2a47AGYk5HfcdeK5Hn2C9WgEYxmAjA2uUcr5c0vE6kR-e7GwHp0bIfN3FEdmWQSTi1lEnnwd0dQ6u7kliGbXT7uQQfPJBLA8Z1wIJSmmlI5xC6SPFrwrSOTVjpTTarTT1yBCtZZUQnIDKXEXrhI7qInm8rCIibqxzteYJvL_eHWW7wORJl71Xc4tutSPDAbUJHpX6LsAZ-Od947YB66MsgbrRXP-SQEtx8T3-KhzUFuckzagmcG_P3Rs31UKy_RykbT4X4sunPZQfqPZlAxeLxYs84vQlvNgBwLsRdnKKMGTaHviGHlGN7yxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTSwdRqMsr2QPb5OoRnGUNXSUt7DURvEmXvSI8w3G9nKTuROJxutWU6p-AfynukSEx-W55M0AzNJ3r9NNeSGc3Myeg665qguZM_GlBcs-lFvUpB8Ysjh6ILQl_NZ_1-sG9Z2ocbl3_8kkWeCP6rzpQ-XuZOai9Ito1yXL6cFT77HkO3mtjipLvXPAcx07AvkCpQTr-GOmT3SWnAb0bJ-8zLIAkflh9QEBxn_0TiqxNBAeW_ZvtmRhdfaqIX6jO0DvQrC7O-ika3s5UReaGnFsYyBJpJgaBE9hW9kY_BrTXJOjdS2MIR1oVRYhqDOSioFoYo15n5fsGD3Cq5Qo7kX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD6aP9fih06Hw8NH9zUK2VQ-wRkiuMer-ohEYOL-qJt63E5qzqLXnVm7b2C-nKZoh5lJz1voqKaZy1Ju0nCGbXNct7SZ2jYoRnII_WOssKTY7rtIlcqu92pNtEXiV9HW3tlqzNnrOJkuTGMZj9hPuED2ZkG-NUS9qu5EBDQ9RlA54S9JYS6vJNOXU34kMuTrdcwAL8-TsrNEsmuKj_tulyfuBAnMWKnEZQi_XzGmFVXjZiUqfGyndctjo-WzoFCD0xeIWJ0--muI1pz0Ryi0y18as-dxtVFyez6bsGeHeXMgFTxktEiZqsQK9F2XaTfmqoHKlOWbR-6AJa7Fa7Cvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkXYNm1AKpkyJofm1QHc8rvGY-QoJEhU5jPkfog5aGgBhJZrvyna76BFPmvzkxu2g1sm7HvBNPvyiPIxLAFqw6FZzOfwU3E-xJjdqWk4_gxgSQC45QvTo4QtehfwugMcBkbQQRagJMctyJ9aKVq8EoLgbjN0tYocMwRMkmGHjThjIRw3Kbea6qf7dKWBPtpVA9EGjmHH6DBM8Cqf37zSuZ0_kuiDNkwzckEnJik-HGYe6b7lo0crKCLfEvDsds34z_eLseaVKL8iYK8GYx_auAULGn5axG411ZzU1G_wt3eMUr7w5ss6pAEcpQ2o9oI1Jv772FWOG9yRcgb5iGFHag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-4h7Tm2xhdrChZS5gCWTs971FUtbwHC9hiAm5FwcsGa33MYjFQOAvOiOBA3Zawtylha_tf6ybsisitv7LrEzm0Zv4tYP9nTYBFVcIDAb0nMextpuRhle_1dbeUJ4JgupTZ_Dn5OJtxtIhfxbwK7E0A-r3_whJG9F3qRO3io7mME2W_uFTtEHTT2MEUPZYxteVPciIkq_RXlCBK91Hamao222g3p4kHJ3t9wRfFVpPnXeu-vj1YuqIleAliGE0f5RbKe9P_K3g3I4BBLEETXr4Wuyx5EFSTecbYT9xALo1NtHXWsxXMEamU2OFE6TwmUL5HYvZrnR73JO_y3ewAFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=o2QVT_9uOJBLEkZ4EzII3mtcW0KuIzekhyc_Zo_yd1NmTJE7O4d7rrgs_aYPlQKDLQ4oPLjqCvql7pEFZhQ8bN9G4Q5uFI8bzh1aa7T8o-PCvShBVN3cCdtC2UNMG6DZKrcYGAfUB283ELVy3Iys9tGfoKTHxklZg-hfjB3ZeocmXh7mKXGqI-4-9vwm2Ip1pbCORSVJUII8nuuJHK-6zWWTqb3oIexW0ybcvg-Ym7CYJmHotQ6BhjgxsA63Y1-3JKWS6Q5iaduxRQCk0bgUrHAj-t_nZxlR6jsioUy6hlOtAUatC9xDM5yNzs3PjIJFMg2v3SUBF_wLf-gtzbWrLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=o2QVT_9uOJBLEkZ4EzII3mtcW0KuIzekhyc_Zo_yd1NmTJE7O4d7rrgs_aYPlQKDLQ4oPLjqCvql7pEFZhQ8bN9G4Q5uFI8bzh1aa7T8o-PCvShBVN3cCdtC2UNMG6DZKrcYGAfUB283ELVy3Iys9tGfoKTHxklZg-hfjB3ZeocmXh7mKXGqI-4-9vwm2Ip1pbCORSVJUII8nuuJHK-6zWWTqb3oIexW0ybcvg-Ym7CYJmHotQ6BhjgxsA63Y1-3JKWS6Q5iaduxRQCk0bgUrHAj-t_nZxlR6jsioUy6hlOtAUatC9xDM5yNzs3PjIJFMg2v3SUBF_wLf-gtzbWrLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC599jkIGJX1-QzQ0iP293sqGM9ZPI2S3b799DCbIlm7Foj-P0d_uB5GzO8nfKE_hYut2-k0mwT38Mo7z7BKwn07afE02Y6bLz6GdiVozzTnwb5NubcY_d82yBlhNk3fN8aAdNrfYNRcH60gIYyJbaR-FaJ1EVlwErLiyturZpYQG_4R-3wxt0V6sV-Rz-6HEo8lqKFGaf3h-CePim62NBQqfalxpLGXVt7UaxiLIx-tOWmCxpJgnlPJIVXv1VZyLQTB1_rZRIWxPg5Y-3oNBrTCW3MGDDNOBIr5MUSrcGfGzdolQ7P4W6mKQ9ReGfYSuDPNM7DtntLyVNeUrI5n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkUYsMBvazE4RPakntHiv4PirtXbFWf_3lfS61ibfizwngsmL7BEBdSHPeI55Daq544QG9e2k_pJ6CCvbDOiPozhQYCOhJkVJqxCbZcRUZJYHvffezDUFIYgcdjitBaM5zsfyNK8I44F8W7Ojyud9xoeI8uE5aKMS26otFVNvjzmo4AkS-fKlsYA4r6ObRrVJtOhwmOhskMzCPg2fbBg5hLWfFnXWIvMCkj5yFLIUodAlR_Tt0M1YnBRf7cYD0b_UZBB0auv1L8tZEGSXdP-pivdxLeDQSSxNB1o6vZuOMIJSRZNGuyCbTGqMXlNmWOV9H0QtIgEjGbq1EdaVfMqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCZMjRConR-zLdG776cErCtQ8SBiEjMCyHzNpI4xIKErM9mYTeqFolmA9Z2M4P16IgAcwasnMfvhgm-06qxwY3dmJqv_yb2QamVr0hg-O1n1MdsnjxAfYCMZ0oiD7mRvxaYmu-F70UzYHCBscLws8b-YKG5UjZGLryjSmjUXu0gUSgAJwHLMRC5Ora3CRi2k9-7KHFle9VfQ6usph9-dcZ34jd1UTS2tjW6egxhzxDROqNYR86VMEr79gVELHRwx2w3jHPm6IjmY3tEqHzs7tdxm82YFmi0gBAzVJ7T8Sg2KNO5Qp2HUkGjA9bfilL0aYSaog7-fQRUVlMOqmWd7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMc7i6CcefyueuyV93kLX8PWxaZNFgdImB3fPbA9V0187uKG77PZAN8Rj_g4W1I5o5abdPMLx0etwQQnWonTpt5cYooXrVTUh7Q5BHiQFU8fEh1uRvVXvbG8EgT2zGHoQOe3-GIWx5PTYGhwS1mTWudZyW_Jp6QNL_gCmvv1FQaSVh1vzxE-gINNqQ3srMNRiOLudPRcyo3GKKhcRBMuS4jYVAbZMBaflaXhn8cwbeNkZpRpY_6Ab1bhvY4WL9kDa462ZrAD4O5tFZ3jk13wMXVIaktJIGFD_5QDQ5p9OJSDrvdyvU3VFaIVJTz8XQG7C7rKluzuS_L0SlaVM5gerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5dLn7BMjxKs9N6kY2_vg2FAU0R6h5B215DdrI5ZWNEcPz8XJc-xiTGSzSrBP8ardIZvQPvKWZu1hrxLB0Pe7GlKVo1fdxfw9KrGgqNS121-FmLR60i1yXNYvCl29WGtv-kuLGDFuZZk4FIunmC4AFvW-KXdODf3_WzgLIqTT2zYftUfKCDBNWtuMzimGKaGnDPoJPmeF3RRO4EXzBdlcWoMH2yQJmtAVTz-oOEZQYdOagEpd9YLLlCyEmS6gfmXWvbzaio4SUvcDItalJv6gZTM0DqqJQOrIU7DfQkaxcBydzRWvTS0V3pg2XqCeqog-5cdGsWoEDujgEWeHZNB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2AqQe0hvqsbB4t_JZDJo5SBjS5tjafCEnNIsgFJnS2bFfL5IhCMK9uDBr5TY1hwjzlGaawlJTy4LavYd7yvP1pXLQ8ljrMEwLuZsOtPTGUlggyVWtXCt7RxeGRMCoVwNwtTgYk1xMNAbm0ZeuW1OjeMCu7xld4kViZDI7iRtPkGs6QPWQ9nyT-7y8jL1VwGQB-dEJ9sGG5f57RV2SVFF8kz-t1x9qeKE3mnODaEy9e-k985qYh9hTVaXUzxMMatR6ynVnkyPN2LKcgs4VjxRLQQSHMS_PXPqkiDv8efdMd-8iSb4Q_3KGMx-ljUMRvAQVi9mwBKAcL54RmCDVw_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=te68lVmN0buWAxlpP4TD2yLiZsvrp6f_luR8XWBrftjmJKKNvhd23yaOzW1ePMm9B0zT3PEwEYwVM8uoMWRVMcfNWUNH1uxGcX3cNexGMoVOHkT5WT1Uwrl_au9n6wDkAgfQQsXO4ZioBFOBAUA8_1rtr5ud-Znw6wJrE5pPGfwJA0Ho82D9VN0JjCFkNhkaAISvcel75SR3ghy7SZB7fsBsZM3ab0XN2kOuLMNLBB9KYM5aEsjKo2_kNr-5q5p2YwE_WhkwCPr9C0q0r-jixcFx_raFZYj2JfXH2EJH3PwUBPrGVd05XaTJWNYWeF-VDLTg51WmF5l9zPKRRPcqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=te68lVmN0buWAxlpP4TD2yLiZsvrp6f_luR8XWBrftjmJKKNvhd23yaOzW1ePMm9B0zT3PEwEYwVM8uoMWRVMcfNWUNH1uxGcX3cNexGMoVOHkT5WT1Uwrl_au9n6wDkAgfQQsXO4ZioBFOBAUA8_1rtr5ud-Znw6wJrE5pPGfwJA0Ho82D9VN0JjCFkNhkaAISvcel75SR3ghy7SZB7fsBsZM3ab0XN2kOuLMNLBB9KYM5aEsjKo2_kNr-5q5p2YwE_WhkwCPr9C0q0r-jixcFx_raFZYj2JfXH2EJH3PwUBPrGVd05XaTJWNYWeF-VDLTg51WmF5l9zPKRRPcqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=HV9GYaUuWe0okBxuDMGBipSo7MdplcgHM1jZCa4wfuiqGYmv2cwt6D0DT7oh8Q6zf1-oEp97c9v_FJFjgOLRaYh83PGdzWBx4xtbaNo1v-Ofp6TY3034WflHB4KG5rvg9jM52p1fTdHu07ACLt59DUv4PD_gNSH73xhIGVLdLI0RsrgAJlxfrGdyNcAzg36vIvkOSwySx_Eogj1gC06Wp69DmjBfQd0QpAzFegs2wxBdQ54loCEBcOXzUsD99Y9W2ZuiEI62VJsOOIccEnXUydb4bhmKZTl50tRgM64T_eQAGB351laHTEINyYDBqZkZ4Zv5XMobhA_HlOrM_3CeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=HV9GYaUuWe0okBxuDMGBipSo7MdplcgHM1jZCa4wfuiqGYmv2cwt6D0DT7oh8Q6zf1-oEp97c9v_FJFjgOLRaYh83PGdzWBx4xtbaNo1v-Ofp6TY3034WflHB4KG5rvg9jM52p1fTdHu07ACLt59DUv4PD_gNSH73xhIGVLdLI0RsrgAJlxfrGdyNcAzg36vIvkOSwySx_Eogj1gC06Wp69DmjBfQd0QpAzFegs2wxBdQ54loCEBcOXzUsD99Y9W2ZuiEI62VJsOOIccEnXUydb4bhmKZTl50tRgM64T_eQAGB351laHTEINyYDBqZkZ4Zv5XMobhA_HlOrM_3CeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=YSp-R7E0pAzSftgJTZF3LutLENsNbcXg8Jaw4PW3DcQUiMn3-2YM16jbohtpU_i8hGHDyIH2MHWCfwCSsRTapz_nu2oFSeL_mp_geFHqFW9R6Ukil2GdTaceyqnlnpdvL4Lpnm0EYU4pdqIKDLUI3ZFt66fJs6SEF-fBPXjnjcqPbOG5wqigOXIxPK4xNpI0OXwFQK5E-RCow0h6ETscMBvpsZ8OqbvHH9mamItjwSse3bXOO-mmp7aziBW7Z2B_DjqBidBi_AqCmXkgO6PXFjYiQ64nwWfxGjF3wL5e6EVvZEGNfmayQkT14rezhdDLV4ltAkk7EGxj_lWVamdQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=YSp-R7E0pAzSftgJTZF3LutLENsNbcXg8Jaw4PW3DcQUiMn3-2YM16jbohtpU_i8hGHDyIH2MHWCfwCSsRTapz_nu2oFSeL_mp_geFHqFW9R6Ukil2GdTaceyqnlnpdvL4Lpnm0EYU4pdqIKDLUI3ZFt66fJs6SEF-fBPXjnjcqPbOG5wqigOXIxPK4xNpI0OXwFQK5E-RCow0h6ETscMBvpsZ8OqbvHH9mamItjwSse3bXOO-mmp7aziBW7Z2B_DjqBidBi_AqCmXkgO6PXFjYiQ64nwWfxGjF3wL5e6EVvZEGNfmayQkT14rezhdDLV4ltAkk7EGxj_lWVamdQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=cNFbd--czywaLyFZL0c_Fvxu2GvPLy7ztT6QWsW2w0iHwUdT_2ldiWrmP3cjSe9wL1FJ_IY_Hg72OLlNWVIu5DWKQuGOplTnjurwC7V8JNfHWGAshfOuErGbDySl0zCf3ye5lpHshN6Heber4bqBGC_xrBwC7x-4Tkl0zOIDkQ60bBgFoIQO_g3tvQ93jv_SDpNAVkqSkVYtzfaf3DkL-fTlcuPT_FDJCiBqtDuYZIzGT8TvNQy-GGbMyesEmsV3ptDGphODbA322XMpKkZUKlWaQQF_dZ583rx2Z7hXGaPfp3unRMTnb5w66wyv1yr-4OVR-RJeLaY68O0-qQIuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=cNFbd--czywaLyFZL0c_Fvxu2GvPLy7ztT6QWsW2w0iHwUdT_2ldiWrmP3cjSe9wL1FJ_IY_Hg72OLlNWVIu5DWKQuGOplTnjurwC7V8JNfHWGAshfOuErGbDySl0zCf3ye5lpHshN6Heber4bqBGC_xrBwC7x-4Tkl0zOIDkQ60bBgFoIQO_g3tvQ93jv_SDpNAVkqSkVYtzfaf3DkL-fTlcuPT_FDJCiBqtDuYZIzGT8TvNQy-GGbMyesEmsV3ptDGphODbA322XMpKkZUKlWaQQF_dZ583rx2Z7hXGaPfp3unRMTnb5w66wyv1yr-4OVR-RJeLaY68O0-qQIuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=lt2tZA26OQeQ0gJXJkd59TZXu0OYjzo5B-h1YwDVuJd6P4DXFJDW9zatUdf5QRDOc6LjfuLiGTSTBr5Bwo3KPu01g-aufnGYk9Xi5d7ZFbpCHdUrfUMEqH8oELb71ctjHdnI94WRxcMAq4mHc8Mmy9t80KadLjKwNTuVmYdixN9qhfPk3bVtZtxPLW_Rj4nl4ixL8xECiJslx2Yn8EQH5-KqqAcS84nsGlfZdOIe-tZluN7HTp2omyFTnmDykSgMwEdZxtg6--MnWsxVShlS8OTumSfMt9pCtPpRXAptuh5hrXjWpMO96KlzQ3nmhajmEvrN9YyYYNgziEhoKS0Qwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=lt2tZA26OQeQ0gJXJkd59TZXu0OYjzo5B-h1YwDVuJd6P4DXFJDW9zatUdf5QRDOc6LjfuLiGTSTBr5Bwo3KPu01g-aufnGYk9Xi5d7ZFbpCHdUrfUMEqH8oELb71ctjHdnI94WRxcMAq4mHc8Mmy9t80KadLjKwNTuVmYdixN9qhfPk3bVtZtxPLW_Rj4nl4ixL8xECiJslx2Yn8EQH5-KqqAcS84nsGlfZdOIe-tZluN7HTp2omyFTnmDykSgMwEdZxtg6--MnWsxVShlS8OTumSfMt9pCtPpRXAptuh5hrXjWpMO96KlzQ3nmhajmEvrN9YyYYNgziEhoKS0Qwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASW-oTVV0kZksUWixqY1ltpE8sE71NHKwOMdl0ADq6cMbG2bGvwXA-G-YzGsss6sRE8eCM202JxDTSAj6rEXCNdG0ugVgZRvLbpAA3eTAyR42ILmjh_zp-z0Lf8_VILY9iN5TC3caewmIUPpCPxWnyQLV-Dph1E97xQ1-E154QUj9bCJe89x9vM51wij05hxcPJtac1l8FQkLLK5N1DfukKoEgJevG6ePnEPt4zfdrh5LpKRssb48KuRJqtsRLk4uHd8PhUKGRL-ri5Fa9_DV-038geKLp7IuvlhnXLrxdpTL495HMdK3uvLnCCCBX78mqroxAUVzK54SyijU6ENRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUoiNuUIWmwhQbqLtONV23rbX6mcEqbhaMBp11BeD-3KyacG7pJe8gttTPk8TevUdBNAr_Yld3zPPwlv1VMknYgPI1WM7ZttR6i3-RDlPqnn6pOqWp2bu_zk8sATZOXzx5tmulRNtePVxr3quujDNpAWBWaxZJt1fVZw55s4_sN-k4zg94A1xxLaJa08PQoLoIULefiYyHxQVvXWtjlwX3whP-Zn6boNKTgOyS7zirn1Rga3Hc7G-RH8P741SmdWpF6BolRB-0ZWhzWiTrHTpFM-ci6AB0dlxfWxH1kLb_AfOHohhfxXy34mWboDFF2kc9d40A4H9E6CeHa6vHApaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCgBKWWlhwvvvkT8pACKJceOpC2uUjTWdb4ClLY_Nhdehe7adBYKXXMR-8QK-PGogI6jK9Ef4mUt9vNoasjRThs2MNwrNTQ-Zi0Q71pKxVvb65V1qLNd1jeBckbV8II6NAJhMNF57HO6prARbithg2OnmTWWmOHszEwHS5U_CDFUZTWXrgshH6IkicSYwRsUAVwFqvKRnAOvNlWrZ5Iy3HljZOLa8cRIjJEssOyt_5_npoid2hZwzHa_fH7tLtZIR3qilmF32W4fYZwHxps1nJ86jB3FZlZU6uiFOmmwVL48YmUuEmopWabvS5G75NHHakCZ9FUVVY_urWcPtRZw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDTWIVz085qGeh-us77ccRK9jlN5BenC9vx2mM-5rQrnjLLvPZk6ZnsPqb5a1-i2jENQPpHmxoiRKztwb4qfOl6wzzE5YchAWVBsO3iOW5NrWkHnmgD5DQjXk_R3ikGbPQOtsCxT_jJT9DjliNG3yRt4TdhRSPlqn7eGOy7KLRaDEn65QJtDSANHmi2XYlczZw3CmuUGBmm9FsmLUgefp9iyYBi6N0VkypJsuRQuN4ZOCQoLYOhcTcvQbhIXgFjHHiQTGTBCwltVa0AY-P-OQv9apD9tK2IBi6E0vT51wLJKa-zzU1lx_YfG7BadEE8fMmyyAnvJC0LekJ3gcPA8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTLx68NYnmxLrCu_NKWqBYz0HpiduycSeH3FAgTrxyJzlOSkBQqAjTznjmqaIJnvkT_m6YBAO7BtrCZwRsTMn_JaIlJa4QWpCEt2iiTtPSTUMiqUk7fQ2hJavBwvAmIcnnwBqP_gIqdfwRhj4hIWmNwv4onFTdBwS1fS3vRkt9c6HErIMdtZ2b0yw9mjlpJKLCuF_BR9Nz02AGfFzUcflLxBdigGIgCiGkznLoPD8Xf7x7_2ooJVFwiN-jlauurkfZPm6mwiUCuV2j16LpqxGzJtj7vdZLxOmfBad3L8n_AVcLiUzc_BGTtyDSoExTpv6KoYbjsAXOy0Z7NBZFJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
