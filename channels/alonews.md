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
<img src="https://cdn4.telesco.pe/file/h3kEKV1g-DBCh1LL5Pn8OoBGPJlLpPtovy2nA-0yvA2oDK4dJgJ2t2prDP3TpJFy8S3I2H8ePkxHQr45HAOJnWsfJMMMpWaeFcPsr0JNL4__twBkQnsfoEh02x7o84jGpB4RVuuyNmKUrPkGbJiOdA9gkbs5so5V2EQ5iLvdfkLQ_c48T_WnvyAsEk0_3QDjGIRkU68YjtWDlgn_BXsnfftkHvz7ZvlSDyJ7Xeu-w_FZVuht5CtmAqXAreA_LI4o0_nPCCGFxTT1OTFA7c3bgoDS3n3wTEH-6u12iMc599nHO9xgWlHaZ3ghwY8TiSXyEAYueJP5pCR62YabZg3wDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 11:50:17</div>
<hr>

<div class="tg-post" id="msg-120107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رسایی: جلسات مجلس به طرز بی‌سابقه‌ای تعطیل شده تا در مذاکرات دخالت نکنیم
🔴
دبیر شورای عالی امنیت در نامه‌ای اعلام کردند مصلحت نیست جلسات مجلس برگزار شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/alonews/120107" target="_blank">📅 11:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98aee1045d.mp4?token=tSUbiDelKu037PesBf2tUoUIKlAO0wNH3LuBhT5bYOKT2vGiHlN-ej4o7UZEAKUqLlHuqJSrZd3OLmsYczAEoFkDDv6VM0DJZnqpwMROseTSMlmfBByvdew3UL6B8D4uPJX4SZxuZfmzFrx9YDnzL-yJPb2Q_pnEVRUyzc9Eed8-jE0H7GM9tiE6DE-qGV4Hx8go1LCMfueDbvNBzB0-If_Jjow7V2RkUlQ6_4R_NtdcwMo7YJBfRwytId_nMVVL0qAwhZ-1QkVStbphZu6H1ql1jkb0CZV4q3VCyXvf5b7hLOD8bwdkDy-aT0rW9nJ7QgNI77oJe-MBJ3hR4NMVew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98aee1045d.mp4?token=tSUbiDelKu037PesBf2tUoUIKlAO0wNH3LuBhT5bYOKT2vGiHlN-ej4o7UZEAKUqLlHuqJSrZd3OLmsYczAEoFkDDv6VM0DJZnqpwMROseTSMlmfBByvdew3UL6B8D4uPJX4SZxuZfmzFrx9YDnzL-yJPb2Q_pnEVRUyzc9Eed8-jE0H7GM9tiE6DE-qGV4Hx8go1LCMfueDbvNBzB0-If_Jjow7V2RkUlQ6_4R_NtdcwMo7YJBfRwytId_nMVVL0qAwhZ-1QkVStbphZu6H1ql1jkb0CZV4q3VCyXvf5b7hLOD8bwdkDy-aT0rW9nJ7QgNI77oJe-MBJ3hR4NMVew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
خبرنگار:
امیرعلی چرا اومدی تجمع؟!
▪️
امیرعلی:
به عشق رهبرم.
▪️
خبرنگار:
مامان و بابات مجبورت کردن که بیای تجمعات؟!
▪️
امیرعلی:
آره
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/alonews/120106" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120105" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فایننشال‌تایمز به‌نقل از دنیس وایلدر، رئیس سابق بخش تحلیل چین در سیا نوشت: بسیار قابل توجه است که گزارش‌های رسمی چین تاکنون هیچ اشاره‌ای به توافق آمریکا و چین بر سر «ایران غیرهسته‌ای» یا مخالفت با «مالکیت ایران بر تنگهٔ هرمز» نکرده‌اند.
🔴
این سکوت، سوالات جدی را دربارهٔ این ایجاد می‌کند که آیا واقعاً صحبت‌های ترامپ به‌نقل از چینی‌ها در این‌ موارد درست است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/alonews/120104" target="_blank">📅 11:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیویورک پست: اداره تحقیقات فدرال آمریکا (FBI) اعلام کرده است که برای پیدا کردن و دستگیری «مونیکا ویت» مأمور سابق اطلاعاتی نیروی هوایی ایالات متحده که به جاسوسی برای ایران متهم شده است، ۲۰۰ هزار دلار جایزه تعیین کرده است.
🔴
گفته شده اون از سال ۲۰۱۹ رسما به فعالیت جاسوسی برای ایران پرداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/alonews/120103" target="_blank">📅 11:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f18e93e69.mp4?token=BaE8dqpguSeTs-RC9nFMoyE488fCrr4rfk4vtmCmWknLHOFxUZDLzH2QgUUDlaK5fk09gR3CsQ1f9cpN4DEMOelR-Z2_p3mmtopTzLtFeHXPqT1wz9ws7ZlUZw-8uHsbuDLqeEApedvNSSWXsZPomQpQNGfekERwIrzdaEs_9jzQcJuH078M9OpRq3fEZ9CW7kvaWu6kJMts9dUfIRzr0QE1cBE47zXKKBZFTVgX2gLHyCE0scXMxpl21JrAu8B-d-rLrVueXl6IPpqYTFiPWU8LruZhMyLH19G3ZvyJ8wuWPKBPvT-I-nfisLai2dhYZcLw6Fx7S9bjoFgeV7JhVSGj1PvGFcqVsrz7gBSg-NmxhNZDbOoX33m8gObSlWz07_xwMZIOSoWz4D2N-crjw7-xYvmr8FI7AumEkDzQr_tG_rhKqOxEhJHJMsiYZgqOTTvCT4aVHv164KnkuP6wFSdK7QqqCUDkV4_pWZOXA5Chqgd_0duW6pDXCQCfZ130eHLJhXylq5zFOXc6mkGOKtwlu9Uk6gtWN5qxaf_Qe8pxVFAe6zV-rm7HJOA6nWVip6rrccmCKDMtZeDVv-uSGwWdgYL9tOCIYHvp4BTbmfXPbJaoL2VFfVZ4byOvlu4enPexx30kRdcV4ASx66J1tJUk2gp_5V3nIqKA_MajCW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f18e93e69.mp4?token=BaE8dqpguSeTs-RC9nFMoyE488fCrr4rfk4vtmCmWknLHOFxUZDLzH2QgUUDlaK5fk09gR3CsQ1f9cpN4DEMOelR-Z2_p3mmtopTzLtFeHXPqT1wz9ws7ZlUZw-8uHsbuDLqeEApedvNSSWXsZPomQpQNGfekERwIrzdaEs_9jzQcJuH078M9OpRq3fEZ9CW7kvaWu6kJMts9dUfIRzr0QE1cBE47zXKKBZFTVgX2gLHyCE0scXMxpl21JrAu8B-d-rLrVueXl6IPpqYTFiPWU8LruZhMyLH19G3ZvyJ8wuWPKBPvT-I-nfisLai2dhYZcLw6Fx7S9bjoFgeV7JhVSGj1PvGFcqVsrz7gBSg-NmxhNZDbOoX33m8gObSlWz07_xwMZIOSoWz4D2N-crjw7-xYvmr8FI7AumEkDzQr_tG_rhKqOxEhJHJMsiYZgqOTTvCT4aVHv164KnkuP6wFSdK7QqqCUDkV4_pWZOXA5Chqgd_0duW6pDXCQCfZ130eHLJhXylq5zFOXc6mkGOKtwlu9Uk6gtWN5qxaf_Qe8pxVFAe6zV-rm7HJOA6nWVip6rrccmCKDMtZeDVv-uSGwWdgYL9tOCIYHvp4BTbmfXPbJaoL2VFfVZ4byOvlu4enPexx30kRdcV4ASx66J1tJUk2gp_5V3nIqKA_MajCW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاوروف یک روزنامه‌نگار را از نشست خبری بیرون کرد!
🔴
به گزارش اسپوتنیک، این فرد دو بار با مکالمه تلفنی‌اش صحبت لاوروف را قطع کرد.
🔴
وزیر امور خارجه روسیه به زبان انگلیسی از روزنامه‌نگار خواست که محل کنفرانس را ترک کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/120102" target="_blank">📅 11:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f43d4a727.mp4?token=McT8xNzJvqpdrb57TAWzEl_gCgeuM7W0lmvfoZhlktcKE9u2bcdQJfYI9zXIIzqbw4rqquhOJCkEfZxWvuo5Bk8GXnisWBLxnQNQJe_vUzgvxlhyNRl3ZZUNudYlnHmUzljg_1n5K16c6G1C0ZoANQXfc9knJM3Zn2aqxntYMujcfM5gpT7VW1Ax4nhhndcr4rjbK-aAPesPGMOoKwjEFRThcvJffaGowlhl75fsIrVlIfVgyBeBgJUEACmuUhD0zAAtu-74LAVBkeWR6fDU5YYzDOHE7ZhP_UAXwT1jz4rQMZDbSS_rX5-BVBJ7ZF4zqJsDVaidHQfwYHzmV-TiUQV2vYYPuqcG_OLkPQUTZnBcEVPK-fvdI-7rmumlyhCG4q-NxWn1a6ms8UhkOOfGba9hV6O3o2x7dY9G82VAzY0Tb_EIIUUN-zwFsmrq1lgom1KfSSqEiT0TZ18ERYnBUW2-6A5Mwl2oNian6OUP1d3vc2c-DA1Xu_W4Zh0WaM65OWImtfv9ZhpT-eajfoYIMTDjHvONC8t7LKEUKFOggpr6QJqlDNbMJrBMiw2KBQX_jIeJk8gZyIJr5eC2XFEK9kpZw90fBYyzc4b-JSIg_pTbeqUqCZva-0OofLfNt-hTrrCG8aFmjsTow7-9O4giKAilA35MFp8ruw5q8GUrRiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f43d4a727.mp4?token=McT8xNzJvqpdrb57TAWzEl_gCgeuM7W0lmvfoZhlktcKE9u2bcdQJfYI9zXIIzqbw4rqquhOJCkEfZxWvuo5Bk8GXnisWBLxnQNQJe_vUzgvxlhyNRl3ZZUNudYlnHmUzljg_1n5K16c6G1C0ZoANQXfc9knJM3Zn2aqxntYMujcfM5gpT7VW1Ax4nhhndcr4rjbK-aAPesPGMOoKwjEFRThcvJffaGowlhl75fsIrVlIfVgyBeBgJUEACmuUhD0zAAtu-74LAVBkeWR6fDU5YYzDOHE7ZhP_UAXwT1jz4rQMZDbSS_rX5-BVBJ7ZF4zqJsDVaidHQfwYHzmV-TiUQV2vYYPuqcG_OLkPQUTZnBcEVPK-fvdI-7rmumlyhCG4q-NxWn1a6ms8UhkOOfGba9hV6O3o2x7dY9G82VAzY0Tb_EIIUUN-zwFsmrq1lgom1KfSSqEiT0TZ18ERYnBUW2-6A5Mwl2oNian6OUP1d3vc2c-DA1Xu_W4Zh0WaM65OWImtfv9ZhpT-eajfoYIMTDjHvONC8t7LKEUKFOggpr6QJqlDNbMJrBMiw2KBQX_jIeJk8gZyIJr5eC2XFEK9kpZw90fBYyzc4b-JSIg_pTbeqUqCZva-0OofLfNt-hTrrCG8aFmjsTow7-9O4giKAilA35MFp8ruw5q8GUrRiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره به‌دست آوردن اورانیوم غنی‌شده ایران: فکر نمی‌کنم این کار ضروری باشد مگر از نظر روابط عمومی. فکر می‌کنم برای اخبار جعلی مهم است که ما آن را به‌دست آوریم. من کسی هستم که گفتم ما آن را به‌دست خواهیم آورد و واقعاً به‌دست خواهیم آورد.
🔴
چشم‌مان به آن است. به آن‌ها گفتم اگر نیرویی آنجا بفرستند تا آن را بازیابی کنند، ما فقط با چند بمب به آن حمله خواهیم کرد و این پایان کار خواهد بود. آن‌ها این کار را نخواهند کرد.
🔴
ما ۹ دوربین روی این سه سایت داریم، ۲۴ ساعت شبانه‌روز. واقعاً اگر آن را به‌دست می‌آوردم احساس بهتری داشتم. اما فکر می‌کنم این بیشتر برای روابط عمومی است تا هر چیز دیگری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/alonews/120101" target="_blank">📅 11:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
واردات بدون انتقال ارز برای خودرو کلید خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/alonews/120100" target="_blank">📅 11:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: باید جنگ در ایران فوراً متوقف شود و به آتش‌بس دست یافت.
🔴
مداخله غرب، چه نظامی باشد و چه از طریق تغییر رژیم‌ها، وضعیت را در خاورمیانه و شمال آفریقا پیچیده‌تر می‌کند.
🔴
برای رسیدگی به بحران مربوط به ایران، لازم است علت اصلی بحران درک شود؛ یعنی «تجاوز غیرموجه آمریکا و اسرائیل».
🔴
ضروری است که هیچ‌گونه مشکل یا مانعی در تنگه هرمز وجود نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/alonews/120099" target="_blank">📅 11:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120098">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
آموزش و پرورش: امتحانات پایه‌های هفتم تا دهم با مجوز شورای تأمین هر استان و بصورت حضوری یا غیر حضوری برگزار می‌شه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/alonews/120098" target="_blank">📅 11:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120097">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / ترامپ : من صبر بیشتری نسبت به ایران نشان نخواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/alonews/120097" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120096">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پوتین ۳۰ اردیبهشت به چین می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/alonews/120096" target="_blank">📅 11:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120095">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/alonews/120095" target="_blank">📅 10:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120094">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کانال 13 اسرائیل:اسرائیل انتظار دارد حمله احتمالی آمریکا در ایران با بازگشت ترامپ از چین آغاز شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120094" target="_blank">📅 10:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120093">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQYBczTS4IYIVqNYWOX0xvLkNdnCkAxaSOiD43nAaYqW6djxEHGNZiQBaGljcl9O-XKgC3Kcp7SdmoBxfa5UtnDDw9lq4Yr4xxXxfKctVFHMnnTTLY9oVjQOroXr3wda19axJTJo-4DAjhtEQ6MPsH-AaGt7hJRert7MFqOUBhdyXEpZN6D94LsU_iFeIBcxs7puuhE6MQWOmx2y4JG0qgXkplY3gToBHJSKI6-aEqptCqmN18SkmHoVzv032mTXlvzJmbRkHCXZCLwHo47uYNChZGr0qI_Oaa5b0YuypeVfsk4r3mGEM6X9IsvEflM6_ZMOc7ZfwpXbh1yva3AaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
ریزش ادامه‌دار قیمت انس جهانی
هم اکنون 4573$
✅
@AloNews
خبر جنگ
‌</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/alonews/120093" target="_blank">📅 10:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120092">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwmQuH3nRQ3eczAcGm0nlDNUwBZzfhnjOzl0q_RSZWpWUPjL3ASvfklQ9P8nZIhVBim7IGTdyNjBw1axCAo__w40TjlqEG_j9ZB8LrWzi7_aX4lUb4ezTGDJEhm5VuIYOojsOjXUua4hMaGHSYw38FKMVEO5mJuLgOuCGFW8KriVTpeFNHqOgOcG7KwtTIX0iXX86iRBMhm3H0Oc_hkcppeAzhgP2DsWFBNSDOhSI6nPOcqrQKKRDa1JmGo7JOxY7_jc2P54txSp9_VrRnd_l84_4SBfPPXeAjpjFGS4CVtJd9jWw-j2qwmKazE_knUTFa1nxL1hvU3DbGem47gVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون چین را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120092" target="_blank">📅 10:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120091">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ8HlUncLuSYAkt1c_qTDXWBvubremDl35br3cnnwqdMZmTa-Tp1f2khfrS-vPhGW45l7QWLeOFSq2SkEe3SLiVYTp6iuRS-0gIISTCv3LASsZYD42tpRRDM-EzCK2-iTeJloJQpOrV_RKPDkJLFeOcGLWXDt67Xw9f6K9vJWST1yLDjWLapLK_8Gtt_xYirI_fNBhohXa4dGooTn-F7k9KWnbmy0-a8Vb2P8zc0RdgSJX5n2IkH971dM8JVihRjj7wHTTruw1MaLLcr9s5ggjL3YfCumnugENeZgMbbRbMnT88ybEI10dro0VtfRQEa3CzwcR0NTOMrELLxTCgHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف ویژه فقط گیگی 170 با تست رایگان
✅
اول تست کن، بعد با خیال راحت خرید کن!
❌
دیگه چرا گیگی ۵۰۰ تا ۶۰۰ بدی؟!
اونم بدون اینکه بدونی کیفیتش چطوره
😐
⚡️
تخفیف ویژه محدود
⏳
فقط تا پایان امشب
🌍
آی‌پی استار واقعی + پینگ عالی
🛡
ضمانت بازگشت وجه بدون شرط
🚀
اتصال پایدار و بدون قطعی
خرید آنی از ربات :
Id :
@LexVipBot
تایم سرورامون نامحدوده
❤️
Link chanel :
@lex_server
رایگان گذاشته میشه هرشب تو‌چنل بالا از دست ندید
👌</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120091" target="_blank">📅 10:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120090">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a3e47e4.mp4?token=ANOZ7LEJH6iQWkpQCKSeT5LwrxqVrpzWe0_fqRH4GbFFeRnqR33jlsmg9qpw9fpNSbM7010IffBTCiDJ29pfQ_foT61Uhdw79msxO3ea8ktdD8i1xXpxPvHMOTps74S2SL5LiIWEa0KZW2LPamZWOLz9G3jZUUCOtCQgRnPNJBmcVg9jUvDNNi4ftAc7luGwtsMsFmHHVTVkQEy6Qe4DumO6x1Btjp5Ha-4UozohYMBA7XRDnsfRYus53ysYBDDCSvf8-I24Hx7LCEcRqDM1_fGr6LPkeFAZkxH9IS-vEzUphFjUmKVTpuXjfn5MqoL4DxQT4_1ifxjCLgOjp2ZvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a3e47e4.mp4?token=ANOZ7LEJH6iQWkpQCKSeT5LwrxqVrpzWe0_fqRH4GbFFeRnqR33jlsmg9qpw9fpNSbM7010IffBTCiDJ29pfQ_foT61Uhdw79msxO3ea8ktdD8i1xXpxPvHMOTps74S2SL5LiIWEa0KZW2LPamZWOLz9G3jZUUCOtCQgRnPNJBmcVg9jUvDNNi4ftAc7luGwtsMsFmHHVTVkQEy6Qe4DumO6x1Btjp5Ha-4UozohYMBA7XRDnsfRYus53ysYBDDCSvf8-I24Hx7LCEcRqDM1_fGr6LPkeFAZkxH9IS-vEzUphFjUmKVTpuXjfn5MqoL4DxQT4_1ifxjCLgOjp2ZvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ مدیرعامل انویدیا به احتمال فروش تراشه به هواوی
🔴
جنسن هوانگ، مدیرعامل انویدیا، در پاسخ به پرسش خبرنگار مبنی بر فروش تراشه‌های این شرکت به هواوی، این سؤال را عجیب دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120090" target="_blank">📅 10:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120089">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: سهام بوئینگ پس از آنکه ترامپ گفت چین موافقت کرده ۲۰۰ جت بوئینگ بخرد، ۴٪ کاهش یافت — که بسیار کمتر از انتظارات برای قراردادی احتمالی با ۵۰۰ هواپیما بود که پیش از دیدار او با شی جین‌پینگ مطرح شده بود.
🔴
سرمایه‌گذاران واکنش منفی نشان دادند زیرا جزئیات سفارش هنوز نامشخص است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120089" target="_blank">📅 10:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ: از روز یکشنبه تاکنون ۹ نفتکش نفت و گاز از تنگه هرمز عبور کرده‌اند/ برخی از این ۹ کشتی همچنان در محدوده محاصره آمریکا در تنگه هرمز قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120088" target="_blank">📅 10:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پایان سفر ترامپ به چین
🔴
ترامپ سوار ایر فورس وان شد و سفر خود به چین را به پایان رساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120087" target="_blank">📅 10:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmj3dqcfe8XbnkJRr5pDUqS353LXmgT2SRH6qACRk8rn6-PgcLzX6T1XuVh7LY8nBbrne5lD5PIdNFIkQVrbHx8_VOUFms9Vi6Iy_L11ZnbsbCO4Su9KQ0THIcnLCXfC7OiECpmt3Sarq32pLmqSZTK5JUJhJ1V7DY8ezNNktiDO0bd5ADeHMyBlVeabDdSHrkGjI1RYwghiEsZdOjgdAXXfMgcM25yG3Z-3pwJxLmfv78ZI4l4WcWeMuV3n5JpcSpHgZzNxaMjMDYxDSA5saI1GwHuLmUrr1vtgnkThOSzZXb-OPE7GxmO7vVU0xTHNOa8GVJBksZtiJiBIijsHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقائی : هر کس در پنهان خیانت کند، در آشکار فاش خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/120086" target="_blank">📅 10:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
🔴
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
🔴
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ در همه جبهه ها شده و در صورت تحقق شروط ایران، مرحله دوم مذاکرات که درباره موضوع هسته ای بود، آغاز می شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/120085" target="_blank">📅 09:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مارکو روبیو: هزینه‌ای برای ایران هسته‌ای وجود دارد.
🔴
اگر روزی سلاح هسته‌ای به دست آورند، چه چیزی مانع کنترل آن‌ها بر تنگه می‌شود؟ این موضوع به یک مشکل دائمی تبدیل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120084" target="_blank">📅 09:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ در کنار شی جین‌پینگ: ما در مورد ایران صحبت کردیم. احساس می‌کنیم در مورد ایران بسیار شبیه به هم فکر می‌کنیم. می‌خواهیم که این موضوع پایان یابد. نمی‌خواهیم که آن‌ها سلاح هسته‌ای داشته باشند. می‌خواهیم تنگه‌ها باز باشند.
🔴
ما در حال حاضر آن را می‌بندیم.…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/120083" target="_blank">📅 09:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5f5af9bc.mp4?token=VIBfveWvZwa6ozi2z_NaiDQW7clpO_LC8G-UobougFssUk0wazOxHU-VdhhVYXKJJP6H3VIK9QdZz_HxFReDql2KmbjHrEYSwQJbCMKAprttcCbuFi6PrOPCy3tjnVI1Wl9fPqZ7FRBSjpLUCCnDUacrq69MWAX8VduRY4Eoff1zYEX4ejzHt-NkKwgARThKklMf-nA-XMFmyTAbMG36ggQYUt3qA3z-oo8uNViJbFPFaQemIkJXIG_7nWBTld9W4CFdRrHbw8h1S2yc2N6u0VsstPAY-p4tiGF_1KahB-IVyt_VItzTQ7zxTM6PpLYrMhypzqJCnX9maISRtpB1fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5f5af9bc.mp4?token=VIBfveWvZwa6ozi2z_NaiDQW7clpO_LC8G-UobougFssUk0wazOxHU-VdhhVYXKJJP6H3VIK9QdZz_HxFReDql2KmbjHrEYSwQJbCMKAprttcCbuFi6PrOPCy3tjnVI1Wl9fPqZ7FRBSjpLUCCnDUacrq69MWAX8VduRY4Eoff1zYEX4ejzHt-NkKwgARThKklMf-nA-XMFmyTAbMG36ggQYUt3qA3z-oo8uNViJbFPFaQemIkJXIG_7nWBTld9W4CFdRrHbw8h1S2yc2N6u0VsstPAY-p4tiGF_1KahB-IVyt_VItzTQ7zxTM6PpLYrMhypzqJCnX9maISRtpB1fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در کنار شی جین‌پینگ: ما در مورد ایران صحبت کردیم. احساس می‌کنیم در مورد ایران بسیار شبیه به هم فکر می‌کنیم. می‌خواهیم که این موضوع پایان یابد. نمی‌خواهیم که آن‌ها سلاح هسته‌ای داشته باشند. می‌خواهیم تنگه‌ها باز باشند.
🔴
ما در حال حاضر آن را می‌بندیم. آن‌ها آن را بستند و ما آن را بالای سرشان بستیم. اما می‌خواهیم تنگه‌ها باز باشند.
🔴
می‌خواهیم که آن را به پایان برسانند زیرا این یک کار دیوانه‌وار است. آن‌ها کمی دیوانه هستند و این خوب نیست.
🔴
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120082" target="_blank">📅 09:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c5c17608.mp4?token=biNzrTu0WEAmxWQpkdX3p-NsAWdtFbu8PBq6zPdyQnIxr97QanaY4oxxOX8V0560K8FHiWTSri4e-G2zXVXacd8ubjepsZz4Mp7yNoRsZaI1-mRAQumeIpX2QbKjkQM_Z4GEtckCDyqay9vM76cANigizv0oNZCw1-66FKHaOPRc29QCNXfI72SDmDkPGJ8MZxmPvb8doTVyIGqAi1v7aZo2UfoiQlqH6HsobEf4qVkdDjQkI-PThJgnzXjQVHEzUrCNZbqW2J2i-Z8oQCtnf7Hp8iqwhqY19q1d2FcSZPz6K8r-lgpib66f4ybGbwHDl6SqLc4Saw4U__jLVL0yRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c5c17608.mp4?token=biNzrTu0WEAmxWQpkdX3p-NsAWdtFbu8PBq6zPdyQnIxr97QanaY4oxxOX8V0560K8FHiWTSri4e-G2zXVXacd8ubjepsZz4Mp7yNoRsZaI1-mRAQumeIpX2QbKjkQM_Z4GEtckCDyqay9vM76cANigizv0oNZCw1-66FKHaOPRc29QCNXfI72SDmDkPGJ8MZxmPvb8doTVyIGqAi1v7aZo2UfoiQlqH6HsobEf4qVkdDjQkI-PThJgnzXjQVHEzUrCNZbqW2J2i-Z8oQCtnf7Hp8iqwhqY19q1d2FcSZPz6K8r-lgpib66f4ybGbwHDl6SqLc4Saw4U__jLVL0yRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هانی‌کس از فاکس نیوز
:
مردم نگران نیت‌های شوم چین هستند.
🔴
ترامپ
:
آن‌ها کارهایی علیه ما انجام می‌دهند و ما نیز کارهایی علیه آن‌ها انجام می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120081" target="_blank">📅 09:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2114b7ed5.mp4?token=eBqtiK8AqSBMg0jiIOvA3EwD_zqv6yFYYhROJMOfNuaFMV4zWSpy1Vmow0ffxlAiOPPFpUborMtCchW4yc3BuFGd2n8uxEUyDuHn2sFJGxyZdD4wzGuFmcC3IHw-SgKvalKEAzVzhF7BZDOVl3zieiaQdMW437PpKJ91H4EVlaBAaYmXKIbx2NxtQgTtS_qoRWqVqpZrP3EraecHASDzrKqrowGFIoLGEyK1ZQFHY16HW_Dz5_1-Sfh0wjAltrkCR5G6ic1j_NxLCeJoLFyr83g6SI72IDua3xqcP4FLzcJ7j3X1eQE3nrJFZzSCyMLXVi2kr9yrXOZ5klydonRsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2114b7ed5.mp4?token=eBqtiK8AqSBMg0jiIOvA3EwD_zqv6yFYYhROJMOfNuaFMV4zWSpy1Vmow0ffxlAiOPPFpUborMtCchW4yc3BuFGd2n8uxEUyDuHn2sFJGxyZdD4wzGuFmcC3IHw-SgKvalKEAzVzhF7BZDOVl3zieiaQdMW437PpKJ91H4EVlaBAaYmXKIbx2NxtQgTtS_qoRWqVqpZrP3EraecHASDzrKqrowGFIoLGEyK1ZQFHY16HW_Dz5_1-Sfh0wjAltrkCR5G6ic1j_NxLCeJoLFyr83g6SI72IDua3xqcP4FLzcJ7j3X1eQE3nrJFZzSCyMLXVi2kr9yrXOZ5klydonRsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ می‌گوید که ایران حتی قادر به رسیدن به «گرد و غبار هسته‌ای» نیست زیرا «کوه بر سر آن خراب شده است» و تنها چین و ایالات متحده می‌توانند به آن دست یابند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120080" target="_blank">📅 09:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542b29045f.mp4?token=c7qNTwEXdpsMgcWEbf1ymQdoLmcIhJeTqZVOPTTNMnMXycdQL5dr-mWCU2g9crGaBj6NhC4veEWCoM87CjniIbzBEnB5SZXVqnLS1vbNFxFNtvL-J3s-WbNAe2ac51IKW9vaSGBBsYCvQLcGbRl3V-rkWq0HVc8AUEdNH_dY88kbkfQa3DFOvXBeZxHVlo7l7E1LpXgRhTYkpdH2lAOSokUeas7lEXPUQqrRnDZ00wFHW9fH82PitN2-6vn9JfCQFDHfEbZID_BqpnOYbeFw7oLi_Xv5Lvh2YNIlHG29d83FYLmNR1ehnppQDjoVKRPmNTYZFlJ7CGjA2cZQPxi4AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542b29045f.mp4?token=c7qNTwEXdpsMgcWEbf1ymQdoLmcIhJeTqZVOPTTNMnMXycdQL5dr-mWCU2g9crGaBj6NhC4veEWCoM87CjniIbzBEnB5SZXVqnLS1vbNFxFNtvL-J3s-WbNAe2ac51IKW9vaSGBBsYCvQLcGbRl3V-rkWq0HVc8AUEdNH_dY88kbkfQa3DFOvXBeZxHVlo7l7E1LpXgRhTYkpdH2lAOSokUeas7lEXPUQqrRnDZ00wFHW9fH82PitN2-6vn9JfCQFDHfEbZID_BqpnOYbeFw7oLi_Xv5Lvh2YNIlHG29d83FYLmNR1ehnppQDjoVKRPmNTYZFlJ7CGjA2cZQPxi4AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رهبری فعلی ایران: فکر می‌کنم آن‌ها در بسیاری از جنبه‌ها در واقع معقول‌تر هستند. باهوش‌تر از لایه اول و لایه دوم که دیگر در میان ما نیستند.
🔴
هانیتی از فاکس نیوز: پس چرا مدام رفت‌وبرگشت می‌کنند؟
🔴
ترامپ: آن‌ها توافق می‌کنند و روز بعد—مثلاً، پنج روز منتظر نامه‌ای ماندیم که باید یک ساعت پیش آنجا بود. آن‌ها جز آشوب درونی چیزی ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/120079" target="_blank">📅 09:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: در حال حاضر، نفتی از جزیره خارگ خارج نمی‌شود — هیچ، صفر.
🔴
مردم در حال یافتن مکان‌های دیگر برای خرید نفت هستند — مانند تگزاس. بنابراین، من نمی‌خواهم بگویم که ما در حال کسب ثروتی عظیم هستیم. اگر من آن را بگویم، آن‌ها می‌گویند: «او، او درباره مرد کوچک فراموش می‌کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120078" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: به شی گفتم که نیازی ندارید ایران سلاح هسته‌ای داشته باشد. آن‌ها دیوانه‌های یخ‌زده‌ای هستند.
🔴
هانیتی(فاکس): او چه گفت؟
🔴
ترامپ: او خیلی واکنش نشان نخواهد داد. او مردی بسیار آرام است. نخواهد گفت که این یک نکته خوب است.
🔴
هانیتی: آیا فکر می‌کنید او موافق بود؟
🔴
ترامپ: فکر می‌کنم که بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/120077" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: ویتنام ۱۹ سال طول کشید. فکر می‌کنم عراق ۱۰ سال بود… هزاران نفر در ویتنام کشته شدند. متأسفانه، در دو جنگ، ما ۱۳ نفر را از دست دادیم.
🔴
۱۳ نفر در مقابل ۷۵,۰۰۰ نفر، در مقابل ۵۰,۰۰۰ نفر.
🔴
نفت به مقدار بسیار کمی افزایش یافت در مقایسه با آنچه اکثر مردم، حتی من، فکر می‌کردند که بیشتر افزایش خواهد یافت، اما این برای یک دوره زمانی کوتاه قابل قبول بود زیرا ما نمی‌توانیم اجازه دهیم ایران به یک سلاح هسته‌ای دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120076" target="_blank">📅 09:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=QqNbJfNVW45a1Ssbcpb8LRDr3tWfsaVR94bCLPtuqEnusSf3yVzbmGnK4QtlCC9LFF-4sVHOpdbW3aHEwR2T25xe_fkljn-qMhbAizQB1pOfmolO_eglzWJCrLopt9iX1Q-j3l2wN57af6QXTloj4-wgKwmash-_7Ts6IFUAuG4uK6xcql6uFkyvVWosuys3D7t7uq5MKrDzp-fi3mocszgZdRHIpaVvyV0XvMef8oCrJG4EexzckDjOYYZEPTdHBQR502DrXiwNwWgsM_6XIgB42pusP4rMRANG13Ci0Fq8BDRUeqsLs9fp5X3A8_UVABV5xLdV27FtXWbouBKt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=QqNbJfNVW45a1Ssbcpb8LRDr3tWfsaVR94bCLPtuqEnusSf3yVzbmGnK4QtlCC9LFF-4sVHOpdbW3aHEwR2T25xe_fkljn-qMhbAizQB1pOfmolO_eglzWJCrLopt9iX1Q-j3l2wN57af6QXTloj4-wgKwmash-_7Ts6IFUAuG4uK6xcql6uFkyvVWosuys3D7t7uq5MKrDzp-fi3mocszgZdRHIpaVvyV0XvMef8oCrJG4EexzckDjOYYZEPTdHBQR502DrXiwNwWgsM_6XIgB42pusP4rMRANG13Ci0Fq8BDRUeqsLs9fp5X3A8_UVABV5xLdV27FtXWbouBKt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: امیدوارم ایران تماشا کند. ما دقیقاً می‌دانیم چه چیزی را آماده کرده‌اند.
🔴
می‌دانید، آن‌ها کمی استراحت داشتند، بنابراین سعی دارند چند چیز را با هم جمع کنند. آن‌ها موشک‌هایی را از زیر زمین بیرون آورده‌اند. همه این‌ها در یک روز از بین خواهند رفت.
🔴
همه کارهایی که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120075" target="_blank">📅 09:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4784b29a.mp4?token=K5SV_Xy_Q6qwc-41v6Kt6HvgcHiTKkyEis6brgaZbADSdN94wNbUZkYekFjIjzSSOEZso-uAW1lo6egfiOWsBrEFy4g_InMV7RYpZCUkYIHV9TRMz3nE7uoQSKLlHhp4EQnC1SVL1AdHh1zBcIAeJCJw1-3AfynDctqIpVPNGLmugrT2ml6so96LoufCOQNBfua09_jSA4_ZqnFx4wab8D3sNPf-fho-7fCIME6pTcTrHIGX3McptP5ICQZXRG0B90W8ll4FeDxuVmSSBT9pcjfPrU65rX8V8_27YrI4D0iU2QRlFsH3DJyo09O2nyiCXTBKhxHaUQ8RX9FTxyoiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4784b29a.mp4?token=K5SV_Xy_Q6qwc-41v6Kt6HvgcHiTKkyEis6brgaZbADSdN94wNbUZkYekFjIjzSSOEZso-uAW1lo6egfiOWsBrEFy4g_InMV7RYpZCUkYIHV9TRMz3nE7uoQSKLlHhp4EQnC1SVL1AdHh1zBcIAeJCJw1-3AfynDctqIpVPNGLmugrT2ml6so96LoufCOQNBfua09_jSA4_ZqnFx4wab8D3sNPf-fho-7fCIME6pTcTrHIGX3McptP5ICQZXRG0B90W8ll4FeDxuVmSSBT9pcjfPrU65rX8V8_27YrI4D0iU2QRlFsH3DJyo09O2nyiCXTBKhxHaUQ8RX9FTxyoiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هانی‌کس فاکس
:
آیا فکر می‌کنید پیشرفت کرده‌اید؟ اگر قرار نیست پس از ساعت‌ها جلسه این توافق بزرگ را امضا کنید، آیا احساس می‌کنید که زیربنای آن ریخته شده است؟
🔴
ترامپ
:
قطعاً. این بار بزرگتر از بار قبل است. قرار است مقدار زیادی لوبیای سویا انجام دهند...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/120074" target="_blank">📅 09:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199e45eeff.mp4?token=Fb0CFXcR-FDFaWBVIip5YJCnUStQn-RdBD13UkYsTV2_w1JzquOmhEle4UHfQPSgPsUzgAE71ypJZ09svYphp_b2By9dpKao136oma9imWjb0xQuYkRH8_0SxachZFTEoPQJ2ldT7Lfu7UbYQwSYphyPdWP2aT5XpAqTqFn8cziELG6mYo8s6sdLIvwveE7B40vZI3fj6BhX5RMVEOpExxUp-iB-YyPhc-auTqYJwgj3PRGK5sxE-H3zoZOtfAcV5jqDlM6vOSPM1Unxn_QSObV__TP3Bsq8b2K9wIBUok4eSnwW5TlIRhjyhMuvur6-EMQMM3JnP6NFqBHXUs9npg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199e45eeff.mp4?token=Fb0CFXcR-FDFaWBVIip5YJCnUStQn-RdBD13UkYsTV2_w1JzquOmhEle4UHfQPSgPsUzgAE71ypJZ09svYphp_b2By9dpKao136oma9imWjb0xQuYkRH8_0SxachZFTEoPQJ2ldT7Lfu7UbYQwSYphyPdWP2aT5XpAqTqFn8cziELG6mYo8s6sdLIvwveE7B40vZI3fj6BhX5RMVEOpExxUp-iB-YyPhc-auTqYJwgj3PRGK5sxE-H3zoZOtfAcV5jqDlM6vOSPM1Unxn_QSObV__TP3Bsq8b2K9wIBUok4eSnwW5TlIRhjyhMuvur6-EMQMM3JnP6NFqBHXUs9npg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من یک نام جدید به ذهنم رسید، «دموکرات‌ها». آن‌ها احمق هستند.
این d-u-m است. من b را حذف کردم. بنابراین، شما فقط یک حرف را تغییر می‌دهید. E می‌رود و U می‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120073" target="_blank">📅 09:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ در مورد آنچه از شی جین‌پینگ درخواست کرد: گفتم: «در مورد استفاده از ویزا در چین چه می‌شود؟» به دلایلی، آن‌ها تحریم شدند و شاید این موضوع برداشته شود.
🔴
ما چند ساعت آنجا بودیم — زمان طولانی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120072" target="_blank">📅 09:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رئیس پارلمان لبنان، نبیه بری: من بدبین هستم... من طرفدار مذاکرات مستقیم نیستم، اما فعلاً صحبت نخواهم کرد، و وقتی کارمان تمام شد، حرفی برای گفتن خواهم داشت
🔴
هر توافقی باید «چتر تضمین‌های سعودی-ایرانی-آمریکایی» را داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120071" target="_blank">📅 09:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرنگار المیادین در پکن: بسیاری از اظهارات آمریکایی ها می گویند که ترامپ چین را متقاعد کرد که موضع خود را در قبال ایران تغییر دهد و این درست نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/120070" target="_blank">📅 09:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دونالد ترامپ،در مصاحبه‌ای مدعی شد آنها (چینی‌ها) موافقت کرده‌اند که می‌خواهند از ایالات متحده نفت بخرند.
🔴
آنها قرار است به تگزاس بروند. ما قرار است کشتی‌های چینی را به تگزاس و لوئیزیانا و آلاسکا بفرستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120069" target="_blank">📅 09:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جدیدترین رای گیری برای محدود کردن اختیارات جنگی ترامپ در مجلس آمریکا ۲۱۲ رای مخالف و ۲۱۲ رای موافق آورد و بازم شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120068" target="_blank">📅 09:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره از بزرگ‌ترین تبادل اسرا در جنگ یمن خبر داد، بیش از ۱۶۰۰ زندانی آزاد می‌شوند
🔴
دولت مورد حمایت سازمان ملل در یمن و حوثی‌ها در توافقی که با میانجی‌گری سازمان ملل در اردن امضا شد، بر سر تبادل بیش از ۱۶۰۰ زندانی به توافق رسیدند؛ اقدامی که بزرگ‌ترین مبادله اسرا از زمان آغاز جنگ داخلی یمن در سال ۲۰۱۴ توصیف شده است.
🔴
بر اساس این توافق، حوثی‌ها ۵۸۰ زندانی، از جمله ۷ شهروند سعودی و ۲۰ سودانی را آزاد می‌کنند و در مقابل، دولت یمن ۱۱۰۰ زندانی حوثی را تحویل خواهد داد. مقام‌های دو طرف می‌گویند مجموع افراد مشمول این توافق به حدود ۱۷۲۸ نفر می‌رسد.
🔴
الجزیره گزارش داده دو طرف همچنین بر سر ادامه مذاکرات، بازدید متقابل از بازداشتگاه‌ ها و اجرای عملیات آزادی زندانیان با همکاری کمیته بین‌المللی صلیب سرخ توافق کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120067" target="_blank">📅 09:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c72bd88a.mp4?token=GaK7M19EP2i0Kwp3KtDv5ssPtHjAC89USL9cnThKNKK16IUUpE3kF7rxdhFNsMTsm0etyQh2vJm_7fwa3akEECl0sTd-RjlVxXIHMwkS-zAqvtMa19fAbrXsSMDspjhgBP-tcoU9y5SM2Uy5RMmM79cZISo7FZNltETv1BhuPgWPDpffnX4NynfRTh_Riv_zE-dRxB3289vv6e31ttuoOdyHvSsvC7zp87i6ZHJG5f1DxKaiZ8YoSJHHRwbWhEYEZr1D2aMLSTpMAGoZBLJvUlvlbFLoihgJ7tc1ACuEuDnZCB4LE14xbRmdqJKAss6XJEFioeVuqQg6aNIW-yEx4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c72bd88a.mp4?token=GaK7M19EP2i0Kwp3KtDv5ssPtHjAC89USL9cnThKNKK16IUUpE3kF7rxdhFNsMTsm0etyQh2vJm_7fwa3akEECl0sTd-RjlVxXIHMwkS-zAqvtMa19fAbrXsSMDspjhgBP-tcoU9y5SM2Uy5RMmM79cZISo7FZNltETv1BhuPgWPDpffnX4NynfRTh_Riv_zE-dRxB3289vv6e31ttuoOdyHvSsvC7zp87i6ZHJG5f1DxKaiZ8YoSJHHRwbWhEYEZr1D2aMLSTpMAGoZBLJvUlvlbFLoihgJ7tc1ACuEuDnZCB4LE14xbRmdqJKAss6XJEFioeVuqQg6aNIW-yEx4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مصاحبه با فاکس‌نیوز: افزایش قیمت بنزین، بهایی است که آمریکایی‌ها باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای بپردازند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/120066" target="_blank">📅 09:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaWzq_8bUY_FhcwJRpnUgljDOJVoBc3nUMrEsdLjKPKdOHuAcGUelS1WZR70H8QmdI48UEWc-ADs_Zgg1e1PpyLK7cLt_w3Dxv5sJq4UZkaa1Rf6DMcRkrl5VCMzQRiaC2FwL6pJs5E8srUv-8yH7CijoQehItBD4isQdJaTKlpBVc2d1BzyfKhgBte13y4I0xBOp1mgQSnmepbV6-QxIAJRjnxTmQ6loz_BOx-n0Vtarl6Vzr_WO4MZ8I5P8EgPIpl5XAABdwdh0dg1n1A8WM05TZPk3kbYXBYalzwEIThGsRFBZgQ8v-y1F2hP0yEDJiQivvSH__tmwBPRVeggqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدار تخلیه برای چندین شهر در منطقه صور در جنوب لبنان صادر کرده‌اند و نسبت به حملات احتمالی اسرائیل هشدار داده‌اند.
🔴
از ساکنان خواسته شده حداقل ۱ کیلومتر از مناطق مشخص شده فاصله بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120065" target="_blank">📅 09:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرنگار المیادین در پکن: بسیاری از اظهارات آمریکایی ها می گویند که ترامپ چین را متقاعد کرد که موضع خود را در قبال ایران تغییر دهد و این درست نیست.
🔴
موضع چین در قبال ایران روشن، ثابت است و تغییری نکرده است. دیروز به طور کامل از صحبت در این مورد خودداری کرد و هر آنچه خلاف آن شایعه می شود کذب محض است.
🔴
چین صبح امروز تصمیم گرفت موضع خود را از طریق بیانیه کامل وزارت خارجه منتشر کند تا تمام حقیقت روشن شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120064" target="_blank">📅 08:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رویترز: ترامپ مدعی شد «توافق‌های تجاری فوق‌العاده‌ای» با چین حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120063" target="_blank">📅 08:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور چین می‌خواهد شاهد توافق با ایران باشد و برای کمک به این کار اعلام آمادگی کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120062" target="_blank">📅 08:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قیمت جهانی نفت روز جمعه پس از آن افزایش یافت که دونالد ترامپ اعلام کرد چین پس از گفت‌وگوهای او با شی جین‌پینگ، با خرید نفت از آمریکا موافقت کرده است.
🔴
با این حال، پکن تاکنون این ادعا را تأیید نکرده و به درخواست رسانه‌ها برای اظهار نظر نیز پاسخی نداده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/120061" target="_blank">📅 08:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد
🔴
تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند.
🔴
هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی مواجه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120060" target="_blank">📅 08:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: توافق‌های تجاری فوق‌العاده‌ای با چین انجام شد
🔴
دونالد ترامپ، با اشاره به نتایج مثبت سفر خود اعلام کرد توافق‌های تجاری بسیار خوبی حاصل شده که برای هر دو کشور عالی است.
🔴
وی با ابراز احترام نسبت به شی جین‌پینگ، به سابقه آشنایی ۱۲ ساله و حل مشکلات پیچیده‌ای اشاره کرد که دیگران قادر به رفع آن‌ها نبودند. ترامپ این رابطه را بسیار قوی توصیف کرد و کارهای انجام شده را فوق‌العاده دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/120059" target="_blank">📅 08:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مارکو روبیو: مردم کوبا باید بدانند که در حال حاضر ۱۰۰ میلیون دلار غذا و دارو برای آن‌ها موجود است و تنها دلیلی که این کمک‌ها به دستشان نمی‌رسد، رژیم کوبا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/120058" target="_blank">📅 08:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87449a5631.mp4?token=AXDvCu4nyz8V6AGXQtN8GPtkIU-9Rf67GgyZb-a7Q4LLmyoztQv4jnI0js_YUKwO_szIjD_81EHqM7K8NDhqqntSyCRHohrm52TrJOQPIx8Cs51HTjRYGW4_xEjZgi63fjOeSqw943V5-jOBUhPFnP-RB0QJe4JtBTYgkuJqzlOpuD5GrDtEyt5Oy7hcTsHNO3Lx47UVxSlHs4J9Uj4u3R5-DL5CI0ZcUwyvwtiAj4HgAiW-bzydpJgOvPtC7ANAbZE2JvE_cmh0aShGUmH41PQVKfthmviwMe2_UUTmEvYNikZkarT7dq5LolQQ7Yrfz49OXWPjl4Y2ZbuBrF2TQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87449a5631.mp4?token=AXDvCu4nyz8V6AGXQtN8GPtkIU-9Rf67GgyZb-a7Q4LLmyoztQv4jnI0js_YUKwO_szIjD_81EHqM7K8NDhqqntSyCRHohrm52TrJOQPIx8Cs51HTjRYGW4_xEjZgi63fjOeSqw943V5-jOBUhPFnP-RB0QJe4JtBTYgkuJqzlOpuD5GrDtEyt5Oy7hcTsHNO3Lx47UVxSlHs4J9Uj4u3R5-DL5CI0ZcUwyvwtiAj4HgAiW-bzydpJgOvPtC7ANAbZE2JvE_cmh0aShGUmH41PQVKfthmviwMe2_UUTmEvYNikZkarT7dq5LolQQ7Yrfz49OXWPjl4Y2ZbuBrF2TQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل در حملات بامداد امروز علیه حزب الله از سلاح فسفری استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120057" target="_blank">📅 07:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120056">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا برای سومین بار در تصویب قطعنامهای با هدف محدود کردن اختیارات رئیس‌جمهور در ارتباط با جنگ با ایران ناکام ماند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120056" target="_blank">📅 07:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccpQdgBOSfZYeDPUtt1lXYgznkjfTJi4cjJk2th_86LWuDblMGkOkkXwYCZRv6hX3G56u7QP0uRX3A6sAN1qKlraei7siDRSmKKX_sViyEXln2DbIoD__42u84ph0pWRIfm1Iv3qOdPj4yjgmAeNliV2Eqj-VErEVF5jF-ENasWi-UfI0PdFB1J4WHsDV9hbNdjxc0V_I4KGOatx3hD6MPZq05RNrztswsuPIm5cB1Wffp-9w1tGrZUfuzgHcwYzh7d7Jvg7ALQz5wvqROwzMbCmkuHa0sc2p-gQz16M9OV-vKAeA4w6ACi4qBsydswpZKD-ijM6t0ZdfHnBJoEODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
اینترنت رایگان و آزاد برای همه مردم
⚡
VPN رایگان
⚡
کانفیگ تست‌شده و پرسرعت
⚡
آپدیت روزانه
⚡
بدون قطعی و دردسر
@NetaazaadVPN
@NetaazaadVPN
اینجا فقط وصل میشی و راحت استفاده میکنی
🫡
👇
@NetaazaadVPN
@NetaazaadVPN
@NetaazaadVPN</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/120055" target="_blank">📅 02:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120054">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOCLlJ4UtZf8pI05mwqZsn5ey9QQRhyEPBi0UtRnhVcTX9vqKVL8gExFo_Q7Nsb2-fFJkxPrON6q5YMHni43oG4MIra4VX2Mv5XI4UKdKINr-QgyKzVA8MZ869fI-MpDWTD0Yb8fH3W5hCOKF6rYC_L1H0S9f_xjIxcasx9cT-aBv5Q4LrLyjo3W6mTe3ld74gGT51nPUiUUlfinOIU2D5GT8UZliViGDpIdhRPeHQfhLRb_Z29PoSSiZr0MCH0kbCYuO95CEZKEAq3qSh9daVW3A-R1ejVELu0Ff983mUkvTPDqdq_dZAgQfqm7U-J11sIkuCabT-yIrUrP0BfGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ویزا مهدی طارمی به علت خدمت در سپاه صادر نشود
‼️
@AloSport</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120054" target="_blank">📅 02:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120053">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/ترامپ:
نابودی نظامی ایران ادامه خواهد یافت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/120053" target="_blank">📅 01:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120052">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh1xldRJKTYpYyYk-OWY-4VbUNXZVlaIDhUHLs4bklSkH8Op2U6BluomTEDN36j17AinQR0sUXR2Bi8xQBJOgNqK95gErBqjUlx4cya4bFbj5cfcreXjpfBSVkMWFMjAkTqpQtpQGGkLn_KALTGAzQBCbkcPAXAEp8WTlhNry4oPrUpBTpZrmfvpnHJUHmuNYGJIM7dSPUWh2iI66ovvxvnt90QW58IBhxU_ON-hMuBFwhOclQKd3TtXgjrA0AplXpq9iCwRjdcKKhVRFmiV4MPVYowXXE0lvYaiCYdvXOzXacj6U-hadIkCWjipv3ObhjnhoT33AXGZSn684iaFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ترامپ:
🔴
وقتی رئیس‌جمهور شی به‌طرز بسیار ظریفی ایالات متحده را کشوری در حال افول نامید، احتمالاً منظورش آسیب عظیمی بود که ما در چهار سال دولت جو خواب‌آلود بایدن و دولت بایدن متحمل شدیم، و در این مورد او صد در صد درست می‌گفت. کشور ما به‌طور غیرقابل اندازه‌گیری از مرزهای باز، مالیات‌های بالا، تراجنسی بودن برای همه، مردان در ورزش زنان، DEI، توافقات تجاری وحشتناک، افزایش جرم و جنایت و خیلی چیزهای دیگر آسیب دیده است!
🔴
رئیس‌جمهور شی منظورش صعود شگفت‌انگیزی نبود که ایالات متحده در 16 ماه چشمگیر دولت ترامپ به جهان نشان داد، از جمله بازارهای سهام رکوردشکن و 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، شکست نظامی ایران (ادامه دارد!) — قوی‌ترین ارتش روی زمین، دوباره ابرقدرت اقتصادی با رکورد ۱۸ تریلیون دلار سرمایه‌گذاری شده در آمریکا توسط کشورهای دیگر، بهترین بازار کار در تاریخ آمریکا، با تعداد بیشتری از افراد شاغل نسبت به همیشه، پایان دادن به DEI که کشور را تخریب می‌کرد و بسیاری چیزهای دیگر که به‌راحتی نمی‌توان فهرست کرد. در واقع، رئیس‌جمهور شی مرا به خاطر این همه موفقیت بزرگ در مدت زمان کوتاه تبریک گفت.
🔴
دو سال پیش ما واقعاً کشوری در حال افول بودیم. در این مورد کاملاً با رئیس‌جمهور شی موافقم! اما اکنون ایالات متحده داغ‌ترین کشور جهان است و امیدوارم روابط ما با چین قوی‌تر و بهتر از همیشه شود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/120052" target="_blank">📅 01:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e6fd559e.mp4?token=C4ibdRMsx4KE2aQfErOTX2GrUtGJZPY3tNAcI76HQn3DTY2x_8wbDRElXruATQA2SlfyRAEzrlntkC9JGdIS1XPW45lEcjKSf_GEsQ7TSATLbzZpC2wVGr1xB2SW5gms3vgzN39s2OvwfEWuDOHxQk5dyLTsiGII4gR_QZZYhf3g-i_6600KNO__O0LV0XuuLMb0Kp50jVuGXYROMRPlLtkeBYKwp5OqQPCRzmde6o16Muu_EHFgKpouZhfmLD-2v3plBeYBgWuSNvjiIWbASCRWBRUyVu3aYqjOMddNmlnozkIsAIg7FszIpzg07PIMM5QjwjvC4vUNMYsmZi5C1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e6fd559e.mp4?token=C4ibdRMsx4KE2aQfErOTX2GrUtGJZPY3tNAcI76HQn3DTY2x_8wbDRElXruATQA2SlfyRAEzrlntkC9JGdIS1XPW45lEcjKSf_GEsQ7TSATLbzZpC2wVGr1xB2SW5gms3vgzN39s2OvwfEWuDOHxQk5dyLTsiGII4gR_QZZYhf3g-i_6600KNO__O0LV0XuuLMb0Kp50jVuGXYROMRPlLtkeBYKwp5OqQPCRzmde6o16Muu_EHFgKpouZhfmLD-2v3plBeYBgWuSNvjiIWbASCRWBRUyVu3aYqjOMddNmlnozkIsAIg7FszIpzg07PIMM5QjwjvC4vUNMYsmZi5C1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز :تو سفر ترامپ، بین مأموران سرویس مخفی آمریکا و پلیس چین، تنش ایجاد شده و درگیری لفظی و حتی فیزیکی هم پیش اومده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/120051" target="_blank">📅 01:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg6H-43fB6ijkkoOktD_2fcI58WWQ4XcK4CVg2khekaAfEI-oYhEeGbTVv17zeCbG046eg6qVu5_POgp6GHyIFvC2xthYo7UTFMAX3RomFvsVmznLS1U33x_TYv_9gzIrJo5y0Eu6A0_H36fgiN8ZuMixrWy5Sv4x6BYRWW9eWKoMu66V41W4NnKGPmm6N7K5TJ8Akv-Erbn2ScjDD8tbDutm91mzrdgYQFRmP4DaN_a3ckFubcC4ed5CaiYkvsmufasOO2B8z0GKDEVIWXjsXqzQz97PH1HmLtDlMVTVTUuNCtnl8fpEW-M7S1XSqYLLsKrIBe4_VpUY_5n0EP6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
آمریکایی‌ها متحد نیستن و بزودی تجزیه میشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/120050" target="_blank">📅 00:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZAJMi1y7qnpPfVaDs1zyzOBF-qaetRroZfw65ZbPD2ARvNUq8rezJjPx2o9sbVJKmLarDTb3IWgWLrSpBfmZK8Jfjs1dtMPJ10N9DBYRgorE4fH__PrxJhI10C0qkCLIFbF1apdKTdJNsf9kT4otsysamZQ8xAugryyE9qJVmMhtpxrdxjmMK1WUOHc7nh2_5842CECurnjd43ndb9opMJot_LyNjnha42vtCi9ui3LiuC0RJ-Irf77At9oezoHiqHeBsnsSnA7BrwIiRC8RFRHnTmjOeiyomhP8dvGGBPmMWJ4KVfYM92N4a8Pxr38mp7CDkbk74aD5mcQHm0c0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری وایرال شده از گلشیفته فراهانی و امانوئیل مکرون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/120049" target="_blank">📅 00:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3eNtTIHBzoTqstTKPCTuAlzIqzFEOAm6mcavBL9HP_-ysmhqY4mFRufZeFJJaTdt1jKjjwvWKt_JEeqSDa6d8jjRyR8TczOUmAevTN2yQ_Upo9I3bD_9GWadqg8B9VIUIKyiXfIwFt2vU8cuy5D-5r5P5t2p3aQfZrlYvW0lUGo9GIGITgJSQikhHYtM2crGPtt7qz-ByQtHwhhtZ-Qq7wPGMS2O9tDAt5P-IaxUt7MWpdYOQu41KoMRRXegKTlLqLCuZVQxWobkwXz5q2X9jeMw0GX4TGAYvKxIyZ1XvWs1BpF6ZnLfB-G2EYIVnrq1C1ijMcUUuYS1R3EJSsRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یدیعوت آحارونوت: اسرائیل می‌خواد اگه درگیری با ایران دوباره شروع بشه،تمرکزش روی زدن زیرساخت‌ها و اهداف انرژی باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/120048" target="_blank">📅 00:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/سفر هفته آینده رئیس جمهور اسرائیل به آمریکا به طور ناگهانی لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/120047" target="_blank">📅 00:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZcLEA5ndm-fJQs0n3pNvJ1EfejpQcOuj2W-1Poa18iG73jlVffPUntkLgWh7VNOcdOwjwH0gnbNQRrXI87wZfvdj-ELwRzgJDm7SFKVJ9gQ-zb20EoeXoZ-pSsoY1Ug8-hqxGqDr4h8g_AmWlIdgloxHVqnJ-wSX_SzhvZpRJ2dJDU4VDl6XtmLG6oTpstteOn9AoHqD9Ep-HQHjkEVL_A4tydQAq6CxlCrXJoKUb7tGYY0dK7FLQ0RmV6LfPJzIFrCqiwiz8ylTjZpP235fu_AU2ero4pZmYIpuxARTd3YLE5BpDf4-V93-HTGw8ob3jfcQ-i8DSn87YyrScVJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین توافق نامه ازدواج که توی دوران جنگ رقم خورد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/120046" target="_blank">📅 00:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120045">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان  استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان  ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/120045" target="_blank">📅 00:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120044">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سنتکام: از آغاز محاصره دریایی بنادر ایران، 72 کشتی تجاری را منحرف و 4 کشتی را از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/120044" target="_blank">📅 00:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120043">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه قطر: ما به طور کامل از تلاش‌های پاکستان برای میانجیگری بین آمریکا و ایران حمایت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120043" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120042">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سوپر اپ روبیکا بیش از یک ساعته قطع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/120042" target="_blank">📅 23:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120041">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhikVk0EoNy8n7Nmm_jP99CDPEIgIHE-azJPuVzQ__s_UIxDvCl9o4CzBUHMEhVfXj966tkLG99wuqJjbCr6BWWCnb2KxwtXpQWDq8adBqt9XeqOxCbvOT6deinAxFJIpP1CMWnfFD59_jqVmcQBK92z2ytx--Kf45_cgXwgfhAnPTIET1mMm2NYa-raggex8wNyvXOab16oKc8KWlNMXNt2mH1Z7ZHzGbdhuQLQ-C8JLgMhRoYSaRXR0QCJlWJNlyxwEBnK1EAcS5etENFmJmAiPH8R-u-r8jWJGNzYqZlfQDUUeMPAjvjAQ0Y70_H2WtJOMYy0CV5lMLvhYWuVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر قالیباف: پس شما به هگست، مجری تلویزیونی شکست‌خورده، بودجه‌ای می‌دهید که از سال ۲۰۰۷ بی‌سابقه است، تا بتواند در حیاط خلوت ما در هرمز نقش وزیر جنگ را بازی کند؟
🔴
می‌دانی چه چیزی دیوانه‌کننده‌تر از ۳۹ تریلیون دلار بدهی است؟ پرداخت حق بیمه پیش از بحران مالی جهانی برای حمایت از یک بازی نقش‌آفرینی زنده (LARP) و تنها چیزی که به دست می‌آوری یک بحران مالی جهانی جدید است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/120041" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120040">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ و هیئت همراهش در طول سفر به چین از تلفن‌ها و لپ‌تاپ‌های جایگزین استفاده کردند به دلیل نگرانی‌هایی که داشتند مبنی بر اینکه مقامات چینی ممکن است از آن‌ها برای نصب نرم‌افزار جاسوسی استفاده کنند، طبق گزارش فاکس نیوز.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120040" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
العربی الجدید: حمله انتحاری، پایگاه نظامی ارتش در منطقه باجور در شمال غربی پاکستان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120039" target="_blank">📅 23:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
میدل ایست : ارتش دفاعی اسرائیل از فردا که ترامپ چین رو ترک می‌کنه، به بالاترین حالت آماده‌باش وارد میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120038" target="_blank">📅 23:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
طبق گزارش بی‌بی‌سی، شناوری که ایران امروز توقیف کرد، «هوی چوان» نام دارد.
هوی چوان یکی از چندین کشتی شبح نظامی چین است که پکن از آن‌ها برای پشتیبانی از ارتش‌ها و شبه‌نظامیان در سراسر جهان استفاده می‌کند.
🔴
این شناور توسط پیمانکاران نظامی خصوصی چین برای کمک به اسکورت کشتی‌های تجاری در دریای عرب و دور زدن دزدی دریایی، حوثی‌ها و سومالی به کار گرفته می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120037" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkwC7PYjH3MHJCoYmW2sjzFZiwhV1Fs85DZyEnk9Oi2H2x37Znkhda_7va91SHjf8VYrH6cZWZppiJZuF3pmTHCmLkIxzIOI8G-jxeWszVrlZYxVqtdq66kTbaLwrPLsbe7huuSfsE1wFxEstv0Zjw521LgzWg-W3VykfuCBouMlZqNpcxp9p6E3U_E_79L8VKDvyB3LtZJsQ6vnYDF55lNlQhQRp6xwUYooHCoVY-jLcoBeIVFQlH10KsdN-qSokciGknn-dlh9rZjfFgTzDC2pcISqWj0rSyGmiJn1xXgohFh9PAYErl24jk-JMpH57sVv63a2toN5dPh1u3iPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدل شاه فقید در تهران رویت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120036" target="_blank">📅 23:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اعتراضات در کوبا آغاز شده
این اعتراضات در حالی آغاز شد که دولت کوبا برق مناطق شرقی این کشور را به طور نامحدود قطع کرد.
🔴
دولت اعلام کرد که "مطلقاً سوختی باقی نمانده است" و وضعیت اکنون "بحرانی" است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120035" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ea95d90.mp4?token=kxScCH-VQSeairBgpw6Z9xZMAjget5qZ33rv9w2n5uxt4g_d07v3MlrI8muXxjg-veMWecKbKL1kvSFmbzlu8qmggbyphywGMn242hMmoMXzApYPfEYFy-7vs8ueMY8OxN3pm_PnA5I_J9gbgjeDx8FRJGU-K6IHjeorlQmDnUflqWt8FwvyGQ7kx_G2u0t8bFmRIxzPV-Xz08GkOr5L7RhyBbH_niUTaf-jFcYTruxVB8veNoqUc4SuxgjUXqXEb9MPP_8ML_ezMWHkWV0TgiApMTnYKc6JHYdyQ-QmAEEbBkn810ygeojSD9jMDXdztB7_tV2DCkx8H0Bdl9zsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ea95d90.mp4?token=kxScCH-VQSeairBgpw6Z9xZMAjget5qZ33rv9w2n5uxt4g_d07v3MlrI8muXxjg-veMWecKbKL1kvSFmbzlu8qmggbyphywGMn242hMmoMXzApYPfEYFy-7vs8ueMY8OxN3pm_PnA5I_J9gbgjeDx8FRJGU-K6IHjeorlQmDnUflqWt8FwvyGQ7kx_G2u0t8bFmRIxzPV-Xz08GkOr5L7RhyBbH_niUTaf-jFcYTruxVB8veNoqUc4SuxgjUXqXEb9MPP_8ML_ezMWHkWV0TgiApMTnYKc6JHYdyQ-QmAEEbBkn810ygeojSD9jMDXdztB7_tV2DCkx8H0Bdl9zsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیندسی گراهام، سناتور مطرح آمریکایی با آشغال نامیدن متحدان چین از جمله ایران و روسیه، از این کشور برای باز کردن تنگه هرمز درخواست کمک کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120034" target="_blank">📅 23:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZjJMgukOmL9ZCydTP4diX1j9CB5BoDE7jQ4Sqqc9UVmobZS2X2U6tNeX-DjUThspkd4seJxbZDS1aPGilxw2DrbNJpUrX4CT7nQeswpLR3fZev0bR9PDjOjD9AEzhZJlpiW4utOBJzgdz3mxvHcwv9R7KSi11vrxIGvyFJWk4BQoDtZz2gz8aIeu5bQpi37oIHRDtmprhgyq0sGOZqF0Bk0Apabg2Oe2GJdLu-o0h16ri8HPrOVNxhz5zmJ5Vn3hQY-YYEw3L406hNtF3aocCeUPCdNaERhCCD2pKXBoUHHKaiOg5NqGN_vot89bTCNJ9MPBoTLFqJWGV04WkLlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
قالیباف بدون هیچ دلیلی مجلس رو بسته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120033" target="_blank">📅 23:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120031">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s71ABPB2QIZ6YLB635oR7fwaDHt0zzRaHWCFr6tOK8G8kSD8vcgmas3JZQDM72BhR74pqDvNXeTH3qki2ewJltLeSlgL0uSVe1vOIjIoM8ODyPsOqxsAi6bJc1xNDOHP4h01ac-PXNdOpjGtc2EhPuWQPj0StMLcNpCKYKKBX16s6qJ2KCRL0Q6v_tWluWeGFtoegieTLcuYIGFusLbwTJTpENKpYJbeZRJLpmaAvbik_ob3A5LnLPj3U_eMknl4IQsLhXMyVJ9twWdWjinti3tFQvFxHqTqwACBfds2vcpMs6BXjCU-H0Vc29KP7Pjq2P2ljkWkjaKao2pLfhf1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5H4goIltBDgGl4EoPePjl_4FkYTJ8EMXCKCUM0zUz1E6h2dc-06162NBmXuU1IPtU_Fgq0h308EIpxO8ysm0EE92KGMggDmcpwkDMDvthWsvYme57a4GAIq0R-BLDajzmuLvqWutY_J7g6dx3dQcrvWE1IQxwBBPz46a4Tzc5BkvRHE3xX6GzYYgTciP-7PeoXxqFHNgVKtEHldZXnKTQIG_uCzjNwq3PKdnQwnv30EUGjmTIJooP1EUUck9qOKAKKCbJmo-6FPlPXD_dRd5ZO5vw7OWuG3OgkBgNO8hFEDquOELmN8P8rH5sLT9p3FUvdkGO1LCHd26y3bDGWrVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل:
لامین یامال تصمیم گرفت با این حرکتش علیه اسرائیل یه جو بزرگ درست کنه و به تنش‌ها دامن بزنه.
کسایی که از این مدل رفتارها حمایت می‌کنن باید از خودشون بپرسن آیا این کار انسانی و اخلاقیه یا نه!؟
من به عنوان وزیر دفاع اسرائیل مقابل توهین به اسرائیل و مردم یهودی سکوت نمی‌کنم.
از باشگاه بارسلونا میخوام از این حواشی فاصله بگیره و اجازه هیچ‌گونه حمایتی از تروریسم رو نده
@AloSport</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120031" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان  استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان  ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده…
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/120030" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر ساعت ۲۲:۲۹:۴۸ شامگاه پنجشنبه ۲۴ اردیبهشت حوالی قلعه قاضی در استان هرمزگان به وقوع پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120029" target="_blank">📅 23:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
صاحب کمپانی حمل و نقل در انگلیس، یه ایرانی باشرف و میهن‌پرسته و برداشته تریلی های شرکتش رو با پرچم‌ شیروخورشید ایران مزین کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120028" target="_blank">📅 23:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آژیرها در کریات شمونه و اطراف آن به دلیل شلیک یک رگبار راکتی حزب‌الله از لبنان به صدا درآمده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120027" target="_blank">📅 23:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-UuACzudQI_SmOzBbtG2ymJcqmcYRGSbKzYmgNrIsFkIfWtmaeDnrFhLDnk8cNYIavIFVua9f6Lk4Jnw25oXjTqzR3VPK2rI_mqTTnF2UCp5lfX8-IgAjqhlH-O-t5IPuun3e9ETSbBva4Pby4sVSyI7nCC-vTjGvJDN8s2_9WSUBFuj0qMM7lCQtrQfTJgJxSjKBlOZYtBQzmT4aPxfwtxCP_Pywzx-oVqlgobfh_r09AvLVlQow4hRdGZVpuUDKaeLh4TGEri2PkWIhMbARLWRi9hFnGdX_nyNmeWjqa5x3qhRErC_h7O6CKa8L4QHnsPy6nPIVE2zSk2kO_4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژیرها در کریات شمونه و اطراف آن به دلیل شلیک یک رگبار راکتی حزب‌الله از لبنان به صدا درآمده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120026" target="_blank">📅 23:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc9058515.mp4?token=HhYhFv4EKY7Tx_BXuCL8150QjQzIXXKlBx4bnRA-l3zTOIa1Z0ZjPwrJqKXPgfB27-qvbO9AyWMTQfisXoWLKEBP-IAbDm7DYAYQoDozPsCxsYp4niuGVZCoBEFl-XOtR7odLt4zj6P5SjPYK7fsRoirXskhsQKkFcgEiaev0A-DH_TJrLZh3dwp3C06jdhMPikFmsT2BbBC1VeW6q_d1wd-yXGhWpZUIp-tt_QIujMye_D6suyX7h1mMb5d2YP_zQoa3gwJlhNkw6NTokcelnZbb3o7q7WFdTZhCg2fx9R5K0Y5kOYkR2IHWcyU4BnvKoJqIy8Slvw5mbJ7vXRwCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc9058515.mp4?token=HhYhFv4EKY7Tx_BXuCL8150QjQzIXXKlBx4bnRA-l3zTOIa1Z0ZjPwrJqKXPgfB27-qvbO9AyWMTQfisXoWLKEBP-IAbDm7DYAYQoDozPsCxsYp4niuGVZCoBEFl-XOtR7odLt4zj6P5SjPYK7fsRoirXskhsQKkFcgEiaev0A-DH_TJrLZh3dwp3C06jdhMPikFmsT2BbBC1VeW6q_d1wd-yXGhWpZUIp-tt_QIujMye_D6suyX7h1mMb5d2YP_zQoa3gwJlhNkw6NTokcelnZbb3o7q7WFdTZhCg2fx9R5K0Y5kOYkR2IHWcyU4BnvKoJqIy8Slvw5mbJ7vXRwCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : در واقع، منطقه داره به بلوک اضافه می‌شه، ولی ما ورق رو برگردوندیم
🔴
یران از همیشه ضعیف‌تر شده و دولت اسرائیل از همیشه قوی‌تره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120025" target="_blank">📅 22:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b1f359ac.mp4?token=Qqu07UcqYdG6-CEJaLumrhxRcQnApd3vm3IRIasSi4jqJxkXKDszQJHLxr99rBiY6GeehtV2H_n0VoJN6FHOwLZ20SJtyQNz8mXHpS_dwkBm_FcfuZs55m43N0FRLoH6_chdKesTO5lPti00AlzCtGURYVcYzxjEJz53WyBc0r3iwEimyrqv0fZJfh1AqiLvzyNqC2g83O4PMsgimm0pMw0H8g0EC7KePH3zBk9tM7LVlEFY6JihA9rWWDYvr2RTU8WbF0e0BX9SOtgXaW6QP96QBE5BLyvsi0dVVBrPisClWtxEqJTdH4iXPcdFelDRDGELNezFoGaxaS3SEHewAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b1f359ac.mp4?token=Qqu07UcqYdG6-CEJaLumrhxRcQnApd3vm3IRIasSi4jqJxkXKDszQJHLxr99rBiY6GeehtV2H_n0VoJN6FHOwLZ20SJtyQNz8mXHpS_dwkBm_FcfuZs55m43N0FRLoH6_chdKesTO5lPti00AlzCtGURYVcYzxjEJz53WyBc0r3iwEimyrqv0fZJfh1AqiLvzyNqC2g83O4PMsgimm0pMw0H8g0EC7KePH3zBk9tM7LVlEFY6JihA9rWWDYvr2RTU8WbF0e0BX9SOtgXaW6QP96QBE5BLyvsi0dVVBrPisClWtxEqJTdH4iXPcdFelDRDGELNezFoGaxaS3SEHewAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : در واقع، منطقه داره به بلوک اضافه می‌شه، ولی ما ورق رو برگردوندیم
🔴
یران از همیشه ضعیف‌تر شده و دولت اسرائیل از همیشه قوی‌تره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120024" target="_blank">📅 22:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-RpGzAogTN9Vfrg2Aab6lc0eOK2EUFfoJnqQCupUOYlR450n5X36cdkpNM3NGEEbpoynxg_8d52Ji5ivCW0Uxl5NI5UsZptGlswbMJeZL_pGARi9rQIuTofKtuAI_akIxSCC8ga4JKWBSpTAdY9Ap4vRT8uNjCXEjMBZdqIniWyOA84q2cxReoOhVBrK7mPYVVPhiCSR120hJEhHUl4iEA6nAERvfraCglRGvl339OOYTB7vosLJOk6rxzwoOTo3pMiuuev22HutvLMJEFS3Bek6uqjQolZm_2FkFBkb4PFhW94f4_XkBp-cYsQqBaW1qhlDyXp6VRO0pjpwc89sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارفعان نبیان ، جوان ۲۶ ساله اهل اصفهان، در جریان اعتراضات ضدحکومتی بازداشت شد.
🔴
خانواده‌اش بیش از دو ماه است که هیچ خبری از او ندارند، اجازه ملاقات به آنها داده نشده و او از حق دسترسی به وکیل محروم بوده است.
🔴
رژیم او را به اتهاماتی مانند محاربه (دشمنی با خدا) محکوم کرده که مجازات آن اعدام است.
🔴
گزارش‌ها حاکی از آن است که حکم اعدام او صادر شده و خطر اجرای آن با طناب دار بسیار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120023" target="_blank">📅 22:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
به گزارش Ynet، آیزاک هرتزوگ، رئیس‌جمهور اسرائیل سفر هفته آینده خود به نیویورک را به دلیل «شرایط مانع از این سفر در این زمان» لغو کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120022" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120021" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120020" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خروج مرغ زنده از خوزستان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120019" target="_blank">📅 22:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی:
پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120018" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
درک گفته های زنده یاد
فريدون فرخزاد
هنوز برای سه فاسد قابل فهم نيست!!!
🔴
حتما این ویدیو رو ببینید.
🤔
«مردی که ۵۰سال از زمان خودش جلوتر بود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120017" target="_blank">📅 22:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شبکه فاکس نیوز از استعفای فرمانده کل گشت مرزی آمریکا خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120016" target="_blank">📅 22:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120015">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل اشاره دارد که تکذیب سفر نتانیاهو از سوی مسئولان اماراتی‌ ناشی از ترس است؛ زیرا ابوظبی می‌ترسد به عنوان یک طرف در محور ضد ایران، ظاهر شود.
🔴
امارات در تلاش است است که سطح حضور خود را در مورد روابط با اسرائیل نسبتا پایین نگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120015" target="_blank">📅 22:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120014">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ظهوریان، نماینده مجلس: بخش انرژی کشور ۱۴ میلیارد دلار خسارت دیده است
🔴
۸ میلیارد دلار بخش گاز آسیب دیده است
🔴
ظرفیت تولید گاز کاهش پیدا کرده
🔴
پخش پتروشیمی ۶ میلیارد دلار آسیب دیده است
🔴
بخش فولاد ۲.۷ میلیارد دلار آسیب دیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120014" target="_blank">📅 22:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120013" target="_blank">📅 22:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما.
🔴
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120012" target="_blank">📅 22:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان
استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان
ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده روزمره در تمامی برنامه ها
✅
دارای ساب برای اطلاع لحظه ای باقیمانده
✅
تک لینک بدون نیاز به بروزرسانی های متعدد
✉️
پشتیبانی و خرید:
🔤
@safevpn_secureSupport
🤖
خرید فوری از ربات:
🔤
@SafeVPNXBot
📢
کانال اطلاع رسانی:
🔤
@safevpn_suportt
😍
کانال رضایت :
🔤
@safevpn_feedback
╚═════════════════════════╝</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120011" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری ایسنا : با قیمت قطعی خودرو باید خداحافظی کنید،چون تو جدیدترین طرح فروش ایران‌خودرو و سایپا،خریداران باید نیمی از مبلغ خودرو رو امروز بپردازن بدون اینکه بدونن در زمان تحویل چه قیمتی در انتظارشونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120010" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از سفر به چین تصمیم خواهد گرفت که آیا عملیات نظامی علیه ایران را از سر بگیرد یا خیر، طبق گزارش کان نیوز.
🔴
مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها شامل امکان حملات هدفمند آمریکا به زیرساخت‌های سوخت و انرژی ایران بود که هدف آن فشار آوردن به تهران برای بازگشت به مذاکرات و مجبور کردن به امتیازدهی در برنامه هسته‌ای‌اش است.
🔴
اسرائیل به واشنگتن اعلام کرده است که از از سرگیری عملیات نظامی علیه ایران حمایت می‌کند و معتقد است عملیات «شیر غران» خیلی زود پایان یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120009" target="_blank">📅 22:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید کاخ سفید تو ایکس : بازگشت قدرت آمریکا به صحنه جهانی
🇺🇸
🇨🇳
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120008" target="_blank">📅 22:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
عراقچی: دنیا فهمید دیگر نباید سر به سر مردم ایران بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120007" target="_blank">📅 21:56 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
