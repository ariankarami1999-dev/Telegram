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
<img src="https://cdn4.telesco.pe/file/ngRiI43z79T5slZA7coKcTX33-02lPZQaZzaDwAGESXqsIPfccW2UIz5i75jg_Z1h8zdh6Rj5RSnzMSXhLuTKC1XP-FTcSAd-st7jmniAz26nmYvjt9agHTSWn146UtFrvT8nE7Mc4LrnEYdPlMCxduwcH4TdOJ-T8-w6EUqtedMnWIfyjjWopwvgYPhdVBwqtyRbxCrRHGdH8IS31hLd_82jD7f-5Pf3VTPbme11RrHtKpVgibvQOBFGngZhABPVK6khmcL959uMRYkeHQRbnVQRPSp87ffHCUCToHXnR6EhYZnrImm1YSDI4ZxEFN80E7KUFiLc8PpSxLuUZeZ2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGLcb464ywRpQ0kW5v8hsDBeFNVIhKhRHRGPgApLW3X2cNy2fKY9BGfjKjYZXyfI3fCVILVOLhrhXJF4PdVeYkCL-AplaGwdXOFdUvx-J5KEczu_nTAf992H2xITq5x5-Xr-HswcyflH4wyn42fhuFalA4vG0PtLusuRpwU1FuH5UpFV9YQPyguCkLkKQLpy3H898-GzKtTihLldIu8Fc8714Qo4lJxSi6uns22NTnmW9vbIm0WakcIw1QkCU-c61rnADhFjxBAb-Bqq_oGE1CpKwnewST2tBRO9C8Ph3m22Mh11rGDfpKMbwYNJHUS3HkhKsoaoY4XEA9LPkaBRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPTszGaq7T4Yts_QniOHvnxrKIAej2Oj7-SS3e7M4lQnAq7JwTZS5VLHJHKaVO7RnuvPNXYWZaA_MNvvJBOEkMg8430fvZOXfSh6Hm2MlSpn2wnY7vfk-U7l6HaqSiJn56ML2YHtnzLBPn0f6yWmG_tYYHAJAIsZZdWQARINosld7h2R4c4b8dDI8MK0lF_m-AuKLHE92vHxFmEKQSYuJt57RTs87J9nGtoEyED72Tft8yZIeQk7nJy4Oaxn6ffZtesMdsj32dk7dr-vPr10PPWdYlR8K3_2INuZtpAU0Fd7TGZU92eMoYftP03Y96Ha_m4vyQ2TkYeNu0AgTNHMGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=TJHEpADlCMe5Gh6ahuAGshAw_d7RDn2koglXQEhqIw9YbjYZjzkUtrVqO4LQcrXnRS43T2GrU4YvNf2uvUrttxFZR446SOBi7fcBt1PPGJs-Oq9wG6pUFs-TWHQdXte3lno4JYQNXOnAr6hNs73SAT4QPYOayxv90P4c0gGPmHLEsjnR_A1xpAOuI4jL6D0MT-xktyg0RMeMHXztXGIYt96iJbQaLRuBpLfrT9Za_aKMPaToT6YJp467Z5yPZIIjWJukBtYIeMFg29fCHJoztBFTJ46jaIPEjxOgn45xRaTaOCAaOR3x8qC1mpO5gMqwhdv_eyyrjHDLpUNGtEuT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=TJHEpADlCMe5Gh6ahuAGshAw_d7RDn2koglXQEhqIw9YbjYZjzkUtrVqO4LQcrXnRS43T2GrU4YvNf2uvUrttxFZR446SOBi7fcBt1PPGJs-Oq9wG6pUFs-TWHQdXte3lno4JYQNXOnAr6hNs73SAT4QPYOayxv90P4c0gGPmHLEsjnR_A1xpAOuI4jL6D0MT-xktyg0RMeMHXztXGIYt96iJbQaLRuBpLfrT9Za_aKMPaToT6YJp467Z5yPZIIjWJukBtYIeMFg29fCHJoztBFTJ46jaIPEjxOgn45xRaTaOCAaOR3x8qC1mpO5gMqwhdv_eyyrjHDLpUNGtEuT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=pT3DAyoE8UCMfYAMDzFkJ3O_4Zq00_sR6h6REEihCS2u_l-LcOFIds47fl9e1sDHdbeBzZcJuYcaTBRAtUu2Y3AGRfdQtQvUEVd9UjS2uRM6i-F_WejMhFJj_bQqc0EEB7U0R9HT4nKCyrU8wnOSKdLovcuM_9DdD1BSAMG_jFfliBKMWDYtIFny4H-AmQ0dpBzV1NvCd85YIvfRsZmy5gGxbXxJvIRPjKUTnnh3ZAZjoKIoRixdjN4ASZ15_55q50SlY4Liq0wxVpnrQylEyGshK2T2tp2fMtLrE9q9dEhoPsaP6sWoj8PqmfJF7bMeoQnWGwFZTGzspn7ZPugc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=pT3DAyoE8UCMfYAMDzFkJ3O_4Zq00_sR6h6REEihCS2u_l-LcOFIds47fl9e1sDHdbeBzZcJuYcaTBRAtUu2Y3AGRfdQtQvUEVd9UjS2uRM6i-F_WejMhFJj_bQqc0EEB7U0R9HT4nKCyrU8wnOSKdLovcuM_9DdD1BSAMG_jFfliBKMWDYtIFny4H-AmQ0dpBzV1NvCd85YIvfRsZmy5gGxbXxJvIRPjKUTnnh3ZAZjoKIoRixdjN4ASZ15_55q50SlY4Liq0wxVpnrQylEyGshK2T2tp2fMtLrE9q9dEhoPsaP6sWoj8PqmfJF7bMeoQnWGwFZTGzspn7ZPugc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdidU8RdJxpe8ePdxbY-Hm7f2UDMjU1O54GqmJqYom01tLZbLMFiOOVoHC0QbKfThD99iGLeYmPLJfmx1_XQtKFH8OjuGA-vetoK_qles8jSmeEJrRPK7UVkpyPvHiu3KLI9Q-Kzyf1mGdaiSHd3Zr4jt3xMggYV-0gUVibGwHnSk7wj4M1tp_JPZEHRnGKcxCXmIwSuMBNQdOvii51nUV-n9IVKLpYVMl9ovhS0JZa84tPZ40HtmrHGX4IgOfxpUsLMgiTNtp5-lQaOV8hMBOPJOTX5oWTjSdrBQzfTcMJv-QRNvrUcD6g2YoU5hySPs5wEgRWmNQH__P-sh5uxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=mQJrE9SdynP1X04SfLQpjF4INddbHVtuCT68ufdPi4nJGX3DxNlFJHL_X6PdYuE0WXnhE3Q1xy0MWVSYtd9d-Ftnb6KHPaJT_09pPKEV7AWG_y8kFMqSDGEhbq7na063ttnTwfNNyK2kAbALRayc9f9nPCLjmgKbA891mD5jeUebIy65ON_2172l0Q2ythUeO9OOw4F964GsEq-L232LOzjzRozN9v8dJ5XyA1BnxCr2o2bsYBZ6Enx_YOIw37wF4uFIW2IYa3sozSeNE0QS5jasl_cRoFueCnMV7n9V_V2-ZLh0pBLirIX1mif-PS2gxzikVaTAV9jh3NQzYEirVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=mQJrE9SdynP1X04SfLQpjF4INddbHVtuCT68ufdPi4nJGX3DxNlFJHL_X6PdYuE0WXnhE3Q1xy0MWVSYtd9d-Ftnb6KHPaJT_09pPKEV7AWG_y8kFMqSDGEhbq7na063ttnTwfNNyK2kAbALRayc9f9nPCLjmgKbA891mD5jeUebIy65ON_2172l0Q2ythUeO9OOw4F964GsEq-L232LOzjzRozN9v8dJ5XyA1BnxCr2o2bsYBZ6Enx_YOIw37wF4uFIW2IYa3sozSeNE0QS5jasl_cRoFueCnMV7n9V_V2-ZLh0pBLirIX1mif-PS2gxzikVaTAV9jh3NQzYEirVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=aepYTc8Mh80-n1bRIX3CxukA-7VNr63ETnzu4FLJ6bI9MdcimHvSsJjMo1E1yuoPeYgs4uWchbcWAkYHPZrhR5rJPGqlhFaIpMYUaqJw_84zCSMWMuhtIvkeBoT07tO8tt2JvnkpNujWZrpyBR3w8tjSi2cedtKtmTjRgX8kZ1bTFEQIzLLuNwQ7y3iDcKmlglTr0Xy3ASgjfLbYygVnr4vW9WHxBfIKy85T6S7i7DyhqPH-GGqWzgcRE9-OEo4qZOiK_5K0DpzorNi6URFIQYYyX_oVns5N0yR_TuWWDWjYxwlbQzxDno58S9n6L34twqw_z94lj07XdrwAQsZj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=aepYTc8Mh80-n1bRIX3CxukA-7VNr63ETnzu4FLJ6bI9MdcimHvSsJjMo1E1yuoPeYgs4uWchbcWAkYHPZrhR5rJPGqlhFaIpMYUaqJw_84zCSMWMuhtIvkeBoT07tO8tt2JvnkpNujWZrpyBR3w8tjSi2cedtKtmTjRgX8kZ1bTFEQIzLLuNwQ7y3iDcKmlglTr0Xy3ASgjfLbYygVnr4vW9WHxBfIKy85T6S7i7DyhqPH-GGqWzgcRE9-OEo4qZOiK_5K0DpzorNi6URFIQYYyX_oVns5N0yR_TuWWDWjYxwlbQzxDno58S9n6L34twqw_z94lj07XdrwAQsZj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=ToQ_6u4U5xkqBjqrYVLtbv_iYvFM5sCYql7Qi9qP-9RYVIXSZ27RzAdHCE4jjRSNQCiIA-TKW-UpOlvoubK9Iw5NbHCvf8q8lKbNl-pOOn1Ft5OShqHv6muJ661WVmQxidNuqaMF2LlWMKfyV83BrzWZ0zPSG322MGfpyh3ITv3bYkiAErZH-AZY1lOf2zv7uJwtXMuy9tnuYB-G-MZ0wV5lj91U92MUuLhgYFk8gT8FsxLqwrBoEgcYjm_rEhwuN6mgFD6AK-Ip1T_mBGmlvf_8kW_5YznxNf47KducgiXf7b_NNnRGyfSx5AwhdJaIynEOeqsAUW_qNHPVUnnC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=ToQ_6u4U5xkqBjqrYVLtbv_iYvFM5sCYql7Qi9qP-9RYVIXSZ27RzAdHCE4jjRSNQCiIA-TKW-UpOlvoubK9Iw5NbHCvf8q8lKbNl-pOOn1Ft5OShqHv6muJ661WVmQxidNuqaMF2LlWMKfyV83BrzWZ0zPSG322MGfpyh3ITv3bYkiAErZH-AZY1lOf2zv7uJwtXMuy9tnuYB-G-MZ0wV5lj91U92MUuLhgYFk8gT8FsxLqwrBoEgcYjm_rEhwuN6mgFD6AK-Ip1T_mBGmlvf_8kW_5YznxNf47KducgiXf7b_NNnRGyfSx5AwhdJaIynEOeqsAUW_qNHPVUnnC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=AN185fbOb4u9kOZeK73m7-yBC8o-nGMbyB_ZEgaVZCAuSQok1AlY13d_AxxLjEJ71cAyCLFMIWjClKwuXdl8ZtRw50NEM8Shfl3pkI3UFxHQ7e9NE5__o8ogeX5tRIxwMmckDa9v1b9ygJ7kbnl0RZnd33z65Foe3b9_2F49mj5Nag9dfPyhMzVH06J2SSVjVNOMBKYbIBL331dY0lfULfjqq5Zb3GYUCeuTRknA18OEV1UDz0h-M2zZhBazDdSGy59Z5IEJpwmQwocoz0QoaeLDS0v8RD2wuW0qb6mKsbABI6pI-o2jtEEPJz5xe002B2-vwZhcErYPrms0ta9K3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=AN185fbOb4u9kOZeK73m7-yBC8o-nGMbyB_ZEgaVZCAuSQok1AlY13d_AxxLjEJ71cAyCLFMIWjClKwuXdl8ZtRw50NEM8Shfl3pkI3UFxHQ7e9NE5__o8ogeX5tRIxwMmckDa9v1b9ygJ7kbnl0RZnd33z65Foe3b9_2F49mj5Nag9dfPyhMzVH06J2SSVjVNOMBKYbIBL331dY0lfULfjqq5Zb3GYUCeuTRknA18OEV1UDz0h-M2zZhBazDdSGy59Z5IEJpwmQwocoz0QoaeLDS0v8RD2wuW0qb6mKsbABI6pI-o2jtEEPJz5xe002B2-vwZhcErYPrms0ta9K3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=ipa7L9rB-DQZy4In1P6ci7jddDPNMvlPLqmcC4NKWwdihERbgyeFF_9AXLMScFeWAj7XkAgn-Q119xpesSkwVQkKlzZiNwPcycpk0f0CHYyylFbDcXLIP_Vt_WL_kZLR0bMG6G4nceA8JJqUqPrQoBRMFKYk8aki29GB43KR-T2HLg-6FkqvNDpT0stuyxVLu5UwuwYPuCI6WmocTNhnVvZ5WpKrci6E3BmQyo2y3jNxxeR4CVAL5gyG_4En6cdhbQtO1_IWV9mcm1DtwDt9SXXzkP_5Rq4jfSmgJUxJVbJVrWmFmeHXJPvif180Qh0XBQUhtW2uoyUR41o4pyo-yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=ipa7L9rB-DQZy4In1P6ci7jddDPNMvlPLqmcC4NKWwdihERbgyeFF_9AXLMScFeWAj7XkAgn-Q119xpesSkwVQkKlzZiNwPcycpk0f0CHYyylFbDcXLIP_Vt_WL_kZLR0bMG6G4nceA8JJqUqPrQoBRMFKYk8aki29GB43KR-T2HLg-6FkqvNDpT0stuyxVLu5UwuwYPuCI6WmocTNhnVvZ5WpKrci6E3BmQyo2y3jNxxeR4CVAL5gyG_4En6cdhbQtO1_IWV9mcm1DtwDt9SXXzkP_5Rq4jfSmgJUxJVbJVrWmFmeHXJPvif180Qh0XBQUhtW2uoyUR41o4pyo-yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6H-c0zMa68aZcSD7vTWLYBziAum_Tx0xp75acXGglNdkKQbzXdy_1fuFfJjVApHsmTHwQsZnDFoOCM37dwl4UanOelLnWSjy7vlaDfUYQ2NMLWpnZXjx5TgOSk7fxotKv-uY6rnl0Uy9eJpbex8qM0ewUY3Td5JOWlDxNiBNGOuZpSgUBFlrY_SgB_7rntC8BMxbODKfrwcKdkglCaDh76zMOyYX_2MczGXVOJIzT3WCnmdwC4_wqQDtYzR3IbTl2hUapuqc0lnVEP2mcpxy9ajoX8__nD2g_S-lpbcv80QFRgbCxm4e8QIPp88XvHyNXqecnmqykx6BkAZ2WAeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzxsvq6m-knJXcHxKcD0Ue-Vc-_hzcT6fOXB9NCZYUI0NsXpzdu7omV8c9G0eydR_D_zt5MDjShPKcwCRP3xIasjT3K2ssElV3eNaZRTsbWGdxRQACyc6pskC0vXNEV3VUsndAbkK9l11rvYeQy7Ao6A_6M-ojPdpVGTHfc_udgCUhpiZMFkhJU1Qh0V2YaivoEJ4BRwlxcvYRUkU9v9VZrbiYWEXO6AN-O39sKnXDU8QPk_ATibHCRvhW53Vqkz5MtqdSqEUMKL2eGfMJiA-Bia0lUjBfjibGcmfjQj3oni0WiUVS-0h8T_7ZKGVzwMyqwPqlIE6pAGZRCk8Eo1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=rIaxJec51KH7R1ovIgu6byq0_aTq-IlL_WjBKzKEuRsQTG0h6AtEtx-F5zVBtw_q7ui_K70NWaD363ZHnEdwUnaYeAXquXaZtlyqb-YJhcoAR6SHy7TXjV6YV-ttpJO4PLdpgN-YveCIUd25fcMnjGeJK1z5D20wjUu-L8I7wJ7AyDtgu7tCVJ-MPIe9GztGI3VWaZAW9aalMoV_lVsnXYRYyHOz4-sLQhaXLjaXewySgxdTRwaQIAIU7NYp1CwdWMJE_iICxXyJIFcHy2ITVsYM6N0LjWzPEH8Dxrm02DSt6b0Q4iCyO5JvW2NT46uf5h1r3eTNp5cxNrh7N-l5joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=rIaxJec51KH7R1ovIgu6byq0_aTq-IlL_WjBKzKEuRsQTG0h6AtEtx-F5zVBtw_q7ui_K70NWaD363ZHnEdwUnaYeAXquXaZtlyqb-YJhcoAR6SHy7TXjV6YV-ttpJO4PLdpgN-YveCIUd25fcMnjGeJK1z5D20wjUu-L8I7wJ7AyDtgu7tCVJ-MPIe9GztGI3VWaZAW9aalMoV_lVsnXYRYyHOz4-sLQhaXLjaXewySgxdTRwaQIAIU7NYp1CwdWMJE_iICxXyJIFcHy2ITVsYM6N0LjWzPEH8Dxrm02DSt6b0Q4iCyO5JvW2NT46uf5h1r3eTNp5cxNrh7N-l5joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=F9XoH5mI9GPdVUkgq0TYPMqXuWqSjd69YwLzS1l_BtBpX8pR7LMILI7j5WnVv3YO0kAkUJoWfkJDQj4Zb8ThQXQPJKnFhAWtaCCx84IvxjjChgKsNm3Hk3VsAajZZRHWzNjJPCtuwzbCfIDhQ-sKuRhb18ESqgg3bQp5eXI3cx-GQsoiO0JguES53kCqk_QZYoEvpGkHmYuEqD8O-yilxOlV8YzEQWR5ofH5iz4frNWmaMIPfAyvLUI2bYiBmEu-Q5kNTetnIY6LDO56QMUsHy2SH64RlDmpnLm9U7VbKTtBMl7EgVpVtu59J8K3cA2e7RhaQ78xrwSS8kMQMFNgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=F9XoH5mI9GPdVUkgq0TYPMqXuWqSjd69YwLzS1l_BtBpX8pR7LMILI7j5WnVv3YO0kAkUJoWfkJDQj4Zb8ThQXQPJKnFhAWtaCCx84IvxjjChgKsNm3Hk3VsAajZZRHWzNjJPCtuwzbCfIDhQ-sKuRhb18ESqgg3bQp5eXI3cx-GQsoiO0JguES53kCqk_QZYoEvpGkHmYuEqD8O-yilxOlV8YzEQWR5ofH5iz4frNWmaMIPfAyvLUI2bYiBmEu-Q5kNTetnIY6LDO56QMUsHy2SH64RlDmpnLm9U7VbKTtBMl7EgVpVtu59J8K3cA2e7RhaQ78xrwSS8kMQMFNgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gH2fibY0-2xqkNvoMZ1gwH5karxUDVfEWK992RobdYm7-JWNW7hmiHM_KRX9r0jOpCAOljckeARcw036LVKNcPsfuNdSpPFXiipFtHnyMVx4Mz-m6h4ZGOtm6e9wgowWgdfOc0KFCgZU1Ti-jBH_7yvJb1w3AxCdr_cPptVr3OssWvZwAiXw2ozzWdSIIYyjwG5pKIc8AsfvzWlJdgfi7yzp2rzmu64jE4YYLpkLhpdcWv3jANzxIrluFQbsOIcbT04XqKUY-m09q4NGmtO-uI1Dh3V73S1PTJC4T1sovDKKwf4_xC0LfFHzH3Hk25pLyV1lZZZWVDEEKLR48oQ-9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gH2fibY0-2xqkNvoMZ1gwH5karxUDVfEWK992RobdYm7-JWNW7hmiHM_KRX9r0jOpCAOljckeARcw036LVKNcPsfuNdSpPFXiipFtHnyMVx4Mz-m6h4ZGOtm6e9wgowWgdfOc0KFCgZU1Ti-jBH_7yvJb1w3AxCdr_cPptVr3OssWvZwAiXw2ozzWdSIIYyjwG5pKIc8AsfvzWlJdgfi7yzp2rzmu64jE4YYLpkLhpdcWv3jANzxIrluFQbsOIcbT04XqKUY-m09q4NGmtO-uI1Dh3V73S1PTJC4T1sovDKKwf4_xC0LfFHzH3Hk25pLyV1lZZZWVDEEKLR48oQ-9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6737mHcPZjIjhqFd5nLOteQBYP7Q9NzgWoSmVWlqTP_kK-mjuWmE-EcPN0iG5wPcDk4Ey8cxns5hNO8tBwjYsulmRVgDCLW6EUhl2mmvsmH5ZYhe28ib7sWsEhab_UXYFuL5anYkaT41Zkq1BtTMBb8DsXXUf1taq_GYuGeRdYqzzyui-PSmk2BHBxuY-P-XnOjUV05YcSW3FvTQ2HLMG8vgshx0NXiRyNMulJkKZHQr3ZjjM70pVNkMtRo3X6T5OeHbY787_wj3irfPd2lim45y-lh83bJV2vk3_czoJpczD9rw3f1E4ilDbvhASBELeXz6KlStRGliSz8qC3RadeCUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6737mHcPZjIjhqFd5nLOteQBYP7Q9NzgWoSmVWlqTP_kK-mjuWmE-EcPN0iG5wPcDk4Ey8cxns5hNO8tBwjYsulmRVgDCLW6EUhl2mmvsmH5ZYhe28ib7sWsEhab_UXYFuL5anYkaT41Zkq1BtTMBb8DsXXUf1taq_GYuGeRdYqzzyui-PSmk2BHBxuY-P-XnOjUV05YcSW3FvTQ2HLMG8vgshx0NXiRyNMulJkKZHQr3ZjjM70pVNkMtRo3X6T5OeHbY787_wj3irfPd2lim45y-lh83bJV2vk3_czoJpczD9rw3f1E4ilDbvhASBELeXz6KlStRGliSz8qC3RadeCUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=r4h89CcNeXy9iqt2h5F7cI3MKseAC1Np03g56vAqbzqPaE2KMnZq-BaEMvMgdmngx9BlJ_gqXoSlCExpqKqYfYP10OzhiY8Jsr3SRYzcyuRfaa-Q7g1PIuBKaKORF2dE30ErU8ZBhpXsMD3DZjMrK82Kvrff3K-d6jeyOJz_QbiPKiaJ505WywGum8DPEZpCdxN0bIovmeSvbX5XDWF83PIA4J2QDslZw1O1mdUPM41aH9A67NSQQzTfg_4-10f15KplEwV34_AHLRjhCIfygamNOBAGyGlmC8MC7kwQUh_ryrCRqbn4m9UatpsYnPrG6w3W9Urs5oKHAG5RWnoZCibzAvzfL7jrPIAvkXx3_nhJW8WS02TEAkHsY_sRiKjJn0ld3in8aoCtNI-CmobNTGuRorW-0Nj402oCK9-ezblThtDHALXQg2aGQ__3yO9Z7thgVnu-c_t16QuUL33Upgmsrn_w8wIn0zVYWIq7zB2YYJPl15WN8zOhYQBXeUiaIr8MrwlfmbDbUkAe_TQ28RoQUJuvagTnAK_6k07wvGjkjSiFIXd-rzP7DZqyZR007q8jBEy_UmTddTVVYkb8UsBjoggaTmGMQkEANnfbFRuy1jH96GwETCNpUTxgPuPbRTGLo4dmWtdswyWM8seS-3WoXsPER--jRLZPXZwY6s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=r4h89CcNeXy9iqt2h5F7cI3MKseAC1Np03g56vAqbzqPaE2KMnZq-BaEMvMgdmngx9BlJ_gqXoSlCExpqKqYfYP10OzhiY8Jsr3SRYzcyuRfaa-Q7g1PIuBKaKORF2dE30ErU8ZBhpXsMD3DZjMrK82Kvrff3K-d6jeyOJz_QbiPKiaJ505WywGum8DPEZpCdxN0bIovmeSvbX5XDWF83PIA4J2QDslZw1O1mdUPM41aH9A67NSQQzTfg_4-10f15KplEwV34_AHLRjhCIfygamNOBAGyGlmC8MC7kwQUh_ryrCRqbn4m9UatpsYnPrG6w3W9Urs5oKHAG5RWnoZCibzAvzfL7jrPIAvkXx3_nhJW8WS02TEAkHsY_sRiKjJn0ld3in8aoCtNI-CmobNTGuRorW-0Nj402oCK9-ezblThtDHALXQg2aGQ__3yO9Z7thgVnu-c_t16QuUL33Upgmsrn_w8wIn0zVYWIq7zB2YYJPl15WN8zOhYQBXeUiaIr8MrwlfmbDbUkAe_TQ28RoQUJuvagTnAK_6k07wvGjkjSiFIXd-rzP7DZqyZR007q8jBEy_UmTddTVVYkb8UsBjoggaTmGMQkEANnfbFRuy1jH96GwETCNpUTxgPuPbRTGLo4dmWtdswyWM8seS-3WoXsPER--jRLZPXZwY6s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=mOUVpF7Nt69lxW8KssW62GYDx5OcJ9nZJPzrR0P-_uOWeiZNbVupVOAzBLfh9IvCFCJCKs1eBz9JuLQ6swoBVfrNIztnf93OBgKJCutrrXinB_0bRg9tn6Etj250GpKznnQEbzpA3tgZ9htVRY1kyjxS5jZ0bg1ok4r4KBpDC-ulJcND0-kNnMvzzYtHYa79GAmUPI0XYouWDIYv5gxPMTpOeTYDw8x9dlDgd_iHZ8vC3B6wdx1TjvTAnIo9J0cZz-DmvIIKOH_cyNKqokng5C69X-h1awHsy4lZJLWlrrtgmDwXXPGgPP1rO63f2LvjhYz4B0V9cLk-8t3nUx71fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=mOUVpF7Nt69lxW8KssW62GYDx5OcJ9nZJPzrR0P-_uOWeiZNbVupVOAzBLfh9IvCFCJCKs1eBz9JuLQ6swoBVfrNIztnf93OBgKJCutrrXinB_0bRg9tn6Etj250GpKznnQEbzpA3tgZ9htVRY1kyjxS5jZ0bg1ok4r4KBpDC-ulJcND0-kNnMvzzYtHYa79GAmUPI0XYouWDIYv5gxPMTpOeTYDw8x9dlDgd_iHZ8vC3B6wdx1TjvTAnIo9J0cZz-DmvIIKOH_cyNKqokng5C69X-h1awHsy4lZJLWlrrtgmDwXXPGgPP1rO63f2LvjhYz4B0V9cLk-8t3nUx71fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=V85QTZjHj_MT5NE4Xpv0oIHE6UG5VCJqujGWDkS7_umJAsmV5SirZCGi4Fh3dUnepZSjYuzsnEIiA9M3h7nDR57nVdJodbZiyFH_jnc7fQhdl5btZN_Ah43iuCNvLcAAhF7UEsJYYPsHQfzauP27NzikUrkXPn9751TOzrVnpDaTa9jgeeTgrv9b-yXi2fhkrQt8YRcO2p79tFjhKOmrmXO8ncpCv8jsTM-oiIUH1O_DgSRexFCwWxihq3JPblmUwzcdK9biX4zHjygmnMVTWIhIjOGdRE504rrwEuBsFpdsPjJD0YuWj98_sJhHFyqLdSaY9SFBkLeKNi2r0Z3bLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=V85QTZjHj_MT5NE4Xpv0oIHE6UG5VCJqujGWDkS7_umJAsmV5SirZCGi4Fh3dUnepZSjYuzsnEIiA9M3h7nDR57nVdJodbZiyFH_jnc7fQhdl5btZN_Ah43iuCNvLcAAhF7UEsJYYPsHQfzauP27NzikUrkXPn9751TOzrVnpDaTa9jgeeTgrv9b-yXi2fhkrQt8YRcO2p79tFjhKOmrmXO8ncpCv8jsTM-oiIUH1O_DgSRexFCwWxihq3JPblmUwzcdK9biX4zHjygmnMVTWIhIjOGdRE504rrwEuBsFpdsPjJD0YuWj98_sJhHFyqLdSaY9SFBkLeKNi2r0Z3bLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=nmfLxZvdZ4f_BsqLxsXLtmqX0xqdBl440p5J-HD2pXub2iWC0LhgO5_MzHagNkuiX_8Aj90ZM_rI463k91qIph9uT_E9tNEgyZYZtmHZus4ThU4sdMNK6dV5fJYVceaaOvsvYNRbgaDCJN2QSaZP1hf8ds_F5lFrpQLTxH5Kz3zIUr60YP18kA31eeYyF7tim4ipnQu_svR5pkkkyp_njBcFgcsueBNIZzQxbyceiyd-fbQNjo_rpWV4W1bYNExVwFSzBtEVlHVkNSJK4nXNagi4vWDofhndikSvjlFLYkc04ZRUvr-04ABfZZ--tjZtJR_krg8aQj7S0-o_5QuU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=nmfLxZvdZ4f_BsqLxsXLtmqX0xqdBl440p5J-HD2pXub2iWC0LhgO5_MzHagNkuiX_8Aj90ZM_rI463k91qIph9uT_E9tNEgyZYZtmHZus4ThU4sdMNK6dV5fJYVceaaOvsvYNRbgaDCJN2QSaZP1hf8ds_F5lFrpQLTxH5Kz3zIUr60YP18kA31eeYyF7tim4ipnQu_svR5pkkkyp_njBcFgcsueBNIZzQxbyceiyd-fbQNjo_rpWV4W1bYNExVwFSzBtEVlHVkNSJK4nXNagi4vWDofhndikSvjlFLYkc04ZRUvr-04ABfZZ--tjZtJR_krg8aQj7S0-o_5QuU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/txgiXxxEvV-LPb7bmlFhnz4kG757nzBjfOngfVqxoMw4Aut9ARjnG7rib-aioG3uVe1sskDgCV-Yss9eB1z6_dvLRrNmbfzuEBL_-01kvYQc2CR0NFh_Sl7fxrN5kUNPzDAkJ0AZDzy5d55eFFMTf7XRagSHjGDMP2PPSxwqv0oyCU_qyNlIGT6Y9UOHJPYqvhkhjyRTXTDik8pnnN-SzbVzldWIbFjQrT880nHlP37RKzxumYCrZvHyj4sZVH065_ArIkkNhSlV6W39k4btxtpfbuVpp72V7vi91jY3L2ET3ea4I5YllepT_7qvQ_nP_vnbz2gt3XHK1YngntQUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VAFjvLn10hdLdMXBawMpgozMBLXEVQBLG9SHpRMTubejlawjqafFQRMOcATt2DodDEIbE3ukkGuyAsNDW1GLqQHrnvl7Z3z8su-Rs-lFc4kk8KCC4Tx6za-_6gGzvHBD0A1vC_i59DrS4pwZcdr6z6AlNm6zwma09cZ3qm-V9ovnwTRZCjzil8PL6EbAy3sHLI_4Praio2lgDHjX-kJqR_bxzHG3WfZ02IM8Xe9PJyaA6nbwaendDq_j7VsKji0gacvcUXhxEP9drUpVX89zoy9i2GWRS5jI_ksPKTqWiVzDCOZ5oCRHZDPndMr4CevC8JtYeHiqotCa5Z-_lwENXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=oo35xX_pjbd52LmaatCJV2V5Nk0WSDE9-0Y13y225-9mtY79g0hWVHFbs4FrOcEwbMGhPWLZIXW1pDUGj1dfVfyWn8yrzFpDIiQZedhRrkY9S9k9VBJQiILEsFZuq05JyxQIEaPeAFlpkO8RPopXKJy9Clls95dR7w3tt9iEDdJa_PodhOM0Q53QiC6NxxworcJoLa9GQb_Vb85OqTsF7o4zRXPyGCqr3rZcYe0bj5yPeo9vUMw8L2_MnC0VSz__vNXLMXU9VdHraKgw4irG4KsWx3hlBppt16xLn_qjo1vO1ZrJrujJ6r6IirZawIQlVt02Dzmq4b0K6B1Vv7c02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=oo35xX_pjbd52LmaatCJV2V5Nk0WSDE9-0Y13y225-9mtY79g0hWVHFbs4FrOcEwbMGhPWLZIXW1pDUGj1dfVfyWn8yrzFpDIiQZedhRrkY9S9k9VBJQiILEsFZuq05JyxQIEaPeAFlpkO8RPopXKJy9Clls95dR7w3tt9iEDdJa_PodhOM0Q53QiC6NxxworcJoLa9GQb_Vb85OqTsF7o4zRXPyGCqr3rZcYe0bj5yPeo9vUMw8L2_MnC0VSz__vNXLMXU9VdHraKgw4irG4KsWx3hlBppt16xLn_qjo1vO1ZrJrujJ6r6IirZawIQlVt02Dzmq4b0K6B1Vv7c02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=HynX9SBagFfPAq13e77l5y3Ka7HEMqUZM1FLuJWiuQ3U6NAUUUi8aukPFczYj2b15kUZ5IGc35Z6m7ZDe3Dm1J29PkijpoMM4Si--Dbr46SyGCBRdmtdNYdSQK7ugU9T6Wz3gfxEpwIhQaEkMPpffd9two6ySDEDg-zHg2XbdChiyJFdvoeanqTmKJzUn2WGwpUBmK6TDnJGTjKgq3Jt6ARp0XdZC75HohNrzlEaMnIz27ukpH0o0QFI68iGO4CQ0HDcluVBzsSvOrGwwY7QwkPFHr9KVoxONUa8mL0yNM4NpwweVM2LnCUzwRSbLWrFX0X-liLzLXmAw7CA3iU5gThhC82yq8yiG-cbcyKDyBqKPkt9cnLlZemiXshSw44AljklBVYie8VYKxfaCPpTb-HpTzfaKg4oIf3bn0Qm9wK1kO-zoKNbvFvE9K5mZWTkHB0wBqP_1vmW-C3hSgZ5EtmTjNLbfxUXQ0ltAohlMcRoUeBH1OCo0UXaCFOngwK73TUevAClOCr7ZrQVL0YNf5RJr5HmhJ-sUpdwqq2hGPyGtuLGhwjZ-rRs5YKRsR3X2d5qFZowpQqN9ZyyvUZpS65NTtjGG98DP_sjZURaD9DDAUDv0ApO8A8n8w4BLNKLiGcEGsRidV0TI27OYH06IUiA-wNkAOyb4HW6Pck892U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=HynX9SBagFfPAq13e77l5y3Ka7HEMqUZM1FLuJWiuQ3U6NAUUUi8aukPFczYj2b15kUZ5IGc35Z6m7ZDe3Dm1J29PkijpoMM4Si--Dbr46SyGCBRdmtdNYdSQK7ugU9T6Wz3gfxEpwIhQaEkMPpffd9two6ySDEDg-zHg2XbdChiyJFdvoeanqTmKJzUn2WGwpUBmK6TDnJGTjKgq3Jt6ARp0XdZC75HohNrzlEaMnIz27ukpH0o0QFI68iGO4CQ0HDcluVBzsSvOrGwwY7QwkPFHr9KVoxONUa8mL0yNM4NpwweVM2LnCUzwRSbLWrFX0X-liLzLXmAw7CA3iU5gThhC82yq8yiG-cbcyKDyBqKPkt9cnLlZemiXshSw44AljklBVYie8VYKxfaCPpTb-HpTzfaKg4oIf3bn0Qm9wK1kO-zoKNbvFvE9K5mZWTkHB0wBqP_1vmW-C3hSgZ5EtmTjNLbfxUXQ0ltAohlMcRoUeBH1OCo0UXaCFOngwK73TUevAClOCr7ZrQVL0YNf5RJr5HmhJ-sUpdwqq2hGPyGtuLGhwjZ-rRs5YKRsR3X2d5qFZowpQqN9ZyyvUZpS65NTtjGG98DP_sjZURaD9DDAUDv0ApO8A8n8w4BLNKLiGcEGsRidV0TI27OYH06IUiA-wNkAOyb4HW6Pck892U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhNuZfILE_V3Tg_NL06ergIJJ0I3e8LvafatPr0xHabsYHl_2f7wmuZCtedBNZRQUJguA4L3XBQ5i9ZSnkatGoSsUbMScNP2Qg9eTBZyXIe4E8voqX05YxxYnEj2Uo02YWfx5fyK8FCWlhK57ueC1WO_SP4VyAloiOGzZojoFDLr9nTOWowziSjwrwiDv-H4I9aTdDEt2eduJDE2skePttwgHScTlCj8K10vaU1gaql4ReRoi_-OyHi6HEOurgHQhixH8d4IVE4LmeT5dKG-kAEt69yvswCfOxtQkknh7jItpjg9cCTnTwQx9Ki3h_A_N8vhrjRTnLVM8tbeIHFpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=cvp9owBaZIVCm8FLdwQ29HO8UnAFeGSBKXfKpxdjOz-FHgeGKA6IrMNxTPLi_VWpB013A-McHlbFJ9WDgbWDuDtUZYzQo0fgQp2lJnl4ntixCVjGCQaq4VoPcwEUvFr9yE_mPJg1szACLL_tmBILfz2n-OzFsrBEwgjzma92E5buyzXDwIcOi-esYoMyUkoMDUDDEv-Obq8fUiT2FfIIjru4Q2Skq70Ky3zBAMDedB2MZO-lERL2OH_76577vswakSmLarjk4UBS_Nsgtl19rm4jeT9-5SWxvda8PPVNtDyRNIcf_Ao91k23yTrxm2-2Rayooj9hmF8UZhDh4d0XtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=cvp9owBaZIVCm8FLdwQ29HO8UnAFeGSBKXfKpxdjOz-FHgeGKA6IrMNxTPLi_VWpB013A-McHlbFJ9WDgbWDuDtUZYzQo0fgQp2lJnl4ntixCVjGCQaq4VoPcwEUvFr9yE_mPJg1szACLL_tmBILfz2n-OzFsrBEwgjzma92E5buyzXDwIcOi-esYoMyUkoMDUDDEv-Obq8fUiT2FfIIjru4Q2Skq70Ky3zBAMDedB2MZO-lERL2OH_76577vswakSmLarjk4UBS_Nsgtl19rm4jeT9-5SWxvda8PPVNtDyRNIcf_Ao91k23yTrxm2-2Rayooj9hmF8UZhDh4d0XtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDwVytgydiEfH6TLRwbtGMVeQhLx1fBX7vhsCXze1YIhpTBuznFJM0Nm7MLiGoXJkYIs8Fy-xGF4CLlbuxURrkgSi-YUOAwtuDRgHL8KrD3LGOM7ru54QEQ9uCrfjqiDuq6X_b5iLFmrWv7ztRrUnWcXLCrWy5aJC7cjVvy1b2JNaeha3nG4w1-VQEpWt4m-Q0Leo94SPskw7on1bo8mFf4hX4rjsG8ER_fb0pO0m2Ciz09avpOG7br6ImN473goaa0PIAZVXCquXUHWj1UWVjLkjKmRFlWhsGK9Chdi2rb7LtcJozUZZdx-9ppOSFI4EwSyZbOSbHJnelMKDqN-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=hzfHdZ2gTFXnkYC5imD3gozVa0msZzFep2h4hlvbZXADemOrSDXHVtG8akAKPbQmEK4E7xGf1qT_viATe0YP62ImyOLdv9p_IsJjZkxjK10IvMGXJZuJwfmHDOFHKibWMIOQ3VO5SjnRa6CykGlWPSjcOcXpZp_GGQmWiWix4EfXbu_Ke393W3xnHkIEkSSxwu4b0_rNss62dZAEdoz_oX6QXHLLTrAyl4scX59PJy9-YbTE7U4fB5nUD2cxLSKuY5212Q757emS6FVTSYgm6iZVcLDGV0AYZpgbDDkbYuDWuKmTa6rcMSmFDr_5zC5uv-RzNGcegUedgju6UUqiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=hzfHdZ2gTFXnkYC5imD3gozVa0msZzFep2h4hlvbZXADemOrSDXHVtG8akAKPbQmEK4E7xGf1qT_viATe0YP62ImyOLdv9p_IsJjZkxjK10IvMGXJZuJwfmHDOFHKibWMIOQ3VO5SjnRa6CykGlWPSjcOcXpZp_GGQmWiWix4EfXbu_Ke393W3xnHkIEkSSxwu4b0_rNss62dZAEdoz_oX6QXHLLTrAyl4scX59PJy9-YbTE7U4fB5nUD2cxLSKuY5212Q757emS6FVTSYgm6iZVcLDGV0AYZpgbDDkbYuDWuKmTa6rcMSmFDr_5zC5uv-RzNGcegUedgju6UUqiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=Eb3P__p4tAEfpDn8jpdf0YwZZDsw7x2MNDh5ApoxlEHLc_pF3lQ-ypzCI2pF2Co3i2ehZceT_ypCmKsjoaPmK2h9HWWZ0U_4TDcuS0sCpiue85DSpSsCEphT6LH14CANSjVWUmYRk8wky8tU0XWmLavMMmMvgt19_WsKIZfRYX2zlB_jGhVh7lOg5IP-yH22Afl_MyQiQsm5o46NGxEt29i5CFu9q3IfwjHMR5-So7JWw6VrojNjgNxPeUBAI-vOHwl23Pqv303ycOuRJt_lhpmUrVBRcylKy82R8AWZ0FfuJMfxPJH-JC1Q_xzlSjZKJ2FhIdB_DdOoD55Fh4ksDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=Eb3P__p4tAEfpDn8jpdf0YwZZDsw7x2MNDh5ApoxlEHLc_pF3lQ-ypzCI2pF2Co3i2ehZceT_ypCmKsjoaPmK2h9HWWZ0U_4TDcuS0sCpiue85DSpSsCEphT6LH14CANSjVWUmYRk8wky8tU0XWmLavMMmMvgt19_WsKIZfRYX2zlB_jGhVh7lOg5IP-yH22Afl_MyQiQsm5o46NGxEt29i5CFu9q3IfwjHMR5-So7JWw6VrojNjgNxPeUBAI-vOHwl23Pqv303ycOuRJt_lhpmUrVBRcylKy82R8AWZ0FfuJMfxPJH-JC1Q_xzlSjZKJ2FhIdB_DdOoD55Fh4ksDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=aZqHTEcNVtg8ErTjGlXvqdHC8oyI8ywfPDZTqN3WT4n2qVOEtPPTdNKm8zk7EZVf5OElijuew-CBKJmdQyhv-iXWCNVJfuOmGmfoSZWmsedwW1zJsCCuEWH-oG2nFiZxeN-4Cu5zhUopyHZQSDuHOqMIn_aKnUzJo9ld-0j6pN6CwwxW2-ig3vjDovaWwXoRo21RIFsdjcXel7OsFmbAAnPTkJ3L1mCRxJXsxD8eiDjHpS4yhMVKaC_N5TeW3FnwH_pTNgFHWtfG6ogg7KKU2KFvcpHqSgXOEoTLXJCl6MXxV17qnddwvg7k8-NFpOehC7XEpLzsTAu30cEUBh_5BA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=aZqHTEcNVtg8ErTjGlXvqdHC8oyI8ywfPDZTqN3WT4n2qVOEtPPTdNKm8zk7EZVf5OElijuew-CBKJmdQyhv-iXWCNVJfuOmGmfoSZWmsedwW1zJsCCuEWH-oG2nFiZxeN-4Cu5zhUopyHZQSDuHOqMIn_aKnUzJo9ld-0j6pN6CwwxW2-ig3vjDovaWwXoRo21RIFsdjcXel7OsFmbAAnPTkJ3L1mCRxJXsxD8eiDjHpS4yhMVKaC_N5TeW3FnwH_pTNgFHWtfG6ogg7KKU2KFvcpHqSgXOEoTLXJCl6MXxV17qnddwvg7k8-NFpOehC7XEpLzsTAu30cEUBh_5BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=OyBQwB6fufy3v-y1SsKn6Nyv1ZjxXoZroe0iJyvxy_iLokUT74rM1AqD4fRA6O1cPYfQqAB3DqDoZcoOl6SAplzRENafaxd-R7z2hU3qY3r9-IT-PVtmYSs9KpEtV0eHX6rNpHwADaIIKcEseRy4SoBzUzc8rwx8nUTUhw3Sn5pyTAxETUE-I70xa0T_-lyfKmpa-FhJcKk-kfUgcIy1bHrVHV-JCPPT3DfFpk2grnVKTNAMPpQ2kKJ9TvJJ7wo9dR4jkK1o-MkuVoiUdzvBASKuBO4dC7oBpqf-yPVYd44dfbFby6QlnLsyqR_V2UufdI_phUJZ6fof99dSuVjgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=OyBQwB6fufy3v-y1SsKn6Nyv1ZjxXoZroe0iJyvxy_iLokUT74rM1AqD4fRA6O1cPYfQqAB3DqDoZcoOl6SAplzRENafaxd-R7z2hU3qY3r9-IT-PVtmYSs9KpEtV0eHX6rNpHwADaIIKcEseRy4SoBzUzc8rwx8nUTUhw3Sn5pyTAxETUE-I70xa0T_-lyfKmpa-FhJcKk-kfUgcIy1bHrVHV-JCPPT3DfFpk2grnVKTNAMPpQ2kKJ9TvJJ7wo9dR4jkK1o-MkuVoiUdzvBASKuBO4dC7oBpqf-yPVYd44dfbFby6QlnLsyqR_V2UufdI_phUJZ6fof99dSuVjgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twrCyxVTRrEUYUJKyzD0D5fdcAFP_H6GIxkAyFM6EbS4HXFVzEapL346y6W8Q-9Jwh2MZ-0NvNiJl4tl5HpiPq1kbWu5xNSh-aAmoTp9QdpCJKb5nU0A7JLN2rpEQ1VkFIO7B5lOy65CEXsSAVU53PzGk2UzdgkXNJdwZ0QnTnvSuvJRJoX1o2Uze2uR8EwNhPG8SUQ-Glok5LyFLFyO82qyi6vRJcO_W4SiP7DfwzIYk5zwMZaMaVT_hV7chFQowxIiqQnsYvv0ga_go2XweI4Ls5P1t-IB9mYX2ftISpsut9PsqfhNSADo-ZLfwyziSddKckoaWkbDR1QCjHQAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ZW5smRLp5NvvTYDE-jhfdObtzTFHpulDZV7hRUoEl4rXXly_cZhv3JIvhhA4szrNamph9fcSHQ9E0CsQnuHhNEiZMTkS8SM_AtJCZBaafIRc4HNp6GvXPoEjPauvM6uI___bhNtkooB5NegUpwS9OGzee9dpPWaop7wjG-CgZ9rXZngT4TIVFASLyiBhNAY7aGNa9qPKNfsgX92LyihvLrhidHW6n1H-aEi7Ghd1hCcgDA4EkxuSy2XviqhfTT_YA_1rlWB1D9kvN0EUYdar3KcP9eGAUk8dTXvENHphjtT9BTWwOow_bFg0uClS5RXXKp32oPAzy-fzXy8zbTfAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ZW5smRLp5NvvTYDE-jhfdObtzTFHpulDZV7hRUoEl4rXXly_cZhv3JIvhhA4szrNamph9fcSHQ9E0CsQnuHhNEiZMTkS8SM_AtJCZBaafIRc4HNp6GvXPoEjPauvM6uI___bhNtkooB5NegUpwS9OGzee9dpPWaop7wjG-CgZ9rXZngT4TIVFASLyiBhNAY7aGNa9qPKNfsgX92LyihvLrhidHW6n1H-aEi7Ghd1hCcgDA4EkxuSy2XviqhfTT_YA_1rlWB1D9kvN0EUYdar3KcP9eGAUk8dTXvENHphjtT9BTWwOow_bFg0uClS5RXXKp32oPAzy-fzXy8zbTfAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwhoeIzpGWWc2yoU4-xAlFyiT3ZuCjts6JG-G911WPujmuq4Udu5q9HLKXqRCkEjnC5zP9b6lTZKARQ17B1mF7i2DP22LgLpA1nCpSo2W4WKl59LT9j1aZ2sbiHhbZOOpnNn4ymmSpPzbFUgqgeOaeuDm3RsLKTMpXE6TJMKcxwGIcDVa49YEnLs-Xkt3l1-YmIviCwE52zaGG4VLD8pvOQNj2Znk9qm5g_hJhfrMLwcsSQt11jvnIsN6Bp_aD9c43eW9H0M524Sneu4iGcHcYsCdmX0oFSusb_GUOP1k1gcaz1LizjugPwwrVJpLVxi-UYVgN14kdu1voh_VFfOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXRuCZvbcbL7SrlnzsxlfS1vpKxuaR1ZDv37AF1RZxuULeHloBT8taiUa43QRYdFVNV63gyt5iEwEnk6f3QLv8b7rIayzcLMqWdecJRqr9z4XHZasNHzX1986zEQ66-LaeRwtCRutTA0tNDo7fagVIZZVjwzkfDnfYMAnww_IUJqrWjemZYvy_iNei9ck3wLp-y6tXvBfAOJ0ekh_7IH4mWmmltVbbW2PJHNWDOFvj-ytI5mfIrfrcjIpn6bdQuKNgqhxU_BDa7fh5yL8HTLXX7sytlm2p3RagOOt5_kuDhiF5rkNTpsCnFWIXevD24L4Ni-mlh2pqQSHp-FquvwOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=FxSFtUs-WVrRA_KgJ9P8pn7OmC-zeKwby0QFst4cOiJWgTraqlb_uSBuTrFiuUHW9abYX_5m9G4cWlPm2vS1z8c4vUPuCu4lmyxNRfGaTBv31eTnt32AORaYdTRMP_XQAOxDjiklKA_PHNmssG9BMaxk0dSFd5vn7A7RncpTOH6997zFcMvRRXMYLE03aaQ6Glr6L9laS_iggit9RFBbv6fq011uQuFfCU95D4cfqjoKfwbc_STfh-WdO0dbdNeDMue2X87B73esjZdxpAPl7oZqivlleUJgGbWxs5jCgax3Hk6zdlTnRcXsC10x2D1XMvXxI1kC_ElwhYBvbEbknA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=FxSFtUs-WVrRA_KgJ9P8pn7OmC-zeKwby0QFst4cOiJWgTraqlb_uSBuTrFiuUHW9abYX_5m9G4cWlPm2vS1z8c4vUPuCu4lmyxNRfGaTBv31eTnt32AORaYdTRMP_XQAOxDjiklKA_PHNmssG9BMaxk0dSFd5vn7A7RncpTOH6997zFcMvRRXMYLE03aaQ6Glr6L9laS_iggit9RFBbv6fq011uQuFfCU95D4cfqjoKfwbc_STfh-WdO0dbdNeDMue2X87B73esjZdxpAPl7oZqivlleUJgGbWxs5jCgax3Hk6zdlTnRcXsC10x2D1XMvXxI1kC_ElwhYBvbEbknA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=i5lMMVoCmxbvcFcAt9Tsm5J5gWlkFBr40VgfWPL70V56xMkkMGETikyIc7EKx54gEjEimv_DB5RENCqDM6UsD9SwwGhurVsjZ0VZT1wGngrrbEItTn7nAYX63Oyhyov3oUJnt-FuIl66N-gsGnM0ZqqvIgfA5oTaHC_j5swwNP9ENMYsexipOjRofr55scnMdVGNdiXDJ1jI33tQPgZrnIH8gLpZ2vAAvtUYCTJnzvFzrFdY0na8KHw1132HU-_FFJ-51dzTwvkPgUADn6qvKMo-0SwxSwdEp0Tbsbm3bt03EHNCsLTRso0iqydK2CFhXt9NORzuoGy0WGV392gKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=i5lMMVoCmxbvcFcAt9Tsm5J5gWlkFBr40VgfWPL70V56xMkkMGETikyIc7EKx54gEjEimv_DB5RENCqDM6UsD9SwwGhurVsjZ0VZT1wGngrrbEItTn7nAYX63Oyhyov3oUJnt-FuIl66N-gsGnM0ZqqvIgfA5oTaHC_j5swwNP9ENMYsexipOjRofr55scnMdVGNdiXDJ1jI33tQPgZrnIH8gLpZ2vAAvtUYCTJnzvFzrFdY0na8KHw1132HU-_FFJ-51dzTwvkPgUADn6qvKMo-0SwxSwdEp0Tbsbm3bt03EHNCsLTRso0iqydK2CFhXt9NORzuoGy0WGV392gKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=PA8kNI4tyXI6WVZFNTMfSE8toyb2GZYtKvD0-Sj-LVeRXJpXp6DHJ7CcTzdsBKb7NvLavqvJCs-u5CTv581mJXBbTx4K1hY7gwkpqxsf0k3X76GZXWTb166xUh9QV99PCd3mSqUFdbmsn6tKrD55DC50f8BA9T6pd1ui5H_gOiRWKimo7yoGEwPwq6aHT9KJBDWjfpRDMbNl28iIaNFLb6z-hMop_xDHnBABJxET-Pa9INd0q4oDrvHeGayLd-gtNWOMgIKUPoL_lTDep1OeK7NTlIiVfRzmjgIlKf-nDcSL2FYm-Qf3PZV6q8QcWM7udqjI5E8JQSUtNhzzGXiFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=PA8kNI4tyXI6WVZFNTMfSE8toyb2GZYtKvD0-Sj-LVeRXJpXp6DHJ7CcTzdsBKb7NvLavqvJCs-u5CTv581mJXBbTx4K1hY7gwkpqxsf0k3X76GZXWTb166xUh9QV99PCd3mSqUFdbmsn6tKrD55DC50f8BA9T6pd1ui5H_gOiRWKimo7yoGEwPwq6aHT9KJBDWjfpRDMbNl28iIaNFLb6z-hMop_xDHnBABJxET-Pa9INd0q4oDrvHeGayLd-gtNWOMgIKUPoL_lTDep1OeK7NTlIiVfRzmjgIlKf-nDcSL2FYm-Qf3PZV6q8QcWM7udqjI5E8JQSUtNhzzGXiFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=aStjPEtxzdUsfZ0CB43XyM_ZCQGTr4jCGq4OR1BMLdUBWfMXaEfX777NGnWXDV6N4eULdudy8LB3d6OtfbzAPDIBvpbfBtHfP15LKkCL7FncU-N9VdDOvDHsMCTY7gymeD_Tg0y57LZx90yrzbeocA2PWv8xj9XgF97-B8bDYPDQrMg0eyndHOnDvs2cBVkJLRt87Qtf5lg7fFmyemKtsxAM6l4kq3BEEQdG1po0M-2LoJTw4EgpWg6d_77T1WW9FRgyILbbNttczhNFdfXwmi8jCY9RdjtNKAhF0uY7RXHQH7ltSAlZpG7pspgv6BtiAB3RmhmJU4hlheBB_tPQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=aStjPEtxzdUsfZ0CB43XyM_ZCQGTr4jCGq4OR1BMLdUBWfMXaEfX777NGnWXDV6N4eULdudy8LB3d6OtfbzAPDIBvpbfBtHfP15LKkCL7FncU-N9VdDOvDHsMCTY7gymeD_Tg0y57LZx90yrzbeocA2PWv8xj9XgF97-B8bDYPDQrMg0eyndHOnDvs2cBVkJLRt87Qtf5lg7fFmyemKtsxAM6l4kq3BEEQdG1po0M-2LoJTw4EgpWg6d_77T1WW9FRgyILbbNttczhNFdfXwmi8jCY9RdjtNKAhF0uY7RXHQH7ltSAlZpG7pspgv6BtiAB3RmhmJU4hlheBB_tPQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDis0I3jBxvg2HPbINEwEper3MpCCmtPFVH7Rl60HozHI77lbVD9fFNA8PyZSgNAI-9uVrVCSmct9sdPtZRPkhUVY_Vz1OQQLVEb_qGEofJXnRLlIyz_5pOfiXqYQ9lftYFSRgjjroZNEVZmhY97r4Rhp0Dew9XGpK3HmutrgIRwCu5uo8wXK3UrowvV_OemQFyMKHLnCO2exbT9_9at-qPF1GcpQGhVvQ_Ye8mbb-JK-NX0nSuPxxe1P7EqIvcvbCSM7Llf-JEMX0V57o4vSTSzpGZ0qEs2mrGouGwEpruhzc3JhT_0sckAZiPKbnKBF5eic-py9_kseWrmXC_0Yboo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDis0I3jBxvg2HPbINEwEper3MpCCmtPFVH7Rl60HozHI77lbVD9fFNA8PyZSgNAI-9uVrVCSmct9sdPtZRPkhUVY_Vz1OQQLVEb_qGEofJXnRLlIyz_5pOfiXqYQ9lftYFSRgjjroZNEVZmhY97r4Rhp0Dew9XGpK3HmutrgIRwCu5uo8wXK3UrowvV_OemQFyMKHLnCO2exbT9_9at-qPF1GcpQGhVvQ_Ye8mbb-JK-NX0nSuPxxe1P7EqIvcvbCSM7Llf-JEMX0V57o4vSTSzpGZ0qEs2mrGouGwEpruhzc3JhT_0sckAZiPKbnKBF5eic-py9_kseWrmXC_0Yboo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=Bth2UZCJv4kU0oEeJ6HEOtFZ6FO8Z4UQdv7uegRyb_COn0OdNekRBGkefEDY91ExJwitU87igk2CjDXu3TLLe5hVFRDByt6xz_k-n8-p_PaGiA6V7dO42PDuwTL7vsXbUjefgTdM4dC0YYvOrKzriGMEiXSFHc4Oqrkw9AlKFsvt3XSNHJ2NycMbOnaR0SRivVB1HSlAx2CGO9lT-TIX14idgXfGfTaxHLX-96drnDQCwuz5VRlBqy3tgTmMgSAfn9_RJTbtSKCaD7liC-KAwj0IkmR-7ffE0qb1sUk8SFjRHETLiRUWNcYu2xdEWXQuoz_1MdPBvCDNdFm2CW4UUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=Bth2UZCJv4kU0oEeJ6HEOtFZ6FO8Z4UQdv7uegRyb_COn0OdNekRBGkefEDY91ExJwitU87igk2CjDXu3TLLe5hVFRDByt6xz_k-n8-p_PaGiA6V7dO42PDuwTL7vsXbUjefgTdM4dC0YYvOrKzriGMEiXSFHc4Oqrkw9AlKFsvt3XSNHJ2NycMbOnaR0SRivVB1HSlAx2CGO9lT-TIX14idgXfGfTaxHLX-96drnDQCwuz5VRlBqy3tgTmMgSAfn9_RJTbtSKCaD7liC-KAwj0IkmR-7ffE0qb1sUk8SFjRHETLiRUWNcYu2xdEWXQuoz_1MdPBvCDNdFm2CW4UUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=X2dsZ5k0r90MaEBLtZXsFf6DLcHEJrZMdzOcp9YJqV0OUPf9HX7U_ysiGz8f9f2Cd7sXgkeGS64XUJq0bG4wS0_xBy00T--adVM42CPwX2f82Be6iB-hM0-RaS-gxl6rxa8SBQ_gIZc_5k6ychpfYNEBcaZqE5WB6iANgfd0l47xW7rlL-6bAi8BzFwSecBFE-SzFdIW9_RYp8GJWpyq0HBQhV7XwL6TlyF2U5igrMkIpMAHsZIho7Mii9DmF8NgIvI4cqcn2SRt3Ta8Gc0btBDe6Cnq1rdq-dYtp0vxGn99pf1vlpSb914O_pcOFPTbJJ1P3mlU-5jCGDZiGZ6vzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=X2dsZ5k0r90MaEBLtZXsFf6DLcHEJrZMdzOcp9YJqV0OUPf9HX7U_ysiGz8f9f2Cd7sXgkeGS64XUJq0bG4wS0_xBy00T--adVM42CPwX2f82Be6iB-hM0-RaS-gxl6rxa8SBQ_gIZc_5k6ychpfYNEBcaZqE5WB6iANgfd0l47xW7rlL-6bAi8BzFwSecBFE-SzFdIW9_RYp8GJWpyq0HBQhV7XwL6TlyF2U5igrMkIpMAHsZIho7Mii9DmF8NgIvI4cqcn2SRt3Ta8Gc0btBDe6Cnq1rdq-dYtp0vxGn99pf1vlpSb914O_pcOFPTbJJ1P3mlU-5jCGDZiGZ6vzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0JqVtNIdbi1WRurJ4R-0WVFNjvkJF4qXcYv7h0-bSdAhXG1aYyeeZklHHVG9dvr-ZRy9fv50NCot1Gp-eReBILF9Zt0-BEOW49GRF3LUd7VqtZoJlTvlfkutHRighd6LGYfx3TIszxlhhMVH0hK44gVzXv_Pf44UXKxhP0VCpu23WhXPub2GxyJI6Z6WmEf1wQdj574NWHWbA1hhGjVKWYpnb7zqe7b4FntNehzpGtNwCLNYYQKf7v2xjlki0ZEH73tX9rWJ2fWtYNB3rmRvO3NtxoNb0-J9gVdi3gjQKwo81mXZMDb1LgrVoBzfhiTqfIiFKekOwPh1WQgGxsmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=PGvjU5iRqUlQrjeBG8sVpCz9J2vI2Mcu-sWGclcOHZfFf_-VxYaPoXbFDVdtmHb5VTPkZaR3DjXcF0jr2bnau1DmKl4yfPHXi4dhAEvOeHosTle_oj1KpFcGHfiGS9ZzpMr-iVzKkK2EmJmGHvdoJvPb2DYrmrIhpHfgh3bZNjG0r78fNF3VdwdKOefVadB4wlu29-wdEGHcdH2kknrIMoWZLAf5BrMyhwVbZUnUWdxQBD0r5xzUeJQg9cty8yMw2h-FIvCAxaxoiY0e9n27kQ9le3i6r3pxI9mAv9WHU38SXOju438JLW6WMNRbY7TgViQ826T2Twi3POLat6MSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=PGvjU5iRqUlQrjeBG8sVpCz9J2vI2Mcu-sWGclcOHZfFf_-VxYaPoXbFDVdtmHb5VTPkZaR3DjXcF0jr2bnau1DmKl4yfPHXi4dhAEvOeHosTle_oj1KpFcGHfiGS9ZzpMr-iVzKkK2EmJmGHvdoJvPb2DYrmrIhpHfgh3bZNjG0r78fNF3VdwdKOefVadB4wlu29-wdEGHcdH2kknrIMoWZLAf5BrMyhwVbZUnUWdxQBD0r5xzUeJQg9cty8yMw2h-FIvCAxaxoiY0e9n27kQ9le3i6r3pxI9mAv9WHU38SXOju438JLW6WMNRbY7TgViQ826T2Twi3POLat6MSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=f0luV1B2XtRdU3O1rBv_Rk0iaaui9ZLphCVpIafjP_1vMXWCXc4UldFKwzOcM6NmWOWHEdMWKznb3IlgZj3K2_s5MjxXZ56BKcZv7pser_oAxueMMZ-WseFH775hbyAKSzuEJCEj-48_CaQ7CiS5aXX4bf8q95xJFFkVGs6SqT5ZH2sGrLsg3S6IWi5Ou25j1Vr1WzBiD65yk2-8R0WbDeGS8ndtaljonT1li001cvpO0C8D0Z48STLHfDPqTrjQS8bvTt-Y1PwfIdFEwFBFi4w2IarfiwM6uFSfVebmexjBYuaioeHsvBu5b2RK0F1-A0DlPtWuybdmKclHzfZDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=f0luV1B2XtRdU3O1rBv_Rk0iaaui9ZLphCVpIafjP_1vMXWCXc4UldFKwzOcM6NmWOWHEdMWKznb3IlgZj3K2_s5MjxXZ56BKcZv7pser_oAxueMMZ-WseFH775hbyAKSzuEJCEj-48_CaQ7CiS5aXX4bf8q95xJFFkVGs6SqT5ZH2sGrLsg3S6IWi5Ou25j1Vr1WzBiD65yk2-8R0WbDeGS8ndtaljonT1li001cvpO0C8D0Z48STLHfDPqTrjQS8bvTt-Y1PwfIdFEwFBFi4w2IarfiwM6uFSfVebmexjBYuaioeHsvBu5b2RK0F1-A0DlPtWuybdmKclHzfZDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=epbh4J0Y1b_gApXOp8fKyj1T5DAP6ZazOn-0ZwcNG_4I6piMzfETILvvRykN-S8jYoRYtt0MzCWydB2DcMQTWfPmEBXsB5vN2fHmUdjinJkbvH039ijYnrU_984PBPgSBdLonWvvAahe4lbMhfKJlMvrY_6fpDY0FpNiJMW1eHVOVe0Z92j6wcCdEzO2FyanZzEBfEWHwDT2iyeQhKAeCb_Tx1XhBbEn9V5WYYFZziXT77xkcwR2mzx03Vj4NUhcxgsYQK-R27kDSlYmBYOYw0a0z3fst6iq5KkjN8SGbz6cKc8wN7qrwKlm7VhUESR0yddYhWwcliPRAWGcCM4xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=epbh4J0Y1b_gApXOp8fKyj1T5DAP6ZazOn-0ZwcNG_4I6piMzfETILvvRykN-S8jYoRYtt0MzCWydB2DcMQTWfPmEBXsB5vN2fHmUdjinJkbvH039ijYnrU_984PBPgSBdLonWvvAahe4lbMhfKJlMvrY_6fpDY0FpNiJMW1eHVOVe0Z92j6wcCdEzO2FyanZzEBfEWHwDT2iyeQhKAeCb_Tx1XhBbEn9V5WYYFZziXT77xkcwR2mzx03Vj4NUhcxgsYQK-R27kDSlYmBYOYw0a0z3fst6iq5KkjN8SGbz6cKc8wN7qrwKlm7VhUESR0yddYhWwcliPRAWGcCM4xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOEN7RrqLlMguiuSB1OexryJTre-iYIxCBiboYSOgCiNQLUP0ArZPGReEjPolCcd_t0LDsnJF2jb7e3Jro1jqDXstKmxNvxZuYlDV_AjP_If_UI2I_XlgK3O0dfmpfoyWWUqZkYg90gMRG8rwKr41tKbWk66_fqvstxjM0kVVYPT6VvXU5FWzgh_h3JRa5hoOSBluzCdPut3Sh233LEOeanxwogoN3xAKiYde65kpQI_shfzSvnxvnXmWl5s44x4OuOqEASjdu9TzUeUJP8sBRmPBza_MHpZ7mKmnWGTwLADeexeXyU_7nQm4ZXzzEBxGx7Q-Jkn0Z2ndIIwCmmrebHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOEN7RrqLlMguiuSB1OexryJTre-iYIxCBiboYSOgCiNQLUP0ArZPGReEjPolCcd_t0LDsnJF2jb7e3Jro1jqDXstKmxNvxZuYlDV_AjP_If_UI2I_XlgK3O0dfmpfoyWWUqZkYg90gMRG8rwKr41tKbWk66_fqvstxjM0kVVYPT6VvXU5FWzgh_h3JRa5hoOSBluzCdPut3Sh233LEOeanxwogoN3xAKiYde65kpQI_shfzSvnxvnXmWl5s44x4OuOqEASjdu9TzUeUJP8sBRmPBza_MHpZ7mKmnWGTwLADeexeXyU_7nQm4ZXzzEBxGx7Q-Jkn0Z2ndIIwCmmrebHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=h0NvE0i-AwCV_rvcw1hI31AiN-xxM-19izz1ykzE4nC4ekJ0T6nGq2pB5RjMGyOXKlQ9xSvX8sAs0baM4WUbclMha9G23Lh0Ac5rCQn0knHCn9fNk8t9hJ1xeOTlNpycNtxvoocYsQWZV1lM40Ibo4krvGowVddzZ0Rnqh1jYCxz_F7qDByxaZQCOXE9AG6E8T-ZnWR7DbTyM8kKU_0dZpoPUxCXphurPTzYERGtk3yYv7M0LXrqI1sqrUT4ezmPLlBnmDx2e6_lcRbNjzcOQb0zwKOmagWv9t5xHfS9jd3TEf-myTZHrcnET9zOQ54zg0tPGpJa7afCmugM7zrxbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=h0NvE0i-AwCV_rvcw1hI31AiN-xxM-19izz1ykzE4nC4ekJ0T6nGq2pB5RjMGyOXKlQ9xSvX8sAs0baM4WUbclMha9G23Lh0Ac5rCQn0knHCn9fNk8t9hJ1xeOTlNpycNtxvoocYsQWZV1lM40Ibo4krvGowVddzZ0Rnqh1jYCxz_F7qDByxaZQCOXE9AG6E8T-ZnWR7DbTyM8kKU_0dZpoPUxCXphurPTzYERGtk3yYv7M0LXrqI1sqrUT4ezmPLlBnmDx2e6_lcRbNjzcOQb0zwKOmagWv9t5xHfS9jd3TEf-myTZHrcnET9zOQ54zg0tPGpJa7afCmugM7zrxbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw-9BJtlcz420D7jucBmspfbW57iH9NXoIk9R9728BpPuEkEVz8zFzK7d9Zv1wXA7ln0AI6w1xxZSFIwChu-k5rNRlHDaIL_IRJPax4ZgvxJFry-MK8YCQscx6fz9ZlHv53pini9IosExmQRPyeuLAMN3TVi8mxDj5j8-MgrhNMFuISoU4H8IzvwbogEvmTaVh5E4_5gEWEAmNXHHO6vqk1nSz6iMWwnwBlKxPYVcwbMxo8PZjRtkk0oSUJ0U6njqeUzKUKMxxb4nIDrrADHwl9ZvbuFOek9-YnLsJYyFh_E6G0g2QMwnRL2zWkodX2cA_0JRueFCfxN735KZkdIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=qKtjqf7_XcEoENW_TrY4SlCLGmVDB-vEwVY7MIs2iL3mujQF0F1NB9Fcir1KmozFzw9P5Hgvsj7BdbZs9JwNLnWNSO4ZCDHwfaQiWYLjVcssZRARs52W78CnIQhesVulWktUjY16EFahBHtZB5SPJvcaJoCxX0H20afqWb72PVcbmWe2emamHd5vvL7S-rPZxJBQ36TmQW_PMbJfcfaPlrpBwtWeYjTttVtOXvFumfS7wfixWf4XeqECH4mPleUttLttYkHGNoqtvy0tjbPc4OaA158toYMMEiyYwXTpmQYcqt_VHEoZ83BfEL4KHOt6VPgMeiHxgKREuT5RvQMS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=qKtjqf7_XcEoENW_TrY4SlCLGmVDB-vEwVY7MIs2iL3mujQF0F1NB9Fcir1KmozFzw9P5Hgvsj7BdbZs9JwNLnWNSO4ZCDHwfaQiWYLjVcssZRARs52W78CnIQhesVulWktUjY16EFahBHtZB5SPJvcaJoCxX0H20afqWb72PVcbmWe2emamHd5vvL7S-rPZxJBQ36TmQW_PMbJfcfaPlrpBwtWeYjTttVtOXvFumfS7wfixWf4XeqECH4mPleUttLttYkHGNoqtvy0tjbPc4OaA158toYMMEiyYwXTpmQYcqt_VHEoZ83BfEL4KHOt6VPgMeiHxgKREuT5RvQMS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=SWxA7NwZhK7KuFRjJtetZA9je14jsJgqwPdfK6w4nM3VeWAOHrG0gyg7Jjzhd8RanaVbBop7S5KfMMrt0KTatVsnlE0xrr_FvUa_l0fDrSail5wTLVAYZx77MVxs_Ku-oPCFKYHze35bmkiX0fypawjQjwgXWVOIVc1SAyjxwwe_bEiIilIJnef8YQw-4RdeDUUE8So8ktIm4XyDM8fPrjDKMl-lHnFvcpHLc7trNZIJmc-6Jo8_9sGbweiAFK4JAqcibiZ1CSa_qXbGZb0X_zGsz1iLPaFvhDzsJDk2r8R2k0-9wQ__bCq6iT15dnCnltiYr4GqAmDuIpccgSZOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=SWxA7NwZhK7KuFRjJtetZA9je14jsJgqwPdfK6w4nM3VeWAOHrG0gyg7Jjzhd8RanaVbBop7S5KfMMrt0KTatVsnlE0xrr_FvUa_l0fDrSail5wTLVAYZx77MVxs_Ku-oPCFKYHze35bmkiX0fypawjQjwgXWVOIVc1SAyjxwwe_bEiIilIJnef8YQw-4RdeDUUE8So8ktIm4XyDM8fPrjDKMl-lHnFvcpHLc7trNZIJmc-6Jo8_9sGbweiAFK4JAqcibiZ1CSa_qXbGZb0X_zGsz1iLPaFvhDzsJDk2r8R2k0-9wQ__bCq6iT15dnCnltiYr4GqAmDuIpccgSZOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=fLdEpbV__U-u0C7G47Wvg3_SNGVpNqCvx8IVuvaZDGEDlPDJdoWjT0Vf5hTo2wgC5puHGMJymqxksSXiL691XXAysUseIju0kuYNhG0GaVi0QDLxAcrXIArbLfufOOoYjlwjv3063g6X6NXSHUXfAXandnxhO2mIbErT3LVV7JeSq4VZNXWt7AQuA-w0NUjEG3qNGAzeTulJwKo9Nu5NTvHZOhOZGM5rsWNi6D7Fur_HiXOCE8L_aJFgMzBlOy9TIiXZs-hxpb_dxbsiiGLwk_QdDfcUCXf_gBvBVmTjM5n51uQrSrHj-L_s8LplLxNOc9YKxwisiXltT5riVrJDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=fLdEpbV__U-u0C7G47Wvg3_SNGVpNqCvx8IVuvaZDGEDlPDJdoWjT0Vf5hTo2wgC5puHGMJymqxksSXiL691XXAysUseIju0kuYNhG0GaVi0QDLxAcrXIArbLfufOOoYjlwjv3063g6X6NXSHUXfAXandnxhO2mIbErT3LVV7JeSq4VZNXWt7AQuA-w0NUjEG3qNGAzeTulJwKo9Nu5NTvHZOhOZGM5rsWNi6D7Fur_HiXOCE8L_aJFgMzBlOy9TIiXZs-hxpb_dxbsiiGLwk_QdDfcUCXf_gBvBVmTjM5n51uQrSrHj-L_s8LplLxNOc9YKxwisiXltT5riVrJDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLzz10lQp2wDwYaFsIYuTdduC0p-AWb-80tC3iVsahU09btZkIJv3GCVvhvxfLyyjaE9uVxho9OR7BoGmNcl4qzRzRNBqIRcox3qnhcVpUIEWetFezp2hj4pw4Bt2lvi0ErpNM50jPXChkec33u1b05RlCGZMciohC3p3N2J0EywEnAZ9uMKX3GXhKw5qxuVem6wFfqO_JroUXm0fVpn1Wn59oSUDcib3cVXHgYX3L9yKPZGD8yRViJN0cBkbQyImjyDEtEMmXeeVppg1pv8P3TsKnqLCm4_H65yDsX9YQhJTyPgiueae1WWGXOmjmSZCw6aiegNoRN_8pJo5fe4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=G5dQ8t2YAlY8-EPl9ahCuqF9wZSVpd1IDPiH3A_--6ElHsFpPUP-DlHv4IDQ47iVzA3UgUmiORmtJ6JLv_8WlGvW1i9XBsNiX5_jKwRbPKucVu270UtfOrejQupEqNqXLPlASWKm6rdvhq2r7knsPM4A3Cjy61ZDXy42Uqzxm1rid61kqUNb8Ai0Oc4R7VHWp-7TeqspoqKpARtvKUDmzk46nvGQy8PbqwWVZ89Lc1An9KtzNyB5mwP8gdtFXi4tXSMzB-SWx0nZQpIBUU3RGZXQU643N4l6303oTBZwd5hWUhFfYuoUdW71OUkpEkIJW_L0ZpcGDGzsSjXm39aPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=G5dQ8t2YAlY8-EPl9ahCuqF9wZSVpd1IDPiH3A_--6ElHsFpPUP-DlHv4IDQ47iVzA3UgUmiORmtJ6JLv_8WlGvW1i9XBsNiX5_jKwRbPKucVu270UtfOrejQupEqNqXLPlASWKm6rdvhq2r7knsPM4A3Cjy61ZDXy42Uqzxm1rid61kqUNb8Ai0Oc4R7VHWp-7TeqspoqKpARtvKUDmzk46nvGQy8PbqwWVZ89Lc1An9KtzNyB5mwP8gdtFXi4tXSMzB-SWx0nZQpIBUU3RGZXQU643N4l6303oTBZwd5hWUhFfYuoUdW71OUkpEkIJW_L0ZpcGDGzsSjXm39aPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=TCW6rLsc1u6QBIYT5Ff56HMsX90cqR7eA2ImMwUWyrh8rBbIovg_RqciXz-12d_CrswRS8CWdZvpp14bgc7XMmZCEatDAocQw4YR03HaeWEVVyyGWAl4bxJetL2R4OseLicAI5SRcK7F0mQZFlSa7i5ocZKmWEAqUz9mkVB8P3rbLu27ZBF2X8yeZ67FPrO2GaQcsxrSE661T40a2y0qSGyyKVPcaQTMJFFgowpK-cnGKTmH_cYC71tKsuFjhW13YNcVA_Mo2HcShphBE0K3kRE3HSiu5M0w2LS16W0nFTJpMXQfSyZ5xsStBFFAenC1Cxmu5yGVESnfH6MKRMv2PyIPtRBYEAIxI6BU6Te5LnxbtnQEa99GSCb6a2D5IJLMylckYHqPKUrE9-QzYSoslIZm_yRClFPvpkDEU9CwaZGoeBo3SXh0jLC7bWBkVBQG6R1OeX3A7zkMZ7qj_sHwnL826KTo2P5-Jx04QsY8lt27hHnH9z9SCu-ICGDqViypXpZ7QasE41rM8rYAIYmvE2wTdAqGjh8M7A01LlE4NICXXVIdlouXCd8UvgO9HTbIHZklbOm8-Yx65E14nDlldpVtVqt-N28NPXKgVKe_mmfx19GkYyErDjS0YHbfcO790hSdAzIO5pBq2eWUtAaXatfYLn1EzJuc5Ys_ebgfR_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=TCW6rLsc1u6QBIYT5Ff56HMsX90cqR7eA2ImMwUWyrh8rBbIovg_RqciXz-12d_CrswRS8CWdZvpp14bgc7XMmZCEatDAocQw4YR03HaeWEVVyyGWAl4bxJetL2R4OseLicAI5SRcK7F0mQZFlSa7i5ocZKmWEAqUz9mkVB8P3rbLu27ZBF2X8yeZ67FPrO2GaQcsxrSE661T40a2y0qSGyyKVPcaQTMJFFgowpK-cnGKTmH_cYC71tKsuFjhW13YNcVA_Mo2HcShphBE0K3kRE3HSiu5M0w2LS16W0nFTJpMXQfSyZ5xsStBFFAenC1Cxmu5yGVESnfH6MKRMv2PyIPtRBYEAIxI6BU6Te5LnxbtnQEa99GSCb6a2D5IJLMylckYHqPKUrE9-QzYSoslIZm_yRClFPvpkDEU9CwaZGoeBo3SXh0jLC7bWBkVBQG6R1OeX3A7zkMZ7qj_sHwnL826KTo2P5-Jx04QsY8lt27hHnH9z9SCu-ICGDqViypXpZ7QasE41rM8rYAIYmvE2wTdAqGjh8M7A01LlE4NICXXVIdlouXCd8UvgO9HTbIHZklbOm8-Yx65E14nDlldpVtVqt-N28NPXKgVKe_mmfx19GkYyErDjS0YHbfcO790hSdAzIO5pBq2eWUtAaXatfYLn1EzJuc5Ys_ebgfR_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=qBAFLazsbyQZM_o240eIIkCF0wJzRlUJrcC1GYF-M5_bfAjOY6FcQ5bg_5oxIgnOp37Y2sJozs9ZBDdmJ2vNrkB8rbVpZVDO0OfNOgosvbW_C0WqDlCjZnSb_lAMdxNhCvVvFmLwsdWoYi3GZlB7IW5f936Hcs-HdmZmiIcy3dPfTTFim4ePmKotyTsMmmvVN73Ccx0httROdQE0VM5BAEG4paigYQVkjVoqBgqimhW2Le5joIMjj-SS44LpSDEZQkFUOyHJ5PRwGEAu7mKyyz4tioCnzl9iwUL70LPrwF_WEpekjIDSsNaCtem2DZhBHudF-CGnmoBSoxTEaORs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=qBAFLazsbyQZM_o240eIIkCF0wJzRlUJrcC1GYF-M5_bfAjOY6FcQ5bg_5oxIgnOp37Y2sJozs9ZBDdmJ2vNrkB8rbVpZVDO0OfNOgosvbW_C0WqDlCjZnSb_lAMdxNhCvVvFmLwsdWoYi3GZlB7IW5f936Hcs-HdmZmiIcy3dPfTTFim4ePmKotyTsMmmvVN73Ccx0httROdQE0VM5BAEG4paigYQVkjVoqBgqimhW2Le5joIMjj-SS44LpSDEZQkFUOyHJ5PRwGEAu7mKyyz4tioCnzl9iwUL70LPrwF_WEpekjIDSsNaCtem2DZhBHudF-CGnmoBSoxTEaORs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=LwKkECSFI7lAlSOUBtU9KfeG8jEc7Kr1qgfiksbzk3x6nf0BTmavQo_JIRnXCDRXt32uUqLxXkdES99JXS-m9zGpjC2jOFJjiZym3IOS1oiTN1QQRr7ZqUkP_fpxaqeXOPATvkx571K30iGIwwSEFoQdSLSLZnBZAatwb_uMdlNpuF8gr7u3_wA3avQjtHMedyK1UAKBsqcNQymm0LgkGxUwDR4mc0vlaNra2K4LikpVURSJ5-Q6f87XpPoyN0pLklRGN4bFRu1Zl5BhtcUE6P4jLIagaDsncOTHvbREpN0yDtGwqgqLSde7nGwpq5NzwE445WGfLLRmXYjQH4TmSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=LwKkECSFI7lAlSOUBtU9KfeG8jEc7Kr1qgfiksbzk3x6nf0BTmavQo_JIRnXCDRXt32uUqLxXkdES99JXS-m9zGpjC2jOFJjiZym3IOS1oiTN1QQRr7ZqUkP_fpxaqeXOPATvkx571K30iGIwwSEFoQdSLSLZnBZAatwb_uMdlNpuF8gr7u3_wA3avQjtHMedyK1UAKBsqcNQymm0LgkGxUwDR4mc0vlaNra2K4LikpVURSJ5-Q6f87XpPoyN0pLklRGN4bFRu1Zl5BhtcUE6P4jLIagaDsncOTHvbREpN0yDtGwqgqLSde7nGwpq5NzwE445WGfLLRmXYjQH4TmSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=Rj5pqbVvYfrg2YuE_q5UwcyQR5aICqJVpjcn9Clq69UtP9_0JN_HFEJ92UARcz8AXeW9u0ZBAK1tK79Pj8cg_rUE1iVRw0hXB1mEIzvSpNJEqYqBMM0orQjQn7bhj_DikHoemB_796X56PLWWUafmutzjnSGIl9mF48ijP_74XFP2QWorHx1pfCdwYL-soWmX0jNIlYvOPnR_9-9zaygo0LcaLWd3kHrIR_RBzzjYVjUw0-6C14-rIxaphlaO-IIjvp7JqOTQsequMVT85BnGi33-rvjBUKvF68HjQWpqLXLENT38F1SAb-5f6S_D94nSrZK_OMP4ef9dLzUwSq0SQv7t2ppxHrJ4DeEoth_BtCGWtTs30UXoHhLhK8IMx9m3sgWJUynywnyuqzdRR0URV9OgOIV6ci7ouYah9hB6Y0E108dr-VPATrGSgOv9l9t4Qnzpik_lm7FMLiKagrqnIlkSH_n38gJ90Cv_zkqEyyk6LqsOCmjSnMHSs-iGO_Ios786bng3_EOVYWtH2Ji0gaLeCpJYy11tqdMgGQieTcKWiOUns2vub09lVXasxpykuxwpkAp5KaZB2ZomgYijlUJHoQiQs0WC6bAe3xeh0FtqL401vn2WYUexCqGetbO7-bfJ9ifTjCFegK6rZ-6Fv-ALEN6ARaWNfbam-2TSOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=Rj5pqbVvYfrg2YuE_q5UwcyQR5aICqJVpjcn9Clq69UtP9_0JN_HFEJ92UARcz8AXeW9u0ZBAK1tK79Pj8cg_rUE1iVRw0hXB1mEIzvSpNJEqYqBMM0orQjQn7bhj_DikHoemB_796X56PLWWUafmutzjnSGIl9mF48ijP_74XFP2QWorHx1pfCdwYL-soWmX0jNIlYvOPnR_9-9zaygo0LcaLWd3kHrIR_RBzzjYVjUw0-6C14-rIxaphlaO-IIjvp7JqOTQsequMVT85BnGi33-rvjBUKvF68HjQWpqLXLENT38F1SAb-5f6S_D94nSrZK_OMP4ef9dLzUwSq0SQv7t2ppxHrJ4DeEoth_BtCGWtTs30UXoHhLhK8IMx9m3sgWJUynywnyuqzdRR0URV9OgOIV6ci7ouYah9hB6Y0E108dr-VPATrGSgOv9l9t4Qnzpik_lm7FMLiKagrqnIlkSH_n38gJ90Cv_zkqEyyk6LqsOCmjSnMHSs-iGO_Ios786bng3_EOVYWtH2Ji0gaLeCpJYy11tqdMgGQieTcKWiOUns2vub09lVXasxpykuxwpkAp5KaZB2ZomgYijlUJHoQiQs0WC6bAe3xeh0FtqL401vn2WYUexCqGetbO7-bfJ9ifTjCFegK6rZ-6Fv-ALEN6ARaWNfbam-2TSOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=a_GS2HtlDZkH93PO729-g_AlvLlP9QG-F3sJ9DpB_m7rrr-IozS3q-gXwJ_4Pv9QNEn8t3pocZBjE_w-eHVZeZKm68cx9MgQXrpDFUTspf7z3Tzia7s3uH40U5c9O1l8UO3buVWPX1VOa-OcTmNJpwBgaB8F9GI5NSl3iFpqkX5hjvF3RFO_MvA1rBsQKxyvnZ50uOdslIrEFbKZviD9AkphYVbAJPyjwb_t3bDzsK6CXCvxb6OG52tG9XjdAsMBYUWH4Simkkl_nuoQDKnA91zqP_U7nshxfiVZ1HstwVwuALRJ-jmUhvhsdE7TZJJfunJGUTalYMfAoUc_BPVKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=a_GS2HtlDZkH93PO729-g_AlvLlP9QG-F3sJ9DpB_m7rrr-IozS3q-gXwJ_4Pv9QNEn8t3pocZBjE_w-eHVZeZKm68cx9MgQXrpDFUTspf7z3Tzia7s3uH40U5c9O1l8UO3buVWPX1VOa-OcTmNJpwBgaB8F9GI5NSl3iFpqkX5hjvF3RFO_MvA1rBsQKxyvnZ50uOdslIrEFbKZviD9AkphYVbAJPyjwb_t3bDzsK6CXCvxb6OG52tG9XjdAsMBYUWH4Simkkl_nuoQDKnA91zqP_U7nshxfiVZ1HstwVwuALRJ-jmUhvhsdE7TZJJfunJGUTalYMfAoUc_BPVKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=jKm6bt8KXoi9hwEFVJHEpmfoFtUKWyGF2G9pNMSjR-qybGQMnb79vUCObnbno0NMPXxUmsQPUEXIb0QpgWWhGejSc2LyrRR7NlY7fX8MHxKlX6gIxsam1GwGbiFUQUtu1a0D83LSSJ0lOL1-77K6CPY4e93-n9OjcSb3qNDn8xpHX2NHaSvPjZSY3K13glWSmBX6oDj9lyogu9V5avmWRO1aamhnSuW8qK77dDM_1T_0ioor9kH5kgVq9xCsGyXccid7X97rAN4T7O1trdO00SEGLzPrrFGcMpNOPWp3li7k_gfJRip1EenhicshawY3eVzibrPDONhRtGE5G4rtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=jKm6bt8KXoi9hwEFVJHEpmfoFtUKWyGF2G9pNMSjR-qybGQMnb79vUCObnbno0NMPXxUmsQPUEXIb0QpgWWhGejSc2LyrRR7NlY7fX8MHxKlX6gIxsam1GwGbiFUQUtu1a0D83LSSJ0lOL1-77K6CPY4e93-n9OjcSb3qNDn8xpHX2NHaSvPjZSY3K13glWSmBX6oDj9lyogu9V5avmWRO1aamhnSuW8qK77dDM_1T_0ioor9kH5kgVq9xCsGyXccid7X97rAN4T7O1trdO00SEGLzPrrFGcMpNOPWp3li7k_gfJRip1EenhicshawY3eVzibrPDONhRtGE5G4rtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=DwOG_0VF9ymKDzP1vXE9z2yJVVfj5MVb9c7PF6_28gfCIK-yFS_ihrHOeNmKZEOsGqwquBDf4XJXX-F1og5BkrM1AWXUiWJCCl_sa_a8DUUcEr0iTi_6uKIlbH3YO9TwXQUzvYRA-2Xh4DngFKdSJoxaj5B60aweG_g9vc63ISnP8FZsyGtsMKItPKz0l_VJFZv8I9mKOfD52vPfxEX167XPynM1gglNIm8ei7BsDhStm32vkeHvg3uqaVmCNTRTcC_2yNl9bhFp4qrs5uDoBffZPjregwK0lfc7WjsBiz5Axo-rvJ1O2iXQ91JJDjOmqj8kyRehu9mKMa-r08fdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=DwOG_0VF9ymKDzP1vXE9z2yJVVfj5MVb9c7PF6_28gfCIK-yFS_ihrHOeNmKZEOsGqwquBDf4XJXX-F1og5BkrM1AWXUiWJCCl_sa_a8DUUcEr0iTi_6uKIlbH3YO9TwXQUzvYRA-2Xh4DngFKdSJoxaj5B60aweG_g9vc63ISnP8FZsyGtsMKItPKz0l_VJFZv8I9mKOfD52vPfxEX167XPynM1gglNIm8ei7BsDhStm32vkeHvg3uqaVmCNTRTcC_2yNl9bhFp4qrs5uDoBffZPjregwK0lfc7WjsBiz5Axo-rvJ1O2iXQ91JJDjOmqj8kyRehu9mKMa-r08fdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=F1AnYsECtERsNYtY0KJreMVkNnQ8WtHSiS56bPzfVWP97QiacNatFzWWCYSj9WSyPLfq6bhFTeF_F6v5gcB-wlVHTMbQV9S6Ef1ABvRxPL-g_r7XvjC-4q5_T9fNfjN6zttcKsXnpf4Fqy5Dy6WN7XRbtldrHLppA41Ok0OLlUqhg8TKDOemulJO6eJ-jEwqSBRW2Iqk4RVJkK61yyFMKvu4LxPK0ZjmDmPjbKlGs4twxrBJ7k4cfK6_fRDgrOPSc0HxrcF_47QCC7TuFuIi6HTdz1UOcEFgCgwkxeq2I7VL0q5l3Nb5PirGony4F9AXUbquf4s5PywLCz31iyVxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=F1AnYsECtERsNYtY0KJreMVkNnQ8WtHSiS56bPzfVWP97QiacNatFzWWCYSj9WSyPLfq6bhFTeF_F6v5gcB-wlVHTMbQV9S6Ef1ABvRxPL-g_r7XvjC-4q5_T9fNfjN6zttcKsXnpf4Fqy5Dy6WN7XRbtldrHLppA41Ok0OLlUqhg8TKDOemulJO6eJ-jEwqSBRW2Iqk4RVJkK61yyFMKvu4LxPK0ZjmDmPjbKlGs4twxrBJ7k4cfK6_fRDgrOPSc0HxrcF_47QCC7TuFuIi6HTdz1UOcEFgCgwkxeq2I7VL0q5l3Nb5PirGony4F9AXUbquf4s5PywLCz31iyVxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-45JQlVNEX5TJAV7vCcZ7_p-CbBgIz9tzZg6wskLNMJsh06wXz-g5HEDr0A8yFIHr4qFHyRDwwg9dWAvifb0RqbdO3XFKYzWsB68uCtHnNMRIDnODU2VgjzsU9RNJ4t1Kx1a7JOb2RIL6TH8AAIguRb28-MmHYv44XmKwIiQw5GMuTh_1JH7lACFa8jY9qhsoAEcPpZ4Jdlux6SrRhA9dAxtSiGbPC3I5k6-peQTGD4FVQdwSFqGKAoG_f5ctNGEGha14fJ6fhFXyRrfZZQV8ddNmCkkyPgGPRhpJIBp_xtAAb62r3ZEgHe5twofIYT-usxvnoUX9qVtYA5BUqXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=iF9_K-8vU9K8-ymPRQXUaY63PEuZyX9BEnOErCnucWSVx-5AHaqoN0reQRaHHUUUBHeqPKaOJ4AZnh2i-F69Nz6ogVB7Gdyleo6S0YQ2GGu_THATGUwItrwl5-Pwno8nqy4HNZIwr8gBhGYBHDcNwllxYCBv8zfUeY7nHBF4kGdFa_r2FcmNa7QNnpKfKRYxK1f2lEB9nu830cs4JruKQHGmkiAedVdPCnLassSo8VCE89iapwjt9tJzJj25SnbjLhjp-lD6e4caJRc0kvbwhmfg3Zn8o0MKSFYtrfa77PpIj86oFgSL7xnRyN8L5Ykh0jFhssNvO3oTBgTyii9ZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=iF9_K-8vU9K8-ymPRQXUaY63PEuZyX9BEnOErCnucWSVx-5AHaqoN0reQRaHHUUUBHeqPKaOJ4AZnh2i-F69Nz6ogVB7Gdyleo6S0YQ2GGu_THATGUwItrwl5-Pwno8nqy4HNZIwr8gBhGYBHDcNwllxYCBv8zfUeY7nHBF4kGdFa_r2FcmNa7QNnpKfKRYxK1f2lEB9nu830cs4JruKQHGmkiAedVdPCnLassSo8VCE89iapwjt9tJzJj25SnbjLhjp-lD6e4caJRc0kvbwhmfg3Zn8o0MKSFYtrfa77PpIj86oFgSL7xnRyN8L5Ykh0jFhssNvO3oTBgTyii9ZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=j0bjkcf44jSRyiKN_A46O0C8pEaMITaQ3-0G1NBIYnfrFwY7yXDhYB4Xna9XbQTp7P1HfzEvLoxgiXkMRGWtDfXeBgcJT7b38w2Cxdd_uMBfcZw49qcgO8WlvZYZ6ZvJ491KCKubIzgUobGOOdgId057tAB3Spyg7LrlBzwKISs9Pkij9PB5lOxQsnR7sqyScV0i4GIroL_LcFXFyMzfNuURmTySb3wFnytWA2PUhc6IlEbarJReZINN325-udtdQDQYgG36LHyfPJulsOm99Tv_wkSHnx4Bs1OI2L7uJ1z6I_nPQqe0PbAln_uCsCpz9hEe0atNRmKQz73-E85g21deHSE9QAKy6Bh0afNx0U0hpfP3J8JSozwr4R9UWnbF-Vtdt5yvvHLig-Aw_V6iiCORh9YyOxXr7qU4RwlTrM-Ux0razKmPm8nrsH87Ouc-8yoYO5EHtG0BFcEuscprRdDzl2MX8Ch74jLjrOH9xvfgYktIOVwpvGFQ7dwMDX0yj1RiuRz1BY5Ik1YMsBooA7RfRQUhxx8HjG3WoUMaeKLfFpxRUZjACPr2E5hW9fK_r8wA3XSDzEPDYeZwx3s6OInXsq_yb9FXi4OVAt4omzdp81q6fM2mgYd8GIHy8Cdt3ySpQ7YMiIcai7NE9mrGKzWfZy-ajMt37nSsKmDN3lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=j0bjkcf44jSRyiKN_A46O0C8pEaMITaQ3-0G1NBIYnfrFwY7yXDhYB4Xna9XbQTp7P1HfzEvLoxgiXkMRGWtDfXeBgcJT7b38w2Cxdd_uMBfcZw49qcgO8WlvZYZ6ZvJ491KCKubIzgUobGOOdgId057tAB3Spyg7LrlBzwKISs9Pkij9PB5lOxQsnR7sqyScV0i4GIroL_LcFXFyMzfNuURmTySb3wFnytWA2PUhc6IlEbarJReZINN325-udtdQDQYgG36LHyfPJulsOm99Tv_wkSHnx4Bs1OI2L7uJ1z6I_nPQqe0PbAln_uCsCpz9hEe0atNRmKQz73-E85g21deHSE9QAKy6Bh0afNx0U0hpfP3J8JSozwr4R9UWnbF-Vtdt5yvvHLig-Aw_V6iiCORh9YyOxXr7qU4RwlTrM-Ux0razKmPm8nrsH87Ouc-8yoYO5EHtG0BFcEuscprRdDzl2MX8Ch74jLjrOH9xvfgYktIOVwpvGFQ7dwMDX0yj1RiuRz1BY5Ik1YMsBooA7RfRQUhxx8HjG3WoUMaeKLfFpxRUZjACPr2E5hW9fK_r8wA3XSDzEPDYeZwx3s6OInXsq_yb9FXi4OVAt4omzdp81q6fM2mgYd8GIHy8Cdt3ySpQ7YMiIcai7NE9mrGKzWfZy-ajMt37nSsKmDN3lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U07lNd7mnH4YjTLhnBMvvojMV9P2Na6OkhxgHsqaKShMbPKQncHgewa3mwFZ09etmuQ30JYWvOH9eqOLw7L-N0h0LDQIDfiepCHD3ebTcbNH9HNcvOPuSF57xtl58FbaDUb7X3vUpaQ9zdBRpzntbHJWDreALI3B-ZCBM9sKgKK2_jJMaPas2DJB8Oyee4spfRXXOTMbliymgmTqkyDLBHBF4000gfduJS7eV6zH7EPta9QTkWZ5GGQ_dIZuQPqVW24Q1y8S94F7vIgv_OjsK3J4WJNzKLfkjZVrgDYJA-ELgHIBLx8r9UNOR3EA63ZUC_-aSJH___ErLHB69CcwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=cJuAc1aVPzyRmKkYs3sJ86d8U3Xpj1J16mcBczsRkNv1nb7LA36m220hzCOSqksLmQUfFfl1gteW96B9uApsxlU3IWwiUf-TuHvAFzxHumM4jvdKnq9HDpfiOyvU0tBqkG8ppXkADdALlyOJak-RZEteMWW48TYiEhk9h9TElP5ZWcFG9opqliNHSPmEETc6v5JatgbKy962PGn5nrtJt4LEW_4-QcwN-5rANDYCIfoLhCKOqj-K2RDapFFuPLskmFiGhbqfrQ-lXa13gdF10VCFBqhMS2ag8cKjxMcnajROTY5uZq-cJYlu8E2khKmIEVbSUmQw1p33gNDsrJpMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=cJuAc1aVPzyRmKkYs3sJ86d8U3Xpj1J16mcBczsRkNv1nb7LA36m220hzCOSqksLmQUfFfl1gteW96B9uApsxlU3IWwiUf-TuHvAFzxHumM4jvdKnq9HDpfiOyvU0tBqkG8ppXkADdALlyOJak-RZEteMWW48TYiEhk9h9TElP5ZWcFG9opqliNHSPmEETc6v5JatgbKy962PGn5nrtJt4LEW_4-QcwN-5rANDYCIfoLhCKOqj-K2RDapFFuPLskmFiGhbqfrQ-lXa13gdF10VCFBqhMS2ag8cKjxMcnajROTY5uZq-cJYlu8E2khKmIEVbSUmQw1p33gNDsrJpMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqTBekWI2lkyttc30DdkGhPA3Xf0UlzIIZbNUdcnVUedxtka-SUxXOWVx3ydkc90mTaKop9yhqCJc9K4d5ZNoRr9p4Y8a-eVqf7xuLjBJkm8wNIR8qk4Xmki9RRLvQABjXjoiwj8wYD05WhHg6RFKkzHL61DPVlcXGhAuMc4niitHGDM3cuQghMof6t4FwXJzUpOnlxlXTEbaV5WJjDVZnRpXD_Pxa2NhkVWNMgtRTBg9SUYqLQGrPLru_M3QFwhd_lymNuoA1gKxErxen3gihnL-3mWJVUxLbkgtMQfi3qwfsUI9JLk08aXOnkm_i0mMrK1Qgo4cPxQYNWH5yRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRDuWjU4wfQTCB92cnwoM6GmyTZARHGaDzaghxMKrnEHkoOK1t1d9wYwwMxKXF96sM3t7caHQGVZ0yR6O-crUuTUHgHkhmIZ76aLCNlWpvw4qlBYrO-GyKrt9q-MciMDM3Tt_HMqi0jS_GMj5ohMRJpWd8TyHHBKhshgI6zWIGMhac74ZeJ0us0OxeMeXwvUmReglIMGCa16gvz0rWK5-UxQQeCJ70yi38n8cDSLPkSr0Hs3z_D26-_kpLxlWsh6QZHUQ3taldwf3BXwCIgbx1FDzwxA03tdwY6ZTFDKi5uMj9ol1qvbgsRdPuGalrjB6cFEEfthp0RgH09-vAdRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=uY2z_xceSdzldNbnemEdjjjnBmKm2rgHL76IoZmwn4_ZVS-pLb1W5Z2Ci0HiHwiQAxkrOeQjYHbiTLmawM0sNTVGb_y9H08jqGmpkb7GMZw_1VtVVgEPdRszKd82Ie6I7Uqfc2ZsLNxMqfIoVuvlRk873BxmY78Y9zrFYFaoLR3t7Lz_aENLfbGG1NsEdkwJgZLkqo4G7TXmdtOQHga_DTr2oDvz69VbNg79yKmv3GqGnoIPSwPCElJ-O3ZlW6x_cUyHtb8L-kc6jDnB-SZ7x3_NDyCOjo_q3D0hg2sW-FQDNbM-MgfGpZptgqjqhoOu8WjDQMVLye3U2kRkqBF76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=uY2z_xceSdzldNbnemEdjjjnBmKm2rgHL76IoZmwn4_ZVS-pLb1W5Z2Ci0HiHwiQAxkrOeQjYHbiTLmawM0sNTVGb_y9H08jqGmpkb7GMZw_1VtVVgEPdRszKd82Ie6I7Uqfc2ZsLNxMqfIoVuvlRk873BxmY78Y9zrFYFaoLR3t7Lz_aENLfbGG1NsEdkwJgZLkqo4G7TXmdtOQHga_DTr2oDvz69VbNg79yKmv3GqGnoIPSwPCElJ-O3ZlW6x_cUyHtb8L-kc6jDnB-SZ7x3_NDyCOjo_q3D0hg2sW-FQDNbM-MgfGpZptgqjqhoOu8WjDQMVLye3U2kRkqBF76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=DrgihsBJyhokzdsG8Hcx6trOrqAavYo3FAR9C-t4lGXqjAQiLxmN9o1tFarY-sny-DVbpTwHOG7iUmpuxsrEi3OiNJN166dsBErP1ff-avqws_3sRsxuZjIMyzKGLtFBgeAYwP404R_3OmMUpKQVm90ACphRB86SSpoc2xrfTxB6ohyQPFC4ydAaIcAyrgPkunWClJJRNlb13H3cXD8Zb_KxEl1qIEbs3ogOQ_vZ6ZWw3TEANvA5JgZC9rm88im0KncrckTZt5BL_eBiklSPonWKgbmTZFnzviIKFY-RN_y3uhiORCw-k_CKaI3jD5RHAo_KUxIDQllc68Vd7VOT3y0lpv4yP_gaIbloivAct_h9xPN0YnNuSXDwdT4kSv4WBYXD5LOPTZY44IV2W22PVSWN_nGJvZ1mgKk1cSs00aHTMYjkFL5L3Q_sMd-L0F2vMHRrXCqMuQgUIB0GAg0GDg8Ej0zSDZHFbtjN8PjfL1uZiY3Doe_TIBkAsNFdvL6QMUOpHABEJBQ3jSFhWWMRWMdJcbQ-oRyvskCAyUhYbESG91dgs9Ds44kuLgkz3l_VNpOWQnti2OLR77Hn1rSR5y5hZmVr6PV965M0bJYpN2Zy82MQHJrOrwDPiivtjOIvHuEAgM7OTGOS7rWddvmUVFLmYMVKWC2fT4gnt9uwG4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=DrgihsBJyhokzdsG8Hcx6trOrqAavYo3FAR9C-t4lGXqjAQiLxmN9o1tFarY-sny-DVbpTwHOG7iUmpuxsrEi3OiNJN166dsBErP1ff-avqws_3sRsxuZjIMyzKGLtFBgeAYwP404R_3OmMUpKQVm90ACphRB86SSpoc2xrfTxB6ohyQPFC4ydAaIcAyrgPkunWClJJRNlb13H3cXD8Zb_KxEl1qIEbs3ogOQ_vZ6ZWw3TEANvA5JgZC9rm88im0KncrckTZt5BL_eBiklSPonWKgbmTZFnzviIKFY-RN_y3uhiORCw-k_CKaI3jD5RHAo_KUxIDQllc68Vd7VOT3y0lpv4yP_gaIbloivAct_h9xPN0YnNuSXDwdT4kSv4WBYXD5LOPTZY44IV2W22PVSWN_nGJvZ1mgKk1cSs00aHTMYjkFL5L3Q_sMd-L0F2vMHRrXCqMuQgUIB0GAg0GDg8Ej0zSDZHFbtjN8PjfL1uZiY3Doe_TIBkAsNFdvL6QMUOpHABEJBQ3jSFhWWMRWMdJcbQ-oRyvskCAyUhYbESG91dgs9Ds44kuLgkz3l_VNpOWQnti2OLR77Hn1rSR5y5hZmVr6PV965M0bJYpN2Zy82MQHJrOrwDPiivtjOIvHuEAgM7OTGOS7rWddvmUVFLmYMVKWC2fT4gnt9uwG4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=QDpyE36buqX_TE7n43BuSPGTPxGEcJKecMC2W_9T85jgJD2YwcFtePCnb8MhF0HOz_XD1bI1IllVauur9avHY4QeXuu_Lu7O4uLRF0nwEFHdNCa_K1LA65cQ8RyxXwkg3Px6DgLDng3pQ1HyyR-adZA6xQzSqtduzSCnTuJqkd3GMdBuSHtjzKDez7-PgqCUE99fu0NvY2trzEE9e3Xenx0UlkoKI1jOBp7_qMrJeTL3l7Jy-gJWFRrNnoQ_bXhE0JMrcPoLWlF_CNkTEgS3VQVl93PPxONi01D6oXMGELOc_B0jMYZaUW0vUn6qWFkS0oJbvcpxbWyVyVKoRp9vaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=QDpyE36buqX_TE7n43BuSPGTPxGEcJKecMC2W_9T85jgJD2YwcFtePCnb8MhF0HOz_XD1bI1IllVauur9avHY4QeXuu_Lu7O4uLRF0nwEFHdNCa_K1LA65cQ8RyxXwkg3Px6DgLDng3pQ1HyyR-adZA6xQzSqtduzSCnTuJqkd3GMdBuSHtjzKDez7-PgqCUE99fu0NvY2trzEE9e3Xenx0UlkoKI1jOBp7_qMrJeTL3l7Jy-gJWFRrNnoQ_bXhE0JMrcPoLWlF_CNkTEgS3VQVl93PPxONi01D6oXMGELOc_B0jMYZaUW0vUn6qWFkS0oJbvcpxbWyVyVKoRp9vaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=Clqnyqhx93HoyeNesHoyy5kAKK0g7AkNzLvN28fz0gh97nK7sWGTUh5UV6DlmoI2MdAJLvy4GOW4SthW-ddvq1TATXcHQsdWQRhy4Bl2r8FbuPEi_rQNlPNeYRKJx6riEZQu_U9fENSf8pEGS98MpTZxlO_IJYWkgaabfVDeTem7Ce25qDYiUBhnNA6Z6Oa-0hb16dJP3fINrWtmDJx6MRNd4quQBCtHV1WMDe5ySvZUIOuMUY-K8lHDXxhnZNlz04mDQJeor45U8QRGtDkGxnNzkUx7OvHHjo9t-NW3rgsYV762nYF18hp_zQ2p5zSnL3dLR1kkYtHN2Ppc9xlg0LxOSa80HR1tfDcbIINGA0j-R7FbL8CJTDUA9PVlAvWW1nJzTRDHBWq2kZdpV8IqsFjbZAnrnb0ezKo3oyrIVspOztKia3c8UPLTjdz3pUfwpYs5vFjRI65pfexiscG3DYLx6MRYI8VaHlJQBUyprNJ0J5qZbIVlAIA2JBJFX3skkadHrdHnHT8Jb5e7G7ejT1Q7oSTA3WXj2M6s8peWBOWcf_b4QTEq_7jf_TawvzDS863OVAGS2qlmmaFBJJwHbcKu1oTZyfD-k0aeGPhdf16sOvM7beQWjMMX0sFf9Dd4-psdpc6pmezcoF2Ot55PP_t2D-ldIxD4lmUcwu56_eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=Clqnyqhx93HoyeNesHoyy5kAKK0g7AkNzLvN28fz0gh97nK7sWGTUh5UV6DlmoI2MdAJLvy4GOW4SthW-ddvq1TATXcHQsdWQRhy4Bl2r8FbuPEi_rQNlPNeYRKJx6riEZQu_U9fENSf8pEGS98MpTZxlO_IJYWkgaabfVDeTem7Ce25qDYiUBhnNA6Z6Oa-0hb16dJP3fINrWtmDJx6MRNd4quQBCtHV1WMDe5ySvZUIOuMUY-K8lHDXxhnZNlz04mDQJeor45U8QRGtDkGxnNzkUx7OvHHjo9t-NW3rgsYV762nYF18hp_zQ2p5zSnL3dLR1kkYtHN2Ppc9xlg0LxOSa80HR1tfDcbIINGA0j-R7FbL8CJTDUA9PVlAvWW1nJzTRDHBWq2kZdpV8IqsFjbZAnrnb0ezKo3oyrIVspOztKia3c8UPLTjdz3pUfwpYs5vFjRI65pfexiscG3DYLx6MRYI8VaHlJQBUyprNJ0J5qZbIVlAIA2JBJFX3skkadHrdHnHT8Jb5e7G7ejT1Q7oSTA3WXj2M6s8peWBOWcf_b4QTEq_7jf_TawvzDS863OVAGS2qlmmaFBJJwHbcKu1oTZyfD-k0aeGPhdf16sOvM7beQWjMMX0sFf9Dd4-psdpc6pmezcoF2Ot55PP_t2D-ldIxD4lmUcwu56_eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=iT2kJ-paiw_FNDQSoVvPeEXl8LmmcvpwRYmve--1oqQ6D8V4iPEHm4B2VWDqPoNBR_TBZtq-ZrmnhTzkPzPZzBc9HzXgpKN7hp8-6Ejh0IK5qQPGlASe1YWX1DM52d5UDntLtLOFqUdLF_fAtJ2c7IL1T0n2UYDppT4J3oQd8Bk8lxKocEQpSF0zYGg_JaVJr_QRLUNB5Tnt7440lftqhDiGopwFCLV6H7U4TGaxfi2flqMEc_282YfOy4Q9fbQjyW2FMyQm_EQraWJ8K7iOlFc42F8AKKsqHCBkH_9btEmOCrc6DYm8oGu7IwIeyexNcP_z9qeTRv3wlPdoiID_pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=iT2kJ-paiw_FNDQSoVvPeEXl8LmmcvpwRYmve--1oqQ6D8V4iPEHm4B2VWDqPoNBR_TBZtq-ZrmnhTzkPzPZzBc9HzXgpKN7hp8-6Ejh0IK5qQPGlASe1YWX1DM52d5UDntLtLOFqUdLF_fAtJ2c7IL1T0n2UYDppT4J3oQd8Bk8lxKocEQpSF0zYGg_JaVJr_QRLUNB5Tnt7440lftqhDiGopwFCLV6H7U4TGaxfi2flqMEc_282YfOy4Q9fbQjyW2FMyQm_EQraWJ8K7iOlFc42F8AKKsqHCBkH_9btEmOCrc6DYm8oGu7IwIeyexNcP_z9qeTRv3wlPdoiID_pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVK5obbVxDy0LWHLd7cp5h-600jOP7IVjr1y-kNBLlD3_NWepTc9uYtOlvoV1QNUlM-BhA6fmQ8FwsiqUmrY2yTQ4ymFLeIBhKJOXglgo9h9etZ3-7HfpTm8ALjkdaqB4pCBP5xX-nMbLMHaIhlGZl290p32bWwTcbOaDNjs9IutiYyWz2_UppuH_sIQdCDIcpBXuXqlZMACIgEbS9IBKiD1iRf_vvlIPH-n3F74K5uLdzJtYf_NuWDeOfgeJgkOx26mISQINpie5cC6SZCUB8fXfcEzNQiGTsG6MF0PBEpDoIkXbOSGQgBihuY7ahg7QE7-vTwynT5yjJty1YZ320NV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVK5obbVxDy0LWHLd7cp5h-600jOP7IVjr1y-kNBLlD3_NWepTc9uYtOlvoV1QNUlM-BhA6fmQ8FwsiqUmrY2yTQ4ymFLeIBhKJOXglgo9h9etZ3-7HfpTm8ALjkdaqB4pCBP5xX-nMbLMHaIhlGZl290p32bWwTcbOaDNjs9IutiYyWz2_UppuH_sIQdCDIcpBXuXqlZMACIgEbS9IBKiD1iRf_vvlIPH-n3F74K5uLdzJtYf_NuWDeOfgeJgkOx26mISQINpie5cC6SZCUB8fXfcEzNQiGTsG6MF0PBEpDoIkXbOSGQgBihuY7ahg7QE7-vTwynT5yjJty1YZ320NV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=XfPNIU_3uv_AC_ddnjoqnlVt17TXBhcVL-DqisqsGU2qtDzxgb6wjM6IR4RFHPK7E5IBOECfRAwkCBcum2Sk8SLJwAO8UhtOT_VSN3tcAfBHLz5DiQB6f3-SrDTIrK6dUre9emO7JvMLs0GfPJe-YfLokYd4FA5e7bSFI1LOgvy4rB4aKepytmZ3j3na01Ar9QD_cRXXgmuAzzeqzh9lWLXAtYC7b8GlxeQlbQIbHNQCf0WoyPcn3OrQVcRlDpn1S_4_BCovnGHXqalE29IXF4jyxSnnnqkML0SYlTKhwlgjT5XClsnrjzCGHODqu3C-twxmhOIAI-T2rR8vFHVMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=XfPNIU_3uv_AC_ddnjoqnlVt17TXBhcVL-DqisqsGU2qtDzxgb6wjM6IR4RFHPK7E5IBOECfRAwkCBcum2Sk8SLJwAO8UhtOT_VSN3tcAfBHLz5DiQB6f3-SrDTIrK6dUre9emO7JvMLs0GfPJe-YfLokYd4FA5e7bSFI1LOgvy4rB4aKepytmZ3j3na01Ar9QD_cRXXgmuAzzeqzh9lWLXAtYC7b8GlxeQlbQIbHNQCf0WoyPcn3OrQVcRlDpn1S_4_BCovnGHXqalE29IXF4jyxSnnnqkML0SYlTKhwlgjT5XClsnrjzCGHODqu3C-twxmhOIAI-T2rR8vFHVMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=UKEXyxtctCsSRwUH3EGyeTOQQdPLDLcPnMwOYGaHzplYSW68aisBX2uTfDATATi4N31fWQt4MecvnWtZ9ig2DH33TUVnnnu-jG2u86QXg_h9XC5oHj5r77tXr8hGudtrfWXlj7MraWQVN72rmiRN63ymA-e_FKK4peF3zT2Mx-TeJ8VPfAsCulH-w9OuNN5fxwpmaoNw51NaMX4ZGKPAXvYFn4lRdyDDNj8QmWwTbyCdKkS0qPVoGqz51rA-iDTbduGjRBrBc1w1bBEZJc5pH4LpakSCZSvXnFGUdJ2bl-ObqNBWmpsxBJCVCIwnDy7FGJHzJABN9qgUqT36Svhinw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=UKEXyxtctCsSRwUH3EGyeTOQQdPLDLcPnMwOYGaHzplYSW68aisBX2uTfDATATi4N31fWQt4MecvnWtZ9ig2DH33TUVnnnu-jG2u86QXg_h9XC5oHj5r77tXr8hGudtrfWXlj7MraWQVN72rmiRN63ymA-e_FKK4peF3zT2Mx-TeJ8VPfAsCulH-w9OuNN5fxwpmaoNw51NaMX4ZGKPAXvYFn4lRdyDDNj8QmWwTbyCdKkS0qPVoGqz51rA-iDTbduGjRBrBc1w1bBEZJc5pH4LpakSCZSvXnFGUdJ2bl-ObqNBWmpsxBJCVCIwnDy7FGJHzJABN9qgUqT36Svhinw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=L3S_Ao8eosI6ELX4ve7wSS7-zm6LIcJYZCFyMnAq4SwqXuSYZcS6uF0IfME0rPQBfJEMtyQ6U3zwZvY6S1oUBceHgYcCkl15GPC_WeoSHY3osB6YnQDGaT96f0VjsFOtjdtk8dKEdgwu6b8BbQ_mUSkzqvICdSOTGiFLeqM0l4mB8m8j80vaJB5kat9QMk-LGI4fLRyAW37LTHgWhDLxJj-i16WFP6SNU-1x5_LNgFyrP2AY47knwHS2Qwj4JZHmQgERNz2gDy8Scp0leNU9sAWIzql3DyIpj2JZUjoGe_rOLbvFPpP9X4zmUSjriQKZmkciPpKD311g9-N1v95l_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=L3S_Ao8eosI6ELX4ve7wSS7-zm6LIcJYZCFyMnAq4SwqXuSYZcS6uF0IfME0rPQBfJEMtyQ6U3zwZvY6S1oUBceHgYcCkl15GPC_WeoSHY3osB6YnQDGaT96f0VjsFOtjdtk8dKEdgwu6b8BbQ_mUSkzqvICdSOTGiFLeqM0l4mB8m8j80vaJB5kat9QMk-LGI4fLRyAW37LTHgWhDLxJj-i16WFP6SNU-1x5_LNgFyrP2AY47knwHS2Qwj4JZHmQgERNz2gDy8Scp0leNU9sAWIzql3DyIpj2JZUjoGe_rOLbvFPpP9X4zmUSjriQKZmkciPpKD311g9-N1v95l_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcaQdaOm-y0OfdfErRX3aBh8Mz2Hi4tuhJB0bPw-LgFlXv8nPAXYu9Zl_q1hcMI_o2bo7uCmupo3wesn2VYxy-ZSGnpkF0KXcrNvGQDEgqYyNPQ9P0gKDzLCyDqsSQy-AD1hPtZu7axPRavExuVhzZsM78V3mypQ8TR3dUr5-URSA1bQ24H55qEbLzfvRIRxdwMqDb1kLOfe5jELSHuRBt73jBTpUvGxaxcaWxyd7jHuhgGZ2Poim-1om2vYSkU_kBGRKRFXCAqe8ykEww1zuXpMPlkMAI8tK6WfgyCjyzA_o4B1VPnO9mNaTb1yCCfFaFMfLfaH9sCbXkLfUPQsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfKDFwT54bewO-3hu1kJus4dHu2sbcKPcYAn5Iqmz3_2vj2CXahj9-e_eYoKow54QX-LOP1kuIEo85DHH4pMIwADy2A6ZDVCfj5YXrOt3JlNaA3dCP0abtKCkIrVtHN8mGpnFnvgycyTOs3qcWyWix4RNR9LX31wS4e-yXb1jqFK9ojdFJf-Md0vpIMX62IEFmb8Ycajgmm7IjrXK-XdxJ7Kjgh6ycs9oFyuf9FMpTFsI8n_ACYQjcWiFq3uW3dvKAPFPwaKZNeU8v7IxffTtSRHGHmUlzolRjDaKtjQDsaqYcgFYmD-IVrwIR2Yb-b7Z5REKZHV8o_5ufmRX_1ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
