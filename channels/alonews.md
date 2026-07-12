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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 920K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-133369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شهر هایی که تا کنون مورد حمله ارتش آمریکا قرار گرفته اند
🔴
بندرعباس
🔴
سیریک
🔴
کنگان
🔴
بندر دیر
🔴
عسلویه
🔴
چابهار
🔴
کنارک
🔴
بوشهر
🔴
ماهشهر
🔴
مثل حملات اخیر، تمرکز آمریکا به جنوب و خط ساحلی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/133369" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/133368" target="_blank">📅 04:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کان نیوز:
عمان به آمریکا اطلاع داده است که ایران پیشنهادات مربوط به تنگه هرمز را رد کرده است.
🔴
در پاسخ، واشنگتن تصمیم گرفته است که محاصره دریایی و عملیات نظامی علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/133367" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFH_iqE7BWEcbnZhHXa6_1d0qe9ACIfFfTWL3LVwMmGwydlZ1xTqaBd8gnWjDc1VLq7b-p707_hq0Fw_VbWm1btF7DjDGH0Eov0HGI-cNH4ncoWByk98n0q38BDYCu3NQs-U8ZgEmdtSQ6BbwA09YJBUnH3ZDWMXFpoH-yKkcEoYckmpSoxZJ3u9q0mYUqgMlWILiripj7Yd3F8A1TNXlxG6sp-zvYXQZlExwLt7YISAj7d5diyysZHil3EuZficRWq_ZCdKD5LISxHy3ZJyG3i1e2amUPtR8919Fx848tA5K-kxet_DZyLB8OVQiyZmCDANhpL7pSjSVgOHo0ZoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک های آمریکایی از کویت به سمت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/133366" target="_blank">📅 04:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
حمله آمریکا به پایگاه هوایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/133365" target="_blank">📅 04:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/133364" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارش رسانه های عربی:
هواپیماهای نظامی آمریکایی به طور مداوم به سمت ایران پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133363" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یه کشتی میزنید، ۲۰۰تا نقطه بمبارون میشه!
🔴
هرطور فکر میکنم عقلانی نیست و حماقته
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/133362" target="_blank">📅 03:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/133361" target="_blank">📅 03:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
چند انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133360" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0U4DfkXeB7IuMQALnVdiBsvaoR8H4lJ9TmYYUxWqgu8l8I1woBNYPyLv1K0ztsyxvdkjREzuOsPzfob5pRFuUc-d2kxmJueSG8IJgoOoxWWHtwsb2-fLKlu85QN-E4nlkRyoSs_JIbPqVKgEz5Z1-rpUphXvJmuNd5eyZJPXRufFRVNyTxtvvQiigDA48qJVVzv-f-9aChCM0YH4pp7lCm4hss5QDhRp2Hp98qDpx-97cdAJIAfZ1JcqmUXhJkHI1oc3bSOPG2-vRfiE5lLlRfZZUVE2s51l1dtpHx_0-rb283NoH4G5poVxyxH4O4YRPKbrk0kv0lwttg9ekDUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133359" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/گزارشات از حمله ایران به یک کشتی دیگر در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/133358" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=gFl8S8NfkarKHJKcJY6IGfWtMAfRtd0NSKGgga2vnuZQ5X550fnda6-nBFh03g1K_QPkqdG8Ikdzj35u8g3oyE7NLNOdstk6rVVcM72k1TLgEy3D6eW0DOxlSRLQx57kH4Kmu42jWmfPRXK4mF2BbNrsZ0KgolSijgfFsVnmBdcMEORcHjw6_3P2lnS9TmDRD_YjVs2PCWe01rYpRdaltUrwzPeRmuUQ_m0fNkMZ7hDdofYPCfu5GMIAUHXWwTczVBFC_PeeIgpW72eiDfd_XBVkxXmX6GVQ_Z2MZnqKnr6TQex339xNFVBD6vGiaplQQj7Z6bDRWAoeXGYzohqdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=gFl8S8NfkarKHJKcJY6IGfWtMAfRtd0NSKGgga2vnuZQ5X550fnda6-nBFh03g1K_QPkqdG8Ikdzj35u8g3oyE7NLNOdstk6rVVcM72k1TLgEy3D6eW0DOxlSRLQx57kH4Kmu42jWmfPRXK4mF2BbNrsZ0KgolSijgfFsVnmBdcMEORcHjw6_3P2lnS9TmDRD_YjVs2PCWe01rYpRdaltUrwzPeRmuUQ_m0fNkMZ7hDdofYPCfu5GMIAUHXWwTczVBFC_PeeIgpW72eiDfd_XBVkxXmX6GVQ_Z2MZnqKnr6TQex339xNFVBD6vGiaplQQj7Z6bDRWAoeXGYzohqdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/دیده شدن پهباد در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/133357" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/پدافند ماهشهر فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/133356" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/133354" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
انفجار در عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133353" target="_blank">📅 03:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/پرواز جنگنده در قزوین به سوی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133352" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
اگر وضعیت کنونی توسط میانجی‌ها مهار و کنترل نشود، تنگه هرمز می‌تواند به نقطه آغاز یک جنگ جدید تبدیل شود.
🔴
به نظر می‌رسد ایران پس از پایان مراسم تشییع، دیگر از آن محدودیت‌ها عبور کرده و اکنون بر مبنای آمادگی برای همه سناریوهای احتمالی عمل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133351" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/133350" target="_blank">📅 03:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdwE7rI8BVFouu_ynxN81U0TUk2yCixabc7E2ZmIa8Sz1sv-qBUVV-8ztUrFGNRQLzzXOE9yuRCmOHCesntgiv_BWl8wMmtEmXnQ1ruBzfdxLRAPvnl2ism7jhEBBFestPAl80XO-dKiF2DAUITrOw52YixasCLyYmeA4bQL5FSl9r_SWqIHNL2O9K1Ch4SdBpS-8e6ZCs4r5dS47cWE5l-7irYBhBv9Jmfsfe1dQqxZrhCtSr-_9g0dIiltmhrzJQqFPcLezbEAtUem2BNWO4Ivx_DbmOlj2f_9Y4_h5MiKAA2FjceBI1TPExOYBtApaLFFKILQEXZBS1k1a0g0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هگست،
وزیر جنگ آمریکا :
- ایران انتخاب بدی کرد، حالا باید تاوانش رو بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/133349" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133348" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic4A505jhWb1CwC_r8wvrlc4ju3-yukzF11MAvHgEWzi8iE6zkF-k3iJghPKdZbMNdz8bMVymPTPjPk-gjyIes_YnSNTCOWFiM5Qy03RbAklihW-HCV7VjXTSc7MwDv-gBaDwuIWgSkJN6gQYYBtqRO6uRBZ-V6d6zytkOkeEoeZC2N7G6qsArZdLLLaD4SHSSvAzkwxFyORHAU3aeAKpEEPnLbB91dkT37sUn0OFEW8IqlpG-nW8gQ1IegGZYXcttTlM9Q6114eIpA2z3sgXmoj9H0XoiPoDDlUmTmTvwRXbH9neDhu_DSItZiZYHW5ahFJ7Z_z8Eo27UNCCih9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ساعت ۷:۱۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از حمله آشکار نیروهای سپاه پاسداران انقلاب اسلامی به کشتی کانتینری M/V GFS Galaxy با پرچم قبرس که در حال عبور از تنگه هرمز بود، دور سوم حملات خود را در این هفته علیه ایران آغاز کردند. یک خدمه غیرنظامی مفقود شده و کشتی به دلیل آتش‌سوزی در داخل و خسارت قابل توجه به موتورخانه قادر به ادامه سفر نیست.
🔴
پس از آنکه ایران به خاطر حملات قبلی به کشتی‌های تجاری مسئول شناخته شد، اما دوباره شکست خورد، فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم به ایران داده شد.
🔴
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی را تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133346" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🔴
این چنلو حتما داشته باشید زمان جنگم پروکسی هاش همیشه وصل بود  @proxynab
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/133345" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/بر اساس گزارشات، ستاد فرماندهی نیروی انتظامی اهواز، هدف یک حمله هوایی قرار گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/133344" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن  اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/133343" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن
اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/133342" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که دانش آموزا صبح باید برن حوزه امتحانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/133341" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
انفجارهای پی در پی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/133340" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/133339" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فووری/سی بی اس: حملات به تهران هم‌میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133338" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری/انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/133337" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7sVCytAoU85DGm_Ctr0tqZLkS-pPEpXHyN4EdWklkstZ3VxPDTkX5i5iJ2seqPV3nAd_4vMmr9rsf6F3_KCq3RYwEZIabZsBuzS8DRJ08tLO1OZNsmZlD2OCzJLgFKKQlylGwiP1H2FC-ScUPq_lDXqXf2o6Zr8J04-rMv74_VPG2YgnXN3ZLzRtD_5sXih_Fp7zFCIV7VUuy0hxqHOCY4XhAwnbxkwkieTojf3R84xuy1gtE_Jo95n7eWqyEjm-8j0UW1p334Ktvtu2a-5sUEgbavtNmjfNza8cYUxlpvUH4NNJ42OtBDILraTy0zsjhl0kgVACXYRRafeN55m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار شدید در بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/133336" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/133335" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/133334" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/حملات به تمام خط ساحلی جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/133333" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/آسمان بحرین، دقایقی قبل/ظاهراً مبداحملات به جنوب کشور بحرین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133332" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در دیر و کنگان شنیده شده است/احتمالا اسکله دیر مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133331" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در عسلویه و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/133330" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/العربیه :
هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/133329" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/اولین تصویر از موشک باران تنگه هرمز
مشاهده فوری</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133328" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تابناک مدعی شد: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
🔴
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/133327" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9lP7YmL0dh83dWEDq7hFyL_H2iahCPAUtjFqIEERtYJX6HMV1psKRKBa_csTGkpHccgkjfkdV3wZr6Tse6hDYMVTqP2Jp9glUuDy-YjnAC2kBMbcPERUs8l0vUiTqTj7e5GQfBL9WMgORKCJDPAQeQcT-wLSc2ZRGt8f_2Yd0YeFT_8g-gmpLE7i0EyuREea4ajDLJFWRxw5V79WB5phB2dEstb0ZrhBZsd0lcGm6vb4dap9Ut9bniWo3-a2gWCF552Tae_qvBo9LM2-Vpet_MgTzRxD4trAlNaa9YpOlWlc1MzPXRRc3xRh6spDfoUbtyA89FtJ30qTrBahUkUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل :
مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/133326" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/133325" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فعالیت های رادیویی شدید در خلیج فارس توسط ارتش آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/133324" target="_blank">📅 02:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کانال ۱۴عبری: پس از اقدامات امشب ایران، ترامپ ممکن است هر لحظه چراغ سبز حملات به ایران را نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133323" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLMVH5knlCyuam4L2ARcoV1a8O2ixUtB36wO18PvQdVGkjAeTv3UpQYKNS-UGte8DTKQHxIglKBSu-5jwkvJ_pFWwSBpXWpfwRC9bSu14BhXu4SKDERVGwxsy5FSN8WgkpaSM1ZNBHIy2Ags8EmC_Y94SXQohl31hcrJmj_2_gUG61kSEknDqx_ZkLByV-fNbS_u91ZLLssCuVHgiQX0JU4VkH3epr6rrmggoOOf7AjaQVuDOwJtx36tZ1aLSP_ToKsOf2gkYNAfQEE7SEXFFS0ndtxczHrLTdl0TZrialZ4PVcv9FqK9-uylOJa41S-4x9tEKG4-yhucaUtMKX0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همین الان ترامپ که رفته بود گلف بازی، بعد از شنیدن این خبر زمین گلف رو به مقصد کاخ سفید ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133322" target="_blank">📅 02:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFhc_uGOb57QSAqvC_-Uv0klZhUGvKDQyOxfs4o9VjgqGquyQToTQ_nfXdiwWSv9vhRJo6dovICQXJPzHnu-T0eLnqAI29tqG3DSDlubBqN6U3sw3AyOFrqd6EjuGzKmqBcgOFgROcoKDHYJa0T5MbchuDH-EEyCGgT1GibDcxX4pDNabE86B6eLCYx4Z0PI3yw8PAkchkFXx8vf0--H-__o5xOm35nD8--72h5sIOhyIqw_MmNWiAkbNq1kW-9Y5BHh9VKPVano52SwNnlGoe-10bhsX0GzuV7R8hjtO9LLRnfJd3VnKdlufSnCvQ_Rc4Epah7-NBq2DMBKlYDp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133321" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آکسیوس:
ایران ساعاتی پیش به یک کشتی تجاری در ورودی تنگه هرمز موشک شلیک کرد،
موشک به کشتی اصابت کرده و باعث ایجاد خسارات گسترده به کشتی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/133320" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
منبع عبری: رهبری و نیروهای مسلح ایران مانع بیانیه تسلیم تنگه هرمز شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/133319" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شبکه خبری آمریکایی «سی ان ان» به نقل از یک منبع: عمان اداره جریان کشتیرانی از دو مسیر جداگانه را پیشنهاد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/133318" target="_blank">📅 00:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کارشناس فاکس نیوز:ترامپ ضربه اصلی به جمهوری اسلامی را برای بعد انتخابات مجلس آمریکا (آبان) برنامه ریزی کرده است و تا آن موقع تنش‌ها در همین سطح باقی میماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/133317" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9_tv91Df3A4Qd9aLTDX3ASLfADfJeA16-zXDH5hdVw4lh34c-ChZ-RPAmMjDH6jfeYqQhaVrH7t59gvSz9KRpMdFW8-OTCgJ-ZyqBGg4K1lHgBgr1nFxw8jmJ1h-dNU4bS6gV37d2EJnxB0jXiJJGLLmCsI_0p2e3aBJG2huJLvxAXo38YMJevNatQ78S-4EY0R1F3BtDPN8GogOyeiaLJhFU5sGsg5aEmBTeAkQtbEiSARHr_5x6E5c-Y7-Izt1HdbC_QQkQSRxn5b5wReoc4yxN45uQg6dvQGTUmyXAP95R17dObnLQdyqL6mYZsm71Sy8HKWeXxkQ0MPoV7lbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری C14: ضرب‌الاجل ۲۴ ساعته دولت ترامپ که جمعه ۱۰ ژوئیه صادر شد و از ایران می‌خواست حملات در تنگه هرمز را متوقف کند و ناوبری آزاد را تضمین کند، ۳ ساعت دیگر منقضی می‌شود.
🔴
این توییت برای 2 ساعت پیشه و 1 ساعت دیگ مهلتی که ترامپ داده بود تموم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/133316" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیروی هوایی و فضایی روسیه، در یک حمله به شهر چورنومورسک واقع در استان اودسا،  با موشک های کروز حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/133315" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / گزارش هایی از فعال شدن پدافند هوایی در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/133314" target="_blank">📅 23:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQQqqWM71mXFpxLhqy5XvJ2cG_fIygoHtVdKZ_IFcWjA5tJ3fAzb2BluDkLm2OmAk_3HBwG0QhCu3_BQjGa0BhhD1J9L1xBghqo_qSY-moWH1Fk-VdMXHsMOZygR0ZoHaVEsRj7AWM84hgx4mRYnTMtAizZCL7HAOGQ7OGC8wWOgGuAr8caRB29AnOC5XLDWlBmoF6ygsK7XZCAZmxeTFT1RUm5aafIyeOVmThREm52B1Qs_p2Kx4HBurUErCcxu9ElU-8-1wh7iNWFlUDhe0BF5SIob60JDKkz_5Yy2aJCm6N81-tVU62lW5r6eED_YtBaBOGo2F_QhPGZPheolKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات LNG اروپا از آمریکا
🔴
وابستگی اروپا بیشتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/133313" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obg6-e3T9TsXTmfok22vZIzIC_tC5eMGKWviTDX2W51Gny9Rne5rY6w0ggEWw3bqQgy0HyYkpCl7vKNmqV9V9qosApQ_bpB-ZW64ma6dxJ52EA6v_2mQmKninArrs3Z8RVlvBSz-zUiiEZiAr1okSuXzTq8axy2qyCK2Y49TbGthmSGDRnbyh-meJzmQ3shBk6bxcb65cSyo_ykejA9cIANS_HAx-D3G_w2Dp7xTtlhAssAq4bvhd41YniSGGgoEwcbQHSvgr3Y1U0lxAMnE1aJePe0zHXVONE_GZ-XY5XNFcg2rset2wnQCTS64uD5JhIkiosBCVauYNqsUY9K2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کپلر نشان می‌دهد تنگه هرمز قبل از درگیری اخیر به سطح قبل از جنگ برگشته بود و تانکرهای پر توانسته بودند از تنگه هرمز عبور کند و نسبت تانکرهای پر به خالی به وضعیت تعادلی برگشته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/133311" target="_blank">📅 23:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل: سرویس اطلاعاتی اسرائیل به ما اطلاع دادند که ایرانی ها توطئه جدی کردن برای ترور ترامپ.
🔴
اونا 47 ساله شعار مرگ بر آمریکا میدن و بنظر من تغییری نکردن، اگر یه نفر بتونه رفتار اونارو تغییر بده اون فرد ترامپه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/133310" target="_blank">📅 23:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شرکت توانیر: از این پس اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری، با هدف ارائه خدمات دقیق، سریع، شفاف و هماهنگ به مشترکان، صرفاً از طریق درگاه‌های رسمی انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/133309" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقام‌های آمریکایی ابراز نگرانی کرده‌اند که اسرائیل اطلاعاتی ناقص یا گزینشی را در اختیار دونالد ترامپ قرار داده باشد. این موضوع ممکن است به ازسرگیری جنگ با ایران منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/133308" target="_blank">📅 23:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjK50ChA7WJtAm6VA_TsyBRI2c8G2axYpMUhZpjWHCNkdHQfFf3XL1OojlP0WdDrWqZBOIjnqRXZp45q68Mmgux_uXXHHPMtAVZlgNNkJK64owo63l1iXWhnv-sPMuo1CkNYpbfxzL2BNqCEMpoIAcYlT-QI0gXdriErc8EK1jgUV-LSbI0bc8CWNo1eVo1wB5Ri6BXXK9FvlayvdCSdFiOzKAtQ4i9upE4IqC1VmURuGIrgGUM2AO1XrxkfNATwuboMcg-gN4jCG_Oc1WZ5-HiG7kaY-913STMeHXYs_nsSNYmS7yI3G6vw1cAotoogPKCsh54Y5DuBLfDnqT_lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی تقویت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/133307" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG1LREhNIjeIf_mcByuvmuWjE5-J51XdR2XZyB2_-erxZD4S5DK2zLPXtbKniLgxTV7bstoxN0U4Ub5_vQTpH62Z1BWu00lJO0MmEPq2Hj7eihpUwCsc_eiL0j8tYPTkc9xB_sArK2lPjBnj1wqO0RY0MT81IY2FJseTG6wxxtMg-0vugAxnFOkpAd9plRCq4bZxukQkZy9zYpIPGTLELlaUHb4BlOn_QE8ihRIPz7Z678rPWPXGlYQA9NkXq5PrQQmXAaGHYZzi-yumh_fGPl2EfP1Xaj45A8qUSvS1iT5aNL132HysCv6JBO97Px0FNtVDgcuvRudxheMCK_YKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول اطلاع رسانی خاموشی لارستان منتشر
شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/133306" target="_blank">📅 23:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مهر : اختلال در شبکه بانکی همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/133305" target="_blank">📅 23:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شرکت برق منطقه‌ای تهران: بر اثر حادثه فنی در یکی از پست‌های برق، برق بخشی از مشترکین ساکن مناطق شرق تهران دچار قطعی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/133304" target="_blank">📅 22:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب استان تهران: هیچ برنامه‌ای برای افت فشار و نوبت‌بندی آب نداریم، چون وضعیت پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/133303" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / نیوزمکس:  ترامپ در حال بررسی ازسرگیری محاصره دریایی است
🔴
دولت آمریکا دو ناو هواپیمابر و بیش از ۲٠ کشتی جنگی را به سمت منطقه هدایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133302" target="_blank">📅 22:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=Ig5by9JLHJ87u8Cv29N2tDv2voKymtj9U37uzciHsz4spG3j_ZEuBEOs_Iy5mTWRYLoDZ15LKSLaN2E6cwTuU2b_F1xPOlCnFXborUWxUbVZqg_6YGCs6FiBrB1jpSYv54K_6eVlgu9ydJXaUr-HuF1EmHI2Mr9rdKrOueH_bLKrfqvRms2Tj5r7V_khfTzFTnWcKsUkGpQoBHrOwfgIexM3nPjZE2InHQdgOScu4Lgneh6OGr17ps04fQqwSfm9mDaEQxQTHb2gtQYAWK7yYQgLXw3VdlIxN0-dnsKNEkU9l2CfGB4Qv51uxEDneOjw99tbd-LSMYYBWLS6SWPhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=Ig5by9JLHJ87u8Cv29N2tDv2voKymtj9U37uzciHsz4spG3j_ZEuBEOs_Iy5mTWRYLoDZ15LKSLaN2E6cwTuU2b_F1xPOlCnFXborUWxUbVZqg_6YGCs6FiBrB1jpSYv54K_6eVlgu9ydJXaUr-HuF1EmHI2Mr9rdKrOueH_bLKrfqvRms2Tj5r7V_khfTzFTnWcKsUkGpQoBHrOwfgIexM3nPjZE2InHQdgOScu4Lgneh6OGr17ps04fQqwSfm9mDaEQxQTHb2gtQYAWK7yYQgLXw3VdlIxN0-dnsKNEkU9l2CfGB4Qv51uxEDneOjw99tbd-LSMYYBWLS6SWPhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی: این مذاکرات مانند خوردن گوشت مردار و میت در مقطع اضطرار است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/133301" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFE1Xfq2lVDMBkTtK7rhhw5RPNMruf9rCRCZsRczZ7lHvVdZahVxPgNsQ7UXvP6pOeRYMMMjqnYQLI1M7clbpq9owvweoBVXBLJ6JUo7hMFQuBSOovTF29T0jiz840wa2Zh17SKyPHPNSKlPcEkQJz8kbPRLHQSuRLIUg9RpeqYi7OGYvcxlmBczLckD8jyc6LPflGhqVwRo2jaR8TGpLpIHMMC-VXUqHD_fi3o_MYNYyFw3kJX0oQJWbdtTTctUq6W9k0XC-iuSDQrYG59SnZ3d1n2ZWyokKMdZW_0mmfHS68wYTN8is4Luhup5lT2GWaID6Y8HlntMuR2dzc473Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید : یک دیپلمات آگاه از مذاکرات گفت : در جریان مذاکرات امروز در مسقط
عمان گفت مسیر ما مانند قبل باز خواهد بود
🔴
این دیپلمات گفت : ایرانی‌ها نتوانستند این پیشنهاد را در جلسه تصویب کنند و مجبور شدند آن را برای بحث‌های داخلی به تهران ببرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133300" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آکسیوس: ایرانی‌ها طرح عمان برای ازادی ناوبری و رایگان بودن عبور و مرور را برای مشورت‌های داخلی به تهران بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/133299" target="_blank">📅 22:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سی‌ان‌ان: پیشنهاد عمان مبنی بر عبور آزادانه و بدون هزینه از هر دو کریدور شمالی و جنوبی در تنگه هرمز در حال مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/133298" target="_blank">📅 22:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9bf0823137.mp4?token=u6ZrQBuU7V86pKEusXmhfR0x9cQkiG6iSYqSIuGUIvXv8PZ5is8Av6yotkuRZMBOUXWtSOex7G5bRZ99BC0PzIU4CTZH59lY3pz7S4EOZUWovKAAMz04UL5oh9MKgDa2p1C9Y3fGweE-vdGZWDXjvDM5myRNxc1Dputdv7voH-7DNWA9LEkGa88axlyLsEjDu7Td9EIYVQCxihepcCDLT7HQN_oxqCei0WoqIvukdqCbY3m66yI0Uuk6lQ9fck318yZXT7Jw864bjqYG03KbmUMkkpJSwPIMKqbxQRwIUKLaQiEnD5K41p5IbUpYutsjQXwvcqzQMxjhmqZkgTurKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9bf0823137.mp4?token=u6ZrQBuU7V86pKEusXmhfR0x9cQkiG6iSYqSIuGUIvXv8PZ5is8Av6yotkuRZMBOUXWtSOex7G5bRZ99BC0PzIU4CTZH59lY3pz7S4EOZUWovKAAMz04UL5oh9MKgDa2p1C9Y3fGweE-vdGZWDXjvDM5myRNxc1Dputdv7voH-7DNWA9LEkGa88axlyLsEjDu7Td9EIYVQCxihepcCDLT7HQN_oxqCei0WoqIvukdqCbY3m66yI0Uuk6lQ9fck318yZXT7Jw864bjqYG03KbmUMkkpJSwPIMKqbxQRwIUKLaQiEnD5K41p5IbUpYutsjQXwvcqzQMxjhmqZkgTurKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استیو بنن از نزدیکان و طرفداران اصلی ترامپ : موساد با مطرح کردن موضوع ترور ترامپ قصد دارد بار دیگر او را فریب دهد تا زمینه برای آغاز یک جنگ جدید فراهم شود؛ جنگی که این‌بار ممکن است به تهاجم زمینی منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/133297" target="_blank">📅 22:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEyMcSg3rpX4ezEagpQBaVuHPgOIzIZCJgMJ5CYNYpAEk5MGJbl03xppLGwuAyIe8CrVSX7rc2H_-_pFIOLiWjt7cAh1u-g38O3siIRAB_dfnF6AhzRd2GmKgaYUyRmEXj00fv7n2oFA_56MbkhSolH1-6eUTsKD9gEvAXw3dUrw2_haJKj4FotVcCO6d40mBXmIn8RiiupPdL_FkeV7DuE7HCkg-Ip6RxMW0dWIG_jEGE1ioSTo_P3-5Jhy5HmO9ZCyYyriIQLc29rkrwGlDnyjxtfjD3OBBVY4UZhqkop_hsWmVZE5me_bB_l4jPGPI4Wzn6FfhQcPpU3n4C1L0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: تمام وجود ترامپ را ترس از تهدیدات ما گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/133296" target="_blank">📅 22:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
روی خانا، نماینده دموکرات کنگره آمریکا، در جریان سفر این هفته خود به کرانه باختری، توسط شهرک‌نشینان اسرائیلی مسلح به تفنگ‌های ساخت آمریکا متوقف و بازداشت موقت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/133295" target="_blank">📅 22:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت خارجه عمان: امروز در مسقط، مذاکراتی میان عمان و ایران درباره کشتیرانی در تنگه هرمز و تضمین امنیت و آزادی آن، با توجه به تحولات و پیامدهای ناشی از رویدادهای اخیر، برگزار شد
🔴
دو طرف توافق کردند این گفت‌وگوها را در سطوح فنی و سیاسی ادامه دهند تا بر اساس حقوق بین‌الملل به توافق‌های لازم دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133294" target="_blank">📅 22:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بانک ملی قطر: پیامد‌های تشدید تنش نظامی میان ایالات متحده و ایران، مدت‌ها پس از پایان بحران نیز بر اقتصاد‌های آسیا سایه خواهد افکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/133293" target="_blank">📅 22:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: فروش نفت ایران ادامه دارد
🔴
ایران در طول تفاهم‌نامه با آمریکا بصادرات نفت خود را افزایش داد.
🔴
تولیدکنندگان رقیب ایران در غرب آسیا نیز  پس از بازگشایی تنگه هرمز در اواخر ژوئن، برای ازسرگیری صادرات هجوم آوردند.
🔴
از زمان اعلام توافق آتش‌بس در ۱۴ ژوئن، ۵۲ نفت‌کش با محموله‌های نفت و محصولات پتروشیمی ایران حرکت کرده‌اند.
🔴
معامله‌گران نفتی انتظار دارند فروش نفت ایران در روزهای آینده افزایش یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/133292" target="_blank">📅 22:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از مسئولان امنیتی اسرائیل: تا این لحظه هیچ دستوری مبنی بر عقب‌نشینی نیروهای ما از مناطق حضورشان در لبنان صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/133291" target="_blank">📅 22:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال 15 اسرائیل:
ایالات متحده منتظر پاسخ جمهوری اسلامی به درخواست‌های خود برای توقف حملات به کشتی‌ها در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/133290" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قطع برق خانگی مشهد از فردا آغاز می‌شود
🔴
سخنگوی شرکت توزیع نیروی برق مشهد گفت: از یکشنبه ۲۱ تیرماه به دنبال مدیریت مصرف برق، خاموشی‌ها در بخش خانگی اعمال خواهد شد. کاشی تصریح کرد: خاموشی‌ها در مناطق مختلف شهر از ۸ صبح آغاز شده و تا شب ادامه خواهد داشت. زمان خاموشی‌ها ۲ ساعته بوده و برنامه خاموشی در سطح شهر توزیع شده است. اگر مردم بتوانند در مدیریت مصرف همراهی کنند، قطعا جداول تعدیل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/133289" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا : اگه ایران به رفتارهاش ادامه بده، پول‌های بلوکه‌شد‌ش رو آزاد نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/133288" target="_blank">📅 21:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فاکس‌نیوز: مقامات آمریکایی تهدید جانی علیه ترامپ را جدی می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133287" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=qa7XbbsCiZfg7NbXESjJFgTu4Ye6w6C7HCBQn56OOQekOn0aZNSuAI5717TBkJhXFbYg0VCFUjkk9-vLjcPUGX0mTDIIFMaej3BsSkPrIhIB1-LG4xK7feosA6AFAIpwaA4NY-a-A7_lZOl_PfWuT4BpYb1I-8gA6yH9_jz7jKMJd2fWnhLQMUbVXQ-xRw49qIgEwM2Ree0u6eO29UfUAj_qffJNmiAOsXEEb0FgYrg7yOM7Mx2BNB9MtdyvRJnJQLlXVriXDqjQmZnyw5gV3MzqQ_MBoWDRXrsO0-S37K2Nqi-wqeb1PJjwd97OL6p0p30aXZXL-FzjWrmO8lwlgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=qa7XbbsCiZfg7NbXESjJFgTu4Ye6w6C7HCBQn56OOQekOn0aZNSuAI5717TBkJhXFbYg0VCFUjkk9-vLjcPUGX0mTDIIFMaej3BsSkPrIhIB1-LG4xK7feosA6AFAIpwaA4NY-a-A7_lZOl_PfWuT4BpYb1I-8gA6yH9_jz7jKMJd2fWnhLQMUbVXQ-xRw49qIgEwM2Ree0u6eO29UfUAj_qffJNmiAOsXEEb0FgYrg7yOM7Mx2BNB9MtdyvRJnJQLlXVriXDqjQmZnyw5gV3MzqQ_MBoWDRXrsO0-S37K2Nqi-wqeb1PJjwd97OL6p0p30aXZXL-FzjWrmO8lwlgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرباز روس خودشو به موش مردگی زده تا پهباد اوکراینی شکارش نکنه
🔴
اپراتور اوکراینی میگه: "نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره :)
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/133286" target="_blank">📅 21:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMz0xS5PrUuVO8awq1ZTcB2almLyDJ1MirJvChrwdaiGGdhOMXDX3o1zeHnyBItWCAZ38_KSDUk1xVSawte0uUKBY_mtpmFH_HXXC8an69t0Q_j5VLRrRIyCro88c0jlPBYO7RqKeXPseMnHqkdrSsVahH-JnNoYZPsJKauTAVMC_AqcgaPFin68S7-unP0OR3YsBErZUJpDpgtDUHY6wHrtbb_2DoqRiDi4pUm1ckH7vTe86t5FktOhSgo-aUT3IUG4amDkbkYVeitdsXJPkIDfnYWzfMDW-UIK1IkDejF9Ng_4H2eB4mV6JljR7ORrQ3ohUmFz0TLU6fmkeQEWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام در مورد حضور ناو هواپیمابر جورج بوش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/133285" target="_blank">📅 21:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کرملین: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/133284" target="_blank">📅 21:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ارتش اسرائیل ادعا کرد که ساختمانی را که عناصر حزب‌الله وارد آن شده بودند، در داخل منطقه امنیتی هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/133283" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c328913ad5.mp4?token=QUSryWfyN1bGPDfFtG0wXbgOdfPVcThimvGYnYvK7XwLPz3F8KyL7AQq5riKyGJWOwpeErNlKlI0hDd-R4kC8mylaK2MeohLnjJTYSGHD4lJ8gJdGzi6-QZnGrIxObxyHW15_KlQj5WXHQyAgSWZBWhGMHdK1zqWLcuGeL9tr-dnrZFTzNP1qVaPLgrG6pCOJsLwNMx9kyh_n9lV2L2J2JBfzmGtvxD-I7o8xFmsqvA4vUc5xfszfyWsmjC-m0ag_Hha2fPD1IaYxm-fRg2WkXHS6bVHkhqIB-tDI1HYEn5HHWHIkl5gukQaOO9H-UJvW-3Dk6UtsZMwlj5i62GO8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c328913ad5.mp4?token=QUSryWfyN1bGPDfFtG0wXbgOdfPVcThimvGYnYvK7XwLPz3F8KyL7AQq5riKyGJWOwpeErNlKlI0hDd-R4kC8mylaK2MeohLnjJTYSGHD4lJ8gJdGzi6-QZnGrIxObxyHW15_KlQj5WXHQyAgSWZBWhGMHdK1zqWLcuGeL9tr-dnrZFTzNP1qVaPLgrG6pCOJsLwNMx9kyh_n9lV2L2J2JBfzmGtvxD-I7o8xFmsqvA4vUc5xfszfyWsmjC-m0ag_Hha2fPD1IaYxm-fRg2WkXHS6bVHkhqIB-tDI1HYEn5HHWHIkl5gukQaOO9H-UJvW-3Dk6UtsZMwlj5i62GO8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل دیجی کالا: در سال ۹۵ پرفروش‌ترین کفش دیجی کالا ۶۵ دلار قیمت داشت و امروز پرفروش‌ترین کفش‌های سایت تنها ۶ دلار قیمت دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/133282" target="_blank">📅 21:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از مسئولان امنیتی اسرائیل: تا این لحظه هیچ دستوری مبنی بر عقب‌نشینی نیروهای ما از مناطق حضورشان در لبنان صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/133281" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txhY1htOG4pnz5hsYi1CMnq1Ob0UmCGnt2WM0pUDysKwWL7LOfNPHjiVMAC1_EaQrCvmdKiTo6YSK7FqWCwru_HfBW5dPBfPQ6PXZo_XUjIyqPZnsc_gYHSZiS0CfBUohC2yRuqgA6Qhmv1oYpfS-2Yx3YN82yQmAgE9nqAKNtREz1Pjbj8_DelnCYdmiuvvmS_LpeIvTfnr9C-Rv5okZfXGfCmgByasLHOZh16UFTjBlZPaN52TocfEHDE8bzup0cbnEkE1Pt-JbWmmGfW_M7wWcjWSD5XVKdBvqIcmxZzHpl3smkdJ-749bhmLWBIEM7OopeRrk7IjAuBL85jjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون 6 فروند سوخت رسان به همراه یک فروند آواکس در منطقه در حال انجام مأموریت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/133280" target="_blank">📅 21:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8c10b060.mp4?token=POnKDnkLiEIAysOt589HfxkrjzUB5gNGFb7Sg7y5yKTFkorJQmxNXGn26rPs2UUHocLl-_Epqs79O72YtP6urStMIwI9tDFCDemSmlcUfn_D7dGJRbvIWnpEaH1XbzXeEKlBy_tnS_mNfN07k25kZYHUXgl0Jd3DpSGtDyjT9L_9_504VYSTTB6MRyFhwxBtbqkK_jDEiLOxotJUaIOPpL9_TC4GJMs5wDxcj3v-qfcTpo7Trg_WpeSv5on_dZQmlK1yPraAMLAWL-RlEHq1xzqbIXfyOPVJTumBonzaA0lBMBFjsuGdkJKNmf5MOLwCYwNjNA7aQJKreC9UZtuotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8c10b060.mp4?token=POnKDnkLiEIAysOt589HfxkrjzUB5gNGFb7Sg7y5yKTFkorJQmxNXGn26rPs2UUHocLl-_Epqs79O72YtP6urStMIwI9tDFCDemSmlcUfn_D7dGJRbvIWnpEaH1XbzXeEKlBy_tnS_mNfN07k25kZYHUXgl0Jd3DpSGtDyjT9L_9_504VYSTTB6MRyFhwxBtbqkK_jDEiLOxotJUaIOPpL9_TC4GJMs5wDxcj3v-qfcTpo7Trg_WpeSv5on_dZQmlK1yPraAMLAWL-RlEHq1xzqbIXfyOPVJTumBonzaA0lBMBFjsuGdkJKNmf5MOLwCYwNjNA7aQJKreC9UZtuotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند در صدا سیما : بیش از ۴۰ میلیون نفر در مراسم تشییع شرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/133279" target="_blank">📅 21:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/393888a333.mp4?token=q3zk8UtgHBuvrOAKo-FvQuSzpk4XDs7wAZhq8QqLXobzy98SJcdNDN-Fczz7cwcIL5DFszEYDFBKa_O7rWTdiZNJfOjxRQloJKxI9kJ2At_8YNXAseZNgrwjwNz4BFF3KEmgbc8OTX07PY655FnK2oAMZS1halY7muiG6646iBiRUj-VuHXHK6H56QoyS8LbbLTu7FqlkVIpLBM8hTeJmSpn_zp6zVUzm9_4IeOCG7Ach0p-klMxFG_JiFqWs6d1s8c_7tza64q6Ccj_ZrS7PSK_ooC61FhxMiai3YPLl0nwvgXO5cgLsu2t0uYKxaah5wR9NbJHoeGJb13iTbMJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/393888a333.mp4?token=q3zk8UtgHBuvrOAKo-FvQuSzpk4XDs7wAZhq8QqLXobzy98SJcdNDN-Fczz7cwcIL5DFszEYDFBKa_O7rWTdiZNJfOjxRQloJKxI9kJ2At_8YNXAseZNgrwjwNz4BFF3KEmgbc8OTX07PY655FnK2oAMZS1halY7muiG6646iBiRUj-VuHXHK6H56QoyS8LbbLTu7FqlkVIpLBM8hTeJmSpn_zp6zVUzm9_4IeOCG7Ach0p-klMxFG_JiFqWs6d1s8c_7tza64q6Ccj_ZrS7PSK_ooC61FhxMiai3YPLl0nwvgXO5cgLsu2t0uYKxaah5wR9NbJHoeGJb13iTbMJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر باورنکردنی دوربین مداربسته از شمال ونزوئلا که نشان‌دهنده فرو ریختن چندین ساختمان در نتیجه دو زلزله قدرتمند در ۲۴ ژوئن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/133278" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750f49ad82.mp4?token=Jf_B71Z-AmelVE2JgJehUTRq_xP7HS0IPra9v950FvljUgX7v-n-C6uZw7Td4GHre0S-1hJyJGgSiW3AaemheudOd_5w5-BMLdQwcDsunViEmJmxcNcr_YruF4EiPRG3RqHbEhzIHDEJiFS0M8DUpoi9_qgsZTB-Kh2Bq3N-Z3LvmRT_olGJJmVdp3Oiup8Bwle25urOlStYabCtgCQTsXLyldaoFjg9A8Kj6ACJZxa5lOSFC5YbK3QR_tR0TDdsWbHy38BYzgmYqorzDdGJorFPRTFyCTv4orBUPoScn825ya-UY_cs3dSf27KaaAClqnvgP6C9jr1NZg1NXer-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750f49ad82.mp4?token=Jf_B71Z-AmelVE2JgJehUTRq_xP7HS0IPra9v950FvljUgX7v-n-C6uZw7Td4GHre0S-1hJyJGgSiW3AaemheudOd_5w5-BMLdQwcDsunViEmJmxcNcr_YruF4EiPRG3RqHbEhzIHDEJiFS0M8DUpoi9_qgsZTB-Kh2Bq3N-Z3LvmRT_olGJJmVdp3Oiup8Bwle25urOlStYabCtgCQTsXLyldaoFjg9A8Kj6ACJZxa5lOSFC5YbK3QR_tR0TDdsWbHy38BYzgmYqorzDdGJorFPRTFyCTv4orBUPoScn825ya-UY_cs3dSf27KaaAClqnvgP6C9jr1NZg1NXer-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناصر هادیان، کارشناس روابط بین‌الملل: ول کنید مدیریت تنگه را، فقط بگویید تنگه مثل قبل؛ میترسم تنگه را از دست بدهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133277" target="_blank">📅 20:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
العربیه: ایران با عمان به دنبال توافقی بر سر تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/133276" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
روبیو : رهبران کوبا باید پیش از آنکه خیلی دیر شود، به اصلاحات واقعی، صلح و رفاه متعهد شوند.
🔴
واشنگتن به‌طور فعال با تهدیدات امنیت ملی که ادعا می‌شود از کوبا سرچشمه می‌گیرد، مقابله خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/133275" target="_blank">📅 20:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5587a6f9.mp4?token=LkGyN5oQ7DYT3fnqKlk3wZM06t5lBuo5L5QiANCnquI37ckaQ-HXYP78NE_fCfMLqUlHh3lp2bNWw1793nXwZk702WrT4GWp1hms0gyHgwypA58c3J8LRTVzQFSRmfGk53zDXq3k1B04Qy-W11ylzjIrU2LzElmcXWm03tzQeE74W6W1xN7kRBEKrCMsgxDQ7UaqM-k5iZR1hH2mxYhSdvxpfGjyqt2jbGaaL-8S42Z49POfATC5uucqfVc4YLFJsSHAsDgHVxXllMUvrvBXxhj5lmsKhDmc-y1SymZ4WezjgL7nBFRLZzWJga6CLToGlLbwMXjNZGpOmhgvIBr3NH2u9xO_db1nNY9bhbYk-_H6fwpEGI1t3VMemBlJg5UWWGt5pw19Ep6GbQNmH3pxoOW9BUy0ADlMfMrWDEFx_0uMJp6KmuIMRA5KpRjKuLLliss3d5UR7JhihMPCubSwex75U0yA5bYL9KnbtdBUB21kUV3xByB3DxdB5IPKx5fpVBs96vgi0IfvWmWemF6dVikcXtMkVUoe2uOSp2LJW27_vOomkq_raCLEBm4nuWn6PUgERAUrSM6qBZzVPdAFki0AcMnI-1yzMpsrzrYh_DSEi0QwJSsLL5MY1EvPsDoO_jr4t65QjmRXwzcAiarFY8d33Iw8LQMNnmFZQkzywAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5587a6f9.mp4?token=LkGyN5oQ7DYT3fnqKlk3wZM06t5lBuo5L5QiANCnquI37ckaQ-HXYP78NE_fCfMLqUlHh3lp2bNWw1793nXwZk702WrT4GWp1hms0gyHgwypA58c3J8LRTVzQFSRmfGk53zDXq3k1B04Qy-W11ylzjIrU2LzElmcXWm03tzQeE74W6W1xN7kRBEKrCMsgxDQ7UaqM-k5iZR1hH2mxYhSdvxpfGjyqt2jbGaaL-8S42Z49POfATC5uucqfVc4YLFJsSHAsDgHVxXllMUvrvBXxhj5lmsKhDmc-y1SymZ4WezjgL7nBFRLZzWJga6CLToGlLbwMXjNZGpOmhgvIBr3NH2u9xO_db1nNY9bhbYk-_H6fwpEGI1t3VMemBlJg5UWWGt5pw19Ep6GbQNmH3pxoOW9BUy0ADlMfMrWDEFx_0uMJp6KmuIMRA5KpRjKuLLliss3d5UR7JhihMPCubSwex75U0yA5bYL9KnbtdBUB21kUV3xByB3DxdB5IPKx5fpVBs96vgi0IfvWmWemF6dVikcXtMkVUoe2uOSp2LJW27_vOomkq_raCLEBm4nuWn6PUgERAUrSM6qBZzVPdAFki0AcMnI-1yzMpsrzrYh_DSEi0QwJSsLL5MY1EvPsDoO_jr4t65QjmRXwzcAiarFY8d33Iw8LQMNnmFZQkzywAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دوربین مداربسته از لحظه اصابت بمب های گلایدی پرتاب شده از جنگنده‌های روسی به شهر زاپوریژیا که متجر به کشته شدن ۵ اوکراینی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133274" target="_blank">📅 20:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سفیر چین: چین دو بار پیش‌نویس قطعنامه مربوط به تنگه هرمز را در شورای امنیت وتو کرد
🔴
در دیپلماسی چین، به‌ندرت از حق وتو استفاده می‌کنیم، اما هر بار که وتو می‌کنیم، تصمیمی بسیار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/133273" target="_blank">📅 20:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کرملین: روسیه آغازگر جنگ جهانی سوم نخواهد بود، اروپا بحران را تشدید کرده است
🔴
سخنگوی پوتین ضمن رد قاطعانه قصد مسکو برای آغاز جنگ جهانی سوم، تأکید کرد که حمایت نظامی گسترده غرب از اوکراین بحران را تشدید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133272" target="_blank">📅 20:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کیهان: یک نفر به وزارت خارجه اطلاع دهد ترامپ هفته پیش تفاهم‌نامه را پاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133271" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133270">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l96TZ48pMwe5Z5ZxO0FANxFaxJ94xmzqceCzkyqJrhdZ_ybH-hgh7irsOdASu65E9JxDnQ9IUyUk1TVqtD3mTOm3_JFjYQ7CaDiZCAvcdog7u9aQTgXPh5qcw60HGXHGf6992pJmRXCw1xDKzdjITYpHjR9_0ErdCse2-Zv5Je8sQC5umgqetyRCg7pp7FJrvRpFLRPI_PmokX6nuafY5iqm3dOmrimiUVVpkKawDFhHQ4GDuZTVS_3cwvSDYbJ3pdvD-SqMOSIlzWjmLQ8MrspkCiEMu-JatVfeIHgUwpj6pdcDgHVBZzXCz7KqtD8PQZBdqlzvpWowC-MDIoSokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور ولادیمیر زلنسکی در مراسم تشییع قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133270" target="_blank">📅 20:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
‏منبع اطلاعاتی ایرانی ارشد به پرس تی‌وی: ایران در حال اجرای ترتیبات مربوط به مدیریت تنگه هرمز طبق بند پنجم از یادداشت تفاهم است و تسلیم فشارها یا کمپین‌های رسانه‌ای که طرف مقابل به راه می‌اندازد، نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/133269" target="_blank">📅 20:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فاکس‌نیوز: تهدید مرگ رژیم تهران علیه ترامپ واقعی است، نه نظری
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133268" target="_blank">📅 20:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI1ZMZG0OSmjqbMoY8VaVgDBr1mvXv8CSu5zsPTrtqJ7_HuKuAE3sdeIGriYdG0kK7KeMIbi18adWvzUzWNHiAYHjwX5vtdJB-3GiPYQjS_KUY8SsxXPevpu4KmVVCaaGjyfzDhfL9HZmT7qllcRKo_zOfKZ5QkK7d87zPWX6tqMe0QWMV4RYOVie7bPXQ1XrlmtW1WQ6lw36Yq5xBlxhvmMf4irWk6fsf2xVx3M-yqMlg-QpGB4EI_-5-xohmS7aXCzGJsHTiOyp-1QIXRA0Ii-3cIQTvaPS4HfKnYxrvNIvlOvDFJq_Jx6s8K2a7dvWRr15eJKo1LRQMaHfAqI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، به مجی هابرمن از نیویورک تایمز به خاطر کتابش با عنوان "تغییر رژیم" حمله کرد و گفت که او یک "معاینه پزشکی کامل" را با موفقیت گذرانده است و درخواست انجام یک آزمایش شناختی دیگر را داده است:
مجی هابرمن، به مدت ده سال، مطالب نادرستی درباره من منتشر کرده است. کتاب او یک شوخی است! ۹۰ درصد آن، اخبار جعلی است. او از طریق گزارش‌های نادرست خود امرار معاش کرده و باید تاوان آن را بپردازد، زمانی که دادخواست چند میلیارد دلاری ما علیه نیویورک تایمز که در حال فروپاشی است، به دادگاه می‌رسد، که امیدوارم خیلی طول نکشد.
🔴
من با انتقادهای منفی مشکلی ندارم، اگر درست باشند. اما از گزارش‌های نادرست، مانند آنچه در کتاب خسته‌کننده‌اش وجود دارد، و مانند آنچه که او در طول یازده سال گذشته انجام داده است، ناراحت می‌شوم. هدف او فقط این بود که ترامپ در انتخابات شکست بخورد، اما با این حال، من در حالی که در دفتر بیضی نشسته و فکر می‌کنم، این کار به خوبی پیش نرفته است. مجی یک بازنده است! اگر او واقعاً داستان واقعی من را می‌نوشت، در واقع بسیار خسته‌کننده می‌شد، اما پر از موفقیت.
🔴
همچنین، من به تازگی یک معاینه پزشکی کامل در مرکز والتر رید انجام دادم. من این کار را هر شش ماه یک بار انجام می‌دهم و درخواست انجام یک آزمایش شناختی دیگر را داده‌ام. من تنها رئیس‌جمهوری هستم که این کار را سه بار انجام داده‌ام و در همه آنها موفق بوده‌ام - به تمام سوالات پاسخ درست داده‌ام. تعداد کمی از افراد در واشنگتن، دی.سی. می‌توانند این کار را انجام دهند، از جمله مجی و همکارش، جاناتان سوآن. من شرط می‌بندم که آنها نمی‌توانند حتی ۵۰ درصد از سوالات را به درستی پاسخ دهند.
🔴
به هر حال، کتاب آنها را نخرید، این یک زباله است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/133267" target="_blank">📅 20:05 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
