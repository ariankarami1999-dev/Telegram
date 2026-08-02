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
<img src="https://cdn4.telesco.pe/file/Yzk6RPVhL5yOaSdJb8QLvb7GKq07cqtYCycJOHmquRGtWh2gGkvC2MLiZk4F7Sc8uN9s1hRy6zqA0QcEBc6oR4ubxL2fejGNV3h2kEjBjWcSz4qIFmRxh4fAAz0z4GumC9geHnk7qhz5xo3bMUV-hppL5DLRoZL52FU-6ZxM3OhCkaczOPCAP6Jic71czu0Sd2bT5eH7uKcB_br7ACvyi6lyRIto0v_WLpDANSuvy6F9cghSE8lEdxSieMfFpnKfhtRrUT7IsMurEy22BaQq39rfEmLr0lraaF0c9zgHNWMkEZ3vf4ibzgEKeM084X5ZSiDeuBkT3c0U8UEL6qv_ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 16:02:47</div>
<hr>

<div class="tg-post" id="msg-454038">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEVQrU-tr9vUVM-3Ksx-__3GS9co8pe0fdUvdLsYgqRc-lgf6gZLPN2lzsWGDNpzMqZPlPI3yQmJth5gIA5RR-XxaAkX2m_5Z8Ff6QSJGVoawvblMMNMNe9p0v6HYV_BxV505NoQnPRSbjkCjgjFFEjxSqyHahneh6W41BbMlS6ZgpuPr5DaG30XGU5oJ8ymlwr78brOdrQuk0Mk_9GQOr7GCrcIR_hh5VaPGcl5n-EGnqvWXy-vJ22iB9c6W1pqFqtMjBcjnkxRYjbOqZEwxqixK67qiZeBmssQYV1WkPEzqhbYSIHpF1y8WMiWDaeD3hdsiHdKYRk6sa56IGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح اینفانتینو و ترامپ به گِل نشست
🔹
بعد از مخالفت شدید یوفا، کونکاکاف و AFC با طرح فروش جام جهانی به بخش خصوصی، رئیس فیفا از توقف این طرح پیشنهادی خبر داد.
🔹
طرح جدید رئیس فیفا می‌خواست حقوق تجاری مسابقات مهم فیفا مثل جام جهانی را به ارزش ٢٠ میلیارد دلار…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/454038" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454037">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح کاپوتاژ اتوبوس‌ها در مرز خسروی این‌گونه اجرا می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/farsna/454037" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454036">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گرما اداره‌های خوزستان را دورکار کرد
🔹
در پی تداوم گرمای شدید استانداری خوزستان ساعت کاری ادارات استان را در روز دوشنبه کاهش داد و فعالیت ادارات در روز چهارشنبه را به‌صورت دورکاری اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/454036" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454035">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv68tC0uNh4ZplBOZf5lWzR7gVOzMSFN8WdlBOSmQY3KvrVYbUOZWeBCgZmLNFgw73k030sYknRfmV1zP398jcnMiqTsln_l8MCBPLAWWm_XF31N16xcILITXeNFcgf4FukoWu5HMWVMlv5uy7WhKo2LuVfa4kQBLSEfwjJS0J995VexOZVaxfLHn5Fd_-gE7xDnVeQrS7JdGI0FNTWIM1HMSW6HFapVex0SEbLceEatsx1iRr-Cl5SAwBp4trHvFxuD2BG8yfWbCepJrEoXdEn6xyn8SyMqAKOwY7Nyl-0WF6xxrMWG8sPWsZ6rxRmkAO9_u8eyqaGUvuBJCi1Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
مروری بر عقب‌نشینی‌های ترامپ از ابتدای امسال
@Fars_plus</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/454035" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454034">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNuJqXF0o4yAZJHvmHNlClEeOqMaDC3-UWf0QgOq43D89imJovEuU-GpGl7Dm5n7wh2J0haP_ghNgWmaxJXIHEDSXgsnnoR8yBJ2O5t0yXuFuaL7pVeddHicH4mONNepyOGxmBVQvsmnyOXYxqt0GxBN-xigEoNOs--6KRrMFWizQVjPncz91esyJqSKOgxz9SOpWTToTX-tXMr790a_yEX-q_h62wgeyOkcDNdVyq5bSlPNVPCIecc7FLlyYzevzq0CqPD9aRPXZtEJ9Lmk4DedbmzRHgCYfUC5u-Fb0mLWQoQUMdJrm8xM6kLrnO2TZCaRxoB2gki7lBDy5TP8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی اسکورت‌شدۀ آمریکا زمین‌گیر شد
🔹
منچ‌اوسینت، اکانت رهیابی‌های ماهواره‌ای، می‌گوید یک کشتی حامل گاز قطر در مسیر جنوبی تنگۀ هرمز لنگر انداخته و متوقف شده است.
🔹
بامداد دیروز شنبه دو نفتکش در مسیر جنوبی تنگه هرمز در آب‌های عمان، یکی در ۱۱ مایلی دریایی شمال‌شرق لیما و دیگری در ۲۱ مایلی شمال‌شرق خساب هدف قرار گرفتند.
🔹
یک منبع آگاه امروز به فارس گفت، «تنگه هرمز همچنان بسته است» و شناورهایی که از مسیرهای ناامن عبور کنند، «حتما دچار حادثه خواهند شد.»
🔹
منچ‌اوسینت می‌گوید که این کشتی در جمعه شب ۳۱ جولای تحت اسکورت آمریکا بوده و هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/454034" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454033">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/454033" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454032">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/454032" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454031">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roIOSzudX2nQrxQdPHSOlaw9dHUkKdNpodvsYLcGO2KKCvONqrLBJXfZJNXTt9JLTtZnZUw5yEKoWbVUIH8-PUFahw3uaaM4rOgt0DdV0yXBnc4z6y_khBrx6oJGH0Fnpy_9Dr8lWtmTVlNWB4qjOi7lus5y5HM_61GJCEMtIsgXRrN-waV_EY_VZ-wpMzxC8wuuu7uvTgbHmb2LbZ9n2JS_5on-CzSSXhBsfoKbcWJ2YkNWO3EwzCbIvmPK-Zp9LpUSBKmeF6v0FFJ75KbZBcpDOJqwPkfQELuXPExT_FlNywujIx3A7_jZNWe6WNI_SBvD6xmMJme0PmgX0NCgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه خرید سنگین،با اقساط سبک!
✨
فرش دلخواهت رو با
اقساط تا 2 سال
بخر!
❌
بدون ضامن
⚠️
بدون بهره
با ارسال رایگان به سراسر کشور
🚚
🛑
فرصت محدود
🛑
4شعبه فعال:
📍
شيراز،خیابان عفيف آباد
📍
شيراز، پل كشن
📍
شيراز، ابتدای دوكوهك
📍
بوشهر،باغ زهرا
براى ديدن مدلها و اطلاع از جزئيات بيشتر همچنین مشاوره رایگان، يه سربه سایتمون بزن
👇🏼
https://jryn.me/bWa2AE</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/454031" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454030">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/454030" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن آژیرهای خطر در اردن خبر دادند
📝
منابع اردنی مدعی شدند که صداها مربوط یک «هشدار آزمایشی» بوده که به موبایل اردنی‌ها ارسال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/454025" target="_blank">📅 15:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر اتفاقی بیفتد خودم را به اینجا می‌رسانم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/454023" target="_blank">📅 15:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
۵ نظامی ارتش لبنان در حملهٔ رژیم صهیونیستی مجروح شدند
🔹
فرماندهی ارتش لبنان از مجروحیت ۵ نظامی در شهرک کفرا در بنت‌جبیل بر اثر حملهٔ خصمانهٔ ارتش اسرائیل خبر داد. این حمله زمانی رخ داد که یک خودروی ارتش لبنان در حال همراهی اهالی شهرک بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/454022" target="_blank">📅 15:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: قانون سقف بودجه موفق نبود، فیرپلی مالی جایگزین می‌شود
🎙
رئیس فدراسیون فوتبال:
رسانه‌ها باید بدانند که بحث فیرپلی مالی امسال که توسط سازمان لیگ فوتبال ابلاغ شده، به لیگ برتر منتقل خواهد شد و انشالله امروز یا فردا به لیگ یک نیز ابلاغ خواهد شد. واقعیت این است که فیرپلی مالی در واقع جایگزین ثبت بودجه‌ای است که قبلاً ابلاغ شده بود و نتایج موفقیت‌آمیزی را به همراه نداشت.
@Sportfars</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/454021" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت عاشقان امام حسین(ع) از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/454020" target="_blank">📅 14:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی کشتی در اندونزی با ۵ کشته و ۴۱ مفقود
🔹
در پی آتش‌سوزی یک کشتی مسافربری در آب‌های اندونزی، دست‌کم ۵ نفر جان باختند و ۴۱ نفر مفقود شدند.
🔹
طبق اعلام سازمان ملی جست‌وجو و نجات اندونزی، علت آتش‌سوزی هنوز مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/454019" target="_blank">📅 14:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454018">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZMNx6lPKDaFhcd2_5yCA9PbKPQ2jA69yc1GBU1ycVg2h0Gn5QN1L-PWXU2fj3vKpAbEEMjzm1BEeVT0zfQXY30kzd9y0ZBEf9O1GXiq_4YQ2-tjkDZPeMoDsRX5rgwo5-8QHP4rgVSCI04rxNoNyWeq3lamLE-qnO7Yy96lcHnAkYWOYc5zFayXympvvL6XHd_Gt23lA3kXImgxkj2EQ8hHoW9fW_RHAjGr07mo6pKqqD3AhjGdM5ficj87juC423C2Mh1oFcx3UkNV759AVFVp4zoEoZv96pikNMGGLhoq_9M6_0RQ_llBopa9fPBUxYsVnB7tZ1JKBmd4hAwRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: زائران برای کاهش ازدحام بازگشت، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/454018" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcIJ8E_LXqIM8G7sgy-bjhEYFM6h7zVFVejLM6wy-x-Zv8zMlNKVJ6ueuPQRfPhGj0PuiXDB2laouVmSKSNaComPdoARcovU27HJlc4hLkkqLUPmjk62WiC7Aic06EU_8Lwdlq4yQb3kHqz052Ki7vWTBPALvvcAGLIWp6nWUPCFAZiK0NU_o5eH5T7a1UZp5N4wS81TVV1hy64WNnnon6RyUWWvsTZmOwXyjbL4S_1wUzaoH2eiFVavt9LdAIq082hbcfWl254PbwnNwwZ-MWq7NTb5PWbc1riHYlKLw4IK_9Xz3h-y1IJeZUxM6t1v7vDIklKBgP9c1o1hxUeD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دلیل نوسانات و تغییرات در اخلاق و اظهارات رئیس‌جمهور آمریکا، رسانه‌های شهرک‌نشینان صهیونیست او را به سخره گرفتند و تصویری را منتشر کردند که «پیش‌بینی وضعیت روحی ترامپ در روزهای آینده» را نشان می‌دهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/454014" target="_blank">📅 14:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا،…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454013" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoNWYDGDolwm7cTCsi36IKevyLwL3sqnXvpjiOh10g06VGnheSSC5DxOqzbf8M-JH281_LL3e1nzl9W1cabZOUCKZ-NaO-5iJNcJ0V3TXimdHVELyonc4UwG34oRhyW10DpZGPi8vvdTUol2qviPYQzne0uW3ztO1R09kH-lNjqlgarHcGLbblbE37oY0svAg976jKLKy9e0f9FXZZjVn-TLihNLZ-Y6T5HL3yVIs2USjmcLPtefPT4YQvMYvLSoFX9xhckaQFUDmXY5IDjB24ZIDWS38wy0IcmVeLq24OolG7k9wYeDsiw9aE6ddFZdjzxMzlI2jWyaMSFf9xmheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ هم حریف لابی واردات از امارات نشد
🔹
شایان نادری، معاون وزیر سابق جهاد کشاورزی می‌گوید که «لابی واردکننده کالاهای اساسی از امارات» آن‌چنان قوی است که حتی بعد از جنگ هم مسئولان را می‌ترسانند که فقط از ۲ بندر امارات می‌توان کالا وارد کرد.
🔹
واردات کالا از بنادر امارات در جنگ متوقف شد با این حال ۴۰ روز پیش، قنادزاده، معاون سازمان توسعه تجارت، گفت که تجارت با امارات با شیب ملایمی درحال انجام است اما «امیدواریم به شرایط عادی قبل از جنگ بازگردد.»
🔹
واردات کالاهای اساسی در ایران انحصارا در اختیار چند شرکت بزرگ است که در بسیاری از مواقع کالا را نه از شرکت‌های بزرگ تولیدکننده بلکه از امارات می‌خرند. تسویهٔ پول نیز از طریق تراستی‌ها و از مسیر غیررسمی انجام می‌شود.
🔹
فعالان حوزهٔ تجارت می‌گویند «کارمزد انتقال پول از مسیر تراستی‌ها در برخی معاملات ۱۰ تا ۱۵ درصد ارزش معامله است.» یعنی تسویه یک محموله ۱۰۰ میلیون دلاری حدود ۲ تا ۳ هزار میلیارد تومان برای تراستی سود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454012" target="_blank">📅 13:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
به نظر شما، شهرداری تهران امسال به شهروندان مسئولیت‌پذیری که عوارضشون رو به موقع پرداخت کنند، چه جایزه‌ نفیسی تقدیم می‌کنه؟
✅
روش مستقیم پرداخت عوارض خودرو و ملک (شامل نوسازی، مشاغل و پسماند): سوپر اپلیکیشن شهرزاد
✅
دور جدید قرعه‌کشی بزرگ شهرداری به زودی برگزار می‌شود ...</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454011" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNuonlJLOPvkRD5Kr5gG7PpeoUip6qUpfF_Cj5Qo3c6WS11ihbtML80hOWAj4hOLUtSBtixWV_mdePpNeSg6Ww2ZLdOi_QnnfG4w87TJ2_a8I4NdFyxmdl8CIvXpyq5n9uFMzJza6XkxBESiE19Eud8DCiZ9u4Auyp1YIrPeCCvpgGOW34iZKKvDy7aELSOIof94lbMLkjDHh_jcQSCwxFZdnT-TG2RFbsbc8GBl5MtfEKimMe9_z-_vcoDVWMcBjRkBfAXm3bV7BAFVe_FjVwk1113aSSeUdzITbWfNpkAyeKjQIdTB8fTTDFf8gozQsGmB_D1Db1bnW0tHJ7YAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ساخت داخل ۹ همتی تجهیزات و قطعات کارخانه‌های مس در سال ۱۴۰۴
🔰
صرفه‌جویی ۱۲۵ میلیون یورویی مس ایران با بومی‌سازی در پروژه‌های توسعه‌ای
🔻
شرکت ملی صنایع مس ایران با اجرای برنامه‌های بومی‌سازی تجهیزات و قطعات موردنیاز پروژه‌های توسعه‌ای و بخش بهره‌برداری، در سال ۱۴۰۴ از خروج حدود ۴۹ میلیون یورو ارز جلوگیری کرده و مجموع صرفه‌جویی ارزی حاصل از قراردادهای بومی‌سازی این شرکت به ۱۲۵ میلیون یورو رسیده است. همچنین جلوگیری از خروج حدود ۷۶ میلیون یورو ارز در پروژه‌های توسعه‌ای سال ۱۴۰۵ در دستور کار قرار دارد.
🔹
در سال ۱۴۰۴ تعداد ۷هزار و ۵۵۷ آیتم از قطعات یدکی موردنیاز کارخانه‌های شرکت ملی صنایع مس ایران در داخل کشور تولید شده که ارزش آن حدود ۹۰هزار میلیارد ریال بوده است. این بخش در مقایسه با سال گذشته، از نظر تعداد قطعات ۱۷درصد و از نظر ارزش قراردادهای ساخت داخل ۵۶درصد رشد داشته است.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sg
@mespress_ir</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/454010" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/454009" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با
بانک‌های متخلف در حوزهٔ وام ازدواج برخورد می‌شود
🔹
معاون امور جوانان وزارت ورزش و جوانان: با وجود اینکه سالانه بین ۴۵۰ تا ۵۰۰ هزار وام ازدواج پرداخت می‌شود، اما همچنان ۵۵۶ هزار نفر در صف انتظار هستند. متأسفانه بانک «سرمایه» با فقط ۲۵۰ متقاضی ثبت‌نام‌شده، هیچ پرداختی در این زمینه نداشته است.
🔹
تعاملات نزدیکی با سازمان بازرسی کل کشور برقرار شده و پیگیری‌های حقوقی برای احقاق حقوق متقاضیان در جریان است. بانک‌های متخلف جهت برخورد قانونی به بانک مرکزی و مراجع قضایی معرفی شده‌اند و این روند تا رسیدن به نقطه مطلوب ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454008" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاموشیِ تنها نیروگاه اتمی مجارستان به‌دلیل کمبود آب!
🔹
نخست‌وزیر مجارستان با اعلام تعطیلی نیروگاه هسته‌ای این کشور «به‌دلیل کاهش شدید سطح آب رودخانهٔ دانوب»، از محدودیت برق و احتمال جریمهٔ مصرف‌کنندگان خبر داد.
🔹
نیروگاه پاکس در ۱۲۰ کیلومتری جنوب پایتخت مجارستان، از آب رودخانهٔ دانوب برای خنک‌کردن رآکتورهای خود استفاده می‌کند. این نیروگاه بیش از ۴۰ درصد برق مجارستان را تأمین می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454007" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا، تنگۀ هرمز همچنان مسدود است و عبور شناورها فقط از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه امکان‌پذیر خواهد بود.
🔸
ساعاتی قبل برخی رسانه‌های وابسته به دشمن با انتشار اخباری مدعی شده بودند ایران با طرحی برای بازگشایی تنگۀ هرمز موافقت کرده؛ طرحی که براساس آن، ورود کشتی‌ها به خلیج فارس از طریق آب‌های سرزمینی ایران و خروج آن‌ها از طریق آب‌های سرزمینی عمان انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454006" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWt9aXes-YjFFkrNfEe3TtLJ7uAGt57H79G1ki6UxU0slSvCEW38XdZWz1q-CzUB3no-4RZBmrcFKOCV1GpOJ3_GXKcGsqFBLZ-M4-0Kx37rkUPUWgRZ_NtY0ufQ8AKgpqz52tUWHx_FSFDpMyWSOwZeqEiQoPjO9htkRqICxXzRgzPzsK4LdtclACCqpwdFq544qYcYuMhqlrp5CF4tExpJ8ZQAHUFzuGuKosxudSMBHCHKdf21wzvT9gcO2rqxxw3ePwV6MCyVqWDGU6j__3mrNs1FMk3iImDN9OKn2eUK_lAHS0bcwWbI2cj-5-mxR85XOgJoj7MzBtDJORRhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۹۹ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۹ هزار واحدی به ۵ میلیون و ۱۵۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454005" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLknFKPto43MxFj6FZI2FYNEgDyK0ZX8wGb9yhtF6n8hhlmuYUYT7GQDx4Wim3iPRtdp2z3ht4VDVK-uBz6UxA5p5YSSPM9oFQB5OiCYhwBzMuvEqrtOCYCXlvRD5lsycNMBMi2japzc4upw7mEVkjS34Fv31vqBvnJOFLmKUt-NaA0Ud2XybMbPecfhf8PwTAqa-vm5rPNpE65D7QD_wF9cEwWXYcFBHdZku26bK8ML3TztwcpP9PaFgtL2FQsZrz5jCcaabwMGCtSuBJpDS-w60rd1OtpQvTcBtbGyGrkRm0UYjuHZ09NwRrMYXS3sG168lad3qpafcLrGM3MbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار رئیس قوه‌قضائیه با آیت‌الله جوادی‌آملی
🔹
اژه‌ای دیروز در سفر به دماوند، با آیت‌الله جوادی‌آملی دیدار و گفت‌وگو کرد و در این دیدار گزارشی از اقدامات، برنامه‌ها و فعالیت‌های قوه‌قضائیه و آخرین وضعیت برخی موضوعات مرتبط با این دستگاه ارائه کرد.
🔹
آیت‌الله جوادی‌آملی در این دیدار با اشاره به جایگاه سوگند و دلایل در فقه اسلامی گفت: علم غیب، مبنای صدور احکام قضایی نیست و معصومان(ع) هم در مقام قضاوت، براساس دلایل، شواهد و سوگند حکم صادر می‌کردند. اگر فردی با شهادت نادرست یا اطلاعات خلاف واقع حقی را تصاحب کند، مسئولیت این اقدام بر عهدهٔ خود او خواهد بود.
🔹
آیت‌الله جوادی‌آملی همچنین حضور گستردهٔ مردم در عرصه‌های مختلف را جلوه‌ای از نصرت الهی دانست و با استناد به آیات قرآن کریم بر نقش ایمان و حضور مردم در حفظ و تداوم نظام اسلامی تأکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454004" target="_blank">📅 12:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق، خستگی را از رکاب‌هایش گرفت
🔹
پیرمردی که مسیر ۲ هزار کیلومتری از خراسان تا کربلا را با دوچرخه طی می‌کند، می‌گوید: «ترس در زیارت معنایی ندارد و خستگی در مسیر عشق به حسین (ع) رنگ می‌بازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454003" target="_blank">📅 12:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_krRhbniHSDMTrAuYvLNklWAbq2SvluFTe46SxJo4U8BicogyewVnPvfygTgRGToJN39lR31VpiMBNoX2zWKV-tfiHpnoEReR6JlkyKIOLC7ifQVzR_pctk8fa5HR7kb0342yYYQhlk7qZTEW9EJpd648E_GU99qyun4oQ0izuoV6zkfnBKOusEZCKOyEdDSBMTW0sk5P5HrJGaD5VFceQJzXp0DtU0Xi74YXU3UCNVniZ--6J09C03XulTHll2jfNVdcjYCvwc-9uyC0KBmHNgWpWRCq4DlWSrfFpv_DiIeaO_iokp__hXQJNBqzdgqnXcr-b9GGzZVEGotpfSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سی‌ان‌ان از عوامل عقب‌نشینی ترامپ
🔹
بعد از عقب‌نشینی ترامپ از تهدید دوباره‌اش به تشدید حملات نظامی علیه ایران، سی‌ان‌ان در تحلیلی به قلم برد لندون، خبرنگار ارشد امور نظامی این شبکه، گزارش داد تحلیلگران فشارهای اقتصادی ناشی از جنگ بر متحدان واشنگتن در منطقه را یکی از دلایل تمایل این کشورها به توقف جنگ آمریکا علیه ایران عنوان کرده‌اند.
🔹
طبق این گزارش، در همین حال، ارتش آمریکا با پرسش‌های جدی درباره توانایی خود برای دفاع از نیروهایش روبه‌روست؛ زیرا ذخایر موشک‌های رهگیر سامانه‌های پاتریوت و تاد به‌طور فزاینده‌ای رو به کاهش است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454002" target="_blank">📅 11:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYSC4nSUZh3AiP_da1nVAe3aHCEFuEeAukI3mpAtXC5K_jo1zG8ltr-2MGuKzrMc8C0NyTqHchVEhLjBJVjmXaOd9ADqBizRNP9tnTNmDcUkBWUAweamRTORxliYpvD-FbS7HXwUlk37aNAT9njF-ux11yrAtPOKS7oZmKwh0zRHityhQpWh7WmdO6cJ3nEoURi5pctdiGIXeVA7kjJfaQWSIWxfHUbH6yIBwFKNvEEpivCvGizncsr9g3UNEHwKkftReiB_XNBClGWtgZUY-SONoSHjh72bDJx5xgKecHixS94lMVm5_LoZ3iBeQDS9SFpr3VitVzFWjBQO9zi1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سرپرست وزارت دفاع: نه غافل‌گیر می‌شویم نه منفعل
🔹
تهدید را مبنای افزایش آمادگی، تقویت بازدارندگی و ارتقای قدرت خود قرار می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454001" target="_blank">📅 11:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان یزد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضرب‌الاجل دادستان یزد به ۲۰۸ فعال اقتصادی برای ایفای تعهدات ارزی
@YazdFars
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454000" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e5f69ffc.mp4?token=d-uApch8RwnqtXkRqMaQ4ArXHAjam6tnbSAlGaOlUY3Rb_6QVUgJZC2ogMQMJINWRuReW0FhGcUOyVc5pjHZyqrWQZKZzVpQah4JhKn24nraikqVOMmmZI-_f5_oAjQ_-6r8hDSJBGfPuqWiXvaI4neiNWSNgJHZ1CVcVKmSS5qzTo2qikwanNL6Og2lON1AN5ULgcAwYx3WXdr1tSk9mzs4T0SoJr13itta9NABhGjuSfmF0dYN5zL74SQl9JzAHEYZ3oyuhZvnBb1ZBo6F9hqi7nChbJvT0pJKJ1i_g9ILIquS-XpKbxWoJlg6ErFW5RsqUP102j-3YY-R3Mt8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e5f69ffc.mp4?token=d-uApch8RwnqtXkRqMaQ4ArXHAjam6tnbSAlGaOlUY3Rb_6QVUgJZC2ogMQMJINWRuReW0FhGcUOyVc5pjHZyqrWQZKZzVpQah4JhKn24nraikqVOMmmZI-_f5_oAjQ_-6r8hDSJBGfPuqWiXvaI4neiNWSNgJHZ1CVcVKmSS5qzTo2qikwanNL6Og2lON1AN5ULgcAwYx3WXdr1tSk9mzs4T0SoJr13itta9NABhGjuSfmF0dYN5zL74SQl9JzAHEYZ3oyuhZvnBb1ZBo6F9hqi7nChbJvT0pJKJ1i_g9ILIquS-XpKbxWoJlg6ErFW5RsqUP102j-3YY-R3Mt8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش میدانی فارس از وضعیت زائران در پایانۀ برکت مهران
🔹
به گفتۀ زائران زمان انتظار زائران برای انتقال از پایانه شهید رئیسی (برکت) مرز مهران که روز گذشته به حدود چهار ساعت رسیده بود، صبح امروز با افزایش ناوگان حمل‌ونقل عمومی به ۱۵ دقیقه کاهش یافته است.
🔹
اقدامی که با هدف مدیریت موج بازگشت زائران و تسریع در جابه‌جایی مسافران انجام شد.
🔹
مرز مهران در روز گذشته به‌دلیل حجم بالای بازگشت زائران شاهد افزایش تقاضا برای ناوگان حمل‌ونقل بود، اما با استقرار اتوبوس‌های جدید، روند انتقال مسافران به استان‌های مختلف از جمله تهران، مازندران، همدان و زنجان سرعت گرفت.
🔹
استاندار ایلام: ‌هزار و ۲۰۰ دستگاه اتوبوس در پایانه شهید رئیسی برای مدیریت موج بازگشت زائران مستقر شده. شمار رفت‌وآمدها در گذرگاه مرزی مهران از ۲ میلیون و ۱۰۰ هزار نفر عبور کرده است.
🔹
۱۵۰ دستگاه اتوبوس دیگر تا دو ساعت آینده وارد پایانه خواهند شد و ۶۰۰ دستگاه ناوگان نیز در مسیر مرز مهران قرار دارند تا روند انتقال زائران با سرعت بیشتری ادامه پیدا کند.
🔹
براساس آمار اعلام‌شده، در شبانه‌روز گذشته، همزمان با تداوم موج بازگشت زائران اربعین، ۲۰۴ هزار و ۸۴۲ نفر از مرز بین‌المللی مهران تردد کردند؛ در این مدت ۴۶ هزار و ۷۵۸ زائر ایرانی از کشور خارج و ۱۵۵ هزار و ۶۵۶ زائر ایرانی از طریق مرز مهران وارد کشور شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453999" target="_blank">📅 10:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453997">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca61f9402.mp4?token=ubUN-Bs8_b17FRpK2tK9ZU7z15HWy5JeKulbxFunZL2h8zE3NBausFoTJbpSqkMyWPT511eUVrc0D_sjRV9YI374pn4HSy_lSxR5GBShaeN7TVc2pl0NSgEWU0kOEPc_d-CuK1_EyboAUFIq9cxaCwdc40zLZpKdFKV80rDe5L2quwZ2lDLkOlbGY2k9VJVxUMzcqCvZ6Lj3VObZMQj8ikdyy8ACSidXRkkV3D_rKNjrB7RHRwDOBlAnKR1oYcurOfp7xTfcmG2qn6Yq1aoWlLsyq0nOONXFK2JGOGeROZr803cmgDjnW2Y30GhbUin5fsL2iizM4odVrKIy_TUhfKagOzeEtl_E1ixk52TGl2YU3gb17fFugBTWaZNEPs-35_M7Ulrtqno2hxgsG4n862ow2xPr-Td41s_n06Qj1-RETuCIpwhZ27L4gpKBLTpS_4-gViq1R3269uYgCaxfiMtudaFcTMoB1zS7onbXUFy7Cmxy1LYV-d7JZs0chMjsJKJ_GumuBY1YsH6bvOS20QSsfcpHBn3qOAJvt8xBcthV_9VhmefkivKvWaCVlGdA8QcQGKb9lEfYq4B-xGwR6qvgSr-MGLd0wcq6o5UqNWT9XmEGokiH27NidLMhTowtqL5ibnJvc4B8Tn0Q6beef7Q419KqTVNi2GoEnh4aElM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca61f9402.mp4?token=ubUN-Bs8_b17FRpK2tK9ZU7z15HWy5JeKulbxFunZL2h8zE3NBausFoTJbpSqkMyWPT511eUVrc0D_sjRV9YI374pn4HSy_lSxR5GBShaeN7TVc2pl0NSgEWU0kOEPc_d-CuK1_EyboAUFIq9cxaCwdc40zLZpKdFKV80rDe5L2quwZ2lDLkOlbGY2k9VJVxUMzcqCvZ6Lj3VObZMQj8ikdyy8ACSidXRkkV3D_rKNjrB7RHRwDOBlAnKR1oYcurOfp7xTfcmG2qn6Yq1aoWlLsyq0nOONXFK2JGOGeROZr803cmgDjnW2Y30GhbUin5fsL2iizM4odVrKIy_TUhfKagOzeEtl_E1ixk52TGl2YU3gb17fFugBTWaZNEPs-35_M7Ulrtqno2hxgsG4n862ow2xPr-Td41s_n06Qj1-RETuCIpwhZ27L4gpKBLTpS_4-gViq1R3269uYgCaxfiMtudaFcTMoB1zS7onbXUFy7Cmxy1LYV-d7JZs0chMjsJKJ_GumuBY1YsH6bvOS20QSsfcpHBn3qOAJvt8xBcthV_9VhmefkivKvWaCVlGdA8QcQGKb9lEfYq4B-xGwR6qvgSr-MGLd0wcq6o5UqNWT9XmEGokiH27NidLMhTowtqL5ibnJvc4B8Tn0Q6beef7Q419KqTVNi2GoEnh4aElM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات وقیحانۀ سلطنت‌طلبان: ما لشکریان یزید هستیم!
⚠️
هشدار؛ محتوای این کلیپ به‌علت توهین‌های بی‌شرمانه به مقدسات، مناسب کودکان و افراد حساس نیست.
@Fars_plus</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453997" target="_blank">📅 10:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453996">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa10b8ba2.mp4?token=OLg06lE4AB8qgL1FmdCir4qUqX0EUX9R4Uk5H7SiQuzcI2CnQGzz-oHvt-ViwibRlC7l7C5ZTtO7bEKFGj1TB3508tg2_1WgkGduifswSJYllrN_Y9X5HmuW0_KJCFw59RgyrqXwPapmPC8hq-ZM3ZAInJKIW6L_Bg-B8EP039fppUgSkf8Fkf0i2LYBgPcQg6sAXbfuSBAB1c9rEM99kb0aRULNxWox3c8ZSjyJdAS320QxfIISyMqUko-l5dKk-bsNxm9Te0X6d_4O9tXkZFwjEZ9w1wydIxZPqtKVnG1lyMUy6dUW-wspKYZ5Sz2i8hclqf44NuTafY9Yw05FqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa10b8ba2.mp4?token=OLg06lE4AB8qgL1FmdCir4qUqX0EUX9R4Uk5H7SiQuzcI2CnQGzz-oHvt-ViwibRlC7l7C5ZTtO7bEKFGj1TB3508tg2_1WgkGduifswSJYllrN_Y9X5HmuW0_KJCFw59RgyrqXwPapmPC8hq-ZM3ZAInJKIW6L_Bg-B8EP039fppUgSkf8Fkf0i2LYBgPcQg6sAXbfuSBAB1c9rEM99kb0aRULNxWox3c8ZSjyJdAS320QxfIISyMqUko-l5dKk-bsNxm9Te0X6d_4O9tXkZFwjEZ9w1wydIxZPqtKVnG1lyMUy6dUW-wspKYZ5Sz2i8hclqf44NuTafY9Yw05FqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط هواپیما در پرو ۱۱ گردشگر اروپایی را به‌کام مرگ کشاند
🔹
در پی سقوط یک هواپیمای گردشگری در جنوب پرو بر فراز محوطه باستان‌شناسی ثبت‌شده در فهرست میراث جهانی یونسکو، ۱۳ نفر از جمله ۱۱ مسافر و ۲ خلبان جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453996" target="_blank">📅 10:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf35f6e62.mp4?token=oL9tIl9x7fU0PJkrR1RcPfthVgfYgSN82O7tQzKhg31b3U-FB0G2ILsiXpSiNbBcdaFQK3ddXIT0NQ6HzVqImHhOL6myoAYDa4EAzI0Z-MXmtCfBB5Ja7p9Ho-HEzZcR69IK6US4-OPDv9caSUTRw8F_5cwXQuD81OE8Pe3Oq_zBLYFZQLOzc9SM2XLSa5PnEEhLypPCoiOswp3S5vxW1J3vJwSBYgPazLVl557J6mvL4AfXRz1FHufqB-7Phu_e5iXygBS3fCFw_wIU8AGjW62ptYkUhbKoT5vX9Hwe5EIxfGXSP-2oWRLdYY-t1zfIO90VWz54uaYSSSHiGUZxhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf35f6e62.mp4?token=oL9tIl9x7fU0PJkrR1RcPfthVgfYgSN82O7tQzKhg31b3U-FB0G2ILsiXpSiNbBcdaFQK3ddXIT0NQ6HzVqImHhOL6myoAYDa4EAzI0Z-MXmtCfBB5Ja7p9Ho-HEzZcR69IK6US4-OPDv9caSUTRw8F_5cwXQuD81OE8Pe3Oq_zBLYFZQLOzc9SM2XLSa5PnEEhLypPCoiOswp3S5vxW1J3vJwSBYgPazLVl557J6mvL4AfXRz1FHufqB-7Phu_e5iXygBS3fCFw_wIU8AGjW62ptYkUhbKoT5vX9Hwe5EIxfGXSP-2oWRLdYY-t1zfIO90VWz54uaYSSSHiGUZxhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پسرم را از دفترچه‌اش شناسایی کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453994" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89916d3d3f.mp4?token=aPQN8qkSEVrjuXN769aQbwJTr4cJR34dXPwnWL2IWXc_SeejEQmHHl6HH5nAZdq4EajLVtxjuRIUyQEf9SiqyP20aYTVziQI47S9C8msOq3miWZFHhJHDInbD0K7YXYZxozfhEvqTT8etwk9v7WXKQhoXxnF0G2LLfU12JDUjFBQNb2LnihxXKz-UIqIUXzcGtBpIoJYPKkCGb3Q8ogppOnJFm-_1Mr5g6ItUx4fFClD3J51yOOYJef9YKz8bjQlbvDFm-PC9ExSSLQVdfhBoUmLLpewAvKR5WffZILOBV580sgFhK_IFJ6ccLNp5JyQboP4f97IjREOhuf5ys6NTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89916d3d3f.mp4?token=aPQN8qkSEVrjuXN769aQbwJTr4cJR34dXPwnWL2IWXc_SeejEQmHHl6HH5nAZdq4EajLVtxjuRIUyQEf9SiqyP20aYTVziQI47S9C8msOq3miWZFHhJHDInbD0K7YXYZxozfhEvqTT8etwk9v7WXKQhoXxnF0G2LLfU12JDUjFBQNb2LnihxXKz-UIqIUXzcGtBpIoJYPKkCGb3Q8ogppOnJFm-_1Mr5g6ItUx4fFClD3J51yOOYJef9YKz8bjQlbvDFm-PC9ExSSLQVdfhBoUmLLpewAvKR5WffZILOBV580sgFhK_IFJ6ccLNp5JyQboP4f97IjREOhuf5ys6NTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در رستوران آمریکایی با حداقل ۳ کشته
🔹
خشونت مسلحانه در آمریکا این بار یک رستوران فست‌فود در شهر «توئین فالز» را هدف قرار داد و ۳ کشته و ۷ زخمی به‌جا گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453993" target="_blank">📅 09:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlguzSchoEp3c4IQTPtpiKTADwW31kvltn85KadGAtWWAE6mC5OGTj2-HggBAWLHTPdz1vaa49xAAabKV_d44vlXsH21q7L9BLR6OQDC6AFXLl-rEVjWVv4jyhwdZWGjJZFI9lnWHDut-Vlvr7Mk-BYpYDv-wdd6rm75Pwe5mImR_34esZhw8HJrVo7ZnQMLtFHV1vC6R3s-6iIPvBbUpCWqD0UKBR7cYovj-MuU3KxQOEoYci2dQKzQgQ5tGHgeMS_aMw1ckOWXAwGCKPR3_OVJzAOfNlr4f3s-Y28aoxDAE-2aqpzeNDSMcwrFbtbhNfV14CgxuLXA-eRDH70S4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxk8triuNwIlzuRhCBhaWi9QJoDbDH_lvS7-8yjF5g9U33BxTnqH5naWSbk-4-pMHPyhCnGDbyLPsdkUTTLmLEYZPeIRBf6rOZr5TAGFUK_S13Xo_bqI6xrP7aq5xEW0M_7ZUTxAquem0RWagN7mtVWb2ThCW-Ws4soSLbce0Qwh74ZlaDVwvuJlVaNdIFblNAfrnjH3jmvdwaWaM8tixuxE_4Y70OseOR05sQoy7bi7z_NO01MPhYFB1TVi4EhyzzpvcEZJASLek6eZJBqJLX_94pkYWb17kfCNDZAv4koAamuppu6N6g3jMZEjuGtwdEvBa6EkmSs6seH8p_n3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHd5CCqtAzeMHuQZVO6uyUPxFbPo8VOco5UtSBdD20RRDacv7ysOjRdhAlZQSaUOM8e8EYBMkPXpDVr6fan8naNN2ioQ9HR5jlebJwOK5g-1SNgGyihDROg_8Kf5meLWuqH9ugiW7xaqMjN6lq_lhPTzsks39K5vVHLvZdLm-aUAwSpiTmB9xWx1BRY0gf6dr0YeE-NlNJfq-VxOBmUoRWfAUwdo1BrEmjUwc9Ttw8cz5fcNIsp5xwAVQrcC_TCjDyK6dhgAvHdBrjQ7Z05OUtmHK1ZZAA5AhemVrHkqX-M-anXy-3HMPllWvotDcsXZHHXijUHiUKh1tz7zqmMn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdxqpDiTvojLiz61kqZkoophE27dLEK28h29fR4m9Bw26HleIF1BeJdMAfeNTMlJtX5t1MRS1VSpudtlg7SO0CUQxF7IeLdROF0qt_z1pYhd99iM_GKKH75bPMSYXpjo-UHZiWFl5iJu10NDFt46qrsCewjPF4oaw84a_9LIoB6X3A4acE9vlGTnueJyGL1nAGqdM6bVfODXH5uR7MWnt1wAR31TNc1JfrjgErNV543a8qPa9NeOHiIgIizEw1gwYAbLXRjiYoKKzVPBPEqZZKAtZpao4XBUnMKeesZgIbuOuPwZrC4EoqPXwXFYZV1mH9NpblQhBz_2IYzidj6AZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUEu3NRb98eJniG5Jc08tMpiefjD9o-k4NEyx4C-wlFJbAVI6kGUK6B-0-21LCAyDDgs22v1IUMa2r0Pqg2o5Do0wNR-cPIAIPbTGPF0m7t0SS8H1C1Z7qOds7kwn1aZ3a3zbLEy7TujfTcJ-EnLuM82zxQOP9j__DcX0apPxy4fe2gxP5mduh8u1vATloJHBZ1mNsQKRPVAVHjn7zwbI4QikjNizQ8rKeTEhD_YBDjKpdCBZNmeZmKBIR6U4pTFrkKAgm6-_RKhwUF8ghChmfAcDgEDrvrBCIyQQf-n-2QmJchyr9azvhPw69UFg4tk0_4RQdqLPaSXzGDmq7vmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcB4tbwtx_fa66QyXF5LNA1zwiQH1WrJWA-bnfyqZmNk8TgXj4ccWLIbredA7xpD-ysx-J5tppo7bgasuWeocFvM-30KHzQ944Jxhn8XjalINyEnbsz8a51g6DMZdiZBH9zuIIxSondwebz4aevgI9wU7SBPeiLqRDY3AeoSDkV5J1EcTj5q_dIeoaVmlyJX5_b5Ylsqh0T-8PBfdo6zHufCqJqKkR7MxhaTlDIBcFHGJegHFKt-9RKynbkaeXQIY-vCpFupcQUtK4yNqPzJjtKB9bpXDLDqKHKvszg7z9765QePoX132NrvlXOkiQmNN6Su210WFisbankogWm-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gk9xv3tawHot_2etiTF8D50kxAZycfGGG9Jl2wuWgnSq6-38Su0XxOrfwl3z9nWYx9TfMmA5FbG4tRVTurRT2y26SJySUmVEg0aMx-qA4pJo4hqQFcu7NkQI0jo1qG3bHbGQov4jLCLZQG4ySZJwYJ9FRhRGUfUJdppqFEPd47JLvN2eHyTB2kgR-wjxd9i1V58uBoB9OaJT-qm7A_sruhdYAm_Y9-sMfgnm4DvVTJnaytDhVfOliHTMOuRSFx0hJbWeQYA4CGHQaig11AClcaKgx6tusqVlC5sdDsz8h9zIwFt7TBoWhu2JShm4pOzLH4OuiaQ9eOflGBGenlT29g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پایانۀ برون‌استانی در مرز شلمچه
🔹
با راه‌اندازی پایانۀ برون‌استانی در مرز شلمچه با ظرفیت ۱۶۰۰ اتوبوس، زائران بدون نیاز به شهرهای آبادان و خرمشهر از نقطه صفر مرزی به استان‌های مبدأ منتقل خواهند شد.
عکس:
فریدحمود
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453986" target="_blank">📅 09:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDZ-I1V_VTi_BcJ8LjEUAZvvua7JpVReJFG2Ee_hk1VGTjTQKcNUQMDNhM1Jr6gyAxk1vSGI25-fiilmK6tAY9yrLaobdeUhmDrUd-eAh_hgMz_Vj3pwHlsds4ZGXdPYfUv113waEl8Yd1TgvsaJt0-fA4ILCSl-Z9cfLs5li2gvLgs5B8Y5j8EGe9tFlkqiODJhjgRf6lVZ6IobKCluKI2MpQEp8SIzmMVzjNPV7IWv2DD3Sx_5OkD0XCuI0F8qmjmN0R4AFoA0IAwxTlwdnEfRz3NzjbFkGdWjMrzs4Iu4hXCnT5EjsWazdfXFDZyDNkncyIxENRQ7g_5frhU3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع روسیه: از دیشب تا حالا ۶۳۵ پهپاد اوکراینی را بر فراز شهرهای مختلف روسیه سرنگون کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453985" target="_blank">📅 08:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fluwK1M5PnQwjlPq3vw3oJq2_-NIqr7BYpMycRNSrMwbaW-FAvR33THGnm4tqBA4wRv0mR7s0YtIuwm_3xNBUUewn4Z2jcDAGb5Km647tQnGOPEn6x2jTjFevRr-jWovisvqXUlJWb0ZzM7v9PWhFPC_Ja7_GF9zaYwU6ygNv3Kc2lXH9c6r20BTYFe00rPjBUM2u_60ZFznjhhdlvoO8r_qMSVokWoV3QIPHm6VZXp8kNGHAPdc5JSJXlSSQurKKTmZ2pkDghXpzAltJjhEyPq6FNxACp3hVoyZ0Z76G9YqR1XcjFcfjOfdMpvYGt5_1B_t9V5UHQTRsO4OzfrDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت‌نفت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453984" target="_blank">📅 08:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0233813a9.mp4?token=CTwDzf8QAOKKkU07SpJLJnWtDZrytW63T-uQDDXPRWREJFwXR9Vu75OoBMB7Yng1d38fPOsxsc2ZdizoqgZ7FtyToXJ4kE_NPx7jxLnuHQuMohvzvBQ_YIeaJR7_Lbl43U76wFDTkDo_E9nulXLDoGKTPPuEJ4VHBOiQZjtzWibmWZLPp2ukzYJMQ8Le05VQ4vOwYYvk2RQQZgEeni9z2EprJjo05451rT3PZ-CDNAJIqYFZ7V757RkmzjaTSGDn0nHhi_mawgqx0pUgi6QbSJXL-wtaDhYwa6UF2PxWvh2V79cG_3NRTM6CB-dxoixq71YqsInsS6pfHJbrqeicZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0233813a9.mp4?token=CTwDzf8QAOKKkU07SpJLJnWtDZrytW63T-uQDDXPRWREJFwXR9Vu75OoBMB7Yng1d38fPOsxsc2ZdizoqgZ7FtyToXJ4kE_NPx7jxLnuHQuMohvzvBQ_YIeaJR7_Lbl43U76wFDTkDo_E9nulXLDoGKTPPuEJ4VHBOiQZjtzWibmWZLPp2ukzYJMQ8Le05VQ4vOwYYvk2RQQZgEeni9z2EprJjo05451rT3PZ-CDNAJIqYFZ7V757RkmzjaTSGDn0nHhi_mawgqx0pUgi6QbSJXL-wtaDhYwa6UF2PxWvh2V79cG_3NRTM6CB-dxoixq71YqsInsS6pfHJbrqeicZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453983" target="_blank">📅 08:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300b440c0c.mp4?token=SEcmUCfUw5XdGvSPd9ZyqhB1jpdgzYBhjHLAvO4euamufY9ATPqi5mn2gPTbxMNRwCBIoWVv9YxDJYOTqspzvjIL_-m-KTTe-F_JRbI_sS7jc7cXgDWNhDv-zLBlrwVf4t-6T3yOXzxjuLAfBVzBiqOss1-i0CNv7MBZ1QPM4sCQhBle1fkV2QMcUOZ5YCy93Q-VSmv_DxIu6gI2rB_K2ANFfkIDENK6iUodQpTrpKD4narxvHbuxlCCt1g8KaCGaKbz3eTEnyudPIa1vmkq-BWYKxgE55hd-M2ZmBClh13kZmvO-g51dE_ybD1_mgKR41Tc45jWr3aXjyo05w9zZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300b440c0c.mp4?token=SEcmUCfUw5XdGvSPd9ZyqhB1jpdgzYBhjHLAvO4euamufY9ATPqi5mn2gPTbxMNRwCBIoWVv9YxDJYOTqspzvjIL_-m-KTTe-F_JRbI_sS7jc7cXgDWNhDv-zLBlrwVf4t-6T3yOXzxjuLAfBVzBiqOss1-i0CNv7MBZ1QPM4sCQhBle1fkV2QMcUOZ5YCy93Q-VSmv_DxIu6gI2rB_K2ANFfkIDENK6iUodQpTrpKD4narxvHbuxlCCt1g8KaCGaKbz3eTEnyudPIa1vmkq-BWYKxgE55hd-M2ZmBClh13kZmvO-g51dE_ybD1_mgKR41Tc45jWr3aXjyo05w9zZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453982" target="_blank">📅 08:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d82d0e7b.mp4?token=LUn4PHI6Ni4kjnm3fp_JZ2uuHimdXHKo0mNvpqdYUjejOf7kw3nQA_UbjKM8Ot4bKL3oXBxqKGPjfLnkegjtHH2_1tz_pPYridKXIyPzOhNYhgjBdWF048O7iTebK0mdQyWFqVNfvMUy6Cn_GrZVK7kGKl-R8uEUwFZcnLyttNLFuenjAKEaHrBKnei0DD7GHYuHwr5rxwghOOxSeBmnNrklbDlmshHhhqb6PzSqbytp6tmDAEwpMUYTxWqZNYyTePmymFn6funbI6b9DZFiLJvsuaCiofGxO-q0r2x96TJygg2tK51ROvlUOUy5CoRULkha-DdpjLlz6th4i-Y-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d82d0e7b.mp4?token=LUn4PHI6Ni4kjnm3fp_JZ2uuHimdXHKo0mNvpqdYUjejOf7kw3nQA_UbjKM8Ot4bKL3oXBxqKGPjfLnkegjtHH2_1tz_pPYridKXIyPzOhNYhgjBdWF048O7iTebK0mdQyWFqVNfvMUy6Cn_GrZVK7kGKl-R8uEUwFZcnLyttNLFuenjAKEaHrBKnei0DD7GHYuHwr5rxwghOOxSeBmnNrklbDlmshHhhqb6PzSqbytp6tmDAEwpMUYTxWqZNYyTePmymFn6funbI6b9DZFiLJvsuaCiofGxO-q0r2x96TJygg2tK51ROvlUOUy5CoRULkha-DdpjLlz6th4i-Y-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران حسینی از کربلای معلی در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453981" target="_blank">📅 07:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453977">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=IEuWtExKmd90jGaJtHvGL-kaTt-wsyzky_ON87emtSmF2jYFzHair6pTSLmpoOvEKYgvdG2HJBJj6txci5Rnu6ZPtJU8v4BKQT3FCBXlKH3HKjpacUBUiSrPN79CQPz0sVkRRyNfI2MTMbWOKxRnvuDXRP2QowDVVQ8594WPSfAScUD0zb9mofpEzHAr0oHCtWblfP1eCSIHqH3h5QVLyIt9T_BXvXWQrbyUfztOvieRG7IYUfnTMjpvAkqZK46Htctcc7flYhOOikT_0UYs0a-K8qkyqRBgBNKsyM_rmDBbV8XkzSt0goGFP6KqwEL88YSLkKl4rbYjzwok9Ldl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=IEuWtExKmd90jGaJtHvGL-kaTt-wsyzky_ON87emtSmF2jYFzHair6pTSLmpoOvEKYgvdG2HJBJj6txci5Rnu6ZPtJU8v4BKQT3FCBXlKH3HKjpacUBUiSrPN79CQPz0sVkRRyNfI2MTMbWOKxRnvuDXRP2QowDVVQ8594WPSfAScUD0zb9mofpEzHAr0oHCtWblfP1eCSIHqH3h5QVLyIt9T_BXvXWQrbyUfztOvieRG7IYUfnTMjpvAkqZK46Htctcc7flYhOOikT_0UYs0a-K8qkyqRBgBNKsyM_rmDBbV8XkzSt0goGFP6KqwEL88YSLkKl4rbYjzwok9Ldl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
🔹
خبرگزاری آسوشیتدپرس گزارش کرد این آتش‌سوزی حوالی ظهر شنبه به وقت محلی آغاز شد و علف‌ها و بوته‌های یک محوطه باز را سوزاند اما به‌سرعت به‌سمت شمال و شرق و به‌ سوی مناطق مسکونی گسترش یافت.
🔹
مقامات محلی، با اعلام بالاترین سطح هشدار تخلیۀ فوری، خطوط اتوبوسرانی شهری را برای خارج کردن مردم فعال کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453977" target="_blank">📅 07:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453976">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtgEdEt44DjOiTbl7JyhImDXOKBJ5mPoyYIw5Hxs4Wjbd_Q7e0IbHoBlIBbgK9akq-3i3dvVtD0juwp5ff4hzc_13FnGz7wP_DQSIHfywyKelOfZBdYiVQay5ffaUB5_whtWXIoYXGnKudllJbqoTSuJOB4wCPizszEoDvZ8rx_DOzlYTNv82UFIUYS2ssZHNazvUOutwm9pnbKyeyKIHdYc8sx4dEq1BHFkCUp2XhaONftPiM8AKBOfcjQ8MzhJPhOkZZf5GArD6jTo4g_3zNZYVwl2SYmw_I31VubCZXokz_Us9SAA7eJ-nrnOE98Pkk3ow3F8w1mcZ5SN2KxCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا با طناب ترامپ به چاه افتاد
🔹
نشریۀ تلگراف از تصمیم قاطع یوفا دربارۀ رئیس فیفا بعد از طرح فروش جام‌جهانی خبر داد و نوشت: زمان اخراج اینفانتینو رسیده است!
🔹
طرح فروش حقوق تجاری جام‌جهانی به شرکت برادر داماد ترامپ، هفتۀ گذشته از سوی رئیس فیفا مطرح شد اما بلافاصله با مخالفت یوفا، کونکاکاف و AFC همراه شد.
🔹
یوفا حتی تهدید به کناره‌گیری از جام‌جهانی کرد تا رئیس فیفا بعد از تنها ۴ روز از ارائۀ آن، توقف و شکست این پروژه را اعلام کند.
🔹
اما جایگاه اینفانتینو وقتی به خطر افتاد که رابطه‌های مشکوک و سیاسی‌اش با ترامپ آغاز شد. او چندین مرتبه از سوی اعضای فیفا به‌خاطر اهدای جایزه من‌درآوردی صلح به ترامپ و بخشیدن کارت قرمز مهاجم آمریکا در ایام جام‌جهانی بازخواست شده بود.
🔹
نشریۀ تلگراف می‌نویسد که عقب‌نشینی رئیس فیفا از این طرح کافی نبود چون اعضای یوفا احساس خیانت از سوی اینفانتینو می‌کنند و می‌خواهند او استعفایش را بدهد یا مجبور به اخراجش می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453976" target="_blank">📅 06:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453975">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای پیشین خود مدعی شد: ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم.
🔹
او سپس با کنار هم قرار دادن لیست آرزوهای خود، ادعا کرد که طبق تفاهم‌نامه، باید تنگۀ هرمز فورا و کامل بازگشایی شده و تهدید هسته‌ای ایران پایان یابد.
🔹
رئیس‌جمهور آمریکا در ادامۀ پریشان‌گویی خود، افزود: بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/453975" target="_blank">📅 06:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453974">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvstMSeGgFEsN9jQj7Y3tyk__xc24cNCiAMFj0DPyJvP4VkOjzjFGNyACnYXmhmvum9pcBjuR7Hqw0A7KVvFxkeYpoJeWzWzNg57VKD6puEAlkYunNVWbUSqBzM6K81WDmWhF0D5Yg4iT0WspKsmbS2S41gHegI1kzYKPQW4z2AwbajNq2j4eYhhtNGhEYgTrwOjx0_qmd14EiUyeJ2fRdpn1_X_IohF6E_XDf8QoFk8fE9y9s9Y5vaJuPGH5kdnA5uJzGapwsTGIqyLZ-ZPdlMkCFPVQXeFmXUQnJPkjLHmRuiE-lhdKoxWBd4tpI6lRZsJNRI8CuXrgRsTRfhfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۸ ریشتری در تخت هرمزگان
🔹
ساعت ۵:۰۷ دقیقۀ بامداد امروز، زمین‌لرزه‌ای به بزرگی ۳.۸ ریشتر و در عمق ۱۰ کیلومتری زمین، حوالی تخت در استان هرمزگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/453974" target="_blank">📅 05:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453972">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/432d846a83.mp4?token=KXabJfTi5bwV7UV3fg3z2uiUJ8wzIia6U1_pGdev2B9bjkWGshmjmOSFUVlkByTQjWBdwcdFIWbgDtX5c3MWratUkp7_RalyB3-9q-nnrR-jRsA6VN8wPIBn5QncTwBosVR6OOHFAA4Q5cAvN_zO7elZ_HRNJ-gb2eIxwndeFONECH8xbjC_fAhzKOrLK5HlItRPetCYh3hoaXbMV4Vzu9COaFU3nqVPJ9WMXxE7yutFwOz03AjoEQG419qDyFncxA4L6g41-ToON9UUnUJEdD_AiNIZ0lgFd0fJPMt9EMgEPb9e83-av1E60UyYtiI-LkU60QOFsu-Fk2NQwdgFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/432d846a83.mp4?token=KXabJfTi5bwV7UV3fg3z2uiUJ8wzIia6U1_pGdev2B9bjkWGshmjmOSFUVlkByTQjWBdwcdFIWbgDtX5c3MWratUkp7_RalyB3-9q-nnrR-jRsA6VN8wPIBn5QncTwBosVR6OOHFAA4Q5cAvN_zO7elZ_HRNJ-gb2eIxwndeFONECH8xbjC_fAhzKOrLK5HlItRPetCYh3hoaXbMV4Vzu9COaFU3nqVPJ9WMXxE7yutFwOz03AjoEQG419qDyFncxA4L6g41-ToON9UUnUJEdD_AiNIZ0lgFd0fJPMt9EMgEPb9e83-av1E60UyYtiI-LkU60QOFsu-Fk2NQwdgFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری شدید نیروهای ارتش و انصارالله یمن با عناصر وابسته به ریاض
🔹
منابع یمنی از درگیری شدید میان نیروهای ارتش و انصارالله با شبه‌نظامیان وابسته به ریاض در مناطق جبل هان، مدرات، البرح و جبل حبشی در غرب شهر تعز (جنوب غرب یمن) خبر می‌دهند.
🔹
این دومین درگیری شدید زمینی طی دو هفته اخیر میان دو طرف محسوب می‌شود.
🔹
پیش از این گزارش‌هایی از آمادگی هر دو جبهه برای ورود دوباره به درگیری زمینی منتشر شده بود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453972" target="_blank">📅 05:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453971">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
حال‌وهوای مسیر نجف به کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453971" target="_blank">📅 03:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453970">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHs1Yu8x4z5Zs8DaaWL8PXj3mtZk1gdfqZKkCsT5Hc0YspTOg8dnqjJqm7x1o3oG2cbfPHBReBCuMRjhqEgKhnEdCdiQG7O5pvImQ-rLlQ97O2ifnstdVPXqLRVTfq0ACRwviGQeVLpyoqd5N1b5w-zvrKhjFxXZ21XUzwg-Fg7vbNgNO-Hb4-qpaT6GUKh78Er-_SEP3fDTOlHcl-dLI_Bv-giSWtYIXOW7Radzp91WSsU2oUf6irtCiQ7h35jZCRlQXkWMjJw7_c5ei4qbIbFUbdW-V6pJSimJKrHTl7OSnDWqRp4_O-PveiPxc94r4_jbvNa0o_WSUPytVMbMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان و هنر ائتلاف‌سازی‌های بی‌سرانجام
🔹
عربستان سعودی دوباره از تشکیل یک ائتلاف بین‌المللی خبر داده که هدف اعلام‌شده‌اش حفاظت از امنیت دریانوردی در دریای سرخ، تنگۀ باب‌المندب و خلیج عدن است.
🔹
این اقدام پس از آن انجام شد که نیروهای دولت یمن عربستان را محاصرۀ دریایی کردند و چند حمله به کشتی‌های مرتبط با ریاض صورت گرفت.
🔹
اما این کار، بار دیگر همان الگوی قدیمی و آشنای عربستان در ساختن ائتلاف‌ها را نشان می‌دهد. بررسی رفتار گذشته ریاض و روش‌های قبلی‌اش در ائتلاف‌سازی، این پرسش اساسی را پیش می‌کشد: آیا این ساختارهای پیشنهادی عربستان واقعاً می‌توانند یک کارایی عملیاتی و ماندگار داشته باشند، یا این اقدام صرفاً یک مانور سیاسی است تا ضعف‌های بنیادی ریاض پوشانده شود و هزینه‌های امنیتی‌اش بر دوش دیگران بیفتد؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/453970" target="_blank">📅 02:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453969">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابع عراقی از حملۀ پهپادی دوباره به پایگاه‌های تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453969" target="_blank">📅 02:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453968">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منابع عراقی: صدای انفجارهای جدید در سلیمانیۀ عراق به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453968" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453967">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0af910028.mp4?token=J2-yjb3zoineTbbWh9b3_PHfaoSsxz7Gbsu4RJvi0-TEJ060-34eWauKpXRFLG5F6RYpfYjCcYVYL_tPVufK3yvqwvr_KSDEqo9JMoDvf0XU7XWrPr1JxTXGVVNiX_2iklSi6NgMtTzBaqdz0UcQSvlZFcBoZO6HCHk1uHnVEecBdGqewWFlxiQv9xZyDVRF0NHUMflhqsO7Es9xHgQ4J-ZFQ82PnCCU3jTYBjlRNHyPNcXRB-GbmU_naPH6WkmD2ZPQH9TZNr0pJ7y18CC7K6w-RZAVcUuUNbrkq6JuVZHEC9OmgwFnmTbwVz51CZOtIZYQfkUunlm7aIpk5bwRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0af910028.mp4?token=J2-yjb3zoineTbbWh9b3_PHfaoSsxz7Gbsu4RJvi0-TEJ060-34eWauKpXRFLG5F6RYpfYjCcYVYL_tPVufK3yvqwvr_KSDEqo9JMoDvf0XU7XWrPr1JxTXGVVNiX_2iklSi6NgMtTzBaqdz0UcQSvlZFcBoZO6HCHk1uHnVEecBdGqewWFlxiQv9xZyDVRF0NHUMflhqsO7Es9xHgQ4J-ZFQ82PnCCU3jTYBjlRNHyPNcXRB-GbmU_naPH6WkmD2ZPQH9TZNr0pJ7y18CC7K6w-RZAVcUuUNbrkq6JuVZHEC9OmgwFnmTbwVz51CZOtIZYQfkUunlm7aIpk5bwRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق  @Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453967" target="_blank">📅 02:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453966">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUlE5C2Ni298xJ2C3Wrevps6qSUygNLFc5C9ra3EFNtGvnTCQOTqMbwyCOyXZioLnFKsSKdvL1qJ2etNAOtewKbHNYmzQSNow_Dmm_w9etjoeABbxsinz5zdyh4mNYQnDTT3lmIPelBGLQM7SfX7jiPM5lqIfx5vp3fUreLZM5DzhhaP4bc3WVhr2VYRZRjGOsOgeMkTkCVS7bX_IcyBnO8UP9hFTV8FLKRnEi1qla--nxnJj23WpvkpSP2JyerrM2pc0EgkLE2EHHrzgbpMnsKs3FynlAX_YDLPstXasd1QUfFctyrVT008xkiR3N8XK8HbkPaeE0ykPphORVO8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: اجازۀ استفاده از خاک و آسمان خود علیه همسایگان را نمی‌دهیم
🔹
نخست‌وزیر و فرماندۀ کل نیروهای مسلح عراق از آمادگی این کشور برای مقابله با هرگونه تهدید علیه کشورهای همسایه خبر داد و دستور تشکیل یک کمیتۀ امنیتی مشترک برای مدیریت چالش‌های پیش‌رو را صادر کرد.
🔹
وی همچنین خواستار تدوین سازوکارهای بازدارنده‌ای شد که از تکرار چنین مواردی یا هرگونه نقض احتمالی در آینده جلوگیری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453966" target="_blank">📅 02:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453965">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=ozKTp1sqPTOZJHyQ2DcK82B_A8lGutE6EBY7wZFy00ZjPhUbiUq7SwiCBhVbvcggBViaNTG75ZBSJrYeZvN4dXs7uVELwbZMj-blXJmwvenZoc3oooauXMTYhg4c08WR0wgIuh6LTwtpBYM56HYCpl2tSr3kJPMdHBbxfg6m5kaAXrb81cCFYKyruq6Bp4-oHJKXgrYn8gSSChR3CCrddleNf9IMmMTyIzYeGVi9Q6i73OlMnFQ7Wkg6ZOHxZtZd4X8XqtLrXlVYXBvSWq6K6ROVJTgDyCRzXtQNLSjFXFxyeL9hyLh9JR2wS1yokTJkzB2b5FNR6xieYhfNJKS5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=ozKTp1sqPTOZJHyQ2DcK82B_A8lGutE6EBY7wZFy00ZjPhUbiUq7SwiCBhVbvcggBViaNTG75ZBSJrYeZvN4dXs7uVELwbZMj-blXJmwvenZoc3oooauXMTYhg4c08WR0wgIuh6LTwtpBYM56HYCpl2tSr3kJPMdHBbxfg6m5kaAXrb81cCFYKyruq6Bp4-oHJKXgrYn8gSSChR3CCrddleNf9IMmMTyIzYeGVi9Q6i73OlMnFQ7Wkg6ZOHxZtZd4X8XqtLrXlVYXBvSWq6K6ROVJTgDyCRzXtQNLSjFXFxyeL9hyLh9JR2wS1yokTJkzB2b5FNR6xieYhfNJKS5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زبانه‌کشیدن شعله‌های آتش از پایگاه‌های تروریست‌های ضدایرانی در سلیمانیۀ عراق  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/453965" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453964">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453964" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453963">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d49a247c3.mp4?token=F1YXUFZHaFhU-FSI9ecrsMxzgSzXpdsL9NYiERYaCaxMLBZktC4gTt9OmCj4HjjE5Dx-S04XG_kRXSrtIxR2rrXWNjIYOCxSYMfhsvarYIVVzw3Uwcpv0O5zP_50aXQ7fturkca4_adFqgDtOo7jP9hDt-O6ZMU0g0rpGUYQhpxaoIWSvJH0HLaxhXhbMrbiADGUtcuVA2cTlHljW4dnw4rhX3PCWkwFwfoW-ZSCk8s-xHH_tbN8zyUoIJI5Xny-P2sYZk80fx9UYZLSNbHhs-D3W9HAJCa29RbMMULwpF2xSbS27gBqt-GY5uZ3_-qyeUJkDkxUMFPnCYwaY6vSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d49a247c3.mp4?token=F1YXUFZHaFhU-FSI9ecrsMxzgSzXpdsL9NYiERYaCaxMLBZktC4gTt9OmCj4HjjE5Dx-S04XG_kRXSrtIxR2rrXWNjIYOCxSYMfhsvarYIVVzw3Uwcpv0O5zP_50aXQ7fturkca4_adFqgDtOo7jP9hDt-O6ZMU0g0rpGUYQhpxaoIWSvJH0HLaxhXhbMrbiADGUtcuVA2cTlHljW4dnw4rhX3PCWkwFwfoW-ZSCk8s-xHH_tbN8zyUoIJI5Xny-P2sYZk80fx9UYZLSNbHhs-D3W9HAJCa29RbMMULwpF2xSbS27gBqt-GY5uZ3_-qyeUJkDkxUMFPnCYwaY6vSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453963" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/453961" target="_blank">📅 01:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrbH-xgZ89etm5JUgoXjRs5CxVaeezilohIThkC71_mW5i1SNh-mMVyUHvGtZHwN7na5hd66b4b1gTfTsrqH26ftwqfVaYs7b8K5TEUbtcwuVnBwhKewefGpxLAGFGs4H22UuWTylU7tFsW-lDoYzMtkYo5zQ4JGneNQPRHAnnwH_ziRDcEJgqAeA3wiLt05tDZemymwFTZ6dbPOOJY7LA3ZOkYxG6U4obAwSq7RNv9jwrMVgVkWnolFuCwOFFoSEG7tRvV5QLHrKGDmBkI-O2Cy0t8Mcesj6GOZJDfnqjV2VJOksvRvu1GHKuofNsH_E4EJKRCOMsDSh6ohFIfnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاراگیری ترامپ در تنگه و توکیو
🔹
عکسی که از میز وزیر خزانه‌داری آمریکا لو رفت، بیش از یک دستور ارزی بود و نقشۀ راه خودویرانگری اقتصادی واشنگتن در مواجهه با ژاپن، ایران و بازارهای جهانی را به نمایش گذاشت.
🔹
دلارپاشی ۵ تا ۱۰ میلیاردی برای نجات ین ژاپن؛ اما این دلارپاشی چیزی است که پرده از پاشنه‌آشیل اقتصاد آمریکا بر می‌دارد.
🔹
دلارپاشی آمریکا در بازار ژاپن صرفا یک کمک خیرخواهانه نیست و از یک زنگ خطر بزرگ برای اقتصاد آمریکا خبر می‌‎دهد.
🔹
حالا زنگ خطر چیست؟ ارزش ین در ژاپن به کمترین میزان در ۴۰ سال اخیر رسیده، ژاپن یا باید دلار به بازار تزریق کند و مثل ایران جلوی ریزش پول ملی خود را بگیرد یا نرخ بهره را افزایش دهد؛ اگر نرخ بهرۀ ژاپن افزایش پیدا کند، نرخ بهرۀ اوراق خزانه‌داری آمریکا افزایش پیدا می‌کند، و این افزایش به منزلۀ افزایش تورم در آمریکا، شکل‌گیری تورم و مهم‌تر از همه یک عامل مخرب بزرگ برای بازار بورس آمریکا است.
🔸
اما مکانیزم دقیق انتقال فشار از ژاپن به آمریکا چیست؟ این تهدید تا چه حد برای بورس آمریکا مرگبار است؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453960" target="_blank">📅 01:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQL8r6VguvGlUD12KjibKK5Wk34C-NR7ThdBLKIJibPiBowhM5Dbg8ovN3facSb8_aAir_JPP12xrrvAWXDVUuZ6B0mq8SkmSvGe2_TXiFsMS6EBuZ9ocNNOO_rsv_Ac0t6PWFszHs1-O5Iq2IvsUQBjLdwnaM8LLq0DjDrS7AG2FEFINgOhlLscrxCVNnbkJ9-VrujLGA74MpGnX9oqnFSNzMV1K65acHBL9-qnEKxbCVYPohhrgPUt8qDl90k3a4Bzf0r7894eT2-qStrHFcq8xZfJsxxXEJorQVZxI-dBrEcjDB8dURZ9ZDH7XuEDg0hSoN7N0CzvM_bZfXmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولان هواپیمای جاسوسی آمریکایی در آسمان عربستان
🔹
بر اساس داده‌های ناوبری هوایی، دقایقی پیش یک فروند هواپیمای آواکس آمریکا در آسمان عربستان به مقصد یمن رصد شد.
🔸
آمریکا این هواپیما را از سال‌ها پیش برای جاسوسی هوایی و به عنوان رادار متحرک طراحی و استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453959" target="_blank">📅 01:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELTwu8UA-y8c860sJtwi9JJhyC-44ytG6WxXtUdsmFGw8PZ30g3ajoJMR_DhvCNTwFkFkuu6zPYsaLdb-jK1brlLPvA5lCT8QcoX9HHNuM75gs7Fm3ZNmNgl7OpB6EH7arlHHEYZ1yupOep4i0UbalT672O3WvXsYxgC4cHxWXmWU3Q1yAnAONauutG4SIcpio2MktSJ4VPE5Z2aAfLFCp56GApf5bi3Cb69iVxiY52CRDusOUqAgZQMmMGlbqmBzh2Nf2bqt6RWlI2zRu015cxt5l4qQjWRaA2UnF-bhyxG9Op7pjoHpdrQn6xzIQAZwsKJbxxdFyul1jAzgJ8Vng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLedsbAbYcwZY79V2e0kZxG5TpVEUx2xpoAATWkG6MbRHbXh3S2Kflg7obHtN-91gLD8-6O1YhhhG59ZDd8vhaLsipJ5_biFlLnYiYRZrHrK-Ih7Pm1qsZRXwiOf8wPYmP3drmp4kfE-plPyxu98Jn0lWo-z-64zkyhkav1eB4ngfpxyFaXDFNFPK8qIVbTWgW55H_RElKPMCIgKlERW1VS_M9I6eH05zXAitvciLRxVd5Jt3Jtrny46q2iMqGywoFhxPf1Zv3ojSQwQv-ZHyKLv9JaypEtLjlwtNzE4vmUtNvcE5994J4UcYFm_Y4nyHR6jT2NX_TbvBsI4NytLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-8RflWjlNZ80fWsxJSBAGugvDfpHQ-5TbButMJkJCzwb3sSCi28oIM5pht7_WEGOj9E2WTF8KlltNZmRr1aMKiSfJlAoYTvfweSDudQNiOvhGhostPPSoP6GJKl-qWR31B0yqrxr3ouvrqfFJviqHoLGBdQ-JOTVn3ICXWVtS0567RkaySsRfZOTxwSFhUcce54ffQBRh7uXI1xNgpx2wy9iMjkVNySv4TaPKAcALMKK-UqaRPd41PmdPDo2UHUIN-LPsRnm57G0udzLX6EFKtf6TKgCiyKpSMiWPK6lqk229tFKsA8fDNVBW3gc5sYpZV7qkDrMG3r7sX31pfhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arLFzp_gGcemIom0qcMBoPKULBCWhxhspimlh4Q1qQ63dsijewYCML2eQz46lGmDm8e0lo-sI-YXK3NW275QSj1qZOK7dfHBXb5sDN8nFBIo2EhlQ3ZznP0tKod4FwF0uocON3DBC0hdb7NVaY348gg3VJYYf0efE4UaNREKcJXDA9KAAJF8o2GkV4axiyH9IrV3NDlw7ipSoPjS9RJNKy9xhU429gJ-8bjS08f_Ax41WT4kO6ctfx8efM-4m7cJZ1LzanvA86rwpstwbhiwkMCuJN2g2g0fosj9rF_jgDcY76YDgkBCoN5Cu9JHTXmIypQdomrcMJ-bV4w_9NdYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLoo3EvwHVwvSaaHaloZDyQcCrDMiHOmrs0xKAhBQBDOE1-2uOgoUDPf_zk8BB8NvgxmwtzOcZlrsGfZP9E96gHXGazECXA6wjD8kATmS8C6zxGGmQvrCmoCxmna5Mlg-c13FNeR3EIvb9tb2dbhNBnF9s4g9mO-tPtVoHcsqv-Iv_qYpgXmXboSq5slfSncGCn13scGN84sf7T5P7-sKfFCl9nOfJduy0ruLJysAF3z-OMGgKRVQnKAxl7jJU1-uf2Fv5G_UqruqPFOGYYixsUaXUb3ltxjBN1ZpT5-FzddWj6VMEjLqLGvG_zU-BM6neEXL-E1783mAeCL7p9ulA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۱۱ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453954" target="_blank">📅 01:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNzaI0BJ0wKEA9NTWHGtNvAUGfDou8mhFWwua1mN1DO_Mb3WPDc16z3CPndQiuAO2GBHtnSpFQXSl1JQAnKEu5VjITOfLpLfGHmVP5M3RxDQp7oAWjgBpzl1weMSp5HbkeWnFhKYnjMPsVqvIbCrYpkreOQcO6pcdOPXB1LankomK30h43AATUN6NW4FZ2qJbFY3Sd1FpENLNo8ZT5Fx2mYTNEL9aK5455F-P-_nKdZY5PjMs2CrpNsiceNcbHpzEO0F5byKrp8oX9ob7bIwl5gzJe3HCJtKEHqeUsGPzKwjdaJglGOma6k39jKM24bZpdi4_W3RQ8g79ZLksIzQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBm9WrAAydCg6-vxiWnkqp8ocI9Rgmp3JfSK0ZNdYm9fynqxgL9VMIY9SUIm4Q2nCLkcIlvgDX3df1QgrbGcL1C_W_9VADEZe3XXPNMt7KIcXzYKRdjvTjH_K3MV7NfJ9slBRnq_5_JEvFXFzb98_Be4uRiJJNQ2xJdeGT_G3tdcsqq1xnkIMprvqpuOCzAiDyy3ABe365gOnSoJ-SpxLNJwvqWTw8pfTwc0vslqz-NAH80xfOYDANB3vH3-R9RaFRIB8yMfeWcIYg09y2Pr6gIj37YnUrZNPIevCba1qF8xSfFv1VRKze_Sgm9JwgQnKw4y0Plu5iKOnfzkntzyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBx7ishttq8VRfT0iyZjGm15WbLG0SPAtClVrJz1LCsuuzGAN6jyPXhhp_JD7_twBuvYyfiD97EKfw1bSYNMRoBBN1hb2gW8QyBgmqWw3fzVY6gKUmc5Gwk2i7aNQF9U1fbGV6aPolnjCMHtIQEw4HvPrYMIxPHorZ4m_k8q0DSaN01blH4nvc7xmGURQKatWlmbknfH7mUzPK9zYWGlQWIVU5rm6vKxDRy7vh4DORLaqmwd-i4tK2_nolcLRc4cL_TypziRWa19NnwXma22BqLebJ7kIpD53PZJ8iGt9t2JVp_9BlPz_aKkMhfxC3Ov_rWUFIO8rjtDlldqPQJOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlHWCIy8EgulpaTfM1uegwYCnmvaGIWo7wq84Iqcj9lSAPhqE-742bxflGuFQLWOiwke03X80YO3IdIn8PZuhm5m9IggqPMm-ZeYZf6hYSO-cR4QjQ40TGDZplxlbffpTb5L5HGLVUwkpUn1K1L5u_hqTUiRRhGVEjrVtOGkrOAuYykzfnaHmjg9WKNXNi-BoZX4zRKw7flZ_hLepds1dLBO6OdWW0yCYYJ547MJ1QxmDpaxHj1NGFdSN5tRkaxsLvNzEgcBtCsb74slRtoI1B2PhnD6QpNgdc8ES9F5HqFu1RIn4jiEGtM7mktcNmq5JWV_8scc9ujSIlEDNpGRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZi8rYzLh0wdsdCuAIc-puLN4MczRQtf9Pg2XvR5ELCKlTmkr7ccI_SZdYGipKp2z09lWt6EYPP6GJgIcEL0LkuZ24kNoiY_Ea_z7Y-iD79qwELOzNyQ16l6y4CrXanucaAoAXO4OGnW48kgQsJXnrzTWEO4x0DUe_483_p6poP-SAY5T0uyJfxFkUN2hcb2fVWA2DouyekMY49fzAq9EyMd4Z2gH7KnXOBcuZb302nsN9N5v_S8eSDbFvWXxOSUqYOuTjchrk84kl1kTYAq9ocZ_Nr-lwu8DW4Pq1MctqNGKR7aRam78K2vngeJKT4v5N6jFo3G7AET8JOJJ--LGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hInT94kMjSmjvdgFSDWAhE8hP0LNg1KkSB_Z9n82fzLGUS9qNqf2zyjz_TERVOSrxV6yB_SwARgU5A5WCeDK4F-funyzdRPDM9-bEogDjvfARN_3YV-H8dcpSu6EK80-xCp6ftISYu8EqgMWhVl_GS45DgSzUydcGZQ4RR20pFRdg65Xv_cRjUtdYTrKP_oapvqgwjRaxpDZ1DlciVGM-GDUTOXm4qGwMUR234jRn4vvdjqBLtob6zg3CboSYzTIBUQ10f19Y8HSgKaAr0HaNTbYCRoU4a4xwQ1DMEQwvolQm93fGq7GniuFq2vn-7UdQFlPCmYPBRl1_MiPzcszpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXXllyZ7fGyOz4XH5Uut5_2jkenvtNUlE0XQFrDqHOR6Y531bJw7IO3K_0eXM3Ll9VdPT1wyH925LhIzWt3xN6ZEMN19s6RBQj7E_QtSm25FVClkHvcU4Hrm4msWzv4-1XwCjkU6cBd7UakZmkeRaFLIaBDjzGolyj-1ooaLIk1zW-rc0lrUN413yXRSIyezT0nks4R-hNkoEEbdtR9eulE3iJ0TJ-tY_jSLnWZoDCjdivSIdygZmSfm1UAn08s0O53Y1ca5GrQVN-49kCqcM57WZ1MuQLD43zhmnscv5KURTRMhEgTpk8wsJp5skTwBSHlZTDghLQm9sRIiVtq97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcrTqBJv4bb86N0dd_ph6ltctWyKzBlzLheRJFgOoW1_vEaC0lnekdU6Dkgwi49GV9Fcy-xrcv93MQO8H0AfIEbcWWrowyXmdRHoeXPyIjPS8OW1NLYqESPiv-iYPvYOPrYZbffUzR8vPGxzn4WBcPj2na4NrXm-iF1maElAIFnWbKrIovAJQJJ-lSeEGeCn-cfWcmyfEp26ihqxLrZj9GRpygjXw7Usqd_LgnCMqIvHpyzW5heObkV7OQxLZywFRpBsbKuNXWqvnUqkpqQz3DZdQs-eT5FpC4_BYjhueWJQ_UZcm4imhKKTZ4RAvcbqejmqYGyQMPQ0kLrtjwcSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0Vr4uyAL5yvHNm5tIgemweOPU4cypQ_-iXUmJAxnn9bGXF3sEPUw9WsQ3ORojNMVqHaAMQaOfpkTydOM1uF6j9CSSYOr3QU4jciM7ddsr8go9sERLxBZy94IDr-WeS_SeeRQrWMaqoH3_w5FAfSWq-Yf6ubzH5ed9cQJAl2J6GRSUOUtzkwyySQ9Ay1OXL2FuIOuoGDhELDcUAt5ya4DTx5WIeKh-XLHOP9Wqnj9-QdbXyDUbwkwMhH09rBeL8iUESpBeq85HKpY-6HKUldScKrZ3SyHUEj5uYk8vl3tTIRaQXlSlOXUNZmXzcsAyMNSw5-SSobm2PuafeEODMgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VRk3gLGpyviYi9MOkSQZJSZeRZVWhB-DJdHX0Cx-y0TI0waOxoaLrV891mIm9Z5YzAJH__x14tueal5xAGAb7dw2QeOJUv8jJ8Ca9LRCgzAKRiwCe3FW0xUDMNQs4_oN8Wxc6cIlXXs0YhoGt0k0MHSRHhAkbG-6n3Ov-iTR6bQuNfhumi0IQxfhPyJZ0X5OT9nVgPcAYtMaArgZgtSrhVSA2np-LqHmzIW7KhSXjpXzQYu-qLtpog9CQTn2wf1w0fdx98emBprCmwVLucj8zP1tm4i-bBCEy2vHkmjy75U2C7pdo5O7RSh2fSmJbgDtEYU4zngt-iRjJhymsL2Ehg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453944" target="_blank">📅 01:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جسد یک نظامی اسرائیلی در جنوب فلسطین اشغالی پیدا شد
🔹
به گفتۀ منابع عبری، شامگاه شنبه جسد یک نظامی رژیم اشغالگر در حالی‌که سلاح شخصی‌اش در کنارش بود در اطراف بئرالسبع یافت شده است.
🔹
به گفته این منابع، احتمال خودکشی این نظامی وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453943" target="_blank">📅 01:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc824939.mp4?token=MWBKzKN2OJGZDfEp4SyYCn1BuxkRRnQq7ucccjerJzBFs10aEICFGSMPaHaNNR0U80aOmED6sKnuFWrUmH-EUFy6w1FgnvfWTlsjG85vPbIneGlN0PbyQIwDtyWLT5DysNX3HBFpJn2vyxkY9-J-__8-sX_xDsSGIHeinMiJlrygenOgisssCMqBiMWIxGofS4iFIxt4HGVzSVxUQKGRERA3jMaADfvI-SCfhOEdUx7V_6-AST795S6qiUhg49gu4nKyuDsKRgAXEDTrrVlQsWVRZImuJs0ay36uWrkSHetI0KSPp8ncy5URMLRbGWzkcoNXEQQOQHa8b-OHK4YEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc824939.mp4?token=MWBKzKN2OJGZDfEp4SyYCn1BuxkRRnQq7ucccjerJzBFs10aEICFGSMPaHaNNR0U80aOmED6sKnuFWrUmH-EUFy6w1FgnvfWTlsjG85vPbIneGlN0PbyQIwDtyWLT5DysNX3HBFpJn2vyxkY9-J-__8-sX_xDsSGIHeinMiJlrygenOgisssCMqBiMWIxGofS4iFIxt4HGVzSVxUQKGRERA3jMaADfvI-SCfhOEdUx7V_6-AST795S6qiUhg49gu4nKyuDsKRgAXEDTrrVlQsWVRZImuJs0ay36uWrkSHetI0KSPp8ncy5URMLRbGWzkcoNXEQQOQHa8b-OHK4YEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های سرخ انتقام‌خواهی بر دوش زوار اربعین
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453942" target="_blank">📅 00:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2ZCHyGl3qiHdkiQ3vpSOQVQxlcaoscEVeN0fm4yQ669Sexpoj3h9CrmYJqlknsGzXru4y77AkTegn9iCPW0JnUhvCEI6gwwQACmsLMfnvhuz-dGn85jcxSHxWMRjMY8pw2NLYJbD9DIqtP9CINEBsR85TSJeIB_nwsenmxjA5Z_nt_o42SxWejUsx1H2FdoKa9GxZsvz1mcvKfwdB0_F6GFhIC77_soH1hDxBTbk9zgjznghNeDd3i77YWwHK71G4vuRYSMPaYtyZGWE2zTQjkqS1op0jd6EpHEzPD06FK_wAm5H-vx6iXn2a7UYQmr7NJA8zXt8THz1w0eY3ShSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرساخت‌های آبی آمریکا هک شد
🔹
ایالت میشیگان روز شنبه اعلام کرد که ۹ سیستم آبی این ایالت هدف حملات سایبری قرار گرفته‌اند.
🔹
این حملات کمتر از یک هفته پس از آن رخ داد که مقامات مینه‌سوتا از هدف قرار گرفتن بیش از ۳۰ سیستم آبی در این ایالت خبر دادند.
🔹
در مینه‌سوتا، شهر براهام برای چند ساعت از ساکنان خواسته شد مصرف آب را به حداقل برسانند؛ چرا که مهاجمان با هدف قرار دادن کنترل‌های عملیاتی، سیستم چاه و تصفیه‌خانه را از کار انداخته بودند.
🔹
بر اساس گزارش نیویورک تایمز، این حملات حداقل هفت ایالت را تحت تأثیر قرار داده و ممکن است دامنۀ آن بسیار گسترده‌تر باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/453941" target="_blank">📅 00:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL1quL419-EPlyZ8XtwfcSqaETQ4X_VL4g63UQjT03Cg8Jn_MLM7RLPi6ugj3HD6PtQK5ywBC0nmz3fyzbcSNj9HQAvv2DOyXsGVigfogI_njuYEuNajab3WQ6y5whK8BgSIGCD9KzECrR-fTHxiGOnMABjkPuHVRKwZV4wbwZnyYiHFw-IAXkWayf5LNh8blFDJAf-OdJwoecf_JOd6y-Spp3fC2foxvPj_14xDIQoKunZcRYtO8Wq9cMiKwCFEIiJreVFAeIoTyi4qYQzrTVGQWEPaNBQZX6xmyu-Nv3K3wxMd5gB7htyEOLIm1c-jAiZRsoMG3kJizeI9-_NhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در گفت‌وگو با همتای سعودی: مشارکت کشورهای منطقه با آمریکا و اسرائیل، با پاسخ قاطع ایران مواجه خواهد شد
🔹
هرگونه تجاوز، اقدام خصمانۀ آمریکا و اسرائیل یا مشارکت و همراهی کشورهای منطقه، با پاسخ قاطع و متناسب نیروهای مسلح مقتدر ایران مواجه خواهد شد و مسئولیت تمامی پیامدهای ناشی از چنین ماجراجویی‌هایی برعهدۀ مسببان آن خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453940" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=USNN9zyfKnxEI7dGD9CfkPIAVUsjvWXm8KBPLtKFmiVaeAPf6u-qKOdzcKRoYqQFRfd81G5yx2pLnZW9OkKh4EZH67h_YZHQuqJqO8ACssqU_KIgh_f6Nu0ZmXSKPBs5mMsJSgyHLs1vbVfKu2sORsNPdQdBwSat6W_5cWrC-cyZLYF312uHw47nJ7jlCAshRDdqscFfmTWmaOV0fv59TW93sL0vi3Tj76v3INhQ-2Z2T1D_nXSObd5efi2PZPESnpo-O4TOt47ITJ2bwUfZ64NRQ7-CzcaQz6SDcHMHLAxSgyhh8_G6NdpW2fu6Izz5NI8SWJvR_QBDrwDQNP9G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=USNN9zyfKnxEI7dGD9CfkPIAVUsjvWXm8KBPLtKFmiVaeAPf6u-qKOdzcKRoYqQFRfd81G5yx2pLnZW9OkKh4EZH67h_YZHQuqJqO8ACssqU_KIgh_f6Nu0ZmXSKPBs5mMsJSgyHLs1vbVfKu2sORsNPdQdBwSat6W_5cWrC-cyZLYF312uHw47nJ7jlCAshRDdqscFfmTWmaOV0fv59TW93sL0vi3Tj76v3INhQ-2Z2T1D_nXSObd5efi2PZPESnpo-O4TOt47ITJ2bwUfZ64NRQ7-CzcaQz6SDcHMHLAxSgyhh8_G6NdpW2fu6Izz5NI8SWJvR_QBDrwDQNP9G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامه‌‌ای که دختر شهید مدرسۀ میناب برای پدرش نوشته بود: تو همۀ چیزی هستی که من دارم
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/453938" target="_blank">📅 23:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1f0c3713.mp4?token=j9NXz9VGWtNBA5wWujJjttqqbXjhPTVaQhfGx0wV1Qu6BQKLRMC6n-uksXtg5Ttq1dy4sxBn6vde34GcMnvXoT-G07Etq-2RiMLbo_YGUVSTFUXDDraUNfCXyM9-_qi7yizdnyC1EbIr-JsIa2YUaMK3KHOgcKryOw1rokNyitqxtRiKGdcLtbT7oD-aZecY8sJfOX5TMXUySinVe_dssSlZ4W7yVwYkfxAc437lxb0OFonfoVuiAL980ToFWh6EoiK_1Aq1KKmzCTo4OyYCswrLgLBeGCQSj1zp16E2SZlOLEaBqYRPlV_hixVCZg6dvrTGfe1nVeb4UCOaDN8A0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1f0c3713.mp4?token=j9NXz9VGWtNBA5wWujJjttqqbXjhPTVaQhfGx0wV1Qu6BQKLRMC6n-uksXtg5Ttq1dy4sxBn6vde34GcMnvXoT-G07Etq-2RiMLbo_YGUVSTFUXDDraUNfCXyM9-_qi7yizdnyC1EbIr-JsIa2YUaMK3KHOgcKryOw1rokNyitqxtRiKGdcLtbT7oD-aZecY8sJfOX5TMXUySinVe_dssSlZ4W7yVwYkfxAc437lxb0OFonfoVuiAL980ToFWh6EoiK_1Aq1KKmzCTo4OyYCswrLgLBeGCQSj1zp16E2SZlOLEaBqYRPlV_hixVCZg6dvrTGfe1nVeb4UCOaDN8A0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام در تمام مشایه برافراشته شد
🔹
روی عمودهای اصلی مشایه با پرچم «یالثارات الحسین و ابناء الحسین علیه‌السلام» برافراشته شده است. پرچمی که به نیت خون‌خواهی رهبر شهید انقلاب بالا می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453937" target="_blank">📅 23:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=DHetGt7giBdxI_UyB05ZhYxFclTNsOJJ6ATk1dEoYFckfpybT0c5Mae4pjrULEAnr9_tEOH2S8VPFaPO6VXQg1iN6DRSMOkldY8fn2UiW53O2ZMeiHHtwGzqLMT5Ak5w7uHWp73dICWMQqJQ8YW28Q1KP-fxoEEfoXeDBqj7c9MH9aoeESxlHUiaKUspsEC3uVi6smQ3QmOVnUT7nH74eMsJwHXrigSrwQl5U7eP9DUl_jDG13OdVGb4FJ5ND_RZ1GyGNgL4tAhJfuSla9vEalMFVbe4KBElhTyEBM5RWisinSag_MywFRdWeY7oKCs0oA_YdIb_7ZOlW_7XQkhe5w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=DHetGt7giBdxI_UyB05ZhYxFclTNsOJJ6ATk1dEoYFckfpybT0c5Mae4pjrULEAnr9_tEOH2S8VPFaPO6VXQg1iN6DRSMOkldY8fn2UiW53O2ZMeiHHtwGzqLMT5Ak5w7uHWp73dICWMQqJQ8YW28Q1KP-fxoEEfoXeDBqj7c9MH9aoeESxlHUiaKUspsEC3uVi6smQ3QmOVnUT7nH74eMsJwHXrigSrwQl5U7eP9DUl_jDG13OdVGb4FJ5ND_RZ1GyGNgL4tAhJfuSla9vEalMFVbe4KBElhTyEBM5RWisinSag_MywFRdWeY7oKCs0oA_YdIb_7ZOlW_7XQkhe5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار هواپیمای گردشگرها در پرو
🔹
درپی سقوط هواپیمای گردشگران در جنوب پرو دست‌کم ۱۳ نفر جان خود را از دست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453936" target="_blank">📅 23:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3Q9ZLwUDpY0ARTVX_IKC9xS6s0Rzj0Ln7tAJRtx4z_pQkKgADFBOXvu2QwI_FduE68S8qccIgaz6jt6WPdGQ8c6BYn-1Q8pfMiiEqCBR9qai1zr55e7bQ3uPXaEbWXIcYMNtmfjYJMsUwb_kuTeQUntWYfxRcGkVqOoyxjm9G9XpH0LgR6OYUCtzXeNmWldIv8PQYRAG2g20mulf_yYUPQLJ1S9JpswnhhwdlzXvzabfICpeCx3wWSxQubLmNJ_phc1uF8FbSVXJw3mkqMJNGuD9HyBG9crkhYLqDGcG_AD2NgZnvpd3r6GbAEHr-89W2AVpT_E-3vmnMV7DZvSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: برای پاسخ به هر ماجراجویی آمریکا آماده‌ایم
🔹
وزیر خارجه در تماس تلفنی با فرمانده ارتش پاکستان و وزیر خارجۀ ترکیه: نسبت به هرگونه اقدام ماجراجویانه از سوی ارتش آمریکا هشدار می‌دهیم.
🔹
جمهوری اسلامی ایران برای صیانت از حاکمیت ملی، تمامیت ارضی و امنیت کشور و پاسخ قاطع به هرگونه تعرض آمادگی کامل دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/453935" target="_blank">📅 23:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e584444a0.mp4?token=HJ6GwHfwlMQv2Mut7xERABCdB18mchy9TsSEjQCLr66cpDQ5PVEDpan7TAVDfxPnEmoRTG9v0wDuR26LyVVkublSJW6-kO-CpkSbntTFOQBMKWppx5q8q9QXiggfYwhLQhsYwAzZXZdKJ3TIR-ThDgHvVwKhJmlVvjUK52rduX0Mrk0hw4G9yR8L4K2QK_Pw3n5esfHD9WcnVYfC7l_4TlhSJeClZq1X5INE--QO7NufR3z31IhAylJfqEuNXR5WDMnM-UpkzqSSCZXRWuBJYByI06hE_cfA4agjy32o8OexrKAdpdrl0tm7nB7UlzsIB9j00-DN8IwmY1IgdQzvZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e584444a0.mp4?token=HJ6GwHfwlMQv2Mut7xERABCdB18mchy9TsSEjQCLr66cpDQ5PVEDpan7TAVDfxPnEmoRTG9v0wDuR26LyVVkublSJW6-kO-CpkSbntTFOQBMKWppx5q8q9QXiggfYwhLQhsYwAzZXZdKJ3TIR-ThDgHvVwKhJmlVvjUK52rduX0Mrk0hw4G9yR8L4K2QK_Pw3n5esfHD9WcnVYfC7l_4TlhSJeClZq1X5INE--QO7NufR3z31IhAylJfqEuNXR5WDMnM-UpkzqSSCZXRWuBJYByI06hE_cfA4agjy32o8OexrKAdpdrl0tm7nB7UlzsIB9j00-DN8IwmY1IgdQzvZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: خون‌خواهی باید یک مطالبۀ همه‌جانبه علیه جبهۀ کفر باید
.
@Farsba</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453934" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267e6e4867.mp4?token=bIuctBgAf7H6nwth3UQrc6ZfNb9W8s6g1d34O9uMrwce4bOu5QTsaXeFHAzuBk9h90sLTrvlpF304Hx5CZoOjPfN1WQxu3q5MxlrVm7_im4fQmPoqp4RPgbOtiQJL2sgBKlEL8lNl0lFZKisV-ju8FoUBH7ew1foIyXr5lDDtV0lTUCoV0SdKti4EKA-6qzNpLD2q_u7OggFFNfIlUjv2M26lCe9uBWBIFBwPBiUjn6pYyNfB4vZM28b6x7YGIG2JvgRQnquTFZcAukLUDNH7mEfLaEs9HNHKhC42GBgCKXTPjMEWB-2a8kJVwjS_L0CpxKPXEbcPTf-W1ACPWwGtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267e6e4867.mp4?token=bIuctBgAf7H6nwth3UQrc6ZfNb9W8s6g1d34O9uMrwce4bOu5QTsaXeFHAzuBk9h90sLTrvlpF304Hx5CZoOjPfN1WQxu3q5MxlrVm7_im4fQmPoqp4RPgbOtiQJL2sgBKlEL8lNl0lFZKisV-ju8FoUBH7ew1foIyXr5lDDtV0lTUCoV0SdKti4EKA-6qzNpLD2q_u7OggFFNfIlUjv2M26lCe9uBWBIFBwPBiUjn6pYyNfB4vZM28b6x7YGIG2JvgRQnquTFZcAukLUDNH7mEfLaEs9HNHKhC42GBgCKXTPjMEWB-2a8kJVwjS_L0CpxKPXEbcPTf-W1ACPWwGtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هلالی، مداح مراسم محرم‌شهر: دیگر وقت استراحت نیست؛ باید برای خونخواهی رهبر شهید برخیزیم
@Fsrsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/453933" target="_blank">📅 23:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">وقوع انفجار مهیب در جنوب لبنان
🔹
منابع خبری گزارش دادند این انفجار در «شهرک کونین» رخ داده است، و هنوز علت این انفجار مشخص نیست.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453932" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113c60f2a0.mp4?token=IwXjMqVvNcs7-unEX5uzz0t8emWDgFwBN_Or8JiU4OU0l62uTjIujY835dG9CFSnu-DMsMYgkgchHAtKkSY6BkpEcQL3-fMAgi7jv7mMNFZwSsogPKeUCszUI8FYKdw5UGqoXAjADG-Z0NLux9FznuyShYfEy64sEZ8k6IPtp5BXmkwGS0LVFKp3q7UObIdGpWPmErOey4mGXGPBxCAoiiUlk1jY9SoPoAodxaP94GMgK--_97pVchFBUw1AcAQZGoPXGQtgBEDA4un8kHcFuaJqzpiXPSSzoIaysLD5U9B-E4hrg5TzoLG7Nou0jMJxxswQpBBRY54pEMkAA4IJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113c60f2a0.mp4?token=IwXjMqVvNcs7-unEX5uzz0t8emWDgFwBN_Or8JiU4OU0l62uTjIujY835dG9CFSnu-DMsMYgkgchHAtKkSY6BkpEcQL3-fMAgi7jv7mMNFZwSsogPKeUCszUI8FYKdw5UGqoXAjADG-Z0NLux9FznuyShYfEy64sEZ8k6IPtp5BXmkwGS0LVFKp3q7UObIdGpWPmErOey4mGXGPBxCAoiiUlk1jY9SoPoAodxaP94GMgK--_97pVchFBUw1AcAQZGoPXGQtgBEDA4un8kHcFuaJqzpiXPSSzoIaysLD5U9B-E4hrg5TzoLG7Nou0jMJxxswQpBBRY54pEMkAA4IJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزم ما استوار و این راه رفتنی است
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453931" target="_blank">📅 23:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
منابع عربی: مقر احزاب ضدایرانی در سلیمانیۀ عراق هدف حملۀ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453930" target="_blank">📅 23:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc184633a0.mp4?token=SB4sfH97rEbG40EFpfPuGYiqA46_MX0_meaOlAuWhfk_YtYWD-i4EVQTH3RjKZy2MYqfQoSj6m009BjpRr38TndklcdTxQ_MxbyCbsU9ukd_iQGOBbpGhjSuXn0Alvb_pS_WKNwhjW0c8d0xIAZaINTjexkIQAw7XtCwxnEdANchOKtQwAUtJbQGXlOS5lMo0JWp3K1P_LkyDA9Lva1GJunzkNi904iNie6qVq-VmCEH3Xud7e_V0-WBb0FzzjITqdRxB8C-jIqg7oycq3HAnqHUKHc3Ll_GRZgARQ4-a-FlvGjAyLTrAQpYfwPUUxLptSF6TT4iFW1pPMDJpWTom7WGxexifc3dSRPMT8u5V3mVJgpLFMvU52N6aawwcqA-ZruqSqZx4-rKkuuWFF94HxHvKkahTvUFw3UDTbNljufUO8H4BEhZlpJmbkDYHBA5NOqS_0M6g4adWYzQsEyPF4j1VZDVfwjpXaiwgvkOSZAo9wfqCJO7_PuKmtcS4TXVROZsobxC-klsEvGJQrFwwVC2T7RAZsbfT9S32EjQINmYKhfggXDKtWZ3K3MOctdc4282Hxg-8DLlNtrQCtJr7oqWvaBg8E8IHAEcHCMQ-ToaZvjUmPj3-vCqzYiIZn-kufjsQLKKRe0xaXiveILB4IpecOIS8xhq5HySKYJbkB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc184633a0.mp4?token=SB4sfH97rEbG40EFpfPuGYiqA46_MX0_meaOlAuWhfk_YtYWD-i4EVQTH3RjKZy2MYqfQoSj6m009BjpRr38TndklcdTxQ_MxbyCbsU9ukd_iQGOBbpGhjSuXn0Alvb_pS_WKNwhjW0c8d0xIAZaINTjexkIQAw7XtCwxnEdANchOKtQwAUtJbQGXlOS5lMo0JWp3K1P_LkyDA9Lva1GJunzkNi904iNie6qVq-VmCEH3Xud7e_V0-WBb0FzzjITqdRxB8C-jIqg7oycq3HAnqHUKHc3Ll_GRZgARQ4-a-FlvGjAyLTrAQpYfwPUUxLptSF6TT4iFW1pPMDJpWTom7WGxexifc3dSRPMT8u5V3mVJgpLFMvU52N6aawwcqA-ZruqSqZx4-rKkuuWFF94HxHvKkahTvUFw3UDTbNljufUO8H4BEhZlpJmbkDYHBA5NOqS_0M6g4adWYzQsEyPF4j1VZDVfwjpXaiwgvkOSZAo9wfqCJO7_PuKmtcS4TXVROZsobxC-klsEvGJQrFwwVC2T7RAZsbfT9S32EjQINmYKhfggXDKtWZ3K3MOctdc4282Hxg-8DLlNtrQCtJr7oqWvaBg8E8IHAEcHCMQ-ToaZvjUmPj3-vCqzYiIZn-kufjsQLKKRe0xaXiveILB4IpecOIS8xhq5HySKYJbkB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۵۴ مقاومت مردم تربت‌حیدریه خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453929" target="_blank">📅 23:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cff13888.mp4?token=cmbqyqa4WdhIARQCOt6UF5FTVrzRgX_53_IwTN18Cpz1VQ1aRqg6H7NGdHjV4yw3ZLxsE0nNJrkI6psgJpOCFGxRsKYHBMiZn9oGUwK0O8WKTZ0cUP77MsvlosZ5eCGUMOGLJUh8CXxddFYafBUG95FsQbFlKFxrxylCOZu-3TcReAnRhKNGI3KAhyrXnYENKPMcHRGc2TeXt_JGjJpz9IFM4-x1yVxmol5x4HvZiCee-bwh5ZiXwUEefydE78sX9VeYZ1EtWB7ybpSx3HLEO1lCYUcxL7_prdQ8X6wSwMRpIZ3w_SLIu7_Vd8mPqtGaYSBbERlQwIkmbXZTGbhhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cff13888.mp4?token=cmbqyqa4WdhIARQCOt6UF5FTVrzRgX_53_IwTN18Cpz1VQ1aRqg6H7NGdHjV4yw3ZLxsE0nNJrkI6psgJpOCFGxRsKYHBMiZn9oGUwK0O8WKTZ0cUP77MsvlosZ5eCGUMOGLJUh8CXxddFYafBUG95FsQbFlKFxrxylCOZu-3TcReAnRhKNGI3KAhyrXnYENKPMcHRGc2TeXt_JGjJpz9IFM4-x1yVxmol5x4HvZiCee-bwh5ZiXwUEefydE78sX9VeYZ1EtWB7ybpSx3HLEO1lCYUcxL7_prdQ8X6wSwMRpIZ3w_SLIu7_Vd8mPqtGaYSBbERlQwIkmbXZTGbhhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمود آن رهبر مظلوم و شهید «مثلی لایبایع مثل یزید»
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/453928" target="_blank">📅 22:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cfbb5665.mp4?token=Sn60pSIortMEGb2vQEKKjC8LrqO3c_yOG5zItUWyBpp9QnrUiGQK9nlM9PKRQNo1SV5jJzXiETaYc62yKRC08TA-k9cNnGNqnNy_5uz1VI5BS4wyw9XVMq0MbaXZUfMg1CWGXwHzWTjJXtjn_MlU1s7X442WC9AzmsrjBsdJ-ihFH-jMBeeX1tXYPQ2ILKiuQSCYBfWOwv4854TyZjx5H9J-CfOt6ripTfGx105KwkfSsRaUeATFktWZqePHEou4IkR2u337kDd-XVA8vWv9I48lMgwEZVC3441DBQaICynWuz4LwF6BuG43C__mub0opeVUZGZhglGQ6_5ZVLBLTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cfbb5665.mp4?token=Sn60pSIortMEGb2vQEKKjC8LrqO3c_yOG5zItUWyBpp9QnrUiGQK9nlM9PKRQNo1SV5jJzXiETaYc62yKRC08TA-k9cNnGNqnNy_5uz1VI5BS4wyw9XVMq0MbaXZUfMg1CWGXwHzWTjJXtjn_MlU1s7X442WC9AzmsrjBsdJ-ihFH-jMBeeX1tXYPQ2ILKiuQSCYBfWOwv4854TyZjx5H9J-CfOt6ripTfGx105KwkfSsRaUeATFktWZqePHEou4IkR2u337kDd-XVA8vWv9I48lMgwEZVC3441DBQaICynWuz4LwF6BuG43C__mub0opeVUZGZhglGQ6_5ZVLBLTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید سردار قاسم رضایی جانشین فرمانده فراجا از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453927" target="_blank">📅 22:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=dILK6PDxJP_JiWUqWp4eP6Uqs6wjluKFIeLofeMdWGzA310ft3Cf5aMpfX0BegAN8uSWPEyqRP_q3SEQrGw_OXQUtThAv4JMkNFEcQnUEhskJsPlbtp29j_wwSKkZ5pRwUfHX_49NEkcw_bQo4lbG-db01WL1mvpKwQr1d6kj9pfif42X_sg8MXOoNDKty5GN5JxiS_OMkfXx1v3peg96vBdIdcuZD8CGtj8SYtiq97Xx6daJjcq4XEW8aY0jhl5XrlVXkqujEYH2x7U16tpoiapcHkzShFyj9rSqVzH9hrnF6pAV04CXJ9fx7ZriYVJnCNPS4H0ZgF2geEY9Bt7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=dILK6PDxJP_JiWUqWp4eP6Uqs6wjluKFIeLofeMdWGzA310ft3Cf5aMpfX0BegAN8uSWPEyqRP_q3SEQrGw_OXQUtThAv4JMkNFEcQnUEhskJsPlbtp29j_wwSKkZ5pRwUfHX_49NEkcw_bQo4lbG-db01WL1mvpKwQr1d6kj9pfif42X_sg8MXOoNDKty5GN5JxiS_OMkfXx1v3peg96vBdIdcuZD8CGtj8SYtiq97Xx6daJjcq4XEW8aY0jhl5XrlVXkqujEYH2x7U16tpoiapcHkzShFyj9rSqVzH9hrnF6pAV04CXJ9fx7ZriYVJnCNPS4H0ZgF2geEY9Bt7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «مرگ بر آمریکا» در مسیر کربلا هم از زبان مردم نمی‌افتد
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453926" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
وزارت خارجه: دولت‌های منطقه وظیفۀ قانونی، دینی و اخلاقی دارند که از استفاده آمریکا و رژیم صهیونیستی از قلمرو و امکانات خود برای حمله به ایران جلوگیری کنند. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453925" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453924" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453923" target="_blank">📅 22:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a618481cd.mp4?token=TQBj1-t5CWAfEYs_HJGTq7gv_OTpYMoGukVq83PLsF9gYWQ24tTpmMOTTMO2gqu3CJ6olo2NYQ1IluOhYq5CPYw18bud9BUQ8JkvqGgHKALgWALn1_BtG-IfdJF7D21mcYknrDVcZ8pGh6zlFv6PvG683eah9mSoEsdLrLfcezxdbMU7bwn_ec4-k1ldbf0FaYqnutCoHtraBy81KITtuRe9U32GnhL_58zAedOq8tjTVSB9qNqp60M15EfOyl1jBQ_TkOmRVsOT9DpQSJQyVkJZFQacIddhPpEVocx8wP-f95uDHuUj8OCNjAGbLpB3GvOCQYBAZRdgsSlcls0lCh7UTxZrlWkqbNOjNt051d-GXH06iBGDO-xSeQOow8xPJmK2nav_GevW5MWkICJ7XIxe-PGTq4CKxvvya2SkSDOsrCwZq66hpGGuiGpJgrZjckfZYQry3qjkWWnFRMQRp58mFQrpQVCo0uy9TeqoPAoKcjFvTiMsTZA2N24tGO2cCVYfFnU5eedMppH6ZqBQHX122zlY3HiH0jf4ZUg7X_Yvdx8ET11sBTfWzmIk-FUnu9l8YADdyYq15BKEixij7KUuuIRzFNd3AJTNiaMJaOEddNV3gmmFoWCnDlKA2Ry2tDxSMI9uTP3Edu8_xmHnTqhxNRpvCOTwMBeafUvBDKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a618481cd.mp4?token=TQBj1-t5CWAfEYs_HJGTq7gv_OTpYMoGukVq83PLsF9gYWQ24tTpmMOTTMO2gqu3CJ6olo2NYQ1IluOhYq5CPYw18bud9BUQ8JkvqGgHKALgWALn1_BtG-IfdJF7D21mcYknrDVcZ8pGh6zlFv6PvG683eah9mSoEsdLrLfcezxdbMU7bwn_ec4-k1ldbf0FaYqnutCoHtraBy81KITtuRe9U32GnhL_58zAedOq8tjTVSB9qNqp60M15EfOyl1jBQ_TkOmRVsOT9DpQSJQyVkJZFQacIddhPpEVocx8wP-f95uDHuUj8OCNjAGbLpB3GvOCQYBAZRdgsSlcls0lCh7UTxZrlWkqbNOjNt051d-GXH06iBGDO-xSeQOow8xPJmK2nav_GevW5MWkICJ7XIxe-PGTq4CKxvvya2SkSDOsrCwZq66hpGGuiGpJgrZjckfZYQry3qjkWWnFRMQRp58mFQrpQVCo0uy9TeqoPAoKcjFvTiMsTZA2N24tGO2cCVYfFnU5eedMppH6ZqBQHX122zlY3HiH0jf4ZUg7X_Yvdx8ET11sBTfWzmIk-FUnu9l8YADdyYq15BKEixij7KUuuIRzFNd3AJTNiaMJaOEddNV3gmmFoWCnDlKA2Ry2tDxSMI9uTP3Edu8_xmHnTqhxNRpvCOTwMBeafUvBDKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وفاداری گنابادی‌ها به شب ۱۵۴ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453922" target="_blank">📅 22:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453920">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAO2ynybnv2UgWwssQtQorttWV2ecoAarbXSJrNPYX9-pFcdNGSiSNDxqnG639hloPrBTg8-d98VRhgFEhG9CX7LgODFnhV8kYQ1GmW7fxY0SAUuLi7rDFNsrWAGoJclNNgH7vheccKjHQkjkPHBqwzqAXINaPexriUjoEcXJ2dM1BKXIeETJ8fwgGRq4RzVXZHu5R2vhClhOXCIfQ5thx6OI6o0N0P7lueFtytOxmEpZIn_o4QT3_AZIOqri6aQwJctJMCCvTM8C8AGVBCD0Zc4IcQi5WJWPWpEDOAYfoOl-vJpVdUPB9eC8u9yDB9Zy6TK2Eg5KBqNOyewulCyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا مجلس نباید لایحۀ رژیم حقوقی دریای خزر را تصویب کند؟
🔹
صفرنژاد، کارشناس مسائل بین‌الملل با انتقاد از ارسال مجدد لایحۀ «کنوانسیون رژیم حقوقی دریای خزر» به مجلس، گفت:  تصویب این لایحه در شرایط فعلی می‌تواند پیامدهای حقوقی، امنیتی و ژئوپلیتیکی برای ایران به همراه داشته باشد.
🔹
پیش از تصویب کنوانسیون، باید ۴ موافقت‌نامه در موضوع تقسیم بستر و زیربستر میان کشورهای ساحلی تعیین تکلیف شود تا منافع ایران به‌صورت شفاف در اسناد حقوقی ثبت شود.
🔹
تصویب کنوانسیون پیش از نهایی شدن اسناد تکمیلی، می‌تواند در آینده مستمسک حقوقی برای سایر کشورهای ساحلی ایجاد کند و بر روندهای امنیتی و ژئوپلیتیکی منطقه خزر تأثیر بگذارد.
🔹
نمایندگان مجلس باید با دقت حقوقی به این موضوع ورود کنند و در صورت لزوم، لایحه را برای رفع ابهامات و تکمیل اسناد پیوست به دولت بازگردانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453920" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453919">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4049471be.mp4?token=rEntAWwrAd_32dnyDG2bwGT7pHLAakLmNMbFyNYb7Ve87JXB02xbuPsnRKpR5dUMRxw1thMOMJyOsY1L2TxwillQrwMCWIeeB8IsEAwihTkEg8jhJoYv0CjJKFR5M_VznURtjsRbQR6YqVMEFUe33PtF3HNOj_Rbd3Htl2bGtlTYZEKrh1kkN1iVyPSELhOiXLsbEvvfc18mt_1S-kxFLJHfi_FN5cFu4MnJxA7T5QAjVgdqKChWhPtdB_aBsWXcYNmYE9y2eOiE30GpHc-0mFQLilIPBK2kAhahcK0ZPiL5gR7M2DeRFYIRHcR4ZMnOVxCQwQOE0zJLQJAIMIJSDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4049471be.mp4?token=rEntAWwrAd_32dnyDG2bwGT7pHLAakLmNMbFyNYb7Ve87JXB02xbuPsnRKpR5dUMRxw1thMOMJyOsY1L2TxwillQrwMCWIeeB8IsEAwihTkEg8jhJoYv0CjJKFR5M_VznURtjsRbQR6YqVMEFUe33PtF3HNOj_Rbd3Htl2bGtlTYZEKrh1kkN1iVyPSELhOiXLsbEvvfc18mt_1S-kxFLJHfi_FN5cFu4MnJxA7T5QAjVgdqKChWhPtdB_aBsWXcYNmYE9y2eOiE30GpHc-0mFQLilIPBK2kAhahcK0ZPiL5gR7M2DeRFYIRHcR4ZMnOVxCQwQOE0zJLQJAIMIJSDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابرپرچم‌های سرخ انتقام روی دست زائران کربلا
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453919" target="_blank">📅 22:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=qeCS4LTqg-QDw1t3SHg0guNNgAYEBqjkTblgZQcvVfd14XFhaaT91iRZ6Wk3vdm1UxfGsbq0FnR4A8jVgZfSMMF1lvxK3_YjdKhREvu5aWSg-Mek1KfrYoNh-3A9g1YLs2LM6ps5BrBseD1tMELCFZVtyeL8X1k6NfmRkn3dQlwOV2RLb8yBQ7NNnAQ-AaBIFaOcI9Qh1J2zmbNiX9j-LMhyual66GPjAvpwPCRiND8ZFKQvTxIlNdCwKyJbQdTB3sq2lXWWKGTNLkSDha3lKprB2fnW-e64-1n6LGSuMDTwC8-Hg6dJzn5rqWZF90YOrkz9WlCmTZH_7poxcP64QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=qeCS4LTqg-QDw1t3SHg0guNNgAYEBqjkTblgZQcvVfd14XFhaaT91iRZ6Wk3vdm1UxfGsbq0FnR4A8jVgZfSMMF1lvxK3_YjdKhREvu5aWSg-Mek1KfrYoNh-3A9g1YLs2LM6ps5BrBseD1tMELCFZVtyeL8X1k6NfmRkn3dQlwOV2RLb8yBQ7NNnAQ-AaBIFaOcI9Qh1J2zmbNiX9j-LMhyual66GPjAvpwPCRiND8ZFKQvTxIlNdCwKyJbQdTB3sq2lXWWKGTNLkSDha3lKprB2fnW-e64-1n6LGSuMDTwC8-Hg6dJzn5rqWZF90YOrkz9WlCmTZH_7poxcP64QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453917" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d264eaaf.mp4?token=ZqT6iGEqCRUfktDv1CbAbpoMFnkDJJ4Vv-M-43Xz2WHlO6pTQs8CR2nC6fc5oQefAjeOQ3AfSzjGqsgGYLlKOwYBxUI4Fhyg9VVB8quiFmUg3DiLuOnPHnLesjUDh6T75Xy5NvVuIGzUEItlU3a7GtCLmeVm4CzWyRMteXPYcwglAN7R5lG9WdIgrWahCKavvXd8usVg0TR02lDHqOHgjNwFFH4-U_X2g5UOPOSkMYgBvM6PJpwduZzxzOa9txD7bJ1TBndJrhx-K4bPtz87cmSGPQ6bbDeNKl1X9-p3lA8Dz8RO6SzuI6BLG1VoTQ3bwVw_XgGf5dYf6AAnqpg33g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d264eaaf.mp4?token=ZqT6iGEqCRUfktDv1CbAbpoMFnkDJJ4Vv-M-43Xz2WHlO6pTQs8CR2nC6fc5oQefAjeOQ3AfSzjGqsgGYLlKOwYBxUI4Fhyg9VVB8quiFmUg3DiLuOnPHnLesjUDh6T75Xy5NvVuIGzUEItlU3a7GtCLmeVm4CzWyRMteXPYcwglAN7R5lG9WdIgrWahCKavvXd8usVg0TR02lDHqOHgjNwFFH4-U_X2g5UOPOSkMYgBvM6PJpwduZzxzOa9txD7bJ1TBndJrhx-K4bPtz87cmSGPQ6bbDeNKl1X9-p3lA8Dz8RO6SzuI6BLG1VoTQ3bwVw_XgGf5dYf6AAnqpg33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام روی پیشانی مشایه اربعین
🔹
هیئت‌های مختلف از جمله هیئت سید مجید بنی‌فاطمه و محمدحسین پویانفر با پرچم سرخ انتقام رهبر شهید در مراسم اربعین حسینی حضور پیدا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453915" target="_blank">📅 22:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2691e9f69.mp4?token=HA63jaIk8qtB6Ro6IcpAvm8iwapsykm8RpSjnhUn2l955puwgXxbAqqfhsfpPk2hBzpXQYf3QFNiVW9qNRUIQeil7Kt6ZeQNsjCzhh1VjJ7UwGgtHWVHTCXd5OIDj4lOh6VBTeRqZpXWBR35HKFNHw685VjA4h40wvYXuCrQ4PeQs-aJikDxA8cwzjdNsli4fB7zMDoae0u2icRUpA0evnvkoJgsSF_QzmQyZkA98Ksv_rBiAH03MGBjUoh864tPz87gaJfclmac5mV6tC28TBnacQ4WDOKSQ9L6wCC8H_xQz4eoUuIw8qfYaiqntx8Z3JIkG3ijDGWM0t_8yQ5Asg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2691e9f69.mp4?token=HA63jaIk8qtB6Ro6IcpAvm8iwapsykm8RpSjnhUn2l955puwgXxbAqqfhsfpPk2hBzpXQYf3QFNiVW9qNRUIQeil7Kt6ZeQNsjCzhh1VjJ7UwGgtHWVHTCXd5OIDj4lOh6VBTeRqZpXWBR35HKFNHw685VjA4h40wvYXuCrQ4PeQs-aJikDxA8cwzjdNsli4fB7zMDoae0u2icRUpA0evnvkoJgsSF_QzmQyZkA98Ksv_rBiAH03MGBjUoh864tPz87gaJfclmac5mV6tC28TBnacQ4WDOKSQ9L6wCC8H_xQz4eoUuIw8qfYaiqntx8Z3JIkG3ijDGWM0t_8yQ5Asg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در مسکو ۳ کشته برجا گذاشت
🔹
خبرگزاری تاس روسیه: درپی انفجاری در نزدیکی یک کافه در مسکو، ۳ نفر کشته و ۱۵ فرد مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453914" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG2PlUB9X-MVRC8zE0Ybd0JgJbc0c8q3JKoGZ79ksFSNvx8eEHcP3Vg9SUYKWX9SRYn5KHa7-jMXrifAymSIpphamodUvPgFgx_amzwhch8nwgzUcZkdMxT4ALtr2MeO1VRTsn7oVORdy_usbaRMPO461Se89YF37s9H87hdrJu5ke8b_TRqgaaVX5cukYiMl07fw6ky1sjVsiyrBo5zl5sZV6wUnBKCJuqEhe6eDWmEgm7RFzD9WWTE0cfQewtSyHprpOLuU0hHgizXZyWaY_6ooPgGgwsO2yVWzh8qYxQV8QfEVIEejux7NBpjRshCR3N2dN1vb_DNf3jfiHLHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوچک‌زاده: با لایحۀ جدید مجلس، مجازات نتانیاهو و ترامپ حبس و جزای نقدی می‌شود!
🔹
در لایحۀ جدیدی که با عنوان «لایحه جنایات بین‌المللی» در مجلس تدوین شده، به قوانین مجازات اسلامی ازجمله حکم قصاص دربارۀ جنایتکاران بی‌توجهی شده است.
🔹
تصویب این لایحه بدون اصلاحات اساسی هیچ کمکی به ما در جهت رسیدگی به جنایات رژیم صهیونیستی و آمریکا نمی‌کند.
🔹
حداکثر مجازات پیش‌بینی شده برای اشخاصی مثل نتانیاهو و ترامپ بر اساس مفاد بند اول مواد مختلف ۳، ۴ و ۵ حبس و جزای نقدی خواهد بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453913" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e869dead1.mp4?token=iDtBAlAg6O-mpI5d9TrVKfLUZ3TaaZk5kUkV0EsgcA6bM3w9Ivypc8rho68Kp6QrQPB2YX1Xt2wtvSNP0hRSJN0tHLrUQrPLpYaV0YmEJaa16RJMgrteU01BiDLju8efX2YwAVogeOQx6E_hEaly0KAmquTJUKtWH7FUOTy6ZacxqaM-Igw7DKcwaf0n60cnivv5hF2ohuKnKMUo7AECdqGWYq_gcAB82Gk0O40ef6COHWI1kvpJ6NzFy4uT1xaNDjnIgv8wCHU-WqpK0KUKTOzcuwfUTCKCxhJnYKwXqBnzvQKTcHYqZ24m30uaILUdbJTvf8yEfTLvci6m4ZUNVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e869dead1.mp4?token=iDtBAlAg6O-mpI5d9TrVKfLUZ3TaaZk5kUkV0EsgcA6bM3w9Ivypc8rho68Kp6QrQPB2YX1Xt2wtvSNP0hRSJN0tHLrUQrPLpYaV0YmEJaa16RJMgrteU01BiDLju8efX2YwAVogeOQx6E_hEaly0KAmquTJUKtWH7FUOTy6ZacxqaM-Igw7DKcwaf0n60cnivv5hF2ohuKnKMUo7AECdqGWYq_gcAB82Gk0O40ef6COHWI1kvpJ6NzFy4uT1xaNDjnIgv8wCHU-WqpK0KUKTOzcuwfUTCKCxhJnYKwXqBnzvQKTcHYqZ24m30uaILUdbJTvf8yEfTLvci6m4ZUNVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداح «باید برخاست» پرچم خون‌خواهی را در مسیر مشایه برافراشت
🔹
پرچم خون‌خواهی رهبر شهید انقلاب در موکب مکتب شهید حاج قاسم سلیمانی در عمود ۵۳۳ طریق نجف به کربلا، ۲۴ ساعته توسط مردم برافراشته‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453912" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrNkxJciwg_ZSz44IdOMqzAchfZpwzkAodK501oIff5FYctKSsZzPHqyEmwT95aJEKlrHPZGtjLwKFOdrSmvs2g7URfWXLwlhIipHsQNN1vJmhyAXtsE8WGxljxj3kV1Sywsl7e16F9a17JH8MezuGMGyftnrmDOqb0Tv5sVBGCJMTCc-tkiYkNDP_09hf0VQSVB5DJfACWTJrgg7aVYf6R-6Lt9MhJ6o7CRsdHA6ICxOW2Bcmh22RHf3Dc2xkAdT_mhA0K6ZjSPYOoUNxPMhcuJ2cdXVBw2eBiEK6WO2tmG6WnIe_g3d3bexhou4JWdVNB1T-RP3ZbH2_iyXrN8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDfMeaNAJMS7iU0R9LgyBW_FUfp23WGSgoEo27KNqOiaqjjVnLjokeYzyl7wu750rC3jShZk1AgUlDDIkWS4yNHMip2WhtLo32pGArqN3B0jwg6_y1-PgEKNkPBVqoK-d-yxtGrZZJE2tDu1Wh_F14K2_YYcusttWPQHgiayss6GHjK9zyR5qqhzNZLG-kSsawxXEbDYz7Wo2hE0wGjeioxJRVSwqAEkNC7do8P1Phb3QPlkfnu0jmVhkg2lf0LbsZkxRgHpXahydVHQLREZYZGBvANnSfT8CBCYj20CoFQHytUPcbUIl1prHZEf0qOLlRiBDALIqHkc5eCh0v6zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAI233H2mSZf8sCZgKMSQXqyBMYIBvfYANmpNTQNHU5PmyV3jy5DLk70UX-TM4PZPUhk2arzpkdpg_0ndYYsKUKyebjOSH5556P7sFdugkTMb5JGPDwAsPMA2BfNrTuBIs-MhKulHeGYq4tlIqB6BT_ZXWYyskpxo4UNvPOh0Nd65Emg43GslN2ubhT8eiGv21fhIITsxM5w9UBf2FVkTHKQiIR9530XoWzbxGFszTGNzHP3Fv-CY10XQJtJKFA8Y-l67MI3jgwKAhQIKr0zbHRb7sJhfLcHa9knAui5LIkYyjEZV-nL7DYmSnrt-voUax4Kk0_gm2hrEdQG7PAZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU6nbyJze96Bw2whqwFoflSGX9wlSQVtNGGPmjVL0dhIOXsQF05_07Yu-PCIqdXlENw_fVczDyFEjKIXOLi6KhTaGZP0uaig3vnnq1OIU4rgy5WFe8TPpjGl7xGgdMzGdNFmRuSdf2YjJ1o1yrPizYsYSBYChuLjNla1SVlveZoe565HTKjXCxKmq0YteSlga-GouGwvnCEqz1H8OaJ76fluJtoNFlfp-nmdn3O1TChkdfRWlveH9ge_59RaEg8idVPh8ype-DyYyy9xnDV0NPddNKhtbbDZ-syticp71y4h5RWU9fMWH0E0o6Ar2b0iWnwRQ5jPVBqnc4gqrreM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lryFK70gRVTNb0bjCgPMDUBy3EzZnpvY2CMWeOwO1cLJsbYumjuYiax2HPyi_VNHyo7TWR2Im7orJWxMCV1BusHsxz4IVVjsNJF-Fjudqu-Ds3mhO0rEahQP6-7N_t9D1qovCJkotixV_UecuJeqiQG9UsFtvgeiBCDNF3qr_uyMhS573T1iIOYycmoH5M2W1LJpEVUaLclDZKvwMHwPL4-ijrVVO4kZb4YnsvSKQ8-y4Yy7PP2SVaL47f59ik_qXb-skeMOD4mXaOBACQKeR3yK0R_Faoo5SssEVSdNBcEcuEyAQODMv2OOz1Flwe3mjfybgQJFNbKtfzys5oBbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8KxHObi_JMzHcUrliwlpo7NRKt4H10mmxKHeKCZVMVTjgW1Bi9I3R6Ka7su0ycWvNeP3xxjNdhfKuQnTUhiJ3Sf6SAaTO1gi7ct64vEfZ-SBwY92-RKzXUzF2Sxc0A1cMItM2l2t2wwtVfyZ_TKnlRRW1YeYeWSP5PVVi3ETQy27MJrSxPkbRRsnZvN4TxxiFNgm70Jr5ZZv48xPOSn0RcL1jknnmyVQdjKZ4fziKxrhBqlOQLe3VgVP52TWiyYTDPfIOgO-3RRZuwsuBahZg-DrBsv41g3Kv2wIydqQ9dNkNTS_qtVKfk5XiweZe6O1sEKQpL8V4wTGbrIgXEd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAGWA6pxNDP7r0kn0NDmAyQYmUYQmSHDBYyDvupO9xjZVPSoMTYEHYqT-eXRDHuxecIXYnjTOP3CMq9FdJfRwf9HG4enzbbSDvEnY050yM889srIF7URXAmh_465B_6ER9oADhAVQMgNnxJhRX0lQIkODXIyDK8PPFA5bp1blKN8OZdJW2jAvMx584pDfSz7IIjMIVgfZRpc113yQIjKGO-SgoIxO99VkMltwORWXTcROixSVSqbZzyVhD4QEaRBajgC8A7bhKSNM585_R8-UHI9LU6YoOP6RfUhfuEUheaXBCaIix5PddRHJUYlyqwLZbp12ph1kTUfQ4uiyrUuWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نائب‌الزیارۀ رهبر شهید
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453904" target="_blank">📅 21:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/farsna/453903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
با چشمای پرخون با
ا
ین قلب پاره، رسیدم به خاک عزیزت دوباره
🔹
قطعۀ جدید محسن چاوشی به مناسبت اربعین حسینی.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453903" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd77f123d.mp4?token=q9Ebuc8XX3yni4U9WAeAV74XtyaVcAv7AousKy9of_NlV64LvE2w4-Ztc5ion4gK326hNc5iLqia3W2JrqQuNE_pU74RvzZz0Suuwu8BcgP4ARir4lMAWz8oFanJEZCTJXr-iwWoKYPSOKRncU4Q8hjQpj--1-xrvf9cfOY09Vr30NJ8XNJnQ8xbtcMJHeO1VErShj4zrzNVs0rTKa94HuxnL-w6JgqVqjuzz7owGmfxuRJGWt_UIgrrXBFIx-QbVi-7JIZTecweBjT1_0KXWOAk0h0GREgalM7Cg6-q-qKgW_0K1jHl9_OU7Fxc-TDTsXnhNpiffMx0ZaPur5pdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd77f123d.mp4?token=q9Ebuc8XX3yni4U9WAeAV74XtyaVcAv7AousKy9of_NlV64LvE2w4-Ztc5ion4gK326hNc5iLqia3W2JrqQuNE_pU74RvzZz0Suuwu8BcgP4ARir4lMAWz8oFanJEZCTJXr-iwWoKYPSOKRncU4Q8hjQpj--1-xrvf9cfOY09Vr30NJ8XNJnQ8xbtcMJHeO1VErShj4zrzNVs0rTKa94HuxnL-w6JgqVqjuzz7owGmfxuRJGWt_UIgrrXBFIx-QbVi-7JIZTecweBjT1_0KXWOAk0h0GREgalM7Cg6-q-qKgW_0K1jHl9_OU7Fxc-TDTsXnhNpiffMx0ZaPur5pdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاموشی‌ در استان‌های جنوبی کم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453902" target="_blank">📅 21:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2057c351b.mp4?token=NuOnIfZXxZ1hcEHPnD5vf0gHmEs_vdCvC3tQlmj6n_uLctLslTTWG82Kp-TQjVuVxaEb3CvRq5B7SKIteT8sRv4a1ZRc-hIu9jAS44Sat8_vvmHk0jsHAkkDqq_EDdi-ueZVptuDDUej7syTqkWNlxA277M5_lcmFJUYJkRHDLDSXkLUZk1gMHCJBrbKyb-aYgc6LIPBq_zbUa4ExFUjBMb7RSa4c07XWi7VvW9kA51o55Yr_9oylsxn7ZSXm-1HHAbtUoBFLOZLIKj8iTXIM_M8gsS6L0hGAjQZNGLkjWHPe3cmHdPw3_4hT49A3T5KdixOmkeYQZR54zHrxZvClw85IvA37gNeQWPe7GMoSZliLFWDpYQiiB69C2IBmv6Xrdue_rmrZEE7grALdBymwxAVIlJTPGwgCQqkm6ZGSc5vJr700OcZG3RGnitUYXrNMjGN2pHYLqMXw35ERHR40T8q20clU7HIeGQwPr6gV63gEhmDSHSmeBXmzbN6LQFR0WLW-rup-VTFHzNMbY1_LkHEYzEqwvX8wHJCojcm40QjJei8KI3W6cGL3WNzrJ4MeEKEYwLX6cfidfCagSEW0eq_QjCnn4J8B3TV6i_4CdMNtu50xtepoFu-jNxQ719AuzDZGoM9ey5yHo--vubHUv3k2EvKUp3P5xG3bej1w2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2057c351b.mp4?token=NuOnIfZXxZ1hcEHPnD5vf0gHmEs_vdCvC3tQlmj6n_uLctLslTTWG82Kp-TQjVuVxaEb3CvRq5B7SKIteT8sRv4a1ZRc-hIu9jAS44Sat8_vvmHk0jsHAkkDqq_EDdi-ueZVptuDDUej7syTqkWNlxA277M5_lcmFJUYJkRHDLDSXkLUZk1gMHCJBrbKyb-aYgc6LIPBq_zbUa4ExFUjBMb7RSa4c07XWi7VvW9kA51o55Yr_9oylsxn7ZSXm-1HHAbtUoBFLOZLIKj8iTXIM_M8gsS6L0hGAjQZNGLkjWHPe3cmHdPw3_4hT49A3T5KdixOmkeYQZR54zHrxZvClw85IvA37gNeQWPe7GMoSZliLFWDpYQiiB69C2IBmv6Xrdue_rmrZEE7grALdBymwxAVIlJTPGwgCQqkm6ZGSc5vJr700OcZG3RGnitUYXrNMjGN2pHYLqMXw35ERHR40T8q20clU7HIeGQwPr6gV63gEhmDSHSmeBXmzbN6LQFR0WLW-rup-VTFHzNMbY1_LkHEYzEqwvX8wHJCojcm40QjJei8KI3W6cGL3WNzrJ4MeEKEYwLX6cfidfCagSEW0eq_QjCnn4J8B3TV6i_4CdMNtu50xtepoFu-jNxQ719AuzDZGoM9ey5yHo--vubHUv3k2EvKUp3P5xG3bej1w2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ام‌کیو۹ دیگر تولید نخواهد شد!
🔹
آسمان ایران، گورستان پهپاد ۳۴  میلیون دلاری آمریکا.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453901" target="_blank">📅 21:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b760780f56.mp4?token=byh8RH9nGt-2tssu9k59ORTIHc2Ia_WFTkkzAZi8cx8TseupGn3BcbPwE_jW2B1Jz2_zee2TRX6CDldyDyIh0e2GFUIg882B5xHStmuUnn7K0HrpWrJMQv3kfimCcQ_MkyoQVxCACzzenxKhBVc1oCAOG8iRnm_epCIHAPeHIsprvifnfIwlmyypXpTeIitHrisb_LRleNG16PAWa8kucJ36sYB0mEkQMzIDNIPjysT2TD5CDq0Pg6yym_67-Uf-mb_knkLRj5X2JiJGcSkjnDkyGJkK_7J_xkahgp9EjZHv2f29a2JY1mhJFMiSgWkykgUfSm6mdVG9hlOz7SMMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b760780f56.mp4?token=byh8RH9nGt-2tssu9k59ORTIHc2Ia_WFTkkzAZi8cx8TseupGn3BcbPwE_jW2B1Jz2_zee2TRX6CDldyDyIh0e2GFUIg882B5xHStmuUnn7K0HrpWrJMQv3kfimCcQ_MkyoQVxCACzzenxKhBVc1oCAOG8iRnm_epCIHAPeHIsprvifnfIwlmyypXpTeIitHrisb_LRleNG16PAWa8kucJ36sYB0mEkQMzIDNIPjysT2TD5CDq0Pg6yym_67-Uf-mb_knkLRj5X2JiJGcSkjnDkyGJkK_7J_xkahgp9EjZHv2f29a2JY1mhJFMiSgWkykgUfSm6mdVG9hlOz7SMMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری زائران اربعین در حرم حضرت عباس
(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453900" target="_blank">📅 21:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312d74af7.mp4?token=sfMkAOFHglas-XNsw3UpImNrbCt0GsAYEdw9SxCT2uiora0lR7RVKsc1aDy9Y-uX1GDxCrF3gBgN80Ux-N-xf_QdNd1w7AwtnQziVks78xat6EYp_PYprDi9soe4H22h7k_dpIqFMpbWYeInOZWYs3lzRuSIgSsonLBPfnISiTN5qYTcaVvUQtKkzlrj5weIIuWG5ZPr8XK22ickMpqWjh205wSnNL_3npJQn62svrHwQznVkRVc4ZKp-t0EV2Do5pA4bhuCt0_8Gj-k2ufeyR1Asotxm7QJh-6tbr1AMrgCaAvW572dg_en45A_p_J100JmHazbHGUZv2XjFd5cs7DbBqN1cGumubTLoVC1VpIC8K0uDXHXyxga2j0LXzBhR8gVRFzAw58dF1YT3AYPB-3uy-9I3LXrPAXHmO0_uY1g236362iTOEvRSlK7MHYkKhCxpUNBCx9t-UNWDSbHb8eOSIF5WIUZBWEmeRciJ_CmJ2O15qf-KZ3-MF-i96lDRb1-BJOmZkpxGgUvvRLEE5OW0OBqLpttQeGHgpgFYgvptPsRSWHLtQ-H7hVGg57QoRWrOy99wL67qO6KJ1xskA8GsAPSCck10AmVXhTEx9KfgUbOfobFRxcXJzmhsyrAi8PC08qyznBlLohpM-AwftYRR46orB85QainkQBJKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312d74af7.mp4?token=sfMkAOFHglas-XNsw3UpImNrbCt0GsAYEdw9SxCT2uiora0lR7RVKsc1aDy9Y-uX1GDxCrF3gBgN80Ux-N-xf_QdNd1w7AwtnQziVks78xat6EYp_PYprDi9soe4H22h7k_dpIqFMpbWYeInOZWYs3lzRuSIgSsonLBPfnISiTN5qYTcaVvUQtKkzlrj5weIIuWG5ZPr8XK22ickMpqWjh205wSnNL_3npJQn62svrHwQznVkRVc4ZKp-t0EV2Do5pA4bhuCt0_8Gj-k2ufeyR1Asotxm7QJh-6tbr1AMrgCaAvW572dg_en45A_p_J100JmHazbHGUZv2XjFd5cs7DbBqN1cGumubTLoVC1VpIC8K0uDXHXyxga2j0LXzBhR8gVRFzAw58dF1YT3AYPB-3uy-9I3LXrPAXHmO0_uY1g236362iTOEvRSlK7MHYkKhCxpUNBCx9t-UNWDSbHb8eOSIF5WIUZBWEmeRciJ_CmJ2O15qf-KZ3-MF-i96lDRb1-BJOmZkpxGgUvvRLEE5OW0OBqLpttQeGHgpgFYgvptPsRSWHLtQ-H7hVGg57QoRWrOy99wL67qO6KJ1xskA8GsAPSCck10AmVXhTEx9KfgUbOfobFRxcXJzmhsyrAi8PC08qyznBlLohpM-AwftYRR46orB85QainkQBJKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران این‌گونه تجمعات انقلابی خود را با طریق‌الحسین پیوند زدند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453899" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfba2ec58.mp4?token=acSiFMRz_2Ow4jmTkpEOsK7cpb699uF-A7wn4gnXb_KnV9uPIGHYYBbiz0eXNouxDPctmFVwJLGz3CDuKfohaP5d3rpxLmo-CjmPlutKrTCXwjOToz0C59wXcFpUEmW6YJJxbha6qeKrTCX8i0zSFjkY1LqtXeQXaVfdKBFuBwK-r5YXmncJYzEg5oZRMhdhtU1tRzju7VYUgvoE4GnWAHlw-jcLekSZj43lfXsNHs04cZPvVLgLsqxjeQ5LV6Ckm2vb5kkaCKsTxtWWSokh7fA69un4_VIzAPddXm2BauqAX1b-jqxrYVJcOzqrQP6_jTfs30O5eArUsXWBeBfnYk1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfba2ec58.mp4?token=acSiFMRz_2Ow4jmTkpEOsK7cpb699uF-A7wn4gnXb_KnV9uPIGHYYBbiz0eXNouxDPctmFVwJLGz3CDuKfohaP5d3rpxLmo-CjmPlutKrTCXwjOToz0C59wXcFpUEmW6YJJxbha6qeKrTCX8i0zSFjkY1LqtXeQXaVfdKBFuBwK-r5YXmncJYzEg5oZRMhdhtU1tRzju7VYUgvoE4GnWAHlw-jcLekSZj43lfXsNHs04cZPvVLgLsqxjeQ5LV6Ckm2vb5kkaCKsTxtWWSokh7fA69un4_VIzAPddXm2BauqAX1b-jqxrYVJcOzqrQP6_jTfs30O5eArUsXWBeBfnYk1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ استاندار ایلام به چرایی ازدحام در مرز مهران
🔹
با هماهنگی وزارت کشور تا صبح فردا ۱۵۰ اتوبوس و ۱۰۰ دستگاه وَن اضافه می‌شود.
🔹
از بامداد تا ساعت ۱۸ امروز، ۸۵۰ دستگاه اتوبوس در حوزه مسافرگیری و جابه‌جایی فعال بوده و مجموعاً ۲۶ هزار نفر توسط ناوگان اتوبوسی منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453898" target="_blank">📅 21:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2d2Sv_qaAIDJ_-nDQAWRFw66b0XWi7hBlLgbrZ-GwG53FKIrJ2OMkhZKgN5LvMhK9fACwS675zGZtkxytOHEOwNy8xBP7UKbkuZ_6ROuwoQFaX3ugSTORY83SIuBiESD3oVWmHJf-42dFucwtC1iBNFK16ZyqPt2DIX1SmD0Ffu6V8SW0JYN8VCXp_FFkYYo7mBptdYD7Qp36PQfnhhMhLiByPe8XqgoH00zenuXrusOdqz-VCBXffY-v8ptLoO7MpbhGgkob1Lern0X5MuonfNeTeb8uyIwt5ooVfDXzHqqHLLg7LTC03yAy5HHOK7b-AZrHtx7Hp8RdFfjHeAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEMZ8yg-T9oSJ7CRbvuIvr8cE6HkLakd3UQ0VwdNHmhnGLKP_mCAqlwZlKFjC0BP_LXhALSgOBq452qVd17k0TOQpm-c6CU-ZkPrCOuRua1ZON9UqSWg-Udi7hjVeT6A1yTOyi3q2rJGVdBvYfdIEF714zWeBcabWC_WzTtT9vvOBykpUXIE_jWeAoX72jNj_CdYESH-91Ursj64FSQ7BCveGH2u2Nks-z5L2ph39GqnHCOuYYBEGBz5hrrh8eyl4DHp20ESmnt83mbd3NZP62fMUNcmeEK2ha7G5uc9xetjAdWnTCKLjpYLFXT6WzbZhT2ih0sWjy2BeIlyo6QKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqrhIczTPCPtJFuUiw6lE36GfWAvtO4FRkAd8vq0G8QRpGzZmb0u0kN41tZkJs5C4_emHFezyNjJChPWq_XHyw1eQCK6gnV9JUUHbdNP_y3sQlFPe3uUGhw8yvP7nhy8qACfNn9kxRHUaiUh-Amwpt97R3kzDXzPNb5JFLLUHR5YpA-Z5M8TzBwfcnQc7_tNnYbO-Bnz-2ejz-yi6RW8LDKZUM1C6Bc2Xsl1dXTo1lNiNB8cdbA-dpFrFEmf7XcRCcQUuetOvLqfNsRZagKIV8tgdr1ENj9KAQ9anMAgwYOjQ5GVPb8qSqyufqXsULiUNasoKYqMcC-y2cez8rxj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cjv1Czl7LPuC9QISmoFE6U6fy9yz7SDIItuCYUZFnyVXZQnC0APXX9ZTe0ocY4-TQ_dqhujfNSbkpX-QGseD456Knv-yq3Y3t3J_gQfV1_WiBa7uG-rJdHNuD4siHKveNA-JakhfDcm5yrAwYjNXiBppEBKZ_TwWcFWMfKHFCgWVfbKuHTlIrJ6xYksUJKiDjHz28zIy4zSRt5Qr7hjc5LY9gVanbk7mUDFziQ-jXUfHmcWO0rVMIBWokIHxiL67NiisatMelghNX79fJkNDUPC5lp3MTVefVeHzgKb8DQ_W-fEE3KLg_cocXjabm4v3ZJd9ZsEZ3T183HLCgD0XJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/his0cKzr2wq5eUA0NdMJoRgE6-KPxuVWK1PrL2T8kZGf8JckBXwqP9dCEp4Aq6dwdKUYO3uSbaH-VcPvg18_Wja829LTj9eWVQVUFeR5GHta3BiZ9Wbd33EO2GCbpUdGh2J_AC6LGPf7_-fpvCdXDAlAy0SD6Sm0Ab3AMSG64qh1kFPmRw2drY2JCNkquUkVmfHYrnWpQxqShZQLP7cqr_OjFBYuHHyvX4q6lVPZ4pUICM5Npe6GJ42RFnDFPBGhUqM54xQoUoZNnK8wQFWoDgokMxsfmwNpBpQZpI_D__AaI9yRqDuuSDAtJ5vyD9dT5N8X0UM0Tl0NsLEEP93-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHF_bv3Sxg_PNbR63eWel0h47p4OjhBH9BDXzH1GXTscaG6KtNv19OrSZ89Dz0-E1GZvnOzDhH3B_i3Njx0JfDcCAeX0Fh5Zr1mfAeCOfWdIdaFXokpmCWeOgZFkyCS59AKaUw93RoVPQdce83RGncc-8cAwO6fy-q6rCQUiC3us4EdU_bG7RL1PXNdYP5DNx7lX8ChNFd5CycSTJlU7DsdqH6REylzSeAEdOSGEQqCwgeevC9RzBj15rcI_Pod2eUXGWRNIM1JDCmMFnULXzq1ka3p8B0SiUSF7ClsMsyQwjl8egOY2eKpC1el2gQcEpN9UXhq1d0PWSdEZd1eTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAYxrl1MU9Qu6va3vHrs_UlwHN3pWqE0cpRcIF05nzzTnbPfVzqBBLVUZWx9svLLKjte0R-LHvNUZYwa9liOjxNbesiVF_R8RCq23mRSYD4_XkHywHwelLC54711falJ_6FoYDo6ZO3vYzox1ABfWHRoFw8WdrxN43RkBAH-_mloE4agoqwxLDYNRxTcZ0wthPdsSSsnKD9spP2kXcTRiq9O7vrKO1las9pXQ5RZQ2VBPI_bM3DbjWJt2XgrccYGrTocOSTCX1EToEnwNQ15IYMFp4PltTS3FwFKBRVJWJwOkkyvO4MHpHgfIxNAUv3PY-haCfuymzCluBMmUmDXTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین پوش‌کشی؛ آماده‌سازی مسجد جامع کبیر یزد برای مراسم اربعین
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453891" target="_blank">📅 20:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2f5ecb.mp4?token=BXn1pQnqptSJRr_QnVCz17b9_e9zl4qpOPePoBQljB2Ho3VOSo8YfyLRpZmICcnuSCVjInWlZJ6pFlkUJzeM5CB4S65Fb2_f1CW493k6Cxz1NmCCARcVFB6XQDU-3Aer6WOhQeaK346EhSMlbeVJvM4JRBHv-oi4QRJMEGPWmMv4piVO655kmQkfeopvzbJBrVAKgtkGmDJWtZ0xCEH2cRxe68SkhMZl_XB3VPcwNMfP4SpuPEqcyHn7oplJsZbUkG94j4Uo1ug6rwArxgZttWcRpmsjDzu1WMiNMKygjad0RZgk-Ud6Hxp1o9EFacDekV12eiauFwzsfp7B5s7azGSq6crs7NZD6U5xERyfQrtaI3EbpLN8HpjhwKLHxlawGXAw-yHtW0ukEVuyICoanpoNaiNzUqKKbB2BNTDuytP2OlSPzO6r2iUj9sljuJhDHEwlNPFhM0z4KGx9eNR_wO-PREdYslSdfMp9X_kiVyUZ3J3hjhlbcHZt8Jnx_5trz1EhMiaTuA8D948NRdducO3-3_KXkwiMVxxO459wj32Z26gpNTnqRVVdvZZ-1KiqHWHcUKbN12WXo3Omr5n62-le9PrGbdFIS2e2gYLJH_ZIdJrfWLFVn32mqLIk8rta2xBr83NF7k_ui_0B-2vre_7tUSNG1o-iuUIxTdwzU14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2f5ecb.mp4?token=BXn1pQnqptSJRr_QnVCz17b9_e9zl4qpOPePoBQljB2Ho3VOSo8YfyLRpZmICcnuSCVjInWlZJ6pFlkUJzeM5CB4S65Fb2_f1CW493k6Cxz1NmCCARcVFB6XQDU-3Aer6WOhQeaK346EhSMlbeVJvM4JRBHv-oi4QRJMEGPWmMv4piVO655kmQkfeopvzbJBrVAKgtkGmDJWtZ0xCEH2cRxe68SkhMZl_XB3VPcwNMfP4SpuPEqcyHn7oplJsZbUkG94j4Uo1ug6rwArxgZttWcRpmsjDzu1WMiNMKygjad0RZgk-Ud6Hxp1o9EFacDekV12eiauFwzsfp7B5s7azGSq6crs7NZD6U5xERyfQrtaI3EbpLN8HpjhwKLHxlawGXAw-yHtW0ukEVuyICoanpoNaiNzUqKKbB2BNTDuytP2OlSPzO6r2iUj9sljuJhDHEwlNPFhM0z4KGx9eNR_wO-PREdYslSdfMp9X_kiVyUZ3J3hjhlbcHZt8Jnx_5trz1EhMiaTuA8D948NRdducO3-3_KXkwiMVxxO459wj32Z26gpNTnqRVVdvZZ-1KiqHWHcUKbN12WXo3Omr5n62-le9PrGbdFIS2e2gYLJH_ZIdJrfWLFVn32mqLIk8rta2xBr83NF7k_ui_0B-2vre_7tUSNG1o-iuUIxTdwzU14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم تشییع و اقامه نماز رهبر شهید انقلاب بر پیکر شهید اسماعیل هنیه به مناسبت سالگرد شهادت او
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453890" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d2e8466c.mp4?token=IlfP73Xm-G7VtEAu6oP7_Vm1OfCtN9T8z0kKl5ZRzjpBSI0pkcMW9xKNG9JLt19X8HxQhfwYPbIEqBMm_Vny1nw4UHvovdMAzkdTqwIYXVhbkNbVMjHKhFo_Qywa4FCN7QiaQpULgRHELwbZM4T8_T5T1f9q03HGGBnXbj8hI2V6sS5owWlFy8dx40IOe-E_VgIi_9aK0w8L_mLulPL0NT5prejS_lj5Yugw6xFhPznBYomC1-V7XGKO9KH8rD_eRI4AQFvMgAyarJ_4wZ1V0_hKfLDv-zE0FJ1IiBrYqjxJoIYmc_CSOZqBDvkKnJjJng6Nhp-_DrA8H1nePZ6e14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d2e8466c.mp4?token=IlfP73Xm-G7VtEAu6oP7_Vm1OfCtN9T8z0kKl5ZRzjpBSI0pkcMW9xKNG9JLt19X8HxQhfwYPbIEqBMm_Vny1nw4UHvovdMAzkdTqwIYXVhbkNbVMjHKhFo_Qywa4FCN7QiaQpULgRHELwbZM4T8_T5T1f9q03HGGBnXbj8hI2V6sS5owWlFy8dx40IOe-E_VgIi_9aK0w8L_mLulPL0NT5prejS_lj5Yugw6xFhPznBYomC1-V7XGKO9KH8rD_eRI4AQFvMgAyarJ_4wZ1V0_hKfLDv-zE0FJ1IiBrYqjxJoIYmc_CSOZqBDvkKnJjJng6Nhp-_DrA8H1nePZ6e14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلوغی مسیر مشایه نجف کربلا در خنکای قبل از غروب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453889" target="_blank">📅 20:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیگیری تلفنی پزشکیان برای پرداخت حقوق اعضای هیئت علمی: این تاخیر ۱۰ روزه واقعاً قابل قبول نیست. کاری کنید که اساتید بیش از این ناراضی نشوند
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453888" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
