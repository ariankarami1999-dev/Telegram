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
<img src="https://cdn4.telesco.pe/file/IhvyOaqUacOi1_M3f_487NVX9KJCyfcXHPI3fho1Hw93Em7lMDlKgYpBoSxp89C0m9LPi82cTTyaxXey7gY9GrWvahBtJoy8mDUBd2yx8E4_1ZtqQ3fW8rh64eC4SOcjFgPkU1eVPZnm_EGoXMkwMgokZRTEzjxWYhIclf5QLAkuSOC00Ob5t0b73fS5lKcNYrqJBwDI8jWhR63hd0ovL2yryW8CObHqhuIS4W3M9Z_TbLzgTQr-DStuA9QXQNkGxVWhMQAKw3Rmv7Hq4kff1jm3KtelyHkGyew2pMJHeqI_yB2FXh3lC5uJqZVmKE6G2TlAuttLJKAF6cqABbrN9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 23:28:31</div>
<hr>

<div class="tg-post" id="msg-122920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Cz-qUx4lej7BOQ-S8XTrw9dfefzF4dKFfkxSDZB0oBQrofv_6rhOp1-o7WnRFUuWLueIHlwUesCRi6xntHa7dSLCDn1ArN5kelnkPkgJ1BIea_HEdQmZzsQ9o4xYIbv95fIXewmu-rfCQ2Iw8C0K7LQYuy7nAtxNlWLCDYeQVszIVVFA8K3w0Ad41SoBk6NNycodLnDYu7TbFseZFQvQLmJZta6o6c6qkIKJbw6aRYJuBk_XYM7Jw8WsdX63NLj67ws8555CLR9oJrcacIRUXR53QF8ltRyu1m-ku-po5gbRV96e5pO1bzlwc9uz4D1-5iQfHo5gzkTDWMZFG4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه آرتی: وزیر نفت هند می‌گوید پالایشگاه‌های این کشور متحمل زیان‌های روزانه می‌شوند و در صورت ادامه اختلالات مرتبط با جنگ ایران، افزایش بیشتر قیمت‌ها محتمل خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/122920" target="_blank">📅 23:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فعالیت ۱۰ فرودگاه مهم کشور (از جمله مهرآباد و امام خمینی ) و ۳ فرودگاه دیگر برای پروازهای حج، با هدف تسهیل خدمات هوانوردی شبانه‌روزی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/122919" target="_blank">📅 23:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اسکای نیوز:گفتگوهای صلح باعث «کلافگی‌ هایی» در درون کاخ سفید شده، اگرچه ممکن است توافق نزدیک باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/122918" target="_blank">📅 23:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-FttNRjsnp55qgxfVfxJ3yodozzsC5Q4pTjRfzhRZ8t4_0Owd53LTpsXTBJuY225RVGuH7Cl25MFmVfHpnX4kmJh3-JZxyEnsD1MInsCHBKhMmbUz6PdXCPs1DuPjpj4yV8OB-ec-l04i_224qM15Kv_GgsVuHVAk0jVY5AOJMjpTC8lScQW5yB-wuR1y0uk8i3ceuqmj7hkS3O7xN1OZMlyPTgs24PAI76wd5hR3QhYq9UjXKELTaqhUB2f_5HM8yRloDPqB9VsU-W1Ivqr4Mg2YCsZsuY36gAjyI1wbi4TmWHnU-RMuPqJv5_O6wvT7IausFQ_43ZpJgozQWSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر کل رهبری باقی‌مانده‌شان تمام «اسناد تسلیم» لازم را امضا کند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های فاسد و رو به زوال نیویورک تایمز، وال استریت ژورنال (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود.
🔴
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/122917" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : آزادسازی ۱۲ میلیارد دلار از شروط ابتدایی ایران در مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122916" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کلودفلر:  ترافیک اینترنت ایران به بالای ۹۰ درصد رسید. واتساپ و ویکی‌پدیا در دسترس قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122915" target="_blank">📅 22:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bd2e3ff.mp4?token=PDSi9zkQRfhgHgBZGWWU1Qooo_QpyYHU84NjHHZtSN6QYdkDXDFirTwzUiCaWJBMEmclmj5olkhmzJaJYvUN__VJvc61GjlXDBR3XiGMLIsICp0zPkLYeVi-J1a2mVet42-6_Rk_zENoNI_Ia0sQnir8QYBQRq_D7RJeXDITIoTtTSQ4VHJouTI1JuSvXiyqc00NMT74YM4jtZOx3NBlOnjzXh8xwWVYkZOMhzGGuZr0QWl_yzt8FAGj7q2K8syvmqACB7p0rzrVGWIEhhKRbtWJJbI3gnhOEVuwGfqKZva3ylAROe21mOgSxrAPcXpNBob2xb6CQx0SXFUWlcmD7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bd2e3ff.mp4?token=PDSi9zkQRfhgHgBZGWWU1Qooo_QpyYHU84NjHHZtSN6QYdkDXDFirTwzUiCaWJBMEmclmj5olkhmzJaJYvUN__VJvc61GjlXDBR3XiGMLIsICp0zPkLYeVi-J1a2mVet42-6_Rk_zENoNI_Ia0sQnir8QYBQRq_D7RJeXDITIoTtTSQ4VHJouTI1JuSvXiyqc00NMT74YM4jtZOx3NBlOnjzXh8xwWVYkZOMhzGGuZr0QWl_yzt8FAGj7q2K8syvmqACB7p0rzrVGWIEhhKRbtWJJbI3gnhOEVuwGfqKZva3ylAROe21mOgSxrAPcXpNBob2xb6CQx0SXFUWlcmD7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه : فیلمی منتشر کرده که نشان می‌دهد پدافند هوایی ایران یک پهپاد آمریکایی MQ-9 ریپر را در خلیج فارس در سپیده‌دم امروز سرنگون کرده است.
🔴
مقامات آمریکایی این سرنگونی را تکذیب کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/122914" target="_blank">📅 22:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoU78z374SnXI5RG2Ekf4QOp93ciX7_BqkT2SLKT5t7SxF2LbarsSFjfiPg3fdj74ABEAGUqkeOpR755p6VN8O1IHOblZrZuodeBIQxtFXehMrcRtuhWI3Zt7r9_ufBkGrnlSlDOFf0nXXIhkn46kIIBHiPnGZZIhg4M5E1svenXd23qolbdfFm4870vq5Xld0h4C1nSDTjCaTNZn8v-wOIBLDF7DXau0USlGmjNfCM2o9o5Ta-_UQ6HZl85JOFkzqhBsAZVoPH43MqEoYVpjfG0fG-a1m-looUs6AnMNqJzOykeV7bdDWrn9rfh703hK4T4tzDGR9exo5AleT7l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122913" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سایت
پورن هاب
به دلیل هجوم کاربران دقایقی قبل از دسترس خارج شد  [@AloTweet]</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122912" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نتانیاهو، و ترامپ در حال حاضر در تماس تلفنی هستند، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122911" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ایلان ماسک : وقتشه یه پایگاه بزرگ روی ماه ساخته بشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122910" target="_blank">📅 22:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/risSiAVuL_4Aav8SVmfKaYTeeBCaK-Fpy1z1Li48mMyhkUm1Ba0BZ7xihFiYxIHvPSB0gh_lKOUWAOnuvcNid1d4wiQWEsW25H0zQ8ZH7cc5_Q2TI3lwMt9X40pFW9ZB1IdYTbOus1yZ4Vvt6GlhVypWQEk9sPxdwycCTGL820AjE0rEpkvosxp0P61Vlx6_AYtG_CvGttBkGnzZhOqLeC-or2ailPM2R7JEmnRI4mouYrr39EnB9IwRX7A4lH2N8QlC9UxIIkrwzmsOKgPcd5gZ3V8WT7U0g6u4q0GCMNIZABhLYSTKSb6TrSZQucG6arogRyRz-WSV73OHGw9BvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نت بلاکس در صفحه خودش: خوش برگشتی
ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122909" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو، و ترامپ در حال حاضر در تماس تلفنی هستند، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122908" target="_blank">📅 22:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR5XlOHaRzXaH9vMyBkiZYt8yefryrLdIMxTr3mE5GS7aqVhjjvhbBzdyI93E_7cEOZ9GfW5TajnOnv-uR22Pt7hRfcIAa12gjkY1VEjHZ8VWcjm-erO6k548MkF5BQnwLfCoeefbrhJgpknQgTW1bdDh8ejA721OcDrFEmR4SjwvFXSiVup27fCgYOhEkb_IcyBZPRJIsp7NgrW6IXDaCagtsGEXglsXil7By6Kv46yyD51YRkwCdfa-3cWPsR9tBP_-iCxk7XyEawwer7eggAHVBBr0XSoWuWacKj7XnIZvD4KrFgZ9wU96V9MTzLKkP_a236cSJbJzL9rpq_6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار سامانه پدافند هوایی بومی «
مجید
» ایران تو اختیار نیروهای مسلح ارمنستان دیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122907" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اتاق اصناف ایران: فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/122906" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فارس: تا الان بالای ۹۰ درصد مردم اینترنتشون وصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/122905" target="_blank">📅 22:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان: کشورهای منطقه فهمیده‌اند که اگر میزبان پایگاه‌های آمریکا باشند به‌شدت صدمه می‌بینند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/122904" target="_blank">📅 22:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نیروی دریایی سپاه: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/122903" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6143492ae9.mp4?token=o-7xDHO4IJBW6vdqC6Rsf99RJFsRUCHkR7nNQwDWU_ml5UrXZBZ3xmStgTI0MRXlVkK7_DFqmdPCKLdzD3x4yXLDd9amrAYt9VWQXlhrZovkjJAUmLQyMgE20kI9ub2BADvaEhoIf2NK9QyvIosy2WeMTnBW-sAXDaRdhexUe9NfuESTOLbOWJv1WuY-3RDXnwni6unrJvdfGQZoivhIpSIjlqf9ifo8b4w6amAxJ56Q9yNHhoFSJa8GQqX9fTYaLNrTkyQBTb-o2J4oQ5hWqXLJ3eFcrZAS6PLFBAn1FUffrw1ni14udCP7YCFepJml7gME55w7JAqa3fnincoZMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6143492ae9.mp4?token=o-7xDHO4IJBW6vdqC6Rsf99RJFsRUCHkR7nNQwDWU_ml5UrXZBZ3xmStgTI0MRXlVkK7_DFqmdPCKLdzD3x4yXLDd9amrAYt9VWQXlhrZovkjJAUmLQyMgE20kI9ub2BADvaEhoIf2NK9QyvIosy2WeMTnBW-sAXDaRdhexUe9NfuESTOLbOWJv1WuY-3RDXnwni6unrJvdfGQZoivhIpSIjlqf9ifo8b4w6amAxJ56Q9yNHhoFSJa8GQqX9fTYaLNrTkyQBTb-o2J4oQ5hWqXLJ3eFcrZAS6PLFBAn1FUffrw1ni14udCP7YCFepJml7gME55w7JAqa3fnincoZMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: همه باید به تقلب اهمیت بدهند. همه باید به ریشه‌کن کردن تقلب اهمیت بدهند. همه باید به صرفه‌جویی در پول مالیات‌دهندگان آمریکایی اهمیت بدهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/122902" target="_blank">📅 21:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بیانیه مشترک نتانیاهو و کاتز: ارتش ،محمد عوده، فرمانده جدید القسام را در غزه هدف قرار داد و ترور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/122901" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سپاه: طی شبانه روز گذشته ۲۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/122900" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvHtGaWHL6WeFdrYMf2976GZ1yIERr-ZSPr9MRK31gOeNACaXS136cxBYNwrHZcZq-90S58sgaRPgm1ooagzNL5oUz9eat3A4SH-POtMNyS-N33WQ_FzZiq9xL0zXOukazgMFmKmCtIa4gcEgdbCOU52n0UmVBb7Roil0-0bCbdhgCdJB_qoC7QdsVG6_FBd41UxtGaTkQ2FIeiq70lQhTOOr2NG-bIn36kkCLrjqrlra8P8ESKzfKa9GRO__rbCMprOGjg63uDDytNi_P0hOjkPatRo049SRFQHp3D7eYbx3RE40fDVtwFvD_zzhKnIU2n1T3EDm6PW5sOv7wAnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXqL_1E-sVHbvuo8_v0nXX0pfVN5nm1d5hCxN-EOC1MCCNMtnQb6_wnCFU7CE6XlZB4wpdhkemQGb5FTdX0UXQ0Lhv7vp9djwXBDh9s6xr3OEnTdwvBmjI_8-T0BZyXQ9TUSH2xEqfNysNGsP6ZDNnkkn3B7MJ3ctGFF5hOKZOxc5vw-tqrvszR8M2lQgVdDlJx84LTB1zmrzdA_HGufgBtYh6jwC5nV740P3lrUvEEjfbsUtIU_1hjxPhUG2uxWGrnxYbjECpQxZVPFfbhNtEWnwzNBbAGkEwmoa9o_ocCYNp3ZLkIeWiE5Esb5g8OFHL0422CyPtL-QRv0SH_QuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97b34ffba.mp4?token=bYkUZcz4JwQGVu8MkVouLbk9hfXubRGVeFYzgzYl51s45RmlaTZn1Iz0orlrt8N4Nv9wwmkPHFqal4bcKdNcWJT4trAkVf1p9_kPy_FQOcbS99KEZC0UlM01VhXKvRModdxY1uo-aOddZ81VbtanI0LwtPkMr35uQb1vnklE1K3KmGtQvpSSkqsmeMMkNS4tJAfveXnMIg9zZH2W6Vc5SF7MmcBj-Y1WMVHctgSX52cLnc3iBkgHtGiguCb5EiaYO25q3n-BTl_HZ8U1jS44G0Dki-u3zL6O2Inlglb1kE7Ju0qDcJfpf1Njo_scQDKXpe776wXlEv5Vu9YuO4uo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97b34ffba.mp4?token=bYkUZcz4JwQGVu8MkVouLbk9hfXubRGVeFYzgzYl51s45RmlaTZn1Iz0orlrt8N4Nv9wwmkPHFqal4bcKdNcWJT4trAkVf1p9_kPy_FQOcbS99KEZC0UlM01VhXKvRModdxY1uo-aOddZ81VbtanI0LwtPkMr35uQb1vnklE1K3KmGtQvpSSkqsmeMMkNS4tJAfveXnMIg9zZH2W6Vc5SF7MmcBj-Y1WMVHctgSX52cLnc3iBkgHtGiguCb5EiaYO25q3n-BTl_HZ8U1jS44G0Dki-u3zL6O2Inlglb1kE7Ju0qDcJfpf1Njo_scQDKXpe776wXlEv5Vu9YuO4uo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل حمله‌ای ترور را علیه فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل شهر غزه انجام داده است.
🔴
در حال حاضر مشخص نیست که این حمله موفقیت‌آمیز بوده یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122896" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWRMvOXbJukVBVMoASxVhHdkA5OO-NzJqWrJrcQ_H2orm0YOdGcrORlFmNS-8niyXJEzXFyPXThnPPrXkrYXlIlxqloz9j9TuVK0RtfCUboTjUeNN8gk-PRy7YpFwHk46yRYUtrTFTUbruuJaEX2uEYnl2vYBDZzQUmkqMVeVAiMBv3UluezNHkGRj7oc-yxCSZnFIDSJW5hwDf9Sksrs_fZxrqbaCxrSSREIM8Nvs9d9eqIVDBEW3JM2N9hpy3Pl-DNvvDm0eWmyXMyOawRVoUvmNjF4LEt8DwWC67sqEIFgb3zdpg9q8u2NzFJWl32Lkjbpo4ey9_dfcsESw3DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاآرتص:توافق ترامپ با ایران؛ رؤیایی که نتانیاهو در ۲۰۱۸ داشت، حالا به کابوس جهان در ۲۰۲۶ تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122895" target="_blank">📅 21:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دولت ترامپ در حال پیشبرد طرحی است که بر اساس آن، پلوتونیوم درجه تسلیحاتی دوران جنگ سرد از کلاهک‌های هسته‌ای منهدم شده را به شرکت‌های خصوصی که قصد تبدیل آن به سوخت برای راکتورهای هسته‌ای را دارند، ارائه دهد، گزارش نیویورک تایمز.
🔴
اگر نهایی شود، این نخستین بار خواهد بود که وزارت انرژی پلوتونیوم مازاد تسلیحاتی را در اختیار شرکت‌های خصوصی قرار می‌دهد. این وزارتخانه در حال حاضر بیش از ۵۰ تن پلوتونیوم اضافی دارد که قبلاً برای رقیق‌سازی و دفن برنامه‌ریزی شده بود.
🔴
حامیان این طرح، از جمله اوکلو و نیوکلیو، استدلال می‌کنند که تبدیل این ماده به سوخت راکتور، راه‌حلی کوتاه‌مدت برای کمبود سوخت فراهم می‌کند، در حالی که ایالات متحده به دنبال گسترش ظرفیت انرژی هسته‌ای است.
🔴
این پیشنهاد نگرانی‌هایی را در میان کارشناسان عدم اشاعه ایجاد کرده و جزئیات مربوط به امنیت، انتقال و ترتیبات دست‌کاری هنوز در حال مذاکره است.
🔴
شرکت‌هایی که برای مذاکرات پیشرفته تحت برنامه استفاده از پلوتونیوم مازاد انتخاب شده‌اند شامل اوکلو، استاندارد نوکلیر، اگزودیس انرژی، شاین تکنولوژیز و فلیب انرژی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122894" target="_blank">📅 21:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: در گفت‌وگو با رهبران ۸ کشور مسلمان اظهار امیدواری کردم که خداوند قلوب ما مسلمانان را به‌هم نزدیک‌تر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122893" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اتحادیه اروپا و کشورهای آلمان، نروژ و هلند روز سه‌شنبه پس از تشدید حملات روسیه به اوکراین، سفرای روس را احضار کردند.
🔴
به گزارش رویترز، سفارت روسیه در آلمان اعتراض اتحادیه اروپا به این وضعیت را رد کرد و گفت که مسکو در حال انجام «حملات دقیق» به اهداف نظامی در اوکراین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122892" target="_blank">📅 21:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نیویورک تایمز: ایران با چندین پهپاد انتحاری به چند ناو آمریکایی که از سمت دریای عمان، قصد ورود به تتگه هرمز را داشتند حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/122891" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1ZBF-8BM069CtELh47je4mngO0xEDMRVEFTVQYpxCdCvBI0n-VELtQ0U7HkdFzyy99h1eIwoYrmcJeVH0zxn-dqKbkoXHaaS2-vB-_iDJ2qwqV0ZN1YpjhkklbHFUl1wLYBUorTSyNGkqcGKUzk8l7IQmhaPTetdkRLKI2cQ-0aa7e3sQmgaqzl4hvMpRq-MDn0JI-Yljn-TkVFHpVPwguzgjKZgdVCKEmCcSomj5LZfkBT11JV_GAhbuKprTo8MnFyn6hd8ZS9qW7WvWTkuRwunb4ddN6I26jATCERFZZEcoS11FXwSp7NuqGQIkgZckIp6EDBleytkXNhtp-qYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122890" target="_blank">📅 21:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
یه مقام اسرائیلی به شبکه ۱۴ اسرائیل :
آمریکا فعلاً جلوی ترورهای هدفمند تو بیروت رو نگرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122889" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">طبق رصد اطلاعاتی واحدهای SIGINT و CYBINT جمهوری اسلامی ایران، حجم عظیمی از ترافیک داده از سمت ایران به سوی سرزمین‌های اشغالی رصد شده.
ظاهرا نیروهای داخلی موساد پس از وصل شدن اینترنت به سرعت درحال آپلود اطلاعات جمع‌آوری شده خود برای موساد هستند؛ طبق این گزارش، افسران موساد تا این لحظه به دلیل قطع بودن اینترنت توان چنین کاری را نداشته و ۲۰۰ هزار نیز پول ته جیبشان نبوده کانفیگ بخرند و امنیت ملی را تهدید کنند.
از این تریبون خواهان قطع شدن مجدد نت و برقراری امنیت ملی هستیم تا یوقت نکند دشمن روی ما اشراف پیدا کند...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122888" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqP__aEnA9hVCRSIftW0cyMd6hAckaMD3kLepkBnNn3BqH-1KcYd8a8fRIQoDR5ypAPmzgeIe1xGPU-1zQcFbzTZBqYlsZT9AtRPbIyAgYwQojHY_rHo3xFIugekd9Dwed42By8qqvtU_sG6J7XZPZsPNlaqg5a4UTi1-tZKcWk-q7MwGOHZJ8lVB1sut4s9nu7pebiCtoH6LhD5QAg_OsDrWz8XnVsnm8eW1K8I5DWHbqxv-H3oUH6TOL26sCVYuul5pqM0GH0LH5rdJUinJR3gmOG6r131szi17_nPcr5XY7q5wDMz0jrBDD0n_elyBERhnRgjpcbDWYbK5wpa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما شروع کرده به صورت رگباری داره گزارش میده که اینترنت نباید وصل می‌شده و اشتباهه
🔴
حتی به عارف که گفته بود به‌خاطر یه راننده نباید اتوبان رو بست تیکه انداخت و گفت اتوبان قبلش باید ساماندهی بشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122887" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی در گفتگو با کانال ۱۴: حمله به ایران پس از دریافت «پیام مشخصی» از ایالات متحده، در این مرحله از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122886" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
صدا و سیما شروع کرده به صورت رگباری داره گزارش میده که اینترنت نباید وصل می‌شده و اشتباهه
🔴
حتی به عارف که گفته بود به‌خاطر یه راننده نباید اتوبان رو بست تیکه انداخت و گفت اتوبان قبلش باید ساماندهی بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/122885" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل دستورهای جدید تخلیه اجباری برای چندین شهر در سراسر جنوب لبنان صادر کرده‌اند:
🔴
— خیرابت سلم
🔴
— بیر السناسیل، قابریخا
🔴
— مجدل سلم
🔴
— قالاویه
🔴
— کفر دونین
🔴
— تولین
🔴
— ساوانا
🔴
— صلعا (صور)
🔴
— برج قالاویه
🔴
— جبیشیت
🔴
— القصیبہ (نبطیه)
🔴
— فرون
🔴
— ابیا
🔴
— دیر کیفه
🔴
— کفر سعیر
🔴
— صریفا
🔴
— الغندوریه
🔴
— النفخیه
🔴
— ققیات الجسر
🔴
— عدشیت الشقیف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/122884" target="_blank">📅 20:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH6sm4C2ciDLxid-CVYiRZ6u4jkL4YlcLE1QJHfc2QhgLORvPKJyFMVIFXfN7TjebF8SIt-Z6bqlTk1BiGQxgeL01T8SYAdhxZs0JYOi2XAoK_qILYUsrClNtCIL3I1Ngcq56ZgzVJqlPZdeVtqo2sPjMO6tQhxCqAdRJd2bhtxWIzbM9fuo69A_29dIBYFp4Xe8o2RaKb3aPiTJGvnfGpHgAuFJFNWZDr1LDVCItWtYZDPUUuPBqcUUUoKHGKl_fXbpQljVwYcn462FxjgZVx2xI_a7bLY5wisezKQ9XO6vV_t-ntoyqzmvra1wRWlgrrdhGRyANCcH_d30TB5hUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا وقتی می‌نويسن خوشحالیم که همتون وصل شدین
❤️
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122883" target="_blank">📅 20:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ادعای عبدالخالق عبدالله مشاور سابق بن زاید و از چهره‌های بانفوذ امارات: امارات گام‌هایی محتاطانه و حساب‌شده را برای کاهش تنش با ایران برداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122882" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122880">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QD-bwU8qvlYEv9mwA9CA4pBYJikj6bzLLW1q8varqcKXxFk_r4WRPHf4bjKA0nTC9CIU27BCxKgJdLTuenuV4SjQvf0p1PTH1mxlkcVLwDxKwUQ1NHTENw0s44aWemLj7tLnRrVO6khFaBqUuovDVoCamZrYj0wfKqOnZiEX1vwgaS3TVSd581__ZePu_w5ht1dAgj9bzF5T2JubY8_GnGg-RdoiV-tmFthCfqvMo7NwoRax64xT5fjPb1Vx1rUPueyRL0UxxMVegkK_uWCsC1XyEJ8SJT77jZQqqaCc-n0nq8Z2EK6Yflxz3RtHGCQT4YnKGJXrO6SEuX7eNCO5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ViJvvab1nYl9X2z4405-pKRDOiF07_pCVlbqW0K1aCVS_VD0S0DJBWOCkF4qcesTULhSaWgfY8-pHm2j3En4vmqMBmHt-BYxROIuLCCAd8AtXSZNujgH6y8d_prKkQDXbM769jPOL1Seuvw8zhAV-o2ib3TPUGvKuIAh75DkQMgdN9egjL5QesTjpobrn1QZFT43ynszbILX-B7WEWsqcP3DdaqqnIpwzhOjgb8PCDsT0nye6exIPxhv4Z8KdhpdeI4OgP7e6dEcO6dmkuip1xVyjxT8M44h8COxumUNSJQX0rTayRJjyQqJYtk01M2Fj0oYM3STwCvHFHsSGjt9_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعتی پیش بورس آمریکا و بازار کریپتو به صورت غیرطبیعی با ریزش شدیدی رو به رو شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122880" target="_blank">📅 20:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122879">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۴ عبری: برآوردهایی در اسرائیل وجود دارد که توافق با ایران تقریباً به طور حتم لبنان را نیز در بر خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122879" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122878">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا به اسرائیل نسبت به حمله به هر شکل به بیروت هشدار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122878" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خوش آمد میگم به رفقایی که تازه وصل شدن</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122877" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/122876" target="_blank">📅 20:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/122875" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122874">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دفتر امیری قطر: امیر قطر در تماس با رئیس‌جمهور ایران درباره تلاش‌ها برای کاهش تنش و حفظ امنیت منطقه گفت‌وگو کرد
🔴
امیر قطر بر لزوم دور نگه داشتن منطقه از پیامدهای تنش و اهمیت راهکارهای مسالمت‌آمیز تأکید کرد.
🔴
امیر قطر بر موضع ثابت خود مبنی بر اولویت دادن به راهکارهای سیاسی و دیپلماتیک تأکید نمود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/122874" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
معاون وزیر ارتباطات: سيستم عامل، مرورگر، آنتی‌ویروس، اپلیکیشن‌های بانکی و ابزارهای امنیتی خود را بروزرسانی کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122873" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به الحدث گفت:
ایران در طول دوره مذاکرات خواستار آزادسازی دارایی‌های مسدود شده خود که حدود ۲۴ میلیارد دلار تخمین زده می‌شود، شد.
🔴
ایران اصرار داشت که نیمی دیگر از دارایی‌های مسدود شده خود را ظرف ۶۰ روز دریافت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122872" target="_blank">📅 20:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما عملیات خود را در لبنان تشدید می‌کنیم. نیروهای دفاعی اسرائیل با نیروهای زمینی قابل توجهی فعالیت می‌کنند و موقعیت‌های استراتژیک را تأمین می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122871" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKJVh1zd24r3NhF9Nhyuw6Vd-JRaK5BN_F5EdzSHne2UbWJOTOKClbvtOt_nKHp-ZVpI8cE4xXIPN4c64JFCyYynmKl_qo37hl1w_qUay3sxl1GsrtLpgNsPLqCxwhP5Ev7yXMvHi5SjIdIkHPX9d8OJQdiU6cpkIp1e0B9wbA1yN6_o4u24qTgPsQ1Ao-E_y4_Mq4zCEAKiJ_mRlFmyvNBEKpPCXbaAESLPoRhfYo5OyERKRihGPrg4cZqc2EviQRwY88RycnG-m_k8UwFWGnpYfIWHeti5VxL9A3JB9BonYF0XK2KMyiZ67hdyJTglVJOPxuv3b9ayr69xhoD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
تازه معاینه ۶ ماهه‌ام را در مرکز پزشکی نظامی والتر رید تمام کردم. همه چیز کاملاً عالی بود.
🔴
از پزشکان و کارکنان عالی تشکر می‌کنم! به سمت کاخ سفید برمی‌گردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122870" target="_blank">📅 20:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKSJaUBTPxg2kc-MuodO3QEie6Whs7fy1S9lQdJ8qIAqJ0DCIfUSkltVeIcX4Dt5gdsbCwFoZ1rdsiMBXVNkTP75ZJRCx1PTFG3A7VAzC44mvC5XW7mG_2-u2rbRW9rct-w8svRPLMD_F9hd8BzwNLC_eJ8N9SzYP1aJ55bFbD5rNki4Jsx7tuEF78QmNTsjjE-Rhp4tG2axwGDnEo3gOqlWaOlHCSNXtZcLgS193GxW78TLgexeVMzD4MKaqH1Jdw6qZk6V1n7ZKlMGT6OOmKYjdxOrbs48cAvIuSHT9Fmr3EywZkraoaQY8ubhpZwJxQOcUPwNjKSmekExBRbrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : پروژه «آزادی» از سر گرفته نشده و نیروهای آمریکا فعلاً هیچ کشتی تجاری‌ای رو از تنگه هرمز اسکورت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122869" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الجزیره به نقل از یک مقام آمریکایی:
گزارش‌ها درباره ازسرگیری اسکورت کشتی‌های تجاری در تنگه هرمز توسط نیروهای آمریکایی دقیق نیست
🔴
نیروهای آمریکایی در حال حاضر با محموله‌های دریایی تجاری در تنگه هرمز همراهی نمی‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122868" target="_blank">📅 20:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122867" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
واکنش سخنگوی دولت به اتصال اینترنت بین‌الملل
🔴
تفاوت نگاه‌ها، در بزنگاه تصمیم‌ها روشن‌تر از همیشه دیده می‌شود.
🔴
با دستور رئیس‌جمهور محترم، روند بازگشایی و تسهیل دسترسی به اینترنت آغاز شد؛ اقدامی در جهت پاسخ به مطالبات مردم، حمایت از کسب‌وکارهای دیجیتال و توسعه خدمات هوشمند؛ مسیری که دولت چهاردهم از ابتدا بر آن تأکید داشته و دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122866" target="_blank">📅 19:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رابرت اف کندی، وزیر بهداشت آمریکا، ویدیویی تو اینستاگرام منتشر کرده که توش با دست خالی دو
مار سیاه
رو می‌گیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122865" target="_blank">📅 19:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحشت در فرودگاه بین‌المللی کمپگودا؛ خروج اضطراری مسافران هواپیما
🔴
پس از آنکه مشاهده دود در هواپیمای ایندیگو در هند، وحشت برای مدتی کوتاه فرودگاه بین‌المللی کمپگودا در بنگلور را فرا گرفت.
🔴
مسافران هواپیمای شرکت ایندیگو بلافاصله به صورت اضطراری از هواپیما خارج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122864" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / سی بی اس: دولت قطر گزارش ارائه میلیاردها دلار به ایران برای تثبیت توافق صلح را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122863" target="_blank">📅 19:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVwoMwef1H-JqMxoiw_-8POap7h99koIHqKMk_OBUy6KyKb_VlfLBEHPWmhYXq_kw6psnkyokNA96L_LH5e9VWRECwOtMRyKFoRFhs7gQFgmW-8q9xPwSUoHC5PIc1YnWyGUTfR5cUHAkFZQWS_FUiEsXfM9g_z1_A9kGIheiSE5OPxd7f1kB9Jt627VfkqD6SqyCIcBtrEs5PCGVf-VpTQUJF8OlO8b-uoU5KqoqzUN_scbNHj4oSjDaCi9zOmCyKU1LV-kNCQySPkPtWhyTDCas2iYVCrwNvn7CgQFjWP0pXkjaxsJAurR1M8GXkBYoofQ7P2DSDEaN7iYWVBuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFzsTJx9tskL7-Mu0NhpaXOJ0dwBqApstHNopckK02NKNyMfl2noS-rtbeVEwYS_tWyeXXFb4c1VDE60-iInY7vUqNEZAsSeZ4tlED2FQV9q6sm5vYitv-WLbcs3E1Zf833eWQnA_WJvs2KJIHA_AtXl5O_dpj9GPYsh4aZgr7QNgu-KJ85qwEnR7Ul74tG3oFKDMFpwZyzTL7gCeYstkYBm6qcTAB0CZC01q2mtjbF33myCfbqxHP5nXzeeqSlPNuiw16au-NSflKx6ToEk54BNju35CmpY-o51-C60e5R_BDjyOdb_JtLKjHxQM9C_JcAxlOTGd812LaWrjoSmYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی شهرهای سُهمور و مچغره در دره بقاع شرقی لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122861" target="_blank">📅 19:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122860">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سنتکام : تا به امروز، مسیر ۱۰۸ کشتی تجاری رو تغییر دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122860" target="_blank">📅 19:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3f034504.mp4?token=pLjvgNl-XR7i6myaWzQznOOZzBGp6IVwxQ6Zj3FmCnNdrgmQqCzcYkUpeIO0dLGLbMn3vb2CZI15bwwp7KyfwBhsml_bllemZLdMo5YpV4vIsaZxzMIxuKd3kkBTJhKFJ4SsBalOhwpR3F-SynHOpwDVeydttBeDdrFUwUBW30zdqBS2EKF-w7lvbSEFVB19iXXhbDi1xKzyAhsXUMz56hUMnxUVMncMBS5DOhAjRVzeM12qYKuKAhDqUh7TTlSA0CGhSEadxsEhdYwS_GBHQulHpc6K5d2Vjos8I-bZqiKelPvoM1W-ef_nnnVzL6_-rf9UCCUjOrF7CUixnmJ2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3f034504.mp4?token=pLjvgNl-XR7i6myaWzQznOOZzBGp6IVwxQ6Zj3FmCnNdrgmQqCzcYkUpeIO0dLGLbMn3vb2CZI15bwwp7KyfwBhsml_bllemZLdMo5YpV4vIsaZxzMIxuKd3kkBTJhKFJ4SsBalOhwpR3F-SynHOpwDVeydttBeDdrFUwUBW30zdqBS2EKF-w7lvbSEFVB19iXXhbDi1xKzyAhsXUMz56hUMnxUVMncMBS5DOhAjRVzeM12qYKuKAhDqUh7TTlSA0CGhSEadxsEhdYwS_GBHQulHpc6K5d2Vjos8I-bZqiKelPvoM1W-ef_nnnVzL6_-rf9UCCUjOrF7CUixnmJ2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزیمت ترامپ از کاخ سفید به بیمارستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122859" target="_blank">📅 19:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شبکه آمریکایی سی ان در گزارشی نوشت، ذخایر اورانیوم و غنی‌سازی ایران، دارایی‌های مسدود شده و جنگ در لبنان موضوعات اصلی هستند که هرگونه توافق یا عدم توافق میان تهران و واشنگتن را شکل می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122858" target="_blank">📅 19:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با رئیس‌جمهور مصر: رویکرد ما همگرایی با کشورهای منطقه است / اقدامات ایران در چارچوب دفاع مشروع بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122857" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با امیر قطر: ایران برای دستیابی به «چارچوب عزتمندانه» پایان جنگ و تنش در منطقه آمادگی دارد / شیخ تمیم: قطر از هیچ تلاشی برای صلح و ثبات فروگذار نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122856" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
منابع عبری: در ساعات اخیر نتانیاهو مشاوره‌ای امنیتی در مورد وضعیت در جبهه های لبنان و ایران با رئیس ستاد ارتش اسرائیل، وزیر دفاع و دیگر سران نظامی ارتش اسرائیل برگزار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/122855" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای شبکه عبری کان: دیوید زینی رئیس شین‌بت (سازمان امنیت داخلی اسرائیل)، به تازگی از امارات متحده عربی بازدید کرده و با محمد دحلان یکی از مقامات سابق ارشد فتح و تشکیلات خودگردان فلسطین و مشاور امارات دیدار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122854" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت قطع ارتباطات: اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود / بازگشایی کامل به وضعیت پیش از دی‌۱۴۰۴ تا فردا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/122853" target="_blank">📅 18:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک مقام آمریکایی به اورشلیم پست: نیروهای آمریکایی در حال حاضر کشتی‌های تجاری را از طریق تنگه هرمز اسکورت نمی‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122852" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کلش ریپورت: نیروهای دفاعی اسرائیل حمله زمینی فراتر از منطقه بافر «خط زرد» که خودشان اعلام کرده‌اند را در جنوب لبنان آغاز کرده‌اند
🔴
این پیشروی به سمت سایت‌های پرتاب پهپاد فیبر نوری حزب‌الله است که در حال کشتن و زخمی کردن سربازان اسرائیلی در داخل این منطقه بوده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122851" target="_blank">📅 18:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122850">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122850" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122849">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔴
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122849" target="_blank">📅 18:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نت بلاکس: سطح اینترنت به ۳۵ درصد رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122848" target="_blank">📅 18:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150e37cfe6.mp4?token=p4KwQQ_-YETEnMbjQefpOcUcBPyzLpCLtslugP9ptjPgj0951JSos-kBjCpGzW5OZOgMXIsVJ4pn4wPlZ7f-AGg9mHrIuTQsd9PGUbIzztzvSX0g1tZ-TqEgmf0WKDXV4dXKhri8GmDNBWii2qbwM1lT_6nJLcLn__W9ykThay1ERD3-O_ynPepu212VLknsV9qDxaqbpxlCK38vGQ6A1-aO6u-fYXaUb7_hDBlNyNS_9NkntbKMd4JR4oX-tw0WIH4Zkgtfkyh2ob8Tea0sglHQmsVv8llmZnel3h37A5i0rWzI276ex1EIbmEYOAasusqukZL76KuP83Oi5t7r_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150e37cfe6.mp4?token=p4KwQQ_-YETEnMbjQefpOcUcBPyzLpCLtslugP9ptjPgj0951JSos-kBjCpGzW5OZOgMXIsVJ4pn4wPlZ7f-AGg9mHrIuTQsd9PGUbIzztzvSX0g1tZ-TqEgmf0WKDXV4dXKhri8GmDNBWii2qbwM1lT_6nJLcLn__W9ykThay1ERD3-O_ynPepu212VLknsV9qDxaqbpxlCK38vGQ6A1-aO6u-fYXaUb7_hDBlNyNS_9NkntbKMd4JR4oX-tw0WIH4Zkgtfkyh2ob8Tea0sglHQmsVv8llmZnel3h37A5i0rWzI276ex1EIbmEYOAasusqukZL76KuP83Oi5t7r_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله های شدید ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122847" target="_blank">📅 18:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHc9GNfJEgo5LX6o37SYCSsRsXu_bXgAcPbgHst6hxDqVuLLOCu7v8LVGd46AXLgU0HXbo5j0qpTzhGK-GHBGuaZCDBfjWnw4lW6SiD26zGsfeDycASiOrZeWBW_X0iT1NALgd0Ib_an_FT9GMjOulfkKDIyrBq7mqu18yzUI41EX5FK9qoGLueCqBtIZmnB1mToMbSE9CM_4LI3wd1EO20-lCzX3xLghMLAyUWtQLnt0eNk1e2bcUHeWt25wjP1HF2mBXPl7t4MBlYHFBSHsDpfY031V7GEJp1DhnjB_rDlNrEXDvXcuBwWR5La6Gv6ws6QaqSOjcdRgy660I9gVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هلیکوپتر آپاچی AH-64E ارتش ایالات متحده در ۱۸ مه در یک شالیزار نزدیک پیونگ‌تک، کره جنوبی فرود احتیاطی انجام داد.
🔴
هواپیما پس از اینکه خدمه در حین پرواز مشکلی احتمالی در موتور تشخیص داد، فرود آمد. هر دو خلبان سالم بودند و هلیکوپتر آسیبی ندید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122846" target="_blank">📅 18:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122845">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: طولانی شدن درگیری در خاورمیانه به نفع هیچ‌کس نیست
🔴
جهان نظاره‌گر پایان بحران در خاورمیانه است و ما باید موفق شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122845" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122844" target="_blank">📅 18:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مارکو روبیو وزیرخارجه ترامپ ادعا کرد ممکن است چند روز طول بکشد تا جزئیات توافق احتمالی با ایران نهایی شود و افزود که مذاکرات به پیش‌نویس اولیه نزدیک است
🔴
او گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، اخیراً تماس‌های منطقه‌ای برای پایان دادن به درگیری برقرار کرده است، اما تأکید کرد که آمریکا فقط "توافق خوب" را می‌پذیرد، وگرنه هیچ توافقی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122843" target="_blank">📅 18:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qekf4m8pFfPf6XOd7HKaLyzu6EqwCzEBR5glcIu7rga2y6GSUeaiAYlU_YHmpA5y5LwIXDeq1RO2kyz1HX6BBJDhUz6qcheJhR65LaZTIeeg_U7j7Zudxxltd58--ronwCc8cwo_cebjj6Va7rnMNVYNbK03o6KTnhjMetQUCmuWzkafPedvLlR_gMvLV8z20HRkNukGZbcbmmMsYvsp-2DJABwnKyPUQr4zBtuZHiBpopIfMm-drCe7BhfFibc-S5ImuHeF5wKPF7C7OOPfObm-AG_GHtMX5rK261_fad3lUXC0riHsMD0cJAJ66KTtxAmfeFA3qsY-Ra1vgFAUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس شورای امنیت روسیه، دیمیتری مدودف: اتحادیه اروپا اعلام کرده است که حضور دیپلماتیک خود در کیف را بدون تغییر حفظ خواهد کرد، علیرغم هشدارهای روسیه.
🔴
خب، ظاهراً آنها دیپلمات‌های اضافی دارند و نیاز به کاهش تعداد دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122842" target="_blank">📅 18:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-eOBOgB7XMFJVU1M4TQD8FdfN1FCHeyJslsJH3rkuTA3JvgAM6dJ8vyde1ctRLV1a6wEGe63PtPKg612GLEpaujtNxdyHh5IksejWrRdooDFsnbYfhYQkTs6LlauIMQ1qvW47UL4TnocOtvZ5NmLIRWKPOcvnZx679Y0GGFL56x7OYkigdA5aX_wH-yn2Us4SxfcZWyCQ2DbDIy6JsTFUPNaFqE-pTSL0jIHm07mQvLWCgNbZg7URUjysUjZM7tZCP6WAjQmcaKdmX_cddjykNg2GHipdCuXONK5wKyMT5yIQN0WVTwBn5v6RBhQ6K5-r0Q3PMdMYqBkyyDFY0SaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به دنبال اختلال در مذاکرات، بار دیگر صعودی شد و از ۱۰۰ دلار گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122841" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه، اردوغان، با رئیس‌جمهور ایران، مسعود پزشکیان، در مورد روابط دوجانبه و مسائل در حال توسعه منطقه‌ای تماس تلفنی برقرار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122840" target="_blank">📅 18:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل عمان، توسط نیروی دریایی آمریکا هدایت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122839" target="_blank">📅 18:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
طبق گزارش نیویورک پست، انتظار می‌رود دونالد ترامپ فردا برای یک جلسه نادر کابینه به کمپ دیوید سفر کند، زیرا مذاکرات با ایران به مرحله‌ای حساس نزدیک شده است
🔴
انتظار می‌رود تمام اعضای کابینه، از جمله تولسی گابارد، مدیر خروجی اطلاعات ملی، در این جلسه در محل استراحت ریاست‌جمهوری حضور داشته باشند، هرچند ممکن است به دلیل شرایط جوی شدید در منطقه واشنگتن، مکان جلسه تغییر کند.
🔴
انتظار می‌رود بحث‌ها بر روی ایران، دستاوردهای اخیر دولت در زمینه اقتصاد، کسب‌وکارهای کوچک، تلاش‌های ضد تقلب و تحولات سیاست خارجی متمرکز باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122838" target="_blank">📅 18:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e4bed3b5.mp4?token=dKPRpkwF8lMlUA1TvxtlocAAJUzA4EbLImcXKs4Yqj4hh9kIbzjfNl6fZk98mQ41Rr0Ac4bVCjpFDSizpf_le1Oii46vDYDh2knIywKIigiTsV2plDKNSXxcDauV94XAbRd3UagdCebUpvXiIych6vheSoxKshyCmjW_vITJQYv1iXp3FtwkzjQByTs61dkeYtNa40OH5F0Ju6Jl8EpSYdfNI1NLxnxu2UDnw53v4m2HZ9NsQ9nBk8mf_RzM6pLg0_4Yd_NVi4z04Zrb4InGxdTOJzzNiFkWe-bUCmAHgkoAeIRbuJ5xfP8FwhgzUESMcTvjgJCQAw5r9LhcIJdK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e4bed3b5.mp4?token=dKPRpkwF8lMlUA1TvxtlocAAJUzA4EbLImcXKs4Yqj4hh9kIbzjfNl6fZk98mQ41Rr0Ac4bVCjpFDSizpf_le1Oii46vDYDh2knIywKIigiTsV2plDKNSXxcDauV94XAbRd3UagdCebUpvXiIych6vheSoxKshyCmjW_vITJQYv1iXp3FtwkzjQByTs61dkeYtNa40OH5F0Ju6Jl8EpSYdfNI1NLxnxu2UDnw53v4m2HZ9NsQ9nBk8mf_RzM6pLg0_4Yd_NVi4z04Zrb4InGxdTOJzzNiFkWe-bUCmAHgkoAeIRbuJ5xfP8FwhgzUESMcTvjgJCQAw5r9LhcIJdK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حمله‌ای هوایی به سد قراون در دره بقاع جنوبی لبنان انجام دادند.
🔴
سد قراون بزرگترین سد این کشور است و به عنوان منبع اصلی تولید برق آبی، آبیاری و آب آشامیدنی عمل می‌کند و ظرفیت تولید برق آن حدود ۱۹۰ مگاوات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122837" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69262d7ad7.mp4?token=k3Matu0-v4LPU8yTRSSW7W0hei4k7dVSL9KvE0gNnyGP5-9NC_dnjCUmtLctu0K3SRySwqd_zbL3dGv1i2uneOG6UCgU7WmyhE9AgAYvsfq_6LGP2mLORg7rJdGB7roIteU8ahA7yqGo-cFR_xuyJu6oUEyLh4NrrKwlwrx5jiu5LYKFJFMuM8pwrLA2YD80uXZ5S0Is4p_7Qim63KD94HyKNSI-j8ICyVdgeFvqTxZ67fhqg5KfgY1cAjfuhT-nzSlXN9Npo8NGyseCY87n0Rnbi4WRfBWQyT8xldtB1kTHP-YLXNJvTgK1sijfUr9AEv2VJTiV_oe5OnBSU5DSOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69262d7ad7.mp4?token=k3Matu0-v4LPU8yTRSSW7W0hei4k7dVSL9KvE0gNnyGP5-9NC_dnjCUmtLctu0K3SRySwqd_zbL3dGv1i2uneOG6UCgU7WmyhE9AgAYvsfq_6LGP2mLORg7rJdGB7roIteU8ahA7yqGo-cFR_xuyJu6oUEyLh4NrrKwlwrx5jiu5LYKFJFMuM8pwrLA2YD80uXZ5S0Is4p_7Qim63KD94HyKNSI-j8ICyVdgeFvqTxZ67fhqg5KfgY1cAjfuhT-nzSlXN9Npo8NGyseCY87n0Rnbi4WRfBWQyT8xldtB1kTHP-YLXNJvTgK1sijfUr9AEv2VJTiV_oe5OnBSU5DSOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملونی نخست‌وزیر ایتالیا : اگر نمی‌دانید چگونه از خود دفاع کنید و از کسی دیگر می‌خواهید امنیت شما را تضمین کند، بابت آن در قبال خودمختاری، حاکمیت و توانایی دفاع از منافع ملی خودتان هزینه پرداخت خواهید کرد. هزینه دفاع، قیمت آزادی است و من می‌خواهم ایتالیا یک ملت آزاد باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122836" target="_blank">📅 17:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7b04a0e5.mp4?token=Wqr4EjzK8kr2Nr3gND-e0tIpMlQFV-cIgOcvVAtwvaIoX1XpmnNGTP8g7JdLv9VYOZu4qz2Vxi0ZMEOBRfAS4qbIXUcLmgf7CvwGey64cmV6WPDWpeAl6DKS_ddWruqpNO9qTf1XSQI2FI0JP9qc8XgSN4VTPYIUc-Ne46MAjMUgm_Mvc18aATd9eTq55d2zsjq9xQ-q0RQ-Ytm_-tyS0TyGYy0JYyOC0RbB0kCuh0VhJvsqmB_x5iXBWCghSC0bLbNpmGwwVOXG_6zgEusxWfi29sIFah7xJpXJGbOWZ0xwUnn06Ghq_yf8Z0fBdS5zmRFoZrtR-ryy7uqVlV3T5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7b04a0e5.mp4?token=Wqr4EjzK8kr2Nr3gND-e0tIpMlQFV-cIgOcvVAtwvaIoX1XpmnNGTP8g7JdLv9VYOZu4qz2Vxi0ZMEOBRfAS4qbIXUcLmgf7CvwGey64cmV6WPDWpeAl6DKS_ddWruqpNO9qTf1XSQI2FI0JP9qc8XgSN4VTPYIUc-Ne46MAjMUgm_Mvc18aATd9eTq55d2zsjq9xQ-q0RQ-Ytm_-tyS0TyGYy0JYyOC0RbB0kCuh0VhJvsqmB_x5iXBWCghSC0bLbNpmGwwVOXG_6zgEusxWfi29sIFah7xJpXJGbOWZ0xwUnn06Ghq_yf8Z0fBdS5zmRFoZrtR-ryy7uqVlV3T5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو داره برمی‌گرده به واشنگتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122835" target="_blank">📅 17:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سی‌بی‌اس : ترامپ چهارشنبه جلسه کامل کابینه رو تو کمپ دیوید برگزار می‌کنه
🔴
پ.ن : کمپ دیوید محل جلسات استراتژیک محرمانه‌ست دور از واشنگتن هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122834" target="_blank">📅 17:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت خارجه جمهوری اسلامی ایران حملات اخیر ایالات متحده در استان هرمزگان جنوبی را به عنوان «نقض فاحش» آتش‌بس محکوم کرد و هشدار داد که واشنگتن مسئولیت پیامدها را بر عهده خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122833" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رئیس مجلس و رئیس هئئت مذاکره کننده کشورمان که دیروز در راس هیئتی برای رایزنی با مقامات قطری به این کشور سفر کرده بود ساعتی پیش به ایران بازگشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122832" target="_blank">📅 17:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تماس تلفنی رؤسای جمهور مصر و ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122831" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بررسی‌ها نشان می‌دهد از میان وب‌سایت‌های مهم، موارد زیر در دسترس قرار گرفته‌اند:
🔴
ویکی‌پدیا
🔴
اپ‌استور
🔴
پینترست (Pinterest)
🔴
کنوا (Canva)
🔴
نوشن (Notion)
🔴
تردز (Threads)
🔴
کال آو دیوتی (CallofDuty)
🔴
پابجی (Pubg)
🔴
یاهو
🔴
دراپ باکس
🔴
پلی استیشن
🔴
ایکس‌باکس
🔴
بازگشایی اینترنت به تدریج در حال انجام است. به همین علت ممکن است برخی از سرویس‌های بالا هنوز در دسترس گروهی از کاربران قرار نگرفته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122830" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfnBpxm_PySPASjdkf8D5bPNMzsyF-7EfmToW4B3OMCEDT9NW6HwpsLqaVg4_H5Tc5MGsbF2ZuE4CJ2vsao4BHleqCQoQroKLvBEWK97cWr8OND9ogjIHPhOc2jlevkZ8vo98YwgoF_njYkUHGZ1wNJUA3V3-LQ9_Ei4CLTaV25s_DMp_Q1jy1HUXPCHQAOK4IBmeHo-V1lpSqr9gqIiBoOGGnfYpaQShNRkQIUzSiQj6ldxbYqiO626wYkZ5duejDZwYOvTs-0Ujaf2PvoawA7kxNwc6RpGehmthtGTlcjHIcrzbBaAOUB7ck6kXXiUzlhsNVBmnUCqAWM8UGOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در نزدیکی کشتی در سواحل عمان گزارش شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122829" target="_blank">📅 17:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رسایی: آقا بازش نکنید
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122828" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuyAhuudeKooChh7fDwLD3mrHhYytu9GMAFa9_cPV9hi98-H6gVO5tekN9xkbNc8OfYkJTaG2f0aPbsVEFGl8aVa2xWPttv0M7cU6A91XlE3b7HOCRpmmsAMsVCYifyyEJ5ppChe2cwpPj1PHqxXfnS4_dN9mPcW4lPu-RwJ6uFBkWn4z0K0MfZEpVIsPdDEx7zLrk-krbmQBy83hZVBy3g9yXW1BbHNOjNjS6frBgDwCUgLK6RmZ0ZiIbkyKE5AKhotTfZUlxszcyS96brY0tJgluAzELjm4EW5TOgzu3FRWca_LDdLIyAMWt3x-S3oCNIivpwyJGbFxwyyC-_L5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در لبنان فراتر از خط زرد (خط توافق شده در قرارداد صلح سازمان ملل) عملیات زمینی را آغاز کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122827" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع آگاه نوشت: ارتش اسرائیل عملیات زمینی خود را در جنوب لبنان گسترش می‌دهد تا کسانی را که حملات پهپادی (FPV) انجام می‌دهند، عقب براند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122826" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نیرو زمینی اسرائیل دستور تخلیه اجباری برای شهرهای مشغره و سحمر در دره بقاع شرقی لبنان صادر کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122825" target="_blank">📅 17:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
طبق گزارش ها ایران ارتباطات رادیویی را در مناطق خاصی در داخل روسیه  و گرجستان  قطع کرد — و برخی از ارتباطات در ایران به دلایل نامعلومی قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122824" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZbzHnh2PvACpaybWii7IsKeW4Kytwb4P88WcF4QtaghZNqwlsNUkv2aLFnomcCEM7Qn4mCBrz8kiLeVmrsKYbuyW15fu8X_U6-npLAYIxGcOCJGgdYCB1FculQhuusVS-jAt3MOOEZ_1EYlsZNJcZEqB-bmym95PnqHm43WbyOYCoG4ztjFMUN7BDi0LhseDyzQX5ek4b98zdMyNfquBrxVEw_ZpbMR5yp4pDi5S9utguoMLsMJjVyeLGeaogKNiJPZHyVowCF6UCX-aq2W2uNPzYWJkF2HtWX7KmvpPsA0S7Ci3y_zNdxt_1fcCrq1qepTisfharzyTmHXwPVv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9CYuNtUSxpJeY_V-lbmMPgYlqM1KTMoYtjPVqAu0Wn9_NQZPk7pBF5pweab84018qtFtQXIzEoBsAIBzU-5_tnI3m1QH_HynDo0vcRIVZ8kHTBpuyZjP3uPtK4jMjMdpZBBrMyPF5ecW0QAUkbC9xRlUP7xHxos6IbiAeW-IqOhhd5GtQJ5XI-tJI_VbVsz9QX0cqG_lczDphIq6-04n4RAL8TNqdCLVD-FcAQTzMRVklLQjoLocnAPbVg-kN7705AknvqJ9EsNvZVueli_BE5Bsa70BOZxfllo1kVWbhHdWwDkgiMwtLNtO2zWEquxca18yyDPzNkNmODXk6WP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tevxC8VM1DgNcnZEBLQ7sUNGEFcS6qqkXLjTma5rKRXPKSJgQHmQy9IWxXNouVqQj-25KmUgrzTapFrNmwDOMLvEdyBYWB5P6PGNuS7yMPQRvf-iGLIz-7nHI2k_ptxBzfQu7quWEGWFfFKl7T9llsOl72y24YeCeBxkLwlUsbotEpOgbHU0qVskMxea0wp3SxIVK_MK4ax5BwvmNbxPwzGwa1j4FvgZTOYwyTFWXtlqUtlaI3NMKMJtkPwPlGspR_Y3ZROZydv2fvWVG7ZKQjDzGB7jBDqZlZ-Wb0i_Iuz1RFWzzqT6c0m731kZG-oZJdbvSEJFv41KI4mldufdjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به کفرتبنت، خربت سلم و زوطر الغربیة در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122821" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122820" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYjQ6wv3mr81e1WFwXEhr9aU1A33PKYht0oU_XSK0oDflwJbZ_PzF36eyGzElpZg6hnnisWVeAELtoO0CSsVmZLfPetuvArb-mYLVK8060fDBJ_pVmjSmNQwIbpfPKFslwRQoeF3K-0UxrJUJ0FEjwX0BLVyy8b95Xe4wKdMAIYpu16ur7J0bhEGUcxaJLUdG0KuCSKcl5DAy-ApanED2u2RIyh4EmNTCB2lR-HkDstVzd4kTERdrXXcTQ9hrMKOTiIXjYCE-2EyzjaBwRrNWpr2nDcmtLwf5M71fhozsAbfhi7j-xsF1lXpXXao2fl6MvkJ-sHGg8RuPK_RTLaWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عارف: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122819" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkrlKLNJtMFP633NTumKVREVQ1MJpweXDNtmDK0VhtS77a7bQEAIVsZukzcpIBQ6iY89dcB7uN4l0p3mrvlu7rF53F5yKMeMcOqkM24BeogIWoKsJ7oOyR6iseIyO78vji6hVjmml9o2fFMVskjTK2FC2NXMEuklavF3bNPVybHPHRbepuNKqKKhL27Pv7pOxQAHfxmDWLVetfD9Tz1VPU9OHDVkr7qu359gAPjUjhRNQaZdMa4gOCURhIAoCXM81_gHiryH3tq7RXQhI7TxxfPl6sgY-ofugPXLg_t7TOUoIfg2hT_5ZP-C_bVhorWCFOlVWFAzDDmM03nXOyPYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صحنه‌هایی از معرکه، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122818" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122817" target="_blank">📅 16:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / گزارش ها از زلزله در مشهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122816" target="_blank">📅 16:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KORMaq-gPVQ_5BRQiC-0hoKJwWlv-DjkoQ4_3H_9wKH00s4AvUIxO0-ZITWrMuy96Qcf3Fp7_bp8yV0vQxTwEVM4ApLaULVwzp6ZoH7LhNQIMVdT1VthqFiNeaoVjOWO6v72qWyzkpqmqKwIPEwrbE8RE9n34VBoe4CF40nxvd_zXf4CbjxARMJyAdeHP3OHl4CJHOq0c3phFKa2wTBbQjvmuU_M5KwocRXq6g_GFguyWksKU3AGq7w3Yxpsk-JTSW9Zc27YXG1bmdoYZAtm4XJ78iyMJNJyJsly7mh4dUgVyxElPAdRSRilCOoT_r6YOO7ZmXQgFA0HQeBKtQQ7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R92ae5kgg9LvzN3n6AlrWRiDKJgJamAOsV6W0md_La_e5DD5DlhxqDRZ_rCJbdzeigqAod1Qj_2VNIT4X6-PtwOrcp3k31SsWFYBxwQDyXRoP3GnZX-ICKwlN3Si4oYscHybF1vLcZdhRKocK2RXP-ebVlUx7bUn9NUDqC3ttClxO79N-mOY3mawC6_NUBUYSdfwWGuzvvO9SLfX2CD-sebRgCUixjQyezEO7h2Of3aTUKB0lFQXKe-pb752zLJt-IBPu4aK6WKKE5aIlfCf02p1BmUeV--52kMuEnvjMNQ0bDtUd3JFdYE-RiAwZ08jLdtnpXAAV2_4ITUfJgCmtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست های جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122814" target="_blank">📅 16:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فعلا پروکسیا و یک سری VPN ها روی مخابرات،شاتل و بقیه مودم ها وصل شدند،نت موبایل هنوز باز نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122813" target="_blank">📅 16:43 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
