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
<img src="https://cdn4.telesco.pe/file/brXB60FjS3BZY9TZbHFrX1raRACsh4KzFgryTQ7uGkFymfjfxs2WaJ3vOIX-uoplUtjIPWCtFf8EVNsWDvdPOcC6MNGN_pO2ScWWVV79AtemOhAvSLMt6faPuqZ-evioaXDdU-zI9nGHI-r40k-7cyYOXGbDZ5Yf6qVxTmGxyCN-2x_m2dEO_zgt9QhUrT8x6O39Oov0v7DqNaDlCAJKc8yHob-UEO3wRFfsW28_8k4yKFIUywn4rdiuVj2GMLayYZOzo5VizwU1ps6puqTZz5EEft_VPNghJ2jO_haEy-6mCr-CbLALCZK2HhSL2Lqfx3kZhRyifEHREvjRmgymZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 04:49:51</div>
<hr>

<div class="tg-post" id="msg-461030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASDe1M_xcwyp3tEJo51ohNOvF9Y80f3R8xhzoCOtcJDQxBdcA1yVkj0a9d2-85u8ow-9O2jb6rdaa-0h5XWetbraidoI2dq9yXJ7luVVldXCCTTtDrkg852QlbgBfudfHGBRfvgxxOOw2BNDAUo3V3QBnceLQ0QdTo5fj9bRP2ItbdqXhJBY6CIb1J6-G9aUYh-2GbKDy8BgPQEef73mvGuhgB5TUJRCmU7_E-tom81XLgMtMPuxBd9lpRJ7fsfRY057WiLJaPSF6xuOzMPj2peBZ8McQozP08vptublvgL0L8UcW6rJyZq7Nz_PnbxAloteSIXJZ5Tf8vohTZL3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارچ نتانیاهو لجن‌مال شد
🔹
دقیقاً یک‌سال پیش، بنیامین نتانیاهو پارچ آبی به دست گرفت و در یک پیام ویدئویی خطاب به مردم ایران ادعا کرد که «به محض آزادی ایران، کارشناسان برتر آب اسرائیل به شهرهای ایران سرازیر خواهند شد تا فناوری‌های پیشرفته را در اختیار شما بگذارند.» او حتی از کانال تلگرامی فارسی‌زبانی یاد کرد که سال‌ها پیش برای آموزش مدیریت آب به ایرانیان راه‌اندازی کرده بود.
🔹
اما در سالگرد این سخنان پرطمطراق، رسانه‌ها و شبکه‌های خبری جهانی از یک فاجعۀ زیست‌محیطی خبر داده‌اند که حالا خود اسرائیل را با بحرانی جدی در تأمین آب شرب مواجه کرده است.
🔹
بر اساس گزارش‌ها، یک شکوفایی عظیم و کیلومترها گسترده از جلبک‌های میکروسکوپی در دریای مدیترانه، ۵ کارخانه از ۶ کارخانۀ بزرگ آب‌شیرین‌کن این رژیم را به‌طور موقت از مدار خارج کرده است.
🔹
از آنجایی که اراضی اشغالی حداقل ۶۵ درصد از آب آشامیدنی خود را از طریق شیرین‌سازی آب دریا تأمین می‌کند، تعطیلی هم‌زمان این کارخانه‌ها یک وضعیت شکننده و خطرناک ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/461030" target="_blank">📅 04:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6486ad58fc.mp4?token=BNQ5rPTIvrER0KoOZwBglX8jKOAykRIeBNm1-71altC7SVCWGRpCYbNIHZNikgBgu-33RX7utijGKrwHMP405mE8sgx_paJMo1LWJF23_xpk1qL5sQ9KAGOK3W-GEDiMzdW6xqkCpbCejEO-U_v4bQqdm2ANTYoihaMqnWDnnTKRPVgDE8TBpAeLmkNxOb1cqAhaASqPnyf9uUQ5RKnLUQq1Aj-ImxEumVKhY0RmQW3PsyqwgqiAh7p3ZxTWZBd_oDsfkTfvg1ZZw8BrOIwaB8xQMghlDRRhBgqY-zpU3zSnjHmBROziSDrWyoKf7gH4Y7-UtPuxkfXDmCO8c68IyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6486ad58fc.mp4?token=BNQ5rPTIvrER0KoOZwBglX8jKOAykRIeBNm1-71altC7SVCWGRpCYbNIHZNikgBgu-33RX7utijGKrwHMP405mE8sgx_paJMo1LWJF23_xpk1qL5sQ9KAGOK3W-GEDiMzdW6xqkCpbCejEO-U_v4bQqdm2ANTYoihaMqnWDnnTKRPVgDE8TBpAeLmkNxOb1cqAhaASqPnyf9uUQ5RKnLUQq1Aj-ImxEumVKhY0RmQW3PsyqwgqiAh7p3ZxTWZBd_oDsfkTfvg1ZZw8BrOIwaB8xQMghlDRRhBgqY-zpU3zSnjHmBROziSDrWyoKf7gH4Y7-UtPuxkfXDmCO8c68IyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آماده‌سازی و پرتاب موشک‌های سپاه برای هدف قراردادن ناوشکن‌های آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/461029" target="_blank">📅 03:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a902bd19b.mp4?token=IOOfovuHBOdrb1OsGPsERuoLIvcqbbB3y7rLkatmxYmhP3kMmQGW794YG2ZkiSou01sJfSuJvPdtGogl_gAGXRO-HCHkUYxCGvtEgn5Hinm0Ze7B-dsnB8GHphuTnna1cPmaE053nM6Ta23nC8d0rSTw0LDHFUZh9vCmyPHrSjH8_XyLTWAeOzv8h2d-jnt-hMKjoMLiPMXJ_MGjg9iRQYtV81mZ6Kf7CnuwPBZTdjZN4aEZIKv25UCactwq0zNTVNknuMQsLTnrAzPe-54JRMA7yaD5wTZIRW1mX1E6P-mCKc7SKYyrjIzVyPYYOR23Aq8i2arNX6GFDtRHNxMswg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a902bd19b.mp4?token=IOOfovuHBOdrb1OsGPsERuoLIvcqbbB3y7rLkatmxYmhP3kMmQGW794YG2ZkiSou01sJfSuJvPdtGogl_gAGXRO-HCHkUYxCGvtEgn5Hinm0Ze7B-dsnB8GHphuTnna1cPmaE053nM6Ta23nC8d0rSTw0LDHFUZh9vCmyPHrSjH8_XyLTWAeOzv8h2d-jnt-hMKjoMLiPMXJ_MGjg9iRQYtV81mZ6Kf7CnuwPBZTdjZN4aEZIKv25UCactwq0zNTVNknuMQsLTnrAzPe-54JRMA7yaD5wTZIRW1mX1E6P-mCKc7SKYyrjIzVyPYYOR23Aq8i2arNX6GFDtRHNxMswg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: ناوشکن‌های رزمی دشمن حامل موشک‌های کروز و ایجیس مورد حمله قرار گرفتند
🔹
روابط‌عمومی سپاه: در پاسخ به اقدامات تجاوزکارانه و ایجاد مزاحمت شرورانۀ ارتش تروریستی شیطان بزرگ برای نفت‌کش‌ها وشناورهای ایرانی، نیروی هوافضای مقتدر سپاه پاسداران انقلاب اسلامی…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/461028" target="_blank">📅 03:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4752a39be.mp4?token=jxuVRocjd6MyHBJMVBtE6CIIyYnVNCD1g_05yJWxSSc2oKQLZN5YvmLih8Q8T827Waxek2DQgrd7cOXqKO618fefLS0QTSVfldU1Y4NrD9b3Zh0KN3X7UODBayael9Vet-JuOUBeL9-0gU-bGB-9sJ2TGXIO9yu-jBEWQjvUxj6ibaQL-JZuy7EB7oVdRHSzko5RgJy6J2uuY1JwnHcy2UFeCuI1LUOFwTQqq5haZY-ql5yJii9TKWHC7aIedBJ5fz2Z_JVb_OoW8lbhhwPkIjhwhSeZGpgU-OCwXHzNDlAraOyipjA6OLOlxmYCMpAt2AlKQQWelA0YJayBEL0JdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4752a39be.mp4?token=jxuVRocjd6MyHBJMVBtE6CIIyYnVNCD1g_05yJWxSSc2oKQLZN5YvmLih8Q8T827Waxek2DQgrd7cOXqKO618fefLS0QTSVfldU1Y4NrD9b3Zh0KN3X7UODBayael9Vet-JuOUBeL9-0gU-bGB-9sJ2TGXIO9yu-jBEWQjvUxj6ibaQL-JZuy7EB7oVdRHSzko5RgJy6J2uuY1JwnHcy2UFeCuI1LUOFwTQqq5haZY-ql5yJii9TKWHC7aIedBJ5fz2Z_JVb_OoW8lbhhwPkIjhwhSeZGpgU-OCwXHzNDlAraOyipjA6OLOlxmYCMpAt2AlKQQWelA0YJayBEL0JdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام صریح ایران که روی موشک‌های شلیک شدۀ امروز نوشته شد: ایران سر سوزنی بر سر تنگۀ هرمز کوتاه نخواهد آمد. @Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/461026" target="_blank">📅 03:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f2c8daff.mp4?token=qrgK98DM5N6gFkVWVveY9eETqycYPnHn4H8i5S4yfBpD_5EOYb8ONlU5QMIACt7DZ3tzEeeGtJ5S_VuWnYYUHRYmG13pORwhs3KYnEX5CQrJcY_1OJhNvt2Pikl0Gphad5sD25A6srdUrB5-KuJK1XISe6hz2VGi95cAKRp0DA3fmrFUUfFg4q9NhUHd06FfFcu639XZhHNm56NpE04ce7eZBfCZMbsUs0Dc_z-6twdySZjz2yB4IvSVto3jrRPGyIf14tV-jhBVHBPuxzH7rpayt9B_ZQciNTRWtBnma_mP9gX6V3E-QnmsG3WxxtL0-vqPF88A_0gbNMQq1uyz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f2c8daff.mp4?token=qrgK98DM5N6gFkVWVveY9eETqycYPnHn4H8i5S4yfBpD_5EOYb8ONlU5QMIACt7DZ3tzEeeGtJ5S_VuWnYYUHRYmG13pORwhs3KYnEX5CQrJcY_1OJhNvt2Pikl0Gphad5sD25A6srdUrB5-KuJK1XISe6hz2VGi95cAKRp0DA3fmrFUUfFg4q9NhUHd06FfFcu639XZhHNm56NpE04ce7eZBfCZMbsUs0Dc_z-6twdySZjz2yB4IvSVto3jrRPGyIf14tV-jhBVHBPuxzH7rpayt9B_ZQciNTRWtBnma_mP9gX6V3E-QnmsG3WxxtL0-vqPF88A_0gbNMQq1uyz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک انبوه موشک‌های ایرانی به پایگاه‌ الازرق اردن، محل استقرار نظامیان تروریست آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/461025" target="_blank">📅 03:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
شلیک انبوه موشک‌های ایرانی به پایگاه‌ الازرق اردن، محل استقرار نظامیان تروریست آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/461024" target="_blank">📅 02:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
چه کسانی می‌ترسند نام متجاوز را به زبان بیاورند؟
انگار این موشک‌ها از یک آسمان بی‌صاحب آمده.
@Fars_plus</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/461023" target="_blank">📅 02:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsHeGvlKwPcNVhYyShZU-2F4NYPUqTRco4LR6yFF6e4CviNpacg5oO2MSytPcQmyTcTF3ina8lwEO27XcDy-bxhoEi6VT6mNSSWw4p46xgZn4Q4khQUGqZL9pej7vPbwEpMQTh8VgzhqqbyGr5zNqeaKHWOjXSwpl9CKgtSnoT6oQ_SFNkWpf_xDaoqUVEDYGinvsM25IfB1XImcuUdejrn0o-rbNTFf5bxID9JKLY2fN7Z9JqYfBddMg_BtMsIvntdKmNBiUO7lLLFj2m9jNoglPZVnipgfSf5jzVB_O_khcR2OWdvNSdLnNl3ewO87XBRlMLOaD6fRvQOW9I5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی تجاری در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس: یک کشتی تجاری در بحبوحۀ فعالیت‌های نظامی جاری در منطقه، در آب‌های شمال عمان مورد اصابت قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461022" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/461021" target="_blank">📅 02:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به تلافی حملۀ متجاوزانۀ رژیم آمریکا به نفتکش‌های ایرانی، رزمندگان قدرتمند دلاور و جان برکف نیروی هوافضای سپاه پاسداران انقلاب اسلامی در عملیات تنبیه متجاوز پایگاه آمریکائی الازرق اردن را زیر ضربات سهمگین موشکی خود قرار دادند.
🔹
در این عملیات، با حملۀ سنگین موشک های بالستیک سوخت جامد و مایع آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 وشلتر جنگنده‌ها مورد اصابت قرارگرفته و خسارات سنگینی به دشمن عنود وارد آمده است.
🔹
دشمن در مواجه با نیروی دریائی قهرمان و مقتدر سپاه پاسداران انقلاب اسلامی در تنگۀ هرمز از موضع ناتوانی و عجز و ضعف، دست به حرکت‌های مذبوحانه زده و بلافاصله پاسخ قاطع را دریافت نمود.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/461020" target="_blank">📅 02:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای ارتش تروریست آمریکا دربارۀ حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی سنتکام مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461019" target="_blank">📅 01:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsrB9Xz1p9SAGkKUWcesOLnYkd3gkwmp-fminVol9quZU9ktYDxY49CFbygJlb-ovbxmtiBbtBFZJIJxVzJd1a_I2rrgEMHG3jGahkJM51rUEDE7wHqUL21KrUidX_ZQW8HnTvjHeAc5ac0Axu2xzu8UDJ7v396RZihq1VmWZaRZgpkwj2FJmLKjXWaeAX0yIKedw4DgL-9Ol2k_I2_dLCzlxAlKGgvEI-lLLaLsV57Djrdc6jtZVBSXEPaWyRosZt6mV7gBF2xMKIdwk11skYZaMd1JjKxuaiFiy_mX0NufAvH0ttOENT7cOfcx3p0LDM-pzsni6iBQZUWF2mlVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461018" target="_blank">📅 01:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در بحرین
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در بحرین رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461016" target="_blank">📅 01:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbdfc4f17.mp4?token=HF-eV8L7skjHxxn6YMEBEVZM9g1sLYe0MD-Vql__gTBiqmrrID6kfBHggvHmEB0MFBQp3TqN-BCG51bhmaN8d9PJQVSzLuh7JRtFH2Oia_cmO7Re30E6bV73KWXjnnBaJNgIbae1f9ghql4xrU8oWnFTngU0ojVXggFUdBtU7JA6et4JraN6z08sVf1MHhfH0EMmyq6ftGKuhzuFRy-8la8Gd95H5UkMQM_5CKkv0-w9xTkZ8D0vpFPXII-iAhH3V2xSiH52ugG0JUX52FUZGbqkOOWq7SywD0r3nZxwksKpHxqtZCvibNr6Wg2aFtsLGuTVzkvvgQkFOaHPcFjydg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbdfc4f17.mp4?token=HF-eV8L7skjHxxn6YMEBEVZM9g1sLYe0MD-Vql__gTBiqmrrID6kfBHggvHmEB0MFBQp3TqN-BCG51bhmaN8d9PJQVSzLuh7JRtFH2Oia_cmO7Re30E6bV73KWXjnnBaJNgIbae1f9ghql4xrU8oWnFTngU0ojVXggFUdBtU7JA6et4JraN6z08sVf1MHhfH0EMmyq6ftGKuhzuFRy-8la8Gd95H5UkMQM_5CKkv0-w9xTkZ8D0vpFPXII-iAhH3V2xSiH52ugG0JUX52FUZGbqkOOWq7SywD0r3nZxwksKpHxqtZCvibNr6Wg2aFtsLGuTVzkvvgQkFOaHPcFjydg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
موشک بارشی ایرانی در آسمان «العقبه»، از دید دوربین صهیونیست‌ها در بندر اشغالی «ایلات» @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461015" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHt6rFO07ytbogT03nADjxJLcqt62DdYAas29081AiRz6xIhaKA1S90kkWuD5wLWwVRvy_dUoXA-TLXkwx-qNHMTZSnjdPdvoJGPMAQp4Ilp-By3hQPmy4MCfywRxnAf0cczHvqcEtxJRDZTiDuXXZwaUN3tAuR7cJjNvBNLyNz6dFTU07-bBHtI9de9LOZks2QReAYkvloXzqRhWGbpn2iURaDx3Fi8ngAqaICuvQyCMN8tO8D7iNUL2wLIQ_Sw3agB1X20tUisQ5FbsA_yjUQM4M148Yoco_bnBtc2zi-DIBhZRNWCJTwwyfCfC2bDbGTQUlcVM4E6whDcPF1NEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
فرود موشک‌های ایرانی با کلاهک‌های بارشی بر سر تروریست‌های آمریکایی در منطقه «العقبه» در اردن و ناتوانی سامانه‌های پدافندی در رهگیری آنها  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461014" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=o76t4xtIuabH2eGwCUMOxhfQSs7IiYSJuv75OZbSX4cccKxjk4posMAcpGQvZ8JcNRu5i8qjvktrPYAEpjC0vptqwMN17WqrMkcpDswyuJdYuOj_xyNidvuSUdPd4cc0XNFUiOTmxEa1FHUiVc3G_eO1GT1afd6-OVxJiOmgBld_PKOTC5q7Yt0yvnoX6F4x_PuIu9_27Y1nheAFQifEcww6k6yKhmq9RcqI3lYFXdbncK0N8MCTZMfp2BbS3z8WEcO8fUxqI0HJIfWc3B_mqlhdb-HLSiqMt9CWUDNG9gtVOdcF8DEgXCHzWLQWhQGEN4lSsNNv_trNId58URUlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=o76t4xtIuabH2eGwCUMOxhfQSs7IiYSJuv75OZbSX4cccKxjk4posMAcpGQvZ8JcNRu5i8qjvktrPYAEpjC0vptqwMN17WqrMkcpDswyuJdYuOj_xyNidvuSUdPd4cc0XNFUiOTmxEa1FHUiVc3G_eO1GT1afd6-OVxJiOmgBld_PKOTC5q7Yt0yvnoX6F4x_PuIu9_27Y1nheAFQifEcww6k6yKhmq9RcqI3lYFXdbncK0N8MCTZMfp2BbS3z8WEcO8fUxqI0HJIfWc3B_mqlhdb-HLSiqMt9CWUDNG9gtVOdcF8DEgXCHzWLQWhQGEN4lSsNNv_trNId58URUlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
فرود موشک‌های ایرانی با کلاهک‌های بارشی بر سر تروریست‌های آمریکایی در منطقه «العقبه» در اردن
و ناتوانی سامانه‌های پدافندی در رهگیری آنها
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461013" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ منابع عربی از حملۀ موشکی به پایگاه الازرق، متعلق به نظامیان تروریست آمریکا در اردن خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461012" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461011" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/461010" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGJmv11AhoctH4x3TXaLKCILMAW84ly4x3VGtC2d6adMHeQIV489wKI54d89KdP9Z1JQBk_oWeAunWTJBrt2g_VccP_je1HdmAr-nHx8DEFSExRX67fGA_II4Ep7XpO0ZfcC5xvRaHp4thOJ8WdielkyKaRtoSQ7oA54LZadQDJJirxpIqrdEc4RfONp8iTbqCBFU52WaAvY1kflayWeEky0FnEK3QCyP6g0Ab8c5wlkWHrzG_z0asN2wwhHYjcJmQjQdtopa4u_EdKI7duS7W8QqFOEG6j0KBpVSEH7-PW5c2p2XpP0VpNogpn230F8H3Gh-0XT27OtOrVZOHeB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران چشم پنهان آمریکا در اعماق دریا را هم کور کرد
🔹
آمریکا طی سال‌های گذشته سرمایه‌گذاری گسترده‌ای روی سامانه‌های بدون سرنشین انجام داده، بر همین اساس کارشناسان معتقدند رهگیری و یه دام انداختن سامانه زیرسطحی هوشمند آمریکا، شکست سنگینی برای این کشور است.
چرا به دام افتادن چنین سامانه‌ای اهمیت دارد؟
🔹
محمدی، کارشناس مسائل نظامی گفت: اگر یک سامانه با قابلیت پنهان‌کاری، خودمختاری و ماندگاری بالا در محدوده‌ای مانند ورودی تنگۀ هرمز شناسایی و سالم به دست آمده باشد، از منظر جنگ اطلاعاتی و ضدشناسایی، اهمیت بیشتری از یک انهدام صرف دارد. درواقع مقابلۀ موفق با این سامانه‌ها به معنای مقابله با یکی از مهم‌ترین روندهای جنگ مدرن است.
به گفتۀ وی، ماجرا در سه لایه اتفاق افتاده است؛
🔸
۱- شناسایی سامانه‌ای که برای شناسایی طراحی شده است.
🔸
۲- نفوذ یا غلبه بر سازوکارهای حفاظتی آن
🔸
۳- و در نهایت تصرف سالم آن.
واکنش آمریکا پس از کشف این زیرسطحی
🔹
پس از آنکه موقعیت زیرسطحی آمریکایی شناسایی شد، طرف مقابل برای پیدا کردن محل آن و بررسی وضعیت سامانه، از پرنده‌های بدون سرنشین استفاده کرد و یک فروند پهپاد آمریکایی از نوع MQ-9 نیز در این فرآیند وارد منطقه شد که هدف قرار گرفت.
شکست فناوری پنهانکار آمریکا در برابر توان اطلاعاتی ایران
🔹
این کارشناس مسائل نظامی گفت، اهمیت این عملیات فقط در شکار یک سامانۀ زیرسطحی نیست؛ بلکه مسئلۀ مهم‌تر، شکست یک سامانۀ پیشرفتۀ آمریکایی در برابر توان شناسایی، نفوذ و کنترل نیروهای مسلح جمهوری اسلامی ایران است.
🔹
بنابراین، عملیات اخیر را نباید صرفاً یک حادثه تاکتیکی دید. این اتفاق یک موضوع مهم در جنگ فناوری، جنگ الکترونیک و نبرد اطلاعاتی است و می‌تواند نشان دهد جمهوری اسلامی ایران در برابر استفاده آمریکا از نسل جدید سامانه‌های بدون سرنشین، صرفاً در موضع دفاع قرار ندارد، بلکه قادر است این سامانه‌ها را شناسایی، مورد نفوذ قرار داده و در صورت فراهم شدن شرایط، آنها را به کنترل خود درآورد.
🔗
شرح کامل گزارش دربارۀ غنیمت جدید ایران در جنگ فناوری را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461009" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110775d818.mp4?token=TTG52xTbUOp2-Mh42AJCtf3HVTnAivoLx8I2zw63EmUUUH6stUmqVgRF8b4IM0qm07kr3XLm65b_WFE3sneNgaVlfMrU8rgDwr9a7cKxmLz_oCvvquhseDKGLZ8pJecfSDefdQ8S9kBicvWvYHzWld27Rc9rYFVAusgfYFENyLod6KW96JEMhiWSOsxhXGCWTVsrj73eouLxRvxwo3s_tYWNjYtnpq0sgsQQ3mYhY22tqqGFRD_UVsoswofoPiUWDLE2JP0recrqg-2iOffJYzl9Z45aPK5n1pKWnBssAKtw6JWFZFYUyd0ew1Q7T_t6tKFz9mZTyGBtJoFxNznB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110775d818.mp4?token=TTG52xTbUOp2-Mh42AJCtf3HVTnAivoLx8I2zw63EmUUUH6stUmqVgRF8b4IM0qm07kr3XLm65b_WFE3sneNgaVlfMrU8rgDwr9a7cKxmLz_oCvvquhseDKGLZ8pJecfSDefdQ8S9kBicvWvYHzWld27Rc9rYFVAusgfYFENyLod6KW96JEMhiWSOsxhXGCWTVsrj73eouLxRvxwo3s_tYWNjYtnpq0sgsQQ3mYhY22tqqGFRD_UVsoswofoPiUWDLE2JP0recrqg-2iOffJYzl9Z45aPK5n1pKWnBssAKtw6JWFZFYUyd0ew1Q7T_t6tKFz9mZTyGBtJoFxNznB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نهنگ هوشمند شما اکنون با ماست، به خوبی همکاری می‌کند و به تمام سوالات ما پاسخ می‌دهد. از هدیۀ شما سپاسگزاریم!
🔸
لگو انیمیشن جدید ایرانی، از غنیمت گرفتن زیردریایی هوشمند آمریکایی در تنگۀ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461008" target="_blank">📅 00:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9fzAA4iP4eecOuPNHs08K9w_BQgnujGhgJNOT3lSnr6DMJqlc_KyeN2vumhr_soZ58H11rrO__5YBx_1aLOno0NebpzZsbxDy7Bw4pl9e2TcgThT4F4dafFBp0-vSc-tJWK4ZutRpysrbDSLoJHkXKJsquW78zfIfLtFd6RCvz7YNQjERnhI3skqQ-5bd7eukrz9NCJUjOQbGF2xnOesuRpKFg3n9ym2Ke_GQuL67wb6O5PzIA4cRl21KmUQKhiGNLXBip2tXLK3Eb2x_8wmbJTTBpl-0Zw88ddUGzQBM7RZqOewHt2LQexPRqyhc_b6CN4cgDCFRAed6XhWloC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
این قرار بین ما و ناوهای دشمن است
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461007" target="_blank">📅 00:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbFKcETQVLaZamenPZaYReOLgVGvW2Xo7XVxq288wzYBg1Ur1R7fKOhTejciT6DnSqphDH1ImyZHt3cmsLxgq0EWApKgLFItXjDpAGdvUqRpfpfceQ8YPA-OVXI7HkCnOjSC04BYWkFo9rYTDjVSIeBaDv75Oy7hMgVT5UPYC2akG1ohVhmg2LvhyLDsUlzA7KMFdXIv2Rf5c0YI_ubLYq__aRYPmyuTAj69ksZRT47sjw5G0quZbosoBaOtcouC_Fszn1oos3EyANkKSyTtPUjCZS3x0hOXY-WQuFqLMFjXke82TTUKjXKCVxSB2qN4uPS2kI_oMDE5uk2ySQ6B7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر گردشگری: در ۵ ماه نخست امسال باوجود جنگ، ۲ میلیون گردشگر خارجی وارد ایران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461006" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLubT-P9fRWjtvc_4pMQvXkxnBQnq0PFbWbabvBArPJciPymBqvtppeLygOmvlJdCfQPI5yxX05f07IAh8uFsiSIgt4LGKPTGkZVh4TFJntDlYamQP-SH2dG3cMxafGUsmO0rQyUdtVprhUnhhLqNNdA-8wCcyFzxSW4X_ubJOLJHlBd9kDPcfR2cjjj1oJDFGLf37CdkYPsW-Po5RfJSPktJVvQx99Zm9l_BABdGcK84bwj0_snhgqBjhYdplSNy4FNhFMgNAVA9CEJV7LXZ6zurWfho7uG7u_lZN33KF1IEBuiQS9McbEBucaL-KW23R45sYnyGVuDmWv1J8z8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKbajrzIkzwTfmZLE1S-hhNyrL8DyJsGQ2yVmL7DHbs3OZDsAJP3UZhQ3BwDcMawrl29C_0lBALFe6L_Zfknt6sAqZSSUHXm7kkjMgYnl-dnZcMQQ_wI4qlI8Y8WSSFli7uT9xil3r8wfYb2KS8fBqLx5IrF0zMhOht8Pekimmx_vaU4uw9m9km8nkxTb6E853KWBYGFmemlCO_KIyl84A_WU0TIw3wX7k_jS5kgXhiHxmQa4kNrM1mLcF5cG9I8HfwucjsMLhY8W0rvPW1gfT3h0BIBxkSOvAlZ-KaXiBewH07DBGYoMbCUSs37pvqsjXsT-SccjYHcCdF6j2MMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGocNbaxVHHkAqI90LO2CdiDQq9C6I78mVnLdsNGzQs7Q2iYA7zBfYwRRRDyL9M-lXbnqHXsdNGzKsnMs7tlXObGBeWrGsRhvS16s9YZ_tkx7k3ChnuCQ_MFojVgb8Ax68DumH3m4bmhq5kzhD8QVicqdjbt8RygToDUEypeze2AZvVfM38wz7QQlrTSovVRXSTfDQcBRGvAEA9KyYQnqK5MQuI8v8zF_MoAmFbxr4hWxSj7KxUxoKi6uxZmKRG8_pBf_Zsy1JAt-4NpUmEcHx-T_Q28HiP8qj5oXfl__br99Vp1wbV6-7zIkRptl0SWqAYcamJ00EWdKlUv0iJlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MH938Pub2c6vBrTGV7KVb7EG2dWjQ9OdbGEydLYfvjMI_bI3q2G236W9lONUK_tze5eMLePlHfTB6xci-P4MrucyAbplEGEQAm3HON6qR323fyDnllExyMmquDnQYQJNgie9w5i2zy7jgUufX3g5e3qc1hV-0oF2KcjCL3F4f7Sm04wpd-yVuzMxYFzZP3ZvemiT6_FgeS_oiVGIMicYncvNM_pS7ARbWPfoWCIqmtZmIw6k0GZJY1COKzN9spteIAE5Zr1R14EMDwdRulzJcA140OiAzJmJ90tz17ct71eU-Nq0x6FrPNh4opj9EmzTHT4t1nxB0ZzCdzSALRUkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKUerNY_rYy5ST7CQxNzc_l8rCHjxIbAW6WDS1zDenU3MQrt1IY4vJOWUej584fmxyexdax23EgLbfmgIcAo0mWvs3NP8TNw5Yx95R8xLayuW62VovIKmExA1xfbWe17XCqixUIuUSLe3jnjpPJlqz8LH4gk3Lq-39NeZOSzyWxuO6iRM6Kji3Ti6azbFPpf3JhmMYcaKu8C8XA_lJNBdco_AMUndFYq-jiGZA082wEzLCEPFKSPCZmJVVnl5nVna9ya_A8lsGBdrvRnRrf5xqHeYodhL2j3TYo8J1oviJkdvRcZ_2nG6MMc07yNuELvDJJmDZRgea6DZBw5G0Nreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZYuQP0TMPPQNpaSLpbnGaXt8lZ2y_BMHbcCKIr8OBkwoSZCv6pJxEhti34cBmCMEJDHn6ETF43_piPw-ryCuAd09y34I33uUny1NsObuAhcoyZ4bY7zvt9sZShHuV4M8vhiewSz9ZYcTW9hDPVEKTnuMMAk-Xm7RT1AuUTHfDM2J4T2Orm4gM3FND-_RAHRYntXou7I0eROyBQTCy7xqfHDoLxAluLG1l3mTdC6F1lJQ7VwW_w6SDzbCjlp2BCUByXR4m2iaoxTpBvV98IyWZRToZDdcAr9r342104UlDDRZBasUR7__qERNFlzN71B9cUBqDlCrOa2SwjWvancqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jg5c4-zovuNuLtrIO8lP_EK6sX1aUeIvx_p6t1KOz2-gwplagm6VdnXs_W3Npj3GfwkBCGM4BE3dHsrkN5nO23yoBSviCBOijPXWIOi9mPvhnu_fRAUoFu-lJRaLT198-NSBezx9Ptflmz8cfcUIelnkJGdMdnojRgeHJI7xxc9S8C4jz3b0u7v7SF4sRxIoWtnoDkA_vtmtlCWIVveocjxs7Tbf3Mr75y9xo76Cgf-MREJl994wz0ssOSJcIPpC28Fc7q7HQtQwm8NJQH-TnzMao1sosCiyUMflwbV-mmJ-V6dpBoFURLTQjGqkwGzOaYc9x7MO8AJicVVL8KvJ4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقه میدان‌یار در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/460999" target="_blank">📅 23:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtJIjt_BOcGeSBtnidQ76co5m_wJcWkl0oJfOsHmXe44ZkV-VzNkkszWb1UIyi825Rs2ncXtyk5qfT0t2-A6hFMt_1p1PWXr206Jbh-lUwnulnpugcHlVE4Wqax-JgXHj21PCr2SW_3H_hkU5txKriplgDUSfuCwBSy5dIVAfeEX8AL_1dFh6gI-7PKvCIcr9GbatWcV2S9riSCCQOqOvC7-ZanIeQtQ6vuVIe5iv0FToZXWbevAy2CtRW8Il4_sx2koIHNEbmXZ764E6o3G0Oc9kRuAlzNCw6671Ee4ts4nsjxpvuiok8dnB4K5lPWC_MlCnEDiWPR83rnFoMEr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: تمامی نفتکش‌ها در محدودۀ کویت و بحرین سریعا تخلیه شوند
🔹
با توجه به شرارت‌های ارتش تروریست امریکا در هدف‌قراردادن چند فروند از نفتکش‌های ایران، به تمامی خدمه نفتکش‌ها در محدودۀ اسکله‌های کویت و بحرین که میزبان این تروریست‌ها و شریک در شرارت آنان هستند اخطار می‌دهیم شناور خود را چه در لنگرگاه و چه در اسکله‌ها سریعا ترک کنند چراکه هدف قرار خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/460997" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c423b150c.mp4?token=JtE09HIOntmQHY5zc2wjpjbkXjOie7RcRuRy7j3RfnXO-8EovMTb_n8F2_Ue7K2zLaVGE8ili3wt1lpCPzbl_xRyZ9jxdq02mBGuNyhXZe2FwqAEZcyG3RT-LhNtvj13jHlbe20hnGnsF_WXXW-V9CZ-XNGlR5vsQXAq3ZQ2NoDGj4i5lgYYk-a-1HtmBzM-v_UCi_5Xbk5U3t0JVEsyMkXgQ3iWR2C_Ts1ee0BQ-o-d0z_Hum014BuZKVFq2-_RN0YXEoKNbJChco7eiCG6dOWbZgtNGK_PSF3cMlQNdQwnDEk07GQLbP7OW2jrt4KUqYulkJkVXOY28QJ5iTBTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c423b150c.mp4?token=JtE09HIOntmQHY5zc2wjpjbkXjOie7RcRuRy7j3RfnXO-8EovMTb_n8F2_Ue7K2zLaVGE8ili3wt1lpCPzbl_xRyZ9jxdq02mBGuNyhXZe2FwqAEZcyG3RT-LhNtvj13jHlbe20hnGnsF_WXXW-V9CZ-XNGlR5vsQXAq3ZQ2NoDGj4i5lgYYk-a-1HtmBzM-v_UCi_5Xbk5U3t0JVEsyMkXgQ3iWR2C_Ts1ee0BQ-o-d0z_Hum014BuZKVFq2-_RN0YXEoKNbJChco7eiCG6dOWbZgtNGK_PSF3cMlQNdQwnDEk07GQLbP7OW2jrt4KUqYulkJkVXOY28QJ5iTBTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از هلیا و توله‌هایش در پناهگاه میاندشت خراسا‌ن‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/460996" target="_blank">📅 23:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBfjP2mFYqDO483YeI7DO1saLSXOfJnHYJnS8HA9E62gQEEGhFcw4TW0iRof7-KWUkxvqgqBooQo0LwUFW7g_IxBMBz2IJ_Fwlhnx4682nrJLJZ29-hVw0tZLLyIqZpZM84qs3g3e8F22HCjs6FMoF-WfbNb2vnetFWA_Ac1Vl89fgIdFVKWwOpzIVQCe1MnH5_3pLaJbUctqHG7waMP7nGCCC1MbC1vGy-7T8wcrKplBY2cZkfx19IFcdZ-Yrk0wmH32SGlfXeitMHo1KSz9xFFDW2WEnw3CdBGpSNOnPibJE8Cp6PPm5yc5SNs38XzPJoQzblQ1Hf0lcMswXZmiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کاریکاتور کنایه آمیز کمال شرف درپی حملات یمن به تأسیسات نفتی سعودی
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/460995" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5901e88f9.mp4?token=TzjhsueIKJDK8KWSmzb03XggoW0eK_oPghfiNytyOs6TQ42JrennE5Y4brefsuMrJYIXLDkqrOjuFIJOivSFIT5BhRwog9ywumUx_egqEIpiAdJQfkG8j8t_B1wyBHXBC4rTvkFelAUFgCHhrOpxd742iCpYMjaJk0ktLlQhwGsiE_gmC9tpc7aVQc8JT-niYwy1-dLyS1O4-iGGqs-BTeEeywi8d9Oss8a4-N3-EveS4RqkzVwHFGEllXqWw_vQiN3_lUTO0qH4FqiLY_e8rhYnbEK3U76X8FM6mtuyeWcm4Vv5vdsiU5_ruBCpLYHkGDl00X0MMgF1BYf0EfwFuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5901e88f9.mp4?token=TzjhsueIKJDK8KWSmzb03XggoW0eK_oPghfiNytyOs6TQ42JrennE5Y4brefsuMrJYIXLDkqrOjuFIJOivSFIT5BhRwog9ywumUx_egqEIpiAdJQfkG8j8t_B1wyBHXBC4rTvkFelAUFgCHhrOpxd742iCpYMjaJk0ktLlQhwGsiE_gmC9tpc7aVQc8JT-niYwy1-dLyS1O4-iGGqs-BTeEeywi8d9Oss8a4-N3-EveS4RqkzVwHFGEllXqWw_vQiN3_lUTO0qH4FqiLY_e8rhYnbEK3U76X8FM6mtuyeWcm4Vv5vdsiU5_ruBCpLYHkGDl00X0MMgF1BYf0EfwFuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۹۲؛ ادامه پرشور قرار عاشقی گنابادی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/460994" target="_blank">📅 22:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP_O2weK0_UONOpBB6FIy_kxeS8tIgXHU4kPYydTD_GGJ4c-N1Yfv-2hIFOwC8_zruYYoli5EYm5WsILJtcBAZsc0b3Ha7bzhrWk3bx48sqIjeWJfBbBQSQVu9YdtXM1zEGuIWIhq7lml0RKqAx8PWBGLA5lLL7DILVmtcXToaMOFXSP8C5Os6Htr7wTs9xakVSoNA3SeJyKKO-7XT6z4MvK0KDKWNjjX5maNZ-IvSa0h1Ha2H2wSMomB5S4rO3RtpdHv3OeJuM6duCbz8ue1WgAryqs-Oyw_CGboO1mHheYDXzDJej4Yv5ILKYr8nwyV2ixEZbiglTjMFBNj_lokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی امید راهی بازی‌های آسیایی ناگویا شد
⚽️
از میان ۲۳ بازیکنی که عبدی، سرمربی تیم امید از آن‌ها دعوت کرده فعلا تنها ۱۵ بازیکن در کنار تیم حضور دارند.
🔸
استقلال و تراکتور فعلا از تحویل بازیکن به تیم ملی امید خودداری کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/460993" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7X5BOh9txVnGB3HSgD8geDfK9sd6jjc2HaPJIrKWnvFUPZBuWjfSXyEAkJ9s09jvtWcugUzL7vc7UMyAHhbBqO7HeKP9LSPIGKj_ZKpgLXf_L-6xSR8ivENrtfe045wpYWuDOoG_sy9Sh_1Ycg8aH7xvGWNDpMTb7E2L4jjuadV87ub56TUAK7rpwuE8UaxcNLwPkQSbqFmUUsDQvZFVYacz8vnQUD9oOUWwCJ5AgLK51-QecJ2JKfHc_mB0cS7rnwblWrb9T8WWCBj6gYNJxhWKdE_FtsxS6jhf-5AI_t5vwouUHhQ7bXCC0AxqIBU6bMfwbesZeLlV_Xm3dUDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: هیچ فناوری پیشرفته‌ای توان عبور از رصد ما در تنگه هرمز را ندارد
🔹
سردار محبی: شکار سحرگاهی پیشرفته‌ترین زیردریایی بدون‌سرنشین ۲۰۲۵ ارتش آمریکا یعنی هیچ فناوری پیشرفته‌ای توان عبور از لایه‌های رصدی ما در تنگه هرمز را ندارد.
🔹
آقایی بر خلیج‌فارس، متعلق به جوانان فناور ماست؛ به خلیج خوک‌ها بازگردید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460992" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
صدای ۲ انفجار در اطراف جزیرۀ خارگ شنیده شد
🔹
لحظاتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد.
🔹
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدوده خلیج فارس به گوش رسیده اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/460991" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drVFMYh-tuendh_UUlMem_4QaRs6KKrnkA460qzrjz9aLJpYPbCNc_o4UY-T5C1kq-K1fWYzlVdlwNtQp18fWqpMWKj_y_7R2vfZKUeMFMadz2KeKFi_BFAVa2OaZp5GRsJCiyM4MTm32QRY0jspVcS6ORJi0H8O0sjM-u6dMSGDkukSoU7N0DBWzSYd8S1TmtlWFIgfvj1quItrErdL6L8AMknca0Hzqh4oHTqllj7sV0Y1xgURASCCDFHXjYxfJt2sGA8sYNns8BZJINxIWUIV0qkVMLBnFCBZcr81HiRmACpCuFKqfxNHnXwXk2ztYXV6LuvpiuC2zlR2z69pOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح: هرگونه تعرض به نفتکش‌های ایران موجب هدف قرار گرفتن پایگاه های آمریکا در منطقه خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460990" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
صدای ۲ انفجار در اطراف جزیرۀ خارگ شنیده شد
🔹
لحظاتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد.
🔹
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدوده خلیج فارس به گوش رسیده اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460989" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
هشدار ایران دربارۀ تهدید نفتکش‌های ایرانی
🔸
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش آمریکا تهدید کرده است که ۳ نفتکش ایرانی را هدف قرار خواهد داد.
🔸
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا در منطقه را به‌شدت هدف قرار خواهند داد
.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/460987" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1wBOJqRVrLZ3qeswkfc5Cdqslviuz5Mjbb6toJgLlU5hR4wX6vZlp0iAtlc4yazGKCoaY2G6mSdX9phlu7y7i4fgS5rKaHo4kVn1rpfNWPNOTHSC4vSvnIDtBWAzHjn3nbaxNpIkYq3bez37kcyW_C5rO0h7p31FG1iietB7lYbiYoNnww7DQsTOefEFMrqYcpG3b9Up1apfG7t615JGpr8qYrz0nLck7-m6cLmkrX3PkiA5cJ_a7WzMcWh0NgW9KST_v830s8wCnwxCPWOlPc_SdgAwva6JvtF2_lAlsr7scI52a-_yMNE8MlsV68prr6lgT2vPsK6tdQKg4-NtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: رئیس‌جمهور برای شرکت در اجلاس بریکس جمعه یا شنبه به هند سفر می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460986" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvxm6Ie9T7JSc9TbE9PXCFASDGkaG-OqcvyUMNM9A1k9poY1zx3bdKGylJEFSsT5ml412VNHKD2ku6NpuOtLKdn95xjSOZX6BMBu6DWDk8_Z48EYAMwYmrLNzj7QHuV7wUsVSvLTVhz-38B75CCNRMCH4wOztoRIMdry4PRUl49noy8quqctRAK9CWKJfCO3iIDGBTWmK04iwulxNsca5ymeMEjwELoBdhrCoYzEqhTEmK22C7pU_jVXcc9BHRLvOTunTHJeswkC_xxQQcnU1shUgHY0fd8_bvkFlgOn5zFMr2e-3AalYoaWG7q69vscBrdPEwKz0qmTQPQBt7YPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTmpAd7zO5Pe3NuQbW7jipI39XB1sAQ4IaSj3lQ6yvYOq0UjSUVQC408m6c5HqQK3XMIcNePNfTDuK2c7nsCPN9Hv3kgEvmKNDIinyqfCY82BSH2AaFAG6Ww0-TeTSn8LERCNzQaKEANt7R4ks78eWCj3k37bRUkYpUlOKiq84iNc90HFN2W5q1VMTQPxmTWlTOFZaU0Km2Gjmtw0F0RaDakm_fnrgO5zWEJcztZfB3yogqpV8scMRzv_rLmmvgxl6HDtgfuesZkw3TmYEQQjVoxWFhkmHeTXiXe4foxGQi7_8i4c1Xi6WeF4tgcAIHiLeqTefOVPA-TvE_5K2J2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFh2LbhuFDMoQHvKRqaCL7jZ0N-OKmTf7nQSRMobzA47aTdb17PYeVAJhmj9j-aSAHvD-D1vWr381vj3OSLTgG_uUsk8GW9vy1iM3NXvA-ZQcOd1kXc61zT9wFksC38iqRe5YvmxMWOxatG6luJUaO3f34CIqZLvuCE30q85tCZLjGOXHuLx7zjS7DiXZ_l4cFGLDHW4YfagGm9pcyhCqUhWwunUFPG50Zv9ed5OIXn7JTEA4cOe-mDm-3eTWpcji0rswhXURMZblpCH7wzjD7QulPPIgcJirQBRuUv9kV2Qs3XiBl4cA_JDmI19ANexlEoIqudRG8Ar6wzv2CcPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXly8LXisft1VSlLGJi0eEtdXn1LDzZyPzHA_fi_fYmdJ9FrkdVbWuY8iYo2O1-IapNE6wv7v6COdmSfcbxhsW7ffS7LtpOogImxXIDI1PQEVFdL3zKfmutKs2rnzK7zf-P1HA0RMKBlM0X2Fv1vlQHSomQumD9_dkHQKNyVJFg1rPL4QjJ1e37OO8-IXats9NMtBlwRR7PDaAyaxAN-w554rouu6bOEyXFF26ooqG1loNxuQU5YGm1kz2dWHAh8_84EV0C02a0nw4K72ILug2fV4gd1_hAl_GtT8t04ok_ab_UqYRrdZOkI8NhRw5XpeRLuLDdW4tWvEd4VVJYQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GO_WcTguu9337bhPQKf3puT7bRusp8eXkD_skWktQtj7z3nxL6ab0DJqqHGuenauA6fIjWRoTotm5tQobenEugpZqoorz5ohsGC0zgLFPKcUdSb0ojkAsVKHvptl_6IU3FFiEwATlki7wLbEXDAXXtco91EjUQ5BdQv0FFCzZsmc3PkDzjTy8FMn0lXFLhpvV8m9ZXv3BHPzt5mr6j797Jrm7B8LIrtLb5kVfyHY2gXKNJvefC7kwX9-BU_5Jp3h_cXhYS1M8j3Gz-Xr64qeM7v-V-k-5QnQJy-rgQZUJGwMVS3ygyQRjvGMgxl101_LEb0jUfkVCuvGKxfGXNFH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awzblc2T2Rn8ajXuxuYd2M20ZVW30PO-mlJfOLRCUpxQ1DN0u40BbYRuQOPOjvzLJQ4NhhOxDbCIYQjDNxd_8F2e8SDXQqWKAjnoIir81CE0iW3T9Ie4s2WvFrH2mcq4c4z3sp2NWPDcIlpB_7LR4ja1YFKiiaKsl3morPwkBoYVa4iYMGcNQxLxGmRffN49K7gZd0XNtwfCLcg1x1nQ0uPl1-2eUt3xvV_Vkooi6TW4Ohq9RHKun08ItDxrybpR3jSfbYVrwHoNneTphvREnYS8j6pVfW2O0DwQfIR4XhEEWUKiB4vOQns7RGFWZAy4QTSibd744LgG-1a1kUt0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8VFrciRaKy56gtZOSvWc4DL7uZXb7Syhw04nlo3gNHQWQD9dtF7Pzwlj9HdBnOAbuAD_j5ueVu4qJHdSukRqH85FiZ7kKNL-1ijryhQllEy-DtK4_ndRYDUlCs11r-FeD5yKwNOBFLrccCmFNdb6RQIEUcJdSnH6Vl19FT68-HcVpud1gpdv1elG6F3--3hX2MGfcw03S19BYNG4DMnmAjf_6O-Bis5aPWQYqo-3lE_XWyY_1LhjGhzhnJpOyKvbBI5rST8monV7xnGxfhxgsmgIBqWyLyKScPhHqvJV7F3kru8raESR0yZVvTY9Izrz4S0g4L-5hEnakGGRPqbLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر معاون اول رئیس‌جمهور به قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/460979" target="_blank">📅 22:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYW_d0WiF_xAWnFpOgXk4x9nfek8a1x4DRpd9IgPXUEsxYdlK-r7GbIJdrJd1ywAvd4Fhl8Gbm7Uslr2fhrKvQ2wfGEjgAl6Hcx4SIidX09VKOOSHc-WV5cdcGzMCEhHZQCCiRlh2W2XPj9zGAPe3XUaPslfh2CaApoqODq8JA7PcZvx9G6Jtmqpi7bDAZmeo-P-esgWoya03cGV6dLGEN0qoqTKXsJi5W14OZ8xe2b5Qhd5Nvl8_H6cMIKYBjcV258oavDSZR593fCwhweOjMjGAhJi8A5iPD4klYy9WOPHY93MijgTQHlyE6wBIZM2BgN8gSslVL4BF9l-fs3D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: برنامهٔ زیردریایی‌های هوشمند آمریکا ناک‌اوت شد!
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460978" target="_blank">📅 22:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460977" target="_blank">📅 22:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANDrHocv_aHMbAWdkAaA9CI43YcdUHmJ1SuDeC8dFUCgRcKx2Qv6wFu-6xyQ0PrtHOG3BtoE7unSUAOw-85561hhdoj1J8ept0oUz3UJIlUBVBJW4TEP1wZpUl6Hz-ef-w9ZKkNp-rKURckhyKRJJNsA5ALJghf4EEbrOSruOwLZ2XZh_6AC60uRacZmEFr_QhcAsN0V5O3RZv7H_0UuwzSEiYBQdNPVaHTN8RyAtOBvuZ89uYqg04Ew-tAd9OdWnX7P7XhN5Sb9JGi6UgbalyBvSwCTqwRRTnXjdLepIZGiLB_Wy_1fBwPuRbSjhGX0y9ziOHdPaVSTFreNsKXkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان صریح امارات به هماهنگی‌های امنیتی با صهیونیست‌ها
🔹
وزارت خارجه امارات در واکنش به گزارش‌ها درباره هشدار ابوظبی به رژیم صهیونیستی پیش از آغاز عملیات طوفان الاقصی، ضمن عدم تکذیب این گزارش‌ها، با افتخار از تبادل اطلاعات امنیتی با این رژیم سخن گفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460976" target="_blank">📅 22:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAqB1zwJ29a__B9xLoD_Xbqq7RuVfPPrSVMzh-ulA4EQr0-sVEDB4FHO5v07yueOCVW9AdPUvMLZ368VfRFI2f0ptNS4NE-QKgu1olkUi3UHx83b98vYXu9d-bs0Asn38e8Rt08MYH8MpfIjNADoy3IfAEl7tawplz_wNDxO38nJweo4s4N9oPTqgqfum8tiaWN720w3rZHKvZHS3Y6WXWfqr3gGqzgFgO2PKramLGrb6FTRtB05_XarKiAgumrULE58Mr_9c1ObDEc0iocbewYZ3T6c0cpgvhiZesMoBscqO0smlFB2mWMcH72u1YPhMKaw5T4TtwmnKAfZTFYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایۀ عراقچی به «راه‌حل خلاقانه» آمریکا پس از ۴۷ سال تحریم: جدی می‌فرمایید؟
🔹
وزیر خارجه در شبکۀ ایکس نوشت: پس از ۴۷ سال تحریم، آمریکا به نیابت از اسرائیل وارد جنگ با ایران شد؛ جنگی که پیامدهای فاجعه‌باری برای آمریکا، از جمله برای جایگاه و اعتبار این کشور در جهان، به همراه داشته است.
🔹
پس از آنکه واشنگتن نتوانست با تحریم یا جنگ به اهداف خود دست یابد، راه‌حل ابتکاری‌اش این است: تحریم‌های بیشتر! جدی می‌فرمایید؟!
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460974" target="_blank">📅 21:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۸.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/460973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۷.pdf</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460973" target="_blank">📅 21:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569380b929.mp4?token=XK3QqAAJSz9c4dhqJyugPZ5XL68NNjqZsyUIrRsAlqqisUs_eu_qQkdw0gvvRYyAcCnvbDrEoHyp0m_DmWtnWQaZ_W3K1IKmA2pOFyOl2urUphT-ZdDgSqSKl0X0JsbvcyRmWC7eH-DU7YtlXLTssXcBmCTipyLBiGqEuaEMgbxHBESLM-fIUKPKpazX_AhPBWgD7IrveVW9ejObcAJYleczEmUPNAoXMoAwADnlCpHWdD4rPPa5sXbrxvLZ9Qc7s5vwOQx8DKDxUdQ7UYyXNdg1AHrgS8A9OYTkJmLJhvjKuClBA5s4cY1Y-GwrKHju-Q6Qj1dRYLz5Fe462XBygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569380b929.mp4?token=XK3QqAAJSz9c4dhqJyugPZ5XL68NNjqZsyUIrRsAlqqisUs_eu_qQkdw0gvvRYyAcCnvbDrEoHyp0m_DmWtnWQaZ_W3K1IKmA2pOFyOl2urUphT-ZdDgSqSKl0X0JsbvcyRmWC7eH-DU7YtlXLTssXcBmCTipyLBiGqEuaEMgbxHBESLM-fIUKPKpazX_AhPBWgD7IrveVW9ejObcAJYleczEmUPNAoXMoAwADnlCpHWdD4rPPa5sXbrxvLZ9Qc7s5vwOQx8DKDxUdQ7UYyXNdg1AHrgS8A9OYTkJmLJhvjKuClBA5s4cY1Y-GwrKHju-Q6Qj1dRYLz5Fe462XBygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم شهرکرد در شب ۱۹۲ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460972" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgMPl5puFFMiwKGK3weRufdI7n6Fh4NlZ1FIT4HrNufnTullEifCoahFOJPLYJBCI3IGzb2CJs592pEW2gxkc7v1h0hNaDcRpsEtppoap8EL-nWot68c4xd69WN91eAPCsk-eeYnnwJcOu9u3n2r3DoC4G6uMBS9dEoD7Q4YuQBN04_kG4KIRiDvW8K5F36kBm1OWgHJGNweixJ1NlHHdH4srsbbVdDq-M_98fibcpkK4wYaITaiPZvPj-l_IMHQ_QOnZEbyNtCr9rwXENGcjarD498OC83EHx3wpS77yidsv7M1rcUQk73d-yApzuxKo96Gxsp6NWzFlHI7a0Aw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pavNF07uhBM8E1oOmYwVMQDXPrnzHpW79leDW6hL1k55jRCZaPN7s20gr4a2wWpslQPanz44OX4ChRJdeYX1rr-DvOVW9gkuUUuBv8atpDynjU7TJm2nGjtYXma0EDhIaKP9qnDIkd4Vmp9eYMQ-aGViG-YeaZIWCdm68EMap5RyO8ogHB8cLcDOHGw9HoACuwN6DrbdkZ1UzwLYmg6A5XI_GTBt_1f_zu_iSPdbAkDvVo2ZNbgUQNBxhll0qMPSmzLUcUAyMbSMRbdGESKp0iTzKsfT2mD8vde7_JeYwNKw39TqqJ9fz9ne_nWG1JV5QaXhHa8nElhSh63tH1Q6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3EvANbLfVXJIok32EmdPm3JkanqF5ESg-PVxyYdWJv9bULBe9a62MUkJn5x1UqWpWKmHF0KJtSrEzmwuZAgUa7LH5hklPlkvW3q9DBxy9z_PcAoroQy0xlGLH6lzROzEkkhjTh72tcBjZYh0roGacQVDbcTFH91XUDkt3hqu5oZtBUPavSpOc5mbv74NtHNXi8h3qu0WxKL3WjBDg2miaHiFSowvPiqscu-lnD7epnkFRdGa3KyhHLrcCgfixT2nCU6jWu3WArZrAUWfqAFSgcPRNawxekkTpsdyBGGO6g6pnQ7ZDhIfVPEZqMJqBycDeimUZwFt-DOYWNWEzpapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsAbDJGeiuPInwK8A20vlbw6H3Z0VBZtTXgsqkEvEhs33yRVMFxCQKmlHiqfSt2ElyE4uKSnQR5HCoBSuvYXa9euznlObAyyafY9341J-O8k3izksQfyAIQlwDyk07pOfAcFCrNvsPoz-FBlgD23CYhZ8Xs0DeJVphLh3aYK0o4gILfBa_ke09bxLWuD10G4VWdo0Nta3XHkYqh4oYG8Fw9SwgfcuDgAIrL1cSYOAfo8aCkKwB_Ewcct_sfIwglcobM1fiftVkHegoVKK14_QzV4ZkRYSz5eiGGOWiB6_BdJJgOo4gYaTFruW6ajKBXqEH5Cvz8Rs-1bEIXAkh96qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzJ9_SH0Q9o5zKYHol23QKf1zLfCc0EA5L4mPPLkK2FaexjVPSP4YcMMHgQ8fcuEgVyhygq8kJ8PQr25QURPByZyDBnaBh2sXklgTDHuPNWqfjUoqULJ6B75wZn7zkCnLiMPEU3RsYZjpUDyq2sPbNKsNbY_NKsHFnzPOeVGGqF8siksfg6z7QEqHnKxt0ujvEBGBO_ECMoolKcVfNBJV_8eeknZW1kI-HcODkpLmmDsKkdk2QUVvMwI5fp-czbvEQIGIl9ADengi_R19HuyXDHT6KawgpulU6ht3m_0EADrWQgcCOlKDB3zVbCkqU4-IvoZfA6ClFn1L8soBmzXPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbK8yt-u6iFIUe6hfg-yRaNaifROdVKw6VCfk-5Zdw_PPg4CmPj6DCqpljnRF_dn7w_E2fy1AUwAMTMKmmJ-yhw8BvRyL5T4HiliYk3Mmajc3va9sPq7cdUHP75lmI_BmKYpNyGcNDxTi4LxXxZ7qmeBX1aDYbUghfvyRGHjVzpT0nvjJpflyqU-yQh1s-EP_qf_maBMu4t-9qCvFjTDqS0rWmJurDfexBDigmNmKMauLq5AwovcX9Grls0ANKZdystR4ZA_2Nw2hcgxI2cD0L_2s2JuCTuuCVCB-n1UTDddbCfq0j3jgvh3rv4SxcuObjPRzjNlGaeSkkfXjuAKag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اولین تصاویر از زیرسطحی غنیمت‌گرفته‌شدۀ آمریکایی در تنگۀ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460966" target="_blank">📅 21:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f351d7a56.mp4?token=G8bCNlyJkBtdXxX419EmWzLpEdE6JlbHPTj6kZA6QISf7nu49OjVAI02EubTNFLK4-dVs2t6vEgFwFKKvRRUIXF2yNMuW57CDUxCCIQ5cMfsYQW5Hmjn34UFUHHpBkcGuv_QMqtwY5-mwgwL39xi2x1X2RWuUYxenmPaXna1mK8EJQ35BdxG6NVnTzJgMg3sM9Pl2641OWQOiJlcfUMe7juy7yEH6aGUNG86y9a9LyJzXnxiWCszlC6Cay4xXJVREKKLSwN5XrkGAziVkYEMAb1mk7AZYA5dPilXmsbzILXKPjXhDSMEOy2V7VpxiXqLWKJrGdojQoNQjYM2M0Nflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f351d7a56.mp4?token=G8bCNlyJkBtdXxX419EmWzLpEdE6JlbHPTj6kZA6QISf7nu49OjVAI02EubTNFLK4-dVs2t6vEgFwFKKvRRUIXF2yNMuW57CDUxCCIQ5cMfsYQW5Hmjn34UFUHHpBkcGuv_QMqtwY5-mwgwL39xi2x1X2RWuUYxenmPaXna1mK8EJQ35BdxG6NVnTzJgMg3sM9Pl2641OWQOiJlcfUMe7juy7yEH6aGUNG86y9a9LyJzXnxiWCszlC6Cay4xXJVREKKLSwN5XrkGAziVkYEMAb1mk7AZYA5dPilXmsbzILXKPjXhDSMEOy2V7VpxiXqLWKJrGdojQoNQjYM2M0Nflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار جدید سپاه را بشناسید
🔹
زهپاد Dive‑LD یک وسیلۀ زیرسطحی خودکار بزرگ یا Large-Displacement AUV است.
🔹
این زیردریایی حدود ۵٫۸ متر طول و نزدیک به ۳ تن وزن دارد و برای انجام مستقل مأموریت‌های طولانی در آب‌های عمیق طراحی شده است.
🔹
این زیردریایی هوشمند می‌تواند…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460965" target="_blank">📅 21:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=OfreUamycP4Ma2x2d4CCVMgC3nAfuImZ6clgspGVOpCMkTwEPdFfdS-gAjgC6_BSTWpBUcUGm5VTuJ0wLidzzPF8HVOF435f9b6H4VGpvl3lVu6dwJah-SdvwMjSHZTmIhSnweTRM4W1j58tzsuQL8nTFnPM91tpiBZ7Vhfu9tuShqkqfdtaVUELMva64tzQSPluifP0UO8X_VZ0NzWB8Gys-IpNsVKj9J5vCeew3ZCgPDMzRJMoeiyoA7JLpcSUg7BlW8SWReWNlGtUAb-sqZWL6n_59QIvLTkVQa6s0tbbDtYSQk1-Z6iIbUGdfzkv1kDYNgNXL0uzoUpdtslRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=OfreUamycP4Ma2x2d4CCVMgC3nAfuImZ6clgspGVOpCMkTwEPdFfdS-gAjgC6_BSTWpBUcUGm5VTuJ0wLidzzPF8HVOF435f9b6H4VGpvl3lVu6dwJah-SdvwMjSHZTmIhSnweTRM4W1j58tzsuQL8nTFnPM91tpiBZ7Vhfu9tuShqkqfdtaVUELMva64tzQSPluifP0UO8X_VZ0NzWB8Gys-IpNsVKj9J5vCeew3ZCgPDMzRJMoeiyoA7JLpcSUg7BlW8SWReWNlGtUAb-sqZWL6n_59QIvLTkVQa6s0tbbDtYSQk1-Z6iIbUGdfzkv1kDYNgNXL0uzoUpdtslRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات عرضه اولیه اوراق سلف موازی استاندارد سکه
🔹
عرضه اولیه اوراق سلف موازی استاندارد سکه بانک مرکزی با نماد «عسکه ۲» از ۱۸ شهریور در بورس کالا انجام می‌شود. این عرضه شامل معادل ۱۰۰ هزار قطعه سکه تمام بهار آزادی در قالب ۱۰۰ میلیون ورقه است و به روش حراج تک‌قیمتی انجام خواهد شد.
🔹
دامنه نوسان روز عرضه ۵ درصد و دامنه نوسان معاملات ثانویه ۱۰ درصد است. معاملات ثانویه نیز از ۲۱ شهریور تا ۱۸ آذر ادامه خواهد داشت. خریداران می‌توانند با کد بورسی در این عرضه مشارکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460964" target="_blank">📅 21:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
العربیه: اسرائیل در ۲ حملۀ هوایی، مجددا منطقۀ نبطیه‌فوقا در جنوب لبنان را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460963" target="_blank">📅 21:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRSa0rbGbRyzzVm9-GDvMcvNOFNARFpgkboFG0hc1kMfGyZnEKQ5WkSc6X5-xLVYO9Fba3p7CQREtl4U3T1XJv4vWwuzPNGjwfShWCURof_Ri7lfwn9wfPexSrXeDoSKh7TR8VdtmILc7qpVaREJaLu5Q4ZIitXGSdLCEkPaSs_gqbPZpz-CSmAWLYjLidhSFtsOE0Iodc0D0nsWA3Dr_wMSr5EgLn0KoTijPT0GUlKaj_K1gQ9n79AtqoFKIt-Ghppg7fbL3STzI5-q6si_83_5kxC-XKVTt--RAo9tDzArwEnwKQXstZ8i-jPjp6SEhZyqLlAL9jb9xds0Luz3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت کندی اینترنت در ساعات گذشته
🔹
مدیرعامل شرکت ارتباطات زیرساخت، علت کندی و اختلال اینترنت در چند ساعت گذشته را «قطع فیبر نوری در ارمنستان» اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460962" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تحریم انگلیس و فرانسه علیه رژیم صهیونیستی
🔹
وزرای خارجه ۱۲ کشور غربی با صدور بیانیه‌ای مشترک اعمال محدودیت‌های تجاری بر کالاهای تولیدشده در شهرک‌های غیرقانونی اسرائیل در کرانهٔ باختری را اعلام کردند.
🔹
این کشورها شامل انگلیس، کانادا، فرانسه، دانمارک، فنلاند، ایسلند، ایرلند، نروژ، لهستان، پرتغال، اسپانیا و سوئد هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460961" target="_blank">📅 21:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎥
مردم به امر رهبر خود همچنان در میدان حاضر هستند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460960" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s95O_T_a7ecnW53_YveZT8gqAQ4iLVFTZtYKuM_ErwWr_Vbjv0VdjEQWwtnyHmbR2SzMQEWFlF0JVVItRL7FfOGSksT4-B3ga-vezjMqZPBTnYJ2Z--OWvUq-NuquGOM88ZT3n9CMDqzu9ejw6NyZiX8iv-CS7xNGL-yDPM_uiodXN0fJll-_ecC-7sGjUePn4_dE7JfP8PigXimON2hUsrGo9ekvHKinK5H6TTdNwy9fw0lDj5F97LMUfpcTnwcloLEmsfzrzmzcFLeo8T_F0kMiruXBLAqgBOg5xd_BKqWnDS3bRpT8_3YDJLtMAhgSjD2smgEgHgiwcyqJh-n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلوف ونزوئلایی ترامپ مضحکه شد
🔹
کاربران مجازی با انتشار کلیپی برنامهٔ ذخیره‌سازی آمریکا با نفت ونزوئلا را نشدنی و وقت تلف‌کردن عنوان کردند.
🔹
برخلاف برنامهٔ ادعایی ترامپ مبنی‌بر پرکردن ذخایر آمریکا با نفت ونزوئلا، کارشناسان می‌گویند ذخایر استراتژیک ایالات…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460959" target="_blank">📅 21:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c071e6554.mp4?token=aTBwUQ0VsHGsjLePFq6TCf1fmWAJGagvG8UoqRSl_78-94luWnut2PRLtrSPZtoq-5zC9DCCCOWzCudDx3P41XLxAzATYnQRPzhobcoZ01RrYI2UWwswOxM9qxAUPlCCT0jyyvxD73vlMfqoRGwNe32qCO7qr9SzNKfsHznbZzmxElQ2RehZXSIaNymrKWqWLy0HqP6Xbre9QQ9t8JYR-YZiUKNvQ3XJA6JUxu2LKk3JefLWs-4tM2Doekgk6_POz0HemkwXcoT4nHQZ0mHQ5cN19TFKYqgV6dTDmQD_ohZc1ZkJh1DmVIMGhOPvjsLoRlM4e04c8AetXyotNQODHr3IcCMj_CqKUBHVCrzA46PFBrPbRWMgc5FEzBNtiYrgHMCmD4kspn-CzDp3zfHPTx5Z0jzNNkFOyauissJSRBZ4DybAVrMKQWyHnYD3SkFnpIuacYj95BMpfVscuCxWKtPbEolZ6DuUWEYGpZSIsAIFXl9PboEGk_kiFLlVzDYS2dbkCeuhr2rpQUBhbThahY6VrRCUdBRJTpBmGbGWThJFRfjJbjfxbequ3UUzaN4TS-kvxaO4iCrOUq_aqqhOySNXm0BaAQAmJWtmpyw5HdtBQPYXLf11GD7-BDX0yTvtnqSonCiOeCNiULkuVxHUkjmDUsQ5ypWwNAyf1FStPZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c071e6554.mp4?token=aTBwUQ0VsHGsjLePFq6TCf1fmWAJGagvG8UoqRSl_78-94luWnut2PRLtrSPZtoq-5zC9DCCCOWzCudDx3P41XLxAzATYnQRPzhobcoZ01RrYI2UWwswOxM9qxAUPlCCT0jyyvxD73vlMfqoRGwNe32qCO7qr9SzNKfsHznbZzmxElQ2RehZXSIaNymrKWqWLy0HqP6Xbre9QQ9t8JYR-YZiUKNvQ3XJA6JUxu2LKk3JefLWs-4tM2Doekgk6_POz0HemkwXcoT4nHQZ0mHQ5cN19TFKYqgV6dTDmQD_ohZc1ZkJh1DmVIMGhOPvjsLoRlM4e04c8AetXyotNQODHr3IcCMj_CqKUBHVCrzA46PFBrPbRWMgc5FEzBNtiYrgHMCmD4kspn-CzDp3zfHPTx5Z0jzNNkFOyauissJSRBZ4DybAVrMKQWyHnYD3SkFnpIuacYj95BMpfVscuCxWKtPbEolZ6DuUWEYGpZSIsAIFXl9PboEGk_kiFLlVzDYS2dbkCeuhr2rpQUBhbThahY6VrRCUdBRJTpBmGbGWThJFRfjJbjfxbequ3UUzaN4TS-kvxaO4iCrOUq_aqqhOySNXm0BaAQAmJWtmpyw5HdtBQPYXLf11GD7-BDX0yTvtnqSonCiOeCNiULkuVxHUkjmDUsQ5ypWwNAyf1FStPZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال زودهنگام شمال کشور از پاییز و دردسرهایی که به‌وجود آمد
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/460958" target="_blank">📅 20:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR6kkqFHVNErF56mPwccP2zST1Zf0K5j5Ykfv4qLMxbJirtltqYsoetJO1RTT8XKbYlMaKT3RRy6s8uhESlxQ7os4MDwkUQcjm0zA9__tgc9W10jEL5EpMhkuPC1rvKHv3_ZR4W-XZda7-HJhIUSagM59Zt3X31Ku0pSYLnut0hXMIMBMJmpzdCwVz8AEa-fLwlr-_hJJLbWQSTcbRvgim2OJfTtuF9fvwjwuwYyqO0WzrLX7gWYKAhDpuZILws7QSQi4L-luPstJLl4zFcumllwsqkQR1IDjzwAw2QhNTiw4s7eiSgr_3wBPCL2QMTGbxtz5gS59qH8h6IR-8t_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی ریاست جمهوری : دوران صرفا «شرکت‌سازی» تمام شد؛ فناوری باید به بازار و ثروت برسد
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست شورای اقتصاد دانش‌بنیان خراسان شمالی
از تغییر رویکرد معاونت علمی در حمایت از زیست‌بوم دانش‌بنیان خبر داد.
🔹
او تأکید کرد حمایت‌ها دیگر صرفاً بر افزایش تعداد شرکت‌ها و توسعه کمی متمرکز نیست و باید به سمت
شکل‌گیری زنجیره‌های ارزش و بازارسازی برای فناوری
حرکت کند.
🔹
به گفته افشین، ظرفیت‌های علمی و صنعتی باید از مرحله پژوهش و فناوری عبور کرده و به
تولید، صادرات و خلق ثروت
منجر شوند.
🔹
در این رویکرد، اتصال
شرکت‌های دانش‌بنیان به دانشگاه، صنایع بزرگ، بخش خصوصی و بازار
برای رشد شرکت‌ها و بالابردن سقف اقتصاد دانش‌بنیان کشور در اولویت قرار دارد.
🔹
پیام معاون علمی روشن است:
زیست‌بوم دانش‌بنیان با تعداد شرکت‌ها بزرگ نمی‌شود؛ با رشد شرکت‌ها، ساخت زنجیره ارزش و تبدیل فناوری به بازار و ثروت بزرگ می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/460957" target="_blank">📅 20:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEYwMdggIm3Hmx8Q-B3BlPrvuymPmwTMhvS__XlZYPzNgz1oV_abyQNEFJHehiE5OYQ2jVhH0KWvGr3CG7TOzqJfTHxJa9gRJc8x0kgCTl3jbhi0GAF83y4vd52w6eStvA488i47d2e5yu6rurZn1nmzjbK1YDzXVs2XiuFsTVQXEQtZJFYU_k59oeA-1o38-EynEgGOBXwDRC9QH_opunTZ1lZj9BaHpKrmXHgAsgu_JG2jcvCVu0aIEREXhekYfpsjmPVHqPCaGIYjgWmevr6ZUfC14b4sSN-YBaPmPR8qEAY5zoq3APIv97VkrzYSFmSBZNV9Ysue5rYOZTC_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میدانی بیمه معلم در مناطق سیل‌زده
مازندران آغاز فوری ارزیابی خسارت و تسریع در پرداخت به سیل‌زده‌گان
🔹
در پی وقوع بارش‌های شدید و  طوفان‌های پیاپی و جاری‌شدن سیلاب در بخش‌هایی از استان مازندران، بیمه معلم ضمن ابراز همدردی عمیق با هم‌وطنان و آسیب‌دیدگان این حادثه، بلافاصله تیم‌های تخصصی ارزیابی خسارت خود را برای رسیدگی فوری به وضعیت بیمه‌گزاران به کانون‌های آسیب‌دیده اعزام کرد.
🔹
به گزارش روابط‌عمومی بیمه معلم، به‌دنبال ورود سامانه بارشی ناپایدار و وقوع طوفان‌ها و سیلاب‌های اخیر که منجر به آب‌گرفتگی معابر و خسارت به برخی از منازل مسکونی، واحدهای تجاری، مراکز آموزشی و زیرساخت‌های منطقه شد، بیمه معلم به‌عنوان بیمه‌گر پیشرو و حامی جامعه فرهنگیان و عموم شهروندان، با تشکیل فوری ستاد مدیریت بحران، اقدامات ویژه‌ای را جهت حمایت همه‌جانبه از آسیب‌دیدگان آغاز کرده است.
🔹
بر اساس این گزارش، با ابلاغ دستور ویژه مدیرعامل بیمه معلم به سرپرست استان مازندران، کلیه کارشناسان و تیم‌های ارزیاب خسارت بیمه معلم به حالت آماده‌باش کامل درآمده‌اند و عملیات پایش میدانی، بازدید از اماکن خسارت‌دیده و تشکیل پرونده‌های خسارت از نخستین ساعات پس از فروکش نسبی آب با جدیت در حال انجام است.
🔹
علیرضا بزرگمهر، مدیر مجتمع ساری بیمه معلم، با تشریح آخرین وضعیت اقدامات میدانی اظهار داشت: اولویت اساسی ما در این شرایط بحرانی، ایجاد امنیت‌خاطر و ایجاد آرامش در بیمه‌گزاران است تا ارزیابی و پرداخت خسارات در کوتاه‌ترین زمان ممکن صورت پذیرد و مبالغ غرامت به حساب حادثه‌دیدگان، مدارس و مراکز تحت پوشش واریز شود.
🔹
او افزود: بیمه معلم از تمامی دارندگان بیمه‌نامه‌های این شرکت که در اثر سیل و طوفان دچار خسارت شده‌اند خواهشمند است برای تسریع در اعزام کارشناس و تشکیل پرونده با مراجعه حضوری یا ارتباط تلفنی با شعبه سرپرستی و شبکه نمایندگی‌های بیمه معلم در سراسر استان مازندران اقدام کنند.
🔹
بیمه معلم در راستای تعهدات حرفه‌ای و ایفای رسالت مسئولیت اجتماعی خود، تا برآورد نهایی، تسویه کامل خسارات و بازگشت شرایط به حالت عادی، تمام‌قد در کنار مردم شریف مازندران و جامعه معزز فرهنگیان کشور خواهد بود.
#بیمه_معلم
#ارزیابی_خسارت
#سیل_مازندران
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460956" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/460955" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b2d16efa.mp4?token=m0_Tf8tRGHHci_mhxJpOBV0UIAYuRnODdRTtmFD6gcaZ9qadUVcUgG7sRCYKL2XIkdDHd1BXzYD4w54idsflta6KyLYRMQZ2cASi9XRXi9LcwgoCO181B5DX17KtXYESdoOwN545I6DryD04yYsFp1goQnust5AprQc-u4MkvCj1P6vTQ7geNxrJmoiMXFYuxtop3fidG5vTyu2UK-mKxkHpIPXmDELIHa6zsCkpQnESE2dlMlwlppj5Y8gF25y--PbX12jnlq0nHv1P0XTaHsDlGnu4vmtjI7EaHg34vU-pKbw2e3giq046ADqrYad26o68VtPkZ1SteCZ5nxZihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b2d16efa.mp4?token=m0_Tf8tRGHHci_mhxJpOBV0UIAYuRnODdRTtmFD6gcaZ9qadUVcUgG7sRCYKL2XIkdDHd1BXzYD4w54idsflta6KyLYRMQZ2cASi9XRXi9LcwgoCO181B5DX17KtXYESdoOwN545I6DryD04yYsFp1goQnust5AprQc-u4MkvCj1P6vTQ7geNxrJmoiMXFYuxtop3fidG5vTyu2UK-mKxkHpIPXmDELIHa6zsCkpQnESE2dlMlwlppj5Y8gF25y--PbX12jnlq0nHv1P0XTaHsDlGnu4vmtjI7EaHg34vU-pKbw2e3giq046ADqrYad26o68VtPkZ1SteCZ5nxZihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق کشور شناسایی شد و هدف قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/460954" target="_blank">📅 20:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در منطقۀ جیزان عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/460953" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldxZmyJ8SwIvk85lNv5WAqouPBbSiP9buWGZ4kFkHEDXKSSiYMLztKeVjqAsyY8btL0VqUHByxY7lMZ8HlInS133o08PbD46gU7MzHZjp-VEjO1t2HcDHJAfWgBAZU0NnN2pcNPKU9CYUzNGM7vyn0975humI9HhxSZf4zd-Yy_bddbFpECaFGt9WtNZGe4UGIOD1kh7bN7hswNIs6Kxn4DaCDW5ZNz2xPSphEmX_K2SCibeoORR51amMyJS-wjJm6Ri3auVtNwBFYdCdi42eOPwub3u9fELoQ6f3dfj36_8ir0bEG1ep6pjifuQON_R8-6uHeN_rysqnm3IgOs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
با بسته شدن تنگه هرمز، ۲۵ هفته است که ترامپ هر روز بخشی از ذخایر نفت خود را روانۀ بازار می‌کند تا قیمت نفت را کنترل کند.
🔹
میزان این ذخایر از عدد بحرانی ۳۰۰ میلیون بشکه هم عبور کرده و درحال نزدیک‌شدن به کف عملیاتی ۲۷۰ میلیون بشکه است.
🔹
کاهش میزان ذخایر راهبردی نفت آمریکا درحالی است که قیمت بنزین در آمریکا به ۴.۱۵ دلار رسیده و قیمت گازوئیل هم رکورد شکسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460951" target="_blank">📅 20:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در منطقۀ جیزان عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/460950" target="_blank">📅 20:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460949" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpCk0nlkXrHeOCg2bqq75gapqrE6L4kxO5B12Cg4L7_qaLgVQKIG0O3mY21MYCoq82fuaPW4n2AW9wqAZKB-AWPGS8fqgdjNbiGA3k-JL3fWm8gLJ1IRge0tPeYMqUmlFc8BmPwmK8ewpc3WK5xVctx4SHqZLSlVZTFdEXIoQL7CySjmPboEHlaE6KJ3vLz2EtZUhyldYa5llSYNY-H9oLWrDXghn5dUozVcLsxdxPi1Q4StbBreEok5DQi7YtAS0FzpT-BD2wrQyVbeXghnnWbiH_btECHgijbPFjMQhxqEgPhfc0qCAK04Sp4769GqzExaPFr85Rt2FantkC7CiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توران در انتظار تکمیل دیوار نجات یوزهای ایران
🔹
وقوع تصادفات در جاده ترانزیتی تهران ـ مشهد که از حاشیه پارک ملی توران عبور می‌کند، طی یک دهه گذشته جان ۱۳ یوزپلنگ ایرانی را گرفته است؛ آماری که با توجه به شناسایی تنها ۲۷ یوز در کشور، بار دیگر خطر جاده‌ها برای…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460948" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTjbd1U-5atIx1cf5Z94TlWsQJwNCizq29JWbrd6dRSBv9J2iRs7BFr07oT7rXMhzRrFDMjhUtRdZrgodMkio5XM9pAdv7ijOMa-op8SMP3zFihcNj_OV-l6liHI2x5cHcTy0LMRM2h19uPT1mSi0L3N-blGgLAzLyyCPk89tHXSsP-RlmMv8dYV8MOMwXXGpg4HbANc5y8b1ySPbBRBJ5jb9ouZ234Jl4HmWFhHJv1TGDr6XQZRTWMsNzSuIdBGt2F8Z2yofzf3Ctva5wkpQrgCKQDQcBuzOlq7pRk9LQAavJl4J2Zx3lbhgPUU4e1EZzu5KP8f6OVdlmO9M_ozyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG1gf86hxFPSq2OnjT6gEWGFt4y_TG3ar8TXf7j4k5cqziiBhP9Z9Nk0_XvSEge2xG043auD1iG3VBUtueYjwWIyJXIpjVKhK22kIo0X8EHtWW9oV0OsgbAMMSxZiwIuqHT1NR35hdkoZoe3nddeMh-EDpxhPTwhDWFz-MMc3cNOSVEWunvzELNgSPjYaOpzTVySmgAN12CRc5Q2g9IFrfjQe79qwEQ3gllCKhUJib484qKvBp3E-6xicV4b7_nPw0cWW3i7-6lSYeafBaj38tgKglQFQN_MV7R9A_LpEvyN1cSBRNh34xpizWYvKhHIyNE6W1I-_pxrCk5EDWkXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgtA2sEgTe_4vNfAWFuF_P9n_aMkoIkmfFReemvnjIUbevvPHTOC9rDqtUWzWhnm89tpxp02hq527eudPf484CwjuhzeTJlA39Z3QjQi9vHGPQicHpxfIAaAQjtD2NVs1g3PNTdWwfVtnKU4lDflt0X5hyDszwxKF22zgMn0eCgsib_VMPU9lgxNVJehKWesV7Jw3YzylH6-WcaTTllT7CPuzQ7AGbo21rbeBNNBz0dLDitwdsJWqfKdX143JRgN8CvAHzzjY0JF8sv8Krsy3clsW__hBmaxFqUWfCzGCv2y3oKinZxHfrO8_eUqhsVn49KYtxHg0J0B4o7I1fm3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VttPJb7ThNAb-Fl6UKVFhRnkCEd-FU1OE5mjCjGCNh2SpFXBekym7zGt4HO5Wm9uzhsA2AwzP0N2Seqb4yqCuNyqpkAmqcbMnbykLmDughoS0QZOWULsW-ESSIrdBSYHsjZUJ6DyfnRHON4LufgN_AWJl3Z-Qwv7I2Tf8cfOUMGujc7J4jJ5b57HMkK5vO6jFk5lo5zYiBt8akt4eOrsGfWNzAWiFgC21D_AiwafrIGOlgmR8kh04UfRiGeol8Ic6KofZlEUkNVr0jVVwEKQ-7O9dpoxH-XqsIw67HxSn2QS8Ad1Tk3-xm1WE4VsWj6L6y9YJ6Hw27pBvXYkTH6L-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS8EbnMnx4f0p_S2XcxAs5Kja4j7BsQttGOUz6IabV2-lbltoazxJ1XRDXfi2zIpwSQ1gq0aBXMHOaAZgdjsTNXKI2WO8R7yr6WRP2qnGfIHYnXrbRjFz6OrSRrqy5S3c5ZXH9DRK2WUswzvvSmcHxi8H9S0Y0IRIhlOCo8ngK6zM5VE_vsr3r8--rvCcwOqsFg6iFXf8KsKVOUW5eNjsvFpcnmCsvsZN3pEYvNCXOAwqGej5C297IbEWXLnV9df1_ct0lHwxUh2ZVOOW_dRpIVcknMbjstSVy3CqRPdFx3UejKO6bd5H3G-KpGz0eFaXEKlZ5SYpdwwwns0l3IzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmL0ouM0Rv6M3bNtfQdAUpHI3Qw1OaMY4vYPKkg4swuL-kD8Ffw3EG5IAGNPe6qCOmBWfPmhHAjVENC_9EO9IRuEJWsd95Ifdn7mHccO0A3XfLOlp3pFuc_5smbvT2Ne5HVPYm5i8Hr3tPdCgON_V7S51usGIkjQ8JKqZLseUExI_u2s6hr--UPukeKsaD8ih7B3RPkROwb3UV_iYpH4kb-rBfPlgTOvwpB1epT76DjMR0Qk7RIZcCf4WSYWzr2NhYplkgmR_MFcddb7gPjcDfEVwk1xmhf-KHyCFd7SWftH8rT5Q19RSYlTZkgQeeCW7vAkLYI8MVLO_TXV7_jEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RneVSQpyIX-tP4gbQVKKkkNVbzH1GC5AQ4oF8GY5Dw5SoDNYnpDItqCD_EJrInIA_fvG8MlnbwulQ6Kh3u5viQD5vDDrQNvYullLaQKvDNl1hVm1AVKYLp4d6T8GX9GOxzR4VxaYYvbhrKukoAFTh0ECmFwBgq7vVb4aHzlH5BRUoCtpnlR8TMYwNMCMTaREuobKt7f6NGLgjHh1dQ5QpjE0kpTWnrgTStm3eUXWli8d2j0st7AiGoApxX_jk_pQBS2jwuEaEGVOC37wYmIQupo795qw_NBI9ETQqNF6NMNs59OhbPZzD_fH3TXX_ZstV3oJSno9QeQVtzGGQXqTlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین دیدار هیئت دولت با رهبر شهید انقلاب در ۱۶ شهریور ۱۴۰۴
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460941" target="_blank">📅 19:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396413856f.mp4?token=HyFY-bno63vOIfzXQkr2frKEpDsS9eXuLKpEI5z8S14MG3Upys9gbQ87EJtYikwp3tSj1rnJ2-xuQmvaIsdYH6Wm1x9XQIn8nxV3RAcPgzmvu5rx1tP8g_1Y6nzW3GUKFymbnCaVS4SIxJdC6z5Yc3e-Cznu5LvBS_O1g3Os3bPdjR-1TB2nqEuEW3HGUZkEIEsdkLJT-jCA-OccuCrJLpAx_X-hYZpwxZ7GU03qLh-aSfXz74GOUcp3CyGy90CkcSlWwRdtdgsl6xiSx3Bm4L_1GOVgpVJC2BEHCripLksaF8_z5MGdFDQtGUtTV9z7igjylKSVC9hBhpPzrNuaPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396413856f.mp4?token=HyFY-bno63vOIfzXQkr2frKEpDsS9eXuLKpEI5z8S14MG3Upys9gbQ87EJtYikwp3tSj1rnJ2-xuQmvaIsdYH6Wm1x9XQIn8nxV3RAcPgzmvu5rx1tP8g_1Y6nzW3GUKFymbnCaVS4SIxJdC6z5Yc3e-Cznu5LvBS_O1g3Os3bPdjR-1TB2nqEuEW3HGUZkEIEsdkLJT-jCA-OccuCrJLpAx_X-hYZpwxZ7GU03qLh-aSfXz74GOUcp3CyGy90CkcSlWwRdtdgsl6xiSx3Bm4L_1GOVgpVJC2BEHCripLksaF8_z5MGdFDQtGUtTV9z7igjylKSVC9hBhpPzrNuaPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نادر محمدی برای سومین بار به شکل خاص و آکروباتیک در لیگ دسته اول روسیه پاس گل داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460940" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTiQwLO4qRrgupUo7prnm3TdW_JZ_FlTdYbDnZziYCMCSbjCpCEKSk8R9XXKsgSkUbQeAOXP548Ytc5hqIjsZXsWhT9i4VluD_Fk8-ZUks3gqZ0TswsShgzPoUzypKkVZIeVITweauDgzCdksfv40Siq26qoVEZtZwXTGzMvocUJPRyj2hDWdrjUvNX818tbhBwnIfQLMq44B1C7SdRgsHJToZajw8NFAlOr7PJE8BPZ22qnwYzNfm66Cn9GD366Lb13xOHocp80zqRW9xhBIUlIPZYPjryMayrxdDkEWEpOIIsMc37sFKlJhgs7XEaohB2OU8QtCetNAeYRnjuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و روسیه نیروگاه‌ هسته‌ای جدید می‌سازند
🔹
به گزارش خبرگزاری تاس روسیه، مدیرعامل شرکت روس‌اتم گفته روسیه برنامه‌هایی برای ساخت واحدهای نیروگاهی جدید و نیروگاه‌های هسته‌ای کوچک در ایران دارد.
🔸
نیروگاه اتمی بوشهر محصول کار مشترک ایران و روسیه است که از دهه ۹۰ تاکنون ۱۰۲۴ مگاوات برق اتمی برای ایران تولید می‌کند.
🔸
هم اکنون فاز ۲ و ۳ نیروگاه اتمی بوشهر با مشارکت روسیه و به ظرفیت بیش از ۲ هزار مگاوات درحال ساخت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460939" target="_blank">📅 19:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سهمیۀ مازاد سوخت تاکسی‌های اینترنتی تا ۳۰۰ لیتر افزایش می‌یابد
🔹
مدیرعامل شرکت پالایش و پخش فرآورده‌های نفتی: تا سقف ۳۰۰ لیتر سهمیۀ مازاد سوخت با نرخ سوم بر مبنای پیمایش به ناوگان فعال در سکوهای اینترنتی اختصاص داده می‌شود.
🔹
این تاکسی‌ها با اولویت‌دهی مبتنی بر میزان فعالیت، به‌صورت رایگان به نسل جدید خودروهای دوگانه‌سوز تبدیل می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460938" target="_blank">📅 19:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئیس دانشگاه سمنان: شایعۀ تعرض دانشجویان عراقی، دروغ بزرگ است
🔹
رئیس دانشگاه سمنان: بامداد دوشنبه میان چند دانشجوی عراقی و ۳ رهگذر، شامل یک زن و دو مرد درگیری رخ داده و به زد و خورد منجر شده است.
🔹
براساس گزارشاتی که در اختیار پلیس است، آن ۳ نفر حالت عادی نداشته‌اند و از نظر رفتاری در شرایط غیرعادی به سر می‌بردند.
🔹
سپس حدود ۱۰۰ تا ۱۵۰ نفر از مردم محلی و رهگذران در محل تجمع کردند و شعارهایی نیز سر داده شد که ارتباطی با اصل حادثه نداشت. در این شعارها نیز واژه یا عبارتی دال بر وقوع تعرض وجود نداشته است.
🔹
در این حادثه هیچ‌گونه توهین، اهانت و تعدی از سوی دانشجویان عراقی صورت نگرفته است.
🔹
عوامل دخیل در حادثه شناسایی و در اختیار نیروی انتظامی قرار گرفته‌اند و با دستور مقام قضایی، روند تشکیل پرونده درحال پیگیری است.
🔹
پس از این اتفاق، برخی در فضای مجازی سناریویی تحت عنوان تعرض مطرح کردند که این چیزی جز یک دروغ بزرگ نبود. اصلا چنین چیزی رخ نداده است؛ این حادثه یک نزاع خیابانی بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460937" target="_blank">📅 19:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXPTCtoq5PcsFlhIt2sUx8WB36duQnIb1uwRJMRAZgGqCChp5dkrM2Lobuc-oh8avfXlyy_bQr9yzlMllBHOwS1hdrErlIGMXUjX-OjumNS_AmAC-RZ9b8tPCj9OeZ9sMnzxxR2J_Bo5k-1UbQTOed8ToIGdvuJGjO74d5sJordb1DDqUe5mMpYibNPD3bepwVCMZSfMUs4xDzNZFEeaFiWqo3HU_BFzkrjP76IrDTit6dujOSRIqscliRxLlhD6dDIY3-B4n4HdhakCASZm2SnKddXLgAp9ogsdBBmeZW47enC4sdpiF1nSInnrrzKdkhAzbQpkWP5WOFghIuZEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
دوربینت را انتخاب کن، حقیقت را روایت کن
مجیدمردانیان، پیشکسوت عکاسی خبری : «عکاس انتخاب می‌کند چه چیزی دیده شود؛ اما هرگز حقیقت را قیچی نمی‌کند.»
امروز هر کسی در جایی که ایستاده است مانند سرباز پای لانچر برای کشورش می‌جنگد؛ از دانشجو و معلم گرفته تا آن کارگر پای دستگاه اما هر کدام سلاح مخصوص خود را دارد.
اینجا اما آدم‌هایی هستند که برای گم‌نشدن حقیقت می‌جنگند.
دانشکده رسانه خبرگزاری فارس با رشته عکاسی خبری (کاردانی و کارشناسی)، تو را به روایت‌گری لحظه‌ها می‌رساند.
اینجا آموزش با تجربه، گفت‌وگو و فعالیت عملی در باشگاه خبرنگاران «توانا» همراه است.
🔹
بدون کنکور | مدرک معتبر | اساتید باتجربه  | معرفی به بازار کار رسانه
🔹
ظرفیت محدود – زودتر اقدام کن
📲
ثبت‌نام: عدد ۱۴به ۵۰۰۰۱۰۱۴
🌐
سایت ثبت نام :
futurix.ir/go/rxDxXO
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460936" target="_blank">📅 19:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
تصاویری از حملۀ هوایی عربستان به یک زندان در استان الجوف یمن
🔹
به گفتۀ منابع یمنی ۳۵ زندانی همچنان زیر آوار هستند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460935" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d4c57458.mp4?token=f-VwdH77EqsYZZ4jVx4BxO7zCmXEMuhTYsINcws1_ONpKXhQFcmLVSMAVw3I1h9sRXGDcsKv_a46tgWUHGdjoRTfFhS_41JWrG7VfJdKOKzZlT7gEzXwPGVYRdJXW7XvkTnZsK_kzkBKpkQn4C4IEPNZEhOFpwOy8cfNDVD3is-Uxk7d7Y1Qc14TN2QN00zGSW9j_8MhwqbB5i7a1KSood4ODPoubdAQrpHwM6yHTzRLetP_RtggIQ_iFhp9T22LBYdhdwJhqeM9CT441Q32d0Jut_v-UcG3E1acQh834spylWEY_OR9YT_HikbRC2YCp00wKs1mBBaK00BzoKVvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d4c57458.mp4?token=f-VwdH77EqsYZZ4jVx4BxO7zCmXEMuhTYsINcws1_ONpKXhQFcmLVSMAVw3I1h9sRXGDcsKv_a46tgWUHGdjoRTfFhS_41JWrG7VfJdKOKzZlT7gEzXwPGVYRdJXW7XvkTnZsK_kzkBKpkQn4C4IEPNZEhOFpwOy8cfNDVD3is-Uxk7d7Y1Qc14TN2QN00zGSW9j_8MhwqbB5i7a1KSood4ODPoubdAQrpHwM6yHTzRLetP_RtggIQ_iFhp9T22LBYdhdwJhqeM9CT441Q32d0Jut_v-UcG3E1acQh834spylWEY_OR9YT_HikbRC2YCp00wKs1mBBaK00BzoKVvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۳۱۳ هزار جان‌فدا در تهران
🔹
رزمایش بزرگ مردمی «جان‌فدایان ایران» با حضور ۳۱۳ هزار نفر از نیروهای مردمی، بسیج، سپاه و انتظامی جمعه ۲۷ شهریورماه در پایتخت برگزار می‌شود.
🔸
علاقه‌مندان برای ثبت‌نام و حضور در این رزمایش می‌توانند به مساجد و پایگاه‌های مقاومت مراجعه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460934" target="_blank">📅 18:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شمال تهران در انتظار رگبار و رعدوبرق
🔹
هواشناسی استان تهران: وقوع رگبار و رعدوبرق، وزش باد شدید موقتی و احتمال تگرگ و سیلاب در ارتفاعات شمالی و شمال‌غربی استان به‌ویژه میگون، اوشان، فشم، شمال لواسان و شمیرانات پیش‌بینی شده است.
🔹
در شهرستان‌های پردیس، فیروزکوه و دماوند نیز در برخی ساعات بارش باران، گاهی به شکل رگبار و رعدوبرق همراه با وزش باد شدید پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460933" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWoQzhhJx2iWViIHzSrabhuG_coUBNDw8JWWdTSn8ZIq8T7AE7k2mUSDe8tO-uhoQgeTpvhu7fT8MS8KN00Ekr3smDHWA8vaeofr2BczV1LCz-QnZoxOj0B37nxMPTaLl7Xflp3kANnJo6oCqsdGeZt5XUmYoX1_R5VQKnL-Z0XNk4MC-slTcrdG7LH10Qb2l-nmIKPI4AD6bteK7NcLjhj5ffiQzZEtoOK-FfbAL0o0llpf9ihz3NdEDpkr1Xb2UfqIsOzRiAjLm_IryBCUkXPuBi0yC8WxybNwXS-0mjv6EpkaW1OQUNAP9PAi1ubBuosz-snrL5XEsHkonDYcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از تنگه هرمز منوط به پرداخت تعرفه و غرامت جنگی شد
🔹
سخنگوی کمیسیون امنیت ملی: در ادامۀ بررسی طرح «اقدام راهبردی امنیت تنگه هرمز»، موارد زیر به تصویب نمایندگان رسید:
🔹
الزام اخذ بیمه و ضمانت‌نامۀ بانکی
🔹
پرداخت تعرفه‌های بیمه‌ای و خدماتی
🔹
پرداخت غرامت توسط…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460932" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
وزارت خزانه‌داری آمریکا امروز نام یک فرد و ۳۵ شرکت را به بهانه ارتباط با ایران در فهرست تحریم‌های ضدایرانی قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460931" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh1RorIADoO80UIp8hkzVv-PxtiTCnV83z7qc8HT3b9xa9ZitR7JT52g8EXdb_oxlqfl-_Shl__j49xjzx8PX4kWPXNeaaarnejXsmlHyxUSZbh981oXd1Ks-V-tvJpPO_YJVoLGEPbmKxzp0jafdJ9dJnNeC_ANR4HPssFid59RCpetxoiJeEXzjZB4cjtLWD_1XYYSBH4qANGkp91AgYoltjGa8bcr-RaczbDo9xCLcrR8kozv9iqU39laS9JNIwGmyalPESAYL7nBU4nsA-BTkcmexNOPd3_SVigIC_FmqZVCs812HDcQ8pB7O_De-Sv5m8J0QMFUKYGo2MKUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460930" target="_blank">📅 18:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQNIhl_tM2LM-2ClAdmGF_-YBbY9xQ77XPri6Aw0SOWSTEtXuNgTMMY7fnArFSE6y8IW2rcAlYFZJ7iwSt2WLfCacKI-hpHaqcNHovTJuXsC5tkk5foqHPDTV_TD-CPoLta8oc5urrDeFlhBp56A7n2yUrdxh4tElGDrQ6c-T319gnhGvQHry9V2WzTjGbf0YMPW1egKEB6iQkGxP4R2BaLnQM6rFb2ZqyRFCJEoqOA7eK6Liq2wFqgh4KGGogKzzQgn-NOp7HJmQAj_KmemZbSJNp0fcDVjG-joe3Jx1Zo_zOhvQXxGTM0HdAyG-mbpa0MD2ydrAo5i4I9p5R1BWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
🔹
این زیرسطحی اکنون به غنیمت گرفته شده و تا ساعاتی دیگر تصاویر آن منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/460928" target="_blank">📅 18:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ حملات هوایی عربستان همزمان با پیشروی نیروهای یمنی در استان تعز
🔹
منابع یمنی از وقوع درگیری‌های شدید میان نیروهای ارتش و انصارالله یمن با مزدوران وابسته به ریاض در شهرستان «الوزاعیه» در جنوب غرب استان تعز خبر دادند.
🔹
برخی منابع نوشته‌اند که «نیروهای یمنی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460927" target="_blank">📅 18:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
وزارت خزانه‌داری آمریکا امروز نام یک فرد و ۳۵ شرکت را به بهانه ارتباط با ایران در فهرست تحریم‌های ضدایرانی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460926" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e36440b.mp4?token=stM_wfx6aTaGs1Ha8ceLHxQuyh1viBFeCUbyMx0SITzPPCRFoJ3ZlPwRtvdjoEqSLZiJ6nMaLI8C4C5q3GfgGPZnCy-7qnPsBFNG5q-FId5Q1xgEcB5SCOZilT_QPTvEn1B5qOxNNLitDmjOgoZIeVDd_lXe3ef0Tn65zV84nkd0GTu6hwGGWTSMyDwTBcnGEpCPHZGuQ-_mDw-OakuDgYr3g7xgZoGZy796Ats9LH0Z6bl32Flb55MFnH5ZkwazgBTVPQt7NGj-RcR2dtomYxzP082QpuVSAEPquXolrdKq7mwGN-ky8q_ADUgROgGGqnP4fMK6TCtydUvD7o24gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e36440b.mp4?token=stM_wfx6aTaGs1Ha8ceLHxQuyh1viBFeCUbyMx0SITzPPCRFoJ3ZlPwRtvdjoEqSLZiJ6nMaLI8C4C5q3GfgGPZnCy-7qnPsBFNG5q-FId5Q1xgEcB5SCOZilT_QPTvEn1B5qOxNNLitDmjOgoZIeVDd_lXe3ef0Tn65zV84nkd0GTu6hwGGWTSMyDwTBcnGEpCPHZGuQ-_mDw-OakuDgYr3g7xgZoGZy796Ats9LH0Z6bl32Flb55MFnH5ZkwazgBTVPQt7NGj-RcR2dtomYxzP082QpuVSAEPquXolrdKq7mwGN-ky8q_ADUgROgGGqnP4fMK6TCtydUvD7o24gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی خراتیان: جریان نرمالیزاسیون سندروم دکمه صلح دارند و فکر می‌کنند اگر بروند و درباره همه‌چیز مذاکره کنند، آمریکا دست از سر ایران بر می‌دارد.
🔹
حتی می‌گویند تنگۀ هرمز چه فایده‌ای دارد، بی‌سواد هم هستند. هیچ آدم عاقلی این حرف را نمی‌زند که اینها می‌زنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460925" target="_blank">📅 17:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9ztQmL_Uc0Xwa-7pPQbOO3dx8RYvmg__DxciqISMm7-B9XlBNdA6LT66xnvNtWSeQEkVl1Enmp7LsOxLAJvqIrkkp4YTCQhxSsLYbAKGl600hDP1bNyDsH07GmXVJP76BCtVubhUuphk7sr1ioUsdz_uHUPzNDxmJ8aVmNU_fxQYSP363BT-z82BWnBxjdTTsqQN6GHbCAalE-q3iXK91t76VVKJ5amKmcr8adcS-zH_61dGGA1mfbtaUeX7LxdFcnSgcFBzr7OukCTZc50Gw7WfZ5_JQG4R5eImb8Qa_vfgqzvAiez3j2FUzp7THgQu6ixuuS31B1aueGkPKHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست امروز سران قوا به میزبانی رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460924" target="_blank">📅 17:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-uaceRCmEQbxHAWUAVBrqMrY9fcGeVnal7Up3L-7sldb1xzNJHLNgkqyOpE_7tlP5J-9O0DOFznNyWZ7ZxqmMjQzVryCRvVe-i9u6G4fo4BxrDjrN6uaikrVEF3sMK2RPy5e_dZOX6qpOzUdo287ihW1X8CpdrDyrEAjETi7hOQsHJtG56EYV6Gr9BWrZUvppwU4R69hOO8dXs3Yp4zsLWax3XFlwKVs9S5u52_eM53pudG3G4Y3UTUjuMrmA-alUGXg1jP5jRNGB5dxIwgcyBXG1AuzOXNsPShjPuX6FIf13mm-DDDXO2crp6mb1lXYo7_CCsVZ2mvQkWMxW1wPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور عالی فرمانده هوافضای سپاه: در شرایط پایدار تولید موشک و پهپاد هستیم
🔹
سردار بلالی: امروز قدرت نظام جمهوری اسلامی از لحاظ موشکی و پهپادی پایدار و دائمی است.
🔹
اگر دور کشور ما را دیوار بتنی و سیم‌خاردار بکشند، نمی‌توانند جلوی تولید موشک و پهپاد ما را  بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460923" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_3esF4yjNwsa4oFEr2zlQUm_jpBesKva4PDL6VRIzUAWyLdvfhwWJPpIWTl6ZISgTDh3E0aScNu2Zx-x2_LmSdTRWefybXIC35jvsRDWc2lc6SL8-bQMDCAWkmmWFsjbmVC5wz23De7AdG2tVnHqVUDQ6cSfB2k8_SNTMralDl39_nuWvCNR_HqZcTVz4uVQh4z69MHDcIxFyJlOIETWYZ2Md-ZC74Cmk_9_iheLvW3-SBx4ujewwvCkd--BM-9qATTUWMN28UDuf2S13mzYHI30KmeayMz3YM3_WDdyjKHCbtgskWclBEBlOGqIoGWAUn1Dgmmn5K4hC2FCuF5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت خسارت اثاثیۀ منزل به آسیب‌دیدگان جنگ از شنبه
🔹
رئیس کل بیمه مرکزی: با توجه به اتمام کارشناسی و ارزیابی خسارت حادثه‌دیدگان جنگ ۱۲ روزه و جنگ رمضان، پرداخت خسارت از شنبه توسط شرکت بیمه ایران آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460922" target="_blank">📅 17:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPUgo_5tbQ_NqqU7G6aEsSZa5Xak163UTJlx7Y3vkUOL4RysYv7FtyYwXRyZGZPgNVAXrOhMIkRBdZxoJvJrTYaSIydsF1e2arZWnHvMb2kZRur3PwgJh03YLtLMReJ4_qu71FVnxoiN4oqA0JGRuMtUvWiSwCFydTQMAUi5Fv039uP6iCZpaqsf3bz_w0pY-IknZMe6K0kR2Ww61_d8ZfClPfwG67K67Cn3soq0RWhXlh97StevG8vKf5vx1uVIvxreW1ftfJXbZbUkxIzHnruCKGC6AVn3Soxy6D3I_sy1er3mpF24HVqVjjgpKDFHqmZYPqeKiR_SqWJLv2FcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: با ساخت‌وسازهای غیرمجاز در عرصه‌های طبیعی قاطعانه برخورد شود
🔹
با قاطعیت با هر اقدام فراقانونی که به محیط‌زیست و منابع طبیعی آسیب می‌زند، برخورد شود تا بستر برای بارگذاری‌های جمعیتی غیرضروری فراهم نشود.
🔹
تملک اراضی و مشخص شدن حریم، پیش از اقدام اجرایی برای احداث جاده و خطوط ریلی انجام شود و هیچ‌گونه مجوز ساخت‌وسازی تا محدودۀ حریم مشخص، صادر نشود.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/460921" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460919" target="_blank">📅 17:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460914">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihPNWc-za5ydUvfwO6gx-ocNxuTY_Ym0tIm_jmFVchpJIcFu2j5vhAy_q2uHc24RhKAA6PcJyhHYFZHocCv4qnxkR2MIve5IkXk89tEvL8tBtEHvvKeSnyCVs_s89cTsR7FpYPYFI1K7nVs7qDKeXNPbUgNuO4GrJsIAocCmgtTE6lBN2_Qv3Phbc6QVSrXVTlCriSF2ksx7uIe7dMKHp4Zt2gJM4HPjeqgilhqU78PxfhP9IYXD7_ARHULo8ssPsF-PqEXi_5ng0sEz19ybSsJFZRWyLLfoK7KT7DifBf2T04tf1uJ8px3iowSs4_9Q5nuGdVb5ZWp2xssPfTOiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjyIz20rk5QjQTJ0EuQhyR5C9wQMmZLjwxYD5dztfouWPPX9MX5JDnmce-jAR8jI9I4-vAIAKHM6N5yAdOrnlv_dtUoNMWphfqLpeHuxiEjnUutMrwe4XtwH8668aEvODTeDOR9vxt7F5tZJk8jwcpQJVbd2OxYz278cfKXO-AatMQX2mjw9tRL43pwxNozgQoa2rf1Ed5EmnL6RCPrKSs9hWuclqwobPI0ZkTE6Z8Y_TuYHlgICV_FR2pX6kHmExGvIMIKs0YlW7bK94KZFTrBgG9B-8bWuUcVHVDjOiSJ6Jwfqb9v_0XVJ5hO8hin4ZveAAqKGjaK2WkhwQ-afYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffP7YPlSiHmP_8Um6WrKIuClngSYLmrGbecG7LwDJD0-2Ps-XG04mE9zhF8H_m_EBVE2BAeuT0tocoYsmYYAZNH2yIYCit3xEX7KIpxUVrd16f7pCXDt9e8KVbu5lfHpyltI9UZeHDZ1g96d0dL8HT3NQiocmBCqnAXndrLmJT7pElZcknadN5kQhTBBpqwP0tSBjI-HrVb64UEM_GbiaJ3PWT9jzV2tA8aZtSTJuL5OGwMYfCaWRYb9kdcJB9N2fLcAKgsYGkrP3iGFAbnUph-9I9PMVi5GNcicM5ptNRPcPr2hszOqczq6-6_dj_C0B0dGLt97kLeQYbNbLk3EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlN3DqpbY_A19861LI79rNXlrV22sGkDkDLfce2URYw_mqn7dea5p-9EgwZAAb26dXX5UL-mFDU2zOr2TuApARAxNuMWTf4jOd3DqUcbbusNVkwVay6etGHGzILgMmOCh8IKninLNRbb0NrwhYPNmje-sXYhBccHc878epUJe7Jg6aUpkYpw-E97tjD_RepneivjGwGQZVwRlealtbpDNq24nmLzFYk69Sj4iuxy4MgbqYwCwOkJvN0yMUw2XTVN8z6vdK6AFw5YkiWHSM_Ew4Mxb9a3P80QDwv9jXQQEb-IeW0UHSiSQtimNWbK6n7VJAxOqx4ExNqluZciSMIDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j78lKUa7wSDCBLWvuwzXR0FThP4F0BIFkvzywp6zt1_C3T2-7uhMd7vd_kTZdDkRCWyKIeRKXchAd0rl5kn2DSN4OCneeqqBhc14bCJbGaz8EfFZcd4j8lvHPvhcwtpYXfiAd5UwxopjX0ObGNip0J3hXAC5jRGrB8qKdKZXE_gPwWTQisT3xo54pBdLf-f0H5c86EdHNCqP-h2-Gt1NsU_TCZjcVZk-dOAQb9JYZlBQw8wIfrw_h_LiFiRbxwdKFRoyf8x07dl7a8n9ZHXEBllNWJ2npmbSp7w9mRJT3ydhDN3kywSFLDgMAbFfzQUcunTAS3of23qKlgvfPSgGqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس بسیج اساتید: از ما نخواهید که بسیج ساکت باشد
🔹
هر مسئول اجرایی که در راستای اهداف انقلاب حرکت کند، باید بسیج را «نِعمَ‌العَون» بداند؛ ما حاضریم برای مسئولی که در راستای اهداف نظام حرکت می‌کند، پادویی کنیم و به او کمک کنیم، اما اگر مسئولی در این مسیر حرکت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460914" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460913">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFTsIf8uFWZWC9OE-13Iwppq9L6xgf82wxbPAbRwvqLh9PaPvdh5Q0CXOpQfiyF3_H1Qo3s5ceD2iLS118bgleASeLR0sx-gP1CGpK4P-CZZ-vnJE3d3kevuU6HqsNqvVdjExw_FcKbqzMVbTUm2PC2V0exqveL7mLF_-yu3VJZco4xovnQr8zQNTSh2TIPLrnLwsmwT3rHiIeXUJhjchBK79XDvvUlPma1VRb37ikVcc6GX4yzLn9xLsZexgEN8-GovWhfY23c9nPL1PwO0dHaYfMjrE13euihiJvMw8kohkE1S8ml_yurBEoAe_7dD0ZqdU0gOZvMlKk-nFBcgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460913" target="_blank">📅 16:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMiBIOpJbapHviAgiFfEnyj-8Jc9Tvqds5rOk37R5Lyc3s8L1hnhmTcvv0mGeUsmZkKpWCutGmW-g1isMBNb72W2a1Qc4tUJpinVA1128D4qnDGt3aSve53IbnBs7qG1rPDT2DXknX9gxxM8d73Lejv1xpVw4rSAI1UfPKjIkhtuHcBJdKh-fHRS1mJJIyCBTsH_Nw_DE85n8KfmZVmrNiKL4YkAtIKVu1rQRp8IX3uOcj4BO0Wi6IPbhymK2YT59huaPsVISk84_tqNMqIQ2wybx2qhpZbsmLyOHGg_Sw7Ak510QgOUvl5iorWKdBBrSdMrUAwgZLh7MJmtc4ln3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، حردانی را از استقلال کنار گذاشت
⚽️
بختیاری‌زاده: تا زمانی که من سرمربی باشم حردانی دیگر در استقلال جایی نخواهد داشت.
⚽️
او  فقط به خاطر صحنه ضربه ایستگاهی در دربی کنار گذاشته نشده و از اول فصل ۳ بار به خاطر بی‌نظمی به او تذکر دادم. @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460912" target="_blank">📅 16:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کندوان مسدود
می‌شود
🔹
پلیس‌راه مازندران: از ساعت ۱۳:۴۵ مسیر شمال به جنوب جادهٔ کندوان مسدود شده و از ساعت ۱۷ به‌دلیل وقوع بارش سیل‌آسا و احتمال ریزش تخته‌سنگ‌ها به‌طور کامل بسته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/460911" target="_blank">📅 16:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEk16Re6GjVwf05d8DycFYg3QleHpPR0LAoPPs-fRGDEyGFul-0ALjXiMq_L2YO_yjGnTfwXiVlnOGZD0fTLV15-A1mZu0Q_4GfOWszOdZ1HT5dlCwJ79Dt5tchHyVKCBkOcsW37o-Xu2sHG2f9DiACP2QuLWVvbPL5KJOhibIXLlWjWURNL1MExrHJnZ5xDgqqXgjsVgMrE3PFDjUU2AwnJIaTBfcEhT3Uo9yS0hqZvMrEYC5hBStY-rck5r75EjXhr6Sja9ELGSGWWihCzEyNut4DePNJxm15HMkxRxf7D4LHc9ANjzytw9fW_-LobRvbgR10OTEznv7YVlrWAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2LU5_9OSeCZt4e7vPF-ZkDtzl02S15AFSCaX5Y2rUPIhoZ1g6sg-q58cLsQAui9vCyuN_vYaxLwd86s356rkH82Eq_ffTh--oEWO8NB9rBMmtFaVBTSz-U1omdBjtNttdGQ__4sH2dVAUSLZKBvth3ewggCpyc1QeZ0ybZ5CX-pmXLUUgnUpCRub8W0rwEU-D1sacQdLsfrrTIUgz4xJxLtOFDjnMRkqbkIbE1OrEIRbHssNxdKzLiVunsdprfgs2EspiZaHgIWzuQsAfbtFfGta7QFER6Ua0iQgwFQxsH91FydmNYs8lRExLgdG0SZ2SaUvPqZvvATluF1AWDMJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پایگاه هوایی خمیس‌مشیط</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/460909" target="_blank">📅 16:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV5oZBwtFUtH4GTJMg5zF8ZeyylKXFNEaG5g8O32hS5xVN2Li9WGVWg6oGLpbZf8y8t9NgzvYx__151S9DCcCgN4vp703D-dckSvPG4P9fxwh5ENsmHkyU-4GmScaRP1lRGV_LErckdrFXzgw0SjRYN6a8QbqiwaiYqBslthkUT1FlgarnIl1tOjS_YaIAANkm0usiKF8bdlVf9izxeTEuJ1m5T69ieb5PwgER6dB-mebb30j0b7b5H_xRChJD3fWuWEfnipa7NJJownC6cTQ63LyLDoYc5F60vY0ea5E5nDKEMCCxcetAiAghYtVJVhKmouykjnnQF3qUIppAJG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۷۰ کارت سوخت غیرمجاز در مریوان
🔹
فرمانده انتظامی مریوان: در بازرسی از چند جایگاه سوخت، ۶۷۰ کارت سوخت غیرمجاز کشف شد؛ از این کارت‌ها ۱۶۴ هزار لیتر سوخت غیرمجاز عرضه شد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460908" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
۴ حملهٔ هوایی رژیم سعودی به مرکز یمن
🔹
شبکه المسیره از ۴ حمله هوایی جنگنده‌های سعودی به شهرستان «الجوبه» در استان مأرب خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460907" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
شکار
یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق کشور شناسایی شد و هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460906" target="_blank">📅 16:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460905">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
شاه کسی را نکشت؟
🔹
مردم پاسخ این سوال را می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460905" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0dv2neVxwbuwu3hnbyJPLpN8VjKc9p7H-CPlrrHYel7ALQg6G2DMslX9Adz8Ma_ZJQbS3VkMAZuXnfLmtB8CRGhuuHzLWeRWRaaMNwvgDdK2IKjmWFd439e-rKGYHoPqDEIB4saM_HXIJy7BfkmJU3WlsM6OLYLWz_0S_iUAkOjbwFGrx1-vbQbCrGiWYSM2AxrC3pR4Z0aRhldhGowylV9vG_MbTCTOBra5xdhh72a1XDaCvHQUDmHtwquHQu4Fy-SkJFUktSogaVAG-SI22uVySq4qo5hp6rXUy7PXwU7wn2-dHAm27gyk1nM6g2XCb3rB9hD0zmX_Oe8_ln7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460904" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bezWsNBMoeOP3GH4BqwleEsu8xHqRuy_9nJfGh3FfIdP1VNmIx7pLFq6caPHlg-fqq6Iq6ch2Sy_FkB8CIKPRnIXb8U2y1Jp0vukBzQO-xNMKLtFZEVrIChdewYaJlD9MW8doVog2_Ecu4iQZXRToYazPahIzearVC1TN3eWknAnxKK_0FxUdsVSvvr8QjOBuK_jdGHot2yRuKQcSnnQnfInUuCsNm5sHRrdHtw2gOS_82QU1ZKj1dsYr0GozlS8bpci_p6QAtjehayQceCh4wFG5Up7Ql4xvBraM2TfqxMxvnDEf-G5QSBqUcP-LMcY2t9PIuEGAnNxYDA76CsEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فرمانده بسیج در راسک به‌شهادت رسید
🔹
پاسدار عبدالرئوف اسحاقی، ساکن پراهین گواش راسک و فرماندهٔ حوزهٔ شهید فدایی پارود، امروز درپی تیراندازی افراد ناشناس به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/460903" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرمیتا بابا، این همونه که بهت میگفتم؛ این آمریکاست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460902" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460901">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm-dmjefWug_ZdzT0reh3bdU_xQFzmA1S3R2n5GRod5-ZpJu6kHHPzzMrCzA14Z-4P0yNfQC9dr1xhGiWnFx6FBtlpPeTthsEURUwweL2NbgvJhOn97zRn9DHJ_DZG_vzolL8asbfCC0uf9_MqN7vFhdyuFRcAFPhqPrIg-T0O_JitOHmkzI9KvgfCfBqjVtyHMRgataBr59Uii4_tsuDSDbsbocDQAQxOp5vS6TvJqNBpAUqYOT_pIiw9F91iSjykj8oHOe6ghVEVvZ9lBG0OmjVC2I_GNlzZf8a9pIHJhyE-HtFqaDQQqwahbmT4dMV7Zb8nfYRiyzk7nlliRSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری
همزمان با تثبیت کنترل تاپیکو بر پالایشگاه نفت ستاره صورت گرفت
✅
قانعی‌فرد با حکم شهیدی‌پور مدیرعامل شرکت نفت ستاره خلیج فارس شد
🔸
همزمان با تثبیت کنترل شرکت سرمایه‌گذاری نفت، گاز و پتروشیمی تأمین (تاپیکو) بر پالایشگاه نفت ستاره خلیج فارس، وحید قانعی‌فرد با حکم روح‌الله شهیدی‌پور، مدیرعامل تاپیکو به عنوان مدیرعامل شرکت نفت ستاره خلیج فارس منصوب شد.
🔸
قانعی‌فرد در یکسال گذشته نیز مدیرعامل این شرکت بوده و در ۱۰ سال‌ فعالیت خود در این مجموعه پالایشگاهی، مسئولیت‌های مدیریتی متعددی از جمله قائم‌مقام مدیرعامل، معاون برنامه‌ریزی و توسعه و مدیر مهندسی را بر عهده داشته است.
🔸
وی دارای مدرک کارشناسی مهندسی نفت از دانشگاه صنعت نفت و کارشناسی ارشد مهندسی شیمی از دانشگاه شهید باهنر کرمان است.
🔸
انتصاب مدیرعامل جدید نفت ستاره خلیج فارس در حالی انجام شده  که این پالایشگاه به عنوان مهم‌ترین مجموعه‌ پالایشی کشور، نقشی راهبردی در زنجیره تأمین و تولید فرآورده‌های نفتی کشور دارد.
🔶
صلاحیت‌های علمی، تخصصی و مدیریتی  قانعی‌فرد در فرآیندهای ارزیابی و شایسته‌گزینی تاپیکو در بالاترین سطح مورد تأیید قرار گرفته است.
@tappico1381</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/460901" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460900">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Minab - LV - Eslah3-1080 (2).mp4</div>
  <div class="tg-doc-extra">118.6 MB</div>
</div>
<a href="https://t.me/farsna/460900" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📣
میناب؛ در قاب روایتی جامع
▫️
«بانک جامع اطلاعات میناب» راه‌اندازی شده است؛ این پایگاه مرجعی برای گردآوری اسناد، اخبار، روایت‌ها و آثار مرتبط با واقعه مدرسه میناب است؛ جایی برای جمع‌آوری خبرها، گزارش‌ها، تصاویر، فیلم‌ها، روایت‌ها و آثار فرهنگی و هنری مرتبط با این واقعه.
▫️
اگر خبرنگارید و گزارشی از میناب منتشر کرده‌اید، هنرمندید و اثری خلق کرده‌اید، از خانواده شهدا هستید یا روایتی از میناب و آنچه بر آن گذشته دارید، آن را با دیگران به اشتراک بگذارید.
بیایید با هم این آرشیو را کامل کنیم و بخشی از حافظه میناب را برای امروز و آینده ثبت کنیم.
🌐
www.minabmemory.ir</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/460900" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460899">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه سرمد sarmad Insurance</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awr9BQ-k_SqNQIsVPOq2l9Q3i21ic1N0oRl0tBiwi_X-D7Ux1p7xpb6fxi8foQADny-Au8MCVV40XbcOcQUVmzeut8Hi9r6JiCpy05h6xLuPIdp6LBZX7oQNyT0G8SgkiDuJjlhKm3YmCN1BQYVYeTYWf0pBH7IVgK4zHfjNErhbk9cFfSQkjoE2ZJ9NsMTUrRgvg0aiupAxMMvm_D0eYPZ40G1YY_Doqztp3S9u1DrBxKf-U1McI125bYaB9Xm8tR9zKEtWwVhw0ZkoZZu3jWq8EseQZ-nFne4y2mxn5CZaVLgupSn3biVfQgeVGuCAckeNim24TwdXHyjqvioUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ثبت افزایش سرمایه ۴۰ درصدی بیمه سرمد در مراجع قانونی
✅
به گزارش روابط عمومی بیمه سرمد، در راستای برنامه‌های راهبردی شرکت و با هدف تقویت ساختار مالی، افزایش سرمایه بیمه سرمد از مبلغ ۱۰ هزار میلیارد ریال با ۴۰ درصد افزایش به ۱۴ هزار میلیارد ریال از محل آورده نقدی سهامداران، با موفقیت در مراجع قانونی به ثبت رسید.
⬅️
این افزایش سرمایه ۴ هزار میلیارد ریالی که نتیجه پیگیری‌های مستمر هیئت مدیره شرکت و همدلی سهامداران است، بیمه سرمد را وارد فصل تازه‌ای از فعالیت در بازار بیمه کشور کرد. این اقدام، با هدف حفظ و ارتقای نسبت توانگری مالی، افزایش ظرفیت نگهداری مجاز و ارتقای توان شرکت در قبولی ریسک‌های کلان صورت گرفته است.
⬅️
این افزایش سرمایه، نه تنها پشتوانه‌ای محکم برای ایفای تعهدات در قبال بیمه‌گزاران است، بلکه امکان توسعه پرتفوی شرکت و ورود به بازارهای جدید را بیش از پیش فراهم می‌کند. با افزایش توان مالی، بیمه سرمد قادر خواهد بود ریسک‌های بزرگ‌تر و متنوع‌تری را پوشش دهد که نتیجه مستقیم آن، افزایش قدرت چانه‌زنی در بازار و ارتقای سودآوری در بلندمدت خواهد بود.
🔗
افزایش سرمایه ۴۰ درصدی بیمه سرمد
🆔
بیمه سرمد، تکیه‌گاه مطمئن
🆔
✅
@Sarmad_insco
☎️
1516</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460899" target="_blank">📅 15:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/460898" target="_blank">📅 15:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EztrAioN778H8tkHRnHcVxeVjbodgexp-5l5VadRXO8FLQ5Bg8bVECbJEUy2NbjtjlJNEaWkITOzaIqwF2PG39khykmihHN_nvUfG6-vO0i_OoEFNIFkad9MCPhEAQCBCgXYYjuHK64jhgljXqXgxrSgb_U2wZWX14pT0Fm7P4-3Tjap6XBxyxcLtO6ZEf46JwfWr9cD2z1UA6_ngz1EX0xanFlHBSZImFtQZpCDGFPBF8LvsajCZ7a6MDiPBNW4dlTxY47SmY86DU4XePPTPXIN0DHaz_OiZC-erU9QAlzXjltiiyKLPPtmR52tZ7D-F_e1SJ46YBMRhH0ykz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عزیزی ادعاهای ترامپ را با هوش مصنوعی به سخره گرفت
🔹
رئیس کمیسیون امنیت ملی مجلس با بازنشر تروث ترامپ که در آن ادعای پیروزی در جنگ با ایران کرده بود از هوش مصنوعی پرسید: ترامپ تاکنون چندبار رسماً مدعی پیروزی در جنگ با ایران شده است؟
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/460897" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460892">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdcuFhcnZdqoNnEGKAVhJIUrwxJtCvRksCo3eRDetHkGiGbvxRnkZDYTGWG0UKTfGDDYjKp_Zke_myhl7fB-39vhs5m23ZsefSX3qKsCNWRXxR-rKwZAioprqUb5e61VyR4AlNqMTqeb9hmkUyD91yXroynnuowM3RbY00y89FHQgQ2T83w2B2d03q64Fu5I9bF-BKmU3Un8lNWigot_HzBaUr7NO1C59JVoN7jrRrpgZwiSNXvv-Gj0s38IcEZ3KcotXVzNkRyIT0iMhsjLyHUUIufp-rsqwF8oxpe0xyMUub-nuvW6zVYO8iK93xHWtK1j-STJDPwah3xSVsgI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1yeLNhprImx9QPV5zMTgdU-ZUNUDz6ciMz6CBytyv-XB4SrS1uxgJ068lJflumExgo4tM3b791qUqUbqOJeGtzaD-aq--OTnGdZPIMYrL-4LA0H7uNfWC2w8VcHFJQCqcL7L8K3JPdlBXLer-Ny6S0pEyU5oH6wLwyHtjWs6ZJGWAqNF8hscJzhTXOxCWdWD7blCkpHPD37RTyhcbCaXjZj7Hlos216V2iNeVfUKRkr4xKHLJ9kiOZiHqYYG1mCQQTImcTnn5kVsYpNJtPufdjCKcIUhd34IyrV08QQK7EOeuS1-z_8BscfjbPRFu7G_1d-z_EM7xIUQo5jdxcSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwOacFj4mAMef5CArKHaPi9V8qbcukzgmPTdqM-goXnyFzQTBh6XuzU3rUjelJ483sT9mNk0_mwFWiaus48s7GW-9PtLZTzZKKQSf-zrEAfqzodm-0neqI0U4huppvIPIGGTVaMtXyxB1Gt8GjzPZD-qMkCeaRqoCetNE1w-cMbgjhH4YzPVSnBApIqy6kL7yEK0c4HR5zOPdkFTzZSQzyP3p7GAx5ugHoL8QSSQj4ux8vXxUXfTn2pxg86ToGhSimWdK_nxiU7QVTp-lWg7YmVKLSBq0Bf15d86ZJkXW8BOo-08310rn7OisWMCQHlqTlpk8kpoo5lRzYFCQBemgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFecXrIHeIlEtsmETE8bYe1W4JhPt_DAHClhQP_EqMQadgB7lZfr2PJ2n9udo347xo582Z7o5E_DqRRqh6sbXi5pAVrU-90bHZ3S7cx1_yYQR90pMihmMoqu92oRRcvcRM9Zz2pITELgdJgMp_cRPlCsBRBALHlz2O8_4kHUYCY1cihYaYlGAu6q_WPNbzXg2vjGYvi-RYGQoC_qPHC1zHk9iv54-cPCGmqmDQaUR1nDZKLIhZNvJU0S1_2ESXs0OB6-yiXGL_8q3a1wFrVVhdW8rcS2_51MMKpWyC4BuWvybf2AW8hX_L-ntuK0ocmMUCITOHLTKcU2xrg0uET6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLQvMzXUnya479336VNUnR4SQ9s5Hib4mIQ17MaL-hin-lWuV7L8QjJABIW9RGZo1dP_SzK1n4nFWZMkp-8IRzYdYSmZ9kvpMTIPL67AnSOfPb1bI4v5pxeuN_IN2AN5E2RelTiC94OHLjl0RnfMbV8uRKKP-WeHenbVBG3XNboIFHmpe7_bB676AzVifAV1jOosvRGOq_H1ftJ4QQrIelhJ4eU21e4SgXQkTzXYdMVwoJ0U9OSRl-T7odO_uH8nBaLVCg7Ls0Yq_eOJFBEr02rnVWJYOxK6YAiOuOsRHoFVgvExUFWd1SSK6E3uZmd1bt1raRJ-txw8U88HMbAN6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تعداد زیادی از تراستی‌ها کارشان را درست انجام داده‌اند و فقط برخی از آن‌ها تخلف انجام داده‌اند
🔹
کاظمی: بدهی ارزی تراستی‌ها حدود ۱۱ میلیارد یورو است که ۶۸ پرونده برای آن‌ها تشکیل و برای ۴۹ نفر قرار جلب به دادرسی صادر شده است. ۲۲ نفر بازداشت…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/460892" target="_blank">📅 15:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460891">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی ایران، آمریکا را دچار سردرگمی راهبردی کرده است
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/460891" target="_blank">📅 15:08 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
