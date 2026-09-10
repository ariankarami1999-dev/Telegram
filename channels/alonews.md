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
<img src="https://cdn4.telesco.pe/file/CzkjVa6VyTe59Ds_gIgwgwN8Udr1tguE2C38FUVeLAl3eM77rBwC9jSvlSnBZeY21cj-jeKASVcd1wzT10UVHfw2dCSQSOgpTMIkqIUXjaZIemVAshxTJmn054mIuI9UJ4Qmq-Ru-jpZeW3r7oCo85M7liR0meUnNexH9ak2piffYKmn94OvX93Q3qaNkYlKVQpC0WiFA-AKmy6FhaDjDHnAfvR1Tjpn1Kne9qpZ1Lq4hDkwtKtKd2SqHtu5d9W7Fnm2PqBQ9y6qnHtr7kh0VAy3xWdVcuhRNAleDVWiu5MkW4yfjZ4Yl4d7ldSD8-C4vaH2AJZxVnj6GU25dz4P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-146673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
👈
پزشکیان: سالن‌های همایش و استخرهای متعلق به دولت ادغام می‌شوند
🔴
در مدیریت فرایند اصلاح الگوی مصرف، دولت پیشگام است و شخصاً بر جزئیات این روند در مجموعه‌ای که مستقر هستیم، نظارت دارم.
🔴
به‌منظور افزایش بهره‌وری و صرفه‌جویی در مصرف سوخت، بیشتر سالن‌های همایش، استخرها و ساختمان‌های متعلق به دولت برای عبور از بحران تعطیل یا ادغام خواهند شد.
🔴
همچنین توسعه و تسریع در نصب پنل‌های خورشیدی سقفی در واحدهای دولتی همچون استانداری‌ها در دستور کار قرار گرفته است.
🔴
از سوی دیگر سیستم روشنایی و گرمایشی هر نهاد دولتی در فصل سرما با الگوی کاهشی کنترل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/146673" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851878f527.mp4?token=jnyKe16PrZM2oPTr9QoKLux2F54OiAnoYN3AsNBmUpbUweUn_vbs2YkPZH7C7nNC2b5daSq9d7Kplnvigy1j_0V84MZjJwei6UsNM0yHq5P4rN_xD6-qexBBrqhuhFFxntp4_3eqz5BJ_MX7K_vKDTl0il0EW_EWKA5JV65b-E1J9S2iDbN2xiJYf-c6oilyXuocOygQKTmQQH7FFLDKJZ66TF34YdgND9g65-cavKRpXyXLATXHJsbNAvHHv2s_7qbSgvJacPXv3TGoD1q0wvCsXQGJz3imCDW97AZlPFodzolnCtanu78VJw_l9sEMXZW9w4VSnVxeI6SISRe-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851878f527.mp4?token=jnyKe16PrZM2oPTr9QoKLux2F54OiAnoYN3AsNBmUpbUweUn_vbs2YkPZH7C7nNC2b5daSq9d7Kplnvigy1j_0V84MZjJwei6UsNM0yHq5P4rN_xD6-qexBBrqhuhFFxntp4_3eqz5BJ_MX7K_vKDTl0il0EW_EWKA5JV65b-E1J9S2iDbN2xiJYf-c6oilyXuocOygQKTmQQH7FFLDKJZ66TF34YdgND9g65-cavKRpXyXLATXHJsbNAvHHv2s_7qbSgvJacPXv3TGoD1q0wvCsXQGJz3imCDW97AZlPFodzolnCtanu78VJw_l9sEMXZW9w4VSnVxeI6SISRe-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: آلمان با استقرار دائمی یک تیپ زرهی جدید در لیتوانی، به امنیت متحدان کمک می‌کند.
🔴
سپاه یکم آلمان-هلند نیز مسئولیت فرماندهی جدیدی را در جناح شرقی ناتو بر عهده گرفته است.
🔴
آلمان برنامه دارد تا سال ۲۰۲۹، معادل ۳.۵ درصد از تولید ناخالص داخلی خود را صرف هزینه‌های اصلی دفاعی کند؛ یعنی بسیار زودتر از مهلت تعیین‌شده تا سال ۲۰۳۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/146672" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=pnokZPI7I8GZ_g5fUonmI0vnyKtfLhfzGbMcEYO1Fbsx6283vTx4pA0kpxJQk-hoFLjASAGYcJXPpRrjQNPc4AS176VX9KWMkW22P8TW8Nb7IJFvudCx_6Uw5ilPpfX0lGWewp1-APjRlPPWhlYheNPLDLB-HzA7VKv7LL_72XAi3g44Cka1G4kfjtvXJIk06QmBrWSmpcny7y9mWNCDvyufNfh3O9sBB5cKe93BGGUosbVUhbyuLl0ZEYo3A-8rCEVZyLzfTdoEb0t0cPvNKo8atwC5NkC3xloIsN5eXlTYBD36e6lrVBMH1NgWWGx7KRvzjFpaPPTxElAif58s_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=pnokZPI7I8GZ_g5fUonmI0vnyKtfLhfzGbMcEYO1Fbsx6283vTx4pA0kpxJQk-hoFLjASAGYcJXPpRrjQNPc4AS176VX9KWMkW22P8TW8Nb7IJFvudCx_6Uw5ilPpfX0lGWewp1-APjRlPPWhlYheNPLDLB-HzA7VKv7LL_72XAi3g44Cka1G4kfjtvXJIk06QmBrWSmpcny7y9mWNCDvyufNfh3O9sBB5cKe93BGGUosbVUhbyuLl0ZEYo3A-8rCEVZyLzfTdoEb0t0cPvNKo8atwC5NkC3xloIsN5eXlTYBD36e6lrVBMH1NgWWGx7KRvzjFpaPPTxElAif58s_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: «همه برای یکی و یکی برای همه؛ این همان شیوه‌ای است که ناتو عمل می‌کند. روسیه می‌خواهد ما را از هم جدا کند، اما ما متحد هستیم.
🔴
روسیه می‌خواهد مانع کمک ما به اوکراین شود، اما ما کمک بیشتری به اوکراین خواهیم کرد. روسیه می‌خواهد قدرتمند به نظر برسد، اما ما قوی‌تریم.
🔴
اقدامات روسیه نشانه ضعف و نشانه شکست این کشور در رسیدن به اهدافش در اوکراین است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/alonews/146671" target="_blank">📅 14:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/146670" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز
:
الجزایر تصمیم به قطع روابط دیپلماتیک با امارات متحده عربی گرفته است.
🔴
تلویزیون دولتی الجزایر اعلام کرد تمامی تلاش‌ها برای حفظ روابط دوجانبه به پایان رسیده، اما دلیل دقیق این تصمیم هنوز مشخص نیست
🔴
رسانه‌های الجزایری پیش‌تر امارات را به تلاش برای افزایش تنش‌های منطقه‌ای متهم کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146669" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/146668" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ایرباس ممکن است برای کنترل بیشتر بر تأمین قطعات، مالکیت یا کنترل مستقیم برخی شرکت‌های تأمین‌کننده را در دست بگیرد.
🔴
این تصمیم پس از سال‌ها گلوگاه در زنجیره تأمین و صنعت پیمانکاری مطرح شده؛ مشکلاتی که باعث تأخیر در تولید و عقب‌ماندن ایرباس از اهداف تحویل هواپیما شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/146667" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146666">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR4NSWiGxfjf5DqxN6-QGcWZLKvJFbMqO1vi8Yuzl3oJQkKrQayyk7AsdIk1eab_CjuSj8a5uqvrwwD6MHeDPMMEr6NCLr0Brxwm0jroT2vRQYC9JLpHZNj158sxIK4XSXy07PzgWiRYqKDkJlxmruE2MDMthVMNwTuAWAkNe3MxXpwj3jMTyOW87neUA2V2IxnObe2HF-8HDotWxJuko-Mz6TrN-qlDUNzcnBOV_C1q_M6w1DUpXW6Lr-Rozo33RNJfTRr7llnuGcC7KzuqXPanLFOfCZ4IxrI1q2A_W80wqTXCfVLtKf-rH6ewPkI7NncfDCRMntKy7AxjfIDCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به‌روزرسانی نقشه کنترل و درگیری‌ها؛ فاصله ۶۰ کیلومتری ارتش یمن تا باب‌المندب پس از تصرف المخا
🔴
بر اساس نقشه‌های جدید کنترل میدانی، پس از تسلط نیروهای ارتش یمن بر شهر بندری المخا، هم‌اکنون فاصله این نیروها تا تنگه راهبردی باب‌المندب به حدود ۶۰ کیلومتر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/146666" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نیروهای جنوبی وابسته به امارات، از ورود عناصر مرتبط با عربستان سعودی به شهرهای جنوبی جلوگیری کردند، این اقدام پس از فرار این عناصر در برابر پیشروی ارتش یمن صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/146665" target="_blank">📅 14:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان: ممکن است در برخی جا‌ها با کاهش سوخت‌رسانی مواجه شویم، لذا باید سوخت و تجهیزات گرمایشی جایگزین به آن مناطق برسند
🔴
جهت عبور از بحران، بیشتر سالن‌های همایش، استخر‌ها و ساختمان‌های متعلق به دولت تعطیل یا ادغام خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146663" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس گزارش داده در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق‌السلطی» در اردن، یک هواپیمای تهاجمی A-10C نیروی هوایی آمریکا یکی از بال‌های خود را از دست داده است.
🔴
بر اساس این گزارش، حدود ۸ فروند جنگنده F-15E نیز به‌صورت جزئی آسیب دیده‌اند.
🔴
سی‌بی‌اس افزوده جنگنده‌های F-15E آسیب‌دیده پس از بررسی و تعمیر، دوباره به خدمت بازگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146662" target="_blank">📅 13:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی خطاب به تندرو ها: انتقام رهبر رو امام زمان که ظهور کنه میگیره
🔴
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146661" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146660">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=gf4Or-blAM17oKhgwKBistQFqHgel8sK5AyppU73sTTsioCm3LBlsKvtz2XX5xilma6HSm-WoIPp51eRPnkXWNbn9_UZkRQkaRuY2PbIIHX8imiq1krPJMOiwYxmDslYeRYFKIoZV0GDkciyGhPreo27oyDdZIsSQ9Eph7ax7xvFIt95kxs4c1TXV6K98KFXbxJWehNJeIFbiCB6mTR5rIkbfIWYU6gYtGIPbImmAZM8VZolrka180JGPPQFMbPnQl8m4kceqWarMqSZJo0EekS1LvWtnlDNfSh-t9Iv9SsFy64ChgfDBLBtOYZZ3-hclxQpe6SQQl3pS8Z_oYeYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=gf4Or-blAM17oKhgwKBistQFqHgel8sK5AyppU73sTTsioCm3LBlsKvtz2XX5xilma6HSm-WoIPp51eRPnkXWNbn9_UZkRQkaRuY2PbIIHX8imiq1krPJMOiwYxmDslYeRYFKIoZV0GDkciyGhPreo27oyDdZIsSQ9Eph7ax7xvFIt95kxs4c1TXV6K98KFXbxJWehNJeIFbiCB6mTR5rIkbfIWYU6gYtGIPbImmAZM8VZolrka180JGPPQFMbPnQl8m4kceqWarMqSZJo0EekS1LvWtnlDNfSh-t9Iv9SsFy64ChgfDBLBtOYZZ3-hclxQpe6SQQl3pS8Z_oYeYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما بعد از زدن بست نابی: بانک مرکزی کشورمان ۵۰۰ میلیون تن طلا دارد
🔴
طلای موجود در بازار ایران و منازل مردم ۵۰۰ میلیون تن است!!
🔴
این درحالی است که کل طلای موجود در جهان حدود ۲۰۰ هزار تن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146660" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
👈
مخابرات اعلام کرد از ۲۰ شهریور، تعرفه خدماتش رو ۴۵ درصد گرون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146659" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وضعیت این روزای ایران خیلیامون رو به بن بست کشونده
درآمد 95 درصد مردم الان ریالیه اما قیمت همه چی به دلاره
اگر بخوایم از زندگی عقب نمونیم
و جزو اون 95 درصد مردم نباشیم چاره ای نداریم جز اینکه درآمدمون دلاری باشه
همه وارد کانال زیر بشید لینکشو گذاشتم  همه رو به درآمد دلاری میرسونه لینک کانالشو میزارم عضوش بشید
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146658" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146657">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل ،کاتز :هرگونه حمله به اسرائیل از سوی ایران، به هر دلیلی و از هر مکانی، با پاسخی قوی و بی‌سابقه مواجه خواهد شد.
🔴
پاسخ به ایران شامل تأسیسات اصلی انرژی آن خواهد بود.
🔴
این حمله‌، ایران را دهه‌ها به عقب بازمی‌گرداند و آن را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/146657" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146656">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkEzheEL3NB_4UmsmgDJpp8Z_QjZh9ZYh3BCVTSUUx2dpLJ7Br4K7XFv4ogyWfvGGMcm0HWgA105ZThDF66hYlVbPiSg0HOk7pt6oxG0ZT9mqcgrhLLZIducR0LpujQg_42Fy05kH-l_wtHr2mkdkvOfp6pHSwXQUB0AR0a4S7HqW0rIOeAt9_pb_rEJwfzKSFy0dcj1MksDdOz1Ke2VU4RTqOu1fgnfwzTwQo5ve1x9M6GHE39OKZv1onMBTVWHFd50LFMnge-tYWUcDzTAslGQXTj5RM8ZoALcWJ_YZ0x7I_UUIh6u8BNZO-I80UTSvb4QJ7r2-g36W7t4x6uTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید صادق حسینی، خبرنگار: در روزهایی که کشور درگیر جنگ و محاصره است هنوز کسانی هستند که مسئله‌شان حجاب، قطع اینترنت و تعطیلی کافه‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146656" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kku2WlFSn5ZocTA0kISoAP18N_mafS3pU1wgH4Nup5OWL2h3LSILzEGF5QtnLrkpGQYr_4qFF65eNMg7hnJwnmIqhx5acYmhQNPlXhY8LwKcgmuVASeRQK_twIc-m3ILBDV-o8pusUPaeM0T9OkEXbZXw7Z8bnXwf0GNWz8Oh6EMdtLIsj7wniv9ySV0mEGrz1Fm5pw9S31OYwKLy9y14GDFkUGeoMNnIiIB6TEhkEtyqdmPIpcVQnw4UiEpVGLwaHMjKfrIDEYMzzfpTigZeAUwW7ScJTQ1ZlA5cq9w2CgD4PgZUQX06MjheWCUU2_cV_3k4wqEJEvXRUdd5CQoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۲.۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146655" target="_blank">📅 13:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شرکت مخابرات ایران در اطلاعیه‌ای، از افزایش ۴۵ درصدی تعرفه برخی خدمات ارتباطی از ۲۰ شهریور ۱۴۰۵ خبر داد.
🔴
بر اساس ابلاغ وزارت صنعت، تعرفه مکالمه تلفن ثابت با تلفن همراه، تماس‌های همراه با همراه و پیامک تلفن همراه تعدیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/146654" target="_blank">📅 13:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79e89930c.mp4?token=PFBqZHFPqURIcKd9KgWROC4G9Eh5nuJfYKh78N32AORts6UmB-P4hm2JKjOCx9_mWBxZVJ6OYBx66LyWyCKC55RXEMYzjoOgLsRYIIJGGhbpYi-NnQdxo6OcFfRvHKMxRBQLKpfqhAQSs3mBrZe5Fhx9t5_5PIjCSH92-d2ddxWcJiQIh5Oqsp6h0E8EkxZxnbzjk83BU5xG9B9CC1n5K7wtB0zYRRYp9Dcy_IHxRITC-3-gHEhqCUsjifod3Y12ayCji3YKf8tcZY30cUnqxRHSqpsjya2eqK9yRDOqXE3CiADEs1vxxs40Eon1q0F9FDyLnabYMdUHLfA6s-AuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79e89930c.mp4?token=PFBqZHFPqURIcKd9KgWROC4G9Eh5nuJfYKh78N32AORts6UmB-P4hm2JKjOCx9_mWBxZVJ6OYBx66LyWyCKC55RXEMYzjoOgLsRYIIJGGhbpYi-NnQdxo6OcFfRvHKMxRBQLKpfqhAQSs3mBrZe5Fhx9t5_5PIjCSH92-d2ddxWcJiQIh5Oqsp6h0E8EkxZxnbzjk83BU5xG9B9CC1n5K7wtB0zYRRYp9Dcy_IHxRITC-3-gHEhqCUsjifod3Y12ayCji3YKf8tcZY30cUnqxRHSqpsjya2eqK9yRDOqXE3CiADEs1vxxs40Eon1q0F9FDyLnabYMdUHLfA6s-AuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از ورود نیروهای انصار الله (حوثی های یمن) به بندر راهبردی المخا، در استان تعز و مشرف به تنگه باب المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146653" target="_blank">📅 13:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نایب رئیس شورای امنیت روسیه، مدودف: می‌توانیم کاری کنیم از کی‌یف و تاسیسات ناتو فقط غبار هسته‌ای خاکستری باقی بماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/146652" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / هم اکنون شلیک موشک‌هایی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146651" target="_blank">📅 13:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146649">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رویترز: شمار کشتی‌هایی عبوری از تنگه هرمز در روز چهارشنبه، به ۷ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی تردد کشتی‌ها نشان می‌دهد شمار کشتی‌هایی که روز چهارشنبه از تنگه هرمز عبور کردند به ۷ فروند کاهش یافته است؛ این رقم در روز سه‌شنبه ۱۲ فروند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146649" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146648">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=JVh8smtIHcoiKFfv2No5OzS1hsD4mQI4gsleU56Y-OLA01M4uWwkgmym1Z5kf5iSZ7kHpdEhNDpy4s001Up7wXPg1OprI61mFtkGB4WpydHwQlXXYvkiKc_eGDqD2361qDZAKmd39JgEbdb5offc677UhWxjEAb6Lv-6HwBHtFfY-FM8mrhj6is3QCZIfEeAZ1EfBTCXMa7uSIBwGOsiK6WqGdZikdd3lFlwmwfV_XBe_J0X_LfANzO2fsm89rHik5yLeQalurM1u-8yai-ASg9Wkh4ilnwsAcIDgaX-JTYpwryTitaupfF7nUo8J9sW0PKVOV9T-sFeeW5KRo2_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=JVh8smtIHcoiKFfv2No5OzS1hsD4mQI4gsleU56Y-OLA01M4uWwkgmym1Z5kf5iSZ7kHpdEhNDpy4s001Up7wXPg1OprI61mFtkGB4WpydHwQlXXYvkiKc_eGDqD2361qDZAKmd39JgEbdb5offc677UhWxjEAb6Lv-6HwBHtFfY-FM8mrhj6is3QCZIfEeAZ1EfBTCXMa7uSIBwGOsiK6WqGdZikdd3lFlwmwfV_XBe_J0X_LfANzO2fsm89rHik5yLeQalurM1u-8yai-ASg9Wkh4ilnwsAcIDgaX-JTYpwryTitaupfF7nUo8J9sW0PKVOV9T-sFeeW5KRo2_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟
🔴
یعنی ۱.۳ تریلیون دلار. منتقدان می‌گویند رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند؛
🔴
معاون ترامپ: رئیس جمهور ترامپ می‌خواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146648" target="_blank">📅 12:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سردار حسن زاده : آمادۀ عملیات‌های تهاجمی برق‌آسا هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/146646" target="_blank">📅 12:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح عراق: اجازه استفاده از خاک خود را برای هدف قرار دادن سایر کشورها نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146645" target="_blank">📅 12:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=vMIlc4RStPnUI0Z7iTzkGTWa7T85JoLBjxFrnPgJJellApOgNqGQBJ-lUUB5cldpquzBkSgLnnUqfopazA06OiDRnS7CfHH_bBOcjIi3t5kL0HFSZBhrAwvV45RLeOP4g6T_YgWt7Ol1ZJDr4qaLDtqoUAuNO0PRQYj1KC115dWEiZsseFWnrduR4d81G6jRelOAJAz13uvn3NxokY4j8x4gtTj1eiB_ZovsCFsgAjCfsAbJ-MfzS6wA0IgNFcH43aati8jAqTSsETc2uTInARChLKtrsNhp4fJI8vvcRe08kyDcdRWMGO7HqaNxiunw6WP7vHpl0LWUL-MXzv4wVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=vMIlc4RStPnUI0Z7iTzkGTWa7T85JoLBjxFrnPgJJellApOgNqGQBJ-lUUB5cldpquzBkSgLnnUqfopazA06OiDRnS7CfHH_bBOcjIi3t5kL0HFSZBhrAwvV45RLeOP4g6T_YgWt7Ol1ZJDr4qaLDtqoUAuNO0PRQYj1KC115dWEiZsseFWnrduR4d81G6jRelOAJAz13uvn3NxokY4j8x4gtTj1eiB_ZovsCFsgAjCfsAbJ-MfzS6wA0IgNFcH43aati8jAqTSsETc2uTInARChLKtrsNhp4fJI8vvcRe08kyDcdRWMGO7HqaNxiunw6WP7vHpl0LWUL-MXzv4wVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
🔴
آژانس هواشناسی ژاپن همچنان سطح هشدار ۳ را برقرار کرده و محدوده‌ای به شعاع ۲ کیلومتر اطراف دهانه آتشفشان را ممنوعه اعلام کرده است.
🔴
این فوران بر جمعیت محلی و حمل‌ونقل منطقه تأثیر گذاشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146644" target="_blank">📅 12:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
قیمت نفت خام برنت به 102 دلار برای هر بشکه افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146643" target="_blank">📅 12:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706322ff6b.mp4?token=N-siwGD8T2loh5Jd68z07lOHAP51FgX5SCaOucdD7qQ5qqNweOGRerV1MA-acIV8-1NV5p5dUCctz9D4Pm67a2nFEoyXlNzlM5fgF8s1ZC4-MDweT9Ffzd-z37HXLawnDjrFq4YQ63hn65gv0WobKuWQuzGBUDfTM-74USe9R1_cfzdCCOj1W7Grvf0oMRjWfmF4UdOqA9m-QqB7RV0watHsIkfrSKo8A-5OwdbDkjtBpSJZ6EDmiV_ohnJ1fhbuG1ZMGkUglKuFVpqwfsmOneeatitgWfvAjD5KFXyWtrnF8QSPlcVhC75-UWGRbM2w82vi4YrTs4BJSbLc3Nva8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706322ff6b.mp4?token=N-siwGD8T2loh5Jd68z07lOHAP51FgX5SCaOucdD7qQ5qqNweOGRerV1MA-acIV8-1NV5p5dUCctz9D4Pm67a2nFEoyXlNzlM5fgF8s1ZC4-MDweT9Ffzd-z37HXLawnDjrFq4YQ63hn65gv0WobKuWQuzGBUDfTM-74USe9R1_cfzdCCOj1W7Grvf0oMRjWfmF4UdOqA9m-QqB7RV0watHsIkfrSKo8A-5OwdbDkjtBpSJZ6EDmiV_ohnJ1fhbuG1ZMGkUglKuFVpqwfsmOneeatitgWfvAjD5KFXyWtrnF8QSPlcVhC75-UWGRbM2w82vi4YrTs4BJSbLc3Nva8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔴
رئیس میراث فرهنگی سبزوار: این بنا سردر باشکوهی داشت که برای ثبت در فهرست آثار ملی اقدام شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146642" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ایرنا: حدود ۱۰۰ تن مرغ فاسد در مشهد، پس از فرآوری به سوسیس و کالباس تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146641" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بلومبرگ به نقل از منبع ایرانی: ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
🔴
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
🔴
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146640" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpxpfB4bzMojaFCk2Y3KKcu1AdHOIdkm81UosEpXf4gzueUwj8kYvASaduhcuRjBDdR6ujpUjicCuGWSzDatYwaIIp0xfRGs1IXTHotdO6Ff0D3yr6RvbvSUhld0CPtXsTqa0VtWqSrZO75oKomSr3GggIPN7WZfFfUczPwCTGH_lS3YRPl5jj6yH-2ldsNLww_NmUKdj6HsqJ1c05u2PexzJKyRi1YQkUCkAnSpgbXyHw9wcgLyWMePhWVviepUyOxT7PEY3gPSC9mzBMiXBzaDLCcZzXAKaQJwjtqgYgTm67CTuUwtSvSVyjnwKgc5InhbeInqYLaRFlABaihW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش CBS، حمله موشکی بالستیک ایران به پایگاه هوایی موفق‌السلطی اردن در دو روز گذشته، به چند فروند هواپیمای آمریکایی آسیب زده است.
🔴
۸ فروند F-15 دچار آسیب «جزئی» شدند. یک فروند A-10 به‌شدت آسیب دید و یکی از بال‌های خود را از دست داد.
🔴
نکته: آخرین بار که یک هواپیمای آمریکایی با عنوان «آسیب‌دیده» گزارش شد، مربوط به یک فروند E-3 Sentry در پایگاه هوایی ملک عبدالله دوم (PSAB) بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146639" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حوثی ها (انصارالله) اعلام کرد که یک پهپاد شناسایی و رزمی سعودی به نام "کرایل" را سرنگون کرده است، در حالی که این پهپاد در حال انجام فعالیت‌ در فضای هوایی استان حجه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146638" target="_blank">📅 11:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خارجه پاکستان درباره درگیری حوثی ها و عربستان سعودی: هیچ موضوعی درباره پاسخ نظامی در دست بررسی نیست.
🔴
توافق‌نامه مکه یک پیمان دفاعی است و در حال حاضر هیچ برنامه‌ای برای گسترش این توافق‌نامه وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146637" target="_blank">📅 11:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره به نقل از ونس ، معاون رئیس جمهوری آمریکا: ما ایران را از صادرات نفتی خود محروم کرده و این کشور دیگر هیچ درآمدی از بخش انرژی ندارد. ایران دیگر گزینه های زیادی پیش رو ندارد و اگر ترامپ بخواهد می توانیم با این کشور به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146636" target="_blank">📅 11:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146635">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پاکستان: در حال حاضر تصمیمی برای الحاق عضو جدیدی به «توافق مکه» گرفته نشده
🔴
ایران برای استفاده از انرژی صلح‌آمیز هسته‌ای حق مشروع دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146635" target="_blank">📅 11:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146634">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رانندگان اسنپ در اعتراض به پایین بودن کرایه‌ها، افزایش هزینه‌های فعالیت و همچنین تغییرات جدید در قیمت بنزین و نحوه تخصیص سهمیه سوخت، دست به اعتصاب زدند
🔴
در ادامه این اعتراض‌ها، اسنپ اعلام کرد به صورت علی‌الحساب مبلغ ۲۵۰۰ تومان به ازای هر سفر به رانندگان پرداخت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146634" target="_blank">📅 11:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146633">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرنگار: آیا پاییز و زمستان قطعی برق خواهیم داشت؟
🔴
وزیر نیرو: تلاش می‌کنیم کمتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146633" target="_blank">📅 11:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fb52346c.mp4?token=ILPm41Vlnv5m0HeNFktq_fiXTdbDSvlhtN6SQaOlqPwAoP-55ZUsuk59Q4UhHjmuygnxl2of9-JShBrLeJi3RsX6c7_TZbTafqHDN4byMYWzjzmlkVe04sYtPNwidIba_FcNqgz59BNX46saydUYlyfuaGoN0mgZUoO-EoXrwLR6AgV1o8chvWuJ8oBBf1Va5JGwtdg1nQryxzjkCnpAm5dKoJ3ibiDcOtorf9t3-17Mz9m36tKDlsD1OUsc8r_s8P7SuFv0C-UTXYb-mifPtWfj8vq9CixO_IwliamwIAe9W8mRzZ38HqG_i7FojLdhsjOUOggp9tpJCdsXbSEIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fb52346c.mp4?token=ILPm41Vlnv5m0HeNFktq_fiXTdbDSvlhtN6SQaOlqPwAoP-55ZUsuk59Q4UhHjmuygnxl2of9-JShBrLeJi3RsX6c7_TZbTafqHDN4byMYWzjzmlkVe04sYtPNwidIba_FcNqgz59BNX46saydUYlyfuaGoN0mgZUoO-EoXrwLR6AgV1o8chvWuJ8oBBf1Va5JGwtdg1nQryxzjkCnpAm5dKoJ3ibiDcOtorf9t3-17Mz9m36tKDlsD1OUsc8r_s8P7SuFv0C-UTXYb-mifPtWfj8vq9CixO_IwliamwIAe9W8mRzZ38HqG_i7FojLdhsjOUOggp9tpJCdsXbSEIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نسخه تاشو ایفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146630" target="_blank">📅 11:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رفیعی، نماینده مجلس: مذاکرات با کشور عمان برای رسیدن به توافق بر سر تنگه هرمز سبب شد طرح تنگه هرمز با کندی پیش رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146629" target="_blank">📅 11:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd0BfH1PnJDfWMwsPp7Qev7vZxaUqCZQOZujF1woMPGD_r5uTRUpVJu-tVZzLqChR6jj2MkJdT2eLNgw09gg1pAKZJuvYmITd83kxrKAlgztxzzMYeMFQUeu7xGKvp4hcyagv8GGmFTyl75U0_Kd1LrBTE_wK4OjBaFMNSjEiUnpqDXo0-CkVfAzX4SHXwU-KUSlQ_7il44F9VFZLlDdVj_YG03PrSfRV1lSKZ_UCJ0aWkryY2TMGok639v3YizBxQdK1D6Yy2VRU6RnX2bQrtq0wpoqyf4-wejAEDtIeFU3jHlkHu49KMJp_6ujjxx3wsINCwq3_QowyVB_Wcg5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با پول پژو ۲۰۷ به قیمت ایران، در کشورهای مختلف چه ماشینی می شود خرید؟
🔴
امارات لکسوس ۲۰۱۶
🔴
المان بی ام و سری۳
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146628" target="_blank">📅 11:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قیمت نفت ۱۰۱ دلار و ۶۰ سنت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146627" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس سازمان مدیریت بحران: تاکنون ۴۵۰۰ میلیارد تومان خسارت در مازندران برآورد شده و احتمال افزایش این رقم تا هزار میلیارد تومان دیگر وجود دارد.
🔴
جبران خسارت‌ها برای طرح در هیئت دولت پیگیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146626" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/151ae0ccb2.mp4?token=Zb_FSn5Fn-uUr0kQZFucp0E49lGs4i5tq4lycsqF6BydRICQZfe5fIZkrSK5vJSnJzRxe7nJ5naka8YldlBIo6ARSIAZyOM7Vrgd71HVHIZ_ju-XHLAtE1jojudnUThj5TZDfbCb1mJWfZYveq8Pr8v5U3BnID14PKMGrPCZ6gTLTs_XEm05uSUvoI5wmrGnrKf9MpTHQrWtWdshIjMv-eO7o1PsuF6YinW69O2hdjBHGaiuxwU2LKck5ZinxJCkLtYfN2Hc-q83NM1T4RwLafouxXTY4ZXuHL0PmMOOhedGxidspSyUWo0WHf_dhdYTUggykED4gqlSsaE_30sIa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/151ae0ccb2.mp4?token=Zb_FSn5Fn-uUr0kQZFucp0E49lGs4i5tq4lycsqF6BydRICQZfe5fIZkrSK5vJSnJzRxe7nJ5naka8YldlBIo6ARSIAZyOM7Vrgd71HVHIZ_ju-XHLAtE1jojudnUThj5TZDfbCb1mJWfZYveq8Pr8v5U3BnID14PKMGrPCZ6gTLTs_XEm05uSUvoI5wmrGnrKf9MpTHQrWtWdshIjMv-eO7o1PsuF6YinW69O2hdjBHGaiuxwU2LKck5ZinxJCkLtYfN2Hc-q83NM1T4RwLafouxXTY4ZXuHL0PmMOOhedGxidspSyUWo0WHf_dhdYTUggykED4gqlSsaE_30sIa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر ایران سلاح هسته‌ای داشت، من با رهبرشان تماس می‌گرفتم.
🔴
می‌گفتم: «آقای رهبر حال شما چطور است قربان؟ آیا کاری هست که بتوانیم برایتان انجام دهیم؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146625" target="_blank">📅 11:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paDlC2nn46ZkGYHDXgJET1SP6ScBdfskvT5JdmABTNh3EIWEUbvtTBTcyke-sFm7O0odnn7L-jKZpANkLnZfCiRlDd_HX2AHGj56zri_mCt1-Aw16mdTOO2x4BkeJ8umf0YrKmJlOQLc1fsFhMybx59odxYKFDNWwtz37XY3scjT48JvE-I_QcR-msrHVlSXhJY3cWbCyl8AG2Hqkk8M4sfiWeKTo0akxb4Vz1Fl60_sTguaVpJrlTIrkRtMXJ0ztNsHoFv05YsoaGJeqWM9DanBvrzVAXRHdZbqW91JX5Sx1xe-vz77dwaqAZIphQOhQNbXb1j3d2G1l-G-jKaLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجارهای اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146624" target="_blank">📅 11:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574dd70fc0.mp4?token=THAzCllrqIUE1wPMZIq7AOv0_eKu1Zcn8q_unKCXCcXkHeqtrGHSJFtyeZivpXWaasa8o5EkjJYoTRuKUZxD3okZAy7ol6wmsGBd3V53uPBV5AnSSrQUjC_ZLtss1Iie2J-maM8lOCwG5ThxvrPrSg0S8SggVKzR7KX3cLiCVtoxqJJb7gz5kYrRvayjTh-1Dlg6qMzUmT9zMF58MuvoV6Bp_SDReiS96hXfbxHLGCGHiXY1GPnfzVSjlkejquReDQn88dsWaMBdUE5SEx0hwC4aHw4DOJ9syK2galU31otxsKbigDl-3woZlhuZlkYVe1Z_7XcO_zLo2gCBePFLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574dd70fc0.mp4?token=THAzCllrqIUE1wPMZIq7AOv0_eKu1Zcn8q_unKCXCcXkHeqtrGHSJFtyeZivpXWaasa8o5EkjJYoTRuKUZxD3okZAy7ol6wmsGBd3V53uPBV5AnSSrQUjC_ZLtss1Iie2J-maM8lOCwG5ThxvrPrSg0S8SggVKzR7KX3cLiCVtoxqJJb7gz5kYrRvayjTh-1Dlg6qMzUmT9zMF58MuvoV6Bp_SDReiS96hXfbxHLGCGHiXY1GPnfzVSjlkejquReDQn88dsWaMBdUE5SEx0hwC4aHw4DOJ9syK2galU31otxsKbigDl-3woZlhuZlkYVe1Z_7XcO_zLo2gCBePFLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختره باباش براش یه مرسدس بنز به عنوان هدیه گرفته و پشتش نوشته خواسته هایی که شما بخاطرش تن به ازدواج میدین رو، من توی خونه بابام داشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146623" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQUFQOEINd8Ev_9b9cHzHmVLiRWacGiA9e5W7I6F_FikTY638pVmslM9UiKCAJnRlCi5-hPhu0dReEiaokGMvkhav21HyA5BcDEy9KjjaP91v9A8cL4DQcqGBBZ6FdIHriHkSVc2DRojGj7fx8QlfKtOHbsNTID6ICwtgMUc-QV_x_dKrGKq7xxnl31_PDhlYYIy3iGBYwoh5HmYzjKop5N-ocQ2T0NSoI1V-PObmWHuvfjHvDaka3roJLmcr8LJLv7NopbCE_918f1X-a0g9dDIRvz9V_5Lf62eonhWFN_83KZd-1hkv7pKfLj7QdZU2raIXBHodc0yL-zsA3HnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار ناشی از عملیات اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146622" target="_blank">📅 11:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccTePucKxhYj8Lrv10xz2VgUE5qvqiELvX0K2GCXO3bxN-hG_T64bdhWY8lnd-VxD_kxlkwzIcjSN3IM3eGmTaImTfjKSJZ9m6O322RL-A1Pi9Lx0gO_OwM0zplqnsR3Jcl7k_WYWxvRgTC1qu039KVCsU5-_WfOfKVP-hq0nrW4IKNG3ItjUfWLS7QwmniWvOgRRV-XwQM_ASpi3lXtw_B2JhN9MT3LNdymM7J-_RfwfWHA45jFNzgdAePx2jwJ19TrwivNOAW-FP334OtKkfbZ9d0FprjR1NZE46Ec3-pwRI0t6-lfASjel2COUz-O9hKwXtj4cCkp9dZPLbNq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده تصمیم گرفته است که سازمان‌های فرانسوی را از یک برنامه کمک مالی وزارت امور خارجه که از اولویت‌های دولت ترامپ در اروپا حمایت می‌کند، حذف کند. این تصمیم به دلیل نگرانی‌ها در مورد اتهامات مداخله خارجی قبل از انتخابات ریاست‌جمهوری فرانسه در سال ۲۰۲۷ اتخاذ شده است، طبق گزارش رویترز.
🔴
این برنامه، مبلغ ۱ تا ۳ میلیون دلار به گروه‌هایی که در زمینه‌هایی مانند دموکراسی، آزادی بیان، مهاجرت، سانسور و حاکمیت ملی فعالیت می‌کنند، ارائه می‌دهد.
🔴
وزارت امور خارجه اعلام کرد که این برنامه هنوز در حال بررسی است و از تایید یا رد این موضوع که آیا گروه‌های فرانسوی از این برنامه حذف شده‌اند، خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146621" target="_blank">📅 10:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
به گزارش رویترز، پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146620" target="_blank">📅 10:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146619">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO0pZtQXLnMzFdPt410RbGNSV16qQB679WJ9-kqUJPdETs0WZnj_MVd9eMOnQc-bacmbzHG-2SRvMn5bp46IHIUvw78MbXKf0bxNihCKcahvNLhL6vSJXNYqZscAxKhnsX4nrL_kBM2axqNL-CYwKk2YhMiWO71c2u_xXrcjeKU_jDudWinBxnEpWj1ApnWcsTXFxJiCO0e24nlCO5lRAVv-Ml_3ik3MCd-wq4JcvYLjIwxE_6i3BGDtDyqyRvCoJMuMhYB8wl7hmSjjWhMkn-Xa2-m6wORiCS98oG1FhLQKlVDw6K4TvIQIHLyHiVuO8kN0LkQjH0AgERkr0GApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات منابع تقریباً با نقشه اگر مخا هم تایید شده بدانیم، مناطقی که بدست نیروهای انصار الله یمن افتاده، اینطور است. جزیره زقر در سمت چپ تصویر بالا هم که مشاهده میشه طبق گزارشات مواضع نیروهای مورد حمایت سعودی چند مورد هدف حملات موشکی و پهپادی نیروهای انصار الله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146619" target="_blank">📅 10:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63e09cd5c.mp4?token=Gct6ICsXGi5dtaNBZAMnsvJhztQXEPmWMebJeSy_cfiIz-VT1wrLTOQSbnD0WOFw6Qqv7NxKUIPS0sWrfKyNUJIqpS_lMsBcEE0LWwrGemEM39Gh-z5Wz7e_JU3hhPYq3f6DNeeHZHQRk1gNbzeLTRfP-BpqpIyLlqSaiGL1gBj05nbtauVq1AgUWoUf0uyCr892sKpUlvViQfMdp5dyfkFo-3q0HVRajvvJhUte4hJZfrv2VAiGw-dTHRHAMgNsJCNqcqhNJwqi1gaODY7uFSmaQiRNNhOnbWiKxHGuI_Dcb3dZyjdoEvaS3tUMIHsgN6u8MA8JiXz6jjq9X399uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63e09cd5c.mp4?token=Gct6ICsXGi5dtaNBZAMnsvJhztQXEPmWMebJeSy_cfiIz-VT1wrLTOQSbnD0WOFw6Qqv7NxKUIPS0sWrfKyNUJIqpS_lMsBcEE0LWwrGemEM39Gh-z5Wz7e_JU3hhPYq3f6DNeeHZHQRk1gNbzeLTRfP-BpqpIyLlqSaiGL1gBj05nbtauVq1AgUWoUf0uyCr892sKpUlvViQfMdp5dyfkFo-3q0HVRajvvJhUte4hJZfrv2VAiGw-dTHRHAMgNsJCNqcqhNJwqi1gaODY7uFSmaQiRNNhOnbWiKxHGuI_Dcb3dZyjdoEvaS3tUMIHsgN6u8MA8JiXz6jjq9X399uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر لحظه رهاسازی مواد منفجره توسط یک پهپاد اسرائیلی در شهر بنی حیّان در جنوب لبنان را نشان می‌دهد؛ اقدامی که به نظر می‌رسد در آماده‌سازی برای انفجارها انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146618" target="_blank">📅 10:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIulAIxaAuL-MI_-DoGzvfy7z66jpraYRNQi4AefdWuEkZrB4fq1Nmt2wABG8-rBgkj8JiYXitK33Aa0BSh9fsMXxghWMyCGNyDTLyL0bHjLY9eTOmcHSOW8tQQOPjOQzimBtEjsx3yV-N1Znws2LvBkDUxhAId_tbyh2VcriP7gqxLeY3oF3zXRyaiJ8EOTHDoGfYXH3HgZnn8tmzj1u-YnLNHwQwh67vNnEQEZ-c7QoA1egPmSMQG5g_uJ8vgU3Ymrfwud_UArrcxjw_zUWYBQ5WbRWuAm095BQ_NywDloY2gHfC8OwPbHJwVqlCOkHmBXnwHU84P_zj5q9Gj16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توپخانه اسرائیل روستای کفرشوبا در جنوب لبنان را هدف حمله قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146617" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یک رسانه ترکیه‌ای: نیرو‌های انصارلله (حوثی ها ) شهر المخا را تصرف کردند و حدود ۲۶۰۰ کیلومتر مربع از مناطق یمن را به کنترل خود در آوردند
🔴
کنترل المخا به انصارالله اجازه می‌دهد تا از نظر جغرافیایی به تنگه باب‌المندب و مسیر‌های کشتیرانی بین‌المللی نزدیک‌تر شود
🔴
سقوط المخا به معنای از دست رفتن مهم‌ترین پایگاه نظامی و لجستیکی عربستان در سواحل غربی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146616" target="_blank">📅 10:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دونالد ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ
:
«به لطف
نیروی فضایی آمریکا
، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، محمد العزوری.
🔴
می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟ از هزاران مایل دورتر.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146615" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=TPkCd16Ghzo5I8MYVeW6SWjeoAlxBioC4va_LcsXywUxnQMMOedcqHnFkLVcIw8a5zAEwZFVFY7tdI-hJQNG9u2Pa3M3Or5pUk1mlmkkrgCLFKv6ic2x_qWxk5kTc042Fds7iQONdRMQWilYq7Vxpk_IVT4U3f_09SQwa1ngBTFaJFG6P6EUfaNZQHfEczUJjSFbsjW5BSw7Qcf56xP3BNbxZSBBZgk1EBALxB4FmeOUgdwy6-cJcrAuWc6naec0IdpJgy9wma7FVnXkZJ8rVJ-YWtel5LzyUgdWgo7oRQ9ZaYXVBTrQVyvbTIUvjEKFq098oxvF-Qn1S-0SJbeg2FmZo2PVX_nC1f4lQRLQBtxbvO3vsFsxBKl0GOT1XWwQxHgx1hZRKl_FqPQP7IHY1jpHsmx4HkXR-e9UW2fLaYYOlZatmsvUy6vwjWry-KJujacO2u0dAQJ5WFelvmeTN-OmHAti4SrOVj2wOPIfMUkfsxHnonlEAxyJW6a3CEiNW-4TyyIoG9xasUv0TXuV-TANZsVUQBRdj4s41m4MYUxP3k-IrmxRWrtVX1oo3US364tj8fwB4fOrXEUSjeo0Y6SC5KN5BYGq-LsRVxeok94bIIYLq57jeJYQhLmyBfFiNJepRMGXeNwOtFPklVqM2A3tTBXs_uAwXQBfOPsB5q4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=TPkCd16Ghzo5I8MYVeW6SWjeoAlxBioC4va_LcsXywUxnQMMOedcqHnFkLVcIw8a5zAEwZFVFY7tdI-hJQNG9u2Pa3M3Or5pUk1mlmkkrgCLFKv6ic2x_qWxk5kTc042Fds7iQONdRMQWilYq7Vxpk_IVT4U3f_09SQwa1ngBTFaJFG6P6EUfaNZQHfEczUJjSFbsjW5BSw7Qcf56xP3BNbxZSBBZgk1EBALxB4FmeOUgdwy6-cJcrAuWc6naec0IdpJgy9wma7FVnXkZJ8rVJ-YWtel5LzyUgdWgo7oRQ9ZaYXVBTrQVyvbTIUvjEKFq098oxvF-Qn1S-0SJbeg2FmZo2PVX_nC1f4lQRLQBtxbvO3vsFsxBKl0GOT1XWwQxHgx1hZRKl_FqPQP7IHY1jpHsmx4HkXR-e9UW2fLaYYOlZatmsvUy6vwjWry-KJujacO2u0dAQJ5WFelvmeTN-OmHAti4SrOVj2wOPIfMUkfsxHnonlEAxyJW6a3CEiNW-4TyyIoG9xasUv0TXuV-TANZsVUQBRdj4s41m4MYUxP3k-IrmxRWrtVX1oo3US364tj8fwB4fOrXEUSjeo0Y6SC5KN5BYGq-LsRVxeok94bIIYLq57jeJYQhLmyBfFiNJepRMGXeNwOtFPklVqM2A3tTBXs_uAwXQBfOPsB5q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «دو نکته وجود دارد. اگر من
برجام را لغو نکرده بودم
و اگر با بمب‌افکن‌های زیبای B-2 خود به تأسیسات هسته‌ای آنها حمله نکرده بودیم، آنها همین حالا سلاح هسته‌ای داشتند.
🔴
اگر آنها سلاح هسته‌ای داشتند، من با رهبر عالی ایران تماس می‌گرفتم و می‌گفتم: «آقای رهبر، حال شما چطور است؟ کاری هست که بتوانیم برای شما انجام دهیم؟»
🔴
نه اینکه مثل الان، حسابی آنها را بمباران کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146614" target="_blank">📅 10:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=ZwDfgulhr9WMcksjL5uvnCe7Aaab5ERAGnML5rIQygBSQ__P6KYEyzSaXenhkf1rGJ95gLr_hi8j86cE6G3Jn2DnztSQCJF5QTGvY_hBNDUIggALgup1dQT2RDN-tC--Mp8LXazyt2smH3jqlq5wkerhbrisedGqUHi7oFS-WatuXCZXR3jPOG_yjgPIlTq06Ez2qBEgWUJSWbDeXcUD9t2ES1rm05ZzyVQS5TXuGfMl-5EP9On2hh4ssArf0kcLC3WeA9Hfe_hSA4D2hebVEdnS-wH6o7JmE9UmrhhyoTfj2l6QOV6b-gNlYaDv3WMbJ7nL9cEPqpesMigHBvaDfyMIz2YsheeRbCHiCFG9T5HlDfOjNcyr1ouFkYiwSZTBu4n-osEPH4nBCd-BI2xCqR7RCh625dpB4d5uIg0mQB-h8qW5lW-2J2mkkPMjNxOd_2567NjUlAHj99arqUiF0mhjTQGNV2xU6ryU3p4CY6eQq5gTMb-MhFAvhnS0J-L4a_UMD68PFsTHYpR9L7vvO0bWmCXqcY9kY_6XRjeNsBS9yTx5P4_3Ddl_TBU5Ov1hDqGy5_luR5BzXNli679wixijy69deH-Swpn6RfLT8_Juj5VSBh7b46UJu-_5b4UnmFLU6-duuFRKHQ_NmKHRSUGB_E1n7EVRj0_pnxg8Rvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=ZwDfgulhr9WMcksjL5uvnCe7Aaab5ERAGnML5rIQygBSQ__P6KYEyzSaXenhkf1rGJ95gLr_hi8j86cE6G3Jn2DnztSQCJF5QTGvY_hBNDUIggALgup1dQT2RDN-tC--Mp8LXazyt2smH3jqlq5wkerhbrisedGqUHi7oFS-WatuXCZXR3jPOG_yjgPIlTq06Ez2qBEgWUJSWbDeXcUD9t2ES1rm05ZzyVQS5TXuGfMl-5EP9On2hh4ssArf0kcLC3WeA9Hfe_hSA4D2hebVEdnS-wH6o7JmE9UmrhhyoTfj2l6QOV6b-gNlYaDv3WMbJ7nL9cEPqpesMigHBvaDfyMIz2YsheeRbCHiCFG9T5HlDfOjNcyr1ouFkYiwSZTBu4n-osEPH4nBCd-BI2xCqR7RCh625dpB4d5uIg0mQB-h8qW5lW-2J2mkkPMjNxOd_2567NjUlAHj99arqUiF0mhjTQGNV2xU6ryU3p4CY6eQq5gTMb-MhFAvhnS0J-L4a_UMD68PFsTHYpR9L7vvO0bWmCXqcY9kY_6XRjeNsBS9yTx5P4_3Ddl_TBU5Ov1hDqGy5_luR5BzXNli679wixijy69deH-Swpn6RfLT8_Juj5VSBh7b46UJu-_5b4UnmFLU6-duuFRKHQ_NmKHRSUGB_E1n7EVRj0_pnxg8Rvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «فکر می‌کنم باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم.
🔴
خانم‌ها و آقایان، اعلامیه‌ای در این‌باره خواهم داشت. آن را تنگه ترامپ خواهیم نامید و مطمئنم رهبری ایران از این موضوع بسیار خوشحال خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146613" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8231bfd975.mp4?token=rlpdyzYOoYgxwOMroG3iukDnSNwDaLWnWb4kaRpjMyh92LrXAt9R3qH62TdH4gHZ3Ee0eG0uAIhg4l5VI_lvzh6DUCyI_hyVs84caa5hxvgJnnRJl7G2dqX5NiaOE3fxrUS54O_BEO6iHDw4DIKZbZYtVLHmz-6Ip7KtVvVSUtWXJv2gqwbUTCWA4qbxoRaL0tBS63JkuGH95VdAC1jWB9aBcFvRbnn4K3YZ9wk_Wxl0SePX6FLiAuRnFy4IlPzOqKIiQeSrLp_F0oRKly6LDn-Fwpo8DInFf1MowVzCibQyxcZRAuTaNQDBKihQRkLsyGEjpnf2z958-oDLHEZWXZgSccfAXETaRPJURkCFY2pcbK-iGbMP84_HsJmCSbMc1DrQZVek9VrX0_Jg6p0QwOH4thU-4wQ7ELAyOOOQsh4nLxTo57JhBY1_QHzp9S9CtRQ-IIADUMEbmqPRHz12Odj5_dqlu9aF3FXilvgQli78t1bEVmV_9_GUzVlI1u9EVlzyIU0AT4k4gSlAIPmZqIGMSbYihm_ARPd7uVXB0xuRUj_mIjYWtOf20EiSayys4ZRSrKIs-l-PeEXrLexsop1ws9UAGesB-GEUf2UO0eJOajq0152QHEj--iFtNeratKZAyEz7hCm8ixrfYQDToku3_Qo6qQ7ZWUYDG7O9Xq8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8231bfd975.mp4?token=rlpdyzYOoYgxwOMroG3iukDnSNwDaLWnWb4kaRpjMyh92LrXAt9R3qH62TdH4gHZ3Ee0eG0uAIhg4l5VI_lvzh6DUCyI_hyVs84caa5hxvgJnnRJl7G2dqX5NiaOE3fxrUS54O_BEO6iHDw4DIKZbZYtVLHmz-6Ip7KtVvVSUtWXJv2gqwbUTCWA4qbxoRaL0tBS63JkuGH95VdAC1jWB9aBcFvRbnn4K3YZ9wk_Wxl0SePX6FLiAuRnFy4IlPzOqKIiQeSrLp_F0oRKly6LDn-Fwpo8DInFf1MowVzCibQyxcZRAuTaNQDBKihQRkLsyGEjpnf2z958-oDLHEZWXZgSccfAXETaRPJURkCFY2pcbK-iGbMP84_HsJmCSbMc1DrQZVek9VrX0_Jg6p0QwOH4thU-4wQ7ELAyOOOQsh4nLxTo57JhBY1_QHzp9S9CtRQ-IIADUMEbmqPRHz12Odj5_dqlu9aF3FXilvgQli78t1bEVmV_9_GUzVlI1u9EVlzyIU0AT4k4gSlAIPmZqIGMSbYihm_ARPd7uVXB0xuRUj_mIjYWtOf20EiSayys4ZRSrKIs-l-PeEXrLexsop1ws9UAGesB-GEUf2UO0eJOajq0152QHEj--iFtNeratKZAyEz7hCm8ixrfYQDToku3_Qo6qQ7ZWUYDG7O9Xq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «نیومکزیکو؛ ما فکر می‌کنیم باید نام آن را «آمریکای جدید» (New America) بگذاریم!
🔴
مطمئنم چپ‌های افراطی این ایده را دوست ندارند، اما مردم عاشقش هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146612" target="_blank">📅 10:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/823844c7a5.mp4?token=KrsW8EPmmCPGie4Vc6EVgo5HGZIY3yQAu30KaHEBd8ZJu0DkqpFo6YSluz2r95XJYh9s5_ixdgdXr5-AxRkImMT9hgoTRTZFOtyDVgrcTcD1gj6YCyhsAa_TN7fd62TZpUigl-v6BRGC8hTWaJ2BAMSQhS-camPOiOhjzMM7Y9GqtDaXwroBZqBmE-ytdrPofi3B0FQJ94WSs0b1royBZYqX3LrQP3IpCWU8Ri0_AFHOL4qxAxZTEpXNrseMlmejixF0v52DQhDW2mi-dQ46Ir6izTc8Q3jbqrobTv0F61UmGR6KGjVG1DPhXCCcMFv8O8yM5micVYjxv7kfijzWHZcXKgjzIXs7adR8SNfimrZcYEe9d0ivXH3fs3eQhVQBhiNfaNEvU-Xo1iOpWmVMB2RUFTqMMOSjCzsBVgOOdsBjzoaIMYoVyFfs-_6Yq8TAFXxKnO1Y7gRbE4QXaqBZnD7mnv4F4J63OS0ARgmLj246eoSLtHCrZ9znntwrpeWLwpMGFgAKE7VAys3-YveDm-J2dROCO1350BPKmWZY8KWFlWzrvkDPXOxRYWUvLNIvX8eiLXWvqtJbIMYPVqlRxvHPQIV4cy5ceUz_ZOStgAd-dCcTV4dr0YU0kDfqsv_37yjus3oNZzwyLhW4TL4kIw5O9ylUdFKXESZ8wNi9LMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/823844c7a5.mp4?token=KrsW8EPmmCPGie4Vc6EVgo5HGZIY3yQAu30KaHEBd8ZJu0DkqpFo6YSluz2r95XJYh9s5_ixdgdXr5-AxRkImMT9hgoTRTZFOtyDVgrcTcD1gj6YCyhsAa_TN7fd62TZpUigl-v6BRGC8hTWaJ2BAMSQhS-camPOiOhjzMM7Y9GqtDaXwroBZqBmE-ytdrPofi3B0FQJ94WSs0b1royBZYqX3LrQP3IpCWU8Ri0_AFHOL4qxAxZTEpXNrseMlmejixF0v52DQhDW2mi-dQ46Ir6izTc8Q3jbqrobTv0F61UmGR6KGjVG1DPhXCCcMFv8O8yM5micVYjxv7kfijzWHZcXKgjzIXs7adR8SNfimrZcYEe9d0ivXH3fs3eQhVQBhiNfaNEvU-Xo1iOpWmVMB2RUFTqMMOSjCzsBVgOOdsBjzoaIMYoVyFfs-_6Yq8TAFXxKnO1Y7gRbE4QXaqBZnD7mnv4F4J63OS0ARgmLj246eoSLtHCrZ9znntwrpeWLwpMGFgAKE7VAys3-YveDm-J2dROCO1350BPKmWZY8KWFlWzrvkDPXOxRYWUvLNIvX8eiLXWvqtJbIMYPVqlRxvHPQIV4cy5ceUz_ZOStgAd-dCcTV4dr0YU0kDfqsv_37yjus3oNZzwyLhW4TL4kIw5O9ylUdFKXESZ8wNi9LMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «می‌دانید، دریاچه انتاریو را از این پس دریاچه آمریکا می‌نامیم.
🔴
کانادا واقعاً می‌خواهد با ما به توافق برسد، اما نام آن دریاچه آمریکا خواهد بود.
🔴
خب، شاید بتوانیم سراغ اقیانوس‌ها هم برویم؛ مثلاً اقیانوس آرام یا اقیانوس اطلس. فکر نمی‌کنم بتوانیم هر دو را تغییر نام دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146611" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckl5yqzZzK65NUPdKPc7TMod5uqoJ2gY486tLnZ7KrTbviFK3xwHYHH_zv55bXpLrFXbtqsojkj7WBBBUHGviqUQY2r0Vy49JKGcrdkoJG_gOox-HTOx8OAw4iHmpHYhEK9xbl_R1l9ZEDJZEtLGT8dOhKgD8mc837H0qmeIzQsqOP5Ym2XS4tosT9O0oZsJCZ9ILOf1riwwLWC7Y21C5rbVf21W4dxgAgO3uveAoiooccRre2GjC0vqFGy8T_e5XKnfc5U5FS-JkLzZzIE6veJyb3Uvr-1FdHNSBK0aZ6iIU-rMg7xPzQVt48LR3JxVPYAac-pfzhllA5oLb0amXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgD64uiyY-FyhaL95zX0SWE9w9X7ZL9urIomaFrYiFSqf6Dk7yDuhQGZkz9PtRZM5CQx2dbDNpizBggvhzV_Ba70fBgmEL7nlHM3EGFEefoFeSB1tfeIOsOqKbMqqu9U_hLfdXZo3DyCDmh3NJqX4MGmroXkqJsn-KCWvg3CeisU5ER2zXmKedyVpdn1lp2dPxESk7tBUQf6JkqA9w4-mEmrwDtBA0E0u8f5qEJeFNjw2zubWzhUqgfztaPwi2FWGGGKucyy4Yl8ABke-0ggrvBa04d5ieZKN64EiR2zKQ49hSYVdcFglQ_nJqee4nfhWi0zqd-9t7Jo1PutlqnF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujm5rhV868jGvq4MjDzTVzcqf9oaifQnsJrSJowrFCzdBncdCincfIGoyS9pkdveD0edsLsgDZWULz9r2gsTifjHCM4dSTKmnDRFgOaD3eKfD9bcf5apmKIDVeALv9vXKp26rH2CiXvqBJ2Lq7lNPQ1ntqwk3zTRkBhvfRWfRlmFhnm4txeOKsu-mamjT2zNkjQYLw-GJmcgYtvqfFpR40DuMrcINfN2WmEVKg7_L5DGxdFEvXyJVbupaFcfgE2TgkEgLDRbh_fyANQRI0H2D6KRzvDuPpzA3rmnPEsZ9l0_-T8Z8-AwOOKJ5wsKIqlphO04Yo4BIBI9l-UNZ1Ccqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اختلالات در فرودگاه جده به دلیل حمله یمنی به پایگاه فهد در طائف
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146608" target="_blank">📅 10:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع آگاه گزارش داد که ایران برای دور زدن تحریم‌های نفتی، به سازوکاری مشابه «تهاتر» (مبادله کالا با کالا) با چین روی آورده است.
🔴
به گزارش رویترز، از طریق این کانال تبادل کالا با نفت، اقلامی به ارزش میلیاردها دلار خریداری و وارد شده است.
🔴
به گفته این خبرگزاری، خریدهای ایران از چین شامل تجهیزاتی برای سامانه‌های پدافند هوایی نیز بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146607" target="_blank">📅 10:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال استریت ژورنال: تلاش‌های اخیر ایران برای هدف قرار دادن کشتی‌های جنگی آمریکایی، به موفقیت نزدیک‌تر از تلاش‌های قبلی بود، زیرا ایران از سرجنگی‌های هدایت‌شونده استفاده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146606" target="_blank">📅 09:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UECqruuRzs6jwMgA5IJwfl8AcSpdKg-blD9A4OLmexN6LhMdNSpmjr7EYPoosMI0-QbtXIwm5j0LnazS0qOXhhj6lOqQXtPxW4a7qL8gGV_yZWxwRVfAOB8xvTg56R7ESMD5VR223cuWKzdZkgMPYjHkszclZ_7J0BeY9F-Fpub7o28d-rqSidvXuV98a-DoqxLuqu7NJRnlvcXMSUJzpxiegVtOAFXa0aTmvyxu3mvPbM4LbhqmD8lnspSp-s0L0OwILVn68ZzMzP23SFusjC6n5kUVc-HmLgfqHljyy4j0VWnMx0F7snYaPGHvE4t7oDIRY9jVs6zZ0cCkPFNXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7bc0fe0c9.mp4?token=EZOd6a6Xo3ah7GlrxQy-JNW6FbmidiUWpSE1Wbf0MTbT_ZylOJv2jHGXyIssVbcW7ENA2ak6WS6p14R3DMfRDIsLo1zChr1N1dvrVWmX0joLO8_v8qihNYQHyKKOEuJlOom4WjVnvquajYls9sYbsZGLf43UKCTIWCbMy15ehrah0teei9r2hzpFcZ-5sUKCTXb2du7_Cd4DdBkI2X-BhA3nMDiWbaYPj04bJOFQghLIkKUecgynjzpgkfeTePckl055tlAqxscpOO4T4v7VOl5zQQTf8zmKJJkOwq-63UcKXp6hgTZmdymbBZEs_QgySRjWvAZ0vZi1QbOzBwpQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7bc0fe0c9.mp4?token=EZOd6a6Xo3ah7GlrxQy-JNW6FbmidiUWpSE1Wbf0MTbT_ZylOJv2jHGXyIssVbcW7ENA2ak6WS6p14R3DMfRDIsLo1zChr1N1dvrVWmX0joLO8_v8qihNYQHyKKOEuJlOom4WjVnvquajYls9sYbsZGLf43UKCTIWCbMy15ehrah0teei9r2hzpFcZ-5sUKCTXb2du7_Cd4DdBkI2X-BhA3nMDiWbaYPj04bJOFQghLIkKUecgynjzpgkfeTePckl055tlAqxscpOO4T4v7VOl5zQQTf8zmKJJkOwq-63UcKXp6hgTZmdymbBZEs_QgySRjWvAZ0vZi1QbOzBwpQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارخانه بزرگ شرکت نفتی سعودی آرامکو در شهر ابها، روز سه‌شنبه در حملات حوثی‌ها (انصارالله) آسیب جدی دید.
🔴
آسیب‌های ناشی از آتش‌سوزی در محوطه تانک‌های ذخیره نفت قابل مشاهده است و دود غلیظی از این تأسیسات به چشم می‌خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146604" target="_blank">📅 09:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: اگر جمهوری‌خواهان هم در مجلس نمایندگان و هم در سنا پیروز شوند، به دلیل موفقیت‌های اقتصادی فوق‌العاده ما، من مبلغ ۵۰۰۰ دلار به عنوان سود سهام به هر شهروند بزرگسال در ایالات متحده پرداخت خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146603" target="_blank">📅 09:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a780e6d1eb.mp4?token=PrP92CsVy_xxOyvEBdJQRszQasNGbCx083twhIVCxX_ltAl-nNXutg2dptxlGlPINZmkjcQHNERl4NzfoNfF2iyLyp5wOoAtj81y4rC6R4Ie5tGa0lmTcn6LIgcKXd1tLPMEI8TEtboy-ypvgKEVbfq-nmOYeIrSD0YlPF4IFToVnooVN4cZMqvQ0qgvg5IQyQWtiLP1b0zGFA90mMTED0p2RJrjJrmtNIuGmX1e0WW4At8nCON6WmKEoi1BTdrkxY1S4Qfy-ST8BHPxqi_QALB5mSstyeoC_6amEQv_GoIa-qpgYzbUFl2AmIi1BB-bmcitOdkM8ueCSER7GO3OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a780e6d1eb.mp4?token=PrP92CsVy_xxOyvEBdJQRszQasNGbCx083twhIVCxX_ltAl-nNXutg2dptxlGlPINZmkjcQHNERl4NzfoNfF2iyLyp5wOoAtj81y4rC6R4Ie5tGa0lmTcn6LIgcKXd1tLPMEI8TEtboy-ypvgKEVbfq-nmOYeIrSD0YlPF4IFToVnooVN4cZMqvQ0qgvg5IQyQWtiLP1b0zGFA90mMTED0p2RJrjJrmtNIuGmX1e0WW4At8nCON6WmKEoi1BTdrkxY1S4Qfy-ST8BHPxqi_QALB5mSstyeoC_6amEQv_GoIa-qpgYzbUFl2AmIi1BB-bmcitOdkM8ueCSER7GO3OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده: در طول 15 ماه کوتاه، ما از یک رئیس‌جمهوری که نمی‌توانست بیدار بماند، به یک رئیس‌جمهوری رسیده‌ایم که از خوابیدن امتناع می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146602" target="_blank">📅 09:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=PqYTD-PGTk6SgBXuBKqnTWJD9piVlhr8a2OG5Euras_eRlnWPX6o_LoD6L5mHeMPdH071jVP_ga2w956VY5TLrkJ5uHMgzK3U7uN3RHGTr3Ad-38WKKhVoJa3-I59c13wODvryEPmZczB_tA498AAzi6GblGNl_LrEZOX9igFCu5BUbuBNUL7RCeLEZzLueQ6ecZnI7TJRU0Juwp1BIJNisMlDZTB3aCJcn1FsygCdB1oJ1VCvZi0P0-lszbXlzZmWvwu96nzGIgyG4XpQqEFjluv5lMCSAvOgkpySvDdVrSa20aLf8d2btAZ-zMbnAVpVZyIrwST7ZHE1TGk90icA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=PqYTD-PGTk6SgBXuBKqnTWJD9piVlhr8a2OG5Euras_eRlnWPX6o_LoD6L5mHeMPdH071jVP_ga2w956VY5TLrkJ5uHMgzK3U7uN3RHGTr3Ad-38WKKhVoJa3-I59c13wODvryEPmZczB_tA498AAzi6GblGNl_LrEZOX9igFCu5BUbuBNUL7RCeLEZzLueQ6ecZnI7TJRU0Juwp1BIJNisMlDZTB3aCJcn1FsygCdB1oJ1VCvZi0P0-lszbXlzZmWvwu96nzGIgyG4XpQqEFjluv5lMCSAvOgkpySvDdVrSa20aLf8d2btAZ-zMbnAVpVZyIrwST7ZHE1TGk90icA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: امروز و فردا در استان‌های شمالی بارش‌ها ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146601" target="_blank">📅 09:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: ایران احتمالاً زیردریایی بدون سرنشین خودکار «Dive-LD» ساخت آمریکا را که به دست آورده، مهندسی معکوس خواهد کرد؛ اقدامی که می‌تواند دسترس به فناوری ارزشمند پهپاد‌های زیر سطحی ایالات متحده را فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146600" target="_blank">📅 09:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=Uvnm_h7KUZtqPLpF0N2LOyV3dOl_ugn2N7IT8FvujgRo5Swhq8HwqPSRP5zthUdazkjlBqcMwVAK51pEiNoy4XQr7x6PH_2-Gi1M4IkJmTd4RnxM0nE7Q2wTl4MnxgxbRlG7HW-E8734-xcfWgEH_qriKFLL-FKWz6wXDIPjO3kFW8cqQfTvvu3BSrswnwkegfyxmr9dDFYZJ2oboP46eD-uWCrBRo1L4IR-GhU9Mc2srmhI2gmK8xItWjX7HRpadbYbMBy790aoJw5LRHDmJHjB4ZtxbN3C2Fc_FcIWx561VjkDzcbXzuTtopNQSoiILA7bukMaV9VxHmbOiuuKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=Uvnm_h7KUZtqPLpF0N2LOyV3dOl_ugn2N7IT8FvujgRo5Swhq8HwqPSRP5zthUdazkjlBqcMwVAK51pEiNoy4XQr7x6PH_2-Gi1M4IkJmTd4RnxM0nE7Q2wTl4MnxgxbRlG7HW-E8734-xcfWgEH_qriKFLL-FKWz6wXDIPjO3kFW8cqQfTvvu3BSrswnwkegfyxmr9dDFYZJ2oboP46eD-uWCrBRo1L4IR-GhU9Mc2srmhI2gmK8xItWjX7HRpadbYbMBy790aoJw5LRHDmJHjB4ZtxbN3C2Fc_FcIWx561VjkDzcbXzuTtopNQSoiILA7bukMaV9VxHmbOiuuKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. منتقدان می‌گویند رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند
🔴
ونس: رئیس جمهور ترامپ می‌خواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146599" target="_blank">📅 09:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
با وجود تنش‌های بین‌المللی و جهش مقطعی قیمت انرژی در اروپا، قیمت برق در سوئیس از سال آینده ارزان‌تر می‌شود.
🔴
نهاد ناظر سوئیس از افت حدود ۴ درصدی تعرفه خانوارها به لطف سررسید قراردادهای گران دوران بحران خبر داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146598" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146597">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ ::من نمی‌دانم او (تالاریکو) دقیقاً با عبارت "ضرب و شتم گوشت" چه منظوری داشت.
🔴
او می‌خواهد "گوشت را ضرب و شتم کند"
🔴
او اخیراً دیده شده که مقدار زیادی گوشت می‌خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146597" target="_blank">📅 08:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146596">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlVyOIvXn8dCpwHBtzP2LUjtxnozDSrDbX_cn2e59sRP636-elLtYd9Ruogm_4Z8s_GfSLbURAamsMWSgj-y1kUH5EcRR1dRifplmxwjB8lbjlu1-hrhwwAx9wxpWOjLYQKqsBX6HPB2SqcXfpXDuxLC9X5Ar6jKVS46_ERLIJEkz2SBuWzu44Mzt26iFsWoXfeuNg2nWQbq8RTZlSed4KRPXkLm5bK6j0QDBZr2NgtK6qv0_BJHaJSDcewB8vA68LOUtVvRNetaX_ulloOs8J0mLR4F_bzt3o6xl7RD8-1fPpyppwXe_nouxBikqxn7caG_x6daGSNRyMq3g_RzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: جنگ ایران و آمریکا ممکن است تا سال ۲۰۲۹ ادامه پیدا کند!
🔴
مشاوران ارشد کاخ سفید در گفت‌وگوهای خصوصی به ترامپ هشدار داده‌اند که جنگ با ایران ممکن است برخلاف وعده پیروزی سریع، تا پایان دوره ریاست‌جمهوری او ادامه پیدا کند.
🔴
هم‌زمان، پنتاگون خود را برای حضور طولانی‌مدت در خاورمیانه آماده می‌کند و حدود ۵۰ هزار نیروی آمریکایی همچنان در منطقه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/146596" target="_blank">📅 08:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146595">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuzkNKD1OsJ9_-_bjQPbYC-Kmg6VN00NaEMbpZMYrzy-IT9_yDIVT_IO5ty-kxyeGJR8mYRIeEtGlnzgq7EHM7g-8yRxMQ2q7bgQzlvQ9fCV7qnap9gecizBQrCzRT2vLa14RtPCPfoZJ1-7omLAP6qUK0_3fm2Xl72kCckCnkt9K2x2-9YpXvmcnKeiVbaXDO8528cdpkWVjeohIgEpFH8X2gkh-Hm1RkEx2DvogxWbvlP_Tsg-u5pKe81Sdd2ihgANEVUaXyIUqb0an_TSM0NmTHiDiX7qZvR7HTVpciWK8RJd2Jf1C5-tG3xWdPMj44O-MtS6KrTOhsnLTf0t3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی : ‏«ارجاعِ پرونده هسته‌ای ایران به شورای امنیت سازمان ملل» با «چراغِ سبزِ شورای حکامِ آژانس بین المللی انرژی اتمی» به دنبال مشروع‌سازی یک اقدامِ خاصِ آمریکا _احتمالا در حوزه ی هسته‌ای_ علیه ایران است!
‏
🔴
کفِ این اقدام احتمالا «حمله به تاسیسات کوه کلنگ» است؛ البته « ایران» پیش‌تر به واسطه‌ها اعلام کرده بود که واکنش‌ش در مقابله با حمله به کوهِ کلنگ چیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/146595" target="_blank">📅 08:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146594">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: پاکستان هشدار عربستان درباره حوثی ها را به ایران منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/146594" target="_blank">📅 08:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146593">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8abdef8d7.mp4?token=ro-rzGgwR8PthjtyGf54Du55OFMsIpWDBtC0luMq9mV7cn4OeNiq3W9j8yh632zdQ_9gBiME1P7m7KdQwpnMrhWbm14vm_s-9zq_EoFCsdyamTtv5MkaoaMNYAFGwiP8BES7T8kbeHX4_z55JbPalesvdi7US3olMUvhT9ihUzo481dFProFVteDlSebp0QGS2XzvhAJtkml-J-6WtdQ4wIgI-1KZDzINIhU2US-GtRWmk4CAwn3ExSvSeLH_3SfXQVvIJ6meNeaB3XrfamS6vfuRilhP6xlYU2VrVbSSnGIUZRgDEuyFBzMXrIHzYlcEKW8kII5TM8VoBhHcLHMRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8abdef8d7.mp4?token=ro-rzGgwR8PthjtyGf54Du55OFMsIpWDBtC0luMq9mV7cn4OeNiq3W9j8yh632zdQ_9gBiME1P7m7KdQwpnMrhWbm14vm_s-9zq_EoFCsdyamTtv5MkaoaMNYAFGwiP8BES7T8kbeHX4_z55JbPalesvdi7US3olMUvhT9ihUzo481dFProFVteDlSebp0QGS2XzvhAJtkml-J-6WtdQ4wIgI-1KZDzINIhU2US-GtRWmk4CAwn3ExSvSeLH_3SfXQVvIJ6meNeaB3XrfamS6vfuRilhP6xlYU2VrVbSSnGIUZRgDEuyFBzMXrIHzYlcEKW8kII5TM8VoBhHcLHMRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پارکینگ های شمال بعد از سیل!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146593" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3Uz_uub4-Tk4IVMNThe3zaVJo8oMkUnyTiWLhACV_oEeU76TA2aoXnoy7VqGXEEAO2njf7iiwQ-RaQkKV33avKsScDyqWfLH6ef-ShsoIBiyXAirQtLSTIKFCy29woaXvpLlDfxTaa3RduXLo0hILeK4vCQVEmxQhOOU6UKQu2nl-XKhJRBnmWFc_3PI9tcQkXF3pR-u0oZKzxoZ-PgefKWBNlIaeR4RmKxdiUOj1XUiLiVmIa_qOOHu2m_g-qntnaBq-ZIosdZn3oubi9Ed92pipUKrC3ggNvKehIzV6UUw1Qo3XP-9j_m1hIx27L7Jjs-ufO9PQCDyxOIIcPHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVkTy5mb17cN0jakpw4bgUYg9dQkI3_wue_xlyNFY646GrpzPvwvAZn23O-ExtRcEJ0xeqZvQav3H3QrOXv8UEQmOEQYXQT21Xfpkd5Jhaxs7kmTL2ngk7EG61-1w5V2gTCPV6S34YExPkOrVi689rlAurBXrpZYmQ7LYnGqWPHLQS0vclhWDkDcURb5pSuqJvu6UxiP4nepi_YayAmBAC7AuH04sRXo-INkLA9ywZb4yidjweogk2BGDccqe9Xnwml2G9342M9ru-LwhGk-JLjtVk-dGrSJLWc-icLh8Fa7S8tSP6FygMrr6VSiZ2Y_W8GvkvreX6y-um_vuEajUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصرف شهر الخوخه توسط نیروهای حوثی یمن
🔴
گزارش‌ها حاکی است نیروهای حوثی یمن شهر «الخوخه» را به کنترل خود درآورده‌اند.
🔴
در صورت تأیید، این تحول می‌تواند به معنای تغییر مهمی در خطوط نبرد در ساحل غربی یمن باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/146591" target="_blank">📅 07:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: در جنگ با ایران پیروز هستیم و تنگه هرمز را در دست داریم‌‌
🔴
ما تنگه هرمز را کنترل می کنیم و فکر می کنم باید آن را تنگه ترامپ بنامیم‌‌
🔴
ایران در حال فروپاشی است. ده‌ها سال است که قلدر در خاورمیانه بوده و اکنون دیگر چنین نیست‌‌
🔴
اجازه نمی دهیم ایران سلاح هسته ای داشته باشد و آنها امیدوارند در صورت شکست در انتخابات با دموکرات های ضعیف برخورد کنند
🔴
ممکن است مجبور شویم پس از نظارت بر برخی حرکات به کوه کلنگ حمله کنیم‌‌
🔴
ما دقیقاً می دانیم که در کوه کلنگ چه اتفاقی می افتد و برخی از فعالیت ها را در سایت زیر نظر گرفته ایم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/146590" target="_blank">📅 07:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw1WCLPq2J44TRTe9MTO7HZNNgRZTvFcMtjKjRh1b6mxFwBhpDA076Il1IRIDnljoMUN8REnrOdQK2XCZDD65p21PYRoYZsr5xKPRBR0FYMHPjYbVOdBmvrE62vzDSv_usBoMmTUnoJGSeMkx2wrlIuE9f9ix5k_2nAliywDPvsPgt_LSW7Br1RCqcS1hcEGDsCuFrkjG-8pn7ZUVOCe-Fdy2XOgs9kIj5p132RYK0j0wL6rknRGCCh1-l9gEIcjlrOPrUwH2uqkqBtuesDFd33VKmngH4txgLSApMPcUC7GMT8RDvBdXuvhmyd6POISdc3Gsso1vKUfzPrLkejbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/146589" target="_blank">📅 01:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz6VKClpvPOca9JSzC8ECX7GYSGn43qzu0xXhadJbP3vx37bEIJi7VSOcrW7HK-sn7Wbwy1d4uOwyQf1PcA6gh4W19KuD9afZFCEQb_T1ZhjzvPJwMXS0JwbU9busMfvCp5iZJEoLBJCu6gP0Q5-GEzEjngkoYEvJcMohqIK1aqc5WLoMeivXABS6CrSbcMcXUNj0_5FZ97Jpx3Z2JsLrAv9QvPDvlIP5-Co5OPsUrDtQCCalGf6KZQ3ncXf0SBSU1j518KHQIrHymbTckYWzPVOo5ijlXRRWp9KKOW_pFuWpHKWAL1PbbrTb39XYGT5JccEThEmOvWpFdk8iCntug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
رویترز خبر داده که پاکستان پیام هشدار عربستان سعودی را به ایران منتقل کرده و از تهران خواسته برای جلوگیری از بحران منطقه‌ای، جلوی حملات حوثی‌ها را بگیرد، درحالی که بقایی اعلام کرده ایران کنترلی بر حوثی ها ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/146588" target="_blank">📅 01:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdjW81TnJLmQ9ZbLUMvasxyjAmeuck5oA4220SSwBHXjF4BLx8FjaumWIyvnvbD8wtQglvhHXZvDVlMgiEN_UnD_nDJfQm9j40KinhWe4c1UkQjY1GWFGDfd-0Cp6NfeYfBxMJA94kPEK9-bxneVeeXeNtNNebw_BY3Twi7WvILEiMDC8JC20PpCtIjt3Iy9cNNaOxXdy8wZ2WXY_mfT91XT0tpU02RT42465QLztMbpQ9KaUb3EBums_VxGu40xZUG9VCgUE5Yk--IkWenkCpNMxHA-FdMyfcZG0QKMwg7xLDRlbvKFu2F_ZRz-34Q3H960YOOOa5ME-aXlh9w-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال شدن آژیر های هشدار حمله موشکی در نوار مرزی اسرائیل و لبنان، بدنبال حملات احتمالی از سوی حزب‌الله لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/146587" target="_blank">📅 01:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e357503b1.mp4?token=k-h1iIZqHuRvDK7pcvHYYl-HYpWsIOD4PGvczHuKOqM0q7d9aX64axlIAlAs5yGRNEdyS2G-ktL0G_h_n0pVmTPdWasGtfvRdalrApp6rjfJF4YQPE-whh5jxHfM1N3g6P7H5cb0P4HjezWREm1NtFbaip6lzADOwP3RNZyt3ZwHSVXmOmJlz8Opf4tO93dJO7Iggg8rw2CCIed5O9r8LMzW1efD47OIViEjGUs3jQOU21WRtdUOHZ6pY_oknYfwHrOKGevg1WhiGGzB7p31F2U8kJXaiynLBB0iDYGzNBOSIBlOJ4SnaSiDZkvE4N37H8VhN4220KtIApb9-DQcSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e357503b1.mp4?token=k-h1iIZqHuRvDK7pcvHYYl-HYpWsIOD4PGvczHuKOqM0q7d9aX64axlIAlAs5yGRNEdyS2G-ktL0G_h_n0pVmTPdWasGtfvRdalrApp6rjfJF4YQPE-whh5jxHfM1N3g6P7H5cb0P4HjezWREm1NtFbaip6lzADOwP3RNZyt3ZwHSVXmOmJlz8Opf4tO93dJO7Iggg8rw2CCIed5O9r8LMzW1efD47OIViEjGUs3jQOU21WRtdUOHZ6pY_oknYfwHrOKGevg1WhiGGzB7p31F2U8kJXaiynLBB0iDYGzNBOSIBlOJ4SnaSiDZkvE4N37H8VhN4220KtIApb9-DQcSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای آمریکایی در آسمان اردن در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/146586" target="_blank">📅 01:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed07c7137.mp4?token=QEK6w75ASKmuaPbhx3Jcgf1cvEfnLLirJSga1oLzf618-bIQ5k8lGk2EeNxCAnt22PqwSOxOlEsYtxRZFejT_uDeP-exU8E6epVlQbfu8m0HyNpsZCcM7j7yIypNvVOcNb2-FoY-E4TaTUZGqj3D2yQjksPwQixp_zftfni6wVrzcVWXok0PbbcHTyhqDF2rzGlfBEzw0Uvc8C1MT2Ps5iO5p0JY6lmMHk3NFG18UKIvyMR5DAS2eikJ61H-GfBicUksNDM1wzA2g4WNNeI7gvZAZ9Vv1UHF4s1zp6U-DXq5eaYQYQQ4FEpwAfEysqwkPhwbRlGYxJa8dgTyCdtvN66pyHnDUAzzLjkg-l4FZi0iCIHGh9ekK38wtFRuQfNnKHABsonHb7FEAKJoXmwLU99tQsTRZYIoHz3gbgY-COav0OWgbL-dHuSNL3pYdx5GVi2PIJOllE_ftumO5LJi2wTTyROkQCRajpXtpdchmiSQxUPptdDlTBAYbUmnFQXC5-L2cULo2-BVjdeYuM36kMLRPlZ8GrPw9-HvQ8etoA1UXqFc2Mqa9ieKz-CntXkCwyduRzNLSRDVC0EHzue4J2UOFVEUk9VJclW4N5iWf6CUEQLa6nIuUZ5fAWSc8DeeHJ6299dOQOaHnBdc_oT1RhIn74cj9XTIVa9pdt1wP7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed07c7137.mp4?token=QEK6w75ASKmuaPbhx3Jcgf1cvEfnLLirJSga1oLzf618-bIQ5k8lGk2EeNxCAnt22PqwSOxOlEsYtxRZFejT_uDeP-exU8E6epVlQbfu8m0HyNpsZCcM7j7yIypNvVOcNb2-FoY-E4TaTUZGqj3D2yQjksPwQixp_zftfni6wVrzcVWXok0PbbcHTyhqDF2rzGlfBEzw0Uvc8C1MT2Ps5iO5p0JY6lmMHk3NFG18UKIvyMR5DAS2eikJ61H-GfBicUksNDM1wzA2g4WNNeI7gvZAZ9Vv1UHF4s1zp6U-DXq5eaYQYQQ4FEpwAfEysqwkPhwbRlGYxJa8dgTyCdtvN66pyHnDUAzzLjkg-l4FZi0iCIHGh9ekK38wtFRuQfNnKHABsonHb7FEAKJoXmwLU99tQsTRZYIoHz3gbgY-COav0OWgbL-dHuSNL3pYdx5GVi2PIJOllE_ftumO5LJi2wTTyROkQCRajpXtpdchmiSQxUPptdDlTBAYbUmnFQXC5-L2cULo2-BVjdeYuM36kMLRPlZ8GrPw9-HvQ8etoA1UXqFc2Mqa9ieKz-CntXkCwyduRzNLSRDVC0EHzue4J2UOFVEUk9VJclW4N5iWf6CUEQLa6nIuUZ5fAWSc8DeeHJ6299dOQOaHnBdc_oT1RhIn74cj9XTIVa9pdt1wP7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست ترامپ در تروث‌سوشال: این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
🔴
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/146585" target="_blank">📅 01:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شایعه مرگ زلنسکی تکذیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/146584" target="_blank">📅 00:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هم اکنون زلزله ۴.۵ ریشتری اطراف بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/146583" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوووووری/چند انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/146582" target="_blank">📅 00:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/نیروی دریایی سپاه موشک‌های کروز ضدکشتی را از منطقه سیریک به سمت تنگه هرمز شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/146580" target="_blank">📅 00:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/146578" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/146577" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tcDmOo9v0OsONC9qW4kQ5Sp32w-QcrpZ9518wK29ncoTWPq6Z2w0oLMTgndyH1PD0tPjqaU1NNj1Bg_ozW0bEvPxtsFT3bD8Fc9P7BjxVk5qOUXcX2Z8j9go9bmBK6OHmcuzzirTrWT_6lMj-Se1w0rM1aO-_d-Qr981nJcxKchxDxa8iRSAD-bmT-kB9NZPdEZyGxSM8MLM6z7M1tgRfcUmf4SQSvOhUsOujF4zHQAneLMzBmCqwKp_4tHucjudxbZ9S-vumSSVtVkZE3Hdvj2KkWKX7dYsw7oSgEYbqTv6vViFAUOLn9QnShq0Dms9DWqLpypN9IW1cyeiTuMx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام رسمی اپل، میتونین آیفون 18 رو با اقساط ماهانه 35 دلار ( 8 میلیون تومن) خریداری کنید.
البته تو خارج، ایران نمیشه
🖤
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/146576" target="_blank">📅 00:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUESRie_y2WRwpy6PgDucz38EpVdVmGgPkn6CGrLgJR1PhNMxPSPNCXNJC8JGBVMCCwHTV36zf6rA0OC25nqceDIpNE4I0dStIm42kXN7yO1oCQe9xahaSaYJ_cH4IShdL9HPUValyXleslJmgz7xs2yvTlZa96JsNT_aX69zV4ui0AKu7IwP9ANvVBgtmkyNv-Zc5q-6JeuxW9oGNJzsMUsnigAVrEwjAVABY-GDBt9O15lfkZ4ujogim33sKnbIfgX8j0x4HSNkyHHfLyvvdWMVCYucIPF_OxmE6iiQIEKoddTDbH4Tfw8fReG4DIBlm-tCRyfJy5wWGZzWzJu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزشی‌ها که مدعی جمعیت میلیونی هستن خودشونو پاره کردن و تونستن برا محاکمه روحانی فقط ۳۵۰هزار رای جمع کنن
🤣
😂
😂
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/146575" target="_blank">📅 00:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146573">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eba47e74.mp4?token=dLAZf6vM0S-QBoZ6NV9jKvyHoEYAbD4wfXTgaQmc8r36ut5cd4eqkLy2h_SUkKDC8ti1p9wbZPvg5tQ40DtBPXtgSJHvSnWFguW0GKM5mw5fv1jaPBJEG6Kgz87vc7fgu6UUoHPZtfIXhJlc_XhTLnrKKsoDZPf1SvKXCksCxi1dCRGx8l0ypupXTkJqtq2Pzukyqkj-yQsYDI0WK-xvGrth93x3h8_5wnNKMlaUe3lW8VJG7-hbDAhfD8YIq0W9fWG9nhByTrzECq7RDR4V-1F2Z-X9UP4qdu51L4oYWv5gcYUvr5Bx6Qodq2IU1-BFBBR0QSjw3ewVtyUI_Pc17IIJg8Sr6u4UD8DL4odlUf_jFrkJRnCMeiNVuR0HK4pggFAhPJC7Tk7-QrgdbtT9TRA16Hgn9UzivuJVSd04NjThWDLZiE_HFJEdA3ugzHgiF6mm1imhCZSOcRVuW0DrGkTE4P5y708BXj6Gc-7Lg-oLZyZsuyJS9UkMhXV_X1l-CHahfgJcdxB9FZvq-HCOxehBhaPx6kxiRFUknXbCTyhGiC3e1f9C0u8KCUq0pMTstSD2NEJoDeTS7IItsjUltxEuPa8bzREuIzy4rEFPlBU3aABW3MmrvRBSDLr7TfXS5qxTRczNYGK81erfLF1LI7NadjptxWRK6Y8OEYzeNNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eba47e74.mp4?token=dLAZf6vM0S-QBoZ6NV9jKvyHoEYAbD4wfXTgaQmc8r36ut5cd4eqkLy2h_SUkKDC8ti1p9wbZPvg5tQ40DtBPXtgSJHvSnWFguW0GKM5mw5fv1jaPBJEG6Kgz87vc7fgu6UUoHPZtfIXhJlc_XhTLnrKKsoDZPf1SvKXCksCxi1dCRGx8l0ypupXTkJqtq2Pzukyqkj-yQsYDI0WK-xvGrth93x3h8_5wnNKMlaUe3lW8VJG7-hbDAhfD8YIq0W9fWG9nhByTrzECq7RDR4V-1F2Z-X9UP4qdu51L4oYWv5gcYUvr5Bx6Qodq2IU1-BFBBR0QSjw3ewVtyUI_Pc17IIJg8Sr6u4UD8DL4odlUf_jFrkJRnCMeiNVuR0HK4pggFAhPJC7Tk7-QrgdbtT9TRA16Hgn9UzivuJVSd04NjThWDLZiE_HFJEdA3ugzHgiF6mm1imhCZSOcRVuW0DrGkTE4P5y708BXj6Gc-7Lg-oLZyZsuyJS9UkMhXV_X1l-CHahfgJcdxB9FZvq-HCOxehBhaPx6kxiRFUknXbCTyhGiC3e1f9C0u8KCUq0pMTstSD2NEJoDeTS7IItsjUltxEuPa8bzREuIzy4rEFPlBU3aABW3MmrvRBSDLr7TfXS5qxTRczNYGK81erfLF1LI7NadjptxWRK6Y8OEYzeNNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب عجیب محسن افشانی در پخش زنده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/146573" target="_blank">📅 00:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0a519258.mp4?token=RwnAll7OufWR5IjhxmMocL0z_ilCShCeyJzWbNcS_N0Rxg2Jd75VIxL5QYun-ErAu6v8fGZTgYLXeUoZkjiNfNLM9woP8GcSHZFK_c1WHykE-63X1-sxr2NqyRHv0gT7i7WBqpLUvDH_Gef56BhMfb696NiKAoVSz6yhp6a6DgGynOTXdu4wkmkW7VPiwl07Ikl4mCLx1gyzkrwIP-P2Ukgfl1YbRxdAPUky-f25VTWWadoDFZYsMMrcK7NusT8PbTf_-7BOCnDcLr1M3ll6NALvhdR2AskF6rIiFx6moAaj0E-h1iUbXDW65qo8CLydWbP-M8hK16Oxos8KMy_g41EhBkVGBoIMnuamTSdEd4bgPuUVfkCWn-WiDbAuyVUjImc7FHtnz6VkYtTaUxcB8QM2GUJfwZEJlui1AmrW9pBAzWJotcc-k_0VaXrzceVBlur9qCDP0VrINTveoklv45wr_sgBa4_ztM1vH6--Zcyhq9-dxVPWuzi3QMZM6ThIZFu1e2J16PSqUX-4QLwUE67cSniESZSWI3Z6QSRTM6v6UdcNMWmm-pUWpyWDTxT01Uh3EWy-lxCd4MAI77Ch38KO0gvVcYQdE27xdSUZIkvMqygYXorzbseV_bBDgoM09sIVAK5ptpYcBauUp5mXUwzpEoudfdOoFKD4TS3vpHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0a519258.mp4?token=RwnAll7OufWR5IjhxmMocL0z_ilCShCeyJzWbNcS_N0Rxg2Jd75VIxL5QYun-ErAu6v8fGZTgYLXeUoZkjiNfNLM9woP8GcSHZFK_c1WHykE-63X1-sxr2NqyRHv0gT7i7WBqpLUvDH_Gef56BhMfb696NiKAoVSz6yhp6a6DgGynOTXdu4wkmkW7VPiwl07Ikl4mCLx1gyzkrwIP-P2Ukgfl1YbRxdAPUky-f25VTWWadoDFZYsMMrcK7NusT8PbTf_-7BOCnDcLr1M3ll6NALvhdR2AskF6rIiFx6moAaj0E-h1iUbXDW65qo8CLydWbP-M8hK16Oxos8KMy_g41EhBkVGBoIMnuamTSdEd4bgPuUVfkCWn-WiDbAuyVUjImc7FHtnz6VkYtTaUxcB8QM2GUJfwZEJlui1AmrW9pBAzWJotcc-k_0VaXrzceVBlur9qCDP0VrINTveoklv45wr_sgBa4_ztM1vH6--Zcyhq9-dxVPWuzi3QMZM6ThIZFu1e2J16PSqUX-4QLwUE67cSniESZSWI3Z6QSRTM6v6UdcNMWmm-pUWpyWDTxT01Uh3EWy-lxCd4MAI77Ch38KO0gvVcYQdE27xdSUZIkvMqygYXorzbseV_bBDgoM09sIVAK5ptpYcBauUp5mXUwzpEoudfdOoFKD4TS3vpHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه، درباره کشورهای کمک‌کننده به ایران
:
ما معتقد نیستیم که کسی چیزی به ایران بدهد که پویایی‌ها یا پارامترهای آنچه را که مشاهده می‌کنیم تغییر دهد.
🔴
در نهایت، آن‌ها همچنان به کشتی‌های دریایی شلیک می‌کنند و وقتی به کشتی‌های دریایی ما شلیک می‌کنند، در کشتی‌های تانکر قیمت پرداخت می‌کنند. آن‌ها به کشتی‌های ما اصابت نمی‌کنند، اما پنج تانکر را از دست می‌دهند.
🔴
آن‌ها دیشب پنج تانکر دیگر را از دست دادند. چهار مورد آسیب دیدند. یکی غرق شد.
🔴
آن‌ها به دلیل این کار همچنان قیمت پرداخت خواهند کرد. در همین حال، ما ادامه خواهیم داد که آن‌ها را از نظر اقتصادی خفه کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/146572" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
خبرگزاری CNN: آمریکا قصد داره تاسیسات هسته ای زیرزمینی ایران رو بمباران کنه و داره برای اینکار برنامه ریزی میکنه.
🔴
آمریکا داره یه بمب سنگرشکن جدید برای اینکار تولید میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/146571" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فایننشال تایمز: ایران برای دور زدن تحریم‌ها به رمزارز روی آورده
👈
نزدیک به ۱۰ میلیارد دلار رمزارز در سال ۲۰۲۵ از مسیر ایران جابه‌جا شده
🔴
همچنین ایران طی سال‌های گذشته توانسته از طریق استخراج بیت‌کوین نیز رمزارز به دست آورد؛ ۴.۵ درصد از کل استخراج بیت‌کوین جهان در ایران انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/146570" target="_blank">📅 23:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146569">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoljCV0QJXG8wMqNIvvQr_ywtGxo3t4KVk8BImfLvSaDsf_JwxwzxrmY3PVM4BcD7M3rX_vlH5w2DSFa3JS_C6JC44fSYWCClYfYRxyv5DWYMuUjAOhRuIE6SmfbdRGrQEo6lUtZRqlRFNmefZfJZgFnoFqtSwjP4nPgNA9Zkwl18B-rrLI-v0auaMrprRy5JumJr_0D_WSvJt6A_Ktdv_am6uuGzq8VeoLjj5W5aO8cxrTL_93nZHTdpEmOYAujQjx3thhpxcx6R7Srsw0svCNuZlceoH6nR2VDViS8t1ES-lIsXYvcm0h-2sVroaPFSr4QnZIMenyLLqKMIag4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع یمنی از ترور وزیر دفاع  به همراه شماری از فرماندهان انصارالله در حمله هوایی به محل نشست آن‌ها در غرب تعز خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/146569" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146568">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuxz8owejXkpPcoYH1gItuyKcNW1gyNH7k5uwqyZsZLH3gjL8_6-XmfoZC4ApI0_7kN3spF1sEsics6yOaSO7ttRkaCP_FLKsCEjzsW55MvudwgfmRh5oPkltDSc6ymtUCTCh9t9yoGyeiGndf3nHsFvzioPxE8arxp10Gj4prRT_Dw26llNg_bVXB2T_mn0pMG6fESULgCU6RNuVHT6XiZ0mNHRkz2nDBPpTWIdMBzlW6nKPSadub1_XLelwySp87JRAcd3tNn7QGl3SsvSuj8sW2Hzq8SlZuyGE-2s7DT1YG9IbHc7NB58dpScDLl4c2Z6PRljuShKEGbjvGgkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نکته قابل توجه در مراسم امشب اپل٬ حضور مریم عظیمی به عنوان یکی از ارائه دهندگان بود.
🔴
عظیمی از ۵ سال پیش به عنوان مهندس در بخش توسعه دوربین آیفون‌های اپل فعالیت می‌کندو امشب در این رویداد درباره قابلیت‌های فنی جدید دوربین آیفون ۱۸ صحبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/146568" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146567">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
توپخانه اسرائیلی به ارتفاعات الدبشه در جنوب لبنان حمله توپخانه‌ای انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/146567" target="_blank">📅 22:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW8CQGnYoB5CcjwE6q3yYYGHgjUfMWHZV9pnt03oMOJyDD0yWtlNQ89FstLFZ7shVzHPNm2iuEu1PX1-ciL79qNYJ_PiKlKjrTYq1cw_kInamnDI6VAQ6yx84SKl7RGBNLYIBd6m_iL5aW683iAqaABk2SLiHC6Fea07VdtojigArjHuYtUqZWSyjRRh-C1Jr4ZmkABJGm-5u8F7zCriNcR-4B-R28BCKWNcMMZZAtTtmtEL2aIsBFlSfO3P_ghaI9G1U738MhioqC2V6rEaTY9gDtIolwsfhT6eR8ICr3f_afuEwJflcAJtbOpayZvI5P2DPRXygigHzydM3Zw7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی به قنطره در جنوب لبنان رو هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/146566" target="_blank">📅 22:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6lruArkGLcgTHJeQHubGpiQAXuW1dRj5NO8XJF6H7SMe1PE8NALcc5Tavjs4Y9xZIwuZ2i_6e3p-C-BhY9DXSisD852aQXhJglTioCgfZTfRtQCKxW1FAmjs-QEdqhGMjSZLLJqkh7LXHhiZXJARcmSJNs8m7pN7h0ADsRo2OE3x0jyGR5fgX_fZcf1pRjev0-8VA6PDUbCUtZBt1AnmCbgC6NWYfekbSiUean74YwnuY9D30mh9fHWYedshzkZgEi2K0Yg-MqKgys5B56qgu4mCYiZ0Z9SadAumjSsQ_NnMJjVvdJc1LGYejTB_lzXKp5TETncmuPfOIvjoVRiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی
:
نیروی دریایی جمهوری اسلامی پیامی روشن فرستاد: امنیت و ثبات خلیج فارس توسط ایران مدیریت می‌شود.
🔴
به نیروهای باقی‌مانده: آنچه از تجهیزات‌تان باقی مانده را نجات دهید و در حالی که هنوز می‌توانید به خانه برگردید و بر دفاع از مرزهای خودتان تمرکز کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/146565" target="_blank">📅 22:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B1IeNF100KWnnttii9LPryirV-My3aRpB9feV0fLpY3JyGB4t7DgbqaB7Socj15OWyFyH7C6B2z-cIJErKJk2g4M021-vdbNzPyc68Uo9k5QyG2RD8wmLD0wdXdhsh7DoPCl8tpBlTcVwbM4r887-YodrxTN3D18SPaf1teziKgpv0oqoP_2anMMwi1XdCpUjpv9Ym4or2CT4nvN88kA6IFt8-yJMH9-NYVRx2iTvHFXFkkcjWbmCCTW8Y8OmFcm8SlrJinUX2us0A6k3opO1hyhNV7UChpckc9ssb71z3qxQYPuWtJJAaVsw7g4ord6FvO3sO3wufNSsFyJvm4eHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جو ویلسون، نماینده جمهوری‌خواه: ائتلاف دفاعی مکه اعلام کرده است که حمله به یک کشور، به منزله حمله به همه است. اکنون زمان آن است که ترکیه، پاکستان و عربستان سعودی، حوثی‌ها را نابود کنند. یمن آزاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/146564" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccdf5d3613.mp4?token=dZDGMyKN23Pf_aqm2BMQeLjHdqY0K5mSr2Lw5Y0q5ewG72lNE2CFRsFbEhfv_affs4faaEbwtB2fwO6jxfURkbZV63j17MlMKib56E9L1U3_ELsO8WBu3cZ1KbX2Q43JWWNP-bi_qfEntw1R8UYMJv7IjoTGct06WaeZTsTN2bOio-gbsB6V2nUJbeSORVdOe9PsrhRPEg8rbiPVCDCJ5K7Sa1HWdcOPlvt_u2ruNN4RP1N3DFeeTHbAlUkHmYiNzpJ67VzdERYDVNqH-L2QHjIj8oYA1kJovVWfVvPl1o0xjj24vgcwhLBJZ5lPazYYW3Die_Jch2Ep2x7E5RR8szzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccdf5d3613.mp4?token=dZDGMyKN23Pf_aqm2BMQeLjHdqY0K5mSr2Lw5Y0q5ewG72lNE2CFRsFbEhfv_affs4faaEbwtB2fwO6jxfURkbZV63j17MlMKib56E9L1U3_ELsO8WBu3cZ1KbX2Q43JWWNP-bi_qfEntw1R8UYMJv7IjoTGct06WaeZTsTN2bOio-gbsB6V2nUJbeSORVdOe9PsrhRPEg8rbiPVCDCJ5K7Sa1HWdcOPlvt_u2ruNN4RP1N3DFeeTHbAlUkHmYiNzpJ67VzdERYDVNqH-L2QHjIj8oYA1kJovVWfVvPl1o0xjj24vgcwhLBJZ5lPazYYW3Die_Jch2Ep2x7E5RR8szzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
:
مشکل در رابطه با روسیه و اوکراین چیست؟
🔴
ترامپ
:
مشکل این است که این دو نفر (پوتین و زلنسکی) از هم متنفرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/146563" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سفیر پاکستان در روسیه گفت: با وجود تشدید اخیر تنش‌ها در منطقه، ما معتقدیم که به‌زودی تفاهم بهتری بین ایالات متحده و ایران حاصل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/146562" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
