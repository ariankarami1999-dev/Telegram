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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-BnDUvRqosati5qeGkQYx2Gpy8JlXTRxG-7lv0eKKB8iLXAygK2tUaBioCDA3WagbpaAjPcyDaaHA7qPFu3elV75hyIHw_b81rIP1RZtiiDK-rBPHCxlfnxLPw14_Pl3bHmCBUy2EeLpeAQj12TcJvlTwkBwnyoOSpohY3XacpBurFWtEjT3more-gB7_3TCWHL8njOAtzeOBLarmNtCNd8t4feuakHsh18stH7kvvUaL16R2oqQrVtHAmXo7KTJ0YcIWXRghSDQ6xumRK-5MtFKGWBLAxYWifserP2xM_n1vFnWCD3r1HsKIgv__CUWCa6LCsL44YtGw1iB-TUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlYlHb8XzvaIxsL9w2Va7XnpRwbTrw4q6AsgE35qKQQu0dczO4guMhDa8h7DxsflH_va7TKlbKuLCCrgTSYG84dsie90KJTC6zHe-3nUD9LU7xHDOYjR5Uc2o5YSL1te9H7eGp5i_dxqaO9hNtIRFzFQf4KRlsEKgZLIne-b-RVKPgC2Dv-GBE1_ZDpOY7naE_sloQjf7T8AxVLYhTqBkvLSNJ1cbQoDS9YJD2p7ZyhEC8rF5PtYmmdO6VLmOyPbBhjIW2eBDqG0rv_a9d1xbvNbMQS9ZIBRHOPBArrPSLB4E4WbdzVKQRNbK2kLg-asGOWWL5OOjaZjnxyajBmLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR5gai1hTYJeZ_I4cj948nsmRGLoxiUgFfqEjt2m1sxSu2q4lHho9IOtCoQNRhM4fkKxNlKv0eG9JQM_x2C8pKwkAgIpgXza_EqDV2-hOJEWBhSlEVU__XE48as8mhw4JVvyhYI-ccoE46XUfSEI0Y0SiumI3T1gxZ-s3E1vf_El0GCqm5t2DYuC5CCvXRSHa6k1NhzfXRASaKkzai8PpNPpQVy1JUDwVxOYITIEjEiQB1xpPgDumaNzTHSClt-LUveZREltZOteViQD32S9mw_w7NdHizMjLqU9MsF9qLImErIJJ8pCzGJKFwg4Uox7hrACywWgsEQ64BNtgFKVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui8_R_KVkR8b7OyOC5Rq397-Xi6IrS46Kkr__9GpV8mmkNZ_JbfD9XMLAE27ma77O2JvlSz-4FHZv6FZ8UC9guB9YBFFYJOnYeC4Ap1TrMpNlpe5tckjm9sJfkgZh7vkSmqUElyuLlAhV_E7im0SC_CIKjByqd7P5KWK8KGRI8IJAw-7v2l2Nm84u_vL0qOTvQPX3PxtXpM8jehJy099hKLVItFiv29e4dtr7i1z2MJBYa4jBohdLauvpEuzw1wFKuVufsZcc41gnKTIaAbjBK1UMYmhXYCqfjlTgB-qoAYG1pGXhP0K7yKkYiQ93D2uhvyUmINUR21D__vZpDpGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwuYRNa6cnT9zFQIrLlPMUbGR9nuDDTM9lJ5WYB6glM8Zjuazz0LggCb9OLlUtlsqBD-yvXsrWk3ywlqxRQb0EnLWihjQcD3CjLyqI8IpaNxVPcx3JnnnBPug15LW_dEHTyK9u4oVrYF05eCA6d0vg4owAp45f5fLJy4PHeGJjD0wdL54wQm7tw5-K-HLc0yblApF6OG1quM7ykHGl9yx5MHd2Xyoc55ym77ViBK5wmm25-4gJALHWe-Trq_z7ro6BCbyaYFyq_sL67tFqhbYMa8Dz9MLKACYqKHrQHDwB8wUt2In56K_xBLZTD5CK7GLi2IpwX7gphAlW5ytLd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-p75RkpeshXIgRwnFibdqKjSKEaMpyqdr1sYoh1uf0KKj-4kKRl7Lvaa5vBKZYzAORxLSJFX_TT3uX6Dv9o6qbZCeMVJqi4uoVDSOfBW_09gjDOZBD9VowE-58bgh4oWfEhXf3WzbHn68dGtCievgOC8knJLsfvFuZXuUEC3lYI29yCLTZ5F5rX29BW1dzRu-AhYIm8CfHsefCyiiYRyjWm-3WOOIyoIcc3Wz7B6XqS01bQcgrGc8C9udjft1mGlsTTK-hPbAh91M9hJ8CH71cqZDGWvqMWEKoLiDS8BbJzLklKnG82fO4jqYePcX2nib6M4kGBsbJjewNMxPlw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXZVcM6POZolmrDd9b7HeQx3TZnG_s6iZfOjvDpyUdtIkMbje4hhnMRUy_VYCtq3ijWKAZlXX64pqXtom62X7wIfrliJONLPjz8tC-c5iMv9uqzHS-Drcm9m4-qUMAVKXys_UvAfPBfSk9DhAuQssT3Y0A3QSzV8jbjZqdOly_JELig1PEU47Q7_sfEb13vPUMEurxWqqUBEQgo1ced4BqIKPBOQ75Ro-4dm8vAudRQgFZGvjQIHt-bTAKd3v0hkdd-3jB0l6PRd3q9w-tnIDMs-RuLbTaJkfPnKzofwlTuCCL19XJ7jsLKYWbufafo3ErcZwRuJ0B8cmLEPSRgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eke00M23YA83nOZLmZT_azxkg5sl1IlOf1GGszyzysK_EHrIjhrBuajxt1e5jaSrb6Si4hctkMr7fB9iQNQFlGqNCzYCzexXivWxh7kDE_Z9iA3I9IwxCNDPQLCrP7mCpRnLBo6nLhxTDY1XXZ6tjSERauYf4ng95rL6mTQj8_GFN9o4PH7qnWbV_OE-GQ7TVUWmI-GdrjHfi_b7uSexMEfkm3Q5Ak-mguYqCgtBV1eB5G9Qb50FRyOFUcVMIQZFzRUGkYS0u3Dcm5SPChZHRl-dq8AA1AGdMuCZwmlbLcY23xAx7sHCXWIGkaJbNX6HIv01mjkca8gPV1j6vyvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBdYO6xkIu0S9-9hoGCl1iSbuk-8ELDB1f3eXTmk0b7HbsUzvjaYh7VMbnJnvo5JDI_PVnwPg7BAgf-rSjJ_oai_dl5TezvVomr--Nw3pBH9EOoAM82af4zykWLRu7cTcIrrZ9mXo9rdaUCtT_QObg-V4Yxn-F1RJbtedjHoe83RRY4_T2UqHdRwKihY8se2HsEEnjQI0y3X6MnatkPd7zu_YknYVMNI89d0iDDCjXxnvg44-79KVUEF-98HhamoSZiLXiJWUdAvYHeyBGFZen92oNep-faYfWwkeYKN7HRsaUixScXCwYKFj4gPxNkhuDcw2LKLcLMlCLTwxegmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6-bfOVJBBPcfzCFSXCuPO1Dz0lm6QQX-5_tQtYX_m5JRy5zTEb7cEmCXqPkZJNR-Z7asS0nUskqx8usN8VqF-W5e_AS3m70MAl7UqZO8CB97OZnTbnnRIyPpeUsUxp8Obm18Ts8n1haii3zsN3RepuQKcQpjY1mJYRMWq96UhmNGrNk1r0DWqPyZWf7Gu-GcdOsYnLB-5bDYTf8kaclqLrxx6dwQxtM3zcGfCgDvkBdmM8bRQdukcDqMeq0L9ScGWS052I73M9uRzMn3YgD3SoP1kWtqEEt9-7tfcQX32rtWbyuR6MHCkdrOYlZHk0pOfWSAlJjh_-wlO6ZRiL7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4GR775Lf9IvKuBnYXUVrd0kmwe1Wg3P9SH6QgH0ftxiWxBwgivzygaRanQ4kXnDdQgOpbzbpGO1T9KjEhBEmphn1KFSW24jRrelpcsFMRtyrDDw1IeR8e7yYFO71CnHw5Nd_hfjn-wnVvQOq_odFTRrLDgwHB64UpSKzEIkjSxzQ6aqwFSswKyj-t4dkWIQfldfedmUOuyxJuuOAowxqnih-zG88hzIdnq18IZc6alFl837bghChZ-VWinvZO9Sld827yZmjd7PSqyPo_faTsgpIKyMFHaSLvCzisYvcGSRiGQcGIhwdlLwFyrFG-xamFACa6BzIDsXqNgeuEZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alGRWVYmul9sl1JYPSbTelcIFebyte3XqVP1yRg1LiYzahXATGMfunxtXQkorDLPVcR0Cg-KAmFZLSle8MSLV0JP9ee41qLzIevhlxxPzL-8ngvgzhXdmyE4OTA9GNYGgofb0syarORTp8hj3dQDhqHmhXk707f0OcfeEcbBy98Bs01IW56WosPUMbD2dYJitWcDNf93dIRVU8f46wGLXhGKqCTMXF5ptirf7ZhnmkyM-6OwWdWdELN8Rqo9Xki98IEnyHOEI3o4pz0p_pJVsonPsnLDw-HNLcX4_L3dga5KURnCMO1H80C1G5bzzhtapwSHS3DWJSqLEWKavlCQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYOQoqh91OzBBEa5WEYFpWDA1JnklQai7fwysym28koUT9KzOXQIHcKZqoN_DGepMleNKW09Zv0_n2VqMph9cZFad7lOhOgXmsVyVrirAj_3gIW6WOi-j4x_lwS2sewDNGs641wC723JHmdERMWvc228h4X861tHypRtNGDQG9xWi10LIY0UMREfG5sN-CbtFQE2GJTECrGkdKzGD9GGc0pUTT4m3ar9j_119NRXCKz6PnHmbS4iuhpMLSqqLcYRnOQhBEEGllIzJKpnfVmXDXJhfBG-N2CpYUPv3scqg_hW_aU7h_YLqXwTILO7R7med_pMP0oOKYasfXnOgWGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBpnh50pdv0AA-2BCq_JG8__Mw-y_nulShVksAf6QV3bm8yIkXyJw_GwCrqDr5pgcvdSlctGctM90WDBZexo6o15aWYFPrTgf6YXTC-CFOJ2kf9-IETONoWJMEvBGhSJReGJOjKdVwShTOg_CSAkA9Ld7RIDRspPyNsgCQ1fnsTP31oFfO10jRnUqBkAcN1A5ApGEPzlqg6jutQTl82zb3SOXNvb8yH4drX17QUTTmNahz5NVMVPG18OPxHFEQPuNEa9zXULOedUJgQ9NY3M_6nuTLrKu-wY6Di0_LRfYiEbAKzF9Kt652T8wN9XONhy0FBBbk0QvWvbvhRYv94i9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO2r3JnomR_mhtIecxyEqox9QFGOjOu0oybw8pKQ-KquF5owpZRSB16CRxEh0iRLg1XcGbrwMqG4LvxXqdm61ednXdk8wjlnUkg-PcRXaxYPax6TrIF8qN366jfRRm7v1gXEWseL7PWsNGm7_OU7u98iXHAfQCJAApZRKdKivoqAfPDYafZ2Z5fYmOrdRMdpHqE20e2a0BZdMN8F5YF0evRT2X-gkv7akJuG_0X4EFHqfjjdzK0ywTbckAaTPiTxB-U-JKXDw6OPYCGwFSmUHryxzoYEo1ICC8Kvwxka0UcK0UczgC3qIv7nYcwx845-d25KuW2z849QvKYXKA4Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9QtjKF0PkJpXQhb9aw-TrORdQPP-B2dORpfP1ZX05gzzG56vlJPf-k1c_LTY1761qFDSJAPL4fTtIqM2V_xolVvVNIGIMGIp2TeMpeZ0nGX-37_FysCzrHRG5B5JVFpSNOU20sfkUWZz0RNK504YZd7v8eFeta9kSf5DO7OdR13C4tXqz89-1W2wn0oGn5n6MiyNqiM7ZtqNVQP7Mzx9AMOvbdpErtdVy8tmGj98aOETOvYfyJNJYzgujMr29vwx3boHIPESUpxVTzpAjVLI_HX5hYwuA2I3xtHA4bAv35Vz3jLCuA5RpjK0-zltNspX46P28_V44Pl8WDLwaKFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmrmr3esKoHcdHbDkrIWOjd_k6lHl0j7PL_wDJ0_HMZOLyxt6QZIRUXmQRmeAMSRW8zLSASwq90xWsMwz8pua1kylJbGdfcwifiSqXxOLANVIwTpdFMkkdahERN5zkITRsmUN6j_8Eu7Y1P-P4whOVcxAWPtf4lPAwYPaBTm0KLWGnEJ94BlWK6MZ_AHfs3Csxro2sFPSECYZPBCRlJK5EKmpMzaNTNaE4whZ5Yc3-7v49FDGulQqLB-Kk5Odr13yc0_IAI3wih57ytZZGLHua-hPXmcC9JcHgCTmrbW9UOiSHDw8Zsp0ahb9l2PJ78qMaA_7lq3Wcp66Vxk_9CCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5_KiiqH3LDUvuB6H2rcrakvbMMXzOp8vUbvteXh13K-tsoCTgEsHdgHKs5hYJwz5GW3LYxk3737Lmhm64fHM1ZrwCCyrV0AWByeZcrPcLXhyhBtd3siuX2zFJQj4OkmYMLPYjYtXSBpM9f6jutf9mNEvbswccf5E5Rb9m1WhB6bewTUt4dzZG8rrjMORHLZCbKUFSK1A0-LbU6keWR90NX9m3v1ts4lqQ-zcQH4yEfi-IoVHmMfnFv9m0Y_OjfmSdc8JpRDGR6V7HhYxGoA_ziF42yrn4hfyzW1ecYv3ipb8bSznnMbU7qkUuXrMbrUlb8JRdMTsMxbIjhb2RV1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrmhroM3OltksV-N2HXG5Fyu4eEuExEL8qeQ0yEAMbJe0JApxN0yR7A3xizeGZINe5Mt5WhYz8sh_vAhIFaL15pOEPpABsYcUU5jHtYIfRglsO9XYIQAksJSVPLQNdoVixQwxpvQGJVNQsQEs-4khNj4KaKL5rCnbqPLZVbz--qno9n5Z8WQfqEcB1JW8Q6oyPPjmxVCETeIqVdIYEGgHier-8aNeTQqPCo3kNTFZXBNkPzL-U6LRzVi9hNpdaIHGk_VU7DS4buKEeB5t_oZ5sna7hUSlYVkUqxREYtTUvdTLnq9UaQbOutMXDPgxq5hxeF8rQtda0oLRa30oxSkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unr3z-bRva4d-mGyAS2zneFhedZ3ovXfsxFD2hU_aSlf_suonjPpVKjIVzB1AsylicMsQ7QxEf0-njUl_Ii4Umw3hko7dzzRGV8v6hvwLLJ3bFB4f8lPNeemLQVm8twIoodGU0ntdfhOAtcNOwGGjpXcemhGFLbbBeTD8swdqD_jZiGu8MfjE5J6zTS21JWT2PeRj6_9T5tqZGHPJarhHRRnMJ0fmMvZO5lP5STq9mod2-tzOxp_u4Ryje7VFSh6Q6kFLfv1cysKdUvsXOXkDRYwVE-6kMYzIPbpjm-ZOOCk04hC5_fusGZ0FkQPkBA6VCm9ra8dWH-zV7qibKiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=oApC_xjrUBAADECr5DhxHvFLTgfCGIGkKjUHguYUBKqwVz_XSCQBnXsfs364VJEinevouEx-SDc2SyYy_qw-nFmna5M6kNpOpRNtY1lpPMfhIh3e0P1RURHBQn3m1WMIa0p_YzUALVDRdwiRCpFNP-68HRWkMKWOckuSVJ18OVe2IJAsyW0uSTuj5HFFzOFxHIaE6SerRzMtK5J7l6XhCwYEpKknR8K9t9Wwwd6W7nFCoiDtydmP1JM09AR6keK8Jp-XggXTPmV6_kk3HnSwaE_RtXxSt3u42Tvn0IdxV1RMbArES6jrF8RYceMAHrKtOz0XtWjK2gQLMScL2YmMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=oApC_xjrUBAADECr5DhxHvFLTgfCGIGkKjUHguYUBKqwVz_XSCQBnXsfs364VJEinevouEx-SDc2SyYy_qw-nFmna5M6kNpOpRNtY1lpPMfhIh3e0P1RURHBQn3m1WMIa0p_YzUALVDRdwiRCpFNP-68HRWkMKWOckuSVJ18OVe2IJAsyW0uSTuj5HFFzOFxHIaE6SerRzMtK5J7l6XhCwYEpKknR8K9t9Wwwd6W7nFCoiDtydmP1JM09AR6keK8Jp-XggXTPmV6_kk3HnSwaE_RtXxSt3u42Tvn0IdxV1RMbArES6jrF8RYceMAHrKtOz0XtWjK2gQLMScL2YmMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRKBwOwshsqZDrk9u_mPjIXEc2bzj01wDwWBFCUM7a2T5GCT-btt3H61TXC1LhGi0YEE2qo8sRyupio4NN1MOVM6O5LXv566f06t-FkMgiFbAexMalibwIrA3DjoGRizbtRScxN6jC50ACJk6hVlo4JRK1ESTd53tCRJD_yGnQYSf16UQz_YOwT4vRifVm_FNkuG4BOHfYt5s3SYr8YqSUJMcjkdMNlD2qAx0PLNOMUbund2cTO3-CXSUJNv07a753-gnBRjPASz6BWvFEWmqDgigplH-FnM-LnYp2OmsdKcDAd-O3peoH6f7e7XbflC6LIaMs9LEoP8K9IQuUw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qihqocrU89XH52pxQWVBnMlvsBy-p2Jt2lFN7pxa6c6iFP6_3IoFR03jvMDfXd7kK5JQv6RxPg6XPkqPTLabLxiNAIeCdLHgLNTKiJ11FQUWlgdXTPIM6qleDqqiDEmVdoKNZEa8-rfM32zIjSEgLHLA0MVjwnidhqVvFhWeOhb5jVDbYF0MvcOl0mjleIMy_-GxaS7wFc9yppUWyxVVf3LG0NubKxvROs7KtJMfJWzzqC1oSQVBCjzL4iwhEfAl8nSR1kOvGfaV7o0xop2Nikr8VVEFDfwf6ms5pPli9UInDH-dmAuO3lHUaMnEFmca7UD1SylZG5LA-zpM9LrTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=NTJX_V6NZLtty6yT1kXZG6V977-tz7-Av4MUnsI1sVAyO6DD0p8TJRtz_YtWzAOWYBIiiNCQgjSOEf0ad5hjnloOOWuc8FkCEPNeRh7EsbMZlTtjXnJqbTqt9-ySWU9DN-Uj41JEQyBcMz6fUuVITPTT9bhQEqRlQxwUsb9bteOyaJbt5kdhricEMT8LbWbsMTSA7e8WCr1c4P6vvcnWITrBR4wcJk0xEDm2yRNwHMPEJ0d2BEE_AZf5axFHgL0AJEeM9hzhnBY6E9mXVvZDXbXYIaG_B-tNeApSgYWglqYwvdGHDzt2i1avUz5kvKuvqAMTIt1d0HsKtGzKaOfPdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=NTJX_V6NZLtty6yT1kXZG6V977-tz7-Av4MUnsI1sVAyO6DD0p8TJRtz_YtWzAOWYBIiiNCQgjSOEf0ad5hjnloOOWuc8FkCEPNeRh7EsbMZlTtjXnJqbTqt9-ySWU9DN-Uj41JEQyBcMz6fUuVITPTT9bhQEqRlQxwUsb9bteOyaJbt5kdhricEMT8LbWbsMTSA7e8WCr1c4P6vvcnWITrBR4wcJk0xEDm2yRNwHMPEJ0d2BEE_AZf5axFHgL0AJEeM9hzhnBY6E9mXVvZDXbXYIaG_B-tNeApSgYWglqYwvdGHDzt2i1avUz5kvKuvqAMTIt1d0HsKtGzKaOfPdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wYQ5VJhY2W0Ij858hXD98Ci-jjamVFp5biEWhRLyKbDE9DrD1DFj09p-Mg_AyofCPQeRxdQfgM72ls9t6jsAGYedLQCRWNOnHzqgsUqhslVeVNuefVNHQ5nq7X9D21yJTlTaEZUZ8-SWeKQr2QTWnE0tmOhRmxGz7I0GWmTfXC3YFBXpU5XFo4J7m3_7XI2-u67BPOymtWUHb8dY8Wgt5g5lCfwRjlbF8UuvVUfLMFTrJWUnNiSeSjG5Vz22dhLcGkwE-FVeP-7VY34oeaRGJybDtBHHz5cx48Atm-F_6k723-KJg38_N8WSTmuAg-nlsP-8A9jyS4iIII1J_KwENho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wYQ5VJhY2W0Ij858hXD98Ci-jjamVFp5biEWhRLyKbDE9DrD1DFj09p-Mg_AyofCPQeRxdQfgM72ls9t6jsAGYedLQCRWNOnHzqgsUqhslVeVNuefVNHQ5nq7X9D21yJTlTaEZUZ8-SWeKQr2QTWnE0tmOhRmxGz7I0GWmTfXC3YFBXpU5XFo4J7m3_7XI2-u67BPOymtWUHb8dY8Wgt5g5lCfwRjlbF8UuvVUfLMFTrJWUnNiSeSjG5Vz22dhLcGkwE-FVeP-7VY34oeaRGJybDtBHHz5cx48Atm-F_6k723-KJg38_N8WSTmuAg-nlsP-8A9jyS4iIII1J_KwENho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCp94K0eE7jqyvzmBWth2ucpr1nifrXB-IHPJuVubt9UZeyRRv8Cz1MyfweXS01ImeC42hRTH6tbX0injd5mshtyev4CoO0MZ0uF4hMhZZ1kifvaI0rZw_b48_dnIp2-BrgWxhW8Zr8Vtefrss5Y-GfIVKKbI564r0LjzZ-t2YrzdCOmVqg-7lgzFR9alx8dsF31s6YnM2eajG_Ced9tvNof1ryWKmkeeqRmYqZB6KlPl46zWwdwGRChqC9eHzrdMDeJEDTwPbMqx998JrMjYxCebGusdAO4WROUeA7vBbYcfsOKg_A9Dwq5LIL3qvduLJpq-KXIwtk1MC1qDGc40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr26
📩
@winro_io</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSYT2K6XhpcuxiZNUf0yOSZ4fvRVNMXr4kX8ImYMRXeuqotVKycFWljnRKQjQYMZAPNhnx7XN3UEC6gGEgeh_bFqW91WS6UAmt4lkAriZrs1OcqY0c26ZVOFMpDhXMnOo43RGkKMSYVXebPDCei5aliJGj_AjyGN0l2fiMTqXqxAHUyB_ZXNepBWreAuG1x7wx7pBwZf-hk5N1i_849q8Q7ZS4H8JMsNNt_yhCmF_TeIpfJXtaclKL9zl_g7Z_RNQNWGrtQ1hp9fUY8RJUHWS_bw5lHVf-GnawdDr6rUEEZF-qft2bYmP_TZsHHwJgD2lHNQgkYWdMBy_5AczQ9VRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=JTwg_0u5WC4ScHn72NkGNCxezKuh3XMcko9-kUlgrb_7crUEDhhSkeBeoOWfN_eqRFkQT2jkfSy6cWAUEHEYGs4vq8qg5DbmjLjZp6W5ATdJDOEKDj1upEWMO-pyR0BsjJCtpo0SrigNN0YozbOG1a0VkqBKFgl7g6Ec4kJHhVDhR7OjlWj-Cv5kXqDFO70uo4Meaz4cZhyshNUv8ynSp2kZfqd9eBzFDPS2FKvYSkx2r0Z4dTYty46PoEK2R_VIroODzuAmyfbztN1QlJzgjHSWO7AzpoWyvCW9bZyu_flAfj3YtC5ek6b6QkXUcAYRsR9N7vBXDs9caztD6w2qxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=JTwg_0u5WC4ScHn72NkGNCxezKuh3XMcko9-kUlgrb_7crUEDhhSkeBeoOWfN_eqRFkQT2jkfSy6cWAUEHEYGs4vq8qg5DbmjLjZp6W5ATdJDOEKDj1upEWMO-pyR0BsjJCtpo0SrigNN0YozbOG1a0VkqBKFgl7g6Ec4kJHhVDhR7OjlWj-Cv5kXqDFO70uo4Meaz4cZhyshNUv8ynSp2kZfqd9eBzFDPS2FKvYSkx2r0Z4dTYty46PoEK2R_VIroODzuAmyfbztN1QlJzgjHSWO7AzpoWyvCW9bZyu_flAfj3YtC5ek6b6QkXUcAYRsR9N7vBXDs9caztD6w2qxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=IeuICwsi0YC4Z0roIzOWLS4-6ritP1yzSZP4ToYxmq8oJvd0LiDHGtIS82M0VcLOcgGMcwFuLfqVM79am2u_rt88C_hvLbxc8DO_Qy2Q0GDnoHl_ZyG0RmYdn7tLoNiZSZLNup01wneH5XrHHjiyUfrBrR0ZwJtkNQzUYgJMRaAjIefl7g_P3PgTZwVZoSEJqthebeb23LanXHsRWD7LQaxgQY0GXZ_9aCAAfrio_Js5FVddaRUMsJTvjYt57gvnuGejmGfJ0MW69sq3dADCcUV6De_bEtTgQgawKvFJksO7xzAwC6GctExI8eF50Tfe_5ViLvZhNWPJM72k3puhe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=IeuICwsi0YC4Z0roIzOWLS4-6ritP1yzSZP4ToYxmq8oJvd0LiDHGtIS82M0VcLOcgGMcwFuLfqVM79am2u_rt88C_hvLbxc8DO_Qy2Q0GDnoHl_ZyG0RmYdn7tLoNiZSZLNup01wneH5XrHHjiyUfrBrR0ZwJtkNQzUYgJMRaAjIefl7g_P3PgTZwVZoSEJqthebeb23LanXHsRWD7LQaxgQY0GXZ_9aCAAfrio_Js5FVddaRUMsJTvjYt57gvnuGejmGfJ0MW69sq3dADCcUV6De_bEtTgQgawKvFJksO7xzAwC6GctExI8eF50Tfe_5ViLvZhNWPJM72k3puhe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=ZDliMbGV7BVKwIt2hsPwAPqdK9AYMo0JU4F0Au4bBf_K_UfncwASmwNvo00_XjNdeOcLOe72sKQq2v2EpXZ81YY9Wpk9d-cSpTzS8bGA8bIWiavBNDfBi9xtZF9aS41ZCTY8nCj-Zc3Evlz5-c4jysA4Id4pMqB2lLQOsWHMqYfMCIK1Y_zakYz7bYUjDzgpRgIIB88AqmHwmP_76x7iZINHo2h-vjz5UglDr9MhrgfLZaq4vvPPF9_kJfnPtRFcxr80gf8DCVN-kFNqdampjO18gt8CW9vonJ35uqKRGPibsGPGJbV1zhFpg4epdZphhSHgQq6u-W2uFj913T5_E0QWdAj9nqp7sTm6yTkScqzSPeuvwhtU0-9ILPx8NVOyQxVQu9reM5d--GuGqDpxNXE35-aUcxprJwrwmdIDENFR3PALqfbrAaox0QP5YKKZRaEVRCw7iCYki6Eq-SLFhnFNBWRsOXIhktlXnqqL2Jvjd7vfC2KVeLiNaH9nNSMKBWAniVGr84giu7hn0xRWc_w9M-dduzdl0uxEZFNEz8ZmWLM_wlGK_TqeznHT2XaeEa4Ow7yDmHzxRglmM3ZmY96DuMba8xWlPJJ0Hu86nxoehlRyBd4UYTlWclYIHdWGYpLecNjjgUyLOuC1FoMkmh7V30zwAtOyGoo1CpISopM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=ZDliMbGV7BVKwIt2hsPwAPqdK9AYMo0JU4F0Au4bBf_K_UfncwASmwNvo00_XjNdeOcLOe72sKQq2v2EpXZ81YY9Wpk9d-cSpTzS8bGA8bIWiavBNDfBi9xtZF9aS41ZCTY8nCj-Zc3Evlz5-c4jysA4Id4pMqB2lLQOsWHMqYfMCIK1Y_zakYz7bYUjDzgpRgIIB88AqmHwmP_76x7iZINHo2h-vjz5UglDr9MhrgfLZaq4vvPPF9_kJfnPtRFcxr80gf8DCVN-kFNqdampjO18gt8CW9vonJ35uqKRGPibsGPGJbV1zhFpg4epdZphhSHgQq6u-W2uFj913T5_E0QWdAj9nqp7sTm6yTkScqzSPeuvwhtU0-9ILPx8NVOyQxVQu9reM5d--GuGqDpxNXE35-aUcxprJwrwmdIDENFR3PALqfbrAaox0QP5YKKZRaEVRCw7iCYki6Eq-SLFhnFNBWRsOXIhktlXnqqL2Jvjd7vfC2KVeLiNaH9nNSMKBWAniVGr84giu7hn0xRWc_w9M-dduzdl0uxEZFNEz8ZmWLM_wlGK_TqeznHT2XaeEa4Ow7yDmHzxRglmM3ZmY96DuMba8xWlPJJ0Hu86nxoehlRyBd4UYTlWclYIHdWGYpLecNjjgUyLOuC1FoMkmh7V30zwAtOyGoo1CpISopM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhHJ2v41aATgC2VfTZbi78TSNiADbhsd6BrGx8iKBt18WW4JnJ4AzFcs0HgBGGRe0mqzFyIRtbKnEupPMqIkdqSmUkOhm4MUaDnrdGiNznuBq-VZxkfpEScuvBCW8K3AS__ohSaVmxCTcbmKMu-OHcHZqpnU_OW0a1akW0w_7KEXKbJVLQuetz-_Uhn4hzkGGrD5gBaKdR0-kDGh-l3cEHsM1B8uETNxV-e5pPfm7kH1qcc5CXmn5jHICbDpoiuLnTgvWFx3e8vxz27kcJY6nt5JNOPQ2XGwDc-d4tIX1Jr5y3Xocw7P9O3lh58owl6lYkvgacFH37LGTbCujZZS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=pCxPBfO4H5K7PjyX_9G7Kzdct80795H6QuD5OAx75MIq-c7kSbRWaoQBRAfqazDnqGK4KXIbVtP04Md4ZRJoW-OACr3pNlc4nUCl_m0lMcdaWPvyVZYfPZsAejbz0thZ92_j_zNYM0rTV4BZ0IhPmF0iHPD2cgp-5Lqd9o5E6GVAMZGfIrlMZXXKo95lrU9XuNE2SAruf4A6vRCfvYHg5ImPUqobo9xEzzjbm-0AK8hfgHiFpJT0J1qe-JMJnHezSnxheJbq4FGLM2BMCdKlWX9r_PmE1uDMMjpVupuVyUQilZezgeEJ0oBmYvPGwTGlwrWl7Oz4TAxN7AIP3LGi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=pCxPBfO4H5K7PjyX_9G7Kzdct80795H6QuD5OAx75MIq-c7kSbRWaoQBRAfqazDnqGK4KXIbVtP04Md4ZRJoW-OACr3pNlc4nUCl_m0lMcdaWPvyVZYfPZsAejbz0thZ92_j_zNYM0rTV4BZ0IhPmF0iHPD2cgp-5Lqd9o5E6GVAMZGfIrlMZXXKo95lrU9XuNE2SAruf4A6vRCfvYHg5ImPUqobo9xEzzjbm-0AK8hfgHiFpJT0J1qe-JMJnHezSnxheJbq4FGLM2BMCdKlWX9r_PmE1uDMMjpVupuVyUQilZezgeEJ0oBmYvPGwTGlwrWl7Oz4TAxN7AIP3LGi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=mUFkXENs704_K-Y6vJFMp8IFd6UERhpBRhoQfwRrJXURRbazOo9f5PV0-a3MFlNvIst21yhnsLmYDcdkScXCkxgnJmE5kOwhfgR_7m3TEnotfdTrIAJnsC1soWBFVJKdk5EIM9Sfif7vu6FZkzticB0lU0JXcUtNMb48CBr8rU3l-PV2RpPoTNOuz1aDs-jJOBCroHwfpnVM9Ku4OPmtt23LV_WQqKaVS-pTgOVXw6I3TknWIBVUncvJZQQwvnAr_2Xry3S6L4HSU0LOcPY2TXRnPrT12gKKfHw3XtKGPARyAjs6JKvXM3cmDEBDLKm-5bHuRA2iGEfXv__h_Ja5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=mUFkXENs704_K-Y6vJFMp8IFd6UERhpBRhoQfwRrJXURRbazOo9f5PV0-a3MFlNvIst21yhnsLmYDcdkScXCkxgnJmE5kOwhfgR_7m3TEnotfdTrIAJnsC1soWBFVJKdk5EIM9Sfif7vu6FZkzticB0lU0JXcUtNMb48CBr8rU3l-PV2RpPoTNOuz1aDs-jJOBCroHwfpnVM9Ku4OPmtt23LV_WQqKaVS-pTgOVXw6I3TknWIBVUncvJZQQwvnAr_2Xry3S6L4HSU0LOcPY2TXRnPrT12gKKfHw3XtKGPARyAjs6JKvXM3cmDEBDLKm-5bHuRA2iGEfXv__h_Ja5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQtf-Viw8NVnUgB_u20I7Cz3xEM5e2wj_Dt_XtjkS2UQiXGt0C3qXDyHCl6ab4VLkTGsSxOiUzfzkeDRXH2L1iIV80k45olrMn8dgQ3RX9aNfaytQ7Mr5iGVaz1p66SACzhuLI-XVGzdW4BZ-eGgnNsLPNC-SKeYhgxaqEolG2SAGfan-IucPzfX9oTkoTImbb8uCGraskTnLNpsJopIyVE5RI3UtNwS-svYZ8x7Qu7K1Tfb1YqEHDsYwu3kGF_Jl4aFaYUoKo_RTBgT1NS3yW-eXSmNU1e2nw3tveFVlQ1cBcD-06iFhJ60EKyVKbZo28cxrWIDAQSws5gT3fAhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmfFirhDy635Mjc9Ed-1OMq3KrjjwxSOTicvxGRt-UZIeTDRR6I-_qelE8-nPYupC636GTWCYy4EvegUP_wgbJNZDsgnchibA6_aFmtsie7tphkk-nkXm1ARaeglX8Yf68kwKC0jwCzLCUpuxBky-xwjw4l_SABFHs_YamVr4oEc3Pu9fNy6Dd79a7HwfyaMAjjDP2DptSoIQGniYge4zxtgMyeCsznkzI4BpR-MvCgaUVdauKSzeV37ZqBFLdQhjw2JXx142XjXf4SADL-ybAbEfAkhzK7qq1Ed2VlxeXshqZmp12xnxTFM0ycs89NSkM7EEYQ7Ak4d3E3VMmhhfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdx8rfFdGKDUmMvKGjo0obOTKCvOXrluXN6uwhoWIkUGlBs9_BLnMhLf__nKVbOMaT-0ZYzlNZj9NuG0tkGqFFX6Ti6vxq4Du2jZ_U7ENoZlE1kHBo7a7mE3QycCKhAP4JHLvQ9LKT3nFfDAy_GlIOJWMbAM6MW1_hZW8io50a-rJQtCmGOUE-x2rOXI21TY5TzQzoIPmrTGxFZRY1Su9HzwHNAJnWsCvFO76GQj3G3yvaT3aZ_Gs-Q4XQXlLNiDef6KFV1sIhjIcV8vb1nSMXryqCh-PXGbrWybktMqjOZs1Y5P4KYQqoChsS5By8aY4l92n_NkBqaxZSichj2gGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtkjYgIocso54NvGy0irklLO_ffoUdl-VM_UuxOOcwfH3OWeFilXzT7tc0dNLq9CsmjnOXZLJ4fhtNXrlSmUbdRZUneYfnP2zg2zcnzxetlRFKwFkODGWsPN66Rwvhx8M54gppNLxRAEF5kSOOMRoPlgvgwSwvA8vQEGfqpl30J_KMvnVzS3btoMrYDwRtwQ2_IoWNToWpSuK4Z8yQmvpzwZ_MpLu2XXJaNnQvdtS6ZzuWlSvRe-vu-7ADxMfjY-J4pHLlfkuqz81Q7MkGQ0SA16LXvwiIYLZ1nINE4qk-yEa7rwxt7YBsiDysMDqttGo1Mv7LFLZRuonX2Dt435xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxEJuJKeuKi7eGVtt8nivlQ3uK6l3wxVuzOwcU8GCpog7mmK4gZ3jZEd9YNBrOiTralDVGN4ULqqv_1BzGsJTSPCIW850K4bLtgAio9a0mo64p-TVb5vRWz5SX4mUeMqxy4baZEldHGZdx-5ift4SM2CJS-vySj0pkt6_u1ANmS4RXw-4FA69Cj6kk9lqolInDPuwyDqZ4qE_pgip8yc65dkB4xjlEBnatNKUw5O7lhyg49pMEw7gSMdbFx9eIlMHAKW4b8P5au-8Y82400txfZx0yalnD5f7NXS2toL6b9umt58GoDB0XH2fhEOFwj8vQKhL809ASKKkdjW_SBtEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT9AyiF29aWJBdQR496iEXoATI4fn2AHbC_6nLf6-zkRvWtYvbKVKrlYr2c9e3VSCdZCWW5koPt0Jj53Pslo3nMG-f8FIHe037M8Leb9-KNTzL-K3ffFsuNAlT-0PQhpBFuouNrr0q4sfEckl6kAZouEwQurg3omPTTcNfZUBxEGUG_2SZ3U2QkwVXNmpC3uZEeS_XK4Vy93kr01nSjpa-k2YZKapuqlVgNAcIJgAvegxY29SC3i2IKwyGIwLl2SjAXY7Vq6XmCjfX95cA6lcGcGGt9NIbjiWT_cwEJnHZGEzWOGC06ggJk2PpJ4t_6-W3XbURjf82Ye-BAvGbtyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=FGqMkX1woEP_w2PE6JnbKzinyKElK4qBeuJSVerLdNtMT_QhnTtlzuJ6PqQHVkt_gLA8ql5C3XEEMLrqs8YIO0_PDfYnLpSJZaM-g_tye_NbtqrpygPZ6OqmNfaB4-JX0wSB_2VYjzBf16UZWMNVRlQVFBPajcv9L2PdQR8I78000gPG4nQNtsR-cOpPo0VqIhFJrVMPU0QMK2ZIV77Jr5DzTOoe5q8i5PgeQlN58k4vP3JZGSsrZ0pMDQcDqKaZOqtRnmZq4SZoaGxJ1Bn6cu_kmi1ETX6yQq0HoVHNyOAFJNrgz761J16YES5_4PnnSTzPnp5q-bgaGml05wtWRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=FGqMkX1woEP_w2PE6JnbKzinyKElK4qBeuJSVerLdNtMT_QhnTtlzuJ6PqQHVkt_gLA8ql5C3XEEMLrqs8YIO0_PDfYnLpSJZaM-g_tye_NbtqrpygPZ6OqmNfaB4-JX0wSB_2VYjzBf16UZWMNVRlQVFBPajcv9L2PdQR8I78000gPG4nQNtsR-cOpPo0VqIhFJrVMPU0QMK2ZIV77Jr5DzTOoe5q8i5PgeQlN58k4vP3JZGSsrZ0pMDQcDqKaZOqtRnmZq4SZoaGxJ1Bn6cu_kmi1ETX6yQq0HoVHNyOAFJNrgz761J16YES5_4PnnSTzPnp5q-bgaGml05wtWRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9CAVff1jx4WNHauV-iNeHWKBdOSTmu-PybT0vDRazGjxU04LB25XcHCufj1ntnroeUnd-NmB9QHcwg5J_BwHMGsK-asKkD_0Ok5-uzUItklLCUXQW3C1Tqs7i6eJROL5kla9k5MgPjS6SleNsM-h8XqFwnXyLElFSYuAuDb5-MWaiHmlYfQT_apyBWCF8YG_FW3J9d3__ISGOHEarjsNRkp1Emg6CoXDBcQ7c5xvnkTvVh3wXdQ750LIaOHR4L-k0Qih7mWgXO8BCcxYQj6gkfafDwjMfn9pUlVCWnLLwHUWJmSbEGv29trut-RMkIH8XcwfUHyRxpiAZvqeZSk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Trb07TgXR7ZyGclvHMy-tfV1GgmBLjO7HCj2LaPjORdUVRU-5DNas_u-bwx65cQSxHGyHgfeOsHM9txghZoCJpzNIeDV202rIMmr8UnczNTyOlAscBY0mrgilVVAMwlNcKslRhady5OF3kRoi46bqLQ7A0hk2Gp76uzTqu9DPkugnWwu7NLN3ItVEsue85h9CRDIrXnu0LwpjMgKtrvKpny-ogsPZFn_ru_mZwnVPktbuDDtTzoAdIEwW1WM2Q2BuP4iNSuGX_iPQDShGptfc55KHSfWISRh43wkWk-oWxhDpSDL0JaCmC_5MvgViZxNEGksZExiOo0mW_Svafug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owSZmc_xMPPxWHskYnOHStDPo7wZjUBT1WrXN2R7eZaFoFDAi8kx2QyVwviMKIrUpfer8UsWW16JKrJf72fAnDbX6CdfzR_kYgTU-WpWvf8Yv_EyFK6kTUT-46Dzf3PN3Cqi5NPE7R5IZOqVl2abgwVk5w3fvUcKaefWYNKLtErJIOJuhOR0EBBo5NHEkYRVtlglLsMrwxamZbXj5nm0Vg-aWB4U8Q49NS5a8ZLtodbLHOaILY_1lNiTS2tx7UZmPXHtS0JRtQz-y9czDRXjk095GMxQxvuz5GzUrptK8YnrhuUWhAt6lkASAei9XWHdIeQrJzNW-ORj35WQkfKubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOnaKV4FHEwCbsJCYzEmJUE6DjvPHmme-hazwB2fe6QJy6e7fSh8PPRU0AUNny7pGbpdaDbLqzhUPgRMDzYU0Q4VVhGBw3e9cWG8i6upgECjVSwFUzjH42CxTFpAmEj5Amo9Dny_ICEGxCdgQsGQWEwReb5OJwsw6FpTJBc6ygWoLwNe08XBeYlsyUbriKsaBpe_wldPNrDJvEOXI6XYCFGt35hS3ZTq_SkXrdgyhGVMgV9s_zZWmn-BDPOQyciRD94mit7ToBdTT978iplro_8nPz-VRQes3Vxf_rGVGmuwZVxooCRKk18UR6FPBgF0ZZ4i_hiKcesU2l8zA5IgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn-mWWLq12FnJL-KB2aSLHz1QxdINReHwu0E1T2jU8zPluvrrb_zioohEaCnEx_mLSLsrXpcVtr1OtlhazFejCjYUerXtqp2TIjy2R-dpWqjmWO36b6w5CDIyiEEPuClRkBcqQX5NzMtb7nOa9kGYEhZIiZoXGf6R3N9QLrkkufMgR5HTxNXKfzt8YawFyXZGEX67ETQ5TZZX1rSUnvdHjGdfNA-A_r_GzZlr5DoGhAJZAzmCK-h6XuA2YLBwNrddO_2c04LC5-7Lb51p-5PsmNsX4NWoRxWEadm26t7uyP-2988emNwIKY_JhAFLhwFps7Wg23A9r_jM9_l-gd8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95Dcbl-dvJ0gSusIiXJ4DxFBm022YFd4bnMtORpWtGDjQ3yrjkzeXVV129ZQ1LFrJLJU7huKZHlX4JMY7qQgFYIGXZlVnLzqu477uW9axlHIeF4cmhw8pPZd_O7gF-0FU_crFflHr8_KKqg9FrbTVb9ZFCiKLi5o7JLqqVrhZX6l5mVnO0lbWehjN27CaPPDb619lV3x-OGF_Y3iLY_qOHDi3hC-EAWE73UCFT_hFzOG9vy8gfnQOxmwAzl2zxpcw5pF7qK0LKBoA5PM3zyA7Db8mKg9opzJaUYRna-hV-chbKYXiwtp0PQZ0j_440-NXuRr0HjmMxVUGsfHwEtTqeiOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95Dcbl-dvJ0gSusIiXJ4DxFBm022YFd4bnMtORpWtGDjQ3yrjkzeXVV129ZQ1LFrJLJU7huKZHlX4JMY7qQgFYIGXZlVnLzqu477uW9axlHIeF4cmhw8pPZd_O7gF-0FU_crFflHr8_KKqg9FrbTVb9ZFCiKLi5o7JLqqVrhZX6l5mVnO0lbWehjN27CaPPDb619lV3x-OGF_Y3iLY_qOHDi3hC-EAWE73UCFT_hFzOG9vy8gfnQOxmwAzl2zxpcw5pF7qK0LKBoA5PM3zyA7Db8mKg9opzJaUYRna-hV-chbKYXiwtp0PQZ0j_440-NXuRr0HjmMxVUGsfHwEtTqeiOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBxw8xid7i53NuK7AcF-b6FUK0f0KncP_3BTiCK-AehjoLBkHWarhgVefEM8iMuI1Sm2CJ5HzRONtWlpFMJsmTLZzaGZdjgF1iF4_yb0xkOwnTb8ZPPb_WjYXbyEgUZ36GRHdwdYT-FUwxEzD6P1WIC3Xmn_hwHfybLXB6UCNy_cSSxtwBfPafwnJ537QBMKm4uVs0KF0JdZI4Jh82jCc58heEr8KwnTUn_RQfvOpDorC2Lt49DB2VyRipxA67l4NUr8KH-N-mMshPXcW4uuayz0kBebCjRa6QBqpamnus_7Rs54FG2s-Z-m135u5ZwYTyFrqMaSXgHsHMyDZaVObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8HEXU1ejn0WEkHMLSQBz-m7D5OTFlUrKXrtG-qlCl0nM1WrCaWXs9oJJRTf3QXqomN3si-fMu2HhBhf_6xnJRLTQ_BHCYqLsU72WIar68D1EpQVQhR4iZUPJ6tJ6LAXxG9lIeKFow8pscxSu-e6fyyXMd-GHNpvRGxCyfWJWDLyeB7zQOVoM4clsZcPWiK2wQ1twoL57uP4U9zHl2OTNXQlCgmtSeZEjjujCTKIzccF26znTWac8If_f91mj-vuFxqu-UW4e-4nQVwPvvco-K2RaHx3rOyc1k1qehRwr9g0VexY-t8k5Xxf9WDY4FZU4g2Kz7tIco9CvJmj9wpPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=FWHC7nMo88f7aYNqu5ILr0rOxlAdXyZn6An1KUBWth3lipNXE7svjeCj0oyP8t-c2H9uBmhypCfPH4GJqYXQMRgioJoRpm0VQbYwguVIbrxk8bYyWsdFA2eM2jctcBXx4dm3KEe2_9qbn3Ax5RppydFqU8-1wsC3qqgy2TbOARBvc3esXI67kS-DM9K1UKWiT-HmeG9yxlkyHmx_i7dZd9KmnS8_R7LDnX9GEuLId1Eci0DkDUG10L3UJ6znK5vJP9s5JR7CTE_2dY0DFwaM4YgjE19P30E_7b_RZ9mQxYEvFHo5Wrdt24vutHvGqRFNGnm0NmgXz3zlVJyqvSOnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=FWHC7nMo88f7aYNqu5ILr0rOxlAdXyZn6An1KUBWth3lipNXE7svjeCj0oyP8t-c2H9uBmhypCfPH4GJqYXQMRgioJoRpm0VQbYwguVIbrxk8bYyWsdFA2eM2jctcBXx4dm3KEe2_9qbn3Ax5RppydFqU8-1wsC3qqgy2TbOARBvc3esXI67kS-DM9K1UKWiT-HmeG9yxlkyHmx_i7dZd9KmnS8_R7LDnX9GEuLId1Eci0DkDUG10L3UJ6znK5vJP9s5JR7CTE_2dY0DFwaM4YgjE19P30E_7b_RZ9mQxYEvFHo5Wrdt24vutHvGqRFNGnm0NmgXz3zlVJyqvSOnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n22WF0JZlhqO8GbkUl3z7SKut-3KcuFaCB1cGfmRFNAukKhq2Jdt1GBj3EhUGxVIWe-_hfkk9YBtq4g1Xs4VD5wgu2HX9g4Rm2JIciqmtkF8dZhMSRNwRsm6lKv7qvwIDuS2f4hK77WraUQvnUxbPksP-rhxBXX6YRMBWdVW_LtKpnbsItQ6OEtmeMoJVdsS33o_douPMYG3ZYen4DyfxYa6mUHa7v2Wa_nMOefOOJ9Telv8AvkPybN_bziyw79vBpwb3C5u6AUqAGe5rZXxYL5kGMGezm9lTbAJBnYhqV_sVfV_T9URMqueFOSvnMbW_psPB8H2FgJzWZuIZB5R4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=BtAaMncpxiHPJB50NqBDXxxot8ksF2aPi4SsUjS-PrQk_BqikQXP6q8Kk-XOWU3871-F-jcC-aPbRi8NAKcwPwfmi_j9CjPNIKrHUgykdRVBIrg46GaK2CXlgCFYR5h6SY7ItdGU4sMoHZ15vPu8S4s1FyqDU6GquDlmLQGHdLE1Qrnido0CnTz1ePUM-cODUH9FUrY_eFT_vLQQdIw6zRNYVRg5GvUF5uXpRMtuKtezVtZ0s-_KnELN7JfH8casSFAYyU1Cl8Dnptzw5qA-pHYN28Y_gnB-rD-1H348C8Ey5XAVM9HkkaSejgmePPxeOSq8V2Z_JvGek0rfhWhwxAprSwNpIRoN5CY_6DrvOTB-0OmyGEvjzYzkDLjv3kF2IyekZdbDb1eEBUWQLHVTaPXoUqfxlZ_FuVAqD38OJa6Kn8Z_A6pD7tdb7ketEwbrM8dXR9D4JyLcmfqz9mFnTUe5yQGHVwBizKJWEgAiAEYdwSvCJflX1ioKolBxmBt2Qm7QOI5gUdIZhTAGqXFWwpVll6TmOstEwBrW-opPEnsIt_kLx8nLCnOhAHNHXMlZgmtHLJIE9Fz3uCoGv_RwjcTCTwQtvOeQVNxKAiQf6VR28MRQ0Kcyu-ElNmBvO5ghzAP-2sYxRaS-bhFJrx5wyUAo_PGjAUxPH3j5mJgUBfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=BtAaMncpxiHPJB50NqBDXxxot8ksF2aPi4SsUjS-PrQk_BqikQXP6q8Kk-XOWU3871-F-jcC-aPbRi8NAKcwPwfmi_j9CjPNIKrHUgykdRVBIrg46GaK2CXlgCFYR5h6SY7ItdGU4sMoHZ15vPu8S4s1FyqDU6GquDlmLQGHdLE1Qrnido0CnTz1ePUM-cODUH9FUrY_eFT_vLQQdIw6zRNYVRg5GvUF5uXpRMtuKtezVtZ0s-_KnELN7JfH8casSFAYyU1Cl8Dnptzw5qA-pHYN28Y_gnB-rD-1H348C8Ey5XAVM9HkkaSejgmePPxeOSq8V2Z_JvGek0rfhWhwxAprSwNpIRoN5CY_6DrvOTB-0OmyGEvjzYzkDLjv3kF2IyekZdbDb1eEBUWQLHVTaPXoUqfxlZ_FuVAqD38OJa6Kn8Z_A6pD7tdb7ketEwbrM8dXR9D4JyLcmfqz9mFnTUe5yQGHVwBizKJWEgAiAEYdwSvCJflX1ioKolBxmBt2Qm7QOI5gUdIZhTAGqXFWwpVll6TmOstEwBrW-opPEnsIt_kLx8nLCnOhAHNHXMlZgmtHLJIE9Fz3uCoGv_RwjcTCTwQtvOeQVNxKAiQf6VR28MRQ0Kcyu-ElNmBvO5ghzAP-2sYxRaS-bhFJrx5wyUAo_PGjAUxPH3j5mJgUBfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXW6_PIqKcykzLpW6NDOceNCZTBAndPhAwIxGgc88HsbdYL5cqnbW1quvFn0H0wCe5MLOwKLICewF3TUBAWoFNHycW7mQ9rz7yO3Uqneh7s5jxON3Zu72_iMrJli9cdP4COQ7_N9l--bhY5VqiJnO0utCS3t3iZK-MfZC7Weoto5_pv8TfkM7R9Po1a6LtkCwo4BQBsL-OdrbqhizR1nyDJTp9dFfDver0V5ob5w3zZbkbvoivYcil4AyifLCCx5zi6VNMDGf6ACQEFsrPbPsezDz2PbyRduvgKB-WWMzFi6itJyI7q0_pXdIwcb8sPsTFBv9bYey3FesKfpm1RWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4WAl_aIA-qXa7B9VbMwhmkk8ErU1yL6FGoRWh3PRmanqa-yAhdS7fog6zluOnjgiohg8fZUz0kDyfeObBd_a0JanGTks4fJL0uquFL1CYsn2wkuxCbfB40ErDaAHQzifarEO5pXfXsvb0iSi0HSCPeCYH3qZ33AemScBAi6GaQ5AJSekhs2wZwbhJ-lNDjNtUUgrBEq3tdNhzAgDkAZ3N7WUFS5dJJIm46dd0savD2BFozrTwkvWisVIFxxbTCiFvJfbTLhVNos-SevE_VUAzC17nUEPSWGCXclg5YbdMNc1OkHPk0RJdmtKXVqV153sf7uP8G0zoXSa8xEY6FODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPcLg_poDIMe4UR4gYOK1m1JJ7lnM4g-E-pr5DBQ-whquRiJuF266nn6gns1wthQ5sVQhWcGNoKwVrDwkUXKrpf27xnMHKY4g8VuFL4M-a_kPw3vna_usu1clWY9_drHEqGWZ8i-8yGWnu_TFyVL8nMAE66Xh9W0qwl4hEEJdjV4GMq4DMAKY8nG0pCoNArg7kf-rNuaZAUplVJQaRw0KgVtaeEQAjAb6gxtnSueXQFWwwtFqvNl_jsmDR2nKhapYzRDJLpr-cy2KxXk6-SYNkmwmr5iMTnlk0O3RNQDLwpCX5mqPU7seo3k53n5rWfoESiXUotrzfUYrxMpOBGmqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=QFFFZC9hdk1WEPlKzNu9xT_x6-jiX7Ylr8WBoXyTRMG2rRR2KYUw5CMq7DDI6qGkaREvalRRxLvaPNJip2Zonk5vSInuchcAYpQ25TokIUeVteL-cTKcc2hAN2eRvBeI0GBTYROEeQ_wlCoI2pAnvyygWM7UP8IEfCzg0jlyUTS2rx3jDzQNGSvNABgH6Qtfiv_cSTYpfxBwl4pKXq_9hHFPaFOES2aomfrB71sCCiTW34Mussu1PtypyhDs7XMZEARQxiC8A3JBptBFEg3697-KWYU_fbU10h2TqFblN7zxuSEyitGZCUhdvz_TkWueIZ6cgR4Krm5Qu3C0MxGIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=QFFFZC9hdk1WEPlKzNu9xT_x6-jiX7Ylr8WBoXyTRMG2rRR2KYUw5CMq7DDI6qGkaREvalRRxLvaPNJip2Zonk5vSInuchcAYpQ25TokIUeVteL-cTKcc2hAN2eRvBeI0GBTYROEeQ_wlCoI2pAnvyygWM7UP8IEfCzg0jlyUTS2rx3jDzQNGSvNABgH6Qtfiv_cSTYpfxBwl4pKXq_9hHFPaFOES2aomfrB71sCCiTW34Mussu1PtypyhDs7XMZEARQxiC8A3JBptBFEg3697-KWYU_fbU10h2TqFblN7zxuSEyitGZCUhdvz_TkWueIZ6cgR4Krm5Qu3C0MxGIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5bbFhpBn8sC5RUQu4kGlbD8tkyS48DkV-hWVjC4H0haPvCfTtYVgWwPJDGhOdeNwGB3ScSg3LiNz0gkMspnBM6HexedkQh41jFgzwUEPVQ_-VZ7f8899fazieo_77Byvbee7WaIe_eu1dKwKJGJMAGb2DKleZZ0L2DCvdW1T-p3epOnr3yvrn3oq6mJ8eal2GQdImSZgtbmkXaGuwWQFu-QV6MN4uY-Wouh5eXb_E6SFMXOGUIHiOjusW2x27u4NzmpF1TwR7xPI9WPc3wHJo0i8Zg9dNauxOniJegBvkBCqwZp_yJ-N9lbuaSLno1eHSMqKMs1ItxV0k4syzB5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly46OtFZ0l23oIGpkHThqAn3Oxf1c0J9b8Rmn5F_96yKo2anddmg3On9S3Q4vOpu4GMnxfv27em-o1Muy85FbAgZhA8MS2O-AMnTc8kt_Uj8L_sHur92RDnwHP4feUPfvqvR8yyQJCzYaz2JPK1riKCQ5rrl7SjLQbLc6xUUqj_K7LlHnTaAv4qQ5IED3g-8Ma8Rh4rY3qAQmnT55wAT0pKDHM9pnr9b4ZDZ3ESw5DAMkGmvVi7lCJbYHHVqq_Wz1-rIwuhbdk9OSurzqvEKuB5-5HULgkNFROXVQMUEOzoGWk83pRebuHcYImzfVli6TGBx1JI1qfIH3m9eCNkU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK-YmMNBmj9BTLBVn9wMaqaUy53CBXc3QGsdbacfVkdgAGvbT3BTYwCi9mo2k4jF7MsKaj0_DPWpVCXNjHF39A88DdM1fL8pf0Nz6wCQGvrPRUWOTm26Q4tlms15HBa3mZzFvg9JOohlA3ISEe3rTTGLIBuxGFD4upWOc0ddaA9VcMQ00sGz6KUuolN6pPzwl9I-QUjv_CSSJnPThNfofZsd8LGVr2gOh9Sn4Qfix7gv7FLzaIgZkk4KMje1Nm9GMD_385iksnyDKrrarhVu5YloqVUfWzy1g3O3MlFKMgoinshrLlyx2sz1KKp93v7g9citmex9WETP89_mSGc3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=INy5_nI6Ug8giDZYFSg8hQ_m3b51VX_qhQbH_RWeiC5xEBy0Qv1H_zgINTxoqi2iHFVt0HZf7JQVk2WaY6wN1BPp7PLdsHTlZmHcia-a8oSjic7UULwR_ZEnphYDiepbpeVGlM8oLCIs9sobIrkof44Qu203rE18SswuPR_tBuz5YbEEQJbRcKhOpLjLtzig8q2pl5kbt03lCCSaYf0rQCQR81ZU19S1Dy9-z7o9Vf2S1vzpT474cdQfS48GloOhIC7PshmZMtMWEQL7mnMgjxo6rjq1gvNG6fKjwpMnDVwNOGn1E01cDpJvmK9Y7ki3VYQ2uo_C_wrFmiwGMhKC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=INy5_nI6Ug8giDZYFSg8hQ_m3b51VX_qhQbH_RWeiC5xEBy0Qv1H_zgINTxoqi2iHFVt0HZf7JQVk2WaY6wN1BPp7PLdsHTlZmHcia-a8oSjic7UULwR_ZEnphYDiepbpeVGlM8oLCIs9sobIrkof44Qu203rE18SswuPR_tBuz5YbEEQJbRcKhOpLjLtzig8q2pl5kbt03lCCSaYf0rQCQR81ZU19S1Dy9-z7o9Vf2S1vzpT474cdQfS48GloOhIC7PshmZMtMWEQL7mnMgjxo6rjq1gvNG6fKjwpMnDVwNOGn1E01cDpJvmK9Y7ki3VYQ2uo_C_wrFmiwGMhKC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R40wZ0fUjy0oBuIKgx2mvOJ0PkGupRoe4vGSfasdUsVPQaKNxpOSbnhT26O0fbfDDTxohpZ_8H2CAOX5oyylLGMc6d6nVIxoNkc-H37-rpQFR9Oqg9m7lYAn44lJlsOeVSB91R_S5WJA4inuOarwTU8HdHnlcgTK8zMXSA_l5gLex3_H7v_6u7Hej5y80j1pnB0fVvW9WLq7icpwq6VlwxfZuflcBYdlQrZUlrRTCJSyYByS0VZ9cTLrdfJHcRwqCuXTNliYrM-X3b7OthJ1yKpv4on-xDyXSkMxH-ACHH2R6fq8527QYRkacC6p10Cop2JRc8GmCWEv42wcNE3AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6FrwEjsB7fKgXl2WJLCi2n-ENGi7ZX9lz_u6Wm2BwJ59k3wvTMJSNYwZ34mxUsY5EIArKsS07UmgERdJnjfZ6pRYHDrjClYn5qi7vCGaVGSbnKotCBtMCiKxrJSpl4v1qpGXX_tDRsdsCGm4yB0j5-ijf9ZhfEZtuBn6fhESJlVINtMb9REuFakPSX8vxDBO6XKG0B-Ux-7JhTjq5t3KXcZ7un3InW0vxqeaskkTLXHL42_xRXXz6YGrDvo73liONHBLKNm3nkIDGLmlw027zjTqV_KiE3zvJdzRgq9bGU4jHJCuOqkGcjyoHAB-KOxV6Iv4BtD1JenedMBW4NTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrDWwHLzwAfpLPvHsCzIn_U5hub-rmaY2RBePra8vXKP_TT6jdRb7Do8SGqdw5rnQlSreSG1DJ6cre4r3IW__bgrBqfMkZh27VWCfP_Wseu9Pin2ughxBsqaeUpfVIJWNJ7CZ5wsSntWJfORTJuDWR0YyMecDAV6CxcfoQBPaz88tX4VY1kukI0a-vVZ4p26YPXDvgZCs-sWPLrQUegZe8_TVMEfTzKrsiyy5gCAjvls_kmvXAEL0N6HeK_r-7bbhg8UHbLmKRIvxgqti2SdcPLmaA0F7UXYqRRVDynukAMCFIw7zEGfOsESWIxTFjIkU9GGM_wxM05Cy9dLppXNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgcalP1RUfvDH4a7KFjvHHsqb1LhLwtBGB5Z-8GGLDkt_zD4JAznOxM0dNs0Ua2w9XEWNvhuppapw-rVLI_CtF-eXgmfvkk1b1IVKNhmTPiMHeG0Jw5xRPJoIsP1Fkswhl-QETwyDq8s0QStE_uOFZsF-rPv1XYd96W3ejk7YoFVmGyVhZTDQsYdu79YtD3PEHoN7eVhhVchUlB4Jstac4_NKSGsefr1Dnjs6npCcOZp6RVoNmbdYWKqOIFtScZc0qWydrtj8R5fVOKl03aSJ3eIaScHmyNnI67iCKp9aAQND6ESkk1ZYEcnp9hZjSeIdSCoR9OWf-Eu-r2AAaSPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ajz0jPDVO5zc8jSnXHcWJCjZP5A6PrvpDQ0HNHDNV95GbQTFBgZeZDFE05_ZAxdwmuf9dcNY9XYPjLJSJ-6p7TJs7UJeXPkzdHAg9p05fO1kDxSbyZ5nSb62iAOcVN1U27nTsiGQ4ZH4nK_A9gnyalyIQF874RMzKU4MFeQubc_FkjnXNJKwWRhWtuH_V3-0gAHRvCGhg1qqMds-6yQRgLlHznP5oNY__F4BcscOVlAuOaPLwNjC3rLWJtYmAfy0lP5kuaJw4FXxNa1kKuEe7ZHwh_KQQRsaL8sYmngyVa8FMPF3FPf4-OYdU0pP6CGlIauAOIk8gqS5omlARNoWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5cHp-wy3MWm_44F648_v-vIlmZsfqM3aCh8FGvmJGyrfPfpfz_O-gYqG1PB4djF0kn_2yYVRWd42z0PlbHXT96du4--yEjYYQ0UHZpCkbsQh3efpAmcbftQ2hXcmVQnBYzleIV9VP_8nNNNFKCk8M7rdJAP1kqOeiKKdcMr6Pb9l-0b9RaItePWBdHA3J5RjMCugII9seG63kz6rA6eqrtM7w1f4xfMQmppnT8anZJWulB2sXoVx8GGcMjcoGTS6U5BT8_LHLHmgvlXKBaqA7O99R-pFTURU4z_TDXqxOKkNxIWhlA4lE9Ona6bsKb39uCOgyiWteEyxAWD3QKLFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifGMsqYOpYiOhrkx7OQwuTGyCIyyh_2IB2OwKnaASD1FVHSQ3E3N93-OWfQ92zs0u3A9pWvCSmhOFJR5RjUvQD1QUTs3JBgwKak9N99VgKYqjOK0eugOr5VYOdnjCq_YwkjW6cYbf06ETyFKKLuzKIaPx7XKvhcCObfMiQ68Kf-OoBDKWM_-01fo-NbTp_qufj40W5xxFSF5GjhiY9hHNq-gI8Cx1HSecokqX6imeOgnR8s1BltWosDQi8xHou07EQX4dK9_oz1lQpvtL6JTRiPf4-PiO2Lh_ZICJWgL5QCowf_92NC3OVTdrWpWVBUMjakHjAbzzq_WDyWw9NPO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=g8zJ8HZeimb8SYhey6PFyuLxzLW2VY81mhR2hZnRGZmHX1atGkiAG-jxB1P_KS4GM5jCxiYdZsp1L0NB7Do4p_Osh_RIXIXO9iF55x832_Nh8drlgrK7Dj1pSKFRUcm-dQmbm4KndKXHHeZvADeCMam58G0zVzpIxPq3mn7Itz3FrEtKc16GrVlhmtekZ-yhVWMIAgpEDdau5oNgkaZnEOAMYfMSsQ2xETsMsPYaa0q7ZpVXXzjqiclIIgcw2J_7pvmTVansMJZiVCGKOB2MhzPBIROJyOdFCRoZT_Yf0liGvlUbE31cNUrwnS-67xrv6aUqV9YWhCj_ypHymA282w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=g8zJ8HZeimb8SYhey6PFyuLxzLW2VY81mhR2hZnRGZmHX1atGkiAG-jxB1P_KS4GM5jCxiYdZsp1L0NB7Do4p_Osh_RIXIXO9iF55x832_Nh8drlgrK7Dj1pSKFRUcm-dQmbm4KndKXHHeZvADeCMam58G0zVzpIxPq3mn7Itz3FrEtKc16GrVlhmtekZ-yhVWMIAgpEDdau5oNgkaZnEOAMYfMSsQ2xETsMsPYaa0q7ZpVXXzjqiclIIgcw2J_7pvmTVansMJZiVCGKOB2MhzPBIROJyOdFCRoZT_Yf0liGvlUbE31cNUrwnS-67xrv6aUqV9YWhCj_ypHymA282w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcCRDO07hCJZ32BVeWOdDQVHR0s1ih1O-Uc4RVPQYqvN2yxbIhcJeLqBtbVMssx9kPUhfbjBBlWu6z1qrt8TEMEALbZ903bM_r3N9COn655kGuI_JrZzJaMUEEwxSCeogPYD3vGCNkkgJRs4lYmw0p9Ej2Vl-lQoR61GtT0nbbY5Ek2Te1vi12zY8HEcRm_E7ePBW9VV0O0os4FJnXuwsbFVbdvDSofqXcANVkTIMzp-VevEdEwYLUP8Xo6DhoOzh2U3xajVEbFi6gN2RKe2B2kS_6lAYxAwfSQOwXbX45XxOkXmzZTMeu0iZFgmpMpU_r91SRbrc7UJ1LRkHUiICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQE1GjS6CuFgcmB5AuRdiDQURGZ5oeJGHQYavMCrC05MIamYpzzJVZndlQJ5xT1JPLylNvdKporNUmT_eIk5krlUKIUyXSJOqgvmroVqDGi4nBpBmKFaGRCfQVlNziPNwiL2DkVF6JECBJC6hTk3JVK1XzeLp4tZhWTFsmvXqKAjzBIqY2m_Fpg1JRSkv1JHrwTrX6WVG2bsuvYiLkXskg8jJoqgpzmM0QuBH3CJnbl41oPP9ske4RayVD6wGRhDhNpDTCEYYmlUidUvBQKz9fZCGB5I57329gpSu4M3awAHMnhCYiraJ-1OWVZLkDR7EoCy6ZpB97gNZWoF05f6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f854N2mQ4V0FKwP8Tv0emHI8h6t3wDSSrH3V3d2IzfMmItLO-sb9uUBSgGbfeMyQYExLOVSdVqRWntTthL-TgOdDUIim4npPY3gxqAkIo26M8fxRcwliWcLOshXNcVR5xiBWApPx2Y08o7qNCKOOXbktIU8K2MRjsstkaH8dT--2o3LDPLcQ24Plz7Ug6mkYKV10WnoQKOG905tRw7OFAcQSPl-4gCp3wwl7G815tdTeTRgzCgHDYpxnvHVdvgxwD4Nejfkrb8e6cMUmbVXpUe1rjX62HEdAyisJSXvhlb0tdrpFzUuZzbVcQigJeURaIrbdqRYtysL929KGP25O6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=DomGvBv_I4E2RI45Frhiy4ZIQuSaV6-AifcvUHKz6qPA_CcRfgXMqIq-biFQR0sAWv6fp2DjP_0qrcPsnIR19ySZ1PZvqQhRaLEx4Hf1ZKNufpXwDXWcYKPmHnLCLnaNMzZj1I58YO55O338SWrSQtVDiUAWS-X9xgeGKqjMgK8IWRLaJcaH6POtA1FgmkY0tyBENEc9Q7HDqGg_UtPHANy1AG1925vLaa1GxaZ3DbcMHb-0dFTKEg-HVfMWfDsFeoKRat5apUJYHZdONJL-YTv1I7sfBSivRLelHQmG4RRy3m-_LwDgOPJZRi6Hk1z0cd84v068EZAUFBwWgyMNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=DomGvBv_I4E2RI45Frhiy4ZIQuSaV6-AifcvUHKz6qPA_CcRfgXMqIq-biFQR0sAWv6fp2DjP_0qrcPsnIR19ySZ1PZvqQhRaLEx4Hf1ZKNufpXwDXWcYKPmHnLCLnaNMzZj1I58YO55O338SWrSQtVDiUAWS-X9xgeGKqjMgK8IWRLaJcaH6POtA1FgmkY0tyBENEc9Q7HDqGg_UtPHANy1AG1925vLaa1GxaZ3DbcMHb-0dFTKEg-HVfMWfDsFeoKRat5apUJYHZdONJL-YTv1I7sfBSivRLelHQmG4RRy3m-_LwDgOPJZRi6Hk1z0cd84v068EZAUFBwWgyMNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGf0nbpYj595-gZWO_mwg4y92YnisSLJ8uEoX8ANUMweuKhP4x1pwGDiW3fpEL1ucm-l_QrXCs9vPpGTyjyJHF9g-0qgK2rormKkBYMaFx--a0pLUHbgPkGFkU9_jw-QXm_2WLS5wLxh3e4yu3B8Sz1nCw7j69Z8_P3m9YCs-FFyobIUamW8uXN0s6x5EI-Y1SumFS6PSdSiXU_426xLcYsMYU0nbfc0QwauE38t6JzH2y4zYmcpKhfAydS3cQXFcvnUXF9tVhCKi_BkEJ3442Ms0l0h3koQ9dZb9JWikcVrkP2Wu53FSCBl7yLEvsyDaMQoI1M0tYm2TfyGuCOHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmMsrPwlYaErqokKxqOzxKZdqZfiLYFRQyd_taXJydIGxo71GOH2ebNd8yD2NFlPNbjYMol8tXzTOrw6MnbI10Mas1hOVRLp0fLH37Ln4KVy94p773Dat8afNd6FDnnSDFek-0UAU5vnP6iXLNCjMGPouNCe20PYtAEjE8n3tA9OUVjo4JU9drl65dZs2nw8zHPWKErAN8kSYq16uzgSnd5pwvEY3BkSrM_UaU7_yDmyBlGrcZjTgf9EA6Ko3CBovor3ibRK_AWGDp2fIsKXzaD-LTChOSLZnnhYwQ_RKHzy6VcvvMMMHAiQqVyovHkZOX18LjSZugDAcjVltTqqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLOKONj0ryW0eYBhgTjpf0RBlSTzUuIS2CvNMHyfd81LOUk4KQjaZK7FYPPvtdMG57HH23O7pzGW-kjPJKsu8MLQAWPQx__xTOy5L3xdabDQcZE4_16mWqabr3Lvp8B7QWQjtxcGWoZN-ReSiMtLTnKcJGLoI8z2r55tMghi3HC7mo_-QYfqDL1dfMCH8Z5FtBUvZv4zTSMbfw7-F8lpAGIMMoNxBoIa9u5IacnyCddZTz_ix1pMfei1kjj-L6fQoAMeRKfOG8rhmQHBlRFAOH-Q7bpUW3hg23HTAmkNaqRYaJAo7tNji7jzCifdvy6413IBsKDQWz-g98YzTXuLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
