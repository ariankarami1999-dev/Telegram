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
<img src="https://cdn4.telesco.pe/file/C2VyBWeKVzNo7REt-WmcqK-x1xN2Od7WKyKsSrUMI20padjJeqkmStE2eDkI77Gbc4H_dntbDxh8gEJ3jQrrvuqyHMGUr52JPOMJM4SCAfMEillDJcrSwObiXkc_ut5OpzNQO0dbL549Jymadu-MJg_A0LZX2PbLdwCrK29gpRMUwH4FSETeHZx5LoQKMCFAMWJZgY0vcHm1DQneoqK4NWR8QQobei4qcfUAH1gNVzabjnylVg9rkeaBCHg2x6pgbYV28vCXhdhZxRzJWlUjgtA2raNVct5J7RavNoJ5JypcGvttLaMBtQiueIa6LiQQA9Q6mYtMkU6jAHHOIIzo0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 00:41:41</div>
<hr>

<div class="tg-post" id="msg-456472">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNL5vanHkMsGntUizANTZgLEwa5BnfHd1bJF7-cflanaUGfnpeteEIpCRhYxzJtw9IgN6Cs0FGArbhSuMB6i_mkaPQEy4nKn_EJUI47utVp5QLGb9escfih260HI3dZm5AO3-iZgW8lI1uxYKUUsgHb31usg_IAFMEzNXBKKrYYrO8rdlQZMbq0j3q1xj79-X3T-7a6o-2kM-_WlE5g5fiULbgs3jXUiYa7Kfzh5RjpFw2PojLIVqGam_Y8sHoANDDFPuXZPsoM5B-pEmCi3eFueZTCAotFV_uNIYmqEEZiAjqkO-kzAkRcZm6zdp2isW99cxyATlGQsSNVYuFjhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پیام منتسب به فرماندۀ هوافضای سپاه جعلی است
🔹
روابط عمومی سپاه اعلام کرد صفحه و پیام صادر شده منتسب به سردار سید مجید موسوی، فرماندۀ نیروی هوافضای سپاه دربارۀ قطر جعلی است.
🔸
تنها صفحات رسمی سردار موسوی در فضای مجازی، در
ویراستی
و
اپ‌اسکرول
می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/farsna/456472" target="_blank">📅 00:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456471">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ادارات مهران و دهلران دوشنبه تعطیل شدند
🔹
با توجه به تداوم موج گرما و افزایش دمای هوا، فعالیت ادارات و دستگاه‌های اجرایی، بانک‌ها به‌جز شعب کشیک و شرکت‌های بیمه در شهرستان‌های مهران و دهلران روز دوشنبه ۲۶ مردادماه تعطیل اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/456471" target="_blank">📅 00:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456470">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab76ea7e7.mp4?token=uP1uPmJkMnpwg5HYDF_HJBqC39rJxBDUKLaHfI0QKTwy-2-7C3vNqZgga7IGMKw4QZXCs5rGW9xb3tPOxqyDkBlAhFOebSZrxzO_4zrBtOyRam51eVvPNz74MO-xDCexyt8gN1FT8pt1neRMGq4w-3sWbKvU3WlHXcPXZeI64_2cgdemaln2ox_kKVJYE1DCZy-OcGGejd9yQF5dRK2wwWJAYO2yqd_LgfAmSoWuWzihrvvtSwtsiiJDHGrAaewERdHKjjWitedfGoqI_HpZyPDhgIXCCqs76u7hMbIhRRoadd9jrToEFBSCStl7Vy2uwD95hSLvOyXEP96rkqH-mZXUcaTyKBbv4CKkDjFwKT4LlIxq8FSA7aH_uF_Nv4OR0AyiSCie4X_3G09x3MyWdQchOkDDgvS9lunwzNZFkMd2jQHZN_8NrdMsm7yzskIhKDWLzXpV-8uRx5dTsL4E4BgW1j1NFG4nyFxGiGWyKrxhT_H7XohLuWKPTYlRFm23eSjdKCBFRukyq8r_kqVBibQt1zQDnMG_I4nbaejTgVh89mHRBue_ueD6CiEaRZmKmLQo5w-3DUv-BrHVu0t-IbDwzeP1h616WX00Wa4zzJsdUzhvgjRD29vLPN0f2x0IJlsUahOinucUzZxnnFmzBYGR8CipTKh1HcOEFt0kqwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab76ea7e7.mp4?token=uP1uPmJkMnpwg5HYDF_HJBqC39rJxBDUKLaHfI0QKTwy-2-7C3vNqZgga7IGMKw4QZXCs5rGW9xb3tPOxqyDkBlAhFOebSZrxzO_4zrBtOyRam51eVvPNz74MO-xDCexyt8gN1FT8pt1neRMGq4w-3sWbKvU3WlHXcPXZeI64_2cgdemaln2ox_kKVJYE1DCZy-OcGGejd9yQF5dRK2wwWJAYO2yqd_LgfAmSoWuWzihrvvtSwtsiiJDHGrAaewERdHKjjWitedfGoqI_HpZyPDhgIXCCqs76u7hMbIhRRoadd9jrToEFBSCStl7Vy2uwD95hSLvOyXEP96rkqH-mZXUcaTyKBbv4CKkDjFwKT4LlIxq8FSA7aH_uF_Nv4OR0AyiSCie4X_3G09x3MyWdQchOkDDgvS9lunwzNZFkMd2jQHZN_8NrdMsm7yzskIhKDWLzXpV-8uRx5dTsL4E4BgW1j1NFG4nyFxGiGWyKrxhT_H7XohLuWKPTYlRFm23eSjdKCBFRukyq8r_kqVBibQt1zQDnMG_I4nbaejTgVh89mHRBue_ueD6CiEaRZmKmLQo5w-3DUv-BrHVu0t-IbDwzeP1h616WX00Wa4zzJsdUzhvgjRD29vLPN0f2x0IJlsUahOinucUzZxnnFmzBYGR8CipTKh1HcOEFt0kqwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغی که پس از ۱۶۹ شب، در کاشمر همچنان روشن است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/456470" target="_blank">📅 23:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456469">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3020d64c47.mp4?token=Br_6T9o8rGo_9ylFLbvFGUSmHFqL_-Sg3Ip5PnYSQ6JSgz_SpbhgUsOv70SlS4-Ns6c36rRV0evDs8GBULTGNwMIRpz2TVL9DNzt1w-tjbM1DHMDC-zBtcU0SvJQSu6nz7MxQWFhGHz5OvDuCK1q1GPs8P-o0jjwXt4lXxG93cBX87v1iviUOT6os8EOQ3eRpuYCkUN3vr6mfJrI-U4jzdVT9xwjIaNkESis7Vdtw92ActLA3RCHvg61tD_dlbjC_8IARt6CEV3_UPuZlvqQl0s0PT-k0D3MhuIr4KeoIVbJ3A8o6dGmX3C8U5qLPgfYMqF9-heQk0TyEd1LaJTkTwZ0JBzM7VE_NRVgZuYt4zU_cDYDCSi_92FhPU8C6CKQqoQfXb2Gk1RnCz6SmElJNJk-BlyQrYhpDdvYZHuZeXDQAg9WEPoYsI4GaagmeP3SenuZlN3W2IhIRwfCrvH9i6T4_L878cBsRJUsMFBStuAZz8VuJJkUrOlgK4HAOSUwgKg6gjXkowdqZTHKcvzNHj01ptl7umqM1fvm_qNQeGHwK_ygaz3M5MZHbaVjamXYJOB8pB20GATC9s-lZHc-cniiBa30WsfCQVgAvSfNVi-qtLvTak7ydU48n7K7uynYdyqW45h2ObI1SlYrBYnChceWtBF_9yPjUV325zH3CUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3020d64c47.mp4?token=Br_6T9o8rGo_9ylFLbvFGUSmHFqL_-Sg3Ip5PnYSQ6JSgz_SpbhgUsOv70SlS4-Ns6c36rRV0evDs8GBULTGNwMIRpz2TVL9DNzt1w-tjbM1DHMDC-zBtcU0SvJQSu6nz7MxQWFhGHz5OvDuCK1q1GPs8P-o0jjwXt4lXxG93cBX87v1iviUOT6os8EOQ3eRpuYCkUN3vr6mfJrI-U4jzdVT9xwjIaNkESis7Vdtw92ActLA3RCHvg61tD_dlbjC_8IARt6CEV3_UPuZlvqQl0s0PT-k0D3MhuIr4KeoIVbJ3A8o6dGmX3C8U5qLPgfYMqF9-heQk0TyEd1LaJTkTwZ0JBzM7VE_NRVgZuYt4zU_cDYDCSi_92FhPU8C6CKQqoQfXb2Gk1RnCz6SmElJNJk-BlyQrYhpDdvYZHuZeXDQAg9WEPoYsI4GaagmeP3SenuZlN3W2IhIRwfCrvH9i6T4_L878cBsRJUsMFBStuAZz8VuJJkUrOlgK4HAOSUwgKg6gjXkowdqZTHKcvzNHj01ptl7umqM1fvm_qNQeGHwK_ygaz3M5MZHbaVjamXYJOB8pB20GATC9s-lZHc-cniiBa30WsfCQVgAvSfNVi-qtLvTak7ydU48n7K7uynYdyqW45h2ObI1SlYrBYnChceWtBF_9yPjUV325zH3CUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع حماسی بروجردی‌ها در ایستگاه ۱۶۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/456469" target="_blank">📅 23:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456468">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96aeabd46f.mp4?token=kdXDBVZfjsiiSrTD9D9FFxh46AyMH160pfj7JCV8X-l2sKszHQegnwdCVumYvzVKkSzlV429Mn5QcJBSxmeJahwTb3GlEJFSyHZ3jaOHrwG_w1aXdj30lynbwDuHfaPcVhFqcCh9OASGFB3hntnzKcQbhdLPeIKNda5gjDjwUlTAVS5pKDtNPZ0qKHo8MICGCFfwUiRF1nW25uCcvIJlreZV9VjCXKj_Ry_NgyOKwPzhx15PBbDAXYkjM2hipxFO3mwwXP7xOaDsKUneE4pBRZJF4aheeDHqZKyvTeT_WuUM96jxSfhYAsjK_XhGmmy5HV4_QcVrCXzj16E-1kN5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96aeabd46f.mp4?token=kdXDBVZfjsiiSrTD9D9FFxh46AyMH160pfj7JCV8X-l2sKszHQegnwdCVumYvzVKkSzlV429Mn5QcJBSxmeJahwTb3GlEJFSyHZ3jaOHrwG_w1aXdj30lynbwDuHfaPcVhFqcCh9OASGFB3hntnzKcQbhdLPeIKNda5gjDjwUlTAVS5pKDtNPZ0qKHo8MICGCFfwUiRF1nW25uCcvIJlreZV9VjCXKj_Ry_NgyOKwPzhx15PBbDAXYkjM2hipxFO3mwwXP7xOaDsKUneE4pBRZJF4aheeDHqZKyvTeT_WuUM96jxSfhYAsjK_XhGmmy5HV4_QcVrCXzj16E-1kN5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌جا پرچم ایران نسل‌به‌نسل می‌چرخد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/456468" target="_blank">📅 23:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456467">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgRXnRXDzBHOkJJrIMBgWwsNM5jiM8Buugsi06UR0jmIVufAJdSf4BfafmdQOFHOzryEVwaGTzgAxT-jXxC0FaQH5WYRuONZg0yVHX6WpsA0JRdXp6YNZeic1x1NqJq6p1EZl3exCYnXpW5UXdeclHC0zuMi1y-EsrLXoOHuKNCp_TeW7Sx1V0PDj_CLFijXP-kbUS2UFIUqyn0Q3BAxHCBo3ilpMfKs0ECEF6S0oBo9GeOy1fOUn3ONOx2MkqfY8knwTzw9vikcY9yACvEUFy6EDOQ1hEPDVS_6_JqrQka13JAXlzAR8qHQmIQ-ZH87Y96YMQoASostxDk8T2Ar2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصمیم تازهٔ جهاد کشاورزی؛ شالی‌کوب‌ها برنده، کشاورزان بازنده
🔹
حسین جعفری، رئیس اصناف کشاورزی گیلان، با انتقاد از اعلام نرخ جدید خدمات شالی‌کوبی گفت: نرخ تبدیل شلتوک به برنج ۲.۵ برابر شده، در حالی که این نرخ بدون برگزاری جلسه با نمایندگان کشاورزان و برخلاف روال سال‌های گذشته اعلام شده است. به گفته وی، افزایش هزینه‌های تولید از جمله رشد ۶۰۰ درصدی قیمت برخی کودهای فسفاته و پتاسه، فشار مضاعفی بر کشاورزان وارد کرده است.
🔹
جعفری همچنین نسبت به لغو ممنوعیت واردات برنج در فصل برداشت هشدار داد و گفت این تصمیم می‌تواند بازار محصول داخلی را با مشکل مواجه کند. رئیس اصناف کشاورزی گیلان خواستار بازنگری کارشناسی در نرخ شالی‌کوبی و مشارکت واقعی تشکل‌های کشاورزی در تصمیم‌گیری‌ها شد و تأکید کرد: حمایت از تولید و امنیت غذایی بدون شنیدن صدای کشاورزان امکان‌پذیر نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/456467" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456466">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495006eb5.mp4?token=hp0-1otbkvo345t0Z3z_aCwQh6_vATvxKg7H11MNsPdttr-jc-0UWN5xTrXQsmgMxonvwHQ5dkXt6vH___9iaK187qi01h8ksS0zNsAyUzaSbhJwrJB0yMq6Jk7sL4j73LZvcmANUXN6lM3MDjMjVriOMxrpDn9KUWSCk9WPGyTxyh6Lxdn0BcyvA7AKFsP_VitNfG-mFfd2cZx7CjqTNXSfEgL8t4DSqdtVY-V5jXAXRN165oUqOqEWAD11l63e7BazWqy1_atwgXyFrwnuaWwFHFDye3tXo5xZFWmpPq3E0ge7zf6grh6Q3mDsh8XWsecg8lkK4JGE2MRrczD73395PVbS7WaqHl1W5mEBAM74nYXFXxXHfFBVXWkrtMgGoPCyIrW4ejytuj39Cdc9mCUCAfU2r8lBUhIA16EhRlc8rVAn9HtxlK38kH-cB4MDr_zdftvkVxfIDRvrbH8PLTBCoO7kfMytGLxaeyKHWd_nx4ZRM-Iw_zhqDuN91tHhshicJb4A1kMl7_GSKZUIudcUM1AQSkop12Smv9ETugS7ZYiz8cEIOxcwVKiy3mdguTkZVkG07Lr6y8NsXx6uwEVmcJrdfM-Za1T11XKf1tT3N0r-OjMKbPhdYc6QGVqVQMg5doccRWGRkVuPa_WjvhlT3ymoFi8-SRNEFbX1YR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495006eb5.mp4?token=hp0-1otbkvo345t0Z3z_aCwQh6_vATvxKg7H11MNsPdttr-jc-0UWN5xTrXQsmgMxonvwHQ5dkXt6vH___9iaK187qi01h8ksS0zNsAyUzaSbhJwrJB0yMq6Jk7sL4j73LZvcmANUXN6lM3MDjMjVriOMxrpDn9KUWSCk9WPGyTxyh6Lxdn0BcyvA7AKFsP_VitNfG-mFfd2cZx7CjqTNXSfEgL8t4DSqdtVY-V5jXAXRN165oUqOqEWAD11l63e7BazWqy1_atwgXyFrwnuaWwFHFDye3tXo5xZFWmpPq3E0ge7zf6grh6Q3mDsh8XWsecg8lkK4JGE2MRrczD73395PVbS7WaqHl1W5mEBAM74nYXFXxXHfFBVXWkrtMgGoPCyIrW4ejytuj39Cdc9mCUCAfU2r8lBUhIA16EhRlc8rVAn9HtxlK38kH-cB4MDr_zdftvkVxfIDRvrbH8PLTBCoO7kfMytGLxaeyKHWd_nx4ZRM-Iw_zhqDuN91tHhshicJb4A1kMl7_GSKZUIudcUM1AQSkop12Smv9ETugS7ZYiz8cEIOxcwVKiy3mdguTkZVkG07Lr6y8NsXx6uwEVmcJrdfM-Za1T11XKf1tT3N0r-OjMKbPhdYc6QGVqVQMg5doccRWGRkVuPa_WjvhlT3ymoFi8-SRNEFbX1YR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خروش مردم شهرکرد در شب ۱۶۹ از تجمعات مردمی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/456466" target="_blank">📅 23:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456465">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c983a49c01.mp4?token=NLrQOpvqeJI_AIlXpLykg02TJZ8PwK2KfkV8qOGy9wmXAanvRHXJgob_9JNIWvwE8NK5kkEtafqFzGiSkA8kKfoob5EOgxE6ClTluzvNogOSBrMBy2kJVERsjrfS6JFPfM07TRKkMWwAabuRmur-5sQDI4_3uFPDnTsrKVNLLjIINdFAMwHLm5kTbH8SEhxyrkBlZLk8iev0b3aeV-ZFkEVvPZxU-wLFzyy9suay9N3Mhnsb8AQK8vKR7QtEWmItlI-5WEPT7Pe5Gyp1Hn240EgFRfDyPa72cDrrhBqH_wb8xFvgGmOQs7niMhMcne03P9reBVQLygNnOV4dBmFm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c983a49c01.mp4?token=NLrQOpvqeJI_AIlXpLykg02TJZ8PwK2KfkV8qOGy9wmXAanvRHXJgob_9JNIWvwE8NK5kkEtafqFzGiSkA8kKfoob5EOgxE6ClTluzvNogOSBrMBy2kJVERsjrfS6JFPfM07TRKkMWwAabuRmur-5sQDI4_3uFPDnTsrKVNLLjIINdFAMwHLm5kTbH8SEhxyrkBlZLk8iev0b3aeV-ZFkEVvPZxU-wLFzyy9suay9N3Mhnsb8AQK8vKR7QtEWmItlI-5WEPT7Pe5Gyp1Hn240EgFRfDyPa72cDrrhBqH_wb8xFvgGmOQs7niMhMcne03P9reBVQLygNnOV4dBmFm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
🔹
سردار جوانی: نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🔹
آغازگر…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/456465" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4d930c6e.mp4?token=aDCKh5NhKwtwMUz1fZAorRBF636v_hYPreTbv_qRU5FgfKtHzycH_1-QmeWPj2YhFUcix2X_Ae3uv0HBIE1xayFpMFq_S5Dwv85eqgqp0AESVLllMn3Q3vpCcruf5xJ1xWMISmAnPWUT0MkqUVti2EyeYJKZcb4zXxpbiFjqjnbelrPVrvS_AAk5ySlnsY5GZnMe0oFELpo5Xlz2XFkZpaQd7DKn_5kJqg4sTk3wETafYMdgVaaUWHLsw-IvjCu17FLn_F-pc4Pfw7-P26NIxMN0ahnxYwBFpPz3NIdEVNi6GvVMYEjSV9BO0rXgY6dv_2FHc_bIuHVmTjcrET2ERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4d930c6e.mp4?token=aDCKh5NhKwtwMUz1fZAorRBF636v_hYPreTbv_qRU5FgfKtHzycH_1-QmeWPj2YhFUcix2X_Ae3uv0HBIE1xayFpMFq_S5Dwv85eqgqp0AESVLllMn3Q3vpCcruf5xJ1xWMISmAnPWUT0MkqUVti2EyeYJKZcb4zXxpbiFjqjnbelrPVrvS_AAk5ySlnsY5GZnMe0oFELpo5Xlz2XFkZpaQd7DKn_5kJqg4sTk3wETafYMdgVaaUWHLsw-IvjCu17FLn_F-pc4Pfw7-P26NIxMN0ahnxYwBFpPz3NIdEVNi6GvVMYEjSV9BO0rXgY6dv_2FHc_bIuHVmTjcrET2ERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
آمریکا و اسرائیل با ۹ هدف مشخص به ما حمله کردند اما به هیچ‌کدام از اهداف خود در هیچ سطحی دسترسی پیدا نکردند، این بزرگ‌ترین پیروزی بزرگی برای ما بود.
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/456464" target="_blank">📅 23:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f51655b2.mp4?token=ZMqReO3FMNxM-qeC0eD0O0QELjncPgSSkGwVcQ6yg5sIEJConSCHpohaLa5gncbs6X6D9NcODl2xjdhraIa2LoaPrCREcE6Xt7QhC5qFxDCh6Nf59zgmvM_zISxbWawjkSqVWfABnc2zx1BO7nNlODbWM7lJCAicADokgUSW-D4oQmgU2v2xgvsFIHO0dIRLLhuYAptbDhicSYhPb1NgIIzTHLzDm-2jKcbYvmMlDOyi6vntGUz41Kf3v78__5QM8I9CYAvokjtKeHay2Ce0sn_UQpd1AaZcyaWgBoXUy5-CIvgf6YmyWOiTN4xYyJ8w8-sxxWJwxu9ws8edgl7iEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f51655b2.mp4?token=ZMqReO3FMNxM-qeC0eD0O0QELjncPgSSkGwVcQ6yg5sIEJConSCHpohaLa5gncbs6X6D9NcODl2xjdhraIa2LoaPrCREcE6Xt7QhC5qFxDCh6Nf59zgmvM_zISxbWawjkSqVWfABnc2zx1BO7nNlODbWM7lJCAicADokgUSW-D4oQmgU2v2xgvsFIHO0dIRLLhuYAptbDhicSYhPb1NgIIzTHLzDm-2jKcbYvmMlDOyi6vntGUz41Kf3v78__5QM8I9CYAvokjtKeHay2Ce0sn_UQpd1AaZcyaWgBoXUy5-CIvgf6YmyWOiTN4xYyJ8w8-sxxWJwxu9ws8edgl7iEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
🔹
سردار جوانی: نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🔹
آغازگر جنگ دشمن بوده و اقدامات ایران جنبه تدافعی دارد، هرچند ممکن است در آینده جنبهٔ تهاجمی نیز پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/456463" target="_blank">📅 22:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b5f96c1a.mp4?token=fdVSFwQsEzTmXHBqk7lSLPwNAP8GzY0KDYOXLqmZoODDESUErJ0toswgWAfvWlh_Rw3UIkoD1-fm-GZ3cw_RLIHOYy_gJgXwTTCu9TpzFwcMrnJttV-sEdcqTGlw9Ay2XqwUpA43azdDZAxoKcckREwZ1M4Mk5y3JRk_bm-2qEkvyNUAvexGfrxBoDpq1albsYaqj1uoEUYdA8fVCmtEy5yHe5rMfSZm9n1CHMd2Bggz2hgHMc3VAqDRd7WiAkuceUg4n_pRgJV6Y7-pEaD2Mi3r_bsHOseFC2VYdEa7ioCuRG3rknvQmHAue3BF77vHC3EIaik28fhRV_l87Y5S5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b5f96c1a.mp4?token=fdVSFwQsEzTmXHBqk7lSLPwNAP8GzY0KDYOXLqmZoODDESUErJ0toswgWAfvWlh_Rw3UIkoD1-fm-GZ3cw_RLIHOYy_gJgXwTTCu9TpzFwcMrnJttV-sEdcqTGlw9Ay2XqwUpA43azdDZAxoKcckREwZ1M4Mk5y3JRk_bm-2qEkvyNUAvexGfrxBoDpq1albsYaqj1uoEUYdA8fVCmtEy5yHe5rMfSZm9n1CHMd2Bggz2hgHMc3VAqDRd7WiAkuceUg4n_pRgJV6Y7-pEaD2Mi3r_bsHOseFC2VYdEa7ioCuRG3rknvQmHAue3BF77vHC3EIaik28fhRV_l87Y5S5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم  @Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/456462" target="_blank">📅 22:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f90307c.mp4?token=i_ttDSlpNeNLU6gxm8ElqcETItHj5c8SuU3okRDeDjQbvjOLcN137lyUpXAv2IYIo6dvGp_EOVAuAoJjPiH_mpgAMYKijO_MBxqNPAf_cafYtIGO6Zf7o7PXAQbisWMq0dwhQmutgF67gtKoqQq2OLnxPSG_NtTtQjtW4_hxkLma5k9VHFCRqVdPxBn5u4_C8sjjI5sTZJIvO3_JZioqDGuZgcLoEnVzzv9Vuf1R2bXAoFWaw7WkZLJVOtR7-IVvJqPq0GCkLYAq-dHRTDFUNC7na8yZsZpPjTRLupMkxtxatMkEBsWVlis8dNfN5M2WYzOk_tnJ8ZJTMhpHorsPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f90307c.mp4?token=i_ttDSlpNeNLU6gxm8ElqcETItHj5c8SuU3okRDeDjQbvjOLcN137lyUpXAv2IYIo6dvGp_EOVAuAoJjPiH_mpgAMYKijO_MBxqNPAf_cafYtIGO6Zf7o7PXAQbisWMq0dwhQmutgF67gtKoqQq2OLnxPSG_NtTtQjtW4_hxkLma5k9VHFCRqVdPxBn5u4_C8sjjI5sTZJIvO3_JZioqDGuZgcLoEnVzzv9Vuf1R2bXAoFWaw7WkZLJVOtR7-IVvJqPq0GCkLYAq-dHRTDFUNC7na8yZsZpPjTRLupMkxtxatMkEBsWVlis8dNfN5M2WYzOk_tnJ8ZJTMhpHorsPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند  @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/456461" target="_blank">📅 22:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=o83ZFXGdna5qtu-9P5PdsZ3EB2t0eJocyMQo_KvFXC-Q92zW-F4yGn_aCY4PLeMidbn-UOoUrznZ58rXfqI1ocWHk83Uicyv3SNFlMLpaeA5xIK76VKfUnajKJcW6qNQMUWiCiaCmZQWpL_mncLbi5npR8L5RfUVyTwccbYAp1P9I93hiyJdcJRjWR0tyI98KWo6OjWTYEBUH88IXx-gBN85X4mPDDaH-8UckbqYIAdhgYbaV3loySh9J2WTuGFiCqx0Gq-vIkymFJqk4kN1pROiF7jBhpam3jMwrkoSIGiLfR9LJaEcrvnKb7KW5vZtj7IEl28DyEczHARlY2rvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=o83ZFXGdna5qtu-9P5PdsZ3EB2t0eJocyMQo_KvFXC-Q92zW-F4yGn_aCY4PLeMidbn-UOoUrznZ58rXfqI1ocWHk83Uicyv3SNFlMLpaeA5xIK76VKfUnajKJcW6qNQMUWiCiaCmZQWpL_mncLbi5npR8L5RfUVyTwccbYAp1P9I93hiyJdcJRjWR0tyI98KWo6OjWTYEBUH88IXx-gBN85X4mPDDaH-8UckbqYIAdhgYbaV3loySh9J2WTuGFiCqx0Gq-vIkymFJqk4kN1pROiF7jBhpam3jMwrkoSIGiLfR9LJaEcrvnKb7KW5vZtj7IEl28DyEczHARlY2rvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/456460" target="_blank">📅 22:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4834b23901.mp4?token=e86EQ1bKvuKwHaCzSaDl2Tky3Y5orWSOALqfsO8LnaIgzzOSRkykyiv_pCFy0cF0olcSrlPcS5CXtUUAaEQrvbdPHV6tc8M1m7OQmFOwfPFYNarHm469ELjHSCA8V1EgsD-fyvRTQaDWHmkYcIyFG-D9_eN8NC-hcCqUpuBV6DBIao2FH8wtYxAqKc9fJzEzS1SeDZk-47Fh4L3P_I0YYD4VA3_pftYaTt3AMxSuQaDRfcyhUnssT9Rl47iyeQnq7xnuGxnhMZ0S940l2h_aAjfEY5UVoxXk5JgRczqmYBxuCpvAjBQNJ8OsBT9sxpQDuf-G8myaCaGPvvXL9-v0tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4834b23901.mp4?token=e86EQ1bKvuKwHaCzSaDl2Tky3Y5orWSOALqfsO8LnaIgzzOSRkykyiv_pCFy0cF0olcSrlPcS5CXtUUAaEQrvbdPHV6tc8M1m7OQmFOwfPFYNarHm469ELjHSCA8V1EgsD-fyvRTQaDWHmkYcIyFG-D9_eN8NC-hcCqUpuBV6DBIao2FH8wtYxAqKc9fJzEzS1SeDZk-47Fh4L3P_I0YYD4VA3_pftYaTt3AMxSuQaDRfcyhUnssT9Rl47iyeQnq7xnuGxnhMZ0S940l2h_aAjfEY5UVoxXk5JgRczqmYBxuCpvAjBQNJ8OsBT9sxpQDuf-G8myaCaGPvvXL9-v0tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بروجن از زمان‌ قطعی برق گلایه دارند؛ برق این شهر شب‌ها قطع می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/456459" target="_blank">📅 22:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9413808a20.mp4?token=pCZPKzr2TQHn5e1KVq_AHx--F59HZIyjdMH004XznHCgM_SdTLIh1ux6Jy2ztiPGI7xkl9jSohMIo190bpcwuA2rnI8JEPOHnNGMWLYsNy2MI0P_XsYP4ycrwF_IOODewm2XdLQ2zFYXPdblqx0BDWolviBY9zO8kIdxQarLTRhUne159XrzcgVuVOFHGXkpNSzRoTR2NxCa_IkJtH6a0fTHFqA3PySwTIQ7ZKCiGuoAPyKaSi-Z7Qmao1yHwDTs12d5FzdJ4c21mO_cj59-DQ60vEidly6AvWLs0m56RvlPjqU5tUzLO5acrAnW1P9VCtxlkD2_Wq3-4ssjxH4p9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9413808a20.mp4?token=pCZPKzr2TQHn5e1KVq_AHx--F59HZIyjdMH004XznHCgM_SdTLIh1ux6Jy2ztiPGI7xkl9jSohMIo190bpcwuA2rnI8JEPOHnNGMWLYsNy2MI0P_XsYP4ycrwF_IOODewm2XdLQ2zFYXPdblqx0BDWolviBY9zO8kIdxQarLTRhUne159XrzcgVuVOFHGXkpNSzRoTR2NxCa_IkJtH6a0fTHFqA3PySwTIQ7ZKCiGuoAPyKaSi-Z7Qmao1yHwDTs12d5FzdJ4c21mO_cj59-DQ60vEidly6AvWLs0m56RvlPjqU5tUzLO5acrAnW1P9VCtxlkD2_Wq3-4ssjxH4p9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم مراغه در ۱۶۹ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/456458" target="_blank">📅 22:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456457">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737a9ae067.mp4?token=v_LW1ERlk9KjgqqwBu5Y2HvcLegukS49w-d2lsshW8ax1ved6bGzLi6vd6rop9664ORCZjQEk1aQ0Iy8g4mIov88bVIZsSZPnS_aDhOCueV4tNfE6s87DKS8fNUst6LFGWBF6dL8a4wO9ImCigQ94LzcdvlGf781vVR_nscOLMa-vrfBpldao0uR8oPC9C6rj9jk-HHBPtf2lIeeUBSB9lsuL5TAb2FuWqPZoVwiI2ILIGliDbjbbTtJse6risnLjq2-YMNg3pTyz0on-EFiMGmxUrF5OuZ5nepxou9BSSiy-sv2L_a_ONrLr3gi-4O7wtVEQlgeUDMD6a1Ew_RvFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737a9ae067.mp4?token=v_LW1ERlk9KjgqqwBu5Y2HvcLegukS49w-d2lsshW8ax1ved6bGzLi6vd6rop9664ORCZjQEk1aQ0Iy8g4mIov88bVIZsSZPnS_aDhOCueV4tNfE6s87DKS8fNUst6LFGWBF6dL8a4wO9ImCigQ94LzcdvlGf781vVR_nscOLMa-vrfBpldao0uR8oPC9C6rj9jk-HHBPtf2lIeeUBSB9lsuL5TAb2FuWqPZoVwiI2ILIGliDbjbbTtJse6risnLjq2-YMNg3pTyz0on-EFiMGmxUrF5OuZ5nepxou9BSSiy-sv2L_a_ONrLr3gi-4O7wtVEQlgeUDMD6a1Ew_RvFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت امدادگر هلال احمر از آخرین لحظات یک شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/456457" target="_blank">📅 22:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456456">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fc7d771a.mp4?token=rsFY7qz_7CF94ztb-qWyr93se0riV6-ywDJzRZS7N1FpsUfJ1wCP_TgFor7jiVUeTmvaoKHxYeNKdFKxdowhKrl0CCVgDEhWjiA7UVV8EZ0Ib9JTDmjYQNremUCtKLNVhcjxgVH4kGXnhqKWPeD4uYyQH16AQjQhkXmRarg0TPg9KS5LtEbCSyB0lZfHGuaO_FN5UQm48JIyxMpjc42uJZvlhX5ZQi6WiUNnqGe_pJFyYwHRczh_ME3wPrjV4aEqvwDDLFmpSwdIgOATT7hFFZ0TJTvtG8Y2XSSxOky-rMHaXwwhsCdlJf6INw_kBfYndlWeUN9k0OpvNiHU9KZKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fc7d771a.mp4?token=rsFY7qz_7CF94ztb-qWyr93se0riV6-ywDJzRZS7N1FpsUfJ1wCP_TgFor7jiVUeTmvaoKHxYeNKdFKxdowhKrl0CCVgDEhWjiA7UVV8EZ0Ib9JTDmjYQNremUCtKLNVhcjxgVH4kGXnhqKWPeD4uYyQH16AQjQhkXmRarg0TPg9KS5LtEbCSyB0lZfHGuaO_FN5UQm48JIyxMpjc42uJZvlhX5ZQi6WiUNnqGe_pJFyYwHRczh_ME3wPrjV4aEqvwDDLFmpSwdIgOATT7hFFZ0TJTvtG8Y2XSSxOky-rMHaXwwhsCdlJf6INw_kBfYndlWeUN9k0OpvNiHU9KZKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۱۶۹ دست از حضور در میدان نکشیدند
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/456456" target="_blank">📅 22:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=ZEFt8b41NlFO3SV7_eZwLsFaDmU4P2Kc-UQBC3TH36xBrbU5YEU2B0ptE6Zy0Q664seLL9Givfsx6h5sYKb_4W7SaulBiy-c-jl-4YFiKW15Q3NolOJPfGXtl7lS4gVwx6YTpUX5L_Qn-YFTFzXEK_-5bVBdPSnS8FUV2VdoZ8mcPH7kJyszdyPQJL6Ym0UqF57CWXy-TLC-km0ea9DCjXilSSSNhWBqtPTvSUdaj8j8OscBiO2o6Y788ubI9YYycz-h79xYOQ31LQw15ywgyN9aVuQjLRGIMqs6CHv9m8y21LTLwxqLN4ooKcNJ6L-JUDSWgBCdmK7YY6Fov7lN1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=ZEFt8b41NlFO3SV7_eZwLsFaDmU4P2Kc-UQBC3TH36xBrbU5YEU2B0ptE6Zy0Q664seLL9Givfsx6h5sYKb_4W7SaulBiy-c-jl-4YFiKW15Q3NolOJPfGXtl7lS4gVwx6YTpUX5L_Qn-YFTFzXEK_-5bVBdPSnS8FUV2VdoZ8mcPH7kJyszdyPQJL6Ym0UqF57CWXy-TLC-km0ea9DCjXilSSSNhWBqtPTvSUdaj8j8OscBiO2o6Y788ubI9YYycz-h79xYOQ31LQw15ywgyN9aVuQjLRGIMqs6CHv9m8y21LTLwxqLN4ooKcNJ6L-JUDSWgBCdmK7YY6Fov7lN1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌کل بانک مرکزی برای دیدار با مقامات بانکی و اقتصادی عراق راهی این کشور شد.  عکس: فرج صمدی @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/456455" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۲.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/456454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۱.pdf</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/456454" target="_blank">📅 21:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bc46a7f5.mp4?token=F2XtIfSdXDt8stswqzTjc3Sy949wZJbUSdS5pDPu9olwvem-EzilLOcJFBs7ZLsUE5g9BEE62f-jtLcLcruZMTbcWwGqmMSLI8Vu6LafgvyFVAWj-lg4Ot7MNFpeOHE_KnDGmtIkUna8_aFOwVoxwsfne5p1_WLf9vVsJFTiMhkJFvIaAPixfsrcUh37SqnhN0jf-CPc3fbcQguiAma3-zkb0rUV501jkjtKswcVc7lsBKxOSx0foQDvEGK7UAx6I0bZmN77TJgaCKegZ1Zu5aKMW26_nq5yLe1Um7Z1TFCCDDKiFLx5rSkH_dFMtTKtBf4PmX5IhDV5i1olHYrleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bc46a7f5.mp4?token=F2XtIfSdXDt8stswqzTjc3Sy949wZJbUSdS5pDPu9olwvem-EzilLOcJFBs7ZLsUE5g9BEE62f-jtLcLcruZMTbcWwGqmMSLI8Vu6LafgvyFVAWj-lg4Ot7MNFpeOHE_KnDGmtIkUna8_aFOwVoxwsfne5p1_WLf9vVsJFTiMhkJFvIaAPixfsrcUh37SqnhN0jf-CPc3fbcQguiAma3-zkb0rUV501jkjtKswcVc7lsBKxOSx0foQDvEGK7UAx6I0bZmN77TJgaCKegZ1Zu5aKMW26_nq5yLe1Um7Z1TFCCDDKiFLx5rSkH_dFMtTKtBf4PmX5IhDV5i1olHYrleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا به یزد می‌گویند شهر «قنات، قنوت و قناعت»؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/456453" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cf671962.mp4?token=l928pUmFTBahpXF8CwT6aDaGCdKmyD3WiE56wmcoDOYcI7lNT84zcy3KsmzriUsGj2j4qS30xA_70l_1UQPnFd86il4ayJjiT-nxpexUyOe31wZcvqhBiKIxtGuaMjLvofYYI31gsDFCxKpCOlQQgmE71jBiw016m7VG6gFkpMCxdVUujQakDacxWj77xSmujMpRXBmIxN_KH9t_TKb6507VeRe-6perQtnxj28o_HgVoO7P9XFbjOFgc82i5JAkgJ1MmsnNeGbs-XmstwACPlWSIZlhUdwoEir8Hd2QjW5iktZJnRUWpcqe-QuuzLBAtjbfMx_eAyflkyg6pvqtZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cf671962.mp4?token=l928pUmFTBahpXF8CwT6aDaGCdKmyD3WiE56wmcoDOYcI7lNT84zcy3KsmzriUsGj2j4qS30xA_70l_1UQPnFd86il4ayJjiT-nxpexUyOe31wZcvqhBiKIxtGuaMjLvofYYI31gsDFCxKpCOlQQgmE71jBiw016m7VG6gFkpMCxdVUujQakDacxWj77xSmujMpRXBmIxN_KH9t_TKb6507VeRe-6perQtnxj28o_HgVoO7P9XFbjOFgc82i5JAkgJ1MmsnNeGbs-XmstwACPlWSIZlhUdwoEir8Hd2QjW5iktZJnRUWpcqe-QuuzLBAtjbfMx_eAyflkyg6pvqtZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید استاندار چهارمحال‌وبختیاری از دفتر خبرگزاری فارس در شهرکرد
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/456452" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=YbKm6YROCq1rFP5CstCFbV0cHmAF88FQMT_fHko6ajN7s-zBl7QlcCNHVIvCOqK9vOOGt7XlEard_NriF3av6KZpVQS57uOifzDtZRks_FL0rcuUKYORo-q0AWmJJDJzZRYdUqFi1LYbhrcMUoA-hm-diV6t0PMITsxTv57Q83My5RNtoU6JoXAcEaJRu5GL-OYIawSk36sRIJNGJYbj57hLm_lrPf8ctcax84SrD75BnXN1042HJir-sf9NVQ9eySOjK_dIhssVO4YUWxP4u8pao3qvJi40xPqguXF2XPD5IefTo-jRG6ciUHazVq1GC4RhdW6Sr4dV7EEymlkt0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=YbKm6YROCq1rFP5CstCFbV0cHmAF88FQMT_fHko6ajN7s-zBl7QlcCNHVIvCOqK9vOOGt7XlEard_NriF3av6KZpVQS57uOifzDtZRks_FL0rcuUKYORo-q0AWmJJDJzZRYdUqFi1LYbhrcMUoA-hm-diV6t0PMITsxTv57Q83My5RNtoU6JoXAcEaJRu5GL-OYIawSk36sRIJNGJYbj57hLm_lrPf8ctcax84SrD75BnXN1042HJir-sf9NVQ9eySOjK_dIhssVO4YUWxP4u8pao3qvJi40xPqguXF2XPD5IefTo-jRG6ciUHazVq1GC4RhdW6Sr4dV7EEymlkt0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جوانی که با دست‌سازه‌هایش یاد شهدای کودک و نوجوان جنگ را زنده نگه‌می‌دارد
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/456451" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy19dcC2BRIn6canE1JOd_Az25hF_98GeO3YQoF6SlzyHmPWoJ2fqijIL7V8q-6Gh4iZiQ1BCFyAL41YgnFGIDckkkuUwJf6h6jXIv0zKqDsPq44Yayg3mo06seeb9QbV-kPOTud2V0sXDVIf6P_93KNdbl64gahhgv1vSFJw9-Elj4AYw1T5E-V9Jl9T5L1R-c7GHeqZ_FK2gwS1oD5Tm5XRE84KndJwR-_Q0BXHeZp_HRzYF-P77m4Qs-Z0CiuK1UjF_POXdzfkYBcGPieIhOQ6cFxWhYJLO1V7mDiDVorDU6WHiflZUiFghRq_wMnXpkBb5QWEaqCW3U7h_Y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تثبیت جایگاه کنترلی تاپیکو در پالایشگاه ستاره خلیج‌فارس
✅
درخشش ستاره در کهکشان تاپیکو
🔸
شرکت نفت ستاره خلیج‌فارس به عنوان بزرگترین پالایشگاه میعانات گازی جهان، با تولید روزانه حدود ۴۵ میلیون لیتر بنزین و تأمین بیش از ۲۰ درصد از نیاز سوخت کشور، فراتر از یک مجتمع عظیم صنعتی، شاهرگ حیاتی امنیت انرژی و تاب‌آوری اقتصادی ایران محسوب می‌شود. مجمع عمومی این شرکت برای بررسی عملکرد سال مالی منتهی به ۲۹ اسفند ۱۴۰۴، تنها صحنه ثبت رکوردهای بی‌سابقه مالی نبود، بلکه نقطه عطفی در معماری حاکمیت شرکتی آن به شمار می‌رفت. در این رویداد، هلدینگ تاپیکو با تثبیت جایگاه خود به عنوان سهامدار اصلی و کنترلی، رسماً سکان کنترل این مجموعه راهبردی را در دست گرفت. این تحول مهم ساختاری و جهش اقتصادی را می‌توان در چند  پرده از اقتدار مدیریتی و شفافیت مالی تا ارزش‌آفرینی پایدار مرور کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/456450" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456445">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBLkZWX5IWBPJzwLsA4nrZ8zOJOAl-t2TKdu1KACwDO4zns2oR6xNCiurHYvNbRY0861mRuo54fENzlUHEizPxIXgxJ6cshvIfjSBLOTrZU1RvigdcVotQLyVXketSpUD-D_FH062HTgCQw0nWjmcpKpf2JV4eUwhl3NuiEmH2fo1pD52RmlQa1dhZxA6KlokonBbTJUU5Gd7IMrQhVAlnT4Y2z3sGcKCScNDWfgqbdI_VEMyDswIH9Bk2hhrF1E-3uAjRxNWsAa1N-SRa5q9tCxuXzJXO4xiT05qAYc7OsF9vgbwny-jI65SchykmJFwVcpcPN9e8PN6Cy2Eikk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXtkwb-NYSt6muSPAp1Y46cu_5wR6ZRrabuRqu7FIsmM_t3jMtuA0DHCg075BAJWCntiGqB1fmpB3Dd0QjS9wNvfBAIADkvHvhwEpBKUeC0ucPSnI9_tqOaklHqDnpybroUMTbETcsq7dDHfzooTIgkZFzaopc9AjmSRDQ-4SPx6uMAup6pB6IyWf4tFBtParl4AI1ffD97m5iMwUv0OHHS825pqYRS1hx2SueDsCHZpHFr6mj6_YBzFIPjt6LC-gKJDBBx0yvIhDkpY8wdDV-N1aJ6bB0y6aUgrAnQH7HvsFOmqLdS-V_eVrNHpzTbygIy-Pn0mDj_rVkdLV7KiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWVLj8FlQJ6qPUnPvSPacJdBljYL7OxHacJewEfi2G2gW1e1ooB1hWRfxQdUoGLoTF2xfzoFtiHZDUkW1rgVa1C66lIUpT60AU6zLOJwSxX-2-coCBMMZwZ4nn037fnfV8633KdkqdI0SCM6o7u4BKFC3wvBMqDGk-HaERyretxprW9kKehQsxO9EHw2cWZ9_qr-0sFPds02NxEWcswjkrA5HYMyJT606ih7rghCNKkaFMEaYKITEZC9SfXcDrxFaQW_uDLB5jPFD3VqRhQuULQHMX3Te5ZdIDH2OCD0PLwCRYQZ3I5xnC-ZtGPCfgb7rr_Cxub05vN3goqkIchm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlZyxZfi8LhBMop5tIJWrGPjqQMWzk71Vl06kf9jLiu-oSqfVybHisrHFAMpMNkRrU_ej5XNGUYNv9BsE0cCXU2vycM65BX_ydWB664v_KGfVy3GjXsmxCRk0giMDyDi_IVZAcTsrMRiYFHpifSS8P5hMH9grFhZoyGR3BeouQCehDR0J7xvNOyLxjZbPYlbpbPFwj3PMYWyWYJdFRTnJi9I3ZjwEfGcgar4pGEghWvbRIa5wsPg6UCpg1JPr2b-ed-Pj_xxgrO3CoATYoQrDQxgveTRiwEmtfaGHG8bcqcmAJZpSenTWY9NR_y5Jj3cnTZ0gWzejt5O0x00i9GbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQ3Flb10Tc0T_A_UStxFYvWEfRRBWNmBfxhDa8P3Zji3JB6Hoy34uiQuau62Z3kLAF5o6b4QV156niAYEUGss7l3Wc4prJhS7biVPNdk2FqlKmWsjSTthvD_-oZuUl84wAETi8Ukbyqt0mwARXjmLKqRuM2bkZahhk1wV8j9ieZfHoy4EwbT7GBlv56pfic01gXox6HoHFZ-NLoQHqJ5U_KRQNe-KkseiDbmVDRqIhRKdKDnmJzLug-kbCQCdNqjUzAxby8PuwkG01bEKJ_0MtC-ESqHc_TF6lzdAA2eG4bxnZkyfECkmpCrpI-Bkl1gcGTr3QeSfadBt9BJSpZavA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
در نشست شورای معاونان مطرح شد؛
🔰
بهبود ۱۴درصدی عملکرد ایمنی و کاهش ۵۵درصدی حوادث در شرکت ملی صنایع مس ایران
🔻
گزارش عملکرد امور ایمنی، بهداشت و محیط‌زیست شرکت ملی صنایع مس ایران در سال ۱۴۰۴ از بهبود ۱۴درصدی عملکرد ایمنی، کاهش ۵۵درصدی حوادث منجر به فوت و افزایش ۲۳درصدی نفرساعت بازرسی‌های روتین ایمنی در مجتمع‌های شرکت حکایت دارد. بررسی عملکرد سه‌ماهه نخست ۱۴۰۵ نیز بهبود وضعیت ایمنی را نشان می‌دهد.
🔹
براساس گزارش ارائه‌شده ازسوی واحد HSE در شورای معاونان شرکت ملی صنایع مس ایران، عملکرد ایمنی شرکت در سال ۱۴۰۴ نسبت به سال قبل ۱۰۵ امتیاز، معادل ۱۴درصد، بهبود یافته و در وضعیت بسیارخوب قرار گرفته است.
🔹
فرآیند ارزیابی عملکرد ایمنی مجتمع‌های شرکت به‌صورت ماهانه و بر اساس ۹ شاخص اصلی، ۲۰ زیرشاخص و ۶۷ ریزشاخص انجام می‌شود. در سال ۱۴۰۴ هر ۹ شاخص اصلی به حد پذیرش تعیین‌شده، یعنی حداقل ۷۰درصد، دست یافته‌اند و ۶ شاخص نیز نسبت به سال قبل روند افزایشی داشته‌اند.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sy
@mespress_ir</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/456445" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456444">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/456444" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=PSmlnGbb0zi6Z22ksS3faiMDBlHe5ePC5ZHIjLtKsgcAjSC-ztd4QySukPs4JtMkFURwVOnYkfVxQfu5efdEedsgfzdX0brk5e8hKD_UIB-Vjza8ZBWlVpBoJiXr8ZG9X0tB3mifHt2s2XVh6KyrXYJqWwOuako0nrLvvf_rfcA3i7A1p76Uo6xjdHuWQXi0mW7QsglnqKlpmFsDb4M782P9k3TUyzp6VDOgRMXdYOhwTLXGg-VrspNYsKKrAEpB-L-V9ufFwCzkP6mw-WP6ZOZrXLXK7IB5RyyElTwxvIeRIjQc9udw60qOs-voKhE9qttcxHdyejwfAFY3gIaNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=PSmlnGbb0zi6Z22ksS3faiMDBlHe5ePC5ZHIjLtKsgcAjSC-ztd4QySukPs4JtMkFURwVOnYkfVxQfu5efdEedsgfzdX0brk5e8hKD_UIB-Vjza8ZBWlVpBoJiXr8ZG9X0tB3mifHt2s2XVh6KyrXYJqWwOuako0nrLvvf_rfcA3i7A1p76Uo6xjdHuWQXi0mW7QsglnqKlpmFsDb4M782P9k3TUyzp6VDOgRMXdYOhwTLXGg-VrspNYsKKrAEpB-L-V9ufFwCzkP6mw-WP6ZOZrXLXK7IB5RyyElTwxvIeRIjQc9udw60qOs-voKhE9qttcxHdyejwfAFY3gIaNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: از دولت درخواست می‌کنیم اصلاح قانون بودجه را در قالب لایحه برای مجلس آماده کند؛ مجلس آماده است بودجه‌ای با محوریت معیشت مردم و برای حل مشکلات آنان تصویب کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/456442" target="_blank">📅 21:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa938a5a8a.mp4?token=RmbV9mHEReyJt24O51E1ci0fP-ysCn3dwPsXBvbUSZsta2sDPYIcOdZO8NXWl8v3qCk6LI9VTR2a1i19XlAaoEbjj7ZJ6fdcZERibxPzdxDPbbbuzB2RUpMwZWufZfiZtULKGAm1UID6vAq5t4UIC1pel95lgi6ngQV2EwHmqEgmyuLRGroUsVSvmnD6lgq3lviqvdRYn67-9MZFEQBD8EsDcIAebIH0u8cw-NgN-Fh_d9F3bBzBnrsRikjqx_S24Pf-odBWq2wAyRw_w6o6PkCKVlbsXeOKjQkih_1zLpRMzbZP4gJ6QdnmsmYdKmg4V9QkoSSYfn-ruwr2J9Uxmq21hSIh_KNZOjouTPNSw886ZyYFzXQ3CwUHSV0GlG9yWP0NZKJD_SSAF8gr2Gb92oRinSyodebYUxAISvlHEyuVyOveOiJuTwhwjdbS3qNzEDChFVVwQa_XnDAmvqyoclkt1BTankZKdbd3msRtG_qMicFncFxS4-Q0kiIUsFvITca9j-kBjoe6R5dFESjBbjNr6_iqzgRNNewj18YD26k4z0Brt1f8U9bsQxy-gby1UuThbY5OP1UouqoslYH4jsHK9vWSQOVrgXtnpNIrQxZDZ7yDYoxpwuV8DdFn903GI1rvfvSBAJrFi4siUfbsFdkacsrCt4avh_NTWK66HnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa938a5a8a.mp4?token=RmbV9mHEReyJt24O51E1ci0fP-ysCn3dwPsXBvbUSZsta2sDPYIcOdZO8NXWl8v3qCk6LI9VTR2a1i19XlAaoEbjj7ZJ6fdcZERibxPzdxDPbbbuzB2RUpMwZWufZfiZtULKGAm1UID6vAq5t4UIC1pel95lgi6ngQV2EwHmqEgmyuLRGroUsVSvmnD6lgq3lviqvdRYn67-9MZFEQBD8EsDcIAebIH0u8cw-NgN-Fh_d9F3bBzBnrsRikjqx_S24Pf-odBWq2wAyRw_w6o6PkCKVlbsXeOKjQkih_1zLpRMzbZP4gJ6QdnmsmYdKmg4V9QkoSSYfn-ruwr2J9Uxmq21hSIh_KNZOjouTPNSw886ZyYFzXQ3CwUHSV0GlG9yWP0NZKJD_SSAF8gr2Gb92oRinSyodebYUxAISvlHEyuVyOveOiJuTwhwjdbS3qNzEDChFVVwQa_XnDAmvqyoclkt1BTankZKdbd3msRtG_qMicFncFxS4-Q0kiIUsFvITca9j-kBjoe6R5dFESjBbjNr6_iqzgRNNewj18YD26k4z0Brt1f8U9bsQxy-gby1UuThbY5OP1UouqoslYH4jsHK9vWSQOVrgXtnpNIrQxZDZ7yDYoxpwuV8DdFn903GI1rvfvSBAJrFi4siUfbsFdkacsrCt4avh_NTWK66HnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم از اقتدار بچه‌های پدافند هوایی سپاه
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/456441" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456440">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMLosyqDt4fdiRIpzNNWGjBoMngt41O5I9sefJHovbrKo3UyLq_47pJYZCeYVqp0r_InECQFWoJxTX_ryUeDoLn5TSsjI3eilZ1ogH_jEKKUDVi36pne0XkCGf8AuzsbyhGKa4VjPThZzx6cJFetXGVifgSEl8Xus0eg5JPhakhfWy68SAjskE9CI5_ip_iqcfaziksXTTGqvtSm-8xeI0N4jqIp1PRS1mAZsNeWisOV7A3VMptjlExDE-3len-BtBEVHcDJPHOQ7no127_-Cc_jM0CQIE0zExvB6hmxI12J6olF_aq3toXvaWihUC65jCfYORoq5vPUXZ-GSo5yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایحه‌ای که قبل از طرح در مجلس زیان‌آفرین شد
🔹
موجی که پس از اعلام دولت برای ارسال کنوانسیون خزر برای تصویب به مجلس در فضای مجازی به راه افتاد، خواهی نخواهی بخشی از توان، انرژی و تمرکز مردم و مسئولان کشورمان را از وقایع جنوب کشور به آب‌های ساحلی دریای خزر سوق داد.
🔹
این کنوانسیون که ۸ سال پیش به امضا رسیده و به جهت ابهام‌هایی که دارد پیشتر از مجلس به دولت برگشت داده شده، پس از چند سال فرو رفتن در محاق، به یکباره از سوی دولت حلول کرده.
🖼
اما چرا این لایحه به تمرکز فکری مردم و مسئولان ضربه می‌زند؟
🔗
دلایل این موضوع را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/456440" target="_blank">📅 21:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415146f8fc.mp4?token=pHNegs4HkF8pyZdo-XFAkUuKaIJoZ68IL7TZbo2e55r0X1OoUSfxgT9vQDP1P15S5Qqt4WsTsE9OWxvyHePj5EOBQ9FqYpF8iCCNer-gHJCL6N3sX72mlQHeZP69tvbqpCqRBUjyr1RrzcH-0SPB4c2082A00I6FeeDL4CHMPRt3YhCvbMe-huzXVul5PBzP9wj3Rg_fZHJkz82qrVro_dGRiV-Lf5l01yIrggjXTsPmxycaSOg7aF3NRHuyZIQZ8ATGSG19rw-TWEG4iAiqse033jJuwTfF_YNxMqkz2BCHs8HLJpgIeQMWgH9qZaS6B9gMpUBPL4ULdSA68qypzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415146f8fc.mp4?token=pHNegs4HkF8pyZdo-XFAkUuKaIJoZ68IL7TZbo2e55r0X1OoUSfxgT9vQDP1P15S5Qqt4WsTsE9OWxvyHePj5EOBQ9FqYpF8iCCNer-gHJCL6N3sX72mlQHeZP69tvbqpCqRBUjyr1RrzcH-0SPB4c2082A00I6FeeDL4CHMPRt3YhCvbMe-huzXVul5PBzP9wj3Rg_fZHJkz82qrVro_dGRiV-Lf5l01yIrggjXTsPmxycaSOg7aF3NRHuyZIQZ8ATGSG19rw-TWEG4iAiqse033jJuwTfF_YNxMqkz2BCHs8HLJpgIeQMWgH9qZaS6B9gMpUBPL4ULdSA68qypzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: در تلاشیم دورهٔ زمانی صدور قبض‌های برق را کاهش دهیم
.
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/456439" target="_blank">📅 21:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGCLdANpIFVNDQeXZkN2-GY4PyPBGaBoBM0pYinVrmqyhZtbKVAGqSYMFNNYY_C5rwPxsroUlL5HxwT3DiiMbdZKMzsfl6YOKBuJbydpCXByBUFqyBayoGNOfC8AkQIqJeonRUGoqi6hlsKnzH2c2soHnq2_WryHiT9R2AsmNeXwQfE4bWMHJK0sJzAb3WxBz5CGO1ZUZA72PAf-6JdSZI5jx9aKOXmVcmloRwdAEByS3PnkpTJSu2E6whKqgWC9Q6h3GiXBJLXVbaQUwq2o2rMTUBeAyxLG5ksmeAyh87BeSaU4-gi1VdvJHM1ccU4MtAMOtW6M_McC5yTlckStRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان فرمانده آمریکایی به غافلگیری از انهدام پایگاه‌ها توسط ایران
🔸
بالاترین مقام نظامی آمریکا در دوره باراک اوباما روز یکشنبه تأکید کرد که آمریکا فکرش را نمی‌کرد که ایران پایگاه‌های منطقه را «نابود کند.»
🔹
رئیس اسبق ستاد مشترک ارتش آمریکا مایک مولن در مصاحبه با ای‌بی‌سی نیوز به بررسی وضعیت نظامیان آمریکایی در غرب آسیا از جمله ملوانان ناو آبراهام و طولانی شدن مأموریت این ناو هواپیمابر گفت:‌ «این موضوع قابل توجه بوده و بسیار دشوار است. این استقرارها بسیار دشوار هستند. از نظر تاریخی، ما معمولاً قادر بوده‌ایم برای استراحت، انجام تعمیرات و سپس بازگشت به عملیات، به یک بندر برویم. حتی در زمان ویتنام، این کار را انجام می‌دادیم.»
🔹
فرمانده اسبق آمریکایی با ابراز نگرانی درباره وضعیت ملوانان در ناو آبراهام لینکلن بیان کرد: «من قطعاً با توجه به آنچه در گزارش‌های خبری دیدم، نگران شرایط کشتی بودم. می‌دانم که فرمانده ناو لینکلن، به سختی روی این مسائل کار می‌کند و همچنین معتقدم که حقیقت احتمالاً جایی در میانه (گزارش‌ها) است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/456438" target="_blank">📅 21:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نگهبان بیمارستان ناجی یک نوزاد شد
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/456437" target="_blank">📅 21:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456436">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی، وزیر سابق کار: می‌شود هم جنگید، هم اقتصاد را مدیریت کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/456436" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرتان در مورد کالابرگ چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/456434" target="_blank">📅 20:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/456433" target="_blank">📅 20:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دربی تهران در انتظار تعیین تکلیف میزبانی
نقش‌جهان قطعی نیست
🔹
طی ساعات گذشته شایعاتی پیرامون باشگاه معرفی قطعی ورزشگاه نقش‌جهان برای میزبانی دربی توسط باشگاه استقلال مطرح شده که پیگیری‌ها نشان می‌دهد صحت ندارد. از طرفی سهراب بختیاری‌زاده در این مورد هنوز نظر نهایی خود را نداده و تصمیم شوراهای تأمین و مسئولان ورزشگاه و استانی نیز تعیین‌کننده است.
🔹
استقلال ورزشگاه نقش‌جهان اصفهان، پارس شیراز و امام خمینی اراک را به‌عنوان سه گزینه میزبانی دربی تهران مدنظر دارد و دراین‌رابطه همچنان مذاکرات خود را در ادامه می‌دهد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456432" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/456431" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/456430" target="_blank">📅 20:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز دوبارهٔ ۲ عقاب‌ در آسمان دالاهوی کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/456429" target="_blank">📅 20:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک امدادگر از جنگ رمضان: پدرم گفت حق نداری به خانه بیایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/456428" target="_blank">📅 20:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456427">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhjNju2QK6HstkK3Gyo3m9cHIGIKNwHWWj3888dqXnvnW6lGM0Uh7y-9OknP0UEdhwSfaIbBg5w0IW_Xp0sVb62h2KSJax8i-rl0dFiavASStX6GSwmyHkRJYT0nfpo8eh5SdUpCpdwZT-M2WVzmTfeiD_eX9zKa1lUc_IBtybflRfdcxGl0cEKk2F1_FNwMNYFy_w1btdYO12ZAM5Dfc8zXMElOds4EgQwLlCGgyE62oKBMtGNPj7vis9NuoGK_RqJXIWcGtHhyD7dU_NhAqtSZSwbAOJtvNBEI43t_3ntW5nlK78Kxc5dDawcdmVkwZths2cMlAeWPIUqrofN38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه ۲.۴ میلیون زائر در مسیر اربعین
🔹
همراه اول در اربعین ۱۴۰۵ میزبان ۲.۴ میلیون مشترک در عراق بود؛ زائرانی که با استفاده از خدمات رومینگ، بدون نیاز به خرید سیم‌کارت عراقی ارتباط خود را حفظ کردند.
🔹
تخفیف ۳۰ درصدی بسته‌های ویژه سماح، ارائه ۱۰۰ هزار بسته ۱۰۰ گیگابایتی اینترنت داخلی، بیش از ۳۰۰ هزار بسته ویژه روبیکا و پشتیبانی شبانه‌روزی در مرزها و شهرهای زیارتی، از جمله خدمات همراه اول در این ایام بود.
http://mci.ir/-7J70P9
@mcinews</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/456427" target="_blank">📅 20:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIzsQ2zS4FzllfFEDPeKDsNCz4RN8PSqTBI3tnzR7rGmr76_HngouIGEZCveNsSn49lPFiK4v438QqVttLVLKSxE5W53a5Uyma5ePms4v1oBpnVEdYA_F2ZbuPDHgbByrQmtKZ2fZzj1xYfsrCpDuFGSjprLQmWwJGvQZrgMMTu106jmVLQCuiv8T92VNW2-oYu3sGygK_vFj_C9fkJfp8xctcfjucEek50-FvJuJUq1IGSh6sDP8ErTOc0pRJ-rGivfDM8V5Okg7-ZXeqrb79_5yayO1HBsbZUpiyrwWipWrCD7DkMmjOaW7y93y__rWmvvkdc1ZjN26gFIK8GfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
کانال مِتانو | آموزش هوش مصنوعی
🔐
محتوای Vip و غیر قابل دانلود
🤔
عضویت فقط با خرید اشتراک
😡
اشتراک یکساله: 1 میلیون تومان
😎
390 تومان با کدتخفیف: fars
🤖
آموزش بیش از 200 موتور تولید متن، تصویر، ویدئو، صوت و اپلیکیشن.
🧠
تا کنون بیش از 110 مینی دوره با ارزش تقریبی 40 میلیون تومان بارگزاری شده.
✅
مشاهده نمونه آموزش ها و پیگیری مراحل ثبت نام از طریق آیدی پشتیبانی:
🎁
@Metano_Ad</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/456426" target="_blank">📅 20:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456425">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/456425" target="_blank">📅 20:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzvjw5DdGAmtsSeqGnfZ-zkjHSMJS0VFwJ9FADDDPo9J_ExZEUW0oYjT9CXJRVOMUeXQq2emeA590wcfSqRUXoKVzwczYsRt-RqPy3eRfPt_tVu4ndw7_qbBgqUty5y_P7C87CLAwppIJJHDgHAL-vHzTcNe23fSqP_3swbU9vDf4kj6Fc5WxrllJBH4QSaHU17br6x7Qw07YuxjfwtGRZWaDFbrUTeo-lEHz-WTrwF46__5esk5jxPy3DXwmUBzZQ-3_Ya-gaw4veiUv7a7Spg69d-gZKOgWslyNac5PErquzLtT_xrE2ZlIw1_4tnr37rts3Xz42_EY-ab0vN_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتصابات مدیریتی باید علمی و فارغ از ملاحظات سیاسی باشد
🔹
انتخاب، ارزیابی و حتی عزل‌ونصب مدیران و اعضای هیئت‌مدیرۀ شرکت‌ها باید براساس شاخص‌های روشن، علمی و قابل سنجش انجام شود تا از شکل‌گیری هرگونه شائبه، حرف و حدیث و ملاحظات غیرکارشناسی جلوگیری شود.
🔹
معاون اول رئیس‌جمهور و وزیر علوم گروهی از استادان دانشگاه در حوزه مدیریت، شاخص‌های لازم برای ارزیابی مدیران در دستگاه‌های اجرایی، شرکت‌ها و سازمان‌ها را تدوین کنند تا این شاخص‌ها برای ارائه به رهبر انقلاب آماده شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/456424" target="_blank">📅 19:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc4tAbVlhGgI3hfdB2ayTjNU73fBxfhMwasePRntUKae968s_gsJ-2zvHspDUtTK5d79Lve3OV5HE5RFmOkpiXffodSzY39As6Vu0xcmYNyn_hW-e2-cI46wxQ4mXxXJoDT6qG9Q6mGjknsoWBisbnqpog6uf6KKaU0Hdv3iG_5vr0iIvVWpr3fUfIo-BMuOo7NY-adO-lancNSvsENZUJeRWwIPyIKqZcQEqRVV6iRcyknVUXDaYTZg5WMIUNvR_me2zhTz0RgI6p3uJGNDTi9hp2hbnTf8QOpKKQhu2bhOTe2Rxjc35eI2l61tIboHP40LdMPV3URar1zDDZ_-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا خلع سلاح اتمی اسرائیل باید مبنای توافق پایان جنگ باشد؟
آمریکا و رژیم صهیونیستی در جنگ با ایران به بن‌بست رسیده‌اند و اکنون ۲ راه پیش روی خود دارند:
🔸
تهاجم سنگین‌تر به ایران برای به‌دست‌آوردن آبروی ازدست‌رفتۀ آمریکا.
🔸
پذیرش شکست نظامی و ادامۀ خباثت علیه ایران در حوزه‌های دیگر از جمله تحریم.
واکنش ایران در قبال تشدید تنش چه باید باشد؟
🔹
فعال‌کردن جبهه‌های جدید و افزایش سطح درگیری.
اگر سطح درگیری به حوزۀ اتمی رفت چه؟
🔹
ایران احتمالا در دکترین هسته‌ای خود تجدیدنظر خواهد کرد.
🔹
توازن به‌کارگیری سلاح در سایر جنگ‌ها از جمله جنگ روسیه و اوکراین به‌هم می‌خورد.
اگر دشمن بخواهد سطح تنش نظامی را کاهش دهد چه باید کرد؟
🔸
هر توافقی برای پایان جنگ باید مسئلۀ توازن قدرت منطقه‌ای را در نظر بگیرد.
🔸
ایران طبق فتوای رهبر شهید انقلاب، به‌سمت سلاح اتمی نرفته اما رژیم صهیونیستی سلاح اتمی دارد؛ در چنین شرایطی خلع سلاح اتمی رژیم صهیونیستی باید به‌عنوان پیش‌شرط هر توافقی برای پایان جنگ از سوی ایران مطرح شود.
🖼
اما چرا این پیش‌شرط باید مطرح شود؟
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456422" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgUjnmEh2WmfKlB7dWoji2UZHQTQFg8sMZBuNKIIg8G4l1K1d7zekMo_lzcaXy-Tw6sTH6nc6p9vg1vLGVMZArd4Z_8CFTrLym0FDY28_heE7eRpyl6h8B_W-JDWOk9t8Wu-KBkmwQgS6sUfM_1AYFq8MQm76zQg83htiMurbI1KcitMMmSqQZ_xxEOsj2jmWQfw6k8vPVSD0Y9JxKqMdbaKXWDAVlWwlL8GkJA05dkk03-uB7CXyM1hdt_TeVBzI1u6OfBQUT-yuPhdBc6R0z742oWVraWvyijgQMX7TP07rdu-nqQnrCedLp1Yk-HpWG2iG2v34B3f3sGGokZiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
قوه‌قضائیه: درپی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/456420" target="_blank">📅 19:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZjYjY3jaIwZXN7g8sOtTNZ9lE8VV1k1X-r9JFgx8a0qEGNxl8B4nuhwzvdjc-Je-4EjFkT08ncpNcwvZkhR-uCR_0CktHsbLHYGkoj5K7xT85Z8YEHxp_ntMB1Kc3FRTwNDt50mxqwJvfvAHnD3q1E41CGnEt4LrOs7TvIIgYlSgfimq3AlUg53uprgbFZgE9ZCH0H6a0BWXsdIAI8fRB1toVNQ2TtVTXXGLkwzmN2PKnMDv13PNzpfmQ6a_Qi2yt5td82CQDMarMgwarKNm-lq-x9WIw0dgMm1hcMUOEpISDHqL-oFaAwW5FtRAbe5o-vVTlKdYbzi1z8hD4Djvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ حزب‌الله: با اسرائیل تنها زبان مقاومت کارساز است
🔹
نمایندهٔ حزب الله در پارلمان لبنان: دست از مذاکرات بی‌حاصل با دشمنی بردارید که چیز جز ننگ و عاری در پی نداشته است؛ با این دشمن جز زبان مقاومت کارساز نیست.
🔹
سرخوردگی و ناکامی کامل از آنِ کسانی است که با اتکا بر آمریکا مسیر سازش و مذاکرات مستقیم را برگزیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/456419" target="_blank">📅 19:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bab0f44de.mp4?token=tyW2kDUdRW2Clr4Dqv3q1jvFOtgrbX-Eh1r7FUANRFIOX9zf96rzKty66FyBarg9YqSlFZV0jcK_0hWfAxDodkbEBEHF1LyljeZvWfB39KfgRwMhPg_ecRM-gqf6wW3F5_Hvhp4vqU78N7j4TJyCnG4TO_NT7Wb7WWztY_H3wxDNk3nnawrmmJDB5MjVrYFVcXbmgDdNBmTRZVHY0EbW6aENNcmHOr2cmHIJBvx8qrHuJlX-xJPmBX4dBKxqN1GVbUzkH-IvGBT19fuTySBbD1F5Da4xRblgWej9mgB-i0Rxe4BsgRvJvWFddPozDrlFnNp-fCwzQr_9AFEgrWAkow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bab0f44de.mp4?token=tyW2kDUdRW2Clr4Dqv3q1jvFOtgrbX-Eh1r7FUANRFIOX9zf96rzKty66FyBarg9YqSlFZV0jcK_0hWfAxDodkbEBEHF1LyljeZvWfB39KfgRwMhPg_ecRM-gqf6wW3F5_Hvhp4vqU78N7j4TJyCnG4TO_NT7Wb7WWztY_H3wxDNk3nnawrmmJDB5MjVrYFVcXbmgDdNBmTRZVHY0EbW6aENNcmHOr2cmHIJBvx8qrHuJlX-xJPmBX4dBKxqN1GVbUzkH-IvGBT19fuTySBbD1F5Da4xRblgWej9mgB-i0Rxe4BsgRvJvWFddPozDrlFnNp-fCwzQr_9AFEgrWAkow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرهایی که اینترنشنال بی‌صدا حذف‌شان می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/456417" target="_blank">📅 19:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ebb0004f7.mp4?token=AXmoV4r4YB9SaTyR2DAYEBE8FnSoz5TFLuDVtnS6y4-7Pe8hh6dERWkZKffnruWmYZ70Q5sI7gklBO-MpqA138vXvbRfJhZLEgK7CV1GmdR0X0CFg9yk3Yu4Eeub4_IK7_LeJZ_MM_OXwTFVf5FYnfvjVLWMbDM5GHByYuzYXG-k2LRcxk4e1aT3ofSIIrWxtYBaZ5DSTlOQ1Yu8ZOrWWt2yVd9-LhLTgL2AMRkWui1jNTg4VDuyQNByk5sgJVbIe8PO9n7fYDUsabg1bJbVvLK5dcBEHX9IQn7lSGzln415V-gJMFvEizTo_1wHDSV8ovUWMkh3Y-3IznjDzqskoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ebb0004f7.mp4?token=AXmoV4r4YB9SaTyR2DAYEBE8FnSoz5TFLuDVtnS6y4-7Pe8hh6dERWkZKffnruWmYZ70Q5sI7gklBO-MpqA138vXvbRfJhZLEgK7CV1GmdR0X0CFg9yk3Yu4Eeub4_IK7_LeJZ_MM_OXwTFVf5FYnfvjVLWMbDM5GHByYuzYXG-k2LRcxk4e1aT3ofSIIrWxtYBaZ5DSTlOQ1Yu8ZOrWWt2yVd9-LhLTgL2AMRkWui1jNTg4VDuyQNByk5sgJVbIe8PO9n7fYDUsabg1bJbVvLK5dcBEHX9IQn7lSGzln415V-gJMFvEizTo_1wHDSV8ovUWMkh3Y-3IznjDzqskoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگ ورزش به همایش آموزش‌وپرورش رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456416" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_whVHsdYRRz3DS0OPh9PzFp_PRMpQlYTmD7ZwB0L4pLMz5OS88nwFo-ikda0ekEBZVUIQRYro5uKKJrMc43VaYSchtIFwGMwR-EbuF2Rrbdy-HDmJi32fp81J9hdbcRWPagzOcc-FwkuGlLJQM-HiV69eK8E-am5_m8Rd8pk2EpHE_nircB9iQ-daQhCSltoTBLjsUmpEn7JGG-dJZT445BXrCZzhe_t9z-tABAb2EObZBwnkNaCnXJ2SSMhcIqtEglYpThxLGU_fAxbKDRKGRK33tW2YI1eFlrZpWLs7fynEWe_4WI_tbl9CmSrByzF78pZXdE508y0BDHp6Tgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌خبری از ۹ صیاد بندرلنگه‌ای پس از پنج روز
🔹
فرماندار بندرلنگه: ۹ صیاد بندرلنگه‌ای که پنج روز پیش با ۳ قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند، تاکنون به خانه بازنگشته‌اند.
🔹
احتمال تمام شدن سوخت، نقص فنی شناور و یا گرفتار شدن در شرایط نامساعد دریا برای این صیادان وجود دارد.
🔹
تاکنون اطلاعی از وضعیت آنها در دست نیست و جستجوی دریایی برای یافتن این صیادان نیز نتیجه‌ای نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/456415" target="_blank">📅 18:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هر ۲ مسیر تونل توحید امشب مسدود است
🔹
با توجه به انجام عملیات تعمیر، نگهداری و کالیبراسیون تجهیزات تونل توحید، هر ۲ مسیر این تونل از ساعت ۲۴ تا ۵ صبح روز بعد، مسدود است.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/456414" target="_blank">📅 18:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۶ میلیون نفر برای مطالبۀ خسارت‌های جنگ به قوه‌قضائیه وکالت دادند
🔹
مرکز وکلای قوه‌قضائیه: تاکنون وکالت بیش‌از ۶ میلیون نفر با درخواست‌های مختلفی مانند خسارات مادی و معنوی جنگ به صورت موضوع محور ثبت شده‌است.
🔹
بسیاری از مردم با وجود اینکه عزیزترین افراد خانواده خود را از دست داده‌اند، مطالبۀ شخصی ندارند اما خون‌خواهی امام و شهدا را مطالبه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/456413" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqpaNGk679_UYDwWATBDdiM3usUjyUlFuIr54dIjl73CchdF7km5adT7C7D0jBvbNTnY5YNhXxDtZLLuXl8V9ppRE2Mp9Cye7cDYfef_vQgKURhzjdy_d9tv79X4DCTqcfUycTMWLx89h7rQU-vA_ngbsn3Yq020KTqbOVDYpc_ZmjQ-4mYLz7Yt3BZ23jb3-0tkbTLi30O63HvHLTUJG6oIc0R-ssHn8hvslRA7gFnoUUBNznQsE2tyODqpLYEUa5I1H7onEzYr6pxDP2WabUDCR-b1wUJTsgLC3lqC644en0M77IBQajEqMj4ZNZjh5hZ1jWTgbvGzcV-ds3JmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: هر تهدیدی در برابر سد دفاعی ایمان و تخصص ما بی‌اثر خواهد بود
🔹
بیانیه‌ ارتش ایران به مناسبت سالروز بازگشت آزادگان به میهن: بازگشت آزادگان، نقطه تلاقی صبر استراتژیک، ایمان تزلزل‌ناپذیر و پیروزی مطلق اراده بر زنجیرهای اسارت است.
🔹
بازگشت آزادگان نه یک بازگشت جسمانی، بلکه تجلی اراده تسلیم‌ناپذیر در خاک پاک ایران بود؛ رزمندگانی که در سخت‌ترین شرایط اسارت، مفهوم پایداری را باز تعریف و به جهان ثابت کردند که لباس نظامی، حتی در غیاب سلاح، زرهی از عزت و وقار است.
🔹
امروز، ارتش جمهوری اسلامی ایران با تکیه بر میراث شهدای راه حق و تجارب گرانبهای پیشکسوتان و آزادگان سرافراز به جایگاهی از اقتدار رسیده است که هر تهدیدی در برابر سد دفاعی ایمان و تخصص بی‌اثر خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/456412" target="_blank">📅 18:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWsDQuJbY43wU8QsQf4xDJeBEkLjj8AQK25Kje4iW2s9CbBVCOR2IhvLuNN8vDRm_Wbe3TxOaAI8qqCwNyUl4k_G3sdFSCR66w2-_UV-OZKMIWAc7BJZIzOPtPX2I9Q1Dyep7fHg6gVSTkF9joVOFXcxWoMAtYxBtQqpbijoKTM3E4w0BB5lt6rZGwJKYKgAQ9PbTQs10BunmbcN-WL-GssMZqzm4yn0Ml_zk_2GvntQBs1q2SoJqBThrX_cdLpAOvv3a2MXG-EV31bvX9p4cz67HrMAdR2cU9pCy4VAzV8Qb5nWbgsqe0wfX3H0unjtz8WRCfoP7_d72OKf1G7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/456411" target="_blank">📅 18:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1d1277df.mp4?token=qI2eJ1BgDwYPzd51RM8o5E7STKZcckDg-mxAQ38txautMuxFuSkFvK6xIHnlFZBPdRhxqwoyxROkZVwCb66qVuItiqHLpesySX6rswIK0_QcWWSzK5HxbtBUolkIgLb07yl-lgEd9eC2WuFKXn2Gt7LHZhCD1W8lFbnSqj0EdRfJnjOgNqQVq2ican9uoe8dIRQkAuz-RU3D91-Zg75DSJEE6-wvjVRq4zs67vOiRoi9Y_3g_VoCDkFdmSwV47bHfEAEqd7HPtEfSCCb6zIv0udBfIWd63C_v1JaXTDxohflVJ3s1qEWmyndAzvubXJON-6oDAs875A2HI4uwB76fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1d1277df.mp4?token=qI2eJ1BgDwYPzd51RM8o5E7STKZcckDg-mxAQ38txautMuxFuSkFvK6xIHnlFZBPdRhxqwoyxROkZVwCb66qVuItiqHLpesySX6rswIK0_QcWWSzK5HxbtBUolkIgLb07yl-lgEd9eC2WuFKXn2Gt7LHZhCD1W8lFbnSqj0EdRfJnjOgNqQVq2ican9uoe8dIRQkAuz-RU3D91-Zg75DSJEE6-wvjVRq4zs67vOiRoi9Y_3g_VoCDkFdmSwV47bHfEAEqd7HPtEfSCCb6zIv0udBfIWd63C_v1JaXTDxohflVJ3s1qEWmyndAzvubXJON-6oDAs875A2HI4uwB76fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس فتا: در خرید از آنلاین‌شاپ‌های غیرمجاز بیعانه ندهید
🔹
رئیس مرکز فوریت‌های پلیس فتا: خرید از آنلاین‌شاپ‌ها باید از طریق سایت‌های مجاز دارای نماد اعتماد الکترونیکی انجام شود.
🔹
شهروندان در صورت خرید از فروشگاه‌های فاقد سایت و نماد اعتماد، ابتدا کالا و اصالت آن را بررسی و سپس پرداخت کنند و از پرداخت بیعانه خودداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/456410" target="_blank">📅 18:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcNqSnniDzkJHEMiA_GMsAA6MT7DnZT7L7kz8TBgP1fn_YAzELenWRdRf1H-YjJzDtbW5G-aRvCWJkCmpBob7NACc3ZOq1GHtoWHMfWMWSGqRGzMbuop9plutKssGd6vchqXramhuNBxqAooLFYlRrC3u40toOAxDXJ2bOsS8RLjGkeip6OuFbF0w4liZrptbP5IA_kZhdzbPi5HALAMKVNp5KnxAMwQaj9aO6kwc_GtnUEnQE74b83_hOVIK7xb33bdAIt4cy5d63H0iA0yq43KO73zbjrALYcMFsixyY3jUnVNAj74OTHZ25UQgAVRzDKw8GLjptAfO6W5ccOiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تلفات مزدوران سعودی در حملات ارتش یمن به مأرب و المخا
🔹
منبع نظامی یمن: حملات به مواضع دشمن سعودی با نهایت دقت، به اهداف خود اصابت کرده و در پی آن، چندین عنصر وابسته به عربستان کشته و زخمی شدند.
🔹
در جریان این حملات، چندین انبار مهمات و سلاح وابسته به عربستان…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/456409" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW-k8DtNRxz3zXNlYgM5mtLxaaZrJG2fXF_cNtrEWDbO5LBah2KtDlF2EBzOPPp9kyXBEjVCsWQRvDCnc6fSAPMXcNyzBr386V-1wzcdYBi2Nbx1B0rsqAQCbwFWZjUYveF5eAZBpuUawQ2BeCAt7YX2_Xx0bcA09eoVDHzqnfXAmHRxpAXW_1nUNI9e130uxgzBaOkyUKlxG03DtR0FBS5imgkgVx4EGMPTK-Cp69G03H0ACoc0R_1No6SsPzuMwrwISrJ6wK7dqp-lW9h63PPw-rJc4UCYwPH1VoldHSuLHT4o5cDJf9la11Wh3wDkkowY16b4S3K6RlRMQtUVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام تصمیم گیرندهٔ نهایی دربارهٔ زمان برگزاری انتخابات شوراها
🔹
سخنگوی ستاد انتخابات: براساس مصوبهٔ شورای عالی امنیت ملی قرار بود انتخابات شوراهای کشور ۲ ماه پس از پایان رسمی جنگ، که این‌زمان هم توسط شورای عالی امنیت ملی اعلام می‌شود، برگزار شود.
🔹
بر همین اساس، جلسه‌ای بین ما و هیئت مرکزی نظارت بر انتخابات شوراها برگزار شد و توافق شد ۲۴ مهرماه زمان پیشنهادی برگزاری انتخابات باشد.
🔹
با توجه به این‌که مصوبهٔ شورای عالی امنیت ملی وجود دارد و در آن اعلام شده انتخابات ۶۰ روز پس از پایان جنگ برگزار شود، شورای عالی امنیت ملی باید دربارهٔ زمان برگزاری انتخابات اعلام نظر کند.
🔹
ما با شورای عالی امنیت ملی مکاتبه خواهیم کرد و اگر موافقت صورت گیرد، زمان دقیق و رسمی برگزاری انتخابات مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456407" target="_blank">📅 17:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQXhd8Wtfgf9KfThpNB8qKouGthQDN_FwhYDWi_ILpP7mqQAdywkbOpkXICar0xZM7y1gRU0EZqpQ_IralhwH9VzmJtjdmXaxTws6urzINWcl7Yzh3xGXkC4mc15k-GeHvO2hsGVyJ8bOwf32WwiQtprSEqQDDeIqS1UijGgABK_geu6Ldosm_J4N5pyVp_7F22hZMO0W6rmC11Aywt-QkYszZJrJ0TsH8zDPoUcWvJi-btp13433hF5VaVesSrUs7YFl9Dk7a415rcdpRYi9_hm72O6fmcrhP4wxF2mKQnrwdPbj4xSVou_tMfqcE9DkaOvZSHPL-ElzG85uGV4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ ورزشی برای درمان بی‌خوابی و استرس
🔹
ورزش منظم فقط برای تناسب اندام نیست؛ بلکه می‌تواند با کاهش استرس و تنظیم ریتم شبانه‌روزی بدن، به خواب بهتر و آرامش بیشتر کمک کند.
فواید دیگری که فعالیت بدنی مداوم دارد:
🔹
کاهش خطر بیماری‌های قلبی
🔹
تقویت عضلات و استخوان‌ها
🔹
کمک به کنترل وزن
🔹
افزایش سطح انرژی روزانه
🔹
تقویت سیستم ایمنی
🔹
بهبود کیفیت خواب
🔹
کارشناسان تاکید دارند که تداوم در ورزش، هم بدن سالم‌تری می‌سازد و هم ذهن آرام‌تری و می‌تواند کیفیت زندگی را در بلندمدت ارتقا دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456405" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBNNpC8m8v0g8zQsZUZADPi80SjzBoICVvlcAkZL7kXvHR7x-wELGR8XH7gVI01tEXaP1U5ygY4uMcqzHa8G28I0pGTD5zZVsoJkrGo06PfLcqkx_jwfrFh7iohdNVgvY4Bdx8rqsZoCo13BQAwZynYhdPd98tSJRcFE7_h0GHNIYg9KqmHo8tLhnfwWqoCA4whU_liI3ySrzSkxvCn2Gvam7ZOEU64tfZq4gFnf6lQP7IE8oVpc4h_Cb1qa3bKj1EO78pykS4dR2DF65do_d5ZL-noHAvM-bEwFvU8epXT2X59a4tvhFL-_01uNTEcHm0mH7usrmv-ZuSnKXZ1zSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمیه بنزین خودروهای مدل ۸۵ و قدیمی‌تر را قطع نکنید
🔹
با اجرای آیین‌نامه جدید، خودروهای تولید سال ۱۳۸۵ و قبل از آن فرسوده محسوب شده و ممکن است سهمیه بنزین یارانه‌ای آن‌ها حذف شود؛ در حالی که بسیاری از مالکان این خودروها توان خرید خودروی جدید را ندارند.
🔹
در همین راستا پویشی در فارس‌من ثبت شده و حامیان آن خواستار توقف اجرای این طرح تا زمان ارائه تسهیلات ارزان‌قیمت، وام‌های بلندمدت و مشوق‌های واقعی برای نوسازی خودروهای فرسوده هستند.
🔗
اگر شما هم با حذف سهمیه بنزین خودروهای مدل ۸۵ و قدیمی‌تر مخالفید،  برای حمایت از این پویش
اینجا
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456404" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f5e1810.mp4?token=iLrawGJl1eYm0vclYkbQCdup59tcyjmOx-CFmY_SEqjFd5u6zdjeRfgvzz2qxOaYu02IiNPwAWeQknl8j-0zqaF0qtMNg1wWlJr42uyp4vYREilRDrBjVLHlOniFaHNEJk5DWnsrYeY9IEb-HMKJeb9dRnKPulgFlQ7U3Sy08UXN7O6AoeU-LrBTsnN_GKFYAL4gMGstlU044dn_plF1iqTbUEMGx6BxWftmfGSUmAh8Tvdeg9V6AQBiADac54-ol3tj3_whm4Kdyte50_2rZws2QiZ0ir8hk_YaVSnFzM5OwDAlgAg-SA33_2Igx2cptvGYCAytccqCcoEk8RxukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f5e1810.mp4?token=iLrawGJl1eYm0vclYkbQCdup59tcyjmOx-CFmY_SEqjFd5u6zdjeRfgvzz2qxOaYu02IiNPwAWeQknl8j-0zqaF0qtMNg1wWlJr42uyp4vYREilRDrBjVLHlOniFaHNEJk5DWnsrYeY9IEb-HMKJeb9dRnKPulgFlQ7U3Sy08UXN7O6AoeU-LrBTsnN_GKFYAL4gMGstlU044dn_plF1iqTbUEMGx6BxWftmfGSUmAh8Tvdeg9V6AQBiADac54-ol3tj3_whm4Kdyte50_2rZws2QiZ0ir8hk_YaVSnFzM5OwDAlgAg-SA33_2Igx2cptvGYCAytccqCcoEk8RxukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند سپاه: در حوزۀ پدافند هوایی حتی یک موشک، سلاح یا قطعه خارجی استفاده نکرده‌ایم و ایده، فناوری و تولید تجهیزات کاملاً بومی است.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456403" target="_blank">📅 17:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSoC6IBBRlARE98sF1htWVs5vNKJ-1ryMbKr2BWcoFeAHVotNQhNrjYu4L_rpDFl5652WYYzFFgFiIb9FWZcYkDlVsX4npBHAIFBROFGy4JqIFlW6jV3SO6EseVuJaPAFF-qAW6IJonBIIh9AXdA_KKVpBYB0N2677gTrOdSR-ePV7b1o2Di2I6sDhZ5qTcmhcddCX2xoMnUIVDJVUvZRcoJIGxY_IAtfJh_0J0pQGGMggcNqRIYZjLjNhM0E4S6WydcPUMoSHucmSC953MilFuFLwBjR71b700wggYRvkKHcPyqM4mnElwCssKfMFgboyLFuwo_piFxh3PmXR7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: اگر میزان مصرف بنزین خودروهای داخلی مشابه خودروهای روز دنیا بود الان شاهد ناترازی در تولید و مصرف بنزین نبودیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456402" target="_blank">📅 16:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f607b9ca.mp4?token=gSIFAaf9BJjr9b86uznHKb0tOw3vmU8WvqDJN3fo0Iz3Ds1NrQLtUY4A1t8oX5rkyLiGEyjwyKp4FmNNdFDsUua9EunH5Ls9bcgTv_ZfinMQ5kiCdlXAxfzs508HtVEkV-rK4DkQtayeFlfLBUWhdmGCyphTb2cJ9XvCjUM_8EKkDRxfiB8aoDvctroiX8LQ303g8KHpfRarEWzzeKBlyP8TK-V6T8yUsWut-ufIJkUOgIJiOrpxvIVa7g4_i1rqBzQSOVXREZgKZW136aqnuiSY3zNkO1VKOMw0J-0vsOG7ikqdgbVoWWJ9u3-oBlXwv4QufGRIBxe_dU2tA_k3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f607b9ca.mp4?token=gSIFAaf9BJjr9b86uznHKb0tOw3vmU8WvqDJN3fo0Iz3Ds1NrQLtUY4A1t8oX5rkyLiGEyjwyKp4FmNNdFDsUua9EunH5Ls9bcgTv_ZfinMQ5kiCdlXAxfzs508HtVEkV-rK4DkQtayeFlfLBUWhdmGCyphTb2cJ9XvCjUM_8EKkDRxfiB8aoDvctroiX8LQ303g8KHpfRarEWzzeKBlyP8TK-V6T8yUsWut-ufIJkUOgIJiOrpxvIVa7g4_i1rqBzQSOVXREZgKZW136aqnuiSY3zNkO1VKOMw0J-0vsOG7ikqdgbVoWWJ9u3-oBlXwv4QufGRIBxe_dU2tA_k3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرلشکر حاتمی: توانمندی دفاعی جدید به ارتش اضافه شده
🔹
ظرفیت‌های آفندی و پدافندی ارتش به‌سرعت در حال بازسازی است و ما لحظه‌ای را از دست نداده و از فرصت‌ها حداکثر استفاده را کرده و می‌کنیم.
🔹
دشمنان با وضوح دربارۀ توانمندی ارتش دچار خطا بودند و به‌همین موضوع…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456401" target="_blank">📅 16:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عربستان: هشدارهای حملهٔ هوایی در جازان فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456400" target="_blank">📅 16:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8013f9430a.mp4?token=BckzX1liWAws3v5MYIYUlhPkRVmbct9dVMb-7GfmVhLkDldRVXBccKEFieMZ7uNJBiv4UJfAMVkYYGP2qqGoVYaLlgJ5Vr4kPK4H-qn2FZJWJtCPlezADVwkc7XNAkYOzJAEYSJlTK_iYmlG5O3nBtl9Hl2ooC244N696IlcbHLozGPHAfa4GMJpyYmcVSIykCGA-v03wBYLnKA31togqTuffQpOC4HFGHg5uqudSkZNw-3BP4G3GftN77BN80uKtGIMdVc-Fx1gT6TpxQGIZEDJ8awePRTheaVvdhMP472usHh-mZcCDbI20zKjokE3cejX368-LkJ0NV1jKofsrgB58hdd-ustmgb2tZ4QHTKiyA0hP6j1xAmHQ6vMRvE2tdghmm2sMTZyLOIqDAL_2CRSCEc6w8S8QQDxtqlIcNa7XEeFG_fLbQv9_up2uZJeSlRsyf3H9lHsPcAL8oFRDOm2EN40KxszKe7WgaojymXIwDsWCZ1kNvqWSuVg3-HrE2a8zb9VrTar5l7eVUe2vbXoCxML5Dr3r9W14KVUCiEP-Mc55ycHKbShvOyQeJwP97UcUOJv3m3IRq8xaysO6Rxf6ri64RVzzqGfLrgsayPhGnoj73XYkoAHzD0BPlhiOsmhu_WgbnNnlkydU4mP94lvYlQXBfV22M_FRNTY2qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8013f9430a.mp4?token=BckzX1liWAws3v5MYIYUlhPkRVmbct9dVMb-7GfmVhLkDldRVXBccKEFieMZ7uNJBiv4UJfAMVkYYGP2qqGoVYaLlgJ5Vr4kPK4H-qn2FZJWJtCPlezADVwkc7XNAkYOzJAEYSJlTK_iYmlG5O3nBtl9Hl2ooC244N696IlcbHLozGPHAfa4GMJpyYmcVSIykCGA-v03wBYLnKA31togqTuffQpOC4HFGHg5uqudSkZNw-3BP4G3GftN77BN80uKtGIMdVc-Fx1gT6TpxQGIZEDJ8awePRTheaVvdhMP472usHh-mZcCDbI20zKjokE3cejX368-LkJ0NV1jKofsrgB58hdd-ustmgb2tZ4QHTKiyA0hP6j1xAmHQ6vMRvE2tdghmm2sMTZyLOIqDAL_2CRSCEc6w8S8QQDxtqlIcNa7XEeFG_fLbQv9_up2uZJeSlRsyf3H9lHsPcAL8oFRDOm2EN40KxszKe7WgaojymXIwDsWCZ1kNvqWSuVg3-HrE2a8zb9VrTar5l7eVUe2vbXoCxML5Dr3r9W14KVUCiEP-Mc55ycHKbShvOyQeJwP97UcUOJv3m3IRq8xaysO6Rxf6ri64RVzzqGfLrgsayPhGnoj73XYkoAHzD0BPlhiOsmhu_WgbnNnlkydU4mP94lvYlQXBfV22M_FRNTY2qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای محله‌تان را بی‌واسطه به مسئولان برسانید
🔹
خبرگزاری فارس استان تهران در طرحی ابتکاری، از دغدغه‌مندان و علاقه‌مندان به حوزه رسانه دعوت می‌کند تا مدیریت «صفحات اختصاصی محلات تهران» را در دست بگیرند.
🔹
اگر در زمینه‌های خبرنگاری، عکاسی خبری یا تدوین استعداد دارید، می‌توانید به عنوان خبرنگار بومی، پل ارتباطی مستقیم میان مردم و مسئولان باشید و مطالبات هم‌محله‌ای‌های خود را در رسانه پیگیری کنید.
🔹
برای ثبت نام در این طرح رو "
این فرم
" کلیک کنید.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456399" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ تلفات مزدوران سعودی در حملات ارتش یمن به مأرب و المخا
🔹
منبع نظامی یمن: حملات به مواضع دشمن سعودی با نهایت دقت، به اهداف خود اصابت کرده و در پی آن، چندین عنصر وابسته به عربستان کشته و زخمی شدند.
🔹
در جریان این حملات، چندین انبار مهمات و سلاح وابسته به عربستان…</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/456398" target="_blank">📅 16:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJTfcxsjdva8dCIJ-NQciuZopk9SShw-ZGTC3pi-WYFeOUXlBzF67-KkIRIef9TtQXlmveOg1GoGF0IhiveVaQDXtnlgeDVD3_7fNoILfK8--f85jOn_Gf_dRxqkTRB8ElDNEAsT00G_ehSeEHIui_fS0fMUdrSxIvPYqY3hoYlPWL-j_ofwKdUGKTnwh_PI8ZPjtf7MKsRzKY1tY0VCrpMICKv8ZblbX3DYvdbJhnBxvLis-rLsYO0Noip1P2BTwVxul1Byx5RxBLRS1oCDWRSrA8sr_2tC7xKkFWd612ff_Jq4EiPlKDanS7OWCUUXwRqywaW1xJmg4mWKABfnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: تصویر رئیس‌جمهور آمریکا، تصویر یک بازندۀ بزرگ است
🔹
رئیس‌جمهور متوهم آمریکا تلاش زیادی می‌کند که از خود تصویر برنده بسازد، اما امروز کمتر کسی در دنیا او را جدی می‌گیرد.
🔹
تصویر کسی که از ترس خود را در کامیون مواد غذایی پنهان می‌کند و دیگر اعضای…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/456397" target="_blank">📅 16:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUL9NNEJiZ08oq4ZyRv2haN4ZM7oDpuRbPYLnbx0HbIohEc8Ws6M4ESWTlFWL-xt7LmzquZNut2OR5ZeO1L7IAkmOl85Y5WLjRkyKwra_E8d_Hut1DifeqkwjK977_yS_5ApB2fHN0c7ww-cBRINeFg_Wf4p2k9a9kH1ag1Ai2_gV05QsH-c1k2XFDkZt95XCVwT5Ld8fbYEUJ54NKHSSJ22IB8hr_kxBOY7wY5jndxb4hKGSFvwvkPjNYX0XrZ6FV_NTsfz4nLyA7R4wacqisZPe8cusMupxs26Ue56EhO-zPTlA-ufDdlvMrdCICrJKlgkJPZdvXhiuAqUSmjf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ میلیاردی‌ برای شکارچیان سربازان آمریکایی
🔹
فرمانده‌کل ارتش: با مشارکت مردم، اگر هر نیروی ایرانی بتواند یک نیروی آمریکایی متجاوز‌ را دستگیر کند یا بکشد، ‏از طرف مردم ایران جایزهٔ ۵ میلیارد تومانی‌ دریافت خواهد کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456396" target="_blank">📅 16:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456395" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و موشکی، محل تجمع مزدوران سعودی را در منطقه المخا و استان مأرب هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456394" target="_blank">📅 15:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ شورای مرکزی انضباطی وزارت علوم حکم اخراج رضا دالمن دانشجوی اخراجی دانشگاه شریف را تأیید کرد
🔹
یک منبع آگاه در دانشگاه شریف: حکم اخراج این دانشجو به‌زودی ابلاغ خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456393" target="_blank">📅 15:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e548a823a1.mp4?token=mDPVchFCrU1tycCr7196jT1ciLXFHV4dYnKTtmJRT6o98nS_Drdthw3H2eNEAR54bz5mh4AbT7T6fJFe0Rfk8sIVEmVxR7fcjgyjPP8_cG0Tsf5tKZJ0z2B3uM68iq5EsYnahsPKU_Xbr1OZ1oPOTuVROzLlJEmMraM5nksNu5LEkaQJbrHQgmUgNfELXiH_Jj4L8bKhl1t5ZGoZd5N5ajqlgj_OewHNdK2zJ05RDEii8YQqkHqjqazHa0FHC6rgQug85VvdahIVOivPiB4Bm6u321KsmlrUq9C0-jiw4EfA_AlMT7FGM4B6aoj8Faf036HmCrAfvv0makMfBM5D7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e548a823a1.mp4?token=mDPVchFCrU1tycCr7196jT1ciLXFHV4dYnKTtmJRT6o98nS_Drdthw3H2eNEAR54bz5mh4AbT7T6fJFe0Rfk8sIVEmVxR7fcjgyjPP8_cG0Tsf5tKZJ0z2B3uM68iq5EsYnahsPKU_Xbr1OZ1oPOTuVROzLlJEmMraM5nksNu5LEkaQJbrHQgmUgNfELXiH_Jj4L8bKhl1t5ZGoZd5N5ajqlgj_OewHNdK2zJ05RDEii8YQqkHqjqazHa0FHC6rgQug85VvdahIVOivPiB4Bm6u321KsmlrUq9C0-jiw4EfA_AlMT7FGM4B6aoj8Faf036HmCrAfvv0makMfBM5D7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456392" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456391" target="_blank">📅 15:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
تعویق انتخابات شوراها با مصوبۀ شورای‌عالی امنیت ملی
🔹
رئیس ستاد انتخابات کشور: با مصوبۀ شورای‌عالی امنیت ملی و درپی شرایط جنگی، انتخابات شوراها و انتخابات میان‌دوره‌ای مجلس و خبرگان به تعویق افتاد و زمان جدید برگزاری آن پس از اعلام پایان جنگ تعیین و اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456390" target="_blank">📅 15:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در خمین
🔹
به‌دلیل خنثی‌سازی مهمات عمل‌نکرده در خمین طی ساعات آینده احتمال شنیده‌شدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456389" target="_blank">📅 15:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0207f5fead.mp4?token=PilM7eqvY8Z0Cid-NfSQCbZOob8Ocbe6I1KK24t85XxWDME3naYjx6moKMpx8vFARLTkgiNhADv9zj2dC61QWo9uINTqb25F5tn2F0be4Ea-9N2vTyLOxdYR_dSCTZpuZw1pGo00hi9uglG1DNe-Q3s6IdWdvaB_vKCYtcQRN9_JTpavUOT3292J_XHCKziWYmLyvcU4_zO6ygMxl98cCtepMCGDZFJqERTByx6QKi0m3FkFFKawj6iyu9XxicwYTxgjELWS3bbYY4L3irgcUf4xCQQq3qrpQmDP7c2Ht_o2oCo1fQ4YfdO1qtO64izRhtDD2URXKgBplfv8uG6CRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0207f5fead.mp4?token=PilM7eqvY8Z0Cid-NfSQCbZOob8Ocbe6I1KK24t85XxWDME3naYjx6moKMpx8vFARLTkgiNhADv9zj2dC61QWo9uINTqb25F5tn2F0be4Ea-9N2vTyLOxdYR_dSCTZpuZw1pGo00hi9uglG1DNe-Q3s6IdWdvaB_vKCYtcQRN9_JTpavUOT3292J_XHCKziWYmLyvcU4_zO6ygMxl98cCtepMCGDZFJqERTByx6QKi0m3FkFFKawj6iyu9XxicwYTxgjELWS3bbYY4L3irgcUf4xCQQq3qrpQmDP7c2Ht_o2oCo1fQ4YfdO1qtO64izRhtDD2URXKgBplfv8uG6CRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رانندۀ خودروی مرگ به آخر خط رسید
🔹
اولین تصاویر از جانیِ بی‌رحم چهارراه گلزار کرج؛ عامل جنایتی کم‌سابقه که فضای مجازی را در بهت فرو برد!  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/456388" target="_blank">📅 14:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFWzpuCedKFMfhryv6AWJCUysIYROtBws5Jbze5vSiVIZd5g9GwrV_vv_yf0MjFhbP-mxPMngOJo3BXjyX-mhrAtrTFOUyGcE4sjJ4WAPqZT4qj9fhz1rFOq4IKqo0V9RDVthl_bdsSGw9zsKxa8xcKl6IIEIlKw-lu8So21EfV7w6YHIwPd5e0-ig6lgf_1y2upd0jVAYhelZYhcdi4dB_loiM2C3Ar4o2ACJ1tBeSBWCAicXS6zbsfgcHp8ThBL1nw14Tk3ZvvKHw6BxzuOS7eCObXGBf2p7PkD5m92drQMHDNulqXSJefzEg8DXUkDQObycVZJT6qG9Td8a-NEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقدیر فرمانده کل سپاه از ۶ ماه جهاد رزمندگان اسلام
🔹
شما در گرمای سوزان جنوب، سرمای ارتفاعات شمال و زیر آتش سنگین دشمن با عملیات موفق آفندی و پدافندی، مسلح‌ترین ارتش تاریخ جهان را به زانو درآوردید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456387" target="_blank">📅 14:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uds4FCQt6tJwwJ2vs22lv2PKHpILigKU-2jEDhLf9h_RzFWGJl9YZ5iQgpdbHBMT8-_PmGjpZGImiCZSEkwW-ciPm0WvEG2AjbDkQkvqnWP3T4xLjEKcFGVlwwN2cYnJ7RSoqwrRTwk5cVeWgU912CYEY9hFQV2zJ8jlrPAY76PC54B0RxTsAbCtOMMDIb0kxOEb9inKMe6EB9TFxhojT6K16OsSW3SzR9kzx3qHcgE3wQbGa00J8UtWzpXftx0lcVFKV7bV33UmRzINccBzrSGWDiA49oGiOvkPIi9XFmhaL_9pCNT8A_To9D5yFtZUm2XPMv5cMG-9n7nX-wdAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ فرودگاه قشم دوباره روشن شد
🔹
فرودگاه بین‌المللی قشم: پس‌از وقفهٔ ایجادشده درپی شرایط موجود، از چهارشنبه پروازها آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456386" target="_blank">📅 14:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XydYAd81QwtC1WSb2yVoKSp7kG61dSQZT9eu2b4FwWQ0VJeZrLOqgMN7TBzGvPKNR7J1ETC0I1c1s2eDbaAvNeCVcdoN4_evT9FPpzOG8s2s_BrlpJlnHlogpl94eChnY573ku2h933I-WXCHHuew7-kK36Uv-OU7Pb3NLsbGrYfIC6j7e-jJNTcPjC02z-t11PLgrxh7SaFgyKyc5Wxfy5Wqg37RV5NHgnNU6iyY6y3U37qvhOSu3HPEO57PSJp-GSERT2bBVm3PUcKpj7Qrd9UhfA4EC_1Pqo_B9m3zPorgwJhOS4jCHs7SKbG3M4bmtPsJbgNZern36MbOJlJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ میلیاردی‌ برای شکارچیان سربازان آمریکایی
🔹
فرمانده‌کل ارتش: با مشارکت مردم، اگر هر نیروی ایرانی بتواند یک نیروی آمریکایی متجاوز‌ را دستگیر کند یا بکشد، ‏از طرف مردم ایران جایزهٔ ۵ میلیارد تومانی‌ دریافت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456385" target="_blank">📅 14:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حکم قاچاقچیان ۱۰۷ میلیون دلاری صادر شد
🔹
دادگستری آذربایجان‌غربی: حکم قطعی قاچاق سازمان‌یافته ارز به‌ارزش ۱۰۷ میلیون دلار و یک میلیون و ۱۰۰ هزار یورو در دادگاه تجدیدنظر استان صادر شد.
🔹
در این راستا ۳ متهم به به‌نام‌های حمزه کردستانی، محمدامین کردستانی و مصطفی کردستانی که با اسناد صوری و ساختگی از بانک مرکزی ارز را اخذ و در بازار آزاد می‌فروختند، دستگیر و به ۲۵۰۰ میلیارد تومان جزای نقدی‌، حبس و شلاق محکوم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456384" target="_blank">📅 14:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e11c685a.mp4?token=BS0KlOBGb-Hgq9UXXtjfuygJm1goWY6iuzE_CP78oIxKyfFVeNhGF3Eh-UBppsmziN0PRa3-3MTlpRaKCXfUUztGUQUebKguOUfDMxvFqzSsVVDAoQQHsoPHyKNHWn3ygIZidCVXNcSlCd1ct8jzTlXzfw4I3M2dQhd1nsLUNSjqqtwJYp05_fSc45HxCJVudPGbAVbUyhAtbC7u1SzDpp_h4crIKW03etMI0F6jBGp1bBntIxS-mtQX7ILT7iLqZQwHmUJdVyYt6JexfNDpnH5rmhN2zgnydwfjhaWHryBNJwUSbR7zsdYjhlAUWhM2fvXum6eFb1YB-uU0QFhdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e11c685a.mp4?token=BS0KlOBGb-Hgq9UXXtjfuygJm1goWY6iuzE_CP78oIxKyfFVeNhGF3Eh-UBppsmziN0PRa3-3MTlpRaKCXfUUztGUQUebKguOUfDMxvFqzSsVVDAoQQHsoPHyKNHWn3ygIZidCVXNcSlCd1ct8jzTlXzfw4I3M2dQhd1nsLUNSjqqtwJYp05_fSc45HxCJVudPGbAVbUyhAtbC7u1SzDpp_h4crIKW03etMI0F6jBGp1bBntIxS-mtQX7ILT7iLqZQwHmUJdVyYt6JexfNDpnH5rmhN2zgnydwfjhaWHryBNJwUSbR7zsdYjhlAUWhM2fvXum6eFb1YB-uU0QFhdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال جالب از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456383" target="_blank">📅 14:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=lLJtDW_pDPwBe3fvJhpl_1Wt5DmQicLNNIbjSdsvCZ_K_fnxvUK3KCliwymf1quwwdoMSZeGUhqaNJcgrcE_behoPcWldQdP52hsnuDenX0rdMuXljfhiw5DIjKLPCeBqHwFNXrFZR15qLmH0R1MGxmLXh6ApfLkJB6GAl_eerydNBeZXmeSX2uSnWknoH_kmbPEh8JQUWGHbRpApIuKyU3jbjmScjTBM-3pSDV7EA7EDh8k55NuNK7TltH0e7y31xb1YhVKDHwDpt6qtFz_lZ7U8-ZKARFWD0eECXyafzN6J7iKIj6W8Se7kPXLQ-K8sSFX0acFiJKkSo2f7-8iVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=lLJtDW_pDPwBe3fvJhpl_1Wt5DmQicLNNIbjSdsvCZ_K_fnxvUK3KCliwymf1quwwdoMSZeGUhqaNJcgrcE_behoPcWldQdP52hsnuDenX0rdMuXljfhiw5DIjKLPCeBqHwFNXrFZR15qLmH0R1MGxmLXh6ApfLkJB6GAl_eerydNBeZXmeSX2uSnWknoH_kmbPEh8JQUWGHbRpApIuKyU3jbjmScjTBM-3pSDV7EA7EDh8k55NuNK7TltH0e7y31xb1YhVKDHwDpt6qtFz_lZ7U8-ZKARFWD0eECXyafzN6J7iKIj6W8Se7kPXLQ-K8sSFX0acFiJKkSo2f7-8iVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال جالب از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456382" target="_blank">📅 14:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انهدام شبکهٔ انتقال اطلاعات طبقه‌بندی‌شده به دشمن
🔹
پلیس اطلاعات فرماندهی انتظامی تهران بزرگ اعلام کرد شبکه‌ای که با سوءاستفاده از تجهیزات ماهواره‌ای «استارلینک» بستر ارتباطی غیرمجاز و انتقال اطلاعات طبقه‌بندی‌شده ایجاد کرده بود را شناسایی و جمع‌آوری کرده و متهم اصلی دستگیر شده است.
🔹
متهم اصلی این پرونده با هدف سودجویی کلان، این شبکهٔ غیرمجاز را راه‌اندازی کرده و علاوه بر ارائهٔ خدمات غیرقانونی به افراد خاص، بستر انتقال محتوای مجرمانه و ضدامنیتی را فراهم آورده بود.
🔹
در بررسی‌های اولیه مشخص شد که فعالیت‌های این شبکه علاوه بر تخلفات حوزهٔ ارتباطات، مستقیماً امنیت را هدف قرار داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456381" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daKnWTZODKym_EoDaVyqtk9u2Jd_84_0cRM2UlGHuxk-jOxZ5zaN1s2ManNy_rYJwvFgPk7ZPPW1zFA4PtbpmOejIT-wf7jG5ep7w7Lbr5t0E_rPn9-E6RYpCjZ_hjXKwNYv19R3cnNpD9sEx11DMpr-vCY5SvDmqSr3PvE-P-qccYLlVr2A43WFw6zRl3IzJ2wbmORu_vvCcescqHICML-7UD_XiVoYqIJgR24yu8vsxfkoalNs7tougUjcPoSLaCptaVgS17lz-eSBQkzyb1NRZLQ1dp9FlJOJc8eIw1cxUH7u22cnYrxCoD0nH5VCablGNVdE-xAGtEDIcFE0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
آمریکا و اسرائیل با ۹ هدف مشخص به ما حمله کردند اما به هیچ‌کدام از اهداف خود در هیچ سطحی دسترسی پیدا نکردند، این بزرگ‌ترین پیروزی بزرگی برای ما بود.
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا و رژیم صهیونیستی قرار دارند، اما ملت ما شجاعانه، مردانه و خالصانه ایستاد و جنگید.
🔹
بنده به‌عنوان برادری که به جزئیات کار آشنا هستم با همۀ وجودم می‌گویم که ما در این جنگ هم در بعد نظامی و هم بعد سیاسی به معنای واقعی پیروز شدیم.
🔹
تفاهم‌نامۀ بین ایران و آمریکا سند افتخار و پیروزی در راستای تثبیت پیروزی در میدان دیپلماسی است.
🔹
البته معتقدم که مردم ما حس این پیروزی را به گونه‌ای که اتفاق افتاده، حس نکردند و در برخی موارد نتوانستیم این حقی که مردم داشتند را به درستی ادا کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456380" target="_blank">📅 13:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3dYg_aTdUpcP9N0Pn786c8JYCWZkTbfAIsHYQPTMe4ULzXDIgVg5tMPO6i-j21btS2xV0UaHdW3zk_jopjDg8HVxjlHmNUQix_C-kSfSSJX10pqAPQk7xeMrJ2NWVzklqXQ-jEzB6dfr1FWG9SzbdLmnRSUfRchPZIqlyBsHcSMAt-IagtnQFt8qtpcxoU7eGLkoyvBf_3kYXBy5rgSUxMXjbHoGbMcOcU_sNlsTTIw4gSoRwxPR3WeS5DFQbGtaq-qQuqmFDqqj2iIPUFywpYwm7JHK3rlDUmkhTdoWtQSYTaMeQeismZl7TH1LfD1oTpBOTpr9WVd31XkSqcvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ترامپ به بازگشت به نقطه قبل از جنگ راضی شده است
🔹
یکی از بزرگ‌ترین مشکلات دولت ترامپ برای خارج کردن آمریکا از جنگ با ایران به تحلیل سی‌ان‌ان، فهرست اهداف بسیار مطلق و حداکثری‌ بود که او و تیمش در ابتدای جنگ تعیین کردند اما با ادامه‌دار شدن جنگ که اکنون وارد ششمین ماه خود شده، فهرست اهداف شامل تسلیم ایران و تغییر رژیم به شکلی محسوس تغییر کرده و محدودتر شده است.
🔹
طبق این تحلیل، «به نظر می‌رسد معاون ترامپ جی‌دی ونس هم اخیراً به شکلی قابل‌توجه از دامنه این اهداف کاسته است؛ موضوعی که تازه‌ترین نشانه از آن است که دولت ترامپ ممکن است خود را برای رضایت دادن به دستاوردی کمتر و شاید بسیار کمتر آماده کند».
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456379" target="_blank">📅 13:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c0d2f05e.mp4?token=cyJ5wWBT8V3p7qWbiNkV0BziNk0s1OnFkvyc3GNMySAqer0lJEBIn-sGQ8w9zQ8OlVrz9WGpPiNuijFrSHeoDlEf2gAtBQ3I8mwPLBTrJcKQPWFMP0Da-c_Uu3-rSJqL9eS9l43YrXPfrK60pKrNXJACBbgDeHcyPWAGBqmdNMOxjBDZ9cwqgvedmO91AJeeHgzMabHB0-5Es9eQyfhL-KVvBO4zI1gPLRRq1cgLczI6SRO5tNJlUeB0NuDKUatR_UCDtsWeGPmXqr84vtEqGdymUw8s7rlcu8SHdSLec8A0Lw9S91YEgHyJ-ex1-Wy_ZkEO82-Dx16EcnHU-XBZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c0d2f05e.mp4?token=cyJ5wWBT8V3p7qWbiNkV0BziNk0s1OnFkvyc3GNMySAqer0lJEBIn-sGQ8w9zQ8OlVrz9WGpPiNuijFrSHeoDlEf2gAtBQ3I8mwPLBTrJcKQPWFMP0Da-c_Uu3-rSJqL9eS9l43YrXPfrK60pKrNXJACBbgDeHcyPWAGBqmdNMOxjBDZ9cwqgvedmO91AJeeHgzMabHB0-5Es9eQyfhL-KVvBO4zI1gPLRRq1cgLczI6SRO5tNJlUeB0NuDKUatR_UCDtsWeGPmXqr84vtEqGdymUw8s7rlcu8SHdSLec8A0Lw9S91YEgHyJ-ex1-Wy_ZkEO82-Dx16EcnHU-XBZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آفتابی‌شدن ۲ پلنگ ایرانی در حیات‌وحش بهاباد یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456378" target="_blank">📅 13:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9NCtNrXVCRFx4lzGCL3HIdiH_7cDyeAYMNWO8If0FUNOtzGxT9KheYv1BDvn1TUBgxz7G2vhwTP2UAa2IeAzGqgi-SgA7nkPTIY59coIzaYAv3W6NmXw1edPflcFpRvO5t14KBuV4JJ30-kTKkIuWOv22j79z3WVpxN6FCOkGpUidIW_qGZPOvKBI7e-jOcvcrTtl9DI6jMBcT0188aI-hGEfUgTKRHAxfcEuU_7Ag2Zk-QA0hMmZegmOJvC4h7uuLiBNC-WPzQPJ75Mk76wLDjM0s10MzQ44VLZZykr4A8nbl87yD847LkoKa7YTiJ5lFr10GKz1kXqnpw5GKASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌کل بانک مرکزی برای دیدار با مقامات بانکی و اقتصادی عراق راهی این کشور شد
.
عکس: فرج صمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456377" target="_blank">📅 13:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNJJYJZiaKpPW6iOodfOzWvCL4L2g8-dddd_Cr1EOkpfRXdhRisd1yOVyFl0jhJfEAkW7h0gQM1lk8nvqXV-mYtw6RVQG9G8ntTB1J_cN8TNoDpdxMHEXH8_rew2fqugn2jAsvds-aPagE5NU0-dW1QckirMb0VJk86bCap4i-HeZDZvMUYxPRhHn_fU5Zajcjg8Il2nwUK5wfW_QeJNIsUqhZ6NXRpD7AJh2LKIZCnlnNSJp4pWOsxcZKBjOOf2xmqN7NtKrdcEir6EMIyUvAF_KADgZ6lpdWj-3LzT5MiH3gKh7SxaFmJWWbaCCnOfr-5TF8sNwJjZUavBF1tYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدبه‌زندگی در ایران به ۸۰ سال رسید
🔹
معاون بهداشت وزارت بهداشت: امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456376" target="_blank">📅 13:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba7c9e929.mp4?token=WNxLJHIeFuIZBHQYD96pPewXRAgDNR19XiHhYoKoujTdRNEhlxDm61ugVHai6-vyVEtrxiGjo4-aY97azc6NJQrgaQV4K5XGcpZduMMlJQTAvnYl5WnS_G9QzHT49AWg-Y3rfG4YYAlPsGXwQIJeXIUbePxj_xZfMDVjL5PxRB9mjwMXMi5A0hB_re3d89SVa4GilERNoztTb_lQ2mbPqQA-hmARwFDSAg29Lfg57Ny_wngUHzP3t8Faf_bjljrgr2VUica5l0j3bY-kgTMQIbPoOnMY3iECtLb3V6F4oRCjKM6UFSbRx3qFjJNhWXO3IW-MaqVLbFKi8qOvpkk1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba7c9e929.mp4?token=WNxLJHIeFuIZBHQYD96pPewXRAgDNR19XiHhYoKoujTdRNEhlxDm61ugVHai6-vyVEtrxiGjo4-aY97azc6NJQrgaQV4K5XGcpZduMMlJQTAvnYl5WnS_G9QzHT49AWg-Y3rfG4YYAlPsGXwQIJeXIUbePxj_xZfMDVjL5PxRB9mjwMXMi5A0hB_re3d89SVa4GilERNoztTb_lQ2mbPqQA-hmARwFDSAg29Lfg57Ny_wngUHzP3t8Faf_bjljrgr2VUica5l0j3bY-kgTMQIbPoOnMY3iECtLb3V6F4oRCjKM6UFSbRx3qFjJNhWXO3IW-MaqVLbFKi8qOvpkk1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456375" target="_blank">📅 12:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7wRQS4JrAWmXFzAPt0LBPeqLn_JjEOjOJ6Zd1oz1P8st9qiNDNQGcz_CwJuh8Zut5L6tt5rdeuJxLyxrgnT9XXAiR7NH2OqXa8wmGHDoOpI0ndnmzO7ZLabXI_odHBFO-6G8DcXfJW1PMWkWf9Mg3pqTzbdW38l6jgHOQGRBbwojMmltv2bbi3ePbdPnk7EdZrv5r-Kjf-4olEQctDW5tClYdLESyfffRUjhkpKn-7m10CRi4SsvdaNIIH0gFHoueBGiwauMU0qokCeBaaDeuTwxF0nyH7W4SH4mwQd0ENeGqBhlMucUyWlHyFJzx1288dzxSh8b0q-Kz_yymJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی به ۵ میلیون و ۷۶۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456374" target="_blank">📅 12:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCldZ71L8H1BwEY5CbudEkDHXa9cWwwJZBNaCRbG4ozRzH0KcxmMOIR63S5mEL4COKTenNH_9slYVEu-m1m8JxTRPcKx9WMeTWL8QWbGso8NheEyR8w0kvNUl7RlgbGEzjs4y6X62Qq2n0eTceASxJwcm99c6lREHhM5g3HpaZERwAwZzP07d-m0JbTfLzIvYrD_n_p_oxUZcItf714hiYf8uWn3iCCHTlPoi1urVrIeTYfMMnHbxp0-1e43ZseIy_jNIAVFJyoyaF9r3BWWp0tBWnfLrB3eKVnnnygnY6U6P-sYL_oseWIn3NZyV37G9rIz8bLMfUvGy4bxV51sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn7rBpWMoaXXOg04A4SWFBunupDCbmR7U5mUoxH7tjRiJjtA23mTD2yqzwaMtfY7FZ1o4fmDZYsIpYGyGtcbW4oPoYVEsFKqrpIOml9u04tgaXXqem66eiGfptWxCsr627BntFUaBlY1YgYfrTG0LbkLk8_oOWizukc-fw-Wy_gHx9WOHJmxSCxxf8Uv-96yDHu9XxkW7fY_p8gaiqxVARfqNW4LBwJDuoP7sU902Jef0YbQZhAsb3BQiGcdpMmZfB1uLdfCqCOkZnwJIaA0T5HmER6SVD2ScyaYg3TCqhoIb76FCgnLM2ykZdJOiUyOP29FIUfuz-3OeyDrNtjL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rK_brezIVR-SQIn2iPeetq9v2Eb4IU2uyVlTgV0avmO2W3mREfrpZW9RdZ1nzG8I4YzeigRck_hbwKYjskzxbCuGC9LJxWnt-fbScAvh4m2bwoV3oXiLuca1wFnC9-MFMwkIg52Bxcnjskde3xhY_aKlmtylIXV-Pu09iWO_a9KK50HorkjblFayChry904nVzzKY98SFC6mRu1qU54Q7L1qjV-T6OIJx5OyDCZfCsau6k8HxBMamI0lEZEqC9t598XuR41denYDHmAehq0GVs8-lLJiJ4kN-IF3D5VojG4ChQ0EQc4pX43I78lRKEAd1eHv6QRgjoAHoHCtP10v_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_65FR6RijYdjDKJH2GV1zCJ9ltvSLrA_fzxdFASMHJGO8SWfrhG5Zlucd5wN5dtIjAJIsk6oRzlG6UQhDI1_cOuIBJM22JmGP5DpaPxM3y6qhLR-7HE4VHIPniqeonVYt-64781KepLIUAyM8FB7YJaB95QHzXZy7mOdHlnd6-sfVo9aCEdGxH6cSGzOkxaJKFwn-RKslaEu4tlv2LmtQgsGD66phs7S52Qo7JroOiJN4hcBin4RdDekoQ5HlVRHEOmtIcMEu_J1EWVzw6Wnc_fA2PZobvhJPmYcyBoIeLiFUAvpR4XPoFTsdnewwK3ByiMgB2y7rMTJC0lT7m7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYpq0t-8s5J6TcbDubSWDbARCE62voExMBO3Lt6lW6HZb_Thc5qsZWO3LpQWF55vt3z8KocndJ2Kp_SQCXdrwkgh2o9WfCrxKasXIzZKb9yg-UTsZ9HDt6JTuKrINEQJBUZwtAtVWsfaDtBF9MjMrI0vozM-ub4GltSmbPK4cqu8599TRsP6EGwnltQ_LdIO00L86gKyJ3ET6blpR-_QQ7nRyXoRkX_8svsbHCzeB6RnYvAXSXOyvIXDS-5CMfKcOz-IO9zYROr35D7m4VIvuqHNcRk5NECZZxojFAlmnhtsBnN00ZFp8typfB1cna-yv1G57ZYHi3gR7XKKvsgPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dR8ZbT-cr4Z9VVlL5nVjELln4J_ul36FrxX5uxN4wN9UplyuQHXyzV6SU_rb0oaHFqSyrHy_mWGRK8EsZyqE5eCr-4ODnd5wP7Es80d8lkrPxVpenTafotIkNJIXTRdx1qTqBaQlJCXIP71b1Wom3mMckMmxyUV6ESd7FozU1Uy4Eoj7WIgrW71sN5GbX-LqERBKBOW5JfOOrMh6cNqjQrYtBoe-BJudkaHDp5Nrb9pgKjkQfVL6k24mwFH44UZGQyq3Hxm5_g8yJKPWwFerB4oCxB3Q2pa-XpvU4u4Av06mNwZ0JNgaAIshetyh8pzHVb0eiuDMptKoxLDI_Yr8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFW5qeyrpKaA75l5DcKTH4Vphbmb6X7pZJn_188jk-8iIc3AKvhFoao55X6eWkA3z-YxG9YbE0taeDt6pHzDpl781v70fU_b9tB1_8Nn7MWTaCzC9V0VfKwjAqmQtCZ007qKw3wFbbmD9hcpf7_NOze94mcdIsmoMgQ1Pd1W7aWL218g9m3R92Zz_V_hilaMP2R8mSH68LJ4CC7IDsNLbQ9pSgEcYoVctUEa3HA38runzcYRBzFCZLUhO-fuhtwM_pPahJdEH2TnejHYqmmAQ1EWI8E4PiCWk0sL7G4tH6KLn7S2SZJ7wgZ5P6LY_mwXQ3qTXnkCh6csyMqAGHyuPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: کلیات طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456367" target="_blank">📅 12:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smf0OtcZp6tzatUTWy5shz12EYDOQNXl31yZSvRBsfCoKFZEH-9HG_yNnIRshnUf48ZTwfepe7R0MZxwF4LZNsBo1vMmBgHOSaa2RmEuoyD0I9p7oUrZPk2YkEAG--EOriEIB_FYEMUL1q-F2yx_8FnbmGImFXONcmMim_wGG_Fw_1RNDEbsBV8fii8AJ3vY6tLV7cJDpU8rEPNeSiU9ogXT5CEyUwTCZ6KEpHPg9oH8jYApuaWMgAuSNq8wLrcPSog_AA2_1pKUHc5mUSOrsbDthwpi5eDUvtbqq59yuyDJWW9m7ElP3AeRTXki8lO3CRjeIcWlzE5TBorx9JS5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آغاز ثبت‌نام بدون کنکور دانشکده رسانه خبرگزاری فارس – ترم مهر ۱۴۰۵
🎙
ثبت‌نام در مرکز آموزش علمی کاربردی دانشکده خبرگزاری فارس برای ترم مهرماه ۱۴۰۵ آغاز شد!
این دانشکده به‌عنوان یکی از مراکز تخصصی در رشته‌های:
📰
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
با بهره‌گیری از اساتید مجرب و امکانات پیشرفته، بستری مناسب برای ورود به عرصهٔ رسانه فراهم کرده است.
✅
شرایط ثبت‌نام:
📌
داشتن مدرک دیپلم (برای کاردانی) و کاردانی (برای مقطع کارشناسی)
📍
ویژهٔ متقاضیان استان تهران و استان‌های مجاور
⏳
اولویت پذیرش با سنین ۱۸ تا ۲۴ سال
🎯
پذیرش نهایی پس از مصاحبه و استعدادسنجی
✨
مزایای انتخاب این دانشکده:
🎓
مدرک معتبر وزارت علوم
🛡
معافیت تحصیلی
💳
شهریه به صورت اقساطی
🏦
وام شهریه دانشجویی
🖊
امکان عضویت در باشگاه خبرنگاران توانا
💰
امکان کسب درآمد از تولید محتوا در باشگاه توانا( مهارت و درآمد)
برای ثبت‌نام فوری، عدد ۱۴ را به شمارهٔ ۵۰۰۰۱۰۱۴ ارسال کنید
یا از طریق لینک زیر اقدام نمایید:
🔗
edu.Fna.ir
📞
اطلاعات بیشتر:
۰۲۱۴۲۰۸۲۹۴۱ – ۰۲۱۴۲۰۸۲۹۴۲
(ساعت ۹ تا ۱۷، شنبه تا چهارشنبه)</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456366" target="_blank">📅 12:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صدای انفجار در مهران مربوط به خاک عراق بود
🔹
فرماندار مهران: صدای انفجار شنیده‌شدهٔ دقایقی قبل در مهران ناشی‌از عملیات معدوم‌سازی مهمات باقی‌مانده از جنگ در خاک عراق بوده و هیچ‌گونه نگرانی برای مردم وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/456365" target="_blank">📅 12:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456362">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bb10a8de.mp4?token=sJ1tMv39RP5KzP04dhTx6omV5vMMCf-9L7OP77pMh23XD0I6uzIlH_8ILi7ZIJKz43i6uFsXmhZQPchJ12s5y2KmOo9Naear-y4AFZ3oSWGRf7FTFuXVCqYZS97lH29zccCisggouwuJFBcRp23wkGAlH321XqlAIeBVunlgbehbTN_Vkdmxcd79lN69XpF3ct8ERBGgUker1gWrd1CNI0QLXq9j1E0PU1OwLuxf9uP4bM0ZHoOCr53wMKH3L0KsB4D-pSQg1YfYwqa_9YjCGDqe0Kbs_V-QqkObiEN1U9lr_mk9aq5QIthdprsTFQWJG2hq1JAOn9ky_qWhNxEQlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bb10a8de.mp4?token=sJ1tMv39RP5KzP04dhTx6omV5vMMCf-9L7OP77pMh23XD0I6uzIlH_8ILi7ZIJKz43i6uFsXmhZQPchJ12s5y2KmOo9Naear-y4AFZ3oSWGRf7FTFuXVCqYZS97lH29zccCisggouwuJFBcRp23wkGAlH321XqlAIeBVunlgbehbTN_Vkdmxcd79lN69XpF3ct8ERBGgUker1gWrd1CNI0QLXq9j1E0PU1OwLuxf9uP4bM0ZHoOCr53wMKH3L0KsB4D-pSQg1YfYwqa_9YjCGDqe0Kbs_V-QqkObiEN1U9lr_mk9aq5QIthdprsTFQWJG2hq1JAOn9ky_qWhNxEQlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ مجدد پهپادهای اوکراینی به مسکو
🔹
اوکراین یکی از بزرگترین حملات پهپادی به مسکو را انجام داد و انبار فروشگاه بزرگ اینترنتی وایلدبریز (Wildberries) را به‌آتش کشید.
🔹
وزارت دفاع روسیه اعلام کرد دیشب ۸۰۰ پهپاد را رهگیری کرده و شهردار مسکو هم اعلام کرد که «دیشب ۶۰۰ پهپاد به‌سمت استان مسکو در حرکت بوده‌اند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456362" target="_blank">📅 12:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab8c1799f.mp4?token=K26CA_8QQTe95j8Y-J7TkXrwuATSIkzgHN0vNrsW57k8qFATnYLLd-PBsxkMIMrFuICccyzeuNmZGsb2j7AfKTW5g3NwhhQ3VkISSbicPbDdki3K3azThx7iBPzcoXjOZ32ek-jCXQgKbHtcEgwkti3rIp9rU420aA6v0VB5QQPJJSAEkuI7k4tBfq9oVTC8iH24rcPi9a4hrtnwiEmUZYJiWJ_MV4pFmQ9BWGoB6AqfoHOvsxeKrnupqCGcgFZZpE6aBwdqdiIbEtDHHTdKKn0coXEzrwH_ZDlBWMw6GjRAekLEDy3aNOqy9OXFwz5fueg7yRbLN1T2JpYv54Salg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab8c1799f.mp4?token=K26CA_8QQTe95j8Y-J7TkXrwuATSIkzgHN0vNrsW57k8qFATnYLLd-PBsxkMIMrFuICccyzeuNmZGsb2j7AfKTW5g3NwhhQ3VkISSbicPbDdki3K3azThx7iBPzcoXjOZ32ek-jCXQgKbHtcEgwkti3rIp9rU420aA6v0VB5QQPJJSAEkuI7k4tBfq9oVTC8iH24rcPi9a4hrtnwiEmUZYJiWJ_MV4pFmQ9BWGoB6AqfoHOvsxeKrnupqCGcgFZZpE6aBwdqdiIbEtDHHTdKKn0coXEzrwH_ZDlBWMw6GjRAekLEDy3aNOqy9OXFwz5fueg7yRbLN1T2JpYv54Salg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استادیار جغرافیای سیاسی: تصویب لایحۀ خزر خطای محاسباتی بی‌بازگشت است
🔹
کمری، عضو شورای مرکزی جبهۀ شریان: تصویب کنوانسیون رژیم حقوقی دریای خزر در شرایط فعلی می‌تواند تبعات بلندمدت حاکمیتی و ژئوپلیتیکی برای ایران داشته باشد.
🔹
تصویب این سند پیش از تعیین دقیق…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/456361" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOLb76DvSrtxPZ8SV4Jn40ojphJ_7K09UGGVciQuitufmhbx1s-zdJU4paFOmeLq_63FihTYexzce-1W5Ja9_5Glf-zvNfKtgEJmS--XdVXm95ny3npEfY1VqXJepwJfa2P44s2BADg0R8wI3TmAk3S7S0wFM6ccN8BI5GWix3GhvCIOZVS3muHrNpZBhw05ttLQIf3AAU1t5AsUB7mKehR56-L2fThBO-1grSe9gSyo8inEplLy0-BLT0whi0g5OWCKdFWC7D0FujIjhU5BkSUrcn41N1FvarmSOwUl0b3ZjI5EY2ZXyd8l7I1kd43b-7aWzbSACwMhFjYJQsHg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت عراق برای هفتمین هفته به آمریکا نرسید
🔹
ادارهٔ اطلاعات انرژی آمریکا امروز اعلام کرد آمریکا از اواخر ژوئن سال جاری(اوایل تیر) تاکنون هیچ محمولهٔ نفتی از عراق دریافت نکرده است.
🔹
این درحالی‌ست که عراق به‌عنوان دومین تولیدکنندهٔ بزرگ اوپک، به‌طور میانگین در سال ۲۰۲۵ حدود ۱۷۹ هزار بشکه در روز نفت به آمریکا صادرات داشته است.
🔹
علت اصلی این توقف بسته‌شدن تنگهٔ هرمز است که صادرات ۹۰ درصدی نفت عراق را مختل کرد.
🔹
تلاش واشنگتن برای جبران این کمبود از طریق بازگشایی خط لولهٔ کردستان به ترکیه نیز به‌دلیل مشکلات فنی و اولویت صادرات به اروپا مانع از رسیدن نفت کردستان به بازار آمریکا شد.
🔸
براساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرهٔ‌ استراتژیک نفت آمریکا به ‌کمترین میزان از سال ۱۹۸۳ رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/456360" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=pzjHF_WcRKWv08n_OS7D1NB88BCt1PdKOV96BS0VVjsAZO-U6i-xNrhecpG1JILONqym9No4ZWAnwNSBLdQ_u_hWU_ygwpinFYAsdPBavvjyxiyCacG-ecoy4dLRRMEioJmwQRqKE1BANGOrr9Vavsoky8JHoixKQ6IHotQ0KSQ50t5OtwyPJZEX8C_JQPgNqCiUfWpActsxGslicjti1b-XsfShRInbOR2Y8Ug_1uW68sLCB_xujbKitVqTiD_WDx2i-_icz9PapPLOZYOU2MEL2KRYP8HgoypOy2lPVAywGuPfHUznW5NF6dSgMW0cC-y9O8iSCb-9sQSq9-wmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=pzjHF_WcRKWv08n_OS7D1NB88BCt1PdKOV96BS0VVjsAZO-U6i-xNrhecpG1JILONqym9No4ZWAnwNSBLdQ_u_hWU_ygwpinFYAsdPBavvjyxiyCacG-ecoy4dLRRMEioJmwQRqKE1BANGOrr9Vavsoky8JHoixKQ6IHotQ0KSQ50t5OtwyPJZEX8C_JQPgNqCiUfWpActsxGslicjti1b-XsfShRInbOR2Y8Ug_1uW68sLCB_xujbKitVqTiD_WDx2i-_icz9PapPLOZYOU2MEL2KRYP8HgoypOy2lPVAywGuPfHUznW5NF6dSgMW0cC-y9O8iSCb-9sQSq9-wmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واژگونی کشتی در زیمبابوه ۷۲ قربانی گرفت
🔹
واژگونی یک کشتی مسافربری در زیمبابوه که بیش از ظرفیت مجاز مسافر داشت، ۷۲ قربانی به‌جا گذاشت که ۱۸ نفر از آن‌ها کودک بودند.
🔹
این کشتی از شهر کاریبا به‌سمت مناطق روستایی و جوامع ماهی‌گیری در شمال‌غرب زیمبابوه در حرکت بود؛ مناطقی که جاده‌هایش آسیب‌دیده است و دسترسی محدودی به وسایل حمل‌ونقل عمومی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/456359" target="_blank">📅 11:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447cfe6f37.mp4?token=K7ablQlQnNVSgVy-jz-B7s1C7XSyxahAOy_5nK_nYijF_YSoI_ARZmFerQ77UvkVLW0uUytaNTN99TIi04m_IL2MhRjRtkf5rcClklE37kA_xJt6NrCFoRrIG1kxcMzNsUMCQi0ZEda-nMfZLqNMwpszCza2C-9-mIvYGq8tfQRtuSG-q1328TGqOjn3FiwEKMGLOCCK2BKA3UERyVEXPiLwncYlIb1PQ3IdRYOR5jd6Yfrfe9t9EiamP-9xXSgg5A6_uK49gyGn3OZN9j8CeFRTAnI4yX_61f5ax-ObbtSGRWkaow2HO9vo0V3zRoLQMWQk1l3SO0hQriOoriqT5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447cfe6f37.mp4?token=K7ablQlQnNVSgVy-jz-B7s1C7XSyxahAOy_5nK_nYijF_YSoI_ARZmFerQ77UvkVLW0uUytaNTN99TIi04m_IL2MhRjRtkf5rcClklE37kA_xJt6NrCFoRrIG1kxcMzNsUMCQi0ZEda-nMfZLqNMwpszCza2C-9-mIvYGq8tfQRtuSG-q1328TGqOjn3FiwEKMGLOCCK2BKA3UERyVEXPiLwncYlIb1PQ3IdRYOR5jd6Yfrfe9t9EiamP-9xXSgg5A6_uK49gyGn3OZN9j8CeFRTAnI4yX_61f5ax-ObbtSGRWkaow2HO9vo0V3zRoLQMWQk1l3SO0hQriOoriqT5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواجههٔ غرب آمریکا با یک سیل مرگبار
🔹
مقامات آمریکایی می‌گویند که ایندیانا با «بدترین سیل ۳۰ سال گذشته» مواجه شده و سیل در این ایالت آمریکا تلفات انسانی هم داشته است.
🔹
شهردار ایندیاناپولیس و دیگر مقامات ایالت ایندیانا در یک کنفرانس خبری از ساکنان مناطقی که در معرض خطر سیل هستند، خواستند که به هشدارهای تخلیه توجه کنند.
🔹
ماهیت بی‌سابقهٔ سیل، ظرفیت امدادگران آمریکایی را محدود کرده؛ مقامات گفته‌اند که سیل در مناطقی که سابقهٔ آسیب‌دیدگی نداشته‌، مشاهده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/456356" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwFeqNR9RC61wizv5t28swAXS45rbVaB5HY16VAenm10rmEPi3aosFHyKaSlMqLYfwazzlFciF0ZPzciqAu3DOjyDslINwGRfnDj2bZPI-4rPuaRD5YZvyVy4Xytjj5Z256D4ZWs7udmSENgBIEKFZ4fFPWRyyJlF1XxsdfbjuQxgAV53wRcc0XxxE8KCj_z5-CeJZdr_Ir5p9dxqX3qAFA9pXoGt6S6_sRbbhXreUqTbqUjsu1TeyXEfDTaUkIF89bzSa_SM7agnMvLsH5oWUsBCrZaJmHXlZkIesbJMKBD2N6t1b7T1095jkul1RchSvXCXwELh4ZscTF9KMLSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارمزد ساتنا و پایا هم با دلار بالا رفت
🔹
جدیدترین نرخ کارمزدهای بانکی نشان می‌دهد کف کارمزد پایا با رشد ۳۳ درصدی به ۴۰۰ تومان و سقف آن با رشد ۶۰ درصدی به ۱۲ هزار تومان رسیده است.
🔹
سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده و کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و با هر میلیون اضافه، ۳۵۰ تومان بیشتر می‌شود.
🔹
معاون فناوری اطلاعات بانک شهر می‌گوید که کارمزدهای بانکی نسبت به وضعیت قیمت دلار خیلی عقب مانده است؛ چون خرید تجهیزات دلاری است و دستمزد توسعه‌دهندگان نرم‌افزار بالاست باید متناسب با آن کارمزدها افزایش پیدا کند.
🔸
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/456355" target="_blank">📅 11:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEgwT8wmoS5RMbnbZigNbREGhL3B4tonVpW_Jb-26kKReqyMRvTtrFzUy_kQLVV78SxPcZkKjg8nDgvgpmED9AFh25U4kDAnkuCP6JwFfbtHahwtqhg6cwq3hYQru-Qc2v-GHWbFB88HnOPkXtcGf6LaF4ZggLTiikNgB63jjOkOSFPfKRYyJxZbjakZqzpVV3pua0xJUMnul4ay4Qz1JX28luisVJmuKV3fQt6QdLw8D-xCLlray5S4OZV3Z8O4cFR3CKjRLxREVmHRQx6VHKz0FCZM76f9VNSNpVWAo1cdEUCaMkhKmr_lVeZLJqUrQkhmn34L-1rK82jyOuhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت‌های تازه از جنگ رمضان در فصل دوم «سرو، سپید، سرخ»
🔹
فصل دوم مجموعه نمایشی «سرو، سپید، سرخ» به تهیه‌کنندگی محمدرضا شفاه، محمدجواد موحد و آرش زینال‌خیری با ساختاری اپیزودیک، سراغ روایت‌های انسانی و کمتر دیده‌شده از جنگ رمضان رفته است.
🔹
در این فصل کارگردانانی چون حسین مهکام، دانش اقباشاوی، مریم اسمی‌خانی، امیر داسارگر، علیرضا صمدی، محسن بهاری، سیدمحمدرضا خردمندان، امیر ابیلی، علی طاهرفر و حمزه علیرضایی پشت دوربین رفته‌اند تا هر کدام با نگاه و زبان خود و در قالب داستان‌های مستقل، بخشی از روزهای جنگ رمضان را به تصویر بکشند.
🔹
این مجموعه محصول مشترک سازمان هنری رسانه‌ای اوج، سیمافیلم و مؤسسه فرهنگی هنری اندیشه شهید آوینی است.
🔹
«سرو، سپید، سرخ» از یکشنبه ۲۵ مرداد ماه
ر
وزهای فرد، ساعت ۲۲ روی آنتن شبکه یک سیما می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/456354" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjShD4JZJHIS47OEVtCQyMlE9Vqva6jiR2XfmkkkuANA7EGyyYGHNJNEIeyZOZaMGY7o0de8AWt9-EmskCqBtaQH1ThiAUAQq1mAPC8zYsufqw_--gafnJDdApqggO7a_dwiN6WnxBsadwChyradEkC8v-pG1_iLsYb0xfP6eLG7T80azNV-FEwHqXP-Keb8baYHRLgFghS2VPWhujBJqP6cYA2SCviE_ZquIQ7yqEIcawVBZQko4B4ebxcblTaIm06rthrZjRNlbF6W2qd7H7dDzr41Ev0XsvCXCxK9tB-QnMxPgZsSI3rssLssYvTjYX-maUxya7_9iCLZkzX7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی را به مزیت رقابتی سازمان خود تبدیل کنید
🔹
تحول در روابط عمومی و رسانه، از همین امروز آغاز شده است. سازمان‌هایی که بتوانند ظرفیت‌های هوش مصنوعی را به‌درستی در فرایندهای ارتباطی خود به کار بگیرند، سریع‌تر، دقیق‌تر و اثربخش‌تر عمل خواهند کرد.
🔹
دوره تخصصی
«هوش مصنوعی در روابط عمومی و رسانه»
با تمرکز بر نیازهای حرفه‌ای تیم‌های روابط عمومی، رسانه و ارتباطات طراحی شده است؛ از
پایش و تحلیل رسانه‌ها و افکار عمومی
تا
تولید محتوای هدفمند و مدیریت ارتباطات در شرایط بحران
.
ثبت‌نام انفرادی:
📝
ثبت نام دوره آنلاین
📝
ثبت نام دوره حضوری
برای دریافت اطلاعات و تهیه اشتراک سازمانی:
📞
۰۲۱-۴۲۰۸۲۳۲۴</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/456353" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/456352" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
