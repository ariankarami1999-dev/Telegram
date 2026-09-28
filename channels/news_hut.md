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
<img src="https://cdn4.telesco.pe/file/TnPraY2FCYOGaAWYQVVPuKAdO4LnYxurvatDaHwk85tOlUhKTrNuV3qIxV6m0BQO1umIh6zrTOnNshR0Ugr2Z1wDtc3YB1L5nN3_c20m3WEt4wuIwCEC-hMKbOHrCDY1Y6kirqBI9ZsEF8NpeIe33mDfpnekPWmooPyvT2pEU5AaF3P1G9VIWVcmRT6R4pDf1Rjco0Gxkq2IwPOQC8tSkEWMotzPL55mlFVahU02yQs6QI-FA5HaeWBzpwNoFl-6vC4dPhjjgqmX8Ke6NJZ7LXy6vDdwc5icge0ZyN4NV3MCX5f6drbCKIDRljTAv9QFoFYsy3-1Bzf3se9ZQIlabA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr4lm-3N-H3kYlWMZyUTAzU3yKRvAsN5hzfE6sNk4n54DZ4VG-Yqpllfocr1uw8J4WYUD3NDm0F4pC1vvTQUyOJC49o05OsEL6_S5j0PDPCN5EY3EPvDhCmEtWkBvkQI3UWtrat0ZOY2UjbuFv3Q592kmiC0GWmsxvUNCo97pl9DeBGvn26Uzs42rwpyjF-KKIO7fpnCa_4Z-ZkZvKC48d46z-INN2QD7-22Gx-Ob0lyaklqfgjnkZbVdJblkFGR5nrngoJx5y4QL2vK4i0FQd8atN9_vT8E_lF_d63ZaqAuV66SzeoXKHDLxH0BX_9j4D8EBX03RSnj_OgMEOcpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwi15ds9jGud7dqj7PeA7U5HF4Nvsl9bvBcRyaHDvLwfbF3N5-h2L1HRzDZ_vQVN6ATeMx8pUOB-Yv1kZJLoJIa6dL7ct4ZTtmlTFbPTfuk0k8VtcK3hSdZfxMaHHFGQt1V4Yh9gLmw2YBuRm9bqQu-wl_IxTQ48QRr0usE9m17cWxGwW-C4axb_BVlVxNjsu-r-zYln0k3fiUSmAMFrrqwxRejU2a9bHAiKDy--aEAs9OGqZroc5uTnh0bMVQl1d0revh0eW230ig0a4tpkKMMQ8d1SQ8ZUziC8xCdJYLmq4DvdgIPGZKh7waLu5RuF7l_GQ48n79Jxds9JNFUECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfSCzyHogaR6TOj6w26aN50H3bAJu8w_d84JH_3_ISkD_FdhIjVQlm0m8BETCwxRiuWDN4T96Ym7wtbePtcn1U-Fv-wwWCJtSlkpQj7WvemjGN9uR5CeI8_0ChLHpnfCop1TKeNq6fDhBB5xK815-KccnDkkKaC3hfw8iOFWpast0-ud0cDUQI2QshUKuG-7M3_lBaTCNMk-ewB8Re2uVP0CNhUF2ulIHH2UXzgtX2ZBbQYb9H-Fz704-mCWGEgbOhJ-tfTJf2u4zudnm3-bZAY2-bJi_iK9FzCY83g2IkFrQQvcsTvXHrIno_6gKjNIbe5ZIUorqzgJjw9uVNB6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCpPN75qewa55-ilUPG0SjeRRFl_wBrBAtjrjURwbP68lVb69fDLm31AsZkyAA2C0YYQzWSFLFtGlHID-4I6v9zARkPvjP-yRBdKiBRCL5et6_X2XaagmE-B9TlkUNJMeaiIClgsZlX9EfDpZNM-TE0N8wT2oXN2A5VG-pSht0HgNv7YvCvgsLr4NZf_6PwmuqGrph53z1t24v3dIg1bkRRX5_ZTewbf2J4xaudSNYk1o0xvXIwIFQch21ASY9be2C0cGAwoF2KRbQtetgYth6UKD79B-2s50qQM32z9_ntqjGDkkqtPj7kulFlt_aMbo-CD6pQeu-rPYAtT7mRluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLtRuj0cIeja9XDfSCyXlU-SjFXymLafLVnZW71FudimNNW3LtObY1Tf0quW37Yvia5Ue7GHtuA7DEwVobURBIMx_dbb_AHQlovVNRrbPtMVDS1W2GLsYt1ihSS-rPpESyD4Pu5OorzQNIFLt2qyNoxPcaTPfIQ80K-NBDlTWxaipB4CYWJgLWyao6YvJzeYGzqCTqZfv9JCICyKo1u675xEsZZA5Mhft1ADMhGY4b6bXbjeVMIUVgOjx8PsX_T-gdBhc5nr_u6991tFykht7NC8Wu2RkvzP6l9CUvS-IGQNnqtGs_L3YE8wsQfScKPYDHpr67SXWt_qa_VPchd9-A.jpg" alt="photo" loading="lazy"/></div>
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=aa6M8DmddzuKp0mZxU5FO6UwlI38jIQt1aP6dH_dU4_1FrRIgNE88uKLpV3ybX7sM7D54fWkKDl_fZGeAV1128M_etQ61xMkXIG6Esc1CAsphJc7RoMbvLjkFusyx86bY_QG-6BOg4XUfALw4ICzWFD5o5GlTMzfoAxgOAVhpNAtDJHoZC0diihFnnrGjrKyDKtjFAu4ua6zdiBJe4vyoEWz-OOjediLPfbUHsv5K85sKbyLxkumuGSwgQEiWXq1itYbXjVtZPG43tAWWqhYQZh2hYnblnQMvF9iJqoVUASCPMsDRSGGSnAaHQpuMkecowLRcF026ufPibcPxDvYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=aa6M8DmddzuKp0mZxU5FO6UwlI38jIQt1aP6dH_dU4_1FrRIgNE88uKLpV3ybX7sM7D54fWkKDl_fZGeAV1128M_etQ61xMkXIG6Esc1CAsphJc7RoMbvLjkFusyx86bY_QG-6BOg4XUfALw4ICzWFD5o5GlTMzfoAxgOAVhpNAtDJHoZC0diihFnnrGjrKyDKtjFAu4ua6zdiBJe4vyoEWz-OOjediLPfbUHsv5K85sKbyLxkumuGSwgQEiWXq1itYbXjVtZPG43tAWWqhYQZh2hYnblnQMvF9iJqoVUASCPMsDRSGGSnAaHQpuMkecowLRcF026ufPibcPxDvYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=BwzGCajCsHrLqH7h7CqK98VWHWPCjkaWn5X8JzeeyVcCKhUBSPcOspSaIwG7dp_F0i1uCmMn1W0Gc1bTio52sn7CIj5gtbQnl6DVC0BBbhyE90hE5YpwCKXuGMy8HBTw7Bu0dZikvg4KCnFuFmLOuP26MU2U_QvpXrtPJrMZZiYF4YeGToIFimjytnquzm1pCwLsoLpAJy-Z_gC0_rZazzktaRxc4jFs71NQvLJ-827tAXSVSFVS6XYftl1vhWM6q7uivMJzTmkpk3-Rmwb_uCdrUdfLPNzNRRy6wxRtqbY83JFv_Ll1eQlPDAhpsu3IaB173w11ebAqiEBn_bHLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=BwzGCajCsHrLqH7h7CqK98VWHWPCjkaWn5X8JzeeyVcCKhUBSPcOspSaIwG7dp_F0i1uCmMn1W0Gc1bTio52sn7CIj5gtbQnl6DVC0BBbhyE90hE5YpwCKXuGMy8HBTw7Bu0dZikvg4KCnFuFmLOuP26MU2U_QvpXrtPJrMZZiYF4YeGToIFimjytnquzm1pCwLsoLpAJy-Z_gC0_rZazzktaRxc4jFs71NQvLJ-827tAXSVSFVS6XYftl1vhWM6q7uivMJzTmkpk3-Rmwb_uCdrUdfLPNzNRRy6wxRtqbY83JFv_Ll1eQlPDAhpsu3IaB173w11ebAqiEBn_bHLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=tTsGFbymMxdrqK28BK2R51wmXEb9VLXOduyC-YbOXMBBi5Oprvg_NMhyaHc__--xfnwOB3NuVo1ifsM3tmKELAWy_J1Kz5_03jK_aTeAcp6azJm8cKtXr7SF1xtRZCeXweqE9dYv-kzaZZt6vcpXKazCYcX6OvZjPGXa_-K7bz6tssq-h0ri8Whyh9qSKre2Qt38R62pBned-IshH02m0V-PETg7znS2dkwAz0UZEfKtfvHgMdrn-xGZ-nn7p1_BDrQsuhwxl2nC7Yis9cMhGkGvcr7Y_GLKvo5QinTXZKuENGbD1x_5aB24121BqFNU-o8_M9W9dyLB5UY1k5tnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=tTsGFbymMxdrqK28BK2R51wmXEb9VLXOduyC-YbOXMBBi5Oprvg_NMhyaHc__--xfnwOB3NuVo1ifsM3tmKELAWy_J1Kz5_03jK_aTeAcp6azJm8cKtXr7SF1xtRZCeXweqE9dYv-kzaZZt6vcpXKazCYcX6OvZjPGXa_-K7bz6tssq-h0ri8Whyh9qSKre2Qt38R62pBned-IshH02m0V-PETg7znS2dkwAz0UZEfKtfvHgMdrn-xGZ-nn7p1_BDrQsuhwxl2nC7Yis9cMhGkGvcr7Y_GLKvo5QinTXZKuENGbD1x_5aB24121BqFNU-o8_M9W9dyLB5UY1k5tnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=bdob6lNgVpkS_gvUaondydhCEk_vdL62_3wowfia7IXASz9bUwaLPSykxz43XhNfPnh8ltVuBraFMLd3QodUmceuGvlEE_r-ynTW5z4DYidcm2zETif4z-aLWTQE2v4-PgIRfoaslRjq1GBqkFutNPTweQKSVxz7d5Tm52a42OnZHisLgVTwNNPxuYBMRwUIZeK--voFz38NCoKrvsrAr5x7gF68BPoAbEhhVXz8P3KmDEK3m6VUu9fIZz79Ta3V-2nUDdAwT2vRHf3tEH5E3R0yNuCEm_cZIQt1YiDh3qWpMLo15ke4zz-iyjPjXm722_1c0kzlK72N2UmLuJDUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=bdob6lNgVpkS_gvUaondydhCEk_vdL62_3wowfia7IXASz9bUwaLPSykxz43XhNfPnh8ltVuBraFMLd3QodUmceuGvlEE_r-ynTW5z4DYidcm2zETif4z-aLWTQE2v4-PgIRfoaslRjq1GBqkFutNPTweQKSVxz7d5Tm52a42OnZHisLgVTwNNPxuYBMRwUIZeK--voFz38NCoKrvsrAr5x7gF68BPoAbEhhVXz8P3KmDEK3m6VUu9fIZz79Ta3V-2nUDdAwT2vRHf3tEH5E3R0yNuCEm_cZIQt1YiDh3qWpMLo15ke4zz-iyjPjXm722_1c0kzlK72N2UmLuJDUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=pZz09MH618Iv7q8e1HN-sf_JcfavjevP7yPSiX8Mepm0h1Asr5A799Sj5f1ld435MDtoXC6Bt_nseo1OKI0r0uX1LfloXigxfdnPVN4KADEAAzwv_u1_beRRddgo7RiU0DMI-mRERx2a2jBvBrv8eE-pUpgbxBciI3vUiPkbbqJd_62Lt0D1oYl7S9sRQHDhSUX1Rhz-lYWV09YDgIpMX6vyhI1c3rGBPhDLcAL87V8dIv14eYRsZh0d8XVyty4MGzfpGpUTAv0lg2CVAt6P6Z97P2oQjUq80v_DWKyt_oLWH1AFeEpprnLNHUYw9lkUuTAGmOq1obVtKJu3BlEpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=pZz09MH618Iv7q8e1HN-sf_JcfavjevP7yPSiX8Mepm0h1Asr5A799Sj5f1ld435MDtoXC6Bt_nseo1OKI0r0uX1LfloXigxfdnPVN4KADEAAzwv_u1_beRRddgo7RiU0DMI-mRERx2a2jBvBrv8eE-pUpgbxBciI3vUiPkbbqJd_62Lt0D1oYl7S9sRQHDhSUX1Rhz-lYWV09YDgIpMX6vyhI1c3rGBPhDLcAL87V8dIv14eYRsZh0d8XVyty4MGzfpGpUTAv0lg2CVAt6P6Z97P2oQjUq80v_DWKyt_oLWH1AFeEpprnLNHUYw9lkUuTAGmOq1obVtKJu3BlEpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZc8q1h4SA6enz9qk2VsvlNnRQN00zxAJe5INWcgRZKcwuNBnwdBmp8M9KWKRnTplipM_gfi3vG5RWxHor7DpqPeVNlpewWQQnzQlb1u1RNj600GvpfBGCA_6w-Lg7EVBAcclKsRvCkYzMwMvA6JmCs4I3cVJTHaDcV5CJ-kqCJJm6YHPll6lUr0tr8va4KzAzPkxLcNIZE5hByjjbtpUo1b6-zdu7ytIHUPW2Yy-XsscgHPW6Ar1V5GDwWQsTfgFRUCroPtpa7Uo37HwKshwTpve1DAiTXHA57RIGotahNx9ijLPmmQagep_bBjT8gair9UtllKm4HeVMWZ3tGqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=F-w3bdFHKVWTW1GeRI8g8HViviwccri6xkY-UdBUk5GnGmTiNnz5sYuFIZgwQmN3xMLHhfop4P5DQa3AWLxvj3WUqeNknEnTc1cuwasGOA3OJnchHjhLWB2GtUkm5RliqWRMMbO52gtfrJ0T1hGCpY_20rNoGKdLxVnD9Bb9lnaRlMQjD8x3z6K5lcGyJM9iy7tSHbbLYueZDmqi5Z86eLITubvy6JozLZYM5LSO9rWQ3jlq7gnS0DpPoE7BEg2NjaESB6KpLGXT7z6jM9qLjtJHr8r7ysCWt4bVBRx0y8taNFg50sfPmVTgaJH-glUDl7HXbW5pudxvuTLVkLoJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=F-w3bdFHKVWTW1GeRI8g8HViviwccri6xkY-UdBUk5GnGmTiNnz5sYuFIZgwQmN3xMLHhfop4P5DQa3AWLxvj3WUqeNknEnTc1cuwasGOA3OJnchHjhLWB2GtUkm5RliqWRMMbO52gtfrJ0T1hGCpY_20rNoGKdLxVnD9Bb9lnaRlMQjD8x3z6K5lcGyJM9iy7tSHbbLYueZDmqi5Z86eLITubvy6JozLZYM5LSO9rWQ3jlq7gnS0DpPoE7BEg2NjaESB6KpLGXT7z6jM9qLjtJHr8r7ysCWt4bVBRx0y8taNFg50sfPmVTgaJH-glUDl7HXbW5pudxvuTLVkLoJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIF-2__YaYV4ZYh_BV6J10XGiaBccARXiQCa7Xfb0Ig2GSByLyAkQ-k6cMtBtCN1T9EqFYQ8VW251vhn0aPMybyB2zkQTMRa9YYd4ILS7ERngmTjGxJkmvHjUS2NDA6gdHVTPFasBIr6mEkXxU-NPJkSs1mSzMtTwNF4WFeaWx76fVJhhfJy8E5TjGaboV3QMisWvWEc6JxRbCr40qnEtZwMM2eXaezlQibDMBBaZJrrHK1N2kBDYGm3_qCKGvrlbVK9qSDD5odiFPL3Q4LQLHRSKGA8sFG5lIhg5YSnOj7PEXzsM4m0v5LfjyOWWGPWqz_WOrqAH8dKdQHK00_VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4c5LX14hS-6YxFCSWOd2hIT9Qjosmb-gCaIZ7ILd_RoNG55F9B_AYZp-Giv6HBweJLz3t398RfPoVE3WMlOZkBgCeiOAG6YC02TeU-X3HI6wYQP02lT2exmgfHQWKLStQnOVAumDXaY8vwVc09Gw7WGmc-IkudWmOtjVYh9w6OpcArO1yVeONy6cqjTQJOudgtuYGLDwtoZxvfPcKM5yMsciRJIL8Rlse_TVlDzn0PFFySqdQywX8Yw5i8bCaUNmZ0A6TFRszp-9bV-vMTSE82ari5RUGzrnYzdTZlcbFsVCbm96PKDJ5GYO3kv1splWW__WcnhOYUElL6216T5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=BBvV3au43NV1Qn2Q7BHGN5QcX5QijkeNcuTiSGxHsVJ_v1MFjxwTskb0LuHPDtugZkNqd13AbeKHPnU7qYMmb5kbnBOtakzW9-_k4XLLuMp7AkaeFm6_4tdPbLDuPDPm3X5_S3FTRr9jVnWMewVWDHgY-GFcPNYTsbjOWpNLro-GtSPtXusda4U7dya-RmlliyavPpq7PaFeIsCED8Kbmx7cjKY8boTniO8Tvn7C8RfqcTTwy92gRUyDwsghk505AaU3XO1QDsA2Kw1Bk2arIm72lzRurO5v7wqKuuQSXD9Xo_ciz8UMjrJLtOBkrIxayWDSzizTeFqd0HO8SO3x4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=BBvV3au43NV1Qn2Q7BHGN5QcX5QijkeNcuTiSGxHsVJ_v1MFjxwTskb0LuHPDtugZkNqd13AbeKHPnU7qYMmb5kbnBOtakzW9-_k4XLLuMp7AkaeFm6_4tdPbLDuPDPm3X5_S3FTRr9jVnWMewVWDHgY-GFcPNYTsbjOWpNLro-GtSPtXusda4U7dya-RmlliyavPpq7PaFeIsCED8Kbmx7cjKY8boTniO8Tvn7C8RfqcTTwy92gRUyDwsghk505AaU3XO1QDsA2Kw1Bk2arIm72lzRurO5v7wqKuuQSXD9Xo_ciz8UMjrJLtOBkrIxayWDSzizTeFqd0HO8SO3x4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Uj9eBNSu0uOq_nCYdNwuPWAE72nJhwIwpJKDRRtrVgu3SQZOC1kZaMA4QJ6heRx8d_MZTSdVXL2nYPN-dMRNKk37DHJqsZy6perkSq061W87wW3JQfenhGIw8h6BRajlLkJbrhCUQGxnaU2rdXcvVWCMuLdXEOPZqj_OEj7LFGm5gnLlCSFFZZM6X63Ak0XQKb7tHsmJWkjUAG9iQq2l8jIHGHuULIdJPxRJNTCrMeBKV-UyaCX5EwDjegB3_f-24nLFYXpRN36rCmx0ryPoefvumxTesJUiN-FbpIzsB7MKYdtpptz4_GuZGNT00Usgqs-VuyONY9DBA7Ok3jzgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Uj9eBNSu0uOq_nCYdNwuPWAE72nJhwIwpJKDRRtrVgu3SQZOC1kZaMA4QJ6heRx8d_MZTSdVXL2nYPN-dMRNKk37DHJqsZy6perkSq061W87wW3JQfenhGIw8h6BRajlLkJbrhCUQGxnaU2rdXcvVWCMuLdXEOPZqj_OEj7LFGm5gnLlCSFFZZM6X63Ak0XQKb7tHsmJWkjUAG9iQq2l8jIHGHuULIdJPxRJNTCrMeBKV-UyaCX5EwDjegB3_f-24nLFYXpRN36rCmx0ryPoefvumxTesJUiN-FbpIzsB7MKYdtpptz4_GuZGNT00Usgqs-VuyONY9DBA7Ok3jzgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=B5nWKWLXjyNdC6UwvPS7zzlgYzl4ztC7xnaTTKP6IANNkGycfu95ij7gJ_GfNZvDS_tHnX3wNPtcQ8Jf_sPUijpF6Hb-Mhzxs0y26d4PAf8YpxuuY37DKyIz_q3bJZhhg-4FBiWaQKSxdsO8zNwZbZOQFl1YwkNaBVWoeVWglXb2sKavcHx38bA6Nc4ekZHwLpDT2bVm3eKQhJ1V4diGIvaaLYORfVp0aatLB8A_mRnxg69UHpbZtyIpTnCi06cUAPNQy0ukHIlDiZ31lm1BN2a8jxfIHUY4h_Q2cIzTT8ncfBx_Jr1C2OoB4kf3JPS6WJRTXMvB_LiqxEU3H5mKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=B5nWKWLXjyNdC6UwvPS7zzlgYzl4ztC7xnaTTKP6IANNkGycfu95ij7gJ_GfNZvDS_tHnX3wNPtcQ8Jf_sPUijpF6Hb-Mhzxs0y26d4PAf8YpxuuY37DKyIz_q3bJZhhg-4FBiWaQKSxdsO8zNwZbZOQFl1YwkNaBVWoeVWglXb2sKavcHx38bA6Nc4ekZHwLpDT2bVm3eKQhJ1V4diGIvaaLYORfVp0aatLB8A_mRnxg69UHpbZtyIpTnCi06cUAPNQy0ukHIlDiZ31lm1BN2a8jxfIHUY4h_Q2cIzTT8ncfBx_Jr1C2OoB4kf3JPS6WJRTXMvB_LiqxEU3H5mKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=kzXY39OqVCZDfpKe4lewnnGxTyytJlZ8TWdbUClP61GK4oqb9RxbwYaAXsvFT-ALoKQF2ICH7iGsEZEshj8FTCEKzrazFJ8AfxkgBfSQSXau4nuCfLb5P32v-zU9I_tGB9bXxr4x8ZNjifKiQyfxsmK6KCsnBMaIT8Inod6zuRUVz6Y3dPKurORkBN2uke5tlWt1VbDBUguVr_xYY4d5FUWKYypEe7R_-0hBoygMWjDjFfqA7i_qbtch4pF9Z5nO-AvWStww3jE8TY64JXm-XpWy3EXsFc02PFHMrNFtdDpyS4DdMFG1-4k_SzaOC_MF-3BBCIpotOnwXh9FFAnBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=kzXY39OqVCZDfpKe4lewnnGxTyytJlZ8TWdbUClP61GK4oqb9RxbwYaAXsvFT-ALoKQF2ICH7iGsEZEshj8FTCEKzrazFJ8AfxkgBfSQSXau4nuCfLb5P32v-zU9I_tGB9bXxr4x8ZNjifKiQyfxsmK6KCsnBMaIT8Inod6zuRUVz6Y3dPKurORkBN2uke5tlWt1VbDBUguVr_xYY4d5FUWKYypEe7R_-0hBoygMWjDjFfqA7i_qbtch4pF9Z5nO-AvWStww3jE8TY64JXm-XpWy3EXsFc02PFHMrNFtdDpyS4DdMFG1-4k_SzaOC_MF-3BBCIpotOnwXh9FFAnBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=bMhOP8CRgZjwDcnmo4brcwQmspt75l0BdfMxUHhBYKzjx6xGl9x_j4wYUiPxO36_1sPbSTOlb-krp5SkxPF3AF0t5dVrOOaZuSBPIESY-okB_Q_4EE5My18ZYAjnXy63xR_Pu0zjmAYzpRtd8KKpqt9N5E18uHQ0APbvgml_xCTkLQ3bnGsSOYGEAVeWm3Eu56Lt4mw59fxYqrd5nZrFZkFZQByfhCW_4MXTVrWnLQGEl5rMNbukaSHAWXBshgfm4oI31rEE_SY3xu0Id9fWpS-mPTZ3OhZ1MSwmD7Y9UPhGbfzjVoluRTGOod6EsURczd5l7xIXuhdIziUAzHaBZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=bMhOP8CRgZjwDcnmo4brcwQmspt75l0BdfMxUHhBYKzjx6xGl9x_j4wYUiPxO36_1sPbSTOlb-krp5SkxPF3AF0t5dVrOOaZuSBPIESY-okB_Q_4EE5My18ZYAjnXy63xR_Pu0zjmAYzpRtd8KKpqt9N5E18uHQ0APbvgml_xCTkLQ3bnGsSOYGEAVeWm3Eu56Lt4mw59fxYqrd5nZrFZkFZQByfhCW_4MXTVrWnLQGEl5rMNbukaSHAWXBshgfm4oI31rEE_SY3xu0Id9fWpS-mPTZ3OhZ1MSwmD7Y9UPhGbfzjVoluRTGOod6EsURczd5l7xIXuhdIziUAzHaBZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvoDVS_ymwbUXQhXOa6wz8AqpINX_3LwzNHxf6I_fWbjaupNzKhAfdEQGjl5KlT4T3slFiTZrtGbzNzrAYKpZNRkRt5NS-jJu6sSmvEnnkefOtpwt6BDHumasP3pkvLHwHTQv-wSn5yLPXyURlnIc9WaCFwsBsDhNG3bzLJDjcu-moBGljm12ItcF-51fKp3ILG8aQg_z6GizCyn-1_Xgb8obBIpT4ZRUetaZhh7DJUzXTPpwFO-DNN4WpnckWxP1mpMLrsigW-_83ZhGOKusuev7fECiXcASQ9ON4uLGrqokVpb3r7bC5AJsS3IuUE2XBd3B3EPZO0c1z5QJ6RqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=JN6M3OrCZrqj3Q15Kd5ULROuFe9qKtK5mewOitC5ODQDEvVMEvjJ89f--z_YEHAftTYUKHC-UgfhBnuzNambJpQwqhvH5CVjvj-WwQaz-AN0hiJz-CFwGetYcdSf1PxHBb-KlZoaQ1xoClH7PM__iq1VbkpqDGSSsYlp95X64fU-ywgwGC2b7UTkFsLjtTq1z1Y_SjanhOs-MenBnsjLb39YcEJyxihuJtoMr0qSGfo92Qz2L9HWN3gpkV4xdJGBwPDXoCyv7mQ4UmRMq8OHPEXPMgN2Ixjy6R9u0xFTMxvmW3rqUzKOFyv_Ty6F6qoWqXFSRbHaSrXcz46sbdai1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=JN6M3OrCZrqj3Q15Kd5ULROuFe9qKtK5mewOitC5ODQDEvVMEvjJ89f--z_YEHAftTYUKHC-UgfhBnuzNambJpQwqhvH5CVjvj-WwQaz-AN0hiJz-CFwGetYcdSf1PxHBb-KlZoaQ1xoClH7PM__iq1VbkpqDGSSsYlp95X64fU-ywgwGC2b7UTkFsLjtTq1z1Y_SjanhOs-MenBnsjLb39YcEJyxihuJtoMr0qSGfo92Qz2L9HWN3gpkV4xdJGBwPDXoCyv7mQ4UmRMq8OHPEXPMgN2Ixjy6R9u0xFTMxvmW3rqUzKOFyv_Ty6F6qoWqXFSRbHaSrXcz46sbdai1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=O1e4wqXBGTzWqNYp4yOeSrFzw2J-ZnnoDtcktF7wbUhRjzd66CJSFnsO9-J0LEr0Gw2HT5kmybCETy9GlPMtVbaTqMzwzE8RqwwVWGiuOTfGHN7EIMsUYKkORk9UTUzX7fp9hZdHf77W4XfKZmVE1L_jKKV-Mpx06mtrCNYLew-9RQ8cZOEleofF16eaYv9cJMqyAv8aHQvfcmPrPwKBRY9uDgZOlx5IazokW5kQbDyFLLMA3mCHAEuZ84SciovUFbDJk-BSTJOMlaN4a7Dn6mCOFG91OGq0BTuOts2Zk4RAUo2y8nB8fVcOo6pBLXeQVi01UT3rqp5dT87kWw1cKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=O1e4wqXBGTzWqNYp4yOeSrFzw2J-ZnnoDtcktF7wbUhRjzd66CJSFnsO9-J0LEr0Gw2HT5kmybCETy9GlPMtVbaTqMzwzE8RqwwVWGiuOTfGHN7EIMsUYKkORk9UTUzX7fp9hZdHf77W4XfKZmVE1L_jKKV-Mpx06mtrCNYLew-9RQ8cZOEleofF16eaYv9cJMqyAv8aHQvfcmPrPwKBRY9uDgZOlx5IazokW5kQbDyFLLMA3mCHAEuZ84SciovUFbDJk-BSTJOMlaN4a7Dn6mCOFG91OGq0BTuOts2Zk4RAUo2y8nB8fVcOo6pBLXeQVi01UT3rqp5dT87kWw1cKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=H6VRxjGIJ2xbXvBBnwygB38GVsKAdVFRq7yD-v64K49irYC5M5OT-v1IeHD19gD_5BIsYwom5kpjt-RjbbxkUTlzYD6RcBMcz6hyfuV0ArFBzmZ2R5XS8mW2lNVO5VWZ_UG9B3KFZScDnUBuHlsBoSEWIc8GDF-vAuRjtS2LuigDIKHO3f8mBkFMDIDIEeaqhWw32MzBlOK8X5gzipr8S1PBfNzDoFsrP6ShKGHWU8_Vw3BdjXvchKI5MafFRRyktPnnXJu5ZqZXrCB3gEkE4xNBBlcyeKbIZjMAiwkEp8QjL3DSunJK_mSFBTPTvE0D3PCjBOOMPEwpjkS1ziM2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=H6VRxjGIJ2xbXvBBnwygB38GVsKAdVFRq7yD-v64K49irYC5M5OT-v1IeHD19gD_5BIsYwom5kpjt-RjbbxkUTlzYD6RcBMcz6hyfuV0ArFBzmZ2R5XS8mW2lNVO5VWZ_UG9B3KFZScDnUBuHlsBoSEWIc8GDF-vAuRjtS2LuigDIKHO3f8mBkFMDIDIEeaqhWw32MzBlOK8X5gzipr8S1PBfNzDoFsrP6ShKGHWU8_Vw3BdjXvchKI5MafFRRyktPnnXJu5ZqZXrCB3gEkE4xNBBlcyeKbIZjMAiwkEp8QjL3DSunJK_mSFBTPTvE0D3PCjBOOMPEwpjkS1ziM2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=ZkLRaFCq7AkRb6BA0Grm3wCTS2RwrCtBsv_F6D4ktn4ua22MtDWyxBBAhzXvt5gZvL1wJZg5Vpr1bcZqCIjhrVVgGc1mb1vnN9FQRIFk51UHUUEFBdVl34UBR1hNW0gFCFeAYx3ArOo0VFe0JBdgklEW61R0LOqdDvFcx8XJRtsomURsoWAow05IbscbYbehbymYdMpu8zHi53gLdrlpH3d0g6rLJxy9Mu9yFZKmSIVpsu1rCzfWFJWZOKC2z1yrvGvY0_S2RuhPEm1Zi68Xz5cFVkQ05HQ-FCTVoNWoQz8gpUwTYUzzN-3Fse8k4wgszrmWXfL8Wbg5VZy7zHQc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=ZkLRaFCq7AkRb6BA0Grm3wCTS2RwrCtBsv_F6D4ktn4ua22MtDWyxBBAhzXvt5gZvL1wJZg5Vpr1bcZqCIjhrVVgGc1mb1vnN9FQRIFk51UHUUEFBdVl34UBR1hNW0gFCFeAYx3ArOo0VFe0JBdgklEW61R0LOqdDvFcx8XJRtsomURsoWAow05IbscbYbehbymYdMpu8zHi53gLdrlpH3d0g6rLJxy9Mu9yFZKmSIVpsu1rCzfWFJWZOKC2z1yrvGvY0_S2RuhPEm1Zi68Xz5cFVkQ05HQ-FCTVoNWoQz8gpUwTYUzzN-3Fse8k4wgszrmWXfL8Wbg5VZy7zHQc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5vwxGCO5IEkDKUoYsr0Kft8BxfiG17Ken07extL-XDLISRNweeqOsDy35Vnk-AmcHvhWx_sbN7Kk5JMNfe7oY3lhD2yxt0KEbOvVtiPjGCHtLov2qT3SIQq-PHlEloFF2VXFFqlQN31KBhCCSACY7z1SfM-i59w3W3VtetMnDw7be61NB4CGc_FG2E6gxlJ1J0v_tbx5H56ivYZOaXb5y7nX7RwNR-FGdv1G3gpymCq321Y6b5L6CjrLeL2-FoIPWDkwICmxz_bPZDWS5-8fctaYR9e7eTGu-Ht4veT8skAYSTXk2Qh2Mn9-pc7YrDLAdW2BcxogFxCcM7o4TXK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PQ2_zBPEl1L5bTKBrprpdwyVQlP-uoNG24GX9gIlFLnikYZvHYzDd1no3ypnoAwgrT33dvKLeiiNfpY88HMCsOlCHHsA83cIQAPCq0m8JoydawC0YduZ0OLqXrv2lqt7WGua7o9SCGmetA-sRVqCtAvAw6n-DMLWMvgmI0Fc34VrVgXGEyh3ogBQSik-wnhZneHNzQg05D8pszk9UdEsnP2Xc9F_IU9cSqOdqohtfSYLzb3hPSsMzUx4eNz6kBLL2BGjyBCDlm8bUwapdniH6zAUWGEV6FvTIKBAXKcTOUE-VixAXLzmnRLvvkEvYbzVjiHhx1_soRjuvSebiIJAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=gcQWswZ0W5gBUWk0qTtNiIbSz742kbTAMd2pYDOuH_pKd-Rs0vccW81XSdPtYItuyaB6sQwZPpZDnuf--wCbOMXf5-C6wv0ExwTKhsRLgxpOGVOQSJrwA-YUZSCv12t2vuFVVTD3E8TdDKBravMSiPAy2decyT8Xgodu5VauowLnNKNXXknP_5IyJAL9RjtrhrTH6v44jalz-_nmc-xEaCmmPcjaV4YTl2z32CtFgiQyzj4AEBmj3ni6X0JUV120YlV7aeotNEhzNC8GgqmwdE_gxPKqMZARLrQPSJ6SBh5qfVDVjgL_9OUH5Ilzr7o_uUGTXO9O-Xt8SNBqQKbKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=gcQWswZ0W5gBUWk0qTtNiIbSz742kbTAMd2pYDOuH_pKd-Rs0vccW81XSdPtYItuyaB6sQwZPpZDnuf--wCbOMXf5-C6wv0ExwTKhsRLgxpOGVOQSJrwA-YUZSCv12t2vuFVVTD3E8TdDKBravMSiPAy2decyT8Xgodu5VauowLnNKNXXknP_5IyJAL9RjtrhrTH6v44jalz-_nmc-xEaCmmPcjaV4YTl2z32CtFgiQyzj4AEBmj3ni6X0JUV120YlV7aeotNEhzNC8GgqmwdE_gxPKqMZARLrQPSJ6SBh5qfVDVjgL_9OUH5Ilzr7o_uUGTXO9O-Xt8SNBqQKbKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=aAqPUc452P3SpQkUlkJZt7xdYnMnZdCeX1x8TpeOJbmyJsIxmpWUo3mMP93AXizEjOh6w-gd_cukQk3uwxUWxgPn5rs6RRlx7t6_jGVm7MUACtZL4n9svRJE-M8jhLejJfWf02KqBaphpGFEBR9Rmv-bNFG06YSAZ_7pvgECJldB5tc4tc2eMkA0Ha4Wtpre0aAA4gMYwy8sOsemBaaWaal0K8KkhLodqZK4Tco8q1CEKP_GAgI3yAxea9mmzNYagMd4QNHUAhhHGW1Brr16_AO6joE6jUd10Q1S1AIhZI1cxWzoX73prXs-qYHjCeVetsrPIxL6uiHKMcsUnhtkUAVovf99Ri-tsTduDRQAJ_yALWp9zn3pKa41DIyrbr2sjrOnxp0AcCw03ZN_499fR1ubVsqfix7rvmbPTR5b_4Sy8LAYqzp0BswF04O8gz4syAIj6XGT8Ujti-kRbqyaU1X8XbZTuLrWnhyMKDw1OnLQTN44TD50TAGudtLOADBLRkuyo5B9JT1r1gsPwzPiudvdfcTd1oqAvIpfpR0W5Nfiz6dSw5X6O1erLfICN76uozCnYa7oMcPIKPuKSqrQrt7TIUruiBBvrD9ad739DsZfjRBE1IZCh055Pkv0e5unIf_kYwxr8xXiUxI2mWvi_T5IitBdGa2LdDtFnpOxRnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=aAqPUc452P3SpQkUlkJZt7xdYnMnZdCeX1x8TpeOJbmyJsIxmpWUo3mMP93AXizEjOh6w-gd_cukQk3uwxUWxgPn5rs6RRlx7t6_jGVm7MUACtZL4n9svRJE-M8jhLejJfWf02KqBaphpGFEBR9Rmv-bNFG06YSAZ_7pvgECJldB5tc4tc2eMkA0Ha4Wtpre0aAA4gMYwy8sOsemBaaWaal0K8KkhLodqZK4Tco8q1CEKP_GAgI3yAxea9mmzNYagMd4QNHUAhhHGW1Brr16_AO6joE6jUd10Q1S1AIhZI1cxWzoX73prXs-qYHjCeVetsrPIxL6uiHKMcsUnhtkUAVovf99Ri-tsTduDRQAJ_yALWp9zn3pKa41DIyrbr2sjrOnxp0AcCw03ZN_499fR1ubVsqfix7rvmbPTR5b_4Sy8LAYqzp0BswF04O8gz4syAIj6XGT8Ujti-kRbqyaU1X8XbZTuLrWnhyMKDw1OnLQTN44TD50TAGudtLOADBLRkuyo5B9JT1r1gsPwzPiudvdfcTd1oqAvIpfpR0W5Nfiz6dSw5X6O1erLfICN76uozCnYa7oMcPIKPuKSqrQrt7TIUruiBBvrD9ad739DsZfjRBE1IZCh055Pkv0e5unIf_kYwxr8xXiUxI2mWvi_T5IitBdGa2LdDtFnpOxRnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4iSv3SK51x5KSMVg-fQ8g8AMi_XBbNViAOg5xl2Zp1jgYtF3_h6xsT0z8C1UkIAwdwiP0wswWfJu2jKqXjfG5q_-lKDSBYTGWQN4J3JwB53yyN_Vgylhfsg7IAJCzjO0lQeVVNmpJmMQM0yTYMKTnKLmvKie2oYxb5PWwbRNcptEU9UGOYMOXi1ldAyLvLhz7Dh1gGPJka8i1JrPuMa8m96OdIdKpVKIZGT0faVN05b72R_q4ai52_JETAEhfmKPV2phHwP84WFtN7gQzS3GDzTKBvm0LvBpiHgYpJ5KMKnJZQrWX2sGhmXfM-TcNRAfthRTXAbL-7t5ncuIrq-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbAMdN5u2Qnqd6t4iNETQUTHlLoY2jCDgAkDxylyEyQ_EBCv9yRevo7FBxo0ZJ3Vm498wnlxJlr5IB3oBM5J2CzY5bdS6Un-qBOGdTyRcdDGbGY3pMCzRKNWiZu3OhjYq-MNVTMCpwllJWPBZwYiUCsFrEnjMmdkRHTqo2npZVcf4EG9aZZ5_odkZf2gyuBXDVQAF70O76e14SlKrgzhjUBsYYko11VNdnBOvG9m2ww7ub0XH5Oki4Nn13L3eQJXrDqhY2TrBJmZI8H2PMpJ6Rk3gU_K2MvwxREX8CZDRf14NkeZGpC8GmuIn1dnH2OXzz3yNbHZqCcE8e6qGIS0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAJ0visnVP9_w1QO0PElsedafA4Z0EKjlyBn0U0BTAGQ43abwhKuswSYiifREcrxVTf_9yjuXD32GHUw7AEt9kexwvF9QcoBVm-k8at6BoYLET7V4vry1cFYAUlY3i3cu6CWXyNtb2UgRW4lCvKifeZgP5OLPtRuXEEFtkzJpAmIGj1nx1bAn0SLr0sx9xQkIv-nRPUU5cFUo5GIz-dvQOzwxltGEf7vbiKf7hg-MRSuvDrS9RprNhviQLhAEF3f4Sn8Hu40eKRn7_cI73Uq2cLKNOROpNrmn7ImnVcAGulZ795Q_jE7y4rP77GdVQW24ZDIZrqP2YZwbHelwkqA8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=NCh7_dLmG7Jg39yuye7NvwaGTu374yTd580Fvh1o4MAicCsJI1ZtaTECDiX8Fp-y5KxwM8ZhA_vtZ-sMhP91V3nqH4Lw9s8lziHCr2GYTgMlCPD1C0N9R_tCM19pAaO4t8qR2_IvQslh293bR__0sCfagWn82ZqNZpGJMAz6sAy68CXEt7Z99CViWJBJAMvo0Tiwdmv1N3dHrofobCPuiKTU3cSSqTvTqj6TO648mfRDFJQIfkAYGrP-6cGo0lU1W8o7oVjElCXp6qr0iXpP59YTJeUVGjnjiVyx6P1zBzfNVP7H_7UoDx05cWvgxZKlquGRMVws2LAgSWE7B4RfzjWCdRM32NhoJOQ4OEnw3vklHBwCjpQXYgDaE-iHGtkGdhaDIqdqTx7NkWmojITx-v3TlCqDNVx0v1eFJZb96csq_5hjaPGBbLeHDSurnn1PEQGanJnhIexswpnqv-jxV6X_al1wviyBAmtxUFpDAWgY25cW8qDSI6CRFJ3RUuFFQlKOtYC5MntEh9DUCd1evmlU4v6KkJlTDonhCwtaLOIbAal_5XJVNEXBfCOhfguQoNR3HNU1hNZbE0F5Vd2z4D1Rg4u87dKTb6nnf0mK8KtfSZgwmhfvwYy9mLPCZrFTWg74gmrfPqbGqpXE1PcLVt0Sno9tEeFFSnBqB96E0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=NCh7_dLmG7Jg39yuye7NvwaGTu374yTd580Fvh1o4MAicCsJI1ZtaTECDiX8Fp-y5KxwM8ZhA_vtZ-sMhP91V3nqH4Lw9s8lziHCr2GYTgMlCPD1C0N9R_tCM19pAaO4t8qR2_IvQslh293bR__0sCfagWn82ZqNZpGJMAz6sAy68CXEt7Z99CViWJBJAMvo0Tiwdmv1N3dHrofobCPuiKTU3cSSqTvTqj6TO648mfRDFJQIfkAYGrP-6cGo0lU1W8o7oVjElCXp6qr0iXpP59YTJeUVGjnjiVyx6P1zBzfNVP7H_7UoDx05cWvgxZKlquGRMVws2LAgSWE7B4RfzjWCdRM32NhoJOQ4OEnw3vklHBwCjpQXYgDaE-iHGtkGdhaDIqdqTx7NkWmojITx-v3TlCqDNVx0v1eFJZb96csq_5hjaPGBbLeHDSurnn1PEQGanJnhIexswpnqv-jxV6X_al1wviyBAmtxUFpDAWgY25cW8qDSI6CRFJ3RUuFFQlKOtYC5MntEh9DUCd1evmlU4v6KkJlTDonhCwtaLOIbAal_5XJVNEXBfCOhfguQoNR3HNU1hNZbE0F5Vd2z4D1Rg4u87dKTb6nnf0mK8KtfSZgwmhfvwYy9mLPCZrFTWg74gmrfPqbGqpXE1PcLVt0Sno9tEeFFSnBqB96E0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nDFvyqj7GXqRboZexvS_Ctx-TbG2ARfonC5h4HvC9ktmjjEtFMmNqkTozUXSGTgdG0GgI1EO7XXDvR24FjHrIzfDqtpvV43iLuCIcFGgVXBuWLy0qmwyISrPAUP0yZPy9KPKmSXlWB5HpRzfLYYCyVHGLax2QD8BPcECqpa_EG8zT7eb5qRy-EnKJ3OaPU4AoIw8-Jj_y-AhmZaS4dLmAOKCUbH1QrUcmEmK4vnc8QbRibs7xcZLdhAzZum0jPZaiNMVvQNwxPY70Uhbtnj8LQ_OJ5n5b3BemkFGuYkNUUh8DJ5VAjXmmuFHeswOwMjQNZkmG_e065lrgT1G8mdFGak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nDFvyqj7GXqRboZexvS_Ctx-TbG2ARfonC5h4HvC9ktmjjEtFMmNqkTozUXSGTgdG0GgI1EO7XXDvR24FjHrIzfDqtpvV43iLuCIcFGgVXBuWLy0qmwyISrPAUP0yZPy9KPKmSXlWB5HpRzfLYYCyVHGLax2QD8BPcECqpa_EG8zT7eb5qRy-EnKJ3OaPU4AoIw8-Jj_y-AhmZaS4dLmAOKCUbH1QrUcmEmK4vnc8QbRibs7xcZLdhAzZum0jPZaiNMVvQNwxPY70Uhbtnj8LQ_OJ5n5b3BemkFGuYkNUUh8DJ5VAjXmmuFHeswOwMjQNZkmG_e065lrgT1G8mdFGak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=dIfJNTpB8MPKjiAltjl1nRWvSl8FjSK9QgDv6DGSsnI6qR5v_rfFBpHkwbBby7MkgZq9aBOdAaJGduK9xNAovNLTLm8c05V9-ODKag1rqAI70venaDWKrBH_BJjY133XKluUCDmUwiP7g8Elj4KsOWVTkXSPQ71LR1f1d0ouqUnNhxmG6StgCgDQGxFGLafn6-RpC2qgPuMBq8TtXOVY8IuEjwQrhRhq0JD0zvDHb1RZDjKWo1GkWksqyo6WFd3yLzOOGFh-mle2WofO07DKmcY7OhHfQa7_vA2RklFXWVY2L309ClnH7ugo_Kz12efhAOZKk5dTr3aeq4s6eY19roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=dIfJNTpB8MPKjiAltjl1nRWvSl8FjSK9QgDv6DGSsnI6qR5v_rfFBpHkwbBby7MkgZq9aBOdAaJGduK9xNAovNLTLm8c05V9-ODKag1rqAI70venaDWKrBH_BJjY133XKluUCDmUwiP7g8Elj4KsOWVTkXSPQ71LR1f1d0ouqUnNhxmG6StgCgDQGxFGLafn6-RpC2qgPuMBq8TtXOVY8IuEjwQrhRhq0JD0zvDHb1RZDjKWo1GkWksqyo6WFd3yLzOOGFh-mle2WofO07DKmcY7OhHfQa7_vA2RklFXWVY2L309ClnH7ugo_Kz12efhAOZKk5dTr3aeq4s6eY19roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loYIJHAML3ppSmn072BIs80mqRq3BtHuBOeiovo77eHH5yoGROm5FgbJ8bfMeT1Lwn9mMOWUGcseZcAC9YaEtyOuVgQXi_yOmxnMEqwfTeW7maJnuTJHe-sOQLftAgv-yn3Tu9PEZn7rxil4upSfz7RX5GhRaGCedZB_0LjpvXs7On3nGJaAOkFLbkqrkFbf_U9XyDHid9-_5tFrMB_-aM53LGDbertiHBbpl8m7boIIlVYqseeKEY5pYC-NpUFY91BB1uyPzoqvATzTTl1ZxSL514PkQ3pzg7OdeonFwIoaddUzcB27vu3mGmhpM95KyYDpoPSbm64Zq01dXoElaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=AAhrPMy8QbS5GPJrKG_Uw4zZc5O-FFybXHUGqByhsJBg4BU2n0BjPKTjSwzBcOywzbIRJP-ZK4ZZEMIQvdEB8QiGFpkdAYo7RJF5EBDteJcZ5S5eJrLmeIm98ZAEgadsZ8juGR09wkNAy79_iODpnn3xcZdOHrvpptWVNXnchBRzlykgQL1ksmbpCEZCqz2WxiqZI7_xblinOoRlXHJA0u2dIHMCo-4nqMxe0t3bWF9rjhmB2slMr2LKwllLQDJTuv46wwWmncfNtEYLtAx8msXsXGb9kkdD1o4LhuJ8t4-LBflE9t7cKK7UH9xh90ATtAQsZd3odDXoimR6tbW9cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=AAhrPMy8QbS5GPJrKG_Uw4zZc5O-FFybXHUGqByhsJBg4BU2n0BjPKTjSwzBcOywzbIRJP-ZK4ZZEMIQvdEB8QiGFpkdAYo7RJF5EBDteJcZ5S5eJrLmeIm98ZAEgadsZ8juGR09wkNAy79_iODpnn3xcZdOHrvpptWVNXnchBRzlykgQL1ksmbpCEZCqz2WxiqZI7_xblinOoRlXHJA0u2dIHMCo-4nqMxe0t3bWF9rjhmB2slMr2LKwllLQDJTuv46wwWmncfNtEYLtAx8msXsXGb9kkdD1o4LhuJ8t4-LBflE9t7cKK7UH9xh90ATtAQsZd3odDXoimR6tbW9cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpiuhQxwXocyOGo2sM6ALcFVvHtDhjqe1lTtb-xsyVL3TAufZLyqYUgP4uAIlVAR_XCCkNvvinLkisidZslfyZ5nDItBwhQRpIIlk_tTcL0dyQam3JgOh_bFtsOLAgEOpDEKrt_2x3t8jQOjrdu6C6EgVYnUN3i24-A4nfMYGgprPdXPVKQ6slpct011QdPEgmQa75gM8mXSA7ONDz2yudkA8srTyjBqvVjwPIXlkq6Xa_bYnxltFxZSLL3OZKW9kULSTFUfKKYLUSjoIGwBHLGpcQLvbIpdg-E76MGDN9o5mXqcT3dNh7ndpdCv5NtbzPj_RGEjrBZe3eLGZX_h1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72367" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=Y1lzpCUoZYc3Xvy-cKEe0h77PGBTesvO1L0CPBCARymryIZQo-iVVsI4ekNb1X_5_qesdb_sCp5jtnedjDby0HIGS7iIEd5qkK0cC9ZL5zU-By39ZrCgepLayIivIV6jSV2oZPJbMPLBZOUXEtMg3k4X4WxZhXPE8aVMfuEoqXCc9eBCfyAJD36LsH3BkE2VGQgMdf1xZ_qFlGZbd2O6ZpbPoGjWoxzpZf0QklHB6yiW6Sua94EYhP7wVmX-g4u6BBQjI3xCluV0mAjpOeva21MavmUvtGHus-fsOpmuXCU_OjDD0O7WaaMI0UIK6DhpfT6l6_wmQk1jumlDyItFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=Y1lzpCUoZYc3Xvy-cKEe0h77PGBTesvO1L0CPBCARymryIZQo-iVVsI4ekNb1X_5_qesdb_sCp5jtnedjDby0HIGS7iIEd5qkK0cC9ZL5zU-By39ZrCgepLayIivIV6jSV2oZPJbMPLBZOUXEtMg3k4X4WxZhXPE8aVMfuEoqXCc9eBCfyAJD36LsH3BkE2VGQgMdf1xZ_qFlGZbd2O6ZpbPoGjWoxzpZf0QklHB6yiW6Sua94EYhP7wVmX-g4u6BBQjI3xCluV0mAjpOeva21MavmUvtGHus-fsOpmuXCU_OjDD0O7WaaMI0UIK6DhpfT6l6_wmQk1jumlDyItFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به‌محض اینکه ایران تسلیم شود و جنگ پایان یابد — که به‌زودی هم چنین خواهد شد — قیمت نفت به‌شدت کاهش خواهد یافت.
قیمت نفت سقوط خواهد کرد و قیمت همه کالاها پایین می‌آید؛ البته قیمت مواد غذایی هم نسبت به دوران بایدن بسیار کاهش یافته است. تقریباً قیمت همه چیز پایین آمده است.
قیمت نفت اکنون نسبت به دوران دولت بایدن کمتر است.
ما مقادیر عظیمی نفت استخراج و عرضه می‌کنیم؛ دیشب رکورد جدیدی در انتقال نفت از تنگه هرمز ثبت کردیم؛ مقداری بیش از آنچه پیش از آغاز جنگ از آنجا عبور می‌دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72366" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=skPy9jxtaxoSFC9JPeqY0oPj6-ltx7L88hL3gtkQ86Q3wX1JGTCDYcSUVKWIRLWJbnVsbA4HS2DBOIv1IkfIOIdBkGmL0I8kWRDgrlpFMI1izOtb8BrvuwJcd6kANymFwUWSD8RyQME-q-dK2So9WQ_lV6nDIy_1AGBejhaTv0kcabPCEKqa5ebNp4UQiMP0_iZOcfSqqGoSZZXCkIohc22aqdA45iYrqpYxqiUjuSsb57_Ob7trcDfWK1jdEafmUed0xDMhaF3nF4a4v8nEfK58bNz0zDt3K2Em6x2vXn3W7LBgaKmWeTjljqrzJG_ESmVlDvu18d1tlp4XlyhO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=skPy9jxtaxoSFC9JPeqY0oPj6-ltx7L88hL3gtkQ86Q3wX1JGTCDYcSUVKWIRLWJbnVsbA4HS2DBOIv1IkfIOIdBkGmL0I8kWRDgrlpFMI1izOtb8BrvuwJcd6kANymFwUWSD8RyQME-q-dK2So9WQ_lV6nDIy_1AGBejhaTv0kcabPCEKqa5ebNp4UQiMP0_iZOcfSqqGoSZZXCkIohc22aqdA45iYrqpYxqiUjuSsb57_Ob7trcDfWK1jdEafmUed0xDMhaF3nF4a4v8nEfK58bNz0zDt3K2Em6x2vXn3W7LBgaKmWeTjljqrzJG_ESmVlDvu18d1tlp4XlyhO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود کریمی، مداح حکومتی، در مراسمی برای علی خامنه‌ای نوحه‌ای به زبان انگلیسی خواند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72365" target="_blank">📅 16:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=cxuWjpij2aF4OmIiyKZbHWfRX5RJR9yiYCAQYQct30-5Bl35zb5fZQ7A0OQ_WnP9JLqBCMs_k6ot4uPMeEBXJBuDO-E4qnTwFDpKKPFCWa5RoEc1LBxgnXa3ggW1ZVRKw53zbGc09WdfFs8uB369X_s4S8883tDl-Gsf4YKbaYXzTi4zxoEkCT9zcQeAAYjBY3t8z7EDW7VLKLIJIhFGbJqitsvNXsP3VlRzNWbz48bRSgfQhvLfjr5onPygGIyKUlgHPXb_CnOP2RFzZEh6jdemefofE2Pg4CXP1dexG38kRU7q-13cvxXLOpqC_DKT7rzwh3Cbo9jLV8gNum3xGANZnmt5bGG13x25NpaQ0-uEJZZUMa0HqdroEtvCNP7EqPDpm4UE6qq6Rfsp5LWXM6dUqgggXWJ_cuoORx914W5saPq14a4E1v9bcZMONRaPYPUiKZu_bV2ZHdEF61SUpyB5ZzO5gfnV0akdFTGeb0ZpgHiXFP34rEOfdiwih2u8uW-4yKzdUzdXK5xm832Er-ifre5taIDqsHEi014xdh1yJ0SJ5njcd6-4pc9XRvm7PcSYvg-xh1jKr_mI_aq7RgQVTZ7uiSANLQyTqG4cxO4EXCBv3gyHdENUWEGjGxzGH8zTtDPTGuCFSMzrVTcwD4-KmA7mf0oYVbG3eGQXPnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=cxuWjpij2aF4OmIiyKZbHWfRX5RJR9yiYCAQYQct30-5Bl35zb5fZQ7A0OQ_WnP9JLqBCMs_k6ot4uPMeEBXJBuDO-E4qnTwFDpKKPFCWa5RoEc1LBxgnXa3ggW1ZVRKw53zbGc09WdfFs8uB369X_s4S8883tDl-Gsf4YKbaYXzTi4zxoEkCT9zcQeAAYjBY3t8z7EDW7VLKLIJIhFGbJqitsvNXsP3VlRzNWbz48bRSgfQhvLfjr5onPygGIyKUlgHPXb_CnOP2RFzZEh6jdemefofE2Pg4CXP1dexG38kRU7q-13cvxXLOpqC_DKT7rzwh3Cbo9jLV8gNum3xGANZnmt5bGG13x25NpaQ0-uEJZZUMa0HqdroEtvCNP7EqPDpm4UE6qq6Rfsp5LWXM6dUqgggXWJ_cuoORx914W5saPq14a4E1v9bcZMONRaPYPUiKZu_bV2ZHdEF61SUpyB5ZzO5gfnV0akdFTGeb0ZpgHiXFP34rEOfdiwih2u8uW-4yKzdUzdXK5xm832Er-ifre5taIDqsHEi014xdh1yJ0SJ5njcd6-4pc9XRvm7PcSYvg-xh1jKr_mI_aq7RgQVTZ7uiSANLQyTqG4cxO4EXCBv3gyHdENUWEGjGxzGH8zTtDPTGuCFSMzrVTcwD4-KmA7mf0oYVbG3eGQXPnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTm1PQxbH_ajebuxgKh3ftv8NAmdr3gqAN6eYsl8JQ0q_bAbB1Ovc629nPLolWXVbJmfCbMeXtJaBbpGaH1pknty6Xmq-w5xduES-W5a6q8wJ3avmhFIvZN8vO8g16b57Fq_YlMSVN9rS90FC-RCb37EObJxlBXrzxARUEK1nDXNXVq2iWlmFBhwyxHMAqXScbJcViIDhX5Ne6SqxsFuhvoCK5Tm5Ji4OjUN4A6PzJT2r28cHU8heAXUfeh7O3rCkQq6QSl_hZ68-DbSzODQDdWyiTdQtMqL0QSpTZq4qtVk4y77YCWKKhyqAKHfvqag6kxHSatmiv-_6RzTIsr1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=BMWIxgfn1gsZh78yeXytqqERua5q4qosEUFqoNQqNuZiwlDP5MoHqC3sisEvPJ3yf-aKiIUZh-GkeLsUuGcQ-6gEe_9LEj4_HSNFHKp7RGzAzc0CuCkmT6FrOnphO--O9m2GPQmiT_pNGF2C7DhqnHJo_fr-_muwS0XEKOFNXnJsTukTu1GyTmyG_Tvc3PyPan85rElLj7R3h7OBqrCDsp1pcepa8Xwr0yP7_7S-dDf9BoJOGDMMsX41GWCPv4JUrlqEdm9dPVd7kuNCoq8UHD9dXyL8v-J-uQrlPb29oIXT4Ol3VkSHuZ6XdBqN4F-Eu7Oas19HYNxDueqF6QDtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=BMWIxgfn1gsZh78yeXytqqERua5q4qosEUFqoNQqNuZiwlDP5MoHqC3sisEvPJ3yf-aKiIUZh-GkeLsUuGcQ-6gEe_9LEj4_HSNFHKp7RGzAzc0CuCkmT6FrOnphO--O9m2GPQmiT_pNGF2C7DhqnHJo_fr-_muwS0XEKOFNXnJsTukTu1GyTmyG_Tvc3PyPan85rElLj7R3h7OBqrCDsp1pcepa8Xwr0yP7_7S-dDf9BoJOGDMMsX41GWCPv4JUrlqEdm9dPVd7kuNCoq8UHD9dXyL8v-J-uQrlPb29oIXT4Ol3VkSHuZ6XdBqN4F-Eu7Oas19HYNxDueqF6QDtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT0-2BzOulirJlMZnMXc15UHSJNAg_nXhXBtCenfRk3y9UV1dyZlb1-QqFfyQY17UfXi_QA_Bu1MyQra1v1nu46LiAHtDU8mt0vfT5u0CyPXsTTgXe36zIMY7qxW2xu8EVpnptwkAGf8-zi8FFEicX0WVQ46eWHe0g8OpLp2979A2iUScF3jIAaz-RdOCmnnWTjQDRGjVpB6j3uC3AHnaGkONCSn06GKg17M6eDoKj8DB8MzYE06akQ6XXJ4HQlJZfQfOKh4BK26zWSb7862Xvqt5LeJXm3_0HqjdxeONMAATZQHtO_NZQZMGerdmG1Z6a2hRMyaDNsUu4xNbH9QsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=OfugKulUsrJTzgReSnu4To0sc1IYuIk0xGjzgldug-Ff6CVd6IuMO9jJRp7uFHaUokjBQe8_fE3VlgoJ7XMKKrshRESDeBz-iA2ABFJltokW7uAE6TYCT6Ax5qUiId_5YL1-OJLaQ86rSQK4-yYZ_YpE6Pa9AbcYepgERbdTopHMEeI7G9V6L0BxlIEKYed20hcU8fL4JUphy3c8pBUCiLpMGHy_umb-0QnSRPnTIlcdlTun0mQVCR52ybOi1K4wF_KDD27hGU9ij4aIQkYbo2dI4MNQTi_liuNmZ17DdhxOTBhbFDM25-PIcuqM-e3c-o7cUTpyTCHhJvRoQjfjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=OfugKulUsrJTzgReSnu4To0sc1IYuIk0xGjzgldug-Ff6CVd6IuMO9jJRp7uFHaUokjBQe8_fE3VlgoJ7XMKKrshRESDeBz-iA2ABFJltokW7uAE6TYCT6Ax5qUiId_5YL1-OJLaQ86rSQK4-yYZ_YpE6Pa9AbcYepgERbdTopHMEeI7G9V6L0BxlIEKYed20hcU8fL4JUphy3c8pBUCiLpMGHy_umb-0QnSRPnTIlcdlTun0mQVCR52ybOi1K4wF_KDD27hGU9ij4aIQkYbo2dI4MNQTi_liuNmZ17DdhxOTBhbFDM25-PIcuqM-e3c-o7cUTpyTCHhJvRoQjfjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=qpfaoflBfX5ghIyoBL3zCQ7w-93YNzC_pWWCFnxVVatVZJU1Z14EFcNiDIEzQAj4-ov90Oyt-E7f9kCbo__0KSizEsvJx24PMIP3vcgOV0NrEPv76sNcCdogu7PxFUN1zbClFo4kYiduYPL9B0iA4EFAN9ryxcknFrfX4zxa_EUqvG2vd58ZgycnRVQvjJzr6mHlvJnZEPDgTiaPQt84nSFr4YTDYs5RCfG9-g1q2ABNNjh5LkeWE3mc6VqjcBv0TBFmz9tXkpYhqT05G8Ew3Uimj8Ta6kRle61Rfy8fSgN-Zbsc2nAM-td4Nr2-zEQI3zA5iG8h2EaJ2YwWFVMdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=qpfaoflBfX5ghIyoBL3zCQ7w-93YNzC_pWWCFnxVVatVZJU1Z14EFcNiDIEzQAj4-ov90Oyt-E7f9kCbo__0KSizEsvJx24PMIP3vcgOV0NrEPv76sNcCdogu7PxFUN1zbClFo4kYiduYPL9B0iA4EFAN9ryxcknFrfX4zxa_EUqvG2vd58ZgycnRVQvjJzr6mHlvJnZEPDgTiaPQt84nSFr4YTDYs5RCfG9-g1q2ABNNjh5LkeWE3mc6VqjcBv0TBFmz9tXkpYhqT05G8Ew3Uimj8Ta6kRle61Rfy8fSgN-Zbsc2nAM-td4Nr2-zEQI3zA5iG8h2EaJ2YwWFVMdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=W9tNUvLpDBNEpsGT8mmRXDS-yfOjuqr8MOVtR1An2v5wZChvgyURy8zYWS0r_tyLLMPpJksUAIIq1agsmbuWqgVGBjjIeLeMfPqArm16ERI_GJIEHOj5R7jj4vfwpQI_XhxEuhKaseL4Erpcp8mbKs50kM0vPRfxxsCA2nNGl-SIrSqEYE4_fqzZvk5dHY4Kh2YwEKLgNtULc_jfgf8JKZJFDGb7bjteLLYVfJCiG8awLj6qXfv32ng66BhVUJ-14gqDVwQ0KwM-ViQW6hNZfOPvGXq0VP4Isw4LIs-3IqLAAq9oW5iullizAmGsxVPU03Py_E8clg5ArnrivoeQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=W9tNUvLpDBNEpsGT8mmRXDS-yfOjuqr8MOVtR1An2v5wZChvgyURy8zYWS0r_tyLLMPpJksUAIIq1agsmbuWqgVGBjjIeLeMfPqArm16ERI_GJIEHOj5R7jj4vfwpQI_XhxEuhKaseL4Erpcp8mbKs50kM0vPRfxxsCA2nNGl-SIrSqEYE4_fqzZvk5dHY4Kh2YwEKLgNtULc_jfgf8JKZJFDGb7bjteLLYVfJCiG8awLj6qXfv32ng66BhVUJ-14gqDVwQ0KwM-ViQW6hNZfOPvGXq0VP4Isw4LIs-3IqLAAq9oW5iullizAmGsxVPU03Py_E8clg5ArnrivoeQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZRRF-4Jf6fWpkXlwf9HkE_A7q7NcjK93WPoe2n8fnUzU9IrCIutElXomyo0i9QSrYVufnCmflpWf8gQGg7nzN77JRIQ6qQuT-hV7av107TQ8WMbUPdWkUxc0A8g72_j1rW86Pbvz-Odogiqh71Mev1nnv8zWHfBoXg5FWIM0R7u0vCTUpJKQMj47bdDf4BDRiBrLr1H1Nu8xAwto91gmtrUbfrMnWErWwtu_Z7Y7DvYTjbM2uq6dZKrQILeEzqqPIDOlp653bP2ict2Nyzw6SSoO-by9KSzmHmpNeyKe76X31m0nyPPYiuyCtCyEKhonU6YVM-ai4J9056Pp7J3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbZu81HKQwYzlPSv2QiShk7GecoA9SObzNAw7Lop43zbBHWqW93PpK82ln0zL22dP5Cg2usQDeUQDos6XDcIfYjotDObsFKbUaIh3l8heFtj_d4z91tdTRXffDt5rZV5zzsr7u71OrejLGwXzIJJACfu9cIshSkqhlmZeKkyAlthJXV-c6p4oqPtW-Q5pVpnnbh2wR7l0o149f9PbGAsaVrqFuyk8oT3Ji8zfX0gwhdlkR-YSA3rPHOfVCGEfDzBeuO9nLo91adedTV4v0t5psli7WNjTWqqUUpsO7zRa_MOFld4KIrAvpbAkpnZv-2OngJ1N-bQs0UOYUe6PFXLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeqsOKG_aF4_9ZeEFZTPS_xRJxhiDoq06v2WvAGS1JjV2qWxknrQhM18ehnuz4PyuQWWC8MBzevRoCzjIQyBaCzwNPdARANoAct1UZDRlZB-9TfrhivA48aYRWKjSmU7-dq6fiBh01DfjEXpsgh-sOn7vjXeVNk8w78zTi6GgIdC_nIoJplZrtva1IO_vPtcBppfRPL8TFj1-MY2-8ih58QWqfUqSpw0UH5-qatTo4hQQodvD1wgrxfGrHTe4TPPrycfYRXqcDU517wwbYiCYEHwKNWgHcZNgW7sXNwj92UfgMxWUjUcpA6sh0TyZSGOQ5U_JoYVuOzuN-QgTfrwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLdMCgZfnLYqkpwIkEQGPW0jl0eOq1WpD2iHRAP9wnHjOkDp0gYrba_Fvvhwupb9DcIrNjA0Ob63loRTL1Ssqmk3ex90dGIykihEocN4dDqd7NmK1FUTqU036zPRONx95zzLp3XHFbIQ0oqXNwQE8Ps8cREYZiTkplxXiL_dTzOLu9yCdUmcGWT0ySYefLUgCx2bLbHF0CvlHAUKrLsyG_pSEbxoE2F1pa52zuldxHVWCYVUdEUXcsa6aQd_pCK-JqOet2q_XMwKD8DK7HdQAqQx1Wfbr6eT-rAoyn23XqUHvkyJO06yx1qYh6DeYaKoz601Viml3ngt2GG6G6YwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJdOsFArH__1Fw8SBEixpGTfHdRi6YTbroK67HnEvNSM3ZcdYt9NJdoMFn0us7SZNKVMwmENfaAdKgJQtIZus5bHk-UHhtqoJMTNqgFaJOSdusHomwjmECdHrOmMWFD9Rve19QnIk07jNa4uy2SjzAJQI52QWo2LqaeMaaPp19I08r2vil5qpuAahhare0NEes7xbHnpxuL9vFZ7jII1MdgDzS3aljy9lSX4pzvHCaMtr5jvfN_W72-9G6jX4liCeH7U_TrhZM_Jbzt59LRxbVhovZNhnnJqcAdvssbjZWzqyQP46VamKnlJsOB_q4wE_vOXysRQNS6NT2e3ENyhTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=QWN77d7dtoluSWxu4YAiw_0V1w4uaTpERKdidt2gpbeISog0G9pZltO9HwP8haFC1CDzdyinCRx9Nbgs8c5_-Du_eb7i9DT6n7X-inDvT8gLGzwPli9B3M6EF2kzQFE3Bf-90vWH9fmBnA7VYwaSRBcrw0SQ2o0k1Go15Q2P70IZTl_42-HX8WzsQmiKlFua97sXmRlhIqKLA9BkSMYUZmTnqi-yHCTwSClLcoVtShTaFgDQyG0KFCbkZgBGE8FIXuk4fp2SpgwQenxDSdN0ckiTJEIedCRdXinTLwBS7V1SYprHWAQlizJJiphPJKT7psdzTMNpYyCrmI4CmsuCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=QWN77d7dtoluSWxu4YAiw_0V1w4uaTpERKdidt2gpbeISog0G9pZltO9HwP8haFC1CDzdyinCRx9Nbgs8c5_-Du_eb7i9DT6n7X-inDvT8gLGzwPli9B3M6EF2kzQFE3Bf-90vWH9fmBnA7VYwaSRBcrw0SQ2o0k1Go15Q2P70IZTl_42-HX8WzsQmiKlFua97sXmRlhIqKLA9BkSMYUZmTnqi-yHCTwSClLcoVtShTaFgDQyG0KFCbkZgBGE8FIXuk4fp2SpgwQenxDSdN0ckiTJEIedCRdXinTLwBS7V1SYprHWAQlizJJiphPJKT7psdzTMNpYyCrmI4CmsuCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=s9Aw-zzoQqTXxYqRTWjvh8C9PJh_G26RzqmvP4T1Y61lERW_p7j9FBYPB-zeYyNCTZpzv3uiYJHoqQNBTk0x6z6YK5Uw9-vpKq-DgDidp5vLuFluxf4xTyhEOIeUVJXpcAEe7Tsptn8d9gYTUwY6gmgWMLAAuI-l7T34NzJXV_LHdRnXb9AmlOOv18gdwIG9bEI6QMzuspYEL7_dYyWi_uZgGvA3tAojGrrFosK7O7XKS8kBkQ_Nu6-5PvzFghAJGQ83WsEVPAVCI129_Wz6JwUrOxL9j9Vbtl52yyU25b8RC1LyRrwSiepAXXYTSr1quTFXqFc-2XQjBFQUAqm0FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=s9Aw-zzoQqTXxYqRTWjvh8C9PJh_G26RzqmvP4T1Y61lERW_p7j9FBYPB-zeYyNCTZpzv3uiYJHoqQNBTk0x6z6YK5Uw9-vpKq-DgDidp5vLuFluxf4xTyhEOIeUVJXpcAEe7Tsptn8d9gYTUwY6gmgWMLAAuI-l7T34NzJXV_LHdRnXb9AmlOOv18gdwIG9bEI6QMzuspYEL7_dYyWi_uZgGvA3tAojGrrFosK7O7XKS8kBkQ_Nu6-5PvzFghAJGQ83WsEVPAVCI129_Wz6JwUrOxL9j9Vbtl52yyU25b8RC1LyRrwSiepAXXYTSr1quTFXqFc-2XQjBFQUAqm0FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULbE9jpC3RKFrcZ9IS9oIHOVRLGMnVWGJIoX0whbfzsw-li19PtyYd1Wg6J3u-LtJ_HfOLpDp8dVnfeZ53dEcIRMX1ITY9PtJk7hQxvDIlD55bZW3P1YEOZ93H7tknT4F2ZmUJVgSMVSQc3cbfQu_Uig2u04pGnmPONR28yjDn3NrnGnKTRG--VClk-AMMQNDj6fPwxEx590dUZNZEMxgrd-0rRnoVDjRX6WiLu3n2U_C2sY3i-BLpFVZWeKCSb1s5cSEcpGpsptnAKTYQtUtZWQXU5wEt5-vwhltbUa9Ss66FQS24w-pvNhgTo-6PiJofu3DHgrrZeuAsJ2v1oC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=UUaxyLdqjJjz8XC1qykxGla7dy_kP_N_-glp1Sf0UXCvPJowHnqTNGuzxZ6a-bJTkBZ8hVfMzhMDxdk1b_3XgC7-ZwNZAROBJBkE_150W_ykoFaKDrZqajdGQDFCXsOC-HA5g33UvryMwfx7L5Njs5CiI6YhqLMxZpEvmLjTjDv4bMSdMwz2u4hd-RX6WYWg50lRibaXLgwJVkg7OVuiynnFS_92I9HTLZQfUV-seJ-dQycHfXKgzgu8L_Z9pImArPAo9VKH7jLEhpQya40J-2zUAdEhVZhYvSVjyUOLL4nwYw3XqPSq7DDnKBQ1unx76MOotD1jVjE4BksPAlUIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=UUaxyLdqjJjz8XC1qykxGla7dy_kP_N_-glp1Sf0UXCvPJowHnqTNGuzxZ6a-bJTkBZ8hVfMzhMDxdk1b_3XgC7-ZwNZAROBJBkE_150W_ykoFaKDrZqajdGQDFCXsOC-HA5g33UvryMwfx7L5Njs5CiI6YhqLMxZpEvmLjTjDv4bMSdMwz2u4hd-RX6WYWg50lRibaXLgwJVkg7OVuiynnFS_92I9HTLZQfUV-seJ-dQycHfXKgzgu8L_Z9pImArPAo9VKH7jLEhpQya40J-2zUAdEhVZhYvSVjyUOLL4nwYw3XqPSq7DDnKBQ1unx76MOotD1jVjE4BksPAlUIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ppytp6D-rbo73mzMMrxOoVvuaKK5XO_UF1zV8yQh7fKciJf8XzJ_ubuRgmp0_kBTRqFXFp0ZHtzavjHcyTbdnoGiJ_hqDWEs2A0MSWEB0qxHjWdQWobD_x63QK72E_h57f1_chu8SFbCJ5LSfvrGTe6Ov3kvHd8Ut78F-IRECpHv4P_muEZHeIjOpPO1MzIdf5lh0rrL891ZFlx6W4J5LgZGNWUrATNzJ2oCqNLRyenkyYOhMr0N2TbYzDVsqkHf0BeWDjrqwtJMXbG7CBdZXy_pmRG_RzxRu7SAEXwz0WnbcBYgm3ja0fM-yXzONivo9Ji6yUNhVh0d-UsuZa5kxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgtfNhsrcYrdpJ0wBXejsCvQGZskrb2EKF741YzwGAFoexUAONpNxt_ajuFQzjuezxYv8zNBE9k2GFqzdn-SbwvGX9aLYu9zYJC9LJ95UOTbf7I5XnYxNdH7KGHRbuPF-cQ6tjcruvCgSzst5wGDnwqVghDeaLGumM1oWv8t4NfIUWqDz3GwxT200KEw_uQEFnxy6znTPVSwhFGcgapXKCrUAR_Ryut69wa1ipEi6aZwnmGgvmA0PtYvP3lub-U5yQmx-9PPxzwEJkOlNEL0gJTzqXdtLSSGjrLKjq8VFjc-C0pdLGscpp2898LdsOwCBGm9G6x85YG_8W9RacbZvQ.jpg" alt="photo" loading="lazy"/></div>
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=sL0zqJTBHWp5y9zCBKM9IyyzcNxux_DnIAt6mcK_a-wphvHTQE3YufCI5G2NkxQLrT7-44y445id4QL-OQfXqNQyqGTlaiJeA1U-X9VjHXY_MWePyTnIt0xr2HoP7sSW2qBCFqa02gcmD686VlQqCX2DCHl2sU4hJlV6BT-VrooNWAHTD-U8hDTG23Hu3L-uCLwL07YhPk1iDITjsDi-0VtMl2q6uxUwzB9Pdz-jfobwuL7RGeCRZI_LA7bCa760dbZr6osPhh7CzcAayFcwXG_cy_EPn908AdcWjF2eAAygHVZDqIIIV1_gBQu_qAO9NINv6dMxIcFjKkPGgUdzzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=sL0zqJTBHWp5y9zCBKM9IyyzcNxux_DnIAt6mcK_a-wphvHTQE3YufCI5G2NkxQLrT7-44y445id4QL-OQfXqNQyqGTlaiJeA1U-X9VjHXY_MWePyTnIt0xr2HoP7sSW2qBCFqa02gcmD686VlQqCX2DCHl2sU4hJlV6BT-VrooNWAHTD-U8hDTG23Hu3L-uCLwL07YhPk1iDITjsDi-0VtMl2q6uxUwzB9Pdz-jfobwuL7RGeCRZI_LA7bCa760dbZr6osPhh7CzcAayFcwXG_cy_EPn908AdcWjF2eAAygHVZDqIIIV1_gBQu_qAO9NINv6dMxIcFjKkPGgUdzzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=J_d75nKQ8D_CbuweHwSO2H5l-4WrYJyEFNA91QNf38q3MUtgYzaluWShC9u-Pj8s9lErY0ilIpki0dAi2kYZgnAkWQtAKPEVfA059HqvaHIeToIhLyFVc_Y5HpCHHt08vD-lvch-nRJI5ntB4UgxUG0LsAFn3w1nhhLQTvE0HEIBJQ_36nOCcZvMG2WpnvXw-IACtN0v7cT9RBJIa_e-7e9mylzCMS64e36xk3PKyODgfF2a0BgAzHAADlq0DerHY-yeSbr9CEeG7V2_SOQH5wAenmm0736pLBlYMIzuMNq7yxT9rqdEQJ9hmCA1tUUUY48tnTCKK-_w7-cOtEcaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=J_d75nKQ8D_CbuweHwSO2H5l-4WrYJyEFNA91QNf38q3MUtgYzaluWShC9u-Pj8s9lErY0ilIpki0dAi2kYZgnAkWQtAKPEVfA059HqvaHIeToIhLyFVc_Y5HpCHHt08vD-lvch-nRJI5ntB4UgxUG0LsAFn3w1nhhLQTvE0HEIBJQ_36nOCcZvMG2WpnvXw-IACtN0v7cT9RBJIa_e-7e9mylzCMS64e36xk3PKyODgfF2a0BgAzHAADlq0DerHY-yeSbr9CEeG7V2_SOQH5wAenmm0736pLBlYMIzuMNq7yxT9rqdEQJ9hmCA1tUUUY48tnTCKK-_w7-cOtEcaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=D-VJw6svpoXZzFL7G2cHVuU8LhXgNwpg4ojgwi6aV6wkwKlp3DoBo7S6l61-z8qNJscH3WAQVAJ7ezHf02zcGZNybRG2n9U7_A1Tmm14nqW-kfQXsvrEsxH6hWZdsR4Jo0pr6qYdUaTXf4NKfeo9PKjzJr_kk7FyhMptR4nlse-bvrohOLVBk6QwDLNntfCq8VNwmb6TTQXHa6KzQjJ86H0weJRz7Nix5NEFSV4Mj2at2Mg3y0v-mlHJ3GINB0FfmTeVGiwimB8XjtxoTYv95sEXBZ73iloO4iz2jvbQieEJD2UhsHgSN9bCEaM22xhMdA8C7CTE-99VbovJ1d5Wuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=D-VJw6svpoXZzFL7G2cHVuU8LhXgNwpg4ojgwi6aV6wkwKlp3DoBo7S6l61-z8qNJscH3WAQVAJ7ezHf02zcGZNybRG2n9U7_A1Tmm14nqW-kfQXsvrEsxH6hWZdsR4Jo0pr6qYdUaTXf4NKfeo9PKjzJr_kk7FyhMptR4nlse-bvrohOLVBk6QwDLNntfCq8VNwmb6TTQXHa6KzQjJ86H0weJRz7Nix5NEFSV4Mj2at2Mg3y0v-mlHJ3GINB0FfmTeVGiwimB8XjtxoTYv95sEXBZ73iloO4iz2jvbQieEJD2UhsHgSN9bCEaM22xhMdA8C7CTE-99VbovJ1d5Wuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxPJcYStRnFWEhbFhWDp_Y1m1sk5gDnz8hw_v0Vh3dZldVOpsgE8lMXnjV6wd0Pi3a1_qJQPQKdqTHUp8nwPge-MzjsGqPO3Kf-r3QtRe-o3ibTZXU3I-pkXEwUYeEkiPzJJrVq9aupm6KUpc72KHY-zo4YQRpGhl5LA5stMhSH8w5D2gRTmkMVCO8cLX3I0CRcNqoWNaP2EPzm08w-meBkiYtji4iJVH-S25G9QyMXe2_biej9sXyGt7LkXIVQ-29p2p29kpowTZSM8Bu1st_iLOjSc3Jrq76IltGawityACCdvuSh0zEhF-S2mYDvlxULm-Hf3gKTkfjGt9L-u2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=MjsE4zBXrC3hhBDbdimBCnsjlBj48xJXT9gUOkcawqgNjrQOJyhR677o87-uX-yaXvMSMU4TrRy2_UsqZbYBh19ssyBqbs0nial-DAmQQRA8BjGh97aG3s4g4KvqSc0Y-2FDBsVzOH6Rn5QJWOEwAFcPrb73r3aJYAZTKvkCkpir9csqIrm10N99K4302M6JA9zrSwVxaH_L-i2HECIXOMSc3W3oOO57djIRyqyYnHombl8g61gODrlpfkNgfYHjn-ZtyY9E3cwmLron8ewFg_VzuoU43C0STXi2SRnPCfvpavTNJRelatn_MU8bjpFuxV8mwIWg3sOU4R71UWIuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=MjsE4zBXrC3hhBDbdimBCnsjlBj48xJXT9gUOkcawqgNjrQOJyhR677o87-uX-yaXvMSMU4TrRy2_UsqZbYBh19ssyBqbs0nial-DAmQQRA8BjGh97aG3s4g4KvqSc0Y-2FDBsVzOH6Rn5QJWOEwAFcPrb73r3aJYAZTKvkCkpir9csqIrm10N99K4302M6JA9zrSwVxaH_L-i2HECIXOMSc3W3oOO57djIRyqyYnHombl8g61gODrlpfkNgfYHjn-ZtyY9E3cwmLron8ewFg_VzuoU43C0STXi2SRnPCfvpavTNJRelatn_MU8bjpFuxV8mwIWg3sOU4R71UWIuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=MSqhLLvMIG9SGJ4cC3AyKLa9vpq9lgPh2qSjrxpCiQ6yI0P_NF73LOCMkSUdHWIF11FzjB6DXhwx0l8GpkQDlhJaPcBDdn-utxyD_EH5BzrN1Du1H7WhjT3MMBFMlgy2QpilLE-IATz_eX4zKCTRCoTB7qycs1zX6_kwd98dJ1P-lUeTYeZNWFT0iou7bweUDKk5cm_e6zhNrdqEm0Scla3zgebcGlOpVOaZ987U8NDWXGg1Gc6RXTh2h68EidjMQIextyjTdW8xH4mhbAtoBy9gvwg_30rylM4ECpHULEIrjGUtwVYIXy65_0JH1azPTQiq103cPw9JU7F8wipUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=MSqhLLvMIG9SGJ4cC3AyKLa9vpq9lgPh2qSjrxpCiQ6yI0P_NF73LOCMkSUdHWIF11FzjB6DXhwx0l8GpkQDlhJaPcBDdn-utxyD_EH5BzrN1Du1H7WhjT3MMBFMlgy2QpilLE-IATz_eX4zKCTRCoTB7qycs1zX6_kwd98dJ1P-lUeTYeZNWFT0iou7bweUDKk5cm_e6zhNrdqEm0Scla3zgebcGlOpVOaZ987U8NDWXGg1Gc6RXTh2h68EidjMQIextyjTdW8xH4mhbAtoBy9gvwg_30rylM4ECpHULEIrjGUtwVYIXy65_0JH1azPTQiq103cPw9JU7F8wipUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72326" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdwKllqC2WUGUZIvIyq8WJ7JcpnUsgDMyZDJajFSSJ-S12OpdvPeHk61GhsJj6qw0m56uOBfjPzxkLs2OFv478GNeFDaj2fB7tt8MMq7KiRRPIq92zubd0NuGgMZW06OvATdnzMROA3Ki2zZEQ48NZ1vlpM_WmytGE9estWShv-LgWO9Ykwa_LHd4Rep4o-9RlqlMIt03CWLy-VfT0COI-gKdfHllxskz1Wpv0RQMWgqGPo5_YQETFrynsPwDHxv5Fusd93YKvq7ppRLzeFc0vAuNOO5ycuSRQ8VN3Ic9rlp0L4qWpLxvqv7RWnzqVzrbzohY4sfIcHrEPyt-Kmgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72325" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق گزارش های تایید نشده، عباس عراقچی بازگشتش به ایران تاخیر افتاده و قراره سه‌شنبه ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) از نیویورک به تهران برگرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=MSSCMmurSlMv08rRNCYj-rOmTBZ3lrJUnoqsoPZL71HqqPu3wOMn4t2vZbbgbreN2X2RYRrkHXbVL5jRtGZ2jSrtYf1Qov7VckimQodYOFe-11ynCjOBqK7cZDnx6hNBfiiJaCFlUaVt79KWoO75UtV5t-uasV15QZ9M8KEAn0m7fIajAaYbO2WzSTYgASNCqvtksIv6gxv5vIUPasFYQaMqJvaqeVHXuzfPmsSO7ngoD0UmuhtyJc9L2eT1SbYpG9udoBG9lnnUr5nXfMC_VfmA1k2UUVjHAQc_YxccHO2O7aKuwXdG9qE-5jxouKtrKMk4naoz2BI61JOt2TuY9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=MSSCMmurSlMv08rRNCYj-rOmTBZ3lrJUnoqsoPZL71HqqPu3wOMn4t2vZbbgbreN2X2RYRrkHXbVL5jRtGZ2jSrtYf1Qov7VckimQodYOFe-11ynCjOBqK7cZDnx6hNBfiiJaCFlUaVt79KWoO75UtV5t-uasV15QZ9M8KEAn0m7fIajAaYbO2WzSTYgASNCqvtksIv6gxv5vIUPasFYQaMqJvaqeVHXuzfPmsSO7ngoD0UmuhtyJc9L2eT1SbYpG9udoBG9lnnUr5nXfMC_VfmA1k2UUVjHAQc_YxccHO2O7aKuwXdG9qE-5jxouKtrKMk4naoz2BI61JOt2TuY9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=C9DKk9t-0Vgerqi3qTZQh540sZgUc2d9CvnQz4ZRNLFMbWEXMC4VjFqcXLw683MjXKBjnq5Zn21lGWXJG1vn3Z1wRv0dAWklybKIXivUUnBrMFmshsrKVAwtutTwX522_10DpsWeE4MeYQcO2LDMAb_DoFJ7YHYzeuLylVdp_s1bvEegRCEdI8EFi-J5E8t08vX-29pKDi97ZfDGKWHbrtIbKL4g4Ei2IDTAtvmfDP-PZF6inuX47dVr-FVXA5fgnVtYCBqtMao2E0U6C-CCMOfAMpb2aqHKxR8CjCwyHJ6Y7vy8SYisTV-Oim8irpJjv-mVAj8ML_HioF551SMFvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=C9DKk9t-0Vgerqi3qTZQh540sZgUc2d9CvnQz4ZRNLFMbWEXMC4VjFqcXLw683MjXKBjnq5Zn21lGWXJG1vn3Z1wRv0dAWklybKIXivUUnBrMFmshsrKVAwtutTwX522_10DpsWeE4MeYQcO2LDMAb_DoFJ7YHYzeuLylVdp_s1bvEegRCEdI8EFi-J5E8t08vX-29pKDi97ZfDGKWHbrtIbKL4g4Ei2IDTAtvmfDP-PZF6inuX47dVr-FVXA5fgnVtYCBqtMao2E0U6C-CCMOfAMpb2aqHKxR8CjCwyHJ6Y7vy8SYisTV-Oim8irpJjv-mVAj8ML_HioF551SMFvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6SWdFHXaXpDjO6HCxNT8ctN8JgCAwT2iGSzNLRoklxLuspEkzTOCIuaOYCZi3HdhApms6PmQ4JGLHCmPm1_wa6-kItz0WZKD1USGNfrUBNBipPAx8YY2PuOUT0qmQZkjavdm2RXhi2Dck5XTltU0f8x6ipA6ai6-tT7pMjM8niFsBTIHqpi6sHYXkiEWG2pUPyJzS6x_r4gnN3bmChqhQyK1FdOjeDGcUaxez6AQlK8nXWMOOSR1ywQC-ibOi_BsOqeyhTBMWHuBwVtT6zHPzNQRawQCl2qHDddihkicdOWe9baOYx5-lXyMByQP35uB525jq1uV51l6mf8mTDqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=Ne4AC0IEaa23j4G3_a9ignFCm0nMqKC3nlHGkqPPJQLJ38m3hoqQqVOQYh9mU5hlR0X6zL0PB6ENloiOgBt1Ixd-w9fcAXi60k4UpJfJBsTksxjWEHmOI5K90npl60TTw6RvF44fePlhl0iMXYbpMynbMVHz8wHgXfFw7J1Lrdhu5w9uToxgma1Pm1dAFrKvnuXMbC7x4MtsellWBOJZGhiYiqL0LjC8yzjh_q_BptdUnCDzQj8Y_oc0ss9oL6E1RwReaOtWKcJ3vHG_nceRpffADjfERbXTyJyUPDWbCs--2Z3s7a1l9hTerAS2Tavbc8TsIT66R7siG2c9lADUwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=Ne4AC0IEaa23j4G3_a9ignFCm0nMqKC3nlHGkqPPJQLJ38m3hoqQqVOQYh9mU5hlR0X6zL0PB6ENloiOgBt1Ixd-w9fcAXi60k4UpJfJBsTksxjWEHmOI5K90npl60TTw6RvF44fePlhl0iMXYbpMynbMVHz8wHgXfFw7J1Lrdhu5w9uToxgma1Pm1dAFrKvnuXMbC7x4MtsellWBOJZGhiYiqL0LjC8yzjh_q_BptdUnCDzQj8Y_oc0ss9oL6E1RwReaOtWKcJ3vHG_nceRpffADjfERbXTyJyUPDWbCs--2Z3s7a1l9hTerAS2Tavbc8TsIT66R7siG2c9lADUwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/perPFkXBbTjUFSPkrXBr7XmZ7BldbygUW4kKZMrDdsfu4oRHySSIIHhDCgcNjtW6uZS0_wu0FT_ahteMGpTCWQab06SJEjsyTD1sH7NZgIP76Uz-7vuv1l2AAUu0u6RDPaqoQ7hhXEDHlwZ-J0N732WI5HdztX2_g_AEJ_4Gtq7ex2ALI_SJisxAt-jm6vQYHl6f-XqNWO0KhR2CYQO8d75ycy-GVBCUNBwu0cdXwJwQ5da1FyNQ3xK2Obk26icNwzlPgOxu4KABSyFAMJFyKnimE4P0ivI8Htx_p5pw9UcT2nNZFVuakW3MUOgmM9lZwM97aQViVgif3nS0uXoZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=G5DrD-Zz2vp95bwLQKILUDoitbCJt72Vach0IoeK7SAPLk9e3NfE6564w252WLA6HEyhNhgrDLbKd0UFwB5xdilU0uiI3VFXX_o9QrkWmWROjLPue3-dSplpOBMdwVvgUcxzi2sBZoVX-aMqGFZAN7yDg_0xpgUF0ULyHf4S-1HZcfKLas0oQUvD-Ij4Ik-fb_uHIOx5IwX59jQVDiT_l6Pk4k5HQgIXDUml10WSCRnsEb_tmYcfihdnyGKqRNH9XovFQHoGQ4588TD5h56KErRMVgMbt-GnOKvH1wHwaGJOiRWlej4_TJcTqJHf4C7y-9HW9-7aVPNeYwtrDuSQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=G5DrD-Zz2vp95bwLQKILUDoitbCJt72Vach0IoeK7SAPLk9e3NfE6564w252WLA6HEyhNhgrDLbKd0UFwB5xdilU0uiI3VFXX_o9QrkWmWROjLPue3-dSplpOBMdwVvgUcxzi2sBZoVX-aMqGFZAN7yDg_0xpgUF0ULyHf4S-1HZcfKLas0oQUvD-Ij4Ik-fb_uHIOx5IwX59jQVDiT_l6Pk4k5HQgIXDUml10WSCRnsEb_tmYcfihdnyGKqRNH9XovFQHoGQ4588TD5h56KErRMVgMbt-GnOKvH1wHwaGJOiRWlej4_TJcTqJHf4C7y-9HW9-7aVPNeYwtrDuSQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-pSyEzfyoCYvSxd9TPO7aJvZ5kvJBELI0DCwZ-DIhsEfunYVpEOAQhecPFVB8I4kpmxkrURNMVf2YLvDAHlxWzEG75UzDWOAfxNvV4XEaKXc3r1z5g9ImFmvQJOTx6c4Vsajbm9VpZ6udWehPcqDa1fl0fumC5hR3X9_9NtKou7x8dsQiAoUNIApn2v3xtTB82OtI7L-PtQkqjPtoj6fTPP02Izmu-5nhoHSxUzKacxOxb4-6-qJdybT4TaRxrY883ocQkyS3yw18aRX7pup-zg3IxF0x4vgYPGvZShF62fkPGJ9xTW7HTfqijGNqrehmLyCnGlRbcinDIuxGSR9Jn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-pSyEzfyoCYvSxd9TPO7aJvZ5kvJBELI0DCwZ-DIhsEfunYVpEOAQhecPFVB8I4kpmxkrURNMVf2YLvDAHlxWzEG75UzDWOAfxNvV4XEaKXc3r1z5g9ImFmvQJOTx6c4Vsajbm9VpZ6udWehPcqDa1fl0fumC5hR3X9_9NtKou7x8dsQiAoUNIApn2v3xtTB82OtI7L-PtQkqjPtoj6fTPP02Izmu-5nhoHSxUzKacxOxb4-6-qJdybT4TaRxrY883ocQkyS3yw18aRX7pup-zg3IxF0x4vgYPGvZShF62fkPGJ9xTW7HTfqijGNqrehmLyCnGlRbcinDIuxGSR9Jn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
