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
<img src="https://cdn4.telesco.pe/file/kdBr0a4mn0Qr3QnbXnxLiieJiuxqAtWDam48omx6JtCRDw6lQHKpVd4WH-2hjvhOE7wAou4pvUymZTg6Oi5aZj-eWQrk_YD1aps_YlCmFNe2WJMEW3a2Q_cs_Uz1baqj3v1X0gkPmNfBCN0e6kdT8O35HHB2B9QMcW-i0uk5UpSjy0aRipYuMboonerhKXhUBTSR1CszKk8_Keyzfih_sHiXS5DVrFBLsmsX0z1LLJHC3XUthqsEa6J40vjQrri2CvcBRW5zMdVP2SAvV-R6DUTKOL_aPhRd9U9Y8hGno4JNUVfZEguUaOUSFp1pNE_Q6x_es35Mzii6mrbXfUo8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-137100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/137100" target="_blank">📅 16:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
ترافیک مهاجمان در پرسپولیس؛ سرگیف مهاجم اول تارتار
❌
پرسپولیس برای فصل پیش رو به نظر ترافیک زیادی در خط حمله خود خواهد داشت در حالی که فصل پیش در این پست با کمبود بازیکن مواجه بود تا در نهایت ایگور سرگیف در نیم فصل سرخپوش شد.
❌
هم اکنون علی علیپور، پوریا…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/137099" target="_blank">📅 16:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc0HQjekUXOLDjCnp36JhbGPOmsVUEKkwiqMwsRHCZFs3iiDvbrONM9AcI5XD8XUH3Co2kKLGDJKQQvwctpUm7PjEtssBFmJ_iBCDEBBIJTyYs2NQ40qy8L6FJGRSkv1us8tTn4X4V00gD2vZsxd2RIxXkMVBDAIK19XdcPkvjx_whPeuCqREG4TA9aVUZwyzapv0NcE7VsQkPWrmhqgAXqEZ5-1CON9bxZx5Y4cIeuK8XYvV6DugSISiq3Oi1Ci8LNzfR7QKF6OiCBNhHyk4k6czKETAu7J3lb3PGJzqjGx-5J1J-8XNNqaXKAG6PZWYboqJ0JYCh8xOWG7U2Je8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽
👀
‼️
محمد عمری ۵ فصل پرسپولیس بوده ۴ تا شماره پیراهن عوض کرده!
۸۰ ، ۷۷ ، ۲۱ ، ۷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/137098" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/137097" target="_blank">📅 14:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
❌
❌
#فوووووووووری   |#ادعای_روزنامه_هفت_صبح
❌
مبلغ رضایت‌نامه محمدجواد حسین‌نژاد، ستاره دینامو ماخاچ‌قلعه، به ۲ میلیون دلار کاهش پیدا کرده است.
🔄
هر دو باشگاه پرسپولیس و استقلال برای جذب این هافبک ملی‌پوش وارد عمل شده‌اند و رقابت برای جذب او همچنان ادامه…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/137096" target="_blank">📅 14:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
رکوردداران حضور در دربی به عنوان سرمربی
▫️
علی پروین: 25
▫️
منصور پورحیدری: 18
▫️
زدراکو رایکوف: 15
▫️
امیر قلعه‌نویی: 14
▫️
یحیی گل‌محمدی: 11
▫️
پرویز مظلومی: 8
▫️
برانکو ایوانکوویچ: 8
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/137095" target="_blank">📅 14:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDyI-2d2NFA3MwpC1Q83G8xMeMiJak8z5BxUM0vz9GRBwxULZ6EsYdzEhy29swUut85gSqwiTkWHaIbku6SYCqL0sp8KZX3WbwEViAkYnNKLh67-GerVszuO0E_RteglCNGqjwwDZCIGcBEfvqSFWDf8oDTXJg8KxwNnpOnR_bCoC1VCYfFjBbbGIqn6JuA88wAYszpnh207-lLiBGHxvKoy3kSqO-T8R1DvtBK_PYxM3sOHiYjGszLQeg-p10CU5zp3m_4_y4NuLLOusAyNjVaURd3SUI-4PBnXco6gIyxxTxwdI8apQgkwXOBRfqrNaJFCTkBYusMwsAyp6Jw8sHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDyI-2d2NFA3MwpC1Q83G8xMeMiJak8z5BxUM0vz9GRBwxULZ6EsYdzEhy29swUut85gSqwiTkWHaIbku6SYCqL0sp8KZX3WbwEViAkYnNKLh67-GerVszuO0E_RteglCNGqjwwDZCIGcBEfvqSFWDf8oDTXJg8KxwNnpOnR_bCoC1VCYfFjBbbGIqn6JuA88wAYszpnh207-lLiBGHxvKoy3kSqO-T8R1DvtBK_PYxM3sOHiYjGszLQeg-p10CU5zp3m_4_y4NuLLOusAyNjVaURd3SUI-4PBnXco6gIyxxTxwdI8apQgkwXOBRfqrNaJFCTkBYusMwsAyp6Jw8sHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/137094" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
دکتر عزیزی دست به کار شد
🔴
خداداد : میخوایم حسین نژاد رو بیاریم ایران!  پ.ن مبلغ فسخ و شنیدن شاخ درآوردن
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/137093" target="_blank">📅 13:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/137092" target="_blank">📅 13:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
فوووووووری از ورزش سه
🔴
خبر شرکت هلیلیویچ در تمرینات پرسپولیس شایعه ست و مدیران باشگاه این خبر رو تایید نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/137091" target="_blank">📅 13:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137090" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
🔻
🔻
علوی سخنگوی فدراسیون فوتبال: با جزئیات مقصر اشتباهات معرفی سهیمه سوم ایران به آسیا را به زودی اعلام می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/137089" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🫥
🫥
علوی سخنگوی فدراسیون فوتبال: برگزاری لیگ برتر بدون حضور تماشاگران؟ این موضوع در جلسات در حال بررسی است ولی لیگ با تماشاگر قشنگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/137088" target="_blank">📅 11:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
✅
✅
بابایی مدیرعامل چادرملو:فدراسیون فوتبال باید خسارت سنگین به باشگاه چادرملو پرداخت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/137087" target="_blank">📅 11:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137086">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137086" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137085">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
#شایعات
‼️
3 هفته اول لیگ بدون تماشاگر برگزار می‌شود!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/137085" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137084">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
گزینه خارجی جدید مهدی تارتار؛ پرسپولیس سراغ مدافع شاغل در روسیه رفت
❌
❌
باشگاه پرسپولیس مذاکرات اولیه برای جذب عثمان اندونگ، مدافع ۲۶ ساله باشگاه اخمت گروژنی روسیه را آغاز کرده است، اندونگ دو سال پیش تحت نظر تارتار در گل گهر خوش درخشیده بود
❌
❌
گفته می‌شود…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/137084" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137083">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/137083" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137082">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
❗️
حمید استیلی: هیچ جوری نمی‌تونید علی دایی رو حذف کنید
💢
برای چی باید درباره گرانی‌ها و وضعیت اقتصادی ایران سکوت کنیم؟
💢
مگر می‌شه سردار آزمون رو به همین راحتی کنار بذارید؟
💢
بین مردم و بازیکن‌های تیم ملی فاصله افتاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137082" target="_blank">📅 10:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137081">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137081" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137080">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfF_7RsP8jAceDenufpyvTjU3aDpexwV-9msoU_Sejn3jeWjC3MZNALhS6sZzKYXtaUvHbEXtOON9KEux09fff3q-CC8EbDRirHRfQliwioH8PYXyT0SlTFN8SaNR5eA7sHf_T4xgmVcCi-PXaR05XG6CJjAJtVHHraAIKQfnLr0LDtex1abNw09jsq8wI46Ps0F_ePnDN7Bevt0U7DU1GL-fLU4n9cJD9skn32syj6crPUb2nSjR5v9vNza85T-YB8j1OjRXJFU9J2IMR7dZSCl_5VXGST31HuWKD8gFoxHuIRwJ5ZdvAcab4fTebT0d_4Zjnh2Jx-o6tDKbI5Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🧤
عملکرد نیازمند در دیدارهای دوستانه پیش‌فصل:
۴ بازی: ۴ کلین‌شیت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/137080" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137079">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFk1kVCIFPQVkQz2x1MRjAJyxdw6XZXFhzn74bJPF8esJZYSbdVGIYVHHL8m9i30TbTqDsx8QPKM_Q8nh02R5LlrtP8XHNb6DT8QoscjVrxsWf0NHUEXYuSqEfaGicVaFtddFYpufZaaq3q3VpUWhe9tr8fhsdmUnAc9mFj-389d4cqRPBPy9DZkkVlIWUM82BQjAhu08XypTxRRQputjWelh7dY32ftV4yzy_AzT-Pq8PVTI2zuZfNj3zwo1UWYcBr3UHDxkZlNcRa18myYbNHafIJXQknOYxaq-E16wP6_HZm4EUiiP-ha38lL0l2dG7FsSXvdyL8xFX70JuWUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/137079" target="_blank">📅 10:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137078">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c21rkm5o5flq8ESk95yOVJxfyjsIxCXBHL5maZHdW8FtDis_6wmb0aT3UkOXjBkX215xPAa6pIcvoeYQzIVUMxPETD46CopNzRrzLTqdJ5Q2xBTxFfVTogbTrOcZbhjxxF89SuPBIUvED4PyyI7L7B6slctZzaa7KJO4bS1eZMdiEkY4O3Py5HNy3DjJA4X04gdtIE2Pd24RHaaAloIZtZLKUTQo1I_QtXmWC8ar20fSvBnRciHBew01463_dMrnwZyi_FIZkhVJBLZP9T7iJYOTDyS7jEAkRobw9nRaUbUl1CSEZW53P77GH0kJKKKBQkVP30UMRerGUW3DhTjozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
تقابل استعداد نوظهور اسپانیا با ستاره باتجربه ایتالیا؛ آزمونی بزرگ برای جودار!
🎾
Jodar -
🎾
Musetti
🎾
دیدار رافائل جودار و لورنزو موزتی، تقابل استعداد جوان با تجربه و کلاس بالای تنیس است. جودار با انرژی بالا و بازی هجومی به دنبال خلق شگفتی خواهد بود، اما موزتی با تنوع تاکتیکی، ضربات بک‌هند کم‌نظیر و تجربه بیشتر در مسابقات سطح بالا، روی کاغذ شانس بیشتری برای پیروزی دارد. اگر جودار بتواند فشار سرویس و ریتم بازی را حفظ کند، این مسابقه می‌تواند به یکی از جذاب‌ترین دیدارهای این مرحله تبدیل شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137078" target="_blank">📅 02:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137077">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی
✅
✅
منتظر یه خرید خوب باشید......
⚡️
⚡️
این همون خریدی هستش که خلیلی ازش حرف زد و گفت داره قطعی میشه و هوادار پسنده.....نامش آشناست......
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137077" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137076">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137076" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137075">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137075" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137074">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
مرصاد سیفی و امیر جعفری دو گزینه نهایی تارتار برای حضور در دفاع چپ پرسپولیس هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137074" target="_blank">📅 00:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137073">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137073" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137072">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137072" target="_blank">📅 00:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137071">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137071" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137070">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
#فووووری   #شایعات
✔️
✔️
گفته میشه یک مدافع چپ جوان خارجی در اردوی پرسپولیس حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137070" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137069">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
آلن هلیلوویچ به تمرینات تیم در ترکیه اضافه شده و قراره بصورت بازیکن تستی تست بده و اگه اوکی باشه باهاش قرارداد ببندن
🖍
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137069" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137068">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚠️
⚠️
عادل فردوسی‌پور با این ویدیو از خودش دفاع کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137068" target="_blank">📅 23:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137067">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=KyPmokBHpEaoHQloGZdHUv3312FyWDS4lMOyXDJ8HG20D-GYNKyAf6YgDC90hRZomkaW-s5rX2lqV2IHZ52zwS4gjTatcylvNWqWreYjr__qg06sCz7iLg9EaKOPdwX6p_WlIdCfLgX4gaVZKPjDSuWjA1lWgR4dlurtF9-oeCasyto_dEqbT-8-zkEzPejwXFjNi4TNRg2JvsMbYUllqldw9hFv2ItgPqHyuoLuB3acZuAN8VJdUewPyVcDz7HtJmF7tm7DoTB4ZoGYITgUm_rOV2sZhNWIS5pkIjVsE2lXRjzF0xWW0ng0iA0I749_E3nnT_kAOuuiHMbxVhu-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=KyPmokBHpEaoHQloGZdHUv3312FyWDS4lMOyXDJ8HG20D-GYNKyAf6YgDC90hRZomkaW-s5rX2lqV2IHZ52zwS4gjTatcylvNWqWreYjr__qg06sCz7iLg9EaKOPdwX6p_WlIdCfLgX4gaVZKPjDSuWjA1lWgR4dlurtF9-oeCasyto_dEqbT-8-zkEzPejwXFjNi4TNRg2JvsMbYUllqldw9hFv2ItgPqHyuoLuB3acZuAN8VJdUewPyVcDz7HtJmF7tm7DoTB4ZoGYITgUm_rOV2sZhNWIS5pkIjVsE2lXRjzF0xWW0ng0iA0I749_E3nnT_kAOuuiHMbxVhu-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137067" target="_blank">📅 23:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137066">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گفته می شود ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137066" target="_blank">📅 23:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137065">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚠️
⚠️
بندرعباس بوشهر قشم کیش آبادان و اهواز بامداد امروز شدیدا مورد حمله قرار گرفتن و گزارشات انفجار تو این چند شهر بسیار مهیب بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137065" target="_blank">📅 23:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137064">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🔴
🔴
درخشش علیرضا همایی‌فر در دیدار دوستانه؛ پرسشی جدی درباره روند استفاده از این بازیکن در پرسپولیس
⚽️
علیرضا همایی‌فر، بازیکن جوان پرسپولیس، در دیدار دوستانه روز گذشته تیم خود، عملکردی قابل‌توجه و امیدوارکننده از خود به جای گذاشت. همایی‌فر که توسط مدیریت سابق…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137064" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137063">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQbDtBZJvQ1KPRz36Mtq_r2nw6BO7QGKzVqdozk3NrnobP0cnRJ7OnGHzXWbeW2ARHkOWUtyY4IpatsJx0d3vQxmuntBrTEATEsuQfNFgk-bYBnN-8_e3BMCx6f2TmxUqAlYfFzdzcVEsL6b38x2olgMEp52rdDczf6fuAXfasVqvsoi1wcUJVNgtImd68ErN6rMiG817GHim8yjOucye3RHs3PlhrcKOfuz1EMcOVB7se6CCKhwynPrQboV2QCTnQCuvfL032WlA82yMwG0d_FzSOYlnqk9c1Y9DZWfijwmRPQ9wPGV3KvI0_c7mXIAAKSf9SG1ymSUDCpERKKWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس تندیس عالیشاه، سرلک و پورعلی‌گنجی رو ساخته تا در مراسمی ازشون تقدیر کنه
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137063" target="_blank">📅 23:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137062">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
عملکرد تارتار در بازی های دوستانه
⚡️
۴ بازی
⚡️
4کلین شیت
⚡️
4برد
⚡️
7گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137062" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-OVC5kMNdEPY67dWd6yvpJzhcz82ame8sI7cAEfPc0bHKRrX2CYvJ1DMITX_kGkI6EHStV2QnJwCvcHweJZRRnNRT48zLa3fATfnsZIqSO-_3X5KZpOQhHxpRb0SiWTrxCAflahoP2FDzK94pfOOHy5ATtxUN1yL9o-wIP1iqCEY2RIOsnD4_5bdbonUXzE6ssQSbKgHv9Vn7vm37AQ7jEfn50YyS089bYLBeKAm419fhYtC4VxafhZULmVpwHTHnAfRfjt0gbskyZ56DKp2FYIp-wuZvDvaTAMaezv1YiZVly4SFCMIGaQkaFKVw-yccqkemAYC59LaZQ-VPlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!
نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137061" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0Q0y8d3qzviDXQ77l4YOF_thCnZLmoGPvcd9bqRhsj6dHyZP2OLBPzInsA-YZL3XHTcIChdJAH7CieMfbFanbwPUqwi9HeuwCxjLcHRsFwseEkF9WqQ6FIALklSxaCnjI97FYrmHICqY7LmVM6bX4-CMxbO-tt5kc0-VT5C0nICao79Ysjl7ARPvG21YW-i1sPgxpZNlnnQ0eBrLGsqQL5ZLjozYGdWPVhsIOdbDCHxjXYQE9-9vAGlHaAIlcrca8InWkGlPYULcqjN_UpcvVOOv1VyT0k85iUYoqA5iUiHHeFNxjRl-nhAHknpML84cvvy2MQNMlhCfpiWm68iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137060" target="_blank">📅 20:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
عیسی آل کثیر یه ویدیو از زمان حضورش تو پرسپولیس استوری کرده، پروفایلشم به عکس پرسپولیس برگردونده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137059" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu8wJbeWX2PqOgoa6tq1-_byP0HLuehmaF8cVleWb7xBKEDIxUlF2oU1M32b9vCmuYb_UR3DFno2wgcGVQ9WE6l5dlwj3DsrD7vaecRIWinTkpfe8wgthB9FjV6KxygVbxdK7cgZne_PC3RvqTr7iXb8omTUyGp-lvnkNADfnXqi6JfS9NCm_KvoG3Cj_Q0gC5_JIu2GgebruOxZDZnDX4K4zFGVTy3l1rtEaYMjg0ykUSKM_CVOpXIK2_z3xIRqicJEas_uSPeIjlwAXLRc2K_nJjIRYgZTWVfUj6dD4sXk3V-NiLd89NPNqXXNE2KCJUTnlG6t0Zb5mIvTVYwtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر آلانیا اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137058" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137057" target="_blank">📅 20:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
🔴
توجه | مدارس و دانشگاه های استان تهران غیرحضوری شد
⬛️
استاندار تهران:
⬛️
با تصمیم کارگروه اضطرار آلودگی هوا تمامی مقاطع تحصیلی استان تهران بجز فیروز کوه روزهای سه شنبه ۴ آذر و چهارشنبه ۵ آذر غیر حضوری اعلام شد.
🟦
دانشگاههای استان تهران بجز فیروز کوه غیر…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137056" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-s0yl22q0n3WBlqGjUmP93AtLQwdopO1aZ5qSXruMiW0Smri16mMUhCtIzKliSnj11ZISrEQhMhbFSpDn0Yk1E0jkc2p9tJV4T_AprE-BU6j2YfJOtbqY2SOHchtvnDoZ4AnrS_J3ufIfXzUdAOyoPrkZrswPUdzRlqU0zg57v_th6-7dL_iDfTlkKgsvXRZNR6-pj1iBXPa4NHesTg2fmBfQJ-rqFRkVs0W5gZnhGIePD_TX_UtvzZfHVnWgRY5dA69M9-DU4f1whMgiETpJHSCvXj4nErtJXwqQpNDjQaph42KNiSw0bNKQKdDODhF6ZvOqQrtkH2gMEgypkuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
برنامه بازی‌های مقدماتی لیگ اروپا
⚽️
امشب لیگ اروپا بار دیگر با تقابل‌های حساس و تماشایی، فوتبال‌دوستان را پای گیرنده‌ها می‌نشاند. تیم‌ها برای صعود و نزدیک شدن به مراحل بالاتر، با تمام توان به میدان می‌آیند و همین موضوع نوید مسابقاتی پرهیجان و غیرقابل پیش‌بینی را می‌دهد. شبی پر از رقابت، گل، هیجان و لحظاتی که می‌تواند سرنوشت فصل بسیاری از تیم‌ها را تغییر دهد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137055" target="_blank">📅 20:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137054" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔄
🔄
🔄
جونم تیم ..پرسپولیس دقیقه نود گل اول و برتری و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137053" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.  در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137052" target="_blank">📅 19:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
آلن هالیلوویچ فردا در تمرینات پرسپولیس شرکت میکند.
🔄
مهدی طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137051" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚡️
⚡️
تایید شد
🔻
🔻
آلن هالیلوویچ، بازیکن کروات با اصرار محسن خلیلی به ترکیه سفر کرده تا به صورت تستی در تمرینات پرسپولیس حضور پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137050" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚡️
⚡️
فرهیختگان: مذاکرات تراکتورسازی با الوحده بر سر قربانی به بن بست خورد ؛ چرا که زنوزی دنیال تخفیف هستش و قربانیم حقوق بالایی طلب کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137049" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyMbwjnjdy_yCcvN5bgWPEI4z0DX-fJ9oMtO_YH7I9uWUJ8mAo45jlSsbu_mwK06rlxL-fhLHSwmwp3Zb6yu4u5BQHklBuiQ-jMzVCVn57d2u6vb_CQxf0EPPHZVc7NgAca1B3URXnrg67hpOPRjSxqb1ev0XEdWSEarhNpci7VgogqSPa3A_VqFR_LXqMa3wnJmfv7oWGl9X8be0x8tXjyGCZGShBg2MQJwylTAw-LSdPXdxisqIvJTMOdvYKmzkEXGFV-7Q8FsScQXO_1lEB44STQUw7d9IbQ1k6VsHje90GU1Bk2967OCLWVX-Cto9jyY-pB7vokl59H6YwpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.
در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137048" target="_blank">📅 18:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137047" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137046" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137045" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚠️
⚠️
⚠️
تغییر ساعت برگزاری دیدار تدارکاتی پرسپولیس و آلانیااسپور
⏺
این مسابقه که پیش‌تر قرار بود از ساعت ۱۸:۳۰ برگزار شود، از ساعت ۱۷:۳۰ به وقت تهران آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137044" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137043" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-QW8Cic9GRzxcDBmShEMzj9BPGmNFdsghZaAkctf9HSMF52-rr2YVquI5bBEElgriu5N2NPwtA7EiqUF2VywD5mU2Acm99uvTDlGMrNtP_YJJW8cF25Oe_2t8Uslfaj9H_HhFOkLtnusO0KkrNOO_7YCFTKXitzkqIdxyhCJIQSNn2o56Tl2dVqFDjU2ZVK--hr-zd5ZzbRLTBM2W5jgau7_DwBb33woU0T746xD6fDfzoC1E8ybw0laSRO7cDCT9MjJvl1rfclZahfBlPDKZbBBiJ12cq03vTTETevkdZZxHiEd4rFOP7C1zTf9ZN27sQ8ILIB_Xp_vZmwc647Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۵:۰۰
[
لهستان
🇵🇱
🆚
🇺🇦
اوکراین
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137042" target="_blank">📅 15:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🇳🇱
رسانه‌ی هلندی:
🔴
آلن هالیلوویچ در آستانه پیوستن به پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137041" target="_blank">📅 15:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgbGaczqTI0OXYyoBvao1X-LlSK6zG4t4lNN3Ar0b3V-sS-qiCh2M89O0geQJ8fbp7Gjfw5PPsDdkAfuA4S1916Nxaf_t5oLWonE75v4KJ1UfzLbezJ2NJHSoDxVnqM0FC-CenC7nVJEWqLYzAutr9OY6SYrWcqth_VBgrKaljSMIkIchsv9PeEdkErFeCglXptTc0b_BIf_9FqIHvGx2pBlJGQHnYU8THLCP-sl0yhluJw6mci8Bmx0bEhynr0oBaWFoPADCX1hlZNQeJ13qKFlG4Wh9A7BX0I39oAwtGSk9HsDwfzOyAyDWdqbPJ7YY0XLcq7j57ZElm2imNBINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ورزشگاه دستگردی تهران حداقل تا‌ دوماه آینده بدلیل تعویض چمن در دسترس نیست و امکان برگزاری و میزبانی از تیم‌های تهرانی را ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137040" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137039" target="_blank">📅 15:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137038" target="_blank">📅 15:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
تارتار گفته عیدی تو فاز هجومی خوب نیست و ازش راضی نیست  پ.ن مگه با نظر خود تارتار جذب نشده .مگه بازیکن خودش نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137037" target="_blank">📅 14:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137036" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
#منهای_ورزش
✔️
باز هم جنوب باز هم مردم بی گناه
💔
❤️
✔️
شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
✔️
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137035" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137034" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915de24844.mp4?token=rhVONm7Rdt-bCbwBeS-6od6oHDVkQezJXO7Ry88d0VUFvP_V7lq_p7slYtQpDPZEJ9DulGUE0-LlZ05kRTW1EC-1q2DFSjOkxsEj-uLSGXO8o3bojqboQ8gRqQ1lzLPpCiZrR7AXHIapiK0NLbLHB91B35UK7vFsnLp87DaDuoajJC9JZHM4G_tIkVyjzYAGUukygjDKIMQry9EdXCWhaWuMh6emrBXXeIyuFMkBfADm8MubAKn03lgl033UwR7pkaeIZze8SMOelw-BR_CJomFZsYs4SWEKtjazXjpY8wPS2UVk6O0SX66RDkdPr3xKmMO3TxCtme4Ok2I6QERVhlfGjk7kCwBQbsmG7XEijqAMPqgJXwDnoh1uKNa9Presjqk7TqBLF9AshwZI7OG14W21fYq1SVeK4pFN6MflanoYb6b6Y7R4q8dwPlb5Ijuumfi0_LAEeKnnIJE5LNdSlHXpgzOmIC7kOmwC7hsxMSfSR4VtaLUMEX3sobMYdnNg8-hhp_BLyfJFlr1jarlEloK7v4eeY2Faw2dpRTKCHVb99sD03uDVsUAwxGOuoJtcqQScWze-SIaE2QW5rEeqEwnPzE14lXp4fgeRunuawmWgpDMvL0sxKR2rlRvLz3hAziv522O0hbPi4O7okikKaS--5k3HBONP01DOSxdzBM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915de24844.mp4?token=rhVONm7Rdt-bCbwBeS-6od6oHDVkQezJXO7Ry88d0VUFvP_V7lq_p7slYtQpDPZEJ9DulGUE0-LlZ05kRTW1EC-1q2DFSjOkxsEj-uLSGXO8o3bojqboQ8gRqQ1lzLPpCiZrR7AXHIapiK0NLbLHB91B35UK7vFsnLp87DaDuoajJC9JZHM4G_tIkVyjzYAGUukygjDKIMQry9EdXCWhaWuMh6emrBXXeIyuFMkBfADm8MubAKn03lgl033UwR7pkaeIZze8SMOelw-BR_CJomFZsYs4SWEKtjazXjpY8wPS2UVk6O0SX66RDkdPr3xKmMO3TxCtme4Ok2I6QERVhlfGjk7kCwBQbsmG7XEijqAMPqgJXwDnoh1uKNa9Presjqk7TqBLF9AshwZI7OG14W21fYq1SVeK4pFN6MflanoYb6b6Y7R4q8dwPlb5Ijuumfi0_LAEeKnnIJE5LNdSlHXpgzOmIC7kOmwC7hsxMSfSR4VtaLUMEX3sobMYdnNg8-hhp_BLyfJFlr1jarlEloK7v4eeY2Faw2dpRTKCHVb99sD03uDVsUAwxGOuoJtcqQScWze-SIaE2QW5rEeqEwnPzE14lXp4fgeRunuawmWgpDMvL0sxKR2rlRvLz3hAziv522O0hbPi4O7okikKaS--5k3HBONP01DOSxdzBM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
❌
بهترین خبر امروز: نوید قره داغی حرومزاده که دخترا رو کتک میزد، دستگیر شد.
🔴
امروز صبح موقع دستگیری نوید بیشرف ، این حیوون وحشی به سمت پلیسا حمله‌ور میشه. پلیسا هم سه تا تیر توی پاش و یه تیر توی دستش میزنن و حسابی کتکش زدن، اعضای محل هم هر کدوم یه انگشت توی کونش فرو کردن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137033" target="_blank">📅 13:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137032" target="_blank">📅 12:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137031" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137030" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
پیوستن پورعلی‌گنجی به الطلبه صحت ندارد
⚠️
⚠️
ساعتی پیش برخی رسانه‌ها از پیوستن مرتضی پورعلی‌گنجی، مدافع پرسپولیس، به تیم الطلبه عراق خبر دادند اما پیگیری‌های خبرنگار فارس نشان می‌دهد این خبر صحت ندارد.
⚠️
⚠️
پورعلی‌گنجی هیچ قراردادی با باشگاه الطلبه عراق امضا…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137029" target="_blank">📅 09:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137028" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
امیررضا رفیعی قرارداد جدیدی را امضا خواهد کرد
🔻
🔻
رفیعی یک سال دیگر با پرسپولیس قرارداد دارد مشکلی برای همراهی این تیم نخواهد داشت اما احتمالا با تمدید قرارداد در جمع شاگردان مهدی تارتار حضور خواهد داشت و زیر نظر حسین اینانلو کار خود را دنبال خواهد کرد.…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137027" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137026" target="_blank">📅 09:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137025" target="_blank">📅 09:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137024" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTI0XSClbbR-ay0b4XaV9I2Y1ji0-0AfryM2aIc4zOBYVplj4DpEDg7k1wOhejHBmkZipUy9LciEzpLQjFzdeGXKK580i2nTyQRMRAk0yG-ngikQX8uYRMNba5LmdV8WYLSWrGW4cAXqjoS8mQut7S9IqDH8aQBPlAyULH8e2q2WyT81jYQVKVRCDB78lkxht6O3LPTsVxYFEPHGKxjVgdYrFNOiQqequ5YFAWvwOmiKPdnwviy8HWUvH1TxzI7ZGfbgPfDfvuoOOIQsiRlYk7zXKciIdiES-2ScPdhDy-QkSO_9R8mbYqX6w_kauSyfCiyYGaO5biMtc4-A_bGrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137023" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtXE2Q801NugBP208v5RN9WYMVzkNxcgJo7bssEFwVQinPZ9uxJcWsZELnDC7Jw7hOlW6c9sIuIQQCRpIMXDElQ_SBnbrB594pu5L0ie_WBByFDz4P-6FhCKWqf3mEIQ8cGCnCN1zpiImTdij374e4sBAquex6w2uuj4_V1NTjOK5WqCoyL-MjmZHjvch2X1ejWNukHLDmdlH3214kYgiY3y8Mxb7zvZ-vQFWlwrAj0RYsDBKhhg8i1K6eq8wCqyySKs-P4Hkw0sX93gmLG1iIeDmIXQ6-oiu6YrFqxJnQ_TIwstJEMtpVcrHGg-5lw73Le_Mf5w9zipNhvfWFDVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۰:۳۰
[
ایتالیا
🇮🇹
🆚
🇺🇸
آمریکا
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137022" target="_blank">📅 01:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De1ixxGiPnP_U9F7n3COcxMLeZJe-R5mMuijsiWdZHsWxeZXB3z-wjRnSwZ2ZaHsAghMEDx_VwJ7RoKFxVyNV1qwHCmxHrWtR0uMugHozf_Az62EXugFphV38I6YZdDjnqKPvyyPftkBWZWbOod6ci52vVVRo4T0LBAKFYiLvdxdtont15U9JF9nf3smUpmQDOae7QAhaaboig7NXZ_frAk2iQAtTgbvnxLFUNvfVvQSaQA_m3j4O8JlxJ1s_LawRIYPlosP4t9_LBg3KFpsttQNemUVOQ-d7CbrFArJOeWj5-HE47et7jCfr-tsRSixvktQ_osiu4Yep3kVEEHfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137021" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️
❤️
❤️
❤️
❤️</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137020" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137019" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
تراکتور از جذب قربانی منصرف شده و کناری گیری کرد /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137018" target="_blank">📅 23:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137017" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137016" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔽
مرتضی پورعلی گنجی با باشگاه پرسپولیس   به توافق رسید و قراردادش امروز فسخ میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/137015" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137014" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137013" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
دنیل گرا در تمرین امروز هم حضور نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/137012" target="_blank">📅 22:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137011" target="_blank">📅 22:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137010" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
دنیل گرا ۶ هفته از میادین دوره و ممکنه باشگاه باهاش فسخ کنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137009" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=QEAR3T6R0JfSLjWCuVcMHZLmeJC9xKeQ-O1pB6Ww9QbU1baA6Z-YGob-WU7Cx39AbU_CzB2PhImWhjbjX2Yyt1TUDUYu7a8DgTj7BsGFmgvSFHXrJ3fCCfhMA5EIun6WiP4nD6jcw4hPRMbf-q3A00SBweLNATf70i5bAVQYl7JUMtlaZJgSShTE-GoLVHHXA3m9EOxz5qy1XHR5_vTFqmwdQNHqIUUn5ZsUOlrm94ylOrUtdALdSJv__wsCYSkoTfyesj9dpvwJjLM-TDuuziEHovvUdtM-ugfSLlk1drzYUjydikkuyc85i1S6xn07xTOSf29MVaXt7XYxHr7OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=QEAR3T6R0JfSLjWCuVcMHZLmeJC9xKeQ-O1pB6Ww9QbU1baA6Z-YGob-WU7Cx39AbU_CzB2PhImWhjbjX2Yyt1TUDUYu7a8DgTj7BsGFmgvSFHXrJ3fCCfhMA5EIun6WiP4nD6jcw4hPRMbf-q3A00SBweLNATf70i5bAVQYl7JUMtlaZJgSShTE-GoLVHHXA3m9EOxz5qy1XHR5_vTFqmwdQNHqIUUn5ZsUOlrm94ylOrUtdALdSJv__wsCYSkoTfyesj9dpvwJjLM-TDuuziEHovvUdtM-ugfSLlk1drzYUjydikkuyc85i1S6xn07xTOSf29MVaXt7XYxHr7OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرین سخت امروز شماره
1⃣
🧤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137008" target="_blank">📅 22:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137007" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcK3lGoISh5UP-XJkbMSfvad4dYyZ5wX_M2nCsfWNnUef7U-yM-ZzdVF_jY4pc_WexF_EmVAlm7uKj7FtB0rGDAROBbSJbt_1WjZtY4ebvf5_IZX2rF--6P_0Uf5KTWiq75pwXNFY1CMZqVhTDQRy2hJfIgaNSrhXDinFgieVspVOXwv45yd-VBTkZ-zk8aIqwrlMBVq9w4nvzCdV9MUvXlB5ZL6xWYUDf0hfo8CLIZUJ5fcjUUswyeT3suOS3J7ObacxV5mQlWEGULOHhkvy2f2NHI0R1lW3kTL91ITw9xpcnImhwji88FumMCZ_yciY9kw0QQF9gk0Avk6tXvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137006" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
یاسین سلمانی ۲۰ دقیقه اخر بازی دیروز اومد زمین همه جا حضور داشت چه حمله چه دفاع
🗣
🗣
پاس گلشم روی یک ارسال تمیز شکل گرفت. با وجود اینکه جلوی چادرملو هم بهترین بازیکن زمین بود نکته عجیب اینکه چرا رسانه‌ها اصرار دارند مازاد بشه.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137005" target="_blank">📅 21:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdF8FC-xeIN4ghshL_Hta4JKzuFERg1u9lEbcW_0LfiQqbPLunP3-Q1e5nLDngXJxbOiy1nhDjWINMVj_JvZM-6x-ZAJ6bLODclaCmefarD9EIk0_NKYOnxff2EkyIn71hsI_WKAOcAs30aZeBR2DBCfcIQ7j0ZxvivH8E8Tn5jVI_v8qtx3XDHBtmRehOWWFcq8XcXBPCRPHraXi-fP7GWWgvsnVs-FEbdDE0WzmoD2BGRXs-rytI9lLT4Z2x0jyyul8q3t54FJs73VPqYDrl5nqXIdynl-hgCBCjlF3buXyNNPxgMwQ7wzawOC_9dswWdEfTL7iSrSz-7uJ7h3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگاهی به ۶ بازیکن ارزشمند لیگ برتر در سایت ترانسفر مارکت با حضور سه بازیکن از پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137004" target="_blank">📅 21:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPrAPZ2wWm4W_XYxYrc0TZLGUz6csZyTgC4H2YNnBjZVRT49fNXwQAVZDAfjhcs5yg5Du7OUWteIkoKH5B_rZIy29TomYuiO3oj-srHOGnqOj5cBPIHWrQks7C3n41fTL7tqb8fDEGhkTaXdG4VxtnBMQiQH2_janz5nBZxxXwRaWaURndzBSXHPjUHtn6IqISpuCAmbpMO7J83B9tBIdrVQ8ARfARk3fJpH5MqR7pzXK8_wwm0eioxnSJcdMs52wEw9_6bQuo2wmqb5a3vy5mO9NWc_0mqM0aYltNBfs7TV0alrqkkBa7Hda1Kg3yN4k5uX2Qz9z6VzRRMG1oteKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
زیر و رو شدن چهره پرسپولیس پس از گذشت 2 سال
🟪
🟪
از ترکیب فیکس پرسپولیس مقابل مس رفسنجان در روز قهرمانی، تنها حسین کنعانی و استون اورونوف در این تیم باقی مانده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137003" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137002" target="_blank">📅 20:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN485V3dxf4j0PpnEDG5QMjMe9XEqt3MubwWRX8DnM-aWo7KYlE1UeKlhVlrGiBh6FSK65SN52E1V3cGo9UTVOg2AXQHmWoRHTd-XkJ15hcf-GzT6CwZghJl-AyF5JYEeKP7yKWzDlqC_pmLcy3WT34NhGW0zzgBea3k3jFgxfswITpI5aTvgUlvpkTwkf49YoPM2szchHIdRFXYmMBvyGQZR8ffXjYvOEp-dPBiX3LuFSJjeI-tRxC5tq1LwTf7drNLH8nl2UQJhN5_JaZ4Ft0OFQ8iydaLHATy8Krqjzelaf_PCao5Cav5y4Wlf2USOpR5s6kfZCRhU97pMW3NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
اوج
هیجان مرحله برگشت مقدماتی لیگ قهرمانان اروپا همراه با
اسپورت نود
🇪🇺
شبی پرهیجان در مسیر رسیدن به لیگ قهرمانان؛ تیم‌ها برای یک گام دیگر به سوی مرحله بعدی به میدان می‌روند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137001" target="_blank">📅 20:48 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
