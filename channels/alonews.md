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
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-125360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhI5-p6NN1FCH-PYN4NN-pQC3lskKSsIRBLFxMb9-WmRQ-yPA0E-oR-4292PQJ5SVAd3zV-aAkYFbGD02Xw4YWXqvuwNzbdn9WT-ItML4-B1qcnYh6Pz4sF5Dq3EelFkvFSFOM0i7gd5vr5SD5Tz-EJuRTR-6Rg7fZHRiwR57bPt0hbTk7kqnyvCrVz2wU0dFov_F9e7SlozcS7XvI7ijYeVW0FOMQM-C-1HW1_38FMTwmORRswG_hVfejPVVRGzrivZTgGitqbr7fduYAr9zvUoxqc5GTP0cHH28M_aTFYLFDvRjb_f9YCc1lVrvxdhX-hH5lFWI5VfBuRztLFVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر و بیانیه‌ای که از دیدار عراقچی و ویتکاف به نقل از کاخ سفید درحال پخش شدن است قدیمی بوده و برای سال گذشته و تاریخ ۱۳ آوریل ۲۰۲۵ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/alonews/125360" target="_blank">📅 20:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125359">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/125359" target="_blank">📅 20:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پوتین: زلنسکی خواستار دیدار است اما من دلیلی برای آن نمی‌بینم؛ نمی‌دانم چرا اوکراین نمی‌خواهد ببیند دولت ترامپ ضامن مذاکرات صلح باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/125358" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پوتین : روسیه هم با آمریکا، هم با ایران و هم با اسرائیل در تماسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/125357" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پوتین : تصمیم ترامپ برای توقف حمله به ایران، تنها کار درست بود
🔴
روسیه هم امید داره این آتش‌بس به یه صلح بلندمدت برسه.
🔴
پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده از ایران همچنان روی میزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/125356" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخنگوی کمیسیون فرهنگی مجلس:
اگر جلسات مجلس به‌صورت عادی برگزار می‌شد، وزیر ارتباطات را به دلیل وصل کردن اینترنت استیضاح می‌کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125355" target="_blank">📅 20:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری «رویترز» اعلام کرد که ایالات متحده در آستانه نشست هفته آینده شورای حکام آژانس بین‌المللی انرژی اتمی، در حال آماده‌سازی پیش‌نویس قطعنامه‌ای برای محکوم کردن ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125354" target="_blank">📅 20:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdnadp_OZqQ5jrbAfctcWb2LMwDshmV3qEs5c5wLT1Z1mzKb4vitlRf1Lm9-sS9252sZUzLJGV_-KdDHu95SWP5D6U5pwAG6kDmk52EyN3MpvDME2um9bfPvI0Sh7BqNRd4KH7niE94VmtOdd1G3qaGT7r1XQRe-VczCaiiz-G8ZI5aYwhUhuR-H9CnjnNH1NHHUSR757lt3OGr_QMkXwLu3GJq5sLbKhXo0JCQ9A9ub0WWgBo-5lpzOhXU_wr-APJJpuUmCEnoAFdrsOrm8dpcEXSKQ_wcMs7gU4-X9dd7sE-zhaIL44ZmaB9wC6LFhfAB-Y2y1_qMgYX-HzKadMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طلا ۱۰۰ دلار ریخت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125353" target="_blank">📅 20:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125352" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مقام ایرانی به سی‌ان‌ان: آقا مجتبی خامنه‌ای با ترامپ دیدار نمی‌کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/125351" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyUpHZpgSh8kRCpg8DhP8gggioZX42N4uZZf9beTPKULbxF9fbKObjIluPLeS0Mek6nsYaGU64P4FusV-h50ewKA_JfhL64uantsmR9kkD4rW7v67IgtPsvUeIAJ4OdVhdhxkdAG6fdQFCv_KVodCP_V7JEuzFoEhpBRq_UHJ-0MSITSbSJf2OAEmxzP6dkhaQy1IDyMVMycfAggidv8Hy6i23hFuOf2OYb2utSQa_f-CsOd7SB_k0H-8AavQTToC81j6ktOEAJA50XO3UdsrDLJzuHVpPlRf2VMnefPWQhrJtHKC5RVkrWD8zaQJSyRFcMzk7AO3EbRHG8vyIeGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش اختصاصی وال‌استریت ژورنال، رئیس‌جمهور ترامپ از بیل پولت خواسته است تا در راستای ایجاد تغییرات ساختاری و خانه‌تکانی در جامعه اطلاعاتی ایالات متحده، بخش بزرگی از کارمندان را برکنار کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125350" target="_blank">📅 19:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
زلزله 4.8 ریشتری دقایقی پیش کازرون فارس را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125349" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: مقامات اسرائیلی معتقدند که تماس تلفنی اخیر بین ترامپ و نتانیاهو، که جزئیات آن به رسانه‌ها درز کرده است، یکی از داغ‌ترین تماس‌های بین دو طرف است و به ویژه با نزدیک شدن به انتخابات امسال، پیامدهای سیاسی در داخل اسرائیل را افزایش می‌دهد
🔴
یکی از این مقامات گفت که این افشاگری پیش از انتخابات به نتانیاهو آسیب سیاسی وارد کرده است
🔴
بر اساس نظرسنجی انجام شده توسط کانال ۱۲ اسرائیل، گادی آیزنکوت ، رئیس سابق ستاد کل ارتش ، برای اولین بار از نتانیاهو به عنوان مناسب‌ترین فرد برای ریاست دولت در آستانه انتخابات بعدی پیشی گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125348" target="_blank">📅 19:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtFuTz5UuptBeGrf907RJrWWDXhUUoZtnx73Lj1rUTDoB9sMJLFEa_OmyMKgncT5Hmrt3B4OOGYZH6dXsYBghUfaBdbNrQ5QK_hl7erGVlz2VU9wJOWQXxzcX332zq1Ar2GdcGuD2NDz9D_HvFKmCzk2Q0KSDsTtjZcCwq7BoOAIfCqEdduDjZXrXPGG_abvaiOrB7nPYjpSpqdxS5ubFfGXw8OG8vXfwQ3jafwga9R7m55SN7-9pA_VekopxRwz46u9Jkj6mEA-o2hwMg7EFqlwjheoNx1r8zjq702zdmpvQhldkEDxH5y-ABbnaksP-yXRkxiWNFJP2C67ugDSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در شبکه اجتماعی ایکس: سرو می‌ماند ولی طوفان به پایان می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/125347" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: مذاکرات متوقف شده است، آمریکا اگر توافقی می‌خواهد باید فورا ۲۴میلیارد دلار دارایی های ایران را آزاد کند
🔴
اگر محاصره دریایی ادامه یابد ما [از طریق تاکتیک‌های ناشناخته] جنگ را به دریای سرخ، دریای مدیترانه و اقیانوس هند می‌کشانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/125346" target="_blank">📅 19:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/ فارس: ایران مذاکرات و تبادل پیام با آمریکا از طریق واسطه‌ها را پس از حملات ادعایی آمریکا به کشتی‌های تجاری در جنوب ایران و ادامه عملیات نظامی اسرائیل در لبنان متوقف کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/125345" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پوتین: اگر در انتخابات قبلی ایالات متحده تقلب نشده بود، ممکن بود درگیری در اوکراین رخ ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125344" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125343">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/125343" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125342">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125342" target="_blank">📅 19:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1pYGhUohQWqQISQxxJTsRjcZb1tIiiobPCPbzD9iOtq5dCKVMU1Nlm5KFMhpN9L6NTZ4gjAG86xIFvetCx0z53IjRLMajR2eoeXJb-yZ9tKakD1-lYXs-R2Q_etH29kLVzOrNQvU5OxUUDjoLHibjxT5u-XOvb1R8j4m7qx2fNcgE65Wlr8joCZtmnnynotzIQ9KpF0P0OlN1oE9NjXCQiHR-Wwg0Ei-fyU-IOHeIv6MSH4YgWC55XB3CQE5dl3Fc1PPQPmVC0N-6OL_zxtHWTSOcmmDspYBH_hzsx5tO9ZcYK1e9yD2dT6pMzRhCIPwl_N9vgZxtNkDQyUaV0Y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته منابع آگاه، ایالات متحده، مکزیک و کانادا در آستانه از دست دادن موعد اول جولای برای تمدید توافق تجاری خود هستند؛ اتفاقی که راه را برای سال‌ها چانه‌زنی بر سر تعرفه‌های بخش خودروسازی و سایر صنایع باز خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125341" target="_blank">📅 19:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ez9hAuy_iYvh48O4I9JWtmygqkoUIn7VzRL-bw-CWHuMXhWgfUclJd2cAB7LVLyQhXSk3JEGm8ppXeM4vCWuiGpOKj1qY0vrDTI5DsQU_GY93lCF0IBhT7kICVYgfFZWPgqHsd1u85dJ-JYcagKFZOZcEsjwAqH1uoIa8lzWuAXQqOqTZau_YHbJHtyO6ryhkX5neVgLZ3WMh0FHX5yCVM1v4lYjtlemZjfgvq_dQhspTYCxsI6Sy-ywIkFXFAoefTQqfz_4IkpZH-9siYxTOqC0GOiq6S2ok48t4IMqR_rUrZc6KQ-3US5XFvKAw9J8GTUlrcp_ufd-QtEmT9bZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نواف سلام نخست‌وزیر لبنان:
ما موفق شدیم به توافق آتش‌بس برسیم، اما متعجب شدیم که سپاه پاسداران ایران اولین مخالف آن بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125340" target="_blank">📅 19:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125339">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125339" target="_blank">📅 18:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تحریم‌های جدید آمریکا علیه ایران
🔴
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125338" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_-Tf-xa-mJHDRiKfLSLUyHlhWttEoUv71e_tCYImK6Yylc8BIE9HiBcY2jDiqK5nqVNUKqVfjFDMs5vuuTSVGwra3HEwWwB3DRjJAlvX4zUAXKRT2kXwu7pQ6GVbrbge24mGl-PU22Th2yEzwHxeWaAcs53bWfqIo6h7-25zR8hBdaEEu6YruQb1BsF9ieu_2Nm7hzARtJCul0xOed-aelaz3Eh5ccoZ7dVFVYV9BldKv42E7wwyA_GzSRvqEO2GEn2pThukZbQrQx4YEAot0Vz4u8Nm1W5TZmXOgJpSoviWa7YepCjOl0mAbfVrJt40Io8MvD1hkCjG9iD_9tutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهر نیویورک در پنج ماه اول سال، کمترین تعداد قتل‌های گزارش شده را تاکنون ثبت کرده است، طبق داده‌های جدید پلیس نیویورک.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125337" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125336">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125336" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhGjq8P2oHGJi7KoINFX4S5u2hFpnTIhi5M6qlFZOZ3QtrjLbWncbAHQdC0QFukzAxaZUKbfrFy7gXfAZKBwbfUY1Fb8q2DU68xr0LwSe0_OSFBziMq9iSDk6K5ciLCOfOvWtl_-dx9k9tuWtUQARPtSdu9Xn_YM958mc7ZWSXs-rKxe2OaYOVdXde-rTNdoUNY3JUJE94jbd40CNXB3G3HW_scsLAGoc8a7m3Vp0RkP33KmIecPKpwyocC97-kuzkl_q4dNXf-UoGwvUdPpYzUscBLZDKTXfBZijZ2PBPvYZ1ie4z3R-A4GDSBTcONZ7f2bb5mhHcGgRCQJFdATQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شجاع خلیل زاده: امیدواریم فدراسیون پاداش بهتری از دور قبل به بچه‌ها بده
🔴
پ.ن: سری قبل حواله خودرو ۱۰۰میلیاردی گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125335" target="_blank">📅 18:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_ss9ter512WEIuR11TLEjSlB6swni0euucl98O4yJpk9iKRzh8fpb1hjuSa5FbAu3DK-xHm4gxlSi9j3jJCpz7AqIr5ZkPjQGfIX2tXifmY0Cr-0spuZIFFMkrMyw6WnwzUbCNWAFSVu7dssOQL3MQWfaPM1si4FgYrq1QGI4BF8yx2b6wcRAzS0ClMNVBHbneGmUEUymuteAscJzw6C_FFmd4kcNmnhjU7UkPwR18HvEgv9et2WUAWSIvGP26HE4kwDwFyffKWzhwiQMbw3PZJwB0Wn4DWrERLJGt0unMWpDq1QRjuvbXwWxHkyaDu1OLDrgK1WoS9G5FUI3kakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125334" target="_blank">📅 18:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iayPR4DXfL9tXd3ULXXZEq3rBJKY3HtS6opreIINMiPzlmKseRknfjAQ_qTfenO1Y5QMQ396lwI__yzxLIojDigAKHXIIKqz1rSRUYitoiaW-TYLCu3OOivAzzz7c34ABOrOrWGmbuJsaPC7iFdqxBAWokzzO-1NvFfzGiaklL1m_Y19ZP5tWMCkx7VSILKji_K8CKy7SpIdrFBKtVQHGU_IbizWL5tvslVAup2bTupHMY-petENIM1xquB5WC5F1P23vzfsEFpG_hv9OHVUA-9XD80MjLI7GBphQXRIjfmElBDKlzLHIw32_gIHKuv82xPl6Rqekz0bbS7uMojaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین به 60هزار دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125333" target="_blank">📅 18:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNJbvGjuKbHHuUAEDy6Y9xzFmbwB-yyNW30yUdoUsSC5rMViDmp_mB8HOdNv8rclN1SGY3Pob4WfahR0m35zFxrxOqiznJg0vtS1_V7k1G6PZK_3i6zhVl_jUWPV6dNFK4RyPtcdBYBq4R2P2UvVvcC0a4MYzyb-Et8-eynFboBb06m3-8LMhllXpiUGs3UkTR2BKKbRVJRJP1gDRIJLiEo_JzxBUChIcfQU_gvhNMyhyt1MzgAyCwxcBj2vVTMdTcfqdQqi446mbx17WAI1bdMy3azTG7pYAT7twWn_Lj_lGMy-GA_qxWaKyHk0TPSCW6p0MQ7CHpSc8N1CXzWfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلی مارکت:
صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسیده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125332" target="_blank">📅 18:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125331">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/125331" target="_blank">📅 18:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125330">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/125330" target="_blank">📅 18:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ردیابی دریایی کپلر : چهار نفتکش با پرچم ایران دوشنبه از تنگه هرمز عبور کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125329" target="_blank">📅 17:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بازگشت به بازرسی از سایت های هسته ای ایران، شرطی غیرقابل چشم پوشی پیش از هر توافقی است
🔴
مدیرکل آژانس بین المللی انرژی اتمی به الجزیره: بیش از ۸ ماه است که نتوانسته ایم موجودی اعلام شده ایران از اورانیوم را راستی آزمایی کنیم.
🔴
فرض ما بر این است که مواد هسته ای ایران هنوز در همان مکانهایی هستند که در زمان آغاز حملات بودند و تهران نیز این موضوع را تأیید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125328" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گروسی: ایران و آمریکا نسبتاً به توافق نزدیک هستند؛ البته این را بیشتر در ارتباط با موضوع هسته‌ای می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125327" target="_blank">📅 17:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125326">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125326" target="_blank">📅 17:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
جمالیان؛ نماینده مجلس:
کشت خشخاش در ایران خیلی زیاده شده. حتی جاهایی که قبلا برنج میکاشتن؛ به جاش دارن خشخاش میکارن. اینطوری همه تریاکی میشن. یکی یه کاری کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125325" target="_blank">📅 17:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ZqvSI0rPJ8yqgAgXMve4aaJcaibm92Qdl_pU4S5dG_cC9a8ukpuC2YriVanzx0FesJao8YJf_SYobqiTamqGivIZzvKGFi35X4nnFPYnuCjzEufoUTuQrIVJPvqZdNN2jVZ4jevmLGSg3nGqKkguVpeXRc2dEpv1T29KrC1slV6NBm0QqU1JiIC6qlE9ok-SoS9MEtDEnsmToMMpXq1zPl9qDUQWn4CLTRL0Z6GXAq_Zm1CX9vqLhLUxwLg725boLNM4dgVAh1reTvRh5gxsdnpQ4T1XDcv6OS0bftfQom1XKUqcTezBCL1oX9ilGfMb9WPeovHMfaMhheaC0hUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وخامت حال میرحسین موسوی تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125324" target="_blank">📅 17:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125323">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125323" target="_blank">📅 17:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhzby0e1f-x8hMd3WKtnqFApgLs0YRJyHnH7UjrDt-Dwnh080zPi3rGLen5_m4IIkq3jVMoP15l1M4dxvyAsgecUjSuKjplPig7GuKBdlIe9sVRSwkhvE82VCDe35jeKYhir0Jcw2fkQaE2gWsFHr-58r5Bsu6zBv3Smc9_jPq0jE9fau9ffz_fb9MXJfUuihmHlOg6oAII5J5pJdko9C_Gs9LZarUaHuC9v0G4ot8kPFgYylBWC45L0GLeH_f8RlTJe0TVIXOqa6_hzy3lX3jgcQZvnEOctkOkeImOXFVHc-ei_5MpiQN3bKZPbfiBK4xEGZBhlTXdt9SYoI1d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
خاک میخورم اما خاک نمیفروشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125322" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125321">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125321" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJLLUTy2sin-c3J9LuAcr9GIzChUlbaezkH2p_z_N0BlWZ45o-c4h9QMTCB4KIw4EkXQPCcywBLk4yFGRYnwJktySC5jQDjhgaIXxw9I-6Ro7lMtkp7LaGoYiSNRCaLv-772SOSWH1IAH6Wf591V9nbet0ekb19tOdPbY4-wyxkkdPRpKPRApsrkexE37D4QqDxooU4OJAZTt4r4SeH8K_ZGOBnTtlO9TEPiYBXf0g3FVrUQcM7f7z6L0mKUzDz7AX2eZAv1GJKfk7UtudNIf70Fitq2oJ2mWByufNmlJff_bjCitpjLc2W6WBvemO1SxlucopWFzdHhd47fPWN72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی آمریکا حمله نکردند و به آنها شلیک نکردند.
🔴
انجام چنین کاری نقض آشکار آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره جاری علیه ایران را به طور کامل اجرا می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125320" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گروسی به الجزیره: ما بیش از ۸ ماه است که نتوانسته‌ایم ذخایر اورانیوم اعلام شده ایران را تأیید کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125319" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125318">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125318" target="_blank">📅 16:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125315">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125315" target="_blank">📅 16:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7JlToKX7E1SjMKCsgjCguoF0XCkhS8itGSeq3CFqhExsbe-pa1qdAVoXpX1Ph47U-acD_Qf6qV5q-wnxxfp1P2-LV-7eDYYy1PQig7h_n7bUZDTMsUUyGj1AU7v6gsVWbSG8PGB51ER3IY0Yl29BPVYzK--G0djp_O63rd_b0c_mOOUQLR9PDTzby7Qw6RxBoFuyPaZbR54FciDHmDTvSS4qmAzh-HoR7DMJkyByi50i5gE4KiYWCuxxTiHi5m-k5A0b6xiwfBEr_OOYhub5en2iyiAfthzghrkN9agymZvIBBo6i3iggt50PbHM_v_MlhPExY7-f1_PVbuJeTMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لبنان :
- سپاه پاسداران ایران باید بفهمه که لبنان کشور ماست، نه کشور اونا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125314" target="_blank">📅 16:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=PP4V24z0IG-fpCZiFJXdWIU5AICa4wxBeWRPApOoiW2z42uKMjUrpa6csHx5gqeei5APMgdlWKLTNKA_Nc72Yj4Y9ixGnRNe45VRbUI7uiGfepDmTCVqftnhvrVfj7cFvOq_ooFZ_RNOMTaqKObWJFTNQr1YhZ9ZuRKQT-vWWq-KnmHi6pklvMcLvZJSYdz-VRXL1GHjzl9Lz5zyf64x6CCSAF2qIrgmc4ofWQ4cJ1lHcUH6yANfCAQmcMRPaEGLTQr3C3JgTusdsrvnnKR9V_SecPLwjJ0BMmYe9kk7K9NPcrlOFdCiSh9fweo-F7zhaTFX9cUOWerW6p9MCduaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=PP4V24z0IG-fpCZiFJXdWIU5AICa4wxBeWRPApOoiW2z42uKMjUrpa6csHx5gqeei5APMgdlWKLTNKA_Nc72Yj4Y9ixGnRNe45VRbUI7uiGfepDmTCVqftnhvrVfj7cFvOq_ooFZ_RNOMTaqKObWJFTNQr1YhZ9ZuRKQT-vWWq-KnmHi6pklvMcLvZJSYdz-VRXL1GHjzl9Lz5zyf64x6CCSAF2qIrgmc4ofWQ4cJ1lHcUH6yANfCAQmcMRPaEGLTQr3C3JgTusdsrvnnKR9V_SecPLwjJ0BMmYe9kk7K9NPcrlOFdCiSh9fweo-F7zhaTFX9cUOWerW6p9MCduaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125313" target="_blank">📅 16:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان به سی‌ان‌ان : به نعیم قاسم میگم، مردم لبنان، مردم تو نیستن
🔴
ایران کمکمون نمی‌کنه
🔴
سپاه پاسداران ایران باید بفهمه که لبنان کشور ماست، نه کشور اون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125312" target="_blank">📅 16:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت امور خارجه آلمان هشدار سفر برای بحرین و کویت صادر کرد و از شهروندان آلمان خواست که به این کشورها سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125311" target="_blank">📅 16:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccd93e861.mp4?token=aJ4ORk9P9fAM8X_tPms58h0XZfJoGX45-VytpN7wWINx_hlNCFhb0WcG6cnabt7C0Xib8p9a2G4zMsGfBTQvBK4awpB1ARJpRAcBPO3Xn5hYhsJrUp98ZlGYNlAF85jzVWELTZFjN7KdUr0SG-JtA2n-xt2aRBMQEmyH76nyQ516Mef-_jh5vTYCcJDX2di4leNbzVMqquVIFpIiSERtZxl0LZ1cA8FksskkoYe4jbZ44XyokgS0xyhzhgDAAX1jMfOesKafYrOTXKQwrK6Yy1Lii8ZoAEpWxIHK_3yoybF8Qs54G2DwSZu7o8Pq-ViL-2HUCudSa4No2xwuT-qXpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccd93e861.mp4?token=aJ4ORk9P9fAM8X_tPms58h0XZfJoGX45-VytpN7wWINx_hlNCFhb0WcG6cnabt7C0Xib8p9a2G4zMsGfBTQvBK4awpB1ARJpRAcBPO3Xn5hYhsJrUp98ZlGYNlAF85jzVWELTZFjN7KdUr0SG-JtA2n-xt2aRBMQEmyH76nyQ516Mef-_jh5vTYCcJDX2di4leNbzVMqquVIFpIiSERtZxl0LZ1cA8FksskkoYe4jbZ44XyokgS0xyhzhgDAAX1jMfOesKafYrOTXKQwrK6Yy1Lii8ZoAEpWxIHK_3yoybF8Qs54G2DwSZu7o8Pq-ViL-2HUCudSa4No2xwuT-qXpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاینده‌رود اصفهان پس از سال‌ها احیا شد
🔴
گزارش‌ها حاکیست که پس از خشک‌سالی‌های طولانی، جریان آب در زاینده‌رود اصفهان دوباره برقرار شده و رودخانه احیا شده است.
این احیا باعث بهبود شرایط زیست‌محیطی، کشاورزی و فضای شهری در مسیر رودخانه شده و مردم محلی خوشحالی خود را از بازگشت آب نشان داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125310" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4AtYgGTb_ZptNLZT0vTbgJwgju8ttQ3fMB4N7ER1pKYpASjPIT7od72FfDQBcZX5GPVVR9a55W42rzBXqhRAV8bQko4QUg_WZfJEC26ga1-7YrvFrGy8fkWUYZApfNncQSQypKoVFsWy02_Osf-xsM8pc6IN8wYjkUKhuDCpv2CGeYJlt9z2ZaHOllThThru2OQ7qFlT3AxHn2IzyT01-F-lHHcoP4QJOtUITog2N2ttZsPJsCJqkTsAyuKQZ1o6yzTQ8ifapBjsTNfnFloWGVeRY4Csa_3mxio_I36EnsnoNKjostF5WI51EVFhrNPtNABSQNG5B0v2-JCvsqftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور لبنان : به نعیم قاسم میگم، مردم لبنان، مردم تو نیستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125309" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enTPmz-XEcVpE2yMVN3dKIklJPy98vAud6i32DAfxxPv9HnL8SCDlmLxmrZuH0p11bATogYulwC5f2dKS5KcxFak1NhKMjsmW_tCCqVD9rzkJ2P7QBq06LtF3gG1QIoHMoyhgU0H-1LbUl2SwJdxwB7bZCu3hYxOlo01TdHzQ_SX8kQf8G1hOHLVjrYRSTw7rXWo5gVe4TlyHQueTo9l4Cc8bZFoD6coML6GhTaA2a4twT716pPHh5u4fbntMCEwrDwIAlnknJsFHWDUYWwl7OAxVR1v8MPOZ4w9CrqxZIZJqBR4vaYNjCmI__eeu6iLhBb35DYkpYdtNa004p5j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
شهریار مغانلو:
آماده‌ایم که هر سه تا بازی جام‌جهانی رو ببریم و به عنوان تیم اول صعود کنیم
@AloSport</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125308" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962d58e87.mp4?token=lWI-y9vwmEhiGzNbCrpd2Ux_lMs6zIi_FFnYjWYzm3Yg9UqqIUUt4E-BO2p9Dp9__woFBgelbftCwjZu2Dvb82DGKcWZtxa6QwAHBwuEc8r5Val3D4Zbhb2AzIDmC6a7toz2d9gZtjy5XGsjvdddA3kzHhCNtl_Phhfa9fADFKieclmfKks_CM4uQoknVNhDBerAcam-gOC97nIUw01ygKpoECOO_vZS6PGyTgb2xqQCYY4nxbrmM6GHLsr3oWj6GecjHXzERvwdoZzLDr6xJk_xflatjcPsrH7GI-OdCJTJX5bcTsK-cwRazxivk9-nLCBZ8BzGG6vfeb-dH5EXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962d58e87.mp4?token=lWI-y9vwmEhiGzNbCrpd2Ux_lMs6zIi_FFnYjWYzm3Yg9UqqIUUt4E-BO2p9Dp9__woFBgelbftCwjZu2Dvb82DGKcWZtxa6QwAHBwuEc8r5Val3D4Zbhb2AzIDmC6a7toz2d9gZtjy5XGsjvdddA3kzHhCNtl_Phhfa9fADFKieclmfKks_CM4uQoknVNhDBerAcam-gOC97nIUw01ygKpoECOO_vZS6PGyTgb2xqQCYY4nxbrmM6GHLsr3oWj6GecjHXzERvwdoZzLDr6xJk_xflatjcPsrH7GI-OdCJTJX5bcTsK-cwRazxivk9-nLCBZ8BzGG6vfeb-dH5EXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
آخرین پیام جاویدنام امیر عباس رضابخش ۱۸ ساله، قبل از کشته شدنش در همان شب:
🔴
«داداش، اگر برنگشتیم... عقب نکش. عقب‌نشینی نکن. ما برای این کشور خواهیم جنگید.»
🔴
او همان شب جانش را برای ایران فدا کرد. یک شیر واقعی، قهرمانی که هرگز برنگشت.
🤔
عرزشی حرام زاده، غیرت یعنی امیر عباس رضابخش نه تویی که اسلحه به سمت مردمت گرفتی و ادعای عدالت علی داری.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125307" target="_blank">📅 16:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه آلمان هشدار سفر برای بحرین و کویت صادر کرد و از شهروندان آلمان خواست که به این کشورها سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125306" target="_blank">📅 16:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کیر استارمر: ارزیابی اطلاعاتی ما و ارزیابی کشورهای دیگر عضو ناتو این است که ممکن است روسیه در سال ۲۰۳۰ به ناتو حمله کند.
🔴
اغراق نیست اگر بگویم ما در خطرناک‌ترین و بی‌ثبات‌ترین دوران زندگی من و زندگی شما قرار داریم.
🔴
اولین وظیفه من، وظیفه‌ای که بالاتر از همه چیز است، حفظ امنیت کشورمان و حفظ امنیت مردم ماست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125305" target="_blank">📅 16:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نیروی دریایی ایران اعلام کرد که ناوشکن‌های USS Truxtun (DDG-103) و USS Mason (DDG-87) تلاش کردند بدون مجوز ایران وارد خلیج فارس شوند و با شلیک موشک‌های ضد کشتی مواجه شدند که آنها را مجبور به بازگشت به سمت دریای عمان کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125304" target="_blank">📅 16:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e85199ee.mp4?token=b7ZRhAprPjpfWhIgQDlXD8FBCrDVAjCE8rEiSfiuWVZ7g8Twjp--I2Z6PrMP4OgctU5apW2ZRBWUxTCjeSz8gW_WKs_rsRZfzjP7UV8LMEKkQlV7lLADVkMoBfpmU-LU4MwzOK4N1XGCwN4zPB-qImYwRwgPtGKynBYem3Rpm6bJMM3T_o1u6H7zsPTw6hStyHM2S5XmKs6VgtuJ9An80CvuravyNMuPg807OqzAxBIiCvdsx8MeQ6gYZUQGtfskIoXpwSkuOoBpSuQlJkz2cZGOIkase-sCtBz3JtcJ8rQBjJVE3FW8qls5uGyeKMNseQTTkLKKgCWjTL97dyD0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e85199ee.mp4?token=b7ZRhAprPjpfWhIgQDlXD8FBCrDVAjCE8rEiSfiuWVZ7g8Twjp--I2Z6PrMP4OgctU5apW2ZRBWUxTCjeSz8gW_WKs_rsRZfzjP7UV8LMEKkQlV7lLADVkMoBfpmU-LU4MwzOK4N1XGCwN4zPB-qImYwRwgPtGKynBYem3Rpm6bJMM3T_o1u6H7zsPTw6hStyHM2S5XmKs6VgtuJ9An80CvuravyNMuPg807OqzAxBIiCvdsx8MeQ6gYZUQGtfskIoXpwSkuOoBpSuQlJkz2cZGOIkase-sCtBz3JtcJ8rQBjJVE3FW8qls5uGyeKMNseQTTkLKKgCWjTL97dyD0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدر اعظم آلمان مرتس: اگر در ۱۳ سال گذشته هیچ عضو جدیدی نپذیرفته‌ایم، این نشان‌دهنده شکست‌هایی از سوی اتحادیه اروپا نیز هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125303" target="_blank">📅 16:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrM1OVm26_5_-C6dFLmfg06rkJ2iPmlpGP1a1pDfgMWjnTOkWeyWMCjlPHUFubCYmGE2wI2qAkfYZ-olOPeXROtGyvJYqaPjR_4EDmMB58ktg0kqKa1mQUWEuTBp54rkWgkZ257jqiU6wgaiIPcGBG7GBsIhIUKdKEx-f4l83IpNcHPQqEwfbwJwM31WmfMMk-aF_jJAUflRNPXxBsYGWTgBtrzqxiAW7pdxnquH-hZXeBnIaXomQCatgwmr6Z_hE-an5LUyLFNmpIxJt7rqoMXjBWBbkybo2sUZyEF8m1JRNGgKhi5iW7ncO58Non_v3P9T2iAUey662BFXY4QRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پست هانتر بایدن را منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125302" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125298">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5GTLA4l56mAcSCI54vMwBFKr1LfMC5ZYPuNkg_orZwAAHy0zYpL3ruMJpYdrnksxHA5Netj8XGU8W-g0VUvhQnvM1uz2FxFRB1B9750CHipy4CxXXBB4DkoAkg99iItXWpumrJdNK-riC7uFq_SxcRNwIzxl_JqfMKFPmy4LPuMme-KYm5dsbY37l4B3n2QR0mCqguU3K1sHOYB5clJ76SMV3e6L7BpmKZnNb244DfJyBiyzLOXjm10hZWtzUU26wU6PMNJXA3XtP0xESzQUo3La6SUkIhAqFA1QEfoLTYvZyytprrtEbL73-tPFadoovInjPVbfc4eCiFJ8Jfxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_dyp3jQK0qAuj1fEj0RJagVNyBkyOnFx983Iw8FLz-jkyqfy8-hXfhave9EnNIOoD914QBjah6jjNGG9rp-0voCZ9vZAw-N_hGgdgqH3v59pKyXEuckL8ygdsd3SPiiN-3qMsNke7b6_-WADnPtQJrIcDNY6B_D5EBcBeYJsbaXq4nek0pe45FhdBAeDfkWTUe1eCXm0CbabGWNfJojkKMIgnLz6dlxdfJL_3iyLABwQ8uMYVcV7Wxz9gVPf0yPv7JJs6r6rob0E_htzdm8fwnMXuN7YaUajunpOQFNfqo_Fv6P5dxfNAYaI6_2HvSFTEfkmD9s_yUhy7Hw3qacFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GObNM9GorqcC8cHTbvLpR-V21-gn_dc7PbVuRtSBSqJY3unrhm0ytEmDIMcDmngPcTIwAXlqrbpDH0RQ_nr-ioSvmF-OkTZ3aiJqm1heCBWTpQqChRwByzr1M53iKM2SO2fFXgzd3ntcfZN7xtBT9GVcFCD-Z0MIds1WSGYvC-rq1P7rwBzr5MA_C_fdFb2Ao_qPxKRwL4-In4QiDi8E09kECUAGUP29zIqeOHmQz4Y-OPqKCMMMjwSTi5g9MioedlCFYwgz5asxvzdlqpw9mM7qAYbaSbfbPpILp13X-J8X3TbSfSXrOORGDPV_nq-TFoNCRdH5evceZzP-XvYTNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
🔴
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
🔴
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
🔴
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125298" target="_blank">📅 15:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125297">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سنتکام : کشتی مرتبط با ایران MT Davina رو تو دریا نگه داشتیم و رفت داخلش برای بازرسی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125297" target="_blank">📅 15:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125296">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l02ksV__Q_krvkBCWN4X_NSZnlhQvZPZzhRNEL3T9HiRCjdOPkJuQrpCSizdpB_owl4qdPM_tGFF37JSzq-FXNcNXXinEZ-Rq5ZAel2QOtcaloQieD_ZtTA6buTn5Fl_O0O3WPM6i5p0F0L8sIo5cLpYRt0b9sTPK6IOUP0RIQV66kBPhteZp03AjsxMZ2hohmj8Nf6BLGEFyieBdU2EKEZRwnRmO_HGZ54DOsoT2SNt9yncWEb-m6KJNce_DDwJlJUTpNerSdUJoY9YUxZ9Ip-OPOYo5rYU-97kwnUgxs0fGrjXRoigewrFVtXBm_4KqlQWO9JXjlJClvwkzqBR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125296" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALrtG2bsJf-4ObxKuJAGA2syc0tHurLBKj5C3T34bbkG_LFjn8m41KMUtOYsvVxOwYqjUgYH3rX7mdZmJzGRSGtv_9uzx2QiviwzZqjsVYoFQLx-evkrpji9JNBE7Ilo__VSqCWFYt8gxuFeEvOnlZ7WssUlH9pZRkr1e9Ow11VUbhSJxJ3xkJ708BVS8WH_OOsl9weGEPGqPCUd0zCdZhdH1feFaDF8miY_aTnKUldZHubAkO1HKKKHm-9YuHLVbpdBtBWwYXra8uLtJL3WGSfHiBWj27kJo06T0rIfibcY1g7RWOQPwkqsyewzVphggZi_KRtilDU-kXAX0AgvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVopM4-T2TaMAjBsDICnQlh-EA5K3Xb6xqi39oLOXggxxRCI1AflAeQwtCifncjvEwC_QfeuKk_j1KeRZmWffbTBkAMTx4yq48mG4qfRUKcBMyVtisDez8vi1EN0pV04-NpXwZr_IPATZ7NsHsgkNAm4mEzOh-oHlpgANJQ16h_1G0_QlyVFdSJep47ffvovNJRkSKZdz1xizQI1L3xV3NoJ0lbKfAt76X6hAINgeoEgNKoE0SeSSGYX02pGABmxzQ2maw8OI7dMs_nQyjGjkgSp-TqYnMpUjjA0wPqKKDnusTQTbLeT3MTnWM1d7Ynsacfavy6OdnZ80I06SGCQ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fcf02896.mp4?token=hrc_E1kwttaAC0EJ6QbCDypCnD-g_eAXaSGVEd-Mg3e26Y12E4-8YflE0LiN9NtA_hVuJ1dhlB9L-6V2x3HfzsxsncqGzA37Doy8_xEH0v3dynRxfh4f2GcJ-BzLIGiYKybOl2TJ1I4Oz-WTciTEne_MW1ZkV8zV11PjklZd9K-LgU2dXWcLuXPZY7OBNLDRX8WJpmTt9Ckq4F_lOredYVHZCjYK2tdRs0zIcMh8veUgG0MbUelMp0rhWZVNVzfeOGLfuzFNNQKJaWNHzRgVRMxHwvMXif-Z0pYnH3knJ2gopNCcxq0-VmSK-X5CjQYJyYPRm5CreyyuI98BnvF4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fcf02896.mp4?token=hrc_E1kwttaAC0EJ6QbCDypCnD-g_eAXaSGVEd-Mg3e26Y12E4-8YflE0LiN9NtA_hVuJ1dhlB9L-6V2x3HfzsxsncqGzA37Doy8_xEH0v3dynRxfh4f2GcJ-BzLIGiYKybOl2TJ1I4Oz-WTciTEne_MW1ZkV8zV11PjklZd9K-LgU2dXWcLuXPZY7OBNLDRX8WJpmTt9Ckq4F_lOredYVHZCjYK2tdRs0zIcMh8veUgG0MbUelMp0rhWZVNVzfeOGLfuzFNNQKJaWNHzRgVRMxHwvMXif-Z0pYnH3knJ2gopNCcxq0-VmSK-X5CjQYJyYPRm5CreyyuI98BnvF4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ‌های هوایی به منطقه جبل الصافي جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125293" target="_blank">📅 15:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
منابع العربیه: دو شرکت وابسته به سپاه پاسداران قراردادهای برق با شرکت‌های عراقی امضا کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125292" target="_blank">📅 15:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125291" target="_blank">📅 15:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از یک منبع در هیئت مذاکره‌کننده: ما در این مرحله به مسائل مربوط به پرونده هسته‌ای نمی‌پردازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125290" target="_blank">📅 15:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فارس به نقل از منبع آگاه ایرانی:
ادعای موافقت ایران با انتقال ذخایر اورانیوم به کشور ثالث، صحت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/125289" target="_blank">📅 15:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ادعای العربیه: جناح‌های سیاسی عراق در طول جنگ ۱۲ روزه بیش از ۱ میلیارد دلار به ایران قاچاق کردند.
🔴
ادعای‌ الحدث: جناح‌ها و چهره‌های سیاسی عراق در جریان سفرهای اخیر قاآنی، مستقیماً به او پول نقد پرداخت کرده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125288" target="_blank">📅 15:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3ef70b59.mp4?token=jr-dxn2YOwE8ueFwCdM-S4Rdua_v7t77IXkToa8693j7QWWPOIOO03jP3mrK5mT9xcSgFyvQ4z5lYKV4g_SoIV426UtBCdbHBqMJq3PPBHos2nzedYGEzHZGd3ECOT2ig_-embyqEV6JuhY_2Ye6dmyqazCw3M_iKktIUAdl6EgJqS6pCvV2AVZGrL04CLd0wVNiVYrKrFpjnvnn_S_R8FPs-0bhpKyFdtasImVcWUT4XrX3rk-MKRRRPoS0jNtMswyHyGPLLeKrrgl_HoBSxnJCIKRuD0V4LCmm54y0-hNZvOWkn9xUajGq2mWT5XONlQo95DVYrnLTtGY634_sDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3ef70b59.mp4?token=jr-dxn2YOwE8ueFwCdM-S4Rdua_v7t77IXkToa8693j7QWWPOIOO03jP3mrK5mT9xcSgFyvQ4z5lYKV4g_SoIV426UtBCdbHBqMJq3PPBHos2nzedYGEzHZGd3ECOT2ig_-embyqEV6JuhY_2Ye6dmyqazCw3M_iKktIUAdl6EgJqS6pCvV2AVZGrL04CLd0wVNiVYrKrFpjnvnn_S_R8FPs-0bhpKyFdtasImVcWUT4XrX3rk-MKRRRPoS0jNtMswyHyGPLLeKrrgl_HoBSxnJCIKRuD0V4LCmm54y0-hNZvOWkn9xUajGq2mWT5XONlQo95DVYrnLTtGY634_sDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/نیروی دریایی ارتش از شلیک موشک های اخطار به سمت دو ناوشکن آمریکایی در دریای عمان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/125287" target="_blank">📅 15:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
حمله اسرائیل به المجادل، منطقه صیدا، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125286" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گروسی: از سرگیری فعالیت‌های ما در ایران برای ارزیابی فنی دقیق وضعیت ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125285" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
در حال حاضر در مذاکرات جاری بین ایران و آمریکا مشارکتی نداریم، اما می‌دانیم که آنها به دستیابی به توافق نزدیک شده‌اند.
🔴
راه‌حل بحران ایران و آمریکا باید دیپلماتیک باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125284" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سازمان ملل: در صورت ادامه بسته ماندن تنگه هرمز، ۴۵ میلیون نفر ممکن است با ناامنی حاد غذایی روبه‌رو شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125283" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کلاس‌های دانشگاه شریف حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125282" target="_blank">📅 14:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نبیه‌بری ، رئیس پارلمان لبنان: آتش‌بس باید کامل و بدون شرط باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125281" target="_blank">📅 14:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecn7a6zqcMxv6UYpcdVlIQzs1FSGcxPbUfE7RqyWBKKUm9-iuDCTW7fDl3WZZPFCyN3oye55Vt6xvPE-VtVhkeBeddCGf8ADEHFQGrpNf6CPBSP9DKoVKf6nNNnA85Qc72IiRd7806wQLTW4L99lNrCU4iaDt5zRP3vI-6tjD676UAOvUhKECNZX8zZNZ8OedBJVCJaH312VYzKsbnX_2aWTKOj_YyBRlNCfY8zjbtlzCsdd1RNRr81q_3SVmG2El03D2NDGUim2PeU_fKwSfvHTbKiHj3w7w34uVnXiV5vBTy-TIQDPJaY9gx_GWVZd8qisNokF_GVEkagMELtKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تا دیروز، تقریباً ۶۳ تانکر نیروی هوایی ایالات متحده (KC-135Rs و KC-46As) در فرودگاه بن گوریون اسرائیل مشاهده شدند
🔴
هواپیماهای نظامی ایالات متحده بیش از نیمی از جایگاه‌های پارکینگ فرودگاه را اشغال کرده‌اند و عملیات تجاری در فرودگاه اصلی غیرنظامی اسرائیل را مختل کرده‌اند
🔴
با وجود گزارش خبری قبلی که ادعا می‌کرد نیروی هوایی ایالات متحده بیشتر هواپیماهای نظامی را از فرودگاه بن گوریون خارج خواهد کرد، چنین اتفاقی نیفتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125280" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObSrG6FvIHbNlWMtMftosjnLhbOCEBphb2pA_F2bMYMfBAz-5pFw-8Tnl2eM06usdjdVsYS0pR8QW_iZpL7jSPJ08XCK4n2PxYitgUz0apBJLsjLK-8EwheAO2bSDej9DJf0VrVOMZOncuBC0DbBVGwAPwy1NNvgcCx7LJeBppTlI3Y_tLgU4Aw8cWy_leemaNsSqAhj_hGULs9CyQcCFe7c1T6DlzmagIiDg7bVJElsg8YzaVMj47K2DNsJeNzD2e9OZPayUXrtgTcCM4zWPR9h19slK0peiSJC6_bvvDU5JzH9hvCmZUmwjpXA0v6fAU9ARqoA2OVQaYWmhzzNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125279" target="_blank">📅 14:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
العربیه: اختلاف اساسی در مذاکرات، آزادسازی دارایی‌های بلوکه‌شده ایران است.
🔴
روش و سازوکار آزادسازی دارایی‌های بلوکه‌شده ایران، یک شکاف (اختلاف نظر) در مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125278" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کرملین: احتمال دیدار پوتین و ترامپ در تابستان ۵۰-۵۰ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125277" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnt6sGSk7LyHAfT01hcLp0M4mJRHgRAqMK5UGtQfI1MX3sJGMFAUBkciem5iLmnxfxVK4pRut80GQUfSd3FLacYs-M0JyLAR46A11lOX9iA-k_iCUrQ-4sDyBDOE1majjGY1NbXCIKGKqOLAXKV-uFan55xM6sizPDD-zP6b7Q8hpyD0s1oUEnV-DyJujnjtRcYddqLIi-wPFoEqtMXC2vPJASPtX4vzoZJwcU7NoIxbALHYClK2O6d2zyXCUU4-H-32cj6wy771LsHAoIorPHM9It3gw5n4wgt0QdBi3ewXWf6-PdeSSzq2ni8joAoJn9jGNKLKdo19i0I_wJ__EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر سکسقیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125276" target="_blank">📅 14:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جمالیان، عضو کمیسیون بهداشت مجلس: میزان کشت خشخاش در استان‌های ایران بسیار بالا رفته!
🔴
در استانی که قبلا برنج می‌کاشتند، امروز به کاشت خشخاش روی آوردند.
🔴
با توجه به اینکه این محصولات خالص‌تر هستند، قطعاً شدت اعتیاد را افزایش می‌دهند.
🔴
خشخاش‌هایی که [غیر قانونی] کاشته می‌شوند، جزو کشفیات است و به کارخانه‌های داروسازی تحویل داده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125275" target="_blank">📅 14:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت خارجه جمهوری آذربایجان اعلام کرد: در حمله پهپادی شب گذشته به دو کشتی باری خارجی که ۲۵ شهروند آذربایجانی داشتند، پنج نفر کشته و سه نفر مجروح شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125274" target="_blank">📅 14:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
العربیه: ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده مخالفت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125273" target="_blank">📅 13:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ماکرون، رئیس جمهور فرانسه : جنگ اسرائیل و لبنان هرچه سریع‌تر باید تموم شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125272" target="_blank">📅 13:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125271" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125270">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=CsYrBO0IEKz4jrHWIv4k-rNhfMc2t-RHMyif9h0CIhMlWBK15m8DiQnjzMtTor1yNvwGG-JlfByK1ah3a2Q4TOQ8k4c7akq5wOSq3lyFTnOviiMki1PTWvESzqLc8RL8jnh_C6ScNi1x_MJcwV6OPfcOTb7GvWjAk-yiIBiW8XXFrzrtwymZL2XpqG5b3oGMI2cgP_SeYjFOAgYCtzsOuquxDipkXDjYhNekfMA6_O03Z1EW66RBa3roo6gkwXz2jhU77PneLIu5ufHf5rZMk85S7_E3I45jEKdjitfK89TOQ9NpNdIdTjVyDCWG_MMWjHigLFrI4VaD8inUu5SksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=CsYrBO0IEKz4jrHWIv4k-rNhfMc2t-RHMyif9h0CIhMlWBK15m8DiQnjzMtTor1yNvwGG-JlfByK1ah3a2Q4TOQ8k4c7akq5wOSq3lyFTnOviiMki1PTWvESzqLc8RL8jnh_C6ScNi1x_MJcwV6OPfcOTb7GvWjAk-yiIBiW8XXFrzrtwymZL2XpqG5b3oGMI2cgP_SeYjFOAgYCtzsOuquxDipkXDjYhNekfMA6_O03Z1EW66RBa3roo6gkwXz2jhU77PneLIu5ufHf5rZMk85S7_E3I45jEKdjitfK89TOQ9NpNdIdTjVyDCWG_MMWjHigLFrI4VaD8inUu5SksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیرحسین ثابتی، نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم خواهند کرد.
🔴
باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125270" target="_blank">📅 13:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125269">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Tdui0xEiN8hznCFiESKIr9ckEc0gruq8YjqByP9OuB9-rHacD-Uz9f8PSgbP8qRlGlMdsiFDn6u7A7vZt19N9ZmYKNIl8QmS9ZYLQUBr49R4rCXiTGiGeIZjfw-Sjc1kRr7KFcgBSmZBn5sLJ-Zy6BWvcxLfX9aRHu6Mn5K2H8bTbUdqRIv13y38YMqPojAsqMTqI2RUDZID1cPa7e9JP9u1rG1TL05hOW7Wbzvz9FvSAi32WVtVEKvRqazwEG3Dix5dJsoGKVHQrxT0gxMYueyn9izFNYqBF7Yt0OiTWJlybG1EImkJqUTJp_1lkmMa3_wuNC4yArrDXBYx_Dyc3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Tdui0xEiN8hznCFiESKIr9ckEc0gruq8YjqByP9OuB9-rHacD-Uz9f8PSgbP8qRlGlMdsiFDn6u7A7vZt19N9ZmYKNIl8QmS9ZYLQUBr49R4rCXiTGiGeIZjfw-Sjc1kRr7KFcgBSmZBn5sLJ-Zy6BWvcxLfX9aRHu6Mn5K2H8bTbUdqRIv13y38YMqPojAsqMTqI2RUDZID1cPa7e9JP9u1rG1TL05hOW7Wbzvz9FvSAi32WVtVEKvRqazwEG3Dix5dJsoGKVHQrxT0gxMYueyn9izFNYqBF7Yt0OiTWJlybG1EImkJqUTJp_1lkmMa3_wuNC4yArrDXBYx_Dyc3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا، پیت هگست برای شرکت تو مراسم، رسید به پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/125269" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPQcQmK_RroObjSNsph2QRe-6lamqMoIkmlOK90vOGHTel2OQYUUOiUudxOkK0iisJ5MMk7d2xfKtHWnloe2nbgI2unZo-If8DjUMTI3uxWpDbNe4E7-lIcMzvgQCykKHEeUgtWe33qxbw1EfNIpL0dbVdP4kT5z3yU3M6RGs1vXptASm2ChPVuuCwbwDfkL_ZPoTgRFGmQVL9gNEpoFgV-ypf4Ubt7SWRFM-GQjbZaoBA_SRsEvLarFJ9EjwJtf311NLanvJ92p6qh172xUk0NNFM3qUg_6KFxT8KERQjjPJNul44OwCAuB3jHyRn7BLFp74O7zNFR5jSSnt1xU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXAEPmqRNLsC9MxpN7OFAYOP1OfyWEPuvxmqe4Gjtt9x_33QeHETo29HkWZqy2DKqzB3y9PmvY5snOwRBI67tk8W5fcfrFOLboPmc3-8FeRU3lcXj1jbwl6q2EawTIn_zkKOnNfQ3y6cknMOxJqTB1fovfkJzR-TM_G-99J7xp0BJjdjv-7QQHKKM2bD0ovQ80QanzeqTmNdTkOYrbnx41aqzu81a0gas_MbIXP7BXDMjjk23FUHl3k9swRbBUGlrCVTdzQ5keppMoffTQdgrAZLHAMmHxmlMejCoF3yDX4-XuYhCPfZv00ieSs6EvXCCzzUHRzummQZwIGrHab9tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنگین‌ترین موج تورمی در تمام تاریخ ایران!
🔴
۱. نمودار اول: تورم نقطه‌ای و متوسط سالانه
🔴
این نمودار روند تورم نقطه‌ای و تورم متوسط سالانه را از سال ۱۳۸۹ تا ۱۴۰۴ نشان می‌دهد. الان تورم نقطه‌ای روندی صعودی را آغاز کرده و از تورم متوسط سالانه پیشی گرفته. این اتفاق معمولاً نشانه آغاز یک موج جدید تورمی است؛ موجی که انتظار می‌رود در ماه‌های آینده اثر خود را با شدت بیشتری در اقتصاد و زندگی مردم نشان دهد.
🔴
۲. نمودار دوم: تورم انباشته ۸ ساله
نمودار دوم که بر اساس داده‌های بانک مرکزی تهیه شده، تصویری عمیق‌تر و هشداردهنده‌تر از وضعیت اقتصاد ارائه می‌دهد. این نمودار نشان می‌دهد که در ۸ سال گذشته، تورم انباشته با شتابی بی‌سابقه افزایش یافته و از ۲۰۰۰ درصد عبور کرده است.
🔴
بازه ۱۳۲۴ تا ۱۳۹۷: تورم انباشته در محدوده‌ای نسبتاً کنترل‌شده و نوسانی قرار داشت.
بازه ۱۳۹۷ تا ۱۴۰۵: روند تورم انباشته وارد یک مسیر عمودی و انفجاری شده است؛ مسیری که نتیجه آن، کاهش شدید و تاریخی قدرت خرید مردم بوده است.
🔴
به زبان ساده، این یعنی قدرت خرید پول ملی نسبت به ۸ سال پیش، بیش از ۲۰ برابر تضعیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125267" target="_blank">📅 13:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhCn-UuUNpFjwsBJwmlN6YbGjxyrxORU4yOCPeN47UmiTqwLAflF14nrAl8QVQqopL7SmVAWDh6j93R14JdpbWDobR27ffcLzPwX7Sv_L4Hn_ywQD8Da_ZjXvCZXzl8uAbcFPdO9A-_gxnl-xpn5cwN54jAaWXyJteJE0xKjO7yDyztcFkuopDTqRIOsO6efzl6hShAxDMkC6BEd5rSZ1Ieoi6oUarubhZGqkIXbaTHwOvGr_h_Jwzw4MavQlexfaJlcg8_RPeRwSdofc2N-f8fKklmuWSBfDPQVqPHEal_TQAoSLhXPIEDi_XRRru6So-hfShEaGBRa4SMnZzuR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار یک پهپاد دریایی «مرتبط با جنگ اوکراین» در بندر رومانی
🔴
به گزارش رسانه‌های محلی، یک پهپاد دریایی مرتبط با جنگ اوکراین صبح روز جمعه در بندر کنستانتا، از مهم‌ترین شهرهای بندری رومانی منفجر شد.
🔴
وزارت دفاع ملی رومانی در بیانیه‌ای اعلام کرد این پهپاد حدود ساعت ۱۰:۳۰ صبح منفجر شده و «احتمالاً از نوع پهپادهایی بوده که در جنگ اوکراین مورد استفاده قرار می‌گیرند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125266" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=CE6Ijb90Uvp5jf5917mWMSgFRaEXajYUJ5SbbZaqF7Fos1reGFVz9bgfQocvDxAbJZTjoQ3AJiuf6_0XrimoTnNykCkNh__L2jEeUBQokKBTX5pzGRxKjFeUKusAO5we-pj_IJMRYFNPgeZwQciVT3xmy6oY0IekMOc7exxwwL0LXj9Gm9Hs6ukGz8E6geJu9tJcvYuf3gynh18bd4Eey8v51E4AfgDDdXTfs21y47CQZNHINoeC56PaTrzrx8sWLZ4HLlvjWWFMTSNr6tFZ3cznYSbygKHBW7pP74IwGR3cB-D9NStuqf4wBTbFayMhPMeLQ84P_K04j7s0hewDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=CE6Ijb90Uvp5jf5917mWMSgFRaEXajYUJ5SbbZaqF7Fos1reGFVz9bgfQocvDxAbJZTjoQ3AJiuf6_0XrimoTnNykCkNh__L2jEeUBQokKBTX5pzGRxKjFeUKusAO5we-pj_IJMRYFNPgeZwQciVT3xmy6oY0IekMOc7exxwwL0LXj9Gm9Hs6ukGz8E6geJu9tJcvYuf3gynh18bd4Eey8v51E4AfgDDdXTfs21y47CQZNHINoeC56PaTrzrx8sWLZ4HLlvjWWFMTSNr6tFZ3cznYSbygKHBW7pP74IwGR3cB-D9NStuqf4wBTbFayMhPMeLQ84P_K04j7s0hewDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاینده‌رود زیبا به اصفهان بازگشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125265" target="_blank">📅 13:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سفیر ایران در مسکو تاکید کرد که ایران با دولت عمان برای مدیریت تنگه هرمز در حال مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125264" target="_blank">📅 13:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=YcEhLOuOOuYOqba3ilryghCadamRZT2rq-e6c1yPHRZBCvye2mpNUMPGNjMeW7YW7xYUCxVolg2EIfURaa0hO3a3WPZXqDNclkasQ6EcF2YTZXtQ2hhNuvR9PfHDeuYXnpHqqT-IUPbXYkuW17jsAGyjHXpl_HNidEFniZIAiHT15jgUstClGKIrBT8sjDEP-ydlhDT3Wc7wHRNvXcLHsds3N7lfmQz90eUVzY7ljO3yfKIkDCEUVqUxsS-aBdy0tfb13xnrijJUeAhJ6_gyi2ZPE-__UoFttfGj8gqc-jQqy4OZcu3X09bMLsSOVDVxm9OX6_k_iW75220yS9uf4qijhgVRYvioBbBCk-44RxSP5ASS2zbo99dM47lyvQCWp041JYYCR0-XareKlLQUHzeNAc7yVHc3Bxm1DG6wrBBv-nHan56K8KyzRwlfksSDakLh2wO_Q1Cu7OAEPkitD9MIJ5QaW9fDyyC41f95H2HuiQ4Ve607bUI_I42LuiaJR8BQ72vOzgxs74N2wQ3dUoiKkZwdfxmx3b3NLejxIhjK85mNJxgGziKdkaCe4T4W29NtYwTg1DT22LwscM-62BFdZ7PdCdZBy2bKb6NEsHZXBCNklbFqoFQ6pdkxeHYDnhDTx4TdIVyPwJO1ugp0cK-EGcP9t8wU_X2Fr-LDQx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=YcEhLOuOOuYOqba3ilryghCadamRZT2rq-e6c1yPHRZBCvye2mpNUMPGNjMeW7YW7xYUCxVolg2EIfURaa0hO3a3WPZXqDNclkasQ6EcF2YTZXtQ2hhNuvR9PfHDeuYXnpHqqT-IUPbXYkuW17jsAGyjHXpl_HNidEFniZIAiHT15jgUstClGKIrBT8sjDEP-ydlhDT3Wc7wHRNvXcLHsds3N7lfmQz90eUVzY7ljO3yfKIkDCEUVqUxsS-aBdy0tfb13xnrijJUeAhJ6_gyi2ZPE-__UoFttfGj8gqc-jQqy4OZcu3X09bMLsSOVDVxm9OX6_k_iW75220yS9uf4qijhgVRYvioBbBCk-44RxSP5ASS2zbo99dM47lyvQCWp041JYYCR0-XareKlLQUHzeNAc7yVHc3Bxm1DG6wrBBv-nHan56K8KyzRwlfksSDakLh2wO_Q1Cu7OAEPkitD9MIJ5QaW9fDyyC41f95H2HuiQ4Ve607bUI_I42LuiaJR8BQ72vOzgxs74N2wQ3dUoiKkZwdfxmx3b3NLejxIhjK85mNJxgGziKdkaCe4T4W29NtYwTg1DT22LwscM-62BFdZ7PdCdZBy2bKb6NEsHZXBCNklbFqoFQ6pdkxeHYDnhDTx4TdIVyPwJO1ugp0cK-EGcP9t8wU_X2Fr-LDQx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس: جنگ ایران در بودجه پنتاگون نبود, حالا ارتش آمریکا به مشکل سوخت و مهمات خورده است
🔴
جنگ ایران در بودجه پنتاگون پیش‌بینی نشده بود و حالا وزارت دفاع آمریکا با فشار جدی در بخش سوخت، مهمات و ساعات آموزشی نیروها روبه‌رو شده است.
🔴
دریادار کادل، فرمانده عملیات نیروی دریایی آمریکا، در کنگره هشدار داده است:
«نگرانم که از بازه زمانی جولای مجبور شوم درباره نحوه آماده‌سازی و تولید نیروی عملیاتی تصمیم‌گیری کنم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125263" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر خارجه روسیه: ترویج گفت‌و‌گو میان پادشاهی‌های عرب و ایران را مهم می‌دانیم
🔴
ترامپ گفته بود که «ایران را به عنوان یک تمدن نابود خواهیم کرد»؛ این یک بلند پروازی گستاخانه و هدفی دست نیافتنی است
🔴
آمریکا به وضوح می‌داند که در موقعیت ناخوشایندی قرار دارد و نمی‌داند چگونه از آن خارج شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125262" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار العربیه: آمریکا همچنان درخواست ایران برای آزادسازی دارایی‌های مسدود شده‌اش را رد می‌کند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125261" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=IBpoBLB2FQ5oChIOySXIXTOytnx6v1sQbXqfCLGlCPP9sJdVv2Bpp8xDbxJwPglbyTrjfH5u7FwmInr_4G8VgccTu2bXQbq3SM6Kys2nPXfltvsg6POWbKZIowtq-A21dQNhlYNQUUYdwp8ORwQq1TxNI20wZzXPA2P2nyiKzB6h8uFIIwLXTzPmnzxouXxnWHNSYLlrK1fTrLWggGBVmYlj2WrNMw7Djh2TbeSeD_je7jyxJ-D9dPMvjU3uTxUR-0NmgX-QlGDjtsACH8WorbRFGXPX1OP-xIHVgaJonGJvyk1PGGOgKMIJJcWMjBI2Pe04Z0Kula72UPuID0JyNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=IBpoBLB2FQ5oChIOySXIXTOytnx6v1sQbXqfCLGlCPP9sJdVv2Bpp8xDbxJwPglbyTrjfH5u7FwmInr_4G8VgccTu2bXQbq3SM6Kys2nPXfltvsg6POWbKZIowtq-A21dQNhlYNQUUYdwp8ORwQq1TxNI20wZzXPA2P2nyiKzB6h8uFIIwLXTzPmnzxouXxnWHNSYLlrK1fTrLWggGBVmYlj2WrNMw7Djh2TbeSeD_je7jyxJ-D9dPMvjU3uTxUR-0NmgX-QlGDjtsACH8WorbRFGXPX1OP-xIHVgaJonGJvyk1PGGOgKMIJJcWMjBI2Pe04Z0Kula72UPuID0JyNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جاوید نام ‎سعید تروند ۳۳ ساله اهل ایلام شامگاه پنجشنبه ۱۸ دی در آبادان با شلیک مستقیم گلوله جنگی حرام زاده ها کشته شد.
🔴
او متاهل و دارای فرزندی ۳ ساله بنام آریامهر بود.
🔴
اینجا پدر سعید تروند با فرزند جانفدایش بدرود میگوید.
🤔
عرزشی حرام زاده ، پدر مادرتون باید مورد بررسی قرار بگیره که چه حرومی به خوردتون دادن که اسلحه به سمت مردمتون گرفتین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125260" target="_blank">📅 13:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مرکز ملی فضای مجازی: بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، قطع اینترنت در هفته‌های اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125259" target="_blank">📅 13:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از هشدار ارتش اسرائیل برای تخلیه، مردم جنوب لبنان، و اطراف نبطیه، شروع به ترک منطقه کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125257" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS2MMn_HTO7QGHUvF2iQyYEOP9KnBWWncYAIHD_lYd_zCONm-Sxa8FbbBprrIuDvnOiq1BsnjnSGJ4l_G0NXtEBxX4EeeRJ1zM_j9dRwgZ8pj2tkFn8zFExmOD8SDw5dhel3I46Msc5vBw2JJSerr-ZNJPNltI-rz58B3_QgeZ3B-MypUw_RuXDFwZ_RgSxPMdM5BpCuBPm9ui88s_lZlFmz4TCAD5ieme5RK4Yces6i97sq-hXyNlwHD1WRC388NX39FcnIzMPBLnBZsfPoWA9AiGdD3oTGN7HAra11drK4_RZ_bJzXJVdphcrxwneKOb8585RMdjWcS3QYunI9NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125256" target="_blank">📅 13:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_sPBBXdbpl9hqCJuXRsf3IJXMDJULOG73Y4lAczM-ujcEN8IDc0luUki3lHMTgDAK4vEfBi-7sz__OeX1J7aaNhBdZf8MRr5vzZ3bGwKiXM-MZtDVpQmE5xOAmVrSzyH28ck3ahu7DEZs8lzsmiUvDL4tmbT-qYh2xlHdcl_1iLjEeeotLUwUFjzqUjGHnvTL0efvHPTQ-ZDHOV69LOSdjcI2-xNtWCyOpQdGP-bOa3yE_b71RuqufYfp3oip0qcm6w7QRtrvpf0unyHLk1twyUufY55z4qyA8uKmmu_KuSyRPTYodJD8bbmMT-Q1lDGgsZKgDTafgFCtqIHy9QNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه دیتاسنتر ایران با فنلاند
🔴
سمت چپ: دیتاسنتر ایران.
🔴
سمت راست: دیتاسنتر فنلاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125255" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Fedo5gR24d6OVLmWaak9CBvcPBCrSsX1WgXsAvFPy-gmzwz3t19BiYLtwSl9ktucA9hg6rt7dAkEZIxPQKYeSgfJRa2n0LbKSB3msKewRUYesrT-QLRDPmXIor3R6VbxNa47gotLPJ2pC110P0VzGiw0Gwp7BH92cNJQTTD1vezHRNq9JS3nr1U1xJ0MatYM6SEut9mBKEV9O8gapjSyeGPL3MqzCBUDIp5ZSTWR4-KP_3pbpd8R_xPX3ffYM-BSbWRtlqRhUBacBPXdnvFcEOyYXiRXiTHP0Nsl2aTNPHskpedxE68Yq0LMU4U2LeEGa2MR7WhPwD-QreF3Sqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنا با ۵۲ رأی موافق در برابر ۴۷ رأی مخالف، لایحه ۶۹.۵ میلیارد دلاری برای تأمین بودجه اداره مهاجرت و گمرک آمریکا (ICE) و گشت مرزی تا پایان دوره ریاست جمهوری ترامپ را تصویب کرد.
🔴
سناتور لیزا مورکوفسکی (جمهوری‌خواه از آلاسکا) تنها جمهوری‌خواهی بود که به این بسته رأی منفی داد و هیچ دموکراتی به آن رأی مثبت نداد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125254" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FIkWHe0fHZSInXvBcoAgCl3KOoIIvwBTxgxUyyCSKN5SXEkqISsB24wwBgguiYvFKURvxCx-9lJ2jC_slGXFZFqqiA57okC1IxbDTLqwxZDHXYom25eWXSwfh_gvVtBDLjhJNMztCuj7zbyYBNhYc8QRUC-Wa3UxJZeuY0lk1KI0kvnEsYy2Oo3Tjw9-OKz1lAF3Ld5YvEmU4oR9ikwCRGcxfjkb-WkSsCCSnI7eybewgSNwZXiZQrWIKz01tLdcBjMqh_-yjjnDfli4DoM6SMXuZlZTcHcrragSrzwRTCgvDlXfmF8EQbfNEVIZ5s2AxBuDnlExJWTFppVflis09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FIkWHe0fHZSInXvBcoAgCl3KOoIIvwBTxgxUyyCSKN5SXEkqISsB24wwBgguiYvFKURvxCx-9lJ2jC_slGXFZFqqiA57okC1IxbDTLqwxZDHXYom25eWXSwfh_gvVtBDLjhJNMztCuj7zbyYBNhYc8QRUC-Wa3UxJZeuY0lk1KI0kvnEsYy2Oo3Tjw9-OKz1lAF3Ld5YvEmU4oR9ikwCRGcxfjkb-WkSsCCSnI7eybewgSNwZXiZQrWIKz01tLdcBjMqh_-yjjnDfli4DoM6SMXuZlZTcHcrragSrzwRTCgvDlXfmF8EQbfNEVIZ5s2AxBuDnlExJWTFppVflis09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جایگزین برنامه 90 بزودی با نام حکمت‌های فوتبالی روی آنتن زنده میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125253" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtAn-NPhB5u2UTF0_MmwiKBThtC-VWqLJ9P5p_3jE-igxKuk2foeKD6QwdJQBeHS1aK2II_G-OAXoQXUFSeLe2nVMBru8lTxVQrP7AzdHFa3-hHy5W84RG9jq6MpPcnZGhjilBya_ea-9ZBs6VRCXM0DTwB_nTMtQMQvErXMOCDK_pUXu8d1YknyjybfQ7HLl9ikL3-4gaS7NzYu--T5e1DguDUeYFj5ApnqfZnS64regnqKSSkfYBaAp4l3wbFhohqK3wMugtjrgi6Fy7POzXq75JXw85UFjccUIbB7bnAVYD-3qViTyGjOQgWCwx8QQlSAZrAGjHqnolm-IszjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجموعه ای از حملات هوایی اسرائیل شهر عنقون در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125252" target="_blank">📅 12:46 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
