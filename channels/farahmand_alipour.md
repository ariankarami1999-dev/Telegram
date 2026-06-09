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
<img src="https://cdn4.telesco.pe/file/cxef7cr3duD96_ysbTmHErvB6V0qWvQ47WmhPYTUTHLD5Es5a5fiufwTvv9EKmE8tSaa2BewRuEKqBqFnN7L78DZSQXdQb4JCfWOBESNoBX6dBVGA619_6jMMnrI-9yMKpvk3xtLZWwrdDiL3JuKARjKaVuBevsFC5ITM50xLXbJJ1AUwgVl1CA91nQaLfOY9QgrkYL9hT4ni3NsGYMyc27BWnvF0SYMvOXRCPqxGLWjhKilWsIvgnfSpqr5QiDbWvfV6V3gGOBvcjE-Uc5bIFJ6IG0HL8CIDDbuZbJj5Q7jFFuknznA793zB3PSpI0OVNsSAX7vFLH920zzL9rSJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjY-Qd4xVC_6hO9aUVQ3mTNQ2MzuQQguklsB9FqsSq5N2pZJmF3ACO8NAl9nkcoou-CMZKSkxZJMuUJpzGFEOVZ8b92EnRrYRT1ujIdd1OH2LlNZOgkLkPMBgYIC98zzt02FwOheFVr7St9a251Dbs32uMK2XrkuM0idHIFvq4LD_re4Z2UcAzmCRZ0UMB3GgCGGjx9LMrbQyYt8xsE6c_ACzIrw5yN3iI76MMo16sQ-SsdzvBZ8-LNEolYz5mzS3v9EVZF2wMYXl7aUsHvwhfzZsbSxGoJ3010pa4LWIfeR98fSLMFaUJz5qPfqZYk9CNn4U_7u2m37Xf92XEXVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWIA7vaW6eOWKyCwQaEt8rRn96sq6SsiWPsCYPkOtR4ENa24Ihg4vp5MXmqwJfoO7vxq353t9MqdpGYcevkeN28RxDQmdVvFF5Cd22K8tQY3qWFFy2aRykGX4v_46S3bVCBU1NRgF1en6xSfRDq0KTg_AK6dnYcYKp_FotiGj1nMq6ku2roMh4rO-cDTjB_841_XbOS_ER9fLHrg7RWcW_Cfb3f2wJLjKYVWnC1SZ9ddvYRbgDb0dxVBON_J1dZyOIgRWfuBq2EiKLMWpSMueFPqJYWAZVBuYFQEyeZDuBgEJpF48ec-vXHa8VqmFDmOq67tQwDdi0wrvWuC199grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz1VkNRSa7x3tpNPOFgR1kS7Ak5A92xBz0ZmRuwQXuFSDlvJsLvqx8qf_yb3tCfgzD_Hl9GoO9g-cnoBzTSdHTw3SOIRkWY_poE467lEiyhOTRckn4VAnU8sAyAyDHAg3XrW06GEyC1OTy45qyaJUa51cWuE1fI2kWoBlhyy_ZUBZzFdSymHV_pND5yIu9bzt23OlVWnwmzD92snT3z2jrxeuM3PTEz_aB24Dv8ke3xIGGVCjY1NalZZSnVQlQ14RobDzpjNHuUkc3CGs2fIRrcRYtWrLYojmdRDp490LkDxm0zWihLX-wc3BeLjo5YCaPMTULOiCRwz3FBaCT28cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOHMF10K4WDoLxoBUEJHMckd7TH6GX9PXf3N22nnZXOUf12BIwMzpla3GBmJN8pWd2mutB9e5Qun1GsXCm_Y6jRLP5EOD2tBWFa9EnfaDdsAutOsTLNOHMaZIzR4DNJRfpsxfoPuF4ic4YAirjl3J3u9WAl49Ke_zENxYDjXcJRhbJ4eWyftdmj6BEplrL7Qo1zTTQjG7kEEEVd4slCDM4uC-ptt3Iscso09dSJLF_aPVAHJFOpL3OSuoqKH8qtv6BFugUaBuXN7A5a9kWw2URD-fUaj0GReP2C6HAEEo8C6FTZL8-f1L00N6Kx23d08Nf0jd2YP7xNUcgKnLoMgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9RV32qaTw0exm9-DK194NbTlE-4E9YEDTZBelmKhAtJ_j5kG90do-ougJdaa0GsfzcC-K65VVfBQ6uKfsVCEHlflMykONaJpyyjow85ZhkwhgNz6YTKFfLyU3Cpl2A1Zt4TNM5jH-c9TG9ZlOAnIO-7O1KL1w38Ll36o2db7YhBBk6dcjXQ0tstSpjIpQ-ePQToQ_dN4yBeGaWTaGIAMC-ZmweDk0Xe5yZcpTshtlokHywcnmkUfI_d10godRXovQRB9cSggFfSQmAMAMp9cQs0FXyc2RA3-vw0al1owD-guBFKfZQq1-uvb2uVGpNBMZTLCJ7pr99NGetd-Hr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OnaQD486OnHpeM6ME67lrGchiBntn4xr3QP02UhTz9_MjCEKaYVoXPWc2a279KgxLXZI3EXwDv70ix7Y7fDmLZ6PeTJ5mv-AzSGsTrk7bLT8mOeANGRt7RpEJRT2g7XtmjoSx4eb2M0FCPXjJVqw-CgQMwzZfm2tp2ftN5KMc05xzSMFxeau4I40msYKxveNcQgI7DaagBL5syIfpU1v01D3Av-68RWcOOsXu72R4bBZ_mSDjYK8CQl_BNrSHZ5oHDyl0bH8GwPu6dWZckDafiWKv1a5XAAojtUEysoesKxbT_DGgVut1fkO4XPc9LZz_CZjD0502m-q5opfTe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZwzkcG2NF92qI08UivrDGCx-Fh3LmDmcqZy4m3i5G8uIkE368TU2o5E0w3rfEWO7DJilUjGjPzPg9crtUX12WTNT_fjJrn3fbOvO9AOM2x6iSc_-cHMTXhH9ojc1w2RxI_cylip9yF1TPmyB0vDQSSb9esf0ERkHtnZOgWQd-3-0r5cFS_dCbBZ5wtHN_PWl4LAHGUyHVcS4eOWYHJQnPzJAHWZwC5ZuB57Mv3hjYsENuUR_DRI8seA8KtoCwObF2wRxDr_B3asSVqHdK24KdNxLpi3x12hzAXrtljSPJZLP1mOlYPZARMW23lPSvMY0KmDclRJIEh-rlw_ATPMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsvPQeKrHlNwcMtQjvJbNiFowRB5F6FB1l2K3UbkqLZ18wTQ33zL8Z8F3W-tR8yithkg8yLJTCFSkYCM6ucNYVabuyEAto8D4D58Fq4lACH03MA-kJPbaICo0R3SGAMyfitWgPNZErVjfBV1TFlrZBHeDyKVEVY_lTxsMZFyQ9yMiCV_n4E0cBUnuMu-K1t9ORmqI4z7lkFGClinP381tRnXlnx_6_W6yeGY-yWrWgvRqc8XgkJjUq1kJsGPTHctnrt_lkAjmNy5KlcB3DCT_OsRDmfsRdBkQKi1ZSw-7BLgGU3ey3BozcIfesboHCNXxrrBp_Ty6jir5xtRXoubRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co79J9dQTffI2q8aoVEy2Bc58afuCSBYCzcCml2gHtCJ3fqrQ6QQIzqfG1lyTLO2Rn6k4hcmfXzTq-WYmKlkhHEeg9uyfkJ5Bu30p-G-FGjVcC6vNNNiHiH6iN3UrhYscD-_NRAjkfCpp9AE1xQKC7UvgqOyVM9Rq505yx9HTbRX3hJxZRXkSwamoDA9a1rB5RWWMkJIAu5jrxKOhuL_enDrtg1MGCt4dhoJSvEDe7qzo8j14o2Cw-5fbVCwTvdTqJppARnfhsfBYVsiIOJIA3feSnePSSqYrLe5tHMoRZX8fpyFtgwpntudQ6oPLcodEo7BXrWOH_b6kqHGoFGo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0bf35Bjrhn8maTV4r1GxHmVRllBm8Bkr_0-1zboWpzyc9-gqAdO8-rU9EJaAiRzflBI1edzYh_04c_iL4gq-3koMDejaLbzUmZbiQh82wxSar7q5Tkgg3zss8xIjVab5FD_8uPHT5V9jTG0HNSViWSRpt5QsadZ9LluWA8HTPz-RDvxf1mgSG6d5HUCsGQFBAZBWIaDRkJnBgyIyrgV18TlfAjb-EOUKxE3sjIhSzHK-21FHzjp_6DIIXbm7KA9D_T2J38oE1heIWHxS_f4vb9UEAWmbft5lYgR56oYYb43_3IarlNvK4F3gUggS2s5ODnGKER5wmyHPu0acGBxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=mGGX5Sr1f5TJrX_-Pnk-bZ3xyQ_RjpuMaNyC5lHLCZFeRLqR95LsJyspwKWveIZN03O3H4ClvKfvavMxcpOm9Jk7QeXr8h497lASTyzR8Ocm_0-chQy0gT_oL9Z-Ljp4OQqGS_fJmhLs2ofOR_5scw-5tY1tzaK7vvhyEtFV4ZyYhZWL_XXmIqJa5LuNkvoVgrpH50KHnmgGewKcZ7zxs4EYv_UdDej1DjtmXE8TbkmEagc9xmffwFOGqFLOCAPerdMBHmE7_iafBigbeh0ddEK0niEXK_pWUJGd18vVc6rfNl0Vgdoe8501lPqeUUi5rRZcs0LtmddhKDXlR9BQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=mGGX5Sr1f5TJrX_-Pnk-bZ3xyQ_RjpuMaNyC5lHLCZFeRLqR95LsJyspwKWveIZN03O3H4ClvKfvavMxcpOm9Jk7QeXr8h497lASTyzR8Ocm_0-chQy0gT_oL9Z-Ljp4OQqGS_fJmhLs2ofOR_5scw-5tY1tzaK7vvhyEtFV4ZyYhZWL_XXmIqJa5LuNkvoVgrpH50KHnmgGewKcZ7zxs4EYv_UdDej1DjtmXE8TbkmEagc9xmffwFOGqFLOCAPerdMBHmE7_iafBigbeh0ddEK0niEXK_pWUJGd18vVc6rfNl0Vgdoe8501lPqeUUi5rRZcs0LtmddhKDXlR9BQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0ek_qZsXHMyYXU0j9YLAOcLZWZJMqK54LmVFHAqwexAOemcP_clNYXxWt2yvCmiQ3GSsZrabj0wCzSxz5YAepDKjFcyIAgNDSdXRwi4hTEDy5v1CfyaRot0TptteBYn5zw8iiHnqU-Fx0lhG5the9NCGkbq7_wYojp9Jm949GX-33bi8KqoTw0DapEtLpb0pD6h1QQzXOd3Muv6urj0y-P0Si_vbNrS1Mi8qk8TlyaVfLJqGttZLfR29ZZtFgcOBITRjcBgc5WYetGoXtAm6pauPc9Fz3HcRnhF6S8GmnI4uehBNEWBMZsCDCOu-Sso68kJUzMt767EStoqiIJfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=EwljOdxkaArhdl3-GkyvMnrkFBrCRNd6WyrzH6G6sodaMNr-uxlzA1usnIY0U8ZVh_uYANKGb0U688LHLVIt4VoKOHgSLiBhJRqbXWwmp63zlGTtZ2D8QyQbWqLZun8MqfKQNcwWy6Vz0s0d89osZqONKce9vUECRrnEd3d11YAr35nj2msjnQwe1lZM7xHpR47ZKIyECR9vlqQ6X0hkLQeyxxVocUNaAixB9jN6MX0uCVocKppWWlhWz1SkJkKxn1smmxYBrMj13TSp67E8osIiFA89uA_uxiDtmc54YsMiHZSWIA4hJUrE_eP-cwx5ebzVikunB3ZH2Gxc5syLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=EwljOdxkaArhdl3-GkyvMnrkFBrCRNd6WyrzH6G6sodaMNr-uxlzA1usnIY0U8ZVh_uYANKGb0U688LHLVIt4VoKOHgSLiBhJRqbXWwmp63zlGTtZ2D8QyQbWqLZun8MqfKQNcwWy6Vz0s0d89osZqONKce9vUECRrnEd3d11YAr35nj2msjnQwe1lZM7xHpR47ZKIyECR9vlqQ6X0hkLQeyxxVocUNaAixB9jN6MX0uCVocKppWWlhWz1SkJkKxn1smmxYBrMj13TSp67E8osIiFA89uA_uxiDtmc54YsMiHZSWIA4hJUrE_eP-cwx5ebzVikunB3ZH2Gxc5syLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=F8gjuAarKy_X9IuxgDFJrZJEH0wqCBwEIPXX0UWSwUBTMTqgTQVHnJPE0pERaGYpa5Po0kYWKUnGjk6H7h3GG40F1Oj1uUuiInszUFKcaOEUeLA8HdE1iEUKMJ6Jh2k1aaQs-MBBVLfpuwkZG0Nb_dJlTwLYFZvxzWjnkYPB4Mp2OD746EO3v1eRf5xJgkhWWsLgVCrk1_a7deO3tGKKkLHeBmK162EsZmx5C1XoN6usLAe5uVtGVfmECb7TwrwupKbM2lWXCKiRCKtTFuf7htDKAzG3cwikQBJGiw5KUHXOoKGEoUgxIat3akbAjlpBQk67OBIsvktRqjQRucmRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=F8gjuAarKy_X9IuxgDFJrZJEH0wqCBwEIPXX0UWSwUBTMTqgTQVHnJPE0pERaGYpa5Po0kYWKUnGjk6H7h3GG40F1Oj1uUuiInszUFKcaOEUeLA8HdE1iEUKMJ6Jh2k1aaQs-MBBVLfpuwkZG0Nb_dJlTwLYFZvxzWjnkYPB4Mp2OD746EO3v1eRf5xJgkhWWsLgVCrk1_a7deO3tGKKkLHeBmK162EsZmx5C1XoN6usLAe5uVtGVfmECb7TwrwupKbM2lWXCKiRCKtTFuf7htDKAzG3cwikQBJGiw5KUHXOoKGEoUgxIat3akbAjlpBQk67OBIsvktRqjQRucmRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=AZXBpjWrBFPrKOckoGAUOloXHYwVqOCrWVF0x6lsxpL2lGeK7JxCFMQTYLgktHa8XHzpzYV1oYynelf-tn9hipW3Snu4y5nsScNjQEBXmHqjIYRLj-9ypI7vE9w4VNWu7DVJWnK_AEGh3ZsLgaWJkq7u2qMi0J3NoMtwP3fG_1pagp-lTJR_tRipkNC80DP-UHeqEIzUo94jQvfDaN91-xxegYd0XeYPtUPJivfh-UnzNVPlbRdAr1D9J92VET_emCTQeZjSpRMJe4-Cr5pRIhtVqtCFAEIP86_MoTFbvKRQ2wWLMSTVerwkJ_wjRrGAOQ58ncrEaUTjFlS_oX_91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=AZXBpjWrBFPrKOckoGAUOloXHYwVqOCrWVF0x6lsxpL2lGeK7JxCFMQTYLgktHa8XHzpzYV1oYynelf-tn9hipW3Snu4y5nsScNjQEBXmHqjIYRLj-9ypI7vE9w4VNWu7DVJWnK_AEGh3ZsLgaWJkq7u2qMi0J3NoMtwP3fG_1pagp-lTJR_tRipkNC80DP-UHeqEIzUo94jQvfDaN91-xxegYd0XeYPtUPJivfh-UnzNVPlbRdAr1D9J92VET_emCTQeZjSpRMJe4-Cr5pRIhtVqtCFAEIP86_MoTFbvKRQ2wWLMSTVerwkJ_wjRrGAOQ58ncrEaUTjFlS_oX_91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVBKu514oNetg3hEwpUVP_ObzskaoL_LZmRkwSInqjKJ461xh-Z8mro5hlro7Z_-T6shhRSZZId9syVw5w3oFx8uLrOkPJ1LKpGNzj2gFiilG4AH4m38QKbsAtJJBtjGK5U74_PRfeOAisBCvAlKIqb5I-CTkrc1Z9Rn4ojV416YFA4KFXWAx5EuAcjLZBTzL06ToEnk0l81-wpKxPe7qdC5ycgXj_RmqCXyfTX1bYZNqf4J8UwuNWB3Jjp3DGE-8WcJsG4duc-zZj0k7qSoiaceOasd3dZ-Nzb66oPDqfPjpLn_B10Y-ciDIWTATwYjOMWHcebhCZ5gIij9xr4gQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCCivtdhZ8C26izHzOEBkNtuZYtaDG7FT99iaYbg2QM2Ypo81VeJ3QxMaRn_WamjzFSfzqx00hDnB_YsP-7HJLxnmpTdWxgQWBq-HQ_zQBnh4MJDEbmjQk0MiDJAt3o007E4PuAPziLSbH0lj_DZZwFnIt0BawuJWqMVcv78zJVfviyWT54PZnte_2UWu2aKLOcaQQPVZiFUdnpz7pwTQSnFfeZ0rHzi3pfLj_gzp3BVxBQpXrU1Bd_YjC_d4jOvVQ96RyYumn91EWm70AV-t8UWo4Np6iqCw4kfajssyS50OXIwksgTcrNViLzAVRwtwa3GaqwtrpBBybGWEtg29g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=OZbvN7i21e7kVOgSeNhvf0aOcOHO3FHxFuLeLY8SfeAdfWHZsKTKbUVdlyyA43HEMUJYLuARaGvKRUQ538JcY9qFohpfbffwt2BE-TvNSXWQUdClp8YgU7KuhGb-K-Ub9akq8PhvjW3gstuvCEw9Or3LJngWiqQFPYdWKeIgt7NVrji9TpfEPclGfzGMcjZg1ZDHbXwXlUJZ9aHDTlB61s101R5pGC4l6Ic2lM5l4grFHthSrcSxgc_MFWxUorb46ZOFnMCP7Xf6lrhG7UPKt5EuLcjjBYYR1JceCsjJtU2AIPQrmMbRou1-NUi3ahh_8DIoU5F8pPRl_YCITAF30g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=OZbvN7i21e7kVOgSeNhvf0aOcOHO3FHxFuLeLY8SfeAdfWHZsKTKbUVdlyyA43HEMUJYLuARaGvKRUQ538JcY9qFohpfbffwt2BE-TvNSXWQUdClp8YgU7KuhGb-K-Ub9akq8PhvjW3gstuvCEw9Or3LJngWiqQFPYdWKeIgt7NVrji9TpfEPclGfzGMcjZg1ZDHbXwXlUJZ9aHDTlB61s101R5pGC4l6Ic2lM5l4grFHthSrcSxgc_MFWxUorb46ZOFnMCP7Xf6lrhG7UPKt5EuLcjjBYYR1JceCsjJtU2AIPQrmMbRou1-NUi3ahh_8DIoU5F8pPRl_YCITAF30g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=pqn1U4nubNqGDS8dbaBq1um-lbP0MYL8nKn0nrzq7G7m4rsUZFEjHwiWXNDIDBlTN8Vq8NjKS3wnFe20sxVcBgtwr0QD2J10KKVqR4-YpHjkWoauhNO_whY3D5es0Lq-86OE2s0_32YkKyz9zsTbIchcHWXhJHdXEL72VgyQZVMf8gThZJFIZSgvsIWGS8ZWw5ENdipzXZSnmYErJgb93LeNtbbPZrw4cPTz9yG4Xzcd1NtUMvgHPJ8z9YNqLXUhdv1qGEzJA2EezC4Bd1ULaSZgRXgswQ3WgEFaDFRo6_RdvI69Fxigzkyp2_B5R7mrhgLCRGphg8hC_LlnJI90HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=pqn1U4nubNqGDS8dbaBq1um-lbP0MYL8nKn0nrzq7G7m4rsUZFEjHwiWXNDIDBlTN8Vq8NjKS3wnFe20sxVcBgtwr0QD2J10KKVqR4-YpHjkWoauhNO_whY3D5es0Lq-86OE2s0_32YkKyz9zsTbIchcHWXhJHdXEL72VgyQZVMf8gThZJFIZSgvsIWGS8ZWw5ENdipzXZSnmYErJgb93LeNtbbPZrw4cPTz9yG4Xzcd1NtUMvgHPJ8z9YNqLXUhdv1qGEzJA2EezC4Bd1ULaSZgRXgswQ3WgEFaDFRo6_RdvI69Fxigzkyp2_B5R7mrhgLCRGphg8hC_LlnJI90HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv8fFlJrQ7kplb-pJjqMDtjKXgaBXc6dVRm7-frSCpUMQ0FBQ7eFJeX75V5py0Av9oFN_v3okGDS_w9gX7yz2ydL1M-N8zPfhG0DdJVKf6OWWHodxZ5wBbBdEpd11q9dUMCJlnWw4JRs23E2VjOhHWI2jtzwbTg7HtHwrIvXjUK9pXSu8F4KqJbG6YldQLUIgkayjmv4zcnaACn3BLnjnAbMtYciENmoKuOL_mdRFsfsgAJnmXf8mDBSo-a4drzY5JCtWixC-LTkYzolQpuNeenc1Eay_YMbbK8BmhfDSXjVNPBa-9en_X3Ecx2pOPr6er1ul7P9k1U4aFab5o1UCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=aR1jc8uRBH6HzMiC1riW0RzvLknXFXZ-rPYTzGnoxEhx_L_NIVZnkQom-SY8dhrQEI5DC5YnX95aK_Isn6Co-76R74_sjTZc5IKG7_j2dcFpj4VzlepKwZP_Qst-40Vf7BUXMh_Lghn0WbJqjsMubcwuxKGmtSU9H7hrrwzHfRAduTdT2jGTpIYPnV-ifJLR4rze2G9hsyQcllsUkrvo0sV_EZeFx7D0IOdApFzJ3FflVMbN6WC_6XgIBcYPkH_kZbi6tIO2_teAh-evJxIjh8jZnZPt0ZD0cISw77WUmTQSjtn7lGdXu5j2-DA5fOVcE3bs33hZhgHToXTV27e91A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=aR1jc8uRBH6HzMiC1riW0RzvLknXFXZ-rPYTzGnoxEhx_L_NIVZnkQom-SY8dhrQEI5DC5YnX95aK_Isn6Co-76R74_sjTZc5IKG7_j2dcFpj4VzlepKwZP_Qst-40Vf7BUXMh_Lghn0WbJqjsMubcwuxKGmtSU9H7hrrwzHfRAduTdT2jGTpIYPnV-ifJLR4rze2G9hsyQcllsUkrvo0sV_EZeFx7D0IOdApFzJ3FflVMbN6WC_6XgIBcYPkH_kZbi6tIO2_teAh-evJxIjh8jZnZPt0ZD0cISw77WUmTQSjtn7lGdXu5j2-DA5fOVcE3bs33hZhgHToXTV27e91A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gws2pyn0CUv-MPE3zVjyxZlU1_uRRoQz5-FtuG7MODglHI0ROBsxjeheLpGQ7ahDVpclsPs9OSJlMaAL05nb_3Tq2CdL9Qc2SyZfFGX_941rxm7ouJ9ZbjPhXsT5ACr9q6eLwaNDxLyZ3D9iToV4IG6O4oWLdqHZDHDLPtqDDtmaIFeFuw5UgCtyRhSR3ASMMlOseZNO-zYYRXcMQmyHpHJ-RFzc0H5uB-xUOoR9iTxIV6yikBfg5zFI9Ki3wyh-RKaMjNHMJkqZ9F7srqegKM4FpBhsFWIU6sXMgDayg3mtMw7nqz9WQ3bJ5uxCO3Kz-R9eMP9acgLTUe9EYWi5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjnRbw0HSQyemqiP4PPPchDTyJyfCB34uf2281tVT_UplbN16M8MCgEUPN-qXyLmcHgw0YcRbcRlV8kZ3s7bb5ARC-ooww7mHZgWHQNaCyGsPc3Y5m52AZoTKg98Kg_51O0id2O5jp4eZQvEn1If_hUQgy1OBGbaWsGdh7o4pIAhqq36tokwoksqRZRN_E6ZCdFXx1yfJ9CLVn8_KOTIA2jUIGd_h7jmhapkjBnDGF6NKv40Z30RcdcNukFjcPQ-BfD_A61SSwGn-8HrNcjRpLRXGKQqVkAnT7RJxe0jqN0Xe8oL2lrFiR0AZHdA_8y1eH62q3DxFTB8jbd7d3IgjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9U6R607nK7tEvvg4g5adbj40H_-czJ1-L0uB_c_E5uYsebw1bcsJGOtXVQbz_kY6nyqvSAPdtqe0JdyzZKrpstsguHL1SEOj9440jdEJFxDJSZGJQn6t9L073OuRQaZWky0HkSoZ_R0xrTpYGp3F8yBOB8LJDH1NgfXj_53_guVWTC1OuK91H_qUewRUMDi1RLkSVhS_2y6gKh7FR36nMHwq0jyNWXl0s68qzW5RM_JmysbViZuQchrrV2yq5zmfyOWFG3bH-3Veh_GdNC0ssW442AWTlOZszedchQ-07hQC41vPtL-EO2hihx0pakKO6WQpp90_xmJVep2CS83QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWIYjZO53eGF48IyqnF806B5x2AsZFgHe3yDYT-CrlfsOIOkMsXsT6dkQBlxy2nGRkO72lI5_EgAipFdaUWtQY_bLnzcDW2HlyvVTvkPIfy62vDVVYLX1TwkvRUu2Eu0Xgk0AeSmGH_P8Rz8pZTeiUdZt-TA8ypLp01Rv9cwkjTNiB5p1fSAeAj-krKC9lCF_8nVEJdLm1g4JuB9kaIzwyPsKuLd2Fz6_x0f8yulMYRAGUeGPi0OaMg-qUtVKcZBEEMgwA5yJmy5DYZtazKR4l0hHRYdG0VHnJIJ4m_NGlqX1-SOnzo2lnv-CYYzNbub3OyuyZdU1bAFCc_9ICdP2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=OZjVVdacCZ0iIhTt6lyq5CFGhZdWIdCuGHz8gfAXzj2DumbEuanXExkNSv9CjknrmIbJFNJ5URCUEXPap2YJfTWgTiQfR-BqSjy4PF9DWmzOfy1JWGB5bLh3QYjD9dTdbiCThysC7fOOFp1x8JBnM3JGmYKglwlVZU6PdRlUalKWvgjpzP0gJPZsT-An4MOzCeoH1ECuDE_taYc-9jwtw_aYskqxv-aXLUSZm76BhJfrYz23wjkFoCScBBs2Oo1vVoFdhkYKUb6NxyOlOvtEcN2k0tJhx-ht3OCmrSzxryHzTkxQQB4EMyuM2PQF7hGyO1H3X07ImBt5yWib_k2QyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=OZjVVdacCZ0iIhTt6lyq5CFGhZdWIdCuGHz8gfAXzj2DumbEuanXExkNSv9CjknrmIbJFNJ5URCUEXPap2YJfTWgTiQfR-BqSjy4PF9DWmzOfy1JWGB5bLh3QYjD9dTdbiCThysC7fOOFp1x8JBnM3JGmYKglwlVZU6PdRlUalKWvgjpzP0gJPZsT-An4MOzCeoH1ECuDE_taYc-9jwtw_aYskqxv-aXLUSZm76BhJfrYz23wjkFoCScBBs2Oo1vVoFdhkYKUb6NxyOlOvtEcN2k0tJhx-ht3OCmrSzxryHzTkxQQB4EMyuM2PQF7hGyO1H3X07ImBt5yWib_k2QyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=aAt2en6RlRS40chgfvpC9JHP6jZkIZEYqnMd20_5aHdML91DUk0UzER1E9EohYkmPe3jMTAkZUO13kBaLJZ-UGL0c6naHsAipbWAX9GaE6ksoxuwVCeBBrdYpLmEA5KWIHfTGnQ5K7S7lKKbflu0H0iWEMb7MfoeM01kkpyjgzkF1HbRaRk5q2004G7Vv9xTtgnberG5W77HSwgGswhIGpOanqr9Eku9U_E2tBiZE2SEcKImYUQyr9Gr41pb6mY7uCTRVWeilFnyfwpB3fHVjteCepv4O_WEicZV47ljw_g8VTEQASmMvEZJX8gWfl2j7U7b6_WXOnmc4hKYEI_NeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=aAt2en6RlRS40chgfvpC9JHP6jZkIZEYqnMd20_5aHdML91DUk0UzER1E9EohYkmPe3jMTAkZUO13kBaLJZ-UGL0c6naHsAipbWAX9GaE6ksoxuwVCeBBrdYpLmEA5KWIHfTGnQ5K7S7lKKbflu0H0iWEMb7MfoeM01kkpyjgzkF1HbRaRk5q2004G7Vv9xTtgnberG5W77HSwgGswhIGpOanqr9Eku9U_E2tBiZE2SEcKImYUQyr9Gr41pb6mY7uCTRVWeilFnyfwpB3fHVjteCepv4O_WEicZV47ljw_g8VTEQASmMvEZJX8gWfl2j7U7b6_WXOnmc4hKYEI_NeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdkuuZYVojyoIOoORMkgsWXWpwRkYu4OC7frvWgXnmQMlP9yTKnZKR_OYOvYUVMfW0Yiqbbs-Z6kbG0qSHH1lRqft16gdalr0FXQCPPZt_b53UZYf1skvrukfofNBTf4FKql0nXmQMzfTXkU3DVM4_ZVRZqs9A9qtQ8w74Y3Svvo8Z_1de-TpQ-j4BhZK1HqeQ1f7FYI4COO-86kmqGxNO4Iejj4SHbFaljkkmp210b5fJLfNzupxGRWCX1i6zkTfIrb4AyN3iKHaeu-cyG9ysNIVICzNykEt1VBXp_d_q6NlmF8c_H3iNdAVow0PyP_jpfuwSguP9hxYfwpwkohYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehugQeoeY8H1ERHc13p4zkzZlxNgHbcCtzHVYLH6k6px7MgNpMvw-o603VmZcleCySTwjolbQQ6cSbVzXwDb7Nd4s_a06FzgcjocJM10_0Or5lkMmdt7CAY8gdgUsx2tdDMGTsHIsghTItkXyrn1u8nJaQZEje_KsrdO1CuczBRHfJcxFpuGJLD5Od81Up-Xas4xLj09zI0CR5LEvqRAdIpfv3geLQMNtXRZBbDMCJGuNrv9cTakLFOpSc2_hrluumUe41uIbg87lZ3OyXAAb5cWbmpbfq2izau6us2lCaEMW6vjVsJFiVe439QKLgIu67fuzAF14PFr0vM0ibIpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBxF2ccfJg7jj3K1go1nEpQuja2adZF7I3LisGGmmsm7M-_tcdEziXA8VVBBmSYyvqkhPWvx4gITE8c1KKPU-BmsAB-5Gt6bO0HM231cYrATmudjswwve5hpq1xiYOmdhZJ-rK0HN1IS65OkGHVI24bV-xZ1QepwvTb6B2AsWCuHuynFhgESYdpUNDUyEXkvjd5yWe5f7lDunY4HmehUPmyGIiEUEzOoz22l3LkJXsWzKhi0Qhh6NaUy83kms5wVI8t2cR0HZOxAiL6uTldiKYH1XOCxPNuIbd1ua00uM7Y6Zmbu_zNaWIbRjsLZxJZ5JiQViVEhrcFsv0ah0b5NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWSfBteUcYHa2e3mmfNdPpLQTa3CivcEsSy6RxKFIjdOdI0Z0ZUWV_sT3aqeflvWmvj-4OVcQUEyNlFPpbKO7MDrJfi-vyPZ7GYyj-mCfMvPEQDlq-CW4QHDnnMXV0Q039uUdjOsmOzLvNMqj-0zsucM0Ulm7iJYBWggXTR3oEfwXvI1e2YInj4M_6_-V5hkNqNIyPeM4qk-Ko1ou3S7zHUb8vxIXvo-MHZnvnzPtBatMohkEGafbxkY9VNqmds4-Wc-Y7vqgyVnQ1ddzdp2hWkb1soDcJVu0Ul1G0a59JCgF4CCNP41fsta_3pgjBbIbziTcFHSNld-Fd4F0X8oTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUp3Kxv_McS9rF_SB1aU3mrtJ1kDBDnS9VoL6kHRTQNEE0vHSNDPaiXqxrK5gH7cA4eWBct0imWG8z5fF5sMC5i9oVelgs11eDHTtlb2TnPFI7MpcbhZjsDP8Ggia0zeZr_zr9LYQVxtT7ub2aZZ2C2vBpa8B9RYJmpDCi2lF3w3bVj0RLdULZxVvuK_MVV1XhXa_xL5U7nTdqhukLL_iO9NeRmoLhoNWRRucNqOClOfmJiTV0VYpdDMkPdgQiMERj5H2wiYENWW7sziFzL7-KkJmqglvLj3ErGYE-AiuSfq0hIwaZyhoRvPOZvURMyxn6E5r8czhf31FP8Ye2FhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOjfmgrqwTdYhjz_BO5WtNmCzzSGayJsHFhYLG_RGbOkzytFDrcCUWYm9j9oqb4elzuSinB0qFN96cXea3iZpxZtvkXhBQOGQxXBkjCAn3kI7lK7u8uVHH7JPz95pTUjzaH_xarBLEr848a27KWqcoCdZwCUADA2k2sekYkFwsDnK0YJmlsQHTxdJMK7MBNbGln15hxnCT5JhmDuNo-3Gog4rjW7h1evqkC83yNKY6iL0MnoHV5-6TIs_2KklTx416pOaJPSmJpdSkWnc2IdhC7FlUSwP6rzmjWI0yhmNWeCvGYmQZiPMQyL2bgVXs4YkMK5MvpyO8MdmAc6WBubTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUTsftKEY0nYDctyj7XX4WyPjxDJBBQZ3aJxM3qqxhHMST8A2FjKuQBuYc0pi9pvGDGLWXtG_85RYpo8uwYk-THi0cr89z3Q-IkkAR7OtlFQNSzQIyxjU39jhk12WA2ivvB0ZxuG0why7QDV4X2z6t_-azwa24fdiH3vB-x5tyJHYBn1oZ4n90FFeqSyrGTL1yNod45cEY_e9f49lCFALq-JTKQaY4we7Nz8N8OhtGSci5tDfLYgXLT6AJIIGSXe-8pKuj-9DfoDyUCMtrMnEOG8-TUrTzcGfK9hOh4K9mhfoM9o6xt1fSUx-guo2gzrRsQSY85Eh1mn03_slbb0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV9ksgMXSGzyp6LogH7M4cSQpQtxF0tJVLJj5YlYP6tcqbm5fn6c7AMuljGOCgOYCI1d1e4Xijrngf5ml1Ozdf92RZpUqG6o5vWSEgOWYyigmymIiFGb5kEyDOKqHeXsnXVg6Bq5uDNezQfD4IitUV6SAC_0Xg88XQbyg3mpAcldKLQ0rTr20VQzCn8yffWGb0UkErHobxgd8__66268BkgNFl_G74F_9G5AoHhaDZxSFjpj_xtTJQXOmQPExQX3VkDIwd2Dc7Q5CnyakmbZlnjwcGX-Y7pG0anhWxrmk7aD5jRHcealelnQxMFcMLPDfBtrDn0FQ2ygLifKrvLBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0IKe4SmA1XDCRyD-dd1_XRdktp23KfZcfEGEuypX0HtwY1Il_265m5Y0lq8IFHlULX3J336XqT9NcgKM-dhFkiz8r8AUHz_DwebQZYEIBxT0e8hVjGQ6787RYUNAT1Y7aL-dy2ZlfnwV-6pBkrNTYkDtLti7pfsHsmgRTI5XBiTpQ4m6AiyS1rixGuondV5xxT8gb_pmnKo3zAhnM_o0c8k1_IDqmEIPH27yUNETBYqZ2qC-sZDV3Uh81TyUZZhrJqMsRYM38pI1GH88356VpwEyYAuNwdtJbiMcJevV2PquSdhbyVvU5CdI9VaVBguGKHOGTmVL3JPpo3y_e4baw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=I75rUDsCGAGqGZV3GoE-wKQFLdXBL--OTQhpiw4ogDFGrxZ9SkQ2o_4qi5bEr8SFXsYTZem4WFar3wd-qVV5N6CwWn03B5PDYLN5aYMqRGPiXtz-ABZjaDA5ihDgNAGsKdWJZ7yIO5oQF9Brj3MeUGDrJMFhh-avYlr4-6znoU09L9d80jA83cigJ2KGA6yXO0D-GIumwM7qzTpeW8Fgl4KOqMdemXhHTUy5tyyW2JY60IZFVkLzkUZA75JV8X19XzPhrTOoE_IkRhqnIHJ9j_-QX0eoDymm7rmTzWHLop_fWsOa6wXIDH07Fhn_JZfYvvxZqFoW8D44DVP7vu8CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=I75rUDsCGAGqGZV3GoE-wKQFLdXBL--OTQhpiw4ogDFGrxZ9SkQ2o_4qi5bEr8SFXsYTZem4WFar3wd-qVV5N6CwWn03B5PDYLN5aYMqRGPiXtz-ABZjaDA5ihDgNAGsKdWJZ7yIO5oQF9Brj3MeUGDrJMFhh-avYlr4-6znoU09L9d80jA83cigJ2KGA6yXO0D-GIumwM7qzTpeW8Fgl4KOqMdemXhHTUy5tyyW2JY60IZFVkLzkUZA75JV8X19XzPhrTOoE_IkRhqnIHJ9j_-QX0eoDymm7rmTzWHLop_fWsOa6wXIDH07Fhn_JZfYvvxZqFoW8D44DVP7vu8CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=TUDxg4F4TJRTr6ELh4GIWocOThFHrNXmFWdYYnFBF0oNiovWYPDegbu23A3Arw6bTIDsCrAcb83VYqQ29ibwcGxCW80fMcq_wXbscjvLprFfgZsRRUjAGyWGFzJig7lHE16UXsa_8QKfYxDUpTxq8MHO7qA-gXTCT2qqQv4IxwTjbsqbZbagnFCO_SXg6mZK16n0Ph-8WwUB_TnwsLuw4VXwIuq1d4aryaPP7wng8MIaWU-C2Gf0ef5c-dqrDXx0jGMPVNxBkL-lJVTQVbeh-fMfqhJB0gPUgrsmUgfZESAro4T4js7tNaP1FmmJhX3B-1htbqVxmAsgrp4v3ZY5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=TUDxg4F4TJRTr6ELh4GIWocOThFHrNXmFWdYYnFBF0oNiovWYPDegbu23A3Arw6bTIDsCrAcb83VYqQ29ibwcGxCW80fMcq_wXbscjvLprFfgZsRRUjAGyWGFzJig7lHE16UXsa_8QKfYxDUpTxq8MHO7qA-gXTCT2qqQv4IxwTjbsqbZbagnFCO_SXg6mZK16n0Ph-8WwUB_TnwsLuw4VXwIuq1d4aryaPP7wng8MIaWU-C2Gf0ef5c-dqrDXx0jGMPVNxBkL-lJVTQVbeh-fMfqhJB0gPUgrsmUgfZESAro4T4js7tNaP1FmmJhX3B-1htbqVxmAsgrp4v3ZY5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=OH9AKNV4tWkk0mirGgs8dsKyEqluEYDDFbWsiQnRPngda623M69a3IcjCyNn14kPDHo7yRpHUtgY6854KHCBaVhy23emcQ1re3eiyMaBtcYHRa6qrdfaw0ZQb2gQovPi41zRwH-Tsg7yW4wDkLm2fRl6zMoVyHR54ZiQeYJIF7OudiSgKJm-H5G65ARWWRxW7wyH_RgZGDh9ApzyBotk5bdQwudGehuPOsK0igMOuJGWCsZKdzjT_A6PyeQP-Xqv7Km_XO96NZ0m07h-cz3EFEy-z3NRaklvMXYu2UynCzCBuRfNZ-3MIhG5DiyFeIRyFnbc2Pz2E2wq9bPeGxyS2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=OH9AKNV4tWkk0mirGgs8dsKyEqluEYDDFbWsiQnRPngda623M69a3IcjCyNn14kPDHo7yRpHUtgY6854KHCBaVhy23emcQ1re3eiyMaBtcYHRa6qrdfaw0ZQb2gQovPi41zRwH-Tsg7yW4wDkLm2fRl6zMoVyHR54ZiQeYJIF7OudiSgKJm-H5G65ARWWRxW7wyH_RgZGDh9ApzyBotk5bdQwudGehuPOsK0igMOuJGWCsZKdzjT_A6PyeQP-Xqv7Km_XO96NZ0m07h-cz3EFEy-z3NRaklvMXYu2UynCzCBuRfNZ-3MIhG5DiyFeIRyFnbc2Pz2E2wq9bPeGxyS2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5gHvrYFtvezmD-_gIHhd76dxq9anmObgvM5Cl76sE-o13Mbvo4pR9_wXiqkWSFsk_GfB59JQbPr0_h9CWxkd0eBmwFchxL4mEf4wTUcren3mOU1DkKst6g3AJj0S4atRdoEfitDx25-Dd04OgfSJ2pYJfEEALKh1aIhr7-EEaXvxYVsQ6j5YrXaU2Ah4GFtjSiqSSAE2VvbPvFvSCOJh4gsDzs2ermTH2l7DeixSq3ngPKUnkquVHwNZRs7FqCvPVXFyf7cZhxZDriiPdjQWrDkb5U_hT1cYUNnV-MhcqL4HMKS0hLEMQDQ5iuLpJ9z5JoH2-Pl6VvNxCLQ3f1w3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THaszJ4sCeVND3wpvQcWXWIeXsw3uPKAkWrh8NQWc-9PbzHgtuKFl6-wz_x_g3AogK_u4OINuYtWd3BGoUSq1KvllsDCYf3K_7PxKja2614ahLHyRUqPr0e4wHjK8YzazRCUpskNfi3AG2zhSdGk_N5OSJHW0AtRGwLOqWVO9qj2M5VfgJ8vcOkR9EyA6mP1QJ0QFU1YNyzqisp9kiKK2-AygfOd4ECXTEXIm2hHWA0NHhRHJbbKPmEOLkwYmlV3x5Rtj5EPnVPmRC6bVMabjADis33A9C-e1wuHEIkUeN0BeFW0j9LmDs1X6V1AihPh2EOdzNgamjhpTh2A8y6tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
