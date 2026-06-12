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
<img src="https://cdn4.telesco.pe/file/p6iFxKZHhHVoicqoie31qkuMWQpjjkTmwkkZHJPC3hCuKoKCak21uaCZkRa6vMC8VpQpieJHWq6JDZ2kLSZR1Vp228qkHmfmG2R5f5_ghKIizRvEyXhv-x1QU-9-qXBJO16AcBeUR9ISY895C0_Im-6xGUNI-3MmdXX3NOp086FzkdaE-oljZwZT3HYuSm0s_8WgtBPTspzynNlJv5ONM7-dLDyA_LqdowOgkamMQujMx_kOrAyE0O_aRmE_q78jtg3dYen9tsNFpB6sE_mzc9Hz-mos7eA_hdQsFFLC2PrqOw73ZL_K7wrOzNmjB55wAHgx6cgYp3kWDRzN5amwJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ed2nvvR-_TK3LOJOphJPESzmdYQz7OBfWL_Q2w1bTJlNELoonP7fWGnCCQ6LxjPlb5lEsm7MyOr5kXbeJTOHlyZ7wTO1fpQ2jG4wDO1kKh1aHBqfTL4XdScyrzlpGkRfVcklxlGGeV5zLsLjfbVGkZC_MvGeC5gutpS9jbnPdYAvUuhZpxCdAAiWxOVP_--_lEYAvKmZR91RQGKgceL-uMZo2TmAvmwfUkkfCduew0lvAsn4_TP2INoVr6KuIGQNIjnaysQRAoOi5ytjsODg61D-EUw5c3wiz3V2lqvD62EoNcexyBFUtcPPb_COx_f3pTA2DbeIizWsqwD6eZhKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
از همین حالا تا ۲۴ ساعت آینده ۱۰٪ بونوس ویژه روی تمامی واریزها به مناسبت آغاز جام‌جهانی که قابل استفاده برای تمامی کاربران می‌باشد به همراه یک گردش پیش‌بینی با ضریب ۱.۸
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/133313" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
والیبال هم که زاییدیم و ست دوم هم باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/133312" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
ادعای واشنگتن پست: رهبران عالی رتبه ایران و ایالات متحده این توافق را پس از دیدار با یکدیگر در مقابل رسانه‌ها امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/133311" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/133310" target="_blank">📅 00:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/133309" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/133308" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
ترامپ: عملیات جزیره خارک از دستور کار خارج شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/133307" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
والیبال هم ست اول و ۲۵ ۲۳ دادیم به بلغارستانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/133306" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
#فوری | نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/133305" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚩
خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
🔴
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/133304" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا فوراً محاصره را لغو خواهد کرد؟
🔴
ترامپ: بله، این بخشی از توافق است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/133303" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/133302" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2zRh3UnZUTC45PP_MTaodtT8a1k5Kp9L4TUbGCVauhfkvsfkkKkfTuNqaaMXX05igkREF1m9KRxFluxGW3eV9ellyN3Hn9laFfDLVdW-HHLiZiluQNEv2p-tlAgBrOqTxBmOpJZV-W4nwhbLxMK61OX4p_3rlA0nHnok610ZvqP59kj5iiJICldYZjI89xD0G41m6r_HnTsOT1V9-smQLMF1Pk4XHAHj2M8v0ZIITmzOiOD3-26OaU6BD4sbjL_RSh5UJAm0q92iok26UAHO19K14mjxV8KT4QKR9kXR4RzH5m6bVUtw9nSTWOiJ99_hNSwiC2Ao81Y56WeN3jKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
توییت بزرگ‌ترین صفحه ترول فوتبال : خدایا، خواهش می‌کنم، بذار این اتفاق بیفته چون خیلی خنده‌دار می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/133301" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
مبلغ رضایت نامه محمدمهدی محبی از سوی باشگاه اماراتی یک میلیونو دویست هزار دلار اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/133300" target="_blank">📅 23:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
بازی دوم والیبال ایران با بلغارستان هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/133299" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/133298" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/133297" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🇺🇸
ترامپ: توافق به دستیابی به توافق در روزهای آینده بستگی دارد و ممکن است امضای توافق ایران در اروپا انجام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/133296" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول مکزیک به آفریقای جنوبی در دقیقه 9.
✅
اولین گل جام جهانی 2026 توووسط کینیونس زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/133295" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/133294" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
کانال ۱۲ اسرائیل: از توافق امریکا و ایران بی‌اطلاعیم و از اینکه رهبران ایران موافقت کرده‌اند ، متحیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/133293" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/133292" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">☄️
☄️
اولین بازی جام جهانی رسمآ آغاز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/133291" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام جدید در جام جهانی 2026؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/133290" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
از امروز جام جهانی ۲۰۲۶ شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/133289" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llkLsY9G88RqQHR7jQqZhyIaZaep6VLQ7vJDiexyP2kURPZPtxKVDFdMlq2AwfGo0pn1iWtWbXcldsQAhdxmvUtQnerGB7BueMOaQzxZM7eUqKwXP3a5ZN_SGpoIUcei6UgojucG0ZvC9aXUqnGAX79G4ONCjimDEhNjGQSXvkiEWUHCll_qZnllYM9wdiTnr0CkJxluiNrV_W1_uIK2H-CI8izU-wxHSv_G0hBE8nJvkekF7n-r_6yzXzrybbXk8tMgjk8YC1Qf6S2wfFMNszcnMxycOq21E1weMsKHUmEeEkQIY5lTffF4JK5w1IQ0_T8dTm8oxTq9_IrxYwphsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این دیگه چه وضعشه...
🔴
تا باسن بازیکن های سنگال و چک کردن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/133288" target="_blank">📅 22:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/133287" target="_blank">📅 22:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/133286" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
معرفی تیم ملی ایران در مراسم افتتاحیه جام جهانی با نمادهای فرهنگی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/133285" target="_blank">📅 22:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/133284" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=s3NEue7GCts9zoWPBbbZyFtq96tyn6a-NnCeVBLrE0RVWijE8Yxb3zSiLFMpZa0AQJKuimu9c5T8MZfqITmAUn1eNPkDWTxBSd-EzIHTtxzyqoi3GxT0QRwAByA8R73au8ZsNZZtd-q484nUyGkVK8Xi1CqsqGCoFyge3om_ax1BBUqex5nplN4CtNLSayt5jtW7jdFUpjO0ZJ5h99BwJfxvKRDO4GLX5UcuPnmINIwXYKbyXVuLhSOPSsKllTAwqT4VOhqZ0GffOVarwB_a2gNGKPpcYUFzLkWJfoddwFVgM04Cb5pVNgl-LieCOvS_7IbQyRe32jAg2lI78IIZa1i_wcCclmmtjqAlw381ix41EWgiAMxJZxgYrit2FievCtZDBbBqCPI0-36ZjR7zJHe7-cvhMHBBzuC8yy6ODIr7bjRe5mFkvFoCGUthCXCUH-08G7ChwVjFgsnVE60jiq4vLKBDSMEVWd1KGbaN3-NCQn4b8j6EIsWhWY2Ncktat--h1oR5alyNGwRRjQx_qmrw2kg9M_U9j0fbSmOsqIY4t4RDqo0qa6oGpjJHyr7rvJhtrYJ1HhB3hoT-zktxyc8Cctg3ZysVTySfyvxbwG1u0hj54WtLsv7cNAL3hfl0FZoK0WjVaAxCXR839cVlvqHErKpb3lJ9Ub2WGzdHmw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=s3NEue7GCts9zoWPBbbZyFtq96tyn6a-NnCeVBLrE0RVWijE8Yxb3zSiLFMpZa0AQJKuimu9c5T8MZfqITmAUn1eNPkDWTxBSd-EzIHTtxzyqoi3GxT0QRwAByA8R73au8ZsNZZtd-q484nUyGkVK8Xi1CqsqGCoFyge3om_ax1BBUqex5nplN4CtNLSayt5jtW7jdFUpjO0ZJ5h99BwJfxvKRDO4GLX5UcuPnmINIwXYKbyXVuLhSOPSsKllTAwqT4VOhqZ0GffOVarwB_a2gNGKPpcYUFzLkWJfoddwFVgM04Cb5pVNgl-LieCOvS_7IbQyRe32jAg2lI78IIZa1i_wcCclmmtjqAlw381ix41EWgiAMxJZxgYrit2FievCtZDBbBqCPI0-36ZjR7zJHe7-cvhMHBBzuC8yy6ODIr7bjRe5mFkvFoCGUthCXCUH-08G7ChwVjFgsnVE60jiq4vLKBDSMEVWd1KGbaN3-NCQn4b8j6EIsWhWY2Ncktat--h1oR5alyNGwRRjQx_qmrw2kg9M_U9j0fbSmOsqIY4t4RDqo0qa6oGpjJHyr7rvJhtrYJ1HhB3hoT-zktxyc8Cctg3ZysVTySfyvxbwG1u0hj54WtLsv7cNAL3hfl0FZoK0WjVaAxCXR839cVlvqHErKpb3lJ9Ub2WGzdHmw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عادل:
❗️
دیبالا چقدررر خوشتیپ بود.
خیلی خوشگل بود
😂
😂
🔴
نکونام:
خوشگل و جذاب هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/133283" target="_blank">📅 22:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVyCLj7oaNeyePC4gurp0cpxEAxQrOTYrJLABDGBB5ZzrYz4GJW08_5E-TdGmRmVXukhbCXuFMTLpLf5KKwsDP02skBdwuETdKpm1n58u5c0i7sYJRT8LjNp8A-Bsqsuo1p9_PeiJBFnnBWaLx2BY4AqzQl4CUO7DB1AZGAz-Djt7b9UYCdN_bCgB9I8RrnLVafq_boRW9ivW8Gd72X0kC5WkXnBq1w30SLgpUXvafJ3wErl_Iy6TUAaw3fB9AUGWZtL1FvMJKKIR1trWx69cO2w00wk1JgYvxpKxF9LIuSHs1_aWKO4uxIStOTLdOGnQhKC6lkLseOIprqazfnHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/133282" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/133281" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
#فوری | خبرنگار نیویورک پست:
🔻
ترامپ همین الان به من گفت که توافقی با ایران "تقریباً کاملاً نهایی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/133280" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/133279" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
#فوری |  | ترامپ :
🔻
من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/133278" target="_blank">📅 21:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/133277" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133276">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی  امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/133276" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133275">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp5lYrERrPY7Z3nhRRQwjRjMfhDdqhjixjg5HraV1cH1CK-IRiq58-WLs2il0BRjNIiD_WrOpmjfWVUkI16cvVoesSA9oetV-E5PeuJisP5Lp4tjMJJ4roPVtJyrMOUvuTH3Fx_Zx29cR-7D7a2XOABbwKgqJPUkI93LazAGflNRHP0xlKL4LObxB5x04F5DujxHj46ic0IAyHzU_NY8vh5n0_Ia71rJvj22HlG86b7TqwKu4hrUISjF1xJNyzJiqW7v3WgT04P5-Yv7XDc6qEYN4cvO6LF3mOAFthvLcNaBT35wxzcsz4nIGRK2teuRiGq6To2Eyzl_wDwHi7V7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار افتتاحیه جام‌جهانی ۲۰۲۶
[
مکزیک
🇲🇽
🆚
🇿🇦
آفریقای‌جنوبی
]
⏰
امشب ساعت ۲۲:۳۰
🏟
استادیوم مکزیکوسیتی
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/133275" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133274">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
داستان پیچیده سهمیه آسیایی همچنان ادامه دارد!
🔻
در حالی برگزاری تورنمت سه جانبه میان پرسپولیس، چادرملو و گل‌گهر در هیات رئیسه فدراسیون فوتبال به تصویب رسیده و  اعضای هیأت‌رئیسه فدراسیون فوتبال به اتفاق در مصاحبه‌های خود درباره برگزاری تورنمنت سه‌جانبه صحبت…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/133274" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133273">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98745e731.mp4?token=i-pH8OmYAxbXLNM8U41s0hIiJHClGzNC7p2I1YDl7h2zJTVQ-VaeHIHQDV_HNdekbSxh01EYoF2OWe1zXVe5QaAIwi4hEzkVWEUugRCXRjywTvOc6W6_vIV47OFQCyQ6Cbj4X4vwuIMktJpcte4tow4vJ7Wps0IL8L_qpuwkQW1eIRBxQtpJSVxR9elnwzW9d58CbtQMlCFYbaSlViqcy82pKHuhUZv5vdJguwZTNoG10QOH6hyLSTGyyJHSSUw7PZWhR4pZZyYcJpTHzv5qoOhUjd_aZawmJiIfCw-XvCZwoLfchWNuK4B64bYpwBnYW75TxvVbE3OVV1zzJRLH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98745e731.mp4?token=i-pH8OmYAxbXLNM8U41s0hIiJHClGzNC7p2I1YDl7h2zJTVQ-VaeHIHQDV_HNdekbSxh01EYoF2OWe1zXVe5QaAIwi4hEzkVWEUugRCXRjywTvOc6W6_vIV47OFQCyQ6Cbj4X4vwuIMktJpcte4tow4vJ7Wps0IL8L_qpuwkQW1eIRBxQtpJSVxR9elnwzW9d58CbtQMlCFYbaSlViqcy82pKHuhUZv5vdJguwZTNoG10QOH6hyLSTGyyJHSSUw7PZWhR4pZZyYcJpTHzv5qoOhUjd_aZawmJiIfCw-XvCZwoLfchWNuK4B64bYpwBnYW75TxvVbE3OVV1zzJRLH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کمتر از ۳ ساعت تا شروع جام جهانی؛
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی برای ورود هواداران باز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133273" target="_blank">📅 20:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133272">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G84qF8uwgJ-DqsPN3eL2MbCPkNT3luk4Mkvkq7PiXrQ6w8rK5UjWgGs7t-Ci4Q4-__kUqSyYq6XRHVBqoSwREbQZuy5BmycBowKhFlJqAppzmgkNqeLffn5jPtiEFmSbdxxbzf94bUIYdANiDNS6PPPPxWWGkCsrryi_8awWVaM_AUk40ON8-G2xVbWqUWq6aeK6eTep1Ob4AnXLZ4HYBIJBfY9Iq9fN480RExZvmVnnAsps05cfyINaiYrGgc18qmR5fj0b74933WK9sgCh33SbvX4hpV9T9o3SxaoREHXdQ_8jDCK_dQYBOHwJicmkuYmqdjLq_ME4rh3jy-7vvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشورهایی که هوادارای اونا حق حضور در آمریکا برای دیدن مسابقات
#جام‌_جهانی
2026  رو ندارن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/133272" target="_blank">📅 20:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133271">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgutFXRg0mfPKzhl2ShhQR841oGCLnqk_VjETOGqJUrGWazXseedMtAtj311lbTtvN0nebObYxp2MWYFl3Y5emkH0dmzxJZUO80mwI7pd9wIebqd1UjTvpSh-x5rWvhG5YxEq6le_sQxzwRvUUARuFYPBQ_H3KaF65OT5OxDmCAmP-zWnrsfMsRXgeUKIkUMRMMa3eoJWkGXh-nNXnxPmA_FeTA8RNXFqMaJHERtWCaOvDLfRckYitGlf3E4My8IqXYDct2BLpWBTzNOM5_bzwE3cln-lP-Rw3rcstJoex2bT1c79IcUDh2yF2OVGX9vndmhDdXaGOduPwfVVoX0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی
امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/133271" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133270">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/133270" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133269">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133269" target="_blank">📅 19:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133268" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133267" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133266">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
اوسمار فردا راهی ایران می‌شود
❤️
❤️
محسن خلیلی:
🔴
باشگاه پرسپولیس بلیط پرواز اوسمار ویرا برای حضور در ایران را برای او فرستاده و قرار است او فردا جمعه عازم ایران شود.
🔴
او به همراه کادر خود عازم ایران خواهد شد تا تمرینات پرسپولیس را زیر نظر بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133266" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133265">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️
❤️
محسن خلیلی:
🔴
برنامه فوری فیفا همواره اعلام کرده باید بازی ها برابر باشد و عدالت رعایت شود
🔴
در لیگ ما بازی ها برابر نبوده و این عدالت نیست
🔴
اینکه بگوییم شرایط برای برگزاری بازی ها بود بماند
🔴
انتخاباتی باید صورت گیرد که شرایط همه با هم باید در نظر گرفته شود
🔴
دیروز جدول ای اف سی اسم گل گهر را گذاشته بود و ما اعتراض کردیم
🔴
ما دنبال عدالتیم و می خواهیم بازی ها داخل زمین انجام شود
🔴
چطور این قدر سریع سه نماینده به آسیا معرفی شدند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/133265" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133264" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
رضا شکاری: باشگاه پرسپولیس هیچ وقت سهمیه را گدایی نکرده است؛ما مطمئن هستیم با برگزاری بازی‌ها می‌توانیم به آسیا برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/133263" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133262">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور باکیچ و گرا در تمرینات پرسپولیس
✅
تمرین تیم زیر نظر کریم باقری در حال پیگیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/133262" target="_blank">📅 18:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133261">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
اینطوری که فرهیختگان گفته باشگاه به علیپور گفته فصل بعد کاپیتان اصلی هستی این یعنی جدایی سروش و امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/133261" target="_blank">📅 18:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل دست به دست هم داد عواملی که نتیجه نگیریم
⏺
هواداران همه چیز را کنار هم بگذارند و بدانند چرا نتیجه گرفته نشد. باید تصمیمات درست تری برای تیم هایی مثل ما گرفته شود. تیم ملی؟ از سوال در این مورد باید بگذرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133260" target="_blank">📅 18:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 188 · <a href="https://t.me/SorkhTimes/133259" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBqokCg7jlJAvjQ0XcjcFhKqhwkBQVq1L1q1_hqJEmg7KBuD91SU4-KKvIQd_VGqg2deZiZQaQaMjwXYMNL7o03C1ZFvPMlC13Jibz5Aci-4s9yMRcHxbZeTyUjXXOfqRCMBv7DUGGoPUc6SjtHkXWImTgz4cDdbAhAGNF2_VuePAaW-p67GjZoQiNtVwMoFbEwRibR7RxCARn147VS4BeOeP9V3K1edliMODTvvTeSul8IkJIkjd-Ed4gjr9mevTQ7PthCtiz1pA00nhojIsYV7YMy7FgGgLVfUJVjZ3Owu5XHVpue5S9-PJMLIPQNAZbEMI5NvkDniDwRRMyGyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
رای دادگاه صادرشد؛ حبس ۲ دوومیدانی‌کار ایران در کره‌جنوبی و تبرئه ۲ نفر دیگر
🔻
حکم دو دوومیدانی‌کار ایران که در پرونده اتهام تجاوز به دختر کره‌ای در این کشور زندانی شده‌اند، پس از بررسی در دادگاه تجدید نظر، تایید شد.
🔻
دادگاه تجدید روز گذشته برگزار شد وبر اساس آن حبس ۴ ساله دو نفر از ورزشکاران تایید شد.
🔻
دو نفر دیگر هم تبرئه شدند و می‌توانند به کشور برگردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/133257" target="_blank">📅 18:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
لحظاتی از تمرین عصر روز گذشته پرسپولیس؛ پرسپولیسی‌ها با تمرکز و انگیزه، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133256" target="_blank">📅 17:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133255" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133254" target="_blank">📅 16:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
فوری| ترامپ: آمریکا امشب هم به ایران حمله سخت می‌کند  پ.ن خسته شدیم دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133253" target="_blank">📅 16:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
دیشب شب سختی بود .آمریکا تقریبا همه جارو زد ...امیدوارم حالتون خوب باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133252" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
سردار آزمون: حقم بود که در جام جهانی باشم.  من ایرانی ام و کشورم را دوست دارم و بخاطر همین ناراحت هستم. می‌توانستم کمک کنم اما دعوت نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133250" target="_blank">📅 16:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
مجتبی پوربخش از تدریس در دانشگاه آزاد منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133249" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
اوسمار ویرا جمعه در تهران؛ شنبه در تمرین
🔖
بلیط اوسمار ویرا امروز رزو و صادر شد و او روز جمعه ساعت ۱۱ صبح به استانبول می رسد و روز شنبه هم در تمرین خواهد بود
🔖
اینکه اوسمار برای بازگشت مردد است از سوی نزدیکان سرمربی پرسپولیس تکذیب شد.برخی رسانه ها هم مدعی…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133248" target="_blank">📅 15:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
سوشا مکانی دروازه‌بان سابق تیم های پرسپولیس، صنعت نفت آبادان، فولاد و... به اسگاردستراند در لیگ دسته سوم نروژ پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133247" target="_blank">📅 14:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
رویترز:
✅
با اینکه ایران و آمریکا هر شب دارن همو میزنن ولی بازم درحال مذاکره برای یک توافق اولیه هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133246" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🔴
رضا کرمانشاهی از باشگاه پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/133245" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSs6KjLfSK6J_Fq5ldfx3CtpK0qDPMUj6M1S8VDbzs-H0Iay6l8bnHNYrfkKY_9uDev-aT5-38EOJ-NpLrVLoFxx1vGxxKEPTp0NRwX7sZxIryzlnG8j61sJ7ykV3JZ1RExeR2Kv8xSjQ_ptf_fkgkcvY0Tl1mEvnu6Z6JKMhAePmDZB5qXeRmEq8G6-QEf4IWuaLWhcioXDF9dTYHa0Fy6-FrikgOZAl4w9Ek6bFIuv7RTN8hwagDg6qVKizGv5Wk4RduIvcxdngQOuyKn5o_D8ZXrmyWv5pyzXBw43ULDuOckpVJYipJPL1y70UKAOKAhBPGAiD_BWjhV28DwGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
امشب با دیدار افتتاحیه بین دوتیم
مکزیک
🇲🇽
و
آفریقای‌جنوبی
🇿🇦
رقابت‌های جام‌جهانی ۲۰۲۶ آغاز میشود، همین حالا وارد سایت شو و
دیدارهای جام‌جهانی رو با بیشترین آپشن و بالاترین ضرایب در اسپورت‌نود پیش‌‌بینی کن!
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
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133244" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
ممبینی، دبیر کل فدراسیون مصوبه تورنومنت سه‌جانبه هیات رئیسه فدراسیون رو به AFC ارسال نکرده و برای همین AFC بدون اطلاع از این موضوع گل‌گهر رو بعنوان نماینده سوم معرفی کرده///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133242" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
ترامپ: اگر ایران توافقنامه رو امضا نکنه، امشب هم به بمباران آنها برمیگردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133241" target="_blank">📅 12:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133240" target="_blank">📅 12:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
هافبک پرسپولیس به استانبول رسید؛
✅
باکیچ امشب در تهران
🔻
باشگاه پرسپولیس برای بازیکنان و مربیان خود بلیت برگشت تهیه کرد تا آنها یکی یکی راهی تهران شده و در تمرینات سرخپوشان برای تورنمنت سه جانبه‌ای که در پیش است، شرکت کنند.
🔻
در همین راستا مارکو باکیچ امروز…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133239" target="_blank">📅 12:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
فرهیختگان: آریا یوسفی، علیجانوف و صادق محرمی گزینه‌های پرسپولیس برای دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133238" target="_blank">📅 12:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🔴
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔴
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133237" target="_blank">📅 12:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-CTeeUWNrd93NdfyKfSXdcfpxdmyR0c6O27DRlDiYpjPu7gb2m-17ZYvEjrM3NyQiFtKJqF-DjatDde2cj2sdrKBruxsXaCZnuU3CPOxUF0fp0pe6Sv0kgbVM1-BClHxfWC5MjN_zGgs3sQiiXRd94QT2dyScEN2scX1Kr-BRZtAiIJNXFo1McOm7B4SAFOCio5yILQq7lPPtM5JGi8fymiD80i-i4LCRJdap4ZmnAkHITr9NyYgFiTQnlEUoiIyXuLfbmq7990u0XTUWmL-tywYOcSWrCEtgA7xRikQkPYSFX763m2pv6yHQVX214PtrE3jNCGH21_V5syFNi0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
منهای ورزش
⏺
یه زن ۲۷ ساله که معتقد بود با خوردن فقط میوه میتونه یه زندگی سالم داشته باشه امروز فوت کرد.
😞
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133236" target="_blank">📅 12:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
🔴
وحید امیری پس از پشت سر گذاشتن مصدومیت طولانی، به بازگشت نزدیک شده و می‌خواهد با حضور در تمرینات پرسپولیس به شرایط مسابقه برسد. او در تمرین اخیر حاضر شد اما به احترام کادر فنی، جداگانه تمرین کرد. امیری برای شرکت در تمرینات گروهی منتظر موافقت اوسمار ویرا…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133235" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚡️
23 ساعت و 55 دقیقه دیگه جام جهانی 2026 رسما و شرعا آغاز میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133234" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133233" target="_blank">📅 09:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133232" target="_blank">📅 09:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF8zutx2ZQsp0ojsUrUg_cGl54sI5zQRdqrE6belxHmn-i13JhF6P7gctAdzobKoaB1149D33G43cSO3fBf7IrFKtHsQu7obZdlC2Niy6ncaYOSZgcLCQIfIylEq2cF4-otrzLmYNpBTMIVjF9woBlTot0uEbDqgddN_R9pzfMJ8c4Uv2hg2Hf2vlG9gHuPgzcmf7eY7sSRhp0KCGOguhBTKnymOwtcgheuXGVeLsWOeU-k7yBVAiWys2wrBEkcv6XUlvVKYmw401A6qEdgipV8cBecoGxkB05QPnFSXqBff-06db-tu6EBamGzAn0adrGvQOwAaX3O2VqCl5QYC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین محمودی امروز صبح برای تیم ملی مقابل تیم جوانان تیخوانا به میدون رفت و موفق شد یک پاس گل بده
🔴
علی علیپور هم موفق شده دبل کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133230" target="_blank">📅 08:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
ترامپ در گفتگو با فاکس نیوز:
🔴
آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133229" target="_blank">📅 08:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABISBTNwaDRV7gAn_Mfc89mpNP8SsGvTFbPPtOlz6suhHucRxj1THa2dlunM3Sf6qdweV5S4pVX97K79eg75dtaNzRcVbGXMKAyS4PZx517BYCy9EnIsl4r10Jy3igwb3Sz8BpKHvVrNUt2PfSAogxxX5-nrx8aLwXUwnwa5Bw5hSuCTQ74cfunZg7U9yL9VEIKV_hBbUHdOLGIEp_xMdwY3857M8xbg6BCqPVOq1ZnHwfUDZfgpwFxJtG3b10eOdenHnKXrEkOJRHtzXQLjtOjcHAyNvSkLa38Dyn19lruHpXQB_tyBzGj04zTkxj5tw087xU4etwxu4xQkfcqiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیگ ملت‌های والیبال / استارت شاگردان جوان پیاتزا با شکست مقابل برزیل میزبان
🏐
برزیل
3️⃣
➖
1️⃣
ایران
🇧🇷
25|23|25|25
🇮🇷
21|25|15|23
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133228" target="_blank">📅 08:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
آمریکا حملات شدیدی رو به سراسر کشور لحظاتی پیش آغاز کرد  مراقب خودتون باشید
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133227" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚡️
⚡️
سلام به همگی صبح زیبای شما بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133226" target="_blank">📅 08:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚡️
⚡️
سلام به همگی صبح زیبای شما بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133225" target="_blank">📅 08:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADM9NpfcI6O84997iBToR_yJECOG7f3P0iuE7PnYp9RG4_EJw4liWilMysd987K_GYO_aDt3JCcl5E9vXfGljMnCoyMymmFhfjI1whXySRFXuBnTl6n7oIhvzXPWnFoS2zpONqXFPbGIAP-qj1T2SfIJw9c_r-NQ4F7XoFpDDot2xdFCgnMM9egxfb7K62o_HyphEtz5kU9ju29_TP5t-VPIxJ2Dl7xxH7Uw6-0tl6Klc-B_yDPTY_qRiAsItBa0gzKaV1z-wFnZfcb5p_9kmPQ8GzRI18iz_cjpkrujjT1ymzVtIyN8aH2j64NOEmUddF65o7G4TXgdhtPJqZvviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار چهارم از فینال ان‌بی‌ای رو بین دوتیم سن‌آنتونیو اسپرز
📀
و نیویورک نیکس
⚔
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133224" target="_blank">📅 02:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⁉️
💢
صداوسیما: برخلاف اخبار منتشره، تاکنون خبر هدف قرار گرفتن منطقه پالایشگاهی عسلویه تایید نمی‌شود
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133223" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=b7WcVBoIcWN9cgQJW0XsgqcAtJHRM3LIeDmpZ4qZ6U06jRjnS_RjM883QPKRm7pSf9dxnEMyfA3N_OoX0pH6UVArc3_ATfaQoosBBCvQA8nsI5w5yuZSMtIQ2gprTF0rCvYL6rJLzpd7JuDq95oEr4aLuH1chJ2iGT5URRa6bcrIy6yRTziBnupPeVMB0bOAqwXW00NiU291SguJ0OvIMI2v_glYL-6h_GtRKAb9K9nL7JgWDvJHRoMEPO2qyFr68FzZVcaqQ7LjPcxa192ko-SOzumNxhOn8dDiPZxXdT2TIswpcb2B8bC-a04ieN_z-NJ9WbocvMkuY6m7Rpw_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=b7WcVBoIcWN9cgQJW0XsgqcAtJHRM3LIeDmpZ4qZ6U06jRjnS_RjM883QPKRm7pSf9dxnEMyfA3N_OoX0pH6UVArc3_ATfaQoosBBCvQA8nsI5w5yuZSMtIQ2gprTF0rCvYL6rJLzpd7JuDq95oEr4aLuH1chJ2iGT5URRa6bcrIy6yRTziBnupPeVMB0bOAqwXW00NiU291SguJ0OvIMI2v_glYL-6h_GtRKAb9K9nL7JgWDvJHRoMEPO2qyFr68FzZVcaqQ7LjPcxa192ko-SOzumNxhOn8dDiPZxXdT2TIswpcb2B8bC-a04ieN_z-NJ9WbocvMkuY6m7Rpw_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133222" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
حمله آمریکا به جزیره هنگام
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133221" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز:
هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/133220" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133217">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/133217" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133216">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133216" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| منابع عبری: تحرکات موشکی در ایران رصد شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133215" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
پیت هگست
: امشب شب شلوغی خواهد بود،
سنتکام تاسیسات ایران را بمباران خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133214" target="_blank">📅 00:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
🔹
سردار آزمون: نامردی در رسم رفاقت من نیست، من با این بچه‌ها نون و نمک خوردم. دوست دارم اگر روزی مُردم با عزت بمیرم افتخار می‌کنم ایرانی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133212" target="_blank">📅 23:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
سردار آزمون از لیست بلند مدت ایران هم خط خورد و رسما دیگه به جام جهانی دعوت نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133211" target="_blank">📅 23:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
#فوری | ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133210" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/049d690382.mp4?token=oM9zqLqjRduH30sbEFf4pj8uRkUwB8AY4I4U-qku1t0grsn2rhuavkQLJg4x2WF1L3awiNW1gQR-mvc3u3yNa0cesIdIEiLo7d6cjz-WIyGVE-5PzeV4DTpKpIusStBSUs7nhdfjl2f-LI_9v0y0vXrBsjbvisUdPRSi-hWKWCrzn1f2e6HljDv_idueiKDysvB8Brip8PTpyQcBma4NgnliPbZkF9its7ERGuTM5hBOhCSnEAcrZvrumdTvGHz2BFOKdrRWC1Yq-v6akkMQzRBw-RRYD19AItITtW8XL2BR9iZQPNhemaA-VhQ0sJWZMin7Xga3W1Nf3hZkYFrJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/049d690382.mp4?token=oM9zqLqjRduH30sbEFf4pj8uRkUwB8AY4I4U-qku1t0grsn2rhuavkQLJg4x2WF1L3awiNW1gQR-mvc3u3yNa0cesIdIEiLo7d6cjz-WIyGVE-5PzeV4DTpKpIusStBSUs7nhdfjl2f-LI_9v0y0vXrBsjbvisUdPRSi-hWKWCrzn1f2e6HljDv_idueiKDysvB8Brip8PTpyQcBma4NgnliPbZkF9its7ERGuTM5hBOhCSnEAcrZvrumdTvGHz2BFOKdrRWC1Yq-v6akkMQzRBw-RRYD19AItITtW8XL2BR9iZQPNhemaA-VhQ0sJWZMin7Xga3W1Nf3hZkYFrJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133209" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوتبالی: مذاکرات پرسپولیس و هوادار برای انتقال امتیاز به مراحل نهایی رسیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133208" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC25NaZHMHAMSZasV23RdQTgP29qwR13AmdtwYNYmW2QuFyGC9HYzXTEef9UFHPkHV_-WjyXtXEeVPYioklPe3V16csCquV_2xs8MsuYygR-urUHsSyeeQJMRYvr4m7N39_ySHYZIqWuFoY80PQWBRbzvZkkaJtKVJG4-2XY6UJAc5q3j_HiG-VOlqjfquYROnaymzja5MupiqvLkp_81uJg8Olty1nDWf4QU1y_N3tu2RkGzFkEneOPcTuhs6_FXwj9P1IWCb7W8IiYiDQnd2eSWVYWxNkPW67ZJv2AI17K0Y6Zepfbm1g018qKt-IUUEJkJx0CoM-LoNVaBViHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امید فهمی، وینگر سابق پرسپولیس و فعلی نساجی: در ۲۰ سالگی به پرسپولیس رفتم و قهرمان هم شدم. واقعیت این است که چیزی که در ذهنم باقی مانده، بازی کردن برای پرسپولیس است و هنوز حسرتش را دارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/133207" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
