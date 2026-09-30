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
<img src="https://cdn4.telesco.pe/file/l1jc-ofSF6lu0fxdUE4p9PWiFwlnpYfLmN1Xk4bQ4QOnp8kl5zZ1IIXwlaN5aHuDJ4oM-ZQd7P99qfQaOoAVjDV0Zqy-7QlJ7eo55bJWsxKkrRamDGUzVKmfAL9ZgXfZhjQjR3Yutf8Re3rAMNdIm7yheohWVdDrdWdTQ68x82JC3xkRDzY8iplt6YGinUNSrY1_wMwZRhgwcmz6UFPRgHCfcC6hcEqVsNk71BTYapF7HOKN2tnKHz1ETBSh2tPqALj3NNeiCdR5uvE85opIfQLOgoFEbM0VTRv8IT7VRfWsz2LQGSKn4G7zX_HLq_dq4yoqaGx6Y5YfMP4Ru0v4xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVBqA-MqO6-4wcuQ0hhXfSVSIV6EbjKxUW5GqZZ-HO3rwYrgThwx4hk2l7YsCgwwBjBOxaHJmi805XotlIlQYLcUceSYxnZxWEB7Li3adeUiHvNJC_t1X_OJ4vswRA-9t3FxNFQ1NEdkIc2qnsVPxH3LEqPycvWmLITL_uQbPknoWsEAoKJghVX114t01U0358BS29qTHL7ideBn25aQrbuzhkyZvSO1xeHShQhh5NRASA3jLVXFXk3atzX0y6Pe2myxx9N5jqxNGK1y4M1lx_RPX2BgqVBxgbByL_HcPR30RwHw0Jx91niSaHXTjX0cNMoojLlhYHeloUS7UFMA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF8yVlQ3XwTvufrBjVQyl33ES1ZGV7QDbZ3XULOnX3Wew-041IVSk0D-oVJpkdDpkDf1-6Or0g0VGnSk-uIkdrHwGb-OLMjcYTbMn6VDshivzRT12UJPADphXrHS_kXbVwZKfQ5pHUy9UHj0n2JCEkYis1CD9d5IBSIOLAMZRUap4wj7rTqsa7wlLafaNd2n2HfpU0it2wnmmT2x25jdXzHTwdA6F9rNfKz4-XOZXlAwcponA0VwutjGDWdBuy32JbRUYgQa1IylOkkOaxXsOmPZZdF2snQ0qeQaC8LGmCrYZs7YgUZ6gT6V7kViwKRXBuC_lVoaDQEavtq6p7Rk4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=OysVKqY_e8kG3_aGhp1xpPfOpYeRoKAjOfYC13emBB2jrTM5m5xw_bXUCHNDjca4ue6WoyJ73GpwB4Sz33GR3vOh2NcAsPDNZiRz2u7ZaeckjiRGO6l3m_by0Ti9f7Sgo6wYJe7W2SAL1OkINw259dz1irHbEihKwflrKe3Hq6CQJNplmfuJgSSsbckuym5W0UokFVKJKCcH9TY1Nz3f-s1dQQka3Avk4QW83gJ-N5YVoAsyf6IIg1K9M-l2I99qSISPMRu67Hz9Toq00WdnOvfW8sYtaHGISOI00xrZVv3-q6RMgaMBdewJqVnLPIy90PJlXp9dvx-O4eAulj0umA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=OysVKqY_e8kG3_aGhp1xpPfOpYeRoKAjOfYC13emBB2jrTM5m5xw_bXUCHNDjca4ue6WoyJ73GpwB4Sz33GR3vOh2NcAsPDNZiRz2u7ZaeckjiRGO6l3m_by0Ti9f7Sgo6wYJe7W2SAL1OkINw259dz1irHbEihKwflrKe3Hq6CQJNplmfuJgSSsbckuym5W0UokFVKJKCcH9TY1Nz3f-s1dQQka3Avk4QW83gJ-N5YVoAsyf6IIg1K9M-l2I99qSISPMRu67Hz9Toq00WdnOvfW8sYtaHGISOI00xrZVv3-q6RMgaMBdewJqVnLPIy90PJlXp9dvx-O4eAulj0umA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGH25pQEt7M22taJyp1eGu-rQCCkoNgcMYgP8KJTWZE8Udrbml_jd4Nax_UBLEDif3i8C9_1LOpVgZjfYjmAN1SDr6SDYIRPl76rwO5eqhpg_LNp2I6fhKleuAmCiEtayC3QqPYUu7EUF1dggN1MqChauXRJaPsa6sQ7Z42AYLdS7vIKs1oiyMihTlOBOF0x-NjOnKwfLimqmG-9Wc8rLNRQRoVeQ85wrt4cwE7lcTEYvuQ0WVdjeoiPGCTxATJmE8yFB6Wo_NEasvXvTH32bliCqC5rrIAQ2Cud35naY0Ok_g2wQuzj04-YAy2Elke24tRR70LgGwB0D6lLhT4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htKqjmRb5P3X_3mF1PsXwarQWkBv-KH2qfyN3-q34YV1NPLEwpCqH0FLiwhply3UIbXPwtzvScpLxIbzRGHE79rk47qh-jakY-XJ9AmmKdheyUaTvJ-VKPq_Sz1rWN19pZp1_bU3RYCU2oumXrGDmXYbPzccfCUpzdg36SbCb2gfXnLYyjWz1UyBS-C2_5UjR02Z4_oMFdejNn_ge-1QcTFjZpkO4DgIxnjrpNZgIhmjC-Wsel4swwBRTm51zELssnqVmDTfhxkEPaVfTa72tiYG8W7rRsSQoX3W4QrsgnPPRStS8SZtsqvbar5AsH9X2JTx4ZCPnOifdHoX5_X_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaInGAR2U5CM2vgoxKogCN7sCiIZ6lki69k2hM1cDkts3n5PJaHIQwJijZ_7JBYTNQhFBnnHZOVMLl4BvoLzCNyoK9DGNhcO6PP09Xs1Y8z-9GT5X0btwc0o2gDMFswoPQjn1kEYg7-Rt7Cq7D0C12Yt2JuziD4aBJfyHbL008v9-aej0T3N5wx_mC52Ie5_YYvCOrNjRXC7AWGILGs9PKRIRFIGLmuOIqdMAXTyuSigQ1pcXRZFI243JQXrMARGVFyy3jw0uZJpE8KZ2x9UesM05H5NJNfPeeJuxr6Sts8yGlq2Q3m30WQijNbalJggmkCxldZsdcOA0cEYF9oOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=Xlfd59eKpKYexpAKwSY-W4Fgs8DAe1l73tSVjZNzVghnW1dfbml6XxIbKZ5zTyQzycyNjlotR75whwuR_cHQT6nmZjeAPHVCTo2VfeOesMMpH89SybmdctPR89kDe-qjBeNF1uI8qxHQd0591EqYMFFkl_pMYWXkzjqYqx3zD7GZvK2Nrl2zQtPs0Q_6C2VLZ_GmpPSEePM81m8djK2feTr_-9opy2KF13iNmAXw7hpg_Ag3MuOgmJ56HRLaOhm8pineAk934L_rRZIFJ1FK8I0L4WKPNvCqxO2sCVMNOqVBAqCQ0I-biW7TmFT047yTMJvp-1jhY4G0dDPlLpGvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=Xlfd59eKpKYexpAKwSY-W4Fgs8DAe1l73tSVjZNzVghnW1dfbml6XxIbKZ5zTyQzycyNjlotR75whwuR_cHQT6nmZjeAPHVCTo2VfeOesMMpH89SybmdctPR89kDe-qjBeNF1uI8qxHQd0591EqYMFFkl_pMYWXkzjqYqx3zD7GZvK2Nrl2zQtPs0Q_6C2VLZ_GmpPSEePM81m8djK2feTr_-9opy2KF13iNmAXw7hpg_Ag3MuOgmJ56HRLaOhm8pineAk934L_rRZIFJ1FK8I0L4WKPNvCqxO2sCVMNOqVBAqCQ0I-biW7TmFT047yTMJvp-1jhY4G0dDPlLpGvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از مراسم‌های عروسی در ایران، عروس یه دفعه تفنگ رو برداشت و این شکلی پشت هم شلیک می‌کرد!
از نگاه‌های داماد معلومه ریده به خودش ولی کمکی از دست کسی برنمیاد
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=DUEzufN7cl7hgA9KAhdNr7Xk7K82nApnSlJKlq2HHihMiePNy8e9DeMdsbbagrImfCXZXslglmt6lvSDh8_YiNRU6h_9-UIqY73OvvXqul9GrONbkd6KcncYmkwLQGoogjgaKgdnJpKsX6qknk5YAKlL3S_4mW-F6UzKLH6JRnmpx8Osdq4Dprh40zJ7b7BCJL0iIo74wY4i3LuB3Vcw_sEP0SRlRME2L0VgGnYyRS2itm7g9A3pSFRpU-e5FTf8EdtlIeevETYqmMQzjNVyuP7U4F3ncCVubmLxur3Sj5m5bR9_7YA25_GaXsFsCiwKBlkTRawY-M-TTNPGmBNnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=DUEzufN7cl7hgA9KAhdNr7Xk7K82nApnSlJKlq2HHihMiePNy8e9DeMdsbbagrImfCXZXslglmt6lvSDh8_YiNRU6h_9-UIqY73OvvXqul9GrONbkd6KcncYmkwLQGoogjgaKgdnJpKsX6qknk5YAKlL3S_4mW-F6UzKLH6JRnmpx8Osdq4Dprh40zJ7b7BCJL0iIo74wY4i3LuB3Vcw_sEP0SRlRME2L0VgGnYyRS2itm7g9A3pSFRpU-e5FTf8EdtlIeevETYqmMQzjNVyuP7U4F3ncCVubmLxur3Sj5m5bR9_7YA25_GaXsFsCiwKBlkTRawY-M-TTNPGmBNnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Bfg32a-MdegO96z2DFOejMKFEIe46S41w-CLTscRXkWxSBjtCr-mgGYxEkJaBopbAGJnwS8JMS2RnxzzcdECyhEq0pXXo1WKeaAaEozcKE5w7PvvwpuoqP0lOHeS3VTmMk8ToxyP7zgAjSmtukYAFfEa2P89qVy2eMJv8ARcTg3OJar0IX8KGPp5tzmOTIImUYWOexxxV0v1UHp-7WDCQ1pzke-QIP0q61mda0blrtGXPTurSRi7IVqxmKjutbDeszcDXQ8713p0OqTszkLYgmhup6j9ToSsFBiaX022m04r8ayiNMJPWz32uhN4235FJXey_i3B7WCuNgorC7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56db93255e.mp4?token=Zh6epp3SQkC6LbqiB32qnamP8r5tjoN55jj2e00FBjg6haHYUBxRZdoloWprQQixFWIqS-MFzqk1cL8STn3-mSsB2zXKKV3tB534Jti3X_qr45YprMjEIvdb_qcYeldiNQ4zAfPZjpyPf-mMcxuACYCWuqhU3ToRmMzzHqrIGy-MrU3-2BIEMkXscziqJTm7eTCrmb9PdXsG1QMzlKVNXKqVqO1gW0KUViTRq0eMPc4vQlp83OOMCcnKQUgNufPKdAyYfr1W_XdXu_9oi0VddLaVm0e_mPrqnFP_F0Ck6z_Zk0O4TVHJfZeG2wE-bxmXcEXwkZVQOB27LLK6IkCOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56db93255e.mp4?token=Zh6epp3SQkC6LbqiB32qnamP8r5tjoN55jj2e00FBjg6haHYUBxRZdoloWprQQixFWIqS-MFzqk1cL8STn3-mSsB2zXKKV3tB534Jti3X_qr45YprMjEIvdb_qcYeldiNQ4zAfPZjpyPf-mMcxuACYCWuqhU3ToRmMzzHqrIGy-MrU3-2BIEMkXscziqJTm7eTCrmb9PdXsG1QMzlKVNXKqVqO1gW0KUViTRq0eMPc4vQlp83OOMCcnKQUgNufPKdAyYfr1W_XdXu_9oi0VddLaVm0e_mPrqnFP_F0Ck6z_Zk0O4TVHJfZeG2wE-bxmXcEXwkZVQOB27LLK6IkCOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو نپال بر اثر رانش زمین، این کوه با این عظمت به طرز ترسناکی مثل آب، نصفش تو رودخونه سقوط کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72494" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onaQrXsBM61k2-e_7xrmnyDgdAktKPmTVNWbi3cpoA7EWzmUaxY0tIwGmGiL5c6TrmhBsWsDVCAN03Z5fhAKVWmfNUHFZ4bifyJp3GEt5UtoQ1RSaD6uNcDxsPEnLvogY4KWG31b1aHEV054YEkCf6jKOVeNyvPDjAsZEmujkNITforAYnKXZ5wW2QmDN9YvI7cwONdNnNw6ekt-xg0i3CWkGOVLJYtjuthzUZB9gpiKfttTVSsRF1aiZ7UKniZjd4NiJgpKTysis04AOSlMqZDyxfqjUmLNaaYBW5o-3XwZxpe5xAtqzwOWj_Vdmp-NkYux3fdchOY1DIr0mbuXC6DY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onaQrXsBM61k2-e_7xrmnyDgdAktKPmTVNWbi3cpoA7EWzmUaxY0tIwGmGiL5c6TrmhBsWsDVCAN03Z5fhAKVWmfNUHFZ4bifyJp3GEt5UtoQ1RSaD6uNcDxsPEnLvogY4KWG31b1aHEV054YEkCf6jKOVeNyvPDjAsZEmujkNITforAYnKXZ5wW2QmDN9YvI7cwONdNnNw6ekt-xg0i3CWkGOVLJYtjuthzUZB9gpiKfttTVSsRF1aiZ7UKniZjd4NiJgpKTysis04AOSlMqZDyxfqjUmLNaaYBW5o-3XwZxpe5xAtqzwOWj_Vdmp-NkYux3fdchOY1DIr0mbuXC6DY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6nEaNuJtvfehjKva7g36NdicnWcqgYfr9wKjy2izqSASstwZZ7Vuc9Rj2VM3Cxfv0DUjbk3MqwVTYHz-Rc0xrOFU107APf12l-c7rWxkepfJgoyIU20SXBioS9WhEsXQRpUH_jE3JfE3vUeIeIQCPtO7z_FIgZ8h27pwaR50Gf2h_aPQceh9_iezARm1M8SH_U-qbn3cdDkGlEocOZF_zk-MRMx6ltvq5vtuPGAFpQckbZ7jM1FJnubTakcJ1vTfXG-HyrzjO4xYp7fKUI4eKlZa1Us0UToFyK00KGkH9clOiqxXYIMTxlOJJzJ6QeepVdzY_uFoqkuX9JH_OIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTdVwuEAaOWpPB6tNiSE8wN92ibKS6jviTFxR9QHM4NyjWa2kTGgs6FMs_x_YDxsT6GxcmmXNzwbTw3J9gN6c-6yuYUG33Ej04I2Y53ul4UUuylVriDte5dlGY0VQTY7TSgIO4B_izOWefCu4nm2qfMiZ1GAe_rA8xRnvmmFD80goEQT3JsY7B7fRRDyW-ffKrKBesh_pjm7vY0vWob-0bAO0uVh4Vvo5bPrKVZ7M8pf7FC6dVkOIwNZZ5HkqwsAdj5X_Ufghys0Q-S5wDUdp5YYTxmOqUDgEDVRumkQpnOqyO4SxuxIcz3JeKxenpKXd2077Z8rZ_Y_J5Tbgmj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cw3_f8ECK9Hkxd8H2AOdSo68XHBCQuwu9CcYI-NLblk32x_SCnBQNupwe9hm7Xr4Z1QMIqHH78bElUrVtTM5FXUGqO61SmfzU5EaNJQq_iCqXpXQU2TW-OQKVY-7fPzdQ4NABWJMtk9YERlkbJCZbh93JUqNyWQY9SQko10kdjk6Vyx5Rjc5KH-UK64_mT-u2VJ5Ukimd3Bpbt-aKGtuJFt7U2dUpI_L5kUrUoaiTFYhc9j78SXrRbEqzlrME84MC94HDFvsM8NYo4SbBOoy9AC1VUX6Yi5oaA4M5PvmVWdIWM6wFi4g5DEpO-etGS1yJF8nbAC4mZ-uDao8eHa3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cw3_f8ECK9Hkxd8H2AOdSo68XHBCQuwu9CcYI-NLblk32x_SCnBQNupwe9hm7Xr4Z1QMIqHH78bElUrVtTM5FXUGqO61SmfzU5EaNJQq_iCqXpXQU2TW-OQKVY-7fPzdQ4NABWJMtk9YERlkbJCZbh93JUqNyWQY9SQko10kdjk6Vyx5Rjc5KH-UK64_mT-u2VJ5Ukimd3Bpbt-aKGtuJFt7U2dUpI_L5kUrUoaiTFYhc9j78SXrRbEqzlrME84MC94HDFvsM8NYo4SbBOoy9AC1VUX6Yi5oaA4M5PvmVWdIWM6wFi4g5DEpO-etGS1yJF8nbAC4mZ-uDao8eHa3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=N5rjY_NLBrvE2TTtUu0zWks_9uVV7LxHcypVFB3l-2U77VanMeBlDHx6hHopsArC40PG4sltBwLIfnqHrACPMlpNXmCloHPwB_8y_hGbabTItfQ822gyJi22BiHcuuo1fDLhIl_exOXgYxnSeOmxxR4QBhMCE48pv3PqkxsuWlmOQA9VWULHjLGAc1HvvdHwwStzZ7oqdeqMbZ_0V8xptW9WLPK52ZacY6jjQpHO2LgfLdIUi3epAIaSJKczmpmE_FDHOtbWcBjEdntOEyCDEiIsBDchLqb3ir8raOBExM1DsC_H-reHZgv5YPlSEkTboxL9zhwjP1xHMnUWye2t7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=N5rjY_NLBrvE2TTtUu0zWks_9uVV7LxHcypVFB3l-2U77VanMeBlDHx6hHopsArC40PG4sltBwLIfnqHrACPMlpNXmCloHPwB_8y_hGbabTItfQ822gyJi22BiHcuuo1fDLhIl_exOXgYxnSeOmxxR4QBhMCE48pv3PqkxsuWlmOQA9VWULHjLGAc1HvvdHwwStzZ7oqdeqMbZ_0V8xptW9WLPK52ZacY6jjQpHO2LgfLdIUi3epAIaSJKczmpmE_FDHOtbWcBjEdntOEyCDEiIsBDchLqb3ir8raOBExM1DsC_H-reHZgv5YPlSEkTboxL9zhwjP1xHMnUWye2t7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج استعفا در ایران طی ۷۲ ساعت اخیر!
طی چند روز اخیر، یکی از شدیدترین موج استعفای تاریخ ایران اتفاق افتاده و پرستاران، معلمان و کارمندان به علت حقوق بسیار پایین، از کارشون استعفا دادن!
به قدری این موج استفعا شدید بوده که خیلی از بیمارستان‌ها خالی از کادر درمان شده!
خیلی از کلاس‌های درس هم دیگه معلمی برای آموزش وجود نداره و صدها نفر استعفا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=rObhVuHu4Xk9Pbc03iDNmsdF79bGtiMUduTyjhh519SJfs8VgrQWB48eeKcXlbrEBlKl5nCHW22p7oBQyLl6lL-adBZb9FoVY-OyMpEFJ1mHvznecSMkhME0fGrATDo-pENXD420PpFlw--2H9ID_99Cr81Hjc8gDA43r7td2gHdZDQlFLMg8z67cZQXuaK_GFe8oSPRXaZaRQuZrPFNo7IyHSTF6hIb0Xo_GNUSKsiuaozuCDh2ocjL5VRTlut7a73Rp-ui2ZNe53Hqkfu0AcIMQ_33SImJ5KcsKbjTfHjXHfIA94PgrXBKi3VWtnfphxqHxh0nEWAY8F5HWyvAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=rObhVuHu4Xk9Pbc03iDNmsdF79bGtiMUduTyjhh519SJfs8VgrQWB48eeKcXlbrEBlKl5nCHW22p7oBQyLl6lL-adBZb9FoVY-OyMpEFJ1mHvznecSMkhME0fGrATDo-pENXD420PpFlw--2H9ID_99Cr81Hjc8gDA43r7td2gHdZDQlFLMg8z67cZQXuaK_GFe8oSPRXaZaRQuZrPFNo7IyHSTF6hIb0Xo_GNUSKsiuaozuCDh2ocjL5VRTlut7a73Rp-ui2ZNe53Hqkfu0AcIMQ_33SImJ5KcsKbjTfHjXHfIA94PgrXBKi3VWtnfphxqHxh0nEWAY8F5HWyvAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNwXjljDlGYb-55_lCqGxWAlCL97OJPL3VJoZWzpi5f10NNRUo9s_kashw_pf1KOZ2U1JSMfKkFWZRqOWWK_srHmvXi34lZfE_xDu-o_8N0s7MS18JjAvSllCPWXv41E9WNNt8z2GZQVDubDzXEaq46-pDTyBE5_AxG0ReKHy17x98E-u_N0hHOBLw_dPx-trYQXJttiF2LR7wPlQ6mUk1v2EENQVkTnPUhwgyHHnG0Dx7pdpaS3JWdqO9LpENRjuJYyRIvoVaX6HVT3fvNfNXcyGLFcMWWJl8RfzqasBJcEeTp1yS4Icio-j3PRKcoLBmUk9GabPvO7oMFk7HucfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72478">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBS9MoZo4Y8PIa73auyXTUv4YgHnQeR2p7xky1bXzEo2MSvQVtv57CInVRc0zy4IAysILFtyCPeZw632OkpYPt-rba7fpeD9zh6yJWy3Ooxsf3jAOJ5YKD5FzXZdQG6a1Jq39vrZDZe90Yj3EtvaY2GOSaibWPNTqYdxcNbQYSGmmvBRqfkS6Ya2kfhxN_U5vG7huVYMs80iwmEOfKKdBtOhzL_BJa1hgeH8GWTNeqA2-jywr-khJToNBCDGP_ubOVKKpTxqauYihAn4fmmElKs_DEfz2fU3xhoTMo7cb4B4bKgKtDmoJeviz1xogqMpGqNpuPIdtkypo5BhDu_jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72478" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfnz4HNhCjmpCOQ3YDYodkdKKaSPx6cmFT4vIpXLBQIPbHANjAoKv4z99SaQ6wZo9ljVlN7eiyoYnnURAyQ9-HEiaPWSAKGKg9ssluGR8WjCMA5-1QN6rr9yqfpUXozB4iam7k8dB_FMni15bQSx6tcpD0iaFc5r1FVFZgqj3I1DDASCmM8ohuujdDLOi3GNXdNvk-8EXhorhE49vmDdkp8kUapbtvNmbJ4qGIy67vZrk9jSa9ZslCrTy3p6Ch5EJUGpdDyhZXVAk0b_nxPQEHGL-ijJSuW8xWSJvkRx3FordrXAOTKiwlQqoAUtKj4ZGsxc83AYwTc1ZtdzfJSeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72459" target="_blank">📅 13:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=s8x5WYYPto_Cdaynat6U_OsVnaA5q8Hvr43kAOeB3x0wSsTDDELSy1eZbrSTQ3NZBr0SGMKQisGLqx8uH7_jgj15GZV1iMvm9RAlsUJZJW-f_376VAqHeJcXhpVeFi0oO6aGsO7nj641TH73y-htViUIw1ZMLC7Hgn2lWuJdjuF9xydoFeKTNwF7qWI4K0E-thFuqB8kZgEFgI0qJAaAfzw7wrQr4fTMVHk5f6pblpM87NwIacVm9XvvgHD6cfE3wrxOKWsV5PoWSBucnu_BzJkFiU6LZ_cqZ9XLLK32ga87h2V3Pk0Tu4ko8l50ErbZ-aO-TB11RFGSqDWbVePBKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=s8x5WYYPto_Cdaynat6U_OsVnaA5q8Hvr43kAOeB3x0wSsTDDELSy1eZbrSTQ3NZBr0SGMKQisGLqx8uH7_jgj15GZV1iMvm9RAlsUJZJW-f_376VAqHeJcXhpVeFi0oO6aGsO7nj641TH73y-htViUIw1ZMLC7Hgn2lWuJdjuF9xydoFeKTNwF7qWI4K0E-thFuqB8kZgEFgI0qJAaAfzw7wrQr4fTMVHk5f6pblpM87NwIacVm9XvvgHD6cfE3wrxOKWsV5PoWSBucnu_BzJkFiU6LZ_cqZ9XLLK32ga87h2V3Pk0Tu4ko8l50ErbZ-aO-TB11RFGSqDWbVePBKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت : خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
خبرنگار : به به خوش خبر باشید دست شما درد نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72458" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1910edd949.mp4?token=riz6KHGBZ-kwEE3WUa1GgovfyfWGxmSWIqyHhvr6LeE8ksMb6EAIreGoiNwo3wWJKiAE3llkDVyW4U-EqHi4dtBfjIEMetKrLnM_UvqVnzZI0wAXYsb4T82sG76Izm_2DFpR9iC5SZ5VQRyNO62_KnbvDJ5CilK1e0DKUgi48DGj9hH1A187cuMoFvL-gKWVz4M0JI1zn7fJbXDxc5C4Flx2mWAIq3EM4_QoiBAu9ExbKU9eVVSetjoqPag2JJtQlKLOl-gUxU5kdakf9UrswRVYBHKJm84c3_5hq_1UOP4CT65jPjZHS2JwuxhRYSsEvv1ZBfsCkLgFpSM77YGgsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1910edd949.mp4?token=riz6KHGBZ-kwEE3WUa1GgovfyfWGxmSWIqyHhvr6LeE8ksMb6EAIreGoiNwo3wWJKiAE3llkDVyW4U-EqHi4dtBfjIEMetKrLnM_UvqVnzZI0wAXYsb4T82sG76Izm_2DFpR9iC5SZ5VQRyNO62_KnbvDJ5CilK1e0DKUgi48DGj9hH1A187cuMoFvL-gKWVz4M0JI1zn7fJbXDxc5C4Flx2mWAIq3EM4_QoiBAu9ExbKU9eVVSetjoqPag2JJtQlKLOl-gUxU5kdakf9UrswRVYBHKJm84c3_5hq_1UOP4CT65jPjZHS2JwuxhRYSsEvv1ZBfsCkLgFpSM77YGgsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار افراد از پنجره‌های ساختمان در حال سوختن آکادمی علوم کی‌یف، پس از اصابت پهپاد جت‌سوز روسی به آن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72457" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=ct7oSxN9mWqg2ct_V6Drp7isGGtbyl1dt35LKt8P5hG8-eDTkpXcUwQ0Db86Yiq9Lo1-y94XYX1FGID7ufduxgLpDlOIEgUrWX6gNhTB5UYxN7odea7xTAIp-m1g7iM24EG40kIBJK_QhOONOVwywtNrh-I86u0YDUpw40bjsqZuwEEAKqjqEDH92DxlLSy0Ig8aLsOpYkD_qPU5_i_SedWIBk8a9UYYtoQWKsx_oz7p26NHbZzFu22I2xPgLEtX1UMC61A4MHnK-2ESDcSo8Swq0qzLXy2zE8b6HneHcN6Abth6OOeV_6QBrAphqX-5R3hW_9t7gdPUSmFcWXi7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=ct7oSxN9mWqg2ct_V6Drp7isGGtbyl1dt35LKt8P5hG8-eDTkpXcUwQ0Db86Yiq9Lo1-y94XYX1FGID7ufduxgLpDlOIEgUrWX6gNhTB5UYxN7odea7xTAIp-m1g7iM24EG40kIBJK_QhOONOVwywtNrh-I86u0YDUpw40bjsqZuwEEAKqjqEDH92DxlLSy0Ig8aLsOpYkD_qPU5_i_SedWIBk8a9UYYtoQWKsx_oz7p26NHbZzFu22I2xPgLEtX1UMC61A4MHnK-2ESDcSo8Swq0qzLXy2zE8b6HneHcN6Abth6OOeV_6QBrAphqX-5R3hW_9t7gdPUSmFcWXi7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6eEWp90STl1m412Kb7rGQBl9pezPnyp18_B44SHBmstshIgrJ6Z3v96N3ypaW4GEyQsqQ_qtPlSspmVKG7s8cqdlTueYf1Nu_HEqvAgN0M7l4XrXiTmKbpJ6JBYSbSWtAAnqrihBpp10RmUDTdP3-jnLuq6YrA8MtGwgbOmrylA_2uG95PMiSvXugLE6tmEDQsgLfvyoaEeq6Ikx7odnuHNmP-MysnxxqLcGiyEHAhyCOCcIpkb2TJrhPZejzD_vu6_uIgdh0XwP_j2pmMXs3zPTLLoPzMjmgQ5qq0TgfWNx6iSFd8R7HwEFCO2fOf-d86Hj3IPn4bE7Kn5ncZWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJAAe7KMFmdopWB36q8kIYvePDClg-b3arAVBJdXe5FOqJrraHV08z-1KSYdpTcHfUpLfLdfOYubbpcnGQC25pTRAr4zW3KAKvAQ3euzJ11sFY2CHGOyKj50qyoWdnJJEQSDXkdLF6OdKTdtlirGvEbn11_rFbdK_0edYIDk_VymvpD7tlJ0kyqI4Up2U20uHWuB4kIKL_35bx_LFdnKFeuDXlv0QHkeuBz9UY21KVSPmEYW9A6_qFytiX9miA-euf9NV70x9zNgseq0TtjS_6Jvxmtkmv1hxdSg_0IGO2K-5rhbAE2UaRyr_3ceXq69k-TKsVI55Ru7CiQaXb7kew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=Vxff92PVGJ-knkl5mtfiEQaVV6ZQg7qWThrIpZ_MCPUVZ8bv-VfYvA6LbGiLRgua3mzumNRf41ZCEiPcSG7l1QqSTDeggiXZjM2W1WAEknRQl2XPMy_eO7vRT9uV4NhD00OVtNCT5O5FDl6BqpmiWwt1KXSlTHBjJjuK1KFVBnrTRtMv9GJ0ToQdjUglzi9nYeVyqPOxAqngT-EOKUjGHqpFQVjSAjF6lyvvrlxVvYEp9xmfAH65phk2Fh67rT7ByT6NKXK85Aq9AT1i9zO3-RjoMQW-mrNbpXv8HL-1D9nEOi_sUME8YIE9P96Rrq6P80Ma2uUF7iEOzxRfElRX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=Vxff92PVGJ-knkl5mtfiEQaVV6ZQg7qWThrIpZ_MCPUVZ8bv-VfYvA6LbGiLRgua3mzumNRf41ZCEiPcSG7l1QqSTDeggiXZjM2W1WAEknRQl2XPMy_eO7vRT9uV4NhD00OVtNCT5O5FDl6BqpmiWwt1KXSlTHBjJjuK1KFVBnrTRtMv9GJ0ToQdjUglzi9nYeVyqPOxAqngT-EOKUjGHqpFQVjSAjF6lyvvrlxVvYEp9xmfAH65phk2Fh67rT7ByT6NKXK85Aq9AT1i9zO3-RjoMQW-mrNbpXv8HL-1D9nEOi_sUME8YIE9P96Rrq6P80Ma2uUF7iEOzxRfElRX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=FPrQ-QFWfE1Z-3mJy0AjmQpNnfOCDI4MkT0lW6wJQALZpJQSWgRV95yhQh-Hj8T5-9Mg6ZpgUmqEhOKjab7OVdLW3OmvrUaCX9ecbxN6Hs7sH2c8SnEyayqkRIDcxW8dCOTROsd4S3xDSTAxGrGJ-5uJgIB1o3OL_K3rnGjlg1EvCcvUHikn0IY9YEUDZnVkMut-7yq9E5wJDGT1zKEMGYHL7pigMpNXeVfz6oHNiXLGBBzh-S68zge6KxPB2geRSpXUmj_GCEXnWmQFMEorqT8kcVbPlSPVh1wLKeqQ92LS5kK-nyF0g7Handy1kBOKlNaopkS5ysfvoW3pNwEyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=FPrQ-QFWfE1Z-3mJy0AjmQpNnfOCDI4MkT0lW6wJQALZpJQSWgRV95yhQh-Hj8T5-9Mg6ZpgUmqEhOKjab7OVdLW3OmvrUaCX9ecbxN6Hs7sH2c8SnEyayqkRIDcxW8dCOTROsd4S3xDSTAxGrGJ-5uJgIB1o3OL_K3rnGjlg1EvCcvUHikn0IY9YEUDZnVkMut-7yq9E5wJDGT1zKEMGYHL7pigMpNXeVfz6oHNiXLGBBzh-S68zge6KxPB2geRSpXUmj_GCEXnWmQFMEorqT8kcVbPlSPVh1wLKeqQ92LS5kK-nyF0g7Handy1kBOKlNaopkS5ysfvoW3pNwEyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ItKsiZKSjU3C9SVfw_6n-zBPuxAOZVPwPeJxLgmO2lqOO2McmB3rMle22bsEGzW4ohBMgwkd-I514pIHy5YI4J7AVgTccf-ecVt1auM5ViLlzLdeZw6e6oMCajtYJK-7t9OqssTVicd6Hvey9KEVHJz4jfmyEhzxJeHQPEhFV1Tsa90fDLiaPrrUIgVAfChveu7atqkzJwkV9WT4W022CTSfvmyaMt1Aq525BIZ-4OPs6w8sWSgy9exppjUv_VqUn1BPnc8nC3OnLTODKvtViBnMw3Jlg8rReHbGQst3fINyhQ4lROUU9JDDhcU-gOV2hun00v5Hmfs7DBb_6vDczhlld76eyVCxNenP8bYiSRGaFrTYsTSbbV2OEdQYuJLlWOzCo9KxhZy7ptGaVf3Z-MuImvBzWDnBxeIFH4_eB3T0CalvHkJQKEMpKtPkplBulaVRSEDwwIqoZwXQqvWR3AWVqcikk29SD_PupKVM45Swymz3inO_x79YhIehb5sdUpCreisQR809ouUV_ZCHqI0nIDrjKA4ER1oYIOgviWtgwMK4HC6Sg27pKe9N5YHRUb9L4h2kkOD_m41-C2WN1VfKrcRJVimOoyapEUGwDlXaEtM-Q-n62Qc603fGhrKB7WXHEI1zAhGEEHh0ocLv0eI97Y2c0vEFKTflA3eh5ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ItKsiZKSjU3C9SVfw_6n-zBPuxAOZVPwPeJxLgmO2lqOO2McmB3rMle22bsEGzW4ohBMgwkd-I514pIHy5YI4J7AVgTccf-ecVt1auM5ViLlzLdeZw6e6oMCajtYJK-7t9OqssTVicd6Hvey9KEVHJz4jfmyEhzxJeHQPEhFV1Tsa90fDLiaPrrUIgVAfChveu7atqkzJwkV9WT4W022CTSfvmyaMt1Aq525BIZ-4OPs6w8sWSgy9exppjUv_VqUn1BPnc8nC3OnLTODKvtViBnMw3Jlg8rReHbGQst3fINyhQ4lROUU9JDDhcU-gOV2hun00v5Hmfs7DBb_6vDczhlld76eyVCxNenP8bYiSRGaFrTYsTSbbV2OEdQYuJLlWOzCo9KxhZy7ptGaVf3Z-MuImvBzWDnBxeIFH4_eB3T0CalvHkJQKEMpKtPkplBulaVRSEDwwIqoZwXQqvWR3AWVqcikk29SD_PupKVM45Swymz3inO_x79YhIehb5sdUpCreisQR809ouUV_ZCHqI0nIDrjKA4ER1oYIOgviWtgwMK4HC6Sg27pKe9N5YHRUb9L4h2kkOD_m41-C2WN1VfKrcRJVimOoyapEUGwDlXaEtM-Q-n62Qc603fGhrKB7WXHEI1zAhGEEHh0ocLv0eI97Y2c0vEFKTflA3eh5ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bre8niuSFyDFMEGX1h0wt41zTvz0wYH9wLrgM9djq-exsQ9kc-RtTn_OFyq7GIv7V8OC2dBkgkTHrR8JpdQlFEXEwmNv1YGwYv-n8PJwcXT63s_cW5_jd6ZDzPQhexz2QnJSvUPpFLcAtUAfPh5IlbXnK8r0KsiAlJiyHo-b4fss89o2QCYafTFNYLL-7gb4wpBuHV1OWj6sAWj8uyj7-YwGfA7aNMKriPawWr1kr5eUaK_MqqR344aglHBHMcJbqfPJdBvptmaLNRIpkP8TTJ1eykSYWMjQUl191UFArOqHpRhxALU46Knz6z-ar4SmwcgMsu6dxhqlkTtTaubAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2070144954.mp4?token=WJa9ddGuqIv9gLo-UWuNEeocC4p5k5R-O8wbp9aWrjheNxpMuoS3F0IRyp0iG1iajOfxBrtZtmeQbSiO_zuHa-GXIgOcnXGzLx3WjVSXsLrZaY6NNZEJdvvM4ErsyQNMBmAjE2n0qvvPcWCT4-ABCRnYev3BNYLHh3bukleNnGLmW1qVAdfyjwWECU6RM7iB7sFjQFP1UdXfS6mLPU0vNpdAFGRv0AgI--M90_wx4GPEO2g7LOZ2Qp5xHdyVKXTGppcOrkXrjL4VnfYFzsiqQYjlfUpEOdoLH6MECkGIzz2wuSZdweRLOXtOVqcAIZMnLIrKB3BoO8y2QJCjMCtpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2070144954.mp4?token=WJa9ddGuqIv9gLo-UWuNEeocC4p5k5R-O8wbp9aWrjheNxpMuoS3F0IRyp0iG1iajOfxBrtZtmeQbSiO_zuHa-GXIgOcnXGzLx3WjVSXsLrZaY6NNZEJdvvM4ErsyQNMBmAjE2n0qvvPcWCT4-ABCRnYev3BNYLHh3bukleNnGLmW1qVAdfyjwWECU6RM7iB7sFjQFP1UdXfS6mLPU0vNpdAFGRv0AgI--M90_wx4GPEO2g7LOZ2Qp5xHdyVKXTGppcOrkXrjL4VnfYFzsiqQYjlfUpEOdoLH6MECkGIzz2wuSZdweRLOXtOVqcAIZMnLIrKB3BoO8y2QJCjMCtpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو به‌تازگی در برابر دیدگان میلیون‌ها نفر فاش کرد که باراک حسین اوباما به تأمین مالی رژیم تروریستی ایران و مرگ هزاران نفر کمک کرده است.
«در مورد هر دلاری که ایران در اختیار دارد، کاری که آن‌ها طی ۳۰ سال گذشته انجام داده‌اند این بوده که هر زمان پولی به دست آورده‌اند — چه در جریان لغو تحریم‌ها توسط اوباما، چه از طریق فروش نفت و گاز و غیره — آن پول را صرف ساخت بیمارستان برای مردم خود نکرده‌اند.»
«آن‌ها این پول را صرف دو کار می‌کنند: ساخت سلاح برای خودشان و صدور انقلاب!»
«آن‌ها این پول را صرف تأمین مالی حزب‌الله می‌کنند. صرف تأمین مالی حماس می‌کنند. صرف تأمین مالی شبه‌نظامیان شیعه در عراق می‌کنند. بله، این‌گونه آن را خرج می‌کنند. آن‌ها این پول را برای حمایت از تروریسم و توطئه‌های ترور در سراسر جهان به کار می‌گیرند!»
«[ما] مانع دسترسی آن‌ها به پولی می‌شویم که قرار است برای کشتن آمریکایی‌ها استفاده کنند.»
اوباما پول نقد و لغو تحریم‌ها را برای ایران فرستاد و آیت‌الله‌ها آن را به موشک و تروریسم تبدیل کردند.
رئیس‌جمهور ترامپ دقیقاً برعکس عمل کرد و جریان پول را قطع نمود و...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=aDgnaZudEGeatd86BgS2VpE53PvarLpIeKt49M5SU2YZNjQrU28zTQgSE-HRN2TcI0kzug3DVPet1Xvdrdt2xzfYJnnqU8X8RI9AV44qTSMX5Or7E__MbHf1GkL5p_OkJiBY3T8YPxbQwWvxt0iwcdgkfZnQ337XjFzfLT2hYPFvvgcmvx-o1MLhDG76VrIv-J_KPu8waF2gw0XXGJduICQQ24naHntzjmkdxuPZRoruwbpH5DdRtFwKKPUwjmOUcwdtwpsy-otKzG2MSOl98YoeB256j3xPhz3EH7eRHpfYoOGWiGKkv4bsvN_r5is2Qs7m51MIDlYAh5wrEAClyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=aDgnaZudEGeatd86BgS2VpE53PvarLpIeKt49M5SU2YZNjQrU28zTQgSE-HRN2TcI0kzug3DVPet1Xvdrdt2xzfYJnnqU8X8RI9AV44qTSMX5Or7E__MbHf1GkL5p_OkJiBY3T8YPxbQwWvxt0iwcdgkfZnQ337XjFzfLT2hYPFvvgcmvx-o1MLhDG76VrIv-J_KPu8waF2gw0XXGJduICQQ24naHntzjmkdxuPZRoruwbpH5DdRtFwKKPUwjmOUcwdtwpsy-otKzG2MSOl98YoeB256j3xPhz3EH7eRHpfYoOGWiGKkv4bsvN_r5is2Qs7m51MIDlYAh5wrEAClyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
مشکل اصلی در مورد ایران، «انقلاب» است؛ نه آن مقامات دولتی کت‌وشلوارپوشی که در برنامه (Meet the Press) شبکه ان‌بی‌سی ظاهر می‌شوند و در رسانه‌های آمریکا بی‌هیچ دردسری تریبون رایگان در اختیار می‌گیرند!
«بحث ما درباره آن‌ها نیست؛ کسانی که در ایران حرف آخر را می‌زنند، روحانیون شیعه تندرویی هستند که دیدگاهی آخرالزمانی نسبت به آینده دارند.»
«آن‌ها معتقدند که رسالت مذهبی‌شان این است که آغازگر وقایع پایان جهان و آخرالزمان باشند.
این واقعیت است؛ این هدفِ اعلام‌شدۀ انقلاب آن‌هاست. چنین افرادی هرگز نباید به سلاح هسته‌ای دست پیدا کنند، چرا که از آن برای باج‌گیری از جهان و کشتار مردم استفاده خواهند کرد. این ریسکی غیرقابل‌قبول است.»
ترامپ دارد کار درستی برای جهان انجام می‌دهد. او اکنون به دنبال کسب پیروزی کامل بر ایران است، زیرا این تنها راه چاره است!
بانک‌های مرتبط با ایران در حال تعطیلی هستند، ترامپ عقب‌نشینی نمی‌کند و ایران قادر به صادرات نفت نیست.
اوضاع کاملاً علیه آن‌هاست. هرگز نباید سلاح هسته‌ای داشته باشند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=btOLK38OO136SoCZbh8q56SVWpXFWYPklN9p9EK6qidw26k4fes67l7eSZyv9djrNueKzl8JyEcNpCcPOja-VT4p9YJU0C68youhx4KQiO7MfFcV5iIfQze6MhGvXZtosOww8osCpqZOzawvt_YSo1ZoPK4qu7_N5dUsPvP_Cp6AjRJ6we2_CwrhS-uUB26Y54ElawBgrC2ATbSzOnAQ0A4CjYzpUsIrPrUWE2AgImXppRYYL9ZhpETTUeNXuL245bu0jhKeVRye8_itpgv9S3p_12k4lfTnhzqbCD0hK70Zi-RVTiPOneCP9sUAy7HS245s6R1O7xcC71IpwgNjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=btOLK38OO136SoCZbh8q56SVWpXFWYPklN9p9EK6qidw26k4fes67l7eSZyv9djrNueKzl8JyEcNpCcPOja-VT4p9YJU0C68youhx4KQiO7MfFcV5iIfQze6MhGvXZtosOww8osCpqZOzawvt_YSo1ZoPK4qu7_N5dUsPvP_Cp6AjRJ6we2_CwrhS-uUB26Y54ElawBgrC2ATbSzOnAQ0A4CjYzpUsIrPrUWE2AgImXppRYYL9ZhpETTUeNXuL245bu0jhKeVRye8_itpgv9S3p_12k4lfTnhzqbCD0hK70Zi-RVTiPOneCP9sUAy7HS245s6R1O7xcC71IpwgNjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpGSNfaWMg2CyI7oUzxmJr9xO49MWMBytbYTQ1_wGhz7sm9xrhgKS8Ewi7Cgv9uUyxCY9hWOiOhC8TyF6W-S8yJk6JpsUevAnDWOb2rsDngCnDV5OVaamJ8-gMTP50FYoBh-c6sGB0_MX6oP77oNUQCk8mmvkSS7-obq84Zwc6jF4kCsT6JwUaOziw_769KED1sJEcfvkta8FeN18ljsoMQG6ScJeIUF_QoRV-To4O3btJu2O-hEzJjdflsNWhqhZ41hx_Ec-AnVAdgvGNgA3M9pF-6vAbVpy6NFfNqiHcCgLHBjh-yNjmx4y7xB64S-cKiWHKCe3XW1wLE05qvFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSBrvryIb1tc8a9PCN8qcGnlvjDX7GjrQ_tTHzWzGvC-OspMwuNVyzhkrhFw5ttc9fPAeztlv29DWr9VYCa5JZdCdp-mktbPbGPi11jzO-Rej3faS_7rBVmJZTzcQRe93yjyDHFxC6-3wQv3ltI3Qynkm0OUzRmuFFwiq7VFBQFmup821oKJ1GiOmh_PGNwnt2DcSrzw_kFe0CfikXKNJIv6qGAuy1xM8LmjyO7h4Bh-WSMAVmz-kD0EccM4TZXrLM_hMHLBcBLEh21XWe19IaVke-bKEZ48tE4Ncj-ITZXj96f5jbjmpidZZlAmZru-1Kt_JropONBz21e68sQ8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=UdCZDAItIGeiy0AP5VqGFmInMUVTZkgzKMcoyDlREHeefR_yaIpN1QNcC4fZUtQX702D9gocdaUfkETxVfeE0Y8To0rbCTfmk5wdfJ4AAu33OM4HV8FKXZVI7-OCvhcCdvylRG8RFgyU0z7IPwDFPDIW3AakOGM4cavgR5nsTWuY_0qvCQaF1_V0DUTGz3BN8EEsBiRm0P-_txfXAa-GVRquUyQPPg0XBIyQ4JvZfFQSmSSwivXHbOIzK0h4F2s9ZSDJZQzAwg3mu1GzDuQ-F3FdXA_O_3QXILKjth1ONse955BMhB9prhIFEf4sBXpI2EQuur9MXN-ZE0_v52IPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=UdCZDAItIGeiy0AP5VqGFmInMUVTZkgzKMcoyDlREHeefR_yaIpN1QNcC4fZUtQX702D9gocdaUfkETxVfeE0Y8To0rbCTfmk5wdfJ4AAu33OM4HV8FKXZVI7-OCvhcCdvylRG8RFgyU0z7IPwDFPDIW3AakOGM4cavgR5nsTWuY_0qvCQaF1_V0DUTGz3BN8EEsBiRm0P-_txfXAa-GVRquUyQPPg0XBIyQ4JvZfFQSmSSwivXHbOIzK0h4F2s9ZSDJZQzAwg3mu1GzDuQ-F3FdXA_O_3QXILKjth1ONse955BMhB9prhIFEf4sBXpI2EQuur9MXN-ZE0_v52IPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=TpCsgPjU3rRRLU09CW8ANxcOPQfWFduYICf22NT4Ze-1mWn0S-XcH3Msi3dXj5AO6zAkuBOGNPKTnOrrfLmf24_LkKt9MC9wtcdm0b6YcMrWEcI6q0C6YaFvHuIO5OA1uKeoXelgvHDj01BacuMmfuOXD-46RuEsJ7Bv6nQNY1JGJltcj2gVK7fEohbgZz9xPDPrrTYA1JpFXFLNnZuvvcKLuUUC-Zls__M1JP6udY_OnE95RxsHjm3gV6xf2t9ygIkEagoJhya7vex9OrtetbXiPiZlO0KlqR3jT1bTreg2R8TC8gukj-kzEib1SRp8DtyeYNF4OkkwM6Pnvp09_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=TpCsgPjU3rRRLU09CW8ANxcOPQfWFduYICf22NT4Ze-1mWn0S-XcH3Msi3dXj5AO6zAkuBOGNPKTnOrrfLmf24_LkKt9MC9wtcdm0b6YcMrWEcI6q0C6YaFvHuIO5OA1uKeoXelgvHDj01BacuMmfuOXD-46RuEsJ7Bv6nQNY1JGJltcj2gVK7fEohbgZz9xPDPrrTYA1JpFXFLNnZuvvcKLuUUC-Zls__M1JP6udY_OnE95RxsHjm3gV6xf2t9ygIkEagoJhya7vex9OrtetbXiPiZlO0KlqR3jT1bTreg2R8TC8gukj-kzEib1SRp8DtyeYNF4OkkwM6Pnvp09_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=QJNhAlE3AXpi-e0515f6WWpJlG7q-UufDvD7OcScqG2ueZ8wSGg8-GXDhLYVXV9oCd9TgDoOJ4iittwL-vS5KZpLdVzL-VSZ5e7YtwkwnQH7rdHRXzOGvoorEc11cDsD8EBprJQW9_mfFHdyIpOmHGGql-Erm50yaWhgAg17cSy9_XA4QQ3JMISEGB09-xl7LQT0giJetAL3lOBNMp_QgyGj66aiPr331tPvu1mw9UA8hbeOxsW4Gyi_n1TYJ54BuRTz6uTFeA6_Z3LiOyf68omdyn7N9GSeplJM-6Anoj_aoPEEk12BEp8atoA__YsiynFnBt8DwKyePExoJv5irA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=QJNhAlE3AXpi-e0515f6WWpJlG7q-UufDvD7OcScqG2ueZ8wSGg8-GXDhLYVXV9oCd9TgDoOJ4iittwL-vS5KZpLdVzL-VSZ5e7YtwkwnQH7rdHRXzOGvoorEc11cDsD8EBprJQW9_mfFHdyIpOmHGGql-Erm50yaWhgAg17cSy9_XA4QQ3JMISEGB09-xl7LQT0giJetAL3lOBNMp_QgyGj66aiPr331tPvu1mw9UA8hbeOxsW4Gyi_n1TYJ54BuRTz6uTFeA6_Z3LiOyf68omdyn7N9GSeplJM-6Anoj_aoPEEk12BEp8atoA__YsiynFnBt8DwKyePExoJv5irA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=wAHaY-Ll-zF76L4MTZmRSzUJWto95yBWj1gXntcd9OKG0hYKFlssYpgdZYW0ZtV1zkBCTF5n-PWsyDF9uKYgJUp2vKYCejrgnFrDeEPX_57jN4x7HoDzy_NnHfJgNByJnHQXkoiAZ3mpq-X35ABoaNGXcI8_EmNKBAkm72r58YhtsWqfOfKEk34GFnDpRK_ygDcBGPavzHhx-jUjSdyx_qA2C8TtENEjhm_KYneJCk8r99xeMKJyYuNvvaVXAe-Dg4opn9NdYmQdfa5Wpth3YkflgghTGwNkJQDIR3lSuoXqjueNWMRRoaywcJ2AD5eKpS9_54iHvedr6zOlOj06fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=wAHaY-Ll-zF76L4MTZmRSzUJWto95yBWj1gXntcd9OKG0hYKFlssYpgdZYW0ZtV1zkBCTF5n-PWsyDF9uKYgJUp2vKYCejrgnFrDeEPX_57jN4x7HoDzy_NnHfJgNByJnHQXkoiAZ3mpq-X35ABoaNGXcI8_EmNKBAkm72r58YhtsWqfOfKEk34GFnDpRK_ygDcBGPavzHhx-jUjSdyx_qA2C8TtENEjhm_KYneJCk8r99xeMKJyYuNvvaVXAe-Dg4opn9NdYmQdfa5Wpth3YkflgghTGwNkJQDIR3lSuoXqjueNWMRRoaywcJ2AD5eKpS9_54iHvedr6zOlOj06fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=pGAlwqeMm4VOG3WZkdBvG2cRlIXuR4WlBtA-0NvuZ-PPUZkgpJvl23TTdayUp7pewX9SnBDghr6JvPktH42s4mXIFDMF6p3xYALoT7RMAFqYaA6eg8QtZ2wvZlf9jSCN3RPRBlhpw6lbdygcRGCMLnGg6KjuP4_dscFF2v22kQL-F1vm069vBE3E_aJDRFHV2oi1Q3NppUGY-pKaih18mD4tQDNdOh3YThpCd-q2YACg8NDqFUwahnOnuqOSiYc4rMSnWKnpwnycWAsbtSuVneK7QqDx1rIeWQQBvzv9hBPH-w0MkoYfA_1e6W79QXFrI1RpN2WYKacotzKCmVGfqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=pGAlwqeMm4VOG3WZkdBvG2cRlIXuR4WlBtA-0NvuZ-PPUZkgpJvl23TTdayUp7pewX9SnBDghr6JvPktH42s4mXIFDMF6p3xYALoT7RMAFqYaA6eg8QtZ2wvZlf9jSCN3RPRBlhpw6lbdygcRGCMLnGg6KjuP4_dscFF2v22kQL-F1vm069vBE3E_aJDRFHV2oi1Q3NppUGY-pKaih18mD4tQDNdOh3YThpCd-q2YACg8NDqFUwahnOnuqOSiYc4rMSnWKnpwnycWAsbtSuVneK7QqDx1rIeWQQBvzv9hBPH-w0MkoYfA_1e6W79QXFrI1RpN2WYKacotzKCmVGfqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=l0NrQ_IobD9YLSc3GXePVBHsF1OBeZ4gH-woyaeXmfUoYl5dstvs6pkdKEq7jtfuQ_UvEYu2gu2J88X1fpmNv0Ba4sf2CvvbvuXLcW4i1Rkw_PSEKu5DCWZjY9TXF92K_c6a6MoUs5aXF-sia2mMfocLFA8hko6mE39WfcNFAOVKT7gER3MKlZElKwOTG4qG64NnKhj2OrbQARavA0T34up5IO8APW7f2nMS0uAEl0fvnx0KNuVLN0yqhBRymFizp-FzVdAfUdwpdMBIME6qJuW2tGAV3hlYSgz9jSKZrD_QbWGy_umO55n_eGUPdIa0xAAvleyNRD4kJsE2b4slPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=l0NrQ_IobD9YLSc3GXePVBHsF1OBeZ4gH-woyaeXmfUoYl5dstvs6pkdKEq7jtfuQ_UvEYu2gu2J88X1fpmNv0Ba4sf2CvvbvuXLcW4i1Rkw_PSEKu5DCWZjY9TXF92K_c6a6MoUs5aXF-sia2mMfocLFA8hko6mE39WfcNFAOVKT7gER3MKlZElKwOTG4qG64NnKhj2OrbQARavA0T34up5IO8APW7f2nMS0uAEl0fvnx0KNuVLN0yqhBRymFizp-FzVdAfUdwpdMBIME6qJuW2tGAV3hlYSgz9jSKZrD_QbWGy_umO55n_eGUPdIa0xAAvleyNRD4kJsE2b4slPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbF-AsX5iuJrjnoLqrhZ_Of9CMSmb3-CAGKium8F2aol0fuMOXi_a0WVFRj3LiPTlwXX9_jacf1P09qGtmkVYr2s5p42uR5KwpQjCIFPHI1MbeP_Swb4warCb45lm4jgZOLIJWScVGptDeLkML2zrmKtjc_OcPAwRFfjVBQRYecZJ2OEmtmeBLOpw9YnENSsXB8ASXLak8IAuhCGTHhZpwTIxdaf6NUOWPmzZRprSgOljymqNn-lVADDLfKKXiSPQDM9iDnp_0t2chbQm6s-CSdYQA6ghlIU0L0ALO3_TpMOxyw_ZOVZNjHXHudtc3p2wkA9PSPvAJTmFNJFT_a0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOR1PbtLUjOiKHNTMDWv3YOPqXnyDl-_CDhTLamkMJ334Ohl0elJl__JRE4rQAZTzl1_2pCM-Lyf9K7W7wAVmOvR4Inr5Oq_yET0EggIDZCIhR4a4jiMsNpgYa64TJgHMyWmiD_WzsJurXRtUwAzgDzfzrGC9AJKE2bowPVTKzv0FnGYYQpnTEPEkR5P2tmc34sJFq3vbBhNcc1nmQJw9DiLA3e7VmfpXJ3-9tjLJuSLKL1KBrNxcV99iph-Gr0S4j-ku7eUwEDYnmAnrk6x2Nwk9QmXWRERd-BxCOIkCbhstk-PqpEn_tvJkXpE65YeXgRxP3NFPPZKpoxIlcEwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTgHUJzgVgaXF5pQkIM5Yd40bR8vjIHLHgEHyV4I0MartkbQ3Jp2WL4cxHOoKRflyNad1P0IO9KDmXZ3u1GqpSMIc_veLfLMB5X3T41TSRsldSlvAH_kPom9gi9RbMLrnUu3tZyS4LiXYYQFdvthQnPlancOcUKg4KQKon3D6Qcw5Z28wYW7LgHDyqL5I2zvVNX261V-M-In64f2N678UfOt_57e8LiccEVeZy3VZe6rGPO38ad4gZthXJZMb8r2ttvbzreVz2eKi9FEIc87XkkBDUexRSlY6u6JhsgJcg8Tc4PG9GX4U3oyAhR_IbrGkufZN7u4kjGFd9k-xktWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=k5clv0zL-wkUTkTBAtJpq2Fm55lGN7fXFMV4qNzaSxdvLvgmIZEl6c4Sk1nESFzGkH-dBXUzTJ8jSOCFkAmkq3m43Scp3gsi_AjiLEZ_rb0QfYP-m61kYXrbp4SocmU1O8bjHOYtk5ouchiSBJ4O4A17LsqbcAEavsmMsk7xwo3oVrePVwY51uMVYfOCVjOHaXDGLzQLKykFjOlZT4ItWwCaaMRnlIj80TLpZhPgz_3QwrDwBMGhvk5b0fWs6EjmHfxhhhGkgREThQcZYJlDhna8qJbk_CDGzIO7KgWl9zWSdLjqNIKuQjYvQIARW3mKpYxqLOaSzzORPtA_B5MEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=k5clv0zL-wkUTkTBAtJpq2Fm55lGN7fXFMV4qNzaSxdvLvgmIZEl6c4Sk1nESFzGkH-dBXUzTJ8jSOCFkAmkq3m43Scp3gsi_AjiLEZ_rb0QfYP-m61kYXrbp4SocmU1O8bjHOYtk5ouchiSBJ4O4A17LsqbcAEavsmMsk7xwo3oVrePVwY51uMVYfOCVjOHaXDGLzQLKykFjOlZT4ItWwCaaMRnlIj80TLpZhPgz_3QwrDwBMGhvk5b0fWs6EjmHfxhhhGkgREThQcZYJlDhna8qJbk_CDGzIO7KgWl9zWSdLjqNIKuQjYvQIARW3mKpYxqLOaSzzORPtA_B5MEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCn36uzmVPaq9zPK5B_coWbjYR2jBqT6kc-UKvbhmzfx3GNtmBvPW5Qjq7fqIjPqpQP6trpSpQoeEnfHdF57hk6Ijmq0h37WD6qeQ9lU8FFSbJPpGdw4TnT58zqUJEUTY7cfke4-QUVh7NfhswitTI1_SO9HqzfxFJq25a4cFFvIACzrzCULW7t2pFmrY2_5AY2XXVaH_zRst4yPxkz2TpoBf4Vv0xP0aHMkw15uu4ni2WAeSwD1zKKLlaHrbEEclPZM1UR5HeXNVS7bocXhRSD-GKjW9VtXvWYThDvFPueVy5DHs1YIMoQNEkPKlPRRFsc_WXJ_QUELZJ9ljGHFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjsnyqq_FC7hDd0zXNT2i7ac5ZLtnABOBxVdTcLrODqfPNOBxgMnxM3NL_iuD4XPy1t0sqqRrEA6_rtYEuWGQvfG2hHS6MNMDA_5c6ZzQ8j84B7zUkyhjY0hSOh2Vc1zro2vLpjFAOMaY7jtn6OHNSpKy9vKkGF7kEgxflxg-of3hDUhZNh3MJxUZeHA16ixj3sHx79r8nlcTUFP3BTFDLC1leIuYXZo9FcaSMjf2uk_YiBr9-izrpZJs0pzIaFtCiYzuUIJcbBSSjA5hfjrE1NmhhiF9XcyVX5EKRLsPZBl16yxhyISLMUfg_H5nMYuhG2MMopNu_bos5sD17ktpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaXoU27fLQq8L4DqunSzSxzRc945_r9qscA4lV_e9dCvOGx2b0k0LP2gGDbTvsYPTxaH6_vL_tU9j1dmL7BkFbTw0Cic7koR3EZ3VwYllGbVkLqgooYfkPeHVoDrUJy4vLSwHhxvrkrRKD5Piymij8eNitBJcwTXsFNt5ZkOj5tOKvS4rlcTkttv0vld3Zj8s13ouDWbb0ZSSq33-7uVaIXtTORRs8CJKovSbRS4FwQAik0K4TpctsFDIK5rQAjQJ8qNaT5ewoSPvgnCC-4U3A6LuR74Y7LBp3qzn2FUVPTjBkA9aBSm42Z6_x0ibbLcmEter0Sls5xNbZd75jlDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=JwrPF9rR6g3tzDa4qXFzcnzTdO-4p5JqzH1cDDrTP2hVBYHcdA2jaqiaSKGFWwDJeihCLIktowVhuB065seDJJNYIm-rIlen1Z-KRgSYHyOyhfiwatuwIt--QGFPQXaX5m-i9NKaGNNV_zEKkstdY_p2u_bRPVgmhJIBret-XriwGnQjrgTSBX9BSsSemKB6N5gYpPDdXJz8f4YWNHJWkt_VuKDGv2psMktb19v61gxiejVYqdGeuoZ1StcTBf_fw-ZcEzQldObtnip1Smgq9Rpg7vcCOhuVFuwNWJ8YGeYx0KNve_1CFSM_otYUGfkC0ILxIrfefDE1tDO6yG1LVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=JwrPF9rR6g3tzDa4qXFzcnzTdO-4p5JqzH1cDDrTP2hVBYHcdA2jaqiaSKGFWwDJeihCLIktowVhuB065seDJJNYIm-rIlen1Z-KRgSYHyOyhfiwatuwIt--QGFPQXaX5m-i9NKaGNNV_zEKkstdY_p2u_bRPVgmhJIBret-XriwGnQjrgTSBX9BSsSemKB6N5gYpPDdXJz8f4YWNHJWkt_VuKDGv2psMktb19v61gxiejVYqdGeuoZ1StcTBf_fw-ZcEzQldObtnip1Smgq9Rpg7vcCOhuVFuwNWJ8YGeYx0KNve_1CFSM_otYUGfkC0ILxIrfefDE1tDO6yG1LVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=D8RcBDqL1OQB-TqHmEfUH9u-k_FSl-g25-BZI1DoUvnRkGa5pgdWk-4WQTvZfrkpT4sR9jWo_xX9iAPoh-1xT06ynYiH5BRdprBlibe-d48MTt9EXYlupISbExCW3E8rejLhNN6z1S34-EquL9pfPZI9Iwoab78wcq_xHfpp8s0jd-rqmPvkDoJqQL77hsbvZ2m3UwHkOxhDzmgXeqQO7x3iM9l9rs_i5gYx7BlpwZkl9cH9Yt1YzL6m6R6i58SlNMdadTEZhksE6N63_V6DyvmBdQhu9ijRHo7PfjTzueXjy94--HI8jzKwxpRITbSUxxKpx0whs-J4DfBgBolFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=D8RcBDqL1OQB-TqHmEfUH9u-k_FSl-g25-BZI1DoUvnRkGa5pgdWk-4WQTvZfrkpT4sR9jWo_xX9iAPoh-1xT06ynYiH5BRdprBlibe-d48MTt9EXYlupISbExCW3E8rejLhNN6z1S34-EquL9pfPZI9Iwoab78wcq_xHfpp8s0jd-rqmPvkDoJqQL77hsbvZ2m3UwHkOxhDzmgXeqQO7x3iM9l9rs_i5gYx7BlpwZkl9cH9Yt1YzL6m6R6i58SlNMdadTEZhksE6N63_V6DyvmBdQhu9ijRHo7PfjTzueXjy94--HI8jzKwxpRITbSUxxKpx0whs-J4DfBgBolFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=PE59EKGgY4j8xm3DgjXXYAcKzR5YacLVuNcFuofYinYmu1IKSlIG-GnbPs94dMOHvqGEgur9FoX-QDI-fcJhCOaSbySCXTLrDKs-MGPhsULKZQwEBTxwsXoyPklBRdMcj0tn0ALh9R9MLQIr6ByCGEvn1LZxx_g7CBuU9R4YC_fbZDJG2RRT4zugemGl1GZyXdtfTM4Ll-OOFiVcMZRFc9XiEdeFwixi6myJ7SLsdU_0nKfBDGeGtl_Jm4e3hswgSY-388qEYt2u2dF2vTj03_dm-HMQZ9DsJ-AKc48qfrC4qZj1E7p6dZUEGDA16Y2Whqa7g0rJG6-iJ64Ahn8prQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=PE59EKGgY4j8xm3DgjXXYAcKzR5YacLVuNcFuofYinYmu1IKSlIG-GnbPs94dMOHvqGEgur9FoX-QDI-fcJhCOaSbySCXTLrDKs-MGPhsULKZQwEBTxwsXoyPklBRdMcj0tn0ALh9R9MLQIr6ByCGEvn1LZxx_g7CBuU9R4YC_fbZDJG2RRT4zugemGl1GZyXdtfTM4Ll-OOFiVcMZRFc9XiEdeFwixi6myJ7SLsdU_0nKfBDGeGtl_Jm4e3hswgSY-388qEYt2u2dF2vTj03_dm-HMQZ9DsJ-AKc48qfrC4qZj1E7p6dZUEGDA16Y2Whqa7g0rJG6-iJ64Ahn8prQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=R_2loY__dYYa6vlTFE0jXU2cSMWOoWbnTNKTL2oI4CCeiRHCnK4KCLH_APZxfCXh_jivC0_AMwedHfUqi2-ubu0xeVxdiXyCMfz9hFGPmJciuGBsqjFlU7waKEb0u000-HNB83Xn8ZaMwjGR6SXUu-3Nnov8di_YAOMKNqWqi4WnvPN4Day8UAegh90LmZnIfsz4uwA8A6-KiHgbBniBDn1D1VDErQWijKkfgc7OxPPO70hoF92B0AZqDNB2iAF3Cz-PonEsrY_9Gq1aLzE6G-ImsJC-GwFt2eJ4RnWyyMNymI4xnJs7l9MQ1mm4wr_NqL8L7QMrvkfIAcy63ihAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=R_2loY__dYYa6vlTFE0jXU2cSMWOoWbnTNKTL2oI4CCeiRHCnK4KCLH_APZxfCXh_jivC0_AMwedHfUqi2-ubu0xeVxdiXyCMfz9hFGPmJciuGBsqjFlU7waKEb0u000-HNB83Xn8ZaMwjGR6SXUu-3Nnov8di_YAOMKNqWqi4WnvPN4Day8UAegh90LmZnIfsz4uwA8A6-KiHgbBniBDn1D1VDErQWijKkfgc7OxPPO70hoF92B0AZqDNB2iAF3Cz-PonEsrY_9Gq1aLzE6G-ImsJC-GwFt2eJ4RnWyyMNymI4xnJs7l9MQ1mm4wr_NqL8L7QMrvkfIAcy63ihAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=u6fWXAlDRdBcVi7bd1kvgJYSdOzDw_6FnpwkfwjMnhYlIXMexv7AOSZfQnIVtsDCRDAqSd9nGjnnbXFUrDV-YpdrfKYlajWVhoeltapbTm8G4xnKD49U8q05K3UHAFihVogZLQbC7S9nicixMnY-J4uiXO9bpgX2P9pnA2-CGjDWCWkGXOA8niOXoZPXAsS4TUHLtDHtR_UmYyt-3u57p6dV0-wwDAQ1hrY0-7L5n3KurrgctSGFFUWLTGeRPiH2qQV3HmVP2iUL9MK_r_i8tBRMetDZnRPkpch90e1uuagvIffqt004Cxvi_pcMikqWuI3RW1qm8OtAWidVtxEhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=u6fWXAlDRdBcVi7bd1kvgJYSdOzDw_6FnpwkfwjMnhYlIXMexv7AOSZfQnIVtsDCRDAqSd9nGjnnbXFUrDV-YpdrfKYlajWVhoeltapbTm8G4xnKD49U8q05K3UHAFihVogZLQbC7S9nicixMnY-J4uiXO9bpgX2P9pnA2-CGjDWCWkGXOA8niOXoZPXAsS4TUHLtDHtR_UmYyt-3u57p6dV0-wwDAQ1hrY0-7L5n3KurrgctSGFFUWLTGeRPiH2qQV3HmVP2iUL9MK_r_i8tBRMetDZnRPkpch90e1uuagvIffqt004Cxvi_pcMikqWuI3RW1qm8OtAWidVtxEhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=v_W5YlrU_fREe7ECx90kfaEaR1MWoW4RVkM__-FKbIhqVO9F4Rf0ZQrVa4XladVVL7Lw0s6c5cajvkOKtZEmebHoYU1zqpsll2q5zh6_K4f3Xc9eNSEtF8c7p5bA1kNrgyL1hQjxNmPm0s3MjccO2VcNhlFOyjglgzK7uUqNpE2Bi5zlKxVSQkJ-HWt8Q95Udo_AF-HDzD990_9jB3_SqHVyn2nFFViqPO91Y3OLHPohA8yFDzKaIEWGLtDav9n2qx0O_vTvLbvmfk-iCdT8cLes0k2ae_9r3tOG9yxoHbn8m0tJMb5xhLu24JNwojdpoX5j7uYGRF5ftTWqa_Uvvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=v_W5YlrU_fREe7ECx90kfaEaR1MWoW4RVkM__-FKbIhqVO9F4Rf0ZQrVa4XladVVL7Lw0s6c5cajvkOKtZEmebHoYU1zqpsll2q5zh6_K4f3Xc9eNSEtF8c7p5bA1kNrgyL1hQjxNmPm0s3MjccO2VcNhlFOyjglgzK7uUqNpE2Bi5zlKxVSQkJ-HWt8Q95Udo_AF-HDzD990_9jB3_SqHVyn2nFFViqPO91Y3OLHPohA8yFDzKaIEWGLtDav9n2qx0O_vTvLbvmfk-iCdT8cLes0k2ae_9r3tOG9yxoHbn8m0tJMb5xhLu24JNwojdpoX5j7uYGRF5ftTWqa_Uvvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=CepKLIIAL-_0p26WlbpRgWDHuCOiqRGqa1WMykY5qvBJbX48xWzWyAHu1driI4vFLof-LVxZBvAjYFwyqC7ojG67-JvnymLlTObmzbXY2r_xoCTucCR7Yz1it3f1u_36MCOHxlP_8jfR4OhyVpfZD2PFnjk5Bi3eafcy-BYGWJqTKhpG4-jBTu57m-pzxNEBzFfYB_YmpuDi8xRgayLQBk8MOVINA2s1exYP6f6NN0bWWcnr7JRl0JU_eO0Q0pWRDiiE6DxRxCHCSgFIArtB8PJ3bYhlKj0cR1-P-v-XtdrE52FTRNcLNdTMXyc9RMAl9tZDFjrv0pf216HxVMtUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=CepKLIIAL-_0p26WlbpRgWDHuCOiqRGqa1WMykY5qvBJbX48xWzWyAHu1driI4vFLof-LVxZBvAjYFwyqC7ojG67-JvnymLlTObmzbXY2r_xoCTucCR7Yz1it3f1u_36MCOHxlP_8jfR4OhyVpfZD2PFnjk5Bi3eafcy-BYGWJqTKhpG4-jBTu57m-pzxNEBzFfYB_YmpuDi8xRgayLQBk8MOVINA2s1exYP6f6NN0bWWcnr7JRl0JU_eO0Q0pWRDiiE6DxRxCHCSgFIArtB8PJ3bYhlKj0cR1-P-v-XtdrE52FTRNcLNdTMXyc9RMAl9tZDFjrv0pf216HxVMtUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=VJe_abFtIRjkQCp-U_mXM-7cogz_V5K9Gb8AoanvNs5Aep9nqf85Cw9ZJSrAH0v0W5I8r__pzEXYAYTxcPcwdQWEBeQRuFw4lxRxz-FJXuYOkrB47Hytk71eW4hPM5DT1B4uZskYIIw3kqtcWZGrtvFdvExFaUk80omaBcriv7NFRb--Itswu_zZGiUnU_b5VACHy1NQbUc6SE03x042V0eRlr8fbBBDy9rFaHPw_AUY8vrNGLbblrKTSeN1t0X7cubr9NOxBFwf95SJF5UYfbizhAYDaXYGx6sLYY_tPuAEzi54XbC7kz9J64za5Ohc4zqa4OzLa4fK_lFnR_Ptdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=VJe_abFtIRjkQCp-U_mXM-7cogz_V5K9Gb8AoanvNs5Aep9nqf85Cw9ZJSrAH0v0W5I8r__pzEXYAYTxcPcwdQWEBeQRuFw4lxRxz-FJXuYOkrB47Hytk71eW4hPM5DT1B4uZskYIIw3kqtcWZGrtvFdvExFaUk80omaBcriv7NFRb--Itswu_zZGiUnU_b5VACHy1NQbUc6SE03x042V0eRlr8fbBBDy9rFaHPw_AUY8vrNGLbblrKTSeN1t0X7cubr9NOxBFwf95SJF5UYfbizhAYDaXYGx6sLYY_tPuAEzi54XbC7kz9J64za5Ohc4zqa4OzLa4fK_lFnR_Ptdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3m9hBjh1SJawBNixI4FJc-cD2chkrQqzfXjjsnuRTuitUSpQwasexhum1zdAu5gGECeIl-LRVsOyHsgpmTIEF7tsKxmODSgguZ8wRrqRFOv1SmiyPSWHcULYs3PMvtz-7hCsgJgMt3bWuJayjYqIXOE06SiXpoLcU53yJRJFr_S21GaQYjiLPTjkwlogX1hiL9OE-nb7Jy1XQVp6vlUfG7PQSi5RVv63a4c8R5Sdcbplc_kJs_ao2FhHeXOOLtCU_KIvq-UpKE2vsjW_TnnqkApCcfFnASShdbDClRNkHFgI4puXF44XdNVhoA74Yo1L_B492-3R0fJvZO7MbzNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=wB8qxc1-cSiy4koDAFVfrGkhM1yA27Pa2AaPJGajRWiUg1GrTRnKZ0O6dvesmRj8cxt2mpwFn2WNBKjKfAkDaPkdEqbbpKJOE0tFJJPP-mQOxzrQdQHJnPdVzJ5fj-c0Z2_Mgw_kCyHqW4iM8sRunT1soQ_EaxdqtsxalodMfCuOn_Sn9WLiKIzV5EIRrpCG9jUXSV4HwADRXK5YIj6bvu8zAVCnqRj1ZGCFdwXqI0ES5cxaoLLFfEAcwDMkAl2jjv2_R-_q32TCsPG_gpajBSoBiVlvFTfc2DDT66U7TywVu51l09Z01rP_490Ek9Wgq29p6PyRHMrueeF0MUHnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=wB8qxc1-cSiy4koDAFVfrGkhM1yA27Pa2AaPJGajRWiUg1GrTRnKZ0O6dvesmRj8cxt2mpwFn2WNBKjKfAkDaPkdEqbbpKJOE0tFJJPP-mQOxzrQdQHJnPdVzJ5fj-c0Z2_Mgw_kCyHqW4iM8sRunT1soQ_EaxdqtsxalodMfCuOn_Sn9WLiKIzV5EIRrpCG9jUXSV4HwADRXK5YIj6bvu8zAVCnqRj1ZGCFdwXqI0ES5cxaoLLFfEAcwDMkAl2jjv2_R-_q32TCsPG_gpajBSoBiVlvFTfc2DDT66U7TywVu51l09Z01rP_490Ek9Wgq29p6PyRHMrueeF0MUHnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhuF3vtamG8vajb-EZqP6G0I5Ur1O-Ii7msLAYd_XxYYP1chLGQxfa6T03fVz5PFfRL1DAkdgFFVCjL_vd24ADjhFm5gdHPPgmpxnr7EAQ4LOejwH7vOai8G_vRH9vcG5i6BwejmGdF6xP0d4glUtknMEPz15LlK8EXS50tB6nX_peqiWdaBGJV3RMJ79j-RpFnfEzPTtA9UagIrBJvil0L_c5OkKiPtBkoqCMnEf-HdTtE96-2POOTlR8VwkW9xQ3Qz_gGlJ9X5deW9Q2EPCUJlofZ0w3_LVEmpdFsv9R4VMtIevfACq9-pUv4QSomuLy4LqgfCJAr9tRG1HINs9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIkVIn3m52dOYmamQ_-xtLTeVuOgQihL9cXkZA_Wc2PBXpu1x4LTFJJ488yanASWrx4XA0UKd9d2jSYCAfbZreqg1wLrrE--1mTR-dPtZuDzBRAmJQ-Mma-vQIvB3uMHMYDcVnpwQy-S11np15xqreUjiJ7EPiD9WDiD-PTidNtj9UUgBCGPRgtUqzWFrgFR5PN8waq6RNSdKKzpZbBuEHNrB-piXlmc3A5sN-JTEj01no_Vo5yoEXtLDJ4KMIcUpXEdKg5F7QLPb1KZpG4CJ7ehcaA5PFS9jw_GLDbsFWMlDbPnoH7LC-_Q1AbRBVIuGPNVv2xhzmrj3FTTdnC49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=nXOWLy8OSwo1ta9ATTN-onzboh5QmwJZZQvsyYJjVEicHm9kMy2mIllTrlTYqlOZ_VmImofy1tO-KXCEZwypXiI32FaqxZAtOouuswX-Xbjs-x-agGAL0Mfw7-Lf_N28GlOX0A4Ng8aJoZm_9zb5HS6kC0mLf-vcQTUG9k1xktoMgi9Cn1hmaXNjfmdPGrKd_b_efH1DSxTqR0bQ7yg0OaZvWSMUr0PPIwXzFKeBgPo-jwwog39wHGbC34mlLgAMiAtQ79F1OOzSz_p6SSI-AIFHi5zQWjHqvyKiSAyLXveGEhwtozqyeHiHzHxsVS3NeSH6O5AidNw-i5fro6OGYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=nXOWLy8OSwo1ta9ATTN-onzboh5QmwJZZQvsyYJjVEicHm9kMy2mIllTrlTYqlOZ_VmImofy1tO-KXCEZwypXiI32FaqxZAtOouuswX-Xbjs-x-agGAL0Mfw7-Lf_N28GlOX0A4Ng8aJoZm_9zb5HS6kC0mLf-vcQTUG9k1xktoMgi9Cn1hmaXNjfmdPGrKd_b_efH1DSxTqR0bQ7yg0OaZvWSMUr0PPIwXzFKeBgPo-jwwog39wHGbC34mlLgAMiAtQ79F1OOzSz_p6SSI-AIFHi5zQWjHqvyKiSAyLXveGEhwtozqyeHiHzHxsVS3NeSH6O5AidNw-i5fro6OGYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=gi63cdJ8BE_BFS1g6M27RZw7MjgsSP9fvCWsCITG28GE2ap11D7gVUVf52O-PAkEHfr94EvMMWHChIM235MZEhNS1dFsV11TrwO34mQ2ZxB4wXPfgKQ982f1ne5g4p8AZxeBpkCyNT_yK0LEZzTKPYbwBUpA8Fr78B2bUkj9DnYntuA_IjL7jqZTMJUIdAU2TBNrQvjE1yQNukCcfy-IMOprt3sIxy8PceyfbyTySMxaY695nVDckPwcRsBmd8QOSIc__AvqbSW2BKHZtvbybWqnmn243gqP7yjT4LTByusAR_eh61aPleX40cUtAfW0Vj9986nDjIUbMO4sLCyeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=gi63cdJ8BE_BFS1g6M27RZw7MjgsSP9fvCWsCITG28GE2ap11D7gVUVf52O-PAkEHfr94EvMMWHChIM235MZEhNS1dFsV11TrwO34mQ2ZxB4wXPfgKQ982f1ne5g4p8AZxeBpkCyNT_yK0LEZzTKPYbwBUpA8Fr78B2bUkj9DnYntuA_IjL7jqZTMJUIdAU2TBNrQvjE1yQNukCcfy-IMOprt3sIxy8PceyfbyTySMxaY695nVDckPwcRsBmd8QOSIc__AvqbSW2BKHZtvbybWqnmn243gqP7yjT4LTByusAR_eh61aPleX40cUtAfW0Vj9986nDjIUbMO4sLCyeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
