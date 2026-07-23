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
<img src="https://cdn4.telesco.pe/file/Hy-43fF5_pucDh4i9ICWmaPkamxKDXaXLw93TRIUgNvvnJGOa12lfVMVRB9YnbNgvvtgVkKJJnc0ps-5s5590XN2PH1ZKKwAPG0MjUgncrs4MQpI28n8kkienMK66CGqKCJgiLPZXRXwBPSJDCwoVA_eOc4kO7Uw4foU8Pc7e-GVWEpSSOTv_SOhM_31KoxC7jpNuL90JENOCYlaaGZVTbcGZGrMurl44m1coZj-sFPJb5D62WaWBc54fp7GxUWhjsUvOwt71Rkv1VW8g1nbSv9pMdX5pgj-TY8HYMXCV4uHBc854Dxv1_-zAqyX75m317e1FSEgF4hE_tjk-cXhqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 05:29:56</div>
<hr>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHrORIESa6rG53foPM3v5FOSrx642mKGPXKRdR6JUHOYRejAlam9EDCa5X5UWlJDpFS5DgNLdeAx_jwr4El9z4dOEbDkuggvEli8MOkXnzTuDrb4sjNFlCOTWtZuOkUv6m5hTGcBr4BO49PBBkVvQt_7_jvYxG68Ag0lIfn7tMVQNToe_adaYmwm4jUwFHTJ2kekSgVlGBXWqUHKnXgPxnJ4PyrUz7aD43bfWhHq_tqrmdrEotrWkA6MvFBh98SWHbrrUFqWYIYy_KLbrj6oB4HAb1fdFS7TRyQy_aPIoDNcvkEkfeIdOxoXd5TYES9OYu3EoQNuR5a_OXNcgCE6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/136858" target="_blank">📅 02:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136857">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/136857" target="_blank">📅 02:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/136856" target="_blank">📅 02:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136855">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
حملات امشب خیلی ضعیف و کم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/136855" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/136854" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده لایحه سیاست دفاعی به ارزش ۱.۱۵ تریلیون دلار را با ۲۱۶ رای موافق در برابر ۲۱۲ رای مخالف تصویب کرد که شامل ۶۰ میلیارد دلار هزینه نظامی اضافی است و انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ علیه ایران را پوشش دهد.
🔴
این اقدام که تنها شش دموکرات به آن رای موافق دادند و هفت جمهوری‌خواه به آن رای مخالف دادند، اکنون به سنا ارجاع می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/136853" target="_blank">📅 01:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فووووووووووووووووری/مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران رو تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/136852" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k15w0dFNymx4oSsw6NAdeqxiPMYxpFte4YarXPj8Pi4jtd-tjloEfiM6ZAltgzH3syl6WETUZ2iN81FG8cunKUpQ7NxTvIRO_utsXSe9EH1ZXuAOBLyshJffrhuw2CmAkuCm5tkBX2-4AsaBa2pgiwx_rYMWVIOZ-yCKLt2QNVOx8WMRjaltgBRVlR7sVq31IenmBid_dCXf2IpAKsaNElmLbPtyO2aKG5jY8lN8A0YX7ruCR99Yf72Lg_TIuqeqgqbS2RjJvyKMrSf0FXfl7Cohh3SN7aVyDvdJ-QaxinWkuS7OF6hMQBEcYJqqg6B-CH2o-nzcr9e_EPXpFgfA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: امروز ساعت ۵:۳۰ بعد از ظهر به وقت شرقی، نیروهای ایالات متحده طبق دستور فرمانده کل قوا، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این مأموریت ادامه خواهد یافت تا توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای را بیشتر تضعیف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136851" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
العربیه: ارتش پاکستان هشدار داده است که در صورت هرگونه اقدام حوثی‌ها علیه کشتی‌های پاکستانی، پاسخ لازم را با استفاده از همه گزینه‌ها، از جمله نیروی نظامی، خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/136850" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کانالای ایتا وقتی آژیر کویت فعال میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/136849" target="_blank">📅 01:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/136848" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الان به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136847" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فرماندار بوشهر: یک نقطه در مرکز استان مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/136846" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یمن: ۲ نفت‌کش عربستان که سعی در شکستن محاصره داشتند را با موشک و پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/136845" target="_blank">📅 01:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سیریک رو بازم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136844" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/ماهشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/136843" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پاکستان به حوثی‌ها هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/136842" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
️12 فروند جت جنگنده یوروفایتر تایفون ارتش سلطنتی بریتانیا جهت حفاظت از حریم هوایی متحد خود، اردن وارد این کشور شدند .
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/136841" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlsRgfp7nb7rvnH1KrCyebXk6tHx82cihbF5oPLIL4jjFj_AgXNvW_rt50V4ssSPlj1U4jpgUodsnIFN_BUvcRW_CvyAUW_BfV8PltfUflIswFa52aOm5YSh1R5C4XagXjD9HAiXHimsqRKD2yTDDAfJgIyKTsj-YBeTo9c49R2SajgG56UzINpZDOhLJNzF1Lyp-2AxiLtcI9BSKYOIHXvlHw95yR2c6KPXt5jea8teJiMy8hdgbLAzs6bvMpXSh5VgeuYlfm6QiS_PwQyOdC25OPoWd5IcJZaDt7We_f8xwVXIrYjF4aVWWNiSjT_62q4p19Ufg-uJD4oa98THfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان بین‌المللی امنیت کشتی‌ها (UKMTO) گزارش داد که یک نفت‌کش در فاصله ۷۰ مایل دریایی جنوب غربی الشقیق، عربستان سعودی، توسط یک پرتابه هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/136840" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اینترنت ضعیف شده؟
👍
👎</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136838" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/136837" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccF_57Syk982El95oFK696QoytwM178zIajuwqkbDLL9NutZRuPQ0eXRO3eNGMkBqNWzK__Xn32K-dzGeyrKyGG-jQiWCxKjuZGKy7j-8YADcFX49nNuAF8-sB-vzoo63IZRJxeqkVULZZ8GTGZR7EjDI5q4UW-8Ff78lXeKM2Y3KcKF_cgQc8UhWpvQhODwE0190uoCBMqwSqWJDwPoNxbG7lTWllzcj7uNJ4U3hqB63sBx60LaUh2cqX1_y6iGSc7jwPiukuZLX54dzv04JPjjJ1lU5YNh9CQNQyU2ZtyI9AkzPzMj_SX0rAEGJm6sTAuXafcI0U5GxYXqe386aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان ایران همانند خودش در انزوای کامل
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136836" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی در نزدیکی عربستان سعودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136835" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پایگاه موشکی چمران رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136834" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یه سوله انبار آسفالت تو اطراف رامشیر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/136833" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پایگاه دریایی سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/136832" target="_blank">📅 00:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
لشکر ۷ زرهی ولیعصر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/136831" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وال استریت ژورنال:
‏به صورت اضطراری نیروهای ویژه، جنگنده‌ها و بمب‌افکن‌های ارتش ایالات متحده در حال اعزام گسترده به خاورمیانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136830" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚠️
فقط زیر ۱۸سال ممنوع
⚠️
◀️
مشاهده فوری تصاویر</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136829" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صداسیما: صدای انفجارهای بسیار بزرگی در اهواز شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/136828" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ : اون‌ها هنوز برای توافق آماده نیستن، ولی خیلی زود آماده می‌شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/136826" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ca1873d4.mp4?token=pwLq7l-R7Z0xsFBk-uRHQKpI57gNEHqmvhtWkgZebzOrFaKDJkopa104C5YGjEKuED1582-c13unh5QzPNmrB7qkjbkIGzaaGAo3MVSmVChzONZYCwXKGm9bXh570jYJo9ulGrL8vAHhPtIOON4fHVDmrRaRtqe7o7t5-eCfFZJhH6gjpnSQxBTSxYm0qLJwVsMnNPkCU0pzjqE4QKG24uMvg8plievwO22L-JknndCWwFPNvQ7dJFF82XGMqSv1nx1gO3SvShn4vaxMAMqBt18-fWqqoVM0qr0NY2hRsejlWlodbEJhI35bnx4i5LDjc5lYYs6Z2786dn2DqqfTqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ca1873d4.mp4?token=pwLq7l-R7Z0xsFBk-uRHQKpI57gNEHqmvhtWkgZebzOrFaKDJkopa104C5YGjEKuED1582-c13unh5QzPNmrB7qkjbkIGzaaGAo3MVSmVChzONZYCwXKGm9bXh570jYJo9ulGrL8vAHhPtIOON4fHVDmrRaRtqe7o7t5-eCfFZJhH6gjpnSQxBTSxYm0qLJwVsMnNPkCU0pzjqE4QKG24uMvg8plievwO22L-JknndCWwFPNvQ7dJFF82XGMqSv1nx1gO3SvShn4vaxMAMqBt18-fWqqoVM0qr0NY2hRsejlWlodbEJhI35bnx4i5LDjc5lYYs6Z2786dn2DqqfTqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری مشاور قالیباف و الله کرم(نماینده طالبان) در پخش زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/136825" target="_blank">📅 00:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حملات امشب آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/136824" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گزارش انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/136823" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136822" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVZ9w2WH3iiVhU45OkSUBAhuOQ4U-Q6A2dRijFYe3DRmCIQOpSv7IGJ0jkFN62yO-e4fqmDt7x-9ZSX-pfMQdi2ROq2oPtO2_E73wA6rsXTX5zAKgYTHPoqxgHYr75mTw5co7Z79tIvEH_QGvCgfmjZsUxaarO6ZFezeNcnF3WAuV-1C9W2kM0kPOoutwlXcP9H9_Fp7baLOEmWKghOY6IdPIF6bReXHi1XoZIR-HFM6QmoHzLQH6KcR4fgs5XGiIEi_iCrYWi3g-RWisslQ-ZHoZ1iN_PM9YCkHj7L0Cn48iWCPCibwGqZ0koofA4Rlov-PmKXHLKQoyfyq-LsAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/136821" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔴
این اقدام پس از تشدید دوباره جنگ [علیه] ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136820" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/136819" target="_blank">📅 00:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز: حداقل دو مرکز سازمان سیا در ماه مارس توسط ایران مورد حمله قرار گرفتند
🔴
از جمله پایگاه سازمان سیا واقع در سفارت آمریکا در ریاض و یک مرکز دیگر در شرق عراق
🔴
یک ارزیابی داخلی سازمان‌های اطلاعاتی غربی به این نتیجه رسید که احتمالاً روسیه در این حملات نقش داشته است. دو مقام غربی که در جریان این اطلاعات قرار داشتند، گفتند که حمله به سفارت آمریکا در ریاض با استفاده از دو پهپاد شاهد که فناوری روسی در آنها به کار رفته بود، انجام شد.
🔴
برخی از مقامات معتقدند که روسیه همچنین به ایران کمک کرده تا دقت پهپادهای شاهد-136 خود را با ارائه سیستم ناوبری ماهواره‌ای کومتا-ام بهبود بخشد. کارشناسان می‌گویند که این سیستم به طور قابل توجهی دقیق‌تر و دشوارتر از سیستم داخلی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136818" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/136817" target="_blank">📅 00:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
در پی دستور رئیس‌جمهور برق صنایع با هدف جلوگیری از توقف تولید، حفظ اشتغال و پیشگیری از بیکاری در مرداد و شهریور قطع نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/136816" target="_blank">📅 00:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZhHZijUiNF4zk3actZ0R-CojmZeM4eYJ-sO_qoAT_PzipKsGZq-mZfqaiEXZwvrRtoJXWmqwcA26V6BRdsgxs2nWnIrlT0qFo_rzHXs7tzw9RM0KXyRRh-hnpgxud93HbKSdmstj-t8aFK8kMjlrTddYNreIxgMsfiw-ysXkbcKgrEQ5_71pMgnK48cTGxlmvLTleA5cCIpdiZyOvdM5tQ3KKyUNTkCRDPdHRVTnDOzwxFVG3I1MCKC2R8OoKq-nEe1zrbBZHcifjWudH0_dGvOB0pzVWkh4ndgLLKsvqRJNN2nUAlxPKOJnVl5LG8Qq6kI1tU3IngRb1r9Nz4vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: منابعی در ایران می‌گویند که پرونده کوه کلنگ (کوه تبر) طبق روایت اسرائیلی و موساد در مورد این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن، مدیریت می‌شود.
🔴
برخی منابع می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/136815" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مقام کاخ سفید: امکان دستیابی به توافق با ایران وجود دارد
🔴
استیون میلر، معاون رئیس دفتر کاخ سفید در امور سیاست‌گذاری در گفت‌وگو با شبکه فاکس نیوز ادعا کرد که ترامپ برای تحقق هدف واشنگتن مبنی بر پایان دادن به «تهدید هسته‌ای ایران»، تمام گزینه‌های لازم را بررسی و در صورت نیاز دنبال خواهد کرد.
🔴
معاون رئیس دفتر در امور سیاست‌گذاری کاخ سفید مدعی شد که جمهوری اسلامی ایران در طول ۴۷ سال گذشته «با مصونیت کامل» دست به «اقدامات خشونت‌آمیز و کشتن آمریکایی‌ها» و حمایت از گروههای مقاومت در منطقه و جهان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/136814" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔴
این اقدام پس از تشدید دوباره جنگ [علیه] ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/136813" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کانال۱۲ عبری: پاکستان و قطر به طور فعال در تلاش هستند تا آمریکا و ایران را مجدداً به میز مذاکره بازگردانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/136812" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded6599216.mp4?token=K5vMOV1RPBJuMR1TbCMkDu09wqgD4WjO_1ki3ESAH_tzc6B8ntoVoLOIel_hT5sHcM_cxPOb14KPDAeWrUQ4g_nwg6PJithsOr_NzHlX7PbEs53d12sjCJOOnQqXMTXopwFvHPos0uUrWB9ZSIxs9NBDdr1r8YoiG5WljmSzlIdrsJO5G22ibXRad93I7-lgogwxPBSizWeWK-foP6JtsbA88xD-pUif1PWVG7Nm78uag3cGluueYDGb-PdrjBLp1-NUHbHKIWWj404XTyRW9u_VnYDCNqwcm5CbqnktLJqDm4Mhi0mH-H2yParjARCS5SLEX2AQUT6Dvl_x4kUas3C5sJw1ZEcubr422WHo8DN4wmPQ6N_QgXJW2ME6n60f0sVU2GjRSR_Sa0jIgPGWqGt3FzunVtzOJZ8BkaOkniMU-uv5Y6VfqfHCilZAxvxtCxV-4X_bRL7n-KdcYeveg99qQzxO5ZJaWXay-HhbkZ17y_jkkK5LTeutjkQRZH4jPZkJ0tkMtVzHcDHRwxeSs2-LJs26rjjcm096GrDNTU1bC7GdjF63p-EyHK1kiiVRaqPbOoHU3WegpDqwhdzLCiHClOnbe2QqxD9EpzEdKpnyswHC4KAOqeu3o96j-0_Ym5ZDzg2Li5aGyKmPfhc9iOj-Y_rLzl6YSuC3BOFtbvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded6599216.mp4?token=K5vMOV1RPBJuMR1TbCMkDu09wqgD4WjO_1ki3ESAH_tzc6B8ntoVoLOIel_hT5sHcM_cxPOb14KPDAeWrUQ4g_nwg6PJithsOr_NzHlX7PbEs53d12sjCJOOnQqXMTXopwFvHPos0uUrWB9ZSIxs9NBDdr1r8YoiG5WljmSzlIdrsJO5G22ibXRad93I7-lgogwxPBSizWeWK-foP6JtsbA88xD-pUif1PWVG7Nm78uag3cGluueYDGb-PdrjBLp1-NUHbHKIWWj404XTyRW9u_VnYDCNqwcm5CbqnktLJqDm4Mhi0mH-H2yParjARCS5SLEX2AQUT6Dvl_x4kUas3C5sJw1ZEcubr422WHo8DN4wmPQ6N_QgXJW2ME6n60f0sVU2GjRSR_Sa0jIgPGWqGt3FzunVtzOJZ8BkaOkniMU-uv5Y6VfqfHCilZAxvxtCxV-4X_bRL7n-KdcYeveg99qQzxO5ZJaWXay-HhbkZ17y_jkkK5LTeutjkQRZH4jPZkJ0tkMtVzHcDHRwxeSs2-LJs26rjjcm096GrDNTU1bC7GdjF63p-EyHK1kiiVRaqPbOoHU3WegpDqwhdzLCiHClOnbe2QqxD9EpzEdKpnyswHC4KAOqeu3o96j-0_Ym5ZDzg2Li5aGyKmPfhc9iOj-Y_rLzl6YSuC3BOFtbvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمونیست‌ها می‌خواهند مجسمهٔ راشمور را تخریب کنند. آن‌ها قبلاً هم تلاش کرده بودند تا این مجسمه را تخریب کنند.
🔴
آن‌ها می‌خواهند آن را منفجر کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136811" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ :  آنها از کلمه‌ای استفاده کردند – اولین باری که آن را شنیدم – که توسط دموکرات‌ها ساخته شده بود: «دسترسی‌پذیری».
🔴
این کشور در حال پیشرفت و تحرک است.
🔴
سرمایه‌داری آمریکایی همیشه به درستی اجرا نمی‌شود، اما وقتی به درستی اجرا شود، هیچ چیز مانند آن نیست.
🔴
گروه‌های چپ‌گرا و رادیکال در تلاش هستند تا آینده فرزندان ما را با فاجعه‌ای به نام کمونیسم نابود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136810" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=Jnjfl0p6FSjP55G9PICtzN7I6FEDRUJyxhEPWVsLC2q51Neko1miogXCjJ3VJQaFQyLXrV63XWDH6U0LzXDL2L_H4x3koFdKY7KxckgV9KPbwC994-BxZr2NhglzQMwO4npMaHfBMJK-W0EhPC17Nd_Rp_nhSdxfFFKPIAOVQrQh-D3MwvqGD3i_gKKEhCraJBP_0GPfQuPJq8kir8iDVJ4BYMqBn5YUlOyOggq5RZqHD4r1ip-Tivw7N0-5bSMjaE0uJG-vHneh2P_yTilzUbKRU_gBU-NcqSsCObFPdrygo0z8t52LAVQTIxpxSb_rgazIOHVAOmVxTnC2aoXSXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=Jnjfl0p6FSjP55G9PICtzN7I6FEDRUJyxhEPWVsLC2q51Neko1miogXCjJ3VJQaFQyLXrV63XWDH6U0LzXDL2L_H4x3koFdKY7KxckgV9KPbwC994-BxZr2NhglzQMwO4npMaHfBMJK-W0EhPC17Nd_Rp_nhSdxfFFKPIAOVQrQh-D3MwvqGD3i_gKKEhCraJBP_0GPfQuPJq8kir8iDVJ4BYMqBn5YUlOyOggq5RZqHD4r1ip-Tivw7N0-5bSMjaE0uJG-vHneh2P_yTilzUbKRU_gBU-NcqSsCObFPdrygo0z8t52LAVQTIxpxSb_rgazIOHVAOmVxTnC2aoXSXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران و تنگه هرمز گفت:
ما به تنگه‌ها نیازی نداریم. ما به هیچ‌چیز از این نوع نیاز نداریم.
🔴
اما این کار را انجام می‌دهیم، چون مجبوریم انجامش دهیم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/136809" target="_blank">📅 23:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=VJuw-jV2gEUejTH3xxPPmE1PPUycqkG35yJd7B_a4maEQ1phL117g0Y0QEtEZuXZ1rBl0JLbPpLafgIPTFNgGJpxrYy9sVZL5cS1KNdgGEDUa-PsqnAazSCl4rS6nAIhSZT82h0Vf2r59_2tMqYxa3A_yzjButLCyYJDem8RIx3LxEW8VUS-X_lOi8IxwjSUbfldXJz2M7Oygup3rGcBs-6-Z4QBmQZqt1kI2O4FGSBOdByMFOkCX1nEJO1oiAN931vqiZDdilkJAzKMOo0zmUSCzPjnUZErL2Prgjnlef-M-1Qb43xmtq4SddRDaSlUDe1GRFvQSQ2J5myZJm8B8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=VJuw-jV2gEUejTH3xxPPmE1PPUycqkG35yJd7B_a4maEQ1phL117g0Y0QEtEZuXZ1rBl0JLbPpLafgIPTFNgGJpxrYy9sVZL5cS1KNdgGEDUa-PsqnAazSCl4rS6nAIhSZT82h0Vf2r59_2tMqYxa3A_yzjButLCyYJDem8RIx3LxEW8VUS-X_lOi8IxwjSUbfldXJz2M7Oygup3rGcBs-6-Z4QBmQZqt1kI2O4FGSBOdByMFOkCX1nEJO1oiAN931vqiZDdilkJAzKMOo0zmUSCzPjnUZErL2Prgjnlef-M-1Qb43xmtq4SddRDaSlUDe1GRFvQSQ2J5myZJm8B8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: ما یک مرکز نظامی فوق‌العاده در کاخ سفید در حال ساخت هستیم.
🔴
این یک سالن رقص است، اما همچنین یک مرکز نظامی بزرگ نیز هست. یک پایگاه پهپاد در بالا و چیزهای فوق‌العاده‌ای در زیر آن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136808" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Y4NAqrJx7KAzaBalIwqInhv7xwz9THsHNbMqsLsEK7eFTTpldAnUqEhZlzoexRHrMc8_n9-YOJRNHA2gF6LsvK_YTuC1QNc9sMQGP1GmJ98niihyOygxzqL5YJP03NTXVlLNR-0IZ33tvR4fpc2EP2pVKXtkuNJHWTkEDvBD7iRiBCh_czDaA4GK6X-_RfuRuK_b4aikmMT9AQEcTD92c3Onm1BZk-r0-KqOj52Y2o7T0F66cT7W23FAXyxL7jxMH2LdzUuknRePFaRtFXVEsIdBitFdbWVclMULa8eyCxU7OLHMlhfY8gfk1grlVj3tNGPcXezzQthz-PojfdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/136807" target="_blank">📅 23:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سفرای پاکستان، عربستان و چین در. ایران در محل سفارت اسلام‌آباد در تهران دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/136806" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=dRGbkp4QmzxGCN0qpV18fJISZVOHuu-SFHkIdgv47lyTybhaly-SFGhfoNl2UYkVnCiij6J8xgJJRGF3DiCkqqsK5tEP5z8wHnxKGpBPKjAGvegCckptUefHCE562B17mNrm05w4SAJOo3w0b_kvDIp54gDvYhJOSLeeIIkgfMX9By3KZ3sWRn0b1U3iG56jpYMNRFo1ZM467yKCbsdAWroN12FiwAcdVXOpNYj14ZA0nN1zO-tp74zGKOKO9ppg6N255ecR-eAdABwJTCbWYWxWdUG4Z6QN9esbGc6UbwYaHhmLd6BXBwo_4YHT57twkXfcpsFh6dRYBLGp_TAODCDq7aJMK4WpFMF6UfeHnj-BWo3rk8yGowUs9SyR23PbpHcSwfPqoM8GjCLcjFjZbVB4yREQvdxTGUuLtGZ5N5go3S9tgvnZOFVax0jg-4Ff-RM7O2sRaxZ8zuB8J-oSRsKDBr5NPP0KY6-IQmAV1dDasAHPftKo6pdPcgFVAvgKVYfh2Byuz229luSZ6YvHsrpPHAoSCdQsJkLY0JJcPMs0oced3M5yOF1PW0Rhak3vfKUVDD1t6mcJs5KYeKBNOtp532llzWmnr0UjHrX5Nt6KJ2LFktnoeIocSB4RZBGEN4dGXeViO67R_BpRKlZUTScqja0iRXgk4nbehTpaF28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=dRGbkp4QmzxGCN0qpV18fJISZVOHuu-SFHkIdgv47lyTybhaly-SFGhfoNl2UYkVnCiij6J8xgJJRGF3DiCkqqsK5tEP5z8wHnxKGpBPKjAGvegCckptUefHCE562B17mNrm05w4SAJOo3w0b_kvDIp54gDvYhJOSLeeIIkgfMX9By3KZ3sWRn0b1U3iG56jpYMNRFo1ZM467yKCbsdAWroN12FiwAcdVXOpNYj14ZA0nN1zO-tp74zGKOKO9ppg6N255ecR-eAdABwJTCbWYWxWdUG4Z6QN9esbGc6UbwYaHhmLd6BXBwo_4YHT57twkXfcpsFh6dRYBLGp_TAODCDq7aJMK4WpFMF6UfeHnj-BWo3rk8yGowUs9SyR23PbpHcSwfPqoM8GjCLcjFjZbVB4yREQvdxTGUuLtGZ5N5go3S9tgvnZOFVax0jg-4Ff-RM7O2sRaxZ8zuB8J-oSRsKDBr5NPP0KY6-IQmAV1dDasAHPftKo6pdPcgFVAvgKVYfh2Byuz229luSZ6YvHsrpPHAoSCdQsJkLY0JJcPMs0oced3M5yOF1PW0Rhak3vfKUVDD1t6mcJs5KYeKBNOtp532llzWmnr0UjHrX5Nt6KJ2LFktnoeIocSB4RZBGEN4dGXeViO67R_BpRKlZUTScqja0iRXgk4nbehTpaF28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
من این را یک درگیری کوچک می‌دانم. ما یک درگیری کوچک با جمهوری اسلامی ایران داریم.
🔴
آنها به شدت تحت فشار قرار گرفته‌اند و می‌خواهند به توافقی برسند، اما من می‌گویم که آنها هنوز برای توافق آماده نیستند.
🔴
آنها هنوز برای توافق آماده نیستند. آنها به زودی آماده خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/136805" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a974815af.mp4?token=jCzkSW0-OJgeBXTk1sUPbPwhmQMOB0UsJA6XQqe2KtrvKYKAJ7pcbKVcW-mbY3mlTv0u2vy15utfY0Et5v77QloHNtrnheGjO_kl0QOKF73aIz0p0NPbRjeB7ob-MB_NLk2k2BW6F3C2GLMVhedxgoEgXXjTJyHokLRPbZX_amKYXAPNPNU-RZCbwLlfycDna-7EUXGMT8earkgdoRi5cJy5_5zulGLfvb1a-MEHICVUhwGD3poBB2rIZ7k8-BsVizwcWQ3TkammopchRMVu27fQgnxvhIZTzHvUL4oOtY-fTt7vtp82Kt4PEk7yt2yfYQa9tQlTgSVMPuh8goxEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a974815af.mp4?token=jCzkSW0-OJgeBXTk1sUPbPwhmQMOB0UsJA6XQqe2KtrvKYKAJ7pcbKVcW-mbY3mlTv0u2vy15utfY0Et5v77QloHNtrnheGjO_kl0QOKF73aIz0p0NPbRjeB7ob-MB_NLk2k2BW6F3C2GLMVhedxgoEgXXjTJyHokLRPbZX_amKYXAPNPNU-RZCbwLlfycDna-7EUXGMT8earkgdoRi5cJy5_5zulGLfvb1a-MEHICVUhwGD3poBB2rIZ7k8-BsVizwcWQ3TkammopchRMVu27fQgnxvhIZTzHvUL4oOtY-fTt7vtp82Kt4PEk7yt2yfYQa9tQlTgSVMPuh8goxEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در سخنرانی خود در جورجیا گفت: همه‌جا موضوع تراجنسیتی‌ها مطرح شده بود.
🔴
مردانی که در مسابقات ورزشی زنان شرکت می‌کردند، همه‌جا را به‌هم ریخته بودند.
🔴
تمام دنیا به ما می‌خندید.
ما در سراسر جهان به یک مایه تمسخر تبدیل شده بودیم، اما دیگر این‌طور نیست؛ دیگر به ما نمی‌خندند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/136803" target="_blank">📅 23:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=HP7HZ8Rydb2hm5kBuuMVJls_vM004sNal_Unfr2KyquI0BtltLqn_L6rxTUiSBp-T86A0udUH3lITzJaNR4HYdKWZ00i4HVrSu8gE4s35K9uqq2dotEsuTQY-lXeWs6CHxvtn5pKAsSn47CXp6V0EZ6S9swT9D_ra_81qw_vgOIUbHDy0S7hgsvxr5NgED3iBF6tueBBEvG8PBvQewQKxZPEX5XBNL-Sc9WuWE_lkWvLXsvCuYaW3knfOhjJBnzuysByihurKCY7YatJ7zgoHaIqMEM9NExDbV5cCgfqidqUQSxVdc-Is0Wkm_dxb7MD0HLI3N4x4qRqTS1UOGPLgzuQjOr8TULxMyvoOwshB7JCNzcz2nKoCxYrGng3NYKGcCTKi-nRhoFIUe9TTWeBK_2luyQGDOozY4bY1afTJXABFgOY7jCu4QzHMf4C_BFGBhHW9JIiJX8tEOFFY7r4rV2p95PA92RkzjGg8mNt7iLLt4O5mBIhN7OHA9k9AvYv0mjCjyi1xHRxdbKZUCVoO30BKFpYZA1zHd6WB5wOuoC6l-MtH92e2Gsl8cr2_zHh89aj72gYN27AE5c10j36F3e5slC__fzOIxstK4Lqw0NKg7YOSTjZN6VMy0nNESZP2qPQfEDgmIbhTADzwsKCVi1NUv2X78qkiWd49vqSngU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=HP7HZ8Rydb2hm5kBuuMVJls_vM004sNal_Unfr2KyquI0BtltLqn_L6rxTUiSBp-T86A0udUH3lITzJaNR4HYdKWZ00i4HVrSu8gE4s35K9uqq2dotEsuTQY-lXeWs6CHxvtn5pKAsSn47CXp6V0EZ6S9swT9D_ra_81qw_vgOIUbHDy0S7hgsvxr5NgED3iBF6tueBBEvG8PBvQewQKxZPEX5XBNL-Sc9WuWE_lkWvLXsvCuYaW3knfOhjJBnzuysByihurKCY7YatJ7zgoHaIqMEM9NExDbV5cCgfqidqUQSxVdc-Is0Wkm_dxb7MD0HLI3N4x4qRqTS1UOGPLgzuQjOr8TULxMyvoOwshB7JCNzcz2nKoCxYrGng3NYKGcCTKi-nRhoFIUe9TTWeBK_2luyQGDOozY4bY1afTJXABFgOY7jCu4QzHMf4C_BFGBhHW9JIiJX8tEOFFY7r4rV2p95PA92RkzjGg8mNt7iLLt4O5mBIhN7OHA9k9AvYv0mjCjyi1xHRxdbKZUCVoO30BKFpYZA1zHd6WB5wOuoC6l-MtH92e2Gsl8cr2_zHh89aj72gYN27AE5c10j36F3e5slC__fzOIxstK4Lqw0NKg7YOSTjZN6VMy0nNESZP2qPQfEDgmIbhTADzwsKCVi1NUv2X78qkiWd49vqSngU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ایالت جورجیا با شوخی گفت:
من اینجا هستم تا نامزدی خودم را اعلام کنم...
🔴
شوخی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/136801" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=GZimQBDuJyy91RV6B6msei2SJ66N8ywOE2IKGWWNv7TpgWSWr8_NvZYWmHrbryfn0wyMO7IwTl2tM_st08SWelVlKZqUmuOArTbR4BjfqYBvBQq9oXRJy32xxFBwUvMPbOJnJ0mFje31dcW3khYJTPR6Oln46r8sgmdkSP_Q0i_tsd_h7BoxQkrchXTw4lc3H6_WUhQIhPe1RySTi8PBexMB_FjU36JcvTbBBMitQoa8g6005BvDZBK-XJhuCcF1wYaA1Ztd33UWMh03BoGnscp2z9T8mihH3AvUUnzUJtrnVuc5ShhwTxnJTrOUlMc5GcTzzx9bZnT0tYAL_3KRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=GZimQBDuJyy91RV6B6msei2SJ66N8ywOE2IKGWWNv7TpgWSWr8_NvZYWmHrbryfn0wyMO7IwTl2tM_st08SWelVlKZqUmuOArTbR4BjfqYBvBQq9oXRJy32xxFBwUvMPbOJnJ0mFje31dcW3khYJTPR6Oln46r8sgmdkSP_Q0i_tsd_h7BoxQkrchXTw4lc3H6_WUhQIhPe1RySTi8PBexMB_FjU36JcvTbBBMitQoa8g6005BvDZBK-XJhuCcF1wYaA1Ztd33UWMh03BoGnscp2z9T8mihH3AvUUnzUJtrnVuc5ShhwTxnJTrOUlMc5GcTzzx9bZnT0tYAL_3KRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درمورد قاچاق مواد مخدر:
به نظر من، افرادی که تلاش می‌کنند مواد مخدر را از طریق دریا وارد کنند، شجاع‌ترین افراد تاریخ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/136800" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ:
ما به تنگه هرمز نیاز نداریم و اگر هم اکنون آنجا هستیم چون مجبوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/136799" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXQzb_fiLbihPfCr6V6hHcIZDVrlTo7Tp5MaP1XZHsbgdqiR4qxrGDzR4WWduoHIN8HcKoh6kLZ76uilJcqQPa0sIWq5J3t0Xm-NnGjD14MnNEPVVGC6LFG7bJ7nFlu19CqUCgHMVpm4uB1SNaNy1N2xnAW9YaHJSjMpq5-YCjnPnixeTYFt7Ux8luj9RnhMH1zVNpXega8KmfdS6gTZeQvwmDbyo8p56ql3XIf7aAkMnZO8LB62SQWax8UsDIMeLUFSURpDyaDBVAIwjMO2SFMGFC2uzZSBuS5_R6Vb8tCd4cGZF69XI1jwzNObj5PQyh8GC1ET5BNzWX4Vi2K8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفعه قبلی روباه پیر(بریتانیا) ۱۵ ساعت قبل جنگ این هشدارو داد:
🔴
۲۷ فوریه ساعت ۱۸ هشدار
🔴
۲۸ فوریه ساعت ۹ جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/136798" target="_blank">📅 23:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyNMLHLhlZeQbBZUApaDCXyUbVRZfmjx_KSZBEetMC28Q-hzslET7-qhzcaQF7GhycQ6NVXfilGbClaYGUe1jo5xK8V--0jB_-0bW23SMkZxpsR11S7D5Tq_vtQhtc4xfkIOLB0yrmSvXGIiARRhE3gzw2cU4Qr9NppEosy_B7Mw4Lluoqy7wLSma9zxS4rocv7U9ATrYZTe5FE4ezmUfpexRp1z51_RNWfAw_EEypLrVQTMtkPGkosb1I1dVns0xHR3LAB5tSnoC1h9mlXLl9jTEewxN3yh3rgwPLlUADAM4peiU3V3R_ZSPk2nHVroYbcLOj_oOaWQmHkDAW8dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیر نویس عجیب صداوسیما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/136797" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
فوووووری/برای اولین بار در 2ماه گذشته 4 هواپیمای آواکس درحال پرواز بر فراز خاورمیانه هستند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/136796" target="_blank">📅 23:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/136795" target="_blank">📅 23:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه :
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/136794" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/136793" target="_blank">📅 22:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پرواز جنگنده بر فراز کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/136792" target="_blank">📅 22:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b372ec2c.mp4?token=GWxjtqFs-qmtvAdGWH1TlCr5vyEYKwYjzbLlFRsJRNGWDUgYjpT4qhsoJNzDljX1pQh3v3IpF3N0rsKM4sNa54Mv7QAXegrMFhFhA9DNtOLU1lMxQr0Pe2dE047ki8sTmI6_7HOD-Mk4UHtEppeLkud7_o1NvZHXm-CA4Uj2Z-Wbt1VahDFZ1WINWQnv3_WqZ5NUzRPDwH4KBpjY7PRLmd72PxBS5y29Mh2bUp8_jmsgv7tINgtShV5N8NYcdpuHhbUKBibxBrVTB1WcV2KT481NGYBQV5oZAN63Uf0FMbhd9Ka7B_0ThCsuWCZoybynWyu6RRWU3WWpfocFgvIyU2BFiqOZK9Qj-T8W2aoHllqPTYnLMXEAVRo5FhIhx9pJgezQ8TS1QX1lbL1YUqM5gWReuK-dlEpgzDibd6tdsTBI4zDYFOAVcrZRoeAovKO6mpxHaobvxZeAw7jMW4_DjOzldZVxkDwWDCB27nYgZ-zBwTW0GwLMjWlmBGnhRwHFityQypb9vFCdC560g41G7_2w_BC2GCZkF_7_ySslFgVA6QMnxtJY8FxkcppUsosBR44OdRFqROv-iXPYiIVkSubcJbrxRXrjMb38YBnO7nmqArlytIcePuVG_WcDEhzw_ja9fE2M4VN8kVyn-l_z4jxlDNueHUQv-LpRqdzBUrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b372ec2c.mp4?token=GWxjtqFs-qmtvAdGWH1TlCr5vyEYKwYjzbLlFRsJRNGWDUgYjpT4qhsoJNzDljX1pQh3v3IpF3N0rsKM4sNa54Mv7QAXegrMFhFhA9DNtOLU1lMxQr0Pe2dE047ki8sTmI6_7HOD-Mk4UHtEppeLkud7_o1NvZHXm-CA4Uj2Z-Wbt1VahDFZ1WINWQnv3_WqZ5NUzRPDwH4KBpjY7PRLmd72PxBS5y29Mh2bUp8_jmsgv7tINgtShV5N8NYcdpuHhbUKBibxBrVTB1WcV2KT481NGYBQV5oZAN63Uf0FMbhd9Ka7B_0ThCsuWCZoybynWyu6RRWU3WWpfocFgvIyU2BFiqOZK9Qj-T8W2aoHllqPTYnLMXEAVRo5FhIhx9pJgezQ8TS1QX1lbL1YUqM5gWReuK-dlEpgzDibd6tdsTBI4zDYFOAVcrZRoeAovKO6mpxHaobvxZeAw7jMW4_DjOzldZVxkDwWDCB27nYgZ-zBwTW0GwLMjWlmBGnhRwHFityQypb9vFCdC560g41G7_2w_BC2GCZkF_7_ySslFgVA6QMnxtJY8FxkcppUsosBR44OdRFqROv-iXPYiIVkSubcJbrxRXrjMb38YBnO7nmqArlytIcePuVG_WcDEhzw_ja9fE2M4VN8kVyn-l_z4jxlDNueHUQv-LpRqdzBUrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عشوه‌های عجیب المیرا شریفی مقدم در پخش زنده تلوزیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/136791" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گویا اینترنت بزودی قطع میشه
‼️
🔴
دادگستری تهران: داشتن و استفاده از استارلینک جرم سنگینی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/136790" target="_blank">📅 22:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک آخوند: علت قهرمانی اسپانیا، عدم کاشت ناخن، نزدن لاک و عفت زنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/136789" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا تو تجمعات شبانه کسی با دخترای بی حجاب کار نداشت اما تو کافه‌ها گیر میدید؟
🔴
چمران: هه هه هه
😊
😈
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/136788" target="_blank">📅 22:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/136787" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/136786" target="_blank">📅 22:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/136785" target="_blank">📅 22:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuQe8RfSBNUfUa65SUL7ZSd8JW__Ca3h8JsY6vGvCCccCSPzCChtIiMtPmQbyHEu51Cv-79dlRz6sdTV8I40mZiBPxjAOF7RMsaRMvTzo0pezDcWHs9Hqpted4j4TjJ_kIUJOmhhcsw6WYJ8ZRRPA2jLC73KQRpaJJIeBpxiOY56JZZTBH-c3ueaHB0WlKegwmaH7HpVBNlYB1Ywvrb9UvTK3xfNUuP1Hhx5cYUmr3gg7kZDy_EwWBakLGspL4KolMvREBU6xVlpLWIkAllgaWZx-82Bp9KgMmcHIuTnWhnmf2twglVhjQ0t11TgvmHND1wPIr03Sux-_3r_5zN4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/136784" target="_blank">📅 21:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند
:
علت قهرمانی اسپانیا
،
عدم کاشت ناخن، نزدن لاک و عفت زنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/136783" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش کانال ۱۲ اسرائیل، مقامات ارشد اسرائیلی نگران هستند که ایالات متحده ممکن است به عربستان سعودی اجازه دهد تا در چارچوب یک توافق هسته‌ای مدنی پیشنهادی، اورانیوم را غنی‌سازی کند.
🔴
یک مقام ارشد اسرائیلی این پیشنهاد را "تهدیدی برای امنیت اسرائیل" و "خط قرمز آشکار" توصیف کرد، در حالی که مقامات امنیتی هشدار دادند که این اقدام می‌تواند باعث یک مسابقه تسلیحاتی هسته‌ای در منطقه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/136782" target="_blank">📅 21:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سفارت انگلیس در ایران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/136781" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/136780" target="_blank">📅 21:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگه هرمز استفاده نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/136779" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
در آیین دریافت استوارنامه سفیر جدید پاکستان؛ پزشکیان: تلاش‌های مسئولان پاکستان برای تقویت صلح، امنیت و ثبات منطقه‌ای شایسته تقدیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/136778" target="_blank">📅 21:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فعالیت جنگنده های ارتش بر فراز کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/136777" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منابع عبری از شلیک موشک های ایران به سمت اردن خبر میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/136776" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار مجدد در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/136775" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6gMZW2YEYsHNLVlvEzbdXHEZl0e7Ezk_lwq2n3A9LrcrUcgtFv1zug446cjdnrxYtdwWvoKQf8tg5NHUpMh90fmQSuGUX5QuH9CJB5xGEtf02oIVAP466BzUIOqQ5Nrq5TL9oayF8YzXiKvz1NhbTkbzCJkG-oTloK_8Y6c3K4rG2UKrh74xmIkqRhCwwdPM3r5Nf9G2rhELcq8m29auoNI6XTrQFv9l3CJzNYsnQF71OGHBxKa6afVMdyJAbgRs2NAQtq9PQyEX_fJNUZNcju8ohqI1zHOTo7Jno__6-wffK8SKWlMN1NpNUIKEptqEPWLoANst_x7Q6j0upv4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔴
کریس مورفی: توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/136774" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFogKSwRUBcdVw9EMPzTxm3TezN4rJHOMYgg8Q-KyEcFMlF8-l9cmBqdTTA4cqEhowClY0dfGg-ndhyu0L0U046wziTvbGXYc-tieLkmwyUciZW9Jgclsosozi_NSSQJuW6ir0HaXU360BubasN19QMRyMmhb419HsrIdalEP5MHJkK1mgiM4J4CDzku0UHizBMV_W6kTLJl_lzV67Q80nY1DyPB1q_KLPDrvfITkCk2lB1JByYR0mpbWPctpAFiIZqi4sg1Xq7f9eAdgL95Y2cKmtOf-4R2fE6NAfDZ1_nZsbKInir07G4EAXQSuzS_873LBR2LYZzvXUZQwA75bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته دو منبع مطلع به آکسیوس، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
🔴
منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
🔴
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
🔴
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران بندهای این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136773" target="_blank">📅 21:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه:
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/136772" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💔
مادر جاویدنام
#عرفان_رضایی
قلب هر انسان باوجدانی رو به درد میاره.
🤔
حرام زاده های حکومتی که دم از وطن و دین میزنن، قاتلین هم وطنان ما بودن و هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/136771" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سفارت ایران در اسپانیا خطاب به آمریکا:
تا می‌توانید تابوت آماده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136770" target="_blank">📅 21:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گزارش اختلالات شدید در سیستم GPS در سراسر خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/136769" target="_blank">📅 21:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q478gblWV6TTLQYZo1DkiyZNl3wCj2oxMJUbNe9rwZ3AYble1cS1T8FRsP0gcemQ9QOSJjBNgTq3ObKqCZNdaXaKELqTyqZ9aa8qabhLepC2TmpZ5-9Q3JwkI5GhjYjsv4_nyiWuU8ZNp2L-N54djmOFN6EWpI6vIvZ0HsPg1KTqHqM0PlWGU6ZjU4uuz4yY_dEOlL-Iv4_sN5V6_xAme8GHjAS8X-znLz0yOoBPvorVDUJT-oZfmkFzvcUsEpdhcenGkTxO9rqb0H7pAtDA0fHBOf9_Nc0bqVxJXOMbxqZEGf-N2MN9VTJQZhm11hnCkH2_coyPhVu3MxT-HmL69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: دوست داشتم برم بندرعباس باشم اما پروتکل‌های امنیتی نمیزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/136768" target="_blank">📅 21:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش شلیک موشک بالستیک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136767" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
هم اکنون حمله به اربیل عراق و فعالیت پدافند هوایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/136766" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/136765" target="_blank">📅 21:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2AYcwXTL9sCDcPQrxi6UL3-mpTwzsUic2HaTvH0isWZDjl-T3Les_hQYyACldSkAaq5Aqr2fASFPkErR9KidKn8CIo06b8fJvIkXR2pvCmM4bPbdXUAubwZoxrpjbH-FDnKtzdYlsmsFNatrM7egFFByxoMVeK2Gpnjl6UAeAHosbop5jAe7N-xxY4NnnDmmvVwg6mAjQ5HnKCQIoRHfgDrWorzLmyV07iQb4goCtKti4KQ7bAMhvhpVB-xxtTKOGQxSUZktprJSHNi5EJAwjsEUXaNEDhSs3upy-IrgWWsBh8f-kDjJsULsCOhq4bO6qGFCfQRR850qExshMDCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادله این جنگ کاملاً مشخص است: یا همه، یا هیچ!
🔴
در منطقه‌ای که ما نفت نمی‌فروشیم، هیچ‌کس نفت نخواهد فروخت.
🔴
اگر امنیت ما تضمین نشود، هیچ زیرساختی امن نخواهد بود، و امنیت تنگه هرمز در غیاب نیروهای آمریکایی تضمین می‌شود.
🔴
ما بارها گفته‌ایم که وضعیت تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/136764" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سفیر چین: پکن مایل است نقش سازنده‌ای در بازگرداندن هر چه سریع‌تر صلح و آرامش به خاورمیانه ایفا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136763" target="_blank">📅 21:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CigfR1Qif4-qxdeqdKgSYiOCXqvWEhm9fJ0zdEYnVTMRdIZHpH9eNqor6ocO1sXJO0LJaE4OTUHP84hZVVlLDZT_Fa6wrF9C5frjX5m1ADAi54fL8WO00WjUlsJl54EQDkIvIIR6w3ny4EK67VaRaTm_o9__S3jxa4yUcqauasmIhqNNIUTSBiYZkqnkCAkCP9J7t-aCxGX3qz_V-ctVo-MkePjEA7XJx2KYZg2ytiQ23GKsyS5aZsIdIW8NSVV2rXOwUUNjrx6u67YdXivRzQuudwK52_wRdiUK7f8LSWtry8l0IS2Q5_db9jYXqZuojjb2fEuZI7X95__TpddylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/136762" target="_blank">📅 20:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
به گزارش واشنگتن پست، دولت ترامپ در حال بررسی امکان انجام حملات نظامی در مالی علیه گروه JNIM است که با القاعده ارتباط دارد.
🔴
این پیشنهاد باعث اختلاف نظر بین مقامات ارشد دولت شده است. گفته می‌شود سباستین گورکا، مدیر ارشد شورای امنیت ملی در امور مبارزه با تروریسم، یکی از قوی‌ترین حامیان این اقدام نظامی است، در حالی که برخی دیگر همچنان مخالف آن هستند.
🔴
یک مقام ارشد دولت آمریکا، نقش روسیه در این منطقه را مورد انتقاد قرار داد و گفت که مسکو «به عنوان یک شریک امنیتی موثر برای مالی شناخته نشده است» و ابراز امیدواری کرد که کشورهای آفریقایی دیگر «به عملکرد ضعیف روسیه در مبارزه با تروریسم توجه کنند».
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/136761" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پزشکیان: سفر نخست‌وزیر عراق می‌تواند نقطه عطفی در توسعه روابط راهبردی دو کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/136760" target="_blank">📅 20:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc7VxFd_nlTHe8Sa4j9uA0vBZyT2Mu7Hh9rJxxBEfjVw8ifGgl-TkHnNxHW50FtB79QON1TrrEW8ME4_1332Q7qvulaRp3JAkMG4NpUvfeeEzhX4g47LNgYWqMsCBVOIUQ4_YRDWcwW-qsfWQX6Bgu4c6nOwBdQbmIcUCr5J6EHTTysgq2T59m4qpcj2gRNf9-WlkwM1YIhDKYvTB5Xu6A7GIvgBfYXRx8M51zJ57KSFtt0k1PtjL4DbiFji_EhQBVwvxpmYU8U6ee8GlKU_TpwTQGRoMB7wFuw8sTPhmRwF4wwfVInfCEf9W4MoCI7scKeMA4Xv9dmmiR2xmxWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیباترین پیامی که تا حالا تو الونیوز داشتیم
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136759" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسیر جایگزین پل کهورستان که در حمله آمریکا مورد هدف قرار گرفته بود؛ نه تنها فعال است بلکه آسفالت هم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136758" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس: ایران با نقض اصول قوانین بین‌المللی، به حملات خود علیه کشورهای عضو شورا و سایر کشورها ادامه می‌دهد.
🔴
ما اظهارات خصمانه شبه‌نظامیان حوثی علیه عربستان سعودی و تهدید آن‌ها به بستن تنگه باب‌المندب را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/136757" target="_blank">📅 20:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HkOezMYrdhMs9uQ3fvjqcOgJMrF6_EourbCJJriYXtuNhQrmLywi4wQu4uYRl12Wy5zMI53HTxd0NbKpWJekEsyiqB-GjQJ4Qk2AWeW4BhYgZiwHjsWHhoTCWb9hOFfHm_RR8wee88d9deYvdlwV6XEVYAFLfaxZz9ZsTyZZiZjsGjPmjazufN8YB7_ulpa7Dy3iBbgZGUxO99mY-NdCLTllYAhJJyIFS0i_70dmy5BVEfqV9td-3JdkAZIImqTldLoZrrcfEewx3qeZRkBOcmSe7huEk_KtoTXEawwcArYVxj0EoDZrz6n1xqAUecYMx-PRdsmavkVzxiiMdZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/136756" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
محاکمه نیکلاس مادورو، رئیس‌جمهور ربوده شده ونزوئلا در دادگاه آمریکا آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/136755" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
