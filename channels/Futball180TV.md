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
<img src="https://cdn5.telesco.pe/file/ivbu0n7Mv2Z2_IZAh8tCO5vklJlEE4Qea1X0sbNWNonKbrj9isiFTxI0r9wWiERXpllwaKh2VQEWLorklr4ueynXoJTRFpNTLSE200IjryBWCz6I2F6MBuQtj_8_ITaG8t0RPPWAg8gPr-1aWJkKwv4lxIPyI592-WC4Jm5dkWwtNNMW3ec_eE0NGZFw4ZcozN2NnSFu7QUHEXCDX1KE88EvdhU48K4RyUMv46QUjOQ1MOGl-5bJJKnegqEI8qTnhvzdoIrPYUcTxcsfg990i0Fqcb3V5CzFzMr4QSDaJTtIdBlCBbrHibV9AjbIWpbUOp7fjjilvmgMRS6haJG7NQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 387K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-108165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=mFw0XBVc3nJPWeuWDXmtqB3xmrjPpvSz8Xbb22cUlblrITLR_FK70zDcthgVKXURo7WMuOlF6coezK83lI2Ij3wc6MFVeMsL_u7b9z2kfVb4PkkM4onb5KW2CUTaF695wI2ybQuLRDNsWimJuIY4d0hgVVizvTrodsbphjeA9FN-kBOOaOV81ucHvt0q_c5YQpzdPFxKKJRxRBnAZulAT5Z38RhE_vx5unjtr8976QJ0QlH4tQ4vcgR9wXzOUlmkynBr7GqbeVOXx0zMu_P9d-zAAnZNCrWozWw7OrHVVo0pU45Fi7FKmalpxRmECDfwjhHoVbqGd5epH2NMGBbyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=mFw0XBVc3nJPWeuWDXmtqB3xmrjPpvSz8Xbb22cUlblrITLR_FK70zDcthgVKXURo7WMuOlF6coezK83lI2Ij3wc6MFVeMsL_u7b9z2kfVb4PkkM4onb5KW2CUTaF695wI2ybQuLRDNsWimJuIY4d0hgVVizvTrodsbphjeA9FN-kBOOaOV81ucHvt0q_c5YQpzdPFxKKJRxRBnAZulAT5Z38RhE_vx5unjtr8976QJ0QlH4tQ4vcgR9wXzOUlmkynBr7GqbeVOXx0zMu_P9d-zAAnZNCrWozWw7OrHVVo0pU45Fi7FKmalpxRmECDfwjhHoVbqGd5epH2NMGBbyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحنه‌گل دیروز ذوب‌آهن به نساجی که به شکل بسیار عجیب و نامشخصی توسط وار مردود و باعث اعتراض شدید شاگردان حدادی‌فر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/Futball180TV/108165" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41de558131.mp4?token=UwF0UvDALdL7Da7DTz5ZDOb2rj43pUbt86wBqh3Gin7wAnKQHPlA9yzhAUPqOBu3OFDqCiueHdQemNS7tD-lBidD5h8hE5d2Os4zhxTV40B3SLl9GszekqXSyjpEPo_Zn2q0CKuyNQioJ17IeedNKN7UKbSGg09buWKeQ0zqufJc2faatwhwD3m-eJHNPErk0MyFkFDEKSmDXHL50OAcEktUdqvhQ_kxb3Fj1Jj8fLBJ1bD_naik4k2LbakfvCWNw7fg0r9mISqCCvs5I2HuU37XF-V3W0LCktfvpu9rRlxC3k1_41b1Tw0jag9cfAL_HtDqL_sAo8XEiHLz2oM1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41de558131.mp4?token=UwF0UvDALdL7Da7DTz5ZDOb2rj43pUbt86wBqh3Gin7wAnKQHPlA9yzhAUPqOBu3OFDqCiueHdQemNS7tD-lBidD5h8hE5d2Os4zhxTV40B3SLl9GszekqXSyjpEPo_Zn2q0CKuyNQioJ17IeedNKN7UKbSGg09buWKeQ0zqufJc2faatwhwD3m-eJHNPErk0MyFkFDEKSmDXHL50OAcEktUdqvhQ_kxb3Fj1Jj8fLBJ1bD_naik4k2LbakfvCWNw7fg0r9mISqCCvs5I2HuU37XF-V3W0LCktfvpu9rRlxC3k1_41b1Tw0jag9cfAL_HtDqL_sAo8XEiHLz2oM1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
هاشم بیک‌زاده: در تایلند اتاقمان کنار استخر مختلط بود. دستیار قلعه‌نویی نیمه‌شب رفته بود لب استخر و دخترا را دید میزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/Futball180TV/108164" target="_blank">📅 11:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejkG0_eruPtbpjRIbpPhsW7mc8Z-WDudMwDY4WVpoNZKGKgnsA8dSs_U1xSiCITby6mCSoLowJcXRtKoUySQPnIxk8_v4A-FQ-PY1d8xMIm2CIuy13TD5p4tHpyjwZfXTnB1ZUzand963jhQWfouJRXXgm0nVfVlY5miz3ICq9TM4Skw5IO6ynpRdH82v9Ft-uJTI8y3pLESbBrn0slOqh21bVXRLe75xuL4pRAMeQdNHXxwGp3gK3kMpkmTAYCqgy37GGmH5oGLjxjPddzDON7OTckdVTdWEmgogzPWonKaisD_sPFxL8TmZxek82DTewRf4QLIW_4bTmNXxQZogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
علیرضا بیرانوند اعلام کرد که از کریمی مدیرعامل تراکتور بدلیل اتهام تبانی شکایت می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/108163" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b39729529.mp4?token=FoB4syqV9xcIR5MrS53IRSeYkwpQz68_0DBzjlEpSrhZqh04nA1bKU-FGSHn3H8xJcoKy4RS04DyaeQ3i2gwbJzWMgG04dcyP4IBJYDdkpkU3S8Tz1u9dpZfzMQyy2TjlrruYeN7_Y4tG6jTGqU7GLKtPii-OXzD4U2CZLzo9FRuzxGcR5stEWX-MoClwASCwRuKrEov1XDmg_V_vLTesDCAT_mLtYfH3DF0wXnb6JcLuMzKw2VQzBuCOE38hs25n8eKWnYyEuYDtLiLK-oZ2OC7_GZGfmImpI_Mg8sI9_DXDrQ-qryJGJYMJHL8d4357IwRMSJJkoKWSpq4sjFxZ4nErPWvvhHs7zfi8A0mhZNvhJnv1HHJlUtf1E8F0T2mI9-I11D0dDT43D9TYkyZUJ-GAGgGzPExGON2rUjnVXnRrtDmRMxmWeSLdAaVrBPKSiqgrsrhIGYvy4ogqs-xAYo6--mMprnZwCmkYvHNEe_uzhCyjLIr9Uwj_jvaN1Qd7aXof5Nq9GnwBl8ZJEIoh3Ey-Oxsrc187-Kuz6biZ2PlurpfCcZYdqamns96x17wHxz2sqzn3jE5keHho7o3DmdU5DG6_KCSPCO2weSVsHIIxXeq0-79REpxNTLEm_Hh9qFVdZJLUVf-av1d35sM1P9gQvmOtYQlu1FgcW0npYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b39729529.mp4?token=FoB4syqV9xcIR5MrS53IRSeYkwpQz68_0DBzjlEpSrhZqh04nA1bKU-FGSHn3H8xJcoKy4RS04DyaeQ3i2gwbJzWMgG04dcyP4IBJYDdkpkU3S8Tz1u9dpZfzMQyy2TjlrruYeN7_Y4tG6jTGqU7GLKtPii-OXzD4U2CZLzo9FRuzxGcR5stEWX-MoClwASCwRuKrEov1XDmg_V_vLTesDCAT_mLtYfH3DF0wXnb6JcLuMzKw2VQzBuCOE38hs25n8eKWnYyEuYDtLiLK-oZ2OC7_GZGfmImpI_Mg8sI9_DXDrQ-qryJGJYMJHL8d4357IwRMSJJkoKWSpq4sjFxZ4nErPWvvhHs7zfi8A0mhZNvhJnv1HHJlUtf1E8F0T2mI9-I11D0dDT43D9TYkyZUJ-GAGgGzPExGON2rUjnVXnRrtDmRMxmWeSLdAaVrBPKSiqgrsrhIGYvy4ogqs-xAYo6--mMprnZwCmkYvHNEe_uzhCyjLIr9Uwj_jvaN1Qd7aXof5Nq9GnwBl8ZJEIoh3Ey-Oxsrc187-Kuz6biZ2PlurpfCcZYdqamns96x17wHxz2sqzn3jE5keHho7o3DmdU5DG6_KCSPCO2weSVsHIIxXeq0-79REpxNTLEm_Hh9qFVdZJLUVf-av1d35sM1P9gQvmOtYQlu1FgcW0npYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
صحبت‌های تامل‌برانگیز مجتبی پوربخش درباره میزبان دوره بعدی مسابقات آسیایی سال ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/Futball180TV/108162" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/108161" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Pd333Wat5cebok6-ymxc30nICVjYTqfBaf9qvlH5gQfLwX_9E6DRNUyakjlInN1ietVHGeTDF3fq3V_915NcorzpwflnE7MxSu8R9_tBBmMpa5E9CzBckcm7L0fdu0WzEpUQhcn3XYE6QChEGn1RV6F9CmB5chJrSXsIf-wTjGDhPiq7RKMx0YharSOVSVMWKtYuEyI0-A83aZ2aR8g67sii5VNAgKuL-iLiRbmHySOSFbtb8_R0J6rAZUD32SdRDFuppGQZnMB5AE-ezgANlqY6C9UW2wRtp5jZZYjhuWNDUImTnse4JIveXceOWPObz-e-OB1viSf4MI1GvBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/108160" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
🇮🇷
فاطمه‌احمدی ملی‌پوش تکواندو که در ناگویا مدال گرفت: شدیدا طرفدار استقلال هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/108159" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hIBN49Pqc17s-DG2aC8B-qJCw8ccxifupRT03zxmSw1Y8PNEZDEkc5L9dQXYTOyUAiqv10lS33Zhii6bZ5l4HzeMYdRCOFzY7fwsN2LIWfKeuQC3FRLkK7TDpUWBD0Rt_Gff9WrTkJIhKAKRdBWIJQq1nOuHPjscgM8_yef3J_Co6sjfI7BOMkKvFcUWXBulb0gvWFllBIZoDK-5FIZTvlLQo0KryMS6wYzIgzlpFTotz-QsEDgewl9gJ5n-zTh48HlQHQI7ybq_MYIL5Xm2QC9pS8_8BXB4sPk7l-yGC5oscpk6yRizwnZXn86ZCl8hnpUFiazidqF-aIW978DULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hIBN49Pqc17s-DG2aC8B-qJCw8ccxifupRT03zxmSw1Y8PNEZDEkc5L9dQXYTOyUAiqv10lS33Zhii6bZ5l4HzeMYdRCOFzY7fwsN2LIWfKeuQC3FRLkK7TDpUWBD0Rt_Gff9WrTkJIhKAKRdBWIJQq1nOuHPjscgM8_yef3J_Co6sjfI7BOMkKvFcUWXBulb0gvWFllBIZoDK-5FIZTvlLQo0KryMS6wYzIgzlpFTotz-QsEDgewl9gJ5n-zTh48HlQHQI7ybq_MYIL5Xm2QC9pS8_8BXB4sPk7l-yGC5oscpk6yRizwnZXn86ZCl8hnpUFiazidqF-aIW978DULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
فلسفه جالب نام فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/Futball180TV/108158" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=VFExk0toVnfBXY5KbCcFJebt7H8665DCmdZIoGoyLlE142EwULd-zUMSx7_u6hGWOf3dUIpDeHYbA550vASjSeDxNOS7cIWqXrrLDFPQy9JDNGLIaPbAIRFCd8gRbwyXA2ARcJhakbaZoN9QSnDhvM9LgsBOuBndi_kiNZEpUCuKSnB_l93XVK_VXu4spKaYVR8PTp--A4AYw5DmNp6Zi9_d05-sgmYBKPm3It56cxuVcaq-pQaxxbWIuxOkPOHxd0wXDzuMuASxjaDFmzA9_2yKjwL3m4ho-ixDpYL3GrD-b68LYtTWbu0l9Glp26XiaGI0nZ7XN7XnvI2BwAXuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=VFExk0toVnfBXY5KbCcFJebt7H8665DCmdZIoGoyLlE142EwULd-zUMSx7_u6hGWOf3dUIpDeHYbA550vASjSeDxNOS7cIWqXrrLDFPQy9JDNGLIaPbAIRFCd8gRbwyXA2ARcJhakbaZoN9QSnDhvM9LgsBOuBndi_kiNZEpUCuKSnB_l93XVK_VXu4spKaYVR8PTp--A4AYw5DmNp6Zi9_d05-sgmYBKPm3It56cxuVcaq-pQaxxbWIuxOkPOHxd0wXDzuMuASxjaDFmzA9_2yKjwL3m4ho-ixDpYL3GrD-b68LYtTWbu0l9Glp26XiaGI0nZ7XN7XnvI2BwAXuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه ابوطالب به نحوه برخورد بازیکنان آرژانتین و پرتغال با لیونل‌مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/108157" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=HfdXzYmddOi6vgwyq-hfMMi4DVe32rJutl9Ov3zP6BnmCA8ef4p_qSUOxyfQmVqhTKmddINaIZrnykdOMIKMkpDiAYFwk7r_uMxG04ZtLOnEO0Bhe1DG-OVsKUbBRMt7qT3lLEB3tR4rTChnGaOuqpC2oAUh1y1U1-rQ-8P6L4M_w2YhlkB82OlR4eM06x2AjDJcKSSwhmDQLyoife2t3XQyoNPXvcwM-oGOT_7d_TvtKNM8OpR3v_1plOejjYs-2MBJg3yx8zas_q325QH_VJnqcVTli-SjGI-_Ivmh6duo6jJCEk6_hcqXgcUsun9r6fnBGw6B8SyCRE1aoEoJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=HfdXzYmddOi6vgwyq-hfMMi4DVe32rJutl9Ov3zP6BnmCA8ef4p_qSUOxyfQmVqhTKmddINaIZrnykdOMIKMkpDiAYFwk7r_uMxG04ZtLOnEO0Bhe1DG-OVsKUbBRMt7qT3lLEB3tR4rTChnGaOuqpC2oAUh1y1U1-rQ-8P6L4M_w2YhlkB82OlR4eM06x2AjDJcKSSwhmDQLyoife2t3XQyoNPXvcwM-oGOT_7d_TvtKNM8OpR3v_1plOejjYs-2MBJg3yx8zas_q325QH_VJnqcVTli-SjGI-_Ivmh6duo6jJCEk6_hcqXgcUsun9r6fnBGw6B8SyCRE1aoEoJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معلوم نیست داستان چیه هرچقدر هم ببازه بازم از فدراسیون پاداش میگیره
😂
😂
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/108156" target="_blank">📅 09:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
🙂
سرمربی فولاد مطهری: داریوش؟ گرشا گوش می کنم، وسعت صدای ابی را دوست دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/108155" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=JoIBleiCCRYLw5dwdtuUcQxAJqhzcyuV6gjzkz9OzVpWIKI3qatpedMLzedu7C1cI_jputbEzb0ax33_OIPYM3M_xhzL8v6LqHDjJnE07xqP9dLY4pFojguT0tn6nwH97Z6-YHcso9N9dALgO0N5d7RHerZop-lDanx_haqbeXcl357UQiBxd-di-uc9syYX0wdchS8CXbsDri0AsIp5nsiiCzgNaFCCOuxPU7-YZdq35YJSlPqwrF0GAZ7_H8HgpM97vXQblCpZ0bdl9PjxLkIxrYnhY8youaUiXZvsT2YNgBcdxwp3dLinFVntkSFLsGG7Fvp3Fc8MuMMQD9fhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=JoIBleiCCRYLw5dwdtuUcQxAJqhzcyuV6gjzkz9OzVpWIKI3qatpedMLzedu7C1cI_jputbEzb0ax33_OIPYM3M_xhzL8v6LqHDjJnE07xqP9dLY4pFojguT0tn6nwH97Z6-YHcso9N9dALgO0N5d7RHerZop-lDanx_haqbeXcl357UQiBxd-di-uc9syYX0wdchS8CXbsDri0AsIp5nsiiCzgNaFCCOuxPU7-YZdq35YJSlPqwrF0GAZ7_H8HgpM97vXQblCpZ0bdl9PjxLkIxrYnhY8youaUiXZvsT2YNgBcdxwp3dLinFVntkSFLsGG7Fvp3Fc8MuMMQD9fhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
عاقبت تیم‌گرفتن با رانت و فشار بالادستی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108154" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108153" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXn0gG-Q6XNyo4EHgflH35smJWQgvz_gNng1G_6SvkhWyCZIweOO2rTqM1U46xMcy91P1u7gkupAvJLJjFB5M4Kwap-pOJDksXx_BfyXgVIsA1C_n9iC37-1B51XxhPG5SZYki3vMVim4JClQxQfjIvElbaqIcmGKE5PHGRBfa7r1zqavIbgyj8EnJ9xCJrVIT8arCdPVFzuhaWhSXtHGeD9xbyn0xIH8y-dq1wF4NWl9bl3wRO69hKsgf3NLN85usuKNbd3jGNdfFx_R5izCpzqG4Aag8uwYfMM3KMGOXaJJG7W_HTnT0ZkgXTSBtRMmsh1IpShv3j_tMMCvuI-CQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108152" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCy6U4IO_c8lb6U3AuuCjgxg3Ijj9YgXIgpYt5ww2iBDljJCwEuCZp_eTsOuKGxhVUsvu591XM_RzJRHV4tmr2qLGKapeEaf0uiDic_HWagu8VlDSIkzdL9hbT-jn-Qt8KhcLEnXkmfoAY_12W0f2Npn3J2MP0NFEq3HJGXBSvIm6J3FByYQc5Cru3gZGdtAJxVU1iBZkHyGKt_sZJWVFaXkOw7iEzj5VVcKVxD1wbECLi4utqidR7R-67NL74L_OFagcNq7JKyq4u8DWx15WU8R7TtUQ4MdNb189wkfW4xUx6sFAVcTTJjP_jYc9JiU96Z39Gqw1UScyH53BCTMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇶🇦
نتایج ۷ بازی اخیر الغرافه حریف استقلال؛ 5 باخت - 1 مساوی - 1 برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108151" target="_blank">📅 00:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=vCWhK4fRxaayTLotMvO0Q6HETBwVWv8wk-3bzRqzQD_VtyfLhuyOo1x_vF-GFyCEDSZsQANx6JGjyBG__nnoTkuNwFskDYcoV4Ge9OTbq-x6K0UrB7Yzx3lHmplIrF2IUmIVjFPlqmAw-YlqVl-WRhxjsGeAID_SZZVz_rEm8tPXpIgl2g8dtJN8noLvZfypcG5POlfG5MHfaTt2Mzq99fvA_7a0W6zDiQB5USZdMyzODVTBdPVr3v5B804sqqM6xh2RoABc5FVpe48I1AqFFdEtW64hkNNnQvtlN-t9HhgrBmyH1IohjwyR_NT_HdqQvmkAbVd3g2-5JBYix6RVUFQFQsOcRCq-eflO__1Gnd8LAwlISMzNZ8FUxoyVIYlO1A2JZ0sAeb3Ygs5TxMgFtvnjLszG5yyIp6J1-BCshKtsBBmowFiML34uTkZbPzzqXSN55Ai4Ikmmw9fpsHB9eRc7QMWJHIL4-0t7HFqJzeZ9y-eE1htxePcM5v41joXiV8ZJqCHcLPMzAjz0CkabSCp4lg5pjNfERtDbwhRpuI12gPntrNhWVe2wLzj94bY4JTGAER4thvDJk0MC7qq80fPR3qLNcZSeR6p3cxMVKZ_Q9aXDVLeHdUo21b2Ygao3najlKd7AkAjU6A1JIDRhn-_jwFME2B67iHpJzbdrN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=vCWhK4fRxaayTLotMvO0Q6HETBwVWv8wk-3bzRqzQD_VtyfLhuyOo1x_vF-GFyCEDSZsQANx6JGjyBG__nnoTkuNwFskDYcoV4Ge9OTbq-x6K0UrB7Yzx3lHmplIrF2IUmIVjFPlqmAw-YlqVl-WRhxjsGeAID_SZZVz_rEm8tPXpIgl2g8dtJN8noLvZfypcG5POlfG5MHfaTt2Mzq99fvA_7a0W6zDiQB5USZdMyzODVTBdPVr3v5B804sqqM6xh2RoABc5FVpe48I1AqFFdEtW64hkNNnQvtlN-t9HhgrBmyH1IohjwyR_NT_HdqQvmkAbVd3g2-5JBYix6RVUFQFQsOcRCq-eflO__1Gnd8LAwlISMzNZ8FUxoyVIYlO1A2JZ0sAeb3Ygs5TxMgFtvnjLszG5yyIp6J1-BCshKtsBBmowFiML34uTkZbPzzqXSN55Ai4Ikmmw9fpsHB9eRc7QMWJHIL4-0t7HFqJzeZ9y-eE1htxePcM5v41joXiV8ZJqCHcLPMzAjz0CkabSCp4lg5pjNfERtDbwhRpuI12gPntrNhWVe2wLzj94bY4JTGAER4thvDJk0MC7qq80fPR3qLNcZSeR6p3cxMVKZ_Q9aXDVLeHdUo21b2Ygao3najlKd7AkAjU6A1JIDRhn-_jwFME2B67iHpJzbdrN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
مارک‌کلاتنبرگ کارشناس داوری: هیچ پنالتی روی یاسر‌آسانی اتفاق نیفتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108150" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108149" target="_blank">📅 23:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNfLNrh36DlQhHm4s-ZefhO5rkaFv1nlglUYM3TzF3UPml7e3Uv2gH9jor-n5pE4fjr0gKkcAZ0urH6wZGVxeRVaa82Lf_lzhAW3IPAheMvUDwaQ3SFZplrc751MGBw66ZIYmp7j_T6u6gsUd6h_8-mlGnLMdImdS9CNBNi_-EkVA-x5Kp6VSNG6n1uTMd8nNLlcZeqj6v5ZFQuf-P93olkkKosKa0CoxVB4uHpsrZXXs8aTqnreSM8R9j2cvkCsDUHh6TvbCe2DLQE9oCj5aU0UJ1c6YnNus9rrlIKOiNwbqvvJKD4bVk5503_mloHpYaDjAjBTprBmpoYl6_96hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ مایکل اولیسه تنها در صورتی از بایرن جدا میشه که به رئال بره. اگر مادرید پیشنهاد جدی ارائه نده، او احتمالاً با بایرن قراردادش رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108148" target="_blank">📅 23:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StX6d2NrQ-tMoH2JJ8heXyXcKEPPk_S7IMknwQbf8XggarCVucksTHsroaQq3EAlZNj5zlpdY1ISBOD9pUjJoTJToNoNQkenB0i9dAELyIFxbogscZJr60W8zjKzw7qExER5VjMgFxY4kiTtKD-0nFH2aC-hQMghS_KLmEh9K7GhLWLwSE_oJKpA-kxSfuLLc2ZeGppqulkDnx2fXis5pRvu0l7kE7TdATY57T53TY3cKHm0kj5QIhiZyhzKA6iP8K4_uSqAFrdusfWO62Xn9t6pTX40Y0jJRN3asidwiDE_Our1-0-njqgDoE3EFBUcI6s1vlWbclJMwJnu2jZv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108147" target="_blank">📅 23:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYh_BliwMFUortAUWJXvVVDHy7KTwYe6lRxX4XIkfFknveS_Bou656imT7oE4GbnFeq9ytXbAWgBmBVL96MTMqmO29vME6PBimsoS4JPZaPUoKQoJYtkHHEZib_s4xzpQ3uDfPgSEejeeDHoi1t33mFGtEnxwb9yjA__W5XNR0yfRttVS-HRqIpnxiWh5nkmPmU1CXePG0cD-NQfG86e7b4505X84rDSk7w1RlQnP6CUw5Qpm3h3Ayb6xBVNddI47kmrLSzHgIVbTgJPJPFYSWixY3UzlOp6s8R3jpEoz-D3I2KMX2movbNA_VUK0Aux9y2HI0B2CeMzoERBLT4fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108146" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=voBwjB9dDkfElbYqP13V_dCaDu1wlMnMWvi9qJ_qg5v8mXlSAR1r4Ai0kTHeo9fQ02gXrTvUau90o_Y2TBaPXLfCXsB78MJcyMA_SFV6toL62P1vBoi-tI0BO_0BgXkoCzMlVnLYLay1KyMdQyyBZlBP0LeklcNn2_0mhk7ilN_TZVDsHom-VeV0iVCdL_cYw1UpcIZSw7oBYGaOG_P5yadm9FiJyNbzORCGqcSsU_8RUhTl34ubgyIQNwn3VCxqYxKYAjdOqLo1bWF9TRnWgsXzLnoMERvFP0IEulnaQ2O8MtjA2WROO_DymcDmQmvkeB6KKOS3bHuKvPhuWAFEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=voBwjB9dDkfElbYqP13V_dCaDu1wlMnMWvi9qJ_qg5v8mXlSAR1r4Ai0kTHeo9fQ02gXrTvUau90o_Y2TBaPXLfCXsB78MJcyMA_SFV6toL62P1vBoi-tI0BO_0BgXkoCzMlVnLYLay1KyMdQyyBZlBP0LeklcNn2_0mhk7ilN_TZVDsHom-VeV0iVCdL_cYw1UpcIZSw7oBYGaOG_P5yadm9FiJyNbzORCGqcSsU_8RUhTl34ubgyIQNwn3VCxqYxKYAjdOqLo1bWF9TRnWgsXzLnoMERvFP0IEulnaQ2O8MtjA2WROO_DymcDmQmvkeB6KKOS3bHuKvPhuWAFEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
در اتفاقی جالب و زیبا جایگاه هواداران استقلال در ورزشگاه یادگار امام به صورت مختلط درآمد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108145" target="_blank">📅 23:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOOTh_EHlVrMPI-pwjQnqJYlewVpPYxJx9yXNFLoWygbUnx_fn9exHomk0jjtSpyDPm2Y2gC-8czR-XExssbs2Dyy-leDcBosr28Hf3ipa-aZaprpacCBdrdzeKhbMo4dvIJMSevM57Ie603emLp4q-HmverCwOfBQfptVGxvsd2AsxiKrVe_6k4lZ9DS_bmVqJhAN44Q8mAJF_7NF2UF5qV-gjAOOV4Xod9AMyg32m8JlcJZa17jbYmd8whvrFvN3VSgfPbCLb7S8OYU5bzVyb4S02cl4BS0VYOi2Vvo-NQm0nHeWBOu_a9X7dvCNVhb6YdWuIGBHRhmYDlGx049A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو در پاسخ به سوال درباره رابطه‌اش با داوران: فکر نمی‌کنم مشکل از من باشد. فکر می‌کنم مشکل، بدشانسی و حضور در باشگاه‌های خاص در مقاطع زمانی خاص بوده است. من در اوج دوران نگریرا به رئال مادرید آمدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108144" target="_blank">📅 23:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCDcw_gmiZ4511SA5QjpkfWx32N-3XR6z1HvnMuI-fJJgBnxzUjGbxFeTs-7lG_H9T1qyVVLQG9K20Mk7GnYMFCjOWvE2Rk6jeqCuzXLo15vS7V8JPtvC9HMSLWlmad5hf0JonVD98gnyJ1WWjDpEPfoQNEfvo1EL-dpLYPIXRJRN6V790fIxWaBpDwM4Q06VDY4HigluY5DNLytzdAxgM51L5OL9UcJMYjH1Ts95lmmJQfvUt_zq6N4_MT4dAA7GJ8auWdtkcN2J8LJtzb1PZRBjydbIcbVLVeH_yGWWn7eSj9CS5Hkl6oEwAliX8n8ojdrl9-rkGDwyd8YCkLa3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108143" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFIQYDzIjBtCkk1LXEVPXaiX13FzHT8mVcbv4-2egYzrO1OUUYHgTYbxtB6M9Bq2LDomZjGjO25I1zFYLifAGn9DPOkQo2K-D4a4zvXViS0GtMnP8hzf2UKQsOWAereAFjJis4q1GuCPIAZgRKfpqckSKtMiGt7jInTWj_j_-4HI_1teYdHyRb_cDqdcWgXj3IQe9EcjSh7d5sgmC7cLeMUp_LD5NqVqOkj6-wnKGQz4eKABxZudv8mMH_ExJZe9gdUWqAVLM7gPyriZfzfW4V6-taGxoSh8CorqOMGgtaj0v9swPILtP_wRhpZ6F_6GJIRrcc8fuevr8EGTSYNg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد ژاوی اسپارت ستاره جوان بارسلونا با این تیم تا سال ۲۰۳۰ تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108142" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRy2hksU5RDEdrqEMKXBXlrV_9GUPgK9iuoIBjPofjlqfDmsbWSNgi4Al8Kft4Na84y_XWC85ezYzgKGcWzV71IDrpz-ajBuSXC9l1MJHNs2f4NdhU5NPCJ-gyVL7f-n0RdeDXNlDB44829v8XW2vfLWrDIeqziAjQEhsDK_GDVq1zDVmGqMO2vaaJpk2b6t4BBQ34Zi0Re2AAKb2Sa7iKIYpkHKwfpPvHLMdDHxLFHajB8FEOO65_oNzDpjaFPDlKHzkWm58ZtK3hst0hcnrD81ooT6t7TWykzSofobaJHfVW2nXSmMyaV7PXMXrl4OnbMK2t3jyj3_tiE0icASPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108141" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQi44-ojU8-fT9A81ZiRSXxKVnTyWQRDyFObiNG3FA_IpcT0o3ZBBfGgPmSJtt48_jlMnO8tB4EfO5Tox8wLqqN1QvM7QW88-JQZ5oWq3cSZrSvx1xrHUOxuVQBXwGw5zJzV_pzd4wwrz4h_pJFbGNLP29KVKiPklJ0AsmORYzOfmGBJpMFPEBxKjbIYbfKaJF9oKd5A296bYlrqTBSrfqfLpom-8leBeQvRViOA8-40rwTC6nviaJWiQ2Ooq1dU9yi9yWaBXMnlUhUUoJwY1Hu8MelC5nwrljdwtfyvQ80_si1skdEFTivH7hncRdzLcRoRmH_O-DjL61s8X-7NLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108140" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14105f8264.mp4?token=M1i-MI31BDy387z7zLRdPjFTxSNxe5u8DgmmZZjVLqT1hX-3hrzTlQA_E60Xt-8UbKG1g2Su-w0_swUW4Bi_7D-nhneY-XaEf0TA1l5D-J130UYJRUBvz2ouQOtGeb5_PM0Fgil8_yALocgrtNQkgDae1YR5pigOphLKe44doi_o8VAPkt9fOq6Bxwwwx-CkKZ319xPrqnsWd3ndIePv4ZiFa_C0-oasnjfa9j17cXgwsI32UlD5gvyIql9QtR9c9AtN0F8Fx1BSuftiximLXOWutgYlOHuLIkkiwzknJpP_8r2jCN-HXASeIOFEKW-ZO9xJKtH6qJReS3w4_5ujrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14105f8264.mp4?token=M1i-MI31BDy387z7zLRdPjFTxSNxe5u8DgmmZZjVLqT1hX-3hrzTlQA_E60Xt-8UbKG1g2Su-w0_swUW4Bi_7D-nhneY-XaEf0TA1l5D-J130UYJRUBvz2ouQOtGeb5_PM0Fgil8_yALocgrtNQkgDae1YR5pigOphLKe44doi_o8VAPkt9fOq6Bxwwwx-CkKZ319xPrqnsWd3ndIePv4ZiFa_C0-oasnjfa9j17cXgwsI32UlD5gvyIql9QtR9c9AtN0F8Fx1BSuftiximLXOWutgYlOHuLIkkiwzknJpP_8r2jCN-HXASeIOFEKW-ZO9xJKtH6qJReS3w4_5ujrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108139" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108138">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMlZ3-yicbqXs4Hbkz_gk9mfYHKY-lmTmcsXE93dzuRpq5fItvr2xVAY_ZFJjVh7DZYrKajMD3gcHD4ZT-WZhpxYKtG3k0QhRTIA3cyYJFKHWEFMWLxhMZd2aVnPcVIq9CAYWt9BE3yq7D_v6mL-A1QdqIcRaDQxyKRSQz9Jz7Mo6uV7zhz6O9KOpMMMpNL_n8ED0iotl65N71j-uXUr-1r7fpSVQtIB6bJVcnYj-e6IG1OnsO_0c_UhkCk2cEsggk28Vb8crCTlpDSglSwsuQLKJODGGlAyeDhP4EMVXiJllXTj4LprGPDyklh7w4EVYcgX2UVOMjq9I11NCyfjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
پایان‌بازی؛ گلباران شیرازی‌ها در اصفهان؛ نویدکیا پرگل به استقبال بازی بعدی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108138" target="_blank">📅 21:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846f23996a.mp4?token=qAZYU-n4QCLN9p3MucUAG4s1UZNNdQvNYNjQ7424WR54ld6CXBl6gAfodyxBxucinBZR8YsV-o6Qtz0MpYsOWqFri8mcXppOfPKNzFu2u0j2QdbOC0S3M3D5M8qH8nPVddc5YFTFVWMpCa5apK7BVrvK7SLbwHUqY6f-zSt8CGHGUUVPvD4276TKnoW_IzCbly1F8etyQJ4ynlfSkKcc5zeCgmOEwlyzPE-QInk2Y8k7s93Lx5UTMLlLk--NxpbqI7-JLeMxGwrSBy0AYp4QFCx7fpCH5aFT5arIgx1VE5S-OxCjtkxEVzm34LhywciSHm8R1lhDaglqL1If40m81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846f23996a.mp4?token=qAZYU-n4QCLN9p3MucUAG4s1UZNNdQvNYNjQ7424WR54ld6CXBl6gAfodyxBxucinBZR8YsV-o6Qtz0MpYsOWqFri8mcXppOfPKNzFu2u0j2QdbOC0S3M3D5M8qH8nPVddc5YFTFVWMpCa5apK7BVrvK7SLbwHUqY6f-zSt8CGHGUUVPvD4276TKnoW_IzCbly1F8etyQJ4ynlfSkKcc5zeCgmOEwlyzPE-QInk2Y8k7s93Lx5UTMLlLk--NxpbqI7-JLeMxGwrSBy0AYp4QFCx7fpCH5aFT5arIgx1VE5S-OxCjtkxEVzm34LhywciSHm8R1lhDaglqL1If40m81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108137" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d21db945.mp4?token=EQfuptldg6s7SnbKJRR8-pW0O2AQWJZNO2bB92cykFN7STvusKURW4luwsjn7ScIa2YChQZbX6I084owwgz0SYsWpWxAZAEPdx9WQ6gieKRTkCUUqroDuhJ7uHJOzzyUo49SuIQB4ym7Pt6tzrmUTxAHTAdf7T32Uxici9bVW6CTTBPcK0AmXNY6ntCaNTKwe7FMsdGLxTJCnNCgX9Qhy8AQYGWWNVMwZqpP0nkuZwEDYEy6C0jGKTDSztN4Jv-NR-9Z3EgCWHgh1BcOgXmF-Isz_f_1HRDpAlAqmfRgjTjMNjPHMrFMRWY92eRauxRzyp9WKLVWzhBM8_ar17xPXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d21db945.mp4?token=EQfuptldg6s7SnbKJRR8-pW0O2AQWJZNO2bB92cykFN7STvusKURW4luwsjn7ScIa2YChQZbX6I084owwgz0SYsWpWxAZAEPdx9WQ6gieKRTkCUUqroDuhJ7uHJOzzyUo49SuIQB4ym7Pt6tzrmUTxAHTAdf7T32Uxici9bVW6CTTBPcK0AmXNY6ntCaNTKwe7FMsdGLxTJCnNCgX9Qhy8AQYGWWNVMwZqpP0nkuZwEDYEy6C0jGKTDSztN4Jv-NR-9Z3EgCWHgh1BcOgXmF-Isz_f_1HRDpAlAqmfRgjTjMNjPHMrFMRWY92eRauxRzyp9WKLVWzhBM8_ar17xPXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‼️
🇮🇷
واکنش نکونام به مقایسه خودش و اسکوچیچ از نظر هواداران تراکتور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108136" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Jokar8RcXo-MGmAEn1MKMKmycqNbCYJ6c1VVR0fc15rpwP6P-wn5CRnssGwt2Crm0zR6q49GatBqNSqi_6uzJs6ZBiKmKwDMhD02uyOOkBor0qTJC8fPMreYF_tNYnodWfuFZYQeQwAnH0pzVaxHmePYiUuURC86FBSOSXuF0DFu1GuS9ce12cpBRQqpOamsv3pjueA3chs9F3xcsdyg_Ivuq9IyQOSoyvEM6iaayUjJ7ToeiGQKL3SpP76uvbvuT33JcKMGT_NRKYU-MJLUTfT0p-mKjN-S94lB2Q0M84AyEthiePj-FA9RelvZJwgFKNfzWQGvE8uLsii0t7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108135" target="_blank">📅 20:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=vkM9-un5eegeUwn_Nvtb-KfNB2lhkiZ6ebdic8FpcVt3moRvnxpfeMa6jZotGXOqiEZOOWbMOJavil123ZgRLuQc-4-igS9CHultLe7iFNUXBZPVKRBV3r5rfsS2GZtcLvPsR4LKKfvBYHvEcnlK6YmZBM-iHlr6DekUfFIJPjZ7J8I-k9qHu_DEVZupmMH1HN9tXT3einoKssao6Me_wCnh3J4CkW6miyYrKhCvOZEiTYBxlcF82K2ZLbLg6CGm-SMrEksLK7OY7oAMbq42GaMMH6m9eruJSQVyexGDBY28rYd0io3NhC0d_fUOV1yaQyHXiJlLinMDN-XFBN8PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=vkM9-un5eegeUwn_Nvtb-KfNB2lhkiZ6ebdic8FpcVt3moRvnxpfeMa6jZotGXOqiEZOOWbMOJavil123ZgRLuQc-4-igS9CHultLe7iFNUXBZPVKRBV3r5rfsS2GZtcLvPsR4LKKfvBYHvEcnlK6YmZBM-iHlr6DekUfFIJPjZ7J8I-k9qHu_DEVZupmMH1HN9tXT3einoKssao6Me_wCnh3J4CkW6miyYrKhCvOZEiTYBxlcF82K2ZLbLg6CGm-SMrEksLK7OY7oAMbq42GaMMH6m9eruJSQVyexGDBY28rYd0io3NhC0d_fUOV1yaQyHXiJlLinMDN-XFBN8PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108134" target="_blank">📅 20:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=fUIfSM_nTiT-9jpkkIFqzkD5WeUvKsu4lDpykx28QMPpgqw4mfm0tkkysAl1U6FYir28p-oaS5d-gOqv7b9udaB4qBxdrG_4StdWFaco97UEauo7l43i-v1OdsxpWTb7ex1Z1efXziBhj6AiHJN4kzTq3lq24Qzqu-s0NCR5h-YmzAvraEz29BLy3BmkiZZGgANGplZiV_rLyDdAqmxPw1XgdGTKw3uZmIywDGozxDKgW7s_-6w2gd3BrVU8DErgtRt327DwouSnWGfW74Ds1jcktq1z7py6Gl4BW5dywTbMdOHVDYrXG7N7-Za-CPVAyQ-Boh-xPoLTnetehtnR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=fUIfSM_nTiT-9jpkkIFqzkD5WeUvKsu4lDpykx28QMPpgqw4mfm0tkkysAl1U6FYir28p-oaS5d-gOqv7b9udaB4qBxdrG_4StdWFaco97UEauo7l43i-v1OdsxpWTb7ex1Z1efXziBhj6AiHJN4kzTq3lq24Qzqu-s0NCR5h-YmzAvraEz29BLy3BmkiZZGgANGplZiV_rLyDdAqmxPw1XgdGTKw3uZmIywDGozxDKgW7s_-6w2gd3BrVU8DErgtRt327DwouSnWGfW74Ds1jcktq1z7py6Gl4BW5dywTbMdOHVDYrXG7N7-Za-CPVAyQ-Boh-xPoLTnetehtnR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌کاشته مس‌شهربابک مقابل فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108133" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108132">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
📊
🇮🇷
جدول لیگ‌برتر پس از تساوی امروز استقلال و تراکتور؛ پرسپولیس در صورت برتری در دو بازی پیش‌رو خودش به صدر جدول خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108132" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108131">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf998598.mp4?token=eN9nBbJalRy6eLbmFuji08G7Da3ze9d2mbYCVUrR1y3I9SBv11Ox-xmxfUMv9vA4dWW3shAjtAzLh8JijTr6guYl-yU2s7zrK3LpLQnHMv3okj27se6-4R_C09gWnT2u5SJXW3RoLeO6c2nz_6n0_vusUU3eOluGAvfeCd4BKxe-kgJPqtwQxftV_Vs70-_N-XhyCoVgj7nI3vCxWyD_BuzAWsUfcsdOPGgw3iwRdYk0k8NO69bHD76QLhO4po3Y4xOD0pzCqV2GLA3em1_8B4ii8LqKBsr72qIjxFD4YVG07LkeP2Azzp0FS4_17SNpE5DQZaQehbZyRDgEwG3NZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf998598.mp4?token=eN9nBbJalRy6eLbmFuji08G7Da3ze9d2mbYCVUrR1y3I9SBv11Ox-xmxfUMv9vA4dWW3shAjtAzLh8JijTr6guYl-yU2s7zrK3LpLQnHMv3okj27se6-4R_C09gWnT2u5SJXW3RoLeO6c2nz_6n0_vusUU3eOluGAvfeCd4BKxe-kgJPqtwQxftV_Vs70-_N-XhyCoVgj7nI3vCxWyD_BuzAWsUfcsdOPGgw3iwRdYk0k8NO69bHD76QLhO4po3Y4xOD0pzCqV2GLA3em1_8B4ii8LqKBsr72qIjxFD4YVG07LkeP2Azzp0FS4_17SNpE5DQZaQehbZyRDgEwG3NZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
💙
سعید فتاحی رئیس سازمان فوتبال باشگاه استقلال: پیشنهاد داده ایم تیم‌هایی که جزو 8 تیم برتر جام حذفی در سال گذشته بودند امسال جام حذفی را برگزار کنند. پیشنهاد خوبی هم هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108131" target="_blank">📅 20:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108130">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=nhGwToA4VNX6_p2_PDiGG-kB31uIYrt_gRKbL7CW4c37zUHzlLo59zTAYk-UK_1IOCjt7oTzWBQrvSyq-kltYqllHVMzXI_1ontmbMdmxHlxikqQbLy5UVtmThHsSpN0FivbTqqfO3IeP31QSlfwMY6K6dU-6nri1Ixk3P5dY8GRzMvQz4ROWjzlGr6SLIXJoHpRJHmVTB86VKwvckscmpF1SYeZgXAZGeOnMOI4KzJXCDxqi15gqjDmmpk9Xzw5yUaxGlo2NzbkjutNIdZ1XqH_FiOQf7xRJt15VpJ1sXmdOvWq-HBoFT6LzHi87okT8ERyqJmJm0y7EfORcCW-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=nhGwToA4VNX6_p2_PDiGG-kB31uIYrt_gRKbL7CW4c37zUHzlLo59zTAYk-UK_1IOCjt7oTzWBQrvSyq-kltYqllHVMzXI_1ontmbMdmxHlxikqQbLy5UVtmThHsSpN0FivbTqqfO3IeP31QSlfwMY6K6dU-6nri1Ixk3P5dY8GRzMvQz4ROWjzlGr6SLIXJoHpRJHmVTB86VKwvckscmpF1SYeZgXAZGeOnMOI4KzJXCDxqi15gqjDmmpk9Xzw5yUaxGlo2NzbkjutNIdZ1XqH_FiOQf7xRJt15VpJ1sXmdOvWq-HBoFT6LzHi87okT8ERyqJmJm0y7EfORcCW-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌پنجم سپاهان به فجرسپاسی توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108130" target="_blank">📅 20:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108129">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f44126980.mp4?token=MkFnYZKkRu55sylH7a0GTpDLVjeII-4eUPZgV7oGidEKsJ_JIb8h_Aj2ILbKP99CDNVt1Mh99iWT3TwAd9jf7dd-TKHFU9xoO_HmGpOfDtAHLCL0j0avlzv132TiKO-vY0QzUvrLSuwLqPVpb-HBVypr2PLq2j_CWPWD24quWB0QbuMFTKX3YyUUvRXyPrdUGVSNGjDMMMVwIGxmEwao0jMLDEOcKwPNRZiheqfG1BiNUn5aBWAOe8cR_WOTLJbaa8qtV01q5P9nhJUv6aQpUfAvJYfE5VuvxmCEO23nd0wjTT0T1_ZXs9kOhWuDHX0Z4YY030vEkHDdyN7gbFe8L2Zb1gj23zXeJW0kWGE-H9Isy86ZifshDD2I5SgIwGppYc_J-DoGisgFoky18VQa0Nd8Uz0MDDVhJ5c06j1HFsfd3ljVY4uUWAjOU0ry_VAqChzQ8KKA5IZ74-ioohRYXHgKRN11OnfAeFLJDvPLGecd9p_aJLU3jwgoFkuBsFqjhlPv2njZO-kw7OC5xaI87B0LsMQ37MuAkSaNlzT6-SPLPE29fBTX-4MDXY7lfH5cQXUwFUzzp3ktuPAfrR2UpmdfYHK3YjjH8c6Gm0rdGms6wZsmYorNn4wkPU-AX_txJHXk8uWT0H5CfJapepCBgx9XaAJd-_Zl8_l1HEK5fRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f44126980.mp4?token=MkFnYZKkRu55sylH7a0GTpDLVjeII-4eUPZgV7oGidEKsJ_JIb8h_Aj2ILbKP99CDNVt1Mh99iWT3TwAd9jf7dd-TKHFU9xoO_HmGpOfDtAHLCL0j0avlzv132TiKO-vY0QzUvrLSuwLqPVpb-HBVypr2PLq2j_CWPWD24quWB0QbuMFTKX3YyUUvRXyPrdUGVSNGjDMMMVwIGxmEwao0jMLDEOcKwPNRZiheqfG1BiNUn5aBWAOe8cR_WOTLJbaa8qtV01q5P9nhJUv6aQpUfAvJYfE5VuvxmCEO23nd0wjTT0T1_ZXs9kOhWuDHX0Z4YY030vEkHDdyN7gbFe8L2Zb1gj23zXeJW0kWGE-H9Isy86ZifshDD2I5SgIwGppYc_J-DoGisgFoky18VQa0Nd8Uz0MDDVhJ5c06j1HFsfd3ljVY4uUWAjOU0ry_VAqChzQ8KKA5IZ74-ioohRYXHgKRN11OnfAeFLJDvPLGecd9p_aJLU3jwgoFkuBsFqjhlPv2njZO-kw7OC5xaI87B0LsMQ37MuAkSaNlzT6-SPLPE29fBTX-4MDXY7lfH5cQXUwFUzzp3ktuPAfrR2UpmdfYHK3YjjH8c6Gm0rdGms6wZsmYorNn4wkPU-AX_txJHXk8uWT0H5CfJapepCBgx9XaAJd-_Zl8_l1HEK5fRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇷
سوپرگل امیرحسین جولانی بازیکن فولاد خوزستان از وسط زمین به مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108129" target="_blank">📅 20:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic85fY3yffouKx68HrDHmgayBCI8o3LRZSUamOzxkaHyZAqz78Bi9nfoUcnV-Nuj_HYuoerKdjU3blUZ5JP9qB15j-K9_esKZfV7TyC00ovOm9JBEegsEo4GXlN2-VyRak4ZwFd35GrqBmcPR0g3CbaxRC6JzsQ8xrKL0rywVlNTi2_tqkzkY30JaeQicRTfmw35WBe0dcVCLEed7m8eh4J6Yao8FSJirIGOH2okcGeN-H9hqLawpbnGFk98bVmeIc_daX2GYoBipcQ4vgdf0lHUlrqADsfcVI2-JOVbeDfSK3beZlkVAYvjPXSac9TgDRPh7zZvLXRGpcDibDdzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108128" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108127">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل چهارم سپاهان به فجرسپاسی
آریا یوسفی در دقیقه 54 دبل کرد و گل چهارم سپاهان را به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108127" target="_blank">📅 20:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل سوم سپاهان | احسان حاج‌صفی '47
سپاهان 3 - فجر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108126" target="_blank">📅 19:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری‌زاده : یاسر آسانی بازیکن تاثیرگذاری است/ بازیکنان تعویضی تلاش خود را کردند.
🔵
کادر پزشکی تلاش می‌کنند تا او را به الغرافه برسانند.
🔵
امیدوارم مصدومیت او جدی نباشد ولی احساس می‌کنم کارمان یک مقدار سخت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108125" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | احسان حاج‌صفی '38
سپاهان 2 - فجر 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108124" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108123" target="_blank">📅 19:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108122">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
شجاع خلیل زاده بعد از پایان بازی با عصبانیت بخاطر تصمیمات داور، راهی رختکن شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108122" target="_blank">📅 19:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=UYYBBkngOJ7jqOweW86lUweKqt1AJD-Aq9P7UOHfgiwtsjl1HJLjdq8vdTEd1ZxdGemenC9bvELk-Z_A-IXmZRMSLDKte4e7C301IsuC6zICGWrQdATJlxnNq99cBR7HbBiNdwCExEOGJpKkXYN-Df_z_5Pxs7BTYXPE8pCP3vpnsi0KduNCIgn6XkARra7N2mQ5pmcob6DICsP2DxyKWBkkS60u3ibSDmC3rjuf1fSSOsokRB2L3tDQrvfy4y81rjYpBmCcJIxw-kqZhQoQY-vccG0kf7BMiEyNPVn3NV0DN4khMS4ITSeiaNZ5bus6xqX7Ewgxbk9Gf5nzqxTglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=UYYBBkngOJ7jqOweW86lUweKqt1AJD-Aq9P7UOHfgiwtsjl1HJLjdq8vdTEd1ZxdGemenC9bvELk-Z_A-IXmZRMSLDKte4e7C301IsuC6zICGWrQdATJlxnNq99cBR7HbBiNdwCExEOGJpKkXYN-Df_z_5Pxs7BTYXPE8pCP3vpnsi0KduNCIgn6XkARra7N2mQ5pmcob6DICsP2DxyKWBkkS60u3ibSDmC3rjuf1fSSOsokRB2L3tDQrvfy4y81rjYpBmCcJIxw-kqZhQoQY-vccG0kf7BMiEyNPVn3NV0DN4khMS4ITSeiaNZ5bus6xqX7Ewgxbk9Gf5nzqxTglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
گل‌اول سپاهان به فجرسپاسی توسط آریا یوسفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108121" target="_blank">📅 19:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108120">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmF2xXTRuN8Lb08kyGNVVmwFdhUbGqD9MsDv3EQyp3OuV64o59HiYK2WXFZFDPliRfRbIKRILb3hEbbxtU5cgWwzNijnsMJTfKF2VUZ3dFXv70Bj3XUFG6kntJ9q56tKDV8-67DKeh0-TrJ7HWpYNti99QE9fuBnDSiC4bih2UpAgGuT5tPmWH-lUctCZv3RVjchBn4BY1tRPTKZZj0AcHjCM5mgx8o8sGbdYzpW5pLxXpG_Bo4KJCJnpqIEQj6CBtEwUYhumgmxPvbuF-aRLCbzzQANhIInamDmrnj7B1o3TPORctDURFeyVOdzvlLAygo2zqI50jRJyfT4fKrCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108120" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTJ0Xp-HevS_NeJyh0scpWAFUkCp2EySRB9U3HBBUTsZYjkJHZUs7ue5RKAEwWeTvc49RNkArnU1Xn5NgdPbMeu_1d4RZGG0L12A0xRIerdKc5XOwezeQeXF7C4kNYP_S46HusKOUCpzoXEhGIxIdTjg_K6z4tGnlPSfWMJuZnjUsrL-dv79B3mO6tIlNAXBJfN3hJKy5iEXHLqxMZvGiWk6crugJ8WqLnMBvSX9uewGiW6zXXH2Y5BCYTNeORP8Zvd_8DWZueJpmKOQJpdcw4igpf3JvsSz1wxu51p4-ZzanIm46hMooWNpFk_RgQYX1LiaKDcKIaRJOZgVR9BLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108119" target="_blank">📅 19:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxiepUfJgcyiC0k5K8Gbidcry3RBeqZzmfrhyVzzebVHQFODFISFgHQS-YoKZi_vswEJL3k33GkY4kHYyZzSiZNwgKb3G19CeYwRCOLQGmhuVaHZdzn9zilGIP2QnX_TIoXrJbmMCse5IdtA6StHZbwzsGm12V90vhWPofeDXinYiwonnLV4_z3vADacKbyswgkPO9ZTUwkl2sqZe3t0KHpZO8ddQ8qo9Jb6iRzT52qdN2eXv1JfuKxP9b83x6mfiV8yjAmS6XFa1WNmciwGQAVjkwTOeqrDPVdwYB8mVXhYPlITObR_2dmovao3KBkdPh5KxZSmkXskIjNpeVJzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108118" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال توسط حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108117" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سید مهدی حسینی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108116" target="_blank">📅 18:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تراکتوروور زددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108115" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108114" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=sIHqU7AH7CPBfMB0TNS9w0I6nBXMRgn79zFmONU0CEPRxrCqhNs46yAPeuzjx4UDgA6zpv4T_1Bdr80Fhjbahj-MDCzWzou9c76gaqhkZ7SOtpURTHrwI6QG8guCnUzCnYfS53wm14zJj9TQ0bMtLal677lMTVbqS49SPJSmH160YJ6uOWNns6FiJ_sfnaDrRwxjxo_16HsyXBiYrVHYRiXZo7JGrZZ8CLr-rgHQUTVfUTse509YO99Al3EOgiIjCUMl_7a0lUEtKY7b-4JMkruqoUpJomg6SpzjBlXLHfoRVTWE3qqqKQatzt0qs5FHCXcRs0Iw2WM4374S72Lzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=sIHqU7AH7CPBfMB0TNS9w0I6nBXMRgn79zFmONU0CEPRxrCqhNs46yAPeuzjx4UDgA6zpv4T_1Bdr80Fhjbahj-MDCzWzou9c76gaqhkZ7SOtpURTHrwI6QG8guCnUzCnYfS53wm14zJj9TQ0bMtLal677lMTVbqS49SPJSmH160YJ6uOWNns6FiJ_sfnaDrRwxjxo_16HsyXBiYrVHYRiXZo7JGrZZ8CLr-rgHQUTVfUTse509YO99Al3EOgiIjCUMl_7a0lUEtKY7b-4JMkruqoUpJomg6SpzjBlXLHfoRVTWE3qqqKQatzt0qs5FHCXcRs0Iw2WM4374S72Lzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
داور بعد از بازبینی VAR گل تراکتور را به دلیل خطای هند  بازیکن تراکتور رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108113" target="_blank">📅 18:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108112" target="_blank">📅 18:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
احتمالا خطای هند بازیکن تراکتور</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108111" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صحنه داره وار بررسی میشه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108110" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726254fc85.mp4?token=j-sxYmT_0aLvoEtp0EsBuSi4zqxdEOreq-RzcY2TCFPw44kcYwr_o_9HSPAFchFXC2l1p0y7LR06YEf6Kge10EzRKW04OX7v0-KebOT74GJ5it0WxTPOlEgNgjl_S01AEYOIGqxikq5Zmbd_iR30KwJsvw4oHUCveKZdHN0aO9kcf4r5KKoidDc_wtsK0c1t9ghxJpe5DI89__y1bmiY6bPsq7QcDRkXHejl1vHAG6BICf7lAHCAG4kwoEw68m2D9SukKyKR-Va5w6CIvGDviI98rB6wGchBue8tgvQfpd_20Uf1wkqfwPdIpYsy6TDZyP8BQIw7t7ezxcpoI3PxPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726254fc85.mp4?token=j-sxYmT_0aLvoEtp0EsBuSi4zqxdEOreq-RzcY2TCFPw44kcYwr_o_9HSPAFchFXC2l1p0y7LR06YEf6Kge10EzRKW04OX7v0-KebOT74GJ5it0WxTPOlEgNgjl_S01AEYOIGqxikq5Zmbd_iR30KwJsvw4oHUCveKZdHN0aO9kcf4r5KKoidDc_wtsK0c1t9ghxJpe5DI89__y1bmiY6bPsq7QcDRkXHejl1vHAG6BICf7lAHCAG4kwoEw68m2D9SukKyKR-Va5w6CIvGDviI98rB6wGchBue8tgvQfpd_20Uf1wkqfwPdIpYsy6TDZyP8BQIw7t7ezxcpoI3PxPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108109" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تیبوووووور هالیلووویچ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108108" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تراکتورووووو زددددد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108107" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108106" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همچنان استقلال از کووووون میاره</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108105" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استقلال از کوووون آورددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108104" target="_blank">📅 18:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wow-uTMNe-sIy3CYiz2GxaSoCXXgHHSWvLmCvbFvo8CzzTTHEJSW20b5kjpdUNfGRpdDe80wkS9u0OO7G4n0F0q-DHXyfJty2y3FJZNhbOPuLwP78fhWDvPPgO67Q8o6lKq8YQBIPV8jThTUb8wVSemdazNve3rPAq3zNcJ-igzNWecOZLa5V5POQPKt175iQxN4vS_6NT5zAzDGUybb9SqBEzLVqkXBEguy_iDDN8eUzSSxvvs9uhClkkfc5Sc4lsZG8KAUdh2oxWCjePCmv1z3ScclVSxQAiYvbogbi9U_kIeCP12UElJF16t5EC-bJIByr0DVcvVjzIcNb-gDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم فوتبال فولاد مبارکه سپاهان برای تقابل با فجر شهید سپاسی⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108103" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVAyyChst4IZ_WsknaXkKu5em_YD5ESus8nypdXK3R7r3qhsgCzKGdn55YHyD9VDYGQF0MQJnNgNs3PrBLu30c1-K36Omw9bX9KySY-dtoWtOfQzNN57hOLjFS-UsahdAEBE9FXAI1KW32W81A9X8VA7WFGq9Puhr8kFp-I93r-5PzEXhjhoP-XDWbSZH1xtUe7zpO7I1tM3p048Oodbdy1saGWEzHcNDZbLsaPkpN2-KJ99TxAxotSnIzj5PmQlif2HlOn3_-tUsQ50x8E3quKNtoYT6w92PlKcNps-XolzI6BcgoPUxI8Hd9vH7vuCfyTSjUJn7WdQ30LF5qPs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📲
استوری منیر الحدادی درحال تماشای بازی استقلال و تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108102" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=fA02me-FRmL1kAcUHavsp-dM3p8Ee9Qy_6nrZaGDLJ3alGNz1UIQ-_Zvcav9TGd-x266RCoUf_g35uyHeL_5CRqEMkk4l7aF7mOEDVgPo0QiL95JbLUhJR5CY-9xKMPWloEnninrzNfzF9L3G4C327sE7urpCkrk0Q39ClpmtiAnFR8VvSh_qCnkJ1Nao-ZuK4COM4fUC0jxpi3Lx0IAmFMJdRfZIKLE_FkA6lQwigJ87ksikJDXCyiewAciHkLcShxjiFRjrAovdaeHP8n9gXsaPvCBepVjaPwh-HUSB1zDD1MtAfV1Hm1TeLkIvgTTk2C4NGewLPRxNo7hv05Epw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=fA02me-FRmL1kAcUHavsp-dM3p8Ee9Qy_6nrZaGDLJ3alGNz1UIQ-_Zvcav9TGd-x266RCoUf_g35uyHeL_5CRqEMkk4l7aF7mOEDVgPo0QiL95JbLUhJR5CY-9xKMPWloEnninrzNfzF9L3G4C327sE7urpCkrk0Q39ClpmtiAnFR8VvSh_qCnkJ1Nao-ZuK4COM4fUC0jxpi3Lx0IAmFMJdRfZIKLE_FkA6lQwigJ87ksikJDXCyiewAciHkLcShxjiFRjrAovdaeHP8n9gXsaPvCBepVjaPwh-HUSB1zDD1MtAfV1Hm1TeLkIvgTTk2C4NGewLPRxNo7hv05Epw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشک‌های یاسر‌آسانی هنگام تعویض از زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108101" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108100" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108099" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=aIqcNIaQFZpz2FAap1ZubF8aMbylOIxRFF2mFznoT7MvfSPDQt3fm2JIhy37zXcONorbF18tgHYKJg7PLrMK9Y30SiPhG3S3xT69BDr8c7xm_SBZudnDSfNYySQ5TCV2bTmUlZAkBkelScD-LzkqgjVFFWlN165--gDud0aVDcql1-LWsL8VlSc5JZ8C3xD1AD_XrQ7WYFG3Z1pJpetiAa4a-seyk7C5rMIjbzz9eTrGPKAkcZGvLL0YPdLyRYpMB_RV7YrBSqltEj2lUAc-elrj3kOJRsqp_CyYCQPldWutHxMph2Oiud8kIs4cMVMvYPO-CZr8slLWAGNk-qIbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=aIqcNIaQFZpz2FAap1ZubF8aMbylOIxRFF2mFznoT7MvfSPDQt3fm2JIhy37zXcONorbF18tgHYKJg7PLrMK9Y30SiPhG3S3xT69BDr8c7xm_SBZudnDSfNYySQ5TCV2bTmUlZAkBkelScD-LzkqgjVFFWlN165--gDud0aVDcql1-LWsL8VlSc5JZ8C3xD1AD_XrQ7WYFG3Z1pJpetiAa4a-seyk7C5rMIjbzz9eTrGPKAkcZGvLL0YPdLyRYpMB_RV7YrBSqltEj2lUAc-elrj3kOJRsqp_CyYCQPldWutHxMph2Oiud8kIs4cMVMvYPO-CZr8slLWAGNk-qIbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
نوید مظفری، کارشناس داوری: در دقیقه ۴۱ بازیکن تراکتور هیچ خطایی روی بازیکن استقلال انجام نداد، جاگیری، زاویه دید و تشخصی داور عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108098" target="_blank">📅 17:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108097">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=dlkqaELjpptDTxx4lmnEB87CEEbbd8KBiNHHEpgixLvjRufrXyTFZ4VEANKpJj-24Mpm2tJ7bfQJvIMapOBD9cbc0OWmPZjDTBchnFTijcS5cU7CUGeBq2JOABKfY-g3nvp4zE6L2_IVowwtRK5D2Z9bQ4aEhuqGUuGJOx20E61tSIsvEuWLpBOoZRZuE9GFfVoybfFZlop8z_HflHU61VDyQ-CzRxrtqc6ehBb1yW0-16bcyRJor4s9bo6YCF7Y0uSREycf4tGTrM6JK-AhM4NiCv27MtBGb0SFO4mQltZ5ZuqET4qPyM3YJN2sFR-EVrdRvv58hskqsi3u3iZGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=dlkqaELjpptDTxx4lmnEB87CEEbbd8KBiNHHEpgixLvjRufrXyTFZ4VEANKpJj-24Mpm2tJ7bfQJvIMapOBD9cbc0OWmPZjDTBchnFTijcS5cU7CUGeBq2JOABKfY-g3nvp4zE6L2_IVowwtRK5D2Z9bQ4aEhuqGUuGJOx20E61tSIsvEuWLpBOoZRZuE9GFfVoybfFZlop8z_HflHU61VDyQ-CzRxrtqc6ehBb1yW0-16bcyRJor4s9bo6YCF7Y0uSREycf4tGTrM6JK-AhM4NiCv27MtBGb0SFO4mQltZ5ZuqET4qPyM3YJN2sFR-EVrdRvv58hskqsi3u3iZGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
موقعیتی که یاسر آسانی به این شکل از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108097" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
صحنه مشکوک به پنالتی برای استقلال</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108096" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108095">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108095" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLs23a-JGXLEz337wLikCFyKC3ldvYnehyeD_9wT6MdCbSQ3_Y1PLcxw5J6R4_ZMz0oFqQXGit1wH2GoT6GGdfwrtOcQ6M7heWLruAt8XVXXjNphGcLIBOe8b2IWF0ddZcK2aAarzxaFso889CMteAzTbmAeRckxr25iOTxN4RTecBDc8NntfVCIWXh0fEdgycRTO4UVtM8cwh9g2DAp37SZIzfkorwLTYBBnLhWJOBi46y64YzFn4BoYjxf3MlPa_GuQOqIOd3T9lo4sNTWlOTShWc5-5yCg5ttyHAVpVHaC8kh93EY4_1X90Bn9Q_cfh-_HDf8ThtoxyMxzCSyxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108094" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=YtSE9sbSXj87-yU5BT_cZiFYDivwpAvDs7XJtVJnNzlWgJtY-avPqUBo0IchMkttCP3ufE7NDMJ5Py0C1Ucr63v8nu6Z-ZR2Xf-4GOPspJbRz6rtu8PBpMQV5ir-W2ADuZ27ZWavbeO2cFv9fUIefbvHDwZH2eFgkjXK49entqciOPtnoRdsVio_2Gjr5djQzvPpd_kMVNjjP6tbPepFkxLT8L36thhwQsJvHA7whpbaDsdAMql44H7PNAEx8b-6Oq7TWu1KLlZcUy_aNx6vPqzEqy3IQg5A2gLuSGbB5ggBVLLROcxUICY-M4opq9XSZkQlfJl6kSwVDWUkhoQWtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=YtSE9sbSXj87-yU5BT_cZiFYDivwpAvDs7XJtVJnNzlWgJtY-avPqUBo0IchMkttCP3ufE7NDMJ5Py0C1Ucr63v8nu6Z-ZR2Xf-4GOPspJbRz6rtu8PBpMQV5ir-W2ADuZ27ZWavbeO2cFv9fUIefbvHDwZH2eFgkjXK49entqciOPtnoRdsVio_2Gjr5djQzvPpd_kMVNjjP6tbPepFkxLT8L36thhwQsJvHA7whpbaDsdAMql44H7PNAEx8b-6Oq7TWu1KLlZcUy_aNx6vPqzEqy3IQg5A2gLuSGbB5ggBVLLROcxUICY-M4opq9XSZkQlfJl6kSwVDWUkhoQWtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رقص آذری سعید سحرخیزان که باعث فحاشی شدید هواداران تراکتور تبریز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108093" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=HL1zG8TvfAr5YT8kHYrglosru375uRzVqq1eoktbpDWOTUIByVDQyXlrT8zyWrvAjLAhAWk4GelPjqyKI-idOk-9015hGWTi5Qd4rYiRXqXUQWhsAqWmDy2yzxO-5XpHjRDFAyUZCjL_BUWQR5uKnk909CF4reSqNyM7Zoj8xVIbNl9NSuF_E2M-ATfAbR5J87aF1CgbEVQ3NTPbsQu59JfytNNQUfZUbGQMxlT9KvTXYxH7AgdAAjXX_A9bYS_EaxXHAGWfE0dRVfqVkNvORK9cZAGkBBLnBTPZQWGCw-k1hFRHf3xgBUfBn426ZVJBDrtF3sqxVuSb2bilLcIbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=HL1zG8TvfAr5YT8kHYrglosru375uRzVqq1eoktbpDWOTUIByVDQyXlrT8zyWrvAjLAhAWk4GelPjqyKI-idOk-9015hGWTi5Qd4rYiRXqXUQWhsAqWmDy2yzxO-5XpHjRDFAyUZCjL_BUWQR5uKnk909CF4reSqNyM7Zoj8xVIbNl9NSuF_E2M-ATfAbR5J87aF1CgbEVQ3NTPbsQu59JfytNNQUfZUbGQMxlT9KvTXYxH7AgdAAjXX_A9bYS_EaxXHAGWfE0dRVfqVkNvORK9cZAGkBBLnBTPZQWGCw-k1hFRHf3xgBUfBn426ZVJBDrtF3sqxVuSb2bilLcIbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پرتاب بطری به سمت بازیکنان استقلال بعد از گل اول این تیم به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108092" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=T1OdMA-ffMQ1JwuEyNXpPa9lHTBbrX_5dBMqQuw_KP3CUjN6g9PMzgO3wpwoTtCZIIJTLpnAs4cEzSiBdOqsbyLqBqwLZl1kgZ87DUm0VuTHvJJWu4MYcrzSsOJXTeIYxwxj5OIdlPGPVPg2nSBqJytiGl7I167A5umngsa9G1Yu9I1AxqXpFG0XPrJ9ZOUIk9nJOyp1RdBtWKxn0vRH1bJuZyyZkxCWLx4NWDA3Za3fJVbc8opIvTibgzrPsiUcqbwo2C8SiohRFm4dXUm_G-lke24-k4aO2LILMHVD1sdMXK9saxFa7YpZ2fa14ZgJGHN6qG3KlGZ5hO3ZuiqDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=T1OdMA-ffMQ1JwuEyNXpPa9lHTBbrX_5dBMqQuw_KP3CUjN6g9PMzgO3wpwoTtCZIIJTLpnAs4cEzSiBdOqsbyLqBqwLZl1kgZ87DUm0VuTHvJJWu4MYcrzSsOJXTeIYxwxj5OIdlPGPVPg2nSBqJytiGl7I167A5umngsa9G1Yu9I1AxqXpFG0XPrJ9ZOUIk9nJOyp1RdBtWKxn0vRH1bJuZyyZkxCWLx4NWDA3Za3fJVbc8opIvTibgzrPsiUcqbwo2C8SiohRFm4dXUm_G-lke24-k4aO2LILMHVD1sdMXK9saxFa7YpZ2fa14ZgJGHN6qG3KlGZ5hO3ZuiqDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل اول استقلال به تراکتور توسط سعید سحرخیزان
28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108091" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اوه اوه هواداران تراکتور رو تحریک کرد
😐
😂</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108090" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سعید سحرخیزان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108089" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">استقلال زددددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108088" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگگلگللگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108087" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
‼️
✅
تایید خبر اختصاصی فوتبال‌180؛
🔴
شکایت بابت مجوز کار بازیکنان! نامه باشگاه تراکتور به پلیس مهاجرت و گذرنامه آذربایجان شرقی درباره بازیکنان خارجی استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108086" target="_blank">📅 17:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=RZs1_oij5oEuWX-tY-LlZp7QrqnEIub6Pbya4GkmX3WOT9_waZkRwGnBPpf-Qv_ez3L6bYdfbhVYq8VfJ4ozXU9XmPKTBA4Q8NqYJJJ1AozoNawfpP1C05rPrkEN91e9RpnLh7NWEdM1mHG_C-Rv39s6VP-J4VNgCFhDFlr7VcfnhhsuZAzksrc-DjFfnnvmn2Ni22T7nWOOgPEI9oopFn2D75hCcRVVxLT73oemh316Vgaf0SFZZujblxH2jboLrAAcGlu71coA-Yz26s_rtusogcYzT25KvyVYpDDjB6ijCdTfT67TkZhgKAnhzl4AZCUhzO4iyQWpFVpe7J-4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=RZs1_oij5oEuWX-tY-LlZp7QrqnEIub6Pbya4GkmX3WOT9_waZkRwGnBPpf-Qv_ez3L6bYdfbhVYq8VfJ4ozXU9XmPKTBA4Q8NqYJJJ1AozoNawfpP1C05rPrkEN91e9RpnLh7NWEdM1mHG_C-Rv39s6VP-J4VNgCFhDFlr7VcfnhhsuZAzksrc-DjFfnnvmn2Ni22T7nWOOgPEI9oopFn2D75hCcRVVxLT73oemh316Vgaf0SFZZujblxH2jboLrAAcGlu71coA-Yz26s_rtusogcYzT25KvyVYpDDjB6ijCdTfT67TkZhgKAnhzl4AZCUhzO4iyQWpFVpe7J-4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇷
🇮🇷
کری‌خوانی تراکتوری‌ها برای استقلالی‌ها با پرچم‌های قهرمانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108085" target="_blank">📅 16:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=cys-x5boEriKzjyRA3um9pgNjSuNI83mmLH76fQhue6Lt5AO4x0naXhxZeIWKRvzb8sqS12XwgSPUmGazUJssbjb9KLL9NCOpj_8w8DpEkx66JGwWdFbELZbTNGWJX3mQytxKpo2NiiZHS0uCZU7hdy33JESwfa9Ef4I3Jx8PwkN4NL55OsebgXEyrq-prJuF5TgMUBxeLYnJippXT_lk3Rl3qG7d6Epc_jLuc7axlty6L6ltvlUPBiBpoBeUctJATl6iU0KkPe1tk0yr6T4cgzkwlsM8KZIo4J8xQWj15RKyeOZyA3RWIO-OJAapgUI3zrltjRyR6FvLEanNagYM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=cys-x5boEriKzjyRA3um9pgNjSuNI83mmLH76fQhue6Lt5AO4x0naXhxZeIWKRvzb8sqS12XwgSPUmGazUJssbjb9KLL9NCOpj_8w8DpEkx66JGwWdFbELZbTNGWJX3mQytxKpo2NiiZHS0uCZU7hdy33JESwfa9Ef4I3Jx8PwkN4NL55OsebgXEyrq-prJuF5TgMUBxeLYnJippXT_lk3Rl3qG7d6Epc_jLuc7axlty6L6ltvlUPBiBpoBeUctJATl6iU0KkPe1tk0yr6T4cgzkwlsM8KZIo4J8xQWj15RKyeOZyA3RWIO-OJAapgUI3zrltjRyR6FvLEanNagYM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
رقص و همخوانی هوادار استقلالی با آهنگ معروف تراکتوری ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108084" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ca421470.mp4?token=fsQCiZ6aiLMLSDkDKpIbmXjsQfUvhlP4OsmLmqkGCjbVgUVNMOHjOf2gTrPZJOXEFivrFz8SUcI3OzVPut_JQEzZh-LiDWCaX52XwjDEBJ1sc1KN6aO1BDmdAJ6QieRsDepPoc_gu4FGOIHad0C1Q6lkBf5H6uIYdlstKxwneABBp09SAC9A1unJFz3m4ZEVqMMx74mqHGNHRDgWpwj1qGZJir95ho9M6m963SsIn_CIW2vTAkBiQgy72qbXQ9NzThczg0Ml0ACZIvlqXisNLNSYXwr-nKOKJf56tvM9oLxAS1MQYyu9D29QBjS3hxa1jpD-Opymd_Ay4ohEcEqLew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ca421470.mp4?token=fsQCiZ6aiLMLSDkDKpIbmXjsQfUvhlP4OsmLmqkGCjbVgUVNMOHjOf2gTrPZJOXEFivrFz8SUcI3OzVPut_JQEzZh-LiDWCaX52XwjDEBJ1sc1KN6aO1BDmdAJ6QieRsDepPoc_gu4FGOIHad0C1Q6lkBf5H6uIYdlstKxwneABBp09SAC9A1unJFz3m4ZEVqMMx74mqHGNHRDgWpwj1qGZJir95ho9M6m963SsIn_CIW2vTAkBiQgy72qbXQ9NzThczg0Ml0ACZIvlqXisNLNSYXwr-nKOKJf56tvM9oLxAS1MQYyu9D29QBjS3hxa1jpD-Opymd_Ay4ohEcEqLew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
اتفاق عجیب برای فرعباسی؛
خون‌دماغ شدن دروازه‌بان استقلال در حین گرم‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108083" target="_blank">📅 16:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلالی‌ها و پرسپولیسی‌ها می‌ترسند به تبریز بیایند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108082" target="_blank">📅 16:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWDXau9JN2JwuXmYArdqzCyQx6umHaCvwLpvnP7Sg1yeasdoeSEf4iP8uDm8pYLcsLFbOufuWJntjuG6--AJdjmkX7asc3OJO4SOhabIGnsnuU6eTM8c9po7JmqIH72O4ecW6-lwnDlLEB-YESBcw37zDBHYjQYHlz-nnvXK5lutJiSTPX076-ABCoTW3rsaflUmOOpoCji_s0wh3KzRCnUJWitqsEcBthwEUma800f8kZLpDqbALCpbJ5snJ77ki3GIW9Jm5lMzVA1kG5ef045r_KkGfRerenn5lwOX8wSno7vyAJFbfOmrs3REq3bxf6xLCq8WUqL0ukJGlwrrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108081" target="_blank">📅 16:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=HUC-K2C-XgjMUjdvEqf1mVEBrOu9_FOyOh_6LHKs8sNZdJhO06at3-3UkV_IaWKNw2A5Qq-PXMyQAplzLvqYB_heGcyLND2C8AdEKvqokxCL2X6yh2YlkOwZyYpVjY628EH6Qz6lOzQx-BJnCAR0h248mMZ5uAR0NIQ8i2RzRVGh8-pA5Q1if1xdByIk_IsQapMK00U3w8O--wcFBR1GLtXIEG2Ggjcubc64Bn3rjNl9eiL43QoHfCrZJmR3_Lrug3BcvOgSaOaqUEj-sZKAgBXPAfWHu8JKtN7pyoDtU7XhAUF3-J2S8H_cNMB9qrJVQXr8dDv9M_7m2BbUls_f-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=HUC-K2C-XgjMUjdvEqf1mVEBrOu9_FOyOh_6LHKs8sNZdJhO06at3-3UkV_IaWKNw2A5Qq-PXMyQAplzLvqYB_heGcyLND2C8AdEKvqokxCL2X6yh2YlkOwZyYpVjY628EH6Qz6lOzQx-BJnCAR0h248mMZ5uAR0NIQ8i2RzRVGh8-pA5Q1if1xdByIk_IsQapMK00U3w8O--wcFBR1GLtXIEG2Ggjcubc64Bn3rjNl9eiL43QoHfCrZJmR3_Lrug3BcvOgSaOaqUEj-sZKAgBXPAfWHu8JKtN7pyoDtU7XhAUF3-J2S8H_cNMB9qrJVQXr8dDv9M_7m2BbUls_f-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
مشکل جدی قیاسی در تلفظ رولز رویس
گلزار: چقد فخر فروشی به مردم ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108080" target="_blank">📅 16:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLzNJYAJzBDLM6l0fp464gGgVnKXbS7K3futYJm3U7EbJ1mtduFiEjVsRrSOnDfnuwB5tykgaDYd5MG4HBo6BeL-Z_ezVkmuwOqzJytfKNXIuT3OPhnX5BxfnNgR5vYhOzx3rEZdxghDxhSp2IHFDPQiUJ-38UDS3fcp7ksGh81C8o9cpLK5fqgAYk4d_11y-0ugTlEyWCQIVtx40XDemGnofxUOMWGH0oJZ7Rz_XRxWCJuscgi_L3uP5DmH5-W7O1sQFxQYqrcouAi4JUD3Vx8ooIJ5uEnb1Sh3lOKrs2ItAqhNXy59BR6GSFfWB7Dejjy_1D5mnkabWpt8wG-GDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108079" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3x67fYXZDVDzMGkgcvnp0TNgaIsmZAEO3Uuva3K99tFXFoE_FfN_hQ_ZHopBO3dJFmQ0eSyrXCdnEbhqJ0vVldyjRdxA3LeTf6PiKgqhS7poi6tpgIf9-gJBgP9CPogST4WRJca2vMJW6nSGm3zYF1xRjoff14di3PUW-FK1WIjtAaqTqqKnhAiL1kkf2esiUiUHwDaUFI2STxEk14DkDdnZrWHY0XQ-bHS3cyB5gEeH6m6yQFo1_ItInc2nnDSwflFPCLkMdY1cpH5d9PlycKbAxgjgTfJ4tQENDmhQ8q8bTueKJJnMXGuXzyj6E7AKVSi_RLdrFWMpBrNvkkC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108078" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=k9_f4tgxxKZMotJqzGKCnYUorhkcKhPKNw4Z-Kw6NeMXUvP9d-D-jspjJjpz3YiBJN5R0QI7HZHNv8cZHRcR6J7E-IYJ9P6ANoEmo81_H14v-YhIHYuexEL5IUbcgaZV2LurRW0qvwWQ4IkZkQ6_pHkDbMC6nQYc-gXDaCh65Jcc7Al5fjEtJlM0_GAJshMiEwNYO3P6qZiQmRq2URR1HsSP8HdWRviQFD9aIHMbVLxTubH6h_neXfFaywbl44iXauShaWzqE_i0u0rJj7ceZkQS_eoXlwseNfGQTsCSquDEuEjh9MpD2zj1Gcq6ruFB80WQYurvFgOhkeO3kcQoGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=k9_f4tgxxKZMotJqzGKCnYUorhkcKhPKNw4Z-Kw6NeMXUvP9d-D-jspjJjpz3YiBJN5R0QI7HZHNv8cZHRcR6J7E-IYJ9P6ANoEmo81_H14v-YhIHYuexEL5IUbcgaZV2LurRW0qvwWQ4IkZkQ6_pHkDbMC6nQYc-gXDaCh65Jcc7Al5fjEtJlM0_GAJshMiEwNYO3P6qZiQmRq2URR1HsSP8HdWRviQFD9aIHMbVLxTubH6h_neXfFaywbl44iXauShaWzqE_i0u0rJj7ceZkQS_eoXlwseNfGQTsCSquDEuEjh9MpD2zj1Gcq6ruFB80WQYurvFgOhkeO3kcQoGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
هوادار تراکتور: بعضی تیم هایی که در لیگ نخبگان نیستند، از تلویزیون بازی تراکتور را در آسیا تماشا می‌ کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108077" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKEn472kYh-Ms5brDBR2QJJSqOdcQahKYroF0pjVWvskPAwqEwUwUwDLKcl0hkSW22qlc6R-2GzGKd0DoTlMdiWnGPRUVGmO1VOErqNjzktmhRYLNYw2ZGQOWROIsLAKw3VDDOXztRo4rOsUWZ-cF6gCrTUsmv6F17KUp86ayoTlk6-B1xHFRsip6r_hhgXoWEmGkrDeopbQdFtWdUkIFdLyDrZN3-LH40qlEFTljQlNCZ-FAUOmPyIAy1ip2XsQcbGEYghqyvElDIkpvDg6HlKqKSayav4O5XcIPSyQSigFK1e5pXnbnR2IdXQ7TjUhTxSjLcQq6_jMVAinvT1MkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب تراکتور مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108076" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=DB7Y0QpEgFJCqhDVnPYKMyEARpf929gJDYauRFMkNUpl1UF34rkgPtFniPmOn10wSv8auf5Fr80hwPcsnqU798migpwLs3kM7qw04rSCdCFPpF0MNhYrOPxzcpWvISJbGfi0TDiaqgNHbKTdCXjENDogUrbSd1oBlf9xW62FXRAKekr9Xhr2MhFTeA7rmMroBT1WN3DBtAXp-fl-dz25XA7ZhWDIF1Djik4rFb8fWGYoBiqe8UiXobF6s3fC0gyOLd2Pjw6M32szI4gyzDKTIWZ5ysDJCfWKnkvFFpxtvaWDyclT-pQSUCWQGXVvdaO6rbheRJ4QMf-dLZfjfnlchWlQz5CUq47cKfDOaZFFEzj2TcLn00HJgogry2KjgryrwI3Ee7Lfl0T5DdxfD9CaZDFuRRtzmKk-wFLqJBgW_02aqwvvWoK4oRLNH3y9XCskcq5nmXrhwcRHpEtiVOUPtkw-g6QmVTigYhbRsfafcN1mDcPwv8iHE6QEIaZuysMVbGrZDmzYWNwyKLnr_0qGB1k44-HjB6Efdmatkds03DWjxxTBNqnR4dv_6wn9v36TZQViSKe_QPjoE3T4UODBceBWpZytbgQUKTg83Z4aYHBlfznUcjqO_F-Q_J4DYVogZQ_zRtgIMV6r7YzxNa41QpeczAAIbsYZzMwv4ulLHno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=DB7Y0QpEgFJCqhDVnPYKMyEARpf929gJDYauRFMkNUpl1UF34rkgPtFniPmOn10wSv8auf5Fr80hwPcsnqU798migpwLs3kM7qw04rSCdCFPpF0MNhYrOPxzcpWvISJbGfi0TDiaqgNHbKTdCXjENDogUrbSd1oBlf9xW62FXRAKekr9Xhr2MhFTeA7rmMroBT1WN3DBtAXp-fl-dz25XA7ZhWDIF1Djik4rFb8fWGYoBiqe8UiXobF6s3fC0gyOLd2Pjw6M32szI4gyzDKTIWZ5ysDJCfWKnkvFFpxtvaWDyclT-pQSUCWQGXVvdaO6rbheRJ4QMf-dLZfjfnlchWlQz5CUq47cKfDOaZFFEzj2TcLn00HJgogry2KjgryrwI3Ee7Lfl0T5DdxfD9CaZDFuRRtzmKk-wFLqJBgW_02aqwvvWoK4oRLNH3y9XCskcq5nmXrhwcRHpEtiVOUPtkw-g6QmVTigYhbRsfafcN1mDcPwv8iHE6QEIaZuysMVbGrZDmzYWNwyKLnr_0qGB1k44-HjB6Efdmatkds03DWjxxTBNqnR4dv_6wn9v36TZQViSKe_QPjoE3T4UODBceBWpZytbgQUKTg83Z4aYHBlfznUcjqO_F-Q_J4DYVogZQ_zRtgIMV6r7YzxNa41QpeczAAIbsYZzMwv4ulLHno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کنایه‌های ژوله به سرماخوردگی عجیب رحمان‌رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108075" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=q6RkPf2ucQA2OMjynPou-BLinAFQAKifxLy9HwWngdVPxCXxg_REUIqnR6j8zxGA7wCtmAjOg-_iw37XFO44BsQz94UmdTJhyIVo6ku6yjR6wN13v8p_miSQa52N6j8RA4hQwFsdI5YZGsCDdFoV4FZRUoNtXAKVx5RtI10B6818iV8y8BL8yWcZBhQAhEgWs3IIptCw7l6Zlth-PsLMCBu48hd8sPfTH6yOOLIgu33DyLQoyzcOMeSp-T9dRpMcGxEvC-ujrrTmaJghRodmqojAiNFe6xc6aoEucCcn12GCQdiP6e3xC4tA1L3TclRuyPM4Er-EJTq5wC_n-37jhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=q6RkPf2ucQA2OMjynPou-BLinAFQAKifxLy9HwWngdVPxCXxg_REUIqnR6j8zxGA7wCtmAjOg-_iw37XFO44BsQz94UmdTJhyIVo6ku6yjR6wN13v8p_miSQa52N6j8RA4hQwFsdI5YZGsCDdFoV4FZRUoNtXAKVx5RtI10B6818iV8y8BL8yWcZBhQAhEgWs3IIptCw7l6Zlth-PsLMCBu48hd8sPfTH6yOOLIgu33DyLQoyzcOMeSp-T9dRpMcGxEvC-ujrrTmaJghRodmqojAiNFe6xc6aoEucCcn12GCQdiP6e3xC4tA1L3TclRuyPM4Er-EJTq5wC_n-37jhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
هوادار تراکتور: عادل فردوسی پور دشمن خونی ماست و همیشه تیم‌مان را تحقیر می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108074" target="_blank">📅 15:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28665d2567.mp4?token=gouHa8d_1KnNy5DCgKUPF6nL5KW1aX7AeTpn6zb7hMBrT7diSLLMom1locrKO6p-6GRn4USBUIP5R0ljO3MTFplm5KsoLGI_Zz9QAjfgA4ACLWJz1td4PZHfIFHPxhqmueNNFEbJJGhmcWzhqjqgyQbpnrH92EmeIA3Sxa-_5xIRls1jkQpPJLL5YNLQzy4EcPWs_OGFORTXxH2Ht5ukRMRofSYOHMcQWUGgA1yQni_59sdAs0bUfNmAeISM3zlzsc_ZXVTIni2HpEd0QSrRLr57DkhlqkjLpPolT2TbqcJKPrLYi0rgccqVILfuISLWCFEtOeHJSyLnGtHpkKePszo8rU5Y5bXiP3w5jkvwe1zn4NTrstk4WStrF-WbUc2XZHF9nzpf4zB4Jst6XnB1J4VHpEUK-rmofBdw7c1fUoYlxbXUIKVRjhT6wTDdAG1ojKvSryP99wtRetxmvbeyXiEPxvKnGFEm61GIACcwRsg9dpYEc009pdy26zG7WbPqW1wf3_LtZ1mG6u8Z3N8STisxKday1KfYm65si4cA9SwRj9ChSN6VHqwn_U3Po7JtwFJLrAnjnD4txm6v3b-m00iFqH7u2CnX7ZAXdEUDYh_0XSKxqNdstCk_k9t7nI-U4FUqqPI-Xbe1Zm7WfSkuNqUY-p2Hmp0I7jAxyw23wG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28665d2567.mp4?token=gouHa8d_1KnNy5DCgKUPF6nL5KW1aX7AeTpn6zb7hMBrT7diSLLMom1locrKO6p-6GRn4USBUIP5R0ljO3MTFplm5KsoLGI_Zz9QAjfgA4ACLWJz1td4PZHfIFHPxhqmueNNFEbJJGhmcWzhqjqgyQbpnrH92EmeIA3Sxa-_5xIRls1jkQpPJLL5YNLQzy4EcPWs_OGFORTXxH2Ht5ukRMRofSYOHMcQWUGgA1yQni_59sdAs0bUfNmAeISM3zlzsc_ZXVTIni2HpEd0QSrRLr57DkhlqkjLpPolT2TbqcJKPrLYi0rgccqVILfuISLWCFEtOeHJSyLnGtHpkKePszo8rU5Y5bXiP3w5jkvwe1zn4NTrstk4WStrF-WbUc2XZHF9nzpf4zB4Jst6XnB1J4VHpEUK-rmofBdw7c1fUoYlxbXUIKVRjhT6wTDdAG1ojKvSryP99wtRetxmvbeyXiEPxvKnGFEm61GIACcwRsg9dpYEc009pdy26zG7WbPqW1wf3_LtZ1mG6u8Z3N8STisxKday1KfYm65si4cA9SwRj9ChSN6VHqwn_U3Po7JtwFJLrAnjnD4txm6v3b-m00iFqH7u2CnX7ZAXdEUDYh_0XSKxqNdstCk_k9t7nI-U4FUqqPI-Xbe1Zm7WfSkuNqUY-p2Hmp0I7jAxyw23wG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
مهدی تارتار، سرمربی پرسپولیس:
جام حذفی را می توانیم بدون ملی پوشان برگزار کنیم به جایش از جوان ها استفاده کنیم. مگر یک بار قشقایی پرسپولیس را حذف نکرد؟ چه اشکالی دارد که جام‌حذفی برگزار شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108073" target="_blank">📅 15:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108072" target="_blank">📅 14:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=tg_fYXyppFNCcu5IMCcpeZjq7PAjtVvMvKjfoQwcSsbDpiQmlZDNRtIHgGUhbjN-LFnR5UIlzu6d01oco2WwHxAvWxRzhW9cI3XCzUYv5c1Dwh1FDGBG83pbvXCCBEIko-jnysUMtQ19ONjHojoIuAqeKROTuNSXKCMhPq6wYAK1SwJbAwSh8u4faijYsiurqmTg2EroLXbBjbCh6MJCF9kgVw0gjQOBSoXTeeCDh4rrN49jGrJS2M9eH_LodqsTeie9ntI5vLgB0cBPSwF3dxGYrP2x5-Ui1R9OoTWF44j6alNb06Ppnun2jum4IQ_QmLxHQSb9B3Mxw8T7fcTcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=tg_fYXyppFNCcu5IMCcpeZjq7PAjtVvMvKjfoQwcSsbDpiQmlZDNRtIHgGUhbjN-LFnR5UIlzu6d01oco2WwHxAvWxRzhW9cI3XCzUYv5c1Dwh1FDGBG83pbvXCCBEIko-jnysUMtQ19ONjHojoIuAqeKROTuNSXKCMhPq6wYAK1SwJbAwSh8u4faijYsiurqmTg2EroLXbBjbCh6MJCF9kgVw0gjQOBSoXTeeCDh4rrN49jGrJS2M9eH_LodqsTeie9ntI5vLgB0cBPSwF3dxGYrP2x5-Ui1R9OoTWF44j6alNb06Ppnun2jum4IQ_QmLxHQSb9B3Mxw8T7fcTcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلال و پرسپولیس در تبریز کلا ۱۰ نفر هوادار دارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108071" target="_blank">📅 14:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=IAhqxSjn8IrNfyYX3x6ETDouNFCz6c2kd6QOP9iW_6c5wQr5v-4EGWlrvf2sv9AnYyAi8CT618K_dwpACDa-HyVotANXaVMqanoriAOqP33rkVIfhEr0wEUMumwZBJuhcKucAos-XwVNby1enU8ku_uDchkC8oW0ouYIVelyRgRl80uLKU87uC21SHOIld3JqPAE-qZ1h0Y7gDD56bwwbZgEJQwSLm7S-PuNy2wuGj9V-t0j1WqZ8X2k-tGLK7R-ZysBjUt6FkxjaLIh6RaDrEGcIz3dofKN3VHJJlxXQZTnXiQuyBO_GpM7wAKpo-DD_skipiCiWLQSekfNypre-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=IAhqxSjn8IrNfyYX3x6ETDouNFCz6c2kd6QOP9iW_6c5wQr5v-4EGWlrvf2sv9AnYyAi8CT618K_dwpACDa-HyVotANXaVMqanoriAOqP33rkVIfhEr0wEUMumwZBJuhcKucAos-XwVNby1enU8ku_uDchkC8oW0ouYIVelyRgRl80uLKU87uC21SHOIld3JqPAE-qZ1h0Y7gDD56bwwbZgEJQwSLm7S-PuNy2wuGj9V-t0j1WqZ8X2k-tGLK7R-ZysBjUt6FkxjaLIh6RaDrEGcIz3dofKN3VHJJlxXQZTnXiQuyBO_GpM7wAKpo-DD_skipiCiWLQSekfNypre-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
❌
🇮🇷
🇮🇷
هوادار تراکتور تبریز: ما مثل استقلال تهران گدایی جام نمی‌کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108070" target="_blank">📅 14:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108069" target="_blank">📅 14:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7dk-WQo_NdvV-Gl-AKsVJpVosl6bKY6Jfe18X72JY2b9kab95vELZwqbX9f84Wc0Hzm4lN6SFt_Kk8HrXzUo067PntaVDqO90wCjRttGuGTLnMjaa9MtN6TS9OkI7i5lSKACo7QYMVAj8OTQ0irfZOwwzuhQfSIkMYmOMlo6g5euob1cpTGxKypT3bcV-6a3N0yOIgi-59B25iO8XkCY9EEqHF-n03kXwXziE2jvgTIx8v1zbh1HnsXybM-sh1zc8GMclDA-hBHJov7VocqJFynQEpcx1LEAx8kUSqt8qleG8iBR3XUS09YqK3lviupsXcrGJ7Idp7PJTJu0JiohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108068" target="_blank">📅 14:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzkpGHqwMywgCxAxGDMLg_Dr66IVEtlxywyPpQxnY7mSZ7ab56_RZCcHVCJ3_B0KxbSeLS8FAi6Ca5o6QriiCOxDXur1KfXT14rmcI4JLI6wwyr-JGcv2vss6oz-xLWWYHws_sd5XHBxD09MWzJD1aBAs6NkKPQl__pOkAaslhdUe-fyfFdQRFZNLmgoB97_vMZqBs9owXaQ5YinC4N4QAVUrebi14CU9_FRKIWD4l2Z3QFCs-u6zBybNaz9wS-vvj6BzG2xZakG142P2w1ddH54IVym-Q9_1S7pUbEYBK3fLJG-volJkMBwhWj58kAuo9awQ77jayf9NNXM2PhQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
روزنامه‌SER: در روزهای اخیر درگیری میان چند بازیکن در رختکن رئال‌مادرید شکل گرفته و مورینیو کنترل رختکن را مشابه فصل قبل و دوران آربلوآ از دست داده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108067" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💥
🔥
خانم دوناجان وایلد، در سن 61 سالگی، رکورد جهانی طولانی‌ترین مدت نگه‌داشتن حالت پلانک (تمرین شکم) را برای زنان با ثبت زمانی 5 ساعت، به نام خود ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108066" target="_blank">📅 14:25 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
