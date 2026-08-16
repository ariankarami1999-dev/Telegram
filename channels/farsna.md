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
<img src="https://cdn4.telesco.pe/file/YkssjLsohcaiuxRnMx7DgNxDXE3FwmI9iaKr7ynqethkbPbFLRsocxJBbtBx0uldu_HPbCyiMZP45Id3C725ZHkvBSqHAi83yAxSzrirZfMI_gRJ8KVbyfUp25kp9ueTWKm13AxtQ6Yr8xVdKo-cymz_VF-lkn6wUnP9v9gfQTrCeR15CVhGiDF65LNvIlDI4IanPwEZfTF6lL1jZvF7EStjKzPuQU5nbExG6hxsj49mXNxuzGZjRDcTKexN5kpEo8J5oUv74a9uFpRRkW5h8iU6nOxnizOOLHL0lSj7G-X24j1YMhWRd-IA8YxuGKquURJ9SwVU7Jh2Wgy7hzQhbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 10:37:02</div>
<hr>

<div class="tg-post" id="msg-456347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت ۴۵ روز برای معرفی وزرای اطلاعات و دفاع فرصت دارد
🔹
سخنگوی هیئت‌رئیسه مجلس: با دریافت اجازه از رهبر انقلاب، دولت از ۲۹ مرداد به‌مدت یک‌ونیم ماه فرصت دارد وزرای پیشنهادی اطلاعات و دفاع را به مجلس معرفی کند.
🔹
ایدۀ حذف شرط اجتهاد برای وزیر اطلاعات مطرح شده؛ تغییری که به‌دلیل مغایرت با قانون فعلی، نیازمند اصلاح قانون خواهد بود.
🔹
قرار است دولت برای این موضوع لایحه‌ای به مجلس ارائه کند.
@Farsna</div>
<div class="tg-footer">👁️ 659 · <a href="https://t.me/farsna/456347" target="_blank">📅 10:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سردار باقرزاده: ۳ خلبان ایرانی توسط قطر به اسارت درآمده‌اند
🔹
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح: ۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
🔹
«جواد صالحی»، «عبدالمجید دشتیان»…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farsna/456346" target="_blank">📅 10:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e832dd9f5.mp4?token=B4zhXrxkmj3VqyspHcoC6uyVmuo5uZouC-MZ3K_IT2hPHhVGiFJBvti3LWIbZKPj8sg2q62gGVJRPdBHl59o9UP-Y7_N7OgPJz9gU65He1oifTKNYW_bI8RC0qnnoKKZpGOg2Y-2hj1giOZ0Gcnl0cXu4OxkkUBspwH5zQdSxuURE2YCrZ1bXVs3q3L53XX080qWgJT9Twv3gbb58bj8EsYaW_R_70dJbMWUE2NlIcUydxFOZ0CQ_9BqO6wHGFlEvehVVxcn-Y_ekUjhthTUcmAr4F43arpzZxZUoM6LhZ4lYnOQY2jeZIJ43lneCebbgXeMV-u61qYJsSWDKAFFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e832dd9f5.mp4?token=B4zhXrxkmj3VqyspHcoC6uyVmuo5uZouC-MZ3K_IT2hPHhVGiFJBvti3LWIbZKPj8sg2q62gGVJRPdBHl59o9UP-Y7_N7OgPJz9gU65He1oifTKNYW_bI8RC0qnnoKKZpGOg2Y-2hj1giOZ0Gcnl0cXu4OxkkUBspwH5zQdSxuURE2YCrZ1bXVs3q3L53XX080qWgJT9Twv3gbb58bj8EsYaW_R_70dJbMWUE2NlIcUydxFOZ0CQ_9BqO6wHGFlEvehVVxcn-Y_ekUjhthTUcmAr4F43arpzZxZUoM6LhZ4lYnOQY2jeZIJ43lneCebbgXeMV-u61qYJsSWDKAFFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ تراستی‌ها به داخل کشور رسید
🔹
تراستی‌های نفتی در روزهای اخیر به‌صورت جداگانه در شِبه‌رسانه‌های داخلی فعال شده‌اند.
🔹
اقدامات رسانه‌ای تراستی‌ها پس‌از آن آغاز شد که رئیس سازمان بازرسی، از عزم دستگاه قضا برای برخورد با تراستی‌های متخلف خبر داد و گفت که «۵۹…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farsna/456345" target="_blank">📅 10:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3373fb4d8d.mp4?token=B2sIbzG3Lhhre6ZEvnmIo-ZqWGhm4Ruj_mt0oWGjUCMlg3OrGSJmp75-DV3y-OXC9nlZGM5V0iukIT1orkElZK0j6eqlvthD41dX2EK-2mXPj3jxjPb-z3CeRSO-nD4L9WTST3pF1_roFQ_6_J04aOBNT69oFwK1v4kEbPx0OU1Y_Bfo2CP7T2Vy_Ua_HdqDcrX8hLmfLoF_GBUu8EkHACZjuY7YAwuMLO_jTRN8GvhZ0T3ydiUSBbAQ0ltdRi1Bnp8LQlyUqKqnnrxnT2-norRSV3rgnhzeiyjlAk8faNUuzAQ7kAOcHE8lZtIJPr4bLkJ39IcQpojV5dXDEGVvzrA3S38Uqj22hF2bhHVOiFvhx1Or02RSdvmLKN9ixSv7sDJb80PutR6OdQ4n59jlfscZ6gBFFn0AcoovLuzHd7NBSq3v2CCmcJJbFG8np1TIlH3je6igXzVos6bGygh7PtjD-nPXbDKB6n9NbBkB3XCIQgZrCmsFhoVgoM7wz5FVVwMHkelEBYHmrTVa4n0DrunQLqcJqwqJ4raCvESeKP07mat_qdmq3mrenOgRr3O1oBqfjwFvHg-SzyR7ve16CWBdfCQGb7rEpHj7xKDJpGzl1nEZJMrHtbeBsAKMPKJASIE4tr4UH4JZmcx_nsr2FkSQhan5tRjJ6WY_c_igJgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3373fb4d8d.mp4?token=B2sIbzG3Lhhre6ZEvnmIo-ZqWGhm4Ruj_mt0oWGjUCMlg3OrGSJmp75-DV3y-OXC9nlZGM5V0iukIT1orkElZK0j6eqlvthD41dX2EK-2mXPj3jxjPb-z3CeRSO-nD4L9WTST3pF1_roFQ_6_J04aOBNT69oFwK1v4kEbPx0OU1Y_Bfo2CP7T2Vy_Ua_HdqDcrX8hLmfLoF_GBUu8EkHACZjuY7YAwuMLO_jTRN8GvhZ0T3ydiUSBbAQ0ltdRi1Bnp8LQlyUqKqnnrxnT2-norRSV3rgnhzeiyjlAk8faNUuzAQ7kAOcHE8lZtIJPr4bLkJ39IcQpojV5dXDEGVvzrA3S38Uqj22hF2bhHVOiFvhx1Or02RSdvmLKN9ixSv7sDJb80PutR6OdQ4n59jlfscZ6gBFFn0AcoovLuzHd7NBSq3v2CCmcJJbFG8np1TIlH3je6igXzVos6bGygh7PtjD-nPXbDKB6n9NbBkB3XCIQgZrCmsFhoVgoM7wz5FVVwMHkelEBYHmrTVa4n0DrunQLqcJqwqJ4raCvESeKP07mat_qdmq3mrenOgRr3O1oBqfjwFvHg-SzyR7ve16CWBdfCQGb7rEpHj7xKDJpGzl1nEZJMrHtbeBsAKMPKJASIE4tr4UH4JZmcx_nsr2FkSQhan5tRjJ6WY_c_igJgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه رود ارس در امتداد جادهٔ مرزی جلفا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/farsna/456344" target="_blank">📅 10:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g27On2mcpKY9cyQjkCEE3DfVRuesbiJoGvSRzFbPQoAuleZFUZYOROokj76ngjN7sQTQn1mCTYL3_aITAoXMCBiNN3wRdU7F06-HC6RbSyqH6NBeg78S9C_L6q8FsSbK18ZshPTcZMPu9LlEQMcDqjq3OcK6t9mUeWCV-2UxJqUZl2VIijN7F9W5i9Am2dlbKo5v6DYB3GzoQk2R1n-f5BGJNb2f3pLC1yH_C4K4cFOUGm94NzpR20fBkvRr61i5kr8_tgN6Df_Uh9jQ4fp3KVn8_iS83GXVCkcDCMzLK6kWsIKZd6NzPM3RbUOJ86aQZINGv4q6_7klecGEaEJQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت چهلّم «آقای شهید ایران» در تهران، قم و مشهد
🔹
دفتر رهبر انقلاب: همزمان با ایام چهلمین روز تشییع تاریخی و تدفین پیکر مطهر آقای شهید ایران، مراسم بزرگداشت آن رهبر عظیم‌الشأن و خانوادۀ ایشان از سوی حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای در تهران، قم و مشهد برگزار می‌شود.
🔹
تهران: سه‌شنبه ۲۷ مرداد، از ساعت ۱۷ تا ۱۹، در شبستان مصلای امام خمینی(ره)
🔹
قم: چهارشنبه ۲۸ مرداد، بعد از نماز مغرب و عشاء، در حرم حضرت فاطمه معصومه (س).
🔹
مشهد: پنجشنبه ۲۹ مرداد، بعد از نماز مغرب و عشاء، در حرم مطهر رضوی.
@Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/456343" target="_blank">📅 10:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9GcQfnMo92Vy0kJkRrVIrOOml--trMCEU2JlPILWxVh_RbKY0JNV6ftKNLUGK3mUl_66QYZl4ekhe80Xthie2WO-MscvkldE14FD0dGCZqwU9Fpd1LwdNY8KkCgrukL0tGITQmEUmGgiDkXHvi3hHbsx1d12osn_Qu6hjVEPDnj5Bf4qy3TUW392YXnTGIaRqY7tlmtieAyHOfeja4vQgkZmpLKFlLVtg70FzUzaj6OmOPjS1dlX07EDAooOQ4e7IkaKXUY8IJi9_WkEwmBd0GVptrcGQfjaYOJkHlxYOMQFpGRBb68WcHpp2mA5AvtLPI1hQrETQsWjJVOjG4F-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گازِ صرفه‌جویی‌شده حالا قابل معامله است
🔹
وزارت نفت از صدور نخستین «گواهی صرفه‌جویی گاز» به ارزش ۵ میلیون مترمکعب برای یک پروژه بهینه‌سازی در استان یزد خبر داده است؛ گواهی‌ای که پس از تأیید میزان صرفه‌جویی، قابلیت معامله در بازار را دارد.
🔹
به‌گفتهٔ وزیر نفت، این سازوکار می‌تواند صرفه‌جویی را از یک اقدام صرفاً مدیریتی به یک دارایی اقتصادی تبدیل کند و پای بخش خصوصی را به پروژه‌های کاهش مصرف باز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/456342" target="_blank">📅 10:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIwhR6s4Dn8AxCqmVeMg8z_C-JU-y3A4tX7clugWudZFKJwNeIuJyRfi5ghnnGaanDE3w2JrptxGaMVNlLwEjJ5oqLsuKzAiQeKwRVDGYNzS6Qe7rdj0jKTT1JV4VsBAe8AjiGrWkxeau4RVsvh-EUk28rjuNYFFNHxnps1u8o664Ns25OIEqm1WNKSEqSTe3JszbsWLxL978qind6HOTJUoxFwc9ugAjc7SsewNWMvO_oph4FGrP4QYfGbiXhvT8l835Uh4vGFGHrQQOpfVnoHtzvEdntPE_Y3oT8TKV8V1YagLOaf9f8Cr8ICpveBgaLhbG-Odq9Lmdnf2sMk6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxXFCrcTtuwT-nBIXHzMKMPvK2c8n4Bb0t6sxnGdzrsKGJxdjTSt7VMuvIHkBM-w8deXZl7fxVqUWG_-X9XhRo-g-HSTLrjod3mQYgxl4VPT0MChABaIhHA6Avf2HqIDrv1nBRnPzW1-xBkDaqs3jvPjBZJAevlcxstwcUa4Ry2FVkyKYFb-kvTOZlLw5CjSdljAAyzmHddI5692bRr8NkJ1SNnTFJS4y23O-sF3Mmg4LP4xmCgxyNxd_ru8sKPR_gfp-TiwqyJhHyPXwlfe1uOey3XnlxQbv4vkZtOkgT_cR9GjUs78cxpp3S_x-l07NoQYHVGtJOFXlMhea1enXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxNh7Eui6PZEc2xgnbQzhYjsR6M4VfS8cRuQIJ3_ADpAgCWUBAGwzzb5D97rdWHEYD6BKZcjYg4N0rBpYuF7UamnvbsUktbT8-qNmSv8G1vj-rjYVE3kI2-lrv6KfeHjZwvxWYWSVQ6l3mmQWQelreBX5dXhzqXQYqbgrCIA01oMbrM2OJh6bnEP45KTETwDzPAMMA5cfHCBZmIEu3mPfsxLIuncsldUSdPtklNQBRfYESAR8e-rywVyY8PCNapgKsSWcHZklCXSMXujs4bc0F7svWars-oxM91NEiuWVxwbK5a2AJZp2zYgqTgKGtMKAQ-6929qUUSzNImn3cBz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCMZFbjI5SKHR6i92s7_ka9VQe3YlxnF_H823RH0plQSCdKgiMKa9kbIjBQO_2KNgW0CSg7AQbwB3cnILucnjNdThDDSZcwnTFj8wIZ9e1DTU5K2KS400Nf6RFAqlNmcqq7cxo1TNpxrQYxjvavQVR-TNl-1k218gw8DWT76E9-_XvMx3owdejgy2VVVVTLAmqYHnUEOgGpwTT6BMAEJKsSg2V5LLkXT0P8ZbOMCS5203HV9st9T3XB1_519_maSR_XhwC_N2B7j8zFQuNPW-Coocpqknms9H8zRZbO58MN6JIKnba6ftEKF8SFKAS6tztUtMRUOnxys5PDcaxI-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwZFCxog3LhFgEIlGW1ge5DoZetuhm-iXAk_0yzZetjpx8PJcOQzSd7ZtwkuBB9fa_9059xisot8zrULJDiTP8ay9OJMi3dn1H1NmDztojouqEl74TwblBIIc-IX4C_yqrumzUJKR11xy4yAU3U2uDfsKehkFP4rsBHNn8ZDNB9J4btwJUf-afCNnPz7Cmm5QUdow44U7sPCWs4INrWpWqTWZraObsiqb7Hond8eTvZgnW8XGkfMlKB-Ne23HyCZALEUZLKY__YVx2OpqX5lBSZ3L1YVRCvL9JX7wfeOcRx_kKB9KJob8eaOSwUolnL5xTofXuw7A1Bb_RmfJX47OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsxyGWUmUF9dght9E8yQYpOYgwZMCCbHQPmLWq9hRqrqaMzN6DTQidumqwbgwQ3G1VboIShayvDsjwX4BAj-mTlHbTRnCi_aci-kbC3tL1_3-DdqQYDD3wHanId7zpqMsRQRHw7u4Gn2R3aecYD9UAtj7gvfLpq18COaH0gTPYbuA6ueno9gY-5OCY41lmEGMKMbNcWjfkJqZ5pMdSgO1DzB4t9q8h1DM_PVS2CFjZ3dzJg33GLhauiNKONsFjhnA5t3MtVFoo3ePKHlZiCh-v2q5da8Bqgyx_TZvIpcMB7IfoyBWEHCacX8ewyIvupjYqgGfV2kYFNtCuISK0XnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMJQ-kfo8PVyTPK36-J35s4urWXtndSMFJewdF9adiEaOTxjNKaXyhuaHJqg49uExw4gH4445sW38A33A0B4QcWHS3zNYkT369oS8xdda1nEKrs0AT2u6kelM0T2AHEwA5_qc4JXCObsuHAZaUkSYqoR9-oXf2TrNoy-9IIq5vfQPkMSn_m_aiWuPGRbC-bj4SipeNmTj0Yx394bti493-ekgeiC0uixjFFZuV4qAElZl3mF9yki-ooYZbQxgB6Rh4X0f3Bnt7-tD9qyRM5aR2BWKnDPBEdh77cgyowsVtyQGNvVN1Wb2d8oIVlhKwIFEa0tGzhu_Ke08XKizCbzIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تعویض پرچم گنبد حرم امام رضا (ع) بعد از ۶٣ روز @Farsna</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/456335" target="_blank">📅 09:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902855335a.mp4?token=uyOyII0bOL_E44pGPBJuinqssf41MMT4jRLoZVoY6KWy9_rVL55YjrxgwvtzkWxj9WX7QaKmmbn9R4eMIQV71Nv7tTCKkh-zOnycgUkI88-27C6XxEO2GJ785QcoSGhpxpDv29MOZGvZxOCCg-V_Xz0MfO7cA80WiccmFS_5S8Go6xeAP9s-PEcef34S298mpUoLH4RHByqFVwTJK9PfObSdvBbqYlUoxyPWxTHCWX_l8wnHhLUEHWowtY5jNoPoBqE36uLSDVr_PehdxXGkoKRHRUjUCD7eO256BJFwtaud-4gA4HIM3CLNjPM_rpA1rOWhncG7KkvwoXxsbwsYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902855335a.mp4?token=uyOyII0bOL_E44pGPBJuinqssf41MMT4jRLoZVoY6KWy9_rVL55YjrxgwvtzkWxj9WX7QaKmmbn9R4eMIQV71Nv7tTCKkh-zOnycgUkI88-27C6XxEO2GJ785QcoSGhpxpDv29MOZGvZxOCCg-V_Xz0MfO7cA80WiccmFS_5S8Go6xeAP9s-PEcef34S298mpUoLH4RHByqFVwTJK9PfObSdvBbqYlUoxyPWxTHCWX_l8wnHhLUEHWowtY5jNoPoBqE36uLSDVr_PehdxXGkoKRHRUjUCD7eO256BJFwtaud-4gA4HIM3CLNjPM_rpA1rOWhncG7KkvwoXxsbwsYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیویورک‌تایمز: جهنم در ناو لینکلن از روز اول جنگ شروع شد
🔹
نیویورک‌تایمز گزارش کرد: کابوس ناو هواپیمابر آبراهام لینکلن از همان ساعات نخست جنگ با ایران آغاز شد؛ زمانی که موشک‌ها و پهپادهای ایرانی پایگاه بحرین را ویران کردند و با آن، ستون فقرات لجستیکی ناوهای…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/456334" target="_blank">📅 09:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=Ia6bJZ0HHecTOSxaOSJAjIlur6fASImsGwD7FOWpr73laom3Zolls3b0nztrlZmkITe4z-49TRyEg3IYJtboIZN_pNrIkMP3L-9da-k2odAAwPuU0hY50Jgc-yFnW1ToulHbuw4F3vytHVBVXhtJ-xPDZQnpVBttfMdQKGnxMRcBiNW7l2pXX-LyYFN9ajASHQd-g8Phf3B6GSXZLX5dkkBJTIoen8K00t9mcPrj0NJFkDSnVA3TcLSKfsm-xqpC_44aHKLdO8YPJ6bNynmVF98jJSIdah0AQaktPz_FIBhlZ2b4F62PxGU6GwPtUh1xIdu6fg-0RmAkzR5vPkBHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=Ia6bJZ0HHecTOSxaOSJAjIlur6fASImsGwD7FOWpr73laom3Zolls3b0nztrlZmkITe4z-49TRyEg3IYJtboIZN_pNrIkMP3L-9da-k2odAAwPuU0hY50Jgc-yFnW1ToulHbuw4F3vytHVBVXhtJ-xPDZQnpVBttfMdQKGnxMRcBiNW7l2pXX-LyYFN9ajASHQd-g8Phf3B6GSXZLX5dkkBJTIoen8K00t9mcPrj0NJFkDSnVA3TcLSKfsm-xqpC_44aHKLdO8YPJ6bNynmVF98jJSIdah0AQaktPz_FIBhlZ2b4F62PxGU6GwPtUh1xIdu6fg-0RmAkzR5vPkBHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض پرچم گنبد حرم امام رضا (ع) بعد از ۶٣ روز
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/456333" target="_blank">📅 08:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2a636165.mp4?token=vEbcWCCEowS43FxhHMyZoQRZKzh3iYb3z2JN4tCQr2TKqZDs9sy1bSEU8mM0zfJlKn956JefX__oaLojaWOoc1nB1syPhZtKlDuTJhZ2OZMMJdIEelkNj9vZ8R80AX2dkmP9iL7vjurp2sdV11NC5HSM2GIMaSRcWXEvSEUKbQ3QpMqStX_uL_0DdxES5GCQ1t7DiWeoOmX-Rj7UvTCKOtDpNDe21I5XPF4jd8JbDmwHpYUK6jml3dr590ezjP_8BA5hVmjr_o9p0aqppikSl4eEFMPlcoyXsNU0AY7cobMJtN_-Ms4SmJEYrpr40_LJGNIct3AmgHr6vGPeydyWuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2a636165.mp4?token=vEbcWCCEowS43FxhHMyZoQRZKzh3iYb3z2JN4tCQr2TKqZDs9sy1bSEU8mM0zfJlKn956JefX__oaLojaWOoc1nB1syPhZtKlDuTJhZ2OZMMJdIEelkNj9vZ8R80AX2dkmP9iL7vjurp2sdV11NC5HSM2GIMaSRcWXEvSEUKbQ3QpMqStX_uL_0DdxES5GCQ1t7DiWeoOmX-Rj7UvTCKOtDpNDe21I5XPF4jd8JbDmwHpYUK6jml3dr590ezjP_8BA5hVmjr_o9p0aqppikSl4eEFMPlcoyXsNU0AY7cobMJtN_-Ms4SmJEYrpr40_LJGNIct3AmgHr6vGPeydyWuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رانندۀ خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال «شهرام صادقی» در حوالی چهارراه گلزار کرج، پس‌از حمله به مأموران با خودروی پراید چندین مامور را زیر گرفت.
🔹
زیرگرفتن عمدی مأموران نیروی انتظامی که باعث تعجب و حیرت…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/456332" target="_blank">📅 08:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461a1510f6.mp4?token=H8BhpQ3rEPsvyRFESRCK2Q_GaYJkv3SD_1QLS8cR0lkqIb5CC723QezX5Ezy7RqzC9L6vUhqR1sNNRyOoeSes9raL9oWYZyDgUCmjnKHwAPSKimWXzRmtvtvI52mXcPZoniFz0U3MzP46-0fa3sz9UYzrF1rLhu47zz6cG67g9p7534sc3blrx7SWJn355PgvVTS1spHFIl-0WxholBRl_eA_cSTIdqoZG1oshRz0mLyuZA-nXQOpycS82rLZ2g_PwPsGMZPa3iUeP023YBBy_77YyCaFOKJkz9M_35w13VGa6kpTqyh2-L_qhXp6oFJcAExTeffqVYrSgMNeiRUwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461a1510f6.mp4?token=H8BhpQ3rEPsvyRFESRCK2Q_GaYJkv3SD_1QLS8cR0lkqIb5CC723QezX5Ezy7RqzC9L6vUhqR1sNNRyOoeSes9raL9oWYZyDgUCmjnKHwAPSKimWXzRmtvtvI52mXcPZoniFz0U3MzP46-0fa3sz9UYzrF1rLhu47zz6cG67g9p7534sc3blrx7SWJn355PgvVTS1spHFIl-0WxholBRl_eA_cSTIdqoZG1oshRz0mLyuZA-nXQOpycS82rLZ2g_PwPsGMZPa3iUeP023YBBy_77YyCaFOKJkz9M_35w13VGa6kpTqyh2-L_qhXp6oFJcAExTeffqVYrSgMNeiRUwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی کور در آمریکا؛ کودکان ۴ و ۱۴ ساله در میان قربانیان
🔹
در تیراندازی عصر شنبه در پارکی در شهر لکسینگتون ایالت کنتاکی، پنج نفر هدف گلوله قرار گرفتند.
🔹
پلیس اعلام کرد چهار نفر از مجروحان از جمله دو فرد بزرگسال، یک نوجوان ۱۴ ساله و یک کودک ۴ ساله دچار جراحت شدید شده‌اند و حال آن‌ها وخیم اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/456331" target="_blank">📅 08:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارز اربعین ۱۰ هزار تومان ارزان شد
🔹
قیمت ارز اربعین در سومین روز از شروع فروش آن در بانک‌ها به‌حدود ۱۱۹ هزار تومان به‌ازای هر ۱۰۰ دینار رسید، اما همچنان حدود ۴ هزار تومان گران‌تر از قیمت بازار آزاد است؛ این درحالی‌ست که در اولین روز فروش این ارز قیمت آن ۱۲۹…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/456330" target="_blank">📅 07:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVHDkZEX-6QB2srcFbumM10QkkZixMB7AsOFckP0KDwMMRhxFuxnXgnx7YSPHYPaCrW_j3lTNrpqqT_G9rprZH1j2tmYiQyoZqHAUXy8l9y-FZdwtGGb5PN7GhfifVpmuR9BQ8dI3ewd9CvBRdYgKCOnwaeiUpnd1Aq_mPkPQ92nOTQPmrFw1jbwIiM_hdaieAYBoezyKNPhPDHBusCGLxz8c8fHMdf8esqlKSKTlrVxFy24qYrbFpdb55e_Os3ZQDFOERj_GtmUpwkiFkejrbmj9ogd79btTmOOcDSVDUEkiSaLpXmozss-CcizR2sW7RElpwyj86A_5My9Dk04CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص امروز کیفیت هوای پایتخت روی عدد ۷۶ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/456329" target="_blank">📅 07:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3A_OgquxkTitoWe03-40tcphafZ2t1YNTwpLRjz29Syh4bPC-KvA-5O2f6w5V5FcasQOHtVYUfkidyyN2SiPxtvE2POejj031HAnteZhqfRGxpM3GJ1lhtwuX3vxfy3A-begrfGH_bRPFznr7yYK2WG7-gc0UOkxDYOcxAEpuZzS8e8wxFOXFtKZp94UIoyNXvOp8oykMw-wqaZqMjl4OaTFpt0KHfIOgObNCMHnT9mwySFJFx19iyrkOK1dUOHm6EpCNssshFYdlWqHwAEklHSru7upVqjtbbg6LxayDS0ktNOD7loyTFStk4MvJFClmrALZ-6XdekbIUPMDfGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رانندۀ خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال «شهرام صادقی» در حوالی چهارراه گلزار کرج، پس‌از حمله به مأموران با خودروی پراید چندین مامور را زیر گرفت.
🔹
زیرگرفتن عمدی مأموران نیروی انتظامی که باعث تعجب و حیرت حاضران در صحنه شده بود،  منجر به مصدومیت ۷ مامور فراجا از ناحیۀ سر، پا، دست و چشم شد.
🔹
این اقدام سراسر خشونت صادقی که با حمایت گستردۀ رسانه‌های معاند همراه شده بود، یکی از مأمورانی که برای تأمین امنیت مردم در صحنه حاضر بود را هم برای ۳ ماه به کما فرو برد.
🔹
صادقی که پس‌از این حملۀ وحشیانه با آتش‌زدن خودروی خود از محل گریخت، پس‌از شناسایی، دستگیری و محاکمه، سحرگاه امروز به دار مجازات آویخته شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/456328" target="_blank">📅 07:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqwSR1iv3rQSY7Qll3VD3ibSVQbnc-q4juNjSxIrvpzjU5UTqDIxJIxY2TtLJJ8q63iUghrMB8WaYT4FEBvqwfU2tTiLFLdM9OBRB3vdO-IWwcLgL0LeFcW0bMOtndstXFn9p2fHmSY52CLMgH3G01EGrQyw7Rc-kYJbOTz8gMVHVpwu7VkcWfdAqW_4Stl3DxQ4imP3lLgoxEOI4osFjbx5k7gvTILSrZcX75cwcovHcpFZXfksnRcmePIakFkSa-eU-ESJjHTiDPOhisZyMugqQfHWEIIkZgIDG3hJZAty1JddImLw0BGd9k_C958L-o65QTS7we5shgw_qV1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ کالابرگ خانوارهای دارای کد ملی ۳ تا ۶ فردا شارژ می‌شود
🔹
پس‌از تغییر زمان شارژ اعتبار طرح کالابرگ، خانوارهایی که رقم پایانی کد ملی سرپرست آن‌ها بین ۳ تا ۶ است فردا اعتبارشان شارژ می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/456327" target="_blank">📅 07:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399a76cffd.mp4?token=FTvtCWxTwobvSS-XlG5Pg3B7qg-ZhQywXA9Y4d9jm72f2fSTlDZ1-_4y-WekWMGA-aTVofathj2z6wvYm7l9v1wWdl-IlyQ1vVNC-vWP7-ayEOdaXuhrPldPjy32wokxgNA3o2df3QGcWAzmxcXXgL6ZWK2V6HzS5XMtmrQUjqKMWbt6xIKWXGLa0RCxwivzwqJLZYG_jC3483tjoy0Gzuzth2fUgEVT1jxi9dKkD6JydF9jaltiaNotM3Ndnf9kp7yRTSjsS9tynxkCxS-a-Y8az-6atLVescjt_-NlEUfOqnJnWWUb5kf0GCSqhvHJBvTf62l0gbSo5n-eLOfvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399a76cffd.mp4?token=FTvtCWxTwobvSS-XlG5Pg3B7qg-ZhQywXA9Y4d9jm72f2fSTlDZ1-_4y-WekWMGA-aTVofathj2z6wvYm7l9v1wWdl-IlyQ1vVNC-vWP7-ayEOdaXuhrPldPjy32wokxgNA3o2df3QGcWAzmxcXXgL6ZWK2V6HzS5XMtmrQUjqKMWbt6xIKWXGLa0RCxwivzwqJLZYG_jC3483tjoy0Gzuzth2fUgEVT1jxi9dKkD6JydF9jaltiaNotM3Ndnf9kp7yRTSjsS9tynxkCxS-a-Y8az-6atLVescjt_-NlEUfOqnJnWWUb5kf0GCSqhvHJBvTf62l0gbSo5n-eLOfvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر فلانی بد کرد چرا با خدا قهر می‌کنی؟
🎙
آیت‌الله جوادی آملی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/456326" target="_blank">📅 05:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/456325" target="_blank">📅 03:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96755745bc.mp4?token=KC42En6TifwnpbIaxtylV5M4cZDjfNnJAKHOnTS7ukrvUoCT8cFeZ6XF72Pd8g6sx1XPi2XGDoyLAwKeC1Ye2_0KbK8ixQzT2Ha3LzXTBDBu8vFH2iCYAzgsym_MvCL92LuxZLGKvlUnsJxClIPCHRWSNAz14MZxIrZvlOXiCFeacsdT8QS78BngwRm_kHKTZA2odaxp-qWNJOWmTdogdz79_B-68yWhc9szPByODMY3a92rII0GdDzHEEaTWgAEJmLQ6Z5TMPEtVoFcomrety3J-sXhBE0O8RoIvzzQIWdcNypkZTaPaftSQKtOoSnbFr-dO7ZnyMzKAsqAhi-6AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96755745bc.mp4?token=KC42En6TifwnpbIaxtylV5M4cZDjfNnJAKHOnTS7ukrvUoCT8cFeZ6XF72Pd8g6sx1XPi2XGDoyLAwKeC1Ye2_0KbK8ixQzT2Ha3LzXTBDBu8vFH2iCYAzgsym_MvCL92LuxZLGKvlUnsJxClIPCHRWSNAz14MZxIrZvlOXiCFeacsdT8QS78BngwRm_kHKTZA2odaxp-qWNJOWmTdogdz79_B-68yWhc9szPByODMY3a92rII0GdDzHEEaTWgAEJmLQ6Z5TMPEtVoFcomrety3J-sXhBE0O8RoIvzzQIWdcNypkZTaPaftSQKtOoSnbFr-dO7ZnyMzKAsqAhi-6AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات فسفری ارتش اسرائیل به اطراف شهرک کفررمان
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/456324" target="_blank">📅 02:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/456323" target="_blank">📅 01:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4d889ef5.mp4?token=uiy2Q-NdE07jEfA28h5FcQZYxi2bUj7l0pTOppbt9wmULzy5HJ_wjeafrpYwv7DHalGjtezRdxuNP2WZtIW2kPdydRWCv7bGrDJ4yIp6MM9GRK2Rq1Z-D8V0-t0tDaJtmpYqK-aZ8vmWW7GnYzCsqXe0SXRKdI426tjAFbtg-5Gx-uLZLZsZk43zySYWCgh4uW1Sd_GPF8Tadqb6ysTskvs3cpKdJMDgqxZIFWgfOjax7BHaROec8cNDO82uodIREgNUZZnZUaM4WszmWVaA_fJGocQh7qoKr5dF8S7ta0sg9mB7ls0s5NNb2MLd2N9C3ZCMZLUGOE-Fgnt9D1uMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4d889ef5.mp4?token=uiy2Q-NdE07jEfA28h5FcQZYxi2bUj7l0pTOppbt9wmULzy5HJ_wjeafrpYwv7DHalGjtezRdxuNP2WZtIW2kPdydRWCv7bGrDJ4yIp6MM9GRK2Rq1Z-D8V0-t0tDaJtmpYqK-aZ8vmWW7GnYzCsqXe0SXRKdI426tjAFbtg-5Gx-uLZLZsZk43zySYWCgh4uW1Sd_GPF8Tadqb6ysTskvs3cpKdJMDgqxZIFWgfOjax7BHaROec8cNDO82uodIREgNUZZnZUaM4WszmWVaA_fJGocQh7qoKr5dF8S7ta0sg9mB7ls0s5NNb2MLd2N9C3ZCMZLUGOE-Fgnt9D1uMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمی‌ها در شب ۱۶۸ به‌یاد شهدای میناب به میدان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/456322" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFEtBG6Zcpx_e1olZ0dzAfpCJJMUjWO7Knacd9mSQvoufWgsVCF9VIZss73icMnK_LOu1R73rhkTBk2epwpNnoCHdPFF_I7-EfpPKpqwLSNN_lvhukcAs0bm6dBL8QrUGvrav4wEC10LTUiUr7RK_d0Rb9yx9MHSwA6C2XaD1-2Nr5cBt-TUWE2f-ZcPVF3EKjIjxvDICeJkorNq6q2lXS7H0BXTpb0VXsIsjSWE1R3k5N2JUp8IY786eBQJRfeSPTAWCJswz_-JFNoZTwMD_KYB8eEhsNyZxx8oKPIlTyAOoUWEDM0XmgM1iY02uS5NKXdf1EOB_zJwkRV0bw6KZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا درهای اتحادیه اروپا به روی ترکیه بسته است؟
🔹
«رجب طیب اردوغان» رئیس‌جمهور ترکیه روز شنبه و در گفت‌وگو با شبکه الجزیره گفت که عضویت در اتحادیه اروپا اولویت آنکارا نیست و در صورت نپذیرفتن ترکیه، این اروپا خواهد بود که متضرر می‌شود.
🔹
اردوغان گفت: «پیوستن به اتحادیه اروپا اولویت ما نیست و اگر ترکیه به اتحادیه اروپا نپیوندد، این اروپا خواهد بود که بازنده می‌شود.» وی افزود که کشورهای اروپایی تمایلی برای ادغام ترکیه در این اتحادیه نشان نمی‌دهند.
🔸
اما ماجرای آنکارا و بروکسل از کجا شروع شد و به کجا رسیده است؟
در
این‌جا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/456321" target="_blank">📅 00:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ5liyjkor4sRCw4Tr4uHgvckA85PyG9CnUAk9g1Ljsd7B-70RUTaFJd6AQ4sYZarskGY-CRVlhDZqPAP-P50MpQHm_qHmJ2LFxYLVRBbas8faszk70nFhh9xFmXrG3bpRJNqUaja-YQcDv8xNnhOkVwbcsVE_EPGld2JZvnsFUJOFIr6C9Rkn8gkd3lp_sdvj1fuxZO4V9rB8vE96_CZ_DHliJwp68MCdK1-PMQ9b5B9VeI3sAbHdqM1JsF1BzIfJzz4X5PcG7aDKk9ewJ8bYujZDpvpRhphHC5a9P9UO1a35obQYTR9kGMGjlfO3VzTLh2b2uCYvsCTVnrYi5bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuDa-DoymBHxRyRY1xCKd9fwelc9UPHjUe6_WLgjEkHfTOQmLdGTFPWe_iVQemJnfx4SMJNNJtm503eoeci5imFVJhbM0Krevy3acYvB126O682F7B6UtuDaP1EA3JL5v4MfJX7L4JBmmjzXdNEY4HpPttP55elkOBUAkV3v_C3G05fAIhjhYn41IlUsFRppKuE6Htvz3i0J0VeGFjYXsQYH_ViWSl0VZEgD82WNNZuSe7qDPPmjnMUM5RA0Ov-POVpY-s6Feu0x106GwXsxdzDPYqJUVJfBY4kJGyE9mxaSvMc3XYdA4G2xmdJ5dYF8N3q7w6p48we6YyefXLtsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgmUYk5HTlk_SstJ493ClnUCprOVCJw86woYUYUwpjxJiweKULg9lBkugftA8514_hKVo587H0ADbXi2FAzDKZRQOGkj7EeijiuoGa5uAtpx6DRAVRc-gcZrkzzVdq1jDefh6xEgUaibYdSXSSRfujFhEEC_t2K1U_WUXDS2ihWYuQi9JH4NcCe6P-BvqgHh8KrmfVpX0o66PHNdCONTSW_LoKt25Mua79UtR9lMzqF6Gr6wMUE0oHHy9xIMAFePNH2tOr5KXHe_onsmJM_1kjiuVKc8YmvDetQo0crGhim0uMQQU2Q0hF6kEpexDt3UK--9vpmNkKZQp9oYzohVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d82UjF22_-EidXQBfL5JrchqB1O_hfgk2rmRPbYKaCLil6JwtHtC5y1Tac0ZTS_Uuq2NL4EAJNErPaQsPGfm0YUi8lXWpwRvKXRAZrJJmmL7enmzluEzctr0hX8RMi-E15YP8UuCYwfe_R_jbqy4zuksT1XqBx5cVoQO68c8OdFqjGd0sd0cn37O-7B2zFM6ijWUsxeyOsWAlq4hLda8Gzcc_vdIKrNbsmRcgdTceoV6kVxMba4Lml4c0Vhav-bmSR_0LvWF5ZpBAs4FwWwWX23A3UZu9sVcijZIrFaUnExQYiuy0vLg_Uiu9jXlux1Ucow3J9tSoQgANr2buHGf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4FWHYwWm_y73hR2CuTLtVfgHY4OslAYiAOv-pyyJD5m-KqD36TtocQTsoPbGw45lIvE2WSKIPjX7ShpwP50A_z5-z_VH8VZcioXWOF5lC3SnV_MWmaKCKwo69JXtFdqo3I62t5PhjlZqPqGAEZgQbhept7QZiIuRaeVcB7K6fguTlMWHKkr0baxfP0pn5zvwd4SVGPvxhwv-TrOSqsgXQWQcKtkdyVu3qSyZr0EbTpKBu4EICzNBu0KEOmj1dk3mDNljiYqiwKEeUA5APAJeGLnWAk12rnXaMfje7sJA4zPq436n7FoEWafTEG5aBbpSaAvHRu4JWeji00dVgxUYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۲۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/456316" target="_blank">📅 00:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456306">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGxbWC1ceWPBECmshJyteT6YzRN1Ly1_D_Nr9ALg5fzP4gh_TpoYzPaFQYH870lysRUn9Yq5V-UbQllcDywntNCl5GE3Bxxv9AXeHo-h9g-kYF6XDhkW_L5-8x07Vu5mrHc_78ObH3i4DsWUfGDaBA319MME3eWl0GKS-kXp9dreDCaErLBWrPKb1gBclHaqlF9kD58TS8fU3aa30uHIKtZmyWSlv1rxNUVZr4qe4JrcErrWbeYsnWe5_TrjMrtiDMZIQ9zWfgXlMQl6AcruQYPqwgaNX4tRlDEbxrwBTU2Yw1T26hcjaCcg-BZpnyHbr7qHeGf8MM01xl5xlZJ8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K30j0IRyNSBt2WnQurYyKqO-gpR9MpzswaxMmevj9jVas70F2SdpWhiA3x7KrrQprlHWT2xAl0a1cRT1vl72ph80trgZgFdm0KB-7yZxFdAwC3_W26SpJk4yaU028f2z8NgDC0VGKCDFG9sxlGHm6744koFI-JLp5KduhaPMFq9OaiVUwoss5RV5_zXCU2j3KRR64Qh-0fdJXWZ3NUJFIVZG93FCTaZDfCGUgg_bmuG9WkYl2XT0hbGntocWzW8oCzp_K8bRAlftNsaFhJ-CkLeDqTAg8rSdoBr0G-aE1fG9R5ugGGVqem9BJKC2iDXnMXMUU1WLLKjUlAq4pPy_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRUANmJqtnyeZ1P7AfyKcTqJIdUxCMcysBbOnxGM7xDuWP4vQkv1Xdoq7eGULjVkj5a4I_xkO11FKCC3XrxW3FwxEUiwQep8z1CyzpPnlHim8rTduVvvnDDyYRb_QZEiAt2cVDcofTTlWBmLDFAlwlkZsWiVZVUXzMRxrb_0i9kJR5DMZJtGseLJKp5GILfI3ImU9ZAGwqDdLfd-c581z9on5GeO80mmCqRFjbFmzbbjo6kCAbWs5QMF-po3zRWTJJ8-dOEKZQtHkTOua8p4UR4N0lWtqUQFOCJCMXzt9PccqEDGlBJyS5YGQbPA9G0IniS1v6Ll5uWVTVk8c9dPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7dDeVcF2F2SmkQMSI1hZ5p-sFyOvpd6Mkxo1az8SswZJwuNolJ9BsBMFAYKZa7X81Cs1Y0YCIOMnAgiA8fjxp2lsLctwNyk8aYxszmJTHZDvtLspLkRY52xnGYQ_Sa8XG9dYdZlLJVdK5Sjyy4b367ADkph3WrffMsyBCYCEtsYSpRu-YPGVBURIKZZqSSY-LtqlALYoncpkBHLdrAs9cf_HYfVEOFLHninJMErkowhJBR-0q_jCeB9KmixKqMqnrNBv6cKrlONS3FtlHjmgVUjlNEceMKClsc-OOodAKI0Q8yz3vp_3hVwZVbqcO5WueGnDTmUToskXs3_TMjqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQyu0lruW0pG0UO53dYfCarERTkpV3HnWBkURJK6TWHDlH3TedbiH7Y5JgiGuFJxBKCZriM9sAtwfM7mOCFqnSL_xz_SyqA0QX3vb3SHaVPBukqBXgjOc92UQKk3uETSPsgR-OA8W1Rd8fYVRifejsRP4Tla6hmxXXKkJ7JrR8QVWQqOuNoW5gGHIEzQy0pW9vhrkjlGC4u87qgYq3JBzvZzD8_xOl18wT6bCpdXuWHGtK25fRmS8muQxTvMy7XFbKz-GDY1ANws7XFxangyGOK67pkVuH-vwARJ4nqOKN1pZK6j6gjvz6n05uYgmKUKuHtDNFUzdL7GpQMicrcHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z41_DZ7PunuiAzdbJqzB0_y2e509-d4lFNU6RGbJ-Iw1KVG93DE-f289rMqUBnmpBGDg9y1ejTEyvIcqFyYt7wkl84kg34Q0SG_ktUIUDjjRecda748DSya-rTW3Dh9ks-8nxt-rIq8EEOV7tQZN-lGf77yh55jNiVK3hV1FJqE24ofeIn5XY2EeX17WrE77s1fZIzkAz1Jna54maFil068Y2LOm-xMyPQw7SMsexC2OSdMCtekw3Vlam9JJW7VgcYSajiamYrzuWS7Yy9kpE1CGBogzIXiKU4VTCtsd4dJS5PJj-e_6IjXScNOaNe17-93z0hVVXF7EVIDjbAwTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaiZ4Uq1W0_YcprP-1S0LyoTFEejmdFZfBXuPjj-iU0v1DiGIFi9Zjh_1qqS701ie1K8-YVSGLDTwS0kcw9DBSNAGb0OfVWOFMLyWE-jFzz2yEW2_klao0PGi3udCsjTokXrI5D4VsbpLMHkgwqYyCv11e4RQr7uQgc7puAq1ituLJpRJpeE_CxFEos_ylrEYZTQuq7qGumT2HwST7TBeiIIYQYF989dy0FsLz7O0ah7l4TVJVHeflpT6WSbV_OGlr3zsO5pigW5S3tlQ0Fj1ZWtkPuKllua1_k4SqwsZvUWIgL9xtQhdMhf1wV9mH6_FB46zOx0tDy4Snjkxox_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XB0R4gyCkdPVDOI21S40wtspDpXpwiqT3COKd99oL5omZS4dsMXQefynJRJKr-rq5hbIv-OwzlKWcupF4lO-86nmKw5uPX6fpFV3M-klIIHR8r1vlql7HSuSYEf8SzH1I5i5wchVbHy7NxzkmYxqyVfQY_2E4-Rife3qcvzyzmiuR3KHp3R6NAmadYo2r3G8CmAwOks0FJfT1XfO0C4DZGxfNch3Jmu3VPlVL1Sqfp6pR9zyJcZ8b810qv2e6EILHrhl6SErPy1Y-KddTmX1taDt4vgfhxn90llxyy6B1--VT0-1MXHPB00INe1vKfyIyLW0nMKCYz5Zogw0wxCA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu5zFn_YGPjORQusaaaTv1YVgvztBLNumJ71VBmk1VFpQX1U3X5jiUWDsZBy7_nP_OJCtiiFscefP-jYq5NuV8I3On0iXOg76gSo_Mt5eoaWvFrxpuGvPQ4iOIC0I9FJ03Pt_UqMBMw_J9lAUiA2aaOXVqY4apuRqDMhfhdDINy3gAinLQuL37IT5xrFdLV5rRWLqKKKtHXde6Jm1dEHCxJ_0-VD15Uz9b54Ev52gSINdS7oqmXzGEbtfjEQMi7oW6zum9gJ53yxCVR-qKyG_C25h6hEs4JPxf7W65AfixnIfmNNEwKftUG9oXjhHIhkpcC2F1NiLSYZLAN5-bgcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noQaKmJBRltXbSqj9o90Q-osuiRIdEYFyiPvYbt6jHvD5zDgK5T_hT1y4vfEA-OVrSoZ76WmiRdKr_JN7KOlfzqAFGVf1LMupwDEjtAm-dIuE9rvzH1NtAxlmr1eJvin_BQbChsr9_WI39JkGhIEV1bhQR8U1zeUW8cMew4mBgXyUiM9718lKPyFKzQmBCoVhZ1hk2dZdyarha8dFkoRipjMP1k29sXan4l9QxI03R6_QF023t5koQbKO0hRooHAf3K9x0jesTbt-k2JmXshSvr2914QaIKyoCiIhcLKPQJ5YIXvP-HgyglNR_ehqdEs-ROUsMtBoGcDqaVuMfbqJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456306" target="_blank">📅 00:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456305">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4125379ad.mp4?token=WzCuEXDevOS3qd3KLWX7CRXbElQa1_mY8dl4rcXpOwKvY0mA4Wn6YvllMJYVOb5gNlnfzETuZLK4nR49nNIc1UszBmHJuYs8j1HjbnirkwwF7z6jRnVbyzwtqqoo-Sl1MnIlPPczmKcr7SGdzkYVgTxdrdayepYWg3UGHnuZ3h2cTPwLWoVl987MFQ-heLcEQ1_3gnj6StnF6KlPl8aoMwVewtFV9IE9ukjFzh1241E-g1zFVwCgt3W0OTDIGtlev7RDLYE80pIZYneINR30K4tqd75pLqZwTitNWZdIeSw4piu9LmnZVJbaq5-isRB_hJusYbBC9UNhosxKARYZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4125379ad.mp4?token=WzCuEXDevOS3qd3KLWX7CRXbElQa1_mY8dl4rcXpOwKvY0mA4Wn6YvllMJYVOb5gNlnfzETuZLK4nR49nNIc1UszBmHJuYs8j1HjbnirkwwF7z6jRnVbyzwtqqoo-Sl1MnIlPPczmKcr7SGdzkYVgTxdrdayepYWg3UGHnuZ3h2cTPwLWoVl987MFQ-heLcEQ1_3gnj6StnF6KlPl8aoMwVewtFV9IE9ukjFzh1241E-g1zFVwCgt3W0OTDIGtlev7RDLYE80pIZYneINR30K4tqd75pLqZwTitNWZdIeSw4piu9LmnZVJbaq5-isRB_hJusYbBC9UNhosxKARYZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار صمیمانۀ اعضای ۲ هیئت خبرساز در حرم امام‌رضا(ع)
🔹
دو هیئتی که در ایام پایانی ماه صفر در نزدیکی حرم امام‌رضا(ع) خبرساز شده بودند، در حرم‌ رضوی دیدار و با اهدای گل به یکدیگر، بار دیگر شعور حسینی را به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456305" target="_blank">📅 00:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xdy_2flkE5hoQAvAPTQUlEd8WaS0tPzv9qCiMGeBvmWG3ZZ5jrf6XuDZofNYc5m9YiPdfQHsKQLJ76LUsrQ9pBD8sV3edVPbelhXirwr_4LLE7m3LT4b05LG-CKc3wOQFJzLWdtUEmP7FODdC45jwniOzllB7_r0MsYuPZ1Ypy32UVYsqdmO9KiI0rrEK9rUI7rtUcVzlRIQMPwRGdoxbHhW6WbrQ6qpWDklda9Gu9yqrfc7Sn8OsMw1UzP03bhxjCcD0-wQFhFIFfAZvyHFtFhTf_LvRz02KBhHaoDa72KmJDLyeCi3drsLybelVAUxUIbj2LlhuemZK3w_0aFz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش در بندر یمنی که زادگاه قهوۀ موکا بود
🔹
بندر المُخا در یمن، زمانی بزرگ‌ترین مرکز صادرات قهوه جهان بود و نام موکا نیز از نام این بندر گرفته شده است.
🔹
این بندر که یکی از کهن‌ترین بنادر جهان به شمار می‌رود در فاصله‌ای حدود ۶۵ کیلومتری شمال تنگه استراتژیک باب‌المندب قرار دارد و امروز به صحنه‌ای برای تقابل میان اشغالگری سعودی و مقاومت مشروع ملت یمن بدل شده است.
🔹
متجاوزان سعودی پس‌از آغاز تجاوز به یمن، به مرور بندر المخا را از یک مرکز اقتصادی پویا به پایگاه نظامی و انبار مهمات و تجهیزات نظامی خود تبدیل کرده‌اند.
🔹
این اقدامات تجارت این بندر را کاملاً تعطیل و تمامی فعالیت‌های اقتصادی آن را متوقف کرده و  آن را به تهدیدی برای امنیت منطقه و جهان تبدیل نموده است.
🔹
عملیات موشکی و پهپادی نیروهای مسلح یمن علیه مواضع سعودی بندر المخا در روزهای اخیر در راستای دفاع از حاکمیت ملی و نفی اشغالگری صورت گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/456304" target="_blank">📅 23:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1titzaE83c8NSd9yex8N-rrxnIpjsZiKmYTvvskHfSL6fjEwH4T2PCeiIBwmT7PJhHVb64sh3Vv0yQDHvJoqMw68YlRAHa7TwE3QttrAwaTlHjDRL4UdW_7C1fZH-Z8TWqOYFMx201X0iMrq5lGzAiQMb2OiPY5L3mXNcUoqJFVv3Yct5BeSawBMQ7A3WWnVq__JZu6mmf25RZ_HaPUHG2XiDKhE_sIz9Upv1-tVs0GLtXumW-K4VEK6U9tPYtDVTXlFs4E2ejv90PV32WBFaES_3rtu1I2vSw36x9dI1-6YPejodyjxtpfRT1hMg9BUhOdus7xg5DoYD91RjLElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل "مقدار کمی از همه چیز" موجود بود، نه غذاهایی که به طور شخصی انتخاب شده بودند.
🔹
این ملوان گفت که به خدمه اطلاع داده شده بود که غذاها "با هم مخلوط شده‌اند" و افزود که لوبیاها از جمله بدترین غذاهایی بودند که تا به حال چشیده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456303" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گرما ادارات خوزستان را دورکار کرد
🔹
استانداری خوزستان: درپی افزایش دما و ضرورت مدیریت و پایداری شبکه برق، فعالیت ادارات استان روز دوشنبه ۲۶ مرداد ۱۴۰۵ به‌صورت دورکاری خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456302" target="_blank">📅 23:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6228d7d5.mp4?token=rGBOph9FXkE9KHE0Tt8WWPh6g5VD9mq2jJ5lqDuwJ4ZZdogQQiYH-0dcHnIA3mMbtDirc_mWd8yn98FxJ4JV3-x8AAeepMIDCaCGWCyl1fKOlzNbob2f4BmYImA4D3jb1Bw2bbXg7yIqhlsnLxZ99DdVkUfZXXo9LuW_JRg6gUmeJRckDe-rCGBs-lfLuTcOlKON-4u5gpe3N7iRekXzpLhB2gdEwk6DZmDT6k-2SFb4LL28PZ2arHIA2T5ltlh4ocfiypPJjhm9W9NSEMsv3atuKRXJFyIXwUg7p4g0nXYWFvqIH5MKJ10DzxFpyz_ZzMPQT4tXVIVgEMvPXqiMcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6228d7d5.mp4?token=rGBOph9FXkE9KHE0Tt8WWPh6g5VD9mq2jJ5lqDuwJ4ZZdogQQiYH-0dcHnIA3mMbtDirc_mWd8yn98FxJ4JV3-x8AAeepMIDCaCGWCyl1fKOlzNbob2f4BmYImA4D3jb1Bw2bbXg7yIqhlsnLxZ99DdVkUfZXXo9LuW_JRg6gUmeJRckDe-rCGBs-lfLuTcOlKON-4u5gpe3N7iRekXzpLhB2gdEwk6DZmDT6k-2SFb4LL28PZ2arHIA2T5ltlh4ocfiypPJjhm9W9NSEMsv3atuKRXJFyIXwUg7p4g0nXYWFvqIH5MKJ10DzxFpyz_ZzMPQT4tXVIVgEMvPXqiMcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۳ طرح پیشنهادی بنزین روی میز دولت است و هرکدام منتقدان و طرفدارانی دارد
🔹
هرکدام از این ۳ طرح تصویب شود، قطعا آن را پیش از اجرا اعلام می‌کنیم و مردم را غافلگیر نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456301" target="_blank">📅 23:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025bafd05b.mp4?token=d0_HQjdZpKmhxJ07k6UoNN5_lfxhH8PKnj9aeerDHzbt3LyTGPJWR7eEd0IZMlFVYJEmqMdVRUJrr-3MXOsZy3ikwxNHLIIdP5MDHaoIzFgOqISj7K7awY2WJCOXDwW0lkwTh75KJMEfO2Hei-KvjRN5Eyi7dpuEHQjYphQL9C0ANkBXDu5fHBO2vSjNHasTWS00zPhsn503GUmNhBkQ2MhSXs022m4r1Md3_tWDywf5l40vOhMs8rMtv_TvaNeWOOIxxbs8_dUNun-q8anFcDArYraVQuJQkkhWtsIHSKU1IMRBW6MNhlzcn3RCd_y4ZEEuRmldbeQUG_4GtTa4HVR26L99BK-JF-lQJrhADjBihTZZ-B6bJuaFKWLBj9WlyYrhW1EksghSISE3MFw2vfh28b9QyaRkdCbOvx2TSgcqLGmu7XJr0bPmaMgSu75cZTKcPDuNxxdyTtwwSHYLdm7Sro6evLyBNRGPwLoa_BT4wNeNJgXbAscBlk9n5UA8Aiqz6KoR0fncnH3WiNUtgspCThg5CvbK9qs1SIvBFbHg2w4sdnB4x-IG3OOyrtHkNW8kWRb5XEYPxBHmvrDmuPLfAIt_DvRbs32QuTtgD8_O3IjvwnnmR6Ckxdww4xHLlMhSHQDOCYTDFyqPov9P0P8_4NgabR1_q101A07mE1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025bafd05b.mp4?token=d0_HQjdZpKmhxJ07k6UoNN5_lfxhH8PKnj9aeerDHzbt3LyTGPJWR7eEd0IZMlFVYJEmqMdVRUJrr-3MXOsZy3ikwxNHLIIdP5MDHaoIzFgOqISj7K7awY2WJCOXDwW0lkwTh75KJMEfO2Hei-KvjRN5Eyi7dpuEHQjYphQL9C0ANkBXDu5fHBO2vSjNHasTWS00zPhsn503GUmNhBkQ2MhSXs022m4r1Md3_tWDywf5l40vOhMs8rMtv_TvaNeWOOIxxbs8_dUNun-q8anFcDArYraVQuJQkkhWtsIHSKU1IMRBW6MNhlzcn3RCd_y4ZEEuRmldbeQUG_4GtTa4HVR26L99BK-JF-lQJrhADjBihTZZ-B6bJuaFKWLBj9WlyYrhW1EksghSISE3MFw2vfh28b9QyaRkdCbOvx2TSgcqLGmu7XJr0bPmaMgSu75cZTKcPDuNxxdyTtwwSHYLdm7Sro6evLyBNRGPwLoa_BT4wNeNJgXbAscBlk9n5UA8Aiqz6KoR0fncnH3WiNUtgspCThg5CvbK9qs1SIvBFbHg2w4sdnB4x-IG3OOyrtHkNW8kWRb5XEYPxBHmvrDmuPLfAIt_DvRbs32QuTtgD8_O3IjvwnnmR6Ckxdww4xHLlMhSHQDOCYTDFyqPov9P0P8_4NgabR1_q101A07mE1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: در طرح سوم بنزین، طی ۳ سال ۴۰۰ هزار موتورسیکلت برقی و ۱۳۰ هزار وانت گازسوز می‌شود
🔹
همچنین ۷۳۰۰ اتوبوس اضافه می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/456300" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195335984a.mp4?token=kOTk8SLjkBbG3XNC9OCrdmL5plZUYi3mQr6fduLrGYd3VoVGNZXSW845i4ssnSrFqulazmUY8Ah1yq9xmkMFCoDFw64yVneAbbUs7tTjCdPjtcBq3os0an3mP0WIaGWBAlaEckpFL3ZznGpob2DgWVnbnBMSVSD3TsXw7e6HzLTSzTU_kh_2S58afxE3bHsFvoks6jfBmLTu9PhuwGB83Gv_Lj9i0sv8G8qnouqYmfbNbPSOl2gJ6hk-1tSoUCiGfCfRC6M0pIQrybNk_c4sBNVrIhWupqytWzhdurAgFkzlm4HSi8z8pvnz5tzU1nxt61O6Ixp7N3Chb0aoJAdbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195335984a.mp4?token=kOTk8SLjkBbG3XNC9OCrdmL5plZUYi3mQr6fduLrGYd3VoVGNZXSW845i4ssnSrFqulazmUY8Ah1yq9xmkMFCoDFw64yVneAbbUs7tTjCdPjtcBq3os0an3mP0WIaGWBAlaEckpFL3ZznGpob2DgWVnbnBMSVSD3TsXw7e6HzLTSzTU_kh_2S58afxE3bHsFvoks6jfBmLTu9PhuwGB83Gv_Lj9i0sv8G8qnouqYmfbNbPSOl2gJ6hk-1tSoUCiGfCfRC6M0pIQrybNk_c4sBNVrIhWupqytWzhdurAgFkzlm4HSi8z8pvnz5tzU1nxt61O6Ixp7N3Chb0aoJAdbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای میناب و گلزار شهدایش در شب ۱۶۸ اجتماعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456299" target="_blank">📅 23:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6698b825.mp4?token=XKy1YYy2C5b8NLs1ST1PIOwlEjtaRJF-DJM6N6MxtrgZbBO_8RzGh7B-NhMtbd_fjNdup7eQWy7yt1WvSPMFP0IIEaJIItHeFV9RKOosyInDEqcnT3FUi6wgjA9H9XPSk-HPDDE--QxgHoxghvvu059uQqFnbaTAZ0cTUFlfRIgyKW3r37xNlBCX6udu5qUal9inJT5-0NuCbS2bcoJ1HbOinlr9nFI8xHi_ul0iUGQc1Berkaxs0oshN8wxHwBUSH5jBfFPqMYtq5AUqBBuA7yqt89lRsr2cgAOq1QT-DhOlN44ppPzcYbYAz2yzfkWtze-1cm6Rau5JNOG5GMc2mgVA7Xk6qcJu6JBpcoaMGIkEL3sPvxOpFzxBA2AZBOx9hRqAXZ0bC9IWhsMfjRULEYoxND52NVRpJ30aqdejbTUOFH8fClFmPBCoYLbsZKNpDxdLrQOhgwGM3Pz0Zom4yj474m-Opl-odq3sBMMK9pXDuq5EiIgIK_f3YkZtFyYgG7EVKM_jJisTjbpw76R4xKk_Sv1SEJsIfnWY25iIb5DCVFh9vwVQhYp2khvx6cWQ21CJMT2znTfv2JmDDpNc9ctvLwvldsb40THs6b3PeG3Se7bShrpQ5cAUbnNGROjZDhilNg6x0kGbHn4yDRQIPBLE0QKJns7G3dsc12Y8pU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6698b825.mp4?token=XKy1YYy2C5b8NLs1ST1PIOwlEjtaRJF-DJM6N6MxtrgZbBO_8RzGh7B-NhMtbd_fjNdup7eQWy7yt1WvSPMFP0IIEaJIItHeFV9RKOosyInDEqcnT3FUi6wgjA9H9XPSk-HPDDE--QxgHoxghvvu059uQqFnbaTAZ0cTUFlfRIgyKW3r37xNlBCX6udu5qUal9inJT5-0NuCbS2bcoJ1HbOinlr9nFI8xHi_ul0iUGQc1Berkaxs0oshN8wxHwBUSH5jBfFPqMYtq5AUqBBuA7yqt89lRsr2cgAOq1QT-DhOlN44ppPzcYbYAz2yzfkWtze-1cm6Rau5JNOG5GMc2mgVA7Xk6qcJu6JBpcoaMGIkEL3sPvxOpFzxBA2AZBOx9hRqAXZ0bC9IWhsMfjRULEYoxND52NVRpJ30aqdejbTUOFH8fClFmPBCoYLbsZKNpDxdLrQOhgwGM3Pz0Zom4yj474m-Opl-odq3sBMMK9pXDuq5EiIgIK_f3YkZtFyYgG7EVKM_jJisTjbpw76R4xKk_Sv1SEJsIfnWY25iIb5DCVFh9vwVQhYp2khvx6cWQ21CJMT2znTfv2JmDDpNc9ctvLwvldsb40THs6b3PeG3Se7bShrpQ5cAUbnNGROjZDhilNg6x0kGbHn4yDRQIPBLE0QKJns7G3dsc12Y8pU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
🔹
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456298" target="_blank">📅 23:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f451cd432b.mp4?token=QLB7Ypv8uyn_bsroL0Jy2RvWc2UG93VuV_9LGNIKZgX9QwMP1T05h8gtu7g6R_UDxa3zVWHjMBUbnGjy3Thd9J_rI2bh04uU4KdhhaTS83_nfaX3tKnVYD-jY8cLwnB7yiltnrG3qoPqIyKUgPva9dDS1nyS6bOtESjpy7TaZHgSaAK1H23cRWeQlwx-Riiu29ACAEQ-_kXDygbWFp0_npRz7XUwnq6KibX2L12_O_dq2et6cEcELMcudtP1F-gFrPQDnMzHShs2OkOKN6s99l1CvP8JiruT_L6LfOU56NP_UPX0OezM_pz_InTFiJzzXmtFhVY9vupVKUPLQxn89A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f451cd432b.mp4?token=QLB7Ypv8uyn_bsroL0Jy2RvWc2UG93VuV_9LGNIKZgX9QwMP1T05h8gtu7g6R_UDxa3zVWHjMBUbnGjy3Thd9J_rI2bh04uU4KdhhaTS83_nfaX3tKnVYD-jY8cLwnB7yiltnrG3qoPqIyKUgPva9dDS1nyS6bOtESjpy7TaZHgSaAK1H23cRWeQlwx-Riiu29ACAEQ-_kXDygbWFp0_npRz7XUwnq6KibX2L12_O_dq2et6cEcELMcudtP1F-gFrPQDnMzHShs2OkOKN6s99l1CvP8JiruT_L6LfOU56NP_UPX0OezM_pz_InTFiJzzXmtFhVY9vupVKUPLQxn89A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت تصویری از حضور مردم لردگان در موج ۱۶۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456297" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔸
در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456296" target="_blank">📅 23:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔸
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456295" target="_blank">📅 22:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=ctypE_zOzg5qXaxdKo58Wtfm6GWmvVOOrP1QQHnO0-yTqbfsk0ZKlREEZKFBZseCQ3cESYobZn8GZcjT-GVzm2axT3WwzNOlxQPnqSSjwJ9jwCjlHezU4MTcjrTsirI1MRYHa62JfdyKwrwmiHXmvgajiVrInvwNyl46oSCSIBkJXbUReLNDy8T3aZqeHDmXsTd7zDdl3YwU65mVt31QYnfRUlzCUYqakybFLM0EGl0nFZ8z--ZJfnJaujOGWBkDtdpUrqu9PGpwBhla1zBcY6DdX8YQEzUzLi6DQp8r0QHPgrSdqk-_sp7eRf_EzFGL-yKwGnVUe5bnHxNeSR_GDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=ctypE_zOzg5qXaxdKo58Wtfm6GWmvVOOrP1QQHnO0-yTqbfsk0ZKlREEZKFBZseCQ3cESYobZn8GZcjT-GVzm2axT3WwzNOlxQPnqSSjwJ9jwCjlHezU4MTcjrTsirI1MRYHa62JfdyKwrwmiHXmvgajiVrInvwNyl46oSCSIBkJXbUReLNDy8T3aZqeHDmXsTd7zDdl3YwU65mVt31QYnfRUlzCUYqakybFLM0EGl0nFZ8z--ZJfnJaujOGWBkDtdpUrqu9PGpwBhla1zBcY6DdX8YQEzUzLi6DQp8r0QHPgrSdqk-_sp7eRf_EzFGL-yKwGnVUe5bnHxNeSR_GDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: باید کلید اصلاح تولید خودرو را محکم بزنیم؛ نباید هزینۀ مصرف اضافی بنزین را از غیر از خودروساز بگیریم
🔹
باید شماره‌گذاری خودروها و واردات خودرو تعیین‌تکلیف شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456294" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/811cfbd05b.mp4?token=wCTxY_QVHnShS_EkhnrDtOzYIRFG4gwMLuZXSBmVLxyvakdrQumxe-U75dt6mmfsBjDDdgZpXiXRpix6aQRrMQHFrEs1HtWnxKH1pUTD-luA4HjUJ6kcqB2GofWbj-Ys3VrSo8ZFyqkKH52Ws_qnx4wakbXi2LYfMKnwE7VbjuleTKV0eGNEPIw8QQc_FTzmx4QeH2M8MFasbuI4v3V8kM9rlXELVLb5M95QlgV0i7JP341UJ_o8nrE54jva1N_BNodmkOqhxlViy0yriP8YexLozqcprQfgRO56Pakmhs_z2nBpHyWZPo4oaT-eU5wHei2AilwofXg-y_neKu18uDtxUNS_bvewQm6YgOgRPcczFpOFBoVtkJyB7wJDrFmxN1FswxrtyVYhxHKc7JpAu19_NpsSj4FByGDQQmZE0X6SfDN2kHP4ECFg3ySdgrFPGXSc1ucwRo2N_apdaLJv4oMTj45rdRcdkUORflH4lppMVygZCQ7HtLmJMuBUTO6iZMdOJBjDc8kDM9-ydbMdYdYxeiSSGdyldHDLul6dMcv3WzC6GRI2jsCYthHFbfSed792DJO1Ty1mMfhiMXfOjMerzY82RXllPa_WG5hUjeAVcZlSJKYC3rNG0yLGSS2l2reb32JMDZrzPTERLftd-lFLclZ-i-dCwl6F2kD7XIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/811cfbd05b.mp4?token=wCTxY_QVHnShS_EkhnrDtOzYIRFG4gwMLuZXSBmVLxyvakdrQumxe-U75dt6mmfsBjDDdgZpXiXRpix6aQRrMQHFrEs1HtWnxKH1pUTD-luA4HjUJ6kcqB2GofWbj-Ys3VrSo8ZFyqkKH52Ws_qnx4wakbXi2LYfMKnwE7VbjuleTKV0eGNEPIw8QQc_FTzmx4QeH2M8MFasbuI4v3V8kM9rlXELVLb5M95QlgV0i7JP341UJ_o8nrE54jva1N_BNodmkOqhxlViy0yriP8YexLozqcprQfgRO56Pakmhs_z2nBpHyWZPo4oaT-eU5wHei2AilwofXg-y_neKu18uDtxUNS_bvewQm6YgOgRPcczFpOFBoVtkJyB7wJDrFmxN1FswxrtyVYhxHKc7JpAu19_NpsSj4FByGDQQmZE0X6SfDN2kHP4ECFg3ySdgrFPGXSc1ucwRo2N_apdaLJv4oMTj45rdRcdkUORflH4lppMVygZCQ7HtLmJMuBUTO6iZMdOJBjDc8kDM9-ydbMdYdYxeiSSGdyldHDLul6dMcv3WzC6GRI2jsCYthHFbfSed792DJO1Ty1mMfhiMXfOjMerzY82RXllPa_WG5hUjeAVcZlSJKYC3rNG0yLGSS2l2reb32JMDZrzPTERLftd-lFLclZ-i-dCwl6F2kD7XIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع ۱۶۸ مردم مراغه به‌یاد ۱۶۸ شهید دانش‌آموز میناب
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456293" target="_blank">📅 22:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31555c2e52.mp4?token=RjHwO1boDCjyxhJ6aKoA8WOiy068VFZNoRPdmxpipWLabbXtFPhAcpa3DpA-cSKMwNCBdOEuQYGJ7-IAoC3LdEZi8sVPYjb1jkiA0aXRXP3RcUH5hS-2vZeLS4XlGEHAIhGmbsYQUogbGlasWjR5S7LVeYUEEvG-XyghEzvrDj4xVpRrR-GrwxD1Cxk9VOjB_BWoaCCAXkD8bQh3pjA825QdH4RRYojqI80QLrFxGNBYFYGKKKHift61314YH3I5nQy5x26x82JsdOOaDlFtN6aZ6P0BmQXjPwGfqfcWXqWiIm9Bb1GbTG6visJBpt_07VqdgO2BVPEs9pvvoShLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31555c2e52.mp4?token=RjHwO1boDCjyxhJ6aKoA8WOiy068VFZNoRPdmxpipWLabbXtFPhAcpa3DpA-cSKMwNCBdOEuQYGJ7-IAoC3LdEZi8sVPYjb1jkiA0aXRXP3RcUH5hS-2vZeLS4XlGEHAIhGmbsYQUogbGlasWjR5S7LVeYUEEvG-XyghEzvrDj4xVpRrR-GrwxD1Cxk9VOjB_BWoaCCAXkD8bQh3pjA825QdH4RRYojqI80QLrFxGNBYFYGKKKHift61314YH3I5nQy5x26x82JsdOOaDlFtN6aZ6P0BmQXjPwGfqfcWXqWiIm9Bb1GbTG6visJBpt_07VqdgO2BVPEs9pvvoShLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: باید تکلیف خودروسازهایی که پدر همه را درآورده‌اند روشن شود
🔹
تا وقتی موتور اتلاف این خودروها روشن است، هر تغییری که در سهمیه‌ها دهیم فقط نقش مُسکن را دارد. بخش بزرگی از بنزینی که در کشور سوزانده می‌شود در موتور خودروهایی می‌سوزد که…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/456292" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e81f7d99.mp4?token=I0YxtvjvuXJzTsuOKdSo67uPZ8lbhsmOZzdczjhoc3YZw_qKpKuS0iJesRsyP-tIMz3lBV7lRfNvkx_BElEAp1gVfOcqC_wLISHyOTJcAn2ODUV9igsvmpgYpIOAMp_Xv14Buqq8A8jrQSKIu-ZqgetcRP4L7p1GuPYOq8Z40WxvTnqG4cvMrb0Q4jmH5K7_Tuctcwwdg28hcGVRxAEhngjhEheNas9v83Kt2eLAXKmU6kBE6cKyKBOxxfECfn5mX2uLOfjy8xKjpmdK139vDho6AgvZdrvkqdkCM5mLEf_INAQyKGoyclReX4xv5sFoRt6Nq4l-GyJ17da5WAgcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e81f7d99.mp4?token=I0YxtvjvuXJzTsuOKdSo67uPZ8lbhsmOZzdczjhoc3YZw_qKpKuS0iJesRsyP-tIMz3lBV7lRfNvkx_BElEAp1gVfOcqC_wLISHyOTJcAn2ODUV9igsvmpgYpIOAMp_Xv14Buqq8A8jrQSKIu-ZqgetcRP4L7p1GuPYOq8Z40WxvTnqG4cvMrb0Q4jmH5K7_Tuctcwwdg28hcGVRxAEhngjhEheNas9v83Kt2eLAXKmU6kBE6cKyKBOxxfECfn5mX2uLOfjy8xKjpmdK139vDho6AgvZdrvkqdkCM5mLEf_INAQyKGoyclReX4xv5sFoRt6Nq4l-GyJ17da5WAgcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: اگر به‌جای خودروهای بی‌کیفیت و مونتاژی چینی، کل یک خودروی ژاپنی را وارد کنیم ارزان‌تر درمی‌آید.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456291" target="_blank">📅 22:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b809380.mp4?token=GbzcFoHGI2ZP_aQM7KpVDJDGTY9rp7kmXiusDwYnHz8cIJwgVNvHJYNw-2kTMRSbi9dlAeZWNDCE039bzYNsu75fgzzooIUHkcKyh00TVRYtYhPEK-YA_X_g6HtHWARahwiuh2OkZTaCfAW-oZC-qhTGS6ssIGSbKwWFLnl7qXxybjIr_pg_Clh06KsI4ZMFDft5fQAZclyO9PcL5FylprkT-_rb-LxCaVBFPcfT7Zs-9qKqKzqhRdiGJ28vwSWPqklf-tDMxkHXjU_76sfizjFDjL2gUgt9_NCi_oVRxzU3w8Gip4F0hoOaPwx6v6OfGhlBBs6RYppd79tpSvV5-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b809380.mp4?token=GbzcFoHGI2ZP_aQM7KpVDJDGTY9rp7kmXiusDwYnHz8cIJwgVNvHJYNw-2kTMRSbi9dlAeZWNDCE039bzYNsu75fgzzooIUHkcKyh00TVRYtYhPEK-YA_X_g6HtHWARahwiuh2OkZTaCfAW-oZC-qhTGS6ssIGSbKwWFLnl7qXxybjIr_pg_Clh06KsI4ZMFDft5fQAZclyO9PcL5FylprkT-_rb-LxCaVBFPcfT7Zs-9qKqKzqhRdiGJ28vwSWPqklf-tDMxkHXjU_76sfizjFDjL2gUgt9_NCi_oVRxzU3w8Gip4F0hoOaPwx6v6OfGhlBBs6RYppd79tpSvV5-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: خودروسازهای داخلی هیچ‌وقت هزینۀ خودروی پرمصرف و بی‌کیفیت‌شان را نداده‌اند، فقط مردم و بیت‌المال این هزینه را می‌دهند؛ ما باید ریشۀ این موضوع را بخشکانیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456290" target="_blank">📅 22:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32dbd0808.mp4?token=cLB8K5kBcI4GxiI6ERAB8Vf9cRW6oySZhoJOjGgM5n9kskkere5DBhPSH0jQB-3kPJV82hoPoi9qCh13MszFZRePOQ6xj28rmF5vOFvRQSy5kte69bpXtFgrNPIStPeGnklMmYvtl2LrumJCgHkpba9oLlqdf8yMC2nvqgkbtV_h63qpiikFxR7FjiWs0aSLa0ZeojuYfdRrpJUKwyxKeXTJOnHBpkaDnMXSmyKrW2KXIA16GRMAkH4_ELCyrz8cbVOrSn9cXUFOdWJca0aXaXC-waGwdR9cclWE72JPTMVCXXsrlsmVYQLCXAaZVRSoKXdDNNZiMyW_lC7rYWchNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32dbd0808.mp4?token=cLB8K5kBcI4GxiI6ERAB8Vf9cRW6oySZhoJOjGgM5n9kskkere5DBhPSH0jQB-3kPJV82hoPoi9qCh13MszFZRePOQ6xj28rmF5vOFvRQSy5kte69bpXtFgrNPIStPeGnklMmYvtl2LrumJCgHkpba9oLlqdf8yMC2nvqgkbtV_h63qpiikFxR7FjiWs0aSLa0ZeojuYfdRrpJUKwyxKeXTJOnHBpkaDnMXSmyKrW2KXIA16GRMAkH4_ELCyrz8cbVOrSn9cXUFOdWJca0aXaXC-waGwdR9cclWE72JPTMVCXXsrlsmVYQLCXAaZVRSoKXdDNNZiMyW_lC7rYWchNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: اگر میزان مصرف بنزین خودروهای داخلی مشابه خودروهای روز دنیا بود الان شاهد ناترازی در تولید و مصرف بنزین نبودیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456289" target="_blank">📅 22:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=ZQHueCzad5c-TxDLSvUoW9Ql374noqIdvqRH8kBMhBzo12PoM7ISagyjeGJhMQNX84oOu6fbb3LeW9qeuc_ioXu8pyPKMtJtBmuPrX71rmZREPmG_6ufGOVfbox-chNw5u5Ugu4toaOG6nIWaud8yTN8mdnq0_KOmDKHSZScBNzh1gD25kRB_EIBi2qkiPy6zXIZBG5gr7ybanHwE5bvyaTvbJAqshZtFKl0LjculZuhp14fO6xk8XqVPfCm_Q1Vh1qGODpNm6Y9I4CCYi4zD5YSN422wCo5ksecaa7WdkwKdB1Ifmtd1F9LdqCE-zKP8XCxf7GFBokkKX72aSjQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=ZQHueCzad5c-TxDLSvUoW9Ql374noqIdvqRH8kBMhBzo12PoM7ISagyjeGJhMQNX84oOu6fbb3LeW9qeuc_ioXu8pyPKMtJtBmuPrX71rmZREPmG_6ufGOVfbox-chNw5u5Ugu4toaOG6nIWaud8yTN8mdnq0_KOmDKHSZScBNzh1gD25kRB_EIBi2qkiPy6zXIZBG5gr7ybanHwE5bvyaTvbJAqshZtFKl0LjculZuhp14fO6xk8XqVPfCm_Q1Vh1qGODpNm6Y9I4CCYi4zD5YSN422wCo5ksecaa7WdkwKdB1Ifmtd1F9LdqCE-zKP8XCxf7GFBokkKX72aSjQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دولت برای بنزین چه برنامه‌ای دارد؟
🔸
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🔸
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456288" target="_blank">📅 22:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
منابع عربی از وقوع چند انفجار و هدف‌ قرارگرفتن مقر نیروهای وابسته به عربستان در شهر مأرب یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456287" target="_blank">📅 22:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhI4Kj41MkRT88M1tAp1VRCCNGOzSZin1QP7onoCqPyZ3s3naiX_oZbTEaMDEh01sFGWPJ9dTCwYFcQUmh41QbGVexRL6ypY_NnSGQ7ojRHmSh2yMphPT8plg7ONI5nkLw8YQ629qI9QddNAe0yFbkd09qPAue_izP8lielYbrV0ZErAWoyohHZYp7p_nPzG0UKxr5LMWOE3vC0vjXZyLkTZZOHn4bVNWQ5jdlDonVwC3cDX_Pj1Ff3ui8ViWIWYooJQ86GFXoLOttpNYW6bUEQwFeRww0uaCwML1q6RhRQiTX9Lj-igjXJp-50SN3qHHAU4pW12M5Ii8jvb_Y5_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ وزارت بهداشت لبنان: شمار تلفات حملات اسرائیل به شهرک‌های «انصار» و «دیرالزهرانی» به ۱۱ شهید و ۱۹ زخمی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456286" target="_blank">📅 22:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456285">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaEMuaFSxpAQsfJZ46md9qwmZq4hlhBt1ZzVmvrOyaKsxbmNI3bwIyQAwwOGcZKI_NTOQiKPPH3-jvR2ictOZFaU6WTDRBkiZhl78Bsrj_68uJVyGHrxlP6NyToDex-Btta9rgD4O3eCGeolfFoTrzdJ86ZnX0nP9FNjpncNwyBIJcCor20BmhpBdNGRWMhziKLmyB5R-G0gp4m0tWGkz5xCnv5wx-yIbeGZJLSoDZpgmq5hQAFSiwRTqcfcZBjAHRi2-Uz3RguvO0S0H3q-S3tauOo6ca3ALiM__aKzByznRTHoR5iS1NRHz9rRJEckjYDH-SW7OcjldNphRW9UkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پسر ۱۱ ساله پس‌انداز ۲ هزار دلاری خانواده‌اش را خرج بازی کرد!
🔹
یک خانواده در کانادا پس از ناپدیدشدن پس‌انداز اضطراری‌شان متوجه شدند پسر ۱۱ ساله‌شان بدون اطلاع آنها، بخشی از پول را برداشته و ۲ هزار دلار آن را صرف خرید گیفت‌کارت برای بازی کرده است.
🔹
این کودک هنگام رفتن به خانۀ مادربزرگش، پاکت پول نقد خانواده را با خود برده و در دو خرید جداگانه، هر بار هزار دلار هزینه کرده بود.
🔹
خانواده پس از اطلاع از ماجرا برای بازگرداندن پول اقدام کردند، اما با توجه به نهایی‌شدن خرید، موفق به پس‌گرفتن وجه نشدند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456285" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456284">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phRzvaC51pi9LxcONITzIAMB-mQE5vRYO87FVH9sX2V3aycW3eOtSJE_EEEhPdPJ2Xv-QDpPibPCswBqLP640vgOSngpKNfm_2cn3YCDcEdOzXoG7x8NwqMNo8bb_O8H53h0ok0c0B2VkZkJgi-i8T5ByQOTcZTwN9vCDZ-cEvh59XjY7K1mf8CC7SoR6xG4MN5IwTmFIhdr7nmtUlrm33GPbCrhpNDNV5oJUs2A63XxLg_ft8Z3LX77oeLcf-KOgHuFtWikHB15TQoKd0c1D3A9BdAAKUDtVcPfzqTwD8rbJzoFQK3oYLoe4CdKJeXRr0NF-pTw1iFRsYDgcE60EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا به پایین‌ترین سطح از ۱۹۸۳ رسید
🔹
ذخایر راهبردی نفت خام ایالات متحده در هفته گذشته با کاهش ۳ میلیون بشکه‌ای، به ۳۱۶.۵ میلیون بشکه رسید که پایین‌ترین میزان ثبت‌شده از سال ۱۹۸۳ تا به امروز است.
🔹
بر اساس داده‌های وزارت انرژی آمریکا، این…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456284" target="_blank">📅 21:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3qrUi7-64R4vYDBNTqldp-8VqmNSeraWYl0eB7XZZeHIY22BFiBgfqiZm1sg1YUI7BdQnDA8gPXuo8VpJoUTEgrG3qbPLB6Bje24VQVF3LYY8NSQFEgt1d7zwJyLS9dIccKX5jIC2cHDhln_QKzBsWW4LaYhRCCRdcSlqUMGgVbdzwlF1zO-wGJ3HahuWKfmPb0GPyiOJgvBWw3Zn-lslvj_vL3CNEUpTtGgZWUVfI0pHvUCkOC_2dfkimYG8mZo9CVNWID_Zguw5Rphzl3AExjQvgd_As0rcCYsyWoU8IwRdtttnfhief9_awPc6CJSjUt_pXvDVlD-F59Y8iv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم پرسپولیس به شمس‌آذر توسط عمری در دقیقۀ ۱۵
⚽️
شمس‌آذر ۰ - ۲ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/456283" target="_blank">📅 21:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cdcc495a.mp4?token=k_j18fKSAVr71t_Y9QUc7DV4bcWsBuOVVreNYxwfKF5K3W37GvnmZBFlovmogQA7kb8diXu0Ia4Ir5OfV-NjgRU-TtPTKk3bOQrykfk09U3yXJxUvZQgupSbiSEjPY06XJ-DxxLME_bAHZCRwpSBIdd1F4N9kWkSJlkMbPTLCLjPmjf8Nw_KshDc_FI8B3ywb-miXOth7bQnwd2bwQbOdfi3L4sikJeVe2mdbNsMY-G7V9B29vVsa-BK1jgkikudAtoVmkZG49IWmsxytH1WrKEXZUHTi-LeBEb_6NqQpwL23hoJ4Ev62_uL45U2Q2VnXUg8D_vqmuj4X9YHOpF_xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cdcc495a.mp4?token=k_j18fKSAVr71t_Y9QUc7DV4bcWsBuOVVreNYxwfKF5K3W37GvnmZBFlovmogQA7kb8diXu0Ia4Ir5OfV-NjgRU-TtPTKk3bOQrykfk09U3yXJxUvZQgupSbiSEjPY06XJ-DxxLME_bAHZCRwpSBIdd1F4N9kWkSJlkMbPTLCLjPmjf8Nw_KshDc_FI8B3ywb-miXOth7bQnwd2bwQbOdfi3L4sikJeVe2mdbNsMY-G7V9B29vVsa-BK1jgkikudAtoVmkZG49IWmsxytH1WrKEXZUHTi-LeBEb_6NqQpwL23hoJ4Ev62_uL45U2Q2VnXUg8D_vqmuj4X9YHOpF_xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیویورک‌تایمز: جهنم در ناو لینکلن از روز اول جنگ شروع شد
🔹
نیویورک‌تایمز گزارش کرد: کابوس ناو هواپیمابر آبراهام لینکلن از همان ساعات نخست جنگ با ایران آغاز شد؛ زمانی که موشک‌ها و پهپادهای ایرانی پایگاه بحرین را ویران کردند و با آن، ستون فقرات لجستیکی ناوهای…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/456282" target="_blank">📅 21:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBJ-Oz-o5MBDROzLE5hpjNyVfVE6LJEnvKp6REOiL2PvqdA8bpsyA-MBPEosXPjv8B4p7xyl9Ly9rW-3KiQ1Sx0vKoMzZreIE4uzErfIgQFjHXfSq6y6SZSDC9EVuHDQujlMMCGZCBF8AE2EpEdwraasZIy_c4Frf_3Byk1p7fGjb1f-JL2FNCj8lkIsv63r4HuR9yROpltTXWVF2NueqxFAuWZdI7t7JMRW0FLCuri0nKhdgkoQsm66-fGRX8L7UrC3apItoZVXRUbiKiIZYUayhnUfnVDCJDzoFPaq1swTumcHCSeZz-7cUAREqboAQTta25NByEpVnU_aqGILkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: در کنار حزب‌الله لبنان می‌مانیم
🔹
وزارت خارجۀ یمن:  سالگرد پیروزی حزب الله در جنگ ۳۳ روزه یادآوری حتمی‌بودن پیروزی با وعدۀ الهی است.
🔹
درحالی‌که حزب الله درگیر یک جنگ سخت با اسرائیل است، دولت لبنان با رژیم اسرائیل دور یک میز می‌نشیند تا به حملات صهیونیست‌ها مشروعیت بدهد.
🔹
اگر وادادگی کشورهای عربی و مشارکت آن‌ها در ائتلاف اسرائیل نبود، این جنایت و سایر جنایات ادامه نمی‌یافت.
🔹
یمن بخشی از نبرد گسترده برای مقابله با صهیونیسم است و ما در کنار حزب الله و مقاومت لبنان و یاران مجاهدش هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/456281" target="_blank">📅 21:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O09QtzKRKN0Y-ldGahffVLm15X5jFdLkzSf7TvwxTu6_ktFnfvRYFTIz65wHmY2GVio10UwqsSlKyq1L_YYiWVMIdNZvSv3B4SGYTHI9ts-9nbpd6FMHEtovroEyvqhj6O-c7W6XSY5YINce-6OeOe1YLGy8Xk9sVSWxiLiO2tTR0vK3BFiwY3C_C0QDTdFFkmDbgtDvMOwtC0riik5A-9gA-t34n4Xjonly9O1IzH6JBAYc5M-3T3Vpe82QU9IVkGBvH6kGyONohWAB61dhCMQaSN_gd5LF3VLnv4phB3qawhp_-u775z8mQm-osLHxKO3W8PknN7eq3fHcQtWjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصرۀ دریایی علیه ملت ایران ۱۰۰ روزه شد
🔹
آمریکا پس از تلاش نظامی، می‌خواست دریا را ببندد تحت عنوان محاصره دریایی اقتصاد ایران را متوقف کند. ۱۰۰ روز بعد، ایران هنوز تجارت می‌کند، کالا وارد می‌کند و مسیرهای تازه‌ای ساخته است.
🔸
در ابتدا باید تاکید کرد که مسئله این گزارش این نیست که بگوید «تحریم و محاصره بی‌اثر بوده است». برعکس، فشار واقعی است اما چیزی که آمریکا به‌دنبال آن بود، یعنی تبدیل فشار اقتصادی به توقف کامل تجارت ایران، تاکنون اتفاق نیفتاده و همین‌جا داستان ۱۰۰ روز گذشته آغاز می‌شود.
🔹
آنچه این ۱۰۰ روز نشان داده، بیشتر از آنکه داستان «شکست محاصره» باشد، داستان اقتصادی است که برای زنده‌ماندن، مجبور شده به مسیرهایی برود که سال‌ها کمتر جدی گرفته می‌شدند.
در صدمین روز محاصره، یک پرسش ساده بیش از همه اهمیت دارد:
🖼
چرا اقتصادی که قرار بود با بسته‌شدن دریا از پا بیفتد، هنوز حرکت می‌کند؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456280" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFq5-u317hzw0H24x8g67oale-bzy_KfEXmUir0EMZ9F3kXNBekU0PNNbbG8J4sPly5H4oc68Gf-fCTj6L_ddPFi1rkYPskEO07bgBNQN8biRsFWUSj0au1bf8_ZTu8VRgojT6zxSX02AQs5q4MmsVaCtzGNTfCXJBYnid-RtJIxL3-QtCSlcxvAvVmQeUSVPSGjppSmSsUyumEdEFK2JwgnZgMHcBsRLuoO4ovltjrkrNaHFy7Pf6fpIMg5Mt4WLTmjFWs7BqAx-eWcPaT_WNl_DxpBXgMlpP3kKlR6oryDwFae9gfGWYroLmMloQJ8Lpd_qhlzOpTwtZXwtvlfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌چی‌تی سناریوی قتل مادر و برادر یک نوجوان را به او داد
🔹
نشریۀ گاردین گزارش داده که که نوجوان ۱۷ ساله‌ای به نام آرچون در ایالت ماساچوست آمریکا متهم به قتل مادر و برادر کوچکترش شده است.
🔹
دادستان‌های این پرونده می‌گویند طبق تحقیقات او پیش‌از این حادثه از چت‌جی‌پی‌تی برای جست‌وجو دربارۀ داستان‌های تخیلی مرتبط با کشتن اعضای خانواده‌اش استفاده کرده بود.
🔹
آرچون در قالب داستان‌های فانتزی با حال‌وهوای رمان‌های گوتیک، شخصیت‌هایی می‌ساخته و با روش اینکه «اگر چنین اتفاقی برای فلان فرد بیفتد چه می‌شود» سؤال می‌پرسیده تا بتواند سناریوی قتل دریافت کند.
🔹
گاردین برای دریافت توضیح دربارۀ این پرونده با اوپن‌ای‌آی، شرکت سازندۀ چت‌جی‌پی‌تی، تماس گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456279" target="_blank">📅 21:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2c5c57d6.mp4?token=kWWCS_FQu2dP8luKd684rl8nJIVtLQ3gs9Qr-efMVzrN2dhQNMIPRQtZozzX2EIb-iW0XA5UJDMvm1GRzB-2UY4sHP9GrFiDKe-43dalCBez5FruZZb2KB8rhiTtSfTdgAm1wW6rpeY3pzSLXz_LuL3qz1Ucy_lTX9cbmxxIQ5jvcT2xVqql3p-eroSkP5Vw1t7rqmID9cCC6RH8WBK4Xw3b_AtPVJCTAhjPbPTvJDkdwopgkpOdkEuMY18glB_7i5quQM2_wQo07PmfgP4PBAk6Z9phW34JIjCSwPvNjXzk6v0FH6SVzO3uYTQMhRV-Y_F92DVjFSROIBL07s39jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2c5c57d6.mp4?token=kWWCS_FQu2dP8luKd684rl8nJIVtLQ3gs9Qr-efMVzrN2dhQNMIPRQtZozzX2EIb-iW0XA5UJDMvm1GRzB-2UY4sHP9GrFiDKe-43dalCBez5FruZZb2KB8rhiTtSfTdgAm1wW6rpeY3pzSLXz_LuL3qz1Ucy_lTX9cbmxxIQ5jvcT2xVqql3p-eroSkP5Vw1t7rqmID9cCC6RH8WBK4Xw3b_AtPVJCTAhjPbPTvJDkdwopgkpOdkEuMY18glB_7i5quQM2_wQo07PmfgP4PBAk6Z9phW34JIjCSwPvNjXzk6v0FH6SVzO3uYTQMhRV-Y_F92DVjFSROIBL07s39jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۱۶۸ به یاد شهدای مدرسۀ میناب به خیابان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/456278" target="_blank">📅 20:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMogqAtmwgTjep7-MajQooKHV_zcKKhcbWQOwZ6HJCTLam9c0BJtsQFwqF6sIB8bvW2mrAmdNBOUv0WvGrNdWKDW-AcAx4fJi--SRq-ED_lHTpQCJ-Ke9-yKcF4p2bYyjfeWPYh2yVVElWXeK4ZpcZHfNA2C-P0YGISWwA-ipfULzqpffCtCr-_2675FVUebPCd9nbov2RE7_oXjcsV9bMgIVK-R4Tzuv8C8DIqsE-GhGELibb6ADkuo8TdocgzuR1QKf1Oh628R8Id02NwVBq4CkQlSrLwxe4V5CTo9K2aFkqbVRLIjrWWsdB24Vb9TziIPa04L3t3t816uENUcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpX5c9IIdAqGpnRIRNS2bX1YCAui2UdCrw1e5mUj9AuZ_BQABeWHlwRvSPtb3Y5fAr-J7xVHTvIiwoJ-oYjprAixEYGlqKCvmKahoqHj1d_K7bmhgprQ_DLYdHqL5bXHzZAvellfWDqPAqhU00WNMMYRt2nkmpj2_TeIHfu23Bu-oeGUtxGa-WT7SPelqop2iv9kCux1eRsUzvzzDwZFBnhAKzWqudHYwWO9p7Y-uW63A2FuGqMKJHHzuEDZauwjveUnPZUxVBX5JTzWRofWX3PVhqa9pC8QGAlBU_GQvAAb44YOsFMU8Qu1vjw-SX3ryC38YEy7yNgL5XRKfECUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_SZBMNVfkeyQDjy9AHlHaedkVHGEJU2LaMQSwIM-4SP_oN6wpshWHVx7-v8a-8KhY0IMgdhN7006mMW7hXYRxKrc4PrQKE6vpKlW4movxQnoWJDBpQOHO4hhCk1a0aKPKksmnVM-nZ4kZgxYQ5k8lT7J_OJ-Uxc_AY8paPEu6_8QLWYdAA0BwnzxU_F7WxfWcd02ICaSvkf0WlOld-Bq4s1QwN1n4Ah4ohYORh-jU1ALlhAZarABrqlg8Grv7UKecgjBFV5EjqrbA3Yg7md1F_RYwP1FFk9k5KP3fz752vHPjv8j9RwRywdQm535DyRsfMAZOGgx6G5WLKIqTBQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INfJ46aie5_fz3HCTzFxODFbONwuI_1-DUURgONjNGEhtOSjR0Jn_4jWU2ARY-UWDG329Yq79f6ZIymMXnc7bmIxhX8vDtd3NzrZqT-4hhMALwZFCaWaKQCsDTdi3DpIMYj5YaPkr4dH64j5CdsqI_JWHdcEhJOJor2ytDH_ghRDkkggEKdu86qSo8Q44B2Rh03w9_8jY0WJykzfj4UPel4GIdztOD9V9arE3LsrvII_xdw1U0Al_FXSzlZyps7GeA9KH0cO3W0N1iIJhUlka7Fpj6aTMTFQ-4xQbObVA1_2c43lR6Rbkc2uoAxRRp74GCKPU6SH1t26-F15WD2O_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vfn5aNsl_5sbaL4b5blmGUp3-IbuPX0djSP9LDBM5uksWpBfXAsX86ljLWFdV3O3nhkxGd2Ro1m5xQgBPgeTLN0EFshq4pijKGOfSf_unj9Ceg9LtL-qnBpRJhhCmPhy5RPH8I2YE51UTK-9dcobtsivO8Q2tzD7DugiDGX1qA1Ok-Sm_ehJ4kogrLEzVdisRJbm3_W3W7uXikSmuWoPqe-T-rfM9ZtjGJThwLf--Ncxue_J9e6gyMeqSz9N1mdB4RKN-8t6dF-tz2pCJOi9--znkMciedXVwivIPpL4v_miJw_ozxNdGPrCNDgauUcaGhvxv93WQ5Mnblt4NelCFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مخاطب رسانه‌ها در یک‌سال اخیر چه تغییری کرده است
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456273" target="_blank">📅 20:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEgtVPiKgoYy4Z3q1aEGpEBM5Xrpd-H-Z_4lMr0CPqouiS0QpE99FhtlowaXJec1wrNezxXamuBcvbJDC-EXEJ3kG6pESYgUx7hrmb4iRoSbFPPnvQTfJFZu0x2oowldGtTE2Kd9B8Ub2gQWEmLVRU4ltSDtYISdklHNtm_CeellB4juDLbSkeEBZAubodNrkednrJ5N6yGm0h0fg_wQuMdarUTksabhM_SVc2EAM3ylCtDoCsViGuypDALAIWqa1gKVPKxBJY3nd7etU9Nb1_-bvr1iwyd8JGcqTaEGiDSC9ka7vo2ipFt0vQhEYgAYMZ-_NUT54Qc3eyOdvplelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توسعه شبکه ارتباطی ایرانسل در خراسان شمالی
🔸
با بهره‌برداری از پروژه‌های ارتباطی ایرانسل در خراسان شمالی توسط وزیر ارتباطات، شامل افتتاح یک سایت نسل پنجم در بجنورد و یک سایت نسل چهارم روستایی در شهرستان مانه و سملقان، دسترسی ساکنان این مناطق به خدمات ارتباطی پرسرعت ایرانسل توسعه یافت.
🔸
این مراسم، ۲۴ مردادماه ۱۴۰۵، با حضور وزیر ارتباطات، استاندار خراسان شمالی، نماینده ولی فقیه در استان، رگولاتور ارتباطات، رئیس سازمان فاوا، مدیرعامل زیرساخت، معاونان سیاست‌گذاری و حقوقی وزارت ارتباطات، جمعی از نمایندگان استان در مجلس، مدیران استانی و مدیران ایرانسل، در قالب جلسه شورای اداری استان خراسان شمالی، در محل استانداری برگزار شد.
🔸
در این مراسم، سایت نسل پنجم ایرانسل در شهر بجنورد، با اعتباری معادل ۲۸۳ میلیارد ریال به بهره‌برداری رسید.
🔸
همچنین سایت ارتباطی ایرانسل در روستای شاتوت واقع در دهستان شیرین‌سو شهرستان مانه و سملقان، با اعتبار ۱۳۰ میلیارد ریال از محل منابع USO به بهره‌برداری رسید و ۸۹ خانوار با جمعیت ۴۰۲ نفر را تحت پوشش شبکه ارتباطی قرار داد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/456272" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA15_DHpWy_iwzefbxGe_1Ieu2bA5Vk-Ob5RK7VA1z_-dmqr9MB0QEK8AHwy3BS9CxGotYLqbQ4WGv4z_R2Y12Aa9h63Cf1qLd4WoIo4iDuPn2GKLiUhaACzMggfpULd1GQ7Z9t_EKaJvx17HInImZYP-Ta2P30dZhX4Sds9pBxdXSqs6Wzoby4k-4qlSUlO6fVrr3E9xzLhMT3oglBrH5d3tefDy50ctgNyWvZP-ilFzEel8llYqQJ8GJRdhXJxG7jNfxKnpPVsD9jd5XzXDFnhkK9i9UVBm4L3xIcV74FA3uWbdulcMLW2_S3bGR3paM4h1aOaufZWXHeX7Dz1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۸
🔹
ثبت رکورد ۷۲۶ همت تامین مالی در سه سال توسط بانک کشاورزی
🔻
حجم تسهیلات پرداختی بانک کشاورزی با شیبی صعودی از ۱۸۸ هزار میلیارد تومان در سال ۱۴۰۱  به ۲۷۷ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته به طوری که از سال ۱۴۰۲ تا ۱۴۰۴ با رشد متوسط سالانه ۳۰۰ همت، جمعا ۷۲۶ همت تسهیلات پرداخت شده است.
🔻
رشد مبلغ تسهیلات پرداختی هم زمان با رشد تعداد تسهیلات، موجب شده تا متوسط مبلغ هر فقره تسهیلات نیز به طور میانگین سالانه ۳۵ درصد رشد کند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/456271" target="_blank">📅 20:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/456270" target="_blank">📅 20:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
منابع عربی از هدف‌ قراردادن مجدد مقرهای نیروهای وابسته به سعودی در مأرب توسط نیروهای انصارالله خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/456269" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oelKoekKluVD2HgjHLbPJd_EbAMI7CNgZbNPR35F-iKpYbGkewC4S_QCIVQXLVDAtv1HmT5sIZpM1oXjOMHWSxY-b8P27cxOCIqFRlMxT5Cd1xIR_BdpIFzt7r35Ls4AkEB1mVDM-W8m20z0W_dqHWwpTi2JApsbq7oYJ38uRnfBsb8edFbcLb_JGlrOQYqImOaRgiJlJWh4-UKZCSW82zsgzi6qaICwat5zo_orWUw8LOYgRKZTsPLtb9sK-YDiprtYENzz5A9LytxJG4zhQFGkQckm9k1neUaHvi-kHkx86RR2Tbyz6bZp4_sbc6VuRiEmbRPfaJLn8LOJsrdLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دستگاه اطلاعات عربستان پیام پادشاه سعودی را به الزیدی تحویل داد
🔹
نخست‌وزیر عراق امروز با رئیس دستگاه اطلاعات عمومی عربستان سعودی که حامل پیام پادشاه این کشور بود دیدار کرد.
🔹
علی الزیدی مدعی شد بغداد اجازه نخواهد داد خاک عراق به نقطه آغاز هرگونه اقدام…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/456268" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجار بمب در مسیر تانک اسرائیلی در غزه
🔹
ارتش رژیم صهیونیستی: یک تانک اسرائیلی در جنوب نوار غزه و در منطقه خط زرد، روی مین ضدزره متعلق به حماس رفت.
🔹
در نتیجۀ این انفجار که صهیونیست‌ها مدعی هستند تلفاتی نداشته‌اند، ارتش اشغالگر شهر خان‌یونس را مورد حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/456267" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tctossU_Fm5JArksudrnf_IvI_bTQ80dw9H3Q9TxI1SFcYqBza6RqH2O9D6CH2xnvwW_R-kiC4y_g_tkW5U-gyRhM5tRvu4IFPpc7b8fAnR3TUZvyc5JxEDJNamQlF3TsY7JSsA-eA1CAbVyGic9gnuj6cyRXSd-WEJdaGATfT-9kHT3Y5sjPcxuheDbADbaZnJxflC7fDvup22d5U1Uq-lT6v00CGOzzX1SHhS9sOHLGimDqYkJKyiSTa36cP3oljlL3E-n9lh8kKHSnYMhwC0N7EKhIWMe-3chofIbTNa-k06a9TxccxTBU4CVxxlOV4sgkLAoHXzIl4PDrIKpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmffCAsaOFwUi4NAXF4Wxb7-OQrD8SKXxbdEZ7Aw4bI5VCa6E7gBNqrDRkMkhPYWGW3bsL3Qx7LoEiScHbeTrwLnWy--5puEYtfJwTnyWX9S8fc8fnUdFnHim1kK6zyrRrj6HuaYncAz4nPbkVDtvwhpeBJZPMWBCpKPcdgtbQqXy4xtCDGx8buQHIl1RWL4JrGy9l8Orl3UkFG1L2p7hgQcA3ohQSDWn4IrX0NJ2qQBHNLdH_3nPSfEbyCmtO2535RA67zP9UxDmkeROzoFemfsDz-NFdnd7jJYEX-Xzf7DBNUIVUePeGrICYo95-Ody57zGXpdvzvC6-dP0TgGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQZCRGJ3iDvklY0Olr9wpmmStLpkLcfuTsa355Qndm-3LITpyvPwn0aLRbMTBQY5oaCcp4dmDeJiVjF3FRoXXWsIp2MssTarZBkjnpljki9_gKj-uGob92jJmdPF_dIBCgETJoEXSkfjXMsu0bbLMXUeILydGpNxLt4JQu2JD_QZgMq3iq8vwqnbxTcdSTraCK4oeqpViLd4Xe4nbiKM7HX-zi3odzxEwTT71rfS1Lus8-Ag5t21NdroCLYbsAZMf6_OamEhw-YJlqIOb1IOv6DgtxGOODqQsm1RTbpf5sT2T8C7--GfzSs-UZLtXz8_bdZVNU57dxR_jnjGvR85gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFruh5MF0jd2iBsMkaOfRsQs0SkEzpsVBpzMhFyQr0J6yNj1Vi_Vx-emWR1q5rSuiftlnUqklQGnJAzx6mMPvQYwedYzDr7ssU3BhgOPZEV3CrXyZJJYR33tDErPHOU7SuCl11glScaUQrsm-w5oXOzHzd3GFGI9hbXvO177wEy8qgCK6Fr-CO-sRPckMshu9Vl5oQyUzYQ2L8yGSk8IEzmDFyO2mRe4b1ZennWRwJXYP4eNCXrYSaw2j8X4-rkL3eYM6WPOnJlkiVF7b6YsiNYH8N44MCGrxUIQFvdnrmevyWzE9EhlbvxLjoKe9kV7FV_xQEUS9O_xFLo3YKE8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UaEmErjgax_XtFgbzsi1rYWRHUCi3g08CIbEqCAZHxBaA-rvw3XzfjmuK4xi1G9TuG_yfUHdR7Dx56LTe5xwb_-SkEOnri-TtHWu1cPQ22l8UweYy4Kb02DWecZ57sa_KUPEusVmpglYGg2HJOfelPGdbFmMSEofKpJdu2XbPB12F8fF7EhsW6122EgWvXz5vt6paPCJpPvF4Q8TeOt9reLGf3FgS9EyU6DPQWrHhiXYnyOuKFcDZQmXAbOfidAfH6h02Ur7ERMkomVjUQtQ5ayijYpSL7K0ad7a6ITZso6ftTTPsT1-zC2ehQ8c5y8iMJ72qmLrF_t23_akdONKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaZ4b9iFxjhQVPypfHojpbIw_EDBX3xLPjC4__mOvedroqAfcZJGRrsP8IV2kMzb6lwsmWv9RKK1TxxaTyharIrHAaKEYIBXn8szAqjDOKgagy-2uUmHH1eLoOfqH2HHuUHTMPLalkLLHBbU6TrdxBXp3J13LJ1FHsHHyjyUGFPMSyYoB4-ZsYRaGj7PBz9V_6OSXYfFXBQsaWS0hkOkwzM563ROXAbnV2thYZyOh54-KopilcN50fyBlMEH074ZEIPPUDbGWWoMdV0PfM4KcgRZjqYE5iEOhgNW3VPnp93Ya2BC7a1WWwiM4pJKSJFKlUkMpH7hdW2pMN2AvBeXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRikCJ8lGyP1QXSrUkRh0XzoXL3VfJ02cQTDzRrowI9NLozNs8fYnudl7sPUnJdyRGAD6fF712BZpv03vFtHCWEgfo-eJk3Rs0FBxBkffnF55E6YiKznmuYRBw5AZEPiaLXCy8U7W7TsBY3uvIM0zQ1EkNvmwOvf_jwItWNliIzZNghCyLkj2PRvrUe9QvjJQ851-MxHlWrfZSMmUnTTsRaAdO_IaH97zjOq6Pe9_YElBU-yD0mbSNDQSnSn0Y7j0xmRjyMQnwlnRDELMcMHnZCW1m9jMIYwAYmXYU8hGdX7TJzlBMOHxwWVD61v7jE-Tg-_M3bNSVePCPYvPzZD6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس دانشگاه تهران: کسانی که در سطح دانشگاه هنجارشکنی کردند، احضار شدند و شورای انضباطی به پروندهٔ آن‌ها رسیدگی کرد
🔹
به‌طور خاص ۲ نفر را داشتیم که متأسفانه در اقدامی بسیار زشت و هنجارشکن به پرچم مقدس جمهوری اسلامی اهانت کردند؛ با این افراد مدت‌ها پیش برخورد…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456260" target="_blank">📅 20:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1130cd59.mp4?token=XIUBk2klwwS6sBBiHCYGRtb1JYyeXsJ0_dbIIcOkaKdilzL1InmGdicTCB7EOjn-U3IeKAzWF-FZfZDWE6FvCzPWinRfxbXVqQ8J3rsWsnBnuHtGlbFoMyIsLpir-Tc95p9ho7AldxKa10nTxCp-1cBC3jzuWqR61qAbQipiFOfxOk2PRO-X0-jG-I6fOwYEv4v4g3Q2ytj4hVAaZ6gDN73syQcV73a51leuC63cZ-OpC2kDMqAFpIGUELnDBvjroZBZT96-RRxkGOQpq-gPFUzE9vsQSQCJxLs0n-bQLgaO5FoRd5bpp2Im_HMfTh4s3oIRdXjD4gt5M_QnBeZ2gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1130cd59.mp4?token=XIUBk2klwwS6sBBiHCYGRtb1JYyeXsJ0_dbIIcOkaKdilzL1InmGdicTCB7EOjn-U3IeKAzWF-FZfZDWE6FvCzPWinRfxbXVqQ8J3rsWsnBnuHtGlbFoMyIsLpir-Tc95p9ho7AldxKa10nTxCp-1cBC3jzuWqR61qAbQipiFOfxOk2PRO-X0-jG-I6fOwYEv4v4g3Q2ytj4hVAaZ6gDN73syQcV73a51leuC63cZ-OpC2kDMqAFpIGUELnDBvjroZBZT96-RRxkGOQpq-gPFUzE9vsQSQCJxLs0n-bQLgaO5FoRd5bpp2Im_HMfTh4s3oIRdXjD4gt5M_QnBeZ2gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به شمس‌آذر توسط محبی
⚽️
شمس‌آذر ۰ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/456253" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va34oLogas1_sbVEJCtxL55OrCcSF7dbpffhvCftjMtoNI3dIayoiu3j_gvJ6sfPTKmvqKvR4wG-ZHWBULNV2ZCZg-3wrn-tD4AgMJCm9gykFKg6tBZBH00BMQu-5dAnL0nGw6ZIWliVyeNQu9IG_jLRL2-vG3tYIZ9uaIA-gzSi3QDlTEDRTtdGWGQCRdq11IvwAVwJRQEWcKngeTgcfjOEpDxpRm4Ii4lNbgtTFa8HKomn-578tOvvx0jZRQyvJYPzfdioaZrKQ5iWXzvaRQt96CGjDASIaonqWr2iQaY3GFmx9Lxqbcrt9tCEAm-04AXOtasLBOncbgZ31SsSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد عجیب انتقال چمن آزادی به اراک
🎙
رئیس هیئت فوتبال استان مرکزی در گفت‌وگو با فارس:
🗣️
مدتی قبل پیش از شروع مسابقات لیگ برتر یکی از مدیران پیشنهاد داد که می‌خواهند چمن ورزشگاه آزادی را به ورزشگاه امام خمینی (ره) اراک منتقل کنند و چمن ورزشگاه امام خمینی را هم به ورزشگاه ۵ مرداد اراک ببرند. وقتی این مسئله مطرح شد، من به‌شدت با آن مخالفت کردم. گفتم اگر چمن ورزشگاه آزادی خوب است چرا خودشان از آن استفاده نمی‌کنند؟ اگر این چمن اشکالی ندارد خب در همان ورزشگاه مورداستفاده قرار می‌گیرد.
🗣️
خوشبختانه مسئولان استان مرکزی هم به حرفم توجه کردند با انتقال چمن ورزشگاه آزادی به اراک مخالفت کردند. اگر ما هم به این پیشنهاد عجیب پاسخ مثبت می‌دادیم اکنون تیم آلومینیوم اراک هم مثل استقلال و پرسپولیس ورزشگاه خانگی اصلی‌اش را در اختیار نداشت و باید به دنبال ورزشگاه در شهرهای دیگر برای میزبانی می‌گشت. چون انتقال چمن آزادی به اراک و پهن کردنش به این راحتی‌ها نیست و کاری زمان بر است.
🗣️
شنیدم این انتقال چمن حدود ۵ میلیارد تومان هزینه داشت ولی مهم‌تر از هزینه این بود که اکنون تیم آلومینیوم اراک هم بدون زمین و ورزشگاه خانگی در لیگ می‌شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/456252" target="_blank">📅 19:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18bc020ef.mp4?token=fq_DPR49XSv24kfFdX1ozwAL4iEJjfyt9YtdSazZ5j0s7f57ltNGzwg-w4cFA0dKbzvl3UhSfRbQwlsh4GGcxnddzZ1kV7P7W3yE2LopsCv3iUcN0oydcYNJLyZK_8IBJyr5sgluueNY7bWuxUA2CTqRFyiLqk5K5zpvxaDfSLM8ivVvuWpS7ncemGWX6QjQOXQDarQYW1JHZPHhGZipZCz_jKBxVANc5dwDYSCfCofZrzV-FPUX-zb1481L3jomzI9SuPwNSOoidiJlzp7bZ22EweEz3SQFQs9fjXPeE9Aq0bVs_hkxpqPckfynqfz0BY9hU4LB70i48_zZDiWhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18bc020ef.mp4?token=fq_DPR49XSv24kfFdX1ozwAL4iEJjfyt9YtdSazZ5j0s7f57ltNGzwg-w4cFA0dKbzvl3UhSfRbQwlsh4GGcxnddzZ1kV7P7W3yE2LopsCv3iUcN0oydcYNJLyZK_8IBJyr5sgluueNY7bWuxUA2CTqRFyiLqk5K5zpvxaDfSLM8ivVvuWpS7ncemGWX6QjQOXQDarQYW1JHZPHhGZipZCz_jKBxVANc5dwDYSCfCofZrzV-FPUX-zb1481L3jomzI9SuPwNSOoidiJlzp7bZ22EweEz3SQFQs9fjXPeE9Aq0bVs_hkxpqPckfynqfz0BY9hU4LB70i48_zZDiWhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به شمس‌آذر توسط محبی
⚽️
شمس‌آذر ۰ - ۱ پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/456251" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqgvE7Jwxjho6365hH2yDcw_9dC8wmTXeZ5KI9FHBnvAGGhlxInBcKHqQ92JiKjMJf_B_xs6qZxqt_Ua-IVd5iCETiAP5x4HuMlG_rFYX8w7CYTobq9YIWqB-avB3VcvMpn5ftqIx3D4HlbMBhHxlFUlFJ9T_4loRQoZJ8bIjUATQC7TIPR3UXHjaBHzrudygEnR3K3u7rF8UARf5w3xNRITiWDYVdqb5FH7IvSP4Hyt8cE3aRZ1PzRe33IJSfxek8bbIMEQ5KsKZqcCRPYii7_itWlCNwDehjAMTU7S8pI3pyvf2mO65WN_VWjYn2GWYSRtdvWkmxgLJhefggvgjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
🔹
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/456250" target="_blank">📅 19:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54eb9c5b02.mp4?token=q2m1LhPLr78ieYU3ATV8cPdvrXMqyZl89tGn9dVl_B7LhqcfRIfGmzrqfw9eB1KgJh_V-FOdIdx6ixF8cSYOx1B2eLUZRqERsTeH9ZnZKhkt1tox_yySvSeH_ZdMvXZaLwrn9u2p9kJ5lciVJ91muEdBD4kv34_KiZj5oksIHDEfcnCtjHAA35kxzPNScpe2gT23JJi2x2dEpN3DpKJEL4qclgAt3kMMaIHbnO9xcY_UTZtAgdyHwT893fShk-pWyvuo9DVM40XrcCUiCqFeNIT8TrfA9Z0yIIEO3IF7j1wl3diNX_wYy5jtx8VgIqa3i-FZ5-2gH2DXquqlpExQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54eb9c5b02.mp4?token=q2m1LhPLr78ieYU3ATV8cPdvrXMqyZl89tGn9dVl_B7LhqcfRIfGmzrqfw9eB1KgJh_V-FOdIdx6ixF8cSYOx1B2eLUZRqERsTeH9ZnZKhkt1tox_yySvSeH_ZdMvXZaLwrn9u2p9kJ5lciVJ91muEdBD4kv34_KiZj5oksIHDEfcnCtjHAA35kxzPNScpe2gT23JJi2x2dEpN3DpKJEL4qclgAt3kMMaIHbnO9xcY_UTZtAgdyHwT893fShk-pWyvuo9DVM40XrcCUiCqFeNIT8TrfA9Z0yIIEO3IF7j1wl3diNX_wYy5jtx8VgIqa3i-FZ5-2gH2DXquqlpExQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه تا چه زمانی ادامه‌ خواهد داشت؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/456249" target="_blank">📅 19:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad5513ad.mp4?token=TDdnww7B-39InsmbKvl-BaKGd86y6cQbWhYeoaqUhxhluN1aVd6nfzmKMfA9y6YidhBs3URakX4LhH7Nuq1SLAzgciwp-lnZNN_wmHRSTnv8T2rNEPrY6MZNac9RXDR9wAaAAyhtDQm79qT796dklGOSiUw6gTAcBXyCGryO84zu5wFVIFtgf_rl-EjA0mPooMG7suMWkmDhL2WATEN_edHoc9KdDEprKMpyxR9ZzpGyZzJLRZD8WWMBwFCtFRydtqFhEp_zxw18mNcS7RUxAIUzLjcvZOyeCCOs5XMSoTJaLuQCt2ISmG4IEeccxGYS_vk_duPAQ86FwsBpxWHgSzdfrqKj_IoYLBanmgW1c0TY_EzE89c9LLroxY2dNaUum5JUksywTQswQt6dFTsEYNtM2UmaJ2VO_i1efN4ewLR3WXWEO_CNufupzpgLDiEQ_MJskRLhcyqnPdOOzLSwOZxh-UH-mctT-cKNCPjtaQsah7xh2HDJc3pflIjIP9c7NM_9bBYJ5AEKHuyPvR4sAMK6o2O2F_cuMTqzkb_dKilCcsPTI3esSZYgUiWT_Dm3ZmiKXcu_DrY_B_Nvz3h6d3550U7ggr8dLYECltU9cFdj5W7W0IFirgHWcB8nUcil7mKQBX4wkOLPI9XCMS3sOLfpXLZQqdbWWRmh8LspkHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad5513ad.mp4?token=TDdnww7B-39InsmbKvl-BaKGd86y6cQbWhYeoaqUhxhluN1aVd6nfzmKMfA9y6YidhBs3URakX4LhH7Nuq1SLAzgciwp-lnZNN_wmHRSTnv8T2rNEPrY6MZNac9RXDR9wAaAAyhtDQm79qT796dklGOSiUw6gTAcBXyCGryO84zu5wFVIFtgf_rl-EjA0mPooMG7suMWkmDhL2WATEN_edHoc9KdDEprKMpyxR9ZzpGyZzJLRZD8WWMBwFCtFRydtqFhEp_zxw18mNcS7RUxAIUzLjcvZOyeCCOs5XMSoTJaLuQCt2ISmG4IEeccxGYS_vk_duPAQ86FwsBpxWHgSzdfrqKj_IoYLBanmgW1c0TY_EzE89c9LLroxY2dNaUum5JUksywTQswQt6dFTsEYNtM2UmaJ2VO_i1efN4ewLR3WXWEO_CNufupzpgLDiEQ_MJskRLhcyqnPdOOzLSwOZxh-UH-mctT-cKNCPjtaQsah7xh2HDJc3pflIjIP9c7NM_9bBYJ5AEKHuyPvR4sAMK6o2O2F_cuMTqzkb_dKilCcsPTI3esSZYgUiWT_Dm3ZmiKXcu_DrY_B_Nvz3h6d3550U7ggr8dLYECltU9cFdj5W7W0IFirgHWcB8nUcil7mKQBX4wkOLPI9XCMS3sOLfpXLZQqdbWWRmh8LspkHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۲ حملهٔ هوایی شدید رژیم صهیونیستی به شهرک دیرالزهرانی در جنوب لبنان
🔹
رسانه‌های لبنانی از هدف‌قرارگرفتن یک خانهٔ مسکونی در محلهٔ «الراس» در شهرک دیرالزهرانی هوایی خبر دادند. این منابع گزارش کردند که همزمان یک موتورسیکلت هم هدف شلیک یک پهپاد قرار گرفته است.…</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/456248" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw1sYa3Z0TRnYntJZqFzlVIovmJgsZ54TxTCvz0S8tcMGsfdVh_CgjCpeXrGN3PLj3GByXB1C8eN1J_4QGAnNkUluGC4MMx7KmbwW73cl3PCBH_bD0Kjb5P6iC3Z11QsRUF3hKexiCR4ud1nlBE2twkcJcxoqqD_-K7Tkxb66-ecr4zf9wozg7DqHFaent3jtJlTAobrXma6X3BTocc1kPgbxyKxUaefXsPMYea5B_o70bBDUtMQSKgRJ8h0J49g9NvRiECI9dWQGr0MqgqwfLRVYKEhZSYIeiOJxj8qhbFsJl_dnb1Z6C_47qhD5sjFCNK2lyJejGLjxivhWCnfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأکید مجلس اعلای شیعیان لبنان بر توقف فوری مذاکره با اسرائیل
🔹
نایب رئیس مجلس اعلای اسلامی شیعیان لبنان ضمن انتقاد از سکوت دولت لبنان در قبال جنایات رژیم صهیونیستی، تأکید کرد مسئولان این کشور باید به این سکوت پایان دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/456247" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103ce0d5db.mp4?token=NMpK4Cv0ADtAfxvFkr1rH1_1biLZJ4av2Ib9DQZ5ccDXxsrH0QgxWaLq888G9JiT1E5_IqAEIJjPjUhOBVSC_ufDC8d2ejHBh_KAN667VBNCo806KqNvfSIZyvrBgODNORZsPCgMYggVOAHu2oPv24AHOrvUQ3axWvnE7pO9oFnXlNq7gQ9WDbdiC_gnhlIAFMzKqLjZhFGRZHm8RQYtIyVDYF6CqI0hFO8QAta2gVls88emEHlcDgz0P37G1g1hyWZmXmb9MtycmnOvh7jaTWLuYUZDmjzI5SstPoK29xoFQIrPlwKOjCfnGEE5qdOrCrejXfBtfnN_QJx7dIPD0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103ce0d5db.mp4?token=NMpK4Cv0ADtAfxvFkr1rH1_1biLZJ4av2Ib9DQZ5ccDXxsrH0QgxWaLq888G9JiT1E5_IqAEIJjPjUhOBVSC_ufDC8d2ejHBh_KAN667VBNCo806KqNvfSIZyvrBgODNORZsPCgMYggVOAHu2oPv24AHOrvUQ3axWvnE7pO9oFnXlNq7gQ9WDbdiC_gnhlIAFMzKqLjZhFGRZHm8RQYtIyVDYF6CqI0hFO8QAta2gVls88emEHlcDgz0P37G1g1hyWZmXmb9MtycmnOvh7jaTWLuYUZDmjzI5SstPoK29xoFQIrPlwKOjCfnGEE5qdOrCrejXfBtfnN_QJx7dIPD0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: دولت پیگیر رفع مشکل ارتباط خراسان‌شمالی با ترکمنستان است
🔹
هم‌مرزی خراسان‌شمالی با ترکمنستان می‌تواند زمینه را برای همکاری‌های فناورانه و حضور فعالان فناوری این استان در کشور همسایه را فراهم کند.
🔸
خراسا‌ن‌شمالی باوجود ۳۰۰ کیلومتر مرز مشترک با ترکمنستان، هیچ گذر مرزی با آن ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/456246" target="_blank">📅 19:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH48WJSSQU0e6Esmna_kp9U3wspCAjE50I8j03Okr4eZJJkMNbOwxUqOTKYdBRGIS1u6TohYnuDeoljc2BPueY2wmGAk7LtBPlJGfYP8T3X8SsGN5kdIyvLOT9dAZZZetDe5GuBIfr-ttzDibBMm0crno5xJQD8j2_iWDWGNNKl4iSvN-sIPKE2g2nMOwXPle4za9EtdBssC5Ykmc7w2VHCJHgZ9osGV8YdA0EaAmo6FI3MfbDNxRtv9aApoDuqxbFP-GNMzgJqcBBXecw6FluOd0wAEzBnTdXRjeVXxt5V6ACearzFWiS9ozsIIaHX2GYCKHWYpb75oh7n3QGFUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد پای شرکت‌های نفتی انگلیسی و آذربایجانی در سهم ایران در خزر
🔹
کارشناس سیاسی و روابط بین‌الملل، داریوش صفرنژاد می‌گوید پشت پردۀ تلاش‌ها برای تصویب کنوانسیون رژیم حقوقی دریای خزر که فاقد جامعیت لازم است، پروژه‌بگیران شرکت‌های نفتی انگلیسی و آمریکایی و آذربایجانی هستند.
🔹
ممنوعیت احداث خطوط انتقال نفت و گاز از آسیای میانه که از شرق دریای خزر به منطقه قفقاز جنوبی درغرب این دریا وصل می‌شد، از ابتدا در متن این کنوانسیون بود.
🔹
۸ سال پیش لحظۀ امضا این بند را از متن خارج کردند.
🔹
قرار شد این موضوع به صورت یک موافقت‌نامه جداگانه آماده شده و به امضای رؤسای جمهور برسد و به کنوانسیون محیط زیست خزر الحاق شود اما این کار انجام نشد و اکنون با گذشت ۸ سال هیچ اتفاقی نیفتاده است.
🔹
اگر این سند در مجلس تصویب شود، یعنی مجلس محترم سندی را تصویب کرده است که می‌تواند زمینه‌ساز جنگ آینده و اختلافات جدی با آذربایجان و ترکمنستان، به لحاظ قلمرو سرزمینی، حوزه منافع ملی و امنیت ملی ما باشد.
🔗
پیامدهای قانونی‌شدن کنوانسیون خزر برای منافع ایران در زمینۀ منابع نفت و گاز را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/456245" target="_blank">📅 19:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ba2d71c38.mp4?token=X5hHeysw5tdAJn4vmfimfMmNZGmiWyBreONbDS9Kh4yFX5NWS4dEqOJFjaLDJ8YsrTLSg_G3XxBpgABnut25oOmvnMvVWEYsmw-sBGTcOpD5xjHrODt-9fpiqbqSbsGnUFRZaSEKPvp92KAQkWKUQ63rHNJYF9kbWkSm7di37TAB6koFH82T-AV7D5UA6eu2U3gTx4IGWxp8oWhebBvtrt17AIpthfjjzquhvoisBMLSImetvOmpgaWBZYhUhAknrMKie9rNo8nZD9c2J6LuRmEyg9LYickd6QfqPUx2q8vuq_81w0bMT47VCvaqiqPpwJkA03cBru4r-gJGZy40-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ba2d71c38.mp4?token=X5hHeysw5tdAJn4vmfimfMmNZGmiWyBreONbDS9Kh4yFX5NWS4dEqOJFjaLDJ8YsrTLSg_G3XxBpgABnut25oOmvnMvVWEYsmw-sBGTcOpD5xjHrODt-9fpiqbqSbsGnUFRZaSEKPvp92KAQkWKUQ63rHNJYF9kbWkSm7di37TAB6koFH82T-AV7D5UA6eu2U3gTx4IGWxp8oWhebBvtrt17AIpthfjjzquhvoisBMLSImetvOmpgaWBZYhUhAknrMKie9rNo8nZD9c2J6LuRmEyg9LYickd6QfqPUx2q8vuq_81w0bMT47VCvaqiqPpwJkA03cBru4r-gJGZy40-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/456244" target="_blank">📅 18:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469a082088.mp4?token=T5dHRs4IvXz2JGctNBWANAOrc_JuDkdQs6QuiH5STTtJH5FKT5bbj5L5cBem9n1RyLAjTk7493H8SRErhkC7RMmFZg0ZE0-8Huo2N_wjjoP6Xynq2_cJdaKmLT2eF-BdnUrKpLziyv1QTjiszz_qpkax1uciRqrIuMzxC8fnnB9twK7RsyjC8mIg_EN9DAJn0nFp_BSPVrRIfbUeGouECGmT_mfG5ARXbQ9-f8iZa0fWzDgDgmrmpgBSwC13h1cf_GSNNbWQDByzBL5KbnUNcy_F_YfQcPk4nqJTqTI23fkz6_Iyycs2feIpg54FfWDneN2t5idYD_lVDYGsCe8guA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469a082088.mp4?token=T5dHRs4IvXz2JGctNBWANAOrc_JuDkdQs6QuiH5STTtJH5FKT5bbj5L5cBem9n1RyLAjTk7493H8SRErhkC7RMmFZg0ZE0-8Huo2N_wjjoP6Xynq2_cJdaKmLT2eF-BdnUrKpLziyv1QTjiszz_qpkax1uciRqrIuMzxC8fnnB9twK7RsyjC8mIg_EN9DAJn0nFp_BSPVrRIfbUeGouECGmT_mfG5ARXbQ9-f8iZa0fWzDgDgmrmpgBSwC13h1cf_GSNNbWQDByzBL5KbnUNcy_F_YfQcPk4nqJTqTI23fkz6_Iyycs2feIpg54FfWDneN2t5idYD_lVDYGsCe8guA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456243" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cun1R5W9DVQkP24E7NAPUfqitzgMuEryMr_5mAdwxmohBruWjfYeVOLN9tHSREJi47G7u6q-v1iP010-6TrLYXAjrkvkrZlUBgiqG4btQhck5psEZ3kBMlZyiXXHiO4Z5OqVN8Bv5eEHiqAQI6ZegTLAx60th_oi4vQz5YIfSrn5e6fiTHu6B8KWCkWScO9Lp8G47mcLHbSz9pJN1t5I4aILUEmODsFHLjfJezCXdYt7k45n0ZMRzJKJTTmwyyWRB_iOfwxudJly3fZHcQuvkklLDSQ_9xVzJARF-h9EG9VVhVVDm34WRr198_SUWikqN6csTfaI_XflALVrUzpnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال و معمای وام ۴ میلیون دلاری
🔹
‼️
خبرنگار فارس به سندی درباره یکی از پرداخت‌های هلدینگ خلیج فارس به باشگاه استقلال دست یافته که در آن هلدینگ خلیج فارس در مرداد سال گذشته یک تسهیلات ارزی ۴ میلیون دلاری به باشگاه استقلال پرداخت کرده است که با صورت‌های مالی ۶ ماهه اخیر این باشگاه همخوانی روشنی ندارد و ابهاماتی جدی در این زمینه به وجود آورده است.
⏺
مطابق این سند، هیأت‌مدیره صنایع پتروشیمی خلیج فارس در تاریخ ۱۴ مرداد ۱۴۰۴ مصوب کرده است که ۴ میلیون دلار تسهیلات ارزی با کارمزد سالانه ۸ درصد از طریق شرکت تجارت صنعت پتروشیمی خلیج فارس در اختیار باشگاه استقلال قرار گیرد. نامه مربوط به اجرای این مصوبه در تاریخ ۲۵ مرداد برای مدیرعامل تجارت صنعت ارسال شده و طبق اطلاعات رسیده به خبرنگار فارس، این مبلغ در همان مقطع در اختیار باشگاه استقلال قرار گرفته است.
⏺
در متن نامه نکات مهمی وجود دارد از جمله اینکه این ۴ میلیون دلار نه کمک بلاعوض بوده و نه بخشی از قرارداد اسپانسری استقلال بلکه هلدینگ صراحتاً از عبارت «تسهیلات ارزی» استفاده کرده و برای آن کارمزد سالانه در نظر گرفته و استقلال را مکلف کرده اصل تسهیلات به همراه کارمزد آن را تا پایان سال ۱۴۰۴ بازپرداخت کند.
🖥
ادامه مطلب
را در سایت فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456242" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42121d529.mp4?token=oOjmEAH9s9chb5mtDMk8gt5DmRMpwBPspW0v8-hgnYYLYOW3-DGhzj7ukWslX1IRvj6QVJs9R_h1t8aGodTJKqcHinZoymuK-qGqFNe9UgtrTOxSP4o1ZlBuXa0zd30C6M_Gy6S1Fb3jUkwGFFXqGEPFuxkKZSVb0QnOpneHnNs5m3NDpMV1VnWicDUQ9qMFR1RvDKznOHaatuuKvSEIcxcCitlIRwepnkHoz_0M8w3CVt-sa3Woz3OFvk7Bh_rn4yIUxOTrIPhNtX-WA2iJ6aok8LQoHFEiRbepdRD7FNGJ8VPnoAZZBb1tVYAdNUWh0MTzfdvPkW_4AqOP2d4YYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42121d529.mp4?token=oOjmEAH9s9chb5mtDMk8gt5DmRMpwBPspW0v8-hgnYYLYOW3-DGhzj7ukWslX1IRvj6QVJs9R_h1t8aGodTJKqcHinZoymuK-qGqFNe9UgtrTOxSP4o1ZlBuXa0zd30C6M_Gy6S1Fb3jUkwGFFXqGEPFuxkKZSVb0QnOpneHnNs5m3NDpMV1VnWicDUQ9qMFR1RvDKznOHaatuuKvSEIcxcCitlIRwepnkHoz_0M8w3CVt-sa3Woz3OFvk7Bh_rn4yIUxOTrIPhNtX-WA2iJ6aok8LQoHFEiRbepdRD7FNGJ8VPnoAZZBb1tVYAdNUWh0MTzfdvPkW_4AqOP2d4YYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خیل عاشقان رهبر شهید انقلاب در جوار مزار نورانی ایشان در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/456241" target="_blank">📅 18:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f63d681d6.mp4?token=tsJUM07CEqhzuDw6UXH4DP0xPa85QtLRfvImHwT-95A5cJAtsEwtNEMutNLCT8hWIxVROZd4zMZO0IZ7lb8r8CZViZ4g1x4Z6f5okD-1O-ABsZK8tLFKsvT3iw0rKzZWZbtnUAuw42vgnedA2F5AhEvDb9815FzMshHiZtzzIA_NFU23ijaICs5aGp6ZoJquUBqkVzdhitL_CMOV5-Rw9JaqPXsSppXqJomdu9IM05LE2Cef1WOMzO4Ddby6f-Nfj81mOqV4qiAq1EqdcXWUT1N7BN7URJykQpUoTSMQEhUtlUnPgKE4e-V9b9SJhgw-fxKCK10GvgZ3qByqZaO-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f63d681d6.mp4?token=tsJUM07CEqhzuDw6UXH4DP0xPa85QtLRfvImHwT-95A5cJAtsEwtNEMutNLCT8hWIxVROZd4zMZO0IZ7lb8r8CZViZ4g1x4Z6f5okD-1O-ABsZK8tLFKsvT3iw0rKzZWZbtnUAuw42vgnedA2F5AhEvDb9815FzMshHiZtzzIA_NFU23ijaICs5aGp6ZoJquUBqkVzdhitL_CMOV5-Rw9JaqPXsSppXqJomdu9IM05LE2Cef1WOMzO4Ddby6f-Nfj81mOqV4qiAq1EqdcXWUT1N7BN7URJykQpUoTSMQEhUtlUnPgKE4e-V9b9SJhgw-fxKCK10GvgZ3qByqZaO-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت ورزشگاه سردار آزادگان کمتر از ۹۰ دقیقه مانده به اولین بازی فصل پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/456240" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNkgbwloqmrxxwMbL6IbI2gwc2j0_8HRL1_MFnZ6_abByLkAywkUU1oNHTqaBPiFOFBr9MpVjkvyEC3I_zEaO2tovjFn_Oqb2tI1wt_jb7bDtXADUftG99MzTWcX68DOKtSzKBoEqC-VTSLNw_gzNETEoXBP7jJFddZdTYJbUBG6VS5kBeSFN43n3wv1N8Jm0ZKG_hr0WiiTJMq2WWuw2sa-AnGvsMVTEahxiB8jLkHLDH2Ys_dGSq8joLP49WnqR23n4rMfswSaAKvtxzg7fOg_RMV1d9xfpbXhSs7Um6RR0PgzsEHhhpr0aoYyNN0AAtYCVj6I2JBVbpchofdh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدارک اردوغان برای نماز در مسجد اموی دمشق
🔹
سفیر ترکیه در سوریه از احتمال سفر اردوغان به دمشق تا پیش از پایان سال جاری میلادی خبر داد و گفت: امیدوارم اردوغان در کنار احمد الشرع در مسجد اموی حضور پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456239" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXD0kknHgJ0kZPfTkuqXPn55Bn3u4oNSYfxhvnSjVG0sl77qBddTZL5jA2giyKUYhzWwUqxfTYAugoGVoo6x6bS4TXk1DFOIyVF0qJezgNckNBcvq5zxmqCISu8Yxi6e6i5eiyeHosGuOQ-6cliA_D1MN8FF1c1fSrfTHWS4a-XLgpd2W1EqDUj50ZgyEh0dEX9IkJnj8jL-k-cmtjJOxt5iAGX_Dldwj5lFahaO8jT-qfavpZ7KJDMKrLdkjNnygcf3Z9Op-jGujaz21daHNmotWjq4paWdDc2GOhSXfJEtU8Uutw1oMMY6vwf6uRazdUUmvRfjTJYn7wORU-BM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwWhAIb0ksUSztkFg_8lmoVVq6YxxuXhZaSz1LzZVtLYgYWHurtjAAwEvzyyOUELWHxQVwgUQ0cvI91xdTp64-Dxkfc9d92v2Xw4CxNWwFo9Eawbi9Xj8xIrBLD_JGN4TTjIKaWzGKvQrgJCfLXb_SOyLnvIrUVsQFVsRFoZJa2bRUfOB3tJJUWpuVqqyJfXtPrfU-Lj_AYZCXfWo4i4ZP787z43jPJ8x0JOxQNs7CEXTdk_-eOEAw2k21lYjSZmBvfTnXDMm_4SHWB0SoqpVa_All9YsWduWpOoPEItamp9LY4e2KsHrIwwLJmm-QPqvfNHWye2jwk1vqLE0dJBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btGuAj8XOROfuEZev_Q8WwcnXxAzq7kAvQvdzvFqI8kjS6Yn1sZqi031Y_sQZ58PRCh_a_-iLna9ZA2ll9FjFpKm_1-rCHJDlXRklLe10-j1HoVZOUibOtUSZjrgdzVYMOjettLExTo4upfKweKjHtjMhm2ZMbOxcEpcWBbHcHM5cAzmNAXMjsFPpxSTEKt6ZlRRL3wyKgc_BIIbHKEztXjrr9GR059j2lPxxb_ZS5tIN2WGMb-CRpS89Ru0f1SNgI5c-GzdppIknpETUYRWpkdtynWdcNlb2-Sc9P1CSEYjTifKIPhZR8c6aLgWcNWBs96EXkMqLRZzBo_Tmx6POw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مشترک سران قوا در نهاد ریاست‌جمهوری برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456236" target="_blank">📅 18:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etZCOINGSfsHQaP37piguIxvSUU5wz1RjXK_VvIEbbjeowg91b169DmY20511Bx_2L_FSeU2QvUWHKD2fxPqpFSpzc-V8OKDqbZtHA-0IIvSZDvITV18bSPtLtAykEKzlxcJfTbbuzwmlRenUsF84LbDv8qsO6F8a1O_nRuUDH3P9_7XDKk4D8lfeP8v5mhhwnYFojzeetJCMNegUEoAfnj9uqBT0iAeH1XZxWNlc_NtNjT9VZtELSHOqFhXQfC2uqQWD9q82Xm0HQGmIbgd9trdOO6U11mE7Mh8jZBck-OEr--kBRzHucJD5XuBb3iov7vM9V7huZdh8Qv9akvl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورفی: جنگ با ایران از اول قابل پیروزی نبود، ترامپ فاجعه آفرید
🔹
سناتور آمریکایی که بارها درباره پیامدهای جنگ ایالات متحده علیه ایران هشدار داده، این جنگ را «بزرگ‌ترین فاجعه سیاست خارجی آمریکا از زمان جنگ عراق» توصیف کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/456235" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUdg3LoJBLNWcYfCX14QEHs6evnvf7fJiCMsDA4ZXGYOCmQnQQfIbBaxWpZUIh9bBz7ungWSXd--OqBqDQiP-hUw5bQxY2PDhoWA5S0mQaR7kivakCS4UR2p0JJa30EllafoBfsCm9yLE4URhSFz4s_WTWI09UCli2VIifxG3a_oBeVLhOSl7d7zA54F15-8ZpplX9rfB4qxuZKzDga5NQQAdXvspg9geMxINl6FmYATb_5I2u7ktz8RuCKnYu8xoKHZMNrMXhXmbBhjEb6ROwxg7lP42H-0kKvnJEeNofXCdpfiW6AIuIqEp4cip55J-IsBKSip5psyCBIIJhnx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تهدید صریح وزیر جنگ آمریکا: حملهٔ نظامی به کوبا روی میز است
🔹
پیت هگزث: اگر کوبا مطابق با ارادهٔ آمریکا پیش نرود، از گزینهٔ نظامی علیه این کشور استفاده خواهیم کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/456234" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BehJFwz-JROO-yF7X4Lktt_zUyJuqksCrcvZbQX4dORXid-4sXUQucGPQD4eUvu76dsRjhxjVQg8Awk_Hev3KSeX5Q9RN7mTYmnyRTx9gH631GYDIhKsxlZZ7hYpYvEDV2r6Uadu7Wmj-oov0XD54Ev77XxZNr5f0tn2zDLLnUO1eGW1ksK0SjocZjPDIDs0fWvxxc7VfLH8eJTsNYr1AO4qROE-UimNZD-V1r0UuZT8U2favRvVTDFMCCJdgMhPDTEIt8YMUyB4nxeZMfN3vfuISA5FxhLvvN_4KnSffvigem04-cT5bbVh_nFAACjmpwWppJxxhrHRQe93hrZPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام فارس TV مسدود شد
🔹
صفحه اینستاگرام فارس تی‌وی که به تازگی راه‌اندازی شده بود با ۳۸۰ هزار دنبال‌کننده توسط متا مسدود شد.
🔸
صفحه جدید
به نشانی
instagram.com/tv.farsna
را دنبال و به دوستان خود معرفی کنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/456233" target="_blank">📅 18:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8175b9c63.mp4?token=Wd86GmYuALK-aQ21R7kEVUdKeAgjayhqoY1lWmVUqN096d22mWR_jqiemgMYGGpxbgl-GnF-Q_fTOiKtzaMKuKfaihkxI0rTozq8a05UFrdt8dGsxz2IXqNHmVhio2PByD6wZyhk8NSBLZGmCeYy8fgQSph80VYEjm6ebZdBEuOqgqG25tvbBQIy8TETtPuekU0CN_qGyCNU59qvPdZbVqcw471fdtJn0n3UT3M7ytmENuF9cm9uoqt-QIGcRGUkcqzDtCGNzsq0yiFIRU8pxY-706P_R_iHuoYBSEsdVE5DzLrRx3AMJEtlpGI4c_6s6_aHFiqYdKXGKurJ-U0TlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8175b9c63.mp4?token=Wd86GmYuALK-aQ21R7kEVUdKeAgjayhqoY1lWmVUqN096d22mWR_jqiemgMYGGpxbgl-GnF-Q_fTOiKtzaMKuKfaihkxI0rTozq8a05UFrdt8dGsxz2IXqNHmVhio2PByD6wZyhk8NSBLZGmCeYy8fgQSph80VYEjm6ebZdBEuOqgqG25tvbBQIy8TETtPuekU0CN_qGyCNU59qvPdZbVqcw471fdtJn0n3UT3M7ytmENuF9cm9uoqt-QIGcRGUkcqzDtCGNzsq0yiFIRU8pxY-706P_R_iHuoYBSEsdVE5DzLrRx3AMJEtlpGI4c_6s6_aHFiqYdKXGKurJ-U0TlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شبانۀ پلنگ نر در منطقۀ شکارممنوع کوه سفید دماوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456232" target="_blank">📅 17:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prmLQ43tENj6Y0vZMHp-O-FlHhqSYp5psk9AWtNdYTlL-pKiKrpuJdllPzt9-IB9T396TrM3jpmhn_SrwWRHQtabnlxuVzQjGaL9neJh4yOVfynR4e-iErzu-bsKB-3ohAc3pdnxpaN_klcKpiWl1CFBKytFS4BIfqVnBSFqffOZi9CQZdqlNrHNDnNXh8mKg6yzal6Q6Lb37ZHH3LCpFDy240C-l1vv3YnYLLsypmR-lAfazSJpffbWHtZsrzqAJmos86hPl9cVT8OMjfAu3l3Z3IryWVZmgtsYDHzAQAu4Fy5zmX3p3b7uW7TgLzuncIe8iMGR7cH8T9ldVcU5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت جانشین فرمانده سپاه اصفهان از یک پیشرفت در جنگ رمضان
🔹
سردار فتحیان: مرکزی که در جنگ ۱۲ روزه با ۴۰ شهید، بیشترین هدف حملات قرار گرفته بود، در جنگ رمضان با وجود ۱۲۰ بار اصابت، حتی یک شهید نداد.
🔹
استفاده از تجربۀ به‌دست‌آمده از روش‌های حملۀ دشمن در جنگ ۱۲ روزه باعث افزایش موفقیت و کاهش آسیب‌ها در جنگ رمضان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456231" target="_blank">📅 17:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gsMVfn2nt3GjYkd9VjNFcySrQay0w-RxN49Yg8UqJqsfRQIAZhv-Ol-d7BARcLnlkLhyqgNwA0g-x-BPKoKXugYqqtT9pt4Wcnq_9KXbpmdE-T0QnRyOsIlt7wLmD7sZOhiFGaMKGXrI0ruR-cYVmGsyuON4Tb33pUWccRdNQ9HCOFFTMUEPHK6B9THDnh1kVWhixjBWYSW3XK-tuhD2fuRXofP669Sju3zP-jCDjycRoQjJNKOvUYJFCNSwz-z7J5YUL_33yDU8LlyTN6ej60bgceGfeFrPlr_mIl9yG8ngVpV04DWlLxDwwAc2VfsaloL6fQKr4Nd7ubD7VSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پزشک، ۱۵ هزار جنین را نجات داد
🔹
سازمان بسیج جامعه پزشکی طی ۳ سال گذشته، مجموعه‌ای از برنامه‌های درمانی، جهادی و امدادی را در مناطق کم‌برخوردار و همچنین در جریان بحران‌ها و حوادث اجرا کرده است؛ از ارائۀ حدود ۹ میلیون خدمت به بیش از ۴ میلیون و ۶۰۰ هزار نفر در مناطق محروم تا فعالیت تیم‌های واکنش سریع سلامت و خدمت‌رسانی به بیش از یک میلیون زائر اربعین.
🔹
یکی از طرح‌های این مجموعه با ارائۀ مشاوره و حمایت از خانواده‌ها، تاکنون ۲۷ هزار مادر را از تصمیم به سقط منصرف کرده و به تولد بیش از ۱۵ هزار فرزند منجر شده است.
🔗
ماجرای نجات ۱۵ هزار جنین را
اینجا
از زبان رئیس سازمان بسیج جامعه پزشکی بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/456230" target="_blank">📅 17:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57e086683.mp4?token=WjtfnsyukOmBw95O4JI4JXMJBU5zsBireXDl5xzMaL-m3-3tqJcZSY6s4CaFpaHPem4KWfhggKPszPiCpS4zk_jSsQkxOcvP_n5sjwJ_Q4QT5BhhBU70zJ6ar04Ce7MCxQS148rfooNCuHfmVg_7Z1QeNgiAXV-ZnaYvvJbqYKQh7En4fB5SR9r3nkphcKvs93im8CMua6nfiEkwU4WoRhOqW2kZ6sdxsxRGQsKZkIFoEMkHZzBlzoVDhbCOAO0btNbK0cFZwYAEI6xmnaVCmFOgtr4lT7uhkzJm3D5cSwnpyLurpOaZRvALbmJu3p9g38CwxHnhY-upgW2bhcAZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57e086683.mp4?token=WjtfnsyukOmBw95O4JI4JXMJBU5zsBireXDl5xzMaL-m3-3tqJcZSY6s4CaFpaHPem4KWfhggKPszPiCpS4zk_jSsQkxOcvP_n5sjwJ_Q4QT5BhhBU70zJ6ar04Ce7MCxQS148rfooNCuHfmVg_7Z1QeNgiAXV-ZnaYvvJbqYKQh7En4fB5SR9r3nkphcKvs93im8CMua6nfiEkwU4WoRhOqW2kZ6sdxsxRGQsKZkIFoEMkHZzBlzoVDhbCOAO0btNbK0cFZwYAEI6xmnaVCmFOgtr4lT7uhkzJm3D5cSwnpyLurpOaZRvALbmJu3p9g38CwxHnhY-upgW2bhcAZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ جان‌فدایان ایران به رؤیابافی ترامپ دربارۀ تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/456229" target="_blank">📅 17:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیش‌فروش بلیت‌ قطارهای مسافری برای شهریورماه از روز دوشنبه آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456228" target="_blank">📅 17:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLDMYMbI68bcH2jlno8wHp5G2W2C0wWlfrD7SMoKn_fUNIlxNIAp4_Pl0hnLaIjEz9GeY191T6_GAW5k4rsZshahnDB5GwxeKN7z83tCOehqN2Mo55mMtA5T4QobMvV5uj5kaOt3JNzmCtMZ4OczMg3GyvLYVn3kLLDKWyIOzHuzJ4dU05fqX_OrOfkkFyGYwjw70rD6WBFnhij1FCKzJu9qT9JcT9XYQx4lAUk6uaqm_YPCb_VF1ppZCEbPWeb30eWFrhe0YmKqA-xQcUHE2B57Z9WS8gFWQ3J-tCnYx_mDhhXsbLrnwfkdU6cJl0iipsRiJk9OURc6ivK4RcQ-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ الکترونیکی کتاب‌های درسی جدید منتشر شد
🔹
نسخۀ الکترونیکی کتاب‌های درسی سال تحصیلی ۱۴۰۵-۱۴۰۶ در پایگاه
chap.sch.ir
بارگذاری شد و دانش‌آموزان، معلمان و خانواده‌ها می‌توانند این کتاب‌ها را رایگان دریافت کنند.
🔹
درحال حاضر نسخۀ کتاب‌های دوره ابتدایی و متوسطۀ اول در دسترس است و کتاب‌های دورۀ متوسطۀ دوم نیز تا پایان مردادماه بارگذاری خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456227" target="_blank">📅 17:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d602e8c27.mp4?token=bwREqstk3FxeY5FmiQaE9yrfehKxR6SY4tHesx-FQk0BOFM_tfFY-z6Wgr3SvxI4HsjwJ9D9bBMD3_md9VYtMamICAP3dSPujKCPzygmAnRP2mCB_sWwsuxmaBPLzDL_7__kO2RFgfSV7vmbYqzK3JiEXTYfZzmykyZX7KhyvvHJ0VS1PGms6mJl7agHYHlvYJARnJKAaAqxdbOZRnUmwpIdwGKc3Xp47PepwpHXq6gM8vTmHZL6HxdeiY-ZpzjqZOPpvTr0BOUT2QNBJsBqEKPVX66TcKGV9Z9QalDLD7Ge95VkjVJI8FwT2aDLu-fdu0aVvktBzOLDA_7pdAld6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d602e8c27.mp4?token=bwREqstk3FxeY5FmiQaE9yrfehKxR6SY4tHesx-FQk0BOFM_tfFY-z6Wgr3SvxI4HsjwJ9D9bBMD3_md9VYtMamICAP3dSPujKCPzygmAnRP2mCB_sWwsuxmaBPLzDL_7__kO2RFgfSV7vmbYqzK3JiEXTYfZzmykyZX7KhyvvHJ0VS1PGms6mJl7agHYHlvYJARnJKAaAqxdbOZRnUmwpIdwGKc3Xp47PepwpHXq6gM8vTmHZL6HxdeiY-ZpzjqZOPpvTr0BOUT2QNBJsBqEKPVX66TcKGV9Z9QalDLD7Ge95VkjVJI8FwT2aDLu-fdu0aVvktBzOLDA_7pdAld6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی، وزیر سابق کار: می‌شود هم جنگید، هم اقتصاد را مدیریت کرد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/456226" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAMudHY8DhKdNE0vsCFaZ4n5oYR94GGBzWurNzzDioxZd-Gqy2izKSoy5ZDU9xZ-Bpl9Fp-Z5IoseHrIF1WpBA9nP10utrX5PoZ7acdQu3Yoa7SWBDHTlreuvfYHwULBj4x-pQ5qAu2tSe4wir7bkgDape3Gtg-c65_quRAd7rxuTBeMWUeuuuWZhOynahnpdHeXPlMjdtWNKadCuVosfmuPg7jLcDcDoe6RBZA1iVBYohiEhpVspProFTplqVFhqNhPwpyk-MB6e3TdSW-99F-x-65iXqERZjV5rT4IYTOn24lED8zrK81CvbRuiwxz6TmfbpXHXaEt0Epu7kLMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
✔️
غلامرضا محمدی سرمربی اسبق تیم ملی کشتی آزاد به‌عنوان سرمربی تیم کشتی آزاد استقلال انتخاب شد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456225" target="_blank">📅 17:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b339ff2875.mp4?token=VBEcmY3hNhM3VmvETPoZNQBR6Frq6ufprxVHt-lGWAT8dBaMDisUt2D0IoTTJX3rUtEqBbf5UPzOvEEBuzQSFJ8MDL_Ca9ga2zOkBq0jYmGnFIwtmjbJZET5XdHrZ-I-sHaujHaq5V9y0D4nrSnPF6F7nQ_3YkYXchGobqSudGsOGQ5_bv-hwmDs-KN7kVKifvKwdM_1vOMZUF5Zt9VE-Q9gYaVXrWKsUgJOtviqmGo-zMF_V4rq8xW0XqCDYSh_5exWny9NSNQTqV_iXPXfwhipuHQQBnKbISRDLkRfO1FVtMP0uJWAMFY8O9a_RO5Jl6oMLbs2IKaEDWkteRdqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b339ff2875.mp4?token=VBEcmY3hNhM3VmvETPoZNQBR6Frq6ufprxVHt-lGWAT8dBaMDisUt2D0IoTTJX3rUtEqBbf5UPzOvEEBuzQSFJ8MDL_Ca9ga2zOkBq0jYmGnFIwtmjbJZET5XdHrZ-I-sHaujHaq5V9y0D4nrSnPF6F7nQ_3YkYXchGobqSudGsOGQ5_bv-hwmDs-KN7kVKifvKwdM_1vOMZUF5Zt9VE-Q9gYaVXrWKsUgJOtviqmGo-zMF_V4rq8xW0XqCDYSh_5exWny9NSNQTqV_iXPXfwhipuHQQBnKbISRDLkRfO1FVtMP0uJWAMFY8O9a_RO5Jl6oMLbs2IKaEDWkteRdqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست قاچاقچی بنزین رو شد
🔹
دادستان هرمزگان در جریان بررسی صف‌های بنزین، متوجه سوخت‌گیری‌های متعدد یک خودرو شد و تخلف را شناسایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456224" target="_blank">📅 16:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
در حملهٔ بامداد امروز رژیم صهیونیستی به شهرک «انصار» در جنوب لبنان یک مادر و تمام فرزندانش به شهادت رسیدند.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456223" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
تیراندازی در دانشگاه ایالتی ویرجینیای آمریکا و اعلام وضعیت امنیتی
🔹
تیراندازی در دانشگاه ایالتی ویرجینیا که چند مظنون در آن دخیل بودند، به زخمی‌شدن چند نفر و اعمال محدودیت‌های امنیتی در محوطهٔ دانشگاه منجر شد.
🔹
این تیراندازی در نزدیکی ساختمان‌های Quad Annex دانشگاه رخ داد و پلیس دانشگاه و منطقه در حال تحقیق دربارهٔ آن هستند. هنوز جزئیاتی دربارهٔ انگیزه عاملان و بازداشت‌شدن یا نشدن آن‌ها منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456222" target="_blank">📅 16:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d794581db4.mp4?token=dkkCbZWbVCMY6d-9Hw8oqbIl7vuKrJtowDBCoeOKsHNeUjXka8Wt3emaTp4oD6GmkpvNxtr1HUuGtdB-ZE-7UcFzz4XzECike7xRz1R903nu3p2R8uuuEK3uRpF66Ys8rOIsGCzfeXzJUXK1pTXE0XzaqZcXSsQ_X3AQuPyIc4AhyKXFcpFkeoyv6zU93xOsyEsh6XnfREGuh04wnyyZ5bZQBouxZJwMVgJllAoCozgHTauBAloZOqTmQ1tW1jS7OEN4W6dBGhH5IFpoEEDZHUo4aQCJrkpe6Ul8GAh-9bVAdRSnUcLe_xSqHR0pqmpwURf1xLTyUhObu0D-zskSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d794581db4.mp4?token=dkkCbZWbVCMY6d-9Hw8oqbIl7vuKrJtowDBCoeOKsHNeUjXka8Wt3emaTp4oD6GmkpvNxtr1HUuGtdB-ZE-7UcFzz4XzECike7xRz1R903nu3p2R8uuuEK3uRpF66Ys8rOIsGCzfeXzJUXK1pTXE0XzaqZcXSsQ_X3AQuPyIc4AhyKXFcpFkeoyv6zU93xOsyEsh6XnfREGuh04wnyyZ5bZQBouxZJwMVgJllAoCozgHTauBAloZOqTmQ1tW1jS7OEN4W6dBGhH5IFpoEEDZHUo4aQCJrkpe6Ul8GAh-9bVAdRSnUcLe_xSqHR0pqmpwURf1xLTyUhObu0D-zskSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ افزایش قبض‌های آب
🔹
شرکت آب‌وفاضلاب هرگونه افزایش قیمت خارج از چارچوب تعرفه‌های مصوب را رد می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/456221" target="_blank">📅 16:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERGTTp2AyHqO3OIEfgi3c1bo79Q8edha9eWc3Bs3JLrBis8zCTHEm-eKwnZ1tMOEIX7RxR7leGLuIxLGX-kBOeyD7RglssVDrPwFvqs3jqx-Pn0eWp1lTZwX6ICfJNVmy-fVmSWEv-OHrC7Q0q08GgzyZ56GcDxvmiKMqI0T85qlSlDNrwghNfPJgWLdS55g074B1ewGQNS0rBjzNMZPU7K7HD9j9BAvcrFdV_vabmuIMlDEdedAubZ1VXM4b5wegm7Tn8L1UdUmuEVQDdlcKi0xvQ-JnZ5fW3vHFmC8mALa1-uojmKBBwjCAzKTtOYtj-yYa0q1AXnglCjjjX1ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان: دشمن اسرائیلی بداند تلاش‌هایش برای تحمیل یک وضعیت جدید با پاسخی متناسب مواجه خواهد شد
🔹
حزب‌الله در بیانیه‌ای اعلام کرد: دشمن صهیونیستی غیرنظامیان بی‌گناه در جنوب لبنان را هدف قرار داد و با بمباران یک منزل در حومه شهر انصار و یک ساختمان در دیر الزهرانی، باعث شهادت ۱۱ نفر از جمله کودکان و زنان شد و ۱۲ نفر نیز مجروح شدند.
🔹
این تجاوز و نقض حاکمیت لبنان، مسئولیت آن بر عهده دولت اسرائیل و ایالات متحده است که از آن حمایت و پشتیبانی می‌کند.
🔹
در مقابل، دولت لبنان باید به دنبال راه‌هایی برای توقف این تجاوز باشد و نباید به ادامه مسیر مذاکرات مستقیم تحقیرآمیز و ارائه هدایای رایگان به دشمن ادامه دهد.
🔹
اکنون زمان آن است که دولت از ادامهٔ مذاکراتی که آمریکا تحمیل می‌کند دست بردارد و بداند که اتکا به تضمین‌ها و میانجی‌گری آمریکایی تلاشی بی‌نتیجه است، زیرا آمریکا شریک اسرائیل در جنایات و کشتارها علیه لبنان است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456220" target="_blank">📅 16:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c8fdcaf5.mp4?token=j2XoFK3v4qDEpZs4V_RpjUPiuyCwhX_lw1i3sm-mU55IGr5bdNF3BIGs68UuRg55TtvCtQxw-SIlYTmXQZR9Lp3Fh62rZZ53MofEMwziOx9iXIuMiS7QOAukAkMlJ-wjkjsCjFqQ-Ct8U7la6F639hX6MFNJ1V2RNOXyfnPC4BCZxIML4yoqOAC6LqxxfHvw3ouTuknaQSV9lIr1Rykay3Hs2XbhEKF54nQBDT5NEmhwCEPul_MzLYLUSjVYTK7eY7t3GoybZLoBD_ViHk-cLg1b4BRHWsKdok2zUOm3WL3L1dFalEQcWNITpLgRnjK13gEFFf3eU1O7hb1U1cTxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c8fdcaf5.mp4?token=j2XoFK3v4qDEpZs4V_RpjUPiuyCwhX_lw1i3sm-mU55IGr5bdNF3BIGs68UuRg55TtvCtQxw-SIlYTmXQZR9Lp3Fh62rZZ53MofEMwziOx9iXIuMiS7QOAukAkMlJ-wjkjsCjFqQ-Ct8U7la6F639hX6MFNJ1V2RNOXyfnPC4BCZxIML4yoqOAC6LqxxfHvw3ouTuknaQSV9lIr1Rykay3Hs2XbhEKF54nQBDT5NEmhwCEPul_MzLYLUSjVYTK7eY7t3GoybZLoBD_ViHk-cLg1b4BRHWsKdok2zUOm3WL3L1dFalEQcWNITpLgRnjK13gEFFf3eU1O7hb1U1cTxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوضاع قیمت‌ها در بازار کالاهای اساسی چطور است
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456219" target="_blank">📅 16:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKDFiRzluWjuPDJ3s7X1K9-vypi1dcc8poFrFiBWUDZQGjchTMzqtg61RkU5gZXXln733ay_E6UiQF3jSs6Jkr6lmohFt9FicUNGhaRv_ZlvwE4VWZSHqzvhYCQc5g9l67g9dOwjR8ZxGeNDN4HuqT3IEX0lxAyq7xW1ZW1ks4dZ-PNWNud5yHFFm0HaDprsH3xW48rNioEggmEcBSqTbC__kQl70XElegeI-tZUq9iI__PZYoWf0H1nQt7vTeXJ1hmbrmYY98_jDVo9ikSpTYXb-YMa9C7a8MWCRd_Jwaj8oUjlIVXuYgy-PzY0LZ2RPZ1sEU-ZgPNsjq3-jweOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما راوی محله‌تان باشید
🔹
خبرگزاری فارس در نظر دارد با راه‌اندازی یک صفحه اختصاصی برای هر محله پایتخت، پوشش اخبار و پیگیری مطالبات مردمی را به خود شما بسپارد.
🔹
اگر دغدغه محله‌تان را دارید و می‌خواهید صدای رسای هم‌محله‌ای‌های خود باشید، جای شما در تحریریه خبرگزاری فارس استان تهران خالی است.
🔹
علاقه‌مندان و افراد مستعد می‌توانند از طریق
این فرم
در طرح ثبت‌نام کنند.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456217" target="_blank">📅 15:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679ed02728.mp4?token=q1iNXZ3ruy3cvrMv3Ha-8k3UX793JOqKn2Ecdqe20ECVsowGBwDJEp8XU8GZBe22uNxQujdB5KUtojls-RgcgVdgAen4ZuClTsPOG4sPITEKrgpgSZ-fBDnT4-GHpv4znt6pCNgXHNCJ7QfA2URK-qYfj-Yy3InQDORSyrZ-du1ZHD-P-xWl7Mxcbm1wfWAuAmvoMWIU2YwXMgUnWwKzrBstpH4eLPbc6YaX2WtFGl8y_f0PhYQC_VZx-pDZ2w5tz2tI0sQR__2LEgjRqgVeFrWafe78n__pxNWZwBHkBA-yFnst2UgaUPQeDMRNnBsrPCeOmLnwD3tyW3OR33aP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679ed02728.mp4?token=q1iNXZ3ruy3cvrMv3Ha-8k3UX793JOqKn2Ecdqe20ECVsowGBwDJEp8XU8GZBe22uNxQujdB5KUtojls-RgcgVdgAen4ZuClTsPOG4sPITEKrgpgSZ-fBDnT4-GHpv4znt6pCNgXHNCJ7QfA2URK-qYfj-Yy3InQDORSyrZ-du1ZHD-P-xWl7Mxcbm1wfWAuAmvoMWIU2YwXMgUnWwKzrBstpH4eLPbc6YaX2WtFGl8y_f0PhYQC_VZx-pDZ2w5tz2tI0sQR__2LEgjRqgVeFrWafe78n__pxNWZwBHkBA-yFnst2UgaUPQeDMRNnBsrPCeOmLnwD3tyW3OR33aP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب اقتدار پدافندی
ایران
🔹
ارتش آمریکا در جریان جنگ با ایران، نزدیک به ۲۵ درصد از پهپادهای «ام کیو- ۹ ریپرِ» خود را از دست داده که هزینۀ هر فروند آنها بین ۳۰ تا ۵۰ میلیون دلار برآورد می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456216" target="_blank">📅 15:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e954320d.mp4?token=gTNgViCw8xQoe4rLiagCwXUPZbFz2rD-AI9fIXtFrCbGJiHugZWijEBpjHX6s6WQVf2buBgg7EqZGCeG3OOxmRGYvLy6HnvbAx5JA0tsToMivHzyQbpEYdGAeutZU_VGeFX-qoxkn1vfXPRUC7Iq74cR3spD3gz13vpO-a_B2Mj6EUh5S36AHqFIT7i4Gy12U-2-G6RvreEuaCKLaRzI0rS9Mp3cXuZssGw2A2gQDxR700Hk80uHCra9fbZ6PRM-QL2jh6-t7DXolTMmaeyT8091XDtB6Bf-LaG4jVcj9Q-jkR1G8APLpPaWO61BGESPkUmhkjogT3F0pMyw-8GJLgbOWS29XVSzye2Q7vF-vKJtKXtcsFXNPXktuYlnMr0Q-jKItkWGbnVEj3an6nysHL-fvrfUhVoTug0ElIUiEBYGdvBN_4vCus-jwnUxoA0NW3aY9bIt-yAQqGLygjr3lJD_gi2k92ME7BCrx5SY6VTvyGXyOc9nEEXF5huNQHP4nFRw3gJSEVdFSl6joULM1KhVG9EWyrLLbOyaotoW6AlgP1AU21pW-FZHYWzTEiyJIMQ2UmTK3sKferiwVW4B_CoTovpxsMz5kflzZu45j9W0K92gdeDZQZOMuUHX2wH2Yy9-UK7fE_fFpABb86ynW1K7qSDgCr0D6522RQfs6sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e954320d.mp4?token=gTNgViCw8xQoe4rLiagCwXUPZbFz2rD-AI9fIXtFrCbGJiHugZWijEBpjHX6s6WQVf2buBgg7EqZGCeG3OOxmRGYvLy6HnvbAx5JA0tsToMivHzyQbpEYdGAeutZU_VGeFX-qoxkn1vfXPRUC7Iq74cR3spD3gz13vpO-a_B2Mj6EUh5S36AHqFIT7i4Gy12U-2-G6RvreEuaCKLaRzI0rS9Mp3cXuZssGw2A2gQDxR700Hk80uHCra9fbZ6PRM-QL2jh6-t7DXolTMmaeyT8091XDtB6Bf-LaG4jVcj9Q-jkR1G8APLpPaWO61BGESPkUmhkjogT3F0pMyw-8GJLgbOWS29XVSzye2Q7vF-vKJtKXtcsFXNPXktuYlnMr0Q-jKItkWGbnVEj3an6nysHL-fvrfUhVoTug0ElIUiEBYGdvBN_4vCus-jwnUxoA0NW3aY9bIt-yAQqGLygjr3lJD_gi2k92ME7BCrx5SY6VTvyGXyOc9nEEXF5huNQHP4nFRw3gJSEVdFSl6joULM1KhVG9EWyrLLbOyaotoW6AlgP1AU21pW-FZHYWzTEiyJIMQ2UmTK3sKferiwVW4B_CoTovpxsMz5kflzZu45j9W0K92gdeDZQZOMuUHX2wH2Yy9-UK7fE_fFpABb86ynW1K7qSDgCr0D6522RQfs6sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسکن واقعی باید چه ویژگی‌هایی داشته باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456214" target="_blank">📅 15:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG5QCG9n1yGwg33Q0RmY-wDzmHEVNFJefe0676xHLI6TXM_y2Ye8a4Uudi79-y8NhL3mmqB3a2HnB2cDfDEs4emkCdO0VXW55IkpcCx4aQWzELuwiKARvfRLWTaNtfS62j9Q3HCShbHuUUnD71cKDdtkZEy9B1RyUvpNoAq4t8aHPaYgsEhgCeq1NDYdSZD3my2h0dtfbTveGN4ScIJAEkTdp8GHiKN21x5e18_Uus2R3K2IHo4vW1IXFeOkmKxAlXp1Cx_8NReMYlIjAhGVA5HsSLIVN471-bn-HvbY-omL17YHqaC4hcz7q7CwYACNrPRBLusNkDhGGoCnMN8ACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: متروی تهران تا پایان جنگ رایگان است
🔹
متروی تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456213" target="_blank">📅 15:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملهٔ توپخانه‌ای و راکتی ارتش سعودی به شمال یمن
🔹
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
🔹
همزمان حملات راکتی از خاک عربستان به‌سمت منطقهٔ «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456212" target="_blank">📅 15:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyDq1tEAdtgoutHWirq5Pijm7VjryTMclYgqyqHUx9Sgt6TMTgHiQPE-p-yN7jHoOTslueDWe7gHh7JnIb6a4rmL5yRAzvJKOoZHJw_kWOUqyWjp8RaGrzuKvJr9kvB8DaGCoGVBtzXB-TXkEmzSgIna0J1IJ1ZGCDH2x_TOnf4lO0nIVZS0OGBDTD-KmOCftMq_OiwvSW_d6O525y8QMmdePvj-YEOI49WMXi_rCPK127hb7hwiIlBNpNRnz-eqzI-08-e9CXoczAu06y2W1THLVOueWTQoxb3hr4g6ILwUHVnKcXHBHnIvL3Vcx_vL0t2I-kWDU_9j2lF5O7TDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
🔹
پیگیری‌های ما ادامه دارد. طرف قطری اظهار بی‌اطلاعی کرده؛ از ارتش و دولت قطر می‌خواهیم که با مسئولیت‌پذیری بهتر برابر با کنوانسیون‌های بین‌المللی اقدام کنند. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/456210" target="_blank">📅 14:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456209">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoKCRFOPMslhp4-zqgcDni-KgfEcsn-tRbum9swLLWGANvFeUXghPGNRe9SKogGi6HOLDOpcDFeQ8WKsz3uGg9iATlJstNJhhNbVk7fHcC9Vd5pBG4lg6rZ86JFs1LSxJj6Cz3XJGhllRA8Zuaf779TJ4tNAqJwXMVTu2025Wq5UeOfZ8GVZgauMTqtubA-_7Ntrd8wtKfY_F-UpHGP0mOyC0tkavB5uu9Kq_Bd1bNHRPIZqop5gGOzE7_3PovrJ-71dVS0K4OPCiPk3NV9xpJh0_Wn3oWGYTp5nyOXxVMDM6sVuDWdCMD3thFsP4Hgk2s3T2GAqczpWrxMT4WO_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته ویژه همراه اول برای قدردانی از مشترکان در ۳۲ سالگی
🔹
همراه اول به مناسبت سی‌ودومین سالروز ورود تلفن همراه به ایران، بسته ویژه ۳۲ گیگابایت اینترنت و ۳۲ ساعت مکالمه را با قیمت ۱۳۲ هزار تومان عرضه کرده است.
🔹
مشترکان تا ۳۰ مرداد ۱۴۰۵ می‌توانند این بسته را از طریق اپلیکیشن «همراه من» فعال کنند. باشگاه مشتریان همراه اول نیز برخی بسته‌های پرطرفدار را با یک‌پنجم امتیاز معمول ارائه می‌کند.
🔹
همراه اول اکنون ۵۴ درصد بازار مشترکان فعال، ۵۵ درصد بازار پهن‌باند سیار و ۶۷ درصد اشتراک‌های اینترنت اشیا کشور را در اختیار دارد و حدود ۴۵ هزار روستا به شبکه این اپراتور متصل هستند.
http://mci.ir/-48B5PW
@mcinews</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456209" target="_blank">📅 14:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9w7ToIG5aXNt8SLPlfiQEAGmX-d4PGdP7jRA_WXwwMeyeo6msqwNn4ngze0kRHwyxoylaPIF2X1WPgIpYXwC1o3uRpfNBld8Gy6XhPl4Pr1gyTViZ7PP8nsbSemd4QnmfiAOXelYdx2K0JM2qFhJiAnkzzeHoqRkCq_qmcKakTOIxcg1e4gKzmq43FLxwmLqY0deO9HgM0zIduvC5HJR04d0ydRuOBwBSo555AOgU_Ge9f8NBtXp5dD4MBB8h5AKfdlah9VeAch8zphq28By8OglZhfwDiDOCGY5QXdRgLblRxPPaPEb9OxJrZVLsvCys5SD6wi46SDcBpDOS62Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
برندگان طرح «سقای شهر» معرفی شدند
⬅️
برندگان طرح «سقای شهر» با برگزاری قرعه کشی انتخاب و معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، همزمان با آغاز ماه محرم، بانک شهر طرح «سقای شهر» را به اجرا درآورد. طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا ‌شد.
⬅️
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می کردند. در نهایت این امتیازها به بطری‌های آب آشامیدنی تبدیل شد و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/456208" target="_blank">📅 14:53 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
