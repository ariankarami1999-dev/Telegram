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
<img src="https://cdn4.telesco.pe/file/MsfGKxPucBbE4jpfY9X16yL8FQ5n6TGcND3qN0GOFTl1zRqAo3yps14AhyU6CHLmMhIdJZsPc0iiuTH0Q9UcxrEUXp4hu_aQCiYM_GsOUUim9FoJ6X3wAlkLqBmec62g3V36xiQJC8-iXhrZnLwpy4zoMndgnUrlEM8F-hD8M2epZqb6HKVw2MY6T1mCLzRIIDyrtPEhibvvvoAbEAgrSeW1tv31aID3QIn-Iwpe1gtFg01P03PuFjdEZeadwHnQcS4UQy3MxNNHXyO1Q7Y0t7_5fBm8ktF470-XsJv0tvAA7eho4BY5uRi64600PlBVbmxflyR8YwWHFOV4Rrz4QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-15966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://x.com/yasharrapfa?s=11
تویت جدیدم در اکس ، واقعا برام سوأل شده…</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/withyashar/15966" target="_blank">📅 21:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیل معتقد است که حزب‌الله ممکن است ظرف چند روز آینده در پاسخ به توافق چارچوب اسرائیل-لبنان، حملاتی علیه نیروهای دفاعی اسرائیل انجام دهد، طبق گزارش ینت.
اسرائیل برای احتمال تشدید در بخش شمالی آماده می‌شود و اضافه کرده است که انتظار نمی‌رود حزب‌الله «بی‌حرکت بنشیند.»
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/15965" target="_blank">📅 21:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سازمان پخش اسرائیل به نقل از منابع:
ارتش اسرائیل خود را برای عقب‌نشینی از دو منطقه آزمایشی در جنوب لبنان در فردا آماده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/15964" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برق در بیشتر مناطق تهران رفته
@withyashar
🚨</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/15963" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منابع محلی گزارش دادند ارتش اسرائیل عملیات انفجار گسترده‌ای را در شمال شهر رفح در جنوب نوار غزه اجرا کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/withyashar/15962" target="_blank">📅 20:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg6zxT6Z2dVUy-L-sdlhCURlNgRJpaZO78Vwv7CKqXkJRMhVdF1vYoCTPt8R4A3u2RqwibaD8JpD1bytpbCrpDMFsIWLYtigeg9r6mXiUoxfrklASMrlgVpDTAfEp9RbwU0u3o5vOo7WzWyUI6Vga5V7SNQl0jTCehAI-kfflxEqwyHmxSNej-_2z379nwvF45CSDCZMoHLCJrnAtHbu4Y2Oy6HLS1E8Zq4GRsdWz0aV6iqEsA0RaJTJb6LTplNrGrI9chltGw0yDDxhlsoAh6nLwyxMYVoCl7FgPLStcfDDw9EimgibcMfFAhLH0A7pw3ITnq8Z9UW_P_74Cnrd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث :
گویا طلبکارم هست حتما یعنی بار کل دنیا رو دوش خودش و آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/15961" target="_blank">📅 20:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=PKRQhJfw4aQuC5ao8AMVrqX8rWBiMxHYibxcFr4sf-p4Hj1fZPLh3z4aS7KnpMTxbtAEBl1e57Iib76urTmJ62oQTiJ5BQDM58biJqCkybVkf_A50szm1n-IKohvCqDF5Ty-pZNi5O2B0Ulx-xI3HFEo5NMnzrWJLkLzn71DLVPqxbua-ozWgOolNUtXDsUZDLKgJEQKGkq9uPPPolr2aMldmMGQRHxrVACcLJasi-RH2DzjhRIrcZyF9EPRAyJZk_GcYVWTpzGMOZ7o8FGMMBvHKXZM5GxiH5CfWUjZOFaPV1j_7KOLe5g4E_LRv9YmOY9ZcZGGfiRxBtLkb_8Q8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=PKRQhJfw4aQuC5ao8AMVrqX8rWBiMxHYibxcFr4sf-p4Hj1fZPLh3z4aS7KnpMTxbtAEBl1e57Iib76urTmJ62oQTiJ5BQDM58biJqCkybVkf_A50szm1n-IKohvCqDF5Ty-pZNi5O2B0Ulx-xI3HFEo5NMnzrWJLkLzn71DLVPqxbua-ozWgOolNUtXDsUZDLKgJEQKGkq9uPPPolr2aMldmMGQRHxrVACcLJasi-RH2DzjhRIrcZyF9EPRAyJZk_GcYVWTpzGMOZ7o8FGMMBvHKXZM5GxiH5CfWUjZOFaPV1j_7KOLe5g4E_LRv9YmOY9ZcZGGfiRxBtLkb_8Q8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر هوایی از تهران ساعتی‌ پیش
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/15960" target="_blank">📅 19:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مظفری مسئول مراسم خامنه‌ای: احتمالا تشییع جنازه هوایی انجام میشه
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/15959" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/15958" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=S0yAIrf2q6GE0WOA47e2RePYgZIAeKn9J4jlAPREKd8BTQw6HC0ZfkP2sxnAllAJFLyQvRAZv7twcz9xVpXDPeKpXnyDTA1gTKR45_agoRZnlTKXXoLEsDSsz0uS5CKlgzHtjz-rZqZjTy3EyjM9b5_j4KosCF9cIqujqfI3pnWHkgUQNG8-ATdZRLR4ft9AP7AP70mvJwoEXegmJJjrjntc0LsIccHHt13NcMHdZTJkfz0XNHmHQelg-gDmQq8tdYr2RshBsfWsYFQLF0a-kqcLAMNhxhcM2KAkPFgTufOZ5me20py3aa9Z5OZmED4tua3bghfRCQ1cxo4UHww7xU8SLambh40sbo78vc8geCVF2YIpO0V6OgLKMMphRw7R6lNFv0It3LZU1d4kItX7xQPkVgX1PPB5da3j6KzLFYik8ElBCavzqzI6QDW_F8ESwya0nWTtbE_wAY9k-h--HFCHGnUg3kXW1711biOhQVvIvBxm09KHQgCKAuFVhtQwdtctPVahxcKu_uCriBKON1jj61lPD9ZuXv-Po3-FmFn7RFkU1T5eJ9joJKIP9my0GTcq5UcbKCI-yqQ5YeIxW-FvNE2povGzlWRuo-x1CR4S04Seh7r-H6PoyCsgqtI7m0lHyvJHQkkBTXjkHxJGgpz4VqepjXWFaSgun6bfeEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=S0yAIrf2q6GE0WOA47e2RePYgZIAeKn9J4jlAPREKd8BTQw6HC0ZfkP2sxnAllAJFLyQvRAZv7twcz9xVpXDPeKpXnyDTA1gTKR45_agoRZnlTKXXoLEsDSsz0uS5CKlgzHtjz-rZqZjTy3EyjM9b5_j4KosCF9cIqujqfI3pnWHkgUQNG8-ATdZRLR4ft9AP7AP70mvJwoEXegmJJjrjntc0LsIccHHt13NcMHdZTJkfz0XNHmHQelg-gDmQq8tdYr2RshBsfWsYFQLF0a-kqcLAMNhxhcM2KAkPFgTufOZ5me20py3aa9Z5OZmED4tua3bghfRCQ1cxo4UHww7xU8SLambh40sbo78vc8geCVF2YIpO0V6OgLKMMphRw7R6lNFv0It3LZU1d4kItX7xQPkVgX1PPB5da3j6KzLFYik8ElBCavzqzI6QDW_F8ESwya0nWTtbE_wAY9k-h--HFCHGnUg3kXW1711biOhQVvIvBxm09KHQgCKAuFVhtQwdtctPVahxcKu_uCriBKON1jj61lPD9ZuXv-Po3-FmFn7RFkU1T5eJ9joJKIP9my0GTcq5UcbKCI-yqQ5YeIxW-FvNE2povGzlWRuo-x1CR4S04Seh7r-H6PoyCsgqtI7m0lHyvJHQkkBTXjkHxJGgpz4VqepjXWFaSgun6bfeEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و صد افسوس…
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15957" target="_blank">📅 18:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد ، توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15956" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc1i7-zAhIGe_dJ55aTTvNQBYFIJfEnXjEHwtqlStsziQrsPYMXi489A9o7Y1p-BzsHSvWuwDdSFkgwFq3A-QkIVkwRKHVjoh6spkrTkHpYFsBnwzYWyiXVHZs51JYHe8KDa7wYqX-WP-zy9DJBERsdCnsvZ_H5oH3m1S9ezkuRCV_frAzVoKk-Lye7Hk4u1hV3f4lCe4FnMIZlN4hc7g9cNoZzz-d36rOm-CfO4d8VD8I2PibihE-ZonA-dTIGC9_boSaWbC8KZ82ch_Osi_c0_lnh3TMAx2-JySVgKTullrHuOtbvZMx_-xEHJW-2vfQ-sWX16Exj2Z0VzOkSRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : شجاع خلیل زاده اولین بازیکن تاریخ جام جهانیه که بخاطر شادی گل نزده،کارت زرد گرفت @withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15955" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علیرضا حقیر(دبیر) :عامل اصلی خوب نتیجه نگرفتن تیم ملی فوتبال ایرانی‌ها خارج از کشور بودن که باید ادب بشن.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15954" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15953" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-wQiLrufTALtA_UYWWtpND_MUuAN-ZTHUJZsyfz-_pBVBKHaZT5Xo3DHSxru1vpFgS_oRaS7j85TGzhcFeFPzmjaYycj8cANjGDCO0UhpGglNSF7vnhxTFk57S1joslL1aEZ1UjAPzE8EJUEg-a8NT-OGccKSVC6YbNDd8PaRNBjhSqn_PNmmVtHsTWvcwy5MMV1nEeIIt09_x9asMP1O07DclIOxBDMtUTApvQbHcJZURbYL-f5h0sWZhrfpqIba9jYjpxXi4gxKyLjZjhdqyve-hKITl2ra-JN2f7uPyPEk63nsMc9xDGZ2atvU3Hf4AmibZrYA8nGhrfbC5yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده @withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15952" target="_blank">📅 17:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBPmCgVOtsduxr_uT2BimGII4sJ7oSlMNx2edbhibpfGjn2QjwblKeaTf2rcbwYcPOpcwI8i___7-LU5J4Z9fGCJ6baMqYj7YGb91Mdu1gT7veVG5X7FHaqrJThiLAAotdC2ko4jRts5NabWZijCOpI2d0wtH2JGaDCmrjRiDbF1TkPjGIZxtOWRhRXAHgIS7YMqQwfm8S6XOIvuNy0P9qzxiWJgTE9UMMRJsErUX5L_6bM96cGuAkY9U83he7bX3vFd6Oa1Y_o0mhRv3PJkW_aE6cnrR3TGebfykgKlx-FflSdApu3WSfWhUzqof7tKnGUPaSezS3g3ujrXrKmU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پر ریزون الان کرج !! ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/15951" target="_blank">📅 17:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15950" target="_blank">📅 17:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سازمان دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است @withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/15949" target="_blank">📅 17:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پر ریزون الان کرج !!
ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15948" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL2r0V4xOXAHDUdURUPG5ipB2XUowiPC5X5NyEJ8Nk8LQoMz6Ap9YgwkZg6f4mO63hyZLzEZR4VL4j6LSRuuE9b4SgSYb1jXruKQz6D8Vqu1XFG7zbaII66RNPspJm5pRf6-mmLz3yKDb9hBVXk-LtDa5adIdlNHdRg3vHz5VGRkQvt_ql_87DKa6vmGaQy8563Kfz2XIOeDuNj-I-olqWFb9QGwNSOttufBrwI43cSeWY3NkbZq90-hPxvWbB8Gja7rxlB28GmDPj3TIEBtB0s-NUNvB_o09UjgYCIWb5NKKjcxBYIdSCJKoxMiSYDuHnnjSvVdxU1glhmqp44XYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/15946" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بسیار بزرگ هم اکنون کرج
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15945" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdKMVptRikl-Pj000wb-Q8_TUXLm1RkGtE_5Ge1PCcSWZ1l4cBWk8ROsdDQjANxgQ9-r9dDAvhIjnRA9ajmRHz67MGk7AsFoPWXzv_5Eg2ATe74IWYOTQqalAQOZv_Q6L-EGEvi8dRUHo-DAc0vI9kUGmeef5dD54y2FsuRiiRWnZgCnxQRlpXsRzUxK2R-HTbcC3OKpSZNH2dJK3oEpH0NMmpesPEYIyalTaBJ-tyFsh8cJcHbyIqm3w34uRiI4Dd4uD8-80d2vPz879vaSxiZdNBZrzqNvf-94eK-7eNEuNa2MMCS_maWs3Qntu_AYmasWWsF7rXBmcGUNd9VRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز
شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند
شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است
شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15944" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">محسن رضایی:پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15943" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15942" target="_blank">📅 14:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله اسرائیل به النبطیه  در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15941" target="_blank">📅 14:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15940">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
رئیس‌کل دادگستری تهران از صدور حکم ضبط اموالی به‌ارزش بیش از ۲۰۰ هزار میلیارد تومان در پروندهٔ مؤسسهٔ مولی‌الموحدین خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15940" target="_blank">📅 14:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری فارس : ۶ نفر از دانشجویان دانشگاه امیرکبیر به علت آتش زدن پرچم جمهوری اسلامی در تجمعات اسفندماه از دانشگاه اخراج و از تحصیل مجدد برای چند سال محروم شدن.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/15939" target="_blank">📅 13:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برقراری رسمی تجارت ایران و امارات پس از توقف چند ماهه به علت جنگ
معاون خدمات تجاری سازمان توسعه تجارت ایران از فعال‌سازی مجدد مراودات تجاری میان ایران و امارات از مسیر بندر جبل‌علی به عنوان یکی از مهمترین بنادر جنوب خلیج فارس خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15937" target="_blank">📅 13:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3GunpkWm4OguEOCHeemP7VcbiEHpq5qh_RHIeYBWfVexJOKsJ6rxrY6Vs6T9KItwRvJVRlfY693DoeXk5sBchbRd8PdUucerXgT51pknMiRPGVzcR2Re34Yjv4oXFPGESGXKz9_3viigbzDk6m5_TMauW9ef5drdtxc0aR9MLn7VZcqPUXr1z-mjXKXzo9EVm_iSf2rtU9zQmeM9ajUd40_SLYRX0RGmGmmZFhYMLO9qvHv0EUo-JfPI-qcb_cL3z-zutrI1IpHgcgHiP_VDJ6fuvUDc_KkfKeOtTdncWVGxbGWeX0FmqrBDYi4dkWUa_7G-5F0lmRHW8HLX93U3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15936" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15935" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بحرین : صبح امروز جمهوری اسلامی به ما حمله پهپادی کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15934" target="_blank">📅 12:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو دیدم با توجه به لحن و قدرت کلام و گفتن ابتکار در مصاحبه ، خوشحال شدم که این ساعت مردم و خودم میتونیم مستقیم تماس بگیریم و سوالات رو بپرسیم ، ولی الان پرسیدم ازشون و گفتن برنامه از قبل ضبط شده
😕
به هر حال من از هیچ تلاشی برای پرسیدن سوالات شما ، فقط بصورت مستقیم از شخص شاهزاده نا امید نمیشوم و دنبال فرصت دیگر میگردم در نتیجه فکر نکنید که فراموش میکنم و پشت گوش میندارم
🙌🏾
❤️‍🩹
با توجه به اینکه خانم قاضی مراد پیج رو دنبال میکنه ، اول برای ایشون آرزوی موفقیت میکنم و دوم امیدوارم دست کم بخشی از سوالات ما پرسیده شده باشه ، خواهیم دید چه خواهد شد ، دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15933" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارسالی زیاد: یاشار داداش ساعت ۱۱:۵۰ همین الان شیراز صدای انفجار اومد حوالی فرودگاه و پایگاه هوایی شیراز همونجا هم پایگاه پدافندی شیراز هست
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15932" target="_blank">📅 11:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flqPPE33I0luqc0Zh05a8N2Y_gfkHkL6bwpXTJFWjtzkvXKTvAVk2Zp2DM80bfosLNGx9OXnvGxBw7VgFTMUFVlfGDgBAdU5Ousu-U2R8wDx-kMhO16_rF64YyoQt91muuT47K1St_-qieWT8fYVG8SUK_s9wtsDDvhMZImglLIAGBaxdkngdpNiVhbVmrmyFuxzLXQ2WxiFkHn5uxdksNTMlzeVz5YKlMkX5GdAE0KiX28dCDW6KhHFYPXc0UMfCBzgqHCWELPTRft6IShewnw2UrTAvXd2Rs9ZQSou9zjWtlkinTOiKrqtwRLeVoAJDq69tARH-Lmtnr_EtV-tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15931" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صادق خرازی : یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور دوباره قرار گرفته بود و کشته شد ! وی گفت کمال خرازی را به صورت استنشاقی(مثلاً گاز، بخار یا ذرات معلق)در بخش عمومی ترور کردند
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15930" target="_blank">📅 10:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15929">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شبکه PBS News به نقل از یک مقام آمریکایی : ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15929" target="_blank">📅 10:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cfede001.mp4?token=MlLs6EyBLyaWRO9iR1AFlfGXLzcarK3g2CSXkqjxFmnYuVH5epLwv8kiCDTx1lUysLYImSLMUx1e8H8Lv53iM1V7fRhWYhKgchrNCoUiLNQ62AItRcGSh-uHGsD5GO8sqMKTZP8ne3DZPgGQleP9jq-cd0Q9HW5LgVrBJXjFhOqg824Tg1RAOj6IDGo9KIfPz-wqxftXadR32Tg0xxHQtQFUt42F6rV8i2L4aSw9Hh9kv3Nu9TsDjpWMACEavnMXwRhuV43RL30y-4AJ4amHoh-g7H0Bz0HkQiRpyGmTy8kkG8VWLDe5lRYtFmUvFE8GEImaXGr4NX4vdSQ8PtHeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cfede001.mp4?token=MlLs6EyBLyaWRO9iR1AFlfGXLzcarK3g2CSXkqjxFmnYuVH5epLwv8kiCDTx1lUysLYImSLMUx1e8H8Lv53iM1V7fRhWYhKgchrNCoUiLNQ62AItRcGSh-uHGsD5GO8sqMKTZP8ne3DZPgGQleP9jq-cd0Q9HW5LgVrBJXjFhOqg824Tg1RAOj6IDGo9KIfPz-wqxftXadR32Tg0xxHQtQFUt42F6rV8i2L4aSw9Hh9kv3Nu9TsDjpWMACEavnMXwRhuV43RL30y-4AJ4amHoh-g7H0Bz0HkQiRpyGmTy8kkG8VWLDe5lRYtFmUvFE8GEImaXGr4NX4vdSQ8PtHeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران گشت هوایی     Sukhoi Su-24 با دود سیاه معروفش
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15928" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">داداش ، چون دروازه بان جلو بود اون بازیکن جای دروازه بان حساب میشه
@withyashar
Bro, since the keeper was upfield, that player counted as the goalkeeper for the offside rule</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15927" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=dZjUXaTuhH_xeEy9LJnZiO9g463Sp2thd643QtqOtT_FjbGQs8cewppPUA_NmBwJ4uRswEiBjdq1lVKm2oHZ_x3Q_cqGQSlqJtzejB5eWB1-VxwDbSFvA4z-11nowSgS-AcH4QY_tcwYk-zYBwpAa6jOMlmds1aDbitVrNE7_jUnMNUBOXdsFwKDlH_xAKiZw-8zLJu9yL6tCXQbfvb7yI0rPAS-QlborLq56Gmvn5sd7FXMSBiaFUT8Wdss_PQul7jdrBMDLK1V301yLw5NfNz29l0zxN_FRfihRnhTXIctTh6ACxEH6seWPAeCjR1LSBoENeqbjhvpFdadXaBo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=dZjUXaTuhH_xeEy9LJnZiO9g463Sp2thd643QtqOtT_FjbGQs8cewppPUA_NmBwJ4uRswEiBjdq1lVKm2oHZ_x3Q_cqGQSlqJtzejB5eWB1-VxwDbSFvA4z-11nowSgS-AcH4QY_tcwYk-zYBwpAa6jOMlmds1aDbitVrNE7_jUnMNUBOXdsFwKDlH_xAKiZw-8zLJu9yL6tCXQbfvb7yI0rPAS-QlborLq56Gmvn5sd7FXMSBiaFUT8Wdss_PQul7jdrBMDLK1V301yLw5NfNz29l0zxN_FRfihRnhTXIctTh6ACxEH6seWPAeCjR1LSBoENeqbjhvpFdadXaBo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15926" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تیم ملی دوباره از استادیوم به فرودگاه می‌رود!
بازیکنان تیم ملی فوتبال مانند دو بازی قبل ساعتی پس از پایان بازی خود برای بازگشت به تیخوانا عازم فرودگاه خواهند شد.
پرواز تیم ساعت ۳۰ دقیقه بامداد از سیاتل راهی تیخوانا می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15925" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قوه قضائیه: موتورسواری زنان منع شرعی ندارد
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15924" target="_blank">📅 09:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15923" target="_blank">📅 09:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گل مردود شد</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/15922" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJtbc-QDkmJVLVMB5MO81-suSkcjSSwzxq037rkuAL_PbrRAJbAzckHGqYnI13FTX_8I2y2PTXOjbWEEDAjcMz92LxO8CCK8CBsPfyuYYgBXuWEcwA80jpa2Jo5gIAmVK-LRSjO-YFen518sw8yxY42KbPhL_sGR0FIbHt2CkVa9bJLWV6rTnWXe7X3owTAKYP4EMuWRvW-aX2UPeW6PuSDq1EjueNCIOWb6wEmEecMeYd24RpovIwOGIq50bY5dkyTtCeAjuRtrnsVqs5wopO70umhweCiA_Xxo5b30aDSeLl3A8RJQkIFQ3eTdfHSMtiKYKOIO40Zne753cDaAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل‌ به جنین در کرانه باختری
منابع محلی از حمله اسرائیل به روستای «زبوبا» در جنین ، واقع در کرانه باختری خبر دادند.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15921" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOPOSvXh2idwLx2rkbblq3jbK3bNXdixGx10BBkfq4Ze_WXY2nYU_0HivRs9lpeh-XU5zkMsBd05c8yK4Fj5i1S8bTIkMh_XGb8wPubS92j5azLsjPnzgIs56VwgUQBOm2-c9P0_a9AaY6WYeN2fiQfcwhzL2BpmUaNhg3dwQAUP5IY87x56f8aNOTdEpiEjn5LIdzGEaZdsdstLJ2sIVnlJCuKpAW7skTYVUFxyLtIwrd3vUeHcU-bTzEScTq884p1_mpxTdQxckoo9gEdpGbC9zzg6SF7Bn__ivsCbcMg8isYnA6MVA7S3TxN8Nlw0WvjV5QfY_SWBF2XlLxVm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حضور ۹ سوخترسان در‌ منطقه خلیج فارس
@withyashar
🚨</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15920" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پایان دیدار و تساوی جمهوری اسلامی ، مصر
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/15919" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15917">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گل مردود شد</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15917" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15916">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گل در‌دست بررسی برای  آفساید است</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15916" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گل‌برای جمهوری اسلامی ‌خلیل زاده
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15915" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟
رخ دادن یکی از این موارد کافی است:
1-غنا کرواسی را شکست دهد
2-کنگو نتواند ازبکستان را ببرد
3-بازی اتریش و الجزایر برنده داشته باشد
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15914" target="_blank">📅 08:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیوزلند ۱ - بلژیک ۳ @withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15913" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیوزلند ۱ - بلژیک ۳
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/15912" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2894ab2ba.mp4?token=GPN7OK_57WeDL_XoBUoRUIDykVAFnrwRBwth7ayiBY8athzW4cUZYYoRAE_IHqK819eum9yAQZb1afYvn83b6_3k88vSfKhLKt35tIuvG4YCs7f4buHkqxaqqXmHmg-sxpY9zNDSsY_gC2wAyxBWET7_vFlDLFQKHnjwPJmTkPXdm9_JN4AbFXNdXHvX-AsYFYqQmoVDuYXmPzS7tw1iQJqe60d8M24f-7i8QEgHvr8I-Ph6xuHjkz7i2Go94QwIt8X6bVfxW8WYhyx52OntLQ-nLfYkrlnmJeQTUcHUdKFbHp5x2ERIbJziarlSxhzaP79oOFREuPw7rHQrsVcxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2894ab2ba.mp4?token=GPN7OK_57WeDL_XoBUoRUIDykVAFnrwRBwth7ayiBY8athzW4cUZYYoRAE_IHqK819eum9yAQZb1afYvn83b6_3k88vSfKhLKt35tIuvG4YCs7f4buHkqxaqqXmHmg-sxpY9zNDSsY_gC2wAyxBWET7_vFlDLFQKHnjwPJmTkPXdm9_JN4AbFXNdXHvX-AsYFYqQmoVDuYXmPzS7tw1iQJqe60d8M24f-7i8QEgHvr8I-Ph6xuHjkz7i2Go94QwIt8X6bVfxW8WYhyx52OntLQ-nLfYkrlnmJeQTUcHUdKFbHp5x2ERIbJziarlSxhzaP79oOFREuPw7rHQrsVcxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) ویدئویی از لحظات هدف قرار گرفتن شماری از مواضع در ایران را منتشر کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15911" target="_blank">📅 08:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همکنون محمد صلاح تعویض شد
صعود برای مصر‌ حتمی است
لایو : جمهوری اسلامی ۱ ، مصر ۱
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/15910" target="_blank">📅 07:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی : حملات آمریکا حدود ۱ ساعت و ۳۰ دقیقه ادامه داشت.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15909" target="_blank">📅 07:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ونس : ایران توافق آتش‌بس را امضا کرده است. ما به آن احترام گذاشته‌ایم. اگر آنها در مورد نحوه اجرای تفاهم‌نامه اختلاف نظر دارند، می‌توانند تلفن را بردارند.
اما خشونت با خشونت پاسخ داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/15908" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144f492601.mp4?token=YtzduZsHliOOr6wyGV4O-8kaFHT__K7vNPCb5BPlSsQve3gg-TNb0kK3QGVNCkkbW-EO4tYb6eRK-OTm04V5UOEEprzmWSXIg7Yi_NZWAmb2rpswVfTIlPEFnCOKoNwRXR-KcgfX2JW24AVfRZxx7KmvsYXJ_yDftq8SoDLnOCwLriamJpZDfGPluKTsdR-8QwtEWNlEWD4GoJE-RQJtdUermgMJvRHCKMjB9DzqrsT8IpJXvDUD9kWjfSgNQeEFGNf7xmnCwxWrPfvTJ7U23EfnzIAWQ1Iosx_E15fRWqzT1Lksbfrk91kDQ4gBrW7genIbVchWg15uVcKqq198mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144f492601.mp4?token=YtzduZsHliOOr6wyGV4O-8kaFHT__K7vNPCb5BPlSsQve3gg-TNb0kK3QGVNCkkbW-EO4tYb6eRK-OTm04V5UOEEprzmWSXIg7Yi_NZWAmb2rpswVfTIlPEFnCOKoNwRXR-KcgfX2JW24AVfRZxx7KmvsYXJ_yDftq8SoDLnOCwLriamJpZDfGPluKTsdR-8QwtEWNlEWD4GoJE-RQJtdUermgMJvRHCKMjB9DzqrsT8IpJXvDUD9kWjfSgNQeEFGNf7xmnCwxWrPfvTJ7U23EfnzIAWQ1Iosx_E15fRWqzT1Lksbfrk91kDQ4gBrW7genIbVchWg15uVcKqq198mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری تن به تن نیروی های لبنانی و طرفداران حزب‌الله
@withyashar
یاشار:درک به ما چه ولی ، روزهای جالبی در انتظار لبنان است... من خبر لبنان بدم میاد</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15907" target="_blank">📅 01:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.» @withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15906" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه :نگارن نباشید  ما با پیک موتوری میبریم براشون ، قااااررررر قاااااررررررر
😂
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15905" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15904">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مردم : کجا ما تازه برنج خیس کرده بودیم @withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15904" target="_blank">📅 01:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15903">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت. @withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15903" target="_blank">📅 01:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک مقام آمریکایی به «نیویورک تایمز»: حمله به ایران، ازسرگیری عملیات جنگی گسترده، نیست.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15902" target="_blank">📅 01:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت.
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/15901" target="_blank">📅 01:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/15900" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15899" target="_blank">📅 01:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDrOXIwve6I4ODzCBI5CVF3AWeutMxB850qxoNXBmbRxLh8oQHJcgP9BqGL2tYKon_s67UuVKSJODW_wNIw4jkBAtZFzJDNEn1r87HmCAim_1x3rL3JubT_xlTBm5ZjfGrYJWRfxja4Ly-1xK639OdxOXRW9yawgbO8ca9mnCC044nMgf0YAPz2XHDMC1F-I2Mf6FJhiHr-6X9ANX4fFCNWLjsHR-qyc_9XhGbLaiYZrBXygb9Jafhu_2iIbrqX0MmBf2ZhNNhUePdmCqo7DxlEy3i80sAq9pyM3jpbL1pPZqPcqoJHQIpMSk5lRctSBJIaCOK8tt2c1bxar13Slmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ششم تیرماه، روز جشن نیلوفر، (نیلوپر) روز دختر در ایران باستانه
@withyashar
یاشار: این روز رو صمیمانه به تمام دختران سرزمینم تبریک میگم، مخصوصاً خواهران عزیزم در اتاق جنگ که واقعاً من را حمایت کردند. مرسی</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/15898" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15897" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا به یک مکان در مسن قشم بخش شهاب جزیره قشم حمله موشکی کرد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/15896" target="_blank">📅 00:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/15895" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن
@withyashar
🚨</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/15894" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعتراضات طرفداران حزب الله به   امضا صلح با اسرائیل‌
درگیری شدید و ارتش لبنان به سمت معترضان در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/15893" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدای انفجار و جنگنده در مراغه
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/15892" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15891" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدا و سیما:ساعت ۲۳:۱۵ امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.یک منبع آگاه نظامی علت این انفجارها را برخورد یک فروند موشک در محدوده اسکله طاهرویی سیریک اعلام کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش، چندین تیر هشدار از شهرستان سیریک به سمت شناورهای متخلف در تنگه هرمز شلیک شد.همچنین گزارش‌ها حاکی از شلیک دو موشک هشدار دهنده چند ساعت پیش از اطراف کارپان به سمت تنگه هرمز است.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/15890" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز: حملات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/15889" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTAyyyzilsh2DqEas7B7GFKaJ8nVvzb7sqCxX9CnKcOjRhvEEmyPTaU5-UMfwV48CsiM6UiDoebaI9SpSwHBTz8G9PnqGTmkp67U7xbrP-pQcj_6d0D8LXmDCdU3tlBmitWd6gofbgU8QHWSW3-eeI04Jl8UEiuLl1ltz35mFQTgtk8Od8gELknI5HcHROD18OwEJZbZ_RMCsdVbfTheRWKDLPaU0yLcLWYOP2xg25AMnLcgMlZyJnQJzMb6Y5o9lCb0BGFBs7GGv_Ga7U6iw6Xb5NqEZGz2x-DTYInbxUZ-q9OgapToXNZ-cxZw-VS0mcdvntHujnBq7oLsfXEAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :
امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.
سنتکام این حمله را نقض آشکار آتش بس و تهدیدی برای آزادی ناوبری خواند.
نیروهای ایالات متحده به هماهنگی عبور امن برای کشتی های تجاری ادامه می دهند و می گویند که برای اطمینان از رعایت کامل توافق، هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15888" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار آکسیوس : یک مقام آمریکایی به من گفت که ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/15887" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اتاق جنگ با یاشار : همین فرمون بیداریم تا بازی رژیم با مصر …
💥
زارتان زورتانه گویا</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15886" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منابع آگاه : سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/15885" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی @withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15884" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک  احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه  احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن @withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/15883" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/15882" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: من از شلیک دیروز ایران به یک کشتی در تنگه هرمز خوشم نیامد/ آنها نباید این کار را می‌کردند و به زودی پاسخ ما را خواهید دید
خبرنگار: آیا همچنان معتقدید آتش‌بس برقرار است؟
ترامپ: از این خوشم نیامد که آن‌ها دیروز چهار موشک به سمت یک کشتی شلیک کردند. ما سه تا از آن‌ها را ساقط کردیم. آن کشتی متعلق به متحدانمان نبود، اما به هر حال یک کشتی بود؛ یک کشتی بسیار گران‌قیمت. کشتی سالم ماند، اما کمی آسیب دید. آن‌ها نباید چنین کاری بکنند. بنابراین، خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15881" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار به ترامپ : شما گفتید ایران آتش‌بس را نقض کرده است. آیا آنها با عواقبی روبرو خواهند شد؟
ترامپ: خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15880" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارشهای شما به اتاق جنگ : سیریک سپاه سرخور طاهرویی رو زد
گزارش ها نظر بر ‌این هست که پهپاد ها هم امروز از همین مکان شلیک شده بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15879" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15878" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/15877" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB_jtPzBo48cqAc2sRwiccksGK4u7NOBYhIGQkLEJ2KNUCsutSr7iEyx-fp3YShh98pH4PNKe4selliWEm-sq3ViS1y6QGT8UkVkTszH-n90EVnlZmUwO_XDLRAnujH626OKsyJAa265jRaXjbmF9l0cb0rtbVudHyNy2azKSVDdnvTTUupIeuBFciHCdJWUmHgs6V-rBDpHxlF7IwQQb8cad6RMck40QgLoXY_CdmuDXXqiyzoNSQ3aJBRFwsfha-WHPs6M_k9wxupS6CNzQeq0LKWE5PN4BLfz9mMIOJPLpduu5JeddaTXKrBRzCiNiQPU1QbMaovZOlsucKhcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک
احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه
احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/15876" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15875" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هشدار روسیه به سئول درباره تحریکات نظامی با آمریکا علیه کره شمالی
وزارت خارجه روسیه تأکید کرد: اقدامات نظامی کره جنوبی و آمریکا در نزدیکی مرز کره شمالی موجب تشدید تنش‌ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15874" target="_blank">📅 23:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2d413441.mp4?token=IFUWRlQ8x12PMUJg6Mb9U1ESJIRkfSED8ungbyOqkjNFaZ6DgIFV6W6nUJSzicYCS_0se7YYHxhZVgAjsRrl6N8aVucW_bZIHWTEWrQ1fg_DIH0bcgjIsUdjjfkQglvYjs_PMCJjiRd5K-fUOufBZOuO5aZ_lyTUso5QjCdSK9DmOgytd0cGqsCJuAJkejKsoBI86wacL633HFaURhb49d0KzPEvRNlpR8i3n3ukFtR7UF0mVCmutlrw-H515i8d7LQV9675EUyNv64qBRrg631XyKU70-6yTXow_RwUwn-t2v7aXDZ0M7_5LGtSl07asXNzD3Y10uk1hKzLz0glfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2d413441.mp4?token=IFUWRlQ8x12PMUJg6Mb9U1ESJIRkfSED8ungbyOqkjNFaZ6DgIFV6W6nUJSzicYCS_0se7YYHxhZVgAjsRrl6N8aVucW_bZIHWTEWrQ1fg_DIH0bcgjIsUdjjfkQglvYjs_PMCJjiRd5K-fUOufBZOuO5aZ_lyTUso5QjCdSK9DmOgytd0cGqsCJuAJkejKsoBI86wacL633HFaURhb49d0KzPEvRNlpR8i3n3ukFtR7UF0mVCmutlrw-H515i8d7LQV9675EUyNv64qBRrg631XyKU70-6yTXow_RwUwn-t2v7aXDZ0M7_5LGtSl07asXNzD3Y10uk1hKzLz0glfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15873" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: اخبار جعلی گفتند ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
آنها برای رسیدن به توافق لحظه‌شماری می‌کنند.
آنها چیزهای زیادی به ما می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15872" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=FPK4Mw6w75nEmaxRqvhzYYyhFvn-XFI7f6aYEeARQR7aSSiO2v0qztx7Ob1ZCMuzO4siJKMVsDmFwpRMVDS3Zqcyjq1u83MWlUZgSOMTT7LCaMIAgqyHY4o7t6GR58i4ZokJ4OofKZrs0gK2qIiYl8bSvUiGwANZ9OgT_FvZkEVaIKb50w4jAF9o2l_7S41L5MLLa3v7dn87ZAeXComx4Uom3q1H0-lYIv0js0W0UT58QkfTzYTdDwF6FZlK2-P6SJ9cTGPxX8oOLtlcVNF4yCCAVXHv_i0St6i4NR2frto32ls68l_dxZahvWHI2pj8k9QrFdfB9EZZvXckwvLwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=FPK4Mw6w75nEmaxRqvhzYYyhFvn-XFI7f6aYEeARQR7aSSiO2v0qztx7Ob1ZCMuzO4siJKMVsDmFwpRMVDS3Zqcyjq1u83MWlUZgSOMTT7LCaMIAgqyHY4o7t6GR58i4ZokJ4OofKZrs0gK2qIiYl8bSvUiGwANZ9OgT_FvZkEVaIKb50w4jAF9o2l_7S41L5MLLa3v7dn87ZAeXComx4Uom3q1H0-lYIv0js0W0UT58QkfTzYTdDwF6FZlK2-P6SJ9cTGPxX8oOLtlcVNF4yCCAVXHv_i0St6i4NR2frto32ls68l_dxZahvWHI2pj8k9QrFdfB9EZZvXckwvLwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: دیگر هیچ‌کس نمی‌خواهد رهبر ایران باشد.
آنها پرسیدند: «چه کسی دوست دارد رئیس جمهور شود؟» و همه گفتند: «نه، متشکرم.»
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15871" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=BJNlnPc1d2Asrv6S5WeZoLzoxCqT0wL7y037hiv77aVLZm4ylU950-cvATWrAQzsfndjgQMVfditMeC2Q-8NaVUAWv1sOEEFDPgtxFfRy81FrK9gkrwB4yIWFdet1QQh2Q500WGw3qxljK8R470VetAURTB64EczIh0G6S_GfxEUxu8T7bxBzmA00wAAaHB0jSpCE_gHjLDVRqvr_EnwL_wg6uAiGfNf9D9EDZP1Euf3h37w7R_O7nr7TRm-adhg4_j2lB9U_u8JOe0c86zEfxJpas5aR6Yp-3qw-w1heLQecJ63JKASEQE9lBAnYtZEqPNhzFH_bBUs6Tt09CSwoFjbUss3fnSNOFdgnwrv37udKOFU4egdkdOJHHv7h27v_dho5IAJ-IgmC0nWvriMyyHcfT8N7qFLkXTTjfTPDQuHvZ1r77LuSGq2zrFhbJugOqMAOnaye16LdsO4NYdddygAgDjhVKJxFH1d6RPAlGJ0t0Fe-t0wiKNn7HAag_g7TNpxaNDpGLir_M92tWTstO5pz0xTJ8CeqmevjWum5XlBfl-KYmkJDFaD_go990FjYrenyDnh3KSdSxy7SVKp6FpjlRmTOEp2AjxBCdxfpj_wqIff9hNuezNEZ03YbhSa0zHkX-be7HXvEEwJRnA0CFKVTSrDJ2NBgkB6WoUt8h4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=BJNlnPc1d2Asrv6S5WeZoLzoxCqT0wL7y037hiv77aVLZm4ylU950-cvATWrAQzsfndjgQMVfditMeC2Q-8NaVUAWv1sOEEFDPgtxFfRy81FrK9gkrwB4yIWFdet1QQh2Q500WGw3qxljK8R470VetAURTB64EczIh0G6S_GfxEUxu8T7bxBzmA00wAAaHB0jSpCE_gHjLDVRqvr_EnwL_wg6uAiGfNf9D9EDZP1Euf3h37w7R_O7nr7TRm-adhg4_j2lB9U_u8JOe0c86zEfxJpas5aR6Yp-3qw-w1heLQecJ63JKASEQE9lBAnYtZEqPNhzFH_bBUs6Tt09CSwoFjbUss3fnSNOFdgnwrv37udKOFU4egdkdOJHHv7h27v_dho5IAJ-IgmC0nWvriMyyHcfT8N7qFLkXTTjfTPDQuHvZ1r77LuSGq2zrFhbJugOqMAOnaye16LdsO4NYdddygAgDjhVKJxFH1d6RPAlGJ0t0Fe-t0wiKNn7HAag_g7TNpxaNDpGLir_M92tWTstO5pz0xTJ8CeqmevjWum5XlBfl-KYmkJDFaD_go990FjYrenyDnh3KSdSxy7SVKp6FpjlRmTOEp2AjxBCdxfpj_wqIff9hNuezNEZ03YbhSa0zHkX-be7HXvEEwJRnA0CFKVTSrDJ2NBgkB6WoUt8h4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم
«کمونیسم همه‌چیز را نابود می‌کند، اما بسیار آسان است. راستش را بخواهید، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
من اجاره را رایگان می‌کردم. خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی که خانه می‌خواهد، نگران نباشد. فقط خانه‌ای را که می‌خواهید انتخاب کنید. همه غذای رایگان می‌گیرند. از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی خواهند داد. در سال اول، شما محبوب‌ترین فرد هستید.»
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15870" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=Sd3hPtLetcQX-gG73-mKYkXcAQVsrc2HSgozFopUTg8xKQaHUH1gsZlUtsrrBkE_dXrMIMGakpiR49TFMLGf5U12Xmb60QPqSBVcwP_OdrxeVbwD7AmDAW_Mwqi3N08A46h4RlDirefK8EocIQ8lSr3KenaspToReG3efA4viKTrcUeGwHPZjuFWKTeVG7rkEQMKgP-i_erpuID68nH-Qg0loDdwVujYD4aSNShYLNC0-tb1wBqDHuZSwV3pn5ISk0U0CZvjAA20zGqE70mOUaAg1VeXtqKNJ60O0Qoz-Cq0ei2uKu2KEPkAB5Vddry3bfDC3UtMiAS1PzqT2Y6dDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=Sd3hPtLetcQX-gG73-mKYkXcAQVsrc2HSgozFopUTg8xKQaHUH1gsZlUtsrrBkE_dXrMIMGakpiR49TFMLGf5U12Xmb60QPqSBVcwP_OdrxeVbwD7AmDAW_Mwqi3N08A46h4RlDirefK8EocIQ8lSr3KenaspToReG3efA4viKTrcUeGwHPZjuFWKTeVG7rkEQMKgP-i_erpuID68nH-Qg0loDdwVujYD4aSNShYLNC0-tb1wBqDHuZSwV3pn5ISk0U0CZvjAA20zGqE70mOUaAg1VeXtqKNJ60O0Qoz-Cq0ei2uKu2KEPkAB5Vddry3bfDC3UtMiAS1PzqT2Y6dDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
دین درحال رونق گرفتن است
«دین دوباره رونق گرفته است. دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم.»
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/15869" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل در چارچوب توافق تفاهم با لبنان، تا زمان خلع سلاح حزب‌الله در مرزهای خط زرد باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15868" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiakH_-owmWonbnShv9TJIULRita_niQu5mxUA2i5iWi1riMl2-L5m_gpQCLeLp10q6LuHp42hxuVrKBNHCA_hj1JefoK0jW00qpQfSA3ZB-RSyV1PmMymLnLJ8whBT04RP4iYrdx-6dNRL_8qV27a-vxXMpb_A2AkU4NL5uxQ4z89lnxh5PdAQTBS5HrqWwUhPZaPoXeQwHVFyfmPV1gr0nTOB6E22UN1awzauYe7eA-xNkGx92I7Oi_Hj60tkx48ODaD82qgy74LBlm-6lqy4hnIpjg3S4PfrEoP8uRgrpT05NdOqZuFx3wjczD98dxubQ5xLDmiwLxv6cPmozJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : اتش سوزی نزدیک فرودگاه امام لعنت الله
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15867" target="_blank">📅 21:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">افزایش شمار قربانیان دو زلزله‌ ونزوئلا به حدود 600 جان‌باخته و هزاران زخمی و مفقود
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15866" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.  این ادعا هنوز از سوی حزب‌الله تأیید نشده است. @withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15865" target="_blank">📅 20:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد @withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15864" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
