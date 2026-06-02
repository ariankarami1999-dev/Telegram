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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 177K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 08:37:57</div>
<hr>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWLOSrbBMcT2kBZGR7N1hpOSyfZEgMOMTZB0VMp2VuaswgQC6w0iN0X-uLDKtLVZfWeCrx-ltZG2BiwnDt0ET0Q4OlBvHHhd9juKgmMWwcWqtdgcpFe1FPMlxNz5u9pE8lFbKFbgzngn0KRlqnRCV0j-dL89aPtvutdnc3q-uH1lyuk5-sL0j9SL9pSgJNyKWqKshTM16RmVg0CcZFAem2eh7BOPPsI5sAtzeulRuJ5X2UmJlTYWgY3Y1GHZRITVVpJXTohjv6N7g4zvh17imoRNPzKIbIFbzmdLPfp2VQq4vKHY5yae1oio24VHHVF4ziHhvc_huHKFj8ycJBR_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7zhLmB6tn14c0cGwfWW0MMWTfHbUu4dx2AzKZChs_Qy5OSbiwt1ofdmzAgYQoPpGtr8UbMvkFNpBnTDwV5jrwkA02900K6Ebdf6y4WGScSfOly4CQGaZANX5dqPjs4ryqe65_seRtyj1fMXagFybx75a5UUUfl1GwAq4FqVmFyg_DqVi_x1L0mN71laLViUsK17prLZ1kMmB1bodgP4x5_6aC08csgzdvkDldGti1H4OH_l3Tyld1EZzSZCTj7Jp9CYhHVV89zAC6ujMe3BkwWJP8eZrRDbfwrmmC1hHvTp8Dt7bnKC-_ewQbNh3xcxoAg5TtApjkKlRarQSIwFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GODitzD6X2KR28rcCFUdzGd5l5CRVASmL7GpPOksPfUFRMbjGDhHS5UwEYKYvPTh_sLlFfg1H0dASnCCvsE-FF8SSwUQ4GrOPxe-qDcDstdrW1kaX0PlybEDY_UjZvr58Q9hSslFqj2UbFKlvtSMHCQ91HyGsS11uccd5MOG2f-qrwChys4k_5AmY3RVLkeDkdhAJCuyrbM1UBIRaV5tUGaF7iLWM-8_TdHOdI9FkVNXzD77TJLHbgf0Q1vM1opAhrHqM9TiUXz9qu6_vIWz_7Iu5Gqb4syFOe-nbTjQpIlEWTnzB9_SX1zAGL1tVBIhUnJlg41BWeIp9wjr8ElrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTLrNrn5kg9rEQYHFjR1NUFBFKmgILwSWBUI6DYYXoVxwx-0LfkG2qjEO9CbO9xTb4c4yJlUINNJsPl_kR7Mz1CSDRrZSqSuips10Je2e7_La7vxmnvre220SBdDQkJr6z-L0lBI9e5mg9U8DXJr7B-wmqKv1O6G-YYsE82ZAz7HRCoa7rYBL3Y3DmjsE9WCwcOpYHqOhyvOtQLBYH0yqqcY3cQFjzXWiph_73j-XAU8T1Gqe_CDbqpjH6dZv98V7FsqYbQlPxdDGwcKA-sQTGxTzjTs6heWRhHHJMsh2jPDl3Q4gBTj_gKOqudCEUBbSPtA9liL2dUoygtAUKsfPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyvnmKD9wqQIKN0cBByW4g4qrBGAP7VY4vO-S-tWC41gU34Ymbuu8eOQHn3xPl-RkVV_ZKMQYjKZkXQrWuwO1qJRFIUzvZcYqQBHXjtK1dZe-_PPIJGgzVYUhQjx1BdkvkucBSr7xhbv5mkjskxV0jNW-2pcwz9DOUoM_tmZpcCBzc7E0CiNN6-gzk7nIXGSpDEHlqYMcvxhd4pFU_5JPpsVjj2H1QWYK7XTjmX-3h2xICYXtZHcWFAd2yzP29ba90sNrc3jrJXZpGWaNwC4__i5DXusrrGWFiJI5yF5HHg5Z1maxKqGPd3tZ_EK2QxvAV2ieXvAiURs56kGDBFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=g5Ml4JAU2qmeZFVeQLJRLHuAcAoTyoWEFvP3k6wNmW6o2x_nIKrv4P4NY0xal84BDtFRFhqUnMniz0kdOkTvS4AGSxUqMvj3JbutPwkY76j-GLrL-Nwj0Tri5LC-4a0fG1XhuUxEIuk-WpUleyRQnJtldwcO8Dko7j-2mIwIY8TVTkudSrHWnSV0Kjv1cY093DQVh3a-q8Udymos1BxjagPKLerIudvrebHOBc7vzaMb0IFFOz8GjyclI5pAG-p3CVGooN0wnk_F_rXWpXbM3B7HURg22YptPrIGhIsrea8kbL8hrG6tf6L1S6rxw5adpnGRlPnb1guQ9Ehfq7QOh1Q7TXFKrzfeW3TlYO2u_pbS5i70XAK3MSNouY1sxS5lfLmSaVF1MyfkkWyoThxsiJcXIFA0rfuhpGyfnnpS7t_h5D0tFv7lMW-SxuZk3HWeTsanmzJwrvZyZoH0hTGlg9njF4qr0UYuG6fxRN-vHWGr8nD1ISW2zcLgT3zk6q-DZcC-KnO2HGu4VxvzKvmbfFBoOfFH5SNIDrxZuqZMUWT1aMePZcgWoSqSkkjvDkZp90eI_ctAZsbZts3H1cpj4DUP7YxXGjcnHNGlqe-xYk1466vuZt3QT2DSh5sK8O-6j8cwttrxQGzJJvtMeD89bYGu9ZdyymgmlfusOY1xRK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=g5Ml4JAU2qmeZFVeQLJRLHuAcAoTyoWEFvP3k6wNmW6o2x_nIKrv4P4NY0xal84BDtFRFhqUnMniz0kdOkTvS4AGSxUqMvj3JbutPwkY76j-GLrL-Nwj0Tri5LC-4a0fG1XhuUxEIuk-WpUleyRQnJtldwcO8Dko7j-2mIwIY8TVTkudSrHWnSV0Kjv1cY093DQVh3a-q8Udymos1BxjagPKLerIudvrebHOBc7vzaMb0IFFOz8GjyclI5pAG-p3CVGooN0wnk_F_rXWpXbM3B7HURg22YptPrIGhIsrea8kbL8hrG6tf6L1S6rxw5adpnGRlPnb1guQ9Ehfq7QOh1Q7TXFKrzfeW3TlYO2u_pbS5i70XAK3MSNouY1sxS5lfLmSaVF1MyfkkWyoThxsiJcXIFA0rfuhpGyfnnpS7t_h5D0tFv7lMW-SxuZk3HWeTsanmzJwrvZyZoH0hTGlg9njF4qr0UYuG6fxRN-vHWGr8nD1ISW2zcLgT3zk6q-DZcC-KnO2HGu4VxvzKvmbfFBoOfFH5SNIDrxZuqZMUWT1aMePZcgWoSqSkkjvDkZp90eI_ctAZsbZts3H1cpj4DUP7YxXGjcnHNGlqe-xYk1466vuZt3QT2DSh5sK8O-6j8cwttrxQGzJJvtMeD89bYGu9ZdyymgmlfusOY1xRK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzlDi_clrk03lkLxkwqGNNDjiJdbf9EnTQmHFPo83Tww0SYQh_avTwshLhP88CFvqtmzktZfqg1Pw3vFNC23InPVbGt1E0KV8zyg3S0qTJAPIF26eFc0mFOLei_UxxQIiUL8uL156WqmszqhAp_3SLksMrXDq9bb0FBaH6MF6QqT_nwFCAO2t-oZfd8pwPAkiA6J_ZLNAmdDjPPRGGWITi7FciXGYRRPdGnifsmS9suqOTz8heTUVRIxqq56WGD14yUPegbuiDAaXB_5XhvyjRj4a5Mk6kT-uvRa53yb6KhcZd03J6ETswFEM8t7_hJuPGdU1mK55KUP88Ii0Tjrhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
باثبت‌نام در‌این‌لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a11
📱
@winro_io</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22639" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1dtHW8VMVFsF89PWJJU_RwtBAo0K8iEo5NK2bI2qnb5fE8tHa-9_u25r_xZ_RKdcs-MjaM6BNZZqV-m9xCsczxSRbP0kTCewANbk3WnSK35hfNH8Ws4-QmUkfTkyUfpRZ6cCQnPcqF1aQ7zLvVqUSPxHFjHRp502OoOWX1Kr6vNvu2Z7xrv_aIWu7i3rp7g3NrG_Mjhl11t94_7d7CnyoEZewgxmXRari7BVsi8o6hShQM6M8hHaDPpbzBhdLhtD_7ukFosFtiYwCyyv4V9u7h7oVmJXt-gJESMqUM5MlIkr7fci3yy5wMV7c_l2BJBsQSOL7D5UAvlFoI-B8fErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjKyGkH1w3cSDTVPVY5tPhu0P0mBlEV4svmTwSulYy-wbwNHQhm__-B-Ivy-SBiTilQ5008y7g_vtfJiI_NfVyaERD0gMM5lFoyy3x4m7BQX-cHPJAp-IjeTwtokr83b_A5Mfv_TG51G207DVXu6Vuyvw3X7vo_O61eXeINTdWGKeK8zsx4Zb7vmsRny2fg3kmZIVh0FDswGcB--kenbx2IOW8PeAwuXFlcq4KipovrkzxWvuX8q7F1mAF9P1sgJrmzsdYdNxtH2BWFvyPh-p8EEKVCq8PbeCjp9hSuoPzpwfVSQ8icehmD1xmPtzSBmvnZfbWnG_jyF080Ycldn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=PvU7tnK0RL83CMe61470-wk_-6DeFVeXN3Y_loAnSR9M7UC_sXSVuzHhirGB-SGpYPUoXbC1UHX6HjO1yYSSYRaVm8Hvox2k8BrND-Z6fdItheJt0YXG8slFdJV8IJpnWm__Xh3PenYhO13kTioVJc2RqO06HSt3Vm10P-0zPjs2YhOJ9dLxawSG6hs4EZHl_0UhDAxyHrzcVIt1ariiH6RN83UQmyOeZ6xr909h3ofZPdw7JslymkofPAtU9QR6fq0X-vYdyGoSA60tZX_KiBPVeO-InhUSRBKBqxic8x00gX5r6aaJPOGusXpQ-tddYqtu4koI870DjpH8qlD0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=PvU7tnK0RL83CMe61470-wk_-6DeFVeXN3Y_loAnSR9M7UC_sXSVuzHhirGB-SGpYPUoXbC1UHX6HjO1yYSSYRaVm8Hvox2k8BrND-Z6fdItheJt0YXG8slFdJV8IJpnWm__Xh3PenYhO13kTioVJc2RqO06HSt3Vm10P-0zPjs2YhOJ9dLxawSG6hs4EZHl_0UhDAxyHrzcVIt1ariiH6RN83UQmyOeZ6xr909h3ofZPdw7JslymkofPAtU9QR6fq0X-vYdyGoSA60tZX_KiBPVeO-InhUSRBKBqxic8x00gX5r6aaJPOGusXpQ-tddYqtu4koI870DjpH8qlD0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvTQA67cJr-m2v2QuE2OK-4yMCnwZujUKvQ8PK_f4IxJQ9Ig90fkYrzhLORfu_jX9J2nWZs12Mqfs6WbC6zLco8CgKx2ntUbrDstq8lhUB84AfXh58XbcPQgPOtrUAlezKrSPfF0XLQS6CPgrvXNV-mmqpjzLe9RY5y49KKZ_HCCC5zKbW0-o7FmbR-i5v6TJf61F1zk9sPksYlWJJTZIZoR2QZubFBcuX66lGqdFw_ANWxwa6QbCYkqfolzV_RP5oxBWYmg7-uN1oM4FjQj3kvObYWKY2Omezzqbv8AC5H-34ielCdyTVR4XIgap11wA5btt65WqM1bKwV4cnKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ZlrpQhxMUJB5XFS2eTgWwD1vZSMgsoV-5FtTIEtzCvO6pUn2wQwYMayCI3LQGFN2kkfFqxZF5oBP-41qfSWUgeRjIlkzBsoayWKJHAg6Elavfi5YIShUM6Ndm-Bwyr-prKXORscBzuAYX8zUczEcEHS03d75eMokuGNkyzAlWjgFV4-9MskCyiXuEdDPU0pdXJ6tZfsp3W9UAdW4xMCyWM0RHWMauOcDXorfXJk1xscYqv5WcOIo2oB_k0-vgMFi6XcH7-mis8TaxCZ82cQJ7yv7eVkJVlZpx1QzF6tfEnoLj5jHIpaVb5xhrmRiRItX47-Hv3ckMODC9v9P2jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4576fhAYUxv0_-4pRiJxIHEqRTUA5tqv7ad8uAI4XDNX8ch2yOTrOyXnYjNfqP9Lfx1XiM1FFKtRDxQjk3yRhml3N0GhrdXRy_uNovgEEiqU1aPEpg5tMuiDQW2bTnIGgAbcL3ey-ptJn11QbMLFSg765q5zJ6VAdCnQSWHDV6P1MdaNTPIL313fnMJbjThBv-0mEtmBV3FKbut6mE3fMRExm44ngqs71FlpBWuL78ZBEXbAsy8qNAcKtC07QgOLPPfqfgYTK1hv6ou6Cnv4TXzNh5WTySyqRqWc044EdbTtSL_GGxWYrshUG88y27CrNOIq97vB3NNtwuOaoaU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhpB1sWc1xYlWPXwGeFG49gWd6xB4TtXyCxlU5-l1R0EU5BSkE-129LuEB0vypQGO_7FPQGsY9x_wiBKy5PrkuShYpi6M-eAzyjJV-E6wnjAOto2z1uzLu2aPAs3tbKdYbzuNwitiyBb9H8PvZqLEVFgJAbe7UJCwpXnKv0yibN_8vnWNxSPfY-G5c3ftERnwS350jrVaNBqOo8K0uT_9pDHMFnqSC4sgsNjrmEw3ZzPIin4eruXX6BV9o-gchtq06EBP5chFVLWqBes0Lpt6CQQZ6TSRicBI0tKXJH0t1Zgamy5VTQ_t8NEuadUrCK-Xmy-ebrvdo0CQmAcKkOsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔑V2RAY-VPN🗝️ADMIN️</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiJlXQ2Nqtu7We7c3aexc6Ls10_FG6N5xDiiDb36liAS-huOBGuLCrQq1Q5SLlxrhV8_jUqujovEf6nQM_E_7H2y-6rHLK6ruejCwaMhOM9xT6NKBbBSli3XGMb84NCvgPbhA9YD5NGBnXOmSn5SCETNn7HQ8sWHIfkkw0RaRlByjIi9hrii9aM-lBJ87BF1RTCXvXyMMCqjSOvMcTXvzNaSKYA3eZVGTKEqtwrMmYaQ8HAQX-dcKUUgN3yR9nOY3Nb-jSC1PodQvobQ1hYtL_3PaWUpqEa5IAb-iEgq4YOZMb5MaEPYqsUifHf4WUyE4iD6xEx72XfDCd_pn4oRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
سرویس استارلینک واقعی
🎖️
💥
🔝
موقع جنگ بعدی،بلافاصله تموم سرورهای موجود در بازار قطع میشن پس جای معتبر خرید کنید
✅
✅
🥇
آی پی ثابت و واقعی استارلینک
🥈
پایداری تضمینی حتی در زمان جنگ
🥉
لینک ساب جهت
استعلام سرویس
✅
بدون ضریب با ضمانت عودت
➕
سرویس
تانل و استار موجود
✅
✅
معتبر هستن ما ازشون خرید میکنیم.بگین از طرف کانال پرشیانا هستین اولین خرید رو تخفیف میدن
·• ━━━━༺
🔗
༻━━━━ •·
🛫
Channel:
@vpn_artel
🕹️
🛡
admin:
@Make_server
·• ━━━━༺
🔗
༻━━━━ •·</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22627" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ax3W7fdpQ-zMR0HBfRmSjxd8QJjwhxZ84DPZ06fbtzgNsS4jxIopj4Y-hkZ8ftjw62c_i9kQ5KdWzND6zHCJf6Bv0h_ZOXkkWRPR0xf7CGLTaT5xpjYmIkBAFXplhtnWLFuUJakSTDwqMfhdl7Lrv9P9a0rQ_NNYXM_uLbSDAI9obSu2nw9E5H-qNLCSFHcT4M0ISU8DeKVxo95_clTmPcdonrd1aIUwwyp3CxZHnCmYf0i4JTHAleAXO8NRI1fU6NyciuXYoYEQ7OW0_QnwQ-fibHfCpd9Q_C8YRX-p59yzKuJtbScvSjyVKZSyWPLxaw53Jk_ZiRLD-sDF_Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZJzVAlZoJZzCgMpuAC4X3NfTMivdxdG_e6_9bHc_UTUPsmZzfruZslHNxhrsFSZe7fr1NRERJ7_S4Liw-lKMJ4zNNBz7DzmtNOIYFTGU1GGiko14_UlpYioILFVjfAwBC7YgVGAfEHcSkQccYRTSauZRgdsPTwIiz0AW1FqhUtjT5m61Fhk9fCQywfUtAfClA_IYSHHLIKLhX6bCVKEL2rgB-lHBb4NnXFS4etBSfkTjiFTO_CKYJ59zBAadwnp_5kFLnmBFdSQDVWY2fDOeuc5Bsn8p0MCj5v4y1TKUivzGsEimEu98WrdvfP46r0gW4ClAzS1WgItxDXitBbOgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-k9zGWBaTw-stSjq-M-NiwPTAb5UH2NfG4ZwQQsHCX_y5q4XmZFPTapRjvwY5dgJYEBPgm44iidXcXyHewwiZ9RvBp4tlWKg4WBr5RVytl00gEBP8uxoCElHFHogObK4t5He8gE9gMKilSN05XxO2vZRn_mO6p3AimLN-VCEwub-M2XJsIeMRSRHzhSxc1AUuUyK-bnQMPN3yhTdZhhiasm2_qTpKdbsQxSn8HAiZkRXW68aLQHMjOnv_LbCLMhBXgJCeZj2OWI2qkxnQbSXxGJyrS6iaZXRvXlDuWUl1s6dR-X0d3TPp7DeaCwvz8YTTliVWT33cxkLRVXvVxNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVNsB-fNrSCzAXOWlPISA5S4YQXEpWr4f1ME0SS_XvwgEO-SRCMATIJ3--tBwHiYNOiVWqg827Qjvaqm2ys8Rn_itggZ5gAS4xgD7HsiHZeDWzJVndt_arsrqo8g34aa2KRTrDFyv0k9YSNzVZDtMh5XED_i0qBc79GNceIspV1XobQXPkT-ixNpHDj6_xLN7VaAQeKOrPogobIGjJXEzkd6OgPWvh1dCHL-DK-wnUOYrgBdR93k4Tyoi9VGS7FStVlTBNopLNAjNGdUrL5rWWuHaX_tdUm_Y5-6qKiRqf5VQdvzDDNGjrCdBN64Qn51ikOiHh4UAHuF0y_sZTXecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6P4e4sMLT2jqpnHE_7BAlNGAv8HsuqDHVen1zj7QnuUYoq_YvRA5Q-uoaAY9chY4mPHa0nyxS8HqnfwmSBiwQTAxsc-o6jeVZozWSmChoKqMSinLoWGF6Q10JJ5m_97Bil8W1YubdTcf634mhCcSYHtqmO9qFQhIZYPTxmYtHZ4z_vF5KzHnCJsEHe_EPOUtS_4Qs23KSPULgTltgSklSfMToP8yZAJeOLyftFBQQ48lkPIULDdeCXEIZT-GS36iZG_e-M2GrmK-RHoKViFhDbZw0NUXP11glKYaycVcpd0zvbeUAFmB-QH7rAuB8JemtOGNB15O1P_Eg-Fdsw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVBDLvOMun8BJmxklwXxFKc7G5d4nsJP1kaGC5Y5FS_961hwYPj79x407SXN8jWn5-PqgdqJ72FRgZi5hsRAv2V1qOyH3q6DEbNXEHWDBNr8AriamQE45v8N9CqqYrbB6m9YkJvrDovTpyd1o6YXRd02uip4WEV82-ixjGZ8vrJQ7q0VrnoPrT4yU45S-ENzS0OXBTWTmmM94SXJo5c05RF3Ky5kJ90kzHxpEd7smfY_c-8KnMk-mBJqFqVqao25eIj63ApGLc0_LdUm4ZWC6voBPpJgWgELQDUeD00_k9p_jW5GJuFYSuOM76H_l2N-VqWM6EskIvquzC-5UkZuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpkT1zhZdySiKQk8anZYSobG0fOlAejBtp_tBuf8sv1bsL2M3dsrIjd63mFPoWK5z0GvMi-XXehTXN6x3Z4rCemWJTk6ncFVMWMOsCkjMsqGid6LpggueOKEvQkHXhe8XwTQmv6c5cfwi70RhWmxk3Avx-Lkef3iL3jgAstmwcKUMScSOXJ1V5e0c-JGpAhaPxg9QOGfxfM8AHtiZrDijmue2NQdUvoUcNS9gP-qasZvhT0KVbOYB5yheBpVTUGY83US0wndlFVqH99MFNUT2CIvkjvRSyMcGbnjPalbzOEsKLcd3cSnVz8QCHrUmOwK1Q-EKI-_eQZIyweNf1Ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=fLKxDzJesskgJNY_6clZgvC4ZvUoBDOdOJDvX9tBLE-FLlil_EK84q2VrUU0zIGlc8gg5lwpBsHY4LgiI__KnZzGUwUtnDJsazBTTqlJuHYuDew5v96JthHBI5dEhMvE46OsKaRvYCsK95XF0ZXPeiVFg7Or5PJ5VM4poSF5kpXdfvpkoVlsgquUYMf6XdP94bbT8ovvl5EocZNDHriaGzhr719YZ8twJRLqpzzf8kkyToYe04jO7TAGy_ut_aCnuAHoDDuYTII1zpcIHquz1ZhlVXevW_DmxDFhw28vH913-eOct2Qspjm3oFma1xmpxkWFwkakhfWt071A3s1Ntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=fLKxDzJesskgJNY_6clZgvC4ZvUoBDOdOJDvX9tBLE-FLlil_EK84q2VrUU0zIGlc8gg5lwpBsHY4LgiI__KnZzGUwUtnDJsazBTTqlJuHYuDew5v96JthHBI5dEhMvE46OsKaRvYCsK95XF0ZXPeiVFg7Or5PJ5VM4poSF5kpXdfvpkoVlsgquUYMf6XdP94bbT8ovvl5EocZNDHriaGzhr719YZ8twJRLqpzzf8kkyToYe04jO7TAGy_ut_aCnuAHoDDuYTII1zpcIHquz1ZhlVXevW_DmxDFhw28vH913-eOct2Qspjm3oFma1xmpxkWFwkakhfWt071A3s1Ntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPxLQHWSX7D6ck0cYmmjGIfo5Tqb4XbPwUAD3xBCrAWp4luh_J3AZa-wuVAcBTZMqoF0qho2SBfgmZxSJvCViLkfxILzR3wekPUYj0L0bJBFC7AveF9uS6VvYcXJdKBsNmsnGmRFggEmVlV-mkMnjWrYFIULLfgXp9_t3lkxMoP8Np97PLJT1SQQmnGVy_o-l-PKZXMzn1RQe7QQOipm7WxtGEkdA8r58ofRyQnfIyySmTHoEX-zAjrjnUrwbwBUP4gbn89AUVt4hzMAQHR8ZiHlFoE8Nxfqsle6iZZ6o0ab1VLHRNNPdDnSxEYEUYragr4dFbsKLp-gLCsSsrLiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnV7e5B5XFyspuQTtklCbixb0WYriKHY4JdYU_WXAT7mmTTRDHuBxkHgcX4DZlaVc7FilECHkGWuVL4s5kbZTAJl5SXey9krNfpWFCiQo1nBLCjP0d71pFwSgNI9VlTYUUMd90VTvi6FEZ1k1pHgV-7K554NarLI-QUzrAPyD2flnLQ-FtoLMvdIu9OC20Aa9WVFxFRhcAbRV844q-lrwUVBgeVBfROhxA2LfelFtavCSmzbl-m_ZMzKYxKN-ZFd-NfoGl6vU_Orxl9fNy76TbFdo9Rw7TvO5a6OweWTE0ldoxZUWvjnVdY7bVNvkOlAz541bcRQhAblEWbcWWApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjCgXEGwL0cxVl1UjbBeL45JH00BVtlQfQzDwvYjbxSO-ZxrVEDuPDH22JOElrX2lRSIjVwfJ6ZWAjJ5_eiEuRRyUAXIlxJbM0G18XpDD4uczL0xp56fxbb3e1kozq7txcbTZzATJ6WX8uha7dK0Jvxrj2AAiHkJ2mLKq_76IDlBLlI7ByH4gOtwzsxtHIVCr8bStWMHATiEBRoFL8ayssgSgwr70NaXrVD9w2zYny2xrByhgoNZcRj7pYSwS3R0uxivFP_F1fVicQEAhDZOUVGVKoxcq7zVQtoGyzAek_HOtyDxmNPLbjhJGZINnbH5Jk0DeVmjD0VhVXIxVn9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWHX7F-2L-PMavmcDyo7LIqG0OG_wJsFbX4bKshDoHBhxxQTNPrhmUa8VoX9ALP7Fgp9j3K1fO2a_bqDMIuizrl8vrXEV3zWf3CWslOSiZE0DNbFlFRoHVeNfQpLWhsbtQOwKFTnsycokOfd3Np4_tOQm17niUQ3fkta9nASfyhfvCAVTkhVTQNWj9v3xEdu8C3EBCmVbKYhS4XCCTab8mpTLU7OKhOTwJ9Gu7_kyBUaHEGZ9WpgXd9tfJk-u1h8g5OoFlP2OkEU0_T4CuyE4w8dkQ_JbVU8nGUAHu219_tBaZ8LdET0WreaKSt5dU8PebokQaz7ZVPOmZwh1de8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilL9sAH4jZXNqcPQgPMj5bBljx3EQqzE8rslRThrmEHw1j2C_NKOz-iVqhFzvgC1qcIC72hSoBKFQDqrNWOBNIXkij0lkyyzdbiMfxyU3yIFiAdp9_5aSMYudFZs5V50IwoJSg2AcFU9G_NuN6USITdSH8P1tcFoNpmYmAZaMg5S-i54fdaTrlkOrf3pMAuwL5wxJf8l971tJa4c26nn88-aOgd2mYnbmQ9UTtR3erRWhBpfzVUggsQz2PtwhXIpr8QrrwkjWyRAaMC2uX_vppY5H4RGCD2EU7OFdDLrejh_qe_ah15198GZcHSWPfvUJ6k_5_G-1V_lb5IrQBe_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU4GYgPP1JaVsmISPk_khWNCBE1PRLUuyCRDxT9JjpkiSw-Wf3rzEqiWGa_8Cm9DG0DngIfth5xTdMIPDi25GFdJ-KjoyJs7HFkrBnOsnNk9pfClTVmQL90Asu0iAZIRJOytxySZdBfd6Eusdp2gL_pJxNQr2F7s6VaRoxraWUbNPjB7flkEkRNi7xt6c7KrOox2z0Us4p13VzZhEgHj_fWTRsgtiYFGxb0RiJUhHpADkStMa832Mp4RRginZFNObSqRPowK8tj0MfOJladMkRZGiOxA_CTXkYOioE4zeli-aY2h9uVQw7Eia-_k63UDyVd5ce99PmM8Rr4pxbxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dip2crMiWFBTlMNz-TVjOkkeeG7v8S8MndOHcr01_Gzp5JEk7JdwqbjUb_LZabwHIYuGzcvdpliF8GbOO0DK3bGEYtIisORHWtPSidiXjeV96J6A_liIYEAOKCuEQ9pjNWDate2l3Dl4caXVPkDq9AsYn3F91GKyJM7kbnJWcBAlS9FdS-MsdfgBQGQRDzfFCY0D4s8ruWVrWHZEDKA3Puup9a0T9tGbZ8ZQfDWhfE_LzkoL_kohJXXW4q07o2sBP2FKPS_xddpYnfBxYQrGlwNMEDRdVg4J9dZwNC0bc0pdJAWXVSm2Bis9a6uey7Jlq2cDIuT1WYRxJ2bi6Ppjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYzAI2BCov-sGmFLa-ZzL2tQzz994ePvCvG7Mr-Nocv831hBcQwvU54hdQeIGP5rHOYfZ-1FConZ4RTX6el5msZHFKCXSYw76xKTeijoi6T3sbu5aoqtWp0kRKgNSfP5ih0T4jEj8kzvW-CuCFu6vr-gqb5fJuMWsvA_X8UHKpwDVUzdxRduqnfvdlxhUuuzGEI75B0eNZ2DNw7DZfoqZJ8QrWYK8ENaRnk7PXzKQ3egrUS116_qau56R0epiz_hG5KIAxgNl568hczSzrUCsVLTeZz57soI_jyQOja61koXJC9XBInyJUkymSKZSnZzL5YQKoNxLWioms7psPR9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDXj_JAbw6OtlwZr0Xf0ntkZ5dL38CgpjCAG-QDCix7Q-o0wo2yk6dZeDH-JXsPfOBbfz8kmcmQGPf3UJdzGAaTWtFxJfXMrrw_JBFlk563lS2HqPn6VIYpqqwxI-iznL8xddlpSfbhMmtF5puCQ-hPsJM67iH6TuDqqh2DdeCIecEvLKH-8lATyeNa4LUacMK1ZlET_NiKZ44r7N3tqGUrjU83PBlg47QDRrMNqE9Ega9ULvxHxbeUnftpxD7ahjtsyNR0arhwcdL_OzsobtQRbDp1jRfFNXU7MA92COQC3snQm2PTMeDrNLdKJWjX8O3P4CfQMICvUOe4qFAf_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfD6ezEUmstnKEH8WqRX1ZFgVXGG_J22QDpUInDFInDm1UcJrm_luN40od9t3wrdvziSXhA9Xys8y4maqwxlBGSoUjILTrwq0gQwbnIjMVzzAo4-N09z6hoW2k0Qgyt21I6tzPdL_sQzKLGnlCyqw5mipBbNwAjtk0r3CHS3gyTBShFeiAAQvmvAcDOeMCo0hPCUKgBwFjBc4BHaNR83fDFTgkNrAOTYCdqZZba9huOquKm2qbnb61rJ9xwgo3vEP_h56FXFgp0H-JUQHE9f-hdhTVF4kyKNPaVXoEJOzdjXioA6rECvLR-avjXDs1D-pHjwpiz1M0vAFnJY40l2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=fFcg-t72Lyfc0XGB4wA9SKJGQCXUF9ICSGo071vgskIctImsAd50FEHYBXReTqRsfJvorlc1LSXeZfGIOPeM6ZJ_69W4RdY6wyltOGQbNe3zYsBX_FQJZb5swIOG7SkhOjY95hd_GCFzC5GJ2FUf-oa27h8NrALtUJpR9KFDGG0VmNdZULICPWSv9qHqe5h5SoWy1TMUOd87vFlUXiONNnEkoV1aa4u07nyuoD_0Rp3OpT3BH0iVs28KiOwa4I6Ze4ctuAOfStcNUUxHWx3aKpcHrLBI8Zr9GhsATVQV7-u3XUlxm66USstUy1t6PRIVmxxBPyqLVZQTFUJp5ZbUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=fFcg-t72Lyfc0XGB4wA9SKJGQCXUF9ICSGo071vgskIctImsAd50FEHYBXReTqRsfJvorlc1LSXeZfGIOPeM6ZJ_69W4RdY6wyltOGQbNe3zYsBX_FQJZb5swIOG7SkhOjY95hd_GCFzC5GJ2FUf-oa27h8NrALtUJpR9KFDGG0VmNdZULICPWSv9qHqe5h5SoWy1TMUOd87vFlUXiONNnEkoV1aa4u07nyuoD_0Rp3OpT3BH0iVs28KiOwa4I6Ze4ctuAOfStcNUUxHWx3aKpcHrLBI8Zr9GhsATVQV7-u3XUlxm66USstUy1t6PRIVmxxBPyqLVZQTFUJp5ZbUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=q-zxIsz5agRBl4FisbpowROtTlh-0FL_RcGdxgFfYtsleEuwTqCtZCC1QiJP0ptyRgRjLsXRn1D1sLpVvDXXoxnadmllHHdJZaUnPvNTjPjTBf1TCwrDBRIxsxYrX09kOoSB89kKKU-hCOGxIFufih16d86gycQFyanRUF7aQ_a-lc1oGpZjI94-b95jNBVo4CpXRZ3ID6kGzg7UXd5ENUTHWZ5Igt2n__63T8pcnqTRtIM6v2vdynvHHBaCuUsJb2Tqqka0OZOvhtYEO1eZd1Sq2stezcnu62tYVZQgdcR9KL6-VauWUqpyWrn86NgOHska2YeNpJVC7w-FTwFeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=q-zxIsz5agRBl4FisbpowROtTlh-0FL_RcGdxgFfYtsleEuwTqCtZCC1QiJP0ptyRgRjLsXRn1D1sLpVvDXXoxnadmllHHdJZaUnPvNTjPjTBf1TCwrDBRIxsxYrX09kOoSB89kKKU-hCOGxIFufih16d86gycQFyanRUF7aQ_a-lc1oGpZjI94-b95jNBVo4CpXRZ3ID6kGzg7UXd5ENUTHWZ5Igt2n__63T8pcnqTRtIM6v2vdynvHHBaCuUsJb2Tqqka0OZOvhtYEO1eZd1Sq2stezcnu62tYVZQgdcR9KL6-VauWUqpyWrn86NgOHska2YeNpJVC7w-FTwFeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av1Fo_PKRo6WW-IZedowJjWGygca4EXdHZa27Jm-UwxbDfjlKDQF-DAQuQo13LwrmjE1i5EoRTMh-Hno6N0c8PhEctUoNFkFKolv43pp8hXXFCefFPZmY8drJI7q1OtXtDZ_JuKLaEoguRXeKUHsHFURhO6QlO72RkbhmVV9R19-VTNlwO6UgnXc9agXArhm5Ct4PzVzyVXasXZZD6aVSxUxwkVP8ZAwebsG0UhN7Qz4vpFbOSyRhGxDUQ_ZWAs5RQrJrnxbh-_Q6IgcmetRpnmpyhqPXPS-PCIWs2df-9Nt1VsIn6Tu14Di_t1NgwM5ejIirgYfxsErIfHzbkkmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=stJBY4RHNDX9FGksZaRIZe4JjdOni5kCPpRLhyx8SAdn0lQHjI3jr4K35c_mt9WgDWbLmE-g6se3UUaDzKgMbZ3BtC6cFPmPSPfAEP98J2PilnXMVZVWL-yEZvf5hRqZuuOr2h3FzVhlwVYrznXSQ05pibEUIdyJpv0eXf8plaHv9H1HZN9b0q7a1l_ioRuCGIeV3Da4kQURIx3C0D3sq7kBrlgj9WPRxi84aAelGXyyqXxoffh7C_1yDlF0EWDyNVLKUcK9zd7LgjSb-tQsCgxYO_dAgaNAy0lQ9YttbloRpX27nrQbKActRDD5QabMvZEZIFuXKg9rX0BMZjseuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=stJBY4RHNDX9FGksZaRIZe4JjdOni5kCPpRLhyx8SAdn0lQHjI3jr4K35c_mt9WgDWbLmE-g6se3UUaDzKgMbZ3BtC6cFPmPSPfAEP98J2PilnXMVZVWL-yEZvf5hRqZuuOr2h3FzVhlwVYrznXSQ05pibEUIdyJpv0eXf8plaHv9H1HZN9b0q7a1l_ioRuCGIeV3Da4kQURIx3C0D3sq7kBrlgj9WPRxi84aAelGXyyqXxoffh7C_1yDlF0EWDyNVLKUcK9zd7LgjSb-tQsCgxYO_dAgaNAy0lQ9YttbloRpX27nrQbKActRDD5QabMvZEZIFuXKg9rX0BMZjseuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4WsvVRK8OiBYftucCgOET2bOYsjKZK4dmqr7hQsQKNCOrB9RqvjFM5BkQ_k4f3BuZyDGU_pQa32xYGs_cwKoHHl3GKS5_2zzs4ntmkKpvmS9j87MnPal4-4xLbT0auzisGWCqHVHrkbDYqZOutRfnYnrr45mF6jpae8Jub7tgIqJIo3GXz4GBW8M4jmfeGY6jN_SX7cBMeTKZ1bGI89gKbGP6osp05NjeYYdHzbcpgonhczdS6qjyddyYTFyk7mPXa4bpVWFzICqiwkFUGOCg9qCFdzrkuUpTtzL6C4kTQMQ6G9Y8uSU-bPnB_yPQLGTudJmsT6rtdcnfYM5DY2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0hi3h4e1Iay1L4hUN3h5ogAi72DtPshfGg_Blm5vRz1kVy8zYBbs5NA1m3pB8YrMJuqJOoUQTlnXsmYsOKGFrifgDw1z0C2rY7jpoSabwFKOlqwjsn7KqxN9qTLJ6wttmXZOvos-xJn8F7H9sRb05VrgKg4oq2MsOVz9KSnZyF1G9GNNFLWX2vd3wjFQ4bt2pD0QsJWWL-zsCScPWVpMuiI4t-7X7OOtksp4QCGNdRQTkDJ-LWWiN0Csh58jIHzhAeDYKtlJrnX00VBrR8qhkyOvUA3LmXmPEJGrpi6hCUQ-z8LO0fZXFgyrRKIQoRxrYmdekmjuDv00UumaaHweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=B7oTTcVjunAUeUNJcbZ_qNyfyWABPKB7wN2UG_KVHe3EVkJPpjeYcIo12GruDeN6GVrL88xc9urWGplB67sx-yy7PAv2hK6krGOh4I9Wc2gzjE0wAUa4kDbRKXoIpuIXv-3P-ys3kxMOoxq7fm4SOLLwWsrOPTgF6rSiZDxoaaRSZfqvKZtLh__I1vSd7WpJL3AULsnE9URkQwGja9944bfXM8HhTZw1fuoQIF2Nb8hHIfNg-1sbosoFGs0NTx_p0OQXCEIlS32VYb1rVPUVsFQuGP9yWaN1xVWgMpbnYqafQwI01YHsDshO4ZLrxkNsmYJv2c7DMljqdMp0dCGFyyK4_3tyzD8-U1iTf7w7275W3DB_xsu8lcJk__0bo0JC9FtkQdV-jN9yBLMiWZ-546CS8vbgH9OD4le5x2SaWD8BhOIyN4tlvrdSwKHnPhTR2ZJ0W3ZgkktEu2L9sZx4AxQQbU_YKJ549HV5uSZ09SxTjRpYZj7JtzX_PscMBjNHk6cSTfE0yS5IZ3alG3hLtA1zQ09tHd9PioM_DZ4GE_7cEl3oSEZeYLOF_9jG5R7LO-yS_h2N2cOwfmX_ssDsMXaDVu4dGU3kx-08oR0RnFR92m6B0wdU8Tlo1Hv2HhdBw_0XbFWBi4QSAei63IRXupEEl9JhvGqsd4fsGkxdCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=B7oTTcVjunAUeUNJcbZ_qNyfyWABPKB7wN2UG_KVHe3EVkJPpjeYcIo12GruDeN6GVrL88xc9urWGplB67sx-yy7PAv2hK6krGOh4I9Wc2gzjE0wAUa4kDbRKXoIpuIXv-3P-ys3kxMOoxq7fm4SOLLwWsrOPTgF6rSiZDxoaaRSZfqvKZtLh__I1vSd7WpJL3AULsnE9URkQwGja9944bfXM8HhTZw1fuoQIF2Nb8hHIfNg-1sbosoFGs0NTx_p0OQXCEIlS32VYb1rVPUVsFQuGP9yWaN1xVWgMpbnYqafQwI01YHsDshO4ZLrxkNsmYJv2c7DMljqdMp0dCGFyyK4_3tyzD8-U1iTf7w7275W3DB_xsu8lcJk__0bo0JC9FtkQdV-jN9yBLMiWZ-546CS8vbgH9OD4le5x2SaWD8BhOIyN4tlvrdSwKHnPhTR2ZJ0W3ZgkktEu2L9sZx4AxQQbU_YKJ549HV5uSZ09SxTjRpYZj7JtzX_PscMBjNHk6cSTfE0yS5IZ3alG3hLtA1zQ09tHd9PioM_DZ4GE_7cEl3oSEZeYLOF_9jG5R7LO-yS_h2N2cOwfmX_ssDsMXaDVu4dGU3kx-08oR0RnFR92m6B0wdU8Tlo1Hv2HhdBw_0XbFWBi4QSAei63IRXupEEl9JhvGqsd4fsGkxdCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9uaKzjVofRyvzQiYsp3UK5XH8k1hCdn__GIwwGL9g-0rTr1pA0ikqmxIzXx_rN2opcyWIb-UHEk_yg_VCKGbiAC1QlfdTUcol2O8ijsE__ZvUFqGkwsSR8wmzTCuMUZvnBe7o_4rke-nVarlEPi1X6Gi0Z9f4EIuWoid2h4UjIwyL26R5bbCMXxT_vP2QXAumzKlF3IbKx5qagpniYv8nRDMgk1VjVQYUlRBUJW64A35rZdGcx-QdoCyFoDrzx7YYei8YAaJo2MyUxvWXC75A1mzRSWP5vZPUnEPhEylNEMBonGNVvSXbOBVxWedHRmdphgyw1z-WgTmeCLavmcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD6jRXZov_UAjbdBuWRySOkPu2H9xFDw4P6WIwz5aROrfXksEksGoVof_MmGv7tNtJUHC0AuHuFXwCjX_UJOlNB66DqwLee2eFDfJlZAWZfIGlfHXbq_umk5-ecsfvNk_5vVziIDpakdP0aEPvxo275vVRY8K7dGc2PFN1Y0qL_V4ljl8tF2pacZXou3Vna8AwDGQLRF3W69C8UNHYX5GiScOi9ufWiXSPS_OCTdhDq2blOnRoMgIwwu9idx2uP5AAlkyRxlfkRdFkLskJzOcQhAOBUvepE3Eb5vFe8g6sMkYIOw3mNMQiYN2kXJ0dkNkkhBOi1dRQkigVcyDI1CBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOXbnyCR4PtIUFstpPiF36zKcxZK_4j5PfkZfvLlI-_DP3jx5dZrykzzZ9JUy3XPTLsIGSRpIT1Ss5sN50iga_R7d4R_2XRe9Q1Dd3-zVV8USUq7qhL2W_7uam1GzKGQP5PsU0VOsat0VUg1vFLv3zoBcM8MMumnEA6bV7qPeXNpWcQ1lCAzQdJzOa2DaZrZ2yQZ18AoHgApZsK93HEh50Z24fxeNksYEPPJqZC6FHqFdeD6Jk1hAoY-vlfkrreRUMZ_HPKZVNsJCFp_dOM9H5FMzfXlnx9wUk-PEyst4ZoDpUynbVGM3mRWkjpF0jDiGmaZg3tHSR_D7ONXAdgXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjYO4wtC1sLqz1i-Dq_ZYGAMJJvWkPk8uGsincmrB3rPo4stDuaWjyNtY2XuyTl3PehvrAhgB5UoGOjggx5cuGlpOHrBNZLvu9ViOfyIkllVYQ4yUPlsqbo_xrKWWBe315ZbyoiRYtR7OyO5oipxdk3OuhIHPEjJZiPdU6Lc2WC5BUub6Z4zf4uvNCdYQH-S3t6Nk3NijlR_26Vqg8MF4VSf_8ul2zReBuQjNd1ZYd_jR5oc4kNQqXsGHsDyXp0BcfHh0ypPYIj_FtqwLHV62jDZI0dtIIBYAuAvnn7FdJOP2ERmhm342re8-bM1vgYfGiQHTXnjyYpxJwvnEQnZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0lwVsife4s6mOrUB6l2f8MHGs8wRG5Vw8FIU0Nl4mdDICAndjY7NFwcudEZlCjBTNvp-Pt_RVEwQJCIxmt4YF3xWBSAfipjjvVCrKD6r_vj7Jc0Igy2zjE1ppeNYUbIOG89Xq0KAAiQMKDkVMbti2N5MocezB0JqnzT_MOiGniQ_SUG8-tvf-5nwTcEhxHLykKwKuhArW2i6uEtxujeC7FY5e3V6ZG2bWA2_83I_PUT1HrgNdejAIL0CzUmEP4SvNVpxg_stITeZOoB55SPkQ42yErGO2JWLPZvE9E8yPA53ZKcDiwzwO9xfcKKNanSUvct8NVWy8X6Vc9Q2U-t_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=patbZj-Wo5e6mw5DYJgalU2sM_Gwx0zkohs12eQ9KNBgA5z4iuMxQO769dwFeTMr_PUtiGvXm-TPnKN6gnAROSZBT2pW2C07SrxSLBtAaEer4gK0c-5F8OUT2-rUeOMdOb2mEymWpiA2GBScxFSDYnPKxMgjKbZioel4gfbHf6M011a6SfGyZcTwp_gyAv51l4Mn3MRjk57ZK0VONS2HmZp0okYBZlJsWKq81-8no4NDd9t5wwy1WS9QFyAqpJG7PcKhFmDBiT30BrEW5MVoklyaICRso1QUBBxAo9Wj8yRINYZebekmdF2_AG_nUD6YztjJj_HirGhXkIMPkLq1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=patbZj-Wo5e6mw5DYJgalU2sM_Gwx0zkohs12eQ9KNBgA5z4iuMxQO769dwFeTMr_PUtiGvXm-TPnKN6gnAROSZBT2pW2C07SrxSLBtAaEer4gK0c-5F8OUT2-rUeOMdOb2mEymWpiA2GBScxFSDYnPKxMgjKbZioel4gfbHf6M011a6SfGyZcTwp_gyAv51l4Mn3MRjk57ZK0VONS2HmZp0okYBZlJsWKq81-8no4NDd9t5wwy1WS9QFyAqpJG7PcKhFmDBiT30BrEW5MVoklyaICRso1QUBBxAo9Wj8yRINYZebekmdF2_AG_nUD6YztjJj_HirGhXkIMPkLq1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUyWKDbe40cn9tTUsFRNBo6qN489Mtm3D-wBJi3dZswe8F8UDICJcvSGCCVc_WEbvT85R5rRPieNKK-blBn-jigLFILomiE48kCyFQmJ1zOMRpUD-6HYg3jLpPdV0Ti4gYpRWaCsx8ULfBNZSb0B-oBIxeJXcR2t7s64Aw0yIWgEaeYrhANLCt-qh2lCiFD9R0Hv4rK7DdEUFUz8Neo7RB2rhKtIlKyuDTMjbrak_p6_v81aYV9ZmQS9hHDPnAv0EVavcx_r_LL8zZvcA-8Dslt4-UFmcKVD044miqcXjsdkmLp5qcScW0nAWQzmKiVxg2AobnW7x6NkAth0-zCAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAf4evg3BeTC5n7GMOeq3ZV-9NHUVeallLyMXH0d_-6yqw15PgP-skp1eAcKhW7clWVXnfEWRkqrdPLJG1mrXnkU0fwJ9M8si40JST-AAggbF0oPh-Clu41k9IbAHzfzvGmLMqahxiBXHaZJR4O1B_jtP_PaP726BJzP2qTG_aT1a2w5NpAmUfZPSq2RfwhT3EnmBr0bGwyz-9PZ98d8qSYniwOofFCLr0S1x5PM_M8YvSrDdHvB5lWTdn9CB-MuPKh0oDyzb7Zo9WYe71jcbBpUzcXMKiXq_8TwfbVB0MwsLnP645fmPT8iGgJ0IdjO5s0vp_Gc90rOsg_jeASFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpu8Ee91rle8e4iVw-aulGLd_hpJQNak9tHE5rP8qf9r68s_l80KC3KCii-J7HffUAV3907h2WNhBGyX3sFpwhW0X911zxbCHcmK0WZETuVtBjGtI7ZugLnre8AG96lT-PQ7vVzZIS-VrCj71rQraQfron2owYHEFJj0tHligEvtzF1qoM9Gwd-tgpuzHV1Prols_vJjLS4YRq81xeumE2541y8qyddaC8i6buDat8JUGC-LFCUnmuWnuq8fdLI1GrEfrheDfW48wdUjnIx_GIoN2y5aFuvQ5iXlYG4LOjKw2XfByrMrbHgSje33BuhTN0SBHTDN6RND53JlftZ-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjN8qQwsI-giI3GLt8Ho0AhHWeTjKJOnVGGHgvsarKj9yGDf9ya2gJUj628S8KI9-xp5D2JrcwCeZ1Z5DzpsoMc1bbwn0Pa14d9_OG1mY7447YCoLKCbAUXP33msBGo1XLfhXnSnwwK5VXESDaTlGsFMRwuP0GNWQjkI3R04x8oPA8glJsuM18sfJX2h-dhv9sHOuUWQKiwSzJ8Svlsj82whq5pUHmxoPH91EfVN5f6BiCsrqMEVuhThTdlEUMvsiuWKNnVumHAB7ApK7LIkG8hHD3h_OsX0kb5b_vAOj16wsXjaGxxRPBkQZZAe5o11fl1k_bZiA86cfDNhuma_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFzPZT1UGg5TNFURzmpIn2dZXtYJ78U8XAdUCmLRJNirlQYMZcedW-Dc5tAIl9IAVaSxRCf3cZoLWz9uSqCTMzFF0mDtYCqvqbPRC9KcsjYiHe156gWun46j4yrHAsZ8vO1pydHQLJUhz3M1bTH5UgS_tIELtB-IcbEIge128zThF-i89BRo2fpzyZB4NAkT7ofB0ZdWC3SUV1PmlaxzY7yHEHjI5Nu3XiEKwqJaVpjgABr8pRjushBh9DdsBdoEbl2h4-ROiAfCk38RJMQPrZH6ibAsqFFqq2TGDTOTtp09h5f5pp_EAu9tk0rq6AbGhredw3WceIn2Mam6nQhQ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfZbK34HINCd0PLiMioA2fdFJKEeEoNUT2ZQIhoFZbNP2BvmY_TnVO5Nl23V94wDmRE3yd_vtMUOvP0gDWYsELWsYZyPGCvVE7f9O_8e9IXRhEbByZi5sMa7VUktD5nVv_A3TulR5WxghbMB3RN34XKgcc6rUquLOtKD7O8kMeHJbXElRQ25U-lANkBWlyLRIw6TWV-7ZZUkkC6mK5qtD6zl8HQcNgpDmg7tkzLOD-WJmfACzZ6O1pnBvMCoFfc73gzFhHoCutFUb8AbAGtIjoY-UOANJkSZ9HKfvDsHBe6lA9cb8x16hFehTBHbLjtoVttVstc3a7I_W9mncfxHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=P_JIWQWVWajgZXZgiYqoRDs60F3defxfX753p6jQ4yiL0ib92fAGhcKxunK4smTEG2uHGEaFGoBw8Sl1f8NLNKpB2A2GuqKrap1oYLvMLGHiqH3_EJurRHg8ACj-UFWRy3KxdRfMVmA8v60fLUevBO5Av3TLxxYnLAuihDKJZMQfJgKfdKHFPZ7b1KIQI5FBM7bkNYac71zZDs7ASwKWcmdDpM40ARIg2H4-Q9xcm2H_r98cszCpcZxg5vBY360B9ttNtGc7OfpEtigiJlFbtwaaPPnmyA6MrfXPvw8jm9GiIDHsA7X-TpL-lqa6G2XqzIY15hS8G5rHY_XHW60bGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=P_JIWQWVWajgZXZgiYqoRDs60F3defxfX753p6jQ4yiL0ib92fAGhcKxunK4smTEG2uHGEaFGoBw8Sl1f8NLNKpB2A2GuqKrap1oYLvMLGHiqH3_EJurRHg8ACj-UFWRy3KxdRfMVmA8v60fLUevBO5Av3TLxxYnLAuihDKJZMQfJgKfdKHFPZ7b1KIQI5FBM7bkNYac71zZDs7ASwKWcmdDpM40ARIg2H4-Q9xcm2H_r98cszCpcZxg5vBY360B9ttNtGc7OfpEtigiJlFbtwaaPPnmyA6MrfXPvw8jm9GiIDHsA7X-TpL-lqa6G2XqzIY15hS8G5rHY_XHW60bGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czlQw1MKZExOKaFUMGTlCR7PWZvYXOd4HfFbZUFXhnsw4CDwwyDJywiQ1egh2z6zXXWzumlOIZVDZofYKUxZyB837N_el5-A92_86X2gEP9JtBR-7POaFa6yubkG7KMyr4Ksjj-yik1aawDKsvae7HTqYWF9tjJsknGnak-Mpjk6w9wttc_6OIXn0P2it7O_Y6ONrz1QV7Fu0z2bEEhCZbebqRjoPRf_4RelShrkQ4Wh3rK3A2rMNHgxHFCKH__ykFFRy0AEvuYxKDCMOu7p2x-PufGoh9VuNymAP6a4dGxvp2oD1Ui3vKy0q2wN_Z8749duHHEFb5vy20l5CFOuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omJgcJiixlxLKq3N9iLZlNsrsl448CnK9WtNxufoaY_9A6nnGEawC4qBDJXsQ2AXUeHi1jJnBDMPdiGUJV11EOmkoB449jNoj1HD0nw8lZPF3d8LR0sBZFtQF7vyj0IsdD3DI2BzZ1sA1tjMxGbD1G7Mh3ZXtnRC92BPzGD5qwrr8ClV_nurz-R779xwNs4_l_e_yDx05GHj8o5kixSBW6BTW05puvwVwgqpkqwM5f_-wpaVlykSgpRFW9TqB-jV3A1cYli-Tk1WoC4eQwTgi5JyE8U3mvB6LdVOfiGtx1PsQ_cwpXNlAoXPH1eu8f8OdjaB0Jl3FtxMHTpMf7sIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLPs0pdbi0uVcHnPL1nJlZDcbQ4Hxud5dnkEVTUA6h5gZKGk_u62bGOu3qDiMnyxDnre17GarZxUbUOsblRLqirZKPC2VSHNLD4W9zTB7BS9IHB2g9RamHpxPVXy4VS_GVrd5kbLfefzfOPDOPABBF10aBk78tYCveHj3k2etmHgQ8uqB5n_j8O5BFRpe2A6v_lt1s_o_wPbnAN1WPo1BxORiA3J5Dxu2fJYjLZw1KquHvzaprGYSJ5kZDpiJ1OmOeYBA01EcLbf5WQnf2PLlpPktpiJYYuAm6IdCbISvPci0wZAdjnoW7CGbWdVSW7GE2aDaQIEGqlKFybOd8vNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cg-F1BjljhPJy6NamIolMgsFXSq72YBvehh93fj8kvUbPa41FRbliek1m5gybL8AGnDGkTmHDuLhZJemrDVnteLkezoOTd3TYQkU696MsbwGWPgvfaW15hapHg3WurM3ln847XY3TF4ZFKhWkZsI2pMTosSQ3wqMru7RtwN07qltC__0WnLhL2PuZvQs_RF6i6w2p9iuxWksFVhw0eRo31fm9VoHy9QgO10N-9WEUS9-mv6uHKpYY11U1p7EGoZ15gxD6mS53WOX3K4Tk2ZXE1jM8evBX8RyNqBvnP36K3OPfTSMGT_Vd_Aw5YgNhspmaZWf_lsQyDc9HpcS1-b-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cg-F1BjljhPJy6NamIolMgsFXSq72YBvehh93fj8kvUbPa41FRbliek1m5gybL8AGnDGkTmHDuLhZJemrDVnteLkezoOTd3TYQkU696MsbwGWPgvfaW15hapHg3WurM3ln847XY3TF4ZFKhWkZsI2pMTosSQ3wqMru7RtwN07qltC__0WnLhL2PuZvQs_RF6i6w2p9iuxWksFVhw0eRo31fm9VoHy9QgO10N-9WEUS9-mv6uHKpYY11U1p7EGoZ15gxD6mS53WOX3K4Tk2ZXE1jM8evBX8RyNqBvnP36K3OPfTSMGT_Vd_Aw5YgNhspmaZWf_lsQyDc9HpcS1-b-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPYNM3t6lWayjYTIyJr4EVlcChWfNRXet3GuLcwnaLSAY9WKLOTkQgqbJyU4XyZKELr1I1KftFc7UJJOKqCE5FruXp29NTeDJeOg-H_pUavVab5DKm_HxZK-XSNiSDIDryh1N665JJB43sXScANAWKOYvojcH8I1hoyjVbT7aR5uYsSrsreGunjONhMAAlxDo1qgK0gKKiDrjN2vbC9hN9SPVbiDlZ4Ww3XJhRooViaLlUhZxgbfgEl3-ZU3Wf07oxr_0svJ4A6bzw02vYNLIQ7WXOW7bNFczo7_emy8OJi1oYWTmyeufoWTpRT9nxxluMZmzr8VeLdchAieB2lYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrYEI_7u2_y41DpoBR9qvCHcBV9hcrzAgcWpOd-fBOEysyeQ4sRTPl1HiR4XbLmkGhW8c5eCuacOFKv3BPeFPZk7eXqGb4gzrgWeqc1KgHbLMvb2zlO13b90o2XgC0qF8AWQNX7hf-ajY1arfWBgkmMvOAtSTxCG4cMeBSTYyZGXp6QcP5xGBeKEND-7lj_qMXVEIkvUrWLy6l-CXQ7qWAelK9gsXF_RynCBNEfDXpIjg5JjBdk8O6to1fqSXJIE1Ye_ipAhadkp82PZk1vNjfO_Yg9hzYINwzG59QvYtVy9w4edkOV5t7n-VEXFDtQPt-2PUs-E0pPBemJgDmxV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCX36jcTk2K10x5vaGvSjO4X0gCHSbXthzQm5_BQPXbOJeM-mFuUXKM_rI8ucKJvJAUAXZ7n5n8u5Vth5mIzhwvipSmZv2B3ECRKkHzc43OZn1LXaeT0fCTbXJWf3EVxNevI0o-d5MppR3kcMDYZCY5uy24Why_0QhpRThv3touBZeXJqEd3tZvu4Jk-cSMjUQGAx4NqGJ4wpEXE9NeWz4PUfNJ0cubF5fWnQ4eAOApfuyaBXVnYmjFtu8_bunzwldaz5UdKMVwOfPG-pq4E-olZhNkekBl671kjxCZ2phbbtSFUOOUMkhtZQfaNu4wa8VwV8ebm9bwetUh2IwwD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0Tm5CiCVkVVV0GINsezS0ibdj5bAB_YdLAGlV25_lzJpWASS8HbbnWoIhSwqR1JbNTx86s6dTxr1wr18kWbFEXuturWXVDR--D4VErVIwjWV2oZOnXhYADG5f7OKQbgxZ1woxXbD88l4UHgM4qhfSybLPiwEVQJYG04SWmWngaQTJHWbZwP6iXPfBhSjNaAAoHtDfx5SY39H5LqhmzKyuieifUQzaP7ubJPusoKgrKVopUJg-yFK7UZQ_KVGshLklcqZwr7uys5tAbrD2RP20L8z833RfxwpAWAhFUVgVxuRsP-nWEw6_fscXuyeJgRel1JUV2XR9O7kG9Y4z8dPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCYnIT5-_2oOIWo9sufujfJRAzLPVXs6rGQWL-i4_PVbYbEVTjXU1PlS-IwUi4GcvArO9cr7euow0ks4uZ6PRgihyllpQFAfnRQMOeoG985OT8JRaKuCuOmEPemb1FEmOQJ96xf3Djf1bh7P9kA6W0_TzNdMP0Q0mfUDCkRVKa8aAcA2VtlvGnP7zDS6kQnLof-mv6M_ngoEtyP8ta_-1Oz0tTL6fS6hJiTN_ML5d98qq-giE_NqS_Vxh8XD49Mcs9zkclI33gfS6Thytzb33YMfrja5l9TqHo1GyF-WX6UW_JqvL2Pk7T2DBwxzkmw9M-c01AWfBgRnKj5HGsMVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La-x6235xi40pPBDqO9KepvKS4PjhQ7c0kaY9kvvM_sGXhGB14sQRPcqqldBbUhm3U-sjgkZ0-sSs3KAxmZ4RWYtwYx6R2ukVA3hMXpecL5MxK7rez5m1lN7JyIjiZNVEFOgq9GQBE68G2EM_hz25umr4QUV0BzrjaW96YAHAMM6EbR2NLudrXZvnvTrnWteif3IhbWi8LAGgYSg5aClSbSC-h3kpRVlySneAiGrnG5-XxMK926zX-Tqvi0-3JEYeIp1mJrq-O2r60nT_kAHyFRDXwrX1ILbLdwKGYITlH9kn9ee-Yj4XKkFT3KCpcMU68dbMZGnqmsf1bhfMn-Wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1jmDvqH30QFJk938rWhbSpT6-TB8z1iZXzAEFTkP8zCdaZqJP_zI1fIRcDfjAH5ZS2lI-6HrREzz8OLeyHQck2aloPwYfJtb4kozwYSeJxPgJ2_DC2YGybNeqS09J7lXZVMbFfVlPrLEQWGOuo8o3VQZKUfuLyvi7KZHmAG4yl7Okm-mwcC4pHFqxqIJIHO7ziRB_OxNyVBFTUzqBs-EsyQHZUjTm-V_k9ewSj5iNqV6aQFxF58J0mI7iKP0hpvmfgukUVYHKbHRleEMxF6hXWkoaaPHkwELZjN2RPQtz-fVSYiuX7OKEj0hbsM6oYCe33BP9qVTVJFT0GC64pP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1hEmEVKtCcZ52Iyn4oDhDFeLgWJkftGkKeH7RX5tqH6oeIKTUJXvpVXyCv3MPTZYDGQgWkVmiEJKZVtjobc4HRgK9JxqH3cFaS9AsmSISABrujYqghr27PwQLbtPNmMh75MA34EzFSqMeQJAjby663KnLZqXhBoRVZbQoeaVKu2-9gWeHlNWSk9gfHQ9n3oKjkZyRFAsvQMP7gDWCCP6inNngz1oguzKk2WTiWFoGym5ed3MGe1LbURa3571KVDOM7vJ4zVrD5kyvr2SWmjmESZWr3X8avcTM_JMy48wWFW7MSc5gsP04g-wHIF44GOSBY8hSTAziT3u-5rIf_EKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=rEi464Ypdcg5N8q5XQ2skUOM6GnjV_wkwXzBITXXK_GTaGNGSd0SCBpalsXasKQTUeVfqm1gHkzIZXABU7IHgzi9qpBKEfo4qvoWmhI-kPQbiTuNWFsOZSzNNXsgJ5baR6gpnDhKOUTSP4-FAY0ZTdddHbrpAu7q1d4m--wwOnt6VdGBfvh-j4iQGKDI1Zv_MJVp4o1F1XI33xJaGJBY12h5cQFRE2gGHE2TWCwch89_0fp49n2H3qKRw99_llbCyz-Ra4leEXdgXnbiDT3hLy8UkZCstjpnphbos494K0P6_j7kOYh5X5ktMwR8dVUbwYuuUEbOllxFuACvUBxsjwi_tWi-0kh1_7ZyRykfUD7t4QCHcXY2HVMvzLSF_uSoppqYLj68ybcD4tMaCYnV06kXuVDqW82TD3EoPaoduZiK05n4NoNz0Z_SyBVcR8RNl6HkjobagNBAj_6sDc7xCB3qAhF58oQt5P9S4hxSSIMKEV6Tzj8c-0WDrhfY3g1OvIZ97OOy4XtxYDwhq3lic_eUJSYEFXHRgIrVxm5qfe37UF2paayJDktzOFlgqZfDqMbO8Dx46iw7rmgxSqkoYfYVYiuBr8xvThprWcD8tCa5SYX03C88rXXhT5V_24HdAMQz0k5_wVxt69P5Q1voj4OOpNBrTrcl3xYHm-b9bjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=rEi464Ypdcg5N8q5XQ2skUOM6GnjV_wkwXzBITXXK_GTaGNGSd0SCBpalsXasKQTUeVfqm1gHkzIZXABU7IHgzi9qpBKEfo4qvoWmhI-kPQbiTuNWFsOZSzNNXsgJ5baR6gpnDhKOUTSP4-FAY0ZTdddHbrpAu7q1d4m--wwOnt6VdGBfvh-j4iQGKDI1Zv_MJVp4o1F1XI33xJaGJBY12h5cQFRE2gGHE2TWCwch89_0fp49n2H3qKRw99_llbCyz-Ra4leEXdgXnbiDT3hLy8UkZCstjpnphbos494K0P6_j7kOYh5X5ktMwR8dVUbwYuuUEbOllxFuACvUBxsjwi_tWi-0kh1_7ZyRykfUD7t4QCHcXY2HVMvzLSF_uSoppqYLj68ybcD4tMaCYnV06kXuVDqW82TD3EoPaoduZiK05n4NoNz0Z_SyBVcR8RNl6HkjobagNBAj_6sDc7xCB3qAhF58oQt5P9S4hxSSIMKEV6Tzj8c-0WDrhfY3g1OvIZ97OOy4XtxYDwhq3lic_eUJSYEFXHRgIrVxm5qfe37UF2paayJDktzOFlgqZfDqMbO8Dx46iw7rmgxSqkoYfYVYiuBr8xvThprWcD8tCa5SYX03C88rXXhT5V_24HdAMQz0k5_wVxt69P5Q1voj4OOpNBrTrcl3xYHm-b9bjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE__rjVpyNxKtsd9fPLE4tVbI0oEMfA8hJM5CtLCYnEgsQdZ78raRVA2SH_Yscgn-x9p78r7gzFx3vhavjyOeLgJbV4GlS7uy8CDQ0jkAuh4ipVwEO6E8LPzrzdBPxIHuQ-5vzVgOsosfGWFtt3wpQiJESZ_lUEpdb0-EkEYjq4tfBMoh2OmBgalKh0JCRUtQY2Ab86tsDfoUAuUh7fwqieBuAtUZ_0pJhOaaE6sAcHv_-4pM-DpcdnDrzfi4ZAuJ3SuPBBhySf5r3m8b7MOPyVyZ1pY4Pd9iakE246m3ZTilsH_ya8AifMIwJfiEo7Ud_n_DO7Geq5k4hqj0OfXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmkQgWnSVXQdY63sodrT4A-6PyX4pqmgoq6tHx6GDhDLrnLd6dc_5-kXfBH5cEgo51BOkqUh0zfKZrnbLP5YpMoCnOvvhtJwoh5-4Y1fUR8ujEvryP-sY2qyh4ipm9I0CpMsOBusphl-QtLNNiJt_Vs1nkov3J885s3Ht7Cf-Xy6xjJ9srd1tyCxxBw_L_6-8dtV54jP9Qg2sHGRk2W_1nQz_hNSP-LJLLKqG26gH2qsQlrL27Xs8hpGBk9u5jVX6qRPnPRtaGtBHWZTYblMxb9dqe6NKFK_v5IWDNlBuK5kb9fXlBagci0oCv1NkBX6JKS05NjsoXX_hvlQsi8AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urzbz2K0hwO-N9i2Zcm7ElUCeR62bHmuHuWmH9zRFDk1bidAhmtAH0YduWLZbSN6SayGT6CQaI7nB6DILK_J6SqlsnHmeSPIJZKTRsdt8m3W7uPfP_SAD-PJoeTnt0z928X7LsCLTqNffI3UWHl293c_YGD3SpgCokZCySFTGs0SJ8r-Uq-OywvCAxe0oioAgzt4NL_f-MskTjTULt8tlO-7rxI2X2-6kj9j8SWvYcFtUDzxM254JQ3pjbTizdnj5NIEBbFtLa91XvozF2ONpAgRxAPehGeuABrdKqcyQuFmDm_nzyFkhMzIRqJJcMS8eymPfNGBA0PQ2zfy-s80fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-tJJsvoAgFyuKT62FN47P0fQMAn9fFhG97_hgO2-vrV9i1B7Lhv2lVeFwHJZt8j3ctp9XcbSIK3CAWQEukyrnkwcq0ACOGrfZL_n9L-OX4NRgsN6O7PSWFMRuUmFfukQ67KFr_ITFwqwQi_QhcVHsBQ1UwkI5Q6tWzzj3bKcMoaIK8UHqB2VgSLbtsA8zvtZedtc4HlkV1OFSx3J4MhjwUHcUdZPRjrkKinMcO46-DzDIvQpZDLfEGSI4W2Jm77OP-sPhwAB37FdSgB7VCUSd_pjtWCmQGoSOH32tMWI1DGDG8nBqNGUw_ksvSPyU-ktbKc5EQPvezUILTRLlVXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=AgNp8xyd5IQKYqzffLnjkqcUPQImn-WxixqABDxY3_5ZezNWufvqOV8_R9ygroC9B2T91BaqTRL5dguzZocT1B6Iq0IHjjjfLL9t3KbLWIh_ggHvS4_NOa1gp_UeZPAutqlN4rve1HOWTUw-Ajt_P-sAdOKYBHYEjSLDCaF0C8W0QWw8MspUJemfeqmVUAIWhzZzSQCqcBngHPJVvQoEV-KQ-kJlZHcNK1vfJObIBp2nv1Wd2washcRNlteOk1yb1knJRpbqgN4UnabVAVVPmKXglRtAmXL3qPc2_S7QqfmrBMt3JBiynaAZZvlTwEFr547d1y0z2HPNt3bdT-YnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=AgNp8xyd5IQKYqzffLnjkqcUPQImn-WxixqABDxY3_5ZezNWufvqOV8_R9ygroC9B2T91BaqTRL5dguzZocT1B6Iq0IHjjjfLL9t3KbLWIh_ggHvS4_NOa1gp_UeZPAutqlN4rve1HOWTUw-Ajt_P-sAdOKYBHYEjSLDCaF0C8W0QWw8MspUJemfeqmVUAIWhzZzSQCqcBngHPJVvQoEV-KQ-kJlZHcNK1vfJObIBp2nv1Wd2washcRNlteOk1yb1knJRpbqgN4UnabVAVVPmKXglRtAmXL3qPc2_S7QqfmrBMt3JBiynaAZZvlTwEFr547d1y0z2HPNt3bdT-YnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPXSycrOg9DtGM3xGCWIUco2sq7xlbjTFtQHx5lbGUPa_5Jn03IX73HhjqdtSzvq2YUWh-69nT077F9ELv6hrHMe9emI9THpgwDUhV_DLGFG8mQu3-xZRKYDJK3hSbIGF1vG1UOdA0wWccuX6KCwmMESkpsteyimNthLHKOFE_xoz1ivhzTTRBVIMvXNrkjh9-8gE6U_GVCsexDwxmUAzJ5mF-SOK7jrSAou976tIj_-z-v_O_QFF-gzSnFKPK5b4DFARiiboPJFRsJMEjqsEP1OKVFd7liT13Lpxd8lftEg3D3dp0wMmTiIfMHIH1ZotOl5AAe9SbqFoDLytKm1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFhpqmCamSM6NITuQ9niPtHe-SuXGl4lNPPmJT49BubfILjfe0oBadfc3Qvm3sM3xQ5tgmIuawlsYT8NBI1Ic6sn8I-r8CrWabYKfufCPybhld7lSiXN1-MPW_h0ievwEzpmt0zTXaMIPCkYxZ6f_d-9NCEd5QujRFcIxvlZPJSX1zJ8mUCnpzU75ZgM5huZZPLMxCuzFNAvd6VAGQ-fgVbi5lTH2K7mS5NFH7utm0fwrngXtI21YtBoXJdj2ftTuii5x3iG92zIJ1ksqWCYzsJPR9l8Bnv6A_1IeWkxYp0JJXuO5_3AQX0Sr2YBydto3xCSL9SFaNHAbkUVKvLycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCc9lW-3XNbU3LWLVv5VLsmrjDQLAuFmU_AJb2NzDGGAEWQdwBQK7wA25vsvpSQOQsxZX3BmHO3JbB39KSiUlMK1SU9qKio83HLWR9mEDdwMR4BJSdaaAeRADPmaBE9fQ7AfJZpeSnpb6SYLx7ydlb0xWK_rjtlmLab-Y3UswZXLQOc_bieJ0gwmzBVEVuVvMPf13lY3zrjTpXGUvH_lIYIUxMGDNX4tBSR7a9-p5gA4hYjh2ojfojFMjjdnpPtFG6OASRnhX1MqnDxMPk-6zMeo4ZOOv16aqYQK1WZ_pdGx4HtJTcxPd0Bvvi6CHH_bZYZ1d5vmLE-qYQ6qE7_aGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTL8H43wb92leVoH8V0XPgXTJSOC2UgrBTOish9WQ1DLJgsR247NSrz1co1hG0HbQGhY5PvXG2ph6HFjCnVYlNHjPVuxnrFKYbEWxFNFz2tOfnif54G5KbrIBcnU7gSpWJavig2IakqohYZrZ67aIJTCRQ0Y57YnLZwI0Q2ro7xt9LlXgFob-MjHJL3g2Ep1ywMMvOYk_1-VFGck9V0wuOdtkjMh-00IzBvx1r1afH6ESg7Fn3PXuBghJX2fajD2kC32snNrvJlOZB0_4evs7He6tDch5A3xSpcR7i2jSuwP7Uzb6piq8SbRf_-I70CivviSufaSPmd6d5o97BcF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqUwbmLrP5KDsQoVSmjNXBNfK3uWf6_pa2rFjLSWesAl6to3YTE156vgX_BgCZLxhj8hJmpLV3-mc_uiwUAP2odPQmOPHxD8flaoLcD2bfNf5RLL3IDH7j9QdnWnu3VboLd59w2qCBGh7zYHTqIkbt8YkJkCeYEm3X5q8AzbK9KJzBEn1DZBQr14GVBHqpceAxm9oMxiGa7HpLlX8qXoFQV8bWoqnEZrt_dSQAIhqUrpLzUpy_NeB-m3V1l4ngPpQupBgwPXQd9gFCZ-_lCx-Svld4V-9CWi3pxdyQGb-j90amQGiiULXkjs53URY7Ni24bycouc2QvgMHnAbL9c1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b86tSzKoVHLz6pIQk52O67gbAx0PTbn_-VQFQNhAOKqZgQp5M_fiR41noUYADLwaYtdHFxJE5_Hw8I_F01NSWzNDBK8NFTmLzgj_tfci6s5-OP-NMSR9qpkyycP2WOXTbNv5_55Doro1w-EYKTN0IIzSwSD1opBM_4VDVmP288MPNeUmGMt1BN7j_4iLYVpFu9F4kG47gQV-KBUb4Ir9OQJKuWgFSmRlTa8mbFT_3kZPUQLBaomesRk3LknmN5XwjzGwpEKCphoPxJz9ir6gGfya17281GvGhzsX9QQJubYNSdrklLx9nb4SDjC7Lkmt-5qwTUICrpXwkNtUFf2dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li8HwnGyt3eDBEtrF4xNaAjTkhVzB_oahQVbJm52ldbsy513qUIIFBqkwVHV5MwGD3J8CBv-I2LIZKbF-pZG_A4JqiQWuXOnwQXrkUOlvS2CQGDvY2E8G2TFKJsvqxIGvVKrFSl737oRDYkS2MD-MPX1jwLnxt_0mV7hb-dafbp4y2CHrKwoctwkgGtS95KIN9GwEPnXZtM55dIsDY0uok8AnzneNHNgMON-t_bC4SpQAjPuIwEa5i7-9YyaZ83LRVEmC-IkHy4RJiR42Dg-kUR89K3xAXQimJn24UlfuHgClaFrcBI1w3FQSY9pgv4mCfLrz8TH8XloIIsyZSM7Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM6e2Z6lDgqOtX6ncmiAm_VLH1F8ecY12RVV6iZNxj1wIXkZNVZZXGhkaRHAtv28eoWJC1POBJWxqIwGVtaeUV3PLJ5YA2ycmDXEp6zABbLZkQS_d6URPxHAAtyXl_JduYNvq_SOurhBj6gedLAlojEl6YXLkHYmoUTp-_aOMBk-T8Cmod6g-oqDU5WYNJ2wlxz0tnQ0oz3AtL7JcRyslN1Gq14eD21wmTsbPfpKWG9As0EN5dUxqiP7SUAk57SAfZIjYdU9J268nr15c4cFh6QC10sy2zurStQqy05TwNmTCVOZlJurPf5RnwMpd16X6NBadVgGmmX0xBqZczlzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=PS1aWePIDKfFvsqWCv5FQjEGRlIb23VbrASZxHEbEvxY2WLMjYMJnqaQ-Q9TvU1sG2ReniZVclzzjMeo2ouFNsTumfhXNFNXVTFluzjIxJtSYpWOV6jD2M3FecS0AgvqJmhp-dB1Rz6oN6HfEUYcXdrIApK1bdjH9jMUdixXvfvIragXfp9IK7KeuUTsundlnXgOZlGKv2h8mXXsoNPgtilSx6G07y8sBi-3iouVm0VNIU-Q07Olx6515dvyoMtstmqE9wV-zd0tsuq95H9EhiX8xmKBAvNdnfu134eMPg_0kVzZhodgcZ9KMLcxlUeYG-ykXNyRJQLA8_uhRR_tiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=PS1aWePIDKfFvsqWCv5FQjEGRlIb23VbrASZxHEbEvxY2WLMjYMJnqaQ-Q9TvU1sG2ReniZVclzzjMeo2ouFNsTumfhXNFNXVTFluzjIxJtSYpWOV6jD2M3FecS0AgvqJmhp-dB1Rz6oN6HfEUYcXdrIApK1bdjH9jMUdixXvfvIragXfp9IK7KeuUTsundlnXgOZlGKv2h8mXXsoNPgtilSx6G07y8sBi-3iouVm0VNIU-Q07Olx6515dvyoMtstmqE9wV-zd0tsuq95H9EhiX8xmKBAvNdnfu134eMPg_0kVzZhodgcZ9KMLcxlUeYG-ykXNyRJQLA8_uhRR_tiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MznmeTcozM8fkJtEfL9q-tnWLw0mJxNq6HBifv_qpOqTXCKrKAwlXrFRQplecVQJy6VIEXnJeqwQYdAOu1O6DyZpXizRT13erjUw4o1Wi-xgwBji47uoN6fGHp1-Ozx-Xoe3QtrILTxKvlrHRMKh4YZbWM5y9Bj33R41kejuzKwE4mjvR_gMBLEWfOLQBUDt5rnIzBBB2rw-OtuQ2lDDlYoVAl2kNlKxsb4S6ycHoDwV7onZJe2LsPszzqmnt2UFFUnunE99pCWUydj7H4YA41CuzQ1EWW8Dj0klMFpAvykLVR4b-YH821zrzsvtjpgPsfC-8MJcbCiJ19_9TWi8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcTpsHsbQEny9wtfb52u3MYrQxylFWST2vVdFqDkairvmPueTbIZ_JLFT2ynR10mTrq7hmI7IEFQS3HcRPjw9duyseF8H4efrPULPVcKHtAzhiWr30QCgSqlXT0pDtwmoWGYHfDBKOIJwe-d1Yt6NaM0dXpJiVHEAJa39R8XwQi3PJRwg1dc2iWd6lctp1PSsX2FXs7WZ2iLkqRKgU11Fvb-n32ZiP8JRyoIxKGQ5VqtfaUHJ2eoqlz6IINcScQT0dhl8U7kHxYBqs0t-f2ewT7nScKyYzYVaBKsp1ILtisL9dHReRz3gqLTDlsnzkaEqSq0b5I6d3e-NhIw8Me7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-8wS_Sz1JdHg9g9wANG41C1S6Xk1pcQPxR9iMBkHjF35IIcE3KnSASFLDRmD5RviypvHtTiikGTuHs5aevi3yNJ-Y1FBpBx4m0-ao5rrHPt6HhP5Q-bXw7yrFEJMjCuYR5VHKH4-axvcYtiDFfrrh5U5hngIh-L2YcUinHp_pzbDYHoYRl1uX0ZYkeLT0DXy2PIKfohfMElkzk_QDlnImb6PyTBn7rBDHilPaxsj5dNm1-kHCq-pTAZ9mrJppQoMtDfytz3qzMj9xZbsIxJTb1rJ_4KrCWl2jiNRmRZNvMpO4UujAW4lOOPpDmHQVftXwEOQfCDPklFJpEuNUb_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskitS9L3hsGnTWKJkalVrn22XehS2zGO_n3Ly2AJSAp55sdN45Qr5rMX28HZsI5XPqhZqI5GpSyZ4N3w10WbVP_hPxWXn1bhW6NiyfSR4G46xxu8-NZS8Q873sEuGjBBVxElY4V6bKu0H5DHJZ9FG31BwQ8cXsdawlLqX-N__r3rfD-oApKOI_r0Zwt3useboSCg5UA-dE2hlfWYKptS3rcmUEvdlIUtnA57ZreRA1m0pxbt_hFJR-6nYj1zwACPxpdsRocgSuIBPaHhRtkxJgTmR2lQxfQWA6earuHgRt0WBCBvEnnv_2cQrTR5Le7rXTfktljFjpqxA-IHWABeb4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskitS9L3hsGnTWKJkalVrn22XehS2zGO_n3Ly2AJSAp55sdN45Qr5rMX28HZsI5XPqhZqI5GpSyZ4N3w10WbVP_hPxWXn1bhW6NiyfSR4G46xxu8-NZS8Q873sEuGjBBVxElY4V6bKu0H5DHJZ9FG31BwQ8cXsdawlLqX-N__r3rfD-oApKOI_r0Zwt3useboSCg5UA-dE2hlfWYKptS3rcmUEvdlIUtnA57ZreRA1m0pxbt_hFJR-6nYj1zwACPxpdsRocgSuIBPaHhRtkxJgTmR2lQxfQWA6earuHgRt0WBCBvEnnv_2cQrTR5Le7rXTfktljFjpqxA-IHWABeb4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=ecrK1i8pVYwXv6IxM7FAry8NOat8sAZcURv92ZrnJkvt21WHbCvdWvnFxTL1Gh5Cg0ivfEjbhJahEWNcK2CsF8V1gFLDi7A61s5Y21Eiz0Ksdnv2aAb2DRT1siBf5MCUB2hx9Bs0sa2JSk-ExlS93piS-5E-yWbAqjeqHDpX-dxoBRaXPkY7bADPQHAXj_9BYBG_-APA_QgBfklHaqJcAW-hBfTTQCDnldOMuf8Dj6CU7DICZYfD78_DBFZeWz6aO0FdJvbimiGkg5glDE9cedN8LXRu6bfgw866lhbu2dN9OJzEFuuNsqgQDNt9Iv90Ykq1aFNpvypZi6qkcW3ytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=ecrK1i8pVYwXv6IxM7FAry8NOat8sAZcURv92ZrnJkvt21WHbCvdWvnFxTL1Gh5Cg0ivfEjbhJahEWNcK2CsF8V1gFLDi7A61s5Y21Eiz0Ksdnv2aAb2DRT1siBf5MCUB2hx9Bs0sa2JSk-ExlS93piS-5E-yWbAqjeqHDpX-dxoBRaXPkY7bADPQHAXj_9BYBG_-APA_QgBfklHaqJcAW-hBfTTQCDnldOMuf8Dj6CU7DICZYfD78_DBFZeWz6aO0FdJvbimiGkg5glDE9cedN8LXRu6bfgw866lhbu2dN9OJzEFuuNsqgQDNt9Iv90Ykq1aFNpvypZi6qkcW3ytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=F4N5cJRHYaODaakBwrSB74JD9Inunr0DnaPiQjXkuTbLJ8X1dP5AbJ1jj6BQh1DdAXM1K6grQHW5hzywZ8R7iMRLdpn0X0OARd6o8VdBCnvyRFdwul8_nWvGtrDcUOkNuFZxTuVvLjDKw9TgRvuwzskf1WsIj8K0mg9emqsP-MqXAVpXLP7FIPlBNevIuBRxFZuf6tHHm8iKxrCFc-sADBCu6xL9ZMjgyCIg4nVohtIIc1cSFi4IpIA5yPjvVkqKdpALhn8Qc3gIxleoGB2p1Jb7wVeWEVBkRcsv1HarbzY2vTGeb8LnRVhQFqUIjqqyZBxn5-rIsURjkF-3IBsKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=F4N5cJRHYaODaakBwrSB74JD9Inunr0DnaPiQjXkuTbLJ8X1dP5AbJ1jj6BQh1DdAXM1K6grQHW5hzywZ8R7iMRLdpn0X0OARd6o8VdBCnvyRFdwul8_nWvGtrDcUOkNuFZxTuVvLjDKw9TgRvuwzskf1WsIj8K0mg9emqsP-MqXAVpXLP7FIPlBNevIuBRxFZuf6tHHm8iKxrCFc-sADBCu6xL9ZMjgyCIg4nVohtIIc1cSFi4IpIA5yPjvVkqKdpALhn8Qc3gIxleoGB2p1Jb7wVeWEVBkRcsv1HarbzY2vTGeb8LnRVhQFqUIjqqyZBxn5-rIsURjkF-3IBsKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMdNF0jTy9_kraN-ZlReP84uzYBkO8bAplP6afJN1DLkPBTO_WWsQyVjnCN--9ijF8WqKmaQDm7dOC-5VkEE4A59qNI_y5M2U5y9mGF10hwRqTdjGtd0VcIkcgD0uymQ5BIQmVGq90gfBcdY9IUxyz797bcNFP0QVglwzwvqbICMlKT69Gw5Coj6JPbLurNsFUhKcOSUZ2e6tzNo6yZtqU8MlIECVAP-4xMuM0dpmPSvJrwi2Xj5Y5pereer4i69PKbjwmP7-9Aw03x7CzdKye8BeC1ckGm_Ty6A7Xs3FzFBcu_2OUKVbI4YeaOf4Ou2v0oZIR353igR52arsdpuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYgYleaz6mivuiGcgPJlruy0VzQ7qiM4PXNGrkjBni8wpFgSIfsaKl74hdwfILiMNjeKF54svJdVkKrE8Q8GFMF1MEOXrf0aNOJA7oRmRUV1MqTHQmm6m-rwwC9mxhKEQv7QqyMljUt-fS5p-c1VS7CY-RQwAtQB5uaxNY5sWEJ8O80E-9mnUlrirVXOJr5nW3p-bhorX4r2qbEcfJFRY08bM_DVo_65h9XNaJ-39jjsg3alD3yJNwwG7cPa_f59TJCNCz5UueCxbCYSGKN4ds0i2aNZ_tn0bMx5jaez3eDPzz3GDktyjK8G29XDujWODlrR3y2tVNypmWXbBrxKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9d3q1YMZUo_ZKFuexQq8_PdodMOCZtod0NYcoTWWNSl2NMlnQf1qFjzKs7XQIuFLp67BYCGhSnPYLag9aalZXSDd17rcrcvRkH9hPRvD8MhBLpSgdUYgPKK8qfN8-tS49C8pEqWN1WH0aDD0PS-u0q1ucf3iMZbdBQ8c_jALQHtfl_atY3PGBfU-53gPb4JJ0OxvXzseRW-xXEzW5ztrH-6-lsml-bd3mM6TinRDgidgPW1Cx-J5zagZV1eyEHATALmjNV16tmoDXmsdrsNueJMUfRhUyp930ywhj15ufWnds7eITvk4HDulYRqgN0ClDKqXChqIf8tYM6qR0O7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM4ZBPyQXJoc4YHRC-gHvfkxFcE2qjdpprCPnoTuLbyaPoiUh1uxMV_S8B_8bfBurasuSPTHKH97dLam21GgFadKzkf3IVZUSJwpUeIef2gexmv6XLgMQSyan6d2WCX8IB3oIa9yrVi8CWbLx4areZrclH2TUsngTUbjjROiGcFspcjovOl2789nBN8-atiWjl3s-Xm3h3DJcjfmECYlkeR10YPxZZ23Vwp-qXvtXxM_1xb5cm8guA4bYLcX6PC1aADNG_2aDTmeeUwmqTuQeiiKf6f7ga9qB7lX_mQg_B-Q65JzmvLnDEbyv5uc8B5sfjYpWN7yDI7TZIUuzwJAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQOaSXSnM2KXVmOy2KhITv7sQhA7UHF2VArILLfFCCe4klrrWyiqnwzU4uqwhr-KD5B_rE-EkcZc8i1xklhWSBNFkHw3jIbELzyuVquBW2EBYhYnEVVNi3vNiaAFGIXXueLe5hgIrhOen2Z0BUxgZwbMX_2bRWTtXh5ib-YX9Ftiqp4rQUf4VAI8gZVSIEHrdImcHQ03iWldPkl9LfqAAOkbFSej1ZlB96mZD-ITsCBY9r1ZGl9rQmr7NKRt4ie7oyqWIZQDvzhdYUm1LhFt-al89VKhuWmJd4L4_i52QGMRGAFIkg_MiykU5FTC3YaqRsb9iIhh4ANEgWMQ3vckfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbfh5S7XTqo3OK-jqKJ4yGFbv95hkaNcu_HlDhQCKMT7CxvmQoHhY77U0rgCbkiiK0Pze1vMnFnRGsa7TPw2WEKsbN9gvaiAP8bg_P3-9FsvTn8CHv9n0HR_P2AMzu2NxtqIOx_DDFYrSwq72I3IJcsucrSJaWhe7A8aHnaSXgsgYIHBw8fD9CMaFa75oGVq1BvB-vRO_FcIuHhThjdY8gX3sfJhv9-eIpl0l5_iTWNkqilmoEw-qQrhR34iKZHtd6eKIAfs-Sj9_PxfS3svGuslDMdquTTZd_5_JoAfMlyQQbCMWyKZ-1lGfu61hDnTG1stYdUqVGiMn4dJwEJ37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tny7GgfwlqcCCyeXrMFD9WotkVqdka-3sqn2ZbLiZ9JlTdrLCibVs2tyNI2a5BvmdOdYbD-nSjrPoNAHCvkThRTV8NSNnzNVowK4l2l_zud0yhAxKMxYSGbSIPnnTZI88Ly85etM7UdIQQbbg20c7-sxwyzkDAQW40H55kOsxH4S6c8kKou5QW4FVWH9cKX1djU8L5NwZkdbKSRcXZZLCjRcELXx8-nRSTGOVrja0SG0GYOtRAQyaRgeeTgz7Gbt0IG7HjPbNHU-gvo7_D7xIor5jw5E6FhLKe1izqzVjg6K1zDf9tzjtSek5tOkeMoX_SdNH1UtKb3UYTEwRnEI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_E5yb7q5vcwE3bNhCXSc8HWvzKKf_F7TEqlrr6Vzi2NS3TPEKISXd-GHTF7cdrS_rDzVGzjeUQr9TeGJAM7IiIB_kZB10pve2t9JdXAdOsifRAB1y3NSzs8PTyxDNYitt-MDGCbEDzlRuyCOWtSUmC0om9wlkyDtsnr1rA4Xark-qEpF2shXH6EYoTog-7WXAx1gqIigEhwCjS3cUYF0X1Qk6LVG2l-OR8IBQPCwcWcoJjufW6sRjdsPoZLnZKRPYnffsDMa9ydKDwMsEGQ1uwDqgDkhpj98raNvWzgaexNl-0nPSsqBtZqWTbMUIxwQlmV6M1gTfqKg05gZxQ3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=nRb2o0xaKXSNvj5ViCLfTvIx-7UM1zMQ0hdL7uOq0RTk2kFIolpx9hWaemnEDDM5YZTpOVZxq5V1vb09VZ0NBEBwxmHRQEkUJZSzHFNh1C5JBHbUpgouT4bzUNj0a67qMPQHyNmhxrZvhshDH3xe-iLpfox_Nw-HdUiK9xfAwDZamckq3As3qMrqX15W-tyaY1ULvHJ8rfDVBU6k0vuz4zGnj80ypSprhNv-FcA09JWXLlR3XB6NgQkzTsIRxSfys3iKbgmXc1wq-iEndqPoxBFfw10EtxY5dpbiW3HPpiRm_umlZBVg0QehWh3yH9ScAVL7EzDBOaCGt2nauob8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=nRb2o0xaKXSNvj5ViCLfTvIx-7UM1zMQ0hdL7uOq0RTk2kFIolpx9hWaemnEDDM5YZTpOVZxq5V1vb09VZ0NBEBwxmHRQEkUJZSzHFNh1C5JBHbUpgouT4bzUNj0a67qMPQHyNmhxrZvhshDH3xe-iLpfox_Nw-HdUiK9xfAwDZamckq3As3qMrqX15W-tyaY1ULvHJ8rfDVBU6k0vuz4zGnj80ypSprhNv-FcA09JWXLlR3XB6NgQkzTsIRxSfys3iKbgmXc1wq-iEndqPoxBFfw10EtxY5dpbiW3HPpiRm_umlZBVg0QehWh3yH9ScAVL7EzDBOaCGt2nauob8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
