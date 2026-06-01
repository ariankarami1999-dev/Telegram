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
<img src="https://cdn4.telesco.pe/file/XP37CadWaq5oiZz5omsQZVNmPh49tGQ_gUTGJyJHSObyF8dsQCUhLa28nu6ofrmoa-j1Ak03PH6KqGtrNE_uQKcLKkIrRPoZQIDiuBh4PzmmKUw0QwyD0eS7p1mYOll3ON5MQaBEDJUBwceVEs5y1gGYuwPiJ4VDNBVoUJm3drIPskwGUfGn40ApK0jCC_eyp623kkNrhMncmqPYGvRD0jJRiJL05rfw5qDtzSspZinGfO5r5QF9Z_d2oheIehR-Aw5mGbxTPGu2Ksr4Y4pRqLeiqrK0xAlsuIKQqxe5EKu5rQNKhHscJI7TVJJ_sLBQVgAIW6qoOvdimnVqPIP6Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 177K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 02:09:51</div>
<hr>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GODitzD6X2KR28rcCFUdzGd5l5CRVASmL7GpPOksPfUFRMbjGDhHS5UwEYKYvPTh_sLlFfg1H0dASnCCvsE-FF8SSwUQ4GrOPxe-qDcDstdrW1kaX0PlybEDY_UjZvr58Q9hSslFqj2UbFKlvtSMHCQ91HyGsS11uccd5MOG2f-qrwChys4k_5AmY3RVLkeDkdhAJCuyrbM1UBIRaV5tUGaF7iLWM-8_TdHOdI9FkVNXzD77TJLHbgf0Q1vM1opAhrHqM9TiUXz9qu6_vIWz_7Iu5Gqb4syFOe-nbTjQpIlEWTnzB9_SX1zAGL1tVBIhUnJlg41BWeIp9wjr8ElrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTLrNrn5kg9rEQYHFjR1NUFBFKmgILwSWBUI6DYYXoVxwx-0LfkG2qjEO9CbO9xTb4c4yJlUINNJsPl_kR7Mz1CSDRrZSqSuips10Je2e7_La7vxmnvre220SBdDQkJr6z-L0lBI9e5mg9U8DXJr7B-wmqKv1O6G-YYsE82ZAz7HRCoa7rYBL3Y3DmjsE9WCwcOpYHqOhyvOtQLBYH0yqqcY3cQFjzXWiph_73j-XAU8T1Gqe_CDbqpjH6dZv98V7FsqYbQlPxdDGwcKA-sQTGxTzjTs6heWRhHHJMsh2jPDl3Q4gBTj_gKOqudCEUBbSPtA9liL2dUoygtAUKsfPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyvnmKD9wqQIKN0cBByW4g4qrBGAP7VY4vO-S-tWC41gU34Ymbuu8eOQHn3xPl-RkVV_ZKMQYjKZkXQrWuwO1qJRFIUzvZcYqQBHXjtK1dZe-_PPIJGgzVYUhQjx1BdkvkucBSr7xhbv5mkjskxV0jNW-2pcwz9DOUoM_tmZpcCBzc7E0CiNN6-gzk7nIXGSpDEHlqYMcvxhd4pFU_5JPpsVjj2H1QWYK7XTjmX-3h2xICYXtZHcWFAd2yzP29ba90sNrc3jrJXZpGWaNwC4__i5DXusrrGWFiJI5yF5HHg5Z1maxKqGPd3tZ_EK2QxvAV2ieXvAiURs56kGDBFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22639">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/persiana_Soccer/22639" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1dtHW8VMVFsF89PWJJU_RwtBAo0K8iEo5NK2bI2qnb5fE8tHa-9_u25r_xZ_RKdcs-MjaM6BNZZqV-m9xCsczxSRbP0kTCewANbk3WnSK35hfNH8Ws4-QmUkfTkyUfpRZ6cCQnPcqF1aQ7zLvVqUSPxHFjHRp502OoOWX1Kr6vNvu2Z7xrv_aIWu7i3rp7g3NrG_Mjhl11t94_7d7CnyoEZewgxmXRari7BVsi8o6hShQM6M8hHaDPpbzBhdLhtD_7ukFosFtiYwCyyv4V9u7h7oVmJXt-gJESMqUM5MlIkr7fci3yy5wMV7c_l2BJBsQSOL7D5UAvlFoI-B8fErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjKyGkH1w3cSDTVPVY5tPhu0P0mBlEV4svmTwSulYy-wbwNHQhm__-B-Ivy-SBiTilQ5008y7g_vtfJiI_NfVyaERD0gMM5lFoyy3x4m7BQX-cHPJAp-IjeTwtokr83b_A5Mfv_TG51G207DVXu6Vuyvw3X7vo_O61eXeINTdWGKeK8zsx4Zb7vmsRny2fg3kmZIVh0FDswGcB--kenbx2IOW8PeAwuXFlcq4KipovrkzxWvuX8q7F1mAF9P1sgJrmzsdYdNxtH2BWFvyPh-p8EEKVCq8PbeCjp9hSuoPzpwfVSQ8icehmD1xmPtzSBmvnZfbWnG_jyF080Ycldn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvTQA67cJr-m2v2QuE2OK-4yMCnwZujUKvQ8PK_f4IxJQ9Ig90fkYrzhLORfu_jX9J2nWZs12Mqfs6WbC6zLco8CgKx2ntUbrDstq8lhUB84AfXh58XbcPQgPOtrUAlezKrSPfF0XLQS6CPgrvXNV-mmqpjzLe9RY5y49KKZ_HCCC5zKbW0-o7FmbR-i5v6TJf61F1zk9sPksYlWJJTZIZoR2QZubFBcuX66lGqdFw_ANWxwa6QbCYkqfolzV_RP5oxBWYmg7-uN1oM4FjQj3kvObYWKY2Omezzqbv8AC5H-34ielCdyTVR4XIgap11wA5btt65WqM1bKwV4cnKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4576fhAYUxv0_-4pRiJxIHEqRTUA5tqv7ad8uAI4XDNX8ch2yOTrOyXnYjNfqP9Lfx1XiM1FFKtRDxQjk3yRhml3N0GhrdXRy_uNovgEEiqU1aPEpg5tMuiDQW2bTnIGgAbcL3ey-ptJn11QbMLFSg765q5zJ6VAdCnQSWHDV6P1MdaNTPIL313fnMJbjThBv-0mEtmBV3FKbut6mE3fMRExm44ngqs71FlpBWuL78ZBEXbAsy8qNAcKtC07QgOLPPfqfgYTK1hv6ou6Cnv4TXzNh5WTySyqRqWc044EdbTtSL_GGxWYrshUG88y27CrNOIq97vB3NNtwuOaoaU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhpB1sWc1xYlWPXwGeFG49gWd6xB4TtXyCxlU5-l1R0EU5BSkE-129LuEB0vypQGO_7FPQGsY9x_wiBKy5PrkuShYpi6M-eAzyjJV-E6wnjAOto2z1uzLu2aPAs3tbKdYbzuNwitiyBb9H8PvZqLEVFgJAbe7UJCwpXnKv0yibN_8vnWNxSPfY-G5c3ftERnwS350jrVaNBqOo8K0uT_9pDHMFnqSC4sgsNjrmEw3ZzPIin4eruXX6BV9o-gchtq06EBP5chFVLWqBes0Lpt6CQQZ6TSRicBI0tKXJH0t1Zgamy5VTQ_t8NEuadUrCK-Xmy-ebrvdo0CQmAcKkOsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22627" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ax3W7fdpQ-zMR0HBfRmSjxd8QJjwhxZ84DPZ06fbtzgNsS4jxIopj4Y-hkZ8ftjw62c_i9kQ5KdWzND6zHCJf6Bv0h_ZOXkkWRPR0xf7CGLTaT5xpjYmIkBAFXplhtnWLFuUJakSTDwqMfhdl7Lrv9P9a0rQ_NNYXM_uLbSDAI9obSu2nw9E5H-qNLCSFHcT4M0ISU8DeKVxo95_clTmPcdonrd1aIUwwyp3CxZHnCmYf0i4JTHAleAXO8NRI1fU6NyciuXYoYEQ7OW0_QnwQ-fibHfCpd9Q_C8YRX-p59yzKuJtbScvSjyVKZSyWPLxaw53Jk_ZiRLD-sDF_Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZJzVAlZoJZzCgMpuAC4X3NfTMivdxdG_e6_9bHc_UTUPsmZzfruZslHNxhrsFSZe7fr1NRERJ7_S4Liw-lKMJ4zNNBz7DzmtNOIYFTGU1GGiko14_UlpYioILFVjfAwBC7YgVGAfEHcSkQccYRTSauZRgdsPTwIiz0AW1FqhUtjT5m61Fhk9fCQywfUtAfClA_IYSHHLIKLhX6bCVKEL2rgB-lHBb4NnXFS4etBSfkTjiFTO_CKYJ59zBAadwnp_5kFLnmBFdSQDVWY2fDOeuc5Bsn8p0MCj5v4y1TKUivzGsEimEu98WrdvfP46r0gW4ClAzS1WgItxDXitBbOgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhyhuPcZx75u1KkHIU5Y8z_Mapy9shyJJFMSTtI-eN9Jvo3qv50YDp0bOgBek6Blj91gXejpz4ceAqnIs9bO8eZ2IGMJwxLlXiJ8s1qCrTGGp_FHZ2iIDiLQNMV9xKH2mlgTdpTwRP4QyviuxyW1Yp_eJHffphI5qArsIKwMEfS5cG_sMF29aOqcahbNlfuuo2PZa1OyV_T_Q5JXOUwjv4qCWK83HlmcQUEfuo_kuFhVO4f36WDwupXaUaTMir0K5XJVTDWhoA1QVzVphcHbDgTW2rnXfgJuGbyw5afEVBs0mFi8evG2FnVlSYJvVY2oYQmhRwaD4yt3hAH-VOYUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVNsB-fNrSCzAXOWlPISA5S4YQXEpWr4f1ME0SS_XvwgEO-SRCMATIJ3--tBwHiYNOiVWqg827Qjvaqm2ys8Rn_itggZ5gAS4xgD7HsiHZeDWzJVndt_arsrqo8g34aa2KRTrDFyv0k9YSNzVZDtMh5XED_i0qBc79GNceIspV1XobQXPkT-ixNpHDj6_xLN7VaAQeKOrPogobIGjJXEzkd6OgPWvh1dCHL-DK-wnUOYrgBdR93k4Tyoi9VGS7FStVlTBNopLNAjNGdUrL5rWWuHaX_tdUm_Y5-6qKiRqf5VQdvzDDNGjrCdBN64Qn51ikOiHh4UAHuF0y_sZTXecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6P4e4sMLT2jqpnHE_7BAlNGAv8HsuqDHVen1zj7QnuUYoq_YvRA5Q-uoaAY9chY4mPHa0nyxS8HqnfwmSBiwQTAxsc-o6jeVZozWSmChoKqMSinLoWGF6Q10JJ5m_97Bil8W1YubdTcf634mhCcSYHtqmO9qFQhIZYPTxmYtHZ4z_vF5KzHnCJsEHe_EPOUtS_4Qs23KSPULgTltgSklSfMToP8yZAJeOLyftFBQQ48lkPIULDdeCXEIZT-GS36iZG_e-M2GrmK-RHoKViFhDbZw0NUXP11glKYaycVcpd0zvbeUAFmB-QH7rAuB8JemtOGNB15O1P_Eg-Fdsw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVBDLvOMun8BJmxklwXxFKc7G5d4nsJP1kaGC5Y5FS_961hwYPj79x407SXN8jWn5-PqgdqJ72FRgZi5hsRAv2V1qOyH3q6DEbNXEHWDBNr8AriamQE45v8N9CqqYrbB6m9YkJvrDovTpyd1o6YXRd02uip4WEV82-ixjGZ8vrJQ7q0VrnoPrT4yU45S-ENzS0OXBTWTmmM94SXJo5c05RF3Ky5kJ90kzHxpEd7smfY_c-8KnMk-mBJqFqVqao25eIj63ApGLc0_LdUm4ZWC6voBPpJgWgELQDUeD00_k9p_jW5GJuFYSuOM76H_l2N-VqWM6EskIvquzC-5UkZuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpkT1zhZdySiKQk8anZYSobG0fOlAejBtp_tBuf8sv1bsL2M3dsrIjd63mFPoWK5z0GvMi-XXehTXN6x3Z4rCemWJTk6ncFVMWMOsCkjMsqGid6LpggueOKEvQkHXhe8XwTQmv6c5cfwi70RhWmxk3Avx-Lkef3iL3jgAstmwcKUMScSOXJ1V5e0c-JGpAhaPxg9QOGfxfM8AHtiZrDijmue2NQdUvoUcNS9gP-qasZvhT0KVbOYB5yheBpVTUGY83US0wndlFVqH99MFNUT2CIvkjvRSyMcGbnjPalbzOEsKLcd3cSnVz8QCHrUmOwK1Q-EKI-_eQZIyweNf1Ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=aj6-5cg_sTJ7iYBrng8W7NvrvygJVm_PJBcOhqWM_K1GqNedizNZpkKytH634onBq8PiY7oY1gh3KFy6ve-nlZ47ylLOsdY58JQ3Yq354MgOQj7PYyYYsEdvFWQfEOd0MQUJhHqA8sASdObNqyQEolt10lkWO2pe6Jk-kjSzAwWI0FLfT_8H1MiSOmnnOuS8ukyQo-SSMfww-PBms581KAKnAsX619tmLiiVBW9hzUB1ILTbp7eaeS-kd3S0UDuAzcxrv1qLc2H4J9Vfowlq607MBRokMITgYqKgkIi_eOKS6wYDzGENBBBFwESkyi_3utQb2hpf2ePMZxFQ1RpbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=aj6-5cg_sTJ7iYBrng8W7NvrvygJVm_PJBcOhqWM_K1GqNedizNZpkKytH634onBq8PiY7oY1gh3KFy6ve-nlZ47ylLOsdY58JQ3Yq354MgOQj7PYyYYsEdvFWQfEOd0MQUJhHqA8sASdObNqyQEolt10lkWO2pe6Jk-kjSzAwWI0FLfT_8H1MiSOmnnOuS8ukyQo-SSMfww-PBms581KAKnAsX619tmLiiVBW9hzUB1ILTbp7eaeS-kd3S0UDuAzcxrv1qLc2H4J9Vfowlq607MBRokMITgYqKgkIi_eOKS6wYDzGENBBBFwESkyi_3utQb2hpf2ePMZxFQ1RpbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb3szWmW03vpmLsEk9QoDWQl_hBpeLSsv5dq6KxTbQEppTJpDGqVE0ty2kyUuEGE2ULHvng9xyu3F0sJCkCyADagOLWxYJvuYBJgyu8ry6lLN41UmnZ60UsHLTqoiouKx_3WBl-rouEwBS2NSeZPmFyLK20pBGi7zNtzcWPmCADFcwjsDpysn520L1_dNAvFW58ABRouEAC9ontYm9b-ZsuhxzcByZ7eoyfLCGfhKV7shGtSF3C2Org-p7ujOjAbXCJO4WnHZTrVLJiuzou3sNy6tr1FRbp_lCnlHKT_C0ZSgnhgFIE572F_vv5LHa82V3_zh0MQRw5wFtInnJ0aIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnV7e5B5XFyspuQTtklCbixb0WYriKHY4JdYU_WXAT7mmTTRDHuBxkHgcX4DZlaVc7FilECHkGWuVL4s5kbZTAJl5SXey9krNfpWFCiQo1nBLCjP0d71pFwSgNI9VlTYUUMd90VTvi6FEZ1k1pHgV-7K554NarLI-QUzrAPyD2flnLQ-FtoLMvdIu9OC20Aa9WVFxFRhcAbRV844q-lrwUVBgeVBfROhxA2LfelFtavCSmzbl-m_ZMzKYxKN-ZFd-NfoGl6vU_Orxl9fNy76TbFdo9Rw7TvO5a6OweWTE0ldoxZUWvjnVdY7bVNvkOlAz541bcRQhAblEWbcWWApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjCgXEGwL0cxVl1UjbBeL45JH00BVtlQfQzDwvYjbxSO-ZxrVEDuPDH22JOElrX2lRSIjVwfJ6ZWAjJ5_eiEuRRyUAXIlxJbM0G18XpDD4uczL0xp56fxbb3e1kozq7txcbTZzATJ6WX8uha7dK0Jvxrj2AAiHkJ2mLKq_76IDlBLlI7ByH4gOtwzsxtHIVCr8bStWMHATiEBRoFL8ayssgSgwr70NaXrVD9w2zYny2xrByhgoNZcRj7pYSwS3R0uxivFP_F1fVicQEAhDZOUVGVKoxcq7zVQtoGyzAek_HOtyDxmNPLbjhJGZINnbH5Jk0DeVmjD0VhVXIxVn9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWHX7F-2L-PMavmcDyo7LIqG0OG_wJsFbX4bKshDoHBhxxQTNPrhmUa8VoX9ALP7Fgp9j3K1fO2a_bqDMIuizrl8vrXEV3zWf3CWslOSiZE0DNbFlFRoHVeNfQpLWhsbtQOwKFTnsycokOfd3Np4_tOQm17niUQ3fkta9nASfyhfvCAVTkhVTQNWj9v3xEdu8C3EBCmVbKYhS4XCCTab8mpTLU7OKhOTwJ9Gu7_kyBUaHEGZ9WpgXd9tfJk-u1h8g5OoFlP2OkEU0_T4CuyE4w8dkQ_JbVU8nGUAHu219_tBaZ8LdET0WreaKSt5dU8PebokQaz7ZVPOmZwh1de8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilL9sAH4jZXNqcPQgPMj5bBljx3EQqzE8rslRThrmEHw1j2C_NKOz-iVqhFzvgC1qcIC72hSoBKFQDqrNWOBNIXkij0lkyyzdbiMfxyU3yIFiAdp9_5aSMYudFZs5V50IwoJSg2AcFU9G_NuN6USITdSH8P1tcFoNpmYmAZaMg5S-i54fdaTrlkOrf3pMAuwL5wxJf8l971tJa4c26nn88-aOgd2mYnbmQ9UTtR3erRWhBpfzVUggsQz2PtwhXIpr8QrrwkjWyRAaMC2uX_vppY5H4RGCD2EU7OFdDLrejh_qe_ah15198GZcHSWPfvUJ6k_5_G-1V_lb5IrQBe_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU4GYgPP1JaVsmISPk_khWNCBE1PRLUuyCRDxT9JjpkiSw-Wf3rzEqiWGa_8Cm9DG0DngIfth5xTdMIPDi25GFdJ-KjoyJs7HFkrBnOsnNk9pfClTVmQL90Asu0iAZIRJOytxySZdBfd6Eusdp2gL_pJxNQr2F7s6VaRoxraWUbNPjB7flkEkRNi7xt6c7KrOox2z0Us4p13VzZhEgHj_fWTRsgtiYFGxb0RiJUhHpADkStMa832Mp4RRginZFNObSqRPowK8tj0MfOJladMkRZGiOxA_CTXkYOioE4zeli-aY2h9uVQw7Eia-_k63UDyVd5ce99PmM8Rr4pxbxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dip2crMiWFBTlMNz-TVjOkkeeG7v8S8MndOHcr01_Gzp5JEk7JdwqbjUb_LZabwHIYuGzcvdpliF8GbOO0DK3bGEYtIisORHWtPSidiXjeV96J6A_liIYEAOKCuEQ9pjNWDate2l3Dl4caXVPkDq9AsYn3F91GKyJM7kbnJWcBAlS9FdS-MsdfgBQGQRDzfFCY0D4s8ruWVrWHZEDKA3Puup9a0T9tGbZ8ZQfDWhfE_LzkoL_kohJXXW4q07o2sBP2FKPS_xddpYnfBxYQrGlwNMEDRdVg4J9dZwNC0bc0pdJAWXVSm2Bis9a6uey7Jlq2cDIuT1WYRxJ2bi6Ppjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLuAjEhE76IpGXoAKSGjT85gTFr1dktcAVO5SYiEqUk-R70h4Z4px6xB_VMGheDnC6MA7dsYnl7Kw0ZlcFfUIw85x5iY9SIGsFfY1rQZI9FxiFFsOB0z2Ya8npB9kPoNzacoTlkUxsR_9zBsrXmt3F74HASCbr1YxicDmgARWcmWCZmHKtx3E8GprT7ltk8qlORO3duhwMTQ98cR7Ac5a1Jt2lEH3SwovRzG12Wwo0fYtvqe9bUyqhI2acUBbTIN2hSQ8BSu1RsIed_7U-NWgoS0Kp5NH1FxEkH1Ot_aLkOTeuDc8uDzJB-LLo-LSCZ-32M4NgYHbssV9TW2WjYYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDXj_JAbw6OtlwZr0Xf0ntkZ5dL38CgpjCAG-QDCix7Q-o0wo2yk6dZeDH-JXsPfOBbfz8kmcmQGPf3UJdzGAaTWtFxJfXMrrw_JBFlk563lS2HqPn6VIYpqqwxI-iznL8xddlpSfbhMmtF5puCQ-hPsJM67iH6TuDqqh2DdeCIecEvLKH-8lATyeNa4LUacMK1ZlET_NiKZ44r7N3tqGUrjU83PBlg47QDRrMNqE9Ega9ULvxHxbeUnftpxD7ahjtsyNR0arhwcdL_OzsobtQRbDp1jRfFNXU7MA92COQC3snQm2PTMeDrNLdKJWjX8O3P4CfQMICvUOe4qFAf_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs7aXxbGX-9Wv4c_Tfjq3Z7bfKiAfvkfkePVEzJEHyOlcHmdzBDSfPzQ5Wod7uvW__ZoohE9YHv0PKNtIBXBoevklAw6KP0-gqkXUXwx3rm_MKewAaOrnVzAn41-DwAOXWbssnXWLf3xkuXZuT1wpDeAhHb3QGnQ_76hFHBwhWmZ7c6NhtU_w5C_spK_QEqmelWBASFWU2Pz7ffhu5XV3sED02rsobs5OPy32lpSTI2F6AXhrlYuQmpyLnzEPRcpekjsWLD0SnqgBeSOLmB7B2Of43MsoFcLlrXF39_nkMGoXA506rZw6XEM06Wxz_j8q4rXEPPFgDx8m_vT7I8tRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=tsdtlvYf5Q4ztE5fAIMoGNHMB7bi36PvmA1p9tUYt_1-2c6lMuqxpB7nner85g59f3HjZ-9EpXLMaQ0oKtH9IdcGN1XIawfmb-jYyvyAUIu_JnWzoQrIV8ki68mjyHGnixf4Bk3mSZrLN4ED-MwUROqS3UYBtp4vxd--IPI2KL2FDBBABX64mGU7ek1rVgieookPOZe7mvQVKTzL0-ORoOwp7L-q2t5goGbWLRrPD-gt9Litjqu_eHCbezNchm0E7mMeuqeQrLXYz2lfd71mmK6HtaCNVgGBT-2ST0z-MnYEpkKryZXzJaD1Ue3Nn3jNApga24xbbmuCuVYqla1Imw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=tsdtlvYf5Q4ztE5fAIMoGNHMB7bi36PvmA1p9tUYt_1-2c6lMuqxpB7nner85g59f3HjZ-9EpXLMaQ0oKtH9IdcGN1XIawfmb-jYyvyAUIu_JnWzoQrIV8ki68mjyHGnixf4Bk3mSZrLN4ED-MwUROqS3UYBtp4vxd--IPI2KL2FDBBABX64mGU7ek1rVgieookPOZe7mvQVKTzL0-ORoOwp7L-q2t5goGbWLRrPD-gt9Litjqu_eHCbezNchm0E7mMeuqeQrLXYz2lfd71mmK6HtaCNVgGBT-2ST0z-MnYEpkKryZXzJaD1Ue3Nn3jNApga24xbbmuCuVYqla1Imw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MoP2_YasLZTuHVrcG4ZUaFvrzc4TfZVwRQ9aMphQCAvCheYNyu43tSz3sweX8pQ9DWSBPws6gSbtNvsfE9bhysc6AeTpP6GH_7144ay70-1flQhY4Z6siMSt2q_n1l1EtNo1cQ-_EhkuVq31Ls4nNmK6p1dzkh8wuLQCxotLbK9dY3pFRqEARZpTGvNQL1MmqBYiDjs4DbvAKkFhebGkPpgQM9A1fFfHv_Nq7lj9wvg2X1-YREaX7TUW471sxE-pIybrmOkR-F9Zcr7uIRwCXV77GsANeNWBdFJLqiy0_KTGZds67jkrncliLtkzWcQXavenXD-_lhf4p0D8KQW8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MoP2_YasLZTuHVrcG4ZUaFvrzc4TfZVwRQ9aMphQCAvCheYNyu43tSz3sweX8pQ9DWSBPws6gSbtNvsfE9bhysc6AeTpP6GH_7144ay70-1flQhY4Z6siMSt2q_n1l1EtNo1cQ-_EhkuVq31Ls4nNmK6p1dzkh8wuLQCxotLbK9dY3pFRqEARZpTGvNQL1MmqBYiDjs4DbvAKkFhebGkPpgQM9A1fFfHv_Nq7lj9wvg2X1-YREaX7TUW471sxE-pIybrmOkR-F9Zcr7uIRwCXV77GsANeNWBdFJLqiy0_KTGZds67jkrncliLtkzWcQXavenXD-_lhf4p0D8KQW8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfq0sfFpSiZ4DBFVjepFjvRlsGRmYinx1vKR7CzSCxcgwDmNg2mgXb4-NhgDGJvhuuYaoco_iO42f6zMcWi8fS377CSOc7HGH05NPs1MF1IdyslI5e8cI0ZmQF12Ll8KeJFkc-PKI5bK3s4Z17imcSzLK5Vnkg3VOl3m42dzsHzSa_6nvI8ilK4yN4dMo63kGbbh5UJG7xfJ9y6dem7ukINpimQsXM97LAb70m2DqlHwM4qbl8nVlbO5Z3BcUeHmdLu_oHNCV2TS1UGl5Z2CDHuGg4jev2GQT0SXISEjjTXVbDZ-cCHwAvCHT_L_gTrU17xAcO8v53oDWlOMAHLd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=iUpM6yqvsmbqolPxynxRKxkhncvUYr6dd-gQTCBJzPLGdIBG9rZGmXp5pUQAqvDdBLXbZuKe5it7QlScYYqk7I0sW4xaw__q1rIGAIKcLNqYsL81efHzS9yN_O__Z7wHDQZcZca9GFjIBajIHOhmCVBShvEa2Ru2XSesYFO2UfKmLp6aleDcPHcAsI1RdLWVhCpE2WzAEa8lLMgaezW7EE_Jmfxj_AKTVC5DgsSEhGBL8-IGNyc7B1ObNxmhHkty9gGgKA0sws1gLBMfKQuGVMO4AFt4py5ETOB_WLRBNrJksZrblgBQsynuKbUlhca_1cwGjFNdCWp4oSgvxeXIqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=iUpM6yqvsmbqolPxynxRKxkhncvUYr6dd-gQTCBJzPLGdIBG9rZGmXp5pUQAqvDdBLXbZuKe5it7QlScYYqk7I0sW4xaw__q1rIGAIKcLNqYsL81efHzS9yN_O__Z7wHDQZcZca9GFjIBajIHOhmCVBShvEa2Ru2XSesYFO2UfKmLp6aleDcPHcAsI1RdLWVhCpE2WzAEa8lLMgaezW7EE_Jmfxj_AKTVC5DgsSEhGBL8-IGNyc7B1ObNxmhHkty9gGgKA0sws1gLBMfKQuGVMO4AFt4py5ETOB_WLRBNrJksZrblgBQsynuKbUlhca_1cwGjFNdCWp4oSgvxeXIqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxvYnzmJ-QtQaN0p2S7e7t7F85J4PA81uh1Uy0wMe3b8jEVWSm2kf-ziT_CX_CQujdfTE5-fO-0Gtuzh_W8TauXw8vL-NvjW8EKBUL2txP8rZZCxO5uCNBcJIks7KusCd2InTW2Rc1JC1_pWWguw6TD68NssRVW3931NabHPoEpsT52x12ciRiHT6eCObyhwhfI175rbkV47iS85OAU26aFb0q-MVU-mVi3d2bDML8OB1TfXckY7p025ld0V4wBtYK8J8v2cuf5cAg9hKBE8acjelBip-bTxqvUAOce7PsW4ETtFdaQCytRyu_zfV-WHLOC3gWULN9WxK2snKJDEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSRFgWDptkbFCzADVO_Y_UO9xO0hHLZuX2F7cHgWU9RCjsErKE8fdx2UcQxoEl5lortecCprLRJBhOZxu5wrDDN2zm1PuQwAC3EiO7fWJ2BJ-mcVe1v0fu3JmHT6pKbfmHGSyPy8xk-kE-ISCMZbvp0YV6YI90UWXDpg2rWQIvb0-3w2ibQ5YC1fmhWwNWGdbN7GrMEdfB1isZb1tc5bJrtzy7LEM7dm6IQrKgd4AK-gvfZ--2dqsex9xDBwoD5BmqNZWrIep98LK2sGPtHJB9jOov3VOWf6mv2ZSwfaKpZUB7SbW4jpYfBFy72aZfmLyEM12Ah-GxPzqYd4ETLIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=jqkS3-QBfHezS4rbDEJOm1k1-MeDinFfQsmGNoirJmpfhUdUgFS6TIN-YhK-ALhje1NNDZHCr4qJgLOdRueZmv2BI1ofFOvlEwvjid438Di8n6wGwvhqh_Ct8oMNatwMqWpYJmS_6U3AhauAsk5K1xGpTPo8PHvkh7FuC-28WLmL0ktmIMacIW_RRyThNdwb2Jvp3Vbyqc5K8USXoaNKTvZbsTFruioAfM8WPFfJ-LC9n-GKuATFqzRYdvHcoxBCUf93zEl7LhVmpiY4KEn0xqA0dU-r6ZOCRpdIemBabvSDGu7H1EqOJ9Y6GASluURPSmhQc8w_E0MpQzWr64LuyEbueg-Z-QDl065vUGae0XfBOyeI5P5xSTwL2PKovxW6OGvYKZ2yinb8DFReMsGucDRRh11kLJ85673f2AWpvB4AyFHDuAhEgkZ3d_St8TSM7bt-BPibsoUWr7pq1zUsN7T1oMlQpPKPLR3zx1Qnu3wqB6Gyg_3c5GB5wgbX9CGsv924y0YaxUPB4xdLNxxE8UQrmqd4wtU1jWvtVNrOTDjpTPhrSf85IuEKcMNk_tyqg3N7Y0o0gJnSz7wug95H--mcaRNLY3xeOwX9WiceB7kGjeTmMNmqxLnZ4xGDrpI8va7ucjLGo7cvn9cj_vhPLn4CB2p_SifIe2_YFjGhbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=jqkS3-QBfHezS4rbDEJOm1k1-MeDinFfQsmGNoirJmpfhUdUgFS6TIN-YhK-ALhje1NNDZHCr4qJgLOdRueZmv2BI1ofFOvlEwvjid438Di8n6wGwvhqh_Ct8oMNatwMqWpYJmS_6U3AhauAsk5K1xGpTPo8PHvkh7FuC-28WLmL0ktmIMacIW_RRyThNdwb2Jvp3Vbyqc5K8USXoaNKTvZbsTFruioAfM8WPFfJ-LC9n-GKuATFqzRYdvHcoxBCUf93zEl7LhVmpiY4KEn0xqA0dU-r6ZOCRpdIemBabvSDGu7H1EqOJ9Y6GASluURPSmhQc8w_E0MpQzWr64LuyEbueg-Z-QDl065vUGae0XfBOyeI5P5xSTwL2PKovxW6OGvYKZ2yinb8DFReMsGucDRRh11kLJ85673f2AWpvB4AyFHDuAhEgkZ3d_St8TSM7bt-BPibsoUWr7pq1zUsN7T1oMlQpPKPLR3zx1Qnu3wqB6Gyg_3c5GB5wgbX9CGsv924y0YaxUPB4xdLNxxE8UQrmqd4wtU1jWvtVNrOTDjpTPhrSf85IuEKcMNk_tyqg3N7Y0o0gJnSz7wug95H--mcaRNLY3xeOwX9WiceB7kGjeTmMNmqxLnZ4xGDrpI8va7ucjLGo7cvn9cj_vhPLn4CB2p_SifIe2_YFjGhbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaUxmAqEKG6jU7Beuq_sPhggmvGZRyks6C5GwHtrUEZqfOcJKuOWNf1ivSLERGfefsxTibNbO9iZgqLopYVYK28cO3SM7bEm0GiouOFqH6xRbQBjicFo5Sn-qDEJw4B1LU0YaXzUxtqO9fUbDspp-19KBHNlmcB0AI-_eBbaf1Vh-nICVpjXJAG8lUmb5ebyOSAl7uz-WVn7JGa7Qr1KqQY5sFHNH2jzLIWCvZ36DFzADh33kayyOg9owGF810Dzx4Ze2BMxXUCrxc_CZA2SRkGIDLfQkk6MCBKxhaxBDe_3tKTQwZTFuMtcjMHMIUIaXdkcgc-IIrN97k1-Mt7QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URToScZ0gG1eXqHYZAja9XIGEkKFNFIEW4fSN5Cn3KB76aWx1vO5dQelLRR5mWIdk7hUpM8bitaqQQV95jjLQoOZIambuagygKdNkQAunpwvc893RdLYyx71LOHQrawPOKugLnXttyGN0jenZN_75V13WsiEbUxu4kBM0uW90UqpLvbNITt1WFnyNuEel9bSL8IqJxFT7ZnoTocSPlbx-qOFlNwYNHeWRLq8nSOiGDip-4ziGeTB3yIRxXiiGJeRA7nRPyPriQp0dx2uMVJrTXnKbsnUaJs8T3VRT7KnlEHrIMe3f9zsU9IgNlgBSKo_C3jA9e-Ag6mwHSEn91MpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edxEYLnGU2CMwZV8qQZJn0iuzi_KZ5QbH2C16zlP6fxEdsP1esc4xsrlaZwZx0UhFXQ82GVGS5PD-lB_j9K9S5_DBx38LgNn75T2AfRGlp_6uyL3qyPY0QjJSiTOptU7aaFcA30jUXpqtQOmRtM6PcsEHGx20jLQziwzkL8SELGXwaqKUZcfl-3AoIIbK8kTBE31i1mug_47S2i0jvSWZ-qqW1-FMfk3GxpWUFlvzO4Q7cKzd5MQrSe1aJDRodMilsXmBNh4iNvX_q9h-KilqE0ypMp7EATFOZCJQVCASV6PzfBHTHogF0XVDA4wP1ilqIaVzBMOHDF76DebUrKjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p__xcxDA2wNqJNmM1F70uui7Jhe6rjSVydCWUjoqwhriHYXUk-ikI_Ry_8IZRT_3fgT829u6YJN2lr37uiJHJHpOd7E2nkNHM_vCbBlrbWkE7wfBbSvwTRv7R46WBOFoStkwuCAUOZ9aPhK_nHV15YHwGvdhdvoIzXCiXoraGYr_kYU47hEBCWyb8CPjzR-ATCeHZ7fq2wa4gTDPuDh0vnrdHv9AtchR6lidI81PiViKcIKbUyPU6Ye0nsiByyjsFvQLc9cGnHyj7D1A73ULifP7KF_3pLcHX0cKerQ1Jzxti0Ho5DJlkOUXbksFsXxyZyHteJE0KHIayXWgQk8UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc7wbwb5mHG-Iqzho_QSy356-ZPuTet9CD2Vx0K2Iz89GqBHIgAw1Kc3UvFOyzHKXey8Ry5z3kSxM3l9VQwASJfGPaBn8htmUODs7bTlXCfFWAAX2GYOy7y-FUgfLZraHhEtB1RbIybiuimRwaoAFzMtBaQfUzvgFOpf_O_DH4HgKoRNGHiyMKphBpP-RZShBezx4uRSxGQwm_cY_V6mZ6nIDX82JH370PuWvCz_78uGkT0Y3iTwISnoSAGglc3dO3n7ZL_YY7Vp1c7F54lWeHPTlkC_rZftfnKVbudrTzJjPEWw_fh2IYHzu-reusN9xjZUz6ewCjJlZDcAyWQJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=rvM63zeejXLh2P3CL6YTs08qUpEqu9RkW1cWgVvnQoWnY-mIlewjYsPPVFeil4bQHIHwibQU8LpCUkxLr80EwP_JVNqkVRsnkFRGDtuCw-PKytGQ6kK2l-GQgUZG5AU-HTds-PKdr5RdYJeQWEzfmXmon42OUFxaym8xlkg3biI_oI60vBokwVUx2xzna5d7pjDl974ZVPzvL8cUjMrIZR9MjA9CluBMqNbNMKmfYuQrCZYO6TCpAWiTiSIrlRjv9_OGb4d7VGubFHvL7-jhW3eGGtGpUvPI1V-EgTPRbxNUROZVTi5Wh-m-zMC_gWLJGOCbF_uya-nQ5nxs85Mf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=rvM63zeejXLh2P3CL6YTs08qUpEqu9RkW1cWgVvnQoWnY-mIlewjYsPPVFeil4bQHIHwibQU8LpCUkxLr80EwP_JVNqkVRsnkFRGDtuCw-PKytGQ6kK2l-GQgUZG5AU-HTds-PKdr5RdYJeQWEzfmXmon42OUFxaym8xlkg3biI_oI60vBokwVUx2xzna5d7pjDl974ZVPzvL8cUjMrIZR9MjA9CluBMqNbNMKmfYuQrCZYO6TCpAWiTiSIrlRjv9_OGb4d7VGubFHvL7-jhW3eGGtGpUvPI1V-EgTPRbxNUROZVTi5Wh-m-zMC_gWLJGOCbF_uya-nQ5nxs85Mf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgCnRRyLGKJxUeTXLkJR99DUJL1l_w0_m1BLGV3bb7lbf2ENAAHk0TTroiatFYaW5yoZhEDPvrWkJGe-d8pidd2-HmrV635wK7zRXhzTLcAmmpcMbN0Ly7ZGhjZnN1oKeX3rgvp686wLSo2Ue6Xy7pcY71pSRjaEXpqb-kNNfz7RALZy1dhk9pc7aCpoYLXX8QYUCeCJeyrNKrFKzIrqIpf4HgqHctQ34yda1QVBYy7Fv9Ven8nF9gWQiOqF7_4MH3peBdl8-S9etITj7dFGKrJgf2leEMW6AlcN9WMYRWJyuhaj83vvfb9YyiXWE3zeKE969ULAOEtII1V3Ftd_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAf4evg3BeTC5n7GMOeq3ZV-9NHUVeallLyMXH0d_-6yqw15PgP-skp1eAcKhW7clWVXnfEWRkqrdPLJG1mrXnkU0fwJ9M8si40JST-AAggbF0oPh-Clu41k9IbAHzfzvGmLMqahxiBXHaZJR4O1B_jtP_PaP726BJzP2qTG_aT1a2w5NpAmUfZPSq2RfwhT3EnmBr0bGwyz-9PZ98d8qSYniwOofFCLr0S1x5PM_M8YvSrDdHvB5lWTdn9CB-MuPKh0oDyzb7Zo9WYe71jcbBpUzcXMKiXq_8TwfbVB0MwsLnP645fmPT8iGgJ0IdjO5s0vp_Gc90rOsg_jeASFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X32CDIjc0sXtoGGrOMKhlADzL8f2ecxIHLUeulwEdQWIu4zPyVyrEw_sQSkzBdBcL9JZpCmUh0wNRGLCrMwh4WskUMr3uSA5fgTIEUEEdXrm_szMTJ8vi1lVueJmIwIrS62DED8hs301ZfrbeUxwL2tO6hsueWaLehEnxQKpE4giDjoEDkrsZd_bd1dC0mPCibEW1isw5A_FL489Q7HNAxEGVbb8v1ZawIboAGQRApynTP0oj2DMAdg4GGhKIjbFPj-_u8WVsB8jtloSYBlVI5w_PBwzE6wnnMlam6DyipG1uEYoePhGkYpXbIchBHlH67SDLa09eRQh2SrGLxcLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zuta6vzO7GoncmxcVfj_Hix6pW7DL5ZcDcpIOBec1kr8kPso3yR4KopLgnrDzsr69Oos-tBr9gOYsXk1CrFjqC_dxQN4uSnDC1fe3G04RI9J9l2rZqw4ab4Q5N0xUu39qAbAQl2oeQWtgPsHS1Em7JOmhHJlk0kQi0_Qc4GpkUoKDaGSZ9sE3cbQ_pRTKIJb8_psbl2FV_rRsSJYt-CH4JiEDbs9vtYDFyZUC4f4mU46eh9eL7QB_BDfR50m_ofNVVa_G-456bbnOOzBoTs0B1vk3CDk0ASH6b3TzD-yImBOkQd5oucIlytWnnnQLlOxaMZ0Pr0TBALAXmWN35GDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk8Vk91-2HDKE4k8hTYzSnF9ObA5t5o5g0DbRJd5X43RPkjgeBTiHso0UDauYEV8lZ071wNmgOKPJzfAcQkhnVQd1EOQLHaGRvHNgXN5Be8y-z0NH3DjBSNiHXojH4XUsoSsYx4aLnmiRcOiPrwojQxVeIR-V9rGnN_qQ_JgDNgSASmqsNbai53eQepwrw51sokBtz4nx8hOAKcKs-z-35InuLJzNayB-jJfC-fQJS29VJVC3eSqBA0jgEIU00oyArTIuo6qbQ_vUghzOeof-K-tz3upMAOm9LYGK2hfy0RuDCPGZwxAf0fIvcZ5wEMSDwFgxRrbQDQ7JN7vGpqBqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk4k2R_zfZp7sm_TdSwudMMTUIb4IM1FjTtPHfPi82Dh3-LZFpSQUTtRX4CGx4tCjuONRV1jtQiLPXnVJTxgCpBjMna2yWnfZ1w5nDNlIm8-Qte3y3WP-3X4ENIo5otgk3Xrtm0aqzZWcWcLBTYX6MTFO0t-Qw45xW1m75LLyrkaLvf2ote-g9ssFX4lYPd5OuPNrQFhQu5pGZam02aeNlh4EtKEbeWv7wlD15Xf5scinbExXIWGD_H9xa7sYun_FVm4-QDsmUlLZ0My1bsvjr1vxme71q7VKxdaaw3fP1ln8WCi8TrzgFxKO9CbJNvCJxlPpNaI1a-p60Sn_YFsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=OCkn_Pkhhl6hAWAo5wJGoYDQyVQd5pYrYq5ssm1vQsEMwzaCDB6nqu6WGEsuoc5K_9RSnJlbaMonTuiYFQha_iS37yBj1wN4MGCxfHntovs9BTsaUmk5zcBmk94xi6CFB7qFFWnBF0eak7pRRyyZsd2uudlpwpNXI-XEnyX4WEooVJS2b-HgIWHil6grlG_Ubbl2o_sETbPAnymK4GSgzR3CDRDBnnqZ6W6bJ5zfHlqknihwBu1ax-Dt19qwscGFN6J_YB9ISXPcDZWdlHuq6ghn7A4rOh90EeQrnYt13-f480V28BUuhsKRMUxCUD0bmg51-45QQgwA9j27j3Xb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=OCkn_Pkhhl6hAWAo5wJGoYDQyVQd5pYrYq5ssm1vQsEMwzaCDB6nqu6WGEsuoc5K_9RSnJlbaMonTuiYFQha_iS37yBj1wN4MGCxfHntovs9BTsaUmk5zcBmk94xi6CFB7qFFWnBF0eak7pRRyyZsd2uudlpwpNXI-XEnyX4WEooVJS2b-HgIWHil6grlG_Ubbl2o_sETbPAnymK4GSgzR3CDRDBnnqZ6W6bJ5zfHlqknihwBu1ax-Dt19qwscGFN6J_YB9ISXPcDZWdlHuq6ghn7A4rOh90EeQrnYt13-f480V28BUuhsKRMUxCUD0bmg51-45QQgwA9j27j3Xb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB3otKRfpVoVAIrByZlhPo5_Mm-cr4X5naXTsZGADwq0bckx3T_VqfD6ewztOZ2B1KKEM_ag-WPLi0POQwXg0QAuq-HldvWj28UaOf_xsoLzoEorDz25l5-lW6vmAMMNYCSGzMBmrbrKZ29eOvbTfByQVA-xBfs3qIZjUO9HSoyWkGGGXER-683aWzLLQY7hWM0PkdGWhDBXQnm_edDptEcgQX9KO5Zhsg77wPYj6Y-uoMyAxM057BR4uL4HiTL5lCnOvcVh8cfHsYgS4q-uWaNmNiT5cvXB6n4awPn6EJ9R9cjfFvuAxbgIMvkUFVCWgT7L9ou4K-foEu1nDKZKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFSe8_LZOPBnZqRlcJTD5KxWcl6GSiOgTepq-6HewvmaD2bMuOOWKzR-P8kzQz_shT0hJabo7e8hb0E6EY1KiiLlQivNIltgUaIAJ3qt4L3B_eqmLQuYtsuHbmW0MI5S0rVPRuL04H1Z4h1kA10-xwGLH37_PZgpzalH3RUdk-TRfOATFO5M9eyacwxD8m3lq-Ae5shD74t59EBIZPoTXyHH_KY4VciCqCk9MtRYjm4YGASdUiq73bP0Wp_uF5VLcgtSr2fCOxGx-MrKuH96oCCOibNpIO8kCWfkk64pc-NjHLKBTh5U5EYnLqKXBWXbgE8yzt3EpwiWwkCv4tcRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhhCnGl08o_ocl-2nCnz97OBW0SR8VjgSsn2v8zhoqlX51S5M1O3VcGKLRLweE1rpiE_38lEMGdvl8aLELRw3IFjantZj1CkWQj--dM8qEXGzy-Rx5ubmX4F0c0xN_MX1AngfSmj47Tzd8Qn5D14QZrBzG-i2YTlV1YRJY_zWnYpn2oGjMizDHLkD1wcTtw4VcvPYw34kSf0v63LamD_6x584-6ru97-CDsbM7UmEMPS1tJK5XC08EMHCkDn63Kfzt9M9BVuVT8aK68-bUd2TP2E2E1NAULdkeRPfPDiTgAnrL4O3gnwTGFE1_zOOfQhMyE2MLxO3ru9cbgHarDAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=md3cVinPGNMX6OFbaoaZAL_XeH4kFl0t34Tk3pQxGPuK0ZyEd868219YpOaM9Hzv9isQ3f52Cy4M4PmNl9sTfTgr4Pjbv_6NbRW9eAmJfvJyfJGnH-EBcvDUXgMsalS6LDx412qnp2feH_6f9-MAgh4vUFWQWMTprcHG8cEEqu6CUMJ5d0aJ2wFcWtSneITI75Y-3jdAECQO4jyeAjJeh9AzmCLae9fSyg5ADpRYbMxMh7eesJRnkrrOSjho134v6bJ-3ZByReiy-VwExerr6QmEvfGlwHjOrYL_yVHZYQvOk1AhvlK63Ro8vOED5q6F2xEA-HYjW3urTpGrZcJ-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=md3cVinPGNMX6OFbaoaZAL_XeH4kFl0t34Tk3pQxGPuK0ZyEd868219YpOaM9Hzv9isQ3f52Cy4M4PmNl9sTfTgr4Pjbv_6NbRW9eAmJfvJyfJGnH-EBcvDUXgMsalS6LDx412qnp2feH_6f9-MAgh4vUFWQWMTprcHG8cEEqu6CUMJ5d0aJ2wFcWtSneITI75Y-3jdAECQO4jyeAjJeh9AzmCLae9fSyg5ADpRYbMxMh7eesJRnkrrOSjho134v6bJ-3ZByReiy-VwExerr6QmEvfGlwHjOrYL_yVHZYQvOk1AhvlK63Ro8vOED5q6F2xEA-HYjW3urTpGrZcJ-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPYNM3t6lWayjYTIyJr4EVlcChWfNRXet3GuLcwnaLSAY9WKLOTkQgqbJyU4XyZKELr1I1KftFc7UJJOKqCE5FruXp29NTeDJeOg-H_pUavVab5DKm_HxZK-XSNiSDIDryh1N665JJB43sXScANAWKOYvojcH8I1hoyjVbT7aR5uYsSrsreGunjONhMAAlxDo1qgK0gKKiDrjN2vbC9hN9SPVbiDlZ4Ww3XJhRooViaLlUhZxgbfgEl3-ZU3Wf07oxr_0svJ4A6bzw02vYNLIQ7WXOW7bNFczo7_emy8OJi1oYWTmyeufoWTpRT9nxxluMZmzr8VeLdchAieB2lYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrYEI_7u2_y41DpoBR9qvCHcBV9hcrzAgcWpOd-fBOEysyeQ4sRTPl1HiR4XbLmkGhW8c5eCuacOFKv3BPeFPZk7eXqGb4gzrgWeqc1KgHbLMvb2zlO13b90o2XgC0qF8AWQNX7hf-ajY1arfWBgkmMvOAtSTxCG4cMeBSTYyZGXp6QcP5xGBeKEND-7lj_qMXVEIkvUrWLy6l-CXQ7qWAelK9gsXF_RynCBNEfDXpIjg5JjBdk8O6to1fqSXJIE1Ye_ipAhadkp82PZk1vNjfO_Yg9hzYINwzG59QvYtVy9w4edkOV5t7n-VEXFDtQPt-2PUs-E0pPBemJgDmxV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCX36jcTk2K10x5vaGvSjO4X0gCHSbXthzQm5_BQPXbOJeM-mFuUXKM_rI8ucKJvJAUAXZ7n5n8u5Vth5mIzhwvipSmZv2B3ECRKkHzc43OZn1LXaeT0fCTbXJWf3EVxNevI0o-d5MppR3kcMDYZCY5uy24Why_0QhpRThv3touBZeXJqEd3tZvu4Jk-cSMjUQGAx4NqGJ4wpEXE9NeWz4PUfNJ0cubF5fWnQ4eAOApfuyaBXVnYmjFtu8_bunzwldaz5UdKMVwOfPG-pq4E-olZhNkekBl671kjxCZ2phbbtSFUOOUMkhtZQfaNu4wa8VwV8ebm9bwetUh2IwwD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3hoPzonRG0WFDOYLKs3MJU4lxj6Khg5gw1qmUpqSl80V8tV02EMIox4GcuyEJjyuMTdSKN3QNBqUIcjRMGGNl5nr-awOQTPTiBhe-qnIo9vDn85Sb0M8yk2zppFCjDouelvQX3pWI9fin_BiFupUryifH6Ia-qXi7JMeK5GHIKUMIJOhs4Ly6QevWww0_XNAMY64LpXbL_o5xhOkzEdo1n_y3oejFTfGuZ4v05aLI6G27-f0TxEYtsYkkiYBfKtK3PnRZONlNFUEUIFUFUNAflO37GMp3_4dUvMLpsxJOJXrpkVYIJTUZolQdwe7n-JWkdc4RQQJuw5lWDnovUt7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOx6OYoeAqPlEsLYAs7JYDvXjOBgIKTSkpX5luaD9ZZorrxyulERkuP9T366vpHb4V-srTH_UTWxNR3KYG4sfTXTA4Vu2c2WEm-qcFFrjXyWurSd9JSYDiBGAPxh6Q5jN16V9PVVUdQJ2ZVrQ1GzIqpIPhCMqBD6rRIcYm9oKU2bbGtUqTevi6uWdAZVVTtkQ-wMCs_V7BxpC_MOXrjxUlaVhQO7_BR3Tpo3oKn2n4TYLNjN1KTFVV6qIyu8DhC5HCfxHduV0IJRw_yS868T9ndtz01vPv91suwXw-L0FjB6NjkuGLzb2Q10eUmhwQ44FS5Z678AnVcGBftAwkYzag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdFF06V_NUSrPmstYrW4LijYXgK1EPTB16tTT3595JVKF33kyZdo1HCOwRZE6Kx102mDo8s8PaRxwt2e6Wq3puPmh7CZhjGwZ8-TOi_5SSdagz4Wm9NgmKzKlwRDS-iqL1sYGQ190_e_eV4oVoCUcIjovrCUeY_xEQNl8UNg9oBRYWt4Ufky1-PynxyIoluAuc6XFEcDONKgb7bVqNeaBkZ1zZJJAVOI9OBcOoaFKpLO3Vpa76yhbMQbp7lHpICYQSC8l0YNUXBoZ2c9atAf8uap1guktf_wjE0yH0lMI1msJcEnKyrSiiuexvA0gno_5InvJJvzH2aqu4WUXORt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD9PAOxk8tEE-HyT7VkmxAumfuWysRK-QHIwLsv6AVD0yDIbkiGTGOx4M_Bc1eKQSLpw4OV-_sp3dZS_n6OTwrerKV84l7idiTUrJZjfwEKJUQGmnETz2f1kFx4AyzetYDzDOK4bcuaz_uRVxXotc0N-vHwj3V06qL1O9mZ6kDslGmR7WU3iTuya951pJxyqbpLnuwSxrZcuYvVzc4aE8-ahuM7zpGfYmajV5JnBblAFhGrLECaghGOOqN5ZwOgAYptE2mOVTN5sl6jjbxKohxLA4h8xENP1Bhodh-WkxGSOvj8AaxnyhjqP1AStCh7fFOjjqj-vdIgt9UuCmDsrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWumCoRyHWYpcIbnn8JtZEJPu1aAYPQM-RBgatzaUmRqb2f1wVbklpCWHCPwg7BpsyuJjvA2wYx5uS5zg6LmZ-AM6ouNRLT1LYlMkrVwFj_ZqdjjTXAow7tfp77Y2je-7G8YmxGP7V7P74fdHH3Ikwkh8Gpy-vlVKjluRUA0lGbiSG1HORDDrDYdEA3Ohb6M99BeUEALQL48Ju3P6ag0bKLruW3GkZC9XfIQ60c7KLWzKrMpmCCr8gB5J2dg5sL4TrQ1ZmWP-aa4GY9FI7jSuM4qpMKxObooMTieRaX919z3szykJaMYeeeSgyinr5IncPAJzyR-mAKaAZBDJd6x6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4rzRwGO1wCl8RP5FsdiVj4SAUcPPsSZlSdGLO3ieaSTYMQMpuSTRs1IpiwWwmK_vn9phKImEkakp0prWQh-5-zJfE0cIUWSG93tp33d6XwlOrrnE7mbosH0TN8TRzox7xGLZqf02ofXtVaDz8Frb7104M9C6JWn9dqXuv8Tw9JgbaF0ypJ__k9mlUNyts59Sh4ZYlhTnmgr1xW4_v6ObvlzoSfN-qClN_8gO3v_dMwsCkMzKcYRj4PZbkbc2IucbClqCbWuSS9STuET1wzfHH1vnM0qVVGUo5F-MzkHngMRub-f1y138e3YsrBhGpPbogoKv_qXAzyGVkktT553gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0_oOeL6O-6_yj1VPLdKECA3f3VCHyOEMX2q-I6C05YNrBv5woMhRTQDA09jbxnstpaxannGhkUShgfZZosY11LwiYo_bZ2piKi59mYOc858fC3wjhDn9SJRJ_EUF2Y6Js5vW8uYihMrsAtTuQWXxkywmx4XUk0FARbhMmspl9a5io5jDDLy5vEKudE3jHr5muVmVHTpE9rEOYd2GU-kzVLyGI6sNlLiDltYsgHLTbkUeSEExE7kKYopUZPjL9cSsCENggbmXgE8Y8NheD0q9TBj9j1-goKK0vRQJzOECAG5uZalD3CmrK8ig22hrj3TelSoFIcJHOvcr939eCH4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKHZSBehWmhILeXDbf82ijJ6ZJxB8hAre8jDVdGofdF0rtSMHWJY09RBZ6JMVb1BeeEMOHGCFlYhM5F3P57jwpW39TFYqeQAzS2dTKecKe4EWR3wm6xYKMFptKIYCoQ-LXAKuhAW8m273PVKKZbEb8l6fMMGjphmsW40raqxQPqTa9lkpkVr23Gz7WjfQ-j-tXgIBQsj5vLdVoP7uMacSY3227yd4yP-3Ncn2VD2V3BrkR9kIgYdemO1dAA0ssdSMmoBOdvmMfvlE35YE8W-ipo0XGYDWWGR3ZJqt0vYEC9A0sMkNIZYqksjjSeQQHikWbuvhhkY1tzYRpzWKi07eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAVcwFF-PRr29iQZ9uycEocTDx81oq7BsWAxGETWB1Y0CFvM82j1n_OEc7okZdQNUUwrJ6FImQbAGMsf2oK1eNls5YMV5oRc7lgxoUzZy320OPk2O5uF7kMZyEAEEJnOjfcJGjX8xlby7-6FdM9NOiB7xGna-wJ7w7kR1qO4h3zHzLeXRFtBXHJdc-3UfO44HiyZ9lhoYrUWT4ZRE4gsAgq5UVG2qxay6sYSxUvmLLJA5Nx8Fe4ipX1F9n-OEkpk6wDt29_Au_Rt7yg0Mr5hnA6YV-sKVDIuNcOP76Tja_-pjba7QP8s856KHaUa4iYTkRj0BnnGk4lkwhSGfQw9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfLL3-rgD_z2YC8tNc0UrLGQF-VWA4p-QAiPzxeLTqehLmlblrHy66E7Xvq6SeFJp4wzE3q8EdQ1l_U6Tyy_tsn1JmuGbViFgI5ZonQAOyKuCTkT6L2Qj1M6lSu8sfvFgIV107Y3KXSAlSm6VaznkJVkyGVrYgyYhfWTWBJvyfB4aBewzmQIB6uYQdZFDAPYa7rgHfTUttsiFycWtB8LadcGP0kM0_XPE_nkiPDEXNBBsjXCUAjfB5jW21wLbg-JUdVy8-I_TttotXCSEXbRNZufNTpa33lEdPNtGBQNiBXqerX9OK9OOngUEUR8TrohSd-BUj8rRfkkhBKJRggoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUwUTZrl6dYxOIdaCg9PIAKDkewXtNTisNol1juRLzjEP3Z-me_Oo0zBkeQHNTmZoeLRK8kX67oqwR2U_1YpvJQzdy5hfJ8_Yk1AcWitPv8d6ZVNhjaPQOF9Kc5m3hEfUZeLZnc4uSwSeaz2xVnNu8FCUrYemvmfLkr-5T0r8nvSi-WHynV_NONbeQO0dlzbFoHs7IkWAU0wNwn9Qn6sQ9v2uX8_ClfJ6xIAg0RkyT2lW0vLEeeHB31jMnLw5uwBerU1OJHRRoD9fA2WLpP11Cwd8XCLu0NVZu1KaDZAAorygjlEn059nRt1-uO-EkpgmjLrNZiL5AfOS-J-Pgsuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAH3tpXIpGt2V0X-pCFdkg8NSgnQI3kchDjvRMqQanL3uCKB5ljbPxnQxl3od07nEb_WhLCbsYySA_pD5w2E4lWnnzS73V9G7DwFfbISScvMjzNobF3NnF7ae4vNnZMn08n7vN322c98lnwPptq715ReXn3V8NREdPIzWo984m4pxf26m51CpgZwofC0XtMJn_W7UUKinhd_7Cq9zV0db3BUuzXAE5Ap_rWfjbeQh8nlA0BgDeZq6vf59cu5qntiNZd6h6vULnZ6--KSXW4LWpyrv1GKTl_aKe4ejBdBS7uJX05ZQ0Jwr3Ru5xvmiW7Pt18tgWyBtTOd_2ttR2rUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U45tzjb3jrXUqtswNC9m41SGShM6GOljK-ZaiDw3ddvEymHlQEgiFHhuQor-ZTHqi6NDj7Bkh09Rm3DmU8kqi44GWzDh4fmUK_r78Vbhl0cWiOa-dVS04lPCxC5RcZXmFTf5cYO6iV8buaMARHqZZreSch4gYbJ8qoaue1eBSHYgKTJFkt0nzaNJri8YywyvmSu8EqsPwkeAjhi-5SGF0gdjM2HspLmwMLnbEMJ1YpwAucaBZ0xGVn65FItaL4Dg_SNXAA-_UGbKLEABNly_wdvhjNzTe5vsbBNzEqZ2WBlGNcPonb7jKCLnsH5S7k62EgpUxP8U7IaZJAJqHGgbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQqs6DfT33UumwWocTLVTlOY4tQfeKCfq_2p3GOYNu7f4AcYKLVBoS0bjPAvHm1cOnmRFvEMrIG06YeDFVLpXeRrOcp5PGNuo1LfZGMgOaV5FiOriuP753WG_b4rRw4HJmwM5arFAAhjk5KNKMbuz-bpP5wpEt1R-hMEDRPgEX8Y1r-jvcemGyJNJZNxxpA_KE-ZAvOjg4EXTVnQ2Rqj5cZvo12tqdbqEbTZfpJtZg-VjhD31mSWEr1rigYfswOZ8QL5mWNSzN5GI_7n_OMv6skmgHKTqDqeEkiKIUW8mrbbJJDGSHwUMVcVpJeEnpAebbLGpcm7-ur1E_Lrw5OPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgzG7okefyd3u0rd3ABUvLOOLk2eLyTFJkBMk5K3UFWciLjXlLX6NNWkQsOb4anw3l6wRAvVoPX7aW_GePCPH8cikmcFJ5-fB0Xgg9Y2tZXH9S4UvR0Ehbl7vIGL3GBhrgZECTMiWqU3EK3X_we9OlCrhQfW_BIUGOFbOMpbFnRnIfe87VqgjcfiXSTQc8U9R7tDUy642Bd1rYz2IzqjV6M7LvXXLaAbZBGcVz2GGwYluSLKOuvl5IQ-ZE_rC0mIJ7mxdplrPXLa1rpHO2eo3kBm1H36OrsQBAUB-XDVu8-ZILfMQTz1x8EQgGrZMVKYv2KVtjKgrOx-_0-cJdYzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGQLHF4FOPlKdyroG4oWAQPtq_7gX11FewLWFtgJHTZflEPK1tBq_0EpAQ1QBoZ-DVgk4l4X61fXbsOXmhZnmgSAroaZaQ7YlVf4NtmszhcTRK08HbI0OBIjrsR9M6EF2QrJZe-fmbvNEPdVHl3Ohi9F5ALoetxeqnAHc_lodxc5yPjjMOfHs5PxkAPMn9Jq1roA2Fj7gmNj-L37WemZcJR9mucrvqeHsjXsO5xqB-91rneS18EDM37KViIXG7TAEcry3ceO-TGWavwi0GswHSKsMWvtd1cbfSDYLp3YlfMzIU_ST4MwaKvVRPyJpuBF6LjueKgwJnHfFf98LJ1HEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7d11aWk1udvmOSfXUpIj5LC8AxmeCh_1GaPPtfnSHMFqqbXfccU6BqmOvrTZ3g_dVAsoMrEoXbmKjdluQLR1H5Oeq-sUu02W7j8yeMcEF1OZa1W8_xrOtLJLF2Mx2AdTjyIBEJ9m3TfQchledVeSc_ULg772R40buXK9CjGB1vbrESnXy6I7qUhiCzBMZ9RIrGj6QIlGEFRlKRktWt9htHrGqUMGuajv6l-bzUZtflXjVkJGPECAqA19u3D9sfTdU_j_bruV2tj2p8MTiegqMuNoNlZVzTnm-UZNyyDuYudrKWy46FJbWtcayOJvu85GUahUfOcNyYo4AoWKwXD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=LetmEbW7fwmSiZ3kbqdrIWmYceyPfOTXupb1ygOMPtOOHT3vDxxPAGT2rcwoWELF3WaFtal4WEEvEAeKPJKKv4AlM6AAllCbY3wB9gLqJx2uVOEPok7ZuPVJOhzu3ip0PDlQijIOxvkHFWjcpYON6ZyEeJWwM5cLVZpYLTpe2UVpCvCYbCOdDl1dC77BNqwKWMjSx-YLYHmai3h16WmFOjpHMNV4MyfjcelhhWZQHDfRmKy23rcZo5u9bkH9soFS_uDT2B1hXTerDeZJFCVhXXNzsJn3yYOpPsc1SoOo3TpdsP3VhxxFT2l_hIzvDEnomF6ZZSREsP65iy07PMbbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=LetmEbW7fwmSiZ3kbqdrIWmYceyPfOTXupb1ygOMPtOOHT3vDxxPAGT2rcwoWELF3WaFtal4WEEvEAeKPJKKv4AlM6AAllCbY3wB9gLqJx2uVOEPok7ZuPVJOhzu3ip0PDlQijIOxvkHFWjcpYON6ZyEeJWwM5cLVZpYLTpe2UVpCvCYbCOdDl1dC77BNqwKWMjSx-YLYHmai3h16WmFOjpHMNV4MyfjcelhhWZQHDfRmKy23rcZo5u9bkH9soFS_uDT2B1hXTerDeZJFCVhXXNzsJn3yYOpPsc1SoOo3TpdsP3VhxxFT2l_hIzvDEnomF6ZZSREsP65iy07PMbbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MznmeTcozM8fkJtEfL9q-tnWLw0mJxNq6HBifv_qpOqTXCKrKAwlXrFRQplecVQJy6VIEXnJeqwQYdAOu1O6DyZpXizRT13erjUw4o1Wi-xgwBji47uoN6fGHp1-Ozx-Xoe3QtrILTxKvlrHRMKh4YZbWM5y9Bj33R41kejuzKwE4mjvR_gMBLEWfOLQBUDt5rnIzBBB2rw-OtuQ2lDDlYoVAl2kNlKxsb4S6ycHoDwV7onZJe2LsPszzqmnt2UFFUnunE99pCWUydj7H4YA41CuzQ1EWW8Dj0klMFpAvykLVR4b-YH821zrzsvtjpgPsfC-8MJcbCiJ19_9TWi8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcTpsHsbQEny9wtfb52u3MYrQxylFWST2vVdFqDkairvmPueTbIZ_JLFT2ynR10mTrq7hmI7IEFQS3HcRPjw9duyseF8H4efrPULPVcKHtAzhiWr30QCgSqlXT0pDtwmoWGYHfDBKOIJwe-d1Yt6NaM0dXpJiVHEAJa39R8XwQi3PJRwg1dc2iWd6lctp1PSsX2FXs7WZ2iLkqRKgU11Fvb-n32ZiP8JRyoIxKGQ5VqtfaUHJ2eoqlz6IINcScQT0dhl8U7kHxYBqs0t-f2ewT7nScKyYzYVaBKsp1ILtisL9dHReRz3gqLTDlsnzkaEqSq0b5I6d3e-NhIw8Me7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUJsyYgqh5LLoPnMc_IAQpJjZ65HUW3fV6p8WtSQq_e0lReKbdlW8GwYi6wiEaKTBez87LdIZ1PIfeK7j-LnYQ-pBDaWIL9ft2yRc8m5XKp3JkxTT6h2VXnRqSlKh6eYa14xDhzNiCGLz7NVRh56fjIJIQyH3I0lbkdyP4KYVQ6Dd2aeeAWa1jX9-WO0yDELQVdHN8sW715DopWfnxElQWsPGw4jezbwTW1VJSjtJlIt6wTIEqVjpN_8Xg9-olytskArxxzcUuZRESPZ8BxkhqbSPlXbbTfzK3cV3mw6UDzOt17U3kAvZxAwuoaOZYHb4T8l7lZFEJ1ZSTl7m2hv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XSo8AfKs9TpAr-MPGNc11J6GWz965SvIOmQADX0MM1RVR2vXygwOwmxi0A4z2-q2HmXLfY4RfLqB082QezRgKWC-VRhk-pHW6soGgPbEY6sIDsGsWyHmDZaGHyakR_UU_pp_j1MXdZTrIyvz0Y3a7BiWt3KYUzdpAdae-GdtQt3TIAnwy1SrmRE672O98PJUnJjhyomGeZu8-Zrjmac4bKdP_hxyV8FQymd1ixQzQQCsY6PqVwdHeOAWmRcZqzpW1Dg__DyHVDbC__2WXr8n_Qex0xLE2LmCj5h3idIMZAPiaqB2KLm43fO_WyRRiBa_zjMRNd1xp40nY8PSf9W4qIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XSo8AfKs9TpAr-MPGNc11J6GWz965SvIOmQADX0MM1RVR2vXygwOwmxi0A4z2-q2HmXLfY4RfLqB082QezRgKWC-VRhk-pHW6soGgPbEY6sIDsGsWyHmDZaGHyakR_UU_pp_j1MXdZTrIyvz0Y3a7BiWt3KYUzdpAdae-GdtQt3TIAnwy1SrmRE672O98PJUnJjhyomGeZu8-Zrjmac4bKdP_hxyV8FQymd1ixQzQQCsY6PqVwdHeOAWmRcZqzpW1Dg__DyHVDbC__2WXr8n_Qex0xLE2LmCj5h3idIMZAPiaqB2KLm43fO_WyRRiBa_zjMRNd1xp40nY8PSf9W4qIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=bOfbqYLv6I4VqtyhMzZeVF8cLLXLxZGLF9I1e8Npx-BxyHN_ydTOAXrOECsnmN4x950SJtykxy3netZK9qP8Z_BC41vQ0ljYEM7b1WY19zfQ6i_-EiLIj43W-NWY7_31hlzztvsXBzXMQaTkj85hhZwug6RicBBLedflAx_vosJkS8bnp1IRc5hjJSQZiJoWcOIl5LgCJSaf2gXhjDwNJNIcKbLoKya0wY1kKH6F8QGyNbm5gL3C5LfeRdP0iH4L9iI37s9RRlnbLuj83tZlw2aLEronWhwkW00b-MHaXag-5EacOMqiylU4ze2mgSqXnwc-w1H51moX1BMWCsS7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=bOfbqYLv6I4VqtyhMzZeVF8cLLXLxZGLF9I1e8Npx-BxyHN_ydTOAXrOECsnmN4x950SJtykxy3netZK9qP8Z_BC41vQ0ljYEM7b1WY19zfQ6i_-EiLIj43W-NWY7_31hlzztvsXBzXMQaTkj85hhZwug6RicBBLedflAx_vosJkS8bnp1IRc5hjJSQZiJoWcOIl5LgCJSaf2gXhjDwNJNIcKbLoKya0wY1kKH6F8QGyNbm5gL3C5LfeRdP0iH4L9iI37s9RRlnbLuj83tZlw2aLEronWhwkW00b-MHaXag-5EacOMqiylU4ze2mgSqXnwc-w1H51moX1BMWCsS7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=HG5fDlQB5KHDZkkHtCX63xJQl84Tc0rncMiYo-Bq0DQi1afBZxzffFqFMOJOsduwCecvaAWRG5RCeFmtLK4v32iqxQmD5jmtVv9IElFoj-oKCEyNYVL_9PYowG88NnUjNDU7tnUHPhc5xVf5NCnEm-wlp_kbwsXPTF7DmcC_d-xSNp3QBd6neNsBd9zAcbQvD1PnPOcMO1Ic-eKid4QDTyT_5AZQOockK2xYs-Dm6KcxSr9HBWraJuRwnIY6Jkkxi_6SwA4JA9_CBuA61CWx6SFrDbwI5i1t3Ynzf5q2smyrnCGLsGRZ21jOtIPFqxsjwJ4IZpgONKBssqV1Gd18BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=HG5fDlQB5KHDZkkHtCX63xJQl84Tc0rncMiYo-Bq0DQi1afBZxzffFqFMOJOsduwCecvaAWRG5RCeFmtLK4v32iqxQmD5jmtVv9IElFoj-oKCEyNYVL_9PYowG88NnUjNDU7tnUHPhc5xVf5NCnEm-wlp_kbwsXPTF7DmcC_d-xSNp3QBd6neNsBd9zAcbQvD1PnPOcMO1Ic-eKid4QDTyT_5AZQOockK2xYs-Dm6KcxSr9HBWraJuRwnIY6Jkkxi_6SwA4JA9_CBuA61CWx6SFrDbwI5i1t3Ynzf5q2smyrnCGLsGRZ21jOtIPFqxsjwJ4IZpgONKBssqV1Gd18BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1cZJSjQYUBzPUD76oSZxTIl5a2G-_yVlqFdtBZOBv-lvasTjT_xq5RfHhwXBD0Jn-706_gsdeoYnJ9G9lqaosoPa-EOLt-jsVXzPgB3zLkx1pr0POAx88XJKvlBhG4P1keVEQvgdbodZz7mzQHF0MuZe1Vw5u2TVu0de9Y5Sos2NRkiqfdlWvSNZ5Cv7e1x87Ci5Gijtl7WrfpyOOZe_CvRkFXVWVDrvx_ceYMhxCP89JVtPqAdMQUXlT_YCz53k0YjF0JcIR-tZoT6yv3GJ9WyWROyZ26yEQicTq7RHy9tnW-6UBW5ugFOuXylOpPKuvig9zimrgwbxc4En3L7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjWtShxrQ1FzWk7lqhP_y2N4TnN8j7K9HqsHBRZ2phcP9aMcYOd0s3FNB-j7_0vPOzmzP_4TBfH7_5N1Vf2uS5ZZW_78dJccLaEBQ2dnW0nq0daVyswin0O62z7q_Uhe4MpLyvwl0TCWNpLJY2UsSNlKbY1Q4snGnewujHeXl7MWM12MwSIqXB_KJP1V9o9w8Rc-VM-d2dyO2TpltGcOYIHFp0MdE4PMZOuJTM9jqjU3nfIi4sA4WL4N15kJoPJDYAFYiW0cQrXNOKmsJbK9jD3L848-xsw1pvTzltvrHWViKj1kg9nOYYOxiIIYIIU-EgVsCEx0R402i_KPXxuzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U80soUGibQfOU7Fi6CI1XnSVs-4w-L2rRaVukXTrGzxuNiJjYk8uAjViWl_IbEcpUA20NbauOHUc8GM8Ht1HL6VRLwxLTOf5qbZmxbcWE20zy0ojsInImkBTNYa7mI6ePq1pYPiNFpeJvy1LiuteFVZfHBVi_UzekW7vf44w7R0G3QyPB8_0hDVgpeRX77t71sEAnhJovZO3DwvZLYVTmXf8CqY4jOsE_YroSy_2QqK5lsdH054qDIfllyeaGDkJnWUD0dDxPgBaxe6wbGgsN81Jp3RyPzbz8hVfypGu1EV7sYP2vmZwDIKT7Sodc3QmoVbMjBxnVWWyPNeTeYLfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU2VsYMn6LQFEM_RJIWDjqroTj3FIo-Qs812I9O0nxVPnKaTuCN8IPT3P8kKqeCUXsC_nfuUAb8vWLvg4aVB4Wb2LMz5rw8cmPYkD4pHK6i8Mi-Tn09-o1arVX8FZczWmnV7WAq9CvclUDws5Eoy0cgakfk8s0uLnx3qcuKlJyIR_e2Dvz0J3M0YwIx4S56e8nt7015oBHNEaZPZ2JLMGKHR86TAoJLUlVnHXHbpUCTtDfqhNKFkTgKY39iocJTHCugdI9KSBd4ozJjp1SKFOG19mDsprhCQ9RGZrNVikarPAB1o4tyfB68q9bvTCo_bXjK_KjQBiZyFKVUFQxErVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlYnYJriJtNVcbG6pKuoaCd3MHXryWq7Xhen0OIshzGQh01wnO7hJaeSLvaJqNP7xaVDOYutrkiO1vmenEFndkrB8MQenOLVun72lZLWOEEKscP5jOtM2i8z7zcj6vw4L6WYftJkAEBSpyfIa5tspUFQW55FAQvFErJi4oX5I_tyC0Te_8r3I0FWTa-FUr6u3cbDnXjm8-FYEjeGYcJx-vvwvmFeyZQi5OkvkRwV9Cw1iLlVWH4PPaQ8RhhlCdDYvnYlxGOZJNuxs2OQi4-HXLjFLsHtxsscBDXZIvgjlgYfnOo3FqRS8a_IS1egTCN8d3NnNGX85g9LazRzbNReTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3Wy9Rsn1bigmB64bKoOZ7Qja-Bo4fPj0C5S1Veh5viB4rGgW658OR5IvsVvNpDzT8eaRGlTBl-HylLinFTdGH27BhunUTvdUTR5urGat7vo_zjxfEuSRNRkf2SHtyZVVZLmM3twtq5Ju-jfq0Cwf9qlVORahxTR79ennXh2XY1nGAOp1WcwoLL1r8bUZJHeihFAy27HsDuYiobXuKW3f4l-gvxN5I0I1s6nNNFRNapatGqPjSXd1XMhsrLTiWb8q8W2julpqPX5G-nm2nYcZHSaVvHrz-u1nHfRYlmqUY9KwP6Kl02oQALBvg2pDp05oafHM_WfQOpox7__O-2XqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubKhZ_ATEW6ANqsmV9M1hlQyE9Iw7DCWY2QWSdHsWIFsuGHr00prs70h4q_qXAJ52rbn12xTrEpMXyb3WBnrr0gQHak1b3l_1S7mw_wVIKGkwts4o4nACHxgREQPK4DQkq0A6upAGcziPObvwvQdC1iZMH3dd6uGFLB1IvxHnVIDpW7VmKJksVcsmKTz6nqFhOtM3Qdj_bRfXfQjPUazaL0WicdPFPkgRBwlPJVmVUEASfR_ebY7xFBnldHzWicexJ5MTzu7UYmwJC9rnuTlQrUvVx6aE5DeeM8vu_s9GPgWau2ljDpz1O_PHHifc-mjffwWrdB-jHwr8i61ezMjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USTcNFtf5c6wxrETSqiq4XrcZ0p9AhesZF_zDMHrBXBNsX-FKXU38Me0Q1NFkrmMgJi4bRnYwgrQk6ZbHX4yUMQYyYc-UZ-6n0TQfxz6lZlEmKnftkTxxpm1PFQNHpQ1AystHZsi0Mos90qVOAaRrx0vyobknV9qVCyON7KGtJQHpnynLK2cJ7HddUVl2ePSRDkmBTmRM3a8LPHUHQIPyIEKgGwcORIx_73RNyuPu5ZzlrWs-eazwV7FBb3R7toqWvRwba2Aa6FzAVyw0ikgf0BFgIl2P__CmWENdHJBy9L4fUynRED9H9D2gfrMsp1AbmAPuPYwbPfaM4mKSc6M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=NmXzR6G1ZXG1m5N62BeXKZJI6UNrF1xwlIsNBc8xcgUGSB7Trfw6c3Au0GepDmVn25JTwSz9qVq3hHSDs61N-Z8ngV6XkpqxmHMoHGJGoFknimBsSRnSxN618CS6AbFUhclgGRluJRhDEXb323AJS0B7LxF8p_MWYL9yPd7WtSrfR_tRIkkr8fA-twMvJ3s8156kgUHPYDL7B9TySyc0c1V7i6iASI3XmuNoDeJ56VFEJq-KcJUwDQ3abU5GI8ySHC3FpzpyMCl0uWQBiQuQmrzgPNoC_Z0D-jL9rZjmXIh4DmwF6WsAIRcnT_-pbvFY9XLtPopWS3huVa0reDTqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=NmXzR6G1ZXG1m5N62BeXKZJI6UNrF1xwlIsNBc8xcgUGSB7Trfw6c3Au0GepDmVn25JTwSz9qVq3hHSDs61N-Z8ngV6XkpqxmHMoHGJGoFknimBsSRnSxN618CS6AbFUhclgGRluJRhDEXb323AJS0B7LxF8p_MWYL9yPd7WtSrfR_tRIkkr8fA-twMvJ3s8156kgUHPYDL7B9TySyc0c1V7i6iASI3XmuNoDeJ56VFEJq-KcJUwDQ3abU5GI8ySHC3FpzpyMCl0uWQBiQuQmrzgPNoC_Z0D-jL9rZjmXIh4DmwF6WsAIRcnT_-pbvFY9XLtPopWS3huVa0reDTqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLCfkm1RAX24NZK1OGtjyHIM55p3bcz5exqOmmttzTIN8mogmxS1NCam4PhAOvCSyaeSzj96JKCzOJ8y9dfkp6pVpOb_lFsrDpZ6yraskqKTfB1bs9TZR4udfYjyhSs03EvhONTP9LUCco9aPKLPNq69vg8vxe4ld-goMlQgh_nYnlLNTeEcm39BwdhSOzRzoUj0Cud5qJjW0__kSQAOW7Gt2dIf4gWfCzDi2JpzOSbR3AlhPzAc5j5YVQY-NgJWybeDIE0BRXHB6u2jvkAhnEOWCxerJ789X3DlQmYYiTNewhLMqstqhm13ZSZESr2zZuQv1fwMNvB1jQoGbfWfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=EGdjRqpfg1qxusKGZmCiS3AzHLpR5QzEKJr82Cp8XafSzphch9weab8DCOKBU3Np6t-v9fuMw4ZsNgyYlZtZIyFF_RlH5s0b_31-UPqYkARVhlLUPwXyXKeKncb5dZGhHbAExmLDfPNdIG32HpqsUKVkrPQhblEA7kiO5lH3F0Hj4NKiiG_qayP6jdL8yqVzSBxzJiH4S5KgZYowySkgTnFmue-1Ok8C0ZTHN2_HPpEgnXnahzma8LhttOEzlMHo7PictL948-Tx7Z0VH3BmAPSigG2oqWEyK_brW80wGjc02s9fQ9P3kxCt9skrYBwQ1ozglN9ePdCfOieR197ExmUw-77SJQWNyOzF9JU93bm8XlvKm1p8YLMN8mASoTe1xx2mnzWjBR1n0qxpaBl91cQtLHP63gowHfZbH_rwoPzUDouK1g9FTdu2hP8INKa5NUmx4OPH2LNrk8cLpga5iikYBxcOpETJ7x1qWtgq6vJzptQpvPJ7r38qR1l7lr08nPs2WlrXRwiGy25jiEBmSptabhWXp-JlXdoWwqK-c1moydkCc4B9MfYngHetSi_zx8Xn2AVKD_WwpkZ95EQnlpN3T9LYdZh4hnG4bB9o6l03D46YWuvDk9HTM5eYDxMrFe-YmmB-U5YdZECTgcINmolv6hB3Onx4PXNUy3S_ISY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=EGdjRqpfg1qxusKGZmCiS3AzHLpR5QzEKJr82Cp8XafSzphch9weab8DCOKBU3Np6t-v9fuMw4ZsNgyYlZtZIyFF_RlH5s0b_31-UPqYkARVhlLUPwXyXKeKncb5dZGhHbAExmLDfPNdIG32HpqsUKVkrPQhblEA7kiO5lH3F0Hj4NKiiG_qayP6jdL8yqVzSBxzJiH4S5KgZYowySkgTnFmue-1Ok8C0ZTHN2_HPpEgnXnahzma8LhttOEzlMHo7PictL948-Tx7Z0VH3BmAPSigG2oqWEyK_brW80wGjc02s9fQ9P3kxCt9skrYBwQ1ozglN9ePdCfOieR197ExmUw-77SJQWNyOzF9JU93bm8XlvKm1p8YLMN8mASoTe1xx2mnzWjBR1n0qxpaBl91cQtLHP63gowHfZbH_rwoPzUDouK1g9FTdu2hP8INKa5NUmx4OPH2LNrk8cLpga5iikYBxcOpETJ7x1qWtgq6vJzptQpvPJ7r38qR1l7lr08nPs2WlrXRwiGy25jiEBmSptabhWXp-JlXdoWwqK-c1moydkCc4B9MfYngHetSi_zx8Xn2AVKD_WwpkZ95EQnlpN3T9LYdZh4hnG4bB9o6l03D46YWuvDk9HTM5eYDxMrFe-YmmB-U5YdZECTgcINmolv6hB3Onx4PXNUy3S_ISY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
