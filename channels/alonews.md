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
<img src="https://cdn4.telesco.pe/file/Q5yFJA0fRnTH-Y54-P2Dc00ivjnLrv7qktmKOANYfMwVCFpu5VkoiaHO7eDt6BXTWB6xOaFoV4A-veg0J3sU3yP0PlGB4PaKVayawmCxalVPGvNTJisykb6oBrWaag1bvWZHBIJpEPkvmOQH8wf8vqewcowDZIc6VqcgjSwINa_QutZgtTSA3nk4p9G30QY5w4k1O-8FLUpD1IpGFdD4bk77DY8P7q-rpH_xjfVaVLHIfL2YTX2d3bUuSaqPcsfzIbyjAEVZWV5t4Z_NvI7gIPJ9WEmjQ0CA1UKR6vBZXMUQUBAHyqWLNzHO3Nb4eiCVqHXby2P1fPLHTj6B6pGXCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-149285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا با ۲ درصد کاهش به ۹۲.۶۵ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/149285" target="_blank">📅 09:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ادعای بخشایش‌اردستانی: ایران از کره‌شمالی سلاح هسته‌ای خریده است
🔴
احمد بخشایش‌اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد شنیده است ایران از کره‌شمالی سلاح هسته‌ای خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/149284" target="_blank">📅 09:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دیدار و گفتگوی نخست وزیر قطر با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/149283" target="_blank">📅 09:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک‌تایمز درباره طرح ۷ روزه ایران برای پایان جنگ
🔴
نیویورک‌تایمز درباره طرح جدید و شروط ایران برای بازگشایی تنگه هرمز به سلسله گام‌های زیر اشاره کرد:
🔴
توقف تمام درگیری‌ها به مدت ۷ روز، از جمله در لبنان
🔴
آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران
🔴
لغو تحریم‌های نفتی ایران و محاصره دریایی
🔴
بازگشایی تنگه هرمز در روز هفتم
🔴
آغاز فوری مذاکرات جامع درباره برنامه هسته‌ای ایران، بدون انتظار ۶۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/149282" target="_blank">📅 09:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نفتکش‌های ایرانی توقیف شده شناسایی شدند
🔴
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔴
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔴
بر این مبنا نفتکش مجستیک ایکس و تیفانی در سواحل شمالی برزیل هستند و نفتکش لنور به تازگی دماغۀ امید نیک را دور زده و به اقیانوس اطلس جنوبی رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149281" target="_blank">📅 09:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
عربستان سعودی، ترکیه و پاکستان جلسه‌ای فوری بین روسای ستادهای ارتش برگزار خواهند کرد تا درباره حمایت ریاض بر اساس توافقنامه دفاع مشترک بحث و تبادل نظر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/149280" target="_blank">📅 08:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کلمبیا روابط دیپلماتیک خود با ایران را قطع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/149279" target="_blank">📅 08:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAsUYUflsUaQV-Rjibx5gqIao6E5NuM3CgE4eS5JzespcZ7xFNJhS8-Gq7b8we9r23HaSNQ5W_r9gYx-FxCjQJXPId5TONUgL_W9CSCsRWeXkhw3QqrNESSEIHkjm_dA_opL3WTVJQ8RdMNYR-EQPjydVmDzr9dVQ6sEMSfKuRgwkQJMK0tUEdsYm5FpUsu7sn5f-NQ45_TevYwAsBdWUKpTncoxKLQ3BssKIMpNVATjsJnWMWFUjnIEpSlH_IFZ8MNZJOofevmmouocIQcKC8xs4eZH-O4j-ug6gHCgK9GH0XNwYTKnHbYS_W5G0LRSFTe4aWIsd0kNrTOsHWdrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: اگر اقدامِ موثری برای جلوگیری از ایجاد «محاصره‌ی هوایی» بر آسمانِ اطراف ایران نشود، آمریکا وارد فازِ اخلال در «مرزهای زمینی» خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/149278" target="_blank">📅 08:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: ما نماینده دو سیستم متفاوت با چین هستیم، اما روابط ما در بهترین حالت خود قرار دارد.
🔴
رئیس جمهور چین: ما با رئیس جمهور ترامپ در مورد تعدادی از مسائل به درک مشترکی رسیده‌ایم
🔴
در جریان سفر ترامپ به چین، ما توافق کردیم که یک رابطه سازنده و از نظر استراتژیک پایدار بین دو کشور ایجاد کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/149277" target="_blank">📅 08:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از عراقچی: طرحی از طریق میانجی‌ها به مقام‌های آمریکایی ارائه شده که در صورت پذیرش، تنگه هرمز در پایان هفت روز باز خواهد شد و مذاکرات از سر گرفته می‌شود
🔴
این طرح می‌تواند به‌محض موافقت آمریکا آغاز شود
🔴
یکی از شروط این طرح، موافقت آمریکا با مسیر عبور دریایی از تنگه هرمز است که میان ایران و عمان بر سر آن توافق شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/149276" target="_blank">📅 08:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بسیجی‌ها قراره امروز مانور موتوری داشته باشن تا مردم رو بترسونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/149274" target="_blank">📅 08:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با فاکس‌نیوز:
ما اورانیوم غنی‌شده با غلظت ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) کنار خواهیم گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/149273" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=kqD-fvtjq2RJfiT5ig7f9Adhh4N7XByPTThJiaBoBfXPKQ0ikNofYpDMW1wNz30KCRyuOgO8He6bSAuiRFMU7DHq8Vhk7mNmKbMldvle2-6PPlfpYGqxWjIkRPsxDKMmGUoXXrdLY7MWi6nln-0Wq94t6M_DmfCy0a291l00GEcvtcayA7dcuzZGbELgvW7Ls_lnN7XY2DQHa7C9hwd_D3TueT5F7rdGP3VmERhAXzn6d20c1qagjgKR5WUVh2bpHqYFmpnkWom0dYAIao03ehFlzjtfVG--8CQ1JtIiUm-UEdAA8FvKk2AmLKhEOsKyHuXlfZpbKLSyi8ayisklkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=kqD-fvtjq2RJfiT5ig7f9Adhh4N7XByPTThJiaBoBfXPKQ0ikNofYpDMW1wNz30KCRyuOgO8He6bSAuiRFMU7DHq8Vhk7mNmKbMldvle2-6PPlfpYGqxWjIkRPsxDKMmGUoXXrdLY7MWi6nln-0Wq94t6M_DmfCy0a291l00GEcvtcayA7dcuzZGbELgvW7Ls_lnN7XY2DQHa7C9hwd_D3TueT5F7rdGP3VmERhAXzn6d20c1qagjgKR5WUVh2bpHqYFmpnkWom0dYAIao03ehFlzjtfVG--8CQ1JtIiUm-UEdAA8FvKk2AmLKhEOsKyHuXlfZpbKLSyi8ayisklkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس‌نیوز: آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
🔴
پزشکیان: آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/149272" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=NY7TGjzFfCD0gxb_r-a5K2fZUdVJWfJGjq-KAoLPciM1WEdVi0NoJRM5gSuWFEj6s9F8mr5BDjPGHr53VwRfo4lb2iTLhHJv4IWhzSczBy4qLquUSBHQPNwgazKb8oKBpOzE1nJpEfQzNnOoyVBbwXUdsulSxaO0oa37pLrhwzoqcbNDuIL5h2CdKQYgs9q9RbQ9cuPpjYu5Ug1eOqNgbElxzTYdIzrXiPAjtxwif6imX75R8BS-uKRX1qIJpMnh2i1w_MVNiygTomEsUYI3zZ4I3cVDG4jBQM37f7pkos62nvbhr83uyORKIdkSsL_oGyo9O0xHcf1S3ItFaHo7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=NY7TGjzFfCD0gxb_r-a5K2fZUdVJWfJGjq-KAoLPciM1WEdVi0NoJRM5gSuWFEj6s9F8mr5BDjPGHr53VwRfo4lb2iTLhHJv4IWhzSczBy4qLquUSBHQPNwgazKb8oKBpOzE1nJpEfQzNnOoyVBbwXUdsulSxaO0oa37pLrhwzoqcbNDuIL5h2CdKQYgs9q9RbQ9cuPpjYu5Ug1eOqNgbElxzTYdIzrXiPAjtxwif6imX75R8BS-uKRX1qIJpMnh2i1w_MVNiygTomEsUYI3zZ4I3cVDG4jBQM37f7pkos62nvbhr83uyORKIdkSsL_oGyo9O0xHcf1S3ItFaHo7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای مسعود پزشکیان:
هر کسی که بخواهد اعتراض کند، کاملاً حق این کار را دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/149271" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=n3r92nfzrFwbeD5j_61ZeYjrdEnNeutv9UMQpJNqFCDxpbqXKdw0R9OiQyJ2Nrde-ePOwtT6Ct8aoX0LKJ3l2Tp_o7Pp-auhubfTwFkq9BruzEQx6HQVdRzJkW9kHzrX-IRwsu7C0sCqp_SUO-fAta1wbC-lPOpI4Q2fxFzG19HLx5rjkpP03qtXSb_0mke9zZS6Ma0js7UTbNCY91e6m0jP5BLb16KNWseeLv0odBUjT21QZAd5QQCrUgW5M2VCdx_24qknocPSkDQ7rgGKb81dOUUDgeLxn7r7gqJKfoWNMgKAKa3RIeXFBM8MQpfAHqd9HvjC9KdV5PRFheo27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=n3r92nfzrFwbeD5j_61ZeYjrdEnNeutv9UMQpJNqFCDxpbqXKdw0R9OiQyJ2Nrde-ePOwtT6Ct8aoX0LKJ3l2Tp_o7Pp-auhubfTwFkq9BruzEQx6HQVdRzJkW9kHzrX-IRwsu7C0sCqp_SUO-fAta1wbC-lPOpI4Q2fxFzG19HLx5rjkpP03qtXSb_0mke9zZS6Ma0js7UTbNCY91e6m0jP5BLb16KNWseeLv0odBUjT21QZAd5QQCrUgW5M2VCdx_24qknocPSkDQ7rgGKb81dOUUDgeLxn7r7gqJKfoWNMgKAKa3RIeXFBM8MQpfAHqd9HvjC9KdV5PRFheo27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: ما هرگز به مردم خودمان حمله نخواهیم کرد.
🔴
برت بایر از فاکس نیوز : اما شما این کار را کردید.
🔴
پزشکیان: نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدارس ما حمله کرد؟
🔴
بایر: من متوجه هستم، اما در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/149270" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzXc6elfFkWn0-UgpeGpMX9bKWRJ5xriv585inJfc3xG3VkFQaJ4bibRIlEc6SWJOYSMfTVYO8oT1zvhNb3ZMP4C7CzXxEcmuIN4n-72-1I0KbWwqxtW7xeEFU_rXp0lqmYR6IHN6pg6C5ywfafn3PtzPweG-9S9RjUWHYLLX48NfJUat5ApWpU0RgPMQUQCLlvIBfHlfoKYYVyeOm4Ohs-hFJmEmAaiMhvV5t31fl5K6QqSigAwNGowhCUhDbnxbTgA3jFxO7V6z9AqvDU1Aom5cJj6E4xrOofTL-VGbMhFr9XdkVgfsjs62SGq_6dhttRl4nvNAaN8fxpiU5F0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/149269" target="_blank">📅 01:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان: ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از اعضای خانواده‌ش رو نداشتیم و این پُرپَکانی یهودی‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149268" target="_blank">📅 01:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4218edcc4.mp4?token=UjhOEgH96cnt485ARqK3K89Eck9H6A1sveoS4dXEhCuZeLxECFSqfPfQC6lAmrVqr9EkRwojiZsOShOrCpBLhv6ihZZc-ShxWIhcBK4Oy8C-QwaLQy6qQfNEwNPi7PvBF3sdKrJuChVRoFBs8kU3B9TAjQOQAD0m46VYgnqbiyJwVYUEJUUfDfNLcB4MhslcNO60sJwZKWplQMLtPPIQRHyzUt4RPOHXTFM4dvNqLIS7gx0rweZ6tmhIti8wnMjaod21cnxxDnb9QqbnpJ4SDwz9WBv6Z6PzkmsA8M5zb1AJydm5cDhEOowBLmCqfwzLpsxUyrVb0YUPRa9VQVM17w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4218edcc4.mp4?token=UjhOEgH96cnt485ARqK3K89Eck9H6A1sveoS4dXEhCuZeLxECFSqfPfQC6lAmrVqr9EkRwojiZsOShOrCpBLhv6ihZZc-ShxWIhcBK4Oy8C-QwaLQy6qQfNEwNPi7PvBF3sdKrJuChVRoFBs8kU3B9TAjQOQAD0m46VYgnqbiyJwVYUEJUUfDfNLcB4MhslcNO60sJwZKWplQMLtPPIQRHyzUt4RPOHXTFM4dvNqLIS7gx0rweZ6tmhIti8wnMjaod21cnxxDnb9QqbnpJ4SDwz9WBv6Z6PzkmsA8M5zb1AJydm5cDhEOowBLmCqfwzLpsxUyrVb0YUPRa9VQVM17w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پدر کودک خردسال خود را به دلیل فقر به عقد یک پیرمرد دراورد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/149267" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77207c734.mp4?token=QKscIDvd8JhSxJAdkWB-XiCekK1IMsAVhgcukjrCUN0_2wSBXrfbbYagLcnkpao2iOkr_HyEhPKzydkjNqEaSsYW7slPdFHWS0hTpfqwoicbf-XNXzJg3xa18RoWh0yvfF1hiIn93MdWjfntYN01wh5Mjkf18o4J3kKZt1WoQyQ-rxS1GTD9yN8RQX99FGGIsFW0Ms9qpL6djVbcR9POcobGnWC486c5ZGZhEtZJiyTPX7vhzTMii3A88Wl5KN2oaQY1hku23kcCnwPdHiILX_Ba7JCBs6tRuB-_rl1kiBIhlqGCJze2kvC0pq24rT7Dg-S5gRLdTitHc6f95fHtbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77207c734.mp4?token=QKscIDvd8JhSxJAdkWB-XiCekK1IMsAVhgcukjrCUN0_2wSBXrfbbYagLcnkpao2iOkr_HyEhPKzydkjNqEaSsYW7slPdFHWS0hTpfqwoicbf-XNXzJg3xa18RoWh0yvfF1hiIn93MdWjfntYN01wh5Mjkf18o4J3kKZt1WoQyQ-rxS1GTD9yN8RQX99FGGIsFW0Ms9qpL6djVbcR9POcobGnWC486c5ZGZhEtZJiyTPX7vhzTMii3A88Wl5KN2oaQY1hku23kcCnwPdHiILX_Ba7JCBs6tRuB-_rl1kiBIhlqGCJze2kvC0pq24rT7Dg-S5gRLdTitHc6f95fHtbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جررررررررر
🤣
سفیر اسرائیل رفته استارلینک رو تحویل نماینده ج.ا بده نماینده ج.ا هم عین دخترا قهر کرده و اونور رو نگاه میکنه
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/149266" target="_blank">📅 01:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0eJm_b_-YoepjZjVzeFYmvIEl8sqFrnOQ3dkuWkKrBqIh_bW0v3WxXTyHQ8NFUUgfIkFPYFCD1CEnRUmZAWfywLjJvLU1mbRK4NHQk4vCYm3ey_LuDtLDniBXDa8S0w3u39izKqqWsLuibYAU97kkLG_j2vZ5lSUXv-KVRVwBPeixfJmPUPj8WL2cl2ukoaWhRfpPxQZ4orJAIp7ZqXbtPL6Z5rKC20FfB25_5t1KeSRaxpoln5XR2OL4mk5SyAxhe0O_5TZ2X7ewZ2gPtrrn-jdaOsQbqkYCAu1WvU7Ig-bOt2PTnqL3nkFFiewW9d3jfJsWO4rfHWSA5XIWYSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: آماده هستیم تا قبل از انتخابات آمریکا، توافق را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/149265" target="_blank">📅 01:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: آماده هستیم تا قبل از انتخابات آمریکا، توافق را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149264" target="_blank">📅 01:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/149263" target="_blank">📅 00:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان به فاکس: ۷ساعت با مجتبی صحبت کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/149262" target="_blank">📅 00:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=OUxHo87Q90V-m7t46xTzvPgsVPNJAt8pDrnuzMIAChbydEJ4mbxqctXmxHra734Sdhgy9Pw9o8iylEjdtF4W4k6DG_MnyNxSEE-GqI_-Vg80WuCvQhyPDw4Aosri9exxRHbbSx8M9wuipDnEG_V88aHqoQmIizsGB1XIJxhMQFgWehPbxUmeZ7ppsbrWNChmmyZTBi_BgvMmuz5BwRN-1zGBx101opMWjRcr7TJsiq_H1hpaKzwPQCuOzjqBOaDZR2sf3fKxiEPXx89q-z1G4u9dqh2ygTIRX4finHmUKU9zon_UbRUl_COcl767lnqyvre1ScgwpbF0mu-7xlkl6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=OUxHo87Q90V-m7t46xTzvPgsVPNJAt8pDrnuzMIAChbydEJ4mbxqctXmxHra734Sdhgy9Pw9o8iylEjdtF4W4k6DG_MnyNxSEE-GqI_-Vg80WuCvQhyPDw4Aosri9exxRHbbSx8M9wuipDnEG_V88aHqoQmIizsGB1XIJxhMQFgWehPbxUmeZ7ppsbrWNChmmyZTBi_BgvMmuz5BwRN-1zGBx101opMWjRcr7TJsiq_H1hpaKzwPQCuOzjqBOaDZR2sf3fKxiEPXx89q-z1G4u9dqh2ygTIRX4finHmUKU9zon_UbRUl_COcl767lnqyvre1ScgwpbF0mu-7xlkl6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بریت بایر از فاکس‌نیوز:
چرا ویدیویی از سخنرانی رهبر معظم در پیشگاه مردم، در مورد این جنگ، یا حتی خطاب به پرزیدنت ترامپ ندیده‌ایم؟
🔴
رئیس‌جمهور پزشکیان:
خب، این فرآیندی است که در جامعه ما ایجاد شده است، یعنی فقدان امنیت که توسط اقدامات مهاجمان ایجاد شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/149261" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60aba8f435.mp4?token=h06JZWWxkNQWEnN_xPttJaxnGfMFNmMrCto5HaksWJiiLcLVvf498PEM17nplnKyf95-3fWQmbZ1jUS21HVG0KmWfr2KxuFdMcUevp0fPGyh26QMKGQynKtrsSrQxLlqRabiZ_hh8maW2zhCxr2OcQNalslmn0TQ21CD5T5nntMXEK0mCbrubmFfHmlXrT6PAVU0hM1pK0rOqtjK3BwNzoDb-NmxSvKeRY3rWUMIl4TnzPAh-HWwRQYr7Ts8_qFGJzjI04Fg1yd1oYc1Hh0y_Z79SVpdBZrkrCoAchFJPJ3ARyknXgHFjt7pExqi2jTuNiTjeVma7kMXdRAH_8PTPUX22qlKGiR1PuIBozXKoJJMqn0Bbv9xx10Lv4tGpJhpOjijN2JV32xFIfVnLlQgQprqOjJDPlCef7QfIm58I8Rql4Qy5WmZGI33jJx9Ay7eIi-r-zntgTIyLEIUErd31DLc2sCGhrk_9FSayhRvhIfPk_VyDgaPlDJ1dyO-LTA1e9wF2mQDu5tfi7mJshKILOihPCE-Y8vqi3phZg8SRRfD0NwY4pULcDS3RSgVNuz3n_tMya180sm8H_gQR8TfVaKNT4krf3w_yqatdIC1ia1Z0eYc_hoezuz5keiht2Tv37j-wpwtsnUhW9FCzOonK9-EyDAaAl2ctidcSGBN0sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60aba8f435.mp4?token=h06JZWWxkNQWEnN_xPttJaxnGfMFNmMrCto5HaksWJiiLcLVvf498PEM17nplnKyf95-3fWQmbZ1jUS21HVG0KmWfr2KxuFdMcUevp0fPGyh26QMKGQynKtrsSrQxLlqRabiZ_hh8maW2zhCxr2OcQNalslmn0TQ21CD5T5nntMXEK0mCbrubmFfHmlXrT6PAVU0hM1pK0rOqtjK3BwNzoDb-NmxSvKeRY3rWUMIl4TnzPAh-HWwRQYr7Ts8_qFGJzjI04Fg1yd1oYc1Hh0y_Z79SVpdBZrkrCoAchFJPJ3ARyknXgHFjt7pExqi2jTuNiTjeVma7kMXdRAH_8PTPUX22qlKGiR1PuIBozXKoJJMqn0Bbv9xx10Lv4tGpJhpOjijN2JV32xFIfVnLlQgQprqOjJDPlCef7QfIm58I8Rql4Qy5WmZGI33jJx9Ay7eIi-r-zntgTIyLEIUErd31DLc2sCGhrk_9FSayhRvhIfPk_VyDgaPlDJ1dyO-LTA1e9wF2mQDu5tfi7mJshKILOihPCE-Y8vqi3phZg8SRRfD0NwY4pULcDS3RSgVNuz3n_tMya180sm8H_gQR8TfVaKNT4krf3w_yqatdIC1ia1Z0eYc_hoezuz5keiht2Tv37j-wpwtsnUhW9FCzOonK9-EyDAaAl2ctidcSGBN0sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس‌نیوز
: آیا مجتبی خامنه‌ای سالمه؟ آیا توانایی اداره کشور رو دارد؟
🔴
رئیس‌جمهور پزشکیان
: کاملاً. به‌طور کامل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/149260" target="_blank">📅 00:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149259" target="_blank">📅 00:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/149258" target="_blank">📅 00:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از رئیس‌جمهور ایران: دولت ما پذیرای بازرسی از تأسیسات هسته‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/149257" target="_blank">📅 00:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دیدار پزشکیان با خبرنگاران رسانه های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/149256" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2e185a7f.mp4?token=jWgUkiwbzsWw7MQDLYLDlpmczL3si6LDKzJxIX8doFQeal9Ecnr4KnyCFw0OeoGWOOu2Nvi0sXeA5VLPSolPoEbCOGOoJNIMF1vgN7KeVXNW-BBqTyvToF6Jksqq6aP__hM2VP18BMOmJUPhqV5u78Gs_aAJXGq-Qvfjs-zyY7WBabBfGutr17PK0RxMWc5QONrBhYr0vevixubXDKX7LLECKWFjLEI0_DKScVpqYVEChp-wQ3z4fUddUH_IIeZCr_EH94Rn2zr9z3zRGk42rklgAtKgUPugMh5aXImlhQbx0anzY9EO1gDxqL9F2zcw4-iYcZVW93UeY22_1RyVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2e185a7f.mp4?token=jWgUkiwbzsWw7MQDLYLDlpmczL3si6LDKzJxIX8doFQeal9Ecnr4KnyCFw0OeoGWOOu2Nvi0sXeA5VLPSolPoEbCOGOoJNIMF1vgN7KeVXNW-BBqTyvToF6Jksqq6aP__hM2VP18BMOmJUPhqV5u78Gs_aAJXGq-Qvfjs-zyY7WBabBfGutr17PK0RxMWc5QONrBhYr0vevixubXDKX7LLECKWFjLEI0_DKScVpqYVEChp-wQ3z4fUddUH_IIeZCr_EH94Rn2zr9z3zRGk42rklgAtKgUPugMh5aXImlhQbx0anzY9EO1gDxqL9F2zcw4-iYcZVW93UeY22_1RyVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان تصاویری را منتشر کرد که نشان‌دهنده حملات آن‌ها به زیرساخت‌ها و پایگاه‌هایی بود که توسط ارتش طالبان اداره می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/149255" target="_blank">📅 00:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erST_9RMW0yquf5P1yNUUn5cINF4f0WOkBrKk5Pi25vBnndZ9EkzBcxwlFSkKSSSYn798HpojkgvHfzdYCriB1B6scyNrNRSIVsmEyBLfN1-Kis13ugFdeM-irdkgk_uS5NZbfJ-mGlUGSEl2RoCtgsZ_kczMm0W9NIlOWsTLNZ45UC30rVE76S8jiMgIAk8LI6_1_E1QxZVUsGjvUWc8WvQ9WTzwVFqdEk-zYZZAZZE7mndsmXt-dQTfK2ceAfVeOts1P1j95F-Nm37HM-vd0KdJhJGXc9rJi8CvkadLnhqiwrA6Xar31fz-4DUF91uKFowzXx27HCvPIBE-yHH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با خبرنگاران رسانه های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/149254" target="_blank">📅 00:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
غریب‌آبادی:
اروپا جواب جنایاتش رو می‌گیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/149253" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRFBsURpkS8ocLQys7iFme1XWcDnB6mW5PCVaaMapAT9dAPg3x0DaVrA6T_1hQtOkfcE-an9CAUqK4rndus3Bvrvzc-K5Gl7NZCDwuDq8EYgRsCefnxHeVimLH9dvPj5NE4MhcBypKkFfoQ4VwS59Bsrwu9bBLio2hS6uM2SJCzy5ZKx6eUy3TQ_wpYsXYK0x0cr_upCfMKdZJUbLlm3pZbmyet7s1W0wN3cYw_fmB9VOKAIStT-wJOGRE-cIdB_Z3kCwv10_ecTgBi7MVqq9JPPD_IKqE1ytGvboOc7Ih0v28RneQHGgwHWJPO5kKyY5LLg4d_3biip1PmBzRwyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای پشتیبانی سریع (RSF) که از سوی امارات متحده عربی حمایت می‌شوند، اعلام کردند که یک پهپاد بایراکتار ساخت ترکیه را که توسط ارتش سودان در منطقه النیل آبی در سودان مورد استفاده قرار می‌گرفت، سرنگون کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/149252" target="_blank">📅 23:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb872c593e.mp4?token=Orso9eDHYNsIFJOVcN2oLz1StiVXi99vvpAHJfVd9AJrcOlPdm3jrqg3BKUX3BxLHJrmoFErCsgXMyDbJCeO4cR6KdU0W6MnHkhhgr3quvM2AdJ2Kda1RfjtGBXt8wZCPcSR4rDptV6fmnYGYOx23PbN7HGAeI10FHrs9t3mA0GLX6NEiIzWUAAwaxbIiAsCA-Epl0xnqT93w1OVEgmPRVe0C0fdFTB24FyYOrEpP0IHAVfqaAtRCMoqLFX6-YS6NbrIiTGE_2-EqktQNtxg9zYTOLOj1tiN424EuBdUnGzc4moKJ8544lRc3hPdiSfNez_FDuPfDUyWmPj7HwoPuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb872c593e.mp4?token=Orso9eDHYNsIFJOVcN2oLz1StiVXi99vvpAHJfVd9AJrcOlPdm3jrqg3BKUX3BxLHJrmoFErCsgXMyDbJCeO4cR6KdU0W6MnHkhhgr3quvM2AdJ2Kda1RfjtGBXt8wZCPcSR4rDptV6fmnYGYOx23PbN7HGAeI10FHrs9t3mA0GLX6NEiIzWUAAwaxbIiAsCA-Epl0xnqT93w1OVEgmPRVe0C0fdFTB24FyYOrEpP0IHAVfqaAtRCMoqLFX6-YS6NbrIiTGE_2-EqktQNtxg9zYTOLOj1tiN424EuBdUnGzc4moKJ8544lRc3hPdiSfNez_FDuPfDUyWmPj7HwoPuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور صربستان، وُچیچ، شخصاً در سخنرانی نتانیاهو در مجمع عمومی سازمان ملل حضور یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/149251" target="_blank">📅 23:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
امانوئل ماکرون، رئیس‌جمهور فرانسه، گفت که روسیه ممکن است در حال آماده‌سازی برای اعزام حدود 300 هزار سرباز دیگر باشد.
🔴
او این سناریو را بر اساس اطلاعاتی که از سوی سرویس‌های اطلاعاتی اروپا، آمریکا و اوکراین به اشتراک گذاشته شده، قابل اعتماد توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/149250" target="_blank">📅 23:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه، مکرون، در مورد تهدید ترامپ برای ممنوع‌سازی صادرات دیزل ایالات متحده: هرگز با دونالد ترامپ تضمینی وجود ندارد. هرگز.
🔴
او یک ممنوعیت احتمالی را «فاجعه‌بار» می‌نامد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/149249" target="_blank">📅 23:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e544f54d.mp4?token=v7xl5DI_z72CBurMzFP7kCKqdrdpZUTOckzfYK-BWvCW6QXj-xmWFYWpP-YLbWvTvxEUANBWqPIWmNghHnx_UvRY41zqdQgISXOyqnZ8L4kttta88Eb_CBqNle_Y6k9hkDRXzpE_bSkqWxgYNkfeGv4tWudsHYEt0nyAu1Q-ciC97tgtzR1AzOyEj4Cxlf2c3pCXq8gA1suQesU1enZo62hQZaXBnUWhr4P2Z0Ho1sPxrfA-jDsY754c2-mr5YfuFNf6GpWSpWyVSCFOxZZEJNo02sEYnJ95WtCv10h9hLiNHG21SMbWm7ex4ZA-CVIIm_A6ady9BqoQT3m0nvFFMplMbUd3t_FHeGazZZpv6VtbShTaAkguJx3-oi3Dii5QmoKmvWmHFRw8pjJ-KLs1nGw7k7cE94DrfuXJjz9wCeToNpa8lsljSEPSYPqjixCeU0u-VkexYqL1aiKF99lj-1-mYbAZuALZFqFb2neU3BppBtjdYkSqpAK4nsJ8n2oe0waSNPLkn-QjVLkI2YgIO84IBSFYr0TXjEVhmkJ8YSFnvw1QxUzaHs1M5Ii2iQJ36XHu-UQhiC92bd6VOLajhcIvau80y5_2BZEH_pQZkHGzl-Y9PCqioDM27hgQD-hUCygTcpawzM24l8pxifaZDi8d-cn0DqPbKqT4g-k5_ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e544f54d.mp4?token=v7xl5DI_z72CBurMzFP7kCKqdrdpZUTOckzfYK-BWvCW6QXj-xmWFYWpP-YLbWvTvxEUANBWqPIWmNghHnx_UvRY41zqdQgISXOyqnZ8L4kttta88Eb_CBqNle_Y6k9hkDRXzpE_bSkqWxgYNkfeGv4tWudsHYEt0nyAu1Q-ciC97tgtzR1AzOyEj4Cxlf2c3pCXq8gA1suQesU1enZo62hQZaXBnUWhr4P2Z0Ho1sPxrfA-jDsY754c2-mr5YfuFNf6GpWSpWyVSCFOxZZEJNo02sEYnJ95WtCv10h9hLiNHG21SMbWm7ex4ZA-CVIIm_A6ady9BqoQT3m0nvFFMplMbUd3t_FHeGazZZpv6VtbShTaAkguJx3-oi3Dii5QmoKmvWmHFRw8pjJ-KLs1nGw7k7cE94DrfuXJjz9wCeToNpa8lsljSEPSYPqjixCeU0u-VkexYqL1aiKF99lj-1-mYbAZuALZFqFb2neU3BppBtjdYkSqpAK4nsJ8n2oe0waSNPLkn-QjVLkI2YgIO84IBSFYr0TXjEVhmkJ8YSFnvw1QxUzaHs1M5Ii2iQJ36XHu-UQhiC92bd6VOLajhcIvau80y5_2BZEH_pQZkHGzl-Y9PCqioDM27hgQD-hUCygTcpawzM24l8pxifaZDi8d-cn0DqPbKqT4g-k5_ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تاکر کارلسون: قطری‌ها به ترامپ یک هواپیما دادند. و این کار چه چیزی برایشان به ارمغان آورد؟ هیچ‌چیز.
🔴
ایالات متحده از قطر دفاع نکرد. ایالات متحده باتری‌های تاد را از خلیج فارس به اسرائیل منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/149248" target="_blank">📅 23:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5c5d8dde.mp4?token=rcJ4Pe2j4ySWGz7_4a27zZVzWJQo4LZZp9uk-lPe3U50ORByec31RbfF_--DJ7_Wrr39zqloDtwAfW9GfBakzyVA0OGCvTj2aqtmMH4SrawGG4yMXdUxsLYZSNbBAsva1q-QX1HDkJctnx7iJyMS3Qe41DILxlpm93GtB9N-9vG6Vmhd5eUmPRGo7KaAdFk_AlJ3AnYavyo4-2eU3yeu2WBSszxxwMPZAbaHdKp0X1CxAzihC3ZD6Q9DtnwTWdY08Olr9GMrMIJzAeyHhSkrgIDP9JsE4YqADRwFq7LKcUGf-rmO9T4jZr8WpSNf2ScQbhI43atgyRNn5h2S-qgrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5c5d8dde.mp4?token=rcJ4Pe2j4ySWGz7_4a27zZVzWJQo4LZZp9uk-lPe3U50ORByec31RbfF_--DJ7_Wrr39zqloDtwAfW9GfBakzyVA0OGCvTj2aqtmMH4SrawGG4yMXdUxsLYZSNbBAsva1q-QX1HDkJctnx7iJyMS3Qe41DILxlpm93GtB9N-9vG6Vmhd5eUmPRGo7KaAdFk_AlJ3AnYavyo4-2eU3yeu2WBSszxxwMPZAbaHdKp0X1CxAzihC3ZD6Q9DtnwTWdY08Olr9GMrMIJzAeyHhSkrgIDP9JsE4YqADRwFq7LKcUGf-rmO9T4jZr8WpSNf2ScQbhI43atgyRNn5h2S-qgrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار و گفت‌وگوی عراقچی و وزیر امور خارجه اسپانیا در حاشیه نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149247" target="_blank">📅 23:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گروسی: برای حل دیپلماتیک موضوع هسته‌ای ایران با همه طرف‌ها همکاری می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/149246" target="_blank">📅 23:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بغداد: آمریکا پایگاه «ویکتوریا» را به عراق تحویل داد
🔴
تحویل این سایت، بخشی از اقدامات مربوط به پایان مأموریت ائتلاف بین‌المللی ایالات متحده در عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/149245" target="_blank">📅 23:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae9e916b8.mp4?token=nE56ZO-kN06eXV1mHor2duf1UES6WVPcq9xubKfle5Eqo0PSBUVlBskceyh3hqaREoyJHiggtmlQHzq-CeBEIsp8muJDjn8iTOWa7UPeByc_h2P1xZThHqynenqzwKIoQMywPbpxfj87nmG8znUjdnYAjFJd-Vj7vaI7FkHLowdy1w5WWcexzhWrYYAoDmH48sk9esQollQ2Vo-kk2Q6kwOCWg25MrXN4ea-eAJAu6A18mKtbhEHDfKeUeo1h9Py5flN5a122w-Zq0P8OVRXKZttb5cZBBe5F5RTIr2ugcfaYvCXTb0DWjY_4VIIC6rpnvpW7t06gMP5651qDCZWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae9e916b8.mp4?token=nE56ZO-kN06eXV1mHor2duf1UES6WVPcq9xubKfle5Eqo0PSBUVlBskceyh3hqaREoyJHiggtmlQHzq-CeBEIsp8muJDjn8iTOWa7UPeByc_h2P1xZThHqynenqzwKIoQMywPbpxfj87nmG8znUjdnYAjFJd-Vj7vaI7FkHLowdy1w5WWcexzhWrYYAoDmH48sk9esQollQ2Vo-kk2Q6kwOCWg25MrXN4ea-eAJAu6A18mKtbhEHDfKeUeo1h9Py5flN5a122w-Zq0P8OVRXKZttb5cZBBe5F5RTIr2ugcfaYvCXTb0DWjY_4VIIC6rpnvpW7t06gMP5651qDCZWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور چین، شی جین‌پینگ، هنگامی‌که ترامپ، پرتره‌ای که عکس خودکار چاپ شده بود و به جای عکس جو بایدن در کاخ سفید نصب کرده بود، به او نشان داد، خندید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/149244" target="_blank">📅 23:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c752dcf0.mp4?token=YfgK9ZP7w0jJLAz_05y9bXxBzfR-e5F7MEpVKZ1g1bH1y5C5RHFSKkOurXsqn4mGQGT1-gEl4t6XioIx9HlNkD_Zz9Mg9dwBNQDraYI9OiR9fpT-priY_-eQlGNm_FEBXThQPIftBkEjUR0ecquFiwr9F191gpwYmLu2LKwwRbCFW-L_ASNSSW-8M7stj8bWrGn8ITN23MYWwYDLmKDwNJq0Asp6N48vh-pyO-aYjqz2YPPZA4OXHgwGKuy0o-htSgOTdRbytr2XZaMHPjw7VddMi2hDwMLKtlhMEWQKcZsLQ7CrQS3NQU7h47IdMwbsOmu-P6ARHDLYOAWpgtXLWKjYeh4FG9q6YBbmPqMb1R0QxEaPoNZDBzNZH4fbJJKNrOfq8xy88AyIsajgZcajPUl6tMtFW6prr9HHv1yQ8pT6e0EnrDRy5E4zzkswCi6yj-4HIHyZnW5Fe6aiJWYgWSq8_cEriZoH03ItTut1mh7PCM3dnj6r9TG5tIl_nZwXgvNR-DJt6NfuASSeLTYAIidZEnNIzDQIkwyWm8nL2gnIXV3-inzXy4cIi34d4eUkbnuoCB41fjJA5BtZgabnWchb9OOrTq9NVc4CRz_n173r3FTLH8esakM9L-mmBo6EHBODaPsEwZfDGGkIHTnwde-367cMW0EM81K1f0uQSl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c752dcf0.mp4?token=YfgK9ZP7w0jJLAz_05y9bXxBzfR-e5F7MEpVKZ1g1bH1y5C5RHFSKkOurXsqn4mGQGT1-gEl4t6XioIx9HlNkD_Zz9Mg9dwBNQDraYI9OiR9fpT-priY_-eQlGNm_FEBXThQPIftBkEjUR0ecquFiwr9F191gpwYmLu2LKwwRbCFW-L_ASNSSW-8M7stj8bWrGn8ITN23MYWwYDLmKDwNJq0Asp6N48vh-pyO-aYjqz2YPPZA4OXHgwGKuy0o-htSgOTdRbytr2XZaMHPjw7VddMi2hDwMLKtlhMEWQKcZsLQ7CrQS3NQU7h47IdMwbsOmu-P6ARHDLYOAWpgtXLWKjYeh4FG9q6YBbmPqMb1R0QxEaPoNZDBzNZH4fbJJKNrOfq8xy88AyIsajgZcajPUl6tMtFW6prr9HHv1yQ8pT6e0EnrDRy5E4zzkswCi6yj-4HIHyZnW5Fe6aiJWYgWSq8_cEriZoH03ItTut1mh7PCM3dnj6r9TG5tIl_nZwXgvNR-DJt6NfuASSeLTYAIidZEnNIzDQIkwyWm8nL2gnIXV3-inzXy4cIi34d4eUkbnuoCB41fjJA5BtZgabnWchb9OOrTq9NVc4CRz_n173r3FTLH8esakM9L-mmBo6EHBODaPsEwZfDGGkIHTnwde-367cMW0EM81K1f0uQSl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فون در لاین از اتحادیه اروپا درباره کانادا: کانادا به دلیل جغرافیا نمی‌تواند عضو اتحادیه اروپا باشد. این تنها دلیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/149243" target="_blank">📅 23:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EXg6B6d43QPYjcvjMicqTZYHet36-wRmFj3xXknx2vgOQUEC490JnNh2uSHqpxoIVQOdLEgjcGG27wbyBz5NxlKYVP4RY78u0TnmH6mjhEem8Jb7y-nn07GzwfnqCwtKru-QEsRWOWDnir88Zx821pKHLFu-Z6_UmdzXRHJ1zlau5ozuDtLSZxy1gSGKUevp6IAed7hDUDIh6zm7ezaqLBiUihBBZSTZRxtmRT1qdrr8eFv0s8Mvo1jbLD28TFYFsRjXjL-TITJA7Zlvg7LBBYATcNVX5oYArDpCyyrifdIZgt8WpdfFkAfc_EsfMUyh4E0y9TwWWtjxuP5PZjySWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی عربستان ۵ حمله هوایی به
جزیره کمران
در استان الحدیده یمن انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149242" target="_blank">📅 23:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
قیمت واکسن آنفلوانزا اعلام شد
سخنگوی انجمن داروسازان ایران، قیمت واکسن آنفلوانزا برای مصرف کننده را دو میلیون و ۱۸۵ هزار تومان اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/149241" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=UKhrgGcNMiiPPCYVeVLvbThxw5Vhqa98Jh4P-Zn6D8UXmUYQptYTt210DOXB8BfUBzDBE8sHgh7puuDRGLK2Xw9PPBP8c743RBeCfnDONxKLTKJdhSpeX0v3jYBWAGrq5myUj52qR0N5SgcZB_Oq9DsIEb369jJPLXJg6xhJj89dE2mZRnxhwZhnfiy9Jb4WalMUdT3sbB88WssbtCGSNC3NDPuV6y9JLuIO8OJd4Svf5yfWSA4h9Ld7kvdS08U-vFeLP6rc7Mc3Z1R01Zng04T00uUkVMq4shvOyiG3VgqpawJP3DoH_SHUGZjUYZaiMlDZzHKLZEE9QncBjb8v0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=UKhrgGcNMiiPPCYVeVLvbThxw5Vhqa98Jh4P-Zn6D8UXmUYQptYTt210DOXB8BfUBzDBE8sHgh7puuDRGLK2Xw9PPBP8c743RBeCfnDONxKLTKJdhSpeX0v3jYBWAGrq5myUj52qR0N5SgcZB_Oq9DsIEb369jJPLXJg6xhJj89dE2mZRnxhwZhnfiy9Jb4WalMUdT3sbB88WssbtCGSNC3NDPuV6y9JLuIO8OJd4Svf5yfWSA4h9Ld7kvdS08U-vFeLP6rc7Mc3Z1R01Zng04T00uUkVMq4shvOyiG3VgqpawJP3DoH_SHUGZjUYZaiMlDZzHKLZEE9QncBjb8v0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه فاکس‌نیوز تیزر مصاحبه رئیس‌جمهور ایران را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/149240" target="_blank">📅 22:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1915ce4848.mp4?token=bA1yTjDhoRyvHJemILytLw9QbLilDo9PqJp2iBPDUnsGx74Y8iy7NvU1s-_tC8lmyEInUvsh-Ep5fap-Otjo6ujuYoVZ1lPlBkAejOyL6AKqiD42pgMCnaXMbgw7tuRdSnYL7aV7Ndayxuno8x946awHQb72dZeBlpFDPgjfvUWrf4iniXc_xAL-nar-K_bGOr7L0qYVTGSPhuXXiKse0Gsqk4jHUmYybXua2WbS_N1bmdjw9euRpN7goh5L2nrv4eqkrngTblnNX9vKjXnKFysvK-mjdpCXJhX4JP9JcwzUP-Il7q_Nhh4249RWwbOTpJFfQ2p-xK4AOYAyoe-goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1915ce4848.mp4?token=bA1yTjDhoRyvHJemILytLw9QbLilDo9PqJp2iBPDUnsGx74Y8iy7NvU1s-_tC8lmyEInUvsh-Ep5fap-Otjo6ujuYoVZ1lPlBkAejOyL6AKqiD42pgMCnaXMbgw7tuRdSnYL7aV7Ndayxuno8x946awHQb72dZeBlpFDPgjfvUWrf4iniXc_xAL-nar-K_bGOr7L0qYVTGSPhuXXiKse0Gsqk4jHUmYybXua2WbS_N1bmdjw9euRpN7goh5L2nrv4eqkrngTblnNX9vKjXnKFysvK-mjdpCXJhX4JP9JcwzUP-Il7q_Nhh4249RWwbOTpJFfQ2p-xK4AOYAyoe-goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 15 عبری: احتمال دستیابی به توافقی بین ایالات متحده آمریکا و ایران "بسیار کم" است، اما غیرممکن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/149239" target="_blank">📅 22:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
یک مقام دفاعی آمریکا : حدود ۶۰ کشتی تجاری روز چهارشنبه از تنگه هرمز عبور کردند؛ رقمی که به گفته او بالاترین حجم روزانه عبور نفت خام از اوایل ماه جولای بوده است.
🔴
به گفته این مقام، حدود ۴۰ کشتی از این ۶۰ کشتی برای دریافت حفاظت، عبور خود را با ارتش ایالات متحده هماهنگ کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149238" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مکرون خواهان برقرای آتش بس فوری در خاورمیانه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/149237" target="_blank">📅 22:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو: ارزش‌های ما، بشریت را برای هزاران سال الهام بخشیده‌اند... و تلاش ابدی ما برای صلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149236" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مکرون: ما تجهیزات نظامی و سربازان را برای محافظت از کریدور دریایی در دریای سرخ اعزام خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/149235" target="_blank">📅 22:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنرانی نتانیاهو تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149234" target="_blank">📅 22:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa32aca47b.mp4?token=Rzfpbn-0ccG5GaLt9udOPSwcAfg1cj4MHr7QzgB9j-I-zh2jdGa00BCwqwM00fHOOjJQZiksYKaeDsK6drspxYmcWddyzTiIgQnMlg4_KXFo0609JYUO2ySMpm-Cua6sHpp90KFkancTnhPJGxgbO8Myo9qPVn43yC-Mqcmdb-7axuJNSiHlemxZrgc9A66Z1kMQPMNY97sRjDGTrrh5_cqI9FjHU464j2ElIRxH6CVHMYKuLcHzibOySt_q6dzlaUxsRtZ0VrA2bhS2BeH0mh-XRLInZ9hbQPq3UV_MrlFZsBrg805RtXWxdfMlotVxu8UuA5FF3oHdFY81iLi1JjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa32aca47b.mp4?token=Rzfpbn-0ccG5GaLt9udOPSwcAfg1cj4MHr7QzgB9j-I-zh2jdGa00BCwqwM00fHOOjJQZiksYKaeDsK6drspxYmcWddyzTiIgQnMlg4_KXFo0609JYUO2ySMpm-Cua6sHpp90KFkancTnhPJGxgbO8Myo9qPVn43yC-Mqcmdb-7axuJNSiHlemxZrgc9A66Z1kMQPMNY97sRjDGTrrh5_cqI9FjHU464j2ElIRxH6CVHMYKuLcHzibOySt_q6dzlaUxsRtZ0VrA2bhS2BeH0mh-XRLInZ9hbQPq3UV_MrlFZsBrg805RtXWxdfMlotVxu8UuA5FF3oHdFY81iLi1JjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره حملات ۷ اکتبر:
به‌طور نسبی، این معادل کشتار ۴۰,۰۰۰ آمریکایی بی‌گناه در کمتر از ۲۴ ساعت است.
🔴
این ۱۶ برابر ۱۱ سپتامبر است — ۱۶ تا ۱۱ سپتامبر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/149233" target="_blank">📅 22:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aae11072a.mp4?token=m8R1YjO2qV5-5I5PnB0Rlgexu84dGllZ4ie_Y1iy5x8XSUO8-tN7kopR42QT-3S0eKlidxwp6K5Mmo_FdOI8E2i-GTJ5P6cHgiqPlfhnCEnvvXsNFllf1rviF2figEvne4CA8wKNPfOfkiL__k5ci8prwuIwTST-WmHH7p40nvzLqrorEgYeulrMsh92yLr6-8EYamHr_8XLQ4a3WO8xHEcc4VvK54odJsG_kdnQHXWq8z8ueuAvUOk5U1MtWBV0QgnH0tizH8TQ3JyZhjbrd2DM1o8HTPdSCggbDipwuZL4U3A0mK_V44DAO2VKIHQnAdC_cB9UvB2wrw9piAQ-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aae11072a.mp4?token=m8R1YjO2qV5-5I5PnB0Rlgexu84dGllZ4ie_Y1iy5x8XSUO8-tN7kopR42QT-3S0eKlidxwp6K5Mmo_FdOI8E2i-GTJ5P6cHgiqPlfhnCEnvvXsNFllf1rviF2figEvne4CA8wKNPfOfkiL__k5ci8prwuIwTST-WmHH7p40nvzLqrorEgYeulrMsh92yLr6-8EYamHr_8XLQ4a3WO8xHEcc4VvK54odJsG_kdnQHXWq8z8ueuAvUOk5U1MtWBV0QgnH0tizH8TQ3JyZhjbrd2DM1o8HTPdSCggbDipwuZL4U3A0mK_V44DAO2VKIHQnAdC_cB9UvB2wrw9piAQ-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو نخستین رهبر جهان است که از اصطلاح "هوش برتر/Superior intelligence" که پرزیدنت ترامپ ترجیح می‌دهد، برای اشاره به هوش مصنوعی استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149232" target="_blank">📅 22:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو یک دستگاه آنتن استارلینک با خودش به سخنرانی آورد و به دبیر سالن داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/149231" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو درباره جمهوری اسلامی: می خواهم خبر خوب را به شما بدهم. با وجود سکوت شما، با وجود ریاکاری شما، تنها مسئله زمان است که در ایران چیزی باورنکردنی رخ دهد.
🔴
قدرت مردم بر مردمی که در قدرت هستند غلبه خواهد کرد!
🔴
می‌خواهم کلمات مرا با دقت گوش دهید. یک روز، و شاید آن روز دور نباشد، مردم ایران آزاد خواهند شد.
🔴
حکومت قاتل آن‌ها با دروغ‌هایش، با فسادش، با بی‌رحمی‌اش سرنگون خواهد شد.
🔴
این حکومت شیطانی سقوط خواهد کرد و ما همه آن روز را جشن خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149230" target="_blank">📅 22:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iywtSSJxf2lVytfr-Vgcw2YS0ail_iYKPwF6gRFpu7PRN2tePqYJtsLfjTiawg1NSnoFHkSR2nIpjgj0QR6X-msE8DE62L2Dpg6t12u3FOogQ1dQ012BvImyyHNVDnqUpe1iMRBVm6ibQglaf6JMFfIknJDCs-HXVwexItZUJpnc5cK7PoH0F7jdDghahod_QAi1OH3cEfPB6WZFiyHGX2aMOZ9xW0nJw78BL4rJkgJ-HVobjd7noZ6rgvs2feWQWPaOaH74YnsV032VbTIqXDkfbKEjSWn9egL5HoCbv_mKbW_8NutnGoVBGw9tKXbaJcaKMb9rdz1IpuCmuZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده امارات پای سخنرانی نتانیاهو نشسته و سالن رو ترک نکرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149229" target="_blank">📅 22:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نتانیاهو: کتاب مقدسم میگه ما در نهایت پیروزیم؛ متشکرم از شما
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149228" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a98d071e9.mp4?token=MItf8umJp9_Jy3fDXV77k-QxS0FWEX80kgQK-W7SL71Eh6J1V0mbwmftrq4RvFYjqdSeHp3TVHAcnXqWskws5hTQCt2kD8pYY5b8FB2jFjaixVIHkK3ArusxA9ktiyKF3j4EBwz4Akq2e4wJb6iOKnaKgVLvknX8MHO4IAPwaQi1ZROV3F8t6a1SvY0S74yzPPDbpHpxBfWGLpO7M7Y11ME7nAx6husK-xDZxUUCHvhJFTFmc89mCIOjBiBRJsycJR-Hw4fDg7c5s9RwjB-dZf3P1yvRrmn9HOH--LbZZl2Ai7_ZCvg-lhCZhmuM7cpQsbXe1uC_JCJpJyC6otapLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a98d071e9.mp4?token=MItf8umJp9_Jy3fDXV77k-QxS0FWEX80kgQK-W7SL71Eh6J1V0mbwmftrq4RvFYjqdSeHp3TVHAcnXqWskws5hTQCt2kD8pYY5b8FB2jFjaixVIHkK3ArusxA9ktiyKF3j4EBwz4Akq2e4wJb6iOKnaKgVLvknX8MHO4IAPwaQi1ZROV3F8t6a1SvY0S74yzPPDbpHpxBfWGLpO7M7Y11ME7nAx6husK-xDZxUUCHvhJFTFmc89mCIOjBiBRJsycJR-Hw4fDg7c5s9RwjB-dZf3P1yvRrmn9HOH--LbZZl2Ai7_ZCvg-lhCZhmuM7cpQsbXe1uC_JCJpJyC6otapLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت ایرانی هنگام سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل حضور ندارد.
🔴
در محل استقرار هیئت ایران، تصویری از قاسم سلیمانی همچنان قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/149227" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aaac1b06f.mp4?token=SpJv8lDGH5-ACdUW7FScxuuONAbVw-B7KDutW1S6eTN1wdvziMtimsFjYB4Xncy7oB5UEavI4GvlN840OiMwLK3iIU55siK6r8IEJgbQbBbJZ2usPm16-gluG-KduN0mGQHybTRwAurn9uS88AIAcGYnU_H6e8nT2rCLRYfJfm6fn8M2cXyhhZ-ukmcQQmJElkqersknUtSnA5mKNsQapL_eb948gsqAy6kxe_IZTTXX-SK0SNu2eR6LZyah9c3dAtrCx_w3Ic6RKNvxln-uVw0Bdba0Va3LZzcTGflFbEXI8Qamcls2D5x1bwpXo_ullveLJZ2OdpSWRL3b4LngoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aaac1b06f.mp4?token=SpJv8lDGH5-ACdUW7FScxuuONAbVw-B7KDutW1S6eTN1wdvziMtimsFjYB4Xncy7oB5UEavI4GvlN840OiMwLK3iIU55siK6r8IEJgbQbBbJZ2usPm16-gluG-KduN0mGQHybTRwAurn9uS88AIAcGYnU_H6e8nT2rCLRYfJfm6fn8M2cXyhhZ-ukmcQQmJElkqersknUtSnA5mKNsQapL_eb948gsqAy6kxe_IZTTXX-SK0SNu2eR6LZyah9c3dAtrCx_w3Ic6RKNvxln-uVw0Bdba0Va3LZzcTGflFbEXI8Qamcls2D5x1bwpXo_ullveLJZ2OdpSWRL3b4LngoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل مرتکب نسل‌کشی نشده است.
🔴
اسرائیل از وقوع نسل‌کشی جلوگیری کرده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149226" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / سنای آمریکا با طرح قانونی محدود کردن اختیارات ترامپ در جنگ با ایران مخالفت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/149225" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
«باید صادقانه با شما صحبت کنم. همه ایستادگی نمی‌کنند.
🔴
ما این موضوع را دیدیم؛ زیرا برخلاف اسرائیل، برخی کشورها، و به‌ویژه در اروپای غربی، در موارد اخیر تصمیم گرفته‌اند ایستادگی نکنند.
🔴
رهبران این کشورها تصمیم گرفته‌اند در برابر گروه‌های یهودستیز تسلیم شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149224" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=QvXQHBmJZo1bATUJaqy8Ua67szgwdlk2FEe51o5ofigHxvDGlfWNQyf8oIRtLj75cXA8JzcCpr_2EEnronki3VjI_6J7V9ljOsLJhSO1ZlrOE0WbEioOAAcaSEaFk6gib1O-0Ak1VxX314h76bvExGvAyfwzlPGrzxzK06x0GsZLfxyUghWkAl-LYevMkiqATXmIqarxqWC_kErg1w89BQcAfxiU5VYcqhIKGz_gffoaIFqadsKH5RINmcPWeFJzFqvqYWwjHPYn_2D7rIzxH8CcOMJ6DpLrmZwFhOspMsuBPAQaFTotORAKuWR0ARWNUnOqM53U4a17yNHyKeQLIi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=QvXQHBmJZo1bATUJaqy8Ua67szgwdlk2FEe51o5ofigHxvDGlfWNQyf8oIRtLj75cXA8JzcCpr_2EEnronki3VjI_6J7V9ljOsLJhSO1ZlrOE0WbEioOAAcaSEaFk6gib1O-0Ak1VxX314h76bvExGvAyfwzlPGrzxzK06x0GsZLfxyUghWkAl-LYevMkiqATXmIqarxqWC_kErg1w89BQcAfxiU5VYcqhIKGz_gffoaIFqadsKH5RINmcPWeFJzFqvqYWwjHPYn_2D7rIzxH8CcOMJ6DpLrmZwFhOspMsuBPAQaFTotORAKuWR0ARWNUnOqM53U4a17yNHyKeQLIi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌خواهم چند سؤال از شما بپرسم:
🔴
کدام حکومتی که مرتکب نسل‌کشی می‌شود، برای جمعیت طرف مقابل یک میلیون واکسن فلج اطفال تأمین می‌کند؟
🔴
کدام حکومتی که مرتکب نسل‌کشی می‌شود، امکان ورود و توزیع ۲ میلیون تُن مواد غذایی در غزه را فراهم می‌کند؟ یعنی به ازای هر نفر، یک تُن غذا.
🔴
متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/149223" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdac61ee8.mp4?token=Ano-WDIVWQKkwarVAW7z891xG2AOg0ZmxPELlzZUk0dXfUFbg7UDAAMymmYlVp5lLkSVaeqvQq_QMrUPBqOXlWu1rWTYs3oVnoAGgHMhFlwO3-_Gkwu5eH7Qx6TTpqHNx61iRKTJLSlqidqqUn7oiNo33ictS6si_3VnQOvbsvN2RgZ3RPF0Uux4jvVBRgqm4J5yCKC0o9kae4FPVkqjcKy_v-YB-WxlY6JUmh66qSPMZuHTlLMsJL-FadaAaJHnFFWiY4y_E7helfhQ9UR5A6Ol0a99JErCJMqQwylEtLf5g81Q9TU6SVAeP70cxw7Nj2w90VFB2IXFXS1rnbo4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdac61ee8.mp4?token=Ano-WDIVWQKkwarVAW7z891xG2AOg0ZmxPELlzZUk0dXfUFbg7UDAAMymmYlVp5lLkSVaeqvQq_QMrUPBqOXlWu1rWTYs3oVnoAGgHMhFlwO3-_Gkwu5eH7Qx6TTpqHNx61iRKTJLSlqidqqUn7oiNo33ictS6si_3VnQOvbsvN2RgZ3RPF0Uux4jvVBRgqm4J5yCKC0o9kae4FPVkqjcKy_v-YB-WxlY6JUmh66qSPMZuHTlLMsJL-FadaAaJHnFFWiY4y_E7helfhQ9UR5A6Ol0a99JErCJMqQwylEtLf5g81Q9TU6SVAeP70cxw7Nj2w90VFB2IXFXS1rnbo4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
از معترض‌هایی که بیرون هستن و از اون نماینده‌های ریاکاری که همگی جلسه رو ترک کردن، یه سؤال دارم:
🔴
وقتی حاکمان مستبد ایران ده‌ها هزار غیرنظامیِ بی‌سلاح ایرانی رو کشتن و زخمی و ناقص کردن، شما کجا بودین؟
🔴
وقتی هزاران نفر از مردم خودشون رو کشتن و زخمی کردن، شما کجا بودین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/149222" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل
:
«رژیم ایران به‌ویژه زمانی نگران می‌شود که مردمش به چنین چیزی دسترسی داشته باشند.
🔴
این یک
دستگاه ارتباطی — استارلینک (Starlink)
— است که به مردم امکان می‌دهد به
حقیقت دسترسی پیدا کنند
و از
آزادی اندیشه و آزادی بیان
برخوردار باشند.
🔴
به همین دلیل، رژیم ایران
میلیاردها دلار برای سانسور اینترنت
هزینه می‌کند.
🔴
آقای رئیس‌جمهور، من این دستگاه را به شما می‌سپارم تا آن را به
هیئت ایرانی
بدهید.
🔴
تا اگر آنها روزی
به‌ناچار از حکومت جدا شدند
، بتوانند آزادانه
داستان خود را در شبکه‌های اجتماعی بیان کنند
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149221" target="_blank">📅 22:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل مرتکب نسل‌کشی نشده است.
🔴
اسرائیل از وقوع نسل‌کشی جلوگیری کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/149219" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نتانیاهو : اکنون، جدیدترین کشوری که به یک ابرپخش‌کننده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است: اردوغان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149218" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل و آمریکا در کنار یکدیگر برای نجات تمدن اقدام کردند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/149217" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43314fb77.mp4?token=nRYuG2xD3Z8BsXfu9pdfzcDtFqFCUX7aEFQyWVNOGSi6wQk9j-ks4AGSx97X7WfKtB8Se1HeWj3_Lfj7YWjP1Nxd9Z6wbmzWjIk25YK_jW91MT_J8o4kIVsdSGNfoAWhyEE7N97ylLzGuweuSobMkHPa36fOkRIMrd7ncFKE5d5W8JK5VVeipowEELRFYr6VWydtQggitt5A0vuBsTdQyg7jh-RAgoOcbh7wuDe5RVOUFXk2HW8KJ23FVLT5zTLHfZUIDaoYG5Tjo2yrZgKLymZDbz1MBL_4QqzMc3qaLF2q2YvuxU-Fk0MFJIHYEjORrwUnURP7AQeaTgYKDgWtsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43314fb77.mp4?token=nRYuG2xD3Z8BsXfu9pdfzcDtFqFCUX7aEFQyWVNOGSi6wQk9j-ks4AGSx97X7WfKtB8Se1HeWj3_Lfj7YWjP1Nxd9Z6wbmzWjIk25YK_jW91MT_J8o4kIVsdSGNfoAWhyEE7N97ylLzGuweuSobMkHPa36fOkRIMrd7ncFKE5d5W8JK5VVeipowEELRFYr6VWydtQggitt5A0vuBsTdQyg7jh-RAgoOcbh7wuDe5RVOUFXk2HW8KJ23FVLT5zTLHfZUIDaoYG5Tjo2yrZgKLymZDbz1MBL_4QqzMc3qaLF2q2YvuxU-Fk0MFJIHYEjORrwUnURP7AQeaTgYKDgWtsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«در این نبرد علیه
بربرها (اشاره به دشمنان اسرائیل)
، هیچ شریکی بزرگ‌تر از
رئیس‌جمهور ترامپ
نداشته‌ایم.
🔴
از او
تشکر می‌کنم
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149216" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE_QvffSamp131u4oX6lOjyhcMbr3X2zbZh3UMkMG9KiJmwkqroK5kWEOfEyTXAU-xejb9SmBFVVxJrTYkRmGzfOSlK2LUbzhZRMyG41AoSodfhOo6ui6m_DHgYxSMR2nQDP4PNVBZrvOChSEYsJTdCOusR4I4fc8PSup8F4WEMO2zLFuBbgqzd6UzLGpe34OtXO_E0epuks1tHRCVR1F85UckDGScPiJZSiqb0ExWrpExbkLqvwrJJj3TnfLWbOh6iLLLHItx8N18a22CCZM6YBCRetqdoRXg4F4pw-4i5Ty3p6lwxrlyfpb9B_qK4DriTvXkFav0hZ3bGMQdDI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: آیا این پیجرها را به خاطر دارید؟ حزب‌الله قطعاً آن‌ها را به یاد دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/149215" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌خواهم از اوگاندا تشکر کنم که اخیراً تندیسی از برادرم، یوناتان نتانیاهو، در محلی که او جان باخت، برپا کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149214" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آنها اسرائیلِ کوچک را به استعمارگری متهم می‌کنند. چه کسانی ما را متهم می‌کنند؟
🔴
در میان آنها، افرادی در بریتانیا و فرانسه هستند.
🔴
آخر برای خدا، خود آنها این اصطلاح را ابداع کردند؛ مستعمراتشان سراسر جهان را دربر گرفته بود.
🔴
استعمارگری؟ بس کنید دیگر!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149213" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «حالا می‌خواهید طعنه‌آمیزترین بخش ماجرا را بشنوید؟
🔴
اسرائیل همچنین از بسیاری از کشورهایی دفاع می‌کند که هیئت‌هایشان همین الان سالن را ترک کردند.
🔴
در واقع، می‌خواهم بدانید که بسیاری از رهبران این کشورها به‌صورت خصوصی از ما تشکر می‌کنند که تأسیسات هسته‌ای ایران را از بین بردیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/149212" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
🔴
من به آقای احمد الشرع سوریه ای می‌گویم که یهودیان از زمان موسی در بلندی‌های جولان بوده‌اند و اگر جرعت داری علیه جولان اقدام کن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149211" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
واکنش نتانیاهو به ترک سالن توسط هیئت های کشور ها: اگر هنوز بزدلانی هستند که اتاق را ترک نکرده‌اند، از آنها می‌خواهم همین حالا بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149210" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP4scwV9kA4gcFApPnP4K5zlTgtXnWfjARByKJaOE13r8ldIRNWN_9ylsrLb-WR6gQu9OkTHR42QVwLZ7UnDJ9777_W7Fhhfb3gUNKjmiRaF0bIp-Wt1qQfBku7Mu7jmiGcAVtOKnZ_8SwJ5qlx79VKOIX0EyWsPeVFdYBjabG3nIp-lI_YOkyyzj8beVf0OuUAipsyCQTDaS71o7kNikZp31PCPdjJqMm-wDTeKPt9augzJUqCqVCeLdjj9ipujUIHmfB0opC7Q_t9ka2KT2TlhJU7kmbE4LabV4fggqImOpWs8iMkaWn8yKOsKkgz37BFGZnX_98KQRBEGKiSBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکنون رأی‌گیری سنای آمریکا در مورد قطعنامه اختیارات جنگی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/149209" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور ایران، قرار است امروز ساعت ۶ عصر به وقت شرقی آمریکا در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس نیوز، مصاحبه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/149208" target="_blank">📅 21:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJthk5u3Lza62FYYFZUntjtdZeDQ6qWbai_6qNZIMH_-53dcjVhctLqnx4ClaqMfo4oL-BDB-ef_ZlKqAwYKRdow3tftvRWUdL4Q4pE0wd1RBfqGQ4WCKpORxayypuWoyVtTj-N8bExYiUSjwNSxXM7acpFxNj2vQIdD9De3mjBTbW2Moej0F5Dmi9wNPx9PkHktPsYv6dHYirng56NBB9ytmniGY6aJDd0SpDyy4hA0wOXvvhramiPndTPC75MzZ2G6xfDQzYpA0PMlHyy7I7M7YcoO_GUL-UzCRsEIz9q97LZlshW9nPKOfiWiN_QxKJ-_3oYLwIGZOMegD8hxSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود ver2 ویژه
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان
﻿</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149207" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2774d824.mp4?token=PfN-VkgnwuNVX7L1rLD03rxZNOXHtnpfKxjME3qhsdD7mNGFL2by-IJDD_1rq2N30U0qFaDKCmcyQF20O2ZGNaoxprS7noMdJ2JTpHY3S4rfYh_5DqQa5Wk9k3y0lNW-HLwriQ5Mvu2CoFC8Unh7WrSwVGIK4E00Z5qZEdJtTpRb3bLx6KoucfipPGC55Qlq0ygt-T8nLHDzih5CN8eGx6t2XSt-mUv15Mp9zRWPqmX6fEpuUw5-OM0SeTsXmMUUyzaQNklJk27vKIIaNRloMuIOlv8fvk1yGCqA1s9gewIyzQCYjYbaSjsVOZeC7ORB2IT-tUjB0J_c7LmEc_RqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2774d824.mp4?token=PfN-VkgnwuNVX7L1rLD03rxZNOXHtnpfKxjME3qhsdD7mNGFL2by-IJDD_1rq2N30U0qFaDKCmcyQF20O2ZGNaoxprS7noMdJ2JTpHY3S4rfYh_5DqQa5Wk9k3y0lNW-HLwriQ5Mvu2CoFC8Unh7WrSwVGIK4E00Z5qZEdJtTpRb3bLx6KoucfipPGC55Qlq0ygt-T8nLHDzih5CN8eGx6t2XSt-mUv15Mp9zRWPqmX6fEpuUw5-OM0SeTsXmMUUyzaQNklJk27vKIIaNRloMuIOlv8fvk1yGCqA1s9gewIyzQCYjYbaSjsVOZeC7ORB2IT-tUjB0J_c7LmEc_RqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی، در حاشیه مجمع عمومی سازمان ملل متحد با «اد میلیبند»، وزیر امور خارجه بریتانیا، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/149206" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg1cj1r9UqrQ5_7RH-YEnqIy28O70TD8HFCuCfaLqCiHPBzrJvygtbvVe4li-cKvkMZHXa072O1TDdqRBULMAF4uKJ5arJJ1aAL9ePkwysgwYRpXcmonn4Hu73YiYO-DvEHn6x5L16mW4D92L6OK0tn7vfl93JrgW5W5ZET0vu9BM2-M1nUcM82Hccs0Tgdtnws4XXp2rly9T4wZV6bqZmX-9jXWQPZ7V4rrDva6NbhNgPUyWIQDDMPM0tcvbMiTkNvhVO4fCv7ZjeLvMnH0sxYScnGIeqxxND5Jh98Rg6mdILLRq3iKjKAfA1P88nmOBPqbBcOvOEC4Uy2tu_HsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطعات کلیدی جنگنده F-35 که گم شده‌اند ممکن است در دست چین باشد
‏
🔴
سی بی اس نیوز: گزارش‌هایی وجود دارد که محموله‌ای از قطعات گم‌شده F-35 به دست چین افتاده است. این جزئیات در حالی آشکار می‌شود که ترامپ با شی جین پینگ، رهبر چین، دیدار می‌کند.
‏
🔴
بلومبرگ روز پنجشنبه به نقل از منابع گزارش داد که شرکت کشتیرانی غول‌پیکر UPS در اواخر ماه مه در حال ارسال یک سایبان کابین خلبان و درب محفظه مهمات از استرالیا به ایالات متحده بود که مسیر آن تغییر داده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149205" target="_blank">📅 21:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=MQN6Mz87pMxlXcpUn2DKF7EXa2nnrNPFtbbqtADjRCF0y30iNeOtH3Y-C12dSOGmoh4awe_fPxBj_VGxwbio409B084qfTDySmyXjjozfFA6N6SBa25Cup9169gptYm0oLOPaJ-zNL9YkHEa2_-UKalWOeKjSfOww0PaF5tAZleJ1AlrFiHKZ2s4n1Z6VBQUUHzCo9QImelEdsC-AN0ouPywvZg2ctJ9-KMoKGjZu_LcK0owlBhDaq8FYgf_Z4l55pc_yjlIbRbWd5WwWLPs3856wXIvS86eZQMbrrp9bpvNK1iTmxrVjsLtjpc-fMxo5fMAKLsxELBidJq04X2sXw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=MQN6Mz87pMxlXcpUn2DKF7EXa2nnrNPFtbbqtADjRCF0y30iNeOtH3Y-C12dSOGmoh4awe_fPxBj_VGxwbio409B084qfTDySmyXjjozfFA6N6SBa25Cup9169gptYm0oLOPaJ-zNL9YkHEa2_-UKalWOeKjSfOww0PaF5tAZleJ1AlrFiHKZ2s4n1Z6VBQUUHzCo9QImelEdsC-AN0ouPywvZg2ctJ9-KMoKGjZu_LcK0owlBhDaq8FYgf_Z4l55pc_yjlIbRbWd5WwWLPs3856wXIvS86eZQMbrrp9bpvNK1iTmxrVjsLtjpc-fMxo5fMAKLsxELBidJq04X2sXw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره شی جین‌پینگ:
«شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/149204" target="_blank">📅 21:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نواف سلام در دیدار با پزشکیان از ایران خواست سفیر جدیدی برای لبنان معرفی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/149203" target="_blank">📅 21:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
به گفته منابع عربی، ایران دو موشک بالستیک را بر فراز حریم هوایی خود آزمایش کرد. هیچ برخورد مستقیمی رخ نداده است. این یک نمایش قدرت در بحبوحه تشدید تنش‌ها در خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/149202" target="_blank">📅 21:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149201" target="_blank">📅 21:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اسکات بسنت: محاصره دریایی و هوایی ایران ادامه دار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/149200" target="_blank">📅 21:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ-UlN03c9TUvx614SoxWARDE6GVB8m6WRW2F6Tjabub1co4gLjp_FZn-f0eZ-abfM9j-4FyJhzOoJQ-Nbi6a7tqVsfQ5KIF3DtkWVkSiIeZ5MjWBChm7RPvLwY4TBIp4I39PhOk-6AN5gAAMk1jZ80ZUSJD7MlWe5ciQIbj3bDVfOkgf00rQVZJV-UyMYIgihwFx_StVIwxVvTKO3AUdssZ7QcK1EHohyySpdXhdUe0sQc9pS1Eo0B0UwcJ1AlQ_EJy5dbkA4iaIOQfcHYviOa_27Jx7IGH3KxyG8RrUHButQJCoA0EslAkFW_jJnVP99M6fXIIu13_mXBFzxo9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی بعد باخت:
بازی خوبی بود امیدوارم روند بهتر بشه، این شب‌ها از مردمی که تو خیابونن میخوام تو عبادتشون ماروهم سهیم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/149199" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اد میلیبند، وزیر خارجه بریتانیا:
«یک سال پس از به‌رسمیت شناختن کشور فلسطین، ما همچنان به پایبندی به آنچه درست است ادامه خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149198" target="_blank">📅 20:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/شی جین‌پینگ خواستار بازگشت فوری ایران و آمریکا به تفاهم‌نامه «اسلام‌آباد» شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/149197" target="_blank">📅 20:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش شلیک موشک به تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149196" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پرواز ایران‌ایرتور به دبی لغو شد
🔴
پرواز امروز ایران‌ایرتور از تهران به دبی کنسل شده. ظاهراً امارات اجازه ورود این پرواز رو نداده. هنوز علت رسمی اعلام نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/149195" target="_blank">📅 20:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
۸۰ کشور با انتشار بیانیه‌ای مشترک در سازمان ملل خواستار بازگشایی فوری تنگه هرمز شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149194" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رویترز: مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک در حال بررسی مسیر مرحله‌ای برای پایان دادن به جنگ هستند
🔴
مسیری که شامل بازگشایی تنگه هرمز از سوی تهران و لغو تحریم‌های اقتصادی واشنگتن علیه ایران می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/149193" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXWLMWl3F3c22jAnM4C0xSfHB3kCM5BqT8EMchTXZrCmSoj0UnJbtJaUYajRFjubJgbuBgK_cfi-vcXBNtYTDpnyXORBTHBcjUM5CQRmVHBV-QO90jBO86J1qwMtMCoCyIDJNlZ4IFWcANoEsvHjQ4YOuqQ4-CJo8JzZHXqM0SKgbYFFqCvLPpJB0byomeLhZDtxdpcy72Z-WIeMFYCZNcIuLyJmVDZ7Mxo_yt0TFh6uCQYbNLBEehXFp24_KPJ9u-ZLvcKIzXoLtIpjgQxZ40l3prynQDTIocKRNptTgELkadnuw-ZQF6bjvJbcMNMkrHFckWJgJovQJHPyUU7fKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به ۱۰۸ دلار برای هر بشکه افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149192" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3hR3wS5v3IO2FgclYPxZFrKW9tRz1RPhaesf8MzUm677STOc9tsPwN34M76eyZplI9RnvMIyqwnbpXsaSwNXq0aIjA-rDYwKV7txJrPCr_oiC3AHsmmc-jDLhCY_PNFw1oaaSTP4HUhGeF5DIZstkAtqfOrsXMIxa466NcArL1YXQsl9lG-Rn-d-n7qVMh8gkHiAgqGAGtCpyoG5bSGhEFnDPDhYDIFxfOjTFB83ors0l5QnQm_9ZIj3FD3D1cEdJjWxYS0hCQnANmCCvxL7HWBUxKSMGyXiYzq4lpbORXvYFqmOHEZnD07KPBZ6XsUtEBaRO2Ry3hKOh7Yt4Dh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mu7WTpR5CJgOZoKx8xkUBBtY120xQj56kOe5rekxypWv56mNKtX8l_quoslrFIkQF758nU6VAGSRXPTUFbd1yhcI26Co27wewbV15UcfwXCBVuwfv-WgW3Vdc8_uGwmj-Fgx80AcmEeKJlVVoFhV4bSeY3jqwooybZxhQ2IoOljDMtsrrAcFOJWX4qUQXSTKH4w5byixczbIQ5dLqYOt8M1_YLUaVmpx_Kp0MKKoDAcZjs3U9J4723_M0jtiS9A16OjJ9HtJFgLNbdOhD_d2PZA3pOWdlGT5wXXaUB71jd6H83YaHxw5pA9TCODaOdABpX2FztOOnVUi994SmT0cWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه ایران در حاشیه مجمع عمومی سازمان ملل با فیصل بن فرحان، وزیر خارجه عربستان و ایمن صفدی، نخست‌وزیر اردن دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/149190" target="_blank">📅 19:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhG6NsY2flvBZnFq1mB4mPJK_N-APTQ_sIpNe0httinroXINQhWt2u-58zi6a1biBLszYFoDB3WaAQVr-rJgOWj7yOsYWOVlllMQe5STprogQ7PRiE36x3ip9BH63zgY8Dbz3MXN5o2Xr2EtYD7bGIwezEPV0OiNK9W_YWZ60366USdje0cxn2xaxF83xWjC0qU-_hnHa23AxmS9uOaD2qpoDn_LeLYfUTETNZ33_Ryr7WIB-y0YKrn6r-2kXiN4HIGEnYGY8pqOECoqru77-1y1MS00U9Xtj6jDF8WkZjLiqn1MAdBcfz7umaqcJ_9M-yamK2ZtDYiaa8ZqKxUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دفتر بیضی کاخ سفید در حال گفت‌وگو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149189" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ac28e8cd.mp4?token=S9tjbxf4_fy2pSYSh8qpfRTAtz6hg0OFE13FF35soKWNAFnEthX_hLYKUXvvZ2O0m4WXU67lbHUsnHBWwpd1NUYhvC8-gS2LQYk_z05DmKgsoXszVDHk5hrzoWz6OJYjvKON7U6fd8vK_na7bJ3y5ghLH3EWdoKTGTfh5ED3MtiZllODDbudEoaimauOK_HxZRUZhQtXOlruN1nvmFLjPnHJCBGZIOyJ1OhTqa6MJSTV781nSc8027Sd-qp5u-rT48Ge9lqnCHKy940kdlY4uBAr2nYVQpFdiSjpIPTQ-uGxNVdgq1_akENDIpeXFVLnkg2GNxIH2dFkcNVjHtyXYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ac28e8cd.mp4?token=S9tjbxf4_fy2pSYSh8qpfRTAtz6hg0OFE13FF35soKWNAFnEthX_hLYKUXvvZ2O0m4WXU67lbHUsnHBWwpd1NUYhvC8-gS2LQYk_z05DmKgsoXszVDHk5hrzoWz6OJYjvKON7U6fd8vK_na7bJ3y5ghLH3EWdoKTGTfh5ED3MtiZllODDbudEoaimauOK_HxZRUZhQtXOlruN1nvmFLjPnHJCBGZIOyJ1OhTqa6MJSTV781nSc8027Sd-qp5u-rT48Ge9lqnCHKy940kdlY4uBAr2nYVQpFdiSjpIPTQ-uGxNVdgq1_akENDIpeXFVLnkg2GNxIH2dFkcNVjHtyXYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، به مقر سازمان ملل متحد در نیویورک رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/149188" target="_blank">📅 19:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149187">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عراقچی خطاب به وزیر خارجه پاکستان:
نقض تفاهم اسلام‌آباد از سوی آمریکا سبب تشدید تنش در منطقه شد
🔴
پیمان‌شکنی مکرر واشنگتن، موجب خدشه به جایگاه نهاد میانجی‌گری است
🔴
تشریح آخرین وضعیت گفت‌و‌گوهای ایران و عمان درباره تنگه هرمز و تعاملات با ایالات متحده از طریق قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/149187" target="_blank">📅 19:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149186">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=hnoJSWdx_laARbe1gG8NrXRjmx-bFRdz9SL8LzCByFvBlL0tjLKNi7zPrRTHI4tKydSoXI1MOR4yYZWIv6Yw2u-aMVzeppXBnEdSEgSR-KYhHEUFMSGHWYH2UggBrvcuCiERZQUM4h64ahqKP_IHfx0vj8AJnTBX5ezqtD3gIN8w677t6uSfPC8T-4-RdyC9CzY-D_QtMrSbVqUkv6Q6Q7rYYiaj5MmdfJg4J5iN5ETn3zEAXYanhBc2_TdKSSi-ZIzoR6aYNfyS_psjkRUQ9Br030xRprg1OujUl0WoZhm4maalAKY5vdxcmJzzSA_1mQ9R7MIfSzZn5Kuhx7xM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=hnoJSWdx_laARbe1gG8NrXRjmx-bFRdz9SL8LzCByFvBlL0tjLKNi7zPrRTHI4tKydSoXI1MOR4yYZWIv6Yw2u-aMVzeppXBnEdSEgSR-KYhHEUFMSGHWYH2UggBrvcuCiERZQUM4h64ahqKP_IHfx0vj8AJnTBX5ezqtD3gIN8w677t6uSfPC8T-4-RdyC9CzY-D_QtMrSbVqUkv6Q6Q7rYYiaj5MmdfJg4J5iN5ETn3zEAXYanhBc2_TdKSSi-ZIzoR6aYNfyS_psjkRUQ9Br030xRprg1OujUl0WoZhm4maalAKY5vdxcmJzzSA_1mQ9R7MIfSzZn5Kuhx7xM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار پزشکیان و نخست‌ وزیر لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149186" target="_blank">📅 19:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شاهکار قلعه مرغی
‼️
ایران ۳ بر ۱ به ازبکستان بخت  @AloSport</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/149185" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7HPfJzWsSBB3nzjhuouAjrCsskhcBoykiEv_gRTkYnror56b-7QQRWizvIUiF0BCL1ReDzlvLgU86Q2DkrhlXdtUg53Cff_c0nT-375SpKC5e1CarCKNw8WqyoOFXSTO1-rUryo8_r_shAmNeeQ-GWa-Fq0QyAGvVYzn955M9_HSY7qP12dyBCpLS3E0T4VIqQ_w4xBb6o9HDmLoQgzzzZ5WceijnIWtJh2I4RtsN-wTg_5UF8wX4HEPoytWN8WgMfif08ZQlyB-xq_8PEArutm5pZm8bB7BYQb26SHUs-VG4r8FFZJ9AXkbQTS9rV1woXz2Izbf1O1CZmjlY-cgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: عربستان انتقال نفت خام از طریق خط لوله شرق-غرب به بندر ینبع را افزایش داده، اما صادرات نفتکش‌ها هنوز از سر گرفته نشده است
🔴
آرامکو در حال ذخیره‌سازی حجم کافی نفت در ینبع برای ازسرگیری صادرات است. بازگشت خط لوله به فعالیت کامل ممکن است ۶ هفته یا بیشتر زمان ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149184" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149183">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رشیدی‌کوچی، نماینده سابق مجلس: آقازاده‌ها از شرکت خارجی کالا را می‌خرند و می‌گویند فاکتور را بالاتر بزنید و هزینه‌اش را ملت ایران پرداخت می‌کند/ پدر آقازاده‌ها همه چیز را می‌دانند و خودشان را به ندانستن می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/149183" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
