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
<img src="https://cdn4.telesco.pe/file/J5JFblfJNQ0YddQag41ngFPQkhZvh2zSv_kGiAH0vfEVFePHuXB8CzSGsoUWq1K4o3DPntHCy4ak969KYBLI5w0fW5qIz6KgeXTpNzkjXRIGpSQBIkyNnlqNPmu264xizUyvl-oyzyXMOMHAZIYEIPoouNlRQ5O1xdVXVbsYlHAkZ6o756hDQpH9xHeZTuIbeHRP613B53TITNdDQJ-F-CGfbSQd3e6fk0Xqxi11-QUKazIxm-djYhopthDO8ECfOefsjT4wQA9shx3ZwVnEzKUP0S1r66WZ2oV_LwcE4BS5AkByp29x4t_uU0R_DbmQhxLHyN1kHh1lmAgq0R_lJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 05:55:40</div>
<hr>

<div class="tg-post" id="msg-125425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O56C9eIa_gX5pzkIM6rs95xLhUUpZcG8BLR3Xc8U-aXQJCHqLjvWNZfiVVma2oaKDmKWRybkYjYI3AgC8iBCcaYY5RQZ4m7e7zoLzuMOiPaR3K4XnyWK5-DKI4qdkIqofSWktnAP8lIKoDmKezXeMV-QyxzlrdVQafD5AIb3CSevkeo0QysELvZVXHVCsFQISRFJq2DkCW0e0mjTc0tctRtAFftaVXzqK8yW5mhAM5VKjxW2tMbGVeTcJKC7rRyNQzLmXXMYFzm2qHF1x4F2rp_zFZ_nseWDPheQaWIwXhINBTtZ7_yKKFM9SR3qkqdAvz5nda-sSYeU3NzQQcrPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​
🔼
کسب درآمد از فروش  VPN
هنوزم ممکنه!
درآمد چندتا از نماینده‌ها رو ببین
👀
پنل نمایندگی وی‌پی‌ان گذربان، سریع‌ترین و
راحت‌ترین راه برای پول درآوردنه
✔️
​
🤑
چرا پنل نمایندگی گذربان؟
🚀
سرعت و کیفیت بی‌نظیر
⚙️
پنل مدیریتی حرفه‌ای
💵
سود عالی
⭐️
بدون ریسک
​فرصت رو از دست نده و کلمه «الو» رو بفرست
👇
@GozarBanAdmin
@GozarBanAdmin
@GozarBanAdmin</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/125425" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ به ان بی سی: خیلی از مقاماتشون هم مغرورن یه سری کارها هست که هیچ‌وقت فکر نمی‌کردن مجبور بشن انجام بدن
🔴
ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره
🔴
داریم درباره ۴۷ سال حرف می‌زنیم که هر کاری خواستن انجام دادن
🔴
توافق اوباما با ایران خیلی بد بود و از قبل هم عملاً تاریخش تموم شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/125424" target="_blank">📅 01:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ به NBC : وضعیت برای اونا واقعاً سخته
🔴
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
🔴
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
🔴
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
🔴
این موضوع باید خیلی وقت پیش حل می‌شد
🔴
توسط رئیس‌جمهورهای قبلی یا کشورهای دیگه، لزوماً هم ما نه
🔴
ولی واقعیت اینه که دو بار تا ساخت سلاح هسته‌ای خیلی نزدیک شده بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/125423" target="_blank">📅 01:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125422" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=Jpkdph4gtkigefSOD9YEjisGAIgKyypYEF3yPXughwC1MoIWoEXcWPK9gauGo1UHEm7YH8f5fTviWiFS8JIJnQvRlQKpQ4QWK6GesdSy6qt3DgbT2x46dT6WibbMjPa7KppfRbXcPi9jRRoDSQ7zhF77pEB8rnZ2_pjWFPHAL-wTi5NunmBTSXWizTl0xznTivfgPIKsnHGSatyi1VojweAAMzs6TtohXx3BBbO1H_cskldCsxgJe_G0NwvK-Mawr5VgjtwbcBtNoneTSpeEpWc-LLxCAYKJy7NQRAUrBcvoxQemGo1mFPbCDgxX5-tCZEzUyFFCptN62CisjYj4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=Jpkdph4gtkigefSOD9YEjisGAIgKyypYEF3yPXughwC1MoIWoEXcWPK9gauGo1UHEm7YH8f5fTviWiFS8JIJnQvRlQKpQ4QWK6GesdSy6qt3DgbT2x46dT6WibbMjPa7KppfRbXcPi9jRRoDSQ7zhF77pEB8rnZ2_pjWFPHAL-wTi5NunmBTSXWizTl0xznTivfgPIKsnHGSatyi1VojweAAMzs6TtohXx3BBbO1H_cskldCsxgJe_G0NwvK-Mawr5VgjtwbcBtNoneTSpeEpWc-LLxCAYKJy7NQRAUrBcvoxQemGo1mFPbCDgxX5-tCZEzUyFFCptN62CisjYj4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله تروریستی به یک پاسگاه پلیس در منامه بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/125421" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/125420" target="_blank">📅 01:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پرواز جنگنده‌‌ها تو جنوب عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/125419" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
🔴
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
🔴
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/125417" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی که در حال حاضر علیه ایران اعمال کرده‌ایم، باورنکردنی است و جهان پیش از این هرگز مشابه آن را به چشم ندیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125415" target="_blank">📅 00:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cVKNLTlAdr4HVinmbKL-BeGHA6yWEftSSYe30X6DA8RUeAOumseXG5mBITbgdPlGH2VvS3vqagKY6BjP_4mopbIo0cqNSldYYgLZOTOd3EhbUzaTvxOxAuW4mGj0quYrj7tKz-PeXiYh-CkscRgSQSPZQOXF3Jk82r2IeooLMIjMubjfVKpH91h95GxzzH6YPcbCm_9o1F80_93eEeklupaWPEJPGmPUVWeWFQT87r12KH6m1IYBmQlOj8sz1xXLy1-HGVVOOEuWbT9WUEPAmrAZl_q_LVXzyUie3_Sw496PKVC8pmVe2mlZm3x02vH6bR77USQXCpa9IldGd1T-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cVKNLTlAdr4HVinmbKL-BeGHA6yWEftSSYe30X6DA8RUeAOumseXG5mBITbgdPlGH2VvS3vqagKY6BjP_4mopbIo0cqNSldYYgLZOTOd3EhbUzaTvxOxAuW4mGj0quYrj7tKz-PeXiYh-CkscRgSQSPZQOXF3Jk82r2IeooLMIjMubjfVKpH91h95GxzzH6YPcbCm_9o1F80_93eEeklupaWPEJPGmPUVWeWFQT87r12KH6m1IYBmQlOj8sz1xXLy1-HGVVOOEuWbT9WUEPAmrAZl_q_LVXzyUie3_Sw496PKVC8pmVe2mlZm3x02vH6bR77USQXCpa9IldGd1T-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : این دیگه خیلی جنگ حساب نمی‌شه
- یه درگیری نظامیه، بیشتر شبیه تمرین می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/125414" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: ما به هر نحوی که شده، تا حد زیادی مسئله ایران را حل کرده‌ایم.
🔴
ما باید یک سلاح هسته‌ای بسیار توانمند را خنثی می‌کردیم و اجازه ظهور کشوری با حضور گسترده هسته‌ای را نمی‌دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125413" target="_blank">📅 00:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/صدای انفجار در جزیره خارگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/125412" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJj9Hbk0XlXLQYJTv7FYy2eWADvFveEz6iIw_fUyfr-78RmjEApZzQ8TSeI-rDPq57T_SOJZwEUVpW5_Qe25gEJb70o8qfhZq9nSlJhaAVKLGbn-sdrTJVtduNc5mEIVRwey5pywCFitLEAUKSMryF9sQ7SoIxjmMAQjO1yE0OOK3Sy8Arvw6-fMTAtIK0lerojW5pVWx96G5b7Z8i19cuSHkphEViZuCU76XBnvlI9KEE7cmfI3R0fm1trCNxREJT4P0r17eCD9FiRl1avKlsnm24yWQIqCVnmqXX9Q5MN9C0H7OZ7FVfBAXBYnzj6rdLu9lnH1M5eo__Cp-XW4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی جمعه 15 خرداد اعلام کرد که یک حادثه جدی در جریان عملیات مین‌روبی در نزدیکی نیروگاه اتمی زاپوریژیا در جنوب شرقی اوکراین رخ داده که بر اثر آن تعدادی از نیروهای ارتش روسیه زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/125411" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNddW4oVBVrroyJZKCXnusw0eRRHkye9wtNamWrz-puZQDIVAfPkcLnaOZn0pblcWxYMIuga5NoeJWnjplnBz8PEFx-iDs4dK9xJV5UCSge0ZeyfaeIBCsARPYHko-5_ujX8KXZCnfONw8-XixwRtJmywx8Ehrg9uMZ-Icus1scRk3aqddtS3l6Gcd_3Xe7eAdzVyYLnWhUeELpaBoB6THJLBq3TvOQ8ruPQCxT3JRdaACObjAaZaP8JB7D715SsYWX2Vt8b9aJWN9xfnwD1S_QXGqCU2ZPGrV9nMV5yy7rdRDNs3xZGZNKzsQkTrC1baMtU47TaPr352DAqBTMlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی طارمی: اگه تو جام جهانی گل بزنم، اونو به آقا مجتبی تقدیم میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125410" target="_blank">📅 00:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyNIPJDv4igPDVhMXn6DWJdvDPbL2CP3dSKGO5dk7vcNTK_LiFVB26SbHgUnW43AEO0Fts6PmlUZZM1Tf4BFkk9wS-jUeiM6-UjjdFxCOxPzhQBntxo8xHc-GbSipmpg3sqgmb5nrOmzx85-jo-9k_fwevZXPd3bbDYIHK4T3uiYnQqpzFfL1H-YoJ8JnKQTDecgKi59Hbd5lTmhTRhgIgfusWS0DjwporvbD3VM08JVAhBecpESezLu9hG-7rrj-_Ql6OcsqkEzieTEkonI1eizxhR-51lX8vn7oVYc181RwVP1V0lcAYIdKjQVky3dSfL93Ta_xy44MlXx18gliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jid4raCLcA4NQU-HsjNobjZ7gS9BSFBuuKAXZmwb7SFZXC4c0x93e4D_lao2C4QiCl6niUConJN4GfIlREIyBGC1QxnE4_ZGj-icOcr-LdlzH93JaxUVvegBPLDhmcVOR6qcpDfnjNPuajClTkQPrwUxI_vjxI0uEzcjDRil7oGpOYSlFOIi3xZyHXMpF9A1lj6ICNiFFGGdF0d0l3JIXJV1HdHz2z2n2i4pctimhVUCiacLheYYRkltrMhhY6O1G-bp2AnhSZ4pVPc8Xtco_QpLLcUF8d-VXJBfdt7F7xWEq0mdsR1cjmL5o1dRo3R6kio4ey_XAZG5a2QnUi3mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ1pE2feAPfoB7c9GPnAR44FmQ-5zL8K_04LYV-ALwmFZeEduWpCeeRaPfUmfVopr3X_w-mA0D0RMBHVB3DVfSlIW7H0xOERABu3OOe9uCVwDjAepZoTB94k2GZe9ARK5s5njOiMmi0ZCKJqiYycwnOWutRxRX_enSTiMarFWsdCobDZIxPgJUlVzF3N5_0PE9fLzINFUjS6nNiGHAOPQxrbIwq7RE7nThsVjR8jThnn3e0ja7DPyZ_E6GfM9KLGKfcYleA4wiCmR3B3WTN9W9ou4RorrXKCcRh3V5sqwlXFpdj07Emdj5ODJiiwmiYkJCk6g7u7jmv7J8qyk06PYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJuFPl9-opn8K1hpoX2fCBOMVnJ2xKEthJuQy5L18Oynmmec_Oxl-yl4_mFHOChz6SB3xBnS_f07yEhHiQwMcRasURESKbRGM8Usox5uXcl6cT6aWuPlORLOOa8SrrOt8pmxCLChRpbui1H_MwouOf0P9eVXQygeeVhZwsJWeEcbHfSLCcKxkjpfSppMJmO11PFvd1SZNVX5U8Gl5UwygsYmVfn4xYWcVhgMpKmBnE1V8ZQ6GET85Vfjo3lHyL1oIyLEgEOSc9aeVSV3FJfDsfwZIIyEsazjwoWERoq65tQ4polquimufStvH0eEjpj_vGc3CZaCFjhLLflknpqXqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صدف طاهریان، مدل معروفِ خارج‌نشین، امروز با یه استوری رسما اعلام کرد که به ایران برگشته
🔴
وی اعلام کرد منقلب شده و انقلابی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125406" target="_blank">📅 00:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a13944d664.mp4?token=MnGAT6WZm2Xr6IBV0JV_3aKak__gCo39fs3f8bL7ILQzuf6RvtdP5ot50A7lDUUe46VbS_K0XHPBdtv0puTqN5LKPnLEFcrepd2qcqgKl3xdV92udH8DxfWJYLHmNC06NA1DDEHw5IvSHHY-QfmrFdrcf2LJzdhWfwboSiZZGs0aODK6kwSE8a1ql52PI_Ryq40eeD4HTTxSJNBKparUQR_hy4gK7D4X4D_OWHaubPc4sQBW3ZFlLAvYa4vcPrfoWAxaz0nWc_7WzdG5LbqmoF2Dcr2kOg-V-F31oqxVog98ogKziqEtjoID62XeLt6PUQwZlFEFcmdyq3cNr55hcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a13944d664.mp4?token=MnGAT6WZm2Xr6IBV0JV_3aKak__gCo39fs3f8bL7ILQzuf6RvtdP5ot50A7lDUUe46VbS_K0XHPBdtv0puTqN5LKPnLEFcrepd2qcqgKl3xdV92udH8DxfWJYLHmNC06NA1DDEHw5IvSHHY-QfmrFdrcf2LJzdhWfwboSiZZGs0aODK6kwSE8a1ql52PI_Ryq40eeD4HTTxSJNBKparUQR_hy4gK7D4X4D_OWHaubPc4sQBW3ZFlLAvYa4vcPrfoWAxaz0nWc_7WzdG5LbqmoF2Dcr2kOg-V-F31oqxVog98ogKziqEtjoID62XeLt6PUQwZlFEFcmdyq3cNr55hcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه فیلمبرداری از جنگنده نسل 6 F-47 آمریکا، این جنگنده هیچ حرارتی از خود بروز نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/125405" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: در حال بررسی امکان ارسال سلاح به تایوان هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/125404" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMfLGg5CMBxKuRg-1xbWY3C-A1RuvaRJAjqjo7uUNQTrMhsgnIE6694glOGEYD9r93u-HV61HP8CNf-tEh7UDjB73QNOCseJCTPWGC0D3bXZUooUpZpQFu4iGSnGikKC8W2OcOhuJikWqXM3kCgLazNUyMq569VFkseGswXbYj9g-FZ5_OJaBT3knKlpR5rDSC7RJ0ThhPbq2Tkk48VE3xGDqInmF_koi1-mj0OoNsVjP8oKiL4hC6-SX1gl433e34O7Iu8sy_7Y8_2Qirn8MESGq-jmSnDSibTwbE3JXahRwIgmVGkysm1_k4sA1v_nDW85AGjj8REmlXjogTFnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس امروز از دست ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125403" target="_blank">📅 23:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: همواره در کنار آمریکا بوده‌ایم؛ برای همیشه از «ترامپ» به عنوان «مرد صلح» یاد خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/125402" target="_blank">📅 23:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / نایا : انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/125401" target="_blank">📅 23:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=mUgrh3I1nL1-_4f-oZX2kh3qGzlRhQJL0HhjKHIDaO9d2xKO1rdCZieO6GTpvVQwkgm8PeSNH7U9j6eZP9YQEYx4ZLHZG7arwTMKUUwtrD4WSy6FanH_oYb1Cc8QFv9EzJZBjrvJ1JWywyGQwfHGrr8Q1Pbqxq1wmhaLQTXoX6eiw6MGt7lQsoZcSdV6qNVIiCBfrT177JYQqAK-4AOi6vQncr9l_6oQjUWkSMTVD9lOOOZYZ3QkunlwfH6KA1ckSeDzVpj1igYSvzZe6LZwellK8QmvfbxQeiGzVc7lOG5ziT69FsjXQkRdVj42kIxnAs43Dx5hO86ye0HDy5IH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=mUgrh3I1nL1-_4f-oZX2kh3qGzlRhQJL0HhjKHIDaO9d2xKO1rdCZieO6GTpvVQwkgm8PeSNH7U9j6eZP9YQEYx4ZLHZG7arwTMKUUwtrD4WSy6FanH_oYb1Cc8QFv9EzJZBjrvJ1JWywyGQwfHGrr8Q1Pbqxq1wmhaLQTXoX6eiw6MGt7lQsoZcSdV6qNVIiCBfrT177JYQqAK-4AOi6vQncr9l_6oQjUWkSMTVD9lOOOZYZ3QkunlwfH6KA1ckSeDzVpj1igYSvzZe6LZwellK8QmvfbxQeiGzVc7lOG5ziT69FsjXQkRdVj42kIxnAs43Dx5hO86ye0HDy5IH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / نایا : انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/125400" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الحدث به نقل از یک مقام آمریکایی: دیدار ویتکاف و کوشنر با کارشناسان هسته‌ای نشانه آن است که مذاکرات در مرحله جدی قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/125399" target="_blank">📅 23:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
المیادین: در حمله به یک کشتی ماهیگیری ترکیه که در دریای سیاه در حال حرکت بود، یک ماهیگیر کشته و 4 تن دیگر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/125398" target="_blank">📅 23:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZLNGbuHIuMxSnGSAxLHHJm6HhVjlKVW_3vi9X0eWPMpKzzcQd9QKwcw6QOimraKJ22cbXSJk5K63OgeFs0KsRM48NpYCBDmE8jWjKMZBqjENrh9PmDq_c1LfML1vNBreGoyJNNo_Fxsm0vp5AEds70nYZFQD-bk1XVieI-ZGBzTFbxZMEPUXbF2_z6lRkh7Nbh8lVR4USqhvY8_zmDmKW4yfDOFTr0_m_qLMuGkwwqB9MAEjpqZtaa861yQWtf3VuxqYxi9nqJQ9DffX4hZaRXgvLqyP152jszKtcmqyKrNwWO0Pmmor75CLfhbg0PUZEaGgzQAeTWbUuM_Tt_gDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز دو نیرو حزب الله توسط ارتش اسرائیل (IDF) در درگیری تن به تن کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125397" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/125396" target="_blank">📅 23:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTplTrBTLUbYi48rT3gYn35-YYSojEJPbS3eejITW2WJKo93AIVpflswJ2KspiKEsASTnJ9MXXuAn8X9RSltk5g473_zRu75HXPvaEWYPudDHgSbs4aIeyHgFXjRVZ_VcaqRfVBoD4VxO4LXzDtuDRDqMXsuOmHk0WO5Zk565wO_Jgcgu3ZuUdMBB6fhnJn1IeUExZV28Py5LOVZAeORbeXeaAoM8Aw2Py-YdAwxxsQ9roAPwBAqs28crb8LHVUsmMim8k8JkPiWGjcXORA0fgq6fUexzvtuGxvooDIcJX2J6MaJKnU67klySaEms2Ov7SMKqIayzeSZjA-TmFCkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ایرفورس مگزین، مرکز فرماندهی آمریکا که بیش از ۲ دهه عملیات هوایی آمریکا در خاورمیانه را هدایت می‌کرد، در جریان جنگ آمریکا علیه ایران به شدت آسیب دید.
🔴
چند موشک ایران در هفته‌های آغازین جنگ به مرکز عملیات هوایی ترکیبی در پایگاه هوایی «العدید» در قطر اصابت کرد و آن را از کار انداخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125395" target="_blank">📅 22:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJkqIcGI_ZhZVaWg9x5mezWCeD0eXdsqBXcjjS8DPunLwRMI-YRrfn-f14dvMr6KneO0YBY8Xr_J7OXy10FdMLDBVixyj3i1pdT8GiJ2MvmPsyFS15xSFBB74N4xVzzSoPp9uRxbrk_vL1FgAnrXMuslGt2RN8eZygidEY9SK-beQebZ3h8JO5NKYtkmNllTGQwxM51fhv7bKQ9CvgU_VCf_jKz9DIVaHjzwEeA7xAGrPw5ID8i2KKgomhSa_6hW-x1IIXffPFZO4uaYVJ4klx-H7Ujw45Hz2ZSIV408pTZudQEkGHfcsYJFQW6P0zECzdROhR5_rExkUm1w3OW6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای راکتی در گالیلای علیا و نوار گالیلای شمالی، شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/125394" target="_blank">📅 22:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما دلیل این خدمات باکیفیت ماست برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot @tvpnshop_bot</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/125393" target="_blank">📅 22:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Yaat1jO-xrDbTwbYARdES4VnXBnYyseUyuZKf8dpv7t_1wwkeFPSeQuFRQAXC5cqe_Z26oZzxcUOJfZiL-cTC0GZrgjtgojC52qQVLFVZ-pl_jpglGbQKUlkh_z9anbAouSE3g7q4izcxQdL0TRXs8zYWMyUmN5gPkUuI8Gq34d9jjwOk3TNAXa6Ppcrjeiqh3lz0FUZ_5rw-QU3nWF6A2dL6LjCapIjUjI2dqPHsWh3RneMHqKA-Vv4yUpv0uO22bOHUjsdvhHJC1q_muSR9nltn2sd1j3L6pOJWYcUA5DIokjhedht5cYxW7uOFbTMV8ejc0jbURWnWt_e5vDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما
دلیل این خدمات باکیفیت ماست
برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/125392" target="_blank">📅 22:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84acc359c.mp4?token=Fjv664K_MDyLvA10DndjfKai0A2GBlQ-GgEeWWiTa8H8NVUeUuCn6Mc9D_DJQXOMEuvNrUw75_oZhrxaK8FsgYQCPlcQCEh-ffhg_X2hd8Q8CUwoSOJvFGX70TEUDX6_5lheXemmjz8OrDVS-Tf77kdW4M6vQ_41TdXDeuUoOZ2TBzID_PCluh_CIO_0rXuraXZbgIVQZJoOkoJvP2GSwDGEMNkMaeEhXLhjnykQWu7tc0p4ZWH0HyfdLfaCy5f8AVu-4Je5O-IN2h63N7LdaTNXOfs8twtGtPBiT3HWPdhWTJSk1tX4PF83lzFTjQnycZijh3jbK3Fw8DQ6sv_EY2ATYrqhjOs0wXW6oCpLfBXGGeF1Zz81s89etUtGxcoZ-2XFcnOpVFB9Kd7jRBCM-BomnuooSHum86WQflEy-fy9bIwMmSk0r46xah9AAV9liLsuZdb8TT9GB770T-z9HDJgTN0p4AGX_1fiEXUqr7yMaZAispRq7mjZ_XKxxC7tstoOGZVp2yK-mQJeii894Pgkn8bZqBK2uSRskFmdc9QD5nUYeD6nPnzl_pxOU7eTeiWUzwRznP2V2XUtFQlJGcSpi57aUHIK9PI2x5-42WjDlBg1JV9yJiCgXY8cNtEmwDl7ghSZr2xQ1IrUPc9ZByTETBCGFjAx5-ZZfZjPUR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84acc359c.mp4?token=Fjv664K_MDyLvA10DndjfKai0A2GBlQ-GgEeWWiTa8H8NVUeUuCn6Mc9D_DJQXOMEuvNrUw75_oZhrxaK8FsgYQCPlcQCEh-ffhg_X2hd8Q8CUwoSOJvFGX70TEUDX6_5lheXemmjz8OrDVS-Tf77kdW4M6vQ_41TdXDeuUoOZ2TBzID_PCluh_CIO_0rXuraXZbgIVQZJoOkoJvP2GSwDGEMNkMaeEhXLhjnykQWu7tc0p4ZWH0HyfdLfaCy5f8AVu-4Je5O-IN2h63N7LdaTNXOfs8twtGtPBiT3HWPdhWTJSk1tX4PF83lzFTjQnycZijh3jbK3Fw8DQ6sv_EY2ATYrqhjOs0wXW6oCpLfBXGGeF1Zz81s89etUtGxcoZ-2XFcnOpVFB9Kd7jRBCM-BomnuooSHum86WQflEy-fy9bIwMmSk0r46xah9AAV9liLsuZdb8TT9GB770T-z9HDJgTN0p4AGX_1fiEXUqr7yMaZAispRq7mjZ_XKxxC7tstoOGZVp2yK-mQJeii894Pgkn8bZqBK2uSRskFmdc9QD5nUYeD6nPnzl_pxOU7eTeiWUzwRznP2V2XUtFQlJGcSpi57aUHIK9PI2x5-42WjDlBg1JV9yJiCgXY8cNtEmwDl7ghSZr2xQ1IrUPc9ZByTETBCGFjAx5-ZZfZjPUR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عاشقانه ی وزیر انرژی عربستان سعودی در مورد مشارکت روسیه-عربستان: ما با هم می‌مانیم تا مرگ ما را از هم جدا کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125391" target="_blank">📅 22:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پروازهای فرودگاه رامسر پس از چهار ماه با پروازهای اصفهان به رامسر؛ در مسیر رفت و برگشت امروز انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/125390" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: مقدار زیادی نفت وارد کشور ما می‌شود، و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند.
🔴
و به همین دلیل است که قیمت نفت ۹۷ دلار در هر بشکه است، نه ۳۰۰ دلار در هر بشکه.
🔴
وقتی همهٔ آن مسائل مربوط به (ایران) حل شود، نباید طول بکشد — به هر صورت، این کار انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/125389" target="_blank">📅 22:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197efe458f.mp4?token=ed5NbJR6PPLHXNEfAqwfy9Q1Z3aGn9_WnOO3Ai3Iln9nmiq0e6HU8M3cGkcSSk8Fct9rho8eU7ZryWSThgFGygmx0Pr6va65J8Zjnz0Cv3tczcq8s6ccbapj5oYdRt16kzeGLKTMWraccLbVTy928dQKGl3XcRt55w271VlgOZD1QcwLF53B0USeN52Ncqgp8B3RTu8YiZQhYQtyniPnZ2X4GXrxCspG7kwTzJR9H2WKinh827IosI5CYCbdyvsuZLVlUGOKvjfTg5rVOy5j-T9xddH9VWEMLJ_e3_6IvrXS9JyWzqpIw_HSD09Xa4NoD6581Wlq6i40oo8eM0x6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197efe458f.mp4?token=ed5NbJR6PPLHXNEfAqwfy9Q1Z3aGn9_WnOO3Ai3Iln9nmiq0e6HU8M3cGkcSSk8Fct9rho8eU7ZryWSThgFGygmx0Pr6va65J8Zjnz0Cv3tczcq8s6ccbapj5oYdRt16kzeGLKTMWraccLbVTy928dQKGl3XcRt55w271VlgOZD1QcwLF53B0USeN52Ncqgp8B3RTu8YiZQhYQtyniPnZ2X4GXrxCspG7kwTzJR9H2WKinh827IosI5CYCbdyvsuZLVlUGOKvjfTg5rVOy5j-T9xddH9VWEMLJ_e3_6IvrXS9JyWzqpIw_HSD09Xa4NoD6581Wlq6i40oo8eM0x6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گشت جنگنده‌های ارتش، کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/125388" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSjavF8uvRtcDpM1sGC5a3rPcQyjTs3OZKMsaALulPUZrwCgYWwBqF2Erlf2460yTcpjal_ftOScOucgwuI7jkYU3T13tJwh2PVWT3mwTfBLkvxNcmhFaFMHzyEKJanI3MRJ0zaGwUxPnY33hzffB2n5jrVs7b91_nqqwF7u31Fc-8r7Zb8KlXXr7T012i_qOGE0h0kmoL2IZmrp2c6YDNDF23NmHX1fHc0EgTl_XIKDsGLqDVZHl80MiEXmYYrSAc83SoVkQkZKwU7qeY7d-QdhDMFENNQ-97OXwtFbi4wY73ZImy-nhOa_J6G2EMWvv_DC-D0uQv6FSrdCchfV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبراهام لینکن در فاصله ۲۸۰ کیلومتری از ایران مستقر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/125387" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA6iQ_S6Nl-xELiBkcykqggeLJ9i_T032QrJNyoUIEihpWrLHrMf7Or4D0Wb06pF-hHays_oeuTZ40ddiL6DJANPn0DnlsLMN8AtqIydJPo5Hx2tmuulxrFoNKxr_hK222ooL_qKeLEfj5SISE96meyzgv_GQRQHl2IIVitcdbv1-3jky84SNJDlaXZfyGGAV2m1dc6FloluvL6lneo3J3xEyyP6skVc4ye7zQQFPaWoXHfdQlKobZQQh2nlu8IJB7QbvsRgpAuSSHSHveBPzMu1RLhLIE26EXDBtgmpBQ6UL6cAACVLzLatDJcOEXuQe_S-sbIG_t8-yy8uvaEnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین باز هم ارزان شد
🔴
۵۹ هزار دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/125386" target="_blank">📅 22:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89a57631.mp4?token=ZKkzyzEHJM4-OiunWTRcg5HFfafMjZUVBOE5IJsk0JV9v5liJ149gcTJihTSyddx84NcsI06oC_r1fPB_IQc1240MqS3zOQ89MUDrT60g2lTTE0CMWxdOaH5OLhKG_ifeAr8QQdknCMKFXo5cU42676s3hfm-4kJ2MLH5wzDn58e7NPD3F2sT-K8_anqj4SMOPUi57tMF3AqKhj0QTAA_BkSGxsJQ-P7yJTm8BLmG1EzJXNR4sKmUZfK2yjQzYmInp_fhnnATM6-HGtHJOYQwi9KTSkn8bu1XqvyhZOQxN93ojfx__xuMm1slmn3pzbuMm_FCEsbRP7bixc608rSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89a57631.mp4?token=ZKkzyzEHJM4-OiunWTRcg5HFfafMjZUVBOE5IJsk0JV9v5liJ149gcTJihTSyddx84NcsI06oC_r1fPB_IQc1240MqS3zOQ89MUDrT60g2lTTE0CMWxdOaH5OLhKG_ifeAr8QQdknCMKFXo5cU42676s3hfm-4kJ2MLH5wzDn58e7NPD3F2sT-K8_anqj4SMOPUi57tMF3AqKhj0QTAA_BkSGxsJQ-P7yJTm8BLmG1EzJXNR4sKmUZfK2yjQzYmInp_fhnnATM6-HGtHJOYQwi9KTSkn8bu1XqvyhZOQxN93ojfx__xuMm1slmn3pzbuMm_FCEsbRP7bixc608rSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام ‎مجیدفرنیا پدر چهل‌وشش ساله، هجدهم دی‌ماه در چالوس با شلیک مستقیم حرام زاده های تروریست‌ جمهوری اسلامی به قتل رسید.
🤔
شرافت و وطن پرست یعنی مجیدفرنیا و بیشرف حرام زاده یعنی عرزشی جیره خور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/125385" target="_blank">📅 22:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ادعای اکسیوس: اگر مذاکرات به مرحله دوم پیش برود، تیم کارشناسانی که با ویتکاف و کوشنر ملاقات کردند، باید برنامه‌ای برای دفع مواد هسته‌ای ایران، چگونگی محدودتر کردن برنامه غنی‌سازی و روش‌های راستی‌آزمایی پایبندی ایران به توافق تدوین کنند
🔴
برخی از کارشناسان هسته‌ای که در این نشست حضور داشتند، پیش‌تر نیز با کوشنر و ویتکاف در عمان برای مذاکرات هسته‌ای با ایران قبل از جنگ همراه بودند.
🔴
یک مقام آمریکایی گفت: «این‌ها برترین کارشناسان هسته‌ای آمریکا هستند که می‌دانند چگونه مسائل فنی مربوط به توافق با ایران را انجام دهند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125384" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از مقامات آمریکایی: واشنگتن تیمی متشکل از ۱۰۰ متخصص هسته‌ای را برای شرکت در مذاکرات با ایران تشکیل داده است
🔴
برخی از کارشناسان هسته‌ای که ویتکوف و کوشنر با آنها دیدار کردند، در جلسه‌ای در سلطنت عمان شرکت کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/125383" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس: فرستاده های ترامپ روز پنجشنبه به آزمایشگاه ملی در اوک ریج، تنسی سفر کردند تا با تیمی از کارشناسان فنی مشورت کنند که ممکن است در مذاکرات هسته‌ای با ایران نقش داشته باشند
🔴
مذاکرات در مراحل پایانی خود است و مشخص نیست که آیا به توافق خواهیم رسید یا خیر.
🔴
ترامپ درخواست کرده بود که این توافق شامل یک مهلت ۶۰ روزه برای تکمیل کاهش غنی‌سازی اورانیوم باشد، در حالی که ایران ۹۰ روز می‌خواهد.
🔴
اختلاف بین واشنگتن و تهران بر سر میزان و زمان آزادسازی دارایی‌های مسدود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/125382" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
خبرنگار : با کمک اسکورت‌های دریایی چقدر نفت از تنگه رد شده؟
🔴
ترامپ : خیلی زیاد، نمی‌خوام عدد دقیق بگم
🔴
مقدار زیادی نفت داره وارد بازار جهانی میشه که خیلی‌ها اصلاً خبر ندارن
🔴
برای همین هم قیمتش ۹۷ دلاره، نه ۳۰۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125381" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=RHX2au1iTrSdGWkvRshZC7xx3MQrLM-rIWib42UhRXDjlK2OBouCtOkh1XJH9EemXQOtrq0FARncIbTdWBF6k5hdaboA0Y8y7Gn-LKvB9sD54TzRYEyaLJUA-qwxw58vA0_iHmivmBJwa2k0txy1q_PGodYt13_GSQThCUYSSABxrJ3Uqx6lC8DglpEQ10DR4WcPPEU_D2hWqDHbbOGGLdF5c7V8wPftlogvGkNf_XUDJd-OAYqYxfoPC23eIrhJOUJ6alIuO-azYmRNa1c0Xdy3prpXDM8TMzDSgmAQm7Zqg5XX4C8kxsK985Nqkck0FKDuVNrmWrhV4Bjh_-RvUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=RHX2au1iTrSdGWkvRshZC7xx3MQrLM-rIWib42UhRXDjlK2OBouCtOkh1XJH9EemXQOtrq0FARncIbTdWBF6k5hdaboA0Y8y7Gn-LKvB9sD54TzRYEyaLJUA-qwxw58vA0_iHmivmBJwa2k0txy1q_PGodYt13_GSQThCUYSSABxrJ3Uqx6lC8DglpEQ10DR4WcPPEU_D2hWqDHbbOGGLdF5c7V8wPftlogvGkNf_XUDJd-OAYqYxfoPC23eIrhJOUJ6alIuO-azYmRNa1c0Xdy3prpXDM8TMzDSgmAQm7Zqg5XX4C8kxsK985Nqkck0FKDuVNrmWrhV4Bjh_-RvUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
🔴
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/125380" target="_blank">📅 21:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATFbtNJ57VCDsKr1Ze9rxUyXru8dptHLsskoowkKOp9kc4M5vaEkcDMSiQDL0pBHGBMibcXOEZgg_duZBVZdJxYSRm0-1b-sQfR1qW8vSgYc7L4ikYu7lJzxF3WMQ3QShqOoFr7N6l9A7tz6ZVmCBFSybWz1x4v5ghC4oTDUaXa7Rihna68lznL9b37FXS7vNO7MKWyTf0NgfKNyQUyPIT_Ha6F7NDDF_2S7HXsqRegwnJLkCfv0ztRJ6d3Yb6FlEku_gATRp-L03TJGk0asRINKoaoWTrlxeZWWqaBjT4h3YhSzKfs-m_JK9i7FauXf0nFlrnRJxhEBAw-fymELYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125379" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ : کلی از نفت با کمک آمریکا از تنگه هرمز خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/125378" target="_blank">📅 21:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موضع رساندم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/125377" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ : ونزوئلا داره خیلی خوب پیش میره، ما داریم خیلی خوب با هم کار می‌کنیم
🔴
کشور خوشحاله،مردم آمریکا رو دوست دارن و الان شرکت‌های بزرگ نفتی دارن همین الان وارد اونجا می‌شن
🔴
و ما قراره میلیون‌ها بشکه نفت استخراج کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/125376" target="_blank">📅 21:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم
🔴
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/125375" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ادعای یک مقام آمریکایی به الجزیره گفت: ایران قصد داشت مذاکرات بین لبنان و اسرائیل را مختل کند تا بتواند اعتبار نجات اوضاع را از آن خود کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/125374" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
محسن رضایی در گفت‌وگو با سی‌ان‌ان: اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔴
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔴
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/125373" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301b042bd.mp4?token=UEG0yu96twdn771p9gsU5O2AtIBvxSDgQbVURpTia-yD96UNdJD3r0-jKH0yeojbzzDGjBUpQSiUvtDktOnobWLwVdQF56BFIewMAy7Fzn6idAzcmRNfmtFx9XJ81NH461e7DsGbkigx8zT_lNzfHrBr6aZF_DTGu1e5LEwNuwga3DrUzpmQKcI5Gtx3cvgVRm5hwdWKNqQ0i28NDR2_XqtRMbi-QuUqg3i_GaBCHwvKMXIYrm1amXXwS001tZP9LcFnfA3wqTMkG1y2RnMrwTXUw94NOFapsNX-QwkvgcCuYl4QfnacNvqg7LMCudp08Oj85jCXTomd1A8Hmn6epQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301b042bd.mp4?token=UEG0yu96twdn771p9gsU5O2AtIBvxSDgQbVURpTia-yD96UNdJD3r0-jKH0yeojbzzDGjBUpQSiUvtDktOnobWLwVdQF56BFIewMAy7Fzn6idAzcmRNfmtFx9XJ81NH461e7DsGbkigx8zT_lNzfHrBr6aZF_DTGu1e5LEwNuwga3DrUzpmQKcI5Gtx3cvgVRm5hwdWKNqQ0i28NDR2_XqtRMbi-QuUqg3i_GaBCHwvKMXIYrm1amXXwS001tZP9LcFnfA3wqTMkG1y2RnMrwTXUw94NOFapsNX-QwkvgcCuYl4QfnacNvqg7LMCudp08Oj85jCXTomd1A8Hmn6epQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ که بیرون کاخ سفید با خبرنگارا حرف نزد، قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/125372" target="_blank">📅 21:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmmuINUWYMzXwrdXQFS_2GxRZLMB7y5J-q-CkQ7tUmO0ULprsDVyTOxKSJPV_xf4B2Hk9lBkfxToy3Zmc5u3S046o5099VyQO5JNS3w6l5p-Xsyu0IJPI881TtrUp3CkzViIlL8LxyKpABwwdsfVz-y-yrw8AkMqq0dRQ9IF-OVLUuUsYBDtgYlAl4ZHJpJFPE2GcVT0cteK0q6l9jV4HYVuvhsqO05OzCUwsOY8bzh1-R8u5M4eB6_bg6onfsMABH8G1Pr018UjOMSduiTOVo4RuwNiRDyKFF6o2QqSdTgrtod4D6veHRwUCAa7GxP5xhMTU1FggsAhyKxy1_pT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olRKyg0xs3ioFhiuIExg-3kH2NkjH3jirKGIGPApX3hOz-tCupLqR6vCGEEV4ybjNF4Jamh5v8vB5zbN8rLVQ-kuXg4eDp1wMHFu0qXi95AwFegmLBib6pn7VwqqwEckVIf4DZAiaQoXNVmKR062zlKZxjMbWpb_qPkjRISUBITMGgrcFuk7F5CXgdho0pX75UP3GlQD1s1q9ktaYJb-aN0_ReBQFkV5oJUoAMNfXYG6OalFvWsg8SawqQ2QZeDSBOU9C2NBHWHeIY5QhI0zdk-hwHJkp8AZTHAY36XjZ_u_QABg2J_ltVwx8BbKs9tlt83fy7GeyE5b23FN-wYwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pybRVr0b0IBoAHONM5s7NwswMkrbEFXldbRtZ9BcKluZwaCb6DYvLGz3liJ9r3l_Q7eL7-7fhial0ZJL5A6mSPlDZW9Upd2wLZyqJLvYSQHeOQ6dErs9hAQ7Gac3J6TJtT8z-XVJVXgEIJpPIR06cBMnpKDrv9ejN0VN6rMz-GfqKExKMNa4pdou0vwy4_nW0iQSXXOHFlOVKKJdTUrIxmu2OCU_4wj4ukq4AZnXVjeWJkCkuUUU_bvSPWrulEbrvm-35VHzi_6Ped_VgrTE3aF_3QkZkvUNJqqe2KtzoXWHHB9ugcvMxNwkzo6_q8KR9qBHi5MAKKIKE87ouaZhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsaxLdadiXHs8sNUMkV6QUJ-yZt1MQM07cFMflHxZT3XknUn5qS6RhORztX2-c5JMfNhP_yRR8CYKdLpDsB2e7em7EkQQxTRjLnyzyRzofjmd151Zh5euPP2WxLL5gKCaCd9fO9RP3vJ6VeHl8CICJUoWUNpr-7dmMYRwKaB3Rk_k6BoqnhaCgHeUQVwFiH9dEgaANm2hmZKXaiU9yiQfDbcbNSyuZX4asXkaLTT4NHdgxhLMIbHm1ZT0toC_aBK9NxC_RSO1aW3j6yfhvCMkMPOjH5g379mfM8xW5D_1N_CRYpGLNinVGFinNlgW6heMzWhLh6TLqLJHs7teZWMOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرمانده سنتکام، دریاسالار برد کوپر، در سفر اخیر خود به خاورمیانه با رهبران ارشد بحرین، قطر، کویت و اردن دیدار کرد.
🔴
او همچنین با پرسنل مستقر آمریکا ملاقات کرد، اعضای برجسته خدمات را تقدیر نمود و نظارت بر انتقال رهبری در ارتش مرکزی آمریکا را بر عهده داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/125368" target="_blank">📅 21:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام کاخ سفید: ویزاهایی که به بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده اعطا شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125367" target="_blank">📅 20:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جروزالم پست: منابع اطلاعاتی اسرائیل، جی‌دی ونس، معاون رئیس‌جمهور آمریکا، را متهم می‌کنند که طرح موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً در اختیار اردوغان قرار داده است
🔴
اردوغان نیز سپس لابی کرده تا ترامپ آن را لغو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125366" target="_blank">📅 20:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
العربیه: بیت‌کوین برای اولین بار در دو سال گذشته به زیر ۶۰,۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/125365" target="_blank">📅 20:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZCcloOS35d8-yGETiYxT7c71L8VWyEK1vnFNKOr3zLVQa_eC5xJevF3lIbHRpMXQY_KPJbRpW4keoHGihkz8gFaFH9VtYn9SAH-QXoWKgCp_kx9asSRdUiJwnDBr7PLr1IouneYQlxdhF1MAzJno5iXhVr2JNx8_UdEmQgd5xBhv6skyeY13XFB1mbwpUIOvrvSxIORVMZhO8g2E7DsoIvbH5o6KCTnBO6k8qjDWl3wAnhXler3cRUPXCFVFmvsdv93G_kfTlpDE22SPrDZfco8A8oUbi907VX7Ys5n6kBkjJINyWDGhY7NiFfEeRJ_-fsly06iVdMkY5BmRPtoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQhJJE8EkVIxXSjLZjWRzckYS7hgApIuHQLJIdotOhLRija2l6lC7sPcoQ8Z4-ThbFikfDgzhL9uCAhxmQyF6fO30NRI76f6rh6I5TaPJh4kDT9mWuhhRZvGYzyc3Zj6MGeiUhxlQ_oFVZeh6DLnKsUbtBM52nBVkCODWlh9siFsv1SLNruHx9zyoICjABlRiZZGBfcHVZQwmJxC5_kyR1xxnT71mbi3Gn22ZjW353114PDqeDac5FMW3kGVEKGbMe63jK9MqTSGxKIqaL6nmoIOjTElt2NfmEN0EEF-zB6uRjlUBpVuvvkNTLCIYiyugkYT6h8WkVHdzvxV8K5pPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R21zpA7FKmCYscQLE1Jq-kz-0AdNUDqTsZi_omIUUq13PLQzkMySCUotNHkfEQp8sx_gHEpnG260Gw1S3hh3cE6o3AguBSnebyO1YwEeR9MkP8BviGsnQ5saUTUrpBuiOHmYUoAm2l4VWsSBYqoXBBwQWetuVH9-sjorX4Zt06GYwfEdEIImxCyOWP5c8t6WvQrJ5oZMiCrlALrEtZpQyjyqGbhc9lx0ZXwoWi_ci_8RgdzBlmAeQ54JXeVOz1PwQzvoUtr8BI9uiTA91S5C3UD4uDXJZ_pweK8GTWoSYbYtcAQhD1Xg7V08zXMkbeGyBAhi1v_lDmvlJYuiXwmK1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قراردادهای فاش‌شده نشان می‌دهد که روسیه موشک‌های هوا به هوا و هوا به زمین را به ایران تأمین می‌کند.
🔴
لیست موشک‌ها: ایکس-۳۸ هوا به زمین (هدایت لیزری) — ۱۲۰ واحد
آر-۷۳ هوا به هوا (برد کوتاه) — ۱۲۳ واحد
آر-۷۷ هوا به هوا (برد متوسط) — ۴۲ واحد
ایکس-۳۱ ضد رادار/ضد کشتی — ۴۲ واحد
🔴
تحویل‌ها به قراردادهای جنگنده سوخو-۳۵ ایران مرتبط است، با قطعاتی که تا سال ۲۰۲۷ سفارش داده شده‌اند.
🔴
ایران در اسناد روسیه با نام رمز «K10» ذکر شده است.
🔴
منبع: United24 اوکراین، با استناد به قراردادهای فاش‌شده روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/125362" target="_blank">📅 20:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ژنرال تامیر هیمن، از مقامات ارشد اطلاعات نظامی اسرائیل، در گفتگو با شبکه آمریکایی «بی‌پی‌اس» تایید کرد که ایالات متحده و اسرائیل قصد داشتند در جریان حملات مشترک اخیر خود به ایران، بار دیگر محمود احمدی‌نژاد، رئیس جمهوری پیشین ایران را به قدرت برسانند.
🔴
با این وجود به گفته او، مخالفت‌های رجب طیب اردوغان، رئیس جمهوری ترکیه باعث شده است که طرح اجرا نشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/125361" target="_blank">📅 20:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhI5-p6NN1FCH-PYN4NN-pQC3lskKSsIRBLFxMb9-WmRQ-yPA0E-oR-4292PQJ5SVAd3zV-aAkYFbGD02Xw4YWXqvuwNzbdn9WT-ItML4-B1qcnYh6Pz4sF5Dq3EelFkvFSFOM0i7gd5vr5SD5Tz-EJuRTR-6Rg7fZHRiwR57bPt0hbTk7kqnyvCrVz2wU0dFov_F9e7SlozcS7XvI7ijYeVW0FOMQM-C-1HW1_38FMTwmORRswG_hVfejPVVRGzrivZTgGitqbr7fduYAr9zvUoxqc5GTP0cHH28M_aTFYLFDvRjb_f9YCc1lVrvxdhX-hH5lFWI5VfBuRztLFVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر و بیانیه‌ای که از دیدار عراقچی و ویتکاف به نقل از کاخ سفید درحال پخش شدن است قدیمی بوده و برای سال گذشته و تاریخ ۱۳ آوریل ۲۰۲۵ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/125360" target="_blank">📅 20:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52ae477eb.mp4?token=HOcjyIFgsK-ACNXbvCVQFkfDpPtn5RCyshlmO96gk1Gj4HlW8aZIe0MRDWyFIDE1EILLZjW2w6AdKENbylAd_JDYQ75Ff4o_FGlPbhY8Bm2tKIM4OWhDU0RgPlfIrJV-StgWX1qDY76ZNzCVK1FNaPOgmXK4YDDXfr8mAdwzrsY9BZU2wvHKY1dCR6eV2ca7p8nULT5_aFBvFDYu7k1wx4216xrFWscAyIMqbC4Rs5Pp2dSumVx2_hfiRYFWFSzNdURlkhMYVzoQzBjTSImwhfBZkvSnYQyKnkRC2GidtiGdDAAnCbnqG5bBOIpjNeKCU-Z6a2XAcAh2EwzDAyzI_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52ae477eb.mp4?token=HOcjyIFgsK-ACNXbvCVQFkfDpPtn5RCyshlmO96gk1Gj4HlW8aZIe0MRDWyFIDE1EILLZjW2w6AdKENbylAd_JDYQ75Ff4o_FGlPbhY8Bm2tKIM4OWhDU0RgPlfIrJV-StgWX1qDY76ZNzCVK1FNaPOgmXK4YDDXfr8mAdwzrsY9BZU2wvHKY1dCR6eV2ca7p8nULT5_aFBvFDYu7k1wx4216xrFWscAyIMqbC4Rs5Pp2dSumVx2_hfiRYFWFSzNdURlkhMYVzoQzBjTSImwhfBZkvSnYQyKnkRC2GidtiGdDAAnCbnqG5bBOIpjNeKCU-Z6a2XAcAh2EwzDAyzI_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه پوتین به زلنسکی: همه دیدند که دونالد ترامپ چطور داشت زلنسکی را ادب می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/125359" target="_blank">📅 20:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پوتین: زلنسکی خواستار دیدار است اما من دلیلی برای آن نمی‌بینم؛ نمی‌دانم چرا اوکراین نمی‌خواهد ببیند دولت ترامپ ضامن مذاکرات صلح باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/125358" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پوتین : روسیه هم با آمریکا، هم با ایران و هم با اسرائیل در تماسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/125357" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پوتین : تصمیم ترامپ برای توقف حمله به ایران، تنها کار درست بود
🔴
روسیه هم امید داره این آتش‌بس به یه صلح بلندمدت برسه.
🔴
پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده از ایران همچنان روی میزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125356" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی کمیسیون فرهنگی مجلس:
اگر جلسات مجلس به‌صورت عادی برگزار می‌شد، وزیر ارتباطات را به دلیل وصل کردن اینترنت استیضاح می‌کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/125355" target="_blank">📅 20:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرگزاری «رویترز» اعلام کرد که ایالات متحده در آستانه نشست هفته آینده شورای حکام آژانس بین‌المللی انرژی اتمی، در حال آماده‌سازی پیش‌نویس قطعنامه‌ای برای محکوم کردن ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125354" target="_blank">📅 20:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdnadp_OZqQ5jrbAfctcWb2LMwDshmV3qEs5c5wLT1Z1mzKb4vitlRf1Lm9-sS9252sZUzLJGV_-KdDHu95SWP5D6U5pwAG6kDmk52EyN3MpvDME2um9bfPvI0Sh7BqNRd4KH7niE94VmtOdd1G3qaGT7r1XQRe-VczCaiiz-G8ZI5aYwhUhuR-H9CnjnNH1NHHUSR757lt3OGr_QMkXwLu3GJq5sLbKhXo0JCQ9A9ub0WWgBo-5lpzOhXU_wr-APJJpuUmCEnoAFdrsOrm8dpcEXSKQ_wcMs7gU4-X9dd7sE-zhaIL44ZmaB9wC6LFhfAB-Y2y1_qMgYX-HzKadMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طلا ۱۰۰ دلار ریخت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/125353" target="_blank">📅 20:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/125352" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مقام ایرانی به سی‌ان‌ان: آقا مجتبی خامنه‌ای با ترامپ دیدار نمی‌کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125351" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyUpHZpgSh8kRCpg8DhP8gggioZX42N4uZZf9beTPKULbxF9fbKObjIluPLeS0Mek6nsYaGU64P4FusV-h50ewKA_JfhL64uantsmR9kkD4rW7v67IgtPsvUeIAJ4OdVhdhxkdAG6fdQFCv_KVodCP_V7JEuzFoEhpBRq_UHJ-0MSITSbSJf2OAEmxzP6dkhaQy1IDyMVMycfAggidv8Hy6i23hFuOf2OYb2utSQa_f-CsOd7SB_k0H-8AavQTToC81j6ktOEAJA50XO3UdsrDLJzuHVpPlRf2VMnefPWQhrJtHKC5RVkrWD8zaQJSyRFcMzk7AO3EbRHG8vyIeGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش اختصاصی وال‌استریت ژورنال، رئیس‌جمهور ترامپ از بیل پولت خواسته است تا در راستای ایجاد تغییرات ساختاری و خانه‌تکانی در جامعه اطلاعاتی ایالات متحده، بخش بزرگی از کارمندان را برکنار کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/125350" target="_blank">📅 19:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
زلزله 4.8 ریشتری دقایقی پیش کازرون فارس را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125349" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: مقامات اسرائیلی معتقدند که تماس تلفنی اخیر بین ترامپ و نتانیاهو، که جزئیات آن به رسانه‌ها درز کرده است، یکی از داغ‌ترین تماس‌های بین دو طرف است و به ویژه با نزدیک شدن به انتخابات امسال، پیامدهای سیاسی در داخل اسرائیل را افزایش می‌دهد
🔴
یکی از این مقامات گفت که این افشاگری پیش از انتخابات به نتانیاهو آسیب سیاسی وارد کرده است
🔴
بر اساس نظرسنجی انجام شده توسط کانال ۱۲ اسرائیل، گادی آیزنکوت ، رئیس سابق ستاد کل ارتش ، برای اولین بار از نتانیاهو به عنوان مناسب‌ترین فرد برای ریاست دولت در آستانه انتخابات بعدی پیشی گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/125348" target="_blank">📅 19:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtFuTz5UuptBeGrf907RJrWWDXhUUoZtnx73Lj1rUTDoB9sMJLFEa_OmyMKgncT5Hmrt3B4OOGYZH6dXsYBghUfaBdbNrQ5QK_hl7erGVlz2VU9wJOWQXxzcX332zq1Ar2GdcGuD2NDz9D_HvFKmCzk2Q0KSDsTtjZcCwq7BoOAIfCqEdduDjZXrXPGG_abvaiOrB7nPYjpSpqdxS5ubFfGXw8OG8vXfwQ3jafwga9R7m55SN7-9pA_VekopxRwz46u9Jkj6mEA-o2hwMg7EFqlwjheoNx1r8zjq702zdmpvQhldkEDxH5y-ABbnaksP-yXRkxiWNFJP2C67ugDSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در شبکه اجتماعی ایکس: سرو می‌ماند ولی طوفان به پایان می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/125347" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: مذاکرات متوقف شده است، آمریکا اگر توافقی می‌خواهد باید فورا ۲۴میلیارد دلار دارایی های ایران را آزاد کند
🔴
اگر محاصره دریایی ادامه یابد ما [از طریق تاکتیک‌های ناشناخته] جنگ را به دریای سرخ، دریای مدیترانه و اقیانوس هند می‌کشانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125346" target="_blank">📅 19:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/ فارس: ایران مذاکرات و تبادل پیام با آمریکا از طریق واسطه‌ها را پس از حملات ادعایی آمریکا به کشتی‌های تجاری در جنوب ایران و ادامه عملیات نظامی اسرائیل در لبنان متوقف کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125345" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پوتین: اگر در انتخابات قبلی ایالات متحده تقلب نشده بود، ممکن بود درگیری در اوکراین رخ ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/125344" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: شبکه قاچاق LPG ایران به جنوب و شرق آسیا تحریم ش
د
🔴
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد شبکه‌ای از افراد، شرکت‌ها و کشتی‌ها که صدها میلیون دلار گاز مایع ایران را به صورت LPG عمان به جنوب و شرق آسیا قاچاق می‌کردند، تحت تحریم قرار گرفته‌اند.
طبق گزارش OFAC، این شبکه از شرکت‌های پوششی در امارات و چین، حساب‌های بانکی خارجی و ناوگان سایه ایران استفاده می‌کرد. همچنین شرکت صرافی ایرانی «مهر داد گرامیان نیک و شرکا» به دلیل جابجایی صدها میلیون دلار برای بانک‌های تحریم‌شده ایران در فهرست قرار گرفت.
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «اقتصاد ایران در بحران است و نیروی نظامی آن تضعیف شده. با برنامه Economic Fury، وزارت خزانه‌داری به محدود کردن ناوگان سایه، شبکه‌های بانکی سایه و دسترسی ایران به تجارت جهانی ادامه خواهد داد.»
🔴
شش تانکر LPG و چند شرکت پوششی نیز به فهرست تحریم‌ها اضافه شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125343" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRbGiX9P0SQKhGzZQXkGZNjDCxAu-Jxx6wRtn0m-nZQtZXeSV4642VZOqnCNLIWxUWRyWbydpVlf-HmWxUi_TMkKXi1FoyFo_ZlxezlCYIqD342hIvnQJcoZ7WhBWL7rtKzAc4bHzdkH4Jmo4g2V1IpLeXWLocG2uNmL08kfEJiAt5sBa50svNTC99PUiwrocy4rhh9ZShQ3nsmBLkL2NzW0NZ9SuBvupxoE-NXq0ZGq7XP7UoHZXualK0YMCzS8PInbAj1VZOp2Iqu7VauCYgGYT7YsQklEbpu0tTmYMZucYA52odyzdMsO3G0Aewj4s4Y5T7j7s6DiOjKHLrrXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
استخر بزرگ بازتاب‌دهنده، که بین یادبود لینکلن و بنای یادبود واشنگتن کشیده شده است، به تازگی با «نظرات بسیار مثبت» افتتاح شد اما، چه به عمد و چه نه، برخی می‌گویند، مانند واشنگتن پست، این یک «رنگ‌آمیزی» بوده است.
🔴
این یک رنگ‌آمیزی نبود. این ماده‌ای بسیار پیشرفته، با استحکام صنعتی بود که می‌تواند تا ۱۰۰ سال دوام بیاورد، و توسط افراد بسیار بااستعدادی اعمال شده است، بسیاری از آن‌ها از ایالت بزرگ اوکلاهما آمده‌اند، جایی که من در ۷۷ شهرستان از ۷۷ شهرستان، سه بار پیروز شدم، تنها رئیس‌جمهوری که تاکنون این کار را کرده است.
🔴
این ماده ضخیم، قوی، انعطاف‌پذیر است و رنگ طبیعی و زیبایی دارد، آبی تیره پرچم آمریکا!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/125342" target="_blank">📅 19:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1pYGhUohQWqQISQxxJTsRjcZb1tIiiobPCPbzD9iOtq5dCKVMU1Nlm5KFMhpN9L6NTZ4gjAG86xIFvetCx0z53IjRLMajR2eoeXJb-yZ9tKakD1-lYXs-R2Q_etH29kLVzOrNQvU5OxUUDjoLHibjxT5u-XOvb1R8j4m7qx2fNcgE65Wlr8joCZtmnnynotzIQ9KpF0P0OlN1oE9NjXCQiHR-Wwg0Ei-fyU-IOHeIv6MSH4YgWC55XB3CQE5dl3Fc1PPQPmVC0N-6OL_zxtHWTSOcmmDspYBH_hzsx5tO9ZcYK1e9yD2dT6pMzRhCIPwl_N9vgZxtNkDQyUaV0Y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته منابع آگاه، ایالات متحده، مکزیک و کانادا در آستانه از دست دادن موعد اول جولای برای تمدید توافق تجاری خود هستند؛ اتفاقی که راه را برای سال‌ها چانه‌زنی بر سر تعرفه‌های بخش خودروسازی و سایر صنایع باز خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/125341" target="_blank">📅 19:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ez9hAuy_iYvh48O4I9JWtmygqkoUIn7VzRL-bw-CWHuMXhWgfUclJd2cAB7LVLyQhXSk3JEGm8ppXeM4vCWuiGpOKj1qY0vrDTI5DsQU_GY93lCF0IBhT7kICVYgfFZWPgqHsd1u85dJ-JYcagKFZOZcEsjwAqH1uoIa8lzWuAXQqOqTZau_YHbJHtyO6ryhkX5neVgLZ3WMh0FHX5yCVM1v4lYjtlemZjfgvq_dQhspTYCxsI6Sy-ywIkFXFAoefTQqfz_4IkpZH-9siYxTOqC0GOiq6S2ok48t4IMqR_rUrZc6KQ-3US5XFvKAw9J8GTUlrcp_ufd-QtEmT9bZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نواف سلام نخست‌وزیر لبنان:
ما موفق شدیم به توافق آتش‌بس برسیم، اما متعجب شدیم که سپاه پاسداران ایران اولین مخالف آن بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125340" target="_blank">📅 19:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4-kCFerPLpvaEI9iw2D0T0-mLBfi38qgwlknt9RXPi75pLsMKUpcnD6ZhtJD3RAfadhnypyCclORl6IK0zx7PjlUk61EnBPmoGEovp237XfkQ9Qlor2wgMFwZ4FP4UXGMBoGfhm12XYVstTLihLMukEzMALiZLBHE1xSl8txUHjkwiwxRdP3I1VMsHKZCumcg8QnWWtvpsr4EVfkEBRz8q-XCL7e4KAmppyLzk32zggOnYHlI21D418h0C2jMTAKL_B7Zm3mEMleQcP65NK1lvkSE8ZqmebqLDyzJ0UiIZWJN9qwCOiJxkPvpfXWbZNWJShW8I2_m36ZxLt6kyq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهرنیا تحلیلگر سیاسی :
اگر میگویند که ساختار سیاسی ایران دچار ضعف نشده دروغ است
شما انچیزی که زمان خامنه ای وجود داشت را با الان مقایسه کنید
اینکه میگویند قالیباف درحال مذاکره است و رئیس است یا میگویند سران سپاه تصمیم گیر های اصلی هستند زمان خامنه ای اول وجود داشت ؟ خیر !
تمام این روند ها توسط ایالات متحده درحال گذر است
حتی اگر توافقی هم شود چیزی تغییر نمیکند زیرا شرایط ترامپ همان خلع سلاح است که رژیم میداند این یعنی سقوط سریعتر
اکنون ترامپ درحال فشار از طریق دیپلماسی هست تا باز هم دست خود را برای حمله تمام عیاری دیگر بازتر کند
بنیان های رژیم فعلی دچار ترک خوردگی های شدیدی شده
اینکه نمیخواهند یک شبه همه چیز عوض شود فقط بخاطر این است که تا حدامکان ایران کمتر ضربه بخورد  تا بتواند از او به عنوان یک شریک استراتژی بزرگ در هارتلند ریملند جدید استفاده کنند و چین را متوقف کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125339" target="_blank">📅 18:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
تحریم‌های جدید آمریکا علیه ایران
🔴
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125338" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_-Tf-xa-mJHDRiKfLSLUyHlhWttEoUv71e_tCYImK6Yylc8BIE9HiBcY2jDiqK5nqVNUKqVfjFDMs5vuuTSVGwra3HEwWwB3DRjJAlvX4zUAXKRT2kXwu7pQ6GVbrbge24mGl-PU22Th2yEzwHxeWaAcs53bWfqIo6h7-25zR8hBdaEEu6YruQb1BsF9ieu_2Nm7hzARtJCul0xOed-aelaz3Eh5ccoZ7dVFVYV9BldKv42E7wwyA_GzSRvqEO2GEn2pThukZbQrQx4YEAot0Vz4u8Nm1W5TZmXOgJpSoviWa7YepCjOl0mAbfVrJt40Io8MvD1hkCjG9iD_9tutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهر نیویورک در پنج ماه اول سال، کمترین تعداد قتل‌های گزارش شده را تاکنون ثبت کرده است، طبق داده‌های جدید پلیس نیویورک.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125337" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82db08198c.mp4?token=aw__0Eg7EjSVmV7sc-eQUUgK01UxNODsEFCcTM_jfiul3dq6Y4Nr1BRikdxWEwKvEDIrrji8K42RaYUmivIZ2gD8y1ZW0ivGUru5g_k6OPejzIspOeCjGeR1UfJwkPUvHyshKiCSTMtQcs-bABcHLk-IcL_gkFDQzgQMHs25USctFGCWKYh1ebb_ZW0L9LqGV3ODcRFkpPwQcq1GXDU8utkU4Tpyh06ZwUmpIDrMeXHX69-akW2LezsCwsdX-BjuWJjYqSOEZ56acVAeJOpvOEeZm3C2jd4uj0efDwk5gM6i0WkoiXRhA-hi7eXQIbPQbSv3X8N7wGifcoy96Vhdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82db08198c.mp4?token=aw__0Eg7EjSVmV7sc-eQUUgK01UxNODsEFCcTM_jfiul3dq6Y4Nr1BRikdxWEwKvEDIrrji8K42RaYUmivIZ2gD8y1ZW0ivGUru5g_k6OPejzIspOeCjGeR1UfJwkPUvHyshKiCSTMtQcs-bABcHLk-IcL_gkFDQzgQMHs25USctFGCWKYh1ebb_ZW0L9LqGV3ODcRFkpPwQcq1GXDU8utkU4Tpyh06ZwUmpIDrMeXHX69-akW2LezsCwsdX-BjuWJjYqSOEZ56acVAeJOpvOEeZm3C2jd4uj0efDwk5gM6i0WkoiXRhA-hi7eXQIbPQbSv3X8N7wGifcoy96Vhdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میدون انقلاب چند روز دیگه
#قیصر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125336" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhGjq8P2oHGJi7KoINFX4S5u2hFpnTIhi5M6qlFZOZ3QtrjLbWncbAHQdC0QFukzAxaZUKbfrFy7gXfAZKBwbfUY1Fb8q2DU68xr0LwSe0_OSFBziMq9iSDk6K5ciLCOfOvWtl_-dx9k9tuWtUQARPtSdu9Xn_YM958mc7ZWSXs-rKxe2OaYOVdXde-rTNdoUNY3JUJE94jbd40CNXB3G3HW_scsLAGoc8a7m3Vp0RkP33KmIecPKpwyocC97-kuzkl_q4dNXf-UoGwvUdPpYzUscBLZDKTXfBZijZ2PBPvYZ1ie4z3R-A4GDSBTcONZ7f2bb5mhHcGgRCQJFdATQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شجاع خلیل زاده: امیدواریم فدراسیون پاداش بهتری از دور قبل به بچه‌ها بده
🔴
پ.ن: سری قبل حواله خودرو ۱۰۰میلیاردی گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/125335" target="_blank">📅 18:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_ss9ter512WEIuR11TLEjSlB6swni0euucl98O4yJpk9iKRzh8fpb1hjuSa5FbAu3DK-xHm4gxlSi9j3jJCpz7AqIr5ZkPjQGfIX2tXifmY0Cr-0spuZIFFMkrMyw6WnwzUbCNWAFSVu7dssOQL3MQWfaPM1si4FgYrq1QGI4BF8yx2b6wcRAzS0ClMNVBHbneGmUEUymuteAscJzw6C_FFmd4kcNmnhjU7UkPwR18HvEgv9et2WUAWSIvGP26HE4kwDwFyffKWzhwiQMbw3PZJwB0Wn4DWrERLJGt0unMWpDq1QRjuvbXwWxHkyaDu1OLDrgK1WoS9G5FUI3kakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/125334" target="_blank">📅 18:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iayPR4DXfL9tXd3ULXXZEq3rBJKY3HtS6opreIINMiPzlmKseRknfjAQ_qTfenO1Y5QMQ396lwI__yzxLIojDigAKHXIIKqz1rSRUYitoiaW-TYLCu3OOivAzzz7c34ABOrOrWGmbuJsaPC7iFdqxBAWokzzO-1NvFfzGiaklL1m_Y19ZP5tWMCkx7VSILKji_K8CKy7SpIdrFBKtVQHGU_IbizWL5tvslVAup2bTupHMY-petENIM1xquB5WC5F1P23vzfsEFpG_hv9OHVUA-9XD80MjLI7GBphQXRIjfmElBDKlzLHIw32_gIHKuv82xPl6Rqekz0bbS7uMojaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین به 60هزار دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/125333" target="_blank">📅 18:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNJbvGjuKbHHuUAEDy6Y9xzFmbwB-yyNW30yUdoUsSC5rMViDmp_mB8HOdNv8rclN1SGY3Pob4WfahR0m35zFxrxOqiznJg0vtS1_V7k1G6PZK_3i6zhVl_jUWPV6dNFK4RyPtcdBYBq4R2P2UvVvcC0a4MYzyb-Et8-eynFboBb06m3-8LMhllXpiUGs3UkTR2BKKbRVJRJP1gDRIJLiEo_JzxBUChIcfQU_gvhNMyhyt1MzgAyCwxcBj2vVTMdTcfqdQqi446mbx17WAI1bdMy3azTG7pYAT7twWn_Lj_lGMy-GA_qxWaKyHk0TPSCW6p0MQ7CHpSc8N1CXzWfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلی مارکت:
صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسیده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/125332" target="_blank">📅 18:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125331" target="_blank">📅 18:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2C5GWEoNvN1gM9nR4LcW5SFe4BpoqCJfV_lI0nlOHyNy6hqwxPswXCNGysJJ_sDbuOjA5qybAYBIiqs5LrghR7pPDzRdPImnNMI3FRiyOI0SVwVp9FxDKyFasOapOX6WPQRfYEa4DnpPyx0KxhoJ2obBWC0dsNDAMhjOrnVUISs7CrTYvNrE2kIa_uvHScCvRfbyhSbfUEvZ4LskW2KCGmm32CYh6M3ArmzI0j2uIWReouHGrXtcxRduw2whmTJW9ow1yai76XzhtA4Jidy_59l9H_gmLlhKTpmb5g9PzOm1VPApCayj102iICqc_OSTP1kz1hzleDfZyvLspW2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125330" target="_blank">📅 18:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ردیابی دریایی کپلر : چهار نفتکش با پرچم ایران دوشنبه از تنگه هرمز عبور کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/125329" target="_blank">📅 17:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بازگشت به بازرسی از سایت های هسته ای ایران، شرطی غیرقابل چشم پوشی پیش از هر توافقی است
🔴
مدیرکل آژانس بین المللی انرژی اتمی به الجزیره: بیش از ۸ ماه است که نتوانسته ایم موجودی اعلام شده ایران از اورانیوم را راستی آزمایی کنیم.
🔴
فرض ما بر این است که مواد هسته ای ایران هنوز در همان مکانهایی هستند که در زمان آغاز حملات بودند و تهران نیز این موضوع را تأیید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125328" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گروسی: ایران و آمریکا نسبتاً به توافق نزدیک هستند؛ البته این را بیشتر در ارتباط با موضوع هسته‌ای می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/125327" target="_blank">📅 17:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6eefcf54.mp4?token=ZCENZPxDSMwPHTYbKAtMVvq_l1P-tQWMmgqom2PsDIZ8Hr_raGLL799GtpYfl_asXZRzC78B41FM9K8J_x2nNSIkfFRIIFVpN2n7XWvvzibalQX8TH5uosv4mYkInorV8511aF9R-H2_oV9s2YH5WLYIKiDhmAtR0bK2HeSe-xZbbXxzpa_SlU9zYYILTGr1dz113y1uKm8Hk-7LnpEbCufm7xNLMFZ4n8kjeee6Z7dIfRu_rQm1CLJPClaql_tqGuuQYr7lJ-NCg87AD4K58_3J_B1LA6Ccbq0gboewpX97riT3QdPbC9YS7CgTaUhyu2vKtnyDF9UI0nRQGmThTrhMXhk_quYn6VVPDJPLs30CMdZDW-lw69B8i1oiG5psK8tv1mpTTxusQ185UNpOn_ZIrKN72iU-b4gfyogzCkuugWJpfo21eJKr4d9MAYte9CUbz6BPfq2Bf69nGTNDiI3b5t2fbqvFZJ-C1BBSykDrchjjho4rX_bPtCKIBsJ0c3ZfCrNvGWItnEejbraG3geH0_gzTcF33Oh_Guyh_0qqVrsG6QzOTUXlFbp5kcFNMYgPwZpo28XSIBVWRU7EWz1kjE36-uUuJJgG5iMp0h62fcb4xkvIw-eVttEgAcV6n-qMK7UlrXoTErHy7B4NSUsB5jL9WLOONHpKJSR7-zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6eefcf54.mp4?token=ZCENZPxDSMwPHTYbKAtMVvq_l1P-tQWMmgqom2PsDIZ8Hr_raGLL799GtpYfl_asXZRzC78B41FM9K8J_x2nNSIkfFRIIFVpN2n7XWvvzibalQX8TH5uosv4mYkInorV8511aF9R-H2_oV9s2YH5WLYIKiDhmAtR0bK2HeSe-xZbbXxzpa_SlU9zYYILTGr1dz113y1uKm8Hk-7LnpEbCufm7xNLMFZ4n8kjeee6Z7dIfRu_rQm1CLJPClaql_tqGuuQYr7lJ-NCg87AD4K58_3J_B1LA6Ccbq0gboewpX97riT3QdPbC9YS7CgTaUhyu2vKtnyDF9UI0nRQGmThTrhMXhk_quYn6VVPDJPLs30CMdZDW-lw69B8i1oiG5psK8tv1mpTTxusQ185UNpOn_ZIrKN72iU-b4gfyogzCkuugWJpfo21eJKr4d9MAYte9CUbz6BPfq2Bf69nGTNDiI3b5t2fbqvFZJ-C1BBSykDrchjjho4rX_bPtCKIBsJ0c3ZfCrNvGWItnEejbraG3geH0_gzTcF33Oh_Guyh_0qqVrsG6QzOTUXlFbp5kcFNMYgPwZpo28XSIBVWRU7EWz1kjE36-uUuJJgG5iMp0h62fcb4xkvIw-eVttEgAcV6n-qMK7UlrXoTErHy7B4NSUsB5jL9WLOONHpKJSR7-zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان عون خطاب به ایران و حزب‌الله:
این کشور شما نیست؛ کشور ماست. این وظیفه ماست. دخالت در کشور ما وظیفه شما نیست.
🔴
مردم ما کشته می‌شوند؛ خانه‌های ما ویران می‌شوند. ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
🔴
حزب‌الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/125326" target="_blank">📅 17:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
جمالیان؛ نماینده مجلس:
کشت خشخاش در ایران خیلی زیاده شده. حتی جاهایی که قبلا برنج میکاشتن؛ به جاش دارن خشخاش میکارن. اینطوری همه تریاکی میشن. یکی یه کاری کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/125325" target="_blank">📅 17:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ZqvSI0rPJ8yqgAgXMve4aaJcaibm92Qdl_pU4S5dG_cC9a8ukpuC2YriVanzx0FesJao8YJf_SYobqiTamqGivIZzvKGFi35X4nnFPYnuCjzEufoUTuQrIVJPvqZdNN2jVZ4jevmLGSg3nGqKkguVpeXRc2dEpv1T29KrC1slV6NBm0QqU1JiIC6qlE9ok-SoS9MEtDEnsmToMMpXq1zPl9qDUQWn4CLTRL0Z6GXAq_Zm1CX9vqLhLUxwLg725boLNM4dgVAh1reTvRh5gxsdnpQ4T1XDcv6OS0bftfQom1XKUqcTezBCL1oX9ilGfMb9WPeovHMfaMhheaC0hUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وخامت حال میرحسین موسوی تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/125324" target="_blank">📅 17:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=S9TPP3rSR2soWWb3zXgwxmqga6rrvaPi5SFEY6HtVCpYCG41PtjUPzBCha7uPI5byQm_ym1e36InZYc4IjpsNzbuHsnCEPoSovB2scGO5ajBUAYzX4G7LNCA0nD3kwCNZiqnMWBJ0ZmVE6IexV1FzP5i3Mwj_AKxOjcDC8Fmo6ABEi4H0U82Xoh1HS9N-s9J0X0LEDgvtfmKwvdP75oYZOI1rNW_bP0pzWloJxuC_2vjYj5E4-N0wCnQGV_RNwa6Y8cpZgotr-1M73wYRmnwOg59U5YP6LWdwNC4JQ4zp718bMw36uThKGj0mUtaXNnkaM90Cd8EB9rrXUhw7ReMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=S9TPP3rSR2soWWb3zXgwxmqga6rrvaPi5SFEY6HtVCpYCG41PtjUPzBCha7uPI5byQm_ym1e36InZYc4IjpsNzbuHsnCEPoSovB2scGO5ajBUAYzX4G7LNCA0nD3kwCNZiqnMWBJ0ZmVE6IexV1FzP5i3Mwj_AKxOjcDC8Fmo6ABEi4H0U82Xoh1HS9N-s9J0X0LEDgvtfmKwvdP75oYZOI1rNW_bP0pzWloJxuC_2vjYj5E4-N0wCnQGV_RNwa6Y8cpZgotr-1M73wYRmnwOg59U5YP6LWdwNC4JQ4zp718bMw36uThKGj0mUtaXNnkaM90Cd8EB9rrXUhw7ReMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروند کفن‌پوش(گنده گوز) اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
🔴
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125323" target="_blank">📅 17:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhzby0e1f-x8hMd3WKtnqFApgLs0YRJyHnH7UjrDt-Dwnh080zPi3rGLen5_m4IIkq3jVMoP15l1M4dxvyAsgecUjSuKjplPig7GuKBdlIe9sVRSwkhvE82VCDe35jeKYhir0Jcw2fkQaE2gWsFHr-58r5Bsu6zBv3Smc9_jPq0jE9fau9ffz_fb9MXJfUuihmHlOg6oAII5J5pJdko9C_Gs9LZarUaHuC9v0G4ot8kPFgYylBWC45L0GLeH_f8RlTJe0TVIXOqa6_hzy3lX3jgcQZvnEOctkOkeImOXFVHc-ei_5MpiQN3bKZPbfiBK4xEGZBhlTXdt9SYoI1d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
خاک میخورم اما خاک نمیفروشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/125322" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipl12B0QLXrbkZlmZC8P4O6PXtR8aB3OffCgJSRmj-ujRJBdshcdnAZ1-nWe4XtHhSzRea9BaeGJqHN2ACbygJF14ikjm9Yl5p6ckZDMRmF_tZ1ENcinSVuETl9UeLtqejIbd-x8fVx_zCHkNsBKDUY4qsNwVig3yVg53yOi6IW7UWDd_xLo7KLiQso3gQ4JfX8Mkm4QKWuhk2CS6ie5Y-mZ77Kj7EmSfHRZnHon-5jat1IzMHNW0ALosc7kW5xtkZMzhwT-ub4dbxkLk7zXJ2Lc-MJVNnqaeoF08TFUaodYkJ98_42-bNGLTqvOkqXMn0790nqbWlirApv8Sh-HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125321" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJLLUTy2sin-c3J9LuAcr9GIzChUlbaezkH2p_z_N0BlWZ45o-c4h9QMTCB4KIw4EkXQPCcywBLk4yFGRYnwJktySC5jQDjhgaIXxw9I-6Ro7lMtkp7LaGoYiSNRCaLv-772SOSWH1IAH6Wf591V9nbet0ekb19tOdPbY4-wyxkkdPRpKPRApsrkexE37D4QqDxooU4OJAZTt4r4SeH8K_ZGOBnTtlO9TEPiYBXf0g3FVrUQcM7f7z6L0mKUzDz7AX2eZAv1GJKfk7UtudNIf70Fitq2oJ2mWByufNmlJff_bjCitpjLc2W6WBvemO1SxlucopWFzdHhd47fPWN72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی آمریکا حمله نکردند و به آنها شلیک نکردند.
🔴
انجام چنین کاری نقض آشکار آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره جاری علیه ایران را به طور کامل اجرا می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125320" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گروسی به الجزیره: ما بیش از ۸ ماه است که نتوانسته‌ایم ذخایر اورانیوم اعلام شده ایران را تأیید کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/125319" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
🔴
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
🔴
پیگیری‌های خبرنگار مهر نشان می دهد، این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است.
🔴
گزارش‌ها حاکی است این پروازها در ادامه فعالیت‌های معمول دفاعی و امنیتی صورت گرفته و جای نگرانی برای شهروندان وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/125318" target="_blank">📅 16:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94dfcf4fac.mp4?token=F0RCTXDrpOKYcNuBbKo1a7_uNrygWddsxujU7qjX0PD4qxnaGpbXNmg-75gQIZ30yiQCCnXB1NcnLjnvWLbTJpY04xT6MB848uTc-vpWLBq6HZ6quV7ypVFEOV6TVZWtRIgmysakIghcqlxnvvqnTRu1dFuBARDGJYLMhq-rVQsnUhhHL0YO2et310nNxkcUXndlS90L-HBqurREFHnoDPq_5daiFfBeKDWLIxRCqhr5SqOZWFNjocvzg4vEz2u4yssZi3t3wZkILfUVXlsVg0o0LoiEvGsccLyKQthZUUlpG0TQVqiPF7N3Dt_QMGi_Y_KclBjz5_KP7Vv77DrATg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94dfcf4fac.mp4?token=F0RCTXDrpOKYcNuBbKo1a7_uNrygWddsxujU7qjX0PD4qxnaGpbXNmg-75gQIZ30yiQCCnXB1NcnLjnvWLbTJpY04xT6MB848uTc-vpWLBq6HZ6quV7ypVFEOV6TVZWtRIgmysakIghcqlxnvvqnTRu1dFuBARDGJYLMhq-rVQsnUhhHL0YO2et310nNxkcUXndlS90L-HBqurREFHnoDPq_5daiFfBeKDWLIxRCqhr5SqOZWFNjocvzg4vEz2u4yssZi3t3wZkILfUVXlsVg0o0LoiEvGsccLyKQthZUUlpG0TQVqiPF7N3Dt_QMGi_Y_KclBjz5_KP7Vv77DrATg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز نیز به حملات هوایی در سراسر جنوب لبنان ادامه داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125315" target="_blank">📅 16:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7JlToKX7E1SjMKCsgjCguoF0XCkhS8itGSeq3CFqhExsbe-pa1qdAVoXpX1Ph47U-acD_Qf6qV5q-wnxxfp1P2-LV-7eDYYy1PQig7h_n7bUZDTMsUUyGj1AU7v6gsVWbSG8PGB51ER3IY0Yl29BPVYzK--G0djp_O63rd_b0c_mOOUQLR9PDTzby7Qw6RxBoFuyPaZbR54FciDHmDTvSS4qmAzh-HoR7DMJkyByi50i5gE4KiYWCuxxTiHi5m-k5A0b6xiwfBEr_OOYhub5en2iyiAfthzghrkN9agymZvIBBo6i3iggt50PbHM_v_MlhPExY7-f1_PVbuJeTMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لبنان :
- سپاه پاسداران ایران باید بفهمه که لبنان کشور ماست، نه کشور اونا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125314" target="_blank">📅 16:37 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
