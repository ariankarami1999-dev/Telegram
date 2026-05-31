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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPm6i7XpbuLruXA9KLV6XcDJXgvAwzzIFNkPgHBQF08fYni6aT3fKF2T6JXBNEI7ghE1rFRcR1i4xkKf2gQ9UoZ1bCLL4kqG9PqdjVdWrrRJ6cgNTIn_hvoTyUT9tRwIA2ZW63oWtR8Lv4I5s1c10xxMLpOGp158zNxlyX5StVkSD1kY57t_xA-0en4gWqWeBY9P9A5e5k-dtcK1jBwxBtJfMbKnVoggnWmBG0w0m2lryylajVv-cPgWfFV7pooF5irSYDYDFqMdU-_DenZHnzNGSWOeGcBqwYeZU38uZxF7n1QQPKH1ZbQfPa21doJ9N4OBER2cj7IbxFySzZYIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mErtgvfzMSL0PqA49tmjNhD72oHRuMLV1hg08yJ2LZGlbDNL-JCtWCFgjCHRs9a2ZjKz04utYkH0r-f2rmZAVLnNbXC2dsBcFim58mevpAHWGSi1HEDobrcqoH2ZOFC3UmGIgogoKj1PF8vrh85MCRxVH4nPpLI5vUDHBqbE6RUfOtarBlQc4z8vNLOdiN3QrB1ixFP2fR5C8BdnAgRJsYiJpTwZw7qlZ0MiIuCBkajbsoG9_NCDMxSnHrQBd_CHNkGABh98jT8EFyFfUIU0KNCcVFk26AdoGYE7g2alTnHdYEWVzO3g9Fxbyu4-tOCWeRZG7ydzEgnXdk9JlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJm-cTZYycEcTIbfp90RapBSPaFRbD9NGu_ZIanE7yUKgsMRFzgIZfdMBoah4o5xNOtsstOAi-qkK-F8tY3HiYgp1vEqTKg9ru1lov6-_bZEQ0Q7c-E9vkwfd19aXqShBY9VF12ytR__fVHm9FbzMho4aT_5jakeP-H9lh-3PSp2UMXbOlLMqiPdcwOB_2vU5PSfQDw-2wPTcHY8s331qAByZKBX9qyQoz1BgEL2nagwyzaYORzhXstaJAFzoUstPOs8UcY3tB4H9GdCb32w5AQGXN1d4JYjUjVG1hmDVevVvJdqtklr7RC5TJpRhtPnzgpEVjqqa7PLFDRy-UZxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opNzkJm_reRBq03VhD4Z_sftbTtdCdetrSNz7jGhIrW62xi0DlqYDiKO0kqcvZ-hIm5crqzvq5K6VB6M_ytKnLVjOzbP410dV3IpBKj7TzF3NcZEeeyZFZ72aWihq3Yc8tMDV95NQ6-ID-0g9_sre2PLZGoUOt91cMiaKG5ZdVZLqceOXLqdCWnG3tFzkAWFqq3W6bP7JJo50iLboG9K5Wdj_Hv8dJd5HodgaWYuqCHWDzgzKD98uTjfYwNg3wuTKIEtwdKuRDScf99KA2MHeThDSvuGSdZmZwhdafJYu8RbbJ11iqrIqivYw27p5boiZjdly3Ikdyc3e-0Wp4p_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
کافیه‌فقط‌عضو‌بشی‌تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست. پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a9
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdW0UzW0XcBl_YJDDPqNkjp_ROSkSqgt4ezymVohkUtuDqpujF18HCkAfySkvK2CfYLZSLxQTyuPOdjCHTmTAUal01OYDr_UwsZ7_y2QAKQArhYgoyOhfvyOQAZwWX4yaBfAqylc8BlsjNA8a1fqk9t4TVRbD_YV1CYRW3eY3XwzF5I4C2RK0o07AhkgkW5CrAftyLXV9cHrFIrP6y5-6DsOzRp9vv6DFJAWV_LU4ncFBrohxjZA_fB9_jhMVeX058lScR8alVlwgU0mTZxxC4pwgca5vNMq1dTwKbe9vEM9xNC3UyL-T5m-0y8cbW4o4rdKHaemQ9aW9Cxag01RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgqxalB68Es8dsVEO7AvKFtzxoa6wkRtZz0-cJxir3b8RmUlHoFTrNtm4dnlBCyeiYCGEE6uoPrtDWx9Co2QlkrpV3oJ8Xg6PNPHGW47vB5pJeNDgZ4pZzoXz4UuvVt3OBBVYAK9Lw10T3lSZlFlJ2vrYsnJArP34UFzyTPPLSmdT3JS5GkarJHJhpQIGKKtSzPEmLtCDajWzjKlDPE31b6k5p1WfEtYNQYwasXGQyNV94USd8DxjezumxZKJ5xFxdgvg6hxCpFgV2KIyZ3KFr4r9YE_aK3urSE2pO1cJ86L_04v8ZpP3SB3ZPu9_Dw8XtOPlcMT_RlEMICzKrEBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuZT08MogQ5Jo_e57mTqNirLQXOlFmut-3QbrH-LC-tYrVUi2IpLyrjSxEIFfLe1xqp7rlM2vZMOYo1enOuZ722qf-7nfPnrK02mKKadJZwXgy3VlLftVv2yDH5ZQ4sqtAe5cAy-mh9nSawDx5y8noZnSsijeaxMuiuEkSgcrnHmbC9Gd8YKYpKPtqADEUJvKNzCNCXdmy1J3wPWR0i08rThDv3sTf_mKnkNF6T3sblWZokvSySLJK3CmzYcXflMRt96fa6UjLCj64kh4vjpBVK5culkmcyGVWX0fGRo4vPA6G3FhQaY6toaf6dva9hiGGeiXYCtf_oLW7jUiX4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEx-2LLmFFd_btN2nkiwPEX375rOZy6yb-pAiuHVV1Bopm2X4nLrhwW-Z2I7QqJNcQlUOHI1qxt_osQ0GXF9fIgAD7zRaP-bqSaqHFQWKRUl0EHteEgh8RzK0nIF95Onlays6PrnXG2GRPzmWAPLUm8LhIEZAdZ0p-mIS61tF73glc_FA2rqNcHieE9V2I1wZiXGOW18sm7cvuFArEINNxM1yu_4ezNfYQo3XKs-vz-uFybfQdrqfVc8CDbgN9GV0HGlmIUfuR6rHXSNLZpGUZUYov2fULj_fHlvCjnsZprxabdzTXDPimbNiPNlWIE-W_-ZkbEpJCxcSTvZ1beb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYeq9LV6gEt_rNP8D93kora1aSvIgsPp6EfeyL32TQ7zNb1pzMQXGkVUHseOzoFKZBJrGxaBCko35tzBvKnJH9DVZA60ZViS0e3pPAxakh1COzs9hskCka_tYHn99st1GMCVR3YfONgIE-SSMWbdSgSGVf2_KQvSntNzDT2ZYwexY4FKBN_QZHHVA44i84Yc8PO_FLL2wAQ-LQlqNUm1pXVk1vEzJoJ3pKBPLWN8pc4OPXeIHDsWNBLNZX_StT0h7nMmDPtgA-ICpENGH9LwbhtKKyEpgCVjS5Y1OmZAYDVXlgkHwUK3G1f7mhKsr8BX-MnKggR3W9lTK81TX2mypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2qMaNCNnmD84eCODEZXhF2EK9G8nIOh5wdrxVwZXYWr_A4VYxvBMPewsJJIDP2SY4Scuy88MAmZ8cX0IjaqTANKnJmzpgWaHufv5V8boGh-0KV-M2q-od9z94XSYL7-cVbbvkh-xoqQOwGkShgc-SfpxvMY_Ta0kPwlkuvmnkbGw9JoYZNYArzxrNpILSEe5OUANYBKlS5CeA8pGtzCELvJKpSfpDRHKcUIZhLv4ypi6Csx2V2Vx7Bf2uvRi5huERKl3fQ5-LuTca_xOy0LjLfA3nmdTLzjM8Wl-x_O_TvFGnFtc3gS4YwAjHytrd05XgS2tj0DH_XPP1mD1Zve_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSseGim6TJb0mxVKoYV-_oF61hJ4-bwX001vLwIl23n7H7_Lg7ZnyfQ3K_YeE3d5abLrT3mL2L3i3V8j9r8kA5NZexvt_6_ZWAzjNQ-1WkI9JhdqrPsNtoE-I_etyGD1_dXFb5giNwNtfxsMvTIQW3t2iMc1lKRLO8BEF3sXUecVCtqA8a9VGuQbFV18rNRaVWsiL-G6KZVdXzMAzIa5rwZUgit4Wa_-7FvKp0sOYruOh2N81UXbDVCHouQ2jwJdpzBlADPDFHf8WARAJxGR_MceULYRqvhnBrWFbyy96Jrty6F2yZ-E9RfcXQSL9u059gMIZ5fRTPwOA-AR_E6H_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THpMoDKupGmfHzlSs3CLF75gskQmV39smeN5O8Rb7mMwSIxYyntYl0rcfmN1IHX7hzFXQaHdxwGriPhKBJvf1qDwPGF6xuqvrf1DI5G6xnRzDln2JUQbiPWNBdVBGVTUF8z9SDcIL1__WaLTrUx7lV7-QhxVr1aOJSAQmEK25MnkqmCW98m1yGnfEWRiSOu2P8l51lUciBK88h2Dhg9yTHfIFixKkr35Stmo2-QqqHumWZRTi50nffa4gfNDmrLb4I-mIL4L3-77UBW0LaKR8KxusnmpoPYqNz9Q1eADhQ0CZG34c0CAcApEhT8GlfgWwflHeEDKAfURMRIes0VueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSoCaP63f-vwzPcxLgrKSEP-7Q8uDpRTEJshTvTAQZ4h_ZzFDj0H2Ilg3XEtsb__RiR_YFIzrBVHp8G8u7edPoTkQ4j9eNc06vdNmTBetfxiR9CSPdPi_MtbAbCKrIovCzbq0dL3SPfJ0VLE3qiMRDYGstqwlmGjT9sKQOaNSpkwqslemf602HxwJEFn-JUR4fjmAwSpAxacj2mhsKOyHp8JUvQB6MgIqIjy7OpNE3HBPcbjqOagBR4H9U0Lf4_B2ySbN2bb20eLrkLoxnJ_LjlKEzHyd_oZ6e4ZP2BZqBq_0NQzCS9Fh0AkFGFwVwgjEFlLEIX0wOeM2E9QB14YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU3I4Rr4kRZgvfMGIOeBuORCUp6095tMHHJoIiqHn8rt404FWkfw8Jq_pvGAWWqqw1xOrLBXms3M2EHB35wVZIRcoGUFPsQ-POb7EcuQfFPuorSHFzw_FAstcnAMxyyGRWFTj8EA3uFqi_QUeq8g4pM9F-U3vRI9iAcmRag_n0wdpWJA3yLuwypdQ30EPzVnG5fdab-9THMzU-A6zL_BeOj3QsCn_H_l3Zqebm05G8LWjGXWFRHY7hAaeCr3l6nPNmvwDEN516xgmztLi-19U1SizR2fNveoiwl6aL1oT_T6Vv_w_hyNsu5HrKxvoJGPvbpcLY_SWPqgW6rtPpcMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmmBiRVpM3FB19W3Yi2AGxKCLp2cqjBVgqxayDDSYBe7w21MrAKScy4Crqt2j4njbA3TDkvBxzggouDaN5eepYbU_OFb2qHRndZDYG_W3lM2BTaR6ZrRJ4ihuP5Q0cKHAW4XFRqn_TFHRQl9raJPqcVHjo5vRZSoR_m1s_zl1Ua4HmwTK1NL6DZqizzAbkIPMI6fuG4CbLbWFyTAKu9BMkg1yZPHGK-TCdS1r2xU37go4Hbdsyu5JIx5Sr_Ynh3quAJInaFAcsCWoMiUhfbt1EzaA4uqIRN6onb5zT5U2YgOxCiZCB2jX2YYsXYZZfLH6jOm7MCYonInxyAUQsb-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=hizADe3hjA8Pg7H3vw3NQH6VyxFVsDDgVMbSx9_RuGefJhsOvEqX-CdA-r4X1PR76ApaiPvz-ssBcV9ZiEf1ZRzBt6CwMjpYCSDvBJDH6TTiLLO13Dnt3xQz_YrAwfw46dsH8N5mYwHiSK2Z6GF6CWJibI23HhzImXvabKLnntAfOh1mv2AO6IhIN1xSoZLw5kU2n45e76JAwnIGiNL3SwRIS8jFy_o5GWQmqDiyGDhv-aGt7NW6pNV2IdPcFAjduzaHtSDQ5kW6rBCvvRCMGS-Oxo599KPnyy9Q4YyTRL8XsYzd5dVSWRLiGX9UjRoskAWxxasVKYP_n7pNI0TmBGK9APcSpHbxSxdA_2kWFSczVVzdFo6UAGghRAx-mTa5Tz8WJvkpEbHMckV62eBY8NccVtIW18dlwFOTySBfOdkofYW-sihxZylZ_sEePEBYPWxX6nq7ujVlVcCvlgCCh71-Z_2b9DKSncYME2CrCAShlU1S03jAgiJUsRUJ5nUHA0GVaF7DVjiYpEybx9WFEDoiEagiAsFfM17TLMS7lHo3PQcqKA3j2KCApCIcSVetOID7r_c33Ch68P0klpAXgGDo_3-vagTohrePRaCemcUbNXmYTBVnIpQ2eshz3WfJHRIKqZEw14e1m9amPQTz1YpgPrRxD3hWRne3GOtOEuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=hizADe3hjA8Pg7H3vw3NQH6VyxFVsDDgVMbSx9_RuGefJhsOvEqX-CdA-r4X1PR76ApaiPvz-ssBcV9ZiEf1ZRzBt6CwMjpYCSDvBJDH6TTiLLO13Dnt3xQz_YrAwfw46dsH8N5mYwHiSK2Z6GF6CWJibI23HhzImXvabKLnntAfOh1mv2AO6IhIN1xSoZLw5kU2n45e76JAwnIGiNL3SwRIS8jFy_o5GWQmqDiyGDhv-aGt7NW6pNV2IdPcFAjduzaHtSDQ5kW6rBCvvRCMGS-Oxo599KPnyy9Q4YyTRL8XsYzd5dVSWRLiGX9UjRoskAWxxasVKYP_n7pNI0TmBGK9APcSpHbxSxdA_2kWFSczVVzdFo6UAGghRAx-mTa5Tz8WJvkpEbHMckV62eBY8NccVtIW18dlwFOTySBfOdkofYW-sihxZylZ_sEePEBYPWxX6nq7ujVlVcCvlgCCh71-Z_2b9DKSncYME2CrCAShlU1S03jAgiJUsRUJ5nUHA0GVaF7DVjiYpEybx9WFEDoiEagiAsFfM17TLMS7lHo3PQcqKA3j2KCApCIcSVetOID7r_c33Ch68P0klpAXgGDo_3-vagTohrePRaCemcUbNXmYTBVnIpQ2eshz3WfJHRIKqZEw14e1m9amPQTz1YpgPrRxD3hWRne3GOtOEuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1ZfkozmLKiR4VRrUSDSz6wGQwNjlzRWosooya08T9ih9gy9pOrJqpBq6oh9liQ_8fJA2hGGLIWLbNDwlNHKImRW46i4tD9QDyK6ZLUDPQiOSxY2YX4R6_rF5EZulsQiRl8RXJHy2g_5Q1JAwpA3SsiO9N3ZV17k8r0BIxZ7bbzcF4JMTw7JH8CR9lvBEG6q7A7BvWsWzqSOl5e4ZLBZaLI5JcmyqQVS7NN2jGxaM8-X8A--nYyqT18cwMdAZHXVudkXKDIl5ivLYVQapL3l9KaRCym3pDacfX-NKr_mjvLVC9AMwd-G_MZdrXXDwy__pzrbgawq5wWcHL9zErvwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cajf7t6TeQg0lE-yF9bxAbXKC2qJnCwz7sfqqN2DeHs_n8qfK_IHHq-YXPLy3uvwIgkReiPN9zEchoqCq9dwpKZg4QHS76TXjDG0ycUX5fz5g7dkeAbV0ft4HnzYu60sA2RH_rtoZ1YzWrRHlgI-sS1ZnOdISlWRXnnzT-tY9fBxvzocD2YphUe44I7bmTbRmJrBlkDZUrq_FT8UJ_4OADMKQt4xvWDXLmJS8al35Go5m0oMdxHZEnQncdRjnIqiIYqTVch8wSSMW9VkTLsczHGUqFxepwNk14-kygmfxOAZ1uh8xOmhzdiYDTNEt2u4O5AYAXDAUOmhi8NI530sZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5CBvzsiNcx_GF8WntRuyU5plYZHH-IVIlGK7rSoII9d194U8_UyZpZn9ZWd-MHsaJExUAz_x5jZ3sw7AK-R2U7F2HHXVDa3QgoCFaZCCYNTN0DCS4u59OVOmW7XLFge_QVsPnh-xGDr-UXyV9FUDpr1YWu31V7B_OpcbFwgJh3hWQAEW0CwYHDg3Yxgf4qkcDXRTr0rVYXymTKclSYIzChUEWZQlYKkalVTeD0QCHuChrq7RS5gfHGetvL-z_PQDclXfpSVpd3jMeXKZmZoCDDqUQU_f6YCOiSe5kUID7eCrjN1lO3GEwF0jgXBd3iFcp6sOI2IYesbz2wgoAfbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=YIvvORuvq1xPgjR0GzX_mwsQtQ25ROTRMJrwqZX-1JdcmuVm1Ts8MHoaYvEIi_6UmHn6TypxYKlqndrq7FBU87GF_3d4eLojgqZF4Wmk0ew636qxBdvlIcd0QLOjslIdSek90Tqx2ZwCdDkTrExGkvql3vRyP87e_ongqFk3MVVINauVQRnswELmApkFCVPfOeLovpuXhX-fLnM6TSMs-qZTVJFldazmFeGJ3z2xEZX-xddLRFZ6fIfOTJL7dP8MtZk6yQIsUzMg02iCQbYRJh8KaOhBbWhGb_mG1dTmozY21LdkaSv8851CAPlf0_4FNsZn6z41_sXr_-Yf2pJ6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=YIvvORuvq1xPgjR0GzX_mwsQtQ25ROTRMJrwqZX-1JdcmuVm1Ts8MHoaYvEIi_6UmHn6TypxYKlqndrq7FBU87GF_3d4eLojgqZF4Wmk0ew636qxBdvlIcd0QLOjslIdSek90Tqx2ZwCdDkTrExGkvql3vRyP87e_ongqFk3MVVINauVQRnswELmApkFCVPfOeLovpuXhX-fLnM6TSMs-qZTVJFldazmFeGJ3z2xEZX-xddLRFZ6fIfOTJL7dP8MtZk6yQIsUzMg02iCQbYRJh8KaOhBbWhGb_mG1dTmozY21LdkaSv8851CAPlf0_4FNsZn6z41_sXr_-Yf2pJ6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V93r-PEXE-Zd3fmauztLrNZ8-8bnduZjaxaFMSnAE-Qy4oNHOH1c1O8lmWMy1EX34P9NZUoW_aOcb3CAr7M-ac5nSIe3CLEOF2fl5MM2rQAwx_2_NBrBzjVQQBtparFBOyG3GAv1D4f2jyqvnbKaylpmPtm8XvRUbJnViwmHvtyFA38dQVwgrWrPZo55s3z1j6hB_7DOLL42meJ8K6E6kJKh5lZfTM8Xsb2nBlcw-MHS69JxIkvAGn-Yd9elmik78uXAOgm0nFNZBMg2l-dS-eZ-9i7V7x6D9yKXBY9OEizN4u9BBF6Ct_U6Bu9XiyJ0Bj594jcblt37WBKXR8n2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd-shwqVK5x2kA6NgcisHkNF1soMo8BweDllMVk0YpM6MUx1Q8J6tfg462W1JTl3ChJ2WyhA2J3xxUZfF1KyxqD_51gkQxTIjUgC2dQO2jWJkgzvzRR-6Y8WTUWdbGiuzLYOUuKHFJiyaTZOXvUxaWq7r0UjOLEycItZ7qexDJS6ga5SjoCVpdzuFwUbvdGcdHii3rdrF6tYIb4KpM6Jk7LOGZRgXG-hu21GqG1RUbHqae2F1NIBIGMiLAw301jDwHXh--aOqn9o43MV1dXywoS8jnu4aR252OhxKCZEsonAeh6eBYwM3NFi13_L4QrB6OscxBJyO4pMoCqNvRJ3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6hx5fDjx5x4p3moHc8b_dbyUMHLpDb68Er2tbRnOT50LIeVX3Qx46mlb92dQOWGfeqCUzLmnO6r6bea9tnBte9VwrAlZv7j2oPSuNxjxVuH18ad1XE1x9MNiQOCrEW6OYjOMMEhH1oba_E_4oYqVbsm5xEwZQIm6Mr5BUgZZ5c_Hu0QP5wagb9sy44JXnBr8iLNMNvc3DBPOrDcyOuRdhDXEouMophnqf3UawLJaC9txJAUImazJTefRU99rCYAVnKwINXBFwNRtHBFXmyIvoXdeNq9VsDEPux9eTvvgFcP9YquQiFQ_5d6YPGzeZ7H8lOKa7HndHR2DJn_68kAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttcwv43nMB1PffDMyIzR6_ZJLNwYLzgOr3SmRfvCT7ujpz2ocSSAgMa69WGenrPJO6qIQ-odEm6shU7FQxBH5xHNJ4EcjSC8DwQzQZFgE3n1fg5O_yHNboaB_Xk7jJ77iI60EbXhC2dYNl1J7-pbhVp0BZb-s6rKkZNjuEFg6Uq5yj0ktNSAB4UBX5CHiZL0FmI8i9Rolp1X4RkV-YvnTYe3T4VUFePg-kd92B1Tulh2JZXC-8uCdrkrYNQfNPmEwJhtF3anxggC7D3jHD2zynMKanlps38lxOrs05f9ETkCPIPWVWQbwjGo9u28HKyH2rBcXTL6bKvOxnSzeCQOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiYDKOiIKCF9Lk5PvhS8X5moyvWuWWTW45TtZ2IAtrYbLnMoPaZk1jPtcrrY-8XXfj5ayq9R90XK8LUNeZF6Yax3vZURufDw-vxNDTWBDHaTy8jC4RlNbvYSFy_yO711CR8TdLownhp2c6KLcooTikGWXbtmvrn-j-O12EKbu-abkbznkCFQmRiTUSgxjPtFCFfnoc1t-hv6Ivowx_9kg7ETLO4JL-5AMtjj5Yjtd2sH_dVM-7lQsUA-lol21QrN8A_Qq3Nwcq7xZpYHWrUzDGYgKKTsY8JOlQ-vlb7Js5yTuNTDwV5ZiTCd00dy5IBjvNVkkLM9LQIWwb_6qk4-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK_i8N7oGyfLfIg8Rhlj1ZG-IZR6SrJWCxh18IK523f0y5qbX8qkA4l-UxiLhwPWWDto54vr1wgK-sdy_2eRzB5SRhXhHyBeZdP6i2bkomEBcdOulLyOMfCEqzBR8SHAli3hCpYial0IYKCzDsuZzJfmNUHWAxDXnt4HfXe5bPG1LzNkeR2Cv0BI3jCQsrFNx1YMUeKu7dQadEQQ0MH-aHX6SYQQHhJUNRuyyGa3fK4Wn0AOaaZRgwGEwEUHGNG7XNklx0qclUPjUzwB8r5lmiwMAMlnQSu55W8raYuomrQ5-1NbOLY3Td9iHTrA4iOjH999lSY1kYzCX9Hwx7iqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ott2JlQAglneESVFWtCOwITjSJDjD2q17a-gHm50zV7ISt0e8XeExD5-_hEDbfpwxe27XLDfOFufVOcRD3nn0Z4WySlWP4d9DtcaebdaskxfbqTjeWGYHkEaCnEKMizM4GRBiocvyhzMwyovAVhPrPV8leLbUtf_xRllv9ITmO4CBaK9wRiS4OPr9j_U05tFJpwF3lN8O8a72P0FvnWKHzmxT93pZuRlHJaa4vEekeIRRzkyEHbkP6aW0PVRWN6RFeQFia6cFZY4ZoWJ_HP2HChumj8X84pzU_UmXOrX5dShgzfT5qLdiJp2wtPfbzuXVlCY7f7iDup6xMB-2i3CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTZV6DDCCWtNyJVPmiljFR25MiWYMOYKtWNO-yYA0vwrHKKsemNZbRy6fOJBbb6cUNcH0jhHAp1SuVJ8K0iKKnJWoGcc_JCOjOggWJtGZ2KpwrtPnwHmAHETCRxNHC113gvdg1FMF2DFjiknartni_-PSoT00wo1Z4ulqaEW33rrMxcscy7rni-i-SIijMkh2vuMVXkXEOcx-6sfiPvY-0LeEVyCae37xjuYZMOktehn_EPhPDLwzoIrnhsQEt1OvpKJQGCC3BF32S6wzm5vU5TVTOmhTaGyAM9yLhuTUs0QDbX8zHzPx_YBQwAkd76-vnPvR2FjKQ_JI-IIWtkc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu1F7FcmJHNMfP1VLQ8QIUWf2raGvMxVEcV4DSDc6oGLamUEWoUIWpTwDtUPqDLBDx3dV92z-7b9gCCfpxR_pXX4alBIDDS3elejmoPyHKwGZQs_Zs7vXor9Kg-ZnTkZF_x5Jv0mQiAQ0Pb-MV-pe-P-uqw1lkLKJuy6FD0VIjCBG0wdtaIHsA6KgMZPSi9ig4FBibBDAfgtm-K4lqtN6IO-sMpywFBQM06SQoQ99j45olf_NYRfIsPq_RXl36KnU3jKStKv_m9Ywg5aa3WR8KPljGsKI44uu66htKEY5-WT7ltXTZJobOrsGpweqwTSXEJe6D6a9_IaxVPeLUND0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI_M86YhoOQhWcYhG8JQGWNqnEDC18TJ0F1sVwWuIR0d_jE0Hm0mzCFVl2Zgi2yoJYtt_qW6e597vTdsH8DN6J0a-MmZlJCgc42PTxrv0nPVKkiKylSeA-iQQBl-ZEUnUhqDz9SXaaqWin3mq6qplJHVCsD2AnSa3tMzWhYsP57I_tah7bofPTSJ1lmiCgjty0agXemeitvCMxiz_aMt1T_CCKtCdqBziqQCj71Zs_Qtk2zoZ35UBKIdBPEnxY9qk1lNm1hHXJKK9k3AC4piqfyZ1BklEZuS-2eEKfzhjXB7MRSnbcWwbQ9SOHSQrz6TXYxUWFkcOqgt6HQfmfMmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jucgwh0I01wSfG4eDiL8niavqKYEE4sd80eSeoab3uWrtK0W1iFgoKPZ-Y-Bz2HZkZ0RvPjs7BgNVghuTvdQcXc-CW4CLkI-8JJb9E8skxb4ei_DEsj8OZiPfRXw1IhAQl0aAQfxkjL50KEJGWV0jjzYpRG8qJ4RZ79ikXp9LQFxJ1vpsS97gNgfd6ppMkPIY92pMK2xYR77INm4qiadr4xSNMbfio6KtA2AGVcok-xbTwkSIbV4DqVtq_X81pajvdkYSb9lAxwoFAfBSPWI5fG7BsXTQP-2pCqekg80cFpIsFCCMe57kpMrOqm9VMCXo8M_7y8-9QmpQ3pSI_nl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtyV7N-e_wvMj0hGvKJD3dwi2N3XdBrcKdDTubBMosLTQOCozWOznsZsueiUKPo_NBoW8jQCLUMel7mWaRMbNuARQh-WDfIHk03blTYGPDTE4IGsqx60DOU-Az3GtYrQI2OAR3DZkuswU2SsS0vHwSfAvkM37uuqo14lr7-NkqekzzKC9-yB-aQbcK-Fjj8TcOydFCuUwQRUu-YARy4cJdwcg2s-GADXwWSpckpg9Z8mmKJ27RMTsVZO0_fr3JUaMYEWl18R8b7a1l8GvwsbNennCqsnKMxSYx6ZZT87qDLetrinnQvzx5kCrZM17vEQ4gWWkxRpR8J7yv92V-6xoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npBmXBusbVkbks95MN92B-ewfkWZX5UcMw_S6HUouAP02cHETCc1_0i_DleaHXdhRB4NMkf79CPAx1mJRMoYJPwnnGrPL7ycRljQnMft5wfUCeOLXwcD8XJkdJXI-ax85j1aPAWCI9-cjZgpKiBZnpvuKRSRiv1S97WEPKaUHASWhC4GzFBK6BlhHFm23SJo0BipFRIPUAxaVlbxgfpu_QXLKcDcuHTNM-yapj2dgQsgvrnNktjhzL1tuiI6AocEqiUv3iM87Z-_XMGgp4QO2z1mprgKeFQAd3y-F6cqSMj_5BUiYsD5dMc_vx7KLS59xAvwoNVMmRoH0gzW_wamcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0XSfjn1vFgIOfm4kYGFq-tkfCxHzu3kFw6OivtOljsg6l9R3lOi7xUxM5CfQCjJKJnfQqd_X6jdQbKAJxBMQAjwIFEAZhNJx6d2KXqSzZHXr3OgOHxyQZ7dr6BLhOsVqcjc0CGg1ob4ZjVn5PkTAyhnCzS-Z8kgwEwoQPwNL8gtfRxtkPFeV2S_f295j5xzNCv1Nc8zRW5vohAprGXcEc70rlgFRLa7m_CDJyjKiPnYD9TCu4d8CNKK6temYtk0a-BDaPYVu7nK7O9EsHmX0Ct75svfjUiGlz1BV8790bK6sTbQ81KNXgU_2I3PSRQNehqhiPlOM_dPmaZ9sWkMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgbG4htRIsTDLbUw1ltjjHYbemlxYHE9fohC1P_o2qb9Dhvg4qbG6_RPeCr_Kkra5KF0sNHNzMDl70CaQbL_eoqhk8Aj2sY4NHhZqDZ9-TIDvdHrtz1HuVYXO1WhaK6v-U8NSwvc9buuTOnJa5WcBEzsziem3T_HF3q5zUAu_Evcz0nrPidYswwSnF2QppLYRnO2Ep3FLsQA010bdvtINIJvov0xCtkR2ZZUKqISEg9Lo88UWBQKFUxDeL0ySiUuz3iiRLsa8UYpv0jwicpvWZksczCeXk7pJeekjsWtJfDu8CWTTlr9qJUijNjcjqJgdJvJtmuLnbQmVGw_2uzUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=kuiL7A9fJgTocHxz_DNEKlvuI2ihpNJ4mqgOWvdcAQJofGXn7hresET_KE-eDHKEQwSOBtH5Mr7xcfAodi76UdWe0Hd4SZ_iDx42jb_8nWcbSpN2LH72VK83MwiBFwdJP5A43REDz-dTdfJKb7Vf8NnvBkxEnq4t0khS0jN2mGPxI-mHdH-OhMt7FJC2kb9OxiunyS8REOdCcFf2K7K8cPZ_s5P3FAwYtaQnaBOXMLERO_fzkF-0Q-EbIdAL1CWyS6Q27rwzlBjhQpexIbJqwmb0jCW4y_v4NVjjsC18IHHd-C2dF-JsUE5DxYmmJ0KsCZX0W1Nl56_vQfrQH_J6cpe5SxQuIpNQMaaGwu4q3lfqp8AttBkdrBPlLPKDqZdzyJtGKx4JAmlNIxUi_ohNbwnBLgrzdRVLYmnMZsZj17LvEdPT2RigCAhdKJzvnxUmOK569GfikkAXwVixKB_2p6P276j_2EA4KOmp4spf4w8DKAlkOnFG4WjTbh7Sm01zGKqdsICjKdKw5Jf5Kwi1VtgJgDNN-BRkNOztsgs3xuL7anPH05WUyIa5WDpnkKTFH26VY72dAoXsG3wRHBYMky2hXNJuyEhdrIKIC7hBoA1bogIuDmL9dd819W6MbFKWob3iShS9c2HnWlCrCWvhF9cHS4EvBJntShhhRQG6Pgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=kuiL7A9fJgTocHxz_DNEKlvuI2ihpNJ4mqgOWvdcAQJofGXn7hresET_KE-eDHKEQwSOBtH5Mr7xcfAodi76UdWe0Hd4SZ_iDx42jb_8nWcbSpN2LH72VK83MwiBFwdJP5A43REDz-dTdfJKb7Vf8NnvBkxEnq4t0khS0jN2mGPxI-mHdH-OhMt7FJC2kb9OxiunyS8REOdCcFf2K7K8cPZ_s5P3FAwYtaQnaBOXMLERO_fzkF-0Q-EbIdAL1CWyS6Q27rwzlBjhQpexIbJqwmb0jCW4y_v4NVjjsC18IHHd-C2dF-JsUE5DxYmmJ0KsCZX0W1Nl56_vQfrQH_J6cpe5SxQuIpNQMaaGwu4q3lfqp8AttBkdrBPlLPKDqZdzyJtGKx4JAmlNIxUi_ohNbwnBLgrzdRVLYmnMZsZj17LvEdPT2RigCAhdKJzvnxUmOK569GfikkAXwVixKB_2p6P276j_2EA4KOmp4spf4w8DKAlkOnFG4WjTbh7Sm01zGKqdsICjKdKw5Jf5Kwi1VtgJgDNN-BRkNOztsgs3xuL7anPH05WUyIa5WDpnkKTFH26VY72dAoXsG3wRHBYMky2hXNJuyEhdrIKIC7hBoA1bogIuDmL9dd819W6MbFKWob3iShS9c2HnWlCrCWvhF9cHS4EvBJntShhhRQG6Pgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhUX-slv891g0vQU3QukrE9Q7wZDv6R9QHdQSLf2oZO6Cn0j0Ver5jIjQsUxzc2End0KQ_woM2mwpDmgzLf-jUHOJE3zjZuFKCdbRDaSwz4U-SrABT_PzekkmkuenKiwK94TAxI-eCmtarASUu1Wr34zplytFl3WojCpcRhTtrGFTV6XxRaK4eXb2dDiiEhSmRz1uLt2kFHWr5Yx7F5aT_CwqybY4uRomY0epGqUMUmI1qUM7dTWLwNBBtBowARECqkI_Ah9duyDn8rteT3raCiwRtjiDt-_ItTImunTwANPXWZLIryiSuEXkvM58sjKVXnr9NYzSxQcXCjW_v6taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3gwNzqgdQtDCxS4e2_b_CLdCtSMrolx47TOwYoYcr2-56Qb-yPjRzfb8EdGIm04mRMCTt2GtJDbGHRQb6jO5hFvY5AoaajBC0_Q1wR0YXGXAZWVuynsJkOmNdkfBkqnvtPggSDt94EezD-Jcm_CBw53Epmd3C63Ferw3Cc03t9wDRaKj7mbskaZq8PALR2E6kISjxUVonj1O8ov1MKyZUvB9dPhtQFZRotu1-FhAfaTOeFM0srH5wDVAFTdKJ1NkD7KLM3tIepzOAoppE9_GO4FXvkYF3j0Qm9CVGHbcrkEKjLQO53aKEFHKvk6s-gt9d5MOkegzFpWOTmyhWdrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THhVWb5BZ5iDZ9M6HqbJvWqrx8fV2-NAYbDoQKLTr61l4Fm5cKwv8IhzQqu2ZOnDyYkl_d2w6EAwgiHp-0gOj_x3DoCGqAcrWsuUE6Yl4gFLTA_QZiJiv_4Zm9XSfr9zDtD0c9XWp9fOp1kU0Rv4qm6MZxQxk20Yg7Nidnq3_8lTalpMlj24bqznJ721Rv8Z-MgRVGRxNIAUKluSDkm5izJ7Qp-99isZH77jW84qOPQGN9uRrup43Jw_02br9GJaGxT1RUV1q6xoMbg3Vn7snea2eXflXCfFhU6x8pYcjqMsVfOU5OW-8xImujQim15YgA9cbZiXYAJEHvjmwaR8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=oGabjA-hO98MjC6IrYjblOhjF6I8qInmjapJu4cHQl9mMpdk6BgpR6zTtTr8E-t7w7RzypMFCUngseEYKa6i9m8RgUVAtaIP9hnBku25zmRy8oGVzDkz9kfdaUM3_2LfPoZJwb61pAz9a-tVGqKsLjOpDCbsCv1VJXdMLq95RQI-piMdfafBEKC8aW2uyYQH7jlhiiaa9-21hkKAOwJtjVo68hAcXtV-12meEwpvibKrZfFhWoPTzug4_J1yaCV6jnKvSEk2zjWKcxMo1Ms61epnawfL8t_Vh_nxYh5cj76E6F9S6KjBkQHQ-cGcMTKUxBaiyhxJF-2CuIZfjvAGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=oGabjA-hO98MjC6IrYjblOhjF6I8qInmjapJu4cHQl9mMpdk6BgpR6zTtTr8E-t7w7RzypMFCUngseEYKa6i9m8RgUVAtaIP9hnBku25zmRy8oGVzDkz9kfdaUM3_2LfPoZJwb61pAz9a-tVGqKsLjOpDCbsCv1VJXdMLq95RQI-piMdfafBEKC8aW2uyYQH7jlhiiaa9-21hkKAOwJtjVo68hAcXtV-12meEwpvibKrZfFhWoPTzug4_J1yaCV6jnKvSEk2zjWKcxMo1Ms61epnawfL8t_Vh_nxYh5cj76E6F9S6KjBkQHQ-cGcMTKUxBaiyhxJF-2CuIZfjvAGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeSlzYd3u--zhT0fzveueRIoFkd0u9zCEglZMrBtPx11K73LFOgQPMPCTd0HBYyOYbgoIgSKWgXoOcdprizvOyXGiuxKHrJR0sZY-rp0L0wsU-Gei7_tuEI4c076sQNsK_nf--iuZQpYyYM3tX_r8n9qxXigyqIt3MpFV10C3OkTIjNvn8D6Y1kR3E4c9w8ErC2wmu5Bd7EQ2excGYq-OoQgqUr24uJ-t7uGdEB5YotkB3d8iOi4RDK1_y0hQuiJ9g2BSV8vBKX0EZbzereMf386XzbIWIHpEUAW2bDlTbIItbBtstopExXDvJu9pHl_y8HAh6QmYQQhudthFuYC3MwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeSlzYd3u--zhT0fzveueRIoFkd0u9zCEglZMrBtPx11K73LFOgQPMPCTd0HBYyOYbgoIgSKWgXoOcdprizvOyXGiuxKHrJR0sZY-rp0L0wsU-Gei7_tuEI4c076sQNsK_nf--iuZQpYyYM3tX_r8n9qxXigyqIt3MpFV10C3OkTIjNvn8D6Y1kR3E4c9w8ErC2wmu5Bd7EQ2excGYq-OoQgqUr24uJ-t7uGdEB5YotkB3d8iOi4RDK1_y0hQuiJ9g2BSV8vBKX0EZbzereMf386XzbIWIHpEUAW2bDlTbIItbBtstopExXDvJu9pHl_y8HAh6QmYQQhudthFuYC3MwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=k_xOCcVVrkVykQINyennC1bZML5ExH5965YAQ47Qu0odfT8WvSZPOOJrXruwT2YbP7XbsN1qaPSJ7vdP6ki2ilpDQxnZcqwxkIaJ1O1_eGF2MCA7GtF6vLapAVmZzZewXnQnNGPeySHgr2rL-SS8GGVI-E0Ji8H1klyATdUu6RIhsSCmhEcL0vM2GyJLx4-Z8OTCM3fhsakb2CY_976H5ONxlRlWEe7yYLpdUBdf5fmPH9qIS8jL8IF4IHXHRGTZDQkNhYh51t19CF1Oz8s5ew2mRRPukELdGPPySS3DFBxmXlvvpX75a1R0rOLj1Ktsl1r5ONMo8PK23GeE9ryBKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=k_xOCcVVrkVykQINyennC1bZML5ExH5965YAQ47Qu0odfT8WvSZPOOJrXruwT2YbP7XbsN1qaPSJ7vdP6ki2ilpDQxnZcqwxkIaJ1O1_eGF2MCA7GtF6vLapAVmZzZewXnQnNGPeySHgr2rL-SS8GGVI-E0Ji8H1klyATdUu6RIhsSCmhEcL0vM2GyJLx4-Z8OTCM3fhsakb2CY_976H5ONxlRlWEe7yYLpdUBdf5fmPH9qIS8jL8IF4IHXHRGTZDQkNhYh51t19CF1Oz8s5ew2mRRPukELdGPPySS3DFBxmXlvvpX75a1R0rOLj1Ktsl1r5ONMo8PK23GeE9ryBKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=u2y738rlhSrH2cXANASuqOe7f4a6_ecJiLqs8RsTCGReLIWLKxhE3n58mihebvBMA3_C-5j13rubw08agdnO9WflugQV86uss-2mmK9b4898J0EWmuWzAp83t0LeNmOTrcBNCWpTUZf_8p_DPAqDyuUgMoefcZj_5a4F4Qa_8UqwtJF4Cx2tC3CYLxAvq9CvsD25VW04Scrstq4gHHdB5DBXwLPOzmDOwJmArEcoVV3NlLUS1O33XECrHF2v0VZKkZx0ykIbCwbCaWGsoXHVbhvd1uxfv0pBY_35kMKtHMGz8nqiT5b5BYM34KBtV8YAlFCZhh_wy5SYf7kEvoGRbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=u2y738rlhSrH2cXANASuqOe7f4a6_ecJiLqs8RsTCGReLIWLKxhE3n58mihebvBMA3_C-5j13rubw08agdnO9WflugQV86uss-2mmK9b4898J0EWmuWzAp83t0LeNmOTrcBNCWpTUZf_8p_DPAqDyuUgMoefcZj_5a4F4Qa_8UqwtJF4Cx2tC3CYLxAvq9CvsD25VW04Scrstq4gHHdB5DBXwLPOzmDOwJmArEcoVV3NlLUS1O33XECrHF2v0VZKkZx0ykIbCwbCaWGsoXHVbhvd1uxfv0pBY_35kMKtHMGz8nqiT5b5BYM34KBtV8YAlFCZhh_wy5SYf7kEvoGRbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-fRTjLqBqHAq-2f6EdYgtnqvFU7YZClwxIFl58xPUkLWn-7sTle8idVlT5MNWUJNpwl_2cjwZgVW1u9O0QWmLGO0O4LTqTqJL7gZONB4lBI6FE6erpJ41zIOU3ASCYQYlFJmxQNpsk1O3ZU4ljzpqNUz27cb4OYa7PQalRv6jSzopZdjiaC3xeX3C-QADCPUoBgrD3ptI39b6c4EzkjenKV8uwBe-8C93F0azXEVOxjSIuSIFGZTf-_GSJ5EOFAGja49GgxNedF9lrDvrS645-kM0nON4uSzWhUIV4NKNJ9FQ-lgHGHPqrfEXUczfwQyEYdFbIpP9PPBrMHKiVBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO5qt7ck54xr66SG5vo-o8cEVhoHGOc0hMa41Qd1UDZ_6OKl-kygYPf8F3tge1VUOWkMM7FCs3-gT2B8OyQjlptsLKz73jVLMwwNe58h_gF-A06PRkYkhizgTdEhm-Ju38DVYvj8fnW2Rxj-7AwCyKzVbtbnTyem_U1pLoQd_bzqp4CBT7oqwXQxKMLZHAfdf-kzOxmHJOZiwD94-NZLx53r-SBLRkp88FdvFSMNfXj00XUZtrhVndcJZd_Agw67VhqHR8oUezyGKtgBjvlYBE1smz35n4R1oSOANQsJ_nv30h9OmDEf92jyEeegoJc08cbQ_5JAJcKF8xvso9j3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLk72qe9Ln4wZUkTTNcxcrcWTnOFUZOME0f55FYwcsISstXmAlA1Ox8HaRkUgVtkjfzR61R8WtbUscbD_2nb-K471h42IF6QH17vOysYR_tVFp15kIeO-EvSB7XJbwbkCqAlGmPEP4NxGjMssc4h0Ua7WCkQFxAt-pWnDgnBfjJ7jd2MU8gmqddVV2AdNMFTfbii1mFpYwMlD2HMhPqldLey-kpLD3aHu8ZlWgoLKew6yKykO7aUX9espa7DVLSRfkq9le8sQg5kVzSOv56gb4rn54nbVY3X5IO-XOzFhyHcAP67nK-LzuafQRyn0gcRFMv1nl6y4MOpD16RpJlW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHPsn-2b2SDzK3JSbHH5RlG9mFYCvgQAMrIsMwTNNOHFy_Km3Mz172HEDZmp3Vkst3umlKDm6Kd6COj9fAtHgLwxZWz4yMgPp8bItbHub-9XQKBgLuk3bYTnzawWyTb2dz7eZdLNXe6uYGPJ9i8EuAJncJLlqr_IKR0U8mhsjA-l5_-D2F9CnMExZrCdCCLQ8D7U8nrTVv8BySoahfs0LMmq-BUKp9BFiviXWD0uMJAbFUYA73nayPDLHpDv30gVuYQRjFkHlB1oNxTlqms-UPdYwqZX9jFRfj0T0WLh52dVYxScs2SUbqmiHYKDLvgbqwz3xi96B6J84Tixvgtkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO8HOHYG4v1Zt6Q0MbLUklJHvc2PwSJe79lEy4VTiQz-3sjB4c8Yfh53JH28RDdGyOh5Acr9b1O9MwVhegTDjLLXvBwAahpPBmRYoQmQ8K2GPRQSAnJ4NkoMsHtMaOkNop4vKu4b3Hdynv2_mi8lvlDoJdyFU7AeLDi7Q8yW6HL-GNS1bGpuJRBWJq2qebDalPtzsAVKumeemwEmC8TwZU5Z55AIVgZFSgGIiGxG9DEeTebrL0rOvy1gsY8e56rJNMv8kD4FRUKt5pW8Go9d1wLCbXGW8bXI0SrkhqNHaVSARup4CyCRedSQe39Ri_yEXA-P46bsSNP8DReogUhXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWqZI_EqHepXvSJmiNZBkdcjEc_FlEE5vRIgk14kHdPmsbhMYC6JL7X3HVRc3FBX3KD9A_wshn67sbLmXqfLQLYjZ4O_9dd19FU6z9QDMldhIET6nYoiyWZnBsEJoxXohIrlBc5dKJ9PEkFhz9vJSJlhGXQSISJ9xduiFHWdrZC7apBvR81Fx-DkwU9pnr9G-czdO2DK4m5VzS0lIpCs1-hBZouK_IOp7aZg0aKYOJjHCmlzU8hdgjfOQzERoPo_glj1Hn7GzY08qJzdmWLv8loA2RYZ1OfgYagW1XJ01xq5CuSqCBKtqMDwNvEi47mf55E3pXRI6mrFbPpon1_arA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjKYYZU8jMFnxwkK7w2wIraQeCf2uTtymFyZ6QkzWsMkRuG9sYpE95e2XIF4F2CcGKuYGpSK6ejjWS-9AD0GFwKbSqzMYrFKwe2LSnNyiFptAGF4rtNH4EdzoPhq3v9gsJtNJrVG50ueusYfUDCLuSVE_6wzNv6QBRuglJ2r_8jB0aZ71Qy7awzrp7U_FtqqHwT4KG-lNcONKBjomo81f4907ons3rpXyL4IHdBQppyr3Coq2eS5F534wiMPWjDKyveuXz_TsM_2JNMGrAMm3Dau-Udx-2FxlafA0lUzX3hXKzrYlXsDAHGiG8U1_bIuHTyM0276gLvqvjmJpN5ngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnAX7tEwVIoXWagwLXSJpvd2VzvMKtirLE4SW2C7rqpNUkCOLKIWHy5I56kUoMYiPMhzjC4BI1mOkiAqdKAD3rHulB4qFgc8OXXBfWOZJ8DXsbbMrjWQ4XBJ1r9eyL7J-iN07z6vn1HZr0lwv45EeduM5uDJscmCy-fJ4oCVyeOKqHN8PjgdR2v2EgMAjGQBw8XUWnvtC_tSX4gH6tmA11nqcEMgMcd0xQ0srMCYxCBAW6IeDucaCm_A5bCxjJDXlig2Oe53wAaw6WwI6zvB4aIOeElwbQBCfKuddRj-TG1_a9KgycgaYMA2HcFa8t-uQ-b6hYEXcCCo-OyD1OovEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy9EBa8IcTCaTa3fvywHHThjPWjpDvhs-XsjwKG2MLdlIEJqTiZ63i8A2T2b2uQiGSFNE6oOeja2rLohm9P-qZY2XFYuOCIoInm5x9DFXSGUnbIs6PrBRGksUO8_3bZkpXTvbzcCx5eyo5TrPSuWHd1gstBucs7aRYSJ43pn_jo50XNtCEkcrA0Pq1j-1xhujyW4Hwe2BLAE6E5vUbJUNkRZW7N1NABjyV57Ok2Xy4NsC_ca1R3dgxIG_1JSAaEUac6EYu_YLzR1lITLVZ_Au_7JR90HMqu_F8N8ymnyfrIhQF7AURP-fC3BiBtcA_7kfAGDHcl0_L27XVOsu9hxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6JpilHeqtvFzP-seWy-xHEQ8te804834-CgNCcVyh0qyQOg5B9LdsEy1lDtoIYg-yyFcwo9kvNGw59PJ2SeU62Di6E4A0hHHq4NNsSo4XImmufZiDkdSEfzm-BOavVuWnUAGXZYqk08xG5H-ovvOkc-sxaC8Tj61ticW-gw-sy-IZjdWCcv5z9lPFKiqO1KYHu8gBfVMrEhBcAvrr5i9Wjnf93Zy9UGvnICEtZXemgxeITxOBNxUSKhPOQ4QWkJ-_PyE0dhl50eiRAlDepbxInuofmIHMMwWs-PvEC1DOTPRmSZ-NvW5txXLvbhOpCDxhSb5Ebt7GVj16m2Plz02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_UBFbaO6QzJ_uP5bOMxsgsl8fRyyQEpVYzc4Jff2UPQ50ngrEUS6qLeQdDdExXnMWOx1XS7FEXPyWY7pDiTIXq3Lw0oVjYYWZYHVhltFaTJu4BGnzTVGW8ZV6aa4d45ezVAvt-seyoskZaood0PUavFmjYwOOA3yZ06pMLhC0-EtrFlsvTG6xp77dSvFh6K7P0yDZ9aO8NCqKquHyJBm-w6MNf_ueEey4f2muUR8GXgGMiThJDG_1rh_WRDztVwONHRvFEOycfLWbBGXLIGswrDebkDZM8TAwkynMdHdzT8vL8rnFeaDDMo7rtJAzWvIBoK_90Hdkr0fnajDYh_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vygfrZe0peBqy5wLGPv9ho1Rn3AHjyw88VF3-gHAEpMTJzpHXRgHPsssoi2yP0pRmJ_iiIGTSoXwqE8HD7CdwXLy3oI-yEdMEpqjrBnMztpRtfqnCGSi7Zp8BZMSXQnn5xv0n_KVT4PsEgXCoMSnMx0MJ3JV-nwaVh53TPj_DWvYpC16CNVBdPWy08GqfMF4ygicHHD1SxaXDPB-Ip4T0P9HWcuO8xEDjx68HfVCl9EmK6mAAOVAmLvovs7SYcR6rXFSWFP5f34hrYkixLyzR40P4KsgP7k142McmYYX8mBbiFqr4V6ntuBIDPyefX1u5ERDJD3o0o8tjcVtxv3KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqFSyguSZqw-DrTVuvF8RM8LB2RxcA6583KA2LBFK2-u0_y2S8Yja941odAa0OBVENvwtOSaAF8rqMZCCpq1k2RjyMoED_YSKVifz0kWoYyvYHLtU8MG08_DOvoFT3_fDyfTUhYnaCZ78NwvOby4wJO1eMmXKlRmz67k7P9u2ym5iNqpU-W5YI8uw4hi_slOKKmEulqcNOxshYPMCRPi6yblgUisdW66fxnaCeIXQhyx1fKMQU7kOS-BdFIyf4NUv88_vT3yms2GrTC4-QiJejbBWr14gAQxwY2C1tEuomucBrQZw2U9-aBInOZHDOmjWqtEjLPSn8Rc3F4_xoL1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTbjiIGJh4i7in-Adlfe919CqkbA4xbNJVvXhUTFMm8lMCcjx1OLeJYU7l-Ve5JFlmKeZzU56B8sBCahUXXs-LqQAa9MAlV-2g1DlDHu99h7YuQtIMXRZufWQ9kpON-Kv_6acn-dS3KvA6BC7OjCWkeHcna0NvmGipniI5YYqv_ZT--F0DWIXnxL-o4WofCT_3YllUI70N-Ac815q7XE8cl8-0YgA6n2qCtj_xerfhjsaoi-UrmaQHsdRfGUgq6N6TSK4TK0aDHQn4G31mSn8a51C8ExMTIS0uwEYQ8KwjUxEq5sQjUaSwhav_n_D1SJFJ8041sr0nYrfoTsX5g5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6WqsJCAfICrUkj7_RTjfoX60jQhW862mLx-dvoUomcENG5erqGlNCvXHJdIEqUa6xCSgaRS2yvLICxBCR2Xs0mGI413m2t5j-koBeujnMN_Hg4tI7WTab2ySf5n61pGl1PaxWuDWRFzY5UfZ477Y1TXKI8eNR-Hy5it1tOCfFPsbg6IwV_R_KC9F--B78SV_kewzqBAG3lL_IXp0-HP494Pc8eK_AEVRTD_t8Hpcf_XpclQwSe6VTVQ6m4X0o8BP6qJ4Fl060pH9aVo1Qg8eOLRtXUGhJaSBOrM8i_UTfPbIcLzKIJOyeD1wKWAXASjCaPb6Kc89KJaTaYOQ1zl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjbdLHwCCrkMT3f_6ZCkPSaQhCzbkN_C5J_gqml9mDxAtZzHYHpih9dGo73b255rp0b9X-wuGqxuT2UkHnfwYAj5QdpnQvvvTSrWadLu53vasf0cE7Z6HesKQ8YciSE0ZcPiTSNFPgHCwn4tsrDWMEEZsrVUshjyZVcKMCGaONVLRJ6s_b7WGAx55lmiWSF7SZzNxlxqH7vE_0jfbhXzx51sXZSerc0gh9tVET_IOi1ZdtTvIB8zZMS9wOhj_CI69rdlnESAHqAGzy_qVoLGW1Iwrl_d6gQQ8afmTGQ3_mgFuP29Ar56w5RtkTf9h35ZRvpvrueSbC3cuftikTpGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=SwHShrPVdDvXRBiY-0CHZuxDUIV_tZdQX7g67Bivdyey9XrCWU3Ey4pO79SY05gEoqf6iBTCTrw_zWpWGXFeDMqZjJzcu9KqBbLcgwMffVfRieMU5rQy2VNwJldr3z9f0LKIQhXDJFVn57UnudHhLHA_S0nQRYHdJNJdv-O_Yf7XcjVyUv7ANCI7iUVcmJBUDBujWdK3OilgFBq5xQOesvXAk45_jPeVQui_kyTPszA5YQJI7Oe7xA1X8yx59Hou0rD0GF6lV0r6JsxIJMVL46rgS-y3CZIoj__mqAhuV894k_ZM2zDZtsS3CHhI57RHhXuCb9GoLASqb7o41AKtBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=SwHShrPVdDvXRBiY-0CHZuxDUIV_tZdQX7g67Bivdyey9XrCWU3Ey4pO79SY05gEoqf6iBTCTrw_zWpWGXFeDMqZjJzcu9KqBbLcgwMffVfRieMU5rQy2VNwJldr3z9f0LKIQhXDJFVn57UnudHhLHA_S0nQRYHdJNJdv-O_Yf7XcjVyUv7ANCI7iUVcmJBUDBujWdK3OilgFBq5xQOesvXAk45_jPeVQui_kyTPszA5YQJI7Oe7xA1X8yx59Hou0rD0GF6lV0r6JsxIJMVL46rgS-y3CZIoj__mqAhuV894k_ZM2zDZtsS3CHhI57RHhXuCb9GoLASqb7o41AKtBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
