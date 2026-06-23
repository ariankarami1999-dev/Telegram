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
<img src="https://cdn1.telesco.pe/file/Gv6N6YehV8uG5cWun5O7dhCg9B1Rm5E6etFAfeu5Gi7FsQntx2yqJ_GTCWVN6piY0rBzZEF4NHh1cMWMYjAhn6FSryWdL0DvXgFmMackgXdLuy_GjpLfcgFg-yAWqdBe5QBVo6t3fx5LP4B9QFQMksxZ6A3UW4lsWBW4r56FsrwLSwZkIu1JwAZVTSxcqz92qZf7DItsQWL-VVkIUNNEZ1TzQU--DUJ5fxW1sd0QvxSbE0_f1Td6kMCbSiejF5MO8KkYzMXPWuZSX3vYb2_os3ZgXdVmaCa3PNE2eR2BiESPwhv8O5L72dmAFLzD9g-wNcCvUus8tBA0KX2xZzKmAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJF9l4f1HtBy4LIuL3AmABjf43ZcVNGOCuQMTxvqAZL8lFB_4OD1ngAA9RU7gCqirlAK9CFs3NnKIiyaTLHTpB_RIr8CdtJqvndpn9wyehM-PStsdXUaq7pYKP0jXX_3piX8lviGZv3oWl6wuf2j8lLTN6sb2TTSLSMRgsBXSKM7Tu2fRyW4g6_QuBAzsq5-tXdmu1Xj5wJ90ajmbixcBKyXbgf-eUmcawbweLBeJOOZepiGiB4qeitClIVO_om19fCJoM6Eq7rCAUFgx75i4dKejOzPu50eLao1q16ViWtx9VXPIJKyYSYJrcJvO6CwQpwvV7YQhXgomMzAbsG7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TK7aQr6e_Ujvvw6OaBL_tQ0fI1p9LJYBNJMFJVkmB-O8ygKUIVF2RJLUPVsu83rf9iW9FQI1CMC8T7jWjOBEOlbUYI2FoSPPTbdnzXcXhCgOeAydQaaiIFyGp4p4SOFQ4qFr-3Yt_IpMRKa1dRbGd5mQXts12BRd3NpvbWYcK8uWOqbZav6MDjXYS9K4OnR-0o_thAOrEODZVSS_L1aSePIbHRaa1oYeupC21L0eP-3tYR_JOoGL_HOvoqiQq97LJfbA8wH5zAUBBJOgAId86TT0dUGac8LIKXAUK2ZeQ8avVIZEz1JjfWennCTr_9w9mWavAAA73JkeoWeFzl3GTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y7IrGiQyNsOpxPi54s1C_uaG5ZfLiQIS0o7lx9F4cQy6RuX_xabwdGZr4ZeS8FlyYFo4EpBdKkuREZ9e-dywdKsPCyRqhJjH6KEQ09J_DZYhJLUSwz0is7bcA2E1xPrzM4UP6HcPlUk0o0SsQnq5mDbRTB8vDEn3zSJPViPahINTXsDnPxRmH5_SR7VKYttONhsQr04_aDAi0RDeA0AEkMkWg_2K78TuyICI55PVSPwKaX6OKFsCED7u8pWursQ2bxKD55FSxyOROqu_E3DKy48UDyAOO0W94leBJ5ql5Y1xtPTZ-trs0yiX2KmivSObtc4fyG32pi6_mdBD6OuvaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F78jlGzvlosNrj2PIL8WxfWmpQNbNDh5qqM20-q0mX8sJcuwYd5v0QvtGNdYeW7TZgmwplWB7eEppAUsmmVbrCBt5RKQlZ9KMh0ZwbO7SJS9LvHMugBZVXKc0CBtJ_gmGrEBw97rmhRg0vQuYuxa7SVOhDPYSCQy9xjsvqoV90SWrVtXQeJtgkJb76WyYjzpTGBAf1xEFcOrC1OqjidyJd_Caifnw612578eR5wBKkZO8sfxxVVnPk6Kl9fOgTJ7uyENR9XetkDeGak_Rr4tzuuchzQ3ue71ZhrdMEkqaMxYtuMJEtZPtOYrp1QSpmrqPkG9vOxX6UmmvPX27KAz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R98Rv4fsoZaXk_KHvZAQjg_TFEcOVc3YscRsfyyit5uOCV_zZTdPgjvDVX35QYzSmCl4_bTZH2gI8QDc9uyPv2MEB030zB9x3Hu7cbmAvNgbgqpJAk5mQGTkrm_N1zbpN0lh_AWU_bOTaDkJVjRDzM5W1q1IohT76yOyLjhj3Yu89z55gSppo84AW_7bPGyIV_so_MA1xm9W7vbIlPVBms4RN7HRQpSeY3zwxZoIb6NVCjo1sWdGWGjlGNMyA_KVPPNww683IXGlPuUkC-K-TQbveAHq7zAwILufA_RmxB-66RsO1yhy_wf4rdw1OBQN7rOee8MjszTYY6bdA8ociw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gOE2PhxSum_WsV58V12iki8WrNf2qOBHxlVMmewEvBu6oK1pdfguc5B1j8XRDZ7-cyktlbv8_x0Sn81vbJoHwAWBemFwFjw2DwS-Kf0C-PJQP6R4HDu_h9DNDvEj5OlZzLdhXzv3wUdn6QIKpuqF__H9sTlI83s8y2OgklIgKFDZHFe_WATURbNnztkovEovRE5s4HCZu4x6DZSqOkgGs_mLVi47iEI2E4qm7d5rGMlMYyaBp8NOt-B2yc2mJ61Wwnv0UQNDXDvdvJJc1JYMRzZkHV5tTKnqoqIruev8hcWX1gLQAfygSIUCetK8qQv8KVUFjSPQWibf79K8-VwQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DyV71ilb2pMQr_RJJ4scBZyqhpEDD9qlyYr2YTKfOpV8OlCXAuwCwn3qxZ2l41LqofSNtzffYk34nUmxd9qA_gPNlfCTvHlB7RKC-Fa8bCaFy3hOCJVZBjxnjxuUTTQMMPNmsW2qSF2pcHwf43MMRMfhQ99FGYcusF2Pb-qdywaeL5x_sCbAoPcZcK3SZCmxgLsAYdqWVcYIQ3fnQXdoLyvBYxj6fkz3vEIWWID2rZGAxWcLFZI3IAT2rVfaq8nErJ4dfH9YPUAh_FiGRA3R6xV_WRU3UYs0jEvI51MJ-31u1rlYVPr53BTPw0adKzNUYMcGhGQ6CxkatjistDU4xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=nPpn9nTK6lKW9Z5-2qcVVrziXVE_rjn3JS8zGXKMfokuk6r2J8WpuoKO9KrgcKrWt6s6JZytEV9YmAUGmDKp8Cx8mpNJ-MEjnFdrKCV9BfyZzCHnu7YVfm6ZdJgeK2s0nf12jHHU2W9fCDyT3zeJ1vWwnkCOj7lrAt3_wsXS7TwT4VHNWr_eBZNyft7hxMGTq3ftZ3fHDxfP2Kbur_h5yDOL9GdRB3xtFO5EIxN38SLfrF3XEQKJlHiucGPasJ4Lh2cu7JUE7tRn7e-FUq00LP_GTXJUXl6ONEqmNv94XHutyx6qmQ5C3ElUlrcIhLDJaenvFY23_KdCGL8tgPFCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=nPpn9nTK6lKW9Z5-2qcVVrziXVE_rjn3JS8zGXKMfokuk6r2J8WpuoKO9KrgcKrWt6s6JZytEV9YmAUGmDKp8Cx8mpNJ-MEjnFdrKCV9BfyZzCHnu7YVfm6ZdJgeK2s0nf12jHHU2W9fCDyT3zeJ1vWwnkCOj7lrAt3_wsXS7TwT4VHNWr_eBZNyft7hxMGTq3ftZ3fHDxfP2Kbur_h5yDOL9GdRB3xtFO5EIxN38SLfrF3XEQKJlHiucGPasJ4Lh2cu7JUE7tRn7e-FUq00LP_GTXJUXl6ONEqmNv94XHutyx6qmQ5C3ElUlrcIhLDJaenvFY23_KdCGL8tgPFCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcGD6SXN_zJ1_YziuFISxaJg7ZQQnLL8mh388Y6viGcNzP_SS9Xmev6vphJMnWwXY3jJVnv0b7MCT5LD8g61yUto-xH9R6yPxlPCWSnUPTBuwdgMuRrG-esLFg6ENtcfVTbuISgSXm8LAlI7J1VpupN1CVxIYxiFFuG9POniUuYcsJ2KNnxPHstQqodbTZDSFQGCqRKKaH2Prk6WTwePVshBsKKShRxd61t4jq2DpuifJqLFXiAhxcq2jV1x7cdOQUt0AcNOSOhVP7zeCqZYoehAip1-Onlc-GEzudLFZ1OgrVOlMt5eS-3-ZstYUmDmp9SKpVGnDcZMxHNzIetUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1NwhEgucqtcR9NCTY6tNzhL4TqTWDpid1biLEspMymaX8BacCaWXkUq_xFEerNYS-Ota6F2lIs_wKaQ8gi978Vu-A3qd09phjOnKI-q98nn8MdOn8a154vx9qilAGErpVcKem4E_iEMPt0IUE3yZsKb5d1gGgDnT8Fy5KiQBQp5tXNmzw_f90w_L81fTJn9tXyESQeljc1-zXR6FRhDfpfm8UXDpuEkmYwLmMXMZsw2jBd5IO22_vCHKwdcFszYOss5IRaRlBOXRasEddn6pBBHU5d1SReIW8yklrbQQBk87WsizebZraVjVVsZCp8Z2GZ8ehg0UiPTwoR63xWxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AInyswH9JQq2iG06xsKgnFOuUzICpOi53suIEY7SNMvH7oX08lRXMpdTiGy1Cvm3hDrPQOvA03dSbLBVgsMYeOaOjMR8RTzjZTvKoNqZD8W1cZUsyEvh7zBFKr4yhLv8bLUnbkTITR2YYtJ4o7H25F_-wzL1dDWyhH5Z_3ydyw3FoclsPqX85tkQ6DATSdmx5xzBNB2ir43u6RRVkMwceh2oqp87MQNANjhxZaXwPMYOu2atHYcOm1HAmLwXM_srARyQX0u2Prc-afWfvqb6oKB7tCZjc3kYjdKH7yJDCkr04FkCPf9wkXKZTKBx1_7gthK6JPWErzIubACGT7r1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JyNK7OgLbvSZT60HJeBRjzM0oWGaf2XQEXMQhRXR7jVgA981ARORTKcbGJwiRD-jt92hzGGp-EeJhB2OqFbrWnbolppCIFNxd-jsztssu0NsJ0nGoS2Vd2r7hClopMEYYnfXxjOC8Y_JWeEh_dPIPyueqsuLW6k5BORRHJBvS7daJNjxkMk9FpNsuRjWrAfbqo54D1HUkKZWQLaTE7ILRZVT2TGv4e1NItpKg28f7fCrlkGNpeMC_QjUhrasdn93omQVuN398L_1Vu2cZhvsqb1s50NIQGQpnpD4S2gy4J7SBIOgByY7szSp8GwxIldoTobTNvNAkgBTizAdAArtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F_xfkFp2TZVuria06JSvRphKx_vILX7xeVV2iaGeQzkiEUuaI2OoEdT1oktTU3Sd8AhKdgFo-28ai4zEA1L61HaQQMsOh2xEVDc959pRxjuvB2GAACuPEhYm1SigLPj14j2F7-4fzmTWnjrsgr7QJZbXYjOe-kurz1sOqr5ny0Vc8tqMjsAZe6PMXGwQEqT3-Ca9mgMlbd7XaPcFH707TeyxB___xh-fF7GAWST8Rl0BFvnZOfq5Ja3JylLM3jZbKzKesOiqDiecC2lh9xFiU4JFL2Bp9p31LVCR6oRMEvvKXQDdBPajUzkl3vpIK1qzg3oRs04J0OiDY3g6ubMOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ndXVwgvjbNuVBfi-hGemyBW33PTxfGVEZXlijDgvD4OmQE1dGmcp9u8ElHpZq_5plHHlI3P3kTnrF87f-vQdGnfv8mKnscbqJuvcoWIsvfQ52nnRKcsZAPkWyqIfyt6JT4uXArQb7Clrk73NQ-iQQxcWq5eKb9wsgamPwnyDq7McilLQRrMr2KsxmLoobc7L-5rHWMa99bsDYNcT12RlMi6kUTsWSe7QtQD4noJi48y280raFRkRZvG3dBzMHjTx5w-2TO8aDXch3XS6tQxOdL9l3o5icdxebI8mpbiDs45UfveRpgLEC0H4gtnoGD6F5M6qfIikpaZXtia-FSKZ0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpPM4_tcs2i5n98QHzqAdXsm3kkFzoOBVRYySRO0EmvOXKqdDIYjTNjGQjLrs-27AnaxFKtOIQ2v8b7YAA7kmJy1CnigI_ygmyP9JfGfXgxFRIrgZNA5EeZqjUnb2FHRChe2M_N5FiZDOdn1jDOuP63xbVG-8941W1BoQMJRSQ9FHSGz0A8-raHSbHtV8ZH_baHrJ4-P5m_bzw9cEpbwnDtLZmgAEh7O9-4UQSSkLmTFvuGbBLUmlkQmpYTDXO7HAXNblQMTYjfKi4ARUrGELD8wdhgROfyO5eR3CTrCQVKaBHVYDbdd6603ju8ACjwWDDgB0FWkInPNXzPWG9N6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GFtcB-WIT66t8BTRJPBsoygb7Pr31U8qOfEX8WZ8PiKEoFyuFIEd_5Qv-drHWvd-kKbVXStXEq1Osj4guRpxGcaSh4TwMhF4N1WZjXODkJnENtA_uJeAcoKvDtxEj_r9JZbo22ceYRYpDU2q1ibYFXEtPlFAXe1EbzUtdVd-sPYrpuOhuD7J-A3MZiOsyP8mmfLNTV3oAhOecLCWffVpJsNUlr77F37xaXh4Sv_nwLzvsIiSkP0TqtYzo3yq2PyhglACQZ3vDeO_cpqOEJzOemonp78cb01_Vr-gb7wyQ-ESg_WneFeRj4pU5R7unetudkkpaiq20QBwwW_V654fbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blDEQaYUrljOgYbmOcG9lr-4uGuC8Ha00N3UUzDuhYI5jW00J5X3Y9DfdmetkzXp5vBmf1ACIQBXn21XVrV6bn_5F9NCxjufjJvbjHo41yw4DpeEurcYUsl059DGsb7HiWvC4gLYS2bIY0UQeQsqs4gPFRQDBlHPxA2N60YqUQcZiLcSHG_FPokWUMnwk7pZx0A0J76p4Qnr0u9TH3c7Hiomckze8FLw-cT5FoVzlOj18nJQBUgsmhhFVza-f07ngAJi6HVjuqQjo_8y7jn4xBlgHvUF8eIjosxxNnjJLgDfE7BfLhnUMQknKaaeZBUhkv6Om77DEsCKGxQm3F1O2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DuZyf8F36Lp4L7DXhohknOgMli2kTBqt1K0gfafI7M34QYgGnGUAyAxRaTWpSTaRF-c6lQIJBCphMqqsWcZWiiKlo03UmJ9RU5ImwPDlAJt7JaR04XAfnM0gUaMCea9elfnxQqWOAyUbHAnEZPSaMd2q6Xx0hS8RI6UJH_b6C1L5YzCekgtMZEKgdH7RltXqeAdh5yTVjxyo07WzziLSlujHz1RV68-qPI6iT-ZJnAemnk-qxq5X988D-OSImTvHvmaa15AL6MfS24msXJ_t9nYkDi95jlebhELx07VVkHFpvrvvkaGeaWPvKTVxBkhdh_KwZcUDUJRlzQi7oP_Bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qSmKu048PbGefbd-sc5E_DIJnJChnzeGAuth7XuC_i36mWD1q9VZFKjHSxuJJKgvrg-HS74E4DmtUce1Xkb-UiU64QmPZodZqqU7krqGr1-lI134ZHA6hA-mnRhM3kCnwCTvfLlfDPfNrH5xoLPlR9V2NGUTyp7-9utJ2FElBWUG4BoNQ3RnDrYy05H1WByo99mJAo5IntUZD2-ztkBzdlPj58gmlX4-ZSC1yyb7ulq91xL9GzoHBVDaULXorQ5HLnfPwrXyYL-CINSh3nrzqqgXk-Eyhnz9qAj84mNU9jFBtE6rfQdH-c9kFyQpRjuhzCD8W08g1znVMxcRAp22dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYwFHUEFImo7YsN3EuGVu_52MD3755SXvIDSO6alt0Zrijm6JE_9pgTdcQC9AWr5ZaPXmfqiULCndSCxYXeCADiSgc6Gan6xiFmB_ric_-Xu80IRrQ_g1r89F7-NYd708RphYOvHwmSsQhjQvKBYQJXktA9Miuf1h6zLhI0A9AYjFlnXZO337YRskoy0phAs9rRflI7XCAtz8y1o28Ury8gmfST5Wzc-4qWcUOfMOpEuzSmFrY3wqKSD_0MFyHHcBd5PcWAbtYx8QBhMUeL5MnkjBZnYl7K5FTlFd0lx6R6PpwnSZeldgC2rLxyThq56awxeLweeXnnUnMAiWIc9Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pzTnfTa4vCt2x1ZZGDFOCOXl-BhsaqIJ7jais6sgtSVrljbyOzULAGea7YcSNwZIhWMUz4YxYJkKP7s7IjKAb3W1uDl0OX8fr3xU0ri0QBZSPagyp7L72baLKmjIZfj29OG7hG79E3IFV-3WnE0wSrFXSYhOGqINYIau0BjOjC0vj_EuzfJPEViCZpmVnjNHOxQMF9avJNsjo6Hw9fPHT14hvMTjMlp6ULJr63cjY5g3RkN7vdBEltjzMAFYh5wO_2mN-T1yUrV0lq69AXRhZOdmCtZebdKgV6AyDS6lSyASI4DA34t_VA6Id-xB5O9wN54wH7uTcVCgUINeTWkJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/srABUx-dTeveJf95X3HDLQy6lQuslIFxNLwf0HKCgwB7l2ZTEJ7oWGhsz4eRpB6tmRmnjJ5aikn9rliYvjZM_0xNoEHLKNpmyz4jje-imuOTD-iRyk7MQoDRorMB-OFfigWUzRj4-TIyy55aCuVNlIfstlA-QTJrKOZgN6FL-w8hv04BAYS_HT0IwgPmOov_RZwyrpXdio-7nyTCjxeIDRbIzU8xCBL3IXFMpKxUM21VNd24mF_b43HcJMX3em7O8RMy-JYJDVdXkXiQGuxdlmT_gbqF-sHnNhO_mOo1Q_SNrkP_eR1DMNfEk4uM7rVj4oXg1QAPX_UBkGx799Zuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFNN2uTMWF4FK0Z4wPAmVuL-sWRkEAs_U6WBTjUWnrq6GSHxuG3sMWVjM4-lSGnNPh9PlINzTcbiSt-G9ZdgnOuzbtPgkPpqTwLoPGpdraj6wbKjxTRk_YnqInIR6O3VgcIRaVheZAsPhaTPV3MTApw5YA2q-2wfN_xZ0BMcWs6wuq4sBeNVgwiLmwNGAMiPKBccf3Hfi6ojnMrHYMW_THZKU7Ohu97y59sT3DJuJjt08zptr8UuHx9seg-ZEGJiEnIYHJQo-oNzGAA5YRL-t9nVmuOduJvt1GFk8FV4bYQRqveCAWpNhoFU3iioNtuORFjDQ48qVE2ghVuVSbi7Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqBHn90nMS2rLn63fu4syJ-kAJCoVjkn5IWs6BewsWovynLCGar5ug18B42KE5is6gIRnCNZZKvviL4qr8ntQPurduKArclSwAM1tp-xqPbdK3lEDsK7Eqek3dgdztAB6YldOp8s2g1eqxeboZjYS0Ikvi-QI4v2a1cJDDBL2fDnA-UXgPv6M-kPkdS7CP5tdguEUGXigrBB_S3bnXMmoAbED6IMNtAelmgZjMWp9f2T5KLhgBVzcwLpeWZjAQzLDpVoWPacdutpf71js_c0mTARtQiUa9xyDlnuLp5PTGCGw4DWmC7IdjWA7BW1nDgn4pc_VbdfUAj7ocK5N_jXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ulcsvBNYL5y2OBGqlLovGMmCD0jKuNMcVDo0ZUnstRlbtuAZraoAD9jMlTKLGYtoDFl78TdQKbGHgsy6jMPwPoPIOrZ1rr4-yzrWRakKToNONnkXTH6eIXIgxlF186RBNRvco8Pi1DswgOoNYTtXcVa-PxRnE3Oe3b834AGbZ7xQsbv6vh7-CdmHhXYD6Y_lZrAoyMKHMz5OE2G3gOhcaZMVT8d0Clh6Dxl9Bz3ukRzvKf7IuCuQaaj95y-vG5kvikt0Bn7if_zi1aX-aP4OGYI1lMgqqjdkTHXNXYHTZ7DYvRIaaTXoMih1gdwXopOrb3xxa_TVpidNbwGdkRA2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SW5e8KXnleRmnofEXKwXT8z5PKVmuDhFokPzxPCRRVS7-XcIr2PijAmJaVSByRqLmU-b7tTpcYCzWmrAWGhm1Lw5RT1ctSq798c-lBogwMGaJ0eRlb2EsJk0dpPjZbvFNgANLmIIBSWL3Nn7lYsD6ElbkTT4KHm4MEMlPOSTC8CRKSISOpvo7hSrbrhkZ9bRgPIMswKXX2p1YNc_07dzp4G4BocNmdR051EfCHKd_XZfjuPNBU_cWUJ5aJ5KI_LHUEbNGEMUw3VQEob3E2V2sGZWgbXNlzkklnKaerDcoiDXSFVrxyh6BV0xG3nepcp6hCOP2n6WSMq4V-I1G57LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UvzNUHIjH492evdvJ_VfKm8FWsRDEp3QggAgpWGVtkJGYO1KOcBSq1EH_pz-I6UqYy-b-lDGwQM8vU1Kae-sPAJVomdc-289qjv8Eo4LbUo2ACGpNFMZdtkekTzQ8c58mxbgMmMivVUbRT2mXXocaPTP1AfFKlOgT4SOONeHSMK2Z71EG6eiFKfDUCiBhl2P7GLUleu35gQTnb0Y7BVkwvkTzyMdzlVeWxCYlzP-IGqJW0RAhhkdPbQOn0v9gYn3RfFcs5GOUZd1B10NL8TT5BO-nGe_O8IvaAwzp4W8mQpmXneqZTomEiiXiX5D_9mkr-ytCHeoVhID_yNRATbPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBOWJUbFXnllr_4OTy2SeUvHpNL4DPtV0bWSWeflx0bmVyhii4nVWTThIPD7bUyYUkB4u5yR9ogdl4fVCps0wdYn3WacoAxlEVyZqu_pE56LzxBWMJH8XSmnLI1ixUGQwpKICkQTOmj_mrGYKb0eGgfwGHeZTL0MhXwE5zQ1lWe3j8K_QVkm6fz_ai43HY5vppGDZpS8WsQFqUCESkfeK4tLB0mLUWn2GvQ3rQ8nTP0LEZsRe5odgx9h9wkXX-fYtEZdGFAoGmXJLe-ZeAYpHsQphR8Lx1ErmXY_9pxslPwIeIFxfxJDIIuq0yXdgYT8_ScFSVeiBH0PasqIM2U3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o77gAZX2cCgy2doOiMd28sm4jWhu1bdNtE9FGVb99XjMoTxFDbeSMbbhxJub5w2hCP9AXrbZLffzqaRrIgGauoP3KaLR32fJ0NmKub_4yDPtrySbYibTckdhbNA9fsRpMy1trMLNbucHGecxpH_YeQ7yltgBVUimqCfNexl3ODWQ3BBKT4PduQ9hliJi3FHlwFDwRShDNHGlGJjye6G-V8UuVlz-tHTnl9dJOKNuFyMa7VZxXn2uGflNKCaxCYVKlhjKw3pkEBh-IooErBSnVUvs83TD8FAqajesfRIbbBiYpGCl5UUYq5LON06Kh6VLo7-gXncbXxbjQ3z9wbFmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YsHZWbZC9umk-6ZiCxOOzDmJ2b5e0ZXKZplbXD6qOi_CALdLiE0AgsA57r-99aOVm6gXThO6-8UlW1x0DRj4DNtEjxXJl0H_8w89Wa5UTIOgAaS0DaKUkKT6D8G6gQjTtGyFswHEEo_rzKnj6hij9tHSrHSJd_sbGU-hRcKaYl6CTPUniOMRwjJrSCWUbCr0t5RbV2srQj_vqAM1CeIxgKsXgOq0o2jrr-VejuXWfKMfdTBojKee1SjRdFYBvtYWcz_v6E3pKcNC1cQLt9TIzFvM1rcg6W9-72wui9YeQxY7T0vpemUXZX8Qe3GeWvLPUpHqRlRVYj593n8GHfQg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W5J0C2MvXMJToy0G4CrgVxH5Nqx-JsCj3GPgJxibXvXFssnCvQlYdSNsEGp5o6BYUgmJ2BBVjGpp9nSOa2x2iRDkEesOgLZD4CGP1MyZBR6XZnKOnsWsMsxS7cAtDSZlXsLv0efo1xF-_lAFGOReDLkA3HjvkhfEItQGXKC340lNJ1Rc7msFapnK0CpPS79dwoMkCtpB74vZIPQBNv0PtFQO5CIvtwmP7gWOH0kzLbbn79RojHS0ZeRWoJP3n2bKWtqXikYpA5zcvuyCby4LY_1sTte3-xnIp1tUMX1E8EfRR4blegbaYYcvl8hf4KmzM98OsB2zULvIi8YH3Crdiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tgyh2fCXPynQM0dPZo5Fyw2-JJHk3sYr7YUxhSBtz5YYig3OLPSoxAHMCfOotwGSyJnhII919cu_dmLlBGEKmsvHu86aZP8mWDU9Jh4YsAAqthK9Y2yM3kaeum1K0oJMzYwFv5ccRF0VTeH2CTdwFKwVjzf60WmwZ-3M5yFsrgbinormUmjbuZOU80TEdhtpl0CG7Id4tkf1N0ZRCzzihD7k4SfyTr-V1yhW7xI_l6PLWd714krhABHky4AVQzebUaZEPn4EW0k_67uwMIpCmizlQZgY07ZR85PufP64u1ekUE2a1J9E2t2OBgl46CTrPfNs9xWrJCBSw3NI5UUojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bSVhf5OOqAIZ3ZhrQ_95Gr5TvLGdIUu6CJD8zgNFZiO3D50ZzJeOJ5Xd294mabJB-8au6vFPNI2wkqQjarUJ09G-Q6-P8SZq0-c_gB047nCRNO5AyAELTLyiPogOERDyy13CKN3y8Oze9J89ralVV6tU9GK0mzR0L0AC6bOJLBL0gHg436EHo80SnD1pInLiGdOifA8FQ8kxmztST0tXIlOW2UFH8nZwcTdN_SlbBV2PZQ8gbYSFPReszBaNOrFVt0PQkEk3n3ck4774wQkct1JtVUXIRsVS_68orkYIAQHyON3FH392GUrdtat4Tg4H1GYBrOyoV9btcMwsBoRXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ky2tJs7szwnpeFS2B4xpXuvBsj4Y9n8MGSJYRM7f7439wq4DIPdMUzIfItYttWPTSkZOucqLCYPx8FooFssH36a1qHVBPgKtNavB3goU-_6fxGqpNSpr3dBJcgzhnFMYn1USclj_rSYQxfS5RVyORA_styj6CWQWh0OzyXo8ca1t3AdFYseKJIGRbFKpQPzqhIKulPxwf0qKblc6B2m9xWVHEfHRlH3u2O2wUnXHKghK-IiRvxQSieAqWlT6DU2E3qZYe8EAoape8xRCKxldXC3wxAz-LngAAD8RZb95960A5yLKVIN6LpuSFsDCavzU5EvB0d4yMPBxVyEOM5vHJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th9N3UuOUONwd2RD2bgzvFw0L9NZDZVL97hStW_eSIWbdfc0kg2InWpr8q9jOKU_mNTV3QtmUyLpxzlOjpfXlr_ULdZtSmlgtlvLuFArSIzQIi8kgbSYTHZwhWMvG2fqLmdy5PWdq3_ELYXP9zngo1q5rtIrmrWWRdnh4qy8Ikyt9vcdfEhO-xVhBKYLbQ1d4zLBUgKgNO9QAVp9_xsT4R7jPuW0HaEz29iRcXqCeRZb58S6Yw5ghvQQAItI1Dx5nOqpD_dfLFCw1LWuOs6HXlGbyDnkAa26Ptj1oyGstYuDGEwLEBbHD5wF12js5eelLcajCp8nQkGfI-J3goNyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhS1V8nti-LD17zFmGU-2NKvCm6otZoVMOPME3CX9nw4Ufyq5AOt0ZW5d5lxoKYIFXoxPsKomBz2A11awKfbAyYDRpTMfjRmvNtCnD1caP6EoBTOzOBOwBa_YzpWIqLaaIwRbXBw370WVGIHdAa1aCNhFsMGhgP-35vM4VqkwQmslC3pmW453GUjVpITGNWX54rzWNgOYE26bHB3DRH5Csd7CL8vDLANf68PR5g2w4chVgwq7eMegnihLSUPiJ7evHQRdRDlu5lucDL9sWUIrKWza_21OIOibmz2F5u6ZX9RkcGVRcdS22D8eV5fvm9jOGw1SKPB6aqKfSzCr3hE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iVo7nDjJje9GXBVGAHxEjKPxG_ZjmwjK1IpcuE7c24x1WppbrkUNwYz63sZ3YbNTb2AAQy9d4kNT-Zoy-2zc-xQPDHxd1w3eAbJPS7ltU22SQj1LKO-MAUkVPHMWbQ82nS703xm08P-nGCoUfk1hXqv0pRBMkjJ0piphtNaq_iLOEVK_ng63hT4kjB5xeO6lArqao5SPHIDt_lVH3dlE-G-gSK41tmcVDqdW0Vtig5R8weYGZ_eiZEdIgRHlOl9ME5vKCrIKMGi8vgQinyq9JEZoReylz341U0oeWMVX8zG9AUnegbqvW1KjoddpxQc6O4nfgeoTSDFXCuarx96-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MmyE7LzYahSVOtEn9Kk0bTjVHqTQP6a9c0zroaR_LCL5BhF2lT3yNMusU2tDxR8kkNanKHHBinCKSt3Q8yOXKrOT6qWcoShBnOaRiyYstgJYXA_Sz6qAoE53DYbQ2LdYwl7PI8iZIDvmimM10Q7xj-5GXSrB8jpAWUv-NmDydw5RLjM8spA79EI2gkIdi2l00esfZhIbVKRtcYJ5wxZIvsBjfB0-WaYrpVVKMytoPWdke1G4CK3wCBN_lPsaVjHEEKCgQlXSwtU3tNNbuRlisO9WpiwK_opJHvNsHBsHMVhOFlTtYdJ8qaAy-9E56uLfCxY1z9Dz7I0PFQU745rGfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/usn2qWtW2nzWw5xUtXbyE6IW90ZlPdmKEsDVO0qYHUibFRd0JN9_IICFygAjMkuc4cSvFUFV9xibWycxdESiG8bBTFE5FTO3-70D6w1fDnwmsJXNGkBhKl2AdEG655SA4eL_tgA9qm54dULaqrJQnWpWk-xCsDlWD0g7xHhuOfTKIB9Gm2e1t3k4vJvOEpsP9V1B5VeUYhW9RP1MIILCvy3-qyRU9LmMsf4vnb3IIVHLI4LRZI0sRkQ57DVlkxunenYxvSflq7tCVDbgiyNOYiPdqsqft_IcGxoPaWMAICKUMeHXZRXRMhpyuSpDeA_jWnBP6K3uUHsz53pbymLX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YAS2VPC5xZg9E405fioDcTZa5FB6wLQRhaLKjACEZ3xdQU4fiCZImzOOaU6kmjFHMSYXZVJLo85FIgWpBRIuW8UqdNN41mDFsSP0OuvhPiJ-7JounyQ9yEPFrw75htJie9j0A5dPo50uUJi4gYS3qwWkvEN2Z7ojd2VVLmOYqKC9YLGNJJcxx2UvkjCkArW8hKKVnecn_jl4bFeRkz4HGUYvQUc4i1kzcHuEZXxJGwBiKIQpnbllh_M1tLGlQ0FESorBYutZ39PHnhDMhnJrXPZaYmLxcWqw_2_477COjuFxs-_5FisdazuFYgDuhsqTTSz3yvsHpBJYef4ZBnEHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvOkqsExm2meGl4pRZUkk7IPRWidcMMjrxI1USAVowYKUj_iRlbXP-xdWEU4Y575V1knmKWt9Fd7AknRC4lWng1jGVEtk4DVhXBFRBbxrmTQGvql6EUnREckCaP2xNPl0VfCUG0Tv4OK_FKIx1Z2MaPlaVnRqf9njHEsQ24eubwLTqtX0DrXkohWwANYokMgI4zGwpr9asB0bdGnN8kJgvZQqWZWYQyupFe1E8A7p0GPYYzwSrf5d9eKCpK3HzMrTJDAkZugZlHd4YxG-gkwLbWVfRN-btCazgg0w5ZTdC88iYIeCdYvVTUb1INOVpKqq-IVCssIX5T5CzuWnhnx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_iKKPq7bJ_NAlf0MthOiuQH2XpIF-8oEe4HxTr_A4osjpvnBa8AHD3_1J5bHh4F_Iqj9TctYGbs0jMY5hNXLIKZ7Mf0Z1HQPwq5AcYMpm71nwTuKkONErUvS4qUdt8kSfDtIC92RCoN2O4gdtvRStAEIMu8tRlX5jcuzXw5-vMkMSTY3Z8gArd180EmoH2fuCsRQYySLT738ypGMi-QoIJhsWOzgeFFmodu_yIjhrsg58cllinCtf3-xnZlC6f3mv6bk2DYs5m83IblILdzHceBvagQH1WWGrVxfb7KFW2Lb3BTO3Q_XGLG4oZINNfv2virvScPB0wf9vreuMHTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTucvivVC0ezbDMlTEBHvMWuX4IE4tKmf98vSNTEd7Q6LKAe9poFxVEz2fsqKfHPfqrBfOrfv0GovZ-eFfEbQarXkG-S6P8OrENSfkEyYHVRMoWTgZ8m3YZUziOwc7ngBvD5iAVrmqCjkO74lXhwVCKvUdLAnZEcP8JFefI0O_BDmZbfmmGK1PlYn13k3g6itLyrMknyukDPSuS43sL3mthul-8pAaWlmioSZ4LWX3elxueRFxL5y_5RFVrnf_iQODJkPgVEumXbJRpqwSrBCwDzu6zIs3VmxOpY-g09AO8tvBJs1q-d_nBJv6W61ZxVFl7Po08EjGJzLVFj5yieXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i30AedKWkp3ZNsaa5ypnsqdleXB2t_xw40KxhsNIPwuGfoyv4EbbzLDal6mECGQCLq5ghvm3322B8_VxZkiRxQijJykgf7LbDCwWI77JSqbGDZOqUOjqI1593zhBNG-0bMOFGxDceFEuIHgENis5caEcKuCbkiD32-1s7v2-3CL8hBrV5XLe-VF2NI3RYUpjkK0j9OnOex4ssvmcfZlYwtqJAO11bYBvFsZ-4d_xdCIwqfOqcE_zfpkkUn4l1n1zIn-zk-Ya6PW9wkS-grf1ps4lW6L_qdHdlMjGii1ujW69DjpvNNHPbPpFCjFcUsUU1Bdyj4Vr_4hob2QLLjXFdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mk-FKM3IywZUfkDyuQI2dk9o9vD1rdaWdS7VmVE4LO5iok0meNXTlW02GbuEnW9yme9WhJdLIckzJSZKR0HSIm6G010rTrt9ez6XGYE1nu40QkAbOa8-M70PJJqD34booonpqZthKxgcDRqCXslpm5ORtJSJBl8K8juQm5B4HAD333-kGRd3yjFz5yzKW_fz3P5sWjQr5mSIqQbZfJmVN1hBeO-WSirBT2I89kU_CxpEg9J1Yk1JaARSj_n-DN02ps0aSdwUiLFZrL_3DQZgX6D_oFnOhLdKgY7WBKon2sT88lPG6HECrEpZp7ioQVysM6yuTRJMnfdhUJteLwPVsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzEKyX9RgQzWuIhcC9j1W9XfyxlbSeank_YxABpHQNeJaQYOMA1NCAV4jbrWqLl9ElSrHUPt1yCzm_NI77ni8pUvNBWL7ga7ZgJyghHbg63lFCmX7_j08iSOSKmeZo16We6ZEpzcxnrdg9Bea-R7F8086zPS3lqWb0EWCqXmrq6kkVIybMCr9TuIX2GOBKVHhHmr-CnVXdO3_qz1mBLkqNw9lGcXLxluODTsf7MeckZ7vF21ji5Pn42OtY1sl-pFDFRxU_rQ87mQqd7ACciZgqrvK4GeVr40pnUH7LHJX6ScfirJs4AKSw6wuKv1wsemS-041MuWHGmUmxYToKvlqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DejKX_2D9WtD5OfyJYQFw9oszLBqHTPuNsCpWsviIMslqKDirVg5XbdgYpEJgqhLMLnMCjQVF0b5ofYSy6A_EMOdaLTjYypOYIQbwQGIh95uclnxHE7wsZxsuRqCvg7xKxITqGIld8o30SmS2_f-wCIGTP2YtLqQhxjr7Et8fF4Nq0OLB_hmxZ7rk2vABh1PWy3huEzR1ltPzxVX46RHfmCBni2_fBJ0rKp_4Y-2UH4DbKGDmQjdQXinbEFh6oczlNhnvu3zk_WapY-0R-Z7T5Rsq9XkSu6P3H47mbWiLdcxxLgD8tCmYvVAQ0fhp_VtvFz9SzCSxIMC0X-v3TOneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ryHWxyG-rX21q5D__wp8FTbJ78_RG1HuEUG6iB3AqWb8uS9Y2_6VbL5uW3wu4JFViQt31YxgqN3ySCyXRqPb2jp_U2Br6yoUYzqokRa6DP88wl64lrsDII_crpZU6l8j_vC0eCxgb2JaD1aAfaClsDBVD8XsoW1oTjE5-1-3Rhp4UbO_C21o2CfPcUccYjZRguzdHwCzjl0ih_hhUC4nH5TKeu00mtf9WrY3UT7PyRFEVzSZloOjq7-twcWAM4G5BsLaO15cOm5E0gTw2iHFm3-xJ48YkvxJIMJ6WanRx7Y1GJgohpOwOS89XwrWHzqyqwH1IXE3xOSnCmHBDcFbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/luTRJGrgsS04WGLrPV1L2aZSdHOE32ZqDdtx17-IQDN1l3etQ-qSpQBfzTkIWj4RWrlDc6QpXtYVFJGcYBZhnbIFxWsmhilCN3CwDB5CU0lev7W435vU52g-CriMgHbp5E-94AaJLgYmkI9HQXAf6izAHp6Z9KfAaezrOPAHvFNGPDuKGvEOTsab-w54shcA_tJ37yPE-LIakr3vI7mqsTeLTgu5m8K9-6o-XuhS1XjGdJobW8PYeng-qkmROvXkc3oq9BimFXQ0CwutbJzR63b3tmc3rUC6W5jmtW0KCWTQ5cMZ0ThbEq8Ch6LNiUnDNpcTS37kqLYZdKrXC2vJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgn-ajZ_esTLzj9tJa4eOOZREQ5IWCNBnxMXvVqFnJBose8RYj-txzRxGSgBHtBVobM422rxPjLRHjB0CAXoTIAk-jufZ023WBSb23li8sBORmeey4LFo_7qEoID1LcpZo3uvoKzu2O7L6ylWvxWjeSJF2ZoOgrJq2AZXsjCKl9pP-eJOrTtLOp8RN7NJKhsm7HQwVjEn9j4-gXW_YVuRZVFnwFjnezuo1PKQ5BHvEt_ZiA7g2_JA22yBtZ93nDw3dlvjltMoo5Orm_cQwxPNsd_LbkS_g_ZwAp_oj5AOzHatTEJNWCI-KFPw-vEr0xDpKzmjF9J1UJSRzo8bOlgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AiyNvoT5Jcbqo1aFn1Xj8mpE961cKycvo7V4qD4o-2RYrDEP3YjCZS49OupALHrdcWyllBYHc7_d444kP1oU8H1T2XTPUOoS8xjg3Gmy9E22YTKBIxDdiIKIbDzGc_RmbyZHEl-T4Ys6VYUf0xAq1fLYH4f-RiHwy-0cziy3nrGdBLlB8AcXOqUUramyX7TfuzFufNE6na03Cx_htRRZCXs1qLsSSeRaFoOrg2IE8Bquc5UDhkFyE84gzOPzkIIx3uglvXAcEuXoU6eJovi5-uYiTUvdR-RKvtP0bQpiipDNHYmsYMbnsGJtkGGsb_BOfWLz1juDW20DivYAYXOPoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
