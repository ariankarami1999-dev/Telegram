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
<img src="https://cdn4.telesco.pe/file/SO-jp_AnMUkUBJiEIUtyrPBL3SICCV6L8EjpuJG5g9JpdV0paAhdXoek4AS8c8VUIZsY-lli-xqShMGmJK8o6JAbRi5IVn_rKW-vYeHLJe9qETyDVqEBI6ppUq2mO3KE1v2_R2CKn85b3xH6t-LsTHrP9bxpe4LlrN3GTExkZGE7iqOzk_eNbxEgeNmY5OLsldXOd3VjVG_sklmCLEeVtQp3hs6MFAIiPv_sssfavcUVZ-0D868d5Yek5wQAsimK5JzlB0WoK-O4ihd2NuQ93Zz1R7Xa9SymPcPu9x1QRAF5Dc5WdCzFDYRfmq7_X0vnhlrZWUZQDZGRy_HmqmcXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 21:23:56</div>
<hr>

<div class="tg-post" id="msg-677442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هاآرتص: ارتش اسرائیل سطح آماده‌باش خود را به حداکثر درجه رسانده است تا در صورت حمله احتمالی آمریکا به ایران، آماده باشد. / انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/677442" target="_blank">📅 21:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677441">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWQsgkV3P5YYtIRmk08Ofxx5ZZeH2xMJUYK7umxlZJBMLZGMGUhi2e82XCb3U4f950WNh7lADE-QYSfExA7VlwpMwFWUxE2n5U1EkYB-aByRRb2BpXGXRhIgiHFogORmI1GHmuTGOQX1w4iNPJq6WRbeR6V16o12et73-fp1Y-bvE7tgTZ6DPM2qkoZFFgsHaNhWCH2K-riordOUWgdPJpPZadvVeSuHzd79e1eRbBRGUQ_CrnOLeGSv0MgDuVxYzoFdrB6SqBkPULUd-WSjeDFpO9SJO83ZX-zbXqwr4HSSKDgSXeE8EO6uiBS_RCqV9D6JSduqHxiT6Ye4o5SJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
الوعده وفا؛ گام بلند فولاد خوزستان برای جبران ناترازی انرژی
♦️
فاز اول نیروگاه خورشیدی بهبهان فولاد خوزستان در آستانه بهره‌برداری
🔹
در شرایطی که توسعه نیروگاه‌های خودتأمین به یکی از مهم‌ترین راهکارهای عبور صنعت از چالش ناترازی انرژی تبدیل شده، فولاد خوزستان با اجرای پروژه نیروگاه خورشیدی بهبهان، گامی مؤثر در مسیر تأمین پایدار انرژی برداشته است.
🔹
این پروژه افزون بر افزایش تاب‌آوری تولید، با کاهش وابستگی به شبکه سراسری برق در زمان اوج مصرف، به حفظ پایداری شبکه برق برای سایر بخش‌های مصرف کمک خواهد کرد؛ رویکردی که منافع صنعت و منافع ملی را در یک مسیر مشترک قرار می‌دهد.
👇
👇
akharinkhabar.ir/local/10964275/</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/677441" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaJT46Ka8pMOzYXKApUabC9HhxeelAPKwyBvE1Hb22siqvSNIUkLHEDH3ejao79P0nIrMBjvRrr5YOE7oZmNexJ5diqrMmVf7a0PJy1DHAX6pqlJVjueOf9hYJFJaNNQMorUT_ae4llHASPTa_NR79tRCVKjYP9MiCJBuGZ7YPOf_-hbayrPKvC_0zLCpW-EV9xkujm2hMsfAe2XOo8NcgD8NFgTv9iynoJodiKyAibO01kfr_aJe6ZWBal-4ml5rHX9NEchRGpN7VgxzYtlLcZbnFZDtcb6MrH0YI1Ikcyg6ryLdMVR-StMij1hyMT3cXoOfSLIeFS4zodUIA8Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی‌نیوز: روسیه در حال ارائه اطلاعات الکترونیکی به ایران است
ان‌بی‌سی‌نیوز:
🔹
نظارت ماهواره‌ای و اطلاعات سیگنال‌های روسیه احتمالاً به ایران اجازه می‌دهد تا بهتر از خود در برابر حملات هوایی ایالات متحده دفاع کند و حملات هوایی خود را بهبود بخشد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/677440" target="_blank">📅 21:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Fz7ZESP1_6PyX_s3cuqDjAZ0It87CNrobiOzeOmfG6h1LmdQgn7S40xv0sBBLmEpz8DyAbn558oypatSFqvUkPxzxTYmAuIMgJ2eqATjlt40qzSgtQE_bazyuiSy1Px0Km6Z2X1xm8JsyhIKb1Xbx5vTJVmccy3xgdcBN_WzMXmbZfNa2n4-Y3_tTMuB9U2Wl4VqJ9b9ubThbja35SRLU3jVAeZheGnxteUog20b4vnRJS0b3ng1hHqDtfmI-RZu7xjCKMjJWJERDp22ACtHlJv7ktRpFIOKX3uboo3A3U1bMVy2rc1w9QqusRk8VNbOaOGew6yJ9V7b5efpiaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای ناشناس آمریکایی که احتمالا جنگنده است از پایگاه هوایی الظفره به پرواز در آمد تا بر فراز خلیج فارس عملیات کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/677439" target="_blank">📅 21:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
الجزیره از حمله پهپادی به سلیمانیه در شمال عراق خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/677438" target="_blank">📅 21:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80bf386d9.mp4?token=WdkDjjvQDXhoGILBJWeUTDDaMZNoZcNPq_W4m6SlWs2PnN4l_BVIflKp7UBi5E44daqsLiX6AH0WFTxCaNcMKJmYDMPB9Ln-Cj9YNgHw2-zjSESWiJz53yabT9JNnZzgMgpqB4D84Ko-zUTdwxaGtNQAw50lXFblf6eU7ZT0k7m7cIQh-fgcv0JVkT-ldWSpT7NC1Ch0GR9gxpD08gAA-WbW4SQORRHDqgJwPTd6FlF41KBcT8OmjgqP6toId-QEOkcf7wkT_nPCfoYgPF_F7UxEWx2V3BYHpsSZd0OaWiDSx0WXmdwi2XNj4K0JLX_48EJ62-LydMfqzMoodfs-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80bf386d9.mp4?token=WdkDjjvQDXhoGILBJWeUTDDaMZNoZcNPq_W4m6SlWs2PnN4l_BVIflKp7UBi5E44daqsLiX6AH0WFTxCaNcMKJmYDMPB9Ln-Cj9YNgHw2-zjSESWiJz53yabT9JNnZzgMgpqB4D84Ko-zUTdwxaGtNQAw50lXFblf6eU7ZT0k7m7cIQh-fgcv0JVkT-ldWSpT7NC1Ch0GR9gxpD08gAA-WbW4SQORRHDqgJwPTd6FlF41KBcT8OmjgqP6toId-QEOkcf7wkT_nPCfoYgPF_F7UxEWx2V3BYHpsSZd0OaWiDSx0WXmdwi2XNj4K0JLX_48EJ62-LydMfqzMoodfs-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید تلخ‌ترین اتفاقی که میشه با دیدن این تصویر کاملا متوجهش شد
🔹
این نوزاد ۴ ماهه از همون روزی که به دنیا آمد در یه بیمارستان در اکوادور زندگی می‌کند چون، مادرش بعد از تولد رهاش کرده و دیگه هیچ‌وقت برنگشته
🔹
پرستارها می‌گن هر بار کسی از کنار تختش رد میشه، سرش رو بالا میاره و با دقت نگاه می‌کنه؛ انگار هنوز منتظره یه نفر بیاد، بغلش کنه و ببرش خونه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/677437" target="_blank">📅 21:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bda2e364.mp4?token=HOjbBvYodLMS1JUiSqIbM6N6S5rvBUtf5A8dDkh1Ir-o2fkc_Q_XJiGH2XTZyIKphnrPFeGjMo2IjLY5XB370U0I86kTByUzJVPIdEvblHNtky8h-_B17vk4jqBry_siGcP-YdrqMk7X4hR2DitOKOTIePTfiz63tnzrmYPwHmmJayyJ6pj68I-B55Pzcc75-JKgyL0NxJUFCYEktN-cym9YH41E1psXX5cbr4xjqFzcClIgyis08LMsQ9Ao84UEJynzrIJdJXAbVkxwBP-D6iEjN6Hw6IJxFwDwylwHNDePCVMGKfXSnBmFw07Hqb9-FjZGPGhyP8NHjsR_jWi7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bda2e364.mp4?token=HOjbBvYodLMS1JUiSqIbM6N6S5rvBUtf5A8dDkh1Ir-o2fkc_Q_XJiGH2XTZyIKphnrPFeGjMo2IjLY5XB370U0I86kTByUzJVPIdEvblHNtky8h-_B17vk4jqBry_siGcP-YdrqMk7X4hR2DitOKOTIePTfiz63tnzrmYPwHmmJayyJ6pj68I-B55Pzcc75-JKgyL0NxJUFCYEktN-cym9YH41E1psXX5cbr4xjqFzcClIgyis08LMsQ9Ao84UEJynzrIJdJXAbVkxwBP-D6iEjN6Hw6IJxFwDwylwHNDePCVMGKfXSnBmFw07Hqb9-FjZGPGhyP8NHjsR_jWi7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: شنای پروانه
🔹
ژانر: اجتماعی، درام، جنایی
🔹
فیلمی که با انتشار یک ویدئوی جنجالی شروع می‌شود و در مسیری پرالتهاب به پایان می‌رسد. این اثر اجتماعی که با نقش‌آفرینی بازیگرانی چون جواد عزتی، امیر آقایی و مه‌لقا باقری همراه است، یکی از جدی‌ترین تجربه‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677436" target="_blank">📅 21:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVzzi_rr90FPW46iI2tGJyUvJuNcS7VdgdqDuCvqg-tUBA3yazpuY-D0OslmGlnN4u6Y3X0W5-22-BKbZ0szBTabfDgrW2DuZ5yEibhwDkXPzV3rUzQnqU-9BCKnt1-fmjzsOYPDtkcOOoumEMSjwepezc_X9BZxZHS9oG9rf2bHS-C_ciEsW6OytiuPpNTnpcLfeYnC3Tpy4fWLr4zBOBzoOF2LS27FuxH7g7cbxW80AmLBi1L6r-l0mJKK0bdzz47fX0LnMSuBs3d8_pPUjYmrLh6CWlMqz2JFK-iy0j1pNywk4F7X0K7KeLIdiPBIj0pdAOki0cCj0boOV093MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
مشتری راحت‌تر می‌خره، تو بیشتر می‌فروشی!
اسنپ‌بارکد رو که داشته باشی
🛒
هم مدیریت فروشگاهت راحت‌تر می‌شه
💳
هم با فعال کردن خرید قسطی از طریق اسنپ‌پی، مشتری‌های بیشتری رو به خرید ترغیب می‌کنی و فروشت رو افزایش می‌دی.
🚀
همین الان ثبت نام کن
https://snappbarcode.com/snapppay-register</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677435" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677434">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a10bb1e850.mp4?token=v3qZK6ji6jUWYiUKZlABu9WgqUJ3yfS3TxE7PT_gG_b-tKNzYtmv6d5ZBqdQtkfUSmpk30wjKX_kZe7gYFBoLGHYAM15W9o2LL23ZZU1u9QbgAlzhBoQSbKvCqWCWabI9WNFOHqGm6PubnbMV6A437ZViyDQ58v_xBJ1IEeyOP2ig86syO8maMLTZ7SXa8fP_XRKhFZIPVhWYyTjdM1QkoMssOLsguOOLfv6JhnxgXp6dSeCuGWaD3iWtbiw5MCuLWUMB1WcHRfA6r8aGEQ2gFFM1yjbWrgtOv3CBryAJIsGZhZT8EBS1FuGSQQ5enA96lnESjRo0jR01g5AkP7xQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a10bb1e850.mp4?token=v3qZK6ji6jUWYiUKZlABu9WgqUJ3yfS3TxE7PT_gG_b-tKNzYtmv6d5ZBqdQtkfUSmpk30wjKX_kZe7gYFBoLGHYAM15W9o2LL23ZZU1u9QbgAlzhBoQSbKvCqWCWabI9WNFOHqGm6PubnbMV6A437ZViyDQ58v_xBJ1IEeyOP2ig86syO8maMLTZ7SXa8fP_XRKhFZIPVhWYyTjdM1QkoMssOLsguOOLfv6JhnxgXp6dSeCuGWaD3iWtbiw5MCuLWUMB1WcHRfA6r8aGEQ2gFFM1yjbWrgtOv3CBryAJIsGZhZT8EBS1FuGSQQ5enA96lnESjRo0jR01g5AkP7xQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۳ عبری به نقل از مقامات ارشد:
آنها انتظار دارند ترامپ دستور از سرگیری درگیری ها را صادر کند و ساعات آینده را بسیار سخت توصیف می کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/677434" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677433">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
‏رسانه‌های سعودی: اردن به عراق اطلاع داده که حشدالشعبی قصد حمله به خاک اردن را دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677433" target="_blank">📅 20:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677432">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
لو رفتنِ ادامه داستان سریال بامداد خمار؟! درگیری‌ها بر سر فیلمنامه سریال بالا گرفت!
🔹
سریال «بامداد خمار» به کارگردانی نرگس آبیار در روزهای اخیر با حاشیه‌هایی درباره اتهام سرقت ادبی مواجه شده و گروهی از نویسندگان ادعا کردند که نسخه اصلی و اولیه سریال توسط آن‌ها نوشته شده است.
🔹
همه این‌ها درحالی‌ است که تیم فعلی سازندگان در مصاحبه‌ها اعلام کردند فیلم‌نامه اولیه کنار گذاشته شده و سریال بر اساس متنی جدید ساخته شده. این تیم همچنین نام تیم نویسندگان اولیه را از تیتراژ سریال حذف کرده است.
🔹
مهدی آگاه‌منش، یکی از نویسندگان اولیه سریال در مصاحبه اخیرش با تبسم کشاورز در رسانه برنا گفته که حقوق معنوی نویسندگان اولیه مورد توجه قرار نگرفته است. این نویسنده برای اثبات صحت ادعای خود مدعی شده است که در ادامه سریال اتفاقاتی مانند مرگ برخی شخصیت‌های مهم خانواده، خودسوزی خجسته، حمله اصلان با قزاق‌ها به خانواده بصیر و همچنین بخش‌های زیادی از قصه‌ها که در ادامه سریال رخ می‌دهد نیز در فیلمنامه گروه نویسندگان اولیه طراحی شده بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/677432" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677431">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326aeee761.mp4?token=IMGRj7IOhBPWxGtyJXOFBC9mpRJghlAVDla5dPFUmrdz8MNPQZIho89aRdYrMGZGP2ZgNDb09GO1bcFXgzcEC61XBov5xFOEGbsIu1Q690YFlmaMsX3XPV9eEeMjx1lv3DEWtFI_jKnhJAZpAqMbrBMOIXQVbgVEo3ttC3qKWBduCOvg0CQ2XVaQwnw_NHx-5qbHlcD_-nxNeiumMVzoVZRHc5M7MKkzDfWXwTx1GF7omhcuElHn7lNid2F4YgH79m_-56qMjWflKzQCBonEc8kdKIB6m0gfEJ-7P_mIr6Lk067q6iW90apC3mspuNcMWau-2RmnVNv_qy6xI8e9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326aeee761.mp4?token=IMGRj7IOhBPWxGtyJXOFBC9mpRJghlAVDla5dPFUmrdz8MNPQZIho89aRdYrMGZGP2ZgNDb09GO1bcFXgzcEC61XBov5xFOEGbsIu1Q690YFlmaMsX3XPV9eEeMjx1lv3DEWtFI_jKnhJAZpAqMbrBMOIXQVbgVEo3ttC3qKWBduCOvg0CQ2XVaQwnw_NHx-5qbHlcD_-nxNeiumMVzoVZRHc5M7MKkzDfWXwTx1GF7omhcuElHn7lNid2F4YgH79m_-56qMjWflKzQCBonEc8kdKIB6m0gfEJ-7P_mIr6Lk067q6iW90apC3mspuNcMWau-2RmnVNv_qy6xI8e9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلتنگی خواهر شهید آرین زارعی برای برادر شهیدش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/677431" target="_blank">📅 20:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677430">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQvcZAeYaDP65lgZdQNWSOQBUmQTxxjMDwJ3Zb1trLIKXPYlobkjznHIUhx6PlX687ALIZFZqFAZH61eo6PfFrS4Np9LwQhNOGutFy-uJ3sugMdda5hoVxr26vDm0-Gd3pwKy5B9eHwrkl8dezs5XFL_sdFtvL2GxY3rxoyBP1Uw-BYtxNbl1VDwyGdefmMjoCNpyEETYp3mQS1g5LaSPdxJlgYC6e0VrRzWWIrUR5A6XLLOOjZJmHFVVqvhsynxftr27vg68ncUFWsE46tPYjomTlKZCkwmNASAaUk_oasJUJZ7G-T8_bfZmfj6w-JhjBHy7J1hn8B0zgP96ZaKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سروش صحت و پسرش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677430" target="_blank">📅 20:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4LSMzTam9gGreHxXKo1vS2yqD5k0FPpsOyFoHyjO3UOh5-q6LGJRhk-bUb1dKjcoOMFh9My_lhbNoA2czbt66Sx7f_eqjycC-qpI8VQdibsakr3_RLrbKTXiS_HJX9f7xAFZbnF8fSumYXtHlyF5e7cU7Y-8gt1LU1tT67GeLFLBXy6Db_ulrslk7ZUB2lxcZBavm0fxx-yqzuRyme_456R-dg9MYXd25t58cYyZlruD-ZwxC_1-SR0qLI_89MkAcFCDuLNMV5vHCGuPJSM_fb6y9uMdlNqnHYyyrv_Qw3w59pZvjBzfsT8SeUo5egoh_iOFa35Omh8Sji4xJDB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9MWOiJLKEJ3LFItQ7fTZZ84rwLH0CVFlbDbePoim1zUH_wQ6ILZ3Rsfxn3aaQJeHwrG9r5SfFK1ACMBd5uU9u5zHBz4u7kUxa5SmOXtTDoJ1c5t81bEEt7J06qz75Bm1gTyttxX8oC30BmEr4-3zj6qWykgFDCEJRG37FXhPRXpFo6-vcR6TTtMAjXIL0g3qsy3vFPZIm3i7LJ4mgqrXpIrDlNU9LFIc7Md1JU2JEl7lf0-C3-rqPPhTY60VOYBby_YQwGRc1iguN5yHbHOPt3y2IvWB6tN_XRDZEkDaIeQoTRGV0HnI1sOZd5wyT_5IH-RBOUBkdqjiqMtJIopyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کیف عجیب شرکت Coperni که با استفاده از کپک پرورش‌ و ساخته شده
!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677428" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ماجرایی تلخ؛ جنگل‌های جنوب کشور در معرض نابودی قرار گرفت
نادرقلی‌ ابراهیمی، عضو کمیسیون کشاورزی و محیط‌زیست مجلس در
#گفتگو
با خبرفوری:
🔹
نفتکش‌ها معمولا بعد از بارگیری نفت در خلیج‌فارس و رساندن آن به مقصد، برای ایجاد توازن در حرکت کشتی به جای نفت، آب بارگیری می‌کنند و مجددا این آب آلوده را در خلیج‌فارس تخلیه می‌کنند.
🔹
جنگل‌های حرا که ارزشمندترین جنگل‌های ساحلی ایران در جنوب ایران محسوب می‌شوند، به همین علت در معرض تخریب و نابودی قرار گرفته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/677427" target="_blank">📅 20:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb333777ee.mp4?token=PTjADOXvr6OKIEw38mu4Bucx38dMirbXsxXGG75VlldZyHCDUcZjE2iQSMGC0RIdp2S9sgZd-wBIdMKBN-CfpoY4Df2Wg-M-e8WlWTwY6KZ6sUfVtBAx1QLy_GKF3kGf5SP7yAmG049Gd3cF4xCrb9H3eMwlHTMvnbNAB-fKNH9bmV0HPJ6n_AU_rCmPiPV2GEXAn8k7b4Kj94aw8Zg2de5gcuasn4x1POiOrMxxhhOEG3JxzX0A2d_iM7lPE-5NMxMPl6SRWLMY_lPLvLftbKRGpMv9R_YksvmjG0UkQ5m1-CCWM0wEhubEGtpebAieAlXTg3sW2nLXk1Nq4UmikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb333777ee.mp4?token=PTjADOXvr6OKIEw38mu4Bucx38dMirbXsxXGG75VlldZyHCDUcZjE2iQSMGC0RIdp2S9sgZd-wBIdMKBN-CfpoY4Df2Wg-M-e8WlWTwY6KZ6sUfVtBAx1QLy_GKF3kGf5SP7yAmG049Gd3cF4xCrb9H3eMwlHTMvnbNAB-fKNH9bmV0HPJ6n_AU_rCmPiPV2GEXAn8k7b4Kj94aw8Zg2de5gcuasn4x1POiOrMxxhhOEG3JxzX0A2d_iM7lPE-5NMxMPl6SRWLMY_lPLvLftbKRGpMv9R_YksvmjG0UkQ5m1-CCWM0wEhubEGtpebAieAlXTg3sW2nLXk1Nq4UmikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگنده های آمریکایی به حریم هوایی استان نینوا در عراق نفوذ کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/677426" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6JDjEOvEuRq3HropVWzQ0FHpjSR5p9Z3sVJf3oTYjoBQyXQIH4h6vZsAhPzt13uYGrVimQ3Xz0DkXGC6G5w1D7mWaTqpoTbu9pL21NUwdfITUn-8AMVQCyhQN91G81R6Y2JBIK1dbNHeYPgqfAzcidmHzGCnM7E7LXoknjsEFK9yvcoIk3wp38UI6yogunReageLL1SxKKE18zob5nxxfLhenR49YJnxj-bhz3Dcb1abtVGEch_vAKrer_ZBCZRZXJGFofGm6TU1JEhhWekjL_yUGni7FhVop3lPhrmsQFPT0PeQvm_vDl9eZ4Dx47KJdDTgZjIVbJOlBVbtDYtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
گاهی احترام به نذری، یعنی فقط به اندازه نیاز برداریم؛
شاید سهم اضافه‌ای که رد می‌کنیم، چند قدم بعد به دست زائری خسته برسد.
نعمت را هدر ندهیم؛ پشت هر وعده، نیت خیر و زحمت زیادی است.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/677425" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb54cd03b6.mp4?token=YZFLhG__O7QyJgpk0va9twrIBsa3ffU7bKwxMKh6GcL98CuhKo1dpHdHMwlSzvnZFKResNl7zxrHS4TewOQvjDU2NJGd40gQrj3rp4ivokOP1K80djqgDIzUo1bPbaqlEkN8SfWjciDuKLljtdCvYL5b55WnEHMBjI35ouU01Wz4bQ5e8GkYHJJ7x3Q9HSVduuExwKB8u8ZuMRFMxIf50nVzUL2QuVIxj-bO590jDVJ5ROCEhu_tJz9NqOVIYQFXzCYQ85mAQ1w3IQpTL3N--VLihtKAYLx3aLKLbdWok9i5z8G8-_z3LP9FFw7weO3bZ1y3VwXIG4Vtk86IspA6-IT3lXXU6EhI_kM5VRXtKfRAUZtbgzzQYaZWiuFT_UEgZLVb690D3zCc3uIWoid06PRCAFAjyfWwAsUUc2Ug81aBx1WeeweGWz0HofNVkmLZTj1hRAwkZWqan9rtr2xrzP2NRZKCHeUEY0mdchYCk2plpCy243QIl02avgea-7PPviUzaosv4zWTd7yPfz4Q_9JI2GCV7iea_atPEHfLpYrn6eKLYq7m0r_MCAjNCuszY8d-KPDwaERPYqxPccI1aIfG97LHITxh1Ss0Wcju0WEIVtWC32A2EyHthYuV1tegeJ2r5PIgNCQrzrdjlpJWZsE1Zvt02tOFqf91wQX6ifE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb54cd03b6.mp4?token=YZFLhG__O7QyJgpk0va9twrIBsa3ffU7bKwxMKh6GcL98CuhKo1dpHdHMwlSzvnZFKResNl7zxrHS4TewOQvjDU2NJGd40gQrj3rp4ivokOP1K80djqgDIzUo1bPbaqlEkN8SfWjciDuKLljtdCvYL5b55WnEHMBjI35ouU01Wz4bQ5e8GkYHJJ7x3Q9HSVduuExwKB8u8ZuMRFMxIf50nVzUL2QuVIxj-bO590jDVJ5ROCEhu_tJz9NqOVIYQFXzCYQ85mAQ1w3IQpTL3N--VLihtKAYLx3aLKLbdWok9i5z8G8-_z3LP9FFw7weO3bZ1y3VwXIG4Vtk86IspA6-IT3lXXU6EhI_kM5VRXtKfRAUZtbgzzQYaZWiuFT_UEgZLVb690D3zCc3uIWoid06PRCAFAjyfWwAsUUc2Ug81aBx1WeeweGWz0HofNVkmLZTj1hRAwkZWqan9rtr2xrzP2NRZKCHeUEY0mdchYCk2plpCy243QIl02avgea-7PPviUzaosv4zWTd7yPfz4Q_9JI2GCV7iea_atPEHfLpYrn6eKLYq7m0r_MCAjNCuszY8d-KPDwaERPYqxPccI1aIfG97LHITxh1Ss0Wcju0WEIVtWC32A2EyHthYuV1tegeJ2r5PIgNCQrzrdjlpJWZsE1Zvt02tOFqf91wQX6ifE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتباطات اربعین از پشت میز بررسی نشد
🔹
این‌بار کیفیت ارتباطات اربعین نه با نمودار و گزارش، بلکه در دل جاده‌ها و میان زائران سنجیده شد... از مسیرهای منتهی به مرزهای خسروی و مهران تا جاده نجف به کربلا.
🔹
تماس‌ها برقرار می‌ماند؟ اینترنت در شلوغ‌ترین نقاط پاسخ می‌دهد؟ شبکه در لحظه‌های اوج تردد پایدار است؟ پاسخ این پرسش‌ها از همان جایی جست‌وجو شد که مردم آن را تجربه می‌کنند.
🔹
با حضور وزیر ارتباطات ۲۸۴ پروژه ارتباطی در کرمانشاه و ایلام با بیش از ۳ هزار میلیارد تومان سرمایه‌گذاری به بهره‌برداری رسید. این پروژه‌ها برای تقویت پوشش، توسعه ارتباطات روستایی، گسترش فیبر نوری و افزایش پایداری شبکه در مسیر زائران بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/677424" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
‏
رسانه‌های سعودی: اردن به عراق اطلاع داده که حشدالشعبی قصد حمله به خاک اردن را دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/677423" target="_blank">📅 20:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677421">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f3be03e3.mp4?token=IB6kMolEfeB0JVgQ5Hs6MGK_qNRSdJnLvRlaGXeEjv-UFCfW_5UGgqq1My99XVyxl8CHhtl7wb6EnhKiWQAmecE4CUNlaJ0qXG6NOBe6LKATZaxAyt4VcmkzTYKgCHt26y8WVt6OMwXacMUlLX7XHzZLliJCexuQJ2bdLVoQy9eJSpUurEECbk6_j_NYwljYqUdB1AkqwqZS3FPCiYpfkjLGX1bGOdhtd6f9JxYbf_bt6jSSWu0QOlWE6NNoeRTFYsPZVoy34xtxlR4a16ATfYjW3G-Oi6hWZIK-viGdu5GM1gmIAZnymm3Q-lzGxj4dnY_DAHAciLhgKY7gVsovRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f3be03e3.mp4?token=IB6kMolEfeB0JVgQ5Hs6MGK_qNRSdJnLvRlaGXeEjv-UFCfW_5UGgqq1My99XVyxl8CHhtl7wb6EnhKiWQAmecE4CUNlaJ0qXG6NOBe6LKATZaxAyt4VcmkzTYKgCHt26y8WVt6OMwXacMUlLX7XHzZLliJCexuQJ2bdLVoQy9eJSpUurEECbk6_j_NYwljYqUdB1AkqwqZS3FPCiYpfkjLGX1bGOdhtd6f9JxYbf_bt6jSSWu0QOlWE6NNoeRTFYsPZVoy34xtxlR4a16ATfYjW3G-Oi6hWZIK-viGdu5GM1gmIAZnymm3Q-lzGxj4dnY_DAHAciLhgKY7gVsovRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمامی موکب‌ها در مرز شلمچه تا یک هفته بعد از اربعین آماده خدمت‌رسانی به زوار هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/677421" target="_blank">📅 20:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22841a66a2.mp4?token=HHwC_D8bmXHqZ6T_6oUDeuAHdmnsj112hA4mBsX-Hxx6trzQuVKYegcmEtTRSwj2wd_WtoGh79rw-ZAKZH_amerIJ70055Bg5gokWcD3uqosyjrk2PhQjxjJUPfZiGGL1EljnThNM-feWuiHRDUbDwNDY6QlGMoYU0cmReSMw8Mj5SN8YlNCE2qFzwEOSZvOj_5KDlvMbJzxInhsh75LIltk1Oq7S0K-SjBdd0YeXIn9A9a5BCtmQ50H4SCQOLzb3JA9Xx9NyfzHtJjLji8rkvIZ9RtmfQh1p18OpMJ-TeEA7X3_f8Zyb9BPxonOUVsIE_giw99DC8ao80ykESqNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22841a66a2.mp4?token=HHwC_D8bmXHqZ6T_6oUDeuAHdmnsj112hA4mBsX-Hxx6trzQuVKYegcmEtTRSwj2wd_WtoGh79rw-ZAKZH_amerIJ70055Bg5gokWcD3uqosyjrk2PhQjxjJUPfZiGGL1EljnThNM-feWuiHRDUbDwNDY6QlGMoYU0cmReSMw8Mj5SN8YlNCE2qFzwEOSZvOj_5KDlvMbJzxInhsh75LIltk1Oq7S0K-SjBdd0YeXIn9A9a5BCtmQ50H4SCQOLzb3JA9Xx9NyfzHtJjLji8rkvIZ9RtmfQh1p18OpMJ-TeEA7X3_f8Zyb9BPxonOUVsIE_giw99DC8ao80ykESqNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جالبه بدونین ۱۰۰ کالری از هر ماده غذایی چقدر میشه
؟
🔹
رژیم گرفتن راحته فقط کافیه کالری هر مواد غذایی و خوراکی رو بدونید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677420" target="_blank">📅 20:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
هر ۱۰۰ درصد رشدِ دلار، ۱۲۱ درصد خودرو را گران می‌کند
🔹
نتایج یک پژوهش با استفاده از مدل ARDL نشان می‌دهد در بازه زمانی ۱۳۹۲ تا ۱۴۰۳، نرخ ارز مهم‌ترین عامل اثرگذار بر قیمت خودروهای داخلی در بازار بوده است.
🔹
بر اساس این تحقیق، ضریب اثرگذاری نرخ ارز بر قیمت بازار خودرو ۱.۲۱ برآورد شده است. یعنی به ازای هر ۱۰۰ درصد افزایش نرخ ارز، قیمت خودرو در بازار به طور میانگین ۱۲۱ درصد افزایش پیدا کرده است.
🔹
افزایش ۱۰۰ درصدی قیمت مصوب خودرو هم تنها حدود ۳۲ درصد قیمت بازار خودرو را افزایش داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677419" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677418">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=f8LyPd5ytM3FO_yXncLRXFcMWKNpBSRkEuU7zCNKsSVncfIRdNOC_xGb0YVJWWgoFcidA507eOwmKsM3QobB8rWfIqQYNBl0sy6YJFXeEzgTEHBBBDiqsdqj4aVwA0jnJQzZkkIEkdtS48EdBPGDTqhx-w8mmA6TQ3p1lXQ2w36pYiGpL7W5XLwLXmD56Mn8UTkttrCYMLAR_1CM6hLUWdABotSRFKRU7_BRa81CFJQ-rMINL22M16neGFzzbgY-mBKhbYlldOHoHIofpBS5SXhBAqdbVCgLObTjMtVm6gRzUbDgXnG3zYMw1vFzCGxJQ87idCkmc4p2DI_8yGbQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=f8LyPd5ytM3FO_yXncLRXFcMWKNpBSRkEuU7zCNKsSVncfIRdNOC_xGb0YVJWWgoFcidA507eOwmKsM3QobB8rWfIqQYNBl0sy6YJFXeEzgTEHBBBDiqsdqj4aVwA0jnJQzZkkIEkdtS48EdBPGDTqhx-w8mmA6TQ3p1lXQ2w36pYiGpL7W5XLwLXmD56Mn8UTkttrCYMLAR_1CM6hLUWdABotSRFKRU7_BRa81CFJQ-rMINL22M16neGFzzbgY-mBKhbYlldOHoHIofpBS5SXhBAqdbVCgLObTjMtVm6gRzUbDgXnG3zYMw1vFzCGxJQ87idCkmc4p2DI_8yGbQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز ژاپن و آمریکا بالاترین سطح والیبال جهان رو بازی کردن
🔹
این وسط در ست پنجم یکی از عجیب‌ترین رالی‌های تاریخ والیبال هم رقم خورد
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677418" target="_blank">📅 20:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAr5LSwvpCBTEjAEA3uxnA-5mCuq8raIKjv8rx1oKccfU9rKbIjyq48_iXT_mnzS3Z7BX5mH95eDNU3ZEAA9eHyaS2oSnr4LL4D6m2HkssQO-9M6BxjXv5CMqFXIWxMj8fgAGFnniKvHgBc6AeKXhkUe7h2Ah0m7_STAuBWF7PxiBNS8LmQD6o2kRS8Ki-GRMecDdBda3sqGDQdIZkbyJa6jGNpocJQuRNacb1NxNUQDgURB6BMx6TCTv0QdfBKJeJ0g0Z75SJINOIJ7Gw1De8PMsAjstLg4V-MaNp6kiUvvdVkQF9hhbpCHTH18wV6PVhIeq3QUqFTqhjCocPRJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فضه سادات حسینی، مجری تلویزیون پس از سفر به کربلا: داشتن ایران قوی هم مصداق خون‌خواهی رهبر شهید است؛ زمینه‌ساز ظهور شویم
🔹
حسینی درباره سفر زیارتی اربعین همراه با کاروان اهالی هنر و رسانه: این فضایی که عده‌ای از فیلمسازان، مجریان و برنامه‌سازان در کنار هم قرار گرفته‌اند، می‌تواند خروجی‌های بسیار خوبی برای اربعین داشته باشد. من چند بار دیگر هم توفیق داشتم که با بچه‌های رسانه به اربعین بیایم.
🔹
شاید در شرایط عادی در تهران نتوانم این تعداد مدیر فرهنگی، مدیر سینمایی و افراد مختلف را یکجا ببینم، اما اینجا می‌شود ارتباطات زیادی برقرار کرد. اگر کسی طرح، ایده یا نکته‌ای داشته باشد، می‌تواند از این طریق مسائلش را پیش ببرد، کار کند و نکاتش را بگوید. مثلاً بگوید من ایده برنامه‌سازی دارم یا ایده فلان کار را دارم.
🔹
حضور در چنین کاروانی موجب هم‌افزایی، همبستگی و ارتباط است. غیر از اینکه خودمان می‌توانیم تولید محتوای شخصی انجام دهیم، می‌شود با افراد مختلف، مدیران، خبرنگاران و برنامه‌سازان ارتباط گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677417" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPlU-SDlsS2S210Qzuqk2STllryqZsBT5-njddhXa4-xxhi6ziszu4TOVZVKSa746nmFOOtaQu8FS5m1GeyALZVZ8GFrEVpTS-6b9KUvcjMJuIISV5Hkl9k2i5Pf1Jpu3KScMHsBGK5NzqDL75EobnL7f-4sizKZn6MKNZAsLC4KG-nhNxLDQf5qd3Jnl9k1aKbZCZfpUMZ42zV9AR6cR1nSEx5mVLT8f_ZpFMp0S_59YGgwmwInthBIfYDR_2u6t482AbyhV4D7wmeWjcvpgvt6U8nStPqXFJbruAuDfpKIZNuK9ZuGcfCSKS7MmFzafGn_5XX1ensLcuFQNdSxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت عجیب کاخ سفید: خداوند سربازان ما را حفظ کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677416" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303ffade53.mp4?token=v2gO57Mqixhd3eZOlQxr3TRfniVwcw0njYIs3_7EZmJ_nx-iISW9JV72gKttIZ77rlGXrsdPksI1UQcMXCK8OsmsagIGIDOcj0zrA2qv7G-PQz23NF-RZ2VcytZCPDHwpMwW6_PvnfFMe9C0o_DhNlS6SiE2cBYXVcMGKxvrYT-btKom1-3PjSQfE4-W86vlkUx508ZDN0lvdg5a475iOLYiL0tO2v-PtvrZG0r9aL3oW85Y5gMrG3ezq-pb-9HO-l0zaw3L2fVt_p22r5jHtx5DlzwdI8rrKQxuYdFuwvXfyx4-6txBnhrQ2XPmaD7Axaj9pJIdUwSXNMTBEmcJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303ffade53.mp4?token=v2gO57Mqixhd3eZOlQxr3TRfniVwcw0njYIs3_7EZmJ_nx-iISW9JV72gKttIZ77rlGXrsdPksI1UQcMXCK8OsmsagIGIDOcj0zrA2qv7G-PQz23NF-RZ2VcytZCPDHwpMwW6_PvnfFMe9C0o_DhNlS6SiE2cBYXVcMGKxvrYT-btKom1-3PjSQfE4-W86vlkUx508ZDN0lvdg5a475iOLYiL0tO2v-PtvrZG0r9aL3oW85Y5gMrG3ezq-pb-9HO-l0zaw3L2fVt_p22r5jHtx5DlzwdI8rrKQxuYdFuwvXfyx4-6txBnhrQ2XPmaD7Axaj9pJIdUwSXNMTBEmcJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتی قبل در پی آتش سوزی گسترده در یک پالایشگاه نفت در اربیل، فعالیت این پالایشگاه متوقف شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677415" target="_blank">📅 20:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbD_qEpumLkSdCdS4gUECY2-jzKPs3Sr-DtujQjZVpadj3fdOittH-x7kOlwN3K686rB6iGn2NPAkWF9GvrGf5Mt40Y7UBnxeGB1MdqC51KfCQAqVDFjIOlKl7QzdUB4yGcfWLhtGVVHvshYffBSB-vQ9xrqNmTto-fF-HeDVchR6qb_JJImzULzpjKe3in_LItlpfkk38zNp5LlB_sMqKV8PzMnGsOxEqr1JjmrvlAvMuOsXxHMgeJwIAde_1cjRmLnql1-CXiqhsB-vsdsZnJPQ2BdpQiV-DtxJBmVIk3gJX6tfOOdBKl2ECP90M3757fgqRCAXT38mr-pMI5BPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/677414" target="_blank">📅 20:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9177878898.mp4?token=q9kl9syR4ebzfNU-D8Znw0PFYB5x7k_FHow0Xt_70235WAwsW3SNMuCBtiL0Ow3gVv9NCXDttZgOEjOM6VIfqS52ITmNT8fBogyHBHK0c77SF2UJtH7LYCIsFEQKAs6-M0PHT5lyN3bMZjjayGqdb4a_mitBg3ZcSpLALdCTSUFxUW6j0zhA296pQPFUJ4MCg5kjheUYwUsWSt8ebRJwuPkI1YGpXNZLLa_sbZknDXeGFDYUn_Y7wIUICixQvPr0UatsoWtWrPBpMXN7kDMWnKYYf10I2RV5WIEcQyuFkpiUwThwXT8MPPDXa7ZDtHRYmkKcC6FPfXU67eqRmc2WMpfNhmX5UeSfZFY9HZd7CQzwIyy0p7hqs1rI2toZGSQwW6b5kFIMU77zfArKfh75JSzj03XykTa6dyRYRiAitMnl18gGvbxf7sdCNyoNqt1Ti-BWcm_ExHmNnlp2jSxqYefny4zW_Drj7bVKgRqqfez21IwP2iSxAt0k87KZ-B4gK07-nvMoR4Kxc8rlmCfGLfa3bEaUwWo3Yr6dtNdRA_p4V3gXUJYdNPPPg-kJLrdO1rq8ZS0SKbp9AaPnNck7IJtQsVi6_SJ994OmUAHO_anezJAH2MkoeqOJgkWeW4bKMJUA3_lWMKxvKMgam2hrdZd_OXOHvm2THLH5I_aiWFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9177878898.mp4?token=q9kl9syR4ebzfNU-D8Znw0PFYB5x7k_FHow0Xt_70235WAwsW3SNMuCBtiL0Ow3gVv9NCXDttZgOEjOM6VIfqS52ITmNT8fBogyHBHK0c77SF2UJtH7LYCIsFEQKAs6-M0PHT5lyN3bMZjjayGqdb4a_mitBg3ZcSpLALdCTSUFxUW6j0zhA296pQPFUJ4MCg5kjheUYwUsWSt8ebRJwuPkI1YGpXNZLLa_sbZknDXeGFDYUn_Y7wIUICixQvPr0UatsoWtWrPBpMXN7kDMWnKYYf10I2RV5WIEcQyuFkpiUwThwXT8MPPDXa7ZDtHRYmkKcC6FPfXU67eqRmc2WMpfNhmX5UeSfZFY9HZd7CQzwIyy0p7hqs1rI2toZGSQwW6b5kFIMU77zfArKfh75JSzj03XykTa6dyRYRiAitMnl18gGvbxf7sdCNyoNqt1Ti-BWcm_ExHmNnlp2jSxqYefny4zW_Drj7bVKgRqqfez21IwP2iSxAt0k87KZ-B4gK07-nvMoR4Kxc8rlmCfGLfa3bEaUwWo3Yr6dtNdRA_p4V3gXUJYdNPPPg-kJLrdO1rq8ZS0SKbp9AaPnNck7IJtQsVi6_SJ994OmUAHO_anezJAH2MkoeqOJgkWeW4bKMJUA3_lWMKxvKMgam2hrdZd_OXOHvm2THLH5I_aiWFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که خوک هار دقایقی قبل از حضور در یک پایگاه نظامی در نیوجرسی منتشر کرد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/677413" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4WnQdJho5tuh8QvAS0OYa38FbhC4E1nvH4JV9P4qg7UdQPgTjEbQg4O0xvbMDCNxIGhcquiAB8zja5YdrWLlFgxZUtRJsPyeIAf0V9bIoB_Az_8fz3z4kicNTBAeIXe1QH6RQREa1gy8-TNo3ciFWYF0FX3hcE8yV9TEWtFAlcK0nz-EVuVtcpEl-TYl8aLkdYzinF_oD57klztkn3KbAoxESKTKjqXajL17d_RG6Luyn8juuLwyOk4NlfuKLnak4crVAGEO3fLmK6VXa6hZMumUUnzUFg4ZJ1g9f1JoAJK0anOjzEwIQu-DIWWuieQDFqFOyc7ePyoby37QsejZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoTXfOL3DJ1Qx3pLxPylQgmZfZLvvZoRRgGtp5eQjMF0_JVXNI9y9ctsaZrdvA8OKEKyFbYCfYvfaiaXKxqUw7N8I-7gwhsUkR7UHflO_ETNX28DXul7r_pAIIfvZUHDN4eRpny5K761b8ZBuFEKvy2CgFXsYAYQJjEO4rbLBACIV71aTjgc7V6RGydv-mx32DGtKKUw7-_anIZdTTcD2A5tI2hIacra58aWcnJ1K2dPpXDAWovOECxXtV1y5axnFpfS3_2eJ5SSoqFmic1dyQWFrMOkjaG5OWv7dNoMJjJj8vz7g9jcpJN1MXzrfKggwkErmzZpn8vYXyXIGDAu5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بعضی خانواده‌ها گذشته‌شان را زندگی نمی‌کنند؛ بارها و بارها تکرارش می‌کنند
🔹
«صد سال تنهایی» داستان خاندان بوئندیاست؛ نسلی گرفتار عشق، قدرت، جنگ، فراموشی و تنهایی در شهر افسانه‌ای ماکوندو.مارکز در این رمان، واقعیت و خیال را چنان درهم می‌آمیزد که عجیب‌ترین اتفاق‌ها کاملاً طبیعی به نظر می‌رسند.
🔹
کتابی برای کسانی که دوست دارند در یک جهان جادویی گم شوند و بعد از تمام‌شدنش، مدت‌ها به سرنوشت آدم‌هایش فکر کنند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677411" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7c9bf91d.mp4?token=YSPAu9l5kR8TvD6PNMiMwWY2rNC6dj9sOWMbniaFAvmXULHX9rO6vy606Vb9uZXSQUBKMvS4iOyf6ZROsrMvabskmNQU_Fy8hXZyRlDiEQaAbm8TjZo0O36XjCoA82ac5gyYGcBE6JnKgKte2XQSzX1osFT1A60RFlrZPcsGt-iwKHdyhdOUGa96yk9LyMac38vznD4ULuiVDShI19WUeKonkz6ye1ago1NeaVkI4CWiZ715fSLWjy2ewf2Nf0kVpfgR7g4gS6VL-byT1nCc1U9J87sf-Q9TK2oa63oF6QrlLKBaKqg5i3wg1vJ5BRoSfsFkjPYcIMwF6SydGRqb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7c9bf91d.mp4?token=YSPAu9l5kR8TvD6PNMiMwWY2rNC6dj9sOWMbniaFAvmXULHX9rO6vy606Vb9uZXSQUBKMvS4iOyf6ZROsrMvabskmNQU_Fy8hXZyRlDiEQaAbm8TjZo0O36XjCoA82ac5gyYGcBE6JnKgKte2XQSzX1osFT1A60RFlrZPcsGt-iwKHdyhdOUGa96yk9LyMac38vznD4ULuiVDShI19WUeKonkz6ye1ago1NeaVkI4CWiZ715fSLWjy2ewf2Nf0kVpfgR7g4gS6VL-byT1nCc1U9J87sf-Q9TK2oa63oF6QrlLKBaKqg5i3wg1vJ5BRoSfsFkjPYcIMwF6SydGRqb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها: این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677410" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677409">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f18f8b8e2.mp4?token=o2RZogi2nl1JgzJRAQ48JON8S0S0Kv2JyAHxlY_3bp2VXPXbVUF6RPoTDA-MJeeVUvh-WolATXDosW_XdejJts5eKGrfn37Qjj_fRg2kcYCqSuMt2cACkqiXxa3TzqCBlpUKTFUt5jO1O8p8eRLhZRvIHVaJsRgPsQoxDEvtCvmZey0rL1lKIe2TDqWePTcGpW48hC5ZKdS8yYikUZPGyIws1R1kD4OTcS43ML5B40ijWXpQ4o7-wCaQDDEETEpOWtmNNzOU755RrrkyLKLDTM54xAK9r772IeYuXUIbqp7m5RmM84us7zXgLhyd4wPWvKR5LIn7pKqEsi3I4mEQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f18f8b8e2.mp4?token=o2RZogi2nl1JgzJRAQ48JON8S0S0Kv2JyAHxlY_3bp2VXPXbVUF6RPoTDA-MJeeVUvh-WolATXDosW_XdejJts5eKGrfn37Qjj_fRg2kcYCqSuMt2cACkqiXxa3TzqCBlpUKTFUt5jO1O8p8eRLhZRvIHVaJsRgPsQoxDEvtCvmZey0rL1lKIe2TDqWePTcGpW48hC5ZKdS8yYikUZPGyIws1R1kD4OTcS43ML5B40ijWXpQ4o7-wCaQDDEETEpOWtmNNzOU755RrrkyLKLDTM54xAK9r772IeYuXUIbqp7m5RmM84us7zXgLhyd4wPWvKR5LIn7pKqEsi3I4mEQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس نظامی عرب‌زبان: رادارهای اسرائیل توانایی مقابله با همه موشک‌ها و پهپادهای ایران را ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/677409" target="_blank">📅 19:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd2Ldkd_eoEO-JJE5opZff0SItmS9b4ApLMP4WqR-8r2jm13JNE2n2i--Uw36A-LfQsgAAI9WCEipMG-w6hFoaPsDnzGLdIMVKlfrVSOKTw1m9MKlDKw9Amn7nT52ix4IlqMXbTHzKDwcFUmiHaR1QZnRHOrJOG7YkmUnazGe7qbivoMQBlh3urNaeMBOihiAfQrpA1PJE1JNnx4a2A1w1NWC7y99qqCt5LgltDSwDyhRKG0LHNm443Fcw3ROanA88uGPSe2PCjvv_rU3KP-40j9qeJi4vG8WAsRftuKNdDQUI7gXzprEDd-54jLmTpK_v-RnfhMb4rdq2PuWKln8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از رهبر شهید در مسیر اربعین
🔹
اگر در مسیر اربعین هستید و یادی از رهبر شهید در دل دارید، یک پیام صوتی حداکثر ۱۵ ثانیه ای برای خبرفوری ارسال کنید تا صدای ارادت شما نیز در این مسیر ماندگار شود.
🔹
در پیام صوتی خود این جمله را بیان کنید:
«من ... هستم از ... و در این مسیر به نیابت از رهبر شهید قدم برمی‌دارم.»
🔹
منتخبی از پیام های صوتی شما در خبرفوری منتشر خواهد شد.
🔸
پیام صوتی  خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/677406" target="_blank">📅 19:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=gAAWxPuIrxyL5Rn9p9c1kXDkL3x8207P1sdfcKF4wDSpz6yG4UgnRAd7U9sIo8A7eVif6Msbud7kD2GRmMg0CxQLmDL1FFOMm68-RwmnZAAboxnNN0zSZ6kFqGQ5cmqnpzR7FWZZDm8RkU4VHCzVllx9i0CbGEkXJHUOtDSsP5hsVQN0uFWZKbV1RsyNtLJ-Ve1E60sUrGVUJQN5IVnavVSr3fDVqSD4LL6avaUBLSTRpxePd0LbSvblwYIfBgDqff2rWewiF4jvgJDbZHFzb4ohszhq_47MQOdsbCUu3tu2yfH2BQ0DwPkntamng2IPy7Gn0eldoKdkUDbJ0gHzng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=gAAWxPuIrxyL5Rn9p9c1kXDkL3x8207P1sdfcKF4wDSpz6yG4UgnRAd7U9sIo8A7eVif6Msbud7kD2GRmMg0CxQLmDL1FFOMm68-RwmnZAAboxnNN0zSZ6kFqGQ5cmqnpzR7FWZZDm8RkU4VHCzVllx9i0CbGEkXJHUOtDSsP5hsVQN0uFWZKbV1RsyNtLJ-Ve1E60sUrGVUJQN5IVnavVSr3fDVqSD4LL6avaUBLSTRpxePd0LbSvblwYIfBgDqff2rWewiF4jvgJDbZHFzb4ohszhq_47MQOdsbCUu3tu2yfH2BQ0DwPkntamng2IPy7Gn0eldoKdkUDbJ0gHzng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آتش‌سوزی در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/677405" target="_blank">📅 19:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4318LgV6mmqxwsc0VA3XWJaBUBaJhLotHVz3abfxFdCpXEN7wnmupaklWrTqzFNcMoLE_Dx8xf-7fHi058Lu1IjrB3c2-0JAm9J3wrOlv-FMQEpvJt0yo-2aVQQ7RSfzTAaUAgtJN1HD9PiNlSI1e8ozyqmk721bG291XSuRSRRzIlkBjHd86EqFTCgWth4gwMRHIVL0MJOHadLZpT-NvHd2cYzFC4l6q6zGBz5Po0W4VSOHJAPGCo6hAITr-_WaG5dw__t-oO7odPvCgyNE0j3AXQaD8PQKzrKZlQ_nPfDhcBlDiLEbCiNP7aexhl68_BlQhc_o5pOJvrWq10zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاکس‌نیوز هم کم کم علیه ترامپ شد
گاردین:
🔹
کانال خبری کابلی مورد علاقه ترامپ در حال مقابله با جنگ او علیه ایران است. مجریان برجسته فاکس نیوز نگرانی، سردرگمی و ناامیدی خود را در مورد اهداف ایالات متحده در ایران ابراز کرده‌اند.
🔹
این موضوع نشان می‌دهد ترامپ در دنیای رسانه‌های محافظه‌کاری که به حمایت آنها متکی است، به طور فزاینده‌ای در موقعیت خطرناکی قرار دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/677404" target="_blank">📅 19:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
محمد مرندی در مناظره با وکیل آمریکایی در برنامه پیرس مورگان: ده‌ها میلیون نفر از مردم ایران برای تشییع رهبر شهید به خیابان‌ها آمدند؛ خبرنگاران بین‌المللی آنجا بودند؛ نه فقط در ایران، بلکه در عراق هم همینطور. مردم ایران نشان داده‌اند در کنار چه کسی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/677403" target="_blank">📅 19:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_9r_VJEht4_3hzwBKZIthvj9IBfxEhqUnoWJqqYGI5pUXXzaiRRyYFxTXm7JP740BGtHc1nbemkPkEuESy2duCQZISz33E_IWzaVpTa0yJaGnkvNuOPE-inbBlJzclI4htAQRQc9h6243CJ2i1pCPK6cHnkqznJ_OWpVkkmbVjcRblhPTQ6ASgF0VC_Ruvje03XISCDm8jq4ze-TaXe4G4ypplQayy6OI7PPUdA4neRbbqFt3hiStt1cdHcwWQJV2E4gnWVw569bdIXkaXGnOYqWvIItqa4AhpvQZvqUBvV-8Kbu_JfSFXrEIzha-hwTv671xEl6w2iDny9F1EmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
همین الان راهی کربلا شو
‼️
▫️
همین حالا با ارسال عدد «۲» به
۳۰۰۰۱۱۵۲
در پویش «زیارت به نیابت» ثبت نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/677400" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA8i4kZz7DmH9jh4VPMiHJwwEx052Ts9hTeB8prRQFb1_FD5UEhb9tMIPie1sZL8_o4DizQVaHs8aP1htaKth5qvT3Kf650nEbbfSTM5BO5uRrPTsz-RGiF3AXnWhgrVFG80bIBzapE4ZmaUw8-33PWvwJOnxTXC1boIQPVt8mI87jPAhsonSQomjciQY2cO09XP7GRNJkSsLhN8ew0znELl6egxEf_qNnKukanIRkdW41WEpJWWwCMNlECPbBipy-aoaS7hOf2dppoAI2lT4_2J1bPfEOf5UOXcxZqodMdldm4qrg9bXC7AT4i8iUWHu2RJ0IvzMQQiXug3A-XMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنان بیش از مردان زمان خود را در رسانه‌های اجتماعی صرف می‌کنند
🔹
برآورد افکارسنجی بین‌المللی سازمان همکاری و توسعه اقتصادی نشان می‌دهد میانگین ساعات هفتگی استفاده از رسانه‌های اجتماعی توسط دانش‌آموزان دختر ۱۵ ساله بیش از دانش‌آموزان پسر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/677399" target="_blank">📅 19:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a17e0d29.mp4?token=cvxkOz-h4Ja-QzbTbwTqJ6pTJr07XUiI6oBCk1QhJZNKWiYo-CbNfCEkZgRQ216o9N6Z5KscpZ07W0ntCs1FLhacnPE0jx1dIM3ycjP9_gb6LjF8VpDEvZohX-PLNX8awII7ROCABHXROcHKx96nXWy6gSnKCe6jOn1npgZX12JXLrmIZlklhKyBPzdBweqwzhEL0o0i_6jgggOK7i-8-CPhxaXoV3rCnTWNk1L18j6RQqvkaZNGnXObwmK7FAMOxlVvM6ObOSKeUE8v2L5JkQTfGYv6EqtklChAZpWM0Z75ElKx8zgHVwbLznoNdVvkRYQ7mDHbV9bVmW-DbIVk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a17e0d29.mp4?token=cvxkOz-h4Ja-QzbTbwTqJ6pTJr07XUiI6oBCk1QhJZNKWiYo-CbNfCEkZgRQ216o9N6Z5KscpZ07W0ntCs1FLhacnPE0jx1dIM3ycjP9_gb6LjF8VpDEvZohX-PLNX8awII7ROCABHXROcHKx96nXWy6gSnKCe6jOn1npgZX12JXLrmIZlklhKyBPzdBweqwzhEL0o0i_6jgggOK7i-8-CPhxaXoV3rCnTWNk1L18j6RQqvkaZNGnXObwmK7FAMOxlVvM6ObOSKeUE8v2L5JkQTfGYv6EqtklChAZpWM0Z75ElKx8zgHVwbLznoNdVvkRYQ7mDHbV9bVmW-DbIVk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام علی(ع):
شجاع باشید!
مرگ یکــبـار
به سراغتان می‌آید./</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/677398" target="_blank">📅 19:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec6418750.mp4?token=qPkjlVBTVFGI2MbrF21UQjbKyUEeVjfhl25X0V-SmIIg_kvxvSoTvyhZALF4h6pYqlrZpY3pkeQ_u3tb-4UUqKCOkWnt1Y5Qjx1ShaChnMaWzOdcfyoh6zKoNI5Ss_OsXRJkpLzQOJIC-V8gUM5KWr4TvwKlC8WoatR0y5E9WHd5N6wRwQs5pFSBHjqjHJ50nzq_bxZv87j7h_Bn0fWwwyiQHVpYMXRdbjLcSZ4e_Oo15hj5CLChFXQfQn7Qwic8N79si7cawIK5Pq04d2EUmooHBSU4k13ybZEHXWc2xZnBOpV9oMY7puwcoqanYBBtYxZG08IM6zgY5EmHBAZw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec6418750.mp4?token=qPkjlVBTVFGI2MbrF21UQjbKyUEeVjfhl25X0V-SmIIg_kvxvSoTvyhZALF4h6pYqlrZpY3pkeQ_u3tb-4UUqKCOkWnt1Y5Qjx1ShaChnMaWzOdcfyoh6zKoNI5Ss_OsXRJkpLzQOJIC-V8gUM5KWr4TvwKlC8WoatR0y5E9WHd5N6wRwQs5pFSBHjqjHJ50nzq_bxZv87j7h_Bn0fWwwyiQHVpYMXRdbjLcSZ4e_Oo15hj5CLChFXQfQn7Qwic8N79si7cawIK5Pq04d2EUmooHBSU4k13ybZEHXWc2xZnBOpV9oMY7puwcoqanYBBtYxZG08IM6zgY5EmHBAZw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پذیرایی متفاوت از مردم چین در تابستان
🔹
ایستگاه‌های مترو در چین، کولر گازی‌ها را روشن کردند و در گرمای تابستان از مردم به این شیوه پذیرایی می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677396" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفردای اقتصاد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc021471e1.mp4?token=Zc0nG3NvZtmtD-KV9dJ4cR90Z1ZBf5roC1sbP4S_yM6sJCRqWEcnOVskoUpwo3wLVrPjEl4PyMqpdtE-v248D25etOtHXd-EFNj2pd-C570olg0kJSgqydzJajofvenN1Wceca6nypbhH7XmH4BGadd1PvmG447-ycp8L-cUoeJhDcoETPtoNO4Bnspz1bjuH9bfRZ54ryVkcTblCE7jD4twtTRBJikv9ciCJlsSBhb83264DJoB1iOlmNtnFzJw_9cTWRUgg9ZOyk_3VfVNbIAG49heKtPSWSnQUPCwaWjFAwSZT2dhkmfBYkzZG8y1cCl3WcJ4WJhNDuDbAaBzIUjwIb38q_oU0doITIuAkOZ-ZUqEOLLQrSsUAh--_ArMcE2Asxo66tqbmRIn4OPAXz2Lsu5S8YSeNXaeTfPEF726KTwdoyTak3hGmzwZyh4dJ8AZAVQEpCWJ7n4ooFb4LYNQ_FfqvEeCk3x7xASMvF63PgZnhRcANnqT2XjLyM2HFqeoM9rlwwf0s4EAqvRs332daroUF-KTT21GB9D7iQ0cMjqNOEtGaPMljr2fEKI1HCdGGrYI4vmiOI7vQxhui8cgg1O5OxU8UtQoa3Q6NnBmyMaALF7_LNNWPcTjo9ftUBY433rOE4qYf73gidm6OiFTLY9IPa-kkuuFxXSpqt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc021471e1.mp4?token=Zc0nG3NvZtmtD-KV9dJ4cR90Z1ZBf5roC1sbP4S_yM6sJCRqWEcnOVskoUpwo3wLVrPjEl4PyMqpdtE-v248D25etOtHXd-EFNj2pd-C570olg0kJSgqydzJajofvenN1Wceca6nypbhH7XmH4BGadd1PvmG447-ycp8L-cUoeJhDcoETPtoNO4Bnspz1bjuH9bfRZ54ryVkcTblCE7jD4twtTRBJikv9ciCJlsSBhb83264DJoB1iOlmNtnFzJw_9cTWRUgg9ZOyk_3VfVNbIAG49heKtPSWSnQUPCwaWjFAwSZT2dhkmfBYkzZG8y1cCl3WcJ4WJhNDuDbAaBzIUjwIb38q_oU0doITIuAkOZ-ZUqEOLLQrSsUAh--_ArMcE2Asxo66tqbmRIn4OPAXz2Lsu5S8YSeNXaeTfPEF726KTwdoyTak3hGmzwZyh4dJ8AZAVQEpCWJ7n4ooFb4LYNQ_FfqvEeCk3x7xASMvF63PgZnhRcANnqT2XjLyM2HFqeoM9rlwwf0s4EAqvRs332daroUF-KTT21GB9D7iQ0cMjqNOEtGaPMljr2fEKI1HCdGGrYI4vmiOI7vQxhui8cgg1O5OxU8UtQoa3Q6NnBmyMaALF7_LNNWPcTjo9ftUBY433rOE4qYf73gidm6OiFTLY9IPa-kkuuFxXSpqt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز و فردای رمزارزها در ایران با علی خویی، مدیرعامل نوبیتکس
◽️
بازار رمزارز ایران چه وضعیتی دارد؟
◽️
بزرگ‌ترین بحران امنیتی صنعت رمزارز ایران چگونه مدیریت شد؟
◽️
تحریم‌ پلتفرم‌های رمزارزی چقدر دارایی کاربران ایرانی‌ را در معرض خطر قرار داده است؟
◽️
چرا رگولاتوری همچنان بزرگ‌ترین مانع رشد کریپتو در ایران است؟
◽️
درس‌های  ETFهای بیت‌کوین برای اقتصاد ایران
◽️
نوبیتکس؛ چگونه به  زیرساخت مدیریت دارایی‌های دیجیتال تبدیل می‌شود؟⁨
🔗
مشاهده برنامه کامل در وبسایت
🔗
مشاهده برنامه در آپارات
🔗
مشاهده برنامه در یوتیوب
#فردای‌_کریپتو
◻️
رسانه تصویری فردای اقتصاد
⬇️
@Feghtesad</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677395" target="_blank">📅 19:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSmzBAT8k3jwZrzD3S14RCe5tQt3_WQFSzYsxZRa9slOEGkHWvwCBEwZnh-J0c_lSMRlpYFn3AiOCSHGWrsK4vBXFCWUrbkFIWqdU_mFKmTRWMBhoJL4IocPgIX9w6bR4NC9JKDI6uHiOCIErUTef5ijGPiZuE3OR-wozgrbkm9RYmhbCnl4CuA1THQD8sVtBNMpVFH0hW9OxvNyNWmoN4XMAia_nE08lE_HYiKTJ_nvqtqc2QM1gmIaynxFFJvAc_MMMJeju1lYgCRW3ClBYNCutQDc4IvedZyr6QmKsjLnt87vV_isUmhQLTpVoTk3oEd_AduV-iUd7Qfp_4cRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف کتیبه سنگی در دبیرستان انوشیروان دادگر تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/677394" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a6164b25.mp4?token=e2wJeQOVaY5VFTK8oppt0tqgzYpxUuvS9fiQmByqC7cuaU-OHmRfcR1RxzB-Qtq7BOSjGeSDjYUR7vqAfWFRgvNTo74NQEjtkpb2zankwGCFvdirAJeg8XkqmWVyIPpIaY72W8J2UaaVmyWVwqa3OBl8ow8ycNvTyYPYYafCh0v-jWstUI4VjudnwlQ46oEXhL56Ds_03wZWwwC6_LbABEv_AztEptNNkcQoPE2jLUBfIrHyuo0JXLQmOSZBmDf3g-ObGVjFCY2iXUKNRYUHtB1I6RNwSQ84SoN_Gu756v105BDEpAFB_FBVgqSFBbkwq8iBj0U3RXk2aYYaGDu5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a6164b25.mp4?token=e2wJeQOVaY5VFTK8oppt0tqgzYpxUuvS9fiQmByqC7cuaU-OHmRfcR1RxzB-Qtq7BOSjGeSDjYUR7vqAfWFRgvNTo74NQEjtkpb2zankwGCFvdirAJeg8XkqmWVyIPpIaY72W8J2UaaVmyWVwqa3OBl8ow8ycNvTyYPYYafCh0v-jWstUI4VjudnwlQ46oEXhL56Ds_03wZWwwC6_LbABEv_AztEptNNkcQoPE2jLUBfIrHyuo0JXLQmOSZBmDf3g-ObGVjFCY2iXUKNRYUHtB1I6RNwSQ84SoN_Gu756v105BDEpAFB_FBVgqSFBbkwq8iBj0U3RXk2aYYaGDu5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاشیدن اسپری فلفل بر صورت کارگران فلسطینی از سوی صهیونیست‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677393" target="_blank">📅 19:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حاکم بحرین خطاب به ایران: حضرت محمد(ص) پس‌از قرن‌ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگر به بحرین حمله نکنید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677392" target="_blank">📅 19:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تولید صنعت طلای کشور در یک سال ۴۵ درصد کم شد
نادر بذرافشان، رئیس اتحادیه فروشندگان و سازندگان طلا و جواهر تهران در
#گفتگو
با خبرفوری:
🔹
رواج خرید و فروش طلای دست دوم و طلای آب شده، در کنار افزایش قیمت جهانی و داخلی طلا باعث شده تولید صنعت طلا در کشور طی یک سال گذشته ۴۵ درصد کاهش پیدا کند.
🔹
ادامه این روند باعث شده برخی واحدهای تولیدی با یک سوم ظرفیت فعالیت کنند و تعدادی نیز به دلیل افزایش هزینه‌های جاری و کاهش تقاضا تعطیل شوند. فروش طلای دست دوم و طلای آب شده به بحرانی برای صنعت طلا تبدیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677391" target="_blank">📅 19:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای وزارت امور خارجه آمریکا: ایران ممکن است منافع آمریکا در سراسر جهان را هدف قرار دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677390" target="_blank">📅 19:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ3XoVOSRXsVCYg1g2tA0PJvKlJa665YdXXQroK6I5flj6YA6S_9gICU479M_PXM7e2zaBoWrlxgPfRSWnhxvhi4J42rBE4UK0DgUwJ8CD8L_D_YtuJ5ao1sJJkKdM0IN79k2oj3D3Xd16RWWFsr-xQSTd4d74yepPHoq_pfEmbmB5geAmkE3ZvoaJngNFw5BUhIOILmFWgstHdK55c_imi31KirsLa9ljFmribd_GzUD9ToFDpsLhLAym7umf64aDhTa7Z03hQQk8vm8HGLNRQGjYFFU7IQSCO2C2f1MUS4RCg-EN7GCrmDiwCgUmvl8JopSENGCldWCr_psbojow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام عراقی‌ها برای زائران ایرانی
🔹
آسمانمان برای موشکهایتان و زمین‌مان برای زائرانتان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/677389" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJsZ52TskB6aNsE4UsyrQrwu_IFl5LAnhpASb_juE51PZzj8HGpBlPDHm4TkWr2JF_1AWQ1Rpmuq_3EFEeHDhklqaojjcf_3Kg9Xm3iA7GHd4rybmZpJkyojGpqbSl7AIxXkJUEvNujhojhU7Czch8GRcdRfKx5cZzO9b7YJAe1Q6k21y4cdwYuhQB-pfuq9zNgMMgCS8T0cu8qj07pouOlAhF5-u7W92Km_FhqBGWvvP6ObKHl3bMqW0iGXYlCYJbMk-dZr7VCPPrq8QfBDI0PrHDP6WCsyTL9K2VY6s0RZA8y3wnDBLU568yRk4ocVsphK101eVFH5vx_npz2HEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
لبخند سفیدتر، اعتمادبه‌نفس بیشتر!
🔥
سرم سفیدکننده دندان LANBENA
✔️
کمک به کاهش لکه‌های ناشی از چای، قهوه و سیگار
✔️
استفاده آسان در منزل
✔️
کمک به تمیزتر و درخشان‌تر دیده شدن دندان‌ها
✅
روش استفاده:
بعد از مسواک، دندان‌ها رو خشک کن؛ ۱–۲ قطره روی گوش‌پاک‌کن/برس بزن و فقط روی سطح دندان بمال (با لثه تماس نداشته باشه).
⏱️
۱۰–۱۵ دقیقه بمونه، بعد با آب ولرم آبکشی کن.
🗓
روزی ۱ بار (ترجیحاً شب‌ها) | دوره ۷ تا ۱۴ روز
برای دندان حساس: یک روز در میان
⚠️
روی دندان آسیب‌دیده یا لثه ملتهب استفاده نشه.
🍵
تا ۱ ساعت بعد، مواد رنگی نخورید.
📦
حجم: ۱۰ میل
💰
فقط ۸۹۸,۰۰۰ تومان
۱,۲۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
📦
پرداخت در محل (در اکثر شهرها)
👇
برای سفارش همین حالا اقدام کنید.
https://memarket24.ir/product/brief/56228/180124/</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677388" target="_blank">📅 19:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
فرمانده نیروهای آمریکا در اروپا: ناوشکن‌های ما برای پوشش هم‌زمان اسرائیل و نیازهای دفاعی خودمان کافی نیست
🔹
به گزارش واشنگتن پست، فرمانده نیروهای آمریکا در اروپا، به پنتاگون هشدار داده که دیگر ناوشکن‌های کافی برای محافظت از اسرائیل در برابر حملات موشکی بالستیک ایران، در کنار پاسخ به نیازهای دفاعی خود ایالات متحده، در اختیار ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677387" target="_blank">📅 19:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCRsGAcejaUf02BP0RmeMvzfqkPyxqDI3LZ62AEa4jOMiKMvrUsJEtvOTwgvD2v2XyEU-wAHKAK1G9vNCFC7Nce1WGHB8R5t9eCURr-iAsWLznRlvvi3n3FLVvMYrEYmf8jPk35CCA0uF8TvhDX5BlSm6OeGa1a-nwxZQWdHGu7zN5l-iEEQkkvVTxSvHhaACUN1ZplS0PWnCilCvF4dbCjbpLAWsdugiAJ5IXclPzMgqY_Yqd5bil5gfz_HhRELcQ0aKfR25noy_LK9HxXD-KYZcyoPV3hG1Gg245xV9XVR7N-tQYGxyLmheGW0Jfkt9UAEoDVPKSHrl-XJ846_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای سریع مسکن‌های پرمصرف و موارد استفاده آن‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/677385" target="_blank">📅 18:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRs6auJeoQ_aG5uXXRcPBCfIXv3sb7U7kiWIVSwegO9a3OVl37poHNYa2Xg1719_ULI0nmL942CBxIx6mw7KANlKTTB_h21Fhvpo_eXG7fPWp0S-phjurjH05zl78MTtSVV-h79GNPpyvMr2A-hC4LpMh_wf7F83an9KKFkBD6LnMcnCYLX-vB-00gjjNb5LmCOfIv-cOcRMS9WketwasDdEobR8AK7d0tirEfjHbam5nxNhd3gcB3EeZHMqMynByhPWL_RIEhvrIKdAW-JGfh71RHv8QwXx2vyHAfna8vQk_gf03E2WFYdBu4EXLDEzm_KvC2ve3pRrQJU2LwzJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
اینجا مهمان و میزبان معنا ندارد؛ هرکس می‌تواند خادم باشد.
▫️
اگر راهی اربعینی، سهمت را از خدمت بردار؛ حتی اگر فقط جمع‌کردن یک سینی باشد.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677384" target="_blank">📅 18:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8ihLOEaWIBsEH4b1RDfXUJ0vVgN29SfTES-oKy2VVfRH8CEJwykhdxpaoc27CZo_CTrDAMrLZN6nVoqKSpQXWoHGio1ehzy1zPLYlqoBZPIxybJYpV4H0wadcEn1c1Chat3cDrfRzKdqXNI7t0Av3Gzj6pJFUzPt-FRdLzmZ0YPBdyCSYkeRsEW_6Op9iORtWMfE80iSWoCIc8coSvMxngvBVkHsvraRx2_-BnVK70l2f68UjRZ6KhfLi-mhx7JNxd_3LtbsTOdp1-066FErbXOC2atYipSoXCsLrr7nu_83JM4CYy3wtt4QY6NjTGwfGwjMfGMCBOwPfrgeU5Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: زیرساخت‌های ایران خط قرمز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/677383" target="_blank">📅 18:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUmnOGyoVKtxOqJ-Hy5oZzU6iHy3YeouYSx46wavrPMa_QXf4VSc7zakcB-a8YOJ1AleNhA1tH5WCtNzbMpZISL_jvZBj60L5S5mL8a40BNHfTm4cQ8uhudn1BkNp0LHFreBHRsXN085EnhST9F0dMyz2IRM3HxaYfPnHEGBjR_C6dYJGUEMKhIIshcx28IgYH3XGSdsHjcImVHMk4OaPXBX9JLBF9myvK7N2Vn334rnM-SJmyhXiV_H2aoABk3snRFdozzDnEn1sgNKdULHTohsVs0UqNIh8h2ycCi5HVVKvgVaPhhhNkWK_-UhKPlSj7yJV3R-agax961BYP7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ماهواره‌ای جدید از خسارات وارده به پالایشگاه جازان عربستان
🔹
تخریب کامل ۳ مخزن نفت و آسیب جدی ۲ مخزن دیگر در اثر حملۀ یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677382" target="_blank">📅 18:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای آماده‌باش دیتاسنترها برای قطع اینترنت صحت ندارد
مدیرعامل شرکت آسیاتک:
🔹
اخبار منتشرشده درباره صدور آماده‌باش به دیتاسنترها برای قطع اینترنت صحت ندارد. اگر مشکلی وجود داشته باشد، بهترین راه، استعلام و پیگیری از درگاه‌های رسمی شرکت ارائه‌دهنده سرویس است، نه دامن زدن به شایعات./ سیتنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677381" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWo3Gv1X3kicy_tRcgnu0qyzqIfwuTmyrxvrub_kpKQdCNFXmzulYVSisaDssFxdCRxfXwYMiJ4LUWHLQm4RRTpZNJ5b65_182x1MAdw7CXS6n8J2PXZsZoBvuPhGOB2X3PTK5dxGk4E9VVnYoy_4M10FxzNxxxuwM9XzGDBjZ6Emc43vd1jLv2VhoXve_UaHoTrR1OPgXsJvOvA9tyPTX_XOVlsYrvpA1KWolsy3LzfjWULqG7uu5jqAmWLc3nm-5U0qBCOkVX3Z5HHcVzwxSxm_Y2nmGK5nTSZXqhO5grn2n0_bzZhGxU8DTHhtefl39NN33OXrpUzU2RDVHxO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fehj6OR-5e_MFazo0iwpS4C2CXeR69V4CsWrlkM1SaWh4ZXMawdJqVBFt3nAEH1xU1FCjZkuBKrs4_bucZoNbeiXx3M_A3k_PtiN-1_2QrHcOF7TglKCWr3HdolnN-jS6ohf0-m3qieC50-IKA2GtkP5SmqnIHvMKNBvRTmFJzv0tXEt-Impd0gOElefeF36pt10xEKUEGnuHsURi3GayATSuZPP7I-X0G7xCr_TdP-gzF9pBMEjHHHjyUj3RB1L_abSf20PWNul-nR_oS5rJln-dsHx1ZEA3_vObLivjAiAlZb56pu9Izr5oy7mLiG9ZXQCZ32j9cSUCj9fgXL1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyhqr6PvBdQCf1RG87GlJQf13gUUpZ79rr7gBIWC6dr2-ol6Xi7RK7cQhulB8vLYh6JaRzUnzyziRHfB1atEEZ2B6WN5jARlSXb11ZvIqjzD8RN049vSJvElEWIIEdUsBRMZg65V5PaQ4PjzodT12_QItmmSIylzO1_58czhi1k8K0w5VAl3J65QBmecrRtmUP7NwCnnv115XgbgjZTDYbeFUj_P-RAUKRHQdpNTO8mH_ze0Kxr7W7vUNwsKakNoar-2Uen-PlMAVs58rCLE6vwMnKHt-IEF-nblCyXm3wIAx6YcxrA7OglJqzyEQZqq-J6VHnUeBZA1PQRcQ2jxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZShaqfxXKvOisxROipetoZC1wmZQZTx6_5nVbbd_bg23qKUdHfk4hFfPvcaa41wT9W8jpz-wsJ_8uEsyboYAA6fVM_-p8tQ5qEZXQvh-VoMYib9ec4m_19nMYZcmVexZFl31EFq0FEFguEARw_e3UYhBb6GPFMuL48GOAmABunUO5pZ3biHuLdfTIjEKzSIWBxgOJJ90lYmGuhdpw6ki483O8ul40IAUZcULYSMZI-xGCgiCLKJ1GI0lJTyOr9HuIeMM1slkIQfZ0kBF0qtl7EQyjEkALWFbSrDePpMeRAaS0zI4o1Zy3U72txRRzzchi0xizwakUzvpANyp12SYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM1qHKocrhIUOgiURIqZ6VJmKMy4n3skUmDICJM6Ww4vtAg5kFteOSAK1HArsV-LZElfPz1Oq2gjNeTG28OE5XZxvquYxQXvbef-BwyBt2SlyGh24iANnWctJ9bhI-9AmQP-nlYqb4JORBgspXO5GmN0KZ4hHAcS30pnHBl0E27wBt0MufVmj8prYQa40snM2bT2bI1dU1L9j-_xt33Y2CSebfrlxm4Q16cFfjI0kg3mt1O0min_MY83POXyWH7EfAwkkgvFOj5lh1OvIsQpBG2nYol_Q_f5EoWtxrqjmneG1BKtmBkVFnE2R16TAFOWgaGAQeqDBpzohLWhTAib7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_s2lK7mBHr87iEPIYcksC3CIAN3JQcQOySw9c8pSnMMQrMKxEPXTAz_IwPux_-zeIqaogBx4R0vevShET4OK-aOFUyOK2I4ZKsdlm28n5UQveu_ViKwRs3_By2pdiQ4bQVrL4etnVdvG3np-Ni-5ZrszTXojR3q7Fmnd0PUvw3V4PU4SVmMKXz8n--2GwOzHhWzqjpT584QtY1V9Z1NSpCvq8-DfkQ4Dx06dHcW8AwvdIlwvSYqVoTBOBp0WRcVa5caZrPZ7V7W8qIaVcP-6uC5tNP7rEeDgcHZxSvfLlm8tP5PY1yH-61bZoDW3_GzYIe7zCJN7G64ix5TIKV6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6TBvTENVtfF-tK9fuKixk5qJKy0DvOMJiEtoKQk6NRoOcZeULM1fo7xsGqerXhyreHeE0rN7S3lM_aLTBbDY92Ba8fBUttBwKPpwAD52h0RBWgIUDorShEZNn7X9g_03oebAQSgQ4KgCwsPQFd3JuKozoK6C1U908TQtXp4ewIHhmTd0I0RHb-vPuiknUTGg62kCyWd88DaumbKAe7dRjrneYaRgc_BphFUxT6n4c50kWn2BqGhqxZoQXaFY7x5XpKD_uNTg7D7Rfn-okD0Qh0luytspdvR8g3mkc0JGydb5Q8HYj7yB3-oVNB6z1Df6mw2NX5qChKaicDmZfJVVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدافع سابق پرسپولیس راهی کربلا شد/ محمد انصاری و جمعی از چهره‌های ورزشی کشور در قالب کاروانی راهی زیارت کربلا شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677374" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
مقام اسرائیلی: از هیچ تصمیمی برای از سرگیری عملیات علیه ایران اطلاع نداریم
🔹
شبکه CBS News به نقل از یک مقام اسرائیلی گزارش داد که تل‌آویو از هیچ تصمیمی برای ازسرگیری عملیات نظامی علیه ایران اطلاعی ندارد و همچنین از اسرائیل خواسته نشده است که به هیچ اقدام نظامی علیه ایران بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677373" target="_blank">📅 18:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: گسترش حملات سایبری به سامانه‌های آب آمریکا
نیویورک‌تایمز به نقل از مقام‌های آمریکایی:
🔹
دامنه حملات سایبری که سامانه‌های آب در ایالات متحده را هدف قرار داده، دست‌کم به هفت ایالت گسترش یافته و احتمال دارد شمار بیشتری از ایالت‌ها را نیز دربر گرفته باشد.
🔹
هنوز مسئولیت ایران در این حمله به‌طور قطعی تأیید نشده و تحقیقات همچنان در مراحل اولیه قرار دارد. ایران از زمان آغاز جنگ آمریکا و اسرائیل علیه خود، حملات سایبری‌اش را تشدید کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677372" target="_blank">📅 18:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گوشت بوفالو وارد سفره مردم ایران شد
منصور پوریان، رئیس شورای تامین دام کشور در
#گفتگو
با خبرفوری:
🔹
در بعضی فروشگاه‌ها گوشت بوفالو به‌ صورت علنی به‌فروش می‌رسد. واردات و مصرف گوشت بوفالو از نظر شرعی هیچگونه مشکلی ندارد ولی آنچه در جامعه مشاهده می‌شود مخالفت مردم است.
🔹
در ایام جنگ با وجود شرایط سختی که وجود داشت ۱۲ هزار تن گوشت از مبدأ‌های مختلف وارد کشور شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677371" target="_blank">📅 18:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677369">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f170b4a0d.mp4?token=YdPuMoE1DaZO7PMi9f9MUibl91iRQXDA8u0_5uqV0RYBq6VAkGWVCWhmgxeR5t9djlB-VLKhqt8t0Y3Z1jpxvQGao5Gy-Vyi0TGFOvUOMGNuzqsc1rXmjkm3DY0CaBGBxlUwJ3kj2Yn5emVV6tCRaU5JpkJ78vag_99Xw3DaQcQNVYucf3tx13I9i61IGCIlkgovxsuSHADB_WJtPdktH7crljzl-q2w4828n4c2p2bOC3DLoBceUm5Xvc3HKqmkV4lFd1PnXZMdP6Wmwve-DJJFAuQcEJGMpoNqHrhxHbfVacbD4BQdDOPOF0-J5lMq9-6h3U3pP3gUDB5IDFn30A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f170b4a0d.mp4?token=YdPuMoE1DaZO7PMi9f9MUibl91iRQXDA8u0_5uqV0RYBq6VAkGWVCWhmgxeR5t9djlB-VLKhqt8t0Y3Z1jpxvQGao5Gy-Vyi0TGFOvUOMGNuzqsc1rXmjkm3DY0CaBGBxlUwJ3kj2Yn5emVV6tCRaU5JpkJ78vag_99Xw3DaQcQNVYucf3tx13I9i61IGCIlkgovxsuSHADB_WJtPdktH7crljzl-q2w4828n4c2p2bOC3DLoBceUm5Xvc3HKqmkV4lFd1PnXZMdP6Wmwve-DJJFAuQcEJGMpoNqHrhxHbfVacbD4BQdDOPOF0-J5lMq9-6h3U3pP3gUDB5IDFn30A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات پهپادی به مواضع تروریست‌های ضد ایرانی در عراق
🔹
منابع خبری گزارش دادند در این حملات، مواضع تروریست‌ها در سلیمانیه عراق، در هم کوبیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677369" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677368">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVn8TkkgK-btpvjt5AV_MwPJ4rf8UmN2OSWR26yrivkFWR62GpZvX_N-u3o7SUQbpantK0AP9hS15XJ20EDNKIV0nWXasNa7pY2nVkcgVDvA4wWnlzJt6prqnXVUALUsgwfOi6MnT03a6BFeawqtXPow4SNIHzK56s25z6iA1SyyZ5TKqa1F4VDVGzbGUfcvprgcMtGq4yRZeHbrRPxFVDaIOKUiWANbNRP3uclqq5-zWKE7hAdnAbXDf17EyVGv2_Wqukfm9q4HDPMaAoZdEM5wnKcEDI5zPJTY__TYMIyVy-CC93sX-tPXOOduZ4s89xNgZNYpddgRSsjWMTTpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
یک خرید حضوری، با یک امتیاز ویژه
با عضویت در رسانه‌های فروشگاه قرار و خرید حضوری، از
۱۰٪ تخفیف ویژه
بهره‌مند شوید.
کافی‌ست رسانه‌های ما را دنبال کنید و هنگام خرید، عضویت خود را به همکاران فروشگاه نشان دهید.
📍
مشهد مقدس، بلوار شاهد، چهارراه ورزش، برج ایلما، طبقه همکف، واحد G26
منتظرتان هستیم در فروشگاه حضوری قرار
📞
ارتباط با مجموعه :
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/677368" target="_blank">📅 18:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
کشورهایی که سفارت آمریکا به شهروندان آمریکایی برای خروج از آن‌ها هشدار داده
🇧🇭
بحرین
🇪🇬
مصر
🇮🇶
عراق
🇮🇱
اسرائیل
🇯🇴
اردن
🇰🇼
کویت
🇱🇧
لبنان
🇴🇲
عمان
🇶🇦
قطر
🇸🇦
عربستان سعودی
🇦🇪
امارات متحده عربی
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/677367" target="_blank">📅 18:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
گاردین: جنگ آمریکا علیه ایران از کنترل خارج شد
ادعای گاردین:
🔹
طی هفته گذشته، این درگیری در سراسر خاورمیانه گسترش یافته و حملات و ضدحملات در حداقل پنج کشور دیگر رخ داده است.
🔹
ترامپ به جای یک جنگ سریع که به دنبال سرنگونی حکومت ایران بود، یک درگیری منطقه‌ای را آغاز کرده است که خطر اختلال شدید در تأمین انرژی و قیمت‌ها و ایجاد رکود جهانی را به همراه دارد.
🔹
این درگیری همچنین به حملاتی در عربستان، عراق، یمن، اردن و مصر گسترش یافت. نشانه کمی وجود دارد که مذاکرات صلح بین آمریکا و ایران پیشرفت زیادی داشته باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/677366" target="_blank">📅 18:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfb62ea7a.mp4?token=hzSOkUKnKhkrm2hNcWSr52IqoM2avxd3WuROzMIhRiVQnB2vGEv8-kWQ83nzKPsUm4sJZK2hTTVtT_Fr3ltySJI49qITn7SOthzraR6dbAbxhF_N5q0cLBQMEXcdWBTGpHanINLqfbukg-t0q5S9CE5Ztw7wKOkrSd6tMt1fe0BMEqIw9BEv-_zC-SNuNv8w4qmFF6goJf9FrDwdXczo_LbELjwp8x5oW_F6x4eO4dmIaWOT89BEO3laS4gsaDP_x_VZviPaW17eVWR2aW30evpvZhrVdOUs_EI4DZuPWaqxacrkom1TMNkXEj-mYENJW0K6gKG04d6tYsQrFl13yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfb62ea7a.mp4?token=hzSOkUKnKhkrm2hNcWSr52IqoM2avxd3WuROzMIhRiVQnB2vGEv8-kWQ83nzKPsUm4sJZK2hTTVtT_Fr3ltySJI49qITn7SOthzraR6dbAbxhF_N5q0cLBQMEXcdWBTGpHanINLqfbukg-t0q5S9CE5Ztw7wKOkrSd6tMt1fe0BMEqIw9BEv-_zC-SNuNv8w4qmFF6goJf9FrDwdXczo_LbELjwp8x5oW_F6x4eO4dmIaWOT89BEO3laS4gsaDP_x_VZviPaW17eVWR2aW30evpvZhrVdOUs_EI4DZuPWaqxacrkom1TMNkXEj-mYENJW0K6gKG04d6tYsQrFl13yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی‌های خودران زوکس آمازون وارد مرحله جدید شدند
🔹
این خودروها بدون فرمان، پدال و راننده طراحی شده‌اند و کابینی با چیدمانی متفاوت و روبه‌روی هم دارند. انتشار ویدئوی این تاکسی‌ها، واکنش‌ها و شوخی‌های کاربران در شبکه‌های اجتماعی را نیز به همراه داشته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677365" target="_blank">📅 18:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0-b4-j_4sU6sRo2HKoDdfl2FUCxzwNGb3PTSWvIllKgqv3HlJLInCnXA2hg0Xo6JOo_Wvt-H1pUdICyoOFRYgtkZc7oR9RIGhviBdHH2DjMAvhC3uIo6OyNvcOpQRV4OzxuL6ZRfXBGbJQTsmajny5Nieapzrvu5W6suYXOFGChpM_PpoVoEEh5qdGR1wF3NBT8M5w4WZuFuaVTC5hK14hR37y0NPgqvEl57SlPYsELgP2YIlpRDs3FsabUxxzcz8wWbscDQkguhzu2e-KIcfsH51hLxh8dVJTFQfuTA0TWjDFfKWmnCYQCpSNrao3M8GgKM_tZh4Sq53DKESzqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین سد را دارند؟
🔹
چین با بیش از ۲۴ هزار سد در رتبه نخست جهان قرار دارد و پس از آن آمریکا، هند، ژاپن و ترکیه بیشترین تعداد سد را در اختیار دارند.
🔹
ایران با ۶۰۴ سد در رتبه ۱۴ جهان ایستاده و بالاتر از کشورهایی مانند بریتانیا، آلمان، روسیه و عربستان قرار دارد.
🔹
این شاخص تنها تعداد سدهای بزرگ ثبت‌شده را نشان می‌دهد و شامل سدهای کوچک و سازه‌های محلی ذخیره آب نمی‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677364" target="_blank">📅 18:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سایپا قیمت پراید وانت را بالا برد
🔹
سایپا قیمت کارخانه‌ای وانت ۱۵۱ ارتقایافته را افزایش داد. قیمت پایۀ این خودرو بسته به تیپ، به حدود ۷۶۳ تا ۷۷۵ میلیون تومان رسیده است. این قیمت‌ها نهایی نیست و هزینه‌هایی مانند مالیات و بیمه به آن اضافه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677363" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677361">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKXmX7eG4e-r68IQqssh4B_Z2AisCyGBIQgV5noWqLkSnQW18kWuBxMCSdZutHFmRy6TxK5Io8LCGrMIzMnxIkyLsTzqzykEoGvCx4RhmHgfyk5x9EbRqMQUn-DJwevdo2L-31b6h5AKy34411WKiiOo-f9vjZigGnOanlMR5uYZZRYpxZqYA7fzxW50KaULKI_7piHcoqqrVtxGjB4ChCT1Ue49893lBGUjKMJvBOSF6jBYFv-rw8_uSNH_S4AAqoAWaFIRSe808Y5CMyrfMuQdqqarkS15upDL-RckYbbAjbwXwpsRDh-u-ybWTRuwLHCxzjXtItPDfXySHEjosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه نمایندگی کشورمان در آلماتی قزاقستان به نیروهای تروریستی آمریکا در پی به شهادت رساندن کودک ۲ ساله در قشم:
وزن بمب: ۲۰۰۰ پوند؛ وزن هدف: ۱۲ کیلوگرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677361" target="_blank">📅 18:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: امروز هماهنگی میان سران قوا در سطحی بی‌سابقه قرار دارد
🔹
ژنرال آمریکایی: نیروی کافی برای محافظت از اسرائیل در برابر موشک‌های ایران نداریم
🔹
انفجار معدن در دلیجان، ۲ کارگر را به کام مرگ کشاند
🔹
سفیر ایران در عراق: توصیه رهبر شهید به مسئولین عراق این بود که استقلال کشور را حفظ کنند
🔹
غرق شدن کشتی غیرنظامی روس‌اتم در دریای سیاه؛ مسکو اوکراین را به دزدی دریایی متهم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/677360" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d96dcf8b7.mp4?token=lSKKXjkEb0_IU7UZsph9TaVv1zyfDrPaJHFeGNP3gjnGO0gPctgDNRJVjNn_9ZOdBhPG4oW77XIVNW4P370R_DcvrBOOxr2y8uteQzwI6aEO7EsSiSZCdIleDrkkPHB-xYoRDPVTOiZcsSYqXaSFQKQViWQBNo1DPIorsiqnhXudDASr_LCy-raCvO0i575bhqYaWQZ3QEXkUvYoj-hoQAhUFz6jX27xGcxTCxt5ihEoQYUodq1-B2273T4yJYrm_80uDhTGNnJjAOs5iHkx2Wlgg5LCA68y69PEAeJwgYPdv1OBDKGGtEEy-azggHQ38dDcmmFiKWC0M0fhnQh4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d96dcf8b7.mp4?token=lSKKXjkEb0_IU7UZsph9TaVv1zyfDrPaJHFeGNP3gjnGO0gPctgDNRJVjNn_9ZOdBhPG4oW77XIVNW4P370R_DcvrBOOxr2y8uteQzwI6aEO7EsSiSZCdIleDrkkPHB-xYoRDPVTOiZcsSYqXaSFQKQViWQBNo1DPIorsiqnhXudDASr_LCy-raCvO0i575bhqYaWQZ3QEXkUvYoj-hoQAhUFz6jX27xGcxTCxt5ihEoQYUodq1-B2273T4yJYrm_80uDhTGNnJjAOs5iHkx2Wlgg5LCA68y69PEAeJwgYPdv1OBDKGGtEEy-azggHQ38dDcmmFiKWC0M0fhnQh4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
خاطره شنیدنی از سخاوت شهید ۲۲ ساله
🔸
پدر شهید «علیرضا الوندی» از شهدای جنگ رمضان، درباره منش شهید و اهتمام او به سنت قرض‌الحسنه اظهار داشت: پس از شهادت، بارها به من مراجعه کردند و گفتند ایشان [علیرضا] به ما پولی را به‌صورت قرض‌الحسنه داده و مشکل ما حل شده است و این حکمتی است بین بانک قرض‌الحسنه و شهیدی که با وجود سن کم کارش قرض‌الحسنه بود.
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/677359" target="_blank">📅 18:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Ur7ZPvcXKl84Uk4H95JLg3SCsscrUMEMHneUf10Pwb-6gbRB5EgVXdt-ZR136Az2-XNRmVp50Izni8tB0SzYcmdk5qqayZcK4tzR4uUBcPBUA9bqTi6uBGK1GS4t7m5GYf2NhIGjd9YPZl1vck7kqrgKW6fe-w_ajdD9WXruZjN2_si8bOAheXkx6tT-hOrPRRwfldLpj9U67W7aQwEFRe9F3rSqggcg6114ZfpWj2ftVZOcjeF0QrKEbvKoXtE7awuzF1XSMiI9LyQBtjQeEGtMipa33u60my2S-xO4QMM-uyWuoQ-9702bG9neO-DJgiylzc842-dEUku4TIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب تصویر پرچم فلسطین بر روی پیکر شهید هنیه در عینک رهبر شهید انقلاب، هنگام اقامه نماز بر پیکر این مجاهد فلسطینی
؛ ۱۴۰۳/۵/۱۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677358" target="_blank">📅 18:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/677357" target="_blank">📅 18:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677356" target="_blank">📅 18:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT3p91KVMzqcIZ_X-XYGEakm6NdrvcYYBi-bqz4Ln6yl-U1JWURBO7viYQvmAOMYnQzTD_BmqdovXMePLEngZgQqtsSwAQUq856WX_vhVjejJ3xb7BQBNhZ6rEMyUbSdBE2uVEjuOaedqjitDI_UmPXbeFtKaNuhokxqpwSi_srMZb1x1Qp9LMchh_ZdiOv5IYZM3PS1jauqDVG0JOm3pjsBeEKpiQxxpQO8tbrrASlsGC77x2jQeCL9EB4WMgtmxR9QsjuvGKSdEius8TUFaet3qPd9zP_gu6EEw-IU45rUNOxs3F5pek54723hR8uO480mM44Ab--1-A1KmQc1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای هیل: جنگ ایران، دزدان دریایی را فعال کرد
هیل:
🔹
جنگ ایران، خطرناک‌ترین خط کشتیرانی جهان را دوباره باز کرده است. این جنگ نه تنها تنگه هرمز را به لرزه درآورده، بلکه به دریای سرخ رسیده و دری را که واشنگتن فکر می‌کرد به روی دزدان دریایی سومالی بسته را باز کرده است.
🔹
در آوریل و مه امسال، دزدان دریایی در کمتر از دو هفته چهار کشتی را در سواحل سومالی ربودند. جنگ ایران، ظهور مجدد دزدی دریایی را اختراع نکرد، اما به آن سخت‌افزار، آموزش و پوشش استراتژیک داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/677355" target="_blank">📅 18:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677354">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxXWfkJlxO-N_3CdfGaERyo_9lpXfCpVVAVxo-Qb1iMAoKrb6MFSNqWk6BhOxSLdmTmvtY9j4X__oaCwVkhjv03dTRujkZpW-6SyflmJdObiCjlKIKPan63IgpZw-b7AegcaXHNQWeLXByeB3M0JAGDnTjY1v0EEShw22BBFk1i3WDj2d4_k_eoozEFvG9YB_miWGOd_pUKaq1orFhtIu8FYG3C5UT19IFwFej1lNeUE1U9iW5KnlTtGUIRvsX2TvM4QvO8Rnye5NaNqz-YbWxykXhQSM34w_XGm-lovRJiEfrHP4YAHcjRfLUfSApyY-SHFS6GLIFgCwLeFuKiNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میر داماد؛ فیلسوفی که اصفهان را به پایتخت اندیشه تبدیل کرد
🔹
میر داماد یکی از ستون‌های مکتب فلسفی اصفهان بود؛ استادی که شاگردانی مثل ملاصدرا رو تربیت کرد و نقش مهمی در شکل گرفتن اندیشه فلسفی ایران داشت.
🔹
نام میر داماد در شمار ماندگارترین اندیشمندان تاریخ…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677354" target="_blank">📅 18:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وزارت امور خارجه آمریکا: آمریکایی‌ها در خاورمیانه باید محتاط باشند و برای بسته شدن احتمالی حریم هوایی و اختلالات سفر آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/677353" target="_blank">📅 18:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677352">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv2P1H1hJyuoAhtACgLr5f2AAukiGQKohGa9CVVAR4rJaG4rcwsWhJ12CYECAgCVIErvKryFsfBzWG3zz41z86xyeS1EN2RZCuIc4mAS27I4Dpq5He-3FaCmDZ-O2nlIeFuOtK8cnFS0RJTK_FKaIOGf8jSlVeilZ3Nw50vAMe7SuIozehpCW0_hmpNolUa-bX9PXhAs6KigxIVAsSqffmRQeE8irpmEMv9LWPqMyyDCRJKPc71beJPTPeY05gqqxGNaylZLIcyrJo2Xd-HjoMMsysVkbmMgsxY5541StrgauiG0w1QA9Dl3pwBuZqyhgRaCF2YygvdgxHcyeYAxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تهران تا مهران، در مسیر ایران
کرمان‌موتور با استقرار پایگاه‌های امدادی در مسیرهای منتهی به مرزهای غربی کشور، در طول مسیر اربعین همراه مسافرین خواهد بود.
پشتیبانی فنی شبانه روزی از ۶ الی ۱۴ مرداد
▫️
02142724
▫️
KMC App
#امداد_کرمان_موتور</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/677352" target="_blank">📅 18:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677351">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYgkC4fJLUpIu94FLoiPpOjyk7feyZsH4jMcRo-d5ErrT9nyvqsIGAWODKowC1IzFS5yjm4O-g23ktSg7BsagBsjSjaO7DTbznRHeLQvPyPcJdvvNmNeId76eNTCRgu5mn8RQ_tHo65C1xx60gKmWRKrOuT_c5pKRJ1V2cscbwf1k4Md3-xUw1gmqYblW2Aw2QWCiGl5Z9w6RyAD-h1-hVYy-4Es-1BGZ6AnYwoMUw_NyUmn-bOcrm9lySuhu3Pj8LRA8mYCkClOQWLq_jaMzXRC-R-bYHH7-6KvfMCqFMrSEZS4N0QPD0Ok6_G9c5PulEuGTNOm4y9j83wfAaxHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادمان شهدای مدرسۀ میناب در شارع‌الرسول نجف اشرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677351" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_qryVB7U3c5Jlga4o6jiSXIZHdAWUFo4il7DQnPn8WfLnxoYWppzIXwbHPVRdpp24GB_52hvitk8AFmo3WqwTBWIz0ud5EC6ZDT2RG-ZCo1QToodpJ-aAEM3x3KIURzWdNKGlqOCkghkM1PuaJJjpMtmL9FeO51fPuEQbunkVqHHYTkY7NyqZO3mH_IimMyizIauYi05OrDr_98CR1XUV2FKY1BAKp9WqVc7GDpKy0zJlb3AS_UEIzvJl9BdqQ59tmmvb_KGse6HkkmWCdgwIXLWKK9sxMpDSqvxaG-obCgm8BQUMewEG34w5zTUAikdCGbJT3hLmb8-V0yVpcoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت جنجالی وزیر آمریکایی در خلال برگزاری جلسه امنیتی با ترامپ
🔹
یادداشتی معنادار از وزیر خزانه‌داری آمریکا اسکات بسنت برای خرید چندین میلیارد دلار ین ژاپن، آن هم درست در خلال جلسه با رئیس‌جمهور آمریکا در کمپ دیوید، توجه رسانه‌ها را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677350" target="_blank">📅 17:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677349">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvQPnPqQGbSvBNzWYEH07lqYnM15WIWcBit1R4HL3-d-KP8ulwFoOQXkVGMor7ELgeAdeeSTau4XbviiNoYQDL9rbc7ia2B0NXFEDAoDsjo8-Jajo-4huHPYFWWBxBMgjnPeIk3ElPXuj3tSL3lsKzHt8GX3nGJdQFMkMdYuMBVll51xdeMps7d-JEQX3G3Ne0BptjcQvAHAcQSUTu0iULOT5IE8Sk4tYFEXJjlqWVc4RDJKTuVXdGuWAonnj3R5Orpitprj-EM6GYmy2TVoOIjTaj4c1yFOweeUFbcx073Bs0036mAre46QErXvlPdJTdlQj4gE6jSxmNSICnFR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از مظفرالدین شاه و کمان نادرشاه
🔹
ماسیکو معتکف‌الملک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/677349" target="_blank">📅 17:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677348">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFVMlQaArNngJNvqqH5UkTywBBTU5Kt_858ed9WSu4rBEfq46qbqkZO83p18gLayi3oVlXPN69HL4gVTC4FjPU4AdKnHX64a8dSkw5A55epfRHMtyLvQyO2uZCmP8_4DJ1fobXzkhE-MVQI05eGRwKzFZ2rlU8VpvFb5tZt3lNvsy-Rq_p5b3SuXBjKz6q8k51PDvdX2fWaOT_1pF5egiiIfEPfq9_W-c6w0w7iB1B7fU50dcfdymdEN46fYj64I4L_poX7VK3uAk23d-6SK0uYFgoCBMN-e927G-gkdWOQQdzWyAj9egQiR2aHZUxC1c4TtSMAqErs1EIXOSJfybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ شغلی که هوش مصنوعی نمی‌تواند آن‌ها را از بین ببرد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/677348" target="_blank">📅 17:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677347">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUmSNvyWYVStRNRTnLlx1GwJPdlGScOFWnN-M3SvS1wlEOkl4BCrdTK23a6rVxJjTsX-z4PHWRFYGsoOxjiFcYTextJR9zdrtPPV3lriUjfni71Txv4KT92XzmfBgGDmEcK7nbc453-y6OXM3Uh5pYmnEk3_eBF9ncFPtNnWS4qxQJOF-3AdsWAwW_ZxeXMuFFnYZ5BjtW1zWm4XeFHxPB2oAFv8nNH07sLf7nTFiSVI_8Ubn8wqeVPEYHU_GKMvlzy6GDtFJ-SB_H-TcR14XkEtD-XKammkMYhCusJ9gGR65YpBQDeDUFOVUs4-BdJD83jR2Fzaj9NyEEGDPU1dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تداوم اقدامات حمایتی بانک صادرات ایران همزمان با پایداری سامانه‌ها/ جریمه اقساط تسهیلات در دوره اختلال حذف شد
🔹
بانک صادرات ایران با هدف جلب رضایت مشتریان تسهیلاتی و دارندگان کارت‌های اعتباری، جریمه تاخیر در پرداخت اقساط مربوط به دوره ناپایداری سامانه‌ها را حذف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/677347" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677346">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo3AN_LHZrAFb_peuMn1MuZrQqSuQwZSQ9w23iyVjFOprawK5ZkDahNDtHsYxP6v0RHJZ8y41dQIFmRhdCnCd-AocAdNwRihvHPRBs9L4aXkabaup4pR8O6wTB5zSFK-ZaC5PlBNEqmkwp4dyKvhZx37FKtEP9AqojJyLjbw0lB-grqm33uUle63FVtCcuS6lHquzpu3VcNEP967v_G9-O6Qw53f0rff1jbFEH7ukBt1ConNxguoBeQL_x7IogB0dAROe0oTTy7GbTIhrdyLhaRRqMt72HRLY5l4LAHXZjr4WTxnOPBr5K5yIgLQzQydFLcsYm2jJ7DHarYO01_9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
خادمی فقط در موکب نیست…
▫️
گاهی جمع کردن یک لیوان، مرتب کردن یک جای استراحت یا حفظ پاکیزگی مسیر، خودش یک قدم در راه خدمت به زائران است.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677346" target="_blank">📅 17:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnWYGr_c0fcDf1W6hsNYf8DtBPYRe9tZuZyjbQj5WW9MKoEUatlNMNQQYQKGTXBohhmwWX1gts74wrlEWVj9LvUpwB3b3zph_1LOmKom6Mxre4GyPskFJq--P3jscOEJpdKczyz76X9iGDKSyAaV-PdUSF4i6Oqq_l1AqjSURHQiNeqeevlX0rT-_cARtZ8S_mzEntlHlEYL2tMvFHIWfxYRhERwFX07rVDep-KnLxOipy1c9ngSKO5jB9zfd3GTlHQMCRYQnHH4AaSed1e-osDmlt7hNCsVSdgtPeSZAKol_fRxhAZo_yMIF12nN2sdqrYyuPZQd5GDXaooTKDC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل گاردین، رویترز و الجزیره از برگ برنده یمن در جنگ با آمریکا و رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677344" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fckrNOJEbi3xveX058ILG-AQhYvOLfJYWD-Y765mPXVTgIZ8-MtwZ50MYAPTgx3Um3KWqvGzAR1ozAzcuKM6ZsqlO9AxE82bPDssyemYWptL2IAkOclcLKG6FpgTngF3HjxhqfqJwv-izKCTLrWFhtO8-qKGB1ciVbi5o6VJSvVhcg0Eo2S13ysGSmTcAO5e0EmekZpsJmOlqqFGuR7N6xWGcqTIeW5oubeKvr6hhX7uMss_j5eG_I8icLckCgjcO2QlDIHEISvbz9VfqSjdeKUiqHIYHgJ7KvviNduTIMlSp4JOEPbM4GqKBpYUYugjj36FVBbmQi9MzbCOWaeZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت‌های آمریکا در مصر، کویت و امارت درباره «وضعیت پیچیده خاورمیانه» هشدار دادند
🔹
در ادامه هشدارهای واشنگتن به اتباع آمریکایی، سفارتخانه‌های این کشور در مصر، کویت و امارات نسبت به تشدید احتمالی تنش‌ها در منطقه غرب آسیا هشدار دادند و از اتباع آمریکایی خواست…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/677341" target="_blank">📅 17:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توصیه عضو کمیسیون امنیت ملی به عمان
بهنام سعیدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات ایران با عمان صرفاً درباره تنگه هرمز است و هیچ مذاکره‌ای با آمریکا انجام نمی‌شود. تنها ایران درباره مسیر عبور شناورها در تنگه هرمز تصمیم‌گیری می‌کند و هرگونه مسیر موردنظر آمریکا برای حضور در این آبراه از نظر ایران مردود است.
🔹
اگر عمان بخواهد بر مسیری غیر از مسیر مورد تأیید جمهوری اسلامی ایران اصرار کند، قطعاً متضرر خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/677340" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwJuixGkBaAVzZ-oie3jc5ZHeQaKLlEze2JPPZrS6aBTm5NL8pYsHPw1ZKg_IKWiw7umGy5kPlAw-PjvaxRBaR6UTN2JF5ktFMTwHtttxfqGaS5hGSWRDPbvZD8XK_y1V2uIhmkdu3cVxZN7paREOBsPLhn4tGNwsl77WfoczXj6riBYRKTYAB2DqSWGviYc6zc56SaFLK_Vc39-T7n8VIxX__CAR0RjA9w4o6-HgyNuR7RPiYGUdILDsmUqNO8eqTSgfDUsnrlhHTfCEMX2EQ-8PvLnRvagM_E6jahuACSJXIcuf6PTWZGEiO5QGs-vtikXDHkjzHxH-HY-T1lpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677337" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b197534600.mp4?token=oynykU9-PgAcbcOH6yftciNir9sAeVd7fZ0BsENJmp709o9M0UBq3yx6_B1rA8xci-l8Qej5n1UmhpgFfoZmG5ZNDTl0Etxm44ubW2Z7-3AXICv9xYSyhr8hN19T4GGgQeeDTvj0iVwsgPOmOvuITtP3EzgI5k_nIuUDxrkbcgV8a6Q6lQ7oTWG6yIiJhWwlLEzH2aJ4R2mhGg77aoZ3pdPocPoJ_nl4Q7YK3bLfhlQIbm5Gvo1yPlIRwhf-drqsFz6dcBegHpFwtpwJ4RFiqBHB4mIbFUZeI1NxbuuckdiXoGrDkiNfJf7RtyG3SplQnvweCsnz_Gm0HdbE19BEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b197534600.mp4?token=oynykU9-PgAcbcOH6yftciNir9sAeVd7fZ0BsENJmp709o9M0UBq3yx6_B1rA8xci-l8Qej5n1UmhpgFfoZmG5ZNDTl0Etxm44ubW2Z7-3AXICv9xYSyhr8hN19T4GGgQeeDTvj0iVwsgPOmOvuITtP3EzgI5k_nIuUDxrkbcgV8a6Q6lQ7oTWG6yIiJhWwlLEzH2aJ4R2mhGg77aoZ3pdPocPoJ_nl4Q7YK3bLfhlQIbm5Gvo1yPlIRwhf-drqsFz6dcBegHpFwtpwJ4RFiqBHB4mIbFUZeI1NxbuuckdiXoGrDkiNfJf7RtyG3SplQnvweCsnz_Gm0HdbE19BEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با افزایش درآمد بازهم پول کم‌ میاریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/677335" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMvGgzaW_ms02pytdWtuQriV1rnaiFnpUTDM-R7yKPHe5Y2uoIUtTp_zzXEswCocbB0Si76H_2_2C7gdpSsTuawvmCBy28KRUUK0F1haGFjQHv4XSULOpFYgeaIWRppI9ONyCklhXnROamg5ny11EGoDWHLJGcp9Kq3-aOMbvNsM9i0L_MhDq7fjoFIg01xHOomLInFZFGHb-Fy733jwPy3iotMGH65k_X_5WD_2pY-06v9mztBubnd7UhEPLDioD5B5gQJc7Srq33tck6n_1wuRlXbHtiC0zrGq0mA4qcChzfcCeqmBOL64y9iOAgB5zsNsLh3vE38ck4jV0XawWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
حرمت نان را نگه داریم؛ اسراف زیبنده سفره امام حسین (ع) نیست.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677334" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اسپانیا خواستار نشست فوری اتحادیه اروپا شد
🔹
پدرو سانچز پس از ورود ده‌ها هزار مهاجر از مراکش به منطقه خودمختار سئوتا، از برخی کشورهای عضو اتحادیه اروپا به دلیل درخواست برای تعلیق اسپانیا از حوزه شنگن به‌شدت انتقاد کرد و خواستار برگزاری فوری نشست وزیران کشور اتحادیه اروپا شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677333" target="_blank">📅 16:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سه گزینه نتانیاهو برای حمله نظامی به ایران
🔹
سی‌بی‌اس نیوز، به نقل از یک مقام اسرائیلی مدعی شد، بنیامین نتانیاهو در دیدار اخیر خود با رئیس جمهور فاسد آمریکا، او را در جریان سه گزینه برای جنگ با ایران قرار داد.
🔹
از جمله این گزینه‌ها حملات نظامی متمرکز بر مسیرهای زمینی تأمین تدارکات خواهد بود.
🔹
همچنین احتمالاً زیرساخت‌های انرژی از جمله نیروگاه‌ها و پالایشگاه‌ها نیز هدف قرار خواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/677332" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب یک کامیون سنگین در روسیه
🔹
یک کامیون باربری بزرگ در بزرگراهی نزدیکی روستای «مارچوگی» در منطقه پرم روسیه منفجر شد و شعله‌های عظیم آتش تا دقایقی به هوا برخاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/677330" target="_blank">📅 16:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام سید عباس موسوی‌مطلق: تشییع رهبر شهید در عراق، بی‌نظیرترین بدرقه تاریخ عراق و بلکه تاریخ اسلام بود/ از مردم شریف عراق که این حماسه را آفریدند، قدردانی می‌کنیم
#
یالثارات_الحسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/677329" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سفارت‌های آمریکا در مصر، کویت و امارت درباره «وضعیت پیچیده خاورمیانه» هشدار دادند
🔹
در ادامه هشدارهای واشنگتن به اتباع آمریکایی، سفارتخانه‌های این کشور در مصر، کویت و امارات نسبت به تشدید احتمالی تنش‌ها در منطقه غرب آسیا هشدار دادند و از اتباع آمریکایی خواست آمادگی لازم برای ترک منطقه در صورت وخامت اوضاع را داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/677328" target="_blank">📅 16:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1bCNmn7nppVTPOAAsoNQP_lk5vs7FCuw-3bp74MWVv9Ch2nX1ynaxO65ebtMyfv4n-aPs4x4AY2nGNHPBWcsqYq9g4mgzRgB2aoo7w-ACzMxe4tTWRp3o2IHhlih-nCgEietWdHYiTWUkYgvkoGho63lW4r_T3rGdpOCSlpqwS4AdeDamoon0srDF_dPuejHFzUd2zfBmjBv0OSGhn6dXnoRAbNc-MUdFybB0V27nJqUJ0GKKqGaIHFYZSiPuOMvpTB2YptizYOJ5C5Yn8XC8DYERAxV68B3KsySkoPZSZjTSyexriTITXtzboku80nUN_MuDz6m4WCq-6VKy_q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APGehJbu-YB4H5s5AJhBwlnThrrpSi_q5RINRL1WzJ1NnU8yuTFDIpWcPq-aNtkaVGWVw3iqeLPzQBq77dveXGukzDXbGkXPhhBJ4algFuGhQRwqW3ZsheqUxhjcIPmCWJlKeQR0s5p60eFFuSx4SpsKtt2RWghWS43H5m85H3wB1nVp7C_AaVFOdDWQTpJ0ndJK5WbWTMPzKNTtP_sXZoYcIxb-C0oy1-GlJfPghj9DtRtLbDoji1LD51kaCotbpjjLhWgkR-9iob4Yte4ON-zhKcjqTbogwHEQQpha6XMbwrwm1g6s4bp5w9CYYDjnVxIcUUDZXF-0rs5H0UH5VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتی انباری جای خانه را می‌گیرد؛ «مناسب مجرد آقا» یا نادیده گرفتن کرامت انسان؟
🔹
انتشار آگهی اجاره فضایی شبیه انباری با عنوان «مناسب مجرد آقا» با انتقاد کاربران همراه شده است.
🔹
بسیاری معتقدند مجرد بودن، توجیهی برای اجاره واحدهای فاقد حداقل استانداردهای سکونت نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/677324" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آب دوباره گران می‌شود؟
آب و فاضلاب:
🔹
تصمیم‌گیری درباره افزایش تعرفه‌ها برعهده بدنه اقتصادی دولت و وزارت نیرو است که با هماهنگی وزیر نیرو و بر اساس الزامات موجود انجام می‌شود.
🔹
در حال حاضر هیچ پیش‌بینی و تصمیمی درباره افزایش تعرفه آب وجود ندارد و امیدواریم این اتفاق رخ ندهد و بتوانیم با همان افزایش تعرفه‌ای که در ابتدای سال ۱۴۰۵ اعمال شد، موضوع را مدیریت کنیم./باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/677319" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677318">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انحراف از باند هواپیما امبرائر ۱۴۵ از باند فرودگاه شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/677318" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677317">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه بزرگ به کویت؛ حمله‌ای که برای همیشه خاورمیانه را تغییر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/677317" target="_blank">📅 15:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
سعادتِ خدمت در این مسیر، توفیقی است که به هر کسی داده نمی‌شود
▫️
کسانی که با ایثار و سخاوت، تعریف جدیدی از انسانیت را به جهان نشان می‌دهند. خادمان اربعین، سربازانی هستند که در جبهه مهر و محبت، برای تکریم زائران امام حسین (ع) شبانه‌روز تلاش می‌کنند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/677315" target="_blank">📅 15:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n67-Zope01EUJ8Eu5iuPsWRF0-mttzQZukT5X1CiZcPWgQhKoVV2rY8zzStFFg-x65tcezRh1ZKysN6FhtogPpIQ0hSSEV7Jj2e2qT_BeOTL4L3U53JPOXuDupYvrGeU6htI2XFou7bSwxTmCpQKJiQTrjhs9RRGZoWYMPbY9nprR1QrNJW8_jZkPdfiw5Vm7_WD4oGVozR1gNmYKPEJPC0NNhZmOUNwWFdDefR4skha86YmH2m-h1Criunep6poNpm_aNPpvXKmqVqk65vyfcfOUa5MO6ztA2Z38RZ32emUW0wmgq0lvHz-DiVsogeelS4Y-SKEpwj1OVWtaCKvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td2FaeLEQN7RACJws0ovBw8VodzCLRL0IWi9_qRB32XGdPCSP6O1sEM1NRRoZ7lbIcm1MYwr-yvww8ZrVPKu9onbiVWT4fOww872V-hZnsKg8BQl8cEbFUsoi7Q4_dnX76OzvE2dn0WGNzTLZA73fgUadjh-h4L9tDlRq4jOAr9RGIfmP5E4PWCYnGpyjIZGR6IkSxLpOf5B0j-73N3erf3AIqk28XwaDU2KdzwQcmZeg9rLj6xMTTixtqBf3oIjprdhvLMaIA4shaJcljj14KPYmYNU4uKPOWiGhbb-RzzUHjrBU19gEFotk3cg48WhAZduD7QegFxQ949I8uKuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqZep3k2hG-IytLUPpUckKEzW-5l_d7gaYvIfIgitEahPDTUeu4ZtaTfAUnJ9DdrojWLzewqK2O7cU0ODzVYnZ8MbiNv9DtzT-Ip4nUN3y0okz32p-B9H33BN-IoTiUfO4b9cZpJxl7UIuTJjkAGG2uDdeK5Ts8fnvaeEttGQwKGIYAGMvUyFCoCLbkqP4kvU9FLlFe7jkq8b7MML_GX3H1soIP1uWzAjY6HHzDAL0NsOA0Ud3XyzsQwMc9WLqpo0s1xQsiRfI0RLE2nj8DJyNEJRVJCDiD76R4ItylnyRWM-MaOR1PT5hkBQ0oengyOCjlTS_TiXEq7G4VMR3AzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGFMy94t5qhm49dj8JVVCM32wBc28qD43LS1QxtnYdDrsC457AYIaCO7qddBY-XhetW0goQBAUr_N3oQYgo51GO_dcaxpWnG1CFAf-Jcnkmc6A8A7xc_fHFB5FDN8m9t4CfcYo790pJsxVLWu_P8LgpfLsgph9Y2Olt45hU9M0o3SHce7HgUqz4Ov9LAWHe1m61ezHdJNmZdsD7WeIh8-eHZWw8tpUFrQUPnfKDe51wIMLDSVnG2VTInotGxTMP_J2sUCqOqRhdEmAlAjAXKhE08S6GdOaBGVbMwL1cq_efi5tv6BK8aH1xAUXD4yR4cqnqN2vXEAmx-jZYq7ZVm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH6Nvq0vGCedJ0IM0jU8jvathrI0IPfpn0x1s-9ulhnmtJTKkvzo63AWDi7Lblk65yW0qEpk7ENuZUT9Dw8V3oCZAuaK0LhxLcfhjp3WwrI5CM3aNSe-dcUJNnu3Kh12GyHOrDqWIrLUbBDeI3J_lzLZJHBu40KnMGPyL_n8YF6Dmnc9hqrIexfR4uhAUeOig6uW12CqAyhJwO4Wym3HeRgi3tJjLjHmHki_DAPxXGXHdTb5X50_u6p7omsXF1u6A6yLm7LaAagK-3x__MxLG6w2ydgk4Ov8cbfkhtHtmESn_E0I6JjccoIUM9rP0L-F1gIbjv_9tobpw_LeUTJKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4GtzGKpu4qmtjr8Aua0PoQUDn4f_Ywursj6njyloSTiKU56QzlHAAyfHe8HrFhci_nyHiLnadtS6RlVimxrNaFNqA2KlSwFFye_11lPf2tYbsBpx8IT_DVESkxMP4nR-lpKbILvAun6OVxcG0A1nd2i7E7hwkO7BjNApSp45z2e9knM6fipxfImOFewf6-ePCbXpCS8FHvNRJKUYfXRWP63Kbf-39RQ6IMk__YNC-a5B2S9hc6N7uJjfxICbeVNfCWDCBHkmivQJ0G1HrtSqMJeav8yztJxhLd-8PM0XgC_Kx0rfufxs7S7JdZgtkgKumwSo3ABVX8qF5URxz-ooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2wkzjH-_hllLpssA8meJ96PjpcblhXIoR2kOURep7V2KXd5LbSrnqGO54apYeRsenA3rvoIbQak6M00q7CbbJUOfhA-O4wkwoEBckAtQRCbicW5ntnXISeeSn9GeO_S_eQB2FD8WFyuaSPFNzQ8yzaoK3eetow1RA2Gc6qLnTg14TvQdyG7HjCFF4-be47DvZ45GwN8pwyct47G4-uH43QormE2JyIuPtgEK_4-zErmckgDv0AUA1I3I5ftJgm6w6TGaw4VgoZMIU8u2t6GqDngjL614HySEegLJBSdBcM8ozTndjXACJItLigQ7YquzX4fRufq-KV0fypzLaLQhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایش عشق و دلدادگی خانواده بزرگ فولاد خوزستان به مکتب عاشورا در چهارمین آیین «نذر حسینی»
🔹
در آستانه فرارسیدن اربعین حسینی، بار دیگر فضای معنوی و شورانگیز یاد و نام حضرت اباعبدالله الحسین(ع) در میان خانواده بزرگ شرکت فولاد خوزستان طنین‌انداز شد.
🔹
آیین «نذر حسینی» که طی سال‌های اخیر به یکی از برنامه‌های شاخص فرهنگی این مجموعه صنعتی تبدیل شده، امسال نیز با حضور گسترده خانواده کارکنان برگزار شد؛ رویدادی که چهارمین سال برگزاری خود را پشت سر گذاشت و توانست جلوه‌ای از همدلی، ایمان و مشارکت خانوادگی را به نمایش بگذارد.
👇
👇
akharinkhabar.ir/local/10964167/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/677308" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پنجره متفاوتی به آخرین دیدار شهید هنیه با رهبر شهید انقلاب، در روز قبل از شهادت در مردادماه ۱۴۰۳
🔹
بازنشر به مناسبت سالگرد شهادت مجاهد بزرگ شهید اسماعیل هنیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/677307" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت دانش آموزان در امتحانات نهایی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/677304" target="_blank">📅 15:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب زائران ایرانی به بمباران برخی مناطق عراق و شایعه وقوع جنگ
/ تلویزیون اینترنتی مدار
برنامه‌های تلویزیون اینترنتی مدار رو در یوتیوب ببینید
👇
https://youtube.com/@madaar_tv?si=ICb2BPIkhXtjbTUS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/677303" target="_blank">📅 15:09 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
