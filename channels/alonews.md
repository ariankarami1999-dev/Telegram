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
<img src="https://cdn4.telesco.pe/file/JV41u49pICKvxhtDZUmkLpYUSvjOzg2peqlHugpy8sLZ7cnVeQil0gqkQ8gaD0G3KFCDAzTqiaCoPDQD5cxfUBXEuODQHdq0BI7Zq2vMWw5LfXu10RRY2jg0ChA4jnFPgjtbFxfYb6m1rIjovPlgvipke9PWJPyQ7tWHVkaOgPUW9BNsmoMLDuVEkcxdP5nFhNgN_KEUfIV43tWA05hHob9TdvXzxCFXYbneMgHlWm06pAkKqdfFda_CagrRRMqVKYT-ik0uA2fKUoRGt8GLRnNQ10CLkWOWJ9aQ0iPJFEb4t9O0xFVC9WNkQzTHO5NwtUs6E6q96VISXCRTYF4NxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-130249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZG7uyNlbxcuAiiUjBPfoUhIxJBWkuiuaFQIbmUpE11_gsdN-yWNgGMVMhuyOw1SX9BGsbe179N7X15T9h3uS9d9TzlSLvYWnadbuSKXFuiz0PkXFGb4zh7EiJmIe4nC1bsJfw6JzcQ2rorsKEwCKrNig85Bf0TlETkCrCPgtPq9k_-yBaVztYorfWIRG00KQlpUBsgI4j2rDpBwTFuxKBnA4Z7wjMPo2lKdpX2VMchsR3OgultPT9k-Aabw1XNeHpNHEiQau-7IGH5-e0WN4ZQEIcXdkvyrO6ROu2XnF0OD8lgwq-9BZOOSN3ulrJh0nXq3tWGkSjmDabfa89LYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxdwGHd4ed-fUJs8v7v-vJWb1eMnv2k-e6WWJ9QgVRa1N9_Jl5CpuJCTHabvKHhBrU-KqPMDyzO0-orZM-nwKz_ErvJg5e8bNYe55pakTvwYDF-0KLGMVM9nUCYVRLDtmnIrfxS9IpbRC0Jv6EDd4asG3sLR-U6sMHMxdwY3bbAhROH4ON6BRZHSs32uE-nKw7OZibIvc_TUm2Keu8ZYMQ2YoWYTAtIFMaikCP6brQ4XtAj7PmSCytq2icvq94hhwY1BGYLyFBSqqGJ3-PilY3p3lvS-2Dz7wJWZzxMVjcJT1NaXevNr90xLo4m2uEPA89ycOM86Su341cxt274wJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محاکمه شیخ "احمد بدرالدین حسون" روحانی و مفتی سوریه در زمان دولت بشار اسد در دمشق شروع شد. او متهم به حمایت و توجیه سرکوب مخالفان بشار اسد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/130249" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شبکه المنار گزارش داد که توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/130248" target="_blank">📅 23:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130247" target="_blank">📅 23:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDdMI6j1If8GksSbhkYA_QKX6pU3SlZpkTbCfZ0ohLPSBWYZY1X0eYMQWL6LP-A04S7wiraSMBL5U9SlTcCq0JycLMZjoUp-cLlSsPlzAPbPRY4djRNdXOXSwnyAO6tWxsa7bwCp8PC5NgQs5P-IS4P3gdyyMzIaSW19LZnQCpTtr9RXkGcWRA8HEx7dplEtTLHXnLalZqeqxuvTfQsmG3WyJ0E3m1kPyaw9M_2MSX29YdXqNKhY26Zcv-UM4tzdyrh4zk78W3fWuYIhbiAhHzXrw86y7jLRX8Hq5LyAdKQkzfjlDjhtjPgwnyXQLN-meteuObhwnDdYmo1ZWJreTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید گفت برید مذاکره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/130246" target="_blank">📅 23:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله رو در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/130245" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=nx1chjl-p0He4tbapu-JolouaNdnVuQyNArDNvqZ4cW3ORk74fNsAXnMKRPVImGQcXUO4_BDPUxlwY9gUa617MtADiAqtzxL8JpDm1SKnlt6JomCsr3W9oqL6gpbJEMLvhsPXZW2lTTFM5WE7hE5KJPLakmlcV2lAu15dQhKxpPo4Z0-iBKFKUvrgt5Sd-nDcN9YgqyhAznEgYajqWqUaoiFPxamYNw8W0iQH4eFbLScY4XVrsA84W_NXAnRfsPAC-XFo_qWbbwZ4jWFrqcJl43hC4G6olUR0VIoMARCavuuKxZWdWWICvUeGMeHvyJGvP3IP5swQz8vhF-i3wHKQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=nx1chjl-p0He4tbapu-JolouaNdnVuQyNArDNvqZ4cW3ORk74fNsAXnMKRPVImGQcXUO4_BDPUxlwY9gUa617MtADiAqtzxL8JpDm1SKnlt6JomCsr3W9oqL6gpbJEMLvhsPXZW2lTTFM5WE7hE5KJPLakmlcV2lAu15dQhKxpPo4Z0-iBKFKUvrgt5Sd-nDcN9YgqyhAznEgYajqWqUaoiFPxamYNw8W0iQH4eFbLScY4XVrsA84W_NXAnRfsPAC-XFo_qWbbwZ4jWFrqcJl43hC4G6olUR0VIoMARCavuuKxZWdWWICvUeGMeHvyJGvP3IP5swQz8vhF-i3wHKQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته از ناتو: این بهار، با مهندسان جوان و بااستعداد در شرکت ASELSAN، بزرگ‌ترین شرکت الکترونیک دفاعی ترکیه صحبت کردم.
🔴
آن‌ها انقلاب صنعتی دفاعی ترکیه را هدایت می‌کنند که به نفع هر عضو اتحاد ما خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130244" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=BbiarLBOWcpDLDVwlNCvNJNupmrb0RbO5s_fv-BdgPmc3gAud7AKpKir8ZGPBJJxKZ-GNrHNmpAmML1VL9dBvjoQdcEtJBIj9wm9L5ZSnVTfLrRrHIiNSvqiTtC2Jgv6c9BzrQoSaTalvSyQF8Mdd-kcpXhomTRHvm_kZoIC2pXHUQIgedrwYl9KY-TD4cVZjcQ7i20rnM9m4v9I_SKupgujX2Y0KdpvSF_7wlQH8n_MF4QFEFZg2v4hTbNlVMLEh8i8fSz5GCPFnXrCqlCbz1LI8ofgPO5180PBwhu85MdWQn54yjz1cSub6xHAq87VjN2LvasbAMnpi4rrI1s5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=BbiarLBOWcpDLDVwlNCvNJNupmrb0RbO5s_fv-BdgPmc3gAud7AKpKir8ZGPBJJxKZ-GNrHNmpAmML1VL9dBvjoQdcEtJBIj9wm9L5ZSnVTfLrRrHIiNSvqiTtC2Jgv6c9BzrQoSaTalvSyQF8Mdd-kcpXhomTRHvm_kZoIC2pXHUQIgedrwYl9KY-TD4cVZjcQ7i20rnM9m4v9I_SKupgujX2Y0KdpvSF_7wlQH8n_MF4QFEFZg2v4hTbNlVMLEh8i8fSz5GCPFnXrCqlCbz1LI8ofgPO5180PBwhu85MdWQn54yjz1cSub6xHAq87VjN2LvasbAMnpi4rrI1s5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هزینه تجربه کردن GTA VI در ایران، در اقتصادی ترین حالت ممکن: پلی استیشن 5 اسلیم 1 ترا - 112.000 میلیون تومان
🔴
تلویزیون سام 32 اینچ - 26.300 میلیون تومان
🔴
اکانت آلتیمیت GTAVI ظرفیت سوم - 5.500 میلیون تومان
🔴
جمعا 143.800 میلیون تومان
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130243" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi6HKd96qkDpVvQD0qAEc_vasXu4R45UCx68j4qG1wGDAKAeIuwDUFG1lW9Vla_pMYVmusfah4F-kpF3Qe5fvQk9lB3pjJw2RqcCukePg6bFiOoJIRCIEooWqO865cHmBYXBiBGddygyeX4KeMgWQ5pL9Zc8MAY4DKSYsSlnW3WADzfIuXN-BVtU-tSGY-GhqLNwBR4LpWHhAbUIYDnVksq4k4VxA0P5ZtcR8SECiKbcdSQSwIEAJP5frXNnBPTfbHgGpslZOoMV6HkGasVyvt_5_EoGyyCLxUmVNeWvserooacSOTlGKedLKm-qyqQUb4_zbWtiQnmfaIR3OTtaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130242" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6-vfN-IKYLpt3wCtn2o7yCuMm2YFmmXO56zPA2AOu30TGDs-XZFcI017-wElrn_ZR-yCLVp0TAkLxK-DrXsPgmke5KErC11s9Y_XYXaNO43EvUCdlRrUtQ9e8JSzFWrLfaY0b04-S-4aNwcUJSuA6bd7tuPcv9aj2XLPZqAcHQInm-VdnQabcmQCdEkfEPkPoghaz9ce0gQxB87GFwaM5Iqgkg-KplkEUvjdYQrB_a2tMwJf7Wm2u16x1lOBpEgXHefeYoQT6cQHz6TNVp5gqBsDsLokTHtHbgt1lwnQjAgw6ooFK-7c4V7ltiXXv_No2a-CdB7XzrBjbUKnl42rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو سالی که برای پزشکیان یک عمر گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/130241" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092b312727.mp4?token=DM6pTxeHeES2qDLlMRwXBDTSy9rYq9mdyZzCW4GBIazSIr31HOUW0-g5vNHldBQksmon--85uDGP8W9oe6yBELGO3a99n8KXlaumZgxBtOz151IYHDczq1dIGF-9Ma791gMoBKmWjghqbaDNNedmYAtiDlgz2quFCnmkaaiMh_Tsis4dKC4FnK8ztdJ4ExFZ8T4W9EeXutsWzaqoQmSQsstsnJ3ie4lphTadzbgJIbzBc3rHPVeEuBi9sIPOl0ZzsO2SskbyAD3qMrejRfg5mie0d2xwuG3gICZmT_nxMzplfjiPMY5S-DOFUvarNB9b1UqrEcEEjwzznTTekIMslg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092b312727.mp4?token=DM6pTxeHeES2qDLlMRwXBDTSy9rYq9mdyZzCW4GBIazSIr31HOUW0-g5vNHldBQksmon--85uDGP8W9oe6yBELGO3a99n8KXlaumZgxBtOz151IYHDczq1dIGF-9Ma791gMoBKmWjghqbaDNNedmYAtiDlgz2quFCnmkaaiMh_Tsis4dKC4FnK8ztdJ4ExFZ8T4W9EeXutsWzaqoQmSQsstsnJ3ie4lphTadzbgJIbzBc3rHPVeEuBi9sIPOl0ZzsO2SskbyAD3qMrejRfg5mie0d2xwuG3gICZmT_nxMzplfjiPMY5S-DOFUvarNB9b1UqrEcEEjwzznTTekIMslg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف در سفر خارجی با هیئت مذاکره‌کننده بدون نقاب حاضر شد اما شب عاشورا در هیئت «ریحانه نبی» با نقاب حضور یافت.
🤔
کجا احساس امنیت دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130240" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
چین رسما اینترنت 10G رو راه‌اندازی کرده؛ فناوری جدیدی که سرعت دانلود و آپلود رو چندین برابر می‌کنه و می‌تونه یه فیلم کامل با کیفیت بالا رو تو چند ثانیه دانلود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/130239" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراق پس از بحران مالی شدید مرتبط با اختلالات صادرات در تنگه هرمز، هشدار داده که اگر گروه صادرکنندگان نفت سهمیه تولید خود را به طور قابل توجهی افزایش ندهند، ممکن است اوپک را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130238" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130237" target="_blank">📅 22:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrFQmBQeGVjrZ5qbGpgWEKfVWA4sWXYyUGDy5nJccj8gxp88cDHI9l4wdTPZ6S_rfFMpE7MHR-6UCHo5vzQbwS8jiY_qkPNjm6Sz7lb2AjSD4HC8Dz5G_uOsZS1Wq_EJWuFI4mYwwg0hr9gCzDvlz47NBMLSt3VFvaKdyaZdGd6LkZXWzSUUPA8elNC3hnkjmQunDm4gXVdCQKyGS90HdeknGqJ1S11KpJ24KiiuRm5bhOJ1A5brxdSEwL-eP4lYySN2KlKW6oehg3HjFYWZPFHxbH9uzdbsvi8OPGVe3kMwXoG7Er7GyO5IThQAd2fpvbGpahXRyFqS6HeVYMc5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130236" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130235">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeiUN_57Tqs_i66TMDufmkyRgpZnB-PPUSShl5Dz6xBAHL0axcZQ-EaJuzAl_LSzE6LgyfY4SpVg46tRtDtf_6zXHECmX_N2HQh9A0YSOI439zgBjLZO6QrUPV-2_BKt9LKgUve6vntoC7Q0hYko_B-aw0iF6sC_YFS2LYiaCggeMw9wZhxUafVWjPr2cU-t6cJ8blKSpFOrN8FAYZ73vXVDwBc_yo7xGbcGQ_J2eO0Qx0Z8pa6JGpHS-UazRyXCe4GHMzDkdZtsKTACxOVL1bEII-p13ulgG33d9N5WqN5eRbdrrduZCP2Nz1BNNcIBgsMiNRbYkwFZLEB7XOrFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130235" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130234">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ملونی در مورد ایران: ایتالیا در درگیری با ایران شرکت نکرد.
🔴
در واقع، اگر در درگیری با ایران شرکت کرده بودیم، توضیح دادن ناامیدی مکرر ابراز شده توسط رئیس‌جمهور آمریکا دشوار بود.
🔴
ما با در اختیار گذاشتن پایگاه‌های خود تنها برای فعالیت‌های لجستیکی و فنی و نه برای عملیات‌های رزمی، به تعهدات خود احترام گذاشتیم.
🔴
و زمانی که درخواست‌هایی مطرح شد که فراتر از آن چارچوب بود—و شما این را می‌دانید زیرا به طور گسترده‌ای گزارش شده است—ما مجوز استفاده از تأسیسات خود را صادر نکردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130234" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130233" target="_blank">📅 22:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروی هوایی یک عامل حزب‌الله را که تهدیدی برای نیروهای ما در ارتفاعات علی طاهر در جنوب لبنان بود، از بین برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130232" target="_blank">📅 22:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130231">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130231" target="_blank">📅 22:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130230">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هم اکنون حمله موشکی گسترده روسیه به پایتخت اوکراین، کیف با استفاده از موشک های سنگین و بارشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130230" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نرخ اینترنت مخابرات دو برابر شد !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130229" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130228" target="_blank">📅 21:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: اکنون ایرانی‌ها می‌توانند نفت بفروشند و پول آن را به دلار مستقیما دریافت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130227" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
احتمال بسته شدن مجدد تنگه هرمز!
🔴
سازمان بین‌المللی دریانوردی از تعلیق طرح عبور از تنگه هرمز تا دریافت اطلاعات بیشتر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130226" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130225">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130225" target="_blank">📅 21:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130224">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130224" target="_blank">📅 21:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130223">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر دفاع اسراییل: هر دلاری که وارد خزانه ایران می‌شود به موشک یا پهپاد تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130223" target="_blank">📅 21:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130222">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، ولودیمیر زلنسکی اعلام کرد که عملیات ۴۰ روزه سرویس امنیتی را با هدف اثرگذاری بر کشور متجاوز تأیید کرده است؛ عملیاتی که به گفته او برای وادار کردن طرف مقابل به پایان دادن به جنگ طراحی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130222" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130221">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130221" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130220">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وال استریت ژورنال: تهران در مذاکرات با چین و مصر، پیشنهاد خود برای وضع عوارض خدمات بر عبور از تنگه هرمز را مورد بحث قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130220" target="_blank">📅 20:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130219">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130219" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130218">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
به گزارش نشریه NRC، هلند در قراردادی به ارزش ۲۵۰ میلیون یورو، هزینه خرید ۷۰۰ موشک کروز روتا بلاک ۲ را برای اوکراین تأمین خواهد کرد.
🔴
این موشک‌ها که توسط شرکت هلندی Destinus ساخته شده‌اند، بردی حدود ۵۰۰ کیلومتر دارند، کلاهکی به وزن ۲۵۰ کیلوگرم حمل می‌کنند و از هوش مصنوعی برای تشخیص هدف استفاده می‌کنند.
🔴
مقامات اوکراینی اظهار داشتند که این موشک‌ها از حملات به اهداف نظامی با اولویت بالا در عمق خاک روسیه پشتیبانی خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130218" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130217">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بازی جی‌تی‌ای۶ در کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه، تاجیکستان و تایوان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130217" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130216">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYysEOb_pbbzczw9oTBPiUq06YuRcdm-pBaWSx2Gn9je9A6osuDcvFj3XDQZD1pPx4IfnUN14K2QvaLhgwlj40O4tIxKBk-VlmkKBEuXyRslUVhvgGEw2T7OWcRD3u0GWcn3HvnO-koRu2zJhd5hVmRbJ4h0qO0e3Vm6BSUzUsO0z7iYRlwz2d-zmpwokzN_Ac94snGTrAOrZe5I4MkTODZNMyvcE-HdD2mvNP6L2Y_pF-i86rn1HMNtc1ZTh88-km7Ib32mewcm5DUJgaL0Ys2yIQlq0v0qm7r9fyAMhhuGRUk99pLD5II6ISXEsTsWIKcMvCkiRTae1WKs0gxLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظر سنجی فاکس نیوز رسانه طرفدار ترامپ و جمهوری خواهان؛
🔴
موفقیت ترامپ در اقتصاد :
🔴
۳۱ درصد موافق
🔴
۶۸ درصد مخالف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130216" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130215">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130215" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130214">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130214" target="_blank">📅 20:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130213">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دبیر کل حزب الله ، نعیم قاسم: صبر ما معادلات را تغییر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130213" target="_blank">📅 20:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130212">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو: کارهای بیشتری باید علیه ایران و حماس انجام میشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130212" target="_blank">📅 20:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
به هیچ وجه اجازه نخواهیم داد ایران
بمب‌های هسته‌ای توسعه دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130211" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من ادعای نبوت ندارم. اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقه ما و به طور فزاینده‌ای در سراسر جهان تعیین می‌کند:
🔴
قوی‌ها زنده می‌مانند. برای ضعیفان جایی نیست. آن‌ها شکار می‌شوند. آن‌ها ناپدید می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130210" target="_blank">📅 19:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130209">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما در خاورمیانه‌ای پرآشوب، طوفانی و وحشی زندگی می‌کنیم.
🔴
دولت اسرائیل همیشه قوی و همیشه مصمم است.
🔴
بیش از ۶۰ درصد از سرزمین نوار غزه تحت کنترل ماست
🔴
ما از قلهٔ بوفورت بر جنوب لبنان مسلط هستیم.
🔴
و تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهیم ماند. ما قصد عقب‌نشینی از آن را نداریم.
🔴
وزیر دفاع و من به ارتش اسرائیل کاملاً شفاف کرده‌ایم: «شما آزادی عمل کامل برای حذف هرگونه تهدیدی برای سربازان ما یا ساکنان شمال دارید.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130209" target="_blank">📅 19:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130208">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: فقط یک فرد نابینا می‌تواند بگوید که دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
🔴
من همه آن‌ها را فهرست نکرده‌ام چون می‌خواهم شما را بی‌جهت خسته نکنم. شما اینجا زیر آفتاب سوزان ایستاده‌اید—فهرست کردن همه آن‌ها زمان زیادی می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130208" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130207">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو: ما تهدید وجودی فوری را از سر خود برداشتیم زیرا اگر امروز علیه ایران اقدام نمی‌کردیم، بمب اتمی‌ای به وجود می‌آمد که اسرائیل را نابود می‌کرد، و ما این تهدید را برداشتیم تا ابدیت اسرائیل را تضمین کنیم.
🔴
وظایف بیشتری برای انجام دادن وجود دارد.
🔴
بله، کارهای بیشتری علیه ایران باید انجام شود؛ کارهای بیشتری علیه حماس باید انجام شود. در همین حال، آنها توانایی زیادی برای مقابله با ما ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130207" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130206">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت:
نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130206" target="_blank">📅 19:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130205">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نتانیاهو: همچنان ماموریت‌هایی وجود دارد که باید در مقابله با ایران و حزب‌الله شود،از لبنان عقب‌نشینی نخواهیم کرد و تا هر زمان لازم شود در لبنان خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130205" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130204">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx13orMq7PUNxp55ARuTGST77bEnNc_iSgYIztUUSAFKmVDJiJdkjoaaMO42YUI8HbKBal67lwnnYX62SRYON89Jq469jUvL0IZ3LFZWB0of_nL2XdtV18S6davwTSPrv_RD5CHbtXyt3d89Tkf-jo2SN9fKJsF6G84Lyi7euhvsdVnJETjS-V4NoUvc1eSau91uJjLKL2RtaiCHb6Ai1tkMbQTa7sBK27PiGFrAcyBiDAnKOmvyVu5qX1J0iRk09ToawbOl7QBmnf7oUiTTDqNBJMVeKODNRROEbS511DktXQW6x4WaZqQLN_VrTEplc-wnyguUY_YtcURwEuhPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، یک شاخص مهم در صنعت هواپیمایی آمریکا پس از شش سال، سرانجام از زیان‌های دوران همه‌گیری کرونا عبور کرده است.
🔴
پیشرفت در مسیر توافق میان ایران و آمریکا باعث کاهش قیمت نفت شده و فشار هزینه‌های سوخت بر سودآوری شرکت‌های هواپیمایی را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130204" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130203">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعزیه عجیب در فلاح تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130203" target="_blank">📅 19:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130202">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش تا زمانی که لازم باشد، در «مناطق امنیتی» در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
ما علی‌رغم فشارها برای خروج از «منطقه‌ی امنیتی» در لبنان، مخالف عقب‌نشینی هستیم؛ عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130202" target="_blank">📅 19:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مرکز عملیات دریایی بریتانیا (UKMTO): مرکز عملیات دریایی بریتانیا گزارش یک حادثه را در فاصله ۷/۵ مایل دریایی جنوب‌شرقی دهیث، عمان دریافت کرده است.
🔴
یک کشتی باری در سمت راست خود توسط یک پرتابه‌ی ناشناس مورد اصابت قرار گرفته که به پل فرماندهی خسارت وارد کرده است. ناخدا گزارش داده است که تلفات جانی و اثرات زیست‌محیطی نداشته است.
🔴
مقامات در حال بررسی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130201" target="_blank">📅 19:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130200">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAE5KyZL0QdrA6XMpd8fE3kBTeMJuRtrTKyZK9fIhRaqCRURZmC6BI2z7aWLqcC7Bddg7frTjhIg7y3JwPs2NEn06ltYG1d-gUsP3ltw5iYk_x7Z4kWQT76fLyPPP7w7ti0urctXN1sk1sHDAutOgm2YFWJyTB3Rs-0rZiXxwqol_06dSwY1dWraprGGw3xzNVIBgtYtrJVTcR6SMjRlNBpyWgj7USBOaqWxLzb3v1Rl8HTbooRKgeh71y5SZBGo80RXEYFUk3L5VekCkIg6m6NEo9TxChda9pDMVegDlmw_h552iEKIbhyfTsxQFoODg34WiLjAJdmW04Wjz7OL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130200" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130199">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130199" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130198">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ایران روزانه تا ۲ میلیون بشکه نفت صادر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130198" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130197">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مقام آمریکایی در گفتگو با نیویورک پست: وجوه منجمد هرگز تحت تفاهم‌نامه حمایت شده توسط ترامپ به ایران نخواهد رسید. در عوض، پرداخت‌ها مستقیماً به فروشندگان تأیید شده‌ای که کالاهای بشر دوستانه تأمین می‌کنند، ارسال خواهد شد و نه به خود حکومت ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130197" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130196">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
🔴
طبق اعلام فیفا، هواداران می‌توانند با پرچم‌های رنگین‌کمان وارد ورزشگاه بشوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130196" target="_blank">📅 18:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل:  ما از کمربند امنیتی در لبنان عقب‌نشینی نخواهیم کرد، حتی اگر ترامپ یا هر مقام آمریکایی دیگری از ما چنین بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130195" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130194">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
لحظه فرو ریختن ساختمانی در ونزوئلا در جریان زمین‌لرزه‌ای که این کشور را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130194" target="_blank">📅 18:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130193">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
جی‌دی ونس: یکی از بزرگ‌ترین پیشرفت‌ها در مذاکرات سوئیس، توافق اصولی برای ایجاد یک کانال ارتباطی نظامی مستقیم بین آمریکا و ایران بود تا به جلوگیری از تشدیدهای آینده کمک کند.
🔴
ادعای ونس، آن‌ها گفتند: «باشه، خوب، ما کسی از سپاه پاسداران می‌فرستیم که در دوحه با کسی از سنتکام ملاقات کند، و این‌گونه بسیاری از این اختلافات را حل خواهیم کرد.»»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130193" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خارجه آمریکا روبیو می‌گوید «خیلی نزدیک» هستیم به «بیانیه اعلام نیت» برای خروج برخی نیروهای اسرائیلی از جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130192" target="_blank">📅 17:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130191">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد وزارت نفت عراق: به دلیل کاهش شدید صادرات نفت در پی جنگ علیه ایران، با بحران مالی حیاتی دست و پنجه نرم می‌کنیم
🔴
در صورتی که سهمیه ما در اوپک به طور قابل توجهی افزایش نیابد، مجبور می‌شویم که تمام گزینه‌های موجود را بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130191" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130190">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیش از ۲۱٬۰۰۰ نفر پس از زمین‌لرزه‌های ویرانگر که ونزوئلا را لرزاند، مفقود شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130190" target="_blank">📅 17:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130189">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رهبر انصارالله یمن: پیروزی ایران در برابر دشمنان، پیروزی کل محور مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130189" target="_blank">📅 17:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130188">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
جی دی ونس: اماراتی‌ها - که تا حد زیادی جنگ‌ طلب‌ ترین و تا حد زیادی طرفدارترین کشور در شورای همکاری خلیج فارس هستند - در حال گفتگوهایی با ایرانی‌ها هستند که قبلاً هرگز اتفاق نیفتاده است، از جمله با سپاه پاسداران، در مورد انواع مختلف مشوق‌های اقتصادی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130188" target="_blank">📅 17:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130187">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
🔴
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
🔴
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130187" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130186">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کانال عبری: آمریکا ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن‌گوریون به درخواست اسرائیل خارج می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130186" target="_blank">📅 17:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130185">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130185" target="_blank">📅 16:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130184">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=u4i20CZWtp7J0q17Is-ACeBuedvX84b3Hor4rH3WY4mL_HAwICreffjOud6GF0ZwmqTd9BxHu-cneEjaLvPBAH397piDePonD9fhhni59GGQJJyy4Rs3SuumG5w-Qlym68IeRMVXqp6oolNjCEz_ZVxR8VusyXE-Y2fNPgBFFa2TAcxtU6VKBDGNqL2vIyADzUFUDbuuiH_mkU74sJvKxigtpZCFzbwEO_N8DR1iNJ718uRBktc-XsxZBhvU8JLmNOgpWhHuq5JNAPVjxAWct3SiZ5ReC_DmVjzCX7c1C77R1R-IGPvBqRcnPP7EKjsBE46Ag_UahAkp_jBpzUEF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=u4i20CZWtp7J0q17Is-ACeBuedvX84b3Hor4rH3WY4mL_HAwICreffjOud6GF0ZwmqTd9BxHu-cneEjaLvPBAH397piDePonD9fhhni59GGQJJyy4Rs3SuumG5w-Qlym68IeRMVXqp6oolNjCEz_ZVxR8VusyXE-Y2fNPgBFFa2TAcxtU6VKBDGNqL2vIyADzUFUDbuuiH_mkU74sJvKxigtpZCFzbwEO_N8DR1iNJ718uRBktc-XsxZBhvU8JLmNOgpWhHuq5JNAPVjxAWct3SiZ5ReC_DmVjzCX7c1C77R1R-IGPvBqRcnPP7EKjsBE46Ag_UahAkp_jBpzUEF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افزایش چشمگیر تردد در تنگه هرمز
🔴
بخش عمده این فعالیت‌ها شامل ۵۳ مورد ترافیک تجاری است و شناورهای کم‌ریسک بیشترین سهم تردد در این روز را به خود اختصاص داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130184" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130183">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdW8XPJKuELKEsqDiToS7ODZC_o-O13Ggi0m0y2ALY9ZjO21OrRknhDFxO1BCdSHk77YfmOHHG0_OV35ajXenlWqfgtszvqXysiLNH1hy1T98MkPwg54fvVZ7p88_9i2eZ2jDuBPkZkEntKtHGMPqKwyb2jkeYDUi00L0I8tLROIBS00efljB2c_O-4K_G3jUiZCefDmOXhkrKdILwpsvrEwOxxmH9NJty56jkswN1HEV3gbW5IVFO8EPymtOLRmNqUwis4tNM0NGfd5NPdAaFz8GebLdViQK0NVqUQAFJLT4h01J2XX0NQAWMSh2DxnFrjcr4WrB_Wk1-lX5ItrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه کپلر: تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است
🔴
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130183" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130182">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCk1tl0Njsx79B1U4iEirCnDoohy6vl6X7eFiXg49JQh3PWQMgAW_720NhA3XfPfwaFuoB5yjdMs924FnmHDBnu-0SGKjSVH-jrACRmXeyGpGXmbhiuu-LK_9zJvn0ltyC0nzTWyT-Y48E8zlC9msTrG-lsHrY_b5e6lAvO7uU4mfl1iGoZWbkg0KJW6LLYO2fDJXAMzp8-V5P2M35RnEwh0cybpmVZR4i2TWpLei_qm-yh1Iv2StwfiJUD4PnBqhqlim8w1Y6cu0AtBIyZGn_67KWMC6MJJMIB3-2wggk9gSvRCiMZOyaAzLwRd2oQI4O_J6AYLn08Kl-F9p8e9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی: هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130182" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130181">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وال استریت ژورنال : ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130181" target="_blank">📅 16:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130180">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
گزارش حملات هوایی اسرائیل به مناطق غربی غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130180" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: عمانی‌ها می‌گویند که طرفدار سیستم دریافت عوارض در تنگه هرمز نیستند
🔴
دریافت عوارض عملی نیست
🔴
اینکه ونس مستقیماً در موضوع ایران دخیل است، نشان از اهمیتی است که دولت ما به این مسئله داده
🔴
در جلسه با اعراب، موضوع صندوق بازسازی ایران مورد بحث قرار نگرفت
🔴
توافقی را میخواهیم که امنیت شرکای ما در منطقه خلیج فارس را تضعیف نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130179" target="_blank">📅 16:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130178">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هلند تیمی به ونزوئلا خواهد فرستاد و حدود ۲ میلیون یورو برای اعزام نیروهای نجات، سگ‌های جستجو و تجهیزات اختصاص خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130178" target="_blank">📅 16:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SLzJToHqUln7RKjWNl0umbGtnFiJ1w5f_cTqph-Q7Qwb4mBSPXIAirP9B3hhTgUscUB7TchcEwj9ESYzvBWtRlNG5MmBAhVsy8XW1nSnaAXkzk6uYGv0sMOfi2-BzMWooG_Qr8kkfop3PNSztGUPeTjRw6zhzlpT2EXykEi3O1ekQjAT-0RQ_k-B6HpBadjFPLfeLYC7jyZO89TopXyM8wDhwO2qVLQVV2whYUBLe0BrCysAJ1TD1ifzZ97VAiaunBlIfCksmq0rvlFRsaj58dzNUqspibDD5hISjcqeKXFKSdbjgmcbo4RJ-ZyEe0M1ZLk1lxHk9cq0ACcOTcnb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلطنت عمان بدون مشورت با ایران،  بیانیه‌ای صادر کرد و از ایجاد یک کریدور دریایی موقت در جنوب تنگه هرمز خبر داد(رنگ سبز)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130177" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROrkSXTKHEzUXB-K4ta4UVYYJqskuqKpmFaIekeR1UA-2_-rRc-0lfXpev0CtJZi2JwoZon7r-a6tkjjHpY4aBD9NMuJD4cFttZ2oLJpUHVDmwG91FJloSH6tLDeg5JWLRm1k8ciQVL0GvLZ8W2meUxh1NE-gZx1IAjSaazyRg_a-tYfWAeMP3gq0sfjvcgJFLUI8GEwFBB56urhbnpxOoGssR94FJI0buYgIXZp-XQG4rYotkXx6Y3qhqxs9898rwHjZCLxzk-zhZQXHs9mRz8p2sD1duwnADxtFHc_W5avvF1uov5hVbbqAvuN-SUyDDJTjgLy2Z8YEmP12k2njg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkhc3JDM47a1JcLGZX3IKOno8Rk25-TvIu6LgaFoU0AYVrPtqKWWEVjpOtea6kdhH5XmWGCPd0mIXOqhtV5roWrpLK5V_cVfAML9BzBlBJEDp5mO93gcdamC-QlQuczVsyFNmjnRqZ0Hwl0DGYvgqXQ6-CV07wyUz5PMqb9vhmZT0Ez-7A008FhPYZOskemu_pWyuvSAC4w2k2yjrfnSCpro9YpQfUo-q-V6F5cbw4QZvrWfpigGfQlS4ceH057ELE09UkmyPOLEKnVEiuE973WN2RxXZJkPETJUSYprkSk0Jt22XDAtgdvZzIyOGwc0eaj8suUm6zOoNrHYcJO_rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قبل و بعد از زلزله‌: لا گوایرا، ونزوئلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130175" target="_blank">📅 16:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQxXoAiRJxV_a11fMsFz9e9Q0y-aRORKvVlPM0b2n5ZWPBI9b2Slg5qxS0O6_efXt1jTgmm0BdtT-k2lm_XgQxIR0DsLRxqocDyNIrgZ0jyCq4JZjHqOJ3goyc3O0wb7WmGO7hj8Fx5zJl1VrVvPlhy-Ed9feiz2QnJsSO2kT6Idybh1eVpV39ipG9Ucna0byDbXPNGiloBFW5vd1X0Kv00KgZXzhC_8vLsQUZLU-rSpO10IXoDBZmQi3RVkwAlhysL60jebgE5V8GjJFm4IJMP-SoNGEiPlc6UnJg2aRcjmSGfPf1GxT9Fm6o7158Y4YSjzvmTMzSz3bQcBPBqjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: «آمریکا به دروغ ادعا می‌کند که دارایی‌های آزادشدهٔ ما برای خرید محصولات کشاورزی آن‌ها صرف خواهد شد. عجب!
🔴
تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!
🔴
این محصول [بی‌اعتمادی] کاملاً ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا فقط سویای تراریخته و وعده‌های عمل‌نشده و حرف‌های بی‌ارزش صادر می‌کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130174" target="_blank">📅 16:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
هشدار یمن به اسرائیل: هرگونه حماقتی با پاسخ سخت روبرو خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130173" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130172" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=N4c8aesBYPfPjUCw-7tCuEnmGBPk2Y8NqGe4pf4BkjriQOZRSINeb-2uccjhRhrtSh3nKN8Ry35CY5icP9C0z_bQy_e788SGYPOp75aDinF8vAGOJ2dJGaSwHessxBestSF-esNvQMR1rs6znPtKVrkzDBkaJWASc3rHFITRtefVlG3qQ4_zvHm-6GIRL_Mr0el8SLMt96Z_TG4kPwO9wBUgZbepQTBZ6cPo4laO8DjJZIeVwzPNVV1wgwZ-EdOOMfggv1N4BTzAjMYlpMf3g1zujuGOhs-CgnMKklSTATyLZz65JrADYWwsn3GbtV4hPBC5tAzLpOf55H5C2AO0_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=N4c8aesBYPfPjUCw-7tCuEnmGBPk2Y8NqGe4pf4BkjriQOZRSINeb-2uccjhRhrtSh3nKN8Ry35CY5icP9C0z_bQy_e788SGYPOp75aDinF8vAGOJ2dJGaSwHessxBestSF-esNvQMR1rs6znPtKVrkzDBkaJWASc3rHFITRtefVlG3qQ4_zvHm-6GIRL_Mr0el8SLMt96Z_TG4kPwO9wBUgZbepQTBZ6cPo4laO8DjJZIeVwzPNVV1wgwZ-EdOOMfggv1N4BTzAjMYlpMf3g1zujuGOhs-CgnMKklSTATyLZz65JrADYWwsn3GbtV4hPBC5tAzLpOf55H5C2AO0_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاشورا تسلیت
💔</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130171" target="_blank">📅 15:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
امروز عاشورا است روزی که حسین شهید شد، حسین اولین شخصی بود که علیه
حکومت مذهبی فاسد و نامشروع
قیام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130170" target="_blank">📅 15:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=SLcAeTWz_ypgMA8Q23EjmS3S63XirNs5TMfdnup08HQVhP_q13hbi5CkhEPGxZqPmQbkmz246Ff_IOhNPo9vIGR7zvHfbQPQ--1CPhCEiayf0hkKzLjwUiKau-ZZhBfAYd_jtULYfo55rSPr1uFZR4jWIIvMMAmo5hQyvC9wm66KP5-M_O9mb4K0k0qEUhD77wERSL4Pk09lCOqPtVTQ9FvkSIrxNpSxTxqrpiHAL2zTh_N8b1QFDqEpoYj7POKLB3iY4l3JGi7m6RBPQYXlI4qpYqxKyJriZ3gjORYuwd5lyqTLpuB6TImZwUnNMczqoSYWyguSzfAfpOCQMclFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=SLcAeTWz_ypgMA8Q23EjmS3S63XirNs5TMfdnup08HQVhP_q13hbi5CkhEPGxZqPmQbkmz246Ff_IOhNPo9vIGR7zvHfbQPQ--1CPhCEiayf0hkKzLjwUiKau-ZZhBfAYd_jtULYfo55rSPr1uFZR4jWIIvMMAmo5hQyvC9wm66KP5-M_O9mb4K0k0qEUhD77wERSL4Pk09lCOqPtVTQ9FvkSIrxNpSxTxqrpiHAL2zTh_N8b1QFDqEpoYj7POKLB3iY4l3JGi7m6RBPQYXlI4qpYqxKyJriZ3gjORYuwd5lyqTLpuB6TImZwUnNMczqoSYWyguSzfAfpOCQMclFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: اگر کشتی‌ها در حال حرکت باشند، ما به آن واکنش نشان خواهیم داد.
🔴
اگر کشتی‌ها حرکت نکنند، این نقض توافق است و ما با آن مشکل خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130169" target="_blank">📅 15:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه درباره عمان:
روابط ما با عمان خوب است.
🔴
آنها می‌گویند که طرفدار سیستم عوارض در هرمز نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130168" target="_blank">📅 15:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
روبیو: ما مراحل اجرای یادداشت تفاهم با ایران را با کشورهای خلیج فارس به اشتراک خواهیم گذاشت
🔴
به طور خاص، درمورد بند مربوط به پرداخت ۳۰۰ میلیارد دلار حرف خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130167" target="_blank">📅 15:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: اهرم تنگه هرمز کم اثر می‌شود؟
🔴
برخی معتقدند که خط لوله‌ها می‌توانند جایگزین کشتیرانی در تنگه شوند، اما بعضی دیگر در مورد این راهکار تردید دارند
🔴
فقط صلح با پیوندهای اقتصادی با ایران است که می‌تواند معضل را حل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130166" target="_blank">📅 15:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ونس: فروش جنگنده‌های اف-۳۵ به ترکیه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130165" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130164" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=cbZjEs90kcqKpys1nEjA_OfJMO4fjWXDN8IKhaYdOnaeKEiBno9LWe0T4OxgHXL0JOI75xgpkx2w6wO9FxhxQ1uIz8HE6PDkt5_n4DCGqOf-Ka4_QRhCVnvMxxws-W281A8beUjBzmYJ1pjWHW8v9m5ZctSvmX1yjZZekMcV66mdMPpxwWslll74fdK7FQ_mZ9cOatLRgAVymYyCVehJ4iJr_14_1dHfhyKmMik3dAD7J0cz9OjygHJKm6k2bJu4zvQXchvAX7Td1kgCO17dwYk6UBd4Hzfvt5lE4f6UkTKlYXzEpSfCZzFpe8dxq09K6CruXw5jB5DotINoXhD0Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=cbZjEs90kcqKpys1nEjA_OfJMO4fjWXDN8IKhaYdOnaeKEiBno9LWe0T4OxgHXL0JOI75xgpkx2w6wO9FxhxQ1uIz8HE6PDkt5_n4DCGqOf-Ka4_QRhCVnvMxxws-W281A8beUjBzmYJ1pjWHW8v9m5ZctSvmX1yjZZekMcV66mdMPpxwWslll74fdK7FQ_mZ9cOatLRgAVymYyCVehJ4iJr_14_1dHfhyKmMik3dAD7J0cz9OjygHJKm6k2bJu4zvQXchvAX7Td1kgCO17dwYk6UBd4Hzfvt5lE4f6UkTKlYXzEpSfCZzFpe8dxq09K6CruXw5jB5DotINoXhD0Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: آن‌ها افرادی در شاخه‌های سیاسی دارند که به نظر می‌رسد منعطف‌تر و مایل‌تر به همکاری با ما هستند.
🔴
آن‌هایی که با آن‌ها مذاکره می‌کنیم، همین افراد هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130163" target="_blank">📅 15:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdK9kQo7McqlNsnUxylJzNfuhtZZj_r3eKdKA3ar0tmsIpbgXZNXbgvUu77cYrz9xUNFpgT9e87ATuSBR8mjKPuM2SMonHn41_SKb1X2K7RAjrhXl6g6pDCsVNvS9R9zvRARXQidsZKOfTiGPfFcxutUMUGVSDb7rnLJ4sOw5ZmQZsRTvByEq5zUEozrO_5QqOLI90mCxGAwcUubZHXwRrtgUnnixcebwpFOxCigqrIRmJkV2lH1eO8oEfktSNoSAa8UVQOwluv5PeWwNTL0087esqP3Dj1IPYlkkr9B9Srn-z0bJFc1S0YYBMF12W9siCeAqvcUjiOPMkqM_F4SFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس آمریکا دو نفر را با کیفی پر از موادمخدر که روی آن نوشته شده بود "قطعاً این یه کیف پر از موادمخدر نیست" دستگیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130162" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
روبیو: با نیروهای نیابتی ایران صلح و ثباتی در منطقه وجود نخواهد داشت/ ایران با حمایت از حزب‌الله و حوثی‌ها در امور کشورها دخالت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130161" target="_blank">📅 15:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روبیو وزیرامور خارجه آمریکا: ما با کشورهای خلیج فارس در مورد موضوع ایجاد صندوق بازسازی برای ایران صحبت نکردیم‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130160" target="_blank">📅 15:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران از جبهه‌های مهم نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130159" target="_blank">📅 14:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و سلطنت عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130158" target="_blank">📅 14:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130157" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر نفت: امنیت غرب آسیا و ثبات انرژی جهان تنها با خروج بیگانگان از منطقه تامین می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130156" target="_blank">📅 14:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض عبور نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130155" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130154" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59328e354b.mp4?token=VK0BWcJtYI8yFeHgR7rOpQ5dEArrZYU-be9QwpQv1GUxpnsYCnfXxWhF6hgrIwwniriaiE_bfGPEOBaWj3CXMRQyJLnLQiDfxGBJxcqY_jhJRVrtYLxbTndCi2cIxd60252Fz64DESlctfApNz-0nhpvdfW5sZvpU2U9vJzFW6PA4BB_7yLQslxPGylNauQx-tyH7dcuGZYWIJwo7JPIPgOIpjluB73z1B7FjRgRvjKpEnw7o7dgyWlhBZ8v8YLGLcX4eYu5mI0mqifdKlWYgyj6bPiBuHxa5HEVMYsLt0O8VPIHjUrYkspKGwwlyu1x6_xejp8cqiylM9O10Y6Gtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59328e354b.mp4?token=VK0BWcJtYI8yFeHgR7rOpQ5dEArrZYU-be9QwpQv1GUxpnsYCnfXxWhF6hgrIwwniriaiE_bfGPEOBaWj3CXMRQyJLnLQiDfxGBJxcqY_jhJRVrtYLxbTndCi2cIxd60252Fz64DESlctfApNz-0nhpvdfW5sZvpU2U9vJzFW6PA4BB_7yLQslxPGylNauQx-tyH7dcuGZYWIJwo7JPIPgOIpjluB73z1B7FjRgRvjKpEnw7o7dgyWlhBZ8v8YLGLcX4eYu5mI0mqifdKlWYgyj6bPiBuHxa5HEVMYsLt0O8VPIHjUrYkspKGwwlyu1x6_xejp8cqiylM9O10Y6Gtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130153" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
منابع العربیه: توافق اصولی بین لبنان و اسرائیل بر سر «مناطق نمونه»
🔴
انتظار می‌رود امروز پس از دستیابی لبنان و اسرائیل به پیش‌نویس پیشرفته، «اعلام تمایل» صورت گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130152" target="_blank">📅 14:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سرویس اطلاعات خارجی روسیه اعلام کرد که غرب به اشتباه خویشتن‌داری روسیه را به عنوان ضعف تلقی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130151" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
حدود ۷۰ کشتی در ۳۶ ساعت گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130150" target="_blank">📅 13:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clrW9yO9bM6naE7skTW4lSaWsQuQEjPudYNltF59b_ojLUx3mUhLtrSQ_Viq6-i02Zx20OCMu7OcYlDwL8GFo2Tvd6i9rnKOFszLTaV11QCzlvZkdUNJ_eaeJC5S4BhugG2wt1sXDPKs_1si69SQamx-4k_FLD1rtjwZCDzGWSCDMgFLP4DFLAgqsoG-s-mjJ1KiameC-fljRS11hv8dlAbOFZ_nIRmXAYZyBAfRcf4BKpDXhMCKUPuSGlitAlFEvVvgMvO7es2SQmJj98IIZi9dh_Iaffn2BnEKZkjLfYf3KNNJ1obJMi0h7e59as5ZpzBAcrRNVw8ssXszXII66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده‌شده در یکی از تجمعات و حمله به مذاکره‌کنندگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130149" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
