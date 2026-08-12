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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 11:39:10</div>
<hr>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d21OJo6dZHKd1HDjtVHE3TIxwzejfF5GYqPoBbveGBRCk6OlZR3ReSd-9cnrpG5O9ALjDDfuMH7TolV6kASq2B4x9ih_Z5g87tN9PLeM0iKFuLs7vOf4inZHPNWnVvkbL1Fg0WWLY-WXE-oJ4wc2Xx9BoFWPUTJhzL5JNYfs-7FYDUKZBZzv8I19oiQzHM_8ikvGThDODdEpsPojEnD0I1eREfpZreYDAB1YCuJL9tfK7db_AxYZGCAWDHXS9dLfcCpKKqnWaxY00URg61BFIER4R4fb0ScVz9gFEVGg1sEkE0MGFm8MY_6MvtqOcy6uxlh9ExoqGnD76g78LkKkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
بیمه ی
🤩
🤩
🤩
درصدی سوپرکاپ اروپا
برای اولین بار در ایران
🎲
درصورت شارژ حساب و پیشبینی اشتباه بازی‌سوپرکاپ 2 برابر مبلغ شرط از وینرو فری بت هدیه بگیرید
‼️
⚽️
پاری سن ژرمن
🗼
✖️
⚽️
استون ویلا
⏰
فردا شب ساعت 22:30؛ ورزشگاه ردبول آرنا
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
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
sa20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/27557" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuE3ELj_i-FK16QcAqNud84zrIlJCXnV4JBeo5NohIz3ozW1AIzH9LvhVNMPcEi5HUFQPu70HPK6VPy8_2sAgaHfhx30kiHBJlra0yG1ujah9Q-t-_XWNlEURCNahxT1gvtsxoml7TKF1futkAsLtAsLjHYPgo6KznH5U7qmE5L92UpW_x2pHmkb31veu7aNKhrJ7rjmNSmYHDS15aL1Dqp8Gnx6cI2WPtOryLF1PMYfRGCoDrRdJBHAvkIGpsah70Q-cP5v6duYgJvG5QaY1o-xmQnJHAdUN0h8kYrRqpiuc18jZGXl7wtcAYKeuojNwFPjuuEUVLP3Xqn1a8rfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQnsg-nraAx5n0o20o_l4loAG9fVpqwAkiuSjYVx95sdM4y3CFAeRJ-lCqKoFDtoGYE9J5lDcsQcZhAqtJoY5Mgnu7hhDFJq7SSdncdkrlWcLLegNqsCSoydWvRCHy9joHwHQz2s924hNpWr9N1o_kyrmGknNdBUUAIX0-MlE9sS1p3JIaK7asJWA1UpLMZpsCyKne6aNnScU_kC8S_jmF5SZugGc3Tch7AkZWKgdyCXHOlqXJT24FTr8TvOpZbmouj0DJnqWqbn9FlLk1hG6KJ80JZNOCtcXGfvSLSTYW5WL1UkAizjVFrqtkpkJq6CF7CGuXOCp4A-NxhT23QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNW5oIcKsYbwEOQZqfJYJxrqf8eLU7DXhCQHOARlVQIO0UozW2XCwPsYa10pxRn72-NysQo-LkFAEb3ejQ7TP_z1gzw4Nzb19xsYyQ8hms4k9Bd4dQvFGp_fnU4fVF99eLHLkIzbIsbJW4cCXjjmEsq182YRjEwtBUlQ9pf3b5FIvGZOVWuaDpF7yoTEBkxxzowawUkyLqgoaaXY9wc7yHm3RGc_KkbXfqROSvKx3e0ecLjux_ERbkqvUgFEzgO2Te7HIhasbRwAQYBHz6QF29EE6uNzKGajRtt5cyBDadpB5ZLE3g5SKtgHZ7P8snya0FQ16hFmaX9_-Zu0SxXhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nto7IK_lgOhNJe2uc2mu5C4H3V5I9M7iqrx7A6utf78qA9QlfeYwf5nRujXMxWSiZOANQJjI4MtAe1hzEZ7TVZerw5DGzIj4Gu7GeZto6eMVAcHbu6Wq8FRNuh9rY4eRhcPJXjavD6gXTrxWseMm7gRPm5gB5uD-bPM_SiR3Qf_zYD6HEs8AmRk2BfzHcAtcNCZt0MNCe7hhdM39a4S-JhLPZfiIZh15NN9eCIVupsT-JPSYUBf1CtrpC1_KJEo1Bddns9-2ipjzHFVtdgn2acgpXJJo0gVp1g7Rv_X-URq6WHoniIH8g6mzPkIRoYvww87dF_Dx6rj7KWkQ-_-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch3uTWBc0w-xy80GWTBNt8u_iNkooBUwCH17kNVKC2UF-AMMuPexXOqH21XOfDu_nfOpSfHrvpa9K11-OGXhsIOFOvqlOeneMtKgUb_bsuQhJ5QiG03pafEV7Hpq3aih98jWEy-gGwU78ljAzMU21UdQMCaudxZrFxRPfUKp50VYvZzqNd4pJGgJPxZGRWZHw-6Trg9CgCY-kbLzqWJ4WiZAWZmnU-BNVfwbmBXNP9Nr2njBS06Lk4ER0PpV17Q0M3Kqr2_J1WWMIXuoIg8gU99J7SWEZ_sFRaeL6WE56XF7MI0KeImPnrT2d7shcd2TBj5V87jInECvDOpkSY1YSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v31WyMptgYfZRzIqhO_IB7L8Gyy7OFx1a8B8cA6VwTMIsHcC8CV_dkjBIqrRIE6usiSXls2y4GMfbJQ-34KP8QZ0cNeJqEnA8Ae59xdyUX1FmcmcxGMj_fs4RU4ezUJ5J0YbH6J10E9sUedYDJtfvrGFgljofK1R7UKtkgc9ne3aXQROH0p0SgRaAGa_GZYm6bNVVH1T-dWBZkTuxcfpfksdHvmhLXjQW4VNi949e39cPY08GOJ29AQdAhVYE6YKbc8sRnQ7QO-jpgviGDdygvRgb-lVzzQfawr-NvJA5Bt9HFUkEKyiY7Tmmj1HDH4VAaeZk6xeddyVjaV-U4cBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWLZ8HV115EvUQp5SQDjjx-MGSekB5cCc3dhAmSrmiaC73RnQ5vfi-RKIQu6niN0lEwkN7UFoyuURuq7N9LuA3Dz5gagXWiGPbA47Dnt_8kK7dcLH2_Hn4TXpJzKO85f9RkPnpdbWQl6-rSnTRm2uo_GLv02XZNR0XpshzSUV50NoHDAfmpaHLyPj1ulux16c4mtIX5PWPTm3vqnOPpmK67_CxjLHHfYJY4OmZes4n2u0oNgfQ2dEWMW5qdL7NF_LXWGp-cy1LJLQc32VS0oyJAx8JsFZ7K9L51VFCZlFrXJXQdRg32P6NRD20V8ldplpt4EMKkPk2j1HwMtUrTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgRm-lwBmranb387ZLOd-WL_0gIG1ZeqO8W-cFmi4D5XDYBtb3og1arQeAJ7GPeMJkrD2Wb_LJcbRVkH85V5BHW9cKCH_YDk8ZpQBfI-FAxZzS9RoDrTytA5eNTogsAvK5KhlDgGFf6SCcAEwfY071hQc9NGTDI4bu1Gz2yCz08TMXLukXFCAnmdWrQnbcNH2M7XVlSBF_jdcypWkVOgjz2r0m4TTnfQYor4nTkp6uqKUsb0-VChnvCnUHTvRL-L1QS8FOgOtCkmH20TQeljORcUEz9T1ZflkPdCpXbzGTERYcCj7yRpyl6YXoPCEhQTpaqqB59XbiqIF1sBUf4-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEk8JkR0rTvTv5Kh6A_UruZNMFYgYTugf-hmP19LfDMECxyP668bP-sTjZscbaknTVaF9fDUb3skA3OSPzqky6B26eDYzSLbfLl1gNq4mc56EsKQeGimaLZVNeJzpH_QELYWUzRNT3RZ2pWmKPBW0UnL6fIgzdg_6qvPeeKfERTLc77aUv0ut24Uo5iwuPs0IZjAtbcjdMkjAB3yutKyBFMbyu_nN_Rs99SiecMBIoMy2ky7KROfwA26WF7-L6uAA9QbVs0N6AoJM-MlGQ_BHJ1bl0Y6WvxFGRSupehWdkTiuoDc5lokCwvdZRfA4KXfWgjp_pX6ZAcgAm3udF5Sow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIly9VknKn6pViGsUQbC-PlVOLo6vL1UltMpzX1ntZNmHf387SrgcBJdZzQNCp8CcSGVRSs0wHAv18IFDpxW9sWD9StDnhWsiYNTP6z5ucEv1jb5o3HeeOondMJgjTM9hOT1h82enQD27SAiDFnhF5BzRYelG8WUCnxLmlefODrkWUf4o_8i-goE_0d1jL6r1pE20tW0_HIgquFxydT8L-Dz-D8X6UyC10RZcgzSzLmMBB9A1BC-NJ7Ftrtq761GMOlluJ1D64jQoE8urx8p1d6yKzGte6ChA6OwMXwf6FLddIJN-gni4cxQmRSyfNhxxJTNC5QLMiaMayQ0S5MCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh8D2xOVAP7Or_u76l2FxY02OTlXgDAZP2jAo3XEOiDFfzfYC5d2zdJ-y4kbGCfEiliJXSsTkE2qBjYzXL7oS9hSpUY6js3gXbmrg1nTDWmOwudVo-f1zkLIU-Y59sAyTT94s0efak5UeY5SwJnQaeUAH_y4r79-EY5R87pRhgKco7MvReT2j98G-Q-JGwAEsTgS7p3EHSosMqA40Qud7M2S076I0oMTxgIpCOSfYAWzRWpgcn9pqHiMbsZTFQxc54vUhm9V8h8ZlGr05sKYgZTUqMXTVBMTfruf04rcWyequ6KgTo-g2EyhNd5ztdSHYcxjjc-n97lv5eNRLbuu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-QZkilT6RQW_sWiL4RKZTLe2zsmWTcsB_bPodcUQall6Dkbsxm3QPwjq_DjVg_fRYTBoO_I3tgnRUig9hllr0xgSbJyiWRgVJndLeMegCINpK3rzrOWHF8P6FN_HmyqUQGR-lGPh041S-2VTRNBWSivJ7aZufsEOqwha4SzRaYC6xRHeoq4VmOOmI67kaQfLfDhjhN24nALz1vlb4Zopo2pOlt0OCorJ9nitCz_TNpl0FBh9jw2esQiEo0b0RQbvMddSHuDtwJ2lknOLABt6C1PN-jfjzjtQnKHFIE9LR2MVAZTs4bzSQIzStjzuH577oqlzSFZFP4OUGmJIG3LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57Aw0qXC6wxngR9FP779GuAtR5PXaO12aSdo1FIXSIqGlY3pkjwIoxomOn9x4TpycIDPRYcPBUVcF-55rroogJLgQ7Kvi4ZEPH4xXP6klXFGxMFeewkOntMl5OPtMPHASb8U4IP7zsio-P6nNhGWzngGmhYg4fMqJ7i0nGwUxcReVbaKUVWKmCp3aaBGhrHE1GIYh0kf21wm80XerXvsvwRrNsbGJIXLtEJjIxDSi43BizIK5s4F2HJukiLfDsxQAp17X6aHuM9m0sU0hvoMcS-BpTTEKLtMpvceDKUGPIO3EOY64CIzhBAUMap09m3apnwOj5svGK0GyGrFXhzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue7JlZe3d5lfkjtemBm5lzYnJcEsuM6pfgI3Ved-5UqpxpO69UAMga3o8TZ7Kn_Ldszrx2IFrbq8AHELUsju9w5rqD2_KfBZNIH7M0a5Ios6hishNi4WsALUdHtKMZ77EtewuAHupHQkfUonKiLQLLic_O2ZsmrkbrtVOStcaoSowxACjrmiqzN7OmU5Ej97C0CrVZCrhQmoTYBUOpnNZiDqnA-zSy3E_YBjlBqoEM1CI14XV2rsLvGudLtsWdlkNOvv56AT6oAfRMtoQ1wjIXgK9wsfwSqsZOdEYH7X8TLkh8STmEUIZm6cZ1wXOv0ONyv8WSTJaPy-olfHUbFLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-FT3mgO4jYBaMJH9IgHpuxZvm5tYpBZElPGQfTOWvQNV8rhhSf599z1WwyIF1GnQ9bL7RqGoNYCbZcvSM7082yYev2hZlopoMqYfV2rF7bouR70SfplbHQYI8w_7Hq2g0J99FLZ5cJCP4nXi3w8DjaLgyCgzxWmmSA0mv-Pp2rBQYPSEywiolbr2f3ZMs2rSoc_noLyRQh_pnrGujVLEJiD5IVqj5jbnlLwgXf3_vMDwqwk-Nw80BN8GbThcYdEICZj1mrG7W2h8-0Og1MoL6cvVasfSHUEdF111FtcciwiRWyLm21ObNHK5mCIDq8BMDUWOfDTBYuRUTIM3GIzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYj-rne6dCfIxbn1wICvGFmfpE8s4LyIV4ApKFmroa2ScUTAcfxzVatK0vzxHYkdC0TsCv4u5diKpusIJ45_fzfpUxHZYB34qzk_nPLt2C4givGBh8m_cjWGfZjWuDIZoKLkxYzZv92OC2mlMMD5Hu6EqWKoFlAtATJ9V2nz8y-uqljboGFzKhDISUFubKtMrAXEYAXvlWeks71ohR5m-r_c6FPzGh-RgY2-SXoedoilMM9bK43YF47EN2g_nEJMlUNbEesnGJaJ1xGOCismAEmmCjc-EiFOaAb-0hWI7ubFwZYUL5ipcnIATVy9HnK2uaOPfPafEgigRaO1k-MT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbSV7noVWtJbPo0llB9tYqspmu9OsUbYnAM0cTQ88gG-gU1n2ayowQXA7n0G4jpo5H7F54DIIObu-u2bWfZyHvhCiBFsRlo264S9OGrgMGEF8-_ALKHSozK03Ti3saurJR7yGTF83JgpRtbAHEGSrHPlXP5K6H_7lQBvUGqww-kCLpX1-qyl4CVaW6Gqd9cK0LZOOeHsc2G3se-K53fxrc0klTkeH4ge9EvCTdt3M0IsRoP8XBFm4ij7ZBnwemf-qFQ66tr2086sSNxa0jIJx7HURHrcO23qMyuGeAnoX2rRoc92ptQGIS1m7B90-lf95dwbSC9Gb4vSq0zgg-7v1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab4L7NKWLQMtYL_Fzb9XqrpWBZBugnyv2g1ZK-ZiiR0vzrr9IoozZSAcuP9udeI13yiksnmdEqZv9kFK1y1f7EQd77A1goL1m2SGJk0xH8WTMO0PGO25wkQ0-4EnWu7O0oWc2IQAy3kleu66MA63BolXeyjkkiox9X9KrstpLjpXcXehFpEW6pxn1fSKJlpJs5rVMZF6U2QvM52uu-yUFewgxuDBAWdWkAw4aELNS7VA59wdxqeDqAOoU1PRQAcO3w_17yc8QmJngnjfO-oPYuhrCzslTC7tppnEOJI6mOhpStQ-uUM7LL6sYcfQvh9N2DwJJKkXCz8Hi7nyP4LAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOV3My-CAGUfk_3OifAcdzS96dfCXiS1XIszf4_hEX6VNROq0vfF-eeRbCiU-DWJJEM1dC0Fkpjh3uppQLTAbD36T38LXd-J4cacky8XboH03kZ0V-zZo7S1jqlxLt42jwBSxD6XQekj4RPn4DnF07hbw_h6FYsKcRxO-Aw8CUHwwK3919rnfgCs1DrW2EYtD6npcA5TH99DOj_viU27E3rJ84e2PbpwGQ51BbMarI4vxWAC2dPItTpvFV5RsQ1YUFl_hstn7T8d8TNzSE_F-b-uRSP8567JMfJ8psmkiDn76vBEGDJbi797Pl2epq90etMmV_yEsEgMgdsTVTmKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtZOx5ysFlCRmQvz_1npte8jHMLMZUVPDDE_um6iAceb1aRjQcUXGuU0KvGHveIq2Y1rcDuxtsLlCfLRbXq0EDDPVa1ySYiOGObzHuoJClmOiQEpsNFI3V6Wj2-HNyy_fiNv44G6p7ca37QOG3tX2ZqWax-FuWWa8cY5MLhqp2BAZCoD1-RjXn1XmhkVxmNqtzFKYJiCJ9uLZWRtQmRHmdeC3vvM_rwI_MbWPKEFBfHmngb8rs0f_wv1v7yUQluVF44mTRvAIJ-wVAo084rI38F4ulforQ10Cy6t3QqO7MLS-p5LD99U9XNqwc3vkWfKlxcjVe8u-7gvOSLl9NqI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t49iErQbTjbk-cpvRgZcYR9p8FOADyb7cxqxVvFIPvDLpeczwDyWuaLAhLQp7erRps5BGEIjr2OWu1pzXvRQ7BzQVNRiuqJ38c6wFYa87B5OdHiFqqUpyzJbyVxjlGiHLwervcBVOJfU_YcqLXsZmIJSTcUOXQei-Hyiq9fkTm00k8SW4fsclstuAGHb2bgWoHb3QkX5BzeLsHz7mfkF9NCchY8I2lrSbg9K8Wzh1CEexJAjwkIXbFN5Yhd_hIAXKIH4tHxy1QyNGOffPt6RLwAqljU4v0sXVp9Z0bjICXI5kO-IcgzXD4EnB6RaL2n0giZwYrP1DY5Zn0QfdH7yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6TIeWy3n7zyTUWml4XoX09gCPoJOfuyjzCJCuBCrv54C-NVzUCKZSPBEbXuYE2Tl5fRnFed7rz_sNmtJBgG8FUccmS6K76_PNkJW5s_MIK8iwcls4U67Z790HvOd_c1d5C7a2k6mEJDUnOXULqW_YAbQ7nq60hw5jEH9UQIfKTFVItAWBBmdVKakCZBpvTC05q2NwNUmUK5Abo107ZFIQ_ZRVHwsRk_D1Ct4QXQIIH6mGCiDikWMEqreMf-pZUd1d6emOjUjPYCLTeiYFT9jJQwwrZwN4PXf09A8MzgeWx-0rvR1YJRiD_BFKkgK6Gqvj-3w-bLtAoZZkR250uBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=FqFQWic5fROnHhFOs5iApMhDpG2MkzKswcI1kn3IKW5wJ7orgVXa-bJI8myr2H38UPqoJlFi2C2lfH4kS8TfSWE7P7edTZE9awYKEURyhgk3wzQa5mG9AqkgiY1nF7imz69zOD9hHSmzkZGdBG3_ucFt11TmbaLEA8qSHyHw3BcQNMNl1__aEhTOxhFzhyGp71mbq_rIvHwH7i3zb0h-zRUVFXCtViA5817-mKPIpUsMRPX7zEch-iXYFnoQM6ZSCZezRxOAdV_cxk0y5LqYjzh7MrhPFCpJh6cKJz6a7fgF-w2HDruJ3zNwJP99bQMfT7JtXX0cdaMpNw6ksug8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=FqFQWic5fROnHhFOs5iApMhDpG2MkzKswcI1kn3IKW5wJ7orgVXa-bJI8myr2H38UPqoJlFi2C2lfH4kS8TfSWE7P7edTZE9awYKEURyhgk3wzQa5mG9AqkgiY1nF7imz69zOD9hHSmzkZGdBG3_ucFt11TmbaLEA8qSHyHw3BcQNMNl1__aEhTOxhFzhyGp71mbq_rIvHwH7i3zb0h-zRUVFXCtViA5817-mKPIpUsMRPX7zEch-iXYFnoQM6ZSCZezRxOAdV_cxk0y5LqYjzh7MrhPFCpJh6cKJz6a7fgF-w2HDruJ3zNwJP99bQMfT7JtXX0cdaMpNw6ksug8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9ZQx85Ei_s7own1kK_e0BuHEdg5HXkhV9gvxBAg5meOulO3z7ESv8jPQAvYfK3mnY51zypiSfJvQT-ceW1iGL5WcG-w7Euj2PEyl75Q4p8tOkfeFavDOmMa_pQe9vhzM-S4Y2kfhyRlGErTMzgfyPR-XnTEpsKkh8726cSmnmH_Xpu5xsOuYeqk6IM_GJR2LWaIRaVE-pfhEbegImXOWNSKEzUZ1JHsKkUi4FNW7491_jQ-U83OVFLxVBKPWETessrxQNAKhppAfMVlFkto4xmKOX2Ot4RkOlX7DkzlTI_ObO6sKIawA9tNinoefy0pAmWh9AKXBtMK8sE1zDqB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dllg2ED7oE-8FpyUgLs_6RVcqhHjMJSmVgI06tTUCcCpiT1yhn1iQXQPg8c5hqf3eBg5JVlB4Xs0YRrHHIb83UcgEuhQmy0NZKj8Kg_Ms3fb9WPIoEPel8DCO0iSdODVDmBV70-F086I0nIU0w896TXB3MU1ziEkKkMBWSUeT20JzoJ5INHMiFbZn7pmDwo_CF02AhRtv0hqJUdbfJSnLIOtOfWI_d0IvmRg8KJrEAqGkAQIlbvIqcq3YcSHGvc8-rBNG41pq061ejbxlf1UBtU7ArtMRtevuH58FqEj2LmgLmRaTbrs9BNmSj_Y7A5-0rCnHil8nKgDC1N2n31V_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euVfWb2p1vC2AWkn-3lJvNXwMSXHbG0ii2V7rz4bUExc7gwawLyg9aso4XtX93funCGVOTaUgmuZbPtcT_wLxauTXmnaBOQYXs17tWQewXDC5J_tByMhkJvU7N3KdzSE9dHcUWyPJfyuYrhrxEYSXl9rIxjkJCaAuRDr-c4hnXzHyBjo0pzAC6moggFw-F8qyttcUgb6nxriqyPLKlrC2Vhpb3os2mFKLGRjHkZn4L4GrjnvByR_JO3w3iIpu71AV7JTmhvcBN8qaP2m3j7eZgN5Ng81eb-zJgoPz4cR6HJvJ8aFsusy1kBpZKDyya15lo5yRohM-ZiLnjl3PP9Veg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCVNa0-nCXtDzkXqbfcBomWDjWcqtlKbjjDa-CDQVZq6VdjxDJi-Qg6deZtwbx3Cs0EsHkZLMdemypIWBVj7UAvF3QX6eCKQVWJmEkoGRMlQt0ymCvPe5JhVrxRdWjJPXc8aMkWhaRxOmVrZLqRDqcHCCz_IeU1ENWODRqMcO8kftzS8J97lPI3BonHWKzoL5K_igp-u3R2J-hbpUyYZAu2oL5pLFjUhRrHH4-QLTxkM1MraMcte6OwGtVRIzOMgGNUfbRt-r8iELZBYV3yo_XobjOWgJRW3IHhJnkxAE10eR6GgOPWzRwaNxAwGUpCxQ25ZDl5cwPYqZzTgk1XEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=QVjLcq5R02f3WIkW6Wk5mj_Hj95T4TH7RUE3yyz4MWuXjWGcPV0cZmsiZjmHm6SNbN33zum7_vV9kpvsNq6BhnYbIcgvfuXwDsegOjYIMXRNaWdun-jlMk888eB3ltWgMwDfPyEkh9AvogIe3AKwxnqFXj8ArganOmFCjgiQOcSFSqFiGCVWtlkgTILRJv9J-sAxFL_KJSlCuabi99pRHkwRJUwast4lH-a0mmMqRSAH1ZjxUq2NnRP-F1sU1ZghUOuKxSO-5G01LhADxdMnklxib2J0wNYLw4wCklFZoUbpinGGiYLjnAbdAWLwX-UzCnoh2jl7kZ9eC8oTVVrFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=QVjLcq5R02f3WIkW6Wk5mj_Hj95T4TH7RUE3yyz4MWuXjWGcPV0cZmsiZjmHm6SNbN33zum7_vV9kpvsNq6BhnYbIcgvfuXwDsegOjYIMXRNaWdun-jlMk888eB3ltWgMwDfPyEkh9AvogIe3AKwxnqFXj8ArganOmFCjgiQOcSFSqFiGCVWtlkgTILRJv9J-sAxFL_KJSlCuabi99pRHkwRJUwast4lH-a0mmMqRSAH1ZjxUq2NnRP-F1sU1ZghUOuKxSO-5G01LhADxdMnklxib2J0wNYLw4wCklFZoUbpinGGiYLjnAbdAWLwX-UzCnoh2jl7kZ9eC8oTVVrFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFyOb-mLEHCfilDGhGpUo8GnLI9jcPpD_eawqZ8qUrFLUfB-3wX-D7Zwq97zAY7hnanzQl8HZgtStE_MMe_Qgm07KKtJ6cbZrPjzgVzVN6sUbMg4qBuuCfFOaK-CAdIq8TAkTrrkoU3dlv-8x6_PXUKciKGzQ_UFLVN2uiyn_rVURkdNkvSECqMLuAjvlxQfqzgPOec6TCxhzKqH0ZtWNLsqpxdYncSFtwtOfClaMpLVjUCOT3E5DmK3keoNV9oWPKFxf_qd2Bs38Eh_bFWflFoOc33i8yFK_Z1aeuQBlKtZyUzsJCyAQ-c24HpRemfhou5y_v3jpKrnWBGbuuyckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1PN5auLAOZWGdRlvx1tv6SQ6Ke-L-nSRpPNvXPrnr187C5T0wAPkGq8uO80tAkcBTOfHkLtHOdabviXnz_PiQOTL-8kqcZTnFY13BvxWsb_RkFlgQ27eFPeTiCt6R6wJCGG7L4gtDCvyCpihy06rIcpHm_-Xg5FIhQSQqiZ5hYwexhwjpl95jPE0UGmzXBw7PeBeS-2vCiEA4kCry_f09e6Nhy9xuty_0WG5u9jSKGLouT9da-9IPSFiWAAACvnLf3YKjl93_rgJkX7fcP-CdxG0i1pqB-bzSix_7AVbwIe7sg3xNgRXgOmhYeofyryDqwaQ5L8DHQjZfJGTqPRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvd9ZyTvFE-lpntGV7dXflsOGtF3eejBp8kJXKJR6sWkVDInUGU8IostIHNUNOyM3-gyAYOs-IXNgplsp8qseKBKieUEg7Uk6O6Nd-4ZLGtrdI6EER9aNSf2auGui2XgTHJuQy6AIlpveGaegKM8yO0DLcngu6ut5PrMlBUXF0dhLVmeXaOXFx_28pyDb-RWOQyGwMN55rUiRAD7k3ng8YNFks9kkKFdlRJaxUzGwqZfBYQhtJv5iWRIBrCZqw5467RqkozT4UN005oFoLITBH9rCLQw3hXMp73-YVcSYpjCytArtbVG2l4f4yxufNGYRMNf4N7avv0NfDSCZ18FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENYYG2jimp6lU4zpxG2jHk2Wqsj7a5a3nQzB7cVAGerStmAYELDuD6BqQ6B2KgWE2FIiFX5bIrhA-LslegPEd-LzbEEFzw4Ql_76LAuQSUFENoJxwq2y_5Yk7SB4IF3Cy1WAz-Wn1WVXftXkJNJZvskAJ3j8LWoibZhR4NoFQe8yjrzbsxuxIUHk3YFHh2mlFkas0skacRQ8dQ9OnmY7JE-4uJRx1AIZKETxO4f1TOu-MUx_n14OqfaNugVzeNohLGNiUk5qgVEfnzWxzhZ4lGVZ0iJyJ-u6AM8F-hndcyrhhk7QAL3OPZCMh775IM3rcEWjKRG83zQeNKIJrlT2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjiMUJ4bHQip1_h8i7KzqcyLhQdUTUMetvZZ5ZJD4e9RtVhxlc49ULROrF0DCm3YHQbiVNrUC6ySAceFtt77enr9UvgBN-bpPox3Pke_bhlD6zaAH5lrcK625JJ2YUqQ9pLesx17GzizQWQg28tkA0u9UPv4jI_tc8y6JGNWKMXupVxqRO3QdvUTS75TFNyTDtztLuQ4Qx0rZ9S9QQA5jpbl0b9v2oqFkYZt_tPKK931qTBNzTWJHSVWsM7fPJFFjFCljtAeIKKDMtVhj3qvwA1-_4eWe0dfg9aOukg9SrkXl0VmJKWd6JSfd-colKnSR2zeM8rTTxIUnFereJ2Rog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0A7sOTN7nyyXiN924NKVza92g7E9TlLyvZNRQO88gVIjWVB0cHRLZZNP7BRWoNryDR0v8NOkSDLQu0wUFExKaitzVmJFnuk1Wb-ogTcK6nRwPeRH28LwIUw2oo8Rz49o8W6AyyLkzOC3zqRwzr75QO8UMfzsb51IQ-yvyvAorwSYX971LKs9rbhoiMiogAAlKhjXqpxU-OX3h7--ZmedPIQHBA6biw0XMiHyNvsii5VYR8a8ooMyLa5Vc7v62G7J26wjBNveGzO7SM-VPHN2EKVHjexY6qd6sGon1-TMH70_Wt1fatijpL-0PXZSCMePr5YTIl5SpS-iVHew_S3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DByjzch4hcIuG4rNMomT_Yp7VNi8ndNi4n2Q0HNxuam90w6QeQlanGpG-oGJfugMN1R8qypn7MXM3NJDrcN67qLEalNmFneroHMh5mnypLhj-3lQym7zP5WnVwHV-VUrnKlGCjM_8bdoQaMzKNjLYPmgQiayM-KPKDTaWVJPrqH2lfrRrHN_Ct-EKH65DWnrpGPqrH6iRg3XbgIxgbNPZPqo6gtBSzs13GN3MiBtkG8HrpOuPxboOkE3WW6T5JW0bu5I0_9pfzgLgNe7k9LbRN2IiGQmNpOAaetyTd7zOLM8AnRWIMjWZEvkBi8NZj96qNwStzHpUAaiIA0KhSnG5e4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DByjzch4hcIuG4rNMomT_Yp7VNi8ndNi4n2Q0HNxuam90w6QeQlanGpG-oGJfugMN1R8qypn7MXM3NJDrcN67qLEalNmFneroHMh5mnypLhj-3lQym7zP5WnVwHV-VUrnKlGCjM_8bdoQaMzKNjLYPmgQiayM-KPKDTaWVJPrqH2lfrRrHN_Ct-EKH65DWnrpGPqrH6iRg3XbgIxgbNPZPqo6gtBSzs13GN3MiBtkG8HrpOuPxboOkE3WW6T5JW0bu5I0_9pfzgLgNe7k9LbRN2IiGQmNpOAaetyTd7zOLM8AnRWIMjWZEvkBi8NZj96qNwStzHpUAaiIA0KhSnG5e4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9rp2vsGNWQ255WQ6Tk_LPvKcLB1fMZq88NViu_FHOvAjI4lP0A81iEXtm11ZoxPxU8QcV2eHW5QSHKnauuhlJ9zS-B-ox1AVp0Dql164yjAFM_oC0xhcEGH3Tzr-SOO4J2mq1JSek1w7Gt7Y6_WFfTJCCdAMR-72n4RHh6t0CkHElUlnTBh_zz1piRj8uKL1n6ei-2bwL5J5QiO17cJY65c56b3a0ylmgtm2gPB-0VxMGlUBnMDXoFUr8H_h3z4_WjlA_Uy65DbSUON9I9UcvI8fgnmTNveRQ5RbWhGOy3a9maIDfwaS7eJZpDiXng01g5Xv75B9XvjaJZAk0o1vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27510" target="_blank">📅 11:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ-WrVuqouCBnFQVOafXFIee2z6FMKiPenGGrFu9rBw6X73cg8Kd6pW7-7nbuSEXj-Tyh1ZgfjKMsrtiptaaf5zHA9EghHLgBA3WcB4yf4CsfqKAsbaUycJ2i8r0txg-YPd0UXb7ER2KWQvA2oKv3KOSuflnAOg1YTv-ljZXVuvNRqI2UvpYyMzQ2CSvWU7NTB_XMtufzsYOJiFTwVgvAGnbDpaLJzpj4sf_ypT0sQvJm7-bJZWctDTLxLi41TirQ6W_bxoE3XG_YGR_Ph2NJ2The-2J8vdMTwD6l0lmntSxN7FboJbPCqdldFWLeA-NAJL0bDYnoqjrYN1mu3a4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDko6X1LfIgRG5mOKQR6TfUm8FOvuR4PJiuEZ5XOu2dt1HKiGLbx8FB9ThjXSJpKrS8H0t-HekBnyoRVxTDfm_-qswOxRSLrCCAsmigxSZWx_ttM5etNX9CwsBcZ0EBgYRLF_TrLhIuVk5bRVFVNq7v8uFDcmw867gl1gnVqcqYkFEHY6fEJIjs1S5z22Cf1i0Ky-2VbEeqtZ9c5e9qPV-iFUfn1QSg1QCDozKBPzPqRxvPN3R0riv4g9k2PhjYvvENTb-qv0dhjXgZKXUi-DnLHBoDFY4GDpdyA62JF5WpO-A91hBlgHvX713CsuIVLoLJLH4oQZ-PiTGtYt-Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=opbFh5r2Q_JSnEL8wIXI1MhjQGx7C4TN0d8hPR-Wb7mwFwFwX0-lnvRijse_gCFQkYeZciWQgtHULzbXAgfReLaQ77XED_dMp9r4Yf26PHUEkamI6eZYRox5XYD9A_V4z0alx4CtoZz9vDWvn7pWgLPkmVPb0WsQO-6QB8JZ3RK22AJ-UiCJl_TaZC8KebGD_F02sp_KX_DMvvjwUXGVgSLUCQsndoAltz35LPKkTXG0giQvDusWbya0AoQu2jTD0swpSBdUXcF14XUkkZaji11S2j9cRchnaQbKlts0_aKjO6i-Pfa_IL881O0yL-V-y34T7dkvqxjtReFgHsbe5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=opbFh5r2Q_JSnEL8wIXI1MhjQGx7C4TN0d8hPR-Wb7mwFwFwX0-lnvRijse_gCFQkYeZciWQgtHULzbXAgfReLaQ77XED_dMp9r4Yf26PHUEkamI6eZYRox5XYD9A_V4z0alx4CtoZz9vDWvn7pWgLPkmVPb0WsQO-6QB8JZ3RK22AJ-UiCJl_TaZC8KebGD_F02sp_KX_DMvvjwUXGVgSLUCQsndoAltz35LPKkTXG0giQvDusWbya0AoQu2jTD0swpSBdUXcF14XUkkZaji11S2j9cRchnaQbKlts0_aKjO6i-Pfa_IL881O0yL-V-y34T7dkvqxjtReFgHsbe5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXPTjEsZQDqd07RwepYIxi4fxpfL5ahP9rNH6urL870bEkkRMrRI2gMdzoL9LxV5rZ13wwWixDkKMTqL62Mw1IWaHs4iTHeXs3jsfivb4OK730VlEHfsFVCZ1M5OMxeZDVMco--kmQ887NL4uVQrdFTLjwtXKvC5K8clvwm5JjZlXHJNe5lKB5SQebzM6OqvPdpJoLCURkKjsW7sECLHl1jj9SST26yO9M0yt3ujBAG6pURwxttafs8q7bB_Ut1eDgiStYqijOP94u0MGQe-zYD3uuVsogVhC8e_vuDPraf-NqqqAu8xPlsX_YF28hBfyMMg-SiB52-OaOVyCn505A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KESj8hO6kxxUvCbgUWvtV8tjNUgJkP8Q6eg777sYTUM_Zyy3xiCRAtL9NWWYekvr3pWvmaDD-25QfOXqQiA2T_Oyz8pvi6-S4kjuRJuFzGaZBcXJaqs8ureiVJTjeW5zFtMPr3HfnB2APAEq3eRByu8joMNjyDA52GJPYlZ9e4ke74Qloadg5jV4gZPfTmNJWNOHpL1mmJyExSeC6rwfAqoTGXF4K_WUC6fiIcXWuzWIpcvnFJvgGi1oo2jHbEREKNZxMV5r-UIDlt1UOeh9XQTsjG8Cl_iqbmIZg4y1gxE7yJYWV-8wf-YuEsL2ws18rMZS014sY3wdYjhonAQthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=vGBCp7XFxsaKUfJHKJ_VfFx26Fpfak_wfpS2FMwxsNy5Kf6DJx0VRzZgj1JE0oHWEkSCaod7feMu09L7QaBoqvBVdT23JMS04Dto9uHDyIvCFfyIPzCce8VsvXjRj2CRqK2Ix3o795Ya0pmCcRulurxFRKYV4u3_PKvOc6Kpz-6bxwHI_2qnzte8XQs__Zls61IBqhDzBejZWyWT3Ptn5vpt8sHSxWrwJmD9dd8xuR-ufXqXP5MId8cczKLgyD4kEmns92rnE_x_c_poVAGQDMdo4C0pvDGXIVHauexqFAUOZCU8Tsfsap8zQkn8pmIssiEh4DvvGYNrM04INkEg8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=vGBCp7XFxsaKUfJHKJ_VfFx26Fpfak_wfpS2FMwxsNy5Kf6DJx0VRzZgj1JE0oHWEkSCaod7feMu09L7QaBoqvBVdT23JMS04Dto9uHDyIvCFfyIPzCce8VsvXjRj2CRqK2Ix3o795Ya0pmCcRulurxFRKYV4u3_PKvOc6Kpz-6bxwHI_2qnzte8XQs__Zls61IBqhDzBejZWyWT3Ptn5vpt8sHSxWrwJmD9dd8xuR-ufXqXP5MId8cczKLgyD4kEmns92rnE_x_c_poVAGQDMdo4C0pvDGXIVHauexqFAUOZCU8Tsfsap8zQkn8pmIssiEh4DvvGYNrM04INkEg8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_r0TFMFBzymlQvn-vgSM7H5g0pDawAon7Dxxi1lg_nztFm4Nh7kXGRLvYVXGT42nKl_J9q4CAB7dTgLTBOuAXj5Pf0pFELbyzjiqyi6JjaCF07vI9eTHjrTPCAsfOyL4VTrbtXOuSWxM2H0UOv89H2pmtqcSrpDZVbiwIL1PlqgCLCculBWicYZaQxz8krWFM10ggCLvBGyxvRYJwyhEXsvsJfQA4qhUvksjxUMWXgwDjb0sNeGydqb-B2ScAfLKK7xCRGqQ-L8cdujzOgY9LdgA-HcK4zv9uTDPy_x89yZaYSboLiwIdIB5OhkZxFGjiM96shkAT_JFutH4t7sbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=o5VfgJGVY-S1kM1oy1bcM5YFODAJdx9S6v8QQ3gSpTsZjzFVpnUJ7PbGWfLcm0-wnRlZIav_wAtMIK8eLOutQRVNHimEdmGMM2jJ1_DkdRtajO1baZcPjXky9GtoamnKYUINcaIvwFxs5b9cJjPAsXILKTc-cMUC6f4HbwLZOstfEprJpHOvz-z_n0AwsS3h6zrEP2Mtelq9uUexMgCQjGNvleeTUAMg5-87kcmK7MOK_3x4PmeC6QR6DPh9Z-cTSWTCgggkxmMXkE3z88OcwBVq55liZciiQVV7ermAs8TYa5b9NSf4JCkXG7ypGS19xCXt-ujDHVXb7ap0SBsJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=o5VfgJGVY-S1kM1oy1bcM5YFODAJdx9S6v8QQ3gSpTsZjzFVpnUJ7PbGWfLcm0-wnRlZIav_wAtMIK8eLOutQRVNHimEdmGMM2jJ1_DkdRtajO1baZcPjXky9GtoamnKYUINcaIvwFxs5b9cJjPAsXILKTc-cMUC6f4HbwLZOstfEprJpHOvz-z_n0AwsS3h6zrEP2Mtelq9uUexMgCQjGNvleeTUAMg5-87kcmK7MOK_3x4PmeC6QR6DPh9Z-cTSWTCgggkxmMXkE3z88OcwBVq55liZciiQVV7ermAs8TYa5b9NSf4JCkXG7ypGS19xCXt-ujDHVXb7ap0SBsJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9LH_ipxCEwm6n1jQB_Fu8xUvLBNoHAT2JkiT4jeE4Uxkl6KdH2RH1spzVszGSCHki2K2Rc2WWEmoWa3QcdTUkyCdnw0Msf8VApPUT6-69nSSY5nM-otSxO3DClK_1VIMpkVB1k77zijsQbiW-C4IIVtK6_ESlNO_vd2AkIfuWhiTkF5C6HQWBJWrK6HJBpjET6X_1nXT5dtOFlFkKQemKQdxOOnCbdDBQMoe8XXKCLPFzd2Pl6KRrz2nNUPwXmDr0-agj1DJ8JoycHtK-RtRJzWx92xEBU68zrQw_f9ioDBUxY7PCe-Z7ULpi_t23Kk12nOIW37_-kMeFEo2AhUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=eFVqPOdXQ7v4IF2zozgOTs4Z6okLD7q9NXaT8fu3CSdTVZnKmQpd8PePTxuMqns_-DXCFy0hjEuTLvTyb7qxcoCZdekZ-hg9fAlRsBJvQ0dpi4hp7cSvclGB5EQrf2ckzrHKTaMexA-8LntKrwD6Yja65BWxA5U8H00NLmeIbiwpILg-JtDSCs7Y5VQpO1af82q5KXP56ah2UltuiAh5SzAdyrKdbrx2pjIs8bAxj9WEBlwrNrEnWmuQFJMNiI3JLV3_MC12R2jdd42O-03GmoFxC0at5YIrYoCWvIalF9kkWvoswWewi-4FhqRMWYjrPopWJ2C_oPRUBTm8gPV5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=eFVqPOdXQ7v4IF2zozgOTs4Z6okLD7q9NXaT8fu3CSdTVZnKmQpd8PePTxuMqns_-DXCFy0hjEuTLvTyb7qxcoCZdekZ-hg9fAlRsBJvQ0dpi4hp7cSvclGB5EQrf2ckzrHKTaMexA-8LntKrwD6Yja65BWxA5U8H00NLmeIbiwpILg-JtDSCs7Y5VQpO1af82q5KXP56ah2UltuiAh5SzAdyrKdbrx2pjIs8bAxj9WEBlwrNrEnWmuQFJMNiI3JLV3_MC12R2jdd42O-03GmoFxC0at5YIrYoCWvIalF9kkWvoswWewi-4FhqRMWYjrPopWJ2C_oPRUBTm8gPV5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv4lCU3jl0HEG8f5zXk3w1KaUBK4OFocKQn4P_WVNNa8PDF4kUi_HqLRvPesapXmUCirDJdKrIcBSnO2wqnM8300XjnhbYhJbidvqbDV0P4lYrhzJoScS15prapG3_CrYa7_xgkrANifdLsSXWlmFOH0qDK0kpZ4BtLrJzrU_9Ax5qqdxpBLAUkIfc7Mw0CfpguzQ3v9bPtoVBYW5lYfY28MZ7_thEZGBcI_1jGTGi1kUeCqZH-JbjtmfHoKK5xBMzD6c7lB6mzys_jMreWzMLZvJ5QSMDXhzfHZg_4CwN-uKedEy_Sc2VTQamnUfh4QwLI3T2HQHvtQf_PBYHnWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=XLjaD5eUTkTg4Hb3DdwNjzj-XnDNLZJAS-pA0cbNoTxUS3GWusuyy4giszmnlxGMT6uAad0OdTP2oly0d4nJ8705ud-KeQax0yGRSWuEZQB-pHvoYLyM49VRfCeghoo0tbnayj3cEgFAdQbAHfj3ytLlaxmQFFeTPnRKkmnzZJWKC-4Xf21D3dnN9F3Hn3HjcwVVabJOJOjjX56ci_Y3FR1OAmcr2zbwl2_SuTSYdPwzjDueI2dgER1cUXDXnzZt5phOGg9Q47G0z-KHycQTTNTlghQlxoUEnkP__KFLgl_zJwleAUxg6rMq7clDNghfpQjYx25k2aj1dgtchsfwoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=XLjaD5eUTkTg4Hb3DdwNjzj-XnDNLZJAS-pA0cbNoTxUS3GWusuyy4giszmnlxGMT6uAad0OdTP2oly0d4nJ8705ud-KeQax0yGRSWuEZQB-pHvoYLyM49VRfCeghoo0tbnayj3cEgFAdQbAHfj3ytLlaxmQFFeTPnRKkmnzZJWKC-4Xf21D3dnN9F3Hn3HjcwVVabJOJOjjX56ci_Y3FR1OAmcr2zbwl2_SuTSYdPwzjDueI2dgER1cUXDXnzZt5phOGg9Q47G0z-KHycQTTNTlghQlxoUEnkP__KFLgl_zJwleAUxg6rMq7clDNghfpQjYx25k2aj1dgtchsfwoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmoxRU1LdIrIMre_TAFrGqfUuSyEtuvTB2NhN9-2lZgZYgOxu_auvS4EuToYPpwpuOgTXUi13rgZYsfrA4FGQbVwczbIaxbxwrVXbmjeTUesQjUhGu339rqdoHA2_jqw42BsArTuC3ZEZzBQZ13G_rHieyXpD_LeAR8luiaAyWQVn7Z43GdLAxzGZCRSiN2EByZhQb0O6ezVDBO42ahzOglxorc2mLWubHrK5vnjl2PI-YChCEsL3hpscBy7qW5QsXvqI_o4qvU8g1AvTP5yvVEpgF--9zbOCd9N65QekffbWDqfLbFiiDapDOMVXdlvW2IgyVOMfW9eqTOiBWlqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_FxBuxIdhItwqjVWCAMsUWX3ytUhy6Lq0tMiFzbMDV4-FfD7UShmI3KbKeCDOy5Sqxb3eY9D3eOKl23yKWli8zmJPhxkeazaYMcilysnTbgfOE5IF9k_FFm16Q-1z0x4Wedso0anYye12L2t7PILcnkSuJ-iw9w5skzW7UzOM5bCIuWukjgTC0VSRC_vHHfvwWwy0lUODcYJMqzme5_r-JCaWUHyhmGE0K9zxcnN93W-MjrlF_st6z8tNBwSOnbtz4MkvoZgZABHrriPbkE2o74wxBSwh7EFirVfNNbxldb8grtvXb3GsK7H37zFntib-FjfWhJ9hzeyAaUoG8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOAUuVhm5iy730QUZr2r0WNZJ_m1uxssa6Met5tVMMXPc6JzxI1EK-l6PVez4n51n95XZihEaEOHQ0THvk_XsKxPx5Ec5lOgBlO1Y0Vou7cgu-O9DIy8wIsi4DbrUB2943AQuAnqFRjefnrW9tKKrV_FWayZJ03IawwmHWzB8t-ZRmxMmVVEluk1-OqITqoU8B1nnStzUJJGLAr4vRsVVH4WKhAWZpvf2RnnVNQDS2ARCeHhw7mCOdE5rZALIyOf9CkDrvZT3-N2uuFukl99VvqLgkp-0Dq4z1B2FYIYzG-2S_sVzoqSsN27OcRRMzw0eGjyDrIp-09upGfWvms6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUpoi01U5hLar5Uh4vwVnUw5YDcoEiMq6UlG4hEEIrRa-7D19tcLBptWNovqOoDHXBugxWyUfLse9HFgLijqVwNlTwrL6mNj7S9PKfj-JJu-UcKCX6jgqf_awzniUTZxecrBM5oma6B6VkhQOcCnhEOALc4KnLdwTwP89KTrmidGqxyvxlCD8ahQ_porSD-uvXPuPtUZmcelkguoV1-3aoO1PAmPQ-34LZdx6fRC9ePh6-Y1elsOczA6zdZOn-d6vwkRrY7YPbSQdlGqmztVnIz6e5OKLhzT7-O-PVUmHa35GXQ_ps2vbDEMHKqlUn9_0U4RqOk5EocrZS5J7hpdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh3wyRumu0Jm1nWILwUI6w73jlcHSowlh8dEE8XskZIhip-vp_uFL7vz9fNre0jFOS3Z-6EfTlzxCAjnxXF0wl7_sdtDTfvopndWY7clCtRYALL2OfKHOUju-3s0JPkqoaYIyR9RyFovMzjaHERkXLeNBE8VVO7962Cw6wzGcISpazsNq2XaloGSwf6kyBWE2hEMgeSwDRfuwS2R9CbyMHcY7cvjBAPir4M1LaQQlNWyUzpv7qIPg6gw-7ZrnP7t2TTdAOVpObftQygA-d0IlwTajDA1fn808lzNiAYw6puK_BF_nTLy8rUrawkbTfRyYIS22J5UdCSyoHL3j8tWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB_4INKtBnQ4wdPDn2rXBTimPs-nz-Ae2Wie11db6KDPlAFfbe6cA3CzJ2p4aCsihB-L7IUmbr8USiG5veMX60HXqHAWxLBB4MbgAID5VCSBLhW0jD2A0hevvcY8Ht3BjxENvdjDlYyftoSqxv_OB8iA3hp084Y3RrwlRPWn4b7yKUBoBZ0d4tkj_B98iH_e2_k-HrsNjeNP0Ezr0B7Vxvc9NRk-zE0oSO7QTSmFLJAuQDLaNt6FEZreUu3iL_NHjuinpxurJpQ_TWrqQkAIzhNUpcq_Fp9joFZq51t1znzu3jajK6DgHuzY8d-J4MLwHq9E3fryH6gL-dHdeo70iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6OxtCJYrmUpDDQl6F30Rizm-SNZCb_RSRysmxOrbEl5b-qaQtLhnLPV3jlZFoaQWaMe6LPvAZTReYFMcPsoUhoBYEYRmpjiic_cpaCOhFdLQI22-Skvd8j7n2jdyVFdtvktTRYvY4QZpIGTx-hrp9BmqmG95Q-BP1C8BBTYdRWsax1nhbQsI7gPjwEXm58h2OQ19PTIhcmvo-wA3bptnW92z3bTOeEinet7r-36_W2y8uDmUWqd7z1zg2mA_PyR_GRDSkTSJ3eDeC6YxIV9QW6NSz9MiFEXJdpqenlZMnT7pUdvTPwxhQy1NTadPpcev7ACLomv-_iw8kHV5Q1G1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq68zaazyFBwUvw9xq-2iSMUM5MTxPr5HXRXgB7pMYtXdmH7VQr3u1lq2W7bclPeIjI9H1Nt_Qvqpl5fntFotPVfWbhS3skQJSw3B-NwrtM-uQj7cHjm9XZftgH2u5VZirc2iQZRtuiyUre_HR5l64n9z1xnLM4IHKcw5om_v0GYFyNHXK4M-kNTnsu2mexrIe7Sk0ISLHz7Qgi4LRm31PuMsR9mcHyDsLLg0dpYnwvr7H8fm549AqYzy9jhH4e1ZZxRQJoHB5JrAQrMWcjHnY8gY-mTmxMDx4zUR2z1I4P-oG-IQjVuYi-ncczykNoYcS3booLCtKVIplbVVtIXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btVXkeBNzoQzE7ti4ZG4PFCG785C7BCPfq1QES507uXxT8ewd3WNV57MVx9LlD2fdMTY-GBs4a1RPXm9HLa2PtyjST5oZJ89Raea4lwduqdVP1BIPdewIRoURp_fjLZll4zEegDGN4b_yfKE3n6pCyhwmjzE31tgOpcuxXlvviZzZydhhSmfA2qcrmt9l-20RnF2vNx4D3nWkfaNWEH4lWhJb7m-JLjnwqfJN8VhndLus25CTgUIkx7u43b7Xw8jYvupQpakBzgytupBlaI2gZ0sniIm_BJsj-NPwshpR-OwT2cFPhzBAnRVKlC4vjmgY2LBqaxz59Qs5GUrTN-vYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hb-WoA4MeOls9PoIvHLyGXbgYyKa6_du6eB4YKs5WO3ILoD5-PzIvgPhzJp9R2_9Dont6bFg_1s0sWusQN0Kh_rVbSaXoRxFbvWiCkgVYrW32bkqEoOT-Xrb5tY4Ami-O0YB448R3W0oyTliD6NxNFXlcAewO0yFiPP2uVt17uzzrQLO_ouUQ6PkHTX7r_I-M8Hrjf0YYCcZb_L64Fk308KjqQzy5fFCu-uAREC2Mx9cSpWgZemGnv2JxoK8Kdo67YT7K07l-VGEhkr2FJ2ETxRXxYYGErC8I2yFkF_zJdC-7_PAj3RHZ7jmWdH5fqrOLnaG5rzQ1FM1ITBGVO2oTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVNKZU45fIyAYBUnoAd-Ks3kq91IZkd9DO4sUZ89o8xJnR1JpIr7Jp8QKp_k99zOizZTEEwRCMNlp5ieDup3eojDw2-fgO1Dx2MGFasX2g8dO61clywy77ZI9my80UDFFpDUoNXTy_BQ69eX-Tu7YgpFMTFj6GRkXOTfoEvrB-N9Ai_KmmKqf_4vwotBmtQD2vWIMIiUWIaKAnEv_szN2Sgkz9Lh-u3ttWspadvCtBsNf2pTvTS7lb-pQP3_fh_q340Cdx6suRfVdpRWPoENeVtDzQreG19o5apcVZwaB-IFbwyP-7VQagBLfOufOKAacHzqIVSePRMRZYahAgRw_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T66qIyAnuy2VW7Q4UwmWQfCNcH-0XPbUM9kDB1PlcPm9qoMWjqPr2W7DXgWDhMTmNXxIsMeStu5pL0GPD1leMHepZSjspzgUKJyAlluq0KjELhAW-aLuDpIBZqGRjMszYRJXthbbULiSXrntmRioQOmnq-sLryz9TyK811Uh7RRk4XBwQN9Sn4zKRqj_EGfxAqyatSIhg0AupVDFjfOQiSJZ49plPAUlLGE7I6M6mWlJm3m1KmaujKRUE5w-Si1Y2PoaSaxqqA29D4aUUHZES-R8c23VcS6RSd58Dw16khowSVKixRk4nUVz3hgiZAUqGhns2Pjt5il0QjvbI-qpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvA4Dsogkin1uTFvqibzGUXfa8CY7jPNm1B_6KNofftPGI4HWJ8-X06-VRzxfSGHEfcgrWoujw5VPtfOR2Zyy7M_SrZxQpzxjTS-QrhDV8aXUMKjFNYp17ifBwc3bOONSFa6MBjpDoYUb1yZJRfzd5BZrU08SnevpJ_IVFudwI0DzVF0jO0sih8ZM-Qdr3tIkzUBYWXmKfFFDeDW6q7Zh8OmV2my9JvlED-88LOsbKVrdbpGywBioCFbN63HpGFDWWbZ-XHcbICAdmur8MbVsxeBQYfODwy_tV_N4lbRhhM1TvJPpPaMfZ1UUniDL2_bHa4n6jbbR7kjPj36UQJ-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVe-S1m30O4RvfowhJVfBnKDwmD0thl8ondJIKwJMdP-jnfsomt-UtvqOnJ2DtYMGl6asm2wbwjptBEucln5JUScWRQL3bHlpWBR7IM4AMoLxlHW0_CeyAeGYR4fm6N--6Ty3PjfIJAqCmZI6JENFRrZjZENUQbh7q645vOnCP-tKuV6fXlAYhS2OJYvwygDmQ_xae1WUjnPcH6arUTSIOtKNWhhGPbx_Lz2y1do01xcwSERdko3dF0ifsFb3V6nMI_3rYjoml-VLN9Jupn63OK-9aHvJIg3NmOFRg4OOdawPwhc6hQX0qcgt__2Kq7_ai0nWnyoMGqnXae8lRgcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNhx-xOTVv-Sbw8cOoIlopW66f2JDCZGAgkKy7CLbCxfxCYnS34pDtchNUJAr9jarD32l60og6Ywc3PY_TJDx6sm0G-oB0GAF18UG0U6HqV9QzStTTlC5NP57g7ySXb91SC6EwUOjKwnNmrHcgUa9eIN5fSfVqlM7MG72ZzM7KxkFpbK89gx-4X8xP3vZrm5bIAE1yf-cB-8G-i6tjhs-TYSF1F7G7F2VE2MYmLpgTPOsCG20FkEMtycraVUQohfPeBfldC2TBI5rpyur52MerWKvvAUPmP6ygU30MeGwmYXxoDYQ_R0iw3ZdWlJGzyEacCFHmyZXUxzL4zj9AXrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edtf4-zZmBW-4pixpXKm5L0I73MRxd4i6goceKvqwrzrho36tJlsFXuGaY6r3bmbwWJDHiHpzJRTUWgJIsdZN6xRXhbvCvfjymviyFdwCTMtF7_lQ9KGpFWH61nWr4McfJDRwJWwn4Tlkqtmk1oDCvZmSiXUOI1PH5J10fWiQhth1yG5L5S_JT9GoiwngkQNafm87E42zU-d_OQOcRb4dsc8LbKsH5NX5Qy97Z6IT_7Yrb4JLPQovy6Ot0PiNShbtCJBoPLA8kyQh7XAB_haOEyAqfgj-JJsqGMphXCotEGMhgi6GBcsBpnMHU8YcWzYuIcmyBFkQJYFewpojZOBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmPgATDd7Oa_Tj1vhblJjo5_KPduKwskThIqHuyIoHCKLAwgRZhgJVtl2MwCvjSXAC7vYHnJGw2312FbuTF1dd-ZkkACYMvqoUYBx5wJijESBZtVC5Qkzd3Hyv1br5qZ4dEPfE64L7pKFSSct5a6dHtzgg2nkdGShv0QvCTLW51xWIyi2ryoMJpCVoKS7URQ29tb0zjrHRtfBpCcf3ml8iiVbduhGNUddyk1iZnnIb_sXo8UC0nx3eXsdP6UsSOs17dXbO5GUy5yPF6tkseTivncOnfS8F5Lif9ugUac2DVk0lNnbHkGHll6KCYcqQZpS8LRLoT5zkp68oJm7HizzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxxXZueBy4Nat21HLeIyFOF7FHhDQnAjbUV7zl_EABcjfKPOfvibdO2usaDv_j79kg8HIgyYUR0CBfnSwwzb7EPvXULJhK8Ay5ZgSZxYNqOnglCIa4BDmLfCY4_7QMWtss5aLmeAvmo65zkwnr9pTkldHBPYhpTLAxOAAB3vQtF2uNWw6HRtUaHyRr2gxwNR63N785UqnC00447TOUhuUdy-E_b7getA4nKonbxwYy_hF22DjadwZS8UCV1Kxa5xYzwjEHTxa9vyo1LemBcuSNvqhR0TtmZCd0zxd1TFl6c7CHCIHxKVly-g0H8OFU-Dc6Pco0oGBh5NvX_2KBWwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJQSpcCBpsm7U_RXg4UudGEB5AhYh4OA0ACYRk8CDaRU4NKa9mFPitFBdSXr6OAnuhCdqwxIDjT8xxPE0KTKQGf4a-u0Qq7On3xX7w8Eu6vHCVPGTDFcY6r8jMaAK9-wjUQz0WDSad6UIGchfCJhLHM6rRgJNUk5yoN7KXIp69Mw8sB2wBxmUC0xzD4bXvPCATbi83n_dKt3Lohk4KbwXsxDSedj5BjrAu3tiFEHp3TG-ojliMjFCl4NCvb7Z8pz9uu8TPyoVaFc_3Dh9gPqgbAmbrUhHo38X-y35Yg4GrIeApNW1itbpFxnBo6PswmefYuZIPLS1LQ8GQYY2_C9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be2PD_EVUSIaKZE60I7vlXyV6TwXJIrrtXLRnlslomvZ-d8kb4y8rPBlllCTf0MM4ySm7z1itlgVgLto2wJw8oW5q-s7M3jhafL0YVuvV0yc6_Y-tr_gnM28Wpliz068xxsQt_2-VqeQiQymhLtpK3p5O7pbEKpd3cid02e7LHVBu4_2-gRXgxS4c71aJZiy3zAlZosZaCVN_kH1zxX6nIzFIGh7Hn-LQ3g94SlQ4pYCo7F_kp_z-pQw3F8RpsVM5BJPOKOGzFAUOkdRlawJxAtTOMhEH8SF13jc_b8WvxMgOBznjFvqCnSxl3DZ7FP9q1ghmhK4LW6F1KPfAQEd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=jLtxnb5183CE98uK5FywBB99cPNS7umMHOzXIWPSqKR_fj9kzHIyeskLtOnm1qhXbEyNPzVhwhGP0CAvltAh2TT5sRrNfDQSWzjtrvEQqc5xMp8UYba66oOWVdzs2-3MTaHyviyysLHQdph1egDjv6YDyX9R4bm3arVrVIxwi-lEXguNMtyLmHaIr3O7bxmHEJLWWFNO0ZzRr4fvqr1gMqrJ1gTpx5LA_zTMfoH5jQrlGTkX3gTYKduIBbvRR-2alqm6pgWl9hoLyOKwFNDN5zucxsZ0KDIKcERqxwIPfw-f3ahYyajQzRxiLOm7QnYhAAGX_Eayid4eoj-7hGBJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=jLtxnb5183CE98uK5FywBB99cPNS7umMHOzXIWPSqKR_fj9kzHIyeskLtOnm1qhXbEyNPzVhwhGP0CAvltAh2TT5sRrNfDQSWzjtrvEQqc5xMp8UYba66oOWVdzs2-3MTaHyviyysLHQdph1egDjv6YDyX9R4bm3arVrVIxwi-lEXguNMtyLmHaIr3O7bxmHEJLWWFNO0ZzRr4fvqr1gMqrJ1gTpx5LA_zTMfoH5jQrlGTkX3gTYKduIBbvRR-2alqm6pgWl9hoLyOKwFNDN5zucxsZ0KDIKcERqxwIPfw-f3ahYyajQzRxiLOm7QnYhAAGX_Eayid4eoj-7hGBJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=jHBhlEfwyRl0QwSzjnLJfdBUsHyIFpRz-UB8d7xXocrsb1XSut_hQqQT00oHBf5fjlWFMirQPgOn4y4DaNiV-I_2Wro_fyYpLqqUrjKL6SVohkpVTvgQky1DKY94Y5KPd7sASrSptge-6xN_oy4vrbfoyP08EO-QdUBOxsstKidMeZv1cVn9UV8UvwEgpWTpol05nBsOff8IcqE5OwQ7Zlcvakudjg2xjEJaLYImqfLfrSTjFTQ9xVH9OkH-_1syCef5iDlVJTSpByrLSgOPpLOj-GTkx7LzuJDtbp5MR-anDVkrXTnEUeCrR-BvkSXlWpH2qqEWpEBzuSJXzFSpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=jHBhlEfwyRl0QwSzjnLJfdBUsHyIFpRz-UB8d7xXocrsb1XSut_hQqQT00oHBf5fjlWFMirQPgOn4y4DaNiV-I_2Wro_fyYpLqqUrjKL6SVohkpVTvgQky1DKY94Y5KPd7sASrSptge-6xN_oy4vrbfoyP08EO-QdUBOxsstKidMeZv1cVn9UV8UvwEgpWTpol05nBsOff8IcqE5OwQ7Zlcvakudjg2xjEJaLYImqfLfrSTjFTQ9xVH9OkH-_1syCef5iDlVJTSpByrLSgOPpLOj-GTkx7LzuJDtbp5MR-anDVkrXTnEUeCrR-BvkSXlWpH2qqEWpEBzuSJXzFSpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrQTRwG6Jb1c3BbOk-TqhYgyJTaa3GXRlwgZ-DbQnk-pwJxjE4K2nmTUxNAiELnQUe8pH4GnRsrIzLbu3pv9loYR6vXOSEAsfkTsAjj0DEjNW8U_dngf0NNfG_9EETQHGxnG9ceQ6hg0hRz52cECk0SbUHALyyFeLytIqU9-b2v8ZNyRF6k6apscHDCHbpH8g6_uuqIKdwmO7uc-r9rZbAcrzszejKDQnheZhMw3PKsPSB767UCK-Mi5ASHiDoFM1yGP4uE9Bj37Ztoj2IXRCYRz1Nu_9QWa-rGEhg1OZtBN9TRZewJn4nCvBegOxmj3cPUTUtrEDI17YeAypdCI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvruVNKatWVUuaBY4gq-wwHO8gzUyvgSnScjncg12giXaVbv3oy72nPqI9nmGRMWzeW5TJmyouPs6L87K1xwEuG8EkZ2kwKN0NbTiftBE_mj_zjR4iVQlsA7rPQmi6YTq1xVYQjQmDoWQQQpsr5zitRPQCejCw7Lkq1IwKaHA8fz2jNeVGaLPxQvfaJtjUVsjeVgnCKUdCUTWtDFY52VwYGodU8LYbSF65Hy08xK1U39dQjewa-VqonJu0WV01POQ6TtOCkwbg3sP_P1UEsThXiCQ938PoySdLEHAZ2BUvM6kMG1vZO8-QhgUxFyJHwh94fJlgIUGKx9Qcy7vByHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOzr3TfkasEirS3mnMEuc1OyNXALkeZkSrNwIjM_DwNIAF36YFeVqVSYHFZ3Y4sHzq0YrmriLPPLVqV80qOcvx5v7qgnAh1gbw8O48ukpiPDhhd9vAhW77Yy0Q_HumN_3-F9MoJDcEYgiCOiZZ0ePZsuEQHt0u6L3r60epp1vrOuE0a7OGLEVZpErPUTc3L8Ovt2p3MtJRn7xMXUplGts-fm0hcWOUULgXG_cqjsAhjpQyRG9fSbSodb409hDVrWND9-uCvcYfuRxv1zRLCuAMtJ_7Azjo5zBfiItmlHHn01t3cksoRF1JUD_ZW1_mUeamKu_O_Vqdid8pI93O-TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jobmRJAyb4v2Vo8iNo4R5j0lh5kV3vjen6mjBJAYKBQ3sC_Mq76ejEPPBtKAUQeFi76iMq0H44MvXwPnlpBb7jHT9Io31G2nPv7l8GOYt4t7h6-1Z1Rdv7ZJzO9XKI0EKqIIarKg8PAUoqOMyiR5ruPgY0OsmpRTf7DmsgdG68ohkoLrTMtgcwmc1Q4TT8rCO1LY973FRkY4c8tDoLThzV-uV-aR-2bvq0QMdCEXY8mcQkOmZymramcmOe_9IyrKZA5wK7KAdamzy7vRgONNNmAn1H3isxw5XfOWW3YtR2sKxnE6VH1-zE3nv6pPShQvRBRNNaY1SJAL3qiHL59W_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_2dAIrFffmZPBt6gOFg55VZ3HaxBKNKxbZFQB5kHviCEX64Ud1OuSaz16HRk7H97cfa5hNoOujGmKGDJYVTs8kpL4Qounate2CwqBoZUTIPw19GbLgBspaJFuTy-c11NMAx9CP9t_SVkgj2Q3E3RMU3zjbHh48P8JlnNOJ0QaBYNxcEJfIJjZvJ-Bv4hrNk5SumibjbbrLaPKfo9FFCWHNAPXH8C2QHHEYSXfQkI3LZIM0H2j9WM4LgG4Cn7g48jQVciPeBWx0b0ZWuw7-_KWGGjELudXm584KTGQyqHk7a0UG7olJ9PHmOD8rLRUsJuN7-RatRlIHOkRYthfYeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=dt0qPnEF7sQ6DN_zJGorciPTYUAIpsnps7cOIuy2acIpmcRzoIKU-Mt5XiynVd2IRYRshgFMUrrMnlI_iGnqC1VfxdexlKrA4EFWLB0sEw5pvd6P8Cv9n2ZPjg9-iDlqrm-VUkUHoHcyvymPI4NmiliJSUCPEdLUjgLzr0RdeQNsJrPhzNwrQFTu7njKbEB4QzPWwQHeWXIVRgYW-vyi1FYFR_NFGcC_7FL1ec0l1-VfmJQBtSAtPCiX_Air3g94pv0ljPAIoCPuML1rG-9RqA_syOnEItRU4mEUZRQwWgKFDczdYIVXRpCKH7WCYKtgz6OYYfkXXFTr70x2KYSGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=dt0qPnEF7sQ6DN_zJGorciPTYUAIpsnps7cOIuy2acIpmcRzoIKU-Mt5XiynVd2IRYRshgFMUrrMnlI_iGnqC1VfxdexlKrA4EFWLB0sEw5pvd6P8Cv9n2ZPjg9-iDlqrm-VUkUHoHcyvymPI4NmiliJSUCPEdLUjgLzr0RdeQNsJrPhzNwrQFTu7njKbEB4QzPWwQHeWXIVRgYW-vyi1FYFR_NFGcC_7FL1ec0l1-VfmJQBtSAtPCiX_Air3g94pv0ljPAIoCPuML1rG-9RqA_syOnEItRU4mEUZRQwWgKFDczdYIVXRpCKH7WCYKtgz6OYYfkXXFTr70x2KYSGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAd_nQl6ApCklsKXAk55Bt_lFxUSuWmYue8GwMRd8QoDcM9_yBCDyFd-zdXVL4Hef0Mwq219K64M0QGtYuX7Ehq2-FwzE6rsozlxFbiBWW_xDPlTJL4-TJ0by1PjRapQU72Nc8uh6ifsmvQCWUn2A7WnLAgQpgxXxP7RPfpQeRy4soda5Zk6liIO2HEaEWihGIE_qKV1JrMAHXVCtvzXFyGr7R_bUljIgbTG6pLnY8kN0NMVi2VeROBPBnxKPxjmJzfCYUSxHcA5shlf5SqqDC9egz7pOCPwsh6kiuAnOE7ukRrfxRmxPG4pSigpuk9dqqOoX6qdkZZWwlhFPwQY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwwzVFMdx_RPb1vkKEdNgDRy7mTjLt84t8_RUdvQxrh1Aob-uZ-2RRuNGv_I4lk8s2P3anS4LFORaOJ9dVm1oRM1EDQykef32iOhNdZPzvk3TVwQqWQs4ZWalz-R0zrQJL_QqaBNH9JwDP-lJSb0t2cpc6DEXK6hBAjmUMGfbdjj_qXn2co1IJouhbbtEacuXQMQ61ww4IUgdCyA_2LF6fshrm6dhFSN2-nizm2xLiyOHiJLIZPcMr12CVhkDPRlXDJgGUMG6AtUdT0ia7ubsEqXW1pOUWgfjKmSGVoOn2H_PKTQLlM4v0AIuirN8CqGkGOx8L85m-VkGjLw8Nn6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbLEHxcABnyZ1f6vlUvz6cJpTidXvA6aPlWCD90DfWjDYDPhsZ7KqzdpVh1NH8k7t9p2zWn5TwE-0lXqpu-N1bp0Sniaho1nyzWy_P3MshEjMvWIzoMn2CHhKlCBDWIbBl_qGGk_OkdYbrjAP8M8ubyNUcMuNe1ICLFwURjatNOkfyUicgFVKy21dSh3DXXz_TPblLZvQAst7Tr8ULCrm_4PUCANE-S4tUMjqD3wXpD0QYzdI853hUjfdedHB_ivdFm7KF5sMVCdocv-GhB2OS4LJJYoti3KqtqJMnsz1d1H37KvWS0bAQU85uuCgayKCTn0RcpY_5VXLwLgvTrgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQS9I6wKe2ZWd761pmQ1MMQhRivZZkhg5YoFCH_1peqBg1PGFhhMR379NJz-R9jWlBD3HmSnVr3vk3HazrFyC2NXQBG5CBTDsJdXbIEn_KxuVcnLr2W5ZviFsO-DL3XDCcIiHIavMqWFHK3hqDuqpYOG-i0F8gc5UxTvnCNTnuUxmv5IH83VoGCDwZuTk6dHuIxUACZjmZra7iaJK81dzl6Y2CfS5wRoJ9Amiu2FjM842B6D_4VYmHdX_JwxWJu_RZudvDfVAglIUbRn9xkGADwm4KQ2Qd686tAIaDAcJfJglx-Jhswu87OwMU5E8aMobaksW1kYW9KLAwdN-K_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27460" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
