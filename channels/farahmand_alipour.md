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
<img src="https://cdn4.telesco.pe/file/LwVhhoeNiDAe7HKkaMgAjFJxme7TH6Ljr8xjrIAEfAxDv6mk0nIYUY02JxlpJwPjarQWsg_Wp07Pq1jRQM6R-fNe6npJlFcYlyBJfKa51QkWvplNOaRi6KZhy0coCntnIg0XQ7I4YNV_iP5s5EsmEMqKUxYOfleJisRqtYcOaGM0rkB5ZjoapxO-q71TFmQ1Ot-jpRuWft4zPkAVBHDE9HXu7eFc_9e-pUMsddskOWm0wmxXj6eZmwuXjv68VBHSb49DM2uGYt-JYF33k8s0DpwdOPmAQqq3AX_hOvRHw--i_snRzM-ognOtdAkzXBgEWY-Q7mhh2rEqz6J0kWwC1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=E0XQuEv2kYzHcX4HDdjJaiG04TWTuu3FLTR4wOJpJt0Kom_E_XerG4wmoHYCY5sal_NMr1pep6uHOE5EQ6Sas6ZVEZWDZgUaD0oqtA5RNLzkiKZJOfpjfp5pGGnqluOKZQbGUWP5SKOAz-8NFUJ0bUfcsF2hVXmcoLGeZ2L5GdjGfbwKKLdjuokgZB7txZaroRCiepXp5SSi8mwBxsQaHnSDeg6coVgqHWXQKg1vzEjoCPK8VncjZcSHzW3ldBpCTpiHi-XZgXdpH_Izz-5lwAcpYeEJ0rQbaBIMhYVtVa-Xd6cZKhwfJtcvsFyah0dvGihnHsm7aoLkXt4CTS8Bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=E0XQuEv2kYzHcX4HDdjJaiG04TWTuu3FLTR4wOJpJt0Kom_E_XerG4wmoHYCY5sal_NMr1pep6uHOE5EQ6Sas6ZVEZWDZgUaD0oqtA5RNLzkiKZJOfpjfp5pGGnqluOKZQbGUWP5SKOAz-8NFUJ0bUfcsF2hVXmcoLGeZ2L5GdjGfbwKKLdjuokgZB7txZaroRCiepXp5SSi8mwBxsQaHnSDeg6coVgqHWXQKg1vzEjoCPK8VncjZcSHzW3ldBpCTpiHi-XZgXdpH_Izz-5lwAcpYeEJ0rQbaBIMhYVtVa-Xd6cZKhwfJtcvsFyah0dvGihnHsm7aoLkXt4CTS8Bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nmaxx-dsW0yD5rsxPe8mtJsXiQA8ngv-N5qQMnCro6q9GyAQlnAJkzGestmUN4zRa4jycsxTvtMWMpgHt0fkgNavNEw2ysBdTrsT7l4GNMr_Ytuid2Xi1uB2NOB6T_GAF2sxyLupybv98S_K5pVbtAKTn92SCElP2cesEBKWQ7V9rmEHnhVM1w3-yUjK56cAgvyRKFrJ7iJziK8E8c5Bb5m2wwO1R9I4_h0syys0PzTBbJIRyT0so45pLLo-nesn78_I_Y6QxDlT7szIxioIchbjnnG4hbAsV_yTsMX5NSTKSCWMo4O48-28-VsytTSCxfSk7uTVS9iiWFzqCqCoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNM_OZ7ty6uOSu6HvfJpT8_pfg3ts3v8cEDr0geIFPDbPNZ46J41MA6bqcIcgRVRNLDOxIea7di5DQKg-GgAubiUewxJ8GNpndZwh4AEK2E-4JX4L_IdyK5XD1hwvebAxbvWOnMmTjjs7rffyaN5qGk9I7OB4YUadvae_UmNmOD5NsYGtpv0XmDzrNr6mghqR0P2ONn4pdSZQTIwUJYHOu8nk2-0X3qiuJTlR0GTUuPYYXrlVZwWJG-pT0o8Flry0HkdJO63hORiJ9s9q5-ZsRjxwGzeWxKsGlZE6V9g4l6dAmK6ZNJXuoUwLCXZiizBSrA74FCzWACSkJKHvyU9Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iEJ1792nZ0wwErbDdLKKwXvf3GGIt3bxnOcE9Ic07IqUny-cBSw_TOcFf8MY9KGPZPluO3FjxfdbnHpJ7c5fNV5oSEbO9dZDFUW0OTahpvD08BeT6Up8TfelECR8pb2OUun5nk1fMm8L8zqveY1YaSt_e7QE4BTceD93XishPydi2CWHCu7f88f8LzNyl6VAJRDI0hN_0QJGa5aGuICneM0be9HnspiC6yIZ8YZHwdaBdpNIGD4Vn5D0yZWbWw4E66w6FxED-2jfkcXBsCShtMm092Ey1WUaUBUhL5PORBKEHT59HYR305oiTwAYdQreBkgsYm4Av7MnqOOEu2EqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iEJ1792nZ0wwErbDdLKKwXvf3GGIt3bxnOcE9Ic07IqUny-cBSw_TOcFf8MY9KGPZPluO3FjxfdbnHpJ7c5fNV5oSEbO9dZDFUW0OTahpvD08BeT6Up8TfelECR8pb2OUun5nk1fMm8L8zqveY1YaSt_e7QE4BTceD93XishPydi2CWHCu7f88f8LzNyl6VAJRDI0hN_0QJGa5aGuICneM0be9HnspiC6yIZ8YZHwdaBdpNIGD4Vn5D0yZWbWw4E66w6FxED-2jfkcXBsCShtMm092Ey1WUaUBUhL5PORBKEHT59HYR305oiTwAYdQreBkgsYm4Av7MnqOOEu2EqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3Mioj4XvEWutby4j0MYWIyMdspaROqB8gqxaUB3WpylH0ouarH-x_9idt8fsjn3T40xeQPZ7AgU8BGqkJZ-K-nrPeUhTt_OcAkqyRfZVEjtIb0j90D29_SgHkg-kJsMoXNkEszSiVcLbNWbAjPbmr7Epz9Ks-vq94Sxb2M9o2LdpQOAgyDMdRCVjlqdpbD2PtG9KebIz-dRQ8g1IGkiGc67Txm-2Ob1nszu2orVL9ODJ88Y7OEbaCSrOtiaLP-fcgQ82AkYpzepTQly2hWRJQcd7YO1V5xynv1jG70jFJk2ae9Omc0beP10QbzZJvRVEesqGORt1fjDVtxI1B7wVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3OdnPsakEFYS1xZXBdMCEhb3TzMEuwi84YI_E_Pgu7m0TkNuHq3XCe0jC_C4JRXWPksqDZ8NRCmRhOl69hGgj5sW0ba3eB6SJkAjOV7T_mdjoh2PtTT0XUjIiS4vlEAwd1NaLAjtChsKUwoECdmv_ADezAgzaVMgrCOT93rQZ3yi6ionYzZz9JhhRG3ImhpngS82HSKYXPnxEojnsWPJf_PawgNV2-n9MI9t9gzzaksuc0Uvk4Zew_08-f3luiEmvJPssndNNRuYuch5ckHU0CTOpCRKD8VGJdVgvHV_C9Fuo84L4gApDsKULoVLvUZ36vRWxsbsSsITlZKqXWQEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=r84DyzvmNnm9a576twT2MaI8gBJftQKHvxUe9UahZKiVrWH7yK-Eb9ggHVZE7vOQmQILpw_zwu642qMDYnIkY42E7lAzJMEe9lHN3nhmSnMsbXwJNBPI5r8q2CZPAjM4csfYOuPNzlfofO2zHAtezsbK-3nXRR3v1c8XHtI4blyb9oD258_1duWennLygfI6IPftYIFsAr3Hr4gBWkkkyHKNh8kN-Ax1b2Md85uBGm7e2XxNCN6wR7Jnw4Ej1zZmRnM6Rd5VxYWa5Cwcx2sSKtL7kqwGFvr9uszYgWqf16r1KLSh4jtw9KuJbm4NU-TRN0R834TYNpDKe5uKE9oAeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=r84DyzvmNnm9a576twT2MaI8gBJftQKHvxUe9UahZKiVrWH7yK-Eb9ggHVZE7vOQmQILpw_zwu642qMDYnIkY42E7lAzJMEe9lHN3nhmSnMsbXwJNBPI5r8q2CZPAjM4csfYOuPNzlfofO2zHAtezsbK-3nXRR3v1c8XHtI4blyb9oD258_1duWennLygfI6IPftYIFsAr3Hr4gBWkkkyHKNh8kN-Ax1b2Md85uBGm7e2XxNCN6wR7Jnw4Ej1zZmRnM6Rd5VxYWa5Cwcx2sSKtL7kqwGFvr9uszYgWqf16r1KLSh4jtw9KuJbm4NU-TRN0R834TYNpDKe5uKE9oAeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz1VkNRSa7x3tpNPOFgR1kS7Ak5A92xBz0ZmRuwQXuFSDlvJsLvqx8qf_yb3tCfgzD_Hl9GoO9g-cnoBzTSdHTw3SOIRkWY_poE467lEiyhOTRckn4VAnU8sAyAyDHAg3XrW06GEyC1OTy45qyaJUa51cWuE1fI2kWoBlhyy_ZUBZzFdSymHV_pND5yIu9bzt23OlVWnwmzD92snT3z2jrxeuM3PTEz_aB24Dv8ke3xIGGVCjY1NalZZSnVQlQ14RobDzpjNHuUkc3CGs2fIRrcRYtWrLYojmdRDp490LkDxm0zWihLX-wc3BeLjo5YCaPMTULOiCRwz3FBaCT28cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOHMF10K4WDoLxoBUEJHMckd7TH6GX9PXf3N22nnZXOUf12BIwMzpla3GBmJN8pWd2mutB9e5Qun1GsXCm_Y6jRLP5EOD2tBWFa9EnfaDdsAutOsTLNOHMaZIzR4DNJRfpsxfoPuF4ic4YAirjl3J3u9WAl49Ke_zENxYDjXcJRhbJ4eWyftdmj6BEplrL7Qo1zTTQjG7kEEEVd4slCDM4uC-ptt3Iscso09dSJLF_aPVAHJFOpL3OSuoqKH8qtv6BFugUaBuXN7A5a9kWw2URD-fUaj0GReP2C6HAEEo8C6FTZL8-f1L00N6Kx23d08Nf0jd2YP7xNUcgKnLoMgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9RV32qaTw0exm9-DK194NbTlE-4E9YEDTZBelmKhAtJ_j5kG90do-ougJdaa0GsfzcC-K65VVfBQ6uKfsVCEHlflMykONaJpyyjow85ZhkwhgNz6YTKFfLyU3Cpl2A1Zt4TNM5jH-c9TG9ZlOAnIO-7O1KL1w38Ll36o2db7YhBBk6dcjXQ0tstSpjIpQ-ePQToQ_dN4yBeGaWTaGIAMC-ZmweDk0Xe5yZcpTshtlokHywcnmkUfI_d10godRXovQRB9cSggFfSQmAMAMp9cQs0FXyc2RA3-vw0al1owD-guBFKfZQq1-uvb2uVGpNBMZTLCJ7pr99NGetd-Hr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OnaQD486OnHpeM6ME67lrGchiBntn4xr3QP02UhTz9_MjCEKaYVoXPWc2a279KgxLXZI3EXwDv70ix7Y7fDmLZ6PeTJ5mv-AzSGsTrk7bLT8mOeANGRt7RpEJRT2g7XtmjoSx4eb2M0FCPXjJVqw-CgQMwzZfm2tp2ftN5KMc05xzSMFxeau4I40msYKxveNcQgI7DaagBL5syIfpU1v01D3Av-68RWcOOsXu72R4bBZ_mSDjYK8CQl_BNrSHZ5oHDyl0bH8GwPu6dWZckDafiWKv1a5XAAojtUEysoesKxbT_DGgVut1fkO4XPc9LZz_CZjD0502m-q5opfTe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZwzkcG2NF92qI08UivrDGCx-Fh3LmDmcqZy4m3i5G8uIkE368TU2o5E0w3rfEWO7DJilUjGjPzPg9crtUX12WTNT_fjJrn3fbOvO9AOM2x6iSc_-cHMTXhH9ojc1w2RxI_cylip9yF1TPmyB0vDQSSb9esf0ERkHtnZOgWQd-3-0r5cFS_dCbBZ5wtHN_PWl4LAHGUyHVcS4eOWYHJQnPzJAHWZwC5ZuB57Mv3hjYsENuUR_DRI8seA8KtoCwObF2wRxDr_B3asSVqHdK24KdNxLpi3x12hzAXrtljSPJZLP1mOlYPZARMW23lPSvMY0KmDclRJIEh-rlw_ATPMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG5RMPS_pTLU1v55QAEFcOksdt2MfA7CYcCGEFpWS8Ac25UcYO0gKrxRZdSC2igAug2ZmexHtUlStFEntaJB4Y-Iz9oTJZKqDXmUDrQhC3upjVLXQZJIStqDmxO2pX5o-GZRX3Yt9aauVon8reczj-JZS5l-wYydKjBYrQOf8b3hV9097fs0EXp1A_n6P_ef68qWSUpO5f4vW4xfP3jWNUW9I6RIib9LFki_icXCDjecrqDUs-TvVnI0gvnVBGp0lUK2Vu0wnVPqKIy7Jl1QLB4Kl3xdbMoiQXAqYOAsJNOONxszM-ETxuNcxnbJiBi-j4uyEOZFxmE9VS93VG-x5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAT5Yo62vOWr3odIdejd4zKBzhTgEZ7K1oMlwMqls1VUENGPYGZSClaIkx156X5UFWNUh8sPY70XU8ootnu_9hDyFYTewwZgnzwC5sG64ijS6_j1bwpCveEdlZv1NYVJgcVqKLYTmhm_d_exTz9lCUH8Fs4bXGJitqNGqAb5HW_kmyt271r7Ub9qT-w9xs0U7PGWxIgLWr5eM-juAHq7STGuV4iK_ZsBdyk7JiJMzh-Kc9UQVrXrW7iJ00aVycRYBFBDLg0dljil83-G3Mex_TjU1XD2d80aStWT5pj3i770Y3MTJfIHov5eEi0b3BhjhPJNv1mo4dcpc5GLr4IUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXU9bJiGUjXq9RHMEvJrIRRxMTI_GldMtpJepEK5nhwVyLtLRS-LQ3oYubtQ6IRIXb5oc6_jeYVl-DbZ_qmlp4Dih-wx5Bh_A-40INr8GxUs17EdQw5yX7AfOlqGcCs_D-SSr3oHKATMxaNLPkdzRq3_dDQkEG-ZafgAA_AWUcPK134rvfg6hn57w8d7fk9N8bKgUAW8VfgmMDMxBSK39KbOF9lVU3sSGQ4rxGPSPrZQXE6IirVkJRQU1dYMpT_9V-CPGadfvnZH1-lAYiCh4ojDG5ZLQV4FzcHwLlTuyKbLmjL5Izm_dFVf6P8T-vE4psJGPHE7ol3zM_v1g-NNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=s9zjupjhLchf5APgiI7tw3uPCH6rv_P3XAo4yo6pYKZAPD2Z5MCCpbrUxqbThiTumA-JL1Q3WxaUHF5dD1aWVJJFYo_ZERYoFpnPkQIio4XC-y8X74bc_h-HzwRfTsLsOf3on2kyiz0iX3eZS7FwvXJgjPSKrMt21L3cqvjAODfV84amjbedAq1LPv_Qa-XC8_PuRfAxdQ3juK50_s_wtzesgcg5l9o3SuWbhGxRssKD_1pnohIqax_odItLEx-BL6u_eRb4LoPaV8x-kwtJh1hW5r9Dd71iYNegXFMSt7q7ofvupd-RV4uvKjEbQ0s1HSN7HcNRh2yIwMsdHVsw2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=s9zjupjhLchf5APgiI7tw3uPCH6rv_P3XAo4yo6pYKZAPD2Z5MCCpbrUxqbThiTumA-JL1Q3WxaUHF5dD1aWVJJFYo_ZERYoFpnPkQIio4XC-y8X74bc_h-HzwRfTsLsOf3on2kyiz0iX3eZS7FwvXJgjPSKrMt21L3cqvjAODfV84amjbedAq1LPv_Qa-XC8_PuRfAxdQ3juK50_s_wtzesgcg5l9o3SuWbhGxRssKD_1pnohIqax_odItLEx-BL6u_eRb4LoPaV8x-kwtJh1hW5r9Dd71iYNegXFMSt7q7ofvupd-RV4uvKjEbQ0s1HSN7HcNRh2yIwMsdHVsw2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsbKcqzppoSYpBcxE0lqlAyjCgtPiQD7GYQ90-2K9cuWe_IAUBnZr6JjAhm-qZ_pyLmyN-cLENtIWBusDaKSeEyHXmorKXfKhUTft6r5strT4DP5RBXwGWNxtpL_KjcG_ivottTeslFmxgWliTYUkUzyU48nxDu33aP5KVR6Qn1UWa3rQv23ASY8vymrQ5me6ojEwvEdwOuIvllRLXtux_PQCQFdr1uir0bMpK6bCNV3IA5DVoBtVp8O6LIF1Fc8Qsc0lrHQ1_Z4CXWhiWpSeDzgfOZUYe0WvAxykR_uUizSKamvTh_7uBmAI28450wp4a1imss3pQJUW4NPS63rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=oEzM_PsqXhhnCG4daNnvUEUuMwPG2fuBp-jxGwZ1qsNxPHCSy_IR9SQ3LJ4sBX2WGG8p1gINl_sBGVQlpGGBNeTXF5hlgYDs_toDhxTfA-2m4HxAEdgA8JfaTQF1NE4QZ40bBx_H0_Rxu7cTceSUd1S_Pafz9gO9pvVeUh4A5sAssJqIRq0PMB5vCbQgBEshwRbvd9aqiXosC0AdcH1-AMkfXeg-Q9BHFPLsBO0oxCg5OlXpZsLFUY-UAC_Lg6SfzB8Jlh1rAVh2GEWXO34kzhTR7Hvrsj0Nx8ZmJ9ftXBGuAau0aV7s-WF5eA7BuxrM3NoZ7kRyDnzdDPse74xnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=oEzM_PsqXhhnCG4daNnvUEUuMwPG2fuBp-jxGwZ1qsNxPHCSy_IR9SQ3LJ4sBX2WGG8p1gINl_sBGVQlpGGBNeTXF5hlgYDs_toDhxTfA-2m4HxAEdgA8JfaTQF1NE4QZ40bBx_H0_Rxu7cTceSUd1S_Pafz9gO9pvVeUh4A5sAssJqIRq0PMB5vCbQgBEshwRbvd9aqiXosC0AdcH1-AMkfXeg-Q9BHFPLsBO0oxCg5OlXpZsLFUY-UAC_Lg6SfzB8Jlh1rAVh2GEWXO34kzhTR7Hvrsj0Nx8ZmJ9ftXBGuAau0aV7s-WF5eA7BuxrM3NoZ7kRyDnzdDPse74xnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=JcGSGVDwalaU_o2LggqBzLveXE1nyQKg5-SGTpasuSlkLLHSvF9ENqxZlzNUz5C-Q4HFOZM1msDynjGcVtIgbNeC8FnExtXR_H49K7m-RwNeBrGvqVgZfzyXK2CIWyUPN7at5I9kjb8pq7IfGSKYhQhVxBO9VvRXQZl7fotTYf4vJII5-L3Ptw5gtuVO_maturxG-Nd0MLk_19KeIytviofkBKkd0T3VVoXNK069tzNwoqob5nwRJwHa8sXxQSg851hP5IitCvO2I0FU7nXLVJDVvP92XoYxbCLv1HnZTTCPmszWyfxwJZRdPFsAgUgE5h9pS1ykNtVwYyJpyR-62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=JcGSGVDwalaU_o2LggqBzLveXE1nyQKg5-SGTpasuSlkLLHSvF9ENqxZlzNUz5C-Q4HFOZM1msDynjGcVtIgbNeC8FnExtXR_H49K7m-RwNeBrGvqVgZfzyXK2CIWyUPN7at5I9kjb8pq7IfGSKYhQhVxBO9VvRXQZl7fotTYf4vJII5-L3Ptw5gtuVO_maturxG-Nd0MLk_19KeIytviofkBKkd0T3VVoXNK069tzNwoqob5nwRJwHa8sXxQSg851hP5IitCvO2I0FU7nXLVJDVvP92XoYxbCLv1HnZTTCPmszWyfxwJZRdPFsAgUgE5h9pS1ykNtVwYyJpyR-62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=bb191vs7BF_neYZCo2R_bZoS7nfJnek53Ya57i6nZVKoFPXqvQW1C4eFAOBbvQy5kV7XIdiA6tvJQ8YeUA-AE0eDbYR9KO50zadI1SgAtoqzrbXhwI92wvMiQF3mvQyT7Rw1QLW4GxdrzMSKgqmirQRPcwqwdtB1R83y9o92kEo1GHh4bww0srzKrPX_j-Xeyt61V7m2OjCwS4nnIyQ6DgyN_q5NreNEhsWck6rhc2r8BlPg_x4Nrc7lOCYrrOnjQCItcih34CPHrbAVh0qUaeIOIrc7r3lKLy0nuQ9t522L8iaKQFeFd_FugC5FDEYMA4OZoOdF8YawXju2laXU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=bb191vs7BF_neYZCo2R_bZoS7nfJnek53Ya57i6nZVKoFPXqvQW1C4eFAOBbvQy5kV7XIdiA6tvJQ8YeUA-AE0eDbYR9KO50zadI1SgAtoqzrbXhwI92wvMiQF3mvQyT7Rw1QLW4GxdrzMSKgqmirQRPcwqwdtB1R83y9o92kEo1GHh4bww0srzKrPX_j-Xeyt61V7m2OjCwS4nnIyQ6DgyN_q5NreNEhsWck6rhc2r8BlPg_x4Nrc7lOCYrrOnjQCItcih34CPHrbAVh0qUaeIOIrc7r3lKLy0nuQ9t522L8iaKQFeFd_FugC5FDEYMA4OZoOdF8YawXju2laXU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trIUtKPt7wJpuFKFUfRagscI6kliQe_i4vcwq8HoMcfv8t_0XttoTdf-HtttKy7yI_7IoIDOdirc-clavpZOA8Dtw-Jc__hT6O2X2Lw3Pba8FCEHW_cqdAFKKRFuL8L5MR4ZHJBGDUN1StdGOUyU4wiWuWJxiVBIhmq9rZ9EN9eQtr3KSh8AafvEVzrSn3hI1PCuPxwnMLtbkBDpWsCTsjyvY2-n3OKk1wAVZaZbfmVSlw6w43cvyXZGosm6cOQ9MzCzBEx0BJLSeZuuI7Qy4j0nkqPuw0VHE6W3Rpj-F7AvIHv1smm0IizI8p7mz7_DmvOJE1wrccQtiaP7R0sHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2LFO5QCykbzAr-YMWOziBVC8HrZTuFrHma-sVP6OpAQ6UaK_NVQuZ0BZexWqntVWdiuLYg0fes940b5GlTtIuewJZ9sULWWuOPXFj5X-MKrKwGqt_oJE8oblcCeEzN_E4Ka8aseMd7Ofgh4Au3r9GMJYFw7vuUHq5ZWitDLiOfVSUaH8yTYGnOrHAFU4TUzCtDdb7Pe9lC4ApaXK1d8Stz81AXuAjL6H9v-wh04HG9ivjQWm-p3ZV1Ng_dtGiwLL9IIz-OWrLr1CUDJ3dvBOhjBU_jRPcSKB0oQIP16mlm7Dq_1CeJrBRUYNoTur5dU7q6toy9ZkEt9A9DPgZzmJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=eRv4fkaeFgm_jKEFIQc8GjV_GoAU3oCIPfQylFjdF8xzfETd-WSleJ5GZiHQK1nQB3Yyyhf_5MlxUbdpr9yvkwfGaDO3oUZZqTCugJcH9RH4uPEIChxepI1xV29ANKT7Ye_ea5UnY1m8k7jsoTdjI2h4d0czpYPfBjxbDRX89oLU49G0bjBu3A17S_9ByFaahtyZV1yCEC780U-l7hE13CCwUwXBAMf5ab-VydZW0sJbJaWe4L9SMz5KpAuRCiRCJ5T9YxX5WPhzKX45A0_fA3JVVHEdMsJj5s1Kt3k4SvwZBtyFxtqZBGTByZO191EJA2b76YBsvTZC-5iGRNPUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=eRv4fkaeFgm_jKEFIQc8GjV_GoAU3oCIPfQylFjdF8xzfETd-WSleJ5GZiHQK1nQB3Yyyhf_5MlxUbdpr9yvkwfGaDO3oUZZqTCugJcH9RH4uPEIChxepI1xV29ANKT7Ye_ea5UnY1m8k7jsoTdjI2h4d0czpYPfBjxbDRX89oLU49G0bjBu3A17S_9ByFaahtyZV1yCEC780U-l7hE13CCwUwXBAMf5ab-VydZW0sJbJaWe4L9SMz5KpAuRCiRCJ5T9YxX5WPhzKX45A0_fA3JVVHEdMsJj5s1Kt3k4SvwZBtyFxtqZBGTByZO191EJA2b76YBsvTZC-5iGRNPUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=QIv1-BLK2HNQr4d_TbswGrrX2ORs6l-neETiUzDwxMA1U-9m0H7t411TjpHs2qWRY9MiOUqLRoJPmA2lcAoD1qW0Rtck0jx4-15iht1iiHGXh2MuT1YtrmKXa63S8uspok-iwQln-OGUhskpcdcNNZPmV4V2Iwe-klaKsGuuUKVHnIeHEAvJQ8EEc3qVySSphLQU8dTJwx66wd5FQ-gE69V6ZisRx8BduNq6PxNUWSatcxluPtDRR0oQbybkFzt1QBrdARIXo75sfqGu2VBCcSL3QoNPPl9ojb8A6WKAIApSeLE1fg2QooCdzrIfoj6oy5mFozBdACUiTjgJQ4IjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=QIv1-BLK2HNQr4d_TbswGrrX2ORs6l-neETiUzDwxMA1U-9m0H7t411TjpHs2qWRY9MiOUqLRoJPmA2lcAoD1qW0Rtck0jx4-15iht1iiHGXh2MuT1YtrmKXa63S8uspok-iwQln-OGUhskpcdcNNZPmV4V2Iwe-klaKsGuuUKVHnIeHEAvJQ8EEc3qVySSphLQU8dTJwx66wd5FQ-gE69V6ZisRx8BduNq6PxNUWSatcxluPtDRR0oQbybkFzt1QBrdARIXo75sfqGu2VBCcSL3QoNPPl9ojb8A6WKAIApSeLE1fg2QooCdzrIfoj6oy5mFozBdACUiTjgJQ4IjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaJN-lnbP8RZtOMQdvj8buDr0zd06JQP7jg2lrp475bNaNAsmx6QaQRxRKc1ElKyKQklWnsLXT7yCQfLgM-DNA_SXXuKDystQF14jMXLcS_eyX_ukhpeyauvqj8mul5eMPWdRcojzY_tMZ3haMdqW87ZhFAREt7mjT_nuPgNfd-Z7M4HARgzDWHWiL05z4Qt-SXw6cIwxBwTJc7c16tfI6SDyH_RULB4T1ucdf1vxNMnjp-fkOFtljjB9V5pF8XehX2MawTEItXIy2qQwhVSCqLkGvjY-JE6OhynichSqvoFIOFmoWBfKOzibmqEMLx9LjJegge3B_RYWHPELRrdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=kQmMStfoAcpP_JhIRrZRPBRYv_08k-t9RMXKOyDz2cPWWJ680A1Ux7b5IrasHeKRAfLeSkFbOMqmFSsUvBEM_6O4Wua_hRl4jV1EkR3ngXVHC9_d1-ZxAsi8Q6QFrRxi5F7eASEQw4ugNjyBDnqufRRv3ru607CXq8MuEx3PvA_arvXjAFPLHmIgjIy2M9kqiZG64qrMYNYDnxqimRv9gBFzIwEgDlOyrewIQ78IATxwDuYbryL0ysFNaw2B-zV8HmB7bnLXYkRHEs_1I5KifNkuRTzFIVVO6KQWfr-QUlz6S1-P83A-qWtHgWZdgFhA-x9IVyr6DRz6Bf_ac9SVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=kQmMStfoAcpP_JhIRrZRPBRYv_08k-t9RMXKOyDz2cPWWJ680A1Ux7b5IrasHeKRAfLeSkFbOMqmFSsUvBEM_6O4Wua_hRl4jV1EkR3ngXVHC9_d1-ZxAsi8Q6QFrRxi5F7eASEQw4ugNjyBDnqufRRv3ru607CXq8MuEx3PvA_arvXjAFPLHmIgjIy2M9kqiZG64qrMYNYDnxqimRv9gBFzIwEgDlOyrewIQ78IATxwDuYbryL0ysFNaw2B-zV8HmB7bnLXYkRHEs_1I5KifNkuRTzFIVVO6KQWfr-QUlz6S1-P83A-qWtHgWZdgFhA-x9IVyr6DRz6Bf_ac9SVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBsVdxI_wLWooeApwvv8JLPn-Hp5GMj9anNH8reaCkuyirElwT2G1GRCaMszUr411S_lP-rmVvBNSRm7NLUL7BbPhHsUTiqIP7TkcqySDjUxE5kuOSWUB0OCQzrfHqBLv33xZYw_bInafGbAelcJlZWQUUmvy_V7Blokl_QEaLA40EZ926I68tdmFhWyGkh-pfCCqwzgdUK03j6pTO5FVJj6Sewt1T5r4TU3K_YvDas3KyzGzPmVsdaeknIVg3IpLBFXWEta5fGloc_a2cy3DSDVkYULJ2izsxukqHn5hI5Gelq2nilh87qSgcLsiSBJsUtuR4JwsS_e3BXttFuLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE3FHqeI5K5dCR2dkPoP7_XBBZvdJkvvbgUUiq7_yCFMYMXZelQF9VxrYlgO3QL2Mpn-XmJFgwGv1_zEr6TfpeoQk_mTGGL7RbtrT61sV-gvTmScjk6xfxDdtUYUQleH1mpmnNGjHe9e25xCyuU1eQ_lnZjUSrh3GXAIdkGc_oXabgDPyNi-ITB9mx5Vk-hJ0xXr25iMZ1zKl3Qa7uy79ZX06nDm9zi1emDAgXOvkqxQZvgzrBjKkUpqAeXRnTw9hiyax_URm_ngI6ZE-GVm0qsmjiSNDOlJGcYvrYjXBEr4_tiu7E4FH0SviTQr5m3PsyRBBAzoURc3tjNBqpGeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQwY-HRpnObqFy2_69IBkGZz2wcIAEXrQesjhYxNxsz7tRsTYLk1w2tYnTD57RTd8aFHgG0SUN3D6Kjcux33Au84GPpuRbggIjRwpf715X-9agPhAQXvMrPLbvqh0YTzn9s_oc2kBKMN64GJZVFUALWkcq3Dv7u8YlkI9KimRUwNnsRJybbbYORH2HMUr8ib6zD1ObjPcqBtgsDvc-z0iHOFeJFgDE-Fivrid8UiuY4qJ5lED0hiMnGKdcD00IRv_yGcI40FJMNGuiqlsiY2qEQnob1cvLkV7sYgwRfq7HhflS-3pd2vocmBR54kL2TepUpeFT0b7_ahHg5h-5E2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtK5kdJyNCkLVWbE1F1Hgtp89Bd7vPHko9-j197vE-n0nfUIyWm1w-fA2gAZdMC_-9V1PcUNxanzRqGIXQZ-gv8dB4bqrQlUJJPxTMyUVvhrVlvHO-GoIDdHw5H2MV6xFpPhCb4ftQcCND5c6yXJab12ZuuFJsRadqgxKkn2tu689-KfmYDFdohf0HCMgZXi8pZfFEJUUf7QmfXiNXl5hjmbtAORIBiEeXVDXCIJAoF250AxqMS5N58Z_xIM6KNtQV84SD_eWsO8HtB024qJ7D4GFJ6yUsCryxp0AG8RojnQOS0HKP9tgwRZxo6fe6T-JNTLrDibXX3U8Fw-IyNz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=XiJ3L1Qu0pWaQiZhBl0LKwHbLeStteWvkjmPm5oNlR_2gX-eDT7Kmp9ikAx4idG55sACxwnitjZsgRhWkUT1SuFjTHA5qhufX4PW06LrFaEeUPsipudog13LSzaWrkeNWNPSEiJZN2or8YxPuldtDVHtaDu7tCBy2eDEL31TrerJu1JtMCM9ckgzJ_gERNRI7c1jatq_sG9wLIqVoB8V-IgYEbFn76BS21Wmafnc-767M-GiaaCFbspjWxgiiyIjLoFUQvAOJX77cJM5RWbnjJfweEPPTzcTQdWa-TtF-ZwMscnE8_doIoonKjU67Xp_uZlmCJcWqR3SQMAEn679RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=XiJ3L1Qu0pWaQiZhBl0LKwHbLeStteWvkjmPm5oNlR_2gX-eDT7Kmp9ikAx4idG55sACxwnitjZsgRhWkUT1SuFjTHA5qhufX4PW06LrFaEeUPsipudog13LSzaWrkeNWNPSEiJZN2or8YxPuldtDVHtaDu7tCBy2eDEL31TrerJu1JtMCM9ckgzJ_gERNRI7c1jatq_sG9wLIqVoB8V-IgYEbFn76BS21Wmafnc-767M-GiaaCFbspjWxgiiyIjLoFUQvAOJX77cJM5RWbnjJfweEPPTzcTQdWa-TtF-ZwMscnE8_doIoonKjU67Xp_uZlmCJcWqR3SQMAEn679RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=gGkdxicJ03JdgScGCsAWBCUseFMemjujgq0tbIjfcoeKr92pTfpyFOASQoW3uroJVOLqQ_vJrhDrn_l5pJ-xSMXU3dXPiBRIC_4U7IcUv2jhZpxGhDtIRXt8bfnkFDWsjDNARfbkb1wadh-hZv54hdXC6qKQdkzp9O_6ywDzrgViTDBmygeljMGLKCtqYXueBvczlBfMtGwiGGalrlLyHP7Zg76cKJqN-h6aqFI6KpQajjQNr3RBapUZU0NnWgE8xNlcUuYLIPDcrnZ1ZudBSHDmszRdhbijguLz4T5kGRVelFiMiHrC4UieDhbMQQTig2g-QMwEsM3PzjlRYgBhKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=gGkdxicJ03JdgScGCsAWBCUseFMemjujgq0tbIjfcoeKr92pTfpyFOASQoW3uroJVOLqQ_vJrhDrn_l5pJ-xSMXU3dXPiBRIC_4U7IcUv2jhZpxGhDtIRXt8bfnkFDWsjDNARfbkb1wadh-hZv54hdXC6qKQdkzp9O_6ywDzrgViTDBmygeljMGLKCtqYXueBvczlBfMtGwiGGalrlLyHP7Zg76cKJqN-h6aqFI6KpQajjQNr3RBapUZU0NnWgE8xNlcUuYLIPDcrnZ1ZudBSHDmszRdhbijguLz4T5kGRVelFiMiHrC4UieDhbMQQTig2g-QMwEsM3PzjlRYgBhKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_acSz8mo_2ZQLDxxugFNocKhSljLbHpxQnsYBmI_w8n2eeCAHJBG7cLTJmudDZwzvuL9WxaP4CDVy---GD1AfABBPm0tF5b4ZnCc7GFcTNyUhJoLXsM3JHKUOpn3AmuafyPV_Imr9JXd8PSm_S5OYo3ccYjo36To3ySBrBLIaIrn_cQS6OvRMaPr2EVAZi-vWurEztqiP5IZWjtzhvA1D9n1x4ZSP1QalX5qmBsG2N3zG3H9ao19Ymp0Z4fgLztSTXmeM0Nc5QOJ6DdUcRVY-4z8HORZzcGCL_f83vWs3JnfrAoFvU_jm7o5TqbTnFP3x1nEDml2nqfppMzyf81pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBRWHnIO8E3Swc4mosvyT6iddc5U0n7KuFGKHYBn6u83kEPy5qX-8cSDu8QEwhJD6FvjuWAcC2V3Wnor5I9f9dlPx6212eOzRQLQaefVFE8gCCcF5bXtwdmFv9nFlxDZbhAJHdXBQTF7MQYoqON03Z4-iY8BNxDUCwlW2hr1CtD_Am0u8O4Gexla3SPkg5ELtwx_eyys5K_G0MOFX1jtMfKhDDfhc3iX2FrWdjg4LP7ubkEKd737zXdNrYBGqBm4VoTVbF7O2LlK4kgYiMFtOP6g6knFIwj4ag3JoxUl9R9AXB1uu_SagNEajuboBlbej-SwVT_jBycwVUT6zj_ovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTqFHIqId1J-sZLbvvKS31dbn46pC2HxOYhzqG3R_mhGtLStTVytVj0yJESZjcFl4F9ASxsrruB6dMNZx1C0aaGhh8cni5WT4Diryng1jFcASbhLC4nV17j24TbkVrkY0JQJsBnkaXtga-zg0S2BE3MTIu5KbkHZ6p4uiHIt-2ziPIdbOylYgEzlxM_ottDgIPOIX4sqYxGoScT32aBr67tOdWG1DH89usmaZUG8KgXzEdJzF-LSwNERGt9zzydxTp7oSSBMEX6NzJTw5xH9PzeSayVTpim9M0RyCwAKfJxi9zdyAwoxpY9moTv33y4qDUn21bUptMg5udN2YQA8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te0K6sgrhqPCziG-T7j4M7M-yzlV_2JHQ3BTAbwk0XgRDb52f49eJly0WZixJWvptRzbTp_w-a-hwvHjPSJirIiS-hZ3QSdNY59StxrHcVvZ3hfHHwEtTE1Fn665Cj0XQiA8wp5r3_9Ukh7jhxMWEGSk4lxgyjrviYfBoetAr5TTVn8LMJ4oMvEfqr7FFxDbtjmfyiQbLYOJpbVFZNOaZtABfB2Umk8fI11SGzuTbn86aw417ijVQ1APdc0ul9BXrrkTNR3U4_BByaMgTMxYMaMhOXh7KBVfeTjBLjlPG-O5HKLS3MhjMYwodlgO41MSzQqp5q6KLXdtGnc__adB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jODJyUtGUPLqUVwwLSCInhqIyLztIktd4gshZk2LBDEbPKcaph7TFgbPu0RV0FWq1FdRDB82vaFwo-6ZYOxMGG_mCMp5N33Ypg6JQpIDY6C9Rh0cx6hQneqXNWA0H4aS26gelFhNYqcayUCRYsQOZq6DalSqPlrTc7li-09Ra1l-qwkHRpbbDvTOaPzjIWpfSJk09Tpup-hDVU-WumEPseqDOAKLBu8N6IEXcwsZ1gZu79ngD0YokqWykLsWalvq44E7TBX6fACwxi2nT8I1EecG-4cSgeaQarEaEm-ezQSIlUmhTrwPSNumfW2wE6C_tSyQHJahQ3IlhoHdDP3iNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRASTPlF8-v3Ag_asrqKVi9atzYQPGJgMCkpoZZDtLKo_wrCVco0CuUhudkohAU6e5abNolGbhVh_lPvsmNnT9dAtPSOO-DY5AX_9ZEHoN2XyA48EnGSvCgCVWpfsIlE1GMm8uLbHWCT_1J8gImRGTO8N7I0_stsEJmwOR_9i_NNnl_nHxv-6S3gjQn8jBFzn6LGJjW8-NPWTuYO1q42JFz4bzm4WJjZLOPa4Rb0TI5ArB3gWKVivP3aM8Gc9ipttXxX0k8qo3X5E6bQsdPNv_Zlm5wd2emSdKB9gVpnUw1rANU1lCCaLgQh7DJHPscH19wkVZUjdQWb4FxeN4xDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9LA2OoNIYzyXLhuGvu6h5Gv_D3sjU0_7OLdRbzpozjOKlM1MVaYDke5AxeexT7xHzUrrbS2hfvUcFoYSrCA8U28Fcnts_jcoZgNJj7Ci02nGvLboosve5GEJ5G38tSCaxNrX2ZQDN21X8p9xQsRNVZWrN8az6sOoOcNdKBFE1gzNAdUi65dTMc3ci9NuM-BoF3jV0sT6TT4TEpDkK63ehX31lVbUbRETu6_OvY3NiJ4KlIsVNg-9lu4KnwE0-xT8hGcq9wYW2DAd0baEdULcO8YALc3B_lIgRO71jvPFNfvl49Tp_BFT101RZDw9eMKDwReL-jSp_FtnG99OY6XRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIuQJ5i9bFDeIxiKr0ZFiM6odh80nKYByTcS1876NEI7jW67vf4vTJ_8R62brn0QHcL4GV3QbS4zDJreQQCnzFwtuGNMinPb6uKgp14ZU4G76ktmOqSI2irFZrqOki2dZk2ejwbMveqOVqHHUEz9fADQjk2QnyCoiM0Y57heSf-Gce9PNqnzhAy4rYQmE5QboI1tabrF1hs6RsXuoDq6V4mhv1XFD75Kj1xwTZNAhTodXoj3X7aUKjwQKGo-3Sge4VxwxYKCUX5ETIj1f6StPCR2AGiPeiv5SK7lVUZTccaZLJg1LjYRSN5AAMslCtDCnfFv_-4YcgXkZMZ0YZU58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQwvlfj9Zz1qv5x6_DO0vKmEgbx04-9wWBc0c9rCntG96fYeW_Gys9GtrpnY9PWWcCfkxNJ8qXXXhs1khO3ksg5j6pIYhG_HsrrERyQbrjJtJchh00e5-2ataGLTK2SA-duG1zpjDrhLR_0WKL0U9BsV_cRjnuM1Wr40cD82dwiTWQGOOVzZEvZAyyCDJQyjNDgffv5LDEnhgzNCa6C2IbUumUmGQ1fySrxwPCzxKosEVTKULawN8HN4YV_w_ViocmPrlG2qU3nfL6c96TAffRk4tKMI15llDpOHEm1QyvGCV7Ww3AVth8GZwtjtCivj011tX6t3DdAJMkCUeZ6EDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Jr9_YaBbng0_5WsIoueCUEVsFu4AL6TFBzlVd1Oc0yH71M783ot6LptNGCrCW6V_pYCilST7bx2H2TMbwstNXndRWjFOc4P7e8-K0nI7OLAYz1cS4pxNuxbaePxT02w5Zwr-6aKhaip1YZDmISsFYxDTK8FD4nNBWpyAclm6lBKrVY97fMO-Cn1FYFZRvSeB7Gu6MJJpHLrgd3omVxu6yFbQJJX3z-5KnjJNWIimft8FXoTN-fce8BFyIRhXMc41p_PRUzwGXXvm0wl50XD8RBESD7Nl_1ysV1ThLKQG8QXTTIQVk7gIl060LPr1rZwE966hpcz8PNMW0HpZ2YhmFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Jr9_YaBbng0_5WsIoueCUEVsFu4AL6TFBzlVd1Oc0yH71M783ot6LptNGCrCW6V_pYCilST7bx2H2TMbwstNXndRWjFOc4P7e8-K0nI7OLAYz1cS4pxNuxbaePxT02w5Zwr-6aKhaip1YZDmISsFYxDTK8FD4nNBWpyAclm6lBKrVY97fMO-Cn1FYFZRvSeB7Gu6MJJpHLrgd3omVxu6yFbQJJX3z-5KnjJNWIimft8FXoTN-fce8BFyIRhXMc41p_PRUzwGXXvm0wl50XD8RBESD7Nl_1ysV1ThLKQG8QXTTIQVk7gIl060LPr1rZwE966hpcz8PNMW0HpZ2YhmFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=Bj_vKS-mJ7UQvag6as3M4foGV2mzkrnvX3jMHST285uA-KI7zb-H5LrTUYL_G7sxS_HiAkJTtyLH8PoXTNOWh8XHWmHn62qDKVEDn8xPrxnMdQHrFrT9xhSHyI0nzNOMFHGYNOC-HEKPqAninuoiZBNIYByheyxhUcJb24_fMVa8q9doLQOjTmTs30DyXDDxvMBX6cBwZheSnIDpR9fsYEHtyUeids3pLXbEozTbcAV58xR2eBXvldf4tgwmX9SCeE3O184HE1faCETzSTzUeXCSwtcplN8MUljXEMJMajwWyRr_oSLq0yeW0r3hnI83obnwQPxk3k4W7xDv1FDRKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=Bj_vKS-mJ7UQvag6as3M4foGV2mzkrnvX3jMHST285uA-KI7zb-H5LrTUYL_G7sxS_HiAkJTtyLH8PoXTNOWh8XHWmHn62qDKVEDn8xPrxnMdQHrFrT9xhSHyI0nzNOMFHGYNOC-HEKPqAninuoiZBNIYByheyxhUcJb24_fMVa8q9doLQOjTmTs30DyXDDxvMBX6cBwZheSnIDpR9fsYEHtyUeids3pLXbEozTbcAV58xR2eBXvldf4tgwmX9SCeE3O184HE1faCETzSTzUeXCSwtcplN8MUljXEMJMajwWyRr_oSLq0yeW0r3hnI83obnwQPxk3k4W7xDv1FDRKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mWpCVpRKQUab5kecEpOD6Wcu_mEbA4KwR840t0qvafYN60Wq9HRY98pCA56F3707k-X_CNd7Mz5Xg7LZnfOlp-lY1D64TDb8RhEgs33-Ncn28wDeuMKdVemZE_AxClElasJatJ-Xl0GbJXT6L6keJwiupVKpwoR_DIzPN61rcdta8JDwPCqPmGc5n0WNuCZDOhLC-ADBVOVYwMXsJ4ArMAuJ-EDK55zVCxa3uraJ8DctKIT1pVQtSqpC06oYtftoBGgAGcHmFu9Lk77GPUQIT0mdxvMTxn7mnUvBok6NOKHx4BjkYy8MbK_GeqDtz-EwoUcIrCC774qSjcw5O2v24TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mWpCVpRKQUab5kecEpOD6Wcu_mEbA4KwR840t0qvafYN60Wq9HRY98pCA56F3707k-X_CNd7Mz5Xg7LZnfOlp-lY1D64TDb8RhEgs33-Ncn28wDeuMKdVemZE_AxClElasJatJ-Xl0GbJXT6L6keJwiupVKpwoR_DIzPN61rcdta8JDwPCqPmGc5n0WNuCZDOhLC-ADBVOVYwMXsJ4ArMAuJ-EDK55zVCxa3uraJ8DctKIT1pVQtSqpC06oYtftoBGgAGcHmFu9Lk77GPUQIT0mdxvMTxn7mnUvBok6NOKHx4BjkYy8MbK_GeqDtz-EwoUcIrCC774qSjcw5O2v24TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyIt4WRUb_J_viP0fSUyCvMJTPH2rijCJHcdJa7noAaPwSdDg9h5k72jZe8bjdstHT-gz2DVYJJL8-S80aAUeakIvKLm9BpAm2-eIAGHwSH33SV_skHta23ZLV7Y0p5vbUeZNaVrCm1roZQB4A5JLzwsAeHn9MSkdbfs7hs0vPZWam2MpCRK3mh_TxwFfchntF3HeXX-TWCdB3ZLwuIixC5rl7t6wYP_MjoRaoLNrnPgCHr8UNLMAwTrpsTeEzy5NNq3CwVBLKT5CLvv9M247iw8SWgZRnI9-QtMiWeVxKqe6x0DxgU0mxUq1QHboJr-Q4Fxa3YVdr-39FGmfaD82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGNo1ivT4xmGeyTgnADBz3wdQXN0riAiu9H5FWzV8czWPjSpbgpefAX9xz2Xy6IBXtb-hhtFTiK843sF_qpAylrwF6VS2h_VBKYb7kbOF4VT-Hh6My_ONM13H_hydWCPM-JyFbhAmKSfO0TA5JRiqh0u2V7JIE-B3xdNti9Qa_Y3irvnGL_q83a8-_o9j4Ycab9BpdoC0jlTxcZgvy72oaXkjCaBL4eYhWV9ygv0gBuA7JzrlbcPs8N0jO6LTsMOlwNE8wy4fzvYenyit9nQJd2dtCZYnSnu5k4L3r-Qnov83i7mHc_aUInvIWsUjW1IC5FQhwKEPnCXo2Ay32gBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIMLH-ycYnUKkNbYWVn0K7IYV3Nbmy6yI7CA6xkMjSDdc22gUKHOIhGi8SjiV3Yq2SzJKofkMFMdiuvb5dxy-vU1dPJ1ZNIJd8aYUVBPZ3lrszKjvpiLn-sFWhfB-gy-gBQq5Iz2x02Vr6nl25ZA7SifGNxsAtpaRlMmrFM8Z4wQY5fFyNxi1D_qyr3saSOYO93f6yV3nR5QYbgvihuo2Ku6ISghUuRW4VyBVr8l2D0XgX4Vg6TpC_34igA1jWmHPeI0VGz1cm_iEzrtosbNYoe3YVatZtJz2zeqMoBm18GsLbaFSQPxYsPxOaRVuwP6cGK_N5GgAElhP0vO_Eqx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIVEB-ZdTpliEQv-fgJOFB2GM1Y4v1f6UTTjXtrDVrJ8I7RulM_hWPu_3Ed5bCUpP_N9RTiAXHOwiz9SN1ICCn38IRfRhB8VGO3kqqYCNonydhl4SNg4hSK7NUyGJYdJ-3zqF57C5MkhsDrC43hUjyjvtF75oYpnpPpH3JuV3YV4Skt21PYff_8Fs2JmLbnwYZJMdJM_ut7U8xcBpQ4JZB0aYX9xKRr1ssmryHRzN5vCLbERt_WCuxMqNugeBzmiY0SeSGOJ2QqXvd3gQaZ-pOyfvo4vNiFjUxda_uRjVW1bEgm85HMUnOQpSZpaD1T2bbiczvSzbsiRqI39bv_N5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqoOfq5aNmJBIL19OY5J3Eie9VXPilh7tncM-c63-dif8dN4ZqDwETl1IIHNMW1c7F0pZpUKaaPzC_dYlGczlTmL5tGswP-mefHXoIVr5HmjY9-9m9IPmdxpZLqovPJHqoVdM3SLxhJZBbQN6BRkjzD2acNMcr30t7qh5ONCbQ39-0HY6SDjAR51j7aqEVU0WYwyqPNx9h2c5OlantGatH-AfZ5sz74tgA1RxYz-kwfUf0eRwhgKX0RXhihluXRicYxl9p94A8a-dhGllfxO7uyT46cLjPpgDmif_ElCxaTsgMHhVEqc854WlLlziiEiyEYc-euZiFoAeWwa4yJHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1Y80kq6dVPQP4DwtB_UtTgrpIkpsaRErN-0i6lzKAcBxivefTDU_aRXTbtpcjbtPa92bU29xLHvBf6cNGw9lC-vJn-vMaji-WtcmDh--e3FB0slOuDzlzKxDugc1kxUjCJpLg_yGuHWBuU_aMdxOi5GLpj9bZYEpNdld9gVeV35oCv2WCd438Y5doZXTtyKlCdqcFRNQcQQdi8wq69mernz9g1g85ogj7Kr8xyJce5F96zaH9WD_8RLLrJRW0dIU73I-voHdHI0hv5LteReYtk83cjO1j2bJyeHevw-DRQM1L9rzZnofgNaYI8wUfVK4G_itQeyARe9GsR1JtJ87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSUxO5bu-dkMBvDHzBsVORNeIIgEnIuA-aBKBd5aitfqx-kO_5sucfpWDyUC8hMr09SKT-DsD18kQq4UP9_ymsmBpQ6jMLOlke8H-kpRnoeb35v8rSW_p5ajy0p4r0Ld0qf8ap_TbqECEyLmGEgOgLdiazLlY0d7QEi2AGkX4nyaj-FmDvIU-9FsKhVIMDqKWoF81f71XEOnSQBJ0Sx9TlTw70uTSRGU3h_s9-xL7SRcNp94KVfVjAZf8ea7Y2Zp6LNEENllRljPMGANsZhKBmsyaoPClcmDye02w2DmDvFcuLJRlDfT4w0GoEFTiGxUtpVxhW8dipbjE_gWaWWUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
