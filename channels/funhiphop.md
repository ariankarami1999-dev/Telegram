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
<img src="https://cdn4.telesco.pe/file/krBPw61ew_PFULRIPrGTKWXpJLL8Evj049T7u27wr83IlK_F-a1Z6xU-duDDJzLhLMnC4d1QN6PJXc7oA3A__MTaNwHJM6EwI9nLrXksWjQxSz5Ier5VHebf8ndT7Qk10SFp_FwVv7WgT6NOcxZZOgAKpk9TWGvPT7Dug7X8Bvt8tffxK1A1LiO81Ggup9J96-QDu1wRwSsV-5wxy_181hpt8s1V8KUoCDrQEQYVUmLHI6z__gIWOMo-qvWHDNxF9VjDOeJTk3VudOCPR78xXA_kZitHoaIur_D0deqH1R7B50k7FqMDDGo4YjAFD2kHC_Eng6FesKxKrkof9qNFpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 265K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP8aXjeM-xsRO4exImFRHW20LeI7wFUHi7ZgxK1BKj6_ItGySkkzoTR1nKqQypU3dJrfEsSMYfjEujenFT-KwhlpdkoT9fHBJ8HbKQivXZoVt7_sYZvLnrKnaP5znWUYbzbK8Sfg4yhlh7VPwGuAM9ThoUUiYCkTOtObKfXlrnAL-mr2u_TOvsLvd_HsYToOkog7UiiXm4OjqgSgdh-Q6ZrSP_DzWIdDkigUnU_2s0ZPi1-TBJxk7G1IADMEu-uCm12ltXwA7apax3BZCs5qrm1-vOcOfPmCqNP6tRZlRO9YxShUCXd5caILLzH0ohXIMi9eI6zqERistawcblD2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv_v5HBHOEOfVWV8PLZKLhv-Yy5jq1uJKND5ouqgPb4Obd-qKk4wr6xgH2IzGP1ONtVL9I7Udsgy9dYvTP79tMQzmbasWQiY3H7QBnp2mJyH5RAQae4HZ54hHRaKS_caCEYMhdKaVlhN3gHCpTEa7h-d87PQ94HRe_pTZYg8-Zmd23lKmm-UuzPTz4ETZquU0ZYpRnK1TlumFHkoihL0CRN3tq1bfaBe81U6z_PUIyNdcPVvIGuVM2UZaUhzkYHJbvkqbh3aNJBTtXOhFNYKAKOx8JjMzIjrsmaxekgh5jbjJS4FK9GYwPThVTNJv06z05XKAKOZJ06lg9N5hPMDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdnI0OIHBI8UpH1-Y5zycyGsEW-dWdII0J7ebhxOoXgsU9C8VtzH1n51pEtn47UVo-QHU75Sev43p0uWr0lA595X3rjlYwlAdm6SiX97xEE83lAR0L3YG5anTQ6NP8zmsNyXME2lHvGPgsgmYEiT0R0yQ5SJS8eVQTusTWztNdhaouPBZjH0Ld4Wz4PSdR3kAlspYu4SjqAYbuZZIbTc5kFuZb-Pi7MCjixEFV8b2IYWLR6-kkpDaK17wUnaT2DTLpMONXuMw0OHM7iuG16HhTI3ByWdgGEvxkO1MAqhdM8MiBqIxiLG--e1I9t0R2fVK9f8romO60OtthyNLHVkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhkjmO6zOxVqq0aydU-vVvkJyUQ4GKZmp5utzDQ4xF-BfuWK9acjscaIWl4v6k9NRA5zGiscCcRkHEktu1pUqwiZmuyxR7uXt18Swvmyr6URjO8uyIgZ5z4-RQWrMM8UIfkUNWNk3CJSyYbgufTOzja2VqU6HYGOz7U0R3VVugmXy1Pi4NV80VSGArQnhWGvX4Ch2ioBSjO9mn_rF5sMV2P_0YlDsvxS1nO4K86nR1rEciUwbteeG5VNVlQVDlPPvW8CIMiv5lVzFlkSSy_YZtHdYXFU-e399HIuwd8dZ9eygoMLROVK-3wKclh156czlf7xIDM5vCkRsha4V1mwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtYgIZbpMavYoNIo-ePNIqZtuR8YStJ4HFEOg_1VGUk4PihnrOCCrCu5GRTGwEvMkm8QaowA-NWxAEOBmyM3R3bsqLxiZOMGG8TPNn-HUiSJG4YiN0qSL1EKiKvYhN-FY2EI_YOmT2PyDlfWw0o9IEaR-YLL7dIdKTmxdK5qQgRSLYD7ZE6SZRzYh4jdMM7liQxvsS5z6FPUrFtd_Fl2KILLXCfZ9v73RZgnJ4JnzBQvDttm4nR3RHKlmWuTDCo-NaS9VwLdr96m-ambP0N8qbjkgf1Rh8Sua2uaW-dIQl5SNepXDeUjg5392LekTQ7SAsz364r7soYIlLDyqDb8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=jejYIefj2M0umNekX-g2M8EOoZFmcwM3oirBG5cwSUE_1-1pvvwGgzxK3uSF8SVfyGxJqYatF9fKvFNAGZfk-LGLm9xfS8BmDiopMDlZQczb6WZNdmtmhNMh0oDYHrQU0rmSQKX09wCaGhYJHHfYERvbm8Q213YjVB1qDpFdwIAGkOxaVxwp34petsq5BNL3-uvwy7uibD29hCUPir0FGABplgBCSH99bPjwp_oZ7QL9KkJEyYzxHz2FdQH-0eZy6VUqBGc3klvHGph1Ls07YGUUB8ScQzkAn6ibgIlUk4grHliIm2WExxsU-wdieY4MThIG1nRt33EwBchvmtqbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=jejYIefj2M0umNekX-g2M8EOoZFmcwM3oirBG5cwSUE_1-1pvvwGgzxK3uSF8SVfyGxJqYatF9fKvFNAGZfk-LGLm9xfS8BmDiopMDlZQczb6WZNdmtmhNMh0oDYHrQU0rmSQKX09wCaGhYJHHfYERvbm8Q213YjVB1qDpFdwIAGkOxaVxwp34petsq5BNL3-uvwy7uibD29hCUPir0FGABplgBCSH99bPjwp_oZ7QL9KkJEyYzxHz2FdQH-0eZy6VUqBGc3klvHGph1Ls07YGUUB8ScQzkAn6ibgIlUk4grHliIm2WExxsU-wdieY4MThIG1nRt33EwBchvmtqbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=kYEZ34SvwKkr9QnoSDH_YqPct0E0i99I1wlxFih5991F-5O4-vYwydUvItxvOA0myLr6ChS2jCP2B_gCGVl9qRC7KkF0Aij9RJUt37HVIxpypBzPEPghgd5qUYMsmvo9InmMkX2OdRq9hA19OWHtqvQc-DjZCO7REjKp_0mOalL8mDWBe9jo4JpVtg1xOcZ933APTWOBuFwTkwFZ0QOV2ygVtGHsfAbzR9MfMWBPhPpbCzAyzR95gHiH5djZCRuV1paFBZ9OsyMsh8Mbc4EvihReM87hBzHGV_bRWsSqTZhN9xX6gyybFV9HGv63xmrM4FGjh_FffDnEn3q59vo0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=kYEZ34SvwKkr9QnoSDH_YqPct0E0i99I1wlxFih5991F-5O4-vYwydUvItxvOA0myLr6ChS2jCP2B_gCGVl9qRC7KkF0Aij9RJUt37HVIxpypBzPEPghgd5qUYMsmvo9InmMkX2OdRq9hA19OWHtqvQc-DjZCO7REjKp_0mOalL8mDWBe9jo4JpVtg1xOcZ933APTWOBuFwTkwFZ0QOV2ygVtGHsfAbzR9MfMWBPhPpbCzAyzR95gHiH5djZCRuV1paFBZ9OsyMsh8Mbc4EvihReM87hBzHGV_bRWsSqTZhN9xX6gyybFV9HGv63xmrM4FGjh_FffDnEn3q59vo0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=iSmotwWpfqrhkizQVHlFOReBNETy0nAS_9tXeTWXFdz5A20YgclYO6u9hEG9OTpBlqCWoSFwFMZdHenYHZepjOQiqMewipx8xhi0gg42cS4w20ABcMFOSD-tO67afZWXWb1u6CnDB3S3XpNsfp4_lz-5xLBK5XVNrykVpWXxZ-ok7WafjN-MRZ25GwuydPuheFRZ2zGbpZcGBO3yFROLOB1zMLz-zaPro185dv3_0bIw0hUcJyWvXclPwsIjz-tujWZCHd9hinYR4x9Gx4e_oDtuKQ2KAxvw_y5MCXY7c4W_3RS7DQY1Vtv-jui4loYrpkPsA8l9VdZiyPzU9Q5Sog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=iSmotwWpfqrhkizQVHlFOReBNETy0nAS_9tXeTWXFdz5A20YgclYO6u9hEG9OTpBlqCWoSFwFMZdHenYHZepjOQiqMewipx8xhi0gg42cS4w20ABcMFOSD-tO67afZWXWb1u6CnDB3S3XpNsfp4_lz-5xLBK5XVNrykVpWXxZ-ok7WafjN-MRZ25GwuydPuheFRZ2zGbpZcGBO3yFROLOB1zMLz-zaPro185dv3_0bIw0hUcJyWvXclPwsIjz-tujWZCHd9hinYR4x9Gx4e_oDtuKQ2KAxvw_y5MCXY7c4W_3RS7DQY1Vtv-jui4loYrpkPsA8l9VdZiyPzU9Q5Sog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=JdBJ916dgpGRmzgO8J7qj43r1lEoE-t8O2MTywWvOxjm3Zaq3olZ0SE9HFUEU5eIAGxl8ZvTlTCXBZZKdon4YLQiwRL063Y-PvMwFKHvZR209e-1AjyG9om5ngQktj88E1GlBpG_JmxjoNcX4XLKko55jikkDJqVXgQj8fA8Kt7uGl663JmWf03-LSZDPnUQtCeLRdFCEYGEF340JP1FyR0_9ZQ80zK7SGeAnbk3pYquCB3S8FS0exCmI3ouFt3eB4-ppWH4xofKdtm7xsKrGyQaqaF87ixQw2lTuUlsFIiMov4BOH0ihemgHQ9Geiwe3ZhJXohR2D4UnI7C8s3fTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=JdBJ916dgpGRmzgO8J7qj43r1lEoE-t8O2MTywWvOxjm3Zaq3olZ0SE9HFUEU5eIAGxl8ZvTlTCXBZZKdon4YLQiwRL063Y-PvMwFKHvZR209e-1AjyG9om5ngQktj88E1GlBpG_JmxjoNcX4XLKko55jikkDJqVXgQj8fA8Kt7uGl663JmWf03-LSZDPnUQtCeLRdFCEYGEF340JP1FyR0_9ZQ80zK7SGeAnbk3pYquCB3S8FS0exCmI3ouFt3eB4-ppWH4xofKdtm7xsKrGyQaqaF87ixQw2lTuUlsFIiMov4BOH0ihemgHQ9Geiwe3ZhJXohR2D4UnI7C8s3fTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBa7yb-eidrbqcjlFDotr1DvHV8VreplPo0e5kucyudUJJun7fHWWgau2EG1cKKBjjkQxtG7iLWPQCDXhbEFsj3zBVXUJ1f3iVcOZo34mVv0H5JRaWOmC8k56DR844DpcmnrsbAi80suK1w4jRKBTFArGbRYhRgBF1fc5qW7qh--mKQbE1AliorhV9AzHfLAppGs5N6ElP_hfTWist-KtQTF8uB_4pDmFfJ14OuClKPAHbw9kgyXlGpgQYglSU5etZWgXsamYxYTvH6-m52OjvbLQBR8IKb16PjaekKEzfb5wYscyIv-2rJ8jtafvv7s2tYsgLtDSUjQW41O-qH36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROmw-aciwy-ePFYYoWjgqNWN2a3dDvA1GENVC09M6y8ggQpOESaerRB8wSU5OPcHmMPSHVwWf7SPLYYnWi8o9j1-fIdpkjuspRE4dgehrSlNRAfdk81Sk6P491E2Fki8Jf1C317CW-qqa3ES9I9CPhMOYZ0iL_GRmHZ-DHhfu0IPuhAKqSFU7enlrt7LIPu5PHJZawFU_nDYzQvEiNMJmMfj4s9TRhn_qHmWJZzCgNcoJHBcyVOi6hevtcXL_q5zAOVu3xCeIs5ihoSgI8iPrB42AWX-zkFIeJ5GcN3cAsQFNw1wqrI3hWdaqwQAW-VE9F8IOmX78ZaHVRdnErx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYLJW1CXC61eroQM9LStxq3ScIzRetcmUPXOeHthb2fBGOVclwzliXOlbDpqMZuRFtjNjL9NSJmmPnEx_AOdgsZCZ4wkzM-vzGDoV5G0nI_5rDd_Hy52VjsLHrC5BSLLv1nZT6QkcVQHw9FWE2IFcd3fYCS-k0u__sLOZxAOpXlP-v79XAqVG6elt1HoY3mVDqjArpV2JqDqlp1wF05CTuN7FDetXw4jPQEue4NOokrOy4L3Bqfu_B7vVS4_gw5i141Q62xhxk368f67O-HafXEHNIPHb1u8inwl8AkfbtuX67u8iXIUGArqjSYPj83MjG5LtQzpOFSxa9vikiNu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=rgvw5vjvz_6OwCUAKMX8KApRqlMFwJqGmrElkjKDsnxhrlz7TwQobKrjierq1sOnnlHm3hPH1YV21XxVeBW_fVtEeVsNWvtFSmRXbBrbA9jV7rZmGBb6K8-I88S222eFVeyp_JzE22cuBIccTf_xok2gu_6PR3DFe8B9bUW09D6MlVSRsxXtIgb0Segq4sWEaf47qGRaV5sTB43jMdIxw1ebIiFBTsZDsqghMp7HGnAfO5UE7XfxVEAlYef6sS68UaHQDkGb_0Ef2SJXNb_ySYwG1pIkgYWrMrOqS9tymW2Wjm_0OQyI0_QVTzcKglOVmrfOToqTtidPaGGuvOWUVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=rgvw5vjvz_6OwCUAKMX8KApRqlMFwJqGmrElkjKDsnxhrlz7TwQobKrjierq1sOnnlHm3hPH1YV21XxVeBW_fVtEeVsNWvtFSmRXbBrbA9jV7rZmGBb6K8-I88S222eFVeyp_JzE22cuBIccTf_xok2gu_6PR3DFe8B9bUW09D6MlVSRsxXtIgb0Segq4sWEaf47qGRaV5sTB43jMdIxw1ebIiFBTsZDsqghMp7HGnAfO5UE7XfxVEAlYef6sS68UaHQDkGb_0Ef2SJXNb_ySYwG1pIkgYWrMrOqS9tymW2Wjm_0OQyI0_QVTzcKglOVmrfOToqTtidPaGGuvOWUVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrncSWWozVRsy8NNi3LbuOhWko4qBBgGW-icNmIHbR3tMker9IKf0U6hsPcVlaTBbfXZmkLLpknDKPRbzBR61g-RgNm2iQWYgwTT1BG2tGq9blmVj3NVVsYp_ogVzyB7M0ewn0wx8dFGPOZN5K8bFhnkuu7K3-Qx41SLLLoQTEUc0dsfU3rCXUNL4zn8pci-BBIYakAdToFGNp-0Cs4r5Mfu0fPC-EXTsujQgddDRXxor-7COGDngacA5XpHn7YqSs2ymD-HWbzfxE-qi0wdyKJaeIjAghmhZNIHdQsdOMjo3g9JfOO8bw3WBlUDi8Wq8_oDW6pOhvnL7cDrrORleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbFVT59uNHFOe6GoH-taM71ZjR4Mo-92XbCrli1-97VdJ6JhAAzS3vQqiCoodYSNDr8VXBJ5XjDyChZYkU6AHQtv-7rjWThahGA1OqpwdRySpqcfGc2--OYiN7hDj_JZVgDbiqLobwZyb9YgSghnhfyT8orfKehlHIEiV5MZLr27Zg4zdk_rND_qQN4e3hhTU_FbqkCi_iRpIqA-_oD3_fQ3o9zYCJvPqFtU62KFgAhliQAlq3l0S9l8z3v18hDFrXp6h9IxCqII26LDLqxiXdy_V49iMJclcs0yFsEkHNPAkv4H2KymR4eGm9UJ_dfjctkGhQZXpXFpsziYVBmc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWzTnObsBxlZsB4_mnpOj1oOZk90xMRPHc7nK9EiOCFaPAK11BFpJrYvay91wt5Dpta9Tiu-C3S92gE-6MAvAgNFKqKTNQbZ4lEiFFFH8h4AgOqXF-wQdblxkiT685jZW4UkQJLLQZLuhXPzV9DfoJ2zu6lHToeWL25o3OjvwANJQkrvSFg5wzoC-mXqegC9FuNMeOtmSIa8naGuDjrfuHwGV1XCHLYQ1HDZAvzbOehdwBlVKQEl6l8IyJjc1u7aDcEhA5l4qDv6_K78XALyN_h14_sv6pDc4kOCSBbskKaCWJOURxDJZ9wMJ36sLTcqE6huT2VKflhliUGslCIIhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=hwgUCpI9SfA_eK2cfO2ChUJtEWbm57S2RIqSBrlPPt2GC2BgXLdIARg7WidafS6LWNOSB95ec_0yYhYXInr6MlwQC9c_2jgalinvsUDCi5v5hKNw1GlzJnxAnVbAOr9NtByVHeGk_EQfBk_oyM0QEJD1E0zLZmvdpcDzKI0lOdxCZ2zAgMDslCg4ZQlmruVAvaK5ZjIeme4yUgLdIfByoJfnCdUthIhZp6rPbeAZL1-224hbqhTe3tNKav-3yuCI9fjQk1NA7fPFBoV96jAAVxzJ_l4Y1UZsLEDuCMzZhhohCs0hohgdioAEAnW2C3BpDRQO78iWjOGeiVHVeawGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=hwgUCpI9SfA_eK2cfO2ChUJtEWbm57S2RIqSBrlPPt2GC2BgXLdIARg7WidafS6LWNOSB95ec_0yYhYXInr6MlwQC9c_2jgalinvsUDCi5v5hKNw1GlzJnxAnVbAOr9NtByVHeGk_EQfBk_oyM0QEJD1E0zLZmvdpcDzKI0lOdxCZ2zAgMDslCg4ZQlmruVAvaK5ZjIeme4yUgLdIfByoJfnCdUthIhZp6rPbeAZL1-224hbqhTe3tNKav-3yuCI9fjQk1NA7fPFBoV96jAAVxzJ_l4Y1UZsLEDuCMzZhhohCs0hohgdioAEAnW2C3BpDRQO78iWjOGeiVHVeawGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3_g6QtqmaTF8FaPTz8JgT9DYSDqM_OwBAf5cViHckRu8w3k86wGbXDF-o8jkfvxrWB7CdpaQpzEu7RzwYv8d9VYvgdkHGdsBYhoQ3IeePKFocfJz-tnq1oqG66W4vy0QG8hYQngwcZcXOsXZiwBA503JPSJTiBkj-X0aADX7PYCZ5ZwtVyZdtx0XlGsLgyuMKwwSiwbapDNWGJ7C-Naz5HDUW7zhSdOB1oksRLTaa5RYwUjINtesXnpGgEw0AaBOiDMrIDwYiy-J2-aZz99H2vqyGqJcJ64aQ1maNXkwAW8Ax1wRQTYqGeXp3tg_6nO9Qgl8mWRSaJOK-m0DCoRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDWDbGOja70IGVMK1pKtiQLv7bbsnipdOcaWIryf1ymNoEatZUlxHNi8YXMZJiFMUBuGCWGEvwuptkMyrpvj2cOrdMjMpn_ZJaVetwkX77rybW-4T2wuXOl80baotHxuxW6NC_f2bRw9OU3WLeeXvoK-QPbwG47siZ4aF7ojXjh9WbuozEnvPN9X_snlvKf2fZJRTE7tN9qIGlvd3AMgPkezC6R45FqvxJ-1R2zVU9l3-NSSAv-Hn8ktvtpRyjerDRJ4TG6H5OjIfG6HL1BmZC2MQpApUmy3GVemJNvsTobocbdgxSyXgdxS_cJiIdAhSdWPa7iK07YuTrQe0i6rXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=uLQzyYw56anYZPOHHqo8MkZhQLJdaSYo-I8ryORM0gNjrsPQOylxRNe71xtiPonyWy2kNpGSI0w7YuDK4tKEkd0kBxFqgMTo6yXMMjCq_ulyR-81JccJDFu9t5HLWvk3jnZpA3GcOAJVFwMNhWHBkQHWV9zfaT4AvH6W9iOhjkZIkrCarx1dg3iQyJDIL7FtW0fUS6gFoBmMr5nze20_ikG4tRVLPPn7C2nv4SDkDj3bPLRwJjsICsr_H_juUAQ1ynWhpie81EqwRfZv0V_6HVHq9gZ2w7V5G6hWT26YLrnSrJHpEftwNzlm_3kCBrf-c5DUn03WHXEvzeMX43e5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=uLQzyYw56anYZPOHHqo8MkZhQLJdaSYo-I8ryORM0gNjrsPQOylxRNe71xtiPonyWy2kNpGSI0w7YuDK4tKEkd0kBxFqgMTo6yXMMjCq_ulyR-81JccJDFu9t5HLWvk3jnZpA3GcOAJVFwMNhWHBkQHWV9zfaT4AvH6W9iOhjkZIkrCarx1dg3iQyJDIL7FtW0fUS6gFoBmMr5nze20_ikG4tRVLPPn7C2nv4SDkDj3bPLRwJjsICsr_H_juUAQ1ynWhpie81EqwRfZv0V_6HVHq9gZ2w7V5G6hWT26YLrnSrJHpEftwNzlm_3kCBrf-c5DUn03WHXEvzeMX43e5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSTQu5AlbDZgvqoDkptfLoL6c5hQ1MPaGWxi1q7bUGWK0T7N4tuzQ-ZF6YaMSZRTSGGQcWOEMqfMmQjSThnBSRrSyY_-2fMkyUh9QORbo0EMurJEsBYUDe4PRV0ctsA1fCoZeQ7cLS2Q2XjYmmf1UK24VsjYMO96z19QBy_Dhk7i2rsxG-HLUplcvVxh-aZ2I-309SKhzvuFn__AtUxCUM6GcEYdWLZJbqnZlnR0-AAOd4WI366z8Xk3swV_37vG1HDOSTQabOysZZEy4s3pNL-j2ZGJB5xFtiT8pN1-mTTAc2JVxfKn96fQAIYz3MVlFgWl8GYkRvSQSQWzMEGcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=uMOqv9JBXZvgHJcEqI4HpjpW5GmR1o2COkjR3jJZWu4ZlUIET-tWH66uf3fjORRxBXkVySSur4ZNw0DckZwbuqB-Y78zTJ-Ad0LwKju7-zlbwZEpeMQNJsdFbPnH5eVyW-5fj440gs3JjrC-_sQNZV1ehXs8lQfika8AZFZNANhZBHUaTC6AxyfxkSchuTB1vf0bLhvmCsivUaoWgMKOlii0yEbWQh2sDeFGRFana7BEUmf-Lxa8S0P-_-nAobSeabz-UM-XZPXc9sSbZ6ZZ4e82MViBgBPGndZYxhwZw1l9Zf3JF0QONYb8KEx0Pg3XzoECvjchn_E-hSckRLWQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=uMOqv9JBXZvgHJcEqI4HpjpW5GmR1o2COkjR3jJZWu4ZlUIET-tWH66uf3fjORRxBXkVySSur4ZNw0DckZwbuqB-Y78zTJ-Ad0LwKju7-zlbwZEpeMQNJsdFbPnH5eVyW-5fj440gs3JjrC-_sQNZV1ehXs8lQfika8AZFZNANhZBHUaTC6AxyfxkSchuTB1vf0bLhvmCsivUaoWgMKOlii0yEbWQh2sDeFGRFana7BEUmf-Lxa8S0P-_-nAobSeabz-UM-XZPXc9sSbZ6ZZ4e82MViBgBPGndZYxhwZw1l9Zf3JF0QONYb8KEx0Pg3XzoECvjchn_E-hSckRLWQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXjWTPuoY3zgoYlEgzzYwUWhqxzirF0w9-W2yjyF2U_c-8EQPP0Fue6eJ9HekUcvQw9s28ZbhRCc0pkrOizA4p4vUDd8iUqQuZeOsNRZx1E_F_O2f9q28PIKlBfAMtu_Tgy7_fxJ_E1qFy8S_gKu5qrThnK1v8D-9gNqSPyAr_F8-QhUS0tsq4xpZOdJurWU15MgTbz7yPYxNR-JUWCtm7JdT7Vj1tGp6iXZOMlcIH6XmhNU8PQb25i_m1HclGnem34ZjmVUMSIJ6ugxmaxLfjVpHd0eL-nHDzf7Bxay1OTurGo_R7gpeG7A1bC41CHQiukLsLdNDwEtTcVyYUBxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpqvkEwNj6mNjDnn9aq6KARUY5zgOFVZpNQSaZXInrHtokIqfnVUsI6gVnYOQpqF5YosoVJWsUp-No5MNxuipzB4DyJ9CIkgcAxRGD-3ul-OiSKyDHGJH5UaZ3OkXhWRFtu_nS-0YdBHRFSA_xa7YQQCJompGciHMOSEafdtnHaR66-4hjT2Z-eCX4OZzvg4CkQtXerJ56eoDYz0ndj2S9ssVGT1KcKhVLpzEpSI82AdooU_5xSTeRJdSCIv1ei61ifEO1YNK4s5TzrPi5a8flYbPRxvpKw9zauuc0AklUGewMkfxCjECZ6CSVA_64DlwndWMHIXciDNE1QupkQj0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=U4zoR3EZIfr3M9cRPXkI1GSksvnfUe9El_DZeUWZwhm5vkeivQBEvSN7WjAhkGTTuMy7d7RL4HsGRRJlzoij5reSra4K8aZQcaIAjdG_OXqqPRvXHVIIDRZ4NhXdGQQUKulBBphD8GYv1-X3WoCk2ZwM7wGnX8SYBdrT4TG65f6Vfjs1gGLxmpPOJdaTfx3adAdy89bfWGczYr60OZLXFB557zEV9v8Qt-3IkHPNORy2t0njzpwx4Q2hoKtK4v6wG5C2q5ZJZczLL5tEQkVcR9mDYhhQORhRqI1fSEgyZ2EFmNcihah9T8W7lq68Pgugm0IF1WjwIyRG49G6O3VI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=U4zoR3EZIfr3M9cRPXkI1GSksvnfUe9El_DZeUWZwhm5vkeivQBEvSN7WjAhkGTTuMy7d7RL4HsGRRJlzoij5reSra4K8aZQcaIAjdG_OXqqPRvXHVIIDRZ4NhXdGQQUKulBBphD8GYv1-X3WoCk2ZwM7wGnX8SYBdrT4TG65f6Vfjs1gGLxmpPOJdaTfx3adAdy89bfWGczYr60OZLXFB557zEV9v8Qt-3IkHPNORy2t0njzpwx4Q2hoKtK4v6wG5C2q5ZJZczLL5tEQkVcR9mDYhhQORhRqI1fSEgyZ2EFmNcihah9T8W7lq68Pgugm0IF1WjwIyRG49G6O3VI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=ScJxrEeOqw3dtF83VVm6DkSY9v6ydZDPZ8_kXg02muJ-sKxMOXPa7DU7aEgKzIHS9s8tSAeFudxSFk__1kplBUmTz_vRrK9atXX1fcs3fzpN2FWze6wtcjSeoQPKsQSPN3s1yZWQ0HpZ2O1WZGajRWStsBp3jLnuxnMFhRTxg7U2KVyPr1lD8y3XI1IeXvp7H1GxVSvLsMzc4aR_jOnaCDoFmETpEBnQZqLmGSVBgkJRYHRvDCBb5atXUQXxAEmfY7zTF8XIh4AdnwC_i1OripveQkkaH-aOJXbsIw5uoNiS1oqz77Anh2d8Txk1bWUVeC8Dq8J-7vlq2obJVTcqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=ScJxrEeOqw3dtF83VVm6DkSY9v6ydZDPZ8_kXg02muJ-sKxMOXPa7DU7aEgKzIHS9s8tSAeFudxSFk__1kplBUmTz_vRrK9atXX1fcs3fzpN2FWze6wtcjSeoQPKsQSPN3s1yZWQ0HpZ2O1WZGajRWStsBp3jLnuxnMFhRTxg7U2KVyPr1lD8y3XI1IeXvp7H1GxVSvLsMzc4aR_jOnaCDoFmETpEBnQZqLmGSVBgkJRYHRvDCBb5atXUQXxAEmfY7zTF8XIh4AdnwC_i1OripveQkkaH-aOJXbsIw5uoNiS1oqz77Anh2d8Txk1bWUVeC8Dq8J-7vlq2obJVTcqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG-I1WsxgWkJVc5VuBFBam33zZvlCNfS7c3NoeggdXzuHeeIyBjO5O8nOEBuwgQ5xTMb4LcU01cVmDG7dAWjqFmFW0LIiUFmiNlTmqD1inGn5FD6c3MCnGbN80UMURItfABTq3C-ugbUPgOlTA9wMBQBPpKJA0PhHeeO5kjvBcLOrtdYXEn-CZ2QXt-DKysqCYWx5vydWG6MFrdXrju6eqV8AjzTlidli-5uO5nOdMUHkRr04tUolr8wsyVwsUwttsJ7xuNVjPKjUDNxsO5Ghro_BuHycmOwfLxe1Q39wrtyydAd8s7lhrdxbU7fhSfl7EFTcVyfZR1eNNhfb3pSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is-vhLpoigH2UUy2d9_9dplEkYjL_2JWqFRF3ZdnpAXmYaRnKy6hBV4B85oDLNJaoc1sRJn96e-EejhaDF2PKm6jwEAOjAQgSF2HKFz7pTCeji6oHkjMMroN8wDrAzfFjreDKFFgQXikBuUyszMyB4M2-AKWE5MuLAXeSQxL2oGUV89yK9NmJ5OOF2gQKFqB9maMnTraGoI8kT2zFmA21K4hzfTx9W4r7UD1uUo9roZ_bzw7D-cT_wrULRfV8fVQvTtPbRJFBahAMFNdyMhODvdEf3smMzuaHrWsGAyIdjP9EQ4TjmEjLbvFCqL-4RZGCAqHhl6wG8y6SCdd4xuVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXXfmz2LfsnoYtr6cxu_5W47Od3BtlD_J5F12lRo-Af1-3w8X8oDs0ciGuF8KyNXVmuLun_eNGHNR203nWKzAjZA5aPbnp7wd3PeZPqW8D7s_OrLgor2kbeslQlN7NmHioFoNbrNj74pGxo1mYMAGFxPms-NeXUBq28cYSTLXQmFv7Neloppvzxs7eirXy4T65-zUsFT3HOQlWSFrquvxLn_suXNxnTpsv91vswv2YyL59tp6BHcy2DC5h9hjcnVYTtpQucfHnc5AVBIqtyXxAay6rq-EETgU8FO_Gy0SQH0xBlqg9VRkn_D5Ns0n1_lZZMb8xsgRE3d0K5NgtnLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=g7lXy_CmsF4EQiRV50HfbpxKGGJ3rEnQgFPaIi0PAk-ZfSxJl2bhHwYL8jAbYfZAFhBFXt1j6KIZ_1yat59_13wKWEmFNdktkP7a_gIha_UqVR2izzpEMJJjYbw_Lto8KsiPlEoIm9NUfPzXS1DoCP-JkqgPNTN7ilPfazTmjp1EKtt8OY3ss52Gz_jpE8bMRtOmcAWWNRvqoYLi9cA8QWqhV0S8_4TH-b8MoaDIvjSrgi0VkhF1_4rlNg9W0VOQDlp22VJEkx5hrqxmbbsgzK5EXjaCo6PUQNvNSF6D3z9Oz04DM1Z4e0CBg38fqbv-T94pfKkPhuKR6-9fAxu9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=g7lXy_CmsF4EQiRV50HfbpxKGGJ3rEnQgFPaIi0PAk-ZfSxJl2bhHwYL8jAbYfZAFhBFXt1j6KIZ_1yat59_13wKWEmFNdktkP7a_gIha_UqVR2izzpEMJJjYbw_Lto8KsiPlEoIm9NUfPzXS1DoCP-JkqgPNTN7ilPfazTmjp1EKtt8OY3ss52Gz_jpE8bMRtOmcAWWNRvqoYLi9cA8QWqhV0S8_4TH-b8MoaDIvjSrgi0VkhF1_4rlNg9W0VOQDlp22VJEkx5hrqxmbbsgzK5EXjaCo6PUQNvNSF6D3z9Oz04DM1Z4e0CBg38fqbv-T94pfKkPhuKR6-9fAxu9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-f7if70DN8FZCosfnritk3ps3Ncl48zyM0jq_nC5cG7QUML4GE4LPGGt3_hW1W6e41shV2etU2AyNvOMWnw8uAtNAdunXFgk9DHJRovW4Wo6ysY404typhRvVU60cJfe9eUwERWCFU-sd3QCnLtUrJNEYThaDFkle_qubbtV7xGDIop_1HhJ7SIRN6oIGKh9OHy_shiqcZb2ZPwBE5OhoGH_6X3wPz0I0oPYGkw6hUah5fOzcJilcFaywkTskMIz2O3xj7D8XvcNZ4NJPkYzNkNnoIAB3lmbkr6U5o8pXklfJs_Mo3V3VitJ-4sRnvPmIHz0RiT_NDWUE58t5SHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJG-Ba8qNVJzSzCmjsbvyAEQ0JVdHHtV4XT2EDT3WSuIM0pi53jvUqdwHKG-r8S-MpsTgzS39D_FLzecjHBVHFB4BrAkERUnkbNdihV6wJNav8kjZi-Q-JOJ6s7ftMG75md9YLeMaaarT-eU5CB44anwF4t8-CccccNmX_qabNBwKSVse4Xf36ZncpR03Y2RNGEnJRMzvuobwaMUlOszKSSoHWpRfuyitqkbTJg6WO4ilg2d-GVe5omDgOJYiug-Q1QeEteCJrsxBGN6Dwmz5hzRjGzIlxbYR1SAjQA7mR0e6PH88i8FzA9Nst7zDOgPvbB1YB_K7ibNo6MQCjPtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=r7Q8tJorhN9tP_wDrb5h8YNJH0Ih7lftfkcFBsQzJD_APyMigK7SGbIbp5WNdP648Gt9BktgVngCFIL7g5xjGkb-S_msu5Lo-PmnxgsGaXtYrjGFQhGBcUNqGQzQn9HKF1K8PXkaliW63CW8HHM7tGbqoQRhTIChOgNL8vK8LxtcrRVhljHID9mmTDP1UUFEXpU002N23SxYspB6RzIa1uwIshe0sdtcug8I52dF947Fvgh6fTWnXclvOEspQGkDGTI7fNiAqvhB-ZP85gBYXBj8PzutOIR-YvXhXy7pSzH_avNS6u9Jh_4CHpj--Hec5FGUYYTKLSXnPo91y_FtgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=r7Q8tJorhN9tP_wDrb5h8YNJH0Ih7lftfkcFBsQzJD_APyMigK7SGbIbp5WNdP648Gt9BktgVngCFIL7g5xjGkb-S_msu5Lo-PmnxgsGaXtYrjGFQhGBcUNqGQzQn9HKF1K8PXkaliW63CW8HHM7tGbqoQRhTIChOgNL8vK8LxtcrRVhljHID9mmTDP1UUFEXpU002N23SxYspB6RzIa1uwIshe0sdtcug8I52dF947Fvgh6fTWnXclvOEspQGkDGTI7fNiAqvhB-ZP85gBYXBj8PzutOIR-YvXhXy7pSzH_avNS6u9Jh_4CHpj--Hec5FGUYYTKLSXnPo91y_FtgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lrm347qiUyt2LEIdoU-hV4RWuRHRcnFjNhsr1gmGNltmFeOZdLJJ1t562mpTGX5n5KWyc9NFbzVDnQzeLVV9zAgd8vgLFDhHKfcATIh66VHi1Th7awLSVBWZfVlMxJDTo_yTsF3IZNxEA9mWvlhnRcizJEGUL-1bk5UHuxyFXajXBYEJsq8nMWxQi0FgSevadZnNlxjZT6WwLI08VlLTJeh4nptpPTybP9mCtLdmGsuoA_En3HXYQFnAporAMPsek_tNARP9yo1VMFJb2DywSk4TtwZtZxw9HHWFTySt1fdw8-iD32xt86FgleC4VUaTQZmgwgC0nDh3C1e-U52DFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQtU2vwo4hdgKF-QA4pzHGxZRMLJNlVYwQlATy2p1spEc2zwbDl9r2-BFvyGMvn7uFQf99zVxxdzgiZHr6CctC8vZYw5-yCbXyvAPxP4Lwjytt6p4afw6LCEaWk49RLbj91ebtgt0UzUmehnEFR2li7G5WAzf388I27HcmCoS4DVBmMlJoVVopA20bqNVfVZ7FnN9oUnCQLGsuxIVVk3Uv0tMvJbEkzrwTbFe3n7bhFl9q8f7Et8KEDRHTRT9U2KfiGBNHTGgCCJsaHAZfrFZ3BRGKCt8_kIaL27rhDq9inQqlcO1jqEGFZ-40761oEggyyhCoeADsDbHL1kF0DoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crmaWhQLLL1opdGtRa0rQzKXlZNvlUODwfxYZGlTKC4nuM97l5UlAsSKBCZap3fkcCJoCd11gWvyeIU4uXO_pKjT-e7IS_s4_0NpHC_Y2ii15fVpKI3uVkvL7elqzOugPeDI7_Sdm7h4Wx7SQ9JipviDryztWYOyk_SXOhdTIFkvqPCTH_TBg_Kwm4KwyNbZNh18uqG6Vlk6jnczYaILBixMsCcnOtOi6ZFMmwcnBM_gGtjBIO_KePRgixSN1WxxHkS4VWAz6_Rv3CkqEPueu9nPN-U95X-Swq9kxKAAE9xNh3lJPq--j5GLQ_hNaDt50bMVB2zTNCd_TiSFQB9yIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=EOAcjOEif1sLdL0RkvnmL06ac-byt9Go6LPiqBzBlAitdeJ1LGI2rsqnntaQEBmvssrwHqsxzpLhzxgqQwKdZ9hWAO4XKYl6lt9cO_Dj9oM3Gv_nV3kGysH0BZ80tQ4O9BBr9w_3CNq8QuEsbppx9INT0hfkJA0I-6LzAISgKT3wC9-xoZ2EEyF1BmR7XoWuEnxuO7vVdvoJfBS9btOjwQAJLjK5SqQlug6iaw8QVXnNWKrnHhXjjZXeMytljzPPzKmbwkV_zpTp-fhgHvQrvXQd0Q4ffVrHHQrGQs-8XHSrsWSQVovGjQY4JUriWuVxcfzJs6IL_D4E3WrqHnwlfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=EOAcjOEif1sLdL0RkvnmL06ac-byt9Go6LPiqBzBlAitdeJ1LGI2rsqnntaQEBmvssrwHqsxzpLhzxgqQwKdZ9hWAO4XKYl6lt9cO_Dj9oM3Gv_nV3kGysH0BZ80tQ4O9BBr9w_3CNq8QuEsbppx9INT0hfkJA0I-6LzAISgKT3wC9-xoZ2EEyF1BmR7XoWuEnxuO7vVdvoJfBS9btOjwQAJLjK5SqQlug6iaw8QVXnNWKrnHhXjjZXeMytljzPPzKmbwkV_zpTp-fhgHvQrvXQd0Q4ffVrHHQrGQs-8XHSrsWSQVovGjQY4JUriWuVxcfzJs6IL_D4E3WrqHnwlfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=PqRbq7KBsrqhhYBSur5XbdiKW6Ihy9MbMr1dB5SZ1kovCEsqv7jP2ALVm7okEMwfwGtJuiyu_CmII4ptPsdHZDWZAn08MSxrcL0wvsjTQcKmD5dn9ntrfXEC0FReNqHKvw3BT7q9yn2e9Rjd6myTX0Bx2Lf367xcQzwl6aE4j_EMXraFT9TXcWZzuziNRX3OTJljYEqgwLogzO6KZeVl4S89d8-dv6WpwMOgoeglJ-4-1SlO-1VRLjmhb0cCjPGL7UB4YVEY94RVznz91KGxpYfQj9dQs6kEXaKhtvu2eJ9qpo0qb_Img-NHu2FRrCM77-pAYJbdMa2Qdy_ZtHFecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=PqRbq7KBsrqhhYBSur5XbdiKW6Ihy9MbMr1dB5SZ1kovCEsqv7jP2ALVm7okEMwfwGtJuiyu_CmII4ptPsdHZDWZAn08MSxrcL0wvsjTQcKmD5dn9ntrfXEC0FReNqHKvw3BT7q9yn2e9Rjd6myTX0Bx2Lf367xcQzwl6aE4j_EMXraFT9TXcWZzuziNRX3OTJljYEqgwLogzO6KZeVl4S89d8-dv6WpwMOgoeglJ-4-1SlO-1VRLjmhb0cCjPGL7UB4YVEY94RVznz91KGxpYfQj9dQs6kEXaKhtvu2eJ9qpo0qb_Img-NHu2FRrCM77-pAYJbdMa2Qdy_ZtHFecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7KITfMQbsAlt-pu9HhSmCSj_OT1wXIOp2KZ4F-xt-bglnZ07RWuwyyuHdkEQvsoVCfWZfI2DDPk1ch9kVZbxNAO8b0IdYzrFsH071ek39ABmLL9UN4zEwlArwZea4YrEqkkRBtTkrfCuWKcuv57E2m89NsPxHluOsrU0lrFbYdapImpLA0Es5Pux-Moqv08wKYdvSK9HmDXyliEh_xQfyQPlcWDom_a9DlZDxc24WcY8H063wMu8yE1Yp244DJMMkgfh6X9fa1bQqUdQ0pr66HLa5ZkpDigCgDFQ7D64oXRL-BYn0POqQnP_42x-9dRjH51xjWBVd4ese6Cj3FEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=c-wyNtlBhhipqAvR0L0hYQs1IqVrOibCGx8xCXB44L0Cnn9SfXKAT_R6Pc6_Cg-_cswzY67w_U8iYMkfIPj1VZNgfWWuCe6QntM39f-yjgaXNr7qhdZuoEYZ_ktqqL_P3KIVajled1Xs4rmnNf67RgmNzwyCzoq7duu9lIcwh5qjJjKyRyKAyf6iGiPT0wMxorrA0O1BuReUq-9cfV7RUmUp4egb680Va9xG6d6qS-Rqp4aWJVGfcroqyM6WV3HZoJbgLUEzCs6PFfLPgMuAJei1S-rO_mNCmKI0_75NzD4FxneX-DCBhxk1FEzvaV6IlJxhi6RcRMJ0dHMAtYwNMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=c-wyNtlBhhipqAvR0L0hYQs1IqVrOibCGx8xCXB44L0Cnn9SfXKAT_R6Pc6_Cg-_cswzY67w_U8iYMkfIPj1VZNgfWWuCe6QntM39f-yjgaXNr7qhdZuoEYZ_ktqqL_P3KIVajled1Xs4rmnNf67RgmNzwyCzoq7duu9lIcwh5qjJjKyRyKAyf6iGiPT0wMxorrA0O1BuReUq-9cfV7RUmUp4egb680Va9xG6d6qS-Rqp4aWJVGfcroqyM6WV3HZoJbgLUEzCs6PFfLPgMuAJei1S-rO_mNCmKI0_75NzD4FxneX-DCBhxk1FEzvaV6IlJxhi6RcRMJ0dHMAtYwNMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqEcFp_nNx4G9Yor4jBJZGo-GA082gw3L6gZbzvhqHMzT1t2gW9St61vLWVZDqtk_s4MjF4h2zzNTSjiZofV7YQY2qUlBQg2wGHGFUnlqQBZoZE4WlcDbS8asLZMujsTQShADsGk6cVp6UYQIwcvXnevFJxgr_IJU1k7A2ysZrIN096LDtiXZ0dbTlxh1MMIlol0P_3PsLWlLbtJ0Fv7Z5P1xDttlyHwQBzncUaQa3WxcmETmm50meyCeCgzsGOopFre9tNz2jGT33J3o1vaQe2lw_uVWfrPb3QpwJuC6hM_TytjF-uXozcR8h4HaXSoEkOEpUbYqfzQ6ivDCBFMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NREJedhxnw5PyzfV8kXQMDiiX3osH0LDn1LOXCzvy9FX5vvyvJn8DmChVLQVDEhl5nl7zbsWUrxSOmGJVocLTmhsH4PomVoU6rN-6YYCIoeTkatr2cys9NwDjaUqyGROBamlTXp1VmDbsdv0iOoJeIOFlA36xWQYsOvL0JJ9C6484H_Mof7HAwc2A1HNowJvuf7BEnbrnN4M1ktX_VPPiAOEKWlhpFydZ9xe2hmxg9vD-4neGfsj2WmDG5OPDQcD4nb0hyl77nc0ZTvSOk4K-GqJkgIRRSt-HqDfV6uLt13FBCbZ-u5S0kRy_2PWkbcRbkhcrrDzZU16lgP0g_eozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvURl8GuyGZG88i1MNCH7FDAze8Io8CkDF76D7OSD5lyQ0IT0mNBR9iCzxUMtQA6DFjVuMc82Z08h7K0ufaTslIQxCdgua_Lh9JEB0NeFkKX-AfPBHvHPtrHf-_tpfqD8ysi8O9SX9ozMX2ny6puVCBDmyKWTCy5c4VoLtSzJboizCAcwhexUnGqPzJWwMMb7Xkog_21fFuTEwpy1Cy4g8HmrROCoGIBuYBMB16OqlixtKn30Q4d4tVUj1y8rm_F1PilXl6S7gSH_DmiIsn4d5imTBfL2uI8oEg8M0AO1xZglP1sxuW-ugB--AgVrAdpv8UPau4eGHDBRBy3pFnKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=OfvK-xJBoT7MBdLIFiL5sovadOE4pFU-XL4_UsND78wJj1BJZH446oglTRiuEqEg4MXmlUe0wz7ibfdg0lvzTzFdJqEWR8bN5naErs5PKi0t2MnqOjg_NLpqIGwNi1DJdqSHHYi-9BC5spcUnoNZZ_6bFAe7Dcob4vaddLERctdXoSEUWLIVlyvF5stcl_sGnHLxie4zicbqW_KOmoaUagS84cw9Szn0PZpFzm0v5ZHZzNYolJtsomIdLX9nBqyW83mQFuGCkSrOCfyjHlWuxhCbJ74A3IN1ZGGuN-HCBQdkNtm9-8eeEOyHA0FV9iU6cvQaSHsjq8X_MMSQ0EgoPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=OfvK-xJBoT7MBdLIFiL5sovadOE4pFU-XL4_UsND78wJj1BJZH446oglTRiuEqEg4MXmlUe0wz7ibfdg0lvzTzFdJqEWR8bN5naErs5PKi0t2MnqOjg_NLpqIGwNi1DJdqSHHYi-9BC5spcUnoNZZ_6bFAe7Dcob4vaddLERctdXoSEUWLIVlyvF5stcl_sGnHLxie4zicbqW_KOmoaUagS84cw9Szn0PZpFzm0v5ZHZzNYolJtsomIdLX9nBqyW83mQFuGCkSrOCfyjHlWuxhCbJ74A3IN1ZGGuN-HCBQdkNtm9-8eeEOyHA0FV9iU6cvQaSHsjq8X_MMSQ0EgoPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOKB9IbHgrysO7iNk1G6xtzjV7CexW5EeL4j52of0mtIA0n6ZxYyLFRiPPokxWbZQb5vGVOxLZuLVPsIOuqhJYxrum5e1WJBsUb1wJRCTIcHBU4TQh22nTr5uZ2skMqvQx4oDCRJbR-44MvtLy7FHqFwaB6qTHmHE0RSLfABmciEXa7tbFJcE3iYdG-T3G7KgqBn6rSfDyIjQHHDRPGjCs_M2TZJnEnlS1UKRMfYgiVNKElzqkzWsMM9ic2YmkP6hcyK_lK4P36wU4bbYCInPTSd9PZDciB_b78PlZI0SCBLRX9F-KxSfqIpQN7EuGMXaz72Nbg6_VYd_2Ztx_xxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_vJC1Cw8iu0jM3Ar4ix08h0wPhlP_SepW-b5sDJOTz_tq9rvvtHZn6T1SWVxtb-nJZns9OdlKzyNDb-OyGzUzUHz39jgLdfLJWunNZZuyknawdEabsL4hgujaK4fBhuhbltRtPw2dxFQ8f9lleRFNLajQWjnU65YfI9o77cEaKQzUCrvqaPd2Qtm_nZ3V54A2qBs80KAH4BXZWjNCv8Fb3pO_m1T6agPJi1D2VSx9Bc4TxWMeKBw2xctaEJhhVtiyOP4BTJgNtUOs6ui2wLP7Zm2KX0SNFolj69fLWJml7p-E4ruJ2L9yNsWQPHR2X8BZLsYGHC71QHbmTDk479ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX-2Aoqm1VDR_yuNMZ_rfWZDjsuxWdALjQBMxAGIE3g72fBX4z5nwVhUj8JQzts5bbeRN4A_jlb3cpq0NXNX-GtQ5sS2ulzNv1rW7Owu6ccMhiZ35XzZw8yKnIjtv84U3oFpH_qvT6bJgKLwjFoRWSsf-xLU-Gq_HlZmMjr4kQNqPWPTfYoJLZBUQ7p2SkKswswhXk4R1WZDeVKcFIwatSATZvJ49-munFkqyPPh0CrSDw9NS-DXspmxzAtS8AFP7IbUWXkYckmxWXugtrVGkMwAbeBNUuPDjgBiBZKB2_2MALGav0xSDZhlclVYVJKS30rjQQUjHLwN7Uw1PO1g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTijDKba_oUmkF3G8m4-iI79A9DbpZV8Ab0CqSrTluvw_oJE9A6VZ752ShI4qK3aBojv3l6mJq7AnSXXMbW8_28i148DJdVPp8oiqjO4N5s7Gda02GSqxlRwtLOqd4wAh9q-uqz00Xaq_5tD1T9IbKzCZWbSqpEpdeSgXRBWBsz3iFtYMJhEVivy7LWABY4RzuVyutHBxew50rPVOrJJ4DBX5tPPwipCdHOZU21AL7uzgV_n9v0UV2HoVem7cYYRxp16w2HaGOxYmczx629vV8Jw6d8TTf79Wf0FtjrihBms3zek2LAHjnW1aza-1x2vuYgiraxw8ic53eikavjduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScLsCjqw3je5yMbfJmREy1q3HSl3vM_DWuNgMEArOlmVKzVjQvZbYPtZQnqPgTykisS6_kdxBq4LdLTVR7VaFyZnGox9qwPh2cLZO3yU9eShW9Kucm32Lp9bp_-GWb4QFaQf3OcgCIsTOF-_KuBpBsXxmpG71esRMzDEBlGd9wthVFtGz2y0h70AcRaXbyQY2P_YnTtSihlkiWwT2KyI-5a-rY0XjKZx9EFjkvuaTZxpTdvbK7hOXRBUiFrjdainiqOHpWoWuY8dXcfz7g8CS-wZrwniOMJTyjchBgd5sWq-GNQdukX8eNVD2lYduAUA_nG0zFr8yhXnKcvziimePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOO9dvmGXHv63Yu9q_dJkLblttQ8IjFZfejaL96L53zexlKo60OsGEkLnEOOd3JBTySci-jrl4yrBc5pbzwAiAbP81_Nz4wKjqN-cc99Rhpj53ia_gl3sCKOtADkO311BdLHCMkNxweg-t90x-2q0D0HVA7QH23pTlbYaB_Z9lVCoQRukJ0idFsiUvw9v875lj6aRSIet5U9z9lcaMIJOSQem3HZ6hFrGN7uGKzpYCmVa1j-utmkBYTsRDCLfTx_EHHhTIp_r_vEU-fYkIYGGyabuC-o2GkeGRBzbFLZ9G9ug8eULLwG0udjwz4QyswfrPoh7wVt0igD8iMXRkEYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihw9THDOJDK5hQrd3zIBEQqELmVaGuNCaLpwMj26kFztVSJ_AWv-tz-DrJ8JXF2YtoCReXWamLN7sYGcCvyYNDQJe_e0YeYHvrhRxHpBl0cCTiGcmYGYPujFZaAGin0riOrO4ojpFZiw5qmZV4WVwh0eX_0Plq5i9mvVcL-IAnIpXhsbLW_s1d5m9AWZiSIT--fv4yNi39YE8Kx6_VBjQFMz6K2dWeWfnxaJIuihAb9w0riFETz23YHFyIVJbbrKLoKboUaCldVXnTFXJzMueXtwnMuJizVdnht5jdbRNoiH0Rwifk1UilXmtMKmVcnNh53mq6oFGEBI9KoQlPduSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eppmJqZvJK-Di1v-zZpa_cCb4cw62K7YzJxYKtgER2m_79YpffjuaZ5k_uyqXC4b_GHavIXLS-UbBSFmDcjN3RhJCrmb4xL-Dyki4RJFcyrERdmQ6cEblTVyRdBoLZZvMqPC7xnki0PcwEBIDGSRTc-_ffJdqwZ0_33YHYmrby3rsBDv8_PP2n9ZndRM1FpJtCcHNlNMbo77esSCRYyp0G2KA6zrrKiB3u7aOXRruOYD4koihMxLXpC9IMuOvpBsqFulaDlP8VAYXdJRguso8U-BuekiWtzmYj9q5KKrGqOHtLJUQrKf5Xrs_LlZvdpWjOOpDXfZL_ODEehWNcQAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih_z86_uNfVlA6O8zo3qiIWW25VZHnBWhwz6Vk0aSlS82Ek52hcIIkxJRPF1vAJPPKz2SGWFOhmbuenwd2nogczebL7eepNswQW3VcaXDMl3fv5Q1JwEUaVDtmvSNjtebNq1fRqj_tvlDMLFnYqm4ybUPx_hHCgySAtqFywzB_wb3bXBcBH3a7C2TAQGZ0hHDNNo1oECUa1pvKZRJqX42mcoh7w3mvgM6aYC5zzAf_n1LJGEjFZBMowUOTHhehZR8t_4F325vDocrIj-r0KAFyn0zkQ37DBmFx0vOx3gG-qIys60Xs3i4fx9l7jIm5K0Q06GswXKnNANmOihukffgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=Y1wkcxclhK_mVRixJsfMuTQSXsQSpOpNlgfL3KA2QY6x8-HjYp-CgzMriWbeRIdCoSdBTtl8ip8tC85lbRFQMAWZz4PLDjq4HpIvHKzoYsuHMtWWdo_anZeLzEHltHk8jlFhXKgczQKot4SPQxB5-2vgBIuunQbwk7M-or17E_wGuIPTwXhrG_W9q2uiIf9qm2nBmu-4MfQ9we0P_V44-rvlJ-jkG1sXiLuU6cWveBIgUSo2Cvn7Cjqb7hAdIEDJurwN4cx8H9RXcOPzQbwvRntSbR5UgSSYE7fq3y-XATQA5FKcn1arsquUN0U7kIbTgixhvcHu5F1DzRIBVBevdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=Y1wkcxclhK_mVRixJsfMuTQSXsQSpOpNlgfL3KA2QY6x8-HjYp-CgzMriWbeRIdCoSdBTtl8ip8tC85lbRFQMAWZz4PLDjq4HpIvHKzoYsuHMtWWdo_anZeLzEHltHk8jlFhXKgczQKot4SPQxB5-2vgBIuunQbwk7M-or17E_wGuIPTwXhrG_W9q2uiIf9qm2nBmu-4MfQ9we0P_V44-rvlJ-jkG1sXiLuU6cWveBIgUSo2Cvn7Cjqb7hAdIEDJurwN4cx8H9RXcOPzQbwvRntSbR5UgSSYE7fq3y-XATQA5FKcn1arsquUN0U7kIbTgixhvcHu5F1DzRIBVBevdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=YbV75O341iXWvvHn-_k7qR0SB8wdIGF82KVtyi6uIjxNlFL7yWbPITx1ZNFyl2VIh2BNJmNleHViWFm_zsmEtgw31swcgmTnXWU8pN2pmN1G-hqOPuyBRLlqYqXYsE936wyqUwzSfRWPGjvhLxyN39KsdfrYPHeBe1_1ZSlpgZT373MIRmSYgMmo3oUrDDhrVPzKKPIcV7uk0HV9mW7ZXFB3Op2zbmhpB_Qt2ASRMlerOY3KjIMUZm6_ew_jccD3rX3EGwy5NOdCgmmE2C9dxKvdxYWTUW7tka0EGDEre4Le1YMyx-3rEY9CkQozQRUCSiayh5k-ntkExI4pfkqL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=YbV75O341iXWvvHn-_k7qR0SB8wdIGF82KVtyi6uIjxNlFL7yWbPITx1ZNFyl2VIh2BNJmNleHViWFm_zsmEtgw31swcgmTnXWU8pN2pmN1G-hqOPuyBRLlqYqXYsE936wyqUwzSfRWPGjvhLxyN39KsdfrYPHeBe1_1ZSlpgZT373MIRmSYgMmo3oUrDDhrVPzKKPIcV7uk0HV9mW7ZXFB3Op2zbmhpB_Qt2ASRMlerOY3KjIMUZm6_ew_jccD3rX3EGwy5NOdCgmmE2C9dxKvdxYWTUW7tka0EGDEre4Le1YMyx-3rEY9CkQozQRUCSiayh5k-ntkExI4pfkqL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nTvLobU1OZw4_Bp5rCCowwBiU1LsCAMGIlso1AX9O16OKSONP_hU5dVoEFSg8YJUnccvqMP1JV_k8niCSwUbPkHBCmVU5W658xrKSzr0EOZgjccznGhIhKXZKoy9sGZQAP4AZumPv_j5JJB0VllHd1ZMAgXN9ylqOsw64yvFzKWwqDOfAE-JpbuZQkuwGtfhgpVmOMieFmllKgReJWf1FVqFRAq07pwR0X6471WJn8gaFZKYC0xzWsFYwOwceEDtg5HNgJuZ8FhSEf_aeaHb_MECWg6CQX16tIhS9uGCgYVD-fnlm4m6Np_ZGXDZcE_f2Y7n_oQ7nTBo4g5x0G1uAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nTvLobU1OZw4_Bp5rCCowwBiU1LsCAMGIlso1AX9O16OKSONP_hU5dVoEFSg8YJUnccvqMP1JV_k8niCSwUbPkHBCmVU5W658xrKSzr0EOZgjccznGhIhKXZKoy9sGZQAP4AZumPv_j5JJB0VllHd1ZMAgXN9ylqOsw64yvFzKWwqDOfAE-JpbuZQkuwGtfhgpVmOMieFmllKgReJWf1FVqFRAq07pwR0X6471WJn8gaFZKYC0xzWsFYwOwceEDtg5HNgJuZ8FhSEf_aeaHb_MECWg6CQX16tIhS9uGCgYVD-fnlm4m6Np_ZGXDZcE_f2Y7n_oQ7nTBo4g5x0G1uAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=HyZTuhKJkBS0gycf2DT8vi2rruCEnhf87GeM-_VclUwQME2FMQKIIfbXSG3AzeR0BqtZnLqNZ-hJHrL8XMIK92k6zGQHMHy0eZqNWGyLP6zD8reR6fy_YPUS2plR8bE105qQ9NyGeIfPSvkSwSolsbc8qWCKqnV0NAtyBiFjpc34TERmEUxNw7YS_P-zBGmiTXFYNviGvGzi03l2Mgsmq_4se_z0wpQ7LILlWIeI9eA5fY6qpNHBZ2GVb4rYGLGPwUy0DGMIvpXoeOTlrt2JOcst3tWycS0IwIGUFbVwNg05HxrAJ6yEDm3f3-TAnT1HwHDonhB0TqqsMu99qaA-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=HyZTuhKJkBS0gycf2DT8vi2rruCEnhf87GeM-_VclUwQME2FMQKIIfbXSG3AzeR0BqtZnLqNZ-hJHrL8XMIK92k6zGQHMHy0eZqNWGyLP6zD8reR6fy_YPUS2plR8bE105qQ9NyGeIfPSvkSwSolsbc8qWCKqnV0NAtyBiFjpc34TERmEUxNw7YS_P-zBGmiTXFYNviGvGzi03l2Mgsmq_4se_z0wpQ7LILlWIeI9eA5fY6qpNHBZ2GVb4rYGLGPwUy0DGMIvpXoeOTlrt2JOcst3tWycS0IwIGUFbVwNg05HxrAJ6yEDm3f3-TAnT1HwHDonhB0TqqsMu99qaA-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
