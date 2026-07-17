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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 02:09:51</div>
<hr>

<div class="tg-post" id="msg-135226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/alonews/135226" target="_blank">📅 02:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💢
فووووری/تعداد زیادی هاورکرفت ارتش آمریکا به کشورهای حاشیه خلیج فارس منتقل شده و حمله زمینی هر لحظه نزدیکتر میشه
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/alonews/135225" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/امشب 3تا پل تو بندرعباس نابود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/135224" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری/به تونل شهید میرزایی بندرعباس هم‌حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/135223" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnAsvQYc6LYy1IepGhEfbNKfFVJlvcSSiETcGtv4XBEX5eFsUWknNizDzaKCDUKvpQSYaS9zPSdQL3qKQKuMPGA2rLFesDYGWob99DNLETOfJXBzQEwHeFxY-ByB8dMvXS5uYxI0lVht58smI9R0zb6c6obPoQshZovMWvRnTJIBRHal6rABtr3EwbyFJCNcgbqR4JwQdV_f-gCgsL_bMpqPgT9PnOEGn3YYqrBuf0V1jESA6LtBTnvmXdjVFAZ4dHxR2qUr6P_aJeLJwR59hbf72VVSudk0gUmuh6FtddkhDmwbOIBuWH0AyW3kLTai8_NEtldAa064qCHXNtYFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/پل مسیر بندرعباس/ رودان هدف قرار گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/135222" target="_blank">📅 01:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135221">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حملات به شهرهای جنوبی همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/135221" target="_blank">📅 01:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هرکی از این خایمال بدش میاد لایک‌کنه
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/135220" target="_blank">📅 01:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">ترامپ درباره قلعه نویی: اون مربی بزرگی هست و تنها مربی‌ای که نباخته
@AloSport</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135219" target="_blank">📅 01:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135218">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135218" target="_blank">📅 01:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135217">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بندرعباس برج رادیویی رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135217" target="_blank">📅 01:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135216">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5uIXqouGSYekamrILgUlqIndpcHLLeX_KPAq8XN1JB92c2t_TGe6r0hW9hnU8xP4iw1GEzkSbXFFSR66IMNurVBOk7DBBYoNMNXaQxY3SAnlTTS_fAzhAg9NnVicuJP-1UoauYbbhoKPd673WTOnTi3eZzbE-LwYyVC_3BZ9cppZXsLbKWpRtcuWWtwO4W_FukF7Oo41BGIZqVm69EWF-QuU3fUGrG6RfYyZnSkL7BQ5hDkHisIo2o6iNIu9ocSB2oK9TwC98Ozc7SA_rhy-gA06UGXUF3DKNZpVYrgNqt2KziQEdZMDdC1Lq46qfPM06pRmtEPAoxldnR0X1l4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه مادر جاویدنام سامان ابراهیم پور که پسرش ۱۹ دی ماه در رشت جاویدنام شد، بعد از ۶ ماه تحمل درد از دوری پسرش، امروز خودکشی کرد و به زندگیش پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135216" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135215">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/شنیده شدن صدای جنگنده در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135215" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135214">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/ سپاه:
دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135214" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135213">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار: به نظرتون کی قهرمان میشه؟
🔴
ترامپ:
به نظرم ایران نباید سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135213" target="_blank">📅 01:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135212">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CZMBOw7P4nhzp-nGU8m2nGKGMrhTkEcswyaJrg3hgx5pB1T1boTZsZ6W882q80muJp8Rdz9duuJmZmO7uEFMmSGDlIJ_C8bxDh8wTJNLZ_p3OuP8Hxr8uHeLi1GjOXaECIugW1vznH3OY-GkSv6FYs0o_L0Y7e4TDXtpV3ayeXGe0Cr5mU1oiLEj2gLfitys3SGjxF3BvGrwhiS9TTQTsir1tgEbgKX3aXN33DXJMSZBj_hr_MPa9zhAjKBazRtg54sKDR5zDPJWP58DyB5-U-iPZipixRAIUeeLA-3jX8P0gVRh1kdCaLD9nvYgEfd9AO6yXr3-zTjCDL9-l1ewNQgq31MhkS3dOTlJ-v6cV7OABmB2JWaULnUnjJnAcYaTsbfpmoQ85JZTbXabkn5RWbC7kSphElsFH8cMs75jOsrnx65v-PSFiswNhcxPZ7G4wXDeavxJt-YnX_LagsITQvtBf2xOMghUSsX4OEb-SN2qqj3yWZX_eVOFCLTu9dj7azb-PlfI3O_c9_FUcikyn9Zw5ZROAlOQia5P9xMPrLWs7Pdxa3KUm6c0rIQl5d4MReBS9LzfZ1qmMWe4GKIcQ25KokCF88ra1rFJ_Y21oGpJIDmD-oKXw5QuGJkrKPlql07C-k-Gq2C2co3YqShMZnbT2eY_biKeSUCwWGFIzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CZMBOw7P4nhzp-nGU8m2nGKGMrhTkEcswyaJrg3hgx5pB1T1boTZsZ6W882q80muJp8Rdz9duuJmZmO7uEFMmSGDlIJ_C8bxDh8wTJNLZ_p3OuP8Hxr8uHeLi1GjOXaECIugW1vznH3OY-GkSv6FYs0o_L0Y7e4TDXtpV3ayeXGe0Cr5mU1oiLEj2gLfitys3SGjxF3BvGrwhiS9TTQTsir1tgEbgKX3aXN33DXJMSZBj_hr_MPa9zhAjKBazRtg54sKDR5zDPJWP58DyB5-U-iPZipixRAIUeeLA-3jX8P0gVRh1kdCaLD9nvYgEfd9AO6yXr3-zTjCDL9-l1ewNQgq31MhkS3dOTlJ-v6cV7OABmB2JWaULnUnjJnAcYaTsbfpmoQ85JZTbXabkn5RWbC7kSphElsFH8cMs75jOsrnx65v-PSFiswNhcxPZ7G4wXDeavxJt-YnX_LagsITQvtBf2xOMghUSsX4OEb-SN2qqj3yWZX_eVOFCLTu9dj7azb-PlfI3O_c9_FUcikyn9Zw5ZROAlOQia5P9xMPrLWs7Pdxa3KUm6c0rIQl5d4MReBS9LzfZ1qmMWe4GKIcQ25KokCF88ra1rFJ_Y21oGpJIDmD-oKXw5QuGJkrKPlql07C-k-Gq2C2co3YqShMZnbT2eY_biKeSUCwWGFIzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیونل مسی
: مسی به‌خوبی مهار شده بود، اما ناگهان خودش را در سمت راست زمین پیدا کرد، در حالی که مدافع بزرگی که مأمور مهار او بود فقط همان‌جا ایستاده بود.
مسی ضربش را زد و همان گل، کار بازی را تمام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135212" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_h4DWnjr9OVlcYkowILBSh-n6d8zSotizpv23RS7HPaeUrdhJ-IIwwO_DbX76kbXCQUqWN9lpscqqSGfYRYpYnBrtQmiVxOLaXyRFFdzdHYseBBNaXzUcmLD79HvT1C93ZACwQqosgt4lticBU4otg8p7hdMRoiKCl8ubwlPMr1Tnphn3e1sV76OVIwSBBop3pURx-wpP79nzoMt60aVq_HIOXEziiHfgflxUKh6XgnRP3J-NgiQfmLekKjvIbqBPRTvP1_X93vyz608qX22w9ZcIbul3Jblw85w_ciQb-yZ3FDU302QxMwasonVnecTXdaVjo-3FGl00txOnfrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
بنظرم حق ماست که یکبار دیگه میزبان جام جهانی بشیم، ولی ایندفعه کانادا و مکزیک رو قاطی نکنید.
🔴
در عوض با چین میزبان مشترک بشیم؛ بین هر بازی یه سفر دلپذیر یک روزه بین دو کشور خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135211" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/حمله موشکی به داراب فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135210" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135209">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4df16a59.mp4?token=VYOmgM4UKvzDwJZcuRt0U0bzLafKWqVYQuS-2IWaCWUFEMsG2iRsCIe6OQ8sCUyep66UxXU7UsPv4V2oUGTwuczeN_PwnzIOdnyc6soPTkEf5IBUAj85mzLaI322xA_VQBAsEJDHYMFI2dWrH9ot0MmSqs7sj0xFb3Nb2GpoYop2EmQnU288DqE9jiEtY3j9o6E5_P0qXoEt0BDFCy3bmomPIcCz5-w-MnQfRTpahmreX24lK0_tWq8-fxLVDxLzVt2xpvd2DEqzum9bqkxfj-zaYeFEFMNtsXdxTCAUea4pcZPRP5K9TC-E66fy74hQ_EXIx_4S_DZE1AGL-GC1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4df16a59.mp4?token=VYOmgM4UKvzDwJZcuRt0U0bzLafKWqVYQuS-2IWaCWUFEMsG2iRsCIe6OQ8sCUyep66UxXU7UsPv4V2oUGTwuczeN_PwnzIOdnyc6soPTkEf5IBUAj85mzLaI322xA_VQBAsEJDHYMFI2dWrH9ot0MmSqs7sj0xFb3Nb2GpoYop2EmQnU288DqE9jiEtY3j9o6E5_P0qXoEt0BDFCy3bmomPIcCz5-w-MnQfRTpahmreX24lK0_tWq8-fxLVDxLzVt2xpvd2DEqzum9bqkxfj-zaYeFEFMNtsXdxTCAUea4pcZPRP5K9TC-E66fy74hQ_EXIx_4S_DZE1AGL-GC1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پلیس به جشن هواداران تروریست نساجی مازندران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/135209" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135208">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/حمله مجدد به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/135208" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135207">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KsvbQ4IZvEKiypftPan3lLx8TDJ8uIlL9tUEXgtwsAXA-xIP8WOIdJ2yn-BHPB9DlTY5F2laAUVOX-duAhAlJB-3Bayeo2OcaQKrC-o0VTN9opzX6Wqe12MFNztzRigRq-zfdFVMpCe5Lq58MSayJteMmZsjOBqvqULfsMN7Z6i9MnuWajqKJ7H1QvToiS52twpmVBKwsV2MxuMhtgzkkbDtW2USSYcug3JTag6Z1E_p-OM6xwPdxTG80Of4_ZovQAoYuBwzKm8we_cGjGFbsn_6A0DJbIsn58GvdQGAhSWghStkbfwpqMGAA5Ya7Ga49bngzuAf-KovyVl1qHHdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KsvbQ4IZvEKiypftPan3lLx8TDJ8uIlL9tUEXgtwsAXA-xIP8WOIdJ2yn-BHPB9DlTY5F2laAUVOX-duAhAlJB-3Bayeo2OcaQKrC-o0VTN9opzX6Wqe12MFNztzRigRq-zfdFVMpCe5Lq58MSayJteMmZsjOBqvqULfsMN7Z6i9MnuWajqKJ7H1QvToiS52twpmVBKwsV2MxuMhtgzkkbDtW2USSYcug3JTag6Z1E_p-OM6xwPdxTG80Of4_ZovQAoYuBwzKm8we_cGjGFbsn_6A0DJbIsn58GvdQGAhSWghStkbfwpqMGAA5Ya7Ga49bngzuAf-KovyVl1qHHdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/135207" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135206">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
به اربیل عراق حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/135206" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135205">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f5bfc22.mp4?token=bjJEM9XM_Mr7P95ca-5FR4hQi5RKi6m3SxOBWxRQ73p4r8r_VeSzS4k7WijBfHSIGLo--Ut8l5iuKVF_75IGUQI0MMKDcnz0v7Qd5AG5pPtBGXu9TMXj7nzqVAuQI6Btx7I4xaMvshhkFrzAtX1o204p-kkjDqear0fjNPLNwfD_zHFWWMh5NwssxEOqYzMTQ8eEAyuIQpginpwyAY5s1xY9eQM7kk4rl2krnFHa0P7mJiCSOI_nLg_8BpVgawaEJWoHyMtlJyUwB41SQKjAYJsFqa7keuuQDD1pMmVofPRL1n4YDYCT7JDN_5AcXYXQkvv_gtUr46ssEmwpKpmP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f5bfc22.mp4?token=bjJEM9XM_Mr7P95ca-5FR4hQi5RKi6m3SxOBWxRQ73p4r8r_VeSzS4k7WijBfHSIGLo--Ut8l5iuKVF_75IGUQI0MMKDcnz0v7Qd5AG5pPtBGXu9TMXj7nzqVAuQI6Btx7I4xaMvshhkFrzAtX1o204p-kkjDqear0fjNPLNwfD_zHFWWMh5NwssxEOqYzMTQ8eEAyuIQpginpwyAY5s1xY9eQM7kk4rl2krnFHa0P7mJiCSOI_nLg_8BpVgawaEJWoHyMtlJyUwB41SQKjAYJsFqa7keuuQDD1pMmVofPRL1n4YDYCT7JDN_5AcXYXQkvv_gtUr46ssEmwpKpmP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی سریال مختار از وضع فعلی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/135205" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135204">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ممد نبودی ببینی با گنده گوزی یه سریا جنوب هرشب زیر موشکه.....
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/135204" target="_blank">📅 01:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امشب بازم دارن جاده‌ها رو میزنن. اینبار حملات سنگین به جاده‌های جنوب غربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/135203" target="_blank">📅 01:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135202">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/به جاده اهواز_اندیمشک حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/135202" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135201">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💢
خبر فووووری/4000تفنگدار دیگه عازم خاورمیانه شدن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/135201" target="_blank">📅 01:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135200">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/برخی گزارشات خبر از هدف قرار گرفتن تیپ ۳۳ المهدی در جهرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/135200" target="_blank">📅 01:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/135199" target="_blank">📅 01:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گزارش‌ها از حمله به سایت موشکی یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/135198" target="_blank">📅 00:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ایران اینترنشنال:
یه گزارش محرمانه که برای دفتر پزشکیان تهیه شده نشون میده فقط ۹ درصد مردم ایران موافق ادامه وضع فعلی‌ هسنن.
۵۳ درصد خواهان اصلاحات اساسی
و ساختارین و بیش از ۱۹ درصد هم میخوان کل نظام سیاسی عوض بشه.
طبق این گزارش حدود ۶۴ درصد مردم دائماً عصبانین؛ ۸۱ درصد برای تأمین غذا مشکل دارن و اعتماد بخش بزرگی از جامعه به نهادهای حکومتی از بین رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/135197" target="_blank">📅 00:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/99d23f8757.mp4?token=GTUlQRVCZJAjG9O_17yL5DvC9-UimYe05LtRYJEQgnYHwBoPr-tnzK6FjIpy7V3XduTlPzSdXnWbR_UDN0AFDRsSLtV3izSIntg5vWu3PU0Do03qCoBDGsJqD3yZnmnetAdVpytLQzh6dtkImMeYi-qEEFggNisN6lwZ6e0G2zM_alzyQMIGy4xBkpC2Pim7gVZib_iiFXXOUVuRMrdU9KyUmAgvFxJ50X480X6_xDhzGAlg0Y-ThG6H1oc1m2RIGDgLLeqtZbAakUhOWPlPVK5YGD2dj7q7_a-_4HA-TVAG-BwajA0GZRfbBdpTZIPTArAH8n2ZrFTPShXotmySpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/99d23f8757.mp4?token=GTUlQRVCZJAjG9O_17yL5DvC9-UimYe05LtRYJEQgnYHwBoPr-tnzK6FjIpy7V3XduTlPzSdXnWbR_UDN0AFDRsSLtV3izSIntg5vWu3PU0Do03qCoBDGsJqD3yZnmnetAdVpytLQzh6dtkImMeYi-qEEFggNisN6lwZ6e0G2zM_alzyQMIGy4xBkpC2Pim7gVZib_iiFXXOUVuRMrdU9KyUmAgvFxJ50X480X6_xDhzGAlg0Y-ThG6H1oc1m2RIGDgLLeqtZbAakUhOWPlPVK5YGD2dj7q7_a-_4HA-TVAG-BwajA0GZRfbBdpTZIPTArAH8n2ZrFTPShXotmySpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/135196" target="_blank">📅 00:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl_U_k9rgs9a1XGwKEtJvO6b6YZlh16ZKY2VRgTvC_M6X8iEPXAtQIsIY_ob5iiWhlP0Waljy5dCSAnygZQZ7uHcjp0-wGJvKOMbOwo_Ft4QYOTV9K60NBQA_awDaFjUSQImHmd6gsglAoaMnC5OLPfq9OfgtfpK03O84Rz_9mQnXg-mXpd1SrDux512ZxpR_8NxSXtl3J0oOJwQJY7Lso01teFBDIC_07qe_G_hB_FGyqa4Tlem2UDW0hZLOYN2ijXsQUNS2nRPfgAh3jaM4LOFvHhdsZ7gKOK_LNro12lI_-RcH-RXWMwLtUGvkFm1_LRHqazfU2Fyrfi2GgP7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/135195" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
محسن رضایی: فعلا به دیپلماسی فرصت دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/135194" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
جنگ تقریبا به مرکز ایران رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/135193" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/۵ انفجار در یزد گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/135192" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135191">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/انفجار در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/135191" target="_blank">📅 00:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135190">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=Mq0pfv8eqLqLxkFMxUQo2IkuGR-DTYlZeF_sP7LgEVwM6bIjJiT72PD951TL8g_XHg9oL_jU3SAMV40p9WAHbKHXkwBgcugnV3sQFUzzUVB5_EUhDeR802vq1Ho8B0g1__o1ARVz8PyEbhVARWLyx4VPuBgt_gsX9DeLMbAJyOaUBk-XnvEL6gDelxD7A6ZNwRLxCAO2enHsjKnos_xNYfcesRiNfFDQ7oyASOBp-s2BVqYDlBKYjGsf9yLdcY77jOrYTISDKpTrkZskvHseIZQ2z7ONTwXPHA4Y_O6K-BpV_-UAgpSsFoo6mPbipnmLyheqvHFuHSq3QMdLKElqsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=Mq0pfv8eqLqLxkFMxUQo2IkuGR-DTYlZeF_sP7LgEVwM6bIjJiT72PD951TL8g_XHg9oL_jU3SAMV40p9WAHbKHXkwBgcugnV3sQFUzzUVB5_EUhDeR802vq1Ho8B0g1__o1ARVz8PyEbhVARWLyx4VPuBgt_gsX9DeLMbAJyOaUBk-XnvEL6gDelxD7A6ZNwRLxCAO2enHsjKnos_xNYfcesRiNfFDQ7oyASOBp-s2BVqYDlBKYjGsf9yLdcY77jOrYTISDKpTrkZskvHseIZQ2z7ONTwXPHA4Y_O6K-BpV_-UAgpSsFoo6mPbipnmLyheqvHFuHSq3QMdLKElqsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک آمریکایی به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/135190" target="_blank">📅 00:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
طرف داره با موشک تاماهاک و بمب‌های سنگین میزنه بعد یه سریا میگن پرتابه! مگه تفنگ ساچمه‌ای هست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/135189" target="_blank">📅 00:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYECPPcAx7GdiET_MJLVSbPRs0MLDqnVN34DQK59XdO-EyBoX1exGyq8KTvWsiuKjhIWyJhB5WlBYOJTsaT2hMxLFX8_CSPtWe3OUiHQQ6ZEAatwCJ7cRtKTjHld_9XVYKp-guPy6lDNI6S-c4obuiJmkq1bbmiGozuJJ6pg1hZ2i3BEC6rO0UYTG-e7jsZxHwGd9UQUvCa9hZNYyI2UmPKrXfhnfEfg5yn4mNXiIrFms2g8HhrCR4BiQ70iMcr1jJjWiIDkwHh3Ov4zkgBaUwR7ohKWzePuWVumuIwJMYl8Jrv5dXGV78qYq3HloZB_6YGQSFrzn4-uYqoNnznqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت عراق رسما مجوز فعالیت شرکت استارلینک در عراق را امضا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/135188" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به حوالی سیریک هیچ مصدوم و یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/135187" target="_blank">📅 00:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آمریکا هر شب داره بوشهر رو میزنه و فرماندار این شهر هم هر شب تکذیب میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135186" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9o7fXPbbwRfFfFj6LwpzbCOk2vqYFST8hgSZA4BfaMmjm8eYDOPWn1anOYRSG0Lej1uK2jPIb4PdI27GcEBW2KXAfL9hpLyQvyw7gDi_DR3v7-79PuXPaQNm2sXidOhKHjgoWg9GI6vY8kMVflYhDaOd6gTgE-15MWC-OGZVqi3y-Eja8XRkqOshwntlo816xMpO8A9-KPLrHFk7PZLUfe_BQGMoQy0VtXVsSYJyARWroQLqN-1mXpcgtHniJPQoX2DZQn9HSqkZhbYxTTVJ7-Xv79eksHjPSMY90QLZvSkMUfHa19AdOnHrvIDoOdeLurI2VH7rsG9dYXpeo0huQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZRpb27b5pOBD2gRj1f9zz54vS_WN1tucFpY--lew1Ps6yL6dUctnFKI4EorvvAujycGsSOEiUGi6Q4hevHDWrn4WNRAPwZJnToU-WxAursD1UTSi8LFvZMYs-pmhLcpz5wvuYzGassFvL3BdOie2W6yRmArT1grsxJAns9Ufm7nnzTb17WZuS9cdWGLhUI6yaL0Ka425ZLjoZxDW95JmbJpyyrwj6f42lWvHmoSPGYrTRz32sJky8TZ0nzGWPnsutpYv2hGHHoeMHfDZFL2ckMTS3H293atr7MM157elHVV55XNhRi3erytSZ_aMF9MINhz0v8smDpoqGLnpGu79g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکسی که با کپشن انفجار در اهواز تو رسانه ها داره پخش میشه فیک نیوزه
❌
عکس مربوط به غزه‌س
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135184" target="_blank">📅 00:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آمریکا از توافق عراق و سوریه برای بازسازی و احیای خط لوله انتقال نفت استقبال کرد؛ ظرفیت این خط لوله روزانه به دو میلیون بشکه در روز خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/135183" target="_blank">📅 00:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe4f4684a.mp4?token=uLNQOJb5di1JHPQbFs3quUxOSe4Jh7RiXvcFeF7aU7xBF4ntoLZ5OMdTwNlkaBuaEyOwXEa8AahyX5-X_UGwAWFF37BUFXPxhj8juryDAU1aj9Ui1DrPphtdYpvco5B994vx57lUQUGP1qaCF7gpnOr0lryayoj2HzbKDCtI7vQlMmPioQcHGOQrBW5QUzZ7njKRhP9wqfZmJXNS6-DIDtZxcy2ewQ84Iy2zDdhXaJwANiCxvdJBbueU70hLa8aIRFph_oHyFd-pEGL6FNq3QZ0DkB2qdmH4FOt71y-bF_UcCzZW-cxL-FfiBiOUvreBW0U93o8ud5692C3fHZiHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe4f4684a.mp4?token=uLNQOJb5di1JHPQbFs3quUxOSe4Jh7RiXvcFeF7aU7xBF4ntoLZ5OMdTwNlkaBuaEyOwXEa8AahyX5-X_UGwAWFF37BUFXPxhj8juryDAU1aj9Ui1DrPphtdYpvco5B994vx57lUQUGP1qaCF7gpnOr0lryayoj2HzbKDCtI7vQlMmPioQcHGOQrBW5QUzZ7njKRhP9wqfZmJXNS6-DIDtZxcy2ewQ84Iy2zDdhXaJwANiCxvdJBbueU70hLa8aIRFph_oHyFd-pEGL6FNq3QZ0DkB2qdmH4FOt71y-bF_UcCzZW-cxL-FfiBiOUvreBW0U93o8ud5692C3fHZiHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
دل‌تنگی دختر جاویدنام
#مجید_جمشیدی_گهروئی
برای پدرش.
🔴
لعنت به حکومت اسلامی، لعنت به نسل ۵۷ و لعنت به حرام زاده های حکومتی که چه به روزگار ما و بچه های این سرزمین  آوردن.</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/135182" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eLOalQj7S3RYFY62wwCrFR8WaVI1rSph2Y8FTy47Ta5ZGxGquZ8aeoFLkT0puLNLghgwAE5NU06p96fx6-Y2qzvh8mJmPbmGrfzNJdI6Y7Mfadk0s9K9oq5Sm2YkLcolgIhpBssnCHTVEB6Yl2_yV07eBEMcc7DmP_q1f_YRWAjlfMAkaYIM9ISJrQqcOAG2H1XeXKUkIItHUm4vtCPJsZdRcOd8TOyP-0l5DbK4a0l0Nqz8owyMMgbkuYNJHdRLJzEwfRAuN7jlqDx7Wc0nulsZCaZUXpF7xLJjlTzM_6ezOwIVjoRmh34GaFIKkpbPhbqiDKxgF6_8xJYbUaU5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی کنسرت جدید BTS، این شکلی یاد جاوید نام‌های ایران رو زنده نگه داشتن و به نمایش درآوردن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/135181" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚫
مشاهده برای زیر 18سال ممنوع!  ساسی عکس فوق العاده
🫦
از حضوز آرام همسر سپهر حیدری اسطوره پرسپولیس تو خونه خودش منتشر کرده
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/135180" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارش انفجار در لار، استان فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/135179" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDytmcqE3S0pISGsaUw68PsmBS8kuXp-aYxbpbDKD4eetDXbECSsXcLfgsHyLj4LVpTjXOPYOU4g8L4PnbFhgQwKo1bj65iOUH-8f489OlJz_b-AN_oQZNUBD7bgyfph7tO8QyHv6Bd_LKayr6yFju4gyvrZcG1Qf9yxZ5Bgzp7XlW3mOKq8i3MT8tfkCd82icrJr0ZMYgABkisC351s77ACmuAB-4CzKx3Q0nZJGPtXePQ_5qHf3tfqrCaoSyx-8WRxhnVTGej_1Q8jdE0QLmAnSubYoDXd8uKZ5mQVOGKCzqixUjf4du4Vm0-4yRiKNlWNIGG4VPuDCDLx3c70cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال:
آمریکا اگه زمینی بیاد، راه فرار نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135178" target="_blank">📅 00:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZadPHAc8zgzI_94OwcDyxheIYktSNdYmYEKPbMNJXUV8cuuFBCSACmNPeLYRI0qf41l7WjbGsLjf8kVmeS3S-uVvegVd_4vfDxoJMSfSZFiMfiSrruL-f-eFOc2NddTZlYCpqJ6YdpKk0diYnOyZ1iLlBfvJU6YqNVqk2Y7SwicwC6MdUI2SZ3DicMe1p5Iq83WSf_j-cdR5vlx6VO_OZUu8WeZY2sBa1DBE5gkAIvhs1Seeb6SdgaYQ4orcC00w0iNrlen0OePVfv0riUOkGN9ED5E93b93ZTiaBOOZL70k11jzD_unPbTnGH5SrYuQOz429QXictqd-FzHopqhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرکی از این خایمال بدش میاد لایک‌کنه
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/135177" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کوچی، رئیس کمیسیون عمران:
از این به بعد اگه ۱ پل مارو بزنن، ۲ تا پل ازشون میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/135176" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مهر:  شنیده شدن صدای انفجار در بوشهر، قشم و سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/135175" target="_blank">📅 23:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/سپاه خورموج و اهواز مورد هدف موشکی قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/135174" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دولت عراق مجوز فعالیت استارلینک تو این کشور رو رسما امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/135173" target="_blank">📅 23:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/135172" target="_blank">📅 23:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1133a3cb.mp4?token=Tg4MkRL2vit4vv7gsWI0Pa0hPXGQp6G5jWPyZimoq24S_9Ep3tFk-OCxBk2XVXycA2ID3kgD-rXNm7UlCXw7UGWRcCoNof36xBXa3pRfT5BlafI111R4sGlVCOH5zI5Fdm7L9P8O98DVepj5iOb9FobvSk6jSZG6sYk8VS9W46EW8rB_qkF_B3SAb1e-PhtiWGSHXsVyCSrkiNKZaH5GolSC7hGI2emfy57Ser3jBja22P6rVv2n-TJyC6vxWB0ICH9gLmL5jxOH3kIwQ7tp0v_JUmEAqx48ialdpDEhQLm6CCTDKu9_va23lYIJkDdIS-cCpDAhLOHlWwnnQ4yuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1133a3cb.mp4?token=Tg4MkRL2vit4vv7gsWI0Pa0hPXGQp6G5jWPyZimoq24S_9Ep3tFk-OCxBk2XVXycA2ID3kgD-rXNm7UlCXw7UGWRcCoNof36xBXa3pRfT5BlafI111R4sGlVCOH5zI5Fdm7L9P8O98DVepj5iOb9FobvSk6jSZG6sYk8VS9W46EW8rB_qkF_B3SAb1e-PhtiWGSHXsVyCSrkiNKZaH5GolSC7hGI2emfy57Ser3jBja22P6rVv2n-TJyC6vxWB0ICH9gLmL5jxOH3kIwQ7tp0v_JUmEAqx48ialdpDEhQLm6CCTDKu9_va23lYIJkDdIS-cCpDAhLOHlWwnnQ4yuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این چه سمی بود
😂
🔴
مجری شبکه خبر با شماره ایران زنگ زده به یه هتل تو عمان و مثلاً داره جاسوسی می‌کنه ببینه  چه خبره
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/135171" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/135170" target="_blank">📅 23:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135169">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRyAQFz9R4gikxWKI2JYAX2RLBOpjAKZwQut_7o0tND1OM5plOjY-GdJgZNS68y-5tFxd6XjlEngcdCMpgkT1aYmMjEnt8XpGD8tz1dH2Kb4rteOHXqM-SC691ZkkUVBygvlqRHsLctWCP5VYS7bKr6ZWQzzHmbIVZoPts-IyJ9n4Ci-dIiWdznWi7nBKKMPkt_gyHTZEYRonnSexOtlrZt_c9lVLsIPuZX8BVUaxf5Qw0STYGhO2Wv_CYmoUU9X96YDOf7W7dS7qPwyJGjABW4A7aK2Vdazz7AVCHFTK3p2858D3tOuuSNRArbci6LdN6a3YedH3yE4DEpY0imWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
مشاهده برای زیر 18سال ممنوع!
ساسی عکس فوق العاده
🫦
از حضوز آرام همسر سپهر حیدری اسطوره پرسپولیس تو خونه خودش منتشر کرده
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/135169" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135168">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/135168" target="_blank">📅 23:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135167">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/135167" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/135166" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135165" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
روسیه: تفاهمنامه میان آمریکا و ایران در آستانه فروپاشی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/135164" target="_blank">📅 23:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_lc5NXVHOEUI7SqehWFOpvScaKc4CX7KwZHnogdjxD_in2LEyR1hJm3Sp_ny3fz99wlIvskolDaME6Yvbpl8qrM4Orx_AL0GONQeeCUdwmyZvLW_nX54VTunolesQxoYELJ-bOixZibsIMA6sQMU08TE3wkUJZoqzjLGfXvPhTr7x-aSRmagnBeX1QbdmS38auLegweAtv0tUgvTOwbk_ZnYGzxG9kqwGsaQWYkPzozEXORpLVAoz1LVQOKyQuz_0dvP9oW_Nr6Yrob_FJloh8Ai95kL85F7myK-oEMd10bLixGWGB4OzfP74qPFuTdL4Yvz_vA2nBXF0LwOSP-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ سنت‌کام:
دور جدید حملات از الان شروع شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/135163" target="_blank">📅 23:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTiVlK4mgdheuGdouo9FcWm_7yz5Gn1gK3exknLVu6ORtM-TmxxAkJ9W6QFjf6Ohpp4sVxE5nNAMZYbU1AhFrOTXiyr9F8AQPmjUb_xcVezs-bxqkjC6djA4JLKwmg1CGe91aRoBNYliJqUExmxNalKD0N8rvbmxfuoOv3x00qeBi-KCAWfLa0iq2trhazznqXP2Tr8-coCJ3eacLPD3zA3BD6yyAut25kfRtNRpFHNjWaTRsTdPwFLgEcP6nKWqBsACj0OpOelsXYb618Fq1wfprA5k6nDLVC_Sw-8He3c7IJgmFuIN8dNu6B7NcazPE2yyBTrY2_ikd5xoJS2Lqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: باعث افتخارم بود که امروز دارلین گراهام نوردون، سناتور کنونی و خواهر سناتور فقید و بزرگ، لیندسی گراهام، از ایالت فوق‌العاده کارولینای جنوبی را در دفتر بیضی (کاخ سفید) میزبانی کنم.
ما سال‌هاست یکدیگر را می‌شناسیم. او فردی فوق‌العاده و یک میهن‌پرست واقعی آمریکاست.
🔴
لیندسی یکی از بزرگ‌ترین انسان‌ها و سناتورهایی بود که تاکنون شناخته‌ام و خواهرش نیز همان عشق عمیق او به کشورمان و ایالت کارولینای جنوبی را در دل دارد.
🔴
در جریان دیدارمان، از دارلین خواستم که برای منافع کشور، در انتخابات مقدماتی ویژه حزب جمهوری‌خواه برای کرسی سنای آمریکا که سه‌شنبه ۱۱ اوت ۲۰۲۶ برگزار می‌شود، نامزد شود.
🔴
امیدوارم این کار را انجام دهد، زیرا هیچ‌کس بهتر از او نمی‌تواند میراث برادر عزیزش، لیندسی، را زنده نگه دارد.
🔴
دارلین که از خانواده‌ای فوق‌العاده می‌آید، در تمام زندگی خود یک برنده بوده است.
اگر نامزدی را بپذیرد، از حمایت کامل و قاطع من در انتخابات ویژه سنای آمریکا در کارولینای جنوبی برخوردار خواهد بود.
دارلین، نامزد شو! بدو، دارلین، بدو!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/135162" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYydIOTKEYe_Doclmljf_KTgub_HQXFCJmV462emAIdcvBcjPXqlvjNPPH0s0WpWU1M2P5QV4lzOqwK78iDLwqqA_WYaG3qnGq-l5TR0RjoVQPGzrjSVMDhOoU2Jll7tsoP7uknWS7UeNV-eEQt1cVwdhFbSZRero6V5AYCUjPC7JUSoLfFMqlHkoo7SLY0mQlb19YTus2IywY1Wo_qGtdiO9ok-BHTwhYyg_GfdIPfXfnOH_hY0f5TJTJx8CwiOfk0h1HI-LzsbdyB6JfR1bQCQGUkfO7oEuBPYEjljlNtYN24mxbAmTw4fS9ToWqu7gb91M8zJHlG91AqEK3u1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: یکی بره ترامپ رو بکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135161" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
وجود شما حرام زاده های طرفدار حکومت تو خاک ایران از ورود سربازهای آمریکایی متجاوزگرانه تره!
🤔
کی داشت با وینچستر تو سر هم وطن های من شلیک میکرد؟</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135160" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPsMqkmSV49tikJstyFX7nS_gNFS24Fcxz0w5EqlSWwBCqxmMFTy4CCAFBJW3HxlPRTP5wGhggT06h4RTUhwrN4VD1a9knd5UPAh7GyvpQi7_w6A1Mai1V0YvCL7qWkCtkxFTL3_b5gIveIoF0KYvYOp5pBcBLjPlJUGYOE04_sUxoeTXUY-ro5G9m75oGAlOqsydeR6eH1JWDE7mUaA3f0sIThRDAhT9KgMO4NAPA9jl2tDmZhfiiHjxSlmqqNJ27mMWXnwfl0YpW5UKyBRwmdM8YgWAmMtJCi3HAJ8kiGk21Z4rwbVXJDPPPcIqHH8olfhbT5OEm0_3zHTKAK1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دبیر:
علی دایی برای مردم ایران عددی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/135159" target="_blank">📅 23:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9cwvAu-qpMGGZZPM5dY0PvUXNPgdUQ1z17U6Qhdfq4Aog19KEVMhmYoX7xZoFS9za1wyQrd0rbA5gh3VUc_JiYml8ECg3Z43eKKY7DNGGc-mnPpDl2NpaIcDuDn5Vwi-J9I2ZqdqpW7MNOq4LiPPbn0sa39_NDbHWFhepz-NUFICpWAbHo6XYdqvF0Uz4oCJPdvGu8Dnth78xhBHA9leDvTKhrzRJKf3mVvPm47wv8U8M5g-31RcxyF88viYjMNiWjdAaQmLmnicYZ5-nszgypsfj6gtxrmRkaVr__nV2NTAV7bbezDSrGy3qVzMW7UFHKLW8hkvuw0AUFSm0yvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیشرت ایمان صفا تو ختم مادر عمو پورنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/135158" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135157">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=lkNzNRb-TD_7KIqPLmFVtF1tNCvCPO9nl08fj159QjQFa_KXmBvJvzKsOSaoCc2y3h3QWejgOddeBErMaWpSHnFVIvQqSvsJFMxt1ukahxdJLDlkCFbd_szKQKc_7BBN26HZZrJP23V4QgdL5ro62FIRSBY5l9mU2JqEzsQZqEPYYv1j98SAokdU5zGXQrjMdiDXLf79geU9QTRkYm4c_kTK_QqOiiB7-3DASy8uLiTQEjN6i0zm68UrRL4CYE-4F2_7PBHR9ETk0XJ72FIRIilyZIkh7qjo_rszchJvm85A64AHiQlN3Sc7GdRWu3IdDosf1RsxawM_zk-0-XoEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=lkNzNRb-TD_7KIqPLmFVtF1tNCvCPO9nl08fj159QjQFa_KXmBvJvzKsOSaoCc2y3h3QWejgOddeBErMaWpSHnFVIvQqSvsJFMxt1ukahxdJLDlkCFbd_szKQKc_7BBN26HZZrJP23V4QgdL5ro62FIRSBY5l9mU2JqEzsQZqEPYYv1j98SAokdU5zGXQrjMdiDXLf79geU9QTRkYm4c_kTK_QqOiiB7-3DASy8uLiTQEjN6i0zm68UrRL4CYE-4F2_7PBHR9ETk0XJ72FIRIilyZIkh7qjo_rszchJvm85A64AHiQlN3Sc7GdRWu3IdDosf1RsxawM_zk-0-XoEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روابط عمومی ارتش:
ساعاتی پیش و در مرحله سیزدهم عملیات صاعقه،
سامانه موشکی  نیروی دریایی ارتش، با موشک کروز ساحل به دریا، شناور متخاصم دشمن متجاوز را در شمال اقیانوس هند، هدف قرار داد.
🔴
شلیک موشک کروز توسط نیروی دریایی ارتش موجب ایجاد رعب و وحشت دشمن و دور شدن شناور متخاصم از تیررس رزمندگان دلیر این نیرو شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/135157" target="_blank">📅 23:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135156">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99HLxpH5AgDMNgNtu9lLcgYxQkYy9LoKDbqJ2WVaNErkBaWlAtcExDBiAT5Pdmy_OjdXZLdZoT4wCdpbbd_djLdVi19uwToL0yIsl22kKqcB2_2bqnGrv-YGhEmsDBlkRMUJa0K1ojZV7D5lSLVNjjXwuNDeTcAWiAtsB1v_8hZL0t7i80xVeb4kvbPIe0oKICLrZcp-eX5-ZBmbTpjlKZRU_cG24WMh_i7FS33TLqrFn7ZbmjhlVzjnriBlvv0ALqy2VvCuibibcGQDP5E7R90IVq1M9kHP02d9cHIieXYPQ5VReNfh5K4WNGAGQ0iBzY83D8fgvGpE0piKAlC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دومین استوری بیرانوند علیه علی دایی !
علی دایی که با ترفند نخ نما شده‌ی سکوت، مدعی مردمی بودنه ولی چنان تیم ملی رو به باد انتقاد می‌گیره که انگار چه سوابق درخشانی تو مربیگری تیم ملی داره.
اون روش مذموم که علی دایی با لابی سیاسی مربی تیم ملی شد، هنوز از یاد کسی نرفته. ولی تنها مربی‌ای که به عربستان تو آزادی باخته، روی فراموش‌کاری ما حساب باز کرده.
این روزها که کشور مورد تجاوز آمریکا و اسراییل قرار گرفته، جایی واسه ادامه این بحث نیست، ولی دوست ندارم باور کنم تو میانه ی جنگ وجودی و میهنی علیه ایران، اسطوره مردمی (!) فقط نو نوروز نور رو بر تاریکی پیروز بدونه تا با این واژه‌ها، هم‌سُفره کسانی بشه که آرزوی بمباران ایران رو داشتن.
باور نمی کنم و حتما اینطور نیست، چون با ادعای مردم دوستی نمیشه در مقابل جنایت میناب و دنا و بمپور و کشته های جنگ تحمیلی سکوت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135156" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135155">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpiPbXb3KehxTLCFWfSnE1Ys_jToinImHPLbjZvlXuUNzOJx4UomcbgkJVR7kdpvxDb_AW_J6bWN7cDAl61dEIipm0rPv7obewIFqPw7j1fO87X1saB_1cEBcQlaGTeAl87d3a7_dmxm0NCrAeytKkHkdcRR15-hH0IIqPr6eixH6vt_KCv1LTfHAMpmLxAeScC5NAO4BJdDlHIScPJSnmooV0WA7yVLAWCz9K34naUGS82IcwjY7uQIPo9pNg3gM6U65ZZKuzfIkDzEJ2rJ4-R9IzA8V533YjHLZMrPsZNCmCGcxkcNhGKGRsodUAVFgxLU-WUn1Y-Su8NE6we2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری علیرضا بیرانوند درمورد حرف‌های علی دایی!
علی دایی که دوست داشتم همیشه بزرگوارانه حرف بزنه و با احترام ازش یاد کنم، تو مصاحبه با برنامه ای که عواملش واسه باخت تیم ملی در جام جهانی دست به دعا برداشته بودن، من رو مسخره و تحقیر کردن.
اینکه من به عنوان بازیکن بگم مجسمه مربی‌ام که واسه اولین بار تو جام جهانی نباخته رو بسازن، نشونه احترام و قدرشناسیه.
من که نه تبلیغات سیاسی کردم نه از رانتی استفاده کردم بلکه به عنوان پسر کارگری زحمت کش، بدون هیچ رانت و با تجربه‌هایی سخت نزدیک به 100 بازی ملی تو 3 جام جهانی و جام ملت‌ها به تیم ملی کشورم خدمت کردم. شایسته احترام هستم یا تحقیر؟
رانت‌خواری و فرصت طلبی رو همه زشت می‌دونیم ولی کاش تو خلوت هم اون کار دیگه رو نکنیم، کاش چهره ما واقعی باشه.. زشت یا زیبا اما واقعی...
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135155" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135154">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135154" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
وجود شما حرام زاده های طرفدار حکومت تو خاک ایران از ورود سربازهای آمریکایی متجاوزگرانه تره!
🤔
کی داشت با وینچستر تو سر هم وطن های من شلیک میکرد؟</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/135153" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
دشمنی "آیت الله BBC" از آغاز تاسیس تاکنون‌ با ایران و ایرانی</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/135152" target="_blank">📅 23:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قیمت هر لیتر بنزین در پاکستان به ۲۹۵ هزار تومان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/135151" target="_blank">📅 22:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14874af67.mp4?token=Fv-XzN_CBfTPUSv3wjsd-Sx9tBdJuIvV1Ji78IkBEcNxBYVaDEY4YmbVnncOBjKZJT4BSEnGOWbh85dcWhQMA0g18tUaVmAfCETkGBcTHiCKloo6jVFYSmfnqex2JCdOSKBo93Ak8D4TukL9tJhl6T0EbhzElSOCCGbPQP3uYo9Su1ewIj1N_BuZQdaoDXJ6VFhPwEd9cQckJ0GsQW9OMI7RPOjtcRGIDP7kgnKRF7YM8AAamZApznIPzetdIksr7xOmLwa45L4WhoMFz82w77AM2-VHRaWFlpscvS8PGq9M_16lIlToB-YpWpUJI1KbyNPx0fEteNO06cVVppNRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14874af67.mp4?token=Fv-XzN_CBfTPUSv3wjsd-Sx9tBdJuIvV1Ji78IkBEcNxBYVaDEY4YmbVnncOBjKZJT4BSEnGOWbh85dcWhQMA0g18tUaVmAfCETkGBcTHiCKloo6jVFYSmfnqex2JCdOSKBo93Ak8D4TukL9tJhl6T0EbhzElSOCCGbPQP3uYo9Su1ewIj1N_BuZQdaoDXJ6VFhPwEd9cQckJ0GsQW9OMI7RPOjtcRGIDP7kgnKRF7YM8AAamZApznIPzetdIksr7xOmLwa45L4WhoMFz82w77AM2-VHRaWFlpscvS8PGq9M_16lIlToB-YpWpUJI1KbyNPx0fEteNO06cVVppNRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع عراقی از حملات پهپادی در اربیل و فعال شدن سامانه پاتریوت مستقر در پایگاه آمریکا خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/135150" target="_blank">📅 22:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
معاون استاندار هرمزگان از فعالیت دستگاه‌های اجرایی این استان طی روز شنبه ۲۷ تیر ماه با ۵۰ درصد کارکنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/135149" target="_blank">📅 22:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وای نت: تاکنون بیش از ۶۰ هواپیمای سوخت‌رسان آمریکایی وارد اسرائیل شده‌اند که ۳۳ فروند از آنها در فرودگاه بن گوریون مستقر شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/135148" target="_blank">📅 22:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aea9b3cad.mp4?token=uuf8wdxsLXBdZtzqWrjL9Jq7TyFlWRM4NqBo50zDaEINHCxRuQWoklGJk0d3AzMparPeFK6svjMer45vEgRPhnurWsRqaJbnsXimS-mX5cci4l3m5D59DncvjOnNNvcCo-cVNcOTPrdGQ6fYgqa4S66dko__3tCxBuPAjsNLXMCg1M107Gwn9TT1IsT6d-M1IT4declZjPCaWOgARr4Phcqln3JBsNHI2uzjEZSJKjDo47XyHasYy0YgM-QekV2qZ3hKpSibPWcqeiiERgMi1FHsK3zOzDk4vz-SDGMrztKPUtQEXrBAr66chl0K9qwPiWj2RoUtiGhkNSkVbCr7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aea9b3cad.mp4?token=uuf8wdxsLXBdZtzqWrjL9Jq7TyFlWRM4NqBo50zDaEINHCxRuQWoklGJk0d3AzMparPeFK6svjMer45vEgRPhnurWsRqaJbnsXimS-mX5cci4l3m5D59DncvjOnNNvcCo-cVNcOTPrdGQ6fYgqa4S66dko__3tCxBuPAjsNLXMCg1M107Gwn9TT1IsT6d-M1IT4declZjPCaWOgARr4Phcqln3JBsNHI2uzjEZSJKjDo47XyHasYy0YgM-QekV2qZ3hKpSibPWcqeiiERgMi1FHsK3zOzDk4vz-SDGMrztKPUtQEXrBAr66chl0K9qwPiWj2RoUtiGhkNSkVbCr7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: اگر فرضا دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/135147" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فاکس نیوز: یک گزارش محرمانه که برای ریاست‌جمهوری ایران تهیه شده، نشان می‌دهد تنها ۹ درصد ایرانیان از حفظ وضع موجود حمایت می‌کنند؛ در حالی که نزدیک به سه‌چهارم مردم خواهان اصلاحات عمیق ساختاری یا تغییر کامل نظام سیاسی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135146" target="_blank">📅 22:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
🔴
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/135145" target="_blank">📅 22:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا مفاد تفاهمنامه را زیر پا گذاشت و از تفاهمنامه فقط یک اسم باقی مانده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/135144" target="_blank">📅 22:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZExUAXlb8ZxcDQsiolSczwbZFvFITHsPJNlm09EEFgwKXAAyKEqaLoml08oagwcuEzAQNSxKiYlOKJc2E48qoBd5jorIXji7KGpR-h5rDnNW28pcfBCsKC6urBcRii3qhTkjDOpX0pqbsjDB5V4Ec9hijVknpRWE-cFPbKdS_BEEbgoQNaGQ7JbnRDj6O7ni27DbGcq1vlcO8sGeAmy4s7Ech6UqUGYaz2ilggUG1gdziAlM1ZI7CP0FK5fgmd2sU3DHMEYWmFXvRDAjWF_M6H194bSDrvnRk1oM91RpMB3iI2R5OUbpNP1-N_XwCa9JevtUiXYJ7nj-b5Q0AAMOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ب
لند شدن پنج سوخت رسان از تل آویر به سمت خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/135143" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا مفاد تفاهمنامه را زیر پا گذاشت و از تفاهمنامه فقط یک اسم باقی مانده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/135142" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بیژن زنگنه در پرونده کرسنت از سوی قوه قضائیه تبرئه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/135141" target="_blank">📅 22:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پرس تی‌وی: هیچ پرتاپه‌ای به محوطه نیروگاه هسته‌ای بوشهر برخورد نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/135140" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPi7miaG7yoTcMKmBlnkRbsDsekY7mK2Udp88jUcdErExVdit87eH1_GweYxOpMR868aUQqi3WAIhOjZXA3Xa_hFMZc-JN-gYBP5j03DFlXUB7XYZpSctVBGVAHyBKeKlSo3TLBef-HrdIyiwKpwV7ROaW0riDz9S33rnk81-tfi2zt0h4fyS_-8IGIv3QgS0tSOf-4ZUouPv--DhSkjrRm3Io7bNYRJsRFlmxz_Z2pugQZ_vky5CKODFT8sp5T-y-dcQkoZZzt7KLljsHE2gf5ndGVwC0ETw9gsZghtEALUlvj28B805oNzWWhmKDuhGomAhHtP5MnvW4HE-1KFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: سه نفر از روستاییان هنگام عبور از پل بندر خمیر شهید شدن،اونا بیگناه بودن و ما هرگز اجازه نمیدیم خونشون هدر بره،ایران از جنوب تا شمال و از شرق تا غرب میهن ماست و ما تا آخرین نفس از هر وجب از خاک خود دفاع میکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/135139" target="_blank">📅 22:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAllw1zzlmePKKHyS-Cibl1_isC1ShR90QioSrmrbygXsSEfKEZU3VAO4fdbpKI-eV88QdncZXVLyjPja1inEqgJB0KyF5-JS9iQAeCDMTaybFt032Riecb4UcxcQZ449c2lA-TAVgSd1xnLOk_PE18Awi_SKjjcn4CJaaRh4XA7CNMK5fSCJ5SWv2ltC-84zqBfuZd-rmThhaTPc4tpTebt41N5-R0wjCKEBzn5TMGLPTwE6NhuZ5W8v61c68KtLQVsHGyJGJuk_nvoi0F5mjBWVpP53_rSbjupYCV22qNAz_3jdTITqCvlCKuWeMt4mAETcWcxeOxDEEZ5t6U0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا در ۱۵ روز گذشته در بحبوحه حملات مجدد به ایران بیش از ۲۰ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135138" target="_blank">📅 22:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سازمان آتش‌نشانی کویت از وقوع دو آتش‌سوزی در دو مکان در جنوب این کشور پس از حمله ایران خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135137" target="_blank">📅 21:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CayAZZyQi0zjl2Fkj1NitGQw3x4Az8Nyag_I1PPEXe3nb3Ij-gllk8VfNaS6v7aaxYjlPvMRbXaUkj86beKNYfTkoqBTSMW774POwrGQoF3_RLSSXB2q8rTggbEKREYlG0YqjlF60jwXUq0Z7GCnt-iXuAiblqkG1D1MzAxpRkUk_MJn2ONh0RoyieDf1GIWPdrqX32YgbfMlbd77uVA1WaJ4fAWTJ90OlwzzD8MCLY8sNMGD7hnw2cVzzSVgXFzZCPwvOPXzkf9RhhcDcirPhrr2JPnoWANZEhJXTxfQ-eEjM58ULiWpFB3NtATIVUNebObReRpCjiQ32dimsD9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت ۸۸ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/135136" target="_blank">📅 21:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هواشناسی: خودتون رو برای موج جدید گرما آماده کنید که نزدیکه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135135" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxzH28XvkrL-DQF0aM9yLIEcytutv9Xfb6YCFuvCBKDLYC8hA20_OthI0qsZRBRz-Zi58HMsRANq0iF7agg1Rdir4UOyYhpc43fnD5iBzQLyOZyUEMpvHm4EHNYdRmQtCbwU8Y033nNT8z1RZqjn1r5EuiVF0Wk2iDXXbG6orxIPEBTL8oYgvc_EMF_v1hodWceqOifm5AwSOVqQOd7tMh9UcxV1kyk6-WOLdf3EE4mlKAvafBlGp-vEh3cVz5ytD6IRn7SNZR_kE8NlORx_SxWLgzSYOOYPWC7BriMpay4Hwzp3vn6mi7fiXyvjIxCiBOPXXKkP35a-YfJKRbT9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین بورس آمریکا
🔴
با احتمال حمله سنگین آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135134" target="_blank">📅 21:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c089a5228.mp4?token=iZ0Zy3DoNacWMnD4Gqkr0q8KCgnRERNl8dkh88nJNu5ZfJe7gu_KXNrQ8SeEG0xinfco3G5FMMwVukgOTN_3vzXWqEwjjD6Ozaog2miVNin9HWEtTivD3972an3ggoZMa-z0RR4Z0vyEcj5dfoBr5B_QGup3OQspFyA8tLBxMgRizy7ChfBT9SO1zFVi8D2KECkVZ0p8HEnI0jsoOoBuE9agjdAZ3AMLf8lbKqfkC2NcI7Y8ZvDp4wXE_fX2Wwya0aVb6cRRkbZiRdO79zLCqSHQ6jFrOSm_OYZddi68Eqw33AdGoeX7dCg7KDLli9wxlRnbxbW4yJZTHksZnsWoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c089a5228.mp4?token=iZ0Zy3DoNacWMnD4Gqkr0q8KCgnRERNl8dkh88nJNu5ZfJe7gu_KXNrQ8SeEG0xinfco3G5FMMwVukgOTN_3vzXWqEwjjD6Ozaog2miVNin9HWEtTivD3972an3ggoZMa-z0RR4Z0vyEcj5dfoBr5B_QGup3OQspFyA8tLBxMgRizy7ChfBT9SO1zFVi8D2KECkVZ0p8HEnI0jsoOoBuE9agjdAZ3AMLf8lbKqfkC2NcI7Y8ZvDp4wXE_fX2Wwya0aVb6cRRkbZiRdO79zLCqSHQ6jFrOSm_OYZddi68Eqw33AdGoeX7dCg7KDLli9wxlRnbxbW4yJZTHksZnsWoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از حملات ایران، یک کوه به طور کامل در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135133" target="_blank">📅 21:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/621b16c793.mp4?token=Dn_GgJmbzLhbQUKuUKcYnpNraYMAFRwRDb5fTdL9vK1oxUguZOi9bQ4JU0v1-TQqMez15uwVn3KdMgBTTGr2HGHGnMaXbU8rUnoa3hBdRnLaXUyxcEvHTJZbGqKzWiVAxrrGdmlhdF-4c4j3K27RaE95ZAhhvbURIjaRdU2uO-VSG8LGZYspI4lzVoghU49Zb-MkzV29_xR2PMSu5uw3t82_etSi53c3m1jyhEUFBK17KQhxZZaxozw7cteq4NNrXF5nLEEKVO6uXtET-GfF0DTAFfD8J9AwhsVCv8OYH5nJVzzJsXYjyz8YcBc_HKD-YF4yS-2Qq34HPG8u9oqooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/621b16c793.mp4?token=Dn_GgJmbzLhbQUKuUKcYnpNraYMAFRwRDb5fTdL9vK1oxUguZOi9bQ4JU0v1-TQqMez15uwVn3KdMgBTTGr2HGHGnMaXbU8rUnoa3hBdRnLaXUyxcEvHTJZbGqKzWiVAxrrGdmlhdF-4c4j3K27RaE95ZAhhvbURIjaRdU2uO-VSG8LGZYspI4lzVoghU49Zb-MkzV29_xR2PMSu5uw3t82_etSi53c3m1jyhEUFBK17KQhxZZaxozw7cteq4NNrXF5nLEEKVO6uXtET-GfF0DTAFfD8J9AwhsVCv8OYH5nJVzzJsXYjyz8YcBc_HKD-YF4yS-2Qq34HPG8u9oqooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای ثانویه در استان سلیمانیه، کردستان عراق، به دنبال حملات پهپادهای ایرانی به انبارهای مهمات نیروهای مخالف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135132" target="_blank">📅 21:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bbc955ed29.mp4?token=sQZGssgirVaIiKuAxbCv1K7RlrOmfRQcj7JcXECNZb7LXPf8_Mm49WvUSOAWUEkvs6HH9w1-89G9_sPbweUs40PmSQobJYOJVC7u2WjK9BqFzoYNi6dSsoKM4GQeisaRC3IDjZaIbsGPnenhFRsHo5DRBIADftxFSsFRrRQZHpfRQu_23puf2bvHHyknTaP4tpdLM5UcTopzgxo0tyPD5LRYIl0oxYE-VfHjNFIWmBSUhrwsBiC9qTr_wiCPy6HRYmT7Ae-7Yv0kCyx_OdEr_L_Lb9if-Mque2vxGvRaz_8W4C2VtihKheegPIgNPihzlVtyFtIXvJzQ-3HHTWZ7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bbc955ed29.mp4?token=sQZGssgirVaIiKuAxbCv1K7RlrOmfRQcj7JcXECNZb7LXPf8_Mm49WvUSOAWUEkvs6HH9w1-89G9_sPbweUs40PmSQobJYOJVC7u2WjK9BqFzoYNi6dSsoKM4GQeisaRC3IDjZaIbsGPnenhFRsHo5DRBIADftxFSsFRrRQZHpfRQu_23puf2bvHHyknTaP4tpdLM5UcTopzgxo0tyPD5LRYIl0oxYE-VfHjNFIWmBSUhrwsBiC9qTr_wiCPy6HRYmT7Ae-7Yv0kCyx_OdEr_L_Lb9if-Mque2vxGvRaz_8W4C2VtihKheegPIgNPihzlVtyFtIXvJzQ-3HHTWZ7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به سلیمانیه، عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135130" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
انفجار مهیب در هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/135129" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تسنیم نوشت: امروز یک کشتی در تنگه هرمز مورد هدف قرار گرفت.
🔴
این کشتی با پرچم کشور تایلند بدون توجه به هشدارها و بدون اخذ مجوز از نیروی دریایی سپاه قصد داشت از تنگه هرمز عبور کند که با ممانعت نیروی دریایی سپاه مواجه شد و مورد هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/135128" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/135127" target="_blank">📅 21:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدای انفجارهایی در اربیل عراق شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135126" target="_blank">📅 20:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135125" target="_blank">📅 20:48 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
