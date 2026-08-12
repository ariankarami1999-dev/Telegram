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
<img src="https://cdn4.telesco.pe/file/uyYRkaWMvZu9kuh9YKWQL5nHcb_Gx-4OVgOUQ4zAC0hKUVaIYCf5jyB20HKE06Fd_YX8_LHo_VWR2hLh4eC7OJV24LMZ5MLg42CwgotgtjyogtG5qXshHvE3k0Avj-NMNHf2KP8lRZhZ1fzpbBPzp5sOIj7zBq-1yjzycgcFCiee_EyHbIv9AELSDVVPcEDrV5LvLKbmkAvJb3Q3-oVJrkLd0D2lT9ryPRiGGXNYAP-jGbZ56JB20iEliCiUH0qrUumqmRHNs6VH6fXQaUcb8VACa8MD7sxYjsCQ_MuxEpkV-6FusoYv67uw4Xr9ftv1znVYa2Ou9XI-AXEGNqEUSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 13:06:38</div>
<hr>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiHqTncLMcVCYwxMl-j93H2FzLgHXt9HwjCEdCs_2cLvWaE7Y8WjBHUn3tp5UstsGGXLwdFNPOisB3ZohunAGN4EtAbM32ck19Mq0JXpiMlmXxJgY8NyzUpSsCEGjg3YldByJLBTkvdbrVZWCKlE3jrYBp8sNjOjBbOQtxCRnIlhPvlZ-X0TNylbWj17dIArYXrIfBvyaAHN_cJn3GdkNC6KjxoxcBmVHZljGihQm4r_tnLfxkaOJh4u_s3RxCbbPpYNILW318-usuorvMdk8KOKG9boHAbGZrZo74wtxxhm41HwZR8HfQ779usGRnzT1AEZuJcMMCI0dHsXsOkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuE3ELj_i-FK16QcAqNud84zrIlJCXnV4JBeo5NohIz3ozW1AIzH9LvhVNMPcEi5HUFQPu70HPK6VPy8_2sAgaHfhx30kiHBJlra0yG1ujah9Q-t-_XWNlEURCNahxT1gvtsxoml7TKF1futkAsLtAsLjHYPgo6KznH5U7qmE5L92UpW_x2pHmkb31veu7aNKhrJ7rjmNSmYHDS15aL1Dqp8Gnx6cI2WPtOryLF1PMYfRGCoDrRdJBHAvkIGpsah70Q-cP5v6duYgJvG5QaY1o-xmQnJHAdUN0h8kYrRqpiuc18jZGXl7wtcAYKeuojNwFPjuuEUVLP3Xqn1a8rfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQnsg-nraAx5n0o20o_l4loAG9fVpqwAkiuSjYVx95sdM4y3CFAeRJ-lCqKoFDtoGYE9J5lDcsQcZhAqtJoY5Mgnu7hhDFJq7SSdncdkrlWcLLegNqsCSoydWvRCHy9joHwHQz2s924hNpWr9N1o_kyrmGknNdBUUAIX0-MlE9sS1p3JIaK7asJWA1UpLMZpsCyKne6aNnScU_kC8S_jmF5SZugGc3Tch7AkZWKgdyCXHOlqXJT24FTr8TvOpZbmouj0DJnqWqbn9FlLk1hG6KJ80JZNOCtcXGfvSLSTYW5WL1UkAizjVFrqtkpkJq6CF7CGuXOCp4A-NxhT23QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNW5oIcKsYbwEOQZqfJYJxrqf8eLU7DXhCQHOARlVQIO0UozW2XCwPsYa10pxRn72-NysQo-LkFAEb3ejQ7TP_z1gzw4Nzb19xsYyQ8hms4k9Bd4dQvFGp_fnU4fVF99eLHLkIzbIsbJW4cCXjjmEsq182YRjEwtBUlQ9pf3b5FIvGZOVWuaDpF7yoTEBkxxzowawUkyLqgoaaXY9wc7yHm3RGc_KkbXfqROSvKx3e0ecLjux_ERbkqvUgFEzgO2Te7HIhasbRwAQYBHz6QF29EE6uNzKGajRtt5cyBDadpB5ZLE3g5SKtgHZ7P8snya0FQ16hFmaX9_-Zu0SxXhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nto7IK_lgOhNJe2uc2mu5C4H3V5I9M7iqrx7A6utf78qA9QlfeYwf5nRujXMxWSiZOANQJjI4MtAe1hzEZ7TVZerw5DGzIj4Gu7GeZto6eMVAcHbu6Wq8FRNuh9rY4eRhcPJXjavD6gXTrxWseMm7gRPm5gB5uD-bPM_SiR3Qf_zYD6HEs8AmRk2BfzHcAtcNCZt0MNCe7hhdM39a4S-JhLPZfiIZh15NN9eCIVupsT-JPSYUBf1CtrpC1_KJEo1Bddns9-2ipjzHFVtdgn2acgpXJJo0gVp1g7Rv_X-URq6WHoniIH8g6mzPkIRoYvww87dF_Dx6rj7KWkQ-_-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch3uTWBc0w-xy80GWTBNt8u_iNkooBUwCH17kNVKC2UF-AMMuPexXOqH21XOfDu_nfOpSfHrvpa9K11-OGXhsIOFOvqlOeneMtKgUb_bsuQhJ5QiG03pafEV7Hpq3aih98jWEy-gGwU78ljAzMU21UdQMCaudxZrFxRPfUKp50VYvZzqNd4pJGgJPxZGRWZHw-6Trg9CgCY-kbLzqWJ4WiZAWZmnU-BNVfwbmBXNP9Nr2njBS06Lk4ER0PpV17Q0M3Kqr2_J1WWMIXuoIg8gU99J7SWEZ_sFRaeL6WE56XF7MI0KeImPnrT2d7shcd2TBj5V87jInECvDOpkSY1YSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v31WyMptgYfZRzIqhO_IB7L8Gyy7OFx1a8B8cA6VwTMIsHcC8CV_dkjBIqrRIE6usiSXls2y4GMfbJQ-34KP8QZ0cNeJqEnA8Ae59xdyUX1FmcmcxGMj_fs4RU4ezUJ5J0YbH6J10E9sUedYDJtfvrGFgljofK1R7UKtkgc9ne3aXQROH0p0SgRaAGa_GZYm6bNVVH1T-dWBZkTuxcfpfksdHvmhLXjQW4VNi949e39cPY08GOJ29AQdAhVYE6YKbc8sRnQ7QO-jpgviGDdygvRgb-lVzzQfawr-NvJA5Bt9HFUkEKyiY7Tmmj1HDH4VAaeZk6xeddyVjaV-U4cBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWLZ8HV115EvUQp5SQDjjx-MGSekB5cCc3dhAmSrmiaC73RnQ5vfi-RKIQu6niN0lEwkN7UFoyuURuq7N9LuA3Dz5gagXWiGPbA47Dnt_8kK7dcLH2_Hn4TXpJzKO85f9RkPnpdbWQl6-rSnTRm2uo_GLv02XZNR0XpshzSUV50NoHDAfmpaHLyPj1ulux16c4mtIX5PWPTm3vqnOPpmK67_CxjLHHfYJY4OmZes4n2u0oNgfQ2dEWMW5qdL7NF_LXWGp-cy1LJLQc32VS0oyJAx8JsFZ7K9L51VFCZlFrXJXQdRg32P6NRD20V8ldplpt4EMKkPk2j1HwMtUrTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgRm-lwBmranb387ZLOd-WL_0gIG1ZeqO8W-cFmi4D5XDYBtb3og1arQeAJ7GPeMJkrD2Wb_LJcbRVkH85V5BHW9cKCH_YDk8ZpQBfI-FAxZzS9RoDrTytA5eNTogsAvK5KhlDgGFf6SCcAEwfY071hQc9NGTDI4bu1Gz2yCz08TMXLukXFCAnmdWrQnbcNH2M7XVlSBF_jdcypWkVOgjz2r0m4TTnfQYor4nTkp6uqKUsb0-VChnvCnUHTvRL-L1QS8FOgOtCkmH20TQeljORcUEz9T1ZflkPdCpXbzGTERYcCj7yRpyl6YXoPCEhQTpaqqB59XbiqIF1sBUf4-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEk8JkR0rTvTv5Kh6A_UruZNMFYgYTugf-hmP19LfDMECxyP668bP-sTjZscbaknTVaF9fDUb3skA3OSPzqky6B26eDYzSLbfLl1gNq4mc56EsKQeGimaLZVNeJzpH_QELYWUzRNT3RZ2pWmKPBW0UnL6fIgzdg_6qvPeeKfERTLc77aUv0ut24Uo5iwuPs0IZjAtbcjdMkjAB3yutKyBFMbyu_nN_Rs99SiecMBIoMy2ky7KROfwA26WF7-L6uAA9QbVs0N6AoJM-MlGQ_BHJ1bl0Y6WvxFGRSupehWdkTiuoDc5lokCwvdZRfA4KXfWgjp_pX6ZAcgAm3udF5Sow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIly9VknKn6pViGsUQbC-PlVOLo6vL1UltMpzX1ntZNmHf387SrgcBJdZzQNCp8CcSGVRSs0wHAv18IFDpxW9sWD9StDnhWsiYNTP6z5ucEv1jb5o3HeeOondMJgjTM9hOT1h82enQD27SAiDFnhF5BzRYelG8WUCnxLmlefODrkWUf4o_8i-goE_0d1jL6r1pE20tW0_HIgquFxydT8L-Dz-D8X6UyC10RZcgzSzLmMBB9A1BC-NJ7Ftrtq761GMOlluJ1D64jQoE8urx8p1d6yKzGte6ChA6OwMXwf6FLddIJN-gni4cxQmRSyfNhxxJTNC5QLMiaMayQ0S5MCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh8D2xOVAP7Or_u76l2FxY02OTlXgDAZP2jAo3XEOiDFfzfYC5d2zdJ-y4kbGCfEiliJXSsTkE2qBjYzXL7oS9hSpUY6js3gXbmrg1nTDWmOwudVo-f1zkLIU-Y59sAyTT94s0efak5UeY5SwJnQaeUAH_y4r79-EY5R87pRhgKco7MvReT2j98G-Q-JGwAEsTgS7p3EHSosMqA40Qud7M2S076I0oMTxgIpCOSfYAWzRWpgcn9pqHiMbsZTFQxc54vUhm9V8h8ZlGr05sKYgZTUqMXTVBMTfruf04rcWyequ6KgTo-g2EyhNd5ztdSHYcxjjc-n97lv5eNRLbuu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqJepWBzbOfirBJZjZf7FcB9uOKdrbc2agOzzQzRz3QPC_epGlAtSRdITOiIxoBC7eIfWirkFhSs3bDlmqfNnGO_iIelxq1cSeOaq0mNuRrnL3TxDYGcN9I1upmLx46vLQYjZjSkGNc_BcJBE2JoADBpF-keDP4UaEXWsV7WjeB6yH97yn3tCMAUZILMy26Dc62Pz-B1Sco30_XafC85tzEz515t3TGbTY2SA31R4gQro84UoQfjabUba0CmRi3xKZ6ooLdYPLE-Nc9ZqTmSdPzBsa8AEUFgUX_Wfd_rn775hEz6sPIf9HblKiIOy01OqA7IhCt_kEXeBKFOzbT5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-QZkilT6RQW_sWiL4RKZTLe2zsmWTcsB_bPodcUQall6Dkbsxm3QPwjq_DjVg_fRYTBoO_I3tgnRUig9hllr0xgSbJyiWRgVJndLeMegCINpK3rzrOWHF8P6FN_HmyqUQGR-lGPh041S-2VTRNBWSivJ7aZufsEOqwha4SzRaYC6xRHeoq4VmOOmI67kaQfLfDhjhN24nALz1vlb4Zopo2pOlt0OCorJ9nitCz_TNpl0FBh9jw2esQiEo0b0RQbvMddSHuDtwJ2lknOLABt6C1PN-jfjzjtQnKHFIE9LR2MVAZTs4bzSQIzStjzuH577oqlzSFZFP4OUGmJIG3LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57Aw0qXC6wxngR9FP779GuAtR5PXaO12aSdo1FIXSIqGlY3pkjwIoxomOn9x4TpycIDPRYcPBUVcF-55rroogJLgQ7Kvi4ZEPH4xXP6klXFGxMFeewkOntMl5OPtMPHASb8U4IP7zsio-P6nNhGWzngGmhYg4fMqJ7i0nGwUxcReVbaKUVWKmCp3aaBGhrHE1GIYh0kf21wm80XerXvsvwRrNsbGJIXLtEJjIxDSi43BizIK5s4F2HJukiLfDsxQAp17X6aHuM9m0sU0hvoMcS-BpTTEKLtMpvceDKUGPIO3EOY64CIzhBAUMap09m3apnwOj5svGK0GyGrFXhzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue7JlZe3d5lfkjtemBm5lzYnJcEsuM6pfgI3Ved-5UqpxpO69UAMga3o8TZ7Kn_Ldszrx2IFrbq8AHELUsju9w5rqD2_KfBZNIH7M0a5Ios6hishNi4WsALUdHtKMZ77EtewuAHupHQkfUonKiLQLLic_O2ZsmrkbrtVOStcaoSowxACjrmiqzN7OmU5Ej97C0CrVZCrhQmoTYBUOpnNZiDqnA-zSy3E_YBjlBqoEM1CI14XV2rsLvGudLtsWdlkNOvv56AT6oAfRMtoQ1wjIXgK9wsfwSqsZOdEYH7X8TLkh8STmEUIZm6cZ1wXOv0ONyv8WSTJaPy-olfHUbFLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-FT3mgO4jYBaMJH9IgHpuxZvm5tYpBZElPGQfTOWvQNV8rhhSf599z1WwyIF1GnQ9bL7RqGoNYCbZcvSM7082yYev2hZlopoMqYfV2rF7bouR70SfplbHQYI8w_7Hq2g0J99FLZ5cJCP4nXi3w8DjaLgyCgzxWmmSA0mv-Pp2rBQYPSEywiolbr2f3ZMs2rSoc_noLyRQh_pnrGujVLEJiD5IVqj5jbnlLwgXf3_vMDwqwk-Nw80BN8GbThcYdEICZj1mrG7W2h8-0Og1MoL6cvVasfSHUEdF111FtcciwiRWyLm21ObNHK5mCIDq8BMDUWOfDTBYuRUTIM3GIzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYj-rne6dCfIxbn1wICvGFmfpE8s4LyIV4ApKFmroa2ScUTAcfxzVatK0vzxHYkdC0TsCv4u5diKpusIJ45_fzfpUxHZYB34qzk_nPLt2C4givGBh8m_cjWGfZjWuDIZoKLkxYzZv92OC2mlMMD5Hu6EqWKoFlAtATJ9V2nz8y-uqljboGFzKhDISUFubKtMrAXEYAXvlWeks71ohR5m-r_c6FPzGh-RgY2-SXoedoilMM9bK43YF47EN2g_nEJMlUNbEesnGJaJ1xGOCismAEmmCjc-EiFOaAb-0hWI7ubFwZYUL5ipcnIATVy9HnK2uaOPfPafEgigRaO1k-MT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbSV7noVWtJbPo0llB9tYqspmu9OsUbYnAM0cTQ88gG-gU1n2ayowQXA7n0G4jpo5H7F54DIIObu-u2bWfZyHvhCiBFsRlo264S9OGrgMGEF8-_ALKHSozK03Ti3saurJR7yGTF83JgpRtbAHEGSrHPlXP5K6H_7lQBvUGqww-kCLpX1-qyl4CVaW6Gqd9cK0LZOOeHsc2G3se-K53fxrc0klTkeH4ge9EvCTdt3M0IsRoP8XBFm4ij7ZBnwemf-qFQ66tr2086sSNxa0jIJx7HURHrcO23qMyuGeAnoX2rRoc92ptQGIS1m7B90-lf95dwbSC9Gb4vSq0zgg-7v1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab4L7NKWLQMtYL_Fzb9XqrpWBZBugnyv2g1ZK-ZiiR0vzrr9IoozZSAcuP9udeI13yiksnmdEqZv9kFK1y1f7EQd77A1goL1m2SGJk0xH8WTMO0PGO25wkQ0-4EnWu7O0oWc2IQAy3kleu66MA63BolXeyjkkiox9X9KrstpLjpXcXehFpEW6pxn1fSKJlpJs5rVMZF6U2QvM52uu-yUFewgxuDBAWdWkAw4aELNS7VA59wdxqeDqAOoU1PRQAcO3w_17yc8QmJngnjfO-oPYuhrCzslTC7tppnEOJI6mOhpStQ-uUM7LL6sYcfQvh9N2DwJJKkXCz8Hi7nyP4LAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOV3My-CAGUfk_3OifAcdzS96dfCXiS1XIszf4_hEX6VNROq0vfF-eeRbCiU-DWJJEM1dC0Fkpjh3uppQLTAbD36T38LXd-J4cacky8XboH03kZ0V-zZo7S1jqlxLt42jwBSxD6XQekj4RPn4DnF07hbw_h6FYsKcRxO-Aw8CUHwwK3919rnfgCs1DrW2EYtD6npcA5TH99DOj_viU27E3rJ84e2PbpwGQ51BbMarI4vxWAC2dPItTpvFV5RsQ1YUFl_hstn7T8d8TNzSE_F-b-uRSP8567JMfJ8psmkiDn76vBEGDJbi797Pl2epq90etMmV_yEsEgMgdsTVTmKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtZOx5ysFlCRmQvz_1npte8jHMLMZUVPDDE_um6iAceb1aRjQcUXGuU0KvGHveIq2Y1rcDuxtsLlCfLRbXq0EDDPVa1ySYiOGObzHuoJClmOiQEpsNFI3V6Wj2-HNyy_fiNv44G6p7ca37QOG3tX2ZqWax-FuWWa8cY5MLhqp2BAZCoD1-RjXn1XmhkVxmNqtzFKYJiCJ9uLZWRtQmRHmdeC3vvM_rwI_MbWPKEFBfHmngb8rs0f_wv1v7yUQluVF44mTRvAIJ-wVAo084rI38F4ulforQ10Cy6t3QqO7MLS-p5LD99U9XNqwc3vkWfKlxcjVe8u-7gvOSLl9NqI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t49iErQbTjbk-cpvRgZcYR9p8FOADyb7cxqxVvFIPvDLpeczwDyWuaLAhLQp7erRps5BGEIjr2OWu1pzXvRQ7BzQVNRiuqJ38c6wFYa87B5OdHiFqqUpyzJbyVxjlGiHLwervcBVOJfU_YcqLXsZmIJSTcUOXQei-Hyiq9fkTm00k8SW4fsclstuAGHb2bgWoHb3QkX5BzeLsHz7mfkF9NCchY8I2lrSbg9K8Wzh1CEexJAjwkIXbFN5Yhd_hIAXKIH4tHxy1QyNGOffPt6RLwAqljU4v0sXVp9Z0bjICXI5kO-IcgzXD4EnB6RaL2n0giZwYrP1DY5Zn0QfdH7yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWBJ3PIMhUghnS-5Z0EtbU7WKERj4frm93aSb1Ki57wr89UoCIOxSheDG05cr-cK2Qtd9GlUBpOYIN11l7JJev3L8Jzhba0msNZL-k_U3a52a5CUspmVBEEl58SOKSXA7QOocYQ4VfKE90vyGkp120iMep4FO0Q2wvbLmQb6todJNnfU9kxqP_QHLOu4SD2RW61kzrzUpNWnRId7fsUrITtXLOzZWjREQ2UGcDl154xeYbPLJ3GxGkbkPMQ4vhVlhb9gsqUzCgOEPAAQyIYOoiBqaPToSGrvnTCUCvVc5TIFGO3Zo7S5a0LJDpyHyVEbJ-CTl1RkMMc51ysLL6au1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=F_oP3pd6pbS3o9jAWJfdDLjkjGNEBMcQAErt7oo7LnVkMvO1u9be6zoDO20IGboWnianqBipq7FJWM5j6KIP7BU7wT16D0cLggHqLSU1cTGx_zceYOEc8U0YvpFgvLpQnSYbt9fr35tW9r2JZC0dzTJhoT-CQWHy74HoMM9anzHbaGM6wLtm81ommK3kA7fPfqGTPQW1DPb_7x3gGrecOe6RqgqVb1P_f5qE9o6_2aIELsbqjBD5jljG-Vs6ejFO9iD8byi9Qy0gWMj5lBwnnSf9NlGZFCANefl6EYhykm4zFjTsh3T7CGhVfvS7y20X6LH52fO2Gl2s6gOngf9mjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=F_oP3pd6pbS3o9jAWJfdDLjkjGNEBMcQAErt7oo7LnVkMvO1u9be6zoDO20IGboWnianqBipq7FJWM5j6KIP7BU7wT16D0cLggHqLSU1cTGx_zceYOEc8U0YvpFgvLpQnSYbt9fr35tW9r2JZC0dzTJhoT-CQWHy74HoMM9anzHbaGM6wLtm81ommK3kA7fPfqGTPQW1DPb_7x3gGrecOe6RqgqVb1P_f5qE9o6_2aIELsbqjBD5jljG-Vs6ejFO9iD8byi9Qy0gWMj5lBwnnSf9NlGZFCANefl6EYhykm4zFjTsh3T7CGhVfvS7y20X6LH52fO2Gl2s6gOngf9mjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWqphbr8P7jQj5fPdEg45x7HNAhchnyzcVt0vsQqkLJBoX57jix6-Y0VTI8FyooxlOrX7GlxSh0MXLCFJ4VkOA65DYr9tSD4PlQeUjyhvafyRanwaTQpV3l5dKqri2BLA2x5mClOSky0A1nHF6tyuV18CuOdFhF6BlVwNRzEMCfWkbGKk0cjMNDqkfuAIUVjhKOxIP8fo1P5W-L6Tl0Dxf3_W21HjhYhVtT-bdFd21kxNH6P3HLnCNnJeA680jyTACvO6bSleG3JkYLU129Wbfxkl7HxltJMTwgxbUjc-L1OVS7xWCuwWO3hLee2aDfOsAtdZksRHwFrNZ00vLDKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2iW9IP8qlvMxaFo7J__EvKJjcd15uU1JdvdYDrQnKpEIS-Rk8MoiFa5OU8RtBVXKNth1BGTAvrO0JsphanTJ9HGRiRESW4OZs04xNHh8XkI1n_9zBSRDNFUbmoeHm-8RBzO0ZWbhg2MwDSIkJp4jhGxbvYlUmfgctvR5j98YWPgRwupKD0Bjqyzf47rnUaK2YqGkO44nvX0NfT4Lo3HGqgJeT-ia4cGE4dtLEscfMviT9b2lEZ5qOaykUCK0X8BhNa34-FswwDFsgdBzRRFrNG1Ul9ZlkHeDDiOfjHi-h5Wv-JoF0qGYbNBJU2byevsH2g9dO1CewN8w0mCGcT20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHuSe-D-_kvG5c9XfL8djP7mwm97aW81OU2Hmi6xIgmgLa6MANbEdYy4zRSXtNN8WeNFT3KAKApwLtDrsmVzWqNkfGnvK3hkTtkeOXtudhWMHG04v6CHNIB35NiTkEgXCwnk_d1ay5qqq7WfLpOcZpa2IHlass2z70mVtwHM09FpnQBwqkJXelS1mDgc2_K85YXT-hJAwchjkYOAomnE_hXovNbI2aIYSi2XX428fdyq0kWzu1TllpO6xUWqKQpBk0AaR59RJSmPYsHQsdB2jGF0eVgGg9LdNqCV7Ioij5QEeAT2FfLDgTWM34MTRvLDMUkBlJyaBqRdZHmoiFr3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRahC18XePeQDYH_krpZJiOn2lTXGNQKa9UQgHo3TLAKvmYvkwb7yehHxIKG4yk-ESiYrOA_GwxPiGKMQCVUurAIHztOhaE_PjSzINVA1XudgHGVtJ2HkDz93lAFHEmctY7FXkCGLTwDplrcLoAus-39i0xVLUP7MEPNHpfbVWzX9XYUX-7exeuoWGhNxBDnsydX51aYiqv-_LEImYFVrY5p7N_308Pz-UpHzEe0nY8PRhSir5xmtTaAPvhdaU4HtRcvkvfsXrjnKqGfk_X9_8TLouVs0CNH6OEPb9kfvkWB-YV9wPTpNOzXeXV5kIYIuhiu1v9qEXCU4tbed5xnOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=Irt6oOuWSjzznyKhOkf02JQy3KyFPzlVh5eHQZaXy7LWCABXLClx4v4xv5zNytdIaiBvWgnO-aImctI76Ly54uNKJ05gLl2_5-ScsRvcKGvVjwX7z00SrzoYQOSw0u8zcwpdxrpX-LiCIy0yKzpvfkhZnnii8ApqeqBRCx1XdxqCJqDqtcCP8qqSYyzhTAjFwNIysOkZl3H6RIE8OWIEUSjrSi5QHBlKyPv6ISGzE3kHdV3oyBULnY0QeowL4-7qRi4Bh7_eBbtQ9Gp4jhMqoOdNJ2KhxwFCduN6NU1jONUSgNZ3ok2bF7m74bdUjr-7xSNvySL4cO8OQq2j5TKfIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=Irt6oOuWSjzznyKhOkf02JQy3KyFPzlVh5eHQZaXy7LWCABXLClx4v4xv5zNytdIaiBvWgnO-aImctI76Ly54uNKJ05gLl2_5-ScsRvcKGvVjwX7z00SrzoYQOSw0u8zcwpdxrpX-LiCIy0yKzpvfkhZnnii8ApqeqBRCx1XdxqCJqDqtcCP8qqSYyzhTAjFwNIysOkZl3H6RIE8OWIEUSjrSi5QHBlKyPv6ISGzE3kHdV3oyBULnY0QeowL4-7qRi4Bh7_eBbtQ9Gp4jhMqoOdNJ2KhxwFCduN6NU1jONUSgNZ3ok2bF7m74bdUjr-7xSNvySL4cO8OQq2j5TKfIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhyKJFW8-549fcW-h0yBtqbAMvJ_7-GwfPHVs_-fi5Fwg9-kHuNE3waSoe8J2i7ybUIJwcd3GW6BeF4Pnz86TtaddPoM7sbFU6PscYDaKeSny-TRU-Tn1efosGrc1v7iRRGurgD6pTIeauCQUVAwThqc-0tyWtJp6tOjpSRjkJte2v-5TER6oeW3u9Q5tNADBwsdfmigNEAroHSTHqBVT5mNeRdXo5632rD-qrt-1JW5J2QS-wLTQurQSWSoyacHYNMH2KSwcVsiogrreW4LpOojVqfNt8FfBybnvgzAh7u-JjLuaaoqaLjw-19alm8OeAxEWOTeG5QUnnDFCHz6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBjbckgl7K5F7OEIbuDvTIMO2SBIBC4gVPMVYNTCcJ0XbWYKL_NKNo2QjeT40HA7lbo56kEAQp0UOa42h9sfBaN2v6SCul8BJK_FKPJh7v5G9yGcO6haCvUHtzFXJvGsSLQI5z8T0H2E8zHewrgCyGK--hVv7Cy1t8Q0PSgoF1PTM7Uca2Fab2eEvEHV1yNEQlwKUn4JrveYIeflGTZk-EU3SgbUdNzsI3BskuIU4mF4DNzwhAiSGCnetDkkaSiN5hztUsLEUDmltSMZk5MvbntA16rL9YSe3h-azZYucSMa54-keP78eK7pMFS5O5GlbYk3rnLZGkI4dUHR5uEJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oht00gVc8F58QypJs6jZDnqYaNUae2zpc0QTBgtqFPWOTo5SqchERmJgzqKd-ufLzSljJixbYrdQm-rDItpiZsFuLF1hjQzIIyLRl7ucaOfmXTCEVTtHCeMpgTQgTWZ6hjiF9teYx_y3VfASZDQ0oTZqrj0_s011rOsPbP4Iv6EX4667V9SzlMCz-0i4b_U6Zeeswubng6F1V-F9QuZLOYSfnon_Wvux3pmMHAYs8QZiM8p8-xhP0m2j07J1VccBR1V5m-6_d_XbctJU52ZpnTO18RAc8CTjp1E6CVIi22XU3ueSYU61_fVSSKk0wazmEmiwuDEq5JQvjISa0cMOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-frAhqUA35ZrKTGP23BhUr3z9QukTd7Vjt6bA8K9IX05TP1Xq7t82u9jCUOIbKQzOMJBC-MnmcEBa2HKGqbhnW1213ZY_C5Zfi_fURpYGNX6BxS7mxOo-E3kwTvqNSJNenFBj1V2mhT6CNF9ih-MkHTTKGSSzOAqblRI5V8ERncJ4hqQyUcaF-3h9JlmgR6PRLrRdj6DZKnU52iAC-vFFYYlVdiaUcxWnfi9tZV7c4RLPm8ErtQ_cRgPGVzuMxuxuYrYfGiQEWqpZiBn-Fb5Q1DGI2rBAXcOfGfzt-po1LZ3qIuAQiA1i6Kgvg6G0WP6c26IOSEDouLAy29leqMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj5LPjg4JFtb4fF4Afn2UClpYoIq7qpV0FrKbouprHOPZcm5YO8tHSCPL8ZHJV4PwnU3l8_x4Fu3b88OgGawgGR2Nulx2ACLP5y_8ZFcn9XVDd8vW4my8hL3p-gAuVe5GLY6Ty_09u_1kPnBOObYod1NoF34ItlPFdJpBAe1owgY8DQgd2VMqAWb2iSM1YmyUNk7Vxr6VEjZbDTGkKnsY_jTk9waPuAIQOjRZ0vheYwbZV_i59TuoE9N_8wQ7AV3yIKp93Qw89ypKJV9Klflof2rAXFoe2TkZlBs7d4dQ7P3TyC43HslIUqOmpWjuzZ6CZRmUY3CXF_9WZk6jVw8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad-oCF-YS79ZTnEQOiBy0T1785ACDirnXWi19WzG74GOX0IuIJ2XYlpUlsqzii---imP_nNhrA_4bNiFSwsZNPyDftqyP2i5nvZe1ewd-dBhegWm-ejW3RCEZbsLcNz8NSUPc7sdmhgRI_WKCXy7WmBb86k5nGHpZmNrSZfvmoBcSTjKD1QxKeYJPJLnxQGfrZMmD6d4jEIlCMgz1yfIM-41mm1lKx_FJeJxp3D3SwvWUMrTRLYGyV7Y2NF1GqjIwywZoYIZ-AvksnMtDm5zDkFA5Q6jOMGi-pIepIXb-LSP9B-SNVpLlD_2EgnK6VfBX7lJIoJnIFXNgOfqVrY6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E51hOptm9221YUFT3_vscih_4dTLbpxuAx4qoPr9bz6Lqd4ZzQqVQcFPm_wumsritvJeP9YmSnjFbD7kOcS1ol_lGvOJDrz1IWH9_-D4m419np9_7qHrehx-lB4ahnZgOdZW8kxJbM-e856U8JFgRWwqOotjybS60NCEv0ayO5FffJkoUI3eQGoqXVwUxLwJrtJP_n21ZL8uQ3iKoeish996G58RzdaVP3Yft_7Ru7Kmn5pwRLmyjCqwkMS4GzbNUKdeqiBuPiUA_ZCWALAAuvzDuX0jXZUv3Y987YUoyrNVfFqnEouqnKLJz5KZV1jnkCNunKptvMapZZLouqxsHOvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E51hOptm9221YUFT3_vscih_4dTLbpxuAx4qoPr9bz6Lqd4ZzQqVQcFPm_wumsritvJeP9YmSnjFbD7kOcS1ol_lGvOJDrz1IWH9_-D4m419np9_7qHrehx-lB4ahnZgOdZW8kxJbM-e856U8JFgRWwqOotjybS60NCEv0ayO5FffJkoUI3eQGoqXVwUxLwJrtJP_n21ZL8uQ3iKoeish996G58RzdaVP3Yft_7Ru7Kmn5pwRLmyjCqwkMS4GzbNUKdeqiBuPiUA_ZCWALAAuvzDuX0jXZUv3Y987YUoyrNVfFqnEouqnKLJz5KZV1jnkCNunKptvMapZZLouqxsHOvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvNifS8ecrtTdDhIpfxMuzwu_R-FN4bSDDU_QWGK-KNUCpVfmv_eFVQ9Gq2qqvrvdrnwhrJCDE2Gh7AW0-CkQv4EvRovfHQ8gC4cdVTgDRlGSR0VTB4HfQW8pqi2qyrThX6W0tTTGsZQcTI_lTcO5SH9198I9wOp7mEz193Sf3hqANvx8CX-ml4x4zdLJFQJwukp2MH2T90h9TRe8Tg-XNCJWmJraIu7rXvp7HvtBT8Q1dnrekLNDBrXX3Ed6bi3Bnv4TuYQZuG-jIc5fjRBQUnVSjusfPh-vRlG1AmKXaNc8SV-pqZLhvGbKDmeTQC4_rT4DSHoYs4KvYKQhsqZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑
️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 150 ، 75 درصد بیشتر شارژ شوید
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن.
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27510" target="_blank">📅 11:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLbXK0wUeYhxVh1P8Sv3zUjeGvWZz1GvKHlGtQgMCO9pIhU88EkfMJOKCCCIPNKEjnUPxn2-e7E6Qj3OCubqHAFiuCyTZE9f7XLrnwS9RDYzL-moXmZAXWQBva3gu_md4T-10f4Q5IenI9U8SysFFesdmGIaGTaZeA11otmEe41SMZtKD07wJdH5Lucw-WqXuJkgt2oybLIFgmBa08gtBllC3gYZIz8mSE-xE7G9FifnLalpLbW2zYNTD3UeajzE7SBNq1l74mPpEoa1uCUtF2MNgOemucjK_tjB74EDqCEugKAHN7oFZqk1YUdllMmdwqfkheUmgqDeWmYKX2VePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDko6X1LfIgRG5mOKQR6TfUm8FOvuR4PJiuEZ5XOu2dt1HKiGLbx8FB9ThjXSJpKrS8H0t-HekBnyoRVxTDfm_-qswOxRSLrCCAsmigxSZWx_ttM5etNX9CwsBcZ0EBgYRLF_TrLhIuVk5bRVFVNq7v8uFDcmw867gl1gnVqcqYkFEHY6fEJIjs1S5z22Cf1i0Ky-2VbEeqtZ9c5e9qPV-iFUfn1QSg1QCDozKBPzPqRxvPN3R0riv4g9k2PhjYvvENTb-qv0dhjXgZKXUi-DnLHBoDFY4GDpdyA62JF5WpO-A91hBlgHvX713CsuIVLoLJLH4oQZ-PiTGtYt-Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=mIZInfa_O1ZRoi7ohh9WjvkPzwVLQ2nDYoOGlsDcSVhlfVG9t9CRsiYxEPiKZNOkvSLBrIHR1uXKS7JSqf5lIm3cPvpotarBlLrrI9vpNVXBfV8EqpPRXY_mSFtGOmyL4kjJG9NFM_PPnxwIvugj5TXI3KS4E0SohB6XjNjpfOGYWqws57akeE3Ogi_2bJ2jOY8CPOyF7CmDyJxXkxfcvTDIOUuPuPOYyTUqrSXqgKpgJvy6tb3OZZSIsT703ci4dolxo5qG2PfrGR4Tmx3cxO2TFJuaPDsRgTkJLCT8J0l-IpSpab-XDLnzkYdZxGM_A6OUrEQ_9o75O8kwx6lMmYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=mIZInfa_O1ZRoi7ohh9WjvkPzwVLQ2nDYoOGlsDcSVhlfVG9t9CRsiYxEPiKZNOkvSLBrIHR1uXKS7JSqf5lIm3cPvpotarBlLrrI9vpNVXBfV8EqpPRXY_mSFtGOmyL4kjJG9NFM_PPnxwIvugj5TXI3KS4E0SohB6XjNjpfOGYWqws57akeE3Ogi_2bJ2jOY8CPOyF7CmDyJxXkxfcvTDIOUuPuPOYyTUqrSXqgKpgJvy6tb3OZZSIsT703ci4dolxo5qG2PfrGR4Tmx3cxO2TFJuaPDsRgTkJLCT8J0l-IpSpab-XDLnzkYdZxGM_A6OUrEQ_9o75O8kwx6lMmYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAOlnK-Yrl2FGkOhc09FMl0YJeIYISNuHYcsptTS2sW9BZOqRB6QmWX06aRpf0sQ1R1-ZW0MDOAQVJTq0LrFS56ea9LiPmgdQx8jg_CY3o9mO-bAfe7RodKs0X2JUj5n48NlAh6187TwiAxWDeTXKLHAOlmU8afrMfDXJRZzAqrGaH4MxYQKWotHsuQarpQ2eDBrOt3tcQnZivEPtXOUr7uKVKI9b1cdPK7nDsq0e2OOB0fsaObyfglQiptzzBoV3-6byfr3EUwktT1GR4eEdWTh51BzPlGCzldUYsUZPpaJJnbKXI4tpbewbu84p-qSGFc0cSZqxmgSz5VZYbatnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIhCQJktvB_lzaoR32XxyWJUemY5jIkmdOLKMaH4UVo-OcKh-ej1c-9umL5rVDi0wiTogQrTwcELjKL4nJxx7sYxjqKyQMVQrfDNvYw6DH0o3908fa84uNGBBfS2tfktdj0Vv-DJ922yiWs_V9r3rvN9Rkg_4ytsIqO8Ry6UaVObIQhkueBY4ce1rUEO9CfVSBLZQpAVsMEKMsvMJbZuAH3Bp9MDwrL-OzwUGIcJotIHrCL3KZLSD37Pkly7mGxrNO9TUnTkIQ-2_w6CUIAixh7PcS0xxd1UmO4kxuhzyLOwptC8cK8LfcgGuGFVzoeZWIwzaVU_ZqRG6LphR0xe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=aBgwCq0Z5GXpxN8rMX4gFnWOx3YcjlHPbB9qWCgWksAyMk_eTFPMJ_KLDy9s4qc6AXTEowZx3ixtpwHRqGGJycoNEI9efx743jfGJ-81wYVvgEKdWZ57CjFnRRP6l8boa3wDMOt5iyF2r4BzygsrOE8T0h9o4I9g3L799U3zft493a2qmeNQPqCqcSQbGb5HjkJUfwybZnr7DYPKk8FfjbVDPPeJ_dzp3rpIpD9urqAqWNn9Wt_TSE7cjtRv5uRBG2f3mdq7sF06SggfzBkJzNG0PEza_NlN7DGNca1xgreTIJgXJo8tU6aHEgUIztueF6HQW2CcEKb_rq7Z4by7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=aBgwCq0Z5GXpxN8rMX4gFnWOx3YcjlHPbB9qWCgWksAyMk_eTFPMJ_KLDy9s4qc6AXTEowZx3ixtpwHRqGGJycoNEI9efx743jfGJ-81wYVvgEKdWZ57CjFnRRP6l8boa3wDMOt5iyF2r4BzygsrOE8T0h9o4I9g3L799U3zft493a2qmeNQPqCqcSQbGb5HjkJUfwybZnr7DYPKk8FfjbVDPPeJ_dzp3rpIpD9urqAqWNn9Wt_TSE7cjtRv5uRBG2f3mdq7sF06SggfzBkJzNG0PEza_NlN7DGNca1xgreTIJgXJo8tU6aHEgUIztueF6HQW2CcEKb_rq7Z4by7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMsAAW5KvPmEagEy-d2sOd5ms2wAFJfQ6c7Q6IZd_rZQDHR8yG1-E8Q5-yR2i-yxeFSf7c5shWcLgVP4YyRHCxuqiI9PXrWEWUYVWDXVarhj4aHV1q7VdSgCcwFBlRIXLTwzp_6VJTWaW-_0FHi8fjl8Datwr3ZljpHRX1n2Qajw6DJJFUZy-gTQ6Jv2pv2QCO6A5KpvH_g_T7y5T7gx8ZqRmzHHPeYtuGarQIgHK-bC7SSqj_5xHpBYRN1rUSzbfBGckGo1y7snvzrRIg8PV7JixELDnGjV5r-qe_DV0-w3Py8Oz6NztkPmiVdDLe7VWBJ4ECWWlEK2Xb3vaVnySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=AntZy0-mFb8p24avc2CpVWGaUv_9HbLcgFqgwOEYF-C4znSJajytRU8gfA_xOJqrlZmh-ueev673ly764cXrdJzilv0OA_aiqw8j9l789-tKEqnheuyj9rO-y5b9Vl9lydYsvQpugNLzNCG1pFimZ49Gwc8yR6ydrU_yw_hcEHKMz5XZmlhoPyf-oP26OGIA3mwa39JYVP_itol5j84MsBJdpnQ49Ex2oy5AWaEwSDU5iv0uhqPucoKk4mR5fowQZymR84Poh-JOo1xiOS6WhAlytppYVBmAResuxLUgNBW4ToZoKkd0lPt3WV1VFVbp27tnqmAlEYoxNreadKWWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=AntZy0-mFb8p24avc2CpVWGaUv_9HbLcgFqgwOEYF-C4znSJajytRU8gfA_xOJqrlZmh-ueev673ly764cXrdJzilv0OA_aiqw8j9l789-tKEqnheuyj9rO-y5b9Vl9lydYsvQpugNLzNCG1pFimZ49Gwc8yR6ydrU_yw_hcEHKMz5XZmlhoPyf-oP26OGIA3mwa39JYVP_itol5j84MsBJdpnQ49Ex2oy5AWaEwSDU5iv0uhqPucoKk4mR5fowQZymR84Poh-JOo1xiOS6WhAlytppYVBmAResuxLUgNBW4ToZoKkd0lPt3WV1VFVbp27tnqmAlEYoxNreadKWWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHa8XLGiWJ9PGprAVsJxlpxi4Zz-_YSEffHHuFDrR1ZpDyxNxdsrVwwbtKPL9lBosHvm6B3rYT5kQlYXN6wPbu4J1yJwr5W9Foq35a8UMD1fM6jSw5QUSu6zxfCz_frMCNocWRaHYLk8-DiHm7zEJO6BpHrI9_qy0y4SaO1hyGdqlLFrTtQbo6VmgbC9DLVyZuLMzLU3p9eiDdQvqmW6KK3CYLx3VxjZrrIgFySfnKjzqvKsK82bY2yni-FF6XU28qaF38qWFHBCjavXCr3GXbKcLyTTdatzDsiwsLunVdKlq1ymuLm1YvQDHXFhg5dyERQ4PAOjVgW9yABeNMg9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=SeCYxUjow-TE5IoEf52CpvGiGel3IcXFM5d51yBtwhNKqPSRbauQ_8POlOIiphj9DrJNaN5wejt0b7QUONh8OX6nvXpHs3IbwLeDh2vWCrD56uZU_3kIhsetgOJMEGWxgoEsuRMO9RZfmGHLI3BK3xYOW7LFwpizCfi57Gz79NCiHF2IAIRRIDA4X4BTdYGD84IwLBRiUMLVQMaai2wLsHIAvC8hAAym878SV8Eg143TS_HkwPpZLlLM-Hjzy2X8gj38fSpnYpuzhOx-QEGfK60ptjUazvvpL3-oLlzJr_wljbnFK6cAv1vNQbB94jwu56oKYyFXyiXfNu_84ilOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=SeCYxUjow-TE5IoEf52CpvGiGel3IcXFM5d51yBtwhNKqPSRbauQ_8POlOIiphj9DrJNaN5wejt0b7QUONh8OX6nvXpHs3IbwLeDh2vWCrD56uZU_3kIhsetgOJMEGWxgoEsuRMO9RZfmGHLI3BK3xYOW7LFwpizCfi57Gz79NCiHF2IAIRRIDA4X4BTdYGD84IwLBRiUMLVQMaai2wLsHIAvC8hAAym878SV8Eg143TS_HkwPpZLlLM-Hjzy2X8gj38fSpnYpuzhOx-QEGfK60ptjUazvvpL3-oLlzJr_wljbnFK6cAv1vNQbB94jwu56oKYyFXyiXfNu_84ilOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um0F7ze82WMiG1nXGWIe1_-THm-00AUvWdKeBuBFoxwQ1pK_H7j9PZpmJxnrKb_ABbABIowkgBVFOWXJNBj2wb9mSTIUurh5ZHwMkU9saHfbFRgc_QK10oZ5q9qZZ4B8V5-9n4XEss4XQK-7X9JHBJLAZtYLX5j_NMxpDQyT-YyaYC4GS6jT2beXGR6wLGCTrk_o6lXJq2EJenIt6XVd3gk64eYyuqGoXbeHWIEq_NzHBZofZ71CBG0G88_Ka-uP48Ak5K0qD9p-oT2DCkJKCwo_auLx0uCxre7gjsW1Nszmtw0CSdWE1iz01a6gouS-K1IrNy0hs9oA9bdHveAsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=loDRQs2oCu8FM3dJughfmkbphg1bE9_S0XQQVtYAuINNZyJT-G4wSa7XlYiLWA8RapzPJ0KYxWTemaftIcRvUitaCo6uuZ-V2IjFEhQS_jbk93rpB7JY9JzDgR9UJTPGFz6T21tn5v_beT3oOXURSWQ0BT5oNIHdCmKAa8wroHJdGWHc5BnyMDF0vYHjaewmxY1ePzUkysfwBzzFGZ2JEyABas8yqaXyulEqCrhPTPT5bmACh8IVMGeSyOa3cfpVEk_MkmXeDexYUxmFCpGGK5ERqWgQQ185eFoKLk9G7Pf1MCU-UDfQGwJSFYlazewgMPDCrYDAc86fXRyZvYgARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=loDRQs2oCu8FM3dJughfmkbphg1bE9_S0XQQVtYAuINNZyJT-G4wSa7XlYiLWA8RapzPJ0KYxWTemaftIcRvUitaCo6uuZ-V2IjFEhQS_jbk93rpB7JY9JzDgR9UJTPGFz6T21tn5v_beT3oOXURSWQ0BT5oNIHdCmKAa8wroHJdGWHc5BnyMDF0vYHjaewmxY1ePzUkysfwBzzFGZ2JEyABas8yqaXyulEqCrhPTPT5bmACh8IVMGeSyOa3cfpVEk_MkmXeDexYUxmFCpGGK5ERqWgQQ185eFoKLk9G7Pf1MCU-UDfQGwJSFYlazewgMPDCrYDAc86fXRyZvYgARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4_FSrryKRI3kEWHW6SNlg5Npy9rLjjIhjnzWegY54Vo_RHlhOd705reaSG4tNgg6kZEbG5wBzHidqcxnB_wpppAEVApWBmywNgEaeudntSbbzBcE9iJRw_vqdSh8HZRb0rp6GWf4xp4Tatnfa1vsQXD7q3XxDbcyFz3ApLNE6LkuMfhZ9thnjo_5fQ3KffBj0sySmC51vFes1O3tp4IrZX9_V1YqRwalQIq6AH1_NSQ4-gx2Qe6Gf0CRlS4wEkDOvklNdEbxZXWwQE6Crvr1XGX3lou0yx_IvMR6jekE7KwJX-SYE7RBbtFSm_J5w--6ZM_qaz0vjkvCCFhRaJo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_FxBuxIdhItwqjVWCAMsUWX3ytUhy6Lq0tMiFzbMDV4-FfD7UShmI3KbKeCDOy5Sqxb3eY9D3eOKl23yKWli8zmJPhxkeazaYMcilysnTbgfOE5IF9k_FFm16Q-1z0x4Wedso0anYye12L2t7PILcnkSuJ-iw9w5skzW7UzOM5bCIuWukjgTC0VSRC_vHHfvwWwy0lUODcYJMqzme5_r-JCaWUHyhmGE0K9zxcnN93W-MjrlF_st6z8tNBwSOnbtz4MkvoZgZABHrriPbkE2o74wxBSwh7EFirVfNNbxldb8grtvXb3GsK7H37zFntib-FjfWhJ9hzeyAaUoG8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_rRJygWwMsEN1MUQhSv5sJmR-I2gCrl-JRYgoi9orzXOVh3gkZKSBuAcnsZghvPAlSYVb8kU38kt7KN7-eBmQahNapIjj8_YPoRTkxdJK3xlDmiHCUNIeSp71EWgqPdpHRQ6EIDezpEohTnPa6tUvN3w_trGC-rfX7GnEi_PFykJ79Pn9rOzev-HdpGa44KtcDv3YIriOYJLmw-grMLwdkqqNFAO6oW8Uqn6GkubMK7VrhjqLlh4YoAh5wiSaZNVP5eoAlOiD6I0CajHkVT2H0TOCfuDWwllcpGkvNO2ell7zkFkasDyMuJWy-DxpUaCrWJk6nP4u2bS4wYVvi6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZTFDixYwBxY7T_nUeeq0LxAypf6rKOchjyl6HNElxpb4ZYFO_kfU9eSsQMJCwLLchlMTBpm59YumHKp2ADWxrLrGB2_xvqAJwn19tmk8t6xWIIXb0ZTIO8DXR3nq-F4cx_e5QzkyaqoK8shQBwIUvanZpIIhfhJfsXJ490TuS5JQQMhmjS2PMp2UR8gG8u1-SGQn--0Qpw4HoW_xRjTI00Y4jxQJVzCbMd_1u0V39px5ecun1XYjrhidSswVc_RjHvMDTWy-7iN8UpjhmZg0EL0H8a7lbgCocVMzeC-s0GRIe76WqTF0eG0sMOvyZk9koN7VaKrIl2e24fs4AgIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkF5uKiOhYvLIijVRUGUBF8rm03ITiAiTHtmbhNR2CR4kLyJ1wa5xgXEHM0Lfsg_ll1Y1uU52RBVRW9tB1wL119kR0WDRnxJatfG6OtAv72P3r5kHB_D9Dwr-c170WU_MJI5cS2GIz52oxLfsenpLuqkKTVyGPTnafHdxQMmwaidj2MejJFNccDJdA82zvFT_mUxV6VZ6ig7EWuqcbYZW7tZqnMLVg5dI4M3uKguyKhqwvLqPxVnHhwX-TAOjArrd55DsUVMH4tWTYapSyZuRdUeKBKqct7u451BfhxUf0a4jgangC_KutO1lrOh42mKd_Dq56LWsdqLQRizUn9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqKo1uooqL5ZZLde-y3Of7uYFwHydYl9bEhHbZ_94p4rJkWxcXl2AIj_cXSzDM4-X3oPCuwN8j_eCfr9Ye6RoCskADRFrhiX6TGX5_NTsbc_395udxfbx_Aoq_oEHGXsEb5pKK-LfuJKGNyRiYJiptdknyJXo1UWlG89zcpUyKZDcvAZOKHirTMXChgqALaVt37KzRoI5va46mAd82-31AOzNWezeu9N5KvaXbLIGSz8l-7MFCzWck4aQDkjorWRFUtzCkTAUqPCqoF6jeccNrmX8OKaA20BU9EMyOL1Qf8vLOxUJ1VKzNUGz25rQDnsnOnZg_golnfC3auppveDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV89p7l4VhtcC-Ai3jaAfq61atwWysEUUREx-BtfNA27rFxaFOs2G1ASNDteUCf36zokOtDoLABGRd99xAHxkbOK8f9dNEF_qabXulHDXH_ZZkfXCR0iLWTH2e4sYfGcJDO3flQhlRdYzeDIh6S4lFPrS5iR_jrP4Q7dEIl_s2GypvJoE5LcIgvdd7ZfBfhr8vVUL0RbNqaKY4aALc4K2HLGBne4rGdMZvuj0-lN4YUeyZESr457F7J6GCyzcdkdGi-JiBwwDAth-SHBo27rusMEo9Gzjrp1rUc6FRgY-0Zf4WbivQAo9YQQEqa5XLHI9YUzAIiAklNUab_yMrzGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7MR7lK1EKkTPUdhflQPO1sWjMCaXx0cD2rHkHX9Jn5ebvgTA2H9rq7u6kDQZ0RTAKsEOIoCvYCG5onwBatPMnRbDXWCM1uymcUUBdoOf_08s_UB-z6rjCjbwOGb5AKkoB2qbr_Nkkc_frRYFv7K5HPdJCB1NZGgFDc8sLyMijq-95YhzlhIhGiywT-K7fmE6iMX3phZhkLJjELIATKBsm3haoXH9X5BOgJ7BRfvY1AhrAmvOh_yNEtzHGuR3XpWKuMSJGmffvARK-8sthdchmkDo8JzJHfUVFHP-RjHZF-fFOzFvXVxLCybJrk-txauRSQ7UQK6fjqazKZXSw_fGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw8WbmvqBlEiy_Fhxt2baKZ5AENsmayGx009SoIDvuCblZrK23NSQc2HtYuimlUG0GHgVo4qznncaRX0dkz7DdsXjeIgd7tv4QxGq23dtXFgFgYqlXYy9d-d329ScIvb9l2rwTpANr9IcNHXxR2YyRHs3xBu6R5U3TOnmAy9EH4nO2ALz3eRxkLPPWMGML--_verDRJ-6Q20yRAq7xZhheEOkC6i461YwCtt4NdLO5sWsUYFTwDJeVh3-TYJG3KAu_9AiBe1jcoMgXedqioqvmYg_2aDtpQ0Q6ZkSswAcJf7lfSim-ReTUCDIOTDmjbGZq9oJySCJ8slM0kRtbyKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYFtFABRf7L2W_rDJWCt3CkwRcE6ov2PV9dho97oSN6IlodfvY4sPF8vOwf8DyO6XXs3tMVnqw_Vmq2xn_4lvfbgNBohQ1p8BA4uJOpfzAFxJI4K5cse0jo9HqZgiDz7rFR72uhaqXRuJbasO9YcH43FPuFmXogM3qI7cxe1_UME9ero9ex1sUfd-xTmyEIATBScKKiDtGv7r0dqFPOX-3Fc2sb5vqw0fs7w_KagT_vU3S-FJRyHLfhdqpF80EkZKbGaoDTul53aWwznsN1--lcQLCKXUjaHcE1UlbAxVWnOQCQNDWx7Vxsdajg8yOR8Xs3OdyX-LkgSWp0t7rNxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVNKZU45fIyAYBUnoAd-Ks3kq91IZkd9DO4sUZ89o8xJnR1JpIr7Jp8QKp_k99zOizZTEEwRCMNlp5ieDup3eojDw2-fgO1Dx2MGFasX2g8dO61clywy77ZI9my80UDFFpDUoNXTy_BQ69eX-Tu7YgpFMTFj6GRkXOTfoEvrB-N9Ai_KmmKqf_4vwotBmtQD2vWIMIiUWIaKAnEv_szN2Sgkz9Lh-u3ttWspadvCtBsNf2pTvTS7lb-pQP3_fh_q340Cdx6suRfVdpRWPoENeVtDzQreG19o5apcVZwaB-IFbwyP-7VQagBLfOufOKAacHzqIVSePRMRZYahAgRw_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjh-mabWA2jGBc_l2mPqbfmfVZfyjO2g-tHEy0ZmIhyakNLUvopaxOk-mifD2xbhPr5LblmWN42SXj-PzQAc8fbnvby-1FjqDxKVJE8wMfM5ef51PH1uKVU9CwKT36PlnEXcI_duaYPiraZhzuNUWJU0F_k5axQCtC3AVNGnLXAryPgj4j0A7XCnBdDsZfe2t5qbVWttwDOugAaL9fMcLVdXW-g0OzsQVLRQImbVO7_6vrbplW7zeWUGbf-2rVGrqJ4lAR_rVaZ8oyQ2UUGq9jwluzY6St6haeUO9UqYmGreOp634ch7dRfBBAwYYcDnvZc0D4n15NvTU3YcDbEqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLwwPxxmasJmgAL9rDhhnP5Ow3N9JFSHOwQ5wIDJJk0AJgx3pR0NoBCjXf4O71WXobHc2Q06pdrKTEihnmgsiH5mt9op32XskntoM23u2BGriYJSN2TVIYCuGYFc6l1ysbIR0XlcxrurILiwlMJdikCeN7XSGkeLwRMD53fDTkmFwrT-2CWwmzlJZSdltDCqPMI7Wxz0fA1p-b4S93mxklz3tVrFbFkSEhbf0tD8ruq4qlr4lIXKyBl8SG9gA-D2s86gB5I80-WlO6KkjTmUwoQ2EYgHCLkG14bu1fxGccc2AzmRdOHq0aUjBDEhfO-j_G6a5JwRmqaWTh_syPLESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU4WHTlkOViNS4oZa-pbDqvvI6PrCPh-Exy8YsN-zvP6Rvcx41r7XwsitwZyZKvBQ28mTKOnQ0rc4d8v9M3Njs6OZkImHxb80KocyrzKxpGffl2_LL8ED48wo7_i6MAOhpGnZ953kDF0Xb1buBSjmOgK72d2DbmNWImdFsIhjPV-Gau-BQ9KOsYj9dgr8Pc6VO7jvRXg73zp8fZPCDNLRoh3_7Z_O6PKVoo15YTjL5G7cfj17GfmwPiqj-bwYl_q85UmduJPlJ5MzSXEVR-o6oibjlbzGX-5pN8xurJpyowIFGRoApLQL9oXiJAQtD8vgxYrlaMD-3M7E_DksPs8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1JPHwbR_s3oAGqmgfyYBJxbfRcH_VFjkmvjiInWZ8MDSrhcx9kbbRHQrajLK64ecxs-nUZ_E_iZDCCMZRZoA93jqObgWwlXKqF1I16yIkWeiu-4dAbi9maDV0r9hR6DESE7E0yKYJEtxskYQ0Zw66uckei0xDJca1Mrdc63EbqyLAA1IxuMmzdasVz2YrWqrJMxckzvClXdST93GT5xD0K0-LRMvFyd1ihh_k4khHYfNJO3PapXTzLamRCVrILYlNj2SkArTOMfeCqLDTZ1ogGjWK2sN-Az1g-1fEJ3HP9uJ3qN5eE0befIlCALP0zXYrtVF261_pCAo-VrZgoPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edtf4-zZmBW-4pixpXKm5L0I73MRxd4i6goceKvqwrzrho36tJlsFXuGaY6r3bmbwWJDHiHpzJRTUWgJIsdZN6xRXhbvCvfjymviyFdwCTMtF7_lQ9KGpFWH61nWr4McfJDRwJWwn4Tlkqtmk1oDCvZmSiXUOI1PH5J10fWiQhth1yG5L5S_JT9GoiwngkQNafm87E42zU-d_OQOcRb4dsc8LbKsH5NX5Qy97Z6IT_7Yrb4JLPQovy6Ot0PiNShbtCJBoPLA8kyQh7XAB_haOEyAqfgj-JJsqGMphXCotEGMhgi6GBcsBpnMHU8YcWzYuIcmyBFkQJYFewpojZOBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqo7c3I-K_Q4VdlpsaABKmS1moM9LGSE_kRVNuR2MDMia06yyYIFti1GBdGEJwbL0cRYyy2k8TPnRHnmGd4cs5bYVtwqWTGekWWPjG0OHbgON37aucucgcuYVHWBgSXOHmTWfcJ1HnGWXR-DLrV3hlSnDmOPXlAJWDeCQlWdvx3foEpW-7LQjdScVS0kO-eNs4nsurQ0JCYhIsn-Ij301sw1I3qY1djVRPgoKUn6Mv5dpP52kJQ_8I3DUGUyP-HCG7nwpG-ef9iBp70phXiY12Q4L-ReTtNh9giF94MQl62-AHzcJSZLG3OGdmiEMC1rrDnvvjwaRXgCCOGASDtieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwS72twW3iXLDZr5t_z0bytmCkEVImAJDzNHx5fxG2yecWwdV7ToSvD4XPIBJzzSqfN0s5F2yTfraA1HbWdDXBPobXN2xFO5f5oPF3j-O3ykG-ua3Vfdk_34RdZw3RIqlBFH6rPo9AQ_y_Zi016pDqdQX4O3motkwbRGLqReNB-njhAotDB-fQvlkQwxE91yIRd7nvG0AwOI8i6IETrFImTz6QyI66Nw5VuS6wQjPoNcWsQCan4rNsS_SR6-FDBrQ9SV9DT80TEA1nX3mFjcQSx5MgprugV2TjIQMeL1xNS86bQXu1TZ2GhLFItNtTwxuxk8TOJzCA-SO797b4fy7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgPWygnZRCCqcHedszopbiy-d82Dqg_86oM7UyM1zNnUSTaaB5QspaUs3QPacmOUGov8YAaKbp7lv968pdaDrcNchudcnmSK1u7dUt-X8P8cwdKOjKsNr7FwwwgWMBkB5tDtOMPHu6sVPuc69rF_x4_KQNyq_GrrIvS4Y1N5CQ503nToUJ_tPzQFQGRD_CKfrGyrghsvpiWlXudHcl26WbvkLV-mAYFymEZxNfKUObI6i7nMxlSfII5UzsFnjxuSkVHRrAjB6fLb6G3OIvpUrNoFFqbgKfFueH3Jsx0hGIaR7i25m3vmk4UZAIXeykhz8EJoD3rwRkZ9khOif_J9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnO-2uDZ4Wm63UYbHV-oOuzNurFv1Kio_Bo_gDcVGsVNZW1ePJWIR83mFf0dv1Sl_Fhk5lQqwLiETRN0IqOWOqh7O63EHjgnkQ1J42DrLHZpfpmLAJeNFmzpe2muELM6SuoriW3Tpy2RKBMsRJ_8LhhkEOXNb6SkvoT-OtFrdH0v6cW-_YUJTncl6Ci7Xc9e_Jn11GPhRI9V8DeyTXsCoVkHz0LC2nGn9QK5mpgEC9O83z5DdMNPpN0y_m2RCtEtlE-JngyU8gcjzkcu7_BzndKZxh0U8PgC2TDr3BmYTXeszFsEomby_UETFyP5uU2eN9HsU7L4YuxOskseB8Q8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=gyTNUlXv1j4nVuaFMFsIB10O8RQfAY-rSNMB38O7lp5nPEhtaGA-T4YM7AjBBhcT1TV_1wBfl6rcjpLMQxdZl7_ZGNyDthSukMPQ46lMxCIdVWGSjaL3Yj7ttiz2kJfDCHkhPI8rxnUHFNntdnhw0yyOOng-smEaQrNLluFcw1EjEvFMSFYZFmsnB8qxRayIVfrYcNaB4mtT9a4ggwr63TpRLfm2vyZMihSMOPEEglLwktyvbdsDqMZwDP3B39Fsxevk7KgQjEtFDgocx-UpZySmmrt59RqMBXBl1--fdECDKqj6O_Hgr4HHFCaeKMRiLmvwKyJyhotTaVMIJio-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=gyTNUlXv1j4nVuaFMFsIB10O8RQfAY-rSNMB38O7lp5nPEhtaGA-T4YM7AjBBhcT1TV_1wBfl6rcjpLMQxdZl7_ZGNyDthSukMPQ46lMxCIdVWGSjaL3Yj7ttiz2kJfDCHkhPI8rxnUHFNntdnhw0yyOOng-smEaQrNLluFcw1EjEvFMSFYZFmsnB8qxRayIVfrYcNaB4mtT9a4ggwr63TpRLfm2vyZMihSMOPEEglLwktyvbdsDqMZwDP3B39Fsxevk7KgQjEtFDgocx-UpZySmmrt59RqMBXBl1--fdECDKqj6O_Hgr4HHFCaeKMRiLmvwKyJyhotTaVMIJio-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=B8VRnIEcLZEF5T6S4In3p_D6eI46zwHrAh8AeWTWCOjjfuTAeq6niyj6N2r8w25ZS4C88Ge8pmCKttu_3PhOOq0D1YyjwKz42eqxNpg6jmpFag5dHRP2dOnXqI6Msbvibg2AlNFPetGCan8vtL9ZcwuAbrneJeLa4FpSEqeNn5XRdyeI86HwE8JoX8v8pQRqeKiyjq8G9C9WhcNqs5mbhe1O2FdJHFqnhOgBfGeLFkgtKNxPzz4Exbo8XRBWUiOdF8J1MDmRocOpFzW-9yxlRfgCdi7mCqb8-EZjCnW9Vjz7ap_koQMohCcmjsXIwNFrRgQyLa3CRcfc-jC3Ys2GJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=B8VRnIEcLZEF5T6S4In3p_D6eI46zwHrAh8AeWTWCOjjfuTAeq6niyj6N2r8w25ZS4C88Ge8pmCKttu_3PhOOq0D1YyjwKz42eqxNpg6jmpFag5dHRP2dOnXqI6Msbvibg2AlNFPetGCan8vtL9ZcwuAbrneJeLa4FpSEqeNn5XRdyeI86HwE8JoX8v8pQRqeKiyjq8G9C9WhcNqs5mbhe1O2FdJHFqnhOgBfGeLFkgtKNxPzz4Exbo8XRBWUiOdF8J1MDmRocOpFzW-9yxlRfgCdi7mCqb8-EZjCnW9Vjz7ap_koQMohCcmjsXIwNFrRgQyLa3CRcfc-jC3Ys2GJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rosZsJeUyLHFa_mVv1FZQsTh5AcnmTy-M_EQ73l7PZa2NFRSGqaI7wErNOzVW4HQVUdPbuRgw45zleYCC6Y84bxH_YWp5-x0GruehKi6QAXo6fIzen2rmXb-4-KoT3wR33ASWku9vqCoUwVSTWpvVmb7GttYHHYhT5VXY9DfyUDIHR-LjGj4rkmSsabgZMzInQ5Q8kn3DdKxb-96QCTEjgY7b6yOLd4EQSzbRe9ecA7q_I_uQ-nbN7LgczrnPGVg9OwfW-1IKwbsYvXbin02yZllVTayEXXU2kAlH1oduDXwWrhasvfJ2wlzfmVEm_imRJ_seauAzu7eAk7P8WDmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC5AtHt4kJ_wNwLln24Gt3pxmJi_5JgN-_7HuVed-1JX-sQistwug9R8RKehNZ6Nac6pEmpV3NjiB-QIgQg0Nid6HvgJ7-FKc5BplbdVsKyMpKckfRMHmUW8d2pQn18_oTU-T4ptXcDvM40o1E6pC5pyzwRr01CG_HYBmOJqYF_ktOoq3p3hwp9nKJYimOcPEoDS2qlHYOa2TA50mmQnEA7lWF75RPoFUtPrfzJIVIFis6RPNexS4Ees7EksAOkrrj_-kMzLSr3OKowPrANj9ByFYCNAIElgFl6mhxmfDaIqr0s-lBHXV0qyLcw3_ervI--yWCJQKYG0ZpakK0fdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKIgRzWUyFMpqHF4NOT6COBejUHSW4lNZDmHWoRTcpiD_IYbLG60RkhaMsBq0OOQySviCrC477m_iwx-mAmVvKagIxm2Exebcu3QwEL7--gS6GjdqxIdjV2IX6kXXZub1iuAezy85b381kBL1TWNHCuKZZcV4Ds3yPmvryOrfo0dsqcN_5sDMfNaN6gvDfQ4Yo6aTgEAr_OgdhDoFmYRqFFKyG-rf7LwEhkQkuWUH3EqXFYY5aDELAAWttriCVWAK_pavUbJWNdiNQrvQWd3LwNZY48c14vfUX7AhGqxGfPiuAYVvqS_cvgzoW0j64QKAyX3GIutB6-wUG7yJWvljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqDY0AtHUDQMimB3LdIAZ4pd9xKHq3q34F-sUOcytAufH_k60Y9fBcx7wX9X2LTQ9q3zSEOLYEd1PdJ_MQtefKhWbrAyZjuzhgrUyWcavxPmMOnBgF27a57-sVgP2XaDta5oOuEwBUYF8p8HDLFYc0IdgUA_5PiDN4CSszKMymewjfEurAT0CCAUAZVKXqkpl8U6EEoyx1gG7ProDl9VGnOtJedl02mUWOK8rWTWkE8ZAq3F1gc9OHi44Kx354G-pg7IUVjv57WoSo2rvSLeFg9TK9Cw66_FbVxcthZTmUZNstR7yAdSQ-PVv2ph7d1NQYB8iM5_Ejc4Ej5vydAXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_-kwdO6SBqHdfSi-Pmrc32NGRXwpGAtPB2CkHKTNWSWheAl8_panH1B0vX3W39MIZIFDDBkXRgTG4RM6_vySio3k6PviuvC5j7QuCTBrzP7BJTXOqso-Cn2xolkhvQjyA73T41LJKf5vVZxFtamMeCdiSS9L4CMPThTcBSV_-r5v4VGJUDB7xomxCzFIv6vDanXWhWvzgaG8JbY9k_c0bYPgK-xyY_XHf0ML-A3U5Iy9qGe-jujuGyJsBqKRyfNKsXnRmCJ398IVkIMRX9COD1vchw67mr8uJARqGTvWLkalloTRLo2HozXh_0prQgVcSbNa2ulTSYW-MkWxJcCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=BECIphWTt95kUJHAH8X4sEUZ3e3uRSxeDMZ3VKk1G8-xdUbY1bR_If9fn8y0ED_Ijb51URjL80_ETUa1URVWWj49oTJ0eWhxpERdJp0w4_MAx2S2taITshkFlX_8Z80iiepgxWfI3Z6JCx_gcvNcH77pe-5-xvH7WWE_5pd2Aq8EVYck6Q5PIt4b5-ihEaBJh4829X1kTWQ4NCxWUgRTIqw5pArtGPo0bv8pUq899tFgHNy1mYXKzGgRtyQDTP2YDKTH2rFgUCdlTNUNU7PmZVTpvI3kOrYlJbiEboW_5LgMJe3LfVQDeegYvO7vV8Cy9AdG1fqDVaOoa5kjxAGmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=BECIphWTt95kUJHAH8X4sEUZ3e3uRSxeDMZ3VKk1G8-xdUbY1bR_If9fn8y0ED_Ijb51URjL80_ETUa1URVWWj49oTJ0eWhxpERdJp0w4_MAx2S2taITshkFlX_8Z80iiepgxWfI3Z6JCx_gcvNcH77pe-5-xvH7WWE_5pd2Aq8EVYck6Q5PIt4b5-ihEaBJh4829X1kTWQ4NCxWUgRTIqw5pArtGPo0bv8pUq899tFgHNy1mYXKzGgRtyQDTP2YDKTH2rFgUCdlTNUNU7PmZVTpvI3kOrYlJbiEboW_5LgMJe3LfVQDeegYvO7vV8Cy9AdG1fqDVaOoa5kjxAGmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArVi9i9XoQ9D2qEPWu4mWcXkmy1aqVfmdDmJ6n5IAdn0pLwxQ4N_L0uJcWGMAtryS-cQBIeROUXqN9afO0MhptBLHusfLGbTLsrQ0BL6DZCsGdLeeahtdjbDkrrIoLRK_ARfnmK8HXTLKX19JsuYnJtBaiVeMGzty0b0OWQuWjNTlN9ryds_oHIcUk6bGe1OrxSuhHG-vy5LMfcaAuDWZH5UvTmYRVq9UHT9CQF1ei2NbC8MMeM3mq7yULCDn66Ag3VefwR7dR7PNER3CgulMO3LZpUEpYyxL36yA6wfTKsVt_oSCx6PiFCh1rsYhHDIl2vXbdIut7ei6sdm19sOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeLNv_MSkMxJNdEvX_-ZyV1crHWabYKmPZuaTxY-LEMWgEgHvC3lfaWxzvgah5YXOClUZqEgr4hP0FG7_wLzAdEUv1q470OQG0tHibwk6pGkirBehC68wjSQc-ROHgry807_WEF9TN1daSMuy_LSJSqd5xDLbmzVwCW3tQY4E-tQwmfSKjRkTy6TH2tVq-yIT4mu8brg-6h3ahBbvHkF0lHnC4WEQW-t8lHEl-_7dpwVpsOIQbf9G3OVXpYQBOyYzaZmz5LUOgmgnYq7hwhnq-JyJ25fii2gFeHPUmNAk_chtW6mrErD09iNOyi-d15nRH5zp46V8kqzWduaoabwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOSY9Fkvwuz11YbRBhQDNW6dmQvgYDhZDeq8DXgjTnywvX2pTK5Fyqx8KRptsdA0qF-J5MOSsll4IrmYX5yQqNCtpjvX_tvqZDq5Wnzh0vMA0azMVF0Vaf4sc04AeAsqIXf36ZFWXBCDfolmcNgOy4cvJbkJwEi3eXporOqoH-0j4bL0KWO_HXCfkLn0P_5zciJmIneaCRSGGsYhOtE7vn3THc8lg1q2QzXDJX9x_X6CHJtt51CZEPOWI5FGasVqWGeZisqAnCHu1yAjUE5_5ofqDc_Vdw8E0Cb5ifE5VnAYrC7aOkdCJSC8kTN0j6qXRP_cIr3PZFcOWGF7j8vxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
