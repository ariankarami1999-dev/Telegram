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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaErQR-wB2DRuJllxriBNRKOPNuBey_IohJH0hR79EXp2ib45FkzY0L3T3Oke2KcDc49EFkOD52lPEaGnl7myBghyIHrjFtU2JUgrIJXniSfUhleBFxO1cZuXzjO5e9k2gio3lBxlHKk-dZgKy-P-exwIgz5mjp2ydZvw2q8MsuyNGymm-SUcPYo4ldAlcEnwVCGIjSYQ65GRc7ItxE0Tcb_xxOpndn5cFugevthTeikn_-jy0s7LI6zNAdvD7fln-gSO8Ki7Br_dns9RC2iejcnjBS7K9bwBD644MUlzi2kzemA2o9ch2wumGNCPiYn4rTbA8-S3yJA9bNxv_qvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_vmA6PrJ286NKfC47fTG9ulDrBXjRkvupbfKcGGTBJ5sYtN5LXvtzuEBNPKhlDFQb60BV5sMW2pUTPUzEnZoR9vdVnQAITKUm6Ac7Te2GiCYuZhXMQFVPAHTefpGGGDr_n3udU7xSEN7L-LnqrRoFFpXUO29i0Oa2IJRiiS1cESw1jgm0z4uzZ9Hd6pldQXCH-J5KhCKVJnOoMtCngqGiUzQA0pH4cec9kOWoNw5UHdUrjFXqbUpB31Xaa-ysSXpttlLlCSuwLOC9i4EQZoXRm4IlYbEF3iy57OadrDjZxTLQmfB33wHzKtQbFU6OLthxClEwzKNen-DW7_UU8Kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8-IdXEqDqfydr9zLTrtVXJP6w4j8U6SDvUFGScO-FnUbQJ_k1QllGvlOx2eHVld9ww-pMAAIM7DReFngMh5fNKkZZQzTpRXUQrwFJFufE1GgYhq0Ofa4_O4Q5LA_9rYkHQKfDuRIAp4hLy0xgMBp6vOfx1dvxpNMSVmTQGg4Ku5ZAhf8Nnznh8ZYvlms0bKOKqQiLUBeHfQsoeazKsJtjSFxRYAAwOI-HVnr9tdRz9fuKHGjq4AalEarQhBo0rN_U8vNZn0ZDMbKpDslfmKi7txHWA2dzKpF-WKom15QvP-URpcik9MBlRz_H__QhVGmNhadHnrO3g6oijahUk_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYsLswt4nM5g3Rorvg3vjroXa5XUE_310JbupsidKVwrWbD3Hr5nRSZOCuUMI3rKxakJdTtraSADSft57uyPbW1DNjWzS5NwdCvP0TkNN2l2E7cJmaRXuyzser7svK5hUGnvtW6yQHh1Xw6JuZTIcRQyLRN7QpI-F6b3_GwrMwQW7FTCs9ATzGhZm1bhBSgJGq5hWBEDJMbEvH1_UiBJ9rKfqjESpXo-ugY_bS64v_fRsvk7rB7v2x5QXXQSLP-1YbCGPbYBZQkZW-43GoGsK9Si-M5A4t5_pDRJH7CrzofbFYKA-fMzEQitnMWg9HAru47V-3ZdFeJhp-LRs0sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7eJZIkrsDNBhzLFRcHiwxwmyGycsNPqKfKGUUo2XiNr0gYtCRP9Zl1R7LMWV87U1B9VSZEJWNGYz7BI84Hx-yg6j8d67GmQ1avWMJJykUnfZK_7a3neZVMHDyWsfZn9idjNOrDhJ-K6B8IXtk3sKLU3rHliZC10qBpiK_Q6QlI5q06UxtOKOrOzcmSosb5qKmcHPElOtMn9_kDnYrjr6CWGcHFuSwaGoIvSFUsXSE7REC68dGEYvmmajy0AVn7dkKiqVugmfGYxIdn-IlEQYvqqzgMxYZh7QDx6aLP5tzOHnuBaum6-Y-moIvOtnclTTAz7DuCcgx1oa0mna1aaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLWWa1ZrGx1ZtBYn_Cc3zKTmdTt5dN0VE46u_eHkn9jxc--XrHvvwpsUSiSyQmMJ00D70rNGYyA_3J7VeGN5FLjhP8ug5hC6Ld-SEIxzsv9UlYD0QdegwCrfDbKbEeTBvKGhQHHQ4WNlEsKISAw1ngIrfm__V1JsVzaxSxLkfDZ_8yvdtWnlj3hXo4fWGgwE2cSuz3RLBf4eM4O1lmprioKouc3E0l-LpsAGdn--fxi14WhmndWEm0k4HE8ptF1p8Dgl8tZ2zgxdoHOhqcjQ91h1uimlVg4zBGAbRU40Up8UXbn8-bsCutJPOiazqRznuoWEakQ_mISQUT8pgrLquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuONBInsU742iA8ghGUvcgmJnCPOkXJZ9p-Y0X2UvLw-SCXS3OMyhPG-RtpgeSftbi9DDUEdQcdhjFv3ob6svpV8EpZZgLZHrHkN1Xfa2yH2Zt1gSONJZWDeADJAaWIRm6mzWI3h_SGgSjr3JcTrVWcqW4iEZkeqj18G6F0uCn5W8-4RDWsZS4wNe5rK9kRFA4A-E96jcVynDkV0OKi9L24JM2-hac5McPKjhmiqevcZlNGYfDjRok6oodXGzoXeHM26WANh_0RDQBb5e9_eU826sjmZu5cfXDV6Y2DDUuqxBoKb2rWXZcW2kszf6nLpyA8OougLdG0mmxKjD9RJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYgZx5nP34gq23xcuVNjLWhFcPV7cytFjPNVut6FeqanMZKDVbGWCH93LmOZDmhLazI0hsXXN1YYW0e5mhTo_58WlHcSN57NMkXIY31Aen2bYf5UZ5K6zS8VolB0WjJukwsj1iFGyLVKxNvVFU-vfj0GvDcz90fuHK983hucbzd4GiGggB1sDR_lrqAxSlR0iEto7siKw4OMTPF1j1dV-oEW3zlTXArAoafiF7VBpsi8bZo0QNBkSa5uiISXtrDUg49b-9EOc_x8uMwZxH6lTd9f-eJ1XxzSMMK0pi9fP1mPae0fuHvsZkCTySI1QKnDBTNeeA37jOGgqdKCpWlv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtrSciN_tBtuYLFijUuQJg0Bmew-y237ZMsf_F6gF39U3ZhyE7Xax6ezNtfpUFOptY27glfhI5k5GEhuLyK7vcXIMc_pXf9WtK04M_xO9IpZGE0i3q28MtGDdc856mx5C9Bs0CYCn5o7lI65-NvfRPoQhQfNrbwgfo0DQXcurg5BmqSiLsQCYytCgQrPhutGBOgyE1HrHZ15e4pukk6JE4xOYOC2TROwnjYsC1nrm5u4kl2w3N6PZmgPopQ4q1d4z64K5VktpqGTlX4jvrS6m-CBbgcdZ7kc_aYWUpmIHacC-kL-y8W4dqvsb2wPse2QFHqjjWRWQTN6UmUE-iA-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B70jGDGmCrj9tcGOaxwEUUZnNEczgx6TOLkwVCE4ktW3f7xIg0HDwiaeFDox2xYQZArs1qikunuf4KzgVRRH-pd52cTUrB8bz_SEkFd8OqvshBTRdpsh444liD0J0MYBq9qwZedYMj9JEp95tc1lHlwd3PryOIyTGwST6G3PNc8_pWNacSEbjMa_kwuZ93dUr2RjSo2Wh5cIvklIjj4G221eSw2eEpDDVDLhNdyGgHjPONEHgKEZGUje3LmlGqlvgZnyGI9S-Qd45rfSzH4VAsJPF0fzwasXkZwcICTUFmPxyZD2VB5Vi3gFGGv92qUoD-DaX76ixWXlmbcN0F6EDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoZEebTd9UIODGQNbacR-_52Us3EV6RprmgGS4WqFrA9CYedkQFPyQOYR9GRbCKIbJ4GKEPjptkYP0UBAf4w1kcBS_QB5ZTyHwP_oRjMqBIgw2QrAIqLYOKA18F4xfuqILFmuzxXwifNwomftDDt-H1nka9O5lCiQcqlhsZdj9iF0lfZfqIPPXHzjp2o77Aa0S-TwsKwEvWmHcBh1t7avoefoKJgF0rR7LF8UqHbV0-5BcbQHE95Bp_OLgvxJanqB3bA3wJ2rOFDuWuYGQrjAyIAVMA_VP3iUmvDbtIcrO5bt_l5ghfDsREm8PObP6xnMwIGLRqcqkX3CQjKs7odDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0HBGEcACQuiC9-bTIJ2Szb-RxNwGwWgntOSLXlz4Hdvl8WPFZHcuAqo8RJ3pbOMrc3hNKSB6NuCQ-IfiObFXovKFB_xHkRQXFBxv3KDsPdnfvF6xwVqZJb71UKK1hRPFCOfslukfSW3ZEVCqe4mlyDz1EIJ3W-p6jNC3L6Nhp-nBA7agSWsm6-4f3P8hzy4cV0BmWwNwNYGVUnJEJHnAZYgwO2o4_lQ1khH5tC7_ldcDVls8FMoY06kWCa_clbcYO8Eng4YlabdQvvh7NwPvxVjLzCCLZH1K1CYtFrihRl-djyvsFMZ16ELH-BMG51uTKYjlxq3kg1v_jTJlA3IXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyjREq9_vZGuzrgOub3fBYBdCkZnvucFjp1gBKFY54Pvbk_VHhkpXno11WxVg99Ru85cudysIgFjy5hfBScwsijMbYBe7myzsAdVmmOBxNsoIjBx2z-WbB2ZVt7LH6M1U8IYOFAUap9Dh97uh8DB2S-s9ppt30sb2d1j86Z2EZAei6PQaqHqR_-CtyKkZ7n2j7yrl51m1VBH60_eVpst0Wn69HyX7v1BOIjc3ozxbXSJHt0qxoXEWLrp4s4chPXFKg3_sjF5Fi6gEn_TXVzxXPUDWq7jG-e6y6gbP76cMrMwKUpn670zUUrqJjuBBaWI2ewW5djw6u4L1Qn3LVlqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=U4i5fzuscC7RGbF-gulCFIH_6MWq5535gPqTuvkLmfPnehclinID1G5azhwcvtEfVqw4JX76S-VA73UVT5VXT9C8DnhOh9TdGgPOC-N5M2QU25fxJnpeZob_PkCVzRAyO8fsrgiTszzei-n6Jk7re8rwNfbAwRcIXk24yUDO-S7VsA-E_DSYlQ35N4pKs93PH_mkPeoW98_77hPaeqd7N78rl-hKlO4AIfvtSnsfLiTZ2FKRtRQylqmISbuojicRFmRqUypmoHP5vGcnda6lXFQZPb3eHVezsGmp-62S8wKZip3Lg46fhDfKMAZzHMZRoiU_qlEkxgdRzjNnWF06sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=U4i5fzuscC7RGbF-gulCFIH_6MWq5535gPqTuvkLmfPnehclinID1G5azhwcvtEfVqw4JX76S-VA73UVT5VXT9C8DnhOh9TdGgPOC-N5M2QU25fxJnpeZob_PkCVzRAyO8fsrgiTszzei-n6Jk7re8rwNfbAwRcIXk24yUDO-S7VsA-E_DSYlQ35N4pKs93PH_mkPeoW98_77hPaeqd7N78rl-hKlO4AIfvtSnsfLiTZ2FKRtRQylqmISbuojicRFmRqUypmoHP5vGcnda6lXFQZPb3eHVezsGmp-62S8wKZip3Lg46fhDfKMAZzHMZRoiU_qlEkxgdRzjNnWF06sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJAier7rFTKYau9JudxUzxAjcdK7LLtwO0a5xgKyW5FDFeP7cq51OfFjkwjmSO9e-INssaX7A86ulV88VDQlq284hcaahlRPw7bW6ftVFbXcF7OJNOLjOg_gKFM_UlOFUJejnauRj1kkfDbWDWbx9spC0j4ZCKBR3PclHcrLgVDPJAHz_BKuZxJMOIDCC1qrcJ9fbh_4BvZXy9k2tZkHOK95dwhSAs9G0XO5d7E6JmdHhJqj4yN-7pJdXU0g1ozFZRGxvSbz8L3k1S98ZvMgfZs6Bn0ZREKWpKwsWhve3gNsFqk7zDYcsVAb5L_Dh_xwkqkse6v-IpHVIefIzjZbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1vfVuot-pDgXJMn0zRDwY3h86idcyIi010lofuKJVV0wmU4VB9RwXLq9QN3lg_Q2vfzx4foAlTz66wx71EUA-9qdLvxaXqZpkM8deISatzNs7r3uU8xSf2M8e_K7Wj8B-sl1d16PPEKN6SPOD6cxRi34blNqrkse7vZRxlFswshOYZxjIEmFHWFHrszpaXFhujpFCtJSNNLr9OogO1w7s7UUx62qd7QarWiq6MjhJs87mdlWauRpyl5TSbpRm6gebgchDjoi__t2YBPT1JBTp-P_DIVuikykPD6ckhtOsPh49gKL6TVhF1e83TXRdfMP9VaoWrG0gL7fi-SVgjuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSbOCbkmUGnzAphfveRxrTFWaBpd4NvE6qc5rs1luOlxYmM7JL9ifzM6sC2Ea_AeKILLwTTNbWJKtf7ECTU1N3TgpwFL0pZUcIDuV2Onj3rN7OP3bs3mqtoFELxYp63pXlSWlARp53UKUu5duo8ZhBMcsLNg-lPfqIzYoQCobh6htc3MKDJ1_puqTPAwFrFAjc-aw9UQrAx8McYdAzdMpvdpMn5bsSbdbXxD1ySnP5P_wJaGnaQUZq8JswGYGAY0gNI2Zqizvg4EyLdggX86UIIq9ADHZxXpmISRxwAUGYvLasssJ1Z0AFYwGyeA7GKzSi4YwoFCjOuaghKoDb2JKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXqS6afEqCrvyi9JahzTaPZxkEmZsxvO3USggD6RSfFnmK71eztRaRxj7XOYJmAH8czMYT2Ny53X0Db6gzKAq-7EidOjwwlFFshQJVOU7SXFBNv_jT-9XzGGQJAIUhwFDSDt3F60pFRo1T6pSHgMiveM41wflCNb-IyKzli8fyE4_nhuMQtDdVjYaeCxvQ1tZ9z52sFn-0oKXgCy2xmubazSfPV5A5UndHnYYZQL8gRhLgI6ZCG0KTRVWVMEAKqWIZ2yUJv_zIAIdYYogInkMbHzx4xS_5ScJxlhXsihDpxs0gf5iScUB82OE_DpeO9gv9MjWQykRDFvnmtC12AjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DShEbdHrVACn8UrnUa0e7uMkXhLRzRp9ko2FZN3kN4RIOKPkrdANbGqTKCljjjSol0qniL4Pwu0YFxCuPv50mXWon5KH5hOlEheclnSbT5FqiJ_At-pw9udTckNG1YGaSSMqXkPvaBduvf_49x24vhYxa0SuX9ZzVCSDYZNw-g4a_UvVxb3HrM6YWjiHCQcGOcA5pvs1uT3DTx0rxK74dTx6idOWEPdeUwgh2NhdswssC8wTpVQc_UnT6C6WZI3wkLXu9wlcXeUouwM_ZXEDnuIRO3KcwUuQ6_0f849sJxCEy3GiVia19Y917oBAnk5KMO_sXXLlp14KoFnhFuEv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow8cpFdYQUAy3A8dd85qsyCNYilnQhmQjoWvDwYWlcujnoZh0CJvqXUUpQNarjuGCbAgAifS5lVs7jwNBWoaoRL2Z7gmM42W6b7W2LKyLtSGQTbnTFEvNq6Z-POyOYu-ku4LuyCNSGbcufeWnNUlaWJnnfDquCkAJHpi8HohU0h7XwDGl3TWsoZlJqaqRMBvf2p9Mu4mBwv9JUzLPLiJ8XvgSJIJBbEx0MSRqXwUnu5PNaF-1jmshiquu0Xh6-6C_HiAZBMYVlhFf4_8Wv4KM9S7hiyzD3Rq9XuylT7BT5sHc5myt8P6dx2rdLGqJd9L0HjYaeLp67DkRA-piTi7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7lcxfPIzx3P69kKSXxUTg0Yvz9zfy1Jj5CdFuEWOzlr0xHD1GrekzQKl4K0R-6tR-n0uMut7v0N59pSEsF5FOAWkmHvBn-UrVgbkTw4KOOYtTUQ8xP3vrxnN73bkoDH2-1dcWYg4kH0Vc2LwHPdA6i5sCU_ZkOrM5NcWCEcIhO4SNR78u3ygQQXf_kr57UcLc9Ho7ANhADVBECNXuvguvf7V_C4swrTw1XjGdwoMfmezLTPF0JDkG5-ThpPBu3ZNsXTQYvUERpGJ1BTYNiT47QT8-jSG_BUkqmmNgt-LmU3yZ6ewxLIXCjPWTzjGWNfmO83GHEa_aBRM7R2J_4EyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoVMA5nPhCW1zUADkgxravRwOPJdRBp4KIe-2kOJj6U_r7gqeSf_SX1q5dmm2uop3Ng40iLl6ZhPNvL-co_gQPUDQooA5oAUfNcJHAROXF_BaFX-7IDjAUj-wfzWUIBvQDwQW7di__fSjcCI43PP_6a9UH4a5KvoGcd5tkREbesxYL7p19aHmK7wV4Cjhk98e1zruNzjfJLxS8VRZ2faf8t6JTg6ow05TAexxnrjPSUIpkeStCOafwSguYsxaQS56tmX6xHOc_Lh6FmTDecuPjG3PCzhxGXnMeSAI7DKBS2l-RQH89OO40lRpn75ki0o_K4398oC4Rn6-o27X87QqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIrJRu57y_sJeGEAysxom0UKVDo37LQjQnpYBjwwhLb0iUQd_JPMlRVv_hF6C88Z4I9eZxtt2_pKYvzu72TqgOtpxpJWUFUa9Xgg7ikTI_mG133Fzg_F6KL5t9HGBW5PFdizzhbPkuzGqU38anGVC-8WSTyTJAUnHyE32KNiS3DGKs4-8CA8NhTkrJ7jHhU0wEtD_PtlXPfgmYaSA_kOsIoWe419k5ncMEt-XJUjkbCYOtCGu9fV6mHpjCaO8Ki99kURLnYpy0EjA2GAeLFliUr9Bs0jMOihoUAoDGE_Q45S2SOjXrsjRslcx_mGdPKvXDVrpnvZwfJW8-aRXyO0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsF8wNcZPhZL2WiZFOSUBXkH_PyFuaVr8Aeu3mUPSaG59jgX8L2AQNarWoi34oDY_ggrVqzeVIwk0NuOF8oW_S-dH1jOs66vv0p0swv81dmiLS8sgeZWC2o9JEJpv-SwbVM6QKn4yggQUkPjVx3zoWcHG5D3qbckknWd6-E6fDnWbkOsfP2o2-fHG8n5OZK7otvwfH1kFiey9BZgOw8DUOkIkztV8oXslfHEkUqSNL5WtMkgaupIt6rmQHYST7VOOp0wauRXIAADATMXEnDtwssN3u3SU8T776kwVK5NbfbpnAqBiXN7MQ4YJZOOj0lupbw8roBy7N3ztHKYekceqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAXVs71CgHbeLkZEf6tPGtHd_6gg2wQ9yP_1GREkMj2EQ5m2nAMKlj-B5lGzCfnndkqBInFBll6EuV172dtGKqPj4ETzExbhXZb4GGIJ_SHdosEJtti8VdNhOKoZpg9MfV70wsXL4PTMtW-iRasfdbaCVOumoEgKSTVzYFqk128NQxlQuXnqJEfrRkb0ggGz3yoDIfyZT1oVpZtuv1FizbCisWSuYEWJe1jj-B8yRVGnvQAdDnTi7UbiM5LGA3i58DemRCnwp-WRe2rk7x96qvSCWdZQCi_OCBBTTVPTv82MLvdWaQ4lirM4DAAgDrsBRsSsYuHS78LXeqX_wfq9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyNbj_Br7AD55aQOXyVYG-UnrRA4eXscyupVA0B90XkqiK8ZQqhP6q8DjCj_rWe-q_-WKc4ZK-mkb28K_eJNH-l-vsWTKiPKwYx2rtOp6H6DqaqhKhSmXR-P_sx_l4HkA8TXseptNIkzLlyqnFTPB5NStmpj89FJzMxyYcpZyeAtl4SO3AnWJEVYZDXUnnwjfQeJKf7oevj2yAX-kzVXX0wV5RCptoYIIKkhhaQkLWUQSPEZEJhJUSjXrrfrAZG87qMtfFE-nn97TlRWVybT7bRKm3aqu7UlErMGu7YUZfKKQg6Q3T3Zvske-03IZr7Sp9VndBBjUOCiQozOYEyUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1vvXTy3ZEiMF0dK4aO18g_ZiUQytNQedP32iA9Rv0wH0CbLra8aA3n30I_SeMReMLT32KTEnxnw6SJPGeS7qzyy-sI8NojFss1_E8uBPDn28wgrfO-LVzoFdrG-_AOs26qjfMmKHMjr2a0ERXgmiH6EO0t3c6nwDWJVafvdToh6MgR8TQ26yZbt5aVl9405G8lk0M77yjr0yXGW4nxdb97VyNCPkyB7tCGIir6IvovvZUNdL5RfiU-IuuiwnQ4XEaDsR5th3B3or7atba79oCuSMbmG61prTAENhqneSKivpwAZWm9INGvELfeugYR5NLwOAoET0w0m0oNK4G2kjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYp5ukiHuQt69uWzlqF_q47fYpO4RMc_8hjzC50k5mp4aeGajbrtGVLXucOMlULguNFIrHBBxnMyw9lJJc6HehXbLjKZvOqS5yP_33S2UNAXfUEL8Xnrh0Hs997uB9sy8TLfmRZbgIkh3ISp96BXJ74xtFOe9cOszSh3kw8KimmlyjcimsJFXJuVVSfYUtYeThR7xpTL80E_n6Fdhf2bULr6dY2q51_o03Ba3VkYx4-eJ2BwTXRFTWe7dC6ZnDP3NbHekyzAXeEx3Qa8BAEFyGiCM-34TGTSERVol1OPwKaA2fAmNG9eHW8_Om4DRIB5b0jBELl_s1xb96vn46w6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAXzwXqKu_5I3F5xUqnG-f_kMxL2wN-WHntkj83if2c3rEog1sU2gNabEjPx97Y9cSKcZTDSOBzpEw3gZLsnN5E9ImbS8JFf9X7ZR0LjG2BjyVWLAsVKrdbTvF5fx2xSvxEoZn9k_l6KxbWqfws453lk0QKywcsGz5a3duAwg6AqB_k9m4_ESZZdPxM3N_0u_loq90PAVimBKJSd_Q5n51KsfJ9FRawqrZ76h8wt66k8QBlVqiUC_e6-9q3B7JrO6ekQo-aMDk8TCqIvH_Mo1IFXJeXOl3mG0D9BHDCYZFtNJSgdg8QQ9R3eXAH6rO7S_eogiQ6WIrhnvpIq-sy9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5HADPGm_JwnhEHixfIHXq0bChgUv5xXhxhLmWdNOSKvaT92RCebkS1OSdllQG8YN08FzhArJGm8l4KJzPpmTlWp1NrbbyKZzvQoSAHm4KhHAD8tmPEUXpqZH-VSAp5-wv51i6ONvZhAUKw8Gd0UyshEZF8YgO6g7fYfm-YXb6i1NNF_7NddfdN5yA4DHU0qzxejJtEAABaiJNUA8P20H8cumPBezyFJJBx-kdddUhf4oCTV3ERdMeci0Lh5PdV9jn9f2CtejMWaUeoER9I6vDpnQdYSsJku3w9V9fa2Moo5WsibZNDT46fTUmJPIYDuNcHKBAzi3xWyphYMmygf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sckECC_XRgd2qHgkO1zsPvrXyahJhPIZ5G9e2xD5iUuI9EGSqTbNip9NzTNzYTP9tdRiLCzRGq4h7wTrqjz8u46AkKyOOV3tNe0jsDd6TKMgBv1le_nmWBir95tYR2ATheu-sTaPo_Ems-jvdR1FxgpJpieSYMsbnWsOKV8Sbdt-XwrnJ0JPtyVNGKT2EtGkmBRvCZEAYMzp0Iqc4NGqLAoh-pu5pd8MdiunLUKhPubqgW5VooUDqAxxHCEnIHIwjK7rAinnIx9HH17E5fVwEf_RtSSEJ04wUXeYm0xO9XSxKrNA7R3w9lpcCSCWTlDqpndsJxwLs3v69Q0rW7zzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjBNfbaj1gZGatc5n-q9ONRTOLwC0PQdyma4clKmxVTnlepk8RIm-orjYjyoRmL53PeNdz8_soodQkYmDvCtW0n60YskGi5xQqk2L4n3c-UC8sS1T3RizqmnqcPKYuBgzDFsBot-GyuEW-awxZZwHRDO0mZEI5-pjbPFXMiilrt588D6_f_8gs7xoA5scKG1f_GGGU_aNHrX8skCJScR1zNXMHsGt5ohkZKVsI9JByPuwRTPJgpKSc8RD8yEnerYsebb8Naq_rq2IgeJJL_XasxSIFnpvrNya2NUO6pDHwujkXIaS3_sht2NiCfB8JkiPDnpc2VdTn2GXUPCXrjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=hHDd7sjBmCly5hSD-6jB9u1b0BzIBBUhZmaFXet8yjAoTJ8--JvgFKqsZoBPC_8JuZmUacR7_idO9GATx1R22Vkz24UxDNCZ1DbjAerkhkv2AhX29AtohWsL8pzhVWSdy9zO1AQDxqA1_SQXijQx30bs_0rcXA9PGNVUTH_3DAYS9VkUzh5FdOlVlGy4zQ7Ub7DsJGa7Dc1qCg7yE7_OYE8YYmvL93zXKFefAPOqYVo43bP5pcaI-N8kM1vtfZbb93fAaXGL-9E0urb993sI7N3j0ao2o-JzROyPlMX0frAE5Zws9YU79mL2JT18sA3AWzFZwKps3s9AE88T_2H4LELRK3CDtdUcIZ8PYcinXZLNhnIto5D1Vfxe2hpibIxLCxiH9DtbEz-dZNCFl3Bu0Cth580axfiVLxWxrpQmdXYLEj9qKNVYvXeXeXfyxAgJYFgZexXWiookz8SKd396RdJJ7s7lyQEYxf4lP_ntaejAKA0Tcag_WI3s5xbTeL3BM1LGhdMCHxcdus9oMEiFJxbeMHTSEtfnG2VuIIJPXvwgWn1yDH_Ly3VV7YsYc5Ra-86ejJRhiHiy_0kEwo4mmXbZoV9Y8HmdZVWWApMJ-4FXa_EUKNOETsK1vCEz_McEZ8JR3PGUxibWJvMAooAJfnhyFGvZDcmUABM_rCHk4-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=hHDd7sjBmCly5hSD-6jB9u1b0BzIBBUhZmaFXet8yjAoTJ8--JvgFKqsZoBPC_8JuZmUacR7_idO9GATx1R22Vkz24UxDNCZ1DbjAerkhkv2AhX29AtohWsL8pzhVWSdy9zO1AQDxqA1_SQXijQx30bs_0rcXA9PGNVUTH_3DAYS9VkUzh5FdOlVlGy4zQ7Ub7DsJGa7Dc1qCg7yE7_OYE8YYmvL93zXKFefAPOqYVo43bP5pcaI-N8kM1vtfZbb93fAaXGL-9E0urb993sI7N3j0ao2o-JzROyPlMX0frAE5Zws9YU79mL2JT18sA3AWzFZwKps3s9AE88T_2H4LELRK3CDtdUcIZ8PYcinXZLNhnIto5D1Vfxe2hpibIxLCxiH9DtbEz-dZNCFl3Bu0Cth580axfiVLxWxrpQmdXYLEj9qKNVYvXeXeXfyxAgJYFgZexXWiookz8SKd396RdJJ7s7lyQEYxf4lP_ntaejAKA0Tcag_WI3s5xbTeL3BM1LGhdMCHxcdus9oMEiFJxbeMHTSEtfnG2VuIIJPXvwgWn1yDH_Ly3VV7YsYc5Ra-86ejJRhiHiy_0kEwo4mmXbZoV9Y8HmdZVWWApMJ-4FXa_EUKNOETsK1vCEz_McEZ8JR3PGUxibWJvMAooAJfnhyFGvZDcmUABM_rCHk4-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=UejOAfevinXexSda7D-CDKy6U4h6yqLYbCdimGFrElkpjdVKMuRxiMiJ-PG8sojvvSsc7B1J1ygrXmCsGstN4E4aK2URsA6mWPYC1huVsTmhLGyHkMj9J0ppK2ZqfV0L6FGy3P26WcN4wmbzhqRYd5T5C24rQmxoCHhh6lbHxpwJjiGfZfJMFdju5IWwILiPoUw0_261NV9UeqcdK_K9FF2u5pgoMAYhJvdo-OVyRZzSgYCLbuJfFuf1LxbYVf6iESiSiDigvht770jUM7iNI_D8bUkUNufKkQdR2ub95m4RLWlMdk2Ts2QufiOiaRU_AWnDI5M-hZVprx57ZI9s8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=UejOAfevinXexSda7D-CDKy6U4h6yqLYbCdimGFrElkpjdVKMuRxiMiJ-PG8sojvvSsc7B1J1ygrXmCsGstN4E4aK2URsA6mWPYC1huVsTmhLGyHkMj9J0ppK2ZqfV0L6FGy3P26WcN4wmbzhqRYd5T5C24rQmxoCHhh6lbHxpwJjiGfZfJMFdju5IWwILiPoUw0_261NV9UeqcdK_K9FF2u5pgoMAYhJvdo-OVyRZzSgYCLbuJfFuf1LxbYVf6iESiSiDigvht770jUM7iNI_D8bUkUNufKkQdR2ub95m4RLWlMdk2Ts2QufiOiaRU_AWnDI5M-hZVprx57ZI9s8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU0Vp0hZ60PeTAcYMF-w3EHElaU_YRMFha62l6dZUYlGDkt2kEBKr-aqy1mbBjpio6plyyMT48zSmjaBdBsCiZ7GpkyqYW6w4I8jdj515Un7ou2ZuwLkG852DNC1EkSXQ76q434JW6uRSnNNWHiLCC8xnZ3Nv_x7sqvsXMRqBNm59z2W9re_2gUTFFIAfCsaxROpeHZVrA-YYVZniIiw-wMdu7cLJ81UFLoaH-50Arv2BvuxCndZEHdlM3ERG2ZHwtdBIwWJcfxpyE4XOtKoIurahQxjrrBUl3VVaMk7F3T6PB2E5qBg8seICe3x9706Hwr5gtFHFljnG_nIb_DUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSKZqFRdc0vOkkpHf4sbk-QzyNdgnz8bZxJoD3o-0GJckoeTgGr4okPHvpP38Y4VXXDkoJDnYvhgy__CxuExCVR6Jc6bfrZ9Q1x2kOCM4x0iz5zIvBc18k_Uyk_m_F27uE3pg8-cT_0aDui3a0PocNpCnwTacSy_GTKbM-uaZIb1vV3STLaHP2MPl54WeAEoNFbfjfGCcplSXdVHHCZQDy4yfkIPFytwj8NsryDFzADsHYdsZXz4rljFIt5408qzZe7BgqKghqWZo_8NThjqHP0Yy0pw430v9cZF-SF4eht4pIkaYtTBSeedZ3E9ykZi-sVjV9OA6-OlKSXsdruzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czpnxaa7y8FClOrW22EWNK5TOv-svOePKDYkKxZwMhJvJnMTAv5Gatu9uaU0zhQxoRhxai9YX_kwoiR8PZs0cwbRrEHpaUwnyO1EaA3S93ZjmrEkWFrUYzEFMsRCtXTzgCiC4unbaTvFvjZ40OrHwXzJdY04s35SozC3BJzo_NizQTYU_WEfffrbVurAPFy_aFRWsRCu4apgJIYOj47VUXG8vRHYOB57rPAtiva_ke5pcepY3HUs6hrAbyp8QoV1rpuxH80HhQd0huabqIpZA4Ij_Co4jclNxrggM0SpJ_GdhJqVxkIdB9Q_cM_qnju06vjSPV5UijfFy1ZU4CrWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biSSYDFQtasWSJ8zfeXCSHTLkcQyk272tEqyejzZUS3dOmVL6mWwj-RHD2utAhZwHucIr3N4CAGs9gxlclhbGROcfs486oypDKSU2uEUxPBbmcaqUBgHJ69bXV9Tl3DWoQW6xvtxFJHBy4csRvIqJTo3pjnALYBaHaxXFUXBaakPiwHB-xvWCvt86AHVzyBzoO_oYqF2dlTmXHhYOsKfwvvoFjb-4FXAHO-rUIghWKztVg56ALab34qW7radMxW5IdWfy-yHdjfyUla_ACx-Qi0R242h1rzTKJzE-W9mJ5x_V3PLTR_IQKydPRx1yfKeOXPpn0SxUs7CD196niprzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMgViC9YugbjeXbNg8YP5KNNo3NiV7PAPPpfAJLbcdUBJ4AQj6KTdyFkBz2ZeU6akpn2s0LpUWQvfpAB7z-2yF45c1dAlJi84AkrNsYv923s0g0COk6jCXzfT65M6qNeJd-Bv78VrJHZ2jGUR7_KEBq_mXMVqb3GJ91xrzaZebmVBS5Y21Oa-pRmVMlr0KGroQyhZtiuDbeJTFhyVxI8vv-glOQwqhS_jzQiv1K8E8XuzsTFStZcop3kAATgZe5I9OAVnKOFIQ9mrrQWxUiX893jdnJ_2-kwSoVb-kCUwWVwCq-xX65iDlzNEKlJoMEcX35Qm-c7GzezDX9VDMurZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmTRuBu3xvZ2eg5vBQpeXFQ80-z9fI_0XpoPqDLMU8VnXhwkKMwr1FDQxgPsomiieooVLh6fzF6wVDL7P06JxFyzFXI1_RQ3UM1HknKyc_PooOJiletmGoXcZz8fJkM9JqJgCMuLaYzIEM4LNlFGAWIUxQTi9woN6y12kmBKXBVVR93j92jrG_TQT7lL9AyfKoRr5kXMrby5y17KKPO6EWp5PyPblCyDDpoWAuHbpjg5cGSqDadGZrVLUo8EKg0L2rMdIcpGGNWtAzrNx-tBU4MqKHO_lJCu5Mr7Edp_Ky7IEyXNGwKuDhT3mtvvX2hxor0OGYIZBzqCD5jQOsmpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5QQp7u4PjwFXI_gd8FtlEzGiUIDT_sO8s6wa_pQ-JHqHZOAjj_05UO4IXUk0WoifJGLe7JU7wtbTMJnueuphRHeHThl3ZOmWW_hPpFa3h1F2l8nl2JaCNzNynSQDSQQNfWFLNacxanFCDgvvp-RqR3M-IkmJRY3sTwyrR-cNcOOOYTQEJE7XE0g6bamWrl6TTafbEDplxlm6UpGgxdLEU6z1lPTp5G08XTwiMl9sNh2cJn77JACInMvNmgN6PLPCOWqof9gF26-uuhmKWs4cuXtItNmIWAb55x41_m0hlr7QDltC9Sk6ljyWukFc-XOusQnOYGZTrf2jnBAqqqW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKu9TSBxvvRpAHYK-WgKMgrKn2ijt43QAcCoiow7N7PFRx6S0Fv23fbOh0vgOJ4m4O68wsJHZfO2QYHH4lLpeyoKAokrY11f5Z484TY_ism1jI6DY6FwnL9n6Ku4LkTFa9rBBlgqSbZ4PRyl0kCoFMj-93Vb0EngEfE3N5KjXbnyu1CAd61YRtUunYYMpGB9YoS5pfz_AoLQUJrqKIRr0r4uSoov2NJlJpSIGo2BfjMJPLh-vU_WpvJi8WsfLzr6lvJ5NUN4CKSmuiv6spQvJVOR1VhmVWWAJMmj0QNDTiNbIa-FQ7YP5dsiW7_v4dGWlpwmOIpizXjO9KjdgYhX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpwPDw1G2FsFM8whFXqsLJNKbE7OfslYLKyFUcpzz3ms5NVfstuzMBfRA4zQDOUPjoIzQ444nHjkEUePzlb6xFf6pt9lXUVkGhPflFvFoim88mWy6bVIy3cXXRO6yPb2KnyGZN8w2glanllJhr6-CZBoLqiQtppGi4PSiwXXVqDEsNuXjyvxbZzqhb3mpR78G5ayYIY8rNwnh7q74QrI3RWgEIMt5zkiq9VMQPHi6BsO8AIiqG_YOX0JXN7zqTTf7R4DXTKSfDr9bQVMQ3o8lN9P7lLBJ-PEuagOhLcbj_gYX0zToLXzEQaM36z8we4wjxbIAS6eh2Y776RA9prQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU2fc5v3t59u9qk7y_x4UuyUDoaPjs6clSLHLi28FHdWUZgRj_f0gBEJpaZnc3yraN5hriifm38bwWgnBr9UfIA0tQNp3sovBrAFB3pNYiL712OinZrhn4-_pmPSvSppLRIJ8aKm56C2qfQZVCFzByX0QEwbN2yTYbX_xgYd9WxxvbrLQGL4Y9sstjTTnOwoCMHajg_d9HE_K6NHoP2XZtjZxmdqlm-yV1_DTO4NS7CXqD06STFtcPFPV3SUNca1prEouwSF4jNLDzFhmt3LafKcJ5cpwNEF1lgTK9I6zjr9H9me-DFa0fq4EHTc-WinleSrIo0DnoS6dzjCltZvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn6qza87HPB5fF5c81DWrOl0U1cxcorBBmf27XWAOxlR0OYaAy5zJG3lZcpQ6eM64wUZuE0VGeo7v8yGcJ_kJq2HG2fcGJQ_s2pAJnAyiOqU02lR5WVgGwu4yPupmGPUaBoIVZiO-YVge2xDG4niJaKorqwZdWKoAohZQ55iwfQnG_uRZAPztb5UmEldrKoPHtGlT99t5tvabtLJGxYWbgDtQA_fZFd3JEmC0IqAafnn6bF3YhR9uryYWfdJsyJQWnvW_tWY_xcqQvNMWy_S9ZzYygJjxd3NSpMk-zdttczCCwiz9yRavJ1uiVdkcxy_bdX_xBLQ0HKTuFR6ahzYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTHCVAm5GrWRFfUDtrSNR6Htq4uhRb4RoMbr6zPRHpBjVTmH2t3fvZkNFg7EgHyzfvKF2qIWhsC2ckAJF1SCZmlnxZ7qWooBJAVDQOB4BOdSCw1dKQKxMaPygADUFxtS9WQ81KJGUH0QtdVsbS611Ad2MAoN1HVQ9LRHCK-JIWC_w8UKL9m_O-yRZSll8RFzuirL-77mJ5FrGcSRE94n5qwOacjE_JPkIUn7tOXXhopDE-NT7L6LkqFEuRRPn4jQYtcgCuc7kSI5yYYff770oKQiLgWIey3hJ3ms7x1A1TDT-ZIEXttV9W0xK6q7Jx7vipmIuXg72SeauB9FJOp1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdcCYVs9mjT0lH0nJyB-SejT2H4baWpAcoZu18jmTPKtmBBUDi8fnxvnd014jGSXyWc4sTuaerze1ENo6WC-MGPHDOwlve_7rbhh9EPteO19zVazOzW9klxcC98zivMqarJjbFuLyUlyZxJrHJba9XYYgSbyim5uOumsDNEMKIsN-QEhVg6zFLhRBT87UCV37J2Dh3qYV9DI0tHUeOQIsvLvsKVXHVfuch87PAiNpU0BkqvOIY-_EpWZvqpW2Zrtc_M9K1nTQh-Z9y1WG-HI7VRV2j5ERkeoLrqKn1luMbwzq8VyDMpd19T4ifobP-7ksM6cUVHtW5LIsalBjzqcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unULANgR-6v-fY3xq3Fkcwn17ywyuHMy_vOdvOQp9-u_mRcSZGlf0-HPolt2fOvXAcZKhuHXnwvbvJPozNyH2H9-3qsnMkU0cgsXyWxONUl_DzL22g0qkgmhBT5eD-AXPApcNm03UdFX_wmvyFPdiVJ00QEuO3NMLfF4ytbaLuPH_c3s5NdqgMsLwCQXVkBreawaRAMZxQO5InqCXKfeTFxyz8lptTUi0le40iQA0MDXt-9jSzEuTZAA5iwEOh2OODyI34sXNRRfCiadd8BgbDyFlSTStrfEVrpAr5-t0qKhilFjRDR7FE_2SIW5PTBkmNqw31Tw5p6ORLVZWFf_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8xCqDFgT4qM8P8GO3IgVuf51zxf4YZcUEoizqjEjRSQEN0Vk7x8-6Zng4q9d1o_UBcsl61j412husGJcsuVTJeVIS0zWo443g1Un69ZSYfaKkDC9He-LQ8Y7qJqdtSu304PU8Wb-CPWqEqyDiDIgluIHLVfSpGdfM1vIMMq9ei6kMB2_CUrRT-nWUZm6tQMETLsca5vbdceetJIc1xNHyIGITbS6w0xbJCoEQhCg6SfyzgD1YSuYeUgJytWcMlngkAFncaz-pIGVDJIPnaAoDNxAUb38VI8uy9m8y7dOK7aHVUxrXxmS0i442Zw-b30qKnjTqcEfXvCncOURjhjhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buczhodAdmcQ98Dkz_Zdv3hm7W2vxdhFVW8MnFY7QUQCdGO0dJWtBuc30aJxSeW76PQOS6gVS6radmp6QDls5WG4OV_ddxzLD2YEH7DS1wEXbLyRuJ9JvzIsbnFFiJVeY_8N80Q107RSM5bbGuIV-vd_b-cq9KlDUcthYstHu3ipWKjySbaAeYd5EplKabKDBYNXxxDFAgujRPlPDzavTEBKO278DNMD4-fp0ENTl-hmobPJhtLMObmfpg5lDDn6mAgp9WrXefiBdBSRMHAGjF2pge22Sw8c1B0J1o2hPAm-oLOhTvOxJ84rxDKep4X1Zjs9RikWFFrkHrlWIFvhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE6H3eiw2Ag0s685Yntvdwu9oA1Qa0FeIMbWnShW3C12_us0uOyMNn6C0Y2_IXt5pVZ9yUjaJHuxlzxYuZZCgjRk3WWQAFW40k2WZzEVZtjsuNEN2N0k_J6MhjL5cSjcDoSiGM5FfbXcTlbe4NVWvkpL40OHgSAU9jfhPzjTRVf3lQoMbfQGNtaF2zslYAMnbj_mQ6HJOl5hfsXD0Ovl3XiBLOvS-vgDCJGAvWq1Q_weTAs8jinZEg1Uwrc2Pj459ZvcohT7GzEGDU4f9QtlfOZnxA083vr40xhcbLxFbUUWoDw0P6pWXfc2D0SuRbQ1bnihqWkSu70Z_wVfrj6r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GpJtRaVoSfeIooqWpIspGNPi2WBc0pMxl0cDR67vw3wle8yYuxIh_01-flWTBQXG4D1ttt1Q5HrDksXlHEjMO2iVzooYlM2_UAIuKK17K6Eb-npdW2mnrQI57e3ezcyQ-D_WW0Wgn8-uH7FmInf1DApClu0zOGb83xcPMGqi6EH45lKiBAZNObjtVOJfX3UKbvTrGjjGBRGcFgZBu_t-dV3nG6Db6psdwZMEnDEqnevytU9XDgXeDPlISdpSj366CZdpbbzbF7CQeuKH6XHR3SM9S4pav74X95SVBXf7MeUo9McZkDfKEOk2F8V4sbUXzfIStd3MAXOxbphAykzSY8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GpJtRaVoSfeIooqWpIspGNPi2WBc0pMxl0cDR67vw3wle8yYuxIh_01-flWTBQXG4D1ttt1Q5HrDksXlHEjMO2iVzooYlM2_UAIuKK17K6Eb-npdW2mnrQI57e3ezcyQ-D_WW0Wgn8-uH7FmInf1DApClu0zOGb83xcPMGqi6EH45lKiBAZNObjtVOJfX3UKbvTrGjjGBRGcFgZBu_t-dV3nG6Db6psdwZMEnDEqnevytU9XDgXeDPlISdpSj366CZdpbbzbF7CQeuKH6XHR3SM9S4pav74X95SVBXf7MeUo9McZkDfKEOk2F8V4sbUXzfIStd3MAXOxbphAykzSY8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voxZbawxL6x8v6m9_ku0K-7zaM438XLeJ6hJTN28X5fMCszQ7IZY1rd8wxCQOmIzz2QkK6lJyIIL5EQGk-I3zK9mnLkDWXwHu77yoqx9tTrs8SpTCnySM-9plKbtkjIat1-MahB66GcV_KHhrraT8VjTyxyNrgtVR_osw48jjLqa2JDsMocVaF2be_d3rze-JKhbvhfxpgzLOKnWE52E_xu6vAe4xTXaw6HhfChjvweo6kdcFOmjSRjf7-yGWZqKGyx0E2lanbQ1Cc9EFBJhUxAJWRP4lmBMmt-UcGRR0JRyeMB7OJCb3tzjD-VYdmR1ud8m837-m01j_5B9YGGeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP9n2cVN08PD274IISZNrGcUo76Y6oxmhxf4qWOs25LwlhvEiC8svSrkVT1HTV-GJ3bqfxOGcCk1up2yDcG3Gjhhpae5ojFZn0uDOQhN94EVe2TiwIn7_NLkm4_eW-CLxgniAO6NJ7L5DE7XQbLXcSG_JqRFiPzcEt7B5UgGGUCzQnIxBzdUeTmzztunGMEWBTNAfPEaoVJ3DGX0nndgm4uPupL54AFxLLKGOaxQzrVGMrIhTrNHD9H71L-hE4WyIeCVpRof7BLqepGvz2XRr5hIkKdlayWStZliIPh88ZoC6o7PToZ-f-NC4ZMlhLPFmotys66YX47mnNykUHLTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Dng3rfxqqmmY-qf9n_vtLY0YcfneoJ6DOEmo8LFlm6VLywCWdM19AC1fblnG42Fz4ZPK1Sum9j5YIMqePGuB0_pzHXP-vrHpVQkdMGXDQPlXHLdHWyp2ThKhpi4dJz4ejTYWtkTM7ihwV2TZJmQFlgSy4ChQKGVi0khO8VVxGXY_rJG3bb-KVIhhBtqzVYMGZvrv0RRzSvXlHbKNNt5jASHLdswNs16hAzRL9H96PjkzMPL2dnuuwAW9VQbMrchj1vRGT4XOK4U1l6_IaIV0TAQFMMLdeSk8rgMOwMUV8tiUgMau9YVkhcFUYVYZI8QW9mPmBAykJPaX3IdUDnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBxZbclK9HdRG7SMb5VEMRBS4h-LcH89AqgJ2FsypSFvYT11zjVWV6I5k21ZrI4o6iFk4EjbquB4Mv3X_8WUIS7kEHK6jC0AYtpwZroJQpQEfqKfESdZbChzHk8jQ_mJfuM2Mj3XEztic9N3lMRQPfQxoC2mNYanqFK3v1tDFQ8c7SbcMsclBdAkoL4tTHyZqDDsZUM_dNrH0PBEqNPeBMM_Z3tofNEaDt4EMbLUSre75jorvGWYQe86yJCjqnYMw-rPq9dZlAF-0F2snaiUzv7XcxS8CvxPXmYF7XO4siiqKm7HQ7fukex_nJUgdRVBE8XnSDfIZ9lQnOCiGrqUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FszvyCKbVXS5rwwgBrTxR7RHOJSpB0LkcobfWAfT-uvM1tsnaLSkQwxK2nNYPquY1eOEu1xIBURgrXzXRsXaFJhoeEdf4qmtacxP4kpW1104Po5S-cuGB4lC2AgItuol7NMiL_8_o-3PBhczj1rPQzdBI4FN7oBfl6YA2HjzfDuJ6G0NWwknWiJBzAwAVl_T_V-GZ85vzx_Fj9idJIrUIiZ14rN_Q-BpwiU8ucAUM8tC5ZiT1kJZtreQWfTqzBcn95rcvraTZGtvb2AI1sCcxVjpxM65wb8jlolnet8bXoiNZsgJtpIdZ2KmV3Ik0R913QeGqKmstUbGf1Q9XA0VRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDy17hdTIfNqNlocLHaxv9Cgibn6YNUIUeDpO63g2zm_rQ2BKb8hrKYo-j0qLzLie3qDRXMUk8KkBBi4Tw9_lJcntcvJ3XffHr7uM1Pr-spEedRsCt6uOgZaIB1avBHZfGC2rm3kn9tQ-IRBwSuY2XL9FoPr3Nw9aD_aTtEI3Ny1qmZ2tPZIp27TiOh4G_6urbAG8ygI3zEUTUZTMqX0ml74GhAl7CHUitZz_nYjAP4TZHxreLqSSaaDnpQpGClvdv-aFmFz5nLwNnSlbwlvmRTcLsttXepvr9RhCkE4tyiUlDnVpTGZOWhpinjVGqPOUJGgMNsvlHIeO2lu14oFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_9Nh_DpKas99KZ5ZpbfkeLDNBlWTYgrAbXA_sbG5MIOrxdiiNEmrgp6yhoRNgX_VykdcvxMm4gGrxM5jMGjE-495SIrVUAYIXe2wKVHSSDsIv3FDVNz7yoLXHy62gHcrC9_kuV3RS3bLtgrH1Q7teUG2n8fdoIBHiWpYRxCi-_LrE8JyzdpGxbl2LRtIQf9J1XviKJ8rSLu8RfDDr1RGdxj6QY7kxZrHBqDsH1s8PKtuHnmStCCMtMxikCnnbFi4Xy8CpQNlxQRBgttcfFZ1SG_koVGp8wrI9mmrAz7LKzNAabCqRmLHB6pfjFuWf3CCHpd-rB_yNTWgvk781tlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UouiygzPbaTxaKzZe3Yu_vKf_4xRHPvpvazDZ9lOmcblZoIZlRoPVsODM9_vUp_7GoFJlvtGUrQmUxa1GtD42h3I9t1Rq9pBdPEZ_i8Hfa-9A6rwD_FJu1KKzkgmd2ADGYMOCYK9eHytzbEB_PPeWF9RGMhMoAbaTgaOXVnGpJnQktnG7EseyXg2_6SrvN31m6-jYg6qHMrFvDu0e2hA6xKt9Vg3ROpgMsnA1gMzlho6ZxaQNTrJaxOqQKe9-im--Rex3OacGPOfh3M3weD3zmiSiA0pj62QHjFshfmUAr5J_JvLb5Oj2N9HyZ7dYQLp83z7hoyW9To4NmD7hhWeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3eHwOCcc2eRvqIVfY7SHGO41PiQvgZNNDUk-oI6snSmIQ2fQ6b3P2RsiancJXUb2UN_CTCd_J5jDl-jelu6WiCN_WJr2lS2ZzJy0Gt0Oj1JLYPiUZrCYQHxFu_21uLIaNFGRSH7ml9dWumGjWckDeJInlR2lRG2v_vXrTvi_jHIhJ7dWZIE06_ryT0XwNcnqqzduuaWY2B6mnmtfWc57kR-_19QwOXMPwo7UVyNcPHYm-xxA-iuoQ6O-rK_tpgBlpaij41TrrnxebFKV9cnU-xYXtgxqFYHwhPAck9YuFMtoaGw4vGnfhWow1yTe1dIc1TongsiC2gy9zS8YTZkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulypkIT3A5zTK28Xv9yBpbe3wyev412MZXej5JzxWEHYMnV9oGn_3fPuFaCeVEpWYHwBh6B7b_C_7cZikYg2ge38yOTMw8fUsBSJyURs6L97q5VpDME-k9VHwYNfrPQawUTvvo-4X0EZ6gLZIRX29nrBRml2Qcg2FXv54P4DABkRVyp7gNqArn9znOuyTpVgNDL1pqkVc-IDDYaQJX6mWGj-NnzycsQ_9SEehxqTKAEKPRlkrant-PPZFG7-hVXwduQ6OupFVJQXWhNtpdr6tGDS4JOciXOXVVW-4fEkVjRXZu6vkQxcUnmPz7dH28QJNIK1t0wVcVi8Nd_zyFDIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faYsutGMJgAF15sRogsFwWq9Fou3WQ8jXwn_T5nOTLqlnfk9kR4_Q2UiXt-erKm4kf4WTS-Pjtos_kNotL4Z3Ddx0KucY-SeK8Nj9lVV-IsdzJBNCGmakpUZzOppA4cps_RnUNuOkPuASDE4uf0mQAaK6QlYCJdjC2K0vOs9iisQTStK2Lq4DyTYsG8CEuZp_bzsJx-0IPzv8l6J79XvS532B6TdHALXf_fanmPNEhtQMNsjbBcjJc-YpyTSkQTfy8u-4tNL0fn3jy3oGnAiDXpT_7n3b3MyiXsKBYQ6QKuboBXwPToubLTaivSChOMxrULMXORWukwFHXChKnWGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph9-I2IY-yzGsk4-gUt1JzW2Bz1j3IMK32lEkKxxnjSekjv96LCaRTFc5-OXM26jMFdNhMlUOJcTC9-bc9s_mp92xC_U0GjKjyi35JFPB0LaqjzHfu_hoL_6eAu-WQRG_rga6fAj2M_ybWD9AaJKodHbkleMg6W3xdVfjE8Px60YIfhYuV1r62-CrG8Scu_gFFF5smhPs5fiVxUM-6OlgsXsMWyqfNQ36hPrWWZhGImOdbCA9GsinGxmrQ_w5A_HwADlCrkK2XNK6dN5QmIhOHmalUPXHmBxj86C449WYt_BgH7aC2O9SIHOuc6ed6zsiP1maX6z_AQ8R2wyMK8UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUVAqZMubGONOQHJjyaoORn3SapR4OZ3d0g4_yasrDLHjFz7WEJNbRwItDUXzBEVnSAi32H7VgOBysnGTL2P9-UrKdNtzJ3lO72t4nw45mfTgdELc_M2zGz9JtGiV0_lfudEVR06zOEBmps2_RnDAAmYG_yZyrDZkGfhcJF1HaNribjY5QnEdJ4Hn1PIFgvMWLv8gaQcGqufOdS2LxhMmaCUjVPEIDKo-byh5soC3WWe5k5JthATaSWHG7l4541vcQYEvg9WqRWsEm9PB1XUf5OVtkSK_JY-qEVq_3w5ovWitgXd65kAL5CUS1R8XZVfTew3JqyDFr8lPoTeURsuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=NIr_Lp4Meqo1OSKP9F4A5JWWikpjPgkRakixGLb_FXln3Yj0DEVq-A1HYYdWL87l1s2z6Fulw0GkdnsSdM03zw7mWfo4wKAaZ53nUjZ-YCx4yCZ8NCAxBFZC1v1aO_l4n-HVFbDhd2dVBuc_uR2KQi6nttSwfLp1zL8dmkO7puh9fwXglOlDyhhal8Su7Uvyn_fWCEuGV4K7o2CNbO9bFpV9zqY36irNYyFS7aYUXpWIAN4vyq-Sif9zGUYSbbuUXejzNnUeI6f0Aht4Tli9kjvEH70Q1NksQgXiAAmQaeyfk2gmp-57aqnci62DKY02Z9HdClt3CHIB32DLgyb5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=NIr_Lp4Meqo1OSKP9F4A5JWWikpjPgkRakixGLb_FXln3Yj0DEVq-A1HYYdWL87l1s2z6Fulw0GkdnsSdM03zw7mWfo4wKAaZ53nUjZ-YCx4yCZ8NCAxBFZC1v1aO_l4n-HVFbDhd2dVBuc_uR2KQi6nttSwfLp1zL8dmkO7puh9fwXglOlDyhhal8Su7Uvyn_fWCEuGV4K7o2CNbO9bFpV9zqY36irNYyFS7aYUXpWIAN4vyq-Sif9zGUYSbbuUXejzNnUeI6f0Aht4Tli9kjvEH70Q1NksQgXiAAmQaeyfk2gmp-57aqnci62DKY02Z9HdClt3CHIB32DLgyb5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzsOCJ1fZRNg3eGgLHZestkhzYxS-eT-R65WOGIyUINyom3mNPLT_C3HHrmtLqqTZ8VTgk8bx_RK3Bxo1ZJXo3cJP6_EuFaMRqS-GrC4uJb161P0su57izPJtB-qCl0y354vl8D9jKlYcU4kNeG_1nCLtkfUihuYNL7gDVhCyNNDdzShnbhQ5mgg8qfn8syS_7kwKu-_1_4lbjkfslrhalBBgIGyeqw3ge12_UjlpJledaypSfAkVImEL0REAt4jz8M9yyASW8oLsiut2aYMX2BwCPht92Qh0bR0xG8GWFywvoGa5vWYyCjIet_83MzAqeLoNSUzqMRjze03HLwkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jq2gLStu6Gzt_2b66FWa96E9b3cwJAIAs-ioRSf47Jg0Fy9EmJMoQK1fyI3EYQj1EPwEWjUSwX4WUtYFmRIgMiwQPDvjXb8SfjgflvdwtCGfilMMdyEHDSYllKLrvOo2ZxvPsTDDbPhHq9XtfOH5Tv9cN6U6J4As-QcMdgLYc8FkyXR8u7hJcJhwdiOWea4sk6ENZ0vDM-Z1lQhNrj-KcKTIfAqyORrET87yzUpLnXm0CAK0s56LcCuRXAAc8W6MwElJHTUu8GrZDEWlkEQSsWBLF6LkRSxPVyDQFzi2e1MRlfwIymA7OS33sfV7RaxuKKdqeDeHzH7o8EzONImhvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXsBbp2pl3aO6y4tv7k8SaXPPDXELmav_xmtcAlJl7Vbc-cZZjSNh8kdCtF9LRlFaFYU18QYNqVYurthjVXbDgCO8V81wtbLEdABGe_6wWt8q1L-kSrtmv20YY5T6nkt0Jgo0Jl-8z-6JhNke1WwmZ8EI5-1MYa397ZOE3Og59sqM4VDl6F09YCEySP5gK-2U2c1Hg9dztJT4b-Mjtl9RHgvoTBD06JW12it544ZYvcQ4dBol6Xt0vc7b8Zy47VvgFXb71PaCy2CqAUxmLEumzfniBYyXU-4BDSMUsaPpnScLYAUiKH_ZZY7YU_4bryMXVMax20npY_8Nvlv8RKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFnlAsPNh0S42Zuzo9xqAep6fxgi2ZPPFU2T1ASwKIvfUBvS8EilViBCY-t8bo45qFF3vmY_ZGZnobZaW-hs9A580U-4VfLVigrAF-A-GlK6hRMPsTGObOQMt-_dLiS4slWGx6yyjfpzVK4XNTj593dl4XO26sweBKno-3Pj0Hbwt0hFLyEiQLle2iZ_GSrQlJi0AQuolSsK1NAM1Av-4lMYD3Ndj-WRDskPYskHsEWOsIhg_djJAZgK3bC0I46Q7yQ0cCRYyxKVvpr0wZJzdESfqp13NgicryuF5DkE5ZnjUs46cETgyAUdnjVq7Ie8b_F0BdGRoycsWrve1i9acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdl3XtBukVlr0qgF1I16ivbGyMw2ywYIyZ_c-xt9Ys83PCkKQ_7yHMHIMwLrukzlmhnguRWyqSW_F0DqNUw6pjahyl3of57h7mKOPMtWwKsJeNDBMvkgvTVQyYTvE3Z_yjSdoqgnZz5q3Y5m56tjVpp1XT6j9MA9xMv4ivzcAxEv5lLB0y7PEuJR8-NWbs68gKC65lVWlMOEI_D7AQB3GCqwWtmIhIhdvelxhVGKZGkHjIqn70zkhTk0DEwIwk2_edQA6GxnMGtQKeMqtgpu5YlmCOgXsjKgXmr7ftC2R89qrNiV7kk9FwNRjsN1QM9zhbHbFWpR9atNDOpRr7QR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0ZSaXHtYXei9BeeGulVFma_jPJRQdlDFTfE5eSFMiJnlFwmTbxT_QAkMpyrLLY_Ln9tO9izg86DL3TfvW2bwcz6qBuCgp16HBLfjZ1T2jAJSq_8uCWU4CN0bijovAFdEprSbYNbo4hvDWymcClYre2nt15Vhc9xmXdB_53O_dfN0jjwWBV8cWq7EqEZR7Qh_FBGXHc8iGS6u2suvhB7-RVg2CXDBjg1VFCv0QR5_CjkmcAvT5BZqBRagto08M-R7XgBUgUZTziyDlK24wWefW3l9xq5NLXO-oGqxLGwQ2y9Gnp9g4g_yqyiZzZgDtcHVI8ic5zJyPF-xOFEF5LRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrYzbXNaWhKiodz-M4uJxEJq_RRAQ62LoLoriPcKw8aH7SpUkka8J6PQsbXaFJMDAj7hOBUOM8rQ8OWhchsctgxq5g7KMlDvZgeYXe2PPS677goZ6B9K5fR-2w9Aq6K9_6wOF0guDY5z8CwC9M9cMx3tmy_lViG0AyrIx9cNVJv18ejisjI4vSeqHQy7-PqnsB-qK_1bL7eUWq4TkgkHq8Wa8DqfpFwoyI0kLC39pzdqm6HYoTbBXoE59VJniFQnBFOxB-VbL72F0xDzgUdnUDz7_Tx4im18rU8_kM6bV-CXGQw7o8xi5CTe9gxn5Dhl9Gtfc9p8kxQHn3TRIUJ8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=TjgLHuF_r4v1zt-57FlDrwYiBDYATdVrAjKpmzjos3eDyrmGlpd0RbZqKqe-NxbpuzfPRvZwXRG6XMOSNKXtmP4HJWSXhU9G-Aa5Sifm9HkJows0mZFky1oE-p16yUj8uMkxBoWfvZCMTVBbhBXKmmZ0e5ciC8gm53cA42LgqEUkKcOWESNs3ZYCNPME6RMHK__akI5j7tQ8g8uph3vmlUCgg1Nz_kJzimiSjiIXJIlEXW9gpgs0BYksKoVwS42q--VwwYMokRI1NYGS8v-YIzlt7lcfZaAiXUSajd_lh5wn03lnydgo0rWz_2OltkPH2oJWt4r7GRrtmKlzveBSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=TjgLHuF_r4v1zt-57FlDrwYiBDYATdVrAjKpmzjos3eDyrmGlpd0RbZqKqe-NxbpuzfPRvZwXRG6XMOSNKXtmP4HJWSXhU9G-Aa5Sifm9HkJows0mZFky1oE-p16yUj8uMkxBoWfvZCMTVBbhBXKmmZ0e5ciC8gm53cA42LgqEUkKcOWESNs3ZYCNPME6RMHK__akI5j7tQ8g8uph3vmlUCgg1Nz_kJzimiSjiIXJIlEXW9gpgs0BYksKoVwS42q--VwwYMokRI1NYGS8v-YIzlt7lcfZaAiXUSajd_lh5wn03lnydgo0rWz_2OltkPH2oJWt4r7GRrtmKlzveBSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALyuyFhnJo10RUwQJ4AqqH-FTUUWtfoDAocdWaqx6zNCCapIZifb4qSsQClYsZTWTF9pG5YuEQIpSpBwpyBa_-U59fS5JV2Kq018CBNDZFn-_357Q-7-OqSX4wxpiO-j0ameKdOqiB8DrPSb1hiYk78gpNhu5TO1jAn-1CasCcsUfdd14ZyCNrN08BQuadsGbXbZ1xUbc9mY_I85L1J_av843j29q1pKHHfP1TaqCw81CP-Rw_xxV_TFS3_2IMx654lrlltSpidJ-89coJ9FgL7k4NPLd3Ik2GuN3V-FcEp41wq92apSreSYxKPf8OkHDVpl_Y08-RzCoN1Xb5gZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mecqgcVi5N3MS-0csQiWJfvJTtdRvXkF24g0gu47iqVIbLIvWhLKxKPm65znp3fZdA6CxJ4DM-FSgOsDar33DkmGAN88G_gonJuIuzvfmPoDjzLtGiwDsxyQeBWBnFK0ioWm8o4-2BxUcISnMpuGa9yao8NFMDUSKjH7FzdMljPvv7dNE98rRc-At_eFCouounx_whdoaMceTQVEHDJbdsl-V5znvFzD-8L-sl3JRznZxcOJv2LfDtGQve3bv3FqpbLuijZIAM2QdELiNVPNBawI43F1ygpno1vbpy1T7rDPvn3EqKdQDWxjn5kSwahphv6xTviZwEUG5_vjBhpFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=B9Wz_G8_tWF-neQJhg28mF6M3D5WENiS0p8zbaeyWi0fnbmucUM1Ry4Pi84HWph_HhcOsZjMbu6C6LHbCryupSETid0Tk8bEGUh8pdr7BA5wt1B3AzXIzdW8j4RxgiTRGquKCThJCwI6q4BGpMe9uokYS44V1EDOaiP-PjHrnpq6UD5g9LO8b-HJuZBxRR3oU2TO2WQlnKLdkgxPI2jT5jLa8N0Vg9LsJ7WPHvSuebATSVJTSe1QoJ_E5mksvmL_ILv-AjItOoQS6uTVdDiRcIZgtcufAJxkt5p8dpWKIgoAIKf26Iq1-RhiXc0IKB3ngeNxA3ZRpLZhJtFTFpjAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=B9Wz_G8_tWF-neQJhg28mF6M3D5WENiS0p8zbaeyWi0fnbmucUM1Ry4Pi84HWph_HhcOsZjMbu6C6LHbCryupSETid0Tk8bEGUh8pdr7BA5wt1B3AzXIzdW8j4RxgiTRGquKCThJCwI6q4BGpMe9uokYS44V1EDOaiP-PjHrnpq6UD5g9LO8b-HJuZBxRR3oU2TO2WQlnKLdkgxPI2jT5jLa8N0Vg9LsJ7WPHvSuebATSVJTSe1QoJ_E5mksvmL_ILv-AjItOoQS6uTVdDiRcIZgtcufAJxkt5p8dpWKIgoAIKf26Iq1-RhiXc0IKB3ngeNxA3ZRpLZhJtFTFpjAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=mmeGmmTqsEW_HzjzxrOOHy9lRkH7mUmN_6VVqMkq9gcyMdzmSYk0UaqTTHKCXK-aD0VemHUOMhsJ6TJ54lOE2YuLV222UGYUzpfRdLEGrRKFj670VKWVIM4g8sLLEcSSlg1biY5BXQkHamWbRMLhonUr9F59lsE-QAmz9mzaH-Lf5L7zDG40ckZxy-fWHI_qZTaKUY-WAIfNxGXPnBstka9g9Yucow8AKC0xgk3_IuBvOWRIluiH9UFYAmLd-g-ybTYwtRqDCXhOmb76qEZI0OY2TStgTH2VugmlkEIR2PyrUXGoMPHoOzKXl07Svi8o7h7X6dZOltEjTycJb4a2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=mmeGmmTqsEW_HzjzxrOOHy9lRkH7mUmN_6VVqMkq9gcyMdzmSYk0UaqTTHKCXK-aD0VemHUOMhsJ6TJ54lOE2YuLV222UGYUzpfRdLEGrRKFj670VKWVIM4g8sLLEcSSlg1biY5BXQkHamWbRMLhonUr9F59lsE-QAmz9mzaH-Lf5L7zDG40ckZxy-fWHI_qZTaKUY-WAIfNxGXPnBstka9g9Yucow8AKC0xgk3_IuBvOWRIluiH9UFYAmLd-g-ybTYwtRqDCXhOmb76qEZI0OY2TStgTH2VugmlkEIR2PyrUXGoMPHoOzKXl07Svi8o7h7X6dZOltEjTycJb4a2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=DX3qqbfxGFeeVW6zTUJxt2hmaYaKkmwLqukNolbj8ijCwV227VPtP4ST8wKiQ_lhubLhLTOsg8sabPfJxK1yNXGntZrSYWME0M1pAvbilecQ1C6xl9JWmNwJ0XEg5BwyHW8SQI3KcPl49xkhg6NEGjtoJ85hML2YQf87Bmnh71xbrKmyXsA4GhJqk_YDxrcbOTydYyiTZE2oUDv9IGyW0I8JqgerI7OMQARpL__QcrFdt-y8uFCWgHGQtnb8Vp6ht_iGrzfrwfaz_AO_xr2hjIBEiTO2OYCS46k7UehmCNP5liC0p5hxlauPPWVNzj6obj6-dlO66v8iul4F4nXh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=DX3qqbfxGFeeVW6zTUJxt2hmaYaKkmwLqukNolbj8ijCwV227VPtP4ST8wKiQ_lhubLhLTOsg8sabPfJxK1yNXGntZrSYWME0M1pAvbilecQ1C6xl9JWmNwJ0XEg5BwyHW8SQI3KcPl49xkhg6NEGjtoJ85hML2YQf87Bmnh71xbrKmyXsA4GhJqk_YDxrcbOTydYyiTZE2oUDv9IGyW0I8JqgerI7OMQARpL__QcrFdt-y8uFCWgHGQtnb8Vp6ht_iGrzfrwfaz_AO_xr2hjIBEiTO2OYCS46k7UehmCNP5liC0p5hxlauPPWVNzj6obj6-dlO66v8iul4F4nXh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=VM95etfXoXiTOOiT1Zb60SJDC8UnkVu1j7bpJ7BXkK8W14Z0IHm0ivZDPD1KeD4Z63jovSWSK-2dzPEyJ9iDyt9kse_g4W8nMv6_yduFZtBTniBk1fmE-JA-IPA05O8Gex4SU3_TEOujGAhbYjqB5Jwg3jWDi2f3ZqMtYiuUkXTWxlvG66o_PAw7Wt1ZnkHOFH_7SCuwBYEcP2V40mE56jpHJyqCsfv4P9Gy_gWNUyEdoQ3XuRyFCy4z0-lNIDwkKRiesKCQOtaS2JBsQ-R74QLNyCvmXAVdeyL-u1IG9iBNLWNsCx378qYqx178i6KXNqeRqKblwwWrWShZYTya1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=VM95etfXoXiTOOiT1Zb60SJDC8UnkVu1j7bpJ7BXkK8W14Z0IHm0ivZDPD1KeD4Z63jovSWSK-2dzPEyJ9iDyt9kse_g4W8nMv6_yduFZtBTniBk1fmE-JA-IPA05O8Gex4SU3_TEOujGAhbYjqB5Jwg3jWDi2f3ZqMtYiuUkXTWxlvG66o_PAw7Wt1ZnkHOFH_7SCuwBYEcP2V40mE56jpHJyqCsfv4P9Gy_gWNUyEdoQ3XuRyFCy4z0-lNIDwkKRiesKCQOtaS2JBsQ-R74QLNyCvmXAVdeyL-u1IG9iBNLWNsCx378qYqx178i6KXNqeRqKblwwWrWShZYTya1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=MJXjoCho5W0_ZrD8XOGrbBZjjHsJFXbsRqK2sqb-FrlIKhm_tXHIszHqTyzIcGT_rZFN8qfWpqJ06kd9rTfi79oVeCR-k4c7huHpahLxdcVsnHsVLalnG3uzcR9iGkqQs_8acbtS3dg_zdLRXX-g9wfHpyvGmNplvx-z9dW_Ip9RhV4_XpJwdUdand-b75rsavFBVvxgsp5i3-23uTcmHlBu3nVYAIvtCon921_OdHNcPLKhvWKTxnR88NLGsFEj6wVmaqJZbrOdYgcL067pNJ58OaZok-BLxQ2LeMPEMWKijR6Shce_3d7BtmriysakkeZ6wNjDy9GHWNAM2eOZYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=MJXjoCho5W0_ZrD8XOGrbBZjjHsJFXbsRqK2sqb-FrlIKhm_tXHIszHqTyzIcGT_rZFN8qfWpqJ06kd9rTfi79oVeCR-k4c7huHpahLxdcVsnHsVLalnG3uzcR9iGkqQs_8acbtS3dg_zdLRXX-g9wfHpyvGmNplvx-z9dW_Ip9RhV4_XpJwdUdand-b75rsavFBVvxgsp5i3-23uTcmHlBu3nVYAIvtCon921_OdHNcPLKhvWKTxnR88NLGsFEj6wVmaqJZbrOdYgcL067pNJ58OaZok-BLxQ2LeMPEMWKijR6Shce_3d7BtmriysakkeZ6wNjDy9GHWNAM2eOZYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNPWjB5qJ1ATkwxE2XSBj6ZhvdzfGnW7XE9P-W_l0TGVhbhpOj94GobhHkupx7zAoox7LIob0C-JpQxE-OLDSzONNXLc4DeeKTtT_XqlKOBwADf-nADmPM_n5SYqxIUTxjIJnN0OTRIjLvA9AHS1jNTro5XmBjmUHMDQ8p1MLuiFKkAr2Q7Vq5jdU0yNUisFX9rvruPuLt0WSGpivwK_Prjx5xLwPUqFTF4g7svi5rleoIfJPxfih6WIrGKfIcbCFd637hgAcg6_fszC2mcIvX5SnMemThxPXQnRGMVLD4t4kgmWcRDmlXXAQaTLjkkxmquMouThCyF78lO25lO_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0Zjk1CA5H7W8OQ7WEfekYCPyHrG3N4RgYED95ZNQrN0ivTPNVJ-L11pV4iqHkkcCTfA7IiHarpzc6nHVxusedHtnBmj8RI2k2xkGEnbhyikgeEQrGbJQJrK0K-jTUZzwx1YtHKyY-hjpvRwX0m61CkW-C_Q1nE_K1Dcjx6sxXKCvUpsUOBl6XOGXFKLdKkKeAenoSGFNBvz5gkgTj8Nr7i0haFQVL-4fWR6vI92sDoM0l0jV3nV4E_8pgCg7J5ZveDZibcdF00zdvtaiO09WkxKfhK1CTxzzXDfbYiH1oNOYptWvTcygqbUWg_v-wmGPArnKQ8imbC2UxU4tSN6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAXd1FwEyUjMqB8f_HPnxIRHolZqForC8UuqUPr4vxJUK8r7vL5oP1dfSsVLTSKdsOMYhNc1G3S6KZB3Cg50S7UQhZ3hJNmibvLi3ruuvygz4GIRm28-zHGVPfcJ00DTOLzKP2Nc--rOdEcSXGHXVsopy2blFxORe2Vy01LNRXY6CnX9nSTv0uz4v0wArkZDCcoEttkvshfdu3yMzg-0pZG7l6tFWQn7YYRm4JYNsMYglBlcBTLTd86vXEN_tpVxO3OxmFoZQQJCT-lmbN_W5X1tbhe7J5RV5PgJz1CcaralUTUG73GiyWMkLcVUbSLE4vS4HMenxwUa0Yxtyn1bwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjkqcUglvyhwK0ZYlm2f6_LbWvF7HHm0bFpw0x602gMfGssyfVhHF-1wxW71T4b0Dm6x1m631ZirX6budpERCitTs6EpR5Kq3d0s0hloVD-zBgl5-5Qne8bVJd5h-zs8r5GQMGjWE1e-uT31-A_dl2IAMK4C7IEVLU1sXRdok6YRmrFRB965amCfrtYzz2b0l276uqPzTO6GE3R5EVAwzlilvOzQr70GJFcuNPyoJBtsMNdG_g_P6kcgcfJ3ZLjaN3itr4_u4S6kEeExQC2GAaMljZ761NZ5yc0WXIu0ZzuVlGK1K9nKmTB6iXt4D8NAR-AB9Sg7lV0wta3bSyMMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyYK0gTgsZxAAiYGXyHRgRGo0gS4gsKm6geybq52IUn_jcJzskb8OW4qr3Dlvcu60Hi44hciJUWDyOz1RWu1ZN8QkCxSHwjjEJ07tzPjYWTLKAnrFRwYGCllK5WUbAkcUUhMY6xpXMLh08fzzQ-qu4hYKvVEeTkCFF_KqUalb3rZjQP0xr8Ln2rwwci0i_-wCKE10RexHsxkUe6o8ZosdFWVmpiRoE9WZgK34Gpvv__1kqwloHfwKIvCSJmtgo2gFgsIEbvIe5AoUfIN_M__3cJ2kJ6EhaMI-_ran1uneKAiGsGTrl5HJ_pQJc684_JDvfnqk6TtbkZLImD-D17daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gE5L9oNrow3JgM9tb7qabSvTI8aVMLzcj-CG3sI2LowRryMQ1vr_7YeCbQ9oMm4z_MRc-pLmFsi4RD3NV_S0aCAYfimWjIh6PRpAG3m3iBlA-iF2rRbPeU5G7-mPZu48JyLninZ7HkFGPMMRWMW1GtyKjmM6Y-wridJy5UcQQoXEkavRMsB4qfGzkwDgaPAPrHPfMmLa06T3mB8DaT1TXbqFWz8leIqEOuUmYfusM0uERenzHBTs2edM5RgFNQhXNM1w3aaCBfDAZ6F160_jKPW4noMSnDHfOkNQj7JX61xVPE3U8HF4T1HavtRRRuFgBJOVK8yPnZwnlXyd8xddOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eok-vtdbzS0IPduMaD-jK6MUHS6myaLee2ekW8a0oLH3YRpVTmcAPq_lHIE1mIX6MNskW6PwbMLb6A1YpJ6i5j-geG3TcG9NDne7uKXuP64ph0kvlr5WzuAkgcPloq42NI74J38mNYPVG5YRjEtFf1UL-f4B-Y6m2_qh2opk_Fdf4fOXb9LfdeePBglH8BFezekdDMv8bbBwuEC9Me9IN_U6MbUjIoWsVIAeIyLvO3_a8qwPu6IMH3db96yU2z-tdUzFjAbQYBB_G9ldcB1H5MpK-4gG4gGne-40B3Vhw-r5cbC07l4nDieZRFpgH5TqRi4Ao9FnGzyeFHtfqFC4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-qp7U7IVf-NwQybXslsAWiVqj-CX33I-DAR3CD_VL3_vzkBpfHHQufmyGqOHkCQ-wfcp2kiSZMGya7yLIp-oyOg7l70clZIfm7M-B3M-CixveJ3KbisvuUOseN-kWFlzxUGcbcqQfThlo8ewADLbbvNOcUIYCKCpK8Szff6HVInPOc_-G2fi6BImWREIRd3zODQ9OhzLt0KmYE4OJvnV203jR5NFVF13GNOwbSsD5zWNli6n2XwYi1-1zZdk50c-WWEInzv65Midu1vGeDM5U6Vd31xgjShJFP6W51cpLukzOFB8a38n61pxJBuvH_V4RzTr6-6V97gbJGokng25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJcVf_0KrTIFgwzD_PVycEbsVniUX17DUpWQvXOXDuyXOdY0L0mUNDEvcBQPeywf9u_xGufJUC1KataAX-ip2TU89v1QFxPUhalFsBeTcjCrTWOQmWoX8QMmZ49oT_5d2IKxtiDzJcwFJwkyW-ERzi7vKZ8HSYURMdI3Ge5ob4Mhyzb2wbEO-VyWblIhXUfI-zwJSeHMAH9fB9oDAGxt06rpYgRgYQksIeHM4If3retdfAsMWKX4xwZkYf96WHQaqEowx2UYMuA4jswc5pa5FnVq6ja8PX6498mF7-i16b5CyJ7TS396UDuQag5cCo9pbKKoqLCvTYivTrJapj0HuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wy_xRbnCjX2XfzAKmncCeCMRQA7pCEGulH5vJQPatz6hk2t_7RGujI9MHhkxe-mRfQE63pV4v__nQw1JpXnrkFVDumsuQpZ6XdClBPefyXl5DdQ3h6DcRGKbzoGHIe1ScX-pmioLza2JVceoZ4SxLknf7OrChBG_MUD0pVQv-0KYewzha1LwKuS-P0SJN31n9Wtr6oG04jMth7FWokf9YjFQlLSLRGnPv3b2c4jOzWmtS9oKMJnOU6yknqXADQILHvi8tFX_pe88VK73FFfuXmbB1gAdH7kxLf8eAFLFkl0oPmSfrE3f0pbUQuIeyzsKVKDoqkahFriSWVqMEDfeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifpN-rPClbRgOgtT7B92AlYu--msjIjU9TWXLHvRytVkwvaIxNVvYvYHhAWZQBaeZQI9uxzGj6NnJEoIpetHqSBoiNNl6TwFdViz3jH37zLvcHSzNBbp4O4HL71gQRnQbJvL7f487QvT-Z1KXi1OniqkUUG9X4y44NM1HDF23cXV9oRgarTAj8UA_H-cdKd007_xYgWG-Cr3cKsd56-ZCTrTMmgY1-IiN_Ons-DYJXIdyUeChTj1jNH6-99cvuA5t1ffL_RKhGFMpQen3NG6tsRq4hjl82j95mO0Aeudv7H7tPkcNdXVxDeTe4IdjRCf5csuzAbAY5AptL0ApiOJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD9jDmo0i8r9tzvxWuOXTKz8hPYDtfMkdnhX-8odiojYVxVDRzmQGWU0EnS16SKLjOiU-GTsxPOz8M4owOqIxO24ofXK1FjAk8k4xGdxQjEo7ahZyp-D-pwwdI6sukN5Uqd1vOhPYtJCPplrWnBoHciGj0z9Q1KI9uzRHJ0o0pjY-A6Qjx5l4CxL6kbSWbeQCwmWVU76eVUMS7nnAiOhl8mxJ5wtdkHCKqhwL9O8cpIkbkZ8l09hY6Op6V8rWerpyN9h_RDR1jUnUsEqq46pf0bATim2wdsQ15F_S5TRFmxBYBT3KpkmACiYJjt8IeJz_cS8KZwQ7G2M25R9_x5LBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=ZKCxzsDsQOqnC2GkEXGpiQcP296YarNghfQRWQMqcg_S2_N7R8ZTpypz4_X54AlVjqpHh9ffS8nWpxuOv6WvMd62zIde4GX37OQIGPGr2gYnSSuwKmlQbcIA9lNWY1jb0wBENJwM4qIUODr8ujTN4aM2c896CiM7YaOKfIWhLK1d_jUSZ4rmpgB2KUEHvzWoV9tPPkq1XqwNei7oqCZ9yu6w2inXPAdLUa8IkOabX7DNh4ZGCg_QxgWEe7O9ed-mQJWgm_HC1JYJGwa7o2hvyEev6hDNIbCc-CxuST-BlkwuJiBN8tKpCq8S8Xnv-JDhzhWRVLH-w-5KBqlTHs9K_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=ZKCxzsDsQOqnC2GkEXGpiQcP296YarNghfQRWQMqcg_S2_N7R8ZTpypz4_X54AlVjqpHh9ffS8nWpxuOv6WvMd62zIde4GX37OQIGPGr2gYnSSuwKmlQbcIA9lNWY1jb0wBENJwM4qIUODr8ujTN4aM2c896CiM7YaOKfIWhLK1d_jUSZ4rmpgB2KUEHvzWoV9tPPkq1XqwNei7oqCZ9yu6w2inXPAdLUa8IkOabX7DNh4ZGCg_QxgWEe7O9ed-mQJWgm_HC1JYJGwa7o2hvyEev6hDNIbCc-CxuST-BlkwuJiBN8tKpCq8S8Xnv-JDhzhWRVLH-w-5KBqlTHs9K_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=rkzynirf1aeQ3XgNpXE_f1ySg6eCcteKZSbtG_ncoH5fSX6F6S9FMmU-1RttPE7hup8cm7aAykb--aRGzteCOdC_VvJjoqx54TsCwrowWucbolnTll6E8xrHFkYmKv-RK-YYd_Pp8MHIFHJWBQxBeJAN3kZ_pMI8z6OLAeclxgqknwUTxZb9er0RgY6fxEL01anesA7X9eSyire80T3CLU0FQXSIl3yTNbHEGEurg0weN_Rrr5E8QqqdhvGNlXV3yfsRL2G_smugUaYcJS3M378PsbPG81SbtX_0PAxvLSnKD3XrRw7PslYBlBsBCEfgbBMR-HZ6yvz-JZ4yTIkk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=rkzynirf1aeQ3XgNpXE_f1ySg6eCcteKZSbtG_ncoH5fSX6F6S9FMmU-1RttPE7hup8cm7aAykb--aRGzteCOdC_VvJjoqx54TsCwrowWucbolnTll6E8xrHFkYmKv-RK-YYd_Pp8MHIFHJWBQxBeJAN3kZ_pMI8z6OLAeclxgqknwUTxZb9er0RgY6fxEL01anesA7X9eSyire80T3CLU0FQXSIl3yTNbHEGEurg0weN_Rrr5E8QqqdhvGNlXV3yfsRL2G_smugUaYcJS3M378PsbPG81SbtX_0PAxvLSnKD3XrRw7PslYBlBsBCEfgbBMR-HZ6yvz-JZ4yTIkk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=e2tIX1Ey1YDcnYZdsBjjuOF18hdjqHLHDj7o8AIILVgPSiGLMH77KFwlLj9L3pt36fk3Jraw-chfNtYBdFsF9NkCOVdIAAb20rUYmMk7cXbUXP01i_Y-FqUv00QTXS_wttA2oWDip0DeIB2PHG83WdQ5Npb2OkINmjGp_FMu18HRR3UE34p_JuOATB5VhHAkZiH4U4YmUq0M9qhC25JExJvq8cmt2tBGi9DUZnWtj1zovlwC2JCR1oiLAYqXYm7LmfU2qV4IJkLOQsz-5XFbcVoRQETKaLRcz1NIKdoGpgxbLoJHEl9gvPVcbGL855XCXsoImaSGdKD8KeW3wQsGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=e2tIX1Ey1YDcnYZdsBjjuOF18hdjqHLHDj7o8AIILVgPSiGLMH77KFwlLj9L3pt36fk3Jraw-chfNtYBdFsF9NkCOVdIAAb20rUYmMk7cXbUXP01i_Y-FqUv00QTXS_wttA2oWDip0DeIB2PHG83WdQ5Npb2OkINmjGp_FMu18HRR3UE34p_JuOATB5VhHAkZiH4U4YmUq0M9qhC25JExJvq8cmt2tBGi9DUZnWtj1zovlwC2JCR1oiLAYqXYm7LmfU2qV4IJkLOQsz-5XFbcVoRQETKaLRcz1NIKdoGpgxbLoJHEl9gvPVcbGL855XCXsoImaSGdKD8KeW3wQsGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNErZjzy1TG5rPwvjvT7FLiFw3p9PPho10qKXw_A4V5JJnv0ZjJJJFbSXLiTDyilplLfsgzGWvRyzLGH4noZ0XSSGbZe6--c8lvekoqcVC86CA-TU75MfpbRQ6eM8yN5OQIb09X2LxChmsVeumUtmHQL5C6vJNB8FzHTM4hDoKugrcTib_shqX07Ws_xuISttjizP9GubivVOwD458BhNUkY8_CiYacLVsi3kAdoPGr5kM2arEbrulNpS7NXXpL_mH089TqfWg7ZsIz-7si-gMPVNA95pJmO4oHVc2PeDo5Z1WSj0JeQi30uoamjxMlE6BIdsdCzFycW_z5e86do-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
