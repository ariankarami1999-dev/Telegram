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
<img src="https://cdn4.telesco.pe/file/Uq2P7yqrbh__jOzt-ndwWLWjF9Zlu94hTsHp3oDaDl4nLIJA6_IyVweLcBQu8s78gN2T7qTa5q1YS5m_39V00bsyDVQO6Mcb5dFUCJZ3GGU5cY4APi7scDhCEdPZMVx3J-do8IXwhopqQg3wyalRPpOw9O5YD8kRrX_zHrfzCgpWAbEehI3GDwAXhYEi4VR1SXvfYLmxIJ1BHlZplc8CfQy-rF1Z4V3_XvHunjhjYy_7eWovMf_ok3Gurm1Qn0-NuwPvg_arfEpBWIz5mEpB4VKqvr720W9UlLgJrqTNhMkLaF-N7AB7bHtPl0SXy0RfkJ3_k04AvSuB3mVAny_-EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 15:16:57</div>
<hr>

<div class="tg-post" id="msg-437672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انهدام دو هستۀ تروریستی در استان فارس
🔹
اطلاعات سپاه استان فارس: ۱۵ نفر از اعضای شبکۀ آموزش دیده که در اغتشاشات گذشته نیز فعال بودند دستگیر شدند. این افراد در قالب ۲ هسته سازمان یافته و در ارتباط با گروهک نوپدید تروریستی فعالیت داشتند و در ایام جنگ رمضان با حمایت از رژیم صهیونیستی نقشۀ توطئه و ترور جمعی از شهروندان را طراحی کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 146 · <a href="https://t.me/farsna/437672" target="_blank">📅 15:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/437671" target="_blank">📅 15:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUImi_Ak6XVQ_jAuqMIs_SxyxCliRqqloI2t_vQDfl17oj3jmVXSdgXz_WWOlL4ZIWBUlcHqFnS7uIGaf7IwWW_4h3Ii7RhW4Eq5hXTFK1fWkhFRk9uN9aSn1jZlZx_DkjBjsvLncOB4Ab907xcqp6EbjsW6J6pwMuSv9Mqkr8AdbVoMJg4TksHaYQK92LW1f_nDYmSMAifFy1vRnP1rFj3vjbKD-jfCtXm2WBxK8M5ZzeLay-iTxcRBw15qtl_DwcRqEmVkk3sASRgMpgs32OKE5_1KCJSv2zLpUiseEBzLxscR6TyIkcXgHwiemaqbAOxkV3VTIHEdqjqtCyJUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: هیچ مسئولی حق اظهارنظر شخصی دربارۀ بنزین ندارد
🔹
اگر مدیران دولت از این دستور تخطی کنند با آنها برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی با در نظر گرفتن همۀ جوانب امر حاصل شود.
🔹
لذا مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/farsna/437670" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/farsna/437669" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT8v7J5FKbJYtHpr4m3cByCcTCaNrmgE_mRus0W4NcldlsM52FgLQpQ_7vIY8jFzz0bhT9I5QK7pbNKtU4nJybS4X_Jktc2auZPrNSVCjNMv-Xjxjw7qJQKMyarj_asimmfTsY5JG742jV9ml4Bxl3iTkRpwfUkTI5UuhIayKifTRgeJ5MwrgjXRou3-zGIba8Ox_fMskxH39INiNYQky682kseIPBy54goj203B8EkY9ky00C81THYh1QtDqU9hNIehq1m5vQ_4pEqShwkmZF5WcRsKtuqOIEXqJBiFOm7zmIVLUTZ0xTp8UVMJy42ieoIo7uH-_J0wtFvcYMheWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نسخهٔ فوتبال عربستان را پیچید
🔹
عربستان در عرض ۳ سال بیش از ۳ میلیارد دلار در فوتبال هزینه کرده تا پرخرج‌ترین لیگ آسیا شناخته شود.
🔹
پیش از این گزارش‌هایی در زمینهٔ کاهش بودجهٔ جذب بازیکنان خارجی سرشناس در لیگ عربستان به‌دلیل عدم سودهی و ضرر ۴ باشگاه بزرگ سعودی مطرح بود.
🔹
حالا نشریهٔ اکیپ خبر می‌دهد که به‌دلیل بحران ژئوپلیتیک مرتبط با جنگ ایران بودجه‌های اختصاص‌یافته به فوتبال در عربستان سعودی به‌طور قابل‌توجهی کاهش خواهد یافت.
🔹
رسانهٔ فرانسوی نوشت: اگر فوتبالیستی تا این لحظه نتوانسته با انتقال به لیگ عربستان پول هنگفتی به جیب بزند دیگر این امکان مهیا نیست؛ چون بخش بزرگ از این پول‌ها باید به مسائل امنیتی کشور اختصاص یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/farsna/437668" target="_blank">📅 14:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ آخرین وضعیت تردد کشتی‌ها از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/437667" target="_blank">📅 14:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvslXMBwcIYV7VUihk0_khpHMVa6xOBtCiQd8DRvb-vgwKYiGuW9rL2v0C9bMiFBkjB1hKQGLBhIQna-Zq_Bq_ZYOxzG8Y1YHyYGvVU3oTu6dpcK-liFKJ3GLi3oKsidl8pR_Zb4b8V3G70uw8KWBwr1kIBv7nNmgkmBRu2IjPP1Yqv4Mes-Co5lFVLurIsBqVjJczI8VFY2mCIuQyYsQpuey5gjHbFU7OhOkyRQLnKk9oc4gkg9fzTuBGS8uUZ6gBsx3mbeIS0SPEu3kn2rssCRCL8opD9gvb6_be4egzHEXaoLC8TZnBhJ4MxYB5b_O5ElE7mbh4nTeSPTPLHRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZkLws7E0mIakiRoyVwVRs1w36X9sXIkn_6MOA2l2a3hWgDbE0KYGumrl5_nuKTVAk0rWdZaKJkNyFhV_zs1SbjLwFki1fhKr9g0N0FT0bOsjjfXLaLuyZHOxnUb2GnN0az5_Qjq2beZ-P8R96gyrFQpBVHDdngdI5JkMP15HjBhn4KsbVkWMXh84P2Hx3mbvF74tAHbknVJz_2wlFyNI6wLlWrtD3Nh9-Gzs9kEr6JcNOmF5wBLoeXRrFm-GBI9UJEgD_rSdS6F_NVJb6qs4HRD2r0SdNkHelDgLGqldAnXCBtYla4FvudsjdELWQtD82W9k2zUPhb8_gi_97Od6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی: جنگ ایران نشان داد آمریکا بزرگ‌ترین حامی تروریسم است
🔹
مایک جانسون،‌ رئیس مجلس نمایندگان آمریکا در پستی در ایکس ایران را «بزرگترین حامی تروریسم دولتی در جهان» توصیف کرده بود،‌ ادعایی که با واکنش تند کاربران خارجی رو به رو شده است.
🔹
کاربران شبکه اجتماعی ایکس با اشاره به ترور شخصیت های علمی و نظامی ایران از سوی آمریکا و هدف قرار گرفتن دبستان دخترانه میناب توسط جنگنده های آمریکایی، با رد ادعای جانسون آمریکا را بزرگترین حامی تروریسم بین الملل توصیف کردند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/437665" target="_blank">📅 14:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-73GK6mkTGG5sykHdcnZfNQsSFKQMV_2XynuoWW7wcTIJ2Uqj4FWvGEJ_F8_CxmRHxs9uw4hENwpJ4CvSDfav80s7ecoXjG4h4uhFX-Vm2fJViQtOIjBjXPSl7AmkHHvAAl034tS3MUrRjnW3ooEdlrnE8rpoY9JW_wA96FZaM2gSKuXn55IdWIiKmQnkAlfanQtOq78S7hShvE-tDT2FuQA-s909gGg8Y48JMc9RvZLXqHvSw8NAqe68z8I-rR90JNyYLE8GVWXwg9PdSHxgikJkdV5reiY5bV2ok8_HXseL5uoffou4geAHaNr8auD1SWZqskzLy9O7bGLMEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حاجی‌موسایی: برای شادی دل مردم سخت تلاش کردم و مدال طلا را به شهدای مظلوم میناب تقدیم می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/437663" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست پزشکیان با مدیران صداوسیما  @Farsna</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/437662" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkEKWmUcdjbjFN3eNmUAaa7evbwghQaHED1Sq0-E3Ti1oui1GAjeIQ42QBAG3gbPnBpmFdYJ09UR3X6vufc2UfD3Qq2EfqgncJQ5YhKUIxMJrwgYXjyo_bO_cDAyPl_8pjuPKRNsrJOnCA2kjhdkC6i6WKrxCEMIh1OHv9w_Z2V1rZUc6MLl4zxvojlH-J7PeBkEOwsUcaL_PRuImfrndbU9XQglD-VwwxQic5ACyghg2Qpg936dAbDTZLvLb4FsdOaEWGSdGh42HlvtoGBrDLBH28HyNgzQKPXokGcf65iOT4DCBYhSUqYo57YthKnisPzD6ZYt5JezeWi2vdIhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmhlbQaEaRJ602UKdR2F0MoCnQyRYtVU3EIxzGL28LBoEKDSa4hBMlUH5VnfgcHM24U11kNCe4mFINXV66y9sMcsI-Ce9I9tQttvBZEjYIeJ4bQZt5i9ahg5Wh0QQTDzOYvNIvczgAK8BNhq78BOCu8s3ukzdPHRKu1YsErCLPFpy58EcixWlwb4k3m0dhYFaPMk0iLuVE0UZl8eZZPVyrWUanOsklcV9vEWEjaxv5KBBIey1Yv83uy6UWJy8C4quY8tZWJ-23C-QWGVoa-T8-o8CmoCHLn3DBy6GYenqDCwqKBMnhdacIAhs5snDgVIglJiMkiW8OfU1zhdbrLFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZK9EQYnCmoaXo2uAHXeXjmMbXSCgFcHs_d0QEwBM-44NvzDfVnoJ6YfU5otN0R0R4oJQUs0SQxxIpsvzXYeFtrtqc7-AqrmbhH7Y0o5XUGdX9az1xPC9nRsgMYbNNvQxD15lUp2Kph_i85AZ-ww2h_X03rInwa2JAsiyvkqsi0ta2DVLpUeQqfG9s9UV9vjLOrzIDi9MUHKTkrL6qMiSBnJzSQV6GqxGC3ZV7mY_LSRi_1-lr3yOpygJ7QrvQaqVKjaoUeRQ11fkOCTbcVQLuDNKwZ99tpHa-NvklDs1RGvmFvi0ZKrk3BCxcSQjBQw_arEeR-yy8OAaFKvKjdW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_kuzd2iB2Ki41B8FXUy9g7OjNGGTVjBD9cTINYh1tWZG8HOcjj_8Ro9quNG6OnZGjScyJWx3kL06nyWS1nRmSHghLo2bmnsVzELu42uPdLTF_M0ilsOLNB6vitySn94yQjTcozChy1HIx_uoXpAoyGSZVPSK63Bp-mc1ZLN03nisW60X-xK7TQD5Pw1guB3nWTaAjhG817UE7gJB7PRA7nnlrQXMjj6zJauYkG3cUW2IhbGEkSLbNkmJmkNGXcU2NmMxYfBPf4guVo1CvBMc1NDaVrEtW1bQw2EVpXTV6wxmNcRYUInVxG-uHQNTSKES3pxNbUjgc0LsZ9WtG0Ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuhznwlL99cnIz4eYtne5E9YwEfNfii6oOKPilhOt_bVhDteQ0wt20fZrskrLICe2ycjDc8fp78qbxKyDYXh4NYPCnbf2-zEAeX62-778KIXFgH0ylDmmrd3vCH4ZjDKBYFP8uGVeyqt_tMa_oWYlsVxJiB7lH_VIx14H5T_XcjT9Nm-fhGOs8OonfZWld6o4cnzKd2zu8YLWHqMe1kVEK76L8m1xeUblnGz8BCbGGn7xe4xv9S0OPVDronNtBcW8ur6Y07ZiocHSSlBo8-vF5NXCqwECzt16SI88Lt47-mjHwGvXRre7gKSfXDxmdl41Ax4SCd3HpPsAJVsnM5PXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-udEcpq0Tu9CANJMcnAYjj9rm-GJlD_xxRKM0NHZWOzOlLm9UNKygv70i_pqIPfD_iuSzG_XTnbCvoCUUozqszkowgENNkfr_EORVeLuqvzr6yEID5RFFQDZi5UjUjaYTxmE4GAyw6vwzMNjFE8wG1MA5gEiWq8AX4c7MCYRN5PS0jE33OS6u5-TI6saVShaVKsbXSeacyQ7NFSKSzUxnkjGN8ew0oC3tZiE-UG8JfSwP9Y8Ff7E7Pxs4P6-PARcCRRTZa_K7Y_GPXbQ0-8LxA-dU0D2aMSaXBK2ZBC4nn1u6WRF1SjpzDia3o1193fmL35siaWZOgtXbe2Z6KizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdnvUJXia4U6lFtTkXPdzElzrYvxDB8Dn8w1aG8z00ZmHPvRkK0gVxVHdWoTL3l1o1eoOR6HaRRa55aCgml6wj8QiSRIfDhchm-EBRm6vg8j1uwcUfr-ror-Ca4StYrM8VhyZZh8ktNIXDmd0I3yfgghPuiob3Uz6ohOKGxnI2ZQCpzBRZPXUVOBZ7oZMMp1rn5M1hMZCIOWtqfU8MKqbegAeROg6OTcWiQ10nWicmvg_3Oiole_QIfdEY6vjHM1dVJiGVnY1mMhyzLBLQj7qShWZD55zg9jJbjiuYnSJouhVxSc9wiLc0yV1wv6Ys3LwnbOFp84MsUwabk2xF980g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دشمنان این سرزمین راهی جز شکست و خواری نخواهند داشت
🔹
کسانی که بی‌شرمانه چشم انتظارند آمریکا و رژیم صهیونیستی بتوانند به کشور ما آسیب بزنند و تجزیه و نابودی ایران را دنبال می‌کنند، باید در برابر وجدان ملت پاسخگو باشند. جنایت علیه مردم بی‌گناه و کشتار…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/437655" target="_blank">📅 14:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTs66IKUIDpI7F-moMnhnA0QyG4_nRk68qqmeNi1Ic9IabeNYyg_VrfyfUM25lfIurLM-tZ-VwArGXFLhkfz42znoHP6V7aYNV_8V_5ZEOoY_cw-ROEaEvu7kFjYxVx_K6gAf75CSTJ9IkBuTDTZLSBCr4bxnEtZk46VDbnsiPkReaXfFNFw0ty6LoM09tFJdBMOmklP-Izl1TVfW-GuQE84Pta_PW8WE5jkp9b5xDWVF0W8al0WjlAOdL00CW8UremSzuugGVk-hDYdyFYzk3oVw1QPY5Nhhan9WYT2W35jhcJ4RYw3i-QeUkbLvuuwNzzg9AlQP0_PPGiRuDQPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اهدای مدال طلای ناهید کیانی و پخش سرود ایران  @Farsna</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/437654" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXiLCgkCzwiQKZi2OnP546A4YSugFoBKjJNFVw-xn2UdN1Aq6KGMrDH6w21hePe_63VacmomxV_cZ5ay8zq0jQHwQxbtv0SZyqZP31pJF_UrJkKuoxAYm3iu_jj4Qsy44DqYy8DrrnEvkx1Cca9Kvu19WyFahwZIpjRcZUhunbAAy_T6977-woo3v7by1aCEd3o6PWrVHaKcdUsXuO_f-aLNzTHNEQGcu_fw3dm9YyyTvhQBt3KC7_847MBmc2VzOds6L0AOb2Ob9m7mNBY47pJpPSjqeemo-H1dpPA7laXeZFmsry1gAhOZ-cASt8SSMVIqZogMZK3Y-XRklfzjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام ادارات تهران به نصب تجهیزات کاهندهٔ مصرف آب
🔹
سخنگوی آبفای تهران: براساس مصوبهٔ مراجع ذی‌صلاح، تمامی دستگاه‌های اجرایی ملزم به نصب ادوات کاهنده و رعایت الگوی مصرف هستند.
🔹
عملکرد ادارات از طریق قبض آب و بازدیدهای سرزدهٔ سازمان بازرسی کل استان ارزیابی خواهد شد.
🔹
کنترل نشتی‌ها، عدم استفاده از آب شرب برای آبیاری و شست‌وشو، و خاموشی آب‌نماها از الزامات قطعی ادارات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/437653" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSK-E4i6t9K1gE0f-qYAMENjZrxHksXM4QL-ObRvN9kldKCXN5cbk_KtjQVFanFyx3-AhS91Ar38Zncc0R6vJAGiSvmP6NX-aOBv2M7iwlDKMoWhtUSnIWI_3SFf_aHWw0gtoBeELdheATyXkE2Fxeek8tMeAkbYr_73u4GwUljRJngr7SdB3WmjJRTc5z8S856OVpozEGPJGWeXFi9NTS8Luy2EK46YXgdtpb7f1nkmZpTed7Sc5vT_deavfvqPttPERriocRwHkwoiAWQtS63dnPCcGGE68osUAtwKgTe0YQlurnb_QphJr9CMwW-FsyIOgCqCgENicYhWUbgKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هلال‌احمر می‌تواند حلقۀ اتصال سلایق مختلف اجتماعی باشد
🔹
رئیس‌جمهور در نشست تخصصی با مدیران جمعیت هلال‌احمر: ممکن است برخی از افراد و گروه‌های اجتماعی به‌دلایل مختلف تمایل کمتری به همکاری با بعضی نهادها داشته باشند، اما هلال‌احمر به واسطه ماهیت مردمی، رویکرد امدادی و جایگاه مورد اعتماد خود، می‌تواند زمینه جذب و مشارکت طیف‌های گسترده‌تری از جامعه را فراهم کند.
🔹
باید به‌صورت شفاف مشخص شود که هلال‌احمر چه سهم و ظرفیتی در مواجهه با مسائل و آسیب‌های اجتماعی و محلی دارد و تا چه میزان می‌تواند در فرآیند حل این مسائل نقش‌آفرینی کند.
🔹
مبنای هر برنامه‌ریزی باید بر پایه پاسخ به این سه پرسش کلیدی باشد که «در محلات با چه مسائل و چالش‌هایی مواجه هستیم؟»، «کدام بخش از این مسائل در حوزه مأموریت و توان هلال‌احمر قرار می‌گیرد؟» و «چه میزان از این ظرفیت بالفعل قابل تحقق و پوشش است؟».
🔹
جمعیت هلال‌احمر به‌دلیل جایگاه اجتماعی و ماهیت فراگیر خود، باید از ظرفیت نیروها و سلایق متنوع فکری و اجتماعی برای توسعه مشارکت عمومی استفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/437652" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ اسامی نامزدهای انتخابات هیئت‌رئیسۀ مجلس
🔹
اخبار واصله از جلسات غیررسمی نمایندگان مجلس حاکی از رقابت نزدیک گروه‌های سیاسی برای تصاحب کرسی‌های ریاست، نایب‌رئیسی، دبیران و ناظران هیئت‌رئیسۀ مجلس دارد.
🔗
اسامی نامزدها را اینجا بخوانید  @Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/437651" target="_blank">📅 13:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه مرکزی خاتم‌الانبیا: به دشمنان هشدار می‌دهیم که برنامه‌ها و راهبردهای رهبر انقلاب برای مدیریت خلیج فارس و تنگه هرمز، آینده منطقه و نظم جدید منطقه‌ای و جهانی را در سایه راهبرد «ایران قوی» تضمین می‌کند، که بیگانگان هیچ جایگاهی در آن ندارند.…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/437650" target="_blank">📅 13:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/437649" target="_blank">📅 13:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی در برابر تجاوز دشمنان در جنگ تحمیلی امریکایی صهیونی، یکی از شگفت‌انگیزترین رخدادهای تاریخی را رقم زند و مقدمات هندسه جدید قدرت جهانی با محوریت ایران اسلامی را فراهم آورد.
🔹
این مقاومت و پیروزی بزرگ نشان داد که باور و توکل ملت بر قدرت الهی و تکیه آن به توانمندی‌های بومی، بر هر سلاح مادی غلبه می‌کند و مسیر پیشرفت و اقتدار راهبردی به سمت قله‌های رفیع عزت و افتخار جهانی در عرصه‌های مختلف را هموار می‌سازد.
🔹
اینک در میانه دفاع مقدس سوم برابر دشمن، که کشور نیازمند هوشیاری و هوشمندی مضاعف است؛ تکریم یاد و خاطره شهیدان اقتدار ایران اسلامی، چون شهیدان همیشه جاوید وطن " علی شمخانی، سید عبدالرحیم موسوی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری، ابوالقاسم بابائیان و....الهام‌بخش ایستادگی و پایداری ایرانیان بر حقوق حقه و منافع ملی خود است و همگان را به ادامه راه پر فروغ شهدا و تبعیت از خلف صالح امامین انقلاب اسلامی، مقام معظم رهبری وفرماندهی کل قوا حضرت آیت الله سید مجتبی خامنه‌ای (مد ظله العالی) ، فرا می‌خواند.
🔹
در این مراسم شکوهمند که بر تداوم مقاومت و پایداری و هوشیاری و هوشمندی برابر دشمن امریکایی صهیونی تأکید دارد، با تأسی از رهبر عزیزمان، “ایران اسلامی با شکر عملی نعمت، منطقه خلیج فارس را ایمن خواهد کرد و بساط سوءاستفاده‌های دشمن را از این آبراه برخواهد چید.” و “آسایش و پیشرفت را به نفع همه ملت‌های منطقه رقم خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/437648" target="_blank">📅 13:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYlOvaCIq7JPtopy-xKUdbnIRfQ1CIW22BZD4_zoWOew42RhPRGUHdwnWESTdQnsTRoOTd6IPzyHzoh5DTrAULgQygrKXW07R_Xst4UMpBDNEHj8MJWFP5RIeqqTSktHANT54_kQoJm4kG40oMOdXD1KVlCci70rA3iKvSaxav7NOygVuTNQ2YAV98fZ7A5HGsKaRNR791rny3830UQaeCNUdNIFIRLHsr9TzoPzfRPVaRuw0Cv-p3KFhHZvUCh7U7GSbnVC6JQWcNE1sPNj1xRfh1jySWntQ3-0kOkW5KQAtWpuj216DFGzNxL23SqAxA_8nWnLBUW8G-R24fOIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/437647" target="_blank">📅 13:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437645">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌ احتمال دبۀ آمریکا در یکی از بندهای توافق اولیه؛ ایران بر مواضع خود ایستاده است
🔹
درحالی که مذاکرات به‌سمت توافق اولیه پیش می‌رود، منابع آگاه از احتمال بازگشت آمریکا به رویۀ قبلی و تخطی از یکی از بندهای مورد توافق اولیه خبر می‌دهند. این چندمین‌بار است که…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/437645" target="_blank">📅 12:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار ناهید کیانی با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437643" target="_blank">📅 12:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437642">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymx6s6F10_1X3t8LN5F00Upajhq4kUB4jWSKe9GQ7tgR-mKWqWXRrTHmZcFI6nYl8WPFrh0dgU3aGvm2n_hF7YLNtAWG89vF75biE2DKfkNAsiv5gwZ0LaOmrYAzfqkuvJZFAhDCGBXqYTQWNqb6Xofg9XoCxmXAT5-7qAc4ozlR-lApxlUcCbVzsYe0iO1ojeV6TA9nG45qUe9upjUKEYBW64IOGe4TqdQNpqskUq8lmoN95DWB3Qs8qjOgG9giVe5qC2MCDvx-SuOLqn6Bx3J82Z3dyfLMnimKFQUA6LgXI7_77BU-gbbJ4jsZ1X4oVfB177tY7g0y_-6ER3ZssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احیای هپکو میراث ماندگار شهید رئیسی
🔹
مدیرعامل هپکو: شهید رئیسی در ۲ مقطع حساس، نقش تعیین‌کننده‌ای در نجات هپکو از رکود و بحران‌های کارگری ایفا کرد. اول زمانی که رئیس قوهٔ‌قضائیه بود، با پیگیری مستمر، در سال ۱۳۹۹ زمینهٔ انتقال سهام شرکت به سازمان تأمین اجتماعی را فراهم کرد و از سال ۱۴۰۰ چرخ تولید دوباره به حرکت درآمد.
🔹
دومین کمک سرنوشت‌ساز شهید رئیسی در تیرماه ۱۴۰۱ و در بازدید از هپکو بود که دستورات صریحی برای حمایت همه‌جانبه از مجموعه صادر کردند تا شرکت بتواند از آن دورهٔ دشوار عبور کند.
🔹
همزمان با پیگیری‌های شهید رئیسی بیش از ۵۰۰ نفر نیروی جوان و متخصص جذب هپکو شدند و امروز هپکو یکی از بهترین و بزرگترین صنایع کشور است که در توسعۀ ملی نقشی مؤثر دارد.
🔹
پس از اقدامات شهید رئیسی،‌ صدها دستگاه ماشین‌آلات راه‌سازی، معدنی، صنعتی و سفارشی تولید و نام هپکو در پروژه‌های عمرانی و معدنی کشور بار دیگر احیا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/437642" target="_blank">📅 12:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437641">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌ رویترز به‌نقل از یک منبع ارشد ایرانی: ایران تحویل ذخایر اورانیوم خود را نپذیرفته و موضوع هسته‌ای بخشی از توافق اولیه نیست.  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/437641" target="_blank">📅 11:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437640">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvW6gM4dVfHYS7LAfDZHPRznwkQryqDazmF2yc3XlJu1S7v6IaSUNXWH_4Z-0pICsfAMQZp8_dRW7ADa0KSzelp4z1HtPtN-GZyqwEIX6jqmSMGyYDBgJNeNx6D4RnPKzcsQnqvWG95ITYM-DN3VcKKRc3HRIGS_6yhBeOU86fOsZSxR4jmaUJUNTbRyU8jcr-LaAcSgyt6J2clX6-ifFoUgTLCN6xmVNu6j_x0YppVz8Blojk0B-9HYT2Sf-dGNN-DIawC1gqgD0t8Eg4D6biQ92L42sNO7Qf9gwQlMxwWNm458CsxCNgcEANculNg0aw1zazI9OSyHJ1HQ1g_J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره‌وری نیروگاه‌های حرارتی ۴ درصد افزایش می‌یابد
🔹
معاون سازمان بهره‌وری: راندمان و بهره‌وری آب و برق افزایش پیدا خواهد کرد، به‌طوری ‌که بهره‌وری در نیروگاه‌های حرارتی از میانگین ۳۹.۸ به ۴۴ درصد افزایش می‌یابد، همچنین باید بهره‌وری نیروگاه‌های جدید حداقل ۵۵ درصد باشد.
🔹
قرار است در برنامه هفتم میزان تلفات برق در شبکه انتقال به زیر ۱۰ درصد برسد و تلفات شبکه آب‌رسانی سالانه ۵ درصد کاهش پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/437640" target="_blank">📅 11:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAwMt89J9_5ojRLhmBhVUix1MyZsKtvRr3cJEhuCvpy7vdzR-Aml-DtGtxlHQTQM624kHw6_xg_jg1DNVP3TahXyya_Adp4Oi-S-l40_wCY-0YRTafzy-jqRS6q75iTihYCnWjB0uyikoCjykI6sHFfMB4gFqMKMrIfgVVvAwOIgEILs8VV9vBFy-lyWgkaI_dbAZq7UdhBC0oksitpjJMS1BEoO8Wa5gL6HFvKuc7XkH-wwbE9RoWhcLBjHrYICj_1bDCZyybhrgvm7RigQAG58PeybZyt-CKNXl8BaYOvfkNe4ytSbSJzwMqBw3NDG5939YBJEcrMNL9z5qkW_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDk382UZaTq1w8703PXE2mKDNs_2ZXgsoxFFVO91Ti99AloMrmS7tGQhEvz0181D8NC80ymw0ATaLLyKQQUEH406pcxbjwH4MYO45pRtJqBdCtyYI3PLnpgnc13PMyJq6GXqvLGBCEWwUm-HqolC_aAvydcNajKyWfqBLX60WTPEBGUi-SgRHDrPcaaRqiXmOfdaRqZHe2Mu7X4cqFBO10SkPU_ybPPqca-FXzJsJo1fpI01_5QFulYl65TvimS17cVSjQzP8KZAds8_Dlcv2ctArWyx6q97rVdM8m7Ao4FWGE61hU3ttT4DuM2a_crh6Sp_nxOlvLMMd_bHR1GMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jASwg4s9j4OfX8ZkN5Xtxn_12AF3nZNhFs8fzBzpU7JAG3WxDc7JnTrePjiSfVUtkLvtCzJTBJYrENvvHBDJEiovsAuDYMU18lhyIU7sX1lTFieg9yK09076fNOu6PsNdDPaZ9CxfmzqIPHvHE1m1B64sI0_gHZlrCpGZLsD__xj9lqxLITun8kK244ABjoujhBzn_7riNlmqUDFRRHqDybd_CQeNXmyDjAoCrY8P-6kx5kMhNbrgNNyxxnVMVWklinIQ29JXcKKJQQS7DmSly5FxhptAK-LsINQkDL39akk4JCa7-R3BKSLjWAApkWdI4pKMWbGH_9n-n2XSUzG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PeWVyomyLSz1Dx04If6AyKZxj8-FfgCBBsHQ-t8zRDCmqoSVl0uXQk7QoMgJviIBBK99Gye7S_VGViY5_FgdBEwXd73Z5tIjG6taW9tbacXbOj1gmDOa43n69QBWrLLDRotEMDSbI8WwpjXwsDpvMX6YEwiyqVyhGEbF0bTqUKFz94GUTSA0Y_chLJy6MYtDUWxkf5QYU2MpUNJldMMIo_ed08sf6T7LshGFFbIxvIMi3tCkbyF_Izy2tT6HDIXomsEDkJA0c5Xv8NaFln6NoU_Dd2f-cxKsVJ5YN6ygaPVslR1vIhAJA_6rDdyzMAJQa4ZMpVqmxSLOwq53XREOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYZeUzk4Bt6teikPCYguUCnrPdLbgc3sZhIuZyQkUQuF7ygyqyhKgxm8VLz0Zbd7OkCZIpLg0koMZInrFPZgKEzbUKwFkY0l1ruamipd47vRX6dzbc6jrW2AwccXAjeRYYqkHrsccrtJ29lzRrF58CSosb6Ubur3Wkjr8Q3_ua183k7LMDr3xGR72xMwYtMIGIf31TEvC-ftYjzX2ooEeE9JeLti0m7Fe3mZyscFV2Pqr6TowESf4nqTI65EKqXpP04wt--UVsR8LiiV_DBMXK2mOIh5R6i5pN_TjvapZN8algXa7-TGX3BDp-6qovZhGkjRg_CNspuZQZ6EjOGMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfW7IWKBftP3uzgjyeSouiHbBdD3xWASKu-F1dlNP4fE7RWoXHrDf4nZgp7sjndZfCvpFFEEJuKFOR4uv1QcjyJfUOH2u1lE1UZyeW0EFl6U0iuQBs2azM2N0XKdGLz5tzUkQzmSn2dzGNKOLuFJjINuUCjF7nIFLwsorztKAOz90nnI5EPpbLEClUNRrkNXEe9o0LS8sXUWg1kZ1_91ABWF_JMck8eAqmJRRSzyegnLmnvXo256wT0IkzhiGMn-bfBqxRXf-LlKDY4FnJrUxQ3m4kCJ92R6cfmgMsf-8WiLTzgPsuR1o4zBFeYfGylLLB7J1_hUXU16EP8WM9rgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWFJLyl7crw2vGaaK0VjGBDCtazYjg26qhC-tsmo1kFXJP_7t4RlY2BL0LqVYFDLguv3BdHrUgZm7iTyygHXlWFNiY5I9DJ8r-DqMhDVhcC8BzyYT5P7-oKeZJvVq2IFjVO22ytRdIwsA5EF1rMdaMbfiIFHk-mziVfQavzNSE5QyPIcN-f2pdK_rmxQODroc4xWj5Jib4JJtyHkUAiSohPK20pbY9NUCA-waaqUuDVFkFf53oPEvCZxazgsD_NPyAVQVUcFFRj_JKz3NcLdAPJWNPND0HCBLhp7AAJj13hNeHJ2mdQ0cHWi6bfYrV8cO5C3CXdMFCyaY2Ox4H8l6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین سنتی عزاداری مسلمیه در حرم عبدالعظیم الحسنی (ع)
عکس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/437633" target="_blank">📅 11:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌ پیش‌نویس توافق فاقد هرگونه تعهد هسته‌ای ایران است
🔹
برخی رسانه‌ها و مقامات آمریکایی مدعی شده‌اند که «ایران در توافق احتمالی با واشنگتن متعهد به کاهش ذخایر هسته‌ای، خروج تجهیزات یا تعطیلی تأسیسات خود شده است». اما بررسی پیش‌نویس نهایی توافق نشان می‌دهد این…</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437632" target="_blank">📅 11:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f0108625.mp4?token=NiLIM3DVUKHVuOUOu4LXgMTNrWPoValLNXAsUxqM-GGFtLMC1TM7p_sec0z4FbtYuzDyfTBIjUf2WdE-rbw5_JItzYG5m31WAAB2Os2BmwzaqebKMnpiwGgOym5e60Z6YpkKc1W5hDkFmQyJXZYTo-c90jbOnEa0LTlXFBpw5dYnegg-S4-ib27rYA4nFU31cfIW-M-Vcs3Ee_XKFDDANfOzagSFG53lyz_D08WsPdS2d0llKDizOFdpoXRLN8_YDXHSAtPs9CRBm-y7ixM0pL4TE4G6I7ulD63biVDYJFVaCjH09bJOUlM-kmEzxdq8_YIbgJ7ShOZdSIx2tIQS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f0108625.mp4?token=NiLIM3DVUKHVuOUOu4LXgMTNrWPoValLNXAsUxqM-GGFtLMC1TM7p_sec0z4FbtYuzDyfTBIjUf2WdE-rbw5_JItzYG5m31WAAB2Os2BmwzaqebKMnpiwGgOym5e60Z6YpkKc1W5hDkFmQyJXZYTo-c90jbOnEa0LTlXFBpw5dYnegg-S4-ib27rYA4nFU31cfIW-M-Vcs3Ee_XKFDDANfOzagSFG53lyz_D08WsPdS2d0llKDizOFdpoXRLN8_YDXHSAtPs9CRBm-y7ixM0pL4TE4G6I7ulD63biVDYJFVaCjH09bJOUlM-kmEzxdq8_YIbgJ7ShOZdSIx2tIQS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: اعتراف می‌کنم در نقد به دکترین دفاعی رهبر شهید اشتباه کردیم
🔹
علی باقری، دبیرکل حزب عهد ایران در گفت‌وگو با فارس: رهبر شهید، معمار بازسازی قدرت ایران در جهان بود.
🔹
عملکرد ایران در جنگ‌های اخیر و مقابله با قدرت‌های بزرگ نظامی، نتیجه دکترین…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/437631" target="_blank">📅 11:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f142fb35.mp4?token=f0f4PNXCUPo7nOJgpkX-bsmJ6wKOHyhaZ4d0kCS0MvA1ui3kbnADEc8Ar-OPuTK7jkos2QNerQgyZfj6q0q4RRp0pW2Dx-oy7w8bF1TFK53-PynOOxelJJhgU4pznt_wZZtjx89ZR5AJ70dpgh33mT3O8mz4fwNAbBR8XmY2oA0sSrQK0Qk5L5WnVQsg2fH3-i4fnC1tG63FCUTi9HEBF1fhbKkpRGc_7JP8fdR4xw5GnkIZrdypUfs6o33B6hLlxT5fl57Z8A9ShmgOlYNBeFgfJ_sOfLqyTcBnhhuU54sXWHVbGSycytuGbNMAXGQXL9kdauK60dK5wvm34xNvHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f142fb35.mp4?token=f0f4PNXCUPo7nOJgpkX-bsmJ6wKOHyhaZ4d0kCS0MvA1ui3kbnADEc8Ar-OPuTK7jkos2QNerQgyZfj6q0q4RRp0pW2Dx-oy7w8bF1TFK53-PynOOxelJJhgU4pznt_wZZtjx89ZR5AJ70dpgh33mT3O8mz4fwNAbBR8XmY2oA0sSrQK0Qk5L5WnVQsg2fH3-i4fnC1tG63FCUTi9HEBF1fhbKkpRGc_7JP8fdR4xw5GnkIZrdypUfs6o33B6hLlxT5fl57Z8A9ShmgOlYNBeFgfJ_sOfLqyTcBnhhuU54sXWHVbGSycytuGbNMAXGQXL9kdauK60dK5wvm34xNvHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناهید کیانی طلا گرفت
🥇
ناهید کیانی در دیدار فینال تکواندو قهرمانی آسیا وزن -۵۷ کیلوگرم، با برتری ۲ بر صفر مقابل حریف ازبکستانی خود قهرمان شد  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/437630" target="_blank">📅 11:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255a86faa8.mp4?token=Ns2tqNTYT6wxLze2qHkE0hKd98Ib-eybgZ_F4Q3DjapTwoy_tWbZO1O8k_zHIRSbZJJD-cWTfAaJ6K0q-89EgOtH98fxRLLhFCnn9NwwS1BU5-UWo6zD5iGJEbCOSzxigvIcKj1c-yVmwKDh69rAlnJbPw5MU6YxRCazrM3ks4ln-N0v6yQSPPpIO0mFmkvKQ5dW87choxtTxGamJLOd5VL1dKlsD24j8nzxMr3zOnyEJpkuysGElcvjmqG7upeDyKcW-VJlPgfA_BMBAIeNFj2z7Jhe5X-q9xBw8ivCiLJf2r6d6clPKpmGpVAZTqpp0LuI8pFH0eN6QwRRD4hGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255a86faa8.mp4?token=Ns2tqNTYT6wxLze2qHkE0hKd98Ib-eybgZ_F4Q3DjapTwoy_tWbZO1O8k_zHIRSbZJJD-cWTfAaJ6K0q-89EgOtH98fxRLLhFCnn9NwwS1BU5-UWo6zD5iGJEbCOSzxigvIcKj1c-yVmwKDh69rAlnJbPw5MU6YxRCazrM3ks4ln-N0v6yQSPPpIO0mFmkvKQ5dW87choxtTxGamJLOd5VL1dKlsD24j8nzxMr3zOnyEJpkuysGElcvjmqG7upeDyKcW-VJlPgfA_BMBAIeNFj2z7Jhe5X-q9xBw8ivCiLJf2r6d6clPKpmGpVAZTqpp0LuI8pFH0eN6QwRRD4hGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناهید کیانی طلا گرفت
🥇
ناهید کیانی در دیدار فینال تکواندو قهرمانی آسیا وزن -۵۷ کیلوگرم، با برتری ۲ بر صفر مقابل حریف ازبکستانی خود قهرمان شد
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/437629" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugo0OuvFXI3FwEw8qulEei93_zFlvmluF9huWegmQOLvqU9lh0QyfwJVyOQEkS8ED8lbs1XDtQQeV_XkBUZOm6HvKbgOWqOtBGAVbWyyf5FFPfzkzivhZfaaKksmNBLf-7F8EgXL8shasmYeBEpOpABbfllLy4qXQ2ZKLB9WecHH6PDwQ0j70ZfsfZOUp3_PJ02CJLZL4_tYYyEk5dKET1N8mTV0qZBUvJrcHjPy7CATZvSrKFxa2HQ1Xm4wHnr1hNtGJEiolHeBhxINHkn1kuZuFVx2bkRZCtGewTBtcJTBFwtYGHFeImbjrQcz-6vf0Bz7rA4nIs-abvDppnnn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس‌جمهور: رهبر شهید انقلاب هیچ‌گاه با مذاکرۀ عزتمندانه مخالف نبودند
🔹
در مواردی، کلیپ‌هایی از بیانات رهبر شهید انقلاب دربارۀ مذاکره به‌گونه‌ای بازنشر می‌شود که گویا نظام به‌صورت مطلق مخالف هرگونه مذاکره بوده است.
🔹
در حالی که رهبر شهید هیچ‌گاه با مذاکره…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/437628" target="_blank">📅 11:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پزشکیان: دشمنان این سرزمین راهی جز شکست و خواری نخواهند داشت
🔹
کسانی که بی‌شرمانه چشم انتظارند آمریکا و رژیم صهیونیستی بتوانند به کشور ما آسیب بزنند و تجزیه و نابودی ایران را دنبال می‌کنند، باید در برابر وجدان ملت پاسخگو باشند. جنایت علیه مردم بی‌گناه و کشتار…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437627" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKsp-33YQZacTM6tuWPlWp0hXEdTWVnQGNVQR8kbQugllHSo2zVGXjNgQPlxbbj74WqCfgcbFAm2BWR-DHdU3SHEuNg-e0h31Gwo55CuX-U1jICfWHYaYM-LRlvUndnhbAMGHupS6OarX0xnc82Y7v9SB8_1PJzikXfg3x4rhMpKPCNMwy3YawNxRNbSOYbqmmWjLYQa5KPpylZpmPYPP9lHn1vG4ynjKWU1NWn3OSKh9q-iWSCR8SH8e7R7FU_oKWlxUbPlsUm3q1_8rx7-6aLscq-9Vja9k-3ETBvGDLlSRY5WN8SMmH2cht6fiffNEWqe26XYvEw7GQS0Wlcbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: از حضور و همراهی مردم قدردانی می‌کنم
🔹
از صمیم قلب از مردمی که با وجود همۀ گلایه‌ها، سختی‌ها و مشکلات، بیش از ۸۰ شب در صحنه حضور داشتند، قدردانی می‌کنم.
🔹
همچنین از همۀ نهادها و نیروهای امدادی، انتظامی، سپاه، بسیج، ارتش و مجموعه‌هایی که در این مدت…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437626" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcGY9MpvvkWUlafSLf6lCp4nVp2HNo2zb6gTKZUah7cvQ7TMrvsoI9jVDhe13ox1_hJGJ_R_97ofRI_0oxEWsVRVHpwIpU2fsLHi3ryKdBYzK-a09goby5BEGB6v0MTJIXWIURBGVd-tQsjwzQqTjmh2nXCQ5lxuXtDp_9bJHwJ2-uXY3F_IIf-AorzHaF1wYHMlgWe0zRqs7v1nflZTgSJ9CsPjHoIrDtlrAt6bZMRlKk54QaCWJLE3uHOAre_sYNyJzisG7tPC507qrLnccmIPYFTStkBDpeW8lrXw4R7hJHMRBG7SgzAzquWvyVR-U4CdOFCy9QKfErVDGx-WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: نسبت به مشکلات مردم احساس مسئولیت جدی دارم
🔹
بنده نسبت به مشکلات اقتصادی و معیشتی مردم، به‌ویژه آسیب‌هایی که در پی شرایط جنگی تشدید شده، احساس مسئولیت جدی دارم و با تمام توان در حال تلاش برای کاهش فشارها بر مردم هستم.
🔹
باید شرایطی فراهم شود که فشارهای…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/437625" target="_blank">📅 10:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvN_gGMD--yhAAwsrFEENA24goJY4hg5R3c55VKqkNMYEzAEAT99ezRpzajtq6VB_O_CCzU7X4TJZesfGDPZB9526Iaad_SD7bEeYe78KhcdyybsgGwZI6O8tILAzI6RQJ5ovMAdFtT_LShimrWygLQAfeZMyc_CkkOMNj9SXx2RNntoYco7XZnOnLoU8__8kf1EV1ZSzLnr23J90uYMUOGyb9fI3fszoSn-D4_rKrjrw5N7TUTYuozJ7rB25GpuxJFM6QB0x5rdK2gL918VOj1uRnSU7IeDLaExZx7gTDv_oKfjvKpmQCD_WIWtFizIVM1X-8FmFBC4-REan9Qkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور: دلسوزان کشور به‌جای نقد وارد میدان شوند
🔹
همۀ دلسوزان کشور به‌جای ایستادن در حاشیه و صرفاً نقد کردن، وارد میدان عمل شوند و در حل مسائل کشور مشارکت کنند
🔹
امروز بیش از هر زمان دیگری به هم‌افزایی، همراهی و همکاری ملی نیاز داریم و همه باید دست‌به‌دست…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/437624" target="_blank">📅 10:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437623">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSnxHxw8S4Ti2ocUsDLj9UDXOt6BbpdVIUq9aZe7cLaXxUYR3RpFOHj42RTldTBGqbj0KNPziSAvk6cHOCApm8fCZva3b5GW57fzxxtMRFzwjQ5bLiK7S9EsBVnTwmXN4fzpKM1LSpTOKWh28Cu_hAblW3j_yMYKFwhM4yQ0fAqc4wQD0y-E816w5EbfNsybqA0KcghoBSuGvquOvgDpazxUB8TjQHl5gbAoyS3PDPOCOKkRWYMWuWhNTmIMv-xnP0F5cGUVYvIgBFcPyZHhi43S4gTXQzBOpZ8yfudHncj86h5d76Qp-wNv6rY-OhEWlek_7op48VZS15U2Ry1n8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هیچ تصمیمی بدون اذن رهبری گرفته نخواهد شد
🔹
رئیس‌جمهور در نشست با مدیران سازمان صداوسیما: هیچ تصمیمی خارج از چارچوب شورای‌عالی امنیت ملی و بدون هماهنگی و اذن مقام معظم رهبری اتخاذ نخواهد شد.
🔹
هنگامی که تصمیمی در حوزۀ دیپلماسی اتخاذ می‌شود، همۀ دستگاه‌ها،…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437623" target="_blank">📅 10:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c28vTsQz7aTs7kzWD_MGcYutS2lBjcwgMENV18a--q5AOJBQMNigagegjzaJ-zD5NodzvEWrUsMSY9YQgnzzbWoNeMkH7W06AuWr2iSk9IiTxSKeCOzAPG7r7SqJ0zdl8kZi30SpWF23L_AOUoBLt89hbNhfZRID575iX26LbiYFjdU9ULBonlCMeu9YBO3P_5kqeLdKvZh1JbFUzuAkBR3o-l8SbP3Ou0BilRhXGwzL1pfksLIofzhBN3zatZaM2dJzNstmquQL3Vbqz4uuK332ftJPRU3iGwiFoIWSKAFTykjErnB0OYX_iANeYW1LmXOlipfIRrOZHaWVt8JZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هیچ تصمیمی بدون اذن رهبری گرفته نخواهد شد
🔹
رئیس‌جمهور در نشست با مدیران سازمان صداوسیما: هیچ تصمیمی خارج از چارچوب شورای‌عالی امنیت ملی و بدون هماهنگی و اذن مقام معظم رهبری اتخاذ نخواهد شد.
🔹
هنگامی که تصمیمی در حوزۀ دیپلماسی اتخاذ می‌شود، همۀ دستگاه‌ها، تریبون‌ها و جریان‌ها باید از آن حمایت کنند تا صدایی واحد و منسجم از ایران به جهان مخابره شود.
🔹
امروز صداوسیما باید منادی وحدت و انسجام ملی باشد. اگر همه باهم، در چارچوب منویات رهبر معظم انقلاب حرکت کنیم و انسجام ملی را حفظ نماییم، دشمنان هرگز به اهداف خود علیه کشور دست نخواهند یافت.
🔹
نمی‌توان هر فرد یا جریانی صرفاً بر مبنای سلیقۀ شخصی خود، نسخه‌ای متفاوت برای کشور ارائه دهد؛ چراکه ادارۀ کشور مستلزم تصمیم واحد و تبعیت جمعی است.
🔹
حل بسیاری از مسائل کشور بدون حضور و مشارکت مردم امکان‌پذیر نیست. این امر مستلزم آن است که با سعه‌صدر و نگاه باز، همه اقشار جامعه دیده شوند.
🔹
اگر بتوانیم مساجد را به جایگاه واقعی و تاریخی خود بازگردانیم و به پایگاه حل مسائل اجتماعی و مردمی تبدیل کنیم، بسیاری از مشکلات کشور با اتکای به ظرفیت مردم قابل حل خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/437622" target="_blank">📅 10:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ «مستثنی شدن» رژیم صهیونیستی در توافق با ایران صحت ندارد
🔹
روزنامۀ نیویورک تایمز مدعی شده که ترامپ رژیم اسرائیل را از تعهدات توافق با ایران «مستثنی» کرده است.
🔹
این درحالی است که بررسی متن نهایی‌شده توافق احتمالی نشان می‌دهد که این ادعا فاقد وجاهت است. براساس…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437621" target="_blank">📅 10:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437620">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a569e2ef.mp4?token=D89sZGdsgA5eWExt9c-Jlfxo6aj8DcLx2hVAbLx1HOMkFDOYFieBy40sbwhC9HgSg28IfD4wBVzrMUQJoIy99QDkztQ9Vi_QoZpv6ZHqUfbDHMRV_Zn4GbYO76bSU5f8vU0-aBlbdqZuZhm5rpYXgyLsiB-omm_Rcl_gDAXLKmhasqGqtA3GWqBCN0oZfIOTCZSol3p8L-PE6ehOkyXeeALuGHrpcxLwuh9G8FmvYAHg-R9z1NKbcXRiYftR6DoU9WhbWi-IcHPCnuNZxR8MDCo_--cQsyDY1Y_upvsSE-Mmd1zkWcIPPR8e-krqQ04Fwd_1XV9QD5_9UDg07-Zw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a569e2ef.mp4?token=D89sZGdsgA5eWExt9c-Jlfxo6aj8DcLx2hVAbLx1HOMkFDOYFieBy40sbwhC9HgSg28IfD4wBVzrMUQJoIy99QDkztQ9Vi_QoZpv6ZHqUfbDHMRV_Zn4GbYO76bSU5f8vU0-aBlbdqZuZhm5rpYXgyLsiB-omm_Rcl_gDAXLKmhasqGqtA3GWqBCN0oZfIOTCZSol3p8L-PE6ehOkyXeeALuGHrpcxLwuh9G8FmvYAHg-R9z1NKbcXRiYftR6DoU9WhbWi-IcHPCnuNZxR8MDCo_--cQsyDY1Y_upvsSE-Mmd1zkWcIPPR8e-krqQ04Fwd_1XV9QD5_9UDg07-Zw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله انتحاری به قطار پاکستانی
🔹
پلیس پاکستان اعلام کرد که پس‌از انفجار ناشی از حملهٔ انتحاری با خودرو به یک خط راه‌آهن در کویته، حداقل ۲۰ نفر زخمی شدند.
🔹
برخی رسانه‌های محلی، این حمله را به «تروریست‌های مرتبط با هند» نسبت دادند و گزارش کردند که آن‌ها «با…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/437620" target="_blank">📅 10:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
قالیباف: مجاهدان رشیدی چون شهید احمد کاظمی و شهید علی صیاد شیرازی که غیرممکن‌ها را ممکن کردند و به ما آموختند که هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان را…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437619" target="_blank">📅 10:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437618">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🖼
قالیباف: هیچ دژخیمی را یارای ایستادن مقابل سربازان مؤمن ایران نیست
🔹
رئیس‌مجلس در پیامی به‌مناسبت سالروز آزادسازی خرمشهر: هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/437618" target="_blank">📅 10:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD2SfGkxUoegvPndhv-iSyKW92Flm0T__72kCB4YrOPMEYWN9ZA1yW_m4unv3S00pDvvbBtPxKMs1BUeh9480vV20zdkJA1kREtE-EpjLuAstmNCnoNu1lWpr9Jv2cVbXrID_vj5cHyBF8H2NicxuRoW71nzozr5C6dOReU2xhAQy4MoWL9my96BHvqsUunuqqwdJ5gzEPKSc94nEa9EU0dffQ_VRclZtKUUACxn8LDFk8oylrLE0fbZw5RhiHYXRIPo4eZYuz1PkDXtOUvaO6szSejvbWguZZIZDbaGW2sr5_zC1D8qB9rvniQQRPy0hc6Puy4kGf9GUkJxcBV-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: هیچ دژخیمی را یارای ایستادن مقابل سربازان مؤمن ایران نیست
🔹
رئیس‌مجلس در پیامی به‌مناسبت سالروز آزادسازی خرمشهر: هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان را بر شانه خواهد داشت و انسداد را نخواهد پذیرفت.
🔹
به‌طور قطع سوم خرداد آغازی بر دلاوری‌های بی‌بدیل رزمندگان ایرانی است، رزمندگانی که به فرمودۀ قائد امت، حضرت آیت‌الله العظمی شهید سیدعلی حسینی خامنه‌ای خرمشهرها در پیش دارند و خداوند متعال، راه شکست را بر آنان بسته است.
🔹
رزمندگانی که به دنیا آموختند افتخار و عزت نصیب ملتی می‌شود که ایمان، اراده، غیرت و شجاعت را در کنار تخصص و تلاش داشته باشد و چنین ملتی هیچ‌گاه طعم تلخ شکست را نخواهد چشید.
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/437617" target="_blank">📅 10:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff508d240.mp4?token=XEV-w5vAomaO5oKFNOo09ecyvxe0kwPCIensn6oa3BmKhDatBvvVxL2PGeD0Kb3-iQwm_TbZd9VPRO8PfTG3ug_jHUALyI_zo4fyyTEEOYRphIOOZr-fft_VNBmR96gZDoWNii8zfG5PDHTiDjqKhTYnvNOKj0bRQuzeNuSc2d5MTTnXK7DeJZVgYirMkyMFmi87Wb1HRS3nr7z-3-mIWmHdlgrrMoY5csgbP-6Y7q2Z7mJgLwEUmYQz-aTQBlKO8kUK-L1dOglLk6w6J3J6ODP4hr9Sj4NeBOu_OlTO8jzMe7bcrV6PLsegD56lhDfxPHCX8SxF7ku_JKkgnHG2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff508d240.mp4?token=XEV-w5vAomaO5oKFNOo09ecyvxe0kwPCIensn6oa3BmKhDatBvvVxL2PGeD0Kb3-iQwm_TbZd9VPRO8PfTG3ug_jHUALyI_zo4fyyTEEOYRphIOOZr-fft_VNBmR96gZDoWNii8zfG5PDHTiDjqKhTYnvNOKj0bRQuzeNuSc2d5MTTnXK7DeJZVgYirMkyMFmi87Wb1HRS3nr7z-3-mIWmHdlgrrMoY5csgbP-6Y7q2Z7mJgLwEUmYQz-aTQBlKO8kUK-L1dOglLk6w6J3J6ODP4hr9Sj4NeBOu_OlTO8jzMe7bcrV6PLsegD56lhDfxPHCX8SxF7ku_JKkgnHG2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله انتحاری به قطار پاکستانی
🔹
پلیس پاکستان اعلام کرد که پس‌از انفجار ناشی از حملهٔ انتحاری با خودرو به یک خط راه‌آهن در کویته، حداقل ۲۰ نفر زخمی شدند.
🔹
برخی رسانه‌های محلی، این حمله را به «تروریست‌های مرتبط با هند» نسبت دادند و گزارش کردند که آن‌ها «با هدف‌قراردادن غیرنظامیان بی‌گناه در کویته از طریق یک حملهٔ انتحاری با خودرو به یک قطار مسافربری، وحشی‌گری خود را به‌نمایش گذاشتند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437615" target="_blank">📅 10:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔹
علی نیکزاد، نماینده اردبیل
🔹
عبدالرضا مصری، نماینده کرمانشاه
🔹
حسینعلی حاجی‌دلیگانی، نماینده شاهین‌شهر
🔹
حمیدرضا حاجی‌بابایی، نماینده همدان
🔹
رضا جباری، نماینده مسجدسلیمان
🔹
علیرضا منادی، نماینده تبریز
🔹
پیمان فلسفی، نماینده…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/437614" target="_blank">📅 09:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ ‌ادعای ترامپ دربارهٔ بازگشت تنگهٔ هرمز به حالت قبل واقعیت ندارد
🔹
به‌گزارش فارس؛ برخلاف ادعای لحظات قبل دونالد ترامپ در شبکهٔ اجتماعی «تروث سوشال» مبنی بر بازگشت تنگهٔ هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/437613" target="_blank">📅 09:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWVRzPREOzQyNPBnODDS9xBJH3Xhz5mZmZVLaCOfjD7op-C0fE6Bk68kDLZStliLg3jHphdw3iendZBOKDOVsy4xj2_J-J_H7aAI2NwD8xbPrBL6-AodTOTf9pNOTbfpBX2fOJaUSCSIVzpL2oUYzTHr2K-jN2v6juSZf9Ri9ZdyMBbRmXmB_pKN_4oWh2v6GwGI_H28ueCwjID6BZ0sQco4No6yiFm2NR3zrQGImvJsD-BtigZUgOn2fh8aMzEpKxuUSORppJYHi9dpAFB_wUuu6BQT7KKr00wW3yXV1pneSQ_K9ajhBUKvKkwj3NgG_LFKma0dWFCZ5OB820TK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مشاور رهبر انقلاب به‌مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/437612" target="_blank">📅 09:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIZGMvnF4jQV1xoDszGNntuFMUJQSlhpckJ7_vltCf03BUIEjUqbl0qGkrcKt5R-z-WjKZUjryGzwQbR79hxYiOcbyb_gkUkQQ0jcFy-hCj0w6DhQofmP2i_v_4yiejdXNcbAYrXmayIy3vZnulJQija8FY4KpSOjysbpWIrylcxLsK7HWvy-KMukqAb10bOMoAz_A-_JYaIuMO2lEuFxeeZyRro_ntsd2Clf0ELWkVNsWJzoZOShAT7YqR6Z_6ObE_7PySZA-HvJ1ksjVtCqNvrBd0JjY6iodXKfEVZUFfyDbaH57s9uYo-nAZ5b2OO5ObmO25o21jF8FPgzZ_R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فرمانده کل سپاه به‌مناسبت سوم خرداد
🔹
سوم خرداد، روز ملی مقاومت، ایثار و پیروزی، یادآور حماسه ماندگار آزادسازی خرمشهر پس از ۵۷۸ روز اشغال است؛ روزی که فرزندان غیور و غیرتمند این مرزوبوم با ندای «ما می‌توانیم» خرمشهر را از لوث وجود پلید ارتش بعثی صدام پاکسازی و کلام امام کبیر انقلاب حضرت روح الله(ره) مبنی بر اینکه «خرمشهر را خدا آزاد کرد»، طنین افکن و اراده الهی، وحدت و اقتدار ملی برابر استکبار جهانی در یک رخداد شگفت انگیز به منصه ظهور رسید.
🔹
امروز نیز ملت مبعوث شده ایران با گذشت ۴۴ سال از حماسه تاریخی آزادسازی خرمشهر و پیروزی در عملیات بیت المقدس، در سومین جنگ تحمیلی – که با حمله تروریستی دشمن صهیونی‑آمریکایی و شهادت مظلومانه قائد عظیم‌الشأن انقلاب و جمعی از فرماندهان نیروهای مسلح و دانش‌آموزان میناب رقم خورد – بار دیگر سربلند بیرون آمده است، و دشمن زبون پس از ۴۰ روز مقاومت  کوبنده و پاسخ قاطعانه و ویرانگر نیروهای مسلح، با ذلت درخواست آتش‌بس کرد و اینک نظاره‌گر خروش ایرانیان در خونخواهی رهبر شهید انقلاب اسلامی است.
🔹
فرماندهی کل سپاه پاسداران انقلاب اسلامی، ضمن گرامیداشت یاد امام راحل (ره)، امام شهید آیت‌الله خامنه‌ای (قدس سره)، و شهیدان گرانقدر دفاع مقدس و شهدای اقتدار ایران اسلامی و جنگ تحمیلی رمضان، و تبریک این روز خجسته به محضر مقام معظم رهبری و فرماندهی کل قوا حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای (مدظله‌العالی) و آحاد ملت شریف، قهرمان و انقلابی ایران، نکات راهبردی زیر را اعلام می‌دارد:
🔹
۱: جنگ تحمیلی سوم، جنگی ترکیبی بود اما پاسخ قاطع، کوبنده و درس آموز سپاه مقتدر مردمی و نیروهای مسلح به پشتوانه حضور حماسی مردم در صحنه، دشمن را در دسترسی به اهداف ناکام و آمال و آرزوهای او را بر باد داد و ترفندهای  اهریمنیش را خنثی کرد.
🔹
۲: عبرت خرمشهر، اتکا به قدرت درون و بازدارندگی فعال است. پیشرفت‌های هسته‌ای، موشکی، دفاعی و تهاجمی ایران، دشمنان انقلاب و میهن اسلامی را را به محاسبه مجدد واداشته است.
🔹
۳: بزرگترین سرمایه راهبردی کشور، حضور مصمم و پرشور مردم در همه صحنه‌ها است که سدی محکم و خلل ناپذیر در برابر نفوذ و توطئه دشمن است.
🔹
۴: نیروهای مسلح مقتدر کشور در بالاترین سطح آمادگی و بازدارندگی فعال در همه ابعاد "موشکی، هوایی، دریایی، زمینی، فضایی و سایبری" قرار دارند؛ بر این اساس بدیهی است هرگونه تعرض مجدد دشمن، پاسخی ویرانگر و جهنمی در ابعاد منطقه‌ای و فرامنطقه‌ای در پی خواهد داشت.
🔹
۵: فتح خرمشهر، الگویی ماندگار برای پیروزی در خرمشهرهای پیش رو و آزادی قدس شریف و نابودی رژیم پلید صهیونیستی توسط محور مقاومت و مجاهدان جهان اسلام است.
🔹
در پایان، با تجدید میثاق با آرمان‌های بلند امامین انقلاب و شهدای گرانقدر انقلاب اسلامی و دفاع مقدس اول، دوم و سوم  و اعلام بیعت مجدد و اطاعت از منویات و فرامین رهبر معظم انقلاب و فرماندهی کل قوا، تاکید می‌کنیم:
🔹
بی‌تردید ملت بزرگ و فهیم ایران در فضای مذاکره برای پایان جنگ، با حفظ و تعمیق وحدت و بصیرت، و رصد مواضع و رفتارهای دشمن حیله‌گر و عهد شکن نقشه‌های او را خنثی و نقش بر آب خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/437611" target="_blank">📅 08:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDVpIKqjLgUqEGBDDIgCLbXsmAZVPB0xghjJtUbcTD78N2sqaXcYO1BnGcbQBqkCM6B6atc3ejWRY8iMqRUDQwEJBDuqsSM-c29IjcuBhgMzlnC5xfiwJcv3m538jDW9Kn6vyIRTOkN9TXSEvgwsca1LME8zCm1UNOf85ZaWaBaj4pLffSyh_NdGUBmEx7SDV_r2hoIedA309Ln0qBScl-o0NhcQTZkyu7GLvXNAoSKurdiPpIAA27t4A_KKOdVZls_dcrV_dGCevzQBCEbT-6wEXvXZ0XblrZboX6T6HBQIf7PSXgjkptwxVrIVwebntpk0w5fPQokFeGwSfHW2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن اعدام شد
🔹
مجتبی کیان فرزند محمدقلی، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز،  بامداد امروز اعدام شد.
🔹
نامبرده در طول جنگ رمضان پیام‌های متعددی را به شبکه‌های معاند وابسته به دشمن صهیونیستی‌آمریکایی ارسال می‌کرد که از جملۀ آن‌ها، مختصات و اطلاعات محل واحدهای تولید قطعات مرتبط با صنایع دفاعی کشور بود.
🔹
محکوم‌علیه در شرایط جنگی، در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده».
🔹
مجتبی کیان در اعترافات خود عنوان داشته: «پس از ارسال پیام به شبکه ماهواره‌ای، شماره‌ای را به من معرفی کردند تا اطلاعات را ارسال کنم و من نیز اطلاعات را از آن طریق ارسال کردم.»
🔹
بررسی فنی پیام‌های رد و بدل‌شده میان محکوم‌علیه و عناصر دشمن نشان می‌دهد ۳ روز پس از ارسال اطلاعات، محل مورد اشاره هدف حمله دشمن قرار گرفته و به‌صورت کامل تخریب شده است.
🔹
پس از ارتباط‌گیری مجتبی کیان با شبکه رسانه‌ای معاند، نامبرده بلافاصله شناسایی و دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/437610" target="_blank">📅 08:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwILAKum3DyD7vRpkKmLWmNZOffkz8v0e4xxd1X606yZxUFmNB2zb3OqWbbXuKW4KbCUThPxQVX-qS5Cqi0A80BR9LLlRS5ocR7ohNgL2efIyc8HcOJ0mkSRUjwaDFBzu1f8ufgyP-dNfRBGmod11eegitT47v1niF__FjKLEMF-2tQBJwpNjwtTlvYsRF-Vd7lBSGKvao9bvf-tWX-PZFJKIFiwDYNWAy4uAF0ofd1DjKwTH4jbSoKh2st8tfd1ydYtiXXmdHATq5io0a23X9GxY4pN6aRuBmbhKYrSK3WAcS8Ro3pBXujBFCViR4MeofP_y53SH8DtLMHPeTHSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: خرمشهر امروز ایران، خلیج‌فارس و تنگۀ هرمز است
🔹
ملت ما امروز هم‌چنان مردم رزم ندیده اما دلیر خرمشهرند که روزها در مقابل ارتش متجاوز ایستادند تا قدرت مردم ایران را به رخ جهانیان بکشند.
🔹
مقاومت، ایثار و دفع تجاوز، ریشه در فرهنگ این سرزمین دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/437609" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nshl3T-vkhlCZyMbugCGc1UNS2GMgdpGYkNim-3U6rNADKKInhC79aqentLnI-WOllz4sBJ6EFIWguucqGqeIGmpS1CstPoOGKTdGWmcOP0VBWCePYjrQ0BMJCxxDOGEhomOLwTZM0w6uQdccHeRn_J-VxP8MgExBabUDb3vW55E7_8aTEu79NnpUU-xyCy2qX02e4mnhudaI79fy5232poZ8w-MoCTcQiy_AtVA1tigs6f3OeSYoRACsNfY7mF7TvKyKG19jH0rsWyvgY6vtQRBVb3WF4NlF3toPZWzKJXGLM-8GhHXLymDvIAcy4rst3PwmFGTHNnmb6kvV-gbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با همان ایستادگی حماسۀ خرمشهر، دربرابر دشمنان پیروز می‌شویم
🔹
معاون اول رئیس‌جمهور: حماسۀ آزادی خرمشهر آموخت با مقاومت و اتکا به توان داخلی می‌توان از بحران‌ها عبور کرد.
🔹
امروز نیز در میدان دیپلماسی، دفاع و سازندگی، با همان ایستادگی مقتدرانه و تبعیت از فرامین رهبری دشمنان را به تسلیم در برابر ارادۀ ملت وادار کرده، تحریم‌ها را شکسته و بر دشمنان وحشی خود پیروز می‌شویم.
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/437608" target="_blank">📅 07:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-TH1GTrzRT1XmNHJcR5nGUJm5-CPC8KMhGnSWIZyz2F3E_Jl1UVAYH1N0Ol9UUGZqQy3VI_GkwTe-OWjy6LFXCgE4gdYaJ3nnB6gRSQwjfNq2CWGyPlYWhkcC_r61krHGp6M79OuPYFRFg09ARnlr5fnfrKNja5Oc5nnkLNoXphwerkf1ZWVkVcpj_9jiKnGon9_y8l98pdmajotMST5oNvTDXCYFPvJUqJvX9SZyj63cShMePTk745wAdgkQ755rqGcl00Qxq6qpxadLXhGyKvfFl0qlMdM5H1cguqBpxu2JXqBK37YmvELwpv3tfkqX_KO74YRrbjilXoiiSpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔸
خبرگزاری AP این اقدام ایران را دور زدن مشکلات عدم صدور آمریکا توصیف کرد و نوشت: ایران با انتقال کمپ خود به مکزیک مشکلات عدم صدور ویزا و تعلل دولت آمریکا ٢٠ روز به آغاز جام‌جهانی را خنثی کرد تا راهی مکزیک شود و تنها در بازی‌ها در آمریکا باشد.
🔸
نیویورک تایمز نوشت: ایران با موافقت فیفا کمپ خود را از آمریکا به مکزیک منتقل کرد تا با کمترین مشکل تمریناتش را انجام دهند و در آخرین روزها با دریافت ویزا در جام جهانی شرکت کند.
🔸
شبکۀ تی‌آر‌تی ترکیه این اقدام فدراسیون ایران را نوعی ترفند برای به حداقل رساندن کارشکنی آمریکا در زمینۀ عدم صدور ویزا توصیف کرد و نوشت: ایران با انتقال کمپ خود با مکزیک مشکلات عدم صدور ویزا و بلاتکلیفی را حل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/437607" target="_blank">📅 07:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7LWloLk1wIOAFRlP0Qz69_10jSK9yJ-1_BSH5nBweJbo67Q7MbYv51xrkBqj8EH8S5wajjJWBOKYgftIkRzyQBq8kpsrmfqFfxilxFyLGV1QJjyLGCI1NfBNg2NruBszKvZ4VRXFgVnB5BoYcaMgDmy4y4niwjyL3AWEWX3KzhvxPrz5r0RguXXQpTuhvCR7HbtYtiLZjDzCOTrEEZznQYLnzP6iz7iAkqYSJqpXvv6tfGQvsRanrHO-b-01h38BAlaqlpg-6YUfrhzcEgUF9GAWImAhS1Tk8ui059VNhQBlG9HWbpO-qadm6zR-iUuJodUIJ3PgSV29YPUkpKnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ تازۀ واشنگتن برای خلع سلاح لایه‌به‌لایۀ لبنان
🔹
لبنان این روزها در کانون یک بازی پیچیدۀ قدرت قرار دارد؛ بازی‌ای که آمریکا با سلاح تحریم آن را بازطراحی می‌کند. از افسران ارتش تا معاونان ارشد نبیه‌بری، همه در تیررس واشنگتن هستند.
🔹
اما هدف نهایی از این پروژۀ امنیتی-سیاسی تازۀ واشنگتن چیست؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/437606" target="_blank">📅 07:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df3wc9mAKBbvm10lWYtFogLpjtknDNAgzhcAcZXAqxeXx1zjh6s_l_w4N7OsYvnu5dChtIuT6ymotgqLYtjBbosXxUl3Kb0-67YJ7f2V-C90Iz6t9ZPXEFuOO6ktFzsWNE_TodR-Lmk9hoCDw-_pR3jGv5JToJo3Ajl00uSoSGPLoNz7atYs4M9cebAT37bIBhyl6Mk6Qr7jr_0xvFv0UgJgZG98zcUzX-eSRltbPgDxNicCdzTvAPi38QYQVgDIlTyGqRh8AtWDk5GlAjWQHNbysjRZfsEz5pUJUuk1qL7aczDJ7ft0mzaQZUH_h9UV7JLPyX-pPBA0z6B5phXTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: ایران منطق صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از استقلال کشور را دنبال می‌کند
🔹
غریب‌آبادی: ‏۳ خرداد، سالروز آزادسازی خرمشهر، یادآور حقیقتی ماندگار در تاریخ ایران است؛ حقیقتی که با اصول بنیادین منشور ملل متحد نیز پیوند دارد: ملتی که قربانی تجاوز و اشغال شود، از حق ذاتی دفاع مشروع برای صیانت از سرزمین، استقلال و کرامت خود برخوردار است.
🔹
خرمشهر نماد پیروزی ارادۀ ملی بر تجاوزی بود که با محاسبات قدرت‌های حامی متجاوز آغاز شد، اما در برابر ایمان، ایستادگی و خوداتکایی ملت بزرگ ایران شکست خورد.
🔹
امروز نیز ایران همان منطق را دنبال می‌کند: صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از تمامیت ارضی، استقلال و حقوق مردم و کشور عزیزمان ایران.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/437605" target="_blank">📅 06:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdRHQinkD8hsarjqdpH0HcoBN7_suSAVXv9Lc2nSXVMDJDikXw80BfO_yuL8NA8SopFWaCbSYwnomsPCA1o0csCH22hErQ_-uF_vM-HCupPxlUIgyLEVJb4mdV9dUmjC3CtUdo4792ivqjAJhrFtDbVd90YrM1zTFPgSy9Sc9HcsLAUolSApp9-i_phSgVfy8FlzLDJellzwlLqxtn0ptMKgFiOHafZdqSlA4Lz7fjDUYeDZP8Sf1d1TfJalEHMJBzBGQ0JalQWEQHBFvDRhRIu_2725Z7sI7jWpOHc1Kw3JehE4hVtHouh1ytQMBY0sFE3EF3kw-xng9174-TaR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم بیمۀ کارفرمایان، و محل حقوق بازنشستگان تغییر می‌کند؟
🔹
وزارت اقتصاد و وزارت کار به دنبال تصویب لایحه‌ای در دولت با عنوان «لایحۀ ایجاد نظام جدید تامین‌اجتماعی» هستند که بر اساس آن حق بیمۀ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد.
🔹
طبق این لایحه سهم حق بیمۀ‌پرداختی کارفرما و بیمه شده برابر و در مجموع ۱۴ درصد خواهد بود و ۱۶ درصد مابقی از محل درآمدهای مالیاتی تامین خواهد شد.
🔹
همچنین کلیۀ منابع حاصل در خزانه‌داری کل کشور جمع شده و حقوق بازنشستگان از خزانه‌داری پرداخت خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/437604" target="_blank">📅 06:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx5kzuOZ0uH86ONTkwgD7ynyz29boOHOV0J2NCVOAUOzziWX0U8y7f25cPsdiW_RpYvUHdtWaK4dVtsmuenJnCmPb-Bsmz2pt8svULpIqq2sAgWuZ4I-l7mbCoZ9JU0v3XwSys0cHPi65-yTuIOfIAz2KxFDJpd2XALTSVRNOSe9kcUqFaaaQPKx2Pra1rAD2bOZOnabGDWZPtxnKAc3KCC1cFNNPFmyJZ7BskOK8bVzcKWSfSbTASRrH1LTDtBOz9q7o3I8SVwHrCubZUEs-FO1JUG9vL1xdD2q9ocD2S0wor6J1vYUBRNQvqi2Gimx53zl3r7OD4wMTKQMGsAKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/437603" target="_blank">📅 06:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه با موشک‌های اورشنیک انتقام کشتار دانشجویان را گرفت
🔹
ارتش روسیه بامداد امروز یکشنبه، حمله‌ای گسترده با موشک و پهپاد به کی‌یف پایتخت اوکراین و مناطق اطراف آن انجام داد.
🔹
نیروی هوایی اوکراین نیز اعلام کرد که حمله ترکیبی شامل موشک‌های بالستیک و پهپاد بوده و برخی از پرتابه‌ها توسط پدافند هوایی رهگیری شده‌اند. منابع اوکراینی از استفاده روسیه از موشک «اورشنیک» (موشک بالستیک میان‌برد جدید) در این عملیات خبر داده‌اند.
🔹
این حمله گسترده موشکی و پهپادی پس از آن انجام می‌شود که وزارت شرایط اضطراری روسیه شامگاه شنبه اعلام کرد شمار قربانیان حمله اوکراین به خوابگاه دانشجویی شهر استاروبیلسک در اقلیم خودمختار لوهانسک به ۲۱ کشته افزایش یافته است.
🔹
ولادیمیر پوتین رئیس‌جمهور روسیه نیز روز جمعه اعلام کرده بود که به وزارت دفاع این کشور دستور داده است تا پاسخ این حمله را بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437599" target="_blank">📅 06:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKLPSoZGt6Xxvlpb-pJ9oa-v2Fp_oYSMehdwCodeA8aDgPTG0ueNkBmcgVmoevJsDil_bWSNA6tlZiwUCCIkT0oY3BUBdc3sJjqgB9rxMLlUEZW6j7Y-0xPrc0XdwYIKHk5_h2vJ2HmSsVK5SytPRnZfU0vtrHhPU1drxUC6s45GooKCuoij_428X-hLQrk5uLHBhlCSJ35iN13bM2AOdpdkxfAYFmzQ2jNWF76fVGEsNPvmq26Ayq7o06zstflgfhVSScat0yEiqneo1iDlayjA9wyBP4B0ennPaUv8QMrMufof2m46qkERJzFphU6Z89ZMZQhLXACJi30aioPn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضۀ جدید شاهین در میان معوقات ۴ ساله
🔹
سایپا در حالی دور جدید عرضۀ شاهین را آغاز می‌کند که هزاران متقاضی این خودرو، از چهار سال پیش تاکنون در صف خرید هستند.
🔹
معاون فروش سایپا دی‌ماه سال گذشته گفته بود، از مجموع ۴۴۰ هزار دستگاه شاهین تعهدشده طی سال‌های ۱۴۰۱ و ۱۴۰۲، ۴۲ هزار دستگاه باقی مانده که ۱۲ هزار آن «معوق» است و تمامی این معوقات تا پایان شهریور ۱۴۰۵ تحویل می‌شود.
🔹
با این وجود، حتی در صورت تحقق کامل این وعده و تحویل خودروهای معوق، همچنان ۳۰ هزار دستگاه شاهین از تعهدات باقی می‌ماند که متقاضیان آن همچنان در صف انتظار تحویل قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/437594" target="_blank">📅 05:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2hxH46AiOyAN2HwmJ0deMT5C6TJZO1RFehE0dz4ilh-svnZAAnH5QdupNk19mVBl24hpkxd3ucsuNhxVvdE6tsFaCppKD-J4y1jQViaGukoMqSrNZ4-DXmhYjkQ9ZRc-LxiAZeGw-IOvYHBkCFF_-2Q2jaBDzJlY7YXeo-vRkyADgI7XtYnkL7EyXsRRW9FMeHC0f3SZnCSiPqOvR4FhG4iCED1mPzGbkRBJFXcWEoX6q_s1x8miNYeg4aFgsV5E_JC6Fm_CdgJrTI-4tiR3WlH-gTPn-_O_HhxteASx8yDotccuMVWEKaN7jO2xpzt2lXlBgTVhTlsQZv1-oy2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاس اولی‌ها تا ۱۰ تیر برای پیش‌ثبت‌نام فرصت دارند
🔹
آموزش‌وپرورش تهران: پیش‌ثبت‌نام دانش‌آموزان ورودی پایۀ اول ابتدایی برای سال تحصیلی جدید آغاز شده و تا ۱۰ تیرماه ادامه خواهد داشت.
🔹
پیش ثبت‌نام از سامانۀ
my.medu.ir
انجام می‌شود.
🔸
اما شروط و مدارک لازم برای پیش‌ ثبت‌نام کلاس اولی‌ها چیست؟
اینجا بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/437593" target="_blank">📅 04:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">عضو یک حزب اصلاح‌طلب پس‌از استعفا: تحلیل‌های ما درباره آینده جمهوری اسلامی غلط بود
🔹
علیرضا اسکندری‌نژاد، دبیر استان تهران حزب اصلاح طلب «اراده ملت ایران»، با انتشار نامه‌ای خطاب به احمد حکیمی‌پور، دبیرکل این حزب، از تمامی مسئولیت‌های حزبی و عضویت خود در حزب اتحاد ملت استعفا کرد.
🔹
اسکندری‌نژاد در این نامه با اشاره به تحولات سیاسی و امنیتی ماه‌های اخیر، اعلام کرد که دیدگاه‌هایش نسبت به جریان اصلاح‌طلبی تغییر کرده و دیگر خود را در چارچوب این جریان تعریف نمی‌کند.
🔹
وی در بخش دیگری از این نامه تاکید کرده که برخی تحلیل‌ها و پیش‌بینی‌های رایج در میان فعالان اصلاح‌طلب درباره آینده سیاسی و امنیتی کشور، در جریان جنگ اخیر محقق نشده است.
🔹
این فعال سیاسی ادامه داده که برخلاف تصورات پیشین، ساختار سیاسی و نظامی جمهوری اسلامی در مواجهه با بحران‌ها دچار فروپاشی نشده و نهادهای نظامی و حاکمیتی عملکردی فراتر از انتظار داشته‌اند.
🔹
این عضو مستعفی حزب اراده ملت همچنین با انتقاد از رویکرد بخشی از اصلاح‌طلبان نسبت به مذاکره با آمریکا، تأکید کرد که تجربه سال‌های گذشته نشان داده این مذاکرات نتوانسته به نتایج مورد انتظار منجر شود.
🔹
اسکندری‌نژاد در بخش دیگری از نامه خود، اصلاح‌طلبی را جریانی توصیف کرد که «ارتباط طبیعی و ارگانیک خود با جامعه را از دست داده» و در صورت ادامه این روند، به‌صورت طبیعی از صحنه سیاسی و اجتماعی حذف خواهد شد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/437592" target="_blank">📅 04:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فاکس نیوز: نیروهای امنیتی فرد تیرانداز را زمین‌گیر کرده‌اند
🔹
شبکۀ فاکس‌نیوز گزارش داد نیروهای امنیتی فرد تیرانداز در اطراف کاخ سفید را از زمین‌گیر و اوضاع را تحت کنترل درآورده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/437591" target="_blank">📅 04:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b584ab479.mp4?token=RD6dP-vhlTdwH9NGV_b2M7VP2XtW39aUGgoqXKh1_v05D_vll7wcihTI7uUMPNP2kBcnr3R2XByNWXnu5m5GBwtwn5DBLHckgRC02V3_na1PsgnSSkywEM8zSzkXMxiEP9axrgYoZYOcvMnx2tu4WvLQ7ZcV11X5doxGd3jbE6n2wzSHK7mY-R24JDfkg0g0A5Y7pkGD_epenOBVTQWgYszvYqTCUUnqSf1Ew5rUVwArg0ZS4R8J10JIHUgY_1uodcldN3YoJGuiH6ugrIgA-yN99lMnXancGzuuJ0lQBNUciC_7508m1mqb1LB0omehRPxiz9Q0EsNemlo_75AfMVn0r8W5lNAi3D8Fp-lmWDUx3n5z90bklkH8pT-F47ZUdibRCKTrHgeyNpBYikZdSJqYbCPtOEVsU4UZdlOVdHS4xaUAQeiBVV5odZ705I5J3tXpxcA86xx9DFzThHFIlKlGcGwM-bB_gIhYnvniZKl4MPUJPSMgBnLRaTjnE4TqiWz3YikJQlirfC0Pi1EQXnYLvfIZWO5ATnIJG2aSH9AIZVsrL7996HbR2bgp3EULySknlgxzaF61C5NEn03UXRsPn1T5USEo487YgDTPLAzSV6mvvktLn2c0WedO_BROE8PDDMkPWWJAS5DzsYMaW4BJWqXfQeu3IaH0rjWH5lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b584ab479.mp4?token=RD6dP-vhlTdwH9NGV_b2M7VP2XtW39aUGgoqXKh1_v05D_vll7wcihTI7uUMPNP2kBcnr3R2XByNWXnu5m5GBwtwn5DBLHckgRC02V3_na1PsgnSSkywEM8zSzkXMxiEP9axrgYoZYOcvMnx2tu4WvLQ7ZcV11X5doxGd3jbE6n2wzSHK7mY-R24JDfkg0g0A5Y7pkGD_epenOBVTQWgYszvYqTCUUnqSf1Ew5rUVwArg0ZS4R8J10JIHUgY_1uodcldN3YoJGuiH6ugrIgA-yN99lMnXancGzuuJ0lQBNUciC_7508m1mqb1LB0omehRPxiz9Q0EsNemlo_75AfMVn0r8W5lNAi3D8Fp-lmWDUx3n5z90bklkH8pT-F47ZUdibRCKTrHgeyNpBYikZdSJqYbCPtOEVsU4UZdlOVdHS4xaUAQeiBVV5odZ705I5J3tXpxcA86xx9DFzThHFIlKlGcGwM-bB_gIhYnvniZKl4MPUJPSMgBnLRaTjnE4TqiWz3YikJQlirfC0Pi1EQXnYLvfIZWO5ATnIJG2aSH9AIZVsrL7996HbR2bgp3EULySknlgxzaF61C5NEn03UXRsPn1T5USEo487YgDTPLAzSV6mvvktLn2c0WedO_BROE8PDDMkPWWJAS5DzsYMaW4BJWqXfQeu3IaH0rjWH5lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲ عملیات حزب‌الله در روز گذشته
🔹
مقاومت اسلامی لبنان از ۱۲ عملیات موشکی و پهپادی در روز گذشته علیه مواضع ارتش اشغالگر در جنوب لبنان و شمال فلسطین اشغالی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/437590" target="_blank">📅 03:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYmVdzaV2qQ78pevTQGFCEvUC-5ibUhzsWqAEeUI-Cww90oUz-4kyuaPJZvQyYNYVc2_ATqbxoN-nO3Fr4yk4dN5X-fpC1lQP2dgyKcl5iby8spC1OQvklemGPJSgqxWLglDrPtAxZQmUW6v-l4LXPrZzhVhiao_3PAtqPL7mUW_kfFIffgNkYvUzArf4CB3ZG04XTGPNytWWs0LD917SlCG4t-85tX_NX7DLLVTKrdvOzS34WREAg32bIw6FtnQ4xhdZJNpdwbCD0QWJW2AQPfv-6ixMkaoqZRNm46k9tLR91zrfr8CpDzDoVEx50_8GyLRs6C5knCTjkkIjHaNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ سد جدید در ایران افتتاح می‌شود
🔹
جانباز، معاون وزیر نیرو: تا پایان سال ۱۴۰۵، ۱۴ سد جدید در کشور به بهره‌برداری می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/437589" target="_blank">📅 03:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32243b2ce7.mp4?token=vsPctlBKFpV1rhyXOwVwK_5msiyFNBzdHQ7PyU-dABpGGkyu_F0ym2SGsGzTsgVzsPMeFocEimFkHcjgk0mulQKEmR8PQmy9JqpU-myJZO1IXIZtoAaiPrGJmLmjIrNgihZCyXnZCcJf0x5Vnn0_su_YZ0QIDa4W2hZOp0b-6cVn7ulANE2lg5o43x5sQ0PV0VycZCm9AcccBo3kVk_J7swuh-WZlylnkVSCmACqrkovYx4nDeTyw0hO0GeNs1PxMDoLEKxloi4n2w3bJs9qHjD0lwRVqxI9L2CHue5U0y1Q3bRRYW5gH6EGW5T_pJxv3JNeuuQzi-8ZP4WAES0Grg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32243b2ce7.mp4?token=vsPctlBKFpV1rhyXOwVwK_5msiyFNBzdHQ7PyU-dABpGGkyu_F0ym2SGsGzTsgVzsPMeFocEimFkHcjgk0mulQKEmR8PQmy9JqpU-myJZO1IXIZtoAaiPrGJmLmjIrNgihZCyXnZCcJf0x5Vnn0_su_YZ0QIDa4W2hZOp0b-6cVn7ulANE2lg5o43x5sQ0PV0VycZCm9AcccBo3kVk_J7swuh-WZlylnkVSCmACqrkovYx4nDeTyw0hO0GeNs1PxMDoLEKxloi4n2w3bJs9qHjD0lwRVqxI9L2CHue5U0y1Q3bRRYW5gH6EGW5T_pJxv3JNeuuQzi-8ZP4WAES0Grg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه تیراندازی در نزدیکی کاخ سفید
🔹
سرویس مخفی کاخ سفید به حالت آماده باش در آمده و به خبرنگاران دستور داده فوراً به داخل اتاق نشست خبری بدوند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/437588" target="_blank">📅 03:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
نماز شهید رئیسی در کرملین چگونه مشهور شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/437587" target="_blank">📅 02:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFvgB4mAnQRGrj3qoyczfaj9qDwE9DZLq0QL-yia-DGX313_L65tIcZq-m5_8m2Dl8VHaaph5B3UN2U3jsSWV2Z5N_8CbYeYmk1krxWGPNdRKZb_2dLcrpHR3YTB8kgjzTJE9XFCvquX1zYrad_0414aLSvdG9SyJ8JBiIC-frUPwCaJWi-siVZpPbfJTgJ7aG69DwzP7axyrJqBv0Z3Kh4eTGiEihd1ionq-Y-dsFABRo11jUyqmNB469WbsMfyIPIYzg8uJ2eBricgBwxYS7XSZ2kLhpRQPik3B95HM_Wse87NtBqmCH_h-yVdOdSCAnizqBiqJL00s40ktp-vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDECXCS20wbyvK0ei8Y1LlF5tAgj5OAqrjUAraNkjdzrasq2Qe10b4NC5PvoE7r7jL7AvvcWIXj_Uwx5Ksns1W8-0l4XJIK5HzvLCGGl6SSxFJnWSYw34pHeMj3RDoa6h51F5Xtf163rTcGmkz5UsJ0YjIb_1AOLtLmTGvGHmpGQpHaFROp-IhcNQgQfepL1gLzzv2sI9lVVpBJfzT4Xu8DGdH0nTP-5f5sMV8dyNQpNr7XpjrNHl2o4Vt5a6opqfq0TL3S4lkHAuxqvrVhJrT_FVVfp6F3bMFrGdaCiAlPeKxj1KIzyRQwXk5gAOKr9l-FfFGzNsCEXMwEb6ZTrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYb1IrizyrRAKQ5oXLmATfLh8qrXiK3nSMfe_CIbUS23ZxsevnMy5e4FtxkIzFMgnVqgfX7gXuRNJUPmxp8wWpEUWYDXxpEcjF4LcBOQMZ15MOeNoznWdo-Su0psBdvY1oAe7bZKhnrEz6Ij6PmR1FdHzfUOpIMVMKWqZleTdSHpfISHnTgkzIcBXqU4XS9bRmrPXl9Lk0L0cZ20RS8XNOdhm4Yw1zJUpRusxJXq4ZLEEIR3-3Ck7SXLl2sZcqoEU3SCaYIP4C3FFQOwwKdGjKEEA5h4wCeuDp37ki7DgXs5E9WSbY8Z8DB3OVxPdIg9c59rKtV17a9V-k_fOE1aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsyHjmvP5hqeZ1ndPtIyo0_Btgla1Fdj2OhyUSgrWRp3RxM2QgHO61E51DJZN3MdT0e5U5fXDnVNaeMF5wrjOqgaG6LW1cM8diiIgLmYX_H_qH2v_yZVtvrVZkDID1lxt8fpx29U8WmIyKX4gQNeeUWiW0WguatB99cPh7DGFK_YImzq9r5jn80D__T3bTgGGGl-x2U3qt0nhAD3EmBkbE2tj5NSdhg89sEAeDY32XfmsNLwdyBO0rKUUJwFLKlrn2G9OCDsQLTHezEucJd_-gCsPfAFbzCsoYrZZqN9-xJH5eZISDy4wMIkWjwKSk_HUO87xd8bJqj1FJLMmOv14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjsFhdfmU4hRRSwyojS2xV5HV_pqQiyRT-HH8ZhsaCslx8PDvJS5LSSC3Xj45QVjJSuMttzhLyvQweUMxGglTFqYki4JiJpcvtTbbuSMWnsVFPtLqN-FwQL9XgbOsI9BxKqi7pA8Em4ngiFoibeVnP69Pfq77nIXTmlHhGr8ghM3X_si0Mw91wLudUPTGar2vZjhn07yg9b46dboYOINDGYoUdsmJXGSVgpiERSQ_ONmZUJROgLh1p13zfQjv3ZwVe-0MmzIJYvrP3fLlfRVb23l-BUP-J34AHQWO86gbj70hWpEtXfs_VUY2FtA_Nsm8t2-JoQCcZQFEJ6HaofY7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی به‌جامانده از تجمع شنبه‌شب در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/437582" target="_blank">📅 02:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76dc06698.mp4?token=tGCsetrS2bJByNVHxGyBWUIJmUzsCXXMROwgs4rq3thOeRfAy-ECOYWwu7fRkh02_cP0CrqNf0Ad4EYRn5ijI7cwtaZq4ZgYW9V8_41shwKGVn7mQFkUOUm68Fh1Z42OJ58cFjZhm3NedkG0c6xjRa3koxMFSc265L0AGnObb_KubrdBi4ZRxMKJEu5aa_ftck_CdKfjDEBd8jIHkJsmux8k696dbifmGg6CeJGtU3WCqUrMM35G-cmOZ-S4lI9j6Zk90LjbZItpH8JYeTz4aSoqbAw1MK4qzYYLZv_xv2kfXD7kJnKA9ypQ0OYVM_JbYJTUhGWKAcPtqeBq-shUGGDs8w4EqsuKvl_-1-_hfkcDA_GHXIEbIl52Xqkwrg2Wy3NHskSQ0_J5UPrkxeE62skOEl7SOqydjSw_oHNIa5dILKYZqhhL6OBlkc3-SgmS7poTxjPQl_Xdem3T0WeIIwvlCyETCvOCvyxcCyH7HrmmHWXmxKzNBrheshaXny3w5nF0gZg7s06g76Z8_BXYpugeVa9oRGkuZYE_l5OiHgsQwpS6diNKiaThKmi8LmyMaZ-7-IaKiVoG_zbkYZLV3iyrCrp2LRfCv9K01zfbGL0wVkiVHD72OPT6BqAg_XsdDcFnRAYo0iRPR0tOlaZ-G85lHZW_on8KhNMRtKyTD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76dc06698.mp4?token=tGCsetrS2bJByNVHxGyBWUIJmUzsCXXMROwgs4rq3thOeRfAy-ECOYWwu7fRkh02_cP0CrqNf0Ad4EYRn5ijI7cwtaZq4ZgYW9V8_41shwKGVn7mQFkUOUm68Fh1Z42OJ58cFjZhm3NedkG0c6xjRa3koxMFSc265L0AGnObb_KubrdBi4ZRxMKJEu5aa_ftck_CdKfjDEBd8jIHkJsmux8k696dbifmGg6CeJGtU3WCqUrMM35G-cmOZ-S4lI9j6Zk90LjbZItpH8JYeTz4aSoqbAw1MK4qzYYLZv_xv2kfXD7kJnKA9ypQ0OYVM_JbYJTUhGWKAcPtqeBq-shUGGDs8w4EqsuKvl_-1-_hfkcDA_GHXIEbIl52Xqkwrg2Wy3NHskSQ0_J5UPrkxeE62skOEl7SOqydjSw_oHNIa5dILKYZqhhL6OBlkc3-SgmS7poTxjPQl_Xdem3T0WeIIwvlCyETCvOCvyxcCyH7HrmmHWXmxKzNBrheshaXny3w5nF0gZg7s06g76Z8_BXYpugeVa9oRGkuZYE_l5OiHgsQwpS6diNKiaThKmi8LmyMaZ-7-IaKiVoG_zbkYZLV3iyrCrp2LRfCv9K01zfbGL0wVkiVHD72OPT6BqAg_XsdDcFnRAYo0iRPR0tOlaZ-G85lHZW_on8KhNMRtKyTD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتاد‌وچهارمین شب حماسه در سمنان
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/437581" target="_blank">📅 02:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0321df321e.mp4?token=ZE5VLlFP5V4ls4BzsIyY6JqkKLJ_FvrGMgqj97Em5wm81zQ8sVw58AmRCEGFSaHVoDFjaS3inVaUdQwIitkTJ41hi3-VBpBBQTsz35BVMBgxXaafX6aRjbohEmzDEtQ_6afZw6LeWbEt5rOv87gW0AFnKbKKxsEFuJ1b5wdz4B982XZgcfZHE6uQh8n46z6ojruO5ZLQDAMfWU1CClnPAqQ4zDTV8G0C-gJeWUrcZ2a-OGdlJbz9ltpc8kdaoI9SGIOnzrg8FII55aV4KXpA59sgOA4oyYuQB28vdluizTcx3K23916kQ7o5-xu4Mbh1zShnU-5VqigqApLb3cwu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0321df321e.mp4?token=ZE5VLlFP5V4ls4BzsIyY6JqkKLJ_FvrGMgqj97Em5wm81zQ8sVw58AmRCEGFSaHVoDFjaS3inVaUdQwIitkTJ41hi3-VBpBBQTsz35BVMBgxXaafX6aRjbohEmzDEtQ_6afZw6LeWbEt5rOv87gW0AFnKbKKxsEFuJ1b5wdz4B982XZgcfZHE6uQh8n46z6ojruO5ZLQDAMfWU1CClnPAqQ4zDTV8G0C-gJeWUrcZ2a-OGdlJbz9ltpc8kdaoI9SGIOnzrg8FII55aV4KXpA59sgOA4oyYuQB28vdluizTcx3K23916kQ7o5-xu4Mbh1zShnU-5VqigqApLb3cwu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه تیراندازی در نزدیکی کاخ سفید
🔹
سرویس مخفی کاخ سفید به حالت آماده باش در آمده و به خبرنگاران دستور داده فوراً به داخل اتاق نشست خبری بدوند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/437580" target="_blank">📅 02:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
تیراندازی در نزدیکی کاخ سفید
🔹
منابع غیر رسمی از تیراندازی در نزدیکی کاخ سفید و شلیک ۲۰ الی ۳۰ گلوله خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/437579" target="_blank">📅 01:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlFeX8CsHlJoZshHifWwocNMiteagsjIvn_J7za2eWeeNZ98MrqaI7iK99pLtOnYlzhWhll2kkBj1XdE508G3hTSWfjDPLbfWeJKocg6iohumKrEOB-IXoi1mfCu-Ap5kKcOZMFBCfS3nUyGX6arZbWsT2tCl1GPJh_4aXtlDLugbQD83A63p4DwL75lHHsOwxN6I_IrzjwT-J0ko1ro5ZcGHZbluMiH5NW9_ZyNONU_l4uT6yJiPowL66N176pCfRglBFZCVaADAd_hVxYt3166sp2nK8H7nGATzNsgfRUZ6hyx84dIcaKc8CN7Ar09lrXq_Lc6j0iC2UMkNONE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHuM6wKxk7xmWgHAmNpnKNCq1NJaI3ABq3IYL6UR3Pg8OEYRBBYWjwWzrTyW5KcPm2yDQ_42-PYbNpHeqgdR_UHcefvbD1OBw0vnoGJbx8I0EMno8fXwS40JBmrmRFaE_dMQ73ckIq2MFnAF0yRehExChhDXqtHUXkAL7v7mmWy8kwpUysjHNn4Msa_i9If00vG6M0uqcM4mbbhvNSwG79O_2Th6_SUOEUMzNWs8yAkwCX8O9tgvDC8q0P_5jkDO0PyYQCHIS_aWmwgGVKrm2Vh5s6AitrofuxJw6-laYA-xcZNoBWKC6WTBP1RFuy8PzqZ6fG2XplYYu9kZBqujzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChbtV-3qca8TmOvPcGyj9l5cTGYHRPS3fYYVuvnQW4IjU_v3QR7m6j5DzF4H5zvlhXuyz_1I_2trySsjgX_gZ_c6rPfSK2vFwtxlTuGMwJd7pj2trbtUR_VPqdXiWxGpoNLf4yBZEdgdFLpPtpBX8IFx9vqr3j2ihpu1SkLs4dnYqFX1fwNsdK11h5OwNh5tGgTT3CLiQIL5cyMhgBYD7v5D77c6ZKGMa80o_h5Cwa8nuIZQdxJPCZDxg57EyPxrW_-gN0BMXP2gllrfKsyK6l9Mb0YTIjikJ458Bv8Bk_DmegMfBCyJgQK1P4xb-wPhllej01Ki4V5N_8f8wtHGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz-a0WgtkNXmxZPX6uSyVnCvoTDtwovQIORM8jv9CtJp0QdeZeVjwX4qDbP1a4dUiwOoqjSB6TLS0xf6hk1yS7GBJQVoXstKEkFmgnEuKoYYTJlKih1th_DflQgYybfocB3X8mUz050slURiFvKoyx2YCLTeaoiWguG5j0wNe-XIlP86VPu2MYmDJndpQmRlgo5_6iHr-NdY1GDrffcHQPiFeK7PVRQBX21yAI2d1EyuEEzizVPYcTM-wimcHu9TeXzu665gxExfYA7UnOZoxf3X3m-QSAqmwiwQUeHtnPkddsn8A13256POGjsBOPYTRAuHjXEziuJ_6rywM51dBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TewJVvs9XVyYeziKCqooXZ5eBAiP0Az1cH0Bd2BhlcbpuB0sxiBPB8PNCSW33bS_PT6StWwpt3a71F4isnYfYkaLz2Vpb9TcCtEDidS4qsB6Xhtc---QIl77D5ouSqx7PJNntXCY-m355pClCmApeCulAYoruxxOVvtTtv5N5x-koCVEe8KvAHo5Ou-4Cryc510Tiy58l3jrqzRN4INiuPrCw49N7IzS94C2S8fpkglZ3eL12d3kGVqoee3X5bCty7IdEvoks0XyaKw90YVm8nbw8o0gMUkMFkJyBeYekfOVXXJ_L5ig_3I9iwaHQHNJOUTOYBIeflKgWKBD4nxT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzKrSz68Sh90Nb5IzHGx8ubOylDVmURbETkhUfv0rVwOSj83cNQef1NWVK9rX_R2H7EvYQWxYxvgjoHW3CPVYrhXyNtu1CY0tEhRHq2f5J2IPjbuMjL2CcrzjKSYulS5yqqYXggVEgQEOzAgJro1T5DMM1NUdm686Q2shsb2jiWNay2PcDbFVW3t6nrxbumyqYHcDluXQdHQEr3TUqddHmZmQEKFAt8UtwfVojQ8Ca27fENi15rQR7cZuBOJsRMIygPcmL8KBJ5nd98jkB-Wikma5uu5Z0AGOHz8C5JT5kIAD4VCD1okCiGrjSAKtOsnAHdxy7hgjUHL16scpb_z9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۳ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/437573" target="_blank">📅 01:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRg9wC5sqcrkqyX6ufbI1Oz1I7gM90Gmu_fWJvCnrSJ8WfvVouEg2QnzaI7_VM8xZLbQbWNtnDoKD1VDyfD2yGVAo50sKmpMYJQ-96voH-EPGnVAKl9CFXkcfOLpoNSxvYwHsxdl3YVEYZLfLQnkPvk1zRPs_SEIViD10BQT9m6bXlCpMF5LCOXwzbuhKwnFZpuwGxyZJMYD3JYeiSooJ89txMBKInZi6mG1Vbp-HBIFNkMfLk52nkRJcGKyhveXNOihbN_zHagdsN_npR_dJ-tqmNbkB6yzWlFV32f1FCel6uJA-rcIdqBIn6Yx_bU9UZVQPDD60LevPERmijAA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJiE96GI3ufyP9S5RmGe_Q3hTnhiiU75oAEIjuqbSozEvmIGd41Ify1S0etNE5_TYaMQCDRQKhmsLli-oZMHc5Bm5n-qBJbdi9BkaPW7tVwXECSEQtrPji5khQW-wOofIJuBgmnC6CqduYFOqzyphbMVFWTTsVcZu-7A9SoVgDj8iZNbHut5CxPFDUNevq0N8GVoBeeRDavV0si_HcZpEdugLhBW4uNBTpPXgXrZ3uxQQXAc3aNHBAXmfUeQJQ7Ban_4Y0-5AC361XhPS9WvRApX5PFZ4KF0_hGS_ZH9k319Crtdms_rOCS_sIaCf1hl5BtUew0PPiIuyHRRGyO0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SboIuJs9hwXwe3mX947ZrElQSbX9xAZYuvEkfa5Xylzwd2BGDfMpo_V0MEc0T9GWUBenIMSQQwCgAX8pEkL4T83y1Y-ZJaKMyfb3ti6qmGIP8TinzEllZa3mS9BsL8AZRPRhJdlaLdqPKyMVV1cqzbi-kMGfpZ4gRQawJwFvSeLWYe0Wi7MCj-rEY46MIgTKvjta0cfjOD9_cy_vO792T0jNhukJ-E9dZrQ8_J9YPCfvD-lqWPAQklxj530jh_xjHILcB3AhD_LO7tmrxCPrV0RdMhKDq5a5HaTCI5Gb-p7foXK-PpS6CxKT6Cy--E7dN0gJJdV8Z261bieh37AUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTwXEuWdH0DZLET_vtiTK1fgJl0a_5eY7QUeIduI44gULCPHUMUh6GQJPLz4bwbC7pRh8xghURwVjUyjBDUXw3xLYUjwHOCKs5AWJ3TQCglaEgPAiFRV2XAcBLiEuDptLO8bfjRzhc7JniWUBOkhnzN3t98WxQP2fx7GXGp3nlyj4jA-wKg-sWphSJkImMFnMnBIcj7gquEKf8PKtdDVK4LvguylQabwW-z3l95Fbyw-4Edcku19I_PQX_k_MpTqHy3LJHnxCZHLKq5EqW2Atf1oTOotoyB7bpUJO10PhBORUEvtdQ2kyj6uVEBDYIz_ZHYqGFwnotA9JEWJMK4-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR4-QHM1ZoxNCv5goIlKJNLqprzKCAtex1xsVqOIZttLE1ufstjCWbhDWmb7PhhV7LsQ6IncO95wFhd3RuxGYXpCVeOTCpoTl0LO9UOAI_JUvQzSksCaMePjRUuworjzjQw-oK7TyTdJeir9qDgYHv_rL0QMqIbYIyEasuJlZASMdHAEZUeSSfZzPZ41Pir8xH4os5SKKTT1x-mFd8v6d55xYfzevVcGX2VJD_l77vP7D9hDodGbzmTsI4qoeTdj46n9UYaHqjcSflUbGGGbkffSnIuF9qJWwgWyxCdiyAHQTQ2sgcGnK4E1qojslRXQntvGhrcoQp6gZJJ_9S0BIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsLZpPQSMBArKTgJ8h9_1Xyix0vEkiUsbjIdC3KqpVy74-DD_MMjRJLArRDHX9jgyE-bKRCjosJvlP-6Ksl6DLJyGvjakrvfPQIyzZuBEx6sLREfzGv7d7UgD1lz5HKEXjYGOXBzVn7px8ZC7oVbVHbQq3aAopXqmigq1s556qD0O2S8xP6uRxUG3-4jy1UYEEiAhMxuC-vZ_bTpBk78dCeY5XlgX6ca37yzXbDlzP0T5g7Ut2pG7zbxdok-AB-1_Pkhq-juuM-pQf2obgyr0OByGjn3TVNmOzxSTBf_MJFZ2l-eNwByouoNPOg9ftwdkyAID2Q6ZLTX3ZUFJMWcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6FAYBjonHic9Pk_3mJSjSg462uOQzd-wSSDTMadXGNHu0zcJUv4IJEPBd9l-zcEPig1UVaTTfU1FyErZM0QQNaBvNtoTRjU8uiQUgs_sDuU6HB-sq67hwciGCxb7Rrm2ojPY00Wo83-XHBJHDGZBGlqvi4akWcet-dm7xteDTjXaZBU53ThuB0TkN2XLKOPpudkJSi6m9oKmJAh900Klkej7C2Fu0AR8cDf7sBnY0p-4BMndjcRjbNB9lvlUCU_U1O6InmFbd4QXk23l5I4iR9XlEfS0LqMpYPD6R9mzuAxSlBxpmLmzwFvGCDS1EHppebuW3QF-51ic73ZEwcN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-CrhVhaZxT27dVF9ho22_1BS_UcgCwFiUdbE-sWCHpbM2wX7xau_Nyj7TG7qwBuKz9HtxJEdMhmNfc4XOMfl6k22feGFbuMM7bLbyrUV-XqXv5QfJesaI_OUnlParqwo-69gihPHbSnu69CiWj5yRTJr_2mqJi3ZPlTjcypdnbxWF5jn4oTsK5J0gHIYOe5PnbgMVre2oJIGf1jloUqcaPLGcP6eOH3w8Cieg-HhQaZeVMDT71ccmukzqUEzj0oIs8QbPs-I-cVBk82_zVFIL8X_J5x5GXrrnX3l1yHpOxzOxliSn9gmvVKujaVdOx4pawo0kd7BBUigGRiuODVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLPm69oHQ9y-I8MGCGoyeXRlGCUSNMM9kkWGShDWT0YTzI_M1Xw8A89689rXsZzU6RBzSb_KJMG_fSgRmpUJM1DDG8kOIrvPssbTDiwtOc1ZwueARv3pwVmjQOUU_62RzLeqtr--XQFNmdoD60FGi0Ly60qqNKkaT0xeNdFAFfG7pI0POVyOm-MQroDppfbRuAJxEdstFJWKC2VkmBp1z4vH9wUTYiKfEpjrrR-r1dphilwmtlu1u-28MKLPe-Vrs6nacYDIpLiGNaET_Mnr4etWy8RPUiCMi0NvYF23-Rm-71z9Nren77b5vBC-3C57aiEt63B2cUQKcP6IBxWV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqIIU62O0h5uCN7135TvJBgXYwIcPm1MFLi8Pq1qJ9BoMZTpbbS8LLBP0ywG3H5RAlRXXOQGOTcQXABAtAc38F5zLCy1c35pISUUYjSJEZLsM2srDBpyUoc2c7_fx_YSL9IkQCOIa39o7BYaschXFDJIYEKVRro8qh8OLKjlOa6Jd7ncRX6yzVkDK0bdA1S2cZONPksefJSbsUB3Rong5uZozFsySQ7Fmg62I-3Jz5iKuxlR8-pifjCJ7xn5zC7t4071y9wQTt-MupFAWtNRlpc0XVFmBEmxdUmLrW_bEclkylH0RWP1xT_wZuxpmj_cmJ-J686t1OaAoaY2laneyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/437563" target="_blank">📅 01:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5nxQmgTwkdbGkVebfqBYIhb_O73BWT9pVX9gnvy8Mqo5nS_6eMMOrgcbm531i8KoFHEHBCpBzocBfGeShFKSKjgxO60KORqOD_YhHVskv577PJFUckaJo8qlLNMdSaCOf4Ws_g4F9JODe3nKaR9fJOxQYFG35RUzj4zCnoWE6qptlNduP5W1pInmRJvVPdzoIaRAtiONEMLNcOhJmhKrUnjRFSE4UGa9sFKGYh-w6dLzQtYsRGNPgXSrKXuYIrDvWlNLfweBEN9sqkWanESXro9hmwB_2UlDhAVnTT_VlzQFvmmxBLXm-SP0jZnIrG2VLSMovdN0M8wS61I4uvdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصادف خودروی ديپلماتيک جمهوری آذربایجان در محور مرند-جلفا؛ راننده فوت کرد
🔹
رئیس پلیس‌راه آذربایجان‌شرقی: در پی برخورد یک دستگاه خودروی سواری پلاک دیپلماتیک با کامیون میکسر حمل بتن در محور مرند-جلفا، رانندۀ خودروی ديپلماتيک که به‌تنهایی در خودرو حضور داشت بر اثر شدت جراحات وارده در صحنه جان باخت.
🔸
گفتنی است، برخی رسانه‌ها به اشتباه از فوت دیپلمات جمهوری آذربایجان در این حادثه خبر داده بودند، درحالی که فرد فوت شده رانندۀ کنسولگری این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/437562" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437559">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/437559" target="_blank">📅 00:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437558">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK0m_1606I-DnLD582VKRN0edzAxRjMYHdQKqyxQwkef2E6coAittKf7Uj8noov2qdJOEbvmtlTPQHFlR_sPBdh8dMahgeGcuWwyWCtekRzhp448kok6zstz4S1GfI0YbbGbNC_l2IgiS8XYdJmY7JwEFr76dwBFO8dJCqPnsed-w9FKEcFx3qZNsOM6lWlnfGDqmSTwDmS4iWauNbAWXLeGwg24fcKYMcyU8hX6FLhSoEEDVW8_KFmhOtOnBF2WjvGjFE8es2e0GP0U4LjR_3u77X-tpFPSwcAe5pDlv5_RfkgKx089AZA_gcwMrxMDrdY7M1yGVKS6jThL9pXIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری گاردین از برخورد متا با مخالفان سعودی
🔹
گزارش جدید گاردین نشان می‌دهد شماری از پلتفرم‌های بزرگ شبکه‌های اجتماعی از جمله اینستاگرام، فیس‌بوک و اسنپ‌چت، حساب‌های مرتبط با فعالان آزادی بیانِ مخالف سعودی را در داخل عربستان محدود یا مسدود کرده‌اند.
🔹
در واکنش به این موضوع، شرکت متا اعلام کرده که در برخی کشورها ناچار است محتوا یا حساب‌هایی را که طبق قوانین محلی غیرقانونی شناخته می‌شوند، محدود کند.
🔹
این ادعا درحالی مطرح می‌شود که این شرکت حاضر نشده تحت قوانین ایران حساب‌هایی که در کشور باعث خرابکاری شدند را محدود کند و در رفتارهایی متضاد اقدام به مسدودسازی حساب‌های دیگر، از جمله حساب‌های طرفدار فلسطین کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/437558" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437557">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق باز خواهد شد» افزود: جزئیات و جنبه‌های نهایی توافق ایران در حال حاضر مورد بحث است و به زودی اعلام خواهد شد.
🔹
ترامپ افزود: با رهبران و مقامات عربستان سعودی، امارات، قطر، پاکستان، ترکیه، مصر، اردن و بحرین در مورد ایران تماس خوبی داشتم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/437557" target="_blank">📅 00:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437556">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU8HjAnFDT0t5wWgNejG6t7c0vvdmux38r7noBYkizDaqDBkWip49i_6Tz7rJ_kbjUuBmobyUxwpgyU76GUOQSP2zIs8viNS_NTg0z5BsuRDaKKlNIBOflR5A14UxDnjfXRNH-5oLrHEzjGbMiy0tiZ-fZ-JRxi30dkK_1QF_I4iM7mSfjBJCLBhltE9D54b2tHXi5PCCN4mAts_Us6l4_iV-hPJAro7NgbmPlH4fWToWuNk0aECNkzAFul5aMsz4LPE9ueKXPm8YNOSzyfGwpK26dUcg72iByoU0aqJ29b6iIIXj66Ej871XRVw74NkVzkrpANW4M4eO1SFe3DcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماهی و صیادان
🔹
در آبگیری دوردست و سرسبز، ۳ ماهی زندگی می‌کردند: یکی بسیار عاقل و دوراندیش، دیگری نیمه‌عاقل (با‌هوش اما کمی تنبل)، و سومی نادان و بی‌تفاوت.
🔹
زندگی آن‌ها آرام بود تا اینکه روزی ۲ صیاد از کنار آبگیر عبور کردند و تصمیم گرفتند با تورهای خود بازگردند و ماهی‌ها را صید کنند.
🔹
ماهی عاقل به محض شنیدن سخن صیادان، وقت را تلف نکرد. او می‌دانست که نباید خطر را کوچک شمرد؛ پس بی‌سروصدا از راه‌آبِ باریکی که به رودخانه بزرگ وصل می‌شد، گریخت و خود را نجات داد.
🔹
ماهی نیمه‌عاقل پس از رفتن صیادان تازه به فکر فرورفت و با خود گفت: «افسوس که غفلت کردم و فرصت فرار از دست رفت؛ اما نباید ناامید شوم.» وقتی صیادان آمدند و راه‌آب را بستند، او خود را به مردن زد و روی آب شناور شد. صیادان به گمان اینکه او مرده است، از آب بیرونش انداختند و او در یک فرصت مناسب، خود را به داخل رودخانه پرتاب کرد.
🔹
ماهی نادان همچنان بی‌خیال ماند و دست روی دست گذاشت. با خود می‌گفت: «هنوز که اتفاقی نیفتاده است، تا پیشامد بعدی خدا بزرگ است!» او هیچ تدبیری نیندیشید، سرانجام در تور صیادان گرفتار شد و جان خود را از دست داد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/437556" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437555">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد یاسوجی‌ها: این آخرین قماره، جنگ ادامه داره
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/437555" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437554">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
«انّ معی ربّی» فرمایش امام است
🔸
در دست تک‌تک ما شمشیر انتقام است
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/437554" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از حضور مردم در شب هشتادوچهارم
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/437553" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه ایران شده جان‌فدای حسین
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/437552" target="_blank">📅 23:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سامانه ثبت ادعای مالکیت املاک راه‌اندازی شد
🔹
تمام افرادی که ملک و زمین‌شان قول‌نامه‌ای است، ۲ سال فرصت دارند مدارک خود را برای دریافت سند رسمی بارگذاری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/437551" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/437550" target="_blank">📅 23:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقی‌پور، نماینده مجلس: شبکۀ حیاتی کابل‌های فیبر نوری جهان از تنگۀ هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/437549" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بروجرد برای امام باقر(ع) در هشتادوچهارمین شب تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/437548" target="_blank">📅 22:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnvP8-bGkpwiFbGvKW0LJXvkPDPT4OpQTpbhP4CDmij8R7_SNPP33OmajuTlf7G5ra-UqHO4MKwK3v5JkUKU1KvipQjClMLSP1eY78vN9C2sSU2K8tXop0pm1iRLO1kWpG3rnR1RqbT3xEb7xwywaM8kgkxNbFOsMxGvo3YbxgVnnYPiExVopP7dfyWmhQhG9MmE7WziscjLxEhtZWE0TdkakrTQ2OhkkEWIstUIS_OX4Yl4qB2XoFHmysrWpxquiHLlv5K0faKJvzYTky11J9GBUmmdfEtZMmZ9vBXBIZwSk5wiQAS4k_sBbN74n-t5Cyg4arrT22VY0ZBk6bsjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی سفارت آمریکا در اوکراین برای حمله احتمالی روسیه
🔹
سفارت ایالات‌متحده در کیف: اطلاعاتی دربارۀ یک حملۀ قابل‌توجه احتمالی ازسوی روسیه به خاک اوکراین دریافت کرده‌ایم؛ شهروندان آمریکایی آمادۀ رفتن فوری به پناهگاه باشند.
🔸
ساعتی قبل زلنسکی، رئیس‌جمهور اوکراین هم گفته بود به اطلاعاتی دست یافته که نشان می‌دهد روسیه خود را برای یک حمله موشکی سنگین به اوکراین آماده می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/437547" target="_blank">📅 22:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور  آهنگران کنار مزار شهیدپاکپور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/437546" target="_blank">📅 22:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: موافق اصلاح ساعت رسمی کشور هستیم
🔹
تغییر ساعت رسمی حدود ۱۰۰۰ مگاوات کاهش مصرف برق را به‌‌دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/437545" target="_blank">📅 22:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار و آتش‌سوزی در مقر کومله در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/437543" target="_blank">📅 22:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هرگونه تجاوز دشمن با ضربات جبران‌ناپذیر مواجه می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/437542" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار ۸۴ مردم بجنورد با بزرگداشت شهادت امام باقر(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/437541" target="_blank">📅 22:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔹
علی نیکزاد، نماینده اردبیل
🔹
عبدالرضا مصری، نماینده کرمانشاه
🔹
حسینعلی حاجی‌دلیگانی، نماینده شاهین‌شهر
🔹
حمیدرضا حاجی‌بابایی، نماینده همدان
🔹
رضا جباری، نماینده مسجدسلیمان
🔹
علیرضا منادی، نماینده تبریز
🔹
پیمان فلسفی، نماینده تهران
🔹
انتخابات هیئت‌رئیسه مجلس دوشنبه این هفته برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/437540" target="_blank">📅 22:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrS0d-rTyiXFqFSzCdx-FOZcsx5uOhQwnUDZp6CbNF_A9G1PQKWaNj3h9UT2nyH6ZL3jJ03ucZVWiRbozOYMATERZUh7AEENsbfHZzKbeT6DwTRItMFNRrUDuKtyINI3RzYPU1hZWN0FCO0A_Yy7y74zhClkW6deTHnhQ9AJzGGti5mfkmLzwBZC1tAnVvwf9KLKJTiL5VcnsOBgmGCxySC0hptdM2YApQWckfNnTT77x5I8lolfUMwmTck49CcXtwKv8yrvhkVtwG5V-SiDrlXyTR8iHTIW7IA6u3TbDCvDE_2x8X_YuVt8aipB4VHd_AYxxl2vmI4FEHlK0EkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد پرسپولیس: تورنومنت ۶جانبه برای انتخاب نمایندگان آسیایی برگزار شود
🔹
درپی مبهم‌بودن وضعیت پایان لیگ‌برتر و انتخاب نمایندگان ایران برای مسابقات آسیایی، اختلافاتی بین باشگا‌ها درباره این موضوع به‌وجود آمده است.
🔹
پرسپولیسی‌ها اعتقاد دارند نمایندگان ایران…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/437539" target="_blank">📅 22:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437538">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار تجمع امشب بندرعباسی‌ها: ما هم ابرقدرتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/437538" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437537">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاشیه‌نگاری فارس از پنجمین تمرین تیم ملی در ترکیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/437537" target="_blank">📅 21:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437536">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8lSDENN7ZfHB3v-5e2ZvQMtF1yH-1Ek-E0hhzI4VjBOUvRB129W4Q93BSDqVLQKHYIQfoJEvQVyKfewZq1_oPw4dUvoUgpY6kq1SX0IysgYeyFZBP-WzfTj6T33Y1v0ifv48BegoQyq84czc7-SgxbxDtFmCeJUhQCwqdgdpeW3ML792RrQ8HN4DjoHT2T1Ud04SNvVnualR0NSnKKJW_1DMF2-9DWNqNSwJ-F9cg10TVpBgSZ96aD8pIumUjYh8GDvlPS1sBNwkzCWUaOHZy8NYdBAZU6dw2dFhisxgKieRFI0Xjjtgk_qZcdtM056x2bEek3zVdyY3ZSsFr1JSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: ایران در جنگ پیروز شد
🔹
گیورا ایلاند، رئیس سابق شورای امنیت داخلی اسرائیل:  سناریوی بهتر برای آمریکا، بازگشت به روال پیش از جنگ در تنگه هرمز با رفع محاصره علیه ایران است.
🔹
ایران در این جنگ پیروز شد، شاید پیروزی با چند امتیاز بیشتر اما این یک پیروزی آشکار است؛ آن‌ها می‌توانند از نتیجه جنگ رضات بیشتری داشته باشند.
🔹
آمریکا در تنگنای آشکاری گیر افتاده و در نتیجه این امر، اسرائیل نیز در مخصمه بزرگتری قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/437536" target="_blank">📅 21:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437535">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
آمریکا زیر بار هزینه‌های جنگ؛ ضررها ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/437535" target="_blank">📅 21:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437528">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAYQFYaCw9MSMD4uOaDTWT0hQ-bS_NKcAZyydRSEdsyp470TVUFZgDNRT_yfe4Ipk1vfYmmMqXTyjcEueiXw33wvNamLKLUpa4HmK7r5VdRss9iRG0GdtlIvesU1EENXMc0VZLHBTbM90DjDwvifRsiVtiUsSVPVGOS_TxU6V-4MjK2Z36X96lWjkA1CFQmm1SXWc6ouCk2o_EeDOtgVFVA6ri84tsz5Pf3OMpYYZ9uyrJFp87c1sv43-EAQ5Geh8-zTRgXwGKP8vl6ufJFYvzvbUqr5VhbdfOOS9SI1kcXZP-I5N9e5cPkZ7lDD0y8LuhebVhmnydM9V8rse5QS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1sJoGPvQouELgC7YNo2g3QpG5UsomRVzwswoE_W8fRgJAF7cHb2mrETEhXEPOuLkBsXQdI46-2rcCbkUz_wOTP1lzS7AXMq5cvLfqLnlor4FsGK5kMyU7HVfnpDUjCGc98XwsBGdSvI7qg8KUAF48acvaIOMAzLx_kOCJp9RW-8hjcd6rlW9DCCsMBSVga0HC4ju4x85BTBaWdy3GvOXdhGh4RA42TzzxchyeIMadcU0oONnvqT0iU5-kX1A2HBvP2TcJA97pUgqZ9m1p756MQU16jsbBgtkOsKBuMybDRGMXfpg9GeRMdl0RrO5CC1-cU_HSQQGZt-odVpeOckyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9ebEWu4TiD2C2RUbxf8NNQ2HOYVr-G_Mp7gIB855yNmx9Ws-q7LWMV4VQ-qNIpBNg-A5Awwps2sPLNxgPpIqkIRMoQfmTxGfjmihK-vdUvq2aw2Wy62QAcADHdT-epPVpXoGdgQ-eZqXYTXNatohiLutwaVRusj7uUkWECrLoFkTOfjiYT8ZTytiWANByhHPCBBkNd6lYAbYF_ZSL29E4wF0PO4BBcewH7VFXhBH29WzC3QpgOtMLWW_70TEvNJAOVUrtpZGLy_0aQUcnmWss7nz7ge_UHkk7pNEEqNakoaamM4RXtmhx3-52BHsUXig2N5C1T3IfeXPAtFq3O_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNpAoiiBymldUaOHNMgypqD6qysfCb2QqmLT5UrHObILHT-UEHCYLrZqXjLLmc4mZctMnpFJO45djVmYuqWU6goa0mlu1UxF5biYPhX85q3CJx6dHTajVKh4K1g3ZF-8oXutQhhhsmcFvuDVNjiQs2tQfAOMF9Bwd_3enHiecmrNu6dc4UBnN0xJMkmCTA1GzQAWu-te3HFDLwbXBApEMZh-bRZf83eGKEhhOTbG9Oag71okrMp29eWMEQTKdeIuS3dgl1kQtxn04C-rfp-gpYTNZA6rvfFOS_sBd_YenTZu5BQkBtgW9OT8c8I5QMlNaz8NHS3GqP23kvBExje9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln0w_zv94OFsEN-c7-GObYREY_RGkrrtq72EfpPHO2B76_YADt_B-QDQe7L2HCuiLdm7SxH44A-nk5T3h5d8jckQfuT7dm8U17Ni2Z7cWAh-F_yEE-l0RfmAXY8rXUQP7Vbd2Odzx1CGrADduDfV-qIizUQSUScCGRImzNSVxaq1WIciqJrkhRupzpyya8ZHKp9daKVgYiR4-Zq_6gJq663f392T2dF5L09k9Pd4D54tC-QTORuCJm-zR7656kg-uAqCCPwxoO4sIvSC1TSsVM0fzYP8yWmtsVTS2wgF589jusigIRFxf54ttyqv0ds4Lcgl5zlx7iGS5r1uC_pGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtpfGI9FSGabCu5WMcpjaKpWGaxXc9wTpOT5kqqGuswicEu_oCsowxy8ozsa8HjzHTaFTuA3bSfR3gniaeKJh85A_F25XjrMbFE9AbI7T_i4wAPFSFYi8kuyqAz92kgiVHvC87lX-N1j5aXYUWfOeTvOdQgy0gVTe-osLjE4PXIBPUXx3s6kkdeRWQe606EkxpmLSN1KtBaGdhPTPltnYgThHxz5BQ53GL268QRsiNYo4P8p8R76SX1eLDqExoxKMc7iPUM29dw_E2HAsBcSbqFiX_oDdHNo6BUB-Hki4nIyuMpZegTgKpYS6iSSRjxLPEVc7V4T-8nWkRomYKaFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPZg4rijt__HSToI07e_R9e8v77FHg-0lVoUJa3vbtHiuIzq7U2SJQZwq71pKykLqz3dVDAIdPs8B_CsJ_Ndk0_1HQkNizhSRFbqkPLijUnTa_jA8-KR6V6KFPov4MBm9H7rVXOACYmaKL5j_33cMmyKfvd6DYq-ryHIa1uwtQ5geB2JzJrhDc1Hx1qv1IKWhwmEuXSBGYTccjSyFOoegbxEoVheKIGNmbOdkpHQVhkD1aTvtzXjDqTffmYaESjMGu_JmmMphBPNPOxVUfYVhAwsd08jykKmO45GV4gxk_Ypc_fQTHEpezHROsTvqPBEwpziVyvTRDlMlBg9PJCdKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازسازی
کنیسۀ عزرا یعقوب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/437528" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437527">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTEHsNSXQZRl5E8Qdrr8tq2dGjviwWP1K3ZB9xVue1JE6lcp-9fWSilJINFxELsZRq8u6643GN3H9KUWpPz0IwRsThfNFsStPwDCa1RGFZjRZ2Wp1A3qjdHGiKGOuNbapDFEO8gyhjlOC5bIXXErDhbghNhBO8AMu2SNilQyh_7X_5aBtbIEjxGYScM5cyR6pNQbNm8T5Tgzh1Z4IGdARNfj9D9rRqhCRQuceigMUma8sd87b4GUFIKnqjUj3OlLLFlR2-yDC5DT8ScpUR_6hozmKV2msWJIFMvqZyWGk3B9wHRr8yUX3y3sL59ZoxJLqLhaxpCOcUjh6ZRSXzbkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ملت ایران، تجسم داستان‌های فردوسی
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/437527" target="_blank">📅 21:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437526">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0m1aFlFUXAGXhtMKHf04cPayYknWRCKXWgdnKkzXPA_yETfK6OC2Z3yMmv1xfahAvvs0MCUqjk-SnptYbwIkg6KkD45FY2o25umwf9wasHCtkCWBTNyRJKou0opHBCfYpYLxVemk-qGgm2Nhfjp49PiH5tDIwvpUgf9ni1Rwp39Wl6GiQKcNwRnB8sElCkc7e0lxO-j8QoIm8BOnPOfmdwF0GBQ-WaZySaymolMeTm7dIgRPxPZIEYQCoMq6kldEeJJfD9fuLnmT32_sfgMxJEjuPCCG1GkkdQFIMtWtyEG1Il44YGfYWwEClDq0mxL5aCOpEiABXbOnF1A7HTISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/437526" target="_blank">📅 21:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437525">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانۀ اسرائیلی: تفاهم میان ایران و آمریکا به ضرر ماست
🔹
شبکه ۱۳ اسرائیل: صحبت از مذاکرات پیشرفته میان ایران و آمریکا درحالی است که مسائل حیاتی برای اسرائیل، در این تفاهم‌نامه وجود ندارد.
🔹
اگر آتش‌بس بین ایران و آمریکا به مدت ۶۰ روز تمدید شود، این کاملا با آن‌چه اسرائیل می‌خواست در تضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/437525" target="_blank">📅 21:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437524">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
امسال صاحب‌خانه‌تان با شما راه آمده است؟
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/437524" target="_blank">📅 21:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437523">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iglnke4HmFiwHkoel9i28sQSg7WbLFIvTXsXxcXngWiuVnSnx7fySAtbZmjpQ2Ap7cZdSstBPYn46LH4gIUXTMsd6r5oTzMP1aJmYZMR3WnYS0jfe-MLHc62t-s7jXE8Huf7BjX6ZDVwDHNeETd1V87BEN8Opdd5y5q07llMX45rQNpNZMsvU7ix41XTLiarDUY-mUUyNrgP2PdnXjLnuJ0AqkRe2F9H5IITyqySubuUM57ZJbWjY5gHxqrmnKIiPWRd7ghMZfRL_Zb9ZJ_bgBIFB-2p9UNjkuRF2IGDQ7gmrYdSI2g8l28qDnFJjtw-citjr820LloRiWGSbCZNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانك ملت در عرصه تامین مالی با عرضه محصول جدید «تیما»/ ۵خط كسب و كاری مهم كشور تامین مالی می شوند
🔹
بانک ملت با عرضه محصول جدید خود با عنوان «تیما»(تامین یکپارچه مالی ملت ایران)، گام بلندی را در عرصه تامین مالی زنجیره تأمین برداشت.
🔹
تأمین یکپارچه مالی (تیما) به عنوان یک زیرساخت جامع برای ارائه خدمات دیجیتالی اعتباری مکمل فعالیت های گذشته طراحی و عملیاتی شده است.
🔹
تیما پنج خط کسب و کاری را شامل تأمین مالی مصرف کنندگان در عمق زنجیره تامین(تیما لایت)، تأمین مالی غیرمستقیم پروژه ها (تیما پرو)، تأمین مالی از طریق لندتک ها (تیما لند)، تأمین مالی در عمق زنجیره تأمین برای صنایع سنگین (تیما پلاس) و تأمین مالی شرکت های توزیع کننده و پخش (تیما پخش) پیگیری می کند.
🔹
تیما با تمرکز بر نیازهای مختلف زنجیره تأمین و با هدف حل مسائل مرتبط با زنجیره های تأمین عادی و پروژه محور به بهره برداری رسیده است و افزایش قدرت خرید مصرف کنندگان، کاهش تأخیر در پرداخت ها و کاهش ریسک نقدینگی در عمق زنجیره تأمین را به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/437523" target="_blank">📅 21:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437522">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">#ببینید
آنونس معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا
همزمان با روز جهانی ارتباطات و روابط عمومی، کلیپ معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا با حضور مدیرعامل سازمان منطقه آزاد ارس رونمایی شد.
این اثر توسط اداره کل روابط عمومی و امور بین الملل سازمان منطقه آزاد ارس و با هدف معرفی ظرفیت‌های اقتصادی، سرمایه‌گذاری، گردشگری و ترانزیتی منطقه آزاد ارس برای مخاطبان بین‌المللی تولید شده و گامی در مسیر تقویت دیپلماسی رسانه‌ای و توسعه ارتباطات جهانی این منطقه به شمار می‌رود.
منطقه آزاد ارس؛ دروازه ارتباط ایران با بازارهای منطقه‌ای و بین‌المللی</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437522" target="_blank">📅 21:13 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
