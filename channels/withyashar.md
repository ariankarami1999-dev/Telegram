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
<img src="https://cdn4.telesco.pe/file/sjqaU07aHJT9aIsxjjxmbgbBhJdB-Z006c3Zp3ZZgNKvtpaZhAokryx4QHvxAa6PRAPcD8PmnMjyf1ilKG1CyIt5n4Ky8eD3QmoIcswgBypGEgLczJv3vCdYJmv6vhCaBQIfprnkBq0rAoCxtvLyZvDQt2yek-xybhzhNWxbPHchMk3_Vj485bh5RD9g0U4f5VLpTrDwQeLW0fixQYCDUhDiWJ-gxUeVOpaPp56QgvCIYxcZtWUQ9QrHZV7fm8niKkqsHUWUfhFhr1da2dPzsAxGaC7eVh1mtc4X1zWihxlO8w7J7L-uESNrSgMnqOXeVfWtVRJ53mGtbmUTCXlvIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5Qb9zl5O4UgLEiUTLGlPe7aIhNfDDKTPlOFD1C7yut57YZChNF6MX6DlMQaKQIh88d57ArC1kjCRaxnaYVl3qB0CKXdr66WmYfuLqu0GNv8CcPX5kBshsX_kllVDtKm9oiszDQGXDjKJrHlvMfZ3r7uljsuLG8GWJ5xt9WrhAw46uqh5FBjFAqQ6JkcHCW3mFl3Y_Lznwj8hjhtiRC0BcoOBimLwGn5aaHZT4faHdp-NoI9KXU4FzVnTn7gCnUJhY2_7WNMqSoNnIhvkezld8ndB14UqzYg9dDV5EeAAT46w3huUqcggMDn_sPotLOyNEXogqj3cEalqFho0REcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh48so0K2zxAF92UvjML3Lm_sbCCZX08Jh7k2inLmnga1p2Fz3Zln1sptFsnKPE5ofTDpSiI89mEAsKOJrnkcHnMjtwqeNXW2-UdLSjv_d5qLGw2pspAkb1ZLFZhRp3U-ouePyRsfmlKV219X-fyWc7dXZk9Q8pxXMbeHEA2XWxT4KygYNRIKBsBMHVSG-Zz3g5dosWmjHYwFM3-RwCQymUGHNIvo3-30u4r6jwKMJ1Uy1FTQIjG8RlopZ7XIPeNCsrU3Z-jsGUfPrQFO6wvK6QnbS1aPrvlDcp5TMg7MpHQW_qehFXUniP1FN5W_fcmkY_0Mik7ifya0mGoSD-LWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2U-riMSKWoIlRspRuPqV8_nuLGmqgOE3VoK_PUdX5IDaT2o7XPbMHtWfHTz5PMILZz10Swzdmf57_kU8OSLoeZwgqmZEmygzw4_BqPU-aSKgSxX4pHqs36MHcgifAjRYPMzLkD6eqMu95_N04Es-fUspf0-lfPTk0ADvL3RDL-oHQc1Iqpcj-8ewgGB245_ABNtdh9DEVS6mgzOCh9TWsYmTEpJ7I_9NqfuVGyyl7fXyI6bhSx8AKK-R_JkGqtAl3-rDYyrfp4B5HxLWID9L7JtZ94WTzFojENpAiNINs2qrmcXihP9G7arICo_fLb7nGDySFPvxQ83D9hGMj1KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpgapNDk4n1WjNxr1ivqpRwQBetlG9VzsWg6bkcrM9cgsX4nFZClwYx_FrW3tEKQvDPTPj3Cte2nHh4UJAfIQ5g_WOhQtL8iFkDvEPDQ9UkPw9bC79RXuR38CWZARTulLUsgWSffu6M-pUR0gJfn4Iw1odAqHbC5ajANhx4b5c4_4vf6H673ZukEq451iNhaB4gsSnE9RG-R0NH4KZp1h1t538dM0FyPIQZUxGQ5bie9jSi6l7OSA2xI6defsTV9Ls-SWGOrsTe7ICaWpKC56DEezK-5Zn_RdDiDv42Prh3h12UmJShGlULLHGA0qckCYMqVwsihySly8iFZp-wuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyS4o7qKc4ylwLjniCk2y1CqoQQqNkap_SI-pdwCdqNyeAysYXRtT_dkEJyEq39KKbk0lO0WpKQMdmzTIKrlOhPYSRsoRtAMB_J2R5EFN8Ee1ivimSgXlFaKfPJ6Hmks4devIjN8jcEUTA-P-1MNxZUY9E32zclV6BdagikTliS20b0_ujpm6oYa7R6HYYTkm0IWB0bTC1nsWrXOYVl8azIuMh8lD8zrR77bJbOZT5w9fBTQAQLxxPnRdzT01rkDlcChVJn1wZeI4JvBKQIMAbkWi1S-7xiCbGN0cnWjxgUc7eLAY3jy3y_Mlc6NT9cT6ng1mb4sBywRZAkPOrP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jah-1cPQMBAmvA5PfxhZS7K8dOke__8MyYDsW017rUdRzDsi1eHz0NgnX-23RWohpLmPAMAQXCdodYMwQ0aG-McQ7G21bENwtWHNf2Bcw2jGxL7z9hBbcdaDJRyN6JqpKA7fHX9kwvv0lVqvTF3HxEfP3UXUnEn28XTBvKVFg5PXDGp9QPWxRQJdYGzMBliQJue9C_ZjE7vkpi47vy1Qji2UM2O9pfiMt5pLPtmUGkwnYrUPZ0dnhGdbJPotqM0PPuYC_dKxI86-6Y9Ono-Jwo1zmG23YE8EEJH_XvU37yV-lxNDDd65OxxVfEmKrFZxj1qhP-_cacelus40LRIVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQzQGnop9GX1qdTIWkKXxxQCIWPwxN1-va-cHPac1htjzqoSFR8WzAQ756AkhBoJvGcBDZ_avdwbJAv6XwAU3EXzJF_gqTJPLeu2GuZTrBY5AQI8BC4dxuHWIbAqOYkndryKYZ0hCjILIddb_H1082I6xXSb-9QRHbHgU4dmqGXV9QaPD8qBCKKog1-jq5wLf0zTlM_Z2SA7SDLPiF8YLUcrsrowXmPP-8ND36brcsxyZYXN8i-A_892V2x9rG2CSZrP1kwMCozUiphsu_mpYyQghLl9zkwVVLFYJiu-VbiNHPUB-sL5ox871cD3-zA-DhGGT9Fq3zMEBpsTFYT-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZbRt2l4wrv16uBvYpA7lsz-yhU4k36b7GfIacvb52HuDQZmTQ-2qudGtIpjoumLkTrtG5m3BWo0G5Vxy792Oa_Kkb1W0zzw0KhfmYbIvURHgL5o-FZWIT0GN32GVjd4cYkMdvvd2lJ-Ys3IoVcW4vra3NI2x6_G8Zyp17ajUodix_j0tNdPzBN7D54gdIE97FWJ80qKQQ0wkUSQkXNpHh3-eXcqB5sSS8bWdnz44ugje_sIFWO40Q-ejtZRbh3eK4w0m9TovG9ZQbAshOATF5WLuW_XB8bUNd3ooYhyyZ3Y83tO8nH406gPRuQyGiXxrnKrbzzxv0G5UAIpnPEwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqhQu3CUW8C0iUQLu-skWjyLHdNKg7coRdwpl9aRyA13pXhOcbabp9aUkGBOSZJoZak07JX2tun10LTYHx1XT38O1dwupS5NvUClimDZEm4RiFdRZfhnvczJN2s-dBMPiJNY5v3VZRmflCHFNC0_FcE8P5qsNEboPA_5XgrE9cRW81bNsiEx46xHhgCijCZ2csXc94v3ZoOiAEGoPCNix0fd3LVrUpYcfi3hOinUIHYNzp5krympWnUBjbVOGgbEvMlzSa2WupYq6c1MgChjYK5wheV9b1vCG9qAE0yY3R_VtOkMWO1aKj1Dju0HBUrclSGBEDePFR_U9UFQgNHlqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT8JaqUohsnl4cMC54Zb7bR68dgjsTFmNbMJNFTsELEswqWYaZVTGdQSJ2Tj_fB2TF3bUo7ZnVw6OBvPQiqAvHH3lXaxc4KiZhS08tiOE2f3rs6e7hMzvXNCULOQsCIhPCxnRHTBxE-U70RM9G7Y86mKGZ8L2fyLOST7QUhD1nmNQffH1us7P-0qw7QTaWMBKLVS9d1qKswLzBOOHqQ8_nCWKqnOkib4n1ijiAn5gQlrfi9B74Swo9MzRYpcoo4Eoogv5egoGJbi8Szp2FHVn7C-dkPxbxn-L74Yr3GO4x5Wo27uDfqd6OpTgSBMQ4pEqWMMnvNPT-WIDlG06R2mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4s_nfyC49l-PdEmi31ORWN_H206gh3I_WIq8rCnNtE7dp3a8Mj5BpynxgvQF3Tu5816gyKU8bYJteLJsMEhRdkpbfpnXwoRQ1T6WZap6E5AYyaSOWR_m2clModO8EHfuHNPhre3a9kFopHv1DopZAJlmklPgr9BUypm-OvFhGS9jlvrxwOZj96Kj8rB88U9wioUBeXRaOpYjqUbzbOyl8aFS8CG8Nu76O16Ku7rA0EtGBZjM1cDDX5q5lnXWn6Al93cd3A2p-grjyCNHVgjxSWsw0C2EoCeNuubJet4CQqO0jtW4qxIBApisOyiCWSXq34xNzwwWuuY-o4NI6sVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBipYKfDPqmOklbyvviicWxuY1nbWKrXwyS27GkhX7JGBP_1t5DdMIrlxoXDHC71yawirHanGkpofFXTBpFpByhepH0q0ZURg3kuYNKnpZ5DlJnwc2HQpfjsJZhCPCIJD_AF8BxPhsA6hxAxUeLs6xa34a9drmL-05NqOf8nhh0rufkDIJAWZNUGEnT3pnxKZcrx-3oFjXtCxtDKPERyIu2XXXhG2dhWz6je4_LO9y0mSOt7R4DkKc_fXBSOBN2-nU46caoCOG-_j_WpgvKUaSBtnJ9dHDlH0dmjuxicEiy_HFLiUKJvmbf6PIDLRCt26ApP_ciTzqzFs31Gqz9_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhgusyX1GsfRZfYOTXhWJuEofw7UBsEEBM-imYskrWfbhXNbIPL1G5uFzU7sev9tOpYjSA18y1Hf6Y0AVmpTkWJnrHffm5JFqiYr3i7JDJzIGYAm446PteLVrM-qUa3PxY0kPz32mgtPp3YJetficfj5nvxQZaD59Ts1iZRwqsRxXX0WSpnowfESg_EhYoKrdUVPRXwdK7FUGJuKVbsnH33dAihAgjFgwxiEEDw-BULFA7aJPaRpnKhkjUo_qUu_pyHcZ51Q_8bK7bmmqVFkxGgASYsJj3CJJxKb0QtV7GNU7m2aqUk1TIpjTtHMRZAYBohkGQq6AKgppmhrRhwKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd2TKAoHNnH4UKt-OjOWblIY8xKNzyhygzAJOnJBj43DH5-bshBQc00UBgrvzNf307Jmf1JzlLCT3M_bDtu_FZ-mC0AiZL2lnaslbLXVofrh6-60d9lBQzwKJxEuyrU-GsPwSywY2wwrum9XRjh0oBjUU8lM6bwl3LxykvizuLkE8IORCtVdCew6dlBZw-zeeiEaZq7Xi7T2WrzhCVtlqwx23iehSlgOIUyM_F2G6fxPQaNlVnQzt30zqT0Mae8JJBkeCnqZKx6Cg0JGZk64kNe4gRf7zUycW1x0_sFhElrbhenWJwL_aWRE5POFxTReu53cZpfMB-TjR_aYL9CEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUbMeao9kYITpWX9QZjLGG1W6T4iQSuxAWpcEaxIiSEnmwb4CL1R8jP3ZJfIhxY_NpxEt4lHF5o-SyFhamHnTcmNturaPiQfSHtEPfPvAdgS29OAcC10kInCvwKZL-hUUq2OVBmQaSGU82ImjLjZ3RaZXb9qjMfSiqqc6PDPH9ercjGAEyV1REfosorp-AW2QkIT9VTVnvL1hUxDqmOEnhe-VtPllwR6dJLqF_YuiXCPh73rhoQtJhnacQ_ftWtW40krXy4f29iKhfhJarTfEzvJ6UUnjc0iGtFZIai-EVxbEJgTxx7UDnWzqtCftFo85BFbShNRlToSSi8aAAIipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6YuRsUfouU1JSWKsVT3zL8VQCh8Gpg3zQPrRTZN7EidZd_VocN7B0ukVNiwXaZMR9ML7gcxHTZ8_R6KBQpC_Am3RiHNsgIuR9dw0AKDs_27U0Vt8PorG-XA38vkeAtCG01HNFVVLsel_1OyMf3yLdNmRoD7RcOXi-3HU_nlA3As1NWEKp2yKRZk8PgLuNbdxQD2WmCghnVjlqQZeW-8GggQU9sy-Vc1lS_L53aRCRcSwL0QlLupydHcps0YFXEBm7U2VUqwQzwwQmdPqYLvSuukk61SiZoSEpH3thVsiLGZWPYxIHg0RLZbaksQxWV2eSeurYe9X6iRHOnoKGcEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzlSdnHYGH-DK6aN_Ww84Cjml7d587bIRE68sbV0ZrYlpbatUADujboB5JUcsEHnVN88qbk5-Fc5Cx05Cup7DW3Q0Ej-fYjWssTKY_0zq7GF4I93EjMpIlbFrq_VEyAxzmOVqi8X5_BxXVLvQpPvZ7VPrjWYmAykM93dUC7_aNvmadpvOgplUQyu0e4vugtf2rA9nvYyMHGX0Zx58tVnotmyPBmd-sXIUSvt3djOc_MciURdv5FcBdjq5B17cjyyawToN5V2kLKuC3evFqYlUC2XTHLprGYS9Nm3lxNULkG9cA4_YUMPTSOZHq6UPHSRLwh_5SkVB5L7NG-w4ACycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcSQ8Oa8hCOBJLOTikylXxZ7zH0pkiUO2v-p1xyij3eEPdvjYe9uXbquoo5A9k__S8ZqsiMJP9Vi_jrYKqg8C6fEQ484BM3r0OlZAd8ZbkCtoRuoCLCUYnc_Z1lvmKjnMWzpJBiKIF093fCMZ1C9jfEENjMlxqRrWDNAr1xDoi_2K4sR-c1koveGUdR8aIu0wwQq1kxc1S83FX9uQ99xqU5deHPbR3QLgEe7r4iKxeRQKuIJHHam1ZJEDwzl-X7msko8sjvlRC3s6k5zJZKvgq9c3dixTX75IUhI41ihNNNJy5tMT8_nc4Egob32RBQbpoBkqSML2s-LzznFNcUP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=jDbZIY0JAhMls5ZFTwsOHczmV9nAGZHAX1cos8JIb1EFd9uF4vnnoLdiWgyukqa671383ztZ-7WgmWBevJnBEGrqNgVoBMxlebP-FVPfniQjGhlNXicuJdFkHjdQ4FdavnBz_MLsILBR449CnHuqE8uW8opkwW1e-uUATydxixnPG1o_sIr1E7cO4xCaWtfjly52cudc_1G_lK8ZxiNfsCEokCytp0PH5Za0j5dYJwH4vN-gxknE-rssDdjUEZtXJOzSwpB89fmpCtZd42t9m0yWxi_oqQ6gdG5DS5K9wqM74Ky3T_6jp4fHnCqOpkSBxtpyFrJFPsTBFoJ92ZU6bhbZm538snMlw5_eGU4Kc7RyId_Fx0FSH8XWwXfSOa7MMEsIPn5ikXH30kKAhvunLk40JIq4r1YIFM_628dZOT25PZeWsE_zW-6fXrcpgUDy_EdG4wbIts3E2BFfeyOi3DNu0Di6dJ6Ih5iSvS8AEwe_UP6WLw2SJwUKNIHV5rlMODuHxUyhHNAWuwpx6nDN9igYZ1gN5wIRNx1uQp9fsMvEwFZ7apIjZx1yF7Y8xFBCxsk0arqVR0_-0aE8hyUFOumWdBiSmtf-pOtyfVnqYbohulXrkNOdMbIO4vjb0w0d5iVkoVP0_9BHuOVBJ07gwfbwg7pEZZRjEoqevVtmvmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=jDbZIY0JAhMls5ZFTwsOHczmV9nAGZHAX1cos8JIb1EFd9uF4vnnoLdiWgyukqa671383ztZ-7WgmWBevJnBEGrqNgVoBMxlebP-FVPfniQjGhlNXicuJdFkHjdQ4FdavnBz_MLsILBR449CnHuqE8uW8opkwW1e-uUATydxixnPG1o_sIr1E7cO4xCaWtfjly52cudc_1G_lK8ZxiNfsCEokCytp0PH5Za0j5dYJwH4vN-gxknE-rssDdjUEZtXJOzSwpB89fmpCtZd42t9m0yWxi_oqQ6gdG5DS5K9wqM74Ky3T_6jp4fHnCqOpkSBxtpyFrJFPsTBFoJ92ZU6bhbZm538snMlw5_eGU4Kc7RyId_Fx0FSH8XWwXfSOa7MMEsIPn5ikXH30kKAhvunLk40JIq4r1YIFM_628dZOT25PZeWsE_zW-6fXrcpgUDy_EdG4wbIts3E2BFfeyOi3DNu0Di6dJ6Ih5iSvS8AEwe_UP6WLw2SJwUKNIHV5rlMODuHxUyhHNAWuwpx6nDN9igYZ1gN5wIRNx1uQp9fsMvEwFZ7apIjZx1yF7Y8xFBCxsk0arqVR0_-0aE8hyUFOumWdBiSmtf-pOtyfVnqYbohulXrkNOdMbIO4vjb0w0d5iVkoVP0_9BHuOVBJ07gwfbwg7pEZZRjEoqevVtmvmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2p7QZQ-Pk0Gq-LhCojLouqgkR34tD7c4PN1WkZbXVZBg_YyvdgWMR_hKLji5X9Beg5UjO_1doytsNyIt5GLw9j9HnGznuSKaJ3wHK-_9G5SW8qEW3I1Yl6KlSvo6V9X5Y5epQl9vehjxeimurHaY5NjZFetawf8Lrj6mFypR62slRQgwt0BjEXGCHxwRcTco9iqZ9_Y5WKowZdN6GXt5ScN-KNt8ed6IF1i9_DQ4_X28O4r5WGSUj_puqu56MSK2ubTpIoXk91w9kpJ-xfu3b9xiUHIMli9PAofSijT8k5TE-gadlubz361QzCnTKunRNLLicvPCw1S_DXIHLwtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgmT1dSYbSZnZua2agowPGMc-HfgmU84IK_QobZHUdjXtnKjLNG3v-fkJkMiutzg9lTEyBq4VasZavINbg-YaykzEmjeexNXlkUcAdZxELO9FqocuXprr3h7Qw5cnRCUZQgepqzRhouT-xSXR-DsxLjp8j6dd9tbDcz8ITa1HjYt9z-9Gqq5wYpMkEagFJbOS3ZOChR7y9jAegbqo0VVg7USMwWq-xAn7M4pH_yIYAaZr8pZ4cSoVz-fdaKS4usJ-PZHlxDgWhWmHvSc6pFM77DnktPP7Oano_MaLxOQcvvWKZqCs6QlsYhivubvQzYMkVjV1Kk8MCQocyRkgS9RGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sseBT1OcGcW9Jp4E_H0diBOTSy8ftt6TfNejR23ypaOKk2rMabJmYNHIgzxPCcwwE02K3LBb13EaI4wRIDXyqDXakjHTGZ8QMkl9YeL5wIuX7h36TOGDE2cz2xGPgkgNB1cEOR6SLrqZ_PFQpabCRPHkiISxBAyKpqejowV1tqVQiWb2pOz8JkGEjO-KGmYpV0a0Fv9MiyaWU6R86V_ozh4-Zfo7qU6IX6Vj5m5-u62H6ucJsRoAfahyWlxtzXCXy_XtKZHNKyzJfszcn_1g2HvQNC-2XA7ON4KITOfAQCnyOcztISsx3GnB8-NK4KnfmuhgC4mwHEl5c2pEZ5q5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtKwQj3lcF2a0fWjMsc3koW7Gephvk7Xw4naWTB_eGW4nKTzYVk0yWTuYX7Q0qcj0gWdlLk1rdXRbqp4F3uY4k0B14ink1H8jVBzIm3-SvQBjBn1cJrs9p8kAmFwZnELkcCjCvVOpXEjtx2rWVHY5GLtdCfeMDF8556jK472P3ctrMD3RAYADsu17LU33TRt9rSotQ8tjlhWDz6gOh2aL7EhrWMdfb3_KL1ADo448GEfdmjnev6CX8sBZT9BE2_ubRQKLwOzm-YNznXQyfCjPt_hqfLO5IG1j2GkpyJKhDLpunJK35F5QlIUDrHES3LcKtUelJ_uQQBD-ot8C7Y2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLbIFhwfkmULrj7g4z2JcQVnUAGWcZufA0TNei2Vcj_MSMkdsJnXFFv20jhgvoGYOLV56wJICCC-Uk5HYpbjObuczmYvaaUMWcirkAKf0FVgev9aX9bZQ3erqpM32vkCNTDYzYpHNQjqcBVZt04XHQooQ1GC6-S3-t4GAy1sFdbBm_Q5HJ0TVDNltqSjNDvczxnMRp5uO03yh0LcMSgikbDL9xezXA81kcSC1OyzXHPFsLghiyThc2HQ1M2FHLNKuNLb1q7VPsuBCkdEPVM48392H5z6mB3IqmVSQ8rz2doxjoyaR341VtMeRL0Twrxtztm5YewBgkdOSEi4cX122Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcQ14komGP2tr4Lk-SYC7T1Kh4p-KBiaWxxqeFtDjUt_Nx1rH8l-qIRP1ZYBnYiNGv-KqnNgo36ScWnsWZq1D5jIAHUCPc4cl6mg6kX7-iPMcXSctnTA383dR14YTlpmirLIbM6jj9XhLSLCzcTvGhkivu2BrxC5AKPRBCaa3udWQaBCXChv-VVlH5qNVuY7V0kzi8wMknwa1HNIIrZmm7YrvBEXB1C_C7EMPoRU2HEkcBWqhfhUsnL3ldISwN4mNktzEQP-1hZRWXDQP0Rkg0gqo5vChjRZ8bR9iKSOsPdkWU_Azw9kJB4t-AcRDrUFGpnIpP0NeZpgrJzU_wCjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=lc0qlZr7jY9gA99479M34SLcBYp1hUvCJUtcsl37pft3ofxt59Z49js03ng66w7Sd9hYP385o8PyTJsuM_0UpXN4y2QyULrw3qWRcLhBsYAwMddpa0Dd53IH6NEWOV8X5PQBzVdNPKVLILlMtzINJzUtEQv9flIDpQJA2o7LX6QNLw1i9Pa1miGwXJhg9G-aEWy5hgOAAG-OW0W8DuR4ZBWENedqFL2_YEbro_Regt6cJbZv8HZJ4uDGSi29I2pWbx6peqtFl3LumJmlDPXnHDQ3UraP6Ewv-sPG1EJojEz-QdmTDd39AXQja46921RkCBfvsvSo14Vhdde0M-A4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=lc0qlZr7jY9gA99479M34SLcBYp1hUvCJUtcsl37pft3ofxt59Z49js03ng66w7Sd9hYP385o8PyTJsuM_0UpXN4y2QyULrw3qWRcLhBsYAwMddpa0Dd53IH6NEWOV8X5PQBzVdNPKVLILlMtzINJzUtEQv9flIDpQJA2o7LX6QNLw1i9Pa1miGwXJhg9G-aEWy5hgOAAG-OW0W8DuR4ZBWENedqFL2_YEbro_Regt6cJbZv8HZJ4uDGSi29I2pWbx6peqtFl3LumJmlDPXnHDQ3UraP6Ewv-sPG1EJojEz-QdmTDd39AXQja46921RkCBfvsvSo14Vhdde0M-A4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=i4Q8L0vkMSThu411f5wYEpYScwpjVoXYiDe6I-W7d4Tt0SOPwdd9Vnv3KlrZtS8i0Y6-uId8TErp_5yEiw9ajufuECKe05JabHD3eHMmSGV0pYBM08VBRPz0pIaT3iOGB7Dj-0KCc4vZXWe_7T3FnHnG94GHIrA2DH3iIj2DeFn4QmQmMgZaal8OpB9gRRge7ZFP7Ng3cvC78S1B4B6UWlphc6f-KLze55k96xJfOkx3pk8VkiG2aLemM-mJO1L-SBRLHfMnw7OdOiwqYulNMBkvtpqW54-BhrCrS1TFl5z-82hytz-nfhDzi4IK4rMJHIB8me9fZCB-a3cC-uj-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=i4Q8L0vkMSThu411f5wYEpYScwpjVoXYiDe6I-W7d4Tt0SOPwdd9Vnv3KlrZtS8i0Y6-uId8TErp_5yEiw9ajufuECKe05JabHD3eHMmSGV0pYBM08VBRPz0pIaT3iOGB7Dj-0KCc4vZXWe_7T3FnHnG94GHIrA2DH3iIj2DeFn4QmQmMgZaal8OpB9gRRge7ZFP7Ng3cvC78S1B4B6UWlphc6f-KLze55k96xJfOkx3pk8VkiG2aLemM-mJO1L-SBRLHfMnw7OdOiwqYulNMBkvtpqW54-BhrCrS1TFl5z-82hytz-nfhDzi4IK4rMJHIB8me9fZCB-a3cC-uj-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cohptstzVjR_UuPnPQEnSuly4klKJhxCPUjihFy7TmOgyZKs6OxFg3TQerBYA1ZEY4sb2p851-SkiMd5J2Bg1vuhv74Ad23mw4iiYx9GVW5gBULrl5EWKhr9GDz5BMr4i0xaT1NNBSFKrrruBHx28OGwfxAQW6wSX4wGy9hCIliEDYHq_E4nn_uroAU4cjfSwLEpJkd6ZSiq4q3u9Vp2-Yq2t3AeKLPGnU4tJ18hZT3uX-cWjFbGk3KheYXDjKGSzwV8oV1G80KRZ5wyJSGjupyfrowpn1g5M6ypvgx9G__eAcz-XlU0Jxg6lRmhMWc2numK7VZm5dvtPOgdTjFLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng4g15Gh_D703actng0o4pHTO3au6G4tf4uHMVlDsnb6e15YlNHpOGRuIdR-efbCE8j5L6aZGOGavWMG43RTtyH5cXO3Wh-nuWm4rGbEd1cpIpBIyZzu0p19a7HgFfwGD1cAW1shB82jWYvNuNnyESN8lvhST0Yjr9mG1zT7TpaO7lZc5B2PJvqakSffKMipJ31qprUC0k6TIqZ0rmBtd1bnwuNzEihpRkrbU7TtD7v7rWWfj3GPaJmqATe-uH8MeTWuY4BTdv0YD0-M8JcMxnmRJI4q39pL_r4g9ompCe31x7rCyl9k17mixTaJrfm4Do8we_MdiULFyqE_ih_YTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=jl93W--2_Pd2cs6VAGYVZ5VV_rn7yXZqYwr0LW95fk8K6DoojOCIQ7332T7GMk3676H45jHspw2fPzHQ4PQVJDbfkF3OfviZ5xWLjh4JA_y0kwztvx83L2GFuH5062yc27-zr7SHaS288cwfp7r7ldnZnVb4qvVS0O22ieP3fDsYBP_TqWWjFajvw1XSHg0urKqmhUkPjTrIgu7T6zomcYkMjhPSLHP_pUJQRRI0d1Tb0TmEXRtxhg272EUaphYwe637yWpp24wxuGFhgOYZc8q6f_oXhhg4PLEZJDW34gp7_55OwZ7lHkYRRBoRLteXHwKjWOBxwgaoUJ1G1GADfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=jl93W--2_Pd2cs6VAGYVZ5VV_rn7yXZqYwr0LW95fk8K6DoojOCIQ7332T7GMk3676H45jHspw2fPzHQ4PQVJDbfkF3OfviZ5xWLjh4JA_y0kwztvx83L2GFuH5062yc27-zr7SHaS288cwfp7r7ldnZnVb4qvVS0O22ieP3fDsYBP_TqWWjFajvw1XSHg0urKqmhUkPjTrIgu7T6zomcYkMjhPSLHP_pUJQRRI0d1Tb0TmEXRtxhg272EUaphYwe637yWpp24wxuGFhgOYZc8q6f_oXhhg4PLEZJDW34gp7_55OwZ7lHkYRRBoRLteXHwKjWOBxwgaoUJ1G1GADfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSuM4QnApLj8dpXdlWpH5nvDpJXRZM_8RIlX-QOXVKB5ANwXe0nKWt1B117PTlMryChzGXRUZbMxDTDkOpCH-4pepV8_RLSVUKUbykK3XrV6bPGRpgQSxpUHtXEwokgvWbWZvnMN77tKHA_5U4-MPI3QprJi-4PqPsIVGkTJ-wyhgDW4ymLL9kz75PRnx2Fq3BYCVWmqkQnV6_3DrsvGmixWKlLUaU2ihCzOFaIegc0SEJLzOzv1xptQXI6vdyWDI3ulLeMdkR1R9Ph4x065loQKkA1qhZnVLtCyQV5gAjGngA4jZJf2sh54ZNHsCETYBBZaXG8MbAzFL397IKk3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYflQd3scXcrKXT8fsuH77GZrzzFJohbWzhc1YI9axgUpJ0zj4Lm4Vl15YwfitF1gXen9UQU6dUy3ysUiHZTnYktfqQ1cHQevJfwxmmaoWBD1_VBwf5L421daBLneQPf37dND1u-4P21_7ogxvygkO-HQDB_N-p7RUPqq6CfQB7EmM-jML5SIXsy31OPHr2KnAbCpFCgtz5Pzbydyxp5h14H1QG5mZeg_vb5SpcQyGUFcRML1NdpJ2B3Es1QZXNwy-dFihVVroIUv2X43CACQgmkIOgM2NWG-WfORC8LCzgZ5wkfrnuUUfG-ovomLceZgHDgzo5UF0xuuyCVh50QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2ras4liptyWq1EK0K3UxkDQXuR4XjJcFT87C4ro5eYCS5pi-RtJV-giRuO0Zh0-RSyafm3GuBpN1Vcmoh0Ky2yc8Re27OMWAiaaEZOB91ZNr4llunCscQzYb0tcyi0VR8w9hNh2teTv9B6zjdfWQwdbreCFGLkTEXaVJ-T1rRgMZR2kAsKoQh_cnlJhM4Bg2wMK8CKFt1j2eeXcWofScvEmQDTBV2_hADJEkaLeWSxG1ISgrBsK5FtMP-q3IAHTOf2SsNwyygO-rpTgXw2V7AJ7cyRQJhtnKNN5CqtxleoGqYybv9QNl0P9GH5vxBNusFzv6_AYMb7I_KjU-zyfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4l5lgt0hSCo-K3_OvGh9qiaYaFHEVTBnandUq9w6hS_77zSAa1nscJ98wYGzRO0CIq0cPR4-swVk4nNbLbMOCXpJ_0Xxto12GsofYnKz1lkPMDWRNtoCxzpr5HfDur225-tR6lAxcKUtrd5dqb8mH5LcQpeoGoxvE2tlhkI7GE6Eh8PLH8FN0NT6LolV76ZDpjrY_QRlHLStNPhhiNWYe6bJbL6PkY-8kPU1TZLASN-451CzpMRg0jx4jDYnevcP70ZaUztocc6vBOKOuyWtmeNPc2Ut_JJo6ng7gAb3F_JgCweXH24J1-kShoiibNpSFIKgLn89TPSuJvCqVqHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=aWPZfR_q4xABKMKOgiAIOqSCkP4pC2PaPhjnJg6g1UwEwhqUdBGlQw7xXVsY8rKdTjGsYn_U9Mva00AcxNwW0iLWA7KKYz0xJVv69Sk-XGHhJn66JXnrThCq5cC8v5FOzogOtNTJI0-cXP7MIo242r8UvrPnR5JFyM-mQQNwtWCiNdD92xc3nc0JcFwVyuUvkiPj-naugvue7Cw0yKUnV4GkQEW78kX2z5deeq6d3Jd75DvuA_z70eTrXnWc6JtPvDCOEieS0UwGdfTn1ZgklraH-ZllF_6k-VO7QHdgIdHut9mMsHtwnGmqaCKU4SQgdDxEJJ0k55bjXu2yxqae7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=aWPZfR_q4xABKMKOgiAIOqSCkP4pC2PaPhjnJg6g1UwEwhqUdBGlQw7xXVsY8rKdTjGsYn_U9Mva00AcxNwW0iLWA7KKYz0xJVv69Sk-XGHhJn66JXnrThCq5cC8v5FOzogOtNTJI0-cXP7MIo242r8UvrPnR5JFyM-mQQNwtWCiNdD92xc3nc0JcFwVyuUvkiPj-naugvue7Cw0yKUnV4GkQEW78kX2z5deeq6d3Jd75DvuA_z70eTrXnWc6JtPvDCOEieS0UwGdfTn1ZgklraH-ZllF_6k-VO7QHdgIdHut9mMsHtwnGmqaCKU4SQgdDxEJJ0k55bjXu2yxqae7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=CkPKm1Ns4uMp8frW8WhqezfJiOSp24LYDO816xNC99wPLzZKZH7Y_TtVCt5gbnFJUsn0XNjJUUGDhuQU7lViQbsuwgdn0PzlhGgL4WPS84U8sghZnqQj56oCXdpK7BAYZt5cQPlEzUrg1gMqmToKZSsLZkXveAhVaBhu5j1kai9bu88n4UwY3O5QoNUumUW5d1-ycYuY4ZeBIkDmbrBzKHGuzqBKKG67KvhCwyiQUw9_MNBSmsPG-5QFo1GRGFmzy5LHyMOYVJxGbHxQO8EMAbSwU5wvfyEsUSrkYauQNZ7-IfJ0f_TIqUO4OkYygFD3apTg8jM4VcQVX089nicK7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=CkPKm1Ns4uMp8frW8WhqezfJiOSp24LYDO816xNC99wPLzZKZH7Y_TtVCt5gbnFJUsn0XNjJUUGDhuQU7lViQbsuwgdn0PzlhGgL4WPS84U8sghZnqQj56oCXdpK7BAYZt5cQPlEzUrg1gMqmToKZSsLZkXveAhVaBhu5j1kai9bu88n4UwY3O5QoNUumUW5d1-ycYuY4ZeBIkDmbrBzKHGuzqBKKG67KvhCwyiQUw9_MNBSmsPG-5QFo1GRGFmzy5LHyMOYVJxGbHxQO8EMAbSwU5wvfyEsUSrkYauQNZ7-IfJ0f_TIqUO4OkYygFD3apTg8jM4VcQVX089nicK7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIqCy-fXDzlgezaXWIjsXLDIKhwAYqv-T8JWPzNeCODwCSroQbEo5dWhTQxxH9Ip_8IQK54MnuS23ilr7kCFKoQevFrIb-mcxgh-90QnvKDLie6DOCBbG_fmSThh1NM6X2Kt8EiGmMqYNsjfAvqpVlgUVpPWK3mcRGgOlSs5n7DjmBYem0zY1kmBI8XlBGcgJ_dHYF26f49uLqoa772E_iAhtYUgD9Dmo-vujnUHVwkqnI3-J5VjgZ9_Dpjitv2eMZEJiNXFxC4wABdNOD5b5A3zEW11lrwwps_i2gaWNh6f3CxgJNxtlObmekVzPU4PzMpigPYFMSwL5U0CQbVtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
