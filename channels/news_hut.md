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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=bIGFFb5Er8qCYryEi7oMzq61OO7MK7ry47iI-sxEfkxt17Non_O6MB8CV3TmDAe8dE1HIbg1PG5Exd-ncMn9B6ZYghDjhDt2Imvq3qqMcXHb5nMsB3dNdd7cxYBlLuHRD2V2W_XZ3ofCCxzTkRm-QD-piBQ0f3BG2QttRNpzOtsMWnmGndTWxoa7pSU1qlGDkxD_ney3sQf6QwnqhBzA43T8fNldpVrfizb5seFshVluzs1NtOmU53H0nRW2QQm09PxLrgCQLjRQO3aRvbynOUo7lycXi8LNmh-dTUa3AKZFrBqWUHMMlCP61KG5bv2AQ9hwW5jB3tC_WhwsdMPG7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=bIGFFb5Er8qCYryEi7oMzq61OO7MK7ry47iI-sxEfkxt17Non_O6MB8CV3TmDAe8dE1HIbg1PG5Exd-ncMn9B6ZYghDjhDt2Imvq3qqMcXHb5nMsB3dNdd7cxYBlLuHRD2V2W_XZ3ofCCxzTkRm-QD-piBQ0f3BG2QttRNpzOtsMWnmGndTWxoa7pSU1qlGDkxD_ney3sQf6QwnqhBzA43T8fNldpVrfizb5seFshVluzs1NtOmU53H0nRW2QQm09PxLrgCQLjRQO3aRvbynOUo7lycXi8LNmh-dTUa3AKZFrBqWUHMMlCP61KG5bv2AQ9hwW5jB3tC_WhwsdMPG7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvqDnHQexkrG-8DtkE0n8PTugFKL7t-1-h2Kggw_h571WuaG9QRY6dCJNu3nAqG4FVC8FATFUihCF2bJb9JAUVShk9mBjjUM2S93s5Ds9p2fkjs62j8u_-ta2yvitjSJIRjfCNvAmK-F2lC3O06ikDCpPlon6n9gfj1CkHyT8wTTx0Qf26MjFH2gB8LiSuB-nle1aNMA7PjFccakGk6oqDNiL_vt23clW4aqXOvKxosc-zAngxO_kxlTgXKzfgBxNoEVK7hN-WJP25BIPF2iZWgq2Xk_vZ47AZoozEDwFI_fAL4VwVtsqgC3JNah2gMTXQU8ABDpu-hkUSUpqw5DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQCyaYMjYA0csIngHp0ToAcb1VaD-dnsv13oA_KB8cpP0V7U3qELZeyxpaXjKuSmBqzkpnvpnfTjgxUi2NYSCDtP1NRPphy3JkfHHVhVzU2cfupd4GnJd4fyer6sflNvSEKXArBhrXivxordUKpxfYUofyloVZyhni-uEGsIPlQ2D0BeM0-J7eCeRoHu7ShZ3jH80xq-p_BWU5vdkUlUuq-FbE2q43fTMBffBO5DGVx-Mca6QviHZA-hlWjDO6Bify8vFk0uKt3ncsRYwv8ZICuMJby-9tb87L3G8ql2OvbRaSHB9M3QY69cjFfIvjJokRd36XRs15T7ggV3oC6vtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6UhA3LVydapccpK0aWeIX4qKGuj_oCA7lEsnjD2cq3SDWh166b4Ds4omMMBTJgLtCjnqEHq_d0E4fLpMb4ZzUTa25QtOETpUL5Nz4jX6nNvyTWCRf5PMrfS_qAmgZjEMW0-yaJU-zLIiXljTGt3dcF_-FPyMN872I2lYjEGhU7W2oLK7EqqUqbNw5-F2u1za1YyjuXk6ecY-H_uoncvmC_Zd3Ne_fDzWtLzgRLph5YE99aW__Pe3aB90VjEfGFGij7W4Nyz4t9lMFg2KabFPSJYaYbBsITcvSuixdE0Z_zBHjoUpndceV0kWK7PoeaCGZuuLg9Rb0qbWyy6BxCiuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=P7hCk4aKqie08KfA7RrQVjlaAdazl3C3x4XandEEtZmQiRdwL-KVKEsDI6oxW0N9ZLLeyAsDe5av_WliKMOSzaGpXgJMnKN7Rx1qyL82Q8ylkJ1pRZFoPpeTugniHHLAYWBMaBBPM8Jxr_p1Ud0IKf5AzRbW_O9ywYwVOw1G-u4NLF1Q4vUdmmOZua96DvLsrkV6NApVXvqJaUPbR-X-42sT-koctnrocjjM3OaLH_aq8468OW6UP1VBOsZB2-8fAFPiVLWDxbis4bRxBkzbxZdJlGxxEJKB6YYJ6ZhxCZl9B9cw7oO8dvhBcPOyiFe_TGgzH4MDx0YjvzscjYTDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=P7hCk4aKqie08KfA7RrQVjlaAdazl3C3x4XandEEtZmQiRdwL-KVKEsDI6oxW0N9ZLLeyAsDe5av_WliKMOSzaGpXgJMnKN7Rx1qyL82Q8ylkJ1pRZFoPpeTugniHHLAYWBMaBBPM8Jxr_p1Ud0IKf5AzRbW_O9ywYwVOw1G-u4NLF1Q4vUdmmOZua96DvLsrkV6NApVXvqJaUPbR-X-42sT-koctnrocjjM3OaLH_aq8468OW6UP1VBOsZB2-8fAFPiVLWDxbis4bRxBkzbxZdJlGxxEJKB6YYJ6ZhxCZl9B9cw7oO8dvhBcPOyiFe_TGgzH4MDx0YjvzscjYTDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=IE7BXHrVbi0rqvuFAp2HCF79RhXlTmzi12dQdpDnyfS_QtZjtAQkODjMTJFRlWAr6QcdRR0I9UIKe_Lt0sryCvbkbEiuEiVGJ0yAw16MHIqPRH_Ot1H_VLeIwj-wkKo2D-je2U1pTX8b4hxS1Q8HrkrApOu-UYTbal6Y4P-32lK2zZQon2_-RL39krix9kYX-076Ogn3CnVC_5RSffRvXeKSjtZRaO2gxzhDJX-ppEhtED6qaV3yWw6PFRHPgGgjWCNy3K1eThkq_3fIYDUjeIIi5f9k7oXN6nGBSTxejhChnuwyxyiC0nIL382jzz6KKd139fM3gGsrlUq2jnd0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=IE7BXHrVbi0rqvuFAp2HCF79RhXlTmzi12dQdpDnyfS_QtZjtAQkODjMTJFRlWAr6QcdRR0I9UIKe_Lt0sryCvbkbEiuEiVGJ0yAw16MHIqPRH_Ot1H_VLeIwj-wkKo2D-je2U1pTX8b4hxS1Q8HrkrApOu-UYTbal6Y4P-32lK2zZQon2_-RL39krix9kYX-076Ogn3CnVC_5RSffRvXeKSjtZRaO2gxzhDJX-ppEhtED6qaV3yWw6PFRHPgGgjWCNy3K1eThkq_3fIYDUjeIIi5f9k7oXN6nGBSTxejhChnuwyxyiC0nIL382jzz6KKd139fM3gGsrlUq2jnd0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=dvUYAo_tcycVsy2zV1hN3alW5E25qhjDbqMcxHX8mQpY0mi_AToSAih15eMPHL5Z8m4QwSYaUloaYoIDX2TWDh9Pcawx2ktk9ikiSabwb8H1WnP06WjcrXn7HsDfUfey4gj8FVYbXy-Hr7uyHAbu5LI8b-LjxjPUK1afYdHaYH7RYizgsmspIpRj4PrVdsVzroYgVw0M1-LcXCt0RsFQdd5Y1ktwD9rcHEeX2NktLfcFdM5OzFIX5TPVMbNbu3azz0fCYoRuW0pz0niBD71qmu3cChGjKzCfdji5kgfpZTgCg4hDe1DgFYslGCY2WN2H-BOr2WlVAhLnc5EsluQjeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=dvUYAo_tcycVsy2zV1hN3alW5E25qhjDbqMcxHX8mQpY0mi_AToSAih15eMPHL5Z8m4QwSYaUloaYoIDX2TWDh9Pcawx2ktk9ikiSabwb8H1WnP06WjcrXn7HsDfUfey4gj8FVYbXy-Hr7uyHAbu5LI8b-LjxjPUK1afYdHaYH7RYizgsmspIpRj4PrVdsVzroYgVw0M1-LcXCt0RsFQdd5Y1ktwD9rcHEeX2NktLfcFdM5OzFIX5TPVMbNbu3azz0fCYoRuW0pz0niBD71qmu3cChGjKzCfdji5kgfpZTgCg4hDe1DgFYslGCY2WN2H-BOr2WlVAhLnc5EsluQjeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72519">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNBNW3j6cBCivss65DbuKm2ZA2Kcr_BPPza6pzJ0s4uux89oB6ML3X2Cz72pLbGAWPo5pDRN2GlxVrAABiZe73y1W3aQss534JN_BTgdGTw7uQCdPDR_Nul4qbJBuuUWzaoew5AWPt3PkTgMmTkzvFt0iN7ochsHwEpeBoKIvlb08tbrr4kkbYUlKjDFSBPwfKrI0-hroLmks9N-lgK9a-qwgS28Fn0WdY5qaZPmlkhzqbzj0oqCRzHhCWQSbceqwJQsAWWd-lGF9ht55VvJMxN1XvWCnOyAH5BGg1jV3honVky9eXVSqz-OVieP_lX-4eBQ5ybhDDy_lOiM8j_Udw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=p84ub3UFhfN8lq-68jfHJrQnCsZlC9Vav6Easrar2qWvVdKvRyDZyfb6Qwj6fWtbAmp1XcJMgeMZ3sZ7p_zEw_SByobb643WXvfafEo-9Fzo1mY7usYK71LDJ5tTN3a41aGlxwBGCYlGxDIvgxtsY_c10_wAu5eok9f5Sbf-44FpmaEhObBYGQeJ3fPmk41zkNIghLyQ957a4gLpiglF3AiaJFqsMe7kyrHabKyudlnt3aW7k1ZhOdHBzjesVn8LikYn03PPNgGUGXcbp34-6iGuFExi0TYiMmri_kB41l6hopxAAhk8CypsnXnBPAa26fUjBh0-yagq6w83Ydt-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=p84ub3UFhfN8lq-68jfHJrQnCsZlC9Vav6Easrar2qWvVdKvRyDZyfb6Qwj6fWtbAmp1XcJMgeMZ3sZ7p_zEw_SByobb643WXvfafEo-9Fzo1mY7usYK71LDJ5tTN3a41aGlxwBGCYlGxDIvgxtsY_c10_wAu5eok9f5Sbf-44FpmaEhObBYGQeJ3fPmk41zkNIghLyQ957a4gLpiglF3AiaJFqsMe7kyrHabKyudlnt3aW7k1ZhOdHBzjesVn8LikYn03PPNgGUGXcbp34-6iGuFExi0TYiMmri_kB41l6hopxAAhk8CypsnXnBPAa26fUjBh0-yagq6w83Ydt-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بمب‌افکن استراتژیک روسی از نوع Tu-95MS در جریان یک پرواز آموزشی در منطقه «آمور» سقوط کرد.
این هواپیما حامل چهار خدمه و سه سرنشین دیگر بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72519" target="_blank">📅 15:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGTS2PYjGzNuOmuUCRpCXS2RxkBpjzrEJWgM23NKN6duVOm5oIXH6jBidS9ElX6AWyJrfQIViaJ-empKwm6N4dRg_fAA0Ou09t8atHzf7ICqtvY8xeTg72VFn_VR_2FCWS08XqzgdNzXqXazRKsdddkd8hxaWmtapTG_Gc3EzRgosEQcE9tBgdC-GW9x3h0LUTbE0jMADWz8dspvSpQ0x0_WTt1n7nkX6LRgXs3Z2aKC0R5hVZDL3_howT5SSynMG7pHGDDn3rI85Ikr2zUUhZ9meNGPLlrGQpIUVzQOdNqZ0nSr0ioslmol24UhW-J0824DQwbEbp16yLSucDpULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3B2skLJH63rSLglCePOJqBqWk0CeJgBAQb5n9eiae7CwFQ5hPwzWQihbRgrypkc7Qu5xB2RZCYdLudCBo_4zm3THw6NfdeEoWZ54ElBZvhDdkbgIXnv2172ajMZncePAe_HcQHtJcSH57eDz69sH21FHRlyqVFn-2ocLhbA8l4qdx2eTzRrqES_6eSKAAxfggLuSNG8SWznT59LP7X9cLfOaJEan4N-BTUFbA_FHTl9Lr6SGQncj5orcwPz2kZu2M_dixQOy4ldHJCJNWzNxGKRzhC1AgAaQ84mMEU9hc-hKN9iQL2Im8UzekC3OkI6uCLssBbxTLwBEZOd6DP8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzt26ZO1u33zKALabe5vfKn3VO0TehU64g-CSN3Ke9mBJZUUVdlhhTSnIE2wmeoDp68sLOCHZ8yFIU3eVYAZdFe8ummNjaXURl4rpBjD-o_gRihoupAT8R3AELbfetCJlLRN0Ud2Tsqc3oY6W1UBLqOb7t1kgQJAd_QEXCq8Tx4tivlIEQcCIXpVW7ZdyOUIlWK4uMkc5dQZEQB6lTrRgYWeyiSD59NmQPkG79Gfu9bJLYbkmEFLV8ED_tlwd_BgZS-TSQi3o1aK_1k3KT2W-yeOT-NUihxFJZ-_q431IlmbFfgcHmDp_YSeNKULEJvIsNvAJYrAXzgfF7GXik13lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنا بر گزارش UKMTO، سپاه پاسداران امروز به ۳ نفت‌کش و کشتی حمل گاز در تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72516" target="_blank">📅 15:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjSzF8AbvsNcdgeV3Gtefdmjr1p6rqPvZ13nIl4iO_JP_DlkvGBrPvTaD1luYTszvHToyKxDXVigxNHSuOKwHv8k8nhVGDq2nXSw9XUCwB6jX7TE-tnyiJdyrrLqULZqb_UJaV046vSE2DyZwm7QReR7TI-JFzaGA4LxcQJujsK7Ex6KIS7H-fJ6-_aMLbpPD0kbKTIm7B6ZGbB7RH7viFL2vMFWmYPEQ8PRD1I_QQELnKZ9YiyRF1T1Y-PTvZ_7MrVtdDloSNjvAmBOU4c81wvBctPqqyY2rrNiZL-9nlnwEzOh9d0m02y_Tr_U6p8AQZYBcdfEjpK9tMtodGVKvo6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjSzF8AbvsNcdgeV3Gtefdmjr1p6rqPvZ13nIl4iO_JP_DlkvGBrPvTaD1luYTszvHToyKxDXVigxNHSuOKwHv8k8nhVGDq2nXSw9XUCwB6jX7TE-tnyiJdyrrLqULZqb_UJaV046vSE2DyZwm7QReR7TI-JFzaGA4LxcQJujsK7Ex6KIS7H-fJ6-_aMLbpPD0kbKTIm7B6ZGbB7RH7viFL2vMFWmYPEQ8PRD1I_QQELnKZ9YiyRF1T1Y-PTvZ_7MrVtdDloSNjvAmBOU4c81wvBctPqqyY2rrNiZL-9nlnwEzOh9d0m02y_Tr_U6p8AQZYBcdfEjpK9tMtodGVKvo6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که هواپیمای فلای‌دبی دچار سقوط ناگهانی شد و به سرعت ارتفاعشو از دست داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72515" target="_blank">📅 15:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=HR0vitmMW2hVUizrJ08NkBAzCsdQy7s7myj2PyBet1KBj2loYplRkAlr0zjgk95jwdmJ3fHtBrnEXtCw-bL2Pk6gZPoYo8pP06kFZcoSq0_B7nKnzGhl-lewjd4slI7TTFkP1n009RBjdoudfgc5FIhH6MtfP78Ot2NtiNMFjk1iX3CeBE87RuGhbLEInQF0Ty6vhnaqXzvkglxgK4N0pG14_2enWUr5qrhe8nRAwz-Q4hVc8wa1X-Xwr6S2ULm3Ut81j2v7tPcKkkSmLM6qn9pqedO1HCeZONHa9r024eEOAFnP2mO-IUGUHLaNyzpdwCzrdfhAMISLW05E81ClwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=HR0vitmMW2hVUizrJ08NkBAzCsdQy7s7myj2PyBet1KBj2loYplRkAlr0zjgk95jwdmJ3fHtBrnEXtCw-bL2Pk6gZPoYo8pP06kFZcoSq0_B7nKnzGhl-lewjd4slI7TTFkP1n009RBjdoudfgc5FIhH6MtfP78Ot2NtiNMFjk1iX3CeBE87RuGhbLEInQF0Ty6vhnaqXzvkglxgK4N0pG14_2enWUr5qrhe8nRAwz-Q4hVc8wa1X-Xwr6S2ULm3Ut81j2v7tPcKkkSmLM6qn9pqedO1HCeZONHa9r024eEOAFnP2mO-IUGUHLaNyzpdwCzrdfhAMISLW05E81ClwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این موزیک به اسم «مفقود» در مورد مجتبی خامنه‌ای، فقط تو چند ساعت بازدیدش میلیونی شده
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72514" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آی‌۲۴نیوز:ارزیابی‌های اولیه حاکی از آن است که خلبانِ عاملِ حمله با چاقو در پرواز FZ1073، تبعه عمان بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72513" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCsGCBjUGpXfcTFLufLorAQN7CFL9cxG2sIuviYnLTWSBt8WX3Xipo2OyY3g2ikYpmlWPAnV3qZsTtvaC3g9cUtdZ2zfbisFsPqDeFy_8PCZneNJ4jxMTAhfNF25j-82Yi1mguBlhHwvztUYuvgIo4fMpZC_kil9XsPgytztynWq23QZhc0C6qHUUEHj47DxDATnYVDDoq6j83cL97SooU5GzvT02rWnkTcnl6nwrcu5JvPkWQht5qhoN_U7vOCks6lJe7hsXrmgwX759EIONbVoldfSxdV9Oc2ddA1BEgd6O21v67nTGpgwrdPAuzCjON8Id4d6KGPCGInL-iVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72512" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8284df28.mp4?token=kBDgNxOwHgxpHoFV72cJs-8D6ym9zLolmaLDCNIffzn9taGtWPIZix3lnYWf-5dtiK2vwfRT6FEOM8CBArU-ipo7DF73bKoVNGbaDFMAIQ0rp9W8_01C0IyZimVnG5a0H53wzYj65STLRERHACXJgnPGFbJ8rM3FDwwt-da5IR0hQLI1J54TWaoCY6nAeX5gx8O74UkIQEJ4NQG3nUPwFqMCpBr7BOKt4HslcrHXLQkt_88is7QiTvE3bdF4A8UWY_t5wv2FILme1FurzIJjeCM5WX3Zfsqavxr_8J-RHPlpAEORf-4Elq8XE4Bxk8XjL1Aupjw2EhBsEfeyNlj2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8284df28.mp4?token=kBDgNxOwHgxpHoFV72cJs-8D6ym9zLolmaLDCNIffzn9taGtWPIZix3lnYWf-5dtiK2vwfRT6FEOM8CBArU-ipo7DF73bKoVNGbaDFMAIQ0rp9W8_01C0IyZimVnG5a0H53wzYj65STLRERHACXJgnPGFbJ8rM3FDwwt-da5IR0hQLI1J54TWaoCY6nAeX5gx8O74UkIQEJ4NQG3nUPwFqMCpBr7BOKt4HslcrHXLQkt_88is7QiTvE3bdF4A8UWY_t5wv2FILme1FurzIJjeCM5WX3Zfsqavxr_8J-RHPlpAEORf-4Elq8XE4Bxk8XjL1Aupjw2EhBsEfeyNlj2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی؛
علت حادثه پرواز «فلای‌دبی»، مشاجره‌ای میان خلبان و کمک‌خلبان بود که به درگیری فیزیکی و ضربات چاقو کشیده شد.
خلبان تبعه روسیه و کمک‌خلبان تبعه اوکراین بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72511" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=AifL6TIrIGRbLKxv_w8NI9gB_pr-IBz3esRM13dB0H2_vblF-nzVWxe6c0W13_1YgMXMMQwxAWf9VntdLWNL8FtYb6aLHJU7g65vLB0i3Hrsiu23r7O5Blfxq21zjJVXF2W7ZSzKQn8GFOvwGps3ETixsTkQdi38fE7ImGhrcBOKqFHotWQe8cYcYW3m997Hzg-TN0-FH0wRP9f7SKnVVyUPCzAGHvsEZ9o3O6dQAPqr0RMS4XPpDm3gFpwPDr-JHP0ZzXxAdSvGGaMkIV75gJvLUMqUFb7rNlv-XBjwW2YMz196c0vXC0x0sBxn-bjkmUt-ZjNsfBMujUB_H3UcSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=AifL6TIrIGRbLKxv_w8NI9gB_pr-IBz3esRM13dB0H2_vblF-nzVWxe6c0W13_1YgMXMMQwxAWf9VntdLWNL8FtYb6aLHJU7g65vLB0i3Hrsiu23r7O5Blfxq21zjJVXF2W7ZSzKQn8GFOvwGps3ETixsTkQdi38fE7ImGhrcBOKqFHotWQe8cYcYW3m997Hzg-TN0-FH0wRP9f7SKnVVyUPCzAGHvsEZ9o3O6dQAPqr0RMS4XPpDm3gFpwPDr-JHP0ZzXxAdSvGGaMkIV75gJvLUMqUFb7rNlv-XBjwW2YMz196c0vXC0x0sBxn-bjkmUt-ZjNsfBMujUB_H3UcSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد
ویدیو دوم مربوط به فرود اضطراری پرواز «فلای‌دبی» در تبوک، مسافران اسرائیلی را نشان می‌دهد که پس از فرود ایمن، سرود «اُد آوینو های» (به معنای «پدر ما همچنان زنده است»؛ سرودی یهودی درباره ایمان و بقا) را می‌خوانند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72509" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVBqA-MqO6-4wcuQ0hhXfSVSIV6EbjKxUW5GqZZ-HO3rwYrgThwx4hk2l7YsCgwwBjBOxaHJmi805XotlIlQYLcUceSYxnZxWEB7Li3adeUiHvNJC_t1X_OJ4vswRA-9t3FxNFQ1NEdkIc2qnsVPxH3LEqPycvWmLITL_uQbPknoWsEAoKJghVX114t01U0358BS29qTHL7ideBn25aQrbuzhkyZvSO1xeHShQhh5NRASA3jLVXFXk3atzX0y6Pe2myxx9N5jqxNGK1y4M1lx_RPX2BgqVBxgbByL_HcPR30RwHw0Jx91niSaHXTjX0cNMoojLlhYHeloUS7UFMA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF8yVlQ3XwTvufrBjVQyl33ES1ZGV7QDbZ3XULOnX3Wew-041IVSk0D-oVJpkdDpkDf1-6Or0g0VGnSk-uIkdrHwGb-OLMjcYTbMn6VDshivzRT12UJPADphXrHS_kXbVwZKfQ5pHUy9UHj0n2JCEkYis1CD9d5IBSIOLAMZRUap4wj7rTqsa7wlLafaNd2n2HfpU0it2wnmmT2x25jdXzHTwdA6F9rNfKz4-XOZXlAwcponA0VwutjGDWdBuy32JbRUYgQa1IylOkkOaxXsOmPZZdF2snQ0qeQaC8LGmCrYZs7YgUZ6gT6V7kViwKRXBuC_lVoaDQEavtq6p7Rk4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=OysVKqY_e8kG3_aGhp1xpPfOpYeRoKAjOfYC13emBB2jrTM5m5xw_bXUCHNDjca4ue6WoyJ73GpwB4Sz33GR3vOh2NcAsPDNZiRz2u7ZaeckjiRGO6l3m_by0Ti9f7Sgo6wYJe7W2SAL1OkINw259dz1irHbEihKwflrKe3Hq6CQJNplmfuJgSSsbckuym5W0UokFVKJKCcH9TY1Nz3f-s1dQQka3Avk4QW83gJ-N5YVoAsyf6IIg1K9M-l2I99qSISPMRu67Hz9Toq00WdnOvfW8sYtaHGISOI00xrZVv3-q6RMgaMBdewJqVnLPIy90PJlXp9dvx-O4eAulj0umA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=OysVKqY_e8kG3_aGhp1xpPfOpYeRoKAjOfYC13emBB2jrTM5m5xw_bXUCHNDjca4ue6WoyJ73GpwB4Sz33GR3vOh2NcAsPDNZiRz2u7ZaeckjiRGO6l3m_by0Ti9f7Sgo6wYJe7W2SAL1OkINw259dz1irHbEihKwflrKe3Hq6CQJNplmfuJgSSsbckuym5W0UokFVKJKCcH9TY1Nz3f-s1dQQka3Avk4QW83gJ-N5YVoAsyf6IIg1K9M-l2I99qSISPMRu67Hz9Toq00WdnOvfW8sYtaHGISOI00xrZVv3-q6RMgaMBdewJqVnLPIy90PJlXp9dvx-O4eAulj0umA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGH25pQEt7M22taJyp1eGu-rQCCkoNgcMYgP8KJTWZE8Udrbml_jd4Nax_UBLEDif3i8C9_1LOpVgZjfYjmAN1SDr6SDYIRPl76rwO5eqhpg_LNp2I6fhKleuAmCiEtayC3QqPYUu7EUF1dggN1MqChauXRJaPsa6sQ7Z42AYLdS7vIKs1oiyMihTlOBOF0x-NjOnKwfLimqmG-9Wc8rLNRQRoVeQ85wrt4cwE7lcTEYvuQ0WVdjeoiPGCTxATJmE8yFB6Wo_NEasvXvTH32bliCqC5rrIAQ2Cud35naY0Ok_g2wQuzj04-YAy2Elke24tRR70LgGwB0D6lLhT4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htKqjmRb5P3X_3mF1PsXwarQWkBv-KH2qfyN3-q34YV1NPLEwpCqH0FLiwhply3UIbXPwtzvScpLxIbzRGHE79rk47qh-jakY-XJ9AmmKdheyUaTvJ-VKPq_Sz1rWN19pZp1_bU3RYCU2oumXrGDmXYbPzccfCUpzdg36SbCb2gfXnLYyjWz1UyBS-C2_5UjR02Z4_oMFdejNn_ge-1QcTFjZpkO4DgIxnjrpNZgIhmjC-Wsel4swwBRTm51zELssnqVmDTfhxkEPaVfTa72tiYG8W7rRsSQoX3W4QrsgnPPRStS8SZtsqvbar5AsH9X2JTx4ZCPnOifdHoX5_X_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=FCq8VmCeCLqPc7lcnZP50P_aSHnITqMuKmGi3MV69k4PhWYw1qq9nySfkBv2M1vHPMratp6n7Uu2BaciLkPDc83-78S9vcdPOaceBMAwDYiqvSNJ7ZqFMzy4TWuldbAlHgQyGY-EkkqWKUSHR6jhajD8CN58BbSUvpltq97xkWyHMRyJBu4pHyTyr0b087AYs58Hq6KaRgwIPVlvfixhtP4GmSy-OWLz6yCAWCjMlILQMG0OjCe1EqzVmhdYPV1J1M-d9OnfQDA-hatAhRrIugnv2yNqjO-H-HJizUbngDQipaBCzWDPQBCTrmhdqKfSI-QEFK6AYzdb3m-tfu2LIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=FCq8VmCeCLqPc7lcnZP50P_aSHnITqMuKmGi3MV69k4PhWYw1qq9nySfkBv2M1vHPMratp6n7Uu2BaciLkPDc83-78S9vcdPOaceBMAwDYiqvSNJ7ZqFMzy4TWuldbAlHgQyGY-EkkqWKUSHR6jhajD8CN58BbSUvpltq97xkWyHMRyJBu4pHyTyr0b087AYs58Hq6KaRgwIPVlvfixhtP4GmSy-OWLz6yCAWCjMlILQMG0OjCe1EqzVmhdYPV1J1M-d9OnfQDA-hatAhRrIugnv2yNqjO-H-HJizUbngDQipaBCzWDPQBCTrmhdqKfSI-QEFK6AYzdb3m-tfu2LIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Bfg32a-MdegO96z2DFOejMKFEIe46S41w-CLTscRXkWxSBjtCr-mgGYxEkJaBopbAGJnwS8JMS2RnxzzcdECyhEq0pXXo1WKeaAaEozcKE5w7PvvwpuoqP0lOHeS3VTmMk8ToxyP7zgAjSmtukYAFfEa2P89qVy2eMJv8ARcTg3OJar0IX8KGPp5tzmOTIImUYWOexxxV0v1UHp-7WDCQ1pzke-QIP0q61mda0blrtGXPTurSRi7IVqxmKjutbDeszcDXQ8713p0OqTszkLYgmhup6j9ToSsFBiaX022m04r8ayiNMJPWz32uhN4235FJXey_i3B7WCuNgorC7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56db93255e.mp4?token=m2W7V4Gpha_VH5BorAXxOMrriS0w5mTMKjqZltHGP398gL3qMq3bhQQSqBkIpeT4F3Sd6g6waIdPYya9lh9kyMNrtlbfHnj4mGxuf4-H5kiNDKrWkF4s9jEjCCGsbOqBgBRuj07w90q3l1vuD4nvbmLwCXSJTAVFGcXCOmtCLH8o86onJNY38AIhS2nBe7bwch34j8hAxAlNvdRFOjj6StWUb4nbqqOJFHRMHBhLRlsRC_EO9LhHz46sVh9SMXiEUEDJYYQKH9oXgS-_d_gMdN3UsOtoZ4vG9Z510_XYcCQrHHjzahn9EImWxRPa2VS_Cr-p-ZM8DVvUfGb6-WIy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56db93255e.mp4?token=m2W7V4Gpha_VH5BorAXxOMrriS0w5mTMKjqZltHGP398gL3qMq3bhQQSqBkIpeT4F3Sd6g6waIdPYya9lh9kyMNrtlbfHnj4mGxuf4-H5kiNDKrWkF4s9jEjCCGsbOqBgBRuj07w90q3l1vuD4nvbmLwCXSJTAVFGcXCOmtCLH8o86onJNY38AIhS2nBe7bwch34j8hAxAlNvdRFOjj6StWUb4nbqqOJFHRMHBhLRlsRC_EO9LhHz46sVh9SMXiEUEDJYYQKH9oXgS-_d_gMdN3UsOtoZ4vG9Z510_XYcCQrHHjzahn9EImWxRPa2VS_Cr-p-ZM8DVvUfGb6-WIy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو نپال بر اثر رانش زمین، این کوه با این عظمت به طرز ترسناکی مثل آب، نصفش تو رودخونه سقوط کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72494" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=ny2WrhF1itF0mKd34vVGdfBIBZ7UATT5AKdU5syJ7RbY_AH2PyW8SM4nQVppWNRnJWshDjmAE1iHNvDsckXrcba2A9FuIyl5FOiA6bhRz1kr1pH1QJZXSjFRdzz6_NCKOY9tQBd3eO6G3BWE8roUU9_EGCm3XSqOwMheu_KVJ8xDL2LmrRQ0zMCJN4kDKxL_76_bLXuFAXSUIS0eH6zdvl_obnGMvYYEuPKJEDzlcNwwqbU1oOleriaHjPE0qo9ZerzcbrOkgDUFDwBUKCeh23f3SrI0obg0EEqX_j-YZe4xgPOS8r7N6RFESzH4UcVJGS4_NbDQF7NHZcKRwIkDSLXWnJWOCiGhNkjAwJaY57LF5pHuKHn0oLyFUalIk_ZVws3e38BazF7Zz58GWffcZn8hO5JxV0Zu3_1PYB4t46A455Zl01T9IqSRVk58w1OUNj1AaB7H-njNFw2jvmcwwxaZHSJ3rjUlvJd3EJCBNyqwzSjLHM7a_8vGLcTeid1rE2AwolFP2CppYHphaY4aOA8PxUy8nCk86HPnMBLG_s_Y9cmPzKe6NewJT4xwDPMsUIrfmmS5CrbV2_f4yqN9BqaFAdcynRZaubIEXvNsRACCa-LsdgnYf1lcPwVVRvw_VHPAvXkSiumc0LSWwoIzrNhpeyeI2m17JA06Dy54ttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=ny2WrhF1itF0mKd34vVGdfBIBZ7UATT5AKdU5syJ7RbY_AH2PyW8SM4nQVppWNRnJWshDjmAE1iHNvDsckXrcba2A9FuIyl5FOiA6bhRz1kr1pH1QJZXSjFRdzz6_NCKOY9tQBd3eO6G3BWE8roUU9_EGCm3XSqOwMheu_KVJ8xDL2LmrRQ0zMCJN4kDKxL_76_bLXuFAXSUIS0eH6zdvl_obnGMvYYEuPKJEDzlcNwwqbU1oOleriaHjPE0qo9ZerzcbrOkgDUFDwBUKCeh23f3SrI0obg0EEqX_j-YZe4xgPOS8r7N6RFESzH4UcVJGS4_NbDQF7NHZcKRwIkDSLXWnJWOCiGhNkjAwJaY57LF5pHuKHn0oLyFUalIk_ZVws3e38BazF7Zz58GWffcZn8hO5JxV0Zu3_1PYB4t46A455Zl01T9IqSRVk58w1OUNj1AaB7H-njNFw2jvmcwwxaZHSJ3rjUlvJd3EJCBNyqwzSjLHM7a_8vGLcTeid1rE2AwolFP2CppYHphaY4aOA8PxUy8nCk86HPnMBLG_s_Y9cmPzKe6NewJT4xwDPMsUIrfmmS5CrbV2_f4yqN9BqaFAdcynRZaubIEXvNsRACCa-LsdgnYf1lcPwVVRvw_VHPAvXkSiumc0LSWwoIzrNhpeyeI2m17JA06Dy54ttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6nEaNuJtvfehjKva7g36NdicnWcqgYfr9wKjy2izqSASstwZZ7Vuc9Rj2VM3Cxfv0DUjbk3MqwVTYHz-Rc0xrOFU107APf12l-c7rWxkepfJgoyIU20SXBioS9WhEsXQRpUH_jE3JfE3vUeIeIQCPtO7z_FIgZ8h27pwaR50Gf2h_aPQceh9_iezARm1M8SH_U-qbn3cdDkGlEocOZF_zk-MRMx6ltvq5vtuPGAFpQckbZ7jM1FJnubTakcJ1vTfXG-HyrzjO4xYp7fKUI4eKlZa1Us0UToFyK00KGkH9clOiqxXYIMTxlOJJzJ6QeepVdzY_uFoqkuX9JH_OIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTdVwuEAaOWpPB6tNiSE8wN92ibKS6jviTFxR9QHM4NyjWa2kTGgs6FMs_x_YDxsT6GxcmmXNzwbTw3J9gN6c-6yuYUG33Ej04I2Y53ul4UUuylVriDte5dlGY0VQTY7TSgIO4B_izOWefCu4nm2qfMiZ1GAe_rA8xRnvmmFD80goEQT3JsY7B7fRRDyW-ffKrKBesh_pjm7vY0vWob-0bAO0uVh4Vvo5bPrKVZ7M8pf7FC6dVkOIwNZZ5HkqwsAdj5X_Ufghys0Q-S5wDUdp5YYTxmOqUDgEDVRumkQpnOqyO4SxuxIcz3JeKxenpKXd2077Z8rZ_Y_J5Tbgmj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=pOdE6ePBFN3aBfSx48Zr7hAMFo2SWq7QVAr5FkU6S2L7NPavVzGhcl_umdGfw-WCEenSlsGVc4GEsaM1ZoLADVJfToR-UX9wfjCe2OlDQvPYFzaWFeb6g7NX3oR69SrAfe5QxVqk1we1i2gsithIAQD3BBuLTzQFgU8yyd-lVASQ21nMTfiWaFeXJ9g5XZ3a-n0qtIRSwuLmcSz3n9lWMTh8je5gwfNn9yVYoVlbBvD1IKx0LOOS6sP75XxbdoK3BGlRae4IrIQmYJKP9lrATl-Ocz1mOqUFVkfjAta9tgSYZIg_YjQgWKqoib_YyZjUdwtXsdsHZHb8bWOZ8BZOiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=pOdE6ePBFN3aBfSx48Zr7hAMFo2SWq7QVAr5FkU6S2L7NPavVzGhcl_umdGfw-WCEenSlsGVc4GEsaM1ZoLADVJfToR-UX9wfjCe2OlDQvPYFzaWFeb6g7NX3oR69SrAfe5QxVqk1we1i2gsithIAQD3BBuLTzQFgU8yyd-lVASQ21nMTfiWaFeXJ9g5XZ3a-n0qtIRSwuLmcSz3n9lWMTh8je5gwfNn9yVYoVlbBvD1IKx0LOOS6sP75XxbdoK3BGlRae4IrIQmYJKP9lrATl-Ocz1mOqUFVkfjAta9tgSYZIg_YjQgWKqoib_YyZjUdwtXsdsHZHb8bWOZ8BZOiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=hRtrJP5z8cPgBXldfBfI63rl8k4vYACyOLY5XVNYalhFmwDpMqOd1fdgJYhA1VrROlghQcdsidm25M84udsb4JVbp09Gbrdu66wi6N7TbBsCwFXBC13sRug1lPtJs3fOOMpBY5aidxNuRiincgPD3tyPR6UEX1dfgTfcKhxwAn2oDE3zbhUxuX_LpnLcU2TuYAc6SUNAq8qW6GGRoothrLSavuQ2mnP49XLnEliH5bgliXeH__-IiuPglYQfkIPg2d82JNqnySJO2RxD814wNMS61g6E8UwSUOFjx2G8lwxCaFVR5CkAmj_ve9U-E6pDeYfN6-Sf0OsrmwCYVQGdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=hRtrJP5z8cPgBXldfBfI63rl8k4vYACyOLY5XVNYalhFmwDpMqOd1fdgJYhA1VrROlghQcdsidm25M84udsb4JVbp09Gbrdu66wi6N7TbBsCwFXBC13sRug1lPtJs3fOOMpBY5aidxNuRiincgPD3tyPR6UEX1dfgTfcKhxwAn2oDE3zbhUxuX_LpnLcU2TuYAc6SUNAq8qW6GGRoothrLSavuQ2mnP49XLnEliH5bgliXeH__-IiuPglYQfkIPg2d82JNqnySJO2RxD814wNMS61g6E8UwSUOFjx2G8lwxCaFVR5CkAmj_ve9U-E6pDeYfN6-Sf0OsrmwCYVQGdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W471BZejw_qfZnbKl8df3A-m9CO-jaiSCnMn-UwrJcxbj9ikr5cVxNrqssE1NcK4JbVk1Fwax_-KsYMjrKp0aoTl_hdC0Alt3ojpGN_88v6Xq7oZM_EHOpQMrOpBGHdmujYxZIe1IrN4KGaIia6P13tjUdwwSw4-R13cNrWVnA_5qmduKCzNMFkNnbucGYdT3QFx_k1y6wPr4nQoj7lEe0wsji_VYQ0aIMy8ezopLge5lcVjlKES5Xpe6RtqTGTwgXNvRYyh4a8mOVpbS3zZ2M9qcO3nheUkV3bvSwYQLa43v9AAZ8hdwm_uf03NAUhWftjPQ6KEnaFOBytS4j5j6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjx7QB24TPpRLdIEuigtwyxgahbC2mxrwgQbeEMCTRxSJLx1ltmJ8eZzzobYwmTFz3Jec3aXm7xOqCsMBgzyvKrvNTwWdRSHY1vaC6rAVAaPoGZu9pZEFBtSkVBsJsAkqs2tWQ964oZOjqpNRN1oJ2NgP-fZDwVJVYvk5YPUZK7ETouSuNEQlO2rdE5KFljeE3XptuM9EQupS9WyoWLtUO5l9ajQso1B0fSv6BVPzyJtt0v_nDP9ozycQEf2XK-LTLcjJiIp7Jp1wxJ0I8MfLfX9BesFFGq42GJcace1Cvjc6gcIMxcTXFp5SGLwRUWRsEUri44PXEREc2lJ0DckRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72478" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCtobgxCo7xfKMPp6lKxTg9e7tHEJvRkqrX_5ArrKMAuSqq8bhCxQfW0RDQpC7MVxajhc9_4w0l3feH7MYWsfia9UjBpeTD7UCSk0PXmNrjUpch5CdfgaHLoO1EzsRXWdZgmsxx2lFwTqSRB1d6K7JRL27N9p-hAIq2ETEFcyodvoAlmTDarItmsO6NfeMLWn4ntSYR_msnjgOKCPFzzbJsunBdEhew4PAnQvgGgQlIARp9LYNRNZeKUbE2O1PCvUwot3y4zZ_OW5ih3dJXE8znIF41gO4gMyLGaEP0XSLenFt0Ls7WaNw98_s96aSvi3AV_lzPhszkwfCDwTjMnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Nhn098TEHEaP7p0A3VDcwTeCe1otoOIrVCVyQwCml25wB-1-Kkl3MUYUR7zvIrR2f3zN8qun-Vd0sCHJOaUj6Sop2n3sZarEBqgWv89WlM6nkBSNXtCcIIS7LTGAjzyG8y2cUO7pQn-OyhefPAKybH2z76_E3i4nkBG8NnqBEqy0ar1j-aAxIGd5IVahs8zC12XOr0WWLnaAGL6UsebSjfLbC-D_FMFqc5kPegw5O5BkWKUA4fXoqyFQ2PfgVnG-O-NWcinNuNXhRBSULFXwC1uhNO8N0O91Dss3K9PqOl-CRO5z2kAMTEq-DiwI8t71CvkmOGS2hE7nPGwF39-Uog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Nhn098TEHEaP7p0A3VDcwTeCe1otoOIrVCVyQwCml25wB-1-Kkl3MUYUR7zvIrR2f3zN8qun-Vd0sCHJOaUj6Sop2n3sZarEBqgWv89WlM6nkBSNXtCcIIS7LTGAjzyG8y2cUO7pQn-OyhefPAKybH2z76_E3i4nkBG8NnqBEqy0ar1j-aAxIGd5IVahs8zC12XOr0WWLnaAGL6UsebSjfLbC-D_FMFqc5kPegw5O5BkWKUA4fXoqyFQ2PfgVnG-O-NWcinNuNXhRBSULFXwC1uhNO8N0O91Dss3K9PqOl-CRO5z2kAMTEq-DiwI8t71CvkmOGS2hE7nPGwF39-Uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=bJi5d9ZK4_1An2KCtDUq9cbvLbaHHLHxh94KZ2xepHF5qF7jdydqkzy1eq1GhGqLGFYQV8GGBa2vsXShZfZK31bkVHX6wp9Ce_8LgUGOHnQSm4zmxF4VGJYqcUXJ-YiY2Uly9WLdkrkNk1eqnlHFbE_zbw6jmqbteZRJTEEkdsPZyjuirg0zag0JVESasZ3SGCClhiuM3jL7g3avCwZGyqA1RvB8uFJUN2Q4M-eSOINBKymeimVx16qrKG6fGIghfjTAQnWDIBdMCo18Ak2zxmLWx_agYDzC4ThSFDsUA205UjIak4cRxH3FP8_O3woHx53IMVnRcgAkOgG33a3WBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=bJi5d9ZK4_1An2KCtDUq9cbvLbaHHLHxh94KZ2xepHF5qF7jdydqkzy1eq1GhGqLGFYQV8GGBa2vsXShZfZK31bkVHX6wp9Ce_8LgUGOHnQSm4zmxF4VGJYqcUXJ-YiY2Uly9WLdkrkNk1eqnlHFbE_zbw6jmqbteZRJTEEkdsPZyjuirg0zag0JVESasZ3SGCClhiuM3jL7g3avCwZGyqA1RvB8uFJUN2Q4M-eSOINBKymeimVx16qrKG6fGIghfjTAQnWDIBdMCo18Ak2zxmLWx_agYDzC4ThSFDsUA205UjIak4cRxH3FP8_O3woHx53IMVnRcgAkOgG33a3WBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=GRGLpMPny7u03Fkzyn4fLBcV-r7MeSQjBpdRyvXkv0NGXsDA7Q8OZxBqc1Id3qffRkaKQdAaN65lHxUAMShwU_b_87KhgZPU3iMQ8WUJVMmOdbejTdiRrwH_CO5t3FPuUhA6-CIfMr4gyZicT1OJh0INhtpYtAKvMh0KTt0mYbawo-MoA6EEGgcv7Rqe7z1kWmKq9WcBe6uDudmW3R3dAZaDozcgH9hSl9w4UXPm-nk8KkIUHBZ6vP7ndoH--CN6mNSLsinVnBbeexlRwueSkH2nKyaNE_aw4UyjJQOzSA3tYw4f9ZMQuDRlh3iJfh0P7H7n3cGbkHr_STuyMznRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=GRGLpMPny7u03Fkzyn4fLBcV-r7MeSQjBpdRyvXkv0NGXsDA7Q8OZxBqc1Id3qffRkaKQdAaN65lHxUAMShwU_b_87KhgZPU3iMQ8WUJVMmOdbejTdiRrwH_CO5t3FPuUhA6-CIfMr4gyZicT1OJh0INhtpYtAKvMh0KTt0mYbawo-MoA6EEGgcv7Rqe7z1kWmKq9WcBe6uDudmW3R3dAZaDozcgH9hSl9w4UXPm-nk8KkIUHBZ6vP7ndoH--CN6mNSLsinVnBbeexlRwueSkH2nKyaNE_aw4UyjJQOzSA3tYw4f9ZMQuDRlh3iJfh0P7H7n3cGbkHr_STuyMznRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=CRijocvA7xf9H7b0b4MACsX4ylq8lzwCNCENxT1Dp2dykmz_kUi8Bu-BIx6KkkNHk8kxqp8Gsk8czA_tvQjMbdy58W5LxZBdAwFBEZLThPrhFLirTcoFIo6jzEkK92SgnuCoLvnPB8A8QGo2XZZslZjE9KW_hpKPcSHKfF_j_8FVIrMmmk8hUhtgY9ocm69zRQZYGBdaELH7JBRO5ROVwxWT1yyFjf59jCg-NDAY6CKTYr6-Sa_d7ARvLa4j2auPT9WwUMYq3A6lpXSMvgfi2D2pfpAOvX2UEH11ZXSW0fCgwCBZ-8kLzexd9Dn-M7ARjoIu64EKu0QaZKKTa9wvZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=CRijocvA7xf9H7b0b4MACsX4ylq8lzwCNCENxT1Dp2dykmz_kUi8Bu-BIx6KkkNHk8kxqp8Gsk8czA_tvQjMbdy58W5LxZBdAwFBEZLThPrhFLirTcoFIo6jzEkK92SgnuCoLvnPB8A8QGo2XZZslZjE9KW_hpKPcSHKfF_j_8FVIrMmmk8hUhtgY9ocm69zRQZYGBdaELH7JBRO5ROVwxWT1yyFjf59jCg-NDAY6CKTYr6-Sa_d7ARvLa4j2auPT9WwUMYq3A6lpXSMvgfi2D2pfpAOvX2UEH11ZXSW0fCgwCBZ-8kLzexd9Dn-M7ARjoIu64EKu0QaZKKTa9wvZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=D1RQH_Wn69ayvWYqAYPAfrDhQ2fsUH8el1zWJfL8F5T77VH_edz690T8wReFMSCVYDPuHQ5IRS9Gb1XXjX9epGX8J3FWeH9UdastKnlCnRp29DuLEy9HJ3nBqGJoFol5G63TANTP00GB99vv_yU8XZo-jZl6-CriSd7lLDLYzjV9JjyGL0rn4JWYX_apzCWUw3WYsB6HPa5mXTwyi6TdnFl46pDlztIkMGodMIQgU50AUw4nnUKp97y3E9mn_YA9SRVtTvBhRt91vZQbugnIG_x2kFii2A-Km7Ai7S_G3mM7aFp1IjikPEc4XdfSunWHA1cDozDUamF210MP1jNVZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=D1RQH_Wn69ayvWYqAYPAfrDhQ2fsUH8el1zWJfL8F5T77VH_edz690T8wReFMSCVYDPuHQ5IRS9Gb1XXjX9epGX8J3FWeH9UdastKnlCnRp29DuLEy9HJ3nBqGJoFol5G63TANTP00GB99vv_yU8XZo-jZl6-CriSd7lLDLYzjV9JjyGL0rn4JWYX_apzCWUw3WYsB6HPa5mXTwyi6TdnFl46pDlztIkMGodMIQgU50AUw4nnUKp97y3E9mn_YA9SRVtTvBhRt91vZQbugnIG_x2kFii2A-Km7Ai7S_G3mM7aFp1IjikPEc4XdfSunWHA1cDozDUamF210MP1jNVZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0B3scnD4-vmBIIosgGVmSWnqHh_8vajezsKqlEqBI6S9dbS5R3fXUy5HRAM9PdU646ni8KPvR0onN7NJ3wPINDSVzs6BIZWIfW55pu8EgE58OHheb9brx-Be8D8tr3IK0D7594ilKNhTEG1w1MZJpa2HpEMPAY9vDLI8QUtW8K3i6lJpC430dS1hQXRyqdLG8yXJJaNFNSkjG-9AWL9SXmxLdpButFzYpG_TC1L2EeQBPZUes9GnTAct2sEl_U6svEtzGRmrDUri3lGguWxH6DHtYNsGyJ2veLVGzjeeeLAN-QNJjqCRYtGTjsmQybjZyzfB5QPqf3xzvWXDtjUi49A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0B3scnD4-vmBIIosgGVmSWnqHh_8vajezsKqlEqBI6S9dbS5R3fXUy5HRAM9PdU646ni8KPvR0onN7NJ3wPINDSVzs6BIZWIfW55pu8EgE58OHheb9brx-Be8D8tr3IK0D7594ilKNhTEG1w1MZJpa2HpEMPAY9vDLI8QUtW8K3i6lJpC430dS1hQXRyqdLG8yXJJaNFNSkjG-9AWL9SXmxLdpButFzYpG_TC1L2EeQBPZUes9GnTAct2sEl_U6svEtzGRmrDUri3lGguWxH6DHtYNsGyJ2veLVGzjeeeLAN-QNJjqCRYtGTjsmQybjZyzfB5QPqf3xzvWXDtjUi49A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=HNbkmxjZOCcKraHlm3cniJwrSlRKAHhO1KydWmRwjN0E-xfOW8yScPM-nbbGf3jbZ_bpc2xp0lPmxONmrCQR3ch7ZUlhdL-W_9r2eN0lvGuu6QLEySckf9gMTGYtwtsFIMY-LeuOm1OpqEghPVCF_dXy3KhBjjKPDR8M203SC-J7f6i_7OU_kdlzBb0MtOqKUmqVvxVhG9faBNh-z4Ka6LtwhiuNpDJDy_JJaK53FP-jlDb0gM7z5BMJ1NyugTzZKYcSktvUNz8B28PWlD054G67vS7Az_bamuuv_rBTyMZjKUoa_6iT3RPEs1s6hBw7wQurpD0qwB4Tr0qAy8Qw7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=HNbkmxjZOCcKraHlm3cniJwrSlRKAHhO1KydWmRwjN0E-xfOW8yScPM-nbbGf3jbZ_bpc2xp0lPmxONmrCQR3ch7ZUlhdL-W_9r2eN0lvGuu6QLEySckf9gMTGYtwtsFIMY-LeuOm1OpqEghPVCF_dXy3KhBjjKPDR8M203SC-J7f6i_7OU_kdlzBb0MtOqKUmqVvxVhG9faBNh-z4Ka6LtwhiuNpDJDy_JJaK53FP-jlDb0gM7z5BMJ1NyugTzZKYcSktvUNz8B28PWlD054G67vS7Az_bamuuv_rBTyMZjKUoa_6iT3RPEs1s6hBw7wQurpD0qwB4Tr0qAy8Qw7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=D2cYeIU8Gnm1idJZfFuqcghFs4k-ozBtVibuczC9YiTnE7dmIPQxyY4ptcCZ4yGdtmGS8HZ_bPz05CQp0tFferbNqS_LkPPwN4VWTuWquzcqSKMR3_tDpKtyuYA50ZeNRvmj5OcsORUcqq_j9Ecxq9TnWeA7vY2wk6aGM4c2oztn4wfMHQLYiEElp-Xe3i-wNS-vLolsnYzlTkSd6UuYEIxgMlt695FunKfSg4sn9dwUcuLx2gyOgDebj8ygDGdt0EJPVDYJll8NnRAVIDC-AEKhhYe8RwhstCJE720S4hl04Z7-2JSF2FVU0l4VOXTzWD6YARQuBkwmDDf_SlP0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=D2cYeIU8Gnm1idJZfFuqcghFs4k-ozBtVibuczC9YiTnE7dmIPQxyY4ptcCZ4yGdtmGS8HZ_bPz05CQp0tFferbNqS_LkPPwN4VWTuWquzcqSKMR3_tDpKtyuYA50ZeNRvmj5OcsORUcqq_j9Ecxq9TnWeA7vY2wk6aGM4c2oztn4wfMHQLYiEElp-Xe3i-wNS-vLolsnYzlTkSd6UuYEIxgMlt695FunKfSg4sn9dwUcuLx2gyOgDebj8ygDGdt0EJPVDYJll8NnRAVIDC-AEKhhYe8RwhstCJE720S4hl04Z7-2JSF2FVU0l4VOXTzWD6YARQuBkwmDDf_SlP0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72459" target="_blank">📅 13:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=CAfacO-FvfuMK4fWFwNQ_5Mh7VObnBCkHS_6r0EkbBzwANQXMP6bx1toVHyZEtrA2vUAh0G8LFv1hC6XMSdjYUHiL-7BnYnAeYVvpfW-AVaySNOcZAWIVhiA6EVsYUBxqf2sI1m0lEE5peM7WFsb-feb-cYDsT98jV6gJmTegDgP0_4Ipr7JXCpegKKGv7NKbQeu6tV5NQ3zazo5PIAEItSEjM5brLoB6UjcvPF0X-HJGyqW4dCHVwqCTZS0a6kyyvNNny4cKlXChbz4BbWdYVG7pylfuyQdF53Yy66-4qKDq81M1H8Ye2fqHkYLL9pY99iLzkOIysWc9Dp-zdeN0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=CAfacO-FvfuMK4fWFwNQ_5Mh7VObnBCkHS_6r0EkbBzwANQXMP6bx1toVHyZEtrA2vUAh0G8LFv1hC6XMSdjYUHiL-7BnYnAeYVvpfW-AVaySNOcZAWIVhiA6EVsYUBxqf2sI1m0lEE5peM7WFsb-feb-cYDsT98jV6gJmTegDgP0_4Ipr7JXCpegKKGv7NKbQeu6tV5NQ3zazo5PIAEItSEjM5brLoB6UjcvPF0X-HJGyqW4dCHVwqCTZS0a6kyyvNNny4cKlXChbz4BbWdYVG7pylfuyQdF53Yy66-4qKDq81M1H8Ye2fqHkYLL9pY99iLzkOIysWc9Dp-zdeN0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت : خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
خبرنگار : به به خوش خبر باشید دست شما درد نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72458" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1910edd949.mp4?token=Gcma44LxDu2Z4X6ImlyckKXKrZONeHEv5ZGplHRMt_8-MTtKZIX8iwnQcLI8ms57WLymZcRGBWbSHvxL5wbBND9_T30dPXkKSk-j93OHB-Z3lRDgjY9eIe9ZHcnfDRLPcqH8a1-wO-nDshZ_vstHVnBg_A6KSFO2_3bwZ5opT8-BdAT3xCY0m8R_F2bqq48Df_Xp0--Tfe62Km9dl5Wmffjo-gEFtE9MqDIgaNBdwuZsf9W4-WaATrLShEEtK_2noXH848E33yOEz3MNoVJDoAqfSyU2L2WkDvBpbb2vFebRAwhiAZmF540SjsEz2Xc42klXlKSPx9Kvr0Rh96mTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1910edd949.mp4?token=Gcma44LxDu2Z4X6ImlyckKXKrZONeHEv5ZGplHRMt_8-MTtKZIX8iwnQcLI8ms57WLymZcRGBWbSHvxL5wbBND9_T30dPXkKSk-j93OHB-Z3lRDgjY9eIe9ZHcnfDRLPcqH8a1-wO-nDshZ_vstHVnBg_A6KSFO2_3bwZ5opT8-BdAT3xCY0m8R_F2bqq48Df_Xp0--Tfe62Km9dl5Wmffjo-gEFtE9MqDIgaNBdwuZsf9W4-WaATrLShEEtK_2noXH848E33yOEz3MNoVJDoAqfSyU2L2WkDvBpbb2vFebRAwhiAZmF540SjsEz2Xc42klXlKSPx9Kvr0Rh96mTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار افراد از پنجره‌های ساختمان در حال سوختن آکادمی علوم کی‌یف، پس از اصابت پهپاد جت‌سوز روسی به آن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72457" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=qU5hSgPp66Hqp_neMkZ5OhqTxcu9pHbqqa0EsOVCvLyFQTbBJO7efS4r_k838GzdpA4NSc0X0oeLIaLClZkX8CTJLab0Qfn16ppGoqS77SD2q5J-w4kvkEyXygl0gJMftPYDeKLOGvY7PqUxDe79nNuTxE3s4CLHXOIxn7dckxO3naFUq7mxsKoNK8XlRH4tugC7iSZ7mdiqsOpSIzBBbhYg7t1L2YCd6Br5fKSeKhE8os177PSqHyeLGz7GNRX20G1q0uiba5pVOpVaofil8rr4okbMIDMnUqeL71FY60vqC25EhhxuTYWia8MEhJo_85gbDJLBxbMAViatDfRgiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=qU5hSgPp66Hqp_neMkZ5OhqTxcu9pHbqqa0EsOVCvLyFQTbBJO7efS4r_k838GzdpA4NSc0X0oeLIaLClZkX8CTJLab0Qfn16ppGoqS77SD2q5J-w4kvkEyXygl0gJMftPYDeKLOGvY7PqUxDe79nNuTxE3s4CLHXOIxn7dckxO3naFUq7mxsKoNK8XlRH4tugC7iSZ7mdiqsOpSIzBBbhYg7t1L2YCd6Br5fKSeKhE8os177PSqHyeLGz7GNRX20G1q0uiba5pVOpVaofil8rr4okbMIDMnUqeL71FY60vqC25EhhxuTYWia8MEhJo_85gbDJLBxbMAViatDfRgiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA-G6guFxgeX8V89rtjAfAAE7OixB_ljpYH2W6erp4THhH99OXjyaDd9BKMBfyGIXcWdm8IWMVQ4KdIvx0byBoUESxdHuNBAAJPkaa0aB70bSOcX0bWHDTryPWrTh5rzh_CHoDCsVaEtlZsLKsPtgchKGdtDPe71y55PJw_nWewmMRVeUxJ4aPC1tedGmXfQMZJ_CXD7cTFnGLqb7wBA1S9ahkzqf8PVLnmDloVH9eLrc1-WpKyXnvYj3Tmpk1stbanLYbFlV6xQWAdmb6S9Zntz6QL9iJ4ZzjesbFdqr43eamCmMnUTav-1ruoslHlz9iVkPCMSrICLBHe63W5tWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xes6IPuzptEHwEmJ5B07Ot-ZWeD_SGV_e2d6Sr8lttCyYn3s014nG1OTX-lHi1GLVqdxfo21cniZO_iVOFodlkBL9XGl5ugK56hSqQe5z0-iA4EBIBzox2f1mC0nw5wy0Q74P-6EbUvxZlS0y_76boG_j0Sh2h4o0gh1QYjnGzWTn9jsTxDakogkvy9CR8z56nRc3EpyZViSDADCb3Edje9Nnw2cZ44o5L6Wgyln57OPw0kf7DzpDzEVe-VE_OENMO3prJ0mQooyilKtRCkPtMAWtFLxAjaSNz3cqcAevEbPlFNrBsB_XEX8JBZihmPEZTxcw8yckjXwOBq0816Pyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=Lj1Y7g7Tsw2uoV3u7HyZ9EcLPmekJ9qv5LnlyyOcYLEllxQfk_hKmoB6C8AOrFedtppNb-qBBH7PKLDTsni0mUB8e6JE4fml6JBmkVRGQAslbu80BzanY2ZJzmC5-CIgfWU_0Qi4O7lBAL9kb6B398rxhICmStDt86YhUNfaqrQBvTQ-6eo3HKtoEnSbl-X_ig1D-yVrSp2K4AmFHGjD8k1D2LR0gMUX-_sDV9ijZAqrKg8P7SoM6BbBsIPC_alSIPYsZ058geYQKv6r-wx2-2qKWv5ipYPMdoaK4u_oB_zYZAX4NeWPKvIhQ5tG-0QMMPN7qGLeTrp4mqueQ8C_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=Lj1Y7g7Tsw2uoV3u7HyZ9EcLPmekJ9qv5LnlyyOcYLEllxQfk_hKmoB6C8AOrFedtppNb-qBBH7PKLDTsni0mUB8e6JE4fml6JBmkVRGQAslbu80BzanY2ZJzmC5-CIgfWU_0Qi4O7lBAL9kb6B398rxhICmStDt86YhUNfaqrQBvTQ-6eo3HKtoEnSbl-X_ig1D-yVrSp2K4AmFHGjD8k1D2LR0gMUX-_sDV9ijZAqrKg8P7SoM6BbBsIPC_alSIPYsZ058geYQKv6r-wx2-2qKWv5ipYPMdoaK4u_oB_zYZAX4NeWPKvIhQ5tG-0QMMPN7qGLeTrp4mqueQ8C_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=FPrQ-QFWfE1Z-3mJy0AjmQpNnfOCDI4MkT0lW6wJQALZpJQSWgRV95yhQh-Hj8T5-9Mg6ZpgUmqEhOKjab7OVdLW3OmvrUaCX9ecbxN6Hs7sH2c8SnEyayqkRIDcxW8dCOTROsd4S3xDSTAxGrGJ-5uJgIB1o3OL_K3rnGjlg1EvCcvUHikn0IY9YEUDZnVkMut-7yq9E5wJDGT1zKEMGYHL7pigMpNXeVfz6oHNiXLGBBzh-S68zge6KxPB2geRSpXUmj_GCEXnWmQFMEorqT8kcVbPlSPVh1wLKeqQ92LS5kK-nyF0g7Handy1kBOKlNaopkS5ysfvoW3pNwEyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=FPrQ-QFWfE1Z-3mJy0AjmQpNnfOCDI4MkT0lW6wJQALZpJQSWgRV95yhQh-Hj8T5-9Mg6ZpgUmqEhOKjab7OVdLW3OmvrUaCX9ecbxN6Hs7sH2c8SnEyayqkRIDcxW8dCOTROsd4S3xDSTAxGrGJ-5uJgIB1o3OL_K3rnGjlg1EvCcvUHikn0IY9YEUDZnVkMut-7yq9E5wJDGT1zKEMGYHL7pigMpNXeVfz6oHNiXLGBBzh-S68zge6KxPB2geRSpXUmj_GCEXnWmQFMEorqT8kcVbPlSPVh1wLKeqQ92LS5kK-nyF0g7Handy1kBOKlNaopkS5ysfvoW3pNwEyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ItKsiZKSjU3C9SVfw_6n-zBPuxAOZVPwPeJxLgmO2lqOO2McmB3rMle22bsEGzW4ohBMgwkd-I514pIHy5YI4J7AVgTccf-ecVt1auM5ViLlzLdeZw6e6oMCajtYJK-7t9OqssTVicd6Hvey9KEVHJz4jfmyEhzxJeHQPEhFV1Tsa90fDLiaPrrUIgVAfChveu7atqkzJwkV9WT4W022CTSfvmyaMt1Aq525BIZ-4OPs6w8sWSgy9exppjUv_VqUn1BPnc8nC3OnLTODKvtViBnMw3Jlg8rReHbGQst3fINyhQ4lROUU9JDDhcU-gOV2hun00v5Hmfs7DBb_6vDczhlld76eyVCxNenP8bYiSRGaFrTYsTSbbV2OEdQYuJLlWOzCo9KxhZy7ptGaVf3Z-MuImvBzWDnBxeIFH4_eB3T0CalvHkJQKEMpKtPkplBulaVRSEDwwIqoZwXQqvWR3AWVqcikk29SD_PupKVM45Swymz3inO_x79YhIehb5sdUpCreisQR809ouUV_ZCHqI0nIDrjKA4ER1oYIOgviWtgwMK4HC6Sg27pKe9N5YHRUb9L4h2kkOD_m41-C2WN1VfKrcRJVimOoyapEUGwDlXaEtM-Q-n62Qc603fGhrKB7WXHEI1zAhGEEHh0ocLv0eI97Y2c0vEFKTflA3eh5ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ItKsiZKSjU3C9SVfw_6n-zBPuxAOZVPwPeJxLgmO2lqOO2McmB3rMle22bsEGzW4ohBMgwkd-I514pIHy5YI4J7AVgTccf-ecVt1auM5ViLlzLdeZw6e6oMCajtYJK-7t9OqssTVicd6Hvey9KEVHJz4jfmyEhzxJeHQPEhFV1Tsa90fDLiaPrrUIgVAfChveu7atqkzJwkV9WT4W022CTSfvmyaMt1Aq525BIZ-4OPs6w8sWSgy9exppjUv_VqUn1BPnc8nC3OnLTODKvtViBnMw3Jlg8rReHbGQst3fINyhQ4lROUU9JDDhcU-gOV2hun00v5Hmfs7DBb_6vDczhlld76eyVCxNenP8bYiSRGaFrTYsTSbbV2OEdQYuJLlWOzCo9KxhZy7ptGaVf3Z-MuImvBzWDnBxeIFH4_eB3T0CalvHkJQKEMpKtPkplBulaVRSEDwwIqoZwXQqvWR3AWVqcikk29SD_PupKVM45Swymz3inO_x79YhIehb5sdUpCreisQR809ouUV_ZCHqI0nIDrjKA4ER1oYIOgviWtgwMK4HC6Sg27pKe9N5YHRUb9L4h2kkOD_m41-C2WN1VfKrcRJVimOoyapEUGwDlXaEtM-Q-n62Qc603fGhrKB7WXHEI1zAhGEEHh0ocLv0eI97Y2c0vEFKTflA3eh5ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlN4A2zbAF0R7Wg5eCVZ12y5J5EUfiAc6Ad6OzhwJaQuYVEfa5weHkVCOoDlBPUnu7gO11o57lo85Sci_n_LiLF_r1NMdIeUld1DCSVI3qshcu71_9yV9FLCYTWzFvhtbfCedr8Xa8_s9XOLc1gPFW4OwS_bBNcC2TUqNjavGpWuhhLmKQuU2AVTf2aidXQAUBIvg06GqSXBM6VdgEvLfje-SOvqsGGmcrYpUXQkNnNNH5ACvXTgrPsI8ICgRPDxyRohDwfxp33zZzu9RiLWeMQKokHldR0Plrfhe3UyIDYjCTlyeqRc6mXV7HhqrcKvYX-14qYv3HG2athBmDXKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=ZawPgEO9TMAKguMBhxtaKBhGEsHTUvJ2b8qO_inCUCFT3SQofkdmEzpjOv9TdR9acyk-LyPUj9iqoAEvPy_XWNaKfS_JyzNv8MsQbebvEi9aPNJH20RWYv92CUbUQvqcvdbrw8c4OTM--QkSPlvGqLt2xrutFJ4JZJWz9X9lLygooR2aXbc7qSNOniOFRCfh8tf-7qhltTgaqcOFrjPY81EBMQ9BDaVLgnx06aSXeEdrm0VOfQxJyx3xa9F4oVQEuAzeu6p3VMPHMzAeZFrR1viTXgB5B6xM5yCJ19Fz5i4gxX_si9tAMWroecvhUgiM88G1Njgc9NutnQLtepzYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=ZawPgEO9TMAKguMBhxtaKBhGEsHTUvJ2b8qO_inCUCFT3SQofkdmEzpjOv9TdR9acyk-LyPUj9iqoAEvPy_XWNaKfS_JyzNv8MsQbebvEi9aPNJH20RWYv92CUbUQvqcvdbrw8c4OTM--QkSPlvGqLt2xrutFJ4JZJWz9X9lLygooR2aXbc7qSNOniOFRCfh8tf-7qhltTgaqcOFrjPY81EBMQ9BDaVLgnx06aSXeEdrm0VOfQxJyx3xa9F4oVQEuAzeu6p3VMPHMzAeZFrR1viTXgB5B6xM5yCJ19Fz5i4gxX_si9tAMWroecvhUgiM88G1Njgc9NutnQLtepzYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=U5LIdRXgk8oIM8RiGKX_6kuXuC9Yy8GU-YrD5ksxI6HMwtcnYuhl9xTIItZbwwuL_on6moMu98oaCSUIHv5xSrdHp7R5xrCR9W3riKbBetjWS9dhPhPGUwYVQaxlGOcWMsMuZEVj4-6rhDLK7-X8xa60co1N4X5W8Q4WbnFgTOaq4bTk_pHZ9PHrdjp65NstczFJ_dRxVcC3pS_NLm6IEwFHEe2o1P-rjiKFGV2EBDvAyEo0_mNZ1tt4S9giKsBt8PpWtHoRQBK5d6vw8TUZYg7ZS3bu4n3HWf7DZyKYh4sSSp9x1O6cIqveVsocVM_5Q2Xsud1ycQ4w-8mGL0iYoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=U5LIdRXgk8oIM8RiGKX_6kuXuC9Yy8GU-YrD5ksxI6HMwtcnYuhl9xTIItZbwwuL_on6moMu98oaCSUIHv5xSrdHp7R5xrCR9W3riKbBetjWS9dhPhPGUwYVQaxlGOcWMsMuZEVj4-6rhDLK7-X8xa60co1N4X5W8Q4WbnFgTOaq4bTk_pHZ9PHrdjp65NstczFJ_dRxVcC3pS_NLm6IEwFHEe2o1P-rjiKFGV2EBDvAyEo0_mNZ1tt4S9giKsBt8PpWtHoRQBK5d6vw8TUZYg7ZS3bu4n3HWf7DZyKYh4sSSp9x1O6cIqveVsocVM_5Q2Xsud1ycQ4w-8mGL0iYoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4Os_AGedqSiUCciRNw8hq8tgq1d0ObS9NuOtUIl3DhiaL6zZATAEGYX3pDTlWEGVVLPXivIDuYuOdHmDzRSfrnwylr5kmmlDW_Fo3Zu5v0ORTcOIkPr3sSogHosCk2ytA4X5TrD8ni2xElgLvhdsy3j0nfqQCOsI_kZHivoWoAhHfRL1L6wVwfail3x2Ld9Kpu1ceFqp02dcOrQaXu542qP8EKTx4g5NZgEO2tDBVF0L1F49z3m5Hy8wUOFPNFPLb7Uh9K8XzZQ_OAU_Owq2TdAe16Cdax1VTK-xjtd1RbTQuYNUgUUzUzz212yAqXKgMY5CcMl8PC8ZdL6vwjMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHUD1Amw1YFDrrXIGchO5MAjeUPLJcLL-QS0QkaTl273ylX_XN3MHaAeJBK1msuBylDUSGDkS1Tq4XcUFJQcztrexvmdmWy_NXv8TOnAYzmC3IJuifyVQze5RsjyG12G1mD_G8SksC9RBQQp9iw2eQKWLT3ErRnAMYSB4Pl52Xub66tytYGx7lk_cDvN8AkoI1JrnO3B17X4-tOfHV4l6O2tlzytnK1HiI5OIoB7rPhtWMst0qQNhYfkp6H-kW0flrKuGnwOm3K-GxdczYWyqZ2wseMoJMBvheNJ9decA-d_0uc6emaFVtfr0xeT_Fzx9to2RpE2awo-r_osM0vr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=MUJgNQKHBD0KLKs1uKbRQDMCDveosLBmxIF6QGFI7TZiqIb9GuMLww5-MPX59FVd9uE4TEo9A_cM2C0IGv20NAU-mDkWY1itZGSaIt1-zUDFAS6OJdIEdP0t5x108Plv1_S62JW6R8EbK0xZ7UklQ35AIi6BrR-TNe1HUwpcHtPKEx53ajU29rXE1qQSj8xaoG0oGs52wqgHaXdgoCyj2wovtrxdiNqgCJcGhduZK_qW5j1z2DENWMtlZiyu1c5Mt1wYR5sXsUt9gVkqvIRzqQMiLimOMzhQu6HnaIaPMV-AMDQNV6smmhlCWuHMk6rB8zs6E9bXUBhoOQaVooNZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=MUJgNQKHBD0KLKs1uKbRQDMCDveosLBmxIF6QGFI7TZiqIb9GuMLww5-MPX59FVd9uE4TEo9A_cM2C0IGv20NAU-mDkWY1itZGSaIt1-zUDFAS6OJdIEdP0t5x108Plv1_S62JW6R8EbK0xZ7UklQ35AIi6BrR-TNe1HUwpcHtPKEx53ajU29rXE1qQSj8xaoG0oGs52wqgHaXdgoCyj2wovtrxdiNqgCJcGhduZK_qW5j1z2DENWMtlZiyu1c5Mt1wYR5sXsUt9gVkqvIRzqQMiLimOMzhQu6HnaIaPMV-AMDQNV6smmhlCWuHMk6rB8zs6E9bXUBhoOQaVooNZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=tS3T7jCL7Z0YDUNLr1ZWBMY28HkKmfPVKM4b4EtyMgxEvEel91eFagyqP2iW1kuDeOKlpIh9_OFC38sQMKeKiVktzQg5o45rg4uxPFQRIele2oNC2VeuzInkMwcEc3yeLLuPc8DmSoZhr8nWUPcc-rLoXLUFMoc1541EuPzGr1yJ2H8tbf2HLq0HCdHcUSpqVwKbckeVQa2Z_8j3YC8PHbqNgxRpBOuPfM9czg6fneSxOojCvc4Qx1JB1xWaWbNt8ZvrCiLrhNtavUBJwY5upbuzMDU3rDMUQTxeYBrA-8MnCNZPKQghWzthK6JAXuDdCG7yrbT27J7RWJMF5HaFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=tS3T7jCL7Z0YDUNLr1ZWBMY28HkKmfPVKM4b4EtyMgxEvEel91eFagyqP2iW1kuDeOKlpIh9_OFC38sQMKeKiVktzQg5o45rg4uxPFQRIele2oNC2VeuzInkMwcEc3yeLLuPc8DmSoZhr8nWUPcc-rLoXLUFMoc1541EuPzGr1yJ2H8tbf2HLq0HCdHcUSpqVwKbckeVQa2Z_8j3YC8PHbqNgxRpBOuPfM9czg6fneSxOojCvc4Qx1JB1xWaWbNt8ZvrCiLrhNtavUBJwY5upbuzMDU3rDMUQTxeYBrA-8MnCNZPKQghWzthK6JAXuDdCG7yrbT27J7RWJMF5HaFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=ORxVBslsrVTy3ItVEvIqO0Y092fY__xLiA304CB0aUYms0tBqt0SBX7EDwx6x94BcK-DUv3HofP-oke2zQIHhZdH5yW8bntalOqQb746xhRhc3VDm53TwarS_C5SBFehc1QTIgkWchvtO75lmSjUYJX91SUWqqzMVJ2B-S1LAyD0Kip7LUeoPJzeg4Hl2I0fXn1sGhFPVIdYhHzrHwkPXgpgJrXwn8eUaQnGYmh4P2lWmtD072iGHrfCbkNOPsL6YwqLtLzxmf3cdkOtu0z14614uXlTSmolpPG0yvqc4G72eDaHNfPgiu1C1-8lG7f5cJFOYxfqXX6UdP09biZLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=ORxVBslsrVTy3ItVEvIqO0Y092fY__xLiA304CB0aUYms0tBqt0SBX7EDwx6x94BcK-DUv3HofP-oke2zQIHhZdH5yW8bntalOqQb746xhRhc3VDm53TwarS_C5SBFehc1QTIgkWchvtO75lmSjUYJX91SUWqqzMVJ2B-S1LAyD0Kip7LUeoPJzeg4Hl2I0fXn1sGhFPVIdYhHzrHwkPXgpgJrXwn8eUaQnGYmh4P2lWmtD072iGHrfCbkNOPsL6YwqLtLzxmf3cdkOtu0z14614uXlTSmolpPG0yvqc4G72eDaHNfPgiu1C1-8lG7f5cJFOYxfqXX6UdP09biZLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=PSvTvXDP4MVzIOo3b9_FHnelIT0OZ3kPsrCZ9QSxxwsKe8BPwpC-Qc2OtrxvLHlsIu-SdsjVzNaKdEFg6oHaw_evb3nvybkroGiTTN3tGDG3nf_N-B7aEXj_5Vi8tmQjSeZdXQ-bGFzYs7AalYZ9_zAZ_pi2135aj63fZxyh_4UdhIjIA_AvZw2WXmVBaE0O6kgnGu_KWAUFWlVwlwdKp4cSm74KH2C5OCkYxKagOduq2A2rm-Mlz1qdnnHrGw3vksPOhHW6-joQbyiRnske6EUKjIbdXR9taZhZBsclEhxsKK22g6hjTDZcup1wKJF4aorDQdJJWSXGFNwmdIrnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=PSvTvXDP4MVzIOo3b9_FHnelIT0OZ3kPsrCZ9QSxxwsKe8BPwpC-Qc2OtrxvLHlsIu-SdsjVzNaKdEFg6oHaw_evb3nvybkroGiTTN3tGDG3nf_N-B7aEXj_5Vi8tmQjSeZdXQ-bGFzYs7AalYZ9_zAZ_pi2135aj63fZxyh_4UdhIjIA_AvZw2WXmVBaE0O6kgnGu_KWAUFWlVwlwdKp4cSm74KH2C5OCkYxKagOduq2A2rm-Mlz1qdnnHrGw3vksPOhHW6-joQbyiRnske6EUKjIbdXR9taZhZBsclEhxsKK22g6hjTDZcup1wKJF4aorDQdJJWSXGFNwmdIrnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=RQilbVjlyZDQcv88eLqSRu6kn2RxzLwNu4OsJT8SRfc_311gBrDp9dym7tuu7PmyJigDBKQ57Dkcibl7VZudXTitgYgWDnTkAoRgCnJIUm8ymqI5IZMMDi-jZ7yLf8WTr6s7Ur6lSS8LYE0Xc2n7gaIwqNymcsHSULTpXZA5mP5E1UaLT8imteqtqOsbaYWprvj0r80NPVbSbGkjJY4AlEQ8nTyp4xO562kcBZhfH1GlJxSL3W0pzYig1liB9Ff5qC1CZ8RtfOLraENTRLsDGF6zpOcyuxbIzyotmdQz6Ix1C34H5xvslx30o3RsXcke5emvCWPjTlXaL87zdkAvtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=RQilbVjlyZDQcv88eLqSRu6kn2RxzLwNu4OsJT8SRfc_311gBrDp9dym7tuu7PmyJigDBKQ57Dkcibl7VZudXTitgYgWDnTkAoRgCnJIUm8ymqI5IZMMDi-jZ7yLf8WTr6s7Ur6lSS8LYE0Xc2n7gaIwqNymcsHSULTpXZA5mP5E1UaLT8imteqtqOsbaYWprvj0r80NPVbSbGkjJY4AlEQ8nTyp4xO562kcBZhfH1GlJxSL3W0pzYig1liB9Ff5qC1CZ8RtfOLraENTRLsDGF6zpOcyuxbIzyotmdQz6Ix1C34H5xvslx30o3RsXcke5emvCWPjTlXaL87zdkAvtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=Pl25Mog6qQ1CMlO6CI1ZtI1g9nf_5hSLy7A2qZyQlTYk--5rW_As8GbSxbDJ9ra275-CaZqI8DqBtuLfyAd5_dLQ3-evzkkzP0jZnAiOB0Yqp_ssq8MiS2SNDNv9B40Fjpnj8NnYBgd4XtIFcsqJQ1yAM45QgIPIbI6BLE2CwRrB3Un__sPHYj9Biaw9p125X556pRWpjULtJQBTSshR2uJApeYHu32p9dAYGEIjn7lcnDRpkjW9R7s4WWCa9Oep5MYKgWOG79dAb86OX3EXWEYd5YTUNkfMRsil3U3bZRZx3q_ks6jXqTWzHxXmqlPKJdLnMxDpEcbdFVb0Z-33GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=Pl25Mog6qQ1CMlO6CI1ZtI1g9nf_5hSLy7A2qZyQlTYk--5rW_As8GbSxbDJ9ra275-CaZqI8DqBtuLfyAd5_dLQ3-evzkkzP0jZnAiOB0Yqp_ssq8MiS2SNDNv9B40Fjpnj8NnYBgd4XtIFcsqJQ1yAM45QgIPIbI6BLE2CwRrB3Un__sPHYj9Biaw9p125X556pRWpjULtJQBTSshR2uJApeYHu32p9dAYGEIjn7lcnDRpkjW9R7s4WWCa9Oep5MYKgWOG79dAb86OX3EXWEYd5YTUNkfMRsil3U3bZRZx3q_ks6jXqTWzHxXmqlPKJdLnMxDpEcbdFVb0Z-33GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-vOgroNnCcvmDMZCo7b3U0J2n7BV6DnK8JC6HRvjun_QRQYVhWlvKI38iI4J8ojZ8SLHVsXs54cWznKd7OFUL1Ctum6tVNwRHuB6ofB9mxqXZei6DKSYnj_iEV41IKGo7SzEJC2BBzcoAUUQSpfN1U0wW_J27yvFWDzgztb5-YBSL-Zoab0hEYO84beFZS9LCUFA5fEii6rR_CK4XZMyeZf4WaLqfeYcrBHrleJP8i05_PaFe76nIBSVzc03VpIAb_F3hCLtHm9jevUSkWajQcFjM3We62VaD6fEr5N3WSzOvJ2SQecG3vqQTF6xeZDTnk7FDxQ7wrEhiVZkueVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmbMZTDtmA5wQlw4rePHD_GAw6YrH98mxuRTn7_fkwhuaYT1VJAVpYsAmWr-PmXD5yX8uI2eLqaAHogG5Q34LKHLfWTDF3o43AXIskWHUFsYRzxE1t-3rOeippQqs9_TrbfE3HmS-la63A0Tc8FDCV4NmkH-OwAR-6gaDDJ6jghtWiwId4rrFr615rki2NgAWdLf25JcKDWp3JuiP_RA25y3WQxUJX_T3mwEv5qqYA9jQcKeZnwbQQPxFKSwHLZuyB6DtYgj70xQ1RtJKwu0SXYChR_aCdUzhAG2tiHRKEGbRuaOM-oa3x8NwXvDlAbFjtRtY14cp7pLAQxD50RGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBiCrB13ZTnCsDsaKV6avf8twD9ggKagBACNRemc3OvexGcj7Z0dl2jyf_lMaCIEgylHFHtNAY5c3iv2Zcy0OzIbXNTyYIx3r72Daz-2e6WKHs9ZBy1qfiiMmmtrL09PLa-05ErvY3TlIJWEN4kHe4Le9Xfy20BgD4eu7YHppBm76_EyI-FvSEivn0sl_PhkXAqxozj7cFZqyyDk-JyUqJLmuN-Wh_EcRrVIWzJIW8z3z125QNAzL0KzHB0rgM2A-XU36zOrK0sArDqC4DehyVFzuGklmWKlC32S1EbpGkA9QmmHPijhx5hBcy2yovV5FRrHyObkB5UNxFb0GmuoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=SKkwDLICg4M7eeqB9FMYYjmx7Q9OSxGGEI8M4m8iGEbL0yMN3oBclhozqr_j0SO6dloSpE-VO1yna63muNCS29tA2mE_QB6-mvO9mH4jAuA-BdBUgeQIXCrT1Y8V05U1kaj-s51z73vikv0PjNthgBLZQGZJplYiBnkgHGTQ4Xj1QfID7E4SYrfT7bM2_nROeEBOL8IS53O8v_ZDhsQJg0fsKD8mvUPHZ7BApbcZ82fSaPyvLbCexC4YQegPueUOGzI5EeT-zpIfZcC9P4DEVpgIxaJPvYSM_-UrhOAluvcx1HxQmpEdWSHxMM4yE9v7_K7jjEwzTeJ3tk86omImVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=SKkwDLICg4M7eeqB9FMYYjmx7Q9OSxGGEI8M4m8iGEbL0yMN3oBclhozqr_j0SO6dloSpE-VO1yna63muNCS29tA2mE_QB6-mvO9mH4jAuA-BdBUgeQIXCrT1Y8V05U1kaj-s51z73vikv0PjNthgBLZQGZJplYiBnkgHGTQ4Xj1QfID7E4SYrfT7bM2_nROeEBOL8IS53O8v_ZDhsQJg0fsKD8mvUPHZ7BApbcZ82fSaPyvLbCexC4YQegPueUOGzI5EeT-zpIfZcC9P4DEVpgIxaJPvYSM_-UrhOAluvcx1HxQmpEdWSHxMM4yE9v7_K7jjEwzTeJ3tk86omImVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JnvXljSZR40vux78Gc9SgZjKLLQnwDrWvocA_Tkn4j0EYJct-3q4c4b7YHBMiTDHBb9d6zf96sR6bk1fyBlKUiMPEr4E6lIWDgtaOzBoc1El0YN6hAPje48-ZQ9H5KNnUKoGGtCnzMUcg8TmF--n1smA9m_TKv-T--dFnUKlETA3NWm3tQbypE3N_TT1TfKaxBjuF-ZJoM-36Dk6JYLLv4VVjKo0vR3GNyG9f6Ke4En5FnAiYcsw311Qs2lSTFQcHTIeDCIHXCHPYPLAV7-cXF1q0qwArJt-rGl3fD_xUlk4LviOmsQvqVpqTB8Jxqm2O0pcrcKS0ysnmIO1zb-lHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMlm4CtqELgt3fUCOH2m2V8TRd6vlLiqqeD-ZC4o_RRO-TioFRdsF61-T4xS8zZxNrUo_1XnL6Cq4KhgitSsDT1nYimT2YeAwuALVeaSzlJ_arzExM-7RkcwuJra50PatghZuNHiV0K20giAC7mFHl0VkMto4CJ7MIuMqYYTYb6X9NOX33R4EuPcB8JgRq5mqalFnpbt92DiKGcLFmNJwtFPYJzo3ARd0w930ldl5j-DIu0oKxO2sRdJCpzXfkFp2wdUDqPz-nyagRWj8ZdSfqC1jyE8TOZ7QbgMo5AfqoKpPSPQT8sEq_tKR7cmIwrXNWG2Y2g_j0kJEFg8QaeZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRpb10FfbZmazmAKG3-XMNRF1kdYpFl23N1rele82mfTh_RB-bVeYTn5pgke6PrLCSH93gLACQlkpbYkaYjt1rOabWYgO10gg8E46gM7jYKGzEwndRSWClcmxSiJEaLyiw8BM3OzZybrOb7ySKuR9OfxW-IOMIddGDmfeIgclyKsNNAHgKf22Q-LR7thSFfT8DGlhPsM6TMM8YOMMqPqI0Gy6Gn7-qrlLbCdHAQZxEwxQAlxh2kOGYZUk-h0sYYGPFKQbVRdCy3Xu5SSB10DHRWmFYIotNwyEleY36stdfWkmutaKIBwCSYNWAUenlI47BelQG3Eali-VN3aizKwNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=rJhI4QHf1q5_VCIEyufQ6vBZX9oZakb0qM0gLBNKOgFaN-9ZM-RDBTtBKHjb6c8v6EeeOt7PzIaYAobHFQ0mMipLNk-U-J5OAfbx1S8Sv6jtDL0n5Wa6kN65rzoH5XgeA5glxdzfob-ecUff4II7i_I-ckWt69ZWdx27gVvYDZlzJRbSOpxVUqs_RCNBG771TFr0utGP08XifovFo7bHSixfQjORebRc30IJPV7YFpWxMCBzrFbU48Xjq1jQqorvi90bKJFXZmU47DyAq_GmlHT71S7ujlvQddyvbtbQzcmB60Dn-yVOWDlBs7Kut6A0-qHhSzMNCOfBeejB7DSWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=rJhI4QHf1q5_VCIEyufQ6vBZX9oZakb0qM0gLBNKOgFaN-9ZM-RDBTtBKHjb6c8v6EeeOt7PzIaYAobHFQ0mMipLNk-U-J5OAfbx1S8Sv6jtDL0n5Wa6kN65rzoH5XgeA5glxdzfob-ecUff4II7i_I-ckWt69ZWdx27gVvYDZlzJRbSOpxVUqs_RCNBG771TFr0utGP08XifovFo7bHSixfQjORebRc30IJPV7YFpWxMCBzrFbU48Xjq1jQqorvi90bKJFXZmU47DyAq_GmlHT71S7ujlvQddyvbtbQzcmB60Dn-yVOWDlBs7Kut6A0-qHhSzMNCOfBeejB7DSWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=ZvtocUWSfdEs0VX64W-EOk3OW_tgoyIIUEilYnAeHu1me0l4ml-3bkg4oPS0uaurBDIgxXWDIHwxT6LPlYNqQz9N9m_l_C3TrONz4qKBhkOGgfAXwWFWQNUUd7dNl7GB3OvjpXR3b9G7gT0MTgaE0hJ4HWiuA09ySVcppzA57fGlX0j6IVr9RG_v3K07seh2uWYedEngO-pqa6Be69t-361VgaNkBBD-tPgrKoI4dRCY6z-w7vGAmXQsOqAcjckrE4vY1LQOu1uMu8YN44AxrRTOGXMGYJbvwdrpN8WhjuBEx5dz_UlHqBkM2mKYNilojfSo2J_nW-CIoQu2uyOtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=ZvtocUWSfdEs0VX64W-EOk3OW_tgoyIIUEilYnAeHu1me0l4ml-3bkg4oPS0uaurBDIgxXWDIHwxT6LPlYNqQz9N9m_l_C3TrONz4qKBhkOGgfAXwWFWQNUUd7dNl7GB3OvjpXR3b9G7gT0MTgaE0hJ4HWiuA09ySVcppzA57fGlX0j6IVr9RG_v3K07seh2uWYedEngO-pqa6Be69t-361VgaNkBBD-tPgrKoI4dRCY6z-w7vGAmXQsOqAcjckrE4vY1LQOu1uMu8YN44AxrRTOGXMGYJbvwdrpN8WhjuBEx5dz_UlHqBkM2mKYNilojfSo2J_nW-CIoQu2uyOtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=FdRFbhfVn9YuyEFH8opofRUBjoQ8M6hDLhOD9wkHrVUlz7lP7vKCAEPKygz1Vovi6fMSW1Hu1anPZYycV0RzHwLsczvegoyB0B1uU_X0JLOsCUCs8zm0VyBufceaTJhi4a9gtWzFkQosBcC62YFzG3RrNFV3KULzD1gsPlOKlOrPbGpzD17bD2EFAn4LyvQDHEQ22MSCHx3hbZoRugyHOtOs0Q-1iqK_p9PWpoSh0MNjTOw_stsLkx6k41_T8wH73AhZQMpCW28mN2D92IN1Xj6XeQbFjDdmd3ob8bykYW7DSweReOFH1UdIxsL4nFyfxs1VZ-oXfGOYBwXCat75sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=FdRFbhfVn9YuyEFH8opofRUBjoQ8M6hDLhOD9wkHrVUlz7lP7vKCAEPKygz1Vovi6fMSW1Hu1anPZYycV0RzHwLsczvegoyB0B1uU_X0JLOsCUCs8zm0VyBufceaTJhi4a9gtWzFkQosBcC62YFzG3RrNFV3KULzD1gsPlOKlOrPbGpzD17bD2EFAn4LyvQDHEQ22MSCHx3hbZoRugyHOtOs0Q-1iqK_p9PWpoSh0MNjTOw_stsLkx6k41_T8wH73AhZQMpCW28mN2D92IN1Xj6XeQbFjDdmd3ob8bykYW7DSweReOFH1UdIxsL4nFyfxs1VZ-oXfGOYBwXCat75sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
