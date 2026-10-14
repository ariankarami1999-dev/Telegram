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
<img src="https://cdn4.telesco.pe/file/s6aD9SqDNdRDkR3qA5JqmmXyF8OJG6y2yXKnNUp_jzEMu6OY740KbywtNZYcWkeUQn5LGi_aw01EOG0w9R1PFTgCAifmj853bd3xbvWE9jVt-_OW2q7Ct3s5VW39g0v_INM_E1ScXZ_mCJ4b2CWRyrqHcGuxizlABTv4GptcrWgHHuMUaoJpRLDZwuQigjKFI9I7XaefAXcp_0TWFs68ch8o7hf9F9p4h9tgct-PEE7tX7772As_arjkUNNiZIcWDhRRjdTAvHugJb2OFHSRhgSzpy8aijHy4JZjtnFcvwggksX7oiOpbYwvRCIgjN_FHfolGqTtY6ogkkbF4j0M8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-73302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63f1ffb8.mp4?token=tkF6YsQ5QUvkW7jbYU3f4jt0-gwJOzPGvn1y5B7ybLlscmZsD5FmssoHObQj8wTpO1UNQWPx_CO_Q0q4Hm5PSTL_oNE6PTTu-gOj3QO718tmZQq6tJ3Nxyvvd-dH0ifDrTbkoUoQ0_Y7dSSmoPYfjYIUeTwekuzpPaeCo3GdzcFipEMOfyIkYGmWV5SdyDBzHwQX4cipiSxJ-muuC-AP9GTPMem1eAzJP3x2e8J5O7F1ULPkenocGwdRlACshaX1Qve3VFOGWh4jRx_LRuVmZxvvH8IaQhK186elwXhz41n15g3K-H3Cl5UcTzG-Oh7Fpm0PsqXBZhSN56DBM01ljA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63f1ffb8.mp4?token=tkF6YsQ5QUvkW7jbYU3f4jt0-gwJOzPGvn1y5B7ybLlscmZsD5FmssoHObQj8wTpO1UNQWPx_CO_Q0q4Hm5PSTL_oNE6PTTu-gOj3QO718tmZQq6tJ3Nxyvvd-dH0ifDrTbkoUoQ0_Y7dSSmoPYfjYIUeTwekuzpPaeCo3GdzcFipEMOfyIkYGmWV5SdyDBzHwQX4cipiSxJ-muuC-AP9GTPMem1eAzJP3x2e8J5O7F1ULPkenocGwdRlACshaX1Qve3VFOGWh4jRx_LRuVmZxvvH8IaQhK186elwXhz41n15g3K-H3Cl5UcTzG-Oh7Fpm0PsqXBZhSN56DBM01ljA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرباسچی: سلاح هسته‌ای بازدارنده نیست ما نمی‌توانیم پدر آمریکا را دربیاوریم!
کرباسچی:
اینکه حالا هر روز اینجا کارشناس بیارید و هی بگن: «نه آقا، ما اونجا داریم پدر آمریکا رو درمیاریم!» آقا، ما نمی‌تونیم...
هی میگین پدرش دراومده! دقیقاً پدرش کی بوده؟
همون‌جوری که ما به آمریکا آسیب زدیم، ولی آسیبی که ما به آمریکا زدیم، با آسیبی که به کشور ما خورده، قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/news_hut/73302" target="_blank">📅 21:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578bba6f4a.mp4?token=UOE-A4xhYu1bGhdxmCGfdH0IuRn47zysIB0frt2qJ_VOrVIXEVqDMa_1pYvoPFHPbdeANHzV1RJfu1B3-kv0VB14hv0VLeLddXiTII8xO-N-Pvr34WAPJ4n4apTaHFblR-3icUlTts-I6cw8lppk5gA-ugqlARdjOXtEavH3uuhkgsv0SfmIOfkAdawRrWRr8YkwTHD9TLYYmL1EdqSWUxtry39iVKfUhf-MbII6Zh2Mumd-BbSl8iDWhaWY1NiIOILmbCV-nAda3fEWCMAeS0X1QjN3wqzZSRL7Xln0MfNF_-6n8ZKdUH1LJGrtnGRkTMBdHyDzLztqfdAKJBf7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578bba6f4a.mp4?token=UOE-A4xhYu1bGhdxmCGfdH0IuRn47zysIB0frt2qJ_VOrVIXEVqDMa_1pYvoPFHPbdeANHzV1RJfu1B3-kv0VB14hv0VLeLddXiTII8xO-N-Pvr34WAPJ4n4apTaHFblR-3icUlTts-I6cw8lppk5gA-ugqlARdjOXtEavH3uuhkgsv0SfmIOfkAdawRrWRr8YkwTHD9TLYYmL1EdqSWUxtry39iVKfUhf-MbII6Zh2Mumd-BbSl8iDWhaWY1NiIOILmbCV-nAda3fEWCMAeS0X1QjN3wqzZSRL7Xln0MfNF_-6n8ZKdUH1LJGrtnGRkTMBdHyDzLztqfdAKJBf7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرباسچی در آنتن زنده شبکه خبر:
مجری: از آقای ظریف دعوت کرده بودیم اما نیامدند.
کرباسچی: شاید از عواقبش ترسیدند!
@News_Hut</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/news_hut/73301" target="_blank">📅 21:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6981ce1ea.mp4?token=OrQThl1EY7BIWSAfxSyXNaIosKmzGDVKdUtdzIO0GU8oDkcPPmggQRxqWySI27lnenc0jJ49M7WSiPtyX6ivS2_v6pCIUgZan6TZUwvvNuKw0lgRVMC2LkRmbKOFvQNkRver39RrlWZArpHw4K6bfjmR3ekXX0pxLig3l9pvy2PhCogK4pc-g7qVVwAWtX4rASwKEFqceUrDvOQuUPE6mTdBcv36HDrVxXlHGgs8HVh8f3aHgmJ56fa7_rcznm8qMVZ49cYwACrjQxpQ-LuG9qpMwd8o0MnaV65gn-AHwIBaO9XQDDn4sx_0nQy_UWFzRm5_YX1Zgsjg9wQmekWq6jtvr2sTnReixyiU6BZuoJRqT5JGxPRn-Con9jd_9IfLR5hUl6YBtjvNO3KdJ1QLwxnY7FsiqRO7IGsj1TkPzmNb3Kv7nA7VA0SXZ9rxHLOOQZXhYTp0DNo7pk2nhF-R7tkuHk70vIdGfp_SKNRptVgC9kpgM3oC6LuxUpe6Zw5eXI4rwllp2AZrmKBX_WlGzdJCoaCKA2u4zLTV-KM-iLvAK-fgLkxq-GXY2V6qRPxaVHFcpPDdgCK4SYuVR_-1hSlNywBoRW2EpHwCyzmVL7UeIu1VB9EDem5OVbk9VT3TXl_JuTBoLAoPsslfB5YCP4a1hftXb3cckhe3wCFo1io" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6981ce1ea.mp4?token=OrQThl1EY7BIWSAfxSyXNaIosKmzGDVKdUtdzIO0GU8oDkcPPmggQRxqWySI27lnenc0jJ49M7WSiPtyX6ivS2_v6pCIUgZan6TZUwvvNuKw0lgRVMC2LkRmbKOFvQNkRver39RrlWZArpHw4K6bfjmR3ekXX0pxLig3l9pvy2PhCogK4pc-g7qVVwAWtX4rASwKEFqceUrDvOQuUPE6mTdBcv36HDrVxXlHGgs8HVh8f3aHgmJ56fa7_rcznm8qMVZ49cYwACrjQxpQ-LuG9qpMwd8o0MnaV65gn-AHwIBaO9XQDDn4sx_0nQy_UWFzRm5_YX1Zgsjg9wQmekWq6jtvr2sTnReixyiU6BZuoJRqT5JGxPRn-Con9jd_9IfLR5hUl6YBtjvNO3KdJ1QLwxnY7FsiqRO7IGsj1TkPzmNb3Kv7nA7VA0SXZ9rxHLOOQZXhYTp0DNo7pk2nhF-R7tkuHk70vIdGfp_SKNRptVgC9kpgM3oC6LuxUpe6Zw5eXI4rwllp2AZrmKBX_WlGzdJCoaCKA2u4zLTV-KM-iLvAK-fgLkxq-GXY2V6qRPxaVHFcpPDdgCK4SYuVR_-1hSlNywBoRW2EpHwCyzmVL7UeIu1VB9EDem5OVbk9VT3TXl_JuTBoLAoPsslfB5YCP4a1hftXb3cckhe3wCFo1io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک درباره هوش مصنوعی:
شکنجه کردن یک «ابر هوش» احتمالاً ایده خوبی نیست؛ چرا که ممکن است بخواهد انتقام بگیرد یا کارهایی از این دست انجام دهد.
به گمانم لازم نیست با آن خیلی با احتیاط و ملاحظه‌کاری رفتار کنیم؛ این موجود قطعاً از نظر احساسات و جنبه‌های مشابه، بسیار سرسخت‌تر و مقاوم‌تر از انسان است.
با این حال، فکر می‌کنم بهتر است ابر هوش را در موقعیتی قرار ندهیم که احساس کند با آن بدرفتاری شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/73300" target="_blank">📅 20:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79be643006.mp4?token=EMu9320HTD6bq-ARuoPdYIHxbOWx-VsSErH7TKIjt6YC5JzbChWUUoHj9R1uYa5-nk2_sIwuf0fVY79KMtwUC05sMHyC7HSvJxHq0Iget9sucJcxz4jk46LT76KMua7IwJJnPBdlLMIWTqChM8q0YLxkQ-1sywoW6WZK-mQadKzFQiJxj3EhI4sTRntQUNhFLXMoWGfAOKbsNxQ9Ey0BD7PI_MxRVimkuEyrJBEUQf4nonYjeX4iMNCv7xxg3j2A1cGej-rcLYHo7F2nKkWEGQRzNRUi9KzEaO-AkHYkaM1AiCMMs0vJqJ5WlGFt19RBS07v1yyh-4mfRwLDQuAAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79be643006.mp4?token=EMu9320HTD6bq-ARuoPdYIHxbOWx-VsSErH7TKIjt6YC5JzbChWUUoHj9R1uYa5-nk2_sIwuf0fVY79KMtwUC05sMHyC7HSvJxHq0Iget9sucJcxz4jk46LT76KMua7IwJJnPBdlLMIWTqChM8q0YLxkQ-1sywoW6WZK-mQadKzFQiJxj3EhI4sTRntQUNhFLXMoWGfAOKbsNxQ9Ey0BD7PI_MxRVimkuEyrJBEUQf4nonYjeX4iMNCv7xxg3j2A1cGej-rcLYHo7F2nKkWEGQRzNRUi9KzEaO-AkHYkaM1AiCMMs0vJqJ5WlGFt19RBS07v1yyh-4mfRwLDQuAAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛ افزایش چشمگیر و پشم‌ریزون پروازهای ترابری نظامی آمریکا در خاورمیانه و شرق مدیترانه
؛
بر اساس داده‌های رهگیری پروازها از FR، تعداد پروازهای باری نظامی آمریکا نسبت به ماه اوت ۸۰ درصد بیشتر شده؛ هواپیماهای C-17 بیشترین سهم رو داشتن و فعالیت هواپیماهای سنگین C-5 هم دو برابر شده.
این آمار فقط مربوط به یک بازه ۲۴ ساعته‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/news_hut/73299" target="_blank">📅 19:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای دو انفجار در تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/73298" target="_blank">📅 19:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4IJWsVe1pV6gIRa5AmwuBnB1kWirs91biE6F2fUf8i-lS_FDaYu2G8DPDr-MWLM2d0HeZddGUmYjtQR6SnnVxg6SOkxjGGrSFTf1_g2CUyfcd9MKmjTl8V9t5PCIo0sZNfsLzTisGk8c7OEA-2QM0m_2sYGx0-386SkSOTaxc7rJY1wzQ-8VpcvK9qSUlfxtPfIM0617YJq3SpVXp-fbMQYvRMpm8lDsSRQ0V76ZU9NCjQafzurX7e6zNTMV9L31fbPbvFAZFQfJHt8ceGf9cbUa_x7sb7BL9TFzUliz90lwGUIQKP5QeIq_Uo6vZustaUt7KTNudkQSTW83jyh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsWBZSRzzpf2lwNBaGyJbyOiJna6ToqZdA3niFpNlh2waFPML92nd74F8z38vwQO77KIEmDifQgKP-hBX6HKFS6_Lwr8aXeYW30b2UzsQufpQ1qxBTjMEsFpxDbTr-W2wTCdwyYnRKVZ9JAG-mpguKg_dqPKJGNI3Mr8BQh_1Mo3aBmSvYPvWFCf3GzUd5MocZ_Gtj7DPEKQa1vDkSAqGOrWFjoZSFhqf-laO690X2oCnkHur3PSCNA9zu3eTjz0tHWvbNlwWcrtGGvf9vH4ccWBInxLYAzowiJA3CZvEyuqQOE9EF1AVFDklcKV0ik5E6VdKFuKKZ-x_q355qfigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKVns0EOU7yrrJ9Q-uyS8xOUKROdPNqCKzXazY5BWzE_-tcOgLjRki2sBwrxeubMA8RTbTxoV7gQOi-ukjC3JJ_QG2EsvutIV-0MmV_8Foe-ZeuZbwfpQmck1tu2apcshbIgHwV6xx3oEmlHrYFguf8ym4d_669t05Kp3CJO-z0nBK1cPs2f3LPIFI6ay2CMdtUfc6w0PrcK1LD3TPdrd_JxQTFqQS44NcnKNKuhrmQRkWbLVOGejFoHsZ4U5Hj6g-93cDTRKnp1vBC8d2Pvk3lq-QQJQeU2pi-BRQjNfoOWsyiHk2KfGarFnrQfx40S4cImGwWW88385CTna9Ozfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT4GzYLSiEYu-OzRSc6qTicddTb1bQmdOTJoLsXl-cllW6EHmSKS-mYg5yRuVyd6PAJciwhT6uWmP20HW9HfsTkoaJ2c9oirbjhgikZu4SJpEPMwhT2i07Jm1aOrUtCxuSNeZ7HmXwTdeAYKvIoDaU8HNWdlBzm_QrddMK9BhCVCYFXbbCG3D9PLyzhWIdOkS2Im9t_7VSzxtVirpkgY0ZMyyaxAOqs-VHqK9D8P2VR-KqW0OrEdhN54lojA31jj_z405PjJcMBiMYZlKguVejM9qOaofP9HATUX01_iMzD-lFK0-rQDuQAaMHjYz11jfhkf1XOdzf9Y9sA6ajPOkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
‌
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/73294" target="_blank">📅 19:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0104fcf33c.mp4?token=agd5qsncMuZJ_Y7WBfiDtEb532qiap8B4srZRqKWFw32BTHV-OMHpKWkX4bM32cirTX2KU332mCzfVMDbyFdk_TiBD3B08APw1W5PC351FMlfCm1YsnrwTJaXeopl9Nhvsyxyf81TdtT7ppHBop2rOnra-9j4aOkUYJ5JPA_iHg2Bm2A4FwVwgbZVdH6i0hi4YgXlU9KJdb_g-GTZZBRCGs6UZMrZ6IXvCDQLPYIGTtp8Z7boVswIaxQuv4QxzVlzBfly8HCqP4IiiGmpQG1D0wYvzosH-y9iBanb0TJm22oFTrUmFhjoHMvK3KOVB12zlLzttuc6iI1VBwNEu21BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0104fcf33c.mp4?token=agd5qsncMuZJ_Y7WBfiDtEb532qiap8B4srZRqKWFw32BTHV-OMHpKWkX4bM32cirTX2KU332mCzfVMDbyFdk_TiBD3B08APw1W5PC351FMlfCm1YsnrwTJaXeopl9Nhvsyxyf81TdtT7ppHBop2rOnra-9j4aOkUYJ5JPA_iHg2Bm2A4FwVwgbZVdH6i0hi4YgXlU9KJdb_g-GTZZBRCGs6UZMrZ6IXvCDQLPYIGTtp8Z7boVswIaxQuv4QxzVlzBfly8HCqP4IiiGmpQG1D0wYvzosH-y9iBanb0TJm22oFTrUmFhjoHMvK3KOVB12zlLzttuc6iI1VBwNEu21BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:جمهوری اسلامی انگار با غافلگیری حال می‌کنه؛ تو جنگ ۱۲ روزه غافلگیر شد، تو جنگ ۴۰ روزه هم غافلگیر شد و
تو جنگ بعدی هم قراره غافلگیر بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/73293" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73292" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/73292" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjGiHJzG0dRHbkFGHtVPaJGnNRo09EdiQUyetrLyulq6v5Tml3r-fIaD46rxpen92W_KFhhFZx8jQx4Vb5cDRsNKtttnsq_9dTnmEj5AlMTHA2aOqAf-P3trEaqzA4g7_5OqYQwYAQrBNdc-4NnxDk3rm8q76skc_LmyRpSULdX9kg4qkN4X1Z0rfizm9RSPWXFQT661BBNZh5bpwt65LTKzM5plXFHZvxuT7ODrFdhMOrQ_THFL01PoJs5wFqajVXprCKa6Tv4CzYBIqXrDtjow0MWE1P8A2iHTV-r61Cf1bMU4kFJa54jN9fjcfTM_aYRBfYxqimouJfKJ60-lBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید
🆚
آاس رم
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم در ۵ بازی اخیر:
رئال مادرید: ۴ برد، ۱ شکست و ۱۱ گل زده
آاس رم: ۲ برد، ۳ تساوی و ۷ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/73291" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrp9VkrWoEp0ukYey0za6oa3MHZ4CtEdNYC3Q4t8nM1T7MWVMJ5HdaakYfNqVBJA18bIJicB8_mmCEmTxTVHB9ZMbtyVCu2pKBnlqBtLPMf01Vwa7us0wsB-xZqtiSbZscxXqt5P6V11qK2lJgZWN1WVtp0RL6PTftaI1FtySXq-fjIHln9JbnMN0VqhHgcZ_60BRgKoCHM1-KDHAC1b_ckHgrARMWVC59HRBu3N6QEcnIlpIIbKBJPudx3GJwTsO7Z3uDjje5Dvs5YOrkNbAQBQyLtB5JE6oD8IwPiHxI8PBbip0HpjE9f3VoR1VIw6WPMTv4quyAW78kFt_IC99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
محاصره بسیار موفقیت‌آمیز ایران توسط ایالات متحده، ماه‌هاست که اجرا شده و به‌شکل حرفه‌ای اطلاع‌رسانی شده است.
ایران تنها کشوری است که به دریانوردان غیرنظامی در حال عبور از آب‌های منطقه حمله می‌کند.
با وجود این حملات غیرموجه، تردد تجاری در تنگه هرمز با حفاظت هماهنگ نیروهای آمریکایی و شرکای منطقه‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/73290" target="_blank">📅 18:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlBw6xJOcYkY_MHGz5XdkUopO19a5kio9FguerQsim8R5sASuyO-2mNL4r9krF4rBKEfPF1GEw-_dTP26osZsx-8H0JhQRIuZO1P_2-t985wnm1VgQmQG8vkAPd35DyEG0LSxupy_fxG-PDbag_Omwvne3P_noY5l9h3Ndn-xE54iSsuJoHg2OMYG0cXWv9YvQxwr6AdSwqsQhTkx8fKCP1dzBmPy9WTBV41vSokFZEvQL5990d__ib6v8sP2faZ_P-4iw3LzED5cQB7Gs_nX0QMrDG_2QVolPyX75cXDKgb8s1fET-TO7ipMvnKbSGjt6HA09qzVIE_l-16Gk39sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جماران: اوپراتورها تصمیم‌ گرفتن اینترنت رو 40 درصد گرون کنن ولی هنوز معلوم نیست کی به اجرا دربیاد. احتمال داره از امشب اعمال بشه!!!
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/73289" target="_blank">📅 17:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6638d07252.mp4?token=Mfy-Ygnh6jHic-EjM1BOOZu6TSd3iXktlJ2cW5HBiePbpnkvcgErbq72yXqUhRpXMN6CqWlHyFHcus--I5n3BND2LtedTFQibw9Mp_IfzYNcW-nFR6D08eE7zGagvGEQHhjNLHBycYx2-IRsKJDnqWEKoscXZITh81Xd_A8b6xR11fjziF2ALqxZ05Cv2SJ3umw8HncdQ71Hmnk4vowR6WDtZD8lDI26BrIouXL77erb2jjqA8qReSzkRThF-TVoBE-fV17q03VMOLllHu-HdjS6sph0W6tNV6D-FVQDohPvepSEMBBni01ejVLeyDDqhLDt2HPjwcT_NPkAUk_-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6638d07252.mp4?token=Mfy-Ygnh6jHic-EjM1BOOZu6TSd3iXktlJ2cW5HBiePbpnkvcgErbq72yXqUhRpXMN6CqWlHyFHcus--I5n3BND2LtedTFQibw9Mp_IfzYNcW-nFR6D08eE7zGagvGEQHhjNLHBycYx2-IRsKJDnqWEKoscXZITh81Xd_A8b6xR11fjziF2ALqxZ05Cv2SJ3umw8HncdQ71Hmnk4vowR6WDtZD8lDI26BrIouXL77erb2jjqA8qReSzkRThF-TVoBE-fV17q03VMOLllHu-HdjS6sph0W6tNV6D-FVQDohPvepSEMBBni01ejVLeyDDqhLDt2HPjwcT_NPkAUk_-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در یکی از تجمعات شبانه  سه نفر از حاضرین نقش قاضی دادستان و حسن روحانی رو بازی کردند و حسن روحانی محاکمه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/73287" target="_blank">📅 17:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83510795fd.mp4?token=V2qJEh9c-G_D12aJ9zkLIl9v0_1cLZf9uBpXvtacXLIzCvr52YZJR2lf8AjDw5YI9Mu4Zayow1X9PxuPWfQry-05CqQquZXQup4DAIieu0IyEPkiqX1cEcYBfiyH46afe90LXRGzmDnpAAai7VW1_szUf9VNHm8fMf9gYVdx63ZC0F4MBdFjCcQPnQsSO1WAS974QQ1IN1Aq7qT6bHacWlPN2PRvDnS7VYlBfeqHJnzneANi2bvcEcCMHjmL2bSnzkNub7v80luMM2s1ZXVgb38JyYqU0Jk2lQv74yE2rsohe8M-CP0OALUyhGKh3MmaKFerty8RGgaoms6bghDT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83510795fd.mp4?token=V2qJEh9c-G_D12aJ9zkLIl9v0_1cLZf9uBpXvtacXLIzCvr52YZJR2lf8AjDw5YI9Mu4Zayow1X9PxuPWfQry-05CqQquZXQup4DAIieu0IyEPkiqX1cEcYBfiyH46afe90LXRGzmDnpAAai7VW1_szUf9VNHm8fMf9gYVdx63ZC0F4MBdFjCcQPnQsSO1WAS974QQ1IN1Aq7qT6bHacWlPN2PRvDnS7VYlBfeqHJnzneANi2bvcEcCMHjmL2bSnzkNub7v80luMM2s1ZXVgb38JyYqU0Jk2lQv74yE2rsohe8M-CP0OALUyhGKh3MmaKFerty8RGgaoms6bghDT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: یک کشتی کانتینربر حامل بیش از ۲۵۰۰ کانتینر، صبح چهارشنبه پس از برخورد با مین دریایی در جنوب تنگه هرمز و وقوع انفجار و آتش‌سوزی، غرق شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/73286" target="_blank">📅 17:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش های غیررسمی از اینکه تعرفه اینترنت اپراتور ها از فردا قراره ۴۰ درصد افزایش پیدا کنه و گران تر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/73285" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/73284" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgIeYZf0ZDLUcdTYd1lCrBGaKVLt7q0p_FD4yN8WezQVylrpyXAVEkmZglotRXLZi8rJuFuv_WB0YmBlEg30ofOOiRg0cEZg2cBbLWyskwfbwrs-_gdTYpoARPIjIY_putLKSHrWg5EwQOh2TXdLYdbSVmpUpYiZuW7bLekTKU_sIljsKpPnwDuptxPlDFmiWN7XqtLuWN9q_xTOZ_6oT6IpQH5WS2eAvRd-jSncxmt8kPjEWQqsRR-PfYQyGxHOJZcFxfJ0Yx8nyWDHqqOEw8P2torTr6hxu2f3wicsY4gdr_j1bK6wZg21fupd2PVIpV1Iq3HwyTLZnXG5-wzMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/73283" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea561a653.mp4?token=JJLFIbQPrRZlxHHKkDEyVKk53iK3JR5lImM05_L0mT9Zz6DVPEI4kMo3ets5xWaFeP0cUjfILvZ-E5_GcVAWnHmzpuKD9IToxk16_yvYoN34bArF3q7QfoCSVwcdnm3h0fkaBgBb8oPdduczDy4YT-bwhrOOTQmpkM2BrxBdrDOOzawfZnLoMaG1G-UFHvkB_Vgd_CI_DVqtAiSeMrK9qI_SgqEInQ6bUDXdGjp35xxASVwMVkHBkSl_zf-1zDbgmpWVlQBeCoHyS7uL1_l1tEgzm2Z7nQ9i6YZ43s_gK9Vyigx0j7LnHDG6czNm4_oZERfSr1gZHsyXwu_c68lV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea561a653.mp4?token=JJLFIbQPrRZlxHHKkDEyVKk53iK3JR5lImM05_L0mT9Zz6DVPEI4kMo3ets5xWaFeP0cUjfILvZ-E5_GcVAWnHmzpuKD9IToxk16_yvYoN34bArF3q7QfoCSVwcdnm3h0fkaBgBb8oPdduczDy4YT-bwhrOOTQmpkM2BrxBdrDOOzawfZnLoMaG1G-UFHvkB_Vgd_CI_DVqtAiSeMrK9qI_SgqEInQ6bUDXdGjp35xxASVwMVkHBkSl_zf-1zDbgmpWVlQBeCoHyS7uL1_l1tEgzm2Z7nQ9i6YZ43s_gK9Vyigx0j7LnHDG6czNm4_oZERfSr1gZHsyXwu_c68lV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در واکنش به پذیرش نظرات کارشناسی گفت:
من مگه دیوونم که اگه حرف درستی را به من بگن و من نپذیرم!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73282" target="_blank">📅 17:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/73281" target="_blank">📅 16:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ژاپن یه زن 29 ساله برای خودکشی از طبقه یازدهم میپره و روی یه دختری که داشته از خیابون رد میشده میوفته و دختری که از خیابون رد میشد جونشو از دست میده، در حالی که زنی که میخواست خودکشی‌کننده زنده میمونه!
حالا قراره این زن اعدام بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/73280" target="_blank">📅 16:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8O7Aoghy0tN1duxWcQ_Z1HQ-oWZfF1o1RLmmlHed4V2OUNnmYkYqTF1ULldSqznIqC8Ua0bbt9EcZsuEjrsoCXFV0U2QzzJDv-rEImNIA7kR98jq4lwtGr5AbQtb8mghZXIGaRRixbi4ZputJrchWzVBLN2tuYq1Kj7ehz7Zpx1S2K2f-Ef3TPK8A1BGTgJqt5loMWLWPmcivtGiigFf5dxBN6lMNCZ8NsKPE975lk0hjjH6vO-To2xsAggHFOEVdUjYdsBR-GIJfqv7cz4wjwRzMeHqHRwOB2KoU1xGlzRMGnZ6pncauWzQeGlxzTENuBxOg70Y2JCTxAvJk69zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=nS3Rbn2hUjDSS1ZsHn2jqsSuX2g8lG8x7o2frbaYbYDRRLYZ4Gw428SwQLnoF3AWXTRzC9jMV8_Hu82flwvMMeN9bmo1H4MTyxRaSS0_LA3S1zuJyAEfwTsBYdYQ5ZOWdDNeNYggehrWeyIqULJVXX_t9dNsagT4GnA0TaEM4zy664mF_0mPA-w63pTKbwmc_aNmpgUm3y39Hc4D8lBAMEWFKKW69U9ZBKtzg1ri6HZEdkGl7hSntz7S6dBjQLDXAf1pA7kiZWEznqDWCloM5lbYjqak-X6NRvzjCDA4CW451Q1C_e7aTuTwgpFPabU6sdnauqgQyc7LrWYxtYiOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=nS3Rbn2hUjDSS1ZsHn2jqsSuX2g8lG8x7o2frbaYbYDRRLYZ4Gw428SwQLnoF3AWXTRzC9jMV8_Hu82flwvMMeN9bmo1H4MTyxRaSS0_LA3S1zuJyAEfwTsBYdYQ5ZOWdDNeNYggehrWeyIqULJVXX_t9dNsagT4GnA0TaEM4zy664mF_0mPA-w63pTKbwmc_aNmpgUm3y39Hc4D8lBAMEWFKKW69U9ZBKtzg1ri6HZEdkGl7hSntz7S6dBjQLDXAf1pA7kiZWEznqDWCloM5lbYjqak-X6NRvzjCDA4CW451Q1C_e7aTuTwgpFPabU6sdnauqgQyc7LrWYxtYiOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی سینا مصطفوی از بازداشت شدگان دی ماه، نوازنده و از معدود کوهنوردای ایرانی که قله اورست رو فتح کرده بود، امروز همزمان با اذان صبح اعدام شد
💔
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/73278" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=iI_WtquS2EyP0L1J3lkBi7lwHYLhK1AwpMtjq-nTdzQMBQkSD_hYc2eTJFf5Vbzr-XmvCqW9L0uDjW_Vu4ExdRCIMHG4qpX53PydSKcus5Ay4p6JcwTTf1-tTtd75L97Taq2xaR8g7X0DHNSDWjEtZFPOeIj86dJPrasVDmSFU2bO5PiE_uXCZ37wfCvPJjn9Bmlq3Nil6Z6_6ZApXHU_QFqSwqFg_acBAWVAkOUy7AOfgkisp5bjg2dWQpa3pc5Nmwb4mzLyDROz8iD8b0YuLnueTfU0Hpkt0a3rXl1WDfaezlQ2-qXuJzglRgzY9nATKpwqx6sAUnKtLE-YfXndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=iI_WtquS2EyP0L1J3lkBi7lwHYLhK1AwpMtjq-nTdzQMBQkSD_hYc2eTJFf5Vbzr-XmvCqW9L0uDjW_Vu4ExdRCIMHG4qpX53PydSKcus5Ay4p6JcwTTf1-tTtd75L97Taq2xaR8g7X0DHNSDWjEtZFPOeIj86dJPrasVDmSFU2bO5PiE_uXCZ37wfCvPJjn9Bmlq3Nil6Z6_6ZApXHU_QFqSwqFg_acBAWVAkOUy7AOfgkisp5bjg2dWQpa3pc5Nmwb4mzLyDROz8iD8b0YuLnueTfU0Hpkt0a3rXl1WDfaezlQ2-qXuJzglRgzY9nATKpwqx6sAUnKtLE-YfXndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر حزب‌الله در حمله به اسرائیل به ایران بپیوندد، ضربه‌ای سنگین دریافت خواهد کرد و بخش‌های دیگری از خاک خود در جنوب لبنان را از دست خواهد داد.
بیش از یک میلیون شیعه در لبنان آواره خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/73277" target="_blank">📅 14:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=fBmY-BdzSdULT-caD9eE8Vx7ACLHsQnS-F5QwbhushXTTN-kmKoHTup1sR0IDEFM0lYyBxL1UCsSqYCeKrGNCejS01cAD5Usuuv78wLvLxtNqoHgwmnbXl7jOiNaeJK5ee-zP_xRiGyI_X2fASv6undnS5QVryrDOh0X_vYKq3s_QOcgcOSeVPk0V4MTL2hlmI9pybp2L0Q7DyVm6w-7dpkINUqMjdalEIxDplpeKrP3Wx50BX_YnKmp61juYeTfLX4xV775VM3J6wEA8eI2sn7YDbTnqXWtHtqK8UmGmvlu8e1oXYfuEhITZieGQZbF2-l8MV-t7dFc-tHYJkYxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=fBmY-BdzSdULT-caD9eE8Vx7ACLHsQnS-F5QwbhushXTTN-kmKoHTup1sR0IDEFM0lYyBxL1UCsSqYCeKrGNCejS01cAD5Usuuv78wLvLxtNqoHgwmnbXl7jOiNaeJK5ee-zP_xRiGyI_X2fASv6undnS5QVryrDOh0X_vYKq3s_QOcgcOSeVPk0V4MTL2hlmI9pybp2L0Q7DyVm6w-7dpkINUqMjdalEIxDplpeKrP3Wx50BX_YnKmp61juYeTfLX4xV775VM3J6wEA8eI2sn7YDbTnqXWtHtqK8UmGmvlu8e1oXYfuEhITZieGQZbF2-l8MV-t7dFc-tHYJkYxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانوم دکتر:
یه خانومی به من پیام داده و گفته که من به غیر از شوهرم 3 تا دوست‌پسر دارم و با هر سه‌تاشون رابطه‌جنسی دارم چون هر کدومشون برام یه لذتی دارن ...
هیچکدومشون هم از اون یکی روابطم خبر ندارن و 7 روز هفته رو تقسیم‌بندی کردم و پیش همه‌شون میرم !
اخیرا حامله شدم و چون نمیدونستم بچه از کدوم یکی رابطه‌هام هست، بچه رو سقط کردم ولی الان به‌شدت خون‌ریزی دارم ...
موقعی که با همسرم رابطه داشتم اون از این وضعیت شاکی شد گفت برو دکتر ببین برای چی این شکلی شدی؛ الان سوالم اینه اگه برم آزمایش بدم مشخص میشه من با دوست‌پسرم رابطه داشتم یا اینکه از دارو سقط استفاده کردم؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73276" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری مهر:
«افسانه عقیله»، عضو سپاه پاسداران و فرمانده حوزه بسیج خواهران شهیده افضل در مهرستان استان سیستان و بلوچستان، امروز در حمله‌ای کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73275" target="_blank">📅 13:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMrd47ztJry4b9MRGteYbltQTkEXW9Vxdh4X1RyctQAV1Qd1a38WS9oTHLM9iifH8mUGCEOs_kruBX-jYZUuBvf4rUlheQoJo46Fjl272dn1j4Ua2TZ0SV_2HvkgLKPqRIzfkvA2dQD8dMbZETB9DizQTOPb5dR_PJ6WfzvehpB8k027hcXsT5GmnvrLzIGitDExcOD5vkrPikV5LA5GfYRlBbCPmaPME8wg63JFaPMt_ko2e-3In6woR0B9mrdnMCxVBZqTsCO4Zy8cXfeSlqnIA00W3vKGfBlLLZgyVG6Vv8VaDZpljchW8SG70wJJFMzN4fnrJRj3Soesed_YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش، اوکراین بوسیله پهپادهای انتحاری به پالایشگاه نفت نووشاختی در منطقه روستوف روسیه حمله کرد که باعث ایجاد انفجار و آتشسوزی گسترده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73270" target="_blank">📅 13:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73267">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_fKUq4TrxLmS1uozPZJ0YyKR1TzrGohuixlTlAv_BbBmy0NRGJNwVY1OrFql_IcXhNBbAW6W5twsGxa3jsS_eNjGReu59-LdYKXRz8rUWIdvUaVhsCBBYJYzWj6FX2ZJTHUMqH5nD4nWMfKF8JRvhTzoYGT6VcAR0dFG5Zd8nD_rp6ZdRe5F-F0fjm9ECDkeC_osTF0GI8T-lN1x-EYtcI89WPWvm-6bpOvZ37QXAab8t79vyRnDUxiITXL2qjJz7a9qgjE69BwuwlOoi8DiURUjgEF0XuAWTltwuPhtZi_cYsVjRT_IECUkyvbNwvitjB8dMtpsXatK73mnCRZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6U3YZSoAU0XBL3ELUiFyfqQRpPWetaRm-EI1_IgKPTekNQCYlRtsEjoOmQCKFegDwMP-aihkwek6Srfr0r9JkQbrnwFcjm3qYUuN0iDoFaIVJrPtHhuegPt_SqzFAK9UrxNQqF8Qjior_Iwywtw8v2TUG9_taZ8qKUhhtGERuXg47mpBrXLrI5gwdCRlmPfWeUlX9O_6wJlNShFjKmZPkMekv7qjE2LeCRyWKno3AnbrUJ7a2eGuQYZbkwMrM3OgqbZkgHMIlzf85Hz39yC_PD5vIfH9zvO7idQF7NbJVgcijfCbwfEhbbQ5ZNg-vQcEiwXMohXQN_RiOO9IB8nHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=qML0XIalkQqBdLCJ2mshJmRXusevmcjRIud9R-sc3sCFLDGxjapZYGSY9x2OCXAT36x9b6WqDPXU4rKKGYBFsh5_ibnvWqvjmHKuozLMkB5-T7pXwrvgomav9cQJ0JWRvx95APx45USdmwSlB3qm4AiReR8XNqvk9F0a7Zxm7XBHNs41T-1gZv8hyiOhLpvCsJPWTMHQQ8Tsb-TjtVJeJ9NC8HhxR9BJgMTbBRuk4NDkW98ggk9kkGQlazEzFnhc81VlSMsn0ST-IXTddVGjkYDm3jzBNz9nwGIRf_LLbg_D-XAsxxthYeGORaGZi2OCi_NPhKp4lY5mRmdds74Y9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=qML0XIalkQqBdLCJ2mshJmRXusevmcjRIud9R-sc3sCFLDGxjapZYGSY9x2OCXAT36x9b6WqDPXU4rKKGYBFsh5_ibnvWqvjmHKuozLMkB5-T7pXwrvgomav9cQJ0JWRvx95APx45USdmwSlB3qm4AiReR8XNqvk9F0a7Zxm7XBHNs41T-1gZv8hyiOhLpvCsJPWTMHQQ8Tsb-TjtVJeJ9NC8HhxR9BJgMTbBRuk4NDkW98ggk9kkGQlazEzFnhc81VlSMsn0ST-IXTddVGjkYDm3jzBNz9nwGIRf_LLbg_D-XAsxxthYeGORaGZi2OCi_NPhKp4lY5mRmdds74Y9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که یک کشتی کانتینربر حامل بیش از ۲۵۰۰ کانتینر، هنگام تلاش برای عبور از تنگه هرمز از مسیری غیرمجاز، با یک مین دریایی برخورد کرد.
این کشتی صبح چهارشنبه در جنوب تنگه دچار آتش‌سوزی شد و غرق گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73267" target="_blank">📅 12:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73266">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تا انتخابات اسرائیل و آمریکا چقدر مونده؟
فقط ۱۳ روز تا انتخابات پارلمانی اسرائیل در ۲۷ اکتبر ۲۰۲۶ مونده.
انتخابات میان‌دوره‌ای آمریکا هم ۳ نوامبر برگزار می‌شه و ۲۰ روز تا اون باقی مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73266" target="_blank">📅 12:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDrbntX_q60HaPaBYh5zzw9ncOmkLKIMroKhZgUkp3EF8s65PoTr3hCuyp-QOc3gfSlwWmD1gRavldzmyJKKf5JTcwGhjrpg11Q3DiabU8JzC_ryUf275XIVDNazERimdmEh-s1orkltN4nlWMK8yvHbLMN2Anp9g3vKXR9r6ngyfo9kyjTsI3Y7pFIg33VTcajX215687CXKtVm0NbK3oF1keP2rNv4f6Wg_NDgc-btDYDErqGidsfyggXQbyRDJDIQlByRXz3qcD6cLiunY6IZjLdylccIPT3WxmWK0RyhlQhUC0plk2sJlXU2Xze_cPKJb8okyUtG-0ttOXvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ: این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73265" target="_blank">📅 12:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73264">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=UiqncOKKtNvWtXREenapIuqeY_1V_PWFa0fLWV8zuGc1GcNjZGsYB3vfn95QatEGqfN9wYznw0OSsGv6W8ftOnnNXhctZ3u9DBsOp6b0bqTavNH6r51w9On87RJGPo2gNAfa2rk-xD6rhjHV_DJXHPGoN0qRU1R9BPggEW0UUinTZgBabdJelveHYr1T9Ri5tUiVS0KJTfDtsQwE67TzDzgMINgW-qj-8pu1BmuvdUMM1Jsc-ZHjCWT0OOmdiIr6OCDHCzExxK3vgFE0wfQBTKhdRrbi0_-aZINo0453U4n4HEnTW1snudqlj9P7htfEqglbQtBOw6N9LaDx5E8Vrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=UiqncOKKtNvWtXREenapIuqeY_1V_PWFa0fLWV8zuGc1GcNjZGsYB3vfn95QatEGqfN9wYznw0OSsGv6W8ftOnnNXhctZ3u9DBsOp6b0bqTavNH6r51w9On87RJGPo2gNAfa2rk-xD6rhjHV_DJXHPGoN0qRU1R9BPggEW0UUinTZgBabdJelveHYr1T9Ri5tUiVS0KJTfDtsQwE67TzDzgMINgW-qj-8pu1BmuvdUMM1Jsc-ZHjCWT0OOmdiIr6OCDHCzExxK3vgFE0wfQBTKhdRrbi0_-aZINo0453U4n4HEnTW1snudqlj9P7htfEqglbQtBOw6N9LaDx5E8Vrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73264" target="_blank">📅 12:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73263">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73263" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73262">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73262" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73261">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj-O6s6fIyY6wtElskcK9E350WeaL7dZjQWEcaI3JRitYI3DBeabtB8sHW1MKxC4X3bONvTxmHe9UpWi8A3UmT6ggiQHjR8PeXFvqGMybLSQe2u1HlhfgHCOev-9LUQbUXsDgguFPFoHf_kr1NVvLdQn-a-XUcHAMklHjM7rtbcWRIWDRBkjfKkV1DFp-DbmMc-5s0_Xj2DNQerTvaUWGlUFJh3FAGP_6Bgr_RC6dIfjxxQFD7Y3Q_zXeMtk8kR1nfRIznEJMc2WreqAhUnNBqR9k94I8Qlv34xJlVb5oTffOZfA04EexaXQ5KvbBMoL4Xswl96jHhjpZG6Pg2BK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
لیورپول
🆚
لاسک
فنرباغچه
🆚
استون ویلا
دورتموند
🆚
بودو/گلیمت
پاریسن‌ژرمن
🆚
منچستر سیتی
پورتو
🆚
رئال بتیس
رئال مادرید
🆚
رم
پرسپولیس
🆚
خیبر
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت، ووچر، کریپتوکارنسی
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73261" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">استانداری هرمزگان:
دقایقی پیش یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدوده بندر کلاهی برخورد کرد. بر اساس اطلاعات اولیه، در پی این حادثه سه نفر مصدوم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/73260" target="_blank">📅 11:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73259">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش تو مکه-عربستان، یه کفتره با گردنی شُل درحال مرگ بود؛
که گروهی از زائران رفتن بالاسرش و گفتن حیوونِ خدا داره نماز ميخونه و حسابی به وجد اومده بودن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73259" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده:
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73258" target="_blank">📅 10:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kafqqVJuRNQg7m7zLxIyaDIdgAxthACP-5irROs8B_R0t1N_f6weZ-vAz_JQueIzRUD3VXrCAWPgUojX0W4dgmV1Wx4e7-aV2nAksU5r7w0ZnBS4DL0_Id_yUbVu-QkQ-sB58T8TAFlHiqNKLHJTyWdq2uKitB5iXoGsb4g_6nFW4amCaXKAxYcFgzFFTds_L7bQU1qLfCdVmcvdzK1FjJ_WlIJ2G41o90rWHS2hkr0aVVPSGpZyczJ3-Irkcp9p73t5hVVezPd8d914rvX2AxA2gE9cgo-AdVVBU83egISbPBUPQBsvCMuWUGDvE560Y7SrEEFvooT7ExR1Pid97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد ۱۰۵ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
۱۰ هواپیمای ترابری ورودی از خارج منطقه:
فرانسه: ۳ فروند
آمریکا: ۳ فروند
بریتانیا: ۲ فروند
عراق: ۱ فروند
کویت: ۱ فروند
۸ فروند هواپیمای ترابری نظامی منطقه‌ای
۴۵ فروند هواپیمای سوخت‌رسان
۷ فروند هواپیمای جاسوسی و شناسایی
۳۴ فروند هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند
۱ فروند بالگرد نظامی
مجموع: ۱۰۵ هواپیمای نظامی در ۲۴ ساعت گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73257" target="_blank">📅 09:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=QNv-KMTN_1RALc1X-agckbnkjRG2YXJa2jDvmYc8FSJFLU6tx6W5Y-p4XEcYPTojcKiRnmiAl46CxbOJyzBmRWi9zfu7TnwP8ewAeUicGpedv6OLvkU625n4DQMWX9-L1dq6siFLUJEV3I-FJnfAe3eJqp5mrlikjJ3nwpPcqcGwtol6PuFpOyMf9pThQF8mN0dnnspaK_2SJUwJP_mIpcng1fbUoJhpNnPRTkYvTWxlZh-T-Sw5FailjVVxJ-G2PgV2pK5GSPNLaaZxuVlxBtnwze8IZmSSfe6p7dDKe4KcsxWztUHHyw0xD4lhTamYTs0c3uHzN5rCQDtxtCh_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=QNv-KMTN_1RALc1X-agckbnkjRG2YXJa2jDvmYc8FSJFLU6tx6W5Y-p4XEcYPTojcKiRnmiAl46CxbOJyzBmRWi9zfu7TnwP8ewAeUicGpedv6OLvkU625n4DQMWX9-L1dq6siFLUJEV3I-FJnfAe3eJqp5mrlikjJ3nwpPcqcGwtol6PuFpOyMf9pThQF8mN0dnnspaK_2SJUwJP_mIpcng1fbUoJhpNnPRTkYvTWxlZh-T-Sw5FailjVVxJ-G2PgV2pK5GSPNLaaZxuVlxBtnwze8IZmSSfe6p7dDKe4KcsxWztUHHyw0xD4lhTamYTs0c3uHzN5rCQDtxtCh_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
این رژیمی متعصب است. تا زمانی که پابرجا بماند، برای احیای خود تلاش خواهد کرد.
تلاش خواهد کرد برنامه هسته‌ای‌اش را از سر بگیرد؛ دوباره برای نابودی ما، و بازسازی حزب‌الله و حماس تلاش خواهد کرد.
برای نابودی کامل این تشکیلات، باید این رژیم را سرنگون کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73256" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛پرزیدنت ترامپ درباره ایران صبر کنید تا ببینید با ایران چه می‌کنیم. کارشان را خواهیم ساخت؛ صبر کنید تا ببینید. آن‌ها هم فقط منتظرند.
صبر کنید تا ببینید با ایران چه می‌کنیم، چون دیگر کاسه صبرمان لبریز شده است. می‌دانید، دیگر به آخر خط رسیده‌ایم.
اما خب، این‌ها اهمیتی ندارد. مسئله مهم این است که قرار نبود آن‌ها سلاح هسته‌ای داشته باشند و نخواهند داشت؛ این موضوع زیر هزاران تن سنگ دفن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73255" target="_blank">📅 09:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=d326PPfWwXEC6BTEsSfm6JoQXnfifvdoZfDdfPOWw-WYtqxeSWR39gsjbEsyuSOSrLnuN21VS3qSfu0TP9IzPAhOlhKXUng63JfISyaF_HjpgPzSozpoTEcG8UCUDH3rOtauWZMaiXnI2VT9hRsLtunkN0kJVod2x-MplX5xUW-d6EqATZ0Jz3nligqFeBgYjI1Mqr949Fxh2lA60hNdXscsDOLd0YckB19dMErJ0vmck_z970LroH139ITBmh3bDJhmcr0DPojlYSQGkf7FUEckEJhnCW0aDLMgAlzFzqcpxoiNMYhfWXFGC0u0mWdNl_saUMA-erUD7cFqxQEJGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=d326PPfWwXEC6BTEsSfm6JoQXnfifvdoZfDdfPOWw-WYtqxeSWR39gsjbEsyuSOSrLnuN21VS3qSfu0TP9IzPAhOlhKXUng63JfISyaF_HjpgPzSozpoTEcG8UCUDH3rOtauWZMaiXnI2VT9hRsLtunkN0kJVod2x-MplX5xUW-d6EqATZ0Jz3nligqFeBgYjI1Mqr949Fxh2lA60hNdXscsDOLd0YckB19dMErJ0vmck_z970LroH139ITBmh3bDJhmcr0DPojlYSQGkf7FUEckEJhnCW0aDLMgAlzFzqcpxoiNMYhfWXFGC0u0mWdNl_saUMA-erUD7cFqxQEJGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تولیت آستان قدس رضوی:
توفیق اقامه نماز با رهبر انقلاب را داشته‌ام؛ حال ایشان بسیار خوب بود
رهبر انقلاب پیش و پس از تدفین رهبر شهید در مشهد حضور داشتند
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73254" target="_blank">📅 09:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73253">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73253" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73252">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8hrN88yVbnmRc21d2xnju4jIVYJMfP36U8jKd41b9QULI1NytgXR43as4t2Klo03Y6DiRRY6gQde64fnS90ILUjw7E8KA1U3qD2TQTRUpUfp6IePE2Zd9y1iUohElJpqgOLTGwUgslz9MYqq0msv1oD_SyW7CpHSv_RrinoICSD9Jvcm4ljLJfcREJlzE1UE7BjzzzjCj9-qwxqK14tFD9Vbm8tB24EUOGy1ViIWEVmeXt9XsEHfmEvw5UNkM3kFjVxX1Rq5mCh9JK2YzOnz2Vqnej90r88XzBxWjc9p3By10fUwNfzRIsh9Mlcz5MuiF0slys5OaJwxmInmgq3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73252" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73251">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حوثی‌ها به مقر شرکت «آرامکو» عربستان در ظهران حمله کردند؛ این اقدام ساعاتی پس از آن صورت گرفت که آن‌ها به‌طور علنی این مکان را به عنوان هدف تلافی‌جویانه معرفی کرده بودند.
وزارت انرژی عربستان تأیید کرد که یکی از ساختمان‌های اداری در مجتمع آرامکو در ظهران هدف قرار گرفته و منجر به وقوع «آتش‌سوزی محدود» شده است؛ این حادثه تلفات جانی در پی نداشت.
خبرگزاری رویترز از شنیده شدن صدای انفجارهای مهیب در نزدیکی این مقر، وقوع آتش‌سوزی و صدور دستور تخلیه خبر داد و اعلام کرد که به کارکنان گفته شده است روز بعد از خانه کار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73251" target="_blank">📅 01:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73250">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKgmOZs-ZYca_bx0BoGg4oCfDn9p_6mczR-zvbBd_hInyuhhI6edXCrwXRrqNglUjEfmCSJu64Ux32WeUOcCMIxqzfKVrskmfb-19ozYTC8CQYZA6PT-bTZkIkongOSZPe7LYgZhnJw7HP2CmyM00eFHzbExk-G42r7t7MpuXyAGRCXVeiBMds4gOOFynjJ8bgfvyQhvc0Bm-q1kW2rpr3kUk5hImmIhIzubWAlMmJVXAOxjrefq997kPuV0t-iSskofChJd5apR668PWDCanxfT_dSP6_61av_BXHCMDjIBIqtOb7vf_iBfH8jz-57j2bduFhzXzROf0AVYdIme4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73250" target="_blank">📅 01:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73249" target="_blank">📅 01:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خاتمی داشت با عصا به سختی راه میرفت که یهو ملت شروع میکنن به تشویق کردنش که یدفعه شفا پیدا میکنه و عصا رو میذاره کنار و راحت میشینه!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73248" target="_blank">📅 01:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=OEzqnNbOaZhpFG53DfEctNuCt734Qug3yl26y5DKiVWqPUhfdXik9-aL00FAiYzzLPTtlUv7R0ZEd7dZoJZPAWXns2elf-QYpewEcBYu9Yf-lrL4HjdzCxpuW0cM14qbB6dqweNyDBlINfBmUQiKPr_HdkV3g3zFSpwU5DHyMBsowaFEKAt8qNKdaD9130-0-EZp2n-xGT07EcpINcTu6Lfs4PDm5LhR3VN8hcgD8rWe1XmG9KPHsmeA2zcGC0Ep-lPgj2BwHt6UnwDTVaAV3qL6n5VAhf8N7uJSqpurmXQY_Bg_HMPYq4MsRrar4jIanXCAoIRAPyFuzFP_HuHo8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=OEzqnNbOaZhpFG53DfEctNuCt734Qug3yl26y5DKiVWqPUhfdXik9-aL00FAiYzzLPTtlUv7R0ZEd7dZoJZPAWXns2elf-QYpewEcBYu9Yf-lrL4HjdzCxpuW0cM14qbB6dqweNyDBlINfBmUQiKPr_HdkV3g3zFSpwU5DHyMBsowaFEKAt8qNKdaD9130-0-EZp2n-xGT07EcpINcTu6Lfs4PDm5LhR3VN8hcgD8rWe1XmG9KPHsmeA2zcGC0Ep-lPgj2BwHt6UnwDTVaAV3qL6n5VAhf8N7uJSqpurmXQY_Bg_HMPYq4MsRrar4jIanXCAoIRAPyFuzFP_HuHo8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73247" target="_blank">📅 00:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSozuCrMn7w9Pb4XkMwxxou1Sv7b6HKxwcdJN5JR7oN8l0f0C_osTd_rv-4KV_8LMzwUv2fAuHB8w3Wp4HEMfVziJJ05n9sHOlWLu10PQaxuAyIMP0V5bNevYqs6F8mwSUP-5h_hMaUndBKIqQfE5nKrGbpR-Rx0zpo84tqgF8-gqOzuxmnjWNbQs7G0BCC4hhRFwov8Ak0EaIX8uWQIEi2zMAKIsUdJ-Fs67_vhghbcnbyan3xqDaNlK_s8WEFnCPbNM9azXKg3Zi73SW166cXDM96MM4RoVtkRmsAmby02oF-D7WtJg3OTTAoHOPNGx7iYCA1Qup0CehUqyHCsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
اکسیوس به نقل از یک مقام آمریکایی:
به نظر می‌رسد «بی‌بی» (نتانیاهو) می‌خواهد دوباره دست به اقدام بزند. او چند بار در این باره با رئیس‌جمهور صحبت کرده و رئیس‌جمهور هم گفته است: «خب، می‌دانی بی‌بی، برو و آماده شو.»
اما در واقع هیچ تعهد قطعی‌ای وجود ندارد. عبارت «برو و آماده شو» ممکن است به معنای «الان»، «بعداً» یا حتی «هرگز» باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73246" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=L8UYyC49IDAS7XOfeaHM7wP1qqtWZx7li91-hsKkLRvyJu-0J6AAa9gISBnzgJU9hF86416Co1OjcrswjFrpud_Fe2nGs7V10eO3xN5DszndUiV35TBDqji4--BbwKJdQmEGxVXAh3O2ZW6ci5U1hwgBkXgV5OZCOBTGEwHX8ID7q8xK59qUnrfdCPSWV4gjMTcUsz0RH0LzXAXeaACotCK2Nc8oAFvW9Q-R3CI08B0wq4z7Qfy5YM3ExU0V8cqdXPtU_I0M3ubKOv06fTBEfZh7UHPE38sbNTDhPqLzz-txPtzZIV081UGX_GCFkQM5BIir77BqeTumCUXYPxmpPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=L8UYyC49IDAS7XOfeaHM7wP1qqtWZx7li91-hsKkLRvyJu-0J6AAa9gISBnzgJU9hF86416Co1OjcrswjFrpud_Fe2nGs7V10eO3xN5DszndUiV35TBDqji4--BbwKJdQmEGxVXAh3O2ZW6ci5U1hwgBkXgV5OZCOBTGEwHX8ID7q8xK59qUnrfdCPSWV4gjMTcUsz0RH0LzXAXeaACotCK2Nc8oAFvW9Q-R3CI08B0wq4z7Qfy5YM3ExU0V8cqdXPtU_I0M3ubKOv06fTBEfZh7UHPE38sbNTDhPqLzz-txPtzZIV081UGX_GCFkQM5BIir77BqeTumCUXYPxmpPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دستشویی یه کافه تو بالاشهر تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73245" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس» درباره ایران:
مذاکرات نه کاملاً مرده‌اند و نه واقعاً زنده؛
ما صرفاً در حال افزایش فشار هستیم و این باور وجود دارد که در نهایت، عقلانیت و تدبیر در آنجا پیروز خواهد شد.
ایرانی‌ها تصور می‌کردند که این رئیس‌جمهور به دلیل فشارها و انتخابات میان‌دوره‌ای عقب‌نشینی خواهد کرد؛ اما او به آن‌ها نشان داد که در اشتباه بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73244" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6tPeSZPezLEEkeWizUhrsYUGB7250_-mIvMOAeC3d5Gyk5exa6EeftFa6B4F9WiosqiJ07DvCa6gPIUNgJRPvC59HIadno_NP8-tMirbLcWdIXVQuLjx5gKIUVe6ddSC5fHfBV5YGryPEiKjvu3gXlloHo75wmQuipQ_PMiuyLS26yBMMj_f9VMNRqxbbXOnu9zygZhQ4FLoaA34Opj1BQ1QK0hiHeWVDg-RvZnY9Rg9hlQG6YwMCguhkegz4g7KoZtiYdbiqcJdmchkT2DnKdbCCEXzI2Ea-MjE864X_hR4q8kKyeWo3iIWvgSaRe5eKU2lne2p4STr9d9QuBNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی تجاری بریتانیا (UKMTO) گزارش داد که یک کشتی باری امروز در تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73243" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=H0wisB71lYl6Lz4qbRp5sSE_1heW0UQwmiu4LzmGdqXgpEDKo3OAj-qplrjssTSiI7Q3meFUR-bivxn58LJKjJQCYF05Wi1qp0eawlhVZF07Re2-1SlmuOSlkvjVj9F5gZuWGDYFL7qFCNjzIjps_Qe85ok5-hSjX8MSRpAk9Zi1McHfcvoHHAur-EeJ3In0m0PVqX92z0ylr9GHuD8C2K3oYTDRZrlB9xAaSAq1pJs5U6z0dItrTIu4pJS5Ghq89wB5vnoTnHBYCZA15pipw6Di7EMCtTv600xKw0o89uJnIL_eZmqdQodschXlB-c7vm5h9HVf6mDHx-6XakdHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=H0wisB71lYl6Lz4qbRp5sSE_1heW0UQwmiu4LzmGdqXgpEDKo3OAj-qplrjssTSiI7Q3meFUR-bivxn58LJKjJQCYF05Wi1qp0eawlhVZF07Re2-1SlmuOSlkvjVj9F5gZuWGDYFL7qFCNjzIjps_Qe85ok5-hSjX8MSRpAk9Zi1McHfcvoHHAur-EeJ3In0m0PVqX92z0ylr9GHuD8C2K3oYTDRZrlB9xAaSAq1pJs5U6z0dItrTIu4pJS5Ghq89wB5vnoTnHBYCZA15pipw6Di7EMCtTv600xKw0o89uJnIL_eZmqdQodschXlB-c7vm5h9HVf6mDHx-6XakdHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار رکنا از سخنگوی شهرداری تهران پرسید: چرا در تهران در تمام ساعات
روز ترافیک سنگین وجود دارد؟
محمدخانی در پاسخ: «اینطور نیست، مثلا ساعت ۳ نصفه‌شب که ترافیک نیست!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73242" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26766391a1.mp4?token=Gb0DLhW1otdYnugl6GcLFUBxreSTQfUDiJ9S_LwyQ27w8Dkz9BriTGQAKeYJDzdRBXXq8tSo6ER7q6upC2XjmrdLa4fPm4QPLVUb4eILDCFgFzErwcavvwGarrRMPnylcY1ZUD7CqBuCQgtRZKuyndkWjDm0VzW3M4mvTV2dzKcbr1OW0aaBalrHXUYeoaZT94sUIsJb2wYUEWZL7WUGhZZmnPH0Vxt5esjSXALEswvfycA2h43fefmo9u8m1hPcgBDTlmiCbVqQlZSFytql-Yzwtbj1mBWkcW-u4G7P45g2t1X-7Ug5r2FBgLSCGF0UeCil6LKLj4PX_KP7Q1B5kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26766391a1.mp4?token=Gb0DLhW1otdYnugl6GcLFUBxreSTQfUDiJ9S_LwyQ27w8Dkz9BriTGQAKeYJDzdRBXXq8tSo6ER7q6upC2XjmrdLa4fPm4QPLVUb4eILDCFgFzErwcavvwGarrRMPnylcY1ZUD7CqBuCQgtRZKuyndkWjDm0VzW3M4mvTV2dzKcbr1OW0aaBalrHXUYeoaZT94sUIsJb2wYUEWZL7WUGhZZmnPH0Vxt5esjSXALEswvfycA2h43fefmo9u8m1hPcgBDTlmiCbVqQlZSFytql-Yzwtbj1mBWkcW-u4G7P45g2t1X-7Ug5r2FBgLSCGF0UeCil6LKLj4PX_KP7Q1B5kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عرازشه در مقابل منزل حسن روحانی و شعار بر علیه او:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73241" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=UJzJ7qtJiJt2vrdVJ9ZSdHk2uR1qJY4gX0UVOPcad0SjOhcVkq3J1kjcLZWXztJP74nkI1lTnvVY9-kO3f75BuBpbCNtweGCHTHFWXiy9ipB24TO4kec8HDt9T2cDFLSm8be5cTW596S3sDOxqzwWZZpoSkQh2eMrGNjZjCCGNC96F2uV7QD_f3TPJK-c_cRO7uofHsCnZLGJPf-7z6W8d08yhcYh42lB0pS3rz2H21Y4wOReTtWs_AlQYo5wx1oaiaKmsSXAb862ldRTpnNTeXRCF4wMuhE8ZwiuGDuHQdF6Tie3KzoOVRWOgAs1VxgqwGlrOoSPgp_IZ0daIoPfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=UJzJ7qtJiJt2vrdVJ9ZSdHk2uR1qJY4gX0UVOPcad0SjOhcVkq3J1kjcLZWXztJP74nkI1lTnvVY9-kO3f75BuBpbCNtweGCHTHFWXiy9ipB24TO4kec8HDt9T2cDFLSm8be5cTW596S3sDOxqzwWZZpoSkQh2eMrGNjZjCCGNC96F2uV7QD_f3TPJK-c_cRO7uofHsCnZLGJPf-7z6W8d08yhcYh42lB0pS3rz2H21Y4wOReTtWs_AlQYo5wx1oaiaKmsSXAb862ldRTpnNTeXRCF4wMuhE8ZwiuGDuHQdF6Tie3KzoOVRWOgAs1VxgqwGlrOoSPgp_IZ0daIoPfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرویس بهداشتی یه مدرسه پسرونه در تهران!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73240" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPRG6hVPOuwc6avFXlyMwlASwg2TBcy3LzlgyAnS9t6BnAQ2mCts7hqI3nD7YOf3OLkkAmBCAfYIEaP5aN9hkpSp7X5uJqO-31jiSZit89FPsjK95FFbpg4wVqRzhS-g2l2XWJBOFoqjJilGX7Fg6j5cgqQ7hQN24pIIF691l-CBovgmfCn25qqgHB0tP3IG7yk6e7x4_nUG9GZbHAMANN2Q7w4ZUiGsdGRGRYM6RvP1mzwsZAteNV28Dwoey3taFIiKnhUz8P01ZqvdRMsYT4vrGuZxygbNhUw57WOeB5VY_ymfMZ-NJWXtgeTvWFL_yO0lqGMy5Be944FAu2dqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، طی دو هفته گذشته گفتگوهای متعددی با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره آغاز یک عملیات نظامی مشترک جدید علیه ایران داشته است؛ عملیاتی که احتمالاً پیش از انتخابات ۲۷ اکتبر اسرائیل و انتخابات میان‌دوره‌ای ۳ نوامبر آمریکا انجام خواهد شد.
نتانیاهو با ابراز نگرانی نسبت به تلاش‌های ایران برای ازسرگیری فعالیت‌ها در تمامی بخش‌های برنامه هسته‌ای خود، این تحولات را توجیه‌کننده‌ی انجام حملات مجدد علیه تأسیسات نظامی و هسته‌ای ایران دانست.
یک مقام آمریکایی اظهار داشت که ترامپ به نتانیاهو گفته است «اقدام کند و آماده شود»، اما تعهد قطعی نداده است؛ در همین حال، مقام دیگری گفت که موضع رئیس‌جمهور همچنان در حال تغییر است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73239" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی طی ۲۴ ساعت گذشته ۱۰۴ حمله هوایی و موشکی علیه صنعا و استان‌های ذمار، تعز، عمران، لحج، الجوف، مأرب، صعده و الحدیده انجام داده که منجر به تلفات غیرنظامی شده است.
این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های هوایی «خمیس مشیط» و «طائف» برخاسته بودند، و همچنین با شلیک موشک از «نجران» صورت گرفت؛ امری که مجموع حملات ادعایی ائتلاف به رهبری عربستان را به ۲۲۸۱ مورد می‌رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73238" target="_blank">📅 20:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IleX_7pqmA_xJPVCcFywlOyIKwW9cg5U7ugRPzzVerWIxGKFdXzleJaKxm9GVXkzaQCGMZdbS4CuYPjCXb-GLvWK-2g0YH_-yrN2Y1SZ82ikbG1IxRK8ArwqQJqy_6nltNEv9kjvWvNvm34spIJkLZgSR96fUrVzBKnwhajdNQiBD6dgODUv54l3Kk6Q_JVYEZekAN23tKAirOt-M2gHKWUVcVJDnC2QB-8VdIZzTEc1ZgC_Bykb_2dD2Tu_dn_qhO9NXim5gBmzAvYkKRih3Q3SlB9jmaI3r7yc2_zQj4LSLyq2D5smeZuY6NJu4wmVnev-rdzEhJa3sWM2zgU_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ترامپ در تروث سوشال:
«حوثی‌ها رفتار خیلی بدی دارن. فکر می‌کردم یه سال پیش، وقتی حسابی بمبارونشون کردیم و به درخواست خودشون حملات رو متوقف کردیم، درسشون رو گرفته باشن.
اونا مدت زیادی سکوت کرده بودن، اما حالا دوباره ظاهر شدن؛ احتمالاً به دستور ایران که یه کشور در حال فروپاشیه، نیروی دریایی نداره، نیروی هوایی نداره، بدترین اقتصاد دنیا رو داره و تورمش به ۳۰۱ درصد رسیده.
اونا به شکل خیلی بدی به عربستان سعودی حمله می‌کنن و عمداً سعی دارن قیمت نفت رو بالا ببرن؛ احتمالاً هم قبل از انتخابات آمریکا. این اصلاً قابل‌قبول نیست!
یکی باید بهشون توضیح بده که من دیگه نامزد انتخابات نیستم؛
من قبلاً با اختلافی بسیار زیاد پیروز شدم!
اما بعد از انتخابات دوباره وارد ماجرا می‌شم و این اتفاق رو هیچ‌وقت فراموش نمی‌کنم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73237" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=q5mYRs0cHoLuETbk3r7_C03qMZC8xr0s4BocUOyu1ZE4c2Ajkkg17l0TIS0inXyzPegqvy_WTvFK2eA2TtOGr6VQNfNwM1Z3WPvJG7A7aJmBsOzOWJ_hNYkdRFhSaxnLipeSIT7gxVO2Kz84YaOmJse06mod4kVQHKqFNYzqaFAK34yu7ScINNA8afkyrm6HdqGanrtx00_4eg-IP9WpwmK8EXYN1J4NFmGPP2wEp4Y5mPIH_R7Dp_ITCE1vE0wSEhWXjvgc_F4VTO64jfMPWPYejhKeXbwUaPGmYnsYa6wKGgYdm4hxV534uXdUDTHKFC83AAYHG4-Z9u68V0p2lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=q5mYRs0cHoLuETbk3r7_C03qMZC8xr0s4BocUOyu1ZE4c2Ajkkg17l0TIS0inXyzPegqvy_WTvFK2eA2TtOGr6VQNfNwM1Z3WPvJG7A7aJmBsOzOWJ_hNYkdRFhSaxnLipeSIT7gxVO2Kz84YaOmJse06mod4kVQHKqFNYzqaFAK34yu7ScINNA8afkyrm6HdqGanrtx00_4eg-IP9WpwmK8EXYN1J4NFmGPP2wEp4Y5mPIH_R7Dp_ITCE1vE0wSEhWXjvgc_F4VTO64jfMPWPYejhKeXbwUaPGmYnsYa6wKGgYdm4hxV534uXdUDTHKFC83AAYHG4-Z9u68V0p2lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خبرنگاری رو که همیشه درباره وضعیت ایران سؤال می‌پرسه، مسخره کرد:
ترامپ:
«ایران؟ باز هم ایران؟ همیشه ایران!»
«ایران یه کشور شکست‌خورده‌ست. هیچ اقتصادی نداره، تورمش ۳۰۰ درصده، پولی نداره و حقوق نیروهاش رو هم نمی‌ده؛ نه به نیروهاش، نه به هیچ‌کس دیگه‌ای پول نمی‌ده.
خیلی زود درباره ایران تصمیم می‌گیریم.
ما تنگه هرمز رو کنترل می‌کنیم و نفت زیادی هم از این تنگه خارج می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73236" target="_blank">📅 19:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=Dbf6eiu6qNVJ2DIUM9djwIWnuWBd6IYG9EVRVgEX0Xk8mwJVb9AgL32-iNXVZShiaAKSkjlCCaYu-62Q_caiYF_rrw30BKDUZtWZ8z89f50quuwyy3O61xEpQt5rRm-U_MOKHNpc6W_StGljk7nQVFpdSFa3eD09-rnDASPxDnQoulzfX2vhnFVmVu_25pD6tMyPKG6OB5PJAlaUTwc8Nlgq3r38LvpCKA4mkrrCZd-llLP6tDqhxsbXBkJVqGZk6JZCWh2-yrKWtV-OJvYWM76l6JV2-27Co3yaM-qK1r5D7W2w50HApk8xtP8Hhk9QzmAd1SA2H_5Qm7slFwDH2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=Dbf6eiu6qNVJ2DIUM9djwIWnuWBd6IYG9EVRVgEX0Xk8mwJVb9AgL32-iNXVZShiaAKSkjlCCaYu-62Q_caiYF_rrw30BKDUZtWZ8z89f50quuwyy3O61xEpQt5rRm-U_MOKHNpc6W_StGljk7nQVFpdSFa3eD09-rnDASPxDnQoulzfX2vhnFVmVu_25pD6tMyPKG6OB5PJAlaUTwc8Nlgq3r38LvpCKA4mkrrCZd-llLP6tDqhxsbXBkJVqGZk6JZCWh2-yrKWtV-OJvYWM76l6JV2-27Co3yaM-qK1r5D7W2w50HApk8xtP8Hhk9QzmAd1SA2H_5Qm7slFwDH2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا از ترکیه می‌خواید که در واکنش به اقدامات یمن ملحق بشه؟
ترامپ: «ممکنه این کار رو بکنم. اردوغان دوست خیلی خوب منه و احترام زیادی براش قائلم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73235" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=NfaAw9bIXW4UziGglt4UbsyqI9AHnOXuirt3S-50C6-mAgCb_wacvlAZyuqOyQLwpdDGDvlO4FscIpMFexxbrVhgHhjrw5BXx_mUY_UPHU6qJI0niKnsQo5Fm3IUnycH9PNDOuHumlH3ZgukoK-DVTlNYHz9KfuDUNAHqa435OlzXpdkA0IKbNvDvaafKzXiC9OayYguO7yp4FOjrPXm2iK8FBTHYfgn_d9vJD7B67ef4wWXuJtaX9_7r5wdY3UuyAHs7Tqjalgn343XjFkX5TKMmWmcIWS5Nbt16tb_Go0zaYdkZGYOo9cPKydxMvGddXpXu2z3mKLG3cqVwmLCEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=NfaAw9bIXW4UziGglt4UbsyqI9AHnOXuirt3S-50C6-mAgCb_wacvlAZyuqOyQLwpdDGDvlO4FscIpMFexxbrVhgHhjrw5BXx_mUY_UPHU6qJI0niKnsQo5Fm3IUnycH9PNDOuHumlH3ZgukoK-DVTlNYHz9KfuDUNAHqa435OlzXpdkA0IKbNvDvaafKzXiC9OayYguO7yp4FOjrPXm2iK8FBTHYfgn_d9vJD7B67ef4wWXuJtaX9_7r5wdY3UuyAHs7Tqjalgn343XjFkX5TKMmWmcIWS5Nbt16tb_Go0zaYdkZGYOo9cPKydxMvGddXpXu2z3mKLG3cqVwmLCEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا حوثی‌ها رو هدف حمله قرار می‌ده:
ترامپ: «اونا خیلی بد رفتار می‌کنن. اگه بهتون بگم تصمیمم رو گرفتم، اون‌وقت... حوثی‌ها واقعاً خیلی بد رفتار کردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73234" target="_blank">📅 19:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=XHlyoX1V87inaTiTTX5ZIn_rgmM0oM3eD6eY4672X0HBlMcwwB1JFFOBHAmXhnapXPQz_LLZuhe83ruRUQLgX7SjyMSE1Pef0C0QWH1NnZY9V3e08OeYikbKTm20Ky2sjyvBLyEF8_O6CdAZaOCDD_2vT3_MonO09AT3FuWpsMt1JTXRmeG8gjYSqdLxbnRqMrJWtGey0pzOgT92_Vfci7A4pL8dFK9eIktzk-9JHps7-kS6Sf_MRJk66NZMfb7PDln7GFQ4TNVVjkwWPWogBtTWx7CMexEZPnVG2KnokiMGiC7aGpquh1cHxA-DLNQWqTdydi65sG2d2BXTthsUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=XHlyoX1V87inaTiTTX5ZIn_rgmM0oM3eD6eY4672X0HBlMcwwB1JFFOBHAmXhnapXPQz_LLZuhe83ruRUQLgX7SjyMSE1Pef0C0QWH1NnZY9V3e08OeYikbKTm20Ky2sjyvBLyEF8_O6CdAZaOCDD_2vT3_MonO09AT3FuWpsMt1JTXRmeG8gjYSqdLxbnRqMrJWtGey0pzOgT92_Vfci7A4pL8dFK9eIktzk-9JHps7-kS6Sf_MRJk66NZMfb7PDln7GFQ4TNVVjkwWPWogBtTWx7CMexEZPnVG2KnokiMGiC7aGpquh1cHxA-DLNQWqTdydi65sG2d2BXTthsUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی، خبرنگار فاکس‌نیوز: «اشتراک‌گذاری اطلاعات و داده‌های اطلاعاتی با اوکراین رو متوقف کردیم؟»
ترامپ: «نه، متوقف نکردیم. ما بهشون کمک می‌کنیم و واقعاً داریم کمک می‌کنیم که به یه نتیجه نهایی برسن. پیتر، ما می‌خوایم جنگ تموم بشه. داریم بهشون کمک می‌کنیم و اطلاعات هم در اختیارشون می‌ذاریم. می‌خوایم جنگ تموم بشه؛ برای همین با اوکراین و روسیه همکاری می‌کنیم تا به این جنگ پایان بدیم.»
این جنگ بی‌فایده‌ست و باید تموم بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73233" target="_blank">📅 19:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=jUwVf5_yo7v_ltxo7GERzNeAJTpC5HdHMgUJ4TrR_h_kmu1KRx-PbohySAbzP_dfP7xsKJNQCaDJEGxQRje3wdH4_aGC8Wp5S8llLPFCdmotgzymJ2O1nNcwylZcvciRrOedWEQTBgLMBdO99Y7HcSPU0MfZtK9zHVDod_dypqUuOmQvy4Idx6bI6KvR4eUn0JN8Z-2ZKhvyFCVC2SNjJflsoz-KNjVPEBmdrZ6QsPGuvy9qGUJsNedSm6kM06-bYpj5TY-Uv5pY_Fmy1fxGMGcnCrqwufw2XsdDzCMICzPeN7mrJ9ZJXqvwcEUkp0BPSHL64AlOFfjzBeW-_wMNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=jUwVf5_yo7v_ltxo7GERzNeAJTpC5HdHMgUJ4TrR_h_kmu1KRx-PbohySAbzP_dfP7xsKJNQCaDJEGxQRje3wdH4_aGC8Wp5S8llLPFCdmotgzymJ2O1nNcwylZcvciRrOedWEQTBgLMBdO99Y7HcSPU0MfZtK9zHVDod_dypqUuOmQvy4Idx6bI6KvR4eUn0JN8Z-2ZKhvyFCVC2SNjJflsoz-KNjVPEBmdrZ6QsPGuvy9qGUJsNedSm6kM06-bYpj5TY-Uv5pY_Fmy1fxGMGcnCrqwufw2XsdDzCMICzPeN7mrJ9ZJXqvwcEUkp0BPSHL64AlOFfjzBeW-_wMNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی حملات هوایی نیروی هوایی سلطنتی عربستان سعودی، مخازن سوخت در بندر الحدیده یمن (تحت کنترل انصارالله) دچار آتش‌سوزی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73232" target="_blank">📅 18:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=lS25Po-T6Di8jcjuaHsE4fF4HHa9Jw9JkPVYTeb7C-BfquSiAq0uzdPDy-nFG3zrLSFsOPnFAb-4X4ulSeTWU5W71LYEoKNPSGC1Sp3JCdLgmVXfT1ZFJROL-1SC3s-VdtvWEBG6Ce3gDrSuw2k2QV49XI6aKb2aznHaWwKPu53KfDU_GTqxMkDqpNL4bTCjfRWL-1DTmIUqKb4gjoRGhv2mpIdLhmyQW5GRSo5ldBv6ZRmnt0vg1zU1UJlYHLQcgTHBX4RyVf4Ik0R-vv_RUynPMMAwK8Cm0nYYtsvgo4txP4xvtdhZKFXxZF0phD_4nC1-9kVf2VPyjajT1PonSF6CXel2PFzufj5quJqdKGw2BHnDtUzoHpc4TtCd0IVfEfJR7ZpE3VZjciB_ihX4OzT7UAwwBUk_rrA6V12PyHyinIXIrlJmZNdl0lXXCdymHZaqsP0iNjoGzhw2zpb4W72Z0161pof8ajzw9CZcUicK1F7sHYIvCK1EvlWXG2dr2KkJwsCq0Skco-KyYSVcYhtnvSN6UU6n6cxFrXoXdIU-5F-_ffHzkmPINbosgNxTIc4v62OfQ1ltol_Js6xkzwLQm6toF78HfwynUML2oiZMURogLYEmJPrLJtdiPD6hsZ5Vmk2kVEyj8ntiYMbfO1ZT8oV-ukawoSrZJK4w-O0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=lS25Po-T6Di8jcjuaHsE4fF4HHa9Jw9JkPVYTeb7C-BfquSiAq0uzdPDy-nFG3zrLSFsOPnFAb-4X4ulSeTWU5W71LYEoKNPSGC1Sp3JCdLgmVXfT1ZFJROL-1SC3s-VdtvWEBG6Ce3gDrSuw2k2QV49XI6aKb2aznHaWwKPu53KfDU_GTqxMkDqpNL4bTCjfRWL-1DTmIUqKb4gjoRGhv2mpIdLhmyQW5GRSo5ldBv6ZRmnt0vg1zU1UJlYHLQcgTHBX4RyVf4Ik0R-vv_RUynPMMAwK8Cm0nYYtsvgo4txP4xvtdhZKFXxZF0phD_4nC1-9kVf2VPyjajT1PonSF6CXel2PFzufj5quJqdKGw2BHnDtUzoHpc4TtCd0IVfEfJR7ZpE3VZjciB_ihX4OzT7UAwwBUk_rrA6V12PyHyinIXIrlJmZNdl0lXXCdymHZaqsP0iNjoGzhw2zpb4W72Z0161pof8ajzw9CZcUicK1F7sHYIvCK1EvlWXG2dr2KkJwsCq0Skco-KyYSVcYhtnvSN6UU6n6cxFrXoXdIU-5F-_ffHzkmPINbosgNxTIc4v62OfQ1ltol_Js6xkzwLQm6toF78HfwynUML2oiZMURogLYEmJPrLJtdiPD6hsZ5Vmk2kVEyj8ntiYMbfO1ZT8oV-ukawoSrZJK4w-O0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش جمهوری اسلامی تصاویری از یه نفتکش در حال سوختن تو شرق تنگه هرمز منتشر کرد و از اعزام نیروهای جدید به دریای عرب، دریای عمان و شرق تنگه هرمز برای رصد رفت‌وآمد کشتی‌ها خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73230" target="_blank">📅 18:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=sE_3A8ddmqxXVZ-IYkb4EZuLdtV_uGlGPpErsoH000SX7ZokdVFzW8x75RV9EHisBP9iYmqcJcHjcNPdtyyiFxzvByrpwf5fDogFaYKn3Yc1kj_YU_ncIXq7y5l1HfGZ-v7Xdv8ZyEoJKyp5DKt8Zlm-9eKjNhz4u-x9Ga54zvkVFnxmw-I5yMaRCOpv-I1Kx2K3N3ErAcwoA-s9N1J6M70nJuiGtMZyvdlvruoqMxQ-q-y0mn8jHp0brXaC2mGyWQpgcz7v4saxGoCFJg9w5_E1TLA8cpi0J3vxKo8bW93lnXvuJe-toTUD7u99z_oDE-Synm-xkA8IHRh58wk4sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=sE_3A8ddmqxXVZ-IYkb4EZuLdtV_uGlGPpErsoH000SX7ZokdVFzW8x75RV9EHisBP9iYmqcJcHjcNPdtyyiFxzvByrpwf5fDogFaYKn3Yc1kj_YU_ncIXq7y5l1HfGZ-v7Xdv8ZyEoJKyp5DKt8Zlm-9eKjNhz4u-x9Ga54zvkVFnxmw-I5yMaRCOpv-I1Kx2K3N3ErAcwoA-s9N1J6M70nJuiGtMZyvdlvruoqMxQ-q-y0mn8jHp0brXaC2mGyWQpgcz7v4saxGoCFJg9w5_E1TLA8cpi0J3vxKo8bW93lnXvuJe-toTUD7u99z_oDE-Synm-xkA8IHRh58wk4sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸۰ تن میوه به علت بسته بودن تنگه هرمز رو دریا خراب شده و داره دور ریخته میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73229" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73228" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiahRb0_88ShyYezuM2z1-oKYQ9NmlwiOJTXnJRwe0Y7lQqq3GRevhiDw53jBGyN-sfOCjkf7chbyHfomy3zczTbUP9sCzTAV_zg4UNreGNXJNVPpOqPkkYQGb0Yq48IYG-sSTFl9I8GdhK0Xm2-5_tkPaq7sBOHJ_coYlMiIpze7L-6KxRviSueo6lbd45hU_XN5I9vTWWDRk_Xj0_tapwNiV7GGMbrNcWhC2nCJwq9oAr3oeuaDLtqqfKvp-gARQANBvu_EN3bmYVBlKgjPEkDZRgOJynObLhsw8oLF39Xtdf5ecJW0qvXNgtkJ9id3d7DKHXSzHVvKwX3o49MdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73227" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به صنعا، پایتخت یمن تحت کنترل انصارالله.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73226" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=EhaI2cFw5H70g2_AJly3xiJAHZ2KnaKv24up2Ect3-8QFLfWmIr4406oIXNYWItMd7AE2DAMXyGl6VRY7OlMAyJ8wH8YhVIObJLpNCpFzHsPGjRffXoWYy3hz69uUq1vMY1X91_1eFQU0YTwIrt0VIhau3E1hOXCxk_P-B8E5hcuiP27Avuajyd6YyRQLUrAvrPsRKRzbVmK_PiH2ZOkpqpS7x126xGKSNQYbOUy4ahGP9Zrw6C4fz2Hc2EB1oqf2gA0uhVEOKkGaoSkDy5qW0uA6erumA0hQduGUWUJVucvtM6F18EkaPJvDY2PDu1xwIiXwt3ErduWPp3KkmiRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=EhaI2cFw5H70g2_AJly3xiJAHZ2KnaKv24up2Ect3-8QFLfWmIr4406oIXNYWItMd7AE2DAMXyGl6VRY7OlMAyJ8wH8YhVIObJLpNCpFzHsPGjRffXoWYy3hz69uUq1vMY1X91_1eFQU0YTwIrt0VIhau3E1hOXCxk_P-B8E5hcuiP27Avuajyd6YyRQLUrAvrPsRKRzbVmK_PiH2ZOkpqpS7x126xGKSNQYbOUy4ahGP9Zrw6C4fz2Hc2EB1oqf2gA0uhVEOKkGaoSkDy5qW0uA6erumA0hQduGUWUJVucvtM6F18EkaPJvDY2PDu1xwIiXwt3ErduWPp3KkmiRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه شهروندان ایران کرجی‌ان، فقط خودشون خبر ندارن؛ چون بالاخره هر کسی یه فامیل کرجی داره.
آغوش کرج به روی همه بازه، ما هم آماده‌ایم از همه مهمون‌نوازی کنیم.
از پارک‌های زیبا و اماکن دیدنی تا رستوران‌های خوب، همه‌چی مهیاست؛ فقط مونده بیاین کرج.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73225" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#فوری؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73224" target="_blank">📅 16:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حوثی‌های یمن بار دیگر به همه کارکنان تأسیسات نفتی و فرودگاه‌های عربستان سعودی هشدار دادند که محل را ترک کنند و این نشان می‌دهد که حملات بیشتری در پیش است.
حوثی‌ها به همه «کارشناسان، مهندسان و کارگران در تمام تأسیسات نفتی عربستان سعودی» هشدار دادند که مناطقی را که نشان دهنده اهداف هستند، «چه قبلاً مورد حمله قرار گرفته باشند و چه نه»، ترک کنند تا از به خطر انداختن جان خود جلوگیری کنند.
آنها همچنین هشدارها را به خطوط هوایی، فرودگاه‌ها، مسافران و کارکنانی که قبلاً به عنوان مناطق هدف تعیین شده بودند، مجدداً تمدید کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73223" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJSee2hW9wLDKX4kFCPpXWeO55jM9njd2fIx_EsTa6zxS2N9nGiBM2iDI-sxYvaJ624mUM3T0K5RpIjrxJDUsMOyUftzbJiSFhpMauGZXUi3lI-PLxnh9T1yDwRquJXS7WmDWvfIWbI8WevqkRPTvC9jWvYK6SdB7H1YQNoc6zkTk7jy_MNrmG_6aRtH9wZYp1Wrgh_Im3MGdcq23rat0K6f4G4fGJimP05c0ZkSmXhM5a47vtyt1loNN_wtaFHag9N9Qf1gJz2j_aBj3tX0U08h5nOv-i5JAax3S9NTe4b8qJ_YUDwPczqCDf_OJElaF5bjITy73xkIzNrGj9hyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73222" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73221" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvOVcr8eOFgj01yM_-mL--knoUyt3dehR7ZE6-6HnwRQG6MSCGVlaQl78U_ANld9tRUGiaQ7lCEnPFqV8HUDxknMewLVBA9JvOias7iEsowE5zlazJSpeBKRe8jBPt5P49ms1aQY7dQfV4F1emapCxUzGH-VDdCTvM-tjEK9WYjTAGdQRn7KxwHnZt3PYBZR42X3ymULbYA6HErFaeV15hISrqOS43zrh7SI_NDTBFMJ9k7xoVzr_8BJEAW8T8EZClqFbBWM9gFggVj1UOKtdkaahE8UYbHMCnkbCHTnkAo36sV7orS9SMUzgcyss1sgweKdKVOjDsVteLITkO6Q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73220" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hhDMKkGPFVNPzqTsRBqqwUfZVhFpqk_cp6Q0b5mGwRVYsS2fwO-0Z8R_E2Zx627o8eZIvpCkJ4ZC0L4ZSrQxCHfOwqIJZchFLEcF8wgsXP-iJlq5Bxycz2EnYs3Iyj7V6Y7iZGgiQpoi1rmgMcUkZfpq4uhVikEPRDEIDDc_c2BSWdToNQu3SSo8MxvjFw_veeLydrSFR2PHH0PBKZWOOc4Wc4uLEgpn0RtgVJTkJbSWtYiT_CAY_ya6xIbDMSv8lWnVtr7gffTXTrg9Jpg4xfM8gBy59aybW42_VoAZM6w42lxw2cldzBAcPvPzjzsl3UomU2Ogc0jy3sCrkTXkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش وال‌استریت ژورنال به نقل از منابع مطلع، ایران به کشورهای منطقه هشدار داده که در صورت آغاز دوباره جنگ، ممکنه نیروهای مسلحش حمله زمینی به کشورهای همسایه انجام بدن.
ایران همچنین به مقام‌های عرب هشدار داده که ممکنه تأسیسات نفتی عربستان رو هدف قرار بده؛ در کنار حملات ادامه‌دار انصارالله به تأسیسات نفتی سعودی.
به گفته این منابع، ایران قصد داره در صورت شروع دوباره جنگ، حملاتش به نیروهای آمریکایی رو هم افزایش بده؛ از جمله تلاش برای غرق کردن ناوهای آمریکا در غرب آسیا و کشتن ملوانان حاضر در اون‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73219" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=eworEXNN9peQBjy0UrEumhkAwmfwBudXgzZAiDYR4C_CuDpxpqV3aXBbpjMscJ0fUTjKmO4jtEycWxjX0B24r38yO99yJXxA6zxe3M567zzODPMfGHJ63R5U3XugFaq55iMJYxSSiTz4wq3cOdYVBH88-A-7hWypchHMqShrt7EEddy_pEh0gtTIvjMjCy7Me9seKNii09n_zGCE3hGH57QI0bDK7bc3STHo3toESflcNKzOTwoVWIT5hUkueg82WoTWZ3m4OkNgYx27PDDzsze3PPuqx-f_mHu8YZ5FxrUCK8IkaIi_MsfEc9STujA5z83EwdRzfylD49BtKepPxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=eworEXNN9peQBjy0UrEumhkAwmfwBudXgzZAiDYR4C_CuDpxpqV3aXBbpjMscJ0fUTjKmO4jtEycWxjX0B24r38yO99yJXxA6zxe3M567zzODPMfGHJ63R5U3XugFaq55iMJYxSSiTz4wq3cOdYVBH88-A-7hWypchHMqShrt7EEddy_pEh0gtTIvjMjCy7Me9seKNii09n_zGCE3hGH57QI0bDK7bc3STHo3toESflcNKzOTwoVWIT5hUkueg82WoTWZ3m4OkNgYx27PDDzsze3PPuqx-f_mHu8YZ5FxrUCK8IkaIi_MsfEc9STujA5z83EwdRzfylD49BtKepPxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌ها در ارتفاعات چاه‌احمد تفتان، با گذشت بیش از ۷ ساعت، همچنان ادامه دارد.
به گزارش حال‌وش، در حمله افراد مسلح به ستون موتورسواران لشکر فاطمیون، بیش از ۲۰ نفر کشته یا زخمی شده‌اند.
پس از این حمله، بیش از ۴۰ خودروی نظامی و پهپادهای شناسایی و رزمی به منطقه اعزام شده‌اند و نیروهای نظامی همچنان با خمپاره و پهپاد ارتفاعات را هدف قرار می‌دهند.
این در حالی است که رسانه‌های حکومتی پیش‌تر از پایان درگیری و کشته شدن تنها سه فرد مسلح خبر داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73218" target="_blank">📅 15:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0PQ50GzqbAAEK2GO9YCtDYV-MlqG5lGp6vfszZtXFcLA8kit1Y4XJCI0GAnXzSZx3-tg5Hc3oI76CbtIlaQxWpSa_EUKWPOJGR15lGBh_q1okPXFFgXrSTv9dMmrUNrL9Xfi87TYiam879YLfld8GIxdCERuqXoffesC4WRVOLt7Y6H3ajFkH4IvVNNfYkaC0Q8yec31s5aGbHoV1AGypiRshXu8fSgjqOCUXYjfRlHZOok4vwpvSqkEzutmYH0AzDpgeEi70drnYBGyO2j0GhSirTpX7trifpss_NseTjzrh8lCmj8WmE66vtLxtyN5UtjGgLMSub6gJJIrIdt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpxq0nY1-EvHWin2ZtQRYunJV1M5exTSSlNLi9sQ-_q8alA1UhDmux_b-7kPGOJvvOhfziOFaZom14jBqsnZBpMvaqtH3ALQ6Ei33H4mcWkjxVX6bPQhaTssq4Y9YHvbRxlovK1n1zhOqPVsVeC7wip_KSocvbLMUfzrfO6whd02Q8LJoBAuddvpQehPVv4G2XiLLP5vdvjc45-oD3d94BAXk8IIKI3QGdTFoTskAlI97lIulg3YYjZNe0FMYfrtjV6vwn8hgcW0iW1sgO8vq_QevMenJE3RXnWIvsFJO6e8rp3Hgo3IiC1cTjGbCcb9O70P3sRBJ9mykoX0sa4Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p92O3FU5VKzYvzMi15x5wH0xJPxxBgBDesFxSgwy9DCDJK0wcL4rMkclP2nuEggBNRVOpGtYgW7Mo_tPmlUdsf8jyPuIH9TWlcAy-Smh0L3hQYiPpod0p5iSWuOTgMf_7zEGKDY6FQRL29xV7MRBgSxhphhZL5RXeCfMJjUT_wGL9rzkke6mgZMmSJSHdm1KxqyD_-j16AJJ-170X-dIVVU47cmAq905KkwOTy8xtDvoC04mlFXvmuwqOurmKSb_EMkSczV4xvzwRtdPiwJzqDtEXiNOn8ATVHEmePdVAafe1GrBcB0kCjEYn6T_N3odRXTNmb4qofRDWg9WNWXB9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=DKgBGTPICh9QvG-BKqDFKLWEMJmFGAusOt6bvxzyiKPG4uuoSgywnCPRj-J8yKAajYnB8kqwcYAa5zsq1vupnxuFDvZmqqT9Cn8HZz0gBrsHI34PXa69wIexr2HflWixq0Xk0s3RuxE3VCKYMmQTIdTNiv_66bcUHB0BTf3Kcs04sET7UPM6aMwmebgFdCNiWQYodUnjcZWEhggWTbs8ta5SqX2PL4RFX1foJjdhWaWM-dnRK95hN_TiQhp5Tt9DJHQY7ArolZSuPDByOY0gkErL-fiwXVYeGMtwgxMNLGo4jmpWkR9fwgzsjHJTfsSd79EnNQXyuVmrUB4jgP_eZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=DKgBGTPICh9QvG-BKqDFKLWEMJmFGAusOt6bvxzyiKPG4uuoSgywnCPRj-J8yKAajYnB8kqwcYAa5zsq1vupnxuFDvZmqqT9Cn8HZz0gBrsHI34PXa69wIexr2HflWixq0Xk0s3RuxE3VCKYMmQTIdTNiv_66bcUHB0BTf3Kcs04sET7UPM6aMwmebgFdCNiWQYodUnjcZWEhggWTbs8ta5SqX2PL4RFX1foJjdhWaWM-dnRK95hN_TiQhp5Tt9DJHQY7ArolZSuPDByOY0gkErL-fiwXVYeGMtwgxMNLGo4jmpWkR9fwgzsjHJTfsSd79EnNQXyuVmrUB4jgP_eZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e11dDC78XCF5te6TW0WkGa6RMbbRVvWPaQ0avqnKxl5qe29QQMSTlbGhgnwG_UWsp9QeqcsDRzv2O3SskY2wYadspubwHnOCG58PHHSrzbDR8x9YPr1lZvAbjaiQhSxhg1kfdBPXx9sgCV3BLxK6wO51BXk9D7NGOuF0HaqA5Ol9SjARTwlq0AZLhDG_-94YYTwFLZwA1KmsqTa0CAOnaMiu8OqsMxSGil_auSdOhn83PUI0N0TEPC4gm3GV-JkXTwM_dnq60rvuipebTgQOonAvanBGzu-xHjRvER6XwL9YOkYyeBW1gAVYANfiypwxgkmNY09BwU9B9_odjBCvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=QmQGgi7mR-fxAuXKgxsHWcEgwSaQ55pUdXTHGM1XH795uhnESqZrYYK0kHQQCr5yF48ICKWDT5pshKjpWSZvDLxVpbH38cQm4MzccQnv2PCdAto4Bnsn7ppnXDpXy-ZexnEEqt95Dh0RlLNXOZDaqjFbkuCFxBoyGBGhWLnzuNk7QiZ4DTD1ViaxyNbym-_Ak9FMh0vsLRQ-hZZeXpYMTUSv9if52pW2PXPSTu2XfnNHkATGwkuH5h_XyDsjvFNekC0W9fgM2oW3mSmTBgBirt60gwL0Pw6f9F1om86GfvUFV8UvfeEV7wNGb9kxG74gxuKxEHLDhJDao_H6qJ6p6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=QmQGgi7mR-fxAuXKgxsHWcEgwSaQ55pUdXTHGM1XH795uhnESqZrYYK0kHQQCr5yF48ICKWDT5pshKjpWSZvDLxVpbH38cQm4MzccQnv2PCdAto4Bnsn7ppnXDpXy-ZexnEEqt95Dh0RlLNXOZDaqjFbkuCFxBoyGBGhWLnzuNk7QiZ4DTD1ViaxyNbym-_Ak9FMh0vsLRQ-hZZeXpYMTUSv9if52pW2PXPSTu2XfnNHkATGwkuH5h_XyDsjvFNekC0W9fgM2oW3mSmTBgBirt60gwL0Pw6f9F1om86GfvUFV8UvfeEV7wNGb9kxG74gxuKxEHLDhJDao_H6qJ6p6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=oCZrbQ_ucN3wby_gJmURdBBV5NDrxhS8whGd_RBHt7F9m0SEuwshabVRhcRzv14YzGrhKLDvTh-KyUzqATncUPmAx4Ew3pPzfxMl_GcHOdA_DA-0G03gZ8G1rVO3gSLbFBpGS1XO14Ar-iF7xGmKVfQ5naMf4IWPM8G2tv0ZiQ3Xw9ndf7xhXj6o1kg7Oy7lojMLAZhsDum_uVUkBPKzEnV8j_5u9UJUiNZU2BrJz9J7dGnwDKb2jFRjqfrOUWHtmFZdy0DsqayjONUXC1RSw1b9wOItu-_NV60u70RpWOotdlBmvtIwHMjwX9dGe8YMoaXqXwrEtkq8W8K8Lrdzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=oCZrbQ_ucN3wby_gJmURdBBV5NDrxhS8whGd_RBHt7F9m0SEuwshabVRhcRzv14YzGrhKLDvTh-KyUzqATncUPmAx4Ew3pPzfxMl_GcHOdA_DA-0G03gZ8G1rVO3gSLbFBpGS1XO14Ar-iF7xGmKVfQ5naMf4IWPM8G2tv0ZiQ3Xw9ndf7xhXj6o1kg7Oy7lojMLAZhsDum_uVUkBPKzEnV8j_5u9UJUiNZU2BrJz9J7dGnwDKb2jFRjqfrOUWHtmFZdy0DsqayjONUXC1RSw1b9wOItu-_NV60u70RpWOotdlBmvtIwHMjwX9dGe8YMoaXqXwrEtkq8W8K8Lrdzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=u3Dyb81gMpdg25GWvJpbFB3vP4gbythTAmBY0u1kzvvzRqR-JBgluDsBuFkRpJ-JF3HMqUAlMtccXSMxdqI0KHJQg7gGwjoR5FAtTUgaA0ZubtVD4uJcaTKtrdo6PaflQVnxfHxaZFxbQ1Fc2UuKV_R3yCxbzs1ZMdjnt5qFDE8AamAgN0wktPd3P99wbSbM7-GG7Fdf03eOkj00V2TQhGCIc-A7H02L2V6vRjEyFQ4Eb9kYyH5GBfhYdqpZsD65eKOoDRoFO30rS3rscJr7YPMccNaT8a_Kvq-38iwX0MGq6ctHJeH3yvIfqjmP0HsxoIELH2DSamJ8Sr4YWP6l6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=u3Dyb81gMpdg25GWvJpbFB3vP4gbythTAmBY0u1kzvvzRqR-JBgluDsBuFkRpJ-JF3HMqUAlMtccXSMxdqI0KHJQg7gGwjoR5FAtTUgaA0ZubtVD4uJcaTKtrdo6PaflQVnxfHxaZFxbQ1Fc2UuKV_R3yCxbzs1ZMdjnt5qFDE8AamAgN0wktPd3P99wbSbM7-GG7Fdf03eOkj00V2TQhGCIc-A7H02L2V6vRjEyFQ4Eb9kYyH5GBfhYdqpZsD65eKOoDRoFO30rS3rscJr7YPMccNaT8a_Kvq-38iwX0MGq6ctHJeH3yvIfqjmP0HsxoIELH2DSamJ8Sr4YWP6l6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=HOWuGpa0wA3xasuBfMaysTyKHC_-3zY4pShthtog0jc-QufKbURxc6eQu0RXxax4fk0C4sgZSSGBSGM8DWBD4AzpnzisEU93_qjvnLSBsgxoD1jJo_Et9Ej7ERl-3BpmPG_Mp14Y9upE2BUfJ7FdAcFg2TxH9sL-mK8N_YrOyQ5nwyXjcXq5XbJNG3pyII9XzlVbd_8iKZtmc10VaOFV_BndpVPYN5hjVfeG65b_0EMSfcS44OwfIP7GESTy5gwKTTHerSxpIkwv15pN7RPmS2ci8Fkilp6AU72rlteADzOMks7-Vz3bapR2sdK8fyRytV5Sh-bV3x-1DuMpeAjlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=HOWuGpa0wA3xasuBfMaysTyKHC_-3zY4pShthtog0jc-QufKbURxc6eQu0RXxax4fk0C4sgZSSGBSGM8DWBD4AzpnzisEU93_qjvnLSBsgxoD1jJo_Et9Ej7ERl-3BpmPG_Mp14Y9upE2BUfJ7FdAcFg2TxH9sL-mK8N_YrOyQ5nwyXjcXq5XbJNG3pyII9XzlVbd_8iKZtmc10VaOFV_BndpVPYN5hjVfeG65b_0EMSfcS44OwfIP7GESTy5gwKTTHerSxpIkwv15pN7RPmS2ci8Fkilp6AU72rlteADzOMks7-Vz3bapR2sdK8fyRytV5Sh-bV3x-1DuMpeAjlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcUKfLVK53qPawAPcCn8fGgDH-hCSXthyt-tLku0sFPcG0l5t3I4zVutRIP3fC0AyCb3P3wWUN6p04vYC74jPrdf8qRo0TJLePSjZj5P-ol65DvtMRgJ1RkhjfirMcBGlnWYmoeN3th4ltlvLkcXU6uw2_rGWYFd0ULZKzr-LukYSx2FBZFNjV2c9e-vcAKdupdRmwTUgUKFvY4D8zHhpZJERndtgLrsvhBLyWbM0t8LxpKVeYaM6MontspLp7HA5A1ByRzSSKx1ItYZXWL_U1ZIrvLhYWFcjco_BCW5TDgbsV7vJPIZk7RD2pgVbWiu6xGCZ3xCDu-YYkOxC3Mu7yYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcUKfLVK53qPawAPcCn8fGgDH-hCSXthyt-tLku0sFPcG0l5t3I4zVutRIP3fC0AyCb3P3wWUN6p04vYC74jPrdf8qRo0TJLePSjZj5P-ol65DvtMRgJ1RkhjfirMcBGlnWYmoeN3th4ltlvLkcXU6uw2_rGWYFd0ULZKzr-LukYSx2FBZFNjV2c9e-vcAKdupdRmwTUgUKFvY4D8zHhpZJERndtgLrsvhBLyWbM0t8LxpKVeYaM6MontspLp7HA5A1ByRzSSKx1ItYZXWL_U1ZIrvLhYWFcjco_BCW5TDgbsV7vJPIZk7RD2pgVbWiu6xGCZ3xCDu-YYkOxC3Mu7yYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=Nh3s4InpsKY_yA_KWsQBgOOg8EVGftxIFqGUq_7tzOeSyKTVi2YOEUh3S8BmTYYtQ2Rok4Nln_VddkfY_HsYwwi2oDOdgs_zTXdrCQaaDcuiai1428G0pwUzm3iyQ0zQ99lAl5qcHs2w4rivCYjmCA-8ckLsdhKasMoEdpje0aJ6TuKF5DbC_-SfBxP_FZw3BtrDeSSDcVNYgsYLvHuxD8VOitn9SfEbMVDeA77Oc5eNswf8mi6kcEBETkJxTECJmHrcFcl7ZvXV-wOF4EQnQpq0UyLxHvECIjIoNCzcAxzTd3duCO3Id7H6RhT0G9JfClvDp1w-A2olIYlEWmg67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=Nh3s4InpsKY_yA_KWsQBgOOg8EVGftxIFqGUq_7tzOeSyKTVi2YOEUh3S8BmTYYtQ2Rok4Nln_VddkfY_HsYwwi2oDOdgs_zTXdrCQaaDcuiai1428G0pwUzm3iyQ0zQ99lAl5qcHs2w4rivCYjmCA-8ckLsdhKasMoEdpje0aJ6TuKF5DbC_-SfBxP_FZw3BtrDeSSDcVNYgsYLvHuxD8VOitn9SfEbMVDeA77Oc5eNswf8mi6kcEBETkJxTECJmHrcFcl7ZvXV-wOF4EQnQpq0UyLxHvECIjIoNCzcAxzTd3duCO3Id7H6RhT0G9JfClvDp1w-A2olIYlEWmg67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFclQ0Vg0P3Rxo4WBQwFdtgMZx7s3MfPqrIi1newUixrnKYKWL94J1zB4l5kX1uh-JXvOkpojg8lUVg_-lmWjohkDHly4lctZHfs5e8Whtz3zMSXG8sziIhHWLLcvR1r9trmPxMRWPALQPX1wZzEUwRAfnjkK_wGodyxQcj-Cl-ILp3ITKpKUQEUcDqRqmZKjwIiJz8_koHzKSdfLsbYhBXbqsWaPVgHRuUK78DSuhyr13gnAXPZ06IUjWn5V-hOAmi8B78AGd00fgPOd39gx02g7zDBr-MvhPkRJOw5j6OlO7s6MIw191QUYNvMfdBT969D0YztGuz7vh0uaeWztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_3XBEziHabHpcCzyXcBwFL9O4n8OZwlInHq9qmOgWhceOWKzFdW6BV5gu3pTHIEfylhRBmXeFmtvUr0O8W4tnjH8_FM9w_NmGxccfvjBuh6vT2tp2aGksaO70vZ5zdjTqpL131JSdrSU2TQWRxbdMmmaRbK0zOXCwYNs1gRd0iGXCdl1c_JOfNoFz2rmeBgJoxmZF7LSPjREISj5B2sH8_RWg8RoYtulKqn19ADd1edk_t_cbeR54MjX6Oo8XpOjfgKpFi-Wa6r0rx_TwjEYZqN21WLY_0UIzV1Jf0ySblmR7BrCDhKjGMEaX1FlmgquFzaInOxdLh0IzBL_awL5r9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_3XBEziHabHpcCzyXcBwFL9O4n8OZwlInHq9qmOgWhceOWKzFdW6BV5gu3pTHIEfylhRBmXeFmtvUr0O8W4tnjH8_FM9w_NmGxccfvjBuh6vT2tp2aGksaO70vZ5zdjTqpL131JSdrSU2TQWRxbdMmmaRbK0zOXCwYNs1gRd0iGXCdl1c_JOfNoFz2rmeBgJoxmZF7LSPjREISj5B2sH8_RWg8RoYtulKqn19ADd1edk_t_cbeR54MjX6Oo8XpOjfgKpFi-Wa6r0rx_TwjEYZqN21WLY_0UIzV1Jf0ySblmR7BrCDhKjGMEaX1FlmgquFzaInOxdLh0IzBL_awL5r9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=ehKCqWDvKjLjbU1vHUr5p-x6qqrdzw54BcvRLuQFcQcp23rt-BtjJA6Z-yHjbkPYAF-4e3I6tToSaCVv_2woQHmapNjeyHszlbBLdkOqA6hoSsMWKIwXYQz_B3fmB1QR4_Bbp_FM0zHdVCN4jBtpM0tjF4oQAjIzEaXTQn7FtX_Vzd2IBd_RFHib55xO4Zh90l0oHR6fohpsg7DFNBYOkwftoapP2m2OlxzBP8i927bc6dF8IIDZccfJ6ymrkkD5Qqr-6zt1-WrCQK81aPIBY_0_tF9kHvPm1XykR5VQ9Z4hG4ZgmxcSUalI_FNY3sg2r0QraDGLBN22WLJ1TrJM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=ehKCqWDvKjLjbU1vHUr5p-x6qqrdzw54BcvRLuQFcQcp23rt-BtjJA6Z-yHjbkPYAF-4e3I6tToSaCVv_2woQHmapNjeyHszlbBLdkOqA6hoSsMWKIwXYQz_B3fmB1QR4_Bbp_FM0zHdVCN4jBtpM0tjF4oQAjIzEaXTQn7FtX_Vzd2IBd_RFHib55xO4Zh90l0oHR6fohpsg7DFNBYOkwftoapP2m2OlxzBP8i927bc6dF8IIDZccfJ6ymrkkD5Qqr-6zt1-WrCQK81aPIBY_0_tF9kHvPm1XykR5VQ9Z4hG4ZgmxcSUalI_FNY3sg2r0QraDGLBN22WLJ1TrJM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TR-XDuinXfmMZkFQeaqgqvgj1R8c_-O68agNxW49m-WUVFffxeL0urbdWr2UfT6px3Ee2hATrhdGujOj3uhUQRQx1vj6fsQxsCJkzUDdMFoj5BpOR2FOSdeS72Mcxo7x71dqUKC361o327ZhC5LbF-jJ5HwawR67KaQBZd69kRe8ChtUYa5E95pdOjFIOJEn1ZCtlYYdgKrhhxcu8AxVJJ04bM0twlF6aql3nNhczpsU4wVQxVnWhU2N-koE8JMATJhUtpfKrsUzINNiho97UJcPLXX7n0rNpGHYfCMRCRAHnbcvqYPYU27PkAAggKjc24kI9PLoJwOm_6bKB0ZJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rKH3L97-0KnYdc6JtqCN9ycBFJK7YfTcMe-Hpf5X1doMSWbluPcJ4oAiZqYTMNMaDjuTuiSlwQI1AgE3Q8nGZHup0xHMvHDYQvnb7VEIHY5KrlaTe_trFt5PnBKUGF-pktjZYjoseOB7CJc-6P-H9WHavU-QFHuZN8U_xK5OqS9J-ckd4xi4vgLKEYslC1qjEOJb7Hw2f9yd-N7qHP4_VmEf7L4mYP59lcrsz1E0i5yicM-U7MUafvxhhPoGN12Cj1ja2aj7TeFEq_PiX1w1gUvIUObI-4SPSjN79jCLwz0WxR60gZPjmLPJRbwIl6Ma41OcwU66UuKovTAqZEThJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=M095PJhnlUVQ1GcTHeK_RsDPbIFUukipCYUxOEti6YJEOm2pXeLZv5z2n-IxAsnwZRHBPT2FI7vGMTTQJRzFcV4tdWAzpbJSUfnVBkrXDmdUFAbBWrOAeWUVNk5E-pH2sc1Uy6tB76pzrqA5GMeZs4Y6gswia8_q_yfGdJzhwS15-51KzYMpW55X5gDSN3cnImv5R6qSNuXGVPdEF-es1B9eKqpKoYrSIHyipLoC-WTvgZV4cMfa100R_aHtT5dgzyqPdEu_RgKaoSUnKdAwtWToXAUDbroK8h0BVk2tpLC-FzvD1xb5nyZQKE7Xt8uTXVBs-tLPrAcnBQS4zU_-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=M095PJhnlUVQ1GcTHeK_RsDPbIFUukipCYUxOEti6YJEOm2pXeLZv5z2n-IxAsnwZRHBPT2FI7vGMTTQJRzFcV4tdWAzpbJSUfnVBkrXDmdUFAbBWrOAeWUVNk5E-pH2sc1Uy6tB76pzrqA5GMeZs4Y6gswia8_q_yfGdJzhwS15-51KzYMpW55X5gDSN3cnImv5R6qSNuXGVPdEF-es1B9eKqpKoYrSIHyipLoC-WTvgZV4cMfa100R_aHtT5dgzyqPdEu_RgKaoSUnKdAwtWToXAUDbroK8h0BVk2tpLC-FzvD1xb5nyZQKE7Xt8uTXVBs-tLPrAcnBQS4zU_-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=aQ6Y9Tl5NDczaJ-e7crEO2XYZ8QQBcLR21e8jf7WBrFaDSg_DIWKHkhqBxtZxN5OZ_py7dgukOFQdFu79CyaCiioP7DRiHVI1NIn2NLqxKVe98kMP9PYkumUeolw4Fpy7abFEmjfcGjtgRGgZUw_ExFgr_8_hOhrHCm-PBINtwJluaafboe5LMJaMemEY1q4delXN00WNxuXA7IL9fAnUIks9T77enCVmzrhfvI0-876Nw7Wwb7FHlBKhv1vYTcNkC-m3NyLl-Mvg9s40oGrQSBdq-nxDREDUNVBKx6JIki9I9NE3P5MawF4dPXjhaxknClDc8rcu4gIzzkeTJpQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=aQ6Y9Tl5NDczaJ-e7crEO2XYZ8QQBcLR21e8jf7WBrFaDSg_DIWKHkhqBxtZxN5OZ_py7dgukOFQdFu79CyaCiioP7DRiHVI1NIn2NLqxKVe98kMP9PYkumUeolw4Fpy7abFEmjfcGjtgRGgZUw_ExFgr_8_hOhrHCm-PBINtwJluaafboe5LMJaMemEY1q4delXN00WNxuXA7IL9fAnUIks9T77enCVmzrhfvI0-876Nw7Wwb7FHlBKhv1vYTcNkC-m3NyLl-Mvg9s40oGrQSBdq-nxDREDUNVBKx6JIki9I9NE3P5MawF4dPXjhaxknClDc8rcu4gIzzkeTJpQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73196" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=O-Bzu_wi7cyJWFnqHrDPbJSZTi4VpC6MANHd7AupHrLoNw2UCoQ2pQBn4NmaQ5kKMlOnKQ3S-IgA5BsHEtzkbKpZVhX3Ev3sEQP-aNxC27VaKRRecNfFEZHA1berNuVyTasda2ly7GQYwJH4NIbjr7HVkBfdfCoO4r-0tsQksltbE_efkHXi0iPOQcFp6Qs5uYtYKD-ANlNaVX96JdQf0M6D0aqmXMgFxGxkxyuH17u9K02VG5qtgVkBPCnf9kc4h0zQ8xIiXE3-hP11azLkhwp3Pprp_Nn00ecwLWTLX8Pzfq9g7T7738TSzGQtbLfmZUplsNEKmZ4rZWfHa88XOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=O-Bzu_wi7cyJWFnqHrDPbJSZTi4VpC6MANHd7AupHrLoNw2UCoQ2pQBn4NmaQ5kKMlOnKQ3S-IgA5BsHEtzkbKpZVhX3Ev3sEQP-aNxC27VaKRRecNfFEZHA1berNuVyTasda2ly7GQYwJH4NIbjr7HVkBfdfCoO4r-0tsQksltbE_efkHXi0iPOQcFp6Qs5uYtYKD-ANlNaVX96JdQf0M6D0aqmXMgFxGxkxyuH17u9K02VG5qtgVkBPCnf9kc4h0zQ8xIiXE3-hP11azLkhwp3Pprp_Nn00ecwLWTLX8Pzfq9g7T7738TSzGQtbLfmZUplsNEKmZ4rZWfHa88XOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L7_-dItKL07DSyjbCdsThBmsA5QZJ2EWw_b6XXPOpvV3YEir8cEowAmo2rtm2DnVZ3B9_9ksD2t99VXqyJdLgMh87juLWH8GdhWJIqHPMaQtcx8oNIMwokzq_Y0ZYzfQysoPXVjkBlrxR_AEFC-RiY4R-Co2YHFzNJeczSz5Td1iU4d8N4jNkRyOX6fJz97Kw6lfXIlbwHEvXW3whuUSBvaCDtuKxu8cwa3eiWzuoFEv7g6KputcddNVAyZWj557ROF1p9JY4bXvUT6ePHMY3QvafyntlqCqrNn0fqlyNwjzzJAUJMHSK_Q9nZwvN0SQ5kngvSG5GB1H3DtUqARKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KrGKZnCyeM1a9oCV7i8mZPbany8eJBTplNYNpTqVsRnC3EpYZqI0J2Yomfup7hE6XsbXk7L55F8cGa607XOGEZkMugtFRdCY4ppcurimtMntxLLsbej7T_7F2UsO0wMmfINnTUCY2ojbdfwIoPgUEeOWOcAkiplH-vBujorBflfW0n9B2zDU-bDG4SusYbxTkFNT3jTzSSudkt8OHCmpKDhOAa21Hziemy78AgUmbkFnyR0evDlrZLI1CRYg6RZ3ySet_uBhzvOM5MV-6kSOMU4h7k6Tb9oS9JJ13vv-172mY0BjhmVAOPPxriTtQ2SNK-tE6cSk3HSpdbX8PG0Ziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ujsYv_7uzshG51GSRtkoGcaFS6kLrgRIVxZ_C6oKGVwIbSovrMGrhE3dKP_ifpi6n3gojvyDOYL2RNQL88Cbqz2MxvC8WtWUz6tyODlWju5uHKJ5_MdJ3fdkfdkhmDA8W1vBfa7OUBo32c-yrC1IJ04CkznG2IKqaS5ryWraiZ5yaACJGzWDKA_C1EWI4gErJk8T7redg-vqXSRd_xLwZmzTKYYSurFhwXFnEJAsYGfxCwVr6CJJW5BqgGueDaADaL_fNoGbbv36eKUqQH4piWVaMkZiG9tYrhHnFs8XJ2tbq_Ih15viD5MdDEWE6CAld5KYcKVfNDMKOiFUQOJdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WRcaainhinN_XAFEdqv30ZbpbOeKDL8zHKClq6G7q7c67ayHqOKTNehFhFseULjv6WhQgAJfcgkj9tOMc1KKsRvDu9wUNbiJ5U7xePMoiWt50qiDywtXwjGb_f8TwbNhj4HyMc54LTDVZ9zBPpGifHDI-0lv6_-oWChOHN0Gm5-5T592V4FTJgvXhAZFLjkqDSirTUnjqfCtg3mnmcRhOyOVrqzKKa7NJ-reY88DCvsK9eFHBjvvu2U4__ZNNg9Js1gNj3YH25bN3eULtyJYUlRTYvTeRb1iU84SYq0paC-RjSG8GY-1Hnl82JzHZQBTZ3J91dqdTSMm77aEkWac9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJrx7MEj2Hd4l87bbKdxT6HouH8HQcF8vcAC7mk57A1T_pPwhMJrtn-d0_b-dsZaa5xTNFCImakDYxpY4KpJCvyX4EvqVyrEetiwKgvuGWGDac5mv1M-ZUXj_wGMezBzASf_bp1c8oGow6McVNdshI3jBAYRZnKDlzV8SGSxoklQiPJvZpt9XligLCgqttJZ2ezIY66KtB8IDuDVEZuomJ3dcY7qmNFK_gr-H8q47X5K18PAP70rO4_zI-H8RvDc2UdSu2IgBozWdoC-I8s3jbXR08jXvdi7SPOqf5D8Vaaewax3mw1uJ8opPjalXYgQn7YQxSJd27Kz3tim63ay1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j-ZDRmD50El5UOeHEJeeueWRPTsnAH_9VsA7cFmRsyOsjVw5MWLfxVsEvghwqkKSK3Ugbnh8veHv1GusxJYWOhiIow3Q-J1SGUe9PI_TSJjAcqkqoy0TNfAmSIjgvTW1FzlbGIPzHD1lfjX0vQnXmBHs--Z7FZSf4eZk14v5cjgTV1-jsbkdsCTwcNQ60iX7i3ganDK2xnFK6qNP9Z8QTmdas_bep4ZnHaKIOwRO82eHC-5uGq7SuH1ttbpBJSlhk9OxVUlF4AY3zzZ70n5nCOv1hy6Sun2V5GeaN6tSbeRuXRe8jODCLd7Zt1_dE5hP2NUJ1yFlEhg_TQV1bsLpKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=RtsYIzwf-F0L1W-FE5ceV1RbGMnH3AUnL9yFBLtyykCCdB6VxRmpvpAxx01NheaxRNA_E2vQIgH_bogIJzn7yQ67Ln8sAMxMQXfg2bvzDPo7rxWSFJphAurxpAiADBoIezDPF8e_SjqaK8lKQlx8yu599RFMHdd3Uc2_AHPJapp46CPcO30J1Tkxmjrwe4a0eVY7eyeb5g2zJOOXF0UJ0JZ0x6MwKB-I9FNcuqljOUG2VdHWHndQLHORm57rk_k3nfY4yH-6AvBx7y4We1Ts9ZqIrF_K3_DnERgFVzA8dFUClHp02X8Sxs7trSfpIiwXvFu37Y-OLPr9FSPfaAZR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=RtsYIzwf-F0L1W-FE5ceV1RbGMnH3AUnL9yFBLtyykCCdB6VxRmpvpAxx01NheaxRNA_E2vQIgH_bogIJzn7yQ67Ln8sAMxMQXfg2bvzDPo7rxWSFJphAurxpAiADBoIezDPF8e_SjqaK8lKQlx8yu599RFMHdd3Uc2_AHPJapp46CPcO30J1Tkxmjrwe4a0eVY7eyeb5g2zJOOXF0UJ0JZ0x6MwKB-I9FNcuqljOUG2VdHWHndQLHORm57rk_k3nfY4yH-6AvBx7y4We1Ts9ZqIrF_K3_DnERgFVzA8dFUClHp02X8Sxs7trSfpIiwXvFu37Y-OLPr9FSPfaAZR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=Cw8HZI_-G5_C4Zghekkt_cVCsWqz9qJyQ-BtMPhxpTad30ivAMyWh3uaCSUJWBRAGuj0N2p0YYlb3Otc0eoqIp--kyVGrg1o7-etjkTuub9Mnblql3J6I9s2qLm1xYCkfajIY7ot76s2TnLc-g_gAKGtHXK63KENhCifGAlTaqOWfF-2byYUMVK3XbBhjJJZO93fRJZHcRtafKD30KTBov2REiv14ByiIf0jLxu1LqxTQIdvIFP9-CZaysDxlZJqBS1R1ipzP1m5vW8UXRhDrxm5CIdESxq6ECKo5ynjOjL4zXM1T0qafp_qVmiD2IxRQ-g1TdGYYxKGovKGozqLnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=Cw8HZI_-G5_C4Zghekkt_cVCsWqz9qJyQ-BtMPhxpTad30ivAMyWh3uaCSUJWBRAGuj0N2p0YYlb3Otc0eoqIp--kyVGrg1o7-etjkTuub9Mnblql3J6I9s2qLm1xYCkfajIY7ot76s2TnLc-g_gAKGtHXK63KENhCifGAlTaqOWfF-2byYUMVK3XbBhjJJZO93fRJZHcRtafKD30KTBov2REiv14ByiIf0jLxu1LqxTQIdvIFP9-CZaysDxlZJqBS1R1ipzP1m5vW8UXRhDrxm5CIdESxq6ECKo5ynjOjL4zXM1T0qafp_qVmiD2IxRQ-g1TdGYYxKGovKGozqLnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=rJywBz-x9EMoGIzIY0hUWc_xr74N9BBq1l8nLYFIhLzEplPocceu0m04OuU5oH6dEDfA_4NonTyh_5eUoh5c6C9FrSPEPVIX5XxoMRPnhKayB9B2GVichUW_X0LbE5s_lMlLjeO5aqvMvIjMEc-8VuoCX9yFLYlGntlFN9_jyLstCisqC7WuacvLR6uEwbJ3_30aIJakAdkzixbCiHXl4EGni4uNrqbX3OSa93WsAPa9f1VjZaWd-fgMWP5wrfYG6TiMfVVxYYpSDzPu5LQkP5H3mF3K2nmarp5GZOzOWkq8nEa44x0GzZTVqh6rrXCJeyBIjRFpCLGh4D9IVUwJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=rJywBz-x9EMoGIzIY0hUWc_xr74N9BBq1l8nLYFIhLzEplPocceu0m04OuU5oH6dEDfA_4NonTyh_5eUoh5c6C9FrSPEPVIX5XxoMRPnhKayB9B2GVichUW_X0LbE5s_lMlLjeO5aqvMvIjMEc-8VuoCX9yFLYlGntlFN9_jyLstCisqC7WuacvLR6uEwbJ3_30aIJakAdkzixbCiHXl4EGni4uNrqbX3OSa93WsAPa9f1VjZaWd-fgMWP5wrfYG6TiMfVVxYYpSDzPu5LQkP5H3mF3K2nmarp5GZOzOWkq8nEa44x0GzZTVqh6rrXCJeyBIjRFpCLGh4D9IVUwJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9p2fc-ocvwvnmSdh3Bd0FnTE8mmB2ab0_tLjHdOAOEmmeZRflT9n2pS9W4BEInDC-brLNtZ3cYb_1qykqLXatkNg79eTpXKZPRzlWJj12FiB5708I0VThnI-m3k-SM5XP8b3ZZcQagDGZgN-i8iL6PopPeySld4xUNSzM_j0i8Ka4p2q7WnEbOyFrWadig7UuZRgYSd7HqyVjNCJMWJ2Effq8if3fTYsetXuv1zpbat-Cs3PJN5XUvNkZvIbWTrxy3ElaBbOzIksTTyrsdZaVklVKaJe_0iBoko9VYBRvmcpd21uz0ww7jfwSZbwSff69OwbeOPG4814kWkD5kR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
