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
<img src="https://cdn4.telesco.pe/file/W3ciE8AV0pkbirl9eXVsxWBWZUYrlKYbzvSXY8BN7gA6vvKXo1_7qz0Iptan7W2rIWA4Ml5MlP1OclZJlbEc2k5Twkg9me-6N-id8Uds314pf7Ga3SPxhul9-YYvbZ9Yuf5o33lGwlcs__rnTJo5JVNSm3E8RRR4hucBdKo1_LwRhJGIUzx3w3TuDjsoXG__p62I7qzdDw7Pq-wgHenCvfUjmZHUZKAuX8iYYuDsjfDJxB2h6ErpPzUZ9sqpVPVPoxouNqdPZXvZjPTSUPCwM7T49xlLao4KwWb6d_RJMUVS9NWWS_KJi1lI05dOrHExTRSYMZ7guKfqWLUCDkc4Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 116K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-70762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنفرانس خبری علیرضا منصوریان در عراق که سوژه رسانه ها شده
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/70762" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70761">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
رقص ایرانیان در شهر وان ترکیه؛
هزاران ایرانی برای خرید، دسترسی به مشروبات الکلی و تجربه تفریحات شبانه مختلط — که در کشور خودشان امکان‌پذیر نیست — به شهر وان در شرق ترکیه سفر می‌کنند؛ شهری که تنها یک‌ونیم ساعت با مرز فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/news_hut/70761" target="_blank">📅 18:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70759">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر داشت چالش ضبط می‌کرد که دو نفری باهم برن غذا بخورن، تا اینکه یه خانم دکتر خورد به تورش و آخرش این شکلی با دعوا تموم شد:
@News_Hut</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/news_hut/70759" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70758">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:
ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود.
امروز همان پوشک ۸۶۵ هزار تومان است.
باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/news_hut/70758" target="_blank">📅 17:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💀
این ویدیو از سرعت تایپ مسی شدیدا داره تو رسانه ها وایرال میشه
حالا جدا از سرعت تایپش فکرشو بکن لیونل مسی با ثروت تخمینی 1.1 میلیارد دلاری گوشی ای که دستشه آیفون15 هستش
بعد یه‌سری جوونای ایرانی با هزارتا قسط و قرض و بدبختی میرن آیفون17 میخرن و تو چشم همدیگه میکنن
از یه طرف هم بعضی دخترا میان میگن پسری که آیفون17 نداره کنسله و ...
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/70757" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار در گفتگو با شاهنشاه آریامهر:
آمریکا و بریتانیا نیز، که احساس می‌کنند رژیم شما غیردموکراتیک است. شما چگونه به آن پاسخ می‌دهید؟
❤️
شاهنشاه آریامهر:
خب، من به آن پاسخ می‌دهم و می‌گویم که رژیم شما دموکراتیک‌تر از ما نیست، زیرا به نام دموکراسی، شما کارهایی را انجام می‌دهید که ما از آن‌ها وحشت داریم.
هیچ برابری بین مردم شما وجود ندارد.
تفاوت بیشتری در سطح زندگی و ثروت بین مردم شما نسبت به مردم ما وجود دارد.
🎙
خبرنگار:
آیا اینطور است؟
❤️
محمدرضا شاه:
فقط ببینید چند میلیاردر دارید و چند فقیر.
در اینجا، ثروت کشور، حداقل ما پنج قلم مواد غذایی را یارانه می‌دهیم
تمام آموزش رایگان است.
در سراسر دانشگاه، ما حتی به دانشجویان پول توجیبی می‌دهیم.
🎙
خبرنگار:
خب، اجازه دهید به شما بگویم که آقای کالاهان (نخست‌وزیر بریتانیا) مانند شما در یک دفتر کار نمی‌کند. شما چگونه به آن پاسخ می‌دهید؟
❤️
محمدرضا شاه:
آقای کالاهان نخست وزیر است.
من شاه شاهان کشوری هستم که دو هزار و پانصد سال سلطنت دارد، اما این کاخ را نمی‌توان با کاخ باکینگهام مقایسه کرد.
قیمت کاخ باکینگهام صد برابر بیشتر از قیمت این یکی است.
در گذشته، شما، بریتانیایی‌ها و دیگران که در اینجا نفوذ داشتید، می‌توانستید نخست وزیران را به دلخواه خود تغییر دهید و در امور داخلی ما دخالت کنید.
آیا برای آن زمان از دست رفته متاسف هستید؟ آیا همان چیز را می‌خواهید، دخالت در امور داخلی ما؟
ما به شما اجازه نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/70756" target="_blank">📅 15:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuA_RttHOxXhFgjgOFTkIWonaPDuzIWYsNTTGp0vaokGpzyBV5gpNUbqinaXR9h7ExK48mYkpKZ28C50B9LgL3bwH3PLE-oPJ9ICIXnXA2qLIF6Qb_7CHQoo_tTE0sRm7Cz-Q-crDWuuvgU010PK-1fZi9phGir4wO9eu-iKDUk0SWYJhQWYGf4aQGLSjUUpIsmKISspuJ4W6dpzSbHYw4zkI3np-z5AceoMAjwvvz8IlQFnAaAv8v3UAp6F-C4uKReXVQb2pK09Wthv-VzBzLmVN4uDLJxJuVG9BZZf0ey24o3PjoiDdMPTzu0kTf173W6rHKcEH50cYg4I8FHxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
اطلاعات ما حاکی از تلاش‌های گسترده برای دستکاری بازارهای انرژی است.
عناصری در دولت آمریکا با بهره‌گیری از رسانه‌های ساده‌لوح، سعی دارند برای منافع شخصی بر قیمت‌ها تأثیر بگذارند و رئیس‌جمهور آمریکا را همچنان درگیر جنگی بازنده نگه دارند.
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه، بر طبل جنگ می‌کوبند.
این مصرف‌کنندگان آمریکایی هستند که پیامدهای واقعی این وضعیت را با تمام وجود حس می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/70755" target="_blank">📅 15:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70754">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
مراد ویسی:
۱۵ هزار میلیارد برای شیر مدارس «نبود» — ۱۵۰ هزار میلیارد برای خانه‌سازی حزب‌الله لبنان «بود».
بودجه شیر مدارس بچه‌های ایرانی قطع شد. عددش ۱۵ هزار میلیارد تومان بود؛ گفتند نداریم.
در همان حال، ده برابر آن — ۱۵۰ هزار میلیارد تومان — برای ساختن خانه برای اعضای حزب‌الله لبنان پرداخت شد.
وقتی می‌گوییم اینها ایرانی نیستند، عرق ایرانی ندارند، بعضی‌ها معترض می‌شوند. اما ایرانی بودن به این نیست که در مشهد و تهران و کرمانشاه و اهواز و کرمان به دنیا آمده باشی.
وقتی پول شیر مدرسه را نمی‌دهی و ده برابرش را به بیرون از مرز می‌فرستی، معلوم است که منافع ایران برایت مهم نیست.
بازنشسته معوقه‌اش را نمی‌گیرد.
گندم‌کار طلبش را نمی‌گیرد.
پرستار اضافه‌کارش را نمی‌گیرد.
بچه مدرسه‌ای شیرش را نمی‌گیرد.
اما بودجه هزار حوزه علمیه سر جایش است.
اینها حکومت نکرده‌اند؛ منصب حکومت را اشغال کرده‌اند. اشغالگرند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70754" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDl7C-LJkbnvGt-r4FiAWmycU3aoOxHuoQjHHUCpl24hFvNCAeB_Y0oF1d24fzEnm5G98U2_2oCGArbfqqJJ0MO-UvQ453_C9aUtb6fQFy_P_9pqzc-T7kFNg5cPPLUHImmr9g9Gbbc_Py39Mm3eG5SbrnZdC6ZeGrif9UK0riueeVqU9vRTtnyEnj1CGJW3zn8S0JYuOC1jFpM_Tvoyfcxlpa9T08TNm00-J4La3x-OEZUOH4W5cuZk2tXiYVEyxYDJRGC43AhQlerRkNp8JmXM6K1kMSx2-q8U5ok6RTXz182Cw61Sptwjc85BORPwGSlIiODq6TSn8b1TXUXjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXhG_4bmQI130SoVlqIokrNj0sSmDpQG6yOxQ3C44PMpsB9jVpXW92bUe7wLlun3bh061nIq2bAq5HO8snf1836ZpGJmjIL8uBYd4vo1ctZeeKBPwwRbnBI5s-vjNoy4KfpAdHK022prQEJUWVDSWaYOqIjZuaqiJ-XJ-PaiVcdttC0HzE6SJLHA0WF8oqK0w6JK5ojgXWdqyRLKPjObugR9M0BoEeCkBNYZS09NpRrdUIBX0d35k5VSQkD1FyiePbEX4ssZ-ZPt0w2aaKGD8S_NIDb7eeOy32ZWbSUyYDiGBMPKwte6ymMcSx5jpTVbfJwOPE6hSeGdhsZvVJQ-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9FbQzYNwPvLp6hdzYk0kBbR5zYtNlNsyTI8j0wyGB2KDmZzUdOhibqb519xnwcjNc2yLDyDNvPGL6vgQHuvetkR2CNz9zqxwLvHy8KIDcWiRaNBJKtsEf8MZOcUJkbc-CX1o7HghQHEh7tcL6f8bRXjJNeLPUXp_n-x2L8jvhQxE552lKw_EiXH_cMVXqTM_wloS7RdJtcCjkhcjFzw4XLb-gO6ipFfiejzHuaEXAzxZepbBbmvbAz4hGJ0mPZAvlkSVNc5nbc4_d-nHSjwTOKBS2EPCchajnsY3Iws7sLTLltvX2NGIGGzIr0NGjprSHXSnISI5Y8nTpoOKGa2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALuhG7RHUsoUUxnkdVMNU-5rmfn99FYMAn2AXFYWfJKWnvEcmSVE-c6HcJP4BUdQp4nibvdjB0HLKj9cIBm9dFuMC13ajzoF5i3GUJhREAbOCEVMjSFh-59D7Et_DcNSmAMJX5zAnLn-ymEHkRADJbjYZDjPfJv1mU5GQ_KdrX3aGlyu-onMloRIewr2Kjcs8QMrb9wZ7uw6PzpZcSUvb16YhL1lISO63NLCTf3bz9wZch_YuIbRw33mWAAgjF-lq1zDMCk0ca0MD6meAvMr7cCy6gYlQL_z4iiAIPOSqvtP4AsaFAtkSZQ5_8r9S4wHhLa293TZC5fLBEnjVSfs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8l84jHhem2V1LgwWIUWmgrPZZbV4megoqusE5tfb4Zi8IGms9VaYYyAs3TDvxuedGM8gB2veqOs-dtOP_caUwvBaopZ8W_IP4H6NjlbMbOEaQMz-7V4WkGUuOdb6bayjsKJy2cPihHFFW49aUHmqeo-vyrF_Boytstz81qlbq2c5KxwqGQOenPEtJ3zUtW9xqDbqfvcd5fCaCz4rlwoZMR0EJZa7k8vObyoMMKklvT5a0vH4sb5CajdeoVmvKNl3Hn0jF5m4WfkDQ62gKpy_w8q6AteQm0VDAvWIOSG7GBEPvpqDz1yqBl3VshgMYhgUjGtZue7bbD5mQQ200OFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL6bikRQU5sagSvJ7gkzTMIaEcpmeK6Jg7TIfCG9ThA5lhO3o8KCDz-P2UMVEFUUegA13FBDk7ZvcbtG24H09krURJaZU8Szid_HqlWPxRVaM9nmfgZLderR-3sKv8I9fOnbzkNWaQ3FSJxSMyxKb1-HOFK_1DCRbSefM2hM8FRMYvPSeBt3xK0IeAkqBMHObl0X47wqq6ZAqDpQ6a08kl-Inm3KEz7_tCyfVm7b0tpVtMwE1BSdaj9YakcRBwBCjMl7ayxFf5FRIKmprGgrL1S6SdsipL5mjdb5MHyMx0p1yfENCIazMdySG1CYUgyCGOBDsT4tgllgi5VccieRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRMTPorfJBPYx1kvegtNYB8U6QILwbcO8tsd50exh-jTI5YxcR-5W-YlCdLvtIVwQBYEAvLQv1WdIUiIZGwC3tRviyfO6s8lEHnAmWZcbHUEfNhuxHxE4FcF893ldhTzAUYHFIibJ-KydqZN-66erkpCFUPoSfPF_qSMM3feihFCotMB4JirlS1X-z4H-R8plhh3xW-JuEBk3u9GHd_2LblYxNLVnLLvP7A8SYiRn_oSMOum32Bm6EWpbuXvAcQOyy6z6u26pDDLqudidTLT1_SUiSLPzN0pbxMSfd_Dm6QGc48IBlBETysaa_DURcJaWH0nXaWjVTRlqc0duAX6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYbNatPLoAw2Iv4xQJmPmUDBqJEAy_cPfGKUBzJmjzUotckwRb5MsivU9TUbVp2d0KVR_0PBin9Zk2EeQtWjfOvmHJZF7JjA-WTxxWIXqnAtnZn7JkN0cwr8mxnyadXeNXAfi6qkZD5ihgD8cPDNJHqUjttrB9SXNiIACiFFcm_9zKPxNTxo253g1-HCM1Ue9qQBu5F_Lqk5FSZ16jq2qi5BRMg_ABP6WVjydBqByj1Nlq6Nk6y3vcZ1yLpgDFuzMBW5iIXw0SDO0Jm9c7b-TkWYBgyW-XQcFDD8O1dtmpPd-35cSBw5NnBl9vDp4MkLSZbW8wrryENfKJHySutrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxip_QGJyyBiE7YwT-6XISecUnItXKNnhvs83pcq1lymo5Zq0MxSAwif-nKRfgrTGTZsWpsr_dFmLslHtjaKOb97e7IGeDBJTRG3849eNyu6RABMi2zwKw3UTlKJkd1PfmtXXg_d-NiCqjmxzdnypuxj9mEJEjdYkn7xgjgj8AjM05ZpCe_J_YHsbNeIaUAhQijiR51PFDcE2LoCRRqZeiuB0IGtkByGfr6yAygwVzMUv2nhssWWT9I4KYrPxRY-uF-qxQoanEW5_kBhoDtGVS_xLKzQPk4Bo9M0VxBT0BUy0H8Ru2FKvsprJLUUDJGqOZSBZD1QWpvKxtWiuNbY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIIuOVISotRkYpmTtLPzNk6SsHYfVl7vLdVpSe_vt0OrJhktCvW07EaaX41lgtVTXIyIgwK2b5bp_0htcfIO2GxIhKxt2cKrr0v4uqitv61Ra3FJyEh3vWjKo8Kd5YfPMzRjlq6L8sbdkj0xBFm-EMCVSd6ho_FymP_95S0VEfPexlTNqosLJ408ia-ZG3kKo4ZgthztdC70rQ4zLw8f63j5SPxUMU4CMNtQ2atsYynK727gidS-vaefwmDoOmGf2OfHSo-pXIYTauAbz9hit_15OGlkanatAe3OETbLPg86dtGRj9Iay4YqLVxjY5QLAeedStipGkslO12iAo5bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdv04PC3GjONLIlY5lAw5AwjUhGJkvYam-DBVA-CCCDBc0rxjRKRk3WClJRiKqeIBTmupxw9gzZNTLxwJdkui2CHs3vwrTA1Y1elN7XVQQPZb3_rLRNAO944nf5vaBs6HF4DWvdYOeernh8ly1_HpYKprMn9Nt-x9AKwKw1w4Fkdy-KrAhGnmtrTJI158UYcpJpRmOxJHgZ8y8doAx7WinaG6Sj0JUB6QDyb7FsrnC7BWkeNjMHXpN9THRKe9BYu4AVYKEsmdTZh4HjuaVdENjU5NI7MiVJSdw4bhdSbFUKCxmLslgEuufrUib32Zjwk7yCourKcn_mtZoztvyFJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Q45txNhNjUpJQfWRk_Lf7rDCGSbuFEs4yzwPyTv1NaMYJF0eaGp07ROgwsXJyTeACML1glPWNS0h05gS0_K7HJYy6IplElDPeXOdReDpTueswN2Hy11ogdfjLXg4nTdMd2jtH-Ag085U67xYdATLZOZeAbplKtoW8KTH8fxaRuUF5-7yOM4wHZIt_QriZRmJ0xF4skoAi2LjlI2WTnjQX7Gs46LE-QH13EW7FmkT0kHgQW-hpDUlXNl6zlO7RndJ7byjGVr0FkPrpaxkI3sxaHyDfr8KvdmxH3nnJKglx2trjP7QQJWWdOGxLjFRkOPHT330KVSwFM0gxjqFuh_rSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Q45txNhNjUpJQfWRk_Lf7rDCGSbuFEs4yzwPyTv1NaMYJF0eaGp07ROgwsXJyTeACML1glPWNS0h05gS0_K7HJYy6IplElDPeXOdReDpTueswN2Hy11ogdfjLXg4nTdMd2jtH-Ag085U67xYdATLZOZeAbplKtoW8KTH8fxaRuUF5-7yOM4wHZIt_QriZRmJ0xF4skoAi2LjlI2WTnjQX7Gs46LE-QH13EW7FmkT0kHgQW-hpDUlXNl6zlO7RndJ7byjGVr0FkPrpaxkI3sxaHyDfr8KvdmxH3nnJKglx2trjP7QQJWWdOGxLjFRkOPHT330KVSwFM0gxjqFuh_rSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBukELYzx2IdUjnnqwG7qg9Zc9zXz0MbpmOG-v0w6M9rdSLH8FTXeftMPl_AyM51b5G4Qsgv4p0ROsFknAMR7ckOxlkrmerdFLMLNQnR29JTKsVHIcU07EjOzeM73ZiQAAw4aPjV1TkWlmrTadCuYM0cUnrgW1cE42WnZrMdH5flmgGH4pTMD8jEH8FTLyp-lHb_sc29H3WzWWw1djDv74GnrPP0oBTfCFiZ6Poo0dgq7vOrOU6EniEaiHcooeuCF9WFDyWbHdSiik76bBsNCoBJeHsumL29vta7Q6SjCTP4Osymjt1I4nevsZ0oW0QX2wvwhoBU62-1ZySJBJ7VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=D64-dFVhVcSo9qyhxO3_d36Ij4sl-nSRZ2oTUIIlksgH253QuHn5FWSKe1h-YDM1_vBZonOqinGfbUspfQka9--8EJX5tzQBu1rYtbkvuzb5PkxDORF_Ywqmeu1oZwteBzFFJhmiZefsPSbwlH4Qihj0COcOZpTe7WQL0Ecm-Kc1eacFpPu1575Hot8T0r0aqZoCLIklGToIiBh_GvmTtfK__iCIsXgTE_bcdLxuIHi9KPcHTOuL8L7i-7Cujq2hIWBVuzBZG7-XUcx8KIQDkyeEK2GNslrgGTAJEz2KhlR2vu7K0NXEl4nHZz6e9hqFEGQulDnYzxyLVDt2UDboSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=D64-dFVhVcSo9qyhxO3_d36Ij4sl-nSRZ2oTUIIlksgH253QuHn5FWSKe1h-YDM1_vBZonOqinGfbUspfQka9--8EJX5tzQBu1rYtbkvuzb5PkxDORF_Ywqmeu1oZwteBzFFJhmiZefsPSbwlH4Qihj0COcOZpTe7WQL0Ecm-Kc1eacFpPu1575Hot8T0r0aqZoCLIklGToIiBh_GvmTtfK__iCIsXgTE_bcdLxuIHi9KPcHTOuL8L7i-7Cujq2hIWBVuzBZG7-XUcx8KIQDkyeEK2GNslrgGTAJEz2KhlR2vu7K0NXEl4nHZz6e9hqFEGQulDnYzxyLVDt2UDboSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihDTqkgWBCgs8NAOGJoebG_rQDh1n4KP7tR3O9sAyEabV8pgLB2MvHMXmXdgpcbbb3yS_SXP2gkd9zUL-3o-HnN3-g6hk6LGZ-GsDdmiDN6y8OOCYcz7514PHe1fQxXdfvdtJC-LE-zDtd7PYAQppBnPu4gOjPtaf2rPNcF3hrm7Z5eP08ZWGmYCkW56UK47kgTAfKfyiXcK_SfNpOTjt772spqQ605FZDloj3yoPd-OePTm0AYD9mwk7hIWrBCW_RAEhwqkwqmwBGb5XUwyKCEaAWqvtRNewVRcvEhv05Dwfokt6flJ9qTp5f9bRNngeh8YPo0DrlOX4YP_AOw8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APNO8DkGLHkYgx1Vx6ZUwLkKKhqBHfS1nYhjM12wmnP5IzikOzLPnNn-cwc-cIUJs4ChTL6W8ThvT1BxKeJw5lyatTN9DYwLuesz4AfLQz5a4uYK4tOBVpVXKy4Q26ijf-bszKfQ3V0m-cs8in_y6TmLwhltjBfUIa-rIGZ7G6ovSvzVDDV0uPa9NyKfHpUGrlV7DHN3n3hCT4SJC50qUJlWbrqXFQ0ZyJipVmWSz2HlR0EOgOeI_wYth44iqC5p1_q2_2J3oa6dX8MS0lDch4OqvvM69EUfm_uwDLLSsqbgilqb38GPo_c11DQbM4ZxtndO3aRRQ7mtbBR2AyibhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n8mpn_ngn5oIDq5mwRLM6MnIDyKsT2i7Ah1jPHNPaJEhEtK2kqPl8gWykJB_TKtAqMRZHLa2VFxswAlG2NrWjZQo3YwAxTqBUhcR-tQVoWrlbz6cBeH1ZufOkWAeptgPZnHmC_IDC8qOjVgCnd09Rqy4k2wCwj7b1MXhSABqXFSKW9wTCJu7On4eQ_Y-_Q2anHijd5C7GPP9HfPqKHrYfJ3S1oKjK47br5XxBwiRnXHKWTonkrsSazHl8-5nXyq-rTlptwDN1fQbdyP4FpJhPoFi1TVRHkz2naQBFVUpdSCBHskg3pCA1HwNF_60PmM1YvdahID6xPA8TDDDvBBmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DSWVMfJf8FDEOChwEyHCeYj0JB-hXeD4akGsMJG43b1lKRuX3gyfvnHFja22Nd29wIU9QvZRVZvhU9Ecw2Marn6BTKUZGWsXC9s1_NOYyo_4zAGD1G0deYJcDDREIf0L5DvOZEvcKTDCrF5wg_FLoS8zXVYwBEqxdest2L7vRlzybLJbaFwWf2gfIAWiYbPU9noWW-UbfDo0AanT5FeIVU3CC2dAz-n-VT2WX4Bjw5JloGBT6QK8kdR_dpfVrqmNn1Dh1FcZ8SQDTV-PwojUlxKrjq6rvJolBzNoocUxkAvJ5KYfZxroVzbu42TqIIvCpYfua8Cpj5FucaKzs6W_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlLU7O24PnSyWbNVLwD6pCgezTIKQun4GvkzqmV3ZL1i466hBj-ZJ8BCsXSagHTwd_-lHjkP_drIDqd11rSRc8X8G-zXFVBkpjZJeWtt69pjjfYR98Rzqhi8YCTOsZQgjQX6aH9IiEHPb2vyBSp0GEVSu_OfD4YU_ZUbHcARb2gHFNhagcAOZc2L-CrsW69z9en0osQeLvBzKjP8_VbeqMV-SnIkgx-HE3_PM4YUnlKpUkgkxiFqmzhlpW3HuSF2LPshhT6OS7G7dtNoDFxWg2R9uOl1zRYqljYCVLdMRUKcEL5_7gUJmatCg9M4SOMV9i-xuE8LRGU79UTN1ROmuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5SOjpSwlLfE6SE_cPqUGMHfyF70JsZ7UTKpq7Y2srqehBPlspixR40GFActOO-Z1oJmrZn4sVFufwttlwQ2BNXUZRkupA5IHBZR26nF6s2WoUJEi4VCtQBI5q6VDJYunmu2WM5JLmYlgzuhvXu5f2Xf4Mn_Yic6In_7mTiAqfgX7UH8hp6A4fhi2hcdAB6tWt7h6tmZPc12X6kEL8m7l_1TvX-pQUe5zecL-pYN1RzL8sTmXlFdcC7WBVFCQtxi8AMxqTRgDWa1fgkqfJmPY-jLg9alh3MkS6HMNrEYwjreoU9o_mzqUJjfPMHDe9UCkdOVtfuRHU9erBvDEnATIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=HJQWCwyGQRyHJaP7C9X4vuCZnVWyl4y_OkIgXOKQ7qBV_M6wUb6SjrZnTGjLoPHS10YDnuaJW1l_JINgCOtSEZUI5axPDFtAL02cE2IOnBz1eulJuQURsQ6O74w_or_JjGfE60vgg85op9yGjT2NLwpoRPa2of7nc8KNcrouoHF7rwmOMiCbh3yNB1RKdF1EPqjv-0FbD1PRRYuTGmpre0XKSNh9i5uW_6a3EpFvq-AXeeSvizxQ10lGyb8BP4xGe7qg2DAJi0skzxqHgw0-aw0cvT6uarFBydF7U8jJby86DxIDckpGhmLbFYsXMbk1BkZXdJUQhh8K5wo5e9NR9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=HJQWCwyGQRyHJaP7C9X4vuCZnVWyl4y_OkIgXOKQ7qBV_M6wUb6SjrZnTGjLoPHS10YDnuaJW1l_JINgCOtSEZUI5axPDFtAL02cE2IOnBz1eulJuQURsQ6O74w_or_JjGfE60vgg85op9yGjT2NLwpoRPa2of7nc8KNcrouoHF7rwmOMiCbh3yNB1RKdF1EPqjv-0FbD1PRRYuTGmpre0XKSNh9i5uW_6a3EpFvq-AXeeSvizxQ10lGyb8BP4xGe7qg2DAJi0skzxqHgw0-aw0cvT6uarFBydF7U8jJby86DxIDckpGhmLbFYsXMbk1BkZXdJUQhh8K5wo5e9NR9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMetmc87nbCc5ysb58-Sh7DoPZdmMPg2Dlh2eCWVqcrfCj7dMYFYtTPQbDPVKXbt6jacFSTcdT42V0myWlTcDnaEC6oQbYmR0a0AwaPEEIIOsyRU5Z_E8ywohE1BIjZMyWzbLbzy_6NVi0qFYNmSueH3C4Z0hqQSlO18IO5elKyfHxmxrqiugJbXy5fDq8Lbiioao8zPUwc7oN1C0xmERu_dPJuJ6mBPFKCe_BFYgioGxtWSRUyD24o-XxtviL9wCxzyPyvmfPWf7C52FsZuIq5JYu04FeourKPm5hVZ3vmLvPuanrVQm97oGdW1qByNB9FwjQCgEWz4efK_BoHWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7PgVNswqTD7mlDW5khQtTPeKH2xY4M1Ll6xHr82ubhMnkZb9IJfD-x6fWmkcMZS9doFxqieR90X56mbR5KcNSuaUmxLIFzZbj_q0XrR58vxXNkmlNJ_CsyKZBSbsf58mxqUZktZ6HcFtFUIo0MwqTAwE5Oz4ne67xB7sE03GkIpjf0J8OLfTgCJDwzX-pqmv2yXYtWWiHU6FO6hqeEhnkyexEuX5SdVnieTqojrXwSg-gfsmH5S5C3At64BWCMe_sNg0ImJX5SKe-3rjUDxHC6ofvMLEPZSrBMmoxYne9iZOYM5bn4n2zecNLZqlTYaL2y4noKqqEjW5YqK6h3SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBw2H7QKmrDIPMsqMwX2G1cUISOe55t3vvTgAmsZ4XpjB0xuUy7FUOySL5t13ve-1-fm6r3gf4iwEfLK4-e8yy9EPPSD9WDRLONwSou6VtVjQ06UUlYDMaYofBUhXTWb0yTrrk7TOAIu2_ugS1q477wbeZ2a4dxbrFn7WbTC5kr7F7BGs_gMS65JMMPi1RT956wlCJayI1tagKkUM1qShNaZUtsMDgU5-R-zHSBpLTvGDrln3TP-KjONXwUFzE5mHtK1ldp6P0xEDAKxUtOoDSZxb_cC757TOIlZbLGnhyW3jCSZ37nGmdrpFCTfhUSlBj90HGErfePX3wU02bF0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeEHR9qzZJrzppRwKM4aqkC0k3_C2v6uw9Q-egnWVSTOhDDoeR3qhXTBnjGWXEasfrTyxgVNZvy5cIbt3iWa7-bykqf3WYVDhfffSoGXgpa-yfmYkew8ojwRcOvvnL2czzl_kvZGuQHlSakKddN-V4wiGVUwPfaev32zkYTHpZM87bhagk3qt2BzenP8xYaP-zS1bKI9TpV4wczXvGRi-9ltYeXUhjEZoMRfdnBk08dBN9rUo-LO-CjyB2WFh0o7dA1GTqPd6HhFS_CeDreS7SsEijExqe-Xl1dHgDKSiBgfY_Z_0Gl6bwqTgmxpLG4sJRA_KXbj4XIaaVCWyM0y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXRXdJVp4VnLnE8wp05n2-_agEFmzP7324DbSu8g64zovFLMR8i5sZygOE2gDQEn6jICJiXBFStLts-oRStjaC-WzRkuAeOwV28XRd_XONKUatDun6KCuffyfZjq2VAkmJfh9yTWV7O-CiEl7ORjfjAoV5RqCg_Dbi4YelVYtffHxtg8ZnqbQEp0TG3q_Qzl-AcSuJOxSfPjsCmPwJTr4E2L4kYhfXS5jvYW-8ksIeV4mdB3QsJsdWfAwypebmP1OYxkeaIoaVn2etbVpqgehAG_aWow5-dkfcxg8CxIk0mgFgVW-gpw65xwGvuIiIpRv_P2CASOXPBe466kgt1klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnoZ7seP71U-eQIwXsQI2wSJ_a88-Q7Go6EOMYOfz-uRaevkA55qT6y3tkZuWWdW1PxERi0PRMypFM_1TO-tEP4akTiR8XY3nK3xODNmFVJ7OIpwA_V72ybL7vAHSfMHAcQgON3fwXGVoR-eG7rXd0ncfi5xTJ5eavQooYrQz5zRiDVu0ngIAvx9WgTT3-saZKd_g5wkw1r0utOG4SdpkQdBU2lp-3MHLmKRiwZk3bojde5CTlm3NImoV8QOmLvH46So2lSA1pLfU2ej3hLSKmBN2Yf9s61iaeyaD096bM1QRv4zE-6Oqj_dAsIp3F5NxVExVHyBAOsIsqNxdYaR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=KgTp4eIgel8I1mMLxCkwJmlE81_Hwgfjqa_zaNn3aUo5RlGIPCfxTB9etKXh5lCpFmgYuhKkedMywrgkNMwZazY8XvQ5tGB1XRJyTu3uzaMVTmbTaPsGRYrsl_ku6kUKznBbMy3POMa1ydpNHKZMkaeMYWl5DQ5TMHEzzD_6IKtNqLZOOLDzW4PkbWZWyBwVAsnIc_UFwZV-vB4usgMIr-xc1vCnfM0kODCxFbb0K9OpxjjCvdslCx8LxjSY0BYjUAh1DCiARxAsm23iB8FR7KGZIsJUhxrpWKKnvgyrAGlKRhhvLQ8g4Tqd_AjtWi7C_gtoUiNYrPJAWQD3tSYC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=KgTp4eIgel8I1mMLxCkwJmlE81_Hwgfjqa_zaNn3aUo5RlGIPCfxTB9etKXh5lCpFmgYuhKkedMywrgkNMwZazY8XvQ5tGB1XRJyTu3uzaMVTmbTaPsGRYrsl_ku6kUKznBbMy3POMa1ydpNHKZMkaeMYWl5DQ5TMHEzzD_6IKtNqLZOOLDzW4PkbWZWyBwVAsnIc_UFwZV-vB4usgMIr-xc1vCnfM0kODCxFbb0K9OpxjjCvdslCx8LxjSY0BYjUAh1DCiARxAsm23iB8FR7KGZIsJUhxrpWKKnvgyrAGlKRhhvLQ8g4Tqd_AjtWi7C_gtoUiNYrPJAWQD3tSYC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=fR3uJq94M8-SoT0jaDc9nbY9pMPDjY1r9Cmj6fz1E-9RovFsqCZzxilhIdz4oTGzEa-I2c2Qp28p63a75iDf1jizUGWWcotzy9n1OMGSepaFHMoIV8Za92RFVg7d8FBTda9sPweDr6todju5vWax3gB3tOcnSiM2zS-_I8otzwxkXyAzQv7J9-1bZKhsDcN_wWauqwmSx0KAxY_GwSVZFWFO7GUgy6CfyGtS5w2WNVal7kvsn1xb9E-6wS_vhMTlDTD8QyfxFBeZ6v90ymKIc7-NmwQ964ZJYEtJ2nDUY8Ac3rU1rM02gGmwqvhbPQp2o_MdWtoNQIoCJS6NXLbxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=fR3uJq94M8-SoT0jaDc9nbY9pMPDjY1r9Cmj6fz1E-9RovFsqCZzxilhIdz4oTGzEa-I2c2Qp28p63a75iDf1jizUGWWcotzy9n1OMGSepaFHMoIV8Za92RFVg7d8FBTda9sPweDr6todju5vWax3gB3tOcnSiM2zS-_I8otzwxkXyAzQv7J9-1bZKhsDcN_wWauqwmSx0KAxY_GwSVZFWFO7GUgy6CfyGtS5w2WNVal7kvsn1xb9E-6wS_vhMTlDTD8QyfxFBeZ6v90ymKIc7-NmwQ964ZJYEtJ2nDUY8Ac3rU1rM02gGmwqvhbPQp2o_MdWtoNQIoCJS6NXLbxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=WklerUzBCsHKFgnSomgWmr8EW4mhIrKQfXy__DB2o0ro25gL6ZGcOIvjOlBv6u2fsUj5qtkNEs1b5ZHJYzP6keylmeefWCzDkHcuyCBsUn00qEg5g_VjdVd3e--5_OSxcVf4QiBvvVzwNV1hMuid8wP8qm29oAFcsUvZsYB1ZE9ZITf9QFw1yrcge_NmaNYn_D7iWCTd1RkLF9uuBaJsSv1CC3HokXuh8ixwFvutPudyi1153u4UWR_PHCwrbWAvCoUupqfJlONbO94K9aUAjDGXeelR4qVayrNyyp92zGn34nN0HA622qmGWC_BuOb0iKuqFZmzkp6QYUd68n0ZUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=WklerUzBCsHKFgnSomgWmr8EW4mhIrKQfXy__DB2o0ro25gL6ZGcOIvjOlBv6u2fsUj5qtkNEs1b5ZHJYzP6keylmeefWCzDkHcuyCBsUn00qEg5g_VjdVd3e--5_OSxcVf4QiBvvVzwNV1hMuid8wP8qm29oAFcsUvZsYB1ZE9ZITf9QFw1yrcge_NmaNYn_D7iWCTd1RkLF9uuBaJsSv1CC3HokXuh8ixwFvutPudyi1153u4UWR_PHCwrbWAvCoUupqfJlONbO94K9aUAjDGXeelR4qVayrNyyp92zGn34nN0HA622qmGWC_BuOb0iKuqFZmzkp6QYUd68n0ZUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_phfk5jE_74mVjiaDGt154IEeY5XjbmKytu_nU0drNOlITT03H6KyoOIb2YdRTjMsiqb76mdP38Lnc3VJyXvvb0JrdQ_Vb4T1W8Q9r3kopRZHXP8UEggU6ULbF8EOCTlPgh7Ix6Nw23ulbHl5SGLaAwec6Dz46oCvJWHk64KSZjvkRAzhuc70Fo6ZC0ixDSsSO9m4u6dzsA5c2lRtvMkfBVFhSzUkA7ci9SRbDj4VwGCEYexzSsbImpJv1KdnLBwGqAqWHZlfwHXhnja_PFk5oOncTdlvsuS5vbNVbgDfW4f6vVD-NjxqDCOU8nQAfsylkjdP8QPSqlimDt4fj4IpsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_phfk5jE_74mVjiaDGt154IEeY5XjbmKytu_nU0drNOlITT03H6KyoOIb2YdRTjMsiqb76mdP38Lnc3VJyXvvb0JrdQ_Vb4T1W8Q9r3kopRZHXP8UEggU6ULbF8EOCTlPgh7Ix6Nw23ulbHl5SGLaAwec6Dz46oCvJWHk64KSZjvkRAzhuc70Fo6ZC0ixDSsSO9m4u6dzsA5c2lRtvMkfBVFhSzUkA7ci9SRbDj4VwGCEYexzSsbImpJv1KdnLBwGqAqWHZlfwHXhnja_PFk5oOncTdlvsuS5vbNVbgDfW4f6vVD-NjxqDCOU8nQAfsylkjdP8QPSqlimDt4fj4IpsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=NDIEs546oNJz2lxtBFv4HLs4Skiq9Pnn-DM2uCOsht2t_qIQh-tV5ual1CGG_iHgl2DE2v8uGn-JEKR5fQPs3NVfB1ywpgdjtfPvbHdnsNzRbUQNUj_1fb84SFd9B9CElglcjCO900HQu2RWcBjwy4wxAo9NyqGrKrDZrR8Qa6l-aOy4B8Htnhy5Y42mWnJo7xKBmx4JYWfigHS_McKmc-73zz_jPHvH1yZEyLt9nIdIZRzBKTWK_VSMz4oqMFsHTUngUidUQ-94Xm_PdZqvRSNEd8x4RQo0noeMwWriDAVUcJlWK141eVvSA_tu8qxMXXak7gylsKLakdOVrhWVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=NDIEs546oNJz2lxtBFv4HLs4Skiq9Pnn-DM2uCOsht2t_qIQh-tV5ual1CGG_iHgl2DE2v8uGn-JEKR5fQPs3NVfB1ywpgdjtfPvbHdnsNzRbUQNUj_1fb84SFd9B9CElglcjCO900HQu2RWcBjwy4wxAo9NyqGrKrDZrR8Qa6l-aOy4B8Htnhy5Y42mWnJo7xKBmx4JYWfigHS_McKmc-73zz_jPHvH1yZEyLt9nIdIZRzBKTWK_VSMz4oqMFsHTUngUidUQ-94Xm_PdZqvRSNEd8x4RQo0noeMwWriDAVUcJlWK141eVvSA_tu8qxMXXak7gylsKLakdOVrhWVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ3dBKSxPqfftqIjQzkO2T6b6112Tmt0FknuuCIU9cOBfi_LKEK6QUzqH2K6rXzDPx_XvNuhC7j8BgudkG7KAbqWWO6VcmXfWrgDWK8eu9lNLeFgHLZ7HrXMomwTvHu-pRfXEGPj3q5v4UlM1fZybPU7BsWOGGIkpCaWAiKguNLulfwBIGFAZq-ldNEokGJBL5xX6umZ__QBEal-TEMKYrNTi3K-A9nWDlQir1CNNSxvFcjyweSo0CrVcVWDwgNhBeeMUZdu_GNhzIscIX-BzfFHDLYzYGDM0v_nMUi0B3LCcZVpAREsPS3wEi5rkpFCN5UOusvkf7GdY-aShJ_2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpjwVPNlCSB6xVY-3fgCDFiuBWFgvJA_0PiATg2_YaceLy4TIA75y2v6xxNp1Gfltk9qz2qyQ8YpAZrwLXpmseS8QgLk984jYPcjGT7sdZKlsaD-p3EH_bMULJ50KeJHmhw2T2k3EJQdOXp9NYm0jtQlsQ9dZDJvkp--_Pv7SWUJQTsJa945X-f5BV4DmU8svczXfXZGXb984-5fDQ-KJfw6eCpT8vgubdwOZOlfNEgNhjPlUWUlg0pBeaKNZQts65ZbtCJb-Z1Fpbtaxja8TuC9lnZtmn1vOjFlX8v7RWsv3JWfqruyS1vKs1RQOj0XP2VE8_txyg_n0Xrmkiw-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=XA0r8UQD7qfhgDjJvQWSlVoweTMBJ4fCjC2Q1quv06UPL0AIxNIQEBz_1INpxuiTi7xQa_dzx81t7wQLZR7pP8rCYHCrwuTQ7AKirNyddAzsrOyHrIMxLoLOsP_hg1fpyt_djUf552P_Rbnq_mjLl09tdxseqr2fD-Ij7hjtIkLvMTEHCwiFCuA5YURxad12tcpxLSmnATrn4P-_0NG1kHzcSJyG6-LW94MR71DYXXqtbDBfMb0MhyYB2DZl_gX3j9WhehsLVHjZ4yPstbrNGctwhPerFlZ9qZA5X__h1ZgAPTCqzz388AwI3_BFA02woh4dkuo1YDuXnjqvxw0iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=XA0r8UQD7qfhgDjJvQWSlVoweTMBJ4fCjC2Q1quv06UPL0AIxNIQEBz_1INpxuiTi7xQa_dzx81t7wQLZR7pP8rCYHCrwuTQ7AKirNyddAzsrOyHrIMxLoLOsP_hg1fpyt_djUf552P_Rbnq_mjLl09tdxseqr2fD-Ij7hjtIkLvMTEHCwiFCuA5YURxad12tcpxLSmnATrn4P-_0NG1kHzcSJyG6-LW94MR71DYXXqtbDBfMb0MhyYB2DZl_gX3j9WhehsLVHjZ4yPstbrNGctwhPerFlZ9qZA5X__h1ZgAPTCqzz388AwI3_BFA02woh4dkuo1YDuXnjqvxw0iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHY-xTQk61Reelp9A5ZYb3maasUaxrzMs94SdGt5rTLUOacj0BpksIvROIeAd9SD7t--vSgF-7Ucp6O8MqwY12_pegoCYPw7CtHZ-lf9-ae0m29DCpyXcyr42Iin4ho4z006rwBx4dh7--rXzR1Gc1kTDl08ezdSl_M-NgMvNf-dn-v9A2WJ2qSdQZ3RBnzcyV6sZdeWURSLosr-OxYG5EKVm8lz0n-32OdYPfgoQ37aklEzL_aDN7jDU6Y-m-NxPLgnQfdAFHPc5m6-Ptg2vuQeEzMQrD91MF7cMVzHw9a0dNw94GtVSNebyxYeKRmsLDTxCXKYyJJwm582uN9FRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=fjqRRwKkXEbIz1YYQlA-j-Ga9CcXG-fRl2Tc_y-o350PQKhuj0i8BBXadbOTgy7h1vNzu8w9di7IZvXdQZIF1RcOc76owzVQwhKHyHl-vDw1NAb6hQrexu_yawBDk6IzfxEd-1AjJsLt4KIUgRjjh8o7JTxEpA3N3-dDfmlqc4o9DWkRMCeFGsO5gYlg5Yy13EZl15V2ciRWDAa91MJgs4JsUasAqhr2g0Nu4KX2R_ab_H6hdp9E-_FUhwOonqytz0FQEsfVk0ewro_GCVRuSwZM8go1nkLuCuLVKNGq40O5bmxiGnxHw3b4qEJ30Q1g69i0VMHVMNwphWMQ401rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=fjqRRwKkXEbIz1YYQlA-j-Ga9CcXG-fRl2Tc_y-o350PQKhuj0i8BBXadbOTgy7h1vNzu8w9di7IZvXdQZIF1RcOc76owzVQwhKHyHl-vDw1NAb6hQrexu_yawBDk6IzfxEd-1AjJsLt4KIUgRjjh8o7JTxEpA3N3-dDfmlqc4o9DWkRMCeFGsO5gYlg5Yy13EZl15V2ciRWDAa91MJgs4JsUasAqhr2g0Nu4KX2R_ab_H6hdp9E-_FUhwOonqytz0FQEsfVk0ewro_GCVRuSwZM8go1nkLuCuLVKNGq40O5bmxiGnxHw3b4qEJ30Q1g69i0VMHVMNwphWMQ401rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=JsvQyZBxxieEDgDs28jx6QpKW5H9D58tg9sPCHMNcWt2GPvUrdF-wnNB31H_eBLX4KzGtgAUuR2mBr-YID3avTfiBPi_1_D7Y0BD9rIdhWxgVzJKCl3TX-JcPsyL65LPy7huVM0Ubozf5E8b52NtxorCFShQYHHH-ysQ2qPqlWfgWuKEpQLUAR6dXbmLTpISQs3bmul5LAh5ev9qMbRxAEZ4xLujsYQ_uNG_mUfDxhZbb19hoX4OfW5hLcqLLxOvbVwkK91zTxkY5MhX-sS42nzNzRU9E-3F2iWiC8fb6Ibu01OgGbqh2OvtUPHuvboneDNSPpyXWbDTslzmEbG5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=JsvQyZBxxieEDgDs28jx6QpKW5H9D58tg9sPCHMNcWt2GPvUrdF-wnNB31H_eBLX4KzGtgAUuR2mBr-YID3avTfiBPi_1_D7Y0BD9rIdhWxgVzJKCl3TX-JcPsyL65LPy7huVM0Ubozf5E8b52NtxorCFShQYHHH-ysQ2qPqlWfgWuKEpQLUAR6dXbmLTpISQs3bmul5LAh5ev9qMbRxAEZ4xLujsYQ_uNG_mUfDxhZbb19hoX4OfW5hLcqLLxOvbVwkK91zTxkY5MhX-sS42nzNzRU9E-3F2iWiC8fb6Ibu01OgGbqh2OvtUPHuvboneDNSPpyXWbDTslzmEbG5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyqsBvkT--0cJN0aIPP0jKq4A_y2NfLIrEoDJIgc60vFrYm0-S1gXov6H3hlgCaBqHwQQ7gLd1qAgVTN5PQv8T3is3204XnqDuoaGepzj4iSK2TWvvqvN9IEjd3ELJ2INURFEHC8mdRUkh8jP-ItZD2Lb8ec4Dhur71VZDBLbxM4xRCnLy8evRw2oBgAbhKKGXRUVWFKuPLsazWct2CITQouq4fgihomkH0DZofBNQj-2TYMa9JQnElu0PkOYHQPiUc-Q78bsJFp2aMu9kJNT6DUeRgyv68eF8SCoxinLuRYb0eskaWYs2Gdjw_3uY-BA2kcaQxD5AI25hDituWgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=LkYxFbkUhwpfPS7QqG6kadf-1ddjK3huSOB2xabj15BVAXRb0kHRq1c5_8lCs74Dv9T8y54Vm_VFt6SkFaz_F7RkgcdW-Otk5G_HIaUXE2NgjNVqhEZDDRIugHHTYIUzpHaVaM_mMtYrqBKGWnewJVmsuJI9zUImv8kl4nv9zKNwnqfwxOnFAal30x-C_0H6EwWCw3EIDmbbIiOTRPAK1rxq_jyfHAnsrJ6ppFz1tn5c2LKXFWd1MqXls14mAXSBqH9J91uljthu_qepga3g76h_zKNO-o18LFoxDYcU9yzlLFCPaGgIb5Jk7fAymeUZU0F2zZAKyjvbynMDCuStWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=LkYxFbkUhwpfPS7QqG6kadf-1ddjK3huSOB2xabj15BVAXRb0kHRq1c5_8lCs74Dv9T8y54Vm_VFt6SkFaz_F7RkgcdW-Otk5G_HIaUXE2NgjNVqhEZDDRIugHHTYIUzpHaVaM_mMtYrqBKGWnewJVmsuJI9zUImv8kl4nv9zKNwnqfwxOnFAal30x-C_0H6EwWCw3EIDmbbIiOTRPAK1rxq_jyfHAnsrJ6ppFz1tn5c2LKXFWd1MqXls14mAXSBqH9J91uljthu_qepga3g76h_zKNO-o18LFoxDYcU9yzlLFCPaGgIb5Jk7fAymeUZU0F2zZAKyjvbynMDCuStWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=SP7Ne_EEWoxWR43RR5MntMYfiKzasQWvqql_YXZ2Ad9H2adjO0EstVnkCipgWSWwE1Eno1JTccMvM3-Ywd79q-ywK4zW4P2esI4yxk4l4mlHXDR3l09XcoJvCr04fJuBYiXtWvIxlsL_lGLoj9t9TWwVWVqNijLxyhUMwGjHTfdN0D0v6_WgZbSLoyJqCbVF_JI6TqnIEVBhqS3IDB63vf8IPKVGADpd94pIaFH6kHOjh_QRKPf4nBs5OaCSFTvPFmzAUdcWwkW5ucN3rn-p5Vpd0FtE4n93a_Qk8IRq80opM4j3-ZLdLskNqkkLvqWr0EVEFGdRBIdIlmYZRyj5eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=SP7Ne_EEWoxWR43RR5MntMYfiKzasQWvqql_YXZ2Ad9H2adjO0EstVnkCipgWSWwE1Eno1JTccMvM3-Ywd79q-ywK4zW4P2esI4yxk4l4mlHXDR3l09XcoJvCr04fJuBYiXtWvIxlsL_lGLoj9t9TWwVWVqNijLxyhUMwGjHTfdN0D0v6_WgZbSLoyJqCbVF_JI6TqnIEVBhqS3IDB63vf8IPKVGADpd94pIaFH6kHOjh_QRKPf4nBs5OaCSFTvPFmzAUdcWwkW5ucN3rn-p5Vpd0FtE4n93a_Qk8IRq80opM4j3-ZLdLskNqkkLvqWr0EVEFGdRBIdIlmYZRyj5eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaGdxdljbjId25Rcrz5IuTSn2E8YYzoBX9vPcDyxH0RTYFeytD90K4tR-xmg0RExHnkAnS5dKFJt-ZjI6X9vXC7HWTs__01yBzqtGXNEP_XSeTWxmSaBXrVCZcqCxH1cPNckRN1wz5nNGaq3BXbQeweNpf5qsalbzkuvFo2GtTQC19ezU0qy0r6A-RHo-PkwLGwqOZFDaBI6Fn86Lflfwynpg3lcAtBln-mLBUV4owbga_Z2lFmC0lqiR_IdXDk71Xcf6-pogBi2vThPvsR6tdeBA0nTJgUA3IlW2w34Jhts8z0NYxJBsJevRxe1ZNwJuWei7BcpaPaJtIEWpYhSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=K-VmCiEXt9ONtvF99iuxfzqD1Unoc1LLrEn1lcziLCWLuMbV9_Pzuaf30zban5hyJlgpknWup3aq6qn3TYCpM-FEQMgzyf47VnOAidQWVP8T3G1vhJyQopEElSIVe9lPMMPeC3LypZpo9BNmjritXcnxKYkAX0NmK4K-inZTLnmXLN7lfrKtTLnZx2YFYdbfLe6etA-IHQB4elHrfsaHdQJMh7JysqWjgH9iAS5kwDF9dk5V5OtN5SQWPOnt9odmN2-5Kx5JBd1S__CTNjbyiCqTB60Ljl2_SXVfWuQ420HKei3F12ScGBsKJiX7quQA2I1Rj_-lusUkHsYytIaS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=K-VmCiEXt9ONtvF99iuxfzqD1Unoc1LLrEn1lcziLCWLuMbV9_Pzuaf30zban5hyJlgpknWup3aq6qn3TYCpM-FEQMgzyf47VnOAidQWVP8T3G1vhJyQopEElSIVe9lPMMPeC3LypZpo9BNmjritXcnxKYkAX0NmK4K-inZTLnmXLN7lfrKtTLnZx2YFYdbfLe6etA-IHQB4elHrfsaHdQJMh7JysqWjgH9iAS5kwDF9dk5V5OtN5SQWPOnt9odmN2-5Kx5JBd1S__CTNjbyiCqTB60Ljl2_SXVfWuQ420HKei3F12ScGBsKJiX7quQA2I1Rj_-lusUkHsYytIaS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=vkkm42WHbQnE3FTHi5Z5appE2aPB7jfOpKhpTZlre2pmIu0FllK5-iKI7yIklrMMI9rEKmcx4FfpmszvercNTeUjYuE-F_v0FK9sjxeXyVHxUztYhxRQpWnhlhrz83sxfUiS4vSQbcY_DQrKQ8iuGxs2aKc5iRzKEDE59U8XiCcdpZ1swMp889mJPe612uV7sRKmwmPBb7rcWCO6GUm1gt6uUG7_i0pinNPFnOzH5QItdaRHMN6v7-mID-z6nYlewpZphQOh6eKP3_RgidLGRJlEwxYs_2Epi9hnxToB0LQ_zkfzKXf59XNOXqB9PX51_ZBSYGM9iqN9rKYavuL3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=vkkm42WHbQnE3FTHi5Z5appE2aPB7jfOpKhpTZlre2pmIu0FllK5-iKI7yIklrMMI9rEKmcx4FfpmszvercNTeUjYuE-F_v0FK9sjxeXyVHxUztYhxRQpWnhlhrz83sxfUiS4vSQbcY_DQrKQ8iuGxs2aKc5iRzKEDE59U8XiCcdpZ1swMp889mJPe612uV7sRKmwmPBb7rcWCO6GUm1gt6uUG7_i0pinNPFnOzH5QItdaRHMN6v7-mID-z6nYlewpZphQOh6eKP3_RgidLGRJlEwxYs_2Epi9hnxToB0LQ_zkfzKXf59XNOXqB9PX51_ZBSYGM9iqN9rKYavuL3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cugIqRkldpnu8XKrTh4CeANCT--JkdWUX_7z8XNRs2aEY-N8PiZOv1fzSa12HC2f9IvjbSXHdZ9PKyMA12zD6e4EyPg-EYCo4Nd2sg9wgirDMq6nFIj4miHUDJxvf68fufZ1xQos9SAM4YIKrKLirb-QNjiQ9PRSioH78YjhFSjTQhW0S40fCbJ8QV2XDzJanOj8M3OUs1HjJX0a5cBqk-OMDnUjlq4EhZwszQaMaz1gpt1FGQcEjv7EVMt9nQvvz_wS9XrHnh3ShFyz0ygLIRwP3XNMVmuMpA32YFLH-clihAipxF-T4d0TJ4w_ab1eB4F_cmzgsmKrfd1DI3IL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=jD-LvyIGgS6AZzhw94jQNDNaBsPKffQQhfjI7aDlJlSZensJoyEe76_T0z26-CpML_DIZE58rPz1B0TZ4DHrS_NaFzWdfe1qVbjEoKfLggNbrL-G9ht8VMOtQpf0udArP9m3Pq_4ESupk9B-H7Hbe4T4wrHQUTeXw_rU4pXOf-PC14m44xEVKVZ9LuFZY6ExnwbPozSPLJoDGMuVMfcegbA6b7HpOGlnACejTHcVVpP-QMipphRDdP9pjhv501lw11pGdpTlaVqiJRsMvGztFjPOT5YnQPqzL-A7BWQ09B2cC-T27MrceKAF_O-_yENTuOQ66LwxlvnJpoa5QYj9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=jD-LvyIGgS6AZzhw94jQNDNaBsPKffQQhfjI7aDlJlSZensJoyEe76_T0z26-CpML_DIZE58rPz1B0TZ4DHrS_NaFzWdfe1qVbjEoKfLggNbrL-G9ht8VMOtQpf0udArP9m3Pq_4ESupk9B-H7Hbe4T4wrHQUTeXw_rU4pXOf-PC14m44xEVKVZ9LuFZY6ExnwbPozSPLJoDGMuVMfcegbA6b7HpOGlnACejTHcVVpP-QMipphRDdP9pjhv501lw11pGdpTlaVqiJRsMvGztFjPOT5YnQPqzL-A7BWQ09B2cC-T27MrceKAF_O-_yENTuOQ66LwxlvnJpoa5QYj9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=ZpJ4YrQ01ODFBp7UW8Exf-TGPjWbiIukWyh71LXoEM3InCeNYeg_v5QbtCqkN-WhRVBh_-Zwtve6TqSx5GGF_19exSHekdM_L66ZX3V3uA2O4iiP4iCeR_Jl_cvzs3ssYS7IvLugRn1GQpXVE8hRY8LR0y9mqCYFz7K7RzWFB2q4bal6F7ZBXCDqIv7g5WW6EqGyHmQgT_6kLCjQfwzkIS60QPGnkiyYZujlBg0licjk2i2FVNMI0zhNggJOdwgw9iv8aFpPuXN8gcgC5pKJeu5fulXP9_aJJ0vK0wDGoeFIH2aAjGXg_wdds1of9VQNwG6cMyogzGkYkfTMDKKOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=ZpJ4YrQ01ODFBp7UW8Exf-TGPjWbiIukWyh71LXoEM3InCeNYeg_v5QbtCqkN-WhRVBh_-Zwtve6TqSx5GGF_19exSHekdM_L66ZX3V3uA2O4iiP4iCeR_Jl_cvzs3ssYS7IvLugRn1GQpXVE8hRY8LR0y9mqCYFz7K7RzWFB2q4bal6F7ZBXCDqIv7g5WW6EqGyHmQgT_6kLCjQfwzkIS60QPGnkiyYZujlBg0licjk2i2FVNMI0zhNggJOdwgw9iv8aFpPuXN8gcgC5pKJeu5fulXP9_aJJ0vK0wDGoeFIH2aAjGXg_wdds1of9VQNwG6cMyogzGkYkfTMDKKOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8taU8CkFYuVqHCTYSJKV2SvXEBFsAHIk_uVCZP_Z3xihWbbxLqQV7CEiBMkXNJYY9x-uJXyCKIBDP44F7Koqas2mxhNbcIhivBixHH4EPK77OfJHs5B78RFO8SikhYQk8S7KeZoXPBe1iieCu0_oQCwNKz8yBN-BJjMcEaOvuZ7izIUDi6hyHOu8XMibDq17oMqTEZm7azQDlXRv_WrDuNfWZ6efu4rKvy7sAA8gkdYT5mGZnCZby8o_SGCjMVHwTYejEUCeMx7kFa3y1WU5SW94pnQ-1wDkynuvA98ZmggdSH6bzxQP6ABxITCJy-fvlslK0gBN2JWkjHarKCNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjONA6FNBc9uJFHIUk4sBK-oFAy_qIJQXAJXT6ylkMdZjCHMYTnrM0upelepgIOJAoaAMtAkvu44x9MXy7qu1YB0IlfO4pZFLG4AV4oaTy9ZdD08ZX8hsVr5SeIKqzFBvcDwIEJ1yRfScAV98NtCrAPISHUWwduAkSyYnCkPxffVIKXZi0l5WNQXQ7mRc-ccVdiQ-VoLUevDzQf8faQTXYnHMXGnK_e5M-JBNEOM7k4yh94f1yja4YTxavh7z86kcfAalM3t9vE2hfNjcqGLauIk7j6lXgHwCkFakvK8nP3Ju1qVSaibjJerLSDQsIagFL0j3QbMf6oR5W9tGyKf1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=ph4hmg557Sz7vl06D_TrwSmqFPrZ2c6DHF-4ueC1p-Q8RiOmihC4pDm082MEeqJK5xvRwCd2JoBsuIlpa-ye78XImu8PmkhphoYgy14zyNuN1AsaBzBDDesY-cZVxXpkk7TPK8rG54c6hVxRWpoD8grz-ggR4m9u5EOJY9jDzEVNbyLovUuTu4IDpUwO_tPqf4yRm2GR9WbPzZYLUtht61VRJCXRFeOD_4g3BK1KEIW6tfg6jGifFxbRlT0kjaEHZzfbdjX9G5WP_bQY5yfa7j8Yxoaq4mU-Idgl0XvFsDKC2qm21lCG9o9bQqBd3XzDg8HlEeNjstvj1K-d80VcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=ph4hmg557Sz7vl06D_TrwSmqFPrZ2c6DHF-4ueC1p-Q8RiOmihC4pDm082MEeqJK5xvRwCd2JoBsuIlpa-ye78XImu8PmkhphoYgy14zyNuN1AsaBzBDDesY-cZVxXpkk7TPK8rG54c6hVxRWpoD8grz-ggR4m9u5EOJY9jDzEVNbyLovUuTu4IDpUwO_tPqf4yRm2GR9WbPzZYLUtht61VRJCXRFeOD_4g3BK1KEIW6tfg6jGifFxbRlT0kjaEHZzfbdjX9G5WP_bQY5yfa7j8Yxoaq4mU-Idgl0XvFsDKC2qm21lCG9o9bQqBd3XzDg8HlEeNjstvj1K-d80VcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrINuYbFilUJNLWJiDrzMUXG1R9liEBREzO5uEeArGraAMi04jSryDnv4gSr_X-SQNEuZ85AbAtJRxB7V7FM0ING4bHKD5grrSB1cOOQ-pql5gX-qGQ3fLnVceBhxtB-zZjpKJIFWBS-_iuP1g8loCcXyFHtwxEwPS4170qXxX1Aaqo54fZxJm-H1QX5VM7thsn01p7SGLNC9zGKG-SU72_0zDqLWvDc4QTrO5P1ryMg-f26_yb24Oyhi6UTFHl49ZykmaWQkSe9pGEE-8ZuFjPjKY66Fx4DlKQLAcFST-TdLzAFmE-V5i_9HwbBiLP74gYnTCRKyeJrawQ1YpFspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=lqvfzWUt7WwQQ7TouqddgAYNvOVtA2fdFUZA_gB9HSKvQmtVOlfCCCMvYMZpX1kGoWWgXfkOut4RHD3KhGQbvlnECj3vjeAPQa23QJGlDpUBVOOK8yZXbZyP_wXxrK18xbQyMFrsD7DivyJgbm2eguC7L2dT6kBARB0_d7lK2knNbUO8SeZGoR0u7H5oegsNsi6022nd4OXRLflvp0EYZxit-4tQotTlbrzwkyBV6A3cZQw0NzJWz0uzVH6zwmlcIJyhHIAUMwmtqDf2GMlz8UVdmm6sf1ur6fD2dwaUMkduMQyFJz8VPI_IIYG9vZklZGPr7en5u3KVtsm-IyH6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=lqvfzWUt7WwQQ7TouqddgAYNvOVtA2fdFUZA_gB9HSKvQmtVOlfCCCMvYMZpX1kGoWWgXfkOut4RHD3KhGQbvlnECj3vjeAPQa23QJGlDpUBVOOK8yZXbZyP_wXxrK18xbQyMFrsD7DivyJgbm2eguC7L2dT6kBARB0_d7lK2knNbUO8SeZGoR0u7H5oegsNsi6022nd4OXRLflvp0EYZxit-4tQotTlbrzwkyBV6A3cZQw0NzJWz0uzVH6zwmlcIJyhHIAUMwmtqDf2GMlz8UVdmm6sf1ur6fD2dwaUMkduMQyFJz8VPI_IIYG9vZklZGPr7en5u3KVtsm-IyH6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2fy0waMTEzYjVve3e0I24zlZw23NSZxgRqu3dsLbjDik3mHUEADbWC7FG2MhMh04MiDuWFTL2vScrvwditn-eA2t9Aj112wNRxHUM9x5p9MBFfVZ0s5-tNvRUiJeUEGDCn1Qgurt8rae2bjwvvdF9BWaAQOTkK_dO-9AOsC7v0qNSxBg-t3K-Y4fZL0F1h3_6cGNzvHCNwl8x2Fx0dMqLYbIzwD7_H-AgtR73wGCra2zHZlv0-7UiPlrlXXPE2e1KpSom7ZFGm7wYqRCIMCESpARJnjhoLi9gELhmygIS4PLOHDpRhEG8V6x1qDczyqoZI6qjZt2Me0fXKj5npjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=dW-C-rbBSHP8tYz45T1TBlicyNfnnCOqDkp8gUXJhQXSpRIjrFIGzZ93-Nj7DTPTWPZG_dx3n2Y2R1xB8bh9N61gi-f4Dd0rTNTvJmhX4jrXTYwzT9jSIOOUz2EFhiKe_fdKfsNkC68Pqo0wZN5ujSCPWL7D4dCVAbNbQstl48G9jN-l3bHE033Rmt0Ibu7qthj3mwRhmWiYOQZSmh-wyzlSVCtOmcW9rAppbU0sMRxAjqlyRjpFgiJuSQeRGm0d8uECtRxAjl0Nss0xtsg-RVvvgukRCr6L-vUA4ntqpvGC_Qtdp5z_yIouFyWtB4d23P6C7BZ4G_2ChG_VHWmScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=dW-C-rbBSHP8tYz45T1TBlicyNfnnCOqDkp8gUXJhQXSpRIjrFIGzZ93-Nj7DTPTWPZG_dx3n2Y2R1xB8bh9N61gi-f4Dd0rTNTvJmhX4jrXTYwzT9jSIOOUz2EFhiKe_fdKfsNkC68Pqo0wZN5ujSCPWL7D4dCVAbNbQstl48G9jN-l3bHE033Rmt0Ibu7qthj3mwRhmWiYOQZSmh-wyzlSVCtOmcW9rAppbU0sMRxAjqlyRjpFgiJuSQeRGm0d8uECtRxAjl0Nss0xtsg-RVvvgukRCr6L-vUA4ntqpvGC_Qtdp5z_yIouFyWtB4d23P6C7BZ4G_2ChG_VHWmScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=B4U2g8h2az7FoiZb4VCPxW1IkzBU5Vqg_rLZ7avx-BIsk-sd_qJlAJ-ydge3A9TqCTXFMz6ub7LM-md8dhb_ut_1LRkp_YPDtIaLXETwssv8_HavqwDa5qERlwefmj20NKd6NEccTUA1Du9AhyeTTZ0ROv1GE1_LH1RbwTq1QvLhfQgSlKblfxE8m2BJB6VY--cYVT-DDTkeV3dae_dbsSF498SVCalNSaCIhRFe5p4D0iUH8APajtuTJ6pG86qVvzW8YElep0blvfetq0xuIpkdB-MnG9RQ87vpCV3nQSOIkpU5qN4t2zSkgyR_oXV9J1G71I9qxNIMMhBeY0mpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=B4U2g8h2az7FoiZb4VCPxW1IkzBU5Vqg_rLZ7avx-BIsk-sd_qJlAJ-ydge3A9TqCTXFMz6ub7LM-md8dhb_ut_1LRkp_YPDtIaLXETwssv8_HavqwDa5qERlwefmj20NKd6NEccTUA1Du9AhyeTTZ0ROv1GE1_LH1RbwTq1QvLhfQgSlKblfxE8m2BJB6VY--cYVT-DDTkeV3dae_dbsSF498SVCalNSaCIhRFe5p4D0iUH8APajtuTJ6pG86qVvzW8YElep0blvfetq0xuIpkdB-MnG9RQ87vpCV3nQSOIkpU5qN4t2zSkgyR_oXV9J1G71I9qxNIMMhBeY0mpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=tKxAVmNpy2xB-IbWwnuHVMRTWvo3EOusGcin6wBodUdmI7uECyJjWfcVFyC5VDu_iAZVN0DPC1r8ucVFtOM79WL1I8pgmaFFmnmvrcTtfhkSeQ7rV7Y31143tGQjIkMKPGQflIGi1udv1BGCBg0mzVhIASpiFRp6eBdkzGQUMMchq96zKH1suaVkKUgm82_3YRWMiDJGDMBY-qgMXX2bg0jcTvItDowD17SumWCiN5BcRyuq_0Sbswi2FBnT0HnU-HQcM2CgRoT4TnNTCIyy0kkxHWcd2Zh2hTtTlQogfyg5o-jCEKYvAR7ut0omvCVPh7mXvmlA5Mtk_v1ih3yXCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=tKxAVmNpy2xB-IbWwnuHVMRTWvo3EOusGcin6wBodUdmI7uECyJjWfcVFyC5VDu_iAZVN0DPC1r8ucVFtOM79WL1I8pgmaFFmnmvrcTtfhkSeQ7rV7Y31143tGQjIkMKPGQflIGi1udv1BGCBg0mzVhIASpiFRp6eBdkzGQUMMchq96zKH1suaVkKUgm82_3YRWMiDJGDMBY-qgMXX2bg0jcTvItDowD17SumWCiN5BcRyuq_0Sbswi2FBnT0HnU-HQcM2CgRoT4TnNTCIyy0kkxHWcd2Zh2hTtTlQogfyg5o-jCEKYvAR7ut0omvCVPh7mXvmlA5Mtk_v1ih3yXCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
