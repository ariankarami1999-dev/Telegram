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
<img src="https://cdn4.telesco.pe/file/sl5UpMLm81y6kv7AHq9QHlox1CpkEfJF524PG54iSc0KvhQ5gDcRx6I7fGHureZQxprnrsRXv3I_mhIfwwdP5HlxS1dWaWeALB8DQ6i4FPvwKpN0hX0w8IkuLhIvm4uK-oqZYsDow_8uuInZmsjb_0lK6Tf8Ka34BVeK9XtH74hS2SC5f2IGbEJ8DWEF5alqKw7F_1WzOKEStowPm26w1uZ-FkflL9NNVBzBaKFBT04j5FNkmFHL0PZnbiNwqio3ZDDLvlTOFuqhVvxvGYiBORDJku4yWwyuMmFFX2aheM4c2OVvfBMJZm-t3O_gNxrx_j7sKOQ8RN46FE11q0Wq0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-439548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
حملات به بحرین و کویت ادامه دارد
🔹
به گزارش رسانه‌های عربی، حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین هم‌چنان ادامه داشته و آژیرهای هشدار قطع نمی‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/farsna/439548" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7bbe8d9a.mp4?token=WgrN9o0hFsnGAIrd_Iv3AaH97JYDKRFAPJw6ESZ8vzV24sLm07r2UQuLRfNcna4fJ_XbeT0IP-36-oyPSu8cC5XYOBZKUJ83UrAwQHMY6o3-BcK9vQCqf9Gn2hwkVojM9B2_Pn9yChApAZ8hOPfyhZhmV9AWla3M6o7-3eVyh0Z-LSaEwtmIF5c1J0MIDfyWyKd_EoP0jQlJoHZB9XiOHaFxqcXvQA_4GRijdWSzz3GbrkEXA_kAh1lcBPrXfVRhzn6UMV4oKkNAEuYHrXdXSbpzBC_dFsVNsLuw9cxL6RxcL7Laz5OZi8NIMQGy2lGLawebAOW4RyJiK_74MXdyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7bbe8d9a.mp4?token=WgrN9o0hFsnGAIrd_Iv3AaH97JYDKRFAPJw6ESZ8vzV24sLm07r2UQuLRfNcna4fJ_XbeT0IP-36-oyPSu8cC5XYOBZKUJ83UrAwQHMY6o3-BcK9vQCqf9Gn2hwkVojM9B2_Pn9yChApAZ8hOPfyhZhmV9AWla3M6o7-3eVyh0Z-LSaEwtmIF5c1J0MIDfyWyKd_EoP0jQlJoHZB9XiOHaFxqcXvQA_4GRijdWSzz3GbrkEXA_kAh1lcBPrXfVRhzn6UMV4oKkNAEuYHrXdXSbpzBC_dFsVNsLuw9cxL6RxcL7Laz5OZi8NIMQGy2lGLawebAOW4RyJiK_74MXdyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام موشک‌های رهگیر پدافند آمریکایی و حرکت آزادانۀ موشک‌ها در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/439546" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فعال‌شدن آژیر خطر در بحرین
🔹
منابع محلی از فعال‌شدن آژیرهای هشدار در بحرین، در پی حملۀ موشکی به این کشور خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/439545" target="_blank">📅 02:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
شنیدن‌شدن صدای انفجار از سمت جنوب جزیرۀ قشم
🔹
برخی مردم محلی قشم از شنیده شدن صدای دست‌کم ۳ انفجار از جنوب جزیرۀ قشم خبر می‌دهند.
🔹
بررسی‌های خبرنگار فارس حاکی است صدای انفجارها از سمت روستای مسن و محدودۀ دریا بوده است.
🔹
هنوز گزارشی از ماهیت این انفجارها در دست نیست.
🔸
همزمان رسانه‌ها از فعال شدن آژیر خطر در کویت و وقوع چندین انفجار در پایگاه‌های علی السالم و عریفجان خبر می‌دهند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/439544" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439543">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
آژیر هشدار و صدای انفجار در کویت
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/439543" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
آژیر هشدار و صدای انفجار در کویت
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/439542" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqSEIBWbhw5geG7tbyafj86gQmpb1bz4o93Et7vkTY6p-RsN1VGzh08PWQXGsw8JqX1zMK9GW2-tgopoORKgath48FifdfGPBZ8_Ettzc3Lnxr2HDsVLdgD0LrVhOoRf_MxhrPneDFiqUoaMw6fxElLtSvk7e5KX0_Q5y8tnY0HTH2--K7q2OSfFdEqH8qPWGVdSOQFHUB_N5FA6ATS1FrTKmV-iQPyNNVqFrGBvpKUAdGIgZFOBltRlZm3JI-GH0fGIuOCf4RaC8lNb8KPeDbOO3YaYLLDnL17e73OTwFkcV0EetBsOMQXlJaCgor_M43_5gPiC5zM8V9CCX6SA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینۀ نهایی سرمربیگری تیم‌ملی جوانان مشخص شد
🔹
گفته می‌شود پس از استعفای حسین عبدی، کمیتۀ فنی فدراسیون روی انتخاب قاسم حدادی‌فر، کاپیتان پیشین و سرمربی سابق ذوب‌آهن به قطعیت رسیده و به‌زودی به‌عنوان سرمربی جدید تیم‌ملی جوانان معرفی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/439541" target="_blank">📅 01:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e027321be.mp4?token=WA7Q31ekmp87rTctUPlsqtq5eJqQzZUCghZHk2PyTQerNIvMFfQxmhUYFKpUJqBKLHOpI0Pl4aBzNXPDxx32uYDYdi8_YXMboDlVe4j1oPCv7PvzkFzdSqlUJ0rH2k_SShWrVghx4GoP5aJglq16eXzNa612tvNzKIcMb1gGYJhW4I4fE7eyrHGj484jmo8WgjtMIBJenBXamlnrvZHNUoml81L7B3Myz-z7lg0vjMrL05aat9aFqCGVbXOINfWNxdcFGpFs2PQH5K--jGD_V0uzHgCUGv5BtlxusoAwCVs3NjKoykAtJzTKwCxrgifzqvbdO1vj6eGcxxbCG0_992Uup-ZhUOWI0ExRsrf_CuQZ5Ibk3wueStUScK_jVXaLd8Ws0nJhpJgBJSrqleNwN2oVPO9ajOjqCnupoZ5PGHAqE9pD0FHQgKc3ZQcKCPQFlD7xJZLiZ_yjZSIAcRD6WGdvnRugYCr37v-n3YCWGSF0n-2oV5tOqqXEZTsNbnkbPFxlh6XUcK48cHb-z3cSKDdI9ffcQpie1L_8DY54sbZwyXCYc_qvU6dqdWADhZqFLKb5OxPhdin0Fx7H6kicW87HDwuPYHkWwmWEwvHA4NPSFFNm1eIdh2Fxc_B7K3H5MamfymduB1NoZ1YQgL8ZsSHzqLQFDDNu--uSwFxsS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e027321be.mp4?token=WA7Q31ekmp87rTctUPlsqtq5eJqQzZUCghZHk2PyTQerNIvMFfQxmhUYFKpUJqBKLHOpI0Pl4aBzNXPDxx32uYDYdi8_YXMboDlVe4j1oPCv7PvzkFzdSqlUJ0rH2k_SShWrVghx4GoP5aJglq16eXzNa612tvNzKIcMb1gGYJhW4I4fE7eyrHGj484jmo8WgjtMIBJenBXamlnrvZHNUoml81L7B3Myz-z7lg0vjMrL05aat9aFqCGVbXOINfWNxdcFGpFs2PQH5K--jGD_V0uzHgCUGv5BtlxusoAwCVs3NjKoykAtJzTKwCxrgifzqvbdO1vj6eGcxxbCG0_992Uup-ZhUOWI0ExRsrf_CuQZ5Ibk3wueStUScK_jVXaLd8Ws0nJhpJgBJSrqleNwN2oVPO9ajOjqCnupoZ5PGHAqE9pD0FHQgKc3ZQcKCPQFlD7xJZLiZ_yjZSIAcRD6WGdvnRugYCr37v-n3YCWGSF0n-2oV5tOqqXEZTsNbnkbPFxlh6XUcK48cHb-z3cSKDdI9ffcQpie1L_8DY54sbZwyXCYc_qvU6dqdWADhZqFLKb5OxPhdin0Fx7H6kicW87HDwuPYHkWwmWEwvHA4NPSFFNm1eIdh2Fxc_B7K3H5MamfymduB1NoZ1YQgL8ZsSHzqLQFDDNu--uSwFxsS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور نمایندۀ ویژه رهبرانقلاب در منزل شهید ناو دنا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/439540" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار در مقر گروه‌های تجزیه‌طلب در اربیل
🔹
منابع محلی از وقوع انفجارهای متعددی در مرکز کردستان عراق خبر دادند.
🔹
رسانه‌های عراقی می‌گویند که مقر گروه‌های تجزیه‌طلب ضدایرانی در «دره آلان» هدف حملات هوایی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/439539" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuBFOhS9WRRhr9ipZ5Tvggpvo5HJ5WVb12837D7re-PupnrKNzYAvXAsGpvpo3nZYAvx_x62H7RJKvQQI95CoSSOQcM0zZnskV2mOtYEOZEbrxyq5zOzbD8tu2ojTRIzEsIT3i4k9GJG_rQ0wGXWlU-t18_vODgCcu1y8XXnMctPCn_koim2s-NfggXCq02dLnBwj5i2vdLLMJxgb0CPRNmimzZKeXKiT1i51hkqBZeic7QS58npKmerjNqRQbEgPLhQQjh86GP2lm7CklJZCntRSUOg_aZYWRq3HmgIVdNNHH8fR68CTPVcGdX7U2NAQd_-4S81hGw69HLjQ4T3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je7H35bL9UEwg15poOKL0wv2B2uNP8UKQjHv7D2GKvUJnG-jU5mnm92AxsyGT96J9SthgniGEdGFQ3ol9OVBF3KTKJRgPQ-Ycf6_uxvXpWGy2IYWgv5J6WaaWU-xzrpiyFY8FjwP7x5p4s265G-ccWOMl7HxqdDOXNk9LjSlOJJ2UUiluN-iImdsIhr0mQPOTQ1coMSh54Pgg7ujv52zCWYp_tsnG5L2YNZpiA_Tt_cqLNN_wB4znMt5NF95Q2aB3Zd3HjP7JZF3p6mQ1tNzyXqwtLTnX8FV9XWkqw4e8SHM2Pdnvl1y5_HFHXUm0cQoNCBqCIeYalzGmgBMz58IbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt60W-1YOfZnPvOkAWjYdfy-l0WE3wj7GLyLXx4nuX_EnPiVdwbN_ayCwq-tH3WBbg9MgesqPCF8HY5sghfZSliHM4Ii-okpOrTbfKVW8wbm3z6hsjlx2qWKy8Q739-clbxsNQzf1nVfqizUm62_huja_m9fPNXero7RgIPRRZ9zSsw9jyl1VRopEd8m6CEApqLhBG4lgM8ze7iiMXrRWsoZm8i8A_8uXc8ruN4gDREPBjqxOdybRP9_5I-RQMd7s1n9DoDLem-7Fnye5imZvsizy4i-nK-wMoPlm0lw6XCBq3vXMfdPk7DyGYdt0e7TnGR1ztBE55D4cVUNO7uK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecc_Dt_XJBHkr7lpmotRtC3R5Q_Ku-SnIeB1CyCRuLFnaH5BpQdkNbWTgNTI27q82TKQE-NJuggcOSinZFGTAmBuiyTR5qUsC6c7EfqfHm-GJCScJT7tjStR-Qck_iMutYFc3az64VK9EAw1HqU8RDIU8lUz9FiLC02QoCwCCOPtwdg3N3THtSMxn66TEdC6aIzb5XW7S-PpqiP4rIu8NcooK8BV4nTEKoQpUyugwalUZw1rNFAQTwxW3LghDXT931XIiMXS2FjgZT4gsFhvJBYW8uhS0sPNb3G0VxqnXx6H-qMYfqcmWfXJU-YAXkgUUvpc3GpF82mN00yyYCWBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9rbJDWos4TXCypbwHU0MEl7Zauq_k7vxF7Sm9n0C9S1PjdCIQnzs9khVhuOfF3Opw2mKBXnR9nZuHxHlDaxa1SkKycpfm6G0RJ6QCo3GRWpDAYSeEJ-BAb2M0RWXkIb6f5IwswBXWC0Ja4ILopslcNIgZk2sVEN-iTvG0nTTJVuhvQPdA7ihPTT2EdM3o6Gv1lsddEIyWx_mlBlEDHL5l58nB2Xe003hix9uRahAPuLkAXHgzgZ7WJchNditSsbz15zUjWwSwhINKmQPqlxjhi1L3d6x3EqrsgoEgyUHgIJtEtbbGbAJfe5j8mrI7O6uinJ-ORYNLPWCU6GUDds1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-lbJ0vccx9xWN6XHv2qGxbs_0W_us9uBnbGFO1YLQ6A9QV21ZVBzIDfPKVYBhzcAR_1Pzne5GcvD_BR5U_LVm3lUlRUdNC8RFUhZmEXq14smDNtuoyj2i7IRMGsH3wkW5tyCzdag5jfDssUO8HJp1_UQfdwt-Zw68um7BaF2t7kLM1j6kunamGiA_j0uHcLcFTGYT9DEpIkbi0DRGsDggqRKMyLOUETUEWWdj1nqF6_io7X-jYNSsXALmVopeyuocH2jT378Z8szCHtMLa2fYy1SZ3qR5sOhTUN_Xczle9kOz1-WNC0OSCAn1wVm0IOglrot86ixnBqS1HYO8kQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۳ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/439533" target="_blank">📅 00:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9EhY4g22rrGQ8I_bTmGDfMxtRbu-9yg6hQBeAnv1XwJD0uKK2EbHMUGmzJkc9PLW8TXEdlgxodyOf2TTetpnltAOvS4JLZsBblL1s_Z3EWK_CMAOH_BO0JITY2VxGgFM0O4-TjoW9rr8pku87Rxk3Q3889t38B9WK30fClNQGt3hBzjJnhC39eHvs2t2390b3UY_t2411eCYHpeHmHt-pqtLO86dSPLdQ409JbDdnhIUb8JpCBkqwVR1FJbH4JF9cVLtZS41UGFRpqm1Z_J0M0oHeG1YCif-iD4GdWaGGuQqR5a-uzDW0CUhnpAHr-mOz5Zz5Dp0XXKRZj1v2FLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mO55ENiPR3ZGGsvN4eh4aFIeXFZFXsMlZZCHooSrznonUc0fO7jtWTeCaumQ2kHZWaaoFaKvtE8DM-oP0F-DuQb1FM8VUAMVwbgOqhHYjJnMneUyMpy-iI-cmRI15NOsK9FD0rhxfzqFsr0L58j6Ybww61iXRYBUlRmeYUDuJPZDywx2reCqOv1oSdUUpmstL-91jtEbSM9P-RUTemIaEWSSMiP4hg0JwaZUrAkroBJN_U7JRdaP3JX7bylvTB4UrgLce8tJ8o0z4U_n2cnxWg3ahwxyrM5wNhFvuqB26nrLaSRXK33KcTCRRLWH1p7Bw9SLJpZqwL1hdS2_Vn6GtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnMYoEtECn4VN12sQflE-g6cUt2QaKZUVwUjdfRbusDMYnEECXXT6GofcNnO5QUJLlDO37n7joyW_dsh0CVwBxf35pzkSMq5KO8d8nWkoh5rqJPwOUrrLOnq_nbS2o1RsO--UYsmk08QZJZlVAVmER1wd_11Rp8UpZEAhFJpkPfR6vYfEm1pMD_s3E2knDnScZmz7DflTRoDZ8yu9sp0UFBU0EXl7pZ2QnvTubeA-BDMe-Sczhc8rLK-LvSq-LdD9qc4tHNu9n7v9uuehGyOmghvFwggIOYfICwlpanRgWH-6f9SnzKf3jQ3UDeQmZ2C8dNu4MEmVOJ9cg-WXknzng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0klL_m67QConn7WPyupal8PvSHRiqaWhHtyj8hBmWf-0usUVnGWeFm-v3jiNNgvqkxjQlM-dI-mL7BnHCKK3R1ewQu2DjN5ObF2UDW67dOUHADzMWLDY33jwuZeyRz5hMW13db7ygqg2SuaI1ztSxp2ctaRHP827Sw9oA0lwNppPK0HJBxvL8xsK-XACJF_QxduPZiSAleaTRc9Hs_JEb8aumtNiTp-QaDWZsSneT4exOfjjq61cDo0pOieJmgtuRK9q5ehxQ1_F8N-B03KFhVuZYPOSRnUNG6-1uHT_Wd4ypYmPiOjbdgNg3DGdiB5JJFFD78VhoZzfG_jYfyStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7SQEM94LtOLlvRRPS3yhNsB2N2kdOd9oCupXnhR3W1--WlN2LQZach4KNq3Xjc3oORBvqIUCxp2IzqJKngnHMTg14S88BzU5GdnBHC5qWPKR24uzKd77ytcMmKB-IIG86hb0eJla_sGe2hB0vyBWOfahF_eSuQDiEbfpCDc_otxxOMJDRsOkBZk9ftmuCF0QgwRzOFnM9jGgrWM8AkgCPQYI6bn7VadkxP5Cj_ogbvtBEps-H7v0Tlu2sVZXCbvP-0Ny8V7Ud3Z3_TdIt0GkUHt5ZTyfnGdaM9H88wpZ7CJH6cvjxHDWq5rBk2Et0UQbRc34YfvG_PF6G7sD_9ehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbU7xxNfVootKJ6B-qpvR6jeaSF-yDjd_6o6L3NqzBS4RXjV3R4ZEOKM6wpuxlC7T6SeD7bB9q7pStY5jlD-iE4HNiCYrBbqF38bvZHJdVSgXA_slCRFV9tv3-2tR6zrhu3bR8HCU7YJUV0omZZin2inpjTqRGZl1XuHf7JLpPi1tIJIDvONOsvrJxQWDM8Dzs6cQ-6fTOa5EMlyOlKneeYDHL-qXQ6b7s7rt1YNHxGsGc9NK35H_kKRtQ1snwgQKPsuxyxIrtdZcSZkV8vBV6mA7Bw29q81KYIbjQyEuIsKqW_B-cyHnzI_MOCUh9SbGhadZaGjWzHn1YkrAVAQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P840oNUYFg7DBRGjj47E_j2KepzIbkDrASi6bmqqJx6JpYaJHDE9MLYz5Lhv7o4AZbbvndxrnBy7Xy69OF1AYmggl3Zw9CUgVoig3lJSgt-J8URYI2CrYIvwDJ25rWQHwwLZYTBb1nBId1oBhT-xc0lvLZGRGavUbUdrA6oONQY51no_NNRs83bEM_R0AVaTrUzItPGv7gfuUy0Stkg3m_UVS-uma-MXu9ysHe9VDMAQisnB7pRWGTtjpFYF9HIS_ucrW30MlF2_eqOF6p2ywzZ7hmPMNjtWoa-VYUcM8OfmgR-LXfWdiEf8DB7fwa269ZqvGRHOYk_5gWUyEUphvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAib7V9QZywksID7vgmuQ4nGUqkGC0fSbAzwOxDXkzueScJS--dHAzfi4wglAYuajqag0ufhKRh_xlhvAwiXWwKBECgHeybHaY4TR15gopABPc2cGROA2D21aT5s4nd6kKu2S0x-ishPac8LkF7_tp9S4IkcbxbmGCUhxqv0mrvtP9fpFLLJQjwDL-ZM0PawkivjtHaIT3MbfOGNREeefrtS6RHnBdL2hpoHtFNkh6IkQdB-M6y1thKLy70amrxLf5WgV3UBv4-gIewisq9wXXEwcPmY0WKL1fmrqFTI-vLZAkML6Hoe9XSbgm9ZuFT5Tq8FoLpTckGRx2dYHHow7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGpUrE65bblgO8QtCy9A9920E17EtjiJ7UqKQUB5So43tPcb5MTxp5uwf_elXBen34vELUasUjA1EHVmZoHpltkcuRuR35w2cDTcbKbu5x8jfbNuTjG_72s-u07RPAaiehj4XjqnAVeZe9eHGZSr6oQ10JGPX_gjw2Xnu1c4YPal0UaFG-PTETpCq2uHSvXPQRJDPwamNyScslwTLWIe_-wUXPKMsOLbEXsr7nhmjAvtlxJFAXWHDcdGYmg2742t7R3Hhbq5VV4E7d3JAWdlPJE7xS7Qk9rjTUIaXBOjrULO6NW_mC8TCwQOJh4O5aZrp2KHybA27usFfL5ulA6yQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_-msPZ1GKbiexb8r-L8_M-heVQ-tI9yeIl37q-PqZlVBS1ozi4cMd1yxgRY1u2DMKFUJ_n5Ux0ZzEmVmoAQkZHTPPcho9b_ACOtG6edu49z_5rnj-FRLhs3sdxAQ5U9wrdKZTwTSx7_9XwlKLhF4KveZrBINhRskWpNgA3EhJeCYV_DRfU00aJ4k2sVEWVmApQ9Jmbcq8lHvgiZ1fQITW4j4akd6vMX-IjaZS4G12ZvpuitFuCu11p12uB1rL0S3HvqY-wyWkAYSUptXvDIOlODhMsILyIMbaQ8FUYJZc6_WheOf5qsNsUiGaC5rQdbkNmIe33WFM6mJy9m4qCLsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/439523" target="_blank">📅 00:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTVEeFXU21PkUIgl02wyBvEI5BgEReC_5Jb5-Q-V8Mf81I7za3Q7wH4V07mFNgopxnUX-otG_cKtV4FUBbxNzyBZnWp2TpapRY8deO8524prhk9HrcVO-EknKzhrHh_mriI484L1l1c3G_HceemfNlr9j4kSBVPqLYNopy60B62-Reo8DymIa9K_PWn80LnRxpDjtUIFDm7oZzANvlm9n3Py7oI0RQcJ1AedSSgqv470aTYFY3JK94pKY5sj5ojmHqaCzLKZoyutiExxkt5sbIt7683Mxnbk1RpMrAJeNe_OBYJETHyybS6cqJ5azPzjC4rqjYwIQ6ni_9c9RPu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویزای اول برای تیم‌ملی صادر شد
🔹
رسانه‌های ترکیه اعلام کردند که ویزای کلیه اعضای تیم ملی فوتبال ایران برای سفر به مکزیک صادر و تحویل سفارت ایران در آنکارا شده است.
🔸
علی‌رغم صدور ویزای مکزیک و هماهنگی سفر تیم‌ملی به این کشور اما هنوز روادید آمریکا داده نشده و سنگ‌اندازی ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/439522" target="_blank">📅 00:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81be34d97c.mp4?token=LvD5WkMnjODSHy2eC4X_0iA9fM16noFgAhaQjPtvjz1Jj-5lZRkm27b1mLrh5x7z8KQ3QUitQd9osZoLvUNPfH0KC8gYIBlw3s1MTbi0fMDMvI7nVIML9X4oBo75SI1ZSmMlBP3JM2REQdk5YEZrfIKj0gOwm5dnt7_cSXmNdts9NXd7di63cepxSZgSqvpwrXyoJ9ewk8SBOtwRQXJaUaN-9MwEUrnV1woWM21k__HCHaiQcrAuNpCzsbMnCp-SzrTrvxe9URjVB83_ivzxsdylQDVS1_e8-FHh3axTkxSUMIj4c09voJSpnPSDi7gZrr_e7Ch9wQOJbmCihVLe3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81be34d97c.mp4?token=LvD5WkMnjODSHy2eC4X_0iA9fM16noFgAhaQjPtvjz1Jj-5lZRkm27b1mLrh5x7z8KQ3QUitQd9osZoLvUNPfH0KC8gYIBlw3s1MTbi0fMDMvI7nVIML9X4oBo75SI1ZSmMlBP3JM2REQdk5YEZrfIKj0gOwm5dnt7_cSXmNdts9NXd7di63cepxSZgSqvpwrXyoJ9ewk8SBOtwRQXJaUaN-9MwEUrnV1woWM21k__HCHaiQcrAuNpCzsbMnCp-SzrTrvxe9URjVB83_ivzxsdylQDVS1_e8-FHh3axTkxSUMIj4c09voJSpnPSDi7gZrr_e7Ch9wQOJbmCihVLe3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای نامهٔ مهم امام خمینی(ره) دربارهٔ شروط رهبری که در جلسه خبرگان سال ۱۳۶۸ قرائت شد
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/439521" target="_blank">📅 23:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPWlYh5MAMFSNi9X4Qrf6joYfAA31hEIsbs63io0qaIaiRY_KBOA5rols4Fi0CshYQTvyT-hrtZ_juPtgB6N19ukVpMLMOJ5Vkn1Wp2qvwJ5X1fg1DPwKH7eilMoF-Vy2LDDyXx0Q5b0u8t2hItCTINbprkVunD4pAGu1DfyZ0dysU55o-TIoQxcLVVoOf6N-hV4LgbCljwaTAUnx4xPRStE2C_jAXU0giGrm0ufHoNjOK95clJbFDQXJMJyaKkomlg8q9-RmfCA1Ohp56jxaqSRvAnp43Ooj6TEDqkdd-VlsMggoNyDNDMTw2ke4Lgv5ymiJoxpqLcj4SlWmyYm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش‌های سیل‌آسا در راه ایران؟
🔹
مهدی زارع، کارشناس زمین‌شناسی: ایران در پاییز و زمستان امسال ممکن است تحت تأثیر «سوپر ال‌نینو» قرار بگیرد، پدیده‌ای نادر که می‌تواند بارش‌ها را به‌طور چشمگیری افزایش دهد و خطر وقوع سیلاب را بالا ببرد.
ال‌نینو چیست؟
🔹
ال‌نینو یک پدیده اقلیمی جهانی است که با گرم‌شدن غیرعادی آب‌های اقیانوس آرام و تغییر الگوهای جوی همراه می‌شود. این پدیده می‌تواند میزان بارش و دما را در نقاط مختلف جهان تغییر دهد.
🔹
گفته می‌شود امسال با «سوپر ال‌نینو» روبه‌رو هستیم؛ نسخه‌ای بسیار قوی‌تر از ال‌نینو که وقوع آن کم‌تکرار است و آخرین نمونهٔ بسیار قدرتمند آن به حدود ۱۴۹ سال پیش بازمی‌گردد.
چه چیزی در انتظار ایران است؟
🔹
افزایش بارش در نیمه غربی، جنوبی و مرکزی کشور
🔹
ورود پرقدرت‌تر سامانه‌های بارشی مدیترانه‌ای
🔹
بارش‌های سنگین از اواخر پاییز ۱۴۰۵ تا اوایل بهار ۱۴۰۶
🔹
افزایش خطر سیلاب‌های ناگهانی، به‌ویژه در جنوب کشور
برای پیشگیری از خسارت‌ها چکار باید کنیم؟
🔸
لای‌روبی رودخانه‌ها و مسیل‌ها، مدیریت ظرفیت سدها، تقویت سامانه‌های هشدار سریع و پرهیز از استقرار و تردد در حاشیه رودخانه‌ها از مهم‌ترین اقدامات پیشگیرانه عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/439520" target="_blank">📅 23:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
خزانه‌داری آمریکا ۴ فرد و ۴ نهاد مرتبط با ایران را تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/439519" target="_blank">📅 22:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba4182118.mp4?token=krseh7HGOq3D2T4P1Ejs27Wt50DEpFRb9IcsYjdUQO-853xfza_FS5t-cCUfN0GbnkNw3McsmbfTC8aia4pIEQ5MR-Pb9RogYYbYn5nyjOogkpP6eas_7NbCQ0EnBYRuaqHIALTI58YKK09Th1jvQreKd8FVi69Ads9-MtAeZ08O9AMbXg6IklZbzwHrJcpRl1lmhoVD0sK4_I92Wq8KspXTHgaNMFcaaFh0maqbL6iPn95XJ8Qs1LbeqJf98ObsGsjICGyU-mq6-3knmdCUfe2XGVNsW4L0CW3XKHWiURObthBvU7HQqIER9GIDhNg6xNcUi4673tNqy-bF3WKn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba4182118.mp4?token=krseh7HGOq3D2T4P1Ejs27Wt50DEpFRb9IcsYjdUQO-853xfza_FS5t-cCUfN0GbnkNw3McsmbfTC8aia4pIEQ5MR-Pb9RogYYbYn5nyjOogkpP6eas_7NbCQ0EnBYRuaqHIALTI58YKK09Th1jvQreKd8FVi69Ads9-MtAeZ08O9AMbXg6IklZbzwHrJcpRl1lmhoVD0sK4_I92Wq8KspXTHgaNMFcaaFh0maqbL6iPn95XJ8Qs1LbeqJf98ObsGsjICGyU-mq6-3knmdCUfe2XGVNsW4L0CW3XKHWiURObthBvU7HQqIER9GIDhNg6xNcUi4673tNqy-bF3WKn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام جانباز معروف جنگ رمضان برای آمریکا و اسرائیل  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/439518" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b686bebf.mp4?token=pO12gIbD3a2_mBTEDj-7bPkhnNydPa-vfXsHJ-pqkdf74HjTb1G1Yfm5FoWWk-a5Wly-5IrRAFZSaGkKm7hbJGHf0et-d7iuJvJBpm-U0qvEpR609hlJBr5UU1Ml543Yddjbl6v_xWra8t3lBDue8KYvZssw0bjwiIm_4hJjT9-N3qT0OArxM4cPyDJCMvdkHVa9GXraN0PJ7WRoZMWaeYIjT3A8Cg_vW36U7t3cNk6TMy83-qkNc7R4NkRHhbxqAYNG_dwId1pXGO9M0C5Q-E-QPNkTE-VrOIzW0Y9wWBJc_PKiDYdV4RX-pDkfHFNvUmkPJ6jHm8PPSc6qoMjnTCryVGb8xxl5D4-bKivQRwvQWcs8NduHn6qWWKjzujkHgzqMgEvdPStdBcGCaglcqGgxt0avCHH3KqEDdbLXBNYhcS6g4z8PxNjmzMv1LvrbAkng33zO8fuU41oy4dcXsCHwep0gQsd4i9n9CmEAZwh0vnpYN5R9BLQKb_7CPD-xr5l8Sb6himY2ojVzcIoTLJf437IRiHdKJKjyZHxMwxlGee3WrZsEkDR49dN9OySSbBnz91ETy4DbTpxVw0Rbu1MkFrigaOYPVtxSbGL5pilhsbPubedwtAkE3IM3LtzgzsvKEF6JYxQ0gVi6vzXXwxHThzn_AQTD59SJ8BpYvg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b686bebf.mp4?token=pO12gIbD3a2_mBTEDj-7bPkhnNydPa-vfXsHJ-pqkdf74HjTb1G1Yfm5FoWWk-a5Wly-5IrRAFZSaGkKm7hbJGHf0et-d7iuJvJBpm-U0qvEpR609hlJBr5UU1Ml543Yddjbl6v_xWra8t3lBDue8KYvZssw0bjwiIm_4hJjT9-N3qT0OArxM4cPyDJCMvdkHVa9GXraN0PJ7WRoZMWaeYIjT3A8Cg_vW36U7t3cNk6TMy83-qkNc7R4NkRHhbxqAYNG_dwId1pXGO9M0C5Q-E-QPNkTE-VrOIzW0Y9wWBJc_PKiDYdV4RX-pDkfHFNvUmkPJ6jHm8PPSc6qoMjnTCryVGb8xxl5D4-bKivQRwvQWcs8NduHn6qWWKjzujkHgzqMgEvdPStdBcGCaglcqGgxt0avCHH3KqEDdbLXBNYhcS6g4z8PxNjmzMv1LvrbAkng33zO8fuU41oy4dcXsCHwep0gQsd4i9n9CmEAZwh0vnpYN5R9BLQKb_7CPD-xr5l8Sb6himY2ojVzcIoTLJf437IRiHdKJKjyZHxMwxlGee3WrZsEkDR49dN9OySSbBnz91ETy4DbTpxVw0Rbu1MkFrigaOYPVtxSbGL5pilhsbPubedwtAkE3IM3LtzgzsvKEF6JYxQ0gVi6vzXXwxHThzn_AQTD59SJ8BpYvg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام عربی مردم اهواز در حمایت از مقاومت لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/439517" target="_blank">📅 22:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198b8ee713.mp4?token=AYi_9TqAc41FPgcakw-lyq22B-Gt3GSOt2aod-DJKOcaSdGLpBg9JOpeocSxvGapUx-H7ws61isqxYtUuV9MWhqUNrW2vZm_VnZMBUs7NoqtHFP3mJD2EsIVoaLzgkvI5VQ4vf4uQ_ti7k0Tm7R8u_LwKtnQpyjpb_PDC3oGp7WlxbaLx4NntAKJKSpl3KYlkfL6cvA2KLDzlYLKFw8LAMP1K0qEctnfFLy38i-xCxkSWaYHutV-B0aRKDV-i5iwBKaOlNF7Cl--8tQS5Gi-cOQWPNrdfxsH1dzHFm_fJ71ANzAGuBxi5SAu4_Vu5yctUJFn28gfiJkCwMzKIGhhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198b8ee713.mp4?token=AYi_9TqAc41FPgcakw-lyq22B-Gt3GSOt2aod-DJKOcaSdGLpBg9JOpeocSxvGapUx-H7ws61isqxYtUuV9MWhqUNrW2vZm_VnZMBUs7NoqtHFP3mJD2EsIVoaLzgkvI5VQ4vf4uQ_ti7k0Tm7R8u_LwKtnQpyjpb_PDC3oGp7WlxbaLx4NntAKJKSpl3KYlkfL6cvA2KLDzlYLKFw8LAMP1K0qEctnfFLy38i-xCxkSWaYHutV-B0aRKDV-i5iwBKaOlNF7Cl--8tQS5Gi-cOQWPNrdfxsH1dzHFm_fJ71ANzAGuBxi5SAu4_Vu5yctUJFn28gfiJkCwMzKIGhhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر خارجه آمریکا در مورد دستگیری یک ایرانی به‌دلیل تلاش برای ترور ترامپ
🔹
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/439516" target="_blank">📅 22:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439515">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=K7NSSIh5Q2FozSHdnodZCR-wC5lK5OsYhEl8nJTONyIJf3uSWxfe-huxtfWrOgXxVuDqSd-gM7y5KbMozL6nY7-Gb2N8NVq29CM0ryoOWP3jKJkwpTyCs7-3OkFZsiuxoxTDbKvnz4XolQ2rqcW3TOrqokJ6e9CRxLitStgSn_4wquUY5KUVYQuDxmUQaeHPAQ_v6GKskhazuDfG_6XForAEkY8sPBQdqXLWUgN7YStpoiYnFctcAnLLIHqLH68z-LLYn3tLOmB5dhGexEWlDKi0XPGwtckunya7cCq5CdaEBO5Ilu3jrv2tqZSe_yHYo5VMKL5lB7EBCXZjgzs_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=K7NSSIh5Q2FozSHdnodZCR-wC5lK5OsYhEl8nJTONyIJf3uSWxfe-huxtfWrOgXxVuDqSd-gM7y5KbMozL6nY7-Gb2N8NVq29CM0ryoOWP3jKJkwpTyCs7-3OkFZsiuxoxTDbKvnz4XolQ2rqcW3TOrqokJ6e9CRxLitStgSn_4wquUY5KUVYQuDxmUQaeHPAQ_v6GKskhazuDfG_6XForAEkY8sPBQdqXLWUgN7YStpoiYnFctcAnLLIHqLH68z-LLYn3tLOmB5dhGexEWlDKi0XPGwtckunya7cCq5CdaEBO5Ilu3jrv2tqZSe_yHYo5VMKL5lB7EBCXZjgzs_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر خارجه آمریکا در مورد دستگیری یک ایرانی به‌دلیل تلاش برای ترور ترامپ
🔹
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای ترور رهبران سیاسی، از جمله رئیس‌جمهور آمریکا بودند.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/439515" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265219d6d0.mp4?token=pGJF2tG_g9ydN7juKestRqDfkmQVCp1KNIjK_rJ-zbOq-vmy0zuveNY12nqOIyTJOXtdz3MpSZNhm6ocWs4MbEhhag3AJHlddu2QVsdwJaheuj1omBShZS4xXRvoOK7Sc2zTt7FiJ-kEumPPacmm_NDlDNzeShdx4Hxt_b4C6xOKj4SetbQ-UEDUyBpxsE-Z2KAw5ZpwljrwWcH5ji4t3-A7fL5KmjT_jOT_9EaG8yhiTymjk7VurPpVxJuOX_SLuxpsfyK9Yioh3B36KH5AjO7K2xko3Lw8VPbV-8rIcvzqcPvDrzaExf7MpqWBL7qL2RH9HZtCXRGRrYrIhk_fHl4XPIqqobIQLoAiPeo0YTB0W3pKsiUK8BsIgWAvlzBlghVEiT7ZlvpUVrGRXeuVbLfjsiMY-6iPSwHFZqnPaY0eHiKEnt7XCwDLRHZq4WTQ1vvXtuWzVpgvVqwk32wMrVN52nbMCCUFtKiHECMfgWLi1MMYTT98VETN8VB7cq9OpWRlbkKCu3Jxh_ZX6VIdKmrb__-44maiOOpexIgoQy3yxh8AbX9LEGm3lDW34MZTiyGPi0jvJY_jiMnnwSGrQ7JDyfISHH8Bbx_xfybb5m5hV75AmqfbY45tH8_tsweuJtIfdqn2goApouhdWLYGebWSVUebZGFKQElj7qefvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265219d6d0.mp4?token=pGJF2tG_g9ydN7juKestRqDfkmQVCp1KNIjK_rJ-zbOq-vmy0zuveNY12nqOIyTJOXtdz3MpSZNhm6ocWs4MbEhhag3AJHlddu2QVsdwJaheuj1omBShZS4xXRvoOK7Sc2zTt7FiJ-kEumPPacmm_NDlDNzeShdx4Hxt_b4C6xOKj4SetbQ-UEDUyBpxsE-Z2KAw5ZpwljrwWcH5ji4t3-A7fL5KmjT_jOT_9EaG8yhiTymjk7VurPpVxJuOX_SLuxpsfyK9Yioh3B36KH5AjO7K2xko3Lw8VPbV-8rIcvzqcPvDrzaExf7MpqWBL7qL2RH9HZtCXRGRrYrIhk_fHl4XPIqqobIQLoAiPeo0YTB0W3pKsiUK8BsIgWAvlzBlghVEiT7ZlvpUVrGRXeuVbLfjsiMY-6iPSwHFZqnPaY0eHiKEnt7XCwDLRHZq4WTQ1vvXtuWzVpgvVqwk32wMrVN52nbMCCUFtKiHECMfgWLi1MMYTT98VETN8VB7cq9OpWRlbkKCu3Jxh_ZX6VIdKmrb__-44maiOOpexIgoQy3yxh8AbX9LEGm3lDW34MZTiyGPi0jvJY_jiMnnwSGrQ7JDyfISHH8Bbx_xfybb5m5hV75AmqfbY45tH8_tsweuJtIfdqn2goApouhdWLYGebWSVUebZGFKQElj7qefvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حزب‌الله رادار ضدپهپادی رژیم صهیونیستی در الشقیف را با پهپاد مورد اصابت قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/439514" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4da4fde12.mp4?token=I8rnbN5PiTRG4ERVloXUTJPsFaj4G_UTFvIgD92_aD0dVf0kzHmuiPOoOE3mjEt10zwUuke6xkAUr8IBKsWXctgIZlI434etYa6HjWr_xZn1Z9cebnBsn3DHxuwdmwqob7lmXqX9_8vfPh2E2j3Ej66GmTEBmEhogx8-4SVRt_Diuw78HqwUmBSZZ8n73J7ZX891e5LYjBqJHddglYtrOQ-42C0dv-kz5fG7i3zE_GBOph3J6WtZ_oBAaEcx07_z-D6jhOHOYzbc9ZduX6qqHpH8WzNLRUuuGIBWZgv2FsFccSZIYz3DLp_BmTHv3LuJGADLuqjQb8XXjk0nLpPQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4da4fde12.mp4?token=I8rnbN5PiTRG4ERVloXUTJPsFaj4G_UTFvIgD92_aD0dVf0kzHmuiPOoOE3mjEt10zwUuke6xkAUr8IBKsWXctgIZlI434etYa6HjWr_xZn1Z9cebnBsn3DHxuwdmwqob7lmXqX9_8vfPh2E2j3Ej66GmTEBmEhogx8-4SVRt_Diuw78HqwUmBSZZ8n73J7ZX891e5LYjBqJHddglYtrOQ-42C0dv-kz5fG7i3zE_GBOph3J6WtZ_oBAaEcx07_z-D6jhOHOYzbc9ZduX6qqHpH8WzNLRUuuGIBWZgv2FsFccSZIYz3DLp_BmTHv3LuJGADLuqjQb8XXjk0nLpPQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مردم در میدان انقلاب
🔸
مقاومت مسیر روشن ماست
🔸
لبنان همیشه پاره ی تن ماست
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/439513" target="_blank">📅 22:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acaaf9a409.mp4?token=BfFmS9f_pMgmo66NLZvdjTe0WQ5qgiuZmrilb3qgnwDxitJU1rp0Akd1AvItRQyr4fG7vrg-luP5J2UEwsAbLnndnomQA0Jwa7VX5BaiArexSzkqp-Aqg5vbCEO9FmSNW9T6QVnOBeVkxlU-pwsNjJDZrejZoroqWUrlyeo90J56RHCFktt_muJVrImNc63CnU2IgKCyNgJwl9fTN0ySteuyRNLCIl2q3mpUbc1KmR43-f7FjCyBjGKGeHr6z_sAeT54jF3R644nqn9_3s9mOt_8Yd-p7q9Ca7i7RaHFHuQsiZaL96UGSAJHPTVgIKLPG31FXm8SCqeuur9-w1XjPyt99pHUWPdT5egyZ99p9XG10IiQdwtRbYQ3lc815AhFyglHX41NO6LhlxrAVfC4GHuRv3OzTdO3KFGNH1l7ACJiImOeh-iB-x20yddmHCpV5LxBfI16llhDNEF2J4X3JvKZ73fsFuAfJghiwitU6iWDHpIxSgOdSzwsyeRirU2LS7R4xFRR83pK7BVOQNhdGQ0Ruo1ToblUK-E-IXsxBwGCrDBUvon6xKYktYwLbGl9rQZ4FxJ4e6kynTu3NL4Li3CnYbSUYuohsPvxEi59qI2-b82pcO5MDH3dfD0Er9OAEKiFZqS4UYysZX7vyMYLIgB4KYOnargYxRjR-nDrsG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acaaf9a409.mp4?token=BfFmS9f_pMgmo66NLZvdjTe0WQ5qgiuZmrilb3qgnwDxitJU1rp0Akd1AvItRQyr4fG7vrg-luP5J2UEwsAbLnndnomQA0Jwa7VX5BaiArexSzkqp-Aqg5vbCEO9FmSNW9T6QVnOBeVkxlU-pwsNjJDZrejZoroqWUrlyeo90J56RHCFktt_muJVrImNc63CnU2IgKCyNgJwl9fTN0ySteuyRNLCIl2q3mpUbc1KmR43-f7FjCyBjGKGeHr6z_sAeT54jF3R644nqn9_3s9mOt_8Yd-p7q9Ca7i7RaHFHuQsiZaL96UGSAJHPTVgIKLPG31FXm8SCqeuur9-w1XjPyt99pHUWPdT5egyZ99p9XG10IiQdwtRbYQ3lc815AhFyglHX41NO6LhlxrAVfC4GHuRv3OzTdO3KFGNH1l7ACJiImOeh-iB-x20yddmHCpV5LxBfI16llhDNEF2J4X3JvKZ73fsFuAfJghiwitU6iWDHpIxSgOdSzwsyeRirU2LS7R4xFRR83pK7BVOQNhdGQ0Ruo1ToblUK-E-IXsxBwGCrDBUvon6xKYktYwLbGl9rQZ4FxJ4e6kynTu3NL4Li3CnYbSUYuohsPvxEi59qI2-b82pcO5MDH3dfD0Er9OAEKiFZqS4UYysZX7vyMYLIgB4KYOnargYxRjR-nDrsG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه آذربایجان‌شرقی در شب ۹۴ خروش مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/439512" target="_blank">📅 22:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439511">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d2f4ee98.mp4?token=udeYUX-UVO0M6YeDE0UT1eGQdI6jdfGXTPsdbGat1X1bDj50Mw9HmaAx4i-AZjmzopap53yl52f06uVvrVlyKwfjGgzWvV78Zl9PblQ46d9bO8Q3Nux0i7QD31C1L18yhneskqeOr1i_UdqyeVxwD6k32wee0i3pK-yumUDKEqEE7YBNS-B4Qcqm0VzVTV0r_2yAlxYlW21Sp7cU8vBRcyCo9aHSoilgo1Fm-3v49oEAQBz1FpKwVoiPHVL23mdZT90aVy7tlY8wElVNmc8Ut0mQl38i_hnXNuBlFZmDp3JHC9u5Vi1bMSDMJSWS-_h6n3DdD2LZhaGphGfTDYU7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d2f4ee98.mp4?token=udeYUX-UVO0M6YeDE0UT1eGQdI6jdfGXTPsdbGat1X1bDj50Mw9HmaAx4i-AZjmzopap53yl52f06uVvrVlyKwfjGgzWvV78Zl9PblQ46d9bO8Q3Nux0i7QD31C1L18yhneskqeOr1i_UdqyeVxwD6k32wee0i3pK-yumUDKEqEE7YBNS-B4Qcqm0VzVTV0r_2yAlxYlW21Sp7cU8vBRcyCo9aHSoilgo1Fm-3v49oEAQBz1FpKwVoiPHVL23mdZT90aVy7tlY8wElVNmc8Ut0mQl38i_hnXNuBlFZmDp3JHC9u5Vi1bMSDMJSWS-_h6n3DdD2LZhaGphGfTDYU7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آلمانی مقیم ایران: امام خامنه‌ای می‌خواست دنیا را برای کل جهانیان بهتر کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/439511" target="_blank">📅 22:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLgg5EEAeAEX7aAzih2620saC8UsX_NHCZtgbn8YAOzQ5nkyAcePb5sPFJ1ZmstaVm24b7SB2s75-TRsYyG_mGf---DG5-QiraMTnMU_dDQP68F6ZUsdTbDYfmrbsClAceSGRRWXWF0LcSNLjV_quJaU_s7BBMHxnZto1s9ocRU0h4RI6NFRUZTHgEwWb4huozDoPxuFq7RsTx0hI0elMxTHUvmOw-JsY7YRGaF_2gihyEA5nfmZ5fpvk9LF41ylbCJjzKtTHzFajL-UarWIxuwfSpFDyoxW3nKb77Hu5URvsmfrVEiuZDVuwhZkRLqHRkZdKQ_oFWamuXEV3kTGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای شهر تهران: ادامهٔ بررسی طرح حمل‌ونقل عمومی رایگان به هفتهٔ بعد موکول شد و احتمال تصویب طرح بالاست
🔹
آقامیری، نایب‌رئیس کمیسیون عمران شورای شهر تهران: محورهای مطرح‌شده در جلسهٔ امروز شورای شهر دربارهٔ تخفیف برای گروه‌های مختلف، نحوهٔ صدور کارت، صرفه‌جویی…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/439510" target="_blank">📅 22:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">احتمال وقوع سیلاب در ۱۱ استان کشور
🔹
سازمان مدیریت بحران: احتمال وقوع بارش شدید، سیلاب، تگرگ و صاعقه در ۳ روز آینده در استان‌های آذربایجان شرقی، گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی، سمنان، ارتفاعات تهران، البرز و نیمه شمالی آذربایجان غربی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/439509" target="_blank">📅 22:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از دیدار سردار پاکپور با خانواده شهدای مدافع امنیت
🔸
این تصاویر مربوط به دیدار با خانوادۀ شهدای مدافع امنیت و پایداری تیپ نیروی مخصوص ۳۳ المهدی (عج) جهرم در سال ۱۴۰۳ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/439508" target="_blank">📅 21:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات هوایی اسرائیل به چندین منطقه در جنوب لبنان
🔹
المیادین گزارش داد که جنگنده‌های رژیم صهیونیستی شهرک‌های حداثا، دبین، صریفا و قعقعیه را در جنوب لبنان بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/439507" target="_blank">📅 21:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69184c7a32.mp4?token=B4Aaz1KAqCbHzIMG8pIoVUTbxJ7jQDfmkS_3jFUy-4WfQGXNcfpg5Biw2pf2TIWHjh5JFiKfNKhRVniiQ5QdXcrBzSyAAgpgMDBDkitrL3K8VySvRdgpPwzr3VpRNN_EeMgBXrB3ZWlLAhft56VANQhpZObkmVcJ9X5iMAUTlGumxG5CvyWn5ouu2R8Nak3qgxk0WUxsWxJ7gRUTCbMa4MMFiMvjcAp_MRiZygFiwuA6tjpcVibYoKF97EaIkqSgYrLrkCmyvidhSThNy-DzW-2-f9aUTyp9EOyzTth5FRVtWosAogKFKS4_kfN7Y_dYItnfUslcRNJioTHooC72_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69184c7a32.mp4?token=B4Aaz1KAqCbHzIMG8pIoVUTbxJ7jQDfmkS_3jFUy-4WfQGXNcfpg5Biw2pf2TIWHjh5JFiKfNKhRVniiQ5QdXcrBzSyAAgpgMDBDkitrL3K8VySvRdgpPwzr3VpRNN_EeMgBXrB3ZWlLAhft56VANQhpZObkmVcJ9X5iMAUTlGumxG5CvyWn5ouu2R8Nak3qgxk0WUxsWxJ7gRUTCbMa4MMFiMvjcAp_MRiZygFiwuA6tjpcVibYoKF97EaIkqSgYrLrkCmyvidhSThNy-DzW-2-f9aUTyp9EOyzTth5FRVtWosAogKFKS4_kfN7Y_dYItnfUslcRNJioTHooC72_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت میدانی ضاحیه جنوبی بیروت
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/439506" target="_blank">📅 21:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439505">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1989d23487.mp4?token=aa1wByJy0FCfTdaVaO8Okz2KN-YGuLxuFe7t9kloCJrr2qd2f19BlG1GbC7s_JOeaOge_w5KoJ9fxYd3jXvPYNx3xF-NIlKOMextXozVJovhd7krluFyOE1M0GoE7oTiwDz3Yha1TV-lwj32nDiGcpl0FYthdA3K2EXJzxgR27juQtGNSjlVbVStn7vPIlDgN3LFlhkAKUZYksrJnYA_IRl40E0UWO1h8LO-xuFTNSMTqhpD8_fCTTCvP623-DpDD8d_LtZrDruvhkth0s9QPyhh7lHxtxVbrNuNEU9LJj4N6I5X0bLRUiuizw8UmUiF-OWmYVA9SHlf8_cV4yftJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1989d23487.mp4?token=aa1wByJy0FCfTdaVaO8Okz2KN-YGuLxuFe7t9kloCJrr2qd2f19BlG1GbC7s_JOeaOge_w5KoJ9fxYd3jXvPYNx3xF-NIlKOMextXozVJovhd7krluFyOE1M0GoE7oTiwDz3Yha1TV-lwj32nDiGcpl0FYthdA3K2EXJzxgR27juQtGNSjlVbVStn7vPIlDgN3LFlhkAKUZYksrJnYA_IRl40E0UWO1h8LO-xuFTNSMTqhpD8_fCTTCvP623-DpDD8d_LtZrDruvhkth0s9QPyhh7lHxtxVbrNuNEU9LJj4N6I5X0bLRUiuizw8UmUiF-OWmYVA9SHlf8_cV4yftJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/439505" target="_blank">📅 21:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439504">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_ps7s3NIwr_EvLkqfw-00HHatktXQ32WEU6rbJzy7NL3umru_d3ITzVZkuAkXHmfoHqrA2A9U51xd4_wYS6ZEp4H1obxc-5rHBOA7JaFyd4uWsi29eGwoojhmy22mEF3tKo5v2EBP_SqIJOjw3SsHMA5q7QydZcA85qmYrjaXAedpRVK6NVCJQJKvTxyRUos0jnbsdGqwajfryfvO5M0iPx6KMyC8kSjEeUHdFTdwPbv1HSXI0lqn1YIIA_G70Npm8nr9h9JsjdxzcI5JdiOoIws3GqgkODqbGDeLp27OoYwRp39L5NJTai_9pdF8kJ9aU4F-3jeWZKmfWWlCqmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش کار با سلاح درجریان مهمانی‌های کیلومتری
🔹
به‌صورت مفصل و فراگیر مواکب کار با سلاح در نقاط مختلف مهمانی ۱۰ کیلومتری غدیر برپا خواهد شد.
🔹
همچنین امکان کار با انواع سلاح‌های سبک و انفرادی برای حاضران در این رویداد فراهم می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/439504" target="_blank">📅 21:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23cf162d0c.mp4?token=b7AeFkDc9yy7ww0WYrnEQBsZf069xQ6fqGc6FIvKk31sQ7TZziKuvZuBLFSpZZcd9Byb5hkkuNK2QZl5jYJhDn7J3Yiv8hvNvoNvq-xSL_hU0Cy0l6ICmBvMquBTUuvsAAAb_-DuQ7PgjggT-23k6z6hzrgFJkOTnam5a-CTaQ2v1CQKYYehp2lxXFuN6AnbxxoVEKDzcrQhmA2npSFmO0My8hzjy-AGuR_M2V4R7hSJImIdpQTns6YO-LqFW1LFIaRkrCVzkQcv5VoEuu3-Nqq7N89tpUTO6HNqJn7Q41TdfDCCpMC2-oBzLz8CqW_4WPROHAVs4XyrYrpV0dmZBDtE8DQ_8cY2RxRO3j3InBwueSVhhikZnbrH-qmf-voiu8berFSQNTs2zCb2PZ_FhmK4VHgg0xfK6fjQ8Gphf2IWL0OBa6fEz5hOrKtWqPDDQqql1RjeVQq4oEIvqwkztHXZsdo6zuW-NsXJD9HR4dfCWyg7w1zGgRMHiI9SVhX8vJzD6SXaay_m-5lXJgFKxo2CncEvmzAXoqFa9aILBKFQAXvtdioFpFddqUWws5FTzTbDHdg7QISyE7RWmRHRK4XP9-nYpcKJBGhHaB247YcQVSLtyO1015qo2SKFanyvJ9WYzNPxd1GNX6p9rNAUOgcrPKQQIREX7C7K7gRLz8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23cf162d0c.mp4?token=b7AeFkDc9yy7ww0WYrnEQBsZf069xQ6fqGc6FIvKk31sQ7TZziKuvZuBLFSpZZcd9Byb5hkkuNK2QZl5jYJhDn7J3Yiv8hvNvoNvq-xSL_hU0Cy0l6ICmBvMquBTUuvsAAAb_-DuQ7PgjggT-23k6z6hzrgFJkOTnam5a-CTaQ2v1CQKYYehp2lxXFuN6AnbxxoVEKDzcrQhmA2npSFmO0My8hzjy-AGuR_M2V4R7hSJImIdpQTns6YO-LqFW1LFIaRkrCVzkQcv5VoEuu3-Nqq7N89tpUTO6HNqJn7Q41TdfDCCpMC2-oBzLz8CqW_4WPROHAVs4XyrYrpV0dmZBDtE8DQ_8cY2RxRO3j3InBwueSVhhikZnbrH-qmf-voiu8berFSQNTs2zCb2PZ_FhmK4VHgg0xfK6fjQ8Gphf2IWL0OBa6fEz5hOrKtWqPDDQqql1RjeVQq4oEIvqwkztHXZsdo6zuW-NsXJD9HR4dfCWyg7w1zGgRMHiI9SVhX8vJzD6SXaay_m-5lXJgFKxo2CncEvmzAXoqFa9aILBKFQAXvtdioFpFddqUWws5FTzTbDHdg7QISyE7RWmRHRK4XP9-nYpcKJBGhHaB247YcQVSLtyO1015qo2SKFanyvJ9WYzNPxd1GNX6p9rNAUOgcrPKQQIREX7C7K7gRLz8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت تحلیلگران غرب از تاثیرات انقلاب اسلامی در ۴۷ سال
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/439503" target="_blank">📅 21:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f77afc474.mp4?token=m1OmztnrTQjP96FH_uFSgRukl9YC4lZCtY12M_dtPOsDUuc33ZAIyU3OzffUkO2vDzsvxW_4XR6nz_l81irexfKforpDGAlK5oegIImoQ-2mfBOUU5hTIlshN1DC6Tswo4Ee-1rhCO203avoryJ_Uyey8Bzpef_GVPSu9CU-ZFWZ3NAVd2fAiJwhPxC9nVhEhIx1TTPYEd_U88s8E0ldWGpXW2Y3ou88s4qFAzTykF128ukkyFhalKF81vv0TGb2Zv12mxYuR9qRJD6Hzx3VqWTblmFcvZY9Iou18ieESqA5o-WyEfhINYjbIw-30rmPSLWLdVT2pt3el7SE-EqdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f77afc474.mp4?token=m1OmztnrTQjP96FH_uFSgRukl9YC4lZCtY12M_dtPOsDUuc33ZAIyU3OzffUkO2vDzsvxW_4XR6nz_l81irexfKforpDGAlK5oegIImoQ-2mfBOUU5hTIlshN1DC6Tswo4Ee-1rhCO203avoryJ_Uyey8Bzpef_GVPSu9CU-ZFWZ3NAVd2fAiJwhPxC9nVhEhIx1TTPYEd_U88s8E0ldWGpXW2Y3ou88s4qFAzTykF128ukkyFhalKF81vv0TGb2Zv12mxYuR9qRJD6Hzx3VqWTblmFcvZY9Iou18ieESqA5o-WyEfhINYjbIw-30rmPSLWLdVT2pt3el7SE-EqdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکست آمریکا زیر ذره‌بین رسانه‌های خارجی
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/439502" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
نام حزب‌الله که آمد، مردم این‌گونه پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/439501" target="_blank">📅 20:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba427bdde1.mp4?token=fI-N0b7wqvuas6Q7DsBWh7D9SgONI78z16ETijCtS4O1KwDepxZ1frI9YesQuYCtTPCunKc2VGdLUJodW0v_Y1UGI5WJhC-lOKDsrZK54XoHwsdLr3mc_KZeYFm51lvGl9rXvylbqIeTntj2PT-ESJzEkNZIfT4EEZ3VggoB9ZZGH_w95Ck-9Bow2LrCDdwG2q06qFwW0fVoALX3alZ0oSdIdEfRdf9FaDXZ105co4h4ule0hFnF4KCwcA7o57dCtVbn7Am39kdpFfq-nO-pPyZqw9Gbs3QdFo6I2tt6DfqrbJdF6-CvrP6JxfJ8Ul_6qeSCzNW675wnuG8l8wbEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba427bdde1.mp4?token=fI-N0b7wqvuas6Q7DsBWh7D9SgONI78z16ETijCtS4O1KwDepxZ1frI9YesQuYCtTPCunKc2VGdLUJodW0v_Y1UGI5WJhC-lOKDsrZK54XoHwsdLr3mc_KZeYFm51lvGl9rXvylbqIeTntj2PT-ESJzEkNZIfT4EEZ3VggoB9ZZGH_w95Ck-9Bow2LrCDdwG2q06qFwW0fVoALX3alZ0oSdIdEfRdf9FaDXZ105co4h4ule0hFnF4KCwcA7o57dCtVbn7Am39kdpFfq-nO-pPyZqw9Gbs3QdFo6I2tt6DfqrbJdF6-CvrP6JxfJ8Ul_6qeSCzNW675wnuG8l8wbEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌آرایی حرم امیرالمؤمنین(ع) در آستانهٔ عید غدیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/439500" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2rB-Crwbnh0kdK0HbfVbb2pVBGJ_07vUSTJ2_1G9Yq8P-PxiD7sg2O_0HfL_LaJj1TXnHpoW7E3n0SKn90KHq8aqi8C0VJjFtwvpbAaXrg57UsR0i30ZXKvp2kLnJSx57H7Gvugxxesf13yTVT8RUXDlV8v5fdFURs6AEamaQf-dkxSP0UUi79-2Qc-CdC4kinCaVXmbnfQmmPzfDw_JkNLcdw6jpbLGdQntMTmKA02qkAilKmNaxBz5mWEo9Y6N71FdPLxoZOKA_4_RyLWVmSa7xurNkIXR1a0x2xlFJ1Er80NNdMlC9tgSOtyDzCzPLmDfAELb3_yoBBNqA80Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجهٔ ترکیه: اسرائیل نمی‌خواهد منطقه ثبات داشته باشد
🔹
آنکارا از قصد اسرائیل دربارهٔ منطقه مطمئن نیست و تل‌آویو هیچ قصدی برای دیدن ثبات در منطقه ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439499" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk338hCk9wvYYTNZ0FkjLegNsCFiCVRo4LhekYtKfd7CROvbsh8gck7uBZQpY5QCibUSVU6YVi2EF_8fplTiozz-IV8zcgnb2S9OYbwi2_iCXnFWNzwtTd-VXzZphHG-vff4R4VOtsBD6i8jxwDqJTnrKA4QxFLcKcQCJgPNA6IgF_AJH0BQXftuJYo9erwfHBmbl-RlHQoM3xKylFTq-eUK4yOr4E1tcQChcTSa1RIjiJ3DNBJJb4MHIAi4uGXxbUqtZcLr4SOzphDKUQw2yDXhyL8L8daMuKcTbBEtg5qB8GNl5VdIRzpUSPil0dazQzb53_cHIFkpg2Pb5IAWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_l8VOYBcYRXRtESNqDy-i8dTupPMJ3-uTO98DA156VHy-nqgQJMSCs9JHaSWgZepDtIa8js_XI5TqhU8YV26hH-_IiSHd_HQnbMPRDTAGLEvpGHD2ysYLaVWbrqzdieEIFXsopMsxgqdV8nmZKI_6qB-_d6OuMmTP1VYkuJmbupSZ9g515w89b_mt6jbTkYct-KBOVBiaPedQZ9kan1VPHI3HNu4NsxuGnaeQ2N1hgT6oS1PZU1cmlikDD0LO7yrOm5L9Szm6yN_bbweOJzBYDNYqbBiwCTxiLvoaXLsE4O28rNPBH-5yJ5_A0WG6iUBgjtMbeN4jSpVBe-yx5nMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTofreXizbHJMbiMrWpZ6VJnvy0JqQOzuU8fWpV3cFilT6-whGqzRdwCP4UwwldThFzdhDBzFQmPoOQ2xwNRi6rFblrli0y6uOzxa-JgtXpIiEydzsSOyNWctMBAdu9p6Hp8OVq-yrFT9zF8zyN8bZ4JOj5n8K1LzcKhIAl3pxs-Rf684-jRuuUXm8bWSTEK1nr-wtFM_GtVa07Of5Vl_2wYItLIZX1_o1Rg6cpT88upYiIR4X8u6P1siy46ZkbwLbF_Jg03dxRscfRMEwImacZrtt6Wq8tdyqXqjgkCkICz2hD5Kb7nFl44L_UXt9EbhCO0IQCmrrutLzL5OABiJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2QZiKRThpmQ6uHUD-1MoxnxGqKKIMOCYdNyn5Kk_jNVhr0SK41xwF6At2oqUPV6pOtC0QGUxJ0-KHY6G9yckJteV1-STXCaUDwmVVD0ub69Pp6vSzehA5yU4Mrk1g_1No6RoPB7G5ZlF68z3J750fUWrjRxu7qzCg2aQevjeM4jVxGNXjBcsJPBZEG3lOuciA2IkuXImrmCPHi8Z6ETVM623EvUuoT74-DxE7c3AuNvIJHRDjODeAH75YxXb8HtL3cYjKlcHJZE2hJ4OFmiJ8xwzKyTPs3J9_xuX0fWpXgHCvnu3o9G_8_J-HEk9XAKvBjOKZHZHh607ec7G3Q3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-93QCUu1Eo2QLoX6vZrIpDLgdcTss2B1cu78zr62hfsNjLaPdmzU7iCJ5IZU7xLoO4pmgIu0IIc-9hVZ2yNwcG7m_rhNzFd7u5wTnk0EMLRYL4zVmUHTguNsykusa_T63yvNPoNZXikET0PyHwM-icqlYIYieSwJE6DevoCMu-TAoiq2or_PKpKQsxWeQ1JMM3BMW2d2AJxypUlUaLUwENFPeVOvh8FUUU2RwMeePhLKsDJy_622EHH1OrsNcsmCq6C4Nu63ZB2nAm86RXR03F1AU8pfsJCZoMSsZs0Djl5Nfc3V5FRtOCGudxnojw8izPm9PCXcX2toLbJqXXscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdqoXJ6w6mcuaJkdL3WJMUEk18EGbifXGo_CPdbCG8G5IKIXg8CjcjJYm3D4aqzXB791FXdOPcwOi37ffCgLUgP3Va0WZAS8b6faQV67qC0P1SinRQhSce_xn9eaL4cIBWetr2TZnchuRdHVQEMwfqBmgCt_FOJdZdWvTwt-dmkiOy3uMS5naD8Gcto4KqwjLok6NT_tSGXfUSt2S9ThtTcCn22u2snzCpNkbrDHuGG5-EW2u_nXA3J7lemFzXzylGW92tmiwwlHQIXh-Y3cHxJg5ImULi_NdqPbH32i9MaxtqVqpizaQ9sCpeC0Kse3qtH4Sj6xjpX6xjT6bu_3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8DIafQgtx6EpZpqazr1l_uY8_iHvHjRADblRZ-GklcOQLnL0xjm1IL_L6NIcXqUjQgueVBF7lqDCm6brn2iJiKhUs0iMIWMXyr8zPwi5dvslSW0Ge_FHqGWx1nUzLk0-8E9taYzYr-dd0OOMEoJXn9dGWCR9Q1JSi3zpKrjQYyy3ghry-bG0l73WQWQ1uycyGOesj3isRHdfM0QingQvUP5D-QeGnSTgdo4gGcCJ6qAa4x5CPCga2cUNJxDIcsCNeMORgyEvnEleAKq5t5SkvCZvEAgnDXfQAikulhYV07iBFGRA8vJ4NrqdCLu716RP1VX6AXVyvPAXjzR5bWkoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کشتی‌های متوقف‌شده در تنگۀ ‌هرمز
عکس:
حسن قائدی
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/439492" target="_blank">📅 20:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32491dacbd.mp4?token=DlZPaBaL-GCsaRzZWsY5xIHNkSuKXsTHTxkO94DECxV4yOu_i3yGLDgULxSA4Zl9FTDxM2zbE6ITMJLUZlYXR2kSY33iXXCct0U91VNzmopxfi0_0uFwC_dpM28-p5VIZj7UP36lVJZBcicyrHOGAyk1E_DAusldTwETrfixQu_hzmHZcJdrtYHqRVuGGJmZUuXG8HI9efuI52QCKSw7v1dSQ1WUA3cLD65our_yn__2-2ad7633yz8UN6jXQPEacXSeHwyb4mhhL_oCW0ikiNhiO-459BPug4hNca5mL4CbuKgbSUqSgn2sGd6mPFDBqwaqRGsYKUkdk7XTzvMX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32491dacbd.mp4?token=DlZPaBaL-GCsaRzZWsY5xIHNkSuKXsTHTxkO94DECxV4yOu_i3yGLDgULxSA4Zl9FTDxM2zbE6ITMJLUZlYXR2kSY33iXXCct0U91VNzmopxfi0_0uFwC_dpM28-p5VIZj7UP36lVJZBcicyrHOGAyk1E_DAusldTwETrfixQu_hzmHZcJdrtYHqRVuGGJmZUuXG8HI9efuI52QCKSw7v1dSQ1WUA3cLD65our_yn__2-2ad7633yz8UN6jXQPEacXSeHwyb4mhhL_oCW0ikiNhiO-459BPug4hNca5mL4CbuKgbSUqSgn2sGd6mPFDBqwaqRGsYKUkdk7XTzvMX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ حزب‌الله ‎۳ تانک ارتش اسرائیل را منهدم کرد
🔹
حزب‌الله: در شبانه‌روز گذشته ۳ تانک مرکاوا در منطقۀ «بالوع» مورد اصابت قرار گرفته و منهدم شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439491" target="_blank">📅 20:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdt2F8TSeIW0FnS0sdRDaBn03ujohqYSXqiI7t7XQmVCQgPv5PFnaiYQwLgUZa7Tu1cAQlbqoceKhtpomEmJYMxEAwL4X5SWFfDRrfqHo_pBwEyV27ofJV3JbNw-4oySL0pdote8m1cGO0V5LQZrH3RIwgNmcF0PeNUsihIVxkoGwU8MmYgUzaLkPkyqlh-ReM8V1hsK01DX2-YW4eyjYq_iFHNLcprYlXfkEQRe8e6crO9JpeiWa0IrtKgVjhp2B5Cc1GW1x37nnTtTDGxfnvM_MTyX02l_JrZ4RxeLMiA2EztomqC5dqXd0Jgib-3cWpWMHcThohfyBSZEL-bx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قسام: خیانت بر خون فرماندهان شهید بر ما حرام است
🔹
تا زمانی که دشمن  تاوان جنایاتش را ندهد، حساب‌های تسویه‌نشده باقی خواهند ماند.
🔹
دشمن بزدل ما تصور می‌کند که می‌تواند با ترور رهبران، ما را تضعیف کند؛ اما خون آن‌ها سوختی است که کشتی ما را از میان مشکلات عبور می‌دهد.
🔹
ما هنوز در میان خود رهبران و فرماندهانی داریم که در میدان جنگ رشد کرده و در نبردهای گذشته آبدیده شده‌اند.
🔹
ترورها و تمام جنایاتی که در نوار غزه شاهد آن هستیم، میانجی‌گرها و ضامنان توافق آتش‌بس را در برابر مسئولیتی بزرگ قرار می‌دهد و دیگر سکوت و بی‌طرفی پذیرفتنی نیست.
🔹
ما بار دیگر از همهٔ مسلمانان، دولت‌ها و گروه‌ها می‌خواهیم که اختلافات خود را کنار بگذارند و تمرکز خود را به‌سمت دشمن اصلی امت اسلامی معطوف کنند.
🔹
ما سخنان مردم غزه را دنبال کردیم، به شعارهایشان گوش دادیم و شاهد راهپیمایی‌های آن‌ها در وداع با فرماندهان شهید بودیم؛ خیانت به این خون‌ها بر ما حرام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/439490" target="_blank">📅 20:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd0bb0971.mp4?token=q41FG78pYAYSpK-99ceqH5KORNT_GdTqxW0Jl9NWNN0wiqMo-rXPeBlKPdMH-n8sgeCylaro0pLFsBw_rTbyL5krWkepE4m4OksdpQEJieDwwazIERyPwMAscvbIwwRK1v0Q0R5h21_Wav4hmd4f8l62GXXF92AjblWS_l_CKbEBMLYcRvk4WyCTwmURKVfYzH7ohTm2fLZpHDiv-EDTwIOD_DItilk5btRx0ilLe5SeggnDk-3VdlEttrfyEFBkoGLmVdpRS4k84MRsMX-bTQrCWJc52NmSc0KPCIWqneLWPjZvx7m0bPcz8yKLQYa7kIUBwvi7AUIozIRJITeTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd0bb0971.mp4?token=q41FG78pYAYSpK-99ceqH5KORNT_GdTqxW0Jl9NWNN0wiqMo-rXPeBlKPdMH-n8sgeCylaro0pLFsBw_rTbyL5krWkepE4m4OksdpQEJieDwwazIERyPwMAscvbIwwRK1v0Q0R5h21_Wav4hmd4f8l62GXXF92AjblWS_l_CKbEBMLYcRvk4WyCTwmURKVfYzH7ohTm2fLZpHDiv-EDTwIOD_DItilk5btRx0ilLe5SeggnDk-3VdlEttrfyEFBkoGLmVdpRS4k84MRsMX-bTQrCWJc52NmSc0KPCIWqneLWPjZvx7m0bPcz8yKLQYa7kIUBwvi7AUIozIRJITeTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آمریکا: بسیاری از کشتی‌ها فقط از ترس [تهدید کلامی] ایران در تنگهٔ هرمز تکان نمی‌خورند
🔹
ایرانی‌ها باید اعلام کنند که دیگر به کشتی‌های تجاری که عبور می‌کنند شلیک نخواهند کرد یا تهدید به شلیک به کشتی‌ها نمی‌کنند؛ زیرا در بسیاری از موارد کشتی‌ها…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439489" target="_blank">📅 20:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=HABUc23hDnGToUyR7PZjqcXjxlNbN_uLDEb1Gu_JFv-0B2zwMAhmIZRt3inEmGQ1BCn7gC7S4X4jHG2MjsgfvUHAU-C3P1wrf0jQlZmxpYHwLATXOhkpqqNftu5Q3zzUlC8OD8rC6Nb7KGBtUeR8yYhtSPmXy3D5H92XIJ3HJQKS5tYZFv_HmwdVpm5cj30xACRpoKAlgME-sAhCoVYSePbAagC_ZgwkxYWmonk6iNlNKBPBYbm0nZfE4VNepMijvcJ29duZmM0M9hSoU_vR1V1geJYJM12CVGMww8EJk6NoOI0e_D61msxVFvQpo_HeI0-SodDfM8i7CgyC5JQ06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=HABUc23hDnGToUyR7PZjqcXjxlNbN_uLDEb1Gu_JFv-0B2zwMAhmIZRt3inEmGQ1BCn7gC7S4X4jHG2MjsgfvUHAU-C3P1wrf0jQlZmxpYHwLATXOhkpqqNftu5Q3zzUlC8OD8rC6Nb7KGBtUeR8yYhtSPmXy3D5H92XIJ3HJQKS5tYZFv_HmwdVpm5cj30xACRpoKAlgME-sAhCoVYSePbAagC_ZgwkxYWmonk6iNlNKBPBYbm0nZfE4VNepMijvcJ29duZmM0M9hSoU_vR1V1geJYJM12CVGMww8EJk6NoOI0e_D61msxVFvQpo_HeI0-SodDfM8i7CgyC5JQ06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف روبیو به همکاری گسترده امارات با آمریکا علیه ایران
🔹
وزیر خارجه آمریکا در جلسه استماع کنگره از همکاری برخی متحدان منطقه‌ای کشورش برای مقابله با ایران تمجید کرد. او از دو کشور امارات و کویت به طور خاص نام برد.
🔹
وی گفت: «فکر می‌کنم متحدان ما در منطقه همکاری زیادی کردند. همکاری برخی از آنها بسیار شدید بود. امارات مصداق آن است. کویت عالی بوده است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/439488" target="_blank">📅 20:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/977b5ddc95.mp4?token=NX59ukT_0QPi8w-g89WtwJIY_Xckcb7FN0-qqJseX3l_dMR11i0JbzaF69wf8rfVMC7qACalGaNAJPTKrO69nKI9iikoGvI14BKbnjXMSFZGa1SbGA2pwaeCNwHIvsmr26HD_2Xp9uusg5mBZFVRlrm135kPxwoTFWYtPY2UDoaUHWvKWy1Uq3tztBI5UM4v4IAh_63HPXwJMf19aRET6MX_uPHy5fbcnBxZ3ETrTE2uihHRE7LW7lGliVEm9krc2nppcbtdqCQgUp9y131MMwlKCNTDOELo6KmIu0-9RQAGWK56jhHsO8d3UJmOl15SMnH6qDZjXdyOd4WjhokdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/977b5ddc95.mp4?token=NX59ukT_0QPi8w-g89WtwJIY_Xckcb7FN0-qqJseX3l_dMR11i0JbzaF69wf8rfVMC7qACalGaNAJPTKrO69nKI9iikoGvI14BKbnjXMSFZGa1SbGA2pwaeCNwHIvsmr26HD_2Xp9uusg5mBZFVRlrm135kPxwoTFWYtPY2UDoaUHWvKWy1Uq3tztBI5UM4v4IAh_63HPXwJMf19aRET6MX_uPHy5fbcnBxZ3ETrTE2uihHRE7LW7lGliVEm9krc2nppcbtdqCQgUp9y131MMwlKCNTDOELo6KmIu0-9RQAGWK56jhHsO8d3UJmOl15SMnH6qDZjXdyOd4WjhokdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریس مورفی، سناتور آمریکایی خطاب به وزیر خارجۀ ترامپ: تنگهٔ هرمز به‌دلیل حملهٔ ما به ایران بسته شده و این پیامد اقدام نظامی ماست
🔹
در حال حاضر تنها سوالی است که برای مردم آمریکا اهمیت دارد این است که آیا تنگه قرار است بازگشایی شود یا خیر. @Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/439487" target="_blank">📅 20:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2ba0c1ae.mp4?token=Z1PzxdY95ZjPrHi_ZhrpGRJCzLko0D64xdAqQ89zocImG6CdTt5eU7245jQYHW56klT_x_mf45la7LiKnBaeXDFGbzjAhsTYaBVR8SE9A1_DfUD9x0-lrSO_57_aRgOGJA0AQmn2IXRYJwUyS7wOHN2rnA2vI8sPvY7ZNxGlYeJZ2Mnxd-cZPa3oqEU-JPWDx24W-1jgzKYncxRPob9XIUj2Wn44Q-2h3LBYQvatPnPfDgYXyUhhZW4F1Aqv6xvPb28XbaXGKQdkfm7wSeavKxMcEnOCx2fSPWZJA6rt5HYI6NFj8wf9sJN1LtBNfXS5hkcuwA6_TUizSx5bUUuMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2ba0c1ae.mp4?token=Z1PzxdY95ZjPrHi_ZhrpGRJCzLko0D64xdAqQ89zocImG6CdTt5eU7245jQYHW56klT_x_mf45la7LiKnBaeXDFGbzjAhsTYaBVR8SE9A1_DfUD9x0-lrSO_57_aRgOGJA0AQmn2IXRYJwUyS7wOHN2rnA2vI8sPvY7ZNxGlYeJZ2Mnxd-cZPa3oqEU-JPWDx24W-1jgzKYncxRPob9XIUj2Wn44Q-2h3LBYQvatPnPfDgYXyUhhZW4F1Aqv6xvPb28XbaXGKQdkfm7wSeavKxMcEnOCx2fSPWZJA6rt5HYI6NFj8wf9sJN1LtBNfXS5hkcuwA6_TUizSx5bUUuMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: جز ایران و شاید عمان بقیۀ کشورها موافق وضعیت فعلی تنگۀ هرمز نیستند.  @Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/439486" target="_blank">📅 19:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bebfbc53e.mp4?token=A7IQ1ec2QHT26qPQqKINjkEBvsSOVrhiiMSXO5bV6wqmuw93q5B2ZeRCEox47UQTFBw0f8P_EKGOtKB9APZoY3UHmfFaKgAi8o9jMMJqrHCW69476f1JghfzSccuuSXG0NKL1OYoyHCZXv6T_7N2F7op35VbRcOWROcJHzytUOOYtCTW6yx9gtAhIZytzyc2w_-awTK0KVlPamPG0n99D2TLmEaZ1LUNBF6F_M1riXj74jqH9PJw5XYvwHukvFAha61rMQ2VeRzkr-dOokG7n7mYeW6pBP5-JnragGvsnlNabRzd_769ODJ1qSnUwTDLh4Yx4dw9vRnsUlJ8bhdEJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bebfbc53e.mp4?token=A7IQ1ec2QHT26qPQqKINjkEBvsSOVrhiiMSXO5bV6wqmuw93q5B2ZeRCEox47UQTFBw0f8P_EKGOtKB9APZoY3UHmfFaKgAi8o9jMMJqrHCW69476f1JghfzSccuuSXG0NKL1OYoyHCZXv6T_7N2F7op35VbRcOWROcJHzytUOOYtCTW6yx9gtAhIZytzyc2w_-awTK0KVlPamPG0n99D2TLmEaZ1LUNBF6F_M1riXj74jqH9PJw5XYvwHukvFAha61rMQ2VeRzkr-dOokG7n7mYeW6pBP5-JnragGvsnlNabRzd_769ODJ1qSnUwTDLh4Yx4dw9vRnsUlJ8bhdEJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آمریکا: ایرانی‌ها می‌خواستند یک سپر متعارف دفاعی برای خودشان بسازند و ما به‌همین دلیل به آن‌ها حمله کردیم
🔹
آن‌ها قصد داشتند آن‌قدر موشک، پهپاد و تسلیحات متعارف، از جمله یک نیروی دریایی، برای خود بسازند که دیگر نتوان کاری در برابرشان انجام داد.…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/439485" target="_blank">📅 19:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49bb2165b6.mp4?token=IXruNjteCRM-QtVcoRqIybxFdlfO3yLaynFLh7PQH-rErpbbxbseV8NlNlGFKeODbND12CmeJWpVv-umWZvj4kkF-1iA50qXKvWbbiJ8inq8wlJHp_-wnGNB3ZYtdS4mNyQlimfbM9VETmln2OxpErDBmvRW6_ysCmDWGzRu0xmuaFLz9rPHSvJpLRM6Ub0bVdNrusx-coKaVQ1NxEVDgT0ZgRi_rXnLM2L_klcQt5w-WsTESHCN0nOOG-AFQlXL1_X50AV9youCGLlgwnl7QvZ19TCFij3yM0tkneudRDQB2RSSY6rMAcScMmJxQBb2ru9SGxVmAJMWloj6DQB9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49bb2165b6.mp4?token=IXruNjteCRM-QtVcoRqIybxFdlfO3yLaynFLh7PQH-rErpbbxbseV8NlNlGFKeODbND12CmeJWpVv-umWZvj4kkF-1iA50qXKvWbbiJ8inq8wlJHp_-wnGNB3ZYtdS4mNyQlimfbM9VETmln2OxpErDBmvRW6_ysCmDWGzRu0xmuaFLz9rPHSvJpLRM6Ub0bVdNrusx-coKaVQ1NxEVDgT0ZgRi_rXnLM2L_klcQt5w-WsTESHCN0nOOG-AFQlXL1_X50AV9youCGLlgwnl7QvZ19TCFij3yM0tkneudRDQB2RSSY6rMAcScMmJxQBb2ru9SGxVmAJMWloj6DQB9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات هوایی اسرائیل به شهر برج الشمالی در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/439481" target="_blank">📅 19:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96f32fd13.mp4?token=DjNwJz11j_sCbOAB9JN4kjk4VqK_nsKABYqdSTyLlg86-7ISG02UZ5DRDb2qhUdbWQRonHoGEv1vST-ghsCUFPQcmHX8DvfKzkktk7duABzda0QQ9hNfrxYDclN45yVRPYAInxqhQ71WYN_J0aex3iG_nk1pHlxINIut31hIcA5hILLbWN-D3uvlnLZt_TXzBP_DHKH2yNvrce66oz-gSZWLrfeeApEeohjoDSPFDnmiXbvelGG-BOW7WyW24sFmFSKIy-cWqbji9gz5c333gDWqkmM_VcALi8IkvsNFOSGKYZLY-7R0miNOK8bT4gNbD7Dpxs-mKF4V74KZEsL6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96f32fd13.mp4?token=DjNwJz11j_sCbOAB9JN4kjk4VqK_nsKABYqdSTyLlg86-7ISG02UZ5DRDb2qhUdbWQRonHoGEv1vST-ghsCUFPQcmHX8DvfKzkktk7duABzda0QQ9hNfrxYDclN45yVRPYAInxqhQ71WYN_J0aex3iG_nk1pHlxINIut31hIcA5hILLbWN-D3uvlnLZt_TXzBP_DHKH2yNvrce66oz-gSZWLrfeeApEeohjoDSPFDnmiXbvelGG-BOW7WyW24sFmFSKIy-cWqbji9gz5c333gDWqkmM_VcALi8IkvsNFOSGKYZLY-7R0miNOK8bT4gNbD7Dpxs-mKF4V74KZEsL6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: در ازای بازگشایی تنگۀ هرمز، تحریم‌های ایران برداشته نخواهد شد
🔹
تحریم‌های ایران بنا به دلایلی مانند غنی‌سازی اورانیوم وضع شده‌اند و تا زمانی که در آن حوزه‌ها اتفاقاتی رخ ندهد تحریم‌ها برداشته نخواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/439480" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75788cca3.mp4?token=Od9qt8CUu1B3CLuyJLtOqJ0oEU-I_VS0TTYVxH8HsbcPSIt5r4_eO6I7YBz5zpc33ypOiEYmxV7kTI09VzJS3yKVpe99RXgC5639gbUtQyiWuAeM7ewc2HNQQnRJy6a8XYKg9CVSZwR-Bsne0x81DkEO3lk9eD_8t4uKuV8gH6BaDaLvmI-p-JIjzLfrQEoQNN7eFRCwO3H9-HeegD4GbftbFbRcZiq3qi9zIigGwrVjl7-TxBAtmYk-engICmlI6XuOiWMfuiOWwSRfK2uxYOpOocrNzp9HfJjSkrjZsLVC35ankVdsxfAyiBNVAhk4hwa1UQIkw1Z8-qlyASHenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75788cca3.mp4?token=Od9qt8CUu1B3CLuyJLtOqJ0oEU-I_VS0TTYVxH8HsbcPSIt5r4_eO6I7YBz5zpc33ypOiEYmxV7kTI09VzJS3yKVpe99RXgC5639gbUtQyiWuAeM7ewc2HNQQnRJy6a8XYKg9CVSZwR-Bsne0x81DkEO3lk9eD_8t4uKuV8gH6BaDaLvmI-p-JIjzLfrQEoQNN7eFRCwO3H9-HeegD4GbftbFbRcZiq3qi9zIigGwrVjl7-TxBAtmYk-engICmlI6XuOiWMfuiOWwSRfK2uxYOpOocrNzp9HfJjSkrjZsLVC35ankVdsxfAyiBNVAhk4hwa1UQIkw1Z8-qlyASHenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید نمایندۀ رهبر انقلاب از مدرسۀ شجرۀ طیبۀ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439479" target="_blank">📅 19:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8oEFcDyXMTJhNzrohvd8RqaJACxxPOSnw61rOdF8kMDEuSq_PH3RnAS4WjQpCDq2Coq8kqfjKhnxczUTYnQdXjvZXr813SGsNaBNjLjFus1JP5sfvXKvAbrfm54vUQ1PN8GhNAZ-t7gxCgBsdfwJK35nqEGTkCLmfKed2LITshbMJGrQIN6sxGQA8IUJ8ZrMudnwtQ9qH4nPRf_kFU4wqOSpnVGn8PSUcpbxFGWJ7MWhmUklBxM4LadS7dv68xzV4gJ0RojOAsB11jyOivNAV2yA1OHH7XHUt5EXBwC64ZyrqJFODJV5mrZi3fL4UMRBThTyMnmExiP_WBCWh2F2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwDcki_UHy0X8xTvy4P0uKP0vnJgwmR2QHMxZ4Boc6rop6dQtR7hXkta7kkyZaANQ1HQDZeiVAJ33h57jXW2DIbnxwnMyeL1RimtNv2dgZuVRB-oL0g_ecn_ueX-HMFM1NahE8RwVjAdqCh3LEXW-0tV0sGmXZ3MgVspy02aCnHOngJWzLEd5s72wA8Uha7RYALkiXciWrf1EI1FyAZefhBSeiYW_20nqzuyiNzJMPxiPFS2QNGSrrXTTwP-36fb27GPwKdKPyVQe7Hsf9nPnTBVSOnX7NQ8LF3_YdKVsqb0ydDRq6x_WMUQTnMJgRtx3q93shLC3efkfuqB7rH5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBzEwRg--th-oOqA8K7hPznDc3vj_bkRzHv0ElN4gENgmkleteN7KLet3eajQk_8ItU1SeIeLrodeTKW7GsuUukGRIrSMThBegwCUo4hMUJ9biB7Nl2pqklEnsl2tEOpRAgAWp1UcCg7JjTOBzfdiWaWfqlU20FRYqVRLD-tbR5zOuS3WKf8uU5ucgLr8wi8R56vhBg3j6xiUqxL7tSgkaagwJKy7W9MYBQJsw1967GCQUz6YSQuboxwFkCrOozUpXqxDf755kPkwN90gq-ts3KW3YSJ5VT94YkFqGn8Pt4EymdB1KqvxelwfDdPHbB8T3tVdTJnfgCZfK24EAQZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOjYIHJ4uNayka_MyP7xDCqisJl4l3S5lzTga-cFXCMz3c_WuVL0SOzxoOVYoetRc43lrldPiDJ9_yg99Lg0Qyov9iK8dxhZWb-FdxbNWq6VNz1J6AeBtwe0mcZA1Iu3Ql5cxpSc3qthJ2O6PN9AkNjMPO8kH5MQYKsK7Q5TyA-pmrmX8p1kLCwY23hJ6_K1M1sn1SywSAnH6PC8B51ApP1Nb8N48rfBrPpHfzG2_gQ89L8ax_XejsI_hKHKM8SNlxH3lvm7H36wXCRz34BTUakyMy6Xod0dqXmW9JLvmJUaeG0ualwTWihRNYDeDqG1i--Sb5WeNOELMPI8dJjatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLNZy4obZHUV9BYsxod4q6kBfcUkjSk4MOS2Y-bNRkjB5hgbxL1f1Z6GeUGtOiXYeOotu_ubdMQ6sgJTCjEIp-SGOWoFmTIx69EKOBMr5c0YIZeiTOjqsLQ8yM7jlXJnUjfX_wBZPLjzVgyqtZ3ae6rhDeI1XpedrY61E_zXr2qQilgRgENJPxaCVzKlxJZNrFgC_weoDYs1ati7Pa4MYeQBNkZh5x7X5HXIC4BGaQ1YI7Fg4z1ED3FOrdrnBDq4SgKQPMQ8vR6RqhooBrIfl9fB9ei-iUyZEx8xhjBnkAzT9BxjQfKFD5Q72WOLwhqd7jypv_jdgEcwWSFqMCArCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtQlteEs4KIIaafkAWGzdW6x1WJPAlWdd9bONN9F9VHvZ4mKn5sguI33JoETa1O1t9K_gK_OzJyjKLPjoCfIgXJXTQynqkNbzb-WfKoyhB1faGqh0BKRtQ3YDcOwMn-On6ERHpCpTIHKRzkqD_JLWx-d8uog5_-8lZT2SdSq-no4piK8lx0SHu5MJbQH1ei8DKgJm1tXAHfU7lomeg5pax9F7SweYMBZEgSmPhg-FbrN7wCMD5gZez49V0hj1y13EGvBGLj63fzXy8RMUxS-dFG4NCIDhslztknYpCt_BDYGS3tdX4RV1ze9QdnW2QEdHbYgNuosfCWQRV47ZYuHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPAxYjPgTCVl4Yov4h_2P4c1DFyFgjss7LEA4jH7MmZTQEE5ZcjIxm7T5AnFJYVk1AhFb2twm6nOpSvvAA6XoC5QkvvF9eG7KEmy52Y5LZKxMGRfkaE3l73LP4-YRJF2y3Mjlfy_yEOG4LR7L8QC-Rj-4mly9Q6G4M8DLC28ztK1pzmOn9SjNURClzGNM-2BlcSArdGvZNqno-3BMomi_C7H-tz8woX6c3q725TGK6CxEE3dHSlsyAJ9H_q6R83ya9lta5517IAz9NygPE-v0EmattiuhduSorhUHhc5Q4uuCTl8X8pY2KPIa7TSgWdbjVy01erVSov31xdlHg4JEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشاغل زندانیان «رای ‌باز» فشافویه
🔸
زندانیان «رأی ‌باز» افرادی هستند که با تشخیص مراجع قضایی و در چارچوب قوانین، امکان حضور خارج از زندان را در ساعات مشخصی از روز پیدا می‌کنند؛ که برای کار و آموزش در واحدهای تولیدی، کشاورزی و صنعتی حاضر می‌شوند.
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/439472" target="_blank">📅 19:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA9AaPmn3laFsCcynUXbqw2R-Hr3MDEMx2mWUyGG30dNgyr_07uRlKEv_TemOQYBG53xdoJbP9tAcbXOjZ0N8olFxk0-xyIYLgwgEk5do_d4RLD1FolAnmulwilj7gRko6H5ChDXXTRQK7wnXl7bjg60apANPEmTcorXRUQcfGXQw__lmVuFOIrvG_me63MSo34saxffuw21TIDHLvOnPqKqacer5Qto9VodU14cEfYzwIpDW_2tKyZRjTdolkmW_gF4afOW5vgqMCFwXaZnVhc9-SfTGl1h64WgpiRgeZAlh60cTp-TRV6Ou-BmjD3pPlKn7pts48TaXy2lSc9ncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هدفمندسازی یارانه‌ها: بخش اول مطالبات گندم‌کاران واریز شد
🔹
در این مرحله ۵۰ همت از حدود ۱۱۰ همت مطالبات گندم‌کاران پرداخت می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439471" target="_blank">📅 19:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6AQ9qJlkA5pYchDVHAE8FZUcTnVeZAVmT299IDlu3swxd7drsjYbsnhAQgaN0RwegPiHt9L2voycntfg7gOTqrzCZ4uLo-kjZuB5vPRyNrFNY8uvC_UIfwdYAKPgjcN7i2RFdo4hBIDaOVA2ks0PALSb6AeZHvQ-f_a-5ECrBV5OtMiuyKIoQOuz1J8uw5x5i2Pdx1b8dlwmhgiUMWWfzv8QgFj34-NOHQBBxeQHc8zToEnB6fAyaHyWu3w-T1y2Q57Q9cR-9GqagcahiS1w6Hxk6Zyb4BTy_eldY_a21dxgyTb706YYWRK-7yXwn2U0m1OIjPD__y8CvsnriuMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم اشغالگر: ما به لبنان حمله می‌کنیم ولی حزب‌الله نباید پاسخ بدهد
🔹
درحالی‌که صهیونیست‌ها درحال حمله به لبنان هستند، وزیر جنگ رژیم اشغالگر امروز گفته در ازای این حملات، حزب‌الله حق ندارد شهرک‌های شمال فلسطین اشغالی را موشک‌باران کند.
🔹
او همچنین…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439470" target="_blank">📅 19:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVSTpvkv3IGRZpqaaLR2ASd5JZQPA4UJQV3cJitcdZ6LzrfCWlwgZTL3eDdw5AYFtx3Yy8IYxUd2oR3h8s64FIGJSlWDOXwWHxUDwnuzCN4PbCKi_QoBAiOCRjsjab9xgqioI2_0EsnSg_kkuv-tvfM99vDdmvaezAtgLeg1GEvh5L2KECSnO1de3hBOUJ2Q6RJPeQgESaheG0PZJgwBC01uUkb7i6TlCp1MUMvig1pPQ3xpLqa2hNdTX58lkhgp-FrqemKd9glxvd2Nodr03mELJ2wovaFCDOCT8Zt-aMhpxtCywsgobe3XFHz7pqBHQIb3JOwibgxui9FpqPiZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله مکارم شیرازی: دولت برای حل مشکلات اقتصادی برنامهٔ جدی داشته باشد
🔹
آیت‌الله مکارم شیرازی: آنچه امروز بیش از هر موضوع دیگری از سوی مردم مطرح می‌شود، گرانی سرسام‌آور و لجام‌گسیختهٔ کالاها و خدمات است؛ مسئله‌ای که فشار زیادی بر اقشار مختلف جامعه وارد کرده است.
🔹
باید با برگزاری جلسات کارشناسی و بررسی‌های دقیق، منشأ اصلی این گرانی‌ها مشخص شود و روشن گردد که چه میزان از این مشکلات به دولت، کسبه، شرایط اقتصادی و یا عوامل دیگر بازمی‌گردد تا بتوان برای آن راه‌حل مناسبی یافت.
🔹
حداقل انتظار مردم این است که احساس کنند دولت برای حل مشکلات اقتصادی و کنترل گرانی برنامه و اراده جدی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/439469" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJT7MQNrv3hdgGpwF1qcBv1OumvgcN0PS_ShdqVGzatjFwteKX9Zk0y0fV6lj-C5it_2EPZMQJhPiSLGewkd9TKanxdk3pbIqurMANI4qIizlPSCfDt68KlZFl1HqN0scIX2UmQ9i_RCXpE4pFPL-dYAfcKhhWgeVULzU697gxwPrIrOzjx-duPQjPGxs3ZBIHyben7jIlO7eW8ibYEqOSRLAQvJ0d6rQib34PUONwojK7t2huSb45olPR5244tM6f4vICMPs0rBDWwvfqxj-mxVv1jGBMwdF1tYAlt8jJt0YXVKSgx4Q2rnux691ErlYHaia35R7NrdUFsQVCpGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙️
بانک صادرات ایران و جهاد اقتصادی در صنعت قطعه‌سازی؛ چشم‌انداز نوین تأمین مالی کسب ‌و کارها و زنجیره تولید/ تأکید قربان اسکندری بر توسعه کمی و کیفی خطوط تولید در چارچوب سازندگی نوین و جهاد اقتصادی
🔹
نشست مشترک بانک صادرات ایران و انجمن قطعه‌سازان کشور با هدف ترسیم چشم‌انداز بلندمدت و راهبردی همکاری‌های چندجانبه، در راستای تقویت نقش نظام بانکی در تثبیت اقتصاد پساجنگ و تأمین مالی تولید و صنایع پیشران، برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/439468" target="_blank">📅 19:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg73K_k9GVU9BUPr1b4cnNE2i9NaxBLDmbbXS5R2v6dVoYi1x4-1tPUgV288ZQ-StqrvNSJwijaPjqmjIsaFq2wk9UP6Kh7qfal7aXnTzeP6PfBfx3lCkR9kLRU0p8RROGJOKx_MH-kPdutKfNBX8yvZ5pSLCJI4KUs8P8eWK0z5qa7fSNENJDey2B6YAqQA2QqXU7Vz3WZqrewjtBM73LmAZduPZkuOdPlheXD6aDhIffaLdWj8Tw8xSpa4TdOlkYqv3d8pUVMBWHmCB2OhR6ebp2i-RNrzLpfC-kVFK5heBp-LYv5lV2dvJAlKleuh9ebpgvNjReoT57Sw3VAE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
آمادگی بانک رفاه کارگران برای حمایت از صنعت فولاد کشور
🔹️
مدیرعامل بانک رفاه کارگران از آمادگی این بانک برای حمایت از بازسازی، توسعه و تأمین مالی صنعت فولاد کشور خبر داد و بر تداوم پشتیبانی از تولید و اشتغال تأکید کرد.
🔹️
دکتر اسماعیل للـه‌گانی در نشست مشترک با مدیرعامل شرکت فولاد مبارکه اصفهان گفت: بانک رفاه با بهره‌گیری از ابزارهای نوین بانکی و مالی، زمینه تأمین مالی واحدهای تولیدی و صنایع فولادی را بیش از پیش فراهم کرده است.
🔹️
وی با اشاره به خسارت‌های واردشده به برخی صنایع در جریان جنگ ۱۲ روزه افزود: بانک رفاه آمادگی دارد از طریق ابزارهایی همچون اوراق گواهی سپرده خاص، اوراق گام، برات الکترونیک و فکتورینگ از برنامه‌های بازسازی و توسعه‌ای این صنایع حمایت کند.
🔹️
دکتر للـه‌گانی حفظ اشتغال و پشتیبانی از واحدهای تولیدی را از مهم‌ترین اولویت‌های اقتصادی کشور برشمرد و تصریح کرد: «بانک رفاه کارگران در مسیر حمایت از تولید ملی و رونق فعالیت بنگاه‌های اقتصادی حضوری فعال و اثربخش دارد.»
🔹️
وی همچنین فولاد مبارکه را یکی از مهم‌ترین شرکت‌های فولادی کشور دانست و بر حمایت بانک رفاه از بازگشت سریع این مجموعه به ظرفیت تولید پیش از جنگ تأکید کرد.
🔹️
در این نشست، مدیرعامل فولاد مبارکه نیز با قدردانی از همکاری‌های بانک رفاه، بر ضرورت توسعه این همکاری‌ها برای تسریع در روند بازسازی، حفظ اشتغال و تداوم تولید تأکید کرد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/439467" target="_blank">📅 19:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/439466" target="_blank">📅 19:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8f4d13c2.mp4?token=cXnzzy-M0Bjhr0in49qJ_gclxDrbTcsx-r8grgoJwHnvZ364GGhCMAnbd7eGNzxbcjeo9CTCyOS4KUwV1G9EyHc_E4nysGA5-VxabP67D1KeS_XyaRHZN9qKL2GuJuu4VC70s5CNqcpVq2IdN0sQ8OBKFiR7DRgiABaY8qm-7prOQ4pQ-XnEVQprDct7MqC4jrqr5LZucYvVuVWfTT2wkc8uv4Obu7aWcS2rXSVyZKekf5qoP-In4DcDw81AJXPK_j4avo_Lb0JSea6JvVrkwix1BVU3fkWFWGSYQ241Digb2nKX7WUhxCZiuhrhkeemx3GOimtd6tSBwMwuE3PqLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8f4d13c2.mp4?token=cXnzzy-M0Bjhr0in49qJ_gclxDrbTcsx-r8grgoJwHnvZ364GGhCMAnbd7eGNzxbcjeo9CTCyOS4KUwV1G9EyHc_E4nysGA5-VxabP67D1KeS_XyaRHZN9qKL2GuJuu4VC70s5CNqcpVq2IdN0sQ8OBKFiR7DRgiABaY8qm-7prOQ4pQ-XnEVQprDct7MqC4jrqr5LZucYvVuVWfTT2wkc8uv4Obu7aWcS2rXSVyZKekf5qoP-In4DcDw81AJXPK_j4avo_Lb0JSea6JvVrkwix1BVU3fkWFWGSYQ241Digb2nKX7WUhxCZiuhrhkeemx3GOimtd6tSBwMwuE3PqLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: در ازای بازگشایی تنگۀ هرمز، تحریم‌های ایران برداشته نخواهد شد
🔹
تحریم‌های ایران بنا به دلایلی مانند غنی‌سازی اورانیوم وضع شده‌اند و تا زمانی که در آن حوزه‌ها اتفاقاتی رخ ندهد تحریم‌ها برداشته نخواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/439465" target="_blank">📅 18:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
سجادی، روزنامه نگار و تحلیلگر مقیم آمریکا: آمریکا بعد از جنگ جهانی دوم، اولین شکست را از ایران خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/439464" target="_blank">📅 18:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e8fc214a.mp4?token=HuoZwGbU1WdfvYDpf36wVTowpMlaTTtHFhg42XrAr58f3g-Q60nMvneihk7RRLGFRLsc1TmBJWObFda1hf0bFN65iuqym97HVczsUbdnoRN4dPXU8vzi5BcCUKbZUdwawrmgaEkyMBtiZky63uNJcf0HKSfLHSjsYPDvGeImOAZvtNTujg_bOhL_WzCxYPeGvP0R5dqFxE2m8wrE1EK1aiJ_Mg_D7keciE2e0W-bTxUvKXJ8SChTQFKA13d4rIKCZSJ0zG1nx40Orj4DitynSI8EiXa7ZDAntRh5cJtrm_f7NE6S7dssdzufhU34klbRsrzUkiwZWSMxXFzM0HrFjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e8fc214a.mp4?token=HuoZwGbU1WdfvYDpf36wVTowpMlaTTtHFhg42XrAr58f3g-Q60nMvneihk7RRLGFRLsc1TmBJWObFda1hf0bFN65iuqym97HVczsUbdnoRN4dPXU8vzi5BcCUKbZUdwawrmgaEkyMBtiZky63uNJcf0HKSfLHSjsYPDvGeImOAZvtNTujg_bOhL_WzCxYPeGvP0R5dqFxE2m8wrE1EK1aiJ_Mg_D7keciE2e0W-bTxUvKXJ8SChTQFKA13d4rIKCZSJ0zG1nx40Orj4DitynSI8EiXa7ZDAntRh5cJtrm_f7NE6S7dssdzufhU34klbRsrzUkiwZWSMxXFzM0HrFjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: در ازای بازگشایی تنگۀ هرمز، تحریم‌های ایران برداشته نخواهد شد
🔹
تحریم‌های ایران بنا به دلایلی مانند غنی‌سازی اورانیوم وضع شده‌اند و تا زمانی که در آن حوزه‌ها اتفاقاتی رخ ندهد تحریم‌ها برداشته نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/439463" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1sZuoIO3HcAv9upAcMJv4Xwh5vTJ6JMnGO4wdeB69h6IgFtbUumVXFgYjAROLKfX9KgeD7V-nc_24ZTaVsyCJFdBb4mODt5NyiXE-noIkA_eaoEHCuiLXVE4ZLN-zBB2fHZC5f95bYvz5_PBE78k2sYqrucDHMJSOCXwaGeXYrkdWUW_jtMqNRD2ElGPZ_M5_Tk5DJqzUVEe29UKaxUY2a5Ya2DFTv45HcPocGwSwxLmjjs3OTOARiP9D5aMa3GIMFPOOpBkiL1S_gfqm0dBovwVca64GRsxa5tsBUvmn0KMFUvxA7i5BOUZ3dufhqALAr_H1svk0cJ7bp2B3AQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای شرکت‌های بزرگ به پروندۀ احتکار برنج باز شد
🔹
فیاضی، نماینده مازندران در مجلس از شناسایی چند شرکت شناخته‌شده در پرونده‌های احتکار چای و برنج خبر داد.
🔹
به‌گفتۀ او، کشاورزان به‌دلیل افزایش هزینه‌های تولید و کمبود نقدینگی، محصول خود را پیش از برداشت و با قیمت پایین پیش‌فروش می‌کنند؛ اما در زمان برداشت، بخش عمدۀ بازار در اختیار واسطه‌ها و خریداران عمده قرار می‌گیرد.
🔹
بررسی‌ها نشان می‌دهد قیمت برنج طارم هاشمی در سال‌های اخیر جهش قابل‌توجهی داشته و از حدود ۷۵ هزار تومان به بیش از ۵۰۰ هزار تومان رسیده است.
🔹
کارشناسان معتقدند تأخیر در پرداخت مطالبات کشاورزان و نقش پررنگ واسطه‌ها، زمینه را برای افزایش قیمت‌ها و احتمال احتکار فراهم کرده است.
🔹
از نگاه کارشناسان، راهکار کاهش واسطه‌گری و کنترل بازار، عرضه مستقیم برنج از کشاورز به مصرف‌کننده از طریق سامانه‌های شفاف و تحت نظارت دولت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/439462" target="_blank">📅 18:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c625b175f1.mp4?token=Dj3Tgffft7UU5Go8yZ_ncZduCsX0sxZA1EdZAMdM5uQlCeTIQU9CYMkbgiEt7IfyG8kG7lxQo8S-spAUNeGsyvcUEUGdjOPFb2y16FiECYcEIygsYgsdWrWJ5geQyuQH-Ec_PbidHNYGslIBN3kHw7F4nKi-m7yKRyVj0VE3z7EIJVsULtkzBMc9X_8GPI-Gig_ZIxGs3YherS8DBm0FvtasToz9p_yCY7HOUvnzewoO-Lk9FXxdaqjrnHNLonI08BC7tI_YxtkDhXU0BMmkjZ97FQGOjWuD7ZQpS3QFgOznoLlWqe8sXlO3Go4_O8yz20EW6Tqnkjota7hvO_8SDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c625b175f1.mp4?token=Dj3Tgffft7UU5Go8yZ_ncZduCsX0sxZA1EdZAMdM5uQlCeTIQU9CYMkbgiEt7IfyG8kG7lxQo8S-spAUNeGsyvcUEUGdjOPFb2y16FiECYcEIygsYgsdWrWJ5geQyuQH-Ec_PbidHNYGslIBN3kHw7F4nKi-m7yKRyVj0VE3z7EIJVsULtkzBMc9X_8GPI-Gig_ZIxGs3YherS8DBm0FvtasToz9p_yCY7HOUvnzewoO-Lk9FXxdaqjrnHNLonI08BC7tI_YxtkDhXU0BMmkjZ97FQGOjWuD7ZQpS3QFgOznoLlWqe8sXlO3Go4_O8yz20EW6Tqnkjota7hvO_8SDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان حمایت: مردم فعلا از مدیران‌خودرو خرید نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/439461" target="_blank">📅 18:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc0963023.mp4?token=lh3P9mNyIn0KHIOsC_937wylrTRBXTRB0_XH2IOYvR6nU6lHd0WEr6LqTpvtBzvaSEE_QbCbN_tMHLLxz6enAOz1rgR4kjUviuYsnmweGLZVObFzEAnMLSdxWhoMR-5kYsJFdKgWU_XPi3xDb2w-5GhWWxpEJQJNMdgYJkH6k0FQAuWQxUXcJQYjKGP9Y3pinne2n36mhG_P2SgXEE-vjJ4cAzjRNRriCG9V-lL-iSXehYHTq4tIhx-pSI0droBT-owG_GR3-MfOGRDWPqbCW8JgEj0EA1SyQUbPesCbztuhVqlJBveVxluOyyuiBoxeznaK5idhHrdYKiwKbMQkdBKO7UwREDuBSQUI1zEAR_5x3032h3CT06IBdZSdszENXbajWlinMX87cXVRcwYSEdqGCJKXeJ_7mXTgq_VEuMmn3jL1YaojKVHdnW97VyLcRP6cjSQIV_ot9gln_u78VjIrz3xt4VOHQ8jkT1OwPAyvX9wTeeT7eupdEMzittEs9dl8Uts4B4RHcGD1mBzzC8j76cj_URe7U_sOhtr6YfsRRj56dzYJwtVosp2pEYZk8yZqqrwaf4H1rwNDcPVeSOmWuTx8Ix4-t3aY3NXZv9UnbL7A5L42zOUAQMmQ0Ol35QgH2pzjUSXopAsBzzTg-ID_Wbkt5jhUdFxy2C7K59g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc0963023.mp4?token=lh3P9mNyIn0KHIOsC_937wylrTRBXTRB0_XH2IOYvR6nU6lHd0WEr6LqTpvtBzvaSEE_QbCbN_tMHLLxz6enAOz1rgR4kjUviuYsnmweGLZVObFzEAnMLSdxWhoMR-5kYsJFdKgWU_XPi3xDb2w-5GhWWxpEJQJNMdgYJkH6k0FQAuWQxUXcJQYjKGP9Y3pinne2n36mhG_P2SgXEE-vjJ4cAzjRNRriCG9V-lL-iSXehYHTq4tIhx-pSI0droBT-owG_GR3-MfOGRDWPqbCW8JgEj0EA1SyQUbPesCbztuhVqlJBveVxluOyyuiBoxeznaK5idhHrdYKiwKbMQkdBKO7UwREDuBSQUI1zEAR_5x3032h3CT06IBdZSdszENXbajWlinMX87cXVRcwYSEdqGCJKXeJ_7mXTgq_VEuMmn3jL1YaojKVHdnW97VyLcRP6cjSQIV_ot9gln_u78VjIrz3xt4VOHQ8jkT1OwPAyvX9wTeeT7eupdEMzittEs9dl8Uts4B4RHcGD1mBzzC8j76cj_URe7U_sOhtr6YfsRRj56dzYJwtVosp2pEYZk8yZqqrwaf4H1rwNDcPVeSOmWuTx8Ix4-t3aY3NXZv9UnbL7A5L42zOUAQMmQ0Ol35QgH2pzjUSXopAsBzzTg-ID_Wbkt5jhUdFxy2C7K59g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله ۲ تانک مرکاوا و ۳ خودروی زرهی اسرائیل را هدف قرار داد
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/439460" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-54.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/439459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-53.pdf</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/439459" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047e9c79f0.mp4?token=fTQr70kta7ZeIX1w7YCJZBscnnWmT_SMo1BMwYOiRcU6hHRBaRpnZKO-Mw_6scCi5pEYaPaoQJ5WmM7fWJo1dr6Ip66BK3LLy5N4WWkxkdVxkeavUV1j_O57_KWDTJgyV5WYjQRLCRWlH4WT8LzrZ32YISq9n9Ycq2LLs9LHxcEo_yFfr6NcW0ULylZdmhpCsjS5ACY3iS7kw2uK5eCMyYAji12o3P-78BFw1hXsfxdWPev9n2vX0fmcbHpjpWlk40n6HItHvMqm8Obk1w36B3tgfIenM6sg07ieLmO9QmPJ60Dg5AmjP3QUz5VbDwNwhwx92ymxu4CJZfL8PFAJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047e9c79f0.mp4?token=fTQr70kta7ZeIX1w7YCJZBscnnWmT_SMo1BMwYOiRcU6hHRBaRpnZKO-Mw_6scCi5pEYaPaoQJ5WmM7fWJo1dr6Ip66BK3LLy5N4WWkxkdVxkeavUV1j_O57_KWDTJgyV5WYjQRLCRWlH4WT8LzrZ32YISq9n9Ycq2LLs9LHxcEo_yFfr6NcW0ULylZdmhpCsjS5ACY3iS7kw2uK5eCMyYAji12o3P-78BFw1hXsfxdWPev9n2vX0fmcbHpjpWlk40n6HItHvMqm8Obk1w36B3tgfIenM6sg07ieLmO9QmPJ60Dg5AmjP3QUz5VbDwNwhwx92ymxu4CJZfL8PFAJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: با توجه به شرایط جنگی، به شورای‌عالی انقلاب فرهنگی پیشنهاد کردیم استثنائا امسال تاثیر معدل یازدهم در کنکور از قطعی به مثبت تبدیل شود.
🔹
این یک پیشنهاد است و شورا نظر نهایی را خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/439458" target="_blank">📅 18:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfHMWKsLpL6dHoA3IJthLB_cFKglDMMPFXG15keRPtzb-5CASKfNOp6GAR-UeobgI0MdbVkGINPlFg0CQ6TRhVKwaBzoQc0Dkd8_1CINcqeAqTP-i_UwCkDp5LGcoNmgoCSGnTa3TC4mQUVNfNSHX36j0PYDBRleOkxg6q-NlahSZcqRO_0L18KqWIju5zIgNUmjABIxWh9K0cjbE6TLCIXstognw8ktJsUe9BqOVJOroxqZjiQsS46l1EadzZ6fXEgmNwog7yAjIh4PaFmJGdDFKPB9Bse0eleZtCEE10X8CffTkpCUmxkgHSYge3zI15nhHYRueKsXvYTW-d2yBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غدیر را از قاب نگاه خود روایت کن
🔹
از شما دعوت می‌کنیم روایت خود از جشن‌های غدیر را ثبت کنید؛ از موکب‌ها و اطعام‌ها تا جشن‌های خیابانی، دیدارهای خانوادگی و هر جلوه‌ای از عشق به امیرالمؤمنین(ع).
🔹
عکس‌ها و فیلم‌های شما می‌تواند سندی برای آیندگان باشد؛ روایتی از مردمی که در روزگار آزمون‌ها، بر عهد خود ایستادند.
🔹
آثار خود را با هشتگ‌های
#غدیر
و
#بعثت_تا_غدیر
از طریق سامانه فارس تعاملی یا صفحات مجازی خبرگزاری فارس
(
@fars_ma
)
ارسال کنید.
🔹
به قید قرعه به ۱۴ نفر از برگزیدگان، هدایایی به رسم یادبود و تقدیر اهدا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/439457" target="_blank">📅 18:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHR9cE34rtzM1T8uT-DH9EKF8Qsw15W1FtoqDG6wfpJimn96vN-XxD_rlgjlQr16myWb9RBPRbaQADG3_P1sTWC1Mtm676170kJhUOlMn__bvlRCLc9ubWbBtqfLKw8M8209HunCoP0A0vUhINXZUQg-PvhZAlAGLUni7yYAikUrKkqIiGqWEkmbWuXKtzTQn8myyVHAh_x9sfljPSRzUZTTVrhqZXb3-W81Ih0Eo31j4LleQyYnerGwXaLz43aHaZQq6iZvE-jo9za0XFUARrRQ7cKBK19brvr3sOJmytokD0w5qCP7Cv0ADg6ch9Yn-KfbPWfCmrwjJ3mV8HrG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف جنجالی دیپلمات انگلیسی: اعراب نظم ایرانی را پذیرفته‌اند
🔹
آلیستر کروک، دیپلمات بازنشسته انگلیسی: کشورهای عربی حاشیه خلیج فارس به این یقین رسیده‌اند که باید تسلط ایران بر تنگه هرمز را بپذیرند و راهبردهای اقتصادی درازمدت خود را با در نظر گرفتن این واقعیت، تنظیم نمایند.
🔹
این تغییر توازن صرفاً یک مسئله نظامی نیست، بلکه نشانۀ فرسایش نظم منطقه‌ای‌ است که طی دهه‌های گذشته بر پایۀ برتری آمریکا و اسرائیل شکل گرفته بود؛ اسرائیل با این واقعیت روبه‌رو می‌شود که نه‌تنها نمی‌تواند ایران را شکست دهد، بلکه رویارویی دائمی نیز اسرائیل را در معرض یک بحران وجودی قرار می‌دهد.
🔸
کروک معتقد است که این تحولات در حالی رخ می‌دهد که اروپا در سردرگمی عمیق دست و پا می‌زند و این فرصتی مغتنم برای ایران، روسیه و چین است تا موازنه جدید قدرت را در جهان تثبیت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/439455" target="_blank">📅 17:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrS58FQVXjK5gf-041eIzW6SuRvA1fr1rHXHwqYuqEmvgFHuNgOH0KtL4hrN2MSQsKsIh3JgxDjLuWBzeT3gi7QtUrE_Z72nmgzSa-cCrTz0y4qOzuKm1bJEwa9csoyppIiq6VqE5ZZql1-L7B3AHeiPw18yVEoookP1F9d6pna6I2D_aMegcSqTctpAvkorOmdrwuwIDQ6l5REfGbVmup4YDOmwi1QTgC7YDJqbnLGWsSgJKo6U0qnElStCoe_SY1h7JuT7e5Umx-I3EullaIS8gdt9pSjqrM8cH6xGuWewyewd111fC59mhtsdjlfWKTJOXihqSnzmKoiPzCcnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس شورای‌شهر تهران: حمل‌و‌نقل عمومی رایگان نمی‌شود، تخفیف می‌خورد
🔹
درحال‌حاضر بحثی دربارهٔ رایگان‌شدن خدمات اتوبوس و مترو مطرح نیست؛ بلکه موضوع اصلی بررسی امکان گسترش میزان و دامنهٔ تخفیف‌ها در این بخش است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/439454" target="_blank">📅 17:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e7388266.mp4?token=g25ntEwJj5ii1-9eabQd_N_4MvR2fFuyYFnE9apdaKBcLRDjir-gBQZGyu19_ydbhDZjRpkOq5AaoS2qnRpXuWHutpSuPfZ9GIK4bWFJOhcFx6yrYeMGog-BJuiBBFSK9nFHKI3qE1bhKzkonEcJPJSMOnJQyVn6t9iISlHmxo57D3ht2EgaVxLBAjpF2LoreK2CdIVLQ6pX20wtyj_e_3LGyg-jDIxZWyJ1Hx0qpQcP78JOTlurc_VmF9eVESnBlLC6_u2CpU48ZWDIO5nbwJ7DnqLwScx-oUNJ_UU7pqnT00-N3MZVDHxrKUjooaYYf8xwkGtRoK5fU_GpKDnL7yDGEcL99dR__CVU7GccDkbtI7T4Vj_ntybB5suT9ePyCG0K9e0ltDvmeu_9Q9hMcGw6hPP8jhtZV2PyPMB4O0Z0mYEFWVHvP7mluAAsnpy-h1u0OP0aAzy44PrsVzod36RqATWNN_9-ULoToSgjdt8NRZSakJeFD5CoYKHzpSMVwGipkWvhRYm3OiAIt0n-6akmOc7-TC5pEE8h6Jqr_t3ta7_128_OxZo0PjKyfRc-09Uk2HM2qk3BuakfPExVrlTIeswLJ6ls__TNic1QzZNs_zyAsmd9xSYYaVUTIn0x7CcuSFgs0Vxw189059Y4gC34_IRFs3zhOcUn6bgaY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e7388266.mp4?token=g25ntEwJj5ii1-9eabQd_N_4MvR2fFuyYFnE9apdaKBcLRDjir-gBQZGyu19_ydbhDZjRpkOq5AaoS2qnRpXuWHutpSuPfZ9GIK4bWFJOhcFx6yrYeMGog-BJuiBBFSK9nFHKI3qE1bhKzkonEcJPJSMOnJQyVn6t9iISlHmxo57D3ht2EgaVxLBAjpF2LoreK2CdIVLQ6pX20wtyj_e_3LGyg-jDIxZWyJ1Hx0qpQcP78JOTlurc_VmF9eVESnBlLC6_u2CpU48ZWDIO5nbwJ7DnqLwScx-oUNJ_UU7pqnT00-N3MZVDHxrKUjooaYYf8xwkGtRoK5fU_GpKDnL7yDGEcL99dR__CVU7GccDkbtI7T4Vj_ntybB5suT9ePyCG0K9e0ltDvmeu_9Q9hMcGw6hPP8jhtZV2PyPMB4O0Z0mYEFWVHvP7mluAAsnpy-h1u0OP0aAzy44PrsVzod36RqATWNN_9-ULoToSgjdt8NRZSakJeFD5CoYKHzpSMVwGipkWvhRYm3OiAIt0n-6akmOc7-TC5pEE8h6Jqr_t3ta7_128_OxZo0PjKyfRc-09Uk2HM2qk3BuakfPExVrlTIeswLJ6ls__TNic1QzZNs_zyAsmd9xSYYaVUTIn0x7CcuSFgs0Vxw189059Y4gC34_IRFs3zhOcUn6bgaY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو مجلس خبرگان رهبری: اعضای خبرگان با غسل شهادت در جلسهٔ انتخاب رهبری حاضر شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/439453" target="_blank">📅 17:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjgLOclUaKKd-w0E6XNdkTG1cV0mhxyQGDQSrwK-VYvIgbIWriCPhxQrLUfAJLVOhcV-xr08ByeU4fPTEQ45C_Dk4paxBCSlw7Dhn3HFL-cgOolrb6DI1TYMxn-FdUWxOJdprB64mLBIqZlfJLejg5L_OB2Yt2hJUjYxMQMwj5ILZIQu6q3nxcqdVmaHgz_E3maDEzpXD7ia3btaYJ--oFqTsB3la1lRVSCjs-l83NlIAIWjcS3J4W0xG5cPRzSZGLpwzjgKqDZlJAg7boT62o_Aq6pgcnFOFLYhxDP1S0Ts1N6Py0qGD6CVfl59dHaafSHjb76EgfK_-9QTuHXfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار منطقه ۱۵ برای رسیدگی به پویش «فارس من» شخصاً دست به کار شد
🔹
پس از ثبت پویش «
تعیین تکلیف کسبه متخلف خیابان ۲۰ متری افسریه
» در سامانه فارس‌من، شهردار منطقه ۱۵ تهران شخصاً در فارس تعاملی اعلام آمادگی کرد تا موضوع را پیگیری کند.
🔸
خبرنگار فارس پس از اعلام آمادگی  شهردار منطقه ۱۵ سراغ وی رفت تا پاسخ مطالبه مردم افسریه را از وی جویا شود.
🔹
محمدعلی الفت‌پور ضمن دعوت از نمایندگان پویش و اهالی محله برای حضور در یک جلسه عمومی، اعلام کرده که ساماندهی دستفروشان و رفع سد معبر نیازمند همکاری چند دستگاه از جمله فراجا، پلیس راهور و دستگاه قضایی است و شهرداری به تنهایی امکان حل کامل این مسئله را ندارد.
🔹
جزئیات کامل پاسخ شهردار منطقه ۱۵ و آخرین وضعیت مطالبۀ مردم افسریه را
اینجا
بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/439452" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYvucUi44fRoh0R0Q4uMZrbdf34HSkwR_7jw_3YICJxuGCv0Ig86Pokz-MAHoM9XftyqDAzWvwoGaYC30WyBpyzg9XnqifCRzHLwhXWcWpl5jS_rPsFiHoVNnQte1Ci9hIH3Tiur2s46tXiybNouiD2SXKvAGJVt2rrNC8avDuj7kWvuc_6q6YEpwvYM533pxPi73pVhFYlmQ-s50S2wqNKFLoOV2v78Mor3YuNxWlYu-yclMRnU-HlobtpMT_lwaQFn0YTPwsPPVu3zhh8DRq1NjynuU_579_yzPX7KIGC52g3aznSxhRGrXhXpLXpLwsRlRm3ZfwGiF1437mylEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ بمباران جنوب لبنان، صدور هشدار تخلیه برای شهر النبطیه
🔹
ارتش اسرائیل با صدور هشدار جدید، از ساکنان شهر النبطیه در جنوب لبنان خواست این شهر را تخلیه کنند و به مناطق شمال رود الزهرانی در ۴۰ کیلومتری مرز فلسطین اشغالی بروند.
🔹
النبطیه که حدود ۱۵ هزار نفر جمعیت دارد، در ماه‌های اخیر چندین‌بار هدف هشدارهای تخلیه و حملات ارتش اسرائیل قرار گرفته و بخش زیادی از ساکنان آن پیش‌تر از منطقه خارج شده‌اند.
🔹
پس از صدور این هشدار، مناطق اطراف النبطیه از جمله کفرصیر، یحمر الشقیف، زوطر الشرقیه و همچنین بخش‌هایی از مرکز شهر هدف حملات هوایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/439451" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGGYukZ6Bik-3Dq1EgDbMWKtCu0ESjSF1aGzjPRg1z6IndL7oUOpA6_OzhpdoF1O1J6mW7KQQ24M9-4_EGDXHv8VgYNB3RDAirwaqXd4vSpVC0KgiyuJJRSqZBVHPjDZ2tGTBk4sKNt3W0083cR-0rqg-IJoQl8B9pNpqb6_Hao-hLOzjxDiUB3tiMpmFfQaD4IZoHSdk_fFdEw8FyCMOwS5Slp7ULT2vpWiyyrxm0kCii6jygknhsfYJ1agYmGb3ygYx7oqXTZrxTS-QZXcm_9OYzO6z8jP-TtIYWIblqF8l0zmKrH2rzcuDnzUhs6fq2urWhtKheKDwOk5VrRrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم اشغالگر: ما به لبنان حمله می‌کنیم ولی حزب‌الله نباید پاسخ بدهد
🔹
درحالی‌که صهیونیست‌ها درحال حمله به لبنان هستند، وزیر جنگ رژیم اشغالگر امروز گفته در ازای این حملات، حزب‌الله حق ندارد شهرک‌های شمال فلسطین اشغالی را موشک‌باران کند.
🔹
او همچنین تهدید کرد که در صورت ادامه حملات موشکی و پهپادی حزب‌الله ضاحیۀ جنوبی بیروت هدف قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/439450" target="_blank">📅 16:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a261d285.mp4?token=b74NvDJgLA-_dII8xvzUiIOeo_YZ6qtdFZ2OCKf50DInTEWSvFc3ORmIzRcc264iRAfnba4CPry0oDydwi1ltlktRmidu3PcCUE1hMsTpi8qQXjEllDjcbGusaBwmuBOp2Mbt1XLkLw83OU6unhQ4rpVeLEOpHyA4y69_4HtQWY88kppGOC38tEoR5nMexeLG0G1IdvpaNITUYEF80ChjqNYwSeaLICuTOhRqPT0P7R866678nlAuZ3vuWwd_mc9nDASRyZGWd7_TKQFXIWntnBGewMbYTUQqa1oebYNFS_HItb9-oGboIiGUyfupPmKcf-rP7BjFADrjXhYEe1YZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a261d285.mp4?token=b74NvDJgLA-_dII8xvzUiIOeo_YZ6qtdFZ2OCKf50DInTEWSvFc3ORmIzRcc264iRAfnba4CPry0oDydwi1ltlktRmidu3PcCUE1hMsTpi8qQXjEllDjcbGusaBwmuBOp2Mbt1XLkLw83OU6unhQ4rpVeLEOpHyA4y69_4HtQWY88kppGOC38tEoR5nMexeLG0G1IdvpaNITUYEF80ChjqNYwSeaLICuTOhRqPT0P7R866678nlAuZ3vuWwd_mc9nDASRyZGWd7_TKQFXIWntnBGewMbYTUQqa1oebYNFS_HItb9-oGboIiGUyfupPmKcf-rP7BjFADrjXhYEe1YZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس شبکه افق: حزب‌الله سایه‌ای از ایران است
🔹
اگر کارشان با حزب‌الله تمام شود دوباره سراغ ایران می‌آیند.
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/439449" target="_blank">📅 16:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جزئیات جدید از مراسم تشییع رهبر شهید انقلاب
🔹
معاون فرهنگی شهردار تهران اعلام کرد برای بدرقۀ پیکر «امام شهید» ۳ روز برنامه‌ریزی شده تا مردم بتوانند در مراسم حضور پیدا کنند و پیش‌بینی شده مراسم تشییع در تهران دست‌کم ۲۴ ساعت به طول بینجامد.
🔹
به‌گفتۀ او تهران، قم و مشهد میزبانان قطعی مراسم تشییع خواهند بود و محل برگزاری مراسم تهران به‌زودی نهایی و اعلام می‌شود؛ مصلی تهران و حرم امام خمینی(ره) از گزینه‌های مطرح هستند.
🔹
به‎‌گفتۀ معاون شهردار تهران، احتمال برگزاری مراسم در روزهای پایانی ذی‌الحجه و آغاز ماه محرم وجود دارد.
🔹
همچنین برای میزبانی جمعیت گسترده، هماهنگی‌هایی میان کلان‌شهرها و شهرهای اطراف تهران انجام شده و برنامه‌ریزی‌ها برای حضور بیش از ۱۵ تا ۲۰ میلیون نفر در پایتخت درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439448" target="_blank">📅 16:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaGMK5GHv8XwsKrwV_6xp0OKQKrsx7YmZGvTW3XOEvU_zaJJwmD_GWyFA465uTO6UUZsK4v8fSfenSjFm7LucJjb7eSdiYSuO-X4k9PycMDk6WHfoUmBXWJsIbjKYycHgUCQ05SQiwWLiw36VzCztSk_mujsj8ViQTorApPUQysjRv9gSFG4YJOJqxfLTeWJ5o_I5raAt3TSlwYYnIidaIBLV93ZIZkXjkMrgE3Fvqxx9BdYKGZJ1eBvQU2AAXn5TfFqz1l1YLFwgjhINUzsfPyDP8eutkH9IorbsKkvxXWKnuSX8yIpg0ERUADIa-aF5B07Ewd392MX90veHGuOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: حداقل ۱۰ دانشمند آمریکایی کشته یا ناپدید شده‌اند  سلسله این حوادث از سال ۲۰۲۳ آغاز شد:
🔸
مایکل دیوید هیکس: دانشمند ۵۹ ساله آزمایشگاه پیش‌رانش جت ناسا (JPL) که در جولای ۲۰۲۳ درگذشت.
🔸
رانک مایوالد و مونیکا رضا: دو متخصص دیگر از JPL؛ مایوالد در سال…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/439447" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ بعد از عقب‌نشینی از حمایتش از حملات اسرائیل به لبنان مدعی شد که مذاکرات با ایران با سرعت بالایی ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/439444" target="_blank">📅 16:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
حزب‌الله: شهرک‌های نهاریا، کرمئیل، صفد و کریات شمونه در شمال فلسطین را هدف قرار دادیم  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/439443" target="_blank">📅 16:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffifl3m-hiAQMxePwErVTSpRaok6TKcGNOPHlQUfnbjgxVIDtphhlgri_Je4Sj281YP9DsbPo1eAKDo94SIAb66WLuJ0EyUUnyNuVQWoQDMHjkVWQy8ssHegRj312Br7TKHs_RAkL5nkmZFwBlg8vpP02EW-G0baJpyHmAt5w4YDg0OIUmvxf6Uws1Bx-jtuuchSPu05xxpGg4yodDSZp0VGYqArIrLCc0utIpDplFVP0sQFsOQe39_zICj2t0REMoi_Ku0fZbrLnHjFjBfqMOTFLiDXvpMELsDUtq6kc_n2Mk8RanqunxuSE-IVdVpyE2a7RkMqNvy5pFlU38TLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی ۲۰۲۶ با قوانین تازه از راه می‌رسد
فیفا چند تغییر مهم را برای مسابقات جام جهانی ۲۰۲۶ در نظر گرفته است:
🔸
پوشاندن دهان با دست، بازو یا پیراهن هنگام بحث و درگیری با سایر بازیکنان یا داور، می‌تواند با کارت قرمز همراه شود.
🔸
اوت باید ظرف ۵ ثانیه پرتاب شود؛ درغیراین‌صورت توپ به تیم حریف واگذار خواهد شد.
🔸
بازیکن تعویض‌شده فقط ۱۰ ثانیه فرصت دارد زمین را ترک کند؛ در صورت تأخیر، بازیکن جانشین با یک دقیقه تأخیر اجازۀ ورود پیدا می‌کند.
🔸
در هر نیمه یک وقفه ۳ دقیقه‌ای برای نوشیدن آب (حدود دقیقه ۲۲) در نظر گرفته شده است.
🔸
هنگام مداوای دروازه‌بان در زمین، بازیکنان اجازه ندارند کنار زمین بروند و از مربیان دستور تاکتیکی دریافت کنند.
🔸
سرمربیان می‌توانند در زمان توقف بازی از لپ‌تاپ و تجهیزات الکترونیکی برای انتقال نکات تاکتیکی استفاده کنند، اما بازیکنان باید داخل زمین بمانند.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/439441" target="_blank">📅 16:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed35b17646.mp4?token=WhHgRgS2nMqBZa57O2yUUaFIt9Qj--KHXXRwAUqvWF49rnWh7ZY8Raz-LJ15BPIwAgmHBF-ta35nQVMZ6mSwWdJDm6je3mn2rXuXC2HcBPFfC6t-ozvlx1nGiSFWvJJxiOWS3LmTgAW10-P8dAwZhaMBg19QvWta9IIFC3AEeESQ3hgKtQlJqkYPjPgdoEYmTwvbn8NrzTdUVpHaPdECxRiHB6woLKqtqHx5n-pn0KOe-fp_8dGjs0mR3BlSNLbOH34KfPfYpMRGZn-dxAkh_rYgHForI_vPTgSeE2K8GRu9xfvFi7m0UA7rGCnMMHOXHHVkM2LCfju3pgOjYdn8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed35b17646.mp4?token=WhHgRgS2nMqBZa57O2yUUaFIt9Qj--KHXXRwAUqvWF49rnWh7ZY8Raz-LJ15BPIwAgmHBF-ta35nQVMZ6mSwWdJDm6je3mn2rXuXC2HcBPFfC6t-ozvlx1nGiSFWvJJxiOWS3LmTgAW10-P8dAwZhaMBg19QvWta9IIFC3AEeESQ3hgKtQlJqkYPjPgdoEYmTwvbn8NrzTdUVpHaPdECxRiHB6woLKqtqHx5n-pn0KOe-fp_8dGjs0mR3BlSNLbOH34KfPfYpMRGZn-dxAkh_rYgHForI_vPTgSeE2K8GRu9xfvFi7m0UA7rGCnMMHOXHHVkM2LCfju3pgOjYdn8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: اسرائیل در لبنان حزب‌الله را تک گیر آورده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/439440" target="_blank">📅 16:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3bbfbd0de.mp4?token=VDUylnWocudR4oOYjSVXeGhvsohZ4FSO6G7tgLHhhVmF7jY3C-qvy8n0s57Um1jdu9Dn3bs60mRFYTJ_JdF-6VOQEpvZVDMS1VryDw5fNU_iDDGQI9ds89mJ3K-t6POzHzlPQh1WqCIUkeAnnp2jFdLlioATE50gjcxEhqTXfOLCa6amTjscE4LNsrB6aaZpkfS6H3QNGDx7h6Mm3lPQsuPGxn5H2zy4FXnibnpJdTCEakfavQb8Y8JdqPots-Lj7QpfapAWzBJa-r-EbRbelQ4Xjoudoo6eIfKNqwZ566nHX5gPykhZMVBK81ZdlsZO3bp50A-T10vL--_yYbgoQq9dgDKom5bb39cXp8OAHH8-PfMM0y2OA5GHJ0z2Jg41cAbgO2B4dTQjL1ye4ZKKaUmrh9t5DT2i4iOOlwSaDfCKAXX-hgIHjm6Pf3aOoDfa4ulFDOj3zuklAq6un2B2XP7826KuHKf8j7h8iUM7eLJvTbf87hBnYr5Or6iJl6bMHuCSdEuaBkKuNeTdgtguwK1_vhDHyIGI9zx4UoqBnOn5yjIyMVA85E_YbAwqxjAdQtRT0YsnpX6T7AFCTl0GJcB8fK10scleKPO4hSWYIRFDddByijzUv7TTkg-4Zt78Fk-gpJ3in_qsySfDfQhRiTCtly6JRav-tbtj1VYsy2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3bbfbd0de.mp4?token=VDUylnWocudR4oOYjSVXeGhvsohZ4FSO6G7tgLHhhVmF7jY3C-qvy8n0s57Um1jdu9Dn3bs60mRFYTJ_JdF-6VOQEpvZVDMS1VryDw5fNU_iDDGQI9ds89mJ3K-t6POzHzlPQh1WqCIUkeAnnp2jFdLlioATE50gjcxEhqTXfOLCa6amTjscE4LNsrB6aaZpkfS6H3QNGDx7h6Mm3lPQsuPGxn5H2zy4FXnibnpJdTCEakfavQb8Y8JdqPots-Lj7QpfapAWzBJa-r-EbRbelQ4Xjoudoo6eIfKNqwZ566nHX5gPykhZMVBK81ZdlsZO3bp50A-T10vL--_yYbgoQq9dgDKom5bb39cXp8OAHH8-PfMM0y2OA5GHJ0z2Jg41cAbgO2B4dTQjL1ye4ZKKaUmrh9t5DT2i4iOOlwSaDfCKAXX-hgIHjm6Pf3aOoDfa4ulFDOj3zuklAq6un2B2XP7826KuHKf8j7h8iUM7eLJvTbf87hBnYr5Or6iJl6bMHuCSdEuaBkKuNeTdgtguwK1_vhDHyIGI9zx4UoqBnOn5yjIyMVA85E_YbAwqxjAdQtRT0YsnpX6T7AFCTl0GJcB8fK10scleKPO4hSWYIRFDddByijzUv7TTkg-4Zt78Fk-gpJ3in_qsySfDfQhRiTCtly6JRav-tbtj1VYsy2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله: شهرک‌های نهاریا، کرمئیل، صفد و کریات شمونه در شمال فلسطین را هدف قرار دادیم
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/439439" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439438">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b21e6e7cf.mp4?token=W5YFPaTyOeCog3LMcrempoBqN4jw5LX6RQKxzUM3B25Kc_E1iQCx-Iy3VFGPOG36JXcd03t3x4mdSJ7lXYIPv8ImzZFFpXT8mMYD8cAYkGRDxdu1srunzt03YpzKZEwW-nG-_1-_-DVaqV8X7drtDlp3_YDPUUmw5_IOGOScJ7ohT4lx_wRb2LD5DaUS9Syf6svjWosBBlvdxerlMlep8MybjhByfv2PzdjVEDh0czXfF-d3eqNoDAIZiIrMJTW08t2XZi-XK5pTXydzxq673dFQIeAKG1WL27-97KvbJlDumYfN8w0iTRLIxiIG-yKAwD5mpXzXGomm42HX5OYcV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b21e6e7cf.mp4?token=W5YFPaTyOeCog3LMcrempoBqN4jw5LX6RQKxzUM3B25Kc_E1iQCx-Iy3VFGPOG36JXcd03t3x4mdSJ7lXYIPv8ImzZFFpXT8mMYD8cAYkGRDxdu1srunzt03YpzKZEwW-nG-_1-_-DVaqV8X7drtDlp3_YDPUUmw5_IOGOScJ7ohT4lx_wRb2LD5DaUS9Syf6svjWosBBlvdxerlMlep8MybjhByfv2PzdjVEDh0czXfF-d3eqNoDAIZiIrMJTW08t2XZi-XK5pTXydzxq673dFQIeAKG1WL27-97KvbJlDumYfN8w0iTRLIxiIG-yKAwD5mpXzXGomm42HX5OYcV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شست‌وشوی ضریح علوی در آستانۀ عید غدیر
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/439438" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439437">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=uQ7xBCuIiTE2rFwZtVu76U27pmQIHIplDj9GB1DYwPxBCbRRLzLpo2QL_UOArN1XKXi4c9pLIWSLAWbRCt9QADIe3wR5vqKd_XpTf72Q1TVF_ytmhQ0CxofhR-cyQ9RFQL1CVhtlaspzEZeYshqe1rTXAJCYjruqDGA3VKexB04OVFnnNjdsUJdfMgwB_wRnXdnb10JFlAm5_7FnNPX0JMkck5to9zI-pCN4XObDOYwtxwkiSw40O5eIQs7EIlRxJnqJnLnCXhLSUamVy4_j3owv7pqhwP9pzQmocVx9TMb-7YoANwF2YhpfPbhXA_c9gaNM7Z2gz87HsHPBldAQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=uQ7xBCuIiTE2rFwZtVu76U27pmQIHIplDj9GB1DYwPxBCbRRLzLpo2QL_UOArN1XKXi4c9pLIWSLAWbRCt9QADIe3wR5vqKd_XpTf72Q1TVF_ytmhQ0CxofhR-cyQ9RFQL1CVhtlaspzEZeYshqe1rTXAJCYjruqDGA3VKexB04OVFnnNjdsUJdfMgwB_wRnXdnb10JFlAm5_7FnNPX0JMkck5to9zI-pCN4XObDOYwtxwkiSw40O5eIQs7EIlRxJnqJnLnCXhLSUamVy4_j3owv7pqhwP9pzQmocVx9TMb-7YoANwF2YhpfPbhXA_c9gaNM7Z2gz87HsHPBldAQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور مجوز عبور از تنگۀ هرمز در هر ساعت از شبانه‌روز
🔹
مالکان و ناخدایان کشتی‌ها از سراسر جهان می‌توانند در هر زمان شبانه‌روز با مراجعه به سامانۀ نهاد مدیریت آبراهۀ خلیج فارس، درخواست عبور از تنگۀ هرمز دهند.
🔹
سامانه درخواست‌ها را بررسی کرده و در صورت تأیید،…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/439437" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439436">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656021c50d.mp4?token=lotbBDr1OyR0PjVp9GUAOYxxV-kTY_JhEawe_blTNCdanXi_bLkjxWgxyYdtx5qXL4AOavvJxqE_tCkI5jgE5dG46d5FwZApgOL2GbiUmU637s0o8-EOlKZlf3-hIdkJwxYUlsaQbuyLUUKbByTH_ZZ9-FjqPO7tKRTg1An-3-QORh2ubMC_szoSfmxG_N2vxOV4RKqqEAV9C_wo5oR3NBiUNFYLkH6Hgq283EYAjeu1VVN64o0CJ3F3XzcWuZ5g0IvK1vnzIxVGwfp1FqHr0rhjHCLJcv_2VAqVDmr1LEYCD3Y4NwqCqGPVVUbhztY29iJnBc-RaV-lhPNF6UQRSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656021c50d.mp4?token=lotbBDr1OyR0PjVp9GUAOYxxV-kTY_JhEawe_blTNCdanXi_bLkjxWgxyYdtx5qXL4AOavvJxqE_tCkI5jgE5dG46d5FwZApgOL2GbiUmU637s0o8-EOlKZlf3-hIdkJwxYUlsaQbuyLUUKbByTH_ZZ9-FjqPO7tKRTg1An-3-QORh2ubMC_szoSfmxG_N2vxOV4RKqqEAV9C_wo5oR3NBiUNFYLkH6Hgq283EYAjeu1VVN64o0CJ3F3XzcWuZ5g0IvK1vnzIxVGwfp1FqHr0rhjHCLJcv_2VAqVDmr1LEYCD3Y4NwqCqGPVVUbhztY29iJnBc-RaV-lhPNF6UQRSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو شورای‌عالی انقلاب‌ فرهنگی: امسال تغییری در تأثیر معدل بر کنکور ایجاد نمی‌شود
🔹
سعیدرضا عاملی: طبق ضوابطی که از قبل اعلام کردیم، هر تغییری در قاعده سازمان سنجش باید از یک‌سال قبل اعلام شود، بنابراین امسال تغییری در مصوبه نداریم و همان اثر قطعی معدل یازدهم…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/439436" target="_blank">📅 15:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313373d690.mp4?token=iCxqHSVvyvMT4FVXUTRsERHaTUqX5GDXwm-JJvKeBVl_eWfPcee3Gt0N5WR_vcduauyCt_JSu9EmKiomzLuO6XPaUgrfrooiOQ_NAz3iSvBZ6b8Hnr3340CD8Bjhk38N5plqfA7MzV-FhV_Cr3bGfFcBIsyJKt59589T8OP5LnHe9hSI8fGG6mn0HdYsjkzOsdERusxUyOINyWkXm-11cU3u5BKHLxhWazHYsalWeZCnlQFCSjJjGisF7vfWYRBMgeCZohrhUSTdniRttP9OKHbtVkgdvxxhDgwWlX7C9ecZWAl3u9WTNSinne-szJrnLTzXPaY7NedIoLiuP1vSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313373d690.mp4?token=iCxqHSVvyvMT4FVXUTRsERHaTUqX5GDXwm-JJvKeBVl_eWfPcee3Gt0N5WR_vcduauyCt_JSu9EmKiomzLuO6XPaUgrfrooiOQ_NAz3iSvBZ6b8Hnr3340CD8Bjhk38N5plqfA7MzV-FhV_Cr3bGfFcBIsyJKt59589T8OP5LnHe9hSI8fGG6mn0HdYsjkzOsdERusxUyOINyWkXm-11cU3u5BKHLxhWazHYsalWeZCnlQFCSjJjGisF7vfWYRBMgeCZohrhUSTdniRttP9OKHbtVkgdvxxhDgwWlX7C9ecZWAl3u9WTNSinne-szJrnLTzXPaY7NedIoLiuP1vSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی شهرداری تهران: مترو و بی‌آرتی تا زمان تعیین‌تکلیف توسط شورای شهر، رایگان می‌ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/439435" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f707799294.mp4?token=o3bme2jBzDjZeA7BY0E6JCjTvh1kVXoySXJ4woXTTWuUseYSMSz7C4vY-zkdPVOeYuGEEMPN7rXDmKEVj1EqxaJd5zsc2hKxDgoxf_bgoNegE7XJ_TePO-jrO6N4-dUC_-w6HuQJ0KimgdY4fRoUbbwsfykRmJ7hGhbNqobax-TvJ2NefsutGGXg118Ea0qaWsJJOUBlU1iivDWSzC-xfbh0-4Ma2XabiKj2UB8a076iCbODi54lxzsp2InijaGKAknh8qrMTgWNyUs91aiPRyG2HTPVOfSlp2qhDO_ed8X9IEENvyM_binRI8j5Q6TvYqaDZ2cu407aisawAVSFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f707799294.mp4?token=o3bme2jBzDjZeA7BY0E6JCjTvh1kVXoySXJ4woXTTWuUseYSMSz7C4vY-zkdPVOeYuGEEMPN7rXDmKEVj1EqxaJd5zsc2hKxDgoxf_bgoNegE7XJ_TePO-jrO6N4-dUC_-w6HuQJ0KimgdY4fRoUbbwsfykRmJ7hGhbNqobax-TvJ2NefsutGGXg118Ea0qaWsJJOUBlU1iivDWSzC-xfbh0-4Ma2XabiKj2UB8a076iCbODi54lxzsp2InijaGKAknh8qrMTgWNyUs91aiPRyG2HTPVOfSlp2qhDO_ed8X9IEENvyM_binRI8j5Q6TvYqaDZ2cu407aisawAVSFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: باورش برایم سخت است که اسرائیل از مناطق اشغال‌شدۀ لبنان با تفاهم خارج شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439434" target="_blank">📅 15:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439433">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPHxhcZwPT1WnbNydwxNPzHY-2ou1MFBGoBpd9ZVcqKepjQpgmBDGEuzhhcEqAVeCA5RFdBiGTafGXlvSfGsx-dHpE6kpdYLQ2vq4eVlE9YkVfbU8Ly3-ECxvPw6C_9y7y0Yw_fAZL-Bw-KhoO8d-hjQ8nbxYOl2pU47iqzKsCO7NDF0iEGNTOlfbxKKsBRSr_6pkb5R7E8AGIzSZ-pMTJ3hLHTW4xkRhtJwl3IshhHLk74_it3F3TnaTwpkbVa5F6SfnFDbipq-hx9sNYRxSwlVDAs2WGeBx1U6rO9b-zF67vEbEYqBETg7d7mORupdu5jUjIka2KqyIjWBwtuPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۴۰۰ میلیون تومانی برای نصب نیروگاه خورشیدی خانگی
🔹
رئیس ساتبا از پرداخت ۴۰۰ میلیون تومان تسهیلات به شهروندان برای احداث نیروگاه‌های خورشیدی ۵ کیلوواتی در پشت‌بام منازل خبر داد.
🔹
این طرح با هدف توسعه انرژی‌های تجدیدپذیر و کاهش ناترازی برق اجرا می‌شود و منابع آن از محل صندوق توسعه ملی تأمین خواهد شد.
🔹
همچنین قرار است نیروگاه‌های خورشیدی ۵ کیلوواتی در ۱۲ هزار مدرسۀ کشور نصب شود تا علاوه بر تولید برق، منبع درآمدی پایدار برای مدارس ایجاد کند.
عکس: مهدی قربانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/439433" target="_blank">📅 15:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439432">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXI0jGOJd6VWH2yvAdWOsXrYTezdsDFFZTR6kx1UinD6zPuTUUldxP94CQxxzTJHZ_NP6DJn2DLcodu-Hsvvwujv_HKHIILIrH6PVIBW9TNC2c27cfbHhThe5oGsgFoybUx9Xkxr-iTF0pk87lRYuAU0p3UoGiZRUE2v_0GipnBjxdGhrcgGL7SgWj9DtHEv8ANCxQujGYKbnsuLaon4sNzyCRoPC1l9qZ8lfTcqoZSdFjgfNKpm4hk6v8deJCAYOO7OYR2OBv40ck24HgDm4IySeFXtviLzzh-yvO7-MwprT9-blvUL0472sfO1TIPxfBeEnVYiAFr527fzNGP3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس آمریکایی‌ها از شروع دوباره درگیری‌ها
🔹
روزنامه واشنگتن پست به نقل از منابع آگاه نوشته که مقامات نظامی آمریکا در چندین منطقه جهان، «سطح حفاظت» از نیروها را از بیم از سرگیری درگیری‌ها افزایش داده‌اند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/439432" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjfMVEJ7gO58QE69-FhNmrXz1XiYbbrPBm53THgkpQqLrEN346LohOt5A0qO_7IXUCiZOqs3LE5xBMgzqA3K5VAczsUp-o7qwdruQ_n8enACrLB66rG7ogdSHyxTGmweF9Oil_ACAo_jPNRYSDY9KZR-Za1AQYpZPqPEDOw0uxkr1khZWaYZaoB9NqQ-jvQ98PBxAFmEpV6q_EWSLtSIiYeNo-vaTrWBWGN3MOO5Hv-Keshxq_Xvx0vl8A-lQnwTUaalCKg85Q0AkR1itbJ9Sa-SsG5ji-xqB5wHNK4I6o7c2JD_95qzXRVtZfuhHgZVeSel7fl_eQChLORebGjLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود خودروهای آفرود به جنگل‌‌های هیرکانی آمل ممنوع شد
🔹
دادستان آمل: هرگونه تردد وسایل نقلیهٔ آفرود در جاده‌های خاکی، مسیر‌های فرعی و حریم رودخانه‌های منتهی به جنگل‌های هیرکانی مطلقاً ممنوع است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439431" target="_blank">📅 15:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46b032224.mp4?token=fwYcKgCPX3GfP23fJwLm2F4MeQ2p1ULn8AZDQBueKBw2NHAIAe7KUoSQFhlN2DKTzy6eSVJ_IWVLCgb0-fVf7NLVQy30QHHZgTFllw5KDeOyx8wq08NfsMNruTuVrThZ-R059N06t_3VXJeC7EFsWYC52tLphtJUTTj519G5iunV153pT6Yt5ed6UgY3ONw6JfDUQd3wIh442QPwie1PsuuBeRun7DXJmwlgCTHKXER4HYr2igl2KVJNZOrYZDb2l6zVXmRD74cDRQfrheUSPUepS-133DUAUsIpJr_OEBHezEwYd8_lchBe5q10l4wdfI2tAQbSx56w2MH7mdf0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46b032224.mp4?token=fwYcKgCPX3GfP23fJwLm2F4MeQ2p1ULn8AZDQBueKBw2NHAIAe7KUoSQFhlN2DKTzy6eSVJ_IWVLCgb0-fVf7NLVQy30QHHZgTFllw5KDeOyx8wq08NfsMNruTuVrThZ-R059N06t_3VXJeC7EFsWYC52tLphtJUTTj519G5iunV153pT6Yt5ed6UgY3ONw6JfDUQd3wIh442QPwie1PsuuBeRun7DXJmwlgCTHKXER4HYr2igl2KVJNZOrYZDb2l6zVXmRD74cDRQfrheUSPUepS-133DUAUsIpJr_OEBHezEwYd8_lchBe5q10l4wdfI2tAQbSx56w2MH7mdf0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: باورش برایم سخت است که اسرائیل از مناطق اشغال‌شدۀ لبنان با تفاهم خارج شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/439430" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5d386dc0.mp4?token=tMxFBD7A58KXFvYPxk8jyA-kBBpNcdzwbZRBzXchK2vSUESE3gXV_HONlDsWWBaeFqWOP6jdTXxRZUGIhH6ixnlLUr8oxfUWSBQsFnc8qb9s1-4CIYywieduxSI8pVCrCPsE5pLMWPHw66mFaqAdM1K63Jt6B4PbcLemRbf5gEPOXDt3D_PTdJPNrCSPgP5TiLwXTfy_UsJo6I7v5-TjBMR_hoMxCm2Q8LMIy569-g1YsaRy5_qbuD7tKMPEPAKeMkQ9iZWZ6k_tW4reTgwSb9-EpMuWZH7FdbsrGcVM0CD7uFRRMj2-A2aORgYt-R88XIlcpxv1lyXXJ26EVaWkJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5d386dc0.mp4?token=tMxFBD7A58KXFvYPxk8jyA-kBBpNcdzwbZRBzXchK2vSUESE3gXV_HONlDsWWBaeFqWOP6jdTXxRZUGIhH6ixnlLUr8oxfUWSBQsFnc8qb9s1-4CIYywieduxSI8pVCrCPsE5pLMWPHw66mFaqAdM1K63Jt6B4PbcLemRbf5gEPOXDt3D_PTdJPNrCSPgP5TiLwXTfy_UsJo6I7v5-TjBMR_hoMxCm2Q8LMIy569-g1YsaRy5_qbuD7tKMPEPAKeMkQ9iZWZ6k_tW4reTgwSb9-EpMuWZH7FdbsrGcVM0CD7uFRRMj2-A2aORgYt-R88XIlcpxv1lyXXJ26EVaWkJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب اقتدار دفاعی ایران در سرزمین وحی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/439429" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_IMump6K6363OYXoY3ZWB2SHkmx1fYcdh5OecKo_NNHIKg09GiC0KdLm3nvKz-tpqpCaLHYCer4irjuLDe0rE1W6mx9aRLJ6LZ5GUEon_OANVj0-JHGnGfjhSR97ATBAbVaFoO8noJbYXTHNF0cf14mHhIM5Sn1ttRgYaVhXlThT9QhTLjdl_XRwG4bkPHw3XODbsoCFuIFIUpNAT07g83iB93r3Xgs8l-DLVG04NwXBP-AbsxgfnPjII3wfUfSLcyMcqkfZBzyKCa5ZsEJmD1yENBNWODKg_nXpiPdm2r1PDaw753pvn89nedlyYcW7FEqst6MrqZdUus7Xc9DYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس بنیاد ملی گندم‌کاران: ۵۰ درصد پول گندم‌کاران این هفته پرداخت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/439427" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTDvYoBFIM0cZsOeQ4HkFVVldHwaH83mwxvJlkfkYFqkJoKmdCEYycU47gWxvFCu1Ej21dArIQE1DXq6Eur93kdxay_6WU9bMUT9VeZKBVEEha5qmm9EA_g3BC4EwhRi7sxLK_4cTDdJdNFP100AGsfPts1i0HMws3UXt6nt5hwEzV3qojOs-2IlbZUk1Tqa_TKLSx3Bqwpx6U0LfBqMCBCHCDOyt9C44JatMJZZ_3mD8N3FCJ0mHLGH8kxorXRdVEW8_WvySxN0bCtQGXClQcH2lWhvhWtVgDcZMgBJ6jGLopmx4oKSf8aquwHT46c3pD9zfFZrMQF_Q13rvkKWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارهٔ پیراهن بازیکنان ایران در جام جهانی
مشخص شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/439426" target="_blank">📅 15:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=TsCK5l1iKjLaptsO2Gmaandae9_K0KSpbxD9SgHN4yYCRxPTNK0WtJjWMd5eAJtdyXxcvUjKegD-P35N1ytE-mltF-evDrXCcEGs1lBIpkDyHM6pSybvIPm8ZqXB44GL8LY50SDPNIbYlgX7YQ8RAsIkS9wTcyqktrMPzTc50JXcuxXACrcm3yK9pnDWF9X-58BuJ9GMbbAPwaZLdJ310x61y3nb7CMVx42KGyeEuUDooLWLnKwUkWNRLtyzcxe-Pqn0trL53L14X0uIlYBL4PmhtprsE6PxaQqTliPedNEtF02kSlR7rkcQKfuIrUaLrz9rkp898a1vPP4754JyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=TsCK5l1iKjLaptsO2Gmaandae9_K0KSpbxD9SgHN4yYCRxPTNK0WtJjWMd5eAJtdyXxcvUjKegD-P35N1ytE-mltF-evDrXCcEGs1lBIpkDyHM6pSybvIPm8ZqXB44GL8LY50SDPNIbYlgX7YQ8RAsIkS9wTcyqktrMPzTc50JXcuxXACrcm3yK9pnDWF9X-58BuJ9GMbbAPwaZLdJ310x61y3nb7CMVx42KGyeEuUDooLWLnKwUkWNRLtyzcxe-Pqn0trL53L14X0uIlYBL4PmhtprsE6PxaQqTliPedNEtF02kSlR7rkcQKfuIrUaLrz9rkp898a1vPP4754JyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در حین پخش برنامه آشپزی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/439425" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaehc8cm20RZa5i7jU9n0pCrlwEaGppOdFmtugZXJzN0NwqR6YOz-M-PBXP6Fy_J2OuFKytyfJp5bgoM6CS02dgbrsQRi0rgvLFPS2XP38Fe4q6D3P_QdjKOwFv1QRvnJUcD8Gwdk04uV1QdD27HxHBWV2V12uIk935IzMh3lpX5XAWzL2ME0Y6Cj7NwxNey8QA8frxR3o7lPgeUQaLwUg3Y-LnNwsaqv3viqGk9SMMcvrEoUWLcSIWOm00Zd2yRJxj1D4D2_uTwsGiSkxQgD7nBKOHouxGP0-kKbBG4OzuDcvVPe4LZ8YIqIXXaVZYx0LTtPbuxil4lBwrqaC79LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس آمریکایی‌ها از شروع دوباره درگیری‌ها
🔹
روزنامه واشنگتن پست به نقل از منابع آگاه نوشته که مقامات نظامی آمریکا در چندین منطقه جهان، «سطح حفاظت» از نیروها را از بیم از سرگیری درگیری‌ها افزایش داده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/439424" target="_blank">📅 15:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef0Dz2hM5iiPbEQWWc8uYqSdxXGn74m18ADM1qKP32ju3srw7pJghwTdVC0i3VIri3hIbr9FQVCLyiX2HTkk7Rks1F8ZY-wPzJoEHZpZ81-ald7i0w1MN4FpPQXapYV1gp5-o3q9vme1wLigfBs-FmKW8g9y9HFW1Ri2nuYkEbfYitpi4PAweYCoLDrwLil9EIDQHvX9AUKjX6Iu54GxY9d0oyoc_YwJFW4FluHZ3o9XOAfPA0q6gDtPr2nlTML_5TbDYBi-Ie8LkxZylor6ON1rIdG13WEwAzfEJzRIOJFNWrQAJiIpTzOGfc6MQsSdQW4ehkCTg9Hhw8Xuv_KeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر المپیکی تکواندو زیر تیغ جراحی
رفت
🔹
مبینا نعمت‌زاده، عضو تیم ملی تکواندوی بانوان کشورمان و دارندهٔ مدال برنز المپیک و طلای امیدهای جهان، به‌دلیل آسیب‌دیدگی از ناحیهٔ رباط صلیبی زانو، امروز تحت عمل جراحی قرار گرفت.
🔹
نعمت‌زاده پس از طی مراحل اولیهٔ درمان و دوران نقاهت، برنامه‌های توانبخشی و بازگشت به میادین را زیر نظر کادر پزشکی و فنی تیم ملی آغاز خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/439423" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67532ff2c.mp4?token=raqQRNLT3oiAL6TN4kFGM8FCHrhytKx3NCSyTkbik1oaide_m-Vjx5Kh5v4r1qQJ488BKENZVsbWlB5TYZlkTrNhylXs25lwCEvDUfb2-HIHz0m5D5JZRh88tkeb-lC-ofX50hKTN37ITRo6HgRvpYykCFuS71zQfBWcA9iZN4L-DR6St7IjyOSP9fAed0SH9LtV6sa-HOfFHr2vwPDo7eGWID5hvvRj7dvDsBbSUtZQsYYh-7EXYE4pEtZNJp7eFDrFVv88HS7F70iIH8m2X1A3JWCzeDzp8glwMreoYPQQRmlOCLvucrU5-xEsHotCvFJ-BRVx91MU9RFZjPecJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67532ff2c.mp4?token=raqQRNLT3oiAL6TN4kFGM8FCHrhytKx3NCSyTkbik1oaide_m-Vjx5Kh5v4r1qQJ488BKENZVsbWlB5TYZlkTrNhylXs25lwCEvDUfb2-HIHz0m5D5JZRh88tkeb-lC-ofX50hKTN37ITRo6HgRvpYykCFuS71zQfBWcA9iZN4L-DR6St7IjyOSP9fAed0SH9LtV6sa-HOfFHr2vwPDo7eGWID5hvvRj7dvDsBbSUtZQsYYh-7EXYE4pEtZNJp7eFDrFVv88HS7F70iIH8m2X1A3JWCzeDzp8glwMreoYPQQRmlOCLvucrU5-xEsHotCvFJ-BRVx91MU9RFZjPecJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاینده‌رود به اصفهان نزدیک شد
🔹
مدیریت بحران استانداری اصفهان: با افزایش خروجی سد زاینده‌رود در روز گذشته آب در مسیر رودخانه جریان یافته است.
🔹
باتوجه‌به خشکی بستر رودخانه در ۱۱ ماه گذشته انتظار می‌رود در ۲۴ ساعت آینده آب به اصفهان برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/439422" target="_blank">📅 14:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlVvBtTqsEdKYChDOLuc20LR_ByxHajiS1yjhThrTtMBPQodrYAh-VFyTLQTAk2RMrfP0WXgBdbOtoNhKqUMWjbMP0XafsXCe3fsg5Q7BhXDCdvjHmfJc_HyMXI0ZfuZlYDQWtkYBhDBG-XbuZQ2B2iPo2hBcUnS-FjGTThQpBT4W--x5cJAb5LvVpmCGh_Td6o-xisyy130nH1r1RM5j-KPZD83SqGHVWDNoyHwpTexSLhmu5eiE7T7xXIzg3QT_uPIUEgP6v1BUok80J-CaNaDXX12B5TkcD4wxYeYlp2xrX6HvpJ1mXnJd3ve2ltTk07YHC0bAX7sy5bXZIGpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نبض زندگی در دریاچهٔ ارومیه به قبادلو رسید
🔸
بندر قبادلو در شهرستان عجب‌شیر، یکی از جنوبی‌ترین نقاط دریاچهٔ ارومیه در استان آذربایجان‌شرقی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/439421" target="_blank">📅 14:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3644805d8e.mp4?token=F3DJM1pgz0vysu0LdtttGN3M-mZRJR0VSUiJFJIROTTLTcTVON6ErqwOiHXTEIZiAi2n4ZOQOn95HQwNRFsy5LWDyk15DrimgItMoKJRR2mGVlnN5MbrCdvOjs_XDE5oV_94VuHWjX3NabIdhv8jdgB8iP9hQIw5IaNCkR5L8mXmrumbnJmmMtdhKYsvoc0itgTBiQ7ELBnEhMdXbOpxiE-40UfWN7m0L-nadh3NqaKqEZMwo0h1PfeSiOVPn2EyphvXyoDmwfEcb9zCFrOMkFUcFK7MbpQCMmc6JeZndslssjhYLSfu_SlnUcoDPXg186MDKqnVb0Z6lsrIR3l6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3644805d8e.mp4?token=F3DJM1pgz0vysu0LdtttGN3M-mZRJR0VSUiJFJIROTTLTcTVON6ErqwOiHXTEIZiAi2n4ZOQOn95HQwNRFsy5LWDyk15DrimgItMoKJRR2mGVlnN5MbrCdvOjs_XDE5oV_94VuHWjX3NabIdhv8jdgB8iP9hQIw5IaNCkR5L8mXmrumbnJmmMtdhKYsvoc0itgTBiQ7ELBnEhMdXbOpxiE-40UfWN7m0L-nadh3NqaKqEZMwo0h1PfeSiOVPn2EyphvXyoDmwfEcb9zCFrOMkFUcFK7MbpQCMmc6JeZndslssjhYLSfu_SlnUcoDPXg186MDKqnVb0Z6lsrIR3l6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: از دولت درخواست کرده‌ایم کارکنان آموزش‌وپرورش شرکتی شوند و حقوق خود را مستقیم دریافت کنند
.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/439420" target="_blank">📅 14:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e6e55bfc.mp4?token=T9CzvJNf1HKTQCG7M_sVeh0JPre605gt-RlHeYArxgKEQuA-csNIpjzqQFy0Kg4MZSeHi1DhjJA5RWDHBvT_iTNRXnMnDutDrhQcCY9Uh5pAK7SUqqeVsxBuXZdFW6WLMLFBvgsrBZutCQSAPa_DKqVfzBc0YOpQGFVrmBS6OrZwJUBaxC4qCTgqyW2JfQx-MZH9sZ-G1KjTvCFh4n9X5qHXeFzCW1p6IqLzYC10kx2Y-Hl_qFUeOnoUEoVgQ3BLDN-XYobzrVmzizxiulihgGzmLi3r9SQLxWapqM7nkkGsCtbxmgciRxN1_7Ase9IY5iBQGwCgsAEmvcF3pWI6eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e6e55bfc.mp4?token=T9CzvJNf1HKTQCG7M_sVeh0JPre605gt-RlHeYArxgKEQuA-csNIpjzqQFy0Kg4MZSeHi1DhjJA5RWDHBvT_iTNRXnMnDutDrhQcCY9Uh5pAK7SUqqeVsxBuXZdFW6WLMLFBvgsrBZutCQSAPa_DKqVfzBc0YOpQGFVrmBS6OrZwJUBaxC4qCTgqyW2JfQx-MZH9sZ-G1KjTvCFh4n9X5qHXeFzCW1p6IqLzYC10kx2Y-Hl_qFUeOnoUEoVgQ3BLDN-XYobzrVmzizxiulihgGzmLi3r9SQLxWapqM7nkkGsCtbxmgciRxN1_7Ase9IY5iBQGwCgsAEmvcF3pWI6eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔹
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/439419" target="_blank">📅 14:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1-Orjb4gRfOm4iEj1T_eeHVCMLTPcK2rs-gGBzK2yvtvD19wlIT2jFplPQ6opL5ZASeDxVR0a1Go85g4h3Vq6DZOJC-a3HUFiUNpdk6gz6oYnGeHjxQ2wXhwRIN8rlcph3IIZqqijgUZDbXsMiPGeQvq0s3aB29_EC1-FuTrVyeBg4zuhHPPqo5kHL-mZqVb-OWcodzzjTyX2lecpPUgix-8_XifwdGtyK5zy0TeaFsh3vjMHxSR0ueLvaslXGGxh-_g6ud_lVAC9xHrQ4uSXwwPTw1IqPmWIBSMxSQvnAT7qTUypCqh41-e1021nBCv1YzNORc6L66UCJ9eVFjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقف کارت‌به‌کارت روزانه ۱۵ میلیون تومان شد
🔹
طبق اعلام بانک مرکزی سقف کارت‌به‌کارت بین‌بانکی در شبکه شتاب از ۱۰ به ۱۵ میلیون تومان در روز افزایش یافت و سقف خرید با کارت بانکی به ۴۰۰ میلیون تومان رسیده است.
🔹
همچنین سقف انتقال وجه غیرحضوری حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان افزایش یافت.
🔹
سقف انتقال آنی(پل) هم ۱۰۰ میلیون تومان تعیین شد و انتقال غیرحضوری برای افراد ۱۲ تا ۱۸ سال به ۳۰ میلیون تومان رسیده است.
🔹
خرید با کارت برای افراد ۱۲ تا ۱۸ سال و افراد محجور تا سقف ۱۰۰ میلیون تومان امکان‌پذیر خواهد بود.
🔸
سقف انتقال‌وجه پایا و ساتنا همچنان ۲۰۰ میلیون تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/439418" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90929c1a8.mp4?token=sZGrWDpKcKKNc_TL2YDlzB5L1rQhih6uZCTZMCuNOwvVNgHcF5OPBgs2KI7RblnJd7y1kbU_qHQOnvNoG-UmZSQTsZ-Nhns8GyOS0fObl0bThwOcjkiR0COaa74n5lYEq6X3zmvYFDrbomYTrNWflD8Cah02GRavIDsG0hOAR5n1DwczDU4Wbs7mFvLGWQo9Cv56CadiQ5fQHsHQAP84mAMMOxIH89XOE6u22YsY6sKr1jMpi49FXJlXoU1keArW05sdiCqAWWEZXMhuPKsDK4vhdc8AW5sXddTswN0weZl7GlGeQw5hLkkyw4sdde13djRTNHP1iikx_VWN62K4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90929c1a8.mp4?token=sZGrWDpKcKKNc_TL2YDlzB5L1rQhih6uZCTZMCuNOwvVNgHcF5OPBgs2KI7RblnJd7y1kbU_qHQOnvNoG-UmZSQTsZ-Nhns8GyOS0fObl0bThwOcjkiR0COaa74n5lYEq6X3zmvYFDrbomYTrNWflD8Cah02GRavIDsG0hOAR5n1DwczDU4Wbs7mFvLGWQo9Cv56CadiQ5fQHsHQAP84mAMMOxIH89XOE6u22YsY6sKr1jMpi49FXJlXoU1keArW05sdiCqAWWEZXMhuPKsDK4vhdc8AW5sXddTswN0weZl7GlGeQw5hLkkyw4sdde13djRTNHP1iikx_VWN62K4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
عبور ۲۴ کشتی با اجازهٔ سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۴ کشتی پس‌از دریافت مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/439417" target="_blank">📅 14:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9O6OVxSbwRO7dc1I3lC_btu5pXapQvQK44jPVcMtRivOr7SuqSkyrD12A-h6RXUzEtJa6eAl9SGcOeMtqxTkAhoek1yPsSk7YU-YkLlMCQxch4dN5NqFPPcedry_cb-XLCVNNyi0vOPyY6N2RAQ8UC0yHRVhceXwcf9KGk-YJ6uFupFbTX5doe_78LWCNAgqSftisQvu-zcPx9aX8kgHBIPVxzpU1Dup7QipM0hSn_u5aPEx9k3AoZvtSnK0wsYQ78JgxrTw6sGMQxN69N26uOx-P8ZhU_hk8twNLdWr3qdM01l-CCJH7YXnEANdgnEIjtgj_NxB6ZDCmLm1eFgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/439416" target="_blank">📅 14:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این خانواده‌ها به‌زودی ۳ برابر یارانه می‌گیرند
🔹
براساس اطلاع خبرنگار فارس به‌زودی یارانۀ خانواده‌های دهک اول تا چهارم که حداقل ۳ فرزند دارند، ۳ برابر مقدار فعلی پرداخت می‌شود.
🔹
طبق مادۀ ۱۳ جوانی جمعیت که در سال ۱۴۰۰ تصویب شده، سازمان هدفمندسازی یارانه‌ها باید با حذف یارانه ۳ دهک درآمدی بالای جامعه، یارانۀ خانواده‌های دهک ۱ تا ۴ که حداقل ۳ فرزند دارند را ۳ برابر کند.
🔹
قرار است سازمان هدفمندی ابتدا اجرای قانون را از خانواده‌های بیشتر از ۳ فرزند در دهک اول شروع کند و به ترتیب به صورت پلکانی تا دهک ۴ ادامه دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/439415" target="_blank">📅 14:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439414">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlDNNQTV3aV-VYWtTkgZA68optelPo978mJM9ACPp_EFk3NrCEVFHYw66g5woTqrKhuVD1pigChtwYTXEHcnCKPY6xf7uO4fM61rLku9Bn8rcwdkFq1tSrulxiFjL1t2xgYLxAWcMNWQC8AHeiD-96sYKXJq-opLPrTLFRkIvIAXhDxs84KJ3CqEX1ZX5-ndLVpiBplecF6Kmjw0KFNkZWFydry8Rppl9vW2dabAdKOSXz3LN6cSMleDMJ42SiQVVx-vmi8IH7lOcLSO4zUPje1EuRKZZM1p5BaSE13Whx8s5ZWtbQ_LWhRQI6Cs8ohqs31BV0mzMKSCH7ck6AFtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس یک درصد دیگر هم رشد کرد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۴۴ هزار واحدی به ۴ میلیون و ۳۴۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439414" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
