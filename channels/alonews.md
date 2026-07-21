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
<img src="https://cdn4.telesco.pe/file/EPGMXoQXrC5-5zhiPjRnRPVhKyYXdgUulr1Kg31fkBaIE_ko5ovv-ODSrSomEqmS7THtdKPpyVPFlnR_VdcBguP7wo80E4HU1aIFu7kfMHwDhLJg6Yg3Sy3B-OGj_r9Kg6e_RITf5xalzLvvgojXaf9o9Q33rfiqxT2Yn6VFfcDRZayd4d1YjTPv0Irsn-ZjxgOKcCfgIvAYRaTmcdBJ8gmgb6EOqfXFsNalBYIIRN9IGB3Y8eb6qiLZ4iJrc6mq7Ge_cOSlEnKWwUWghcA7SakPR92ZJfY2Po7Gc5vm_71ug_f4jHYMfip22aNOAkpShy5pa-Nmn5LXSAD51nhnMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 01:26:36</div>
<hr>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvHbkLTvKVraKTdWHuJpQPvmdyabOuqtkTOQ0Gu2edc6fknHSXF_HyzTsZ4c52SoPZPsDKTWDq1-m4lmSI3Vu30I5sr6mUfv9lrLUsK9aFBLJshaQnrkb1uvabWoIKGwyQF8NJqvTfH5-6WyUovvK18l75LG94c_tTzQm9KPbgRG0zHO1rySg4oZlh2U5AuXra16JYDet_m-0c2KksiSHEoeFlFL4d6_yHhDrvHNi2bXdZBqKurN5D0GZTJDcFHCKyplM96EculrHGA3LvVQuzxxGeYuF4mTrTjn7ZVN4cyvvJgogtAD2zzcDAMQhjrH07ofak6kCs0dcECnyqiygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: دیپلماسی به پایان رسید، جنگ بن بست شکن است
🔴
هیچ ایده راهبردی وجود ندارد، احتمال حمله متجاوزانه دشمن به کوه کلنگ(تاسیسات صالحین) نطنز در ساعات و روزهای آینده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/136512" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طلا بخریم؟ نخریم؟</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/136511" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136510" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : من دنبال بمباران بی‌حساب نیستم
- می‌خوام بمب مناسب، در زمان مناسب استفاده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136509" target="_blank">📅 01:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O71v94k5NuUlcHWa8mtpd1xem9NRaPcS7r7oRUs7gYsVWKJFZ5XElfV-HUDQA21aHc2QF0931X44AE7dWgroCKJG1z3ok6BAJOhLRBwhgc-87ywZC0WNq18CcVMN4JmZrozTvr2HkpPO9X8fRqvA6qmRWV31eYigRMRbPygpveD3_efQ4ygRspqCR-7bVI4oO0O-A0oXvlyw4AwJvjeakpBGRUZGkCQy7BzGgXysUCQ5AS1AdlUJ6DeRoNUprosudFQvNsESsWP4wdc0kTodMoVqNL6oamVqHxXULqpVBpjocuyBKB3UkoUEkJRUmcU28IB1TFS6cPxNFkAZPn5Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تاسیسات اتمی کوه کلنگ با هزینه ساخت Nمیلیارد دلاری که بزودی نابود میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136508" target="_blank">📅 00:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما این جنگو شروع نکردیم، ایران 47 سال پیش این جنگو شروع کرد
🔴
پ.ن: ایران‌ نه! یه مشت عقب افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136507" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هگست :
- ما دیگه وارد جنگ‌های احمقانه نمی‌شیم و دنبال تغییر حکومت ایران هم نبودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/136506" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بیانیه قرارگاه خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به عنوان توسعه جنگ در منطقه می دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/136505" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💢
فوووری/۵۰ هواپیما سوخت رسان آمریکایی در اسراییل مستقر شدند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/136504" target="_blank">📅 00:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwM0n920otYpHMGm38kcB61dVRmICw-7u8TT7SFxKiSDxzbvFUga-oNbY301ANBZ2yxfr63-TGgj748su5QTYTdZ9nxx5cuxJhv-cNIG6i_7donUPZ5X3IkGOBDsXPpN3sBaFnhhiMOL0bRtEqNu-EcbqIqhQ5LIt7kkqWMJv4fYZcQ2LCerJrRmf63LQ_UUhCvpE9vezSHRGaCz7PWpsAuUF3uEgJoGFVnr-uJG70B5_gDHZ1EGEHdpBGfZBZGBekAMmfrznEAhfLnA8s4y7utGetqGfeK7uNlj98byo4PGFSb-MwCz8YDwogFr9zAzyhm_9DEdM2qWlYraGRM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136503" target="_blank">📅 00:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس: دولت پذیرفته است که فعلاً هیچ‌گونه اصلاح قیمتی در حوزه بنزین انجام نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/136502" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDqTR35M3tg6lO2x7a27eOkMSRPn0YgnjN6eJYlwWzRRgR3-G0Evdj2GlcxmkpWxwyFCjjIAuvssusD5Eywy3PmyqZkTZe8piDVjUcxIMCr74YTH_Q2pbU6xnAXpZofEoTHJgi7xnhm3VYlZ4Ev3REmzPx2He_UgzDbGlceFfiw1qX679zigsTm-fdHbQQ2Fhd3w0NhfVgbIn-L8uJndqEYJK4wb7jRlC5RHsvZm2tZ8L2NaKEbUcXR_exg54zULUEUpaQTmevjpujdIrO8I6w5PP6dY7UpJ3rG7Z5CaH8n77JWywujBKItCoQtww6gzKqlWC-WO2MPnYWztOWfUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۶ فروند هواپیمای KC-135R/T Stratotanker نیروی هوایی ایالات متحده بر فراز اسرائیل و اردن در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136501" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136500" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136499" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آه مردم ایران بد یقه جمهوری اسلامی رو گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/136498" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگست را قطع کردند، آنها می‌گویند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136497" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/136496" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما باید دونالد ترامپ رو بخاطر شجاعتش تحسین کنیم
🔴
اون نمیزاره گروه های افراطی اسلامی به سلاح هسته ای دست پیدا کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/136495" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما در حال حاضر محاصره‌ای مؤثر علیه تمام کشتی‌ها و بنادر ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/136494" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-2LgnMZBaaLEfu5ISeD4lAemUdXk2rBrHq35E8FRAABvsAKj6HeAaa0oAt2OrpjwRcFQokXCndd9OwNzWm0cAwVEli_N-zb_dv08RRToq7pJdehpzbZfF82ym1YhKsmHdmhFRt0JojwxBYCGLXHfSR6B_hCT5hHOee5D32gXrlZ6-5YYncsPOqCM61BimUwVDWJn_NUBFihf4HnBPlVnIEOZvHqxtQxrNg-vhPUJ8_YH49V05U0LHwZ1rjejd8PaD7QaL5mwO-SI9hCDsWoZa4GPBV1njAPeJGNmy3t9Y1g6qkSfwZdPstNcO455TjxCknpKFtdGOt1n3MRviSfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۷ درصد نفت جهان از تنگه هرمز، ۱۱ درصد از کانال سوئز و ۱۱ درصد از تنگه باب‌المندب عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136493" target="_blank">📅 23:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atvFK_kWTtlnfDh8kJIayreunHiXGhELeoOwdhnK2VDp4FV_rqv4tXwXbuIm8JZlHIF03qf-_za8o89FlB3_4GZH0WxsI1XjK4YXPJ3kis-U0cZxS53bdVJtDcXTRJavNCV7oU0yWJiX_tVZDdDy3ZTxXOQOhMKO4h2ZgzO9OlquZV5y1yf-fX7piaiEov3S8J1llkgDxln71iFNEV-qGrXjMt8rFKsYMdNWEnx96UK28g3T2nc_GH3UsPtt-47KvSxgTzA9dB940ODBeYqHq0kI71lgj_wr6ZJgl7dbE2wCKO5MeXv5lmsXKqeT5F_CUoMUE6ILIuOMxATx42P3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای E-3B Sentry AWACS آمریکا در آسمان عربستان سعودی
🔴
سعودی‌ها بارها مشارکت در حملات به ایران را تکذیب کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136492" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
هگست : جنگ در ایران برای آمریکا حدود ۳۷.۵ میلیارد دلار هزینه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136491" target="_blank">📅 23:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRzJGsKvbl1U66cHtf6HQVO7BueERNRSCotx5sLDjeuUoFheh9FNsGtJEf4p-EInqPJAeDegTarAQxOvpjPmuvjwTDSvhQvcO-zmR9VwL9ElOa-FCx_vmfxU77SzZcgYSJ4dnh3i2E1Yl8_kxP5vzfoCzntU03MOsmxJTG8Pmmr7knf59tLULBrgMjxcX1MaJ7VjbdtUKS9KHAq3eL8iQYzJbVRkaAJ1IqFUDZxZ8Qfk722suM6DVW19L2hx5nInq7RoraoWont-UESCbiJcw-Eo-VSOcZOsCzeWCcV8HGPitRev8_MTzjL2HzmH1_74Zd6ccGP-hVuCVpWZBqvlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
🔴
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
🔴
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
🔴
جنگ در ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔴
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
🔴
جنگ در ونزوئلا: ۱ روز، ۰ کشته.
🔴
درگیری نظامی در ایران: ۴ ماه، ۱۸ کشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/136490" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ:
ایران از نظر نظامی در ضعیف‌ترین نقطه‌ای قرار دارد که تا به حال داشته است.
🔴
من اذعان می‌کنم که آن‌ها همچنان از قابلیت‌هایی برخوردارند، بدون شک، اما میزان خساراتی که ما در طول این مجموعه عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین شرایطی قرار داده است که تا به حال تجربه کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/136489" target="_blank">📅 23:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ: پنتاگون دیگر توسط کارمندان دولتی اداره نمی‌شود؛ بلکه توسط نظامیان باتجربه و مدیران برجسته کسب‌وکار اداره می‌شود که این بخش را مانند یک شرکت اداره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/136488" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بحرین: هدف حمله جمهوری اسلامی به منامه سفارت اسرائیل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136487" target="_blank">📅 23:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / خبرگزاری کان اسرائیل: نیروهای احمد الشرع، رئیس جمهور سوریه، در حال آمادگی برای حمله به حزب الله لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/136486" target="_blank">📅 23:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136485">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvLz1kUwLsID-_eShgRlyIP3vbriLOx9JVPu8bfNWHYVgKxAPRNdhbu-I9Bbpu4UO2I9St0TNktPlOHoVwk9OaQ3hcfwFx8MxI7vLREvEWACHS45rCBN6V1hSR4u4g87Iw4Zq28RK6YV7L4OdiqPmgZpzxqpnYiRtPAUEGAe97BZQIEtPhueXZDVnd_UGXhgAfj1Sh97RB4u-fGEN2tazZvBNRodr1BbrjcMOlfa6VLLs64darQ2OPr9ScdNwlJ15qRcn1bj8BxXIvnEwK-XlAwz1VmYMMxxykrwcTkLYHf_FEKS0BCwQ97GhKsi-QlkgF3SBLY426i82JkuXhUdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرواز مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود
🔴
دونالد ترامپ اعلام کرد: «به دولت خود دستور داده‌ام که به همه شرکت‌های هواپیمایی آمریکایی اجازه دهد پروازهای مستقیم به لبنان را برقرار کنند تا شهروندان آمریکایی بتوانند به‌راحتی از این سرزمین زیبا دیدن کنند.»
🔴
او در ادامه ابراز امیدواری کرد که سایر کشورها نیز تصمیم مشابهی اتخاذ کنند و در پایان گفت: «از سفرتان لذت ببرید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136485" target="_blank">📅 23:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
منابع ایتایی: در صورت حمله به کوه کلنگ، ایران تاسیسات اتمی در نیوجرسی را هدف قرار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136484" target="_blank">📅 23:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yd9zJ2Ia0uKGQkLtNE1bzE8PDEcZoSV2_LxYoIU4TCa-0tQifO8J19_YkB4TmdrSE11sQCONFJpjbyLvssVzy6OSrWYi5tHCfbF33eZQIDagDnkW76nWbYiNZYwQisz0hLaFvoH0-lBlRMz15KhR4hGB69JZExD8KCErTCHixqkvF_gQhqltmqwDsG8toaq6kjIWkGQ-HdnGTTux_5gcgg4HGo4T8zJ2gMTBTNEiupgep4im23lFpaCtk5pWCgG_5tSdLyJAC9qBA0zSGsSYtUac0-A2wK1wtbjhzTZ9BXgf3IFV8tGKA7xw9sIoO1jfVNrgAeM4POUCLwlJ7fwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بعد از دیدار با رئیس جمهور لبنان، دستورالعملی صادر کردم که به موجب آن، به تمام شرکت‌های هواپیمایی آمریکایی اجازه داده می‌شود تا پروازهای مستقیم به لبنان داشته باشند تا مردم آمریکا از این سرزمین زیبا دیدن کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/136483" target="_blank">📅 23:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سپاه مدعی از کار انداختن چند رادار تاکتیکی در کویت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136482" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4wjZhpPhIjvafDpAcDuZJKsI10aBeqt9Q5eNfJBCbjOfa1OLm_B1dftRIN1jAy1n-dCLNK5KBOhOK_hFxQKln5w-rDQDzkEX375BMHfgNT2Dbi4rrtdJw3IN01LKJkfVXjmKTdafKkSrYfN0o8qhvoUDtLMkvwQJumocjQet-6vVaHi_KczY3HHcmzmrMJYBb04NrAv2oMRuPIaeS7ERqHDu0jgsyly4CSeMi9DwP56tX7E3R8YoSsik_w82rPyoJL1N3lnqZvCnLJUfABjfa3ylAZ4yBCjr8EfhNOeeA2IxC8Oi4PXe3FeHN9zMRza9iApBv6PZcAX0C-Y1gcoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136480" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/136479" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / نخست وزیر جدید بریتانیا با استفاده از خاک بریتانیا توسط آمریکا برای انجام حملات هوایی به ایران با استفاده از بمب‌افکن‌ها، موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/136478" target="_blank">📅 22:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
برخی منابع ادعا کردند که امشب آمریکا به کوه کلنگ حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/136477" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از پروازها تانکرهای سوخت رسان اسرائیلی برای اولین بار از زمان پایان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/136476" target="_blank">📅 22:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سپاه پاسداران، بلغارستان، یکی از اعضای ناتو را تهدید کرد و گفت در صورت اجازه بلغارستان به آمریکا برای انجام عملیات علیه ایران، این کشور را شریک جرم آمریکا دانسته و اقدامات لازم را انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/136474" target="_blank">📅 22:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / ادعای کانال ۱۴ اسرائیل: پرزیدنت ترامپ، گسترش دامنه عملیات علیه ایران را پس از حملات اخیر، اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/136473" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کویت سفیر ایران را احضار کرد
🔴
وزارت امور خارجه کویت : نفتکش «کیفان» عصر دوشنبه هنگام عبور از تنگه هرمز هدف قرار گرفته و در پی این حادثه چند نفر از خدمه آن زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/136472" target="_blank">📅 22:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yma0cWwvWPJj3lRtvwmNnA4pkCRaMPl9ijixu0t-lIvb9fzY3I2AxCooUtrwGeqavL86IcwMzxiyfExO4q0hWXQOH0NFbFDEf-lkng5jogUdOMp8sGUNHIY7wxmWm6WjE-bGpWcpJgwG9NN82y0rqkxQ5mLx8zNqaDYbJVsHIcBtMBp3mGrZk2_e20YA08b_gKDIb27tVQiGuus5zAtdu0lvVcE3lSAPGAp0q2MIfz17VIxjiPJdQn-XCznSgMnguvIvp_d1_yzvORNX7mkj-KPN0S4AEjPCe2d8a-yWempsrS9piyLWLZnke922juCglhZ4MJ_TMxtNOZe2QlYmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش i24NEWS می‌گوید که OpenAI در حال گسترش فعالیت‌های خود به اسرائیل از طریق ایجاد حضور در توسعه کسب‌وکار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/136471" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgHKrwTSgNH7gLiFzZfL0DTETIX3xNs9t1psBdVlAnEoHVz8SEpBi209UkPrAF0fAKWOYXb4ozM-l_eyTtFTcZHlAm8tQA4oPeM_7-e4_SqfMIbCkkQ9O-53aRg2As070v6vqNGZgNTq9mMZ_EHlZ4JntUY6hyFe6EnuYMYWLsqYYtOY4-ZbIcGVn8-zy2pe8h98b95JZew60rJShcMCwWgd_AGy4M1qJB9H2iy4cBJdh5jo7-P0pjc9_yHB_GOuxU4tIeD2pg5Idz9UEgzM4zPXh5VpJfRH5mGfb7GhgeocMo20tUX29NEJNl-7XB0zHg4LxTBD_huVuKngcjudDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲ تانکر سوخت رسان آمریکا از رومانی به سمت خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/136470" target="_blank">📅 22:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136469">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های دولتی عراق، فرودگاه بین‌المللی اربیل به دلیل حملات پهپادی ایران، به طور موقت فعالیت‌های خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/136469" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136468">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل در خبری فوری از وقوع حمله احتمالی در اطراف سفارت اسرائیل در پایتخت بحرین خبر داد
🔴
این شبکه مدعی شد گزارش‌های اولیه حاکی از آن است که سفارت اسرائیل در منامه هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/136468" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136467">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=BO0MK_fM9TAtZ6ggUf2-AxpKItbXJIRXOX1gEpaL8Q0Os63OuM1daNi1UfYbm4aSyLUj2fZMvMVOEdV8zMJsFoZ_ULOjr5e1sVW94Prc2UQ1y4vzG51__GeK42MOUXGubJp9Ivm991rM9ysbVDCUQOo-1vTIRJ_hITPH3F5Xsn53Iyoc9Os4_B0WNWhlT4ySLSy680QBV6Dxj8MZuHz4p35Znz-D4qHXTdo6DgxuoAaJ7rj4pQomjPxs1Ra-dm8huBFGfE8e8TaSuUd2dRU0XqMgeK91eBavQWZEm6TDR327cH2iQrxz1wGL0adtu1vfYXgbsQbgJRIsvve4Bizk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=BO0MK_fM9TAtZ6ggUf2-AxpKItbXJIRXOX1gEpaL8Q0Os63OuM1daNi1UfYbm4aSyLUj2fZMvMVOEdV8zMJsFoZ_ULOjr5e1sVW94Prc2UQ1y4vzG51__GeK42MOUXGubJp9Ivm991rM9ysbVDCUQOo-1vTIRJ_hITPH3F5Xsn53Iyoc9Os4_B0WNWhlT4ySLSy680QBV6Dxj8MZuHz4p35Znz-D4qHXTdo6DgxuoAaJ7rj4pQomjPxs1Ra-dm8huBFGfE8e8TaSuUd2dRU0XqMgeK91eBavQWZEm6TDR327cH2iQrxz1wGL0adtu1vfYXgbsQbgJRIsvve4Bizk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی شهر اربیل، واقع در شمال عراق، در پی سقوط پهپادهای ایرانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/136467" target="_blank">📅 21:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136466">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1fb8bd4c.mp4?token=MKW8YYCt3riOAtvRaL1bzSPGkEmjA5RHCDqWquB46Q_LhIn2HIAxtZlUKToOV5_Q1v4d-2bDR7x64WDiwpLT5DzJwGRIUvY5X1ti5Z6vECSdA8KQlayRtKw8dM1CfBzpc9itsbxVkN_Tm8O78gpFW25u2hvNUVO8DlQF33KqlM4-5Wg-6ydj-PQ8OJpoPUmBnyA5VVCGfjJm0__mdYLBNHehyJu3Ve54T-3vSNfHassOY-MYLOWndpQehfEBBDU3El-ymCrKYntGeNdYx9VQxfFnNZXjo-j-s5UdMiNAC1675QpXICD_mnQYKO9jxJLrf0DMxZDDGjagJfx0YLXjJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1fb8bd4c.mp4?token=MKW8YYCt3riOAtvRaL1bzSPGkEmjA5RHCDqWquB46Q_LhIn2HIAxtZlUKToOV5_Q1v4d-2bDR7x64WDiwpLT5DzJwGRIUvY5X1ti5Z6vECSdA8KQlayRtKw8dM1CfBzpc9itsbxVkN_Tm8O78gpFW25u2hvNUVO8DlQF33KqlM4-5Wg-6ydj-PQ8OJpoPUmBnyA5VVCGfjJm0__mdYLBNHehyJu3Ve54T-3vSNfHassOY-MYLOWndpQehfEBBDU3El-ymCrKYntGeNdYx9VQxfFnNZXjo-j-s5UdMiNAC1675QpXICD_mnQYKO9jxJLrf0DMxZDDGjagJfx0YLXjJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های انتحاری در حال حاضر در آسمان اربیل در جریان هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136466" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136465">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8d1b726c.mp4?token=YHeHsQ5y53fMrybMuJrtmNPTT-4ew0W471KzN62SmvlB-qvkyxVi1fnXBKD0PWFo5lgs8qDMfLbszMJX-tZyr43duyErhkeukCjp0gYj-POZxIarnEQEIeEIxherDJQULbKLMnmxoUahBGnhPsos6VjYG9MYJFepC_71sqX45n0kW6pmiFDux_oVv5-vZJtCEavl7G0OtOCH-xf_XFkJw7ZEnLu3oagLoFQKWfszUU7gezhVedxM9Tx-g4YARmxtDOmsIV2Nk3Jn901762WNgpchInZ32m3cp9dwHZ5KL-wJ8xhdszx9X97lrnqXGWFwb4nqOpmoFZiJ2QQJzIIHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8d1b726c.mp4?token=YHeHsQ5y53fMrybMuJrtmNPTT-4ew0W471KzN62SmvlB-qvkyxVi1fnXBKD0PWFo5lgs8qDMfLbszMJX-tZyr43duyErhkeukCjp0gYj-POZxIarnEQEIeEIxherDJQULbKLMnmxoUahBGnhPsos6VjYG9MYJFepC_71sqX45n0kW6pmiFDux_oVv5-vZJtCEavl7G0OtOCH-xf_XFkJw7ZEnLu3oagLoFQKWfszUU7gezhVedxM9Tx-g4YARmxtDOmsIV2Nk3Jn901762WNgpchInZ32m3cp9dwHZ5KL-wJ8xhdszx9X97lrnqXGWFwb4nqOpmoFZiJ2QQJzIIHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان اربیل‌عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136465" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136464">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فرودگاه بین‌المللی اربیل بسته شد
🔴
منابع عراقی گزارش دادند بر اثر حملات موشکی و پهپادی اخیر در اقلیم کردستان عراق، فرودگاه بین‌المللی اربیل بسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/136464" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhqeZL2uQXLmajz0gPs8DOw2nAbXVIemzUlXAHaQnYx9n79vJJSaxRSPCfjNBJn1JxXBFnIl2vJpZ3Y20MQwT5uWgFIBzkvw74cAjvSB-CVViK0XtoAaz-faBpxliz3iPMqygxID_7r-VWCgVpuS0uHOq81DrJPvCA-NvYaBegcqictJNRg7bydmvWILsO_zKePY1POjJfvmGIcL-3PH_QxbK42SS8iYS8_IHNd_imoyNAY1-40-5p1hJ7AwK2fysjAgHVPRbIZO_7iW9-piyKZwDx-ky0rLTRzToGMwHKquqNTSVN_g8hKFqmjntEUuQ-x7Y1MjcMMZrqihhhpdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد رآکتورهای هسته‌ای فعال در کشورهای مختلف جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/136463" target="_blank">📅 21:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136462">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136462" target="_blank">📅 21:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136461">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی گزارش داد که سه پهپاد حامل مواد منفجره در نزدیکی کنسولگری آمریکا در اربیل، شمال عراق، سرنگون شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136461" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0e9aeb4d.mp4?token=ibwDyDcenBz-2BIi_UgCeeec8_x5yC72Q4bEw-Xbh8wYk1-fgtjp_emqW_Uq4biB-UpPiWYMRggcQ5fIyuKSMqhHJoieI7UOOGxL7LUKlKIm28JWfi2GZ_OGC-Q4zqcyfq3IcK4B7PCJkDm_ktOdI84DDnEquwADki4X2OdV5DJgvXifwgg11EVXRFrX2JG60ujZI8LSaSWALDk81kSQUzj91044liJ1yeg8MJCM9jnrk2dQk2wjRnejeFJKrzswAfGNBRHZk-NQp-RwAMrZdTl-ogbMV_YgZdd75npWA8KXr7gkqnuN7Y8ZSiifGGpA5somOT4r-zUCCs0TtVFMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0e9aeb4d.mp4?token=ibwDyDcenBz-2BIi_UgCeeec8_x5yC72Q4bEw-Xbh8wYk1-fgtjp_emqW_Uq4biB-UpPiWYMRggcQ5fIyuKSMqhHJoieI7UOOGxL7LUKlKIm28JWfi2GZ_OGC-Q4zqcyfq3IcK4B7PCJkDm_ktOdI84DDnEquwADki4X2OdV5DJgvXifwgg11EVXRFrX2JG60ujZI8LSaSWALDk81kSQUzj91044liJ1yeg8MJCM9jnrk2dQk2wjRnejeFJKrzswAfGNBRHZk-NQp-RwAMrZdTl-ogbMV_YgZdd75npWA8KXr7gkqnuN7Y8ZSiifGGpA5somOT4r-zUCCs0TtVFMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از رهگیری پهپادها در آسمان اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136459" target="_blank">📅 21:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بلند شدن ستونی از دود در پایتخت بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/136458" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f99c9d3d0.mp4?token=kyNwiMERP4nckc21djojBi3StYoIPf2nRFxCO7YZlVn_FywI7ryA7lXeRIM-9E0LN6UK4ZF6fgoQXukJ3671p9ktPchscodo6K6-9IhklKadRprBL20_3c1StN2bW04eB0SX-LgjsGEDr-mGLXIu5-jlB5SYaWgPmEjDAfmUVOLOe4XhF4ShSFaFcYMC2JE-pUrEfuImv6JXcXq159UgUQUKNz7BK-oHWAv_uENGRHlROmfQaEhBHfxVz77GEq7afekvoOKxM019ejInFys5ySoePr6p_BhwJv4I1pTerAKqTvLaq5NGFxue6urqbvTD4zs3usD_sth8jGYgNCQPRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f99c9d3d0.mp4?token=kyNwiMERP4nckc21djojBi3StYoIPf2nRFxCO7YZlVn_FywI7ryA7lXeRIM-9E0LN6UK4ZF6fgoQXukJ3671p9ktPchscodo6K6-9IhklKadRprBL20_3c1StN2bW04eB0SX-LgjsGEDr-mGLXIu5-jlB5SYaWgPmEjDAfmUVOLOe4XhF4ShSFaFcYMC2JE-pUrEfuImv6JXcXq159UgUQUKNz7BK-oHWAv_uENGRHlROmfQaEhBHfxVz77GEq7afekvoOKxM019ejInFys5ySoePr6p_BhwJv4I1pTerAKqTvLaq5NGFxue6urqbvTD4zs3usD_sth8jGYgNCQPRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلند شدن ستونی از دود در پایتخت بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136457" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136456" target="_blank">📅 21:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZb6aP1w47Jiw_Fi0oxJ1rz-3TulT5lJxvGvBOWVHjbWGei75j9Qx-nzM7doqgSykcEMX-VzkPOBGUPml3f8DMQpNUJ7dZ-WKCAbk-qT7HCKf-h0wCEmCYtn5l30O7OZOzRvyKPWi8L__bFbDZO3uvbCGB2DMFy5CB8jcNKEAZtBvNVWFwOM7rZxkfZ34Nj9Q6KpMZ5LaeV2PW5JtBhj8yOrIcBNvTmjJLFpcyG30S3jvSA2ffBbeUYnq9PuNnKMuLDyratT3MKJV36qptvEUzN60kdsEDRnT5wRAuijsgCzmxNjF1fmwez2YEU0f54begZNYWAz7TXiRfWutkd13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت سیاوش اردلان، خبرنگار BBC: ابتدا همه فکر می‌کردند حملات اخیر امریکا مقدمه حمله زمینی است ولی نتیجه ضربات ایران نشان می‌دهد امریکا باز هم بدون برنامه وارد عمل شده؛ یک مقام نظامی آمریکا می‌گوید ما قابلیت دفاعیمان در برابر موشک‌های ایران مستهلک شده اما کاخ سفید به حرف ما گوش نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136455" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l83jJbXMeMTzAyBi45P0dHjrD23hcndKQdUgQsMx7l9LCW93G0YzZ1F4PuljKNfY1kpv7gwZPGq-ibmKRzdLEro1076kRc3U21-YM3z7JjMu2TLHE6BYfYI1_PWavxUOJF4DQT4DDp9pWlXek_rvAz_C861z_9DKB-SIGAJaw53j2AQly5wUYSVfIH6d4I8CNKA8OAUrozuBhq_dqHmSAhsaIlkKctdZR2pqcAdamPE4Q4UZG8G63dpTSKyYlp9kZQz6fsF4hWtTGOxL9Vk4MY6BboRH59WqB88JvyjWAKRyTomUdpaXWnl38IMkh-sAlxjCQSjpR_L23GGRDx3L7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش سوزی وسیع در کوه دراک، شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136454" target="_blank">📅 21:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f59fef3ee3.mp4?token=O0BYUGlvkD589R-vNngxJu7g4-gvvYwKEK2ncz2B2yLQKo2w7Rd1m4umvOsWv0bn1kNlDTIEJAIGoonZoDACmLE105gBSm8_RJMraQLuMPFdWkBqYbjCXyfSBrI9aaGbmgaLhK5b7AyIixnV2l3qXEZV3GEF_p9VkxvjkkqtqWWxg_FW0bRY8TesEdsy8mTMQVaRp-ofQOb1m7hViba3XHrCH1W-30BV2_L_1rkNfqEfwsJuh6gYNaa-49xUnwdcyOnrlXsTpd8HFl5IEEiEv5eDwgrH4aLF1KnM8mK_WxIvsqk82qNZGSk-wu_fs74L4bN8TvM_zvPiMcCe9kfxDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f59fef3ee3.mp4?token=O0BYUGlvkD589R-vNngxJu7g4-gvvYwKEK2ncz2B2yLQKo2w7Rd1m4umvOsWv0bn1kNlDTIEJAIGoonZoDACmLE105gBSm8_RJMraQLuMPFdWkBqYbjCXyfSBrI9aaGbmgaLhK5b7AyIixnV2l3qXEZV3GEF_p9VkxvjkkqtqWWxg_FW0bRY8TesEdsy8mTMQVaRp-ofQOb1m7hViba3XHrCH1W-30BV2_L_1rkNfqEfwsJuh6gYNaa-49xUnwdcyOnrlXsTpd8HFl5IEEiEv5eDwgrH4aLF1KnM8mK_WxIvsqk82qNZGSk-wu_fs74L4bN8TvM_zvPiMcCe9kfxDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136453" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136452" target="_blank">📅 20:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۳ ریشتر شامگاه سه‌شنبه ۳۰ تیرماه، حوالی تازه‌آباد در استان کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/136451" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون مجلس : آمریکایی‌ها جرعتِ مقابل مستقیم با مارو ندارن، فقط هیکل گنده دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136450" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل: برآوردها در اسرائیل حاکی از آن است که دونالد ترامپ به‌زودی حملات علیه ایران را به‌طور چشمگیری تشدید خواهد کرد.
🔴
به گفته این ارزیابی، هدف قرار دادن زیرساخت‌های حیاتی و مقامات ارشد ایرانی، می‌تواند ایران را به واکنش نظامی و شلیک موشک به سمت اسرائیل وادار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/136449" target="_blank">📅 20:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حمله اسرائیل به شهر المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136448" target="_blank">📅 20:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارشگر کانال ۱۱ عبری: گزارش‌هایی از منابع غیررسمی در عراق حاکی از آن است که سه فروند هلیکوپتر آمریکایی نیروهایی را در صحرای البادیه در عراق پیاده کردند. پس از حدود یک ساعت، این هلیکوپترها دوباره به پرواز درآمدند و به سمت اردن حرکت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136447" target="_blank">📅 20:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حزب‌الله تهدید کرد که در صورت عدم اجازه فرود هواپیماهای ایرانی، فرودگاه بیروت را تعطیل خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136446" target="_blank">📅 20:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70432ee662.mp4?token=jZL5oI-jhLfLE6FJv7M86d4UsOJfaSTgF2-GeCLFlQXKF-Yav4owZX_UwMY6YnKuQnuyEJjmkiGe_zHQuOKDHggzm_qiXaV_j8eBlh4LKrmv3tgx6NJasRS7VxAop_SRkDroPTxuEdsi3_zTlCQqG9vNZfQ6Qlv5JJPusSbDjTZq-Lmujzih8lj0pQ41lh6YJcS0eioCZ6AP0paLCjP61K0Msg3ZaOmq1fCRyeBNOcfoUxCHBqIx_QGfM7w-ELLwxrKG_5MKRHGdhytRdCOgMCFAHkWg76EA_bMmGyYFwOetjYZ7VGGxBFzhpAru_eKbpUmurdVnagXNchrHF1xjLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70432ee662.mp4?token=jZL5oI-jhLfLE6FJv7M86d4UsOJfaSTgF2-GeCLFlQXKF-Yav4owZX_UwMY6YnKuQnuyEJjmkiGe_zHQuOKDHggzm_qiXaV_j8eBlh4LKrmv3tgx6NJasRS7VxAop_SRkDroPTxuEdsi3_zTlCQqG9vNZfQ6Qlv5JJPusSbDjTZq-Lmujzih8lj0pQ41lh6YJcS0eioCZ6AP0paLCjP61K0Msg3ZaOmq1fCRyeBNOcfoUxCHBqIx_QGfM7w-ELLwxrKG_5MKRHGdhytRdCOgMCFAHkWg76EA_bMmGyYFwOetjYZ7VGGxBFzhpAru_eKbpUmurdVnagXNchrHF1xjLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: ایران فرصت‌های فراوانی برای مذاکره داشته است، تا نشان دهد که در مورد تنگه هرمز رویکردی منطقی دارد.
🔴
اما اگر ایران به حمل و نقل تجاری حمله کند، ما نیز به آن‌ها پاسخ خواهیم داد، همانطور که رئیس‌جمهور گفته است، ده برابر قوی‌تر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136445" target="_blank">📅 20:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / تعدادی از بمب‌افکن‌های آمریکایی B-1 هم‌زمان با اظهارات ترامپ درباره هدف قرار دادن کوه «کلنگ» در ایران، بریتانیا را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/136444" target="_blank">📅 20:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
توی همدان، بعد از شکست مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و فوت شد:// @AloSport</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136443" target="_blank">📅 20:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: [عده ای] چنان وحدت و انسجام را تعریف می کنند که اگر  کاری آنها می خواهند انجام نشود یعنی تخلف، یعنی عدم همزبانی، یعنی وادادگی که [این‌گونه] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136442" target="_blank">📅 20:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ:
ما اصلاً کارمان با ایران تمام نشده است،
ما در حال حاضر قصد ترک خاورمیانه را نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136441" target="_blank">📅 19:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YztRtTMK_iswEwTGs1lO758dbY-nnCRdisDakIYckdmoO8B5BYLjFHXQ6QOXmhPY52hxQrwGFvfjVtU8SwEbS3BXoJu54CmDAYUB58VKtwLXu2qnIJjD5uzp6NGhyP64UqS68ONlk39yJGjRhBEAP9I-d36wrrAzrjvmyuG8OC-j3JHE2Pi5YTvW-sMf2Tw3UVsjG_GJIaRJCjH38PMV-0lFMVXPpie8W5ydHHILdiOjdFxayRT-Cs50r_zN81jEWipDQwV6UVOrS61vUqQMtbTgfXZKPkNVuvFb6-dxOcwnieu_lV7mgSx1RFa9RAVq3wpoMeHreAE2YOps5Uta1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان:
حرفای زیادی تو دلم دارم ولی الان نمیگم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136440" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: اون‌ها حتی به بچه‌های کوچیک هم رحم نمی‌کنن
مردم معترض رو می‌کشن؛ بیش از ۵۲ هزار نفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136439" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
دونالد ترامپ: اگر اکنون از جنگ با ایران دست بکشیم و برویم 20 تا 25 سال طول می‌کشد کشورشان بازسازی شود اما کار ما هنوز به اتمام نرسیده است و ما جایی نمی‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136438" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136437" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: اگر نیروهای ما بودند، حمله مرگبار اردن رخ نمی‌داد
دونالد ترامپ با اشاره به حمله‌ای که به کشته شدن دو نظامی آمریکایی در اردن انجامید، گفت:
🔴
«آن‌ها توانستند از اردن عبور کنند و حمله را انجام دهند. اگر نیروهای دیگری مسئول عملیات بودند، چنین اتفاقی رخ نمی‌داد. وقتی کار خود را به دیگران می‌سپارید، گاهی نتیجه آن‌طور که باید پیش نمی‌رود.»
ترامپ همچنین درباره ونزوئلا اظهار داشت:
🔴
«در ونزوئلا اتفاقی رخ داد که شبیه جابه‌جایی زمین بود و هیچ‌کس تا به حال چیزی مانند آن ندیده بود. فکر می‌کنم بتوان اسمش را زلزله گذاشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136436" target="_blank">📅 19:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل معتقده که ایران نه تنها سانتریفیوژهای پیشرفته خود، بلکه بخشی از ذخایر اورانیوم غنی‌شده خودش رو هم پس از جنگ 12 روزه سال گذشته، به یک مرکز زیرزمینی عمیق در زیر کوه کلنگ منتقل کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136435" target="_blank">📅 19:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136434">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیتر هگستث در مورد جمهوری اسلامی ایران:
ایران هر فرصتی را برای مذاکره و نشان دادن اینکه در تنگه هرمز معقول هستند، داشته است.
اما اگر قصد دارند به کشتی‌های تجایی شلیک کنند، همان‌طور که رئیس‌جمهور گفته است، ده برابر سخت‌تر به آن‌ها ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136434" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136433">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آی معتقدید که ایران سانتریفیوژهای هسته‌ای خود را به کوه پیک‌اکس منتقل کرده است؟
🔴
پرزیدنت ترامپ:
ما بر اساس مواد عمل می‌کنیم. آنجا جایی است که اقدامات انجام می‌شود و به احتمال زیاد به زودی به آن منطقه حمله خواهیم کرد. آن‌ها کار زیادی در این باره نمی‌توانند انجام دهند. معمولاً من چنین چیزی را نمی‌گفتم.
🔴
اگر فکر می‌کردم آن‌ها می‌توانند کاری در این باره انجام دهند، هرگز چنین چیزی را نمی‌گفتم. اما به زودی و به شدت به آن منطقه حمله خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136433" target="_blank">📅 19:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136432">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ : هیچ‌کس جز خود ایرانی‌ها نمی‌دونه ما چه آسیب‌هایی به ایران زدیم
اگه فردا از این توافق خارج می‌شدیم، یه پیروزی بزرگ به دست می‌آوردیم؛ اما فردا از توافق خارج نمی‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136432" target="_blank">📅 19:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136431">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ:
بدون شک ما «کوه کلنگ» را در ایران بمباران خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136431" target="_blank">📅 19:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136430">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ:
هر سایت هسته‌ای که ایرانی‌ها فعال‌سازی مجدد آن را مد نظر قرار دهند، ما دوباره به آن حمله خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136430" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136429">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1c69b0f2.mp4?token=hS4MjrUdKy5dgtQ6sPyXvn3u0HyqQPmdZH7KT3CU01c8m-CvFMGaJ01q3oL-8wiWKnpD4xLp1SEn33IXn5pLhl8g0Y8eADN_uBQ4HC0T0Aj1Xs9sn7_7Tk5CY-tGJi8Ii0otz-X5MV30OEvpD0R3lrox5fg3KtOKaPos1LRROfoCzYlVTonBIPadvZ-4ZE3Uy0CYGLQTvUIZ39V5-mT31PG5rIFVIoUuZHpjhKjyA_mq0u4gCpSB_Et5Hc4033yQjQlUian__k5bsnhh1YZkmQ_ttjv0vR2mKrlZiuncEql3EdR3BWWyx9rJtHDO_zBVuY-IWFARh_qnMDphzG6qGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1c69b0f2.mp4?token=hS4MjrUdKy5dgtQ6sPyXvn3u0HyqQPmdZH7KT3CU01c8m-CvFMGaJ01q3oL-8wiWKnpD4xLp1SEn33IXn5pLhl8g0Y8eADN_uBQ4HC0T0Aj1Xs9sn7_7Tk5CY-tGJi8Ii0otz-X5MV30OEvpD0R3lrox5fg3KtOKaPos1LRROfoCzYlVTonBIPadvZ-4ZE3Uy0CYGLQTvUIZ39V5-mT31PG5rIFVIoUuZHpjhKjyA_mq0u4gCpSB_Et5Hc4033yQjQlUian__k5bsnhh1YZkmQ_ttjv0vR2mKrlZiuncEql3EdR3BWWyx9rJtHDO_zBVuY-IWFARh_qnMDphzG6qGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جام جهانی: این موفق‌ترین جام جهانی تاریخ بود.
🔴
ما حتی یک اعتراض هم نداشتیم. هیچ جرمی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136429" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136428">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Qi5vVHpEEwRb3Hu7cHks7S_CpUUflfbOclbmS7oq3NwVD941uMoZmEZ93HaaKbBdWP3d_ZRLNe1JiUs65t5q8QecfCqfC_YCOC9jMoSUyMg1tz4Id_MSgxXj2G0I08KIuC_doU4vztM5ie4O9jYnP52W1jX6ecKSCkg4OnGOTUjmyDrKn6mT5FdYSracvVMWv_ZXEIKcOaXC_c2Hv7pDxDEJholEbrrgXVJ5XMziD_r4lVgN-VXY3YJZLHN1oo96Fjpw9IsXylsDxvtnIQTiWhAZB9vyJV50i66vDad7MrH2q5YdPatk7zRZeyCZG1gS7CacZkvAnQeyfqF_UHyAIVSdsxPeNCxKaLqizmm7FhPAlC28hfpWUS_YxGtd3KSDiN6j_Bs_jVcdvyRRTCiI4DnI6iWYhFzW_a1QI4KSO5Rl2v9OWMWDMdRDZNOeOfz_a5VrbLJHhaQOWMdhrT95TtzqkQs1nAb3nNpS64XGKUBnVha1lY0GomN00b0X3fn4OCviYT-mP2JpyvRj-Ud27pmNCN55AmuZ-owakZeZlonTTpmDdPiEGoBYsQZU5rR225LOtHj5x8v1cPjkiuP1HHoArRW0b4Fvjk8tR1X4T97-HXPGNLEwaysVVbMLySk5MrmiIGDbc_S6MangBXF_owNwDUXm7CPA2PRNuII4F4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Qi5vVHpEEwRb3Hu7cHks7S_CpUUflfbOclbmS7oq3NwVD941uMoZmEZ93HaaKbBdWP3d_ZRLNe1JiUs65t5q8QecfCqfC_YCOC9jMoSUyMg1tz4Id_MSgxXj2G0I08KIuC_doU4vztM5ie4O9jYnP52W1jX6ecKSCkg4OnGOTUjmyDrKn6mT5FdYSracvVMWv_ZXEIKcOaXC_c2Hv7pDxDEJholEbrrgXVJ5XMziD_r4lVgN-VXY3YJZLHN1oo96Fjpw9IsXylsDxvtnIQTiWhAZB9vyJV50i66vDad7MrH2q5YdPatk7zRZeyCZG1gS7CacZkvAnQeyfqF_UHyAIVSdsxPeNCxKaLqizmm7FhPAlC28hfpWUS_YxGtd3KSDiN6j_Bs_jVcdvyRRTCiI4DnI6iWYhFzW_a1QI4KSO5Rl2v9OWMWDMdRDZNOeOfz_a5VrbLJHhaQOWMdhrT95TtzqkQs1nAb3nNpS64XGKUBnVha1lY0GomN00b0X3fn4OCviYT-mP2JpyvRj-Ud27pmNCN55AmuZ-owakZeZlonTTpmDdPiEGoBYsQZU5rR225LOtHj5x8v1cPjkiuP1HHoArRW0b4Fvjk8tR1X4T97-HXPGNLEwaysVVbMLySk5MrmiIGDbc_S6MangBXF_owNwDUXm7CPA2PRNuII4F4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
«ما آن‌ها را در سطحی تضعیف می‌کنیم که هیچ‌کس فکرش را هم نمی‌کرد ممکن باشد. آن‌ها واقعاً به‌شدت در حال تضعیف شدن هستند.
البته آن‌ها توانستند یک مورد را از اردن عبور بدهند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136428" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136427">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b360764631.mp4?token=p0MyktM_VirJ6uD4Wpg_e_OABU4bLHpcey2K_V43ahRLQ_bnNLY3IFpb08f4jJZccYkNNQ71PcEzsIR-QtfHLiN4n7d3jkqxLXeQL7U9vulOg_SWOy6pgwEZKDIEAkljaVNWn6XmzW87vGzARoSI_JaDunefRlyygrhcu5eyLZCkpQGShUR14P_4njoXnpr8TBNiZAPHDttDypexM03igCzWw3psUynQ8lkJeJ0w3RcK3CxQUlgy8mdo8zFl34Ak1HRTMgm4uWiL15cxiz7CgSm7cY6xDSvxbR_W_iODZsUjxSAMsTvEZSy5IZDVBXMVMawDBEWyZvyW-N4xZfxKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b360764631.mp4?token=p0MyktM_VirJ6uD4Wpg_e_OABU4bLHpcey2K_V43ahRLQ_bnNLY3IFpb08f4jJZccYkNNQ71PcEzsIR-QtfHLiN4n7d3jkqxLXeQL7U9vulOg_SWOy6pgwEZKDIEAkljaVNWn6XmzW87vGzARoSI_JaDunefRlyygrhcu5eyLZCkpQGShUR14P_4njoXnpr8TBNiZAPHDttDypexM03igCzWw3psUynQ8lkJeJ0w3RcK3CxQUlgy8mdo8zFl34Ak1HRTMgm4uWiL15cxiz7CgSm7cY6xDSvxbR_W_iODZsUjxSAMsTvEZSy5IZDVBXMVMawDBEWyZvyW-N4xZfxKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: آنها به شدت خواهان ملاقات هستند.
🔴
تا زمانی که آنها آماده ملاقات به شیوه‌ای معنادار نباشند، ما هیچ علاقه‌ای به ملاقات نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136427" target="_blank">📅 18:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136426">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbc828d30.mp4?token=bi504BvQ7EzLVaPbI_3xKHlkt5E_d1NP7bW2M8iMvt7p_FvMqsaWo18ifFC-jPS0XQgaFzlNatqH3Cc8qhuO6Bh0OsxMAgragPy-qMBJ0Ae983ma_2dS3lxIc0MFDbMHz2BLs-a60Tg9rA76LbHavMAqkApZ1XA59oPYMgiePQpocSIZKd062HPYEayGTxRp5kueOt9-YOJk2Dbo26aQJiM5osn2KP_AmaEVI0DTbB2TjmNXEtZSO4ZD45wNP3jOLBhx-rIfSirvhUwtPRAyNjFmAO8SD5mJ9WnezwmheufbG9Jf32xGp67SHrZoSl9qPUgORjA_L_tJ58Mp6kvkkCAf_Xxj9nN-leRs4MI5Bp6AZganQhe5IjyjaApku94ENdk6pFFfOYWvrwdZyYQpgnHD0T8dipHsid9DW4OECBidRc8FayznRvH6OpGyf_8gHaoH17-yoJUCzGSv65f7V59f92WRUQ9lA19SOA4XFFbftDWFrWWtv1uAUDesls7Z6LepK8brimjLYVP4QP4rlbyUK69mWR2UH8UQe5jCNiATpJK3MZtZk24B1Qn1Hr56gS8MgXBOHcka6UIeag86NR7BgaSGD91WRLGCo7f6r0ap0ANcgB9h1_oTds1wpvslmagq1vdn6qyp20U9bPTEd4uvLnyZ8qbqU1Xvhw-zrdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbc828d30.mp4?token=bi504BvQ7EzLVaPbI_3xKHlkt5E_d1NP7bW2M8iMvt7p_FvMqsaWo18ifFC-jPS0XQgaFzlNatqH3Cc8qhuO6Bh0OsxMAgragPy-qMBJ0Ae983ma_2dS3lxIc0MFDbMHz2BLs-a60Tg9rA76LbHavMAqkApZ1XA59oPYMgiePQpocSIZKd062HPYEayGTxRp5kueOt9-YOJk2Dbo26aQJiM5osn2KP_AmaEVI0DTbB2TjmNXEtZSO4ZD45wNP3jOLBhx-rIfSirvhUwtPRAyNjFmAO8SD5mJ9WnezwmheufbG9Jf32xGp67SHrZoSl9qPUgORjA_L_tJ58Mp6kvkkCAf_Xxj9nN-leRs4MI5Bp6AZganQhe5IjyjaApku94ENdk6pFFfOYWvrwdZyYQpgnHD0T8dipHsid9DW4OECBidRc8FayznRvH6OpGyf_8gHaoH17-yoJUCzGSv65f7V59f92WRUQ9lA19SOA4XFFbftDWFrWWtv1uAUDesls7Z6LepK8brimjLYVP4QP4rlbyUK69mWR2UH8UQe5jCNiATpJK3MZtZk24B1Qn1Hr56gS8MgXBOHcka6UIeag86NR7BgaSGD91WRLGCo7f6r0ap0ANcgB9h1_oTds1wpvslmagq1vdn6qyp20U9bPTEd4uvLnyZ8qbqU1Xvhw-zrdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ممنوعیت دریانوردی حوثی‌ها در دریای سرخ برای عربستان سعودی:
🔴
خواهیم دید چه اتفاقی می‌افتد. تاکنون که نیفتاده است. ممکن است بیفتد، اما اگر چنین اتفاقی بیفتد، ما به اوضاع رسیدگی خواهیم کرد.
🔴
ما قبلاً این کار را با حوثی‌ها انجام داده‌ایم و از زمانی که این کار را انجام دادیم، مدتی است که از آنها خبری نداریم.
🔴
آنها مدت زیادی است که با ما مشکلی ندارند، از جمله در طول این درگیری.
🔴
من فکر می‌کنم اگر چنین چیزی وجود داشته باشد، ما فقط باید به کارمان برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136426" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6229ca593.mp4?token=Q4Ibi5JacpbADlS-ckeQjCLt7JnKuJCRT2n9bomtFDNZUzo0h3GZnd-9ZtLfvgFDm8rVapjJXO4qdzlXAqJRWXVpEL8k08b_YLaj1W1exmsrlGPSqu8IIL2eIDTZ-t8MeNXYz7K4m0ABh_6zxWRUeU7zXIWVjBQ4LDLgaXBz6MVODFm6lCn1qKlEtCRHDrbDxDblQfQNffLqktdhbb36wEu1P2btvE-lGEHQMittKTEtaRBETYDBfU95I4KUaaiwIBQ9zW4tHBJIMsvH0COo5codxJX3xohrztLTC3fYGxU4zJL52-vjY4h48tCUSusPGTUw_eusGOwPWN9s3rGL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6229ca593.mp4?token=Q4Ibi5JacpbADlS-ckeQjCLt7JnKuJCRT2n9bomtFDNZUzo0h3GZnd-9ZtLfvgFDm8rVapjJXO4qdzlXAqJRWXVpEL8k08b_YLaj1W1exmsrlGPSqu8IIL2eIDTZ-t8MeNXYz7K4m0ABh_6zxWRUeU7zXIWVjBQ4LDLgaXBz6MVODFm6lCn1qKlEtCRHDrbDxDblQfQNffLqktdhbb36wEu1P2btvE-lGEHQMittKTEtaRBETYDBfU95I4KUaaiwIBQ9zW4tHBJIMsvH0COo5codxJX3xohrztLTC3fYGxU4zJL52-vjY4h48tCUSusPGTUw_eusGOwPWN9s3rGL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هیچ نشانه‌ای مبنی بر آمادگی ایران برای توقف جنگ وجود ندارد. پس نقشه چیست؟
🔴
ترامپ: از کجا می‌فهمی؟ اگر هیچ نشانه‌ای نباشد از کجا می‌فهمی؟ چرا؟
🔴
چرا چیزی را می‌دانی که من نمی‌دانم؟
🔴
تو نمی‌دانی چه گفتگویی در پشت صحنه در جریان است. آنها به شدت می‌خواهند ملاقات کنند تا به آن پایان دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136425" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdedce66bb.mp4?token=V6FbB9cpmm-_StSX47FPBzClUEd76SW8dLWaNSSjDS3H2MWu-mYr1ZPLwONRohFLpLZ2Ge7-o7V7ERzVWyklUG4__3f9mW_ooIuZqw1-T3ZPfY2_MtEg-7JV-lqhcntcyskz3UclcExf2cCRSJN7lvix_JkJrEIPD5I3jwA8g8MNSlQJsAedevA83eJi1k9c9CcKoKAMBdHa7Bnb1RQaGj8KTSOCWssgv3kvmbF5ivLLLiAKNh9ZUecDQwcHDNDOvi517QAFCDxH7cKCMe5KcU7X4kImyPupJlkq2EzvznfTEuhmMfF6QFGvzWIfi0IABxs-0NK_0q6OhNgyON58JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdedce66bb.mp4?token=V6FbB9cpmm-_StSX47FPBzClUEd76SW8dLWaNSSjDS3H2MWu-mYr1ZPLwONRohFLpLZ2Ge7-o7V7ERzVWyklUG4__3f9mW_ooIuZqw1-T3ZPfY2_MtEg-7JV-lqhcntcyskz3UclcExf2cCRSJN7lvix_JkJrEIPD5I3jwA8g8MNSlQJsAedevA83eJi1k9c9CcKoKAMBdHa7Bnb1RQaGj8KTSOCWssgv3kvmbF5ivLLLiAKNh9ZUecDQwcHDNDOvi517QAFCDxH7cKCMe5KcU7X4kImyPupJlkq2EzvznfTEuhmMfF6QFGvzWIfi0IABxs-0NK_0q6OhNgyON58JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ
:
ما مشکلات زیادی را حل خواهیم کرد. ما قبلاً برخی از این مشکلات را برای لبنان حل کرده‌ایم.
همانطور که می‌دانید، مسئله حزب‌الله وجود دارد. اما ما کارهایی انجام داده‌ایم که فکر می‌کنم جهان به آن‌ها توجه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136424" target="_blank">📅 18:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335c9d8392.mp4?token=ASTuKNq9cgNIRG6f-KUTNwxGpUUdbWmT7zBoKEZpRgjBGKGLpJGwHdcpl3yv86lI88EUGhlGoOpbqH5QthDEcFkPpuRzasbAjNhmnxMsQydbtapKAczmGhDhPQVDr3TgviQs6cRTXJLa-vq16f65C9peIntieu_vZO2bp6TIdls5439q2-5fAkXKp9rw0RQQQy1wJr9snWoo-YEpYX1Vi5g9ZVDVIG3y11yK0wErw9UiLg9by0tzaqmkHKhQBEQXzDgQPAvbJQm6y9M-FyIwoU_k2RY-6p_z033mwFqvuaVFe8-3CeyuRjck8qndFDcxhfAXKFYorLvZ2VwZMeawzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335c9d8392.mp4?token=ASTuKNq9cgNIRG6f-KUTNwxGpUUdbWmT7zBoKEZpRgjBGKGLpJGwHdcpl3yv86lI88EUGhlGoOpbqH5QthDEcFkPpuRzasbAjNhmnxMsQydbtapKAczmGhDhPQVDr3TgviQs6cRTXJLa-vq16f65C9peIntieu_vZO2bp6TIdls5439q2-5fAkXKp9rw0RQQQy1wJr9snWoo-YEpYX1Vi5g9ZVDVIG3y11yK0wErw9UiLg9by0tzaqmkHKhQBEQXzDgQPAvbJQm6y9M-FyIwoU_k2RY-6p_z033mwFqvuaVFe8-3CeyuRjck8qndFDcxhfAXKFYorLvZ2VwZMeawzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
به احتمال زیاد، لبنان از بسیاری جهات، مکانی خطرناک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/136423" target="_blank">📅 18:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ecbd3e1f.mp4?token=S1xmiFwyP1Hx52pL01zwA33fJ0Gjla_F6kzDlGOCJ8quPe_d2ESnc6eSAG2PXRPwkfQpolD2rCdmzr8tcMwMvkILI8J5c3u-h9OA1brx2sfO3xwlSPIdqXtjFBwPY0zSFbEYRdlXNZD_1yuL3YZ8adM0-8iEQWqOxYrZcgLC-6FPtkXMpfeU5eDOCuRGdebqq9lpDRY6ZfuCa5ClBCUJuY_Z6N6KvzTKHWO7TKMNaBs8MsBw6j-i5evUVSJWfFt5ruxe-LqSbCxsg86bidYmTVh6URPnBMIJ5Yagn-M0kogLrv-8epzzpoAR7xlz7phVxtHUa5OO_TjJ0edr44SSKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ecbd3e1f.mp4?token=S1xmiFwyP1Hx52pL01zwA33fJ0Gjla_F6kzDlGOCJ8quPe_d2ESnc6eSAG2PXRPwkfQpolD2rCdmzr8tcMwMvkILI8J5c3u-h9OA1brx2sfO3xwlSPIdqXtjFBwPY0zSFbEYRdlXNZD_1yuL3YZ8adM0-8iEQWqOxYrZcgLC-6FPtkXMpfeU5eDOCuRGdebqq9lpDRY6ZfuCa5ClBCUJuY_Z6N6KvzTKHWO7TKMNaBs8MsBw6j-i5evUVSJWfFt5ruxe-LqSbCxsg86bidYmTVh6URPnBMIJ5Yagn-M0kogLrv-8epzzpoAR7xlz7phVxtHUa5OO_TjJ0edr44SSKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
بسیار خوشحالم که در کنار رئیس‌جمهور لبنان هستم، شخصیتی که در این کشور و حتی فراتر از آن، از احترام فراوانی برخوردار است.
ما قبلاً در موارد متعددی از طریق نمایندگان با یکدیگر صحبت کرده‌ایم و روابط ما بسیار خوب است.
به نظر من، لبنان برای مدت طولانی مورد بی‌عدالتی و سوءرفتار قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136422" target="_blank">📅 18:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136421">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1a209c97.mp4?token=nEpa8ncH-4jzCwRpBQO3oiNBn4OvT9feFhgPtWmkwRQyrOfmof1ocsDacDTvhwBCzTIEcpia3YHlAKNenYsphHCWH4vpn68zvfjguUinXHeEDRSmn3K-0YRoCIzIlCt9whYvopFIQ-9T1xfLwAtpk1OKM64dFYJ9W4oeXTSNhu8dHZyRZJOvTTw4GfBYmAqle8xoIjvSz0ARKzPQcq4sdaVGsVgjriuPDvL3hgRoFg7t1EFU1Ctg2EzcyqV00eldhdSFsvQ2YnUiFz-ovRZftqUSMmR0KB-ETmfC7kv57pS4t60xMRJnv37aG-zAwq7383qDzid8wR68Zh2nw0MjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1a209c97.mp4?token=nEpa8ncH-4jzCwRpBQO3oiNBn4OvT9feFhgPtWmkwRQyrOfmof1ocsDacDTvhwBCzTIEcpia3YHlAKNenYsphHCWH4vpn68zvfjguUinXHeEDRSmn3K-0YRoCIzIlCt9whYvopFIQ-9T1xfLwAtpk1OKM64dFYJ9W4oeXTSNhu8dHZyRZJOvTTw4GfBYmAqle8xoIjvSz0ARKzPQcq4sdaVGsVgjriuPDvL3hgRoFg7t1EFU1Ctg2EzcyqV00eldhdSFsvQ2YnUiFz-ovRZftqUSMmR0KB-ETmfC7kv57pS4t60xMRJnv37aG-zAwq7383qDzid8wR68Zh2nw0MjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس جمهور لبنان با ترامپ | کاخ سفید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136421" target="_blank">📅 18:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136418">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
قیمت هر بشکه نفت برنت به ۹۱ دلار رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136418" target="_blank">📅 18:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSi8BhN6UFmogB_MMBJBw4IA6BujvHytyLRGD7rxzjoEJmXUiGt1kJlVDzR1JR67d7QkF60XTw5ppsLfOfVKoqViEQQNGlTXTIFf0XLFsa05NY53ngI4bzILWaxkxV97-tLwxR0Q8SD2hFDY389UlUU2zSYQXf2t8q0NUTK3hO88-c_AftnzYSOiSeLxE-3ZSmhjEzYlMumhabJMaC8_Gqr9osnc5r9KMmJdsIGSJsLYv6Ce42VktxFnOWVyx6rIsHoE7jDk4VEXF2K_4XZJW9062pX1m3D2f71JP89XINPpuoopggOQJFQBl1IOwjwxhrbgSRs9ZMvDowjTOkuFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پستی دیگه‌ای که ترامپ از یه دختر ایرانی منتشر کرده :
(کشتار مارِو متوقف کنید)
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136417" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136416">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljEqhQeneYK98Y9hnrSmQzG-NPIk68I4c7IzXSxc6G10WZnuHwj1_E1iUZe_VWQDM2Qm8P3J6MM4TgGjO3_PLis84fFp1kbxCi9kA-LsVpbBESR8SJOirLqW4ojNUjntVtuSRTpZqMMlZnDi4M-qLDLBlYKdxTl8Jr6DqLMlEKmPoXCZmpfgJmubORuZqhO76ksxAo7xVrvkxG30duij1fmSL1YLAH6aqcWM2zm08Yb0UHuE4O87zv1uv7DIMAKrPeEt6Y71vIM9MUgn4CuVeCTVwvuqA_UYWgkSLSDbk-TkU36dBeLWfUILn1UaQLpfPP69DKYPm14EL8Pwwqbp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
تو جام ملت‌ها ایشالا جزو ۴تا تیم‌میریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136416" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41df0c99ee.mp4?token=jvkJbHABpHaCXSSJ1Sdja_zfvPBuykuyY86I7h0T844NpFdG26ncc8aELdXUvZFn2r1fZFowihuZwINnuaWoAJh5GLqzTdhvPozZNrk6K9W2BE-o2kK1QnfP1EJDakdW2TsF1GCQPBnns5kGg-kwf-zDv01QcMwAwsNpYHsSACJwAma63yoawYzVJGgLAx5CEanu1tzasVGq6P5RzsSpTryoziU6r5BnPwhjLQa3QvLcu8H2dhHuvmzF-4hSyxv6R96998xZxwJumXrbomhK_2a8bQATZeluQOnmdrT-SN8FJiehLTKBXr8VJQDrXsKE4Z-KqFsdFNQ3LCh_oxoewQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41df0c99ee.mp4?token=jvkJbHABpHaCXSSJ1Sdja_zfvPBuykuyY86I7h0T844NpFdG26ncc8aELdXUvZFn2r1fZFowihuZwINnuaWoAJh5GLqzTdhvPozZNrk6K9W2BE-o2kK1QnfP1EJDakdW2TsF1GCQPBnns5kGg-kwf-zDv01QcMwAwsNpYHsSACJwAma63yoawYzVJGgLAx5CEanu1tzasVGq6P5RzsSpTryoziU6r5BnPwhjLQa3QvLcu8H2dhHuvmzF-4hSyxv6R96998xZxwJumXrbomhK_2a8bQATZeluQOnmdrT-SN8FJiehLTKBXr8VJQDrXsKE4Z-KqFsdFNQ3LCh_oxoewQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرق شرافت و خایمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136415" target="_blank">📅 18:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136414">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اساس گزارش وزارت انرژی آمریکا، کل ذخائر استراتژیک نفت این کشور به 311.4 میلیون بشکه رسیده است که پایین‌ترین سطح در 43 سال گذشته از مارس 1983 است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136414" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136413">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc6dbe157.mp4?token=uaUTMFIBmSQPtD8af-t0zf3dvasfDP2bSTlDcGdeicU_17I-2flMb2n8wKYqXXf_IbjFBn6nEpmCOFcOj3Y4YDx-UTTW38MGbziMwxdZCgVoByxzBK0z7FNkHFmXf9TjXliibsKFIrGMukhJpW_P4jRL62Fdsy57WRJPrym1orKVfsCd4iuqBwy7JAnVaEMN573uEAvI-PxvzyoGdtSFnEoZ92Ow2j4fkk9muBirh8lB1xFXg7nuUp5UXeV7KJ5WbxNY2rR75xfZPqzHgYb3oG3JbZUk-dGt15kJJ3OXOyyk18ZT9IQ4thmIQFw9lyZL-NDtlRlksexqp5oHIPwgJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc6dbe157.mp4?token=uaUTMFIBmSQPtD8af-t0zf3dvasfDP2bSTlDcGdeicU_17I-2flMb2n8wKYqXXf_IbjFBn6nEpmCOFcOj3Y4YDx-UTTW38MGbziMwxdZCgVoByxzBK0z7FNkHFmXf9TjXliibsKFIrGMukhJpW_P4jRL62Fdsy57WRJPrym1orKVfsCd4iuqBwy7JAnVaEMN573uEAvI-PxvzyoGdtSFnEoZ92Ow2j4fkk9muBirh8lB1xFXg7nuUp5UXeV7KJ5WbxNY2rR75xfZPqzHgYb3oG3JbZUk-dGt15kJJ3OXOyyk18ZT9IQ4thmIQFw9lyZL-NDtlRlksexqp5oHIPwgJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های وسیع در استان سکیکده الجزایر که از پنج روز پیش آغاز شده است، همچنان ادامه دارد و نیروهای امدادی در سراسر این کشور با ده‌ها حریق فعال مبارزه می‌کنند.
🔴
سازمان دفاع مدنی الجزایر از ثبت ۱۷۲ مورد آتش‌سوزی طی بازه زمانی ۲۰ تا ۲۱ ژوئیه ۲۰۲۶ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136413" target="_blank">📅 18:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136412">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا اعلام کرد نیروهای این کشور از اوایل ماه مه تاکنون به تسهیل عبور حدود ۹۰۰ کشتی تجاری و انتقال نزدیک به ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136412" target="_blank">📅 18:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136411">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مرکز مشترک اطلاعات دریایی سطح تهدید در آب‌های خاورمیانه را «شدید» اعلام کرد
🔴
مرکز مشترک اطلاعات دریایی در به‌روزرسانی شماره ۷۴ خود اعلام کرد از ۱۷ تا ۲۱ ژوئیه چهار حادثه امنیتی تأییدشده برای نفت‌کش‌ها ثبت شده است؛ سه نفت‌کش ناشناس در نزدیکی عمان و امارات هدف پهپاد یا پرتابه ناشناس قرار گرفته‌اند و نفت‌کش «Wen Yao» نیز در اقیانوس هند توسط نیروهای آمریکایی متوقف و بازرسی شده است.
🔴
خدمه دو نفت‌کش آسیب‌دیده ناچار به ترک شناورها شدند و خدمه یکی از آن‌ها به‌وسیله یک یدک‌کش عمانی نجات یافتند. در این گزارش تلفات انسانی یا آلودگی زیست‌محیطی اعلام نشده، اما سطح تهدید دریایی منطقه همچنان «شدید» ارزیابی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136411" target="_blank">📅 18:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136410">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منبع نظامی یمنی: ۶ کشتی در ۲۴ ساعت گذشته پس از هشدار نیروهای مسلح و اعمال محاصره دریایی علیه عربستان متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136410" target="_blank">📅 17:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136409">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شهباز شریف: ما به نقش خود در میانجی‌گری ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136409" target="_blank">📅 17:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136408">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نفت برنت از ۹۱ دلار هم عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136408" target="_blank">📅 17:52 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
