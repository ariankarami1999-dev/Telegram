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
<img src="https://cdn4.telesco.pe/file/ZEA21uWy6n3MfH1OqXrKVl65sgu9XL6_bqYWCqkGc7j4DhF4U9ZDAr-X6uIjs-NY2vZq4_SMoIFm78M_pbg1GZJezDSAsKJkvRCEsv8rFmbg6x1hz_nTH4ktD0mXMyTEuQDbnyEmS9_xNrRfeK2zTctc5Ar9pnTzaBWclzCMmpe7aa9AhC8rTv953JKTKz_fNTXydGcCZHv-llZKFYIYDITjxENe727i_0ytX1-zoy-H6MuysUH_4gdc-WZUAKAtUXoKEjkZ5svIwz0FWxQmOY3kXzYuLf5l_5NgQprl8I4plqkmeOsMJyvhgZaiLK0w0q2Z4Dh890DUF-OQA0GrcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-144126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراق برای نخستین بار از زمان آغاز جنگ علیه ایران، به خریداران نفت خام خود این امکان را ارائه می‌کند که محموله‌های نفتی را خارج از خلیج فارس تحویل بگیرند
🔴
خریداران می‌توانند محموله‌ها را از طریق انتقال کشتی‌ به کشتی در نزدیکی سواحل عمان دریافت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/144126" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رسانه های عبری: اسرائیل به آمریکا اطلاع داده که از عملکرد ارتش لبنان در مقابله با حزب‌الله ناراضی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/144125" target="_blank">📅 20:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTk0Udr1q3kdzveNFM3gYL56HqVONw_mUDeJkvddZJXRddWs7jG2k0EVV3M2wuSd2KshFQxj1YUSp60QMXdZR2OSpoBHKII5BChNnWwbr-RmLd68LbRTNbzi92KovX8AM5G8LzR5Jz-4AaVXqR0X4cJ_07U-d6I_Y8oBmzYJDQDFklWyUn5xNM6Scwn_bj3GR7B9tzRB9xXLPuHJsvJl1n-6HL4Lbh7qw35zREunjDrP-KFWpDnedo--iHc2GyCkPuKK5TMxIkDAErUMeo9lWvUy9MW1U3QsJTKc9p0DzsOFShxdqK_RKI4ivzqlvKRHRoaGO1nFfrRy5Mqs9BAIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امشب یه ماه‌گرفتگی تقریباً کامل که بهش می‌گن ماه خونین (Blood Moon)، از سراسر آمریکای شمالی و جنوبی قابل دیدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/144124" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ادعای ایسلامیک مارشال محسن رضایی: آمریکا شرارت کند بلایی سرشان می‌آوریم که در تاریخ ثبت شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/144123" target="_blank">📅 20:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144121">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef01d16472.mp4?token=vYWG7C8aDerStAVo9Et8DgzTSuDV0C6QwftpGwZgo6h68fW4iNRPXgfVV0781MOhW2AX8tvfq16Rd00h0A_35EAWR2hbfR0SAnEGG7Ci60NEsDNfnoVJS0rZYDxLYOxp75eLKp95aDbwhOGnw4NDHO9v5pt-qO-lwdY7o-5DpDXYQjF9HS4UiQmWm2FhsQBY770wnfyDjHm-ejEPwmza5syFB_-2SUS24NGQ1pEd5jTOY-SIRPsTm2ZvGkNBW1RcUGZjUJYkG4KqauhYlx56X1YfU8tgAL-y417hMYAmZoF54p-C-Tul53gH-Qxu3DIcs2OT1YvpLVcoAvlSjl8zmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef01d16472.mp4?token=vYWG7C8aDerStAVo9Et8DgzTSuDV0C6QwftpGwZgo6h68fW4iNRPXgfVV0781MOhW2AX8tvfq16Rd00h0A_35EAWR2hbfR0SAnEGG7Ci60NEsDNfnoVJS0rZYDxLYOxp75eLKp95aDbwhOGnw4NDHO9v5pt-qO-lwdY7o-5DpDXYQjF9HS4UiQmWm2FhsQBY770wnfyDjHm-ejEPwmza5syFB_-2SUS24NGQ1pEd5jTOY-SIRPsTm2ZvGkNBW1RcUGZjUJYkG4KqauhYlx56X1YfU8tgAL-y417hMYAmZoF54p-C-Tul53gH-Qxu3DIcs2OT1YvpLVcoAvlSjl8zmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب یک ارزشی در حرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/144121" target="_blank">📅 20:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144120">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udNFQO-wkSA-bHFfRcHWGqvItobz1vW1HfouYSx2oE1LTY1DP8KP4mfTQlhTJDQPV60stR8wI0awVgXnA4wOYzoeOE6QNxZDH91TvHCgzFSqYM1advxFD2Go1jMpKUpzrKYhfogyfrYXVoDK48Enk1tfPQDAELs5VsKOQIGoJWEgXTKvTX6kcmmfmOWHCMbsmVBVjGlZ4toY-h4aogO6w722cnIlqkao_OBSwoSBP194EdNI4JVYQSxPUUpgRRnTawlUUPZzaTNZISddpvdLlUoOkcNgmgZBiAWcWKnggR0GYG-GRVra2M2ZNUxrldGnJ0k1GixPheUb80y2bfec5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان UKMTO تایید کرد که تانکر نفتی کویتی به نام "السسلام ۲" دیروز در حین عبور از تنگه هرمز مورد اصابت قرار گرفت، که به احتمال بسیار زیاد این کار توسط نیروی دریایی سپاه انجام شده است
🔴
این کشتی پس از آن در جزیره تواککل کشور عمان پهلو گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/144120" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144119">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
اینروزا این پسره حسابی سر و صدا کرده با سیگنالاش
🔥
هرچی گفته سود کردن مردم
😐
الانم یه تحلیل خفن از طلا زده
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144119" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
منبع آمریکایی به الجزیره: هیچ مذاکره‌ای با ایران در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144118" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منبع آمریکایی به الجزیره: هیچ مذاکره‌ای با ایران در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144117" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW6IPQZyT6-Q5BYireJnq9kyfxJl06deiqXYRRej5atzaGuo3vnGndQ697FnWgh53_Yd6mhneyza3myan-iyZkg2a1TOwfMU68tyfWKijt5crreQ4VhHUmvQpyiWM9GKOccvFbiGB0YEAkMFJRfIPVBA5pkzMe1T5mBsrsOKZhdvvqPb7I7VjaDMBy_apJe_3wcuFCGz8fRyCi_s53wMa32Ngx0Rf1RXTOqH1iRzfamDSCfksKBgQwq8PpejceC6JeSq8KxKD0QXy89PAPSbX3VlwwVeIb4hOlrhx39yfJW4xUv7up99wvr9lTODdQvCi-Mf99HW5Mt4jEdv0FDPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط کافه بابک زنجانی پلمپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144116" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: منطق حکم می‌کند اجرای تفاهم‌نامه به همان شیوه گذشته از سر گرفته شود و مسائل از مسیر گفت‌وگو حل‌وفصل گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144114" target="_blank">📅 19:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDqvuuEXC0299cC5giX_n9XXxf9fThHaeeacV1KI-j4SGAKSOsakGpxblzJl3vg1_RZDrbgTymLUmf5BTdE4cAcSeyaWi6V9FZhGw9WJ434c5QQLMzfKAX-DsLRQsAFnbfE9-yR8KZa_qAVUMLNIxL0RYuS-Gp2jtHFyjVvUaBsoc4rTHAeYVGdDYyq7MXH_jHBRoaQY_GA_MDyB0qriGmuU7AES2bRsVPuhVDK1Gs-3ToZ55CUvVCgHcqqugSbgkGrAlZg4Lmw4CPb-FQWx7zRbvMoaWXHcSj8kC3tJ0C0FmMrI1A75CE79Fx3im9HZzEgmXnMce244DrpXy2-kHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: همه چیز تحت کنترله
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144113" target="_blank">📅 19:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6kQ5SwAvNIYIqACLZlhTRlpShpdSeGO7HfTNcYjhbyH_dsrivssxsRcC3C949EnR_roAkvb_skX9az9muJmeRTDLf3eo9RjRocBTeHguqjZtLKsFIQMVEf_702dXE2DcRwkZg2wukwpCOawx_2iBKNKMsIZ57HnBKkKl9s7SVXt0FbYFvB3DjiEwgX72REi2aYrQggW0QmvRSXLmG3AeHh6_3PnRnzeCB1I5uP3igK5vJsSmPSUrFrHkrv56f1d3jVTepvArKd7fPFjdzAFx8RH1KNIYKV8FRSe-f091gVP9yUJ5JbAjEIDOu0kog0CUch_Jwj-0krjLLlR2ZFJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رکنا: زهرا متقی، دختر ۱۲ ساله اهل لشکرآباد هشتگرد که ۸ روز پیش ناپدید شده بود، در شهرستان چهارباغ پیدا شد و به خونوادش تحویل داده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144112" target="_blank">📅 19:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/144111" target="_blank">📅 19:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خارجه قطر در دیدار با پزشکیان:
روزهای آینده پرکار و پرفشار خواهد بود و تیم قطری از فردا فعالیت خود را آغاز خواهد کرد.
🔴
امیدواریم تلاش‌ها به نتایج مطلوب منجر شود و با بازگشت به فضای دیپلماسی، راه‌حل‌های عملی مورد بررسی قرار گیرد.
🔴
اطمینان داریم رئیس‌جمهور ایران از تلاش‌ها و تحرکات دیپلماتیک حمایت خواهد کرد.
🔴
درباره موضوع خلبانان نیز درهای قطر به روی ایران باز است و مسائل مربوط به برادران ایرانی با صداقت پیگیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144110" target="_blank">📅 19:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر خارجه قطر در دیدار با پزشکیان:
شیخ تمیم، رئیس‌جمهور ایران را همچون برادر می‌داند
.
باوجود تمام اتفاقات رخ‌داده، احترام عمیق و صادقانه میان دو کشور پابرجاست.
🔴
قطر به دنبال بازگرداندن ثبات به منطقه است و دست گشوده ایران به سوی کشورهای منطقه و تلاش جمهوری اسلامی برای تأمین امنیت و آرامش را به‌خوبی می‌بیند. امیدواریم با ادامه این رویکرد، مشکلات پیش‌رو برطرف شود.
🔴
مردم ایران برادران دینی ملت قطر هستند. جنگ از داخل منطقه آغاز نشد و از بیرون به منطقه تحمیل شد، اما هزینه‌های جنگ را همه کشورهای منطقه می‌پردازند. شرایط کنونی مسئولیتی مشترک بر دوش ملت‌های منطقه قرار داده است تا امنیت، توسعه و پیشرفت را برای همه فراهم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144109" target="_blank">📅 19:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان در دیدار با وزیر خارجه قطر:
اتفاقاتی رخ داد که قابل قبول نبود، اما همچنان بر این باوریم که ایران و قطر دو کشور دوست و برادر هستند و می‌توان مسائل پیش‌آمده را با تفاهم حل کرد.
🔴
اتفاقاتی رخ داد که قابل قبول نبود، اما همچنان بر این باوریم که ایران و قطر دو کشور دوست و برادر هستند و می‌توان مسائل پیش‌آمده را با تفاهم حل کرد.
🔴
مسئولان آمریکایی باید صداهایی را که برای جلوگیری از بازگشت آرامش به منطقه تلاش می‌کنند، نادیده بگیرند. منافع عده‌ای در ادامه جنگ است، اما جمهوری اسلامی ایران معتقد است صلح و امنیت به سود ایران، منطقه و جهان خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144108" target="_blank">📅 19:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXetL2MD8jpMv1-kisxmej_r1z8oGrR8pTmzLGSMKXkaXGUJC3t4T6sK7XKQaSt-c2h7RabrzsZ0myE1mEKQtWKBDsMOAJhGH3H0Gg0dpUjApHRsMdZiwFl_2VVX9l8_hoKmzagvlY_QJkQaCOTw5ix8q3FOL-8m36cDTmpf3-aCzITCBTj7Ex7QEv2PKm59koXS_akWJn_94EU34HaCvHLs7UdOl8pYeM6PvzTAD50uWTXEh05J9YSt6Op0arqmhT5quqcsswuxANpD-cIT8oR0-46tBEIU2veHsD3dpB7DevpCorHnILbH4jDro8AN4M_GD_dlTqjxLl0Ko8wGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام اداره راهداری البرز، عملیات روکش آسفالت کنارگذر پل B1 آغاز شده و طی چند روز آینده به پایان می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144107" target="_blank">📅 19:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
علی الزیدی نخست‌وزیر عراق با فرستاده رئیس جمهور مصر دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/144106" target="_blank">📅 18:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-WScbCGysEBq7BaeT_lnQS20HvGHH395_gwFog64aQzRD_zah37TJOhZUJci3XKln528E8xFrpjvYjdaxg2XgWjcFZ7J6miQWeQOsCB7TsI7dazKKVXjw3dbHU6nUVNJYTqeqYGAOK6JHRbSO0Fe8-odeXkcirwai3nrW9mZsJZEDzteoTVbbgG1YMrF_Kqh0kxSxkNfRQyQ7dzwGrexZ5adoNyBlK36yXLtgRcgcv6uiq82spCHXQpZPUZ4cThjcs1Yt9c-YsEzZLLodsG-qPIM75_N6tJU4paYFU4fApH5Twr0InD762KBlDBOm4cwh7rk-TIuqK2b3gl8m5WGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): نیروهای دفاعی اسرائیل فرماندهی حماس را که در اسارت ادان الکساندر، ماتان زنگاوکر و آورا منگیستو در نوار غزه مشارکت داشت، از بین برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/144105" target="_blank">📅 18:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZESZSKbs-xtihGjpv7frkOtp74vCTdybEu2NrLQoImZwfk7qp1uBUVMSq8BpFhTRidJR0mA8GJ3wPnLNKBO-gFP2x699Eg4ynUpXCes9XYpJ7kpeCP3qrs-oXHxy3v4Ure38Dunhk3ygnV76qcYosGfNtIm6fQtxtycf5_Evc-4obokwplDPJl8rDFH8LJEbZOxz_MgC_uQz_5Kk_Q_WD6__p5s-DLwWnlA-5SPzx2fix_yTJdNL8mih3D4ZaHRg5n7FIDShdLS2CJBtTTF2xkhgHbVH_Xg1XgLyLnJ2cKG-PhhTclmNQ6Aj-n1eTYvrqHDBEPPDZnv33Kds56Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه قطر با پزشکیان دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/144104" target="_blank">📅 18:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، برای تولید برق انرژی هسته‌ای داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/144103" target="_blank">📅 18:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
حجم بسته اینترنت "نامحدود" شبانه همراه اول از ۱۰۰ گیگ شد ۸۰ گیگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144102" target="_blank">📅 18:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqlOv3Yk0fz9g4LYmoZ0PkSda_f1iA4_1q2ltl5uz5tNVjPfqc34V_YO1vAWETUzEvFy1oD22MFLnvtgjIQSvbmUrullqexM3shFZg7pw-71MYhpo6OAZGagLXhg_TS5q17tbMOnhhvH4LOteVlGXVqYgRGCGeQ2qVd4r72eGz3q0W6ZPk1npBDrHc6CViTnQFZPCC9CbZNvx5XA9-Lm3VgJzul3Fxdmicx88qI7N4XaAlT3oMmY0gIhBJ9ZDLQRGgMfovoLff4Yjuf0fXN7dJIsMoKb1DYptr8QSDn2OnxgwpEB11Em65Qbehntz8W6a8NHsKrGIc3p9fBMDAAfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سارقان حرفه‌ای در یک عملیات فوق‌العاده سریع و حساب‌شده، موفق شدند تنها در چهار دقیقه، گنجینه گران‌بهای عصر برنز اسپانیا را از موزه «ویلنا» به سرقت ببرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144100" target="_blank">📅 18:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۷۵ کشتی تجاری را به مسیر دیگری هدایت کرده، ۳ کشتی را غیرفعال نموده و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144099" target="_blank">📅 18:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68c118693.mp4?token=GtfTrue-zp_Arnv7-cpYeAd-wphxwJQz_VGnmPm9s37PYr5JQmHVBFOtheWJuvEOcfrlbg0I047uEgQAjb4CrVVz6Gykx6Wp1B8enGHhiI5feeBx0vBeRqxzgsIxKChDRws1BwJYo0SYZCYEb5euqAfi2HnzJZWADH-HdaFPBWP0Baxm1IO0w9GA5AmVMySi-c4dI0JVSHmPuG1x46s8Q7CyYlkut17_8mznp7bdHrAR1_SAUJIRg0foNMqnKF9xHwmjfVGaI1HpNF5lcwbtSMA8in7xYGw-QW1tGi4eqc5ZiT_JrPL6fKJiwGGeBEv-sq-WrjQcv7V8GNZFiEI5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68c118693.mp4?token=GtfTrue-zp_Arnv7-cpYeAd-wphxwJQz_VGnmPm9s37PYr5JQmHVBFOtheWJuvEOcfrlbg0I047uEgQAjb4CrVVz6Gykx6Wp1B8enGHhiI5feeBx0vBeRqxzgsIxKChDRws1BwJYo0SYZCYEb5euqAfi2HnzJZWADH-HdaFPBWP0Baxm1IO0w9GA5AmVMySi-c4dI0JVSHmPuG1x46s8Q7CyYlkut17_8mznp7bdHrAR1_SAUJIRg0foNMqnKF9xHwmjfVGaI1HpNF5lcwbtSMA8in7xYGw-QW1tGi4eqc5ZiT_JrPL6fKJiwGGeBEv-sq-WrjQcv7V8GNZFiEI5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی سودان، یک انبار سوخت و تجهیزات متعلق به نیروهای پشتیبانی سریع (RSF) که از سوی امارات متحده عربی حمایت می‌شوند، را در شهر مرزی آدیکونگ، واقع در منطقه دارفور، منهدم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144098" target="_blank">📅 18:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpZMq8hII5aE3ugVJkGCerwLrBvndCt9Pq6aA3YtZUztO-w7GzfPxRaPu_-eco76ub33MxvPXaxJyqrqMUrMeykd_ZEaLxh4hUcPL5gi2kFjKUbRzYgQ40KheUX6xTkxjZKoQn5EKUR6p3S9aXbiiW0vVJ0ctVN9TYNqNGNistOWDtAywgaP3gfTzFXa8GByTyfXfuK9SyhCHg6D-Z9lR-J5oKcoboRA-RyKwJJb_ezg6zhd9sUwmoXzGzBQGS4B1cVge-JdTq0IgbUp5d9mN8V-KC9c1ov56LAO2AT-tLmNTtmvRZQXgjpp1N4o6ozc7fgWwXTL9yJZcllKRdSZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیلا ابوالحسنی ۴۳ ساله و مادر دو دختر نوجوان تو شاهین شهر که تو دی ماه از یک مغازه ای که درحال سوختن بود فیلمبرداری کره بود توسط دادگاه انقلاب اصفهان به اعدام محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144097" target="_blank">📅 17:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUWxQNBwq2NA49O3kuDfDyCkxbkti18ZBv87AAPUqGQ4Ne1A9l0za6mm5riq6n1_eIsZyrHL8OJuctBtnt9NIflEV_csHz0fvkUOIru0IR3zx1GEUN0NqiTiuBA15TNxiirWOjiwPOUP9dc2_yvi16EsNSAGUyLihGXxEOZoMM3QspCXgUQ0Jic-fS0lVKN1ox1LtqoJTexixfLh73qjbX5liIEbvqjx2fsZNWaKNU7CEJFsL4Em1Z_r4gWQHtWbqTcpTDtmkld8h2AzhcZWH-sFG03snXlMFmDKPVfiyFrx369uP4cVuAJQogHUvxVvQ2F_L0irFM9MzbSxwMHmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود تلاش می‌کنند، رژیم فاسد به هدر دادن مبالغ هنگفتی در خارج از کشور ادامه می‌دهد.
به جای اینکه میلیاردها دلار را به گروه‌های تروریستی خود اختصاص دهد، این رژیم باید آن پول را برای مردم خود هزینه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/144096" target="_blank">📅 17:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف: چپ و راست داریم پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/144095" target="_blank">📅 17:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نتانیاهو و کاتز وزیر جنگ اسرائیل بیانیه دادند: تا زمانی که حماس خلع سلاح نشود و تمام سلاح‌های غزه برچیده نشود، اجازه هیچ بازسازی در غزه را نمی‌دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144094" target="_blank">📅 17:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای وزیر نفت: هنوزم نفت رو صادر میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144093" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
با اعلام اداره محیط زیست مشهد، سگ گردانی در بوستان های این شهر ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144092" target="_blank">📅 16:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVXFveSRSjhLaz_OVOX3SfRzfVZ9COgsGS5QQBVVv2lfjAOrrd-SQwhU7Wb_e9wHB9X5pPQKJRWJ3bj_oO0K59KAsZVaf4-a34o8ZTIi3JA7qcuYJDtYtmYc7bGr-t_nCQb9VbbRKKFkMs7R9HI-yjg_vHisKHMVYFPmtp-g3TqGUhgJWBqKnM57u6j3tt2lfZw6fzeejxaB-OiLy7f7YW9YujEfqcVg5nXwN0M6jkiJX7IOspzUu-lBtSvHHmt54P6QK4NxlEnH1BcoNcjXEUnXyThsQ6bcqbVPv-a3hpPQT2AjV2pBDgsnA8lioDFvM2x9gneseEuzTQtuXKdQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داده‌های کپلر نشان می‌دهد که چین در سال ۲۰۲۶ روزانه حدود ۱.۲ میلیون بشکه نفت ایرانی دریافت کرده است که اندکی کمتر از سال گذشته است. شرکت‌های دولتی به دلیل ارتباطات بانکی با غرب از خرید آن خودداری کردند، اما پالایشگاه‌های خصوصی «چای‌ساز» نفت خام تخفیف‌دار را برای سوخت داخلی خریداری کردند. این پالایشگاه‌های کوچک‌تر برای واشنگتن تحت فشار قرار دادن دشوار است، زیرا آن‌ها با یوان یا ارز دیجیتال معامله می‌کنند و وابستگی محدودی به سیستم‌های مالی بین‌المللی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144091" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144090">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd5eb8afce.mp4?token=c1aJJuQtJnqW5kTuEUmbbTXmMxJXW2KhgcxRVFmFZ6kf4y0Ez0VqT2WGu8oocPFxj8oKLeRWqjGkYMAED-cyL5WbpAunhpgftyc0SaOTZbmn6H1CpPQ9L4r9X49f1-7MAHKjkF73pwtwYGdGYoSsbGUmt5kTknzHYoBmwYjHX0FiKA7FJkkiQ4rjcoq-C-fqbzBBAa1HEojA3-oCbA8qODFp9OzI7A9eq_P0umcfDwVDY9t_k3j4jQsTFhpJwcRwSxVk43TlQxy52txC08WeCa5lSoWrvggshFXqwzO37fBHFB0ciTWjQKxQv-fjxtf_In11tzv1js3anIqp_mttxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd5eb8afce.mp4?token=c1aJJuQtJnqW5kTuEUmbbTXmMxJXW2KhgcxRVFmFZ6kf4y0Ez0VqT2WGu8oocPFxj8oKLeRWqjGkYMAED-cyL5WbpAunhpgftyc0SaOTZbmn6H1CpPQ9L4r9X49f1-7MAHKjkF73pwtwYGdGYoSsbGUmt5kTknzHYoBmwYjHX0FiKA7FJkkiQ4rjcoq-C-fqbzBBAa1HEojA3-oCbA8qODFp9OzI7A9eq_P0umcfDwVDY9t_k3j4jQsTFhpJwcRwSxVk43TlQxy52txC08WeCa5lSoWrvggshFXqwzO37fBHFB0ciTWjQKxQv-fjxtf_In11tzv1js3anIqp_mttxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند عقب افتاده توی روضه بچه رو آورده پای منبر و اتقدر فشارش میده تا گریه کنه و بعدم میگه داره روضه میخونه
#جهل
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144090" target="_blank">📅 16:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQWULDiaJuXJqYgCzlGwI72xbxrYqSjrV_WdT78Xf-pMN5LWI97Jq4OBGc0gTVPgSa0wkOw3_LNovnDjADFoc96YgiMGgOfXZXxf9k5zDbIRn2VMOhp1J2k-HkAg4nUpJuRrwo4HG-QVshqPfda1vC2kL6Y24_-o87nrt-yql529I89l9O0LoPwll-bH6ZnvO6Q8cY_NlCBXg_BfFiQoo5XrgInPUoVsgn4ZbGdmknCactt4H1PCkBMMTtMtI-cJlYPAhoUHFEbN9pGURc9GGDGiO8VGlVvHHZ9mwpKBTKGxQmZ1SwMU2Tj7eUQ-1pezCII4f3aw16cjsg0dM5itkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک توپخانه اسرائیل به جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144089" target="_blank">📅 16:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144088" target="_blank">📅 16:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=vULkTj_sX8gS7qfQorw6zNP0cvwD2GXWwL6xBnvmoxMtUJHjeOi8UYWm_mo9bDNNGNPfV7Wh4nMUSy8IiHepukplcAQQlu-MIrZzZZloQpjOGC-8468A3dRY9N1N4iJGx7S2Yf7VNctaTK858jHeFUZpAaJ__jAtU3TUXK7vIaFjFkvbkaoMFcTf-2E3ouLuSksv9jdvSfBKa8aKEIroD5lMEEYpW6pZoR3KF-Thvr-LEZLfwEQModL0k9X1RcM7qqyajqsdMMsy9AaaMpofkEK23jX7BuHjuIItb4OYu4Cs6iWarE15a0A-O4LsEGGbnn2sDAKLwhFU2LsbuWSFiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=vULkTj_sX8gS7qfQorw6zNP0cvwD2GXWwL6xBnvmoxMtUJHjeOi8UYWm_mo9bDNNGNPfV7Wh4nMUSy8IiHepukplcAQQlu-MIrZzZZloQpjOGC-8468A3dRY9N1N4iJGx7S2Yf7VNctaTK858jHeFUZpAaJ__jAtU3TUXK7vIaFjFkvbkaoMFcTf-2E3ouLuSksv9jdvSfBKa8aKEIroD5lMEEYpW6pZoR3KF-Thvr-LEZLfwEQModL0k9X1RcM7qqyajqsdMMsy9AaaMpofkEK23jX7BuHjuIItb4OYu4Cs6iWarE15a0A-O4LsEGGbnn2sDAKLwhFU2LsbuWSFiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لویت، سخنگوی کاخ سفید:
در حال حاضر، هیچ مذاکره‌ای با ایران در جریان نیست.
🔴
این وضعیت تا زمانی ادامه خواهد داشت که آقای ترامپ احساس کند که شاید آنها به شکلی جدی و سازنده وارد مذاکرات شوند.
🔴
ما هنوز شاهد چنین اتفاقی نبوده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144087" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حمله موشکی نیروهای حوثی های یمن به مواضع عربستان سعودی در منطقه المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144086" target="_blank">📅 16:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9hFzzum6i-ypuuabUmg-OMn9tUU0vP6-ooynJ7F0mb8lLjH5LbEU2LfS_pRvHR1HEDWpcYwIp-RhfNjIVPCYzhSRJffEQuTKSv_ObMscz0jmtA7-cjMdnUypklHCiVUlNmU4LUWDZ50DUMCZOIVpR3HG93cR3ehRh1jSVkJu5t6G-4NptS7SgwNgMWnHS4JaxlR3xbW9DMoQ9e_O1VgMVbCNZBtqJcBPsqeLtd9M9MKMNUlvC8V_R8psKvfDJZXAqdfpceUcaE4XXEsw8mOLnhY92hBVNCmsWwWPEYOnadiO8ZJDjPFeeYeyXgB54zDP4P1JD1igdbCilg04db2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJiSz_RZ3TN9ncLvjvxAuAYjkckT1TWNZzxcENEoDaKflxf_0UPzy3d7TTZ1oZBUgRbEOZwVJtdIn9T48IyOuTfVyZ6pbnNmjPYYyEBYIm3F6cLyY54bluyNUcHvgf78vaPwVRo99f2JbrqaybdatI0qT1dARWhywJwQbNObsmzl5pFjS069_-LA4BIcADv66Rg1W1Ro60OhmYFADFnd7M3YIrQDZ50q5-2EJpdlpR78YhjWC0TU8SKGnMXKhVc353V3s1-tln-gaK7IDi2YIyZlmVWW23RthrXfBSJNLAMxdUm5Bt-Y7v3Bjwj-dpRR4q83mjMgY9NzqUyxdDAjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbCecDIiiLdbB8RHH9m3PoWOYSeeC63LMrtLmTz4ETLKeaXzgWCufhpOWX0-8eIkNXNt4pTqqk6Fa2sRtx6bboBtKry_yPZZBdLE8NZ_6BBA0cxm0S17_RaPLrk66nODisWkb3BKfNpfy71_R1ULTu_AN8wJxYpZgJ2gaCfpBvclNVN2iesCnEOdyq-ua-r-b8-tULcHCk08BLdvfA2fprbLUIivkd9X_Pp-ByxQequCk6a4iyYicX9z3k764996hp_57jra2hIZcQmu7dZR_4C6cVdC7-tLF9y2pjynwoP2RR75X-D0WEL2c_hlinja__Sj1iJ1txxOPP8-JlDT8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر نبطیه لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144083" target="_blank">📅 15:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دقایقی پیش حملات هوایی شدید جنگنده های اسرائیلی ، نبطیه در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144082" target="_blank">📅 15:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شهرداری مشهد ممنوعیت سگ‌گردانی در بوستان‌های ۱۳گانه شهر را ابلاغ کرد و تاکنون بیش از ۲۰۰ تابلوی اطلاع‌رسانی نصب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144081" target="_blank">📅 15:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa8eb8b15.mp4?token=TlcbVF7InOyoDvuuc0QlKGF2Tw6nsSJcrkEqKgvy_SQaBGJGw_69OamzrGGt1Kpb5uWDJJha2eQlFkrren7a4eVrSGeRtFPzqK3CVi7t_u3l1hPioQJE33f_PUz1NgfVhD7qAX7tWq_VmSYu8qX2zR98fThoaLzwyQSDLp1kF2KnOJCdFAyqjA2TYnG9OrcNq74IQBw09uwEZJ_nlgJG6a6j66irKrbmCW52CeGOwoqiHwVQOYp17VWtMojUoCKI_vkuFp6dPrdv52kcLrUajvInnDqyskpBi1_3nTJISqAHLWGEZl2s0ERV1NDX3eSbYWOualPgMGLfj_DaoQpTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa8eb8b15.mp4?token=TlcbVF7InOyoDvuuc0QlKGF2Tw6nsSJcrkEqKgvy_SQaBGJGw_69OamzrGGt1Kpb5uWDJJha2eQlFkrren7a4eVrSGeRtFPzqK3CVi7t_u3l1hPioQJE33f_PUz1NgfVhD7qAX7tWq_VmSYu8qX2zR98fThoaLzwyQSDLp1kF2KnOJCdFAyqjA2TYnG9OrcNq74IQBw09uwEZJ_nlgJG6a6j66irKrbmCW52CeGOwoqiHwVQOYp17VWtMojUoCKI_vkuFp6dPrdv52kcLrUajvInnDqyskpBi1_3nTJISqAHLWGEZl2s0ERV1NDX3eSbYWOualPgMGLfj_DaoQpTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان شدید در مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144079" target="_blank">📅 15:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، ایران در شرایط تشدید فشارهای اقتصادی آمریکا از طرحی مشترک با عمان برای ازسرگیری عبور کشتی‌ها از تنگه هرمز خبر داده است.
🔴
تهران اعلام کرده اکنون گام بعدی به تصمیم دونالد ترامپ، رئیس‌جمهور آمریکا، بستگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144078" target="_blank">📅 15:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آخوند طائب: اگر اقتصاد ایران را به‌هم بریزند، اقتصاد جهان رو به هم میریزیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/144077" target="_blank">📅 15:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e83a74d6.mp4?token=u2HcEyIkLCu9vQc6w1KWFOCVJfa0ByCoFf7AkEHftKVvem3RquRHJoZSQ6wy8mv6grmptlz-5SWFBEVmi4wee-z5Y_r5ejqAz0h1BDfUwZkaksCYsQ8Fg1AgHLrAkULk_t8JUpOYgQDNLh7kMsoV5bERwyVnozRyD7Rl4ZuaJNQIV4uOJNdqm5-wWadRbXhKfU_hWIrV8A6T8ip3KB4bcqpl7OP-28QlIzfAKF8jT3-eVe_DGzWj3CX3kq2np2_dzafhBiTQu_uwxNGUzYf0qrScMkUAR-3OJulXt3R59HNR2OJsD1im0LYrQ-mjIztd80_4f3DnBm4gq_6J2xT1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e83a74d6.mp4?token=u2HcEyIkLCu9vQc6w1KWFOCVJfa0ByCoFf7AkEHftKVvem3RquRHJoZSQ6wy8mv6grmptlz-5SWFBEVmi4wee-z5Y_r5ejqAz0h1BDfUwZkaksCYsQ8Fg1AgHLrAkULk_t8JUpOYgQDNLh7kMsoV5bERwyVnozRyD7Rl4ZuaJNQIV4uOJNdqm5-wWadRbXhKfU_hWIrV8A6T8ip3KB4bcqpl7OP-28QlIzfAKF8jT3-eVe_DGzWj3CX3kq2np2_dzafhBiTQu_uwxNGUzYf0qrScMkUAR-3OJulXt3R59HNR2OJsD1im0LYrQ-mjIztd80_4f3DnBm4gq_6J2xT1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم حمله هوایی اسرائیل به شهر عرب سلیم در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144076" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ ایران در حال نزدیک شدن به بن‌بستی شبیه به جنگ اوکراین است
🔴
در ۶ ماه نخست جنگ اوکراین، بسیاری می‌گفتند درگیری خیلی زود متوقف خواهد شد، چون برای اروپا ناکارآمد است که از روسیه انرژی دریافت نکند، اما مشخصاً اشتباه ارزیابی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144075" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
روسیه از تصرف شهرک شوچنکوفسکویه خبر داد
🔴
وزارت دفاع روسیه اعلام کرد، شهرک شوچنکوفسکویه در منطقه زاپروژیا توسط نیروهای مسلح روسیه آزاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144074" target="_blank">📅 15:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144073">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohqJGuJMQPLw104CS-vR5-QH9hcFPhUtz1eNmBuXWiUuwXd9c1g9FMtA5dcWH_s4Q8QRDqkZy6ppaWMMuOwpVZkkzMJpFgY22YUZx8RXYSoyfGhwScmnhzWv7weYnZopV5-OrFTkmM2hEZXwUfym2bsGH-mQwClbG_9l-FmGAyx5S3R0c2155wkibAXUATnd0XCasEP5VersoUkwsbDC6-mkQVqiopXHCr4g-BeS_lYjhSErfVHnrC_ddE58Ua988IDzFNby_i_S6enhpnLmhbtsTMJnjlASU5LSfa_AfqnP66BCwsV9vwtfwFYR0bbNDN-xhcZC3GpqS_zq8oWL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144073" target="_blank">📅 15:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144072">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع ترکیه از اسرائیل خواسته فوراً به حملات علیه خاک سوریه پایان دهد.
🔴
آنکارا همزمان تأکید کرده حمایت‌های نظامی خود از ارتش سوریه را ادامه خواهد داد.
🔴
این موضع، نشانه دیگری از افزایش تنش میان ترکیه و اسرائیل بر سر تحولات سوریه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144072" target="_blank">📅 15:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر علوم: دانشگاه‌ها از آغاز مهرماه به صورت حضوری شروع میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144071" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش اسرائیل: حزب‌الله دوباره دیشب با دو پهپاد نیروهای ما را در منطقه تپه الطاهر در جنوب لبنان هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144070" target="_blank">📅 14:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نخست‌وزیر عراق: آمریکا برای خارج کردن نیروهای ائتلاف بین‌المللی تحت رهبری خود از عراق، نهایتاً تا ۳۰ سپتامبر مهلت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144069" target="_blank">📅 14:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز : یک سیستم دفاع هوایی متعلق به نیروهای یونانی مستقر در عربستان سعودی، تعدادی از پهپادهایی که توسط حوثی‌ها به سمت شهر جده (ینبع) پرتاب شده بودند را امروز هدف قرار داد. این سومین باری است که نیروهای یونانی از سامانه‌های دفاعی خود در عربستان سعودی از زمان آغاز جنگ با ایران استفاده می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144068" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lei1GjB3kgOFLqmNRvnOJTnqIN-EQlQkNF6XRdXXp1dDQoTfBKOV8wU8Qz2yU10LNvP2FLMbXG2aCHQnY7Bk6EEjblsy8QctkmKoL7xEPDGyMgqoi5dH8JHL8QEFJoeB5178-u5JFIVtTb5jeLUB9gmzLz22Y10srPccPp8I2o6kMck6vzYj6FIuM0ysd10I0mJTLwF_lWAsDw612BSxis8bjXr8FotuuCwMCphUsfbWpP1Uea-8i4t0N1AGJ2ZTdWz6viX9C29x5VStoxRSyfSkBDGmlbPUVaIJPFiUnEyrYLA1pH5pPsnAk0mcHtJN2P4Gu4PF-KCcVRHoO5Ljdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تانکر در تنگه هرمز مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144067" target="_blank">📅 14:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPlv3XOztEorAGdJ1YCNrBZuRj3Mtg_PccBxLMwWSAlmwolidy3Bldj-iabUQmXgu8hSOEWFd1GoZ6yBj1mpJ4x1PHC3fm52qTAPNERca85qlmxR2WS6VpFIN9_oQLOiQqzq1yr6QAfW9j2mFxV40AVtxGKQ3ctPUM_hhkV1iXHlbICxwqRukj_7IrqZ3tcxWvrR8At8IIhLHrbNcZt-PYAT5zRP4YLnmzrTzL8EflF1yaEDjvy5EQXL2r_JuapLdEvczs4uFy3e9yGvlo_nR28guNjFUaxG3z30JGxK1KUZlsKiO9Ejoodof4SRfHSb50N5QUNhpb5TdphjY9wtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش
The Hill
، پیت هگست، وزیر جنگ آمریکا، شان پارنل، سخنگوی ارشد خود، را به‌عنوان گزینه‌ای احتمالی برای جانشینی دن دریسکول، وزیر ارتش، در نظر گرفته است؛ گفته می‌شود دریسکول قصد دارد طی ماه‌های آینده پنتاگون را ترک کند.
پارنل که یکی از مشاوران ارشد هگست نیز هست، به‌طور خصوصی علاقه خود را به این سمت ابراز کرده و در فهرست گزینه‌های هگست قرار دارد.
گفته می‌شود دریسکول پس از ماه‌ها کشمکش بر سر نفوذ و قدرت با هگست، در حال بررسی ترک سمت خود در حوالی پایان سال است.
همچنین گفته می‌شود او آماده است حوالی
روز کارگر (Labor Day)
استعفا دهد، هرچند کاخ سفید می‌خواهد او دست‌کم تا پس از انتخابات میان‌دوره‌ای نوامبر در سمت خود باقی بماند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144066" target="_blank">📅 14:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسکوت شکنان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbsJNEP_JPUBU2QPci05X4JkLThf1SZ5cHU_eQPMyXzcQkrc2P2NOqblLixMGvSL1iOpHXQVMYs2IevNlEmjgZYKhBj4zxebO6su9OtfuTqUUzzvt_727ubgfhqQxAJ3dt_fysprN-Q6EO0wBI9rDlYVYCXdkqo7lHwbkCNL00L9Ga_XsDb5U5ZmZqQlMVRGwVvVdL0Uf8l-PzwlnQCzxONLdBnFppPrr-VWOtfEBQTO9jMbBi901UvZqNnBIYvC9fffjVViDnAcQjMWS5LfZY_eaqAY4dox5eW72b_B92EXxj33kYN5pHzrb6hwum9vCmtjC4Dmtu_0dO5q38tePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با داشتن ذخایر بزرگ نفت و گاز، حالا برای مدیریت بحران به سراغ مردم رفته است. مسئولان با راه‌اندازی یک کارزار پرهزینه در تلگرام، از مردم خواسته‌اند در مصرف منابع صرفه‌جویی کنند؛ در حالی که این سؤال مطرح است که چرا کشوری با این حجم از منابع، برای عبور از بحران به صرفه‌جویی مردم نیاز دارد؟</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144065" target="_blank">📅 14:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afCwQEBgV8YUxJACgs255ePHnSCdtdCNW0ZKiExvBfcPSH22PGMYCEIodjM51xFtfgdRdFPDLI5T089UpSQs0eQ6s_2-4f1jMVq7uQm1JqvZry9J5dkEEEJbVK9tosyfERxvPcX0ML1bgHjjfh79JEwzXpyyCVC9GdNy1yXeTh-l-nluungd8hvjgEeBx4jOKy5rmbsOpLtoI-2YryzyvYzW3e_VDE12tvqln7xUa1J0e7CAk3fI8JnWINY7PgvBD-UGSTyP_v17D539qHFNg5ETQfQrAyo0pQU7vXHEoWo_rX0XotqmjHJ2c5lijLhKJ76P5zjJUoqdf0SpDF2-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود نخست‌وزیر قطر به تهران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144064" target="_blank">📅 14:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رئیس پلیس‌راه اصفهان: مأموران پلیس‌راه جرقویه-ابرکوه حین ظارت بر تردد خودروها، یک دستگاه نیسان را که توسط دختری ۱۱ ساله هدایت می‌شد، متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144063" target="_blank">📅 14:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر بهداشت: قیمت دارو افزایش پیدا کرده، زیرا در حمل و نقل مشکل ایجاد شده؛ مواد اولیه‌ای که با کشتی به کشور می‌آوردیم را الان به اجبار با هواپیما می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144062" target="_blank">📅 14:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144060">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c886e053.mp4?token=nW4-8ORqDGDSTaimqfOHDfVWjBrXyAfN_HGfr49QUUAxP4xOn_5ADie3CRXEsaEotLKlsLN-_LVTm0LQUEAJo1XpIh44oSikeW0RXH9jSc0ZeEr2_BHj_xb7pD5ASruXd8FmDy4U6hDPZJ3KRG7BbIDbGt8QCjzppVTL6sgsEArQChrBr_CN0jNDBzDUHf5N_1l4D6VGm3yjsjp8jalN8Pl2DIWO3Y2DHFqj4ruFSgrhS8uD8T0KWZu9mVHaht5xg6Nn_0hsEsGriEQbVSxctXjonJPmXKikgUWbFRZoo1aFLIHfQS3kPoc9R74GyiPaRF7nN-KrHYkD_cdIdIpHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c886e053.mp4?token=nW4-8ORqDGDSTaimqfOHDfVWjBrXyAfN_HGfr49QUUAxP4xOn_5ADie3CRXEsaEotLKlsLN-_LVTm0LQUEAJo1XpIh44oSikeW0RXH9jSc0ZeEr2_BHj_xb7pD5ASruXd8FmDy4U6hDPZJ3KRG7BbIDbGt8QCjzppVTL6sgsEArQChrBr_CN0jNDBzDUHf5N_1l4D6VGm3yjsjp8jalN8Pl2DIWO3Y2DHFqj4ruFSgrhS8uD8T0KWZu9mVHaht5xg6Nn_0hsEsGriEQbVSxctXjonJPmXKikgUWbFRZoo1aFLIHfQS3kPoc9R74GyiPaRF7nN-KrHYkD_cdIdIpHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز در یکی از پمپ بنزین های رفسنجان بجای بنزین، آب عرضه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144060" target="_blank">📅 13:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144059">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روزنامه نیویورک‌تایمز: به نظر می‌رسد عربستان سعودی در حال آماده شدن برای جنگ جدیدی با یمن است
🔴
هفته‌ها حمله نیروهای یمنی به اهداف سعودی، پادشاهی و یمن را در آستانه یک درگیری تمام عیار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144059" target="_blank">📅 13:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144058">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8246fbbac1.mp4?token=teL1vtdiD7hJD-b7fsLueAvMARQ-vbpowdfXVi92PoQn-4MRyAmnUlUTxp_aBbtWQMjrcFkOjes9JLisUZivZ0Cb7FCGUbhPOUGmPfiAHEFUdownDjgjq_VhWg89hu8uNmg-vvXTk4Oh3NVXhaUIOjL78z8DcI6KSkQ3BDpOV6sPAzdnbvVmyT0ty5uBNquXnmVnBBOAHjJiB85MO1hjeodEKjlzyaeWD24BmG_TPHg6tlUOQORozM8WU80eeYpFMYlVDS5G8y5pdsq-QF5QBqWxmzgZSYF8tQIssDShK3jEIpfthpJJdI1dapUT0DtF18jpZ8F9sYFmKSkNnEmdiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8246fbbac1.mp4?token=teL1vtdiD7hJD-b7fsLueAvMARQ-vbpowdfXVi92PoQn-4MRyAmnUlUTxp_aBbtWQMjrcFkOjes9JLisUZivZ0Cb7FCGUbhPOUGmPfiAHEFUdownDjgjq_VhWg89hu8uNmg-vvXTk4Oh3NVXhaUIOjL78z8DcI6KSkQ3BDpOV6sPAzdnbvVmyT0ty5uBNquXnmVnBBOAHjJiB85MO1hjeodEKjlzyaeWD24BmG_TPHg6tlUOQORozM8WU80eeYpFMYlVDS5G8y5pdsq-QF5QBqWxmzgZSYF8tQIssDShK3jEIpfthpJJdI1dapUT0DtF18jpZ8F9sYFmKSkNnEmdiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد الشرع، در یک رستوران در دمشق، هزینه‌ را با کارت بین‌المللی ویزاکارت پرداخت کرد؛ اقدامی نمادین در مسیر بازگشت سوریه به نظام مالی جهانی پس از سال‌ها تحریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144058" target="_blank">📅 13:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144057">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پادشاهی عربستان سعودی و سوریه دو یادداشت تفاهم برای توسعه راه‌آهن و حمل‌ونقل زمینی امضا می‌کنند.
🔴
عربستان سعودی و ترکیه نیز طی ژوئن گذشته یادداشت‌های تفاهمی درباره پروژه اتصال ریلی دو کشور از مسیر اردن و سوریه امضا کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144057" target="_blank">📅 13:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر ارتباطات: در جنگ ۴۰ روزه، ترافیک اینترنت در حال رفتن به سمت منظومه‌های ماهواره‌ای بود
🔴
اگر استفاده از این منظومه‌ها به نقطه غیر قابل بازگشت برسد، بخشی از حکمرانی در حوزه فضای مجازی از دست می‌رود
🔴
بر همین اساس، «بستن پرونده فیلترینگ» یکی از الزامات ارتقای حکمرانی در این فضا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144056" target="_blank">📅 13:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144055">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قالیباف: اختلاف و فرسایش توان داخلی، دقیقاً همان چیزی است که دشمن می‌خواهد/ حمایت از دولت به معنای چشم‌پوشی از ضعف‌ها نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144055" target="_blank">📅 13:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
میشل ایسا، سفیر ایالات متحده: حزب‌الله نمی‌خواهد با دولت لبنان، ایالات متحده یا اسرائیل صحبت کند و دستورات خود را فقط از ایران می‌گیرد. ما می‌خواهیم سلاح‌های خود را تحویل دهد و چیز دیگری از آن نمی‌خواهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144054" target="_blank">📅 13:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeNhWalcXg9_pTaoWfjREs8HpJoKnoZo7_TTT-l9u8GpIotggpOvp2mRWT7yMj3PKfLq1jt-RUUek8zLKzcUViCgBBkf9QYfe9QwfPihlzSXbNFxdoQrh8pbk_W8VznTd4O4K7ZdWmQmc-TmRU7a-CNghUleU4OqDa4fAYk6K27Pa3UGEY3Mg2PU7rzk5eUPzWzpNKMNuaWtvfzfPu5bvxWszkaEmkEKuT3f64KHswSc9Vqii2XWKbj0uTrVGE5lme1ga4QPHMsbahveHgAL7XcITC4U1rmVkp8jyhJEdQ-ws6zXzQuWUa30jOW0Uruqb_ShgdKx9v_M3ObyviI-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشورهای اتحادیه اروپا (سوئد، هلند، اسپانیا و لهستان) از بروکسل خواسته‌اند تا طرح‌ها برای استفاده از ۲۰۰ میلیارد یورو دارایی‌های منجمد بانک مرکزی روسیه جهت تأمین مالی اوکراین را احیا کنند، در حالی که نگرانی‌هایی از بحران مالی وجود دارد (FT). تلاش‌های قبلی در زمستان گذشته زمانی شکست خورد که بلژیک این ابتکار را مسدود کرد. اکنون یک ائتلاف در حال تدوین نامه‌ای به کمیسیون اروپا برای از سرگیری کارها و یافتن راه‌حل‌های قانونی/فنی برای اعتراضات بلژیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144053" target="_blank">📅 13:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144052">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روسیه: نیروهای خارجی در اوکراین هدف مشروع خواهند بود
🔴
وزارت خارجه روسیه اعلام کرده فرانسه، آلمان و بریتانیا با ادامه حمایت‌های خود، به طولانی‌شدن جنگ اوکراین دامن می‌زنند.
🔴
مسکو هشدار داده هر نیروی خارجی که در اوکراین مانع عملیات نظامی روسیه شود، «هدف مشروع» نیروهای این کشور خواهد بود.
🔴
روسیه همچنین طرح اعزام نیروی چندملیتی از سوی کشورهای ناتو را گامی به‌سوی دخالت مستقیم‌تر این ائتلاف در جنگ دانسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144052" target="_blank">📅 12:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144051">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اظهارات هزینه ساز موسی احمدی، رئیس کمیسیون انرژی مجلس: اگر تمام کشتی‌های آمریکایی هم در خلیج فارس مستقر شوند، مسیر صادرات نفت ایران متوقف نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144051" target="_blank">📅 12:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144050">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳ ریشتر در بهشهر ثبت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144050" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک‌تایمز: عامل سیل مرگبار در نپال، ممکن است جدا شدن یک بهمن یخی از یک یخچال طبیعی باشد
🔴
احتمالاً توده‌ای از یخ با عرض حدود ۶۱۰ متر به طور ناگهانی از یخچالی طبیعی جدا شده و ترکیبی از یخ و آب را به کف دره فرستاده که انرژی بالقوه عظیمی داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144049" target="_blank">📅 12:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش از شلیک توپخانه اسرائیل در المنصوری، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144048" target="_blank">📅 12:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ3TEXhvCNuJb6VJFE_0leBPswo9ObsYXKmGqJprDJKWCXLqQ_ejEaNvopQSNEVaJVUFUV16Fg8nktOMOPV6xMLTq-kGmYCIKOijm8TD8TKgFxZlLhSUxH3vdcpdkp03RbQu-1sTFq-HhWM7NPDqprKPnM6ADvAef1awI-sRs0eA53bU1e557VWy00hzuPbBxXOQXHwdeGEGJUChJFc1vWySIKWG2YrxSNWhk64c9v0xZi-olxWQQn_WIjzxGE6dyLKujqwPTq1f0n1Z3jvmfsiV7Cyo7fuwXcVLXJerSfyOBuLtt-vwjRF1oQ406Vv0NJsB0iXq0gVpy2gpe5AZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از شلیک توپخانه اسرائیلی در این منطقه صبح امروز، آتشی در محدوده بین شهرهای کونین و ایناتا شعله‌ور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144047" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: این گمانه‌زنی که عاصم منیر به عنوان فرستاده ترامپ به تهران سفر کرده، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144046" target="_blank">📅 12:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLo60BOk-VwfCtJCo8Lw5lin-duJJ0Oj0fYHV8zAPO3TtS9Jxs1Q0lNeP8eJ-2grONXagMWKwC5eKvMXtQkcIZBZ2NcJvoFWUMnn_OQzZRMz8HZunH_4BSfZ6yrDMZFuQoSi2_xzktpdMob98Y4TKatTIwd-AKiCTnM19TOWg8DsY6U6lZjUyWdDSO-E5eb2byz7vWpFOkjHDO1t3tLTaXB7j6CYpMNng2j_A6nAWfiHEFV8mfJKS3zsyqxfGojNn8GAW7rT6dVUJq4dr9-k5yEtOwILaQ99Jx5GcnoynHkOp0kIuIuaUvEsQxd-geQp0oRv-eJ2dqtf2Q0naJcFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkFeoOwna9L66vWOhTkVxRtXDDwO_VrTnUmyXCii3OB0H460xjeLHvtjwGq4PNDbyf_38tuXsW2dekWfRxcUwMa4yBxA6Dj5OqzTvYv-qBObwm2w0wi9AxlCeKMV9kSA0q_qdaAIq0K7kIG4OB1Xrxv90AjrZaGXLVAB4PNyT7DJdvP25V3F58G85ekYWpnxiSr8SSN_9yXjjhLrkbEVbI2bzmOXRWm0dHYK_JEUYhzwKH2aTgT94uGyLAaZMxaheTnkt-jkFrF9mKvNmmzdD7xNKs_eWaHGkS3Xg50CRqdVc_G-72x_vUMFjTmOIfQd5CE6T71TpdHRenz50GgdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5XyKsShI-xkZ-o83ckkNOxKjYT0Rg_a36G0xIT87sGLuznomtXKqpuptCqxZr95q_mblBS1lXQKmJQ8ekpGFBLfpUewWk0tr_aopXykWjccy9rKFFqR8YwEH6IUgulA4HIpjqEU4jgNRILy8jkqXLOCn_MlIkB5d2lhtVKudR-qwh7lXDQ28qRDeUSMd3qVCm118adalsko6vukPNd32SYIFFoSLrk9RoHbwRPd7NUJmnBpa9PPyIOu_eV_NyzxgKIrH7yFMUhg6u4FqrTNivFkJJyu_IQMGzvck9zKoIpyWMg2uWkVJeIcSLiSawn_5xI9KrLEFqUcDgsfxG7jCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاويرى از توقف كشتى ها در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144043" target="_blank">📅 12:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
به گزارش MS NOW، ملوانی که ظاهراً در یک اقدام به خودکشی از ناو هواپیمابر آبراهام لینکلن به بیرون پریده بود، اکنون به دلیل «تمارض» و غیبت بدون مرخصی با اقدامات انضباطی نیروی دریایی مواجه است.
🔴
همسرش می‌گوید که مرخصی زایمان به او داده نشده، پس از این حادثه مراقبت‌های سلامت روان کمی دریافت کرده و قبل از اولین جلسه درمانی‌اش به او دستور بازگشت به کار داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144042" target="_blank">📅 12:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTju3ywEy2qPrNdV1lSEgIOzYNdCNRV0LkEHA2Q--kBmQv69n2SL7wOpdl9YcwEJFcw-W02VdkHmNPIXmla-ZWtdT6m4n0i6r-rIHGgiEtfMgW2PE9YRWYvUBPnvdZ0d_bGqFSHVqzSKGbK26AB75A01lk7vf5WBaKuyzG0nXiRrYBI9kxrLBWn2zSSxjTLmjPw_CoWMTrxwHus9BRhc6ZiGWyuS1Bya0z1EL-GzSxnCebZeAnT3TB9EvCrJCSiRdBzrAdeAYGOcAo9U6q1XqfTeF2pbXIZDQRUXh0JviWN97M9RBOmZz-azaDHrNgBFW3exdYCTTps4M-PMF_s4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: باید تو دادگاه هرچه زودتر حکم قصاص ترامپ و نتانیاهو رو صادر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144041" target="_blank">📅 12:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9368fe922.mp4?token=tS7alSCAlGgPzcdH71QaJYcYGt3NlOmyc9nUB6k4ytcjMBM9_Gwzg1IQk9A0aY2wQZD8OeZzZa8GDe_7uY-mvqpzlSqmd9tktxqOReOiUMKg6G76uPsq58juEbQyFIGvMz-NPmtyKBUJ6Snbd8DnHdnFTU1haD_qHVzpKSMeZwpRVVjnUlaJant5ULaAKtya7D8UuwkzfuBhVqQGb_WwnoxIgH1uWZI0M-T-6IcUhgF9vtWMaVp_bKxUGxt4-KZnP_-qtqXQXzXq67lHNA7kndLdOKPuSwPApetvuGCENLfKKsapIOKUInDEElfazWT7srcqhjxnqiaSXXLqELVZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9368fe922.mp4?token=tS7alSCAlGgPzcdH71QaJYcYGt3NlOmyc9nUB6k4ytcjMBM9_Gwzg1IQk9A0aY2wQZD8OeZzZa8GDe_7uY-mvqpzlSqmd9tktxqOReOiUMKg6G76uPsq58juEbQyFIGvMz-NPmtyKBUJ6Snbd8DnHdnFTU1haD_qHVzpKSMeZwpRVVjnUlaJant5ULaAKtya7D8UuwkzfuBhVqQGb_WwnoxIgH1uWZI0M-T-6IcUhgF9vtWMaVp_bKxUGxt4-KZnP_-qtqXQXzXq67lHNA7kndLdOKPuSwPApetvuGCENLfKKsapIOKUInDEElfazWT7srcqhjxnqiaSXXLqELVZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل بزرگ دیروز در مرز نپال و تبت دقیقا از این نقطه شروع شد!
🔴
جایی که یخچال های هیمالیا بر اثر زلزله فرو ریختند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144037" target="_blank">📅 12:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46983e76c.mp4?token=SHF-ivbwkwVZ2ShIpWykAwjQfhVp7bcfJNyKalj0SLqKxWAYSNaPXW8SqKSRri5YBBfYO4Pm5mWRPT48OFuSlYg6LLR_Qzwbsmnlho3KPsrzDxjMEIfoxYVPK0BTR39B-v5xWX3z0OPLlREDgum1Zj3vkDcX7ZCS9JfV2MWCtbqMMgt8v2Apo1gyxIGp2SAwSzH_t0kVwKnkI_vucuMySRSlrL_1Cg9hZxhBfjV6IlnclFsMOr_DxcL_tqvpG0af1OmN85nK65YY9OqWmO3PjAQcoQ2gJ2bjuybFlieT5kTXL8w_D9Cv8ifDwVwRFf64LpO-Ob3p55IRIE62Svv8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46983e76c.mp4?token=SHF-ivbwkwVZ2ShIpWykAwjQfhVp7bcfJNyKalj0SLqKxWAYSNaPXW8SqKSRri5YBBfYO4Pm5mWRPT48OFuSlYg6LLR_Qzwbsmnlho3KPsrzDxjMEIfoxYVPK0BTR39B-v5xWX3z0OPLlREDgum1Zj3vkDcX7ZCS9JfV2MWCtbqMMgt8v2Apo1gyxIGp2SAwSzH_t0kVwKnkI_vucuMySRSlrL_1Cg9hZxhBfjV6IlnclFsMOr_DxcL_tqvpG0af1OmN85nK65YY9OqWmO3PjAQcoQ2gJ2bjuybFlieT5kTXL8w_D9Cv8ifDwVwRFf64LpO-Ob3p55IRIE62Svv8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست، وزیر جنگ ایالات متحده، درباره اسکات بسنت، وزیر خزانه‌داری: «ما در هماهنگی کامل و تمام‌عیار با او در مورد خشم اقتصادی و تمام فشارهایی که می‌تواند وارد کند، هستیم و می‌دانیم که ایران نمی‌تواند آن را تحمل کند. در نهایت، اقتصاد آن‌ها در حال سقوط است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/144036" target="_blank">📅 11:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzEM1MoJlN0oPR-1wezC69sO5--dYL1k-M6mp_KC3qmdyjuFqG5k0Ap-wnv7hQ4Fvgj40-Ag6Y__32WKxYEekt0zbfxQ_Vb2jb84E0-f6En0fV7AejKo_TYUeZrTwFPa-eIkXNURqtPeel77qmoQ0TpkpBvETWcpEGP_x2zPXm758SvH62Ow8Vb9uWdwlG9O7gFxmt9khvQtbM2JFj0OoyOxDwiCJY1s8HW7FkNHBAwZgCUFLrbEmZJ1goLRknNXzJM-0H2DGDwjnmitSwlfwrTRmBzJ46uooRyBLDn3wwX43ceJn6Y4VQhjUs5wB5--GS60l0_FXYlFKauKMZ3tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید علی کریمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144035" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
خبر مهم درباره ابر تورم
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144034" target="_blank">📅 11:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
آتلانتیک: ترامپ به متحدان خود گفته پس از بازگشایی تنگه هرمز از جنگ کنار می‌رود/ یکی از مشاوران ترامپ گفت: «ما فقط سعی می‌کنیم تا انتخابات میان‌دوره‌ای دوام بیاوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144033" target="_blank">📅 11:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144032">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیویورک‌تایمز: سیاست فشار اقتصادی آمریکا علیه ایران به نتیجه نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/144032" target="_blank">📅 11:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144031">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a1d00ac4.mp4?token=emevDm0jyRPtE6ohqDg5IVdgkNN0A9UnrxyYFOwcW-2S1vg6Fwm0ye8_J756X-QXAPc4iTbhNudzOgzfsTUYnHBJa59UPOqQ0IDdTVYzjRgchTsji-EKi4vPIILfcW0r9eieTV_T34RNAPxM5dAsVIcooe4Viagsmp6mJmKYZhNgKcxOlde4BA7GXre01KAKINFWWl1zxxIqML0Xw3oAmoVf-O-VbP4NWYeZMscm5MQ4NGyzrOM8Ga5wH6n2uHWQek_3TnkqrzjBeA170YOk4Qzgz8NkwCp1UnU6XvDi_aPxgdeom12PesQMgYPPELHq-FD57Er2Y0biYyzxNl0nJbGy-lzF3D_Op7PJX1pZ1ok9V1zaMx1nFb7N-qKYfsR8-MFHCm3jHa7R7pGuHMEAAj7TZP2BX_LJ7enlGCluB8MHOdZhwslONBGHpJu4f-MhxpVxhorno0biFRBDwQaKRWy1ljXDSbJD9RjrWoMFTrkipBRpF4_2_pfh7tXgC9YvImjI-lGX9kOXD1-P-93UEGiLsgTN0kXqzi94DaSBXutIYmGUDKLsJAtLu1UMsleA4cuklocQuIj5PxL06QGu44HeU5sP18CO1pig1I-yKFP5PzhEmAAzcAQ1_kRoKhT3KFLUzKhCKwTkNTw3I2Aog-jmByoUfTttYpj-Y486Nq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a1d00ac4.mp4?token=emevDm0jyRPtE6ohqDg5IVdgkNN0A9UnrxyYFOwcW-2S1vg6Fwm0ye8_J756X-QXAPc4iTbhNudzOgzfsTUYnHBJa59UPOqQ0IDdTVYzjRgchTsji-EKi4vPIILfcW0r9eieTV_T34RNAPxM5dAsVIcooe4Viagsmp6mJmKYZhNgKcxOlde4BA7GXre01KAKINFWWl1zxxIqML0Xw3oAmoVf-O-VbP4NWYeZMscm5MQ4NGyzrOM8Ga5wH6n2uHWQek_3TnkqrzjBeA170YOk4Qzgz8NkwCp1UnU6XvDi_aPxgdeom12PesQMgYPPELHq-FD57Er2Y0biYyzxNl0nJbGy-lzF3D_Op7PJX1pZ1ok9V1zaMx1nFb7N-qKYfsR8-MFHCm3jHa7R7pGuHMEAAj7TZP2BX_LJ7enlGCluB8MHOdZhwslONBGHpJu4f-MhxpVxhorno0biFRBDwQaKRWy1ljXDSbJD9RjrWoMFTrkipBRpF4_2_pfh7tXgC9YvImjI-lGX9kOXD1-P-93UEGiLsgTN0kXqzi94DaSBXutIYmGUDKLsJAtLu1UMsleA4cuklocQuIj5PxL06QGu44HeU5sP18CO1pig1I-yKFP5PzhEmAAzcAQ1_kRoKhT3KFLUzKhCKwTkNTw3I2Aog-jmByoUfTttYpj-Y486Nq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست درباره ذخایر مهمات آمریکا:
چرا باید به این سؤال پاسخ بدهم که آیا انواع خاصی از مهمات را داریم یا نداریم؟
🔴
ممکن است به شما بگویم ۱۱۰ درصد ذخیره داریم یا بگویم فقط یک درصد داریم؛ من هرگز به چنین سؤالی پاسخ نخواهم داد.
🔴
رسانه‌های آمریکایی احمقانه عمل می‌کنند که می‌خواهند وزارت جنگ آمریکا را تحت فشار بگذارند تا درباره وضعیت سامانه‌های پیشرفته و محرمانه‌ای که ممکن است در اختیار داشته باشیم یا نداشته باشیم، توضیح دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144031" target="_blank">📅 11:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144030">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/301fdc8983.mp4?token=U_-8SLtBZXRJZTAQ-qoSp4q_Q5rdt8R9WdFEKQ_MyTrZeHzNozKRrhifKoGeU5REA2wayG-J8AkpwbotgYPM_LcM345fajlajtCnw6tw1t-vtFdObQa8WsjzSOgko3vb3XaPXfXL2ZS92HvZdLNNUgoDfs5mz0Cm2MNGJ6uXXJfgYJ4wFVlvmD1bFUi8ZTJFR2it7UgBGiEyUpmVFTXHBQi2KUD6cd4Wzeg89HIJz34Caay355Vh9D1ROarq30aciP0K5kWFkLMmQVT1CFFHa1W63JKYxF-eZNqJyo-9TmXyPvZ-la8boiYxwIvbEVxOOw7bRR0M_P-0J9AFr-CyDjwA3EasnylfEt41-kA8ulgVANUjUDkNB6imQwAuFI_euq2e9RtQl1gEgp55cmykQwHWkUmyBA8CkSMe_B8NhzZFqv4jfP6QqnfkKNIWK3QhIQfkUzimjEAdLCt5ITiMaMxa0EHnPikurp9vQV-HjA1WdPtH0TOYshFyFqKno5n8wCT9diLUxRJ0MK2icDywqEGz8dxnPigq-ltT1aFxQX1sxbYkQ27JIhyVuJAclY0jgL_ulwoW6iJexdhw6Uw11GRfFB-5wc1-9xyE2o1fEO72ISanqh1FbDGoAUWSahvYGrxelLfcIehe1YfeQYLjDhcPPRE1UAYN5o-f2FYcd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/301fdc8983.mp4?token=U_-8SLtBZXRJZTAQ-qoSp4q_Q5rdt8R9WdFEKQ_MyTrZeHzNozKRrhifKoGeU5REA2wayG-J8AkpwbotgYPM_LcM345fajlajtCnw6tw1t-vtFdObQa8WsjzSOgko3vb3XaPXfXL2ZS92HvZdLNNUgoDfs5mz0Cm2MNGJ6uXXJfgYJ4wFVlvmD1bFUi8ZTJFR2it7UgBGiEyUpmVFTXHBQi2KUD6cd4Wzeg89HIJz34Caay355Vh9D1ROarq30aciP0K5kWFkLMmQVT1CFFHa1W63JKYxF-eZNqJyo-9TmXyPvZ-la8boiYxwIvbEVxOOw7bRR0M_P-0J9AFr-CyDjwA3EasnylfEt41-kA8ulgVANUjUDkNB6imQwAuFI_euq2e9RtQl1gEgp55cmykQwHWkUmyBA8CkSMe_B8NhzZFqv4jfP6QqnfkKNIWK3QhIQfkUzimjEAdLCt5ITiMaMxa0EHnPikurp9vQV-HjA1WdPtH0TOYshFyFqKno5n8wCT9diLUxRJ0MK2icDywqEGz8dxnPigq-ltT1aFxQX1sxbYkQ27JIhyVuJAclY0jgL_ulwoW6iJexdhw6Uw11GRfFB-5wc1-9xyE2o1fEO72ISanqh1FbDGoAUWSahvYGrxelLfcIehe1YfeQYLjDhcPPRE1UAYN5o-f2FYcd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع آمریکا:  ایران می‌داند که ما تنگه هرمز را کنترل می‌کنیم و جریان نفت از این مسیر برقرار است.
🔴
آن‌ها قمار بزرگی روی کنترل تنگه هرمز کردند، اما نتوانستند آن را در اختیار بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/144030" target="_blank">📅 11:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144029">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0928bb66.mp4?token=UBIQPwz761yWFGNrO6MajlLb5kIDaV5rNw8vc7BHtO6KX4B4vK0ytvu3SJ2GlTxN2yWYpI7P0B18cGrtzg_FJJ9C26N4zdfvZf1F0LCQG92f9we7RCtULwGYBDLkBLn11K0gtnIrli6SB5ubZffYs6ZhhJT2ZvLjFhKNkMkjvOf1d3hoWTtk9zfFEqK3AFqg5d1iKMt4UEEhmkk0D3YVEYN8o80mFCtt5-h6fY9gLR-MfDJnt19Br8fQgrostv3tTk4LZzmaX0lwMJWi2D7poflVXsmr9_oH0d1U3pFJlRrHjxW1ZDdh4mZS04f-BBBJ9un8Rtcj5WTjZKRAnsT__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0928bb66.mp4?token=UBIQPwz761yWFGNrO6MajlLb5kIDaV5rNw8vc7BHtO6KX4B4vK0ytvu3SJ2GlTxN2yWYpI7P0B18cGrtzg_FJJ9C26N4zdfvZf1F0LCQG92f9we7RCtULwGYBDLkBLn11K0gtnIrli6SB5ubZffYs6ZhhJT2ZvLjFhKNkMkjvOf1d3hoWTtk9zfFEqK3AFqg5d1iKMt4UEEhmkk0D3YVEYN8o80mFCtt5-h6fY9gLR-MfDJnt19Br8fQgrostv3tTk4LZzmaX0lwMJWi2D7poflVXsmr9_oH0d1U3pFJlRrHjxW1ZDdh4mZS04f-BBBJ9un8Rtcj5WTjZKRAnsT__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست درباره ایران: تنها انتخابی که ایران دارد این است که پای میز مذاکره بیاید و واقعاً درباره برنامه هسته‌ای خود گفت‌وگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/144029" target="_blank">📅 11:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144028">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: همچنان در مرحله «شروط متقابل» میان ایران و آمریکا هستیم
🔴
بستری برای تعامل مستقیم میان طرفین نیاز است تا زمینه را برای یک «مبادله واقعی» فراهم کند
🔴
مسئله به «معامله امتیازات در برابر دستاورد ها» نیاز دارد؛ در غیر این صورت، تجربه‌ های اسلام‌آباد، سوئیس و دوحه ممکن است تکرار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144028" target="_blank">📅 11:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144027">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال : افزایش سریع پهپادهای تهاجمی یک طرفه ارزان قیمت توسط یک زنجیره تامین جهانی پیچیده که همچنان به چین منتهی می‌شود، امکان‌پذیر شد.
🔴
پهپاد شاهد ایرانی با کمک چین جنگ را متحول کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144027" target="_blank">📅 11:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144026">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
معاون حقوقی رئیس‌جمهور: آقای قالیباف قول دادند که مواد دارای ابهام طرح «مقابله با نفوذ» را به کمیسیون برگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144026" target="_blank">📅 11:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144025">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773515bd61.mp4?token=mzJqm6vkJPOVxzA7616ybcDPzNc2o9ffGRU4fAFBsZzAcTOXi3Sl01o7TqkMsIjyUpI15pareWpriw17fM0u0MlfPXrI4mTcyDNBSUHfUyT4XGCgTK0VTg4FEhfyW1qAgMhf3qXGzv6iKmHwU0fVPiuD6DvbOi7qFc4ODx3TQqVN4FYxoWcLX_djVNsnI-LXQdGZ0QXj2LXHnrS1c89xGX-7QhIT6f2IiDqaDu1ISGzKfBMs86piheNLDRSRTh9Wi8Oo4xFmAauWHhuo51f2ElnxNfd7TGVTvZoKL7-DOjyQC8grmeSjByRPfIFfp1ciD2lN44ef3G1GBQC76KZH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773515bd61.mp4?token=mzJqm6vkJPOVxzA7616ybcDPzNc2o9ffGRU4fAFBsZzAcTOXi3Sl01o7TqkMsIjyUpI15pareWpriw17fM0u0MlfPXrI4mTcyDNBSUHfUyT4XGCgTK0VTg4FEhfyW1qAgMhf3qXGzv6iKmHwU0fVPiuD6DvbOi7qFc4ODx3TQqVN4FYxoWcLX_djVNsnI-LXQdGZ0QXj2LXHnrS1c89xGX-7QhIT6f2IiDqaDu1ISGzKfBMs86piheNLDRSRTh9Wi8Oo4xFmAauWHhuo51f2ElnxNfd7TGVTvZoKL7-DOjyQC8grmeSjByRPfIFfp1ciD2lN44ef3G1GBQC76KZH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرفای عجیب مهدی طائب: «حضرت موسی ساخت بی‌سیم را به یهودیان یاد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144025" target="_blank">📅 11:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqzGbAPS_vI8H55llaokOI0C1frBW2mDHFJCDXvMgtq_RSjR2uMa9fgcN4Gm1xYzvNPkte_wuvp8qd9Upyw3BCSp9DQCbyEi7xdHlZLuXK-5SJaTFR-f7RorDn6LUkFJU98EMUSfs6fZc9vRMZK_rkv6t-q1-q1E7GHeMb8PSQHkdY2m0jI383ga10rcPz-FHvN2BRrlJ5S3PSo_7RUWhJdoEcmtcujmzhiBo-MmSHVTxc8eFhB6kJtcFhZWQK8lNI67iRUl9WVKrymlNDKLqR3BUbAhAlt9eTAcMVZL5912noG7Ju1mNsPoy-8f79TNCVw3OUvnoRqnhb3tl17_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروفسور کاوه مدنی، دیشب جایزه آب استکهلم ۲۰۲۶، معتبرترین جایزه جهان برای دستاوردهای برجسته در حوزه آب، را دریافت کرد.
🔴
این جایزه توسط کارل گوستاف شانزدهم،  پادشاه سوئد در مراسم سلطنتی که به عنوان بخشی از هفته جهانی آب در استکهلم برگزار شد، اهدا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144024" target="_blank">📅 11:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144023">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: تماس‌های آژانس با ایران و آمریکا ادامه دارد، اما پرونده هسته‌ای فعلاً در اولویت دوم است
🔴
وی درباره فعالیت هسته‌ای ایران در کوه کلنگ نیز گفت شواهد محکمی برای تأیید آن وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144023" target="_blank">📅 11:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144022">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: قیمت نفت به روند نزولی خود ادامه داد، زیرا انتظارات برای مذاکرات ایران و قطر جهت بازگشایی تنگه هرمز، افزایش یافته
🔴
نفت برنت ۰.۷ درصد کاهش یافت و به ۸۷.۲۴ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144022" target="_blank">📅 10:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144021">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان:
کشورهای اسلامی متعهد شوند به تمامیت سرزمینی یکدیگر احترام بگذارند. از خاک، آسمان و امکانات خود برای تجاوز به کشور اسلامی دیگر استفاده نکنند
.
از تجزیه و بی ثبات‌سازی یکدیگر حمایت نکنند و امنیت خود را علیه یکدیگر تعریف نکنند بلکه با هم امنیت منطقه را مدیریت کنند.
🔴
این به معنای اتحاد نظامی یا یکسان شدن سیاست خارجی کشورها نیست حداقل عقل جمعی است. اگر نتوانیم میان خودمان چنین قاعده‌ای ایجاد کنیم چگونه از نظم عادلانه در جهان صحبت می‌کنیم.
سازمان همکاری اسلامی باید بتواند پیش از تبدیل اختلاف به جنگ وارد عمل شود، نه فقط بعد از کشته شدن هزاران انسان بیانیه صادر کند.
🔴
شیعه، سنی، فارس، کرد، عرب، بلوچ، زن و مرد همه باید احساس کنند که ایران خانه آنهاست و قانون از کرامت آنان به یک اندازه حمایت می‌کند، اگر می‌خواهیم از وحدت جهان اسلام سخن بگوییم باید وحدت را در خانه خود نیز هر روز بازسازی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/144021" target="_blank">📅 10:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144020">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پزشکیان: در حالی که مسیر گفتگو میان ایران و آمریکا برای حل اختلافات هنوز جریان داشت حملات نظامی گسترده آمریکا به اسرائیل علیه ایران آغاز شد
🔴
این حملات در شرایطی صورت گرفت که مذاکرات ایران و آمریکا در همان ماه برای یافتن راه حل دیپلماتیک از سر گرفته شده بود، رهبر کشور ما فرماندهان ما مسئولان ما دانشمندان ما دانشجویان دانش آموزان ما و مردم عادی ما شهید شدند شهرها و زیرساخت‌های ما را هدف قرار دادند
🔴
ما آغازگر جنگ نبودیم ولی با قدرت در مقابل این تجاوز ایستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/144020" target="_blank">📅 10:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144019">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
روزنامه «فایننشال تایمز»: اسرائیل در حال بررسی اخراج نمایندگان انگلیس، آلمان و ایتالیا از مرکز هماهنگی امور غزه در «کریات گات» است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144019" target="_blank">📅 10:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144018">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پزشکیان: دفاع از ایران به معنای دشمنی با ملت‌های مسلمان و همسایه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/144018" target="_blank">📅 10:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144017">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: ما همراه با کشورهای دوست و با جدیت، تلاش‌های میانجی‌گرانه میان ایران و آمریکا را دنبال می‌کنیم.
🔴
فرمانده ارتش پاکستان در چارچوب تلاش‌های میانجی‌گرانه و برای ازسرگیری تلاش‌ها جهت بازگشایی تنگه هرمز به تهران سفر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144017" target="_blank">📅 10:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144016">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: واشنگتن دیپلماسی با ایران را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144016" target="_blank">📅 10:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gt1HxuLtR6HC1DF8Ecmr4zblsa0wJwJGkL4bv8GWt13_F4gRk5BGkDcrRvtvcW2yPeWnSEbuZizRTkq7V9fTPk2NYZbUq0UeUG8Kkob7XbGADAQ_FBtQ3CO9dIpxztbkNdKLI1_bO8OhS3yqTFP3FRsY-ie5vtS2arDElaCHIWUJI4ZcrpuXLHWkwGqsAS7kdOeAROo6DIEySoeOHihDdA39swZN611HTGU_0UFe8dCvpCql0iQP0UDSFrrbwPtFwZgo3OwypZXsdjVYFxJdDuCiSlkvBnksCe24cV6Y4fOM9D6NmdIY7ESiLq9RQZZSHolINlsRrhncW0hnWVk4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2D_wIXAGKWQfuGkk5Wi-8HJCR9g9PYI6W7IT4wS-WoRqNINheA2zKkhpmPRu5Bf8_srSyEWRcQ680s4Uhj1GVAuu6xJCrDzgdUEXyO3bGRBPzT7u_jsbOBFOZdctApbTrFveGWbsIqc0gYLBF1VjUfEPx4gY2RkYRz78nfwdaqScggSN_jmc0UP3rIde2AOzgyQZYbaaU5TkgiaRultPnRj_ZCnfz9MrQC3cLrwl4QvZc0zootzk3KkodbTrMu1zx4e6dtCwqQjqxXGAhqfg-9rWnIe85kNBa835rURhpgPR4cP7VqoM1rJWYkmnYFotiGAeHYV1IRZ5UE3JRtriA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی نفت‌کش «آمارا» متعلق به امارات متحده عربی، پس از ۱۰ روز توقیف، به حرکت خود ادامه داد.
🔴
همچنین، امروز صبح، ۵ فروند کشتی نفت‌کش و حامل گاز مایع از تنگه هرمز عبور کردند، این در حالی است که مسیر آن‌ها توسط ایران تعیین شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144014" target="_blank">📅 10:02 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
