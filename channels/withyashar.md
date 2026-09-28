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
<img src="https://cdn4.telesco.pe/file/Kur9L0vrNAXFgtttimB4nxvWTdqu7_YFY4v7DwJv3g8LsNrIk9ofG-dEtzX66Cmcb6Y3QyZDMUNivp8FfYcCJaqd4GJrz7qdodHriM7LiWfLJ_UeHG9HHWm328aOwXxlbIOav0_RK9Zqpbg475m194WqM0o8w5mlM-btLUxDABNg68dxE9a4OOnEhm04w1jApgawQUG2VOdfe-0HJy4ncUEhLo51l2eBWys48N_sj3AICFaQ6_173gJ16lqjLqR65MccV0XyIb1Esj-3t-rX3ey5EIrHAimLmsrr356V7cgfJVwLd8_GBSlRz4EKOzjsaiKQGte2sWRwj4Dg__G0IQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH1XJAeInntSUcewDyiss0wSzYDd94n-Hv6xxnBB7_ejRZ3M36R0_tlUVMc8MxRRq4T2Ca3JRO5gcoSuumUDkSlsEb8pHsUYDxI4IlC12xZEFMsUCpsP2IJtcMhoX7BCZhQnH0GUPkbyqVySli6TKJZRP3JJQDFC-5qN_B7BpKJSImGDQk9ioSckSkue8NPivG4rqEGkxhVJpeVGUHWtIUdrrdz7nellkzplkSQl62vF2Kd8wrBclKPdwW6D3-HrhbmMKCPJiXKptywCQaXsl_s529tuNzD10KBOA3EjiTI1tuoNGgyAMHKADu8ObMEMtTc_FaljbYtUHO0Kwl7wYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
شَدی ابوحطیرا، از تأمین‌کنندگان مالی حماس که شبکه انتقال پول «ژنو» را هدایت می‌کرد، در یک حمله هوایی دقیق در غزه کشته شد. ارتش اسرائیل مدعی است او
ده‌ها میلیون شِکِل ارز خارجی
را برای شاخه نظامی حماس منتقل کرده
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/24421" target="_blank">📅 18:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مورگان اورتگاس، معاون فرستاده ویژه آمریکا در امور خاورمیانه: «سناتور لیندزی گراهام هرگز از باور به شما (مردم ایران)دست نکشید. او باور داشت که شما دوباره آزاد خواهید شد. او هرگز از تشویق رئیس‌جمهور ترامپ و وزیر خارجه روبیو برای حمایت از آنها (مردم ایران) دست نکشید.»
@WarRoom</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/24420" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n40AMJDp9lRiWw4IJg7LzZL0GzHzO1XVg690pHCbbqk7pi5cnXE8rI3_78N1Ol2JZzx07rogJtyisjKzCylXCTJtRx-uCOitLoYKIT1x6V0ugQeQNpg2gfaYCNu-T1Wr4rHqgvpCZHn0H4GNQ2Rucv2tM7kSYfPKeFfKQhB0Zu8LCNBhgmGeTK3seYQD1pvMfF50-LmFBYbGzX8kT0ylj_UdH4ppEtKyCYJbRLZphVisnXdAe8Fch5uMGR2n3VZ3c5teZ-5JxfvXdcGGkNmK7fcALATP3erM-9GkfSdhY2T8jTmnXLKgFgigGr9faIf3ilWApdR9wsDts2bby2Q7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه عراقچی موفق شده یه ناو جدید اعزام کنه ۳ دسته هر کدام ۵ فروند هرکولس و ۱ اسکادران اف-۲۲ ، این است «قدرت مذاکره»
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24419" target="_blank">📅 18:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تسنیم : عراقچی امروز با میانجی‌گران در نیویورک دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/24418" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران: کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت ۱۸:۳۰ یک جلسه سیاست‌گذاری در کاخ سفید و ساعت ۲۰:۰۰ و ۲۰:۳۰ دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت ۲۱:۳۰ ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و…</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/24417" target="_blank">📅 17:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارشهای بسیار‌ از دو انفجار سنگین در تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/24416" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyxmXIicaiUN6X3VhmuFAQuYxIXftWwCrRKoGVguTfXH5Nn6QO1OeUfxkqUlZ5pll07NmvZhhJTI9RMTjp89bAOCQ3t9O6UtARx-EJMEiWv_uu9P2Vd6Ggm5JUpoWy5DtpzEOatQXgun4mezbS_nh4pY1_VHRR8HiIb-RC_jgB6_YG9_oSuhUPwliTXAUJ_KQs08PQ96e2ptTe_LFqSzH19MNjtxyPRW-HlHHuUL33lc5Z3-8SVLW06h3EIphg9NzZCpkXyfsQF5K3FnwZQamxPw0lMUF_mKJe5AfglFBvbDTT1Z-O-1fMZkbXK4VdF3qoQOfbqR8VXs_JSTcxK-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : فلکه دوم فردیس لانچر و موشک آوردن
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/24415" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران:
کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت
۱۸:۳۰
یک جلسه سیاست‌گذاری در کاخ سفید و ساعت
۲۰:۰۰
و
۲۰:۳۰
دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت
۲۱:۳۰
ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و
یک اعلام رسمی مهم
خواهد داشت؛ موضوع این اعلام هنوز رسماً اعلام نشده، اما گزارش‌های منتشرشده آن را مرتبط با
هوش مصنوعی
می‌دانند. ترامپ ساعت
۲۳:۰۰
نیز با خبرنگاران رسانه‌های چاپی دیدار و گفت‌وگو خواهد کرد. شام خصوصی ترامپ با
داریو آمودی، مدیرعامل Anthropic و سازنده Claude
مربوط به شب گذشته بوده است. همچنین فردا ترامپ و مایک جانسون قرار است با مدیران شرکت‌های بزرگ هوش مصنوعی دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24414" target="_blank">📅 17:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امروز ترامپ بیانیه ویژه ای ارائه خواهد داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24413" target="_blank">📅 16:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24412" target="_blank">📅 16:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYkW3gwAjZPS86Qcl0PTTAZN1hg8RsHAOrE1Iz-S757pgdf8a6On6C7-v3lohDr5DqmwFSYL1DFkty0lODX1hiiaUIgegPPJKDgDJDpJrLRD3nhOHl9Z1uwriyWRmPBk0tWgXmrmjCXiqEecHNxcEXrM7dul9c0LZ5jlrhgPkJaaaR-Te1jU07xHtXAfDtBkF2v10ZiSnVFbIjR0PIFZXKQKAW7E_ajJZ3UO0Ak3ej-C0taZOXZletCaCxH-w7fsGRatnjGkyULJ_HF_dwGuGNrbObx_DGjMImnjGLWGtTR5IHws1DLTjoVva7BvVpm-EfnP6hOISeCSfhL5UBOEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbV-bD5__eb_VBW94wKM5Ha2SFUixjc_OzFbEMFBZScHVNbIFOy0SadMW2CDCUJOE8w4Wmx51MJQxlvMi_di5grwJboWBvmoYWRiR1V8Q796OBNcxvANQm2dKhrqvDIGGO2jdHhdrrCN5xbw_fQhuKH_n05YXbKuDQV7Sms6q5zyhCbYzGj_OC22UDITyw1KHm8Yv6763dXQF7tmmazA9B9FG2xTJ8pyp6tPopHY-7Sol_cHF6eWltknSVvO3I8snn2JZTQjcIBqfezG-R9XsTVHJev4k7nwLoFo2GtSngA9wLb5jo9EwwDSWVnc5B3XMv9wO7t-jNLBboMFEzWeJhZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbV-bD5__eb_VBW94wKM5Ha2SFUixjc_OzFbEMFBZScHVNbIFOy0SadMW2CDCUJOE8w4Wmx51MJQxlvMi_di5grwJboWBvmoYWRiR1V8Q796OBNcxvANQm2dKhrqvDIGGO2jdHhdrrCN5xbw_fQhuKH_n05YXbKuDQV7Sms6q5zyhCbYzGj_OC22UDITyw1KHm8Yv6763dXQF7tmmazA9B9FG2xTJ8pyp6tPopHY-7Sol_cHF6eWltknSVvO3I8snn2JZTQjcIBqfezG-R9XsTVHJev4k7nwLoFo2GtSngA9wLb5jo9EwwDSWVnc5B3XMv9wO7t-jNLBboMFEzWeJhZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی از انتقال جنگنده‌های رپتور به خاورمیانه هستند:
GOLD21: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 17-46034)
GOLD22: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 16-46021)
GOLD31: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 18-46051)
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24410" target="_blank">📅 16:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=ie8IsElWD9FUgncZ-sBsAkBoeyz6a8jQofiulo7YEjEEioG1AgD-9cVEHcQrA5TdIqAf5u6In5GQIdRSLikYuWfaks3oUnG6wVEwxpet0vA9383ZNpFSzfitKG0Z5ZVL839KR5A5dnCwJaVbGFcwvW9ioTtz6eJi34FnRcO4ZKAJU9nUk7sijTDDCxrkItIFuLYaA-DJlALjetUD8IJ9xt2WTx7PAOfdGxLOcXEc2rTa7RNN34oUTZcD29EqHdm7pPakbnL1YW0ZovQ__kTUVnApBZmru5cxXUf__nPMv-L22a6UAKOr9OGdwVPPQern8w0PeA9HH0mZjU8o-Wxnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=ie8IsElWD9FUgncZ-sBsAkBoeyz6a8jQofiulo7YEjEEioG1AgD-9cVEHcQrA5TdIqAf5u6In5GQIdRSLikYuWfaks3oUnG6wVEwxpet0vA9383ZNpFSzfitKG0Z5ZVL839KR5A5dnCwJaVbGFcwvW9ioTtz6eJi34FnRcO4ZKAJU9nUk7sijTDDCxrkItIFuLYaA-DJlALjetUD8IJ9xt2WTx7PAOfdGxLOcXEc2rTa7RNN34oUTZcD29EqHdm7pPakbnL1YW0ZovQ__kTUVnApBZmru5cxXUf__nPMv-L22a6UAKOr9OGdwVPPQern8w0PeA9HH0mZjU8o-Wxnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراضات به گرانی دانشگاه علامه طباطبایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24407" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNeqSIwCkhzXvwl3NLBJlmWEZWmgm8jzS19HdlkWJGVGjPK8Kn5mbvt9D18NT0pBrG6JvHxM_SNg_-mOQ_Sy74q__99RQUHHMia98xvJbVVeb7bFgL-lqIQHpG7UUSz0hbGBA-UtxhL1RAfGIbwTeODNjKcUU4k45ZcFD9SDhs_MaOrbamWZRTePspUPbDZAEsIsFncZz299rj5A3xu-ASa-1qMQk2X4mXBpu7WZAYqgApcY7TTn87ViXFxy37yqQRwAsFWwv9iWWaEhiZtDfhOP7pI3WivbQsHvD57Vj5k_dZqDzfYBDA5bwv37XUMnPx4Q0236OO1Y6Yzh5uNX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24406" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWhCO4pwnWy9JsjoiYBwv0R2hQ6lrrWhvy8mk3TIh6HtXBm95XQy4YN66_aNnuz6L3U43vJD9tjm3PVZLDTe_6kR9hYLcu-_7jS4MOQVqSmj7rFQXOCk3nFHsrJCKuyWi8tD_24tWtW1ZWuIgwBtV0vjMB-E7yMLDHeCOHN1WmzHaNwqrTePmtS8R4w3tTYQli6cjlE_uN_pgELzOUmUr19TNhfqrvxHl3F0trk4gEFaJ5dkw3PVlyZLF3AnaCuqAq1XWaGTi73tRkLsDSjMnxvgyQnR2KNMZeZSkNqKlSK_KJ4hiaxZIkvln_an45hudAVpPktjc92vl24vw8xLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام:
ادعا رژیم :
یک فرمانده ارشد سپاه پاسداران امروز گفته است ایران از طریق «نیروی دریایی» خود
کنترل کامل تنگه هرمز
را در اختیار دارد. این ادعا
نادرست
است.
واقعیت:
ایران نیروی دریایی ندارد، زیرا
نیروهای آمریکایی آن را غرق کردند.
ایران همچنین کنترل تنگه هرمز را در اختیار ندارد؛ همان‌طور که
هزاران کشتی آزادانه از این تنگه عبور کرده‌اند
و تنها طی چند ماه گذشته،
بیش از یک میلیارد بشکه نفت
از این مسیر عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24405" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEQ3</strong></div>
<div class="tg-text">یاشار بندر عباس طرف پارک شهدا صدای دو تا انفجار اومد با فاصله 3 دقیقه از هم</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/24404" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش صدای انفجار بندر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/24403" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترکیه تودی :
پروازهای باقی‌مانده شرکت‌های هواپیمایی ایران به ترکیه نیز ممکن است
از اوایل اکتبر ۲۰۲۶ / اواسط مهر ۱۴۰۵ متوقف شود
. این رسانه به نقل از
دو منبع مطلع
گزارش داده که به‌دلیل تشدید تحریم‌های آمریکا علیه صنعت هوانوردی ایران، انتظار می‌رود تمام پروازهای شرکت‌های ایرانی به ترکیه لغو شوند. یک منبع نزدیک به صنعت هوانوردی ایران نیز این موضوع را تأیید کرده است. با این حال،
مقامات ترکیه هنوز چنین تصمیمی را رسماً اعلام نکرده‌اند
و یک منبع دیگر نیز نتوانسته این خبر را تأیید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24402" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینوستینگ :
بیت‌کوین امروز تا حدود
۸۳ هزار دلار
عقب‌نشینی کرد و حدود ۱.۷ درصد کاهش داشت. افزایش بازده اوراق خزانه آمریکا و نبود پیشرفت محسوس در مذاکرات ایران و آمریکا، اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک را کاهش داده است. اتریوم نیز حدود ۲ درصد افت کرد و آلت‌کوین‌ها عمدتاً در مسیر نزولی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24401" target="_blank">📅 14:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز:
طلا امروز حدود
۳ درصد سقوط کرد و به پایین‌ترین سطح بیش از هفت هفته اخیر رسید
؛ علت اصلی، افزایش قیمت نفت و بالا رفتن انتظارات برای افزایش نرخ بهره عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24400" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اورشلیم پست:
منابع حوثی مدعی شده‌اند حملات عربستان به مناطقی در تعز تلفات سنگینی برجای گذاشته و حوثی‌ها تهدید کرده‌اند در واکنش،
پل‌های داخل عربستان
را هدف قرار دهند. اصل حمله و میزان تلفات هنوز از سوی منابع مستقل تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24399" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مقوا ای آی : انقلاب اسلامی
سلطه و وابستگی ایران به قدرت‌های خارجی را پایان داد
و ایران را به کشوری مستقل تبدیل کرد. او سیدحسن نصرالله را شخصیتی کم‌نظیر دانست و گفت
پرچم او اکنون در دستان شیخ نعیم قاسم
است. وی مخالفان مقاومت لبنان را به
بی‌تدبیری و حتی خیانت
متهم کرد. خامنه‌ای ایران را
قدرت اول جهان بر اساس «محاسبات الهی»
خواند و مدعی شد دشمنان ایران پس از ضربات رزمندگان، دیگر حتی از
دریای عرب جلوتر نمی‌آیند و به‌زودی از این منطقه نیز خارج خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24398" target="_blank">📅 14:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری
NBC:
در جزئیات تازه‌ای که امروز منتشر شده، اعلام شد در
۲۳ شهریور ۱۴۰۵ (۱۴ سپتامبر ۲۰۲۶)
، یک موشک کروز ضدکشتی ایران در
تنگه هرمز
به یک شناور حامل نیروهای آمریکایی اصابت کرده و
۸ تفنگدار دریایی آمریکا
زخمی شده‌اند. به گفته سه مقام آمریکایی، هر ۸ نفر دچار
آسیب ناشی از استنشاق دود
شده‌اند و برخی نیز علائم
ضربه مغزی و احتمال آسیب ناشی از موج انفجار
داشته‌اند. این افراد شامل ۷ سرباز و یک افسر از نیروهای تفنگدار دریایی بودند. هیچ‌یک از مجروحان وضعیت وخیمی نداشتند و هر ۸ نفر پس از مدت کوتاهی به خدمت بازگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24397" target="_blank">📅 14:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وحیدی :  اشتراک چت جی‌پی‌تی مون رو تمدید کردیم ، یه پیغام از مقوا براتون میزارم تا ساعاتی دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24396" target="_blank">📅 13:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دلار ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
تتر ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24395" target="_blank">📅 13:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در فرودگاه بین‌المللی مهرآباد تهران طی ساعات گذشته، یک فروند هواپیمای C-130 هرکولس متعلق به نیروی هوایی ارتش جمهوری اسلامی و یک فروند هواپیمای ایلیوشین-۷۶ (Il-76) متعلق به نیروی هوایی ارتش یا نیروی هوافضای سپاه پاسداران در این فرودگاه به زمین نشسته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24393" target="_blank">📅 13:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئیس سازمان هواپیمایی کشوری با اشاره به تلاش‌های مستمر این سازمان برای احیای مسیرهای پروازی، از رایزنی با وزارت امور خارجه و ثبت شکایت رسمی نزد سازمان بین‌المللی هوانوردی غیرنظامی (ایکائو) در واکنش به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی ایران خبر داد.
@WarRoom
یاشار : بدجور دارن تو باتلاق دستو پا میزنند ولی هی میرن پایین تر</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24392" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)  تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)  بیتکوین ۸۳،۱۵۸ $ انس جهانی طلا ۴،۱۶۳ $ نفت برنت ۹۸،۷۳$ @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24391" target="_blank">📅 12:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43823eee78.mp4?token=bRFlOcr86BPDQuoNQ7ooYag0hCV-IOoCxPS3nSaGyF99IToooUc23ulwDhdoj5b4fVpglR5SernCZdI2JS16tyzLy8Jz8bUGyb8b6v0ovbMi7lAXarYotHS1RdQZMCOgiIX5K-rMt_sSYLn2kWaFfpKfqKiWH6IGShSj_NQZ5dwG6YBH49KFSKpc4JQkBjpVEwgdYF8aKoAwLjWYUCVPHjAKMIlKzwP8ApFuuRLRlvaHC19I3c8Imu9N3Asw53GIEuoHVrvB65-lz3zYFLmvLYJlprJF7R4wYEVi7WrQ8_y3Ql1GjL5Gkl0CZ2p-xuWlSepxdl-U5QoAHD4D30vsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43823eee78.mp4?token=bRFlOcr86BPDQuoNQ7ooYag0hCV-IOoCxPS3nSaGyF99IToooUc23ulwDhdoj5b4fVpglR5SernCZdI2JS16tyzLy8Jz8bUGyb8b6v0ovbMi7lAXarYotHS1RdQZMCOgiIX5K-rMt_sSYLn2kWaFfpKfqKiWH6IGShSj_NQZ5dwG6YBH49KFSKpc4JQkBjpVEwgdYF8aKoAwLjWYUCVPHjAKMIlKzwP8ApFuuRLRlvaHC19I3c8Imu9N3Asw53GIEuoHVrvB65-lz3zYFLmvLYJlprJF7R4wYEVi7WrQ8_y3Ql1GjL5Gkl0CZ2p-xuWlSepxdl-U5QoAHD4D30vsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیوید پردو، سفیر ایالات متحده در چین: شی جین پینگ در ماه مه موافقت کرد و در اینجا نیز آن را تکرار کرد که آنها از عدم وجود سلاح هسته‌ای در ایران حمایت می‌کنند، این بسیار مهم است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24390" target="_blank">📅 12:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دریادار سیاری، از فرماندهان ارشد ارتش: «غرب تنگه هرمز و خلیج فارس تحت کنترل کامل نیروی دریایی سپاه پاسداران قرار دارد. در شرق تنگه نیز کنترل کامل در اختیار نیروی دریایی ارتش ایران است.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24389" target="_blank">📅 12:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه های رژیم : بیژن مرتضوی به ایران بازگشت
@WarRoom
تکذیب کرد</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24388" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24387" target="_blank">📅 12:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سفیر آمریکا در اسرائیل : واشنگتن به‌زودی ساخت سفارت خود در اورشلیم را آغاز می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24386" target="_blank">📅 12:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=FR7w-Ex9g7yLVZew4E9E1fjeyfqAGm79UxO4sqF4DjGWw_bHfh8UDEQYepudmCMf3BOwzXDqoebt88mLbw0-jJAPQQqXDX77Au8uhd5xpLO_PWWQtB8dNm2HwnY-gOPZ0fW7naOHq5R3Y_WSpZvdmdeOFaKSTfK075N1a99FHR0M6NDT7bBmaRB1saehcNTyBpmAw4n0gU8o6J5iKEzNItdePTojbCEQnuPcpgA4Rn3cg45rRzY0SZYHoXET-v88ZMbpCby0YaOxDBxFBNmbbXNm7Wfc9ezyvn8MWOfdtd-lRFOI9ndJpJSl9fDzopvSx1sG3-mtnaGLVOv0e5fVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=FR7w-Ex9g7yLVZew4E9E1fjeyfqAGm79UxO4sqF4DjGWw_bHfh8UDEQYepudmCMf3BOwzXDqoebt88mLbw0-jJAPQQqXDX77Au8uhd5xpLO_PWWQtB8dNm2HwnY-gOPZ0fW7naOHq5R3Y_WSpZvdmdeOFaKSTfK075N1a99FHR0M6NDT7bBmaRB1saehcNTyBpmAw4n0gU8o6J5iKEzNItdePTojbCEQnuPcpgA4Rn3cg45rRzY0SZYHoXET-v88ZMbpCby0YaOxDBxFBNmbbXNm7Wfc9ezyvn8MWOfdtd-lRFOI9ndJpJSl9fDzopvSx1sG3-mtnaGLVOv0e5fVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحرکات نظامی امریکا در عمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24385" target="_blank">📅 11:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز : اسرائیل اعلام کرده پس از پرتاب یک
پهپاد انفجاری حزب‌الله
به سمت نیروهایش، مواضع حزب‌الله را در جنوب لبنان هدف قرار داده است.
حملات اسرائیل در مناطق مختلف جنوب لبنان از جمله
صور، نبطیه، مرجعیون و بنت جبیل
ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24384" target="_blank">📅 11:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل اعلام کرده یک
تک‌تیرانداز حماس
را که به گفته ارتش در حال برنامه‌ریزی حملات بود، در جنوب غزه هدف قرار داده و کشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24383" target="_blank">📅 11:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز:
ایران همچنان بر
طرح هفت‌روزه بازگشایی تنگه هرمز
پافشاری می‌کند و می‌گوید حاضر نیست شروط خود را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24382" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۳،۱۵۸ $
انس جهانی طلا ۴،۱۶۳ $
نفت برنت ۹۸،۷۳$
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24381" target="_blank">📅 10:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=bRa4AKf9bVVaYwijD38US27AmOoziY29dBBU_IVnrAVUq9bzqR8I19Dpp-pdccfIBOj8VB9R79PXW4WeoDtoFac2DkcDPC2bRazHivomOdzP_Mq_hA9F0j_Q5YbXkJkuMLiXTRbbvSWPwfNCWukzkGkRds4VJb05aBZig8BaOyrG53p2nWwuQOnXXYfgGzBL_AwvOlLZHLPGxgMyVwCf-hiib5iv5xpPJSyhEGSN54ZyIHV-fTVjsr5Dv5lWV0HH2o2f-BencuNO9U33NoondnXiBGXocE2KDqd5MXivcOD1sCe41WcolLD-bygb307h-JEBK0rAPDKrpKOp_L5wRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=bRa4AKf9bVVaYwijD38US27AmOoziY29dBBU_IVnrAVUq9bzqR8I19Dpp-pdccfIBOj8VB9R79PXW4WeoDtoFac2DkcDPC2bRazHivomOdzP_Mq_hA9F0j_Q5YbXkJkuMLiXTRbbvSWPwfNCWukzkGkRds4VJb05aBZig8BaOyrG53p2nWwuQOnXXYfgGzBL_AwvOlLZHLPGxgMyVwCf-hiib5iv5xpPJSyhEGSN54ZyIHV-fTVjsr5Dv5lWV0HH2o2f-BencuNO9U33NoondnXiBGXocE2KDqd5MXivcOD1sCe41WcolLD-bygb307h-JEBK0rAPDKrpKOp_L5wRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پل ستار‌خان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24380" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007a727a10.webm?token=WCSNuxy4FBiRR7_TNsUEoXpTENoXrQzDxmJHO2bdOYzVhr4xq1XYWe3YhsM3x3xCK-oqWgxfVpF5ouAZmnc5LrZB4URtcKgSCPMrooYaUh3b-WaJr9WB60n8wxOe_OiVeOuKPJ4rzS-1lmRow0Y9zoTeIk_nyqBSeNSq1e17tGg04Z_GmoR91kYg4BLdccjMNRCfmC9HTlfSUbiBKWJyrM5xy-7i0PLrtE0Qu_Hvfx-yoRSHbdB2A3vXUP6MbTCBqZ0ywThfZSLliJyIPzHHz4x4HhbYs1azW8rUwFbuqFRCifXjly8RqKiotx947PK69HgvZhZwoQLwexT1vTjV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007a727a10.webm?token=WCSNuxy4FBiRR7_TNsUEoXpTENoXrQzDxmJHO2bdOYzVhr4xq1XYWe3YhsM3x3xCK-oqWgxfVpF5ouAZmnc5LrZB4URtcKgSCPMrooYaUh3b-WaJr9WB60n8wxOe_OiVeOuKPJ4rzS-1lmRow0Y9zoTeIk_nyqBSeNSq1e17tGg04Z_GmoR91kYg4BLdccjMNRCfmC9HTlfSUbiBKWJyrM5xy-7i0PLrtE0Qu_Hvfx-yoRSHbdB2A3vXUP6MbTCBqZ0ywThfZSLliJyIPzHHz4x4HhbYs1azW8rUwFbuqFRCifXjly8RqKiotx947PK69HgvZhZwoQLwexT1vTjV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24379" target="_blank">📅 10:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=XVin5omvW2qgXA2PjWr-z9W4C5BDWYlnHHYHm-1XzMe_4vv04Hqsggdb_pgPWe58NWEstbj5L1VOEY8IEaU2J-s9gIeXA63a0-WQXZDj9PrWgfmqyZEeS7uxBlBWwf8VD_SZUDnt0uA1nnP2Sv2VkC8WTeXwEf7v03BOhhWZmvrMn4GDy2726sHM7lOINTLuf_ulHSXhIJJ2Uuk2MP_oTAb4hTFh1I1W1qQQgqTq35E3koxwjgp8YduXxcbEVUy87iqtyPWkYLpsGH5TCNK0u_BNiOL79q4Obcj5JYtdEQ_-T_-x_zXS-8oJ0elPqPdZZUFZ4keH6MTZ4hVDUl_mARIz19Zro-XQ1kIMS6QdFKa09kzDon9jZGtRv9ZmOSwqIVqMiMFpWtIFwvHhVhTXUW8YUhqXpyRfcY40yHHZQBc0TzE9hc5k3TJr1CM2t1z19HtgUMHii8nXvZiW3VCN3WTwNaM8vFBdIAQ5m9KWB6Eqmw9yzh_gljT28EbzF8GIbsoshlinR6VYTbtsuuw7K5qO2lPqwDRS_SFAmi87IfFw9cJQyKcdyFvuIhvDQBLnK1q84BGLX8h2d5htRflQea1PcDHw1obOLmQZ_xs8j8vRmi4qEJsVKEodYMEpOxqtk2wEXHfbi49OkkmbDINI12uZMcQt92G7lj_MJBzMjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=XVin5omvW2qgXA2PjWr-z9W4C5BDWYlnHHYHm-1XzMe_4vv04Hqsggdb_pgPWe58NWEstbj5L1VOEY8IEaU2J-s9gIeXA63a0-WQXZDj9PrWgfmqyZEeS7uxBlBWwf8VD_SZUDnt0uA1nnP2Sv2VkC8WTeXwEf7v03BOhhWZmvrMn4GDy2726sHM7lOINTLuf_ulHSXhIJJ2Uuk2MP_oTAb4hTFh1I1W1qQQgqTq35E3koxwjgp8YduXxcbEVUy87iqtyPWkYLpsGH5TCNK0u_BNiOL79q4Obcj5JYtdEQ_-T_-x_zXS-8oJ0elPqPdZZUFZ4keH6MTZ4hVDUl_mARIz19Zro-XQ1kIMS6QdFKa09kzDon9jZGtRv9ZmOSwqIVqMiMFpWtIFwvHhVhTXUW8YUhqXpyRfcY40yHHZQBc0TzE9hc5k3TJr1CM2t1z19HtgUMHii8nXvZiW3VCN3WTwNaM8vFBdIAQ5m9KWB6Eqmw9yzh_gljT28EbzF8GIbsoshlinR6VYTbtsuuw7K5qO2lPqwDRS_SFAmi87IfFw9cJQyKcdyFvuIhvDQBLnK1q84BGLX8h2d5htRflQea1PcDHw1obOLmQZ_xs8j8vRmi4qEJsVKEodYMEpOxqtk2wEXHfbi49OkkmbDINI12uZMcQt92G7lj_MJBzMjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
به‌جز نفت، که قیمت آن از دوران دولت بایدن پایین‌تر است، دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها کاملاً نابود شده‌اند.
اما به‌جز نفت، قیمت همه‌چیز در حال کاهش است و روند کاهش ادامه دارد. ما بدترین تورم تاریخ کشورمان را به ارث بردیم، اما تورم اکنون به‌سرعت در حال کاهش است. کشورمان وضعیت بسیار خوبی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24378" target="_blank">📅 05:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=Doj-T78308Jj_rzBUVd6tggNTQqFZWNxtn5bmIqbkSoR-saRaA1yKWigOu9tGw8fWwXlGfMgYxCInUH-JXb-MuT_a6lijTzfni1ojTqsjChk5-lNSsCeil2CA4oLKs81co-_69Y8a6JJaJsLrHR9Bp2rKg3IjFeUlUnRo_e9WXazb26QNpZ2xi0L3z8rkVf6jkiPR8_clOtgF1ydvBL9pJx4Nk1ENGzrccZlQyNf_iTlocmKgStSQegWhM0AQGrhSAO6l2T1dYvIlCOLcnjeol12wmrTVORW_icmzLMUd9jMxTxO7cc3GdJ6RNBVMmQ9QUziHx7yuJG5yNsE7JqZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=Doj-T78308Jj_rzBUVd6tggNTQqFZWNxtn5bmIqbkSoR-saRaA1yKWigOu9tGw8fWwXlGfMgYxCInUH-JXb-MuT_a6lijTzfni1ojTqsjChk5-lNSsCeil2CA4oLKs81co-_69Y8a6JJaJsLrHR9Bp2rKg3IjFeUlUnRo_e9WXazb26QNpZ2xi0L3z8rkVf6jkiPR8_clOtgF1ydvBL9pJx4Nk1ENGzrccZlQyNf_iTlocmKgStSQegWhM0AQGrhSAO6l2T1dYvIlCOLcnjeol12wmrTVORW_icmzLMUd9jMxTxO7cc3GdJ6RNBVMmQ9QUziHx7yuJG5yNsE7JqZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
می‌توانید درباره حملاتی که در بریتانیا رخ داده و مظنون مهاجری که در این ارتباط بازداشت شده، اطلاعات بیشتری بدهید؟ آیا ارتباطی با ایران وجود دارد؟
دونالد ترامپ:
ما همه چیز را درباره او می‌دانیم و به‌زودی اطلاعات بیشتری درباره این موضوع خواهید شنید.
ما آنها را گرفتیم.
@WarRoom
یاشار ، تکمیلی: تمام رسانه های جهان به اتفاق میگن کاره ایران بوده حتمأ سر نخ های پیدا شده و  عملیات توسط یک زن کشاورز که به ۳ ون مشکوک میشه و گزارش میکنه لو میره</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24377" target="_blank">📅 05:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=as-ojRXLu7LuMteXIY68FOro2N_UZmuUzCcmjx33NH62cNvmJ4_g1_NBcqUdElvsdFzQybEx0HKcFz9CzHEjh-ypaJf8xUMrWpo7yNns7Xvwqc7bgMM_teoaIyLA5RiGDwPaZS3dkZtQIrXGErOzIDx5SHrvqjtkKo0ZExPNlaRYOPaDd0Hf3_B50ayiZkhgH4g0Q3DnyBY-nadpatQVI3GONzvgz3HjvUnoqkp5sLW2dPYcuzom6jL0O2wuH03Rlr_FnvMp0M-C2VRbmWo51vCpOUmsbSLTE9pi92sxhebfwrC8aruK7Ve96UKZMWviy6yX-uaf041XmRVf6Vc-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=as-ojRXLu7LuMteXIY68FOro2N_UZmuUzCcmjx33NH62cNvmJ4_g1_NBcqUdElvsdFzQybEx0HKcFz9CzHEjh-ypaJf8xUMrWpo7yNns7Xvwqc7bgMM_teoaIyLA5RiGDwPaZS3dkZtQIrXGErOzIDx5SHrvqjtkKo0ZExPNlaRYOPaDd0Hf3_B50ayiZkhgH4g0Q3DnyBY-nadpatQVI3GONzvgz3HjvUnoqkp5sLW2dPYcuzom6jL0O2wuH03Rlr_FnvMp0M-C2VRbmWo51vCpOUmsbSLTE9pi92sxhebfwrC8aruK7Ve96UKZMWviy6yX-uaf041XmRVf6Vc-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژنرال جک کین به مارک لوین در فاکس نیوز:
آمریکا و اسرائیل همین حالا
توان هوایی لازم برای تغییر چشمگیر روند درگیری در داخل ایران
را در اختیار دارند.
او پیشنهاد می‌کند معترضان ایرانی علیه
مراکز سپاه پاسداران
دست به اقدام مسلحانه بزنند و همزمان هواپیماهای آمریکایی و اسرائیلی نیز از آسمان از آنها پشتیبانی کرده و
نیروهای کمکی حکومت
را هدف قرار دهند. او می‌گوید: «
ما داریم این کار را سخت‌تر از چیزی که هست می‌کنیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24376" target="_blank">📅 04:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT0ggtGAz60JZyb5-RMkQco_ZO7Wx1tTotc7tDyhn7Lt3ORcr5M_DuwcYBp5PUaRYI94fgQVMLTsANVzhYnOfNSCYzx3ebV6OXxbl4uXgxrUwgDF_LOh-0Yyfiu-XkJevxgNDYV6Ip0Sj9FXf5le8VCjnwfSQolKrSpRq48dNZCfPRfQY5AYj-gjMjjpLkOW9fbYaA24_gkLPAJV0LiDJhG338fFbJyAF3SzI19GN7Y5KcGDcR7c_jt8oJCqoJ4M3slm4BYYbZdFLXVeGEj6MVU3sggEZSAvK8Sd_b8WfmhkeJCaYabdYEnXxvJhzrfRuq6y-NvDFYcuOw3JjFDDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بمب‌افکن‌های راهبردی بی‌-۱بی آمریکا در پایگاه فیرفورد بریتانیا؛ در انتظار فرمان احتمالی ترامپ برای دور جدید حملات به ایران! یک بالگرد رسانه‌ای که برای پوشش عملیات تیم‌های خنثی‌سازی مهمات انفجاری در منطقه ولفورد به پرواز درآمده بود، بمب‌افکن‌های…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24375" target="_blank">📅 04:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24374" target="_blank">📅 02:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24373" target="_blank">📅 02:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24372" target="_blank">📅 02:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk7oSYnth-F6R5HlBgp40BYhYQKi81J05cNbQaErDOSCdOt2VwPw6EHkwnYBscSk1MJEXfko1ZmJL9RjDISmFv9TGiHTbgrUj3WjNuT16pFGLDfm8NMbW5eg1MC9HHb4i0pBL-ZudxSJZ6Y44E2irs5b_zRSW5v0842h_JaktBozt8yiJr_0r9Y_vTsfiyjFaPH_Mx8ImKEkUOnmQqaW5EDUBN-vdRK1boe2TmryovyTuvYbpQ6FtN3jzyiNR1rnItb8X0dm-UQbL8t_YHd8uAGF3FJ9pA9XAQan0FDg32PqfAXYBlV0Rjdk69fRyqlYpAMGeGRgijT-nNCu-waxEN3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk7oSYnth-F6R5HlBgp40BYhYQKi81J05cNbQaErDOSCdOt2VwPw6EHkwnYBscSk1MJEXfko1ZmJL9RjDISmFv9TGiHTbgrUj3WjNuT16pFGLDfm8NMbW5eg1MC9HHb4i0pBL-ZudxSJZ6Y44E2irs5b_zRSW5v0842h_JaktBozt8yiJr_0r9Y_vTsfiyjFaPH_Mx8ImKEkUOnmQqaW5EDUBN-vdRK1boe2TmryovyTuvYbpQ6FtN3jzyiNR1rnItb8X0dm-UQbL8t_YHd8uAGF3FJ9pA9XAQan0FDg32PqfAXYBlV0Rjdk69fRyqlYpAMGeGRgijT-nNCu-waxEN3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WarRoom with Yashar : Winter is Coming
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24371" target="_blank">📅 01:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=M3VIgMydN71VOa2-r-IlGsSHrQCkbaimLfLBpr-kfUMmRM65r1tl82W1i3C_eqfPw77bJnWSbKkJuPM0r--OPpV-MXILqpU5TeNJgUlE-fD3G4wdT7M-sFGraINpzOr64kVTug4Kz9OSgL5gJEadPrjenKQAPEjand8mWAwfwSEbLy6eVG2Vw49qNCB01tpEOA9zUZQpKAG8n_vcPMYOYmw3ZiAC7vYG26Rn308AOFpkIkMS480s9TIF-zbi2W0d87duYj7mvGxhprn43wXkDE4FbVHnkaSYU4rF21xhDzJ-SJU0_f6ofMFBxDYZuqiVl-xElDGs4TXyyoA-zPwd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=M3VIgMydN71VOa2-r-IlGsSHrQCkbaimLfLBpr-kfUMmRM65r1tl82W1i3C_eqfPw77bJnWSbKkJuPM0r--OPpV-MXILqpU5TeNJgUlE-fD3G4wdT7M-sFGraINpzOr64kVTug4Kz9OSgL5gJEadPrjenKQAPEjand8mWAwfwSEbLy6eVG2Vw49qNCB01tpEOA9zUZQpKAG8n_vcPMYOYmw3ZiAC7vYG26Rn308AOFpkIkMS480s9TIF-zbi2W0d87duYj7mvGxhprn43wXkDE4FbVHnkaSYU4rF21xhDzJ-SJU0_f6ofMFBxDYZuqiVl-xElDGs4TXyyoA-zPwd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار Daryl Caudle، رئیس عملیات نیروی دریایی: ناو هواپیمابر یو‌اس‌اس تئودور روزولت (CVN-71)، از ناوهای اتمی کلاس نیمیتز، در حال ترک سن‌دیگو برای اعزام به خاورمیانه است. این ناو به همراه گروه رزمی خود و بال هوایی یازدهم ناوگان، قرار است برای یک مأموریت طولانی‌مدت به منطقه سنتکام اعزام شود؛ مدت این مأموریت دست‌کم حدود ۷ ماه برآورد شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24370" target="_blank">📅 01:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo1WdGHa4POBnT6gbpeDiUmn0ZCgHIyIeIfg5Dhi8lGoVjQXrZ-4v5jg-NbiFXrce5PeIuh4oUGUgTKN79uL3UgEphbU3oOR6gt1QG6s7Z9cvtsZbAV9z53yjz_EhD7Jnem_h_xBzMmo3AtMTl1a_SfM5ZzPvT-Zg7VA6smfDjXIgoCSkA4WkdPj0tPGrCtETUfv0fT4VC2O1cPLXrid1bFIsoWGG88BEMwRs-B-boKqTZHlWxaGa6SjxgNYPjBlhXI0ehyX2zvj7VYkaK0DDuysA6QkJrbv-Iitp7fFijb21FP-INbESewcIWLwHnHmWm-FhgpeBORD1UnJisbBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با خرافات : تمام دایرکت پیغام اینه که ترامپ کلاه جنگ سرشه ( البته واقعا هم ترامپ اکثرا اتاق جنگ
مارالاگو
میره این کلاه سرشه و روز اول جنگ هم بود )
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24369" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=ghnGv6k7QYb4HTcYyTZJh0kUp5OCgp9SotDBcjRGtRQz7uz3VDcUAHqLZvKRC-VESrBqlHDfqlwuquIpSh6VIL2oEUvFBXgyi1Rw5F21CxkRdHHlbq-qEn3-1LUvf1srX8iVove9HS0tMzCIKaMo_8S9E9psT09P752LyRY4fVyaMDv2H_EyLcta3zfFm83lZY-Pl743YdamqZohs49H6tg5l5K8OXN7VFfNjxfRNKPglOqTXqT_mH89M9476pdlycueKBd0r0jNiVFJsjrSZHj-jxBp4CDvwFaDb3v_bkzgIytnBaWpRDQrvZFbBPlbewGo1HVC6PFcH_FHiDPuFVT3Vf_M_AkRyJzB_Twf8SeBHSRbxk2ZmrvOSmCgCJ-YqQZQULtsKUrzjPqpnZhE01VUmEfmD_m5_sKruejeOtdYAnPNlcE2DHomd3cng4v4a4vIVNW0igGeiZqqdNFMUrjh7VFYjiGKQ21l-9KfBgl1XggwpcsP_QhlY4iJu1Hfatwl4d0ovSQYGmi3hXHs1yBQadVbpYI0mPb7AxNuIxi7TbpcUeS-bJRsrkbbNWXn5ueP6S9mKPSsyIR3wcde55h93k3uHKQ36Axwkhg2OMluJELewD79_7ClWKVdDSshaCB-6H8Kl9W69L772KsXjmj5FqYSZgPOyMRjo_8H8o8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=ghnGv6k7QYb4HTcYyTZJh0kUp5OCgp9SotDBcjRGtRQz7uz3VDcUAHqLZvKRC-VESrBqlHDfqlwuquIpSh6VIL2oEUvFBXgyi1Rw5F21CxkRdHHlbq-qEn3-1LUvf1srX8iVove9HS0tMzCIKaMo_8S9E9psT09P752LyRY4fVyaMDv2H_EyLcta3zfFm83lZY-Pl743YdamqZohs49H6tg5l5K8OXN7VFfNjxfRNKPglOqTXqT_mH89M9476pdlycueKBd0r0jNiVFJsjrSZHj-jxBp4CDvwFaDb3v_bkzgIytnBaWpRDQrvZFbBPlbewGo1HVC6PFcH_FHiDPuFVT3Vf_M_AkRyJzB_Twf8SeBHSRbxk2ZmrvOSmCgCJ-YqQZQULtsKUrzjPqpnZhE01VUmEfmD_m5_sKruejeOtdYAnPNlcE2DHomd3cng4v4a4vIVNW0igGeiZqqdNFMUrjh7VFYjiGKQ21l-9KfBgl1XggwpcsP_QhlY4iJu1Hfatwl4d0ovSQYGmi3hXHs1yBQadVbpYI0mPb7AxNuIxi7TbpcUeS-bJRsrkbbNWXn5ueP6S9mKPSsyIR3wcde55h93k3uHKQ36Axwkhg2OMluJELewD79_7ClWKVdDSshaCB-6H8Kl9W69L772KsXjmj5FqYSZgPOyMRjo_8H8o8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«مشکل بزرگ این است که
پالایشگاه‌های روسیه در حال منفجر شدن هستند.
این در واقع یک مشکل خاورمیانه نیست؛ بیشتر مربوط به
روسیه و اوکراین
است که با یکدیگر درگیرند.
اوکراین در حال
هدف قرار دادن پالایشگاه‌های گازوئیل روسیه
است، چون روسیه بخش زیادی از فرآوری و پالایش را انجام می‌دهد. بنابراین این موضوع واقعاً جالب است.
من با رئیس‌جمهور زلنسکی صحبت کردم و گفتم:
«باید در مورد حمله به پالایشگاه‌ها کمی دست نگه داری.»
او هم گفت:
«احتمالاً همین کار را خواهیم کرد.»
»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24368" target="_blank">📅 01:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=Ub2wd0575knzowBjoectZQ_qNeBlYNClp1PZ-lhgaZOoAwm9RxUlzgXBFT_qdYVlEMOdRIEp25cKZoa6_6scOIpXdHSY7L8vML6jxIf-UeVMNwwMD7Ec43TiuugkcCnDvPQf4f80Xqj4f2pqR2wCQW8531HcrEQZg4Cu1KfrurMv5HdKhNIBxOFhImTszx2ifG_DiacVTrH2NiRCZ19RfC2liRiLXoSWymav15tGJm8MaugeeVp8UdHBiGJ9B9ktXW1ReT4arAqn-05QxjZld7ZpZBG7sBlMOXnmHdihG-LqPPPVtbVABLM9ze-B8hTHzr1UARirC6itd5x63hcZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=Ub2wd0575knzowBjoectZQ_qNeBlYNClp1PZ-lhgaZOoAwm9RxUlzgXBFT_qdYVlEMOdRIEp25cKZoa6_6scOIpXdHSY7L8vML6jxIf-UeVMNwwMD7Ec43TiuugkcCnDvPQf4f80Xqj4f2pqR2wCQW8531HcrEQZg4Cu1KfrurMv5HdKhNIBxOFhImTszx2ifG_DiacVTrH2NiRCZ19RfC2liRiLXoSWymav15tGJm8MaugeeVp8UdHBiGJ9B9ktXW1ReT4arAqn-05QxjZld7ZpZBG7sBlMOXnmHdihG-LqPPPVtbVABLM9ze-B8hTHzr1UARirC6itd5x63hcZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای هنوز روی میز شماست؟
ترامپ:
«نمی‌خواهم درباره آن چیزی بگویم. منظورم این است که
ممکن است چنین اتفاقی بیفتد
، اما نمی‌خواهم بیشتر از این درباره‌اش صحبت کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24367" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59060499.mp4?token=EdxcjjFLC7Ff2iRK0hMhZXOj_zmhosFD72x8hCd4H7-wbYUHExm_qWcNOi1JY8hZziQn4CfEhzedleg-noVW3it-B-bIUjF1q7ggG6QSDzUe3vXj1uU1a8mo6xV3Twfim4CxKHE6XGE9Hdu-E3bdI38wgclw6EH6YeAyP960eJxxP-qgc7qiUtdwh7jI2A05iQyGiK4P1G-jSOJxtwcM_GinPFDb8mM-NkLOvw8VioxRnaKHnfwL7oVdoXu2OBOd2LeDscanw5w37wFdSXrozhBUtt3dCu9eju_MEIrbjBKybJ7Kw3GqCxPccE4lgE9bxbygsOVDLiRnA4fHK-7NXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59060499.mp4?token=EdxcjjFLC7Ff2iRK0hMhZXOj_zmhosFD72x8hCd4H7-wbYUHExm_qWcNOi1JY8hZziQn4CfEhzedleg-noVW3it-B-bIUjF1q7ggG6QSDzUe3vXj1uU1a8mo6xV3Twfim4CxKHE6XGE9Hdu-E3bdI38wgclw6EH6YeAyP960eJxxP-qgc7qiUtdwh7jI2A05iQyGiK4P1G-jSOJxtwcM_GinPFDb8mM-NkLOvw8VioxRnaKHnfwL7oVdoXu2OBOd2LeDscanw5w37wFdSXrozhBUtt3dCu9eju_MEIrbjBKybJ7Kw3GqCxPccE4lgE9bxbygsOVDLiRnA4fHK-7NXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
درباره ممنوعیت صادرات گازوئیل چطور؟
ترامپ:
«ما این موضوع را
خیلی جدی در حال بررسی
هستیم. چنین اقدامی گاهی می‌تواند باعث
افزایش جزئی قیمت بنزین خودروها
شود.
بنابراین با جدیت در حال بررسی آن هستیم و
ممکن است این کار را انجام دهیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24366" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس: تحرکات و آماده‌سازی‌های نظامی آمریکا در منطقه، احتمال اقدام نظامی جدید علیه ایران را افزایش داده است.
ترامپ نیز گفته همچنان گزینه ازسرگیری حملات علیه ایران را در نظر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24365" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=GYsYlBMhX7U1-JPr_ebA4PETZGtr3Gz4W3uJ3VxOWoAvRe9rkPG7yyPPLd6sDf0yCfRxdV8fq1DS68qrPCwCPqs7F4-iA66SHId_9eua9eN_LUsxDAqEW-aNRRgPSRMlDcMeCJ6zYfx8Hxj7zydjrKIjZM8CNcY2rKwwxtzeR2LBGCfIbKPPcCDY0BSnUnGLQogol-8e6oyoXWGtyeeTtdLPHBZYjn13_wIqBYOq4mKctB0hp7vV45QJf7cNA620mpBExetNSO2Qb3f2ftsBb8Zq-rhltuhJLx6MWylzI0m8rda31aeziA7GHNsc-5EBEzZoc7O4hStOJa3KyteU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=GYsYlBMhX7U1-JPr_ebA4PETZGtr3Gz4W3uJ3VxOWoAvRe9rkPG7yyPPLd6sDf0yCfRxdV8fq1DS68qrPCwCPqs7F4-iA66SHId_9eua9eN_LUsxDAqEW-aNRRgPSRMlDcMeCJ6zYfx8Hxj7zydjrKIjZM8CNcY2rKwwxtzeR2LBGCfIbKPPcCDY0BSnUnGLQogol-8e6oyoXWGtyeeTtdLPHBZYjn13_wIqBYOq4mKctB0hp7vV45QJf7cNA620mpBExetNSO2Qb3f2ftsBb8Zq-rhltuhJLx6MWylzI0m8rda31aeziA7GHNsc-5EBEzZoc7O4hStOJa3KyteU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
فکر می‌کنید این جنگ با ایران را از طریق
جنگ اقتصادی
که وزارت خزانه‌داری به راه انداخته پیروز می‌شویم یا از طریق حملات نظامی؟
ترامپ:
فکر می‌کنم
هر دو
. از هر دو طریق پیروز خواهیم شد. از نظر نظامی، واقعاً
تا حد زیادی پیروز شده‌ایم
، اما این به این معنا نیست که حملات را متوقف کرده‌ایم.
ما قطعاً
با اختلاف زیادی در حال پیروز شدن هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24364" target="_blank">📅 00:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=FKyAX8GJHI8V8JcmMgYExbgqz3qn2miAx3yt7lO1hnaHl0bLavugJfRkk_eIePWEadPRiX4xLl5QHVcRUNzLVoK-DuXeQrx0GI-T_ZUm4JkWLlGOpK6_1qA9E1X2Wfcz4G_PdOy8UFfnFU8DMZlzUDrGN_fbUDd0vT9xnEL10kOwAEnwqfrLm18X_MYHbFxS5jpYEGTx3v7XjwzDSPO87LBvf6zL_13eK16XAdqi8BCGmYEV1_jMqgALWqZ0GgjiWYF6TKumUtijcknsGTTZZEmEoGvLGY-NLsWF-XAghvLGXmNBf27Eo_CKIc2OVPNmwKaiwDcXClOoYKrnKdnRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=FKyAX8GJHI8V8JcmMgYExbgqz3qn2miAx3yt7lO1hnaHl0bLavugJfRkk_eIePWEadPRiX4xLl5QHVcRUNzLVoK-DuXeQrx0GI-T_ZUm4JkWLlGOpK6_1qA9E1X2Wfcz4G_PdOy8UFfnFU8DMZlzUDrGN_fbUDd0vT9xnEL10kOwAEnwqfrLm18X_MYHbFxS5jpYEGTx3v7XjwzDSPO87LBvf6zL_13eK16XAdqi8BCGmYEV1_jMqgALWqZ0GgjiWYF6TKumUtijcknsGTTZZEmEoGvLGY-NLsWF-XAghvLGXmNBf27Eo_CKIc2OVPNmwKaiwDcXClOoYKrnKdnRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«فکر می‌کنم اتفاقی که خواهد افتاد این است که
خیلی زود در این جنگ پیروز خواهیم شد
و به‌محض اینکه پیروز شویم، قیمت نفت
به‌شدت کاهش پیدا می‌کند
و به سطحی که پیش از جنگ داشت، برمی‌گردد.
و نکته کلیدی این است که
ایران سلاح هسته‌ای نخواهد داشت.
این، کلید حل این مسئله است.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24363" target="_blank">📅 00:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">معاون پزشکیان: برای عبور از زمستان به همراهی مردم نیاز داریم.
@WarRoom
Yashar : Winter is coming</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24362" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الجزیره : تنش در تنگه هرمز پس از رد پیشنهاد ایران ادامه دارد.
الجزیره گزارش داده پس از رد طرح تهران، نگرانی‌ها درباره ازسرگیری درگیری مستقیم افزایش یافته است. همچنین
گزارش‌هایی از انفجار در
محدوده
تنگه هرمز
خبر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24361" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدای انفجار در تنگه  @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24360" target="_blank">📅 23:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a093c8ddbb.mp4?token=dnvPSIYegG2nSDcIyIgHktTsxjz-0bmOKa9HmAU6Hgu4VAdI0gRDaUDKKrJyRhK3HHqATVKjhm5g6dvm35zQTtT1UqHgzhiGw9jicSz0EuOA-NUfa2Iy4lkwg2TthDv9Nfdzhdr8sMry8foAkgIs0DMKzh_X0vpN8pyPIIFDz7JJhsrPFM0EHNI5M0vBBzuCs_9dObmPstDJP9IZBf1a9XeoI690DNJCvohDMOYsLQhXgNgDyAYdrv58YxJNvqoalX9wJLS4DYcFfpjeghPTB56A720POoOTgds3FqfvNAPsbqhu2HbL0sYgrK-0oX9aw9JJmaLLAeDelwkwpJglFhPnTMM1BKB1oJukw93QWwMhNSV9LtWbiD_hU4oWtzNpo1s6KkiIzwnKw2jrSSNcs5HTcrRiXhSgwPHsQTY94BxiutpO8qIdq64L2tRhm_BwG5_6mc0FbIXHrtm8gr1SBVgN-WXya9U0l4zgTxMCmAj1tQqGECDQoeJVnTj5RLBhDunvPW6acCBl-p-E4NOOpd5uhhEz05cHinsgeLwPeVIxmGsoIE85YGoEXz2ArHsHCcEqDO7M_gNZuJhcXFtJVBycaD-kAM_pkU75m9CckzxVyE-FUpUSrElSHD1XcDNZy0uEFGC6xX6hD5KXo1SiKYpugBF3npPvXZNTydA_PAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a093c8ddbb.mp4?token=dnvPSIYegG2nSDcIyIgHktTsxjz-0bmOKa9HmAU6Hgu4VAdI0gRDaUDKKrJyRhK3HHqATVKjhm5g6dvm35zQTtT1UqHgzhiGw9jicSz0EuOA-NUfa2Iy4lkwg2TthDv9Nfdzhdr8sMry8foAkgIs0DMKzh_X0vpN8pyPIIFDz7JJhsrPFM0EHNI5M0vBBzuCs_9dObmPstDJP9IZBf1a9XeoI690DNJCvohDMOYsLQhXgNgDyAYdrv58YxJNvqoalX9wJLS4DYcFfpjeghPTB56A720POoOTgds3FqfvNAPsbqhu2HbL0sYgrK-0oX9aw9JJmaLLAeDelwkwpJglFhPnTMM1BKB1oJukw93QWwMhNSV9LtWbiD_hU4oWtzNpo1s6KkiIzwnKw2jrSSNcs5HTcrRiXhSgwPHsQTY94BxiutpO8qIdq64L2tRhm_BwG5_6mc0FbIXHrtm8gr1SBVgN-WXya9U0l4zgTxMCmAj1tQqGECDQoeJVnTj5RLBhDunvPW6acCBl-p-E4NOOpd5uhhEz05cHinsgeLwPeVIxmGsoIE85YGoEXz2ArHsHCcEqDO7M_gNZuJhcXFtJVBycaD-kAM_pkU75m9CckzxVyE-FUpUSrElSHD1XcDNZy0uEFGC6xX6hD5KXo1SiKYpugBF3npPvXZNTydA_PAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس با لباس غیرنظامی از داخل خانه‌ها خمپاره و موشک شلیک می‌کنند.و بعد پس از کشته‌شدن این افراد در حملات اسرائیل، آنان را غیرنظامی معرفی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24359" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تایمز آو اسرائیل:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل،
امروز به ابوظبی سفر کرد تا با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کند.
این سفر با یک هواپیمای خصوصی انجام شده و نتانیاهو روز را در ابوظبی سپری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24358" target="_blank">📅 22:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حمله درست و تند مجری انگلیس به وزیر دفاع انگلستان پس از خنثی شدن طرح حمله به پایگاه هوایی مشترک انگلیس/و امریکا فرفورد:
‏“باید میان اعزام تروریست‌ها از
سوی ایران
و ورود آنها از طریق قایق‌های مهاجران غیرقانونی، رابطه‌ای مستقیم برقرار کنید. به شما هشدار داده بودند، اما شما به‌جای اقدام، برای سپاهی ها هتل گرفتید. این افراد احتمالا از جای دیگری، مشخصابا هدف اجرای این عملیات، وارد کشور شده‌اند
‏هنوز متوجه نشدید که اگر یک دولت متخاصم باشید، یکی از بهترین روش‌ها برای وارد کردن عوامل خود، فرستادن آنها به‌صورت غیرقانونی با قایق ست”
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24357" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه سعودی
Ajel
به نقل از
سخنگوی نیروهای مسلح دولت یمن، سرتیپ ماجد عبدالله النزیلی
: عملیات ۷۲ ساعت گذشته ما باعث کشته و زخمی‌شدن ۲۳۱۶ نیروی حوثی، از جمله
چهار متخصص ایرانی در عملیات پهپادی و موشکی در استان تعز
شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24356" target="_blank">📅 21:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال 15 اسرائیل:
مذاکرات پیشرفت چشمگیری نداشته و میانجی‌گران از مواضع طرف ایرانی ناامید شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24355" target="_blank">📅 21:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لحظه هلاکت و متلاشی شده تروریستی که نوآ ارگامان را در ۷ اکتبر ربوده بود
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24354" target="_blank">📅 21:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز، آخرین وضعیت فیرفورد : بامداد یکشنبه، ۵ مرد پس از مشاهده سه خودروی مشکوک در نزدیکی پایگاه هوایی فیرفورد انگلیس بازداشت شدند. ترامپ اعلام کرد مظنونان از قبل تحت نظر آمریکا و انگلیس بودند و پس از نزدیک‌شدن به منطقه پایگاه دستگیر شدند؛ هرچند جزئیات عملیات مراقبت هنوز کاملاً روشن نیست. در جریان تحقیقات، مواد مشکوکی از خودروها توقیف شد و تیم خنثی‌سازی بمب ارتش وارد عمل شد. به‌دلیل احتمال انفجار، حدود ۸۵ خانه تخلیه شدند. فیرفورد پایگاه مورد استفاده بمب‌افکن‌های آمریکایی در حملات علیه ایران است و سپاه پیش‌تر درباره استفاده از آن هشدار داده بود. آخرین وضعیت: هر پنج نفر همچنان در بازداشت پلیس ضدتروریسم هستند؛ اما وجود بمب آماده انفجار، هویت و وابستگی مظنونان و ارتباط احتمالی آن‌ها با ایران هنوز رسماً تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24353" target="_blank">📅 20:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c011d84cee.mp4?token=U3KvpC18akP8eQBxacqzwt9lTfYljJg-658r55m0jAvdxn1_pACG0rOvX9-jFXftssDQRHAqGTk4c-wQGHcRNT_6UAYNiOKSiQ2yul_6eR_rbB9ATWqNgbDIuwacL6w9OzW0PD5Q1l1inahrDejxNjglfocFwcAnaP2PaQi_RPnPvw8l3PaD_EwyIipLSu4NOGXyR_SGFILv00Oe1spCsmOmaGPLEi_ZJsgJ6kuRhY-6zTn_03IsBRDw5tex2ttnQIj0bSgfuJ3t8gVu6U5M46ed5Z-ea2P_jsMSddZ5uzgsMIxMb5Qzr3UrG4Juckv6MKifWhMXiyRBJdvmfgs8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c011d84cee.mp4?token=U3KvpC18akP8eQBxacqzwt9lTfYljJg-658r55m0jAvdxn1_pACG0rOvX9-jFXftssDQRHAqGTk4c-wQGHcRNT_6UAYNiOKSiQ2yul_6eR_rbB9ATWqNgbDIuwacL6w9OzW0PD5Q1l1inahrDejxNjglfocFwcAnaP2PaQi_RPnPvw8l3PaD_EwyIipLSu4NOGXyR_SGFILv00Oe1spCsmOmaGPLEi_ZJsgJ6kuRhY-6zTn_03IsBRDw5tex2ttnQIj0bSgfuJ3t8gVu6U5M46ed5Z-ea2P_jsMSddZ5uzgsMIxMb5Qzr3UrG4Juckv6MKifWhMXiyRBJdvmfgs8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که سپاه تنگه رو بسته و دیگه خودشم کلید نداره مونده پشت در ، و صدا هایی که هر شب میاد
@WarRoom
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24351" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای انفجار در تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24350" target="_blank">📅 20:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a52224fd.mp4?token=Wnb1xtfHn21JN8em97WXhNrLnN0I7xBoR0BKmeqjhVvuur-NkqErbBH08olFU1NQ5edI0Y5WmqYJ4h-JmYZj4wz5x80vjPjsTcYG3m45fyknQESCzeHSF_b7Ftkp97iFYIHPR7gstexBEd1dfdurv3DHlAxzoP-HRVKCSo5aGpo2oQE2ub9LSrq23oCOxB9zj36NVSQN7IGbhJKkaHU3lF-8ciknrvsSMmfJzh0ui_UXauN778k5v_AvalVwS9EIQCq5XVM5iOnJbYq6RP7AOt99H2AC7cAlJ51shdrkPTgZB9RUH3--xhI58547sCAKXnBccD925N5rDowdCz692g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a52224fd.mp4?token=Wnb1xtfHn21JN8em97WXhNrLnN0I7xBoR0BKmeqjhVvuur-NkqErbBH08olFU1NQ5edI0Y5WmqYJ4h-JmYZj4wz5x80vjPjsTcYG3m45fyknQESCzeHSF_b7Ftkp97iFYIHPR7gstexBEd1dfdurv3DHlAxzoP-HRVKCSo5aGpo2oQE2ub9LSrq23oCOxB9zj36NVSQN7IGbhJKkaHU3lF-8ciknrvsSMmfJzh0ui_UXauN778k5v_AvalVwS9EIQCq5XVM5iOnJbYq6RP7AOt99H2AC7cAlJ51shdrkPTgZB9RUH3--xhI58547sCAKXnBccD925N5rDowdCz692g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه کامل صحبتهای ،
عباس عراقچی، وزیر خارجه
رژیم
، با شبکه NBC:
ما
کاملاً آماده ازسرگیری جنگ هستیم
و در برابر هرگونه تجاوز جدید، حتی اگر به
«جنگ آخرالزمانی»
منجر شود، ایستادگی می‌کنیم؛ اما همزمان
برای دیپلماسی آماده‌ایم و انتخاب با ترامپ است.
ترامپ در جنگ قبلی خواستار
تسلیم بدون قیدوشرط ایران در دو روز
بود، اما اکنون
هشت ماه است جنگ ادامه دارد و نتیجه‌ای نداشته است.
یک
طرح منطقی برای توافق
روی میز است و با وجود اینکه ترامپ آن را رد کرده، ما همچنان منتظر
پاسخ رسمی آمریکا از طریق میانجی‌ها
هستیم. ما به
انتخابات میان‌دوره‌ای آمریکا اهمیتی نمی‌دهیم و منافع ملی ایران برایمان مهم است.
غنی‌سازی
۶۰ درصد غیرقانونی نیست
و برای اهداف صلح‌آمیز انجام می‌شود؛ ما NPT را نقض نکرده‌ایم و مسائل باقی‌مانده را می‌توان از طریق مذاکره حل کرد.
جنگ راه‌حل نیست.
برای بازگشایی هرمز نیز
طرح هفت‌روزه‌ای
ارائه کرده‌ایم: آمریکا طی چهار یا پنج روز اقدامات موردنظر را انجام دهد،
روز ششم تنگه باز شود و روز هفتم مذاکرات برای توافق نهایی از سر گرفته شود.
همچنین در داخل ایران
چند مرکز قدرت وجود ندارد
؛ دولت، سپاه، شورای عالی امنیت ملی، مجلس و وزارت خارجه
همه در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24349" target="_blank">📅 19:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b0a03b2.mp4?token=JF81wdOB17VPJXfJblColV8JDmllp_r5CcM-WjtL9R0hyHaCDyHa7byTGaKrqx_no92zpA0ap7roFufE4VI2F53YNrUR5IQUVx44PWAXR9aXpfVBTu6FqAP7OORENjZ_XT1G3mMRaHM7fvP4LYJO6YRyas0sjhVZrwwQCwAWYHYhsBG4OPVm1uDzmUvfKuexWbh6rali3TY1LEXf0medPaQYUqoGgZopc20Ymwo4xn2ceEAKq7Et5A965r05inPvfd0y8u8UAGOLpk2ZPuWpO9AUwtJP4C5bX8VNj479RhoV0hM2k1rgALtaZHT_VFG5G6DIRIQKax-SruGD9hIQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b0a03b2.mp4?token=JF81wdOB17VPJXfJblColV8JDmllp_r5CcM-WjtL9R0hyHaCDyHa7byTGaKrqx_no92zpA0ap7roFufE4VI2F53YNrUR5IQUVx44PWAXR9aXpfVBTu6FqAP7OORENjZ_XT1G3mMRaHM7fvP4LYJO6YRyas0sjhVZrwwQCwAWYHYhsBG4OPVm1uDzmUvfKuexWbh6rali3TY1LEXf0medPaQYUqoGgZopc20Ymwo4xn2ceEAKq7Et5A965r05inPvfd0y8u8UAGOLpk2ZPuWpO9AUwtJP4C5bX8VNj479RhoV0hM2k1rgALtaZHT_VFG5G6DIRIQKax-SruGD9hIQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل گیتس درباره جفری اپستین:
بعد از آشنایی، اپستین گفت می‌تواند برای
سلامت جهانی میلیاردها دلار جمع‌آوری کند
؛ بدون دریافت پول یا داشتن نقشی در این کار. اما این طرح
کاملاً به بن‌بست رسید.
گیتس گفت وقت گذراندن با اپستین، مانند بسیاری افراد دیگر، به
اعتبار او کمک کرد و این موضوع بسیار تأسف‌بار است.
او تأکید کرد که در آن دیدارها
هیچ زنی حضور نداشت، هیچ ارتباط مالی وجود نداشت و هرگز به جزیره اپستین نرفته است.
گیتس همچنین گفت ناکامی دولت در پرونده فلوریدا برای
اعمال مجازات و شناسایی اتفاقات در حال وقوع، یک شکست باورنکردنی نظام قضایی
بود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24348" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مجری NBC: آیا درست است که ترامپ در حال آماده‌شدن برای ازسرگیری حملات نظامی پس از انتخابات میان‌دوره‌ای است؟  مایک والتز، نماینده آمریکا در سازمان ملل: این گزارش‌ها بر اساس منابع ناشناس است.آنچه می‌توانم بگویم این است که رئیس‌جمهور همه گزینه‌ها را روی میز نگه…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24347" target="_blank">📅 19:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bae950f91.mp4?token=W4JH1oeB8_oh38JXhDu7k9rgSJvn_IrmYVdKubRRbQsHTRq1JxEoP8-8oJvShdqwbCesb-cXhP-xrdtGSjdCHeyXc2jm68k8GyQLbuiY7z1XNjF4cbCkfN0KKPvDW39zo8qV03X_2ycfFa2KpWDphQGqIjQuDQg-8969V9ZzbB6DWiD2sivmnEfeC4Fs3XMMu5m3KrtJd8PyAxjv-bRHvTqorCF2iPw1-Ee1I5jKQTt0p9wnMZvrW4AifKS2sUFYwWEu4uQImS4VoX1VMgaHUzj4Mjt_H81qnyR198ILCLbND3Kxvheo3n3me6CXhD-uYJM6N7ZbCG5wYlfYztABNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bae950f91.mp4?token=W4JH1oeB8_oh38JXhDu7k9rgSJvn_IrmYVdKubRRbQsHTRq1JxEoP8-8oJvShdqwbCesb-cXhP-xrdtGSjdCHeyXc2jm68k8GyQLbuiY7z1XNjF4cbCkfN0KKPvDW39zo8qV03X_2ycfFa2KpWDphQGqIjQuDQg-8969V9ZzbB6DWiD2sivmnEfeC4Fs3XMMu5m3KrtJd8PyAxjv-bRHvTqorCF2iPw1-Ee1I5jKQTt0p9wnMZvrW4AifKS2sUFYwWEu4uQImS4VoX1VMgaHUzj4Mjt_H81qnyR198ILCLbND3Kxvheo3n3me6CXhD-uYJM6N7ZbCG5wYlfYztABNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری NBC
:
آیا درست است که ترامپ در حال آماده‌شدن برای ازسرگیری حملات نظامی پس از انتخابات میان‌دوره‌ای است؟
مایک والتز، نماینده آمریکا در سازمان ملل:
این گزارش‌ها بر اساس منابع ناشناس است.آنچه می‌توانم بگویم این است که
رئیس‌جمهور همه گزینه‌ها را روی میز نگه خواهد داشت
تا اطمینان حاصل کند جهان از اینکه ایران با در اختیار داشتن یک سلاح هسته‌ای، جهان را گروگان بگیرد، در امان باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24346" target="_blank">📅 19:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس:
میانجی‌های قطری در آخر هفته به‌صورت جداگانه بین مذاکره‌کنندگان ایران و آمریکا در رفت‌وآمد بوده‌اند و درباره
تغییرات متن توافق پیشنهادی
گفت‌وگو کرده‌اند.
انتظار می‌رود مقام‌های قطری در صورت ادامه روند،
از روز دوشنبه به‌صورت جداگانه با عباس عراقچی و استیو ویتکاف
دیدار کنند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24345" target="_blank">📅 19:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران خواهان توافق است، اما توافقی ایرانیا میخوان با توافقی که ما میخوایم فرق داره
ترامپ همچنین گفت :
اون ایرانیا در مذاکرات «زیاده‌روی کردن»!!!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24344" target="_blank">📅 19:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس:
ترامپ درباره احتمال ازسرگیری حملات آمریکا به ایران گفت:
«همیشه به آن فکر می‌کنم.»
او در پاسخ به این پرسش که آیا حملات مجدد را بررسی می‌کند، این جمله را بیان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24343" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آکسیوس , باراک راوید:
منابع مطلع می‌گویند مذاکره‌کنندگان آمریکایی به ایران اعلام کرده‌اند
تهران حق ندارد برای تنگه هرمز شرط تعیین کند
و آمریکا معتقد است ایران کنترل انحصاری بر این آبراه ندارد. این موضع یکی از اصلی‌ترین اختلافات فعلی در مذاکرات غیرمستقیم است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24342" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پروازهای ایران همچنان به ۱۰ کشور برقرار است
چین، روسیه، ترکیه، افغانستان، پاکستان، ارمنستان، بلاروس، تاجیکستان، ویتنام و مالزی
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24341" target="_blank">📅 19:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار سی‌بی‌اس:
یک مقام ایرانی به من گفته است که
مذاکرات ایران و آمریکا که قرار بود روز دوشنبه برگزار شود، لغو شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24340" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران: «ما اکنون رئیس‌جمهوری داریم که چینی‌ها برای او احترام قائل‌اند. چین کمک‌های خود به ایران را به‌طور قابل‌توجهی کاهش داده است. تنها حدود ۱۵ میلیون بشکه دیگر از نفت ایران روی آب قرار دارد و پس از آن، ایران دیگر…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24339" target="_blank">📅 19:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود. آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24338" target="_blank">📅 19:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bac83090.mp4?token=Za5zmirhqFKPzLEbc70RfQo-xGaLWS3LSrBjQZLPE9A6eb8JF-3f_U19vOYr-vxQB8nhL-6ren56uS6PosekCzLl83Z4ELSNSwU_tmnVyjz_29x0ybj2O2AD0nV9GuO8-Dgu6V0mvKL3ZBOjtspaEtoUe7_nWow74yRlqv0FAgCraXVK7nNqMGvkSa5GcvONnz17ZIHyg_74h2aLN94DrPx8nR5aHloGHjfQHi2c2L7NgQlLPzOc827zzSzlmX7ZN-Uqb7R4iRIBxa3oQ0eT2hxRYrs0BNTROsM57kYyrBPZKiZdM5Pjve02_BZdQZoh6ENlvniVXFkIHDf5LFXFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bac83090.mp4?token=Za5zmirhqFKPzLEbc70RfQo-xGaLWS3LSrBjQZLPE9A6eb8JF-3f_U19vOYr-vxQB8nhL-6ren56uS6PosekCzLl83Z4ELSNSwU_tmnVyjz_29x0ybj2O2AD0nV9GuO8-Dgu6V0mvKL3ZBOjtspaEtoUe7_nWow74yRlqv0FAgCraXVK7nNqMGvkSa5GcvONnz17ZIHyg_74h2aLN94DrPx8nR5aHloGHjfQHi2c2L7NgQlLPzOc827zzSzlmX7ZN-Uqb7R4iRIBxa3oQ0eT2hxRYrs0BNTROsM57kYyrBPZKiZdM5Pjve02_BZdQZoh6ENlvniVXFkIHDf5LFXFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ما اکنون رئیس‌جمهوری داریم که چینی‌ها برای او احترام قائل‌اند. چین کمک‌های خود به ایران را به‌طور قابل‌توجهی کاهش داده است. تنها حدود
۱۵ میلیون بشکه دیگر از نفت ایران روی آب قرار دارد
و پس از آن، ایران دیگر چیزی برای مبادله با دیگران نخواهد داشت. احتمالاً طی
دو هفته آینده
آخرین محموله‌های نفت ایران به چین تحویل داده می‌شود و پس از آن چیزی باقی نخواهد ماند. ایرانی‌ها می‌گویند در صورت دستیابی به توافق، تنگه هرمز را باز خواهند کرد؛
تنگه همین حالا باز است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24337" target="_blank">📅 19:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6805c8bfd.mp4?token=dysY_Uz2IxS3CWTK-G7rN8hVDloLvSkegeH2Gnoi86D3KiCzY6e8_b2qxKqQwB5EkNSqR3xRHhnY88rq-CrJ0qb2bwBHHiwWzcmAnijA-o2xGAwmw6WmfGTurizVbfJGcQUyIDdJ6TH7KFrv1b7imxgHmao3SS-UFXAKFtEP5EZZs61GFPAGZtfqCV02iOK7EdH28Z1Qy7fTS-2MA2EVBTI52AmJ5zFBKUPtgTbCJ-wdijr8Vv_1I_SNBaifg7EVL0ESCYXSIpZXwIgLoSNiaF2iPRtGm9melalqxtrnb33M4X3AfFX3eBE2mmJ95UYAn8ibGgtJjBiGxV3uT1P1Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6805c8bfd.mp4?token=dysY_Uz2IxS3CWTK-G7rN8hVDloLvSkegeH2Gnoi86D3KiCzY6e8_b2qxKqQwB5EkNSqR3xRHhnY88rq-CrJ0qb2bwBHHiwWzcmAnijA-o2xGAwmw6WmfGTurizVbfJGcQUyIDdJ6TH7KFrv1b7imxgHmao3SS-UFXAKFtEP5EZZs61GFPAGZtfqCV02iOK7EdH28Z1Qy7fTS-2MA2EVBTI52AmJ5zFBKUPtgTbCJ-wdijr8Vv_1I_SNBaifg7EVL0ESCYXSIpZXwIgLoSNiaF2iPRtGm9melalqxtrnb33M4X3AfFX3eBE2mmJ95UYAn8ibGgtJjBiGxV3uT1P1Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود.
آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24336" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f3c2ed42c.mp4?token=a8ec670fn1bqRtT1YsjhX5ZNDni1n8IRzhK47JaLnQ_VZQy02FnI2zw7aKhOs-jHeYnrASxKKWM8NI5sWd9j6eFUMU3cRizlAF5PbV3AUWGpKkyGX-swZDGbN49Bu43tvkKwMafGNURnDYUol1CVTqdGgyHnAFhzx5Iw7oE0P_Hi7n8_yho9gANFmkRzb67IaJJtHl0oGtEf-UucXlUUBw62DQtSIN1i9EB5j9CQ7Vo5lcRlbmKl2y0tlpY1XWl9qH5IU3WDuCBhcGpxgZDf_OcyHgQxVN13T2JUqqbGBGmC4mz_fU6wO8wB4kP4Ow4sN6nhzrkoeR2N5eUUxJyiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f3c2ed42c.mp4?token=a8ec670fn1bqRtT1YsjhX5ZNDni1n8IRzhK47JaLnQ_VZQy02FnI2zw7aKhOs-jHeYnrASxKKWM8NI5sWd9j6eFUMU3cRizlAF5PbV3AUWGpKkyGX-swZDGbN49Bu43tvkKwMafGNURnDYUol1CVTqdGgyHnAFhzx5Iw7oE0P_Hi7n8_yho9gANFmkRzb67IaJJtHl0oGtEf-UucXlUUBw62DQtSIN1i9EB5j9CQ7Vo5lcRlbmKl2y0tlpY1XWl9qH5IU3WDuCBhcGpxgZDf_OcyHgQxVN13T2JUqqbGBGmC4mz_fU6wO8wB4kP4Ow4sN6nhzrkoeR2N5eUUxJyiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
شب گذشته، رکورد تازه‌ای در انتقال نفت از تنگه هرمز ثبت کردیم؛ حتی بیشتر از میزان نفتی که پیش از آغاز جنگ از این مسیر عبور می‌دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24335" target="_blank">📅 16:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8efbe7394.mp4?token=g03fXxAhdgZrpCCqfhtCslX7RsGLuhcv-4705zu3OuNUb6eKVhQljOa4W8lIFTx5OdterccrfARAMgzbzcRXhtCV8mLweSwIDlF7oPcvKFJPCnbyld_oCi4RcTDLjWEC4HwZXJ2UwRkOZBLCA6xC2S4vyfN1g52zBPJpbCK53MH7hCLtc8BL51x1xYXNhuTMXLw-1OhWJt2nQo7P8URCVecRHn-0f9XlXdkRJBF_tCdL49TeaEfl9GQL3_JHkByzZUEzjQXNdW8f1IpUxorwkFbPyc4Oq7jSaGKmiPATLmbn9vjQ7Cm1Qkj73uV-FrMjOs-tcvQtdrr3MHdPa7dlv4vFMYeKHKjfgwvHFqr-NNqmv-MbjGtvF4onvOoWPMN8YfHaN4w15--ileVsTl_7s0LJ4OpURpHY4keBnadVsIRSBu5AJz7bitQ9l78DpJ2NvycSnzebya55KgIGuoWmBBcuXf5E41WWXMvs5Mmz_PjG7zHxm0xtQ5Tx2upKO7HW6UaQUPXtNSAOvQ1CXbKOjsQxgGbvwDL0ITKvSfEIGOMsJkDfWP7wCTewU5oJQ77-FaoRH3s9Rh8EXhJODQlo46a2PBPqHgwGX7HuButjiN__zM_-d0P3N4efNHJY5K-c6kjXwAxqa10TbR1fyPGP86jiCrClpGmHCVFEBl1Ih-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8efbe7394.mp4?token=g03fXxAhdgZrpCCqfhtCslX7RsGLuhcv-4705zu3OuNUb6eKVhQljOa4W8lIFTx5OdterccrfARAMgzbzcRXhtCV8mLweSwIDlF7oPcvKFJPCnbyld_oCi4RcTDLjWEC4HwZXJ2UwRkOZBLCA6xC2S4vyfN1g52zBPJpbCK53MH7hCLtc8BL51x1xYXNhuTMXLw-1OhWJt2nQo7P8URCVecRHn-0f9XlXdkRJBF_tCdL49TeaEfl9GQL3_JHkByzZUEzjQXNdW8f1IpUxorwkFbPyc4Oq7jSaGKmiPATLmbn9vjQ7Cm1Qkj73uV-FrMjOs-tcvQtdrr3MHdPa7dlv4vFMYeKHKjfgwvHFqr-NNqmv-MbjGtvF4onvOoWPMN8YfHaN4w15--ileVsTl_7s0LJ4OpURpHY4keBnadVsIRSBu5AJz7bitQ9l78DpJ2NvycSnzebya55KgIGuoWmBBcuXf5E41WWXMvs5Mmz_PjG7zHxm0xtQ5Tx2upKO7HW6UaQUPXtNSAOvQ1CXbKOjsQxgGbvwDL0ITKvSfEIGOMsJkDfWP7wCTewU5oJQ77-FaoRH3s9Rh8EXhJODQlo46a2PBPqHgwGX7HuButjiN__zM_-d0P3N4efNHJY5K-c6kjXwAxqa10TbR1fyPGP86jiCrClpGmHCVFEBl1Ih-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:به محض اینکه ایران تسلیم شود، به محض اینکه جنگ به پایان برسد، که این اتفاق به زودی خواهد افتاد، قیمت نفت به شدت کاهش خواهد یافت.
قیمت نفت به طور چشمگیری کاهش خواهد یافت و تمام قیمت‌ها پایین خواهند آمد، اما قیمت مواد غذایی به میزان قابل توجهی از زمان ریاست جمهوری بایدن کاهش یافته است. تقریباً تمام قیمت‌ها به میزان زیادی کاهش یافته‌اند.
ما حجم بسیار زیادی از نفت را خارج می‌کنیم؛ شب گذشته، ما حجم بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از زمانی که قبل از جنگ این کار را انجام می‌دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24334" target="_blank">📅 16:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ در ‌تروث : در حال حاضر، شمار افرادی که در ایالات متحده مشغول کار هستند، از هر زمان دیگری در تاریخ کشورمان بیشتر است!
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24333" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امیر حاتمی، شهید زنده، فرمامده ارتش جمهوری اسلامی:
جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24332" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d096c16704.mp4?token=ZaBeakoeYVbSnTM4_R2cwcA7R_tKNJLxG9IY99ke7sXfR7jwSEIf5rDoryXubCmnZ3XmQFn1ErCrF53eWBBJDwszrKwdjZ4UYvZj_yun1Bn27Z8SNbvDu4450_8tXy4EaALiL9-5Yo9WQOWz9aMgGqrn6VwLickTkCyg40ysfGOvaFrABGu02xo-m_2v6JgeRJ8xufKhnbQ5o9NUTyUVQDr3HroWZneVuFteb7s46hXQuR-a3ammS9N79dc69ZDrFI90-3bADags_fEM-Hb4rs_hZ36AaUO2OKgLfSjH0x2ngCgC97BdCB0YrKzo6UN9VB5RgZDcac7ZLErtlWWmSUIF2afpIV5UDyPDCHN0L3lgN-ekdku5f1XVExaYpageuDATEM-gVEvMvqA_gdkYOd5lJ2GAtJ5ubLlYqWEDXnMJcAxZ3RckYvUS1OVittCwy7GWKZKIP9G8L0yXo6XDz2FWKUPp8QRlk-cfHF_v9OvWoSaV4spuqpx0JLQNTdcUt_a4QygLK5HDq4BAClKQoXc0UjE3YjBpPemfMOl2rc_gkqtdproMlIxr97uPf0D_PXEwL8rOVCGBFCwXq6-t4Is9L7eCt7c8we7ZVrmM388nqZXhHGYN1BPK2Ui5Oo5jCYfOuPxXtScqefft16544B8cPlG8u94UgdhczldSvFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d096c16704.mp4?token=ZaBeakoeYVbSnTM4_R2cwcA7R_tKNJLxG9IY99ke7sXfR7jwSEIf5rDoryXubCmnZ3XmQFn1ErCrF53eWBBJDwszrKwdjZ4UYvZj_yun1Bn27Z8SNbvDu4450_8tXy4EaALiL9-5Yo9WQOWz9aMgGqrn6VwLickTkCyg40ysfGOvaFrABGu02xo-m_2v6JgeRJ8xufKhnbQ5o9NUTyUVQDr3HroWZneVuFteb7s46hXQuR-a3ammS9N79dc69ZDrFI90-3bADags_fEM-Hb4rs_hZ36AaUO2OKgLfSjH0x2ngCgC97BdCB0YrKzo6UN9VB5RgZDcac7ZLErtlWWmSUIF2afpIV5UDyPDCHN0L3lgN-ekdku5f1XVExaYpageuDATEM-gVEvMvqA_gdkYOd5lJ2GAtJ5ubLlYqWEDXnMJcAxZ3RckYvUS1OVittCwy7GWKZKIP9G8L0yXo6XDz2FWKUPp8QRlk-cfHF_v9OvWoSaV4spuqpx0JLQNTdcUt_a4QygLK5HDq4BAClKQoXc0UjE3YjBpPemfMOl2rc_gkqtdproMlIxr97uPf0D_PXEwL8rOVCGBFCwXq6-t4Is9L7eCt7c8we7ZVrmM388nqZXhHGYN1BPK2Ui5Oo5jCYfOuPxXtScqefft16544B8cPlG8u94UgdhczldSvFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: در پی بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره در نزدیکی پایگاه RAF Fairford در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24331" target="_blank">📅 15:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZmKzp-PR-Njp4IKsFX9vokeAR4vlWvhPv-vRlxnQJh6E3-dOlpzyEbQIOj8fRXaTo5OSqzP7Au1BmHH8dk6zRnESAfRY0vezZq02yrTTpmhZlSJp4CqNod3aNGFAhpCwZ85FAOhuWQorJlufbiHkg7XLOsdOJgaYoBxlmHAX7HvFX2dKC_BvpwWd0SR_tQp84Ig6uH_nwTpxqVrtqgOmyuWSgcmmReMm1AdYmt6ECwxm2bGG-BzejvoFGlmm9yIpHCdgkr7StRbP9Lnfm2D5AWFArJ8U7bf2lsoNTIbz7-kD9myqo5BqFG5-kYxbN78yyavWvZezMCqaGi8P7ReeyvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZmKzp-PR-Njp4IKsFX9vokeAR4vlWvhPv-vRlxnQJh6E3-dOlpzyEbQIOj8fRXaTo5OSqzP7Au1BmHH8dk6zRnESAfRY0vezZq02yrTTpmhZlSJp4CqNod3aNGFAhpCwZ85FAOhuWQorJlufbiHkg7XLOsdOJgaYoBxlmHAX7HvFX2dKC_BvpwWd0SR_tQp84Ig6uH_nwTpxqVrtqgOmyuWSgcmmReMm1AdYmt6ECwxm2bGG-BzejvoFGlmm9yIpHCdgkr7StRbP9Lnfm2D5AWFArJ8U7bf2lsoNTIbz7-kD9myqo5BqFG5-kYxbN78yyavWvZezMCqaGi8P7ReeyvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : برای چندمین روز متوالی حرکت دسته جدید هواپیماهای سی۱۳۰ هرکولس به سمت منطقه و اینبار هم ۵ عدد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24330" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه: یک فروند زهپاد پیشرفتهٔ ارتش آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام انداختیم.
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نامRemus 600 «ریموس ۶۰۰» بوده که توسط رزمندگان نیروی دریایی سپاه به غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو، به منظور بازیابی اطلاعات آن، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24329" target="_blank">📅 14:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه : یه شهپاد زیردریایی خودران دیگه آمریکا رو گرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24328" target="_blank">📅 14:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ-h81UL9yPrEyhGIVOxyRyEmqDUQRUti4SP4vO-YBQPRsdJjR0FNekplvHUc30hTD4iunrS_jNAXOk5TN0uFb4XGjfCxDNqPKXL7u_E-wsAcaEQVw2N5QG3Z0UNCiZrccScpqriPj7gOprTyJK1J3Hrp2S8rIcmCpwnzvp8iedAmNIfcvdpIXOyb0ggcGjQlZVDp0OYdYmhcRNSrbHcl_FXOctimPZuqXJvsTZHLseFalHL4ZLejPJFaWQlxXhc9_V8jsmGHpWlIDzVAq4e6mAcfXTZPmUAMNKGwM5Eyn6ENAeHPh09s80wTZwkET6wNER_60odJCWKHxACThTmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبراهام لینکلن به هاوایی رسید ، چقدر با RUDY11 خاطره داریم یادتونه ؟
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24327" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت ایران:
بر اساس اطلاعات به‌دست‌آمده، اسرائیل و آمریکا برای ضربه زدن به تاسیسات نفتی برنامه‌ریزی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24326" target="_blank">📅 12:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnSVtWN0FfGazvv_R_MH1gGPUSKSdGJYHIy84T_57sFJ2UmKCU_a7La88ivbUClVo3mKkA_5XqgGFaKwymQuYxPYhHBVmAABQEjnWSW4CkGZDBKaMlsWh5VMpd0DFFQCnfJe0iEKmnbQPVX_w0XKVWLXxD1SGlvce0iZOJMPTaBsvWaOQvmMPZh9E1E8WgJi1I9CJ1rGKSVHel5kRMy8d0ldHOagjlTIfSMdAgqS54IjtJXGH2klsiD4QR5c881oL6V-tKkpd0I6jjYWJJ-_D_gFqer1Y_hykS2Gf4Vug2BAgIueuHBLqu-adZ8l7GBtg9PKzV-sinF-Zwf6ycJQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/re6zuQDwqnKdpKb7IqmO2L5_YHMMGefKFUIm03BOnYKbMoGG4sF0FCX8zZHCxzUkINE3ciVjwFuSBwRue9CnflJLY8g9vgLYWGnka8lUn7VsPCRcPgLR_X4jWNybPqtLrfIQIUCLb3tELXJfVbotO_tW5iiFxkoFXwowyuh_DF_YKZW2oJskDduq4i5gOrnvwTQYHURUU-LJkKwEvosFBRKpaJgoflj6dxtjy1_OBKNMIRjHP3Ci9mGky86b4dIdfflulwxf2ogylaTQDxZxaFj0glVMIyANXyWYCokjV60hH08XLlduh77kLeS5k6dR-KLlda2ekei5Fl0Er-9bTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAXwwtxoOKZrT7uqE_C3_nPN1UocL9XCt45WAV__Po6VvVvCivb0KdyKgiqNLoXlr6jVpyOAiM6BqH4tg94VUcRQv1kZXBDqLNVZ_gx5I3A1QEns1wUYPfJ9IpDRIWRSaBcLXiuvoXVtuFb8nw-ahFxwAnd_7gBwAC03G87Dk3LdO8eHGg66D-xgDMQB8K2WcOOa_QkE-3K6IJSGdMm4MKDy941Lmx66y1Yt8mcqWJhJv2mEtxdQ_C8BlZNng9v1Kdxx2fyiDeMvfts1pLa9bmbtgyNIWYa8h6tbkBVgJvgNXf9udDdrJLE9mgxhRNKKBB7d43fNXIrzMxRXJzxyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVE49AXJtCOf_0VqI3G_MuuTArrxDxNL9yqMYydJsQW-kEf8bjbO5ZK8gp99RE2JZ3r1z0jWJjfj4-G601ZcGAIls5qFvRVWMPfm3fe38mxz8IpYdSqjzDcJza2T9uqWPUN3xE3l5J3dfMHomZt0szh9JuuKPvHCwGgoJEpK75As6Qw-RlgO_YdOPMjCyP1w-1fDZxAE625OCaFKliIQSOgGsgcOULA5b42_jLFM874QCC2FbLW2hjQ0UR7DlzNspd12sD5bncYQGRacISPYBQ2GuA7YJwo6pFTZCWF3ko0XSrEYORbwjYKqj_6dBHx6IkGoGEz_uQwUTvjak_A_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkqPzouJKjZTmJ8QHcbeRNHT6RTOlOBrPNDUijy5Yhunhyl3qQHU_q8IInwADSTceudLkVkf9nxyZe0IxaUh8FDdhSqW4g5502q5n1bMKFDKIn-KrBa6UgsD1AscAK1rblNuR-MsfGqfgz44HD1zWdFeN3fkiBYSL1eDpL8kuCoY3XcpE21jMVzd0y1VnfOEhOSq-0ze2FdrypJNmjgcfDdGW2OYhOvUlc3MJ5Qi389OD4V3yUzIeEJ7eckoy-lqzo8RzAMqAb4R9aF7b8bTA8Yb99iy_Gw7n6u6UfMvgs0TNNtXyj1PMJ-xdqPovsVfzpzVhUDikN-mcOhKJ6EWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goR-YyC_bBJ3HFfBH9lpd1Dfgj13QYfZ_o9Hwxu0dzDwUht6rw9B9rOrrvA0eb65gF6rPD2ItYN_KHYhfR_FQOkpUVR35pCxfHV5UJlXPQlIGIncGwdTidV-dJewMJWBPc_hmFSicimrKOKz2mQoKeHR7YqNd95jTFimTem2m9jSLBUTN3QjQXTAxffT3rBlmCPgRRPAuiEximrZHJcV9dCZvVRvJ_5iHXEGnn4MoBdKgkR5rtqd9BmC4uzr2lLm7WRHySRcA_8Ce0mvV-d8wYqAbBEals3rPCxuOKxRGAUlqX25dB4xD7s4FeipknXrI7Q5lVa3Oi9G8x7c8OG0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkYnx1FzsBDClrZqsZYqQUuovcfhfZjzyZb6QlehXnK41IfvvGepmVBqowsKN8BXTB7DB4cHx8ExeFHdz_W2n9fkO-Av0AJQYUbGH5Njj7miOcfAr1OAMu6shkTe-Byj2QokBHYnQCyOZ0Yu6B-1CrUg64diboBDS-rNItDYx-DQgfhAGpPLhtxyGZWum_r7NQlvhOGuIkPmmU-2ktiW2fzsK_VT69cWdvDEdIe_x5a2tTJT51peL2ko_DvWidli6yDxO46PPJtwzT6SXvECVjBt72qB5ipo6GGrerG0hBXZ3c4NHpdjLzwbs-4i5eLrCOG9uwetqeDyLrGROwub-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoM9xEfq5nsF_CTbSNVmatj6mKmucL-PbTJHg49gY-l1X9hS5P-H-m4WK_iDIVshaUzeNQwjdbMCIUcc4GY_AbzOxNZXkBOwBY4yMMBOJYbplKJEwpeoU7jd_59KvA53zuqLLo1Q7xtb_-CrTwtBC6UL1dzX3FSBDLdKF0t28YjC8qruKYyrLo5cCnB7uU7OBg2icoy8sTNDZsH_CkrdvIsvfWMoHvF8IyKv69n01ObcE4bKtlBa0Nr12tirVq6xWQp7XWKu4t-ycuL57V7Vjn9ddC1yaAIsswLNa9bxcBUH1I7vW95miJkYl9ZM5G4AdyspfHpkZeAQhzhNWy-J_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNbvdktR7JxUcI6TghBRRy35U9Mn7ucHhp1GQEV6Jx1G3nBUNingf1pCC89fmWdbgqHigSQV_8DRx_7mx9C4VHvpndG7XVDZmFe2qE6dzk3YmiJ5w9GpBspLNxi3-j5Opv2vq8qe3x0oOT9VTi5b7qNxT-ofVZj7J47HfbAKWMuiRQASHb8I2RJRcN2BsqE0cA_kvj-qe_HfGg1XCYnzXmL1x34BMi66D4gyHtfrR7XHErDz0RiDFjlv6lGOpy7760s8bNNHpikLBRXt2Ro0uQwuSCSD3EVf3oRuvheIj3aClMKqvhbARkxsxaDRQVtjt18Rs-FHNnG-r28zjQifqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_N6FO3PQPB_joRyFaLi7yC8wTF7HU8nqNIT71TzvhXxCw28ONsqLuD3qKaAObBZ9UnDypHu1Bnskg7OnbxKyBhcvQ0BNL415f4pQ1S_0yA0ZVfbfmNpfF5uMy2n2Nz9VWSDofJ3sTdpK__Pdc33rnS_TgSUpr3jD6pn28rxmDCb2exR-8zCgywkHa0xEZ7DMJJ41LBIDjRptIoslbjvdmmxH5T90h_tnSWSIFhAQloLLUPhKYK7OiQrgyo_FmJFB4w99b2KGpJuinwj9eaQ7plwfiizwXhuQirmf-u6Vn47jkJNJ5y6Nufj5MmVFB33WsA2SihAqfo1kVbaEPFttA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آوییشن‌ایست:
۱۰ فروند جنگنده
اف-۱۵ئی استرایک ایگل
نیروی هوایی آمریکا پس از بازگشت از خاورمیانه و مشارکت در
عملیات خشم هماسی علیه ایران
، در پایگاه هوایی
راف میلدنهال
در بریتانیا فرود آمدند. روی دماغه جنگنده‌ها نام و تصاویر شخصیت‌های بازی
مورتال کامبت
مانند اسکورپیون، ساب‌زیرو، لیو کانگ و شائو کان دیده می‌شود. همچنین روی این جنگنده‌ها مجموعاً
۴۵ نشان انهدام پهپادهای شاهد ایرانی
و نمادهایی از مهمات استفاده‌شده، از جمله
موشک‌های جی‌ای‌اس‌اس‌ام، بمب‌های GBU-39 و راکت‌های لیزری APKWS II
دیده می‌شود. این ۱۰ فروند، نخستین گروه از مجموع
۲۴ فروند اف-۱۵ئی
پایگاه سیمور جانسون هستند که از استقرار سال ۲۰۲۶ در خاورمیانه بازمی‌گردند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24316" target="_blank">📅 12:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏در دومین سالگرد نفله شدن حسن نصرالله، مستندی از لحظات جستجو تا رسیدن به جسدش رو ببینید، ارتش اسرائیل اعلام کرده بود بر اثر خفگی مُرده و درست بوده، اسرائیل اشتباه نمیکنه ( با زیرنویس فارسی )
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24315" target="_blank">📅 12:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یانشا, نخست‌وزیر اسلوونی: تغییر حکومت در ایران و انتقال مسالمت‌آمیز قدرت به مردم، برای توقف صدور تروریسم و ایجاد صلح و ثبات در منطقه ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24314" target="_blank">📅 12:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز:
در پی بازداشت چند نفر به ظن جرایم مرتبط با
مواد منفجره
در نزدیکی پایگاه
RAF Fairford
در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از قرار گرفتن پایگاه در بالاترین سطح حفاظت آمریکا،
FPCON Delta
، منتشر شده است؛ نیروی هوایی آمریکا از
افزایش هوشیاری نیروها
خبر داده است. پلیس می‌گوید حادثه مهار شده و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24313" target="_blank">📅 12:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVy2uD-pu3tU_8gnZtkrAYKQZ8UuuEZKCzCs7I8I6fsS_J5XJ-Jo8JLQvsP2ikJIYRaR_zt4wyD53THqLWxYGJVG8dJ2c4FsBOBKFb3opuuBj2voygJ4gy3Roh7v-jt51gzlZxI7eTn_gSTCp5r_d8MCCs7FiFxcA3qHkRx6vfWDH7qH6ZcauVOVwRu2wRuw7VxJvM80zkrxLf08aUBPg6zoGJF4dfm32BdVyIn_6UzTzuDoHdCCT48oJAASDjYnQYlYlyO4NdACwpQBpTvlC7bnvPZ1NymrkpSYbwqZA_ji1aNVXzy5JBSeyfBm8DzsGpRsyVnpuym3XHVyYY4WDV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVy2uD-pu3tU_8gnZtkrAYKQZ8UuuEZKCzCs7I8I6fsS_J5XJ-Jo8JLQvsP2ikJIYRaR_zt4wyD53THqLWxYGJVG8dJ2c4FsBOBKFb3opuuBj2voygJ4gy3Roh7v-jt51gzlZxI7eTn_gSTCp5r_d8MCCs7FiFxcA3qHkRx6vfWDH7qH6ZcauVOVwRu2wRuw7VxJvM80zkrxLf08aUBPg6zoGJF4dfm32BdVyIn_6UzTzuDoHdCCT48oJAASDjYnQYlYlyO4NdACwpQBpTvlC7bnvPZ1NymrkpSYbwqZA_ji1aNVXzy5JBSeyfBm8DzsGpRsyVnpuym3XHVyYY4WDV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسخره کردن پزشکیان در فاکس نیوز : آقای پژاکیان ، یه سوأل ساده هم نمیتونست جواب بده
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24312" target="_blank">📅 11:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24311">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDkliw6ubUqiLL8cbp-BRvwzO3djFyn-Xdu0rkLb-Pj0rJKJ2I2DyKw6HEhmNAegS76FgyQIq3ISjR3li9FmKkUXblcsso8aI3okE-n8ABoMb8kCkogzEHuChd0tgLR6_6GLE-85MAsucoP3rFjcDEDHO4otU81ow9EaZnM2pCjthnIZgm86y3amljssE4jjAyqEaYPK1GMqfmxkqKsOtkSbZFMuOfx_H2rLujWzNM_4-sy67IXioV6Gx3XhSsnWQ8Vp7kDKeTDZ4M-l_BtnvOL8rjE27jmtrkxvFO35QiGLrilIiOsyevwyWc64GoBS1kCzwqJzpVzNo9srq93jXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نجات ترکه موتور یه پرستو نشسته قشنگ ارشادش کنه ، چیکار که نمیکنه این رژیم
سردار سرتیپ پاسدار
محمدحسین زیبایی‌نژاد
مشهور به
حسین نجات
(زاده ۱۳۳۴ در شیراز)، از فرماندهان ارشد و شناخته‌شده سپاه پاسداران انقلاب اسلامی است که هم‌اکنون به‌عنوان
جانشین فرمانده قرارگاه ثارالله
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24311" target="_blank">📅 11:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تمام بانک‌های تجاری بزرگ در امارات متحده عربی و ترکیه انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24310" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-SGZNeN6chQNARPrZqA2vmAESZippLpzTZJZtcB_tdmjY_seWjZwZ2M0vdnpRoUcqvWe93Q45WnRarlm_XobH1XIM7IEMq1FHIHamHZfmbOX_ys7lX5yc8RjHjMaky83gr60q1eVk7WEKbrFcVZJoZfZAGBtmVLAQx56wTYwMMorWRENhfIw1b-4HJgLC1534BXjjIGFOcHJc9ZNZHJpvFyNSMmqVOAENzrWlzBrF-R1JalLmCYgschCMi9soyTTKJEvApVjMzhwR_56uVYj5PGiosXCGvEtrZz0y4BuV1wX_sKj7il3kfgq50eEM_ZfyoZFmTxNQFUv4suDZw80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24309" target="_blank">📅 11:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqJ7-uqRtAd0WBNTMfflfCBVFOXZwZZYyqLo1wb7aZ2s3-Tq0P13QTac8qhKJpRdw3GLmeGBIDwozGFJgRsAngIpM4qLyB6TlJ2U8lFuNPdhWqJU5Wk5FDnI7HZ2Lfno997--5QWDJB_aN97k06zvkbGdEyVSlZMuPDT6W-PXp4OPKDJ9zjJ7Cz3MGv2ebD3d51u6Sjgex3e2lZ9Bn3XRl_482UVl_xdo4yi1xRGXIVzgJzC7ABP4DCJvd0zSMoaxGO-qDMQglBMXp9w9goe4PtxP4D66Y9fgtWOyv6-a0fl7LvH9evXRR-_IfwjhMJIEQKilkhBnA5uyjKIDukeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های رژیم : سرهنگ دوم
مجید بهرامی
، رئیس پلیس آگاهی شهرستان ایجرود در استان زنجان، روز پنجشنبه ۲ مهر هنگام انجام مأموریت برای مقابله با
قاچاق کالا و ارز
جان خود را از دست داد. بر اساس گزارش پلیس، در جریان عملیات، خودروی قاچاقچیان با خودروی مأموران برخورد کرد و سرهنگ بهرامی بر اثر این حادثه کشته شد، این یک ترور سیاسی نبوده و
عاملان این حادثه کمتر از ۲۴ ساعت بعد توسط نیروهای امنیتی و انتظامی شناسایی و دستگیر شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24308" target="_blank">📅 11:02 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
