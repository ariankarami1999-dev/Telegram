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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 14:32:08</div>
<hr>

<div class="tg-post" id="msg-125734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULDeH6-J-fQhBnek07gRvaCDZDyeVuF-ryYT9uZ9BgL3YxUyFZ_g6PaJ0ZBZT_BPHIaNO23bcQReknE19WUKINqGSIfhilp7tUnDhZFGFI1ZaiLVMdOxZ-SLTSYU2YtY9xoNzKZ-BGIRZbgrg31Oa36XM_QJrK-cv39Mx9nV21dbO0uResxluW35gntONyW3TpChxFQseiDfr9ibGWX7byIUtJRaZiexvSRfmwp-98IzRtLkGG08Oo627QfIIQRzQfq9ysMzdpn77c5JwQ-PX9oThgxVtob1eR2mgFsznNSVQ1JDfstaNz1tzsTqRy5xbUbUgJQOOu_pAbjXGnBXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVJeAbYagX2ZvxfZeTc-UYsjBaR3-rUz5rS533XmcFXfa63aW0NiClmCd46CnDaW1D8NNnef_ZgDVghaAQPE5OYhtSlDLDJbAylB1VB9aUQnpmA7AvpdLeT92e_AbEC56jEujBLMJ0C3WCgV2b87XdBUftFqbdvg1vqTmV5aMzNPLuj_FcJrz1PyOmRiRlX6v4d3Mv7VB9_cSFrIgxCoWMbTRSCItOyP8GVf7pz4kuOBJbFCIX1DQxbwsIb_qtTlWDy7xglUDnMcBYWQjWeFs53lMELWXA1tUUOUHpm-Vbach7kUUY8avLdjIW94oHtUkVYyRcBshnc628e4hbnxMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فلسطینی با مسلسل کارلو به شهرک نشینان اسرائیلی حمله کرد که دستگیر شد
🔴
در جریان این حمله تاکنون یک اسرائیلی کشته و 6 تن زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/125734" target="_blank">📅 14:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عضو کمیسیون آموزش: اعتراض به مصوبه کنکور فایده‌ای نداره؛ دانش‌آموزا برن درسشونو بخونن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/125733" target="_blank">📅 14:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku195pOJqZ4fb9VG4HE3KHhk7IV66iThaEwUAkol1uOg8ZlYewrVVR1R7Tiz0lpX1dIPSaEIdicBBJ6KJo45087VCA58N7GQEuoWeqDbuG6B-i8Tkut_9H8ytzWh4IP0lphExQXCHrBXpAyU4zome_VUF20CMMahm_vbBZyAL39kZ_CIWVmjIzemdkmyU_0i1YPQiXlLCoFSzmVMTC09pMHLFpmLh_eyO0yhW3okk6gNmB2iXfLqca-hEsaETPtc4eeK_GgkdX5nhH6fL0XSu9_JARm2w6v7SJREOX7EZVQ2x51-mJQGFHPMLPAqiYqteFEG2Vw_lK84bBVj5Mty3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روند نزولی واردات نفت چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125732" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125731">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در گفتگو با سی‌ان‌ان: مشکل اصلی مذاکره با این آمریکا این است که شما باید با مواضع متغیر زیادی روبه‌رو شوید؛ تغییر مداوم خط قرمزها، اظهارات متفاوت و متناقض مقامات مختلف
🔴
وقتی آنها در مورد دارایی های مسدود شده ما صحبت می‌کنند، هیچ امتیازی اعطا نمی‌کنند
🔴
تعداد قابل توجهی از مسائل اختلافی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125731" target="_blank">📅 14:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125730">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / ۲ زلزله پیاپی به قدرت ۲.۶ و ۲.۹ ریشتر  با عمق ۹ و ۷ کیلومتر پردیس را دقایقی پیش لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125730" target="_blank">📅 14:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpFBfpzwZJslH8tqZPcdd6L5AkK6lfQPq2-qRHEPk0WeZaCYeiD47baju1pSiSJvaMdBsecGF3QysJVYo5gGXf5a9fdMYQOH685V3NeGOjou46SZBm_EAIj9NuBXjR9FaRe6vMSVJpsFd1KPw0LZORqfdFU884_2_iWE_g2pFUocel3Lbr_mAt-tItlz-sm9F9dP0M3AVbVp1VNSYk8KynLLKfnVDZU-Iu1REbclRFOUJE2Bx13mzGbgnJ_dSSdMTkkwl-DASXq2jWCAHFqhzTA6qOT-xEGOcM1bfS59O9PiDRMUrVlbhdQSwgejZnEiFk6blPZI5vr3lldekokq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی چین در ماه می بیش از ۱۰ تن طلا خریده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125729" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عضو کمیسیون برنامه و بودجه مجلس :
از کشتی های عبوری از تنگه هرمز ۱۰۵ تا ۲ میلیون دلار عوارض می گیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125728" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عضو هیئت‌رئیسۀ مجلس: وزارت نفت صراحتاً اعلام کرده که قصد افزایش قیمت بنزین را ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125727" target="_blank">📅 13:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل: حمله در مرکز اسرائیل هشداری خونین درباره ضرورت ایجاد تغییری عمیق در میان عرب‌های اسرائیل است
🔴
اسموتریچ: گسترش جرم و افزایش افراط‌گرایی قومی در میان عرب‌ها در اسرائیل، خطری وجودی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125726" target="_blank">📅 13:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK2OvznSIqSM782t4jIopyErmKm5D_z6gKDRrL71DVrSfNaoNbxUXbo7Ibfr71MbCYq1HjjZURREhVfMOXGgHU3FhRB9mtTI4pkJYTVYzqyrnQkWo8LI2jwfRue5SiSmxa-zTmpcQO7ghN85S9yIlmR2sLWzGdX09vKQfhlQ_37zuIndhdAlDOO2Zziygjmy3TlT1LYuZYod3b1QReuaqMZuMIaxnzfqhDkbQ2Jn7zvp4UmhkeoT3ZIKnyW9FGwJG2CDhKQeqj9wctLMA8KyWAhgSQxmRscLd7bDSfZAM1ONBFis8S1fq9qE_r6bxOUDLORdTG-JuW4UhGw8ik08iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح«بانک زمان» توی منطقه ۴ تهران اجرایی شده و بزودی به بقیه شهرا هم میرسه. حالا چی هست؟
🔴
توی این طرح مردم به ازای پول، با زمانشون بهم دیگه خدمات میدن!
🔴
مثلا شما یه ساعت به یه نفر، زبان آموزش میدین و به جای اینکه ازش پول بگیرین، اعتبار دریافت میکنین.
🔴
با اون اعتبار مثلا میتونین ۱ ساعت ماساژ بگیرین، یا ۱ ساعت استخر برین و یا خدمات های دیگه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125725" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی و وزیر کشور پاکستان در مورد تحولات مسیر دیپلماتیک برای پایان دادن به جنگ تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125724" target="_blank">📅 13:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران به سی‌ان‌ان: مشکل اصلی ایران در مذاکراتش با واشنگتن، مواضع متناقض آن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125723" target="_blank">📅 13:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری /  یک‌ مقام‌ ایرانی تایید کرد که در صورت استفاده از دارایی‌های ایران برای تعمیرات مناطق جنگ زده کشورهای خلیج فارس دوباره به آن زیر ساخت‌ها با شدت بیشتری حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125722" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دستگاه‌های اجرایی موظف به استفاده از پیام‌رسان‌های داخلی شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125721" target="_blank">📅 13:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoAcHURoOZWAGk74OaMuuz929I-I-IT6tubRd6imSLCKyjTaLNRdYv56WmFUuXUhzc-YHzhMrqWdUBzj8DyKPkowR6Y4Qeepbmgs-rXV5tk8eLtQkPKsZZudL_Zg3EHBdZQ1VwjYvj0YHMZChYRBNYkT5ID2dmAA85TDxcLMYZLzvsdP5XzLtYeyjs_RtDN4HyFwIfdboU9lFkiV9z3O-TgMT19Z_5rCCyfnH1w0aaRs7tPbY5CCaObJ9SF34kIQUQQYqwJlkXBjNEbfXgUZVop1GYN-2PP5L87OvtJr6uEdTqGbtR2j7CeFG522SPOSvX-meg5cNBXkz3H9s06YoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین 200 بوئینگ می خرد
🔴
مدیرعامل بوئینگ : این سفارش تنها «مرحله نخست» یک توافق بزرگ‌تر است و انتظار می‌رود در آینده سفارش‌های بیشتری از سوی چین ثبت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125720" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGxjASmqR0mS9rCzNFXKhtovfHD9UNuxj95cnnDfPe8qJ-6e98uIxrcKvdDnibZYsCmH0nMWvb6nNFajJcigOI4tgAB50DbvB2orvxCw80BLzSmmR-KSR6vUyFu_APd6KwenZi3tuXTL-jT1kEd2ujawMXSpAGOwCUbR6ff0eVUrSZxXuDd3pRgsLrZJy2CAoOwDmsR-Tpt_6SiYBUO4WPDU0dUtB7iXDhVvCPgVfxbLTDux11Oh-NcnOdU4v8LmEvONeR17Gf6gXYBYORUHvpKEM43OMrpF2yhagl-FIEZAwPMGDDxKy-LISpfqZyMUx2IoqmAgkLdK0DF--DFKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125719" target="_blank">📅 13:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
معاون وزیر نیرو: در دوران جنگ اخیر بیش از ۷۰۰۰مگاوات نیروگاه ما دچار آسیب جدی شدند؛ البته همه آسیب‌ها و کمبود‌ها با صرفه‌جویی مردم حل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125718" target="_blank">📅 13:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وکیل: توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
🔴
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125717" target="_blank">📅 13:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف طولانی کشتی‌ها در هرمز از لنز دوربین یک گردشگر در عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125716" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv8SArXlrWPEv7Fj7rIschOU1lUyS3jGPdCoXNe1vV9NamSI4EZe5eWIuCYpUbd4Q2fHU9iATge8k2MELsIdSG67NXlieCa2dh9EXUYYV9aFBa_h1TbYMfSSbiTXv8Cz2upP2i1F-jUVTUIbFbgPn0T-YPoZcASH4b-mBTcZjHpj0u9OGVtGhpx9gUurCiVjJWtTWmuv0y6F20-nkc8Z3JtJXEC5k3DjuxK2gdwYo_Pqt4-x4br8x4mB54yKp6jH55J8k4p7PWCeBcd3BBY7hGpnKgWD21ZzNRBPtRUy11m0-NStnMy_cjYcKK_xbSm6vC2cfRO4d5Vx2LXl_qwwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از زمان جنگ ایران خرید غلات و دانه‌های روغنی کشورهای خاورمیانه نصف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125715" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbj9yKHUG6w2atRR1o7EP4SWgMDkzdsGpZmHBrHFeW_x02MeDAceOHzo1icdou1vJ0J55YUWpne3Vydn3xQ6srdJIP2AV76ObNQ7lKNKvheVCo6pMyajCPoL2c3vEv3YXesnQQcVPtTPTT8ngJkJsE4vBXjoey-znjiN28-zx1AWPP_aKNdF2IueZD0ymjAn6KCDKEWo78LF3rzr8592b1R9xpYkVLW1PqDkzKQRwH5uPkb9fPOGoTF2cuUiFAPNqFJvhP8m4SsU2i_BrpdZH_VyZB0LpUDcOsVgi1euexAqSDhKI6Grkb125Kp35aEIUtbMZJ9_CfCQj2fmBeY7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبارهای موشکی کره شمالی
🔴
دولت کره شمالی برنامه ای برای چند برابر کردن ظرفیت تولید موشک های بالستیک برای سال جاری میلادی در دست اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125714" target="_blank">📅 12:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت دفاع روسیه : تو ۲۴ ساعت گذشته ۵۰۰ پهپاد اوکراین رو منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125713" target="_blank">📅 12:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL0FdEjh4ZUyVB_oJAt4LFQRTGOGMceHHKUxN4ThsIoxNDiW4ATBLVO1BK9SlQ-4FCp0yRmt9GZNfIPsvdyrBeGKKCTYqzBN3Civ9g2xt8N-zVeatDqxJY_PpJMKzDUGAKMkPsqx7rbIos_0Xw5-1jfGVo3re1wgDGvHDUXTYOC3NYye5x3rmXg_Z0fIpIULAXxBbUXqo4x8GUmRmkaDce4cD3v3lNqQlR1REuT79PY6fTbFZQiaYdT7aauOVl7u6qfDKt2H0yf0KBHZpOZg4PTu_01cJ53vAR4Q9SK__8jHeRlrFxoZx1mBX_bWnvZwrUH-ypCqdVFaI4xp951rTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۲ هزار واحدی به ۴ میلیون و ۴۹۴ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125712" target="_blank">📅 12:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125711">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نت‌بلاکس قطع گسترده اینترنت در کشمیرِ پاکستان را تایید کرد؛ این محدودیت‌ها در پی تشدید تدابیر امنیتی و اعتصابات پیش‌رو اعمال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125711" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وب سایت خبری «والا» ارتش اسرائیل عملیات زمینی را در حاشیه شهر النبطیه در جنوب لبنان آغاز کرده است.
🔴
النبطیه یکی از شهرهای مهم جنوب لبنان است که در گزارش‌ها گفته شده نیروهای ارتش اسرائیل در اطراف آن در حال انجام عملیات زمینی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125710" target="_blank">📅 12:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نامه‌ای که وزیر کشور پاکستان آورده بود برای مجتبی خامنه‌ای، تحویل عراقچی داده شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125709" target="_blank">📅 12:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / خبرنگار الحدث:  تیراندازی در ۴ نقطه اسرائیل رخ داده
🔴
تعداد زخمی ها به ۶ نفر افزایش یافته و یک نفر کشته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125708" target="_blank">📅 12:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125706">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCE0YtEZVJOz_uxU4t5eAdBqJQuk1o0NK0mFD_iCnYSJdtLokJihHpDvYuGczgoKYHJg6d84fz9QcR5A2fFQpkCqRiaL3KbuMhlxkg3Y9UzhHp8E23QH_u6-85TR23sgVpElESkaa24Zu03sReyiILt6FTri_ZYbNFyCr68rqb0h08KrGlKipXUOec_TrRuQiwyIglR3SKtb1CfHj4z28zQ6kqUxFyFcynL54lHeHbjoxg6tyvBSQNy8c6mGal78vOaA3BB8vzH26Xw7ci-XKCT34Q83vqOpRWiYlWdwQIeZlbCFakVJiraJGTj0xGQSIPOdqvCBGmT6Fprw7UV7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4OhfwwkO7-Y0PNSS40Wk9R2TWM2N4GqB-7VF6KHvYdMXR59YOs_yYD1SEbsm8b0Q7hsiMo101aXa1V7W4FlDVF8dZH23SWU5vLCofjK4S3q0OzEyvhKzg4X5A366UDET0XyMMB8um6e0aN0ncnnv6w52788-RO1hEfRKJ6-NNcZK_6Ssskv8yM9UI3zfbyNGZ5NxXG6aRRNi_Cn72RFfQAQZD1cBItK2lU4o1EdfoSay2LHzxPemAIh7ZnIaNgnGULnI7KZxddkpGpCuM4ABSYsX6Jp9rOlkkj59cx8ImxRZDzNRVJmX_GfcLbEDnvJFL82i-LUOI4YF1m9xspjxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر قلعه نوعی دقیقا عین این ایموجی شده، حتی رنگ لباسش!
🫄
@AloSport</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125706" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125705">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مهدی خراتیان، کارشناس حکومتی، در گفتگوی اختصاصی با برنامه «ایران‌تاک» با اشاره به دی‌ماه ۱۴۰۴، پایگاه مردمی شاهزاده رضا پهلوی را رد کرده و علت اعتراضات را افزایش قیمت اقلام خوراکی دانست.
او با اذعان به اینکه در جریان اعتراضات حدود ۱۰۰ شهر در آستانه سقوط بودند یا سقوط کردند و برخی فرمانداری‌ها نیز «مانند آب خوردن» سقوط کردند
، گفت: «ما دقیق اطلاع داریم که لیدرهای اعتراضات، جمعیت را طوری هل می‌دادند که سپر انسانی مقابل ماموران جمهوری اسلامی شوند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125705" target="_blank">📅 12:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125704">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq5yB4kPz_tWif7zfaV-ghNqROIb-nDqXlCJMQopor_7SS9-fc2vuihch1o09YAZO88rE9bOXVwNsVivVqdyVHCzXkfqPIfXh6AyJu2Oq28LksgCLRCvSfDmly9OBgTlqCPaC-R_3VCSIu6x26eABvH0v11c__ZwNvAotZHKaAFv6RUCPYl1TU2RxjVyR1Q9cnoGZlnfCYLjaHfwhf-aiYQQiB35xcnjSiCtpfHCxhpbAIzEGqZceEyiolFXo8vbpeM0oHdW4JBNl8lAfcEXyp9HjARspsSrtp3L1dE-3lBlAaNevF4VxWD4X5ODYEdrJgveaCHCrox8fitrPEocBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه‌ای که وزیر کشور پاکستان آورده بود برای مجتبی خامنه‌ای، تحویل عراقچی داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125704" target="_blank">📅 12:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125703">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPIwJWO-RRNL20AY4RNgWYiqAgWoi6XctWqdg9BstJMZiWZHLgGTgsnkL3dtZELC9BiyQpOJGuuRSHiEfXuzIxsnLytOc9hzkbLKotHAglf4-wwvAejlXAMJdog9ZIv7yrGprunsI5QkjqWw95VIfd1awxLeY9Ym1E0zlogB10Qm3oNGoaiKjIPXhXffLf5qr3GYDZgdLWcLw85sS_BhPpn1CIR26ymwOjwPCpLsxT9rUNHnMixgE70ikVvrXmJud_xKBqSTQ2SBAdoEE7j1GR_UVyeyZ3r20HazhmYiI-yG60SLZ9qptkrERc1Hbs5mixVATgkFzbGBBj_hQHtzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسرو پناه:اونایی که اعتراض میکنن دانش آموز نیستن بلکه مافیای کنکور هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125703" target="_blank">📅 12:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125702">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تجمعات شبانه : ترام ترام حیا کن برو خونتون لالا کن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125702" target="_blank">📅 12:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125701">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
طرح رایگان‌شدن مترو برای ۵ دهک درآمدی در شورای شهر تهران رأی نیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125701" target="_blank">📅 11:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125700">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125700" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125699">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره: ارتش اسرائیل در لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد
🔴
معادله کاهش تنش و محدود کردن درگیری به منطقه جغرافیایی جنوب لبنان، همراه با محدود کردن عملیات تخریب اسرائیل، در عمل با هزینه بسیار بالایی اجرا می‌شود.
🔴
اعلام کشته شدن یک افسر و یک سرباز اسرائیلی در درگیری‌های اخیر، موجی از خشم شدید و گسترده را در محافل داخلی اسرائیل برانگیخته است و تأکید کرد که ارتش اسرائیل در جنوب لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125699" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125698">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی   وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125698" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125697">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXbhPWO3Vl1vzQoMz6seMAxt_yxtr1oZY2CFUrmkObrZy06-cViXb9LmwiBXl30pvhos1xfMn6y7H0UOjGPA51EV3-1ReJJAa6_tOmE_eVh6oKVhXGJORtI1SAzig8uXtfOKevYnJp04S8PfF-OA8gS9udyZ96uLU_YE86Tuzpvd07XzitBCpyG32tThNwLGO2ixh7a4-TJGjT4dKiy-BIGRy-mxR7bbFVUlL82i6vDjGVEhipNfVZxcuGWgCZ4mV7cazuEehNg3tDzsuKItinen6MBjuha4C844iCc_IOUuiTKkyRHa8OsQzMTNZ-0U-qkyUeyKymK7pqdnA20inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/125697" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125696">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تتلو واسه ماه محرم درخواست مرخصی کرد که بیاد مداحی‌ کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125696" target="_blank">📅 11:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125695">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در ۹ اسفند ۱۴۰۴، امریکا موشکی خوشه‌ای که با انفجار به ۱۸۰ هزار ترکش مرگ‌آور تبدیل می‌شد، به لامرد فارس شلیک کرد
🔴
این، صحنه‌ی آزمایش جدیدترین سلاح مرگ‌بار ایالات متحده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125695" target="_blank">📅 11:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125694">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3FdiGnvhIpJkJiQMZUymQx-81W2YaU7KdpkHy-_mNQh77TN6QfQPeQcu5QFgb8uMuF1LaEsbcPoxjGVf4l9nfO_Yoxj5Ix0v61o1uwFavttq7TBPiasVdNBLixCn4a28T9Yi7fUZx9Tmj2x0D6mp95SnafRSqbOJOcZNCoyHOq_xmb1AYSrwCjdhcV-wwPSOqy4tJwoyS4UoBQP_USgKGDGQ4GqIF__P6g_y09Z1FPnGQN7hD3WqRwiHYgXzIcDvFJRHpRCjj71j25J7QJ_veSg43LFZhJa3Vq1DIYv-Gu-nSnAMulSH4mfqRQdWZKoQXm2wmw7qIKomUyTVmAH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس تهران در یک ساعت از آغاز معاملات امروز، ۸۶هزار واحد مثبت شد و به ۴میلیون و ۴۷۸هزار واحد صعود کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125694" target="_blank">📅 11:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125693">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125693" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">‏از وقتی اینترنت پاکستان قطع شده  کانفیگ‌فروش‌های ایرانی خیلی جدی رفتن تو گروه‌های تلگرامی پاکستانی و دارن وی‌پی‌ان می‌فروشن.
‏توسعۀ صادرات و ارز آوری برای مملکت به معنای واقعی کلمه و آتش به‌اختیار.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125692" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125691">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125691" target="_blank">📅 10:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125690">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
معاون وزیر نیرو: هیچ برنامه‌ای تا امروز برای اعمال خاموشی‌ها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125690" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125689">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125689" target="_blank">📅 10:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125688">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در طول شب، پهپادهای اوکراینی به انبار نفت سیمیکولودیانسک در لنینه، کریمه حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125688" target="_blank">📅 10:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkahdQEOBbWbbrAOlT9vWMRsyjyszeF-R7bf4M91UySVgw6Dj2VY_FdK36ud4Z-iHeCmPGRmnpn4zxPkGqSn91cCedHYqHC-rJKzNs2n_tmdKgprRAHgknKvKJCEw1Y_dvIkZxcuuI5pHRAlnz2UUHqW7rjHFvFHuEI_sZqRae0AjST87NNjF4YDiNQxVBJSWiR_bglIjvdw98KLcW3Mc59cKXJfxPvJToHAp5CQm37PzxcQwf_gyhhsykK3sG_0-y50Tqc7K1CpiBXKvyzc1jBImB756GtvUaNNDLLgPa6sP0A0Ad0tvspdudrWjhQwMWDcvgWHGu05WuAQCbzjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:مذاکرات متوقف شده بین ایالات متحده و ایران... و یک "پیام بسیار مهم" از پاکستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125687" target="_blank">📅 10:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125686">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روزنامه اسرائیلی «یدیعوت آحارونوت» مدعی شد: خانواده بشار اسد رئیس جمهور مخلوع سوریه خواستار خروج از روسیه و سفر به امارات و بطور خاص امارت نشین ابوظبی شده بودند، اما مقامات اماراتی این درخواست را رد کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125686" target="_blank">📅 10:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125685">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9YLplwjE6VqFzk_PeyuX8MpCEXPZD3S5M1YyC0p_CZWX4d3eUTFFJjRSPdKDWOiSgPST-OAg10d897zOL0gZHzTAA-bo3R6BHWlOla9BPUUec3jQXpanLBSEsDyUpMflsk477i5DabvvP4nI28b3uTifT2Nok45Avn8UIJmuRT82LZMDfXT9ZZHZKKX-eQ3GnN1qJDFma-cYIkAk12auvNawCXaZhWV95NJ5iCm6iQ5R7kseNJKREEeA5bVKspORt9hHyMm9xUKkQt5bDBdaWrYlYT4LGqoJJE5_uoup6iKMw03aMtVB1qkYWbEGppbduJeIl00yClrnH2lhIYe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر سوخت تقطیری آمریکا به پایین‌ترین سطح از سال ۲۰۰۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125685" target="_blank">📅 10:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125684">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الجزیره: در پی جنگ علیه ایران، ۱۴۶ کشور قیمت بنزین را افزایش دادند
🔴
نرخ مواد غذایی نیز همگام با قیمت انرژی تغییر کرده؛ این موضوع بر هر مرحله از زنجیره تأمین، از کود‌ مزارع تا کامیون‌هایی که مواد را از مزارع به قفسه‌های سوپرمارکت‌ها حمل می‌کنند، تأثیر گذاشته
🔴
اگر قیمت‌ها همچنان بالا بمانند، خطر سقوط اقتصاد وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125684" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125683">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فرار هالیوودی با خودروی پلیس؛ متهم دستبندش را باز کرد و پشت فرمان نشست!
🔴
یک متهم بازداشت‌شده در آمریکا موفق شد دستبند خود را باز کند، از صندلی عقب به جلوی خودروی پلیس برود و کنترل خودرو را به دست بگیرد.
🔴
در نهایت واکنش سریع مأموران، این فرار جنجالی را ناکام گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125683" target="_blank">📅 09:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125682">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یدیعوت آحارونوت: هنوز برای اعلام پایان توافق آتش‌بس در لبنان زود است
🔴
با وجود اعلام حزب‌الله مبنی بر رد توافق آتش‌بس، اما حملات به شهرهای ما متوقف شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125682" target="_blank">📅 09:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125681">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_PiE0_CDEMqiJHn3rl_sFk0M4J9GphhWXKikoBe8vylgNu1XYtWFZuHI2YdTs1iIEsn8J2A1ngnZec2H0dkS4SD7hxx3ZuR3wbE9eX-CgO-UwLsdTurXyct2Jc_Hi6eQvU2ONlXsLLn-uDfTm5ihaJEjGccjH0zTR3ObZ_5IHcCOzROg6HldAZtEDBrfq04XsgC64_D_aGKmTQDVvxqWdLlxPyMEElmtaKCRsbKJYJpvOXV9HH7cy1YSySRtyq0tyuQfzJADc6jun-gBC78QQJIv-wCEv2VISBCeIvWMBVwBTOE3Y3GxtvIQnVFzTsW2Dh1lkwzLyOSg4hR3o9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۳.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125681" target="_blank">📅 09:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125680">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDvutrp5ml9SGGOnRftK8lPHvDsSr1g9rJ-MMHOcELfxhJRMO1Gu2Ns0we2dZx97PKc3CFbNfa6ck-y0Meyi8jkJoRqFynJ4cBTl6ug6NVtHypbSi6VJxLI74v0sN7yimsmu67P0FuFuoWFTojluuMnR69hFePnhglBC2ZFo3KTbKfVMuc4ZwMNo8M_Msd_p0ysEEUMsc_DNVosmG6iWMDCwS1Gv3jNay0UjukuVNvZu5qfHbyr3KpniOHAClyE4-5tFlFrdywGX2J2awCvxo9ODNPsj2PZHpsS1p8662QrBpBOf7OA5RfVFGYJVP5eXUxdcf8ugqjRLz87LZMJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشار تصویری با عنوان بندر پهپاد نوشت:این روزی واشنگتن را نجات خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125680" target="_blank">📅 09:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125679">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKq8eVg5xpxr_hlnJ8SqYl3wlmGHos3iJq-E3RzDZvSDpLf3R9OowdIg1g7MoZ9oA2-2J-qiqPpjIIKF5mj1ZqDJB-Qya84eV3BGbIkmom4ntO2BWYJjo_0lDYToXkS-bXC0W1mhnAMOhF-P-jgno_jn3f3erzalk5Oa_5cVKCl8pPL-J3Agr1anKQnfA2NxTF7v7_rcYhpPXS7KdqKIzRaa3lSgq6fUyEs8V-bT_UnOVmSA-9ZMEILDquvoABWg-tCAXnzBm87xzBtkzkMbn55gl4BDOqTCED6fckZui7sg5crQbTtVEkb7AUpT_4Tev9iPs8T1k49Op1h_p0jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر کیم جونگ اون، اعلام کرد که کره شمالی هرگز از جایگاه خود به‌عنوان یک قدرت هسته‌ای دست نخواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125679" target="_blank">📅 09:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یک تیراندازی جمعی در یک جشنواره در تولدو، اوهایو رخ داده است که در آن چندین نفر مورد اصابت گلوله قرار گرفته‌اند.
🔴
قربانیان به بیمارستان منتقل شده‌اند، همراه با تیرانداز که در بازداشت نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125678" target="_blank">📅 09:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سفیر ایران در مکزیک: تیم ملی فوتبال ایران اطلاع یافته‌ که باید در همان روز مسابقه وارد خاک آمریکا شده و پس از پایان بازی، از خاک آمریکا خارج شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125677" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل منابع خبری عراق از شنیده شدن صدای انفجار در استان اربیل در شمال عراق خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125676" target="_blank">📅 09:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
امتحانات دانشگاه جامع علمی کاربردی غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125675" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کره شمالی: سلاح هسته‌ای، حق حاکمیتی غیر قابل مذاکره است
🔴
«حتی به اندازه یک سر انگشت» در این موضوع عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125674" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGKTRr66lUC9wibSB7yvOuJHBNr_kyu4lSClu_Z7onvjuoS8RM7BAPUB4yGf6lqHIH9ssm9VPelyd1WV-rNEciDOHs-jqQ8-RQHCeMidKbIMTyPnjckOxeo0NLJ1SVTpiSXxL8-qXpvQUdIaPxeJ2axsOk0Locfq6_WE78jytRpV4PqBC5pLk8YTehPCSgs5ykbwokJgvDTNwI0qHUeXmi7SDhW_8iUoFBPrmvWmlpUyV8dsfJJEqFM61DsiJINuEF2jyPabJS3TZF_g11tfPfQ6Ja7j7sD8_0VvIwjSAZLf1vn94PGIaYkasMWhkHdHDIUxiVMdq0PelGCpO2TsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز دو پهپاد ایرانی را بر فراز تنگه هرمز رهگیری و منهدم کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125673" target="_blank">📅 08:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پولیتیکو: راه‌هایی وجود دارد که ترامپ می‌تواند توافق آینده با ایران را به نفع خودش تبلیغ و توجیه کند
🔴
اگر ایران موافقت کند که برای دسترسی به دارایی‌های مالی خود از یک خط اعتباری استفاده کند، ترامپ می‌تواند ادعا کند که بر خلاف اوباما، هیچ پول نقدی مبادله نشده است.
🔴
اگر ترامپ اجازه دهد ایران به نحوی از تردد کشتی‌ها در تنگه درآمد کسب کند بدون اینکه به طور رسمی عوارضی دریافت کند، می‌تواند آن را به عنوان یک مصالحه قابل قبول معرفی کند.
🔴
اگر ایران به عنوان بخشی از یک یادداشت تفاهم درباره چگونگی پیشبرد مذاکرات، تکرار کند که هرگز به دنبال سلاح هسته‌ای نخواهد بود، ترامپ می‌تواند آن را یک امتیاز اولیه بنامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125672" target="_blank">📅 08:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tohEHrfBbFVef42P7I8FtnxrSTEQxj6M3qnAEx1ZNHEtUbO4AQ0llDRqpZQDVIdmP3WMSUMP4nCbkpJ6tT1aoPsfK-ulhiaG-2beO8U9KlC16phPflbmG5qOozxmaTnPwPhf1euLXdcjvrHf3KuPOpLFz9fDWNqq4IIGwJIZwV1wsMs_jH3WMTZcQSbye6oJswn20jGoB9unr4CSymgUGFVb_nHl7V6TGZFTsQYMw8punh5r2r7wok4c8VipQ7uNn8jK2F9MqZBoDIuAksaEzA1b4fQXCt-7pKUAFmVFRgv4Uj_vU8a58iduvI1lMCqKJIrTK5Hy013mv0XE-7Nypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل ابزرور: تصاویر ماهواره‌ای تأیید می‌کند که از آوریل ۲۰۲۶، عملیات توسعه قابل‌توجهی در «منطقه پشتیبانی لجستیک ارتش ایالات متحده» در ینبع عربستان سعودی، معروف به LSA Jenkins، آغاز شده است.
🔴
به نظر می‌رسد که نیروها و تجهیزات نظامی بیشتری از آمریکا به این مکان اعزام شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125671" target="_blank">📅 08:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر خارجه عراق: یک فاجعه اقتصادی ممکن است رخ دهد؛ اگر جنگ علیه ایران تا پایان سال ادامه یابد، با مشکل پرداخت حقوق مواجه می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125670" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTVGwXSBDGiaUCRjyV_1fP7CX0o9Gzrmm4S4uZKX5jVuEvocJKFr11OONUblO8HOILrBy0iy70V4o39WFz5uG8HxaFlG0bWObEQS3eipPpf8-WzSRWwlTyJOMvZ47umzoB5UhXMeB0uFY9u8MLe8cSQ9pho5x3O5mNElGq8G-xMh7Uki46ED9G6-Q2CNCS7qjzbZH5e0-UkRkdCEz9mZMveYsNnW-nS26caMAyww_x3yrja0qxBVzPPhkYV3iXCGPWUqml-PwBfXn4u6DIUKop53XjfnWNmn9FFsQeG30weoRGipm6ure6lyXPMCHr7uwdPRSlLPc6ApNTjDbGpndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش CNN: دولت کوبا شروع به توزیع سلاح به شهروندان عادی کرده و رسماً از آنها خواسته است برای یک تهاجم نظامی آمریکایی قریب‌الوقوع آماده شوند،
حکومت نظامی در پایتخت کوبا اعمال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/125669" target="_blank">📅 08:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_DLYbS3EppG54ErI9OFfGe0iDV9kUORGjMfURN3bKLl0QCizCJ2m_9rG4ZlwBcOGgnsi67JFRMQA_dE1lmANdPlDC1Uw1pg_7JmRxsK64JEMUJBtKn_fZPqWSeM5gopme6MEoJR_h6qMvw3ha8lqKVvqe2EK1frYRa5thZoOkH9tzl6eJsO3TS03pvJVbowAtI6timdu-3GI9JvbzRQ4T_EmVYAUpuR1NA_X01rgP45W6FRKrywzIaexSb0bPe4bh7jBZ2cAFmJz5v832Nr0iqaNHa4ylylc1jL-8ydmFulNASyo3__flbikTOQGnYslRUWtCmXubP_DMDHl6BG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرچ گوگل یک سرباز کشته شده اوکراینی: مذاکرات اوکراین و روسیه
🔴
مذاکرات زلنسکی
🔴
جنگ در تابستان به پایان می‌رسد؟
🔴
چه زمانی جنگ به پایان می‌رسد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/125668" target="_blank">📅 08:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کیهان: چرا از NPT خارج نمی‌شویم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/125667" target="_blank">📅 08:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxzqtlRJkFkL6ymhR7UJsh8Kcw-b54mOLkMtChrC4v--uRGr36ZWICNdKRtMMarrqOiOsINuoIXDF25OPPO7iNKSALsTL5qwx8W7WeWPMIxq9ZhWQdR9tGVnTwtusfQsWTV1Z0HOD-64knVFaZ51ITU7TqwuBmUAqxrxaAu1kgyKifWlE9SGICEv_caEGzWUMntghaedmZ7_s0dIOqoO43ZW8TxBcOp-Asz_UEDDMTrJv-CcMqO9SHrMRReZ0Yz4yuTBwGVaw7bAd4820kDz4pEAHY03PDC_lFsWJ0jVCv0OJf5Fg8MP4YqJp_z_WMmpzQw459EsqQ8jcCzHcMFs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/125666" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0rorRzdaghndyAbecL3S0VKYkbri2SHsqIjFEFwYpO0axg6GGrmCHrgQnEVJyxyGVsROrPCaD6409l3tG4YkPzkuamlomCZ1TXXOF4gw2uMT1aQ07z5A0ucU1QB6HOWhzon1QXj6QbBPZyWskz7o-hwcBlHy0w8LiRCeNqsdXIHEbvyG6O8zAvv4KsnhS3KR_DtE6TO8Bt1w5qM7ZlfQEZQQ1pm-ajUlGuxHPZbznFv5zA-1MAg8lMccicgpoNaZwa-K-3zWIz96pLi_B726j-UBCWL-3-R4gilX4sv2vXvupIggaT4lAazmNalmFnmi8syttxjRB_n9B5W47skiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید نشان می‌دهد که انبار متعلق به شرکت فناوری انرژی آمریکایی بیکر هیوز در اربیل، کردستان عراق، کاملاً تخریب شده است.
🔴
این تأسیسات در جریان حمله پهپاد کامی‌کازه در اول آوریل هدف قرار گرفت و تصاویر نشان می‌دهد که ساختار آن به طور کامل نابود شده و هیچ اثری از انبار باقی نمانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/125665" target="_blank">📅 07:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/voOe_XjOX6w_jkg-dNGADUzSG2dwSwknBT1fObzu20v5yCH3h1iPmX8ogY5bwWAmXGk8a1HYW9wcCqEXYX-FPskQFx5B6m_F2bhvcycn6hPo5CTsqs3lNc6m6Cr4ViHByx7fpf5t-TQPW_5ElMDeOrxDvtPGrmot-Krk2O5bBpPSFPait9f7QPCptDtpWzCkybkLECUZ7r78I2a_MChvobKb4RFmT8-Zr4HimwKuL3ZA1dkQ1b08JQM92Z7XAcB3i9SC9fGNYZ69XuFE8wiQEXfzj_JT-cQnEi1faowZKtwlDikV9_c6PKiDxTSAJv2C4NcvDETRtx34K8AwrvRk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/125664" target="_blank">📅 01:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
پیش‌نویس یادداشت تفاهم ایران و آمریکا در اختیار نهادی در تهران قرار دارد تا در آن بررسی شود.
🔴
این پیش‌نویس برای اینکه بدون مشکل به سمت اعلام توافق پیش برود، به آرای اکثریت مطلق نیاز دارد.
🔴
ممکن است در اواسط هفته شاهد تحولاتی استثنایی باشیم؛ البته به شرطی که دولت آمریکا مانند دو هفته پیش که تشریفات اعلام توافق آماده بود، در لحظه آخر نظرش را تغییر ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/125663" target="_blank">📅 01:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip-D8AFEPrL9zHKbH8yoW39f8DO9ZqsOBzfBqWh93__x3F5SoyVfRP7rV6vUyyCZwuQ9BGi9P722aRzugGaQsGuu4-AsGyVbq-9OfuxziO3GFxo6GmCZPoX0vqx6O_sN75PkWMSDNCrJVWxS6ExDCdvvPAtC8eTaNQ6_5LB2ZZgp6wb2P6iOMqJ1FnVTL7xMZstZzK6I2Cuun1i_LINDYQCohva0ZclQZV1xdJnn0ZE1dsNW4S-tXaAQoh44G-cw2GMsTfrhEKxsl0FJsRe4OTXLbiPatuDLLfAio-CdyIjHhCEoscNpHB7_tbvUKHliLwHVGhrcl2ZHPWrJVKT2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنعانی: حاضریم تو زمین بمیریم اما پرچم جمهوری اسلامی بالا باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/125662" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخوند، اسماعیل رمضانی : بالاخره یه جایی باید مشخص بشه تا کِی می‌خوایم مذاکره کنیم
و باید چه اتفاقی بیفتهِ که بعد بگیم دیگه مذاکره فایده‌ای نداره و ادامه نمی‌دیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/125661" target="_blank">📅 00:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Akg-yauBMAHgUJ3z74z4OZQ8Ely-DtPYxMviUWAM08eFVLo9JA9FMU5WPBYC3Mbx827_UrtUwUHcXsAL031-pgjVXD87iZhXcFK3s4IH_Qd6emypHJd8nHCwhSrFKQtTrSj5o8MAWT1BSRwZgVE1EdDkmkiQi9_DCfQKJcNmh3-rEO-9eC8HIVuz8HX2plCvZfKtCwbnOlGxw7jr_GDNza-ZUgl_YRI8gFI0iDr1DqZzMusjIb-fj30Gs8wBVdd3tZwue7rE5tcUoVvgnLSSYdCJuIqfeKlCXe8d-9M508XMjFxU_Ir7fOtY5AJu-Vdfkm8UdnYAyfJaDnESeUj5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درپی درگیری میان پنج دوست صمیمی در ورامین بخاطر یک دختر، چهار نفر از آنها به قتل رسیدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/125660" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1ErrpJ-WcCHoqqnCMb9_R_TJ0kyA2vgWn7Di7AOHXXlx5-kfenVf-gfvWJjZ8KTg9L2Fc3O0EPLc407Om-VCdCu-FKcSGofHc3w0JcsoLERqas3HXvXefPQfjoXwSiVmVX1bx_-ft08Qpf6d-t9WqYuzkez-SSo-txUbm98dFYsiOPpyVt3U-651ZroCVW88wLuVKgr4iX1qYjDTBXdzJvyI19uosRfiMmcnUf2sWCbNLstRRjSFJmf_cpjlui2bM1mR-sk-2EOuHJJolwMk0c5e2n6P_E-RGHKygNAbzzwdV6PIfrt-I_awk8tVIhPklkJIAULQ-hprp19Q7kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به انتشار پست های عجیب با هوش مصنوعی ادامه میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/125659" target="_blank">📅 00:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ثبت ۵۰۰ مورد ابتلا به ابولا در آفریقا!
🔴
سازمان بهداشت جهانی در بحبوحه نگرانی‌های فزاینده در مورد گسترش بیماری همه‌گیر گزارش داد که تاکنون نزدیک به ۵۰۰ مورد ابتلا به ابولا در منطقه مرکزی آفریقا تأیید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/125658" target="_blank">📅 00:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mot-dFe2KWdHxYunV5NUleKOM-rukw0W3yT5g1ObCPJmxXFZh1omVyDcBiTadLIAn0MXd5AJGA84WaxdKafUvCuICT21gbg8glhlnf9LaAVctEiqHsHoNzInrmcfmxf4qAgBB3WSv9RKp29eJn-hjIOZRuUc0TujAklOul7a-dMwwC2FQt-hUdWIh363Dqe37mPFFuG9ciq_4mRl_AIhvWzgdS2wsISJZ4kkKjDa1KTVqmsnaCjvvBWpxoIPQ8KSnq37aO_peg1Ah2T2OpTH4EP_HGYlzLOOmaK3xB5r5xgBPvETZQf5enraFxTK2oUs9PFGXvHMAZo-S_gbi87hVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/125657" target="_blank">📅 00:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FYjxMBcV97SQiXPj0xR8kKm4Vcz-l-UMoWC5NNlKft3UCHP2B_2qQncSF_CZjeakQ2rpeA1Fq1EDVvphcEz3MnnFwHnIhsrJ2o6dQ81jGi_m-AVL3dJv97xhqPLmgpcB-GbySDMvb0hKUHEfA19rg_iWxFUuEDlJd8wjA_l_pfvAP-JHuGm7NxdH6CjlDJQCW0zRY5O4jBV0dWVx_wzQMW92uFeII7hdwm_m8ylm774F4L0bFQwSgvz9eZsDJz7Lnsm73X8y1rsb8tJl5b4fJzT3Nyb-ImikkoNUrmEqZRFa70Gnw3xgTf-rP5HUPDWrZ4Qa17Le9PQK30drjP6QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fmPbwDL1MrX7O3bLXZvD21mv6Bp705IBjhCPy5jonWsfCi-wpLTZ1dY86W2PwtVqhcDk9e66xZWTJ-I5OMcw-7Ti7LUyuA5p56R99tMfcFE6hw3xqo8GbVQVvTGwnK7xWmBn3ABVSnsB1c7QQjHRofrVjN5VqSA-wj4sD7H_MWq4VpSr-1HalpTx8YrqMfDnL15SSFzQ_Zsi58BYbp4DoF6qRbUZncWHfQdpvHs_8CT6DxHBKbEd1DH2No3ZEIa06D7MNJrb7UHnsrpGsPAxOkrATFLFv6YJnEUqlysMg6n7xkr8LTrKK_y5b9_hdkIBLAbHrV7PEFh6aVNvxqgj9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسرائیل اعلام کرد امروز دو سرباز دیگرش در جنوب لبنان توسط حزب الله کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/125655" target="_blank">📅 00:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lny0Ed1yrSek4kPj1PcdYAMdrrV0hpsTHA-FWA0732WEqBldOL2433uMQMxtuqWtFtjn7OmY1BlZNar2ceqBNp1p8aM80yBk_AAoGpqoFrATFj5MxooIg9L8p7OiZve1s9Apj1QGMMXNRELa8OUBQZd3zyBdgtJT6cBGcy1wgDZMRWunc7JsqGNNc_rKtxnth2eIM8-J-HJ74WbgZFNonZ9ITpDORIa5GMttcWd715WELa6HGl-OzEiC98JAwyBaH6YnyQemhNgZmQGlo19FOpHqj_NxVcuoauAtVHN1xUOFcxjkBEBzytBu9qj_tEUlEK9bW00dqWP57O8WRElDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای پایگاه دریایی شهید محلاتی بوشهر قبل و بعد از حمله
🔴
تصویر توسط پهپاد Q4 تریتون امریکایی از فاصله ۶۰ کیلومتری گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/125654" target="_blank">📅 23:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
لاریجانی، کارشناس سیاسی صدا سیما: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/125653" target="_blank">📅 23:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a83f7f667.mp4?token=cdJvg5Kq9sIfTzr5WLX3rvLWDDgexY0YFGjZ1byTHsbRv8aEGldG6i1wjhmKakjMMNM48bmp7555y497a2rnqDiE8RdNYbPB1fha8qwItleJ7mstT7VAfpLjhncsLakHtclhBODSflGDnFYkc75FBPLyNCfQ6eDJySjRATyVdy3eP7B9Mhqm4C3vY0S5DVnwFcwewRo4T57ovXkTo2FLDGeIlVDl_xbQWIwGfDNv2Pk6oGdrGolhmkAN3MiCU-U4vt-FoyTVC3Xzvbhihbo0cEEwVnPJl8xYPhasFjSC8swDtTyLtOSuhMj2EUm9z1UUcey8pqOkgHMPr3HN_EFZF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a83f7f667.mp4?token=cdJvg5Kq9sIfTzr5WLX3rvLWDDgexY0YFGjZ1byTHsbRv8aEGldG6i1wjhmKakjMMNM48bmp7555y497a2rnqDiE8RdNYbPB1fha8qwItleJ7mstT7VAfpLjhncsLakHtclhBODSflGDnFYkc75FBPLyNCfQ6eDJySjRATyVdy3eP7B9Mhqm4C3vY0S5DVnwFcwewRo4T57ovXkTo2FLDGeIlVDl_xbQWIwGfDNv2Pk6oGdrGolhmkAN3MiCU-U4vt-FoyTVC3Xzvbhihbo0cEEwVnPJl8xYPhasFjSC8swDtTyLtOSuhMj2EUm9z1UUcey8pqOkgHMPr3HN_EFZF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آلبانیایی‌ها به یک اقامتگاه مجلل 5 میلیارد دلاری توسط شرکای کوشنر در جزیره سازان و تالاب‌های Vjosa-Narta اعتراض می‌کنند.
🔴
ششمین روز از تجمعات تحت عنوان "آلبانی فروشی نیست"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/125652" target="_blank">📅 23:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
باراک راوید خبرنگار اکسیوس: دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/125651" target="_blank">📅 23:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c6bed627.mp4?token=Tr6Tt2rFak15EjcY5PPasTb-Ooga1mIkhtmiYM1-F8cxT07B4_Dve6xsIvEy50Ji1tLyvNoa3yMWMOavroS6s6wTe-OTKhcgPMn1Zo7eVCj697PYLttdFHO2PJoMJ-jSZxRdBa0lWFRg34a8f-6RCcMd4VK8HaGqReMGm3eM8knV9vLNU0PgTUVlQPr5FLge-cgBrda0lFLL-l9n8Q-BoWUszugieoyvaNNCELbqH4Ft0ALH7kHiFt2UY_B9KKY1xzXzsQICh_-rInGFRJsGhYP11CNzwcZgFri_fwalSRHtdR3D0ZIUPxIOFYuMzLldmHf9tykkvrkBMIcY8qyAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c6bed627.mp4?token=Tr6Tt2rFak15EjcY5PPasTb-Ooga1mIkhtmiYM1-F8cxT07B4_Dve6xsIvEy50Ji1tLyvNoa3yMWMOavroS6s6wTe-OTKhcgPMn1Zo7eVCj697PYLttdFHO2PJoMJ-jSZxRdBa0lWFRg34a8f-6RCcMd4VK8HaGqReMGm3eM8knV9vLNU0PgTUVlQPr5FLge-cgBrda0lFLL-l9n8Q-BoWUszugieoyvaNNCELbqH4Ft0ALH7kHiFt2UY_B9KKY1xzXzsQICh_-rInGFRJsGhYP11CNzwcZgFri_fwalSRHtdR3D0ZIUPxIOFYuMzLldmHf9tykkvrkBMIcY8qyAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجیب اما واقعی
‼️
اندی هم مجوز کنسرت گرفت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/125650" target="_blank">📅 23:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/125649" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تابستانی گرم‌تر از حد معمول در راه کشور / هشدار آبی برای ۴ استان
🔴
رئیس سازمان هواشناسی: با وجود کاهش ۲ درجه‌ای دمای بهار امسال نسبت به سال گذشته، پیش‌بینی‌ها حاکی از تابستانی گرم‌تر از میانگین بلندمدت و عبور امواج گرمایی از مناطق مختلف کشور است. استان‌های تهران، مرکزی، همدان، مشهد و بخش‌هایی از دامنه جنوبی البرز با محدودیت منابع آب و شرایط نامناسب بارشی مواجه هستند و مدیریت مصرف آب باید با جدیت ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/125648" target="_blank">📅 23:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125647">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YwJikTgkXQhz78VJk3zguuGd-8-wBVNYTL-XzSJwfD7eblso7b1NG6-nx4IBYG62_ufT2fVPafyGnH6yLCUzepNFbMDj4TevSkQLyypcLpBN855_rFJuAHwspMH3RI0Sovt5mRwUNyL1Sfw88KyCYJlqkXYaSszMAZnt8wwCbf5ZzfeI8Z4eTlqPpiiRBGKCj6KYwqB0LQYYdG2FDnXWeqvufya3Y80suaZyi8H9ET8TQUVDU_PVSPoLUC-lCLTGnmophQ7Ims47ETFxlRNRx3dlDEH3PZa2xI3QRDVbNEzmGOjjB5npXL6spZ1eoVwsHa0Cub8CscwBuemluhiJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز تعدادی قایق تندرو نیروی دریایی سپاه در مناطق مختلف تنگه هرمز درحال گشت زنی بوده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/125647" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر کشور پاکستان: پیام‌ مهمی از سوی ژنرال عاصم منیر به تهران آورده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/125646" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTYWyG_86LF-9elYA4wWjjk2WQeuEjNSBazQrUeuaOuyr9CuMhA8GJca8K2MLtPwYZwoJGB2d17RZlj37n836yF4YN48l4GKGwcBk4p-OOkDujSWVdChQPYG34Vi-f4zHya5KBP0otmrfRbSZA-vv0NVIHdTRDcs5QSAhmAh1gDj-mfzXO7vcaVJyFeUNDoKrROfPfSSOiGFVc0RmZRdBm_aZsfAQJCOe7g0aXl6EKsTKhecajIwHrGZILc7D9HAI0yZTiBhJE2Zr0fkNbfcbtjmtUmTmGPlRrHr7-2t63Z3jO12hyYMYLXyD2ZsVmyP3hD3Au1-ZGvfWoTGfRBcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدف طاهریان مدعی شد بهمن ۱۴۰۳ به ایران بازگشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/125645" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتس: سربازان ارتش اسرائیل همچنان با شجاعت در لبنان علیه سازمان تروریستی حزب‌الله برای حذف تهدیدها، محافظت از جوامع شمالی و تضمین امنیت شهروندان اسرائیلی عمل می‌کنند.
🔴
هزینه سنگین و دردناک است، اما در کنار این، عزم و شجاعت سربازان ما برای تکمیل مأموریت قوی‌تر از هر چیزی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/125644" target="_blank">📅 23:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رئیس شورای شهر تهران: رایگان شدن حمل‌ونقل عمومی بدون تأمین منابع مالی به توسعه آن آسیب می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/125643" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125642">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم  @NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/125642" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125641">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NesGfoXKaPtEHTaIaUM__lQEdZ9aTZ6nc3k9LUTXJp4mjcgflCn50kOLDeNKQXJaSTk4tD4X2pmHNV8eUpVh23s8rIhhf2PBh8f18TU8HzceXn1sctv32nKcCPuUTx74UwjJGTFfs7StXPBURWO97hl1tWEULN6IhRHL10XiJ5QgqwhZzhvq8k-3n3FnV5i7HX6qhLUWW5iatRn29TChaEZLCS-P-QfoW6QD6Kj_Ft6YxSphZNl3rDHxz2UXDPw0QuVEAhZFLD46tIxe6lMcrsFlWxzK-6JBwLUxJkddTiKEXHrceNoL4Nati5A0tuIcMZYOd3fxGctwCB_VvIsapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/125641" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125640">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.  توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره. دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/125640" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ از اینکه حزب الله و اسرائیل حاظر به قبول آتش بس ترامپ نیست و به نبرد با همدیگر ادامه میدهند ناراحت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/125639" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125638">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ_O4w707sAaOtCzKwnTR9CfENsnoaAaAJre_YqrbTpk7V4MyiApArRE_Gk5JH8ZDIwfUoUkQhUZxoQA55jrgGyyU3hPhwUphL2kOGL7meCKMq7mZpM-JZWlqdEHqp4_H1-fnhOUBpWVFxh_l3TQzFEP5Y1np2Bz-1KSUZhyOAGwGgqnml8jO9xqo8J8p2sKihNJQekyZyNYPHowL1O73jLWFOEJ8haQ_BbUx0TJsL9YKLUvgFDp7aXOb_innlxH6pHTcTJ8qOLu9jDXMWZ3n5fRHGB8AedkNk9wNeugqkJEiOvRhMEVsJh6RHu_6iqC5pbGOadqAuuf8AlcErm_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مونا آذر، بازیگر ایرانی و مشهور هالیوود اعلام کرد که بزودی وارد ایران میشود تا از خاک ایران حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/125638" target="_blank">📅 22:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125637">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کانال ۱۲ عبری:  افزایش تعداد سربازان و افسران اسرائیلی کشته شده از زمان آتش‌بس در لبنان به ۱۶ نفر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/125637" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125636">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSGFwNx99RhQSHXO1Y2m4XHQI9JnwrAv7LWfsibpvFpLQssMuJYOqgSrP5F-3Po1YxvH6b-QrhYTtezCygt46NCKmp6dinh-RIqGUHfQSFEzF38gCXp7embT-h9jSvHaFeUoxneWy3yiFRXBGkz1ix1OYPz6oGW2Sc2jErcrHu6haWOw5e06PMghTd4vLoQAKtMoA2BFUkhLaCayDMKCPeX22doiYnyzUlO5NrmQxC4oY-kpTpxTEwp6UugDS3pe-HRo1rFENMMWeuczKmdX7tfHjUr_x1fpuFjvt-sI24t9_vDtrSIO1Mu2fxDMIHks9li8wV983itDBDM3CKURmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش صدا و سیمای جمهوری اسلامی، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان اعلام کرد که عملیات خنثی‌سازی و انفجار کنترل‌شده مهمات منفجر نشده باقی‌مانده از جنگ اخیر امروز، ششم ژوئن، در بندرعباس آغاز شد.
🔴
عملیات پاکسازی تا سه‌شنبه، دهم ژوئن ادامه خواهد داشت و در این مدت صدای انفجار در سراسر شهر شنیده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/125636" target="_blank">📅 22:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125635">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شاه چارلز سوم به همراه جمعی از اعضای ارشد خانواده سلطنتی بریتانیا، روز شنبه ۱۶ خردادماه در مراسم ازدواج شاهزاده پیتر فیلیپس، نوه ارشد ملکه الیزابت دوم، در جنوب غربی انگلستان شرکت کردند.
این مراسم خصوصی در کلیسای «All Saints» در منطقه کمبل برگزار شد و در آن، شاهدخت آن، مادر داماد، به همراه همسرش تیموتی لارنس حضور داشتند. همچنین  ویلیام وهسرش کیت شاهزاده و شاهزاده خانم ولز، ملکه کامیلا و دیگر اعضای خانواده سلطنتی از جمله شاهدان این مراسم بودند.
شاهزاده پیتر فیلیپس، که در حال حاضر در رتبه نوزدهم خط جانشینی تاج‌وتخت بریتانیا قرار دارد، در حوزه مدیریت ورزشی فعالیت می‌کند و نقشی رسمی در ساختار سلطنتی ندارد. همسر او، هریت اسپرلینگ، پرستار کودکان است. این ازدواج پس از پایان ازدواج قبلی فیلیپس در سال ۲۰۲۱ صورت گرفته است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/125635" target="_blank">📅 22:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
🔴
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله استیو ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/125634" target="_blank">📅 22:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=o2zxfLaiUyR4FKJQjlwRBlro5IEzcYyG85v06Nh6vo7YsvVNKVXNE9s9eheLXT2wAybuzzfns3nIdK_nmgxRFnnKKzHSP70NoMRBBJ7MVp31qDNj85cuUytvKWMYC45wX6koUTmYYesNKB6hqpubfeQWULSENT7sUJDpYtQG_qjIQk7_dX9Aon40RrftaZ0IUs42Aq_2CcjPjG2zBhMbA0ZKLiBZkDOOZou4Nt00yfaAikEiW9GazdOZs9TIRL9aGtarL1RzN5yp8RmeRZwXcbGQaJJaQKlveOCV1dBmCP87rTrH7jNpE0cZ-l7jceTHnbntPwe0IxEDOj5M0nkpsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=o2zxfLaiUyR4FKJQjlwRBlro5IEzcYyG85v06Nh6vo7YsvVNKVXNE9s9eheLXT2wAybuzzfns3nIdK_nmgxRFnnKKzHSP70NoMRBBJ7MVp31qDNj85cuUytvKWMYC45wX6koUTmYYesNKB6hqpubfeQWULSENT7sUJDpYtQG_qjIQk7_dX9Aon40RrftaZ0IUs42Aq_2CcjPjG2zBhMbA0ZKLiBZkDOOZou4Nt00yfaAikEiW9GazdOZs9TIRL9aGtarL1RzN5yp8RmeRZwXcbGQaJJaQKlveOCV1dBmCP87rTrH7jNpE0cZ-l7jceTHnbntPwe0IxEDOj5M0nkpsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویان مختاری شروع کرد به قرآن خوندن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/125633" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
