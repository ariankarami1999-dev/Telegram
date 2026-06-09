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
<img src="https://cdn4.telesco.pe/file/g0jgodk10PvjCbzUN4NoF8m_-zym-0VKbx_QLzeNHW70AvJvMNrDJO8wiCTA9V5Q2OtZ8x0QuVP5hnx3_ymo9iG-TcBSpzDCGhwxw3yAD6LG4dAtF-HyI_lRPt1clLWGS2cn0oaBKGaIfS2D0KFNCCQ-vPKp-DEQxL4N1jiJxy5Xsbf4V4QN8hq3t2FPnBZGVhCTRL9gFf9dEHxSS5FEpQfbAsUbwMmi_-HWiMMSP0CEogO56hYHN3l27bo79-3WCO7EZrmFdhn84Puo4Ao3JsBkAZdJ2UUTgn4Av0NdwvDnxjSc4DDgQtCI_rN4UvuTPIXJwzQtZkx9fScraDCqtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-17182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس مجلس ایران، قالیباف، گفت: «ما زبان دیپلماسی را ترجیح می‌دهیم…»  «اما ما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.»</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/17182" target="_blank">📅 23:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17181">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری CNN گزارش میدهد:  یک فروند پهپاد انتحاری شاهد-136 سپاه پاسداران، موفق به ساقط کردن بالگرد رزمی آپاچی آمریکا بر فراز تنگه هرمز شده‌است.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17181" target="_blank">📅 21:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17180">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری CNN گزارش میدهد:
یک فروند پهپاد انتحاری شاهد-136 سپاه پاسداران، موفق به ساقط کردن بالگرد رزمی آپاچی آمریکا بر فراز تنگه هرمز شده‌است.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/17180" target="_blank">📅 20:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس مجلس ایران، قالیباف، گفت: «ما زبان دیپلماسی را ترجیح می‌دهیم…»
«اما ما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.»</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/17179" target="_blank">📅 20:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران با پهپاد هلیکوپتر آمریکایی را ساقط کرد!  آکسیوس به نقل از یک مقام آمریکایی مدعی شد: تحقیقات به این نتیجه رسید که یک پهپاد ایرانی با یک بالگرد آمریکایی برخورد کرده و موجب سقوط آن شده است.  این مقام آمریکایی مدعی شد هنوز مشخص نشده است که این ساقط کردن…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17178" target="_blank">📅 20:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کریپتو رشد خوبی کرده و طلا هم 700 پیپ از کف فاصله گرفته .  ولی همانطور که گفتم خوش بین نیستم که این توقف درگیری ها پایدار باشد. مراقب باشید</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/17177" target="_blank">📅 20:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دقایقی قبل ترامپ در توییتی اعلام کرد که ایرانی ها مسئول سقوط بالگرد آپاچی آمریکایی در تنگه هرمز بوده اند.  او اعلام کرد که ایالات متحده باید به این حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17176" target="_blank">📅 20:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک فروند بالگرد تهاجمی آپاچی مدل AH-64E ارتش آمریکا روز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و هر دو خدمه آن به سلامت نجات یافتند.   به گفته دو منبع مطلع از این حادثه که با نیویورک تایمز گفت‌وگو کرده‌اند، هنوز مشخص نیست که این بالگرد توسط ایران سرنگون شده است…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17175" target="_blank">📅 20:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17174">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل:
حمله‌ای که ما در ایران انجام دادیم، آمادگی برای ضربه‌ای بسیار مهم‌تر و شدیدتر است.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/17174" target="_blank">📅 19:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17173">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/17173" target="_blank">📅 18:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17172">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ: نتانیاهو مورد حمله قرار گرفت و پاسخ داد و من نمی‌توانم او را به خاطر این کار سرزنش کنم، اما او مورد حمله قرار گرفت. او پاسخ داد و اکنون آن‌ها توافق کرده‌اند که کار را تمام کنند.  بنابراین، قرار است برای یک هفته یا چیزی شبیه به آن، یکدیگر را تنها بگذارند.…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17172" target="_blank">📅 15:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17171">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
نتانیاهو مورد حمله قرار گرفت و پاسخ داد و من نمی‌توانم او را به خاطر این کار سرزنش کنم، اما او مورد حمله قرار گرفت. او پاسخ داد و اکنون آن‌ها توافق کرده‌اند که کار را تمام کنند.
بنابراین، قرار است برای یک هفته یا چیزی شبیه به آن، یکدیگر را تنها بگذارند.
این موضوع مدت‌هاست که در جریان است. می‌توان گفت حدود ۳۰۰۰ سال اگر واقعاً بخواهید — اما قطعاً ۴۷ سال است که ادامه دارد.
آن‌ها زدوخورد می‌کردند. و اکنون هر دو از طریق من توافق کردند که متوقف شوند. و ما در مراحل پایانی چیزی هستیم که قرار است یک توافق بسیار، بسیار خوب باشد که به هیچ وجه، به هیچ شکل یا فرمی اجازه ورود سلاح‌های هسته‌ای و غیره را نخواهد داد.
اگر برویم و بمباران کنیم، که می‌توانیم به راحتی اگر بخواهیم انجام دهیم، و دو یا سه هفته دیگر بمباران کنیم، دیگر هیچ چیزی برایشان باقی نخواهد ماند.
اما شما برای ماه‌ها تنگه باز نخواهید داشت. اگر بمباران را انجام دهیم، می‌دانید، تعداد زیادی از مردم کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نه.
و ما یک سند امضا شده خواهیم داشت که در واقع قوی‌تر از انجام بمباران است.
آنچه ثابت کرده است که یک چیز بسیار قدرتمند است، محاصره است.
تنگه هرمز بلافاصله پس از امضا باز خواهد شد که ممکن است در دو یا سه روز آینده باشد.
من به نتانیاهو گفتم، «کاری که درست است را انجام بده، اما می‌خواهم هرچه سریع‌تر متوقف شوی.» زیرا آن‌ها باید متوقف شوند. این مربوط به لبنان است و باید متوقف شود. ما می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17171" target="_blank">📅 15:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17170">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقاله وال‌استریت ژورنال با این استدلال آغاز می‌شود که جهان وارد مرحله‌ای شده که بسیاری از برنامه‌ریزان انرژی دهه‌ها از آن هراس داشتند: کاهش قابلیت اطمینان تنگه هرمز به‌عنوان مهم‌ترین گذرگاه انرژی جهان. نویسندگان توضیح می‌دهند که تنش‌های نظامی و امنیتی اخیر…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17170" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17169">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سقوط شهر نال خضدار در پاکستان  روز گذشته، شبه نظامیان ‌ بلوچ مستقر در پاکستان، یک شهر پاکستان را تحت کنترل گرفتند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17169" target="_blank">📅 14:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17168" target="_blank">📅 13:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij3H1sBilw0GYckTM4XbtqoeEbMU8ZqgZjlvkeu6FOb8ZerI_gsAPACnahI0gNYULOe_ixuKLsomXvax28SvbXpIegJH-R8A37bb9K1SrZ6jdgtP8uyrDRLkdH9nxGtR4bHsMNLLTw9lqQR8H_F7ytAndXfN-UVu8KVoYWunnY5tBlvb3AN5P-DAoFbOSZPy4JLDhPYTZlivQYgHm1ELCH7nOm-Yj3luMfIq5aq7CzeXofR0f5d65uuownR6l8oQajXeaa4ZiLQuZhhWEA5c3GuDyKwZoXTExohsOnqnp4kPr-wMT_1OnOQmY0zGbiTgr13GWff9J9saoc-4imTvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت هواپیمای ملی جنگ الکترونیک دورایستای ترکیه در آزمایش‌های پروازی
۹ ژوئن ۲۰۲۶ | گابریله مولینلی
هواپیمای جنگ الکترونیک دورایستای هوابرد ترکیه (Hava Soj) که سامانه‌های آن توسط Aselsan  تجهیز شده است، حدود 3 ماه پیش برای نخستین بار مورد توجه قرار گرفت؛ زمانی که تصاویری از یک پرواز آزمایشی آن در تأسیسات Turkish Aerospace Industries در آنکارا منتشر شد. اکنون تصاویر دقیق‌تر و باکیفیت‌تری از این هواپیما در دسترس قرار گرفته است. این تصاویر در قالب یک ویدیوی تبلیغاتی که توسط Turkish Ministry of National Defense به مناسبت صد و پانزدهمین سالگرد نیروی هوایی ترکیه منتشر شده، به نمایش درآمده‌اند.
این هواپیما بر پایه یک جت تجاری دوربرد ساخت شرکت بمباردیه ساخته شده و در برخی منابع ترکی با نام دیگری نیز شناخته می‌شود. این پروژه یکی از مهم‌ترین توانمندی‌های راهبردی ملی ترکیه به شمار می‌رود و ریشه‌های آن به اواخر دهه ۲۰۰۰ میلادی بازمی‌گردد. هدف اصلی این برنامه، جایگزینی سامانه‌های جنگ الکترونیک قدیمی نصب‌شده روی هواپیماهای ترابری نظامی با یک راهکار مدرن‌تر و بومی‌تر بوده است. با این حال، این مسیر طی سال‌ها با فراز و نشیب‌ها و آغازهای ناموفق متعددی همراه بوده است.
حتی پروژه فعلی نیز با تأخیرها و مشکلاتی مواجه شد که در برنامه‌هایی با این سطح از پیچیدگی چندان غیرمعمول نیست. زمانی که در سال ۲۰۱۸ قرارداد توسعه تجهیزات مأموریتی این هواپیما به شرکت آسلسان واگذار شد، برنامه اولیه تحویل سامانه‌ها را در سال ۲۰۲۳ پیش‌بینی می‌کرد؛ هدفی که محقق نشد. نخستین فروند هواپیمای پایه این پروژه در سال ۲۰۱۹ به تأسیسات صنایع هوافضای ترکیه تحویل داده شد.
شرکت آسلسان مسئول توسعه بخش عمده تجهیزات مأموریتی و محرمانه این هواپیما است، هرچند تمامی سامانه‌ها را تأمین نمی‌کند. بر اساس اطلاعات موجود، این هواپیما از یک سامانه پیشرفته دفاعی در برابر موشک‌های هدایت‌شونده فروسرخ به عنوان بخشی از مجموعه دفاع شخصی خود بهره می‌برد. مسئولیت یکپارچه‌سازی تمامی سامانه‌ها نیز بر عهده صنایع هوافضای ترکیه است.گفته می‌شود تجهیزات جنگ الکترونیک این هواپیما بر پایه سامانه‌های زمینی اخلال و جنگ الکترونیک ساخت آسلسان توسعه یافته است؛ سامانه‌هایی که روی کامیون‌های تاکتیکی نصب می‌شوند و در حال حاضر در خدمت نیروهای مسلح ترکیه قرار دارند.
در مجموع 4 فروند هواپیما برای تبدیل به این پلتفرم جنگ الکترونیک خریداری شده‌اند. انتظار می‌رود نخستین نمونه عملیاتی تا پایان سال جاری تحویل شود و این سامانه احتمالاً در سال ۲۰۲۷ به آمادگی عملیاتی کامل برسد. اطلاعات کمی درباره تجهیزات الکترونیکی نصب‌شده روی این هواپیما منتشر شده است، اما مأموریت اصلی آن شناسایی، ردیابی و سرکوب سامانه‌های پدافند هوایی دشمن است تا برای هواپیماهای رزمی خودی «دالان‌های امن» جهت ورود و خروج از حریم هوایی دشمن ایجاد کند. چنین مأموریتی مستلزم برخورداری از توانمندی پیشرفته کشف و مکان‌یابی رادارها، سامانه‌های قدرتمند اخلال الکترونیکی و احتمالاً قابلیت‌های جمع‌آوری اطلاعات مخابراتی و اطلاعات الکترونیکی است. پیش‌بینی می‌شود این هواپیما دارای ۶ تا ۸ ایستگاه کاری برای اپراتورها بوده و بتواند حدود ۸ ساعت به‌طور مداوم در مأموریت باقی بماند.
هواپیماهای اخلالگر دورایستا از جمله ارزشمندترین و پیچیده‌ترین قابلیت‌های تاکتیکی در حوزه جنگ الکترونیک به شمار می‌روند؛ قابلیتی که تنها تعداد محدودی از کشورها در اختیار دارند و تعداد کمتری نیز قادر به تولید کامل آن در داخل کشور خود هستند.
در آینده، این هواپیمای جنگ الکترونیک ترکیه می‌تواند در بازار صادراتی نیز موفقیت کسب کند. کشورهایی مانند پاکستان و عربستان سعودی از مشتریان بالقوه آن محسوب می‌شوند. آسلسان هم‌اکنون از طریق همکاری مشترک با یک شرکت فناوری عربستانی، در حال معرفی و بازاریابی این پروژه در عربستان سعودی است.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17167" target="_blank">📅 12:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روابط عمومی ارتش، از کشته شدن یکی از پرسنل واحد پدافندی خود به نام "سید بهمن حسینی" در حملات صبح امروز اسرائیل خبر داد.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17166" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">موسسه مطالعات جنگ:
راهبرد بازدارندگی ایران به‌طور فزاینده‌ای بر توانایی ایجاد اختلال در شریان‌های حیاتی تجارت جهانی و افزایش هزینه‌های اقتصادی برای رقبایش استوار شده است. تهران و متحدان منطقه‌ای آن تلاش می‌کنند با تبدیل تنگه‌ها و آبراه‌های بین‌المللی به اهرم فشار ژئوپلیتیکی، هرگونه اقدام نظامی علیه ایران یا شرکای آن را برای آمریکا و اسرائیل پرهزینه‌تر کنند. در این چارچوب، تنگه هرمز، باب‌المندب و دریای سرخ به اجزای کلیدی معماری بازدارندگی ایران تبدیل شده‌اند.
ایران طی سال‌های اخیر بارها نشان داده است که کنترل و نفوذ بر تنگه هرمز را صرفاً یک موضوع امنیتی نمی‌داند، بلکه آن را ابزاری برای اعمال فشار اقتصادی بر رقبای خود تلقی می‌کند. تهران با استفاده از اقدامات قهرآمیز دریایی و اعمال محدودیت‌های عملیاتی بر کشتی‌ها، تلاش کرده است نقش خود را به‌عنوان بازیگری تعیین‌کننده در امنیت این گذرگاه حیاتی تثبیت کند. ارزیابی‌های مختلف نیز نشان می‌دهد که جمهوری اسلامی کنترل و تهدید به اختلال در تردد دریایی از طریق هرمز را یکی از مهم‌ترین عناصر بازدارندگی آینده خود می‌داند. مقام‌های ایرانی بارها تأکید کرده‌اند که در صورت تشدید فشارها یا وقوع درگیری، می‌توانند هزینه‌های سنگینی را از طریق اخلال در تجارت دریایی جهانی به آمریکا و متحدانش تحمیل کنند.
این رویکرد تنها به تنگه هرمز محدود نمی‌شود. ایران و شبکه متحدانش در تلاش هستند تا زنجیره‌ای از نقاط گلوگاهی اقتصادی را از خلیج فارس تا شرق مدیترانه در اختیار داشته باشند. در همین راستا، رسانه‌های نزدیک به حاکمیت ایران از شکل‌گیری یک «معادله امنیتی جدید از هرمز تا بیروت» سخن گفته‌اند؛ معادله‌ای که در آن کنترل یا تهدید به مسدودسازی مسیرهای حیاتی حمل‌ونقل دریایی به بخشی از قدرت بازدارندگی تهران تبدیل می‌شود.
در این میان، حوثی‌های یمن نقش مهمی در تکمیل این راهبرد ایفا می‌کنند. اعلام ممنوعیت عبور کشتی‌های مرتبط با اسرائیل از دریای سرخ و تهدید به گسترش این محدودیت‌ها نشان‌دهنده تلاش برای تبدیل باب‌المندب و دریای سرخ به جبهه‌ای دیگر از جنگ اقتصادی علیه اسرائیل است. منابع نزدیک به حوثی‌ها حتی هشدار داده‌اند که اقدامات بعدی می‌تواند به جلوگیری از عبور تمامی کشتی‌های عازم بنادر اسرائیل منجر شود. این تهدیدها بیانگر آن است که هدف صرفاً حمله به اهداف نظامی نیست، بلکه افزایش هزینه‌های تجاری، بیمه‌ای و لجستیکی برای اسرائیل و شرکای آن در اولویت قرار دارد.
تجربه سال‌های گذشته نیز نشان داده است که حملات حوثی‌ها به کشتی‌های مرتبط با اسرائیل یا شرکت‌های همکار با بنادر اسرائیلی، بسیاری از خطوط بزرگ کشتیرانی را وادار به انتخاب مسیرهای طولانی‌تر و پرهزینه‌تر کرده است. به همین دلیل، فشار بر باب‌المندب و دریای سرخ در عمل مکمل فشار ایران بر تنگه هرمز محسوب می‌شود. در واقع، تهران و متحدانش می‌کوشند با ایجاد تهدید همزمان علیه چندین گلوگاه حیاتی تجارت جهانی، هزینه هرگونه رویارویی نظامی با محور تحت رهبری ایران را به شکل قابل توجهی افزایش دهند.
در کنار این فشارهای دریایی، حملات موشکی محدود حوثی‌ها به اسرائیل نیز در همین چارچوب قابل ارزیابی است؛ یعنی حفظ فشار مستمر بر اسرائیل در حالی که تمرکز اصلی همچنان بر استفاده از اهرم آبراه‌های بین‌المللی و تهدید اختلال در جریان تجارت جهانی برای ایجاد بازدارندگی و تحمیل هزینه به طرف مقابل باقی می‌ماند.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17165" target="_blank">📅 11:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کارشناس صداوسیما:
در جنگ ۳۹ روزه؛ بالای ۱۰۰۰ تا کشته از آمریکایی ها و بالای ۲۰۰۰ تا کشته از اسرائیلی ها گرفتیم. هر کدام هم ۶ یا ۷ هزارتا زخمی دادند. برای ما که کشته گرفتن کاری ندارد و  الان هم به احترام کشورهای منطقه که از‌ ما خواهش و التماس کردند کوتاه آمده ایم.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17164" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJGiGuSaYT77OEf_mAGq8cOTQARS9Ga_Ns88ZVcueOW22vMefaC6dYvqFR33bouKyMcc87hgLwcq-_FcmhOFGSqnrigsoZBK26izhWlPfwHZNcbJ5qI3ErD1D5o88L1BhnywcCxUTOoiIlo5c041RS4l8fn97Y-a5rAoGuiJJr_PUH9f4SpAISb9Rn79MyWo5rY8sbeHPuLOmJsQJLA2_nZd3paCdBY3v4c-QEmrGd7mcqYtejbwbvfZcKm99nWr2B8YW3nebhM4A8TMJj9MDo2PwOYO5xk3ZLqjj421Nsmfwdcd9Qe9k0lEF38dlVYOn-2KS4tqwfXkPl3UjI6fiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند بالگرد تهاجمی آپاچی مدل AH-64E ارتش آمریکا روز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و هر دو خدمه آن به سلامت نجات یافتند.
به گفته دو منبع مطلع از این حادثه که با نیویورک تایمز گفت‌وگو کرده‌اند، هنوز مشخص نیست که این بالگرد توسط ایران سرنگون شده است یا خیر</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17163" target="_blank">📅 09:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZYuRpqcbVFBxxhjkK9V8pDt5BY2izPI6hYV1xjVVeAwJ4kKgJYHCqS8tntIAecXVmN5jh49HYJZb7xhAIpU5tQRYPmwaGzJRsrAe18EDCcEF_v8TzxYUpXeZZm8s0jTwIn_AeEKaOCfAGErvAxqvmVpDGXYBzljRfjhrmkBjSHqxj0f5DmqCNhSzquDu_hHuybqbeiKAeO9VDGR9WPQLXuoLywEgGMCu6BTDlkUjANA3t93zokQtZ4PfLisl2GHDeeQizYCFflsLBaTR8H8F6bUju7nFXj71KjbCoFTzD1xk7kkkr3KY_RVqSwLpLlzKufEHVvQYvRuXAHJOJwrRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دقت بکنید عمده اهدافی که در این یکی دو هفته اخیر مورد حمله آمریکا قرار گرفته مربوط به رادارهای ساحلی و سامانه های نظارتی و مخابراتی و ... بوده است که  در کشف اهداف متحرک و هدفگیری آنها جایگاه اساسی دارند. هدف ثابت (مثل پایگاه های آمریکا در کویت و ...)…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17162" target="_blank">📅 08:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: «ایران همه چیزهایی که می‌خواهیم را به ما خواهد داد.»</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17161" target="_blank">📅 02:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">طبق گزارش‌های منتشر شده توسط ژورنالیست کن کلیپنشتاین، همزمان با تهدیدهای ترامپ برای انجام یک حمله کماندویی، ایالات متحده به صورت پنهانی نیروهای پیاده‌نظام هوایی ۸۲ را به اسراییل اعزام کرده است.
این اعزام به آخرین برنامه‌های مشترک ایالات متحده و اسرائیل برای تصرف جزیره خارک ایران مرتبط است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17160" target="_blank">📅 02:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">روابط عمومی ارتش، از کشته شدن یکی از پرسنل واحد پدافندی خود به نام "سید بهمن حسینی" در حملات صبح امروز اسرائیل خبر داد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17159" target="_blank">📅 02:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این حرامزاده پول بده نیست بیخودی امید نداشته باشید</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17158" target="_blank">📅 02:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔶
ناکارآمدی شلیک پراکنده و ضرورت حملات متمرکز
🔸
از شب گذشته، الگوی شلیک پراکنده موشک‌های بالستیک کشورمان علیه اسرائیل، نتوانسته تأثیر نظامی مورد نظری بگذارد. دلیل اصلی آن است که توزیع فضایی و زمانی اهداف، مزیت ذاتی برای لایه‌های پدافند هوایی اسرائیل ایجاد…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17157" target="_blank">📅 00:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادامه آتش بس را مدیون بچه های هوافضای سپاه و پدافند اسراییلی ها هستیم!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17156" target="_blank">📅 00:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گفته می شود امروز، پس از حملات هوایی تلافی‌جویانه اسرائیل علیه ایران، هیئتی از امارات متحده عربی با هواپیمای بوئینگ از ابوظبی وارد تهران شد و با مقامات جمهور اسلامی دیدار کرده است.
به گفته منابع ایرانی، این هیئت به تهران اطمینان داد که امارات متحده عربی از هیچ عملیات نظامی آینده اسرائیل یا ایالات متحده علیه ایران حمایت نخواهد کرد.
به نظر می‌رسد این دیدار نشان‌دهنده نگرانی فزاینده در ابوظبی در مورد احتمال حملات مجدد موشک‌های بالستیک و پهپادهای ایران به زیرساخت‌های حیاتی نفت و انرژی امارات متحده عربی باشد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17155" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.   این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17154" target="_blank">📅 22:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17153" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">— فرمانده نیروی قدس سپاه پاسداران، اسماعیل قاآنی:
«از تنگه هرمز تا باب‌المندب و از خلیج فارس تا دریای سرخ، یک کمربند مقاومت امنیتی جدید تأسیس شده است.
شرارت‌های رژیم صهیونیستی و آمریکا در این منطقه با پاسخی از سوی جبهه مقاومت متحد روبرو خواهند شد».</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17152" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ گفت که او از نخست‌وزیر اسرائیل نتانیاهو خواست تا به حمله موشکی ایران پاسخ ندهد، اما اسرائیل بعداً تصمیم به حمله به ایران گرفت و تنها در مرحله‌ای متأخر به ایالات متحده اطلاع داد.
او گفت:
«آن‌ها قبلاً در راه ایران بودند. من توانستم دامنه حمله را کاهش دهم،».</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17151" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نفت کش هندی بوده !</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17150" target="_blank">📅 20:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توقف یک نفت کش ایرانی از سوی ارتش آمریکا!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17149" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توقف یک نفت کش ایرانی از سوی ارتش آمریکا!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17148" target="_blank">📅 20:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">اسرائیل بامداد امروز به یک سیستم پمپاژ حیاتی در مجتمع پتروشیمی کارون در ماهشهر، ایران، حمله کرد و هدف آن یک قطعه گران‌قیمت و ضروری بود که مسئول انتقال مواد در داخل این مجموعه است، به منظور مختل کردن عملیات و توقف تولید
ای۲۴.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17147" target="_blank">📅 19:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آغاز حمله سنگین ارتش اسرائیل به شهر صور لبنان</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17146" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17145" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به نتانیاهو گفته که او معتقد است ایالات متحده و ایران در حال نزدیک شدن به توافق بر سر چارچوبی هستند که به طرفین اجازه می‌دهد برای رسیدن به یک توافق بلندمدت به میز مذاکره بنشینند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17144" target="_blank">📅 19:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قرارگاه خاتم با ندای «لبیک یا دونالد» به استقبال خرید کریپتو رفت.  اکنون توپ در زمین بی بی است</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17143" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIV7fu6_ubMcaUMzKD_KO6AtcmrrSmojSKkILXVb_WWEtGADxmU68BNu8gCs-kZi0PKCbwa1NIB3va3mUSOXoaHuwVd76gHM-LcV8tQRrlfFYR9IIG3_8JxoSKAff0wlRWIOoNjUu6Yku2jqR-dJmP7BrI2K55OTlExwti30ikpATR6Wl7D5DnVTfRD3Ipy-3buttcqD6GcEdUUx7QmnGDC1mjsc3TqM4vPONgzzfagTfGZYlvUyjKN3h8Y9JvGVXQOAx9xXfVI72jkxf3DSIKtGudVYvY8dqNABlZ11Uf2cYAKAs5t8bZz3mkJX9w8UcEhy5tnccadFfIm-7P_e7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم با ندای «لبیک یا دونالد» به استقبال خرید کریپتو رفت.  اکنون توپ در زمین بی بی است</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17142" target="_blank">📅 18:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— یک مقام آمریکایی به سی‌ان‌ان گفت:  «ادعاهای اسرائیل مبنی بر اینکه ایالات متحده موشک‌های بالستیک ایران که به سمت اسرائیل پرتاب شدند را رهگیری کرده است، هیچ حقیقتی ندارد.  نیروی نظامی ایالات متحده هیچ‌یک از موشک‌های ایرانی که دیشب پرتاب شدند را رهگیری نکرد.»</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17141" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">— یک مقام آمریکایی به سی‌ان‌ان گفت:
«ادعاهای اسرائیل مبنی بر اینکه ایالات متحده موشک‌های بالستیک ایران که به سمت اسرائیل پرتاب شدند را رهگیری کرده است، هیچ حقیقتی ندارد.
نیروی نظامی ایالات متحده هیچ‌یک از موشک‌های ایرانی که دیشب پرتاب شدند را رهگیری نکرد.»</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17140" target="_blank">📅 18:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17139" target="_blank">📅 16:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، از تلاش‌های رهبری سوریه برای بازگرداندن ثبات تقدیر کرد و پیشنهاد داد که احمد الشراع رئیس‌جمهور سوریه، می‌تواند در برابر حزب‌الله در لبنان نقش ایفا کند.
او الشراع را به عنوان «رهبری بسیار خوب» برجسته کرد که مایل به کمک به ایالات متحده در تلاش‌های امنیتی منطقه‌ای خواهد بود.
ترامپ حتی پیشنهاد داد که سوریه می‌تواند در تسهیل حملات «جراحی» علیه حزب‌الله نقش ایفا کند و گفت که او می‌خواهد «زندگی بهتری» برای مردم لبنان داشته باشد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17138" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:  «هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره 'صلح' در حال پیشرفت است، مشروط بر اینکه نادانی یا حماقت در راه آن قرار نگیرد.  محاصره همچنان با تمام قدرت و اثر در جای خود باقی خواهد ماند، تا زمانی که یک 'توافق نهایی' حاصل…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17137" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود./فارس</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17136" target="_blank">📅 14:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">— سامانه‌های پدافند هوایی ایران در شهر مرکزی یزد فعال شده‌اند و در حال دفع «اهداف خصمانه» هستند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17135" target="_blank">📅 14:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:
«هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره 'صلح' در حال پیشرفت است، مشروط بر اینکه نادانی یا حماقت در راه آن قرار نگیرد.
محاصره همچنان با تمام قدرت و اثر در جای خود باقی خواهد ماند، تا زمانی که یک 'توافق نهایی' حاصل شود.
امور باید به سرعت پیش بروند».</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17134" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بروجردی، عضو کمیسیون امنیت ملی مجلس:   تسلیحاتی داریم که اگر به کار بگیریم زندگی صهیونیست‌ها را مختل می‌کنیم</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17133" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بروجردی، عضو کمیسیون امنیت ملی مجلس:
تسلیحاتی داریم که اگر به کار بگیریم زندگی صهیونیست‌ها را مختل می‌کنیم</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17132" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">— ارتش اسرائیل:
«برخلاف گزارش‌ها، ما در چند ساعت گذشته هیچ حمله‌ای به ایران انجام نداده‌ایم».</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17131" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
— رئیس‌جمهور آمریکا، ترامپ، به آکسیوس گفت:  «هر کدام از آن‌ها خوش گذراندند. اسرائیل حمله‌اش را انجام داد و ایران حمله‌اش را انجام داد. ما به یکی دیگر نیاز نداریم».</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17130" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Operation Nasr !</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17129" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
سیتنا
:
سرعت اینترنت از شب گذشته با شروع درگیری ها افزایش پیدا کرده و فعلا دستوری برای قطع دیتاسنترها دریافت نشده اما شرایط پایدار نیست</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17128" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هرمز دوباره به صورت کامل بسته شد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17127" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDBoDAu6YzRgSbAnLwwPoKkjhWfX5gaBy6VnyFlCvn-a5SRuIJs86xp01tc8oYGPGZBFLcrH4CMaxfebQlMa_IrklWTVQZnht32vxxFP82SBK-M1ZLMCzlCkGlBNwJqzfju4iWTm8Hp3aXy6yQ6d0fWtxNVAfU2t329SJk2VvG_O7lZnTqY0p9QlaA1bK95I8RD20HlcsrNRd0OJwyxeESC1XxBnbjz1YZf0JRGca7DXBaVbX7tsIEXMaykKxKoNUyxIovRc-BRphKfiKA_dDEbcJftwP-O_cHtx8wM00YMEUpNRd6EbgAmpQ8a-pRHkEfLWGEGI9msgQREmMMM8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی ببینید گیر چه اسکل هایی افتاده ایم!
اینها برای فرزندان ما تصمیم میگیرند!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/17126" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارتش اسرائیل می‌گوید انتظار دارد چند روز درگیری با ایران ادامه یابد و احتمال از سرگیری کامل جنگ وجود دارد</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17125" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فقط نت را قطع نکنید ، بگذارید این لحظات را کنار هم بگذرانیم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17124" target="_blank">📅 12:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMIQKyGtPLQAr559hrkfmBlO34dIwA9VIWmCyiK7xCo2yLRR_7APf5W6uhzFQ2oJMNUqaMbPk8Wes-SyxJpIOrPoDIBd-XAUrWHOzShG7m8_Pl1f1QbEgjBQWJ6yzHbImfbNe9VVSfII00gKGIQMxW2guh2q69LsShWcV75Z8647DXM4ffp98_b8W-oS45DF2LucVeIkr8Djcv7G9jRtLA2ip7rwEB-E75vtU9gXtk-nGVrsZlIV5rvb5pL6wxgRldaEaJWjbX983Jg6HWHFlEjS7LRE033WLsWC-81_iSYoFdOaAX9oioHIJx3ms2r3ycFTaoiKyyPezZDzrk18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بشدت حق!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17123" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اصفهان</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17122" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسرائیلی ها مدعی شده اند که با حملات امروز، روند بازسازی پدافند هوایی ایران را مختل کرده اند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17121" target="_blank">📅 11:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کرج کرمانشاه</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17120" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17119" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17118" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17117" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال 12 اسرائیل:   انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17116" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17115" target="_blank">📅 11:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانال 12 اسرائیل:   انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17114" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال 12 اسرائیل:
انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17113" target="_blank">📅 11:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دلشان خوش است که 4 تا فلسطینی فلک زده از این حملات خوشحال باشند! نابودی زندگی و زیرساخت های خودمان مهم نیست آن وقت شادی مضحک این یارو مهم است!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17112" target="_blank">📅 10:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خوشحالی یکی از فلسطینی های مظلوم نوار غزه که میگه:  ایران الان داره می‌زنه، داره می‌زنه، جانم ایران، جانم جمهوریه اسلامی ایران آزاد، به عشق خدا. به هر کشوری که با موشک‌های شما مخالفت می‌کند، حمله کنید، حتی اگر پدر خودم باشد. موشک‌ها را پرتاب کنید.  @IRAN_CITYOFSUN</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17111" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران،شهر خورشید(رضایی)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4484d2171d.mp4?token=lS-ikg7JmQob6jZJhyDmm4MvwLSZTXglFNWschzjXNXnoZua2dTAMujvvUUGnVNceM1wKNYCLOYXzlx7Vb_BGXV8UC1nguq8O7_owX-U4rMkmHluMoGQmJaDszBnJpcAE1cMzkqWiX9SOXgYhJczsnrNWkhkrRCfPPSEINA6nZc51EQZhOaZ1cuDE33I9pJH30u6cDSmCG7WfKqM0j-33-VTrda3jHl-ZyoAGknaUAOMOatwnbF-Lhtq5kzx61dKDcDoN9buhMskDIc2gb8gTHF6Q_P2GBHY_xz9AFUP66e6-74LJk24Qgv3tI36zUamEsRfsxRAkTgW3WvA9Evhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4484d2171d.mp4?token=lS-ikg7JmQob6jZJhyDmm4MvwLSZTXglFNWschzjXNXnoZua2dTAMujvvUUGnVNceM1wKNYCLOYXzlx7Vb_BGXV8UC1nguq8O7_owX-U4rMkmHluMoGQmJaDszBnJpcAE1cMzkqWiX9SOXgYhJczsnrNWkhkrRCfPPSEINA6nZc51EQZhOaZ1cuDE33I9pJH30u6cDSmCG7WfKqM0j-33-VTrda3jHl-ZyoAGknaUAOMOatwnbF-Lhtq5kzx61dKDcDoN9buhMskDIc2gb8gTHF6Q_P2GBHY_xz9AFUP66e6-74LJk24Qgv3tI36zUamEsRfsxRAkTgW3WvA9Evhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشحالی یکی از فلسطینی های مظلوم نوار غزه که میگه:
ایران الان داره می‌زنه، داره می‌زنه، جانم ایران، جانم جمهوریه اسلامی ایران آزاد، به عشق خدا. به هر کشوری که با موشک‌های شما مخالفت می‌کند، حمله کنید، حتی اگر پدر خودم باشد. موشک‌ها را پرتاب کنید.
@IRAN_CITYOFSUN</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17110" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBxJgvkBzhHnXbP0Sr1OvvACaBuuHT0koKKegl37KdMfFBhOTqsazfsWaG9oGpT5Tz61UhrNR4SG3E-nG_0FuRxN8qKrL4zT-Jy09q9VdRFzRJmAZk7l9HMlFJEaIj_QkWXbGs_wliAcqQACxs2KGJoJ4zw7XScViEiJhA9s6zYrFufs325xPUwYM6iudYda-VuA18uq0LLTlQT0t-Cteok7Dnq31qhWWOuss7bdFlfwTNrDXd9ZYW1TgREXEy6TiOFbf3nVGF9cGCgI12xxdC_7KLSFrjC62dhvj4x1QIZDi8vP502H7q2A_duwuFUPKC_3gNMhniQu2rWvuQmHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه های موشکی استفاده شده در حملات امروز</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17109" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17108" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17107" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17106" target="_blank">📅 10:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17105" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17104" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه ی نیروهای مسلح یمن:
ممنوعیت کامل و مطلق دریانوردی رژیم صهیونیستی در دریای سرخ</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17103" target="_blank">📅 09:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب فعلا خبری نیست برویم بخوابیم .  به نظرم کریپتو و طلا و نقره یک ریکاوری و رشد خوبی فردا خواهندداشت.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17102" target="_blank">📅 09:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اورژانس استان تهران:  در پی اخبار منتشر شده شب گذشته، تا این لحظه هیچگونه تماسی مبنی بر وجود مصدوم نداشته ایم</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17101" target="_blank">📅 09:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Operation Nasr !</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17100" target="_blank">📅 09:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17099" target="_blank">📅 09:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در اسرائیل، تخمین زده می‌شود که این یک ابتدای شعله‌ور شدن یک تنش است که می‌تواند به یک جنگ  تشدید شود. آماده‌سازی برای چند روز درگیری.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17098" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه پاسداران: «ما آماده انجام عملیات در تمام جبهه‌ها هستیم و پاسخ خود را بر اساس سناریوهای مختلف دشمن برنامه‌ریزی کرده‌ایم».</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17097" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه پاسداران در بیانیه ای مدعی شده است که در اخرین حملات موشکی خود پایگاه های هوایی تل نوف و نواتیم را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17096" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه پاسداران در بیانیه ای مدعی شده است که در اخرین حملات موشکی خود پایگاه های هوایی تل نوف و نواتیم را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17095" target="_blank">📅 08:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اورژانس استان تهران:
در پی اخبار منتشر شده شب گذشته، تا این لحظه هیچگونه تماسی مبنی بر وجود مصدوم نداشته ایم</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17094" target="_blank">📅 08:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : نیروی هوایی اسرائیل ۲۰ هدف تو ایران را زده</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17093" target="_blank">📅 08:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منبع اسرائیلی:   ما به حمله پاسخ خواهیم داد، حتی اگر در بازه زمانی فوری اتفاق نیفتد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17092" target="_blank">📅 03:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کارت نابودی حزب الله را سوزاندند تا کارت باز کردن تنگه هرمز را نگه دارند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/17091" target="_blank">📅 02:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: «حملات ایران هیچ  تأثیری بر توافق ندارد. ما قرار است یک توافق بزرگ انجام دهیم»</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17090" target="_blank">📅 02:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ از نتانیاهو خواست «چند روز» صبر کند تا ببیند آیا می‌توان با ایران به توافق رسید –</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17089" target="_blank">📅 02:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر تعداد موشک ها اندک باشد عملا همان حمله فرمالیته است</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/17088" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایران پیامی به اسرائیل مخابره کرده و اعلام کرده است که موج جدید حملات خود را به پایان رسیده تلقی می‌کند و قصد انجام حملات بیشتری را ندارد، مگر اینکه اسرائیل حملات جدیدی را آغاز کند.  — کانال ۱۳ اسرائیل</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17087" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=Mw0LfZe_O65TtjOwuHPRcrkxUPQKVsIAJ85_Drit6SkqK-cp6torMUfl6nl_RI14ewW_rYBAhI9n1-nzYOjjnjXoyleGaUyFXt0oeDber6D9SpwaBCY2mZsXDlGyblHAOsOOOdax1P5IHariuNmREUg7467s-lztgYLs7rds-Cjg0YmPTFg7av4kTPLaB_G4mP10_YlG_lgdeZ98M0uK1AdnbvJBlOkRcUVNfvOTiUaVT_TJ4yp1K928TjqO4ugiWoM2J8kbar6gJ2-lRqdnN7qTf5WG6DNxqa2M6NdVCx4XxbGeh9vkrgWH0c5su28G_Gt8CRoEgAMHBnvA5g9FUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=Mw0LfZe_O65TtjOwuHPRcrkxUPQKVsIAJ85_Drit6SkqK-cp6torMUfl6nl_RI14ewW_rYBAhI9n1-nzYOjjnjXoyleGaUyFXt0oeDber6D9SpwaBCY2mZsXDlGyblHAOsOOOdax1P5IHariuNmREUg7467s-lztgYLs7rds-Cjg0YmPTFg7av4kTPLaB_G4mP10_YlG_lgdeZ98M0uK1AdnbvJBlOkRcUVNfvOTiUaVT_TJ4yp1K928TjqO4ugiWoM2J8kbar6gJ2-lRqdnN7qTf5WG6DNxqa2M6NdVCx4XxbGeh9vkrgWH0c5su28G_Gt8CRoEgAMHBnvA5g9FUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:  «تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.  در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17086" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:
«تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.
در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17085" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17084" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک مقام ارشد اسرائیلی  گفت: «پاسخ مورد انتظار به ایران شدید و گسترده خواهد بود».</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17083" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
