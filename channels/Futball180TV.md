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
<img src="https://cdn5.telesco.pe/file/V4lToKpjSDviDx3cL2dVUVl_BlVhYAOIAzmvbMWO2IwWQ4ZnQMiV5mPQrKwhdZseFAnRx_Kdyp4qUfDYmaiLuAPef37Wx6oicsKyX8VEGzByvNrWQs-bLlLiOBjPU0zfSdseHBx3wTcmkgrj3zkqZWr9NW6iLlUSIZ0ojH9G6FpIEzIzvff9zxgFt0R7TUmiQMHzGJaPMphIHvuR3b3KsfTftKIrlL4_8KjOONKLGf6gHzhFOQKoNpGSQwKru9VtBcShUFvc9X3HxVGA8w7xQUxs26fY1VwELmJWslRjdqjBWm9w7nSevNID7fHgOrmFTZhsIw0siuBInRdJRYtmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 421K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 02:34:10</div>
<hr>

<div class="tg-post" id="msg-105968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/105968" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYqYepU2n98kMU46HxqqguFnUEU0WjoV4l36dkfVzAWmUZMHUBHEl-l4edImunBZ1FjCn4bI1x_p5wRzlW8kHhKMkRaAm_YSx1CqEqVPOGZPWlt244u5m7jeKY880h8-sZpN6iUqNUWQXhpG2dwqXtAr9TBC7Flgt-zF-1JmUkuXAAxmtGbER3num0hcH8W_rwA4t63M_11QrzMQq1lJaIv1elPUbWG7XFMLs603sREcKlVpnDW3eUJ44o4kp-qwKT8UedyN-jcryud_7MChnitl-AVlCWL45q8uAcNoBpUYErF5Gd0MEuSJ5oEKXCSVMT8wZaYnGx67iCVOVyn8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/105967" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/105966" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خب دیگه بگیرید بخوابید. تا وقتی بی‌بی دست به کار نشه این موشک زدنا اسمش ترقه بازیه
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/105965" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
لحظه باز شدن موشک با کلاهک خوشه ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/105964" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
⭕️
⭕️
⭕️
یک منبع ایرانی نزدیک به سپاه جمهوری اسلامی: امشب از موشک‌های خیبرشکن استفاده کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/Futball180TV/105963" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تصاویر منتسب به حملات دقایقی قبل سپاه به مناطقی از اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/105962" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/105961" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXB6m2hnuFmfnUatvwHm6Go15NHTbzt77qN-yB8Cwl-P9w_uKIi7nLpd4BGuqCSHHN4k4gZXCv8NOM8RytViFBnChf1u3gidDGaZZFQtXGrPqEffd04nwaEYDshHnUNrMONT2VG_5YUNiWi0W8zlxHNuz52Ar0h21nP84T8jLhjyUwUhSRRQLuPoSwY0jjIOEExWe0IeuTKMrw717Tb5wJIgJ8fkOTfs8xO5cipYkCW89-FKGzQ9zoQPVcueWE4OZPaJ-nilAtQl-XzBqOXytW_ow0WbCxnC4cqaifAH8sID808OeN-FOd3BG4c_IQTjBamOby8OwitCVUWnQz-KXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/105960" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
گویا یه دونه موشک به پایگاه آمریکا تو اردن خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/105959" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/105958" target="_blank">📅 01:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🏆
ژوزه مورینیو: برنده توپ‌طلا؟ بنظرم کسی که یک فصل هیچ‌جامی نگرفته هم میتونه برنده بشه. نظرم بدون شک امباپه هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/105957" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران
به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/105956" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/105955" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=Bh5hnxRDrV4LvSrg13r7P7BnM-0lt8931Xm-DbP1AdfTMA-X5RsZmt7phOC08zS2vx5b-cfTaiTJ7KUblYvQiFAKxVQW29Wu2hMROcx-VONxVWgXabjbaLcrH6-n8sLc3QCYgsQQcVhSRskcQtFj9bcvghucnwqurMXZSyc5bKdsjC2RKvvTe35NNNjGLy40eAcHwgm6z8czSbj6yzq1QwLa66NEkQnrPRq877-xwM93CZ-u_HNDp1mo8tZxvOr3u0aqiCSpG0QauehcvURndXNcgmQWBCH4avVpu38MH9c7057XN_CuUS41kIqTM2nt3oSGdISRG_CFsjV_bGf3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=Bh5hnxRDrV4LvSrg13r7P7BnM-0lt8931Xm-DbP1AdfTMA-X5RsZmt7phOC08zS2vx5b-cfTaiTJ7KUblYvQiFAKxVQW29Wu2hMROcx-VONxVWgXabjbaLcrH6-n8sLc3QCYgsQQcVhSRskcQtFj9bcvghucnwqurMXZSyc5bKdsjC2RKvvTe35NNNjGLy40eAcHwgm6z8czSbj6yzq1QwLa66NEkQnrPRq877-xwM93CZ-u_HNDp1mo8tZxvOr3u0aqiCSpG0QauehcvURndXNcgmQWBCH4avVpu38MH9c7057XN_CuUS41kIqTM2nt3oSGdISRG_CFsjV_bGf3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/105954" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
صداوسیما: دقایقی‌پیش ارتش آمریکا به یک شناور تجاری در نزدیکی جاسک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/105953" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSgICVKToHSbQrAYSPoTxBEMxh3Q5PgskxJ4LTkwdSeN3brdONqnDCH8GAcct9e0yvEuBNke355nBaynIeDKgC2OvQawg0lMowYJJ-TUZty7NN5JAEA5BogSwIH5_HHozYWYLGD13bRRbj2k9DG1DDi-_FThEDrVJktqbDBi28HB4qWTt9Xlag-1gN2aHHKp319yP-IfR9dGlLQf7yuEVw3fqNwKqYbZhQi5opAEz1Wh9KeYiYgyGrrVRxxw_U0HbS-kDEPSe0fGejabrO3fOXdEZS4lfBIKrUWn3p28VGJNoqDCIksHmLNAgXNos5nJNFaKyWe5f5jjbgdhgpe4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موشک‌های سپاه به سوی بحرین و کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105952" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJKvxpz7Gta6Lydcv8_P4Mqx0rUTPhHl928IVT3shmjlIK1Alcc5EaRQglmEG_x6jQJmhK4-hgsB7PZZSPu5FZQq2ZjUjHPEMFNbgpLVmn_yzA4n4lHWhnjfK4zAcdBc-92zJfXGLgHiLTGPJLdme7QH-kf_VGvSBTwDu5JKEY1XnI_DzvNhn1cB6ngVfi6gGBXbSK9ZR6RN7FXzIvFAHonxtT3I2vkAFhOpMe-WupeOQ_yf9UMRp_mXx1D6dyjfJODA2YvGLasz966RLM1INqQNLrC9M0VPKCj1t82cXhwFxOX28k_2S0embQeYu7SedubzQTR8c857FibBQfqomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/105951" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/105950" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amj6KzUESjW-Ii-N2ckcnlciIH_l4NHwQJRtWQ6LJr4RKNr_kSPnVwrVrAo4cwJb9IBzWXJopM2zfxNTKDb0uABgB1iZOrIefKcq0EArZSyo2uSbIgJJA5h9p0Ro7rrhxWyYRaw02lsP5nUj3_yvMTFNwXpJPvMbSTuAYnQE8b4bEkeg-1o7IWfZQjz4sGZWfZAA1maHnSodyatm2R0oeXqQ7z-39fnwdRN1sXMjhK1Hxz6DM4cDJ9q1AU7huVUJ_kL72fzqMwt_nhaOrwKs9C2w-tudwrSCVTBXGT5YNCxXp699y6Kxo92aYN0K24K3d1cyfofRNI2EGpB9RVUoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105949" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHdV1V8UjDe1awGITmdFI61hXpA818oWj3_6iDv3aHgfOe6uX6y5wqyXX1mTn4w2CzjSfxW7U9uCJTl2hHIAbSO2EajpHqwZVrukWqTAut3JufW04JQeAS-w3PVr02cPMD20DE2hxc-fBa6Q5eGZsBGWZEeBoxWVzr1-BAlsVnGj37FsILRgXbyYW4LJ6OJlW6LHvBFEllvJsNliSyTXm9ic6sBB9I2tWI-LbMLznlCSBGngBHccQgvmCbU9Hi_sXOfcBoEiQOwlgcaF8UZkoWWJetLzlmckmsE4zm-puNwDxR4cwVJDrSlSMj6aqTN7hNSu5mQ_SkJRylXDA6DJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇺
📊
ارلینگ‌هالند در لیگ‌قهرمانان اروپا:
‏59 بازی
؛
‏59 گل.
👀
🐐
اسطوره، لیونل مسی، برای رسیدن به 60 گل در لیگ قهرمانان اروپا به 80 مسابقه نیاز داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105948" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/105947" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0ZcOB-WTKiD8LIEN7g9E41zavRO12ui_oYSFGKEgKx4D-ah826tROs8LyzG2dP-mqXgzAaIBdn49t2W8NbsQabSU3vsLZ6xdIT8gecuJkUhWVSbs4TdYFQJfgsvJFVJGyna848Y3lE-n62CU9o8Hlwqgo_WRpgsdQl2AWxRlyPg4PDrV9pjERMVRggf7hHkPAjQ9XyQagYCO3g2cOcHhmF1zsjPIEWv6LRjGMAy0gKiyt09uWtus2Ud3rmAPpyDf3CoIPzBxtHB1dpdM5UIRkfjrz9fyMnWPUhopQu-Nc0heKyJlvrfOGmCSKj5LUmmeZkXA-rkLMBWYAFdRNs1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇪🇸
والورده بهترین بازیکن دیدار اینتر و رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/105946" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP2M7BmxpGYQSHPJn9OmkK-v6c2t9Eh8eVdPvcNOBsvQM8NDdYwWqCTswHjzP2DUhTyIcDH-61vmSfadWvm7uljLqQPfXI3UmrDXXufolNfWc9KYHyjWZsT8VEMjhHRM_Q85GSFCB7xNjnAieBKALebpsnuNtnOud0BQoUifG_ZFooTl5EGarsWSGXmesv22uLMfuFpDh1ij_jXTydbCxywtmC81TDTWsG5U8ttvmX-YwHfHQDK6Xq0M10wwl3vG6-GKhN1GZm9hc1Nyhfr2Dq2MK_oZAPYSbGpDHvyegr10ihRov3hQk0J5pIqVcvvKFA6JcM3JMKjXWlBrg3ka0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
نتایج بازی‌های شب‌اول لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/105945" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=crIEnAhkJ_Waw7qBupDNb46MtbvV1Og7Is8eGLv2FCOhyZ_Bt8VOun1EGEfXnbIv1Fyq5Pa78-h69JAoYeaTO9-VVWq7nY_fjKE-DXAJY9OvbziRvAnPLV5aV1qoPC0nviU4m6m2BxpmZsl_FcCjUGUeUG8Kyr8jPTAqZyG-KisH2G0LLZXelaDF_Vp0bxCMrrVdcnPP7s_cr7ux6hIwBQNqBcTHJDMlr7jDN8C_xRiOpJuF9KqMiKAF6yErV8dquyVXGdVaizFysew_eUR85i9xKBKcWPcJ9ik0VQPjZARQ1vFhS6G8QPGwjVvKHPDXvk6nI6xLyreI6CeAXyictg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=crIEnAhkJ_Waw7qBupDNb46MtbvV1Og7Is8eGLv2FCOhyZ_Bt8VOun1EGEfXnbIv1Fyq5Pa78-h69JAoYeaTO9-VVWq7nY_fjKE-DXAJY9OvbziRvAnPLV5aV1qoPC0nviU4m6m2BxpmZsl_FcCjUGUeUG8Kyr8jPTAqZyG-KisH2G0LLZXelaDF_Vp0bxCMrrVdcnPP7s_cr7ux6hIwBQNqBcTHJDMlr7jDN8C_xRiOpJuF9KqMiKAF6yErV8dquyVXGdVaizFysew_eUR85i9xKBKcWPcJ9ik0VQPjZARQ1vFhS6G8QPGwjVvKHPDXvk6nI6xLyreI6CeAXyictg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/105944" target="_blank">📅 00:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ_LIkmLwoDt3D6Gmyu45NI5wMEJLJ4r1VRaY7gqoRxE9QIROOnDrZuAamOkcuhDIuPeAqH_ur7iWeHdJ84AYBg07WRCfHu4h4-enxFYPtRy_Jjn3l0Va2rj7Vd28EoDVBZED7E95U1lYcCdmylgN3IjuPwCVa-uwllDdopO_o7_q5_FIq1cGn25wk5nJ7jTnluQpPeCI1HkvX2TgNLpohpr9DTSUUDnt2pwucnNKbvAWHl-hcvl9ThnkcznHZ8ArgUbsTd5f3_Cg3_-L3mE5nUv3L8w0ZwlLEQ5IAtLOzCKW1Dn-nTc7ky0qoxg0OGtBAk_P_j13CrOsBdf-iA4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
هفته‌اول UCL؛ برتری سخت و نفس‌گیر کهکشانی‌ها در خانه؛ درخشش دروازه‌بانان و فرصت‌سوزی مهاجمان باعث رد و بدل شدن گل‌های کمتر شد!
🇮🇹
اینتر
😃
-
😀
رئال‌مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/105943" target="_blank">📅 00:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=n4M1I-5l1NlOHxPMKBzcI5w9ZFbviv6to3DyA2dkK9OXRRcBakIr1u5I_ur5ouv3g5dY37wf8mmVvdcf6Z2nd4ge8R5QW-sLIveRSpnXwRYsKl7zzAO1HId0KFGvdffmGwkWh0nz-F5COdPZfnXfp7jlX_gYiI6-_XUORGAeJv8aNAqq1d-apPOvIWL3UXxLe8PPtZW65t5RedX7OC7SGgNVjsdzCbmmvi6PgQS2JKFebOx2dU5aSEfnlm7kjHyCcUAj5Th0PVebBkMUoIRuFGwLC_6sK3K1NSMAJlV2-OnRE44ocr35TO5uRkw0xKhQFXSamYCJdNA15aW4Y7GG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=n4M1I-5l1NlOHxPMKBzcI5w9ZFbviv6to3DyA2dkK9OXRRcBakIr1u5I_ur5ouv3g5dY37wf8mmVvdcf6Z2nd4ge8R5QW-sLIveRSpnXwRYsKl7zzAO1HId0KFGvdffmGwkWh0nz-F5COdPZfnXfp7jlX_gYiI6-_XUORGAeJv8aNAqq1d-apPOvIWL3UXxLe8PPtZW65t5RedX7OC7SGgNVjsdzCbmmvi6PgQS2JKFebOx2dU5aSEfnlm7kjHyCcUAj5Th0PVebBkMUoIRuFGwLC_6sK3K1NSMAJlV2-OnRE44ocr35TO5uRkw0xKhQFXSamYCJdNA15aW4Y7GG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل اول اینتر به رئال مادرید توسط آگوستو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105942" target="_blank">📅 00:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئال کیری بازی در بیاره مساویو میخوره</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105941" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105940" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105939" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینتر یکی زددددددددددددددد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105938" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگلگلگلللگگلاگا</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105937" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
سپاه پاسداران: تا لحظاتی دیگر تمامی بنادر بحرین و کویت هدف حملات قرار می‌گیرد. منتظر باشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105936" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئال بازم نزدددددددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105935" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105934" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلر اینتر با اینکه کیری بازی در آورد ولی حداقل ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105933" target="_blank">📅 23:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امباپه بازم نزدددددد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105932" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کورتوا نبود الان بازی چهارتا گل بیشتر داشت</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105931" target="_blank">📅 23:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFqrrwg2VYZPO1ZYzCJEJFBGDJ5xsNZHv08pNwCGevgvadZEn1-MzAkjZ9lokroHwIiZ674GMtK1JlrBTlIGpha64I2rr2IMrek57lYgTLkb59JdvIhvdTvflj2hKn6gdHip73uTwjM9m8rvlXaF79-0qgmwg0Pd9P1jdOdPlr2S5z4wkyluf_qmjG1urBpc_AnLzTic3sKOhfQ7TVPuQHaOjmMMRDaJj2yF6YvX41konYX3M9zKScLIDzhRW7iASrENtcDmtR_QX1qw0fpQ3sVcz1Q-DNop5cbchlTykBLOKb0_jPatIeJCSBL2gPcVWoghoK14VThUtvcnsk5EBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105930" target="_blank">📅 23:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105929" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چه دروازه خالی نزدددددد
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105928" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105927" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105926" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGYlS9vtvWxziz-ffFLUCra9pYCNlYiiuYhaeROg7sFiiwWhI_CWVd8o0Xp5YG2ze0l3BvMYZHCp0gNtUHIcrD3gSDUErz6GCO2PctPnT-FylIEwwyXGDKq5vXWzdQGn8GMjkNOUO1m7wRXMIVSmNzyuLDtoQQfxKXimZrnPwKHt5z676eqjLWsJlipn0MaZKU2M-DYxxekkiA6wBuamJi73WM35eV6VL9APr1bk4RQJsu64OeDZytjSZF0iDPOetL5tJSIcTeMz1PiLHRx20zNongkDFjTXMVF2VPDUyb-vZELA_cq6LzKCrERAEKpDZlnKSU-z943j4jjcWv4teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
وضعیت نتایج تا دقیقه ۵۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105925" target="_blank">📅 23:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کورتوا خداااااسسسستتتتتت</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105924" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=nB_14Pc2JilUzlLSXJrqdBDmkrskU0DEC5FjExjRt-IINbTabNVZplRqqghokq_Zj_Hcs9jiVyEodOoLG6i3pG7II6u8fHpoA6QYec5MkEVM5naMT6T7bzohxcPLICKe9eVvVvkpMG_CE-e8gFYxYND53WzPaSsQs9XnwvrYAijYp1iFrsi3ydsMPCZ1O4iEpOfgUQhgomwT2iu9WSJIH81hgA8QDO85_Bkxg6p4fpM-UX0yr-Wg4qLhDPgTwStqZSAe5eDYNjdICkgj86dIbtTwPwkbaGI6h9YoYqxJI9RSw67fNq1cP_s96JT2oeBwt6b11C8rd4RHdBs6ObtMsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=nB_14Pc2JilUzlLSXJrqdBDmkrskU0DEC5FjExjRt-IINbTabNVZplRqqghokq_Zj_Hcs9jiVyEodOoLG6i3pG7II6u8fHpoA6QYec5MkEVM5naMT6T7bzohxcPLICKe9eVvVvkpMG_CE-e8gFYxYND53WzPaSsQs9XnwvrYAijYp1iFrsi3ydsMPCZ1O4iEpOfgUQhgomwT2iu9WSJIH81hgA8QDO85_Bkxg6p4fpM-UX0yr-Wg4qLhDPgTwStqZSAe5eDYNjdICkgj86dIbtTwPwkbaGI6h9YoYqxJI9RSw67fNq1cP_s96JT2oeBwt6b11C8rd4RHdBs6ObtMsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105923" target="_blank">📅 23:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امباپه چه تک به تکی ریددددددددد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105922" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105921" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگلگگلگل برای سیتی توسط هالنددددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105920" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز: امشب برای سربازان امریکا دعا کنید  نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز  ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105919" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105918" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYQIWHPYGRxMQOsOpgveNE_tGmjKzi9w1Kr5dX-i4atmJJBFNbCvbF_dPPtynaWYVUczoLMRJ_motvgcVK9ZVyZwg629qM2FWlZTM_oIJWXHsI46IEsfIBKmDcXd0lehvoFxRgytoYtW0i6PNmLt1c9im6YgrUxyKWV43CPQpozK2SLxJHrNLMVSwTOzjYs8c_Ohd7JXoet9VElsvFkIExJQUX4lojNIZJvIckt-t0zuJS0Zimr4hoYmjuimYJy0tiuaSDsIUNfOE-vX-DTePWGEDywe1PchXRe6v5DUHbWzm-U6pW0UnEs0b9N3r9cBovEMjkN7wdUlz9vRRMpmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت آخری که رئال‌مادرید گل نزد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105917" target="_blank">📅 23:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105916" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105915" target="_blank">📅 23:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105914" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105913" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KyBhxnNfNFZNOHaAShWpms__adZbQKDEFLWSy6Kd5Q1b1AexAipA43EWTXLFVOG08DCdiX2E6k7hGBiKD_6BPvQDKtxs7NA0_DVcadzuvud6w9B_9DNA9eW7NNSTiswCQFHXBW0vhrbmjkAmc6MUflgPss_KE4TxWDa7iJg2yLBkkgtFEAJM45mftFhKFFzsZAlqggYWkuPT4J5_o0FDkmtBbeMR1ZixI6YRW3kcOp4KllHclAZaGNZEQhV6SWEblIA21uWUTVzrucoHmu6hz66jXAHoas8DX__phpUJthbZLXqlIAaZt7JySPDK32DRIH7VDvThSj51srAIJJ_8gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KyBhxnNfNFZNOHaAShWpms__adZbQKDEFLWSy6Kd5Q1b1AexAipA43EWTXLFVOG08DCdiX2E6k7hGBiKD_6BPvQDKtxs7NA0_DVcadzuvud6w9B_9DNA9eW7NNSTiswCQFHXBW0vhrbmjkAmc6MUflgPss_KE4TxWDa7iJg2yLBkkgtFEAJM45mftFhKFFzsZAlqggYWkuPT4J5_o0FDkmtBbeMR1ZixI6YRW3kcOp4KllHclAZaGNZEQhV6SWEblIA21uWUTVzrucoHmu6hz66jXAHoas8DX__phpUJthbZLXqlIAaZt7JySPDK32DRIH7VDvThSj51srAIJJ_8gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
اشتباه فوق‌العاده کیری گلر اینتر در صحنه گل دوم رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105912" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انتقام بارسا رو قراره مورینیو از اینتر بگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105911" target="_blank">📅 22:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اشتباه فوق‌العاده کیری گلر اینتر
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105910" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئال‌مادرید دومییییییییییی</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105909" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105908" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=iQXlb7i0qrBWlM8YtIWhPftyIDOb7JKDN_Xf8MxiPci-YAU0wLh9MDs5s9sQpoerAP_UZxPDYBOmNX_VpDeFvbMFrDLcrinVs6v97r29nMZX36ZeCPi8-z_CN0rmj46y-PcxT4AS9aVTCUMfMnsCAa_Jr84K3qxkk1jbbb1tgNmdj-eAL9yc_PqGR__oBWWIfR4pmdQ9OlEtn7m2ymWfz_saK8AujbYab6yFFv4124GObVCVyX0SUZqYXiIV_yl1gcrkJ_27ByZ7doanu6IAs5D1S1_0948NWyIbAxfAFm3mU0vQQ1x2vChDGX0ZbNgaws7g2_7V8U89UMxOv7YaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=iQXlb7i0qrBWlM8YtIWhPftyIDOb7JKDN_Xf8MxiPci-YAU0wLh9MDs5s9sQpoerAP_UZxPDYBOmNX_VpDeFvbMFrDLcrinVs6v97r29nMZX36ZeCPi8-z_CN0rmj46y-PcxT4AS9aVTCUMfMnsCAa_Jr84K3qxkk1jbbb1tgNmdj-eAL9yc_PqGR__oBWWIfR4pmdQ9OlEtn7m2ymWfz_saK8AujbYab6yFFv4124GObVCVyX0SUZqYXiIV_yl1gcrkJ_27ByZ7doanu6IAs5D1S1_0948NWyIbAxfAFm3mU0vQQ1x2vChDGX0ZbNgaws7g2_7V8U89UMxOv7YaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول رئال‌مادرید به اینتر توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105907" target="_blank">📅 22:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امباپههههههه زدددددددد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105906" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105905" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDxOqGMGOHzoA97bO-rVCRJr5yH6YLlLyv8K4NTXhzGzir09uLNgKO7g0V4szHyAgMm-Ha2Uty4H03vTt5-mba6KbqYRX8MwgRIh40p76wh8GnRB4IhAv9FS5Px36i_bnZSCPbbp9flnGHFO6iiM_H4uxDwFHTTDD9pWq71YpV7DTY5FPqDjrxXZwu7pR6t2phw8XHV56vGVQnQaHB8A9qYVH3BGmgd-quIDto8hlqJwVWd9GSsJZn1vG2kgK_C325gqtg_ezIAQkCpSzcidYZVMpL7cysh5RQ8CDFkKXlHr0woRMwfzWjQ2RtGKghRMlrYBsycT8QakKy7yWyQ6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتیجه اخلاقی از فوتبال ایران:
فحاشی ناموسی در رکیک ترین حالت ممکن ۴ ماه محرومیت داره.
جمله "شاشیدم تو این فوتبالتون" ۶ جلسه محرومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105904" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال رئالیا از اتوبوس تیمشون
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105903" target="_blank">📅 21:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnjqBg4eFNCkDcGUsDrkTX7YF20XzYKm0v3JR8Lp15hctfIV6TfFFq8wyb4XApGxwXlEhYi8rwPgO2voBCZ5iKXJYIKrzhi5JBh6pNwkuWSa_9it85Th6zo2q1qazOTE22t3Ktv6Fnf6GIJowf7Wg5aQcXM3XYzhOAC_zmXmuGgiqvUN7V-jAmvcYrxgDT16ntD6JhSppPP0nLHxY8z5fgr8HRMUMFKmlOVPsgTT34isI4JHjbBnSOZX9cXD5JO9kijsuCmje0iOoA8f0HNSK8PXb9kr2g4zLZ-18J9X1EsaiuHtrj8qJXS_-B00O4h5FCYPCCsPSsdEoJg7gHgUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🇪🇺
اگر کیلیان امباپه در بازی مقابل اینتر گلزنی کند، به عنوان پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا، هم‌تراز با رائول گونزالس، با [71] گل شناخته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105902" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105901" target="_blank">📅 21:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: خلیفه و گودرزی از نیم فصل بازیکن استقلال هستند. بحث انتقال خلیفه و گودرزی از آلومینیوم با مدیریت باشگاه آلومینیوم توافق شده است. این دو بازیکن از نیم فصل بازیکن استقلال هستند و حتی واریزی هم انجام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105900" target="_blank">📅 21:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwfoDyVNySRetp3Pm-OQ4xxrvmpHntW8o8zuRdW3UgySDiIZuhsC-2AGro6sGqYWrdlnq1aMEv3kgrrBlR8-gs3o3FkALuAR0fA269MtqCWt7MnNfPSnNCTGsay_S80OSmN4QRCfh6YKDUmO_x1xeWPKycWrPR9G9ZNMbG_LUJ2HcC4hbkXVzo5cxeVhWWtawYLefc3kavNLVvWLQRfBJxQ9CocqJzA5W1E_OybMOQ3Tqh95MQ1x1O91ditthiO6sh3iYFp_2tmYDCz1pGtkT2EmAvooC8lgSkLnPbS9UVgrIq5z6d-ruSQYQSq8_1Q-KlkPrshLh2RstJgDWBJr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇵🇹
ترکیب منچسترسیتی و پورتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105899" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hYn6ZK9mcKd2BVFwW2HhI7_ATCskDa_Mmi5WqK87BQiRVzJG5KiOZd_ePB5lG_df93HHKQAD2mjX7qtd-VwAjtVIJ2B7G8OKZj537HHxe3OQDMOH4mjv2EIjrrWgXNtVSfStwErTc5dK2I-XbDkYxDQGKiK_3VJJzvuC7n6sL3SMQujyNIKDJUgbKnasmghrGcyrC3DktuQxjmsR2x_F8wUh1Wrg_ezW0BSSAKxNHJWDEYxouhRxcSYd0sbO5jJR6Ke5jYvbGxDGtL7R0-2GLrx9f8JDD2GCC_ul91o4gBZxTb02wkPvUqbj62JGj9TMjQ6eCveMEaJm1NJV8F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105898" target="_blank">📅 21:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiYPz4_77N4FBzE3yF9ndxmOVfROv9dR2r9cUJrJHKej0lRnlE2VtiLiD0RLi0iyiyirVY96JIVKdmRjYzH6ZjXwzplcWcbs6aNrCcmkxpSH9qXtnJMAKvNIc-SoyjalEiVSh8LRxvVLHKMXLxKIGTU8CeaIDRMMlsfmR7gJppHh6QvYul1zQlUvkj7LsnWMx-2GuRpOqA5HSvShWT60N6cOTWEwukY47dtIIFPpM_OU7WUnvs8EVpPsWnMoqlxLtNMpVvjRM4eR8jswG_by7XDaMEIB0_-zUedr5cE8-f35X-DiKAynGqpzDaiU0wP-UBBS0qkF-Sz1lJ4BHYpLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105897" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0hZ5_wcRyasZlfeCAHveS0NOBfnYOdPtanlxiImVK1-3qOhrEsCVShdmaEBSThcNeTevHg4PRZnHkH9gu9Pz1UgmnqSCzx3J5uil_GnDh1CeE1dOwkcxf4lhRALSl0dYBl0JsBSyvW3WxfzzVrYFqNyps_qsCUwRS0rKpQ8CfAwmMhgai58dJ8-0fH3vky4aXur6FHJtVhDBVwrRkBMra7IJ3JVQzXCU9KTCpmxflx7_aZjb5g1C8EXhzKWRrRgmEtDQ2sF0muW20j8hRjLbeSS3bjdd9zD6awBss2DWnsTyMb2BjYniJ9Le_aEcJu6au7YvIIDi41fYeUTNpxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105896" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-KHLnyIxhRmDbvSWdbKkJcitLJSkN-cfT4sSniXNtU9Xsc7mH7dCrHJU8N4czBrTmFmNwHpnVKi_FHdHMxU2uxlbv9z04rix50kEeAWq_mVBWMFM-irnpneHhAmIKzOCJKmjFfPhwc37C0SxMiyaQre8KavHfqPOUzdNXrxM5h_tJCqTq2x-P_PRdHnG7aAiEsP_eoCjs53NsB5fFuucjsJbN2piaZlZOfAqTG9Zi-ij3hluBTo26YVD_PmaeuJeXhWgpoxusV4eqaTE1fl-ScV1PYkTaqnbCHQTXRmNJ9R9M4mxMcnrtOIbfXWnwG7UBqmGHSWQfdQUMxr584rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
رئال سقف برنابئو رو برای خیس کردن اینتر بسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105895" target="_blank">📅 21:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBxD-sJOne6wJJF3odaGyXxL6YDsyst8rG_YHcR73ZY3FuTliiiE4dRk3M9dnbqfJdzAT9n-NhcoJatFakoGMvCf0gKNceFeTXxwh39WUwl_Tp9PNsCBPx0J_eDWoNmxexBUxUVRnbS7otK00usBW0stWYPiWH82lw9hMvjCpXoMelMd0WukyZxpVKafeDr-1InL465layeFh3UYtbdQK09qEvHsWHMf5cZ3pv_LdmLgbeAg8OvcaNkIrNdAfekGvSnE-zaDMPwrI1dJzbr1JoH15J877TajE4yqBIiMKF3KQkVFVov9_n4HQP961cPQ1SBleyMY0G8BMJtzkU7pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇺
دیگو سیمئونه: خولیان آلوارز جایی در ترکیب فرداشب تیمم مقابل لیورپول نداره و باید از روی نیمکت بازی رو ببینه تا شرایط روحی و روانی درستی دست پیدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105894" target="_blank">📅 21:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d57gWs3hVp4Tufsa8rcO9TbwLFEiJ28SMjNJeLH10a3MKde5Dv5pvStJvgFZXR-wQcpaHqDIXceArVhlpVK8fLlL351cdTebwVrQUNsEyfE7z6F_HO55mvvtoco9l4jeUmMB5M7mfsGMVpZiWmwEUcZCACh0HMwn0JX2llK3ti-4mGHW4vYy3F-iTqf5Wu131cHP1vdkzP_RrjXwMSahUnZeOWPXWPSmdtQRBuKZ-UUAR3lXx12SMYt8bA8zA_Ubh06mYAIXU_P_nrSMZ3dGURBlejMkcSgiM83TkvA_n9_xvDkZcifWg-I3Tmi-zD-YgilDU1WCoLw7Xl-uxKJt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار سال ۲۰۲۶ با باشگاه و تیم ملی:
🇧🇷
رافینیا:
بازی: ۴۰
گل: ۲۱
پاس گل: ۸
❌
نامزد توپ طلا نشد
❗️
سادیو مانه:
بازی: ۵۵
گل: ۲۴
پاس گل: ۱۳
✅
نامزد توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105893" target="_blank">📅 21:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل تماشایی آاک‌یونان به لاسک اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105892" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇺
اولین گل‌فصل لیگ‌قهرمانان اروپا؛ گل اول تیم استون‌ویلا مقابل کلوب‌بروژ بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105891" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqPGviY1xikDEVtjIbQzIAFNpwTIL4GfolwXH2qUl2nrAVxVNzRHfQPFBFJsylgQOGgxN8B1yiFgIrwN4wc4aiP0bhPxTe98vTnUPcbBmjv1-z6BQUzculQDjp--J4V-YSvQ2LJr8GE8tJMc1AyAnuiu40EyTXiIp7FqVKKSXoHEtEcKicRQQeDYoeGJWfZE4xyHvGoEdXJOjD4N-f4VSDZ6b95d29zk1N0N-005WztjU508mllPIdgAb1jd2Y-gICtf2zWb5J0NJ44_C0SQCBzvJtLalupEDCjTBK2KrOGTL7lO-aIOoCashqirUGOPmjokYKAWFZCPXyfMJASHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
غایبان پرشمار رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105890" target="_blank">📅 20:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC8PdzKnMskI7OARpVf1q87zKBz_9Vit40w8HDxmNj0zHxynjxzPYtzLwHjHe9xN6_4-oNFzOR8trNMNDINbO8D3u2aHK4HMlV7ZdSorlJUIlAWonpBb5Rpvi5d7Y4zP5ESlS9DaulK_2EPoINkXpxjjiLBMu0EbXNpkraZ7Peyj8pF9Uvux25glH7ZHTLkAFzfp_Oc6HkaGJmnB1rDsg16RT0wIht6MaV_HyV-6Ps2XoHsYfE8pIi5aCMoKUPIEPCvNu4EKDcCUMgYOaRi2UZD9RxMllPglaarmsnZY55dIyhw6kjb8pIqTwW-tzDEBSVKhfjmy_hUDUpvyAj853A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
محمد مهدی زارع مدافع پرسپولیس بدلیل مصدومیت پس از تمرین ریکاوری سرخپوشان در حمام دچار بریدگی پا شده و ۸ بخیه خورده است تا شرایط حضورش در بازی آینده پرسپولیس نامعلوم باشد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105889" target="_blank">📅 19:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7IgZpxy-zKpklGaDS0hziMfRMpDE792ARifx2_4pNt1uJDjQJ9QTVH5cWVhuG5borWhDy2SFcOz7pZTkcZ_tCiZ_eny0jvLlOHfuYpfC3XTH6--RQk6t7Rw6x5dxyd48g1Sv_wvXIjpoOnFlOLv7Z5WMEecfswb4_B2BtOPNSLS12D_gTBCTtC1m0zkSuUvZ5wYmVC_MAF0Nc5JbYx2Dp-EsvG7kbop15b96zdVJzQdDqLwwc7ou4-ZGY_8rl4ogZGfkPGfsZlzX_nbiekCch-pg3lWeSnSZm5noka9hyDKc3_X-F3Bb2LqlypU3t0W-qv24HVNK0IxCohWq97Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
برنامه‌مسابقات‌هفته‌اول لیگ‌قهرمانان اروپا؛ از امشب تا پنجشنبه بازیا برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105888" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره امیرحسین صادقی از شکست استقلال در دربی با گل امید عالیشاه و درگیری شدیدش در رختکن با یک فرد رده بالای فوتبال که منجر به جدا شدنش از آبی‌های تهران شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105887" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشتِ یک قاتل خونسرد به لالیگا برای بردن کفش طلا.
☠️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105886" target="_blank">📅 18:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyGOy8MNHj6d0MEJJXQczok1vBHZTuaiGkb6kl8igBlyuL87aRSaDm-4-Nz3njJ-rho6twj84rKwGGtvzmkY2m0m0JjwCj6QrCDY7FUcEKfvQ1RKfTvgO3DsGdOqGg7JcZeVpt1HQpofg1Q_gexK9tSWVevWbIf_-_-erXbGK0QrYfsmI0KgaX5w4OlWfBkwv7QF5LxOa6r_6_7XgRPiNfoyylvSsGMzjDGkmJJS66-N9C4PSxo_q65clK_xkZwhOX5eLDvt9YV7OladSp357IMkocYJYz21M2hRGtg5oSzjfjLYZWG7RkcUC2Q5cN5ExVGPD85oRYg2Lm_YVbDysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
فهرست نامزدهای توپ‌طلا مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105885" target="_blank">📅 18:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمدخلیفه: دبل‌سیو مقابل یاسر‌آسانی با اختلاف بهترین سیو کریر فوتبالی‌ام بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105884" target="_blank">📅 18:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwKN9smNh7vgP_kjKhgC4SevlvkkZiSLNsuY1J_U1nPWXilnLUh8Uess9yS5VarDdCWmIfMuYX-zBdC_VgJC1rrNx-IkEO_aGKVhhrcvfEmhZassWUAgOCBqM2jspj2G7MuwlQatC6cdH3wnGicJDfRKsyXjVZh646Td5Fl-5MAM39Ybj3fpXIy87mVKgON7Z84T0DLUH8SZTvRwc5dMeiMfB2n_pTw3K7mFPiky0tOF5YnKWLICk1XxXtoFfahUxZ-pkVneyqm4lPz0KcOzuK_JUalyMQ-Ls5svw9N2KG1BmyftYGhhIvWgiUdZ57bs5OSroSzVY6clgChtiSnyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
پادشاه مسی نامزد کسب توپ طلا ۲۰۲۶ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105883" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105882" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT9-vF0dzd4hR92gkKy_2F7E5x63NNcScOl-bTUvWXDgvAUFmIz7htGplMh_nKpFtfVXI1PxmN_aTHlVdUHlezfH_fCf-PMHibysb2lUp_5_xGicFH9mr5UZgZZJIDq607zM9aUHJHE1_DXobRePnzGc_gaVw0ed5qdEKEvXDe2CoapA7asOB__i6VzQYien1kGPBqtZVKMsO0LOBnkFQhPGMUw-CimzVGNrAwS_RxlEO81XYIOKMOgVT75cbOpc08jP9Pzr5N1Am16KPfnqVla4DZ8askTrwgO6ts3pT9LyD-6Uf-_AGC-Klr--fkoBCHja1xoCpC8fvxY59wu_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105881" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG4xPk8nYlVUOldWIh2AX1x83uFc4QVOAZuYwCncDzCTkDyxbhGsMT9J-49t4GWQmn6nNxflKSm-jdT5IuF7lTVjB8o3X1_XIQYYGJwdFjsJUqEFMqdpjia0nDmMNQfVjVGKM5ZjnPm58akBIX7FO21iK1Cemmivmq6IiNKvXGyMBv6_XWeyBPP6PJ0EtqSgFxhddLDVqb8DEke_V6mXm1QpTrZUL10JSmQSiNngZp3IkfO6qDivACACSwEiuCcFUfxgguXr9OO-AN6FHoI10UqExtnKadFlzGo5Kl5Ijq2QhSHmp52NdlCHiPStcYPWkj4E9bVSZ5_ySP-ZfvfDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
ترکیب‌احتمالی امشب‌اینتر مقابل رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105880" target="_blank">📅 17:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqmicQoVY0T6peVmCCFjRe_h7I-e9Zab4WDjQ2aZwd3T8Qvof8ytLjtpDRpaG9j8D8R_fAaiC0sfDVnGBP7Nc_AL2xzWnHxs3TCY6oEJ_FBpHO3cDWqEvcY_kiT7f2Ia7Z_IWXdoA7FP-aS5m49TBbMxa6KjIXEULxmy8hdYOlUb2dAqCIgszNOr3UI3H3RWv9BEfunCVngC6GEzhBS2-DI82o3SNzBMC0nmVhkdN5ff4OyC4CANO75eQJc5C2R967E5d6LgM-vZZDeAeQ0Vjcw1kHTIappWXQVE-ir6yB1vaREIahKmnJo3-UTMmtmRh4knDE8MR_OutECb3es6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
نامزدهای توپ‌طلا ۲۰۲۶ زنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105879" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNMoZMJ1yvPvdN8hDOncoDrnqkBvKJ1UeTCXBRKrTSapt7vbLu-Rf1XMxYb6zSQDucKfG8MaDnmvwbgB4blER5kDPDEgB-SbZI3dmcLyPNR0S8wpVKPtmqTcLg2MekWOMM1yqSnkAYmkfaH8W88IvgJwdNyNbZRgalIaG0OTuR1-RUYxA4akKegPGiiQtScH0hRiJ24DG2Rj0JtDEc1Xakx7wyMLOm-phYZetff9x0mhwbUPxiiUUv39oJnUYoLPttJe1AdHiPd-zV6MtXgVt7aaQNkfAvR63fE2gJgMmV3i05SWj5iMpO3ywE_dn75f9DUXtKkWV3GUL5EaQeIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
پیراهن اصلی تیم‌های حاضر در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105878" target="_blank">📅 16:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پیش‌بینی یک سال پیش خانعلی: تنگه هرمز و باب المندب را ببندیم نفت ۴۰۰ دلار می‌شود
پ‌ن: قیمت فعلی نفت ۹۷ دلاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105877" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEoGK3PJBa08ScyTsLQu3EHWtQk5vIZqcpbSXjckvYAg9LdjtxrS7m0tWYcd83KUOqHy8RylpNduRpNLe-U4xlhZuRrWinLlPISp0O0Uo-hUADxK3oFxyqDPlpG-uMtFCWtbZ8yfsQsY5bK3xeheB5iyhqc73aJmyMnj7dSyc22oVpJ6JSV6UK_X54X-RzT8he4XaUEApSiC3sb1-Ia5o6_Jw4di7GxYJjeAjRPyCKCoRfk4mIHXsh6JlU9SQItkJbdf2u1rBRyk83Rolrnxe46lqeYpt9DM_XrNdKBlELZh4pQGWTxZodriFvSQbopgRmIG-SB3UehIcrH4lzacGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbiu_fzaRTNDVNonC2uPOQoCNa1OiIPsAMWbjG1R1kCPElyYNOptbMCkT4bvB8Ec2bDGc4tqoKSUNUFBD0OSz4BYjmSxlmUbtWPPovqtUo94QwpNpAWHWN56UXFtxjDlSWdb3sFBMRknG2Ginq7g_6FPey7q60DmrYAIXs3iLjSlAgFbVsLv_fNO3UCzqrg9VF-fdKmx7P75MoQGQTMDhEuGAWRZTdlSWswUx2mzPkRzNSWkOsWMJgC9aNmlRDWOOnkYjSQ-qPNe_vy7d9V3t3HONdPqUtX3gqd7FxSo2PyEPrsvA_IHHXwE6rFK3rHC5VDdgs7yf6MeAQvm0gWtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
نامزدهای جایزه بهترین بازیکن جوان سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105875" target="_blank">📅 16:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابوطالب یک‌سال پیش خیلی قشنگ کفت؛ تا سال‌ها مغزمون راحت بود اگه علی دایی اون پاس رو نمی‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105874" target="_blank">📅 16:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
❌
🎙
مجری شبکه‌دو خطاب به خداداد عزیزی: فحش دادن شجاعت نیست؛ و خطرناک‌تر از خودِ توهین، زمانیه که به اون افتخار کنیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105873" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
یادی‌کنیم از روزی که کل‌ایران به هیبت و بزرگی اسطوره علی‌دایی در جام‌جهانی افتخار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105872" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ8-3wD_xHaaosK1tNIdzUGea9iRnN3qEiPQGI3gkQ5ujXhIbLNrRzeG7Irj-kHTs2GOv85vS69Dks6hT2Nu6k6ikRyEFGQAILyR3NWfIHTMhht2NvBfCJZWxdIVw6GhNk4RpuuffLvKtO_8oixcU_gexcKp3GKlYjsppVJ-OGMhdcl2PlUYCvnpwbRNdhKEkUrHFIS-pKS76LwdzTdHXNUo7LXcHlWzhlUzXtNrr4pgiqvon9_55o4IMzxN3BfMur3vcFAUAvt4yld0f9dgSIN8eSX7GzSFczA7eXaqQPTDmQYbmm-lCV8w0w7bBQpBgxfWT66WKZLJhuKaNKUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
🇮🇹
نتایج ۱۱ تقابل اخیر میلان و یووه در سری‌آ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105871" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUwfIwJeLpVK54YvwFA8HKwvWgBWay7ClP80c9F306Gk3DrODfR3RO7Q1pw5wBra7GwUQJfYjAxoSKHmql5Z1ls3ydh7zwb6pPchkhEqzIpE1nFNmMdboScJC9ZGjFcA-KRLGzCz2goQ0U1bbPpv__zEOnRbgaujdnzm8aIGQr6g20h1M1M5d7tAFOLI4SE1wqdt54WPBvj2HH2Y92tJYJnI5hu53m9xp_BjX88Fwx4gkA2c-mCkqTCMj12tByqNKlix30EWKvBm77bHHaCgpPk0mUoELPXXS9Nbsv7goDZPKxukKlr5DfCywBZx_GeV5ZMwLyaN_0JJ9B9s6s0SBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست نامزهای بهترین سرمربی سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105870" target="_blank">📅 14:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCLVjcBxyrZYHkppyjneRCswgbCXfz_JOS5frY6QCn7Tg5ISViObgPSs4Jo2aWDJHvYhpikqaij0tHsZ6A1ZH7IM5J_SzJlL6_rUx9oST5UrMG44hhEgf_V8HjWdFo5NGyoEp1cz7F3uncq3hoVoHP2W68llwTi3MgvkdvLLI6mBNxG-WkQHXSU4JctIsI0FSuJlS31-ljbD0fPiziCMxLPlN50i_1clDTL9kre-XI6kyJMf4IBIsE0aGqmuJEQZ3OimYYPDmpb_ye3gFVGJXErXCCXv5GSYn8kiK1TWgKkRDfbvZIOrbAZfB2sM3r0HwCKa3jtELO8Ubg6WAE5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج سه‌سرمربی اخیر رئال‌مادرید مقابل بتیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105869" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc23hugvWBvhfBoR8xCxuqFbIuOKYmXbPW21I5iQKRtYEfWFHbKIvW0BRXH93WthbKvl2qu1_Hq1bA27XbUf-v8ClvNHoHWDEtnFeBstgczOCdt5G_7c49M9hfl-NoeYe9jJXND7qB_ALMT1CW4fPkpvzPalfMudI5ET3x9t01STgSHkLTXcvh_o1GNu2DbS6ojLi_kuTbBbyZrYvJHvwJc12azXAB5NObk1uBcpi9IF4WulJvK6EY2G9XZr1Eg93bBl2me0jV-tkCjwQXhy6E_x-WgdzWjdkBjwKSXsUoUGaBmZeLoQRISVZInepXGJCsv6MQQKICC8REkNnLoJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد خط هجوم بارسلونا در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105868" target="_blank">📅 14:02 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
