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
<img src="https://cdn4.telesco.pe/file/WIUSo-T3tyYpo5Dtkz1xo7xomoOCgtPrf8cZLRjcpw65SFgNmQGBZZrTitIZUau_0wdAWnqjinLwX7TvKXDyd0r3mOUKI1qgizBRe9dzaytIf-sDk-C9OzxQeDTe-a1oCPrV5FTTFXvPgNsRn2Fnm48p5V6irGkTyujWe-7a3haxWqcyo25BW1pE2LgO15Bch0YQi8XMmI3pxjs8R5zA8g4SKiW-orgT9z2kold3gsVwzvEUceHkkBs_26HwJbObfQutnd67nKGLSb2VwYkWuh6RuUuBvV92r1Sxg1KbPKC1j4XU8eyVEWRfgcrLFxK8nW7lhLlclN43RZ4aYzq0-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 05:01:38</div>
<hr>

<div class="tg-post" id="msg-438261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJxmmaDpaFTIGmx1DbKixh8wCsnerBl_H2G7hwU2RRo5NCVFiNcpHEiqAI--BMt9VDuA8EQYpoofJtZYAmoaFRXW5j9Oqw5LtADz8VxZkBlsgRfTdFErZfF0athNBtVKzDxbFqkd9wrSW5Kk50yJVv3JT_Etmsb8D1j7o2MH8tfUDlihdSgmzOzNpfwXgP0T1fA7iXnAPrmpC54oYSPyi9w63F6mS66y_CWiqmrLoDpPziQWRVLQrPEw6kJB2UgQW_ocHZAhJZTuEvcVMHm8bR7kbtZqL2IwVDt0DXe9s0JSPwbVeRApvYlgkchnHgz-H8SQKHEu8mw1KkQnPSpuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ واگن ملی امسال وارد خطوط مترو می‌شود
🔹
مدیر عامل شرکت متروی تهران: سال گذشته ۱۴ واگن قطار ملی وارد خطوط ۴ و ۶ مترو شد، که پس از آزمایش‌های مربوطه استاندارهای لازم را به دست آورد.
🔹
امسال نیز ۱۴ واگن قطار جدید وارد خط ۲ و ۴ خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/438261" target="_blank">📅 05:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرودگاه بین‌المللی تبریز بازگشایی شد
🔹
سخنگوی سازمان هواپیمایی: فرودگاه تبریز که در ایام جنگ اخیر مورد حمله قرار گرفته بود، حالا به‌دست متخصصان ایرانی به مدار فعالیت برگشته و چهارشنبه، ۶ خرداد بازگشایی می‌شود.
🔹
این فرودگاه، سومین فرودگاه پرتردد بین‎‌المللی ایران است که به ۹ مقصد خارجی پرواز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/farsna/438260" target="_blank">📅 04:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ces2z0sFtAOqbpCnI8tTP_vEMRqjfdc_Ju5AslFkGYM1IUDb8tRtRuZuLJ-8d3iZGzhoc0suZjO-qHl_fko0ASLUxGx5vJDZTNID6XrLp2zVIPXopje271WPK8wOMk0kjPVoxgUv4sUwPc9S8yJt80SCOSoRLxF3HuFhd_1vInFicE4KDtZ5CBP7zEzbZ01rLJjpvp6py58XFfRCImyU0FQcViRLIds7p0-zQ27xBvUHTpEGg2TC3LxLAuMYelePQkPOeCfOI0j_iMvVFBrak5qX0up4uZNf8F8xkNmr6hbhDO7LebSH00HRSSpfYhhhg2bnuXxYSB97N8zKTLOS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از جنوب لبنان به شمال فلسطین اشغالی
🔹
منابع صهیونیستی می‌‌گویند که در پی شلیک موجی از موشک‌ها توسط جنبش مقاومت «حزب‌الله»، آژیرهای هشدار در شهرک‌های صهیونیست‌نشین شمال فلسطین اشغالی فعال شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/438259" target="_blank">📅 04:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
میدان‌داری مشهدی‌ها در شب هشتادوهفتم
@Farsna</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/farsna/438258" target="_blank">📅 03:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قطع برق ۱۰۰ اداره در تهران به‌دلیل عدم‌رعایت الگوی مصرف
🔹
مدیرعامل شرکت برق تهران: همۀ ادارات پایتخت به کنتور‌های هوشمند مجهز شده، و مصرف برق آنان رصد مستمر و مدیریت می‌شود.
🔹
طی روز‌های اخیر حدود ۱۰۰ اداره و بانک به‌دلیل رعایت نکردن الگوی مصرف، مشمول محدودیت برق شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/438257" target="_blank">📅 03:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbIVrsobTI_TiRmOI0XdQxfaMBI3MVtXNINiIj5golK4R0O1qtPSOfo09jvQV9FkywUx2MsWsKmX-U4LbMIPLBqIfCSdxlxCqfUmYROcQ1cXOef9AUzFsBcpKJMnzY-VHicWcUPnUH5p8ewB42pme_O8Q4wmbiaMg2i44POFOaFpLVd_uu8vnyg3-pSTF3k66mveWv-GI8g_RI5cvJQrR7gW6dfr_aZ8Ac-iauVnJRQtaoQHG4MSxarLK2DEf3--nHQrTfX8bHp-UrGKPvvWXRN8ozTe_gNLmJTy4XHtiPqXHO1t7P3uqTkzsoLeSX2xf1U-gTkrx6Kb0nYKgzWsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آشفتگی در آمارهای پنتاگون از تلفات نظامیان در جنگ
🔹
تحقیقات اینترسپت نشان می‌دهد که آمار و ارقام ارائه‌شده از سوی پنتاگون درباره تلفات جنگ علیه ایران بدون ارائه هیچ توضیح مشخصی کم و زیاد شده است.
🔹
اینترسپت می‌گوید مقام‌های آمریکایی تاکنون به درخواست این رسانه درباره آشفتگی‌ها در ارائه آمارها پاسخی نداده‌اند.
🔹
این رسانه نوشته که وزارت جنگ آمریکا در حال پنهان کردن آمار نظامیان کشته و زخمی‌شده در جنگ علیه ایران است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/438256" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzR4fuTLLqxruzH4CpZq4QLitmqXwOvenUOimu8uZdzvvnhu5NBpi4B6qwBKQ4wH6ejqJ2S6VnTz39ZMXcBx6ARF7MHzJdYunVBgye0YlQfHMa_EGFSGJiaAItIE1U605dAR3g-esK9vWvs42xVGt3RHuQiBwl4tsEQBbnns27E3qDspi19SHCDSGItg8dhnbeLiaOQe_XeQ-jLRWitszXoRtvedRPrszRg-A8DcsqO-Kt8AvlmYSZaIp_hqeAwdGZX4JwWHRM2823d7bF1-zAeKKCqxYDAorYlqexRYgL6nxoUHp29ah9-7KqlZVlfLfHFg3g5_b7i0SBkx0CI8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشک کروز مجهز به هوش‌مصنوعی در کرۀشمالی
🔹
دولت کرۀشمالی اعلام کرد، روز گذشته سامانۀ موشکی کروز مجهز به هوش‌مصنوعی برای حملات دقیق را آزمایش کرده است.
🔹
این سامانۀ موشکی از ناوبری تطبیقی با ناهمواری‌های زمین برای هدف قرار دادن اهداف تا فاصله ۱۰۰ کیلومتری با دقت «فوق‌العاده» استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/438255" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791f29930.mp4?token=rxqL_CIu5HlbOCzJILWlAdd0XcSGSDi-xBNyzB_qM3n8_P5ktORN4NAbrRqAgIsiHuoLAaWeLIYGkU-Af6yhuAH4_9nvEQZC3GHUpJeLb2ToH1jNE54o0GNkFXcsZCCJ26coBteWQMltK0MkX1HiC1LnBSpl8CXDdcP_5kRRLD36g3MVlkV-QNhLjnTho7Irv_xisy1Z63s0Kz_oO0lNjh9EGo_7b_2UFQp3NnMFtPwe04RmxdLWlmcSvL9O5cZq8yzrs7VdAojR1BJCSaau6Z8a_ywUPaKaSvxcPx_bBzcay4k2-k1eSlc0iz0MqoU-KdHX1Jwf_Bpylgm1_fXW5nvRt3hnMlSOY0BVw0tYo2f8FKc3igpZTeSw-jaS_VutWdIaGBkHSwvn4f0J8TK8WwIcaaKzfpONBSr9vW6fUwAvK7IPb9CkjFZVVQlixw5t7DiwihkohFOr2UkO8GuF5fhZIrq7mrtkUqbhTdeTkpPbMAw3WukrahslfbKI0w892PHp0pKXWCIK03GMUUgjZ2Am_42JajA9Y1x-SaRC91uwKMjuRdYh1KhH9NfiVgF6ha58kdKuGbs4lyrV5SYC0YnRw1q_ZGCZkdjFVkjr8BVq7EO_r2fz3DnCfYo27rKTyg2O_ePI9nhKk358tSff7POOJwaIOCui2Zy4_IyDXG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791f29930.mp4?token=rxqL_CIu5HlbOCzJILWlAdd0XcSGSDi-xBNyzB_qM3n8_P5ktORN4NAbrRqAgIsiHuoLAaWeLIYGkU-Af6yhuAH4_9nvEQZC3GHUpJeLb2ToH1jNE54o0GNkFXcsZCCJ26coBteWQMltK0MkX1HiC1LnBSpl8CXDdcP_5kRRLD36g3MVlkV-QNhLjnTho7Irv_xisy1Z63s0Kz_oO0lNjh9EGo_7b_2UFQp3NnMFtPwe04RmxdLWlmcSvL9O5cZq8yzrs7VdAojR1BJCSaau6Z8a_ywUPaKaSvxcPx_bBzcay4k2-k1eSlc0iz0MqoU-KdHX1Jwf_Bpylgm1_fXW5nvRt3hnMlSOY0BVw0tYo2f8FKc3igpZTeSw-jaS_VutWdIaGBkHSwvn4f0J8TK8WwIcaaKzfpONBSr9vW6fUwAvK7IPb9CkjFZVVQlixw5t7DiwihkohFOr2UkO8GuF5fhZIrq7mrtkUqbhTdeTkpPbMAw3WukrahslfbKI0w892PHp0pKXWCIK03GMUUgjZ2Am_42JajA9Y1x-SaRC91uwKMjuRdYh1KhH9NfiVgF6ha58kdKuGbs4lyrV5SYC0YnRw1q_ZGCZkdjFVkjr8BVq7EO_r2fz3DnCfYo27rKTyg2O_ePI9nhKk358tSff7POOJwaIOCui2Zy4_IyDXG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هشتاد‌وهفتم کرمانی‌ها در میدان اقتدار ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/438253" target="_blank">📅 02:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRqHT7gt6FbrGg6ZF7SPG3aCe4ijJkHlgTVdkDG7LQAKMH94qnHD2KSb3qm37HAj9QL_3P1eYiXn3ca2mjk2BL2JXuXyewYKez6Mllie9lu9JuMkWes0buGn3-UBvJh9MOjvKnsa0-UvMo3JEFti_thBEO5f-btE_QtIbUxg0s9dcOF-TXpGg4cEJi6gw4IrwYa4uJrM9Ht9C-hC8abk-Fcb4RNLErnqWP-9uDC8-5K6-SgbRLo6ZdRzvV2VPUhc4pzbE97Q4Wom_ucX-ZIdPPyOgSvkSjesFN7CJgyCLOK2Pvpx5Lcshl7vO5zI4t-MeYSbZ5HQWfm13GZj7RagxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعه‌بندی گوشت مرغ ممنوع شد
🔹
وزارت جهادکشاورزی از ممنوعیت قطعه‌بندی گوشت مرغ در مراکز غیرقانونی قطعه‌بندی خبر داد، و اعلام کرد محموله‌هایی که در شبکه‌های غیررسمی توزیع و قطعه‌بندی شده‌اند، توقیف و به شبکه‌های رسمی استان‌ها برای عرضه ارسال می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/438252" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e4776e5c.mp4?token=kXLQtWnw1tM1SYBRf_yGZ2-rIqMZkC3JshR2ihNrZ8qgyPuzznjP6Ya0m7nf-VB_7kx3oEdAFKekPENfEH-2vZKvG29Y7hswCjDbedaTKUqCuejgpyaQaTBSkr3F6xqrS6bLmoVKxAwIqP61BC-OrkbG0pY13NhRMDZWvVcwy43xSlgOJhesrSSpVPIU5W2lrK5D4BQi3GVlRiJowNiag55iZtF6dsOxX6AccrwL9VRgCqM8VIwVTrn-Sj0yWbXemufaGgrUklc_BcG8OvIQ14bqcZTz-6fcw9U5kGSj-fzmi0iz6Wvdu4Pp236bFtW450xq3hMZYLReKznEEiYjbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e4776e5c.mp4?token=kXLQtWnw1tM1SYBRf_yGZ2-rIqMZkC3JshR2ihNrZ8qgyPuzznjP6Ya0m7nf-VB_7kx3oEdAFKekPENfEH-2vZKvG29Y7hswCjDbedaTKUqCuejgpyaQaTBSkr3F6xqrS6bLmoVKxAwIqP61BC-OrkbG0pY13NhRMDZWvVcwy43xSlgOJhesrSSpVPIU5W2lrK5D4BQi3GVlRiJowNiag55iZtF6dsOxX6AccrwL9VRgCqM8VIwVTrn-Sj0yWbXemufaGgrUklc_BcG8OvIQ14bqcZTz-6fcw9U5kGSj-fzmi0iz6Wvdu4Pp236bFtW450xq3hMZYLReKznEEiYjbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۳۱ شهید و ۴۰ مجروح در حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم صهیونیستی به مناطق مختلفی از جنوب لبنان خبر دادند.
🔹
وزارت بهداشت لبنان اعلام کرد: طی حملات چندساعت اخیر رژیم صهیونیستی به جنوب لبنان، ۳۱ نفر…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/438251" target="_blank">📅 02:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
۳۱ شهید و ۴۰ مجروح در حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم صهیونیستی به مناطق مختلفی از جنوب لبنان خبر دادند.
🔹
وزارت بهداشت لبنان اعلام کرد: طی حملات چندساعت اخیر رژیم صهیونیستی به جنوب لبنان، ۳۱ نفر شهید و ۴۰ تن زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/438250" target="_blank">📅 02:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwSd8mN3bUCLroP2A8cnuwcLIh8-6MBotzkI56G18jDW4QHEZp8h7-qRA0M5RPo9u6ot7KlubxpPw6D5IO3YIzMRB8a7aca8QRKLz5eRGskqEecvnoleuykJ8RiP9Z4uXc2BpeqepAXT1ML17svtGDjo9YUsYhkZVoqp-PRrxacxglgjJ2bGhe2L7cKjw0y5hfMQW6puz-ygMNpuA-HCSrEjgRf92B_QTtpQ6j2SkAs2-Mx9V2NLpryrZWEcBeHs1mKUOyCmLvqfx7s8Neh3-nKa4CO0pDhaib9_LwBMKpseF3SKvbXBJ0RlFA-jl1jp1paHSR29_W9qkD0ddYAojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام مسکن ملی افزایش یافت
🔹
در بیست‌وچهارمین جلسۀ شورای‌عالی مسکن، افزایش سقف تسهیلات مسکن ملی از ۶۵۰ به ۸۵۰ میلیون تومان به تصویب رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/438249" target="_blank">📅 01:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ce2af54a.mp4?token=rZIG_-WhL12erGoWNcsMMdIaBSp2Wm76i9taPhKg8mNA9r7cfFXItanpTH3Dl10a0tZxNgGyco0R6ZZNkmTKLlgLEKe4K6Dwv_OzBBcttomP6jXpwrSnrGJnjs9IwoYxO8q-93FZP6gaQTRAIE6RY3KgYq5gZ3n_svpcgxkeCpwMTdhQZNGuDDFWig6jLZlGO0yWxKPql73zDHBn0356832e0LyxKN_HIHRvEUn0OiceffYspcLBGRo1TXTONUFMUOTlKxjV_BrvLZI1JAQHy-G8Pbtg6_pdLbS22Vz5Qd8D8PGXfD_MVUdnmySl-MwfdBUy0Q8HYDtv8f2z-r0XKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ce2af54a.mp4?token=rZIG_-WhL12erGoWNcsMMdIaBSp2Wm76i9taPhKg8mNA9r7cfFXItanpTH3Dl10a0tZxNgGyco0R6ZZNkmTKLlgLEKe4K6Dwv_OzBBcttomP6jXpwrSnrGJnjs9IwoYxO8q-93FZP6gaQTRAIE6RY3KgYq5gZ3n_svpcgxkeCpwMTdhQZNGuDDFWig6jLZlGO0yWxKPql73zDHBn0356832e0LyxKN_HIHRvEUn0OiceffYspcLBGRo1TXTONUFMUOTlKxjV_BrvLZI1JAQHy-G8Pbtg6_pdLbS22Vz5Qd8D8PGXfD_MVUdnmySl-MwfdBUy0Q8HYDtv8f2z-r0XKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار روسیه به کشورهای حاشیۀ خلیج‌فارس دربارۀ پیروی از آمریکا علیه ایران
🔹
نمایندۀ روسیه در سازمان ملل خطاب به کشورهای حاشیۀ خلیج‌فارس: ما مدت‌ها پیش می‌گفتیم که اگر چنین اتفاقی (تجاوز نظامی علیه ایران) بیافتد، چه بخواهید و چه نخواهید، ناگزیر وارد این بحران خواهید شد.
🔹
به آنها می‌گویم، شما گروگان سیاست آمریکا در خاورمیانه هستید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/438248" target="_blank">📅 01:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61e8aa2590.mp4?token=pL2gjqL7Qqv-1hj0JdVGiKcKt9EvvQPdkjM3eiQ0ZiAIBuY36bRC04f3UP_D8n1c0F_bHHvDCYRcx3COP1Z4bNzY3xc1Nfn9b1ocprZvGP7mFaBcAWWv0coaYPpzluMRCjTxoW-Za1WQXYLvT5Gs6XvWKJefhYVOdaQ4j9HwCEdvtMglZit9OyFVmkhmerpIIUvoYKvGrJa87_t6l57T3A8j-Z0QHB5C7SivxC1AmxpP3rr-41B6qwCDTNNVj94MBtvShlCmyYwh7gJxFRz_LC7lbb3OEei-OXKQmezXvxNgV1BqZrIR0I-3KgJKUzJNU6vj5F6vev3Izs_FiJYJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61e8aa2590.mp4?token=pL2gjqL7Qqv-1hj0JdVGiKcKt9EvvQPdkjM3eiQ0ZiAIBuY36bRC04f3UP_D8n1c0F_bHHvDCYRcx3COP1Z4bNzY3xc1Nfn9b1ocprZvGP7mFaBcAWWv0coaYPpzluMRCjTxoW-Za1WQXYLvT5Gs6XvWKJefhYVOdaQ4j9HwCEdvtMglZit9OyFVmkhmerpIIUvoYKvGrJa87_t6l57T3A8j-Z0QHB5C7SivxC1AmxpP3rr-41B6qwCDTNNVj94MBtvShlCmyYwh7gJxFRz_LC7lbb3OEei-OXKQmezXvxNgV1BqZrIR0I-3KgJKUzJNU6vj5F6vev3Izs_FiJYJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعقیب‌وگریز پهپاد حزب‌الله با نظامیان صهیونیست
🔹
رسانه‌های رژیم صهیونیستی گزارش دادند، یک پهپاد در شمال فلسطین‌اشغالی سربازی را تعقیب می‌کرده، و سربازان دیگر وحشت‌زده سعی بر پیدا کردن محل آن داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/438247" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تشریح فعالیت ناوگان اتوبوسرانی تهران برای مراسم نماز عید قربان
🔹
روابط‌عمومی اتوبوسرانی تهران: خدمات حمل‌ونقلی این شرکت، با تخصیص ناوگان ویژه و تقویت خطوط عبوری منتهی به محل‌های برگزاری مراسم، از ساعت ۵:۳۰ صبح فعال می‌باشد.
🔹
پس از پایان مراسم نیز، شرکت‌کنندگان به مبادی و میادین اصلی سطح شهر، بازگردانده خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/438246" target="_blank">📅 01:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQTh-EqtoU5JzoFKYLor2yyM5eWX7d0A7KeEl4lExtC4eHaucW8LxK4ZR63FYwIfpHMhLLjlYvjEhGKov0J4LnINPfU-A2pBLzxHYmCJfoX37JPcMTWN3hVeymS5r0Atl1vDXQRLAMOPnfAQYI6q69i5T8zfHt2pH_72PngnP0DEyY32P6hEe0nBmuPCwiqwBCbHXoHwvFqiueqlvB7pUq_hqcWYn4llXUXmcKetSdy9_eZF7eIshOT8fhlL3-AG5yqrgZBdBds-b_WyK9YGWU-x-FxtK8GdTranjhi7KuDCQQMcUsw97Z9A4iO9cGS8pOnnAWv5C-JCPzpkatEChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مرگبار مواد شیمیایی در آمریکا
🔹
وقوع انفجار در یک کارخانۀ بسته‌بندی در ایالت واشینگتن آمریکا، منجر به کشته‌شدن، و مصدومیت تعدادی نامعلوم با سوختگی شیمیایی شده است.
🔹
به گزارش گاردین، آتش‌نشانی لانگ‌ویو اعلام کرد که این حادثه پس از ترکیدن مخزن محلول شیمیایی «لیکور سفید» که در صنعت کاغذ استفاده می‌شود، رخ داده است.
🔹
به گفتۀ مقامات ایالت، این مجتمع تقریباً ۱۰۰۰ نیرو دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/438245" target="_blank">📅 00:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شکار بزرگ حزب‌الله در روزی که گذشت؛ ۸ خودروی نظامی و ۷ مرکاوا
🔹
حزب‌الله طی سی‌ودو عملیات خود در روز گذشته، علاوه بر حملات راکتی، توپخانه‌ای و پهپادی به محل تجمع نظامیان صهیونیست در جنوب لبنان، از هدف گرفتن ۸ خودروی نظامی و ۷ تانک مرکاوا به‌همراه ساقط کردن دو کوادکوپتر اسرائیلی و انهدام یک سکوی گنبد آهنین خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/438244" target="_blank">📅 00:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ_-l0JlIM5T0brFBZxMjYs9I7QGcc2KYytKxS0fMNp8qW82-ovFRRP_ew0-eiDYGm22amej5ucGZRgeWAIev7RjswPwZfP2EvHeGCK36Kmxw1arPdLsz8A-t8RstjcGAobidbm36gfC1c5Dfswhl7dsh6N7gEd43cjflSscheIlgd7oMuqYVRiu05MkBYsLXiLagAAaKdPe_ZoIKN-7ZpsmRvM7mX0nsWHpgJUyF9OMy_MutEkMHMKCyFzFh4i6OQ0qo2i64_NHy9YmvdNJX1z0fM9Myboo5bzk19P_fWrFrXjEAvBSIYzOfIdp4FqJ-2ecmYtSZotTowDoNxl5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهانهٔ اسبی
🔹
شخصی نزد دوستی رفت و از او خواست که اسبش را برای کاری به او امانت بدهد.
🔹
صاحب اسب که تمایلی به این کار نداشت، گفت: «اسب دارم، اما رنگش سیاه است!»
🔹
مرد با تعجب پرسید: «مگر بر اسب سیاه نمی‌توان سوار شد و کار را راه انداخت؟»
🔹
صاحب اسب با صراحت و خون‌سردی پاسخ داد: «وقتی دلم نمی‌خواهد اسبم را به تو بدهم، همین‌قدر بهانه هم کافی است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/438241" target="_blank">📅 00:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d45e25a0c.mp4?token=EtURQkFkShVS1Ab56Fht7-9kMLS0xSpRytwhmOk9hw44bWwEtD_eUgcUSVHXh4eSfcBkP9PR8ZHeTjqVRhyf7ZbHMLY5w28YfI1dtifAnhTaWnz0gyc6amTNW6bTasHIuVfolOiBjEkYG4YGtsuaVErRfv6uMEKXMJ2JGl7w0M3C9-Zdhhvm1IXKEGdiy6Eun_u9P4uCTCGxYrz-LTXkD-gU0W-26w36lmb46llstTv2qsQPFGASAyqgNdxlJMhpcRjogVKlkoO8NFZiyxk-lDtFKGA2nGgZoEkVh-k5TAraTrXqLNw_jf8Xw5USv_ZNuWHlzu3gB2SjK7jqeyQMpy2dPRrKhrDOEiJ0h1p1wWWs-l5MnEg6WjfI6rorC_q8IPafgBidy_Qsd2U0Ingc-S60VH_ER3y1kGbJX8TNFY4tp8eWCKJRIamKJNtArW3KbzaG0Y4BrstzzE_VDIK_dEgO_OWv-Ph077iVqDkSedb-XCY5forK2caRKFZmR5zmB2cX39Ec0Eb0IPzNnBX40E7wHtcE0RXUnwnXHjuePqCwNxjXnwid6gqTuGm2PfCPHvjWGGUMnwqtZJ3v_RnG0Pf3rfztx4wnvcUIlvQL6-SnvQYdNts8IxkAi_De3aIy6f3BNWJCsQAoG2wb1ithb7PlzS7XRdl2tEFTcBWQ3So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d45e25a0c.mp4?token=EtURQkFkShVS1Ab56Fht7-9kMLS0xSpRytwhmOk9hw44bWwEtD_eUgcUSVHXh4eSfcBkP9PR8ZHeTjqVRhyf7ZbHMLY5w28YfI1dtifAnhTaWnz0gyc6amTNW6bTasHIuVfolOiBjEkYG4YGtsuaVErRfv6uMEKXMJ2JGl7w0M3C9-Zdhhvm1IXKEGdiy6Eun_u9P4uCTCGxYrz-LTXkD-gU0W-26w36lmb46llstTv2qsQPFGASAyqgNdxlJMhpcRjogVKlkoO8NFZiyxk-lDtFKGA2nGgZoEkVh-k5TAraTrXqLNw_jf8Xw5USv_ZNuWHlzu3gB2SjK7jqeyQMpy2dPRrKhrDOEiJ0h1p1wWWs-l5MnEg6WjfI6rorC_q8IPafgBidy_Qsd2U0Ingc-S60VH_ER3y1kGbJX8TNFY4tp8eWCKJRIamKJNtArW3KbzaG0Y4BrstzzE_VDIK_dEgO_OWv-Ph077iVqDkSedb-XCY5forK2caRKFZmR5zmB2cX39Ec0Eb0IPzNnBX40E7wHtcE0RXUnwnXHjuePqCwNxjXnwid6gqTuGm2PfCPHvjWGGUMnwqtZJ3v_RnG0Pf3rfztx4wnvcUIlvQL6-SnvQYdNts8IxkAi_De3aIy6f3BNWJCsQAoG2wb1ithb7PlzS7XRdl2tEFTcBWQ3So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفاوت شب ۸۷ تجمعات نحن منتقمون کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/438240" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
موج ۸۷ از ایستادگی بروجردی‌ها در خیابان‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/438239" target="_blank">📅 23:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d69293677.mp4?token=E-jFIbCG4jM0K6lmS3blwTZD0X6sTBtzVfm79ktGTkZlfrwL_QQWSaC_KWnqnFmAdUuLkgFia_e8PSqYwkZz80Ho8cvLWWyXgeGjYWqdf_72tihjGVFUeoVNkk9xK9Mktmrksxjgkyd36fhG5GTAXXsqJUHl990Rmo_68HXzf7LtyOYnggOqTv3aRwNUw5cuxQtN7Q7_bDGezmZWOmS15-NIZXlYCK0f02qcpwxb2l6Z6M5fIyewg8fB9qyproW2CY6Xn5wUanXcj_Y1cqQgn_FaHhYZhlbmRMhNu9eOoOO7BiGMktF-aUGAaKDJ3cpE0xbeFI3ESMqEdT5RFyfYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d69293677.mp4?token=E-jFIbCG4jM0K6lmS3blwTZD0X6sTBtzVfm79ktGTkZlfrwL_QQWSaC_KWnqnFmAdUuLkgFia_e8PSqYwkZz80Ho8cvLWWyXgeGjYWqdf_72tihjGVFUeoVNkk9xK9Mktmrksxjgkyd36fhG5GTAXXsqJUHl990Rmo_68HXzf7LtyOYnggOqTv3aRwNUw5cuxQtN7Q7_bDGezmZWOmS15-NIZXlYCK0f02qcpwxb2l6Z6M5fIyewg8fB9qyproW2CY6Xn5wUanXcj_Y1cqQgn_FaHhYZhlbmRMhNu9eOoOO7BiGMktF-aUGAaKDJ3cpE0xbeFI3ESMqEdT5RFyfYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای خواستگاری تلفنی رهبر انقلاب برای پسر یک شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/438238" target="_blank">📅 23:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e83c8266.mp4?token=nD77I9zCTnXPn2KQQGgFMf2ky8_58DRv2M1kSZK8Kwdt67h4bFQWp93S3OgKeCYs3ZdS4YVid1nzcLGTflRmVz0jBU0YAhH9E8M_zttCBPNNQhUr2RJtjwUXYUM4t3GQ_IPMs7CII1IwYnBoZOe3ZlCmry4WhpyCoMVxnBXScr--KPcn2g3Z25PbNNXnjIBH26U6hMbxqZCqV4I7DSradlQK8Ou-hHFWw-eeNpD_bMaSGm6IOGnDzXsEpNMyK0ESlOF1SVmrm3a8sDzuyqvR85BGJKHO_jP5O6VIDfhIdUoVdB6REbpWz1y-BnraGLl5znPrEk7O_BpiXVmX4ZfwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e83c8266.mp4?token=nD77I9zCTnXPn2KQQGgFMf2ky8_58DRv2M1kSZK8Kwdt67h4bFQWp93S3OgKeCYs3ZdS4YVid1nzcLGTflRmVz0jBU0YAhH9E8M_zttCBPNNQhUr2RJtjwUXYUM4t3GQ_IPMs7CII1IwYnBoZOe3ZlCmry4WhpyCoMVxnBXScr--KPcn2g3Z25PbNNXnjIBH26U6hMbxqZCqV4I7DSradlQK8Ou-hHFWw-eeNpD_bMaSGm6IOGnDzXsEpNMyK0ESlOF1SVmrm3a8sDzuyqvR85BGJKHO_jP5O6VIDfhIdUoVdB6REbpWz1y-BnraGLl5znPrEk7O_BpiXVmX4ZfwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ الله‌اکبر در جوار رواق کشوردوست در جمع عاشقان رهبر شهید انقلاب رضوان‌الله‌علیه در شب عید قربان.
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/438237" target="_blank">📅 23:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419cee0e82.mp4?token=GCVm3uO93vDoZUSn4ViqA_rFf6Nvdi2v1ZQ1h223rWQ3JqMh5So0Yi-ixyJwROwpmDyEVKoXhxXPyCWefp9jRIMu_Zi_sN1awUSRZEgQEXvgDwCvlTSy6Q0lTCzhzTWQOReDeO1kuGiQ3ce8tDd11_wF4tqpXZ4z1f0oZXwWk4mugMmohLCQDtDUmH16dAyr7IuHzw95yjGZwMgBWCedGI5-5q2N286u7ce9xKg3BAtV_OPBA1GEYrVxz_KnIqQxpSNrQ_tdxu9InX76E7lZbUNU4N_KXCREtTdEuu6RxeMeET-uVt4NNVs8QCqchP-YHcCQMwIKevaDHc1iiKL0DW01CX97WFvikaCpCDQFFTTclyYRT8AaaIikodTi1rAVo0xqXWfFbhVGcFpw3nIRvfqIZ2_yvpJDQpYcLZuTAyXJelenfdJgLIqI2t91FU8j4V1ZNqxJNbsnR4tUJ3WV5p5Cv4urCa6LIqMLMCQE_zRhIPwl0oDRXqiro6DHZF3Jj9Fe-VM6W_Zkh7cnY97YfQhsc9b52pSVs5tco93IoPEPOBvjYTtyToLoL14qo2EwYBszD18dSJwxbBus26D2tjS2E2LLf47VTBCEmQJQ2CSQJAmX3FXH2LEFVE2PJgPjGhOrA5edS-SZQJSUSLDU-AkwMK6bU0z4Azu_x4h6YxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419cee0e82.mp4?token=GCVm3uO93vDoZUSn4ViqA_rFf6Nvdi2v1ZQ1h223rWQ3JqMh5So0Yi-ixyJwROwpmDyEVKoXhxXPyCWefp9jRIMu_Zi_sN1awUSRZEgQEXvgDwCvlTSy6Q0lTCzhzTWQOReDeO1kuGiQ3ce8tDd11_wF4tqpXZ4z1f0oZXwWk4mugMmohLCQDtDUmH16dAyr7IuHzw95yjGZwMgBWCedGI5-5q2N286u7ce9xKg3BAtV_OPBA1GEYrVxz_KnIqQxpSNrQ_tdxu9InX76E7lZbUNU4N_KXCREtTdEuu6RxeMeET-uVt4NNVs8QCqchP-YHcCQMwIKevaDHc1iiKL0DW01CX97WFvikaCpCDQFFTTclyYRT8AaaIikodTi1rAVo0xqXWfFbhVGcFpw3nIRvfqIZ2_yvpJDQpYcLZuTAyXJelenfdJgLIqI2t91FU8j4V1ZNqxJNbsnR4tUJ3WV5p5Cv4urCa6LIqMLMCQE_zRhIPwl0oDRXqiro6DHZF3Jj9Fe-VM6W_Zkh7cnY97YfQhsc9b52pSVs5tco93IoPEPOBvjYTtyToLoL14qo2EwYBszD18dSJwxbBus26D2tjS2E2LLf47VTBCEmQJQ2CSQJAmX3FXH2LEFVE2PJgPjGhOrA5edS-SZQJSUSLDU-AkwMK6bU0z4Azu_x4h6YxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباسی‌ها امشب مسلح به الله اکبر شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/438236" target="_blank">📅 23:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cac6a41c.mp4?token=XTMpDmpotm_Z29nflLiDoOH1mGNdwZuUspxnevQDohffSZiWhhPj6J3vW-vi63P9CzrzBTHTR0cRwIT0HjTCTcpKf2XtduBwuyd_C5Tn_Z47g3ySIEKFDIbNJg_Qj0lXVMn7FxvkIHZlJCKn4hK3YJGU4XAIhRuEP_-0BzLrDt_o0z3rlWjuS7KrIRiAwL1hjgZsv_uN-eZ1-ZENvy2qM8GDead_sToud98ASiVfCy8vRzuaGP6PqOwj-X3jVv1k16_zB-c6Sxv2HRVMsBXEZ45vdCbph0QFBjyZ7A_dh8OiZDxluAPXdbvhoKdAj2IqQY6aidTZsWSjJqqm9_5qvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cac6a41c.mp4?token=XTMpDmpotm_Z29nflLiDoOH1mGNdwZuUspxnevQDohffSZiWhhPj6J3vW-vi63P9CzrzBTHTR0cRwIT0HjTCTcpKf2XtduBwuyd_C5Tn_Z47g3ySIEKFDIbNJg_Qj0lXVMn7FxvkIHZlJCKn4hK3YJGU4XAIhRuEP_-0BzLrDt_o0z3rlWjuS7KrIRiAwL1hjgZsv_uN-eZ1-ZENvy2qM8GDead_sToud98ASiVfCy8vRzuaGP6PqOwj-X3jVv1k16_zB-c6Sxv2HRVMsBXEZ45vdCbph0QFBjyZ7A_dh8OiZDxluAPXdbvhoKdAj2IqQY6aidTZsWSjJqqm9_5qvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری گرگانی‌ها به شب ۸۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/438234" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400a0b30cb.mp4?token=qIpUPhQ41Y5CZ8R1kQh4UnrQTef3OAJu1qqu-5GbFEEOAed3K_WEfDBipnA2gMLRttyQWERSFANzpqhVgGuwtTeWFf81r7ifu85eDx8M8xVrpeWy24IMZnfvV-PwreRvaPvNib79QsWGq3ES_O58pRvB2fZnmwvLcRzFvPrFZFKllqC9puAW038vFFj2hI-UV5lWuXq201pIEjJL-IU0oKvi-x_bWN6qd8h-UBSHYfRhulg8ZmD2OyDPrgHiJj_nhdmQ3jjheYONjNX5fFN8_7RMdkyT147Dj_Pf9uRP4FcWKIPzIvH2hiJ-hmqSWfWxo_VL1j-NzKof3pPtEdTNIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400a0b30cb.mp4?token=qIpUPhQ41Y5CZ8R1kQh4UnrQTef3OAJu1qqu-5GbFEEOAed3K_WEfDBipnA2gMLRttyQWERSFANzpqhVgGuwtTeWFf81r7ifu85eDx8M8xVrpeWy24IMZnfvV-PwreRvaPvNib79QsWGq3ES_O58pRvB2fZnmwvLcRzFvPrFZFKllqC9puAW038vFFj2hI-UV5lWuXq201pIEjJL-IU0oKvi-x_bWN6qd8h-UBSHYfRhulg8ZmD2OyDPrgHiJj_nhdmQ3jjheYONjNX5fFN8_7RMdkyT147Dj_Pf9uRP4FcWKIPzIvH2hiJ-hmqSWfWxo_VL1j-NzKof3pPtEdTNIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«الله‌اکبر» در بام ایران
🔹
طنین شعارهای مردم شهرکرد در شب ۸۷ تجمعات ملی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/438233" target="_blank">📅 22:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ef25ab28.mp4?token=X4xFJ9jl26iOQhbIVBV0X-nebMWDMUqGnJZrHk_qxazLimgQ_R6Ms5KvlSjOYvSiCIvrRD_zO06UTWI7nQGhfDVLM4nQL1q4VD7B99lzVU0rPW-n9Y5lZ2WyJSL4GEjOWtnLjmnkhSEhrm1FSfEvXOnc-YHK5y2VAKIg4uE05c5AFGZVbTaZxX3lOUfIDPT6xiSwsdW6z9Jvb4F5_Rz2huiLaaevy8pMQMe7xiGfE3Ib1UVj9gRmrHkL9UyLM9xwm1s3jktBPaIWbToRbxzeU74FZSUe0MYmT9tz_TbqmGyl2LkrMeI-2ECWknGDmdt1WT3g2J3tIfxrgYC6AOFDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ef25ab28.mp4?token=X4xFJ9jl26iOQhbIVBV0X-nebMWDMUqGnJZrHk_qxazLimgQ_R6Ms5KvlSjOYvSiCIvrRD_zO06UTWI7nQGhfDVLM4nQL1q4VD7B99lzVU0rPW-n9Y5lZ2WyJSL4GEjOWtnLjmnkhSEhrm1FSfEvXOnc-YHK5y2VAKIg4uE05c5AFGZVbTaZxX3lOUfIDPT6xiSwsdW6z9Jvb4F5_Rz2huiLaaevy8pMQMe7xiGfE3Ib1UVj9gRmrHkL9UyLM9xwm1s3jktBPaIWbToRbxzeU74FZSUe0MYmT9tz_TbqmGyl2LkrMeI-2ECWknGDmdt1WT3g2J3tIfxrgYC6AOFDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ رهگیری دوباره یک جنگنده F35 توسط سپاه در بامداد امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438232" target="_blank">📅 22:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1281a6896b.mp4?token=h0Tdnmw7TbZM_EBLPT5AR80Sdf0ba9wZ5x91eqg-4vBONzUSb7-ZPM7uf2hDHkjm4IjnaDoPPph9kh85KltoDD7o3rT8cxBtIolg7t6nyO3D--I5KZ5ZzEbeWKcqdDkfQzrEEEnnHu5olQ2eyFkKKlz6fMY2XbBGwFO9tmzoXa4guA-GmPWVAbFLGa5K0iem9g2eBsMcMqFbufB8La_5oKYcEUdyX9yKPaXPyB8KvVt2M45WB5OxCBvufbAyRztYW7pjNMxXzCE4m5RIn3d-taLndHKScuXeG1OBCR3Tra3VypJY-nXzVPHZTY-8Si7UX4R5h1E74Yc-nW7JXRtZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1281a6896b.mp4?token=h0Tdnmw7TbZM_EBLPT5AR80Sdf0ba9wZ5x91eqg-4vBONzUSb7-ZPM7uf2hDHkjm4IjnaDoPPph9kh85KltoDD7o3rT8cxBtIolg7t6nyO3D--I5KZ5ZzEbeWKcqdDkfQzrEEEnnHu5olQ2eyFkKKlz6fMY2XbBGwFO9tmzoXa4guA-GmPWVAbFLGa5K0iem9g2eBsMcMqFbufB8La_5oKYcEUdyX9yKPaXPyB8KvVt2M45WB5OxCBvufbAyRztYW7pjNMxXzCE4m5RIn3d-taLndHKScuXeG1OBCR3Tra3VypJY-nXzVPHZTY-8Si7UX4R5h1E74Yc-nW7JXRtZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات اولیۀ حملۀ رژیم صهیونی-آمریکایی به مناطق مسکونی لامرد
🔹
در حملۀ رژیم صهیونی-آمریکایی به چند واحد مسکونی و یک سالن ورزشی در شهرستان لامرد در استان فارس ۲۱ نفر به شهادت رسیدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/438231" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e134e5633.mp4?token=clQzfwDjwIPVE61PqIZmkDIqMFTeEFPeGv-Vyc-SIJsJbhfne2gzKYKxDwL1FWJhFmY30XDGiCWQEDH7nxubgDWvOtHBqaBL5PDBVWSdXBqRMY2GqD-qsglFZRirtoPccxkPyU1eCO7LT8OGNgDaJhtbPEuvHIINWysGPlfFV9GAizKS85A1Wq82YM-Cm35RUq-N-fXcNLSJLQ5Oa1iswbvGXyBorqip7yOQYPWoQwJg8aMVtxqB2CkDQJxGAUkVYnVJaS6649do7M1lCCrKVWf2OZqKp1a5uooFli0G4UxkqRN3otEGTWOOvp9lewUcmw-ss58VrhquqWlmX7PX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e134e5633.mp4?token=clQzfwDjwIPVE61PqIZmkDIqMFTeEFPeGv-Vyc-SIJsJbhfne2gzKYKxDwL1FWJhFmY30XDGiCWQEDH7nxubgDWvOtHBqaBL5PDBVWSdXBqRMY2GqD-qsglFZRirtoPccxkPyU1eCO7LT8OGNgDaJhtbPEuvHIINWysGPlfFV9GAizKS85A1Wq82YM-Cm35RUq-N-fXcNLSJLQ5Oa1iswbvGXyBorqip7yOQYPWoQwJg8aMVtxqB2CkDQJxGAUkVYnVJaS6649do7M1lCCrKVWf2OZqKp1a5uooFli0G4UxkqRN3otEGTWOOvp9lewUcmw-ss58VrhquqWlmX7PX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: یک پهپاد آمریکایی را سرنگون و پهپاد و جنگندهٔ آمریکایی را فراری دادیم
🔹
ارتش تروریستی آمریکا در ادامهٔ ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438229" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438228">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
مردم دنیا در مورد مردم ایران چه می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/438228" target="_blank">📅 22:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438227">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/438227" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438226">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6-rj1TECp0TDUMiZoVtNywdEVyvuJ_Z-26B5RtWdBhDlML4jwlpuVIaP-uta4jqWCzDqYWoj38kMBokfxxHVXh_vv4G_UGLrTAGfnjBFVL-QaANtuWaf5jhuFD9DuRaTnia1dKRFQ0rq74ilZz-jWwvHkTDoRjOQFs6bci6kiStyJB35j-A2KEKloXRRimuxzuXGJ_Xi5xUCppCSD49wjc26FKGjoGssSkl-W2mywAPhwShzsVJkesg5xlYfeCc7AMubfGmMAQQ_igUBHFWti2T1G6rhlFGbuaaAodlJ8D-ItrxPOmlZ19BgHZDSvtD1ITByV0IaP3sebg4gOg2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔹
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438226" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438225">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عبور ۲۵ کشتی از تنگهٔ هرمز با هماهنگی نیروی دریایی سپاه
🔹
نیروی دریایی سپاه: طی شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز  با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438225" target="_blank">📅 21:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">شمس‌الواعظین: وحدت فرماندهی ایران در آکادمی‌های نظامی تدریس خواهد شد
🔹
ماشاالله شمس‌الواعظین عضو شورای اطلاع رسانی دولت گفت: در جریان جنگ ۱۲ روزه علیه ایران، دشمنان گمان می‌کردند ساختار سیاسی ایران متکی به فرد است. با ترور رهبر انقلاب و حلقه اولیه فرماندهان در ساعت ۹:۲۰ صبح، انتظار داشتند تا ساعت ۱۱ صبح کشور کاملاً فرو بریزد.
🔹
برخلاف تصور دشمن، ایران تنها یک تا دو ساعت پس از ضربه اولیه، از جا برخاست و واکنشی ویرانگر علیه نیروهای مهاجم نشان داد. به گفته او، ایران مفهوم «روز دوم جنگ» را به «ساعت دوم جنگ» تبدیل کرد.
🔹
این تجربه که چگونه وحدت فرماندهی و انسجام نهادی در کوتاه‌ترین زمان پس از یک ضربه سنگین در ایران شکل گرفت، به‌زودی در دانشکده‌ها و آکادمی‌های نظامی جهان تدریس خواهد شد.
@Farspolitics
_link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/438224" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438223">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عبور ۲۵ کشتی از تنگهٔ هرمز با هماهنگی نیروی دریایی سپاه
🔹
نیروی دریایی سپاه: طی شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز  با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/438223" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlYpQKgH-CcmBwDqdQ7mrFyK_QSH8Ec-gCNxmSS5-nEDh97Yc2W9ktgx7OHBKPtoD6nHRKY7QE97FAyVaRiaDXVZXuBfPU77tfykWekJm-Kt_zKlO24kJzzjg0Eb3wRaFlmkDGgCkh06WeiplwGx0odYnaZ5kaKHQ1uxmPAFs5G56bMz8VEzS7Iw186ksW0mwZH-eE02RSTL78FKCNTjdPBJ4_6Kgw1It2UOZ4O06dTepD3dp06WzY-rmU8wHL1LKOcCMeudl8xPjS_BRF_4XdGRdkGKaxe6sBUCrmZX0nDhFI1j5kF4zIkDWksvQQ6NOH9BnBzObz5QlFPrRMHYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6uqhzWyDl-0RPDJGQPbg44JAe0mvIltVUvkXDiM_lHyC6pcibMvH43AyFYYmnwU580KwVADwqM4CgGDWseZlbuO5DJ1tq2MmwtG7phJc3FzW_o1LYgMvEw8bsZRsoeymqFSmwqhh6j1n-cpr9lgXhYHhAU7GV44HSXABf940-e2_x90NwO0S_KnVQZsHW6QN8h4GU79D-PSOQqtIN3MdfPBsspm68HycT7oGPS5E8L40g2smMVdC9uzAb9-RmSxgTeQnRG1IVLjd3hp5b5NAukli1dB8z8_0Z3NjU1X3dB0qOkFnVIFMNonRIo0DAzMBW2KCzoZ_FAIl1yGUJDo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAW_uTPZoyfSYx6d2-DgHp0m4xjXER29WCkSeJzVul-EKqSBlGGTBYXezeqo3ajJljseDca8lZqP3WrXi1Z0tLCAyXsV9EZgAc2IhdRNhlxEaBL3CSEjRIrfEDTnwMs4oXeCm3uoA2uS7wtWya-rWZJfDgUhus0WOZgA22JJKbHmM2_hcHKvifVQ4EcUt3JUHl_cVYPP4ZWZ8Vadcmsv3GPiOciyOATOnWCiQ9feSPZCE1BOast6EiaR8OXqtIz2Mna-R2sTgoIH_4XQzuOgWlP5kGFgUEtIokBSOmbQ9jb7Drshp4GmeUxxaHzXHc8qawI-4ag7qLTYwULAIX3wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhi72qsBeJ1JytNrs6dkni0qUhvEu3iQWTG4LyIvX23pK-VhPEPQtrDdZx64mm-t6-LyJbTT7UZvG-dblY5p0LaAyD-hH0R-hR2nXIir1wM7J_FHrCwwjfDukaj1OkiJ8mpLQhRZXsiI8c6d85Dh5CW4nZG12I5sOdFyDrAOeaEolHHjazY5SKV8f6J7fmmx-O3rsdx7cD6h6cl1YyLXm16CTYWxvh78-7C-XGdLIiajbd8r2c0aY_UiauOrwX-nx7dS6_mGlhZdjZx7gYWV7vtZFhCdBSZZXzq3rlGOWJrO1wvfuJIRyxI7Q_dPO5MfDsppt40Ob_JU92Jao0Dixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njumMbEF_OMulgCP89GqTxlC0NJ2987ydFfTOWSdn8xRh-QMu8JDDk45TGaNP8KhqO6zLbXGvWCTCxKZPYXxXgjk89nJ5EZ--0oXl4YA56RhZZ7UbIEE7FhpLU7M-rOhy6gx7nPMlFPHfeR-eXXjHkx5ujQcpSog0mIGL-bkHvlHO2CHC1JZDSS5XKSxn57P6n6x1Qivh_hW7baSdpLlKWNfYcduK-Gms9bdTrA9-cfnUp21xtkh78Cf_9VrSWwE6T-lhG_iN0j1mX-__RNrYFAlgeqs00QoFc70zGyGvuUbyTe53lTHRqXBvbglSaqmUGWN7e8NgMCt0FX5AaNcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFjz4j8tNAG_iYBWD2J4AitkSMinYswThxCPeztBL1CyHOr3BhtAFL54bSxCRAMBSXujhySVtGCPSq8I34ZQXmfGpD0W1yfvA9-046U68yJchGc5FEkfR8r2CV1fBmhFOf0w5R8QSATHJRSg46sQd9XinZf6T5qswTUz-c3PosNFJVXHVN6PXq5uh8CttJCL-9SepYGtF_gjB43LIrt-jkNWY1hqJRh_tzk34xxVzK6KHfJfZc4bi-IqsBmlToq8ZC3u_WA7YoqCY1_DPHE29lrtBdYozOiEs4qOZJ4R-jHdPHfzO9uBR43WkW7smmliKolX4SbY_0gdr3v5_-bgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ud3gu__bYfLmBIGCoU-obYX2gUWX9dC9AWEVIvGn0LHYM7UGu997zPQgoqygCT_tvME9led8ixJsK9BrWiqYiAElOL5zqcP_Y1s0GR7Qg4iGGJgg4EBPwgibH_AeiDhPRz7C4gPGJVUsdevK8BZ3a_wVTmp9SS9ylg6VLtbRviOiB5xSIcGiass7KgH7QOKSGikngKAneMqZs-7JJpgKywwFcI3wF4BgniBlhzXx7ZSZhPgV66_e3fqcwELK1V4OqeO8L6O8uLn9i0VBv4DfKj6ogW-Ci9wVmqJJxlznudiip7a-hCj6MivXhoLh_xmW-MorzwW3DgnJyv1-c4ZK6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم دعای عرفه در قزوین
عکس:
میثم‌ملکی
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/438216" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb40dc0aff.mp4?token=T_KzCiiYKj1v4EOWY6NNCcjlEU43zO79zqDDHNJOrRD5pWJYjjB1xAEPN98e63nEf3ImI9kzswVVrOrR5YPw8NyeWY3MBELDP4QaDeGdV9zPV6utAoqQDk17DfaA9ZAfUfu2AoFzKCgZxVPNJt4xsNfMX63hzXQ08JaYngili9zEGQcEt-xr0xPWK82M9pHtuWeb84E6UPZyFI9k6hQiqkNewaxJdHSKwGAWcAt9Rg-sqjJCGwjGnrgEFwIIXY1yKOCqi66h3n6kDKOEAH3MMmgd4516B0-9DNgeWmXSUjnUlci4OmH_FtkOkEHHFVgXdbRfIwS3th-poRlBXRZQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb40dc0aff.mp4?token=T_KzCiiYKj1v4EOWY6NNCcjlEU43zO79zqDDHNJOrRD5pWJYjjB1xAEPN98e63nEf3ImI9kzswVVrOrR5YPw8NyeWY3MBELDP4QaDeGdV9zPV6utAoqQDk17DfaA9ZAfUfu2AoFzKCgZxVPNJt4xsNfMX63hzXQ08JaYngili9zEGQcEt-xr0xPWK82M9pHtuWeb84E6UPZyFI9k6hQiqkNewaxJdHSKwGAWcAt9Rg-sqjJCGwjGnrgEFwIIXY1yKOCqi66h3n6kDKOEAH3MMmgd4516B0-9DNgeWmXSUjnUlci4OmH_FtkOkEHHFVgXdbRfIwS3th-poRlBXRZQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کشورهای منطقه فهمیده‌اند که اگر میزبان پایگاه‌های آمریکا باشند به‌شدت صدمه می‌بینند.
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/438215" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106bb1fc7c.mp4?token=Qodj7dkFNXkrwtDkatw5FjuL3mU0g2Z-lmH1PX-ojShOANzBYnKLKKee89jN7RJmw6bDRX4v1JQGFy-uOGMVt_jyG4cACb81bs_mctsBqaHD9Za5d4Wb-N5Y1_NHwl8rOWo0ea76m2WRc7kOqmboPQQxOjt-nT_KEf96L_VFAbX_S18_gP6Sq3vxcIQeNxhyoGw7DMk6777ihNrldUtQi6EnRh4XPZlDRBKJfqKiFFPguYPiNejwMongrpOwZCKy0aZm4Dguo29_7jNCDOHBcoGM7b1z8Iam4XJypWxchs_wN6yp3pnHj8aOBGA-f1GKiVl3fJeJnF9MB8-1UbGwPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106bb1fc7c.mp4?token=Qodj7dkFNXkrwtDkatw5FjuL3mU0g2Z-lmH1PX-ojShOANzBYnKLKKee89jN7RJmw6bDRX4v1JQGFy-uOGMVt_jyG4cACb81bs_mctsBqaHD9Za5d4Wb-N5Y1_NHwl8rOWo0ea76m2WRc7kOqmboPQQxOjt-nT_KEf96L_VFAbX_S18_gP6Sq3vxcIQeNxhyoGw7DMk6777ihNrldUtQi6EnRh4XPZlDRBKJfqKiFFPguYPiNejwMongrpOwZCKy0aZm4Dguo29_7jNCDOHBcoGM7b1z8Iam4XJypWxchs_wN6yp3pnHj8aOBGA-f1GKiVl3fJeJnF9MB8-1UbGwPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام کودکان مشهدی به ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/438214" target="_blank">📅 21:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438212">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-TxFWJcO7IRnANYV_LhKnunj-taoblveIHlsG_T4Aq-CqOyRP9CEav0B2n36nMysda5onchXtEruAThTNGOvokLtJQ5NkNuNN7yzWZlWsUWw00uihc4u36c6-uWmdkuMaOVuZubhcPc10hsP5-rsz9mqaTJIxRcEINkK3loebBSGrTmSWxcQ9oqMTfl-H1RgPdt5q_Jl2g-ywwtmdFs87LJHwd7htURvfQ0OBpFE8-ilJM8yTDPJi5oM-47265zcYpn-yErg7SudydGGA2oFI13ysfQLBZv_njpk2XCgcEj2EfZlnDPARj-J67m94AWFJFlBx9vP0yK_U8qGAIywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: در گفت‌وگو با رهبران ۸ کشور مسلمان اظهار امیدواری کردم که خداوند قلوب ما مسلمانان را به‌هم نزدیک‌تر کند و شاهد گسترش همکاری‌ها در همهٔ عرصه‌ها و حمایت همه‌جانبه از هم در مقابل تهدیدها باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/438212" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbac7ff3b2.mp4?token=eLS21nZ06JzRIh7uD6w9Kcrrd2aiq2WJNEVQ6CJWR9ooGXI8uJ9TObj8w6ElRE8LP2Y7SVXv0BBueFhOXmPJU2gNUv19ZImJjJ4BRTNcIjj3TUsufPek19qvb5MNjwIQrbT26HBk3fS61JTarc6cwhn-njC4dh9PQ9utStHAnRLuk9xir_RZCFfvvKCABGItcM1aOij1o7Osx6ZUx5IJium3Iks3tfVD3N3uB1H1ldNDxOEpQUXwXFpxElTgkYisxZUqojd4UwJdyrNFTWuBmSL5XlObaOh7svBD1sZhh8UqUgcIApcWkemkeDTr293CvW43177baUzaip2vt5EmUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbac7ff3b2.mp4?token=eLS21nZ06JzRIh7uD6w9Kcrrd2aiq2WJNEVQ6CJWR9ooGXI8uJ9TObj8w6ElRE8LP2Y7SVXv0BBueFhOXmPJU2gNUv19ZImJjJ4BRTNcIjj3TUsufPek19qvb5MNjwIQrbT26HBk3fS61JTarc6cwhn-njC4dh9PQ9utStHAnRLuk9xir_RZCFfvvKCABGItcM1aOij1o7Osx6ZUx5IJium3Iks3tfVD3N3uB1H1ldNDxOEpQUXwXFpxElTgkYisxZUqojd4UwJdyrNFTWuBmSL5XlObaOh7svBD1sZhh8UqUgcIApcWkemkeDTr293CvW43177baUzaip2vt5EmUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحقیر وزیر خارجهٔ ترامپ در هند
🔹
به گزارش اسپرینتر پرس، هیچ مقام دولتی هندی برای استقبال از مارکو روبیو در فرودگاه دهلی‌نو حاضر نبود و تنها فرمانده هواپیمای شخصی‌اش به پیشواز او آمد.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/438211" target="_blank">📅 21:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82dcfef5b1.mp4?token=aaEt6FRBOTTXnoYiPj1dEK32Lpa8lVYiC4AfmQiIHdCHymtmo6WnT2e_1wUZfL28Plkoh1tToL262sUqH7aJbVdl9nyeYR5plM-i1Tme1aXz5l--0tP7km-Z4H9Cf1Xn6eogbH8VLFnwf4wKT5pKJygLWHJ8MNAGjk-hO0O5TK7NAfDKTERsdDsR-FQx-1Lq758lJzt1L642JKWmDT2CwyH0eZh3BACcWihl-jPtuhdFRlavrOg-IqiN5BRKNhiapTbB7ck9C1dcEsTuXdkeNxIULB5SeGn-302FFDOr4jR6svNjlBVNsRQVYT3JySJQUcW_9cnH6qAYJuDLspYuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82dcfef5b1.mp4?token=aaEt6FRBOTTXnoYiPj1dEK32Lpa8lVYiC4AfmQiIHdCHymtmo6WnT2e_1wUZfL28Plkoh1tToL262sUqH7aJbVdl9nyeYR5plM-i1Tme1aXz5l--0tP7km-Z4H9Cf1Xn6eogbH8VLFnwf4wKT5pKJygLWHJ8MNAGjk-hO0O5TK7NAfDKTERsdDsR-FQx-1Lq758lJzt1L642JKWmDT2CwyH0eZh3BACcWihl-jPtuhdFRlavrOg-IqiN5BRKNhiapTbB7ck9C1dcEsTuXdkeNxIULB5SeGn-302FFDOr4jR6svNjlBVNsRQVYT3JySJQUcW_9cnH6qAYJuDLspYuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار یک خودرو در حیفا
🔹
منابع عبری از آتش‌‌گرفتن و انفجار یک خودرو در منطقهٔ «اور عقیبا» در حیفا خبر می‌دهند. یک جسد از درون خودرو کشف شده و هویت او هنوز معلوم نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/438210" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438209">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8fb760f2.mp4?token=r8lsCjqqG6JsgPexcT5juY0F_0euhNw4UW6iAFPJW-i60Q2WMR_EFBCrGQZ1Rgt4lBNmWXJWGVDI122fzTNC_DbUEF_urAOa-Ig4U_NvrftODWn9CMGMyPEafwPeYzmCrj-9c7hgmluHaYItxJcP8jsbaMzl3JTxWM1jae4_1YULg6kWYAtbm0WLTWH3sgU_Wupq8Tt1v0exNGLJhvdY35qqYt8Kj5UYGyFJsW0akSXbItBx48wEHhFQBov2CMo02akEBlvQHZUYUlLQBtCPwO1fUwx_74Lu6VPjQ7QbQQ44m92R35gOx52H365cUDYl-zu1PWQeJgTg0kB3MzrwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8fb760f2.mp4?token=r8lsCjqqG6JsgPexcT5juY0F_0euhNw4UW6iAFPJW-i60Q2WMR_EFBCrGQZ1Rgt4lBNmWXJWGVDI122fzTNC_DbUEF_urAOa-Ig4U_NvrftODWn9CMGMyPEafwPeYzmCrj-9c7hgmluHaYItxJcP8jsbaMzl3JTxWM1jae4_1YULg6kWYAtbm0WLTWH3sgU_Wupq8Tt1v0exNGLJhvdY35qqYt8Kj5UYGyFJsW0akSXbItBx48wEHhFQBov2CMo02akEBlvQHZUYUlLQBtCPwO1fUwx_74Lu6VPjQ7QbQQ44m92R35gOx52H365cUDYl-zu1PWQeJgTg0kB3MzrwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور و انرژی پرواز همای هنگام خواندن سرود تیم ملی  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/438209" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438208">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cb27fb52.mp4?token=P_-mYjpCkr-vX1rW7lQFCXvITsYo3Xu7i7HNkNwXjK3fDkRPazO-U2YB6FjYmQ_hZv3tvhWSMhrT5boartKwQVMI1k89wuAZjdHzDe2UnhQUfkNBgnLLfGsT_XK3wSxvaElhRtBxdJTpUK8u8m1s87pW-Mqy1DCYuCpMYuIICCRp1ZLkVMqN-y8BylA_LZBDQlgttlyURrVW4YpmN0zRK4zjmPnM4B9ClodOmdbG3KSU6c9oK3pyzEi0YckCYstVbHBOOekefAztu0CCOMc46y-ZyV3PXyYkh1iSFWq_RdWB4doN70KNYYkPSRcNhjGrRF7fO469hPbR7ajp5izkxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cb27fb52.mp4?token=P_-mYjpCkr-vX1rW7lQFCXvITsYo3Xu7i7HNkNwXjK3fDkRPazO-U2YB6FjYmQ_hZv3tvhWSMhrT5boartKwQVMI1k89wuAZjdHzDe2UnhQUfkNBgnLLfGsT_XK3wSxvaElhRtBxdJTpUK8u8m1s87pW-Mqy1DCYuCpMYuIICCRp1ZLkVMqN-y8BylA_LZBDQlgttlyURrVW4YpmN0zRK4zjmPnM4B9ClodOmdbG3KSU6c9oK3pyzEi0YckCYstVbHBOOekefAztu0CCOMc46y-ZyV3PXyYkh1iSFWq_RdWB4doN70KNYYkPSRcNhjGrRF7fO469hPbR7ajp5izkxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «الله‌اکبر» در سراسر کشور طنین‌انداز شد  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/438208" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438207">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4f157c5f.mp4?token=J4u0t1hJMJDRfJwtp6E5_Wvg8tICfDyqZeIZunYka-_47H-iZU6brSysLeakwL9AlNC-BIDQTLhw5RfDvyAKaeEoEvWJKMVhFC2JoZ3vz7KSCyK-SL5_K1b_d-uo0Lh1Msru4M_eoq_CSjeE3ghmRm8Sl-aU4vHQhacWZamnhWaHFnd4Gu4Xhe0aI0r649kiKFi25n6YD3VLolnV9c8ap2o9sJb-qPjhFHGFXDhn6Iw0-tnO5soPbnN--fhdaaS__H0Fjq-xUWWZbpDfnpjBDPW_wxFOUAW0hccBMl6I8Jw19KPXWZXtsDeya8kmmHXK_QyoHJmVIlz-uwK4K3_WdbhYTrmDyGRC3q5NTHSUHRJcUe-tIFz0yNo3UTZuRIeBsNHD9M8MUDQDZH2la53K2F3O_DtP2QqZ2xrZVX_K9YvhxL1EggoGQ-W762nO5d14ICP8hdTmHkgoRLLMFqUegtNRe2D065GYod1tYhlxWJ-lhd0CoU91al-WGeTdQJe8aiZ3lqhZJqGIGkgtS8D3lPR03r5vC0_3D0H9Cb4kufVr2eEOUj6Mvq-gMZ3W90rFjtsKwBTFLZ6WQ--pjMX2uYqKRsiIjfSZ5OI8OPhPsbPGwa6jvPpB8dwqBzno4GZBA9piJzec2jUZiUjOBnShgxpf8Q2ytyJU5a9DC6vPNUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4f157c5f.mp4?token=J4u0t1hJMJDRfJwtp6E5_Wvg8tICfDyqZeIZunYka-_47H-iZU6brSysLeakwL9AlNC-BIDQTLhw5RfDvyAKaeEoEvWJKMVhFC2JoZ3vz7KSCyK-SL5_K1b_d-uo0Lh1Msru4M_eoq_CSjeE3ghmRm8Sl-aU4vHQhacWZamnhWaHFnd4Gu4Xhe0aI0r649kiKFi25n6YD3VLolnV9c8ap2o9sJb-qPjhFHGFXDhn6Iw0-tnO5soPbnN--fhdaaS__H0Fjq-xUWWZbpDfnpjBDPW_wxFOUAW0hccBMl6I8Jw19KPXWZXtsDeya8kmmHXK_QyoHJmVIlz-uwK4K3_WdbhYTrmDyGRC3q5NTHSUHRJcUe-tIFz0yNo3UTZuRIeBsNHD9M8MUDQDZH2la53K2F3O_DtP2QqZ2xrZVX_K9YvhxL1EggoGQ-W762nO5d14ICP8hdTmHkgoRLLMFqUegtNRe2D065GYod1tYhlxWJ-lhd0CoU91al-WGeTdQJe8aiZ3lqhZJqGIGkgtS8D3lPR03r5vC0_3D0H9Cb4kufVr2eEOUj6Mvq-gMZ3W90rFjtsKwBTFLZ6WQ--pjMX2uYqKRsiIjfSZ5OI8OPhPsbPGwa6jvPpB8dwqBzno4GZBA9piJzec2jUZiUjOBnShgxpf8Q2ytyJU5a9DC6vPNUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاتزا: به ایران آمدم چون باید خودم بازیکنان را بررسی و انتخاب می‌کردم، حتی اگر اوضاع آرام نمی‌بود
@Sportfars</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/438207" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438206">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591aad3eb7.mp4?token=U4obzty0PveT4fI8hX5XGVV5Ix7WmZ4zBMR3VSJzvtEdVBexc7AJus8SABDlMXUsD0wnmQ8T8M2J-5uTeExocdfTdHVg8_-4vkf_YcETPCdBpODMGU23ARl_7O-6tpRfrR1PxpugKY_ICib9go1_a7UqNwI1xyEnsbSM1ZYgVG93BXbXelrIKH3nMKY0V9gOZglmzj9mip7-8ZcvUPW5tsyUqjc-KGK0bjfZWVlQjC71N9Lb5VPaxGp15EAQbMZpKtwLPaaDpbiIm4X2fix9ksYvjcW-ZAJNUyYtZadwpZpkUGAwe3S8Q5EkVIOy2mr1gqq242DYi-bPCfv9JjyGAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591aad3eb7.mp4?token=U4obzty0PveT4fI8hX5XGVV5Ix7WmZ4zBMR3VSJzvtEdVBexc7AJus8SABDlMXUsD0wnmQ8T8M2J-5uTeExocdfTdHVg8_-4vkf_YcETPCdBpODMGU23ARl_7O-6tpRfrR1PxpugKY_ICib9go1_a7UqNwI1xyEnsbSM1ZYgVG93BXbXelrIKH3nMKY0V9gOZglmzj9mip7-8ZcvUPW5tsyUqjc-KGK0bjfZWVlQjC71N9Lb5VPaxGp15EAQbMZpKtwLPaaDpbiIm4X2fix9ksYvjcW-ZAJNUyYtZadwpZpkUGAwe3S8Q5EkVIOy2mr1gqq242DYi-bPCfv9JjyGAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراخوان سراسری برای ندای «الله‌اکبر» امشب ساعت ۲۱ در سراسر کشور
🔹
درپی انتشار پیام رهبر انقلاب اسلامی به مناسبت حج، مردم ایران عزیز امشب رأس ساعت ۲۱ با حضور در پشت‌بام‌ها، میادین و خیابان‌ها، ندای «الله‌اکبر» سر دهند.
🔹
این فراخوان در راستای اعلام وحدت ملی،…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/438206" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy6_vx-QMfmRwaMZBS_rpw9Ajg113EMx46OguDDNHjGbtVoAfV__e65864jaSW5iA2d97vBPQt-R2O2KK-eMSZCEEUg9bbr9f1s3aWEUI7P6xJ3Mv3g3Uuk2PhAVSGMbdy55nT92D1aaV-bxGSyoScYEHPcdW4cclTkM70CgZAC1wGcSMQdtWQrmH11ImuHJUqrFL_8qk_zVbwbGUxgxrppTMrXNlHbpqfCD8ERrRGzvxl1kMiJ7fhA9lgzgPxJrR_aTM--za3qJuG1mfwNk-LDlbGTaXN71DEFuvrEJmhsbd2EbToVValP2SeG8yuiY4EFHpe5LXmhv_GnQGywkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927e05c410.mp4?token=nNhOUHz6dcVoYnB4uTfLobajsHy18tLP0B8A56iJMslJUCcy49Jrs7KkUAlgZmDz67NtReWV7AU4x4hRHW9tPxjBKRlbTB26hlSLY59n_FF5BYkm92UXJs7UdLR6Zs-J0bPQdNW1iMDMBVIksCnoTx-NAdtPxHXy3DnRheQV5_UFmBp-UmiHk2G_vOGfQgAhqqk7pgXDtYLSQ5Pbu7wFpAMxLiwW6-YnukmLYtU1Q-gmOLsVHiw_trILE5WPFI7ZRpnL23T4sQC-JNAYxagrZUbv1u8Bf8CS4j6E2-xks415bTOZDCCnzw1HTrXHaiAStY1xtq7-U4vCrLf2k66wSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927e05c410.mp4?token=nNhOUHz6dcVoYnB4uTfLobajsHy18tLP0B8A56iJMslJUCcy49Jrs7KkUAlgZmDz67NtReWV7AU4x4hRHW9tPxjBKRlbTB26hlSLY59n_FF5BYkm92UXJs7UdLR6Zs-J0bPQdNW1iMDMBVIksCnoTx-NAdtPxHXy3DnRheQV5_UFmBp-UmiHk2G_vOGfQgAhqqk7pgXDtYLSQ5Pbu7wFpAMxLiwW6-YnukmLYtU1Q-gmOLsVHiw_trILE5WPFI7ZRpnL23T4sQC-JNAYxagrZUbv1u8Bf8CS4j6E2-xks415bTOZDCCnzw1HTrXHaiAStY1xtq7-U4vCrLf2k66wSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
شکوه دعای عرفهٔ امروز در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/438203" target="_blank">📅 21:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8S8IKIG5DfpkslAJnpjEuCFCQVZ1O3OboXAYg5Kl3UrPSAJ_gD0zC70r8s5qVejutSEvhCB64765RztRqptYvZUFSCdFID2OviS2Xko4cH181GbuEMHQJEuZttb7FRl7asoXjETLMs5MDqb1t9KHKUNpRIZrZMFuU_jfaAo8bvKhR3jF2fdvYCcDKgcXBVIRJLONoNMB9QPqIgztqFxuN9F_6U1RA_yVdxu2uFoCxml44EUsx6LuxHTO5d0CMUporVS1ovj68NsVqqZ0eesGjDAIXQ2ZftUlCgp5_hYMSIv8vmPc5HZzhQi7uW-7NTN_wM5K6osO8zCpXlUvK3bOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو دستور گسترش تجاوز در لبنان را صادر کرد
🔹
بنیامین نتانیاهو نخست‌وزیر رژیم صهیونیستی امروز سه‌شنبه در  نشست کابینه سیاسی و امنیتی این رژیم گفت که دستور گسترش عملیات در لبنان را صادر کرده است.
🔹
نتانیاهو در این خصوص گفت: «با دستورات من و وزیر دفاع (جنگ) و با هماهنگی رئیس ستاد کل ارتش، در حال گسترش عملیات خود در لبنان هستیم».
🔹
وی با بیان اینکه ارتش اسرائیل با نیروهای گسترده‌ای در حال انجام عملیات زمینی است،‌ مدعی شد که نظامیان رژیم، برخی مناطق را در جنوب لبنان اشغال کرده‌اند.
🔹
نخست‌وزیر اسرائیل در توجیه این تجاوزات که نقض آشکار توافق آتش‌بس است، ادعا کرد:«ما برای تقویت منطقه امنیتی در لبنان و همچنین محافظت از مناطق شمالی تلاش می‌کنیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/438202" target="_blank">📅 20:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnQMEpT0Emh06m4Y9kI-0XKtCcXvV72CUTfFF4nKMznagOy2-FhQgrmjgLUgB4in8H8yMw-7XvBKj-EhOJRxDUrRiLhhHZVjsvYvl6woYmCFbvONIIJcX9syhD6h_KhVyxdPQQPhVGyRwgMsKW-7zBOzT_N7CTA2gwz3AYf8H0ji4hRsNCuuwxB7tBWwC0qNa12wYOFd5GK3-DrPu7IFKtSuzGQHeYwOvrp_GRshvaJtjN5d_pJEGA32WKQK2aRY8k0zKHx02OOMfTMRiWQZ1Dk-SFXeXg3KtNjo7JWGifbZAR-6EPEfPuPGeJgsR2LVfAJWfZ3guQ4fBtN_Diwemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تبریک رئیس‌جمهور به مناسبت فرارسیدن عید سعید قربان
🔹
پزشکیان: عید قربان پیام رسای کرامت، آزادگی و نهراسیدن از فرعون‌های زمانه است.
🔹
امروز آموزه حیاتی این عید برای ملت بزرگ ایران معنای عینی یافته است.
🔹
امت اسلامی می‌داند گشوده شدن دروازه‌های نصرت الهی در گرو وفاق و ایستادگی در برابر کفر و بی‌عدالتی است.
🔹
ایران اسلامی دست برادری به سوی کشورهای اسلامی دراز کرده و همزمان در صیانت از خاک و اقتدار ملی خود ذره‌ای تردید ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/438201" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438194">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vg2ckWuZH9uEi_7P0W2HwOwdlU1bhQpp4ZQNOyR0o0R7pHuEczcbLTXAbKYBVN4JbIwV-JzOuNL2OnDgbFQH6Lxm6XLg1gVIifIIfQheDZav5n8lVXzTB0aoGBvBp68uVx2YVY_nlwiBf_hqa9XeFZL4nWuf1g_AKVA8Q1R1it9uQccTprbyH_jbtUaqZGZg3kI9NlsEL6iJ8jtDYnxg2ZC4_VHY3KCDr_QHI2thWBtQsJzBF14NkelHgBYudHR76OhQieuZP2msmpuIq8gxrzQ37fdatcReZNY9wXUxzibTAjutDxeIPeyIaT016kVmHanhutuUQx_dJ8jk3UplmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m--t79NgT9_iem_nN0Zuu-zXZhMoIVqErF9dIdSyev8jfBuuGnBx_lIDruDcoZT-VDSWfHem4og_LpAB27JdslX5smvWDznxotuP1KXqlo7MNYmS_6pAS8wDUDkNazZlO2_XQnUiCwq_Pwq2nmFAP5WCyekM_qo02s1myXHmA2NONkY2wf3FgaESZh7fkGqXY7kRNmRz8opDG10GVNoRV4fQdP0j93Ca4R7ic-VC4vsQuRXfDMPCfhQJ_zLguKASZF8hcw4qAxTWT9Q-g41tJOXxNiuwAoALH_jLN0TXb6oyoSEpBOsscDnp-8SM5sFU5Lvwj4085B4DZBD30MNxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR8b5zSUTKx9jnZVFno48SoDqDh9vc5V5ou1smtjeauAvngAO0JrFGLMIzk5bYrkkAx2xML8odBn3BL0RYqi2lRrVUsLCCtNy-oujcNsIfMpV2th0x7nnZnz3q5cQ0JBPtUpjhFwWeoPhmfEH2qLMUjLzSYfGvkRhXLVWVsULYailRiynYeeNFa1MFjqOkJgALw_ltnY6NS0yJFjp25p2G1TW6DDeuCQZYcPzPd0_q8zswLpEQeH4PqbwDk3GmXNbO8lrno3IoFsIkFpqG3Lgo6ViwMI1_c2Zm9CVFkjBeesFTJV8AK9huMS6_aRQOMZy3wYcwCAMniGu7rjsDWbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtNnbD-LNPKlWs6FNr12Mv3He8cET-R8A_dZ8F6OaeQ1hHrz038ZE9Gpeymn0wWPQ0qIjByLcQBcFdOhVi0r2yW6SWB_8RVg1JrLRgVnH3Nvun5pSuz7VJwF-7leghQU-rRMOn2AI6HLfQpoUl0M0OrWxUsUQHjBw_ruL2v3EZx8BrQfv1EIcCAeM7AVhLSe0ROu1yeDLx46jRjlOSxXAVBZSIipSbvrvpYu2YDuH8PKqkNp87ZdtSdawEoBT7XgAR-2TGQ60EgKVaqhqw1e7J9QMbCOo3ekdgmteu1uZMndRokZ3CwZdY-LiMBOflZ2v7AIr6P19IV-r68OA4oSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2JFq22rlKYAuxGVVHDIEskh440Ij4KC5AVdRtcV6dTShpYWVf7Xp9FKG6wd2bCBmh92j-RUHTXK_F6xW5WVUVs2VEZivCMV1vAxR27ZvQxw44OsHmjqc3BE6Aai5xGuEPsc-POk0hADdVmi6hOuLLxHE2SbZLc-3s20ZTvmrl5U3YgGn6gKIVjeLsRPZRc5RtZnsm2_ydlDC1ngR3HBZxCzDAMXtTkaEjWBvh1BimxNUHc-vdchvEGeeOaTt8fPRadRCjVGpYJW0qKTbjmH4H5w7x16IfoeL3ckimHkgtHDjG1hAkw3frlCihwhKjS2iTqSxOTescSLy0xTDy-R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mthlc15izUt5cCs0Ff34sKIb8Y3mY6KRRQgBpnCXj3jFA3fFIcMPOSE0pki3QPSr-B3AS0I59qFoMlY4KjnBWtB8t-tBqjYnGbwESylLLzBr0-BT4yR086Tk-T6xe78yw3R8g5KNwOA9vgpBfcBlRAxUdSfWvgbU4ugjTQg_l551S-5IrQbhWdv2aXlPxWlRhh6R0gcaCQcZGRW5lwAhVKoPnT5CTURaXudl0dYCr5Wyheq163yu6gzEqDpzFjH4V-hudJMw3G2CUUsIUyFIJKbtAcAwk6-cYP4Gv_Pe0o3xI1lheGrWHlqXdkehBPAG-jT-YBZDqjLZQf8nsm7HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egn0FLVpUw5OAeahsknwqypUJewNzmmvKMQhnvYQ0xXwni_K9WUWJDzgRjI4fIehBMZCUew2JUP_q_n74INy3yrn2ryDkEOX8dD5c0GdKEHmDQI6aHHNpB_2N69At2EIAjEKVhDS70pz_0ZWsHLc0NNs-jtpOrcQixriYgjritscc_xfWjGVrKUYEgVBPd6C0RVSNeCAFpnKzt3iIrldFoR5aSPd0mzTW5wulABEuVfJhOCrisxXVyKPeZ8nHpdp-tA-5qyMW_WFmW0tou0H3_TC1xI1WcCk0PW0lVDwVqXpiRR8OtDIP-C1Axp1rgsx6GXHSR6EWezs0WFtJqBHXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ٔ
📷
برگزاری آیین دعای عرفه در حسینیهٔ اعظم زنجان
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/438194" target="_blank">📅 20:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438192">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivlGGoADGt1s21OhzqALFla7-yAqrt99ruRvmv3WUUanCwxvQCFhs2ngBJcrqqt9UGib-uHtZO77VNYEFmQhERA8rM156CvLJh330cadIfEK0T94nEGHD3-KWathaVXA4fFE2vTrJk-pu0SyNp4Pi6eXWkik9hQ9fyrmw3NsZ7vrA68WajAdWV0c5sgJj_Tq83ZiCiaNkJPevNaidcIgmKsUgALBLtaPLMVKtm6pbG5FPWw6N338UUvRFbNC8A-jIyYjhWi1-bUrJUjCt41mQvLvWEi4vbPL5gIey9I9-0EMeFnsqvwIWVqG7BKb1v2TwCvBu2zTHsB_vXE2r7T8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷ و ۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/438192" target="_blank">📅 20:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roZ8rqFDJ5POtzVHsjMUzAMY8DxB2gJ7Ds7TgDmGt-j8QX7xth46db8k906_xNbZSLcuqtIImVJT9fGEF7t1ZNzzwGfCi4CsYM7hnrDtx7O-Ey0LdNdzA61QIMCeFLX73zxbLWC3XpGAvoN1aFhzxk-Mc1GDPHRWFXviZ5jKdXjPXUB9pvRGkgvljp0NOPE2k8QCJH0JbC3IRFfoaFiXA4AblGUIxgN63M_bZXqGTeX306LRKzzTkGrLduXGtM0zVTi6LINRSHqokX_0aKYbuWBW_IFXVDh_U-ieyaXZsLuO8bZ0ThksjPNHL5kH4ZdJmaCXnh0DxH926xVH-3tNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERfAY0SHsQ8vdEyNCBbuBa2jMa8K4XnsuCO0Nq8bjBwatP_flr90206IdPouO5hmJ6Ly3UxIe9_DlB746miZ1EFDdgPbUaqmkoMbHR50pq5ixnNVOAAHmXY-IyGl2CIi-j66pd_Dhfh8PD9s7r_2NUJ0vFsHP6wOiGmiEmesewTZerAae6mmY5Qd_HFFEtlCgvkoAKjKdBskZ-S2GmtzWw9hqNQ5Y-roeQuUkvV0i31zZB9vOcNzbtUDy2vbXrfTAKJyioQooXK7eB0FO0ZPKYZmRwhoCvK6KPn3P-6yTRJa9YCRyEoaSKRDfahj6kdlZI-7SvpQH9Yp4SecHTbiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYqPS5zruZuIsFvdkHl3PL20v5o6YQPsY42XJoaWf93pfU74lACfAm28ntVpI9kKhGDNrMQGsL5UXv-gPxrG_5IV1cVIP8dU3pLOJtLBHR2gyUGny_2YkYXUsYiwUzL47WZxtSs4c_Oefgw5lZswrh0F_FM-xtfax9LF8AtMO4Jklkp685T8GCUmPo9WRW250HZ-N8oVEcJhUD2Img1oxmOj2mvsx5EZtPSZzAeCQtHCg74Xj6EEl0tvYnGx9orLFbo_8VUIbpqDy74FBZy8pMCiIqizvqtEvtqLEFwFxo0HDu-lSPFXALTrlNBXDLoeGvqXrGC3QBwxW4Ah4IW3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbyWNVkhuJjeXXGsx4oH5hxNBFyZHn3-JDdsklRKhrJxnUF7UW8k5A5RvgY21frZ2q_x9UIHF2r5dC2JIsYeo8yp0rlcuhNSUlwpyaeNT0gz3iQr3hav4KfxMa7g4R1ApM4ID-cnnWVWYP6qvYBxIo0A0fnzXKEyuYdxigYDoDhIxHh9vLt3DbtIoligGB9p29KWWTLVo4xwRirtfIo2kNiE25eRBomWxF7r8KQnDLyZs414vqCSpy2zmeNZ-Tc8kdxUFyZNKf7GP5qs8uDaeoA5_rn2FCU0lu9kfw3Dx6qs6NJey-aY1Ea-ViJ0CZhZMNtYxSiX3LCuMdUC8_ppVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO7jCyS9l_oFT9z-mqSmfhLOOm2ZFLql1xCy--qIuorW5xeSUKVDZZSXF9s_9afkhRiBDUDassi6t3Tq_QGDBrynL1TF5OKe0Aq4xQoS38bPtQGw6pFU_zGwED63Cst5JjnV9yYut6MnjlbhRciWlwfpvSlUjTAvg4ohyrAzXuwc-V3mtnymePtYwfAAhxbrNNY_lg0ErTHs42WvepLUNJvP7UlNJ4iv1KSX-WqAo8sWYroPPjAUn6g4AUbWnb-0h2C5BmAwus3HhYgD8NuDcSAoP6WKVyWV99UqhAi42Liakp2Qr36BejpzySqR3ogYT9K88zxSobuiuvYyX4g9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plRnzkXBJucPNbtRVzPLFqQCzHl3AtjhMQy43GQWpZk5q8sE9qz7CI5ZkI8Lm6FSEEBgOVm6T9g65J69sJRFyQA-XQraJRGg1JKMR0JweXCq8PHFTN8ah07b6SDBhs66nGawZjFwwHPwC4NNl1hqPM0m5a1bG7xLRA9IkKvCTgdSUD1bZRTxKnDwgMGCh8dmyVh15blemI1S7q4lNxWDUOCIkMlwW3SxeWo9yFa7xcHSUxVf8_MpFzqHEaerQjp0yd_mb3gTyZ04n9CmsgBhSC1qA-dvWJJnUUwrpMkYw2kjg8Kis4yXKWJ1mxcfho3NkviMtwMvYwZBrQs0yvjJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knEbUYNPAtHXKg2icWMWJn1p5D3LqQqvS9V_0Jt7mI_oT2tXqGrmpAV2ANxTV4wzwl1OLrgsXcJKOCXNWvHpJ_fOJe-Q0Rbaal38rBhN0HyO7y3DTE_IIbE_HHSTImNfFKw_rJzmxSohhoUajpSta5fs69tNVZzixZUAN2_4TCndQ8CgT9ezk5w5XcjaG5prLMfjwwwRA-NkJS2wu-IcF56Z7zjMWhdKUE1mDUUl_sEyH-fzS1o6ODXuwZv29i-FxF23Llo93Gcs7xd7o591YGhyuO8zblqm1FGehBVhiglvKny6Jm7J_wz_Ocj0OGzwiCzuobxnEIVW5-doyXEeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUSXBQf-IEs54i-Of8Ig3pIY0qw9VPGlJskuXZ7IuMN6cmju3FPafQ6YL_qGce139LTLtUCcVxD7B296Jtg_wYBe_s91bKG0aRX9jx0kkJTHsuTkQv-IfQNPHf8anIAy8ejfNbeAYDmb5mQwceIPP4laPkrKQxZdKftcX67DH_JfFnk2enjQTy0kAZCjorhpSWzKzFwm-zbsgBXxAW_ldEk_HJgTbuChLtIXOzCP0m21ux4HvvScLLk6iNgcfu-kT_2Ff9GIsMc9dVontXHy2uy4IcrDp6pd1fGUe1P1JJXt39zi2BIBIW8Q5mvPuoSYHjWkfdgouYnoFgEsLlYH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNi8Rre_v66ExIdNGcMkM0Yj6CWy6EjWbUzHYzpu7tkXKvTzhZNzygRE6hQvpY1jBmEHCfUnsLotiKl0JF6gANIuWuO0wAbnUOZ-PROHoezMap4j4-YO-kjAngA-i4TgEdFwauQiKAycJ-PrTjH28yASDY7IqjOuCMq1vxvqw7UbjE8ZSx-Nboz2IijNJ9s0BEiJGMyjeBFiaBI88S_5NVlB3pXKzXr26nffDdQFwAd6wsbCkElWWQQPifpXgAAeYSpQjXvdBUV4A-X7t9dKiexlS19IZ1UQdzN40lem78u7wv10woALdQfoqz8fP0iHzbTOGB9BYOXJDjI4RdVBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsPGray3mNSfsOpNhY6t9bexBkwVTEr4ygOnodikhlhV2YOu14yzX0_Q-oq-RydlBzwPDTYv2ByySPiDaamuWj4aZZSmzbf30NK8IOgmxul8O1G-4EDRGsXRt4OpyLGkAvwY_3zc7B3zqIllROV-zfq9xJb5g6xsacNODQ-8k5lzyCDy05EEENeNGGJ9OEjTr5gXS8Ti0AxSLrqp7TNBlJfxNgO4kay7dOVVqfA_F1sLyG2-syCsiRGKa1WONoSOLaRpS1t3jMtDSWt2pAXVXRBFY-5zsnFyir_x2KFiTjKv6ol6W16qV1pOxs6Do9PaU0yF9Xce6Hk-F718PZVEYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طنین دعای عرفه در قلب قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/438182" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIrv9MeFElZTy2DJRkAxWORBvsnLIwgh5vafV-rUfIPayChz8yz7mij-mzrHFotZBGvYVgv8KiBSLYn2yjYKTMrVivHkobOg9ZoniGB1VEoyYVv5X2LMC2oDYmK18Wwfrz3MnkDc_Sq-TyNeT2HXgUQ6SQC1aniuCDkQBIsxK00WapG7i83OmDxDNGoYznwNdB5f93oD8S1ey3cUOLbsjP3NBut0ykk78P_6I2Y8AEpNzsJeB2KU7t5yCSsh-OTFMEp8Zy4Stps3p-2SBlFQ2s6jdCE96mdMYLQaMZ1cIcwm0y3MROqVhqOIGiXJjegNn5epdePmRIjeFsfFXI0Iuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای از سرگیری برنامه شکست‌خورده «پروژه آزادی» در تنگه هرمز
🔹
روزنامه وال‌استریت‌ژورنال مدعی شده نیروی دریایی آمریکا در اقدامی تازه، عملیات اسکورت و پشتیبانی عبور کشتی‌های تجاری از تنگه هرمز را از سر گرفته است.
🔹
این عملیات احیای برنامه موسوم به «پروژه آزادی»…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/438181" target="_blank">📅 20:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5cd22859.mp4?token=TDhjURqDVf0xxz9Qe9wbnhjCjuCwxmQKvQUd5N1zy89Y60EFSpIf3b5y6Y-pf7iRMH1HPK4GWH9KJnDtqYIqRIpWWszbwQhKuZOr06_YEElG6bH4CsOOH3tspts_Q6GayR8NVLDJug5e2jhfB79pmFZk_Y8IVpQzA52adF7TS8jspIUnn_2PAbBwkMcgGN3cXFw043njgyLFp9y5igJ5i3djW7TsO-pSr7T0GPHpFS4VVnAHp2yrSokHmpookVvpQkyOkhWgBdmhsnPM3DeVssxCEk8_rhodxBNhgLPJHPqNunRVxSIBXhxRleT3F2OfYXHzwSlzwylBOUorPYgO6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5cd22859.mp4?token=TDhjURqDVf0xxz9Qe9wbnhjCjuCwxmQKvQUd5N1zy89Y60EFSpIf3b5y6Y-pf7iRMH1HPK4GWH9KJnDtqYIqRIpWWszbwQhKuZOr06_YEElG6bH4CsOOH3tspts_Q6GayR8NVLDJug5e2jhfB79pmFZk_Y8IVpQzA52adF7TS8jspIUnn_2PAbBwkMcgGN3cXFw043njgyLFp9y5igJ5i3djW7TsO-pSr7T0GPHpFS4VVnAHp2yrSokHmpookVvpQkyOkhWgBdmhsnPM3DeVssxCEk8_rhodxBNhgLPJHPqNunRVxSIBXhxRleT3F2OfYXHzwSlzwylBOUorPYgO6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ ملخ‌های کوهان‌دار به تاغ‌زارهای زوارهٔ اصفهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/438180" target="_blank">📅 20:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
حال‌وهوای بزرگترین میدان دام شمال‌غرب کشور در آستانهٔ عید قربان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/438179" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKTzdaU2RSWo3O6XEGaQdCF1S7jhO_OGrs2DuYioSXcMrl_74ns0GFyV8QgKPsEVwyMBz44N6bTdpiCmYEtfb9rvPOBMbnasnNJ73YLbaMn-pdrMjbPxG4IDWTjLuTXzdZk_SX6NkGkpSy8iwhmLGkuiT4e3Zg7z6d51lVn7toPitZoIeUhIG41o9YGrqRQ68EE9i6TWTUB3e8UwiIEdno0rxHxAQT7hRuyU4qy5i0olLomts_I3PJhyFsH-TGFr5tH0WCbJevmnram8-zsR0wJabD_JAtrYFKdPoSzryJEndviWStFEDMZUqirSnEE2Bpq3WZ2-RZei4OE-GSxsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvJkGJpY2Rz_DLdFYECECyd95eqq6mipt3U8BVZ8NMdKqDPJG4ePWBbpgZM6qV4ya_RyqBD3A9PR7fF9y-mFzfsSqxV7_uyzn3J4udfVbg3i3KaRFCdRfkm_IBAUVeIxgjCHPJL-VLv8crWML6yvs68-PuxyL2F-gNK1jn4VBRjqQRpr0z1RjH3gpVLyuRtwcnq0f21wMH9e4JIGcBTrUZrJI8RHLtB_SreA7HUjuu0MAtmTmIXCacurH7u8JF7mvBYvt5B_S7ulekrWRRycciITlswDjCvfwARp6tNvlLnLufy3mnWf1yiaH4b-7i9yo4kp0iYFv6c2RR_3NW3c3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKYX9YlNFq8wMs_UyQ8YzeQJ3Azm8JJH_j770LbIXKLEqnfidWVTJ-Hy5VXNV036075x2NbSaS9kB5-zOvIUi_N5GpnXPKDgZJ2MxYaRKqgtqWhxmf0NZYHNe3PuMybTaVfTxNSnPEXCMZw74wmoWsVMqL6rrYaqKGbxMPCk7QRxHunyLJ7I21rvf13p6Gx-jhf2noLwB1wHEQCN3AmA2AM9PYxtSSBrzACK-Sy9X_hJeRCl7qJ1CVcx1VIiR5iH_jxLOf6xpTApn2B5ybrC-dKorgs1J1sgRVBREknj3XH4KPYuL5SbMq1JIfX9JX0eHNCpsjYi28LNWbj55k8euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mku5SKJ5bAXybsSXogLDqCJA4ptIsyDzo1ta0-U9AcruV5PE8TFmzdErJzRaaWm_6c_9FGnFDoJuuzMB4dVGX7350FBDcLr-xKn1dgqFeVxQv0_Fs8XPcmarJadwM1Xd_NtWWsFdSDGJmdvgwsMFkPeNtn9Wq0wukaUEF7QrFQBLYjLKjofFQsUll3RriS40pdf0DpQguWYGc8gFd49iLHUgtDGNvz3YvVAYKZK4Ndrr2aUPus64oMq8yP-E8iw0WoRjgwh0l7JJ6xpvTb0vvs4uMHf8mQk5RJnvan-bVF_VwbUovPnTBEPOevruGoZQxROx7FO1woAiJda-826ByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saBmS_5u70ZOg3L_c1zfzKMCs1rTLGhLwT43Oin-Q-E77swcAezxJxIh3ySfrXmDfPGza98ck4NpIo1Ecy6jNozHzEhi9NeaK8IjjYET6hRGQ-z9o_eRm0z0qYqCetUHOCPD4-I4ALc-SnrYfCzDTbIBCGsLd4ioHdvV1Z_P0kzo6hi9Y3i4GwXE__ihUMRD8N5InN0mDziAUzAdsAdmLBXqxuZpGPN872_x-Igri_FmemoAfPzHUvaV_wB-A0dwHIrBtJGvNRhRZ-1oReLnwnvG-3mGhlxO2XZUiNX95o9wrhd5o5sEsEIcW12JD5EN0n1tnld3vc14aFoUvDAxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXEe998N6CJI2D1SajRNAV7JbUGHV-5IyZEJqS5hEY_JZigp9zEYV8aJPC1hetQ8TRrsxPa_Z_G7_eUEcI6V--gPWyV_QkCqzaQveXpyYmxeh2nRWgWRK3R5ZdG0TpwijSq6B7AAbYACuBmVfB1i0CYlkej3NS4hPDKlPxVPuYiPhUb9Hb-G9FS2cdDOuqsThf4Spl11oiK_sxos46Bt4yNI5Itjk0JIUTPLGUJYvd83ak738LrQG3XFhBEWYrG4LliYFYFoffjJ1uvdT1B2tDQma4dthlBSTCgsCkuVZFClgqeypgJJecOurXj3WMb_xC0suQaz2GDoQd5BevgtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAI8Y9WpdRH6tlweWYvmc6_Oja6d2kSweFSCL5P1L0EZjWlg-qTsmRisSYLBOaWCU9G69VvyoR_EH0Zc6cqRIMBv_A-SGjZ7qdVIROoTrJLcNiFU6OhAIT4-p56bBpICWaLMPxKGTCvhYGLIvPMibts66yT_1qlmF_73fTgiInpsQr1PDU9DaAwTfDH7qEXM_f890opwgBU7GP0dv_Q6aCPLTst1Rzuye6qeEKetc8CwLa2Sw6BIusBhg0bvRkakEokoaI3J9AlnGCGOj70R3yaDGsydyhit0zPANoNp1KaHwQWut1YX1FuSNG7j9-tUkuWGN3q2SSMMmiGl-Snejg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دعای عرفه در حسینیهٔ صنف لباس‌فروشان
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/438172" target="_blank">📅 19:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfXT1IZHH76FdrG-VMpxL1qkUc4zTCuiaJSAb4sWzUtmlmSDfjkZB2v-errcRyckOurQ2YMzjrU8IZ5YExaVMwOyeE-xBAuq_QYGiSqIAA4tr4Ezd8QHJyQO8QbqYAtc6yTUJFBihVSm7U0i0ZHcK_vf9f1JgIHabzahURpPys6bxkOGDg9gncTSpsYCsK2m15oNP4VA21zSrfoGDfpyN_x2rVPfdL3URVGI75Ku5220sovoLfJyEHWvK4ONtS7h5mZy08fpS8UGeUcCYpZ-dUM2nbAzTGmAcqvJ6fYnlTPG0PUMB-hjfdg5HDSvH-LXoScQiXiReQcvvhAHaMxNjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری دیده‌نشده از حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای رضوان‌الله‌علیه درحال اقامۀ نماز در منزل.
@Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/438171" target="_blank">📅 19:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f54ea5a2.mp4?token=aQDwsQlJ8QRVRLDmOLTl96Iu5VayFzHVKVHv5RQ3BvPhdqXwwjOXx4xFeXOvAoFTx__arJX6CnIrbVuiB55bxHVo0K5vZ-laCEwIdrW7dWXlDKyYHKYFLrc9vUWgP9ra_lDkJAW6iGbVHeYhbktQysPJIgq6wGdKWq2VJL--ct8aL161V9BdqBAQUqhIvuyOL6xWYPeY6HrJ-FtIWZcR7mKo-qv3S-JaBZfaob9BjMjMv_YyxnVQSA6eCFw_5VfYHitynU9-QP6tWGP4ff3_oyViVfvNtlASgiFCw7Lo-WYg045lG2Kw0vwHzPjIXsZFKRplF5oXCmpCq_Zr7ewKSmC-C9a9CzMWrVySMNWR0-57jmEue4HUQeVK2Fz_IxlxUqWGIVQ7Hvv1LvR4xEnXFVnb-c2381pB16QDokU_rMeTfiKwkTAKo4Eo_oeOgUItUNmM6_vdj34DK_FJXAi4l8GhykY9FbfHSrZ30u_uhcY3uM9SfTdXXvkFmzQwpMcDSXsNwe4qULptNqiSMF--vFUYu8wrmR0gWRbDdpTn0Ely_DBRRH1ShW-sNeLSJ8thXgS7s7XzBx0E1cuJa0bHPl-BLgtahIIaxmd4mbv5vr061wi0XYGm-DBj3e4cSgeX6hkGkpEyjzDoAJwLLFUm71eMgNJtopeAHumhQ7dTpRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f54ea5a2.mp4?token=aQDwsQlJ8QRVRLDmOLTl96Iu5VayFzHVKVHv5RQ3BvPhdqXwwjOXx4xFeXOvAoFTx__arJX6CnIrbVuiB55bxHVo0K5vZ-laCEwIdrW7dWXlDKyYHKYFLrc9vUWgP9ra_lDkJAW6iGbVHeYhbktQysPJIgq6wGdKWq2VJL--ct8aL161V9BdqBAQUqhIvuyOL6xWYPeY6HrJ-FtIWZcR7mKo-qv3S-JaBZfaob9BjMjMv_YyxnVQSA6eCFw_5VfYHitynU9-QP6tWGP4ff3_oyViVfvNtlASgiFCw7Lo-WYg045lG2Kw0vwHzPjIXsZFKRplF5oXCmpCq_Zr7ewKSmC-C9a9CzMWrVySMNWR0-57jmEue4HUQeVK2Fz_IxlxUqWGIVQ7Hvv1LvR4xEnXFVnb-c2381pB16QDokU_rMeTfiKwkTAKo4Eo_oeOgUItUNmM6_vdj34DK_FJXAi4l8GhykY9FbfHSrZ30u_uhcY3uM9SfTdXXvkFmzQwpMcDSXsNwe4qULptNqiSMF--vFUYu8wrmR0gWRbDdpTn0Ely_DBRRH1ShW-sNeLSJ8thXgS7s7XzBx0E1cuJa0bHPl-BLgtahIIaxmd4mbv5vr061wi0XYGm-DBj3e4cSgeX6hkGkpEyjzDoAJwLLFUm71eMgNJtopeAHumhQ7dTpRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عرفهٔ منتظران ظهور در مسجد مقدس جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/438170" target="_blank">📅 19:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbT_eAYhoGa79rlgQxQBuE6yzo6zb8fWGZU1Hx8DTf8pWzLYaK17343N0npwvPNpQ0UzgKq23e21WZpKzk-L5hh7L1FQB-yXzKtlwWsgLUw6Xr2zsGaMBiZJZ9Ww23d4jlXvMe_pgoLII2w-VjoLFhp97FLywnN6X8xzWNjiXVYD0dzoXSgR-GCrRTH5Vs-xf1100at8f9044jc4WxRcZFqe1C6fRekHdXA6IKNEMlNw0v3oRVmbb0fhM9PUIZE6FzwtNn0Iue-Cgm25-KgLAx9j9lLhs6ks1ajy7HYV9H8V3W5QePjMHpKCOvUT6l2c9XkOuMgZTEf_SKbdX_9LCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4CIpNc_0C7qN7Ktm89c6Jn0wUmVXYSSzoe0w9qtyH0Xm0gj76IIIOHu8_u7Z3QnIvu6kL0Xyk4e_m4d31r7sIOimkddIdVnBNbhhwDylNQSmrT10knzyRc-bKc8FOHdJrTffQf6oVoo7mz6buD_uuBekbdvr2QmIWeFEDWexb937fsKj__C4NVgyaE82utqPjF89XE3iJlYf20D4888y8SRhszcGj4UE3aWAKxYheMwmFfVOCtLokbWeK7OpIFBCLDsTT46VfVajP0Eh2BA25he_PCErxITNJl0If3DvzLROLnp0UN-K2IdwI5nZx7F-UnP57TFKGIsY-WaPkIgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL4Hl_jfPSOMqaDWDDB7isD4jIKMi7sThdOrnZeSfsZplz--45pUGL4HSSPoEncUhp9Hj_kHEUd7yR0S-vOxrRLd64ZIY0_nL2jgZnuS_-qNdu11byW-xXgY23ayFd3PASvJaGyi1NoMc63uMdxxZZ-xFEkYzl14M38q4Mblvf4ck4gSd_yrkuToZgXSOcked0Pi3E33ZliAJp3WWwqaucduowdKcgu5slB2-WnTsLwls4iJUkYxVWRgVAhn615mCKFjhzlGW9lWELEKssAh_S8UEbHQcgMV0aeN7O84e0QOQ8b5yR-L4gOHCL3G65a5_m4Gf1Zm5XUsQgUhRyQ1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lu24cUjcWyMGpdzNvdGJzsXR7VA6w_6pgDCXDA3rZ5BiE0PiF_SmFOhYvPVwOJhnCom7CiWUJ9ZMPpkPgZwlPZa0vvfrEZv5QpESwFih_qLux7VylvLUJOtE6likqQeDhtlbMsYRwzB0vGhECIIX2I8DirVASNiy503xZCgjlEsIVa5_ygwo7KeqwX8W5beymb0s1-Nv6R6De1GDdC9gjvlCww3LK5zMTty5juLZaSQjgz9f0l_l-v5sWMAbaV_93ES2KdWgn1mCIzbFjZDpFcxRDTF4mCDU7ZtKwey-p22ttuYHcS0X89AOJBTDKy-R0MNY3mF_K6Zxk2NW3z-LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AR-tEsMH98piD8-U-XSKWlkHpWZcwp5TVqO0atsPU_ESXm_1sBWpzrwRI75_UxV7_B-ghAh9n8ORWTm7x0Z5RICHH1zcd3hEGOz7FcUzgwfZmvt5SWRadfM6AvsQBk4DDsGkcU_wOAX7MUhtoVXUEn4_5fBnrXbMhJ6_xH9EJNiPpkKyZ7wzpBJnGVd221t5CzAtmLKR4UByS2EYoQZymH__RUOrOAi2AN-acnW9QMUeSdhsfUtVvfxmVCb47g_Cipyn7m4YZU13hguizD50O6PE6vMzsi7mYRaGMHBUREiGoiMVjro70qD7ehcXG94hKVUPy0yUCWKZ-VjRzCdq9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز نیایش در چالوس
عکاس:
غلامرضا شمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/438165" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-47.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/438164" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/438164" target="_blank">📅 19:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkp-LUhLzajIOTVNX2bo2AjaoMC-TS_T3XL5QbgSlLtmpUQnjOiAtKlKv3aV_uVhFATIN4Q9Y-RhfLTvwsEuC91NE97r2tXiQcnMKJLjbhVM6s51F6BkP3KPukncNNgWlW70VDCxwapVT7pYTKh4ePumEzaBMedMJud6v3DixooG83oSPO4k3HtEx-HNhygI2kgU6G65zOcU9dFa5fbE9PYYyPmsk_kTgpr3Unnm8Ot9nFn33jmO5Z_-3pAk_VkmZSWQs2uTj2LPcw3id2AXfMrQES3LiRyK9siD3nmCA01RRKNvBOrSp6eWyUSlPnbmsaKI0-nDXuHz97zUSOYKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار آمریکایی از پیگیری شخصی ترامپ برای حذف منتقدش پرده برداشت
🔹
کارتر، روزنامه‌نگار و نویسنده شناخته‌شده آمریکایی که سال‌ها تحولات تلویزیون شبانه آمریکا را پوشش داده، در شبکه ام‌اس‌ان‌بی‌سی گفت: شواهد نشان می‌دهد رئیس‌جمهور آمریکا «شخصا درگیر حذف برنامه کولبر بوده است».
🔹
او در ادامه شبکه سی‌بی‌اس را به تسلیم شدن در برابر فشارهای سیاسی دولت ترامپ متهم کرد و گفت: دولت تلاش می‌کرد این مرد را حذف کند چون منتقدش بود. این کاملاً برخلاف ارزش‌های ماست. ما آدم‌ها را به‌خاطر انتقاد ساکت نمی‌کنیم.
🔸
ماجرای ترامپ با سی‌بی‌اس از حذف بخش‌هایی از مصاحبه کامالا هریس در برنامه «۶۰ دقیقه» آغاز شد. او پس از شکایت فدرال از این شبکه، خواستار تحقیق کمیسیون فدرال ارتباطات شد و تهدید کرد مانع ادغام اسکای‌دنس با پارامونت (شرکت مادر سی‌بی‌اس) خواهد شد.
🔸
پارامونت برای پایان‌دادن به بحران، با ترامپ به توافقی ۱۶ میلیون دلاری رسید و در قبال توقف شکایت، به او زمان تبلیغاتی و پیام‌های خدمات عمومی (PSA) به ارزش ۲۰ میلیون دلار در پلتفرم‌های خود واگذار کرد. ترامپ در تروث سوشال این توافق را «پیروزی برای شفافیت و عدالت» خواند.
🔸
کولبر که از منتقدین سرسخت رئیس‌جمهور آمریکا محسوب می‌شود، در آن زمان این معامله را «رشوه چاق و چله» به دولت ترامپ توصیف کرد. برنامه او پس از این اظهارات لغو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/438163" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438161">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE-qI9EDZpf7Wb5Zt0-hNlxsNN4ZdGSfPz9d5cWSCQXVovxb8RrOSFpOhBEC5XcGAGCyfKCmKc1TA0LbU_tkz60snn6E2rcghnxHM1GvhjJ3ZmZOnXJesK7iyuM6uP7qEYJjOCm49RhVmu5DwP0d8eacMtIa5CTi_q-gsfvYhuyc4IO0jQwfeN5KY6sgNCJ89QewU8H-zMECylr4GC9CVMYIib34k1E-RTMmQMi6tn6WkCeWPwYM1xPyNiuSOEXO2lMnGUHCZJGn4OGA-ps4JbbqmFcAmwyOPvmORmnlg3EJZswpqP-ZR0FmfHviWvgvcXdojxwzDPEnc9_mrZEADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در گفت‌وگو با اردوغان: موانع بازرگانی در مرزهای مشترک باید حل شود
🔹
از مواضع اصولی دولت و ملت ترکیه در حمایت از جمهوری اسلامی ایران قبال تجاوزات اخیر آمریکا و رژیم صهیونیستی قدردانی می‌کنم. نقش آنکارا را در پیشبرد روندهای دیپلماتیک و تقویت ثبات منطقه‌ای…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/438161" target="_blank">📅 19:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkFTt6A1pm_SPzAdkDoYxjLlxG-DYB9sHpGFv18xGI07L6xw9l6hFrbn5c4PnuVsHzRge3g9K-8WN12OaP1y73vXUTgsxGXoptYe0_DHjQbJnOmpoWt5u36vxw79L5E8O08NkOPnVbDyMTt2NfHplTUTLSJkvO7rJ-e0NVUgTZDbPz5LgkRXCmLTv3p0m_i7CW0C8TcllCXoNwrJv1eaKjDTbrKDfaLJN9JyN8cONOmeT1f1hu3qOOpQEh5e_eEOWtSOUo1DEwrwSqr4SOFwoVk0EWXE-BeNuy7-uybGa4ysYPUcEO5SP8kiLrTcJ5AvZmpW6diZ4z9juOFuE2W9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9Yves1cebnL8UUpKWX1ZGVP6GKiK5ragALc7Q83V-qcL07e6BLeUV3O_oI7alQvvukCKfP8UDpX05GAIr4EAdl2RsAkbstWChFK2O_J_qB68ENwzP3Ozu_v7ghTVnEY3qA5-TF8Su7H-wKcHBnsEEj9Op3Y4R_Zuo7mgIjpyPA6w4DTNmOuj14zLuGtT_Gf42ottOeKUrSNXKEuNs1zurdawjVfNxIlzLL-uGefl34TR8IfmTmwjKDy8-_WMydP8XHqyI0lG8UEKumvE7IIFHYCjGu8uLlcBkU7TmAf5Kct7a_EcX2-lDIhERg5pJN0mVYvhxX9R6QsV58ghNvFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_Lq1kqxDHrkerR4NyZniYKFkEpC64yza7uWpziQq6TcwXBzX9ppJbM4FAjRyfWR0_5JR5m0Oxik3Wedf8g5_IKaBncwn2TEVWB7mY5-bIwZVwpa3a9ui-tFDcINne8a9EnTtxyHbDEXRnreEhYkpHUcXqREP2gLh4hOVKW2LWMiEtmDxxV_PLKCKVGZ6J6SpNRkgz080RsxyfK_Aou-XrfkSeYNGSNzZZoJttiOlvuUvUDbyM6pq1Bd_NBwkNtsnXkI7Czl1XUUWodhJijTMac8550eim4S4BTkT2oFcnafaYtO9jeBgvFc-Wdpfyc2CTvvQh-pXTkeKhiGtN2tLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNj1TfBp3dE_OEHO1-j_HESW1DP1MTmuRYB7jGyJTqxGLc-GMQzqOa2XI-0NklKrcHuKYH9L1IDowwV7MAjhZgL2otIf85BnurrUnFOrqwVNWPt2V3WxlRu1NRfxZGcrAdLnQpZXJ2by2XVJPoVXLauuh4oUqgDCD3bDC3aODe4DWr5ua9IPF_8EbQzOt4QqERfOmXGHI56EkVej2e43AYB7VSwwxsQvCvOIfF8N4sUYTKKcQiQC9Anzcc-SyRgJSy3ujrdZYU7Z7RfrqpZMmCBXicJHYwRTmgdlC8PLbAuNajb88urdzuZAkthAmaVUSbns_eflfoVJdU84waGYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C--DOmMRA4-RvkcbEP7P-E-ZegE-NQCE3SwDBHh5UTlg7wSRlk8nBjCm6O_3F3_xLs4g1TZ5ZU8GGwwaJ1890xk33j26SQGlEQG4nttxCRxLOVvvcVGla3XIbl3XlCIY3NDjRtbWdBwPbwJsfB2EKooWWHRu-7r3aZD-oLuomMdoxl3FmegEOcrGpoY4l125NRdeZymCSnGqidVpT02xzU9LQrNHP31v9C-r-uoutA8MDFz-KcMrAJ9tIepsv6-FMgozTaJaYquzgh6uRWGN-V5pyrE8gvMx7N7vefbPfu0r_xtn9l9w3lHlVSDC9fgCHl4FKNqcBLciuUniE0FdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9Ea-21qvMY-NxSfvms6x8jBjQFWeLbUny5-1f5R55ddg9JISfM4qFUcfzp0UeANSEHLhAoAgaDxZZQcLqJngZUGeuZnd0bx1JgAZXL9LUHqwvbmLuzfAK276zurspEH6TrLf1OxxWLwnMNfagKRAAUqL2d8gSUdDtacVlH9DbPzTh7ZpBsYNmWNVSjZlDEWyp7BhuOs8XJ8VTzo7WRvvh9KHjx1Rp2uir5PhBUrhNn8ws6lYeV1TmHTKJ7zCYY5XK-Rscu9ULUw5Y1bHpAA5gDNaUXU3BK5QBdQgFJH1NfH5KPfh95wee9w6Pyqr8xjCk3blZmNfKc_x-Yken5AdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین بندگی روز عرفه در ایلام
عکس:
یسنا ساده‌میری
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/438154" target="_blank">📅 19:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438153">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-sD-wpaqPOMGLkyimeYdEqg5eCgLZw-zR6kDonOqyXOF8lC8xZHHOCOv1m3e6E4GDCzlxaLg4iVtTrGVStF1FtHbim0fZShUKb7vfhrZ2vwSj82gvs83R47F_lPNMkrzbpTbUjNeUc2INzcVNSkcrnUrCl9dY1RYO_nI7ViogdAW6arVyrgFaIscwLMrOOfk7Ec89SaEKYe7UOC3JpunNygGDjDcjsTxKXnGoGz-Wderg_-YfTudz3WkcxAvN-0Wbiy08NKEk8JhEjOoWQrjbm2wu2eJKsX8pUaPmqD4dRIVEmQPNpFI8PRuzpLhfe16e7mQ0O_bmZvGMofSm2Wcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در گفت‌وگو با امیر قطر: ایران برای دستیابی به چارچوبی عزتمندانه برای پایان‌بخشی به جنگ و تنش‌های جاری در منطقه آمادگی دارد
🔹
ایران صداقت و پایبندی خود را به مسیر گفت‌وگو ثابت کرده است؛ اکنون زمان آن است که طرف مقابل نیز اراده خود را نشان داده و در…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/438153" target="_blank">📅 19:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438152">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqP1XyPSjerox3XG3o6wVgvIg49GKxtNpG7esE7bfG6gkR0W9K9ek8cMKQxFbgA1Pnw6LU6gwHTOUk_608zR1cKoKMQ5K9MkkRslTzHyNTKcHg5kpi6037eqhyr7SroATl03aOwanCajQ47Unl8AnuLs1AeLEof-TZ__-Qv9wuy_NBKhuR1KTt07xryDYiKyFPvzvxtCM28ocaJ9hSOOmPXyCg6FzOb1Et8eSvCLwpjAvImmYg8P2fMpmxy-62X-1RwAuPdFc43Fq49rzq1glkPcMbG-fqyRzPr_g0BZGS9bdH8DRjgcEHqmic4qG8A75uXIs5Ri1O5sZ0K1urkSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در گفت‌وگو با رئیس‌جمهور مصر: رویکرد اصولی ما همگرایی و همکاری همه‌جانبه با کشورهای منطقه است
🔹
اقدامات ایران در چارچوب حق قانونی دفاع مشروع و با هدف دفع حملات پایگاه‌های آمریکایی منطقه صورت گرفته است.
🔹
اطمینان داریم که پس از گذشت از این مرحله،…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/438152" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438151">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTki7RN6SCLGxuHAKNZYIXemmfs6NlWLpj1YYSk8alwTYO0EQU5YoT6U29z1jCh3pDAi5lCIyBHVh0O4EKnaVkAuT_X44VDsENKvXARBYjyLnVJyaD9mpZLwc-lyw82tYEHjkt2T2YZob1fI-1C6WO6tgj5zdWrM8fHuCeq9qS99xGun1TN1q-iAdgEECh5NSS8dSVN8skmh3RcDOUvw20l36yoA8UFw22TM17OQPGZNN5wZVUbd528EXqk4yp3arvEQlsh2u3pNUBDXvWKf6R4qpf5tzjI7rBIp93hl7LBw-ztzCN1LnY9n6KmrzCapunhiiiV5iQX6cjci3tjwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای از سرگیری برنامه شکست‌خورده «پروژه آزادی» در تنگه هرمز
🔹
روزنامه وال‌استریت‌ژورنال مدعی شده نیروی دریایی آمریکا در اقدامی تازه، عملیات اسکورت و پشتیبانی عبور کشتی‌های تجاری از تنگه هرمز را از سر گرفته است.
🔹
این عملیات احیای برنامه موسوم به «پروژه آزادی» (Project Freedom) است که چند وقت پیش توسط ترامپ اعلام شد اما تنها پس از گذشت ۳۶ ساعت متوقف شد.
🔹
وال‌استریت‌ژورنال مدعی شده در نخستین گام از این برنامه، یک ابرنفتکش یونانی که حامل ۲ میلیون بشکه نفت خام بود، با هدایت و مراقبت نیروهای آمریکایی از مسیر تنگه هرمز در سواحل عمان عبور کرد.
🔹
مطابق این ادعا این کشتی که از اوایل ماه مارس در خلیج فارس متوقف مانده بود، اکنون مسیر خود را به سوی هند در پیش گرفته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/438151" target="_blank">📅 18:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438150">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfG0KdsH93O1jKwAGYPYC9DzlIZbuR3MTyufwC4i4p0ZtKGuhv_rnX4Z2m5FP_9IwcbL_WO-KOdkF8RJ8ioxZtA6QIkXX3YzZQnWp-bncPaUsnJEFXbBJnlGtBy-IQNTAlN0yT6PkfZol5wtiikIo5WBEXACOTsykc2-cEa1H4BktBshtFV_Xbcphd5-sfCbW3m6HIYXazTlQX88k7BXLNS5nr63VShutMr8fa8i57BckFBMOqnwFsLtByYMxGicRG_QM2JK7-UZHMe3CqL6e_Vt7XKsBBXN6FWknEz4AB7NhWl2PdVb-S-pltKWTraBNGs5K6NqMJvFhGnckZxdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در گفت‌وگو با رئیس‌جمهور مصر: رویکرد اصولی ما همگرایی و همکاری همه‌جانبه با کشورهای منطقه است
🔹
اقدامات ایران در چارچوب حق قانونی دفاع مشروع و با هدف دفع حملات پایگاه‌های آمریکایی منطقه صورت گرفته است.
🔹
اطمینان داریم که پس از گذشت از این مرحله، فصل نوینی در مناسبات ایران با کشورهای منطقه گشوده خواهد شد.
🔹
ما به آیندۀ درخشان منطقه که در سایۀ وحدت امت اسلامی و نفی هرگونه مداخلۀ بیگانگان محقق خواهد شد، ایمان داریم.
🔸
رئیس‌جمهور مصر: از روند گفت‌وگوهای جاری به‌منظور پایان‌بخشیدن به تنش‌ها و برقراری صلح و ثبات پایدار در منطقه حمایت قاطع می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/438150" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438149">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffc1ec55.mp4?token=Hn9rorhDqOGY_FoQL0AxFD0a951dz6Mc__XO0tABy9m2xWaafTJvoSaFwHJLzZZyRN-kxsFIGnX73dv1X2vwmoRS6EZ9B7wdo89ntRPbgKoU3LgXPz4t9UjBusOjEk6jIAhfSEelc3E4c4CQs8JG4BLwXaAnNb5TSAQl_7_IpW9s9Ov-g31BMBm8zFpZP47Qx5PUo4hyfr3OOMtxPWwOTOZKd90-LOXeog9Lqqan6dFTr1WuBFAfihAlLVXgRmChKDHki652_ZO4sNiUAv2q03vYW7ObIxx4PsozU7RacYaiVAFGRQmnhm-_rmdGbQnF1B0-42LwoOtzQ2t6Xeh50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffc1ec55.mp4?token=Hn9rorhDqOGY_FoQL0AxFD0a951dz6Mc__XO0tABy9m2xWaafTJvoSaFwHJLzZZyRN-kxsFIGnX73dv1X2vwmoRS6EZ9B7wdo89ntRPbgKoU3LgXPz4t9UjBusOjEk6jIAhfSEelc3E4c4CQs8JG4BLwXaAnNb5TSAQl_7_IpW9s9Ov-g31BMBm8zFpZP47Qx5PUo4hyfr3OOMtxPWwOTOZKd90-LOXeog9Lqqan6dFTr1WuBFAfihAlLVXgRmChKDHki652_ZO4sNiUAv2q03vYW7ObIxx4PsozU7RacYaiVAFGRQmnhm-_rmdGbQnF1B0-42LwoOtzQ2t6Xeh50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار پزشک آمریکایی دربارهٔ بیماری جدی ترامپ
🔹
راینر، پزشک معاون رئیس‌جمهور پیشین آمریکا: کبودی دست ترامپ که ابتدا به‌دلیل دست‌دادن شدید توصیف شد معتبر نیست.
🔹
همچنین ورم شدید مچ پای او که ۳ ماه پیش معاینات نشان می‌داد ورمی ندارد، نارسایی مزمن وریدی اعلام شده است.
🔹
ترامپ مرتباً اواخر شب یا اوایل صبح در رسانه‌های اجتماعی پست می‌گذارد که این نشان‌دهندهٔ مشکلات خواب او است که عمیقاً نگران‌کننده هستند.
🔹
او خیلی اوقات به خواب می‌رود و بارها در دفتر بیضی کاخ سفید وسط صحبت افراد به خواب رفته است.
🔹
بی‌خوابی مزمن بیماری جدی‌ است که می‌تواند خطر زوال عقل را افزایش دهد و در افراد مسن باعث کاهش عملکرد شناختی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/438149" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438148">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff1de4a5b.mp4?token=JnR_ms3tTzy4Rzt7fDsxekr8gO772seV0_rdtYaGbyJXh15ys3u5ph17hyPaHHjeaguElOq_qI7WTFq-YTnXNjQuAg-GlJjD8Off8OkiHHWOBkRZ0i5U1oUvxh8sgNxrZnRLhVedx3DvLRWBVR06sU6eJNhpcbbpCU6ipg_6uRrboM_aARfPENob_ju3B8fNEqQfxZHTIsCXkasYhC44eqrSqM1kWmtdNPLiCvU73-UeGh3eyd6Kni4cNrH6RKMs7dpvxhpez40_tgqH6M5vVPAMI48DF7err455EqN1Lp3iHqhp3Jqf7MVI94gLwXOMIaK0MwNURpWg8HBNybLMUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff1de4a5b.mp4?token=JnR_ms3tTzy4Rzt7fDsxekr8gO772seV0_rdtYaGbyJXh15ys3u5ph17hyPaHHjeaguElOq_qI7WTFq-YTnXNjQuAg-GlJjD8Off8OkiHHWOBkRZ0i5U1oUvxh8sgNxrZnRLhVedx3DvLRWBVR06sU6eJNhpcbbpCU6ipg_6uRrboM_aARfPENob_ju3B8fNEqQfxZHTIsCXkasYhC44eqrSqM1kWmtdNPLiCvU73-UeGh3eyd6Kni4cNrH6RKMs7dpvxhpez40_tgqH6M5vVPAMI48DF7err455EqN1Lp3iHqhp3Jqf7MVI94gLwXOMIaK0MwNURpWg8HBNybLMUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: از همهٔ حجاج عزیز می‌خواهم به دعا برای تعجیل در فرج منجی بشریت عجل‌الله‌تعالی‌فرجه اهتمام بورزند و برای وحدت امت اسلامی، آزادی فلسطین و مسجدالاقصی، رفع گرفتاری‌های بزرگ مسلمین و رسیدن به ظفر نهایی مقابل استکبار جهانی دعا کنند و اینجانب را…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/438148" target="_blank">📅 18:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438147">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌آخرین وضعیت اینترنت بین‌الملل
🔹
گزارش‌ها و داده‌های بین‌المللی از جمله نت‌بلاکس و کلودفلر رادار نشان می‌دهد اتصال اینترنت بین‌الملل در ایران به‌صورت تدریجی درحال بازگشت است.
🔹
نت‌بلاکس در تازه‌ترین گزارش خود اعلام کرد در ارزیابی جدید سطح دسترسی اینترنت در…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/438147" target="_blank">📅 18:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438146">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxAOyWti0FNMD_tBPfujlW0kPIcyTZIB-BSUTNgG3mCreEU-rQpoWrml-_zkir1UfUzEs83NuarOoVvu3OIfnN6fpDTi43Frrlv0RblkJU1R10OmTMFQ34hnV3ObhV-IDuHVXl6eQHJJAJ1zjtI2zy8Fd4EunLhzh3GOWb_l0SJrLmaQObz3juY6C3uOYbzPvZd4evgCGwFcTMqwCdSS8WAXgBUWbHUzrm1IxEEJxDib9kfnx9zcHf1guZRX9_rWUzHYkkEhHgG3owLOBbpVg5KX42koqMx9Byb8YKW8JD2HOzZ9o6xfQE5LK6I3sQH0MQLD3HTMbyxUK8FipWWjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۵۰ عالم دینی شیعه و سنی خطاب به الازهر: جانب حق را نگه دارید
🔹
۱۵۰ عالم دینی شیعه و سنی ایرانی در بیانیه‌ای از الازهر مصر خواستند جانب حق و انصاف را در قبال جنگ ایران نگه داشته و اسیر فشارهای سیاسی در موضع‌گیری‌های خود نشود.
🔗
شرح کامل این بیانیه را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/438146" target="_blank">📅 18:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxWDXi4880iXredi7EceQu-mJZ2lpsty-pDygnOp2ds2chXP-HnP4NZbs2B4BvhTxwcPg6v8RGR5tC3CAAzek84kzNTj5VpQEMpyNl6YgaJIVlSqpFaUp7PUzQNRELGpmZXLWMFBPa8NkYMqx0r-USyzW-dKZJzHq7-zkMKceJOSy8uiPTEF3Xn7mwEYB4eTyRv3SECO2r2QR706b5dmL0vLIcAALosEhltXap_NDVzY0GRCUB5iFU5mQi6n-J6mk6_H8gkBLjrVcB5TMGN-GhwVpuwuT-k9VfOep3ldM1Xk08yCX9-62Ejtkn4tzYa9RBCYNyqwfVjVvmlJyyU3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQld35jGQudesSmCqnmiSemJUWDZavj4q-B2gnZfmOS2Qndtz3SEMAOgG-6GoDx3alURfLUYfPYadrBoqvH_KvKJs2WaR5xJbz2RKS9bBjgMq2WoheJLO-quxeIyhkyocxJP2aJVWIa5345HkxCZ3vj1K9RAyIPQluA_bHc5bPcA4Xd_Th8JEEulkClhveIzyVmhNprOi4ZgKJvr-M9Sz6bp0d0zvtoE8Qmgr3e7kOzs_oNnIHdqX04hXrml4L5gl0ia_LNqYK4xPVOft7u89yXlEycMkYbU3L-akWtOZZLbDtfH9Nkl1pa-9z5XcSixNJLxwXml_kjRD8JekKdlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgsoXhSwKZ9DdBjupCM8epFxrikbhOmUzuiVQvwPW0JByHCsOGWIeRN-CI9j-bJleXOuIY4FSaIgNcUAw6CgHm7BtUgKEJih-I1Qus2ii4uJbR5UEwbhE9f7vKDPmmn7_to4k_us7ok3aYbGQoLA6PgxTwQ5HR32sh9ZlGSDYHbBJU8hH0Oz6T34fEDqoAdPEQ0kgkoA_g8MpsHA1Khpm3d6XbZ15EUqQTH1o8Wah7D3vvBh2AFyoLHjf_pbh1Q5h5gEIXDvWglLQztBbevcgS6o79E56DfUEh6MPlwDuKjsQYtUUuIX2G1zKvdeUruNqmsl3FNpFeMWZJlFSl-LJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2dllFih92MAjUgtUSzxWj6P6oXTaxYMYnvuL8noAkN1S-ak_Ycuyl5SJAy_HVHdmXhH1DWjJHSZp2jbqgXjbtt6qbQH5BJz-4_eoCAH-kT2pWP3Xqb97DBq8jIwg8y1TJDCeIcLWthXPIsw7U4p5lbrHbHj8ezlPYQIfXXsD-AKDXoVOf9fXa2Re7kARpeUisb7Ma1YKzLkmeFXGl1VbSN3UmGfeggkFYMw-RUbZMFaqnvwpkmulkXp9BdE3hRxrKSZh22O6IqJh5ksjUJwVaEfsBfUuznCOIo1Yb9dor01EzpgdhxLTXo4HhaRryD1vfVocn_fdYTXf2qHuUJcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhwm8YkdbeX82JiDy6OfmyDZRkzOz66qvSfoDE9xzMOxkhMIa3YdkS8oUtgGYTCI58Bm2KIV438c4A0twj2P_sCtvCynzkaHBPwV0bzPi2tVxwxDCBiO_x_x4cKZ8uH0HrbYN9QxqGWW6M16xiexlbXZuV0YUmiP1iSQrE0pM-4lOv6RFjAeDebm-p_Sbu36-8voltm8zFzzJ3RLqNcShPkvMc3Z8q64kqyVymN9BdbppUtMQ8g5l_nOJDb5BwmrlNH6zs7R62fh9yYCTvb4QiqDKXIhUEq1QttCivzNK3qwhKm4kdg_gMvWCfN-kjH_W1pkHTGYk44_eyL2pWq_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epfUYsLKveppmDCgLWdCHWTThiw11kaJukZse-tVhlEwWgL_G4UeisGYT-R2eH_6hoFa4pi0VG3OuV6uAfggwF84X1N9ddw6SCb-nMiKUYSYdTi6ZHHcK6pFj65pfxvSv5vHRrzWMX0ZyJnw_7f6eAyXli7dX7xND4wbrwqlmkMHL2I7tUdEvU2e69g_LsuR-__rT6iFHvWiAKv7X8zFq0Szn6ZFa9Zxuvlv21vnTPCiSylITs5T8OStWrQx130DNZjZaZtKmaJktg07mOANeR1Lpyz4pWdqKHN_nEP6bAtdfrsw8V854hXdvsUu8yJ-kZz1zc0JWipVToI_pEJAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm1cUe7LWyMmY_kFPY22rJbNvc5YcWM0ZfWxG99vkHpTrqxUHzem1fqaVaprrVj3AHrPpjqhSuaVJmSKVhrT7Ukf4eWNlzyg6SP7dVp5j1EDw2oZjj82C_MpvyL7FV3_J1Qu-albawTQ0wzO4JnrDXpEFKOmJ4lbMQtLxiaj6yUEUqR4kt5zhXfnnY0ba6qCZYT7-Ntb_ouC7xYQO73wjYSMgfsKGhEygjQgZ0Dp-v8s24m5Oir4w5Lmq62bm3qktOs_Us45zxjgsAAQUgYXMVT9Bq4CO5yEN7zoPWCiLtN0sk24y4N1nspatYqL8VnZo6i7GEjjCG0NPOwLVJcdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دعای عرفه در گلستان شهدای اصفهان
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/438139" target="_blank">📅 18:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438138">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtGifJExLErWRDKdNCXu-_SL0N2Bb6w2eSeXp3oiZWmQodQXtn5TIi-SvEHEB7OLsX-QdOgPsilQXNchHFcZoQdHUf_NrzAHmjpBijpVwxtn_FSmozVW_gdlHOrc9-uVwaSNXaWw65qYiDVcLekGcoPAzVsvbvBCZ6SdWJOJIaY2HUmAgL0wy9q2QMWZYKTPD9IHO8ec5kwdjWns4pc2Jl06g8OfPcTVb9SGPXtSEMZ644K_HYLQVf6NU655KdBMLOGYXZLroVkm2w_8uZEmcL88OlbrhTTNbl26sa86hrGUSK_AMk2t1GVQFZKz8hfgTp5ttEugBphtmv0YZS-_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان بولتون: ترامپ عاجزانه به دنبال توافق با ایران است
🔹
نشریه هیل: مشاور اسبق امنیت ملی کاخ سفید، جان بولتون می‌گوید که ترامپ «به طرز محسوسی عاجزانه به دنبال یک توافق است.»
🔹
بولتون شرح داده: دونالد ترامپ به فکر منافع استراتژیک آمریکا نیست و به قیمت بنزین در پمپ بنزین‌ها نگاه می‌کند و «هر کاری که از دستش بربیاید» برای پایین آوردن آن انجام می‌دهد.
🔸
بسته شدن تنگه هرمز به روی متحدان آمریکا باعث افزایش شدید قیمت جهانی انرژی شده و میانگین قیمت بنزین در آمریکا با ۶۰ درصد افزایش، به حدود ۴.۵۰ دلار رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/438138" target="_blank">📅 18:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ly6R-CgZ150S1k3o0HlIOCUCCZ0xNNjfrvNMtK5aMgIytNX58b61gV8rR-H6UzeUe44tpBSXD62I_XLrM9v10Xj9_vVCp2yYNTphZULYbpf9h1Dr3C-R1KgJpFKS9hBc1__PA23coi5b_6r1SY8qxG4yjDnyMp4ti_tROXtURFexVDYKDxjIAYzWTCHVHgzcBRGCSPp0WdM85Yt9a3m5RAsZwwNJh7jmOdi0WM5u9yZBCy04XtBIpDfd1rUokh_fH2IH8_VOvTM6A_yGJzP95CyUK9skCB8_ijefzagNlYwktecKr-kBR5akFI4iolnWbrudzWBlPVA_3lFyZoQonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ret2sk3FBotTxpQBkLU461lwQiRePY7OE2mvZEQeVvUtP4FIyyzpzjiyweq-WdJ3C0fm8LGKHo7u7z4VoJllovdZh7aiowHlyLRczNW5X30HysUWDNxPp3XncpWPy8QzpI8Gyzj2GcyKGx9kscBtRNu75qxS6KNmpkcx1Ei99Beb-REasI-pBxzSjElsdYlw7S7vCy7vHoc5LQvckkUmbjy9bbs-ZAwb0_FGvayS-44y5-EV4z4i5WUcWeTAaVpa_hOJmtdvP89oQoq4I4foaNnKL4O-w8b71FxKOJMBrAlFDAWPxhUAjVUOEQOVWkmRRxk4_a9cPtJzwwKKzHBpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFUTo_6BX5eDi5tRYaGf8_Qe0Cq0uA7CuaCDJ10w9dGDorkDMI2SKKymAo4WhSvsKnV8vbs88FoMUI2jssmQ1X3J21VBw0oN6mCAZrBYTEGThqvH63s2pUs2bmbVrWmOwCjvzrKaHmxY3wXPxuLEnZHouiLN6vb2ZL-P6OeKTF5uSMEdDpKgn_Ql7-MsOrUf3v76efEEnvByZOmMRVmt5K2HvPSanBJSapXDBc1ZflIoOt_n2yD3Pl2DMnQCMo9JlQ3JPDc1Jq4IARmYHNAVKKKPkF1Uk4ae-g5lB0lRWI76QhTK1Ff_H9DFLGpAPTZbkmYtLpHUAP_XYQppeHHjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMmEdr6P3BYrYIPJ1j2aHSE2HXwX5Z05exwAVok-T3fI1_PwsSfAPqyaH4PlIMqlBVt-ZEefLZT5EXzRh7iclVOoNIQlah1ZCXwBECAE1UiuBxBqO95VPmThd_cVydHwKuoFtb-7itmiGEYxB70uJS3kI5EB9dSF7UnF-iukOv2Bnstpj4kXpd-EK3qmntqxjg9VutNFW_qmoTjkAu_-NpF4_Ga8hikyAxE1U1IjZHHfY3ywCaq5UkCFmYMLYZYoKLhKXmHenlPDDnWqOACsR6nNQ3B5VeddNO3r1nd35cYr7BpLbDucFdTvyxH41U7dEUOXHTLLA1YEF3FbgHibFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ohd8cSHNcitlvMqz_6Q3vNruNbR85IY1qMXSDCdKdRlTwvfPg90vQgMa27nV9Ch8r6xcG7169GIO0a2DVxxjN3158Nxa94_m8KJekR_tnDnRcLXQxxOrfcYyR_Q6_B9_USKyP07sCj9jKmrTcemQUEJdEbMOGUzhc_ggluv61JgpTd5Vlv_g-3QhUiKhZU0a023HUrGZ8UG1o0vFt0V1F6KahIzyDvZyRf7K4KIEU_NxIqUpOG83h6qoJ0KsBIAevMzTP2KuoHKhMl7pWZs2vTQXA62XJIEUVTrC8nn2CSgFypqJ7MiALX7FGBCVQTLeqv1dczTlZXym_YWvB1cjuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از مراسم برائت از مشرکین در صحرای عرفات
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/438133" target="_blank">📅 18:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8Y5RG45aMCh8gwRb7qhu_9zEcv3vazcYxLFOlLbtLxluc0m_hX0VjKhfgbno9_dw__nDkpHasXgmX8Efq5FP1bz1ZBcaZHwmYHFwlR2mRP8UfCNrQ_H1vBO8vfUNvlbIyViZKa0XTLNklaI4yC3jWg0VdUWkvBWwNILZTLUlvdMzcQaeHXfNKcu0WqCDepYJCUFR6VL4bSTuS3uE1jx5TTXmPD74mRieT9XYdYbKofTmeLO90Vq3G2LD34s-3Eocq_HPmvM31gylMHnM2agunhtI4fBEdJ1CvJipg21vE-dZ55zIE3IktyHI6EURR3xi24kWB0ZmmaWXlF3PASw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌معاون اول رئیس‌جمهور: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
🔹
با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/438131" target="_blank">📅 18:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDnqVuw12Gd4tq5_kuC8qk6RvHqTcWc3W-EWW9faio0NMyGyQdOmnIPA8zMcMGtcQ42kQUPGmJdekXaLf13X-cR-hbOMD8ceIGG-yC5RHhrIWlXXtTGbu15FpDWM6C1T_PfzVpN9c_bsqsXtBR-_-EHC4yqTrKk3SsBe3emrc_C3V2Rynuir_MvwgVPAsnkPo2MELfgnZY-JgDOtXjiSRwLce5adbae08E9DKFq1RjTeL7IhyH2HTGH16-41Sp7KW2_FPkTGypWG8gvWCVChytSUdtOu9L6pDkeID-zZelN5NZ_U6M1GHh_uX6Bx14LROkh17xD5beZmfX2O0PZ3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای خبر مجازی شدن امتحانات نهایی در فارس چه بود؟
🔹
سه روز پیش مطلبی با عنوان «امتحانات نهایی مجازی شد/ زمان برگزاری کنکور تغییر نمی‌کند» توسط یک کاربر در پلتفرم تعاملی فارس منتشر شد که وزارت آموزش‌وپرورش و سازمان سنجش، تکذیب کردند و در فارس تعاملی هم پرچسب جعلی خورده است.
🔹
این مطلب توسط خبرنگاران فارس تولید نشده و در صفحات اصلی خبرگزاری نیز بازنشر نشده است.
🔹
خبرنگاران فارس دارای نشان رسمی کنار اسم و آی‌دی‌شان (تیک نقره‌ای و لوگوی اصلی خبرگزاری) در پلتفرم فارس هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/438130" target="_blank">📅 17:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ سفر هیئت نمایندگی ایران به قطر
🔹
خبرگزاری دولت: هیئت نمایندگی ایران به ریاست محمد باقر قالیباف، امروز به دوحه سفر کرد.
🔹
این سفر در ادامه روند دیپلماتیکی است که در چند هفتۀ اخیر با میانجی‌گری پاکستان برای خاتمۀ جنگ تحمیلی شروع شده و ادامه دارد.
🔹
در این…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/438129" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwx11PK9m5yKekiDiJXbSzPwiHYSjGBUOEmrTKxogQv0crrzdQGmjYhdVaVM93TF36biYXZUgy5APdyeP8Nt8YGv4e1fn4BePCHYYGW59wmi_aY1PVCtWVEciKhBG9mHvOMpRtwC5ha1lIWg4vLRkRJSdrBVBDnziy_se_Y1hhOhkJul5zrM8_t9luyA5MDIMGRORu_fy4bQwmlE2Ahsn_ewyceG__2sNgZ1-tLHtTBofUmbXzwcNZE2HWtp3NrCD4gXZCAfRLqNq7mKjxUdjp_oEh7gNeZkogUkJGqpSbL749w_fUTwXUwEYcuD46tDC2arSxp4b35XyYSrh-ffug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست ۳۰ نفرهٔ پیاتزا برای لیگ‌ملت‌ها ۲۰۲۶ اعلام شد
🏐
پاسور: عرشیا به‌نژاد، عمران کوکجیلی، علی رمضانی و ایلشن داودی‌پور
🏐
قطر پاسور: علی حاجی‌پور، امین اسماعیل‌نژاد، بردیا سعادت، پویا آریاخواه، امیرمحمدگل‌زاده و محسن دلاوری‌
🏐
دریافت‌کننده قدرتی: مرتضی شریفی، پوریا حسین‌خانزاده، امیرحسین اسفندیار، علی حق‌پرست، مبین نصری، احسان دانش‌دوست، متین حسینی، علیرضا عبدالحمیدی و اسماعیل مسافر
🏐
مدافع میانی: محمد ولی‌زاده، یوسف کاظمی، سیدعیسی ناصری، نیما باطنی، آرمین قلیچ نیازی، شایان مهرابی و متین احمدی
🏐
لیبروها: محمدرضا حضرت‌پور، آرمان صالحی، کمیل خجسته و حسین حاجی‌کلاته
🔸
مرحلهٔ مقدماتی لیگ ملت‌های والیبال ۲۰۲۶ در گروه مردان از ۲۰ خرداد تا ۲۸ تیر برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/438128" target="_blank">📅 17:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4100b3272d.mp4?token=caYRMTROgXCO9VlF8MJdFOzbnevqXcJ9IJZaYBlWGF20-mOTtVWTn1fRI9NecH652Y8ocNUprVilhiCw_GhiKgDUkH89iw5zkFu5rOz5hRqDvBkaEWkq6A9VuzMtuuWuab_kTbM2xHA_mv4piSDEdcR3hSPayo1q9s-qhln50jWxvFKD-ZuVkVt21IuFlRx_nJScA9fAGKqSmno_0nWhXZiH3FdJ52vR-Z4FOovtXEy5ayGvMsmmApBwPTZLlcxzf-KkJR1mAcX4NgCZyEdh7NKr9MbzsJwnuH6QN08w6fkvoS-Zibg0D2WNJlKAF1S8A6hEdASmtAINvFL-TJJ49oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4100b3272d.mp4?token=caYRMTROgXCO9VlF8MJdFOzbnevqXcJ9IJZaYBlWGF20-mOTtVWTn1fRI9NecH652Y8ocNUprVilhiCw_GhiKgDUkH89iw5zkFu5rOz5hRqDvBkaEWkq6A9VuzMtuuWuab_kTbM2xHA_mv4piSDEdcR3hSPayo1q9s-qhln50jWxvFKD-ZuVkVt21IuFlRx_nJScA9fAGKqSmno_0nWhXZiH3FdJ52vR-Z4FOovtXEy5ayGvMsmmApBwPTZLlcxzf-KkJR1mAcX4NgCZyEdh7NKr9MbzsJwnuH6QN08w6fkvoS-Zibg0D2WNJlKAF1S8A6hEdASmtAINvFL-TJJ49oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حضور زائران رضوی در مراسم دعای عرفه
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/438127" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1VvYzgAEOZ0cHNQ34bjsH2712UOPRIbmB_OgMK9nnZa2SvpM7WVMs72WA-N4oL2tvO734u-RuafnoSThWfWrlU3YGFDlPt5Hdq5m2qGqD8qX6rjiDmxyeeAnnIu3LpuU-zIb6Emzvc3uit2n_L6BqncU5lqE_FDVZ8qMxRNwXxJ5Iu4i57Th2zrpH_qJn5A7qDFRIi_wCR_zX905Q02_2X6de01fhf-ozqo7irahWr9Yjz0JOKeQHo_t6QEKi_ebVKHhPT2K93nDzb3XE_3DsfMWubX6YT67LIeTp9nXIvWKzCuPC5de6wJJmLg_6U73OnEAa0RHV1MkHjMMnHVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
یک منبع در وزارت ارتباطات: مصوبهٔ بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/438125" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8735883516.mp4?token=K936DGQZHVExAGhdnYzPPjTOf9EWMuwgoXm7Q9h2wSCVLUlEzukgHQ6rdAqM0PTDhgCDYxycmK9-oR82O0khWn61saecWGCiXSjTOmYl4tgHQsx-9gBq0M7zTVQykScAWDyhyoHvsLdFl5nfUs_ffAPtofW4w0WdogfdaqLwpmqrxLRZZ1bVKmqhbLbU4yax_76vRxlk0vPrNh2mH1uMlUsM6ynM6NeqRHSrhtpLQw51CvV1jszLFmi_t4YWoyJ_Ax8ETOKClP3nJapYSxIrc5mjt7MwYqXROVIMyjyadky5nNUyypZ6Gv7fH8aa24ngMEkWG_P3oUeMh347xhtkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8735883516.mp4?token=K936DGQZHVExAGhdnYzPPjTOf9EWMuwgoXm7Q9h2wSCVLUlEzukgHQ6rdAqM0PTDhgCDYxycmK9-oR82O0khWn61saecWGCiXSjTOmYl4tgHQsx-9gBq0M7zTVQykScAWDyhyoHvsLdFl5nfUs_ffAPtofW4w0WdogfdaqLwpmqrxLRZZ1bVKmqhbLbU4yax_76vRxlk0vPrNh2mH1uMlUsM6ynM6NeqRHSrhtpLQw51CvV1jszLFmi_t4YWoyJ_Ax8ETOKClP3nJapYSxIrc5mjt7MwYqXROVIMyjyadky5nNUyypZ6Gv7fH8aa24ngMEkWG_P3oUeMh347xhtkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ صهیونیست‌ها به  سد قرعون در شرق لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/438124" target="_blank">📅 17:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
آغاز مراسم دعای عرفه در حرم بانوی کرامت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/438123" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
برگزاری مراسم دعای عرفه در حرم مطهر شاهچراغ (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/438122" target="_blank">📅 16:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e1ee161.mp4?token=ClInHbfRU6jssezh12JLEmPVZ9-35pKfvlkbNsGHBSULZf8tNFvRFHPSGHuaWidrz3v_gkLVB4RoITJxZAJ6_tWmlwU9dArw5iIH4gSyXf7uZhg9yg8ALegwicjxqd2rw5SamHTL7OQ7Rhm_6r1shPJcS0z641uBVgfqjvhcUQR9bYPzmbDM2-RUKBslbgI5hlLu5xAlT3hgOFjmwPYPCrM0U3FMpPY_dBTV2SIYp7FrkFkS20Uo2ulM7xByannN_lHtkH-1qphR8qV66gfbDH_pJaiwOpDmbJG7cbLrslXYjCTOJlm-B7MXosmtE2hdiZ6Y6yC0QPLHvZ-yOw3a9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e1ee161.mp4?token=ClInHbfRU6jssezh12JLEmPVZ9-35pKfvlkbNsGHBSULZf8tNFvRFHPSGHuaWidrz3v_gkLVB4RoITJxZAJ6_tWmlwU9dArw5iIH4gSyXf7uZhg9yg8ALegwicjxqd2rw5SamHTL7OQ7Rhm_6r1shPJcS0z641uBVgfqjvhcUQR9bYPzmbDM2-RUKBslbgI5hlLu5xAlT3hgOFjmwPYPCrM0U3FMpPY_dBTV2SIYp7FrkFkS20Uo2ulM7xByannN_lHtkH-1qphR8qV66gfbDH_pJaiwOpDmbJG7cbLrslXYjCTOJlm-B7MXosmtE2hdiZ6Y6yC0QPLHvZ-yOw3a9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/438121" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444f48172.mp4?token=aZyMTeMcKghpm-2MfyykqcMXic9RQRf-_Qe_YyWN2XCh1G419whXwqCZ6-MQS2Y_FxCBaQyDVqNktYy1BRf8qi0Fm5V0gFKEODvGS4RTHpJhL-JnEgZX3qBuCudqegO7QCd6ydmWtt0PlMT4sZE_Y-SKGeSG4vChF2aGgR6qADbuW9nVTR8AYKfeXFIZLpk1IFnsRMbNlF3qYBj07mAZFfwyz7uM2LMQhS1uPQCaxc89mG2kuH3dOe8GXVFKWHttJy7JHyUvXPOvjjgfVaqdM1vnIpPmLLn5cXJbliUuO8Up53srTJD92rw9lSNWWwst48eFjgBhWCR-jS00uJcaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444f48172.mp4?token=aZyMTeMcKghpm-2MfyykqcMXic9RQRf-_Qe_YyWN2XCh1G419whXwqCZ6-MQS2Y_FxCBaQyDVqNktYy1BRf8qi0Fm5V0gFKEODvGS4RTHpJhL-JnEgZX3qBuCudqegO7QCd6ydmWtt0PlMT4sZE_Y-SKGeSG4vChF2aGgR6qADbuW9nVTR8AYKfeXFIZLpk1IFnsRMbNlF3qYBj07mAZFfwyz7uM2LMQhS1uPQCaxc89mG2kuH3dOe8GXVFKWHttJy7JHyUvXPOvjjgfVaqdM1vnIpPmLLn5cXJbliUuO8Up53srTJD92rw9lSNWWwst48eFjgBhWCR-jS00uJcaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر رضوی، آمادهٔ میزبانی از دلدادگان روز عرفه  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/438120" target="_blank">📅 16:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438119">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwgCDF5tMPaE-cQdwwWwHsZyyMBEBvl3MKRCIA2I4DFhthk1WAhoxl8Lxn3RtScI6R2AnWVpT_TX3lcE4ZX_R9_Zq1Os4VGHELTtF2YVtgC6BSZyWve7-vWi1hd9eyNMQThvlgOZ_MCSw_zX28ZH3aT4Lm4IHWKGcCvVE68X45JMc4jx5PD1a0H_dRaj8FbHOtDm9ydJhGXQhpCLRx-YrrBse2eVGlzJIXg9vj58a8Po8gs-9lsOuIhmNE_r13-4T3eaLCGYSi0CGYPUtT-fxp5ltIvy46tQP3_7oLbSwqY1GjaAr2y-rSfPPnO_nFu80CP2KDHsTSHujJvP11MdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرما‌یه‌گذاری ۷.۵ همتی برای تجاری‌سازی دستاوردهای فناورانه
🔹
وزیر علوم: در تفاهمنامه‌ای با صندوق نوآوری و شکوفایی، این صندوق ۷ الی ۷ و نیم هزار میلیارد تومان در تجاری‌سازی محصولات و دستاوردهای فناورانه برای تحقیق و توسعه، ایجاد سوله‌های نیمه‌صنعتی و احداث ۱۰ برج فناوری سرمایه‌گذاری می‌کند.
عکس: احمد معینی‌جم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/438119" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d258dd80be.mp4?token=aTAu_Z2e037c7wbsKksY3B3vhqeQDPqvcN0BovwMcT8dM5pfwSJ3d84YYQ-GmNp-2NrDzqyuuh2LYFX1Az7kwKoOqbq2kamjLy0iwiGXXmZBLlQS0OPpvknWB5FDni4zxRzle3HSG9EsGFPdcPimYq2Dm0Hyf1ZJeQPJ9tVcb_Sk6Yv0E-ZCujuDqiT5lS2su6bTTkbzbGNFjkzoLQ3fIF6y70M4bXv1jXH2E4Qgl09AjRJRpz8dMvj2J4qSp8PLpfeE4K7guHUtKZP4z_BmO3pNDQA0xXBO0eHazFwocBJpCRKN9yEgZjjNimwvqOI1j7sFvUhBxiU-S_VxesAL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d258dd80be.mp4?token=aTAu_Z2e037c7wbsKksY3B3vhqeQDPqvcN0BovwMcT8dM5pfwSJ3d84YYQ-GmNp-2NrDzqyuuh2LYFX1Az7kwKoOqbq2kamjLy0iwiGXXmZBLlQS0OPpvknWB5FDni4zxRzle3HSG9EsGFPdcPimYq2Dm0Hyf1ZJeQPJ9tVcb_Sk6Yv0E-ZCujuDqiT5lS2su6bTTkbzbGNFjkzoLQ3fIF6y70M4bXv1jXH2E4Qgl09AjRJRpz8dMvj2J4qSp8PLpfeE4K7guHUtKZP4z_BmO3pNDQA0xXBO0eHazFwocBJpCRKN9yEgZjjNimwvqOI1j7sFvUhBxiU-S_VxesAL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعلام انزجار زائران عرفات از مستکبرین جهان
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/438118" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6547b80539.mp4?token=VtIgdMjh7P1N8bT-7XGsxcWL253GZ4jKRfSX9y32xGIugCm__3t6mi5u0tSssH6LH9tVq2A45KVHskj_MFamGw-n3FmOngByaMzPzIG0M65H67SAYRZ4GAIvOkE5J9tzzg_FcyYYRFhtp6qFJ9VdApB11lvPY2FOtDsI37JrhgkJXaM5up7mgjR_v0Me2DgdWwASrN6XfK21m3u7X2QiXlRS_0jmr9ZCI2ljLRMpZ7Avb6SaGjE3xIV9Cgw7jJ-xpQRpWElp5_hT2x-_bZHKjlEPk8rtLiNzbw8aRNDZTS2MpD-1Vgi_YvI3zNrl-vBuCDXG7HbS3GcJba9TOy9cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6547b80539.mp4?token=VtIgdMjh7P1N8bT-7XGsxcWL253GZ4jKRfSX9y32xGIugCm__3t6mi5u0tSssH6LH9tVq2A45KVHskj_MFamGw-n3FmOngByaMzPzIG0M65H67SAYRZ4GAIvOkE5J9tzzg_FcyYYRFhtp6qFJ9VdApB11lvPY2FOtDsI37JrhgkJXaM5up7mgjR_v0Me2DgdWwASrN6XfK21m3u7X2QiXlRS_0jmr9ZCI2ljLRMpZ7Avb6SaGjE3xIV9Cgw7jJ-xpQRpWElp5_hT2x-_bZHKjlEPk8rtLiNzbw8aRNDZTS2MpD-1Vgi_YvI3zNrl-vBuCDXG7HbS3GcJba9TOy9cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#نماهنگ
|
روز عرفه را قدر بدانید
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/438117" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دعای عرفه .pdf</div>
  <div class="tg-doc-extra">207.7 KB</div>
</div>
<a href="https://t.me/farsna/438116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
متن و ترجمهٔ دعای عرفه
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/438116" target="_blank">📅 16:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f09713cb.mp4?token=HUtTowUWm7_Nz4_GqHMboKaEsqTnWIOeT21OvTiPVpKR5GtaVH9zopC8T6475POKuOcNsbSDSi_D6243XJF18MOkAgHDpbq-GJQitTOI-0mNuuKYCwOcbDLnNrNiSqD-lyTEKNLzdQpVFTWGRH_zXGWLwxpZaIVYxgLZOE61fgwRajOcPpQzsWKTlJhI6wvJYTudYokcv4x9Py1sGXS6GIgcdfKFHgWdKoJ2Y56aETML9kKGcD6kfy6nXKLTCj6FidxSvc6wpr-J_8FhVIjg8zQcd01NufwTkB8NkQAjMd1omPIuhIR5928gOHnPajVV-Sfa7qT-dGWMHNw4x3mkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f09713cb.mp4?token=HUtTowUWm7_Nz4_GqHMboKaEsqTnWIOeT21OvTiPVpKR5GtaVH9zopC8T6475POKuOcNsbSDSi_D6243XJF18MOkAgHDpbq-GJQitTOI-0mNuuKYCwOcbDLnNrNiSqD-lyTEKNLzdQpVFTWGRH_zXGWLwxpZaIVYxgLZOE61fgwRajOcPpQzsWKTlJhI6wvJYTudYokcv4x9Py1sGXS6GIgcdfKFHgWdKoJ2Y56aETML9kKGcD6kfy6nXKLTCj6FidxSvc6wpr-J_8FhVIjg8zQcd01NufwTkB8NkQAjMd1omPIuhIR5928gOHnPajVV-Sfa7qT-dGWMHNw4x3mkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر رضوی، آمادهٔ میزبانی از دلدادگان روز عرفه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/438115" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPR2s48_L8vAVU30MMpQC69a15hM22d4YjQuIyt0cD-0oYrI51_xMPgiAlEoz_lgOU-wBTQrFKO_1w-yX51Vb0ScevVlrFG0BUjQ6Pgy35IfpUlrG-gfa0pWc859JRNcxWcsMU2RAvP2hpIllt06w2c6VFD2cP9plP-BMan0TCAK8Cn4s1pJjGIggKo2VLSYKs_1NApATsjZ0bpWlcPTrltG4gsFDNH23cyf9mwnUOTeaaqKyurbKT1cJVXkjeYxGGgsM79JrnkbzWN_7rgm-RI7GQCVsl_OYaydirNYfgtSIPsDfDkwu6MeGQaz5Ya2mRiOKXyACMtO6Ar2cFHSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماموران بدنام ادارهٔ مهاجرت آمریکا در راه جام‌ جهانی
🔹
وزیر امنیت داخلی ایالات متحده، تأیید کرد که مأموران ادارهٔ مهاجرت آمریکا در طول جام ‌جهانی ٢٠٢۶ در ورزشگاه‌ها مستقر خواهند شد.
🔹
ماموران اداره‌ٔ مهاجرت دولت ترامپ به اعمال خشونت‌آمیز شهرت دارند به طور مثال ماموران این اداره تنها در عرض ۱ ماه به ۲ شهروند آمریکایی به‌صورت مستقیم شلیک کردند و آن‌ها را کشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/438114" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otqkCLnjB1ZHcUCiwcSSEsAUPmtrGrDxx5ZBhKOjjGutpYi87U6dwRFSD5r0LbUOvjHkzWJptWq3VqFCFZS1-o17ZPj_mwGBNiPC81bu66Lx-N1v-3adzOTT-lo9BE3ud8lBUMIpfpuL15EIUc8OHMvkdILLi0HD6MDruWq5EUptpO4ISZL4ex3o4VaZi76oTOlQbQFLaWpBaD1cjGhizp6hrZA8Xq7kZ5eaMeVLInUiSu9k02QsyekFgZ8r0XQlDKesbaJQZuDVe_pPyRpC0qr3PL1cLUiyGQCHFp51Wt7uY6nupj_Y-4OimsspyiZdowtlxGqiIkjKt5w1Ay7nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی عمان
🔹
سازمان حمل‌ونقل دریایی انگلیس اعلام کرد گزارشی از انفجار در یک نفتکش در ۶۰ مایلی ساحل مسقط دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/438113" target="_blank">📅 15:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYe69EDHAlA5MTSHE3nUjDPd-5y_kCbXTF6KShJBNNZebYpCpLwcW_UjeO7OY86Y_WkjV0gScnFZHbUlSN2Lh06i8AkBULxtOXvYt6BerD6wARuI99o2_YCAAV-6wvJnGLpC0X7__ITwU3yzQvSA7XE6-xN86wqMqrnFYr258PBcsL8ysLM4bxI0Ws-Kpep_xnx29eCP9Hb941rYj8BZViuEGwb7nlrc720VM7fGjDi11sohyBV7jEcTIgoi8AqIfBftn--PbPIJVHE7x0f-J6WQEWiGrEERoBwZ26HCkFYDPSz-N5IkpwShWcrGTueyy9efjv2ocZvdOqmGNMvIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان عمان برای رشد تجارت با ایران شخصا وارد عمل شد
🔹
براساس اطلاعات رسیده به خبرنگار فارس پادشاه عمان دستور اقدامات لازم برای افزایش حجم تجارت ایران و عمان را داده است.
🔹
عمان از گذشته تمایل داشت تا بخشی از تجارت ۲۵ میلیارد دلاری ایران با امارات را جذب کند؛ حتی روسای برخی از شعب بانکی خود را تغییر داده‌اند تا کار تجار ایرانی با سرعت بیشتری انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/438112" target="_blank">📅 15:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf6d039eb.mp4?token=dRsH-b2H41H4YhO4svLIwWbG6pBWRWZ_fwBsFFcsKsclReiJ55qQb7z_5a4FXR-jOAQcVcIceBfRibcoIDtn3l8qQs0cFtZJbUHOQutPgHQa625UrgtF62VVSekgdBe1K6sMnavQjPPZnMv9xWwMCSnIslcqpjGH5qHSfPyuVfG3r8rdegK4tD3dAE-wEUsAAqHNaeYXGW_pyoYj3ZSOTSHkiJTXjZhuzHbKUt3yewZbn38-5_gWMrgnT0hnB8HW49HUHqm0ahAY0cEohvrmUsjC0y8ki5ZF8V-PzKfrVMZuDm5f6qZWb3claPtukLh8MAUc0iuBEvZW5W7B6sYiXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf6d039eb.mp4?token=dRsH-b2H41H4YhO4svLIwWbG6pBWRWZ_fwBsFFcsKsclReiJ55qQb7z_5a4FXR-jOAQcVcIceBfRibcoIDtn3l8qQs0cFtZJbUHOQutPgHQa625UrgtF62VVSekgdBe1K6sMnavQjPPZnMv9xWwMCSnIslcqpjGH5qHSfPyuVfG3r8rdegK4tD3dAE-wEUsAAqHNaeYXGW_pyoYj3ZSOTSHkiJTXjZhuzHbKUt3yewZbn38-5_gWMrgnT0hnB8HW49HUHqm0ahAY0cEohvrmUsjC0y8ki5ZF8V-PzKfrVMZuDm5f6qZWb3claPtukLh8MAUc0iuBEvZW5W7B6sYiXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: در جنگ رمضان به فناوری‌ای دست‌پیداکردیم که حدود ۲۱۰ پرندۀ دشمن را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/438111" target="_blank">📅 15:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOaYAqHlFgOVfWQtKtUNw2p8m7OSgHNtNXXWawASblmhOadV_PY5br3YdYIQGMMBSLtTRRof5FGwVmQpB4mIdtKVfIjCnLWhe3OgwwRnbsHvGVLSCBaTYTjMXxMS9pGxxAG8cCfGJHcYYd5nNSAfdAPkeO5ZJeXmweN8zFYaVPQlvytJqqNvomKaOcVK9DHrfv7hyWNaxybqjFz2DFX8b_JAo4o8eCDLieYPXBWMe5EhLXbBCNghJeUfG0uP50nj_CMqJB8EC6SAo0sTvC2uuvek6EBx6uwYn3r-dH4EKdpI8-Cgyx3dEAuj7yDCFlo2eInNJlJA1LREnmvz2vCE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق اروپا در گروی محموله‌های گاز قطر در پشت تنگهٔ هرمز
🔹
شرکت‌های اروپایی برای قطع وابستگی به روسیه، از قطر گاز طبیعی مایع (ال‌ان‌جی) می‌خریدند که با حملهٔ آمریکا و اسرائیل به ایران، صادرات قطر، یکی از بزرگ‌ترین تولیدکنندگان ال‌ان‌جی جهان متوقف شده ‌است.
🔹
حالا قطر ماه‌به‌ماه این شرایط اضطراری را که از ۱۳ اسفند ۱۴۰۴ با حملات موشکی ایران به تاسیسات راس‌لفان اعلام کرد، تمدید می‌کند که به‌معنای عدم ارسال محموله‌های گاز به شرکت‌های اروپایی نیازمند سوخت برای تولید برق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/438110" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci--R8NJzm8mg3p_ESu5CteIXl3kujs7hX-jA-bOG9JAQdLZPLJ3NBhBeFtpEMzzT8n9JvVs_VxcblMnGQBnjGV4q-DXoyKuhkzySsSFR1KZlguIpgf5YX4rokMSNCITSWXEMTf9RH6ckosPMFgq2WnKVg5Q2hnpgzV74uOz5-YRsZjg6RqssTpr6CqqR6-SYOfXEa5B3iuVZe4fyphBLxgGeK1D9uP0dRoWvxAgCy1NsJYEDtu1t2EmR-FCzRJwM_3uLna0HVOG_Ov92yh9RfhqSnG9Bq7k2TLv30LCnye_YT7CFgzUk_e6ruhTKa0IThaluo7c6hgkWNEv29M4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/438109" target="_blank">📅 15:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on6qaVGS5zmz4oogf6xolLS5dvqyGv3WDNVqU6d8XYgbJyAxWFGqhvu1B848tLFp2_ZkkOUItiFTRyThqRhReZCdkswNsbP6cL7mBUp1c1yr_2pLeB9wles6BcFB64ffbD07pmZUYtHR6SHQKCvpjyELXeCK6buHaYwx3z-uVEAh4-UA544JvUT51lXjN1423iKyOz9AK8HNAJKTjfuf-qm4Cx4-1fdTKNxmfasxUrNyvWcxpQcWhx7Uwv9ShfC7WEXPIQXuIfqtrrbE-leFgK3Bif78EQaS1GvKF6PfKMzsUbGMAKSP9GAEWCueKeFotsevmHcDxxjvkBqAZLfU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: یک پهپاد آمریکایی را سرنگون و پهپاد و جنگندهٔ آمریکایی را فراری دادیم
🔹
ارتش تروریستی آمریکا در ادامهٔ ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/438108" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd0a764f0.mp4?token=EaqHjtoIwdkUhp-tSQW3-1F2nJDJ3QfdwjmQGbKOgp0Zcu7cAPi32LC2RI3rBQrY0Yif26xNTkd6O7QtMUJQFdLa0DcvYDKy1RedxyBb-XEmwn9aqP_kDd4VdNFknEfUav2VND1ds5KGC3rbMMChYa_gJmhNPL7R5vGq8kv67SQtdkGeQ0eKukdHsN3XSGoi451dhISnjuH50gR9lP23wAtnHxSUxFuvvIw-KNmH9A7r5hwYrz6COJpvEQgu3q2L588W-bJDmoZ5Fe_1_rDhmVgf2l6xlA-WpcurChZIwVnbCCiq29FU7JdXz_V1TiPlYvkA4DwxAs-He-QU0Y4CXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd0a764f0.mp4?token=EaqHjtoIwdkUhp-tSQW3-1F2nJDJ3QfdwjmQGbKOgp0Zcu7cAPi32LC2RI3rBQrY0Yif26xNTkd6O7QtMUJQFdLa0DcvYDKy1RedxyBb-XEmwn9aqP_kDd4VdNFknEfUav2VND1ds5KGC3rbMMChYa_gJmhNPL7R5vGq8kv67SQtdkGeQ0eKukdHsN3XSGoi451dhISnjuH50gR9lP23wAtnHxSUxFuvvIw-KNmH9A7r5hwYrz6COJpvEQgu3q2L588W-bJDmoZ5Fe_1_rDhmVgf2l6xlA-WpcurChZIwVnbCCiq29FU7JdXz_V1TiPlYvkA4DwxAs-He-QU0Y4CXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: انسجام داخلی مهم‌ترین مؤلفهٔ استمرار برتری در میدان نبرد است
🔹
اگر جبههٔ داخلی تضعیف شود و مردم در سیاست‌گذاری‌ها مورد توجه قرار نگیرند، تحقق اهداف ملی نیز دشوار خواهد شد.
🔹
تلاش کرده‌ایم با رویکرد محله‌محوری و مسجد‌محوری، مردم را به متن فرآیند مدیریت…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/438107" target="_blank">📅 14:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e82f84d5.mp4?token=W8U5Cd12Xkjsm5zU1t08k02IABYSNjAnRUVQK0GHfOT9hBj1HI5Pg9s7e36geZ8hVKOuEpJnsW4BQ0dAa8jUhvJ1iTGME8xzFOtRkpN9A2mI2EazRTVG2cIRTUJ37hJpoZLLYAaxMR5TLCNpF8pvrGG2X-nsgAXzJrEb_iQND1qQ5bZbgye_uoT604GoKVRXFbtNCCRY_L-O3Oe925-nAsYq0_zKuOYZrTmUTeJuDb2d3u_fdBDh370cgjb8zk57JTQLSXqnuv8AgPGqhIRFq_ajVBaUDOv6DGQjAfUVhpvPdUcjXzGVQ1GpzsNZ7zKAhG4SRisbk_lrpv4e0piixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e82f84d5.mp4?token=W8U5Cd12Xkjsm5zU1t08k02IABYSNjAnRUVQK0GHfOT9hBj1HI5Pg9s7e36geZ8hVKOuEpJnsW4BQ0dAa8jUhvJ1iTGME8xzFOtRkpN9A2mI2EazRTVG2cIRTUJ37hJpoZLLYAaxMR5TLCNpF8pvrGG2X-nsgAXzJrEb_iQND1qQ5bZbgye_uoT604GoKVRXFbtNCCRY_L-O3Oe925-nAsYq0_zKuOYZrTmUTeJuDb2d3u_fdBDh370cgjb8zk57JTQLSXqnuv8AgPGqhIRFq_ajVBaUDOv6DGQjAfUVhpvPdUcjXzGVQ1GpzsNZ7zKAhG4SRisbk_lrpv4e0piixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد متخاصم با «آرش‌های کمانگیر» شکار شد
🔹
در ساعات گذشته، فضای خلیج فارس شاهد نمایش اقتدار دفاعی جمهوری اسلامی ایران بود؛ جایی که رزمندگان ایرانی با رونمایی از آرش‌های کمانگیر با سامانه‌های جدید، یک پهپاد متخاصم را بر فراز آب‌های استراتژیک خلیج فارس با…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438106" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سفر به قطر و تبادل آتش در خلیج فارس؛ چرا مخاطبان خبر را از رسانهٔ خارجی می‌خوانند؟
🔹
در روزهای اخیر، انتشار خبر سفر آقایان قالیباف و همتی به قطر و نیز جزئیات تبادل آتش در خلیج فارس توسط رسانه‌های خارجی، پیش از رسانه‌های داخلی، موجب گلایهٔ گستردهٔ مخاطبان شده است.
🔹
کاربران به‌ویژه به رسانه‌هایی مانند فارس اعتراض دارند که چرا باید اخبار مهم مربوط به مقامات ایرانی را از منابع خارجی دنبال کنند.
🔹
این نقد از آنجا ریشه می‌گیرد که به‌نظر می‌رسد برخی مسئولان یا توجه کافی به نقش رسانه در حکمرانی ندارند، یا به دلایلی مانند محافظه‌کاری امنیتی، همکاری به‌موقع با خبرگزاری‌ها را در اولویت قرار نمی‌دهند.
🔹
این موضوع اگرچه نافی دیگر ویژگی‌های مثبت این مسئولان نیست، اما مردم این ضعف را می‌بینند و آن را ناشی از کم‌توجهی به سواد رسانه‌ای در سطوح مدیریتی می‌دانند.
🔹
باید توجه داشت که خبرگزاری‌های رسمی موظف‌اند اخبار با حساسیت بالا را پس از بررسی همه‌جانبه و اظهارنظر مراجع ذیربط منتشر کنند.
🔹
این رویه و حتی بسیار شدیدتر از آن در همه جای دنیا مرسوم است؛ تا جایی که برخی دولت‌ها و کشورها رسماً ادارهٔ سانسور دارند.
🔹
اما با این حال، گلایهٔ مخاطبان از نبود پیش‌دستی رسانه‌های داخلی در انعکاس به‌موقع رویدادهای مهم، حتی در چارچوب رعایت ملاحظات امنیتی، همچنان به‌قوت خود باقی است.
🖼
در این میان، رویکرد پلتفرمی خبرگزاری فارس فرصتی فراهم کرده است: مخاطبان می‌توانند اخباری که از منابع دیگر (از جمله خارجی) در صحت آن‌ها اطمینان دارند، در بخش کاربری فارس منتشر کنند.
🔸
خبرگزاری فارس موظف است این خبرها را صحت‌سنجی کرده و با برچسب «راست» یا «غلط» مشخص نماید.
🔹
بدین ترتیب کاربران با جستجوی کلیدواژهٔ مورد نظر در سایت فارس، به جمع‌بندی از خبرها دست می‌یابند؛ چه خبر توسط خود فارس منتشر شده باشد، چه توسط مخاطبان و سپس تأیید شده باشد.
⚠️
این مکانیسم اگرچه راهکاری برای کاهش فاصلهٔ خبری است، اما اصل گلایهٔ مخاطبان دربارهٔ کم‌توجهی مسئولان به نقش رسانه در حکمرانی همچنان پابرجاست.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/438105" target="_blank">📅 14:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAEBWrvsQYans-BaP7Z-yD7QYh08r2TiJBCVFZ34dTeYVyC6QzO8nQ_jRnGWr7TQPeCSEwd1Gs__w_tOoC3Ul4BMbK_KOmtH2aXfou1lwvrFsJWusBWBFdRdaggVV52AKtimUYW_IWfKr8i32srKvEIXZE0mSCTWxdCJ4XeUIVAICGu--IJQ7QFfGrSX54UpkZiyAGjZDlb19TQzi6x7mVhPMZf8-_LCUkRucE5RN7Z51BS5hwNBjF5e5QEcEu82h9wJF5WKKHrzFcJc_nCb4jiq_GEvW4S50s726AGHcBB4XWF1FXHTC2FS1xzWgBznxa2QzZiOs3vXB2psrsLy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان سراسری برای ندای «الله‌اکبر» امشب ساعت ۲۱ در سراسر کشور
🔹
درپی انتشار پیام رهبر انقلاب اسلامی به مناسبت حج، مردم ایران عزیز امشب رأس ساعت ۲۱ با حضور در پشت‌بام‌ها، میادین و خیابان‌ها، ندای «الله‌اکبر» سر دهند.
🔹
این فراخوان در راستای اعلام وحدت ملی، حمایت از جبهه مقاومت و تجدید عهد با آرمان‌های انقلاب اسلامی منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/438104" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/438103" target="_blank">📅 14:30 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
