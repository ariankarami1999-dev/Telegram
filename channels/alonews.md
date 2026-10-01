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
<img src="https://cdn4.telesco.pe/file/LKUcJOMXwon0mKhbhlO5EuKDeiQnQUbLK71hd4w0xXNyZkC42PpXKYogpOmJRmq-Y4oA9SNmbty7xOX4JxsbAoJdaeJQ4tOzj7pMoPl4fKqckU19PYWCPuDgE-PxSNZk-D-FAlyXKhTbyhIoYORKLRPKNq1UxjrkJIEHE6Ym3bYVQgl8OTXcFTBoVw1R5iwV8NhMvuy9xHZavcgdxgmeIa6qjpL5h9F-RCWkdp9pUiRlexj-q9ts2XdcOGAOnhiLkNiiErULk6uhnutyXQVXc6ksF_thUIItdfbnx4AibW7enpBFPZYzf1B4ngbZzijzpxJh54C41bPe-YVhrcz9og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-150423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1wJrje4ON95LryVkNYsz6tN_LzIoMM5NA6LQamC1BoJjwBZHqdFIM5RF3uuYuv976Smd3JnjozQ7tsA3QHu3HfUis-LPOroauC3NQiSC-4ivWW4d9VeM-Ie4WwyfVZxtpYWb7vQhSuskrbrJmXjtYZb-DG4p9_2dMF5YV8xbTWE2yGg76zH94iBomAVN7HxCMGeAZ_KkfPRn0YvRobPY-9Vzp58W4lm6E9JBV9AWHCFgkflCAjm5eOEi6S0CHdD6jI-xPDDGUJ_cEZEfDK3eCAhan4EUD1Pw5p6rbkjFWdhjf_C2BY5zUT7KI4QOFdBu9TZPd3b1kYXq6Fhbf5Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر خروج آخرین نظامی و جنگنده ارتش آمریکا از عراق
🔴
شبکه فاکس نیوز همزمان با تکمیل عقب‌نشینی نظامیان و تسلیحات و جنگ افزارهای ارتش آمریکا از عراق و پایان ماموریت موسوم به عزم راسخ، تصویر خروج آخرین نظامی و جنگنده آمریکایی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/150423" target="_blank">📅 17:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رسانه های عبری: امارات تحقیقات درباره حادثه پرواز «فلای‌ دبی» را آغاز کرده
🔴
کمک‌ خلبان عمانی که مظنون به تلاش برای سرنگون کردن این هواپیما است، برای بازجویی به امارات منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150422" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=A3UQR4dAeyY03rD5JB0HAurKFlzPwePswWjz1DcZjnjWVExxMRn4KE1K4ICKK1dk-R0QhsYMMaVdBDlWenKiJdHuTUG4FVnbQ-o2tORIc-xEREEhHObbXpd_BXSKrkrAZFxleIgLhj5roBy99SSni9v21eGrc5K58aThxufNy2B9NZRQGrlXZgAjr79okHWt2XW8y-cwPN0OrVRcH7UZ5kE7oNvhyj82hO03K0kQaJUh8t0fJcNtVTCG2_eE6X7fhtfO4nRciWKt7dAPmLReg9QcPhLJzPMASG3HfGqgL3oGH_3nrGfYiMg4CyMymY-o8kjbhJw_PhOifXXY6aThZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=A3UQR4dAeyY03rD5JB0HAurKFlzPwePswWjz1DcZjnjWVExxMRn4KE1K4ICKK1dk-R0QhsYMMaVdBDlWenKiJdHuTUG4FVnbQ-o2tORIc-xEREEhHObbXpd_BXSKrkrAZFxleIgLhj5roBy99SSni9v21eGrc5K58aThxufNy2B9NZRQGrlXZgAjr79okHWt2XW8y-cwPN0OrVRcH7UZ5kE7oNvhyj82hO03K0kQaJUh8t0fJcNtVTCG2_eE6X7fhtfO4nRciWKt7dAPmLReg9QcPhLJzPMASG3HfGqgL3oGH_3nrGfYiMg4CyMymY-o8kjbhJw_PhOifXXY6aThZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل درباره عمان: سلطان قابوس فقید، رهبر عمان، چند سال پیش از من دعوت کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150421" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پزشکیان: عده‌ای کنار گود نشسته‌اند و می‌گویند لنگش کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/150420" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دونالد ترامپ در مصاحبه‌ای با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150419" target="_blank">📅 16:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: تحریم‌های اعمال‌شده علیه ایران یکجانبه هستند و از سوی شورای امنیت صادر نشده‌اند؛ بنابراین به تجارت خود با تهران ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/150418" target="_blank">📅 16:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پرزیدنت ترامپ به مجله تایم: اگر به سوئیس می‌گفتم: «متأسفم، نمی‌خواهم سالانه ۴۰ میلیارد دلار ضرر کنم تا ساعت‌های شما را داشته باشم»، ما همین حالا ۴۰ میلیارد دلار کسب کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150417" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو: ما می‌دانیم که خلبان مهاجم، تحت "فرآیند آموزش و تلقین افراطی اسلامی" قرار گرفته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150416" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نتانیاهو: اگر سلطان قابوس زنده بود، عمان به توافق ابراهیم می‌پیوست
🔴
بنیامین نتانیاهو درباره عمان گفت: «سلطان قابوس فقید چند سال پیش من را دعوت کرد.»
🔴
او افزود: «مطمئنم اگر سلطان قابوس زنده بود، یک شریک دیگر در توافق‌های ابراهیم داشتیم.»
🔴
نتانیاهو درباره حکومت کنونی عمان نیز گفت: «حکومت جدید موضعی سرد و فاصله‌دار دارد، بنابراین هنوز نمی‌توانم چیزی درباره آن‌ها بگویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150415" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان :  هیچ‌گاه از گفتگو فرار نکرده‌ایم و نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150414" target="_blank">📅 16:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ به مجله تایم گفت: من آی‌کیو بسیار بالایی دارم. بالاترین هوش را دارم. من خوبم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150413" target="_blank">📅 16:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6rL1w948HftpWabC9SZBKOJ9IqXQa6c4WPubV7LS-uY7tMn2vNmCsVK-O6m6CBJeBZHYFmoW-IzGWmBok2CmchJGXDpVtzCIqQfUtNemEhiTsTopBdnmQ4XKCp9YiVqCzqVM3qVgUIXDlVxEFYMiFHCzm1wsUE3rK55PbD3jmHgWSiGrI0tyoTy2jv8o4ksvgfyks7FqxUhY_S5ucljG89xgGXpBIaC30xml-_7CzrZ7R5JBo96lspGJePdLkDyXInJw7CJGqyTtBW1MTlcJ63BDoNET2qT8YagbvZzzOassB-y3mRMM9jVzMUD0nqP0unjufb1DjJGIKz69E5X9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال‌ها بار دیگر به فرودگاه ریاض بازگشته است؛ 10 هواپیما در انتظار مجوز فرود هستند و در نزدیکی فرودگاه به‌صورت دایره‌ای پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/150412" target="_blank">📅 15:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
🔴
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150411" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: تهدید بسته شدن هرمز را می‌دانستیم؛ ایران اکنون توان سابق را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/150410" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: پیشنهاد ایران برای باز کردن هرمز «تقریباً کافی» بود، اما نه کاملاً
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/150409" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: نظرسنجی‌ها جعلی‌اند؛ هر رقیبی را با اختلاف ۲۰ درصد شکست می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/150408" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: بایدن حجم عظیمی از مهمات آمریکا را در اختیار اوکراین قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150407" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم نتانیاهو پیش از حمله ۷ اکتبر هشدار دریافت کرده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150406" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: او را دوست دارم، اما سیاست‌هایش دیوانه‌وار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150405" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150404" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
🔴
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
🔴
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/150403" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150402" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150401">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150401" target="_blank">📅 15:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: ما سلاح های زیادی داریم و وضعیت ما عالی است. ما اکنون مقادیر زیادی را ذخیره و نگهداری می کنیم و آنها را بین متحدان خود توزیع خواهیم کرد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/150400" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ عملا گفت که تا انتخابات میان دوره‌ای فرصت توافق هست
🔴
حدود ۳۰روز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150399" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: با نابودی ایران، صلح را در جهان برقرار می‌کنیم
🔴
خبرنگار تایم از ترامپ پرسید: «هفته گذشته گفتید ممکن است ایران را نابود کنید. آیا همچنان چنین احتمالی وجود دارد؟» ترامپ پاسخ داد: «بله، این کار را می‌کنم؛ ممکن است.»
🔴
خبرنگار پرسید: «چطور رئیس‌جمهوری که خود را رئیس‌جمهور صلح می‌داند، از نابودی یک ملت سخن می‌گوید؟»
🔴
ترامپ پاسخ داد: «چون با نابود کردن ایران، صلح را در جهان ایجاد کرده‌ایم. فکر نمی‌کنم با وجود ایران هرگز بتوان صلح داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150398" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150396" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره رد آخرین پیشنهاد آتش بس ایران: آنچه را که یک سال پیش رد کردم، امروز با آن موافقت نخواهم کرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150395" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol4PKXD9BWQiy0NjZAyDQdHnqjD_0NqwP4TeSvpn5btZjDWmjU5KgTY7ccWndinx7v9PzfqCpBEXJB_D9_AZNsIz570HS-XObhFewTQ62ylH8CSfu6tva0J3dQshmnKLOoSQ-yE-YGLR63J0O7H1SkezNmnjunqMKe4QDmX5SsMzRQIblutCsvstTOWKIOZCemo5QoC6tPso6LnbgT8JnRL6glmu0ua9_TsB78pCs0Du3ucUdoo7HYv6CsZ3fJULI5BhcBYuda37AqJUnoXkJqzp-EvhepiuHvKkxSMs0gsz9Jk5wFQuDLbU4KZG2JYp6SilEjYPaGZFrsiX6k5cCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت فلای‌دبی اعلام کرد که به طور موقت پروازها به تل‌آویو را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150394" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150393" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
لحظاتی پیش سکه طلا از رقم بهت آور 260 میلیون تومان عبور کرد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150392" target="_blank">📅 14:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ایلان ماسک به پنتاگون در طراحی و بررسی جنگ‌های آینده کمک می‌کند
🔴
«پیت هگست»، وزیر دفاع آمریکا، خبر از آغاز پروژه‌ای داد که چگونگی جنگ‌ها در آینده و تأثیر پیشرفت سریع فناوری‌های نظامی را در آن‌ها بررسی می‌کند. «ایلان ماسک» به‌همراه بنیان‌گذار کمپانی آندوریل و رئیس پیشین مجلس نمایندگان آمریکا این پروژه پنتاگون را رهبری می‌کنند.
🔴
این طرح «پروژه مریدین» نام دارد و پیت هگست مأموریت آن را بررسی «میدان‌های نبرد آینده» و سلاح‌ها و فناوری‌هایی توصیف کرد که نیروهای نظامی ممکن است در آن میدان‌ها استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150391" target="_blank">📅 14:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بن‌گویر ،وزیر امنیت ملی اسرائیل: در جلسه کابینه امنیتی خواستار تحویل گرفتن خلبانی خواهم شد که قصد هدف قرار دادن صدها اسرائیلی را داشت؛ او در زندان‌های ما با تمام وجود معنای سیاست‌های مرا خواهد چشید، چرا که در اینجا جهنمی واقعی در انتظار اوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150390" target="_blank">📅 14:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150389">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بدرالسادات عراقچی، خواهر عباس عراقچی در گذشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150389" target="_blank">📅 14:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150388">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq7FYFykCw1E0v4p4d2ctQplXe-V-EGku9qSXorzg_NAnyhnoX75P5v6csGwqSgdgklx_Pz8f303zg9DfkGTE1PmXrIWWbFjRAiDhJ7DCgldEeWH9YSTl0qtEmJEQc89zL4Pd8zSRgairO8misdDMp2nDoJFrTbKcV6Iywb7qRbvEt5yS6blHe1GGi-jX1RKdjmx0kHLpfkfArezpfjoVpATECWDLabz9klW4CFBKFnMAUq6D6SskQmAMuNMKGJB8ZqpqCxILaIH1TmRVclPEMGcJHx947PI35PGr9u__lNU7ovHA0JAJCNXkO562dpFVz0aA8DurkJTQrsiIXsqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین در اقدامی عجیب بازی رو دقیقه 89:59 متوقف کردن و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150388" target="_blank">📅 14:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150387">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
لحظاتی پیش سکه طلا از رقم بهت آور 260 میلیون تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150387" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150386">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اکسیوس: روبیو پس از بن‌بست در مذاکرات، روز دوشنبه از هیئت ایرانی حاضر در سازمان ملل خواست آمریکا را ترک کنند
🔴
منبع آگاه: عراقچی از قبل قرار بود دوشنبه به تهران برگردد
🔴
قطر همچنان در حال گفت‌وگو با هر دو طرف درباره پیشنهاد مصالحه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150386" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150385">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نایب رئیس مجلس نیکزاد: آمریکا هرگز نمی‌تواند صادرات نفت ما را به صفر برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150385" target="_blank">📅 13:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150384">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7QBu_hODlKqLXVENBiGkqnHYcnF_0HX8wN34B3wQ5F_gmMHBG8-weuLyNOo0twKR3FuNbkSDSQ0ovTo1jtD96VpfUtt4by2QJPMHX3AuzS0zrueLWOiCqBqSnE6fNrzNgs-CRDn-iLizy331sLGB3CrdYThau5zVYEIojQgmprz-d4yb6J7lD1PI4MfDro5sVjlGK2jf7SNcboI3nttP6NqyIlsKhf4qgIyvuqWi3RuY5YqYuOr2h9OFBJ2EjNab8mvKWvbnzCMTPdeh-0pzTjbqZ8h7dSY4WtUnpN0-H8gxNT0r1qpUPPkwr1H3t0B-d1GCg0uQvTXEvH0nY30hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 هواپیمای سوخت‌رسان اکنون بر فراز تنگه هرمز پرواز می‌کنند. به نظر می‌رسد ایالات متحده تلاش می‌کند کشتی‌ها را از سمت عمان عبور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150384" target="_blank">📅 13:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2d20e32f.mp4?token=oU3IvfA7kbstwMeoewYfQRJqvfWFZTmAbgXD_v50pj5VS1GGb0QLQMZsyp-XZhd9dxvxvRcihu7ht9O1lxKzOjArAotccqfLmO6fvOmdlHuvy43Wo8MZJcQk3BAk-eP2WfKBu1kha-TukB9ivZUeX5u9VCPdS1KhoDmv5bSJ0FncoNI_ATb4QTvshy0xvj66GE7TyxwjFdJYAdpoGJ3_nekTsKJ8MqHhY7wD_hu7CQlW4H4cUXZnEo3_dkUfaf_5ymldgVfkBgB7iNfbyOSNdeim1JaQ3VIEnJ0yewEtrkxPtXaHiCWyFXPb9XgqNGppAQVufKBUYJvv9fzsHSd8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2d20e32f.mp4?token=oU3IvfA7kbstwMeoewYfQRJqvfWFZTmAbgXD_v50pj5VS1GGb0QLQMZsyp-XZhd9dxvxvRcihu7ht9O1lxKzOjArAotccqfLmO6fvOmdlHuvy43Wo8MZJcQk3BAk-eP2WfKBu1kha-TukB9ivZUeX5u9VCPdS1KhoDmv5bSJ0FncoNI_ATb4QTvshy0xvj66GE7TyxwjFdJYAdpoGJ3_nekTsKJ8MqHhY7wD_hu7CQlW4H4cUXZnEo3_dkUfaf_5ymldgVfkBgB7iNfbyOSNdeim1JaQ3VIEnJ0yewEtrkxPtXaHiCWyFXPb9XgqNGppAQVufKBUYJvv9fzsHSd8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین:
یک هدف در دریای سیاه مورد اصابت قرار گرفت، همچنین یک محل پرتاب و ذخیره‌سازی برای پهپادهای تهاجمی در منطقه اوریول
🔴
همچنین، تحریم‌هایی علیه یک مجتمع نفتی در منطقه سامارا و یک انبار تدارکاتی برای نیروهای متجاوز در منطقه برانسک اعمال شد.
🔴
ما به تلاشمان برای سلب توانایی از روسیه برای ادامه این جنگ ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150383" target="_blank">📅 13:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Atif_FMfQVwDL1SwwMf6g6h_IOoeHsdf6ocUWBU3GV1SZHRRPyzovNiygyoX5bgIYaxlfma-88Um-AVhSBJK2T7uInyo1hhbOuy1LSKtiGsQshFK2S6iWZ4k5zANqXsn6owiMR9gNRDaXQVEp7OiHtvrU2fKAl8yJslvjdXWCS3rscM5NPMnNRjdr6fn0nEJ1Ew-HgGMaBXovM5GoqYyneAX3TXSF6j-4vXrmW0xRk7Xbxj5Yzp4WXe0K8JrsplJFJMH1f-aUL-naLiqZeRnVUI03fQF-rTuQ5mFYSDhjnlcZg-fMEMqhrR5U0N4zANg6Ki55ZxC82QDmvr5imD8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
🔴
بسنت: احتمالا ظرف دو هفته چیزی از اقتصاد ایران باقی نمی ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150382" target="_blank">📅 13:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز: مقام‌های سوریه و حزب‌الله در ترکیه محرمانه دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150381" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عوستاد خوش چشم: برای بار سوم تاکید میکنم که صددرصد جنگ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150380" target="_blank">📅 13:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmbDpSKeRpsY-BIYK4g083-umKEaGmS56PCc-azyVnfHJ-y65Vj_fk3DNuucRaM3_I8ISwflw-KBWZcq7KrCZEGJCWgp0WC0zAOYI-a73GeUpmuL7zozlYtC33sRb-bnhQvUo7W_BeMRXj48T1rjkhp-BP_8mHphskx7RVb1wOhwSWEaTt77t0rUsPuevmZ0nO1jIAwryD084o9RwkPa_TmBeiIZ8BAWtwAeMG6r22xvTILEGBTGF8hQt_EhbTZu7xK5uxHt9aY-78zM8Xe2oz_wzS-vPhrXq_4gZzmLO6F-U9ntoPr0PHZDKFzwhknjg__Lu557zIur69nIcU2Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیروز تو قم عده ای برای تصویب قانون حجاب اجباری به صورت نشسته قیام کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150379" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=KRYVOZ8EBDS3quds9gKMtFNd_xS9ixaAHziH6ra1plp-CZp7USRW5INiKTpsikm_qZGWH2nu1Onogky0sFZYF2A_6PBho-0ZFRRCK9coyLdwsMdkylmK9atiV3Y48BQKMVeFYx_VszgqK_HhiS_YQZdhxELDcZyZq-kP4vedlKjWkysVyVk52VUTjWlthZD79TjHHc70TONVsbAsG60pN4vo2fUhzCN_-fT2NVWZjCpQShsdthP8wH1SvAKCuhzlacq3bhpiXj-qLjXF_zOxQqOzgzTxFIo5l4AMnoSrbvz4tcSvPKvUIYnJsiCg0W22IeM0Jep_E63dSJm4Fuu9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=KRYVOZ8EBDS3quds9gKMtFNd_xS9ixaAHziH6ra1plp-CZp7USRW5INiKTpsikm_qZGWH2nu1Onogky0sFZYF2A_6PBho-0ZFRRCK9coyLdwsMdkylmK9atiV3Y48BQKMVeFYx_VszgqK_HhiS_YQZdhxELDcZyZq-kP4vedlKjWkysVyVk52VUTjWlthZD79TjHHc70TONVsbAsG60pN4vo2fUhzCN_-fT2NVWZjCpQShsdthP8wH1SvAKCuhzlacq3bhpiXj-qLjXF_zOxQqOzgzTxFIo5l4AMnoSrbvz4tcSvPKvUIYnJsiCg0W22IeM0Jep_E63dSJm4Fuu9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد!
🔴
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150378" target="_blank">📅 12:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حکمی، معاون فناوری وزیر ارتباطات : اگر استارلینک فعال شود وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150377" target="_blank">📅 12:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بازی تیم ملی فوتبال و گینه‌بیسائو به دلیل تحریم‌ها لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150376" target="_blank">📅 12:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba87359042.mp4?token=NY1bM2Hq-fKt0wxlSMCHDIAWnE_G0y7cvHLSpKKvk-zrrq5S3R0eyNNYX3d0xf1VlwBujqGeLi_OKP873YuwVkAk0crDXyUM6XjwOfOUYLgGO0KXwlbxTFW7KLJXdrVVCl2tqxQTEqKZ6eTyrUHb9T0lh7lVZq3DmEEPgFNqhlFPvv8qKsnn6JnewjCDp3aFfpBAxUIy8QdruYyxhgPSAaTRhBn1yQAF7JT8rxp91E_Zz_cAJu4dTC65eK1zR4toBJxrpLnM67sN4r4MNY5g5ROLeWse5sMR1_-3mV-rPVNs-CpTosyJUjH10vsztkNkWWHSOSuDEFHnxH9S-rQVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba87359042.mp4?token=NY1bM2Hq-fKt0wxlSMCHDIAWnE_G0y7cvHLSpKKvk-zrrq5S3R0eyNNYX3d0xf1VlwBujqGeLi_OKP873YuwVkAk0crDXyUM6XjwOfOUYLgGO0KXwlbxTFW7KLJXdrVVCl2tqxQTEqKZ6eTyrUHb9T0lh7lVZq3DmEEPgFNqhlFPvv8qKsnn6JnewjCDp3aFfpBAxUIy8QdruYyxhgPSAaTRhBn1yQAF7JT8rxp91E_Zz_cAJu4dTC65eK1zR4toBJxrpLnM67sN4r4MNY5g5ROLeWse5sMR1_-3mV-rPVNs-CpTosyJUjH10vsztkNkWWHSOSuDEFHnxH9S-rQVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته و زخمی در میان نیروهای وابسته به عربستان در جبهه سامع در جنوب تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150375" target="_blank">📅 12:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbfIi72_vgvNBzShL_IEL_1f8l7lUm2V7Vw9_nhH-9XI8svXN08KtXrvJGcp_58DNnWVDgFIf-Mh60Tpz1qXlD3yXKI681hzEbk1Q-1306gdDmG7_Ly_Ip8zANOUt-mtaZasMMnV95OuDPYxTEPqbudGtr2EVRcWBEwfoa2fxfsnZ6yX20IAN0tRoXs4jQqjJZelOK-cQ3tNoN2Y77Obu7OjJBVD7zHtfA1uLftDqVd3dEVfOe7nl7ueAqEwKGL1rt7GjQ5Li5N3ZNvnjOsg8VYqRzi3c100VftDdKG4gwNKL34_m8prwmvODgaBoFZ4x-dSxIR8kI8IdX1D41c_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8r72bBuUC_Tq2LPJ37izXZgOMGQvuugdZJBrDtMeuST4u6-Nm0zRo0ieq0QHUae91aKUWOPwjBJQlOYw5aOubIRPZCHPu5TeAxa6oaT6UgKM3PgMhlXXfeq7ZQ15UchF2jn9jMA7dFIslJikDnFdEyGKGt1i7HEIQzyqqQvhzuONg_LhsjatfxRWGNORkWF65CQgFZOqmGadnc3ZLqFswR67OpQUEMP3OgzVoRfG8QWuzX4nTmBauQpRJqeEXlLWWkZbE4bGBImi5pC4BIuCxGvXPNN-JIdg-VAkPJd-7p_8PYlo-4sfw1Hs7wS7ZoRDIkxOptuEeYf8-BfM6tgnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای سعودی، مناطق جنوبی شهر تعز را هدف قرار می‌دهند، در حالی که تلاش‌های مداوم خود را برای جلوگیری از پیشروی حوثی ها می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150373" target="_blank">📅 12:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIVFKdTKMIIqZphvmTJODSYORkHlkFQcrROqn5le4r0LNtiYGtcRiZOhaI-kYfnZbQf9fEfNQAH-FwP6W5yjo6OFwTuUK6Gx5beE8WxSEWjaE8jn-btzVA0OHb6XEFJ2XUj63cWVqQKbknCjF43UKqQqadGYC_O3Ejdamzo9dMAjNOxyaEThRYz2R8YfNpWUWn8mvMnuyuYqbV4IPU4Xe8SPJGDYL5WwNMrWK3uQXsn2EIWgiFcs_NcIdISH5qC-IpCOdUBu6FDS3nDfGYHjujBspIk30er-TEAerb7WGcPXUt_3b-cikNbN-7fWZB0RJlwZZ9mvUYmpkS424KSuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در فروشگاه‌های کشور.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150372" target="_blank">📅 12:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خروج ترکیه از یک پایگاه نظامی در عراق
🔴
وزارت دفاع ترکیه: ما تصمیم گرفته‌ایم که پایگاه بعشیقه-زیلکان را به تدریج و بر اساس سازوکار توافق شده به مقامات عراقی تحویل دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150371" target="_blank">📅 12:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
ان بی سی: ایران پیشنهاد آمریکا رو رد کرد.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150370" target="_blank">📅 12:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قلعه نویی: استعفا از تیم ملی؟ نه، تسلیم نمیشم و دوباره تیمو میسازم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150369" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7NMzrjJvbg8O3f8IOtF2yUn7H93VpgnNTzMElicffzxHadJWB3Woy0GbB5sXqgUEsRQVEXqz9FNUVLAhrw5TxkjY18RseWlMa7mz-fTAjbuVHjNdgwhYU7T_J8lhU_dwPIJoY-7t-tW05SmwvWg0YNuATgZtRyi28JQDbQfi_DFTTV8nCGKgAeEMSzSWKG5CQ5bEJCrWSivoI8NUJaALbhJTi_j-Oz1iDBORC5yPpHIBthWWlVp5vwMdwob7niuzMrG43-RLL4c5Hy5rdrf0ClpFAw1IS0iNZ6s2Arkr7lcjbyKo--_TJVKNwQ_zB6GmP6R2sV062eyZOdVAelPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
3 هواپیما نمی‌توانند در فرودگاه بین‌المللی ابها فرود بیایند و تا زمان صدور مجوز فرود، در مسیرهای دایره‌ای پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150368" target="_blank">📅 11:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150367" target="_blank">📅 11:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو: خلبان عمانی به دبی منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150366" target="_blank">📅 11:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مدنی زاده، وزیر اقتصاد: به سالیان ساله که می‌گن دو هفته دیگه یا یک ماه دیگه اقتصاد ایران منهدم می‌شه و فروپاشی اتفاق می‌فته؛ اقتصاد ایران دچار فروپاشی نمیشه خیالتون راحت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150365" target="_blank">📅 11:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz__Bj-IjLxWNlL_YMJFmxNQp72QNM-cWwaor13KAtp__JhE_zbZXBmyLuxpUSokaYRDlY6MiIQCx0QdM0Vlca9K2Da2doDzJ-urcInq_n-d8_V01VToUc64ag7DEMs-lv9sEuH_Ped4yh_22iqG72CXyVrvp8QnpubehCqT5syR1b60gb2XTePDNqDsQB00TImXuEnYN3XguddKc3d5QYH_6ARYJOBSZWyLrEkMdY_85h_7OT0erBDJIQ1Fht8Mlh-OHNH4x56CQTobpoVU3Ckat4hCff6QNCsb1ZMmENomcb3BrquRXSmTZHWCcX1SUsLtjQwNFEAJXh_Asrsz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر از روی سایت نوبیتکس حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150364" target="_blank">📅 11:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgnFlGgFMSM-g88YazwAwkATMXoubQOqLpyBdY0lmrnxNt_sHIJ6MGclav5qZgVdtsQKubsNtRZRkWuIY6UAXEO9VdvMsTsG0GFt315r8S4ov3TttWOp9OHcwoeIs_IjE3FNbDx-DHmf7mUb9KoHo3iIOW381sUbDX6Jp5063PFGoEPdexdiqk8N8PkDRUk7MUZJPwjfkU7ZwdWwYM0ynt6-yCRazhmKiFTyhOtONhN3KCjF1frebKbXKakS0n4KwbK5FPtzHtfGSuBU3sDCICEfE6LMI7y9F1jOzDzDQtWnzm2rue8oMNjNftHDzm8MDf6hcHxiNKhxc45Px0GSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی: رضا پهلوی مایه ننگ ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150362" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igiDKf1kElZJYf1_iD8nf8QLTNXhJp5neVKL5K5bsZNZOXF5ur6w3nv6LbdIIHNQ__VPNmP-5FwIw_7xOtdj9VyhPycE-ZsagmwM7Z2BohSoyUINKbbxBFGYP1wWiEd8_J0_D2kpNc4ZqwsNThd2K6tvSDDTLcfg2bjDTJlE9II9UNDesfRqSvcRZOhXJ0mp_vtOooKSZ9c5KktrV8IUIceuBTF_G1JAVgPr5VfD8drLgah6BzbgdaW3rICSnlV1ISHx20GoRVlWJV1G20nfBO23y6pWw5hNxqqsaNQY6lmBq_dzoSonkqJoS7fqnsKyzvsKmZ6XTY-6-4wt3gCs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHz-BgIHiXX5uWb_Va9UNySAH4pfU0apnOv4OSZxOKhDgeZC-G_z5VZtDDoob1R3tEB_8O9EsQl9kAse0D4C4SzLvSXPgayJvhvceWrcjNdjeMKyXnseciXq1uCeoSgO0ZCVFLTgpXsqdZb38oTEjszKde1zdxN5mHIwkjEussq9LAQTq7E_gp5nNl68EjKeN6BpD0QsEQT5qHW73WbDhvaBV9mX0GFBTEdtn_IElzXP1up1IBcD-k8RHazAEOCc_8XGqzlb4Pnn0OVjODcdzCaRz2lFzhdCzipllYKmmqmDNASmIJBy16LSg-oXzfDpwo2LwHSG815AoiKDUyT3tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مسیر تدارکاتی نیروهای وابسته به عربستان که لحج و تعز را به یکدیگر متصل می‌کند، پس از منفجر شدن پل قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150360" target="_blank">📅 11:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150359">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نفت برنت دوباره بالا زده و داره به محدوده ۱۰۵ دلار میرسه  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150359" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnwsEjrc3BFTqfl1fWBdY90lXX3olsrVBSPZUKNPpqnwN10HUJ_YlK2-8lU5JFxXDUqrpx32fJM2-VziUswzxbn1YnKGC1YXp9Gi1rEVnmTxpjPkZNxSSxN-_JumIyhvxpKd8rH_CRzM2matdWU515pqSbrm4OLuqWhAkBKm8UkDGMWadSX7rIHTlBfZjnGGxcFbrdzKLOFFAAoEp3wsxnboE-_3HK5GosbTrgEfViuWohNgnBWYt5HopzRvGFyGyJLHNPUFRoDvtyyZeNQPLQd4fkrHiwX-OQIVBYKmjzl9QlU_clctiJ6fkH-QuXkBTwl7Z_uYSz3qTqR7hWQHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جمعه این هفته غرب و شمال‌غرب کشور در انتظار توفان خواهد بود
‏
🔴
سرعت باد به ۵۰ الی ۸۰ کیلومتر برساعت خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150358" target="_blank">📅 11:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20bffe9181.mp4?token=poXEIrG4jNbJQfi7dwzXCvC7JWneU2_wOhKsHOqrdnuOb0K2QQv3g0jo4ovcVP70tewz4zYlwwnkOR1Mrx5kKCx7A6lLr7F0nWVz7H2wVSmWpVxAnWnwsUUlRblX-ensDFHXFuC-VYLCHCFaXRJgzx3Y4riueff2fOCz-WZhfy7rV1Chkl4h-m80J1ZRDhadrhtRKjZsFCMNM_O1R9U9xMFuZzAJrtiFZBODAxGLZgrvUkPpJJyyQgWyOrzJHvtDXzjNvs3U6rVp95krmDjBC4VnZ8ocvsGx0WIVBbT2qLkUICAdc7qflTYJPWDpEx5y4Bk1mPM13iQcdycAy2gXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20bffe9181.mp4?token=poXEIrG4jNbJQfi7dwzXCvC7JWneU2_wOhKsHOqrdnuOb0K2QQv3g0jo4ovcVP70tewz4zYlwwnkOR1Mrx5kKCx7A6lLr7F0nWVz7H2wVSmWpVxAnWnwsUUlRblX-ensDFHXFuC-VYLCHCFaXRJgzx3Y4riueff2fOCz-WZhfy7rV1Chkl4h-m80J1ZRDhadrhtRKjZsFCMNM_O1R9U9xMFuZzAJrtiFZBODAxGLZgrvUkPpJJyyQgWyOrzJHvtDXzjNvs3U6rVp95krmDjBC4VnZ8ocvsGx0WIVBbT2qLkUICAdc7qflTYJPWDpEx5y4Bk1mPM13iQcdycAy2gXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌های شدیدی بین نیروهای یمنی و نیروهای وفادار به عربستان سعودی در منطقه شرقی شهر تعز رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150357" target="_blank">📅 10:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPLOTGcXFVwaF3ZniiQF1uY4wMcABdpPCIY0JosGYdVBEjbaDLcjqjyBr5GWGC5Dike3_kekiYB6dgypuOp7pV09X3V5y6zP1VVU67Pv9ugqnBYwRlzHV6uVhN1R7EX8Y2shSO6S_ZQTdbPY0o7mNuFLrgg_WX1KJkPm7BUeQ_PybNH5jKscNH06kI7LKFYDTNIOHkvz0k8IcGYRRoYSiF77nM1oqoGwfFhDI-2iKBRntENca-eansss-KxaPr-zH2_8IdniyLPMeGjsQ6H3pZF74MFSmJet07WWHZllFSerX73XrMhotWWcnBqZ8gStsZHKh4giG1PcGWxlZwwCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون آسمان امارات در اختیار چند هواپیمای نظامی ارتش آمریکا!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150356" target="_blank">📅 10:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bciK8ZazovwD0Jlnu34HQA4KnDds-SDDGOIVpbj2kt48Hof2Vwx6tz4DqW3i41e1_lXKgjvWrkYZLElK-rbFRiNUyIYZpSn7V5XeadtdKdTGDp2LXxpu-tuZ73VvuxwHXQzXUp-FJyzkVoe8MSMfmNmM8gbzhZcCojEFw9vqNGN9_z3yLYAhfbIY7jULJKFZqPAbTLwsc7pOOdRfjSWTL8f6LMewYcI_ulGp3OS5bwOyC4voDAiJ1QRUNJDnY271y8k6TFl8N8xCkECEvLL3affqEdej0HaR-GxvzzkLy_ttixS4EMzh8ZvLxgz9yOz5smq3l8Msny20DFWcelNIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئد از اول اکتبر جنگنده‌های JAS-39 گریپن خود را برای یک عملیات دوماهه ناتو به لهستان اعزام خواهد کرد؛ عملیاتی که با هدف تقویت جناح شرقی ائتلاف انجام می‌شود
🔴
این جنگنده‌ها تحت فرماندهی ناتو از آلمان، عملیات‌های هوایی را بر فراز شرق لهستان انجام خواهند داد و در حفاظت از یک مرکز لجستیکی پشتیبان اوکراین و همچنین تقویت سامانه یکپارچه دفاع هوایی و موشکی ناتو مشارکت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150355" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آژانس هوانوردی اروپا: از پرواز در حریم هوایی عربستان، لبنان، ایران، عراق، بحرین، کویت، قطر، امارات و عمان تا ۱۶ نوامبر خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150354" target="_blank">📅 10:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150353">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8oqB7hOWAGvF6v9lEMw9i9Lcy8ck_ICBYVdOR3wjLvgRtPw_Nu2r_NSGKkBlb_pLd9p6hBIOOvFtLn09MqCH633NtU06Hr7q6u-sqmcHJccJM7e-qZKaKoG0Id7AzjqVSLvbvLVLYPKXrZN72oh7h9REG-Uvke72nUWXAcUwN2uNFOcCkeFz9GlqiVAvpR_K0AXgD2kvQ2dwxnLER0ikbLmEsxvbdQnFzFQyff5PHCMiCZDnqbgqvwTRkIOLCsWGggm8O3WfIWFtLageXLkbBnNZp7SKo0XqA6rACcJJ56bYg_qQ7zA1i_swzIMhPBG7EcZ4N7jgThrLO-3TGvIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر پناهیان: اگر دانشجویان را اخراج نمی‌کنید، ما مردم به حسابشان برسیم، مماشات هم حدی داره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150353" target="_blank">📅 10:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150352">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: نفت با ۱۲ سنت معادل ۰.۱ درصد افزایش، به ۹۸.۱۵ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150352" target="_blank">📅 10:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcoaxtOm6aQNw7adJjfZrcKvtZ4emyTg216wbzRSPRbkhP-ArrDTYboJHLo1Mrk17r1Hr5ZfyF9t7kqbbnX0sXM9pL0sijM1o6E1c6TuAVZSRIM281qF8MKNxUnEtdZAPcs4Ww0CYsBCyqbDZZMGt1yp7QimAqqVCFBtCc5mDbo5DKPJnASQ7_C3ka_bsP49nRdHNJLYOfal23MIhsKMGa05pI9rUU9CzlxPOy8Rb-K54U0ulDECNBnvSbVAp2O9Zs5YoAJ25PnhF2OcENTAqqWX9ge_BdUQ5WrFJrYT5hAS4qCb-WIHlDIeU-G6derLr_oWMVdzu3bpCXBTN0vs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووری / حضور هواپیمای نظامی ترابری «نیروی هوایی فرانسه» در تنگه هرمز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150351" target="_blank">📅 10:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150350">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ae64b476.mp4?token=tQqmYZgEh__3tZt_BC7A7KaWBbx0dyDpZztzHAHP5Mi3FJas46srsA6_0FF_E_vIP5l4TNJASZOVcNNW7eIBCUFte-qRUaSJxseNeba_c4csT8Oim9gbGLoQy_ZL5_cKOJbMZTl30-EdTmn6Pi4x88j9C3dP_BxCNRGaeo8-b9wip_9rxr9l-K9p0asAjpBY0sBkcMpcIPd8Gy3awXohzNbX6SOf4Miioy5pO21tbuKViDP2TU9TKA-gFF-S749YwCzjGN2ulcUUHVHpQfdmqIDe-Z7bWJvwRo4QxtH195xkS9V_8D3XqIRXf0tDgG6LvXuQhWScUWbeMvs2NDa59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ae64b476.mp4?token=tQqmYZgEh__3tZt_BC7A7KaWBbx0dyDpZztzHAHP5Mi3FJas46srsA6_0FF_E_vIP5l4TNJASZOVcNNW7eIBCUFte-qRUaSJxseNeba_c4csT8Oim9gbGLoQy_ZL5_cKOJbMZTl30-EdTmn6Pi4x88j9C3dP_BxCNRGaeo8-b9wip_9rxr9l-K9p0asAjpBY0sBkcMpcIPd8Gy3awXohzNbX6SOf4Miioy5pO21tbuKViDP2TU9TKA-gFF-S749YwCzjGN2ulcUUHVHpQfdmqIDe-Z7bWJvwRo4QxtH195xkS9V_8D3XqIRXf0tDgG6LvXuQhWScUWbeMvs2NDa59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما در حال مبارزه با وحشیان هستیم. این افراد وحشی هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150350" target="_blank">📅 10:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150349">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e3f59506.mp4?token=NSywvDlMIG4XV1HB6nZpYZqaEa6HTOxyCw7A7tl4g7hbI4hEqRiYK1Ffg-cfUVYIoq-BTscgIpRLfWTn6PZJ9qPl5-z-v0e4BB7emr4nBwkA4ftkD9AUq122-sCQyzKRGytR4KJopHo83Gg-tdx57_L5v5Fi0MmGCjWQ2x0FrXqLu-RSx4kHLJA6d-UsDo6rclZzVQStCJqlcX9v7WuJug8cSTGB0sGUrroucTaorVtpq3UdKutFY-rxC2FNu6hXOjlUZHC6x2GbMTSlv6Ovy6UFMyE2bv7fNv9arGSo48zm43Fz9tqTqW_pCnyybo1rrIt9YZBO9i0c97Fcc31we2k5Yf3NwArPNfS8yNq5OEzzvAIA_GUEV4n4R-w-zTllO9KGYjTQgRi7AxBACgDqXIrQSJYrw30Fcq7VVIdYnLb7mhxU46VlrsHLFSC8rRm-05f4YSS4InadxBHdgajHCg_KhjWrCvHbdwjuQAvB6s-CCtaKtcrDRb9D2EiOjHgeymnDb-u2_yIFyol9yeJ10T3lvWftJYggHP0eE1Ux7lUzgfbgMTvgtbsgDxDqz-k8EYjUoldZaB5N0s214T6Nqy_CJUyQZmdaoH72lq6T7vefTWtKSqZpZE_BhJ1HLiF3Vh_02UCBpYdZ7i2g4GgbSBGJi8vn1PusZ8y7GF8e8bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e3f59506.mp4?token=NSywvDlMIG4XV1HB6nZpYZqaEa6HTOxyCw7A7tl4g7hbI4hEqRiYK1Ffg-cfUVYIoq-BTscgIpRLfWTn6PZJ9qPl5-z-v0e4BB7emr4nBwkA4ftkD9AUq122-sCQyzKRGytR4KJopHo83Gg-tdx57_L5v5Fi0MmGCjWQ2x0FrXqLu-RSx4kHLJA6d-UsDo6rclZzVQStCJqlcX9v7WuJug8cSTGB0sGUrroucTaorVtpq3UdKutFY-rxC2FNu6hXOjlUZHC6x2GbMTSlv6Ovy6UFMyE2bv7fNv9arGSo48zm43Fz9tqTqW_pCnyybo1rrIt9YZBO9i0c97Fcc31we2k5Yf3NwArPNfS8yNq5OEzzvAIA_GUEV4n4R-w-zTllO9KGYjTQgRi7AxBACgDqXIrQSJYrw30Fcq7VVIdYnLb7mhxU46VlrsHLFSC8rRm-05f4YSS4InadxBHdgajHCg_KhjWrCvHbdwjuQAvB6s-CCtaKtcrDRb9D2EiOjHgeymnDb-u2_yIFyol9yeJ10T3lvWftJYggHP0eE1Ux7lUzgfbgMTvgtbsgDxDqz-k8EYjUoldZaB5N0s214T6Nqy_CJUyQZmdaoH72lq6T7vefTWtKSqZpZE_BhJ1HLiF3Vh_02UCBpYdZ7i2g4GgbSBGJi8vn1PusZ8y7GF8e8bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: امارات جایی است که اگر به آن حمله کنیم  تمامی دردهایمان تسکین می‌یابد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150349" target="_blank">📅 09:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150348">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5551445eb4.mp4?token=JlWt43273lSCExrEYSbxqn4gtK8sOdSXmwvPrJg5ggypYmq_ofVp1I9_fnzGUZrduwRxuIfeT7OsdT01W_jiOEFUreK0vJ3NyDD_13dvXo7kpW5q7XvvhFgb38CaYZEGRldDFsXK9TthznEhMfKSJEfen_1F9abF1m2SOzSnRQT6rinXlB7_vyzThJx3vtYB4lDBcgMmZumwFHb4QEMDZrOONAly5cf6PtnqdNK6UdInjDSOlFyeN8dZYx0dqLOQttdvNo1l54hUQDp-I-GhSggT4FT383Ak-G-8SGTGqX48drTX2da5ONMQ47ve-oFVtGuXXmxeQa8I_ImCXArVBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5551445eb4.mp4?token=JlWt43273lSCExrEYSbxqn4gtK8sOdSXmwvPrJg5ggypYmq_ofVp1I9_fnzGUZrduwRxuIfeT7OsdT01W_jiOEFUreK0vJ3NyDD_13dvXo7kpW5q7XvvhFgb38CaYZEGRldDFsXK9TthznEhMfKSJEfen_1F9abF1m2SOzSnRQT6rinXlB7_vyzThJx3vtYB4lDBcgMmZumwFHb4QEMDZrOONAly5cf6PtnqdNK6UdInjDSOlFyeN8dZYx0dqLOQttdvNo1l54hUQDp-I-GhSggT4FT383Ak-G-8SGTGqX48drTX2da5ONMQ47ve-oFVtGuXXmxeQa8I_ImCXArVBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«نمی‌دانم آیا پرواز بعدی هم ربوده خواهد شد یا نه؛ اما مطمئن شوید که یک اسرائیلی کنار شما نشسته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150348" target="_blank">📅 09:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150347">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شورای امنیت ملی ترکیه: ایران و آمریکا به درگیری پایان دهند
🔴
پیامد‌های جهانی این جنگ، در آینده به طور فزاینده‌ای تشدید خواهد شد
🔴
این درگیری‌ها «چرخه‌ای تباه» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150347" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
من هیچ هشداری را قبل از ۷ اکتبر نادیده نگرفتم، زیرا هیچ هشداری دریافت نکردم. من منظورم این است که این یک دروغ کامل است
🔴
این موضوع توسط برخی کشورها یا برخی عناصر خارجی به صورت سیاسی مطرح می‌شود و کاملاً نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150346" target="_blank">📅 09:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150345">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51dfc1507f.mp4?token=W_zwQUa5FiV_YO6UWxgVTOq4PVP62cpU6oyH_r1nRODuRWb1zo9rxOF4zYOLEcqX_z7inlMS8xP5pRmWIdZLvP3yQJZamIOmbmgNSZWTomwExcYDIUFr7PE6jDbTtrX_3VEI5sc32e6oruKmoRftz0wyzHp8CE7lbuUhuP2KyCjsVz7FfHLbAx7oXFUVqkz2Zl-BGvUozSVF1jyuBFKA2OkXLcsAZoSA2oJvHDvuKAlq4WjIwqQBWa9ZvfV8rmDtho0L2URxV8J-1gcSz-16FAkd-a3nknJvoIT2P3jmS19XxBrNmJnnBKW7zmfCXMABybZgIcY0uOhqbFoxqEKIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51dfc1507f.mp4?token=W_zwQUa5FiV_YO6UWxgVTOq4PVP62cpU6oyH_r1nRODuRWb1zo9rxOF4zYOLEcqX_z7inlMS8xP5pRmWIdZLvP3yQJZamIOmbmgNSZWTomwExcYDIUFr7PE6jDbTtrX_3VEI5sc32e6oruKmoRftz0wyzHp8CE7lbuUhuP2KyCjsVz7FfHLbAx7oXFUVqkz2Zl-BGvUozSVF1jyuBFKA2OkXLcsAZoSA2oJvHDvuKAlq4WjIwqQBWa9ZvfV8rmDtho0L2URxV8J-1gcSz-16FAkd-a3nknJvoIT2P3jmS19XxBrNmJnnBKW7zmfCXMABybZgIcY0uOhqbFoxqEKIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران:
آن‌ها در تلاش هستند تا سلاح‌های هسته‌ای را توسعه دهند و روش‌هایی را برای انتقال آن‌ها به هر شهر در ایالات متحده پیدا کنند.
🔴
این کار مدتی طول خواهد کشید، اما آن‌ها روی این موضوع کار می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150345" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150344">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران:
این یک راز نیست که ایران خواهان هدف قرار دادن اسرائیلی‌ها در خارج از کشور و همچنین در داخل اسرائیل است. ما این موضوع را درک می‌کنیم.
🔴
و در واقع، ما نشانه‌هایی را نه تنها از خود آن‌ها، بلکه از گروه‌های نیابتی‌شان می‌بینیم که نشان می‌دهد آن‌ها علاقه‌مند به انجام حملات هستند، به طور قطع توسط حماس و حزب‌الله، درست قبل از انتخابات. ما شواهد روشنی در این زمینه داریم.
🔴
اما فکر می‌کنم که هنوز نمی‌دانیم آیا این اقدام به عنوان بخشی از آن طرح انجام شده است یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150344" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150343">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31728f2cf9.mp4?token=exLggXBpknhXwdu1JvdEjNfJk6Xq6917TmZperAUW9qh_99sC6s6yX-mSiQ-GsydfH-Pf1bzaFGBGUbXPHbQjPZy-LzEuLnVRKCsi2mh5iyzn0SEtIQ_OUx5Z6mokuSwrd5t-WHjuv9TnJ96Z75fxeCn0AHOEXODNLstG-r0lLT_AN8T5m__a2lfd7kicAP62S94ImBqy0MdAT2pv-oDC4sR4HjNml59BGS_GFGNDTWHG18eXFfaiqdac4zRC7Ijo6Ryo5ZYW43mXGKccuMtQ9Dh8yGsc3XaES3YDFqvQ6N-vmtGnUvG-yktcdh2WER6ev43mYl4fh4yXEEHSuLUT2oulVgM07yW8aU-b5nSgcSPBmabpaC-hn1Tq61UmfSWhQjkEPdI-e-d2q3J_3a9twXfh356-K5ps6Fda35GLvR4uvPic7DTTD2D7D5vGV0r4URzrH_C2fdpkPLmVCFaKXf4TmDAB1ExmEIQpv-nrBBAXmS6Uw83oHJuaoJ3BGYq4EvYaTb9x-Cl5tn6MywwYPYw7rHMZv_2PP1SDlL_3V7SawSBXDI58_km36GbsB9SD4ejDf-jvnNAFZjQ6WZAbEfHBTS5ykPq3mHn575KQ7sT3S96d6Zw8EE3x8GrLsq0uKe2J8zrX1Ivit7BUYx-4gcQ7wFkd2hq26dipTvmzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31728f2cf9.mp4?token=exLggXBpknhXwdu1JvdEjNfJk6Xq6917TmZperAUW9qh_99sC6s6yX-mSiQ-GsydfH-Pf1bzaFGBGUbXPHbQjPZy-LzEuLnVRKCsi2mh5iyzn0SEtIQ_OUx5Z6mokuSwrd5t-WHjuv9TnJ96Z75fxeCn0AHOEXODNLstG-r0lLT_AN8T5m__a2lfd7kicAP62S94ImBqy0MdAT2pv-oDC4sR4HjNml59BGS_GFGNDTWHG18eXFfaiqdac4zRC7Ijo6Ryo5ZYW43mXGKccuMtQ9Dh8yGsc3XaES3YDFqvQ6N-vmtGnUvG-yktcdh2WER6ev43mYl4fh4yXEEHSuLUT2oulVgM07yW8aU-b5nSgcSPBmabpaC-hn1Tq61UmfSWhQjkEPdI-e-d2q3J_3a9twXfh356-K5ps6Fda35GLvR4uvPic7DTTD2D7D5vGV0r4URzrH_C2fdpkPLmVCFaKXf4TmDAB1ExmEIQpv-nrBBAXmS6Uw83oHJuaoJ3BGYq4EvYaTb9x-Cl5tn6MywwYPYw7rHMZv_2PP1SDlL_3V7SawSBXDI58_km36GbsB9SD4ejDf-jvnNAFZjQ6WZAbEfHBTS5ykPq3mHn575KQ7sT3S96d6Zw8EE3x8GrLsq0uKe2J8zrX1Ivit7BUYx-4gcQ7wFkd2hq26dipTvmzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران: ببینید، ما فقط مانع آن‌ها هستیم. ما مانع تسخیر کل خاورمیانه توسط آن‌ها هستیم، اما هدف اصلی، شما، آمریکا، هستید.
🔴
به همین دلیل است که آن‌ها این شعارها را سر می‌دهند - آن‌ها ما را "شیطان کوچک" و شما را "شیطان بزرگ" می‌نامند، و آن‌ها قصد دارند "شیطان بزرگ" را از بین ببرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150343" target="_blank">📅 09:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150342">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3319ed1ca5.mp4?token=MvziqQ_PSTqYD0bF0nbNXyhOXOjP0Z5ngIHUUfwDO5BJCQBpnsvZsn4HzzDbyMw9jgaN2OxQmAvFtcS7FHaxIYrgSx8q51iRsVR9SoF7hkD-2cidO6YEWj_UqE79NpyHoyAlZ2jIhBQB40edMa_MBDv92BLCeiRQAAsC4_XxOp708Gk8mZRxbTQ8vB3TEKihWy9atMS3fsxImR-H-7oKmHaNqALDY1zfTqev12YBxfYk5UHnftPECui8nuOFjKI7tyAMjpD1qgHJHGjfqd1FTmKnwVZhhMlIFODjZ8o7xGhcgCIZdhbH7OuY6HiR3cl95Lwbsi2F0Al3lKXVok0OLGgvnaS_R0eUxvMYoq-KaxDz6_GUeiHG46j9d2OFXC35rUfWi3_6_CsRwMU2dlMUJHK3vWEV0dwihmVpc8OyaSZJfhOyXl70bXk1hE9dZTU4tVPb-GgVsHsRGldth0S3Wi-zWS548cJIm6FuCYgbnhTxizU0WYVuhYcMNiEAgvDsLh5_LZJRhfrh0j60m6S3qVC6ri-GM1XJ0uGJAG2eI8OMilexUesJQxgzbQzSGIMh73ITal5e9c0IdVVQYjG9mPklHdZzeOMXmmb-Io_GrlvUxaClHdzoq45OpdGH90VjDFz33_S5M0oo2liRhYER6v1n_VQCZEBCDbXan9j5THw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3319ed1ca5.mp4?token=MvziqQ_PSTqYD0bF0nbNXyhOXOjP0Z5ngIHUUfwDO5BJCQBpnsvZsn4HzzDbyMw9jgaN2OxQmAvFtcS7FHaxIYrgSx8q51iRsVR9SoF7hkD-2cidO6YEWj_UqE79NpyHoyAlZ2jIhBQB40edMa_MBDv92BLCeiRQAAsC4_XxOp708Gk8mZRxbTQ8vB3TEKihWy9atMS3fsxImR-H-7oKmHaNqALDY1zfTqev12YBxfYk5UHnftPECui8nuOFjKI7tyAMjpD1qgHJHGjfqd1FTmKnwVZhhMlIFODjZ8o7xGhcgCIZdhbH7OuY6HiR3cl95Lwbsi2F0Al3lKXVok0OLGgvnaS_R0eUxvMYoq-KaxDz6_GUeiHG46j9d2OFXC35rUfWi3_6_CsRwMU2dlMUJHK3vWEV0dwihmVpc8OyaSZJfhOyXl70bXk1hE9dZTU4tVPb-GgVsHsRGldth0S3Wi-zWS548cJIm6FuCYgbnhTxizU0WYVuhYcMNiEAgvDsLh5_LZJRhfrh0j60m6S3qVC6ri-GM1XJ0uGJAG2eI8OMilexUesJQxgzbQzSGIMh73ITal5e9c0IdVVQYjG9mPklHdZzeOMXmmb-Io_GrlvUxaClHdzoq45OpdGH90VjDFz33_S5M0oo2liRhYER6v1n_VQCZEBCDbXan9j5THw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
برخی افراد فریب این تبلیغات را خورده‌اند، تبلیغاتی که عمدتاً از طریق شبکه‌های اجتماعی انجام می‌شود و هدف آن بدنام کردن اسرائیل است.
🔴
اسرائیل در اینجا، داوود است که در برابر جالوت بنیادگرایی اسلامی جهانی می‌جنگد، جالبتی که خواهان نابودی اسرائیل، نابودی آمریکا و نابودی همه چیز در میان این دو است. این چیزی است که آن‌ها فریاد می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150342" target="_blank">📅 09:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150341">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نتانیاهو: اطلاعاتی را در اختیار انگلیس قرار دادیم که نشان می‌دهد حمله‌ای رخ خواهد داد و از سوی ایران حمایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150341" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150340">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8882baca16.mp4?token=mCI76XUC-CWypPlaPy1sIe_l6XQwALoOHWrCllZMste_nC23mnmJVaXZK_3CEmbmh9UYrBeO9YH4KBffxEJ3n3xmCUVjUJMJ45HoDyHUWtxBG5TvqSrhntR5G5Sw5eIGcCEZtxHzHS7idUXZ84gjFDcMLG6avSEQmOEhEw7Qbi1-blKPN7pS07qx9VwFy1k6De7dLK83T5PxC2htsifyDf_VUbxr7A6wZkKFr-rQPh_GAKDwHLP_h0UCGFkFzqITuvOSriEd4o_zvpCFMRrBD5UgPiABpsazMnpJ3V-XyBU25lphEh5gIjSUVJlRQkegJp8XUYU3RhyvHyMLxKBuxbD1Nh4YzMtFALIiV9xRUOeEG7X_SpPZECZ3BEys7Un0tkBLBPpw-wPu7W3SqKcaTLTV0t9q9pdBBVuKpg-oq8u5ZEJQzerAenkKkhhbEKGuJ7JTseuMEg_KbV7S8161d41966fiC7k4-pAPxGGlhu3Ngs3OnWmh-hsEsulGhVcdTw5GoplQEKm4Q3q7bumiqiYgCkyL_KzdqwieujwhNr-GjvD_sCX8PoeImmW0LCv3VYmV81mcYGM2QJmisr1Mu7O41w7MIALVmseBH8f8OSVUES7r-pvvD83EZl2Hxtf_PTZcyewIxg20_mIVnbD6pCa_vQJpAI5QnPvcEZLboQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8882baca16.mp4?token=mCI76XUC-CWypPlaPy1sIe_l6XQwALoOHWrCllZMste_nC23mnmJVaXZK_3CEmbmh9UYrBeO9YH4KBffxEJ3n3xmCUVjUJMJ45HoDyHUWtxBG5TvqSrhntR5G5Sw5eIGcCEZtxHzHS7idUXZ84gjFDcMLG6avSEQmOEhEw7Qbi1-blKPN7pS07qx9VwFy1k6De7dLK83T5PxC2htsifyDf_VUbxr7A6wZkKFr-rQPh_GAKDwHLP_h0UCGFkFzqITuvOSriEd4o_zvpCFMRrBD5UgPiABpsazMnpJ3V-XyBU25lphEh5gIjSUVJlRQkegJp8XUYU3RhyvHyMLxKBuxbD1Nh4YzMtFALIiV9xRUOeEG7X_SpPZECZ3BEys7Un0tkBLBPpw-wPu7W3SqKcaTLTV0t9q9pdBBVuKpg-oq8u5ZEJQzerAenkKkhhbEKGuJ7JTseuMEg_KbV7S8161d41966fiC7k4-pAPxGGlhu3Ngs3OnWmh-hsEsulGhVcdTw5GoplQEKm4Q3q7bumiqiYgCkyL_KzdqwieujwhNr-GjvD_sCX8PoeImmW0LCv3VYmV81mcYGM2QJmisr1Mu7O41w7MIALVmseBH8f8OSVUES7r-pvvD83EZl2Hxtf_PTZcyewIxg20_mIVnbD6pCa_vQJpAI5QnPvcEZLboQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اطلاعاتی در مورد یک حمله برنامه‌ریزی‌شده به سبک یازده سپتامبر علیه اسرائیل دارید؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: نه، یک حمله خاص به سبک یازده سپتامبر. این موضوع نیست.
🔴
موضوع، حملات تروریستی علیه اسرائیلی‌ها در خارج از کشور، در اسرائیل و داخل اسرائیل است.
🔴
ما اطلاعاتی داریم که نشان می‌دهد عوامل ایران، به ویژه حماس و حزب‌الله، در حال برنامه‌ریزی برای حملات علیه ما قبل از انتخابات هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150340" target="_blank">📅 09:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150339">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66334306bd.mp4?token=TTTWHI_S52YkqA4XCfU4pEl2Ewv-5Gv5RTWI7Jafo3ktHJ88qjVcM9iUuUkD-vzLKKu7ff8aJr4zJyyD2_Gy4IA5gPv9lDKFDRgkJZ41G2gwPaLSbdxVeP-eY-TkzU4efI2X2MVerxAtb3RkrajaOaLCgAuB404ZR4YrLYdhY3lCfYAQGhBR032L7HU58OmS59rXzeahbC2kk9gmqedn7Md0GD30UriUrpHI9u98acGJUakSmLmOa9eLgPIyZsZZ_dpvCJNmNouw-iILZba39ebF5xXfSO_Zk23v6h2peAARzF9tRGHcozeoVaCyNFyL9hC2LI-kEuLxu0HHEgi4NFw8PPw8tG8lP3AZCmekPNS-_1tTqdGcRlnqJ9Pv-lGAtb3Xv9nKAkKti_-i3iMyfM6dgEW5g17EFJmGH3ikHdSdAKULSECL0iRHmZloLBHiLlU8B4Z7yFBBDb8UzVFKXIOR0bnGV9HdeosSrQdPkY6i8FryqfwUAw07Nh2-nnyReDK6VOInODDAc4gvYpxZ9u9RJuF83axMA5-2H5VoqeBvq2Hr-9-AzXvkdFTzcXkUhzUWAkJZg86KgHN_2vcqWbUjzzpWdoDctvAKNKktoiB3LsdAVSAcPNLJAjwgnrXa5ksiR-KqXQtHLj7Slm7nV5AtD4i-aMxRa247UGAHZhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66334306bd.mp4?token=TTTWHI_S52YkqA4XCfU4pEl2Ewv-5Gv5RTWI7Jafo3ktHJ88qjVcM9iUuUkD-vzLKKu7ff8aJr4zJyyD2_Gy4IA5gPv9lDKFDRgkJZ41G2gwPaLSbdxVeP-eY-TkzU4efI2X2MVerxAtb3RkrajaOaLCgAuB404ZR4YrLYdhY3lCfYAQGhBR032L7HU58OmS59rXzeahbC2kk9gmqedn7Md0GD30UriUrpHI9u98acGJUakSmLmOa9eLgPIyZsZZ_dpvCJNmNouw-iILZba39ebF5xXfSO_Zk23v6h2peAARzF9tRGHcozeoVaCyNFyL9hC2LI-kEuLxu0HHEgi4NFw8PPw8tG8lP3AZCmekPNS-_1tTqdGcRlnqJ9Pv-lGAtb3Xv9nKAkKti_-i3iMyfM6dgEW5g17EFJmGH3ikHdSdAKULSECL0iRHmZloLBHiLlU8B4Z7yFBBDb8UzVFKXIOR0bnGV9HdeosSrQdPkY6i8FryqfwUAw07Nh2-nnyReDK6VOInODDAc4gvYpxZ9u9RJuF83axMA5-2H5VoqeBvq2Hr-9-AzXvkdFTzcXkUhzUWAkJZg86KgHN_2vcqWbUjzzpWdoDctvAKNKktoiB3LsdAVSAcPNLJAjwgnrXa5ksiR-KqXQtHLj7Slm7nV5AtD4i-aMxRa247UGAHZhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو:
فقط یک میلیون اسرائیلی از امارات متحده عربی بازدید کرده‌اند. فکر نمی‌کنم مردم از این موضوع اطلاع داشته باشند.
🔴
و این موضوع در طول جنگ نیز صادق بود. جنگ مانع از این اتفاق نشد.
🔴
این اتحاد یا این رابطه، جنگ با ایران را نیز پشت سر گذاشت. و اکنون ما باید برخی از اسرائیلی‌هایی که در آنجا هستند را ساماندهی کنیم، تغییراتی ایجاد کنیم و تدابیر امنیتی را تقویت کنیم.
🔴
من بسیار خوشحالم که امارات با ما همکاری می‌کند. ما در کنار هم کار می‌کنیم تا مطمئن شویم که این [حادثه Flydubai] دیگر تکرار نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/150339" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ :  دیروز یه لوله‌کشِ اسرائیلی که اصلا نمی‌دونست هواپیما چطوری کار می‌کنه، هواپیمای فلای‌دبی رو نجات داد؛ فقط با بالا کشیدن یه دسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150338" target="_blank">📅 09:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150337">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKRnpRAidMlMdG06Madu7HfVOUqL0rbMa-xcCmvbipJHPu6LaANQhHhEbw1kKwZmnHNjXJBnVLuz5pWTzP0xRFwdto4VyA33TcjarAEL4tSailZauwxNh-TzHH4aOZGtcJH9xd0wQfHHmAJltWqcTsiATz3wwfTznUNudjtNzwgDnQWtyWqzVcZuO3LiV8TFrUg3HoFJV_yjQ19iqmnInpQVcVktcVOsbkUVdHsTzFLIg9W3v9uHAtk4Jsgkx_6pKJTR6O63VNHzvUDcsUHvci94ymnBPuWg-ZvbucQZF0D4ohbjsWgGa9njkr-K2y4b3Cq-lGIu8Xk-kWvZbnkeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،از طریق شبکه Truth Social:
تبریک به شرکت بزرگ بوئینگ به خاطر تولید هواپیمایی به نام 737 Max که توانست در برابر نیروهای گرانشی و فشارها، عملکردی بسیار فراتر از آنچه که برای آن طراحی و انتظار می‌رفت، از خود نشان دهد.
🔴
این، نمایش شگفت‌انگیزی از برنامه‌ریزی و طراحی دقیق و قدرتمند سازه‌ای بود.
🔴
این زمان آن رسیده است که به شرکت بوئینگ، که در حال حاضر بهترین هواپیماهای مسافربری را تولید می‌کند، به خاطر "هوشمندی" فوق‌العاده این هواپیما، اعتبار لازم داده شود.
🔴
به کلی اورتبرگ و تمام مسئولین و همکارانش در شرکت بوئینگ، تبریک می‌گویم به خاطر انجام یک کار عالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150337" target="_blank">📅 08:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150336">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روسیه اروپا را تهدید کرد: اگر جنگی آغاز شود، کوتاه و برق‌آسا خواهد بود
🔴
ماریا زاخاروا، سخنگوی وزارت خارجه روسیه، گفت مسکو قصد تهدید کشورهای اروپایی را ندارد، اما در برابر هرگونه اقدام نظامی از تمامی توانمندی‌های خود استفاده خواهد کرد.
🔴
او تأکید کرد روسیه ابزار لازم برای مقابله با هرگونه تجاوز را در اختیار دارد و می‌تواند مهاجم را شکست دهد.
🔴
زاخاروا هشدار داد اگر کشورهای اروپایی به روسیه حمله کنند، جنگ «کاملاً متفاوت و بسیار کوتاه» خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150336" target="_blank">📅 08:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2owFrsAU6MZjot6fXfdVnkvW4PfrZMQEfLuLZG7_mLmmhrgLzdKEAyzHpU7kJw5Y6xfr3iNBFrYf4dJQhg7_jfAkMsDP6zv5DgD3oH-XlKAr0KTiqs5kVSPYKVOwyYV4xj9nFuuWS6jO1QHmZo8BjdWq_haNPrTRe2pMoFFc4H_fl8XVgBdIYVjFx5OT6bzM7QvAwAtm_hcCrCgFs8-0GnGWAwie8UI7iSBXwEfM7OXk8vaX_8PpXg7c9uMJpabdme5ohr8wgMP5DvZiVO_0wicL6aGMMad3xiGaQCRtgQgd_htCMLq9LRP5baE89KiIUKgGNp6EgogfvsqlasRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران شلیک موشک به سمت اردن را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150335" target="_blank">📅 08:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb52ef312.mp4?token=o13p04HQPfzFpRwQoDJDwvrtBq5RclBoVF4f3nLA-7hGeMBN1hQuCh5s-tWzQ6Tm4qgmTBTlGW_3TZHcHgbF_azPpWFjbxa6FF3F-YElhGHBwHdlreGKNYebiy1cKEEPL96vtbOnJp-BKauAOXenINjzm2s8AD1_K7EftpS1Z1QpHcfYo_813UO9iUTDtzQQNax__IW53D7hq8I7hD-hQEl9_mamIu_zEmUzQ4FDNxG5aDtnESvawRCrZEOLbDluLe727sWY_Z7hkPFBT3cdnXxIwKq3M-i-Bo7fYauPxIgHJTg9HZhZiC8RAJW-n8w8R-PBfgGgKPMjxiMhNZ8j7ZKxxwCf4I1DgNYfq6uoZ48ttVwbimC7jRC-DH5Fz7yY9sBqeF-3_nV8DUzTFE6x8vE3yn-y8RyWiSWPbkGeOa0UgvKbVO3eH2Vvrqj6UGq2cK_wU0RsVFGCgjwZHbg1uy6MDgrUuGkl6K-qDj8dOkxsKfj0lIm4yTnACqftCiWJuRnkc9fNqn1ZptU-yoI50qbJnggcWk24DllaABBk7pL7K9OJD7nG4hk011rxqJ0pjCDl7qZ_aBG2t5iOkG3_5Gpw4OC9LzNNCdqMSNwBrNcZI_vPT3XHxdMSPzyNVkssWY2pFe8HkkvlaO4LoZixd_pMlb565xAfe5yi-vEOUEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb52ef312.mp4?token=o13p04HQPfzFpRwQoDJDwvrtBq5RclBoVF4f3nLA-7hGeMBN1hQuCh5s-tWzQ6Tm4qgmTBTlGW_3TZHcHgbF_azPpWFjbxa6FF3F-YElhGHBwHdlreGKNYebiy1cKEEPL96vtbOnJp-BKauAOXenINjzm2s8AD1_K7EftpS1Z1QpHcfYo_813UO9iUTDtzQQNax__IW53D7hq8I7hD-hQEl9_mamIu_zEmUzQ4FDNxG5aDtnESvawRCrZEOLbDluLe727sWY_Z7hkPFBT3cdnXxIwKq3M-i-Bo7fYauPxIgHJTg9HZhZiC8RAJW-n8w8R-PBfgGgKPMjxiMhNZ8j7ZKxxwCf4I1DgNYfq6uoZ48ttVwbimC7jRC-DH5Fz7yY9sBqeF-3_nV8DUzTFE6x8vE3yn-y8RyWiSWPbkGeOa0UgvKbVO3eH2Vvrqj6UGq2cK_wU0RsVFGCgjwZHbg1uy6MDgrUuGkl6K-qDj8dOkxsKfj0lIm4yTnACqftCiWJuRnkc9fNqn1ZptU-yoI50qbJnggcWk24DllaABBk7pL7K9OJD7nG4hk011rxqJ0pjCDl7qZ_aBG2t5iOkG3_5Gpw4OC9LzNNCdqMSNwBrNcZI_vPT3XHxdMSPzyNVkssWY2pFe8HkkvlaO4LoZixd_pMlb565xAfe5yi-vEOUEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه چیزی شما را مطمئن می‌کند که حادثه Flydubai یک اقدام تروریستی بوده است و نه یک مشکل روانی؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: خب، ممکن است اینطور باشد. من نمی‌دانم. به زودی متوجه خواهیم شد.
🔴
ما نشانه‌هایی داشتیم که ایران، و به ویژه از طریق عوامل خود، قصد داشت حملات تروریستی علیه اسرائیل و شهروندان اسرائیلی در خارج از کشور را افزایش دهد.
🔴
اما فکر می‌کنم که هنوز خیلی زود است که بگوییم آیا در این ماجرا همدستی ایرانی وجود داشته است یا خیر. فکر می‌کنم به زودی متوجه خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/150334" target="_blank">📅 08:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f751ae8.mp4?token=DLDzyNjv5a9Z_F3wHT8D_Yf4w3oVBPu_MTeVYPOqAevcujRyZAIeHJHbDu_wZOfdTLaOn7kRE5gA7cIHt76Tz5CwiP883n50GJGoB6CsU4wSb1IHOol6uY1bc9mXVy1gn6I7lsNd_E88R_lODFWysyPW7BIcuDrLbOzYYK35_eb5M_KMtXi6Ijv7bsev0HomFg6CwNSgUngmR_sSpmkv4FyQnnHQH2_8tlLM88dR48Qjt4pBw3v1UsDntO9BC0jiaje8mk_Gtj9Llh-mSd8ZKuLlWkHsTozda9CYFjjI_k76e2sUKC6jYi5aY_DH2EYdQkkVJqGQCBNI_gU6dMIQ-IG0lyH5lyFtNtA2vdNZ46xSGIBsY5HXqL1lTeX-KP4uXt3YOFMp7a7TO1xwtoXzg8YtM1AavUGB3y7815v7jFP-itFrxVpNxnsqfWfIt6fhcnxqf0FSDtStFq73Vmt-d2aZ_nf-AdMucjqDSYDlAnkP4A3cDc19_k8OtuJZs5KUTiiRWHje0RJp2XU_HGtDKaIF99BON2UlZ9KtXFi_yOLCY5x5-tYl4zgMmNTmedIucBom5Dk6KlMv2pS_vAMSxk98QR4Bt_2sIljzM1EFpWol4h-IZQux0OXfNTy3iD9bVyEX0XYlxgpG692cSbky9oTCl3Ianxh05tgKQLof9XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f751ae8.mp4?token=DLDzyNjv5a9Z_F3wHT8D_Yf4w3oVBPu_MTeVYPOqAevcujRyZAIeHJHbDu_wZOfdTLaOn7kRE5gA7cIHt76Tz5CwiP883n50GJGoB6CsU4wSb1IHOol6uY1bc9mXVy1gn6I7lsNd_E88R_lODFWysyPW7BIcuDrLbOzYYK35_eb5M_KMtXi6Ijv7bsev0HomFg6CwNSgUngmR_sSpmkv4FyQnnHQH2_8tlLM88dR48Qjt4pBw3v1UsDntO9BC0jiaje8mk_Gtj9Llh-mSd8ZKuLlWkHsTozda9CYFjjI_k76e2sUKC6jYi5aY_DH2EYdQkkVJqGQCBNI_gU6dMIQ-IG0lyH5lyFtNtA2vdNZ46xSGIBsY5HXqL1lTeX-KP4uXt3YOFMp7a7TO1xwtoXzg8YtM1AavUGB3y7815v7jFP-itFrxVpNxnsqfWfIt6fhcnxqf0FSDtStFq73Vmt-d2aZ_nf-AdMucjqDSYDlAnkP4A3cDc19_k8OtuJZs5KUTiiRWHje0RJp2XU_HGtDKaIF99BON2UlZ9KtXFi_yOLCY5x5-tYl4zgMmNTmedIucBom5Dk6KlMv2pS_vAMSxk98QR4Bt_2sIljzM1EFpWol4h-IZQux0OXfNTy3iD9bVyEX0XYlxgpG692cSbky9oTCl3Ianxh05tgKQLof9XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا در حال حاضر نگران پروازهای دیگری هستید که مقصدشان اسرائیل است؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: بله، ما نگران هستیم
🔴
من با رئیس‌جمهور امارات متحده عربی، شیخ محمد بن زاید، صحبت کردم و ما توافق کردیم که پروازهای شرکت هواپیمایی FlyDubai را به مدت چند روز متوقف کنیم، تمام شرایط را بررسی کنیم و تعدیلات امنیتی لازم را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150333" target="_blank">📅 08:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: از زمان روی کار آمدن ترامپ بیش از ۲۵۰ هزار روادید لغو  شده
🔴
افرادی را که مرتکب جرم می‌شوند، از تروریسم حمایت می‌کنند، آمریکایی‌ ها را فریب می‌دهند یا از نظام مهاجرتی ما سوءاستفاده می‌کنند، شناسایی و روادید آن‌ها را لغو می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/150332" target="_blank">📅 08:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150331">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اکسیوس: روبیو پس از بن‌بست در مذاکرات، روز دوشنبه از هیئت ایرانی حاضر در سازمان ملل خواست آمریکا را ترک کنند
🔴
منبع آگاه: عراقچی از قبل قرار بود دوشنبه به تهران برگردد
🔴
قطر همچنان در حال گفت‌وگو با هر دو طرف درباره پیشنهاد مصالحه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/150331" target="_blank">📅 08:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150330">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آتش‌سوزی مهیب در گمرک اسلام قلعه؛ ۲۰ کامیون در آتش سوختند
🔴
یک حادثه در گمرک اسلام قلعه به‌سرعت به حریقی گسترده تبدیل شد و ده‌ها خودروی سنگین را درگیر کرد؛ آتش از یک تانکر حامل سوخت آغاز شد و در ادامه حدود ۲۰ کامیون طعمه حریق شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/150330" target="_blank">📅 02:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یک جانفدا: اصلااااا مهم نیست گرونیا، گشنگی هم مهم نیست، رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/150329" target="_blank">📅 01:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: ایران نباید سلاح هسته‌ای داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/150328" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ : الان تنگه هرمز را در دستمونه، عملاً اونو اداره می‌کنیم و کنترل کامل در دست ماست؛ البته می‌دانم که این وضعیت همیشه می‌تواند تغییر کند. کافی است یک مین بندازند؛بنابراین اگر واقعاً مین باشه، شرکتها حاضر نیستند کشتی‌های یک میلیارد دلاری خودشونو از تنگه هرمز عبور بدن. اما دوباره تأکید می‌کنم ، الان نفت بیشتری از تنگه در حال خروج است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/150327" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM7OQiRBFmX8jeE50Kx3-cx0xZbL7w313D11E0jujGGpAIBddRthG2BSlSBlvRgiyi58X8GcNbOnovJDbciopHSX2RmD_97zEODQt494SwRscPGQnAe-svJEka35p2FB-2Knv5BraG112XDo9QH0tk3Fqa6la1UlXi7UyjssdjymuJtnHviEuDW3rLcOJCeiEKmcS0P2sWKjUdlNDrrRvEem73rH824roMaLPT8cF9KNPWrVR6L9Rbr2gRGfolx3lTwS5Rf8ohvSkJKsL4peBvLefQbofTLlAmQHPn7utWXazTFW_O2JCPNWqm4SOWMHePkOAIhiwlwonmncA_z7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حکیمی: اگه استارلینک فراگیر بشه، برق رو قطع می‌کنیم
🔴
معاون وزیر ارتباطات گفته اگه استارلینک بین مردم جا بیفته، تو بحران نمی‌تونن اینترنت رو قطع کنن. برای همین مجبور می‌شن برق رو کامل قطع کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/150326" target="_blank">📅 01:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/150325" target="_blank">📅 01:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: رهبران آنها به شدت برای کنترل مبارزه می‌کنند، اما کنترل چه چیزی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/150324" target="_blank">📅 00:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed59a70323.mp4?token=Bw7DcePfIxNcZyRn6wSt44J57Y_wnhv_cgP8S2dBr5_Es4Ts_X8NAbBQMcex2DsiMEm_k-lCxkvL19WgwpE1UJdKN26kbz1HB9bLEfiT45Hr-eDAJ4oE5Ux-K6cLlYO1_PEjsp6W3s4C4TV3ji4qTnMerDT1pAABwqiWqM-S2rNf6vCs1JBZcrHyY5GMvjsmWDRh3iRGaeF7JdWjGCnY6fDib3dqzsDEV7EqWjBCOznTKwlrFSt83u39zj6W_VGswNFZC9yGmZNfGAFeVyjX1z5cv8Gl4by6JPiXkQNXnXC_LiVX9itKlTiMZhP5muQh-mvyEY1C98BJQ9PCqWtyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed59a70323.mp4?token=Bw7DcePfIxNcZyRn6wSt44J57Y_wnhv_cgP8S2dBr5_Es4Ts_X8NAbBQMcex2DsiMEm_k-lCxkvL19WgwpE1UJdKN26kbz1HB9bLEfiT45Hr-eDAJ4oE5Ux-K6cLlYO1_PEjsp6W3s4C4TV3ji4qTnMerDT1pAABwqiWqM-S2rNf6vCs1JBZcrHyY5GMvjsmWDRh3iRGaeF7JdWjGCnY6fDib3dqzsDEV7EqWjBCOznTKwlrFSt83u39zj6W_VGswNFZC9yGmZNfGAFeVyjX1z5cv8Gl4by6JPiXkQNXnXC_LiVX9itKlTiMZhP5muQh-mvyEY1C98BJQ9PCqWtyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ترامپ درباره نقش ایران در حادثه فرفورد: موضوع را به‌طور جدی بررسی می‌کنیم
‏
🔴
از دونالد ترامپ درباره اظهارات اندی برنهام، نخست‌وزیر بریتانیا، مبنی بر وجود «نشانه‌های قوی» از احتمال نقش ایران در حادثه نزدیک پایگاه هوایی RAF Fairford سؤال شد. برنهام گفته تحقیقات درباره این پرونده همچنان ادامه دارد.
‏
🔴
ترامپ در پاسخ گفت: «ما در حال بررسی این موضوع هستیم؛ آن را به‌طور جدی بررسی می‌کنیم. ایران در حال حاضر مشکلات زیادی دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/150323" target="_blank">📅 00:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=IPQu9w5DQ8MgBxpo5N2tgiVEKI6T0DUynl5eeBaL5UwoBYRom_SPxT0URGU1E72GwCshLJygAxf3DtjFQm8OlWRY4NRKJ7LC-ppuJam9h4tUAfIRBjvp7dI55wxeedSzJGM_-9edVtuY53oSQswxlpUeKG9oX4C4UmVOlPnHLQsl8XgingT0C_E7Lyh5V_ynFCR1XLAkGkg3ahfiaT4TtryrxSGJnfD8xKFAl74yi23H1krzPZSXyNCkuvvRASOOvwOEoK4V_RvGqNOGFkRRpNKRc14JdEcuG7unk4RoJ2bA8HQfuIAnqQkspSuCzXThHeLJywbREMb-ba8-1T0vig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=IPQu9w5DQ8MgBxpo5N2tgiVEKI6T0DUynl5eeBaL5UwoBYRom_SPxT0URGU1E72GwCshLJygAxf3DtjFQm8OlWRY4NRKJ7LC-ppuJam9h4tUAfIRBjvp7dI55wxeedSzJGM_-9edVtuY53oSQswxlpUeKG9oX4C4UmVOlPnHLQsl8XgingT0C_E7Lyh5V_ynFCR1XLAkGkg3ahfiaT4TtryrxSGJnfD8xKFAl74yi23H1krzPZSXyNCkuvvRASOOvwOEoK4V_RvGqNOGFkRRpNKRc14JdEcuG7unk4RoJ2bA8HQfuIAnqQkspSuCzXThHeLJywbREMb-ba8-1T0vig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما ایرانی‌ها را «دیوانه» توصیف می‌کنید. چطور می‌توان با افراد «دیوانه» به توافق رسید؟
🔴
ترامپ: شاید آنها را بمباران کنیم. باید درباره این موضوع تصمیم بگیریم؛ یا آنها را بمباران می‌کنیم یا به توافق می‌رسیم. زمان تصمیم‌گیری نزدیک است. این ماجرا خیلی زود به پایان خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/150322" target="_blank">📅 00:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
به قله رسیدیم
‼️
🔴
رئیس کمیسیون لوازم خانگی اتاق اصناف در تلویزیون : خانواده‌ها برای جهیزیه به جای ۲۰ قلم فقط می‌توانند ۳ یا ۴ قلم جنس بخرند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/150321" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مهلت ۴۵روزه شعام تموم شد
🚨</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/150320" target="_blank">📅 00:31 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
