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
<img src="https://cdn4.telesco.pe/file/RkDi9HasRQzeYg1HpuC9ye9OLaCKqMP2K2QSmH_ZWrh4N0lduh9VbR7g7xoLXAYjWXKd_syv1wzjM6nrD709esryuF9TC-ac_fpt_UERg6raAUc4xkzSmnzYhKHwWKy7-75L5lbQYRpFnOurABMjO-xKnYu-blgGlu-G0HZqTMcIfQ7wEF9igapS7iXx9Is36hg68_bD38l3-9sYTyjeO92MYbhWLhDt8cASp5CcWWh89XuDGCzMG_2tJ2SyLdw3oTDZrY_6qu04RsdctaqNDls8t9ywAc1CuIz1Hy8FGG_hgKRZ2SuLb1qFzw36W-dB-Bq-MhkjkuiyQneYXMni-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 37.5K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 457 · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=mryeakP9YeuqqnNebuwWMTPCFZgfu53_I3Y5NcJk3ZY-31YX7w_nkYulIhDcyy36RB0tisRGEt88WpU637SQHJwQ2NwomFs9z6iD3o-wsi2Q1kTNM7CI_QiW2GqQntwTbQGtP_O-2QnlEb_0kb-lLSD4KqJUZgFv0e66NzLcAXkBDblHl3dAcPJIhEIw-GMqyyfiUHY1lHQqBoKvhfQttEhVp7KHTo_Sh9HTrVhBxs9CyJPeoiKnKXNTE1CRyg2RKA1ud_1BQtg5g7NbJwHFwY9DBOdHLPAim_aYu6SCAmfzYD7lYjDXd5NNaa0GXwf9d-iR8aPIKiEBRAp6zzU0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=mryeakP9YeuqqnNebuwWMTPCFZgfu53_I3Y5NcJk3ZY-31YX7w_nkYulIhDcyy36RB0tisRGEt88WpU637SQHJwQ2NwomFs9z6iD3o-wsi2Q1kTNM7CI_QiW2GqQntwTbQGtP_O-2QnlEb_0kb-lLSD4KqJUZgFv0e66NzLcAXkBDblHl3dAcPJIhEIw-GMqyyfiUHY1lHQqBoKvhfQttEhVp7KHTo_Sh9HTrVhBxs9CyJPeoiKnKXNTE1CRyg2RKA1ud_1BQtg5g7NbJwHFwY9DBOdHLPAim_aYu6SCAmfzYD7lYjDXd5NNaa0GXwf9d-iR8aPIKiEBRAp6zzU0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=nFsgSvodP3upeDUNhGHd1DwWznpCDEtJOlRjhKnES7X-0kvapcw51IAMm4gr6L7cZUj38I5gMjM2EtoNpcAwde4zxnQJ_gtLa1i7_k5BL_m91mlkNRS3MJnCpenGW6OZkNccyX5lTN72GOvpt9OP3Fy8WDkWIM7zcrDYynh30-r85dYZiv9_9IjI5nhSXb0Z3OpYt4VkTtTCwlMbcTYdSTQCcmSXA1wfJy6c0FNKc3x3Z9Vxh1A8u6nVzPgyEJN-_QhkhCu2C6-A3auZBGhAd8Boq9VCkbuZIDtwsLNQy-EbA9ctVSf2cO_8q36nOFbwuYosHsRYJB1eGh9lNhR3Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=nFsgSvodP3upeDUNhGHd1DwWznpCDEtJOlRjhKnES7X-0kvapcw51IAMm4gr6L7cZUj38I5gMjM2EtoNpcAwde4zxnQJ_gtLa1i7_k5BL_m91mlkNRS3MJnCpenGW6OZkNccyX5lTN72GOvpt9OP3Fy8WDkWIM7zcrDYynh30-r85dYZiv9_9IjI5nhSXb0Z3OpYt4VkTtTCwlMbcTYdSTQCcmSXA1wfJy6c0FNKc3x3Z9Vxh1A8u6nVzPgyEJN-_QhkhCu2C6-A3auZBGhAd8Boq9VCkbuZIDtwsLNQy-EbA9ctVSf2cO_8q36nOFbwuYosHsRYJB1eGh9lNhR3Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsH-ZaRywzjXVJFgAD-Gmt_iUzbuO1Z-1XpXVMnFxBMSoin9AC8inyc0vqtEvs4gTGjUxS_CFiyUzxeWj4wMa0LDv5nucDrSUNGjd_AibrgdhWYB_2sU1qkLhIyAB8DKyEoZnI50AwNJWijvDR5Ffo1H7uVD1PAG_pd4bLc8mquCLyrfjvyPutEFlTOIxLwjswK2Ys0I2zK4-5rfkLAWTyMyWzMY7ayo5XA7SSKC2iotMmqCkPjXfRg4zveYQ77CJt1szv4jzM4zkEVTLML846K8WvK4C__oUt-c8ofFyQ1xTRUSIGuzelyb-gs2gogFjYTZaXG1j0jUQSvDKtidDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=HaN7sVWVhFMrzVSpzsqxsIeBM62weNT9LYzAVjo75G8n9C4XGhbt3OH4p-hsV47vWYSY72Mqy4MrgX34VYU1MZz2JCXgk0IirdkUysoo6NH6uS5HMW1xa6ytJndhU_ZSzOb_zD3W9fGsCpSAnMB5Iag3qGTWLMBPqWmb6WCBTKh4JH4AfEWiWFOOL8IVId6yK4Fo0jEulHGeJVnSqrtdWaW-XVcisXxqg7QraEKKy_i9vcA9_fMhdW4hECSuWwhCt_fMQQOHF8JGz92l_Y989yIjQRqPYYqUTG1JPPD1Q5_pz4OhcSQJouf87fO61DvSlhjOpggNDquJYTyCPue-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=HaN7sVWVhFMrzVSpzsqxsIeBM62weNT9LYzAVjo75G8n9C4XGhbt3OH4p-hsV47vWYSY72Mqy4MrgX34VYU1MZz2JCXgk0IirdkUysoo6NH6uS5HMW1xa6ytJndhU_ZSzOb_zD3W9fGsCpSAnMB5Iag3qGTWLMBPqWmb6WCBTKh4JH4AfEWiWFOOL8IVId6yK4Fo0jEulHGeJVnSqrtdWaW-XVcisXxqg7QraEKKy_i9vcA9_fMhdW4hECSuWwhCt_fMQQOHF8JGz92l_Y989yIjQRqPYYqUTG1JPPD1Q5_pz4OhcSQJouf87fO61DvSlhjOpggNDquJYTyCPue-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scuBphbjrwigL6FRj9eWiJfRLzDCNlS4p5vZAXW2WYwXhq961KlwYqFDMYP2KgCG4iE_-5awcQ4wWqneA-VxG3Qv7w_GZDM7bxmvnM0oN6Ufczy0-ePNwVDVpRcj089hLhPBaPIAqSzBkB6h0RxoKLEMrYV-U7YhGk5VMyTaNuzD0wTCu90KUY1Dt4vaCi41maFhL5I4yrnLPxIczN9e2Y-pfbq1NIIPgnVFXvXrP8YQk9bn1nKeg9D9nyz5EhsiKNxugb2c852NWby4_TgAjdaRn5vjGx4CyQhZww5s4kINZzW8U8tVXlrL72neXO7c_afffDO_CTbpuoQ2PamI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUodIcpCXRpC1dYj3HEB771k9ZS16SnuD0xMNjh4FQV5Rj8VdzjTZVs6rYX9qOg4Di2HQVQLXTLBszkApaTTInNyHy_sihLUUMF4Rw4PLZirTkXGzC7xRJ2wD9QCKsHNluh7v_4dVAd9pujjQSlhNIFKyKdefMXVP3sNB0-7DbIoN3D_y5Tdvw1ptcqqML8nu8oLA8G20dqXI0PTzaI_9ABND3n1QPFf-eVmvPHmJwVziS02ukVJ2wBz3iUMg1Qz-MiEYtZhD4ZA7l3tk6jAoACLQ2T8TyTj8HRG_WSTSRdMlFPP7sQ4B5GRH0zLJAFvVcR7ROoZxiGzWStk9PuNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=N-N3Yp7247sm9qgbY_Mzjh0E1A_gTS3RP00NwphdHBIgiKBlAm40JJa9gn4n3NNusbiqkryaM0ruVSswFn_-va0PRcfAHl1FYzE3cCfwXh2SKzGBnQAuA33B4INaJAHNs7cDvXxYhwoloI_tGsuw9K0A8b9YKoN07QWTTg6gYBH3KjKQx9uWKHatF5fjjf60qILyu6356rt9prIZ9jl1iqw8o91ib8Ug8kQhqk95quMqPGXBTT_Szs5ilXUjRefVED--lCAVlWkn14msHbHtHjay1vIkeU11E4BkpLj82OrvGRnvCzkKMSK2JJQGz4lbuLOAZbVtak_nckQpmlknvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=N-N3Yp7247sm9qgbY_Mzjh0E1A_gTS3RP00NwphdHBIgiKBlAm40JJa9gn4n3NNusbiqkryaM0ruVSswFn_-va0PRcfAHl1FYzE3cCfwXh2SKzGBnQAuA33B4INaJAHNs7cDvXxYhwoloI_tGsuw9K0A8b9YKoN07QWTTg6gYBH3KjKQx9uWKHatF5fjjf60qILyu6356rt9prIZ9jl1iqw8o91ib8Ug8kQhqk95quMqPGXBTT_Szs5ilXUjRefVED--lCAVlWkn14msHbHtHjay1vIkeU11E4BkpLj82OrvGRnvCzkKMSK2JJQGz4lbuLOAZbVtak_nckQpmlknvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6KOsyO_8acB-LqMziKULZTEvY_bu2iEe66IGBkh1iJ4feD1W8Q5iOGOhZlDCTazB-t_Ru-_33RNGVirbyB9gGhvZ-4uWtWfPEs0_OAS5VsOWBNi01Kc8zDibktrug5djol9e4G9Tf1-c9fYcoOHoXvSLN9k8q51df2wFOs0EERVoPihMc52KeEp2WERwy3WJXMAc10Vkro1DkWRCrzoDuC7_82iigs3rkoBOE9ZBjIYNN4odvCBruB9T-b6fOaRnLe1FGgwUQGCF9HSdQrnJfaT6AuGttBUny2Iw1ViPgeic2KxrxoMxZS9b65GVkczjqECza5O1S30TdV38ulGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5ZPvXEbv-GORpqcQZWD0H9-iy0v0akmd0UKG4pMFcAlHnNI7HOgyP_b2I3aCtHZdn206MIgb_kPNmf1AG6IkS2yrYudNi4cQN4z4bp0zB4vdhzZxm5bIZkGGbZUtPlFL1eW1ZBvuVfc6dwI2n2BwycuE4Q3ms6DQ9AOi1DaZDx2_Adyr7gyNKf8uwTvT-SMNppZa1DJFpKZz58A1PNdU1gLHAGYsPQ6cvFKVgN7onuYHb3m2BI1ocla3DwtiPko91wGlr6X0YxcUuQF99P2AZ89h9rxhPNKFP6As8WcKTbig4gIQYE4Q1MObPHZROAnpZVyhWDe7K7dhbohaCEETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)
و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.
او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت جدید و بسیار قدرتمند برای زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد.
هر بانکی در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور آمریکایی ضعیف و احمق. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
به مدت ۴۷ سال ایرانی‌ها ما را «گول زده‌اند»، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8290" target="_blank">📅 21:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✈️
جدیدترین آپدیتِ تلگرام
🌐
[ ورژن : 12.7.2 ]
- لینکِ دانلودِ داخلی ( بدونِ فیلتر ) :
✉️
Telegram ( Direct ) [ v 12.7.0 ] :
https://uploadgirl.ir/d/c99c188e-57fe-469c-91ce-843a37e803f3
📌
خیلی مهم : فایلِ آپدیتِ نسخه ی Direct هست و در صورتی که نسخه ی Direct رو نصب دارید دانلود و نصب کنید ،
+ فایلِ نصبی داخلِ یه فایلِ Zip هست که باید استخراج کنید و سپس نصب کنید .
+ اعتبارِ لینکِ دانلود : 3 روز [ لینک آپدیت می‌شود . ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qULk-ALNye8EZX3ywhFJs_ERewVru6BSJd4wXsKNdeOFgRE3iP-ZkN20olmwmdLm3bYpuHItg2FRAACBB34UuFZbqmtfO8CdePVVFTf14YjJ3NxdfFaL2UDRZYkwRnY3lO5cAtufnoAdUrVYNvjjwrvOge697MMykrrNegi_ryGzrskrbeBBdPRAVQSO1g4ynrtouTgXhFGaGQRklo4jC_X10GtQS9dDRvwRosMMO_zW8v10Z6aSRr68hOdUn9jCKPD-HQNVPIaAWKTy44mSeNEWqnt0sbQSuSoYvb8H5Rqa_cxH-dw38-HbRhoUZJO5ok_JoQes_K3vsQvesBaTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/IranProxyV2/8287" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZetMCuObtzwuY_y0ucVHRGr5u4k78uFzvN0TROL7em50GTr6nOR-0i4id33pkctQCLkUtjx-SN-e2RSHJYbZ5TwZJdTWEkG3NPopztGBCo20D9rGcK-aYpdycwi3g6TQ-jtsPlqSobiELx7FxyqeTf2ljxcorLLABQKzaxDSsv9_FvBesnnKdWg-gX9skTm2q18p0qLwHqz1upRboFpzOdTD5f1hrabxbqgypZoPR7AAYK4kMaX_-sWuYibsjkO_-wWr82jtrQO5BgnYme_rPUzCnWqfcUB_vmYEX1-_Ab46IgNNgJL1mK_xbacdeT4qMPXSpxR_9-9WfGiGkZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کامنت هارو باز میکنم پست بعد حرف نزنید فقط نتیجه رو بنویسد به نفع کیه
از اونجایی که خودم بارساییم 3.1 به نفع بارسا میشه</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8283" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه چالش میزاریم هر کس اولین نفر نتیجه امروز الکلاسیکو رو درست بگه بعد بازی جایزه میدیم</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8282" target="_blank">📅 12:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨الکلاسیکوو🔥⁩.npvt</div>
  <div class="tg-doc-extra">2.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8280" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8280" target="_blank">📅 12:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان جوری اومدی ریدی تو نتا جلیلی تو خوابشم نمیتونست همچین چیزی ببینه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8279" target="_blank">📅 10:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=qMZKRFLlG-CoV0PDXp6jobqJQsJvudbhMA7qYfJFD_gdayO542jjcaJwkCyZZE-BEKEuyR4C42Vmbw-5sCSGUSXBzlDDynOD4lsY1dSGLhMcel_-3Ua5zmeOAFzFM5XejTvfTg4cyXxD1uTXktfQaO2hxpC0eoHUi50qRe4cB6yv7kOF0hAPYVzIyEu9FHjk6ZV99NR2QaGS879VH3kGhP9728XLFmAsaLa_wsjVrW6iezt1oMZsCbgo2w64m_cs5pj1GxjWxBOMaeiliUFvnsMHF48MWWCq97pkEOFsYFzMfOHhGNKMcd6iyxwKzyVmEh_5Pn7i8x3Cn7m64MpOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=qMZKRFLlG-CoV0PDXp6jobqJQsJvudbhMA7qYfJFD_gdayO542jjcaJwkCyZZE-BEKEuyR4C42Vmbw-5sCSGUSXBzlDDynOD4lsY1dSGLhMcel_-3Ua5zmeOAFzFM5XejTvfTg4cyXxD1uTXktfQaO2hxpC0eoHUi50qRe4cB6yv7kOF0hAPYVzIyEu9FHjk6ZV99NR2QaGS879VH3kGhP9728XLFmAsaLa_wsjVrW6iezt1oMZsCbgo2w64m_cs5pj1GxjWxBOMaeiliUFvnsMHF48MWWCq97pkEOFsYFzMfOHhGNKMcd6iyxwKzyVmEh_5Pn7i8x3Cn7m64MpOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری علی صبوری که میگه به مرز فروپاشی رسیدم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8278" target="_blank">📅 09:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHg2BEn5MmGsBFlX-xdEqegxT78iJLiD4WFUOMc10EJijMVRjHdWV_lVPxeDkcKaQ7N9atS3_sm1cFfU0qdOOm-4GiDr1vD3iwEmmxCl2cuuW-rK_KNYU08Uby2oYpXdC2ajgyqXFUWdcJIKx3Tg6DdDoTNUFAS7hrOGqnAUQqs3nenZzMPxzG8I-F8HgBUlyDbRjLJlJ6Q2CMc1KcXvCuvijxBsf-a74sClIu_V41Jlg5q7j9YUczWgBHgIGOOekezYzst-uQYzSUNHoS-KtLzpfn1PIW1TmbUl5WVoFxSoG3xb4EdWPmz1LB1QD2yNGExgj9BCYpqaTxjqk1wOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی صبوری بعد این که ویدیویی داد و فحش خار مادر به نظامو طرفداراش کشید
الان این استوری رو گذاشته و گفته بیاید منو بگیرید ببرید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8277" target="_blank">📅 09:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjFsXVtYWFwH2W1zvetWELjREzwu6L8Mt8Ld6673nDQb8Z1VVfBsIQUlFFQy_YeicXmDjMFqSPwZv4i4kaFAvrH6Yjm8RAaPHOlNQimLMR4Fvkc36lpSWnSnSmXB3YS1KHOevdgvv1LtQhyfIqomF-ZCTAqpkBdOeylLdsHWYuU2anE_0u1XhMY-dGEJqo7yWDwL8L77FRcI447aDcKMKsYsPxQzYr3Ohy5hGKW3lhmpSDHxoARe9xpQIyPGY8OQTKGIsE7GF6ljdA6qNkluBNkP3zZ_MpgX4gbkNxHYAm-A6SsMAkNlVqpjAlfJSdmcvUduNIE6JmmhWSu33UoXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8276" target="_blank">📅 04:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رفیقا پروکسیا اختلال دارن تیم فنیم در حال درست کردنه اختلاله. کانفیگ ها اکین مشکلی ندارن  میتونین خرید بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8275" target="_blank">📅 02:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💎
دوستان سرور های تانل که به اینترنت بین الملل وصلتون میکنه، هیچ مشکلی ندارن و قابل سفارش هستند از ربات
🔥
@RUSSIAPROXYY_Bot
ولی سرورای مختص تلگرام فعلا درحال حاضر سرور خارجمون به مشکل خورده پروکسیا وگرنه سرور خودش اوکیه، یه مقدار طول میکشه اوکی بشه، اطلاع رسانی میکنم همینجا
❤️
✨</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8273" target="_blank">📅 21:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8271">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مجدد اختلالی بوجود اومده رو سرورای مخصوص تلگرام، منتظر باشین رفع میکنم اطلاع میدم خدمتتون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8271" target="_blank">📅 18:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlZxFIzmULC4baYYIzEkm0Sx2Bx5LWCUkVGXRgNSqA0BXkWnJiqY1qV3Ina6VPJADEbnaRyJgqf8Sehx8a6U7cNAS5bY6X4sTyDxem_jqj41vh6w_MWpwLt-C6uGf1BYbuuucxPO_MKsB_iM8Sf_EarGCnbiPOUJnva8znfvut-U15-rSLEs4Owe2CMigFu6qbZ5fwkKRp9T4RBm5D-__jTLpF2PEcT8BLvOkavJrSxbocCOuVJgIr8Ymuf6DH_chaBNS2uDQMLM_rfhXB22CbEre2zeR8XvW5-4yNoY3SSW0nCSBjLt52htreI5NH7RAsKY4ampoOFgnWQz82R5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز تست خدمات اینترنت 5G در کابل افغانستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8269" target="_blank">📅 17:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤖
چند ربات کاربردی تلگرام
لینک مستقیم فایل رو میدی، تو تلگرام میفرسته:
@DirectUpBot
باهاش فایل فشرده zip بسازی:
@zipyourfilesbot
در تلگرام فایلت‌ رو میفرستی یا فوروارد میکنی لینک دانلود داخلیش رو میدن بهت:
@ICESENDBOT
@catuploadbot
ارسال فایل از گیت‌هاب به تلگرام:
@GithubGitlabDownloader_bot
هوش مصنوعی تایپ سپیک:
@TypespaceBot
دانلود از یوتیوب:
@YoutubeFiler_bot
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8268" target="_blank">📅 16:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کارزار اتصال مجدد اینترنت بین‌المللی:
www.karzar.net/291129
شرکت کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/IranProxyV2/8266" target="_blank">📅 13:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تلگرام
در عراق رفع فیلتر شد
🔻
سازمان رسانه و ارتباطات عراق از لغو ممنوعیت فعالیت اپلیکیشن تلگرام در سراسر این کشور پس از تعهد مدیریت تلگرام به رعایت قوانین داخلی و استانداردهای نظارتی عراق خبر داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8265" target="_blank">📅 12:04 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یکم اختلال داریم رو پروکسیا به زودی حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8264" target="_blank">📅 11:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💎
تخفیف فوق العاده تا اخر فردا روی تمامی پلن ها اعمال شد
✨
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید، درضمن درنظر داشته باشین که سرور هامون پرسرعت تر شدن و بهنیه تر
😁
❤</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8263" target="_blank">📅 03:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚡️
𝗣𝘀𝗶𝗽𝗵𝗼𝗻 𝗣𝗿𝗼𝘅𝘆
Host
:
37.152.190.145
Port
:
1082
Host
:
91.222.197.45
Port
:
8001
Host
:
45.148.250.241
Port
:
8080
Host
:
85.9.104.72
Port
:
4040
Host
:
37.152.190.145
Port
:
8080
Host
:
94.101.186.25
Port
:
8080
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8262" target="_blank">📅 02:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=VNUMHBAhIf0LQwVqgM6mGHRfeBAmG-9FghNAJYf9Lng6rrSwoe_XvcqnZim10lv9Ni8bCccDbR6q8T2Eu_owVo1EtyJ2AldPBc6E17am7zXyKfR7pXLiWcNfAWRIWDEJZLlAC1GB9iYRntcSaUsBNB3VXPXgqkdRbgXBBctTuO6IUbp87Nzb7-8D5YlMKWHllCpQVelAYGGt7AfkixBWA0jmTfzPd1Q11fYOhQTj_lk2fWUoCn2HPj2v9R6tSlUTjj9M1g0QbBhLFAByEF709hrwtQfGoR106uHbwL5JT6iDfL5MUWpUTNM6-XuNyCP2fQZs9GVXFN-3UPGCWBWYmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=VNUMHBAhIf0LQwVqgM6mGHRfeBAmG-9FghNAJYf9Lng6rrSwoe_XvcqnZim10lv9Ni8bCccDbR6q8T2Eu_owVo1EtyJ2AldPBc6E17am7zXyKfR7pXLiWcNfAWRIWDEJZLlAC1GB9iYRntcSaUsBNB3VXPXgqkdRbgXBBctTuO6IUbp87Nzb7-8D5YlMKWHllCpQVelAYGGt7AfkixBWA0jmTfzPd1Q11fYOhQTj_lk2fWUoCn2HPj2v9R6tSlUTjj9M1g0QbBhLFAByEF709hrwtQfGoR106uHbwL5JT6iDfL5MUWpUTNM6-XuNyCP2fQZs9GVXFN-3UPGCWBWYmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمارو نمیدونم ولی من دیگ از تک تک اینا خستم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8261" target="_blank">📅 02:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRODO4Iiim9q96OTKPB2qBDt2CLoS1a6ElOGPNWSNRvKDNvm3bj8ee9d0JI-jvXfSpXEse40sC1hUxYU2z7t6oHaTPucgreTE3WK37jB9Lziyx-YwR8RLO622kQavovB8Xfr00KFMwRERL2pvYaKPoYRrsFM_-hwlwAw-ooCtMm8MBhRvWOiB2AunvT9jsVH0u_kXD9RaUn0NlLbu8-nhDPC72E-utGam5SvxJHOvL7d_iSTlmKLq36T2O1BamdjuwCCG38r8U9RoNvz-0dLAtV3Cafbjmm715U2PNyb51zV2Zrplv3eSpkyacKktl_5dOJRYZdfxp-gly1aRAoc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
- ایران وارد روز 64ام از قطعی اینترنت شد.
47.500 ری‌اکشن فیک:
🤩
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8260" target="_blank">📅 20:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Injector.ehi</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ اینجکتور مناسب ایفون و اندروید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8259" target="_blank">📅 20:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دلم برای هدر دادن وقتم تو اکسپلور تنگ شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8258" target="_blank">📅 20:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhFmXM99k_S_5z5DCGRbkYoUBOrgB5xYPWWftGJcCV4xTX_oBxENx-nvO_0lKRrIgSA6JCDYbsvCQLm4npga-uft4m8o1124us5wvTjdDTty-k3TwUmXi0p9dpXP1hCMtTcUHGmropWq0Yv5YtEzNuRZDxr01nzskdkYxhmCqWkdMjML_LprFUjMv-veX3ru4_UYChqksI3U03R0nU9bXJg7vLdL4MDw1KeVVFMTbqQSOCnB1sY3EIzaW7Wp0EBeWWNRaEREuJY3Cu88mJXdyqOXMdvskbuAY_7TV_Z1Vx52nWZsKz3mMNTQl9jhiZgumKtedhJuA2SuOJFGZiZNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر سال ٢٠٢٢ پیش‌بینی کرده که سال ٢٠٢۶ هانتا ویروس مثل کرونا شیوع پیدا می‌کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8257" target="_blank">📅 19:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آتش‌بسی که نقض نشده رو میشه نقض کرد ولی آتش‌بسی که خودشو میزنه به نقض نشدن رو نه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8256" target="_blank">📅 19:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEn_YtnRNGhrjWOKtZGXMUlawz2o5EQHOK-s0EPpRTMs5lz8pQnshhRPnexLlXw2PLqZJ4TjyN57YFWYV-v-aigBItRCbaHYtsREFmyvNsKGnUl3b2gM9ADHSJcCC01umsO30jl9bS74uCsBB_kJZ_6828GyH9ouuti3pRYMuDHpcT6hEfPq9mamDSaP1RM6-wFKVYfsnVHCLR-epWHHQom9gFgVN-o78_K3wGrEtwv9fo6BpjuyD6kXz8tR72dNJvwhU3RfpJ5Lh9K-VcC1J1KjUXWgoY-vYvXbgnbgF9S-WUFUpLO-v9yRc2ybYv8YmtxiEoTEb9n3RvPA-AQT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم تحویل جایزه چالش امروز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8255" target="_blank">📅 18:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFEkcGRNzJwwfnNgBuXITtWzU77Cc84L8QOE8fQEPjoCzAT3tgntMHlzcTpBs3n7CfPoMhCkGSp0Jqg0XoiBEdH90rP5E7QOxOeUF9QtWWaR5B31yafNiL1HQsmyIN6_6jbdOSJ2f1m46xn_jYQeJKwVCOLDL4I9cSi6YQKcogx1bv5byRQbebGt-SGyGaX5aEpI9ejjLMmOOf_o49QW5dmdu3Yxbr1LQ1bQnSLDFp8LMwWSwTTEF43Fz7FEibdVoM2ECMA1l7y-UclTcHaKQltm6wnOOlLC_TTtYbqtil4HQI_kAqgOlWeMZ8liWGAoWWze1FAlyjYEkwnSSV8N_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پستی عجیب در پیامرسان های داخلی در مورد فیلترینگ و قطعی اینترنت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8254" target="_blank">📅 15:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJv9FqJas6cVKyWBLjXaO9oyXyAQzKFVeAxkjdec3bochlsevSXp-icZZnxofMOnuqx52MCLHNyHRE8zuqdizb5ugEt9xtl8opU3cLXS4YAA6sXTb0Y6fIB3xL4Q7V_HDDwOF958HP-2sLT_rr-H2JFBQRIwSGUqm9T7baXOaaxJ2xIFl_ANNFgN8iQV9adwPC6x3rBFo7BBkAj7ChP97gqlCgtlF117LxSvM-W5sI9OUZ-iYZ9OFVVe2xD9YZqs6wze_0_PeFdvzbvYSm0y6kbgJqIsNujm0CxNmdnkMiEJ6h5g5Rq21PyROIFn2qGAZiONgsgZC2CEJ4G7WhlpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی اعلام کرد که پدافند هوایی این کشور در چند ساعت گذشته ۳ پهپاد و ۲ موشک بالستیک ایرانی را رصد کرده است.
این حمله منجر به زخمی شدن حداقل ۳ نفر شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8253" target="_blank">📅 15:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il0gMpVE6n6Y61Be3E_HKd-CXANGXkf0--E770LzSWh-6LJqjPbMqgvoHU6G2aI5P1-3G78wSSKBIlm9XotHU5P2ur35Kbe8SLWqPJ8brKja0vqiOCvDwMHnt7_BTb-kgND0YDnH8bmJ28XGetO2cdbUmnlCvbFxQd6aaUAdN1UsnvKJQzEY0SBzKWMVralemaZnCRLYvfi2oCUyC9VXgx-WFLZbqsnb73yMLIf1MEOTWOdBgT611AajihhkftZLlG4yS3utkpikVY91G2Bkz5nDo1HlEtkhbC0VCiPfdMUpL3xOUeWvvpyZfKj_G18IG-wAh0FbTl6TKlcb-rSe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعی اینترنت در ایران  به ۷۰ روز رسید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8252" target="_blank">📅 15:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔸
منابع خبری از شنیده شدن صدای ۳ انفجار در امارات خبر میدهند
به گفته این منابع خبری ۲ موشک بالستیک و ۳ پهپاد به سمت امارات شلیک شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8251" target="_blank">📅 14:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAxSDEz26aJjTn8roch7sLcTkIUUkJ_CLFOTNP2RLqTfIYouGxyEFy8ZwHK7Y34fRUySdq5yhsvSDydtVQq0JlwH507oj_srjX1GXnSoaXW2hanCZafSVkFC1mZ42RYWGtlXOhqbo185UvLQWzslG8NWaB4osCmGcOWJYQrfNAFbxlp3B1KqNMew9NLaKRCS629C_v0As_nRNfw65D9wyATt_SMhoi5eexB85qYHZ8YiZ_fnDVgBa0gIjxwg4e1Ss-9fpe23XkUEhz3tK5XjlJzm-faXM7najVKu5T_j0Kfk923ldShwNrNCfS40hPQzpFKsx6ml_IWRimMU7gNdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال
لیزرها: بوم بوم… رفت هوا!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8250" target="_blank">📅 14:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری - حمله موشکی به امارات
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8249" target="_blank">📅 14:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
امروز روز جهانی خره این روز رو به خر های زندگیتون تبریک بگید
🐴
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8248" target="_blank">📅 13:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">https://t.me/IranProxyV2/8243?comment=7857
🔗
https://t.me/IranProxyV2/8243?comment=8191
🔗
https://t.me/IranProxyV2/8243?comment=8409
🔗</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8247" target="_blank">📅 13:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMIlad</strong></div>
<div class="tg-text">https://t.me/IranProxyV2/8243?comment=7857
🔗
https://t.me/IranProxyV2/8243?comment=8191
🔗
https://t.me/IranProxyV2/8243?comment=8409
🔗</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8246" target="_blank">📅 13:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
اینترنت رو تو سکوت بازم گرون کردن
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8244" target="_blank">📅 12:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8243">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎰
هرکی 3بار 777 بیاره توجه کنید 3 بار برندس این بار ربات ایدی هارو خیلی دیر میفرسته
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8243" target="_blank">📅 11:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکانت خودم 11:16 استارت کردم ایدیشو نداده نمیخام بی عدالتی بشه دیدین یکی ارسال کرد ایدیشو اصلا نفرستاد تو قرعه کشی شرکت داده نشد</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8242" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه قرعه کشی دیگ میکنیم این ایدی هارو خیلی دیر میفرسته به درد نمیخوره</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8241" target="_blank">📅 11:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب رفقا من با اکانت خودم استارت کردم خب ایدیشو هنوز ارسال نکرده خب اگه دوست دارین صبر کنیم قرعه کشی کنیم بگین یا اینکه یه قرعه کشی دیگ
❤️
صبر کنیم
قرعه کشی دیگ
🔥</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8240" target="_blank">📅 11:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تعداد کمه حدود ۱۵ نفر شرکت کردن احتمال برنده شدنتون بالاس فقط یکم ایدی هارو دیر میفرسته برام</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8239" target="_blank">📅 11:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب یه قرعه کشی بزاریم ایدی هاتون استارت میکنید برام میوفته تا ساعت 11:30 هرکی استارت کنه بینش کانفینگ قرعه کشی میکنم</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8238" target="_blank">📅 11:04 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۲۸ دقیقه دیگ قرعه کشی میشه</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/IranProxyV2/8237" target="_blank">📅 11:02 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه ربات پیدا کردم میتونید ازش گیفت رایگان بگیرید یه گیفت ۵ دلاری داد دوست داشتین استارت کنید ببینید شانس رایگان به شما هم میده یا نه   @FreeStarsGiftAirdropBot</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8236" target="_blank">📅 11:02 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">https://uplod.ir/4gza58rw4dcr/126.zip.htm
نسخه ویندوز هپ
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/IranProxyV2/8235" target="_blank">📅 10:55 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTGlP9OhXdCouGOpwrW--2CBo7UqJfX_hmG9vfwfcWjKucd5sbWgAAJabeTLVBmlYu1TbgGQx3ddtmHV3gTX4PD6sj3ukbCuDkEKZgI7_uitv-sgIwFsbmgn73kS8qAGd3h4HkBMzi1qnfe9_cug4viBb4S7vR9-A82j-LJAjDjdvwGRx_tbE3hf3n0obSkauCbBtSUjn4JvH5qzvWJRE8FcJkhKdkfc1UM6aZDyg-HcpghYLWko1pg_-_XMZdlAk5Mr6Jqpg_JJBCZ9POUWbNdufkYrYBtiEs8INNp0pyuSK_TKA12jYDDTlQ1tEmto644UdbiLpgWLQEbDhTxvlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ربات پیدا کردم میتونید ازش گیفت رایگان بگیرید یه گیفت ۵ دلاری داد دوست داشتین استارت کنید ببینید شانس رایگان به شما هم میده یا نه   @FreeStarsGiftAirdropBot</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/8234" target="_blank">📅 10:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه ربات پیدا کردم میتونید ازش گیفت رایگان بگیرید یه گیفت ۵ دلاری داد دوست داشتین استارت کنید ببینید شانس رایگان به شما هم میده یا نه
@FreeStarsGiftAirdropBot</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/IranProxyV2/8233" target="_blank">📅 10:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ویدیویی تو شبکه‌ های مجازی داره وایرال میشه که ادعا میشه علائم  ترسناک پوستی فردی رو که به «هانتا ویروس» مبتلا شده رو نشون‌میده :  کم مشکلات داریم خودمون الان باید دغدغه این ویروس جدیده(هانتا ویروس) هم‌ داشته باشیم؛  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8232" target="_blank">📅 10:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b47fb12e.mp4?token=rE5Loo_nz2bEfb3VMKU6-eriVm4bhKESfTnM7tE8FZat4_DkEJeufFyfhG63_NFh6tnISSkOf-R3EsLkN0k5mSzLItI4D_w54QDBykDrIwr1SnUzqHfladfPfBb02UZnrx6LNbBksZDmAxn4odWFnRkLKh-ZuEWGJ2uDNoMp7AlhHFzZHay_MF9qetJ0pynUQGqB62i3Bj3xYm9ntzhc7H2iGZHnbPH0rXQ1etYywFe25xn7VPbToyP7SNSzuEZ6NzraIhssdjcKzkXqUINlghPRx7DT-NCyPRpcHAj487oa46vt_5j68QJxxeYtc2WdMEqdInV8JY7PKzv482RevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b47fb12e.mp4?token=rE5Loo_nz2bEfb3VMKU6-eriVm4bhKESfTnM7tE8FZat4_DkEJeufFyfhG63_NFh6tnISSkOf-R3EsLkN0k5mSzLItI4D_w54QDBykDrIwr1SnUzqHfladfPfBb02UZnrx6LNbBksZDmAxn4odWFnRkLKh-ZuEWGJ2uDNoMp7AlhHFzZHay_MF9qetJ0pynUQGqB62i3Bj3xYm9ntzhc7H2iGZHnbPH0rXQ1etYywFe25xn7VPbToyP7SNSzuEZ6NzraIhssdjcKzkXqUINlghPRx7DT-NCyPRpcHAj487oa46vt_5j68QJxxeYtc2WdMEqdInV8JY7PKzv482RevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی تو شبکه‌ های مجازی داره وایرال میشه که ادعا میشه علائم  ترسناک پوستی فردی رو که به «هانتا ویروس» مبتلا شده رو نشون‌میده :
کم مشکلات داریم خودمون الان باید دغدغه این ویروس جدیده(هانتا ویروس) هم‌ داشته باشیم؛
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8231" target="_blank">📅 09:56 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ: آتش‌بس برقرار است
خب برید بخوابید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8230" target="_blank">📅 01:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Config</div>
  <div class="tg-doc-extra">Habib</div>
</div>
<a href="https://t.me/IranProxyV2/8229" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ مخصوص های این روز ها
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8229" target="_blank">📅 01:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فاکس نیوز:
حملات آمریکا به ایران ادامه دارد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8228" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
شبکه سه: آمریکع آتش بس رو نقض کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8227" target="_blank">📅 00:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c91a84ba.mp4?token=Ah1HOszzEjSMCZuWDG3CA0_OYJnjC2mT5H5qmX7wT9uSmbcpNItqHjMmWj8FNZ6f_5IykmdcYYMSqVD-p06DVff8C3nzNFzm3k38pT2DlMYHoLOALpRwgz4RJ9h8GgMpIojpnz3wUwOGBoHYPGq1cSQFqCIqgCG2SCxrlAeQOxF20YJQyLrzOU1Y4fWSUgr65Z6SBleDLaELI6M4j0KgQsr7vE9iWzB2ALUNnM_bdsRbY4UnGnBQwfgPL1B8xKUlQIvVtVBF0q9IClF3E_h9OwaAAQbA--b6uejBhBO9W_NPeDVvmG5Fw7HRqt5SvQCk5-KiLK6dD_HWH8uRqPwm0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c91a84ba.mp4?token=Ah1HOszzEjSMCZuWDG3CA0_OYJnjC2mT5H5qmX7wT9uSmbcpNItqHjMmWj8FNZ6f_5IykmdcYYMSqVD-p06DVff8C3nzNFzm3k38pT2DlMYHoLOALpRwgz4RJ9h8GgMpIojpnz3wUwOGBoHYPGq1cSQFqCIqgCG2SCxrlAeQOxF20YJQyLrzOU1Y4fWSUgr65Z6SBleDLaELI6M4j0KgQsr7vE9iWzB2ALUNnM_bdsRbY4UnGnBQwfgPL1B8xKUlQIvVtVBF0q9IClF3E_h9OwaAAQbA--b6uejBhBO9W_NPeDVvmG5Fw7HRqt5SvQCk5-KiLK6dD_HWH8uRqPwm0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم وضعیت سرعت سرورها</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8226" target="_blank">📅 00:40 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
💣
فووووری سخنگوی قرارگاه خاتم الانبیا: آمریکا با نقض آتش‌بس دو کشتی ایرانی را نزدیک تنگه هرمز هدف قرار داد
حملات هوایی به مناطق غیرنظامی در سواحل جنوب ایران انجام شد؛ ایران در پاسخ، به شناورهای نظامی آمریکا حمله و خساراتی وارد کرد
ایران هشدار داد به هرگونه تجاوز، پاسخ قاطع خواهد داد!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8225" target="_blank">📅 00:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش هایی از انفجار در دبی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8224" target="_blank">📅 00:38 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
سنتکام اعلام کرد؛ ما در حال انجام عملیاتی در جنوب ایران هستیم!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8223" target="_blank">📅 00:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستانی اگه سفارشی انجام دادین و هنوز تحویل نداده شدهه، ربات درحال بروزرسانی بود، الان اوکی شدهه، تا دقایقی دیگه همه تایید خواهند شد
❤
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8222" target="_blank">📅 23:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
حمله امارات به ایران تقریبا تایید شده
فرمانده کل ارتش:
پشیمان خواهند شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8221" target="_blank">📅 23:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">میدل ایست : امارات متحده عربی به قشم حمله کرده
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8220" target="_blank">📅 22:59 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بازهم ویروس چینی ویروس جدید هانتا (از منشا موش) در جهان شروع شده و تا کنون به اسرائیل، سوئیس، آرژانتین و هلند رسیده و نکته ترسناک این ویروس، طبق گزارشات درصد مرگ ۴۰ درصدیشه که از هر ۱۰۰ نفر ۴۰ نفرو میکشه  خاستگاه بومی این ویروس نیز کشور چینه...  @RUSSIAPROXYY…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8218" target="_blank">📅 21:40 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzHwkQ2CW3FvP4REXcs9uvmgEsTlwjWVS_5vhu39M5SjAzVxzBctvkD66jeissjFJDiLUzJPjtxYgy53mOrAkT4KIyKq_sQTI8utq3ElfSuQZr1MsHT8xlOqwlSSaqt7lc_5BAz7OzYGTOjQUW238Qrm0CPE3cjcgOSIGMdjGJdZo0mLFyWjNj0b9Zm-7JrgXok7D5Z9pN8j0smaazhPpRwWFCHV8fCJWGGIKpabuoVqraAaI9gLo7Kv1ZgUM5Pyv8ialZPwyuezc35FKMUbyObBmvSuKHLsL2cGdXQpfVIOanfFK0IvBRFZ9K5vcqAQJKlaHS6xFm0csZ6R5Qu4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازهم
ویروس چینی ویروس جدید هانتا (از منشا موش) در جهان شروع شده و تا کنون به اسرائیل، سوئیس، آرژانتین و هلند رسیده و نکته ترسناک این ویروس، طبق گزارشات درصد مرگ ۴۰ درصدیشه که از هر ۱۰۰ نفر ۴۰ نفرو میکشه
خاس
تگاه بومی این ویروس نیز کشور چینه...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8217" target="_blank">📅 20:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d0c82f90.mp4?token=VHSE3Wp1xuQZo_K7lFMLdcRss0WhnXTFaCIhzor7zES8txMufnR5BTfPP-_ma9UqXmyRVpWDoiezsk9XY0E5u1x_7N-yYLMXySQ2dI_0hp-yh8EKqk74MZjT_zksua56zkG_EatwopFO53Piyke0Am1UfVuHDJP7EX5e2GFbO8Pp1qtc9QgscE93DiFYC4d_9xKK7HEKqxzJ7o1ZGHsd8FBMMnw9ucL4oJIVfT9Ke0aGVLH3SMsEkP7utHf05NDljDN0WVZpRS9dNNAPG2EgtrkHf_0w3xMQu96Ubf75EV3MDV6x2W9Q9m_Bw1wC_mWThV6YTkWjSEEl89vhFe5RqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d0c82f90.mp4?token=VHSE3Wp1xuQZo_K7lFMLdcRss0WhnXTFaCIhzor7zES8txMufnR5BTfPP-_ma9UqXmyRVpWDoiezsk9XY0E5u1x_7N-yYLMXySQ2dI_0hp-yh8EKqk74MZjT_zksua56zkG_EatwopFO53Piyke0Am1UfVuHDJP7EX5e2GFbO8Pp1qtc9QgscE93DiFYC4d_9xKK7HEKqxzJ7o1ZGHsd8FBMMnw9ucL4oJIVfT9Ke0aGVLH3SMsEkP7utHf05NDljDN0WVZpRS9dNNAPG2EgtrkHf_0w3xMQu96Ubf75EV3MDV6x2W9Q9m_Bw1wC_mWThV6YTkWjSEEl89vhFe5RqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان بهداشت جهانی اعلام کرد که تاکنون ۵ مورد ابتلا به هانتاویروس تایید شده است.  پزشکان اروپایی هشدار دادن که اگر جلوی سرایت این ویروس به سرتاسر دنیا گرفته نشه، با یه‌چیزی فاجعه‌تر از کرونا روبرو می‌شیم!  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8216" target="_blank">📅 20:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgvbTnUMyd6NSrMKMxSeKX_YuI2Q2EOKVB37TrsQwDBopRfF-Mzp2Hy-MQdfK92sLvhlcCs9O5pMM0-3rXxeVZ_HWG04xlHi9O0_UZYSTgOkf6Mc7vqqUq1V8Ll8zn6PSs_RQ2P21XV3F8VVPTSdkX42IsVsxy5NwDxM_sUPAd6PXQtVK3ON3f4Rk9fgFJwI6C3eS3IRglem1PtsJjc_d01UQGmHbRrZN31RWWzsVqd_tu_J4MWuTTk_SmLtGEz_Bt0EteaQEQ8UUkmVNk3V5fSih61Qvr9hlZ9zwcBn5S_lR6rSUS3c1FakZXH7E3Q5B27Meiis65NRlj2QRQsrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان بهداشت جهانی اعلام کرد که تاکنون ۵ مورد ابتلا به هانتاویروس تایید شده است.
پزشکان اروپایی هشدار دادن که اگر جلوی سرایت این ویروس به سرتاسر دنیا گرفته نشه، با یه‌چیزی فاجعه‌تر از کرونا روبرو می‌شیم!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8215" target="_blank">📅 20:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری CNN:
انتظار می‌رود ایران پاسخ خود را به پیشنهاد ۱۴ بندی آمریکا از طریق میانجی‌ها تا پایان امروز ارائه دهد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8214" target="_blank">📅 19:40 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
وزارت خزانه‌داری آمریکا تحریم‌های جدیدی مرتبط با ایران اعمال کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8213" target="_blank">📅 19:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آدم میمونه بخنده یا گریه کنه؛ یارو یه ساعت اکسپلور گردی کرده فیلمشو گذاشته تا اونایی که توانایی خرید VPN و کانفیگ ندارن نگاه کنن  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8212" target="_blank">📅 19:09 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8Kjb5453waMkzLH1qMYMtfIA1Fwoua8Yk8lfPIXMU-A5_HdfLaClinUvdgY8H-5D4hB_1F611Gpyzdox5tNVNlsDkKTMdvGl-rP26bAKUI_zq0z9mnJC7L-BzFVrmeh9_UWfbJTvKolLfM67qk68VWxjKEWNiLTKfdcdfMOZV70zRfdR79w7kWw18heahvFbdDxIAK4AtJaxMrmvr_5WTZ0gspT37b2gMTWZFpJQ8SlcxLpHEbXN6f5XGkzQeQA_6lHCloN9LcoocN3DTK96PB_YN463OpHHuUf8IgSV_VwiGBImL3R8dF9El5wm_QCvKap3UjUZ9vFNOZHJ2YXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدم میمونه بخنده یا گریه کنه؛ یارو یه ساعت اکسپلور گردی کرده فیلمشو گذاشته تا اونایی که توانایی خرید VPN و کانفیگ ندارن نگاه کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8211" target="_blank">📅 19:08 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8210">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef81b4529.mp4?token=kJqXr3Dn_5PBYC2lKtSOrUKsZiTvFso318GhIEa38jDpIDHhyS7Gxxlk9IoHfUVvacKZXLNvhTTv-57XyY71_kcSZiopYqjxLONfkUMe78y7LViVwS8gRE68WSdOvPP1W-dn0kGWijCh0xbRHeN8hdKIQ3yZ-hWI2RV-x88TbhIekQwHBLfob6aV6RCGXMPIOm-nbycseWrFdsQa7OPYdejoIiqJ1fSK5g-ZcqMfUtVpeJptMU_3iynTCGOeE2ucKMJ0jtbtw0-agLdnftpUMBkeQbUUqYxzTFP--tlkRx6xi0nDY7wSibtgWI3M2cPmgqyACpWbeq3JzNxd_eqtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef81b4529.mp4?token=kJqXr3Dn_5PBYC2lKtSOrUKsZiTvFso318GhIEa38jDpIDHhyS7Gxxlk9IoHfUVvacKZXLNvhTTv-57XyY71_kcSZiopYqjxLONfkUMe78y7LViVwS8gRE68WSdOvPP1W-dn0kGWijCh0xbRHeN8hdKIQ3yZ-hWI2RV-x88TbhIekQwHBLfob6aV6RCGXMPIOm-nbycseWrFdsQa7OPYdejoIiqJ1fSK5g-ZcqMfUtVpeJptMU_3iynTCGOeE2ucKMJ0jtbtw0-agLdnftpUMBkeQbUUqYxzTFP--tlkRx6xi0nDY7wSibtgWI3M2cPmgqyACpWbeq3JzNxd_eqtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/IranProxyV2/8210" target="_blank">📅 17:06 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
