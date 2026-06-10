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
<img src="https://cdn4.telesco.pe/file/SAXMoVtsV5vR8Mog_ilzAdmm--ujVL-CFGa14rQ3HeKF_xndggELlVFR2poMfLXUaQwW-KXF4Pj5nozdcBGlPcmbHltWBzYyjZ0ntuwc0lO6gw9Ro2CyBUehzORSYrpgO-BAKYKoNKYFtZv59lHR-d5xjs51a15wGQs_GEixklfEikEyc4HkaWJ5_hqbL5oF4OZQO7N-aB8Y1GEot1NVP2ZRuyOgVAsCrSLPzayCxckdBELFjoh2C3E8Jji13afu1T-p3l-cGXapQueKwZldNz40cHDtfKwAdx0ZegYeDLDmOjMVs0n3xX3wyQx3oXos9utSefgOyfKezXRsR7b3QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 03:23:56</div>
<hr>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj1RpKtqk7sKEcEi0Y1GtATFdk2JNaoXaDHJkGN6-yj7ogeqR1UKa8pRxzxqgtsmhc_4V3NmmA48eCzpd3HIDyrOYZutbXFJg4-gMbbLMIgIPQUrpNcjPvHk8islQlqn6vAN9Hlw_-Hw3ehfY3GcmQ2ftRtTcPe9aP9BzdN3QZ3FrFIG4sJ6wUJc4ggKrMZ9NamUZWsOxqakiH-YFgbgoRmyqczvr1AueMG_FMUzKKRGXqzgrniUlzX_mrTWA3bx1JfRxU9JA1dyIn6VEQnavL9YUkFgtxNcnHqRi7xFFxQmOSjmIwYX44C_nJLsUtgof_ol_d4VD8vYVwO01RyXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 110 · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd3Q-rfJ1nF9r576pgTVYoC5FHApl9FZ4RNrNC3mSplLfB3leQNGUy4W_f4pYhRMguY00501K3ypEJ7a399vyLuwcjUSqkh9TZ5KstcwgDWkvec0LFYlzYKHv1u00qwbWUvPm3w6AVws-FXRaNooWW47ozW6tK9R9jZF1Kd0QIAhx7kwWAXwzcZKfrUqJjyNSrMbcBabTI3sEzlKIR0VSHW3JreCClRXWVP6x9sSaauSNQ2revQjoLK-PppMTRhjvTiSojF27l18GaMt9hPwtFV69uuT7DsMfmMZTba6pnV7uYkzNEcH_nu0-e7ixz6ZdxbwabpU3DJgTOuQi2_fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti3L8onMtqznfhME7Ut5wv_465syR7o0kyXgSmA506xCGaKdRRMLdI0nBz5PWLByeMBoiT12fSb9q2DO1tuHKhRNhyqiOUowWHjYL36xzy3vte2x05ZktCR8SaLJBvI5ANVLpLVL97gBPQih7gs4cmPxi6y3zQoWQG5HsXCNpt4wkQPjayAP3SUwBfXpvqNiC6Wth9n0UW_Z6fr4Ms9MOwlbQTs4sHFyL_BiPesB7iNP4T-9ZtnUGPER58PMsFVhd-hRvdlIvYt8GeQPjs3PQY8ut81CZZjQcZflg7ciRNclXm3tRFzE0Ya6V9YL6FO1QtmB1DiWedm9SocLjuFaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😳
⏳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 43 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6264" target="_blank">📅 18:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=aAsErgm01zKu-5MV1JQGtwTYx4WT5spG-nbp69rf6qdSIeArb8lrNHrJoVXkmVQ5QWpnIgZ_yDkqegKK8uiKvSVlT3xZExrCPMx1eQetWfdnhDFV1mCPx_EmZGPPrV63ZVzqTdu_3jJn4uVHJe-xWO_HYe6fAJNzV3zYEMDF4kUsmnPX0LJV4Dk0FxflQowp7yNdfTkcKXiEoqDbWutjk0M75kXKKjsBQvnMqc8g8pxz0n7T2P1It2TUzh_L6Ts-Gba4-9pwsht542dhpcuzKVg8ve0wkN5BK1_YqzZJNR62Uv6_wqAiPsKpxU32mN7s5BDJ8u-QcRNsxk6mPFlacoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=aAsErgm01zKu-5MV1JQGtwTYx4WT5spG-nbp69rf6qdSIeArb8lrNHrJoVXkmVQ5QWpnIgZ_yDkqegKK8uiKvSVlT3xZExrCPMx1eQetWfdnhDFV1mCPx_EmZGPPrV63ZVzqTdu_3jJn4uVHJe-xWO_HYe6fAJNzV3zYEMDF4kUsmnPX0LJV4Dk0FxflQowp7yNdfTkcKXiEoqDbWutjk0M75kXKKjsBQvnMqc8g8pxz0n7T2P1It2TUzh_L6Ts-Gba4-9pwsht542dhpcuzKVg8ve0wkN5BK1_YqzZJNR62Uv6_wqAiPsKpxU32mN7s5BDJ8u-QcRNsxk6mPFlacoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYA7WLdMe8FtcxNLqft5ndwGH6eatcxS27Df8fUY_M4KL03wXtzmJsX__Uo9OACIbNrgO29IwatuHdjyoB_Efr_Ol-F_MjvMDRGMiHRaFhk1IBZX38IgfGuxeS1Ro60BMteK0MblR8MbogYNI2jGlYNBbbnAw1VJo7QgsKNFak7PLbIXSA3GA3s8eQIIdaQkW8dlOFpL7GnEBPtitRDlFzFSXDo2qkm0eZbzxjtbjh78Joca56V3KcmGpjJRliv3Kem0O3Vj6-qRc91rhfirxskZECVNdwEK1fE6HMOZUQMLn8ajO7lciYjyZPGJpOXnLOFSmPX-l9g_JOrW4lQ-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXtKQhnxRD8XVMu8l_voWIe9zwAxDyqzTHNyzWwxCHhLVmFycZ6q5lmh5odFKSTih30pwaVMLbr62JEXxtkHGNzCid0X9YtTlz4w36rBUJ2CamEK86KMVZvzJhO4WcX6JFPfMwD-BAF4PmBL0ZUoH0ngTVDmTSjjuLWkxgOaurgpkttjBpXY-Y6YiUrtdICVKjoz-fAV3IJsQ2DHdbzsA0AIGR9h4CXgNfbzYKLULQGf9-jdiA7zuGkmQ_7capR8E0siKhXoIwRo99aqrX_l8KNtj2j5XqiUzokSz0dOo90_T7wpl-cM_XI1AIVUFT1Cuume8_OL79LfAsxd3-lPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe_NSekPuvCnKRvPobmJHiVYCpgSpwKp066x4B5DYcVUSlz-FnnY80TqsHLUVN-Rc2OgzThTzsmIWHGqFPzxQx4ThX7TRuuWVBBxZslj9FVTGSZkwURDooxugspy5WWoPuieodw1lqpXimTeZ7R4z7mr4K0AAtN94rR6RWsNbuF7RbIQ6N49A5Q__vDbN77y1rX8y7r_bIcGjIUrVl8Qxc8XlSZfLMEsEdcdPKHwOpsUJPZHYjwxslxWLd9JEj1LpvRWLQJqktzknPekpUTXRCvF5Dx38sGLuE2C7P-oXezNd46LVBDlzlzx7NgauuT_cC94V7vDJ2nm2H5FGVnfZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAJY8kNC40ZsOOMfUv2HdB8cRKhqFv7XQbftmoxdksLCsxb1XQHO6sTPngjF0G1Jfwy90fUrCdgFk1rh0bkJEfj9Oz0ScQdXGkkkj9UwS4pteinE7aSh1QBCuPc2Vfh_jbJAN-bkPnx3-p3yz_ZgAaCZSqhXZ5GSAsv65rop4xXDeIRQ-69b7dZikk_Zl5vTs1E-DAFs2_oH0U9u5dpRWwBSKuieER5mociQ6zyXJpCPwFInTW2elVG_adRUcZ431nS4ouk4tJZkO6JrJthoMUOqk89s1eI2HCoQrJzXOFAPkENyftQXUxY9AaA-9YIFtQUFZcRpABSQg-I2_V4DYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUg4bXY9_aSUDNCUovMlqSukOvq37v8yEpbEdpRTGzuJp9Gi0ypg9WplmhEJc9XcLXVlNYgSxQdZZq1n71QwSrI1UWjh4JZ4niG-p3LVjMSsE9HqZRV44rlrXJ1KSl0HYLnwwhLU9NB8i3dIyBTi352bWU80G6QSyyPAbqucixNBx9ridWFIUQJa8woEzIs2GaSco35OY_RlKjChYmVigTazmPwkHVxbbupXcm-kD0PER_FrC2zny-kK7HydmWamSV76oqXGShB3AETbzbeS3bHzV6kIfl5bexIdSt9JLIDrKfZ5r6JzW4IudXgipvXYDIR-FRkmFo5dOCyrRj76AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T31Oer-inXkkWVNy42nXduwAYzAtgPBP_XZOkOnZNMpWtUdb9cGp3Q-L9pwUa0X6cPmzY8vqsAVs6PyMYXkNRxx7YTkEH9hH2d5N2qfAAXu0GKRn1AYGYiu5YoC3eCfgdIuWy31jigbDpq2VOrpIdKN_csx6IdImotuByQ9b8SALKKm7LVzceWDfh-CFw_bbxRfEEJQQPVyH5C8cEi29WOpBTUJmO6p5myvyiLhjfj3xTw7vslXHO8y1nuaBI8Jf-RG0i1XEH-Y9d2nSUDBweiGh-RkTrnMkpwh5sjG8wrjSwIjRFW7Xnz2zFDpis_7VvLx8IsPFX1hUgfWLqb4RFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DjWZhBBzDuUpE1MwqGmqJq5MbQK34xfcAvUpdZ8QvpSMeJi_Sfh6OkG_2hQTeuO1pSaCXlUwwtWx4_4WvuKg1ndn5c_rwAWeXr6PLXLoPn0WKh5ZngpnCzoeByExmsaDMhB3KC1AS89GUkW5zcAlRyEaDxXcPIf1ze01O6yr8PIe9nR7FTlIKSjpOQKXzAo8uw-EtuDyPrtQ_w6gI1Z4rcNQ-VsQIWLoWkqiXhvxWNRZn6cZR9WClrv9iXea5cYOq_CWTHaVJyeVdD-PxB2F15IbFeHL7PnVJ0j4KSmcelvVeM0FoPgEkt4q-7B4howubCbYbofKrq5iNXSqS_fOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DjWZhBBzDuUpE1MwqGmqJq5MbQK34xfcAvUpdZ8QvpSMeJi_Sfh6OkG_2hQTeuO1pSaCXlUwwtWx4_4WvuKg1ndn5c_rwAWeXr6PLXLoPn0WKh5ZngpnCzoeByExmsaDMhB3KC1AS89GUkW5zcAlRyEaDxXcPIf1ze01O6yr8PIe9nR7FTlIKSjpOQKXzAo8uw-EtuDyPrtQ_w6gI1Z4rcNQ-VsQIWLoWkqiXhvxWNRZn6cZR9WClrv9iXea5cYOq_CWTHaVJyeVdD-PxB2F15IbFeHL7PnVJ0j4KSmcelvVeM0FoPgEkt4q-7B4howubCbYbofKrq5iNXSqS_fOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH-vrAK3n9IHMEY_lZVKlIWIHrq3wPv4mnYUM7lVAF-T1CQ2kpahVLuQKVUOnXaDjvOp5sxuUy1AYUcQIEcWA3iIUL3vXXjvfvPTvd7caPA4_MoGT26GCA0Hkqr0Dp9uzWjLBd1Xjmv16MGk02mJfEEt1PB-LU9URRPX56hYDY01cSQH6k5WugpJfY7_qoLSLh_VWjcutx4-INumEM50-_V88-LiiVb6BqYLUy3gT2TkP6Bg9wZVM_YVUCuX_gDoTM2yn1lEALVxwpDO2WZZzbE_lrgL_sMuDPVq3C2e0x6pmGwm8CdyReKTKzY3CA7kRA4u5Bj2f3FaobPAL13d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2vaJjfJvaniqxZGvPleqfH_AYpFE5nY8bu1QMUbQvqg9kyjaT-E6_kajdaGzr9suX03EPQ6_dsolNo9qxVt3rJD3llk8t6kCaB7T1AjL4U1nGgcbw0j1CoAP4fTaeRkTAVlRbuCR3KYkcuqW5jibp0BGRCIm_8sPhhm2PdkCKK3ciH4LQXE7jKaAa-ZlqcyAXBlgTFSw8sj--myvQR61ISlREmB189HRjBV5oFzNDz0ZV6iLzgoHtG0x0gtaU-6wHYOr8MTTdeBZx_XJyFrboBilwwecm4nrQ2J4WBG8CIMo6t5-RZQc41jK55VjT8_NGp-fn8tjOfH5GVhgElPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsUsZJEraipwwUCynhXdECgKStFPWhkrR31PL-GZ4KZsqV-Xgd-i3G9TdVWdirNWdyf2HXBmwrJMBSv_n7Yqhc_cCSKiLWLKYmBg6IaGQ7oIz_KO7J215vhL8yuHvSElhdKJunX2rR3aHaLYqUPw59_3PxnUL57qsRozkMz7s0bYuBYJ09ePjzzBVRwmOEDGVI9OBHJMh_cK7PyBebyeFCCJFbzLPGGcjgu690EIdgRoLnPwINWV0-Paj9D8WsfQLxtyWH5i6dfAtFnKS9vD-geg22Um-O2Uu7AVZawWgb55HKfqO53BZNdFwDRdyxMapO2j5G8FjQKDZ7k1U_6xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D36tV5DeJf872-KLKu_0vgmRbddRPcVeX5FsdzRqkjhxQeKfbUtFOwr8fsuo0C-syuMmlxEDeP8ZK6aORC3RXgV6L_l3ATpG3a_tFEmtjaGGhpExrPpDUPyGcPILR42erxF4sL65dx-3DBdOaQpXeIKOKaxCr0RsueZakI98CWeYmwnsbfK9YJwSuEYfGRuK713BBJj9lEB_vI3AtEFMN7DBCK-NaphxI0lv2xwH6DkthaQhui95Gs9-rEw_9F_TjN1WMr47Au3VqyYFB3C6H9A_QEE9M9cCBKAAPEve4q8DE39GH84vEk9JkMr2KXwC3ROE6LQvBoszgB0hupWb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=P-bce-97gABycvctfne_FdCu10qLZPPbhRFvImXODO6UzEtVRC24tdrPsqKymCKYIp0dqR8DdosuF-LFvAXRorttyRV_sDX1yCpUYFnE8x4RwNkbAg7gUMy_KJrxhGQfAlIKQzl5ANOJTvcmGwSsAmxJRCBrb4JLoQJ-I90WXys2lHaamRhkT5GRaD9xeNB5qaCiFEFBsAmc6ywMCwbKoHg_JKL6YyNWqZSc9E3PBpgjX-0Hd4uSW_vJsWxJ8X0qlcesWHxo18q-kGEtQFG22StAeV-Kglol8tiT3xNCaKGWRDfasLjLjUECZNSbOgwolVjOiN_N8WtvXiTW07bWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=P-bce-97gABycvctfne_FdCu10qLZPPbhRFvImXODO6UzEtVRC24tdrPsqKymCKYIp0dqR8DdosuF-LFvAXRorttyRV_sDX1yCpUYFnE8x4RwNkbAg7gUMy_KJrxhGQfAlIKQzl5ANOJTvcmGwSsAmxJRCBrb4JLoQJ-I90WXys2lHaamRhkT5GRaD9xeNB5qaCiFEFBsAmc6ywMCwbKoHg_JKL6YyNWqZSc9E3PBpgjX-0Hd4uSW_vJsWxJ8X0qlcesWHxo18q-kGEtQFG22StAeV-Kglol8tiT3xNCaKGWRDfasLjLjUECZNSbOgwolVjOiN_N8WtvXiTW07bWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_-k0braoKBi8givp174fvm0x8zfsOoeb87LtdCeB3gVisbSOW7K7zDtBK2s7LIXtQXA9J1sJWS1gt1N2BEHCYHEuAnBD_M2w9LZj_QLkiaab0XwpOTp-fOYO0kz8Qu2yWckIH7v0chOld6_1QoVG0H-MzSJ1NE73r0MCq_LJcdrLM9975dh7RrQ_MI423aU1KeR78b3lI50WeORKajeonHq3SiyklZJ4hiBpGYLAX4Du-Ec29pCCTOUEM656lOymEY5xxXecCuCssHwjLGadr4IuIqtDAJNQzFUudsU7oUBNO4pNFlDnb_O1G98kX0UfpjxgKEjwBr2BO8Iw2lL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu9LDMiH2GY1fpyoVSl_cOeAPe2m9cfCGNXnGWoIoLYEYnq5J1Pgqg82JcIqxAERg41iyQLzfqL7rijyXaAwyDoVR-FfoMkbzWBjv8uLBTHT7BDjutdNp4TAYXk-mhjs2BnYM73QmClEGp9u9wINBpJOdrJRrwHsBqlsKRl13TUR28ywneWJGKmrUuLIIQY_YCosy6uxDLJXGY92SjjVniLhyoGJ74CaReQHLBeZt5vhQzeDkor54vS_hZTHJI2x7BydiXE3AcR3n1198ghl5bEJWF3npPi5YQY_nGPZdSwmsDv2nTw9IOI-2-tvTBZ6Ncv0l1eZo4ZRWlZXDyopHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozn2WRpqCgpIYJlW6vnSELxvhR43k-bVi454fQOpRMPPR3mJwBnrZreDc87Ng6V4NKB0OmyU-VJrRmmzitBDkTRGHm6Ws0-iA9dPSE6deG0D3OR5V3ZVet_k9phl3ssormEHydCSyXd9hvLHQV6yyUFHXVAEtPwR3Xthiz_qd-3_uibajUSM7VBnoyx5ejTQwy-ZozwljioYwrWtiBX7DPTZFoaT8lKibxyT_VfD9kayHXe-4VAnZP1UQNqOGKkt9hkJ4wFj7R4n5X4SbnEe_KZGLvaDmK2aqQ8OaJshOy3n0Tf9XwARVEpRb63dSUWMNQF3mERoQyJH7nDSWtU9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq0oG_gUX53459HlA--FJKXo-fuan5L7PeVtoL_SDq2A58j_Gv2sRHK_pVWcpwsPoBmy-l5U_wwYRrD1PmhaI4cM2kBwT0arFEbt35S7Fwyv3t1vUFndmzuRzjbecshfhLI92rhDA6YdCwJhQn3zW_C5O-kuRizwi67pAZTgGEG68koCWDud9lUXwbUywZS8Uc-6CZ2mnKpr7KoBeEMy767p5AhCfN72JerbhRTLQBjm3P5VXCKuNVSC4Dpher0VwLOTSwusySUfIGCsoe8V-nigPaZgdDzBfsti4hmfDpF2Ie8xqPVp6OAsmzmyyTmTPlj0n5jaZiavGlzlQZ9snA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvkPCmMySnlW4_xEdJNQIr6ZKPzSPm1vOBavrQux02NxsByoEnkfZjsUip6Wdu2RpkAdfPRuSnC-VRHe24tpgSABRfjOThBLKXI5XBDb_SvpjDCtAsmXIzUzsCKy6AM2oDYW65q02pq73_v_ES9ZtM7cxtuZNi9cJgRfrYYyOjhSCq9EKGQ1KY5Dfjv_Tqgg2rxkWYn8G-I5B394LaEbBKCaCL5NiV0z3HexFHv8l_YwAN8zuhlxqNUz3xs9iv99dn3WdjpdAvjhe18G9NbuRqvqrnF4zOiGCIje30UXUnENrIe44rbA55uYJ9wR4GDwDjvKHt3994z_dMGtuwH3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny-dlDRlnzLBATB0lKx93UY1Yos95HQwBTw0pSpXNHiwGsQyOIWjXCMg1urNWw_USqyeWGpWLuNL_EnOcr9SwKfMw63v-O4l-7XqHjzQ6NHV81qdBcwnl8bBgyzw3wWUVG0-Xz5xBV77XqoKBXwaxWGMewZudSmifzA0kZKcBdY0ExhTl4Oj86XSgu8oVwSQ1l3UOU5lW9uS-tmQ3xt9AHG37p6hW2QzixX_kXoC3c0-PWzU9kkfIJd_ckQ8f5qr_wGGZXv0iCmSqKXvQ6VCu1UqUoAfztg5orC7GjshbP84cHTycKsCzKTg-tU90pveEIRAUHicDm8gPYNwv106TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTJS0ZqeT5gsQnBRyryS24AATc2DuWJh-7lRYVGPUrZ6uEuxLeqF9SIo9Cx1AkAq24wmDsz9ETmQKlN_f8cCv7H57ZK4SUB8Rg500cPnXo3h1vyOqaXrz12XA4uLguRbiNUE6cVua_CY0QidjHEA97t9M2ffnOya3DYQOTnEiA9jRVOzbLwa7IC3KuCngT4vF92xcSkPETUBbADWNkQUemGEo2LPg7dfhv5Ccane7Ru_fv3MLdWJVR-rumxAvvjbuwrOslkQsMlYF4eW4AeN6LcZ5wFZjlofJ167h1rODgWLFVfOriDG7olUah1bBlQgNYFkMHl3QS0oLqjR9_w03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nk4eQTZDp28p5Kp4aOzFHCGUwVVlnlQEyC3X85zPX_OMxKNah6hUwK1VRE5QDy4RZxmC9U8fCbSffxepZain9F7yeyv71RXQ5zFADQkc9DBGWMEfDfctFWwyZE48uEDJTSVnlR_JMn68KH_Q-hghE2uNMwPSaeLi_Hop-pg6vXpyj4cGWaHoXJNM0olQnLMhovlFGowupxQc4TcKDcZ5WHfDWKOnCoKEHLTG_G1h2tD-aW1gvvBLUMQ_X2td_NPSLz6YF62Td8a2kAgwUeJFgiR8Zej6ZKEsiDeM3EFUBr3G9HDJdMF3O92MvhcCS03bFi-Juf0T2ufrBAb3BsuCMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=ZKnPWa6EbXZHn_yGeUDVe9xvZgetidySgVNqP41ez2YUp9X6FGWzzs6CafmrxtvCCnHKRdB9mLHfcLdVTNZXJqGinsJSbMRHbP9YD0XAwPCqeFpBCXgfaNXu8A2l6SXT2F3qmSRjuLn4-o3nAfYBd9trKQ41k4i_3BRjqhtidwnYaErLtFvXb2wkwYkyBFS-jlAv6cl9UePQdmzFNXdTfTbmcvVLZqLlgey2Bs9pQCrzwoxcLrAFVcpw71qZnGzCLwQReDUT-3utRChfuFitp_sP4bfdW1jHTxGDJ-11lzRk3nvxJQ0M-yNVbitfyj_EJMdLkHkY1OQIjXQDJnlfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=ZKnPWa6EbXZHn_yGeUDVe9xvZgetidySgVNqP41ez2YUp9X6FGWzzs6CafmrxtvCCnHKRdB9mLHfcLdVTNZXJqGinsJSbMRHbP9YD0XAwPCqeFpBCXgfaNXu8A2l6SXT2F3qmSRjuLn4-o3nAfYBd9trKQ41k4i_3BRjqhtidwnYaErLtFvXb2wkwYkyBFS-jlAv6cl9UePQdmzFNXdTfTbmcvVLZqLlgey2Bs9pQCrzwoxcLrAFVcpw71qZnGzCLwQReDUT-3utRChfuFitp_sP4bfdW1jHTxGDJ-11lzRk3nvxJQ0M-yNVbitfyj_EJMdLkHkY1OQIjXQDJnlfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QALikIVac8A7swF8jT4TmrSYHXWkEV9ESMK4m5nHtXjAoSA1WG3k9eZhlEDNUsSq4aKQK51b81WsHhMxtFippqVN5_b1PK_8mGS9pzfUTH3oPssXUXHjVBzqj1PS2x6Kc6_HQ_085NiCGPkEs0Dxn6H5LyMPimUhvW6tZiqZ4jJPJdDSKScUFy5Z8PgnA3aNEBzakEXi5emp9q0F0QupKkSMvZZuHVyGsdljGdGm8totAQYj3xsmOiyKhTU3MFO-AOxeLLKL2di0sEXsrRza6fZl9CHzaaZOiyr6v0jdou60Tn_4l6jEzPzg57LY8Q7V8abYtDCQ3OGPhMV1SY-uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=nJdv0bbR3RrkLywR2H7zxoaAlf-n_YCVwawo8ZqsRENHjTfSaJB8_Axvci5H4xxSaAItLgaoNs6nw6uTqnOX7xrkpnG8jhf_T13KY_jWgVgSv81PBCT39YLNaje7XmP0YIDcrKxEbsfwewKiDfoiTvSmmR0vk5RYtgM5Lfe0r7F01ff32sZ2IBs_ladXrht4cZP9URFgmctxUiPuUBQcBd_Uwqc2CmDT4BcYl1UJJZBk7teAWkHQ8ibrmzj55eInnhQ2avBSnaRoNu9l6wYOf3GRTE9Sa0d8bXrsctA_IwO5qiECLUzPqWu2AN-UR8ZL77-LFFNcslklk3iLa7bx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=nJdv0bbR3RrkLywR2H7zxoaAlf-n_YCVwawo8ZqsRENHjTfSaJB8_Axvci5H4xxSaAItLgaoNs6nw6uTqnOX7xrkpnG8jhf_T13KY_jWgVgSv81PBCT39YLNaje7XmP0YIDcrKxEbsfwewKiDfoiTvSmmR0vk5RYtgM5Lfe0r7F01ff32sZ2IBs_ladXrht4cZP9URFgmctxUiPuUBQcBd_Uwqc2CmDT4BcYl1UJJZBk7teAWkHQ8ibrmzj55eInnhQ2avBSnaRoNu9l6wYOf3GRTE9Sa0d8bXrsctA_IwO5qiECLUzPqWu2AN-UR8ZL77-LFFNcslklk3iLa7bx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaF6QkoFLhQLKmDyFqKGoxKrtVrH-tcn6dDU0NwVo1ceIL6KCGvaNU9imZ9WqDR3fEyRSg696oQ8gqLPqa-AZBKEsvan4W8DOLshkt-hxH3wJxVHFQTK0b636g56s_TXS3QQP-3BcDitQeZTFjmkRiwB74met3TClIJeP8nLAztaOcbGnwY92gwRIGzs0I4e-bH2FGDysqZduWKqpDPJyj1x3Y7sBzFl8N3JDWVQXPDB6vHn1W7so_4vVmlN9oIkvwNx24anev8oQ5sLuqOovlf18ooOxdNqiMxJ84zThJKl_8ZXuEf5wNUtoEKg2FiKK4Tj8CWR3g9bwuCQC51nUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=I_F4Mz2SPz_97AfRUozZIjAmRLcJoSPoqmNHNSiUQCIZOKu21RY2kCGwl4lPUuc_fyoGUc0WBKCgYjcSt4KWjPX9RSid2AGBTyPUbXLPPYnJx6hPXNETWXczl79fTJUYnPmRA2MQljhQXlLRwa7Wz6Tc6TS4oocoSitFZWrtbF78lXcNalvWsxRA9UPAaeiTutf7Kp2t5uOK3_HobutlIOJ7rj7gCuAPezeGlTa1ifDi7TttsmUNAq8GQ4bHbBUXo4P_QNnQAJceUAFa2M2qLRdwSiwHytdeCuJiXzu9MJomb1ThvifVzd_YwTz2o6lAHGk1RFnKKMOSmcR5hYsc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=I_F4Mz2SPz_97AfRUozZIjAmRLcJoSPoqmNHNSiUQCIZOKu21RY2kCGwl4lPUuc_fyoGUc0WBKCgYjcSt4KWjPX9RSid2AGBTyPUbXLPPYnJx6hPXNETWXczl79fTJUYnPmRA2MQljhQXlLRwa7Wz6Tc6TS4oocoSitFZWrtbF78lXcNalvWsxRA9UPAaeiTutf7Kp2t5uOK3_HobutlIOJ7rj7gCuAPezeGlTa1ifDi7TttsmUNAq8GQ4bHbBUXo4P_QNnQAJceUAFa2M2qLRdwSiwHytdeCuJiXzu9MJomb1ThvifVzd_YwTz2o6lAHGk1RFnKKMOSmcR5hYsc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=QGBRc7kOJvfwcb2ZiMFBTfQ6tetIDCLxkW041poAlRvluU7y-0Ae10d8E0M7hwN9KSXhYrtqwizSFZsDQRNv0PG-Q8KnPQIb-ffZQDKz-gkLZavRh4htiekOI8jXUZV5c8nxy8xHM9IRosuELK6yYqM0RIQFgWZWzRPGVuezIZ1w_vxhBb09qxqcylodJoF01eqHgWN3gjzL2t-4nTI66cS9KDgD0AP4fnNNxlUOCfUJ2JrN4-PYqbLtlECxPWTqGOsAqlaASymHrmJNfX5u2a2WJBH8UMa3VUQqAHAsfCmghX4h5ajfTVbbwoAP1MxjDyiJm0Aq7wWSVEiKRDR2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=QGBRc7kOJvfwcb2ZiMFBTfQ6tetIDCLxkW041poAlRvluU7y-0Ae10d8E0M7hwN9KSXhYrtqwizSFZsDQRNv0PG-Q8KnPQIb-ffZQDKz-gkLZavRh4htiekOI8jXUZV5c8nxy8xHM9IRosuELK6yYqM0RIQFgWZWzRPGVuezIZ1w_vxhBb09qxqcylodJoF01eqHgWN3gjzL2t-4nTI66cS9KDgD0AP4fnNNxlUOCfUJ2JrN4-PYqbLtlECxPWTqGOsAqlaASymHrmJNfX5u2a2WJBH8UMa3VUQqAHAsfCmghX4h5ajfTVbbwoAP1MxjDyiJm0Aq7wWSVEiKRDR2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=hvdAVNHu7BMIUAiKrHNbaG61yl10ubkDQTbqDRHgPFaTXhKWN0SR3g-3ubEAzeJMWyJ0Daj0c57b-fzMy6a81hxM81bA1RoW6KhkzcQfRDZPX48NVYHwnaZCI0jvlMNdZ-7R8sbfMDi_g7hMV4hbg6n7wwPgeCFZz-HqgHv612bwfm1ot9h3iKesDmoDoAeXYsMYdRE1yG_Gb-kqKdUxreRRH4EHlf9HfqEYLy1nAP5nbNTcqGmxqMo1n7TgiICN25A2VGVUXuFMaADi6oMeZoZzGQHWh9mXfsO_iTKZxutP8KDvvkNi-BrsWIwj9ydK9dloQq_ZQqXkYdbUJxqlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=hvdAVNHu7BMIUAiKrHNbaG61yl10ubkDQTbqDRHgPFaTXhKWN0SR3g-3ubEAzeJMWyJ0Daj0c57b-fzMy6a81hxM81bA1RoW6KhkzcQfRDZPX48NVYHwnaZCI0jvlMNdZ-7R8sbfMDi_g7hMV4hbg6n7wwPgeCFZz-HqgHv612bwfm1ot9h3iKesDmoDoAeXYsMYdRE1yG_Gb-kqKdUxreRRH4EHlf9HfqEYLy1nAP5nbNTcqGmxqMo1n7TgiICN25A2VGVUXuFMaADi6oMeZoZzGQHWh9mXfsO_iTKZxutP8KDvvkNi-BrsWIwj9ydK9dloQq_ZQqXkYdbUJxqlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFKe5XqmEw9SAtt5jhH2CDeVrYAJehcx22sCMAWuF0tc7coubFwfGNHZRY-NmPzsa_J9F5mgF03trQ0KoP6MqGHpoxGr1KgodE8TYbxpsLJkT_U-o789i_NBLACNWOHDSSlu-_WZhvD9bqcNrh9icP6iXViOZSpjuegrklD_P5ntIFcdkthyeiktBLBhQiu4f-VfSvRKF0TjzsmQ7n2fUrL4NCm6Gn5KazG9rPXVNpIvUNnFZvaHGwpAQC-kY6vynR5KqhdbMQ9OI14pKVlmolHksBl84NBrey45ImkLb5fz__lbl9qxH0FTM9HvaEdhIXRCUg35WnGLt3xp_6n5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSui7SvyyZ0XNh6XdJWjGszQX8Mr3g7nlaDtMEyl_xdjfFWFqnFZzb21cEeq_EtF11WqERt3Du8rZqMK8SnnP2sW92xHMvWGptYqkKd4WHfQbL4UR9XBLG68mnPpLeQRnG1EloVtmkpfpWhkW_uc6VPdEVHztCq1E6k6qmrX-q254m91XmQA6BTWBOvkZn6IwN0Mb_Mlmp7KZmPdjmyAoATA24LHsqx4ar2rEmKKKtMQjAS1mBHn37AvkUQQ2rUzAg7MtgZe-f3WQq7l418u5zvU2wwNLvWKYluQz-L0LG2chB6JUx9_g07oIPXuNIFe4xkxcICRSNEH2_21Jvoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDRd0SuQHKVRWeljI79PUQwCnENTAHNeeBogq6goZOD5awMww27wD7wvwHVYtntQuS7nYeDz5jeWBBwQukbWbFThgXP6GlCPCXj6aHy5u6iPZ1L7oLIbMrZ1LJXUJKoOXLAtcfWW4mdmkPJWl5Jg7ex_KMW9UT3M0oB-Ca_89RNOog9JkL9c770NwdNvq0dwVqI2ZG2WVhHJGaTQU_SQipsp8cc9YnSwUNy0zjNjbzk1vPu7PdG8rZ5dEtLe__3rZPgeU7DjkBPThfocbliQ5HPalwJEBKBLO62fqyBsnz5KsodU6S6IlcaXBPOm78QRWaN74U3eA8tja6lJHVKhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT_Q-rG4dyAl0tDSDw0Bdkhcz1QKtzyXTuWgzU1wqjHzKRUnlhJ2EcvrX1IeiWPDuyV_1kLU2O5wZvJwcJkH_BabakFh6AqLJHFHQw3j-AIRJ_ZwNi--W8mwSrTwO4FnVErKNTzBOQMbUQUoESTwf-46HQ1PIm2ZcKntDDjO3CGWiCYa5YwQE4dhaHklPANZ--0pm3Xoje0HcEkFyf0VqeetJzfR0kRKR5_aW5dZiDRVwE9jCInetXfeU4ehpZomzcH-rOSpC_dbSupUfRg9U0uNDtgngVf1vwVQ9WoCEMV4a9xn7Z9HyYUqrhRH5he9P7TCc2e7CK7FzJNOq-4TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=Jc3NlZ33Moyj_iRoDAKSlGgg10-bgNhjjII2lx8PZ1BOZ-53zHy5gVcLDjKlXpcaS7F1dRegC58yIzeFYZeEE4khmCXxfxy5t3ST6Kr8pJee2NxehNoUHDgf8QWUNDZm4WKtChRb4RCMUu3mwtR1jNsDrkONcl8dKadvX-UKyycCK9BZl-CRkzHgs4dfqtQqxpLhMVb8pu9NH19-g2BZF1GgZForfRtg8A2Hxg72yrjRaRAuae4bMja040F37SR_RMeSDFh3L1uMpkv2voXdOM8dzwGqFA-QiDafuKF4HRXqq8oBV7Q1KKm7D5QHGdf0rdPNNfDIxbFsnVnv67DZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=Jc3NlZ33Moyj_iRoDAKSlGgg10-bgNhjjII2lx8PZ1BOZ-53zHy5gVcLDjKlXpcaS7F1dRegC58yIzeFYZeEE4khmCXxfxy5t3ST6Kr8pJee2NxehNoUHDgf8QWUNDZm4WKtChRb4RCMUu3mwtR1jNsDrkONcl8dKadvX-UKyycCK9BZl-CRkzHgs4dfqtQqxpLhMVb8pu9NH19-g2BZF1GgZForfRtg8A2Hxg72yrjRaRAuae4bMja040F37SR_RMeSDFh3L1uMpkv2voXdOM8dzwGqFA-QiDafuKF4HRXqq8oBV7Q1KKm7D5QHGdf0rdPNNfDIxbFsnVnv67DZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
منابع ارتش اسرائیل: آماده سناریوی حملات گسترده حزب‌الله هستیم
بر اساس گزارش رسانه‌های اسرائیلی، منابع نظامی این کشور اعلام کرده‌اند که هماهنگی کاملی با آمریکا برقرار است و هم‌زمان برای احتمال حملات موشکی یا پهپادی گسترده از سوی حزب‌الله به مناطق مختلف اسرائیل آماده می‌شوند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6165" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
💎
vless://1b5607ba-c295-43f8-923a-dc633a099276@82.47.63.98:8443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=farsroid.com&mode=auto&path=%2Flokayb&pbk=US5uDp2cCip8cEuQUWEf4o7VbASXg45EeVia_Kz2QTI&security=reality&sid=fc0f43e6354ef57b&sni=www.qq.com&type=xhttp#%F0%9F%94%B5@ArchiveTell%20%7C%2050GB
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6164" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرکت Wizz Air اعلام کرد تمامی پروازهای خود به اسرائیل را حداقل تا فردا لغو کرده است. برخی پروازها نیز در مسیر فرود به تل‌آویو به مقصدهای جایگزین مانند لارناکا هدایت شدند.
در همین حال، سازمان فرودگاه‌های اسرائیل اعلام کرد که فرودگاه بن‌گوریون همچنان به‌صورت عادی فعالیت می‌کند و پروازها طبق برنامه در حال انجام هستند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6163" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📰
گزارش‌ها از حملات به مواضع امنیتی در ایران
بر اساس گزارش‌های منتشرشده از منابع ایرانی، چندین موضع و تأسیسات امنیتی در نقاط مختلف کشور، از جمله استان استان همدان، هدف حملات قرار گرفته‌اند.
همچنین برخی منابع وابسته به اپوزیسیون ایران مدعی شده‌اند که تعدادی از نیروهای بسیج برخی مواضع خود را به دلیل نگرانی از حملات احتمالی ترک کرده‌اند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6162" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪سرعت فضایی.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/6159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۲ ترا
💎
متصل رو همه اپراتور ها
✅
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6159" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=ZqLDfEijzOqr2w6wFQGByM5lCSOaR0JDpREfEjsTqPNHOeyljMmdQ8Loqt7Qvi5DPEDEoAI-rrqSx8npOqVb7h05lhPSs2xoVdMtKGSUkSTpCQQx8BKZoVDsZWbqe691jpdXoS1-y2FTWdpnDFbF-6D8BNMFzdNKxCxaEGYdOXhsE91LKlh1-3yNbx5RQWEuauyTBYQjcvH47XjPu57ZZ51JiGuXAm16HsqW4davgDD2HfYXPH1j8SB7ICXAAcP55AlyLe80A0c_ZcjiH7MrZDkpyvFOabUuSvzcZxNBGh_iV6omduP0C62ea-TFCvzmrDMJYUIJ1vyQTdeJls8p6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=ZqLDfEijzOqr2w6wFQGByM5lCSOaR0JDpREfEjsTqPNHOeyljMmdQ8Loqt7Qvi5DPEDEoAI-rrqSx8npOqVb7h05lhPSs2xoVdMtKGSUkSTpCQQx8BKZoVDsZWbqe691jpdXoS1-y2FTWdpnDFbF-6D8BNMFzdNKxCxaEGYdOXhsE91LKlh1-3yNbx5RQWEuauyTBYQjcvH47XjPu57ZZ51JiGuXAm16HsqW4davgDD2HfYXPH1j8SB7ICXAAcP55AlyLe80A0c_ZcjiH7MrZDkpyvFOabUuSvzcZxNBGh_iV6omduP0C62ea-TFCvzmrDMJYUIJ1vyQTdeJls8p6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📨
پیدا کردن اطلاعات از یک آدرس ایمیل - این سرویس ردپای دیجیتالی آدرس ایمیل شما را در منابع آزاد آشکار می‌کند.
🔥
حساب‌ها و پروفایل‌های عمومی مرتبط با آدرس ایمیل شما را جستجو می‌کند.
⚡️
منشن‌ها و سایر داده‌های عمومی که ممکن است به صورت آنلاین در دسترس باشند را نشان می‌دهد.
💥
به شما کمک می‌کند تا ارزیابی کنید که جمع‌آوری اطلاعات در مورد شما از یک آدرس ایمیل چقدر آسان است.
💎
فوق‌العاده ساده است: آدرس ایمیل خود را وارد کنید و نتایج را ببینید.
🔗
https://behindtheemail.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6157" target="_blank">📅 09:42 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
