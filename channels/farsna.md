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
<img src="https://cdn4.telesco.pe/file/gLuGNg4tknGYL7og6NK0hS5jk-_dlpqX6ObhQoTld9q7NWgX3yAIRBp-FbQwLRIkNmONkvu4yGS5p4h0icQIDnxhChi83Dk3EO8CRw35CCKESxJrBXyjZdiOlgf62UHIlC9Ks4QJOK0f2si6rE7ohfElbny40EASIDnsfnuSIeah9l_lfng63VTdib7YxDgX6xcpE4RZDArXn6Y__eZuxXQs6ethw5NnUeqqwkqCQr19swEz0DgbwAiR-kaa5tv_oaVvB_tbN-Ofji_in1K7rOQ7Ii3PBscQ8oD0DAiHvO8_PAMkM7Th7nGze5rBlXXip3AA4XuhSdYfLXFFbY7zRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 18:51:49</div>
<hr>

<div class="tg-post" id="msg-455012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb90fa67c.mp4?token=oeb2M6Mkec-OXLagtEBl4zh41RN-t8sglaCGncwgTl2S7w4jgmPX7uQSloMc_OVAvPzuVlWUuAowHAuHwL7D2xDtCg5DcoLlpBkVoAWXFzOzAJXssp2WCbZd-WTer9-cOFKB1OS34ROTKtd3wldkzNgAsO8J0JX_xLeP3xZ7bHU1qFP4JB-6mC4HmRGxJ0X7XSW4YxwtrpD6GYpAP_SsOUZG8Gli4HqIH4Vb9tuTlaBH4r9Vcq-8f1dlE0r8clUPz5VClLW0Bfp1hG_tKMvRJMbh5sSamvSsrHLEODUusfImspwkmMqUOxZkjSDZ1qV52Wvu5C_u2rFfUQSRoyLoYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb90fa67c.mp4?token=oeb2M6Mkec-OXLagtEBl4zh41RN-t8sglaCGncwgTl2S7w4jgmPX7uQSloMc_OVAvPzuVlWUuAowHAuHwL7D2xDtCg5DcoLlpBkVoAWXFzOzAJXssp2WCbZd-WTer9-cOFKB1OS34ROTKtd3wldkzNgAsO8J0JX_xLeP3xZ7bHU1qFP4JB-6mC4HmRGxJ0X7XSW4YxwtrpD6GYpAP_SsOUZG8Gli4HqIH4Vb9tuTlaBH4r9Vcq-8f1dlE0r8clUPz5VClLW0Bfp1hG_tKMvRJMbh5sSamvSsrHLEODUusfImspwkmMqUOxZkjSDZ1qV52Wvu5C_u2rFfUQSRoyLoYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتصاب فیلمی با عنوان تغییر دبیر شعام به خبرگزاری فارس
❌
به تازگی فیلمی با عنوان «انتصاب محسن رضایی به سمت دبیری شعام» به‌عنوان محتوای خبرنگار خبرگزاری فارس درحال انتشار است.
✅
خبرنگاران خبرگزاری فارس تا کنون چنین مطلبی را منتشر نکرده‌اند (و مطلب منتشر شده از سوی کاربران این خبرگزاری بوده) خبرگزاری فارس اطلاع‌رسانی در خصوص این اخبار را منوط به انتشار رسمی از سوی منابع ذی‌ربط می‌داند.
⚠️
خبرگزاری فارس بیش از ۲ سال است که تبدیل به یک پلتفرم خبری شده؛ در این فضای تعاملی، کاربران تنها خواننده نیستند و علاوه‌بر درج نظرات می‌توانند تولید محتوا کنند، پویش ثبت کنند و حمایت بگیرند تا با رسیدن به حدنصاب امضاها، مطالبه‌شان از سوی خبرنگاران فارس پیگیری شود.
@Fals_News</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/farsna/455012" target="_blank">📅 18:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_j-9pLq-lqELo9BYYQYB_Ux6skE6MscoSyTdFGzwiqBjOBitltUOsiISB8Sse26ZhrMYYJSOBZEOu7O0V0cJJI7Tf5RVGOT5F7cef1yMwDS138O6_RYNZqGPvN8gwnFtudnAo1o7nbMg8qFX_h8pK-vqpLjiUEe9K_vkVLrmyyJEHZQz1XP-cPDEOoipQJsRcw_bLJUsLyIssZbRydP6etj70OdonnjUaaED4E-qiEUFYjkR_Un-Y0cqnMmpJJZrqeEFDQMfjyd1JKShFDrjXLrOj4SNhqUmyl5UsaDdZOuy_EF1Rnjr7N1GVVY_OdP0xAizCl6FeF-GAex7002Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
موسیمانه، سرمربی سابق استقلال به‌عنوان سرمربی تیم ملی آفریقای‌جنوبی انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/455011" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G38QJLbgf8BTQJNQr19shZLXSP8ae8qRma9KS5jFEOF41grkEPt6UEK1I7s2iYJIebo4-V84gno2GDIXb7uUvi2XUx6Zj8xKD6n1TvrbTxJ6PXMizTZbv2uzo8vZrvOBKC_KjV_euNJZT4G_tLiGsv34HW3ElLWoYVamF2EbyA-1ZE8nnd3Lje9y28ZGswMHHMBjzbLV0jBOhe7kJQwW1qRXxn9jwfVv0VBNmYARKmqWSU-cnl3_CNuNSUejznyyT4U1NQZSFdYWpQfW7goq9MgicK-8gnUUPKnnjr7mza_1btRUgmjrAIqA8lu4eO3PG4V-xVAPZNGA1jf3Lw0VZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دهقانی: رسانه شریک توسعه ملی است
🔹
فرید دهقانی، مدیرعامل شرکت معدنی و صنعتی چادرملو، در پیامی به مناسبت روز خبرنگار با قدردانی از تلاش‌های خبرنگاران، بر نقش مسئولانه رسانه‌ها در حفظ سرمایه اجتماعی، تقویت اعتماد عمومی و افزایش تاب‌آوری کشور در شرایط بحران تأکید کرد.
🔸
دهقانی با اشاره به شرایط کشور و مواجهه با جنگ، محدودیت‌های انرژی و فشارهای اقتصادی، اظهار کرد: اگر صنعت مسئول تداوم جریان زندگی اقتصادی است، رسانه نیز مسئول حفظ جریان آگاهی و اعتماد عمومی است و این دو در عمل، دو ضلع یک مأموریت مشترک یعنی حفظ تاب‌آوری کشور هستند.
🔹
مدیرعامل چادرملو با تأکید بر نقش خبرنگاران در شرایط بحرانی گفت: در روزهای جنگ، خبرنگاران تنها روایتگر رخدادها نبودند، بلکه با اطلاع‌رسانی مسئولانه در کنار مردم ایستادند و در حفظ آرامش جامعه نقش مؤثری ایفا کردند.
🔸
وی همچنین با اشاره به ضرورت رونق تولید، سرمایه‌گذاری و بازسازی اقتصادی پس از جنگ افزود: اقتصاد پساجنگ تنها به منابع مالی نیاز ندارد، بلکه به روایت واقع‌بینانه از توسعه، چالش‌های تولید و مسیر پیش‌رو نیز نیازمند است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/455010" target="_blank">📅 18:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU-EErLbfZrL62BS2s_WjcjgxYAhWUkrZT-hZKo3C13DRX5j5nM0XIX08C4GEGtFRFuaIT70qeG7ojBZHmeL8wFt0mQFP_70T8J1myof6zF6Rw9n9LLV5GLt4hen9YajUDzjGZ_gtBHsczKFHa6fZmo40cr5fsOl0QOsmLffOX2bZ2sF09HilqhT45pWDLzv04fTeJpK5GOdcFBSppgHyimkRHk7ijnf7GijweJYLJhplZlsCymkiwi1osX4WV3ew77W0LoJ5uYMJLYdjXf4U9aozhLIWERqgO3S4P6tt3g9AbZcdzj3tfeoD3JjyEi8e7-sM4iFXf07bACRVh4ZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/455009" target="_blank">📅 18:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455008">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/455008" target="_blank">📅 18:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گلستان - خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g03owI_9Ccis8E48ZRcfPWbcfnsn_-7Z0AitN9Z0lSJhjMmYMXjwkHsBe062HwBQK31qiKiVqYeVHPUEwMZLnWQuTE1kBMkZy20xvE6RtNyQ0XOMEYY6rU-3jH44FE7wQY5PcHTK6RQ-qdz5XsN8N_4mJda3NQk24HhB3BSqbsRjfqSMUh7pZ76ZXOaqYZWAu2pGNPy_tyFgLqb-FchuP5Ut5gLvN4Jc7mVFI7xNMvMJAOffdsTRp15TYcjhCJT1NHeKe0D0k3enkDJhLmOTzE23TRvVAj0pudczLZgyQKox2w5l0Cfg3B0cwjLUQf7uk99YYDwOmgvWFAOU02Ob9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0sQYPEHJZoTX7TwmoQPigQcrSYJXEfvx-B0bu18CC2wVbv0iDxwlZKi_BsR_TT0Wlbgx9QMEIbS-7yi4MimHTxdZT3xPuKrWuUq0rmLhopCVbk0cpfldCRTHt0BMxtjrxoIr8wIKPrWBpCSNlQbQuh5d9Dv9Z2tQkzyvo5kLolSU7HbG8eqz-28zGL21O-yXifphJsl578XOV3uGx48e-WCtMqAKeqLBvT18VebarlyPzhqdIKzgNRyCj5Lu8TtUJXn0jPaknUaUHfOwaG4vXRIkilX5viA1888GwHhdr4fGqLNdptjSYRKF0tYwznrOnP7kEeIjN1ZjJCQ9p-TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_gcSTnTIMxz4mlu0xSfYwLYreQLj58dbn4zYBPtzD7UDF00eQ4a6jDzb9RsgWNU33Kw6RasgGd0bNwJlEo-J41i3jE6jtCVd-40CsC_6rPO5uQ5ePuoVwOf_-QLYyr8d8aOKUC5nSE39EYvxACuhMebbiaMozu3befoNrfZ2gTjg1aKp2cSTJkiCNn6osPu5POsNsxBeXgZHEeVx9A5KR-c3Tx-IiaopW-v5qUUS1X3QL4TNMRpo0T3L6vxuRVvcpfHOqh290PgFMJBwi8140zcAD_BtbvQ13F6BuN5a0ztF2BBqAtRsAREWoGcjTqyfOi06weLt89E7KT8rxvbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EadblJvvVLoQES_MCIKDbgk_WCYfsnjZRFRSuKfZPcXGmp9WFPbK7rX8pekq8OPtxGFqezO6_yiy_bFCKOfrBWY0FViVGIEIYeFivMAn1o1MdysK62G2q5ifm92Oc4QVbDYser2x7XWM3vArwuvjLQq35k67KIU71arrjGInXXS4poPzVkZG86vy-cy3TKYZ9bQjJfkkI960OvgXcSp6MrTVzVVD1oH22B63eAFIu4u9tsrlsYXuJ_zVhhQVCVLeSxksV_3oxo7PGXXkemNavn0ljva0_nSOMfWyi-mbYsc_Xh9UdeGWHLipguAFfshunW407xJCNdVXVkko-Stjcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دادستان و رئیس کل دادگستری استان در دفتر خبرگزاری فارس گلستان
🔷
دادستان و رئیس‌کل دادگستری استان گلستان صبح امروز با حضور در دفتر خبرگزاری فارس گلستان ضمن قدردانی از نقش موثر این رسانه در انعکاس اخبار، روز خبرنگار را تبریک گفتند.
@Golestan_Fars</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/455003" target="_blank">📅 18:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d2d9423e.mp4?token=hNoyFPnYbacF1Nu1YTN7LrujL8BZfNNdD--B56uIm2cw13qj6490agkT-0Gfa29bsDqweIYkW5IAi1VX2J-GvoS7dXvxBDBiU8Y_2Dcv17gjtEajRJeto2dWKDSICE0YV5BJ4LSuX0pWDLpHhLDCIVswrN9K0i782ye-_zVwhvDjEakDGIJMy3QmJPttAo7MrESbqUtuty08rKu9MvTgk4COmjmOKm9svwY95WBv1ATvWuHL0Qx5rzXcVAkFi4evVuQ5ox1DOiKJcsYu0Wnlh1eNSXCN30-AcM2KOiLbznmNApKoJEe2aYxGkRw9neVrxtG3YSqNN4FVVkrw82EaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d2d9423e.mp4?token=hNoyFPnYbacF1Nu1YTN7LrujL8BZfNNdD--B56uIm2cw13qj6490agkT-0Gfa29bsDqweIYkW5IAi1VX2J-GvoS7dXvxBDBiU8Y_2Dcv17gjtEajRJeto2dWKDSICE0YV5BJ4LSuX0pWDLpHhLDCIVswrN9K0i782ye-_zVwhvDjEakDGIJMy3QmJPttAo7MrESbqUtuty08rKu9MvTgk4COmjmOKm9svwY95WBv1ATvWuHL0Qx5rzXcVAkFi4evVuQ5ox1DOiKJcsYu0Wnlh1eNSXCN30-AcM2KOiLbznmNApKoJEe2aYxGkRw9neVrxtG3YSqNN4FVVkrw82EaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  یمن: تجهیزات و ادوات نظامی عربستان در پایگاه «صحن الجن» هدف قرار گرفت
🔹
سخنگوی نیروهای مسلح یمن: پس از رصد دقیق تحرکات نیروها و مزدوران عربستان سعودی، تجمعات دشمن به همراه مهمات، تجهیزات و ادوات نظامی در پایگاه صحن الجن در شهر مأرب با تعداد زیادی موشک و…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/455002" target="_blank">📅 17:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d217574a7.mp4?token=nRCOCrb8cP_oMjg6sMK0AbDgT6uwSCgMimdb2hHKyJlU0jM40U9duWrGNWd2ICMNnRNCYk4uC0fjS61l9tBvPuo7aOStYEGX-e7uQyJ7Md8RcvpbIjYTlVhq5lXI8KdKkwAChWob-vHsnLwOdrkUakgd5lMrS_K_n8X-9Zrpj38UWHEZHkJFpjGes3uP3ZIpGZ6BP7uloTjNLMdUKA8NbiyTDVSBWbBn5uS6RSt8MN1mFtcgZcl_P6m10Z9G-HHiUg96Z1p0qolgwLHRWTfL0XU2OW6mLo2EGWGdPGuDJdTKP8k6KwCQ1t3vDJsBfhXC38CBkDXTY4wKxkn-tHsToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d217574a7.mp4?token=nRCOCrb8cP_oMjg6sMK0AbDgT6uwSCgMimdb2hHKyJlU0jM40U9duWrGNWd2ICMNnRNCYk4uC0fjS61l9tBvPuo7aOStYEGX-e7uQyJ7Md8RcvpbIjYTlVhq5lXI8KdKkwAChWob-vHsnLwOdrkUakgd5lMrS_K_n8X-9Zrpj38UWHEZHkJFpjGes3uP3ZIpGZ6BP7uloTjNLMdUKA8NbiyTDVSBWbBn5uS6RSt8MN1mFtcgZcl_P6m10Z9G-HHiUg96Z1p0qolgwLHRWTfL0XU2OW6mLo2EGWGdPGuDJdTKP8k6KwCQ1t3vDJsBfhXC38CBkDXTY4wKxkn-tHsToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع هزاران نفری علیه صدراعظم آلمان
🔹
حدود ۱۰ هزار نفر در شهر پلاوئن آلمان در اعتراض به عملکرد «فریدریش مرتس»، صدراعظم این کشور، تجمع کردند و خواستار برگزاری انتخابات زودهنگام شدند.
🔹
معترضان همچنین خواستار کاهش هزینه برق و گاز، اخراج مجرمان محکوم‌شده و مهاجران غیرقانونی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/455001" target="_blank">📅 17:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2Kge2nyAN4-elTRRw0Slhd9e55aZqT7ruwR0R6f-H4IGy7rElimqPOi0sQmHB9XaQbkNBuF-eakgsyRIphU1bHM_fFiUtAkIEY0iHa0S2WSa9unTuajGcDuqcIzuE_ySwW3i0luhnsv6V2fGsr35hf0jFU1TDHFF-_8u-H8NLzJQ82gkS3nvECd4OEH9LjHn6BVBKJ3zOlMsAU-lLA5wNY-kRd27not3nATmbYQfMuVJMjx5_j-utHZvwNKC2Px3NF9gSfx074JYhkIXIeO6c-YkufP3xdg9iLCgMxnT8TNU2PVHIKDlNZ_fRS01p1jmw6LTbicDWlDHM3-j5V2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnxjt8Bjkq5qBPjeHc-dq9RzkC223_7dn-LrQpXTa8_d1DKhFXWRkHsb5wg8XCcclKsEcq9Pi3wBtrGKTRmYneUVIDG5GOyn2D48wUDacvXAQEqQ0Rn6R0pt8S8f7HYXg5dvI9Uq2Yy_oN6AEf1v7iAxIzhjXjCxwXaieF75NP6q8K9tl1g6Xo_jVqcj4NgtT-30MtlX07EHrZKbtBEcdzWX8chfJeKNT5lthMpNuWI3RDL0Dlx3tmZvmh5CpeTH5BHEyx-Cwr2tyPDlnHHeunkKNTM7pyGVVPIjmn7xm054-al4_zb6UuVqZ1dEuPClKvSGEblkP6N7IPnwdpe2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9eJ-f-u7W5qpEHH3MRL05ECr6QjGncLfKvPbuUglcH3Y6BTG94M5azAVOQ7WRn7elnr3ZHsUuDNzo6kUCrgXp3wQIcrPT02qRcWUanKkrC2LqIblPxfquyTFno3CaCvxVhpJ3t8SHaEerMcHaqdukugcE3RDCuakZ3VIU4R2rPCmtFSQUp7Q_dV6PFeeToBPCsm8Jep8nbBMxA7E4aIgqenWPp8BHJBl9UUP0AaiZYJAJTNr6wHQjNrsJ28ykiUvDqqgWYKUubM2MISS682XtUQoj2a-hX5IUmZQ_bUjX_IofBJ3pGg1xUmY90icnI44Ha3seLAYCQnDdOok_WvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOmhdzOFqy-kxK3-DQ240N72aKg9nAIJoyU3cvxNYY62xz37iGyX8ihvXGWG-MSVdTy1VXrXXuWmuaDC0f0KOLt1YyNNSTKRUnaJsPaCFCZdecCCi_zWA5CGrx6SGQcYFLtNj3VrXQbV9S7zoDcAjK8cE4DNfHlvJLdDj1mHDo3A0O5Sbd0BC-dsH35Ij-BNuk9B7E8vW9mQnGs8pOTfv6WRc9Pg9hh3xxwPUNts9Y9C21TrGtsf2MC8zaE7AP8a8t9ANEqJ1Rnn7I8-NM07_-ZoMk9uJBC0qJa0hsANyjCO9ZJRPWcE6m63iEqjucIZJ6aqzPSRNOKERqZrrqd0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_sArapUqeA8kTGpK4qcDGQVdP1EtUsn2ovBSgICEI1OPzSpoTDHCPNlUBhpHHE4D2AjXMEieVYAnkTkkJ6YNR3t3YETTfxbu8Hr5AZgrnqMHqt8nK9cTOHcuvNaRrq2c850ZTn8mrZuYKUU4pBZYWSEhX6RiK0GaU3V1Xc86lY2J4biq36AbgE0ogMfX6gjaZwWZwfP3e8u82h-XYWQYkDJdHjy2DrrXpP9V1gUswSlBQVkQIfWcI-sLe_42YFeoGX-N9Ga5DrCB6rX587z47IYsvIbRRmdcb5eUWp7zYdqw2dQQjKtyuYkr7Q4KBIUYf7NFRl-CRr4dXunAt9M9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge-dYJOG47Ewni1LTEt9YdRWTQkp5YyXqUzTOrr2nkZjluJ_nZoX8MFCoD7xKCBHny0ilWiDvlhvc1_1q6J2_7DOUU7Ax_r7yOeShm9L57If4hE6bo2CMOLahsfRNwdQl83IM2Tu8if-mdByS7D2ImFzPVubO3KMY92dalNY0Yp3kGt5SCE60y9dkWZ1eVtaL6M3XG5o45x0lgzqEjI_zOUl_UeE9ZaiB0H7DqiGV5Tefc2sPF_E3J3__J1-a2x31mQ1Q83sMYb3hguweTZsGnq--Ack689GAsPmHM-4mFMav73i1D8NVYMneLTuhShjZQZ3fkVgDJYuBL4KLLiYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq8okoy9PQVPaOWyRhZfYIwJ_0S4lBvLQ6Z4-Hi8t9YNMys3vfHlQIAmfapSpusq15ugyRuAUA6dAUfn91fxiYLjkavHHOfo9ZiH4C0taxuUzJw2aSQdPBL6VscbRbXWZeCuaz7ur19rmnTWn41T7ZxEG1wlMGIgVJfgd9ErD84AG9oTJpq5NAg63pMlXAa2c0lNOf7j6a0Y-mRB9S1J3COAZN1-4uU8_AjctpVqRHOHnaB7ggYS7IctkVMD5YOqpePE27TstWvAXcuO3ePTLxkJGcYgdyQ83tOsuUPKu-eSh0HitQiW7CDejhE7jVWBYj4-YiM1UC3trDYV8IinJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس صداوسیما مهمان خبرگزاری فارس شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/454994" target="_blank">📅 17:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e3eaaab5.mp4?token=ap_UQ8e0-1cLjeUXjeLKswb0AnRmy_a0KrodAklOUmlVxgBd4rp_-T3uAedJCUqVQCBepIHZXpn3ifDGbXDgA315awZMg6se35ztcZjhSQDZ1GFojv22gcaQEUzB2cxTSJT0AGDpXGshLHfw_bc69eb9BdU-n7OkoeeWn6l4XHaCQfdPFXJ8aZlz7tDLud8CoYfDB0j7ecPukcYqWW4fI7Ego4R2ZN46wnAu9467XPACfDyAdCFLhsYxmZbAYpsvIXOkqUasurMpVp3FHt4_WBqrAUTgmZ12R1T_6C4TT07mCRmNH_jHAPRyLCsMPyhuyUIrlpbud8TtshFYAEahlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e3eaaab5.mp4?token=ap_UQ8e0-1cLjeUXjeLKswb0AnRmy_a0KrodAklOUmlVxgBd4rp_-T3uAedJCUqVQCBepIHZXpn3ifDGbXDgA315awZMg6se35ztcZjhSQDZ1GFojv22gcaQEUzB2cxTSJT0AGDpXGshLHfw_bc69eb9BdU-n7OkoeeWn6l4XHaCQfdPFXJ8aZlz7tDLud8CoYfDB0j7ecPukcYqWW4fI7Ego4R2ZN46wnAu9467XPACfDyAdCFLhsYxmZbAYpsvIXOkqUasurMpVp3FHt4_WBqrAUTgmZ12R1T_6C4TT07mCRmNH_jHAPRyLCsMPyhuyUIrlpbud8TtshFYAEahlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی برای خرید پدافند هوایی به اسرائیل رو انداخت
🔹
رئیس‌جمهور اوکراین اعلام کرد کی‌یف آماده خرید سامانه‌های پدافند هوایی از اسرائیل است و مذاکرات میان دو طرف در جریان است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/454993" target="_blank">📅 17:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcfEPLHCy517e3dGoSR7KD4aCkXXxZacJz2EiFfoF89CzzYogaqixgqodGulaR38uAF_uBxDMDugZi3wK04ljXZOMFCpsvt9ZbpQlKek8OV0GQUsUq_4z5m6sxNw-HlVaeQ-SD8Nz2xUh6YjZalnXWzGTyrmw2hrWymR_Z5QIjdlmnMqUoo9xMnKacGkZ3rtWrM1HlXg1Lbe6S8erTxvoXhsjdrx_nUVw--aKwMdoekjAlg6WAKHYu1N3rP5oTLYU-R8yTvAa7GqYZjixCWHEhu8vaafdjUZB98VuRpbVwiCTk_6MZG0CuF6hWmv4INQERzW5T0xcZiFbwSDxJrM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگهٔ هرمز باز نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/454992" target="_blank">📅 17:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8e551a9.mp4?token=VX-V9xPdLOCyAhbx2ot5F7r3TSwgt3vT2zzaaKkgUMOcWiar52gJ5PW6XajsUmLwkEvGNeTcSE8JtPLag1xkNeaOyTQIZ-9qwTvilLiSNMmDUIryua6xhJnZmuKc7MnXqZ70HvTjflY1aEBZfPXhMBzbO5FrJCpFhyz5ALtRTfYfkha1fVApKZ_kzAQlOtx2brm1Phe5B2yW-lJkQxB6VAJJ7jvYiIuVmgOUNHuIl9Evz9jITFN423fms9zh0LEmtZ1dv-F8W6qb_jn8QT-4nzQJbISvT-FX6wQpB9Y4yC67uPbrp2-m-iVyXKEIopR8EDuPgY_ANyhsDs97DNS92A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8e551a9.mp4?token=VX-V9xPdLOCyAhbx2ot5F7r3TSwgt3vT2zzaaKkgUMOcWiar52gJ5PW6XajsUmLwkEvGNeTcSE8JtPLag1xkNeaOyTQIZ-9qwTvilLiSNMmDUIryua6xhJnZmuKc7MnXqZ70HvTjflY1aEBZfPXhMBzbO5FrJCpFhyz5ALtRTfYfkha1fVApKZ_kzAQlOtx2brm1Phe5B2yW-lJkQxB6VAJJ7jvYiIuVmgOUNHuIl9Evz9jITFN423fms9zh0LEmtZ1dv-F8W6qb_jn8QT-4nzQJbISvT-FX6wQpB9Y4yC67uPbrp2-m-iVyXKEIopR8EDuPgY_ANyhsDs97DNS92A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آمادگی رزمی مجاهدان یمنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/454990" target="_blank">📅 16:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730c164f95.mp4?token=NhFGW4D2M6MdYJUQJ28MeSDSsSeITiLrmj4x57NsBgCcy98pkQTopBvuJEbJv42ONKNeJapuKUtkbpxDvdkiBYK44f9Sv5CYpbjpRyVcNLpyfxT_cCarcfIX7-YheyDN96S9VC4lVJzYxiBEGZPdt4MYpFWzKmFEnO5IHKv924ryL_FAlEGgeT69I-Zb2jLzXhh7dcVLWVdPZkgXh8zw5JmtOgJmaUILvEPNX0qRVKXHIjBitdPSzOXqagYAifVPt3zL9h051rThLhLR3AFrIp0itZG3ZPiV49Uo1hh9SAMmmSMKml7p6G8MeKrQ9Eg_lXkn1dA_iEYip2Zgfkfzr3u0PgDXVidhFeC3TdKPpBUyRVSQ3SZtawtTM0PX7ha_gZJPujvTkIJZ6L0vvRZ9TDuQJFK7G7uG5bu-0_jv7pMCozZR_DNBOZXZJB5rBqb2EaQdvxdCjrMDQHrWMYEhLQ9fZCK4Zm3uNKwz1OcyDanuG-tlyygD5e8NW8IYDE8iWsEipi-NMESAS91vjzt-prUXWauCUQ_TDL7Op1dSnI7fFml26U5U3K_fkMMe-ZAssLwugSTxQp4Vd1C1BoTaPqAIX-cTAJHxJfJ-vlb1LP5JsY8zGohs8ZoDBAtpsiFfWWy2ZSkBCiJ7D5VYMmIzQOMbQAkoLhZgLiXqTE-UywM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730c164f95.mp4?token=NhFGW4D2M6MdYJUQJ28MeSDSsSeITiLrmj4x57NsBgCcy98pkQTopBvuJEbJv42ONKNeJapuKUtkbpxDvdkiBYK44f9Sv5CYpbjpRyVcNLpyfxT_cCarcfIX7-YheyDN96S9VC4lVJzYxiBEGZPdt4MYpFWzKmFEnO5IHKv924ryL_FAlEGgeT69I-Zb2jLzXhh7dcVLWVdPZkgXh8zw5JmtOgJmaUILvEPNX0qRVKXHIjBitdPSzOXqagYAifVPt3zL9h051rThLhLR3AFrIp0itZG3ZPiV49Uo1hh9SAMmmSMKml7p6G8MeKrQ9Eg_lXkn1dA_iEYip2Zgfkfzr3u0PgDXVidhFeC3TdKPpBUyRVSQ3SZtawtTM0PX7ha_gZJPujvTkIJZ6L0vvRZ9TDuQJFK7G7uG5bu-0_jv7pMCozZR_DNBOZXZJB5rBqb2EaQdvxdCjrMDQHrWMYEhLQ9fZCK4Zm3uNKwz1OcyDanuG-tlyygD5e8NW8IYDE8iWsEipi-NMESAS91vjzt-prUXWauCUQ_TDL7Op1dSnI7fFml26U5U3K_fkMMe-ZAssLwugSTxQp4Vd1C1BoTaPqAIX-cTAJHxJfJ-vlb1LP5JsY8zGohs8ZoDBAtpsiFfWWy2ZSkBCiJ7D5VYMmIzQOMbQAkoLhZgLiXqTE-UywM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت تجمعات شبانه بعد از ماه صفر چیست؟
🔹
قائم مقام سازمان تبلیغات: «ادعای تعطیلی تجمعات بعد از ماه صفر صحت ندارد.»
🔸
همه ساعت‌مان را با ولی‌فقیه تنظیم‌ کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/454989" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juB5ksZICtcnIl2APqLud5jnRR76rHKwcwG51to0ECcHPV6dNycX1qNcT_KrseNVgjzehXUd_jKysrleF0dCOo63TrWYZPZHHSC56Nu6ZNhs2Ifq699RQ9i8DNH0PjFke-vFuxpbmglQjQHpX5Sz9EZHXFtjGNE_c_pCvAOfWYZu029GGMW09ueRHfH6f7n-AYZ_73lMPRp8sb-unV0rKh9BVb8yLCWx5daFaE4O-sHCZazccSpZ9y8zFu8FQYRfDYJPaoIK1UVPBFrS-1StvZHImkcJu0wiW29KHtpnXgST6cf39v2QDxUSftvMw85jZ54oFexyayxL-hrkdFIjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش‌از ۱۱ هزار قرص متادون در اصفهان
🔹
معاونت درمان دانشگاه علوم پزشکی اصفهان: در جریان بازدید نظارتی از یک مرکز درمانی متخلف در شهرستان تیران، حدود ۱۱ هزار قرص متادون و ۹ بطریِ ۲۵۰ میلی‌لیتری شربت متادون و شربت اپیوم کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/454988" target="_blank">📅 16:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsoolZ3RyCRFEGa1MQcHmICHoTPbQLeselALiDqy7UdqeBZdu53ybeheVo0F0aqcEeUlDNAN0JKODmYrBvcrG9eO4DwE5ZKAOjbgIerWgpsyTx5zpTTDCprJ4_65Xm-DzDnZJERKvB5gX7NPOqqIKmhexbitqxsedAbk8uqO7v5MzdxGw_edeQWra8mZkSgKp5KMzbRO9IW0VXf8JEKvUXwFs51Ovc9JHi7FgeXPDXM8-4d_W3k0hAG-LMXxEevpD0tpkqSSTxNdXpTW33RXmEwY1L9AyZrYuyV_GWGivryvXPDw-DnvaNKpRwqmi737ajfq5Mp0gzGmcFKwW3kDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: رهبری هر تصمیمی بگیرد ما تا آخر ایستاده‌ایم
🔹
اینکه ما بجنگیم یا نه، بهتر از من و شما، فرماندهان جنگ می‌دانند. آنها قدرت خودشان را می‌دانند. رهبری تصمیم می‌گیرد و هر تصمیمی ایشان بگیرد، ما تا آخر ایستاده‌ایم.
🔹
تکلیف جنگ با دولت نیست؛ هم در قانون…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/454987" target="_blank">📅 16:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al8-5wqTYNqu7WI6iGXmP02X7KjnDdxvs59N4AxQC5IxnwcmWk2S1t6G8gQW32ql0dxRsHKjZ7EYkSy2UI0DMrPfG2lHKgo627aFjdZZRYlmTuGLaqN_PNX4WZ54KUtBPqnQJrr2lhFjo8hLS43rCBoBPhLxAWe6G4-xZIQDoNlYU1NrSYfyHCZdb-7vNMBf06raOX_w3vVnTw1jPT70LWIILWvEB6Ynr6OSmN1bDvibZ1vzU32KdcHHhzxzVYbZzTqX3WbFZOIvoh8dT7UEukeyRNLC8Lz96YLPO9Q9d_DNcb0xeuHv7G6QFVHjZJs5ySGFzzazx1NDPUyGypdZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n46ydVU4afVbLhen27cNmdgyDlZ-qv_o6Ip7TJy5OHo9Pz-1DJFYNnfZLWK2xeVfqaJMX4ms-DyRUiahGJuk3zqo-YMgfET3ITIaIKC6VOMbSULQsqwm0AS0aZZCVS2rthqQTb958D6PPDlo1wcWKjlqIt01vyrpCgLx-9cwoCUV3s5wsDfX8AshVmrkwIZcKRzJ1jbjfvJ-ok6ckWKqeY7F9SxNAjNGDvJmVt785f34N9ZCnGmcwHclNxBv4DT2W3j-VGRgKwfcSMepJefLuk3pcrri54jiQZM3x4YNkjdeCHyRxb6DH7dhwh4q72ysMKwOANCgmlkEQB6TVP98gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjbumdQ_870z637tPdR_YbgXWbRF4kOC-HscZX2J-mrNuVq_cF3QT_7Unu1_XgEXup2z22q9In-hOnbbO_qjqZ3KjXzfrRZmciVkW12UymnR4zCrOf9FPwLhmtgPj13iRBnWDhSRRalpRBg02H0JzTPLYi4RWQZHj6RPI3NbV2HO8V0Oe2V6-Bl1GAI_S9L3CEAS1-gLE2bv2TEmasJ6K92pBAjUEwt1yYtT84Up3g64EkoHkjmAzk2Ii2bCE3pM4eAKA-S0JLlNV0DHH6xmeeJcYppHUNgmEwd9WCjPo857FOG00sR7-NtbZjc6XYRcdz9Kk6hbhG6u-TWXi5_Peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0vcuMnjyYdYvjyLjUjrJIohx77F4eZpY9C4m7HpPEMwf4Cr4-TKgR6y1WT8-L1u7Fsw6wkw478UqsnlweXK1xDngkCYYovVL8iQWrDuU74eUoXK1sYDW1S9x9McgWU04wpmEJDQST0hhcb9tupbwr-mOZk0g_1E4kOzhOFu_b_eABDqNnmSHO8latov3KI5Vna0-JPue6rmw5ehNdz7LhgMejGHI2WpwWP11Ct85ShajXarlLcfXH2UyCCJ25o4ggYaDA-dCJ240ZT-l9a8oWZolJ7N3NtESmRPHh32dtlLStWjHoLvW9DvaCdbyEnR4duOEkb0tzd-wsvnSM8kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNdGK9xZl7Uw8HGRnoOfKBsB5Q1MjAFpNgVSz0_zYsbbOuFILlRIgt7lGYuNrY548nJ_3yfM7oYcSutEVwq4ShXkEkVY_JNnpOrXLGaoaQ_OHgMuVwmoiqs6OD1T79h7JFEkRnjB1n3SJkcEJYxjX_5KkV5oFUW7oFBuB228ZqF5zBXbykovGONf5fNx0gi5X6iNPwNX1QIekZ2srNbe8gK9MN3kB6l7TEwKb5dLzzTm3q0szP55sd0cbZSr79iwDw7vgKKaTI1gVhBleyWY6q-WqbmFSWqCkNCmLFPHCzZ88Y6vlba-JdB00GA-oUnUxYJJFkT6P1mUwCGWtBD5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر آموزش‌وپرورش برای تبریک روز خبرنگار به خبرگزاری فارس آمد
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/454981" target="_blank">📅 16:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
تصاویری از عرشۀ کشتی متخلف که توسط نیروی دریایی سپاه پاسداران متوقف شد
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/454980" target="_blank">📅 16:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlknirmAdYYgK7wt2MVvChshznkbc_xH34YiWORvp0RTvZA_Sjn_T7-qB9puJ253dDz-sjOW-A-j-jZfyCAs44TDY2NmNRK5DwcM0P3bjB8m-HKfAINtKLLxJN7f0cDWIERRMnqpKFMFMrXtCnBc9HOs8kbseNQqqqzcp5eSWksvNz_zyf3Nd599OISDf_gZq17yeuRSpOR7Ek6XEmrVeXMeB2L4ZLohap6KVfWexa_11MXnlW7BkCjwS3-GlqcSiqd53BKDnX_dFaXDUie4roRMzmz3s99ZQpyg5kV3_bTEDT8SEVzNiqSyCYEVO1t5hdAE_asprXxJDKqrUPJavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تصمیم گرفتیم اینترنت باز شود
🔹
بعضی از دستگاه‌های امنیتی تهدیداتی را در خصوص بازگشت وضعیت اینترنت ملاحظه می‌کنند و همچنین با توجه به حملاتی که از این طریق به زیرساخت‌ها انجام می‌گیرد، نگرانی‌هایی دارند.
🔹
با وجود همۀ این موضوعات، ما تصمیم گرفتیم اینترنت…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/454979" target="_blank">📅 16:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4933f2ce.mp4?token=MoAe63u3FTxfZac4u1bcjPlRSloCIE7Qz11k-aGVouOTALQLpa6XzaE3RNDIRlO8cyjI6eKJ6FRA4E_dZ7gaGAtugLXM97MIlT1ATrzPqzU3hbWeXbHYykyloqw4UAFaLSJGOKB_WXtEn8pKHsG_viUAN8lJNmanTJrJGDP6ljWljeDY9uE0eE1PNpJJX-3EVsg97BdcEKMG08LkSDL9pSD_qhqjp9ka_lErw3UFjOWwLxSgRs0PRwszAYfSvzqlwafQdb3l6seVEaxGSftv79GqnpjrHX_vgFt-Lp6m_J8U7XuABqtTnJs5yqCC98bugSEX-YbUw6LzHpC92yG51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4933f2ce.mp4?token=MoAe63u3FTxfZac4u1bcjPlRSloCIE7Qz11k-aGVouOTALQLpa6XzaE3RNDIRlO8cyjI6eKJ6FRA4E_dZ7gaGAtugLXM97MIlT1ATrzPqzU3hbWeXbHYykyloqw4UAFaLSJGOKB_WXtEn8pKHsG_viUAN8lJNmanTJrJGDP6ljWljeDY9uE0eE1PNpJJX-3EVsg97BdcEKMG08LkSDL9pSD_qhqjp9ka_lErw3UFjOWwLxSgRs0PRwszAYfSvzqlwafQdb3l6seVEaxGSftv79GqnpjrHX_vgFt-Lp6m_J8U7XuABqtTnJs5yqCC98bugSEX-YbUw6LzHpC92yG51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محاکمه علی‌ضیا و امیرحسین قیاسی در سریال آقای قاضی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/454978" target="_blank">📅 15:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff4245438.mp4?token=P4mOON8pczXdJFWBuy61iM3WbkCHyb8ZEQMXsNehzKp1EB34Ddm6-EwKSAz4Wi2mvZzXDlBni5Azla6PEAKYcf0ZMIqOw2Ivt5fsuIwvJmZxjM6rctood4aZ8ev7bPZzkRI9gYK8pVMaja1WxlJPgPxh1ES_XXkEydSQdXrSbJd-uiazjQXrWkFmapk0w1j59F26aTfMEaw_K7_f8xMXC5h9DNUObfdUSLtJPf110fkkP7BMRgNCikMevszuyYkBoewVu7tuco02cHjIlTP1jOmlSqZrcEbrUKhyROdseaNNVJW1kUaDuVecq-p0bxMd5cfqxfmbyh_0IfEQhxmKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff4245438.mp4?token=P4mOON8pczXdJFWBuy61iM3WbkCHyb8ZEQMXsNehzKp1EB34Ddm6-EwKSAz4Wi2mvZzXDlBni5Azla6PEAKYcf0ZMIqOw2Ivt5fsuIwvJmZxjM6rctood4aZ8ev7bPZzkRI9gYK8pVMaja1WxlJPgPxh1ES_XXkEydSQdXrSbJd-uiazjQXrWkFmapk0w1j59F26aTfMEaw_K7_f8xMXC5h9DNUObfdUSLtJPf110fkkP7BMRgNCikMevszuyYkBoewVu7tuco02cHjIlTP1jOmlSqZrcEbrUKhyROdseaNNVJW1kUaDuVecq-p0bxMd5cfqxfmbyh_0IfEQhxmKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی در برنامه سمت خدا: «اول مثل یزید را بشناسید، بعد به عزاداری سیدالشهدا(ع) بیایید»
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/454977" target="_blank">📅 15:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faDCY-rC16be5xAs4rYpP7L0U3EmlKIRSnvT4rfr9joxUYt3qDsq6UxABf5K-LAKL50_5Q_nB-LzvCs5Hvd6zDC4cNl3ftANr7VSVwufeKeMSguVkWHO69s0bkMwBvUVeT-7GerYCz7S3VgK4Rf-KAyGqPTDpOX1hGzNzVEV3FjtM0PnGWPh_t-xF3DImjVlra2thI-1xIhc2_1E-3fXDBkBanBCaODR-QZsPTYAMsSqdSGBDwBK02sl__r2vKPS0lDkmkcgtC9lpRqLiRwMx1ElFT7tzn17BtUq7A_G8K1wJt13rXBfWWDbk_ijGIrsnff2Jaip4HCTUSXB4aq7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مهم‌ترین نگرانی‌ام معیشت مردم است
🔹
امروز مهم‌ترین دغدغه و نگرانی من معیشت مردم است و تمام تلاش خود را به‌کار گرفته‌ایم تا به هر شکلی که ممکن است، مسئله معیشت مردم را حل کنیم.
🔹
جلسۀ دولتی وجود ندارد که در آن با مدیران اقتصادی دربارۀ بحث معیشت مردم…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/454976" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84526b2bb9.mp4?token=rTLkYwhR2xeyaxUatdAJxckvPr4dAQLCxOBV1X91on81em3TYmx9fqxqKuSq7LNuRuIS47ajVdBaW66L8M2scHsaiBn39nCo6fiHSV6yAO6s6AVV2lG9WZfjvdzYqH02oiE9VqMxouGGgLJgyjdyBjRD9QmfRpLwxFYS3PMW2TmwQpXT8KMJdmdTRJ9KCNhelyuC54D7i29PpC5ycZAjR4rtjk4-b2PZSypVnHyUubeC_50SV0UPvRlWzyRQZm4iSiopfN7PBA4vj8akcCxpabQp8VBPVLcjnsMhZSoY4aBST4wWg4GE28UIbN1Bw8863RBeq-hDrkMWY15rTF2aaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84526b2bb9.mp4?token=rTLkYwhR2xeyaxUatdAJxckvPr4dAQLCxOBV1X91on81em3TYmx9fqxqKuSq7LNuRuIS47ajVdBaW66L8M2scHsaiBn39nCo6fiHSV6yAO6s6AVV2lG9WZfjvdzYqH02oiE9VqMxouGGgLJgyjdyBjRD9QmfRpLwxFYS3PMW2TmwQpXT8KMJdmdTRJ9KCNhelyuC54D7i29PpC5ycZAjR4rtjk4-b2PZSypVnHyUubeC_50SV0UPvRlWzyRQZm4iSiopfN7PBA4vj8akcCxpabQp8VBPVLcjnsMhZSoY4aBST4wWg4GE28UIbN1Bw8863RBeq-hDrkMWY15rTF2aaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت قوی‌ترین مرد ایران از حادثۀ میناب
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/454975" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX9NL1EzKUr05d38iO9VIon1wVURpJXTX8JbFzC4NOFnGcFsA96noMii89YDUXT-EhKZjEzhuHBIFwa8S1rpTGM8UwXISv5rk5ETrFgAVOjOJswzPgmDgnq7qf6o-O5e-jf9JHcuEd2XHrzV558ZCI2tQ47zsevM1mjX5yDXS_qulyROjPGJhgxcBaynvnPpZFggGlMxCo9EwypujMw3j7WBfH_1i1-PEfPsqIZav1hVirWN3YQritBvTZBZRC0WUVgI2yasJFB_vG9PogbV5LOD-B74eDUBZQlEYcsiF9uGvfrEJdfXY8zm-sfCSxvi13wbABNW-ybcyZ4GSMloCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: در حال حاضر کمک خبرنگاران برای ایجاد وحدت و انسجام بسیار مهم است  @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/454974" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4110a6cae.mp4?token=bCjSmfx7TmBGsWM48T0DRfWphn80igCi2ED6Pl6aItGzvBLd4Jy6qKE8cJurobloodDb3qmnVy0v0F9h1K5fbjlqaSiy1HGsvi4Vdt6lVIXqflKezb1awViInbfXqpJ5F0409PuiaJucu67eqGjN_L5BDyeqs2-UQPBpZCSHJBk06Xj2A8yJ5J69RdX02r4lsSUDNXop-qHb8w9-RPST5PA7WR82qxXLY4FzsHQP3tprzgrIMMukYENXPblxyQyoQaFMhpkHvtpt-DhIwsaDi0jbwQo3k8dxiJzdBDdQIVrLQkqEA3S8WtMeWoCFzFV8vRFBCzpm5-BPg_ClO81RDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4110a6cae.mp4?token=bCjSmfx7TmBGsWM48T0DRfWphn80igCi2ED6Pl6aItGzvBLd4Jy6qKE8cJurobloodDb3qmnVy0v0F9h1K5fbjlqaSiy1HGsvi4Vdt6lVIXqflKezb1awViInbfXqpJ5F0409PuiaJucu67eqGjN_L5BDyeqs2-UQPBpZCSHJBk06Xj2A8yJ5J69RdX02r4lsSUDNXop-qHb8w9-RPST5PA7WR82qxXLY4FzsHQP3tprzgrIMMukYENXPblxyQyoQaFMhpkHvtpt-DhIwsaDi0jbwQo3k8dxiJzdBDdQIVrLQkqEA3S8WtMeWoCFzFV8vRFBCzpm5-BPg_ClO81RDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران، مهمان تابستانی ارتفاعات دماوند شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/454973" target="_blank">📅 15:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۹ مصدوم به‌دلیل سقوط آسانسور در میدان آرژانتین
🔹
سخنگوی اورژانس تهران: درپی سقوط آسانسور در خیابان احمد قصیر میدان آرژانتین، ۹ نفر مصدوم شدند؛ خبر تکمیلی متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/454972" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqvMtRS24Rubu2X8fAIK_2gBL0TtEBao1irZcX7duAmu9c-Oyw561SbVceYvAZlsenk5RPlAv2RosnZ0sZs_7HGo3EyvSo3U6e_u1tfm32C98qYXa39NTX_yt3mfNlTzLotUVV3SBPazFRrPoYFybeXn4xewXO35_0c-2JEICVoEg1PG1EwwEpbzXMZKWSErC-QeOPLQxsvqt61PGl_FtBJg4uEKLxr_cezEpdhE-uXywGBUsYqlOSy4SC-yY8MdAGLPlja12HrXueS-M9suyUMu8qDbKiyXQPyXFVTS_9QIjy1Ud1ZeAojaeODyvx3o-PZSh8kNY9vQR8KMS3lnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل میزبانی استقلال و پرسپولیس در لیگ برتر مشخص شد
🔹
دیدارهای استقلال و پرسپولیس در فصل جدید لیگ برتر در ورزشگاه شهر قدس انجام خواهند شد؛ بدین ترتیب به احتمال فراوان این دیدارها با حضور تماشاگران انجام می‌شوند.
🔸
دیدارهای لیگ برتر فصل آینده از جمعه ۲۳ مرداد آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/454971" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
رسانه‌های صهیونیستی از زخمی‌شدن یک نظامی ارتش اشغالگر در یک «حادثهٔ عملیاتی» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454970" target="_blank">📅 15:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b0e75560.mp4?token=vnQoHAGRkFQ6c6nsjhyElnxNXf-drgZAt68rBK5WWR1mopjkm-0i0TZdpuZaSVZIKV1CTKwPL0F2dBnMCgkXycmWYRGuO9521GetkA9v1EndY0fS7-HYqf_7My3gTBY-CaVzJjS7xgGpqT-Hul2e_nJhLSgG8Yz_exHctWkWXsny2Q7WphDJ3WBYqu7OHl-OFYcjTapdLn0kCEcx6ZlpFsHiISCPzdyTIS0QpAzaJucLhHdnAvGZgcpGRr7IQYmX0nsE9oTFjnLOMtk9gaT-8GozGlFmItjJHcX-5ZUE77iNWUF4pLjNqL-RrBAhvc-xpu-au4noy1qw-jax3yn_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b0e75560.mp4?token=vnQoHAGRkFQ6c6nsjhyElnxNXf-drgZAt68rBK5WWR1mopjkm-0i0TZdpuZaSVZIKV1CTKwPL0F2dBnMCgkXycmWYRGuO9521GetkA9v1EndY0fS7-HYqf_7My3gTBY-CaVzJjS7xgGpqT-Hul2e_nJhLSgG8Yz_exHctWkWXsny2Q7WphDJ3WBYqu7OHl-OFYcjTapdLn0kCEcx6ZlpFsHiISCPzdyTIS0QpAzaJucLhHdnAvGZgcpGRr7IQYmX0nsE9oTFjnLOMtk9gaT-8GozGlFmItjJHcX-5ZUE77iNWUF4pLjNqL-RrBAhvc-xpu-au4noy1qw-jax3yn_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر صنوف و تولیدکنندگان همکاری نمی‌‌کردند وضع خیلی بدتر از این می‌شد  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454969" target="_blank">📅 14:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665efbb507.mp4?token=KO8CkLM78EE5X5cVlwM-aZvh3h8PrIZ0QP8lG7lx59dAtyUDnHabLJiogHrsgjqOuRpyksS5G8J7oToza2MK-qNc1PRupXZbgytJ-no532qLxdRe846JP7fhbfqQadxg7O744Jr48jr4bUd4VQSoDb4lkx-YcvqqKaag7mmJOMxNeqLE4kfW2CFZzYWUddFDnRP-FZVQry_REFb_NExzNa36oowytSTLZFK3aOSIAT24nEp9dyesjr_A-m8kZFvQIWBku5RF7PslkjIvuuDbKRFd5YwXEpWOlCK-sOINNee9vko-j_xXmhKpJLtnnawjRoSEv9ISmrL8U3EDxZaEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665efbb507.mp4?token=KO8CkLM78EE5X5cVlwM-aZvh3h8PrIZ0QP8lG7lx59dAtyUDnHabLJiogHrsgjqOuRpyksS5G8J7oToza2MK-qNc1PRupXZbgytJ-no532qLxdRe846JP7fhbfqQadxg7O744Jr48jr4bUd4VQSoDb4lkx-YcvqqKaag7mmJOMxNeqLE4kfW2CFZzYWUddFDnRP-FZVQry_REFb_NExzNa36oowytSTLZFK3aOSIAT24nEp9dyesjr_A-m8kZFvQIWBku5RF7PslkjIvuuDbKRFd5YwXEpWOlCK-sOINNee9vko-j_xXmhKpJLtnnawjRoSEv9ISmrL8U3EDxZaEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا استعمارگر و قاتل است
🔹
آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفت‌وگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454968" target="_blank">📅 14:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c6712df5d.mp4?token=F2Z2T5spjtIb4f4wJ4FRiPpvTnLwe-B2FRVpbiDfkZylaFM9sCZGsruycbWP6ZtrN4U6NhcNEjy-N1EDOgwfDZtMsx2wDh4RkKZ2h2EY-LFvJm3I6iMnr_Aiju8gFNmkxQCMa_3wDVYIhz5BxJjtqZqBIa9Qs31qFkp9gYVwAQHti-VeSBQWGpIE8Fd3zRC0GjA8goEIemPtqGuR1KlPbUrM3qdij5qTDKVNeH8VYOHDDMDnAvX4EQGHvDayyXWLzntYpODcZe0CZfraU7clZHmw3a9xarnNC2bV74wNmrXmdZhgPIJSEPzYdRePZgpqLQN1LCT97K_oerP9TClTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c6712df5d.mp4?token=F2Z2T5spjtIb4f4wJ4FRiPpvTnLwe-B2FRVpbiDfkZylaFM9sCZGsruycbWP6ZtrN4U6NhcNEjy-N1EDOgwfDZtMsx2wDh4RkKZ2h2EY-LFvJm3I6iMnr_Aiju8gFNmkxQCMa_3wDVYIhz5BxJjtqZqBIa9Qs31qFkp9gYVwAQHti-VeSBQWGpIE8Fd3zRC0GjA8goEIemPtqGuR1KlPbUrM3qdij5qTDKVNeH8VYOHDDMDnAvX4EQGHvDayyXWLzntYpODcZe0CZfraU7clZHmw3a9xarnNC2bV74wNmrXmdZhgPIJSEPzYdRePZgpqLQN1LCT97K_oerP9TClTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا استعمارگر و قاتل است
🔹
آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفت‌وگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/454967" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a509aa35f5.mp4?token=fBnNT2c1K88iPPOLRHHnC17hYp6eaD60Y7rmNHpTNh7YY5EGB1za33deXfNxG_qIDmDMvSXn5JwBWdV-UTqOjluYoM_sn3daaZMJ6E9f9r_1kM3-uvA5v0tNaLjDnqUp-If9-OSypO4B2qhjN78QkgoZnVAo2-YCHuJMnlXXmffZyegLxToDzYsyz-gNr6HKNzd9U2jP2z3RO9F18RzBSiHxTYjKb25jyIedifmol4v01rWw8NHNBY-p4s1T4mLjiXWdFHb81RqIbH6iuRDjjlNrZjzSTtkMfuN8jrEBAcl_ifSISr8TNmSUSagiovRfUozIsGbQhRK20GBJerVhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a509aa35f5.mp4?token=fBnNT2c1K88iPPOLRHHnC17hYp6eaD60Y7rmNHpTNh7YY5EGB1za33deXfNxG_qIDmDMvSXn5JwBWdV-UTqOjluYoM_sn3daaZMJ6E9f9r_1kM3-uvA5v0tNaLjDnqUp-If9-OSypO4B2qhjN78QkgoZnVAo2-YCHuJMnlXXmffZyegLxToDzYsyz-gNr6HKNzd9U2jP2z3RO9F18RzBSiHxTYjKb25jyIedifmol4v01rWw8NHNBY-p4s1T4mLjiXWdFHb81RqIbH6iuRDjjlNrZjzSTtkMfuN8jrEBAcl_ifSISr8TNmSUSagiovRfUozIsGbQhRK20GBJerVhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما مهمان خبرگزاری فارس
شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/454966" target="_blank">📅 14:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
سخنگوی سپاه: بازگشایی تنگۀ هرمز منوط به پذیرش شروط ایران از سوی آمریکاست و ارتباطی به مذاکرات ایران و عمان ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/454965" target="_blank">📅 14:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lteziOLuAOV6lQbYjkFCADdYEHL86Gnl9wZNIimBtb70xTmj_ph2EuIMJ_M6pO5yh-jf8G-AM7bDSBosXJIcm25PEEreeGsVvOdniSxgzCTHyUsc1szylvJi8qBXd114LkySg_QSaJU9woQma6NbhJxOf5hJKRUI2LCroNfLjQcD-kR27d5lbGoA-hZjmS_1D3oqT72gkFIw2p75_tGysPe5fC-e2nfLL1sSTdNlxqbwbwPQhAWzdmYFYVe1n7VbMueekO_UfiMn-LmhWZmCLBw8ZTOyB4HyeMLSMKulBILwZCmAz05kFhd7CdJUPbabs24uZ0YxngTvx3Jn2Paqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه تختی هم مثل آزادی شخم خورد
🔹
با اعلام مدیرکل ورزش‌وجوانان استان تهران، ورزشگاه تختی به‌دلیل کاشت چمن تا حدود یک سال آینده آمادۀ میزبانی از مسابقات فوتبال نخواهد بود.
🔸
سال ۱۴۰۴ چند بازی استقلال و پرسپولیس در این ورزشگاه انجام شد که اعتراض کادر فنی…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/454964" target="_blank">📅 14:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a1c18c4c.mp4?token=rN_4y1hUJ6QdJLup2sLj3pSUjcvN36U0Wn9vs7fdza_o0qKzf8prkmgX3L5TBz8LHd9ggRZR6_O6Fbk2aoCm77KtXqtDJZ6g9njC0fO8hNRdI2x3nY5OlDuuTjZ2Ys3anstLyMUuArWaKUau0qZR0Gf53bexpIOhJIXhTeZyYaJGbxlk3X3nlGvLADbKY50CmZHRMkckw6bi_Eb1860RcoA1z_CFWwanYEeCrWqYTe7D_jcec3JiCq3DC1SrfGVSIfrZD36C66s2mnHsWQ1NchtleKJcVWv_YODr6gurPmC64suy2v-77nLkqGONNTcLs_QWdg8leQbVkTzRro9JhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a1c18c4c.mp4?token=rN_4y1hUJ6QdJLup2sLj3pSUjcvN36U0Wn9vs7fdza_o0qKzf8prkmgX3L5TBz8LHd9ggRZR6_O6Fbk2aoCm77KtXqtDJZ6g9njC0fO8hNRdI2x3nY5OlDuuTjZ2Ys3anstLyMUuArWaKUau0qZR0Gf53bexpIOhJIXhTeZyYaJGbxlk3X3nlGvLADbKY50CmZHRMkckw6bi_Eb1860RcoA1z_CFWwanYEeCrWqYTe7D_jcec3JiCq3DC1SrfGVSIfrZD36C66s2mnHsWQ1NchtleKJcVWv_YODr6gurPmC64suy2v-77nLkqGONNTcLs_QWdg8leQbVkTzRro9JhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454963" target="_blank">📅 14:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3atk1agjFni8O3YcZ3DraXVS7YZCEHLQDcmMPaqzEpkvsT5hn36cWUTu8yksx1kuHJHfM-i7hFx0Y6gMOdAcXYLmScVdJzfz9fDik8GaSiGXJsXEAsPQ70OxBp610dk_ylBEyu9IkIYeVcTs2JO5gxVMfwoDJtQMvMncjjeLNcFzIC4E1Mn6pDBMIpXBJvvaIc0fw2pbKfyVTl77_Asi4ZciQOOh4OuwSMZfkwXNTjxpG7MvgRYPGFcjHpu9r2sFmiNC5-xEOhperO52lrTZDhgZhTO1khyh1M6qdAqs1B5XNCPhLukk8lxRK8T6RnaqYGp2vSJE_TMy4eAGMU26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی درگذشت
.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454962" target="_blank">📅 14:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZo8tBPEk6Afb67OtMcf21CqPh7aRE6a7FPzX0i9KWsmG3ncRkOZ1zIdbtZ8MbaH4DYHF4OBtYVLU__nvXzUFs7RTGR1TCJuPv8QxisSw26T4KMj1RmjrFhk-z8yRN_zFbPTJLTHdKM4qaX7SVFJoEKyZDRgbQNwnyXc2kpRcQm4zYvcxCySiMjzBK9h_sPB-fhLwXOtcCDdbOSVRk8pkyOAo5cjjyOX9S5bgwFya973-MzI0ZHobuUm2i7VL53BUf1N4qGL5uSlR6uSHO2gUz92Rmj8pn4NeM8leVANJccKgbOvTmloXGbovB0vIugvDIUoVQq6v8SOesYp5idGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به کشتی اماراتی در تنگۀ هرمز
🔹
خبرگزاری امارات گزارش داد امروز یک کشتی متعلق به شرکت «ادنوک» هنگام عبور از تنگۀ هرمز با یک موشک هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454961" target="_blank">📅 14:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163c0107e.mp4?token=MZq-ohUxOX6Z-YsSP3g-DFUE86Y4RJASdGqIode_h_OmUdFtl8hm1dwNojSOfyxbFhGL_OZ9H5JFLreZAmpl8z9GUTwpg3OgM3gigQsv2sAJ0li5kecdjEV_tFx58VXO3XSiVd-TzCshCjKoDnLWEhPFVP3_Zil-zAnoMvxL32lFIFGosf08JAvAMj4WEUH6SrnFI0ayKESRL9dk8CgCjGo_hO28oRaVFeP3bg3E_Oao0quJMCJ04PS8Ahl3sc6GmqsxkwyDJhmTHqbXVl--bW8Zp97XHazQAIM-SLOe-DuT9QyvlTiqB_YkwWO7UYfA3U9NdxJhuZH9nk2dFSEnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163c0107e.mp4?token=MZq-ohUxOX6Z-YsSP3g-DFUE86Y4RJASdGqIode_h_OmUdFtl8hm1dwNojSOfyxbFhGL_OZ9H5JFLreZAmpl8z9GUTwpg3OgM3gigQsv2sAJ0li5kecdjEV_tFx58VXO3XSiVd-TzCshCjKoDnLWEhPFVP3_Zil-zAnoMvxL32lFIFGosf08JAvAMj4WEUH6SrnFI0ayKESRL9dk8CgCjGo_hO28oRaVFeP3bg3E_Oao0quJMCJ04PS8Ahl3sc6GmqsxkwyDJhmTHqbXVl--bW8Zp97XHazQAIM-SLOe-DuT9QyvlTiqB_YkwWO7UYfA3U9NdxJhuZH9nk2dFSEnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: بازگشایی تنگۀ هرمز منوط به پذیرش شروط ایران از سوی آمریکاست و ارتباطی به مذاکرات ایران و عمان ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454960" target="_blank">📅 13:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMDWA6UTe5novEH4omROL4jdGuDnpmo1-Mxfg0qT9LJ860Fmt8eGS7fQH3f4c1CZhHccS9kqUNARiYh_Eas4dOyOy_ha__OKwpC14X1ACB9XhgL3KZ1kdnHP9LzZwGmggF5IjvrgBIEfBZfaFjRJE1RFcYya0bOjCETvDPyu218iupq-WLFOHo75KEEYuj10LK8oOeNAjFFprVn6kMQ8ttMiAHZnD0PvoYp4rOXEbOkUAOu3HUVJkTkmV7tzkx6r-ZH760L9i0UTpfOXVeaU00gJ0NKhc2BN0997sflpRiZIs036xvblkR8xSjDwANSltHaOL-sqobtzK1GuxE5fkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قتل یک مداح پس از ۱۵ روز بی‌خبری از او
🔹
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شد. خانوادۀ او آن زمان در کربلا بودند و پس از بازگشت به کشور پیگیرش شدند.
🔹
مسئول هیئتی که رجب‌زاده در آن مداحی می‌کرد در گفت‌گو با فارس: ۲ روز پیش ویدیویی از پیکر آسیب‌دیدۀ حمیدرضا در شبکه‌های معاند و سلطنت‌طلب پخش شد.
🔹
جزئیات دقیق دربارۀ نحوۀ وقوع حادثه، زمان و محل جنایت و همچنین هویت عامل یا عاملان جنایت، نیازمند اعلام‌نظر مراجع انتظامی و قضایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454959" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1369d7fdb9.mp4?token=Vybu4qBMyIAzji8zJnFx__cH85ArWH8kGKRdK8IMWs1YoC_CENZDTQMNZ6ECrC-aasWueifbuafmMNVMc4iMWcmLJUXz29wzif2CV97Y-SuzzeDxcJpNRPS4BdLUfazKfD46VLj5136MIMepeDne3ehclClBugfwzyscmzKF3ef4D5ww0P7cR9hWqqjiPf4rSNfEGel5qYc8W2r9DwORm3T2szbQEF0yl-WChEpYUNXEtm8eoO6Dbyj9EXTPT05PGr_7KDH1ocyvJ1k78LUIyM5hBMeCt6kyh00YPrQtLP9RIVstzkJLTQeUHpgjNe2BpZ7_Hb8jzN_o-lfGmA_SlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1369d7fdb9.mp4?token=Vybu4qBMyIAzji8zJnFx__cH85ArWH8kGKRdK8IMWs1YoC_CENZDTQMNZ6ECrC-aasWueifbuafmMNVMc4iMWcmLJUXz29wzif2CV97Y-SuzzeDxcJpNRPS4BdLUfazKfD46VLj5136MIMepeDne3ehclClBugfwzyscmzKF3ef4D5ww0P7cR9hWqqjiPf4rSNfEGel5qYc8W2r9DwORm3T2szbQEF0yl-WChEpYUNXEtm8eoO6Dbyj9EXTPT05PGr_7KDH1ocyvJ1k78LUIyM5hBMeCt6kyh00YPrQtLP9RIVstzkJLTQeUHpgjNe2BpZ7_Hb8jzN_o-lfGmA_SlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلوغی مرزها بلای جان واردکنندگان شده است
🔹
با تمدید مهلت تعهدات بازرگانان تا پایان شهریور، بازرگانان فرصت دارند تا حدود یک ماه و نیم دیگر کالا وارد کنند و جریمه نشوند.
🔹
با این حال گزارش‌های رسیده از گمرک‌های مرزی با پاکستان از شلوغی و بسته‌شدن مسیرها ورودی و خروجی حکایت دارد.
🔹
بازرگانان می‌گویند با حجم بالای ورود کالا به مسیرهای جایگزین بنادر چنوبی از جمله مسیرهای زمینی و بنادر جنوب شرقی، ممکن است با این مهلت هم نتوانند کالایشان را ترخیص کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454958" target="_blank">📅 13:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8dD6ChNv48FAwjJ1RW4MmmU3nIlYzRWth-0_IDURmxDaQ7xnhy6RI_uoXh28_RidaFONOTiO45BTeW0z2iuLHqzM_X1kIYZayxTN73LNCn_qmG0QiADX_EtR5OeCJ_eC4VbmyHSQMsecnSCoCOgoiUN8bwQfkEijkBOnQ-yYX5AuhQ8fWMHJeonwbe7A2F_GEdBtWCaShuLsPZ_dG-r_WpmVtGixLOWBYqmj9CLJs0-SYBNiy7T-oiDxsbTRy0Pam-AxubwH8cs0ItDipUh4da4sBZtCje8cuL_DVM-kDRzNRjAHW1tiOaC0iEQYAbSqANt2kyBqqv-lkvgt2PHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری شد
🔹
با گذشت چهار ماه و چهار روز از برکناری وزیر دادگستری آمریکا توسط دونالد ترامپ، سنا سرانجام به جایگزین پیشنهادی رئیس‌جمهور رای داد.
🔹
مجلس سنای آمریکا سنا با ۵۰ رای مثبت و ۴۹ رای منفی، تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تائید کرد.
🔸
بلانش سابقه فعالیت به عنوان وکیل ترامپ و فعالیت در پرونده پرداخت حق‌السکوت ترامپ به بازیگر فیلم‌های مستهجن «استورمی دنیلز»، را دارد.
🔹
ترامپ در اوج کارزار انتخابات ۲۰۱۶ از طریق مایکل کوهن وزیر شخصی وقت خودش به دنیلز حق‌السکوت داد تا بر روابط نامشروع خود سرپوش بگذارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454957" target="_blank">📅 13:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB_uTB-CdNMpe3RRyF0mt__bDzXMEcTH-yt2RoXF1A3-Q1lBfsWEC--aVpbo3ZH8FbwsNd-hmny3LEve9iAvsPS6FLFLnUVfgt9kBZEU2XadPUVw9nqI4VfOSoZQUe9jCZPoXLt4etRLUHmzbg-6Y9p3knV1LGkoo4AmW5AZEZ4ulR5Wv6SLTzViPQP5DGju25h-3fcQ9jptZwHy4KychX_9_N38O9F0_WVQKLBBJ3Hif9clPKo91PnyW2C39bfWefMloTuG-ZWqXXFe5abNpvcTd_Cp_H7RvYGcvKs6dV7Dv1vGLj-XauQyBs9CImvLPy6pZc9IXwuXtv3sCDUFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454956" target="_blank">📅 12:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9CM5Y4clqKQO_FxnJMSQqIsrweUOe0gb4iLo8POJF3xMtD8JTZRQFW7uGyUlYQpwv74efMv0yy_tT2Tednc2DBg3e3wtjYHamIP2ZBFjFewIWpmpWi86AKYYgDCIKPdGimetQJpDGh5bh7iP9M_bivyTsSZctbCDWYhLnCAYSMAcghYKx97wb-60PObaYJyTi4HMERojwrHzQ8UHb86eEu7FQZZn0_JIj9K93mORQuNKNPPWy_ICgv2hOLhmc4vOSJar6cyxvRLb7r15nNvANxvFgN2uCIlMcoxqsNOITkWecG548OQLidU3yokYFuid2ookQUHA3qzh_ZgPpHWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454955" target="_blank">📅 12:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok2X2eHBnsIR8-9h-MEZwBFVmviPLey3IoBKXkBZEJyAlGXNRRVZDI2nCb1Fsr4sTgDDoLsqJBhMR2X76T2mfSy7yNQcWLgBzBSWD-KtP0uAm6Xo6WF66WFK-MSkza_NgmXUBsXqions3cqAToE11YBh2rMwtnfNjujdZYE1p0U1tmieneIucRDkRjoOZclWOt9maJMYAASbJpSiWQhpkpFlGU2E3liemDV1v9wePq1XvNRjRBcjYq1xFhj9wXU8DTAHRZ4EQTto4w3ibsMOZHQo7ntYNxOCHXGjnEkFXpCZm0dES02kiSTrD1p5GpdYhRcAfvxNVq9K1XwIlBQpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی، مشاور رهبر انقلاب: نیروهای خارجی باید منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454954" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ معنادار هوافضای سپاه به تهدیدات آمریکایی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454953" target="_blank">📅 11:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odBEYGn0tdmdCXqu1fb5ER5W16PMa47tIJ7q6JBj5O2ToiuzyaFxiw0htfSAOhg5-SuTcrFW3U2kkrxxgEy4pNqpAd02fZEpBMsJrCzv8XO4Inim8T4sIMuxOHNApwrTiCxRDGVq0sTtfEdF-oHXGVT8i5JhRaho_-Bik_ZAV5y4CFX2VSp_heV-z9gAQyo9TGxAklZImjBdtbihWNdkp3BdabgJ4KNSSU-JrDB4-1NwV_HBJPtL-R5e4ejB3AZF7EczSNQD53lUoJxNfDpCQdtN3KgwWRM8lXsyPiYK4-7qOfb0g5kYV62JrVfapjnkGspZp-YH-GIF5UzR25lZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱۵۴ هزار و ۴۵۱ تومان
🔹
یورو: ۱۷۸ هزار و ۵۴۲ تومان
🔹
درهم امارات: ۴۲ هزار و ۵۶ تومان
🔹
یوان چین: ۲۲,۸۸۹ تومان
🔹
روبل روسیه: ۱,۸۷۹ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454952" target="_blank">📅 11:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب: بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454951" target="_blank">📅 11:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxRWdzRLiLOofHrBzX0B42bYH8IyX08yVmbb2OZ19RoC3FCYOmAdls_OdDnMMihxy3Fx3-lJA0wY5_nIx6DxZVjorRCeQZQlBA0UvE7EVZp9uJkKsv-0f-fM1E64kZrkGW2Wniu9j3j99nBNsx_x8KvLJkQ8giunZY7OriEYVprcA4QjZiO-tprzWWGXxnvvjOmgz9NAYk8JrLMX0LfATkropAkla7xdwbWws05pH2E27nu8DeXW0lkZ5f7EmRm_boM2eyoBbU5p1EQ6rY3CvSQ5VAMgcHl4OaAeDtp1GW-l6pMuSE2ZY9WBMwEdNUVQQI58Gx2xq9Sv-y5lip-Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454950" target="_blank">📅 11:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454949" target="_blank">📅 11:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454948" target="_blank">📅 11:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHMQ4vGBGzxA9466pPB8g0f06Sh0gHDTH2a23jdaP9uVkG-JaBAcQQxtGti5SAGzJc0VUSB4c-29223cLEYyn2BKucKivGVPllgIMdVFhON_uTtG3FzCmdAK_3c-5Pz2gpMEFf1q9IX0Li24qztNn0dM0v_5Y4T2b6nlreV5HPK-n2na0iPbkjrs7z70dwD6wIOvj15lO2ZEhP-YlFdWUsxpVUZFIbpZJaBY2vG-9-qpzmN3c3myX8TI8qVzCcfNEONHaQZn8XgVuZDA9Tbi7AEj5xO8XTZ6pO2xz1-EVrTt9yql_f0upHpwWtv8oUx3W5yJplJlTfgCG-WYtw7Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیهٔ وزارت خارجه به‌مناسبت بیست‌وهشتمین سالروز جنایت حمله به کنسولگری ایران در مزار شریف و شهادت دیپلمات‌های ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454947" target="_blank">📅 11:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی و اعلام نظر نهایی دیوان عالی کشور، ساعدی‌نیا رسماً از فعالیت در حوزهٔ کافه‌داری محروم است.
@farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454946" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Rf8cBl4DlMoeXtrWuFiLfR8v-X0H-di2XBrgi0_ScWQCbKkG6elcrpmEfKAt03ehBoyeA59g_4DK6wdYkSm3cofdEiLp9MXQ8KPmRotcwYTX3I55DtJt4GJOyRzyd9xKlHwLub5vVff0JtRHy_t-O3OgPMiDROf3Hn8jzNgCchViipRen1WUGUToGjV473Z-Eag-HyVACr-2Iic_4I-Ff-kJ5AMGIeFTy69u1JcU3LMX_u6wuqcx9qMw9aiI2JhQvTaIPQkw48PtSQOayjDS4JUN2IdXaXRb7xHApBhlJvEp5u7ekCT_Lf2k47UWrOmoWGsjSEfWw31rC-fMR4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف لاشهٔ پلنگ در پناهگاه حیات‌وحش عباس‌آباد اصفهان
🔹
در جریان پایش میدانی و بازدید از آبشخورهای پناهگاه حیات‌وحش عباس‌آباد اصفهان، لاشهٔ یک پلنگ حدودا ۵ ساله توسط محیط‌بانان کشف شد.
🔹
این پلنگ که در حین تغذیه از شکار خود تلف شده است، جهت بررسی‌های تخصصی و تعیین علت دقیق مرگ به مرکز استان منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454945" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: درپی انجام انفجار‌های کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454944" target="_blank">📅 10:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNdI6_06ZmqJTOeSXfzeR-Ox9O2og1VJj5PvI7PmB8RfRsmZJLEz3bUILPJupl7h-3pHA9m_dHrUe8TCalMAn4rb3kVbRQsK8Xv8QT5XmKWBTAXUIgUdmJvyIcxOXk0xNZruMQGRgRTVyyRq5WyAXDUWJxfKCaO2YapJFyfP1fLj4n-DXcHD42xXPC4vK5XYM0y4HC636DcphgsUdwQqzrBWZeniXfRJZMr2Iwf7dd5NJA_OIOV7a20W4oq3Cyg5MoiY5SWPi0n67h8tZYI4xcte9MNrPFJZ1RG4JlJ0H7nEmyQOkTufYTmT3KKfC4a96bO90fmKhYe7f5flcdLrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی یک کشتی دیگر در تنگهٔ هرمز
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که یک کشتی که احتمالا نفتکش است در مسیر جنوبی تنگهٔ هرمز دچار آتش‌سوزی شده است.
🔸
بامداد امروز یک آتش‌سوزی در کریدور جنوبی تنگهٔ هرمز اتفاق افتاد و یک شناور مقابله با آلودگی نفتی و اطفای حریق به‌نام «ادنوک ای‌آر۰۱» خود را به منطقهٔ حادثه رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454943" target="_blank">📅 10:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUmTCs9-mA5p6qCHSrc7iCbZgh8TSUp58xCB3gL0WDSI_ATYCTM8vyFNGUacl6AoG23RRcY1H5XifRP267tYeNDxT7ZLl0HtGouZYlHkzldLD-3zy8dy27_7mlpXTq5BPgK6VdrzbrTsgl-OnZRhiTrRKcq-sJR-jaf6tVibOiCVFyf88CPtEbxTkLosiqWzeGX6Sv0E1w-1sYiEDeemNRd1HkVumpPRLu0IZ0GxtUR_6TyXkoOa6d3Hib0lkao5XJdN0OhEmF4hlSrB2h7_SrzfT1sk8pERK8EM-XtdpxFERmYjPPvvF1L4cIxY2Dbltbz1wFS7BExd0RQstA1fig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاچهٔ ارومیه جان گرفت
🔹
شرکت آب منطقه‌ای آذربایجان‌شرقی: حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است.
🔹
استمرار این روند امیدبخش، نیازمند تداوم مدیریت علمی و رعایت دقیق الگوی مصرف است تا پایداریِ ایجادشده در تراز آبی دریاچهٔ ارومیه حفظ و تقویت شود.
عکس: عادل باخدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454942" target="_blank">📅 10:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCY8Tr09X168pnG5G9kcfcry1Kr6DYUYgnJ7NPIxJKoiDXgvu3oX-r7ii4srYp5AjUgHJKLu3Nj9oOtN0shGfE5uZAp-Zoykw2NeXTml316bYGeXtAPsgLkm4_9OdfcC99m-Vwd9KmgwB2-VF1EjnMOLH7SqFCqb_lfUPy6ldYCzBO7yVnPWb6NaU_WxUbVTHV-6-UBF0TF__EndqWNTpqmpEVQfwjuopz9cMkR95xy4nFz2Tap7NTha-wIvTEbez2janZ1j2-h5l-Dgzb7wvfNpsTiPBOURJbdMRnoM6g5jN6qtdT4xlyJA_Djxy4LhU7OfS__XEjIvpGlHK31jXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو برای کمک آمد
🔹
رئیس فیفا که با طناب ترامپ به چاه افتاده حالا به دنبال خروج از این چاه با کمک عامل این بحران است.
🔹
نشریۀ تلگراف نوشت: ترامپ وارد میدان شده و می‌خواهد هر چه در توان دارد برای حفظ اینفانتینو در سمت ریاست فیفا بگذارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454941" target="_blank">📅 10:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش: خبرنگاران فرماندهان نبرد رسانه‌ای با دشمن هستند
🔹
ارتش جمهوری اسلامی ایران به‌مناسبت روز خبرنگار: خبرنگاران، فرماندهان خط مقدم نبرد رسانه‌ای با دشمن به شمار می‌روند.
🔹
فرماندهانی که با ابزار قلم، تصویر و روایت، در برابر هجمه‌های سازمان‌یافتهٔ دشمنان ایستادگی می‌کنند.
🔹
خبرنگاران با روشنگری مستمر، ملت‌ها را در مسیر تشخیص حق از باطل یاری داده و زمینه‌ساز تقویت بصیرت عمومی در برابر موج‌های فریب و عملیات‌های شناختی می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454940" target="_blank">📅 10:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454939">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEJHZetUcFI_7W_j92L_BS8PNGcxOx28Rof1OFLpy3ULZVBtn5yvW8DxosCxLKdWADtEnju0MFzzAhQoIqTtjktWeYGCJclZzpXCiBQbiFOCN4Ddj6nSh6HfaqHVcGcvA6_NSDW94RYzRRvPEcHT2C1lI2MT5bi8SlGufr7nepzQiO3f8TqR7zjrVNN2o811K6sWc82so28kEMjJfP3iBBBuYdS7nz4sAELyAoI7Ri7URuL8ChifC1sEcdDCYr6HRj7b28YJLW8L1ZfAoQBBZJopf1LHJz7MLO_g4ACwWYGRuD1QmT66x7c3U7Ncurc7fpILmMHinXYlYPmR797vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454939" target="_blank">📅 09:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ایام عزاداری دههٔ آخر ماه صفر در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454938" target="_blank">📅 09:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای سرافراز خبرنگار؛ نماد تعهد و دلدادگی اصحاب رسانه به کیان انقلاب و ایران اسلامی و آرمان‌های والا و تمدن ساز آن است.
🔹
امروز، منطقه و جهان، شاهد یکی از پیچیده ترین و سرنوشت‌سازترین نبردهای تاریخی معاصر است. آمریکا و رژیم صهیونیستی در جنگ‌های دوم و سوم علیه ایران اسلامی، علی‌رغم تمام تلاش‌ها و اقدامات نظامی و عملیات رسانه‌ای، نه تنها به اهداف اعلامی و شوم ترسیم شده توسط رئیس‌جمهور پلید و متوهم آمریکا دست‌نیافته، بلکه ابعاد تازه‌ای از بن‌بست راهبردی، شکاف در صفوف متحدان غربی و هویدا شدن افول هیمنۀ آنان به تصویر کشیده شده است.
🔹
رسانه‌های جهان، با اذعان به ناکامی واشنگتن در غلبه بر جمهوری اسلامی، به وضوح از «شکست» و «تله خودساخته» ترامپ در جنگ علیه ایران سخن می‌گویند و حتی اعتراف می‌کنند که تفاهم‌نامه‌های حاصله، چیزی جز «سند تسلیم آمریکا» در برابر واقعیت‌های میدانی و قدرت مذاکراتی ایران نبوده است.
🔹
این اعترافات، بیانگر درخشش مولفه‌های اقتدار نظامی و بازدارندگی فعال کشور است؛ مولفه‌هایی که مرهون هوشمندی راهبردی، ایستادگی ملت و پشتیبانی همه‌جانبه از نیروهای مسلح، به‌ویژه سپاه پاسداران انقلاب اسلامی و نیز مجاهدت هوشمندانه و دقیق رسانه‌های انقلابی در مقابله با دروغ پراکنی‌ها و بزرگ‌نمایی‌های خصمانه دشمنان است.
🔹
در این میدان پرچالش و معنادار، دشمن با بهره‌گیری از تمامی ظرفیت‌های جنگ ترکیبی و سایبری از جمله هوش مصنوعی، در پی تحریف حقایق بوده تا میان ملت و نظام ایران فاصله بیندازد و سرمایه عظیم اجتماعی و وحدت مقدس ملی را نشانه بگیرد.
🔹
تجربۀ اغتشاشات به‌ویژه در کودتای ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ به ما آموخت که ضلع رسانه‌ای فتنه، پیچیده‌ترین و حیاتی‌ترین بخش این معادله است؛ جایی که «روایت اول» از آنِ کسی خواهد بود که سریع‌تر، دقیق‌تر و هوشمندانه‌تر وارد میدان شود.
🔹
این تجرب‌ تلخ فرصتی شد تا خبرنگاران فهیم و انقلابی و رسانه‌های متعهد و زمان شناس، در جنگ تحمیلی اخیر، با تمرکز بر روایت‌سازی صحیح و بهنگام، با عملیات روانی و آفند رسانه‌ای علیه دشمن، تصاویر ماندگاری از صلابت رزمندگان، گزارش‌های صادقانه از حضور و مقاومت مردم، روایت مظلومیت شهدا و خانواده‌های آنان و بازتاب همبستگی کم‌نظیر ملت ایران، را  تولید و انتشار دهند که بخشی جدایی‌ناپذیر از تاریخ پرافتخار این برهه حساس و ارزشمند محسوب می شود.
🔹
خبرنگارانی که در جنگ تحمیلی دوم و سوم زیر آتش و در معرض تهدید، لحظه‌ای از انجام مسئولیت خود عقب ننشستند؛ آنان که در کنار نیروهای امدادی، مدافعان امنیت و مردم مقاوم حضور یافتند و حتی برخی از ایشان جان خود را در راه اطلاع‌رسانی و دفاع از حقیقت فدا کردند، شایسته بالاترین مراتب تکریم و قدردانی‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454937" target="_blank">📅 08:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWpzp0cF3XfmH5fC0GqsdWivoO6yLlUlZrqgVAM4qmpcv9Hl8mE5dNEp-B6CNyoSHHfbr4x2WGLUn9j1UqhoUCz4pFJhTxV9IiDHjLPgqWmu_ZDYNkvPNYpJ1OMCyvGX4YRvK3TwvKaGcEbW88FMAwsPAqxcAeoA8GjRoI2jTw3PNKsqoa-Y5GlorMDvUbE7Nwmd1Xw8H3F4tSF5f21X1dEIKsPlyiS8pfcf2zB_-RLU_g-erU5ApdTAYoqHeUxg-IzVgm6sXN4y7jVZ69t1s0pghla2X_oHaI4SUMqYHWztfdwszPEAV4m3zv-74haVhf1VrbclxCMkKEg9YRXyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: خبرنگار متعهد، هم‌سنگر رزمندگان پشت لانچر است
🔹
رئیس قوه‌قضائیه در پیامی به‌مناسبت روز خبرنگار نوشت: خبرنگاران متعهد کشور در دشوارترین روزهای یک‌سال گذشته، با شجاعت و مسئولیت‌پذیری از مرزهای آگاهی عمومی و انسجام ملی پاسداری و در میدان جنگ شناختی، با خط تحریف، سیاه‌نمایی و تفرقه‌افکنی دشمن مقابله کردند.
🔹
در مقطعی که تمام دنیای کفر و استکبار، جنگی موجودیتی به ایران عزیز ما تحمیل کرده‌، عظمت کاری خبرنگاری بیش از پیش درک می‌شود.
🔹
خبرنگاری که سعی می‌کند خبرش درست و دقیق و سریع باشد و در عین حال التهاب و تشنج اجتماعی خلق نکند و امنیت روانی مردم را تثبیت کند، حقیقتاً هم‌سنگر همان رزمندگان پشت لانچر است که از تمامیت ارضی و عزت و اقتدار ایران عزیز دفاع و صیانت می‌کنند.
🔹
خبرنگار متعهد، دیده‌بان تیزبین میدان جنگ روایت‌هاست؛ او که با کلامی سدید و قلمی بصیر، خاکریزهای ذهن جامعه را در برابر تهاجم ترکیبی دشمنان استقلال و اقتدار ایران، مستحکم می‌سازد و اجازه نمی‌دهد که غبار تردید، سیمای درخشان حقانیت ایران اسلامی را مخدوش کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454936" target="_blank">📅 08:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزارت دفاع: ایران در میدان دفاع مقتدر خواهد ماند
🔹
وزارت دفاع و پشتیبانی نیروهای مسلح به‌مناسبت روز خبرنگار: در شرایط جنگ ترکیبی و عملیات روانی دشمن، روایت صادقانه حقیقت، مطالبه‌گری مسئولانه و صیانت از افکار عمومی، بخشی از قدرت ملی و بازدارندگی جمهوری اسلامی ایران است.
🔹
خبرنگاران، یاوران و همراهان راهبردی در شکل‌گیری گفتمان دفاع همه‌جانبه و انقلاب صنعتی دفاعی جمهوری اسلامی ایران هستند.
🔹
جمهوری اسلامی ایران، در میدان دفاع، در میدان روایت و در میدان اراده، همچنان مقتدر، هوشمند و آماده خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454935" target="_blank">📅 08:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRxuH2Hw1H61mgb98W7XdJUPE-r7I2etsrdC3ZJ8GFXNRUvjxrYFf4tc3vNLy6hJZDMmi-l1y43i1EX9Ee9c-CTEBQyduQB0GPtkSlITj01ENJMglHX5nII7ATGt9AKa91Zxr1f0mEk80wXxcYRezjhGXZxjkC3QbB86b9NwkQHzIA92yGredJENa3qqfQLKw-_Rz1slKXohyUYvvQlhbIPcV_K_Kf5_g95sGk4NKMdvV-_FWdjSpUHzlnr2xxUCyoR7APe4LHKPnBKPfMkN48mclwJJD6u7Q3PA93kh9oigsSkFIjZNqRPE5-Q1G-fMnX8iMKpqlIYKCbkmuL1ChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: خبرنگاران رزمندگانی هستند که سنگرشان آگاهی و سلاح‌شان حقیقت است
🔹
پیام رئیس‌مجلس به‌مناسبت ۱۷ مرداد: سرنوشت ملت‌ها علاوه‌بر آنکه در میدان آتش رقم بخورد، در میدان روایت تعیین می‌شود و میدان‌های نبرد تنها بر خاک و دریا و آسمان شکل نمی‌گیرند.
🔹
صهیونیسم و استکبار جهانی تنها شهرها را بمباران نمی‌کنند، آن‌ها حقیقت را هدف قرار داده و اعتماد ملت‌ها را نشانه گرفته‌اند و اگر روزی با گلوله به جنگ تمدن‌ها می‌رفتند، اکنون با خبر، تصویر، شایعه و تحریف به میدان آمده‌اند.
🔹
در چنین جهانی، خبرنگاران تنها مخابره‌کنندۀ اخبار نیستند؛ رزمندگانی هستند که سنگرشان آگاهی، سلاح‌شان حقیقت و مأموریت‌شان دفاع از امنیت روانی، هویت ملی و اقتدار فرهنگی یک ملت است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454934" target="_blank">📅 08:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یمن نفت عربستان را زمین زد
🔹
کپلر گزارش داد، صادرات نفت عربستان پس از اعلام محاصرۀ یمن از بیش از ۴ میلیون بشکه در روز، به کمتر از یک میلیون بشکه کاهش‌یافته است.
🔹
تنها راه باز صادرات نفت عربستان اکنون کانال سوئز است که سابقۀ بسته شدن دارد.
🔹
همچنین پیش‌تر اعلام شده بود که برای اولین‌بار در ۴۰ سال گذشته صادرات نفت عربستان به آمریکا صفر شده است.
🔹
طبق داده‌های کپلر پس از اعلام رسمی‌ محاصره از مسیر باب‌المندب، میزان بارگیری نفت در ینبع به‌عنوان خط دورزن تنگۀ هرمز صفر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454933" target="_blank">📅 07:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2nxUjCbbIfYs8djqzhiJnw9hrxkK9w3_1AqkIhiECQtwmpMDSDbGgtAy5t8EtruIgKor00XoFJU3rj-dLr4Macla9jOXdVnVu2gMZPHwuF-jjKcnp7XBuKzMvkTKRc582_0LedcuuMuvcL-UBjywcCUtyYExpOgt0-PSJ8UU7M7xzEnouFBsWPV02d2IDvdcN9KXZhq5lyo1b4YrZvLtUDPSj84SvBAeoSzpEKoJJmUdrPDNfmhQTv8l0_tc1mFzbNAHR9y9ns13dV1o4R6w7JhHBgUveaay0TgAg04WeLFjE7q-SJsup9j95yu73K_sXyPi5OpZ83AgPYmWDxg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه سیزران روسیه
🔹
پالایشگاه سیزران روسیه ساعتی پیش هدف حملۀ پهپادی اوکراین قرار گرفت.
🔹
پیشتر فایننشیال تایمز گزارش داده بود که نیمی از زیرساخت پالایشی روسیه به دلیل حملات اوکراین متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454932" target="_blank">📅 07:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW1jmVZUini9eiC8yNM_6v2tjQ6fuHeTH9ffi9AjDCDnrcVZpxlHhV7tywcsetzpfn-bOlnY1CXhTyYmcXS2eOTXz82T-kKOt__e_-ZmQd1VJjRiGq5LoliPU11I39DlxvHgY1Y_ksuXQFIBEHQLprQ-6HUquqES5jIG-0sTw_xGkKvrsaQzwiUEXHTcYDWCQyNPowF9x4i2pvRtenpGZSNOEzOzniErf3ihhkxYW-isVLL7CQNveaMOKcEBrmVTyB3riakxdaB_vBN0wzFE2Z8b5YrX7nD6P3s321WsgrZZndbtGh2ohWCYZ7V26NEdDVpoU0YbJ4eZdKmS-cWdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار هواپیماها از فرودگاه جده عربستان
🔹
دقایقی پیش، هواپیماهای مسافربری به مقصد جده حاضر به فرود در این فرودگاه نشدند و از فضای هوایی جده گریختند.
🔸
تعدادی از منابع غیررسمی از حملۀ ساعاتی قبل یمن به عربستان خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454931" target="_blank">📅 07:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ab2e54ea.mp4?token=b5KnJ9YFySlfeBVBhiTj-QRs88DjXLwVbdy-gFvm0lef-lYpz_lZK-MVEI3pgaPi05fHOkdshTgmKC1eJ8iS5tUNc55Bgny-WeJPbY7xl1hSHVMkjqgqiO-8wC3VlIpHjdKZ65L93_tVM2abu22JSOEg8wLnT5uYftq-rhtGXEo3WmBu9IcypB_aXNfD2q1ITAueJmlmIs4P5Se7kqQILAEd1UGpK8pcBsGwrd7jXKIOH4ZZeX0mwOM-1BaVpJXer3pdoe5hkA0SCvUt41dfAWWaBJsDiSDWmQd2tVjz2eCDfDOaQ9mY2iTzBX3WKgTPCMm_A0-5IjaALsAEmTMZtymy3aK8n7OTXtrf5SFqZePE05GcBcdEN-SMSnaMdE2Kchm3DlNIFlyXQ8TJ5-Rek0LmwUVa350hOqUOwpoSIyMIhLf2LkbIR1yVjdvXSwORm5Q0TsT0Z8nuJO4PSSKJM5Fu-bi-rfDJfn2QImvuyFCnjf4gMj5NDrem5etZAw91HAWgA1Y5e8wBbmwxzkh9YE7sdgqzjQ8PCdTepGtjH2oduZR7e9wvUNkAVUEQ6OBs1oR_43cD7AbgFUZaHNGIDQuqmkGo8GPlhNd_FAKL1PFN49jU6wsGhKhY6j11HYPQ5fUArXp6MktcTg3RV_ZerPfzzLj_XmUGBMG_fwF44yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ab2e54ea.mp4?token=b5KnJ9YFySlfeBVBhiTj-QRs88DjXLwVbdy-gFvm0lef-lYpz_lZK-MVEI3pgaPi05fHOkdshTgmKC1eJ8iS5tUNc55Bgny-WeJPbY7xl1hSHVMkjqgqiO-8wC3VlIpHjdKZ65L93_tVM2abu22JSOEg8wLnT5uYftq-rhtGXEo3WmBu9IcypB_aXNfD2q1ITAueJmlmIs4P5Se7kqQILAEd1UGpK8pcBsGwrd7jXKIOH4ZZeX0mwOM-1BaVpJXer3pdoe5hkA0SCvUt41dfAWWaBJsDiSDWmQd2tVjz2eCDfDOaQ9mY2iTzBX3WKgTPCMm_A0-5IjaALsAEmTMZtymy3aK8n7OTXtrf5SFqZePE05GcBcdEN-SMSnaMdE2Kchm3DlNIFlyXQ8TJ5-Rek0LmwUVa350hOqUOwpoSIyMIhLf2LkbIR1yVjdvXSwORm5Q0TsT0Z8nuJO4PSSKJM5Fu-bi-rfDJfn2QImvuyFCnjf4gMj5NDrem5etZAw91HAWgA1Y5e8wBbmwxzkh9YE7sdgqzjQ8PCdTepGtjH2oduZR7e9wvUNkAVUEQ6OBs1oR_43cD7AbgFUZaHNGIDQuqmkGo8GPlhNd_FAKL1PFN49jU6wsGhKhY6j11HYPQ5fUArXp6MktcTg3RV_ZerPfzzLj_XmUGBMG_fwF44yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوری زندگی نکن که واقعیت را نبینی
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454930" target="_blank">📅 05:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyKey8xHAgqKk-Nr830mFBBQtFlb_3Wg6s5tPnHeKNkLI1EO5af3qQIAJ01zAIWcgNlkNb3DI1J8qul6D4Rqi14W-hagMGUCoUgXigX65r_4Bzpglr7kCYVnYhAzV-JwwcyFMPgXQv2m0-SP6i2c2XIBG7zWggSbXpjwa8jIqLdd0XS9OSyffjuUK2_aeMis_l72wH23iJteawzgjw6jLu3ndO_gHfcg344VIgWw7nFnaGidsC2pYnZ2hzF5DRUvyQtkMzLcRNUnJx6jbw1pLGloOvBv3ldZwoLM1XYDJJEP7NNYo72-kF4PXrrEplaeKtxcna2SScgO7SKMb9NlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۴.۶ ریشتری در گلباف کرمان
🔹
ساعت ۰۳:۰۷ بامداد، زمین‌لرزه‌ای به بزرگی ۴.۶ ریشتر حوالی شهر گلباف در استان کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454929" target="_blank">📅 04:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buxAqFtt9KZehIYthIa_PSnXb-jT0GUIjbnncUKemI6ZDBMdsvOfVslXaGltUr4WIaBJg_kSq47jb4CXrCMekEXEyX6G12b4wF8U3SF21TDunvpD4PiVWNFkL0JZZUDWcuu62ND69LyF5zhWY0rVv6s3qYisY0NpdNROoDXacE4bAW4iDz4yiGx9x2RnbkrAl2EjTdAP6UONxuYv1kQEVtz5V_sy7Va0F4d47EZLLY8l8Jz6KgRuw_WuZMMbZgOC0QAmai2eROe8qvozCsSiQcpmO3e-1Ox4tU6T5SxarmBBOt-w8ll78U05GTZaLRFrZz1PxYDU7LUZAgeeaQRE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ارشدترین ژنرال آمریکا درباره محدودیت‌های نظامی علیه ایران
🔹
شبکه سی‌ان‌ان به نقل از سه منبع آگاه گزارش داد «دان کین» رئیس ستاد مشترک ارتش آمریکا طی چند هفته گذشته در گفتگوهای خصوصی با دیگر مشاوران ارشد ترامپ صراحتاً تاکید کرده است که ایالات متحده باید «راه خروجی» از جنگ با ایران پیدا کند.
🔹
به گزارش سی‌ان‌ان او گفته گزینه‌های نظامی موجود برای تشدید منازعه می‌تواند نتیجه معکوس داشته باشد و صرفِ اتکا به نیروی هوایی نیز بعید است اهداف اعلام‌شده دونالد ترامپ را محقق سازد.
🔹
کمرنگ شدن چشم‌انداز پیروزی نظامی باعث شده کین در این دیدگاه تنها نباشد.
🔹
دو منبع آگاه تایید کرده‌اند که او نگران گزینه‌های نظامی روی میز برای تشدید درگیری است و موضوع یافتن راه خروج را با سایر اعضای کلیدی کابینه از جمله جان راتکلیف (رئیس سیا)، مارکو روبیو (وزیر امور خارجه) و جی‌دی ونس (معاون رئیس‌جمهور) در میان گذاشته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454928" target="_blank">📅 04:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ادامۀ تجاوزگری‌های رژیم صهیونیستی در جنوب لبنان
🔹
المیادین: توپخانۀ ارتش اشغالگر صهیونیستی منطقۀ علی الطاهر را هدف حملات خود قرار داد.
🔹
همچنین ارتش اشغالگر اسرائیل اقدام به یک عملیات انفجاری در شهرک «میس الجبل» نیز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/454927" target="_blank">📅 02:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb10961f.mp4?token=N9sGcyhh_vAjchSkCyoA0NGpR3pFk1Xrm17Di00L-8_dMs64Fg3EyaeYz5lApL6vj0hHKV6z2u6apkHO-ZLdFLkVgG8MfEHRYYbjbrgrdpz-m8qNbfFTdwx1HwadD85ExVSVHUlSjnwpp18A5b5KP8tGkOKC_gnTh1-yDI8ExnnoEJr8kFA3UmTegtw4fcWZ9OBEFcrFw_3rrKRNDMNAzGJ38e3IJpxUhpn9ZQdQuwc2hVHljWrRPa1novXnfN5PfC2gIRZr0bPpNXwn2rFMQAdLUiPZjkMS-gRUJuUiqObglZ_9ANLl6ueOr4AifM7NewItLa82-LLHmxEGCHkCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb10961f.mp4?token=N9sGcyhh_vAjchSkCyoA0NGpR3pFk1Xrm17Di00L-8_dMs64Fg3EyaeYz5lApL6vj0hHKV6z2u6apkHO-ZLdFLkVgG8MfEHRYYbjbrgrdpz-m8qNbfFTdwx1HwadD85ExVSVHUlSjnwpp18A5b5KP8tGkOKC_gnTh1-yDI8ExnnoEJr8kFA3UmTegtw4fcWZ9OBEFcrFw_3rrKRNDMNAzGJ38e3IJpxUhpn9ZQdQuwc2hVHljWrRPa1novXnfN5PfC2gIRZr0bPpNXwn2rFMQAdLUiPZjkMS-gRUJuUiqObglZ_9ANLl6ueOr4AifM7NewItLa82-LLHmxEGCHkCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرس‌های قهوه‌ای دوباره در اشترانکوه آفتابی شدند
🔹
تصاویر تازه‌ای که محیط‌بانان اشترانکوه هنگام گشت‌های حفاظتی ثبت کرده‌اند، دو قلاده خرس قهوه‌ای را در کنار تعدادی کل و بز وحشی نشان می‌دهد.
🔹
خرس قهوه‌ای در رأس زنجیرۀ غذایی بسیاری از زیستگاه‌های کوهستانی ایران قرار دارد. حضور این گونه معمولاً به معنای آن است که چرخۀ طبیعی منطقه هنوز از هم نپاشیده است. زیرا خرس برای ادامۀ زندگی به زیستگاهی امن، منابع غذایی متنوع و کمترین میزان مزاحمت انسانی نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/454926" target="_blank">📅 02:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca78e40b2.mp4?token=qpjHDN5altoc0bT5XfgTfhSUAmtpcwXW-XZhpuEgyEJJhNmUqJ4D-Tg0jrgT9X7_0xPapW5c039G_OWrgR7kJQ_q9oujsK9CVUj2XEmqHCsb6SwPVdNdbJmmp0LVgLKRJoitEHeRIEDCBcWCbfDXYwDbtWLTwuaji5mninelJ4YZFGyydyV_1aJYxMPlRtlVbbOJR-MJuYY9-ErQcLoOSZYHDP7ZqfHbcZCXUqY20avS4nRiG9tdiouhMz5zN01jXJnKGp7p2p7mBKopBELuJtgfbSstPHBmmr5SwAGjdfdmOP8eghVDl8gIWTWHOQFQ3F8xEdBvAO-yoKhr4kyVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca78e40b2.mp4?token=qpjHDN5altoc0bT5XfgTfhSUAmtpcwXW-XZhpuEgyEJJhNmUqJ4D-Tg0jrgT9X7_0xPapW5c039G_OWrgR7kJQ_q9oujsK9CVUj2XEmqHCsb6SwPVdNdbJmmp0LVgLKRJoitEHeRIEDCBcWCbfDXYwDbtWLTwuaji5mninelJ4YZFGyydyV_1aJYxMPlRtlVbbOJR-MJuYY9-ErQcLoOSZYHDP7ZqfHbcZCXUqY20avS4nRiG9tdiouhMz5zN01jXJnKGp7p2p7mBKopBELuJtgfbSstPHBmmr5SwAGjdfdmOP8eghVDl8gIWTWHOQFQ3F8xEdBvAO-yoKhr4kyVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی سلحشور مداح و رزمندۀ دفاع‌مقدس با حضور در میان رزمندگان مدافع خلیج‌فارس، از خط مقدم تنگۀ هرمز می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/454925" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=oWD5e1nzwFlOi0ytRiJbySwvMBbkW7an64oD5Oz4nzAa7Qwg7KXj4VquLxil4izedg76fFCd-KRzROIq3-n7Gz4U3BYD0YQt_GZNGHK8jd-Fsl8f_koBY76jGkDj-fnK8yMiK0hPhA0Qq86n5odOwi1Cv2gKi_cDlgr67cShKV-mamw3MmekVDTU7oNfllMQ0NltRaxQ5gyxN4zVaUZywZ0G6sWibipgD8RCIRofPa-UAikx_tlgHeUmRk0FRnlAEHu6IlcHbtXG0O4J_Kvm7kYevalVWU3du8U1z7vXL1Hz6LIrXix_HFGzZv_5CeznGd9-PgBHH1Qi_p5IU18kMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=oWD5e1nzwFlOi0ytRiJbySwvMBbkW7an64oD5Oz4nzAa7Qwg7KXj4VquLxil4izedg76fFCd-KRzROIq3-n7Gz4U3BYD0YQt_GZNGHK8jd-Fsl8f_koBY76jGkDj-fnK8yMiK0hPhA0Qq86n5odOwi1Cv2gKi_cDlgr67cShKV-mamw3MmekVDTU7oNfllMQ0NltRaxQ5gyxN4zVaUZywZ0G6sWibipgD8RCIRofPa-UAikx_tlgHeUmRk0FRnlAEHu6IlcHbtXG0O4J_Kvm7kYevalVWU3du8U1z7vXL1Hz6LIrXix_HFGzZv_5CeznGd9-PgBHH1Qi_p5IU18kMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانسورچی‌ها ناتوان از پنهان‌کردن ضربات کوبندهٔ ایران بر ارتش آمریکا
🔹
وقتی قدرت نظامی ایران و ضربات کوبندهٔ رزمندگان جان‌برکف ارتش و سپاه بر پیکرهٔ ارتش آمریکا آنقدر خسارت‌بار است که با وجود سانسورهای گسترده هم نمی‌شود پنهانش کرد. ‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/454924" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
مردم فسا امشب هم برای ایران به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/454923" target="_blank">📅 00:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCm29aTZZIDLxjoPs01PPuhiCiW0U6fBhLRSY7oEy6Di2pj9i1vm9meWh4XDC2iVFlWw2trapqkZCUU6NSpU79t_U0qMXnV_EPezET3TMOM0UOfcAjNvBELX7n9fxBjomYQLXPd_UkDEUmJ6dXjyxS-VVV_TdgmAKv_m4OIBgaJ1iv0dwoNjNO7XFkLz_PbirtwZH4RvSO9yFwM3qNhGLJAThMyYr_twtJ-CXSA4G5RsI53mPYBBLjZ7u-BDAPn6xCd_XHz8mVDl9r7J2dLnpl0exozK8dlUFQ4ciRgb9tk_vvuI8GrnBpXFveYL2TMXuxNbWXOn2wZZj4D9cS_Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب‌وکتاب اشتباه
🔹
امام صادق(ع) متوجه شدند مردی در میان مردم به تقوا و نیکوکاری بسیار شهرت یافته است. ایشان برای بررسی موضوع، به‌صورت ناشناس و به‌دور از چشم مردم او را زیر نظر گرفتند.
🔹
مرد وارد مغازه‌ای شد و در فرصتی مناسب، دو عدد نان دزدید. سپس وارد مغازه دیگری شد و دو عدد انار هم دزدید. امام به دنبال او رفتند تا ببینند با این مال حرام چه می‌کند. مرد به راه خود ادامه داد تا به فقیری رسید و هر دو نان و دو انار را به او بخشید.
🔹
امام صادق (ع) جلو رفتند و از او درباره این رفتار عجیب پرسیدند. مرد که امام را نمی‌شناخت گفت: «ظاهراً قرآن نخوانده‌ای! خداوند می‌فرماید هر کار نیک ده برابر ثواب دارد و هر گناه فقط یک عِقاب، من ۴ تا دزدی کردم که می‌شود ۴ گناه، اما آن‌ها را صدقه دادم که ۴۰ ثواب دارد. ۴ گناه را از ۴۰ ثواب کم کنیم، ۳۶ ثواب برای من باقی می‌ماند!»
🔹
امام صادق(ع) در پاسخ فرمودند: «تو قرآن را بد تفسیر کرده‌ای. خداوند می‌فرماید: «إِنَّما يَتَقَبَّلُ اللَّهُ مِنَ الْمُتَّقينَ» (خداوند فقط عمل پرهیزکاران را می‌پذیرد).
🔹
تو با دزدی ۴ گناه مرتکب شدی و چون مال حرام را به دیگران دادی، بدون اذن صاحبش تصرف کردی و ۴ گناه دیگر هم اضافه کردی؛ پس ۸ گناه مرتکب شدی بدون آنکه هیچ ثوابی برده باشی.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/454922" target="_blank">📅 00:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c14ff6ba.mp4?token=aD5_uspBAV7ofz90d1nqBepUeftVAiiO7cfX9TDLzDva3t2Zze63xQDT5p_j1TCoT8SzzAlSkdr8FbaaiBsqmNguDBYgVe1l9cr02Z9mltFCjN4kTRCf9YfTsX9Or2EGtoPNTiTVN4mAyk_xzphR_tl8o4mSas4kO-K53OKj3fO3NOduPNMUiFoSWgTbByZ-hyZ8dOkIp43PaACmpWLOjP9T-FKOsk4EIREdTT9HGwXXVrdRRS94YzHzVve96fMJ-BZFQc_IePAGmnhjTE2U-OX952tPic64qhxwrFiWVKVW4CDnESvKLcCvmojk1V1YBfbyRl7W-iOUE1LY8_XcnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c14ff6ba.mp4?token=aD5_uspBAV7ofz90d1nqBepUeftVAiiO7cfX9TDLzDva3t2Zze63xQDT5p_j1TCoT8SzzAlSkdr8FbaaiBsqmNguDBYgVe1l9cr02Z9mltFCjN4kTRCf9YfTsX9Or2EGtoPNTiTVN4mAyk_xzphR_tl8o4mSas4kO-K53OKj3fO3NOduPNMUiFoSWgTbByZ-hyZ8dOkIp43PaACmpWLOjP9T-FKOsk4EIREdTT9HGwXXVrdRRS94YzHzVve96fMJ-BZFQc_IePAGmnhjTE2U-OX952tPic64qhxwrFiWVKVW4CDnESvKLcCvmojk1V1YBfbyRl7W-iOUE1LY8_XcnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرکردی‌ها با شعار خون‌خواهی به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/454921" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_AEpS35uD66cGAk2gOhPfa4zInV_q_oO4jAJKw0dVQIkC25t9gcTiySv-VmlbXapBxNigCs4_Ie3M2GPI_PIncvNk_w85WEnFucDjco1gp29zw-vKVlD08wYld_xjAIGmAwDSlrRt36Kq6lAKS1f513A6bYrHs_XJzCUmDIrQbTsVXDPUK5Elq4tdNQikSlCLYkn3okWgpZe5Csau1zT61wIkfF52mk055TD83hN7wOUo7djSnGFWkqMAEbImwcqQ26hVwH5oYoI92nC-2HNN7lsUhaR3rCL3d1aKrGcLrHZl-izjygQlupAFvmxdZ1w6et13wX8fdCw-qUjCApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس از موشک یمنی نفتکش‌های سعودی را به دروغ واداشت
🔹
خبرگزاری آمریکایی بلومبرگ: برخی از نفتکش‌هایی که به سمت بنادر سعودی در دریای سرخ می‌روند به جای مقصد نهایی خود در عربستان، نام کانال سوئز یا بنادر مصر را به عنوان مقصد خود ثبت می‌کنند.
🔹
این تغییر رویه تلاشی است برای پنهان‌سازی هدف واقعی این شناورها که همان بارگیری نفت خام سعودی است و همچنین فراری از گزند حملات موشکی یمن که در واکنش به محاصره عربستان، دریای سرخ را به یکی از پرتنش‌ترین مسیرهای آبی جهان تبدیل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/454920" target="_blank">📅 23:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
وفاداری کاشمری‌ها در شب ۱۶۰ بعثت مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454919" target="_blank">📅 23:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aed543861.mp4?token=XAEDSdOmWmINsMSj0glnmdT1waAJMBALHjDsjBkL0_O7oriby4w0DwQyubHhG42MpOsZ3s5hhxZDkCMCI3WW2_Uf7oNS7m-DrbXlfxYuNiRLdFfTxAVhn6Zs4M6gyykf6QMlJ6GCAbI9DPO0RwuV6p88en70M1XXamGH3zeQaGFtM24Ovupr5fAabqdvtDcnlwlRfD8LA7mfPY5_Wthf44PXVdVHDkzKBXVKq6OaGBNWRdKyjINWomXP_9m0PWsCKYtfXhgjb0hxv-vDPn2hF5LwKgWaftRd5Xb3UU3J0iTnMOz-7Oi63E1mWelee9aVBZ_aXYBcSijiqFQZ6YDi1zoN712RjVBSad6UVrD9VsiHa3s66kJfTXMF-2JoQkvlg0lHClFPVPLnuQWQdhD-gMj72dnao-TEGfUaAxmEvp0a1yVaJn9qHcoFoqrZLHeOUz53DdF8HXJTuljYMnFqbuOOnNIDyian4lCVL2aN1tBH0iQiXw9igRmkWkCyDmwkn3ZQc7MuUpVaUasg8qeClOyVKY0Du1FtexkIq_NqPDJzX5_UKBuHi8oK7rXOuhSjg6uJaF35-knD7nplgjhU-7KM66bf5ke84y0g_oajZIHR9zEm3LVF-Rmp4oxBLqlzni4wO8HUhRiWzww7ImoGXjalamV84OUogHXLDZReXR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aed543861.mp4?token=XAEDSdOmWmINsMSj0glnmdT1waAJMBALHjDsjBkL0_O7oriby4w0DwQyubHhG42MpOsZ3s5hhxZDkCMCI3WW2_Uf7oNS7m-DrbXlfxYuNiRLdFfTxAVhn6Zs4M6gyykf6QMlJ6GCAbI9DPO0RwuV6p88en70M1XXamGH3zeQaGFtM24Ovupr5fAabqdvtDcnlwlRfD8LA7mfPY5_Wthf44PXVdVHDkzKBXVKq6OaGBNWRdKyjINWomXP_9m0PWsCKYtfXhgjb0hxv-vDPn2hF5LwKgWaftRd5Xb3UU3J0iTnMOz-7Oi63E1mWelee9aVBZ_aXYBcSijiqFQZ6YDi1zoN712RjVBSad6UVrD9VsiHa3s66kJfTXMF-2JoQkvlg0lHClFPVPLnuQWQdhD-gMj72dnao-TEGfUaAxmEvp0a1yVaJn9qHcoFoqrZLHeOUz53DdF8HXJTuljYMnFqbuOOnNIDyian4lCVL2aN1tBH0iQiXw9igRmkWkCyDmwkn3ZQc7MuUpVaUasg8qeClOyVKY0Du1FtexkIq_NqPDJzX5_UKBuHi8oK7rXOuhSjg6uJaF35-knD7nplgjhU-7KM66bf5ke84y0g_oajZIHR9zEm3LVF-Rmp4oxBLqlzni4wO8HUhRiWzww7ImoGXjalamV84OUogHXLDZReXR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کلاته‌رودبار سمنان از ایستادن پای تنگه هرمز می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454918" target="_blank">📅 23:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5493f0e659.mp4?token=VL-vYg50qGobBL0jEBzhisZ7R6dni2v-1SK8Tn2a-M8TTH_lWmFeHpCb_YrXtcYWpwFEUWrPRCNaNNVLDCHTj0ssj-N0twARtNUMroasuJjteXK1Q19TmsksrjxOW1r74zGQHSUioCGmFkrztMEoX0FFlJT4rycWfngpV1VpfmFXgudx1fvt1IapPypoXI6nIRd2GXNAuOlO3DSlQZpIuhcA2OTZLO6u23DKr5aVfY0cZdhj9OZGH4wnn32jCfFKBkJEpB3e0ADF2_5_x1oYqIxq2W6oS-MrlGMRHw1msJT1hn0acnBNwEhAjPD2RCLe6LP4bAExEgTXW3bCsNl_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5493f0e659.mp4?token=VL-vYg50qGobBL0jEBzhisZ7R6dni2v-1SK8Tn2a-M8TTH_lWmFeHpCb_YrXtcYWpwFEUWrPRCNaNNVLDCHTj0ssj-N0twARtNUMroasuJjteXK1Q19TmsksrjxOW1r74zGQHSUioCGmFkrztMEoX0FFlJT4rycWfngpV1VpfmFXgudx1fvt1IapPypoXI6nIRd2GXNAuOlO3DSlQZpIuhcA2OTZLO6u23DKr5aVfY0cZdhj9OZGH4wnn32jCfFKBkJEpB3e0ADF2_5_x1oYqIxq2W6oS-MrlGMRHw1msJT1hn0acnBNwEhAjPD2RCLe6LP4bAExEgTXW3bCsNl_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدان برای ایران تا پای جان در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454917" target="_blank">📅 23:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0f07184e.mp4?token=v1LB4kjmtToto988_zPHWVvubwUQHXu2u7-Bf7W6LJS_jfaWsTB9RXbWAiGubZ6jhd1L5zI_nrJJIgeEZTGmTQuVgcDLAM729u5fxPHYzpCjDIvnXs0oRkxq8UT_FnzwOHY0lFuADqKImqSeM-1tC6s4wTy1AiTV232kiASd_KQ44m1E5WVBjDIR3RMRI_DhwXitkn-idG_2eGoxDtNMeVOIYmA2ZL_OhGw80BHkqmUKLy0BHhPQQ2oJ4J4IG8XWuRiWxG2bC8W9OO3ptPAFb5kcP1J4N57WAlPpyJa2FijOsgIY-iwtYalJfops-prUUqHIXBIRPEG_h96rBs7OFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0f07184e.mp4?token=v1LB4kjmtToto988_zPHWVvubwUQHXu2u7-Bf7W6LJS_jfaWsTB9RXbWAiGubZ6jhd1L5zI_nrJJIgeEZTGmTQuVgcDLAM729u5fxPHYzpCjDIvnXs0oRkxq8UT_FnzwOHY0lFuADqKImqSeM-1tC6s4wTy1AiTV232kiASd_KQ44m1E5WVBjDIR3RMRI_DhwXitkn-idG_2eGoxDtNMeVOIYmA2ZL_OhGw80BHkqmUKLy0BHhPQQ2oJ4J4IG8XWuRiWxG2bC8W9OO3ptPAFb5kcP1J4N57WAlPpyJa2FijOsgIY-iwtYalJfops-prUUqHIXBIRPEG_h96rBs7OFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانه گرگانی‌ها به ایستگاه ۱۶۰ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454916" target="_blank">📅 23:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgEU3LdNIb00ycbQb3zXlQXbalvCv-6k0Wt70hL2ar6j5ouGxUo1g9u7ZSUT2jQJE6OJQn_bW35BG3-hAPP26TAQQeSGRjCh0GDRFPnhnCJnAHPRQnwGtm3sZgMpPd1JgJJVuk9dfOoM_NO9CVTQ_yhN3vuD4zkYFLIPHb-j7YGUhSa1SHctkUgiQnyARpUPyXi8ieavEM_rRrPQUbMk6S7V4Qtp5SUjxD5kXhMzmBV7RNizCw2TLDlJ3pIrwHPRzGy_cLYETHfsw06msWGja4ZBhq0anJXCFp5shraYLD1KZAkB7F0763Lt5bZI3AK3l0PKCWvZ2KEN3dPt2jf74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: ملت بعثت‌یافته ایران تا استیفای حقوق خود از میدان خارج نمی‌شود
🔹
ملت بعثت‌یافته ۱۶۰ روز است که علی‌رغم همه دسیسه‌های دشمن، در میدان حضور دارد؛ این ملت تمام‌قد در مقابل دشمنان ایستاده و تا استیفای حق و حقوق اساسی و مواجهه با ظلمی که دشمن بر او روا داشته از پای نخواهد نشست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454915" target="_blank">📅 23:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
خون تاکستان برای وطن و مقاومت می‌جوشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454914" target="_blank">📅 23:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G03ZtnizsgVjz6QdJHmNFhVFSt-ptkDLu6Tv4ISmOoqDGt7sl3J42qgv0vM-vhXd6foUBpltFj-FPCFzX0ReOUgppR2JkcewU4h3VQlLS3oXeBOygkrmfZ9Vdu6iAo3lX0G3pDowWN03dPzUfAadxA6jnk11Z8En62KNYzHFQUkQu3oYohCJo7AeR5NRDDMHJmdvaiQ7db2zZ8fOOvjoM9I6uNLkOVe4JMxeULaGw2jsrinabyvuelwew5dUzw7NB07NAj6Q5b_4m0r-0rqZDp9zPeZNEYuQJMcoMP1iqIdPqIck0dF_gCemwmbdBABh5J7O1pbJYGUgoL0xpsO_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق مکه؛ ائتلافی برای نجنگیدن
🔹
عربستان سعودی، پاکستان و ترکیه امروز جمعه ۱۶ مرداد در مکه سندی امضا کردند که از آن با عنوان «توافقنامه دفاع مشترک مکه» یاد می‌شود. مهم‌ترین بند این سند، بر اساس بیانیه مشترک سه کشور، «اصل دفاع جمعی» است؛ به این معنا که هرگونه حمله مسلحانه به یکی از سه عضو، حمله به هر سه تلقی خواهد شد.
🔹
اما اولويت‌ها، سازو کار تصمیم‌گیری در سه کشور، تجهیزات و خلأهای فنی در توافق، تا حدی است که هرگز فرمان نبرد مشترک صادر نخواهد شد.
بیشتر بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454913" target="_blank">📅 23:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی بروجردی‌ها در شب ۱۶۰: لشکر با ابهت لرستان، گوش به فرمان امام زمان(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454912" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با گفت‌وگو توانستیم جنگ لبنان را متوقف کنیم، محاصره را برداریم و برخی تحریم‌ها را کاهش دهیم.
🔹
عده‌ای می‌خواهند بجنگیم؛ همان چیزی که اسرائیل می‌خواهد تا ما را وادار به تسلیم کند.
🔹
ما کوتاه نخواهیم آمد و سر تعظیم فرود نخواهیم آورد. @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454911" target="_blank">📅 23:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کلیات توافق نهایی شده بود و برای افزایش اعتبار آن، قرار بود امضای نهایی از سوی ترامپ انجام شود تا امکان عقب‌نشینی از توافق وجود نداشته باشد.
🔹
اما کمتر از ۲۴ ساعت بعد، روند مذاکرات به‌طور کامل تغییر کرد و توافق به سرانجام نرسید. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454910" target="_blank">📅 22:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از قالیباف خواهش کردیم که رئیس تیم مذاکره‌کننده شود
🔹
همکاری و هماهنگی میان دولت، مجلس، قوه قضائیه و نیروهای مسلح، عامل اصلی عبور از شرایط سخت بوده است.
🔹
بی‌احترامی و تفرقه، خواستۀ دشمن است و باید با همدلی و احترام با یکدیگر رفتار کنیم. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454909" target="_blank">📅 22:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هرگز استعفا نداده‌ام و نخواهم داد  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454908" target="_blank">📅 22:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ دولتی به اندازۀ ما در جهت سیاست‌های رهبری قدم برنداشت
🔹
اینکه عده‌ای اختلاف‌سازی کنند و القا کنند رهبری چیزی می‌گویند و دولت چیز دیگری، هم در حق رهبری جفاست و هم در حق دولت. @Fasrana</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454907" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تفاهم‌نامه آتش‌بس با هماهنگی، تفاهم و همدلی در شورای امنیت ملی شکل گرفت
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم.
🔹
کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454906" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا از سرزمین کشورهای منطقه به ما حمله می‌کند و ما باید از خود دفاع کنیم
🔹
مبدأ حمله به مدرسۀ میناب در یکی از کشورهای مسلمان بود.
🔹
دشمن از پایگاه‌های آمریکا در برخی کشورهای منطقه علیه ایران استفاده کرد و ایران ناچار به دفاع از خود شد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454905" target="_blank">📅 22:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454904" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454903" target="_blank">📅 22:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیر بار زور نمی‌رویم، اما به‌دنبال جنگ و تجاوز هم نیستیم
🔹
ایران به‌دنبال جنگ یا توسعه‌طلبی نیست و تنها از توان دفاعی و امنیت خود حفاظت می‌کند؛ اگر فشار و تهدید علیه ایران متوقف شود، دلیلی برای ادامه تنش وجود نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454902" target="_blank">📅 22:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454901" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454900">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در جریان مذاکراتی که با فرانسه برای لغو اسنپ‌بک شکل گرفته بود به تفاهم رسیده بودیم اما آمریکا نگذاشت.
🔹
اروپایی‌ها اختیاری برای تصمیم‌گیری ندارند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454900" target="_blank">📅 22:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454899">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با امر و نهی نمی‌توان جامعه را به درستی اداره کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454899" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: خیلی از مشکلاتمان با کشورهای همسایه را برطرف کردیم اگرچه آمریکا و رژیم صهیونیستی با توطئه و جنگ اخیر به دنبال ایجاد اختلاف بین ایران و کشورهای حاشیه خلیج فارس هستند.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454898" target="_blank">📅 22:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مساجد، مدارس، مراکز بهداشت و شهرداری‌ها پایگاه‌های عملیاتی هستند که دولت می‌تواند برای اجرای برنامه‌های خود در سراسر کشور از آن‌ها استفاده کند. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454897" target="_blank">📅 22:09 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
