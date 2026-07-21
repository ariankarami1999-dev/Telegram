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
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 13:46:06</div>
<hr>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پولیتیکو: دموکرات‌ها به دنبال توقف حملات آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/136334" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پزشکیان: برخی اظهارات در داخل، دستاوردهای ما در مذاکرات را کم‌اهمیت جلوه می‌دهد و نباید با اظهارنظرهای نسنجیده، زحمات ما نادیده گرفته شود.
🔴
در یادداشت تفاهم، ما بر باز شدن تنگه هرمز به روی صادرات نفت تمرکز کردیم، اما طرف مقابل این موضوع را نقض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/136333" target="_blank">📅 13:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / حمله به ارتفاعات خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/136332" target="_blank">📅 13:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته
VS.
دانش آموزی که ۰/۷۵ گرفته
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136331" target="_blank">📅 13:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0_4zQofpDfbKKDtVluutA9vXHy1Bwq2OzEligkn1mHU3XHst9Uw82nbqgwUgsVAu6N3PK2k0YMYDWpNSEiY2natRzmzx9W6cqADmhZ0qj1yR7s8SapMQfMV20GYYUa_GOZCOPu69dQxN39uTGeFOJO0K8JDzvNTdQRHaQiikHcwKG4RyR7HIGL0fDtNChJWsILAHr-yLaBbv2ExFH6VTQzE7FIZBLxZkhN_uWJKM5cRxkL3mpdKnEDjAQEBPIbGayC8ez9kdJG_bAc-sraq8jKvNxwMt3UUvjeAlARnRl5_4l06DP2lWAV8Kd2Lq5VlW98vqDThM4KlYkKCWwl3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنین مشاهده شده است که یک عملیات نظارتی و جاسوسی مستمر توسط آمریکا، که از عربستان سعودی آغاز شده، به سمت قطر در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136330" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkG6apNAVkgLfFIk25W50Sfy-8_IvVgA3p4WwppAm0I_2qWefKlNGRjmUG-i5O-CNLnQshU-oM4f0uo9bhHx2m-IQHVZCrFk1XU2PE8VpTLeTkMPfdQmZXl4akqiai02P9imH51lbH5hfcednMSBTEUUq6FIszihRrWsy7L9Vbg2RcSHftZsrEFJl7ueFozYOd_9WWTQyoI76THnAdQ3hzoReccLtaTTKeSrTxr3Z_g04IUgBHCmvyvD3jfOli9qnZA5pCosIlY5qM6t3nZP1y2M7AOQZq8neHjzyn7tNP9uiaSLCV1aGCs2SJWCta2vbXZ5E5qllRn_1vwrEWqD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد یک پهباد جاسوسی آمریکایی در آسمان قطر، در نزدیکی سواحل ایران، مورد هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136329" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/136328" target="_blank">📅 13:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / به صدا در آمدن صدای آژیر خطر در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136327" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136326" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / به صدا در آمدن صدای آژیر خطر در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136325" target="_blank">📅 13:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcPgHcD7pyW09rzoc-kjc705y9_7lNQiA6fFcmxYO98Y4rk3vU5580-soiPc90HYmzBbmSSuk8JiVPU4JfkhbjJgtJSCDulM_vfJOESr9kHRvYtr2OuiWHNiRMHK0WthLDRJhcU7-MAvYJ_hnxh7_vNHNBsqV_bDillFPs-sBIklLZat4C5_hB-saHFJKZ0FBaTj48JRPZhS2jIEf5DOtdHXpsZSLhcAZSV4Apmbcr4K8Nj1qy8c2cbWUshTJyD-CJqilWf_ghz0TyjGdIHHonQjsz5hHwn2-5JyR0qOERMJqzrdc6vI-DIl9hjjE-sK6Kqi6gaWkisdBJez36cSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeIicYDDapj2ELwKA-JOQnj8BeKKTv-HnB0PeVacVgOWZR90XWlHFKuYXilqyyaQMNw3-yUbDMi30PhMRz--__FIP9lbNuoBXCiqau2s9F0BzMm1exFqkJLHnitGwj5uhiKdpS8z1pEqpRVpKRktqhWUknxItVku8OYVCQROCtGmzm3LUTS3hwsmU9PjusvedYDquvDchtLGWFaEYn9z_iWgF0zmOyQAhiqfMirW5n5IP1otquuz5ASZIV40TDtlBmAcug1lh1YiQcQHF73kzl04ENCCpNjEW-0LJ2oEprFdZroE0hc-6wo_K_tnBfCZlrM9ocGZKm6J117U3n1AlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از شلیک موشک‌ها از ایران به سمت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136323" target="_blank">📅 13:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136322" target="_blank">📅 13:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl7gDoBat_YLxWQ_mKs5okFG1pJm5b2UaamrL1LjdaSknFJWlg4682yFIConci9isLdJKfcIMRxatg16wEU0mTnSoI4erMms4rJQIVg5Zf1YoTOxczYVOM_avPDIwd2xYPiJSDMHRG7Ey5W_BKvYuSzmvAZ-drYm4su_iawLLWFeOgUMy5qjT6j0YnByvhSea6VLgvvF22N8l85BSB8JNthBUJWqpcPKVW6_CdoacVadtiwE38uYbL9FCMSjL6mc4ZUOHc3HPf1A76rJr6KuNO6rMm_hsxHiW049S44KBW8aXD9HWXfF3K3iQgyw9ENQtdLN05XYFdEbb_FaqKq-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری صدا و سیما:
افتخار میکنم مثل امام‌خمینی، هندی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136321" target="_blank">📅 13:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وای نت عبری: مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
🔴
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136320" target="_blank">📅 13:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شلیک موشک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136319" target="_blank">📅 12:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY40uOeiWEA_zMvplK2fex0gQ2Hwta5VhGHqOwkro5pavEqt_ABPMbN2anvbSkk-ZimJoxtPl04FoYWVlTWnpaK5MybcjqtBkbFIJXuc67IImyGMj24g7RoxQejhRj0_5od4JPTKZG5CcIUU4InTPc5gOiag1ydPqt045IiJwfAs6s9CYmolxUPqQrPIXZbYWRfr7mBcw4sJx3WsfGbtCeit6OJHUz0a2dVlic-QWD9FDDZrkHLe2lmoQh_KwmDyRexQ6jEfMdX555AXJvqTRLyqvVxQ0ctGh_BuC2TXdQrgegyrT571Yjvlr0300bpATmi98k86RliPBuhNFAKpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f15b07102.mp4?token=YPZJPa72R0RLVBaukMn4YTNU1EQI9sU48dJ5Al1g8Sv-eCnQ3tTBtMx9NDdSVHh9SPDDOIajqU2H8cUL8HrorTcXXfExYjKqlTsfiT5zYOj0uEMCcW8Qp5hKLYWEOwHkGssWWQRZMBGBUKHGCGqsC3jFdEDNwSd36tF1H87MRnqZA1783iFTfB3CFoomxrBNgJl-xJu1ZW9ghYWBGDF53-_ynbbpoWaOHlSGkMpTowmdrrvT9jnwZhFdf9EjBu4ootk2Rl0ndZ-0cmYjo0Iv619lec26Skz6KbCvKbOGpa7ZpTQ591HcCgRXpi0OIB6rSoYJvoJSZRAL-KdPIBboUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f15b07102.mp4?token=YPZJPa72R0RLVBaukMn4YTNU1EQI9sU48dJ5Al1g8Sv-eCnQ3tTBtMx9NDdSVHh9SPDDOIajqU2H8cUL8HrorTcXXfExYjKqlTsfiT5zYOj0uEMCcW8Qp5hKLYWEOwHkGssWWQRZMBGBUKHGCGqsC3jFdEDNwSd36tF1H87MRnqZA1783iFTfB3CFoomxrBNgJl-xJu1ZW9ghYWBGDF53-_ynbbpoWaOHlSGkMpTowmdrrvT9jnwZhFdf9EjBu4ootk2Rl0ndZ-0cmYjo0Iv619lec26Skz6KbCvKbOGpa7ZpTQ591HcCgRXpi0OIB6rSoYJvoJSZRAL-KdPIBboUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله با استفاده از بمب‌های هدایت‌شونده روسی، مناطق مسکونی در زاپوریژیا را هدف قرار داد که در نتیجه یک نفر کشته، یک نفر مجروح شد و ساختمان‌ها و خودروها آسیب دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136317" target="_blank">📅 12:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شلیک موشک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136316" target="_blank">📅 12:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/136315" target="_blank">📅 12:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdeo7oICKVkuU20ZCwjXhRlq6_LQlrRm-vw4aA-KNExc4d61nBcWRuNwkF2LuJZODx2ytdtDtj197StiGbPnPdkMh_VRx0ZSQr8QZFDeWlLK0ysJe6msjnVFCIyWRdDtHRonYAMrdlL_k2DIG_zLBCjR7e-CbJsUXSn9o3ce4kB_gq9WQgMUUDI0SIjpqBjtgFaZFEqCap7zuzaytI-8a0K9OmGS7yU2kcCXecbU4MVQuMeEEKM9bkRPCeMTgLtf4ZjTW-RgNyKHg5M9yUTwkMflYYDNjyUIwxIo1d5qzxUUUkVBXjoe6USoYbEpZ7H5s19JUnds_zeCzSNCkEEZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه نویی ۵۰۰میلیون تومان از پاداش جام جهانی خود را به خیریه کمک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/136314" target="_blank">📅 12:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCSj9BsV37S1Yg2tlAxTp5IYiP4Fs5SPGYxjRo2CrTrfZ7T__GoCZxhYCm6gkk77O3NfbgpT6HseqcxYPYbLFyw3dzHMdFry2TPpDBkpl3RI-nc_N6aABpWOGJFEl6hIDmpDM-r0MPxO_a5nJBN2QII7oMAnf2SprtmzuzRPnheXcplylvsBpQPmds3u70jFuHcpUKQeky4WWsgw61O0VsBtw2fW8rjFFmA_haUy0-AQiIf-_3hfrI0qb-YohlI8z4h1pZ0CpUC_cYhxxNrQoVGwKOMnsvrTAQrDKg39bUYhB8WAMtqtACL2PY7lb4YSYe9gF9DW9PGeiHhif3DRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgshMk6Bq39xsL3Bfq1ujDoaCshb8A4-HCiT7NTzOaJ0Nl6sduCqNeoCKkpmG68jFB4hGvdk-QLgIB8_e56a8EH-dIfA9v72xzXZy5UolzJs0zuJWsi27ZL25lIhfAvDuHIhpl47EFWPa-NjnenAIt_ez_rsrwPnotpA0wysGjZ79RWBTEl5O7_ZLYMyBiSdOMRqaEpYs7MoJYnmEBq5-i18AA2h7tNjNCgppaVcv1hZLm134zWkDwB58bxxH-Up1tDR-C68qCHYzVTqL9F10y8SW9O2FQQWi5uhUEOJ_HNlm7GthURPg68zcPkq4DRf71C7XL7P1YzoQqZv3MIsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/todhPhB9u9x_X3irdWOAzw74LYt-ptBdbRrqfwCBh32nJ0OyQa1_4GlbF1Cos0fouuDlYa6EmYmun3jfXPhawHQqMM9hWj6xF1hhcX--wq-OjlvMCNr2D0pWvrThuO5zpdqxOPa_3UEwm3yIK6E1CEzpIrwalOouCsg4mjIDsZVC_7VLESY4Z9X_Pvsikv8EwnGFk98PLEQg45CUi8UAYJbo_Bc-FEzk8nj2W65VJSUQCcsg0GYNQAzOZhmvSjZjTM6IMhvgb-bqmj3B4Wwj45rU-fsTlOFdkARIW3F8Oyj1O_hHYTf_sCr48GnTsVV7rgWQmm5MdOCBKgQnhybvSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل، درحال تخریب ساختمون‌های جنوب لبنانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136311" target="_blank">📅 12:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
در پی حمله سگ های ولگرد، یک کودک سه ساله در سنندج جان خود را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136310" target="_blank">📅 12:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533201e41.mp4?token=GeeijKyR1Q8q6PonZohXMnnkoO2-ZsGQHgBgZZvvqBgKAP90zczenF3j2NHjde3lUKF5Qg6Uv_ZZqLMmo5GdDgIs8joeuX5Ude1dBLb1IaAG34XyNk5zeGRXoTcN7WQhZYX8SoDn7TDj_XWU2-Ubztat8myL9I1Wyh4d9c8EN6e2rTD84Pp0HYKAItD_GeaapPWrx6nWJzaKBbieU1VikbYXiVSqEWWL8GyakeS_-g5QutGe_8sCEvgOSz8Xim76oItjeFTwSJw8Zdvjjs8XLE8FnScFcqdIlq-jiFrfeZSFPJAbFHlrGCra1b6bFZB16dMzdK2NwusLvc2S1HtipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533201e41.mp4?token=GeeijKyR1Q8q6PonZohXMnnkoO2-ZsGQHgBgZZvvqBgKAP90zczenF3j2NHjde3lUKF5Qg6Uv_ZZqLMmo5GdDgIs8joeuX5Ude1dBLb1IaAG34XyNk5zeGRXoTcN7WQhZYX8SoDn7TDj_XWU2-Ubztat8myL9I1Wyh4d9c8EN6e2rTD84Pp0HYKAItD_GeaapPWrx6nWJzaKBbieU1VikbYXiVSqEWWL8GyakeS_-g5QutGe_8sCEvgOSz8Xim76oItjeFTwSJw8Zdvjjs8XLE8FnScFcqdIlq-jiFrfeZSFPJAbFHlrGCra1b6bFZB16dMzdK2NwusLvc2S1HtipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافندی اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136309" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfY1ts-Q0zyN3MoqGAhBYLXfT4etTFz5WdXon-8BcJ4iQpbYtlQRxYgHfANvzT1FbhXaejmfIlYpNPWCGvdktbhGVivAn7iPd9_Tfxy6KHvs0q8J7uqJsSjhKR67jDbtfWJZFFVqr24ziy0hB3vNmAopVp-eqgfwcU9V8bEbV6uMN66k0AnzFnMx3k93eYqyXigL5vuUY7JuUNF0PWaSKRG6CMullF82UZYRIEwmD1I3BNu2zUbERdAw9QncK4WbDV0Ii_pn_Z7e2D2k4XcXfPc3TrAywpYVb3luPwi1CiubyluS6xl2b6yx7Qb7Wav9-2o0TQe7ajFn2JGZvxyz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه WSJ : اطلاعات اسرائیل تخمین می‌زند که پس از عملیات طلوع شیران(جنگ 12 روزه) ایران هزاران سانتریفیوژ باقی‌مانده را به تونل‌های عمیق در داخل کوه کلنگ بالا، یک مجموعه هسته‌ای مخفی واقع در 80 تا 100 متری زیر زمین، منتقل کرده است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136308" target="_blank">📅 12:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSoiu6zvQ3Rdf1p9WIohi4HGWhzCL22dtJ1oygpZ1QqY7GPZvWyy0InhR6nYigg67tGjNPX9nPMB0HYbNa9KdwREdAzbojrU1yXGom4ACwZ-cWzk0pw5azH0nvEMvbohpONipzIlsj0QI6_9IeP7sGd2aWAEb-N_AVn8LFpHIOHVVfVtTg5wkwzIxFW5t_1j49UKyvqcyZSbMHmXhXgoHnVtaCZUxxTbHShofkW9Y00TaG8QTPRaVQaPD142el5svrAAyvgBdi6vHFqN78lMo2D4v4NLVhNf_moBF5Y0ycQ3aICGNYCDQ76jv50cB5Y5ITn6FLo6RMepE7d4oZt83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور وزیر نیرو و عضو ستاد علم و فناوری شورای عالی انقلاب فرهنگی: مادرم را به دلیل بی‌حجابی به فروشگاه وزارت دفاع راه ندادند. من هم به معاون وزیر دفاع زنگ زدم و شستمش، او هم گفت بیایید تا حضوری از شما عذرخواهی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136306" target="_blank">📅 12:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
الحدث: آغاز دیدار وزیر کشور ایران با عاصم منیر، فرمانده ارتش پاکستان در اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136305" target="_blank">📅 12:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قلعه نویی قبل و بعد واریز صدها میلیارد پول نقد به حسابش به عنوان پاداش
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136304" target="_blank">📅 12:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE1aeqKTsGktAIdqjMhkuAE-mfc1RhHtphzYtpAgcC72b2kwxPhSv78qRq68v4CwgoU7pyuBwiOdlYDtrXwYypl5L0r_jjl0maosTL3WKaV89ES8HMxTkgeeGZE5LOeoR7cDo60I12RLy-9t0s6xn3hmeWClYrZ1iGmp7K--4dthB2RMUUhAug4Nie-lk4Qln7P7rrbdKMo1o1asCY5n4m2eQIrUc1aKqQZFHgP5STft3bnNdH3-E15rU1Z7pQld6coD_ABktX64EIwzB15mmseCCQRhGrvDtVmfVIGqGAfAoxGtVu31T9WOcRa3JOVn91OJTMBemzoQOlbU84twVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
یه مشت وطن فروش بی شرف مخالف ما هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136303" target="_blank">📅 12:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سس گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136302" target="_blank">📅 12:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136301" target="_blank">📅 12:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔔
تبلیغات قفل ربات الونیوز
هفتگی 250$
میزان جذب: حدود 30k
سفارش دایرکت</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136300" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بنیامین نتانیاهو، یک جلسه امنیتی طولانی‌مدت که بیش از پنج و نیم ساعت به طول انجامید، برگزار کرد تا درباره افزایش تنش‌ها در منطقه گفتگو شود.
🔴
این جلسه حدود ساعت ۱:۳۰ بامداد به پایان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/136299" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136298" target="_blank">📅 12:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال استریت ژورنال: از زمان آغاز درگیری‌ها با ایران در ماه فوریه، حداقل 18 سرباز آمریکایی در جریان عملیات‌های نظامی این کشور جان خود را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136297" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
صدای آژیر در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136296" target="_blank">📅 12:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awaL8DonAucwvr1bhZAZoVJgqdZNlOTNqQB20p0DZcTZrN58ZWXHoc9d5r-rQfNPFE6bN5NSp99lPGIBxJ-wQj8fgOaAbvKrL-yhueQ1YBpDxzFAzFESGFPjbD_TCRT7lf_ydMPb604_oj-4qwN34Wv_r7lcIdBySr1Fe-yRsJ8k7LqVeLvEeirWtWkaV2YzsrnD0OMkSd_7O6WDNxkCavxjx5lyafTC_SB5zoKzru8TLdCDJ2yZpJCUcTqflbUqV5_akT89Ap8ZrFE-vULLuxufnil61a2DvzDS02lJbDLdK70JKgqhq2-UVoxDVkcsJeLTpza13HZqIrzicl7ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ شلیک موشک از سنقر کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/136295" target="_blank">📅 12:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت بهداشت: مرگ ۵ نفر در ایران بر اثر تب کریمه کنگو طی سال گذشته؛ ۴۹ تن هم مبتلا شدند
🔴
بیشترین موارد ابتلا در فصل گرم
🔴
از مهم‌ترین راه‌های انتقال این بیماری، تماس با خون و ترشحات حیوان، به ویژه هنگام ذبح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136294" target="_blank">📅 12:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بیانیه مشترک اتحادیه کشورهای جنوب شرق آسیا: شروع مجدد درگیری‌ها بین ایران و آمریکا بر تجارت، انرژی و امنیت غذایی در منطقه تأثیر خواهد گذاشت
🔴
ما نگران هستیم که تنش‌ها، فرصت‌های دستیابی به راه‌حلی صلح‌آمیز از طریق دیپلماسی را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136293" target="_blank">📅 11:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت دفاع اردن: ۵ فروند پهپاد که از ایران شلیک شده بود را رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136292" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
معاون امور زنان و خانواده رئیس‌جمهور: به هیچ عنوان موضوع موتورسواری زنان، حرام ذاتی نیست
🔴
نمونه اولیه گواهینامه موتورسواری زنان چاپ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136291" target="_blank">📅 11:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de1e4db8c.mp4?token=FmSwe_N36gSuUc8mRjYFwUu5OMbO0s60b9a9H05tSI8mdIb3iZDugvrKZ-XNAusn-OsAKDIRNBZ5KXr3OdxSDKZ3DanbIANYB2BeiUuYQcF8X9xtBqu1ZsbfeSKevuqWBCuwSWsN8Gn5COKJrsBYQjg85QwBaQo-bv1Oyz6l208554TGOSBkwGkSIPRJilO-5wj0dnPQL29fYL2JkRsPElzfyRAlAiy6eH63GYvBu_m3VCHPBXSnrz480ZsPVLViT-sqmUrChkw46E62yUi4im71Q54r6Y7sHEpP3X6ZgRVO4cDuvrehPnwTxG1wjE9ibKzcoeQBHRmBVghTdzePkLVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de1e4db8c.mp4?token=FmSwe_N36gSuUc8mRjYFwUu5OMbO0s60b9a9H05tSI8mdIb3iZDugvrKZ-XNAusn-OsAKDIRNBZ5KXr3OdxSDKZ3DanbIANYB2BeiUuYQcF8X9xtBqu1ZsbfeSKevuqWBCuwSWsN8Gn5COKJrsBYQjg85QwBaQo-bv1Oyz6l208554TGOSBkwGkSIPRJilO-5wj0dnPQL29fYL2JkRsPElzfyRAlAiy6eH63GYvBu_m3VCHPBXSnrz480ZsPVLViT-sqmUrChkw46E62yUi4im71Q54r6Y7sHEpP3X6ZgRVO4cDuvrehPnwTxG1wjE9ibKzcoeQBHRmBVghTdzePkLVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد موسی غنی نژاد:
زمان شاه وضع مردم خوب بود اما امثال شریعتی مردم رو فریب دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136290" target="_blank">📅 11:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouf2NGbJxn3JzdzEKbfUSLLYijRiYsHkh_0a5UJdLYEVKdaeaLo_jDvrHSkxA2KnjPfdSK0JIua61LgnPAIp2B44sBXpZH7qD5NiBE3vk8rB_R8IdlR0WNrPVYGiZg4b1CNBw28f1vinOps58ncOXrUg-Rv1rNARQJnwRURCZvE28wyvNk5fTVdWb19T7YXcKeXe5-opycg7NQBjqUuYkunJi8EWqgENycTyZBHqwokFx0dcZrRtbTtNpTKOJb9kd3rSLX4Ir5kgYeePC61OGk_B9qmRVmanPD89DlR3TS1Bz1_hatpborFKwiE-P7CQtYE5FwK8vyn-HkX5VB2CRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور وزیر نیرو و عضو ستاد علم و فناوری شورای عالی انقلاب فرهنگی: مادرم را به دلیل بی‌حجابی به فروشگاه وزارت دفاع راه ندادند. من هم به معاون وزیر دفاع زنگ زدم و شستمش، او هم گفت بیایید تا حضوری از شما عذرخواهی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136289" target="_blank">📅 11:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر مالی اسرائیل، اسموتریچ: اسرائیل هیچ انگیزه‌ای برای مشارکت در درگیری محدود بین ایران و ایالات متحده ندارد؛ وضعیت فعلی، بهترین شرایط ممکن برای ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136288" target="_blank">📅 11:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فرمانده نیروهای دفاع ساحلی یمن: تصمیم ممنوعیت کشتیرانی برای دشمن سعودی بلافاصله از بعد از ظهر دوشنبه به اجرا درآمد.
🔴
ما از توانایی رزمی دریایی برای اجرای این تصمیم و جلوگیری از عبور کشتی‌های عربستان از دریاهای سرخ و عرب برخورداریم مثل همان کاری که با اسرائیل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136287" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk9RN0O7e8529p9NF7gKn5-qfmzahbWSZ9rZWxaKImnBflJETpgsJO0s00Bx7VA1UEt7Q2JQBhvflZL1A4faG0SzT2z-yViVMcwrJXkP5q6JqV81XYY-cIoBEJACfR7rZBCKBLMLyd9wKCFb0gjkO7uWsyJ0ermx6p4W7wMscmVRELxsn-M3PXN4QGjR2Zij0FT8XTfNECKpa-FPKtfR_kGp4QeXdkzZWUnhFhjhzRkryVyNl8dTlHVtMaJUaQEThLCdjuThaAxC-Yx-2TNaI_tJo7P8EAXTzFQ24VGMLpDKYxNAEwjJZtGOGqHtEedh4DYfftKtnn9IeEr4LxGVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور کریس مورفی با بازنشر یک خبر از واشنگتن‌پست: بسیار نگران‌کننده است. یک مقام ناشناس دولت امروز گفت: «ما به دلیل کمبود موجودی و خسارات ناشی از نبرد، سامانه‌های پدافند هوایی و مهمات دوربرد کافی در اختیار نداریم تا بتوانیم با اطمینان به عملیات ادامه دهیم، و فکر نمی‌کنم کاخ سفید از این موضوع آگاه باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136286" target="_blank">📅 11:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مدیرکل درمان ستاد مبارزه با مواد مخدر: اگه از عطاری‌ها، مواد مخدر بگیریم، پلمپ و دستگیر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136285" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759573b975.mp4?token=ZeEtpPlk-3iVYiFTMWrj97vOPmu_c0ewrdjWZg-YHKYHhkkliCXkQctm-2O-ZnwWmWXGyZCJ8gPPb38-DYQ72nQGxubKh2ywdWQu6F06Zw5OcNEtY_y9csEZ9yy7NlWRZcB24-Kvnyo19GQa81j9ShZmTl4h5S4MXeStR9h4GCXFDdrxR5YPwvl92CNlxsIpXBIO0w6phrI4xXMSVdn9DJ9sxaui8uXASyZklZLiEJdxejSkWHvbkqyAkR1sALkOgCx7obw06pI4Iyh9lkQ7QzIyMV8o-eBhhnq6LkBZjvGj1UATO0Psy0bR60oqkuin9zhuzJl0T6-DoUZ8tgQMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759573b975.mp4?token=ZeEtpPlk-3iVYiFTMWrj97vOPmu_c0ewrdjWZg-YHKYHhkkliCXkQctm-2O-ZnwWmWXGyZCJ8gPPb38-DYQ72nQGxubKh2ywdWQu6F06Zw5OcNEtY_y9csEZ9yy7NlWRZcB24-Kvnyo19GQa81j9ShZmTl4h5S4MXeStR9h4GCXFDdrxR5YPwvl92CNlxsIpXBIO0w6phrI4xXMSVdn9DJ9sxaui8uXASyZklZLiEJdxejSkWHvbkqyAkR1sALkOgCx7obw06pI4Iyh9lkQ7QzIyMV8o-eBhhnq6LkBZjvGj1UATO0Psy0bR60oqkuin9zhuzJl0T6-DoUZ8tgQMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازنشر به مناسبت کصشرگویی‌های مجدد عوستاد ک..چشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136284" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
خوش چشم ، کارشناس صداوسیما:
توئیت قالیباف مذاکره‌طلبی است؛ مثل فیلم Inception به او تلقین شده است
🔴
ببینید این جمله را چه کسی به شما پیشنهاد داده؛ پیگیری کنید! به شما تلقین شده است!
🔴
فیلم Inception لئوناردو دیکاپریو را ببین؛  قالیباف الان خودش یک پا وزارت خارجه است؛ مجلس است؛ چین است؛ همه چیز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136283" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کیهان: جنگ آمریکا با ایران و اختلافات دو کشور هرگز با مذاکره حل نمی‌شود.
🔴
یکی از دو طرف باید از اصول خود بگذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136282" target="_blank">📅 11:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / یک کشتی در نزدیکی سواحل امارات هدف قرار گرفت
🔴
این کشتی مورد اصابت یک پرتابه نامشخص قرار گرفته و سیستم ناوبری آن دچار آسیب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136281" target="_blank">📅 11:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpK1xapOcaXLXYjrTfk72P9qTdagHKiRiXx7ogzc3E5Oml5L1yDw9XhZDGLzLli907CgWMRZPJoeqHwbkPlxNAI04luK1QEwJfmtyZtF9RlJ5_EnzJofX8QOk4sGBN0c6IenFe9P7JdTS66Fro66JZ_UpmjbCe9t1tO7TFavOR9x5Dk-ClQdqfmkFVfBiJYvNpZRhrRoah50MOTHBv80ob69_qOqOyeihCerkIKfpNLDwGpfT_GlbjhdnGprv-72LsQHHgVIbFL1BsCnTG_q76EPXbD4Wg_gkGxIrGYLdHdr5e0TG3WpxWfZmmsoV2joRV6c0Sq4S5vlEGvf9pVTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
بیرانوند بزودی استاد دانشگاه تهران میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136280" target="_blank">📅 11:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saF2H5RSkRAmPKdh8ldnXNRuPy2aTgijIdWwtJzmcVoYK1KsGLXU4TIz9AnVU8rh4Ho3Qqdh6LmPC8Hh0VBcVxyEeokbsOQYkdVVM9CTKiXt3oizRhhvY7aTM61d-XeOc1L3TrAIOCxG6bi1JktHDc6z5P2iVCCfQ6b8PLuMWW2iPTmerff2KJAGHbshiEN5Ug_9e6fjowQ86IbmOBSb3XRNp-FzZqxSa-2e71qsiI8gOTAJSeWaT5Msl6uO_h6FKoZXQMb_cFLRNoSzyphzzyAyQ6oQ2OIzq2qdmspEfz_QPiAiwc_a45TO2m_87XDGjSCThzaRq7kMPzihES0yYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مغزهای کوچک زنگ زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136279" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قالیباف در نامه‌ای به پزشکیان برگزاری جلسات علنی در شرایط اضطرار را ابلاغ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136278" target="_blank">📅 10:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZCKxnhQ6IONYCCeOrdmxLgd1NsVWtt4hjLLC2dHKYdc3X7A2OsqpoZKHXj2EM7zwstbdAmzNNkWg0GMPYepdEydfEw2qIokRp2ysrBAlWcAIw1qs8EwX_IxqdwsvbNbFLX-L-A2JegpPV-VSXpyTjgPm8Gr_NbbibRt_kmjlaBL4Iya_3KFcw0MoY7iIccmHCZArMhQxsL5be-O-SZP7oIrU2VF4u715h3poUWewz2xZ84B7d5KqW9z_gaejyNXQEvBmG2qSn6eefMeWasLFTTrk0C_DXDibV3PvUsx7SUN266lahRzH_rU0aR0wv1QvRJXYCuWwurpnQ4CjKhFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده!!
🔴
بلومبرگ گزارش داد، در بحبوحه بحران تنگه هرمز، عراق برای انتقال فرآورده‌های نفتی از طریق سوریه به سایر کشورها، از ناوگان بزرگی متشکل از کامیون‌های تانکردار استفاده می‌کند؛ زمان تحویل محموله‎ها به بنادر مدیترانه‌ای سوریه می‌تواند تا چهار روز طول بکشد.
🔴
به گزارش این رسانه آمریکایی، تنها در عرض چند ماه، سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136277" target="_blank">📅 10:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCwVxa0DE3MU0KQgqFNDBkI5Vf77gcS75bcsfNPdgDvWUzw4xbtTcDPmnDdRm4wmK-i50_xyNaVlQNwQjFqC_mBDXbp3RRgU17b_z_YCHJn8yrXs6t7tQLdoz9TFytfYGX4OozsHMm-niFmo2gtKRUbecSiShku7NlZ5Iof6SD-uc9HCO6EfAJn_o48MRd-nwB1smklZUohk9EZ_oLvApLSZOe0Y9sZWJ0N5WBhZyG1EkTZlqC9W3RMuPhCcSsuJSDLQhd622fyAXcWk2uWBnNJDnGhxiNzMKlMKZmG6QX-AeztYQT3G8nyl6rWz9ZB0PJne_ans8H4b2SeH3dxLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شاباک، عدام ابراهیم شعبان نسمان، رئیس بخش عملیات تیپ غزه در سازمان حماس، که در حملات ۷ اکتبر نقش داشت را کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136276" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سوخت‌رسان آمریکایی سیگنال اضطراری ارسال کرد
🔴
هواپیمای سوخت‌رسان آمریکایی متعلق به پایگاه هوایی الظفره در امارات، هنگام پرواز بر فراز خلیج فارس، سیگنال اضطراری ۷۷۰۰ ارسال کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136275" target="_blank">📅 10:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McgoGh_JqnnRuy3sGeAl7qQN7GRMbbPq6nOZVkF6ltybAjqk_q7vnfOHR7mcWws7ONEBdTCUNZEOsxfHtU3WP5zCrHzyVCgv9ULRbLStF5yRs-lxR4aZsPuE5JB4Samvs4BJ2WWXa1eiBK1qxr9PLe6AiFLL64JAmrYLAs7tZjMVUVI4qtEZR7OvP91P0FHhBsSpzXEoD1wyn9FXGFzoK-cixp53eD-Mp5PAZAkX-hy2pmk6nBDewanGDlfVEZrq2n5tNCEtE_vptnfRNkUMJ3eOfnw3GLAdPvPJCWczDCgaJxyQM3vqtdiEz2g7lP9ETam_zjrLaGNnId8WM5NQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی‌ساقی:
هرچقدر پاداش به تیم ملی بدن، کمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136274" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نیروگاه برق الزور کویت هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136273" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfEnMtLGt6ajsXFB4bvFPvGojvTm1A1vvO_QoS1NVYWvjgeg8WcBbYLLsKVk14_ys8_8MJkzu5EAg9diU1msrSb8eUsGONJajUGA1N16ON4NMdpZkx_ztZ2HrCVr5wtfraZOUKjh-F7eocAd458Sat1FchW4d2vFRAb40LRxOTXEhm8s22shTvlz8hoF-2gYTi5tSWybg_MAEcwzWakouW5L64b_R_HlKK-dg3zvttfu23w-lFdwqRGvTF6TEE2_C1WLknIR7LwOmDBmucyG-mt7WhcDj4fElT2G0c8vbmd-YAlPK1HatyM7mIClqlGmGoHgHBrcmdbEzCadN-AX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شایعه حمله زمینی پیش دستانه ایران به کویت و این ویدیو از انتقال تجهیزات زرهی که وایرال شده، قدیمی و مربوط به یک مانور نظامی در ایران حدود ۲ سال قبل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136272" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی منتشر شده از طرف سنتکام از حملات شب گذشته آمریکا بر علیه ایران ، در این حملات از اف۳۵ و اف۱۸ سوپرهورنت استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136271" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCmdkTdodss2F0gFff55d4xzn8VYEcu_8R7PvWMNIvSls2DvZy9H38Ck2jczSGOJrbhZZwRolTw7REeqMy80z6-ex-MGEwbEGbzuhWcJ20CyePIRy3I7qYh1EkmZZQ6ANU-KTn6mCbRET5odcFREd2edIQpkBM8eCjZ16rwCIJoLnVhID7wezCtGdn_ffzHd5DGWTjUcpB3yaP2xsTWu6fcaFTRozrJtU3ptjj3kGw37j-BKHLjhZtWGvYlCWxRkXR4tJSofnoTtXd7B0C21CReEzUmMIjLPV8O-W6WKy5YplhPCDoy1IryWpqJiwolDpl81C4F5k_eAJj1JbsG1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnxBpNrdANTm6-j9pNOjg6LWeE1VykNm9E_upHXSo6IKRTNAnSnhIqmyYp5iv52jz8qYjd8OyuF1eR96h3YM8mBn9oK6SprP-2WoCmeu3sG-JtK2GGs3kylAXAhmAO0roeWedFHy7KBjMK_NhyWha58lP_wd_ziwn00XqsTATuh9SMSrP_g7UZG94UYIKFRjAoIvWvS9Hpq5meLW0sv-YPFj1k53MIAOvQD1ZydY6nLqR2PLTA4TViQOXVqsaC2CCuQjDyH_9X4WDdKmZmM-slCHOKX30giLQ-ExX7GoAsmJjxuAANX1RojOfhu5uKBz_DZh2Sh_mDLUJZv6o3vnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMPemEbx3vC0BhahTX9ZeC_8YQEtzF6vKsr2VhzMjzGe0u2S16aCAwrQtA-z1rM5I0tfr70IglyOlbfErpsKUajuPhU3VBzTV-4hwPkGMemo0knMNBLNFJSlFfXbSAsgU2PO7EigE4i18zOJuX2FkEc3VLuFhmL0yfa1HaKV1vNlNbajU657oWWfqD7wb7vrsM1SMQf-MAF_Qj6c9lzLIcThinPWWOSeI1GeZUUTyifHvLCcntRrYglXkkC7PNvCdAZi4qSd2-SSY-oloD5xQvp9fMyiGlz9gjMCNKNghTZFUdGmXcwsS3uBn1tEyzb-u16tTta_tlA5bA2U9UEKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JECgLxtxg7mO4Vs5IZQp4KZV17GkGdfyNdQCGfWTMyj9QQzznRX_psuleIMOakwgRcE7e-IC3ZPr5oBa1wH2LYpDaylek_iYgaKZg5DLEdl4x29lJAPmhr5Ll9ba0nN898_YVqe8XaRevwZYaJYO1fDVN8urR553c4nI1ACfp-uHHafQHgK8mm_6SaW5nK0Ipu_xYKhuE--KaLR8_24RhmWMNyQJA9wyeiyTdG0HcWP4QvY6ldw-U0gr77gTPJqQ97jKN4X8KnAYeOPugf_-GaupYkvyrEcRIrh8Eb2YiusXQ5ub8pCj1LMUrrjpB6i7BJh5o520Vh1kTH2ngR1Ftg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هدفمند اسرائیل به غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136267" target="_blank">📅 10:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkB_I3yDVHnyofVxQUyMKFizzzMjl5gbo_OVXReS7Xw1qU4kpukwkauyv4fZphbhYdDsUdRYmxF7HcrfHYfu1FlnyD0YY6Pm0lBDabxwEkQ66AKZJz0kfHFVfLHY_OVEGRb-bVvX1aF1g9oaaT3No9wCl6E8ZO3fCVwTUt6-BUfHUFyO_3-J-fQNw1oztAnm5bl6dQiQS97zeWg4dQOvSt9NPYPZMQ2BGBpbnqN1lj1xgh5iPl5hZ7TC187NVvF34TDFTcJW68k0MEUhJ3rnXwSAGgx-IfP5F4R6Jq3yAHQIMk3h1VRKgeUSWm4WE3Mls4ZTSys_HL4YNDfXZmUcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله موشکی اوکراین به یک کارخانه در لیپتسک روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136266" target="_blank">📅 10:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=exkpn7VKRIegoQAyKRt2ovz9lni-GwKP1GEOlhpEz3QyeSAnswaVag-0C8RqUItz7lAmF-OX6pnOsSvTgw8xEWOP5HW-86GC97zZqFfIZilcwcGEI5Rzmi3uLtczJcUKY8eEjxKtNFFw1AbtZ7Rh9F7BLOVPY9spBUdj8I_jgywJ2mtmK6MzEsbZOLJLt7Q24E5A2v3OZZg15c3xuMufRHkWerQsmmvirQGg1W0nmp3yuVpb0PTaHF7y7w2zoRrrwS0_S5ygrTFNOK2dofXl5-4PdZqbrUD50BWg2L4xcYWri8EfxcfMAS4Tl8BRWRpf7L177O7cdvdmFznmfG1M8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=exkpn7VKRIegoQAyKRt2ovz9lni-GwKP1GEOlhpEz3QyeSAnswaVag-0C8RqUItz7lAmF-OX6pnOsSvTgw8xEWOP5HW-86GC97zZqFfIZilcwcGEI5Rzmi3uLtczJcUKY8eEjxKtNFFw1AbtZ7Rh9F7BLOVPY9spBUdj8I_jgywJ2mtmK6MzEsbZOLJLt7Q24E5A2v3OZZg15c3xuMufRHkWerQsmmvirQGg1W0nmp3yuVpb0PTaHF7y7w2zoRrrwS0_S5ygrTFNOK2dofXl5-4PdZqbrUD50BWg2L4xcYWri8EfxcfMAS4Tl8BRWRpf7L177O7cdvdmFznmfG1M8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در پی اجرای بخشی از توافق با دولت لبنان، از روستای زوطر غربی عقب‌نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136265" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگهٔ هرمز همچنان مسدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136264" target="_blank">📅 09:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سپاه: یک رادار هشدار اولیه، یک سامانه رادار دفاع موشکی، یک رادار FPS۱۱۷، یک سامانه پدافندی پاتریوت و سامانه ارتباط ماهواره‌ای مربوط به پدافند هوایی متعلق به ارتش آمریکا را در پایگاه احمد الجابر کویت هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136263" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سپاه: تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش آمریکا در منطقه‌ی الرُکبان اردن کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136262" target="_blank">📅 09:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد؛ اما ترامپ و اسرائیل به دنبال یک جنگ تمام عیار علیه ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136261" target="_blank">📅 09:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1n2iGcJ9Mmt_-5NUlVM9dE2sSsgpZfDf0gmyQFQx0YkFsOySZ3eZO2HjNN6rlJecF1x-SmWucUiiS7yApHNUscmdkiJptiwKOjboajYTuY-GBUIFw2mHV5xkquWV4Ya2yTYMFhjPW4RSwfB5dOJWaVdC7nmdkBT3aMbnS-mPOk9mTMbi_9ybLDQ35Y6qKx589_oE_D9yof1OUhd1ElAGUO5EmQjMCueL8TtwzqQcMFhgiVJ45XodyubvWa22Eq6XQlARlETg0kAR22fKB2hVOBqvfxrvLcy_9fvJ52-K3zSJDKllyYtCqa1-PNoruDEGqVOgvtsp7mr-8zwIj8WEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل آبزرور: یک نفتکش صبح امروز هنگام عبور از تنگه هرمز، در حدود ۸ مایل دریایی شمال‌شرق لیمه در عمان، هدف حمله سپاه پاسداران قرار گرفت
🔴
این شناور نفتکش M/T KAIFAN متعلق به شرکت نفتکش کویت (KOTC) معرفی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136260" target="_blank">📅 09:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مسئول آمریکایی: اگر ترامپ تصمیم به گسترش جنگ بگیرد، این حملات شامل تهران و تاسیسات هسته‌ای خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136259" target="_blank">📅 09:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سپاه : زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136258" target="_blank">📅 09:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=jCt-t8euglX2OycMDVxfvPoMSPfWEHy8dcRxhyg3Y6UoWe88dBMe6mBsla2btwUjrtGys9EPmkZUxFBaRABdfiXN5K_IudRDKWaZruJk7BYY9Hq55rww3HrkCVmM5LUnksDcalqTSD6iuh0N2ebNqVhC4irb3LWAy3jfrAz8M4Lr6kyzV2ozwVoQftHxLq6AQLQZPmEdff1UDRvlRNQi5l3iKyRfemXq-lq6apAFdtwY2reCDPfDeKk0d5Lb9tXXYxcMZzJ4H-zxc-YX1iYn0PUuH1Y7fDwt1CctuXb0lqnp48XmZ_T2eBCEkXt0NyDu3bK0atozIumM2m00cDC6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=jCt-t8euglX2OycMDVxfvPoMSPfWEHy8dcRxhyg3Y6UoWe88dBMe6mBsla2btwUjrtGys9EPmkZUxFBaRABdfiXN5K_IudRDKWaZruJk7BYY9Hq55rww3HrkCVmM5LUnksDcalqTSD6iuh0N2ebNqVhC4irb3LWAy3jfrAz8M4Lr6kyzV2ozwVoQftHxLq6AQLQZPmEdff1UDRvlRNQi5l3iKyRfemXq-lq6apAFdtwY2reCDPfDeKk0d5Lb9tXXYxcMZzJ4H-zxc-YX1iYn0PUuH1Y7fDwt1CctuXb0lqnp48XmZ_T2eBCEkXt0NyDu3bK0atozIumM2m00cDC6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: به حملات علیه ایران ادامه می‌دهیم
🔴
کریس رایت، در مصاحبه با شبکه «اِی‌بی‌سی» : واشنگتن می‌خواهد با یک توافق صلح‌آمیز به درگیری با ایران پایان دهد، این امر مستلزم همکاری دو طرف است.
🔴
«کاری که ما اکنون انجام می‌دهیم، تضمین جریان نفت، گاز و سایر محصولات از طریق تنگه هرمز، با یا بدون همکاری ایران است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136257" target="_blank">📅 09:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=Es8yq3e-4qqyIHT9Fd39xPucmSwxCMwVoJPlt5M3n9R-snr-ye_P8ulVS8-9_Zdl2bdNl51z2qnZVd8sI-YM0z_87r4S4Bu9GDcKYSUAED7DCBwZz6VtGdJRHIce25_60EkcaLzO5l7t0Y_XyP5HSatSax5qhpU8v9WWVR0YPX5N85yBOttG4CWoSYnFqRSFRKX0kDdq9Rdz_SLp5srKlTpayAoqsxf9fzHz9eTGPhZzTW5HRouIs-YjW9eSUthgYYGE62dTAp3iRnoQHXyjUpAh8YO_zY-_t23fdWKpiKdSBtGNTMmvIeibfty34RHVFSm0CWlTcu4HOVrEA7jpoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=Es8yq3e-4qqyIHT9Fd39xPucmSwxCMwVoJPlt5M3n9R-snr-ye_P8ulVS8-9_Zdl2bdNl51z2qnZVd8sI-YM0z_87r4S4Bu9GDcKYSUAED7DCBwZz6VtGdJRHIce25_60EkcaLzO5l7t0Y_XyP5HSatSax5qhpU8v9WWVR0YPX5N85yBOttG4CWoSYnFqRSFRKX0kDdq9Rdz_SLp5srKlTpayAoqsxf9fzHz9eTGPhZzTW5HRouIs-YjW9eSUthgYYGE62dTAp3iRnoQHXyjUpAh8YO_zY-_t23fdWKpiKdSBtGNTMmvIeibfty34RHVFSm0CWlTcu4HOVrEA7jpoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر جدید انگلیس: می‌خواهم به کارتن‌خوابی در کشور پایان دهم
🔴
ما به اندازۀ کافی خوب نبوده‌ایم و باید تغییرات اساسی در رویکردهای سیاسی و اقتصادی ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136256" target="_blank">📅 09:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136255" target="_blank">📅 09:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccsirRUUrIDMycMFvPzOPHTQ1JG93DkVrj_guYda4zt2rRuhyxkkfpfnio0d_jPmkbk3OjYNMocJ6FXQmiioL-SL-7W_JtOD3hC3buCoT660Al76W_VkIAoylbug4xUl6if8bUGwbEfnxeAXFKD3l8OtIRFh5VHomGdMLcG1cZHM3AT5pbMDGvWsQMgEOE9U281tuVYVxrAepIkgHyuIGFjv2jzHV6yQgXb1iTYSr0_bnJDb1YNxs_m5Dv9T2ceDSrpKYgqmWyfllSBbzNmGO1JkruyWy5tXBB76OO3ALLS1numWo15M6qH_109NQrHB783mhpmHi2M6SJe5_x-Dfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر نفت استراتژیک آمریکا به کمترین میزان در ۴۵ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136254" target="_blank">📅 08:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کلید اولیه سوالات آزمون کارشناسی ارشد ۱۴۰۵ دانشگاه‌ها و موسسات آموزش عالی فردا بر روی سایت سازمان سنجش آموزش کشور قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136253" target="_blank">📅 08:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn5GgzUdpPaPYy5ZDtujFDmyiySunkVHUgjE_MLRkiWpG2NpgZnsSHq6QzmSoeHFPo4IEPxUZ-SrO3Fwji9ysHgFXqonJApDgDQOycsfjT62ysDwzSwFxdJGVXYuB33aY6B5koOCW5FuB6i24bQCw0Jup6tj-HGFfZsdW6ceGMk910OKOdU9sNSh8NB57rQEtAOBX9OH5FjFJYSOHD30OROZmdsHuP6NGYXLP908orgpGPPkDIJiBvGyzI14Z6IOPcrO85aIe-aGMKolUUHRqkxERnofGv6MY62npcIoviJaLPiRTOF5umcSPwJlO8ATZxQjwNRYQ-jJyJxakH7CX-s8" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn5GgzUdpPaPYy5ZDtujFDmyiySunkVHUgjE_MLRkiWpG2NpgZnsSHq6QzmSoeHFPo4IEPxUZ-SrO3Fwji9ysHgFXqonJApDgDQOycsfjT62ysDwzSwFxdJGVXYuB33aY6B5koOCW5FuB6i24bQCw0Jup6tj-HGFfZsdW6ceGMk910OKOdU9sNSh8NB57rQEtAOBX9OH5FjFJYSOHD30OROZmdsHuP6NGYXLP908orgpGPPkDIJiBvGyzI14Z6IOPcrO85aIe-aGMKolUUHRqkxERnofGv6MY62npcIoviJaLPiRTOF5umcSPwJlO8ATZxQjwNRYQ-jJyJxakH7CX-s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله لفظی خوش چشم به عراقچی:
عراقچی تحلیل‌ راننده تاکسی‌های خط ولنجک - بهشت‌زهرا ارائه می دهد!
🔴
می‌ترسم این تحلیل‌ها از طریق حفره‌های امنیتی به عراقچی القا شده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136252" target="_blank">📅 08:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=APtT5GgSZFLIuLB-05o2tfdYYmRRgbZ2qG1qR2X_zweD3vP3-LHM45PngfvxGl0ghwZNHb_xQzAoHDIWoHJ8TQ0EHsep2pvL3VL5DYz_FBHxHSNAnIQALFLAnohmspkf81eUwHTSs1p1lrHdLn3QBGj2j-EmcBIeX061C514Rzz9Zpnq2mWs3TsT76p087sb58HzsQ-f6tcgqdrkOSYHlmUq54R2tp20pqmHV6orkWbOjqL1QaTQx2C8WZA7BkC49aK3_8x5_atGb7W8iht5L_T5LY7j3yAX29gs7SE9V6YsjW1IYw334AhSjQyXtQ6ubhmm6d90EzAI_556C96oDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=APtT5GgSZFLIuLB-05o2tfdYYmRRgbZ2qG1qR2X_zweD3vP3-LHM45PngfvxGl0ghwZNHb_xQzAoHDIWoHJ8TQ0EHsep2pvL3VL5DYz_FBHxHSNAnIQALFLAnohmspkf81eUwHTSs1p1lrHdLn3QBGj2j-EmcBIeX061C514Rzz9Zpnq2mWs3TsT76p087sb58HzsQ-f6tcgqdrkOSYHlmUq54R2tp20pqmHV6orkWbOjqL1QaTQx2C8WZA7BkC49aK3_8x5_atGb7W8iht5L_T5LY7j3yAX29gs7SE9V6YsjW1IYw334AhSjQyXtQ6ubhmm6d90EzAI_556C96oDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارلوس خیمنز، نماینده کنگره آمریکا:
شاید چیزی که ایرانی‌ها را پای میز مذاکره بیاورد این باشد که بالاخره بخشی از خاک آنها را بگیریم و بگوییم اینجا دیگر خاک ایران نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/136251" target="_blank">📅 08:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روزنامه انگلسی گاردین: جنگ آمریکا و ایران نگرانی از کمبود گاز در زمستان را افزایش می‌دهد.
🔴
اروپا برای تأمین ذخایر گاز پیش از فرا رسیدن زمستان با فشارهای فزاینده‌ای روبه‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/136250" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpZLD1sTm5zpy5KFPinz4CKYtuR8gG3xx723PTx-CzSjcCsOvw-5twqJnrCQMoW7VfMrVzX3SPIL1Asn3vsRmWFoP8j6jP3hM564Ynn_2thHkNGqQlly2cAuNdc0gKN0VmLxQXo2QevtYLnx8G6If6eneA2onVvWx9iTBoH-9xraRbExHuZ1Q2Dt9mcmUSzRlUij7H_WC9i43pfU9IzVZl12BwON18vadvUqwYX_M4bT5riVJyXG7-0_df3lJLMCbTVVzSfD_XMigAkhl6Feel9kH15QrixExiv46irteUxGQ8JNk-2vlFSPOC-MbzCEYBvG2sSPGEkfus6EBss6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت شونه تخم‌مرغ یه‌شبه ۸۰ هزار تومن رفت بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/136249" target="_blank">📅 08:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نقاطی که امشب مورد حمله ارتش آمریکا قرار گرفته‌اند:
بندرعباس
جزیره قشم
سیریک
بندر لنگه
بوشهر
چابهار
کنارک
شیراز
کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/136248" target="_blank">📅 03:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb2c07bcf4.mp4?token=WYQvRrr8XWlI3TBfWM7cBEZOyZSVTvAmyhGwPFugTSDXzyp13L9h-uSfQZFjZUlsDVnsylroL58Yu3DKCFXYx0uZJcNzZCzGEDq7pUjj-vq2zMqLbaW5zejKsCTP59JBe4J9nR15O3AbxZB6yeKh7olbckJwTqKGmNWtISvvqDdK2N0M_SMINyZU8REPbTp1Samv6GsNJPkM8CK0hbDy6xGsCpbVNVMheGSLbn9kDkFyujCnBTzuA2cneU-drrkchgk6jVjyjzzaP45gPRRRKKGZ5nq8qdbjDtvQ_T6hszzA3-HtF_4U9UIV-Ri4Ljdpt0IZGF4wQLHr1WKSeiefLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb2c07bcf4.mp4?token=WYQvRrr8XWlI3TBfWM7cBEZOyZSVTvAmyhGwPFugTSDXzyp13L9h-uSfQZFjZUlsDVnsylroL58Yu3DKCFXYx0uZJcNzZCzGEDq7pUjj-vq2zMqLbaW5zejKsCTP59JBe4J9nR15O3AbxZB6yeKh7olbckJwTqKGmNWtISvvqDdK2N0M_SMINyZU8REPbTp1Samv6GsNJPkM8CK0hbDy6xGsCpbVNVMheGSLbn9kDkFyujCnBTzuA2cneU-drrkchgk6jVjyjzzaP45gPRRRKKGZ5nq8qdbjDtvQ_T6hszzA3-HtF_4U9UIV-Ri4Ljdpt0IZGF4wQLHr1WKSeiefLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فردوسی‌پور:
ما اینجا نوید و محمد رو داریم که خیلی مسلط دارن اجرا میکنن.
🔴
جاودانی:
خداروشکر بهشون صندلی دادی و قدرشناس هستن (تیکه به میثاقی)
🔴
فردوسی‌پور:
نه بابا اینا قطعا آدم حسابی هستن (تیکه به میثاقی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136247" target="_blank">📅 03:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از مقام‌های آمریکایی:
اگر ترامپ تصمیم بگیرد دامنه جنگ علیه ایران را به‌طور قابل توجهی گسترش دهد، احتمالاً اسرائیل نیز در این عملیات مشارکت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/136246" target="_blank">📅 02:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
چهار انفجار تو نزدیکی پایگاه شهید باهنر تو (کرمان) شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/136245" target="_blank">📅 02:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/136244" target="_blank">📅 02:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gkf4BbBiXzRIJi0wEqcTNJD7RjwNiR_LgYKDTeCG-vOA16ZPOQ63-5mbyXSHHhK8jSE-L0lNacZn9M2IsH_CaxkEmk6RI_WBD_MFfxtOvpT5OEyqohHrDMYbxgKmn6EcS6NtHipdHm3JIZ0b5Y3Qm-nmqOnSolM7MtqXrl3HJjXwFN4yyWMj44w6YYDE4vxGqlMSfh-B39dW26H_GnzTQ1IS7NH7TUCc6kdQ_ZJujs6Hw4vR4FamGYsDWccQqc8zEs9h0BIC51o2p8KUWD_gSM3N-KMER1VvN5pYJgpMCoDUjyguejA11ABOm5UWipaOeNMe0el0PffCaM8vVJX0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماد شرافت در فوتبال ایران
به افتخار عادل
❤️
بزارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/136243" target="_blank">📅 02:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4766344fdb.mp4?token=YsGfFePMy41r_nykWemW_iCH2oqQadG7vxMb1RHvA-KgWKMAJ8QYE5jAPGdH6OJShV2hdH-IlT9b-cmagYk4KgOA3e0oSj4uRXJheKlzNcRImwpC3nW-yO8c8PBwaPys4U2Pz7TlghxfqriHHaqjHFLyd23rAr_6nHlJ8nx2CTBeelqcpBpy9W3Hnbh6E4IFDkbWbKcW-Kspmj1JqOAx53NFK1SczclAQMxlV3pfRR0Zb9exuT3Yb10WUQgDRVG-bMpUwLxL6j8Ke_DRDJmWeH-smI7lbCYmLzJxGHFnAUKzKvgvC9--uges1xUEyBjhhQ8GAMIfVPhv1JBNEAzUwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4766344fdb.mp4?token=YsGfFePMy41r_nykWemW_iCH2oqQadG7vxMb1RHvA-KgWKMAJ8QYE5jAPGdH6OJShV2hdH-IlT9b-cmagYk4KgOA3e0oSj4uRXJheKlzNcRImwpC3nW-yO8c8PBwaPys4U2Pz7TlghxfqriHHaqjHFLyd23rAr_6nHlJ8nx2CTBeelqcpBpy9W3Hnbh6E4IFDkbWbKcW-Kspmj1JqOAx53NFK1SczclAQMxlV3pfRR0Zb9exuT3Yb10WUQgDRVG-bMpUwLxL6j8Ke_DRDJmWeH-smI7lbCYmLzJxGHFnAUKzKvgvC9--uges1xUEyBjhhQ8GAMIfVPhv1JBNEAzUwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه‌نویی:
پاداش یعنی پرداخت به موقع؛ پاداش من رو هنوز کامل ندادن که، فعلا 70 میلیارد تومنش رو دادن.
🔴
این پاداش بابت صعود به جام جهانیه که خودمون به دست آوردیم، پس چرا ایتالیا و امارات صعود نکردن؟
🔴
قرارداد من با تیم ملی 30 میلیارد تومنه اگه تو لیگ بودم زیر 90 تا نمیگرفتم.
🔴
تازه پاداش من ریالی بوده و بَده الان از خودگذشتگی کردم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/136242" target="_blank">📅 02:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
موج دوم حملات شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/136241" target="_blank">📅 02:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0s9BpuxqsnL6oOQ7boW1okeqAtiPv7rhaAELR5JQ6NggRGV51lqMCxzKeewMi7o3scYSCOLaSk934aImh553O0nV4_bm3y0B9NAx3JoJ7eumJOuunC0rQW6PoFjsQIPsqjUkbL_47vJwcAzR1cOQPFGGc_RhY9N-vm_kKxgSvKZmsw9j2vmQIhLC-zD4QDvXmkNFTVaMVpLMTyNPlILHtiK-ws9065OuyXRt7HiQz5zUl-2FEZXepusvM1dPj7qV8n-dE2kTKLSkz8UYhxbJd2ic1kpbcGJOp1KR6zt5o2pQIW5zCvc8IEGPd1U1sk1ttg32gbRinMpAsp8S5sueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه هوایی بندرعباس توسط آمریکا هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/136240" target="_blank">📅 01:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/136239" target="_blank">📅 01:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQViYOL_613sI_NAnCoPUIzRro2ZMNSke5OgREgv05M8qb1nDn9TOOqMucZuS1ZqtEvXsiCFPQIGQ6bwwCY8h029hF-dIqJ-O9SbRW0hleRYq0RgUJ9GoD7E_RzpkFgL6H-WaC-LM87FJy_8UUXoVHv7pX27CzmZHcma6aW_eXb3lIgioYAXg_zP6DGKpo3gl7LRLBbVJWLLGSqhX5I2ffs5VOG0Z16H6fUgOADaTWdVgsz-Trm3AeHnCT1hCdL-6A01szT2Fjmo9_8jQSPy_0ThSjMAR8_Iqd-miNId871i8JkccpSE32YojqR1mVsvqKoG3gRYhKpspLst1iB0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌ها از حمله به یک کشتی در تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/136238" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzZ8z7O1nqd21M10atrFQD6yP0nT4Hk3BXtAddMCCenFYCThdhRcIinotaOplY4piNVoTyCnpZjbRr-VpgPblaK19HPm1f1k1xnDuNUHdnkeoVMiiCD2_o95uzeJsrBW8v3xwN-oprVdmWDrB4n-sQUH5lN26QBe-eYMUP4XT_v5XzOJPcwo_I2uWBmep8Gr4gNz5ct0l5u72QNMQpruSu9uj2pY3ssyLQS2VTL3hHYwoeMZ0UtUltIyUSnbGJAa7p2NKK5qPtnif6e4iKukof5Fh6IQqwBztePaUdjLwLHPhih3YMYPsvGGl3Lm76D8xNSYf1qN82rph3jT9XitLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی تو کشتی میزنی و اون زیر ساختت میزنه
🤝
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/136237" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بغض عادل از صحبت‌های حاج‌رضایی
جایگاه اجتماعی با پول خریدنی نیست / در آخر، تن شریف باقی می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/136236" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHhJwoYFvIte4udln17jf9m6DTW8IpM9Sgtvh2ntSh715CGe6GavV7yIjxA2mDvflQ7D4r83imsh6mBH3AkBrgygpZnisOwSb6nnA4Zj2MVVRqZwQLXMwMHlKpJ0xVCCDbnQI4GKjNPlrPeSJlMM6l5adSIER1AwTqOXzlK9ANv45QEDeRmPtHnWEr3mFPQlOBauNxUK7uwD6LZXgkgEv75WO7DG608YYP5tc6dcki1uYRObYv-ptjRpOo78cjVrxrwvDHFQUkIzFLP0BpDoEgx_q20sVDZBp3OdjRq8jC3obuyxEIVA3HRS6SIomug-ftIAjeOMRlREFNYN_ZzfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عادل امشب از این ظلم اشک ریخت
💔
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/136235" target="_blank">📅 01:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e13a6e02e.mp4?token=O-fyKzVaQpAtqRa0kNrce97pUbDbpi91WE6uuWBCZi3AyhNYOFofd-L6f2xlUUJmylqXxwb2mb1t44e9n_13HmdKB7rlE9A1MrPMc0FXVSmBR0WjQnehJvm8hWWFuoEXPPWT-5zGIEOOfGbvPx8yAllUu8WSUxC0YVZAm4hIQoXsQTQ7eNp2Ro3N_vdD2DUSgCnANW7HjmQk-0rVbR76rVJ7WgL_BtLBv6iGl5zOqE-39mACBIE4whbEXVVT2v3EVSsZWmwWDTxQPH7l1E7mjHT1HSMpuOnz9w0j8ctN8mgA6toQG4M7VuMsp_9LFklBgZJEHlpQRWiOlfaKh47i3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e13a6e02e.mp4?token=O-fyKzVaQpAtqRa0kNrce97pUbDbpi91WE6uuWBCZi3AyhNYOFofd-L6f2xlUUJmylqXxwb2mb1t44e9n_13HmdKB7rlE9A1MrPMc0FXVSmBR0WjQnehJvm8hWWFuoEXPPWT-5zGIEOOfGbvPx8yAllUu8WSUxC0YVZAm4hIQoXsQTQ7eNp2Ro3N_vdD2DUSgCnANW7HjmQk-0rVbR76rVJ7WgL_BtLBv6iGl5zOqE-39mACBIE4whbEXVVT2v3EVSsZWmwWDTxQPH7l1E7mjHT1HSMpuOnz9w0j8ctN8mgA6toQG4M7VuMsp_9LFklBgZJEHlpQRWiOlfaKh47i3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی‌پور:
من بله قربان‌گو نبودم ، نمیشم و نخواهم شد؛ اصلا بیاید من رو بگیرید ببرید ولی من جلوی شماها سر خم نمیکنم.
🔴
همه پلتفرم‌ها و برنامه‌ها n میلیون تومن پول میدن مهمون میارن، به همه مقدسات قسم مهمون‌های من همگی با یه تلفنِ من میان، علی دایی و کریم باقری با یه زنگ میان این افتخارِ منه.
🔴
خودتون میگید کارآفرینی کنید بعد من کلی آدم از دانشگاه شریف و اینور اونور آوردم اینجا داریم کار می‌کنیم بعد اینجوری رفتار میکنید؟ دیگه نمیدونم چی بگم...
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/136234" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.  وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/136233" target="_blank">📅 01:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxsNkxeTLqMfymLvwPGtmxm0xVpoWhHRb-N-Nhuko3av27w_YpLv4gXGKWBBKuvXGD1bG575g39sajnAfBDGcpLEmEaKJqzxa5xefQT1jUAp9ozH2fUmi64bJa3M0RXrHHHXHhAaM13M2iei5h_OPPVX-rlJYjI7VRj0onjgz35W5s-6QuEQiuflvRAupTw7COUMBVKqQVUjNaXrzIc1t2DVK9cK2-FAVXSa-q8KX5rKA2H8c98z1NSBfv0I_bT2soeL-3uBOf2UQtQSLGbkDJI9xRKw4es39TWFdyxLJ88gRs0jciRB1xQ7dWwOeLXOs6dQ2L_x05W1vuakp3b6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی در شبکه ۳:
140میلیارد تومن پاداش گرفتم، مبلغی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/136232" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/136231" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUS9_CGUvB8hybJDgTCS6TcvGuYlSal5QA6dpjxmxshp_gT8l7JjGxUEbnt937HQMb-Al3wrXJ3PtYDhM08ya8AEBAs1k4D4Tz1Ka7CaibDzILFflu61gAgyIoWdf5mlHUX2oBPbi8OAy_Rqort1p8_QqEuFhNzoMxi0bpwHTtcVKnjpmChSxRIxWpKyunwmuO0TRe2iQQAxoP7Vzwi4e2fVqQKK97-FWLGji_MyzpimYezzGcNjRawFyRi8grNQ1-rOe_sedgP-cL4goDeSzj2isgCgJxQs_AK9Ocm_UKSCk717ddILm8mThyDCU--s5JLgHEPESsZEXLrJEB6l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/136230" target="_blank">📅 01:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REjuYxE4-oquvkpA6N-dM-zGOSQoSD6RBB1-lrrNuitY4x408rm9TIs-glRYnaT8fvrBA1vEN1NnpL6SD3aSDFDRou4PedJmJS8YLNcragpPh9umLviGANYTlMEmJVfMFtHdm4lm-y04aSXtx7klSNjxPmM_OuOm5i5NyxvZEVlF8-NzYgLH0DraKZMMnbUA5s1Qt-dgI8WA5R2YYKTmnyDaz4krwThJJqVUJ9VDTK_gCmY1RUQJGuYjhExm4oTNdGzcmGRfbRtq6plurfaRabiWFRnqPQIhT872YrNxl52CyZRSHmOiA_gszoiz0mrQaYrgHbugVH0_7mtHbh0lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید ترامپ و عکس اینفانتینو
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/136229" target="_blank">📅 01:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5ZryoWHg3fxcwcTJXpjyIudIRqBx8Q0HfIFfYdZkXZjTCkzEA2o93iJbzP6v7ypLVS4fAKFtEIUpMBNKAgFxcUYq-wHfDByxfJt6-rNU5D2M3N5sse4RL8ln-ofxWpzbwG5PqRP9aA5u6g0lwS6Kvs18lQStTVcXwI0p1CmjzGe4ne0R6RY-n-3ltHytc10ZvWimAc-F_2wceunkXfvSCZv8XR97cqZVrEpBi-rbCceBzJXPuC9pYpLlDz_vscDgTclMjJfzI8hgMubREiEzeXRS8Wys4_9B4zXNq6ZKRdJAFlwNukGJiamMPNliEeGIKvNrqvvqZ95I0GCBtq0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیراز کوه دراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/136228" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی : من خودم رو مقصد نهایی نمی‌دونم
🔴
فقط پلی هستم تا مردم به انتخاب نهایی برسند
🔴
نه طرفدار سلطنت هستم، نه جمهوری
🔴
وظیفه‌م اینه که شرایط یه گفت‌وگوی سالم فراهم بشه و آخرش مردم خودشون تصمیم بگیرن چه نظامی می‌خوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/136227" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
