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
<img src="https://cdn4.telesco.pe/file/FZiO55tkzNDD_2W2N9PRMP4a3ovaw9p9oXugPRwvLkw2HgwNS0VJOr9Tp3P87fRStl7HSn8cYGm4XKwwfs4NvqVriHMJjNWC881AAfyiAgh_nXgRP0Fs0McOLW-P-vi8iVf5zEQ5xmTRwbZT9SCr6yjmYpygGO8K7-EzEIyE_KV0eT22N7xwlgFhn6Pj1UEmCO7_WCt1_QJem9NxKxJ049a0F9me4x6x8V5YmW66BM8sC8zNOttEDhZsBcCVjVtS1mHFSPACJgaeL3vs9BZ6fcq1O7mtBVV48SsGtLOzyvvgSMSh8y6YL75En27R89UHjH2yBMIFxu9JDyKqOnO-kQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 456K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBMEH-7NL5NmkF6G30_Yur-A2fMoInsMHfIyfctlJ0WFzn5YwyPqlaZk2G5Qu-WPw1aZecHlQSN_WHuyBohF7APW7ZsDcnY0zhd6QEjvsw6RNZgC6frQhS0TRRELG3ZlFyXI7DJcj8Nq3FyctgiQICAk1yPFTjzjZURYgw12tMm-_ut1Fe6gVNoBzJwzUOUuyZXjweOe09wjF-thXvKkzPudVWUw9Qt3mrROFIcZFQoBFVL1ganCqNaqiuhGbJoOnvwHeM8eTSDshmgFPHC6op3i6E-HAl50hsLWIGJVX7aetlKjVhBd0bk0nMRj3IOIYeXI19rtJnURe4TtttwdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAhmuTQ0YZ0vlQj81311dWCpWbjqBu3cAbMz3j9oc_KjY5fbcEwMLzMu0i8TvJK4SFI2uAS-nQ9fSxeiZjHEha1xDx-5m_qrJ2CsEVp5F8n0OSDv5AT4Hwu74AZB8gP6rRBHjYkHoum65jhoA0tzTsC888toPK79EoTaoJWQAFao-edj2ZplXpI8x5bvFkhjt8aJc-pIK1deMqs09Y3Vp9MAzW12Z_OBTEIrtlxsOI9kgA4vk-ppcQvQrRMqMNG6OhNoi0wt_bw8QAZwVDnFMbVBiq3WIq627LEYVrZTqoK2s1cApp4FDkrT3ui23VYXKagrcH2QdYoMUfh-JgysrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv23Z7rhs3RCxr-dOJ8N-ijV49pI04tFCDaSlXazK6xMs4UyFekJfNfbdsPaN4C3kSAhTx0bkwr3x51_2Rww-XeE-6GpYABZihq45Xy739Qarn7UszLUqQuJVVA1kQ6kZ3mwgsD5ZNQorz33rSDXf0GSMFCH7RKVfwOdkJMh25QwaR0GEQh0_T2wnfGqOuKLg6jC-FKf2O1rP7lWHgz0hKXGGKw0g39_RRQ5QVxOqtRQz17rk5lALDojpC9N6R5aphxYIIlpJZE-kUsa_ihp-3_C5Odt70M-PzKthZXzmUl8KdfKbDqB8jmneDRfQJKe4PZDJ2HH00EBgrKsq1dmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUDyXmJ36FEU_MT25i-4u2knrfB4Z6_u_NWWMF_Afw5iZgQaT0XdDyusTKGid2kVNa7HftQUvjaOSzzCkPTNRn8_XvDVXbuhEiIwc2-4f8YmUryyHL4icJz1PdDDSFTDuWk5KTBdXoTj1Xcj1zQR8iMHVIbR4xdcNQCjoRizIVfhvS-TrqNKj7z7lBwBHpPJgA1lB1mklHsaxkUG_YmlVozdpFtO51-GRmE31NkEu7Fm8VQFRXlkFm_B845O0k0ZgVvua_ax1ah_Wgxo3xXzBAFXnCTtry6bTr9wvajXPYXHvvtOGtJgx0MjAskbVIwvX9_UOtvWC6q43YyEcBrLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2_l66wN5k9CQOaT6Rix9G-x40nZ3C6o1igDBgQXGWLus28SsllypWOFnXPhALtyfblsvo2I2rGDWpbLo9hcK6709slujCkPEITmWsGfEEHuWeaMJzxreIkwg_zpZAUxMYPhiGSs2THcZQRHkeGoqpAaVyxLn52CmZFbAAPcbYSC4ukSLt96Z6B-MZQKApWh1yakL6HtxB6Dx-W4F5R9pDhEUpPSSOpq2vscrx_bQvP_ejXvgkwRNekvfSqAHBVIY-h2oGa_i2f2cYbdnYvtMUOkTNUOix5O2VAMr9sgjtiXVu7jn9PSdKkpUVBEpQ9h5gzWAMwItCUaRqXcYgc_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmC4UYlR37QuYf3tPuFAYC-L0cLbLgCoSbMJlBxT5zUZEIYy1U-YUcNZr6YrZixaPjsYeRHbL-La9pxwItW97qyCbEotYXi19yl9rkzAjluyr5kcji80xnaziqniCfpe6JR66oyGZykGa3VTalkRXBhAl0YwxlptGGjerMeoxuMA8GVe7tHixFbav6wdGTF40rZ8NuDNYXvoxWHlwEo3pEDnuVlA7SaYWNVGJU0Rf4rpKZeADwlqaK4LRl220FcriVBrYHHfUSGQARtU5GHErvKEffhL8Z-M7zjys9oZfqUGjvHhSLK9anOX9QOMSGT4II_YXEEgiLSj81lUAr3mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ERqF_zsYr7LAjZng3d4yMUGh4wvNqoEJbWpn63QFDWc4Gt3uRe0PWXC-JXJMqg_EPw77uv4G5ML_uiXQNkkRLGmWUoEqD94uNF1LOWOEYvWpB8SPCI2OkqcdH_pjx0JRFEeKND0a1lc4AopSO7xBHtjQnxea0xGnRV8rz7WPsqyXn1xV80IwW1k5tPTc85AwDM75xx5T538GORcWiJ7xRlsr8kFuhGj_8aDHqRpmdGIj65jht0tzx0oDJi7-rfETkuV-P9c46r1gB34TB0RoFd28XcWfXyeuJh_D9wovjcwaJCnRExK-5VF28elc4-yTy0Y2c2fdl8boqZxmmPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7GaLUhaogIXL_lGBaVzWoPNVCq2KprvpCdDXjUaE0cRKujMGFFE7XoeB0oGsbJSPjHZyXPIJJXRmVBvWA3v-RfqwkSu3U0WqevGAFInQOhEodtbUsbT1MJPXCraA-z3FdQEpulefUWuqdUwIm4bmqtqlwaY5GCLMAsaxiq4Dz1vMCffg3MlM3B00cmBZo77mrVXjZlkvYlrM-6AAIdhdO2uDeN20bIAsHJ0UhUk1JCvDznl9WkeoPXMSAj2c15dwOA4RPRNGLDKzbyTF_EYAjgRE2gcB1r_HQflGhFucquUGhpiQ6tdPaHGNJqn_Msu_k3jgjPJz9-TxelTyCR6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVv945PSqUUNZO5M09_SD5AFoVPXDuSMoO1r8hda6fEWwXXxMRGRpFMOGPWpoLzlPzSUFdHGRcPWW2Vh9yOYXnYzGLs_MrCejKjmjqrHDQ8WFKtWPvY3Y4zUwh-bxCBIZvpsPyPSOhBn2QWA0Zanr_QoYRgf2LI03ijLmoOs7-i4Lx_FjuYBo4qdVeeqko3D-2Ls2k2vZzwL6IMHCPdn4-PMY_wNHmIDrdae670qihZNJ17qkqYx85K-MxogbCzDdHCpfLddYuiE7GakpY1W7XghFswCiwUUOglnFwzB1kx_-n0gqwNvdbZvZedEx1x46rpvmuvWWDCvL9OyXr9LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OY0_rVcMyf3kXqtUZf33-b7V7ODo-vdTeXgyOGuiVnqPNYjsLl1nwEtoLeolUUwhdSeZqD4d4nJeTTjlDWQOvMotCVtBa3q8vGe2U6Yi9gspBjx2JlU85aFl4tn9hNQFhPEoVpQADRTHfza0H1qhmshMBegX6VuWijn1RrtZuRw9hZgr8AYI0dj_F9FOa5_RtVGa-41KF3t-PcrP6cM_wSZlRQJG9EjG-CUNS9U_7FvwJ36UlVHGPuRj3WYAUcOWJZ-VRLVhR0EMe7jqJ14T9Ty1klcUqN9lsWLoBNBRS4iuXOWyoV1yCFiLw7YXLf3_42oyEdzAdDSjeePvZ8_VPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OY0_rVcMyf3kXqtUZf33-b7V7ODo-vdTeXgyOGuiVnqPNYjsLl1nwEtoLeolUUwhdSeZqD4d4nJeTTjlDWQOvMotCVtBa3q8vGe2U6Yi9gspBjx2JlU85aFl4tn9hNQFhPEoVpQADRTHfza0H1qhmshMBegX6VuWijn1RrtZuRw9hZgr8AYI0dj_F9FOa5_RtVGa-41KF3t-PcrP6cM_wSZlRQJG9EjG-CUNS9U_7FvwJ36UlVHGPuRj3WYAUcOWJZ-VRLVhR0EMe7jqJ14T9Ty1klcUqN9lsWLoBNBRS4iuXOWyoV1yCFiLw7YXLf3_42oyEdzAdDSjeePvZ8_VPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D78ojxFj5Qsh-kxf3WfK8H_U-MdL-XXbR_YZnALLpFHTDmP5uIq8KCVZ5RaKtPkoVTH7lVUsLHPo9CWGT1DI3Grrvd7w796CIWMc2E5gaMMz6Y0YaLw8YiruUiLSa46BUZg2j7mnqRUi3XR9qS6bnyeAkKL0xtvo-ZtR0yniQhj3tzimUhf-0LmeJdVjuQWIV7h908c5O1e2Ur6m3y2CAhJRNvZNjs5-syN9F2VOvUjQZ5zpDU5MkwxyVcBMI54czA-dofhu7VjichprtyhcuXuWvjbrq0eRB2oBPzVWPQt63mRfRukaqFm3smYiZByEcVQMkuoNPFfql5Jb7lcLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTt0SY8d0KPDQpKcQJXf5p2i4IMOu4HeC5ZlT5UumAo8-o8Ij2_WRiPDkGbELh9l7wMKFqBs8hPw9cWm9bMgc0xo0BhVt6h__hKrFZgw1i2fCpYPX-S_BBsTXEAffh_PIudJqZWBxX_UVRPMWCCyNhp__ao0nUJeht11vQriQzM0KJKR4eCSBXe37D8c7dQGTgiWXEEYHroPm2GPQVon2d8PikK_gWR9kuuBdkBhMsq0omrPGM06MESJB2x-RM0LmI04CdQN74wwPg-GBeEn5sQ1ri6d9TJI59GfS8dtiE-HxiyniRFehzSNtJhdTMBpCgn3D4N-2L0rSz0WZPDFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUkYjfBIlUCslZJqur6TC62Ug8p7QIJD3knl3nAZiSqUQrYPkQtnXOqFfsA3brbiQPFimEo7LBU1KsbMuGKd7ieWDdVNvX4AIrJhfJkdv-TxkkDpDq93aqIDGnu0uAV3Z2S0-iyL_nhbCAm5MJZJ8Zp1RHkA9J480N88gIAIWGL0oYKa7Du4NeJNRk47ru0qNrADH7oYhAFDB89QZd45rHaCX7NypYEQnR7Zb8uZGkuHjFOCUdzPQ2KRw_EFNL9JnIfHVjKT-gVRckT6t92iYnK7bdrEf1w7wYpWPA9YoeqOIvWgz0hjOF-Y2mmRLDXcpcKvKB5FtgngaT66XM2bgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At-tv92HnblOsziQzOTfV_PLP-bKCr9sRpEtgcVoZEyxx02B4E_HPd_OZLzAh_cotC8t8S_DzLOYH6qSzp2mOtOM2FrR1tzc5BTVhmhKj9oroY_78-BRFdx3H5-uUeUJlhYbJU50gJYT45KeUY6lfr-df8hBcCC82H444VojHiv1EN8DOdIxmUiJXSMtWhS6caAXtbyppimU_WbSmcr1Yn_c-4S_sV5CVZmVELo16n2j9SpNzGIs__1baN6xH25veCtXL30BQpcTvupsKg4f73WglmetOI3f4gaG2BBOjEJoQxaKSH0iS-f8J4hUidw0031PqqrSwb09BR_H5Ha21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_jKTRmYLc3l7HC1dmrM9ZbZzZf5A_l4t46gWe_UU8IWL4fokBXMKUVwaQiLA_UzJdjeJp1aznAu2UvLl24CfRqt_M9IO2EQ4Os9k4JPflxR3tfDBfh7QjEvXvnEfjJ23P7FlVmkm19Op_xM4ebAj5g8-CeN4LerN4SrlM8SVGRxkDXHDMBFGln-Vz6PrLHPQ1aRtTi3ojb3gkAE3ekdoCjGRm8JJiVvdVSSrwwAOKPlVn-417LrKfSwqiLrk7ho8Z7icyFG3chmJSubNFLIUVVCmG4TPhnOpqzDj5jPLt1XQiZuUWy9kAVMulEPak7BD8b_UESJiJkBP3eKLvIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVgSgiitINGxTwFmc05IVZ_3EshXV9Ta0jK3CUgD0IMKOShMe5uUkMqxE7W4H308kUQWZInDWT3Yv0mBMGvDdh9Vf5Yg_uT_MC2VlRXe7-QSoeWN4jvurKB-4JiRgOyXWsWYFLXBWTb8yX0p2JYtvkRAzDbYL5sYkyVgAQobFtgK6KAQ00gWzeDz2gKY5rzvpnp_8gKvQKyJBzh8OR9mO9Mc8K1co5-6_mlyc9MQChxGoGm1MSjMWc0KHDZ1UIoz_hSxPmPKDpkt1dAjdssFpZNeBSC6ULTi3x9q7Pw84lcBV0_y_WJewE-Z9MDLHafzcqy7gwl7Bl_Pw4OUesIbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6HvTN37ZGL87s_OoFNpEd-r3xCECNQWzuJIAP0iaaequkGO5kGhVkfIEkun13z1U2tfQrS7bQadxWmxnenpvblVfnbQO3ZRDoolqO30pvya7GsAXI9p53iDzSoo6sGdOETnwIVagGG8ZUktVySJDOWdxbYSVC4G6uvCOMeBpaV3nBWtYay6S7sGR0HCQ0wGZi0h7b6llAsXNTsqvPaMmPeJKKw1uBuA_ZzHjYzYnE_rPD8-FE-GrpJHVfEWHaEUbgKNYVyyias4jUmAbkwiqWB5_ftZXuLoFqG2RsAyFe_ryhmgF5rKNYQ6TOUX1FFp91qYkbW74WszXMS3R1e7fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWUCg5QmaHkvsoTVoa7-_c8Qeo10w1auaQSq9rrgv1QVufYpJCKlVIZsFg9KVsqf4hNBKXycPHgb9Edgs02v7DZEft50Dc6ymyiEk1p55cs4tpZ0KEtBEsYmAhnemU3jGh8qVdxb4BL96DAKj9AGXakYORe1ZHZhOk-fWt72s7-NhpMfs0iiRV50peJo6cCbt0gvbh175zGNyglmQToUtLwo0-LgA1bzobJeJ3eb-sHDiBoyNH2FRzbwK9bbs4ZXl0ApRgNr1jTVCDV73V1xlrEFTYynGYzV-CI00DxCR0p59F_VzFGi51cLEG9IQ8v8T0q6Ux7W1pGF_FI2FuwJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thXebj5d3r-P-0bjJWGrB0rVW8N1_okxt41Fpgf2ecFtzjYeCupDxL8kEgMgQ7LlufIx-oVGQvxYqmsFijBZcmYWQsG5HlIpQg0VTxKeBK8Zmmakxp4G4sb907oDakosGFffw67bPq0poZY8cqrZaZAHHuXyazNEqcXwKbQrGaxOIV3iMkFR39tUtSYvLS6VyBPGGPnO4Ieqr4Gg-PANjJNT1fz-7wBc0Fuv7zIIJi4gS5xN0xebjkYb0Ux3L8Y7o8djnrhD_ECaKD6UnlMMuE36tVq64HDFE2wblEhCBi8XyLgi1z00NYtmjgsWuIyVs1hjz6jRCG_-RCtewR_UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس یک فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ یکبت
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r1
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30273" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpngXIDCHJz0sjujAjXNfzj-L5ZfyqhprTqKYwWLYiRTbIXEXuaV2szv18pazySdBRUqfj6CAhQXl1V6N1bT9HiOARz-M_5HahuwwZFUJZEh4cLykiHr8wZzQPTTW_Upul1rWr3iEE7jFgoZtnkBI6ye2Y4LMezZg2sTowJdoaycdNXRgTLQBzLVnWd_uFwt2Ig_EkleXGTNI4sr3_ldxDZ9V4p4uPS03rAS5Cw2DZzBTdHeoFl3ddSUzAF_IY3rBWMoYT0Pr69Ns-qiRbcX3SCADyDH7E5zqgQNpcaX4G2zEiIARj7WoUjVumJzps-Oq1mLBZ-j7e0ggostoEKtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CEk-BJnY6mYcvcyBiw-bHzxE4zaYWLyUcc3CecWm8iMh7jzrbD5-OCJO9fKbJprtdX6SWYM8iOXux1uCaoj7e5Kv96SqBM6MALzRoff2FmQ1OSgyEERcJRXBPIeEmEvB64bMRpzsQGJmgRbD2Tci8r_jSfmlEklgJ5NF-oXDwjTTL27v-xXrn5JQkMCgREpLXgShxkia1lVYavNRZGMh6FX81bk0moptPL-FxOJqZ8H7nKUBgr6VFX1hOZqyj9l80r8XyCrSantngrIj2mDswTFamRyGv1y4vjLAsZYEBW3a7JH5HGXW0eqffTgp32faM8Rsm4oXQr9H0zRGzX2tDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CEk-BJnY6mYcvcyBiw-bHzxE4zaYWLyUcc3CecWm8iMh7jzrbD5-OCJO9fKbJprtdX6SWYM8iOXux1uCaoj7e5Kv96SqBM6MALzRoff2FmQ1OSgyEERcJRXBPIeEmEvB64bMRpzsQGJmgRbD2Tci8r_jSfmlEklgJ5NF-oXDwjTTL27v-xXrn5JQkMCgREpLXgShxkia1lVYavNRZGMh6FX81bk0moptPL-FxOJqZ8H7nKUBgr6VFX1hOZqyj9l80r8XyCrSantngrIj2mDswTFamRyGv1y4vjLAsZYEBW3a7JH5HGXW0eqffTgp32faM8Rsm4oXQr9H0zRGzX2tDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=ofd8Q2H6xp6wEn3A7YVMWrFxzUk0icXFiAKOAPVAPa9toFV9pqtVKHblIdWvtRS44HYcnExgGCkJNylUUufxBSllFRjTFWp0l2UTKhsjWjT3B_kKi3WnRAwBt16tfxZxDCBpv337pzL9FM_KnuoxExyO_IYTETSRzuDCcVWnrZ3pJ4XWtT6D2jfbIHoLxIdzHkt8hE6aUfcqvlWefAAwLr3Mfjgux6Z2Fi8k674Bpw0vzKu5QUYu1NVqUsQ7dubu10_qbU7VRHTKP4tmuAwTm4hr6rXDrKUZW70gZNMH9_2_uJrSRfZlplRoQ4Tt_oDGgZNnPn4zD-tz1q1dPVQgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=ofd8Q2H6xp6wEn3A7YVMWrFxzUk0icXFiAKOAPVAPa9toFV9pqtVKHblIdWvtRS44HYcnExgGCkJNylUUufxBSllFRjTFWp0l2UTKhsjWjT3B_kKi3WnRAwBt16tfxZxDCBpv337pzL9FM_KnuoxExyO_IYTETSRzuDCcVWnrZ3pJ4XWtT6D2jfbIHoLxIdzHkt8hE6aUfcqvlWefAAwLr3Mfjgux6Z2Fi8k674Bpw0vzKu5QUYu1NVqUsQ7dubu10_qbU7VRHTKP4tmuAwTm4hr6rXDrKUZW70gZNMH9_2_uJrSRfZlplRoQ4Tt_oDGgZNnPn4zD-tz1q1dPVQgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-ojI5rTqTEJl1-6O8uT_eDMO_393YAl4-qUgRax277zc12_OUWvGt0YXpnKg2E2uLttoEAu7uEAd_kOgvszTax7fLFYTCUb-0Tqeh8OGIBJjvSvILM0-XLjkpiwsu_kUpn_-8M6UJps6BQOFzu1Wx8VGeC-1Afd9eZI-U_-Y49DLbRMxNNOlSp4UbNt3e4b24EnVGq9ER0ZqUWw-JiuuqFwLZ0DUrr02wyEjwvg8hdNIS_vz537P7wWtqyPBEKaejVz3DJdBPu_mdMg8nT-CnU2ev8qTzMig2tLrAVvEenp2g3sxabOOuThD6f8ujK_bxKz09KRN7XWOPrA3GHXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxrTEK5bjsdlOw-kegsmh4KunPpm7C7x1Ov0p1nlQ817ZC6-ygHpWU1bmw3AUSfzSQBqtXBEUnvArSgovxL8jgtR6BuybYsCjO5eYJ9tfNCCouAWTpN0a9V2GNQLlMl_KZNb1VBXh5W-NhtbATxEMFybeSsWMvv3j0SyVrGUmUUm4HG9ymfxEMK6VgxGX_9pJqQaovTYrezF4-EtbUCOxKcvew709UJl1hfefj3pB-UJd9XuhC8NQd_xnVXgZW9R6y9xK-QiWeWWxNjvR6rINlFbJ7fsnwaSXDHrcsvrrgoC3gzEMlyHbAoOvOSopk_QOcIscnLI7a3Eq4_y_zGr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9fyzlFBoxThjZPJcKq4D1qJQUSfjtlVWn_kuQBRdnsvcjdT66zWUBjpbhJcpH2188BED9dbnf1MzqnN0hI75dR8VP8lW4GM33HB3xJYYnAwAxOAiZzFafs-I6MSxmjSd0J7ToZcOq4hiOfdlCayQMmnTue2i3isErjU13QswUfJak9G6AUds7dZQC9k5BflG19_AEZYb2bejJT6BaJgLWgVTjiGC8R-WNxjtR8rUXOSIqgYSARLaehaUIgJp79LJNWcB2XAOAvCNOkbJZbBOfq_Y5XrKV3NijoBZvwG33sklg0X7OLkJk9NkiUJGgj7ipQLEfP64TjQvRlacRTUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_57tllRopNbf_eXcOf9UvcHmbPW1ZTicNK0rD4MSYAM05mjwQoWP3I0P57HNioWIJdxNHMqLWLMzO8z0Le7z6NiOU4NOADcntpmgdjFeUK6tFI4aOwJG3pe60SRzj4Du7Dm4n9C12R2SBwqdOZTcJ2NAuaPPp25IyF0_DpXsUACOUWmg6qIBX9TCaFtH0DbmtDFR99EBszN8NmCqPJTjmBV1EUXlZ3s0PjrRYIy8KppNGhtNuJ8eW55XEsDOe3lBkJdc5JhzVAw_Tz7HLfLpfVbJAdAberJQ55450vvnjS2tbsFqnGo_LHw8krSJOCvr71PpeAd9WHcRMZKIN5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJIYSPKzNq5pfaZn8oN4kTSULncEx6k0Du-8xRHvR50f-lAZWw_6bjeURdop5N3QxBSpbjuFxvv-Fj8vMEEQKDOTdVotFF-RAuDA_DBGXu8HpjwKCP9o6JEAwPY3SiRnGiRKIP2MKpMZY5VKouQ3fG2yT2YuLGqYFDzOdplKbrgs108u8fgeoQ1QwbFsIJ3S9elHWx3eY-bzRWYFP_ajM_JAsJCFC1r3jPdn80w7TDeoqXRKSqDKh-rLRLnGCVT0bamws4OulIKqvnEUFpIWVaIEbiA72CmKAPti611n-8DKW3T-1FZlHQUE1tt-XkMAGirkXzZUPaULgUYvb97Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siKMJrE3UMsUPWgfI-C7a8uorMQojRi1kCtEDbEIFT93z0oWB6Tn1w1LF2wfynJNNcyggo5bCyzis7QRmGH3DH5P5oper8lcm6fROc0OvNQRGT1iTkB4FbBMqGxGDe_xT3gg-zAzdZcSuItFJ5PAETJcU91Tz8aWif5ScBY6c97g_6R7bbE0WfifkgjzfAnLDnuh4mfRjDlT6J9_41S4z-_HvykPrfJKZbd3lve6QGrRE8F82_ztFgW4PCtJGCyWazlFaHIBId_X2YAOV6-Wa3SDpbrxsL1P3uLHKFmeOe8GvtYLf3sQHzEjWuHz5NXbtlFY-qo6s2k0cuBVJ21iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53c7m7GgZmBbXWpaQOLlI0H_kDoE-8uW9KqO9APisiJEXl_8-flPxG8HzAVpA9yUjRjRaSOhZ816KMOrOx3TH20kGAptOItIND2W8k7vtlxAAebv5oQa5c6IthxbzacJ9PsBliYBffku3P570rW8XgZDwIopLe3fc1d_y9CyYVliafFWSmeNQXfgzszNsLaniWm5ekR0vifnJZp-xhqoNTfQwmInVluBnksOtJCvlh_Z3Jf6cQENh2lUfIrgmi3PQu6udRnxOpUiq6LYdW_8lfv6aKggADXav3R9Q38V890cUVuzNaFW1CqOsHJf9qRQbnYgtmFDhCtlBO7eDfvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM8iVPTsqZA98Fi79nn-01QokNnzJruzx7da6YgvCOP-QuBBhW68toOmt5wchIjG229cO061zK9x6nZfzWj9u15oypokbzc6fXRZP2uALtNcs4l4jz1KLQaG4CgxePWECM8LzTvFuEvw6pVNPe4VcGihyv16BEYzg9KoRRYg3nJMZqng3-UGIWHBvJOcMDN-WtxQH1oi1V8ojtHYy1xJNLo_0_ZhexA9_pu7mcYP1Hz4QJttRGuIqi2bd5pPVYvQACrn-0TKU08TxHcss259lwwrc8T5j60P0x8qQdSq1k7lNfaxaBj1hjNhgQ0nHbbAZC0Ozcuukv97KJvCkcF2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHIj1Nkhvp5MnOLtmuILXjECSJTr23bU10YWqBcIRJGFOkAFfKTi2Qyv2QzIPAFA9IS1S_CPTp0slCLTWlVFl5Z7mIMtvGPUzd3Sf3InLXzx9dv9fAEGXdhwD85fpqjvBRJl1DQXCRkw-qyu7TrC75eoOV1uvsmmApoo5PzsHHv-anqTWEBX-gVFA-4PtXh0GyX2IUmJ7ZB3eB76SSXQNltCNuphBMTVKf9W4OU35uE84rdMJCiZMalKU6V5fsRtHQVbSnWv8BhyhLLXCpeugOHV5lCMS96ywg2PlyFJZm1EHgtelnX1cQw1LPvzwiFVWVSuJGa8HLm2_zzivJCR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS41kz7ioSBK0291U9p1E8YgukCTOnQeajopz4CPRg1ak5PuPY00fFMkzIiV5-6XWKZQ9sDG3FBivBxMCoAev5tiQ7IkmDl95z9fjl-WoPGKt0ZSPvX4X9Pe5XrnyVwS3enzx6TWo_jAplHbswfw8CI2BXts6nQfXUQyD40LLZRq0cB2o9zUhfq_0GsTM0-PLqP_pPOUnczMI0xii8IwT3b5PFtYSRj0Izkme2aMeMiPh9CuiMe7H1j4lx6RQ2ABfBV0aWvxRjbvdWo0ECFNto9fbL5IwkyJx3ORQWhG_TOJfOAdy2O3ji6q8D2QZ8hJpsaUrVFGzrTn7LijdNMmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjW1Ox9FJRHNC-MCzHIwTcHwKKNl2cEnCK9lrPJHrneko-kY1NJ5MQy3Zl8ptU8O5x2JSvsJU9O5pyHcBjF-PK1XDuM5r1afvT6ptCaY3Gnli5AqNfb3I0W2ReHOt2eXhWEGPbPs2pgguZfnTjpFLVcFEhnRjXfNFMep5z0Kfbi5K2nQeidGKAlD6LYgIIYczdgsT0GV3U9qi_1yEK9orNP9P9BQFB_4HiCWS7KBX187JB_1VccE-MLyAOCZ1-eALUEWXo7xFIya3JLWBG2fM5b_16qD87pIf_s_Dqlf3gCO4mALmVIE0tlI695pp9F889PMp3JFzuzSromjp_83fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3dTWrtANiG-dqVQfeDI9eJ_7jEVUfPjWTOOSDoHQJg4quNDWnjOkVPEw5Aei-gn3lcKBb6Cnu4Uof3TlWaTrLAJjVOX1if8aILeIJVDKYJGZb0vfe8L1fGHXIwMEJKG7aLzU3Sty0B7Vv9uGAlmq6suKfdY5DSU3EI4n9b4TRjeDNWEAIWt7jg7H2Ass-Qq4-Oj1jOj6z9khqnR1D06G7HMj1S_TPhILlxhxRFyNg9Hv6L1aKh4ctFX68OXYV-aj9t9FNvwdwe33wKprLVGSA6jLXIWYZnd1lYdf4hiOaWt-mOtK92q7Z3L1qJS6C4LFEHFeQ50A2je-v6I5voSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDMAMWxspcSyEjz6ckOOw-9XzKfFKu-t2ap0XWHAD2T25FbxX6F6hOM7oqF47dbhNo9jM9qOgWJAgPEzgnvT1GXQo4DVCb8iQf-zVvjwTqqmsKScSKIzH-xUSIpCTrpNxzEpFheiH40TDbjHfZZ51JD-10A0ZuAYLhtmtMnHj3DY0U9aWv43oQQvMvwwyt8fICIEJRIGYwBu8JFh-HXUljhiRz1C3nHDpZ6rqDCCZRxYummI5nK5Uy0grl6Cvq6_s6Xcq6ZqXD4vjz_doEqrUGfe02vaB6RPHQFmNEsD08k6ReSuHidREFHyFhIeDldkjsrA655qJROikIqR3nhh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnUPvlwdacl6VwKu_j8o7rZm5I8chbtc5SPWbkEfFA76gjywlPBnoqmxjR3L44hEW4KabdfCGj1N2CvEO_vl5GczUHBSA6Q6EtrAmNj7Xe5r39-zUu6Fk97bdCVcQY63skkRwopHS47BVnZhjqRU4IHO2AsznXcG_icDtk_7n_Opjlh9hWu7gvMtObLEmgSuLWzdFRu0Lej5dCp0lCqi-rTBf4Y82FLCDibWmEeqoo73Z7lbpmW-GrlOPliuuLlGi9tD1lKPMkyzXoLpNY03ox_oqZ8nqGO6JTFqzpuCAXgpZ9rsgv-c8jcyZtt_ed3G2cfEL0uBrfyv4hgtT9UGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peMdUzxsSRgtI35luBy3UR0yzWP_AMCzvHSdmf8IY2XWZpIm16hTKpyT6dtQRjc28h8vJgdxp4aGkQK5kvrEpDha368g9OG-Ypki7oC0pLHTEhAAKWQUJKHW0BrvC2j2ASk4LkL9ZEtPG59v_0yKgxiTwgbwS_4RdZtwD-qyO25hX0KvvHKsXbS9MIbo82blcRXc2OrYXvTylWk5WVsF-QZQVUQH-iIcovNqDZLn3Q1rUQZe97ZisHULQF8dilHdwQT1PAlfXu_Gkkk0FAtmKiCGF4YMdR4PgYTk0nZ0wf0BnjXeJFiVviK3mQWhPipgbJJ42olysXr-J4_ANd_e0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrGIrnhSsFMWKyMTC6TEzv19FrQOzQ5O_N_CF2n0OwEsW-JXNwcYkspxqHHx0QBwlBB0cE5U480BHhxRXj1fsRWywAmJ3r007hEEtJfc6BOAYTIDFmo3zvgCb3UYMQPKX47tyPGBEMXPN0lkL9IFpNcAZGff0wukTPBGoQ6lZvhEMnt3fTAAZeMXtARKxOA5ON_NfYWLAKNxmC-dm1FugVg-Egpqcbt-AECVreSE_l9zFLqpg_rfp2kfGJiBO81J5GkFgmHcXXHo03wZosjWkxcj4tBqsYIadjxyA2_YkmbSo8Ti2vARi4AjB1lc7tWsi-_-zA69-VXDieI4rzID1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJjoQZGD63zZBrAXEVtE7fWXpJHyBcaiNCzbGAiEJZERzO7K-peqaK1tLk5SJuS_jjkoguw2DAQroCCUQwPdGbsxVrRCYxmIG6dJfqbhyVLM0qjFdWiZ8KnK2_j2dxN0Yif4YgAG-3GkuHkdLIdPxemnyMOo7V34eSJjXjF_-LMCI_UVFviGG6Wn_LhgfnfWVIp-i4aEChcrujOITr8BNycTBXiMwE2D8K7NG0YsF-YSw-tJ-D9smRag0dqso0UQ2GmmXy5_77_I0VgIhdGBKizUzQSbgS333PXXz2Hra6ivyfjghNSJyAjxGTCdCvr0ZE9-H8k0dM3h4M1e_OR93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TStD6blRqto4NllFF1Gbkv0WDsGbOCd0Y0NyXwasdpZgcbY2G5PRSb3GR9r82eno2CQsPP9USIglr9hC56TdaWW6L7YBT4lgRC96PvwS5KzLH3acCfyzd4UBXjV0ugcOsdpzqTYa3N0czA-4Qmi_LKeYjd2caqmBhvSgt3e2Zwf_HjGJj6Aj_eecTsADZNI3kLOHUcvp4oaIFc9NmhlwFWkWPHkg0NNyhCF7rDf3aqmrJOvq1RyQorOtuINvtt2ACYZ57e8jNomj0AOcE7bsxbmXfgmo_Q2k6BB_5MSyXds9h0Kk0g4WvNGTPgKiEAsDJrn49fqU3cVhB1-h2AnqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZUdvFH1vDP0B4vUPGuSAyocaug2oanIMmYLehSdRvAwqzeFQ1xNF2ibCAWOt6VKmab0IScWQRu_4b0Cj7Ivl0QIuZQ3nyhX2SCxyebVyu4Mhw_rxP08A3ec0yFBWjOS4kjgkIeCt8GQO_a6HEltob4EeNf3AVaPvzCxqFQQlXkLFK_Qfrk_2WavTqmIUbWee38n2bv_qP03Wz05CcIQGbpXP0Mgp1h7Xd6pMTSA460MmdpzODDeyomhcBfe40w6doP11p2pDx54Co4LTE_u42M0K1Lr9PeC89jIdE-TDqdNS9Jl_ZThCfs9c5mCoUcqR6qYWU6dzS1Xhc1ByOXikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNdq1j52xafLS8v_Ueo6cwHl_53dWavv4GbbnaaKijwVsj38Cbu-lHolFaoCWsKqZUjRKWxNZUDbhoXNMRxm6ze9v0qjV2PUw6tXm7UPES2EjI1VkFPjrOw6e-Nrr2iTcmFQgE5ykMrOm06M2a-prKVqSLmDr7LFR7yJvBZlSPA1JDxNUu5QowMJLpAz7yJG1dgoTlbu31MmY7WIiJW42EpV52HvCM7_Ge-HAOUOekZSdrj9dI98HNvMQGFfCp9vfVpHnoVBGWhxBRviXw12ULS3ptMgk_tyLAhm75yaAQCSgg6CfANvfXYPgUrCxXU4f55dMq0-dmzTtfJZKyZKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=lQx7oL-aeAj8S8dWaRPpu6V0Fzgi927dMfagdFCYDkT1Ee-vlz-X4nXickTj43Jy3kB2hisMo2aIvlRAqRy5TAU9Ixql_CLW_diWw0YMzzGRPDT8vJMy9E_OWP9Rp3Q_aQlmTnk0MBC2M5-u8sclseXKPfQuPVLfDyBMn8gmvtmeHSmbVXYEcOiJwCwq1nTQbTWmyiv0AmNuv5Sw7CL_reezyfCDFM3l2Xzx96t0lzCgTUviZiQ1FWD79zhblS014oSAh_kUTQ3SZFVPnRt-i-86kdCU0bQqy2vHvtDKqE2QiVwc_KhNEARvydKGYspDV7UFkvSVmRqgvCB5gCQQEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=lQx7oL-aeAj8S8dWaRPpu6V0Fzgi927dMfagdFCYDkT1Ee-vlz-X4nXickTj43Jy3kB2hisMo2aIvlRAqRy5TAU9Ixql_CLW_diWw0YMzzGRPDT8vJMy9E_OWP9Rp3Q_aQlmTnk0MBC2M5-u8sclseXKPfQuPVLfDyBMn8gmvtmeHSmbVXYEcOiJwCwq1nTQbTWmyiv0AmNuv5Sw7CL_reezyfCDFM3l2Xzx96t0lzCgTUviZiQ1FWD79zhblS014oSAh_kUTQ3SZFVPnRt-i-86kdCU0bQqy2vHvtDKqE2QiVwc_KhNEARvydKGYspDV7UFkvSVmRqgvCB5gCQQEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLd2xLAWUZ_8GPJhFbZZh8nue-tZ7Sc3ki0A9NpH17R0yhZ5-gheoZj6hivEowsUaHrNd6USg0lhsIPKBA8GoAYdOyK7PjeyXvf_rasvACXABauvwCvFnJ3HlPkqnazmx15Xz3Lm14UjBltodlFGr3IgLMBA2eH-lebissMSv7zbYXCbbfPe6ecfyab_TDJ82tjwisJHjj7FcT0pm3ZeD1crlVXh-g3HikuiYp7wxRq6ibSFpbF-wVKkxrSoVu2vjef8Gk74K0jE20fCNOLjlch3WbW19uXaLe9BbOpb8F9qC_duRD9_vY4C1E36OpgdL6re1Cp25Pu2SiyAuB5Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOLqGq35G2zISCNcWnPt9KfXyTw_RxqAdFRhFLJpfk3a8_nw3O_fvL49wYUu3NWRfmIPLWt6K28HK9cbV5YOhrloJEb_oXzSWoqTA7nMbtVnUvzL7nj5koqnk6LcYuYkSGA9SHDQcixZ22a2eu5F-pKdVs35l54Q03EJGnQZZ7Q5dhVMJ9IiKpF89nvHGMArrrLlVCQYEG2h3JnzFlTuYRccMjMmcbd65ps1OAmTLh7G5LAGdGT_-K6041D-AG5lpsyhS-kCNDW_Kq46cBUnVW4s-ZL8rUhGBVfBKrnSB69hzvqGzHRMpaAWx_gRPFcKvrvMVWeEw4fwWhfbtlpLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=DrBRVw2fRB2fuCXZ0dNGs7nDfxeI7KwaPUZUudRr_u5Unp55RL3XB8waDC7MNaP1OhvJEwdCcQe5fuN5APDhgR5PXO-VqQqMXEL48lFZI0PYaU2NAITyGQfaiW8hk-MrOcm-rXiSiKfO2DmdoR4OG73HuZuVVZAEcJxHGjw4YPZG6xI6nI0QAs6Wq8bD3v6mBTC33AqVaFgSxOl97cD5aB8n-Agq8VU_GsHlLN47pzzIvekCL-XHx51N40Wq05SeRBuDuHSUKaG_RJrYf0dj7etulelGzkb6B756SdDYiIYCW7PIGKRIM-DHtljZwVLDCWEyysVdb18Lu5BP7fnKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=DrBRVw2fRB2fuCXZ0dNGs7nDfxeI7KwaPUZUudRr_u5Unp55RL3XB8waDC7MNaP1OhvJEwdCcQe5fuN5APDhgR5PXO-VqQqMXEL48lFZI0PYaU2NAITyGQfaiW8hk-MrOcm-rXiSiKfO2DmdoR4OG73HuZuVVZAEcJxHGjw4YPZG6xI6nI0QAs6Wq8bD3v6mBTC33AqVaFgSxOl97cD5aB8n-Agq8VU_GsHlLN47pzzIvekCL-XHx51N40Wq05SeRBuDuHSUKaG_RJrYf0dj7etulelGzkb6B756SdDYiIYCW7PIGKRIM-DHtljZwVLDCWEyysVdb18Lu5BP7fnKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvozabrmc7k2v2vObiQ9O8jJXgcPWOCJi05GWXpT9wVrRChdvO4-NHM64g-Y-VtLXzj6GbAdKVzFb2KAYnRNq5taS9zm6RfUsuR3VFNNnwSlngeIbwpSzivx9IV7qFCTPKFagF0YQW8eL8wKpjFARe4xKA1XqANLITs_x3RlNXKmF2ia_PG4h0xrFLaxRkwfHZtsXkCmwaaKEIgEcIRRQS4LT49m1B-hnbQmeTH-Vkcd5C6cM0vbAoBAYK58j53vQL1j_5LEPOIqkFHI4YsTaz9Qx9EctaIdTK_MVMILJAywU_yJ-VW_ZvqrWeo9P9EGfhiya1Z7oyY61tWSMRoLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=OaCjwAgvdNSSQwi06YQhcWI0iJsoCgxaNYBd8o5Lq_K0D4HMQNP1AiM12yIjwRAqDdKh-I9WcfC-ngsP7TMdXLwQqQU7eYm2J0v_85d5xby7hI5rQWFW6UkYJbFDX3on2GYwhQpMS1MTHUDYdwvCY-K8YXAxakDvQxW55gL_8Hd2YeSbyZsIV7qEIhn4M6QWgZ7rXttn2CJmicQvOe9dN7u9nmRpAcmzADndXZBRVjGNork-SjPaF1MhplizOVHj2tnVpY_jaTiogFWRtRUAUvB0_znKwqArpf9ppJw04bgRy2KUeFFUrgGoY-yuaHtQLYXkkNvuW56Xvtin3sOUEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=OaCjwAgvdNSSQwi06YQhcWI0iJsoCgxaNYBd8o5Lq_K0D4HMQNP1AiM12yIjwRAqDdKh-I9WcfC-ngsP7TMdXLwQqQU7eYm2J0v_85d5xby7hI5rQWFW6UkYJbFDX3on2GYwhQpMS1MTHUDYdwvCY-K8YXAxakDvQxW55gL_8Hd2YeSbyZsIV7qEIhn4M6QWgZ7rXttn2CJmicQvOe9dN7u9nmRpAcmzADndXZBRVjGNork-SjPaF1MhplizOVHj2tnVpY_jaTiogFWRtRUAUvB0_znKwqArpf9ppJw04bgRy2KUeFFUrgGoY-yuaHtQLYXkkNvuW56Xvtin3sOUEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e53SDFdiC7Z1W0odpaspMfXPkK_LUlS2sAr6-MdL901_IIouZ1Zns_g7N9ILhtCVmKV-X6U4pylo3JyXZ7irvnZhV9Jw2taKyc0Eyhjqxq6X7V-SLfPpdhLjAyL9UV2QyRrM7ZBD75fRRBMWE-M9MePnRGnLfE7oy0MkM_Rgx1WUUxTBfh2d2ueDvHJDb6Y4MlqbONvXlWliYM-OcoYoKO4MZo_LOhui4PlXUrxHFb-QIZ7DvqOQzS0X8AfN_zNnjBACju4r0mSf4wGMtnfxQpTeXDziMfmRfnrOo0naKigF2jcxW7Xbj-WyV_RbeJvMijFvScCsI8npzozQRGifxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzIia62f-GuvH56v86t9AjEZl4dHTzD4IH2ciDrr4a8qcIFVChPky8yl0NlkWhmywGa7GI9a3Y79PiBwnb7sKVtIfvvLaMy_WNizzEVljvGKpknPd-lDKLKsZbq_aHFrvgOIHAagaBdJrI2wQajqaxRIX5JsfQUoO5NJzH4Ed5-Y6tqYnqaXZRQh3BgMgua5gY8KgpbsXIsR3DuwKGSc8VJ-45cj_WJUfOWo4lx3k1MU9GNSHDr8HoIoEEqHdDHoRL8Vjp3-49YJA3Z0nyvxitouP64x8JBgZ5Y4Cd9-esnOz8mAFrORwGcWHdXQM5xAufni5H5IrK2eXs9rdXnJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR_mRUTRU8hBJ7V4tGxSI2W2CKfPA7ZP369QXmB2ophq_GY-qXvkOfcfaZVhShYFNQPsWs5V9_R78wYLvbKmHEigwyyvSfcFCavwO6CpqhX5CUG8OTj-YMLZxI-A8g0ZjgtFU2sofO-4oc-bgqTgPgTOZv66Ix7Cy0DNkBovADpfTNgeO9Gt6ynIil04HgyfAED_Oy6oCLAey9E5UyEOWnmHI5K-onl7xhzD6UzbMw0JzCDAl1J1NNPsMrZ_olBbF6ZM-vqqkzJNHJRZk1LOZfp4Nc1foT_rdeTF134fpFkw9PXkTkuN6KJDBGFl3T4GF_MLe1MJ4e4G5PGIQYM8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=E3Yk25cFylWsDbhPBTbY_xTOW61v4Sz46b842iwwX_oYSrK0RDx5ktBoCTyVBHG3fUTAhZJpKUdglFDwuCAm9FL3o6-NeNIMV0Ttq8OpvTWarSTehubBgYwdbfVYiy9QOuBxyzKKl89F7PehzSde31YniOsJNmklWv6-1_DRY8awbkw0ybhzieQPqfv43eSLclTFBPnXdwT7shAHWTV-s7HPa3n1K1CaG7Ha13dIjMfCtbBesD-Hf-DpXp4EMQkbK5jMn-7jlOaHtU6tdEaP45WppjiQIUwbpjQb-K50wm_haMciWghgYO0arpc5GUja03FAReoHFIcDD706aqG8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=E3Yk25cFylWsDbhPBTbY_xTOW61v4Sz46b842iwwX_oYSrK0RDx5ktBoCTyVBHG3fUTAhZJpKUdglFDwuCAm9FL3o6-NeNIMV0Ttq8OpvTWarSTehubBgYwdbfVYiy9QOuBxyzKKl89F7PehzSde31YniOsJNmklWv6-1_DRY8awbkw0ybhzieQPqfv43eSLclTFBPnXdwT7shAHWTV-s7HPa3n1K1CaG7Ha13dIjMfCtbBesD-Hf-DpXp4EMQkbK5jMn-7jlOaHtU6tdEaP45WppjiQIUwbpjQb-K50wm_haMciWghgYO0arpc5GUja03FAReoHFIcDD706aqG8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=rS93jt3nUkOUtrJRL9OOoth-eVcbINaxKxAaB169HAd_k2ENznepK1paQ46kAp2gq6ShnYeeF8vHN1v5A1MsNzkvthgLQGhI5aQkNeg4oSv4ej9dlVry9nlon0wVW2m0uT7cnHVcB-mbE0dGGQE4QzTOCJICyPhPatGA_m0yx5EaZ88gaGYXSM8CecRHlnPM6mWUBP5_OBggTEhQrXHCcn2Z8I09O_8LRr0upoKXyXckDOo1P_NYHUAPEmBLt6khkhNXk5lXsAY3WO2IM4XsSqtWAaP-FDYMuHYaWUzYKNfhvX_3xbHFfVInHXPoq2kppZAP_CzNOrskQ8YQKZPo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=rS93jt3nUkOUtrJRL9OOoth-eVcbINaxKxAaB169HAd_k2ENznepK1paQ46kAp2gq6ShnYeeF8vHN1v5A1MsNzkvthgLQGhI5aQkNeg4oSv4ej9dlVry9nlon0wVW2m0uT7cnHVcB-mbE0dGGQE4QzTOCJICyPhPatGA_m0yx5EaZ88gaGYXSM8CecRHlnPM6mWUBP5_OBggTEhQrXHCcn2Z8I09O_8LRr0upoKXyXckDOo1P_NYHUAPEmBLt6khkhNXk5lXsAY3WO2IM4XsSqtWAaP-FDYMuHYaWUzYKNfhvX_3xbHFfVInHXPoq2kppZAP_CzNOrskQ8YQKZPo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=sjuPvG3hV1qqEN164JgUkzAuIGYwBbwTxyYMToGZPjogzY3P819Zhrvw1kbWTMFhSOAUixWxUp_lPYDDWg7h4RvNJ09PxHaOrTEB7UFGZxHbEFLkXa5ePIJIKUY7Pb_cKc7QxxyzL_wrCxSuowEObTiBQyiP8efGEVfRJTAC0JZHeoWC4wvIorl0uvJJEMDsdfXBTqUs-mFawIZPPIM9EveCetd-VJW530qszdqMy8EQNlsxPV3wYbU3zOdyORW9_wSjqVdzuCIkPwfPoCfgdkI__gcRqwWAxNQZwzz5iidTSRGefcL-EuuRGk4jlEjH65c-jXtZaj5iXBoeWss81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=sjuPvG3hV1qqEN164JgUkzAuIGYwBbwTxyYMToGZPjogzY3P819Zhrvw1kbWTMFhSOAUixWxUp_lPYDDWg7h4RvNJ09PxHaOrTEB7UFGZxHbEFLkXa5ePIJIKUY7Pb_cKc7QxxyzL_wrCxSuowEObTiBQyiP8efGEVfRJTAC0JZHeoWC4wvIorl0uvJJEMDsdfXBTqUs-mFawIZPPIM9EveCetd-VJW530qszdqMy8EQNlsxPV3wYbU3zOdyORW9_wSjqVdzuCIkPwfPoCfgdkI__gcRqwWAxNQZwzz5iidTSRGefcL-EuuRGk4jlEjH65c-jXtZaj5iXBoeWss81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpXS1fIEtDXa_i9BAOlINcVgD1HbEhucGQ31I4fgJJbT6Q5cY-UGyNaUmH52GF8wYYZoSC7_qRhVou1FhuXf_U3B2jI0BgXeGFVekyEaCJDabYELi4Mi5bSRJ2D6JQuRw1vLJT2lO-c4WAhNRoQh_xNGQV1uDOUxo3cybZ5ERfX2PupNQow0IBRDKxXv9IgjP_RuXzqls1paYgKxQvy8Stej8I6xu_XqA1iD6w843178moU3MR4zkHgLZESj2Up3i8RDJE0W4a-5FNwH9tm7P7UiM0F6f4RdefQunzTVXjR3cBXvxMQPlaWY4PBBKy_V_wzMihjBZktts2WFmNhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2wr7BNffK3Zqj6YNm0byFFha2dZIKflhG6wg7c0O1PvX8b07UZsWwr7bjDARI67ejgk_F10BX1SI9_3LnQWzm1Be8D1nk0Tus3coUpl9p1djt8dpQq4EPvoo2z4_L0Mi0cMFd00rM48Llfn8dzVIYIoApON8RSnwV3-wd8xeTks8W0v68s9NRX17cnfxCTEDCxmYEN6BH51mee8PCC5uC7JRCabPQVmpWRiwzuagBDqzd920NBKtnv--iFVVQw-iTiBjD3Y8A-7gx2ZUQ0sLNKJ16y15xPlEx0iwYRV27wt4bKq6hbMjUhTHThnXxGzpKSL8dvBpcBFuKcg7XXITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=U0HC-QI2BaBUBE6X3312_vSwjKYeoEGALevJv69LTYw1nCGDejL97kHDP7uLAukVbF4wl6XheBPzXo7S_Xi20siohXZWHQERgQj1UayZIEdX0U8iZgalKgjm0Vv2Pv6s3Z0lgSXxJnzxyx56nPp0uiT5tCCAO31izRpnmb5EtRQWcrEl6sIlFbjYFl8l-rk4IHb6_Th2ccpV98Ygoz_NUFPhwB65YFYO96DaYFTBJNuEi2ibWDJxcDqJtPaclmMVHqeaCEKbb4YlvB4Fw8TtVxJnhqg9Nixd8boDjds3kFQvk-3ZP8E6Dzjgs2zeTvfj-GLcn8i86d7gP8XsB3VwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=U0HC-QI2BaBUBE6X3312_vSwjKYeoEGALevJv69LTYw1nCGDejL97kHDP7uLAukVbF4wl6XheBPzXo7S_Xi20siohXZWHQERgQj1UayZIEdX0U8iZgalKgjm0Vv2Pv6s3Z0lgSXxJnzxyx56nPp0uiT5tCCAO31izRpnmb5EtRQWcrEl6sIlFbjYFl8l-rk4IHb6_Th2ccpV98Ygoz_NUFPhwB65YFYO96DaYFTBJNuEi2ibWDJxcDqJtPaclmMVHqeaCEKbb4YlvB4Fw8TtVxJnhqg9Nixd8boDjds3kFQvk-3ZP8E6Dzjgs2zeTvfj-GLcn8i86d7gP8XsB3VwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpaIu90cNcHyM4YEVKE-VRjzSc63gGe23n91GscDmz9AnX1Ra4-Ww05TayEkSqAjvA3QDl4iTaazghrKF6-637hrRXYaUXCh2OSOOd7rA3ORoGMvZa0JwFZSSxMTogitx-IUqDbPCHlsnLh8lJWl6Dx_GpzV0AI0TfxY8i_8v96cG-MF9TOFewHM1KPzmfgYOnxqHFeOhV2uUP4vKJ578NAorhoMv5VU-1V0YPEDZ30rPpp4Pv8P0mpu7t4y681PowdBUECpAze5sTpC7sAeaVfMbYC9Y7G8KkmxKUrPGLZpwoRL5b3RA3j_56Wyy08iJeWuIs046fCQopo8o1Brng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK0UqYBaet7iBmMTcKqpLJ8VlsS-ih8GUfLLZFadB5seJjdEJBsicOl3BaV5W_yA_GrFUFThrC3yfWFfEfQy1YwZ2WQMre_E292F4oCWnLTbvGMlc1MV7YnA416sjhdLQEOCTpusrk2BgZy4YE7HrEH5pFfkCxrVuHBlWzFcq5YqtNDT0MQg6F5WvxE5uxneQESOm8IVQAfGuM2Ee5dKog8jv3aBK3khYgpQ9fKYJsF0bU2QRP7Nr7HqPNF4GBfTX4pkSM2E-B_RYAsE_OtRh3ZpSU4bYBhIYVam9UWGE1rTFQuwtNzamdChsMOWjeflwfacovE7d2rP5jxJJHK0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=ri2BogB6n4dbRDr2b-8KG5YukX6-DlY3c0B0iu6TTZA5IqD1fOjywEla6mRRGhvu--DZN54YFaLlKr8THL48PGJhVGQmMlKYS8oa77Yb0XS68X3MQ8MWWv_tXNGttCItQ69EPVd0L57ivwhJn5dMQ9_kfpNnK3pKqVCyX2rJCOb8UwTksubwIssUftqzuyxmp8a6izlOB6jFFjib60UTs7D2JUnc_nDB3SQVDEpEhBF6MVqKx4RwYLhKK6YfJUJwN0SJQD8muOkk06YNPjMPn28Vc18ie_5DkdWC-l4p9DTrTuu9iU6q5RhIcW4hlYWV-W1gRw8Lt4lQWX_VBhFYjZ-oYNRqu3Sa7B_GjfnIodcKAbAZHn7i77dFfvWblNGVDHh6GcRhmp8Ti6saJKUgs8FjQ04MI4u6dp9bONPjD5WvMhvZebyUZiar2OELG7i7jL6GB7ZajD50THpZdXQzX_AgiP6zUXL3LuLrQ_ewGLINwx9qBWeUBhxyOPxJsoSpKybIvUaAWxnjChJJWaQ18iBk3-40Z4Dok4vKuS61fYhu4kd7UEKt5Zh1eESw0AdBbUicINZ4RAWIvB13Ie1k9acuXkz5pgoI_HY20nVMIST6p9XJzBofsKlW7nILOXt6nQiV0P6Wd31ZjKgJIeJh22ioKH68sGa-owpM9Q52F_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=ri2BogB6n4dbRDr2b-8KG5YukX6-DlY3c0B0iu6TTZA5IqD1fOjywEla6mRRGhvu--DZN54YFaLlKr8THL48PGJhVGQmMlKYS8oa77Yb0XS68X3MQ8MWWv_tXNGttCItQ69EPVd0L57ivwhJn5dMQ9_kfpNnK3pKqVCyX2rJCOb8UwTksubwIssUftqzuyxmp8a6izlOB6jFFjib60UTs7D2JUnc_nDB3SQVDEpEhBF6MVqKx4RwYLhKK6YfJUJwN0SJQD8muOkk06YNPjMPn28Vc18ie_5DkdWC-l4p9DTrTuu9iU6q5RhIcW4hlYWV-W1gRw8Lt4lQWX_VBhFYjZ-oYNRqu3Sa7B_GjfnIodcKAbAZHn7i77dFfvWblNGVDHh6GcRhmp8Ti6saJKUgs8FjQ04MI4u6dp9bONPjD5WvMhvZebyUZiar2OELG7i7jL6GB7ZajD50THpZdXQzX_AgiP6zUXL3LuLrQ_ewGLINwx9qBWeUBhxyOPxJsoSpKybIvUaAWxnjChJJWaQ18iBk3-40Z4Dok4vKuS61fYhu4kd7UEKt5Zh1eESw0AdBbUicINZ4RAWIvB13Ie1k9acuXkz5pgoI_HY20nVMIST6p9XJzBofsKlW7nILOXt6nQiV0P6Wd31ZjKgJIeJh22ioKH68sGa-owpM9Q52F_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRPO9jnxIM8ehesiotdU8NGHzggBPMujT7URiwjRbGGLSEekidqx6_BsQIw5EK6C2n-adUicya66cuzCO6gWor5jU6RhmNxphtjboFWsX6MWP4O1Xqu7OsBKH6xTKRvbSFFNsqOpCmF3tBecWLg4armR_cTw3QJlPT_U6oO-Pb1ETOxwZdN4gWFC09JUK4Rom7xXrTVo604Ihu-8L3XBdaVgHi4BnPX9vo074vN-36GwiVFQWY44wAxrjpvbRgWooBxzq-n8gbvvgXRLgqV9HOhutgdcNlL9RCQ1kuPUbn079Pma15tNhtOMtB52NLR0OTcG3y5zp5QDosOfUxrAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLGDI-am1FerTIeA9AbAuUH4NOGUCrUhJE90BADo_eQXAVvFVB4x14LNMnQop1oMPHKTa43B_0K0rYZAreEUeW1sj6tRS0hX6Vuh92JuwqBj7XgZNi2lDQKlWCW8-jqLo_ouODPVrEEPL_JLjyZdHcqDyat6Cuc3PFajwuL2AglivJzh8rNqEwV0qtWVphI3yvVOrC4PzvtGUrO5kwAvMHtt9DQ2N4FmxEWOjdvciyejdxm3e4eeMhFzD9N-zOnIDofpYsrvKmEE7Ly885cOtzZYgrv0ykRjml13LNUPhg8x7wRvl0bVpq-i02v0KsAAqCpeDzb4Pv3bqBaGqHbEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Pdk94K78VqROs8XS5y3_pSCQ30hx3yfXdUBX58Kfel_V0_zK-Sy_6oNa1ANVyCExIOKklCaWlDJp1w6u2hUR0CQgtH8O61TjVy43-hGdud_VQxZ3uV3lqKYmWlqpbqnWcGLKd-vauZRgzvDxjG3Rp-403fWLOaD8ylBK78y5UkeYeJ7FB2EUdn7HSjj1Frk-BMartW1xXJmJ0mGr9JxqXBYff4MJL-OXDj3c5ty2jLfFDrjv-Oj6RHkAOXfh4XrNAAProEcmUTjirVHa7uE_VtnzVYFbMtmuKSvgDSMtzeV-NzPIBRrwBpUk-CuhLUaAcTJ6VPnB72gOsF_m_LOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=ETjkPvea2KFbmuw-5nNPMqeNFq0_qbMSjQdwkrGJl7eq9GdwCEsWSdGtRnnerMlIGXCxd2RTksqFQxejVbVx72FBcUzBr-bplolwaKgJ1QuRljw8RhA206YgmVcotcj9Hpf1CcmZrZ4P6VCGGpV948ZnMPDel65-5VjTRbQSwHF8M3s4kRYAkfyvlNFI5Otxf3D7XpEA82258VSb0O1RlwO6X-hZdPpP2DUuvFOKYQd__7UTcsnKxjpnQDBYDHXaEtI6ag_TQbnBprCa_sTBz4TQdG2isJn82M-gjxsL94vlwtNdnZBLyNt2OysAkULUHlQ1X2Xzjy9VBIaZPZvLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=ETjkPvea2KFbmuw-5nNPMqeNFq0_qbMSjQdwkrGJl7eq9GdwCEsWSdGtRnnerMlIGXCxd2RTksqFQxejVbVx72FBcUzBr-bplolwaKgJ1QuRljw8RhA206YgmVcotcj9Hpf1CcmZrZ4P6VCGGpV948ZnMPDel65-5VjTRbQSwHF8M3s4kRYAkfyvlNFI5Otxf3D7XpEA82258VSb0O1RlwO6X-hZdPpP2DUuvFOKYQd__7UTcsnKxjpnQDBYDHXaEtI6ag_TQbnBprCa_sTBz4TQdG2isJn82M-gjxsL94vlwtNdnZBLyNt2OysAkULUHlQ1X2Xzjy9VBIaZPZvLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=VLnk0CL-2BblANp0FidFNw9C0LgahwZ3M6ZuIL8zmxbf7DjrD4-nDKeKhtm94Y3iljHh4JJ6P0J70zDSQV5mWDWazQyFiEoqd9O9qqOQu5H0mh8k9waZNUCHPRS1825_FrmsnVVKumKiChcf2BajzlR7qJgm7rMlvgTPiNcCP7yxAnhvvJSjgx-tGXZas0QZSpkp0c4r6briwgc6Cwtxn2Nfubgf0dZWgHi5-R2e3VFoZSKXsdoL4Ofy2e2Xe9kb5FaRISdMjDXzZQRfpnaKYeHlq4VlfveKogMKHC9t16HNf89RRxuMEgTQ4ASdoZMgy57-iXUjD-FmzaFa4Fp27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=VLnk0CL-2BblANp0FidFNw9C0LgahwZ3M6ZuIL8zmxbf7DjrD4-nDKeKhtm94Y3iljHh4JJ6P0J70zDSQV5mWDWazQyFiEoqd9O9qqOQu5H0mh8k9waZNUCHPRS1825_FrmsnVVKumKiChcf2BajzlR7qJgm7rMlvgTPiNcCP7yxAnhvvJSjgx-tGXZas0QZSpkp0c4r6briwgc6Cwtxn2Nfubgf0dZWgHi5-R2e3VFoZSKXsdoL4Ofy2e2Xe9kb5FaRISdMjDXzZQRfpnaKYeHlq4VlfveKogMKHC9t16HNf89RRxuMEgTQ4ASdoZMgy57-iXUjD-FmzaFa4Fp27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amBBeFaquxzYt0ilAL7f2zmM9UWQTJHy0Ja5iwIKgDJu0MgvMYRF9oU6oiCpE84rQ5UpCKo3jbY6MTDa3nrGFuB7QUyS3YGc8Hr3aYkMRTWtPM11BPzNQc0xl0bpW6-K6_PyisL2krhOHRfOBzTLb3eykKyqtRFRiwZZyUw_Mwun1qdI0_D9VHWkA7E8r8B1MxCWc-vTapfoAaHvyb1y8yX-NkHoMOmybR1Sjg_6a14SuxAdw4cCO7ZEcfLLSqbaIdJrQsrHkzI6_3-n1dEyKFcbNMenzveLjLAXK6MNp_pz7KmjcEy7wjaYoeiTmIlxwQBANf7hiRaVn4W0NBVZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOUFZSKjZlikQfHd8RzYK82t3lqQCUZPSMB9iGTRlIdd7uCNu2JUHNWHgWTFy9jfN5HIWBfRxjAivxwyUgG-zvZD9rGuzoUZi3XcqNmAL_6efDazQllK3Unq8R6z9VPY4HYD0M_f90lh1QPOBX4C8OqwWk91XY3xMlWuPHIPeScmyxIaLhB-0CfArvm99bBEG69qKzGxWXIrQCvzFagtiJPXo18YM_rbKNwmQ3_S6xhDyON7s_vg9HGf-HzayGrEwQyzZow1VeRM_2_XELGmRBoReq1nA7H1qJoukk9J93hmJ5IwoS4r9JS1KWhJpduW76a0OpvD1oE_r88fF0FrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SonF0-RIt1rB5s37jDRZj7MS5jR6co4VkBjjV904XesJ72jkWsyHN6hei-iHJ2yF9KKrzA0w5o5NNR-_muwcB9qvmlvIyEid1QFOn8ZfxuxK4QtoiIfNN-iELMy1nFXjvOa805GHJiHvAAIcg4-H8jjxT9QGJ8Rduwj43ZtPCxFFOZGZnq7pan-v73_czB_hQUhpDZRxLB_DfEy7DZU2V5SYsk1XA-fgCUXX_rK-4LcCD9QiaaI4wo8Qfe9eTlxa6LO5CKlgIEOplt-0K4pjSPndaIObp5wNRFwS0G38Wrk3R7SbsgNCM4FWIME70Qr-LFxPnnO3e9GpFjY-Jig1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWmVc7g_HYOTU-PASs9t-bbTsyNiFF0rdIpn_GN-cu-csnZqp982rSO20wFY_SrWLBkW8UXxlPx41yGhURT90eur1x6JxrfGLa1aptz7usgY32ihxyKtqLz0CuAWlmCkpJTDa2e4rq6aAroSG5EggeJ9eIgzPYfpunAz4HPqWuG3r3qVtL9K6-yU82Tqh-e4s5rmOJAK8-T6EIc8Csa0uKBKB-I3ti2iv5EZJxBeD7bX8dDiwejINGDV1JgPdCP-U0ogana9n1-EBCZtQRZPrUf-Q0iiENvYaSzwq6iFNtoXGxqT3I7nPMwbZHy5A8f-cZYVrmioQZPmsCc9eo1eCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj85gTjlBx3Rosv4cFVUTvaReFePIiHbjgZ43e2Chh9uHl-hpmQIk9Ad5rU-CzPqQlwNrSo7ipRoWla8EjRj88ULe2m1TTUa-z22NluPWtQZOJLRiHFOcMPq9vl6uO0VIwo1mlohfKSHSAZMIQgU5vQZd2hzTKJd6KI6yfSXSva2JPkZ4L0FSrdIOrnaIcqlnm8SsdzOHZuTJCGxlz0zlPCqKxrp8lcPSPzvjqTyKlYYfgmyTCFVURNoOUDzo8yi7D5YMZ_KxGqDQfxtKerc3qzdaA9nlhIlE-8Vv9TPrYcPPzXOsK37zZdZ3asltUabU__oZHGHdI5iLMclam9C1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=SziK2gSoxa7um1V-BBMRIIb0sT1aLBSHpcAF82WYhktUoCL3J7c7u1AkXMl5flseMX4zREniwnuGjj7kCF-oSGMkx-V6zHFBM7lZjUBtDEeJCgpFLu-lTiyEe41ap_y31HYY59Km5A2o-aas8_WzycM9GThqt_oMvY4SblpNOCb7rqKI81pZZUQyRGtbteYz7djSMOjZrtmc7ZTEuzOnmK06tsdSkJUoUxA8b-em4OuETRg2ActW83NeKpBG3R7CJ1lTxdHSQAuIH2a_TcVc3PrefNjyALI2W7d0GpaNfx-x6UDchaLJSGhgH7S7p37dFKTrzKPPO6oVn8b-Iu89pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=SziK2gSoxa7um1V-BBMRIIb0sT1aLBSHpcAF82WYhktUoCL3J7c7u1AkXMl5flseMX4zREniwnuGjj7kCF-oSGMkx-V6zHFBM7lZjUBtDEeJCgpFLu-lTiyEe41ap_y31HYY59Km5A2o-aas8_WzycM9GThqt_oMvY4SblpNOCb7rqKI81pZZUQyRGtbteYz7djSMOjZrtmc7ZTEuzOnmK06tsdSkJUoUxA8b-em4OuETRg2ActW83NeKpBG3R7CJ1lTxdHSQAuIH2a_TcVc3PrefNjyALI2W7d0GpaNfx-x6UDchaLJSGhgH7S7p37dFKTrzKPPO6oVn8b-Iu89pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=kR2fKWlBve33QQ82wW9shbkk5zm6UG155FjbjqmXexgPC6dq-Vytfb8qaPbmkWeIp7MwWuIwDEOJPvOM7v_y8jxGRRf9VSeCL8lLDLIQHn-V_NJmBiZHwivOb9Xz2UIjaZhIEJO_pWnOylnAPkySQ1XEKXhUcIremHznxRKl7TdUFWN3GNBCfPVXe7HJfaPj2GxpWSPVS13gT8wRLDOcI9mTYm_NDbytep-p9mn-4URDLuoGxMKD3_XWkMaesJLLWCtoEVvE9CBa02_Ve-tHKJ_GREKnZ_FBmFWElcpm18wSwj8Un6cKx7gFqh4izhFr6ywzDOZiVQtWgBaiuPxc3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=kR2fKWlBve33QQ82wW9shbkk5zm6UG155FjbjqmXexgPC6dq-Vytfb8qaPbmkWeIp7MwWuIwDEOJPvOM7v_y8jxGRRf9VSeCL8lLDLIQHn-V_NJmBiZHwivOb9Xz2UIjaZhIEJO_pWnOylnAPkySQ1XEKXhUcIremHznxRKl7TdUFWN3GNBCfPVXe7HJfaPj2GxpWSPVS13gT8wRLDOcI9mTYm_NDbytep-p9mn-4URDLuoGxMKD3_XWkMaesJLLWCtoEVvE9CBa02_Ve-tHKJ_GREKnZ_FBmFWElcpm18wSwj8Un6cKx7gFqh4izhFr6ywzDOZiVQtWgBaiuPxc3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSLpuDfpy2ZoxPLxhA-lP2dJV4XHWvEXOEzB6zrNyMVSIdypVlPsAw4lNQKBhgsxueriq7_E-RyMgL_je62vxBE56ez3XhEgKWR5b--_xWRonBENdHyOnINNu0cjdBb5jTtsuXATjkxQXhRe8-nauRihn9K7IscqFYaN5UQGq2GT83-hALz7i2f6Sn2BG6749pNGTJ0hm0QpOqsCIMhNXdifaV_-6C6eIuG-7ASOfT_bMeHkXbHYUsrgzZYr2EAePtaLtoH0Ml2t9ZbAl7Fqieid6h2CQ3pSzBSJJBgZ6V6AUdV3gWmIyiP-6_77TjMOrzpw763kEyD2Z8MUY-7z1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMKZ455Yx_IR-7Ys0PFUI7lbZ2SQdu3QC-YJsdzFvHkMgu47EV-fr2K1QuvmuGIePKNMxvPr1LR6RhmPWLQRiSGbAujkkSy0tqQmgEGF1LgOUftksfWnTPd18_H59_nf4vV3VGa80f8U3Yu2sJQyL09dGnEmKjcvpzToIsyVbkP_H-o-iaHlW0t7PC_Z6XoohA4ksjcPLfeVwRzloeCR8_WuZWNowJelG6C38XHwanxUOEHkqoSIUjV1eCnCB0XOkeLRlllRnr2guuMR7gu23KyjhKuxK3ohbI04amtHqQTtTVE5RGSUorU7qTQAn7OlflJ6eRn-ZTSYU8jwtUDvAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWVuVGNcSs0J3dkMIrng5zIbHk3RtC06fdGL37r3pMnRXVFYGl4_vZrSXrPSGgX580kZ73lu3GRqi-mXSDbmwSL4YPVkW6HtXAoRyPHUrau1INX3GaFI310e6EJb7fTPg-xr2v0aurlqmaIYMF4Y4n2rOQmKrdEOZCyoJ_Ko1m-88CUw5WpwV-CXETpLYpkJEYDPSDtihYHm52XQyuv3ROFzfdq8bCMAQifYEGgf3a6yZTHT8ydQBJlk62Xruce8eOGX34Lg-4oLJeIEvTM9NdAI6kDAEU_mfIEzTiLZw4petUL8V30wT-rX1TttVAUYulKz_IBIW89w2B9D7Dp8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvADHkRGp6OyTzZMFJQZv5YNvKk3-RLfgWEcoG99X3EAqF-HG2abyoIdvC-nSnTqVrkI_CX6cWjfd2ICYj2QwAu9pKddWIkiziPHap4kkvqHEqBKD3g_DHZ-944NgdZ_b0I0drcU0fMuPFAKSCATaXyDbPyxHuiCNjJvK34CAfN7Wfw9nP3iUgXTW74eNluxGkKkGWDHcZO5dLp4QTZ7jcwlmdgdxRj6J7R_mXu9XQFe_2yCIkgZbX5FUYkhpkUclL0SuSI7k3T8_OtSVs58AgdyIYIbX2irdza7f-Ewzzxxs0vG0Mcn5iVRarts0S2RnAc57UP1N4euPNtmZlTjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNK2Qgu-PiWo6JvAEM9lxtCWEKfALNeL0ilIkiyn-jkTaumdhVMpBcdHsQLcBnSrMzGGpp533DX6WB2zUiNyS3cXm7xEcW8nf_ZhjlCgUjtjOyqOvkSjCle_ZuHSrs712s7xZyOM-1frfs0MEmKKUKVWgIc6zGsvzAk7OSHuls5-XPA48LtzeUvCurLUHtN0LZpikr_GVJXNEqFAsLPdmd_7f4_uqIAN4QzDuSfImTUHxkg0zWa9T0B6yP3uoW8vifvrxlEShBVR2W0iGokmTWYMK2sw0pSag_qJqCCWAtStveuT0wKsLyCrD-MWjTJBnEHWyKlS1t8v1_q8IqQjcyd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNK2Qgu-PiWo6JvAEM9lxtCWEKfALNeL0ilIkiyn-jkTaumdhVMpBcdHsQLcBnSrMzGGpp533DX6WB2zUiNyS3cXm7xEcW8nf_ZhjlCgUjtjOyqOvkSjCle_ZuHSrs712s7xZyOM-1frfs0MEmKKUKVWgIc6zGsvzAk7OSHuls5-XPA48LtzeUvCurLUHtN0LZpikr_GVJXNEqFAsLPdmd_7f4_uqIAN4QzDuSfImTUHxkg0zWa9T0B6yP3uoW8vifvrxlEShBVR2W0iGokmTWYMK2sw0pSag_qJqCCWAtStveuT0wKsLyCrD-MWjTJBnEHWyKlS1t8v1_q8IqQjcyd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhBhiBpTTqbE-2KkZKD-w8edFpzjZDyN4vgQm21rDMEipV6u1Erz4yJrT_kJzfvBjVpQyyI9u1LAxjyS9kPmYEOf_QFkytGV6HyWWvgNTvjqQIFn9SKhQfeyn8KY3hHqqzT33GgkrJZsSvaP8sr5NgpRQR1yIXcUaocUnsIaIyDpS58RGF66vIphwvdUo2TDYVo22FJVCQHX3Wm-zp2_TMi18otLHYANpUlr3cwn9gWCAE93ZLdXST5AlZvNOLVlIBxsLKzcxS8VTA9CU3taFtYcfwC7S6816j_7CusnUc_J7OGzuoxfxxGYWqxNhnFYSBiG-cyESbY8dJcB9WCGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQKeslw0KgSwZV-lgaIecw8z5SPeBdmrNQgdVcDBjEXS5ngMDm_Ls4aIvaS3drRRN572-Xrr73yYZIYqBU4rCruty_BGmRObP4uFrdfhwiXPszMOuq_T-1fQafy2yEGq1wTnp1OfcI1e2g59vRvWgT88VZDWv7tsuLGAnkSItkniGg3psn9LLaCFTslNJ2kqJ0HQ3zhhe5Ki9sP2XbwVhwIis84VvRnuatPQr52Fcj_DPIzRf5zOZ-h3AbQ768j4_jJteEsVNALV8JjKBzBOgsQdSUMG8cFg1G_nu1-OkA8wqdMx38Qrr7EQOrDqqssEeerZ9_MTHbzdEl4UH00n4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9NovtNBUGASQcAGrPHthg5FdqmrpDlYjN3tNh8rxtlGi_Or7KmSAA9YMdyV97r4Ua2Ndz_ptz71CXwL_PLpNBoo1w0xbkz68mkzUIMUc8qxiig685OSLXQJVR2rRHL4t7OatsMRA0bs4-96hwXggrDzGfEwQca1sd4SH_UqX95E-SmZ6qaO8cn3Sl1NU1zG2ImdyWjW_qgp-WnV2yaLHRaZOcCWtT_ITfiKLd_CLo2dnuYRQ0Su_JzSzylN0mRYUzrLK0BA92m9IVtRtOHNzErvPn6YsgTq93ryFXPRmid2ItPNKxltqSn2R9CVM1j7D9eXKC7cj2WPivrw9inUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA52PNu7E05uP7jTUmCl164yOAQN8AozB3hwNNeaBgTH4LSXdZf1aWCatVuXQ-XB9jCLl6BnST9I56QZdShpRXY99VQeozyh4Kg1fVYPqqpDITX6KYKNv0CJSu2GhZfHDna2t8OQ33DdWIZmB6J0DPwuWWVS5bkfp-IwpLNsCL5pUUUrI-Vbrlv0coOOv5OBn2-mcoO0n4CmvP8j9qOFGDUj8A3kXtg8azjTLyVjX-qbYmSDcoX899dpBB_IdzYJXDOj2-xz94QAZilp7mRou8GajtWUad7Dhb-_oitHItQeG5itqPMKPQi6asON-J3unlQ5M_KXPEZoHldQcRIspA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=EsJjCQSLKtJduR_oovhoxEmI-iOHpQ0m7FeS6yOoSdDDC6Fa_O4_Gv9Ek7rFHI4YPLPQ4CCzduP9R2bPFCqrSJbAV0C5Fhooa5Ww-5RgmPM6ZL71k5RDKpfFC5RSusKM9ppL2frNTXZIvLumgdmd0CaidR6-DcDidJF6Dk5XUKL4403AR8AL72XHlReJymAqvfyd5XgjVZroxljLOCOh56vwMVHLHieGfeZo6JomhYopLyxWdMORbKDuAmFAjCKyZAbRvlQ5l48OmxpeidNfe14Ni6Qfrg1MVi9WkSDswIjUIzB_n9Q3S_HurYiPXOo65VzmmH0Eg8kQLnJ6kgD43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=EsJjCQSLKtJduR_oovhoxEmI-iOHpQ0m7FeS6yOoSdDDC6Fa_O4_Gv9Ek7rFHI4YPLPQ4CCzduP9R2bPFCqrSJbAV0C5Fhooa5Ww-5RgmPM6ZL71k5RDKpfFC5RSusKM9ppL2frNTXZIvLumgdmd0CaidR6-DcDidJF6Dk5XUKL4403AR8AL72XHlReJymAqvfyd5XgjVZroxljLOCOh56vwMVHLHieGfeZo6JomhYopLyxWdMORbKDuAmFAjCKyZAbRvlQ5l48OmxpeidNfe14Ni6Qfrg1MVi9WkSDswIjUIzB_n9Q3S_HurYiPXOo65VzmmH0Eg8kQLnJ6kgD43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqCCcMSHrjTANXRBBeT6cRrGb9Uw-o1-kQmKELaUup9Jfw-qeLzZKO4PtO48eXglzbJZFZL32TYl7GyfUnhM502gkJZ2JrTbN1lvNh4NF3PybJGrMFqO_odD2hfLfOhicmmwmlJNabQtVq0TOIcYQzmMQRZqdhF-WKrBlxJZg-K5T1c32-8Z4E_WxgJP-nCJgFMov8aEMEIW6FRn42O1bTqYgEgnsQF_HpMuEg-vkRQU7n-2pP7dmya5lMUPZxoHiytU286sg0ftcn0LOYdG6G7kQe-L9jqhU-rbTQq18kC6Qi3d--cOBR5FLdyyREiTYPiDV-AmdcRpfd_O7jSZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=AXvh_XD8PI9u8XTm9F6Gsq-OoF0cRq3VRByx49GO_j5SS8xmYw9MnNdY7lKnuz9pAAShmJ3_Sj__T_45jcb-RyOjddNhEy8AqAkcwCu_C5BcOszQGd65NMk14QF8FGRYBmZrRVNVQwVPdueX7gYbll12ar74o_EZnbn4SMVKw1vs9826HN0bdNFVjFqWgGe9ZrWeo-kbLQwJRou-0G7GqPpwguWgBYqjj4x1UNkPhw9-e4Jwpr7VLlbmciHA0jSZk8g2GM2VZwZ4Bo5wWp2lv-xNk9ELRUbZfaAY7A1n8G4-zJkn6WZWtR3c8BvLeDULySKEvW6CSOChoDJPcuoL4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=AXvh_XD8PI9u8XTm9F6Gsq-OoF0cRq3VRByx49GO_j5SS8xmYw9MnNdY7lKnuz9pAAShmJ3_Sj__T_45jcb-RyOjddNhEy8AqAkcwCu_C5BcOszQGd65NMk14QF8FGRYBmZrRVNVQwVPdueX7gYbll12ar74o_EZnbn4SMVKw1vs9826HN0bdNFVjFqWgGe9ZrWeo-kbLQwJRou-0G7GqPpwguWgBYqjj4x1UNkPhw9-e4Jwpr7VLlbmciHA0jSZk8g2GM2VZwZ4Bo5wWp2lv-xNk9ELRUbZfaAY7A1n8G4-zJkn6WZWtR3c8BvLeDULySKEvW6CSOChoDJPcuoL4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbT7rg31xjz8QnIXqsRHKZE5xsXLKLB7mXZ1IqQtV5xHOinW_TSFCR5eb9MzUfQh72hwAbMhQ0RRN1496eJscmI_GLMSVhYdtDo00DpK5n-epuOyR2SKw7u-oY8aiTpioIyNoA1CQv6NP58vH4kcK4Lwz-6Q772k1vKNgMJahJJpRKMMVdiNNNQjwGnuRLBcwojC4n9d4vXwpf76Dgs6bIQEzebw-Rx53dwD5L9sOLY-bjwA0_1ul8AwPEQgLr5XRWI1w70e3sxjEe4ynAYDkNiGU5SIY-JT20L6RLKQSBM4l8XEAXpGeti48eCr4DUlYAGjY7F7vpRDyVHMBISjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgHPrJ04FEIOpNiuMzBXjVqfiJWxAl0aMjbqjv8WR_Mr-xoLokTkg4-P8twFFRTZF7rOPyDBiolcnN3Xg10-SpUAK3kMcAio0UTZmYHIMQbN19h_waN7EQmxn4Mhj63MZZAN-Dp7Gc7KB1PCfpdju4pM4OvQAlGyUhZw-U8-aeavWiA1wHNh9quKIFU-2SGUIMQoD_mMp2D0Pnv7mt6Yu9DU2pWdYn8q-h_wZ5wxvBNNRsy1HJ5QS1wQTu63Fnv9Xj26gcgAVkZ1teey_Hscf6BlQzlnMmhM7-mOwlfLd00y9p7GEbof4QaU4ZQIb9gnUOVFeQ27Q0cDl6ko0lazqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpC_dzECUJiH7ikKTtW5haAB5P4G7VVvR5dtP1K3Hvxr2GYRH5pXbetoxxcX99mZWv03nCcq3q8nyQk7qkJetJvw-Uj2ywgCSrPBOlNKdrZIdbEXPS_8XDh7-aYhfi2cCBPEHuSHS76LcbHxjYHDChtWOAnPlQukWmkshEptLBztOJ3yMxrdmBvkVcINjWsE9xOc0TCkKs6jP056bDy5ac4I3zy80rq2QHp6Yk5BXkiSIrd8EmWKPVmGGwYlVZztVpzW7J3c_bRkt8-R9pYZAhtWqweAZy4cpJrowFop7WezTqmeYhXW1B_KMUKuIzLRLAAS3Rwm0mwIZrlnhz9CZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqv5SIM98lEhlPZ7Yw-iVsN_O3-OGb-WrIqfybTKnIumzrKMUC-BU1xZqeetwAojwlGz-8TQC6egkcs53xMwGTAzYNnPL9mreXmXLqKvSgF1G2Eez8LQesdn9Q4wpQSvFcg5jq9NT21FZpRdQPGkIBdtqgGc0aC9m2_DAPkOzXhelhKL4aWT_t3vEcntpyNUIkiMMZl_ByYe0MPcfmY46t7G0Lbf_nevqUF4dEnEz6Vj_edAlFEvmjH47EuAXA-HwQY5JalfW-kR_Q9A3GHcRTb7GRU6e4bjE-rMydXTYPG5EWw5yG4VLbkHBUE9XYiRQDkOmVdL1BqQhwHdosFEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKYxhdLIgl9u2bx8vkC-j8ZST14eGZHLcSzLP2tZpQgRmDqKdmhLBsa0hylrXBeNPEUfTbvuNwcUIrfhzMgxv3tuBTamFiEOua0BFH84EmgaMzynOBsOUQkEF5QTvHbQMKDySr4HPyvT_4FZqbW7TR1xhKgz-m5BYC3vWj0uZsAFgnUuzecDMDys_Zvjur3HEiqckYfB9yJ12qK8kp8Ka1DPRTGkseDuEVXMU1ivUsCMWVe90mnBwckL3o6oxYgKy9HlM3757a55NLCVdNviehp7FMMDPW41ccQuA56vl8nCzY8S3noY5oD7GXydUlkylGRO4Qb63qVubBx-Hi3DhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
