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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 353K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار مجدد بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/withyashar/17062" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدای ۳ انفجار بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/withyashar/17061" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
@withyashar</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/withyashar/17060" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان بحرین : 4 حمله به مقر ناوگان پنجم ایالات متحده
@withyashar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/17059" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه : تنگه هرمز اکنون به طور دائم بسته شده است و ایالات متحده و متحدان آن دیگر هرگز از خلیج فارس نفت دریافت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/17058" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.  @withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/17057" target="_blank">📅 11:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آلارم وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/17056" target="_blank">📅 11:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هم اکنون وقوع سه انفجار مهیب و پیاپی در بحرین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/17055" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">همین الان فعال شدن پدافند مهر آباد تهران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/17054" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=qeVnIwwviB78iA4FKVrp9FIlQDlVtBak-tMNRKIHliOien-6g4TvC8nTR8o-tt_70PjytW1H-jiZbUPTqcHiiaCJmyjn-2PyERDo_jivldAu4hC-fZAFcffQ10Iv8WkGUAA61pA2kGmT5_xhTBXqZo0K0oB9G8QuOgNVIKIE7Cq1Rt4PZa3eSxLQYeYEnclivVkQNITNWC-qZgvhFgELXZGoZN_5T8JBKk7Jy95RZ8oG31DGXFw0nNk_jmcs0qaB8H1e2XSy9GqHPrPrCcEyvFGbEaM6WKlD4serke6g4MEPvKuCFbYmHTJfjUEWIsQEe8Rv7EUCg8EdvjQR98lvdS4kVabf6n0XswqwwboT1D1vkCxwNb9_3cbGy_EM1-oFr_H__niLLXuW2_upnWUFbchtpdjDGjO1CnbAdN0yIhH395tgc3jVvGdXWfihjSO0KiOOGu196nmH7LIa6NhBE7AwyppFBYeGqc9FotWrlL6zrZ--zPwIPD3JChG68MEhKmG19lFJ1zxh3ecXwr8QSRJJy84nf33pmxE7pnyIBxaJ-c6HVFc-L-w8Key12UQaZUaJiHq2NnU7JKrt6BZd9h6uewuD1Dco9lJ93Co6Mfoe-2sOmq6otnXMvdnppHmLu-fmJi0CRd4j58ueoLxIJ6-5t-HA2Cgd_u4hiFzTtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=qeVnIwwviB78iA4FKVrp9FIlQDlVtBak-tMNRKIHliOien-6g4TvC8nTR8o-tt_70PjytW1H-jiZbUPTqcHiiaCJmyjn-2PyERDo_jivldAu4hC-fZAFcffQ10Iv8WkGUAA61pA2kGmT5_xhTBXqZo0K0oB9G8QuOgNVIKIE7Cq1Rt4PZa3eSxLQYeYEnclivVkQNITNWC-qZgvhFgELXZGoZN_5T8JBKk7Jy95RZ8oG31DGXFw0nNk_jmcs0qaB8H1e2XSy9GqHPrPrCcEyvFGbEaM6WKlD4serke6g4MEPvKuCFbYmHTJfjUEWIsQEe8Rv7EUCg8EdvjQR98lvdS4kVabf6n0XswqwwboT1D1vkCxwNb9_3cbGy_EM1-oFr_H__niLLXuW2_upnWUFbchtpdjDGjO1CnbAdN0yIhH395tgc3jVvGdXWfihjSO0KiOOGu196nmH7LIa6NhBE7AwyppFBYeGqc9FotWrlL6zrZ--zPwIPD3JChG68MEhKmG19lFJ1zxh3ecXwr8QSRJJy84nf33pmxE7pnyIBxaJ-c6HVFc-L-w8Key12UQaZUaJiHq2NnU7JKrt6BZd9h6uewuD1Dco9lJ93Co6Mfoe-2sOmq6otnXMvdnppHmLu-fmJi0CRd4j58ueoLxIJ6-5t-HA2Cgd_u4hiFzTtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای جدید، خسارات قابل توجهی را در یک پایگاه نیروی دریایی سپاه در بندر عباس تأیید می‌کند. یک آشیانه آسیب‌دیده، خسارت به یک سازه در امتداد جاده و ضربات قابل مشاهده که بر دو اسکله تأثیر گذاشته‌اند، قابل مشاهده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/17053" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/17052" target="_blank">📅 11:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود ! @withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/17051" target="_blank">📅 11:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درود وقت بخیر خسته نباشید چرا حملات فقط شبا هس؟ روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/17050" target="_blank">📅 11:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">درود وقت بخیر خسته نباشید
چرا حملات فقط شبا هس؟
روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/17049" target="_blank">📅 11:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با ترتیبات ایرانی باز می‌شود نه با تهدیدات آمریکایی
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/17048" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر دفاع اسرائیل: ما از هیچ نهادی اجازه ای برای ورود به لبنان درخواست نکرده‌ایم و نیازی هم به اجازه برای ماندن در آنجا نداریم. ما خواهیم تا زمانی که حزب الله در تمام لبنان غیرمسلح شود.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/17047" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17046">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد، این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است. @withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/17046" target="_blank">📅 10:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=calYZNM-QsGPRHVO5hf52Btn2P4xHeQeAJc2yqj8S2esFkoPIkELS32JV_hPKWy8Zb9c45YwJuT0nYqqmPm4SKg7Irtx1qI_ZvPEYaXD4tJk3gGpqk_ZXqZQdpScGrD9BdirXBlv1U3Lev3B7ehzmT_Ir6UhVXn3vPJ5KvtG8_tsBKTDk1bOaOOXhjJgqg7G-Qll-2vEi5GFOaKNuxgr5IuncPwK8nkm0c-IEpc7Wiv2mAlDcpGcBJE4Z6N2v88WYovcwgwglktWRuD9Pnrnt4qL6XCagLxXhj7z2mizzbqJVzJvJwjRdJFb0xmzgQv8lXQj9Y2BSNi4lzG55kMWGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=calYZNM-QsGPRHVO5hf52Btn2P4xHeQeAJc2yqj8S2esFkoPIkELS32JV_hPKWy8Zb9c45YwJuT0nYqqmPm4SKg7Irtx1qI_ZvPEYaXD4tJk3gGpqk_ZXqZQdpScGrD9BdirXBlv1U3Lev3B7ehzmT_Ir6UhVXn3vPJ5KvtG8_tsBKTDk1bOaOOXhjJgqg7G-Qll-2vEi5GFOaKNuxgr5IuncPwK8nkm0c-IEpc7Wiv2mAlDcpGcBJE4Z6N2v88WYovcwgwglktWRuD9Pnrnt4qL6XCagLxXhj7z2mizzbqJVzJvJwjRdJFb0xmzgQv8lXQj9Y2BSNi4lzG55kMWGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام. من با قطار دیشب داشتم میومدم مشهد از تهران. ساعت ۳:۳۰ صبح که قطار توی نیشابور واسه نماز وایساد، دیگه حرکت نکرد تا ساعت ۷ که گفتن پیاده بشین و با اتوبوس باید برید مشهد. مثل اینکه ریل رو توی یه قسمتی بین نیشابور تا مشهد زدن. الانم سوار اتوبوسیم و هنوز نرسیدیم مشهد
😔
😔
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/17045" target="_blank">📅 10:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17044">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPkPGEcJ6RAKhKenOWESIrZiw8FPspKMhx3CgYWVDvQTIZ88ELFXsQob4DsLcCy8xHxbiCZJX-D35KrHWU0xJtyNUo1be3GFj_GMfWxHUgmdoTl0f2Xx262rFUtUGEiicS1-Y3BM3q0bhw-FR2l_WPK3ddUx8mLK7t5SvqPuv6OntZ0JVwHLqXbTAWqh_4uOocrjdN8OuufjdNU4RH3MuBJ47CICS7bkkdggbVt9MCNvrys9E8bguP3zHgAZDAW4Xdnoe710pTkJsDDCWapR3BI8YscARiVLTDs4jhhxX6bHrdAyGgmS2-B2MxwZQoXbpZkUYct8W6KqUlXS4H2-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان : آتش‌بس رسما تمام شده است/ احتمال انجام حملات بیشتر و فراتر از آنچه اعلام شده است وجود دارد
همچنین به نقل از یک مقام آمریکایی مدعی شد: وضعیت مربوط به ایران همچنان بسیار متغیر است و ممکن است حملات بیشتری فراتر از آنچه اعلام شده است، انجام شود. ارتش آمریکا در حال حاضر در وضعیت «انتظار و مشاهده» قرار دارد و اهداف حملات امروز، موشک‌هایی بوده‌اند که می‌توانند علیه دارایی‌های آمریکا مانند ناوهای هواپیمابر مورد استفاده قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/17044" target="_blank">📅 10:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17043">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد،
این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/17043" target="_blank">📅 10:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17042">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باراک راوید ، آکسیوس : کاخ سفید در حال آماده شدن برای چیزی است که می‌تواند به دور جدیدی از نبرد با ایران در اطراف تنگه هرمز تبدیل شود که چندین روز و شاید حتی چندین هفته طول بکشد. مقامات ارشد آمریکایی به من گفتند که مدت زمان این کمپین جدید و شدت آن کاملاً به گام‌های بعدی تهران بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/17042" target="_blank">📅 09:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17041">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=T08kOAJQfWZlwA0lJ_qpBWsgj04Iw1WFItseegaxqBwXDRK7ZoAwmxeDpFv26TIqka2Ej64IrStiXdabEZ2qCU4AnU4e-XI5lmY_zWeLcW71T7KSAdbUxDFfrx5zOZm6RgO0KPJkB194BZQirhu8sLD3DftaFokO18YSchN1ukVxhjlHsa4z4iJkWI22wc5kZP-ns8c_-TATn-JXRdynpNJbJll5EhtyJsmDnAP1ssGQHDfEArvAMsxxVyRIUschDEvdo8ViAEDmoehPQi1OtBbXJvsgFnIsyTHQvWi0kQyCxaV_6Ztl7X1khCmE_ozZESRpL7vMtuI7i8_dT19gZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=T08kOAJQfWZlwA0lJ_qpBWsgj04Iw1WFItseegaxqBwXDRK7ZoAwmxeDpFv26TIqka2Ej64IrStiXdabEZ2qCU4AnU4e-XI5lmY_zWeLcW71T7KSAdbUxDFfrx5zOZm6RgO0KPJkB194BZQirhu8sLD3DftaFokO18YSchN1ukVxhjlHsa4z4iJkWI22wc5kZP-ns8c_-TATn-JXRdynpNJbJll5EhtyJsmDnAP1ssGQHDfEArvAMsxxVyRIUschDEvdo8ViAEDmoehPQi1OtBbXJvsgFnIsyTHQvWi0kQyCxaV_6Ztl7X1khCmE_ozZESRpL7vMtuI7i8_dT19gZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت
خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/17041" target="_blank">📅 09:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17040">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ادامه حملات پهپادی ارتش به پایگاه ها و مراکز راهبردی آمریکا در منطقه
روابط عمومی ارتش:
در پی تجاوز ارتش آمریکا به مناطقی از کشور و یگان های ارتش و در پاسخ به آن ،  ساعتی قبل و در ادامه حملات ارتش جمهوری اسلامی ایران به پایگاه های آمریکا در منطقه، سامانه پاتریوت در کویت، آنتن ماهواره ای(سایت اخطار اولیه) در قطر و مخازن سوخت ارتش تروریستی آمریکا در بحرین، هدف حجم انبوه انواع پهپادهای انهدامی ارتش قرار گرفت.
نیروهای مسلح جمهوری اسلامی، تحت تدابیر فرماندهی معظم کل قوا(مدظله العالی) با اقتدار و تحت هیچ شرایط اجازه تحقق اهداف و آرزوهای رییس جمهور نابخرد ایالات متحده را نخواهند داد و تا پیروزی نهایی از آرمان های والای انقلاب اسلامی دفاع خواهند کرد.
‎
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/17040" target="_blank">📅 09:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در پی حمله ارتش آمریکا به مناطقی از جنوب کشور از جمله چابهار، مقامان منطقه آزاد تجاری چابهار تصمیم به انتقال خودروهای وارداتی از انبارها گرقتند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/17039" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد. در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/17038" target="_blank">📅 09:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=YyLUxq9FxC-ktpyyB5s7M6-4O4s_GFG1Oq63W7O3JvHa3-vTqLDXO_bpXQthMMoLdPXJza5uFDpZ8YVsgovXpl_l59y21KfZoWYg8vrmqAqXUzMLvdvANd5OMPkU_ADvWV7JFccoVsz2x-iED0TIUpQDuploPRhG0zES2XhZSNgCRqFDtyR_5g3vAfw2_WpXRz6mFUmFZr4N37hw99Ls3xgA-xzjUmq12ZLEAjbmB5fi0Dhlde1-w9L_rwMJmic-aVFHWGEjzXWImnXeHq1I6N53BHHIuih8zhYvzMqjO7Pu72iszIOnk_qtt16mJafHACFabEJ8v4dGWog6mleGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=YyLUxq9FxC-ktpyyB5s7M6-4O4s_GFG1Oq63W7O3JvHa3-vTqLDXO_bpXQthMMoLdPXJza5uFDpZ8YVsgovXpl_l59y21KfZoWYg8vrmqAqXUzMLvdvANd5OMPkU_ADvWV7JFccoVsz2x-iED0TIUpQDuploPRhG0zES2XhZSNgCRqFDtyR_5g3vAfw2_WpXRz6mFUmFZr4N37hw99Ls3xgA-xzjUmq12ZLEAjbmB5fi0Dhlde1-w9L_rwMJmic-aVFHWGEjzXWImnXeHq1I6N53BHHIuih8zhYvzMqjO7Pu72iszIOnk_qtt16mJafHACFabEJ8v4dGWog6mleGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد
فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد.
در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور جدیدی از حملات را علیه ایران تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را هرچه بیشتر تضعیف کنند.»
سنتکام در خصوص اهدافی که مورد تعرض قرار داده، ادامه داد «نیروهای آمریکایی به حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17037" target="_blank">📅 09:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
راه آهن جمهوری اسلامی ایران اعلام کرد: به دنبال حمله  بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می شود در کمترین زمان ممکن این مسیر ترمیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17036" target="_blank">📅 09:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17035" target="_blank">📅 04:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17034" target="_blank">📅 04:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq_EXiUq0rjEObLsta3yF0yiZ9LcFgwSm9r6ne-Z_BlwJ_u6UrQRp2OT2g5188Ym8hYbIS8z0YYI_TI-KJuAZK3AhYAr0mM_cD6i7f4Ae8bP1A_-Nx5uvOi75v2B8W_oL4mYSydh6hp2R-rleNsUbQwPSsVeOwpBIiHfRuCxq4CP1ACIPLFqG8f7FsV03ZWyiPqbKZypVDtYUNsc3YoIMTmwRG2O1-1JP2JNPeypglvjIHhdM_Sujwnl3TXsQk_nhKffsjeEQevx4q9iALmoGWYcJwWE9KA8_ZAu7hlkbcScnY3aCRmVjnAZDhvjhCidE5MzijJDAvRrRbJrdhyxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک ۷ تا موشک از سایت موشکی خورموج بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17033" target="_blank">📅 04:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG01WlyL9YxIF01sojQX6z9-h7xbCxbZph18NwTH-C-REbzPJFflgF881hMuIfTqp2WEhiaGHRyIADQxLDXIKKtBMd_-yeTsBPHVLjRZA2Xn0hsn_SEM-0-LmJA-LKmeQ6fo1WigFqwUqEYYWrjkhd7eNjxxrHGLCmuAD19pGhARp45XAgQQvdK2dlchpryQ70gf2Hdg7zhTBkU_3yPizG8Zw6MWo_nM0js887uMhJBh3d-miouEGUWSOeP8paqRF9mj20PNFDmNg8LFyi6dS_Xnf7apjImBwrsEeb_4FaUsDa-_1WWl2AHLrQvlSvZkk40-U6isywad9R7VcysDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از شروع حمله ۳پا و شلیک موشک بالستیک از بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17032" target="_blank">📅 04:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : ۳پا یک پا هم قرض کرد و حمله رو شروع کرد
😂
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17031" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بوشهر دو انفجار دیگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17030" target="_blank">📅 03:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">از زاویه دیگه آق قلا @withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17029" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=Adn832l3xlOBYWvAzv4Eo4MQg7FtpTzRkTF8WM-6m1vmAJnNGH59mn2oevaTp7l3jKpVxgEw8QlcxjpVaOpuV-eXc3pEfX9PqObyzO07ocClZ3ilHH5ToxE6-wh28OjXlVoqcjVhpdPMupgSYcmb2taqQ5bpFMEhL0_zNUbFy_trkFya0d5uvqDCDeqjluP_7wE-M3kXU2VEuV9w3gtTfBwDxF9Yh_Zo38mJdszkZSUjhxFMD0XQS62LkbqiqcD0M8JE6e-E2x1PVyiRmHktEU03a7zJeK-cRcR5AfSYyEK1YyFHi7bpDGF5cqb1KC4t7ENO2qLz_CM8R8Y0Pi487A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=Adn832l3xlOBYWvAzv4Eo4MQg7FtpTzRkTF8WM-6m1vmAJnNGH59mn2oevaTp7l3jKpVxgEw8QlcxjpVaOpuV-eXc3pEfX9PqObyzO07ocClZ3ilHH5ToxE6-wh28OjXlVoqcjVhpdPMupgSYcmb2taqQ5bpFMEhL0_zNUbFy_trkFya0d5uvqDCDeqjluP_7wE-M3kXU2VEuV9w3gtTfBwDxF9Yh_Zo38mJdszkZSUjhxFMD0XQS62LkbqiqcD0M8JE6e-E2x1PVyiRmHktEU03a7zJeK-cRcR5AfSYyEK1YyFHi7bpDGF5cqb1KC4t7ENO2qLz_CM8R8Y0Pi487A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان هوا فضای شهر چغادک ، بوشهر رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17028" target="_blank">📅 03:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">همین الان شهر چغادک رو زدند
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17027" target="_blank">📅 03:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17025" target="_blank">📅 03:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724fff2286.mp4?token=IDy-97_JQnQB8rS6cCNNQOJ9AIhBPPvdmwg75EB_YV_MgH2_RvuLdg2n9dFxWduQx5FK8LhK4dSLsSL5RAR69YoZuS_gN7f-sbrP3gejxzMS46f3XvKepOXPVZuNgfWM14ux8Zwc60THoH-ucMyDmN-8i0goHUqS_pQVSjHk8oAcrQnnjiCl5o1wnUUVDLP29Qs_MD2NH6-IsJySFDmKrNrlauTWCbtZzveLuIH8b1U65iZzIjS0VkfDP-oaBYzT4lMzotnOhDy6aXDn37W478mZ12jExW6UpcgtCHJk5Cr-ZXXJU4mY7VIe_Z0gPj-1BzUbLA3HZb5i2Y85HWz9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724fff2286.mp4?token=IDy-97_JQnQB8rS6cCNNQOJ9AIhBPPvdmwg75EB_YV_MgH2_RvuLdg2n9dFxWduQx5FK8LhK4dSLsSL5RAR69YoZuS_gN7f-sbrP3gejxzMS46f3XvKepOXPVZuNgfWM14ux8Zwc60THoH-ucMyDmN-8i0goHUqS_pQVSjHk8oAcrQnnjiCl5o1wnUUVDLP29Qs_MD2NH6-IsJySFDmKrNrlauTWCbtZzveLuIH8b1U65iZzIjS0VkfDP-oaBYzT4lMzotnOhDy6aXDn37W478mZ12jExW6UpcgtCHJk5Cr-ZXXJU4mY7VIe_Z0gPj-1BzUbLA3HZb5i2Y85HWz9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل ریلی کنار پل دوگونچی آق قلا استان گلستان @withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17024" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام همچنان بیانیه پایان عملیات امشب رو نداده
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17023" target="_blank">📅 03:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFpm2ka8Sc2md5bTl878GsT6GxABq-Jav16Lt1PATAJ_4oqivxR-r9yJfVW2Si9-QE1IVLTH-eJq6ND9D124ztuHXwpO3rf2BvhtquhnT4nqseE6OCcSVAA3uFMFKDr_KAYUGFJgwSCNehgAGnF9kxpINbHI5PSfKd1A2x6AOGhAW-FgsGa-Sag1hQKDOhMhxJdMIlDtPJ8_-khU3F4qBVE9n4liUij-mmuFi7saGv0DRMUDVq77Wvh60C9Sv-qMLE-Su7FbcOOT5h2jfLm5q_ZvFO8go_7O3ZSaFKx0zPHfFfeLFoBcOxKcaTZIq0_TlPMtu1D5cNpSKUII9zFoYO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFpm2ka8Sc2md5bTl878GsT6GxABq-Jav16Lt1PATAJ_4oqivxR-r9yJfVW2Si9-QE1IVLTH-eJq6ND9D124ztuHXwpO3rf2BvhtquhnT4nqseE6OCcSVAA3uFMFKDr_KAYUGFJgwSCNehgAGnF9kxpINbHI5PSfKd1A2x6AOGhAW-FgsGa-Sag1hQKDOhMhxJdMIlDtPJ8_-khU3F4qBVE9n4liUij-mmuFi7saGv0DRMUDVq77Wvh60C9Sv-qMLE-Su7FbcOOT5h2jfLm5q_ZvFO8go_7O3ZSaFKx0zPHfFfeLFoBcOxKcaTZIq0_TlPMtu1D5cNpSKUII9zFoYO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل
ریلی کنار پل دوگونچی آق قلا استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17022" target="_blank">📅 03:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUR3YxeZO_F-1hLnX50Ql_MXn-ehet7t4NaJkU-CiSArG-mAXz9-gQhhweojaP2bUz7b-XJWdmnyPiAou4upc5grT5RkFR2zo8gu04lIvCPse1sv16RuTwzdNKcNNk-aqAiwSiFCB010EEUKgq-QYzM_u5vBWENluCCzp0ADz-CrkUzkilJIwkRbpFC4yUbh1gmgdf0etQSphH6LGXwXWEiwiSCJGRnpQNckrHVEwPPHiEXP3m__mewMJQRVr1hKIWlZtGd6RI1KOJGt-Ud3TUJVxedizqWUqbzJEqbz-8vKOEw5AooO_h-7dvF8kfWr53lqEn5A8zPGGcfklH9pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsvwn-NFZAtrBV3zDgNeHaBlfjH1rbrGCgHP73Um_YN-3bhorqlujMN_nHC0HhVqFJmjnlfxqaMUMN20tP05NfhGmqui6TVViaf02ozPSd-X3zERmkGpuprbi9mn7hGpqoAir2VrcuNzQwnEICZoVKHebqYgdmPRtxk5Ph-yG8wGAuffbxM2HsL3gwlWa719-RdDj97BN6tBFgFZCR4ioCGi8fZV038gibwA8HQQtER6xN_b8eSxqp-LRJabEscB3jzmGr1vP3hrkfPypd34ZcU49GZoBWyz_Rk4YNfySTb90qKm3TsDb9GRJzirkwHFHp-VrFur3mH3yPej8vZoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJjfs7pcgNKSr6zRaE3svc0mlhZ8KBpgGS4rpOzc5-O8JPuMYrtpgQmwV3hgY8efy-MlphGYIPE4zvXnvroMLwPHWzZK4h4AS4mRJjaL-yh5tuDEC_90WncpUUhm74DWtUms1U6CM2oxPwt3TZ-In71XNeUS3EKyk9hQrk86z-NlPury8SVAzFoqup5LTU53F9avt4ysiNXdkGHHoGVDoZ0OyqiZiocvazUdd8daxSfrWIKMdANPEVbQCcTIttUXoQWqb_qQUk9MLUQprhj-Z7VkQa-UM_7kl_v0UsTlNZPiWmFu1WM5WkpA2r37_tX2N_i3wu1_lpkvHV3ee1tdIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های حمله به راه آهن آق‌قلا در‌ استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17018" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=NGyoPCPJXRpZuevyRFH2RGzI185D3TVC8cdsfu5_9GBEHG_1XQQQnlmaSJ__DeMcBNqo0Vjlm3uEVSMjw7LwdGs_aJEIqxW9ceBuXL4k5l6suY5ibLOE2f1rQQE8AYQH1CGpUytT7xBGUPRNfk0-NTynkhkpj9H_uULq7YPZcmVydiJNkgG9Fp_KM4O57lZ6sj6_ksj4tAvYCCw-26B-pdciklLlrvUIYOZUkXaau62JFjTTHbM_81WRMyNNFXK_dq_St0-f2KpEchNA3jnqvqUHWWC7GlDPBN_yBhGLez74EJ2lA_F5MgRS6zEG7DimR4wqMP504VOjSEVmUeAVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=NGyoPCPJXRpZuevyRFH2RGzI185D3TVC8cdsfu5_9GBEHG_1XQQQnlmaSJ__DeMcBNqo0Vjlm3uEVSMjw7LwdGs_aJEIqxW9ceBuXL4k5l6suY5ibLOE2f1rQQE8AYQH1CGpUytT7xBGUPRNfk0-NTynkhkpj9H_uULq7YPZcmVydiJNkgG9Fp_KM4O57lZ6sj6_ksj4tAvYCCw-26B-pdciklLlrvUIYOZUkXaau62JFjTTHbM_81WRMyNNFXK_dq_St0-f2KpEchNA3jnqvqUHWWC7GlDPBN_yBhGLez74EJ2lA_F5MgRS6zEG7DimR4wqMP504VOjSEVmUeAVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود !
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17017" target="_blank">📅 02:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان میگین که راه آهن رو در آق قلا زدن
! کسی نمیدونه چرا ولی من فکر میکنم بدونم ۲-۳ روز پیش ویدیویی برام ارسال شده بود از ساری که یک قطار بزرگ پر از کانتینر هایی چینی اومده بود !!! خوب الان به نظرم پازل رو حل کردم ! ویدیو رو ااان پیدا میکنیم میزارم ! موسیو یاشار از مثلث جنایی
😁
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17016" target="_blank">📅 02:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارشهای زیاد میگین که موج چندین انفجار در آق‌ قلا پنجره ها رو هم لرزونده ! آیا تررور هدفمند بوده ؟! هالیودی‌زدن ؟ همه سرگرم جنوب بودن هدف اصلی اونجا بوده ؟ خواهیم دید چه خواهد شد ! @withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17015" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17014" target="_blank">📅 02:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ، درباره ایران: ما به آن‌ها ضربه بسیار سنگینی وارد کردیم و من می‌گویم که ما به نسبت ۲۰ به ۱ به آن‌ها ضربه زدیم.
هر بار که آن‌ها به ما ضربه می‌زنند، ما ۲۰ برابر آن‌ها ضربه خواهیم زد.
وقتی آن‌ها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ خواهیم داد.
ما از نظر نظامی، پیروز شده‌ایم.
چند وقت پیش با ما تماس گرفتند. آن‌ها چقدر مشتاق به امضای یک توافق هستند. اما من نمی‌دانم که آیا آن‌ها شایسته امضای توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17013" target="_blank">📅 02:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9jyd80YcIi34QGMezKgJYaHOHXJC8WwJJEHkAnO-Kz6-QXR7lDuJPxrKa9l69LdMbHv-SC_LisygJpfBU90mgLhR7qte9Wn--50fut-MSUY78BevBq-ge5y74vL-C629_q1z0vFCqGvEqm_N8PErQvzU9zOqX0Py0wSIIAE4a69At_MBZMqyGDbeBWs05OUR8oin8PL4tdfL5CUyZGlmhbzZCpIM3RAgEsm-WQnA9vrypvbaPQVlSzL23l3oafPryLd37C5tWLqxoPYIKZ1VajKGnagwDOi10EtyPyAdSVAZVlnngvIIopj21j6mOFVNkgYxWUyxym0MVXqUrZcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17012" target="_blank">📅 02:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاید باور نکنید ولی ده ها پیغام دارم استان گلستان در شمال کشور ۳ انفجار انجام گرفته !!!
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17011" target="_blank">📅 02:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار در‌بندر لنگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17010" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانشهر
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17009" target="_blank">📅 02:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند @withyashar کاره موساده</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17008" target="_blank">📅 01:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سپاه چرا انتقام نمیگیره
😾
🤣
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17007" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajCGf8HGmRoBneepA817pCjDVy2oPG1kuVu1wcZSLroQBV1OHsrUxdUpBj8rr9RiDsFyoA3XMZ4_8EerP02Po8KY_r-cGf2hT5OZRs4H6b4LvOmJAlmlUoYKcCSfwzqtyOE6WCMulsYo_y5kMMaC2I4yYMadF9rBpu860fJ3rAYk-FvdKrgRG4FeXyZF--HO1UdWPFzBELgON-Z6PDDEJ5xXKynRhtn2RCbeG-xOWuNNPQAc-TkPEhdvdEOemJXSA8iifjO_14k9tuKR1XfSVEfZndlKLIVugmyEyNeC00fZ2h4UExIuDE0Pd_0xOgL9n9dhHDufg9U53g3HXAknug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ما تازه فرود آمدیم (انگلیس)و با هواپیمای جدید نیروی هوایی خود که قبلا به پایگاه نیروی هوایی سلطنتی میلدنهال بریتانیا فرستاده شده بود، ملاقات کردیم.
در مسیر بازگشت ما از ترکیه به ایالات متحده عملاً هیچ انحرافی در مسیر پرواز وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17006" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">با لبخند وارد شوید
😁</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17005" target="_blank">📅 01:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش دو انفجار‌ جدید بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17004" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند
@withyashar
کاره موساده</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17003" target="_blank">📅 01:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17002" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فاکس نی
وز به نقل از مقام کاخ سفید:
مرا
سم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17001" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاهورا</strong></div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17000" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHN3_D78NXngwAFGBfP7NEtMr7U4bJruQMx0GgfO1CwLBfO4dZumJjhokfoubjHHLGhOxEqQmPMoyb2n2lDEOFGeyUzlud2TkaidfbSbsbrAGzUn4CuNMwl_mCgyzbCskVMo2oAcdyJPxW0hcxarlKLbnXJiipyjCnVR_T3emSh9M3atjomAcCnsWWJpy7i1AaGINNpRbunG3ip433ribDUR4AhLmh1GXVK9c3FKlT4T3bs_A_G3wT4dvhm9hsPGWj2i7GDXE7ar4v_YnWL2hLKeDxa4rSIghvTsLakpg4n7k2QGBpgdeUdWHpeGd2DjEG7yWFTC14V1ElOY1x1Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاطی که امشب
تا این لحظه
مورد حملات امریکا بود :
از چابهار در شرق تا بوشهر در غرب، خط ساحلی جنوب ایران + جزایر
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16999" target="_blank">📅 01:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/16998" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک مقام آمریکایی به شبکه سی‌ان‌ان گفت که "توافق آتش‌بس با ایران، حداقل به صورت موقت، متوقف شده است."
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16997" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدا و سیما : اسرائیل در این حملات به جنوب ایران دست داشته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16996" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3v7-L5x21GKQhfkbu9S87Uhcr57fMaQcwVk9cJnWqOVV0O4JeqZlZ5smbkVKaToLCmk1pHCgkYF2hoJvcKIS6hTyBX5OXSBAp2o5ELsTFcmPqL0-BG-6GhkYxP9-l30n8nlugi5enoQo64XofjSPIIOCNDB7cBZMH0U1OBh-JUXFJ_klOHBMypN6yzW5iTWEdnYOBM5XUZrDcuDZKbVqG0oZ2xKimuNmp-GbUsl6yQ98vBrO2rfzxPyjwco_juM9pOPIa5oi1YiBlH73fwG153Jr6t2AwcnLVsS5ZLAOd3WNoHOSvqrRL7fSpPrzDbaKEECzWHDEK8TabCe6EZ96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر وقتی سیستان و بلوچستان ، فرودگاه ایرانشهر رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16995" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اتاق‌ جنگ با یاشار : هر کسی دستشویی‌‌ داره بره بین دو نیمست
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16994" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تکمیلی : وقتی ستاد امنیتی بوشهر نمیدونه کی‌زده و میگه دشمن نمیگه امریکا یعنی‌ ممکنه این حملات از سمت کویت یا بحرین یا جای دیگه باشه ! در نتیجه من از‌کجا بدونم کی‌زده !!!! وقتی اینا به کشور های دیگه حمله میکنند آنها هم متقابلا جواب میدهند خیلی ساده است ! @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16993" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ : این یک انتقام برای بمباران کشتی‌های ایرانی دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد! @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16992" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMm8dPQUC7f89i696x5k0_CdH51ThQbl86sIs63VkAOlyVc8Uys0dKmOHlVXFOHHHSPokPlZGEHPz80-LQwLTKdX66SEULM6qXS5CiRc8vjW2RDP652Bbae5d5-CdVqc8DFG1adKwyp6e8vYXpiIf_y_RKq9q_qCSPgNm-pcjoueJx8_FKvBld-Xx8YJ1t4qVLsGD5uXP55AMZgtCj4yDjnj8DcrnKo3o0AZ_BJbrz7IRufEfcbiO3uPSINjcRtEwDCRK8LSwlznnTSln9o2yQHNf6o1LPwIaH6Z_IKIUrMk3fzGzWP9mSjjt2FfT-FckNygp9Rtv1qAR3yjm0pezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار  @withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16991" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فاکس‌نیوز: ناو گروه باکسر از ساعتی قبل وارد نبرد شده!
این ناو پس از چند هفته وقفه، روز گذشته به حوزه فعالیت سنتکام در شمال دریای عرب رسید و اکنون در حال پشتیبانی حمله به ایران است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16990" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a052382f.mp4?token=byT9uA5pTdWH4sMZ0BkOoaexR8SZTaE-I2G7z7EMLk4tEJzPGt5qqWI0vpI9PJnhncwxEuJ0tgdTeqsxWuD2bwRLCYtacDcdyszqhlAlnihNXBLUU7KNbLEJfy8_Id2JjCDd7EeljDCYkSbh5XrGI7wH13YW5b7CPOnVV-nGTXSPd3E2jNxr9c9PT4SBxcgHRvnAF0IC2wGVEsrt1lwRJH5FMgGvXL64DyB_N2ms9Wmnk5cqSwlT6Ot2lkfGIzt5R203uulGYVaS_ucR9Z6kHRp4RapJM_ie14hnOrtkoam43JjqF09xcHCGsfe-5OFipcvWHDEcu8CwtsqRRCROQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a052382f.mp4?token=byT9uA5pTdWH4sMZ0BkOoaexR8SZTaE-I2G7z7EMLk4tEJzPGt5qqWI0vpI9PJnhncwxEuJ0tgdTeqsxWuD2bwRLCYtacDcdyszqhlAlnihNXBLUU7KNbLEJfy8_Id2JjCDd7EeljDCYkSbh5XrGI7wH13YW5b7CPOnVV-nGTXSPd3E2jNxr9c9PT4SBxcgHRvnAF0IC2wGVEsrt1lwRJH5FMgGvXL64DyB_N2ms9Wmnk5cqSwlT6Ot2lkfGIzt5R203uulGYVaS_ucR9Z6kHRp4RapJM_ie14hnOrtkoam43JjqF09xcHCGsfe-5OFipcvWHDEcu8CwtsqRRCROQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج کنترل دریایی اسکله کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16988" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایرانشهر بلوچستان زدن الان ۳ انفجار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16987" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16986">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laEQlIKb_olquy0mlXweR0_v-b0tpTskWLfSyoKh3zo3DhPmMYs7uDp0D_10ZECA_zVjDP8uJwA2NZy7-ZMvug0M6kOyxawX3FVd-IBATFglwLATRFJKNyNnkBLDkHngP-3EdtIpkqkZxxEWzb7Q5i4aNlRgfMsB6gtUWhUt5EL7_X8BJif6j36aL8FABh-yHKTxQEgG462joG3-rxyk2AHtictEc5I0bsaUe6ueKlRgVMPkJJeJdjHgxlK8eg_d0htFTllbY2auvYFISZ8QP2TY79N696_8O6APzgko7KYjfd2RsslJQgxTCUW41fhKLucgfOyUgz1UlnZFVh7Sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت : ۱۰ سوخترسان و یک هواپیمای آواکس هم اکنون در منطقه، چهار سوخترسان از تل آویو بلند شده و به سمت منطقه خلیج فارس میاید.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16986" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه های رژیم : رهگیری و انهدام دو موشک کروز در آسمان بوشهر توسط پدافند ایران
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16985" target="_blank">📅 00:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای انفجار کنگان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16984" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چند سوخت رسان جدید آمریکایی  از تل آویو بلند شدن ، امشب شب دراززززززه و قلندر بیدار
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/16983" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/16982" target="_blank">📅 00:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/16981" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/16980" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستانی که نمیتونن جوین بشن، این پست رو سیو کنن، فردا عضو بشن یا با یک VPN دیگه امتحان کنن. جریانش رو قبلاً برای بچه ها در وویس گفتم، به خاطر امنیت شما و چنل هست. من از شماره ایران استفاده نکردم و محدودیت عضو میخوریم
🥹
🙌🏾</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/16979" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشات رسانه های رژیم از کشته شدن چندتن از نیروهای سپاه پاسداران در چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/16978" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3642cFs_4iWn09zTFIYvWCnLUlK4X3UOLdW883OK47Vur0GTxCbtD-ozGZXpr-yUQPTbz7rtN6dD9s4XeGHGFlRCWK1DZNgN4fuXH1KYDv8MWkxin-sgWpNMtZxaM-_L65aWb_oFsZySVi5vSQ_pUDX1gIcn2jNJx-3_TsHixt3XzzfGQupZysgdtZ9my3ZK2m0c0S5k0psxr4ifZWaCIECf0un09Gq0XR-GBarGkmPsPXNpx8dgI20hrKwY1xZwl6-W9ohSkdBgzcZ_hq8Z8obtoPHBF0TKAlgNOWMzeIHnojZMFnb2tst6M-ijoPKoyKOytF1OtWOu0MGyqqAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/16977" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اطراف بندرلنگه چهار انفجار
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16976" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dv6uNn1Wy2pn54RF2cVgy522xMDO3pyxUAKAeKpVowjSzMt9ofc9pLgv6qr80cWxjJjSzapeli74qvuT2CQfOe6hONFDYBvEs6F7-8I3M4MRNmE5rYx2FQheBRyZttJuHfGjLxasUZViLMXvYJxRwlF4kZ8L51-AjYbKEhLR8fa0GFm8eEszwAJ1LG4D4Y0ZxhRK8bcqzTBQIOwwesTDbVyen2VMXbYOplTTaUtm7ddKAvO0YEq1Bx5hBd35lukIrh5IcyJspmYoWOzD6i4bEJF4InfFt1pF4edFass1tcVOSd9bD9C6ukR6mVBOedqFOU8u0wp4CRT5CtqR2DK5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/16975" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj0Bxwg7In3zgam8kUvaQR9GhG4MGNFz2LXsIDURxSPG7cH7G0ZibVhuSA5EMAsr5n9F8dgkEEEA_Rp_R3ymArTBaHMuyMrfin3COtGM62sZbwN4UvWfHNCjs4NS-bj4MWYWfGzEw7cITyXjdAyZkllQg9ofgGSdYpdyJeYG7BZ5-g9P0Ie3OLc0I4-d_EhGYWhwVVwPw3t-NxdVGXbOZwF2MUWAS5nPw6hEciwC22prybn5cKTr_aItmopO8KAdOOKVtM8fPsNLJ2B4GyklGGGUHMdyT8aas3sND7l-9o8o_E-GEfeYHf0VJrc7KdYtAw4c3xHlK0o8ia59YZ1IgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16974" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدای انفجار در‌ جاسک
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16973" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوموسی
‎
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16972" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16971">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرنگار صدا و سیما:
در پی حمله آمریکا به مناطقی از بندر چابهار، ترکش‌هایی از این پرتابه‌ها به بیمارستان امام علی این شهر اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16971" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=na9Nrq44an70G606NMaOKXupv8UwIU9GLqGl7_sCljXSRAatHaEcNAOk_PwM32QKTY-IBWpnjLhFpH96C45MZo727yHz6ZVSTZ2X6GtMW-2fYxGSClTWBeqrzYL3OAzsKslrNoOUgQQTILbitZsRhEfMZ9Ag16Rh1A6c2mA-yMyVMA50MQxa53lkqG9onK2dIxVz0lsDTiSWojtRlK0ty9Xq9kFatd699x3C0ZIvtdv5nvVllMzb_M64SrqnqKij2Hs7OSG8m-XkI2cfAHaZVh4J75voq4btD4sRHC5uU_nRHqY-zVSSUYH_JLERYc5SfEJJBruNXJvesmx8vW2QcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=na9Nrq44an70G606NMaOKXupv8UwIU9GLqGl7_sCljXSRAatHaEcNAOk_PwM32QKTY-IBWpnjLhFpH96C45MZo727yHz6ZVSTZ2X6GtMW-2fYxGSClTWBeqrzYL3OAzsKslrNoOUgQQTILbitZsRhEfMZ9Ag16Rh1A6c2mA-yMyVMA50MQxa53lkqG9onK2dIxVz0lsDTiSWojtRlK0ty9Xq9kFatd699x3C0ZIvtdv5nvVllMzb_M64SrqnqKij2Hs7OSG8m-XkI2cfAHaZVh4J75voq4btD4sRHC5uU_nRHqY-zVSSUYH_JLERYc5SfEJJBruNXJvesmx8vW2QcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16970" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=pR4zY1rQhxIUKWbS2aKaW67RYDjj2UuESNbSEQ5No4J0k0IKHAMLfpmJ96FQnSHZFKwt8mDn6TGIcuKjPX0FlQtbWmzakaMN7t7wQBrLjL2lKiwG1zEghfQN_vfb6_spdaZVfx633LKoPrna5E5TwEfmM8fI8X2cygBdZbl-0vGcXpyJpxqvvnY9KnWh9hqNw1pF1lpx9d-IVlAPKA8c1KIRH3bPR2h4xwzvN4-ff2hoEDzgNRiM0FM6psxgH1hX-Wi4LRrTNazXnvV8uCQiVD7DpgW68mlQxjsMpJjROYBkDiJNY_va_2lB2uFnPytbhKZukqumniwIKxNXVnfwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=pR4zY1rQhxIUKWbS2aKaW67RYDjj2UuESNbSEQ5No4J0k0IKHAMLfpmJ96FQnSHZFKwt8mDn6TGIcuKjPX0FlQtbWmzakaMN7t7wQBrLjL2lKiwG1zEghfQN_vfb6_spdaZVfx633LKoPrna5E5TwEfmM8fI8X2cygBdZbl-0vGcXpyJpxqvvnY9KnWh9hqNw1pF1lpx9d-IVlAPKA8c1KIRH3bPR2h4xwzvN4-ff2hoEDzgNRiM0FM6psxgH1hX-Wi4LRrTNazXnvV8uCQiVD7DpgW68mlQxjsMpJjROYBkDiJNY_va_2lB2uFnPytbhKZukqumniwIKxNXVnfwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16969" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=fWcbjTG8kEAELyxgNm3Jo320YrXh1EcxMdhNCRUJq0_DdHFbgLm6luv8IA6T7C2_qCrkqWfJ42azkQ2006bJdOwynhbB-b7EiIUUYTAAPnI_-8Q4ZZxxGRjx4Uo6V4o1Dz-KIn5hjDHtUjZgyZ1R35yGDRyUuZfigB1pO4z5Y3toNJDuVntnumLHSAhOhnYnRMDcbiOWztUwu1730AJmdf6BD_f_gOCd2QpxQbvy-e5vUQ2YEufDylHZJqS3oKd8B5tU5oC47lRnxUpzzUzEgtsZS4vhTsYqi4IKyVIDl7rUjkM_Cvs0wcXu39sWoPCNU6M6BScADPYF71732mCiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=fWcbjTG8kEAELyxgNm3Jo320YrXh1EcxMdhNCRUJq0_DdHFbgLm6luv8IA6T7C2_qCrkqWfJ42azkQ2006bJdOwynhbB-b7EiIUUYTAAPnI_-8Q4ZZxxGRjx4Uo6V4o1Dz-KIn5hjDHtUjZgyZ1R35yGDRyUuZfigB1pO4z5Y3toNJDuVntnumLHSAhOhnYnRMDcbiOWztUwu1730AJmdf6BD_f_gOCd2QpxQbvy-e5vUQ2YEufDylHZJqS3oKd8B5tU5oC47lRnxUpzzUzEgtsZS4vhTsYqi4IKyVIDl7rUjkM_Cvs0wcXu39sWoPCNU6M6BScADPYF71732mCiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به اسکله شهید کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16968" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش انفجار بندر جاسک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16967" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlwi6UznwiGvz7Lnt0zv7ejHWsf-uCQnmovjdZ3rIwJU0lYrNEoeZc76HKlQqsbAOvsUAEeY1SkQBukeun-zdfbIzOPkxoWAdFdNuHViEbgA9B00ROAOCAzKle7ZWc_NPKYJOfRxZZoaYnp20x2N7hQZnMwAN1IAaql9qYja-vWUpUXjX6ery9F5PJGJdueCy_0QLYBitk1I7YEMnO45829qszt5YrzGTZMYhiefrAwCQUv2_w1n9PYrCIZilChXps_VaYTZVnmV1BQ7vmh5kGhXXNCOxcf5cMJ3scPk_VqLdBqHhig7WA_MxpWdrf4g88RMpYpYx7YrUnl2E6ywaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJGKneZ7jrGF7VK4afX6FYCnpXh0nA5IpibsKsCJtObqwOlexc9JcNL-vj2Cr9GcOM1vddumCd8P0kRF0i_I8bHUAO6R_COatQaSHGMTlw9-J7wV2-P-MGMdz96BuUKkGvYtLCJ2srXPtK90Fo0xGd3fEUyHqAYo3WqwCXCt8xIHxOYJd_872GfKIMq6Pgh_uRIai0Dk6P-9wsyHTw6sqFPX33QcIlviMnhjlnEADcwTJvsRCG-qw_Hf1okLHh6IggNVqz6jZ44etvUuVGbeNx1GXAtqReop7ZnjZQu-OR3aKXhgs_9_pUrtylLP_as0tsaIFP0CGA1ZB1jb7Ru1Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16965" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رسانه های رژیم :  شروع حملات موشکی ایران به مواضع امریکا
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16964" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmMscpDZn_Na9V1CxGW6YkJNk9O9ijp4Won1-I3R2oWGn1ZpgfJqaHS0UEkx8GPqVsMtkSlGzYYlevTAk94ViZEyFzrpbQBQnf7deL-znv1zUpRH5qg59Z83eNvCfKNRXk2-8-B-EpVCltgPC1_vZhX8HqfkUljm0aLx1XNO_Xl0bjt6P3TFdLqyq7DGHG9ypfm4ygF2vwSTBDeaUexCQ7FvnOAqEY97_YupxgqBEnqMCOWJJTE3Q03ooautWFAK05s_w4m5RUKq-ee_gkusTVbnJ7KpNryvrivnF4U0xbjuejPmHssPE6K0DT9wU5LKE1p6RktYhp84DNtOSvOQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16963" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=ERzXSGjGlpWFcDSDFUHzRvhtKQ49uUbcSrJcl_OAII78PiUM3inkl0aNj1CphAy77vCvJ3wGLPfB4UXKu07oEIJQTQ8jixIRDaAvNSxuHJ6eQ_4uXVTzrzhKIhz3Ztx-On8-xaOcPpEMkFlXW-EkHGtUbFxwMvgdNLBF5A9DwYLCFbth6rqb5pzWbE5bkCraLKIAV859l3Hiebnxuqw55l3xxUWjhFENczRkZ_nFBdv3VqYiSxnOMcEuVeHG2bbibLmYNVjfIP9zDecqWQlQJQGxniblia9GIiJGl8Onjag7N5Dn-rTuJdUeTwLkaFQKkSW8KnXT7tAH-a4lhpP8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=ERzXSGjGlpWFcDSDFUHzRvhtKQ49uUbcSrJcl_OAII78PiUM3inkl0aNj1CphAy77vCvJ3wGLPfB4UXKu07oEIJQTQ8jixIRDaAvNSxuHJ6eQ_4uXVTzrzhKIhz3Ztx-On8-xaOcPpEMkFlXW-EkHGtUbFxwMvgdNLBF5A9DwYLCFbth6rqb5pzWbE5bkCraLKIAV859l3Hiebnxuqw55l3xxUWjhFENczRkZ_nFBdv3VqYiSxnOMcEuVeHG2bbibLmYNVjfIP9zDecqWQlQJQGxniblia9GIiJGl8Onjag7N5Dn-rTuJdUeTwLkaFQKkSW8KnXT7tAH-a4lhpP8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16962" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=N-owh95DubyerZ-yG7lZ5YsqWL_7lyj2gD-aIg2zY35NXeBrh3h5847UnoLyWS63sGMQDeO4j5GvsnUZZqrnj3QVdOj-aVvVDcFIWLEnC-w8pXSbAmHYgeQlXdRuRxRC6stk8xnKITTCIldqGxVKb3KsaFG3O5T_nMqP4iuh0uvNhYepgbRC034SN8xsduFBPOt8KoCKlBaEPgmlXrgoiUUc0xkwSeMWUn8qYAWUenGJT3Pj5gW514kYOQSRiCps48iMb5C-QS757vEAKP36N-mBxUt7Fjn8pCDF6kifS0gs-KYgpbY22Fcut3rOxd_NAVukTfkmRvMhT7dC8IEV1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=N-owh95DubyerZ-yG7lZ5YsqWL_7lyj2gD-aIg2zY35NXeBrh3h5847UnoLyWS63sGMQDeO4j5GvsnUZZqrnj3QVdOj-aVvVDcFIWLEnC-w8pXSbAmHYgeQlXdRuRxRC6stk8xnKITTCIldqGxVKb3KsaFG3O5T_nMqP4iuh0uvNhYepgbRC034SN8xsduFBPOt8KoCKlBaEPgmlXrgoiUUc0xkwSeMWUn8qYAWUenGJT3Pj5gW514kYOQSRiCps48iMb5C-QS757vEAKP36N-mBxUt7Fjn8pCDF6kifS0gs-KYgpbY22Fcut3rOxd_NAVukTfkmRvMhT7dC8IEV1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16961" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQXDgWseI7D2Fjcl60jWMS26UyeUDu430Hyy3c0l7ZbHn0vAHWkSL8tnIYR-4btLbsL1o-NrjPMYDk01pt_HtEI5kv-Y9an1DbOftCKwYwqE1MlvNhV6bYcdkvokSmFMgKzf1WvoyD8ZX9uabueCqj-Veh1ojqgWaep3YDdz-m3jfi7aHtVFHaXWhYcpGzJ7FmhgNCuUyYwiAgaLv6ftr1PK5R8MK6JyxxnJFlfJ3CkxOgCWos6MaHIvtYQnIasbFBat6Qw0XG41zllNCieR0y_SHvbHCH-fVUNR-WIhGi6khtrCrlTQnr6u_89EJGFAY9SX9GGF4RxuSDeJ6-cYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی سازی سمت اسکله باهنر بندرعباس رو دارن میزنن
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16960" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16959" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فرودگاه بندر چابهار مورد هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16958" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=UyLAQgdaa7XYR0mL7aNbFRBQ2PMDA2EkLbWUwUrtDWvDa-MEcXdSGLir7HaTvGpeXO8EUKwfj6RdJhNc81uqx0qP9fvj1gyiu_JAbf7O16PvMdHPwl7QAx5MYyfwj1Dwa0fO1eUb4Q1fsmNLjUjgsi8ks4ExmC0as8V8uUQ8-vF7jUBjAV4h-DXjcMKCVRISMFQBxw6en6fWAmaHlFDHZLL3nwF4LybWqNKqojXZLBpKfmGt3cgV1NNGCMvKzSp-nFVxLGuN_X37zg07nfwsXjlRyg9ijSJBUuBbvB6Nv3L3vaXeqiwH2xcPEVfLJo6LRZDWiJofcsQnK_qJ5eE-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=UyLAQgdaa7XYR0mL7aNbFRBQ2PMDA2EkLbWUwUrtDWvDa-MEcXdSGLir7HaTvGpeXO8EUKwfj6RdJhNc81uqx0qP9fvj1gyiu_JAbf7O16PvMdHPwl7QAx5MYyfwj1Dwa0fO1eUb4Q1fsmNLjUjgsi8ks4ExmC0as8V8uUQ8-vF7jUBjAV4h-DXjcMKCVRISMFQBxw6en6fWAmaHlFDHZLL3nwF4LybWqNKqojXZLBpKfmGt3cgV1NNGCMvKzSp-nFVxLGuN_X37zg07nfwsXjlRyg9ijSJBUuBbvB6Nv3L3vaXeqiwH2xcPEVfLJo6LRZDWiJofcsQnK_qJ5eE-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16957" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
