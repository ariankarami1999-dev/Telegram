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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 194K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=QIgc3Gl5pSYv13LuXvt97UJUNlPa_8RKnH6U_jFkBua08r6TS66YuEXEIoYCNI2lvA5795mOX5dtPpRdzjTCEKeZfREoVf45TvMhAe0MNvJYpGcqHg-YFJecc9noFEIH57NHhKMAaTX6g-T7H6whH8IsLqYFaOoJG4T4ZOw58nNO9_H__mLUh7NqcQmTWad9pujZ0yLP_jgRdSIiyDoUZFVxrk66k2UYKG582EEq7ChF-vsgGTYXKEn463jUc1YO_23kN0lYwwdFOXgg2hm0gBMUGdSlfqytPkYmAc34i6iBCzlP5Pg9bz7bHVNX77AM5bDwCnyjttwlZmd9AWEBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=QIgc3Gl5pSYv13LuXvt97UJUNlPa_8RKnH6U_jFkBua08r6TS66YuEXEIoYCNI2lvA5795mOX5dtPpRdzjTCEKeZfREoVf45TvMhAe0MNvJYpGcqHg-YFJecc9noFEIH57NHhKMAaTX6g-T7H6whH8IsLqYFaOoJG4T4ZOw58nNO9_H__mLUh7NqcQmTWad9pujZ0yLP_jgRdSIiyDoUZFVxrk66k2UYKG582EEq7ChF-vsgGTYXKEn463jUc1YO_23kN0lYwwdFOXgg2hm0gBMUGdSlfqytPkYmAc34i6iBCzlP5Pg9bz7bHVNX77AM5bDwCnyjttwlZmd9AWEBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBWoiH_M2a3Tfg1-YBWd4syIFQ6x3TCb31v6zP8DTmMLKsKL_Ka0zOyt6xpZovbbhaam_fTdQCFjSEVeLihFEbgIs-ltRfm7ARhp0SSr27I0dPY0tGNSj9K1eqs0aedPZ_ktecfB4yZ72OizeoqXddiujNuxzJ__QDoPfiBXCECdxfjXM9LdBkGFqO76gQzXaNjU-gTXwvtE7SdYmODbYAzUkWAeDihbB8HBkGmkyLQDHj08mMYOFHw4jHp60nEXSN8tgHRrsqsAp5-RkW_5hGHEeg8cHA_ilpeHsuB18TYqvLywMRY9C2FgN7D-lomkmBUVM8Ashfr1Q2eguHlQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF-NTGkSoqIiwHLoxY5lv_M4Sv8NIcSMgIYa2Wxz8MbtH5BndN2Qtd6rKdtXcdrLljDKCm9FaSINN2v7D0ME3gFqO1dw54End8GJ0Q9Nvo3-gjMJv1sW9oFdrVZD1sCwBlZ9fRcTp62T1G60mdXbtkSb4dDavM4vwQTyFBKXeauYH-QSDwhv4PhA7suupjZ7DvsZPGNY3GgfN2oG_D6GYEPfYoqvjdS-UzqQgvGnamQmoWfGInsaZvdABZDeRZILhT4lEK1Ewnayt0l0zORZwctI2nHp7UP1MaQofs976ugIgvMS7AFBwUWjkaBD0dw9oQ7nm0vmhHYmAejdQp_WQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=sDIT5-cFQyel0Bm271k48XQ7Dx26vvd3HldxdQRjNGSCnLBTtxTaKZKLvjqqoB_MPjW3OBACjBd_Qv-YtRapl05E3DbU2_h3kpsoEXimKUdVDHRQW8tmTqH8OX5r4l22YLiA_ddvDLrBCPyKwTFKNX19DBBrSMlesIyc7wEqG-vmkEOa25i8TZwjB0pEHfGvXeXAPuUNV_1_C7zCrqRSfdwELMh9rMYSYp5dsV0gSo5PNGw_Ar-gzZmWAA7cv9_NeIxwDHjAkHUJITJMBAoNyrfmH5YZ4J1VD_NtoBAw0a2XV4nWSjsKvW-n8TZr1JOcBMar2sp192yJwx4V4KILHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=sDIT5-cFQyel0Bm271k48XQ7Dx26vvd3HldxdQRjNGSCnLBTtxTaKZKLvjqqoB_MPjW3OBACjBd_Qv-YtRapl05E3DbU2_h3kpsoEXimKUdVDHRQW8tmTqH8OX5r4l22YLiA_ddvDLrBCPyKwTFKNX19DBBrSMlesIyc7wEqG-vmkEOa25i8TZwjB0pEHfGvXeXAPuUNV_1_C7zCrqRSfdwELMh9rMYSYp5dsV0gSo5PNGw_Ar-gzZmWAA7cv9_NeIxwDHjAkHUJITJMBAoNyrfmH5YZ4J1VD_NtoBAw0a2XV4nWSjsKvW-n8TZr1JOcBMar2sp192yJwx4V4KILHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au4AMouTjHZ24iz2vsg1UtCXHSmIVhFq3gRvOFKGP3vK_LE6TMKhdTCUf3yqxhfPUaa-ELaFcdQF1gdAvR7Cfz5fxWPI9b09al_o0EVVz5UMWl4nuFNwQCVglDU_ORRjGYGnifdh1AK_diNMpkHDECP1u2VOPrdAZG6GHAQa8PLeYB8D55bK6lGvr-tGJN9b7MF0JinxLoPMHaBiHgLTp9_leY2IGlO61s5yraDwrieWx3AJR1wzfwme0TgA2DX_7vZ37QzGBupEc5YEMiXmpucHutRJ_BkQ6NL5adYQxVU5DVoSImqqGuoobDSZBDSRioKVA06xNzTwj15-fFJj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYpHLO-yAwtIhIUFUbUe2GZkQwoAupbym5_pwAtsHmFEPyMU0zIqwk69Ck7mGlbvs___hmXLNcyEX3rrZgeIjJPzFgsnWkajOnNtwNXnUzW_aoPkx-EDcFn4pdbNPLXp6HFqgyMX2S3VEx1Rs7aHQimtKM6eg8QmQUr1JTn5zFHbADZVj681usel4U_q9mHL9UX4NGhsZK3SlLYsgABuLujNhc6hRLkrFCqr6coR8ahIzrF3iSaf-WPkFrgsXlh-MCwew4TiEU3ZwrGFsubHztAvvypxGQe-YH5Ytlf9Paq_GG6ksViD_F8ClFastev9XE-NMygaY7kogn1F296pgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHN-axy_0M-fYRbHglWa6AGJoKfJWo4p4txMru6biCUWeEiOGMZWXGNor2jVV-oJv9sTw8wNDQMSJj4FZ-OttPNJvWnz8SwBgIbjZZpP8ocEfwkkQ-VeXeJuO5J4pNNTJ3oyahRibDGIt3Miqhzr1fW2Xdrmv192H6vJNeZeQSywgesxGBZ9DbIoEZQQuytYWrvT2IA2DP_Qaj4AWxSF8Au1D-YjTAYF-QZebofjxp0k5wSlduRjDfp9vIRf1DI0UiVdgwJDmUcSODv3H_E9Bxo1kS5G8TlZNbekqvSb6pyEF71lfozTzu1tTDdbWDuuLU7ifhj1bwtZo1b8NTyWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMGFHSHin1CWgMh90X7WZ2gopoYZeEMuQDot-9uKTRYm6EvHVBrFwmllr5cl5W6cpxka87sJa1QDzBlSROhZm-OBA3pf2Fospc_BxjRgw3XzGRukij2s7XB3XPz-BkvcUuvm1e1MQ96S8rO4cNxXFpPE05LYBS9syYX7yz8uZDaNSsDMJYImRerGJm3kmA22BAxH9zFqxXwIaf8Z6JZI4ZKdJpbtynaZgW9RYQgXP4VK8IWrx8t_nHPsgWta4OGEJiIoyFfsULOpAPGQkIq3KyGx1DUu3qInUk5kkn__r9pIpOLz9IP-74CMfY7QonUVSmAnfCbksVOGQY9BcjktEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEydeuJz_lPL6REKt6uG13r4OgVZ4WWn2JKgxhRfGCgZHnHP-63QGa5BC-1aTUl2HOYy9Me_lucUwW3C6xo2sNW4ioSTj9phQmQ0o_uVCU6AqrSlUIDi8Y_aM99S5VqXbIsojaFc8GtVWWa5XXO5VfozXBKw7d39fGZ-92hjN0pHy2PJezWd8kq7Xtc-yGLrpWm8X-mgwOqs8N7dHperln7-LVfblooEpU-Rlxq3T_PI1jGETR_pxezyt7uyei1z0CIgXnVkhXTK47_cdirJl96MMLs6c24BeqTmW7YRgeEEtcnxZsR5Id5FZOhxwqsTJJFJAnh_TvzATxKDsv4KkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEouIJbfPNLRVsoAiKGSUYyHBOyK1EXsq_nBT4rC4EJn_2quDINSKUr8akbVFS6CYXr5zuY6UAvZF4eaCZlyGIRvXTm7VtEnR4qas830QudmUMQCkIJov29fOPculs69HNtVwmYw0uW0jqkt0tHwvCEWsFwl3fuAa3KDMJE3fDZvZNokrrmp2NcwShYSJAIylW-k05P4QOoE4MJLrig2kpewjF3wHKzToouF8VaIhlb3n9JNjhhcGniu1NdHeo7DDsOT6ERf5Si8-EjKBQUricC9MZnyJQLKNafrtzOaF4H9N_sPTxnc-Vaoeg08khunqGaKKPzrX91K1wnXd6BIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmQzLijl6-MWybeuasyOLJubHsI5xxwlyG4pM1bs_GD1DOl7kozm-gD00cv7XudprC-YJqhrXyEivzPEVXxesJePLur9o3gB7vZbax7O6FzLc7MX3B7_UC32eHjv4h9cFy21680veFtoIKWoeCrvVKaIFfaza4PlkQcP5EktdvetGS4PcAn10H1qbN0JelQyuE3OCHVvCXT0Ggnx6o28mKi9M84qxbO0R1S53QF_cEwcl6dhLvtlkztr0vLXjoVFmer2meu46m9F6ERBFdOz98Q0-uYmtbbrqd-hceyLFXWeEcjxOozrqrbyP5xsBF83b6tkiZaFfAZjF_jnq6uEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkPuOBvm2pcp4wvkDkR0AYEinFcPQy0dTzwElBzhzMQELX96htq4juR99ea78DGRG13l6OwlEX8BE6MOhsBbC6QYKXWlzGVMDCcxQ9OIZHB6FEIWEAl7emLzuxUYaKkc6UpvM4sbGuXrDdmQkF1jC1_Im_OoaT8-HZhLx3H_TAnNzwkjCy-8MtFuQDMRMdpaLthB2NanYlA2Xe15wBptm7vGPFSzNvkgc6pUdpW8iGOfVFl8aMeBNmKo3zUVV-ahnLLTc1tNdc3bjN6giKr-9XG79LoiHk2rwrwl8z78-4EpRQ5APZUaK5QqqWl_9vcH-SSIvrWzLA_54ugFzE86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=HJuWAunGOxgvvDukILsAtX8eY_BgiQJ3a5fA3QgO50lBWMc4XUJfkM38CmVIAKyflYlI6VpN6S5x-2_VeF9By23zI3BrJfKse9B9Xp71ACus_ElFpaz-MVoWx9wYRngNcfcbD9ZdzG-Y-QJJUvIK5gbEwl-lVPouZ9lUYZTtFnzmbfYN-MYVA5YG010KD8VakgBTcy7qoXC6J-7yUZpWk9_9XrLj-3sESnEHhNmUd3bQVmbt457oZKLJdzDL5Y1CPeJpN5dOpvk3oDG6pMclUq-Kw7QPfGoIeO6kElxPQnQvSUQbfBY6zo_RVzvOQUIe5_FuvyEr8tOFSULzpt2AdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=HJuWAunGOxgvvDukILsAtX8eY_BgiQJ3a5fA3QgO50lBWMc4XUJfkM38CmVIAKyflYlI6VpN6S5x-2_VeF9By23zI3BrJfKse9B9Xp71ACus_ElFpaz-MVoWx9wYRngNcfcbD9ZdzG-Y-QJJUvIK5gbEwl-lVPouZ9lUYZTtFnzmbfYN-MYVA5YG010KD8VakgBTcy7qoXC6J-7yUZpWk9_9XrLj-3sESnEHhNmUd3bQVmbt457oZKLJdzDL5Y1CPeJpN5dOpvk3oDG6pMclUq-Kw7QPfGoIeO6kElxPQnQvSUQbfBY6zo_RVzvOQUIe5_FuvyEr8tOFSULzpt2AdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=enYnH10M76f5W_U0Gn6w_rrxFazaKCyeyP2YNiMt2ZyZUxzCDqBkqY98sLfhuI4_anL-qzy2rM2fjOZtYSujmtt4p0VqigEzBqhbdE6osaktNps5p212NfFbJNbDAL7LSZgk4eWQTNqbevqoa0JMtrzwIjeufSAveff1YBiqHk-JB82NN6eQnJK1cxskmH2103BPFklApGe4Ppuz7qxNGGfA61FBhluLBB6Pw3pytuToC4KBwqyt-4_cdRVIbGedbQM2xpZxe4BKeQekQLQLj-ib48_Wx-1dpwysfAqCDl7noAX0ya-rrOwJcRJDVnsqUkA0sSA5j540JPEY7Emr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=enYnH10M76f5W_U0Gn6w_rrxFazaKCyeyP2YNiMt2ZyZUxzCDqBkqY98sLfhuI4_anL-qzy2rM2fjOZtYSujmtt4p0VqigEzBqhbdE6osaktNps5p212NfFbJNbDAL7LSZgk4eWQTNqbevqoa0JMtrzwIjeufSAveff1YBiqHk-JB82NN6eQnJK1cxskmH2103BPFklApGe4Ppuz7qxNGGfA61FBhluLBB6Pw3pytuToC4KBwqyt-4_cdRVIbGedbQM2xpZxe4BKeQekQLQLj-ib48_Wx-1dpwysfAqCDl7noAX0ya-rrOwJcRJDVnsqUkA0sSA5j540JPEY7Emr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYHxXe4q32nEEucb8YbJHuGQ-uPPAlbEnnY77reWv45sIsCE2HGpGSlKxUgOjOjENk9xAs4d7_k5BADEzBADgc7KFAeXW4lu1jaz92kPx9ZDEc14tsq_KWBpgINNWEzNl-4_XFpfZ_62dyUv52esMnRJ-jnWrAyO_pe-C0s-b43amYBd-gtek0xX2a184ob_sc_IVvS92SA9_wAi_9_yH8xxGiAOJ98nyMl4Ir-5jP2Y97FXlDmIYaonkRPyrKS7HV-mWLSVBnUol5XG3Hrur_IXj4pxeBS9lBvokyZc4Yp1hoYxzegCg3Njr7wg7UwAcktjOSGR2YrOAHkFrytsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=iZGm4XDNnABDicFxJwbX0whAOUhK23smyCYwoHV5MROjOSMV1dHgHpveNNm5Fn6MFPm_D1EgbpuhnOtzlpNBW9XgmaDJtLw2P4iPQFqsZ5-Juf8bsluegrNM0yka7rqS4dtxlMH__kd5fO4B1_dKGXs0nPiXWj8n1H7YXgb9be_CDmtnw7mK3znxCQvDW5M_cNoImB2Rs5BqSgx2R8KF_cxwJOwY29TL5QolB_mnPKqSWjjDsILly6kLm-CGv9z_dX70otGWsIqsCWfa4rXLku6L0DJzdVJlar5IYsp28D-AG1lEo9JzTNjzBYvUcaLJwWmUqBBrorxPps09nGk91A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=iZGm4XDNnABDicFxJwbX0whAOUhK23smyCYwoHV5MROjOSMV1dHgHpveNNm5Fn6MFPm_D1EgbpuhnOtzlpNBW9XgmaDJtLw2P4iPQFqsZ5-Juf8bsluegrNM0yka7rqS4dtxlMH__kd5fO4B1_dKGXs0nPiXWj8n1H7YXgb9be_CDmtnw7mK3znxCQvDW5M_cNoImB2Rs5BqSgx2R8KF_cxwJOwY29TL5QolB_mnPKqSWjjDsILly6kLm-CGv9z_dX70otGWsIqsCWfa4rXLku6L0DJzdVJlar5IYsp28D-AG1lEo9JzTNjzBYvUcaLJwWmUqBBrorxPps09nGk91A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=ZgSQ4A2a_rvIC41DZXCgz9gmkjLAuJpqlZYqH-Ou7xjHUyB40mqccAl7FDXV2YMszlGhfKrJ92tiJVns9cT0CcO32kdJL1H0wb25k3k-6ovVLgr1XFe3TQaBU-iIXMGwrzkEVMdUf-5842RtSBt0dHTH3hXIvhEs-DlkRBbllX1DkZb_yCCQMXVwtoPE2XktV3mVlEKgUX5UYsIgwLXAIzVBbjh-vV0rbHu8iF-YDMwBzoNvoHLccyVM6bV9t8RrNo42kscXl6nbmjY8ORCOnDIJgNsnYEOTBUeVY5xt5tY1YtGCYObkbW8VgEr4hbPIkNUcLYN0Iz332-mTTwgshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=ZgSQ4A2a_rvIC41DZXCgz9gmkjLAuJpqlZYqH-Ou7xjHUyB40mqccAl7FDXV2YMszlGhfKrJ92tiJVns9cT0CcO32kdJL1H0wb25k3k-6ovVLgr1XFe3TQaBU-iIXMGwrzkEVMdUf-5842RtSBt0dHTH3hXIvhEs-DlkRBbllX1DkZb_yCCQMXVwtoPE2XktV3mVlEKgUX5UYsIgwLXAIzVBbjh-vV0rbHu8iF-YDMwBzoNvoHLccyVM6bV9t8RrNo42kscXl6nbmjY8ORCOnDIJgNsnYEOTBUeVY5xt5tY1YtGCYObkbW8VgEr4hbPIkNUcLYN0Iz332-mTTwgshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=RsoZi3mmkET4Z-xShgv0QNAwP1GMRVjlsRZEN1xZ_oEJpdi11EsUl2RXwH42R0GQEkJHw-8Pdzi6EEvsrCA8rbeIuTy4Chv5qGQxM9TtFqQsipa7q6aUQz3eBq7S66EtcoddA75yzHxpUOAhffplR7XOC4rUVeqozPS-y9dqsLONgGHAvkf5wyIYP7oeTxxnC9WLw8pTCS8iIHeVXwp6SyrbMtOHXywRumIpEJetzcxuI7oWHds5EhDBKLoVdEga9mIozc4LCKonLUe8yBIwxKWGXsYYoJggz2JVT4WujCUztvnXgdRQdpC0KZjstOl22yZ8D7qVEDd_DIRZ98o9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=RsoZi3mmkET4Z-xShgv0QNAwP1GMRVjlsRZEN1xZ_oEJpdi11EsUl2RXwH42R0GQEkJHw-8Pdzi6EEvsrCA8rbeIuTy4Chv5qGQxM9TtFqQsipa7q6aUQz3eBq7S66EtcoddA75yzHxpUOAhffplR7XOC4rUVeqozPS-y9dqsLONgGHAvkf5wyIYP7oeTxxnC9WLw8pTCS8iIHeVXwp6SyrbMtOHXywRumIpEJetzcxuI7oWHds5EhDBKLoVdEga9mIozc4LCKonLUe8yBIwxKWGXsYYoJggz2JVT4WujCUztvnXgdRQdpC0KZjstOl22yZ8D7qVEDd_DIRZ98o9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=UxnVaYkh1JQuFvQYmmxHX2fP9h4yTr-jgxGQfLMEHcCvLb-xR08MrndXftsbuIQyttakwry6OdDT26Q-th6ET8XUHde0zpEX4wf_-8UqtBw19eZg7VJIAxtrTOm5BAE9XATSgwAryPb7tJVGcdmqESLv6ZYBiXknsoo_JJABmdw9X1sOdYMjQ5LoJJC3QSTLFZf_uCKN2lc3NBAsCdV6Yv_pmPHs7BfLQgBiCEmWb3pP0NYsELeyR7EkaJqiZp48zLIRmum7gHONi6nfidxw-Q-tF71N42OMKyzlPM_U_x_teYN1hXh8PoHcy4jsZQ4tWbKtBS5WVAY7qU57XbbEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=UxnVaYkh1JQuFvQYmmxHX2fP9h4yTr-jgxGQfLMEHcCvLb-xR08MrndXftsbuIQyttakwry6OdDT26Q-th6ET8XUHde0zpEX4wf_-8UqtBw19eZg7VJIAxtrTOm5BAE9XATSgwAryPb7tJVGcdmqESLv6ZYBiXknsoo_JJABmdw9X1sOdYMjQ5LoJJC3QSTLFZf_uCKN2lc3NBAsCdV6Yv_pmPHs7BfLQgBiCEmWb3pP0NYsELeyR7EkaJqiZp48zLIRmum7gHONi6nfidxw-Q-tF71N42OMKyzlPM_U_x_teYN1hXh8PoHcy4jsZQ4tWbKtBS5WVAY7qU57XbbEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckVu4k7auW6NY0LUnRH33lAjPyiqPM-GGUej_qe97MeNZSEQ5Tc45zwfWDmUV7N4kOO4As2TW7iOesTlJOvlGE0jYP48nMlNRqoSczH1McaSqCrSv3wNtX4lICCeZyZ1O4-3S4QDyC4PF3xOwKk-egma3erUpzd_jTit0UxSOuq2bRO8vkOaydaUfUFxDJ-kYR7Nh0PmqD7rHiDeAvZKN1YTb_r4E4tqUBpPvBcCINy8Ho9GIZXyQupMsKU_wkXK-w-hCb7bBIMqPd-K2_XyiFqL1VO3yqnTVm3eIB13pD35qa2EyMnvAp-U6_O75J03feYzQ1K_to3HZ5cvQEs30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVDUEFND2gJRMgMJ351RDgRDwf5ZX8-txZTeK9TJMetvb-WctRMhWcSiMG2a2IRGT4p2nq4sBvIgoobU43KRktIhTIYSZJn2b2rB3RWqqt-oT4UC94kWRi-DfvElo7dwO3ytDhiZCzAvHQuRzVOXctvdISx7sdVhX16aNwb_ejAbN6wgqa9k1aVV3Igp_bZ9kuxy6HxpAOkHpSkvEMQVaWCj_VT01Ny1a-wHmkIhmN0eBuYfqGzdDdNjcf1zTAVPmIR_8UA58RYZ-zSt4ANHmQEmKjKHKfrKUEAoqGIdxHOxpg96W0duEusSJUUeeAT5pqH9dYsrCsX2MHwrIKkn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3qPXmYLn8wGNo5G2KF9O4UadVwLgwXwjffURIUCrs85uz_eKTDKE-U3zO07oXhQsq7cAAW7saFyOwkETyjj_UzfwLGcSwREhj0X3FjJfeajCaQ8SJWL7gLvhk6SXFvJcUjE6T7zLP0NXMqUpEyBJ8ACZ_bxydGWdSEp9knHofr21cdsM8sfmOCe4CB97FK2EQfsi9SE9gjPyatzwvjSHoZtIgGIg0X6TMb6a4ZtVdLUaO7xeipPDVKI9xF0epl9EcHSCMOqXWXNxnAUsy3uQI2MsZbdI5g5Otmap8GL_de6Sgdbf5GFW0FRSecA-lojnWloHhMnLtaDAhjzjWcABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0JBeGYjSXWthkaKRvUTgROvAYqpBRVI2UxN5EX9Mn1ZDchyyU7xrWR8t0yH7mO8StHG9jO_nyAfKqY6N0cz4g8EWGZxKHAvYQyshQNzW2iRFhwIb1OIRWOWX0_yod00Km6A5fb90KbptOJZLB31aVK7D3e0zhp67aWmGJx2uq3EXpTmDvF1Aa_ailBKu8pFt0lXR6CEPYw_41sc2h9WKyYNtyLX2g99HeJMa38HZ9MPMTK77qhA4IYgZ-XYDEuG6vj71bsT_XH-qkC0E5u3-1cCdzKx7TGTgKSaXo8PNow6Rvyejj2FHi90NPX75V967SQT5Q8kg-vy_fv71PtMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpOFrI3-k8j7rvP9oKo0SaLpSXLPG6zgWwAkpQSBzTDzccHipGx5K-vJVfVQt3dzYu2SIfT6bO9hVTTXW9WRhH2TZYc23ZrvVskzywjBC6RNVYHQVtoiO1FA-V97ITsXgMIv8B74SnPx7-P2W20K4sUrKD36nWkcLYAmDTxbiaKM6gesVgR7IBVlNvkRS27kG6gvrubKWkljQBdhHaDOc6Wu1FgZx0Na0pkKhK2wnlOQH3QJtFbuIGjV9AYPW4cJQQ_gezhVLJN0giVkThr6dh_iKk09kUz6o478LhUrfed-53mGCykWEzLqkicSn-P6aLSHvKN953QsxYsWeTwY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtjfHXwC2La87OjMXas6FTsZH3UZx4grRbMqM6DDOASeGwphVA2Y7Y79fzsnTcSGASdMesLVXBNScljDAA6m145IJPXf_GCjefgq03GspOMffofNUE3vz7g1tLRQsAWBYdjEjXqu1yrRKEDyHxqkxn8ys86T01Vr_INfICtvfIt-RGmHorhwrMbxrUbxhJX4Ye2D3_BsgZS6TE4QXjuRap8nP0hT9rMc-VxIOFMhjAH9wyIH1luLKgKsKIJhoZn3olcgiF9YQkQnK8OyDlT6o8NK0zZzLkeHOJAAi6mhSi5JcaFyIRSi10jxJ--SHJqO_nndCTv6hjxQymohg_jXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=FEY2aLdTswrE2CShAwPw5-xMG6PwNFieCeN8EOmWp-IzusGL2ZSsK2wfGFWdSq2ALAHE_p1OHss31r1Yx1W_2a1XpziaedniPUuqWfNSWaTchQVvgVKrRBwbQFGksV-8ANcTV5ud9r0oJycFeROgrVewROQSivm2TGkt_Rb2w4Fz2_bVB3V8W07t6JRCfycTOsWFwJb9EEwheP21-icrNOsUzo3lB7kuWAafrFkc46KFLyO5RECk7TFMqzXaNCNY720C-DBpg645iLiV9RKpKpXPf9GpaWkuKx1hc5WqVK4za4ylJc3T7eSQN5KN23xaifhqHukfdIwZIDfR8sPO-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=FEY2aLdTswrE2CShAwPw5-xMG6PwNFieCeN8EOmWp-IzusGL2ZSsK2wfGFWdSq2ALAHE_p1OHss31r1Yx1W_2a1XpziaedniPUuqWfNSWaTchQVvgVKrRBwbQFGksV-8ANcTV5ud9r0oJycFeROgrVewROQSivm2TGkt_Rb2w4Fz2_bVB3V8W07t6JRCfycTOsWFwJb9EEwheP21-icrNOsUzo3lB7kuWAafrFkc46KFLyO5RECk7TFMqzXaNCNY720C-DBpg645iLiV9RKpKpXPf9GpaWkuKx1hc5WqVK4za4ylJc3T7eSQN5KN23xaifhqHukfdIwZIDfR8sPO-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNy96DAGN8zQsWtX0XqIMaayhualDAR9Kf7UgSo35-s_Df8Q-JeG0Lu78jpmavCpWCuc1x64CgaMmr0ujuk8xYu8Y3Zu7qdPWwYxKQX76jh6TVPqLYyhj9-Ue-RLDU1BsMOjuoe7abB9QMX3TpQNfgpfzFKVNDF-JOVrTWfWUURqqELJo1jzCfR6ZXdNIEKc24VFUQZPEMeP7BimnkPaFd8_A3IzIM2vodxe5M21j3_N0ia2Qngl1q3EQPX1Sq2MaM4wi8fjTwNxGaBFVwka5H4AtxhM9T7gxeanRXlDoKnD1cHw1-NProveNIzAkcBOUOc5biU3Woa-zxVRMI-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhLxNxXxZTZ1oQ-vO_CflX4LAidbqshaYdYDGVV70dEDuFydt59vaX9x4CbB1Yv1RqbBb-YfL0hgvRk9Yfp_wsF6lB0Pj7y9let51QOeDiobj_cZKehPW0m0RgJNvZsRfnQahazRBTEMufD0rrTQkqoGnQ1QujygVLcaelZYNa5ocP0Y-XjJ5dUaxuN-d4hV6hNsnClW1Q6mOIxI8939pvjndofMLefEACreIu2AtrE278qI2Aj6nzVwmRqZc8sgjKRe39PDinvtTEdibTAGVmkISkFhzB5LQNmmGBZc_0wGAxXDWRRicN5i0PqUdQvLw1U6tZo5MXWN119kIbWKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIs6Ew_VgQs5NpSgAbN3uwXl2EEtTAeQ5ANnTPpjhqTDv5ZjdZQ1CJ4c-3artWr1cjTe_oBSx1I-aMd6lRtgMLpsq9YGE3pgw9AWhCKKJmJAWVQZAv0aAOcTrtSUI5Iub0mr_xN4TQTUehFceFe8IYQB-rf2sE5uNI6NdIOYNfH1z5QqI8cPi6Wb9nlQ2gZFp25UJTytW1spr-ufWQPz6jlZJ1WXWoDYe3CnyjUDrDPA9ZWDlOQJdS84jRgluARsET5Q_rc5nZxbXPor-DlQuGRsJaOsHh8pIODlOVeIFS-NKvPBuGxjUu4v7ohU3nD1Wrkc_FUZJLUKstaczdEXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwpTn48p5YWN0F18hZI4Z6_9xJQNoUmtkPKGpnclLhnme4TieAUywT8aZ0XWXnIGoWfCq5T67XFtwpB_yyMVuYmH48AlUGblLoe7-qbnpPyBlZqN81tXaZVi9E63SvzVtzxWM0D0CLKaGNcZfP-exn4NxUqPNEyEe0YIr3fzS2FwqVkXes9vxsk69mu0YCR8ikcKSzEpETPhtSaeLwxbTAlWYKBvqDkxCLxD6jCl-fNFCp946zpVb2NyVb4iPlaO-SbkCiIdsM9wZjO7h8rcJR3IlNr6oNGrrcxL8RDvCasH2P2Hnd3wi99YisFrrRdOt9OO_SmJ50P3BZWTK5Al5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=uGkl7aVlmS17zoIJa4ZadRaHKnF-Y5UhRo0IFsyd3ejSbZXKZoWAPuYqMPPk4WyxOsGG8UHFC6XUyo4SvSs9IvspnEjnwjsDAxfZOJJfoxrFbgfiIBGqyCZ9lE-cLmxmQ2PhlmB7eQww6YGRso2DlSjqIOUhFjQDpQQ8epxG4TM9-PxlC58KrN1g0necjSS6VKIPknIGgupXN7zq_GyoJvvrAzR42LvF2WjJl8W5iu40XtV1h4C20B125NWZruDJfHYEo19TBjOVFl62wzf-M0EQuDcF9SwzWA-JQCkoDmXmvB9Q0VPHSTKOBWGDuGECHDKC1ciotn02r0r2wkwruw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=uGkl7aVlmS17zoIJa4ZadRaHKnF-Y5UhRo0IFsyd3ejSbZXKZoWAPuYqMPPk4WyxOsGG8UHFC6XUyo4SvSs9IvspnEjnwjsDAxfZOJJfoxrFbgfiIBGqyCZ9lE-cLmxmQ2PhlmB7eQww6YGRso2DlSjqIOUhFjQDpQQ8epxG4TM9-PxlC58KrN1g0necjSS6VKIPknIGgupXN7zq_GyoJvvrAzR42LvF2WjJl8W5iu40XtV1h4C20B125NWZruDJfHYEo19TBjOVFl62wzf-M0EQuDcF9SwzWA-JQCkoDmXmvB9Q0VPHSTKOBWGDuGECHDKC1ciotn02r0r2wkwruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW7QpMIfXFcLeEDh8BLDqZ6J_7qu-9d_Ee_LhXj7uEjYHGQgGOhVceq7FD9LJDZhV3QBd5rR1hMCwjGIPsdxnhFPSLgtAIsES3sh7JTCTryofFuSMDpV9EPcuBL_XNVGQrYk6COETXA61e3sfZ-2mi2eXflq4HP67Lh0Nt1S-Xi-sH0LCfzI2iZbA03qkrlYsuwO6TCX3MAeiAhTMLjjDIxat1J0bY2kPcfbulKjruPyLXiUKEn4EqaHfXNLfSy6eY0avPub06Bcr7iV23L-3rPQjdF_8lm5OUz8K6cBQGceRZlKfie5_D5WRmplhvtWYDRrn-_k3J9e8Epd8kp-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=FbJ8v3gyht_PsuK1oyw5Y1MrUUyRw5uyp2G4fRcrrAe6qu9Eyqg7A4NKKf4KgBnSCGzSi0M9zSHAH5PwMCBrjUsY6QbEnm8jZ-t6K6RrxjT3gYjGU10tOqQePGBPl6xRt-7tppMMjeY8X4-rqvcA-CkgZf18h9geYisGNqpu0vq4Q6Vmvd9YzPqzFYrlGboQcAbCfW7jqnlqEGJi7qjbPT7PXAfCTUD064XLI6Dhx9nJFkKvLkBJr8E9RsLVV7E6a13pKoCRYx5TzNioNEgk-pKHnvffCsLt2UBE_bgxft8Cenm5vm6VsUegmUzCLvLMI2jdFeQ9TzA7P2iuk0BaFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=FbJ8v3gyht_PsuK1oyw5Y1MrUUyRw5uyp2G4fRcrrAe6qu9Eyqg7A4NKKf4KgBnSCGzSi0M9zSHAH5PwMCBrjUsY6QbEnm8jZ-t6K6RrxjT3gYjGU10tOqQePGBPl6xRt-7tppMMjeY8X4-rqvcA-CkgZf18h9geYisGNqpu0vq4Q6Vmvd9YzPqzFYrlGboQcAbCfW7jqnlqEGJi7qjbPT7PXAfCTUD064XLI6Dhx9nJFkKvLkBJr8E9RsLVV7E6a13pKoCRYx5TzNioNEgk-pKHnvffCsLt2UBE_bgxft8Cenm5vm6VsUegmUzCLvLMI2jdFeQ9TzA7P2iuk0BaFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=NbX0csL39TOwxi5lrNNKTWuZtGoUocL3uMZg9KxWhJ1JTF2GjISihrJHReTvmFkfOEXbmHw1D7VLXzFTbF5gElJJuEPHsQHg1Ly8qYZA13_-u8_2wAWdG7MO6Hpa4_d6CM3p8E7Q4u3EbomgttZiV_AREyXDOVi-dUhQsXkIU66_WrWiIUfQrMc83CxXDH-k7wa56H06GDCvGebBBZsPdqt0mutss06bnFSd6oUkIgRy-Xbll_mGq4wyZ6ArCLsZH5SjzdctBapMqs1WD_lVS_AB__zshFPOzHvvf7Oz0bu4CyE5MSTwm3IH60A-DXWfKBZJD4LbQiWqOznLjd8OEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=NbX0csL39TOwxi5lrNNKTWuZtGoUocL3uMZg9KxWhJ1JTF2GjISihrJHReTvmFkfOEXbmHw1D7VLXzFTbF5gElJJuEPHsQHg1Ly8qYZA13_-u8_2wAWdG7MO6Hpa4_d6CM3p8E7Q4u3EbomgttZiV_AREyXDOVi-dUhQsXkIU66_WrWiIUfQrMc83CxXDH-k7wa56H06GDCvGebBBZsPdqt0mutss06bnFSd6oUkIgRy-Xbll_mGq4wyZ6ArCLsZH5SjzdctBapMqs1WD_lVS_AB__zshFPOzHvvf7Oz0bu4CyE5MSTwm3IH60A-DXWfKBZJD4LbQiWqOznLjd8OEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=fRFAzQJ_5xVISUzIZBF42FSFl2jh04oodN4GoM77yGOrpSuKE2fc_yu8Wo2Y2h20OMOf5cfDxWp6EKKERnBtMZ2sIT-_m4g1zHVsSoKF-a2bsCIwNhyHrxAT_p3B8oSeNxou6AEnnwdyFqv0JMpGWB7Qm6biBSUMddkVap9JJY7925vO0w2ysWP_fAXYf9QZNPIdYV_veEsFN-5ofkOoJyS3N2V0CaWnkPQZG81AnaLfXJwXqodfA9fVeNG8omWV6DbaZiWHBN-4F9-kPu0UYxxvtsGgcPx3GS0zha0Raqu66O_hrsjRwh4pGH_JaKpse9BKCXsoDxvBjyKxre9GMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=fRFAzQJ_5xVISUzIZBF42FSFl2jh04oodN4GoM77yGOrpSuKE2fc_yu8Wo2Y2h20OMOf5cfDxWp6EKKERnBtMZ2sIT-_m4g1zHVsSoKF-a2bsCIwNhyHrxAT_p3B8oSeNxou6AEnnwdyFqv0JMpGWB7Qm6biBSUMddkVap9JJY7925vO0w2ysWP_fAXYf9QZNPIdYV_veEsFN-5ofkOoJyS3N2V0CaWnkPQZG81AnaLfXJwXqodfA9fVeNG8omWV6DbaZiWHBN-4F9-kPu0UYxxvtsGgcPx3GS0zha0Raqu66O_hrsjRwh4pGH_JaKpse9BKCXsoDxvBjyKxre9GMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moIY9vOK9WBnxgSi3TwE_J0pUKTE6JCq-jtvjED5j7O3ix97Y7MZjxzC2jjZQeQL-V44uwxoKkQO9Pl3U-k7xNc2nG3GmGAPfdeHZLsVx5EanEaTm-Sn7YL8zqykZo-EuLHg_0dGOMzQHMzqZWxEu1kh8L5035jRTaQ7CR8gywutN1vXNrilQyCSyu6pmzM9DRu0A7tZeA_BKB6i_RJxBHVx9_gk8cuNfPUJeWOuItNgk4IlAEFRcgsT_gLHDuLxB-PQ7R8QGt5ZhzWx01RzQ3CMao18RbaHgg8y1XYtyyk3obuJ4KNorLwoNLJRkLcAkS5YeBv3AGtAseOm4NkhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=LChnV-GHzN-quW5pQXVZXMSRpS9tkVPQKgq8rpnGw9yoSbYfZCyBeb1oDV472iKAkLEn9GiOVE_IKOq4Y4bhFCcTPUQ3kJ897dLgNgLddDvIAHGzSaSSoxamgl41jnYufWhFhFi6Lf0OszLjFKx9h46zdp7HntecLEH6EVljjWC_vvPnV_INslZMaZ7mktBdTHNXMC6RUwNYh7KAFCEhbKeipViM22oighcskC8Zkn1NNOYoRGeFDnvdjxE3eDdIe0qd2steWGrI1Q9Ae9h8qZZK3w88l0smPLLrwC7kvMsotuDKfTLUBqGTE1_Z-pAvy8Om_ADQvkdKStslH7ZRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=LChnV-GHzN-quW5pQXVZXMSRpS9tkVPQKgq8rpnGw9yoSbYfZCyBeb1oDV472iKAkLEn9GiOVE_IKOq4Y4bhFCcTPUQ3kJ897dLgNgLddDvIAHGzSaSSoxamgl41jnYufWhFhFi6Lf0OszLjFKx9h46zdp7HntecLEH6EVljjWC_vvPnV_INslZMaZ7mktBdTHNXMC6RUwNYh7KAFCEhbKeipViM22oighcskC8Zkn1NNOYoRGeFDnvdjxE3eDdIe0qd2steWGrI1Q9Ae9h8qZZK3w88l0smPLLrwC7kvMsotuDKfTLUBqGTE1_Z-pAvy8Om_ADQvkdKStslH7ZRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFm8YUho5knPIv0kZsqAJFb6WWynAYb7UqNqBdW5rmtPRJLedkqknTHvit7a3daUt7L49KwdMML9XxrehEcee-1horD1IZlmKWIaU_SznjibDVRxL-fqT4P9HHELoXyV9w-xvnYwUGWWjJBcjLvrmNLhtY_iM3I5dEHHVwNP-my5aYHaXvHt4nzUv-kq19DtvhAVTpA8kRMzhDunnv0v2EEH85SUz2d_jWje2fwDNpNdJ3Twu---deQr7l6gKyT5_-sNEpXl3nRe27Iu_jDx8qUvsFWOx6_1dM7FqAlgbuDdLThgOHvJoDgmKG-x4vIDmVPXvidTRWout8j3S42QcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZWyuJ3gBNkSHA_EebHXtvHyeg6D8buq6_AZXO6jA_hDjCJCiaMcr3S9blYZ85jJu37nDCYZm35yk7seRZYB4JGiGhkVWI-oENKJWg-gZqWbRs6Hx1q9hOjCntzkYYDw5Z5nZpf836YyBivLmjJa5K7585p9qFjVYvrdtBgvlvMLLuApbhfiLkEmspJNYUsNrI2WhgShMASs4gp7cWMx6NoaK_S5NZ2DIL1iGbex2IpUpc6Rx3rehyLUbUwDScWUIJfRuK2oT6RuKLjG9oejH_8HuPb5B-epQKXEv93bHBgYbCClpT9kg278bcoudyYVG6w16HF_5uKZxQBOW3yUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=h0dDO-eT-kUezTHh0vl39oa7E8c1zgDEAvbyXgLQG5BNkaucjDLnrW4T_UA4Vj36gWE5yhGlGdxhcQapT7RkXhD5UeP3949SiHQRv_VfWGPUFmpHDvqzbRK5_rxpNwb30P6dSOb7LpUAI8-9M9qgCeqoGoWCeD1UuH6A9-dRkkXHXd1HS5-AgoHLKxikKdufAZJFWB7knaZQ86PQJw6mqzFPnSiq-8MyMzmgBeR0jRlegkMNqDq7f1ckgQ7HGnSnS02UQ7C-s1-m50ZFsWLDcV85aPOycbHk64pFcX4ekNU793Fg47J-c8t-8-CQBD7Roe1fLTBvv0usnDtmYfwPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=h0dDO-eT-kUezTHh0vl39oa7E8c1zgDEAvbyXgLQG5BNkaucjDLnrW4T_UA4Vj36gWE5yhGlGdxhcQapT7RkXhD5UeP3949SiHQRv_VfWGPUFmpHDvqzbRK5_rxpNwb30P6dSOb7LpUAI8-9M9qgCeqoGoWCeD1UuH6A9-dRkkXHXd1HS5-AgoHLKxikKdufAZJFWB7knaZQ86PQJw6mqzFPnSiq-8MyMzmgBeR0jRlegkMNqDq7f1ckgQ7HGnSnS02UQ7C-s1-m50ZFsWLDcV85aPOycbHk64pFcX4ekNU793Fg47J-c8t-8-CQBD7Roe1fLTBvv0usnDtmYfwPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=Fu1Xr1W4KNiBluFVhqyuVrBxnXwe0mfKjpmy-CauxeHXOR4dfl71PQdGzB_gz-Zt1KdfuXHB1QdfXMpBG98eIh9Bn24WlV1QglEcC3NDBRaZ_bLKwYMscy0uQLhP7edp0FR_EwqCQK1ArOEg8kG_HuCftr9fZfuN62DfGxa2IbWqmwy0gSkhB0V2_5iHFbl3nUPzSfZqZ9mvJbKq9EMq1pkNVgwVg8ZKN2FBlv5pX-XtF-Cwro8NUjdU0xvhv10CmbvoTNUxm2WEPLgKNv0F_qoju7ZBYPYfXrLry7KQpXgBSIGLBOeG_a0x-h1wYXZZzhgnqizK1khOxSovunPRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=Fu1Xr1W4KNiBluFVhqyuVrBxnXwe0mfKjpmy-CauxeHXOR4dfl71PQdGzB_gz-Zt1KdfuXHB1QdfXMpBG98eIh9Bn24WlV1QglEcC3NDBRaZ_bLKwYMscy0uQLhP7edp0FR_EwqCQK1ArOEg8kG_HuCftr9fZfuN62DfGxa2IbWqmwy0gSkhB0V2_5iHFbl3nUPzSfZqZ9mvJbKq9EMq1pkNVgwVg8ZKN2FBlv5pX-XtF-Cwro8NUjdU0xvhv10CmbvoTNUxm2WEPLgKNv0F_qoju7ZBYPYfXrLry7KQpXgBSIGLBOeG_a0x-h1wYXZZzhgnqizK1khOxSovunPRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=GDK0CDIWIStroSA-0jHG5TBX5D8hZ2ew9yKLtH6scGy2XspoJE43dbHul-g6RURKLvj3rSmagQNY8n0s0YZA2njmk14ovGP215c3-LpAJTFZNoq4RYIoqBOyUua02ZXFYqXzFWpBO30GFk-Sif4MOfLdrQmG926nZTUFDV_teqYGMBLVbPfUHDWDME3ceZ5bDbl03ZdsCjGy7Ve5SeE6RRLhTHzvl5d_JgZqhTECxrRiXt5KbBfcCBXbZebGUT9CVXqX3ur9N8ztw96z8_GXT1maRPnN5NYc7f8R94eoEazuBU_dlLL9koeWR0OhfmZA3T8czHcHK57G9ZAtKZHBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=GDK0CDIWIStroSA-0jHG5TBX5D8hZ2ew9yKLtH6scGy2XspoJE43dbHul-g6RURKLvj3rSmagQNY8n0s0YZA2njmk14ovGP215c3-LpAJTFZNoq4RYIoqBOyUua02ZXFYqXzFWpBO30GFk-Sif4MOfLdrQmG926nZTUFDV_teqYGMBLVbPfUHDWDME3ceZ5bDbl03ZdsCjGy7Ve5SeE6RRLhTHzvl5d_JgZqhTECxrRiXt5KbBfcCBXbZebGUT9CVXqX3ur9N8ztw96z8_GXT1maRPnN5NYc7f8R94eoEazuBU_dlLL9koeWR0OhfmZA3T8czHcHK57G9ZAtKZHBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUoCkT4KnTjvJN2CDI1y-nsXQ7kQxT2qtkoHyDVhP77V20xCJKKltcZG1BJ4JZI3tfmsb_J_nTkYDV4ixy1lX0t7AqvraWqFVB_uTrs2B6gdouePoTOc0yrnzdSSESIagCrfeiX6LFoGnTdyJwjgL9mUvZWBUs5KALBpqOgOEQi0lT2ZklAt6wXh9S-qUY8y6PC-1RCrhXwuGKYNz5wMGWXoItZe26anVjK2AMJLscuxctQFX358_4--cxquMLbkengb3wbhRBL92ab-GU4SvnZQfWRokt9N0Q7am8IEP4qt4rfN351-UWRmtK4iU83AwF2c26be5qGJyeav0BbZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=B-GTAP3tJ5tHqV7dtCp7IE8p6k3fUp_kaiO4ynYqy3NGvgYQv6duSi56eTUIqvNMQCNMw6MHSHlexhhkUf6XGhwCYsKum1sUzv-u_aKjM-BR1iFptlJHplgB36qzj9002st8tCYOH6H4jZYIW0LemhSiXLhqS-OxB_nP1cf9go1mgW2FuKEQdvZGIpM4v96S_CwfK8Ayhz994Pt-zF6rMt8camDGl_Fd5lIl3b6Nqgh-3R5w2ZfnGhOE91mX3mXr2CC4Xu_eDtNJH76Im2ri1xZislbKlp6ST6TAHyPOEsTPlN4ZSD_CFVxVvy_bgQiudRrbkzp7M4P4mkHFRYmBwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=B-GTAP3tJ5tHqV7dtCp7IE8p6k3fUp_kaiO4ynYqy3NGvgYQv6duSi56eTUIqvNMQCNMw6MHSHlexhhkUf6XGhwCYsKum1sUzv-u_aKjM-BR1iFptlJHplgB36qzj9002st8tCYOH6H4jZYIW0LemhSiXLhqS-OxB_nP1cf9go1mgW2FuKEQdvZGIpM4v96S_CwfK8Ayhz994Pt-zF6rMt8camDGl_Fd5lIl3b6Nqgh-3R5w2ZfnGhOE91mX3mXr2CC4Xu_eDtNJH76Im2ri1xZislbKlp6ST6TAHyPOEsTPlN4ZSD_CFVxVvy_bgQiudRrbkzp7M4P4mkHFRYmBwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=pHVm-bIFlt9NKbRr2wuucYAuWaaYiJa3bvhR-vgL8HrW6RrSoj9uUvDa6fLjmn8DBGzBmNyaV800aKtXVSDXl2-ixuTERFAWn6fOMe8Jnxq43YNynkHs1o0lPtNff1IeNgcS-NS_aBziy_8QpnB19Udk77NsH0pjkel87gZXKAuDWW6tATnCPUXpOEzxluKWpsqF8n_LUPq6fgQQ7bJHNZn0_l_kmWWDOYVnVL5LAvXZbUPJlipTlBQsyLkLoSM8jmblI8u-BBq0TqURXrtj5gFa-53oIMxjUtz0qN3HvlalmboDDcenuAzxDI-4CCmamy-E6lMXsE74kfwLRPxXyHY9AY4oHTw3e4MEQeZ-SeHNhEbXjixh8cut938J5UwKM2v0jciq2MN05aTy5n-B47OjiytduJE5W-pPHvOo3eu8b9F9e62XkhhZj9Cqh6qqKdQsSeH5NKgJFrJAAteMaN-SeWDub__6ZE7LVcTjTUqof-qPYiTnFUkxRRxeqcUdzmjxENn4G8o2yJzbj24tCjE7AoGXsYzd0eQ8xkmHau2aoTxKVLVjiVuAcu2ediqBGeKBysQAhgneIUebBHIdXzdO7ZbMprcmcJYXuSiAiQruiDIbQcWctan8K-xX1bTthIluSMEI71lLYW3jyatJZ7VJOrtcQqy3lr6E1iVw1No" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=pHVm-bIFlt9NKbRr2wuucYAuWaaYiJa3bvhR-vgL8HrW6RrSoj9uUvDa6fLjmn8DBGzBmNyaV800aKtXVSDXl2-ixuTERFAWn6fOMe8Jnxq43YNynkHs1o0lPtNff1IeNgcS-NS_aBziy_8QpnB19Udk77NsH0pjkel87gZXKAuDWW6tATnCPUXpOEzxluKWpsqF8n_LUPq6fgQQ7bJHNZn0_l_kmWWDOYVnVL5LAvXZbUPJlipTlBQsyLkLoSM8jmblI8u-BBq0TqURXrtj5gFa-53oIMxjUtz0qN3HvlalmboDDcenuAzxDI-4CCmamy-E6lMXsE74kfwLRPxXyHY9AY4oHTw3e4MEQeZ-SeHNhEbXjixh8cut938J5UwKM2v0jciq2MN05aTy5n-B47OjiytduJE5W-pPHvOo3eu8b9F9e62XkhhZj9Cqh6qqKdQsSeH5NKgJFrJAAteMaN-SeWDub__6ZE7LVcTjTUqof-qPYiTnFUkxRRxeqcUdzmjxENn4G8o2yJzbj24tCjE7AoGXsYzd0eQ8xkmHau2aoTxKVLVjiVuAcu2ediqBGeKBysQAhgneIUebBHIdXzdO7ZbMprcmcJYXuSiAiQruiDIbQcWctan8K-xX1bTthIluSMEI71lLYW3jyatJZ7VJOrtcQqy3lr6E1iVw1No" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=VpXQbxBgkNJ51UNFCS-l31ZZi54CpPqZC_hONf710BJGWnN_olc0dS5aiHjv_qMoB10pKYSH9LsKilzIWHX-W5I9mn0OokcEhO4I7ccVArWGWXkVjevOW9dtrupBNe9bPrWCv0YMErwndBpPcsARznxSJIWEbnZ2KKjh2pAUm8XkzE18ZOYHnS10WtLPLsdtAn8qHp6UEp9V5j2IGGcHTMmzp5qN2IPLXa9QCqzdKMgiPmEelINm3MXGA166D_S1POBGb-KPymbPABEUXFCsZDGjkmn0rLGNoJU-QUd2MkxOGpz3AOV5oNQnv2kHAGF2qcp-M8VYps78Iqd_u67CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=VpXQbxBgkNJ51UNFCS-l31ZZi54CpPqZC_hONf710BJGWnN_olc0dS5aiHjv_qMoB10pKYSH9LsKilzIWHX-W5I9mn0OokcEhO4I7ccVArWGWXkVjevOW9dtrupBNe9bPrWCv0YMErwndBpPcsARznxSJIWEbnZ2KKjh2pAUm8XkzE18ZOYHnS10WtLPLsdtAn8qHp6UEp9V5j2IGGcHTMmzp5qN2IPLXa9QCqzdKMgiPmEelINm3MXGA166D_S1POBGb-KPymbPABEUXFCsZDGjkmn0rLGNoJU-QUd2MkxOGpz3AOV5oNQnv2kHAGF2qcp-M8VYps78Iqd_u67CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLUjJtaFefVJezfCdKMPPnbgU6uphlISfn231Kf34phZy3e5F9fwLipg82eddBAoYoyscAB0W6exAz4MRU8aOsmiJufC23V4nV1hAbQ6b6UtywuQ45dbie3iAJSIpDkmXFdPVWdmwDbXNq8rxPyooJlDf_uKKOVIQZwuWSYlTLPtk_yu6GFDpG2NtTyv9ZI_uEVmZEXc1Di_ogsFoYcsT24j31BOE5UKfGvi64hFkHqqWFhagJSYG3tuY-X1i_lr52_Up-M9vH0mOKVpFz8wmy2Derml5qWSpZzRh87n-pNYs3ZLFtmAmVc-abvPZUwnuzS8ubbVNjxMvEk9aB4qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBlWngSJdhdPUR6H_bXnRAKb7p7gr58r5eqiHLaP4iHp4v0s-Iz9puG1SNtygCP3YBVxf9gekqy74ZiIRY79rrF-Jpn0vmIEhWTYnb_pIRS3kXGPPL-vZTBPWhgQCXCmVIAn4LsXO5evcZMU4bd8LKuM07h6SXQ0iuRneTc2lEiz-koCC3jRSdlJwWl6h4e9M6OiNHetWOdzBKCAgwN793FAZzRxoO4jyMBkGkasrOsnw545mS63Qzds8p-sfMRcY0tsebyngH4t12hY078GKuUBXsC6L0oXM8AYo9V7RE7bfOem44B5AF6LKRm_bk9FANqq_k1EVB2S7TbxE22z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzsrCclPecb__e-cTq5ZNjFKfFDoNRLFlcCTLAdQyVZEhE_wL6__LYwHJSJ0J1sZyIsO3HveYoY3Xy2117Cf8vsGVc7cQl4XcncLs8ZPjPUa-ZFX3iwvCJ-oYJqvxQsSZMAPh1wpePO3r_S1Q-5UZ127qVrUmlYdn-fKkzj7Ce3Kjo_6ayZi7da7igyIgAfUkB-lWxyb41sCXAC71rsQA4cp9yhfLgoSTtC1UJxLEUOq3xoOosqt4evJG59rUr1YiBky1tswxPZO_FqQZBWA5O8XRii_Qiz6Y8WKPx2HSFWjTMC3QreJHIwvBxfY5KVfYEViik5elMASS6FkM2SdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql-S41W0IuNLFtxImixHUtfmSAneWB9TXCYWPTcdDt8kn_fRT9OlvsJO478bfAThD0--5p7zZVBj3R9yrE85zdZeyb9bV3-T8ocM4QtM24UjXYXFZXuedVFscjvqjmu5SSb5xmzGGwhDij6kWXA63QljDXGFuurNikKdH1fVuOymPd3H3B-CJkDuHFhuNAbf2jjz5kVDvKLVw0YMHlDAfSPVRQ2bNwnb1IlBIsdYTD6MVW9qsQ1X0_0ynUr9kyP7UYb68vqvjhms5_Xc92zy5szK_t7fBcjhhNaWjPO1QUETi_NRp3Phskzl-mqZSPl0L9VK04_Opt7ulxvHZgUilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=aMXkKvL0eumfg95F_zQcuLS_wgR2r8_uelGyWjokbCLYqrFk-UfyApsq-fD7SKuTfL9ronqs9bfVrxDJuFERsF66Kdwhc3aMY09Ao6spmRpcx0yqv_s_7ieN73eZruRWuiOKGRx6o6i1LCL5RhZxIBXQPsEbduko5ychRVN_cpkvc4sLyDeDM4nz_6gs8q1fxJtjJGtO7C_E0_OCON8uP5AwfJPfQ_AgqwCb0NNvXdHNlGIMQqa7qipAs0Wb55QJ8XywHfqQIQiFqbnK7x4R8CJSnYIYMpjTpstrSi9MU2nkru-whbNAjwdQg_hq01HwH3U9i9dPWdpimeDHaW4Q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=aMXkKvL0eumfg95F_zQcuLS_wgR2r8_uelGyWjokbCLYqrFk-UfyApsq-fD7SKuTfL9ronqs9bfVrxDJuFERsF66Kdwhc3aMY09Ao6spmRpcx0yqv_s_7ieN73eZruRWuiOKGRx6o6i1LCL5RhZxIBXQPsEbduko5ychRVN_cpkvc4sLyDeDM4nz_6gs8q1fxJtjJGtO7C_E0_OCON8uP5AwfJPfQ_AgqwCb0NNvXdHNlGIMQqa7qipAs0Wb55QJ8XywHfqQIQiFqbnK7x4R8CJSnYIYMpjTpstrSi9MU2nkru-whbNAjwdQg_hq01HwH3U9i9dPWdpimeDHaW4Q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB2YJMhnU84M4J6CWer0Nq0ELSIy_1wqVYaHvQBNEStoDCvVHVpDlmE4H2Ag5Gv2O237cYdWQGthg8Bb-shtLGAc5s2z2aAvDMIhS6HpNA9deYOKproEtJtInXHEf4yES3dm5XgB13Y9BvLlE_VmQVwO1UhUxSxjk7WuWLmxie7slVKIREcGpgS3FCSJZOCaj2p7ZNzG3ZvOspgGEag6DAXLKSEtInOi-fvb5n-U6mVg35awktpYh3NGIqurDzZwzH4Tp3ImJ1pcOvojrtZoC6c-JivW08QSnrYojgHx3kTkwhPLnSAAhkqwgfp7WjtiEQYUiLu06r5_NdXSk9pZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=Z9arCuSrUmnB5t9erERuFmPqiXu7W_CiF-sG3wBeq7CKeerGtt13EXBC7Y0dQGwwxe4KLFcMuvnnVGWipo9Yh5X2dGNuHjfDVgjEFH1C8cNp0HpaSI_xvyVRzQE-_v1fKEytkiwNT2qW3Z2IYayRV1kUayOWQcRBOAm80zjhs12zhcggLvDewZ6LOu4RWLaOeekHb2pov98ho1U3wsi8iCSb22d1YZPjLZf5H90sEDRW5PtD8d6hXqZ3BS66zFKz7qH_eg-at4ZP5FPRRmnCE2IEA_Ev931ymK61UuF-TGo7V-fjxntlBBvhxV74d91TJtcgpL4Kx0-bst_G5WAHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=Z9arCuSrUmnB5t9erERuFmPqiXu7W_CiF-sG3wBeq7CKeerGtt13EXBC7Y0dQGwwxe4KLFcMuvnnVGWipo9Yh5X2dGNuHjfDVgjEFH1C8cNp0HpaSI_xvyVRzQE-_v1fKEytkiwNT2qW3Z2IYayRV1kUayOWQcRBOAm80zjhs12zhcggLvDewZ6LOu4RWLaOeekHb2pov98ho1U3wsi8iCSb22d1YZPjLZf5H90sEDRW5PtD8d6hXqZ3BS66zFKz7qH_eg-at4ZP5FPRRmnCE2IEA_Ev931ymK61UuF-TGo7V-fjxntlBBvhxV74d91TJtcgpL4Kx0-bst_G5WAHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=emwPFMjBwqGTWa6TE55m5grmmoM4FzeeluVJkE175W1y3qTJQkg3__0hXvV52HguBPuuA4SxFgvRGtPcrvCClahiOBi7n_UMMSVAzIvOybY0HGPWZXBncLHcQw9tG7QatAeOPUaY5-mz2dFWiUTJMUvYrfcnPp0aK5EaDtLrg57x2Ri3iFsLcQC4XzXaEmxVXnlNy06MIvzOxnaLG8byKOrp_sRoFKdptH-InCUG7nFP45Nkp39c_ZDbU7NjdOYqJkapt4knB4ysnC7qbqk4yH_iJ2ul2nj9-X9rHeazVoT9rZKaH4MzRDFrLn0uciP7AFSRe88OJC9YfgICCavM4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=emwPFMjBwqGTWa6TE55m5grmmoM4FzeeluVJkE175W1y3qTJQkg3__0hXvV52HguBPuuA4SxFgvRGtPcrvCClahiOBi7n_UMMSVAzIvOybY0HGPWZXBncLHcQw9tG7QatAeOPUaY5-mz2dFWiUTJMUvYrfcnPp0aK5EaDtLrg57x2Ri3iFsLcQC4XzXaEmxVXnlNy06MIvzOxnaLG8byKOrp_sRoFKdptH-InCUG7nFP45Nkp39c_ZDbU7NjdOYqJkapt4knB4ysnC7qbqk4yH_iJ2ul2nj9-X9rHeazVoT9rZKaH4MzRDFrLn0uciP7AFSRe88OJC9YfgICCavM4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXY71TgbNWtC1d72v8snIi2ijDIlkPXaaf4JhoNE3FkBvn1GMS1AS3vzN3FX6PnYitQL7ma1Xa5Lc8Zt6oxpKhRiIQ7lXffHl_kZA5de1y2yVHCHF_I5Kj5DjrPhF_bc0YQEF_fBR9-dZwgswov7yZd5zJU9VjWLg1kN53Gpgxh37edSe-7efYvEclAEK6N6fc_dahMhAuls7-6E4JpfCMM35CkLltYS3UFZG-2NkOMxtnZ9ajGrDMkf6lS-LU1fqzLBChBSsDdEbaS9IxvcIZKhOTEvU9HGn24M2hKsYUQdiQTaR2ct2dAnFmr615EY3x68QuSBqbqPsWOP2WF9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heCh5ASf4QI_HL8x4rbnbGblbMx9J2UjtW--vqHaVb5d45yw7gap6IR0Er1TbrZgA3DddXL71TqF7f2Q9FjmBHVFNK9dvRoOjU-OxNFXLm5BdAooUZ8q-d1C8H6FkGN97xqk9FOuO_RNcjfPqI3UCTB9L9UrD42-Dq6p2PSoVIe2LSA4leOJPO-C0CgWqj8nJ2y3o_f3O5kr-oC0LeCJwc8iI6st_6CvpNpT7H2gtB859pKdaWlYGiI3yCkDb8awSFTO4qkgBVbcH6dNwD4WHaKofV-P7QsPH9dwFHe6IfzeTR-i1cZJOeow2hxXZkxSr3hLgy4JuY1EYG85sEY84A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=sfbKbhjFT0Wt6foRoPgIXu37H0lZCmRTDS_yI_msm7ufTGBAPkWrM1fCToFJX37wAzs8XCvljS759wdXub3HI9cH5XpnQjb7MmgK2RD6XrpxV-fGu4MNTkjJHiwE8GQ8O-_0EDtgT-KDY3q62XrGAZYyQO8DiKe5BXSCBfNxoeiJ3RDHR7yWwouW_U-gA3gE1v7Hr1wDVfWSKA5E4Q0gx_vNQGwR_n1IoWqGpLDfoBHul6z8iIpoosA5ew3OTH3NA8IezYIV3Las2KipSExHvUz_HxtU2WSNCyD_NZW5j5WuiZz86WcwJN8-AgKo6dpkZtd0pzwfqYnbNEYYtbkMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=sfbKbhjFT0Wt6foRoPgIXu37H0lZCmRTDS_yI_msm7ufTGBAPkWrM1fCToFJX37wAzs8XCvljS759wdXub3HI9cH5XpnQjb7MmgK2RD6XrpxV-fGu4MNTkjJHiwE8GQ8O-_0EDtgT-KDY3q62XrGAZYyQO8DiKe5BXSCBfNxoeiJ3RDHR7yWwouW_U-gA3gE1v7Hr1wDVfWSKA5E4Q0gx_vNQGwR_n1IoWqGpLDfoBHul6z8iIpoosA5ew3OTH3NA8IezYIV3Las2KipSExHvUz_HxtU2WSNCyD_NZW5j5WuiZz86WcwJN8-AgKo6dpkZtd0pzwfqYnbNEYYtbkMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=oYOSof2xpA6-TcIJkE1O2fSlYvL2foVsiJ2kTIaO6WeRol1NYpgavxHYmEkyK8BQ_JStDyX0LDUuILr8Z2JHRiYjuNXlnsJvqTepdO9XO0ELOSsEnS4wDlzCY3UdV83pZfrbPFs6jKw6CGMpNVaXsBe7-3iyXY0hKZJEgXR29CXflVNotSoDutrGailGKOahaplGz6o8e5CiTSwFpaPbCzXLe-R-LbdpaIz0xGc2DjYJzZGGM2hvLeHh4g2X0vJbyzGuOmZgUiGx0J_ag5ow6IllDXaUzFhQoOjQcPy8k-elQyQRF1c2sWnQNoqJl77SY3h475toNpvER0_Xds94pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=oYOSof2xpA6-TcIJkE1O2fSlYvL2foVsiJ2kTIaO6WeRol1NYpgavxHYmEkyK8BQ_JStDyX0LDUuILr8Z2JHRiYjuNXlnsJvqTepdO9XO0ELOSsEnS4wDlzCY3UdV83pZfrbPFs6jKw6CGMpNVaXsBe7-3iyXY0hKZJEgXR29CXflVNotSoDutrGailGKOahaplGz6o8e5CiTSwFpaPbCzXLe-R-LbdpaIz0xGc2DjYJzZGGM2hvLeHh4g2X0vJbyzGuOmZgUiGx0J_ag5ow6IllDXaUzFhQoOjQcPy8k-elQyQRF1c2sWnQNoqJl77SY3h475toNpvER0_Xds94pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=D1jJUQIPCG5sRQX9U3ky-vZ4Mcnua5h864hhqfFOsQtjmfB2ZB044BAjKLLYr7Bx4uKv_KBZjhrCCA26SRT5N3gm2BPets_kijQ5zjlHPzXjEEkdR42K2SnttX56b6BP53NpSnL_5Qatnq7n00EQhRtHYpJR7gTpnUegZ4DzkNba_LlS5on76NlK2hjt3tRVNkMTev-NxMpk1VmzZ0O_1WTIASp1qhTdzekvapJtczgwHYXepS04P1cLs3CUG54UGZhnNXCJqey0lw6uP6n9UPX_D67TwtIDpsfcawGnxQrOkphl2xSYhfwxzq6ezcGst6WRkqjdqxLgkBxoV9NToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=D1jJUQIPCG5sRQX9U3ky-vZ4Mcnua5h864hhqfFOsQtjmfB2ZB044BAjKLLYr7Bx4uKv_KBZjhrCCA26SRT5N3gm2BPets_kijQ5zjlHPzXjEEkdR42K2SnttX56b6BP53NpSnL_5Qatnq7n00EQhRtHYpJR7gTpnUegZ4DzkNba_LlS5on76NlK2hjt3tRVNkMTev-NxMpk1VmzZ0O_1WTIASp1qhTdzekvapJtczgwHYXepS04P1cLs3CUG54UGZhnNXCJqey0lw6uP6n9UPX_D67TwtIDpsfcawGnxQrOkphl2xSYhfwxzq6ezcGst6WRkqjdqxLgkBxoV9NToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4d2VSzLGCKMkxkSmGrlMLjQOxs7ONX4KSkpfEswBqAm3gXeLd-ULFx1rz7lVXkeQZnjv1Ieay2Fc_x4o51Lu919far4oEgT7mYb7jdPCOtqjcnK73xaV24rIO9eyDxRNR52qIWBiKn97RweCk4sVQgoBapQdp7uWD_Gwv5G7HFU4aJd_orXrdq5Dnfqk2bJVBcHkJ6VrzOGaSYu4enJw4Wts8jwo8i_abloE2zGOST7RO_xhQ5QbNRNKS5JNtsLPLQn5oW-I6wf34dq_6ZAM-MpgQ9wkOVQPAr1W0jcWHg7_uGnwGqUAxEC1PrY-NjLvjK7xNMxqgFXGulkL9N5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4L34DNSFjIUg2EJiRAv6xjJBW3633AQVAG1VXnSDUIvS8tIoZjaSJYupEdFHWJnoDP7-5pfrGpMY7q4hpfkAXRdYrIoYkJT7So5R-ODjQ2wygJWSU1AlHNA8SzHuByGiGs1t6o-K8Yop3zUYs_VboEB3cB3TljQZ-TNZ6rcgQ3F6aupiOwGwHCaAS60CxKBYPrkYxqua9rd2pWtpYLVd-zgtHO31JqSneojySkyaVcmXxA73rN6lkvdaJ0Q0oeGAiCZNqKgPCyqvZPtGaQp_nN3tHtrbyAxJRhVI3D6FBad79NDyVV1uI65mgenM01XnvStuzMkuD1LNBKEpZPNMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=huUp2H0Z2fU9a_KbdxJ8FlE6Cv1SttfPkr7l3wZSaYJAXYWNAZgC1MZeDXD1P34Ail6Rlr6Lsn8KTyXyOfwSp-l3hE_pCEahZ3wyae6tfPKXeimhShQoKXw8dnJMyNCT9g6OrztBpzIlfV_y24TL5o9OPYQfgQy2IOICuAbLCm9p3DwOy3XA34EnHQA2aWY8SqswhR9tsuE0bOIXaNYuXhzk4pZbECxjSjTN_S5MUhJIVzNRzBoSkNFHR-tITgPqLOxPSsHQ_N4_1ctXqY3a9JzyFDV9gpeDjsnMMH7snyCh-GAZrYBp1mhvQRINQKL4M_wPtTjIcNDdSFrMYLPa7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=huUp2H0Z2fU9a_KbdxJ8FlE6Cv1SttfPkr7l3wZSaYJAXYWNAZgC1MZeDXD1P34Ail6Rlr6Lsn8KTyXyOfwSp-l3hE_pCEahZ3wyae6tfPKXeimhShQoKXw8dnJMyNCT9g6OrztBpzIlfV_y24TL5o9OPYQfgQy2IOICuAbLCm9p3DwOy3XA34EnHQA2aWY8SqswhR9tsuE0bOIXaNYuXhzk4pZbECxjSjTN_S5MUhJIVzNRzBoSkNFHR-tITgPqLOxPSsHQ_N4_1ctXqY3a9JzyFDV9gpeDjsnMMH7snyCh-GAZrYBp1mhvQRINQKL4M_wPtTjIcNDdSFrMYLPa7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=ue6ELk4CjwzHLtI7BWJlm83dJ8tpVqK4MMzYj-4JUtIBroCUqeUdUTgmHcseEmekcPmDq7kuwEewW4dEW9VDt3uTUh8yjH_UG6JeqQrUWECgcUOkaqzOteZ2mJm2hZbJIGJe5o0gPgvJ9GFEfSc3rrhHaMUd4uA2JZzEqBbK0i-iS4Z8Byskio_VQkmkykvm1URkLvH9pvIATqhG5tREae7vZ2-JvvpVgkjMDN3JkNu86xGi9SF6vn68oc7r3PdoCStqejeDF86SHPqGJyp7OLakQeIw0XsaloB09-QYpmm6vNCYLt1SYhVz7ZLbq_Xtp-j7_2saZuN28q41fHeGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=ue6ELk4CjwzHLtI7BWJlm83dJ8tpVqK4MMzYj-4JUtIBroCUqeUdUTgmHcseEmekcPmDq7kuwEewW4dEW9VDt3uTUh8yjH_UG6JeqQrUWECgcUOkaqzOteZ2mJm2hZbJIGJe5o0gPgvJ9GFEfSc3rrhHaMUd4uA2JZzEqBbK0i-iS4Z8Byskio_VQkmkykvm1URkLvH9pvIATqhG5tREae7vZ2-JvvpVgkjMDN3JkNu86xGi9SF6vn68oc7r3PdoCStqejeDF86SHPqGJyp7OLakQeIw0XsaloB09-QYpmm6vNCYLt1SYhVz7ZLbq_Xtp-j7_2saZuN28q41fHeGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=TlPBSOKLKQx5kxgOOOT8BCBLjOcrk0t1ZuThsegYFtfQE2AoQqa_A5R_9WrCf_v0BfOFz7OaXurGmsSJLGbJnSWKa4YguN-KQ0VLv4SHsUDGa01MmW4OuicOT6_axL2MtKyQw92wcoFm04fHYxgTfZ3HQzEwqJ9C3QAcZKdHEJyOjYQq76E-nCC361Ko16c3_bxiwmSzsyAJwptRKl8cHfCTmk7phIG95MgO6L-OWmAvNpXXX8nBEhNxVpr2qc9yqoZGdsm3JrUND2icmdOOsAyhlGkJ8e0K-X8IkRP1wTpnYJfym3jn2r8wL0SBHmKrIJCkEFADwiDYhejh_FEmew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=TlPBSOKLKQx5kxgOOOT8BCBLjOcrk0t1ZuThsegYFtfQE2AoQqa_A5R_9WrCf_v0BfOFz7OaXurGmsSJLGbJnSWKa4YguN-KQ0VLv4SHsUDGa01MmW4OuicOT6_axL2MtKyQw92wcoFm04fHYxgTfZ3HQzEwqJ9C3QAcZKdHEJyOjYQq76E-nCC361Ko16c3_bxiwmSzsyAJwptRKl8cHfCTmk7phIG95MgO6L-OWmAvNpXXX8nBEhNxVpr2qc9yqoZGdsm3JrUND2icmdOOsAyhlGkJ8e0K-X8IkRP1wTpnYJfym3jn2r8wL0SBHmKrIJCkEFADwiDYhejh_FEmew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=JgdZQxP6-KMuTgjuzbLRcet1sdWOQ4Lisu-H2lS-HdZV22Q4Z_ykS2c4FXuXheeLLwFBkHe3mG_BI7rdYsFePWQVbpTM5Upya32wKTF3eF3cIjY7Su16_KyDPy-hfUmXe7etrALz33ADauY3cUw5IZ1-Dk9kE0BI6H8aWlDfrrMCmjN7QcRRt_m6kbLYwZ5RBwCNQLEP6PnmhCB6WPA0H7eLSzAu_YKfeY2ARfzREu7wY5LXBaSn4JbI1R_YN0NqEEiqdqkS9AJYsGumY2ggEtM0ZWmok97WypzeEdmzjOVYmsMtIoyZZ51bwnPoo_Cr3xqlGmKvEeLT_UqDSFHyqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=JgdZQxP6-KMuTgjuzbLRcet1sdWOQ4Lisu-H2lS-HdZV22Q4Z_ykS2c4FXuXheeLLwFBkHe3mG_BI7rdYsFePWQVbpTM5Upya32wKTF3eF3cIjY7Su16_KyDPy-hfUmXe7etrALz33ADauY3cUw5IZ1-Dk9kE0BI6H8aWlDfrrMCmjN7QcRRt_m6kbLYwZ5RBwCNQLEP6PnmhCB6WPA0H7eLSzAu_YKfeY2ARfzREu7wY5LXBaSn4JbI1R_YN0NqEEiqdqkS9AJYsGumY2ggEtM0ZWmok97WypzeEdmzjOVYmsMtIoyZZ51bwnPoo_Cr3xqlGmKvEeLT_UqDSFHyqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=cBjW_UYlKZl7xfZ4bqSFBsmZypw3jGrHD4G8BuD9hHbbp0qwqm0pMxkGYmWybxyVdUEQio_t3WYZj_7N8iCxQR5xG1UHzL1tWPRHPhg3pkRcplHRJj3eqHyAT19GbfH38oxVHns1oo8hN_mEJx6iW77JFiOcErCdOPxzjmxmUUE8nsi_mF72fhIOb9KxyKyV9p1dxyY7huFClwXyDo_ToSdEJkx6HrEj4oVixkWsgdDHZOSvWNvx8H2_QInNrA2hK6Li9f4vRp8DZ9shvA-7cqzonhfjQ68yy04USU7Cxoce69fBw7u2wmsYYh29hJIs7xcClXsba1ao0Lm-bc5sAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=cBjW_UYlKZl7xfZ4bqSFBsmZypw3jGrHD4G8BuD9hHbbp0qwqm0pMxkGYmWybxyVdUEQio_t3WYZj_7N8iCxQR5xG1UHzL1tWPRHPhg3pkRcplHRJj3eqHyAT19GbfH38oxVHns1oo8hN_mEJx6iW77JFiOcErCdOPxzjmxmUUE8nsi_mF72fhIOb9KxyKyV9p1dxyY7huFClwXyDo_ToSdEJkx6HrEj4oVixkWsgdDHZOSvWNvx8H2_QInNrA2hK6Li9f4vRp8DZ9shvA-7cqzonhfjQ68yy04USU7Cxoce69fBw7u2wmsYYh29hJIs7xcClXsba1ao0Lm-bc5sAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=RbO5ggl7VMxer4Nh8R4MkWp77eyFiypMVrdic--ALlIhEyxtNzWGEakRlCd0Q_4VHc-rCfwu2QJBhueW2NSKeYucpxA9azxs3F5FKL7rpnvsxE_Tnc_mnbx5wWDbAa8lnbx7k5JphKM8M188Kg7V9LNEqOF-zDYIyX2YU4jTlrjuxiosIj8DjVOlXmUCpi63Q5noqwZWYgAGDebJTFYBuo1-wVNVu73oniIAOB_YxeosTFaWkPt_UapmGdBzSblmuKRz0n-Sl2QQJNUESTMXb7CfLc2CW4-miHFXp0W5-A_zF2htqEN5UIF-k7AjwRh9EfCrakNTXTq_bt_jvTWsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=RbO5ggl7VMxer4Nh8R4MkWp77eyFiypMVrdic--ALlIhEyxtNzWGEakRlCd0Q_4VHc-rCfwu2QJBhueW2NSKeYucpxA9azxs3F5FKL7rpnvsxE_Tnc_mnbx5wWDbAa8lnbx7k5JphKM8M188Kg7V9LNEqOF-zDYIyX2YU4jTlrjuxiosIj8DjVOlXmUCpi63Q5noqwZWYgAGDebJTFYBuo1-wVNVu73oniIAOB_YxeosTFaWkPt_UapmGdBzSblmuKRz0n-Sl2QQJNUESTMXb7CfLc2CW4-miHFXp0W5-A_zF2htqEN5UIF-k7AjwRh9EfCrakNTXTq_bt_jvTWsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
